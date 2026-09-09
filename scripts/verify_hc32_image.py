#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Audit the linked HC32 image and source provenance without accessing hardware."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import struct
import sys

from elftools.common.exceptions import ELFError
from elftools.elf.elffile import ELFFile


ROOT = Path(__file__).resolve().parents[1]
FLASH_START = 0x00000000
FLASH_SIZE = 2 * 1024 * 1024
RAM_START = 0x1FFE0000
RAM_SIZE = 512 * 1024
ICG_START = 0x400
ICG_END = 0x460
IRQ_COUNT = 144
EXPECTED_ICG = (0xFFDFFFBF,) + (0xFFFFFFFF,) * 23


class ImageAuditError(Exception):
    """An image does not meet the board's boot or provenance requirements."""


def require(condition, message):
    if not condition:
        raise ImageAuditError(message)


def read_assignments(path, cmake=False):
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith(("#", "//")) or "=" not in line:
            continue
        name, value = line.split("=", 1)
        if cmake:
            name = name.split(":", 1)[0]
        values[name] = value.strip('"')
    return values


def resolve_path(value, directory):
    path = Path(value.strip('"\''))
    return (directory / path).resolve() if not path.is_absolute() else path.resolve()


def audit_sources(build_dir):
    cache = read_assignments(build_dir / "CMakeCache.txt", cmake=True)
    require(resolve_path(cache.get("ZEPHYR_BASE", ""), build_dir) == ROOT,
            "CMake ZEPHYR_BASE is not this development repository")
    require(resolve_path(cache.get("CMAKE_HOME_DIRECTORY", ""), build_dir).is_relative_to(ROOT),
            "The application source directory is outside this repository")

    allowed_headers = [ROOT]
    sdk = cache.get("ZEPHYR_SDK_INSTALL_DIR")
    if sdk:
        allowed_headers.append(resolve_path(sdk, build_dir))
    for name, value in cache.items():
        if "python" not in name.lower() or not value or value.endswith("-NOTFOUND"):
            continue
        if name.endswith("EXECUTABLE"):
            executable = resolve_path(value, build_dir)
            allowed_headers.append(executable.parent)
            if executable.parent.name.lower() in ("scripts", "bin"):
                allowed_headers.append(executable.parent.parent)
        elif name.endswith(("INCLUDE_DIR", "INCLUDE_DIRS")):
            allowed_headers.extend(resolve_path(part, build_dir) for part in value.split(";"))

    commands = json.loads((build_dir / "compile_commands.json").read_text(encoding="utf-8"))
    require(isinstance(commands, list) and commands, "Compilation database is empty")
    source_paths = set()
    header_paths = set()
    for entry in commands:
        directory = resolve_path(entry["directory"], build_dir)
        require(directory.is_relative_to(ROOT), f"External compiler working directory: {directory}")
        source = resolve_path(entry["file"], directory)
        require(source.is_relative_to(ROOT), f"External source file: {source}")
        require(source.is_file(), f"Source file no longer exists: {source}")
        source_paths.add(source)
        arguments = entry.get("arguments")
        if arguments is None:
            arguments = shlex.split(entry["command"], posix=os.name != "nt")
        arguments = [argument.strip('"\'') for argument in arguments]
        require("-c" in arguments, f"No compiler input switch for {source}")
        index = arguments.index("-c")
        require(index + 1 < len(arguments), f"Missing compiler input for {source}")
        require(resolve_path(arguments[index + 1], directory) == source,
                f"Compilation command disagrees with its declared source: {source}")

        index = 0
        while index < len(arguments):
            argument = arguments[index]
            value = None
            if argument in ("-I", "-isystem", "-iquote", "-include", "-imacros", "--sysroot"):
                index += 1
                require(index < len(arguments), f"Missing path after {argument}")
                value = arguments[index]
            elif argument.startswith("--sysroot="):
                value = argument.split("=", 1)[1]
            else:
                for prefix in ("-isystem", "-iquote", "-include", "-imacros", "-I"):
                    if argument.startswith(prefix) and len(argument) > len(prefix):
                        value = argument[len(prefix):]
                        break
            if value is not None:
                path = resolve_path(value, directory)
                require(any(path.is_relative_to(allowed) for allowed in allowed_headers),
                        f"Header path is outside this repository, SDK and Python: {path}")
                header_paths.add(path)
            index += 1

    required_sources = (
        "soc/xhsc/hc32f4a0/soc.c",
        "soc/xhsc/hc32f4a0/reset_hook.S",
        "drivers/serial/uart_hc32.c",
        "drivers/gpio/gpio_hc32.c",
        "modules/hal/xhsc/hc32_ddl/hc32f4a0/soc/system_hc32f4a0.c",
        "modules/hal/xhsc/hc32_ddl/hc32f4a0/drivers/src/hc32_ll_icg.c",
    )
    for source in required_sources:
        require((ROOT / source).resolve() in source_paths,
                f"Required source was not compiled: {source}")
    cmsis_headers = ROOT / "modules/hal/cmsis_6"
    require(any(path.is_relative_to(cmsis_headers) for path in header_paths),
            "The compiler does not use the repository's CMSIS 6 headers")
    return {"translation_units": len(commands), "all_sources_in_repository": True,
            "header_search_paths_checked": len(header_paths), "cmsis_6_in_repository": True}


