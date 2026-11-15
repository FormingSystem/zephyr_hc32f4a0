# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Verify explicit chapter navigation anchors without scanning upstream documents."""

import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location(
    "learning_check_docs", Path(__file__).resolve().parents[2] / "learning/check_docs.py"
)
check_docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_docs)


class LearningDocLinksTest(unittest.TestCase):
    def check_document(self, link, target=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "README.md"
            source.write_text(link, encoding="utf-8")
            if target is not None:
                (root / "chapter.md").write_text(target, encoding="utf-8")
            output = io.StringIO()
            with patch.object(check_docs, "ROOT", root), \
                    patch.object(check_docs, "files", return_value=iter([source])), \
                    contextlib.redirect_stdout(output):
                result = check_docs.main()
            return result, output.getvalue()

    def test_local_and_cross_file_explicit_anchors(self):
        result, _ = self.check_document(
            '<a id="local"></a>\n\n[本章](#local)\n[下一章](chapter.md#next)\n',
            "<a id='next'></a>\n\n## 1.1\\_下一章\n",
        )
        self.assertFalse(result)

    def test_missing_local_anchor_is_reported(self):
        result, output = self.check_document("[本章](#missing)\n")
        self.assertTrue(result)
        self.assertIn("#missing", output)

    def test_missing_cross_file_anchor_is_reported(self):
        result, output = self.check_document(
            "[下一章](chapter.md#missing)\n", '<a id="present"></a>\n'
        )
        self.assertTrue(result)
        self.assertIn("chapter.md#missing", output)

    def test_legacy_heading_links_and_missing_files(self):
        result, _ = self.check_document("[下一章](chapter.md#标题)\n", "# 标题\n")
        self.assertFalse(result)
        result, output = self.check_document("[下一章](missing.md)\n")
        self.assertTrue(result)
        self.assertIn("失效链接", output)
