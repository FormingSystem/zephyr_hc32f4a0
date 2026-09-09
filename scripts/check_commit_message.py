#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026 FormingSystem
# SPDX-License-Identifier: Apache-2.0
"""Validate the project's Chinese commit convention without modifying messages."""

import argparse
from pathlib import Path
import re
import sys


commit_types = (
    "feat|fix|refactor|perf|security|content|docs|test|build|ci|release|revert|chore"
)
scope_pattern = r"[^/()\s:]+(?:/[^/()\s:]+)?"
subject_pattern = re.compile(
    rf"(?:{commit_types})(?:\({scope_pattern}\))?!?: (?P<description>\S.*)"
)
signed_off_pattern = re.compile(r"Signed-off-by: [^<>\s][^<>]* <[^<>\s@]+@[^<>\s@]+>")
assisted_by_pattern = re.compile(r"Assisted-by: [^\s:]+:[^\s:]+(?: [^\s]+)*")
han_ranges = (
    (0x3400, 0x4DBF),
    (0x4E00, 0x9FFF),
    (0xF900, 0xFAFF),
    (0x20000, 0x2FA1F),
    (0x30000, 0x323AF),
)


def contains_han(text: str) -> bool:
    """Accept a Han character, rather than any non-ASCII byte."""
    return any(start <= ord(character) <= end for character in text for start, end in han_ranges)


def validate_message(message: str) -> list[str]:
    """Return actionable errors; allow manual sign-offs and one assistance trailer."""
    lines = [line.rstrip() for line in message.splitlines() if not line.lstrip().startswith("#")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    if not lines:
        return ["提交信息不能为空。"]

    errors = []
    subject_match = subject_pattern.fullmatch(lines[0])
    if subject_match is None:
        errors.append("标题格式：<类型>[(项目[/模块])]!?: <中文结果>。")
    elif not contains_han(subject_match.group("description")):
        errors.append("提交标题的结果说明必须包含汉字；重音字母或表情不能替代中文。")

    in_trailers = False
    assistance_count = 0
    for line_number, line in enumerate(lines[1:], start=2):
        if not line:
            if in_trailers:
                errors.append(f"第 {line_number} 行：提交尾注必须组成末尾连续段落。")
            continue
        if line.startswith(("Signed-off-by:", "Assisted-by:")):
            if not in_trailers and lines[line_number - 2]:
                errors.append(f"第 {line_number} 行：提交尾注前必须空一行。")
            in_trailers = True
            if line.startswith("Signed-off-by:"):
                if signed_off_pattern.fullmatch(line) is None:
                    errors.append(f"第 {line_number} 行：Signed-off-by 格式应为姓名 <邮箱>。")
            else:
                assistance_count += 1
                if assisted_by_pattern.fullmatch(line) is None:
                    errors.append(f"第 {line_number} 行：Assisted-by 格式应为 Agent:model [tool ...]。")
            continue
        if in_trailers:
            errors.append(f"第 {line_number} 行：提交尾注之后不能再添加正文。")
        elif re.fullmatch(r"- \S.*", line) is None:
            errors.append(f"第 {line_number} 行：正文每行必须使用“- 描述”。")

    if assistance_count > 1:
        errors.append("Assisted-by 最多保留一行；人工独立提交可以不包含该尾注。")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("message_file", type=Path, help="Git commit message file")
    arguments = parser.parse_args()
    try:
        errors = validate_message(arguments.message_file.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError) as error:
        print(f"无法读取 UTF-8 提交信息：{error}", file=sys.stderr)
        return 1
    for error in errors:
        print(error, file=sys.stderr)
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
