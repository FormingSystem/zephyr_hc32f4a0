---
id: learning.zephyr-docs.serialization.page-8
title: JSON头文件源码
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/json_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_JSON头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/json_8h_source.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 8.1\_阅读说明

译注：完整保留官方 Doxygen 源码浏览页展示的代码，只移除展示行号、还原不换行空格并清除行尾空白。网页本身省略了部分文档注释，原行号存在跳跃；这里不是另行下载的完整原始头文件。宏、声明、实现及版权／许可注释保持原样，接口说明见[完整API译文](P006_JSON接口参考.md)。

## 8.2\_源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00027"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00087"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00102"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="foldopen00180"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="foldopen00216"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00852"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00869"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="foldopen00917"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="foldopen00961"></a>
<a id="l00961"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="foldopen00987"></a>
<a id="l00987"></a>
<a id="l00988"></a>
<a id="l00989"></a>
<a id="l00990"></a>
<a id="l00991"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="l00997"></a>
<a id="foldopen01019"></a>
<a id="l01019"></a>
<a id="l01020"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="foldopen01045"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01054"></a>
<a id="l01055"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01073"></a>
<a id="l01074"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="l01093"></a>
<a id="l01094"></a>
<a id="l01109"></a>
<a id="l01110"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01125"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01135"></a>
<a id="agroup__json_html_ga18a137ac5e2998d375540298670797c4"></a>
<a id="agroup__json_html_ga20efb9b01733fadd8086dcab8be2ca85"></a>
<a id="agroup__json_html_ga210433173e35241dea8976bd7f532570"></a>
<a id="agroup__json_html_ga41e6e90beef8bae12fca1de2584145bb"></a>
<a id="agroup__json_html_ga4348a45b1a45a271e3d62a0c5a4d9c0d"></a>
<a id="agroup__json_html_ga43ee6d1fbd3fa8fb2ae052844b465dda"></a>
<a id="agroup__json_html_ga4ffccdc602ab98d489499bf6fa4fa6c5"></a>
<a id="agroup__json_html_ga51565a7e00a520d1257a0b6a91058a3d"></a>
<a id="agroup__json_html_ga5ef155a3a6444801592badd6a092734c"></a>
<a id="agroup__json_html_ga6196411958e2e9b3683af4c281214b92"></a>
<a id="agroup__json_html_ga64859a835e7cb88c2499360fb00ca344"></a>
<a id="agroup__json_html_ga73997fa2154fcbc80f37edd7bcf3477a"></a>
<a id="agroup__json_html_ga9e3a815cae48a9825ff9904b97618ecb"></a>
<a id="agroup__json_html_gab4e6ad4a040c271d74eaa313c580a739"></a>
<a id="agroup__json_html_gab758ad32cfb6369f4967a6842ac63245"></a>
<a id="agroup__json_html_gacb409ebe9c59789a5d9aca02c6c94674"></a>
<a id="agroup__json_html_gad612b8441a21dca34cfeec6257877509"></a>
<a id="agroup__json_html_gaeef63343b8b15edc3ee96028332bfb39"></a>
<a id="agroup__json_html_gafd27bbcb898dc902cf1dadd3369cf923"></a>
<a id="agroup__json_html_gafec772f687a0280f5211139bd019e582"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a1434ca9f19f4a411ea98e02d8a2cac7f"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a15a20a35f875a495a7514ae1a7027e75"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a2483f21d814abcd08b5253e55aef70c9"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a37f98b21d196182fd2b8cd4c71ed607e"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a6218cd0d5d8a34cf4b32797f361b5a41"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a651dd91f092a66f0e718a637e0178401"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a6e273425323ac63abad33f757572219b"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a7f49f406c8204e6d53353e26213d5169"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a835bc516b25eb0619b3f1a52f1ebc911"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a926d6b0a5458be2e707d51f0b25dbe77"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4aa5cf82525a71c8a9ca8c69c1adb0ff62"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4af1e451cb321c805cff8fcde3561d3e64"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructjson__lexer_html"></a>
<a id="astructjson__lexer_html_a9b403c5505e9a2cd9e475416b2e7f0ac"></a>
<a id="astructjson__lexer_html_aa4d4a29301fb840c691bbfa416474de4"></a>
<a id="astructjson__lexer_html_ab285bc72bf12a4de31b45ac0fc992620"></a>
<a id="astructjson__lexer_html_aeaf5743a9285e0aef9df99f9b3b48320"></a>
<a id="astructjson__mixed__arr__descr_html"></a>
<a id="astructjson__mixed__arr__descr_html_a0565129088b2a039a370db2779f327a8"></a>
<a id="astructjson__mixed__arr__descr_html_a3756bc3113f91e5acece578d37ad5409"></a>
<a id="astructjson__mixed__arr__descr_html_a3fa2bb6fa60dda662c11d273f6c26504"></a>
<a id="astructjson__mixed__arr__descr_html_a5e0c419152731f1de5525448d1348b67"></a>
<a id="astructjson__mixed__arr__descr_html_a7d758504ef6b87a60468b1bf8e0aca41"></a>
<a id="astructjson__mixed__arr__descr_html_a7f3ae3b8861e2ff2ad2c3d1e9b625f94"></a>
<a id="astructjson__mixed__arr__descr_html_a87454dd52ecb62d2751b3705436a9603"></a>
<a id="astructjson__mixed__arr__descr_html_a98f997d9e3ef4c1b4869b3be4a140875"></a>
<a id="astructjson__mixed__arr__descr_html_ac8407e2ae891402cc17811f5230a43bb"></a>
<a id="astructjson__mixed__arr__descr_html_addaf657a20864a1a5040390720a084d7"></a>
<a id="astructjson__mixed__arr__descr_html_adde1179c855ca7e658389e6dcd5923a1"></a>
<a id="astructjson__mixed__arr__descr_html_af27f330563f6bdf30f7c0a50992a9112"></a>
<a id="astructjson__obj__descr_html"></a>
<a id="astructjson__obj__descr_html_a0449d269cff7813f37066f0381b9e8f5"></a>
<a id="astructjson__obj__descr_html_a0a459bf5ad8a210395fe80c5edd72d93"></a>
<a id="astructjson__obj__descr_html_a2120b7752253ece0beddcaf4c57d3ed8"></a>
<a id="astructjson__obj__descr_html_a475717ac4dd01296c01468450e50f75b"></a>
<a id="astructjson__obj__descr_html_a4f5e97c654d0c5e21f1efb5a01966e56"></a>
<a id="astructjson__obj__descr_html_a5d5df7aab020feb3eeb59a7f6089b066"></a>
<a id="astructjson__obj__descr_html_a602bf4d8bb5d47c8edb40963ea8ba42f"></a>
<a id="astructjson__obj__descr_html_a8c6f3eae5e678b8b8ef1957c46f488f1"></a>
<a id="astructjson__obj__descr_html_a975e998d3ec36f234f09aa2d0d116c9c"></a>
<a id="astructjson__obj__descr_html_aa01763bb5316fdce6acc64c7d7d21406"></a>
<a id="astructjson__obj__descr_html_ac12783b89f5507bef7fa3da2c56d1d61"></a>
<a id="astructjson__obj__descr_html_ace6558c5156a76658d8835fd5e65ee52"></a>
<a id="astructjson__obj__descr_html_adea0b44d1552305df9dce70074044ba1"></a>
<a id="astructjson__obj__key__value_html"></a>
<a id="astructjson__obj__key__value_html_a2f6ebba58df4fbeef182257031362179"></a>
<a id="astructjson__obj__key__value_html_a30594e48462592aa03b967b38bce0097"></a>
<a id="astructjson__obj__key__value_html_aa902a4609788956586cdb29969c4d490"></a>
<a id="astructjson__obj__token_html"></a>
<a id="astructjson__obj__token_html_ac996ab0b850803998a37025b57051144"></a>
<a id="astructjson__obj__token_html_aef14abe1f0cefda6bd89d058787550b1"></a>
<a id="astructjson__obj_html"></a>
<a id="astructjson__obj_html_a7a48a2dca53ee74e7c8eb4727af0e33a"></a>
<a id="astructjson__token_html"></a>
<a id="astructjson__token_html_a606e33f699c3ec5a66f450cc1777b3c2"></a>
<a id="astructjson__token_html_ab163615cc3a39191d5a48e900c579e94"></a>
<a id="astructjson__token_html_abb55042d9343358e85311ea52cacb963"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DATA_JSON_H_
#define ZEPHYR_INCLUDE_DATA_JSON_H_

