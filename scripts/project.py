#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Build the complete HC32 Zephyr checkout with an installed host toolchain."""

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
HC32_BOARD = "uyup_rpi_a/hc32f4a0pitb"
SIMULATION_BOARD = "mps2/an386"


def run(args, *, env=None, capture=False):
    print("+ " + " ".join(map(str, args)), flush=True)
    return subprocess.run(
        list(map(str, args)), cwd=ROOT, env=env, check=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT,
        encoding="utf-8", errors="replace",
    )


def module_paths():
    paths = []
    for name in ("cmsis_6", "hal_xhsc"):
        path = (ROOT / LOCK[name]["source_path"]).resolve()
        if not path.is_relative_to(ROOT.resolve()) or path == ROOT.resolve():
            raise RuntimeError(f"The {name} source path resolves outside this repository")
        if not (path / "zephyr/module.yml").is_file():
            raise RuntimeError(f"Missing vendored {name} module: {path}")
        paths.append(path)
    return paths


def environment():
    env = os.environ.copy()
    for marker in ("VERSION", "CMakeLists.txt", "Kconfig", "scripts/twister"):
        if not (ROOT / marker).is_file():
            raise RuntimeError(f"This repository is missing Zephyr source: {marker}")
    sdk = Path(env.get("ZEPHYR_SDK_INSTALL_DIR") or
               ROOT.parent.parent / f"zephyr-sdk-{LOCK['sdk']['version']}")
    if not (sdk / "sdk_version").is_file():
        raise RuntimeError("Set ZEPHYR_SDK_INSTALL_DIR to the prepared Zephyr SDK")
    env["ZEPHYR_BASE"] = ROOT.resolve().as_posix()
    env["ZEPHYR_SDK_INSTALL_DIR"] = sdk.resolve().as_posix()
    env["ZEPHYR_TOOLCHAIN_VARIANT"] = "zephyr"
    env["ZEPHYR_MODULES"] = ";".join(path.as_posix() for path in module_paths())
    env["PYTHONUTF8"] = "1"
    # A previously activated sibling checkout must not add external modules.
    for variable in ("EXTRA_ZEPHYR_MODULES", "ZEPHYR_EXTRA_MODULES"):
        env.pop(variable, None)
    return env


def build_path(name):
    output_root = (ROOT / "build").resolve()
    path = (output_root / name).resolve()
    if (not output_root.is_relative_to(ROOT.resolve()) or
            not path.is_relative_to(output_root) or path == output_root):
        raise RuntimeError("Build output resolves outside this repository's build directory")
    return path


def doctor():
    env = environment()
    if sys.version_info < (3, 12):
        raise RuntimeError("Python 3.12 or newer is required")
    if importlib.metadata.version("pyocd") != LOCK["pyocd"]:
        raise RuntimeError("pyOCD differs from dependencies.lock.json")
    for name in ("git", "cmake", "ninja", "dtc", "gperf"):
        path = shutil.which(name)
        if path is None:
            raise RuntimeError(f"Missing host command: {name}; activate the project environment")
        print(f"{name}: {path}")
    version_fields = dict(
        line.split("=", 1) for line in (ROOT / "VERSION").read_text().splitlines()
        if "=" in line
    )
    version_fields = {key.strip(): value.strip() for key, value in version_fields.items()}
    version = ".".join(version_fields[key]
                       for key in ("VERSION_MAJOR", "VERSION_MINOR", "PATCHLEVEL"))
    if version != LOCK["zephyr"]["version"]:
        raise RuntimeError("Zephyr VERSION differs from dependencies.lock.json")
    required_sources = (
        "arch/arm/core/cortex_m/reset.S",
        "include/zephyr/kernel.h",
        "kernel/init.c",
        "soc/xhsc/hc32f4a0/soc.yml",
        "boards/uyup/uyup_rpi_a/board.yml",
        f"{LOCK['cmsis_6']['source_path']}/CMSIS/Core/Include/core_cm4.h",
        f"{LOCK['hal_xhsc']['source_path']}/hc32_ddl/hc32f4a0/soc/hc32f4a0.h",
    )
    for source in required_sources:
        if not (ROOT / source).is_file():
            raise RuntimeError(f"Missing required project source: {source}")
    sdk_version = (Path(env["ZEPHYR_SDK_INSTALL_DIR"]) / "sdk_version").read_text().strip()
    if sdk_version != LOCK["sdk"]["version"]:
        raise RuntimeError("Zephyr SDK differs from dependencies.lock.json")
    import jsonschema
    import yaml
    schema = yaml.safe_load((ROOT / "scripts/schemas/module-schema.yaml").read_text())
    for name, path in zip(("cmsis_6", "hal_xhsc"), module_paths()):
        module = yaml.safe_load((path / "zephyr/module.yml").read_text())
        jsonschema.validate(module, schema)
        print(f"Vendored {name}: {path}; recorded upstream revision {LOCK[name]['revision']}")
    print(f"Zephyr {version}; recorded upstream baseline {LOCK['zephyr']['revision']}")
    run([sys.executable, "-m", "pip", "check"], env=env)
    run([sys.executable, ROOT / "debug/verify_pyocd.py"], env=env)
    print(f"PASS: complete development repository {ROOT}")


