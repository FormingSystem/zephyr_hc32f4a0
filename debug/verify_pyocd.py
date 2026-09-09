# SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
# SPDX-License-Identifier: Apache-2.0

"""Verify portable pyOCD configuration and init hooks without a hardware backend.

Load the real YAML and user script through Session from an unrelated directory.
Replace only the target init sequence, retaining the real pre-init hook timing.
No probe enumeration, connection, register access, or Flash programming occurs.
"""

import copy
import json
import os
from pathlib import Path
import tempfile
from unittest.mock import patch

import pyocd
from pyocd.core.session import Session
from pyocd.target.builtin.target_HC32F4A0 import HC32F4A0xI
from pyocd.tools.lists import StubProbe
from pyocd.utility.sequencer import CallSequence


class OfflineProbe(StubProbe):
    def open(self):
        raise AssertionError("Offline verification must never open a probe")

    def connect(self, protocol=None):
        raise AssertionError("Offline verification must never connect a target")


def verify():
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "debug" / "pyocd.yaml"
    original_cwd = Path.cwd()
    original_builtin_map = HC32F4A0xI.MEMORY_MAP.clone()

    with tempfile.TemporaryDirectory(prefix="hc32-pyocd-") as unrelated_directory:
        try:
            os.chdir(unrelated_directory)
            assert Path.cwd() != project_root
            # project_dir is the Session API equivalent of the CLI --project.
            # Session resolves the relative user_script after entering that directory.
            session = Session(
                OfflineProbe(), auto_open=False, project_dir=str(project_root),
                config_file=str(config_path),
            )
            assert Path(session.project_dir) == project_root
            assert Path.cwd() == project_root
            assert session.options["target_override"] == "hc32f4a0xi"
            assert session.options["dap_protocol"] == "swd"
            assert session.options["auto_unlock"] is False
            assert session.options["frequency"] == 10000000
            assert session.options["user_script"] == "debug/pyocd_user.py"
            expected_script = config_path.with_name("pyocd_user.py")
            assert Path(session.options["user_script"]).resolve() == expected_script
            assert session.delegate is not None
            assert hasattr(session.delegate, "will_init_target")
            target = session.target
            assert isinstance(target, HC32F4A0xI)

            flash_regions = tuple(region for region in target.memory_map if region.is_flash)
            flash_snapshots = [
                (region.start, region.length, copy.deepcopy(region.algo),
                 copy.copy(region.attributes))
                for region in flash_regions
            ]
            backup_ram = target.memory_map.get_region_for_address(0x200F0000)
            assert backup_ram.is_ram and backup_ram.length == 0x1000
            visited = []

            def check_before_sequence():
                ram = target.memory_map.get_region_for_address(0x1FFE0000)
                assert ram.is_ram and ram.start == 0x1FFE0000
                assert ram.length == 0x80000 and ram.end == 0x2005FFFF
                assert target.memory_map.get_region_for_address(0x20060000) is None
                assert target.memory_map.get_region_for_address(0x200F0000) is backup_ram
                visited.append(True)

            # Board.init reaches the actual delegate before invoking this harmless sequence.
            with patch.object(
                target, "create_init_sequence",
                return_value=CallSequence(("offline_check", check_before_sequence)),
            ):
                session.board.init()
                session.board.init()
            assert len(visited) == 2
            assert not session.is_open
            assert tuple(region for region in target.memory_map if region.is_flash) == flash_regions
            for region, snapshot in zip(flash_regions, flash_snapshots):
                assert (region.start, region.length, region.algo, region.attributes) == snapshot
            assert HC32F4A0xI.MEMORY_MAP == original_builtin_map
            assert target.memory_map.get_boot_memory().length == 0x200000
            return {
                "status": "PASS",
                "pyocd_version": pyocd.__version__,
                "target": session.options["target_override"],
                "swd_frequency_hz": session.options["frequency"],
                "main_flash": "0x00000000..0x001FFFFF (2 MiB)",
                "main_ram": "0x1FFE0000..0x2005FFFF (512 KiB)",
                "backup_ram": "0x200F0000..0x200F0FFF (4 KiB)",
                "relative_script_resolved_with_project_from_unrelated_cwd": True,
                "flash_regions_and_algorithms_unchanged": True,
                "builtin_class_map_unchanged": True,
                "real_session_user_script_and_init_hook_verified": True,
                "probe_opened": False,
                "hardware_tested": False,
            }
        finally:
            os.chdir(original_cwd)


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
