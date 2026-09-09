#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Check local diffs without reformatting byte-identical upstream source imports."""

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path("governance/architecture/source-manifest.tsv")
BATCH_SIZE = 50


def git(root, *args, check=True):
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        encoding="utf-8", errors="surrogateescape",
    )
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or
                           f"git {' '.join(args)} failed with status {result.returncode}")
    return result


def read_manifest(path):
    """Return provenance objects; a missing manifest gives no exemptions."""
    if not path.is_file():
        return {}
    entries = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        fields = line.split("\t", 2)
        if (len(fields) != 3 or not re.fullmatch(r"[0-7]{6}", fields[0]) or
                not re.fullmatch(r"[0-9a-f]{40}", fields[1]) or not fields[2]):
            raise RuntimeError(f"Invalid source manifest entry at {path}:{number}")
        mode, blob, relative = fields
        if relative in entries:
            raise RuntimeError(f"Duplicate source manifest path at {path}:{number}")
        entries[relative] = (mode, blob)
    return entries


def staged_status(root):
    """Disable rename detection so only actual additions can be exempted."""
    fields = git(root, "diff", "--cached", "--name-status", "--no-renames", "-z").stdout.split("\0")
    fields = fields[:-1] if fields[-1] == "" else fields
    if len(fields) % 2:
        raise RuntimeError("Unexpected staged Git status output")
    return dict(zip(fields[1::2], fields[::2]))


def index_entries(root):
    entries = {}
    for record in git(root, "ls-files", "--stage", "-z").stdout.split("\0"):
        if not record:
            continue
        header, relative = record.split("\t", 1)
        mode, blob, stage = header.split(" ")
        if stage == "0":
            entries[relative] = (mode, blob)
    return entries


def check_batches(root, paths, *, cached):
    failures = False
    ordered = sorted(paths)
    for offset in range(0, len(ordered), BATCH_SIZE):
        # Literal pathspecs also handle brackets, glob characters and leading ':'.
        paths_batch = [f":(literal){path}" for path in ordered[offset:offset + BATCH_SIZE]]
        args = ["diff", "--no-ext-diff", "--no-renames", "--check"]
        if cached:
            args.append("--cached")
        result = git(root, *args, "--", *paths_batch, check=False)
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
        failures |= result.returncode != 0
    return failures


def check_repository(root):
    root = root.resolve()
    actual_root = Path(git(root, "rev-parse", "--show-toplevel").stdout.strip()).resolve()
    if actual_root != root:
        raise RuntimeError(f"Refusing to check enclosing repository: {actual_root}")
    baseline = read_manifest(root / MANIFEST)
    staged = staged_status(root)
    unstaged = set(filter(None, git(root, "diff", "--name-only", "--no-renames", "-z")
                          .stdout.split("\0")))
    indexed = index_entries(root)
    skipped = {
        path for path, status in staged.items()
        if status == "A" and path not in unstaged and path in baseline
        and indexed.get(path) == baseline[path]
    }
    local_staged = set(staged) - skipped
    local_changes = local_staged | unstaged
    print(f"Source imports skipped (unchanged baseline additions): {len(skipped)}")
    print(f"Local changed paths checked: {len(local_changes)} "
          f"(staged {len(local_staged)}, unstaged {len(unstaged)})")
    # Both views must be checked: working-tree edits do not excuse staged errors.
    failed = check_batches(root, local_staged, cached=True)
    failed |= check_batches(root, unstaged, cached=False)
    if not failed:
        print("PASS: local diffs; imported-source identity is audited separately")
    return 1 if failed else 0


def main():
    try:
        return check_repository(ROOT)
    except (OSError, RuntimeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