def audit_configuration(build_dir):
    config = read_assignments(build_dir / "zephyr/.config")
    expected = {
        "CONFIG_BOARD_TARGET": "uyup_rpi_a/hc32f4a0pitb",
        "CONFIG_SOC": "hc32f4a0pitb",
        "CONFIG_SOC_HC32F4A0PITB": "y",
        "CONFIG_CPU_CORTEX_M4": "y",
        "CONFIG_SOC_RESET_HOOK": "y",
        "CONFIG_SOC_EARLY_INIT_HOOK": "y",
        "CONFIG_UART_HC32": "y",
        "CONFIG_GPIO_HC32": "y",
    }
    for name, value in expected.items():
        require(config.get(name) == value, f"{name} must be {value}")
    numeric = {
        "CONFIG_FLASH_BASE_ADDRESS": FLASH_START,
        "CONFIG_FLASH_SIZE": FLASH_SIZE // 1024,
        "CONFIG_FLASH_LOAD_OFFSET": 0,
        "CONFIG_SRAM_BASE_ADDRESS": RAM_START,
        "CONFIG_SRAM_SIZE": RAM_SIZE // 1024,
        "CONFIG_NUM_IRQS": IRQ_COUNT,
    }
    for name, value in numeric.items():
        require(name in config and int(config[name], 0) == value,
                f"{name} does not match the HC32F4A0PITB memory/interrupt layout")
    require(config.get("CONFIG_ARM_MPU") != "y", "HC32 MPU layout has not been implemented")
    return config


