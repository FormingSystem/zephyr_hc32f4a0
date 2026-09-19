# SPDX-License-Identifier: Apache-2.0
"""Run project tools with this checkout's .venv and locally configured SDK."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def python_path(root=ROOT):
    return Path(root) / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def windows_paths():
    """Read installed host paths without changing user or machine settings."""
    if os.name != "nt":
        return []
    import winreg
    paths = []
    for hive, key_name in (
        (winreg.HKEY_CURRENT_USER, "Environment"),
        (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"),
    ):
        try:
            with winreg.OpenKey(hive, key_name) as key:
                paths.extend(os.path.expandvars(winreg.QueryValueEx(key, "Path")[0]).split(";"))
        except OSError:
            continue
    return paths


def environment(root=ROOT, base=None):
    root = Path(root).resolve()
    env = dict(os.environ if base is None else base)
    python = python_path(root)
    if not python.is_file():
        raise RuntimeError("Create this checkout's .venv with scripts/setup_environment.py first")
    local_file = root / ".local" / "environment.json"
    local = json.loads(local_file.read_text(encoding="utf-8")) if local_file.exists() else {}
    sdk_value = local.get("sdk_root") or env.get("ZEPHYR_SDK_INSTALL_DIR")
    if not sdk_value:
        raise RuntimeError("Configure an installed SDK using scripts/setup_environment.py --sdk")
    sdk = Path(sdk_value)
    if not sdk.is_absolute():
        sdk = root / sdk
    sdk = sdk.resolve()
    lock = json.loads((root / "dependencies.lock.json").read_text(encoding="utf-8"))
    if not (sdk / "sdk_version").is_file() or (sdk / "sdk_version").read_text().strip() != lock["sdk"]["version"]:
        raise RuntimeError("SDK missing or version differs from dependencies.lock.json")
    paths = windows_paths() + env.get("PATH", "").split(os.pathsep)
    # Existing Windows repository checks expect native Git path output.
    git_dirs = [p for p in paths if (Path(p) / "git.exe").is_file()
                and Path(p).name.lower() == "cmd"] if os.name == "nt" else []
    tools = [str(python.parent), str(sdk / "gnu/arm-zephyr-eabi/bin"),
             str(sdk / "hosttools/qemu"), str(sdk / "hosttools/openocd/bin")]
    env["PATH"] = os.pathsep.join(dict.fromkeys(p for p in tools + git_dirs + paths if p))
    env["VIRTUAL_ENV"] = str(root / ".venv")
    env["ZEPHYR_BASE"] = str(root)
    env["ZEPHYR_SDK_INSTALL_DIR"] = str(sdk)
    env["ZEPHYR_TOOLCHAIN_VARIANT"] = "zephyr"
    env["ZEPHYR_MODULES"] = ";".join((root / lock[k]["source_path"]).as_posix()
                                   for k in ("cmsis_6", "hal_xhsc"))
    env["PYTHONUTF8"] = "1"
    for name in ("PYTHONHOME", "PYTHONPATH", "EXTRA_ZEPHYR_MODULES", "ZEPHYR_EXTRA_MODULES",
                 "WEST_CONFIG_LOCAL", "WEST_CONFIG_GLOBAL", "WEST_CONFIG_SYSTEM"):
        env.pop(name, None)
    return env


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["doctor", "check", "build", "test", "debug", "exec"])
    parser.add_argument("arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    env = environment()
    if args.action == "exec":
        if not args.arguments:
            parser.error("exec requires a command")
        command = args.arguments
        executable = str(python_path()) if command[0] in ("python", "python3") else shutil.which(command[0], path=env["PATH"])
        if not executable:
            raise RuntimeError(f"Host command missing: {command[0]}")
        command = [executable, *command[1:]]
    else:
        command = [str(python_path()), str(ROOT / "scripts/project.py"), args.action, *args.arguments]
    return subprocess.run(command, cwd=ROOT, env=env, check=False).returncode


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
