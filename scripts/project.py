#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Repository-local entry points; dependencies are discovered, never installed."""

import argparse
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
LOCK = json.loads((ROOT / "dependencies.lock.json").read_text(encoding="utf-8"))


def run(args, *, env=None, capture=False):
    print("+ " + " ".join(map(str, args)), flush=True)
    return subprocess.run(
        list(map(str, args)), cwd=ROOT, env=env, check=True,
        stdout=subprocess.PIPE if capture else None,
        encoding="utf-8", errors="replace",
    )


def environment():
    env = os.environ.copy()
    zephyr = Path(env.get("ZEPHYR_BASE", ROOT.parent)).resolve()
    if not (zephyr / "VERSION").is_file() or not (zephyr / "west.yml").is_file():
        raise RuntimeError("Set ZEPHYR_BASE to the prepared Zephyr source directory")
    sdk = Path(env.get("ZEPHYR_SDK_INSTALL_DIR",
                       zephyr.parent.parent / f"zephyr-sdk-{LOCK['sdk']['version']}"))
    if not (sdk / "sdk_version").is_file():
        raise RuntimeError("Set ZEPHYR_SDK_INSTALL_DIR to the prepared Zephyr SDK")
    env["ZEPHYR_BASE"] = str(zephyr)
    env["ZEPHYR_SDK_INSTALL_DIR"] = str(sdk.resolve())
    env["ZEPHYR_TOOLCHAIN_VARIANT"] = "zephyr"
    extras = [str(ROOT)] + env.get("EXTRA_ZEPHYR_MODULES", "").split(";")
    env["EXTRA_ZEPHYR_MODULES"] = ";".join(dict.fromkeys(p for p in extras if p))
    return env


def git_revision(path):
    return run(["git", "-C", path, "rev-parse", "HEAD"], capture=True).stdout.strip()


def build_path(name):
    path = (ROOT / "build" / name).resolve()
    if not path.is_relative_to(ROOT.resolve()) or path == ROOT.resolve():
        raise RuntimeError("Build output resolves outside this repository")
    return path


def doctor():
    env = environment()
    zephyr = Path(env["ZEPHYR_BASE"])
    if sys.version_info < (3, 12):
        raise RuntimeError("Python 3.12 or newer is required")
    if importlib.metadata.version("pyocd") != LOCK["pyocd"]:
        raise RuntimeError("pyOCD differs from dependencies.lock.json")
    for name in ("git", "cmake", "ninja", "dtc", "gperf"):
        path = shutil.which(name)
        if path is None:
            raise RuntimeError(f"Missing host command: {name}; activate the project environment")
        print(f"{name}: {path}")
    if git_revision(zephyr) != LOCK["zephyr"]["revision"]:
        raise RuntimeError("Zephyr checkout differs from dependencies.lock.json; review the baseline")
    sdk_version = (Path(env["ZEPHYR_SDK_INSTALL_DIR"]) / "sdk_version").read_text().strip()
    if sdk_version != LOCK["sdk"]["version"]:
        raise RuntimeError("Zephyr SDK differs from dependencies.lock.json")
    cmsis = zephyr.parent / LOCK["cmsis_6"]["workspace_path"]
    if git_revision(cmsis) != LOCK["cmsis_6"]["revision"]:
        raise RuntimeError("CMSIS_6 checkout differs from dependencies.lock.json")
    import jsonschema
    import yaml
    schema = yaml.safe_load((zephyr / "scripts/schemas/module-schema.yaml").read_text())
    module = yaml.safe_load((ROOT / "zephyr/module.yml").read_text())
    jsonschema.validate(module, schema)
    run([sys.executable, "-m", "west", "--version"], env=env)
    run([sys.executable, "-m", "pip", "check"], env=env)
    run([sys.executable, ROOT / "debug/verify_pyocd.py"], env=env)
    print(f"PASS: development repository {ROOT}; Zephyr dependency {zephyr}")


def check():
    # These checks also run in a standalone clone with no Zephyr checkout or SDK.
    run([sys.executable, "-m", "unittest", "discover", "-s", "tests/tooling", "-v"])
    run([sys.executable, ROOT / "debug/verify_pyocd.py"])
    run(["git", "diff", "--check"])
    run(["git", "diff", "--cached", "--check"])
    print("PASS: project tooling and debug configuration")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("doctor", help="Check installed dependencies and pinned versions")
    subparsers.add_parser("check", help="Test repository tools and offline debug configuration")
    build = subparsers.add_parser("build", help="Build the bring-up sample")
    build.add_argument("--board", default="mps2/an386")
    build.add_argument("--pristine", action="store_true")
    test = subparsers.add_parser("test", help="Build and run the bring-up sample using Twister")
    test.add_argument("--board", default="mps2/an386", choices=["mps2/an386"])
    debug = subparsers.add_parser("debug", help="Start pyOCD GDB server on a connected HC32 board")
    debug.add_argument("--probe", help="Select a probe by unique ID")
    debug.add_argument("--frequency", type=int, default=10000000)
    args = parser.parse_args()
    if args.command == "doctor":
        doctor()
    elif args.command == "check":
        check()
    elif args.command in ("build", "test"):
        env = environment()
        # Output paths are fixed under this repo; no caller-supplied deletion/move paths.
        if args.command == "build":
            run([sys.executable, "-m", "west", "build", "-b", args.board,
                 "-p", "always" if args.pristine else "auto",
                 ROOT / "samples/bringup", "-d", build_path("bringup"), "--",
                 "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"], env=env)
        else:
            run([sys.executable, "-m", "west", "twister", "-p", args.board,
                 "-T", ROOT / "samples/bringup", "--outdir", build_path("twister"),
                 "--inline-logs"], env=env)
    else:
        command = [sys.executable, "-m", "pyocd", "gdbserver", "--project", ROOT,
                   "--config", ROOT / "debug/pyocd.yaml", "-f", str(args.frequency)]
        if args.probe:
            command.extend(["--uid", args.probe])
        run(command)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