def check():
    # Offline checks need Python tools, but no SDK, west workspace or hardware.
    run([sys.executable, "-m", "unittest", "discover", "-s", "tests/tooling", "-v"])
    run([sys.executable, ROOT / "debug/verify_pyocd.py"])
    run([sys.executable, ROOT / "scripts/check_project_diff.py"])
    print("PASS: project tooling and debug configuration")


def build_firmware(board, *, pristine=False):
    env = environment()
    destination = build_path("bringup" if board == HC32_BOARD else "mps2")
    configure = ["cmake", "-S", ROOT / "samples/bringup", "-B", destination,
                 "-G", "Ninja", f"-DBOARD={board}",
                 f"-DPython3_EXECUTABLE={Path(sys.executable).as_posix()}",
                 f"-DZephyr_DIR={(ROOT / 'share/zephyr-package/cmake').as_posix()}",
                 f"-DZEPHYR_BASE={env['ZEPHYR_BASE']}",
                 f"-DZEPHYR_MODULES={env['ZEPHYR_MODULES']}",
                 "-DEXTRA_ZEPHYR_MODULES=", "-DZEPHYR_EXTRA_MODULES=",
                 "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"]
    if pristine:
        configure.append("--fresh")
    run(configure, env=env)
    run(["cmake", "--build", destination], env=env)
    if board == HC32_BOARD:
        run([sys.executable, ROOT / "scripts/verify_hc32_image.py",
             "--build-dir", destination], env=env)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("doctor", help="Check installed tools and complete project sources")
    subparsers.add_parser("check", help="Test repository tools and offline debug configuration")
    build = subparsers.add_parser("build", help="Build the HC32 bring-up sample")
    build.add_argument("--board", default=HC32_BOARD, choices=[HC32_BOARD, SIMULATION_BOARD])
    build.add_argument("--pristine", action="store_true")
    test = subparsers.add_parser("test", help="Run the bring-up simulation using Twister")
    test.add_argument("--board", default=SIMULATION_BOARD, choices=[SIMULATION_BOARD])
    debug = subparsers.add_parser("debug", help="Start pyOCD GDB server on a connected HC32 board")
    debug.add_argument("--probe", help="Select a probe by unique ID")
    debug.add_argument("--frequency", type=int, default=10000000)
    args = parser.parse_args(argv)
    if args.command == "doctor":
        doctor()
    elif args.command == "check":
        check()
    elif args.command == "build":
        build_firmware(args.board, pristine=args.pristine)
    elif args.command == "test":
        run([sys.executable, ROOT / "scripts/twister", "-p", args.board,
             "-T", ROOT / "samples/bringup", "--outdir", build_path("twister"),
             "--inline-logs"], env=environment())
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
