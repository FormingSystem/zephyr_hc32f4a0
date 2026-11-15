// SPDX-License-Identifier: Apache-2.0
// 2026-10-10 rewrite. First preserve saved PowerPoint changes using build.py sync.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
for (const key of ['RUNTIME_NODE_MODULES','TOPIC_DIR','TMP_DIR']) {
 if (!process.env[key]) throw new Error('Set '+key+' before authoring a private candidate');
}
const require=createRequire(path.join(process.env.RUNTIME_NODE_MODULES,'__artifact_entry__.cjs'));
const {Presentation,PresentationFile}=require('@oai/artifact-tool');
const w=path.resolve(process.env.TMP_DIR);
const topic=path.resolve(process.env.TOPIC_DIR);
await fs.mkdir(w,{recursive:true});
const ds=JSON.parse(await fs.readFile(path.join(topic,'slides/content.json'),'utf8'));
const p=Presentation.create({slideSize:{width:1280,height:720}});
const C={text:'#29263B',path:'#0070C0',arg:'#B84E00',cmd:'#A02B93',fun:'#087B3D',muted:'#646173',purple:'#7350BC'};
function rich(t){
 const rx=/(hal_xhsc-zephyr\/?|zephyr-sdk-1\.0\.1\/?|zephyr-main\/|\.venv\/|hc32_port\/boards|zephyr-vscode\/[\w/-]+|python\.exe|boards\b|CMAKE_EXPORT_COMPILE_COMMANDS|G:\/[^\s，；。]+|\/g\/[^\s，；。]+|\$\{workspaceFolder\}\/[^\s"]+|(?:\.vscode\/|modules\/|samples\/|build\/|zephyr\/|boards\/|\.venv\/|\.west\/)[^\s，。；：]+|(?:settings\.json|zephyr-ide\.json|west\.yml|module\.yml|zephyr_modules\.txt|CMakeLists\.txt|CMakeCache\.txt|compile_commands\.json|prj\.conf|zephyr\.elf|zephyr\.dts)|(?:zephyr-ide\.[\w.]+|C_Cpp\.[\w.]+|EXTRA_ZEPHYR_MODULES|ZEPHYR_MODULES|ZEPHYR_SDK_INSTALL_DIR|CMAKE_C_COMPILER|BOARD|CONFIG_[A-Z0-9_]+|ZEPHYR_BASE|westBuildCMakeArgs|relPath|board|relBoardSubDir)|(?:find_package|target_sources|project|cmake_minimum_required)(?=\()|\b(?:west|python|source|cd|cmake|ninja)\b)/g;
 let last=0,r=[];for(const m of t.matchAll(rx)){if(m.index>last)r.push(t.slice(last,m.index));let v=m[0];let col=/^(?:hal_xhsc-zephyr|zephyr-sdk-1\.0\.1|zephyr-main\/|\.venv\/|hc32_port\/boards|zephyr-vscode\/|python\.exe|boards$)/.test(v)?C.path:/^(?:G:|\/g|\$\{|\.vscode\/|modules\/|samples\/|build\/|zephyr\/|boards\/|\.venv\/|\.west\/)/.test(v)||/\.(?:json|yml|txt|conf|elf|dts)$/.test(v)?C.path:/^(?:find_package|target_sources|project|cmake_minimum_required)$/.test(v)?C.fun:/^(west|python|source|cd|cmake|ninja)$/.test(v)?C.cmd:C.arg;r.push({run:v,textStyle:{color:col}});last=m.index+v.length;}if(last<t.length)r.push(t.slice(last));return r.length?r:[''];
}
function tx(s,name,text,x,y,width,height,size=28,opts={}){
 const t=s.shapes.add({name,geometry:'textbox',position:{left:x,top:y,width,height},fill:'none',line:{fill:'none',width:0}});
 t.text.style={fontSize:size,typeface:opts.code?'Consolas':'Microsoft YaHei',color:opts.color||C.text,bold:opts.bold||false,autoFit:'none',wrap:true,verticalAlignment:'top',insets:{left:0,right:0,top:0,bottom:0},lineSpacing:1.2};
 t.text=text.split('\n').map(l=>({spaceAfter:opts.code?0:5,runs:opts.color?[{run:l,textStyle:{color:opts.color}}]:opts.code&&l.startsWith('#')?[{run:l,textStyle:{color:C.muted}}]:rich(l)}));return t;
}
function para(s,arr,x,y,width,size=28,gap=19){let top=y;arr.forEach((t,i)=>{const line=t.split('\n').reduce((a,l)=>a+Math.max(1,Math.ceil([...l].reduce((b,c)=>b+(/[\x00-\x7F]/.test(c)?0.54:1),0)/(width/size))),0);let h=line*size*1.35+10;tx(s,'Body '+i,t,x,top,width,h,size);top+=h+gap;});}
const master=p.masters.add('Temporary body');const layout=p.layouts.add('Temporary body layout');layout.setParentLayoutId(master.id);
for(let i=0;i<ds.length;i++){
 const d=ds[i],s=p.slides.add();s.setLayout(layout);s.background.fill='#FFFFFF';
 tx(s,'Title',d.title,64,42,1152,70,42,{bold:true});
 tx(s,'Stage',d.section+' · '+(Number(d.section.slice(2))<5?'① 工程与依赖':Number(d.section.slice(2))<8?'② 工作区与设置':Number(d.section.slice(2))<10?'③ 应用与 Build':'④ 产物与日常操作'),64,126,1152,34,22,{color:C.purple});
 if(i===0)continue;
 if(d.table){
  const count=d.table.length;const heights=d.title==='设置显示名称与 JSON 键对应'?84:count===7?57:count===6?68:count===5?78:90;
  const table=s.tables.add({rows:count,columns:3,left:64,top:184,width:1152,height:heights*count,columnWidths:[310,421,421],values:d.table});
  for(let r=0;r<count;r++){table.rows[r].height=heights;for(let c=0;c<3;c++){let cell=table.getCell(r,c);cell.fill=r===0?'#EEE8F6':r%2?'#FFFFFF':'#F8F6FB';cell.text.style={typeface:'Microsoft YaHei',fontSize:r===0?26:25,color:C.text,bold:r===0,autoFit:'none',wrap:true,verticalAlignment:'middle',insets:{left:12,right:10,top:9,bottom:8},lineSpacing:1.2};cell.value=d.table[r][c].split('\n').map(l=>({runs:rich(l),spaceAfter:0}));}}
  para(s,d.body,64,d.title==='可下载仓库、可用模块、受支持板子'?594:184+heights*count+20,1152,26,12);
 }else if(d.image){
  const raw=await fs.readFile(topic+'/assets/'+d.image);
  s.images.add({blob:new Uint8Array(raw),contentType:'image/jpeg',position:{left:64,top:187,width:775,height:386},fit:'contain',alt:d.caption});
  para(s,d.body,880,194,334,27,25);
  tx(s,'Image caption',d.caption,64,583,1152,37,19,{color:C.muted});
 }else if(d.diagram){
  const gap=27,bw=(1152-gap*(d.diagram.length-1))/d.diagram.length;
  d.diagram.forEach((v,j)=>{const x=64+j*(bw+gap);const n=s.shapes.add({name:'Flow '+j,geometry:'rect',position:{left:x,top:184,width:bw,height:100},fill:'#F5F2FA',line:{fill:C.purple,width:1.4}});n.text=v;n.text.style={typeface:'Microsoft YaHei',fontSize:25,color:C.text,alignment:'center',verticalAlignment:'middle',autoFit:'none',wrap:true,insets:{left:10,right:10,top:8,bottom:8},lineSpacing:1.2};if(j<d.diagram.length-1)s.shapes.add({name:'Flow connector '+j,geometry:'rightArrow',position:{left:x+bw+5,top:227,width:17,height:14},fill:C.purple,line:{fill:'none',width:0}});});
  para(s,d.body,64,323,1152,28,18);
 }else if(d.code){
  const size=d.code.split('\n').length>8?25:26;const effective=d.code.split('\n').reduce((a,l)=>a+Math.max(1,Math.ceil([...l].reduce((b,c)=>b+(/[\x00-\x7F]/.test(c)?0.61:1),0)*size/1152)),0);const ch=effective*size*1.48+14;
  tx(s,'Continuous code',d.code,64,183,1152,ch,size,{code:true});para(s,d.body,64,183+ch+25,1152,27,17);
 }else para(s,d.body,64,186,1152,30,25);
 tx(s,'Reading link','完整操作与来源：同名 Markdown '+d.section,64,637,1152,27,17,{color:'#347D95'});
 s.speakerNotes.textFrame.setText('对应同名 Markdown '+d.section+'。本章依据 Mylonics IDE for Zephyr 4.1.1。'+d.body.join('\n'));
}
await (await PresentationFile.exportPptx(p)).save(w+'/authored.pptx');
console.log('Exported '+ds.length+' slides');
