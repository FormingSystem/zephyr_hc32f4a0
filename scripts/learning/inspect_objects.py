#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Build and inspect the T03 ARM object experiment without running firmware."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "samples/learning/compilation/object_probe"
OUTPUT = ROOT / "build/learning/compilation"


def stop_process_tree(process):
    # Share the same scoped cleanup as the Zephyr learning runner. Import only
    # when needed so setup errors are recorded before loading project tools.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from run import stop_process_tree as stop

    stop(process)


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run_command(argv, log: Path, commands: list, expected_failure: bool = False,
                timeout: float = 60) -> str:
    command = [str(arg) for arg in argv]
    record = {"argv": command, "exit_code": None, "expected_failure": expected_failure,
              "log": log.relative_to(ROOT).as_posix()}
    commands.append(record)
    try:
        # A file avoids waiting forever for a surviving descendant to close a
        # captured stdout pipe after the compiler driver has been terminated.
        with log.open("w", encoding="utf-8") as stream:
            process = subprocess.Popen(
                command, cwd=ROOT, stdout=stream, stderr=subprocess.STDOUT,
                start_new_session=os.name != "nt",
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0,
            )
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
                raise RuntimeError(f"{reason}; inspect {log}") from None
        output = log.read_text(encoding="utf-8", errors="replace")
        if expected_failure:
            if record["exit_code"] == 0 or not re.search(r"undefined reference.*g_bias", output):
                raise RuntimeError(f"Expected unresolved g_bias, inspect {log}")
        elif record["exit_code"]:
            raise RuntimeError(f"Command failed ({record['exit_code']}), inspect {log}")
        return output
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        record["error"] = str(error)
        raise
    finally:
        write_json(OUTPUT / "commands.json", commands)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tool(sdk: Path, name: str) -> Path:
    suffix = ".exe" if os.name == "nt" else ""
    # SDK 1.x 将交叉编译器放在 gnu 下；旧 SDK 布局也可显式使用。
    candidates = [
        sdk / "gnu/arm-zephyr-eabi/bin" / f"arm-zephyr-eabi-{name}{suffix}",
        sdk / "arm-zephyr-eabi/bin" / f"arm-zephyr-eabi-{name}{suffix}",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    raise RuntimeError(f"Missing ARM SDK tool: {name}; checked {candidates}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sdk", default=os.environ.get("ZEPHYR_SDK_INSTALL_DIR"))
    args = parser.parse_args(argv)
    # 禁止把固定输出目录重定向到树外，且不递归清理既有实验结果。
    if not OUTPUT.resolve().is_relative_to(ROOT / "build"):
        raise RuntimeError("Experiment output must remain under this checkout's build/")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    # 先覆盖旧结论；中途失败时不能留下上一轮的 PASS 供读者误认。
    write_json(OUTPUT / "report.json", {"status": "RUNNING"})
    commands = []
    write_json(OUTPUT / "commands.json", commands)
    try:
        if not args.sdk:
            raise RuntimeError("provide --sdk or set ZEPHYR_SDK_INSTALL_DIR")
        return inspect(Path(args.sdk).resolve(), commands)
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError, KeyboardInterrupt) as error:
        write_json(OUTPUT / "report.json", {
            "status": "FAIL", "error": str(error) or "Experiment interrupted",
            "commands": len(commands), "software_executed": False, "hardware_tested": False,
        })
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


