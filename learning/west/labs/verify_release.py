# SPDX-License-Identifier: Apache-2.0
"""检查 P05 的固定教学组合；只读，不替读者同步或恢复。"""
from pathlib import Path  # 读取文件，并比较当前目录与工作区根目录。
import subprocess  # 运行已有的 west、Git 和应用程序。
import sys  # 用 sys.executable 继续使用当前 Python。


def output(*args):
    # 收集命令及参数，执行后取回文字；命令失败时异常会中止检查。
    return subprocess.check_output(args, text=True).strip()



# 先确认站对地方，后面的 app、libs、tools 都从这里查找。
workspace = Path(output("west", "topdir")).resolve()
assert workspace == Path.cwd().resolve(), "Run from the experiment workspace"

# 本次实验明确接受的组合；键是项目名，值是清单中的版本文字。
expected = {"app": "v1.0", "arithmetic": "v2.0", "checklist": "v2.0"}
# 每行用 | 分隔名称、路径和版本，splitlines() 再把输出拆成多行。
rows = output("west", "list", "-f", "{name}|{path}|{revision}").splitlines()
seen = set()  # 用集合记下已检查的项目，最后发现遗漏。
for row in rows:
    name, path, revision = row.split("|")  # 按顺序取出这一行的三个字段。
    # 顶层清单仓库不在本例的三个依赖中，跳过它。
    if name == "manifest":
        continue
    assert name in expected, f"Unexpected active project: {name}"
    assert revision == expected[name], f"Unexpected declared version: {name}"
    # 分别问 Git：现在在哪、上次同步基线在哪、声明的标签指向哪。
    head = output("git", "-C", path, "rev-parse", "HEAD")
    baseline = output("git", "-C", path, "rev-parse", "manifest-rev")
    wanted = output("git", "-C", path, "rev-parse", revision + "^{commit}")
    assert head == baseline == wanted, f"Version mismatch: {name}"
    seen.add(name)  # 本项目所有版本检查通过后，才记为已检查。

# 逐个检查没有发现多余项目，还要反向确认预期的项目一个没少。
assert seen == set(expected), "Missing active project"
# 版本一致后，实际运行应用，并读取第二版检查表中的新增内容。
assert output(sys.executable, "app/main.py") == "2 + 3 = 5", "Unexpected application output"
checklist = Path("tools/checklist/README.md").read_text(encoding="utf-8")
assert "Recreate dependencies in a fresh workspace." in checklist, "Missing release check"
print("PASS: active projects, declared versions, Git commits, application and checklist")
