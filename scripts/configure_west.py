# SPDX-License-Identifier: Apache-2.0
"""Configure the checkout's parent as a supported west workspace."""

import configparser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def configure(root=ROOT):
    root = Path(root).resolve()
    workspace = root.parent
    if (workspace / ".git").exists():
        raise RuntimeError("The workspace parent must not itself be a Git repository")
    if (root / ".west").exists():
        raise RuntimeError("A .west directory inside the Git checkout is not a supported layout; review it first")
    if not (root / "project-west.yml").is_file():
        raise RuntimeError("Missing project-west.yml")
    target = workspace / ".west" / "config"
    config = configparser.ConfigParser()
    if target.exists():
        config.read(target, encoding="utf-8")
        if (config.get("manifest", "path", fallback=None) != root.name
                or config.get("manifest", "file", fallback=None) != "project-west.yml"):
            raise RuntimeError("Existing west configuration belongs to another layout; left unchanged")
    # Same topology as west init -l: the manifest repository is a workspace child.
    for section in ("manifest", "zephyr"):
        if not config.has_section(section):
            config.add_section(section)
    config["manifest"]["path"] = root.name
    config["manifest"]["file"] = "project-west.yml"
    config["zephyr"]["base"] = root.name
    target.parent.mkdir(exist_ok=True)
    with target.open("w", encoding="utf-8") as stream:
        config.write(stream)
    print(f"Configured ../.west/config: manifest.path={root.name}, manifest.file=project-west.yml")


if __name__ == "__main__":
    configure()
