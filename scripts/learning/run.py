#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Build or run an in-repository learning application and save its evidence."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import struct
import subprocess
import sys
import uuid

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import project


def application_path(value):
    root = project.ROOT.resolve()
    app = (root / value).resolve()
    allowed = [root / "samples/learning", root / "tests/learning"]
    if not any(app.is_relative_to(base) and app != base for base in allowed):
        raise RuntimeError("Application must be inside samples/learning or tests/learning")
    if not (app / "CMakeLists.txt").is_file():
        raise RuntimeError(f"Missing application CMakeLists.txt: {app}")
    return app


def extra_config(app, value):
    if value is None:
        return None
    config = (app / value).resolve()
    if not config.is_relative_to(app) or not config.is_file():
        raise RuntimeError("Extra configuration must be an existing file inside the application")
    return config


def report_summary(report):
    """A successful command must have executed cases, not merely built an image."""
    suites = report.get("testsuites", [])
    cases = [case for suite in suites for case in suite.get("testcases", [])]
    passed = sum(case.get("status") == "passed" for case in cases)
    complete = bool(suites and cases) and all(
        suite.get("status") == "passed" and suite.get("runnable") is True
        and bool(suite.get("testcases")) for suite in suites
    ) and passed == len(cases)
    return {"suites": len(suites), "cases": len(cases), "passed": passed,
            "all_executed_and_passed": complete}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_identity(app):
    root = project.ROOT
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    difference = subprocess.check_output(["git", "diff", "--binary", "HEAD", "--"], cwd=root)
    status = subprocess.check_output(
        ["git", "status", "--short", "--untracked-files=all"], cwd=root, text=True,
        encoding="utf-8",
    )
    untracked = subprocess.check_output(
        ["git", "ls-files", "--others", "--exclude-standard", "-z"], cwd=root,
    ).decode("utf-8").split("\0")
    # A new shared header/driver outside the application is absent from git diff.
    inputs = set(app.rglob("*")) | {Path(__file__), root / "scripts/project.py",
                                    root / "dependencies.lock.json"}
    inputs.update(root / name for name in untracked if name)
    files = {}
    for path in sorted(inputs):
        if path.is_file():
            if not path.resolve().is_relative_to(root.resolve()):
                raise RuntimeError(f"Source input resolves outside this repository: {path}")
            files[path.relative_to(root).as_posix()] = sha256(path)
    return {"head": head, "status": status, "tracked_diff_sha256":
            hashlib.sha256(difference).hexdigest(), "input_sha256": files,
            "upstream": project.LOCK["zephyr"]["revision"]}


