// SPDX-License-Identifier: Apache-2.0
// Initial authoring source. Preserve later PowerPoint edits using build.py sync.
import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire(path.join(process.env.RUNTIME_NODE_MODULES, '__artifact_entry__.cjs'));
const { Presentation, PresentationFile } = require('@oai/artifact-tool');
const topic = path.resolve(process.env.TOPIC_DIR);
const build = path.resolve(process.env.TMP_DIR);
const content = JSON.parse(await fs.readFile(path.join(topic,'slides/content.json'),'utf8'));
const ppt = Presentation.create({slideSize:{width:1280,height:720}});
const C={text:'#29263B',gray:'#646173',path:'#0070C0',variable:'#B84E00',func:'#087B3D',cmd:'#A02B93',purple:'#7350BC'};
const sources={
 local:'本章 Markdown；本机 Zephyr 4.5.0-rc1 与 IDE for Zephyr 4.1.1',
 getting:'https://docs.zephyrproject.org/latest/develop/getting_started/index.html',
 external:'https://zephyr-ide.mylonics.com/getting-started/external-environments/',
 configuration:'https://zephyr-ide.mylonics.com/reference/configuration/',
 implementation:'本机 mylonics.zephyr-ide-4.1.1/package.json 与 dist/extension.js；configure-existing-environment、Ps、Ts、cl 等实现定位见同名 MD 1.15',
 readme:'https://github.com/mylonics/zephyr-ide；图片：https://raw.githubusercontent.com/mylonics/zephyr-ide/develop/docs/media/main_build.png',
 project:'https://zephyr-ide.mylonics.com/user-guide/project-setup/；本机扩展资源 schema 与 Build 向导',
 application:'https://docs.zephyrproject.org/latest/develop/application/index.html；G:/zephyr_practice/zephyr-main/samples/hello_world/CMakeLists.txt',
 build:'https://docs.zephyrproject.org/latest/develop/west/build-flash-debug.html；scripts/west_commands/build.py',
 cpp:'https://code.visualstudio.com/docs/cpp/customize-cpp-settings#_compilecommands',
 workspace:'https://zephyr-ide.mylonics.com/getting-started/workspace-configuration/；图片：https://raw.githubusercontent.com/mylonics/zephyr-ide/develop/docs/media/workspace_setup.png',
 references:'同名 Markdown 1.15：官方文档与当前安装包实现定位'
};
function rich(str,code=false){
 const rx=/(G:\/[^\s，。；、）：<>"]+|(?:\$\{workspaceFolder\}\/|\.\.\/|\/g\/|build\/|samples\/|include\/|apps\/|\.vscode\/|zephyr\/|commands\/|src\/)[^\s，。；、）：<>"]+|(?:\.venv|\.west|modules|zephyr-main|zephyr-sdk-1\.0\.1)\/[^\s，。；、）：<>"]*|(?:CMakeLists\.txt|CMakeCache\.txt|settings\.json|zephyr-ide\.json|compile_commands\.json|prj\.conf|west\.yml|helper\.c)|(?:relPath|toolchains|venvFolder|toolchainDirectory|zephyr-ide\.[\w.]+|C_Cpp\.[\w.]+|cmake\.configureOnOpen|ZEPHYR_[A-Z_]+|CMAKE_[A-Z_]+|-D[A-Z_]+=\w+)|(?:find_package|target_sources|project|cmake_minimum_required)(?=\()|\b(?:west|python|source|export|code|cd|cmake|ninja|cat)\b)/g;
 let cursor=0,runs=[];
 for(const m of str.matchAll(rx)){
   if(m.index>cursor) runs.push({run:str.slice(cursor,m.index)});
   let t=m[0],color=C.text;
   if(/^(?:G:|\$\{|\.\.\/|\/g\/|build\/|samples\/|include\/|apps\/|\.vscode\/|zephyr\/|commands\/|src\/|\.venv\/|\.west\/|modules\/|zephyr-main\/|zephyr-sdk-1\.0\.1\/)/.test(t)||/\.(txt|json|conf|yml|c)$/.test(t)) color=C.path;
   else if(/^(?:relPath|toolchains|venvFolder|toolchainDirectory|zephyr-ide\.|C_Cpp\.|cmake\.|ZEPHYR_|CMAKE_|-D)/.test(t)) color=C.variable;
   else if(/^(find_package|target_sources|project|cmake_minimum_required)$/.test(t)) color=C.func;
   else if(code && !/[├└│]/.test(str)) color=C.cmd;
   runs.push({run:t,textStyle:{color}});cursor=m.index+t.length;
 }
 if(cursor<str.length) runs.push({run:str.slice(cursor)});
 return runs.length?runs:[{run:str}];
}
function text(slide,name,value,x,y,w,h,size=28,color=C.text,opts={}){
 const s=slide.shapes.add({geometry:'textbox',name,position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 s.text.style={typeface:opts.code?'Consolas':'Microsoft YaHei',fontSize:size,color,bold:opts.bold||false,autoFit:'none',verticalAlignment:'top',wrap:opts.code?'none':'square',insets:{left:0,right:0,top:0,bottom:0},...opts.style};
 s.text=Array.isArray(value)?value:String(value).split('\n').map(l=>({runs:rich(l,opts.code),spaceAfter:0}));
 return s;
}
function paragraphs(s,items,x,y,w,size=30,gap=26){
 let top=y;
 for(let i=0;i<items.length;i++){
   const item=items[i].replace(/。$/,'');
   const lines=item.split('\n').reduce((sum,line)=>sum+Math.max(1,Math.ceil(Array.from(line).reduce((a,c)=>a+(/[\x00-\x7F]/.test(c)?0.55:1),0)/(w/size))),0);
   const h=lines*size*1.28+8;
   text(s,`Body ${i+1}`,item,x,top,w,h,size);top+=h+gap;
 }
}
function diagram(s,labels,y){
 const gap=34,w=(1152-gap*(labels.length-1))/labels.length;
 labels.forEach((l,i)=>{
   const x=64+i*(w+gap);
   const n=s.shapes.add({geometry:'rect',name:`Diagram node ${i+1}`,position:{left:x,top:y,width:w,height:112},fill:'#F5F2FA',line:{fill:'#7350BC',width:1.5}});
   n.text=l;n.text.style={typeface:'Microsoft YaHei',fontSize:25,color:C.text,alignment:'center',verticalAlignment:'middle',autoFit:'none',insets:{left:8,right:8,top:6,bottom:6}};
   if(i<labels.length-1) s.shapes.add({geometry:'rightArrow',name:`Dependency ${i+1}`,position:{left:x+w+7,top:y+49,width:20,height:14},fill:C.purple,line:{fill:'none',width:0}});
 });
}
const coverMaster=ppt.masters.add('Zephyr cover');
const coverLayout=ppt.layouts.add('Zephyr cover layout');coverLayout.setParentLayoutId(coverMaster.id);
const bodyMaster=ppt.masters.add('Zephyr body');
const bodyLayout=ppt.layouts.add('Zephyr body layout');bodyLayout.setParentLayoutId(bodyMaster.id);
for(let index=0;index<content.length;index++){
 const d=content[index],s=ppt.slides.add();s.setLayout(index===0?coverLayout:bodyLayout);s.background.fill=index===0?'#161127':'#FFFFFF';
 if(index===0){
   s.images.add({blob:new Uint8Array(await fs.readFile(path.join(topic,'assets/series-cover.png'))),contentType:'image/png',position:{left:0,top:0,width:1280,height:720},fit:'cover',alt:'既有 Zephyr 技术教程系列芯片封面背景'});
   text(s,'Title',d.title,64,209,725,182,58,'#FFFFFF',{bold:true});
   text(s,'Chapter','P001',68,95,550,45,25,'#C3B4E2');
   text(s,'Subtitle','Windows · 已有环境接入教程',68,445,700,55,31,'#C3B4E2');
   text(s,'Presenter lizhaojun',d.body[1],68,533,700,55,29,'#C3B4E2');
 }else{
   text(s,'Title',d.title,64,45,1152,66,42,C.text,{bold:true});
   text(s,'Stage',d.stage,64,124,1152,36,23,C.purple);
   if(d.image){
     s.images.add({blob:new Uint8Array(await fs.readFile(path.join(topic,'assets',d.image))),contentType:'image/png',position:{left:64,top:180,width:780,height:440},fit:'contain',alt:'官方文档界面示意，非本机操作截图'});
     paragraphs(s,d.side,880,192,335,27,22);
   }else if(d.diagram){
     diagram(s,d.diagram,190);paragraphs(s,d.body,64,356,1152,30,23);
   }else if(d.code){
     const lines=d.code.split('\n').length;
     const size=d.codeSize||25;
     const height=lines*size*1.48+14;
     text(s,'Code',d.code,64,185,d.side?755:(d.codeSize===23?1170:1152),height,size,C.text,{code:true});
     if(d.side) paragraphs(s,d.side,840,187,375,25,24);
     else paragraphs(s,d.body,64,185+height+24,1152,28,19);
   }else paragraphs(s,d.body,64,188,1152,31,27);
   const foot=text(s,'Reading link',[{runs:[{run:'详细步骤与完整命令：配套 MD '+d.section,textStyle:{color:'#347D95',underline:'sng'},link:{uri:'../'+encodeURIComponent('x'),isExternal:true}}]}],64,639,1152,26,17,C.gray);
   // The final XML patch replaces this placeholder URI with the exact sibling document.
 }
 s.speakerNotes.textFrame.setText(`对应 Markdown ${d.section}。${(d.body||d.side||[]).join('\n')}\n依据：${sources[d.source]||sources.local}\n本机插件版本 4.1.1。官方界面图片为文档示意，工程名按正文选择。`);
}
await fs.mkdir(build,{recursive:true});
await (await PresentationFile.exportPptx(ppt)).save(path.join(build,'draft.pptx'));
console.log(`Exported ${content.length} slides`);
