# SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Regression checks for merged-deck defects rejected by native PowerPoint."""

import unittest
import posixpath
import xml.etree.ElementTree as ET
from zipfile import ZipFile

import build


class MasterLinksTest(unittest.TestCase):
    def setUp(self):
        with ZipFile(next(build.HERE.glob("P002*.pptx"))) as archive:
            self.parts = {name: archive.read(name) for name in archive.namelist()}

    def test_formal_decks(self):
        for path in build.HERE.glob("*.pptx"):
            if path.name.startswith("~$"):
                continue  # PowerPoint owner lock files are not presentation packages.
            with self.subTest(deck=path.name), ZipFile(path) as archive:
                build.inspect_master_links({name: archive.read(name) for name in archive.namelist()})

    def test_unregistered_copied_master(self):
        root = ET.fromstring(self.parts["ppt/presentation.xml"])
        masters = root.find("p:sldMasterIdLst", build.NS)
        self.assertGreater(len(masters), 1)
        masters.remove(masters[-1])
        self.parts["ppt/presentation.xml"] = ET.tostring(root)
        with self.assertRaisesRegex(ValueError, "Unregistered slide master"):
            build.inspect_master_links(self.parts)

    def test_unregistered_notes_master(self):
        root = ET.fromstring(self.parts["ppt/presentation.xml"])
        root.remove(root.find("p:notesMasterIdLst", build.NS))
        self.parts["ppt/presentation.xml"] = ET.tostring(root)
        with self.assertRaisesRegex(ValueError, "Unregistered notes master"):
            build.inspect_master_links(self.parts)

    def test_duplicate_layout_identifiers(self):
        presentation = ET.fromstring(self.parts["ppt/presentation.xml"])
        relationships = ET.fromstring(self.parts["ppt/_rels/presentation.xml.rels"])
        targets = {r.attrib["Id"]: r.attrib["Target"] for r in relationships}
        masters = []
        for ref in presentation.findall("p:sldMasterIdLst/p:sldMasterId", build.NS):
            target = targets[ref.attrib[f"{{{build.NS['r']}}}id"]]
            masters.append(target.lstrip("/") if target.startswith("/") else
                           posixpath.normpath("ppt/" + target))
        self.assertGreater(len(masters), 1)
        key = masters[1]
        original = ET.fromstring(self.parts[masters[0]])
        first = original.find("p:sldLayoutIdLst/p:sldLayoutId", build.NS)
        copied = ET.fromstring(self.parts[key])
        copied.find("p:sldLayoutIdLst/p:sldLayoutId", build.NS).set("id", first.attrib["id"])
        self.parts[key] = ET.tostring(copied)
        with self.assertRaisesRegex(ValueError, "Duplicate presentation-wide layout ID"):
            build.inspect_master_links(self.parts)


if __name__ == "__main__":
    unittest.main()
