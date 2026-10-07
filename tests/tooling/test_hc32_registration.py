# SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Keep the integrated and standalone HC32 hardware registrations usable."""

from pathlib import Path
import subprocess
import sys
import unittest

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "learning/board/labs/hc32_port"
BOARD = Path("boards/uyup/uyup_rpi_a")
SOC = Path("soc/xhsc/hc32f4a0")


def read_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


class HardwareRegistrationTests(unittest.TestCase):
    def test_native_schemas_and_matching_hardware_identity(self):
        for relative, schema_name in (
            (BOARD / "board.yml", "board-schema.yaml"),
            (SOC / "soc.yml", "soc-schema.yaml"),
            (BOARD / "uyup_rpi_a_hc32f4a0pitb.yaml", "twister/platform-schema.yaml"),
        ):
            schema = read_yaml(ROOT / "scripts/schemas" / schema_name)
            with self.subTest(file=str(relative)):
                integrated = read_yaml(ROOT / relative)
                standalone = read_yaml(MODULE / relative)
                jsonschema.validate(integrated, schema)
                jsonschema.validate(standalone, schema)
                if "supported" in integrated:
                    # The standalone lab is the GPIO/UART teaching stage.
                    # Native USB and HWINFO are later integrated-tree work.
                    self.assertEqual(
                        set(integrated.pop("supported")),
                        set(standalone.pop("supported")) | {"usb_device", "hwinfo"},
                    )
                self.assertEqual(integrated, standalone)
        meta = read_yaml(MODULE / "zephyr/module.yml")
        jsonschema.validate(meta, read_yaml(ROOT / "scripts/schemas/module-schema.yaml"))
        for setting in ("board_root", "soc_root", "dts_root"):
            self.assertEqual(meta["build"]["settings"][setting], ".")

    def test_standalone_vendor_registration(self):
        # Do not let vendor entries in the integrated tree mask a module omission.
        prefixes = {}
        for line in (MODULE / "dts/bindings/vendor-prefixes.txt").read_text().splitlines():
            if line and not line.startswith("#"):
                key, value = line.split("\t", 1)
                self.assertNotIn(key, prefixes)
                prefixes[key] = value
        vendor = read_yaml(MODULE / BOARD / "board.yml")["board"]["vendor"]
        self.assertIn(vendor, prefixes)
        for binding in (MODULE / "dts/bindings").rglob("*.yaml"):
            compatible = read_yaml(binding).get("compatible", "")
            if compatible:
                self.assertIn(compatible.split(",", 1)[0], prefixes)

    def test_native_board_discovery_in_each_root(self):
        for root in (ROOT, MODULE):
            with self.subTest(root=str(root)):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "scripts/list_boards.py"),
                     "--board-root", str(root), "--soc-root", str(root),
                     "--arch-root", str(ROOT), "--board", "uyup_rpi_a",
                     "--cmakeformat", "{NAME}|{VENDOR}|{QUALIFIERS}|{DIR}"],
                    cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("NAME;uyup_rpi_a|VENDOR;uyup|QUALIFIERS;hc32f4a0pitb", result.stdout)
                self.assertIn((root / BOARD).as_posix(), result.stdout)


if __name__ == "__main__":
    unittest.main()
