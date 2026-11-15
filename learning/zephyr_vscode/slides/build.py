# SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
# SPDX-License-Identifier: Apache-2.0
"""Rebuild the teaching deck, or sync PowerPoint edits back to Open XML sources."""

import argparse
import json
import posixpath
from pathlib import Path, PurePosixPath
import tempfile
import xml.etree.ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "src"
MANIFEST = HERE / "source.json"
DECK = HERE.parent / "P001_VSCode_Zephyr_IDE接入已有工程_Windows.pptx"
NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def inspect_master_links(parts):
    """Reject copied slides whose masters are absent from the presentation.

    A renderer can follow a layout's relationship to an unregistered master,
    while PowerPoint rejects the same package. Check both directions here.
    """
    def relationships(owner):
        folder, name = posixpath.split(owner)
        rel_part = posixpath.join(folder, "_rels", name + ".rels")
        if rel_part not in parts:
            return {}
        result = {}
        for rel in ET.fromstring(parts[rel_part]):
            if rel.get("TargetMode") == "External":
                continue
            target = rel.attrib["Target"]
            target = (target.lstrip("/") if target.startswith("/") else
                      posixpath.normpath(posixpath.join(folder, target)))
            result[rel.attrib["Id"]] = (rel.attrib["Type"].rsplit("/", 1)[-1], target)
        return result

    presentation = ET.fromstring(parts["ppt/presentation.xml"])
    rels = relationships("ppt/presentation.xml")

    def registered(path, role):
        targets = set()
        for ref in presentation.findall(path, NS):
            rid = ref.attrib[f"{{{NS['r']}}}id"]
            if rid not in rels or rels[rid][0] != role:
                raise ValueError(f"Invalid {role} registration: {rid}")
            targets.add(rels[rid][1])
        return targets

    masters = registered("p:sldMasterIdLst/p:sldMasterId", "slideMaster")
    notes_masters = registered("p:notesMasterIdLst/p:notesMasterId", "notesMaster")
    if len(notes_masters) > 1:
        raise ValueError("PowerPoint requires a single notes master")
    layout_ids = set()
    layouts_by_master = {}
    for master in masters:
        refs = relationships(master)
        layouts_by_master[master] = set()
        for layout in ET.fromstring(parts[master]).findall("p:sldLayoutIdLst/p:sldLayoutId", NS):
            identifier = layout.attrib["id"]
            if identifier in layout_ids:
                raise ValueError(f"Duplicate presentation-wide layout ID: {identifier}")
            layout_ids.add(identifier)
            rid = layout.attrib[f"{{{NS['r']}}}id"]
            if rid not in refs or refs[rid][0] != "slideLayout":
                raise ValueError(f"Invalid slideLayout registration in {master}: {rid}")
            layouts_by_master[master].add(refs[rid][1])

    for slide in registered("p:sldIdLst/p:sldId", "slide"):
        for role, part in relationships(slide).values():
            if role == "slideLayout":
                linked = [target for kind, target in relationships(part).values()
                          if kind == "slideMaster"]
                if len(linked) != 1 or linked[0] not in masters:
                    raise ValueError(f"Unregistered slide master used by {slide}: {linked}")
                if part not in layouts_by_master[linked[0]]:
                    raise ValueError(f"Layout not registered by its master: {part}")
            elif role == "notesSlide":
                linked = [target for kind, target in relationships(part).values()
                          if kind == "notesMaster"]
                if len(linked) != 1 or linked[0] not in notes_masters:
                    raise ValueError(f"Unregistered notes master used by {part}: {linked}")


def source_path(name):
    part = PurePosixPath(name)
    if part.is_absolute() or ".." in part.parts or "\\" in name or ":" in name:
        raise ValueError(f"Unsafe package path: {name}")
    target = (SOURCE / name).resolve()
    if not target.is_relative_to(SOURCE.resolve()):
        raise ValueError(f"Path outside source directory: {name}")
    return target


def inspect_package(parts):
    """Read the actual presentation order, which can differ from XML filenames."""
    inspect_master_links(parts)
    presentation = ET.fromstring(parts["ppt/presentation.xml"])
    relationships = ET.fromstring(parts["ppt/_rels/presentation.xml.rels"])
    targets = {r.attrib["Id"]: r.attrib["Target"] for r in relationships}
    slides = []
    for number, ref in enumerate(presentation.findall("p:sldIdLst/p:sldId", NS), 1):
        target = targets[ref.attrib[f"{{{NS['r']}}}id"]]
        part = target.lstrip("/") if target.startswith("/") else "ppt/" + target
        source_path(part)
        slide = ET.fromstring(parts[part])
        fields = slide.findall(".//a:fld[@type='slidenum']", NS)
        if len(fields) != (0 if number == 1 else 1):
            raise ValueError(f"Slide {number}: expected one automatic number (none on cover)")
        title_shape = slide.find(".//p:sp", NS)
        title = "" if title_shape is None else "".join(title_shape.itertext())
        # Extract only visible title text, excluding XML formatting whitespace.
        if title_shape is not None:
            title = "".join(t.text or "" for t in title_shape.findall(".//a:t", NS))
        slides.append({"number": number, "title": title, "part": part})
    if not slides:
        raise ValueError("Presentation has no slides")
    return slides


def sync(input_path):
    with ZipFile(input_path) as archive:
        if archive.testzip():
            raise ValueError("Damaged PPTX package")
        parts = {n: archive.read(n) for n in archive.namelist() if not n.endswith("/")}
    for name in parts:
        source_path(name)
    slides = inspect_package(parts)
    old_names = json.loads(MANIFEST.read_text(encoding="utf-8"))["parts"] if MANIFEST.exists() else []
    for name, data in parts.items():
        target = source_path(name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    # Only remove previously registered package parts, never unrelated files.
    for name in set(old_names) - set(parts):
        source_path(name).unlink(missing_ok=True)
    MANIFEST.write_text(json.dumps({"format": 1, "slides": slides, "parts": sorted(parts)},
                                   ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Synced {len(slides)} slides into {SOURCE}")


def build(output_path, force):
    if output_path.exists() and not force:
        raise FileExistsError(f"Output exists; use --force to replace: {output_path}")
    if output_path.is_relative_to(SOURCE.resolve()):
        raise ValueError("Output must not be inside src")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    parts = {name: source_path(name).read_bytes() for name in manifest["parts"]}
    slides = inspect_package(parts)
    if slides != manifest["slides"]:
        raise ValueError("Slide order/title differs from source.json; update the manifest as well")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=output_path.parent, suffix=".pptx", delete=False) as temp:
        temp_path = Path(temp.name)
    try:
        with ZipFile(temp_path, "w", ZIP_DEFLATED) as archive:
            for name, data in parts.items():
                archive.writestr(name, data)
        with ZipFile(temp_path) as archive:
            if archive.testzip():
                raise ValueError("Rebuilt package failed ZIP integrity check")
        temp_path.replace(output_path)
    finally:
        temp_path.unlink(missing_ok=True)
    print(f"Built {len(slides)} slides: {output_path}")


def main():
    global SOURCE, MANIFEST, DECK
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    rebuild = sub.add_parser("build", help="Rebuild from src; requires Python 3.10+ only")
    rebuild.add_argument("--output", type=Path)
    rebuild.add_argument("--force", action="store_true")
    update = sub.add_parser("sync", help="Sync saved PPTX edits back into src")
    update.add_argument("--input", type=Path)
    args = parser.parse_args()
    if args.action == "sync":
        sync((args.input or DECK).resolve())
    else:
        build((args.output or DECK).resolve(), args.force)


if __name__ == "__main__":
    main()
