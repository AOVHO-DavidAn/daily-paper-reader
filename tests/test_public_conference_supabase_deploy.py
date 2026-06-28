import importlib.util
import pathlib
import sys
import unittest
from unittest.mock import Mock, patch


def _load_module(module_name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    return mod


class PublicConferenceSupabaseDeployTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = pathlib.Path(__file__).resolve().parents[1]
        src_dir = root / "src"
        if str(src_dir) not in sys.path:
            sys.path.insert(0, str(src_dir))
        cls.mod = _load_module(
            "public_conference_supabase_deploy_mod",
            root / "scripts" / "public_conference_supabase_deploy.py",
        )

    def test_resolve_project_ref_from_supabase_url(self):
        self.assertEqual(
            self.mod.resolve_project_ref("https://lyucdwgefyfbmaiopjbk.supabase.co"),
            "lyucdwgefyfbmaiopjbk",
        )
        self.assertEqual(self.mod.resolve_project_ref("https://example.com", "manual-ref"), "manual-ref")

    def test_sql_plan_covers_four_public_conferences(self):
        names = [path.name for path in self.mod.sql_paths()]
        for conference in ["osdi", "sosp", "ieee_sp", "ndss"]:
            self.assertIn(f"create_{conference}_papers_schema.sql", names)
            self.assertIn(f"match_{conference}_papers.sql", names)
        self.assertIn("enable_conference_anon_read_policies.sql", names)

    def test_run_management_query_uses_beta_database_query_endpoint(self):
        response = Mock()
        response.text = '{"ok": true}'
        response.json.return_value = {"ok": True}
        response.raise_for_status.return_value = None
        with patch.object(self.mod.requests, "post", return_value=response) as post:
            result = self.mod.run_management_query(
                project_ref="project-ref",
                access_token="secret-token",
                query="select 1;",
            )
        self.assertEqual(result, {"ok": True})
        args, kwargs = post.call_args
        self.assertEqual(args[0], "https://api.supabase.com/v1/projects/project-ref/database/query")
        self.assertEqual(kwargs["headers"]["Authorization"], "Bearer secret-token")
        self.assertEqual(kwargs["json"], {"query": "select 1;", "read_only": False})


if __name__ == "__main__":
    unittest.main()
