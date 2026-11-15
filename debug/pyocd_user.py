# SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
# SPDX-License-Identifier: Apache-2.0

"""Correct the HC32F4A0PITB instance RAM map before pyOCD target init.

pyOCD 0.45.1 starts main RAM at 0x1FFFE000; the vendor map places its
512 KiB at 0x1FFE0000..0x2005FFFF. Backup RAM and Flash algorithms stay
intact. This hook changes metadata only and performs no register writes.
Vendor evidence and board configuration are recorded in project-docs/hardware.md.

Hook API: https://pyocd.io/docs/user_scripts.html#will_init_target
"""

from pyocd.core.exceptions import Error
from pyocd.target.builtin.target_HC32F4A0 import HC32F4A0xI

MAIN_RAM_START = 0x1FFE0000
MAIN_RAM_LENGTH = 0x80000
BUILTIN_RAM_START = 0x1FFFE000


def will_init_target(target, init_sequence):
    """Correct the instance RAM region before executing target initialization."""
    if not isinstance(target, HC32F4A0xI):
        raise Error("HC32F4A0PITB configuration requires target hc32f4a0xi")

    memory_map = target.memory_map
    main_flash = memory_map.get_boot_memory()
    if main_flash is None or main_flash.start != 0 or main_flash.length != 0x200000:
        raise Error("Unexpected HC32F4A0xI main Flash map; review pyOCD support")

    main_ram = next(
        (region for region in memory_map
         if region.is_ram and region.length == MAIN_RAM_LENGTH
         and region.start in (BUILTIN_RAM_START, MAIN_RAM_START)),
        None,
    )
    if main_ram is None:
        raise Error("Unexpected HC32F4A0xI main RAM map; review the project hook")
    if main_ram.start == MAIN_RAM_START:
        return

    corrected_ram = main_ram.clone_with_changes(start=MAIN_RAM_START)
    memory_map.remove_region(main_ram)
    memory_map.add_region(corrected_ram)
