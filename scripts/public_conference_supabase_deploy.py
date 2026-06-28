#!/usr/bin/env python
"""Apply and verify public-conference Supabase SQL.

默认只打印执行计划；只有传入 --yes 时才会调用生产 Supabase Management API。
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Iterable, List
from urllib.parse import urlparse

import requests


ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from local_env import load_local_env


CONFERENCE_TABLES = {
    "osdi": "osdi_papers",
    "sosp": "sosp_papers",
    "ieee_sp": "ieee_sp_papers",
    "ndss": "ndss_papers",
}

SQL_FILES = [
    "create_osdi_papers_schema.sql",
    "create_sosp_papers_schema.sql",
    "create_ieee_sp_papers_schema.sql",
    "create_ndss_papers_schema.sql",
    "match_osdi_papers.sql",
    "match_sosp_papers.sql",
    "match_ieee_sp_papers.sql",
    "match_ndss_papers.sql",
    "enable_conference_anon_read_policies.sql",
]


def _norm(value: object) -> str:
    return str(value or "").strip()


def resolve_project_ref(supabase_url: str, explicit_ref: str = "") -> str:
    direct = _norm(explicit_ref)
    if direct:
        return direct
    host = urlparse(_norm(supabase_url)).hostname or ""
    suffix = ".supabase.co"
    if host.endswith(suffix):
        return host[: -len(suffix)]
    return ""


def sql_paths(names: Iterable[str] = SQL_FILES) -> List[Path]:
    return [ROOT_DIR / "sql" / name for name in names]


def validate_sql_files(paths: Iterable[Path]) -> None:
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("缺少 SQL 文件：" + ", ".join(missing))


def management_query_url(project_ref: str, *, read_only: bool = False) -> str:
    suffix = "/read-only" if read_only else ""
    return f"https://api.supabase.com/v1/projects/{project_ref}/database/query{suffix}"


def run_management_query(
    *,
    project_ref: str,
    access_token: str,
    query: str,
    read_only: bool = False,
    timeout: int = 120,
) -> object:
    url = management_query_url(project_ref, read_only=read_only)
    body = {"query": query}
    if not read_only:
        body["read_only"] = False
    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        json=body,
        timeout=timeout,
    )
    response.raise_for_status()
    if not response.text:
        return None
    try:
        return response.json()
    except ValueError:
        return response.text


def apply_sql_files(*, project_ref: str, access_token: str, paths: Iterable[Path], timeout: int = 120) -> None:
    for path in paths:
        sql = path.read_text(encoding="utf-8")
        print(f"[sql] apply {path.relative_to(ROOT_DIR)}", flush=True)
        run_management_query(project_ref=project_ref, access_token=access_token, query=sql, timeout=timeout)


def print_sync_commands(raw_dir: str = "/tmp/dpr_public_conference", run_date: str = "20260629") -> None:
    for key, table in CONFERENCE_TABLES.items():
        raw_path = Path(raw_dir) / f"{key}.json"
        print(
            "PYTHONPATH=src python src/maintain/sync.py "
            f"--backend-key {key} "
            f"--date {run_date} "
            f"--schema public "
            f"--raw-input {raw_path} "
            f"--papers-table {table} "
            "--embed-device cpu "
            "--embed-batch-size 8 "
            "--embed-chunk-size 512 "
            "--stream-upsert "
            "--upload-workers 2"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply public-conference Supabase SQL and print sync commands.")
    parser.add_argument("--yes", action="store_true", help="真正执行 SQL。默认只 dry-run。")
    parser.add_argument("--project-ref", default=os.getenv("SUPABASE_PROJECT_REF", ""))
    parser.add_argument("--supabase-url", default=os.getenv("SUPABASE_URL", ""))
    parser.add_argument("--access-token", default=os.getenv("SUPABASE_ACCESS_TOKEN", ""))
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--print-sync-commands", action="store_true")
    args = parser.parse_args()

    load_local_env()
    supabase_url = _norm(args.supabase_url or os.getenv("SUPABASE_URL"))
    access_token = _norm(args.access_token or os.getenv("SUPABASE_ACCESS_TOKEN"))
    project_ref = resolve_project_ref(supabase_url, args.project_ref or os.getenv("SUPABASE_PROJECT_REF", ""))
    paths = sql_paths()
    validate_sql_files(paths)

    print(f"[plan] project_ref={project_ref or '<missing>'}")
    print("[plan] SQL files:")
    for path in paths:
        print(f"  - {path.relative_to(ROOT_DIR)}")

    if args.print_sync_commands:
        print("[plan] sync commands:")
        print_sync_commands()

    if not args.yes:
        print("[dry-run] 未传入 --yes，不调用 Supabase API。")
        return
    if not project_ref or not access_token:
        raise SystemExit("缺少 SUPABASE_PROJECT_REF/SUPABASE_URL 或 SUPABASE_ACCESS_TOKEN")

    apply_sql_files(project_ref=project_ref, access_token=access_token, paths=paths, timeout=args.timeout)
    print("[done] SQL applied")


if __name__ == "__main__":
    main()