#include <zephyr/sys/util.h>
#include <stddef.h>
#include <zephyr/toolchain.h>
#include <zephyr/types.h>
#include <sys/types.h>

#ifdef __cplusplus
extern "C" {
#endif


enum json_tokens {
        /* Before changing this enum, ensure that its maximum
         * value is still within 7 bits. See comment next to the
         * declaration of `type` in struct json_obj_descr.
         */

        JSON_TOK_NONE = '_',
        JSON_TOK_OBJECT_START = '{',
        JSON_TOK_OBJECT_END = '}',
        JSON_TOK_ARRAY_START = '[',
        JSON_TOK_ARRAY_END = ']',
        JSON_TOK_STRING = '"',
        JSON_TOK_STRING_BUF = 's',
        JSON_TOK_COLON = ':',
        JSON_TOK_COMMA = ',',
        JSON_TOK_NUMBER = '0',
        JSON_TOK_FLOAT = '1',
        JSON_TOK_OPAQUE = '2',
        JSON_TOK_OBJ_ARRAY = '3',
        JSON_TOK_ENCODED_OBJ = '4',
        JSON_TOK_INT64 = '5',
        JSON_TOK_UINT64 = '6',
        JSON_TOK_FLOAT_FP = '7',
        JSON_TOK_DOUBLE_FP = '8',
        JSON_TOK_INT = 'i',
        JSON_TOK_UINT = 'u',
        JSON_TOK_TRUE = 't',
        JSON_TOK_FALSE = 'f',
        JSON_TOK_MIXED_ARRAY = 'm',
        JSON_TOK_NULL = 'n',
        JSON_TOK_ERROR = '!',
        JSON_TOK_EOF = '\0',
};

struct json_token {
        enum json_tokens type;
        char *start;
        char *end;
};

struct json_lexer {
        void *(*state)(struct json_lexer *lex);
        char *start;
        char *pos;
        char *end;
        struct json_token tok;
};

struct json_obj {
        struct json_lexer lex;
};

struct json_obj_key_value {
        const char *key;
        size_t key_len;
        struct json_token value;
};

struct json_obj_token {
        char *start;
        size_t length;
};


struct json_obj_descr {
        const char *field_name;

        /* Alignment can be 1, 2, 4, or 8.  The macros to create
         * a struct json_obj_descr will store the alignment's
         * power of 2 in order to keep this value in the 0-3 range
         * and thus use only 2 bits.
         */
        uint32_t align_shift : 2;

        /* 127 characters is more than enough for a field name. */
        uint32_t field_name_len : 7;

        /* Valid values here (enum json_tokens): JSON_TOK_STRING,
         * JSON_TOK_NUMBER, JSON_TOK_TRUE, JSON_TOK_FALSE,
         * JSON_TOK_OBJECT_START, JSON_TOK_ARRAY_START.  (All others
         * ignored.) Maximum value is '}' (125), so this has to be 7 bits
         * long.
         */
        uint32_t type : 7;

        /* 65535 bytes is more than enough for many JSON payloads. */
        uint32_t offset : 16;

        union {
                struct {
                        const struct json_obj_descr *sub_descr;
                        size_t sub_descr_len;
                } object;
                struct {
                        const struct json_obj_descr *element_descr;
                        size_t n_elements;
                } array;
                struct {
                        size_t size;
                } field;
        };
};

typedef int (*json_append_bytes_t)(const char *bytes, size_t len,
                                   void *data);

#define Z_ALIGN_SHIFT(type)     (__alignof__(type) == 1 ? 0 : \
                                 __alignof__(type) == 2 ? 1 : \
                                 __alignof__(type) == 4 ? 2 : 3)

