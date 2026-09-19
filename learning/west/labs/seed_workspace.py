# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""生成本地实验用 Git 仓库；不运行 west，不修改已有目标。"""

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


LABS = Path(__file__).resolve().parent
LEARNING = LABS.parents[1]
REPO = LEARNING.parent


def git(directory, *args):
    """用局部身份和关闭签名的提交创建教学历史，不写全局配置。"""
    command = ["git", "-c", "user.name=Learning Lab",
               "-c", "user.email=learning@example.invalid",
               "-c", "commit.gpgsign=false", "-c", "tag.gpgsign=false",
               "-c", "core.hooksPath=", "-C", str(directory), *args]
    return subprocess.check_output(command, text=True, encoding="utf-8").strip()


def write(directory, name, content):
    path = directory / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def commit(directory, message):
    git(directory, "add", ".")
    git(directory, "commit", "-m", message)
    return git(directory, "rev-parse", "HEAD")


def new_repo(directory):
    directory.mkdir(parents=True)
    git(directory, "init", "-b", "main")


def seed(name):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", name):
        raise ValueError("实验名只能含英文字母、数字、连字符和下划线")
    root = REPO / "build" / "learning-tools" / "west" / name
    # 已有目录一律拒绝，避免覆盖读者的练习与提交。
    root.mkdir(parents=True, exist_ok=False)
    remotes = root / "remotes"
    arithmetic = remotes / "arithmetic"
    app = remotes / "app"
    guide = remotes / "guide"
    new_repo(arithmetic)
    write(arithmetic, "arithmetic.py", '"""第一版：整数相加。"""\n\ndef add(a, b):\n    return a + b\n')
    v1 = commit(arithmetic, "Add arithmetic v1")
    git(arithmetic, "tag", "v1.0")
    write(arithmetic, "arithmetic.py", '"""第二版：保留加法，增加乘法。"""\n\ndef add(a, b):\n    return a + b\n\ndef multiply(a, b):\n    return a * b\n')
    v2 = commit(arithmetic, "Add multiplication in v2")
    git(arithmetic, "tag", "v2.0")
    new_repo(app)
    write(app, "main.py", '''"""直接读取相邻仓库中的教学代码，不安装 Python 包。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "libs" / "arithmetic"))
from arithmetic import add

print(f"2 + 3 = {add(2, 3)}")
''')
    commit(app, "Add arithmetic client")
    git(app, "tag", "v1.0")
    new_repo(guide)
    write(guide, "README.md", "# Optional guide\n\nThis repository demonstrates a project group.\n")
    commit(guide, "Add optional guide")
    git(guide, "tag", "v1.0")
    manifest = root / "workspace" / "manifest"
    new_repo(manifest)
    template = (LABS / "templates" / "west.yml.in").read_text(encoding="utf-8")
    write(manifest, "west.yml", template)
    shutil.copy2(LABS / "templates" / "west-commands.yml", manifest)
    shutil.copytree(LABS / "templates" / "commands", manifest / "commands",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    write(manifest, ".gitignore", "__pycache__/\n*.py[cod]\n")
    commit(manifest, "Record the initial repository set")
    write(root, "revisions.json", json.dumps({"arithmetic_v1": v1, "arithmetic_v2": v2}, indent=2) + "\n")
    print(f"Prepared: {root.relative_to(REPO).as_posix()}")
    print(f"Next (from repository root): cd {manifest.parent.relative_to(REPO).as_posix()}")
    print("Then: python ../../../../../learning/west/labs/init_workspace.py -l manifest")
    print("Without an enclosing workspace, plain west init -l manifest also works.")
    print("Then: west update")
    return root


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", default="demo-01", help="新实验目录名；已存在时拒绝覆盖")
    args = parser.parse_args()
    if not shutil.which("git"):
        parser.error("找不到 git；请先安装 Git 并重新打开终端")
    try:
        seed(args.name)
    except (FileExistsError, ValueError) as error:
        parser.exit(2, f"{error}\n请保留已有目录，换一个 --name 重试。\n")
    except subprocess.CalledProcessError as error:
        parser.exit(1, f"Git 执行失败：{error}\n已生成内容保留在实验目录，检查后换名重试。\n")


if __name__ == "__main__":
    main()