def audit_elf(path, config):
    with path.open("rb") as stream:
        elf = ELFFile(stream)
        require(elf.elfclass == 32 and elf.little_endian and elf["e_machine"] == "EM_ARM",
                "The image is not a little-endian 32-bit ARM ELF")
        require(elf["e_type"] == "ET_EXEC", "The image is not a linked executable")
        table = elf.get_section_by_name(".symtab")
        require(table is not None, "ELF symbol table is required for the image audit")
        symbols = {symbol.name: symbol["st_value"] for symbol in table.iter_symbols()
                   if symbol["st_shndx"] != "SHN_UNDEF"}

        def symbol(name):
            require(name in symbols, f"Missing boot symbol: {name}")
            return symbols[name]

        segments = [segment for segment in elf.iter_segments() if segment["p_type"] == "PT_LOAD"]

        def read_address(address, size):
            for segment in segments:
                offset = address - segment["p_vaddr"]
                if 0 <= offset and offset + size <= segment["p_filesz"]:
                    return segment.data()[offset:offset + size]
            raise ImageAuditError(f"No file-backed ELF data at 0x{address:08x}+0x{size:x}")

        def executable_address(address):
            return ICG_END <= address < FLASH_START + FLASH_SIZE and any(
                section["sh_flags"] & 0x4 and
                section["sh_addr"] <= address < section["sh_addr"] + section["sh_size"]
                for section in elf.iter_sections()
            )

        vector_start = symbol("_vector_start")
        vector_end = symbol("_vector_end")
        require(vector_start == 0 and vector_end == (IRQ_COUNT + 16) * 4,
                "The Cortex-M exception/IRQ table does not occupy 0x00000000..0x0000027f")
        require(symbol("__hc32_icg_start") == ICG_START and symbol("__hc32_icg_end") == ICG_END,
                "ICG linker symbols must describe 0x00000400..0x0000045f")
        icg = struct.unpack("<24I", read_address(ICG_START, ICG_END - ICG_START))
        require(icg == EXPECTED_ICG,
                "Unsafe/unexpected ICG words: watchdogs must stop, "
                "Flash protection must remain off, "
                "and reserved words must be 0xffffffff")
        require(read_address(vector_end, ICG_START - vector_end) ==
                b"\xff" * (ICG_START - vector_end), "The gap before ICG is not erased padding")

        vectors = struct.unpack(f"<{IRQ_COUNT + 16}I", read_address(0, vector_end))
        initial_sp = vectors[0]
        require(RAM_START < initial_sp <= RAM_START + RAM_SIZE and initial_sp % 8 == 0,
                f"Initial SP is outside aligned SRAM: 0x{initial_sp:08x}")
        expected_sp = symbol("z_main_stack") + int(config["CONFIG_MAIN_STACK_SIZE"], 0)
        require(initial_sp == expected_sp, "Initial SP does not match the linked main stack top")
        require(vectors[1] == symbol("z_arm_reset") and vectors[1] == elf["e_entry"],
                "The reset vector, z_arm_reset and ELF entry point disagree")
        reserved = {7, 8, 9, 10, 13}
        for index, handler in enumerate(vectors[1:], start=1):
            if index in reserved:
                require(handler == 0, f"Reserved exception vector {index} must be zero")
            else:
                require(handler & 1 and executable_address(handler & ~1),
                        f"Vector {index} is not a Thumb handler in executable Flash: "
                        f"0x{handler:08x}")
        for name in ("soc_reset_hook", "soc_early_init_hook", "SystemCoreClockUpdate"):
            require(executable_address(symbol(name) & ~1), f"Boot hook is not executable: {name}")

        flash_load_end = 0
        for segment in segments:
            if segment["p_filesz"]:
                start = segment["p_paddr"]
                end = start + segment["p_filesz"]
                require(FLASH_START <= start < end <= FLASH_START + FLASH_SIZE,
                        "A load segment falls outside the chip's 2 MiB Flash")
                flash_load_end = max(flash_load_end, end)
        for section in elf.iter_sections():
            if not section["sh_flags"] & 0x2 or not section["sh_size"]:
                continue
            start = section["sh_addr"]
            end = start + section["sh_size"]
            require((FLASH_START <= start < end <= FLASH_START + FLASH_SIZE) or
                    (RAM_START <= start < end <= RAM_START + RAM_SIZE),
                    f"Allocated section {section.name} is outside Flash and main SRAM")
        return {
            "elf_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "machine": "ARM Cortex-M4, little endian, 32 bit",
            "flash": {"start": "0x00000000", "size_bytes": FLASH_SIZE,
                      "load_end_exclusive": f"0x{flash_load_end:08x}"},
            "sram": {"start": "0x1ffe0000", "size_bytes": RAM_SIZE},
            "vectors": {"start": "0x00000000", "end_exclusive": f"0x{vector_end:08x}",
                        "external_irqs": IRQ_COUNT, "initial_sp": f"0x{initial_sp:08x}",
                        "reset_handler": f"0x{vectors[1]:08x}", "all_handlers_valid": True},
            "icg": {"start": "0x00000400", "end_exclusive": "0x00000460",
                    "configuration_words": [f"0x{word:08x}" for word in icg[:4]],
                    "reserved_words_erased": True, "watchdogs_auto_start": False,
                    "flash_read_protection": False},
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-dir", type=Path, default=ROOT / "build/bringup",
                        help="HC32 build directory (default: this repository's build/bringup)")
    arguments = parser.parse_args()
    build_dir = arguments.build_dir.resolve()
    try:
        require(build_dir.is_relative_to(ROOT), "Build artifacts must be inside this repository")
        config = audit_configuration(build_dir)
        sources = audit_sources(build_dir)
        image = audit_elf(build_dir / "zephyr/zephyr.elf", config)
        result = {"status": "PASS", "repository": str(ROOT), "build_directory": str(build_dir),
                  "board": config["CONFIG_BOARD_TARGET"], "image": image,
                  "source_provenance": sources, "hardware_accessed": False,
                  "hardware_tested": False}
        print(json.dumps(result, indent=2))
        return 0
    except (ImageAuditError, ELFError, OSError, ValueError, KeyError, struct.error) as error:
        print(json.dumps({"status": "FAIL", "error": str(error), "hardware_accessed": False},
                         indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