def inspect(sdk: Path, commands: list) -> int:
    tools = {name: tool(sdk, name) for name in ("gcc", "nm", "readelf", "objdump", "objcopy")}

    def run(argv: list[str | Path], log: Path, expected_failure: bool = False) -> str:
        return run_command(argv, log, commands, expected_failure)

    version = run([tools["gcc"], "--version"], OUTPUT / "compiler-version.txt").splitlines()[0]
    target = run([tools["gcc"], "-dumpmachine"], OUTPUT / "compiler-target.txt").strip()
    if target != "arm-zephyr-eabi":
        raise RuntimeError(f"Expected ARM cross compiler, found {target}")
    common = ["-mcpu=cortex-m4", "-mthumb", "-mfloat-abi=soft", "-std=c11",
              "-ffreestanding", "-fno-builtin", "-fno-common", "-ffunction-sections",
              "-fdata-sections", "-fno-unwind-tables", "-fno-asynchronous-unwind-tables",
              "-Wall", "-Wextra", "-Werror"]
    relative_source = SOURCE.relative_to(ROOT)
    variants = []
    for scale in (2, 3):
        for optimization in ("O0", "O2"):
            name = f"scale{scale}-{optimization}"
            directory = OUTPUT / "arm-cortex-m4" / name
            directory.mkdir(parents=True, exist_ok=True)
            relative = directory.relative_to(ROOT)
            flags = [*common, f"-DSCALE={scale}U", f"-{optimization}"]
            run([tools["gcc"], *flags, "-E", "-P", relative_source / "probe.c",
                 "-o", relative / "probe.i"], directory / "preprocess.log")
            run([tools["gcc"], *flags, "-S", relative_source / "probe.c",
                 "-o", relative / "probe.s"], directory / "assembly.log")
            for stem in ("probe", "calibration", "entry"):
                run([tools["gcc"], *flags, "-c", relative_source / f"{stem}.c",
                     "-o", relative / f"{stem}.o"], directory / f"compile-{stem}.log")
            nm = run([tools["nm"], "-S", relative / "probe.o"], directory / "probe-symbols.txt")
            run([tools["objdump"], "-dr", relative / "probe.o"], directory / "probe-disassembly.txt")
            link = [tools["gcc"], *common, "-nostdlib", "-Wl,--build-id=none",
                    "-T", relative_source / "layout.ld", relative / "probe.o", relative / "entry.o"]
            # 每个变体先制造缺失定义，再用同一组对象补齐，覆盖失败与恢复。
            missing = directory / "missing.elf"
            if missing.exists():
                missing.unlink()
            run([*link, "-o", relative / "missing.elf"], directory / "missing-link.log", True)
            if missing.exists():
                raise RuntimeError("Failed link left an unexpected output ELF")
            run([*link, relative / "calibration.o", f"-Wl,-Map={relative / 'probe.map'}",
                 "-o", relative / "probe.elf"], directory / "recovered-link.log")
            elf_info = run([tools["readelf"], "-h", "-SW", relative / "probe.elf"],
                           directory / "elf-layout.txt")
            if "ARM" not in elf_info or "little endian" not in elf_info:
                raise RuntimeError("Unexpected ELF target or byte order")
            unresolved = run([tools["nm"], "-u", relative / "probe.elf"], directory / "undefined-symbols.txt")
            if unresolved.strip():
                raise RuntimeError("Recovered ELF still has undefined symbols")
            run([tools["nm"], "-S", relative / "probe.elf"], directory / "linked-symbols.txt")
            run([tools["objcopy"], "--dump-section",
                 f".probe_metadata={relative / 'metadata.bin'}", relative / "probe.elf"],
                directory / "metadata.log")
            metadata = (directory / "metadata.bin").read_bytes()
            values = list(struct.unpack("<6I", metadata))
            if values != [0x11223344, 8, 4, 4, 0xFFFFFFFF, 0]:
                raise RuntimeError(f"Unexpected target layout/conversion evidence: {values}")
            if not re.search(r"\bU g_bias\b", nm):
                raise RuntimeError("Object must keep the external g_bias reference")
            size = re.search(r"^[0-9a-fA-F]+\s+([0-9a-fA-F]+)\s+T scale_sample$", nm, re.M)
            if size is None:
                raise RuntimeError("scale_sample missing from object symbol table")
            variants.append({"name": name, "scale_sample_bytes": int(size[1], 16),
                             "local_helper_present": " t multiply_sample" in nm,
                             "metadata_values": values, "metadata_hex": metadata.hex(),
                             "elf_sha256": digest(directory / "probe.elf"),
                             "preprocessed_sha256": digest(directory / "probe.i"),
                             "disassembly_sha256": digest(directory / "probe-disassembly.txt")})
    if variants[0]["preprocessed_sha256"] == variants[2]["preprocessed_sha256"]:
        raise RuntimeError("Changing SCALE did not change preprocessing")
    for baseline, optimized in ((variants[0], variants[1]), (variants[2], variants[3])):
        if baseline["scale_sample_bytes"] <= optimized["scale_sample_bytes"]:
            raise RuntimeError("This exercise expects the selected optimization to shorten scale_sample")
        if not baseline["local_helper_present"] or optimized["local_helper_present"]:
            raise RuntimeError("The expected local-helper optimization was not observed")
    git_head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout.strip()
    inputs = [*sorted(SOURCE.iterdir()), Path(__file__).resolve()]
    report = {"status": "PASS", "git_head": git_head, "compiler": version, "target": target,
              "source_sha256": {p.relative_to(ROOT).as_posix(): digest(p) for p in inputs if p.is_file()},
              "variants": variants, "commands": len(commands),
              "controlled_link_failures": 4, "software_executed": False, "hardware_tested": False}
    (OUTPUT / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1) from error
