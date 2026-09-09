# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Check import exemptions against real temporary Git indexes and working trees."""

from contextlib import redirect_stdout
import importlib.util
from io import StringIO
from pathlib import Path
import subprocess
import tempfile
import unittest


source = Path(__file__).resolve().parents[2] / "scripts/check_project_diff.py"
spec = importlib.util.spec_from_file_location("hc32_diff_check", source)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class ProjectDiffTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="hc32-diff-")
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name).resolve()
        self.git("init", "--quiet")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "core.hooksPath", "no-hooks")
        self.git("config", "user.name", "Diff Fixture")
        self.git("config", "user.email", "diff@example.invalid")
        self.git("config", "core.whitespace", "blank-at-eol,blank-at-eof,space-before-tab")
        self.write("seed.txt", "initial\n")
        self.git("add", "--", "seed.txt")
        self.git("commit", "--quiet", "-m", "initial fixture")

    def git(self, *args):
        result = subprocess.run(
            ["git", "-C", str(self.repo), *args], check=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            encoding="utf-8", errors="replace",
        )
        return result.stdout

    def write(self, relative, content):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def import_source(self, relative="upstream.c", content="upstream text  \n"):
        self.write(relative, content)
        self.git("add", "--", relative)
        header = self.git("ls-files", "--stage", "--", relative).split("\t", 1)[0]
        mode, blob, _ = header.split(" ")
        self.write(str(checker.MANIFEST),
                   "# SPDX-FileCopyrightText: fixture\n# SPDX-License-Identifier: Apache-2.0\n\n"
                   f"{mode}\t{blob}\t{relative}\n")

    def check(self):
        output = StringIO()
        with redirect_stdout(output):
            result = checker.check_repository(self.repo)
        return result, output.getvalue()

    def test_identical_new_import_can_keep_original_whitespace(self):
        self.import_source()
        result, output = self.check()
        self.assertEqual(result, 0)
        self.assertIn("unchanged baseline additions): 1", output)
        self.assertIn("Local changed paths checked: 0", output)

    def test_modified_import_is_not_exempt(self):
        self.import_source()
        self.write("upstream.c", "local modification  \n")
        self.git("add", "--", "upstream.c")
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("unchanged baseline additions): 0", output)

    def test_new_local_file_is_checked(self):
        self.import_source()
        self.write("local.c", "new local code  \n")
        self.git("add", "--", "local.c")
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("local.c", output)
        self.assertIn("unchanged baseline additions): 1", output)

    def test_unstaged_edit_disqualifies_original_import(self):
        self.import_source(content="clean upstream\n")
        self.write("upstream.c", "unstaged modification  \n")
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("unchanged baseline additions): 0", output)
        self.assertIn("unstaged 1", output)

    def test_unstaged_edit_to_head_file_is_checked(self):
        self.write("seed.txt", "modified unstaged  \n")
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("seed.txt", output)

    def test_existing_head_path_matching_manifest_is_not_an_import(self):
        self.import_source(relative="seed.txt")
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("unchanged baseline additions): 0", output)

    def test_literal_pathspec_checks_names_with_glob_characters(self):
        self.write("local[1].c", "local code  \n")
        self.git("add", "--", "local[1].c")
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("local[1].c", output)

    def test_missing_manifest_does_not_skip_source_files(self):
        self.write("upstream.c", "upstream text  \n")
        self.git("add", "--", "upstream.c")
        result, output = self.check()
        self.assertEqual(result, 1)
        self.assertIn("unchanged baseline additions): 0", output)


if __name__ == "__main__":
    unittest.main()
