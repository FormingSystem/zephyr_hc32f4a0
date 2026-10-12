# SPDX-License-Identifier: Apache-2.0
"""Preserve the saved P001 cover/theme and package reviewed artifact-tool body slides."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
import copy,json,posixpath,uuid,hashlib,io,sys
from PIL import Image
if len(sys.argv)!=4:
 raise SystemExit('Usage: finish_package.py authored.pptx output.pptx saved-reference.pptx')
AUTHORED,OUTPUT,REFERENCE=[Path(p).resolve() for p in sys.argv[1:]]
if OUTPUT.exists():raise FileExistsError(OUTPUT)
if OUTPUT in (AUTHORED,REFERENCE):raise ValueError('Use a new private output file')
HERE=Path(__file__).resolve().parent
W=OUTPUT.parent
W.mkdir(parents=True,exist_ok=True)
N={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships','rel':'http://schemas.openxmlformats.org/package/2006/relationships','ct':'http://schemas.openxmlformats.org/package/2006/content-types'}
def q(n):a,b=n.split(':');return '{'+N[a]+'}'+b
def xml(e):return E.tostring(e,xml_declaration=True,encoding='UTF-8',standalone=True)
def read(p):
 with ZipFile(p) as z:return {n:z.read(n) for n in z.namelist()}
def rp(part):return posixpath.join(posixpath.dirname(part),'_rels',posixpath.basename(part)+'.rels')
def reltarget(part,t):return t.lstrip('/') if t.startswith('/') else posixpath.normpath(posixpath.join(posixpath.dirname(part),t))
parts=read(REFERENCE);a=read(AUTHORED);data=json.loads((HERE/'content.json').read_text(encoding='utf-8'))
sourcehash=hashlib.sha256(REFERENCE.read_bytes()).hexdigest()
if any(n.startswith('ppt/comments/') for n in parts):raise ValueError('Need manual comment mapping before body rewrite')
presentation=E.fromstring(parts['ppt/presentation.xml'])
presentation_rels=E.fromstring(parts['ppt/_rels/presentation.xml.rels'])
slide_refs={e.get('Id'):reltarget('ppt/presentation.xml',e.get('Target')) for e in presentation_rels}
second=slide_refs[presentation.find('p:sldIdLst',N)[1].get(q('r:id'))]
base=E.fromstring(parts[second]);bt=base.find('p:cSld/p:spTree',N)
page=copy.deepcopy(next(s for s in bt if s.find('.//a:fld[@type="slidenum"]',N) is not None))
rels=E.fromstring(parts[rp(second)]);layout=next(e.get('Target') for e in rels if e.get('Type').endswith('/slideLayout'))
notePath=reltarget(second,next(e.get('Target') for e in rels if e.get('Type').endswith('/notesSlide')))
noteTemplate=E.fromstring(parts[notePath]);noteRelTemplate=E.fromstring(parts[rp(notePath)])
coverNotes=reltarget('ppt/slides/slide1.xml',next(e.get('Target') for e in E.fromstring(parts[rp('ppt/slides/slide1.xml')]) if e.get('Type').endswith('/notesSlide')))
# Preserve the saved cover, masters, layouts, theme, native signature and assets.
cover=E.fromstring(parts['ppt/slides/slide1.xml'])
for shape in cover.findall('.//p:sp',N):
 name=shape.find('p:nvSpPr/p:cNvPr',N).get('name','')
 if name=='Title':
  ts=shape.findall('.//a:t',N)
  if len(ts)>=2:ts[0].text='Zephyr IDE';ts[1].text='从零理解与使用'
 if name=='Subtitle':
  for t in shape.findall('.//a:t',N):t.text='Windows · 工程、依赖与图形界面操作'
parts['ppt/slides/slide1.xml']=xml(cover)
covernote=E.fromstring(parts[coverNotes])
for shape in covernote.findall('.//p:sp',N):
 ph=shape.find('p:nvSpPr/p:nvPr/p:ph',N)
 if ph is not None and ph.get('type')=='body':
  tx=shape.find('p:txBody',N)
  for par in tx.findall('a:p',N):tx.remove(par)
  for line in ['对应同名 Markdown 1.1—1.11；从原生工程组成讲到 IDE 入口、配置与构建产物。','主讲人：lizhaojun。插件依据：mylonics/zephyr-ide 4.1.1-prerelease，固定提交 1f046e660bfe1ba4720d58abccd69d1aaf903f83。','本轮界面截图只证明对应入口；CLI 构建、GUI 操作、硬件验证分开记录。详见配套 VALIDATION.md。']:
   par=E.SubElement(tx,q('a:p'));run=E.SubElement(par,q('a:r'));E.SubElement(run,q('a:t')).text=line
parts[coverNotes]=xml(covernote)
pres=E.fromstring(parts['ppt/presentation.xml']);pr=E.fromstring(parts['ppt/_rels/presentation.xml.rels']);types=E.fromstring(parts['[Content_Types].xml']);sid=pres.find('p:sldIdLst',N)
coverId=sid[0].get(q('r:id'))
for e in list(sid)[1:]:sid.remove(e)
for r in list(pr):
 if r.get('Type').endswith('/slide') and r.get('Id')!=coverId:pr.remove(r)
for n in list(parts):
 if (n.startswith('ppt/slides/') and n not in ['ppt/slides/slide1.xml',rp('ppt/slides/slide1.xml')]) or (n.startswith('ppt/notesSlides/') and n not in [coverNotes,rp(coverNotes)]):del parts[n]
for e in list(types):
 n=e.get('PartName','').lstrip('/')
 if (n.startswith('ppt/slides/') or n.startswith('ppt/notesSlides/')) and n not in parts:types.remove(e)
srcroot='https://github.com/mylonics/zephyr-ide/blob/1f046e660bfe1ba4720d58abccd69d1aaf903f83/'
sources={
'1.1':[srcroot+'readme.md#features','https://docs.zephyrproject.org/latest/build/cmake/index.html'],
'1.2':['https://docs.zephyrproject.org/latest/develop/west/basics.html','https://docs.zephyrproject.org/latest/develop/modules.html#without-west',srcroot+'src/zephyr_utilities/build.ts#L196'],
'1.3':['https://docs.zephyrproject.org/latest/develop/west/built-in.html#west-list','https://docs.zephyrproject.org/latest/develop/modules.html','G:/zephyr_practice/zephyr-main/west.yml','G:/zephyr_practice/hal_xhsc-zephyr/zephyr/module.yml'],
'1.4':['https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html',srcroot+'src/setup_utilities/workspace-config.ts#L634'],
'1.5':[srcroot+'package.json','https://marketplace.visualstudio.com/items?itemName=mylonics.zephyr-ide'],
'1.6':[srcroot+'src/panels/settings_view/SettingsPanel.ts#L33',srcroot+'src/panels/settings_view/SettingsPanel.ts#L397'],
'1.7':[srcroot+'src/setup_utilities/workspace-setup.ts#L935',srcroot+'src/setup_utilities/west-operations.ts#L575',srcroot+'src/extension.ts#L1195'],
'1.8':[srcroot+'src/project_utilities/project.ts#L65',srcroot+'src/project_utilities/project.ts#L822',srcroot+'src/project_utilities/build_selector.ts#L405','G:/zephyr_practice/zephyr-main/samples/hello_world/CMakeLists.txt'],
'1.9':[srcroot+'src/project_utilities/project.ts#L338',srcroot+'src/project_utilities/build_args.ts#L146','https://docs.zephyrproject.org/latest/develop/modules.html','G:/zephyr_practice/zephyr-main/cmake/modules/zephyr_module.cmake','G:/zephyr_practice/hal_xhsc-zephyr/CMakeLists.txt'],
'1.10':[srcroot+'src/zephyr_utilities/build.ts#L196','https://docs.zephyrproject.org/latest/develop/west/build-flash-debug.html','https://code.visualstudio.com/docs/cpp/customize-cpp-settings#_compilecommands'],
'1.11':[srcroot+'package.json','https://github.com/zephyrproject-rtos/zephyr/discussions/48837','https://www.msys2.org/docs/git/']}
order=['ln','noFill','solidFill','gradFill','blipFill','pattFill','grpFill','effectLst','effectDag','highlight','uLnTx','uLn','uFillTx','uFill','latin','ea','cs','sym','hlinkClick','hlinkMouseOver','rtl','extLst']
for num,d in enumerate(data[1:],2):
 root=copy.deepcopy(base);tree=root.find('p:cSld/p:spTree',N)
 for e in list(tree):
  if e.tag not in [q('p:nvGrpSpPr'),q('p:grpSpPr')]:tree.remove(e)
 authored=E.fromstring(a[f'ppt/slides/slide{num}.xml'])
 for e in authored.find('p:cSld/p:spTree',N):
  if e.tag in [q('p:sp'),q('p:pic'),q('p:graphicFrame'),q('p:cxnSp')]:tree.append(copy.deepcopy(e))
 rel=E.Element(q('rel:Relationships'),nsmap={None:N['rel']})
 for rid,typ,target in [('rIdLayout','slideLayout',layout),('rIdNotes','notesSlide',f'../notesSlides/ide{num}.xml'),('rIdReading','hyperlink','P001_VSCode_Zephyr_IDE接入已有工程_Windows.md')]:
  attrs={'Id':rid,'Type':N['r']+'/'+typ,'Target':target}
  if typ=='hyperlink':attrs['TargetMode']='External'
  E.SubElement(rel,q('rel:Relationship'),**attrs)
 for imgnum,blip in enumerate(root.findall('.//a:blip',N),1):
  rid=blip.get(q('r:embed'))
  ars=E.fromstring(a[rp(f'ppt/slides/slide{num}.xml')]);ir=next(r for r in ars if r.get('Id')==rid)
  old=reltarget(f'ppt/slides/slide{num}.xml',ir.get('Target'));media=f'ppt/media/ide{num}-{imgnum}.jpg';parts[media]=a[old]
  newrid='rIdImage'+str(imgnum);blip.set(q('r:embed'),newrid);E.SubElement(rel,q('rel:Relationship'),Id=newrid,Type=N['r']+'/image',Target='../media/'+posixpath.basename(media))
  # Native PowerPoint cropping, keeping the original screenshot bytes intact.
  imagefile=d['image'];rect=(425,8,600,224) if '02-' in imagefile else (450,301,942,341) if '03-' in imagefile else (48,516,365,201)
  iw,ih=Image.open(io.BytesIO(parts[media])).size;x,y,cw,ch=rect
  fill=blip.getparent();existing=fill.find('a:srcRect',N)
  if existing is not None:fill.remove(existing)
  crop=E.Element(q('a:srcRect'),l=str(round(x/iw*100000)),t=str(round(y/ih*100000)),r=str(round((iw-x-cw)/iw*100000)),b=str(round((ih-y-ch)/ih*100000)));fill.insert(1,crop)
  pic=fill.getparent();xf=pic.find('p:spPr/a:xfrm',N);width=min(775,386*cw/ch);h=width*ch/cw
  xf.find('a:off',N).set('x',str(round((64+(775-width)/2)*9525)));xf.find('a:off',N).set('y',str(round((190+(386-h)/2)*9525)));xf.find('a:ext',N).set('cx',str(round(width*9525)));xf.find('a:ext',N).set('cy',str(round(h*9525)))
 footer=copy.deepcopy(page);fld=footer.find('.//a:fld',N);fld.set('id','{'+str(uuid.uuid4()).upper()+'}');fld.find('a:t',N).text=str(num);tree.append(footer)
 for s in root.findall('.//p:sp',N):
  name=s.find('p:nvSpPr/p:cNvPr',N).get('name','')
  if name=='Reading link':
   for run in s.findall('.//a:r',N):
    props=run.find('a:rPr',N)
    if props is None:props=E.Element(q('a:rPr'));run.insert(0,props)
    E.SubElement(props,q('a:hlinkClick'),attrib={q('r:id'):'rIdReading'})
 for para in root.findall('.//a:p',N):
  props=para.find('a:pPr',N)
  if props is None:props=E.Element(q('a:pPr'));para.insert(0,props)
  for sp in props.findall('a:lnSpc',N):props.remove(sp)
  sp=E.Element(q('a:lnSpc'));E.SubElement(sp,q('a:spcPct'),val='120000');props.insert(0,sp)
 for rpr in root.findall('.//a:rPr',N)+root.findall('.//a:defRPr',N)+root.findall('.//a:endParaRPr',N):
  children=list(rpr)
  for e in children:rpr.remove(e)
  for e in sorted(children,key=lambda e:order.index(E.QName(e).localname) if E.QName(e).localname in order else 999):rpr.append(e)
 for idx,cn in enumerate(root.findall('.//p:cNvPr',N),1):cn.set('id',str(idx))
 for ext in root.findall('.//p:extLst',N)+root.findall('.//a:extLst',N):ext.getparent().remove(ext)
 part=f'ppt/slides/ide{num}.xml';parts[part]=xml(root);parts[rp(part)]=xml(rel)
 note=copy.deepcopy(noteTemplate);nr=copy.deepcopy(noteRelTemplate)
 for r in nr:
  if r.get('Type').endswith('/slide'):r.set('Target',f'../slides/ide{num}.xml')
 notes='对应配套 Markdown '+d['section']+'。\n'+'\n'.join(d['body'])+'\n依据（版本固定的插件代码，网页为官方在线说明）：\n'+'\n'.join(sources.get(d['section'],[]))
 if d.get('image'):notes+='\n图像来源：本机 VS Code 4.1.1 界面，2026-10-10；'+d['caption']+'；本页采用原生裁切放大，原图保存在 assets/'+d['image']+'。截图只用于查找操作入口。'
 for shape in note.findall('.//p:sp',N):
  ph=shape.find('p:nvSpPr/p:nvPr/p:ph',N)
  if ph is not None and ph.get('type')=='body':
   tx=shape.find('p:txBody',N)
   for e in tx.findall('a:p',N):tx.remove(e)
   for line in notes.split('\n'):
    par=E.SubElement(tx,q('a:p'));run=E.SubElement(par,q('a:r'));E.SubElement(run,q('a:t')).text=line
  if ph is not None and ph.get('type')=='sldNum':
   for t in shape.findall('.//a:t',N):t.text=str(num)
 np=f'ppt/notesSlides/ide{num}.xml';parts[np]=xml(note);parts[rp(np)]=xml(nr)
 rid='rIdIde'+str(num);E.SubElement(pr,q('rel:Relationship'),Id=rid,Type=N['r']+'/slide',Target=f'slides/ide{num}.xml');E.SubElement(sid,q('p:sldId'),id=str(500+num),attrib={q('r:id'):rid})
 for folder,typ in [('slides','slide'),('notesSlides','notesSlide')]:E.SubElement(types,q('ct:Override'),PartName=f'/ppt/{folder}/ide{num}.xml',ContentType=f'application/vnd.openxmlformats-officedocument.presentationml.{typ}+xml')
parts['ppt/presentation.xml']=xml(pres);parts['ppt/_rels/presentation.xml.rels']=xml(pr);parts['[Content_Types].xml']=xml(types)
if not any(e.get('Extension')=='jpg' for e in types):E.SubElement(types,q('ct:Default'),Extension='jpg',ContentType='image/jpeg')
parts['[Content_Types].xml']=xml(types)
app=E.fromstring(parts['docProps/app.xml']);app.find('{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}Slides').text=str(len(data));parts['docProps/app.xml']=xml(app)
with ZipFile(OUTPUT,'w',ZIP_DEFLATED) as z:
 for n,b in parts.items():z.writestr(n,b)
(W/'baseline-hash.json').write_text(json.dumps({'original':sourcehash,'slides':len(data),'tables':[i+1 for i,d in enumerate(data) if d.get('table')]},indent=2))
print('Packaged',len(data),'slides; saved cover, masters and original image bytes retained')
