# SPDX-License-Identifier: Apache-2.0
"""检查 P05 的固定教学组合；只读，不替读者同步或恢复。"""
from pathlib import Path
import subprocess
import sys


def output(*args):
    return subprocess.check_output(args, text=True).strip()


workspace = Path(output("west", "topdir")).resolve()
assert workspace == Path.cwd().resolve(), "Run from the experiment workspace"

expected = {"app": "v1.0", "arithmetic": "v2.0", "checklist": "v2.0"}
rows = output("west", "list", "-f", "{name}|{path}|{revision}").splitlines()
seen = set()
for row in rows:
    name, path, revision = row.split("|")
    if name == "manifest":
        continue
    assert name in expected, f"Unexpected active project: {name}"
    assert revision == expected[name], f"Unexpected declared version: {name}"
    head = output("git", "-C", path, "rev-parse", "HEAD")
    baseline = output("git", "-C", path, "rev-parse", "manifest-rev")
    wanted = output("git", "-C", path, "rev-parse", revision + "^{commit}")
    assert head == baseline == wanted, f"Version mismatch: {name}"
    seen.add(name)

assert seen == set(expected), "Missing active project"
assert output(sys.executable, "app/main.py") == "2 + 3 = 5", "Unexpected application output"
checklist = Path("tools/checklist/README.md").read_text(encoding="utf-8")
assert "Recreate dependencies in a fresh workspace." in checklist, "Missing release check"
print("PASS: active projects, declared versions, Git commits, application and checklist")
