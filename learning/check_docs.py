# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""检查本仓库教材的本地链接、章节编号、元信息和实验源码语法。"""

import ast
import os
import re
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", ".work", "__pycache__", "build", "dist"}


def files():
    for relative in ("README.md", "project-docs/README.md", "project-docs/development.md",
                     "project-docs/environment.md", "project-docs/distribution.md",
                     "project-docs/python/venv/README.md", "project-docs/west/README.md",
                     "project-docs/learning/environment/P01_可复现的开发环境.md"):
        yield ROOT / relative
    for directory, names, filenames in os.walk(ROOT / "learning"):
        names[:] = [name for name in names if name not in SKIP and not name.endswith(".egg-info")]
        for name in filenames:
            yield Path(directory) / name


def main():
    errors = []
    identifiers = {}
    documents = 0
    sources = 0
    chapters = 0
    for path in files():
        if path.suffix == ".py":
            sources += 1
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            except SyntaxError as error:
                errors.append(f"{path.relative_to(ROOT)}: {error}")
        if path.suffix == ".toml":
            tomllib.loads(path.read_text(encoding="utf-8"))
        if path.suffix != ".md":
            continue
        documents += 1
        body = path.read_text(encoding="utf-8")
        chapter = re.match(r"P(\d+)_", path.name) if path.is_relative_to(ROOT / "learning") else None
        if chapter:
            chapters += 1
            number = int(chapter.group(1))
            if not re.search(rf"^# {number}\. \S", body, re.M):
                errors.append(f"{path.name}: 章编号与文件名不一致")
            sections = re.findall(rf"^## {number}\.(\d+) ", body, re.M)
            if list(map(int, sections)) != list(range(1, len(sections) + 1)):
                errors.append(f"{path.name}: 小节编号不连续")
            for key in ("id", "title", "kind", "status", "domains"):
                if not re.search(rf"^{key}: .+", body, re.M):
                    errors.append(f"{path.name}: 缺少 {key}")
            if number > 0:
                siblings = sorted(path.parent.glob("P[0-9][0-9]_*.md"))
                position = siblings.index(path)
                for neighbor in (position - 1, position + 1):
                    if 0 <= neighbor < len(siblings) and f"]({siblings[neighbor].name})" not in body:
                        errors.append(f"{path.name}: 缺少相邻章节链接 {siblings[neighbor].name}")
        match = re.search(r"^id: (.+)$", body, re.M)
        if match:
            identifier = match.group(1)
            if identifier in identifiers:
                errors.append(f"{path.name}: id 重复 {identifier}")
            identifiers[identifier] = path
        if len(re.findall(r"^```", body, re.M)) % 2:
            errors.append(f"{path.name}: 代码围栏未闭合")
        # 本仓库正文没有带括号的本地文件名；排除代码块中的说明性文本。
        visible = re.sub(r"```.*?```", "", body, flags=re.S)
        for target in re.findall(r"\]\(([^)]+)\)", visible):
            target = target.strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            filename, _, anchor = unquote(target).partition("#")
            linked = path.parent / filename
            if not linked.exists():
                errors.append(f"{path.relative_to(ROOT)}: 失效链接 {target}")
            elif anchor and linked.suffix == ".md":
                headings = re.findall(r"^#+ (.+)$", linked.read_text(encoding="utf-8"), re.M)
                if anchor not in headings:
                    errors.append(f"{path.name}: 无目标标题 {target}")
        for line_number, line in enumerate(body.splitlines(), 1):
            if line.rstrip() != line and not line.endswith("  "):
                errors.append(f"{path.name}:{line_number}: 意外行末空白")
    print(f"documents={documents}, chapters={chapters}, python_sources={sources}, ids={len(identifiers)}")
    for error in errors:
        print(f"ERROR {error}")
    print(f"errors={len(errors)}")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
