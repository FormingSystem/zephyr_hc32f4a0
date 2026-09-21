# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""验证教程的实际行为；必须用安装了 requirements-tools.txt 的解释器运行。"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import uuid
import venv
from pathlib import Path

import yaml


LEARNING = Path(__file__).resolve().parent
REPO = LEARNING.parent
ENV = os.environ.copy()
# 测试不继承用户的 west / pip 配置，避免改动用户环境。
for key in list(ENV):
    if key.startswith(("WEST_CONFIG_", "PIP_")) or key in ("PYTHONPATH", "PYTHONHOME", "VIRTUAL_ENV", "ZEPHYR_BASE"):
        ENV.pop(key)
ENV["PIP_CONFIG_FILE"] = os.devnull
ENV["PYTHONUTF8"] = "1"


def run(*args, cwd=REPO, expected=0):
    result = subprocess.run([str(arg) for arg in args], cwd=cwd, env=ENV,
                            text=True, encoding="utf-8", errors="replace",
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if (expected == 0 and result.returncode != 0) or (expected != 0 and result.returncode == 0):
        raise RuntimeError(f"Unexpected exit {result.returncode}: {args}\n{result.stdout}")
    return result.stdout.strip()


def python_at(directory):
    return directory / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def check_venv(root):
    sources = LEARNING / "python" / "venv" / "labs"
    wheels = root / "wheelhouse"
    wheels.mkdir()
    for version in (1, 2):
        # 构建在复制品里进行，源教材保持干净。
        package = root / f"package_v{version}"
        shutil.copytree(sources / f"package_v{version}", package,
                        ignore=shutil.ignore_patterns("build", "*.egg-info", "__pycache__"))
        run(sys.executable, "-m", "pip", "wheel", "--no-index", "--no-deps",
            "--no-build-isolation", "--wheel-dir", wheels, package)
    interpreters = {}
    for name, version in (("a", 1), ("b", 2), ("recreated", 1)):
        directory = root / name
        venv.EnvBuilder(with_pip=True).create(directory)
        python = python_at(directory)
        interpreters[name] = python
        before = run(python, sources / "inspect_environment.py")
        assert json.loads(before)["is_venv"] is True
        assert json.loads(before)["VIRTUAL_ENV"] is None
        run(python, "-c", "import lab_greeting", expected=1)
        run(python, "-m", "pip", "install", "--no-index", "--find-links", wheels,
            f"lab-greeting=={version}.0.0")
        assert run(python, "-c", "from lab_greeting import greet; print(greet())") == f"hello reader from v{version}"
        assert "No broken requirements" in run(python, "-m", "pip", "check")
        # 同一应用契约：v1 通过，v2 可安装却不符合旧应用的行为要求。
        output = run(python, "-m", "unittest", "discover", "-s",
                     sources / "application/tests", "-v", expected=0 if version == 1 else 1)
        assert ("OK" if version == 1 else "FAILED (failures=2)") in output, output
    frozen = run(interpreters["a"], "-m", "pip", "freeze")
    assert frozen == "lab-greeting==1.0.0", frozen
    snapshot = root / "requirements.txt"
    snapshot.write_text(frozen + "\n", encoding="utf-8")
    run(interpreters["recreated"], "-m", "pip", "uninstall", "-y", "lab-greeting")
    run(interpreters["recreated"], "-m", "pip", "install", "--no-index", "--find-links", wheels, "-r", snapshot)
    assert run(interpreters["recreated"], "-c", "from lab_greeting import greet; print(greet())") == "hello reader from v1"
    run(interpreters["b"], "-m", "pip", "uninstall", "-y", "lab-greeting")
    run(interpreters["b"], "-c", "import lab_greeting", expected=1)
    assert run(interpreters["a"], "-c", "from lab_greeting import greet; print(greet())") == "hello reader from v1"
    constraints = root / "constraints.txt"
    constraints.write_text("lab-greeting<2\n", encoding="utf-8")
    run(interpreters["a"], "-m", "pip", "install", "--no-index", "--find-links", wheels,
        "-c", constraints, "lab-greeting==2.0.0", expected=1)
    shadow = root / "shadow"
    shadow.mkdir()
    (shadow / "lab_greeting.py").write_text("marker = 'shadow'\n", encoding="utf-8")
    assert "shadow" in run(interpreters["a"], "-c", "import lab_greeting; print(lab_greeting.__file__)", cwd=shadow)
    run(interpreters["a"], "-c", "from lab_greeting import greet", cwd=shadow, expected=1)
    # 配置测试暂时恢复读取 site 文件；只修改本次生成的 A。
    ENV.pop("PIP_CONFIG_FILE")
    run(interpreters["a"], "-m", "pip", "config", "--site", "set", "global.timeout", "30")
    assert run(interpreters["a"], "-m", "pip", "config", "--site", "get", "global.timeout") == "30"
    ENV["PIP_TIMEOUT"] = "5"
    assert "5" in run(interpreters["a"], "-m", "pip", "config", "list")
    ENV.pop("PIP_TIMEOUT")
    run(interpreters["a"], "-m", "pip", "config", "--site", "unset", "global.timeout")
    ENV["PIP_CONFIG_FILE"] = os.devnull
    editable = root / "editable"
    venv.EnvBuilder(with_pip=True).create(editable)
    dev = python_at(editable)
    # 使用本机已验证的后端目录，避免这项额外测试联网下载。
    import setuptools
    backend = Path(setuptools.__file__).resolve().parent.parent
    devsite = Path(run(dev, "-c", "import sysconfig; print(sysconfig.get_path('purelib'))"))
    for pattern in ("setuptools", "setuptools-*.dist-info", "_distutils_hack", "distutils-precedence.pth"):
        for path in backend.glob(pattern):
            if path.is_dir():
                shutil.copytree(path, devsite / path.name)
            else:
                shutil.copy2(path, devsite / path.name)
    editable_src = root / "package_v1"
    run(dev, "-m", "pip", "install", "--no-index", "--no-build-isolation", "-e", editable_src)
    module = editable_src / "src" / "lab_greeting" / "__init__.py"
    module.write_text(module.read_text(encoding="utf-8").replace("from v1", "from editable source"), encoding="utf-8")
    assert "editable source" in run(dev, "-c", "from lab_greeting import greet; print(greet())")
    print("PASS venv: isolation, identity, freeze/recreate, uninstall, constraints, shadowing, config, editable")


def check_west(root):
    name = "check-" + uuid.uuid4().hex[:10]
    run(sys.executable, LEARNING / "west" / "labs" / "seed_workspace.py", "--name", name)
    run(sys.executable, LEARNING / "west" / "labs" / "seed_workspace.py", "--name", name, expected=1)
    workspace = REPO / "build" / "learning-tools" / "west" / name / "workspace"
    ENV["WEST_CONFIG_SYSTEM"] = str(root / "empty-system.ini")
    ENV["WEST_CONFIG_GLOBAL"] = str(root / "global.ini")
    ENV["WEST_CONFIG_LOCAL"] = str(workspace / ".west" / "config")

    def west(*args, expected=0):
        return run(sys.executable, "-m", "west", *args, cwd=workspace, expected=expected)

    run(sys.executable, LEARNING / "west/labs/init_workspace.py", "-l", "manifest", cwd=workspace)
    run(sys.executable, LEARNING / "west/labs/init_workspace.py", "-l", "manifest", cwd=workspace, expected=1)
    from_source = workspace.parent / "from-source"
    run(sys.executable, LEARNING / "west/labs/init_workspace.py", "-m", "./workspace/manifest",
        "--mr", "main", "from-source", cwd=workspace.parent)
    ENV["WEST_CONFIG_LOCAL"] = str(from_source / ".west" / "config")
    run(sys.executable, "-m", "west", "update", cwd=from_source)
    assert run(sys.executable, "app/main.py", cwd=from_source) == "2 + 3 = 5"
    ENV["WEST_CONFIG_LOCAL"] = str(workspace / ".west" / "config")
    assert not (workspace / "app").exists()
    west("inventory", "--require-cloned", expected=1)
    west("update")
    assert run(sys.executable, "app/main.py", cwd=workspace) == "2 + 3 = 5"
    assert not (workspace / "docs" / "guide").exists()
    assert len(json.loads(west("inventory", "--format", "json"))) == 2
    west("manifest", "--validate")
    west("status")
    west("diff")
    west("forall", "-c", "git status --short")
    west("config", "--global", "color.ui", "true")
    west("config", "--local", "color.ui", "false")
    assert west("config", "color.ui") == "false"
    west("config", "--local", "-d", "color.ui")
    assert west("config", "color.ui") == "true"
    west("config", "--local", "manifest.group-filter", "+docs")
    west("inventory", "--require-cloned", expected=1)
    west("update")
    assert len(json.loads(west("inventory", "--format", "json"))) == 3
    west("config", "--local", "manifest.group-filter", "--", "-docs")
    assert len(json.loads(west("inventory", "--format", "json"))) == 2
    assert (workspace / "docs" / "guide").exists()
    west("config", "--local", "-d", "manifest.group-filter")
    manifest_file = workspace / "manifest" / "west.yml"
    manifest = yaml.safe_load(manifest_file.read_text(encoding="utf-8"))
    project = next(p for p in manifest["manifest"]["projects"] if p["name"] == "arithmetic")
    project["revision"] = "v2.0"
    manifest_file.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    arithmetic = workspace / "libs" / "arithmetic"
    old = run("git", "rev-parse", "HEAD", cwd=arithmetic)
    west("update", "arithmetic")
    current = run("git", "rev-parse", "HEAD", cwd=arithmetic)
    assert current != old
    assert current == run("git", "rev-parse", "manifest-rev", cwd=arithmetic)
    run("git", "symbolic-ref", "-q", "HEAD", cwd=arithmetic, expected=1)
    frozen = yaml.safe_load(west("manifest", "--freeze"))
    assert next(p for p in frozen["manifest"]["projects"] if p["name"] == "arithmetic")["revision"] == current
    run("git", "switch", "-c", "learning/local-note", cwd=arithmetic)
    (arithmetic / "LOCAL_NOTE.md").write_text("Local development experiment.\n", encoding="utf-8")
    run("git", "add", "LOCAL_NOTE.md", cwd=arithmetic)
    run("git", "-c", "user.name=Learning Lab", "-c", "user.email=learning@example.invalid",
        "-c", "commit.gpgsign=false", "-c", "core.hooksPath=", "commit", "-m", "Local note", cwd=arithmetic)
    assert run("git", "rev-parse", "HEAD", cwd=arithmetic) != current
    frozen_path = workspace.parent / "west-frozen.yml"
    west("manifest", "--freeze", "--active-only", "-o", str(frozen_path))
    frozen = yaml.safe_load(frozen_path.read_text(encoding="utf-8"))
    assert next(p for p in frozen["manifest"]["projects"] if p["name"] == "arithmetic")["revision"] == current
    # 重建时不继承原 workspace 的显式 local 配置路径。
    replay = workspace.parent / "replay"
    run("git", "clone", workspace / "manifest", replay / "manifest")
    shutil.copy2(frozen_path, replay / "manifest" / "west.yml")
    ENV["WEST_CONFIG_LOCAL"] = str(replay / ".west" / "config")
    run(sys.executable, LEARNING / "west/labs/init_workspace.py", "-l", "manifest", cwd=replay)
    run(sys.executable, "-m", "west", "update", cwd=replay)
    assert run("git", "rev-parse", "HEAD", cwd=replay / "libs" / "arithmetic") == current
    assert not (replay / "libs" / "arithmetic" / "LOCAL_NOTE.md").exists()
    assert run(sys.executable, "app/main.py", cwd=replay) == "2 + 3 = 5"
    ENV["WEST_CONFIG_LOCAL"] = str(workspace / ".west" / "config")
    west("update", "arithmetic")
    assert run("git", "rev-parse", "HEAD", cwd=arithmetic) == current
    run("git", "switch", "learning/local-note", cwd=arithmetic)
    assert (arithmetic / "LOCAL_NOTE.md").exists()
    # 自仓库导入必须相对于清单仓库解析。
    guide = manifest["manifest"]["projects"].pop()
    (workspace / "manifest" / "extra.yml").write_text(yaml.safe_dump({"manifest": {"projects": [guide]}}), encoding="utf-8")
    manifest["manifest"]["self"]["import"] = "extra.yml"
    manifest_file.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    west("manifest", "--validate")
    resolved = yaml.safe_load(west("manifest", "--resolve"))
    assert any(p["name"] == "guide" for p in resolved["manifest"]["projects"])
    source_app = workspace.parent / "remotes" / "app"
    shutil.copy2(workspace / "manifest" / "extra.yml", source_app / "west.yml")
    run("git", "add", "west.yml", cwd=source_app)
    run("git", "-c", "user.name=Learning Lab", "-c", "user.email=learning@example.invalid",
        "-c", "commit.gpgsign=false", "-c", "core.hooksPath=", "commit", "-m", "Publish imported guide", cwd=source_app)
    app_revision = run("git", "rev-parse", "HEAD", cwd=source_app)
    manifest["manifest"]["self"].pop("import")
    app_project = next(p for p in manifest["manifest"]["projects"] if p["name"] == "app")
    app_project.update({"revision": app_revision, "import": "west.yml"})
    manifest_file.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    west("update")
    (workspace / "app" / "west.yml").write_text("manifest: {projects: []}\n", encoding="utf-8")
    resolved = yaml.safe_load(west("manifest", "--resolve"))
    assert any(p["name"] == "guide" for p in resolved["manifest"]["projects"])
    run("git", "restore", "west.yml", cwd=workspace / "app")
    west("config", "--local", "commands.allow_extensions", "false")
    west("inventory", expected=1)
    west("config", "--local", "commands.allow_extensions", "true")
    west("inventory", "--require-cloned")
    west("inventory", "--format", "invalid", expected=1)
    extension = workspace / "manifest" / "commands" / "inventory.py"
    code = extension.read_text(encoding="utf-8")
    code = code.replace("        return parser", '        parser.add_argument("--count", action="store_true")\n        return parser')
    code = code.replace('        if args.format == "json":', '        if args.count:\n            self.inf(str(len(rows)))\n            return\n        if args.format == "json":')
    extension.write_text(code, encoding="utf-8")
    assert west("inventory", "--count", "--require-cloned") == "2"
    west("compare")
    # 整套本地源和消费目录搬到含空格/中文的新位置，验证没有固定绝对地址。
    original = workspace.parent.resolve()
    moved = original.with_name(original.name + " moved 中文").resolve()
    allowed = (REPO / "build" / "learning-tools" / "west").resolve()
    assert original.is_relative_to(allowed) and moved.is_relative_to(allowed)
    assert not moved.exists()
    original.rename(moved)
    workspace = moved / "workspace"
    ENV["WEST_CONFIG_LOCAL"] = str(workspace / ".west" / "config")
    west("update", "--fetch=always")
    assert run(sys.executable, "app/main.py", cwd=workspace) == "2 + 3 = 5"
    assert west("inventory", "--count", "--require-cloned") == "2"
    print("PASS west: init/update, freeze/replay, config, self/project imports, extensions, relative URL relocation")
    print(f"West evidence: {workspace}")


def main():
    (REPO / "build" / "learning-tools").mkdir(parents=True, exist_ok=True)
    root = Path(tempfile.mkdtemp(prefix="check-", dir=REPO / "build" / "learning-tools"))
    print(f"Evidence retained: {root}", flush=True)
    print(run(sys.executable, "--version"))
    print(run(sys.executable, "-m", "pip", "--version"))
    print(run(sys.executable, "-m", "west", "--version"))
    print(run("git", "--version"))
    check_venv(root)
    check_west(root)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
