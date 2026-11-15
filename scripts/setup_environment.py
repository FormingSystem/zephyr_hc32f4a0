# SPDX-License-Identifier: Apache-2.0
"""Create a per-checkout Python environment; download packages, never bundle tools."""

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import venv

from project_env import ROOT, python_path


def configure_editor(sdk):
    """Preserve existing JSON settings; machine tool paths stay ignored."""
    target = ROOT / ".vscode/settings.json"
    try:
        settings = json.loads(target.read_text(encoding="utf-8")) if target.exists() else {}
    except ValueError:
        print("Existing VS Code settings use JSONC; set the .venv interpreter manually")
        return
    settings["python.defaultInterpreterPath"] = "${workspaceFolder}/.venv/Scripts/python.exe" if sys.platform == "win32" else "${workspaceFolder}/.venv/bin/python"
    settings["cortex-debug.armToolchainPath"] = (sdk / "gnu/arm-zephyr-eabi/bin").as_posix()
    bash = shutil.which("bash")
    if sys.platform == "win32" and bash:
        bash = Path(bash).resolve()
        if (bash.parent.parent.parent / "ucrt64").is_dir():
            profiles = settings.setdefault("terminal.integrated.profiles.windows", {})
            profiles["UCRT64"] = {"path": str(bash), "args": ["--login", "-i"],
                                  "env": {"MSYSTEM": "UCRT64", "CHERE_INVOKING": "1"}}
            settings["terminal.integrated.defaultProfile.windows"] = "UCRT64"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sdk", help="Installed SDK directory; otherwise reuse .local/environment.json")
    args = parser.parse_args()
    if sys.version_info < (3, 12):
        parser.error("Python 3.12 or newer is required")
    local_file = ROOT / ".local/environment.json"
    local = json.loads(local_file.read_text(encoding="utf-8")) if local_file.exists() else {}
    sdk_value = args.sdk or local.get("sdk_root")
    if not sdk_value:
        parser.error("Pass --sdk with your installed SDK directory")
    sdk = Path(sdk_value).expanduser().resolve()
    lock = json.loads((ROOT / "dependencies.lock.json").read_text(encoding="utf-8"))
    marker = sdk / "sdk_version"
    if not marker.is_file() or marker.read_text().strip() != lock["sdk"]["version"]:
        parser.error("SDK version must match dependencies.lock.json")
    compiler = sdk / "gnu/arm-zephyr-eabi/bin" / ("arm-zephyr-eabi-gcc.exe" if sys.platform == "win32" else "arm-zephyr-eabi-gcc")
    if not compiler.is_file():
        parser.error("SDK ARM compiler is missing")
    if not python_path().is_file():
        venv.EnvBuilder(with_pip=True).create(ROOT / ".venv")
    subprocess.run([str(python_path()), "-m", "pip", "install", "-r", str(ROOT / "requirements-dev.txt")], check=True)
    subprocess.run([str(python_path()), "-m", "pip", "check"], check=True)
    local.update(python_environment=".venv", sdk_root=str(sdk))
    local_file.parent.mkdir(exist_ok=True)
    local_file.write_text(json.dumps(local, indent=2) + "\n", encoding="utf-8")
    configure_editor(sdk)
    print("Ready: .venv; local SDK selection saved in .local/environment.json")
    print("Next: source .venv/Scripts/activate (Windows Python in Bash)")
    print("Then: python scripts/configure_west.py")
    print("Then: python scripts/project_env.py doctor")


if __name__ == "__main__":
    main()