def stop_process_tree(process):
    """Terminate only the tree/group rooted at a process started by this runner."""
    cleanup_error = None
    try:
        if os.name == "nt":
            taskkill = Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32/taskkill.exe"
            result = subprocess.run(
                [str(taskkill), "/PID", str(process.pid), "/T", "/F"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=15,
                creationflags=subprocess.CREATE_NO_WINDOW, check=False,
            )
            if result.returncode:
                raise RuntimeError("taskkill could not confirm process-tree termination: " +
                                   result.stdout.decode(errors="replace").strip())
        else:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        cleanup_error = error
    finally:
        # Reap our direct child even if tree cleanup failed; never report that as
        # successful tree cleanup, and do not hash possibly still-changing files.
        if process.poll() is None and cleanup_error:
            process.kill()
        process.wait(timeout=10)
    if cleanup_error:
        raise RuntimeError(str(cleanup_error)) from cleanup_error


def execute(command, env, destination, evidence, timeout):
    command = list(map(str, command))
    log = destination / f"step-{len(evidence['commands']) + 1}.log"
    print("+ " + " ".join(command), flush=True)
    record = {"argv": command, "log": log.relative_to(project.ROOT).as_posix()}
    evidence["commands"].append(record)
    with log.open("w", encoding="utf-8") as stream:
        try:
            process = subprocess.Popen(
                command, cwd=project.ROOT, env=env, stdout=stream,
                stderr=subprocess.STDOUT, text=True,
                start_new_session=os.name != "nt",
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0,
            )
        except OSError as error:
            record.update(exit_code=None, error=str(error))
            raise
        record["pid"] = process.pid
        try:
            record["exit_code"] = process.wait(timeout=timeout)
        except (subprocess.TimeoutExpired, KeyboardInterrupt) as error:
            timed_out = isinstance(error, subprocess.TimeoutExpired)
            record.update(exit_code=124 if timed_out else 130, timed_out=timed_out)
            try:
                stop_process_tree(process)
                record["process_tree_stopped"] = True
            except (OSError, RuntimeError, subprocess.SubprocessError) as cleanup_error:
                record["cleanup_error"] = str(cleanup_error)
            reason = f"Command exceeded {timeout}s" if timed_out else "Command interrupted"
            raise RuntimeError(f"{reason}; see {log}") from None
    print(f"exit={record['exit_code']}; log={log}", flush=True)
    if record["exit_code"]:
        print("\n".join(log.read_text(encoding="utf-8", errors="replace").splitlines()[-30:]))
        raise RuntimeError(f"Command failed with exit code {record['exit_code']}")
    return log


def toolchain_identity(env, destination, evidence, timeout):
    sdk = Path(env["ZEPHYR_SDK_INSTALL_DIR"]).resolve()
    actual_version = (sdk / "sdk_version").read_text(encoding="utf-8").strip()
    evidence["sdk"] = actual_version
    if actual_version != project.LOCK["sdk"]["version"]:
        raise RuntimeError(f"SDK version {actual_version} differs from dependencies.lock.json")
    suffix = ".exe" if os.name == "nt" else ""
    name = f"arm-zephyr-eabi-gcc{suffix}"
    candidates = [sdk / "gnu/arm-zephyr-eabi/bin" / name,
                  sdk / "arm-zephyr-eabi/bin" / name]
    compiler = next((path.resolve() for path in candidates if path.is_file()), None)
    if compiler is None:
        raise RuntimeError("The selected SDK does not contain arm-zephyr-eabi-gcc")
    version_log = execute([compiler, "--version"], env, destination, evidence, timeout)
    target_log = execute([compiler, "-dumpmachine"], env, destination, evidence, timeout)
    target = target_log.read_text(encoding="utf-8", errors="replace").strip()
    evidence["compiler"] = {"path": compiler.as_posix(), "target": target,
                            "version": version_log.read_text(encoding="utf-8", errors="replace").strip()}
    if target != "arm-zephyr-eabi":
        raise RuntimeError(f"Expected ARM cross compiler, got {target}")
    return compiler


def assignments(path):
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith(("#", "//")) or "=" not in line:
            continue
        name, value = line.split("=", 1)
        values[name.split(":", 1)[0]] = value.strip('"')
    return values


def audit_build(build, app, board, compiler):
    """Check an actual Zephyr image and its configured input/target identity."""
    elf = build / "zephyr/zephyr.elf"
    config_path = build / "zephyr/.config"
    cache_path = build / "CMakeCache.txt"
    for path in (elf, config_path, cache_path):
        if not path.is_file():
            raise RuntimeError(f"Required Zephyr build artifact is missing: {path}")
    with elf.open("rb") as stream:
        header = stream.read(20)
    if (len(header) != 20 or header[:6] != b"\x7fELF\x01\x01" or
            struct.unpack_from("<HH", header, 16) != (2, 40)):
        raise RuntimeError(f"Expected a linked 32-bit little-endian ARM ELF: {elf}")
    cache = assignments(cache_path)
    config = assignments(config_path)
    expected_paths = {"CMAKE_HOME_DIRECTORY": app.resolve(),
                      "ZEPHYR_BASE": project.ROOT.resolve(),
                      "CMAKE_C_COMPILER": compiler.resolve()}
    for key, expected in expected_paths.items():
        value = cache.get(key)
        if not value or (build / value).resolve() != expected:
            raise RuntimeError(f"Build {key} does not match the selected input: {value}")
    if cache.get("BOARD") != board or config.get("CONFIG_BOARD_TARGET") != board:
        raise RuntimeError("Build board does not match the requested target")
    return {"directory": build.relative_to(project.ROOT).as_posix(), "board": board,
            "application": app.relative_to(project.ROOT).as_posix(),
            "compiler": compiler.as_posix(), "elf_sha256": sha256(elf)}


def write_json(path, value):
    temporary = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def publish_evidence(evidence, destination, index):
    evidence_path = destination / "evidence.json"
    write_json(evidence_path, evidence)
    index.mkdir(parents=True, exist_ok=True)
    write_json(index / "latest.json", {
        "evidence": evidence_path.relative_to(project.ROOT).as_posix(),
        "success": evidence["success"], "state": evidence["state"],
    })
    return evidence_path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build", "test"])
    parser.add_argument("--app", required=True, help="Path relative to this repository")
    parser.add_argument("--board", default=project.SIMULATION_BOARD,
                        choices=[project.SIMULATION_BOARD, project.HC32_BOARD])
    parser.add_argument("--variant", default="normal", help="Separate output label")
    parser.add_argument("--extra-conf", help="Additional configuration relative to --app")
    parser.add_argument("--scenario", help="Select a tests.yaml scenario (test only)")
    parser.add_argument("--timeout", type=int, default=600, help="Seconds per host command")
    args = parser.parse_args(argv)
    if not re.fullmatch(r"[A-Za-z0-9_-]+", args.variant):
        parser.error("--variant accepts letters, digits, underscore and hyphen only")
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    if args.command == "test" and args.board != project.SIMULATION_BOARD:
        parser.error("Automated execution is available only for mps2/an386")
    if args.command == "build" and args.scenario:
        parser.error("--scenario requires test")
    app = application_path(args.app)
    relative = app.relative_to(project.ROOT).parts
    # Keep samples and tests separate even when their topic names happen to match.
    label = Path(relative[0], *relative[2:])
    index = project.build_path(Path("learning") / label /
                               args.board.replace("/", "_") / args.variant)
    # Short, fresh paths avoid Windows archiver limits and stale reports/images.
    destination = project.build_path(Path("learning/runs") / uuid.uuid4().hex[:10])
    destination.mkdir(parents=True, exist_ok=False)
    evidence = {"started_utc": datetime.now(timezone.utc).isoformat(),
                "source": None, "application": app.relative_to(project.ROOT).as_posix(),
                "board": args.board, "variant": args.variant, "command": args.command,
                "python": sys.version, "sdk": None, "sdk_expected": project.LOCK["sdk"]["version"],
                "extra_conf": args.extra_conf, "state": "running",
                "commands": [], "success": False, "hardware_tested": False}
    output = destination / ("twister" if args.command == "test" else "firmware")
    # A valid application receives a fresh failure-safe index before setup work.
    publish_evidence(evidence, destination, index)
    try:
        config = extra_config(app, args.extra_conf)
        if args.command == "test" and not (app / "tests.yaml").is_file():
            raise RuntimeError("This Zephyr snapshot requires an application tests.yaml")
        env = project.environment()
        evidence["source"] = source_identity(app)
        compiler = toolchain_identity(env, destination, evidence, args.timeout)
        cmake_values = [f"Zephyr_DIR={(project.ROOT / 'share/zephyr-package/cmake').as_posix()}",
                        f"ZEPHYR_BASE={env['ZEPHYR_BASE']}",
                        f"ZEPHYR_MODULES={env['ZEPHYR_MODULES']}",
                        "EXTRA_ZEPHYR_MODULES=", "ZEPHYR_EXTRA_MODULES=",
                        f"Python3_EXECUTABLE={Path(sys.executable).as_posix()}",
                        "CMAKE_EXPORT_COMPILE_COMMANDS=ON",
                        f"EXTRA_CONF_FILE={config.as_posix() if config else ''}"]
        if args.command == "build":
            execute(["cmake", "--fresh", "-S", app, "-B", output, "-G", "Ninja",
                     f"-DBOARD={args.board}", *[f"-D{entry}" for entry in cmake_values]],
                    env, destination, evidence, args.timeout)
            execute(["cmake", "--build", output], env, destination, evidence, args.timeout)
            evidence["builds"] = [audit_build(output, app, args.board, compiler)]
            if args.board == project.HC32_BOARD:
                execute([sys.executable, project.ROOT / "scripts/verify_hc32_image.py",
                         "--build-dir", output], env, destination, evidence, args.timeout)
        else:
            command = [sys.executable, project.ROOT / "scripts/twister", "-T", app,
                       "-p", args.board, "--outdir", output, "--inline-logs", "-j", "2",
                       "--short-build-path"]
            for value in cmake_values:
                command.extend(["-x", value])
            if args.scenario:
                command.extend(["--scenario", args.scenario])
            execute(command, env, destination, evidence, args.timeout)
            report = json.loads((output / "twister.json").read_text(encoding="utf-8"))
            evidence["test_summary"] = report_summary(report)
            if not evidence["test_summary"]["all_executed_and_passed"]:
                raise RuntimeError("Report contains zero, skipped, filtered, failed or unexecuted cases")
            for suite in report["testsuites"]:
                suite_app = (project.ROOT / suite.get("path", "").replace("\\", "/")).resolve()
                if suite.get("platform") != args.board or suite_app != app:
                    raise RuntimeError("Twister report does not match the selected application/board")
            # Canonicalize junction/symlink aliases created by --short-build-path.
            builds = sorted({path.parent.parent.resolve() for path in output.rglob("zephyr.elf")})
            if not builds:
                raise RuntimeError("No Zephyr ELF was produced by the test run")
            if any(not build.is_relative_to(destination.resolve()) for build in builds):
                raise RuntimeError("A test artifact resolves outside this run directory")
            evidence["builds"] = [audit_build(build, app, args.board, compiler) for build in builds]
        evidence["success"] = True
    except (RuntimeError, OSError, ValueError, TypeError, AttributeError,
            subprocess.SubprocessError) as error:
        evidence["error"] = str(error)
        print(f"ERROR: {error}", file=sys.stderr)
    finally:
        # Failure also receives evidence; an old success can never survive a new failed run.
        report_file = output / "twister.json"
        if report_file.is_file() and args.command == "test":
            try:
                evidence["test_summary"] = report_summary(json.loads(
                    report_file.read_text(encoding="utf-8")))
            except (ValueError, OSError, TypeError, AttributeError):
                pass
        try:
            if any(command.get("cleanup_error") for command in evidence["commands"]):
                raise RuntimeError("Artifact hashing skipped because process-tree cleanup failed")
            evidence["artifact_sha256"] = {
                path.relative_to(destination).as_posix(): sha256(path)
                for name in ("zephyr.elf", ".config", "zephyr.dts", "twister.json", "handler.log",
                             "CMakeCache.txt", "compile_commands.json")
                for path in output.rglob(name) if path.is_file()
            }
        except (OSError, RuntimeError) as error:
            evidence["success"] = False
            evidence["artifact_error"] = str(error)
        evidence["finished_utc"] = datetime.now(timezone.utc).isoformat()
        evidence["state"] = "passed" if evidence["success"] else "failed"
        evidence_path = publish_evidence(evidence, destination, index)
        print(f"Evidence: {evidence_path}", flush=True)
    return 0 if evidence["success"] else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
