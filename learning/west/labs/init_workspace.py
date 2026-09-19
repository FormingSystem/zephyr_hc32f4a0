# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""从工作区外运行 west init，避免外层 .west 抢先被发现。"""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

LAB_ROOT = Path(__file__).resolve().parents[3] / "build" / "learning-tools" / "west"


def local_path(value):
    path = Path(value).resolve()
    if not path.is_relative_to(LAB_ROOT.resolve()):
        raise ValueError("初始化目标与源仓库必须在 build/learning-tools/west 内")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("-l", "--local", action="store_true")
    mode.add_argument("-m", "--manifest-url")
    parser.add_argument("--mr", default=None)
    parser.add_argument("directory")
    args = parser.parse_args()
    destination = local_path(args.directory)
    command = [sys.executable, "-m", "west", "init"]
    if args.local:
        if args.mr:
            parser.error("-l 不能与 --mr 同用")
        if not (destination / "west.yml").is_file():
            parser.error("本地清单目录缺少 west.yml")
        workspace = destination.parent
        command += ["-l", str(destination)]
    else:
        source = local_path(args.manifest_url)
        if not source.is_dir():
            parser.error("本地清单来源不存在")
        workspace = destination
        if workspace.exists():
            parser.error("远端模式的目标必须尚不存在")
        command += ["-m", str(source)]
        if args.mr:
            command += ["--mr", args.mr]
        command.append(str(destination))
    if (workspace / ".west").exists():
        parser.error("目标工作区已经初始化；不覆盖 .west")
    env = os.environ.copy()
    for key in list(env):
        if key == "ZEPHYR_BASE" or key.startswith("WEST_CONFIG_"):
            env.pop(key)
    # -m 还检查目标的祖先，因此先在中立目录初始化，再转入受限实验目录。
    with tempfile.TemporaryDirectory(prefix="west-init-cwd-") as neutral:
        temporary = Path(neutral).resolve()
        if not temporary.is_relative_to(Path(tempfile.gettempdir()).resolve()):
            raise RuntimeError("临时目录位置异常")
        if any((parent / ".west").is_dir() for parent in (temporary, *temporary.parents)):
            raise RuntimeError("系统临时目录也位于 west 工作区内，请换独立临时目录")
        staged = temporary / "workspace"
        if not args.local:
            command[-1] = str(staged)
        print("Running west init outside the enclosing workspace", flush=True)
        subprocess.run(command, cwd=temporary, env=env, check=True)
        if not args.local:
            if (not staged.resolve().is_relative_to(temporary)
                    or not workspace.resolve().is_relative_to(LAB_ROOT.resolve())
                    or workspace.exists()):
                raise RuntimeError("拒绝转移：源或目标超出实验边界，或目标已存在")
            workspace.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(staged), str(workspace))


if __name__ == "__main__":
    main()
