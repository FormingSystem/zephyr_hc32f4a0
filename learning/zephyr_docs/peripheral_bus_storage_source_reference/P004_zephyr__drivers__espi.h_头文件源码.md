---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-4
title: zephyr__drivers__espi.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/espi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr__drivers__espi.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/espi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P004_zephyr__drivers__espi.h_头文件参考.md)。

## 4.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00036"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00098"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00121"></a>
<a id="l00121"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="foldopen00159"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
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
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="foldopen00206"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="foldopen00235"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="foldopen00262"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="foldopen00268"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="foldopen00303"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
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
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00363"></a>
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="foldopen00378"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00415"></a>
<a id="l00420"></a>
<a id="l00425"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="foldopen00445"></a>
<a id="l00445"></a>
<a id="l00447"></a>
<a id="l00449"></a>
<a id="l00451"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="foldopen00462"></a>
<a id="l00462"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00472"></a>
<a id="l00474"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="foldopen00484"></a>
<a id="l00484"></a>
<a id="l00486"></a>
<a id="l00488"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="foldopen00499"></a>
<a id="l00499"></a>
<a id="l00501"></a>
<a id="l00507"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="foldopen00521"></a>
<a id="l00521"></a>
<a id="l00523"></a>
<a id="l00525"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="foldopen00536"></a>
<a id="l00536"></a>
<a id="l00538"></a>
<a id="l00540"></a>
<a id="l00542"></a>
<a id="l00544"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="foldopen00558"></a>
<a id="l00558"></a>
<a id="l00560"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="foldopen00571"></a>
<a id="l00571"></a>
<a id="l00573"></a>
<a id="l00575"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00610"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00625"></a>
<a id="l00630"></a>
<a id="l00635"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="foldopen00738"></a>
<a id="l00738"></a>
<a id="l00740"></a>
<a id="l00742"></a>
<a id="l00744"></a>
<a id="l00746"></a>
<a id="l00748"></a>
<a id="l00750"></a>
<a id="l00752"></a>
<a id="l00754"></a>
<a id="l00756"></a>
<a id="l00758"></a>
<a id="l00760"></a>
<a id="l00762"></a>
<a id="l00764"></a>
<a id="l00766"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00772"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00846"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00869"></a>
<a id="l00870"></a>
<a id="l00871"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
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
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00960"></a>
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
<a id="l00971"></a>
<a id="l00972"></a>
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
<a id="l00998"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="l01014"></a>
<a id="l01015"></a>
<a id="l01016"></a>
<a id="l01017"></a>
<a id="l01018"></a>
<a id="l01019"></a>
<a id="l01020"></a>
<a id="l01021"></a>
<a id="l01033"></a>
<a id="l01034"></a>
<a id="l01035"></a>
<a id="l01036"></a>
<a id="l01037"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="l01040"></a>
<a id="l01041"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01059"></a>
<a id="l01060"></a>
<a id="l01061"></a>
<a id="l01062"></a>
<a id="l01063"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01066"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01073"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01089"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="l01093"></a>
<a id="l01094"></a>
<a id="l01095"></a>
<a id="l01096"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01101"></a>
<a id="l01115"></a>
<a id="l01116"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01119"></a>
<a id="l01120"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01146"></a>
<a id="l01147"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01150"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="l01153"></a>
<a id="l01154"></a>
<a id="l01155"></a>
<a id="l01156"></a>
<a id="l01157"></a>
<a id="l01220"></a>
<a id="foldopen01229"></a>
<a id="l01229"></a>
<a id="l01230"></a>
<a id="l01231"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="l01234"></a>
<a id="l01235"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="l01238"></a>
<a id="l01239"></a>
<a id="foldopen01252"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01258"></a>
<a id="l01259"></a>
<a id="l01260"></a>
<a id="l01261"></a>
<a id="l01262"></a>
<a id="l01263"></a>
<a id="foldopen01280"></a>
<a id="l01280"></a>
<a id="l01281"></a>
<a id="l01282"></a>
<a id="l01283"></a>
<a id="l01284"></a>
<a id="l01285"></a>
<a id="l01286"></a>
<a id="l01287"></a>
<a id="l01288"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="l01291"></a>
<a id="foldopen01346"></a>
<a id="l01346"></a>
<a id="l01347"></a>
<a id="l01348"></a>
<a id="l01349"></a>
<a id="l01350"></a>
<a id="l01351"></a>
<a id="l01352"></a>
<a id="l01353"></a>
<a id="l01354"></a>
<a id="l01355"></a>
<a id="l01356"></a>
<a id="l01357"></a>
<a id="l01358"></a>
<a id="l01359"></a>
<a id="l01360"></a>
<a id="l01364"></a>
<a id="l01365"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__espi__interface__backend_html_ga04547d61ee4ed5d34fca3fb11ec0370f"></a>
<a id="agroup__espi__interface__backend_html_ga1a8715b387a037dddacc92424fe0ba6f"></a>
<a id="agroup__espi__interface__backend_html_ga3c3e6a70a04c14ec50fa0dcef4055f73"></a>
<a id="agroup__espi__interface__backend_html_ga422abe38a4d2cce441d5165192adc982"></a>
<a id="agroup__espi__interface__backend_html_ga4712365e3a38d859fefbf0e9a6f32b07"></a>
<a id="agroup__espi__interface__backend_html_ga47ea19517406b64f074b4eee7a9d1923"></a>
<a id="agroup__espi__interface__backend_html_ga6bb1bb8af96c58dc0d9ad041d95cd397"></a>
<a id="agroup__espi__interface__backend_html_ga79255a516e48256d8381d0b32e5ae345"></a>
<a id="agroup__espi__interface__backend_html_ga7d497e1f4573f54f49202b67cb5cbe5c"></a>
<a id="agroup__espi__interface__backend_html_ga806a0b3f3f4e629c5556f1399c4e29e2"></a>
<a id="agroup__espi__interface__backend_html_ga838aefb5fbe399f6492803ceb391fa8c"></a>
<a id="agroup__espi__interface__backend_html_ga97336083a3ed3f561301fcf5762dc73c"></a>
<a id="agroup__espi__interface__backend_html_gab0313b00d884426800395ec5a907f744"></a>
<a id="agroup__espi__interface__backend_html_gac7e3730c214b877772b24c4055ab997a"></a>
<a id="agroup__espi__interface__backend_html_gae7497b9629a9444f94dae125fdf46005"></a>
<a id="agroup__espi__interface_html_ga0a97d11167367342283bfe6b6d66726e"></a>
<a id="agroup__espi__interface_html_ga0d7c61f1f4ec611d0c8a67ba73e2b4f0"></a>
<a id="agroup__espi__interface_html_ga112f7554ba614c8e5f239b1319b4a763"></a>
<a id="agroup__espi__interface_html_ga143ed88b1f220f9582c809165fd983fd"></a>
<a id="agroup__espi__interface_html_ga1cd0afc52d533414b5bbc684cef8b9af"></a>
<a id="agroup__espi__interface_html_ga2557cfc7a38f669d14e9826e3fb0fdee"></a>
<a id="agroup__espi__interface_html_ga2629a5518a94f031419eeccd05f07373"></a>
<a id="agroup__espi__interface_html_ga36ac3fbf9813f78bad90f047e1eb1128"></a>
<a id="agroup__espi__interface_html_ga3e52615f244d7fa8ccda495ab8ec8a5b"></a>
<a id="agroup__espi__interface_html_ga4b8f4fbf66a2b2ae394e00b16500f70d"></a>
<a id="agroup__espi__interface_html_ga4e35c754c720f262805689a94985272c"></a>
<a id="agroup__espi__interface_html_ga7227c53d384eb0dc666361261f069f68"></a>
<a id="agroup__espi__interface_html_ga7f04f98ea6a4671b821cf6ddf6bbf2a6"></a>
<a id="agroup__espi__interface_html_ga869551e20fc2c3be4311c21c3c53999d"></a>
<a id="agroup__espi__interface_html_ga880b6b04824f9f0deea10e8018573b88"></a>
<a id="agroup__espi__interface_html_ga8d88e4e3893d610713195e5352ec2565"></a>
<a id="agroup__espi__interface_html_ga9d848c7e367cf277230f365f73c15c46"></a>
<a id="agroup__espi__interface_html_gaa8bb48b5592c4b49d27c9b8a42432410"></a>
<a id="agroup__espi__interface_html_gab02d46fd690e33875cc1b2433c976891"></a>
<a id="agroup__espi__interface_html_gab42be7c76c4523cea96365aa77fd18be"></a>
<a id="agroup__espi__interface_html_gab65a0951a8912d9de398cfec0aef7d35"></a>
<a id="agroup__espi__interface_html_gabf5f0ea01ec8ed5345b2e119181c2313"></a>
<a id="agroup__espi__interface_html_gac55098842dd9d181144ac4b4122a610e"></a>
<a id="agroup__espi__interface_html_gacab2b3bff7d940e71ee1c2a9fdedf782"></a>
<a id="agroup__espi__interface_html_gad00b6a22843e5df9c6d6945d0d82310e"></a>
<a id="agroup__espi__interface_html_gaeaae20afa90d9d825d80997369f31465"></a>
<a id="agroup__espi__interface_html_gafaa3f7d54503c901ab23bd79a7f8a755"></a>
<a id="agroup__espi__interface_html_gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a87e70bb0f5c4f6a3a21ca1bcfa4540fc"></a>
<a id="agroup__espi__interface_html_gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a9f47188ebd9bb4cb6e426d0bc0b6595c"></a>
<a id="agroup__espi__interface_html_gga0d7c61f1f4ec611d0c8a67ba73e2b4f0af766582d28d16af7c5aff6372e4ee243"></a>
<a id="agroup__espi__interface_html_gga2629a5518a94f031419eeccd05f07373a0e6e9dc1a7975cd80991090a78ea6231"></a>
<a id="agroup__espi__interface_html_gga2629a5518a94f031419eeccd05f07373a24478711945fd5258d8ca86bbb79b867"></a>
<a id="agroup__espi__interface_html_gga2629a5518a94f031419eeccd05f07373a8948a6f18bfbe87859a529d5f6e669b8"></a>
<a id="agroup__espi__interface_html_gga2629a5518a94f031419eeccd05f07373a8d8c64c49e8c7a75cb3a665e63a6f5ce"></a>
<a id="agroup__espi__interface_html_gga2629a5518a94f031419eeccd05f07373aa217b4786d7b8bacbaa4ec740550e71e"></a>
<a id="agroup__espi__interface_html_gga2629a5518a94f031419eeccd05f07373aaea75bb5ab8a5ff31dd6b8787f44df30"></a>
<a id="agroup__espi__interface_html_gga2629a5518a94f031419eeccd05f07373ace2e4ef0298e7c67a82dbfcab43769ad"></a>
<a id="agroup__espi__interface_html_gga2629a5518a94f031419eeccd05f07373af51b7171cf6085fa7946333ff32fe2f0"></a>
<a id="agroup__espi__interface_html_gga36ac3fbf9813f78bad90f047e1eb1128a3b5e529d1d0ba11c59172ab01c30e203"></a>
<a id="agroup__espi__interface_html_gga36ac3fbf9813f78bad90f047e1eb1128a996aee0a8f8ba0cead11cea0d39d2973"></a>
<a id="agroup__espi__interface_html_gga36ac3fbf9813f78bad90f047e1eb1128a9ac837699f302bd10332814c7014adea"></a>
<a id="agroup__espi__interface_html_gga36ac3fbf9813f78bad90f047e1eb1128a9f2a9cfda3b803687a0992a9d41f0014"></a>
<a id="agroup__espi__interface_html_gga36ac3fbf9813f78bad90f047e1eb1128aa09f7dcd4b2d3addfaddbad5b8f2e5a2"></a>
<a id="agroup__espi__interface_html_gga36ac3fbf9813f78bad90f047e1eb1128ae6d4d43eded0d8a368c90ea653a60956"></a>
<a id="agroup__espi__interface_html_gga3e52615f244d7fa8ccda495ab8ec8a5ba0335f2d34fab46960939e2d2c1c12e3f"></a>
<a id="agroup__espi__interface_html_gga3e52615f244d7fa8ccda495ab8ec8a5ba0edb306e5fabcbf8b009375cde6a8a2b"></a>
<a id="agroup__espi__interface_html_gga3e52615f244d7fa8ccda495ab8ec8a5ba2e5a736cf8a63491ee13d51ae4f8f073"></a>
<a id="agroup__espi__interface_html_gga3e52615f244d7fa8ccda495ab8ec8a5ba380e3d4e6b5579c8bb94e792fcb7d71f"></a>
<a id="agroup__espi__interface_html_gga3e52615f244d7fa8ccda495ab8ec8a5ba54c11e63fcfe3f859af57e65af3f31f7"></a>
<a id="agroup__espi__interface_html_gga3e52615f244d7fa8ccda495ab8ec8a5ba5b480e093a58849d4181bba22d5868a5"></a>
<a id="agroup__espi__interface_html_gga3e52615f244d7fa8ccda495ab8ec8a5ba5f2ae0575ca4e9b61c0acd7d4f08ee82"></a>
<a id="agroup__espi__interface_html_gga3e52615f244d7fa8ccda495ab8ec8a5bac8ec7673b4466b278dfb5e468f7a4d79"></a>
<a id="agroup__espi__interface_html_gga3e52615f244d7fa8ccda495ab8ec8a5baf3dbc2bcc0ed883bc4d4160c21e6934f"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca07591a29b44dea00b0218680644c180b"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca0d877c057f5f32c02e55e89afc0a562b"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca21fadb75fbf1f2131e6b44b318a955a5"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca2f59f8c02560181d98b2d3b29de8f800"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca3040bdf3cbb3888f3972202091fc5592"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca4b760583473994661ef490a64201b2ac"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272ca6be11dd62eb439a30d95013f2b3ebcee"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272cab402f4c4e5ebe41bd4e7927ab24806dd"></a>
<a id="agroup__espi__interface_html_gga4e35c754c720f262805689a94985272cafb7c66ad4601fcd17e4a1c040491c1a3"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a07a6b00a4b1cfad2137dc43d7232fc9f"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a0bafcd0bb7f592f0e308dcfce39bcd08"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a0e13f250ba0c5a37451c7f3b0e98e663"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a19c40230e0bb4cee7b6ee42580c28a8d"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a1d54a71c6d2e52cb66cfaa0b55b61152"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a231caf3d46cde2eaf7305bf3f694838c"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a2d9b2eef499d1bfd13bec1d2caa0e2f3"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a2f3f97b51b750050cd98e887e39431d1"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a3d95f095ae41bba9ef916fc68ddd4779"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a4ef1fe12bd09be0875864d6c32164f73"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a504ae332b89262f70a0bf1a9c8b6f527"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a58280c68c980476aabefa16e0509dd1c"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a637b5c00aaca05e5daa6969a680cbbb1"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a736724f8229aebc356c2720a34a0143f"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a89420628ae26df4c45ef7fba04a3a85e"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a8a7b50f0aa53a2c80bae7747d628d219"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a8e15df6f8159b4c275dc4b20aaec352e"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a923f3e602d9f8ac821ece2a625183146"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a9410475f349afcf44ddb25ebbd454978"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35a9e32eee077aaa1668c356fe1d4ab1cc5"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35aa4c8c69475b48d88302066823d2f3592"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35aa87af5b5de184238e5f371851aaee692"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35aae0a3fd882c5765db33a4e7bd05e1ab1"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35ab4f0bedd5717660cc8cac2d85c6c3d18"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35ab880a7156e489d5f7b8f78550e72b166"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35ab9deb0dd6d4e878eff6413ddc34bb36c"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35aba8b891a643ca567966d091963be4615"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35abe28432b566619d8c6cce5e5034e5333"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35ac4b4e30c097a4ef49f21549a799e1e13"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35ad14b4b7a25141346bfefc507c588a238"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35ad3319083735295454bc59b742988cfca"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35ad99ea62f91b40c8926cda944928e3631"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35ad9b6bb998bea0bc983ab8a6c452d52a1"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35ae34962d6db346e02f175894843ce0e1e"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35aee0a1576a6e07708e1cde59597b49662"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35af10e9e5b320301b2fe923e6793adbeaf"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35af44250de6f60eabf9b0d85b8860ac56e"></a>
<a id="agroup__espi__interface_html_ggab65a0951a8912d9de398cfec0aef7d35afa1f99a7e45b306c6736888e280f527c"></a>
<a id="agroup__espi__interface_html_ggac55098842dd9d181144ac4b4122a610ea0e245cbeef479218d4e6c9bec57e40d1"></a>
<a id="agroup__espi__interface_html_ggac55098842dd9d181144ac4b4122a610ea68ecb52b04ffddcc93fbcc77d3643687"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea02bf8538a66f633e3d2ec094f57c6173"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea02c7b1c69d803a5c45304260786afb6f"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea09f241a3f6ffcb5b7839c81c7fc4ea6e"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea113a85c90924922dde04f3b5bf64046b"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea3cce8bd0205691ecda53fc469606929d"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea464db427cfd432b44874495ed7503db8"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea530fb2a8690538e9659d6eb2c234fb91"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea5c592b1cad381b296cde832c67264cd1"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea5e7205b5f1371f1a0f2eaed299389475"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea689643f6feb724a303d3b790ff2899f7"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea83266d88740588d45be6667a4034c447"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310ea8c62cd1266681c88aa0cb1af65ab551b"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310eaa9135a5ea9a5ebd9d25660c37983c5d6"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310eaaef0649f867424ec0c7889acb7354911"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310eab70684413d736c8583f3dc53f14b7c7a"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310eac172afb38cb38970ef6242a4f45132f9"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310eac5b666b3319dc2ef0fc571684c2ea198"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310eacdeb74a9534310f5dab3f1bfb5def534"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310eae1e018f0ecde965905752204e557ba40"></a>
<a id="agroup__espi__interface_html_ggad00b6a22843e5df9c6d6945d0d82310eaf97f7d0d3562dba07b826101bb805243"></a>
<a id="agroup__espi__interface_html_ggafaa3f7d54503c901ab23bd79a7f8a755a0ccb80544cbda501cc90ea0c3b868e54"></a>
<a id="agroup__espi__interface_html_ggafaa3f7d54503c901ab23bd79a7f8a755a32f636bbad2618a6b1554656d3b53206"></a>
<a id="agroup__espi__interface_html_ggafaa3f7d54503c901ab23bd79a7f8a755a5616bf2bf49a8c457fcc2f27d9fe0518"></a>
<a id="agroup__espi__interface_html_ggafaa3f7d54503c901ab23bd79a7f8a755ac2e84a127870ff50359cf96528c9a7c6"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="asignal_8h_html_a5d326f119f87d0facaa662520f8c322a"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructespi__cfg_html"></a>
<a id="astructespi__cfg_html_a75175c60a31c3a88c83772b99c2a5c34"></a>
<a id="astructespi__cfg_html_abb24c88ecc977d8116973d44a7e7cb94"></a>
<a id="astructespi__cfg_html_aed88dd6fc8028a7c281260e7fa29ce21"></a>
<a id="astructespi__driver__api_html"></a>
<a id="astructespi__driver__api_html_a049bff890414ce43f2323238a6ee3d15"></a>
<a id="astructespi__driver__api_html_a2241bb06a85d6220417cee282e359021"></a>
<a id="astructespi__driver__api_html_a2ae357ec0cf8f4ee548f50350bd4eaa4"></a>
<a id="astructespi__driver__api_html_a47041efc4fb0879b2812bb53533b8ab8"></a>
<a id="astructespi__driver__api_html_a53b561bfa5dbc53dbf8cbb6af88c1b36"></a>
<a id="astructespi__driver__api_html_a5c1be83cf9f3eac140b8ab7b37a86c1b"></a>
<a id="astructespi__driver__api_html_a5ff3310cd5db4a08c42284cc4ea48057"></a>
<a id="astructespi__driver__api_html_a74218772f99c24af2fe9ae5b1749039e"></a>
<a id="astructespi__driver__api_html_a96ad30567d449161c7c30f86b9500808"></a>
<a id="astructespi__driver__api_html_abfd2310657421141737af0f8316825ef"></a>
<a id="astructespi__driver__api_html_ac27072d18c70f4b415467d01a37a2f75"></a>
<a id="astructespi__driver__api_html_ac9033b4b59e0c99747e367ed283ab116"></a>
<a id="astructespi__driver__api_html_adfcdf83461d94819c788dac869b09096"></a>
<a id="astructespi__driver__api_html_ae7f3be0766c35a75d611735f09e6b728"></a>
<a id="astructespi__driver__api_html_aea877fee89f0d346b009c053a3c0a09d"></a>
<a id="astructespi__event_html"></a>
<a id="astructespi__event_html_aa0491cbed5bec091721dfa14898b7277"></a>
<a id="astructespi__event_html_acac75eb1d2b384aa337a5240825b635f"></a>
<a id="astructespi__event_html_aea36925bd3f599c1481c9cc867795c33"></a>
<a id="astructespi__evt__data__acpi_html"></a>
<a id="astructespi__evt__data__acpi_html_a8fb3633a97b1af7618b391539f576c6f"></a>
<a id="astructespi__evt__data__acpi_html_aa5d1e0b548e9be6b65daf67316df8bfe"></a>
<a id="astructespi__evt__data__acpi_html_acb291c371bb201d0ceb739fca7e22d3b"></a>
<a id="astructespi__evt__data__kbc_html"></a>
<a id="astructespi__evt__data__kbc_html_a0c17b320752b11dc04926df2965807b2"></a>
<a id="astructespi__evt__data__kbc_html_a55e94583f10481a2cdc34ad7ba388f2f"></a>
<a id="astructespi__evt__data__kbc_html_a5f56bd66943cc82825bb1725bf8a2966"></a>
<a id="astructespi__evt__data__kbc_html_a75294f9d88f6dfad7bb56e5af5613c64"></a>
<a id="astructespi__evt__data__pvt_html"></a>
<a id="astructespi__evt__data__pvt_html_a67a1ac452110cfdb0c9c5e0f453c5c57"></a>
<a id="astructespi__evt__data__pvt_html_adf7edc5acdfb9affde2d1ff1d18cf23d"></a>
<a id="astructespi__evt__data__pvt_html_aff82e44d2a95e985d1a672169f55e4df"></a>
<a id="astructespi__flash__packet_html"></a>
<a id="astructespi__flash__packet_html_a22244bc4063618707eea571f170bdfde"></a>
<a id="astructespi__flash__packet_html_ac638c0b5d0d98e15ab66850afc394cec"></a>
<a id="astructespi__flash__packet_html_adade51336ae37a519c06b12bf19fc86d"></a>
<a id="astructespi__oob__packet_html"></a>
<a id="astructespi__oob__packet_html_a0b19890b5e63ecbd1b95eef57fd9263f"></a>
<a id="astructespi__oob__packet_html_adf45a10c88a171df8e7138929958b346"></a>
<a id="astructespi__request__packet_html"></a>
<a id="astructespi__request__packet_html_a22a0111e338827125eaf79ce8516b744"></a>
<a id="astructespi__request__packet_html_a4ac2d50786fdc4c4bd8da88bde28f77d"></a>
<a id="astructespi__request__packet_html_a6f808763faf949ff7ef83d68fb71e7ba"></a>
<a id="astructespi__request__packet_html_a9b474155dfa0c74d0bd55e4b831b383a"></a>
<a id="astructespi__request__packet_html_ae8b7dc12b04f469b5689ad27cc4f0643"></a>

