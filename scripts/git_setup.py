#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026 FormingSystem
# SPDX-License-Identifier: Apache-2.0
"""Configure this independent repository's local Git workflow, or check it."""

import argparse
from pathlib import Path
import subprocess
import sys


git_settings = {
    "core.hooksPath": ".githooks",
    "commit.template": "governance/templates/git_commit_message.txt",
    "core.autocrlf": "false",
    "core.longpaths": "true",
    "pull.ff": "only",
    "fetch.prune": "true",
}


def run_git(repo_root: Path, *arguments: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo_root), *arguments],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def configure_repository(repo_root: Path, check_only: bool = False) -> int:
    """Never configure an enclosing Git repository if this directory lacks its own Git root."""
    repo_root = repo_root.resolve()
    if not (repo_root / ".git").exists():
        raise ValueError(f"独立仓库缺少 .git，拒绝配置父仓库：{repo_root}")
    result = run_git(repo_root, "rev-parse", "--show-toplevel")
    if result.returncode != 0 or Path(result.stdout.strip()).resolve() != repo_root:
        raise ValueError(f"Git 根目录与脚本所属仓库不一致：{repo_root}")
    for relative_path in (
        ".githooks/commit-msg",
        "governance/templates/git_commit_message.txt",
    ):
        if not (repo_root / relative_path).is_file():
            raise ValueError(f"缺少仓库基础文件：{relative_path}")

    mismatches = 0
    for name, expected in git_settings.items():
        current = run_git(repo_root, "config", "--local", "--get-all", name)
        if current.returncode not in (0, 1):
            raise ValueError(current.stderr.strip())
        if current.stdout.splitlines() == [expected]:
            continue
        if check_only:
            print(f"未配置：{name} = {expected}")
            mismatches += 1
        else:
            result = run_git(repo_root, "config", "--local", "--replace-all", name, expected)
            if result.returncode != 0:
                raise ValueError(result.stderr.strip())
    if not mismatches:
        print("Git 本地配置已就绪；用户身份与远程连接保持原值。")
    return int(bool(mismatches))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without modifying Git config")
    arguments = parser.parse_args()
    try:
        return configure_repository(Path(__file__).resolve().parents[1], arguments.check)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