#define JSON_OBJ_DESCR_PRIM(struct_, field_name_, type_) \
        { \
                .field_name = (#field_name_), \
                .align_shift = Z_ALIGN_SHIFT(struct_), \
                .field_name_len = sizeof(#field_name_) - 1, \
                .type = type_, \
                .offset = offsetof(struct_, field_name_), \
                .field = { \
                        .size = SIZEOF_FIELD(struct_, field_name_) \
                }, \
        }

#define JSON_OBJ_DESCR_OBJECT(struct_, field_name_, sub_descr_) \
        { \
                .field_name = (#field_name_), \
                .align_shift = Z_ALIGN_SHIFT(struct_), \
                .field_name_len = (sizeof(#field_name_) - 1), \
                .type = JSON_TOK_OBJECT_START, \
                .offset = offsetof(struct_, field_name_), \
                .object = { \
                        .sub_descr = sub_descr_, \
                        .sub_descr_len = ARRAY_SIZE(sub_descr_), \
                }, \
        }

#define Z_JSON_ELEMENT_DESCR(struct_, len_field_, elem_type_, union_) \
        (const struct json_obj_descr[]) \
        { \
                { \
                        .align_shift = Z_ALIGN_SHIFT(struct_), \
                        .type = elem_type_, \
                        .offset = offsetof(struct_, len_field_), \
                        union_ \
                } \
        }

#define Z_JSON_DESCR_ARRAY(elem_descr_, elem_descr_len_) \
        { \
                .array = { \
                        .element_descr = elem_descr_, \
                        .n_elements = elem_descr_len_, \
                }, \
        }

#define Z_JSON_DESCR_OBJ(elem_descr_, elem_descr_len_) \
                .object = { \
                        .sub_descr = elem_descr_, \
                        .sub_descr_len = elem_descr_len_, \
                }, \

#define Z_JSON_DESCR_FIELD(struct_, field_name_) \
        { \
                .field = { \
                        .size = SIZEOF_FIELD(struct_, field_name_), \
                }, \
        }

#define JSON_OBJ_DESCR_ARRAY(struct_, field_name_, max_len_, \
                             len_field_, elem_type_) \
        { \
                .field_name = (#field_name_), \
                .align_shift = Z_ALIGN_SHIFT(struct_), \
                .field_name_len = sizeof(#field_name_) - 1, \
                .type = JSON_TOK_ARRAY_START, \
                .offset = offsetof(struct_, field_name_), \
                .array = { \
                        .element_descr = Z_JSON_ELEMENT_DESCR(struct_, len_field_, \
                                elem_type_, \
                                Z_JSON_DESCR_FIELD(struct_, field_name_[0])), \
                        .n_elements = (max_len_), \
                }, \
        }

#define JSON_OBJ_DESCR_OBJ_ARRAY(struct_, field_name_, max_len_, \
                                 len_field_, elem_descr_, elem_descr_len_) \
        { \
                .field_name = (#field_name_), \
                .align_shift = Z_ALIGN_SHIFT(struct_), \
                .field_name_len = sizeof(#field_name_) - 1, \
                .type = JSON_TOK_ARRAY_START, \
                .offset = offsetof(struct_, field_name_), \
                .array = { \
                        .element_descr = Z_JSON_ELEMENT_DESCR(struct_, len_field_, \
                                JSON_TOK_OBJECT_START, \
                                Z_JSON_DESCR_OBJ(elem_descr_, elem_descr_len_)), \
                        .n_elements = (max_len_), \
                }, \
        }

#define JSON_OBJ_DESCR_ARRAY_ARRAY(struct_, field_name_, max_len_, len_field_, \
                                   elem_descr_, elem_descr_len_) \
        { \
                .field_name = (#field_name_), \
                .align_shift = Z_ALIGN_SHIFT(struct_), \
                .field_name_len = sizeof(#field_name_) - 1, \
                .type = JSON_TOK_ARRAY_START, \
                .offset = offsetof(struct_, field_name_), \
                .array = { \
                        .element_descr = Z_JSON_ELEMENT_DESCR( \
                                struct_, len_field_, JSON_TOK_ARRAY_START, \
                                Z_JSON_DESCR_ARRAY( \
                                        elem_descr_, \
                                        1 + ZERO_OR_COMPILE_ERROR(elem_descr_len_ == 1))), \
                        .n_elements = (max_len_), \
                }, \
        }

#define JSON_OBJ_DESCR_ARRAY_ARRAY_NAMED(struct_, json_field_name_, struct_field_name_, \
                                         max_len_, len_field_, elem_descr_, elem_descr_len_) \
        { \
                .field_name = (#json_field_name_), \
                .align_shift = Z_ALIGN_SHIFT(struct_), \
                .field_name_len = sizeof(#json_field_name_) - 1, \
                .type = JSON_TOK_ARRAY_START, \
                .offset = offsetof(struct_, struct_field_name_), \
                .array = { \
                        .element_descr = Z_JSON_ELEMENT_DESCR( \
                                struct_, len_field_, JSON_TOK_ARRAY_START, \
                                Z_JSON_DESCR_ARRAY( \
                                        elem_descr_, \
                                        1 + ZERO_OR_COMPILE_ERROR(elem_descr_len_ == 1))), \
                        .n_elements = (max_len_), \
                }, \
        }

#define JSON_OBJ_DESCR_PRIM_NAMED(struct_, json_field_name_, \
                                  struct_field_name_, type_) \
        { \
                .field_name = (json_field_name_), \
                .align_shift = Z_ALIGN_SHIFT(struct_), \
                .field_name_len = sizeof(json_field_name_) - 1, \
                .type = type_, \
                .offset = offsetof(struct_, struct_field_name_), \
                .field = { \
                        .size = SIZEOF_FIELD(struct_, struct_field_name_) \
                }, \
        }

#define JSON_OBJ_DESCR_OBJECT_NAMED(struct_, json_field_name_, \
                                    struct_field_name_, sub_descr_) \
        { \
                .field_name = (json_field_name_), \
                .align_shift = Z_ALIGN_SHIFT(struct_), \
                .field_name_len = (sizeof(json_field_name_) - 1), \
                .type = JSON_TOK_OBJECT_START, \
                .offset = offsetof(struct_, struct_field_name_), \
                .object = { \
                        .sub_descr = sub_descr_, \
                        .sub_descr_len = ARRAY_SIZE(sub_descr_), \
                }, \
        }

#define JSON_OBJ_DESCR_ARRAY_NAMED(struct_, json_field_name_,\
                                   struct_field_name_, max_len_, len_field_, \
                                   elem_type_) \
        { \
                .field_name = (json_field_name_), \
                .align_shift = Z_ALIGN_SHIFT(struct_), \
                .field_name_len = sizeof(json_field_name_) - 1, \
                .type = JSON_TOK_ARRAY_START, \
                .offset = offsetof(struct_, struct_field_name_), \
                .array = { \
                        .element_descr = Z_JSON_ELEMENT_DESCR(struct_, len_field_, \
                                elem_type_, \
                                Z_JSON_DESCR_FIELD(struct_, struct_field_name_[0])), \
                        .n_elements = (max_len_), \
                }, \
        }

#define JSON_OBJ_DESCR_OBJ_ARRAY_NAMED(struct_, json_field_name_, \
                                       struct_field_name_, max_len_, \
                                       len_field_, elem_descr_, \
                                       elem_descr_len_) \
        { \
                .field_name = json_field_name_, \
                .align_shift = Z_ALIGN_SHIFT(struct_), \
                .field_name_len = sizeof(json_field_name_) - 1, \
                .type = JSON_TOK_ARRAY_START, \
                .offset = offsetof(struct_, struct_field_name_), \
                .array = { \
                        .element_descr = Z_JSON_ELEMENT_DESCR(struct_, len_field_, \
                                JSON_TOK_OBJECT_START, \
                                Z_JSON_DESCR_OBJ(elem_descr_, elem_descr_len_)), \
                        .n_elements = (max_len_), \
                }, \
        }

int64_t json_obj_parse(char *json, size_t len,
        const struct json_obj_descr *descr, size_t descr_len,
        void *val);

int json_arr_parse(char *json, size_t len,
        const struct json_obj_descr *descr, void *val);

int json_arr_separate_object_parse_init(struct json_obj *json, char *payload, size_t len);

int json_arr_separate_parse_object(struct json_obj *json, const struct json_obj_descr *descr,
                                   size_t descr_len, void *val);

int json_obj_separate_parse_init(struct json_obj *json, char *payload, size_t len);

int json_obj_next_key_value(struct json_obj *json, struct json_obj_key_value *kv);

ssize_t json_escape(char *str, size_t *len, size_t buf_size);

size_t json_calc_escaped_len(const char *str, size_t len);

ssize_t json_calc_encoded_len(const struct json_obj_descr *descr,
                              size_t descr_len, const void *val);

ssize_t json_calc_encoded_arr_len(const struct json_obj_descr *descr,
                                  const void *val);

int json_obj_encode_buf(const struct json_obj_descr *descr, size_t descr_len,
                        const void *val, char *buffer, size_t buf_size);

int json_arr_encode_buf(const struct json_obj_descr *descr, const void *val,
                        char *buffer, size_t buf_size);

int json_obj_encode(const struct json_obj_descr *descr, size_t descr_len,
                    const void *val, json_append_bytes_t append_bytes,
                    void *data);

int json_arr_encode(const struct json_obj_descr *descr, const void *val,
                    json_append_bytes_t append_bytes, void *data);

struct json_mixed_arr_descr {
        uint32_t type : 7;
        size_t count_offset;

        union {
                struct {
                        size_t offset;
                        size_t size;
                } primitive;

                struct {
                        const struct json_obj_descr *sub_descr;
                        size_t sub_descr_len;
                        size_t offset;
                } object;

                struct {
                        const struct json_obj_descr *element_descr;
                        size_t n_elements;
                        size_t offset;
                } array;

                struct {
                        const struct json_mixed_arr_descr *sub_descr;
                        size_t sub_descr_len;
                        size_t offset;
                } mixed_array;
        };
};

#define JSON_MIXED_ARR_DESCR_PRIM(struct_, field_name_, type_, count_field_) \
{ \
        .type = type_, \
        .count_offset = offsetof(struct_, count_field_), \
        .primitive = { \
            .offset = offsetof(struct_, field_name_), \
            .size = SIZEOF_FIELD(struct_, field_name_) \
        } \
}

#define JSON_MIXED_ARR_DESCR_OBJECT(struct_, field_name_, sub_descr_, count_field_) \
{ \
        .type = JSON_TOK_OBJECT_START, \
        .count_offset = offsetof(struct_, count_field_), \
        .object = { \
                .sub_descr = sub_descr_, \
                .sub_descr_len = ARRAY_SIZE(sub_descr_), \
                .offset = offsetof(struct_, field_name_) \
        } \
}

#define JSON_MIXED_ARR_DESCR_ARRAY(struct_, field_name_, max_len_, elem_descr_, count_field_) \
{ \
        .type = JSON_TOK_ARRAY_START, \
        .count_offset = offsetof(struct_, count_field_), \
        .array = { \
                .element_descr = elem_descr_, \
                .n_elements = (max_len_), \
                .offset = offsetof(struct_, field_name_) \
        } \
}

#define JSON_MIXED_ARR_DESCR_MIXED_ARRAY(struct_, field_name_, sub_descr_, count_field_) \
{ \
        .type = JSON_TOK_MIXED_ARRAY, \
        .count_offset = offsetof(struct_, count_field_), \
        .mixed_array = { \
                .sub_descr = sub_descr_, \
                .sub_descr_len = ARRAY_SIZE(sub_descr_), \
                .offset = offsetof(struct_, field_name_) \
        } \
}

int json_mixed_arr_parse(char *json, size_t len,
                         const struct json_mixed_arr_descr *descr,
                         size_t descr_len, void *val);

int json_mixed_arr_encode(const struct json_mixed_arr_descr *descr,
                          size_t descr_len, void *val,
                          json_append_bytes_t append_bytes,
                          void *data);

int json_mixed_arr_encode_buf(const struct json_mixed_arr_descr *descr,
                              size_t descr_len, void *val,
                              char *buffer, size_t buf_size);

ssize_t json_calc_mixed_arr_len(const struct json_mixed_arr_descr *descr,
                                size_t descr_len, void *val);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DATA_JSON_H_ */
```

## 8.3\_源码注释译文

版权归 2017 年 Intel Corporation 所有，SPDX 许可标识为 Apache-2.0。原法律声明完整保留。其余普通注释依次说明：

- 修改词元枚举前，应确保最大值仍能放入 7 位；参见 json_obj_descr 中 type 声明旁的注释。
- 对齐量可以为 1、2、4 或 8；创建描述符的宏保存相应的以 2 为底的指数，使数值落在 0～3，只占 2 位。
- 127 个字符对字段名来说已经足够。
- type 的原注释列出 JSON_TOK_STRING、JSON_TOK_NUMBER、JSON_TOK_TRUE、JSON_TOK_FALSE、JSON_TOK_OBJECT_START、JSON_TOK_ARRAY_START，其余忽略；最大值为字符 `}`，即 125，所以需要 7 位。
- 65535 字节对许多 JSON 载荷已经足够。
- 最后一处注释标记头文件包含保护（Header Include Guard）ZEPHYR_INCLUDE_DATA_JSON_H_。

> 译注：type 注释中的类型列表是原文内容，当前枚举与实现还包含其他类型；不要据此把这个历史注释当作当前全部可用类型的清单。

## 8.4\_源码对照与相关阅读

译注：可从本仓库的[JSON头文件](../../../include/zephyr/data/json.h)与[JSON实现](../../../lib/utils/json.c)继续跟踪，位置按本文相对路径解析。本地源码不自动等同于网页 latest 的版本；上述纠错另核对了本次读取的[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/json.c)，摘要见[来源记录](../SOURCES.md)。

[JSON入门](P002_JSON序列化.md) · [接口参考](P006_JSON接口参考.md) · [头文件](P007_JSON头文件.md) · [源码浏览](P008_JSON头文件源码.md)。

[上一章](P007_JSON头文件.md) · [返回大纲](大纲.md) · [下一章](P009_JSON对象描述符.md)
