# SPDX-License-Identifier: Apache-2.0
"""Apply series-native footer, slide fields and 120% paragraph spacing."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import copy, json, posixpath, sys
from lxml import etree as E
NS={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def tag(prefix,name): return '{'+NS[prefix]+'}'+name
def serialize(x): return E.tostring(x,xml_declaration=True,encoding='UTF-8',standalone=True)
def target(parts,owner,role):
    rel=posixpath.join(posixpath.dirname(owner),'_rels',posixpath.basename(owner)+'.rels')
    t=next(x.get('Target') for x in E.fromstring(parts[rel]) if x.get('Type').endswith('/'+role))
    return t.lstrip('/') if t.startswith('/') else posixpath.normpath(posixpath.join(posixpath.dirname(owner),t))
def run(candidate,output,reference):
    with ZipFile(candidate) as z: parts={n:z.read(n) for n in z.namelist()}
    with ZipFile(reference) as z: ref={n:z.read(n) for n in z.namelist()}
    foot=None
    for n,b in ref.items():
        if n.startswith('ppt/slideMasters/slideMaster') and n.endswith('.xml'):
            for s in E.fromstring(b).findall('.//p:sp',NS):
                if s.find('p:nvSpPr/p:cNvPr',NS).get('name')=='Footer signature lizhaojun': foot=copy.deepcopy(s);break
        if foot is not None: break
    assert foot is not None
    page=None
    for s in E.fromstring(ref['ppt/slides/slide2.xml']).findall('.//p:sp',NS):
        if s.find('.//a:fld',NS) is not None: page=copy.deepcopy(s);break
    assert page is not None
    coverMaster=target(parts,target(parts,'ppt/slides/slide1.xml','slideLayout'),'slideMaster')
    for n in list(parts):
        if n.startswith('ppt/slideMasters/slideMaster') and n.endswith('.xml'):
            root=E.fromstring(parts[n]); tree=root.find('p:cSld/p:spTree',NS); f=copy.deepcopy(foot)
            ids=[int(x.get('id')) for x in root.findall('.//p:cNvPr',NS)]
            f.find('p:nvSpPr/p:cNvPr',NS).set('id',str(max(ids+[1])+1))
            for c in f.findall('.//a:srgbClr',NS): c.set('val','D4CDE8' if n==coverMaster else '646173')
            tree.append(f);parts[n]=serialize(root)
    for n in list(parts):
        if n.startswith('ppt/slides/slide') and n.endswith('.xml'):
            root=E.fromstring(parts[n]); num=int(Path(n).stem.removeprefix('slide')); tree=root.find('p:cSld/p:spTree',NS)
            if num==1:
                # Put the artwork behind master graphics, so the footer remains visible.
                pic=tree.find('p:pic',NS)
                if pic is not None:
                    cSld=root.find('p:cSld',NS); old=cSld.find('p:bg',NS)
                    if old is not None: cSld.remove(old)
                    bg=E.Element(tag('p','bg')); bgPr=E.SubElement(bg,tag('p','bgPr'))
                    fill=copy.deepcopy(pic.find('p:blipFill',NS));fill.tag=tag('a','blipFill')
                    bgPr.append(fill);E.SubElement(bgPr,tag('a','effectLst'));cSld.insert(0,bg);tree.remove(pic)
            else:
                f=copy.deepcopy(page);ids=[int(x.get('id')) for x in root.findall('.//p:cNvPr',NS)]
                f.find('p:nvSpPr/p:cNvPr',NS).set('id',str(max(ids+[1])+1))
                f.find('p:nvSpPr/p:cNvPr',NS).set('name','PageNumber')
                f.find('.//a:fld/a:t',NS).text=str(num);tree.append(f)
            for shape in root.findall('.//p:sp',NS):
                name=shape.find('p:nvSpPr/p:cNvPr',NS).get('name','')
                if name in ['PageNumber','Reading link','Stage','Chapter','Subtitle','Presenter lizhaojun']:continue
                for p in shape.findall('.//a:p',NS):
                    pr=p.find('a:pPr',NS)
                    if pr is None: pr=E.Element(tag('a','pPr'));p.insert(0,pr)
                    old=pr.find('a:lnSpc',NS)
                    if old is not None:pr.remove(old)
                    spacing=E.Element(tag('a','lnSpc'));E.SubElement(spacing,tag('a','spcPct'),val='120000');pr.insert(0,spacing)
            parts[n]=serialize(root)
        elif n.startswith('ppt/slides/_rels/') and n.endswith('.rels'):
            r=E.fromstring(parts[n])
            for x in r:
                if x.get('Type').endswith('/hyperlink') and x.get('Target')=='../x':
                    x.set('Target','P001_VSCode_Zephyr_IDE接入已有工程_Windows.md')
            parts[n]=serialize(r)
    with ZipFile(output,'w',ZIP_DEFLATED) as z:
        for n,b in parts.items(): z.writestr(n,b)
    print(output)
if __name__=='__main__':run(*sys.argv[1:])
