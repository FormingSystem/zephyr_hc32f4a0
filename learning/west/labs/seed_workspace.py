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
# 从脚本位置计算教材根目录，不把调用者碰巧所在的目录当输出根。
LEARNING = LABS.parents[1]
REPO = LEARNING.parent


def git(directory, *args):
    """用局部身份和关闭签名的提交创建教学历史，不写全局配置。"""
    command = ["git", "-c", "user.name=Learning Lab",
               "-c", "user.email=learning@example.invalid",
               "-c", "commit.gpgsign=false", "-c", "tag.gpgsign=false",
               "-c", "core.hooksPath=", "-C", str(directory), *args]
    # 参数列表直接启动 Git；-C 选择新建的实验仓库，失败抛 CalledProcessError。
    return subprocess.check_output(command, text=True, encoding="utf-8").strip()


def write(directory, name, content):
    """创建父目录并写 UTF-8 文件；本函数不创建 Git 提交。"""
    path = directory / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def commit(directory, message):
    """只在刚创建的实验仓库中暂存文件、提交，并返回实际 HEAD 的 SHA。"""
    git(directory, "add", ".")
    git(directory, "commit", "-m", message)
    return git(directory, "rev-parse", "HEAD")


def new_repo(directory):
    """目录先存在，Git 再初始化；main 是实验约定的初始分支名。"""
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
    # 第一阶段准备发布来源：同一个库先后产生两次提交与对应标签。
    write(arithmetic, "arithmetic.py", '"""第一版：整数相加。"""\n\n# 定义加法函数；这里只描述做法，真正调用时才执行 return。\ndef add(a, b):\n    # 把计算结果交回调用者，不在库里直接打印。\n    return a + b\n')
    v1 = commit(arithmetic, "Add arithmetic v1")
    git(arithmetic, "tag", "v1.0")
    write(arithmetic, "arithmetic.py", '"""第二版：保留加法，增加乘法。"""\n\n# 保留第一版的接口，原来的 app/main.py 仍可以调用它。\ndef add(a, b):\n    return a + b\n\n# 第二版新增的接口，用不同结果证明我们确实取得了新代码。\ndef multiply(a, b):\n    return a * b\n')
    v2 = commit(arithmetic, "Add multiplication in v2")
    git(arithmetic, "tag", "v2.0")
    new_repo(app)
    write(app, "main.py", '''"""直接读取相邻仓库中的教学代码，不安装 Python 包。"""
# sys 提供当前解释器的模块搜索路径。
import sys
# Path 用来按目录层次计算位置，避免写死本机盘符。
from pathlib import Path

# 从 app/main.py 回到 workspace，再找到相邻的库目录。
# insert(0, ...) 把这个目录放到本次 Python 进程的搜索路径最前面。
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "libs" / "arithmetic"))
# 在刚加入的目录里找到 arithmetic.py，取出 add 函数。
from arithmetic import add

# 先计算 add(2, 3)，再把结果填进文字并显示。
print(f"2 + 3 = {add(2, 3)}")
''')
    commit(app, "Add arithmetic client")
    git(app, "tag", "v1.0")
    new_repo(guide)
    write(guide, "README.md", "# Optional guide\n\nThis repository demonstrates a project group.\n")
    commit(guide, "Add optional guide")
    git(guide, "tag", "v1.0")
    manifest = root / "workspace" / "manifest"
    # 第二阶段准备清单仓库。复制扩展源码并不执行它，也不克隆受管依赖。
    new_repo(manifest)
    template = (LABS / "templates" / "west.yml.in").read_text(encoding="utf-8")
    write(manifest, "west.yml", template)
    shutil.copy2(LABS / "templates" / "west-commands.yml", manifest)
    shutil.copytree(LABS / "templates" / "commands", manifest / "commands",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    write(manifest, ".gitignore", "__pycache__/\n*.py[cod]\n")
    commit(manifest, "Record the initial repository set")
    # JSON 只记录教材证据；west 选择版本时读取 west.yml，不读本文件。
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