```c
/*
 * Copyright (c) 2019 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_ESPI_H_
#define ZEPHYR_INCLUDE_ESPI_H_

#include <errno.h>

#include <zephyr/sys/__assert.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif


enum espi_io_mode {
        ESPI_IO_MODE_SINGLE_LINE = BIT(0),
        ESPI_IO_MODE_DUAL_LINES = BIT(1),
        ESPI_IO_MODE_QUAD_LINES = BIT(2),
};


enum espi_channel {
        ESPI_CHANNEL_PERIPHERAL = BIT(0),
        ESPI_CHANNEL_VWIRE      = BIT(1),
        ESPI_CHANNEL_OOB        = BIT(2),
        ESPI_CHANNEL_FLASH      = BIT(3),
};

enum espi_bus_event {
        ESPI_BUS_RESET                      = BIT(0),

        ESPI_BUS_EVENT_CHANNEL_READY        = BIT(1),

        ESPI_BUS_EVENT_VWIRE_RECEIVED       = BIT(2),

        ESPI_BUS_EVENT_OOB_RECEIVED         = BIT(3),

        ESPI_BUS_PERIPHERAL_NOTIFICATION    = BIT(4),
        ESPI_BUS_TAF_NOTIFICATION           = BIT(5),
};

enum espi_pc_event {
        ESPI_PC_EVT_BUS_CHANNEL_READY = BIT(0),
        ESPI_PC_EVT_BUS_MASTER_ENABLE = BIT(1),
};

#define ESPI_PERIPHERAL_INDEX_0  0ul
#define ESPI_PERIPHERAL_INDEX_1  1ul
#define ESPI_PERIPHERAL_INDEX_2  2ul

/* eSPI specification defines eSPI target and eSPI controller terms
 * note that sometimes eSPI controller is also referred as eSPI host
 */

#define ESPI_TARGET_TO_CONTROLLER   0ul
#define ESPI_CONTROLLER_TO_TARGET   1ul

#define ESPI_VWIRE_SRC_ID0       0ul
#define ESPI_VWIRE_SRC_ID1       1ul
#define ESPI_VWIRE_SRC_ID2       2ul
#define ESPI_VWIRE_SRC_ID3       3ul
#define ESPI_VWIRE_SRC_ID_MAX    4ul

#define ESPI_PERIPHERAL_NODATA   0ul

#define E8042_START_OPCODE      0x50
#define E8042_MAX_OPCODE        0x5F

#define EACPI_START_OPCODE      0x60
#define EACPI_MAX_OPCODE        0x6F

#define ECUSTOM_START_OPCODE    0xF0
#define ECUSTOM_MAX_OPCODE      0xFF


enum espi_virtual_peripheral {
        ESPI_PERIPHERAL_UART,
        ESPI_PERIPHERAL_8042_KBC,
        ESPI_PERIPHERAL_HOST_IO,
        ESPI_PERIPHERAL_DEBUG_PORT80,
        ESPI_PERIPHERAL_HOST_IO_PVT,
        ESPI_PERIPHERAL_HOST_IO_PVT2,
        ESPI_PERIPHERAL_HOST_IO_PVT3,
#if defined(CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD) || defined(__DOXYGEN__)
        ESPI_PERIPHERAL_EC_HOST_CMD,
#endif /* CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD */
};

enum espi_interrupt_flags {
        ESPI_BUS_EVENTS = BIT(0),
        ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS = BIT(1),
        ESPI_OOB_CHANNEL_EVENTS = BIT(2),
        ESPI_FLASH_CHANNEL_EVENTS = BIT(3),

        ESPI_PERIPHERAL_UART_EVENTS = BIT(4),
        ESPI_PERIPHERAL_DEBUG_PORT80_EVENTS = BIT(5),
        ESPI_PERIPHERAL_8042_KBC_EVENTS = BIT(6),
        ESPI_PERIPHERAL_HOST_IO_EVENTS = BIT(7),
        ESPI_PERIPHERAL_SHARED_MEMORY_EVENTS = BIT(8),
};

#define ESPI_INT_ALL_MASK  (ESPI_BUS_EVENTS | ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS | \
                        ESPI_OOB_CHANNEL_EVENTS | ESPI_FLASH_CHANNEL_EVENTS | \
                        ESPI_PERIPHERAL_DEBUG_PORT80_EVENTS | ESPI_PERIPHERAL_8042_KBC_EVENTS | \
                        ESPI_PERIPHERAL_HOST_IO_EVENTS | ESPI_PERIPHERAL_SHARED_MEMORY_EVENTS)

#define ESPI_INT_BUS_ONLY_MASK (ESPI_BUS_EVENTS | ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS | \
                        ESPI_OOB_CHANNEL_EVENTS | ESPI_FLASH_CHANNEL_EVENTS)

#define ESPI_INT_NONE_MASK      0U


enum espi_cycle_type {
        ESPI_CYCLE_MEMORY_READ32,
        ESPI_CYCLE_MEMORY_READ64,
        ESPI_CYCLE_MEMORY_WRITE32,
        ESPI_CYCLE_MEMORY_WRITE64,
        ESPI_CYCLE_MESSAGE_NODATA,
        ESPI_CYCLE_MESSAGE_DATA,
        ESPI_CYCLE_OK_COMPLETION_NODATA,
        ESPI_CYCLE_OKCOMPLETION_DATA,
        ESPI_CYCLE_NOK_COMPLETION_NODATA,
};

enum espi_vwire_signal {
        /* Virtual wires that can only be send from controller to target */
        ESPI_VWIRE_SIGNAL_SLP_S3,
        ESPI_VWIRE_SIGNAL_SLP_S4,
        ESPI_VWIRE_SIGNAL_SLP_S5,
        ESPI_VWIRE_SIGNAL_OOB_RST_WARN,
        ESPI_VWIRE_SIGNAL_PLTRST,
        ESPI_VWIRE_SIGNAL_SUS_STAT,
        ESPI_VWIRE_SIGNAL_NMIOUT,
        ESPI_VWIRE_SIGNAL_SMIOUT,
        ESPI_VWIRE_SIGNAL_HOST_RST_WARN,
        ESPI_VWIRE_SIGNAL_SLP_A,
        ESPI_VWIRE_SIGNAL_SUS_PWRDN_ACK,
        ESPI_VWIRE_SIGNAL_SUS_WARN,
        ESPI_VWIRE_SIGNAL_SLP_WLAN,
        ESPI_VWIRE_SIGNAL_SLP_LAN,
        ESPI_VWIRE_SIGNAL_HOST_C10,
        ESPI_VWIRE_SIGNAL_DNX_WARN,

        /* Virtual wires that can only be sent from target to controller */
        ESPI_VWIRE_SIGNAL_PME,
        ESPI_VWIRE_SIGNAL_WAKE,
        ESPI_VWIRE_SIGNAL_OOB_RST_ACK,
        ESPI_VWIRE_SIGNAL_TARGET_BOOT_STS,
        ESPI_VWIRE_SIGNAL_ERR_NON_FATAL,
        ESPI_VWIRE_SIGNAL_ERR_FATAL,
        ESPI_VWIRE_SIGNAL_TARGET_BOOT_DONE,
        ESPI_VWIRE_SIGNAL_HOST_RST_ACK,
        ESPI_VWIRE_SIGNAL_RST_CPU_INIT,
        ESPI_VWIRE_SIGNAL_SMI,
        ESPI_VWIRE_SIGNAL_SCI,
        ESPI_VWIRE_SIGNAL_DNX_ACK,
        ESPI_VWIRE_SIGNAL_SUS_ACK,

        /*
         * Virtual wire GPIOs that can be sent from target to controller for
         * platform specific usage.
         */
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_0,
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_1,
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_2,
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_3,
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_4,
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_5,
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_6,
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_7,
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_8,
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_9,
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_10,
        ESPI_VWIRE_SIGNAL_TARGET_GPIO_11,

        ESPI_VWIRE_SIGNAL_COUNT
};

#define ESPI_VWIRE_SIGNAL_OCB_0 ESPI_VWIRE_SIGNAL_TARGET_GPIO_0
#define ESPI_VWIRE_SIGNAL_OCB_1 ESPI_VWIRE_SIGNAL_TARGET_GPIO_1
#define ESPI_VWIRE_SIGNAL_OCB_2 ESPI_VWIRE_SIGNAL_TARGET_GPIO_2
#define ESPI_VWIRE_SIGNAL_OCB_3 ESPI_VWIRE_SIGNAL_TARGET_GPIO_3

enum lpc_peripheral_opcode {
        /* Read transactions */
        E8042_OBF_HAS_CHAR = 0x50,
        E8042_IBF_HAS_CHAR,
        /* Write transactions */
        E8042_WRITE_KB_CHAR,
        E8042_WRITE_MB_CHAR,
        /* Write transactions without input parameters */
        E8042_RESUME_IRQ,
        E8042_PAUSE_IRQ,
        E8042_CLEAR_OBF,
        /* Status transactions */
        E8042_READ_KB_STS,
        E8042_SET_FLAG,
        E8042_CLEAR_FLAG,
        /* ACPI read transactions */
        EACPI_OBF_HAS_CHAR = EACPI_START_OPCODE,
        EACPI_IBF_HAS_CHAR,
        /* ACPI write transactions */
        EACPI_WRITE_CHAR,
        /* ACPI status transactions */
        EACPI_READ_STS,
        EACPI_WRITE_STS,
#if defined(CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION) || defined(__DOXYGEN__)
        EACPI_GET_SHARED_MEMORY,
#endif /* CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION */
#if defined(CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE) || defined(__DOXYGEN__)
        /* Other customized transactions */
        ECUSTOM_HOST_SUBS_INTERRUPT_EN = ECUSTOM_START_OPCODE,
        ECUSTOM_HOST_CMD_GET_PARAM_MEMORY,
        ECUSTOM_HOST_CMD_GET_PARAM_MEMORY_SIZE,
        ECUSTOM_HOST_CMD_SEND_RESULT,
#endif /* CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE */
};

#define HOST_KBC_EVT_IBF BIT(0)
#define HOST_KBC_EVT_OBE BIT(1)

struct espi_evt_data_kbc {
        uint32_t type: 8;
        uint32_t data: 8;
        uint32_t evt: 8;
        uint32_t reserved: 8;
};

struct espi_evt_data_acpi {
        uint32_t type: 8;
        uint32_t data: 8;
        uint32_t reserved: 16;
};

#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_DATA    0
#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_TO_EC_CMD     1U
#define ESPI_EVENT_DATA_ACPI_TYPE_HOST_RD_EC_TO_HOST 2U

struct espi_evt_data_pvt {
        uint32_t type: 8;
        uint32_t data: 8;
        uint32_t reserved: 16;
};

struct espi_event {
        enum espi_bus_event evt_type;
        uint32_t evt_details;
        uint32_t evt_data;
};

struct espi_cfg {
        enum espi_io_mode io_caps;
        enum espi_channel channel_caps;
        uint8_t max_freq;
};

struct espi_request_packet {
        enum espi_cycle_type cycle_type;
        uint8_t tag;
        uint16_t len;
        uint32_t address;
        uint8_t *data;
};

struct espi_oob_packet {
        uint8_t *buf;
        uint16_t len;
};

struct espi_flash_packet {
        uint8_t *buf;
        uint32_t flash_addr;
        uint16_t len;
};

struct espi_callback;

typedef void (*espi_callback_handler_t) (const struct device *dev,
                                         struct espi_callback *cb,
                                         struct espi_event espi_evt);

struct espi_callback {
        sys_snode_t node;

        espi_callback_handler_t handler;

        enum espi_bus_event evt_type;
};


typedef int (*espi_api_config)(const struct device *dev, struct espi_cfg *cfg);
typedef bool (*espi_api_get_channel_status)(const struct device *dev,
                                            enum espi_channel ch);
/* Logical Channel 0 APIs */
typedef int (*espi_api_read_request)(const struct device *dev,
                                     struct espi_request_packet *req);
typedef int (*espi_api_write_request)(const struct device *dev,
                                      struct espi_request_packet *req);
typedef int (*espi_api_lpc_read_request)(const struct device *dev,
                                         enum lpc_peripheral_opcode op,
                                         uint32_t *data);
typedef int (*espi_api_lpc_write_request)(const struct device *dev,
                                          enum lpc_peripheral_opcode op,
                                          uint32_t *data);
/* Logical Channel 1 APIs */
typedef int (*espi_api_send_vwire)(const struct device *dev,
                                   enum espi_vwire_signal vw,
                                   uint8_t level);
typedef int (*espi_api_receive_vwire)(const struct device *dev,
                                      enum espi_vwire_signal vw,
                                      uint8_t *level);
/* Logical Channel 2 APIs */
typedef int (*espi_api_send_oob)(const struct device *dev,
                                 struct espi_oob_packet *pckt);
typedef int (*espi_api_receive_oob)(const struct device *dev,
                                    struct espi_oob_packet *pckt);
/* Logical Channel 3 APIs */
typedef int (*espi_api_flash_read)(const struct device *dev,
                                   struct espi_flash_packet *pckt);
typedef int (*espi_api_flash_write)(const struct device *dev,
                                    struct espi_flash_packet *pckt);
typedef int (*espi_api_flash_erase)(const struct device *dev,
                                    struct espi_flash_packet *pckt);

/* Callbacks and traffic intercept */
typedef int (*espi_api_manage_callback)(const struct device *dev,
                                        struct espi_callback *callback,
                                        bool set);

/* eSPI interrupt control */
typedef int (*espi_api_interrupt_configure)(const struct device *dev,
                                            uint32_t espi_interrupt_flags,
                                            uint32_t espi_interrupt_vendor);

__subsystem struct espi_driver_api {
        espi_api_config config;
        espi_api_get_channel_status get_channel_status;
        espi_api_read_request read_request;
        espi_api_write_request write_request;
        espi_api_lpc_read_request read_lpc_request;
        espi_api_lpc_write_request write_lpc_request;
        espi_api_send_vwire send_vwire;
        espi_api_receive_vwire receive_vwire;
        espi_api_send_oob send_oob;
        espi_api_receive_oob receive_oob;
        espi_api_flash_read flash_read;
        espi_api_flash_write flash_write;
        espi_api_flash_erase flash_erase;
        espi_api_manage_callback manage_callback;
        espi_api_interrupt_configure interrupt_config;
};


__syscall int espi_config(const struct device *dev, struct espi_cfg *cfg);

static inline int z_impl_espi_config(const struct device *dev,
                                     struct espi_cfg *cfg)
{
        return DEVICE_API_GET(espi, dev)->config(dev, cfg);
}

__syscall bool espi_get_channel_status(const struct device *dev,
                                       enum espi_channel ch);

static inline bool z_impl_espi_get_channel_status(const struct device *dev,
                                                  enum espi_channel ch)
{
        return DEVICE_API_GET(espi, dev)->get_channel_status(dev, ch);
}

__syscall int espi_read_request(const struct device *dev,
                                struct espi_request_packet *req);

static inline int z_impl_espi_read_request(const struct device *dev,
                                           struct espi_request_packet *req)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->read_request) {
                return -ENOTSUP;
        }

        return api->read_request(dev, req);
}

__syscall int espi_write_request(const struct device *dev,
                                 struct espi_request_packet *req);

static inline int z_impl_espi_write_request(const struct device *dev,
                                            struct espi_request_packet *req)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->write_request) {
                return -ENOTSUP;
        }

        return api->write_request(dev, req);
}

__syscall int espi_read_lpc_request(const struct device *dev,
                                    enum lpc_peripheral_opcode op,
                                    uint32_t *data);

static inline int z_impl_espi_read_lpc_request(const struct device *dev,
                                               enum lpc_peripheral_opcode op,
                                               uint32_t *data)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->read_lpc_request) {
                return -ENOTSUP;
        }

        return api->read_lpc_request(dev, op, data);
}

__syscall int espi_write_lpc_request(const struct device *dev,
                                     enum lpc_peripheral_opcode op,
                                     uint32_t *data);

static inline int z_impl_espi_write_lpc_request(const struct device *dev,
                                                enum lpc_peripheral_opcode op,
                                                uint32_t *data)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->write_lpc_request) {
                return -ENOTSUP;
        }

        return api->write_lpc_request(dev, op, data);
}

__syscall int espi_send_vwire(const struct device *dev,
                              enum espi_vwire_signal signal,
                              uint8_t level);

static inline int z_impl_espi_send_vwire(const struct device *dev,
                                         enum espi_vwire_signal signal,
                                         uint8_t level)
{
        return DEVICE_API_GET(espi, dev)->send_vwire(dev, signal, level);
}

__syscall int espi_receive_vwire(const struct device *dev,
                                 enum espi_vwire_signal signal,
                                 uint8_t *level);

static inline int z_impl_espi_receive_vwire(const struct device *dev,
                                            enum espi_vwire_signal signal,
                                            uint8_t *level)
{
        return DEVICE_API_GET(espi, dev)->receive_vwire(dev, signal, level);
}

__syscall int espi_send_oob(const struct device *dev,
                            struct espi_oob_packet *pckt);

static inline int z_impl_espi_send_oob(const struct device *dev,
                                       struct espi_oob_packet *pckt)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->send_oob) {
                return -ENOTSUP;
        }

        return api->send_oob(dev, pckt);
}

__syscall int espi_receive_oob(const struct device *dev,
                               struct espi_oob_packet *pckt);

static inline int z_impl_espi_receive_oob(const struct device *dev,
                                          struct espi_oob_packet *pckt)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->receive_oob) {
                return -ENOTSUP;
        }

        return api->receive_oob(dev, pckt);
}

__syscall int espi_read_flash(const struct device *dev,
                              struct espi_flash_packet *pckt);

static inline int z_impl_espi_read_flash(const struct device *dev,
                                         struct espi_flash_packet *pckt)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->flash_read) {
                return -ENOTSUP;
        }

        return api->flash_read(dev, pckt);
}

__syscall int espi_write_flash(const struct device *dev,
                               struct espi_flash_packet *pckt);

static inline int z_impl_espi_write_flash(const struct device *dev,
                                          struct espi_flash_packet *pckt)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->flash_write) {
                return -ENOTSUP;
        }

        return api->flash_write(dev, pckt);
}

__syscall int espi_flash_erase(const struct device *dev,
                               struct espi_flash_packet *pckt);

static inline int z_impl_espi_flash_erase(const struct device *dev,
                                          struct espi_flash_packet *pckt)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->flash_erase) {
                return -ENOTSUP;
        }

        return api->flash_erase(dev, pckt);
}


static inline void espi_init_callback(struct espi_callback *callback,
                                      espi_callback_handler_t handler,
                                      enum espi_bus_event evt_type)
{
        __ASSERT(callback, "Callback pointer should not be NULL");
        __ASSERT(handler, "Callback handler pointer should not be NULL");

        callback->handler = handler;
        callback->evt_type = evt_type;
}

static inline int espi_add_callback(const struct device *dev,
                                    struct espi_callback *callback)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->manage_callback) {
                return -ENOTSUP;
        }

        return api->manage_callback(dev, callback, true);
}

static inline int espi_remove_callback(const struct device *dev,
                                       struct espi_callback *callback)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->manage_callback) {
                return -ENOTSUP;
        }

        return api->manage_callback(dev, callback, false);
}

static inline int espi_interrupt_config(const struct device *dev, uint32_t espi_flags,
                                        uint32_t espi_vendor_flags)
{
        const struct espi_driver_api *api = DEVICE_API_GET(espi, dev);

        if (!api->interrupt_config) {
                return -ENOTSUP;
        }

        return api->interrupt_config(dev, espi_flags, espi_vendor_flags);
}
#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/espi.h>
#endif /* ZEPHYR_INCLUDE_ESPI_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 174 行

eSPI 规范定义了目标设备（Target）与控制器（Controller）这两个术语。注意：eSPI 控制器有时也称为 eSPI 主机（Host）。

### 注释 3：原第 227 行

条件编译配置（Configuration）标记：`CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD`。

### 注释 4：原第 304 行

只能从控制器发送给目标设备的虚拟线（Virtual wires）。

### 注释 5：原第 322 行

只能从目标设备发送给控制器的虚拟线。

### 注释 6：原第 337 行

可从目标设备发送给控制器、用于平台特定用途的虚拟线 GPIO。

### 注释 7：原第 379 行

读取事务（Read transactions）。

### 注释 8：原第 382 行

写入事务（Write transactions）。

### 注释 9：原第 385 行

不带输入参数的写入事务。

### 注释 10：原第 389 行

状态事务（Status transactions）。

### 注释 11：原第 393 行

ACPI 读取事务。

### 注释 12：原第 396 行

ACPI 写入事务。

### 注释 13：原第 398 行

ACPI 状态事务。

### 注释 14：原第 407 行

条件编译配置（Configuration）标记：`CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION`。

### 注释 15：原第 409 行

其他自定义事务（Customized transactions）。

### 注释 16：原第 431 行

条件编译配置（Configuration）标记：`CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE`。

### 注释 17：原第 642 行

逻辑通道（Logical Channel）0 的 API。

### 注释 18：原第 669 行

逻辑通道 1 的 API。

### 注释 19：原第 684 行

逻辑通道 2 的 API。

### 注释 20：原第 697 行

逻辑通道 3 的 API。

### 注释 21：原第 717 行

回调与流量拦截（Callbacks and traffic intercept）。

### 注释 22：原第 726 行

eSPI 中断控制。

### 注释 23：原第 1365 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ESPI_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P004_zephyr__drivers__espi.h_头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [espi_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0)
- [ESPI_IO_MODE_SINGLE_LINE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a9f47188ebd9bb4cb6e426d0bc0b6595c)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [ESPI_IO_MODE_DUAL_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0af766582d28d16af7c5aff6372e4ee243)
- [ESPI_IO_MODE_QUAD_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a87e70bb0f5c4f6a3a21ca1bcfa4540fc)
- [espi_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gafaa3f7d54503c901ab23bd79a7f8a755)
- [ESPI_CHANNEL_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755a32f636bbad2618a6b1554656d3b53206)
- [ESPI_CHANNEL_VWIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755ac2e84a127870ff50359cf96528c9a7c6)
- [ESPI_CHANNEL_OOB](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755a0ccb80544cbda501cc90ea0c3b868e54)
- [ESPI_CHANNEL_FLASH](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggafaa3f7d54503c901ab23bd79a7f8a755a5616bf2bf49a8c457fcc2f27d9fe0518)
- [espi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga36ac3fbf9813f78bad90f047e1eb1128)
- [ESPI_BUS_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128ae6d4d43eded0d8a368c90ea653a60956)
- [ESPI_BUS_EVENT_CHANNEL_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a996aee0a8f8ba0cead11cea0d39d2973)
- [ESPI_BUS_EVENT_VWIRE_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128aa09f7dcd4b2d3addfaddbad5b8f2e5a2)
- [ESPI_BUS_EVENT_OOB_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a3b5e529d1d0ba11c59172ab01c30e203)
- [ESPI_BUS_PERIPHERAL_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a9ac837699f302bd10332814c7014adea)
- [ESPI_BUS_TAF_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga36ac3fbf9813f78bad90f047e1eb1128a9f2a9cfda3b803687a0992a9d41f0014)
- [espi_pc_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gac55098842dd9d181144ac4b4122a610e)
- [ESPI_PC_EVT_BUS_CHANNEL_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggac55098842dd9d181144ac4b4122a610ea68ecb52b04ffddcc93fbcc77d3643687)
- [ESPI_PC_EVT_BUS_MASTER_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggac55098842dd9d181144ac4b4122a610ea0e245cbeef479218d4e6c9bec57e40d1)
- [espi_virtual_peripheral](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga2629a5518a94f031419eeccd05f07373)
- [ESPI_PERIPHERAL_UART](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a24478711945fd5258d8ca86bbb79b867)
- [ESPI_PERIPHERAL_8042_KBC](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373aaea75bb5ab8a5ff31dd6b8787f44df30)
- [ESPI_PERIPHERAL_HOST_IO](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a8948a6f18bfbe87859a529d5f6e669b8)
- [ESPI_PERIPHERAL_DEBUG_PORT80](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373af51b7171cf6085fa7946333ff32fe2f0)
- [ESPI_PERIPHERAL_HOST_IO_PVT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373aa217b4786d7b8bacbaa4ec740550e71e)
- [ESPI_PERIPHERAL_HOST_IO_PVT2](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a0e6e9dc1a7975cd80991090a78ea6231)
- [ESPI_PERIPHERAL_HOST_IO_PVT3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373a8d8c64c49e8c7a75cb3a665e63a6f5ce)
- [ESPI_PERIPHERAL_EC_HOST_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga2629a5518a94f031419eeccd05f07373ace2e4ef0298e7c67a82dbfcab43769ad)
- [espi_interrupt_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga4e35c754c720f262805689a94985272c)
- [ESPI_BUS_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca21fadb75fbf1f2131e6b44b318a955a5)
- [ESPI_VIRTUAL_WIRE_CHANNEL_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca6be11dd62eb439a30d95013f2b3ebcee)
- [ESPI_OOB_CHANNEL_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca4b760583473994661ef490a64201b2ac)
- [ESPI_FLASH_CHANNEL_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca3040bdf3cbb3888f3972202091fc5592)
- [ESPI_PERIPHERAL_UART_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca07591a29b44dea00b0218680644c180b)
- [ESPI_PERIPHERAL_DEBUG_PORT80_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca2f59f8c02560181d98b2d3b29de8f800)
- [ESPI_PERIPHERAL_8042_KBC_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272ca0d877c057f5f32c02e55e89afc0a562b)
- [ESPI_PERIPHERAL_HOST_IO_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272cafb7c66ad4601fcd17e4a1c040491c1a3)
- [ESPI_PERIPHERAL_SHARED_MEMORY_EVENTS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga4e35c754c720f262805689a94985272cab402f4c4e5ebe41bd4e7927ab24806dd)
- [espi_cycle_type](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga3e52615f244d7fa8ccda495ab8ec8a5b)
- [ESPI_CYCLE_MEMORY_READ32](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba5b480e093a58849d4181bba22d5868a5)
- [ESPI_CYCLE_MEMORY_READ64](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5bac8ec7673b4466b278dfb5e468f7a4d79)
- [ESPI_CYCLE_MEMORY_WRITE32](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba2e5a736cf8a63491ee13d51ae4f8f073)
- [ESPI_CYCLE_MEMORY_WRITE64](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba54c11e63fcfe3f859af57e65af3f31f7)
- [ESPI_CYCLE_MESSAGE_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba5f2ae0575ca4e9b61c0acd7d4f08ee82)
- [ESPI_CYCLE_MESSAGE_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba380e3d4e6b5579c8bb94e792fcb7d71f)
- [ESPI_CYCLE_OK_COMPLETION_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba0335f2d34fab46960939e2d2c1c12e3f)
- [ESPI_CYCLE_OKCOMPLETION_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5baf3dbc2bcc0ed883bc4d4160c21e6934f)
- [ESPI_CYCLE_NOK_COMPLETION_NODATA](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gga3e52615f244d7fa8ccda495ab8ec8a5ba0edb306e5fabcbf8b009375cde6a8a2b)
- [espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)
- [ESPI_VWIRE_SIGNAL_SLP_S3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab880a7156e489d5f7b8f78550e72b166)
- [ESPI_VWIRE_SIGNAL_SLP_S4](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a4ef1fe12bd09be0875864d6c32164f73)
- [ESPI_VWIRE_SIGNAL_SLP_S5](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ac4b4e30c097a4ef49f21549a799e1e13)
- [ESPI_VWIRE_SIGNAL_OOB_RST_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a2f3f97b51b750050cd98e887e39431d1)
- [ESPI_VWIRE_SIGNAL_PLTRST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a0bafcd0bb7f592f0e308dcfce39bcd08)
- [ESPI_VWIRE_SIGNAL_SUS_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a0e13f250ba0c5a37451c7f3b0e98e663)
- [ESPI_VWIRE_SIGNAL_NMIOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad14b4b7a25141346bfefc507c588a238)
- [ESPI_VWIRE_SIGNAL_SMIOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a1d54a71c6d2e52cb66cfaa0b55b61152)
- [ESPI_VWIRE_SIGNAL_HOST_RST_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35af44250de6f60eabf9b0d85b8860ac56e)
- [ESPI_VWIRE_SIGNAL_SLP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aa4c8c69475b48d88302066823d2f3592)
- [ESPI_VWIRE_SIGNAL_SUS_PWRDN_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab4f0bedd5717660cc8cac2d85c6c3d18)
- [ESPI_VWIRE_SIGNAL_SUS_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a9e32eee077aaa1668c356fe1d4ab1cc5)
- [ESPI_VWIRE_SIGNAL_SLP_WLAN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a3d95f095ae41bba9ef916fc68ddd4779)
- [ESPI_VWIRE_SIGNAL_SLP_LAN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aba8b891a643ca567966d091963be4615)
- [ESPI_VWIRE_SIGNAL_HOST_C10](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab9deb0dd6d4e878eff6413ddc34bb36c)
- [ESPI_VWIRE_SIGNAL_DNX_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a923f3e602d9f8ac821ece2a625183146)
- [ESPI_VWIRE_SIGNAL_PME](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aa87af5b5de184238e5f371851aaee692)
- [ESPI_VWIRE_SIGNAL_WAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a736724f8229aebc356c2720a34a0143f)
- [ESPI_VWIRE_SIGNAL_OOB_RST_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a8e15df6f8159b4c275dc4b20aaec352e)
- [ESPI_VWIRE_SIGNAL_TARGET_BOOT_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a231caf3d46cde2eaf7305bf3f694838c)
- [ESPI_VWIRE_SIGNAL_ERR_NON_FATAL](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a504ae332b89262f70a0bf1a9c8b6f527)
- [ESPI_VWIRE_SIGNAL_ERR_FATAL](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aae0a3fd882c5765db33a4e7bd05e1ab1)
- [ESPI_VWIRE_SIGNAL_TARGET_BOOT_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad99ea62f91b40c8926cda944928e3631)
- [ESPI_VWIRE_SIGNAL_HOST_RST_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a89420628ae26df4c45ef7fba04a3a85e)
- [ESPI_VWIRE_SIGNAL_RST_CPU_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a19c40230e0bb4cee7b6ee42580c28a8d)
- [ESPI_VWIRE_SIGNAL_SMI](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a2d9b2eef499d1bfd13bec1d2caa0e2f3)
- [ESPI_VWIRE_SIGNAL_SCI](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35afa1f99a7e45b306c6736888e280f527c)
- [ESPI_VWIRE_SIGNAL_DNX_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a58280c68c980476aabefa16e0509dd1c)
- [ESPI_VWIRE_SIGNAL_SUS_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35abe28432b566619d8c6cce5e5034e5333)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_0](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_1](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_2](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_3](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_4](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad9b6bb998bea0bc983ab8a6c452d52a1)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_5](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35af10e9e5b320301b2fe923e6793adbeaf)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_6](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35aee0a1576a6e07708e1cde59597b49662)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_7](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ae34962d6db346e02f175894843ce0e1e)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_8](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a8a7b50f0aa53a2c80bae7747d628d219)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_9](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a9410475f349afcf44ddb25ebbd454978)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_10](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a637b5c00aaca05e5daa6969a680cbbb1)
- [ESPI_VWIRE_SIGNAL_TARGET_GPIO_11](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35a07a6b00a4b1cfad2137dc43d7232fc9f)
- [ESPI_VWIRE_SIGNAL_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggab65a0951a8912d9de398cfec0aef7d35ad3319083735295454bc59b742988cfca)
- [lpc_peripheral_opcode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gad00b6a22843e5df9c6d6945d0d82310e)
- [E8042_OBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eac172afb38cb38970ef6242a4f45132f9)
- [E8042_IBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eab70684413d736c8583f3dc53f14b7c7a)
- [E8042_WRITE_KB_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eaa9135a5ea9a5ebd9d25660c37983c5d6)
- [E8042_WRITE_MB_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eaaef0649f867424ec0c7889acb7354911)
- [E8042_RESUME_IRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eac5b666b3319dc2ef0fc571684c2ea198)
- [E8042_PAUSE_IRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea5e7205b5f1371f1a0f2eaed299389475)
- [E8042_CLEAR_OBF](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eacdeb74a9534310f5dab3f1bfb5def534)
- [E8042_READ_KB_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea8c62cd1266681c88aa0cb1af65ab551b)
- [E8042_SET_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea83266d88740588d45be6667a4034c447)
- [E8042_CLEAR_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea5c592b1cad381b296cde832c67264cd1)
- [EACPI_OBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea3cce8bd0205691ecda53fc469606929d)
- [EACPI_IBF_HAS_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea09f241a3f6ffcb5b7839c81c7fc4ea6e)
- [EACPI_WRITE_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea689643f6feb724a303d3b790ff2899f7)
- [EACPI_READ_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea02bf8538a66f633e3d2ec094f57c6173)
- [EACPI_WRITE_STS](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea02c7b1c69d803a5c45304260786afb6f)
- [EACPI_GET_SHARED_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea530fb2a8690538e9659d6eb2c234fb91)
- [ECUSTOM_HOST_SUBS_INTERRUPT_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea113a85c90924922dde04f3b5bf64046b)
- [ECUSTOM_HOST_CMD_GET_PARAM_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310ea464db427cfd432b44874495ed7503db8)
- [ECUSTOM_HOST_CMD_GET_PARAM_MEMORY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eae1e018f0ecde965905752204e557ba40)
- [ECUSTOM_HOST_CMD_SEND_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ggad00b6a22843e5df9c6d6945d0d82310eaf97f7d0d3562dba07b826101bb805243)
- [espi_evt_data_kbc](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [type](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md#a75294f9d88f6dfad7bb56e5af5613c64)
- [data](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md#a5f56bd66943cc82825bb1725bf8a2966)
- [evt](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md#a55e94583f10481a2cdc34ad7ba388f2f)
- [reserved](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md#a0c17b320752b11dc04926df2965807b2)
- [espi_evt_data_acpi](../peripheral_bus_storage_model_reference/P009_espi_evt_data_acpi_结构体.md)
- [type](../peripheral_bus_storage_model_reference/P009_espi_evt_data_acpi_结构体.md#aa5d1e0b548e9be6b65daf67316df8bfe)
- [data](../peripheral_bus_storage_model_reference/P009_espi_evt_data_acpi_结构体.md#a8fb3633a97b1af7618b391539f576c6f)
- [reserved](../peripheral_bus_storage_model_reference/P009_espi_evt_data_acpi_结构体.md#acb291c371bb201d0ceb739fca7e22d3b)
- [espi_evt_data_pvt](../peripheral_bus_storage_model_reference/P011_espi_evt_data_pvt_结构体.md)
- [type](../peripheral_bus_storage_model_reference/P011_espi_evt_data_pvt_结构体.md#adf7edc5acdfb9affde2d1ff1d18cf23d)
- [data](../peripheral_bus_storage_model_reference/P011_espi_evt_data_pvt_结构体.md#a67a1ac452110cfdb0c9c5e0f453c5c57)
- [reserved](../peripheral_bus_storage_model_reference/P011_espi_evt_data_pvt_结构体.md#aff82e44d2a95e985d1a672169f55e4df)
- [espi_event](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md)
- [evt_type](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md#acac75eb1d2b384aa337a5240825b635f)
- [evt_details](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md#aea36925bd3f599c1481c9cc867795c33)
- [evt_data](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md#aa0491cbed5bec091721dfa14898b7277)
- [espi_cfg](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md)
- [io_caps](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md#a75175c60a31c3a88c83772b99c2a5c34)
- [channel_caps](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md#abb24c88ecc977d8116973d44a7e7cb94)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [max_freq](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md#aed88dd6fc8028a7c281260e7fa29ce21)
- [espi_request_packet](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md)
- [cycle_type](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md#a9b474155dfa0c74d0bd55e4b831b383a)
- [tag](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md#a22a0111e338827125eaf79ce8516b744)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [len](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md#ae8b7dc12b04f469b5689ad27cc4f0643)
- [address](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md#a4ac2d50786fdc4c4bd8da88bde28f77d)
- [data](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md#a6f808763faf949ff7ef83d68fb71e7ba)
- [espi_oob_packet](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md)
- [buf](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md#a0b19890b5e63ecbd1b95eef57fd9263f)
- [len](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md#adf45a10c88a171df8e7138929958b346)
- [espi_flash_packet](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md)
- [buf](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md#a22244bc4063618707eea571f170bdfde)
- [flash_addr](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md#ac638c0b5d0d98e15ab66850afc394cec)
- [len](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md#adade51336ae37a519c06b12bf19fc86d)
- [espi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga9d848c7e367cf277230f365f73c15c46)
- [device](../device_reference/P002_设备对象结构.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [espi_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga97336083a3ed3f561301fcf5762dc73c)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [espi_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga4712365e3a38d859fefbf0e9a6f32b07)
- [espi_api_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga3c3e6a70a04c14ec50fa0dcef4055f73)
- [espi_api_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga47ea19517406b64f074b4eee7a9d1923)
- [espi_api_lpc_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga04547d61ee4ed5d34fca3fb11ec0370f)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [espi_api_lpc_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gac7e3730c214b877772b24c4055ab997a)
- [espi_api_send_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga838aefb5fbe399f6492803ceb391fa8c)
- [espi_api_receive_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga806a0b3f3f4e629c5556f1399c4e29e2)
- [espi_api_send_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gae7497b9629a9444f94dae125fdf46005)
- [espi_api_receive_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga79255a516e48256d8381d0b32e5ae345)
- [espi_api_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga6bb1bb8af96c58dc0d9ad041d95cd397)
- [espi_api_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga1a8715b387a037dddacc92424fe0ba6f)
- [espi_api_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga422abe38a4d2cce441d5165192adc982)
- [espi_api_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#gab0313b00d884426800395ec5a907f744)
- [espi_api_interrupt_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface__backend.html#ga7d497e1f4573f54f49202b67cb5cbe5c)
- [espi_driver_api](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md)
- [config](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#ae7f3be0766c35a75d611735f09e6b728)
- [get_channel_status](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#ac27072d18c70f4b415467d01a37a2f75)
- [read_request](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#ac9033b4b59e0c99747e367ed283ab116)
- [write_request](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a5ff3310cd5db4a08c42284cc4ea48057)
- [read_lpc_request](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#aea877fee89f0d346b009c053a3c0a09d)
- [write_lpc_request](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a049bff890414ce43f2323238a6ee3d15)
- [send_vwire](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a2241bb06a85d6220417cee282e359021)
- [receive_vwire](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a53b561bfa5dbc53dbf8cbb6af88c1b36)
- [send_oob](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a47041efc4fb0879b2812bb53533b8ab8)
- [receive_oob](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a5c1be83cf9f3eac140b8ab7b37a86c1b)
- [flash_read](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a2ae357ec0cf8f4ee548f50350bd4eaa4)
- [flash_write](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a74218772f99c24af2fe9ae5b1749039e)
- [flash_erase](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#abfd2310657421141737af0f8316825ef)
- [manage_callback](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#adfcdf83461d94819c788dac869b09096)
- [interrupt_config](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a96ad30567d449161c7c30f86b9500808)
- [espi_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga7227c53d384eb0dc666361261f069f68)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [espi_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga869551e20fc2c3be4311c21c3c53999d)
- [espi_read_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga112f7554ba614c8e5f239b1319b4a763)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [espi_write_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga143ed88b1f220f9582c809165fd983fd)
- [espi_read_lpc_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaeaae20afa90d9d825d80997369f31465)
- [espi_write_lpc_request](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga880b6b04824f9f0deea10e8018573b88)
- [espi_send_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gacab2b3bff7d940e71ee1c2a9fdedf782)
- [signal](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html#a5d326f119f87d0facaa662520f8c322a)
- [espi_receive_vwire](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gaa8bb48b5592c4b49d27c9b8a42432410)
- [espi_send_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga2557cfc7a38f669d14e9826e3fb0fdee)
- [espi_receive_oob](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga4b8f4fbf66a2b2ae394e00b16500f70d)
- [espi_read_flash](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga0a97d11167367342283bfe6b6d66726e)
- [espi_write_flash](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab02d46fd690e33875cc1b2433c976891)
- [espi_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab42be7c76c4523cea96365aa77fd18be)
- [espi_init_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga8d88e4e3893d610713195e5352ec2565)
- [espi_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gabf5f0ea01ec8ed5345b2e119181c2313)
- [espi_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga7f04f98ea6a4671b821cf6ddf6bbf2a6)
- [espi_interrupt_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga1cd0afc52d533414b5bbc684cef8b9af)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [espi_cfg::io_caps](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md#a75175c60a31c3a88c83772b99c2a5c34)
- [espi_cfg::channel_caps](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md#abb24c88ecc977d8116973d44a7e7cb94)
- [espi_cfg::max_freq](../peripheral_bus_storage_model_reference/P006_espi_cfg_结构体.md#aed88dd6fc8028a7c281260e7fa29ce21)
- [espi_driver_api::write_lpc_request](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a049bff890414ce43f2323238a6ee3d15)
- [espi_driver_api::send_vwire](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a2241bb06a85d6220417cee282e359021)
- [espi_driver_api::flash_read](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a2ae357ec0cf8f4ee548f50350bd4eaa4)
- [espi_driver_api::send_oob](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a47041efc4fb0879b2812bb53533b8ab8)
- [espi_driver_api::receive_vwire](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a53b561bfa5dbc53dbf8cbb6af88c1b36)
- [espi_driver_api::receive_oob](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a5c1be83cf9f3eac140b8ab7b37a86c1b)
- [espi_driver_api::write_request](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a5ff3310cd5db4a08c42284cc4ea48057)
- [espi_driver_api::flash_write](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a74218772f99c24af2fe9ae5b1749039e)
- [espi_driver_api::interrupt_config](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#a96ad30567d449161c7c30f86b9500808)
- [espi_driver_api::flash_erase](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#abfd2310657421141737af0f8316825ef)
- [espi_driver_api::get_channel_status](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#ac27072d18c70f4b415467d01a37a2f75)
- [espi_driver_api::read_request](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#ac9033b4b59e0c99747e367ed283ab116)
- [espi_driver_api::manage_callback](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#adfcdf83461d94819c788dac869b09096)
- [espi_driver_api::config](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#ae7f3be0766c35a75d611735f09e6b728)
- [espi_driver_api::read_lpc_request](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md#aea877fee89f0d346b009c053a3c0a09d)
- [espi_event::evt_data](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md#aa0491cbed5bec091721dfa14898b7277)
- [espi_event::evt_type](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md#acac75eb1d2b384aa337a5240825b635f)
- [espi_event::evt_details](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md#aea36925bd3f599c1481c9cc867795c33)
- [espi_evt_data_acpi::data](../peripheral_bus_storage_model_reference/P009_espi_evt_data_acpi_结构体.md#a8fb3633a97b1af7618b391539f576c6f)
- [espi_evt_data_acpi::type](../peripheral_bus_storage_model_reference/P009_espi_evt_data_acpi_结构体.md#aa5d1e0b548e9be6b65daf67316df8bfe)
- [espi_evt_data_acpi::reserved](../peripheral_bus_storage_model_reference/P009_espi_evt_data_acpi_结构体.md#acb291c371bb201d0ceb739fca7e22d3b)
- [espi_evt_data_kbc::reserved](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md#a0c17b320752b11dc04926df2965807b2)
- [espi_evt_data_kbc::evt](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md#a55e94583f10481a2cdc34ad7ba388f2f)
- [espi_evt_data_kbc::data](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md#a5f56bd66943cc82825bb1725bf8a2966)
- [espi_evt_data_kbc::type](../peripheral_bus_storage_model_reference/P010_espi_evt_data_kbc_结构体.md#a75294f9d88f6dfad7bb56e5af5613c64)
- [espi_evt_data_pvt::data](../peripheral_bus_storage_model_reference/P011_espi_evt_data_pvt_结构体.md#a67a1ac452110cfdb0c9c5e0f453c5c57)
- [espi_evt_data_pvt::type](../peripheral_bus_storage_model_reference/P011_espi_evt_data_pvt_结构体.md#adf7edc5acdfb9affde2d1ff1d18cf23d)
- [espi_evt_data_pvt::reserved](../peripheral_bus_storage_model_reference/P011_espi_evt_data_pvt_结构体.md#aff82e44d2a95e985d1a672169f55e4df)
- [espi_flash_packet::buf](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md#a22244bc4063618707eea571f170bdfde)
- [espi_flash_packet::flash_addr](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md#ac638c0b5d0d98e15ab66850afc394cec)
- [espi_flash_packet::len](../peripheral_bus_storage_model_reference/P012_espi_flash_packet_结构体.md#adade51336ae37a519c06b12bf19fc86d)
- [espi_oob_packet::buf](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md#a0b19890b5e63ecbd1b95eef57fd9263f)
- [espi_oob_packet::len](../peripheral_bus_storage_model_reference/P013_espi_oob_packet_结构体.md#adf45a10c88a171df8e7138929958b346)
- [espi_request_packet::tag](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md#a22a0111e338827125eaf79ce8516b744)
- [espi_request_packet::address](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md#a4ac2d50786fdc4c4bd8da88bde28f77d)
- [espi_request_packet::data](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md#a6f808763faf949ff7ef83d68fb71e7ba)
- [espi_request_packet::cycle_type](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md#a9b474155dfa0c74d0bd55e4b831b383a)
- [espi_request_packet::len](../peripheral_bus_storage_model_reference/P014_espi_request_packet_结构体.md#ae8b7dc12b04f469b5689ad27cc4f0643)

---

[上一章](P003_zephyr__drivers__disk.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__drivers__espi_saf.h_头文件源码.md)
