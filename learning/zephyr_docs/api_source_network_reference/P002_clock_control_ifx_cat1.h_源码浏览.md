---
id: learning.zephyr-docs.api-source-network-reference.page-2
title: clock_control_ifx_cat1.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx__cat1_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_clock\_control\_ifx\_cat1.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx__cat1_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx__cat1_8h.html)。

## 2.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00025"></a>
<a id="l00027"></a>
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
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="foldopen00084"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
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
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
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
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
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
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
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
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
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
<a id="l00315"></a>
<a id="l00316"></a>
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
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
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
<a id="l00376"></a>
<a id="l00377"></a>
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
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="foldopen00407"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="foldopen00417"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00445"></a>
<a id="foldopen00446"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00467"></a>
<a id="foldopen00468"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00489"></a>
<a id="foldopen00490"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="foldopen00515"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00531"></a>
<a id="foldopen00532"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00556"></a>
<a id="foldopen00557"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="foldopen00580"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00602"></a>
<a id="foldopen00603"></a>
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
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00626"></a>
<a id="foldopen00627"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00691"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="foldopen00734"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga0421e7b519bd9b829baa8a2e7b234931"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga04bb0312c12347d0ceac9fc033993221"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga16cf7a3976d594e17bdcb595d024a6f7"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga1b13def736a7046ee628830ab686ef3a"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga1dba84b96bf16b98d672369a4bbe58c8"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga4b7e7866dd86214ce5910c2d01dcf49c"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga4c10fa4f6073001fde1fd49fe3769181"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga5516442b0c25b62024b765545fa2b18f"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga5deb0165e6f3e18acd4d3b841f96c50b"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga6bfb0915441740364a239ca3a68d6d8b"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga726332ad1db3729a208a2be1458478ec"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga7585bc918f0435fcea3de69f5d2368c2"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga933b6bafae3eef87ac8e0a4ae7a849d4"></a>
<a id="agroup__clock__control__ifx__cat1_html_ga9ffa2a2c7427ea6049d7790f725ec185"></a>
<a id="agroup__clock__control__ifx__cat1_html_gab111d1af9166ca01d139b3e0512a811b"></a>
<a id="agroup__clock__control__ifx__cat1_html_gab62704a8cdfda5914cfb7dfe81afa8c0"></a>
<a id="agroup__clock__control__ifx__cat1_html_gab9ed6e703b1b98d5a713a8ec4cfbab79"></a>
<a id="agroup__clock__control__ifx__cat1_html_gacacef8eba03b64537cbd0f09c3425089"></a>
<a id="agroup__clock__control__ifx__cat1_html_gad55fafafdec37c322f2faf036e955dcf"></a>
<a id="agroup__clock__control__ifx__cat1_html_gadda478f75d4546b4de8d978e56dba1fa"></a>
<a id="agroup__clock__control__ifx__cat1_html_gadf9e87e3582b2042993c3237afe20383"></a>
<a id="agroup__clock__control__ifx__cat1_html_gaf1b81772f3de1dfcd08b5eaf96b60b33"></a>
<a id="agroup__clock__control__ifx__cat1_html_gaf8c74267c99cdebf0ae977555336f65c"></a>
<a id="agroup__clock__control__ifx__cat1_html_gafe5b77c891a50a08f364fa4d85af29ac"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructifx__cat1__clock_html"></a>
<a id="astructifx__cat1__clock_html_a0e1e36ab2abe21b227f8b76d195fc627"></a>
<a id="astructifx__cat1__clock_html_a4361f9f52e5621aedc0b4f2e0e011896"></a>
<a id="astructifx__cat1__clock_html_a95619b170032a2b9b111d2f59602fbe7"></a>
<a id="astructifx__cat1__clock_html_ac02e464103810c9907c16194eba88979"></a>
<a id="astructifx__cat1__clock_html_ae8032f282998a9d9a31c5d967f384a4e"></a>
<a id="astructifx__cat1__clock_html_af59f4aff030f57cffc4a44d761f18d66"></a>
<a id="astructifx__cat1__resource__inst_html"></a>
<a id="astructifx__cat1__resource__inst_html_a50f1d0589e90b071ddc451efcbb56892"></a>
<a id="astructifx__cat1__resource__inst_html_a711df9cb83f6d7545b939fd56a7e10e7"></a>
<a id="astructifx__cat1__resource__inst_html_ad71f2ec8d25fa0792e287b1e0a58ca3f"></a>

```c
/*
 * Copyright (c) 2025 Cypress Semiconductor Corporation (an Infineon company) or
 * an affiliate of Cypress Semiconductor Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_IFX_CAT1_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_IFX_CAT1_H_


#include <cy_sysclk.h>
#include <cy_systick.h>



#define IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(block) ((cy_en_divider_types_t)((block) & 0x03))

#if !defined(CONFIG_SOC_FAMILY_INFINEON_EDGE)
/* Converts the group/div pair into a unique block number. */
#define IFX_CAT1_PERIPHERAL_GROUP_ADJUST(group, div) (((group) << 2) | (div))

#define IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(gr)                                                        \
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL##gr##_8BIT = IFX_CAT1_PERIPHERAL_GROUP_ADJUST(             \
                (gr), CY_SYSCLK_DIV_8_BIT),                   \
                IFX_CAT1_CLOCK_BLOCK_PERIPHERAL##gr##_16BIT = IFX_CAT1_PERIPHERAL_GROUP_ADJUST(    \
                        (gr), CY_SYSCLK_DIV_16_BIT),         \
                IFX_CAT1_CLOCK_BLOCK_PERIPHERAL##gr##_16_5BIT = IFX_CAT1_PERIPHERAL_GROUP_ADJUST(  \
                        (gr), CY_SYSCLK_DIV_16_5_BIT),     \
                IFX_CAT1_CLOCK_BLOCK_PERIPHERAL##gr##_24_5BIT = IFX_CAT1_PERIPHERAL_GROUP_ADJUST(  \
                        (gr), CY_SYSCLK_DIV_24_5_BIT)
#else
/* Converts the group/div pair into a unique block number. */
#define IFX_CAT1_PERIPHERAL_GROUP_ADJUST(instance, group, div)                                     \
        (((group + (instance * PERI0_PERI_PCLK_PCLK_GROUP_NR)) << 2) | (div))
#define IFX_CAT1_PERIPHERAL_CLOCK_GET_INSTANCE(clock) ((clock >> 2) / PERI0_PERI_PCLK_PCLK_GROUP_NR)
#define IFX_CAT1_PERIPHERAL_CLOCK_GET_GROUP(clock)                                                 \
        ((clock >> 2) -                                                                            \
         (IFX_CAT1_PERIPHERAL_CLOCK_GET_INSTANCE(clock) * PERI0_PERI_PCLK_PCLK_GROUP_NR))

#define IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(instance, gr)                                              \
        IFX_CAT1_CLOCK_BLOCK##instance##_PERIPHERAL##gr##_8BIT =                                   \
                IFX_CAT1_PERIPHERAL_GROUP_ADJUST((instance), (gr), CY_SYSCLK_DIV_8_BIT),           \
        IFX_CAT1_CLOCK_BLOCK##instance##_PERIPHERAL##gr##_16BIT =                                  \
                IFX_CAT1_PERIPHERAL_GROUP_ADJUST((instance), (gr), CY_SYSCLK_DIV_16_BIT),          \
        IFX_CAT1_CLOCK_BLOCK##instance##_PERIPHERAL##gr##_16_5BIT =                                \
                IFX_CAT1_PERIPHERAL_GROUP_ADJUST((instance), (gr), CY_SYSCLK_DIV_16_5_BIT),        \
        IFX_CAT1_CLOCK_BLOCK##instance##_PERIPHERAL##gr##_24_5BIT =                                \
                IFX_CAT1_PERIPHERAL_GROUP_ADJUST((instance), (gr), CY_SYSCLK_DIV_24_5_BIT)
#endif


#define CLK_HF0  (0U)
#define CLK_HF1  (1U)
#define CLK_HF2  (2U)
#define CLK_HF3  (3U)
#define CLK_HF4  (4U)
#define CLK_HF5  (5U)
#define CLK_HF6  (6U)
#define CLK_HF7  (7U)
#define CLK_HF8  (8U)
#define CLK_HF9  (9U)
#define CLK_HF10 (10U)
#define CLK_HF11 (11U)
#define CLK_HF12 (12U)
#define CLK_HF13 (13U)

enum ifx_cat1_clock_block {
#if defined(CONFIG_SOC_FAMILY_INFINEON_CAT1A)
        /* The first four items are here for backwards compatibility with old clock APIs */
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_8BIT = CY_SYSCLK_DIV_8_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_16BIT =
                CY_SYSCLK_DIV_16_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_16_5BIT =
                CY_SYSCLK_DIV_16_5_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_24_5BIT =
                CY_SYSCLK_DIV_24_5_BIT,

        IFX_CAT1_CLOCK_BLOCK_IMO,
        IFX_CAT1_CLOCK_BLOCK_ECO,
        IFX_CAT1_CLOCK_BLOCK_EXT,
        IFX_CAT1_CLOCK_BLOCK_ALTHF,
        IFX_CAT1_CLOCK_BLOCK_ALTLF,
        IFX_CAT1_CLOCK_BLOCK_ILO,
#if !(defined(SRSS_HT_VARIANT) && (SRSS_HT_VARIANT > 0))
        IFX_CAT1_CLOCK_BLOCK_PILO,
#endif

        IFX_CAT1_CLOCK_BLOCK_WCO,
        IFX_CAT1_CLOCK_BLOCK_MFO,

        IFX_CAT1_CLOCK_BLOCK_PATHMUX,

        IFX_CAT1_CLOCK_BLOCK_FLL,
#if defined(CY_IP_MXS40SRSS) && (CY_IP_MXS40SRSS_VERSION >= 3)
        IFX_CAT1_CLOCK_BLOCK_PLL200,
        IFX_CAT1_CLOCK_BLOCK_PLL400,
#else
        IFX_CAT1_CLOCK_BLOCK_PLL,
#endif

        IFX_CAT1_CLOCK_BLOCK_LF,
        IFX_CAT1_CLOCK_BLOCK_MF,
        IFX_CAT1_CLOCK_BLOCK_HF,

        IFX_CAT1_CLOCK_BLOCK_PUMP,
        IFX_CAT1_CLOCK_BLOCK_BAK,
        IFX_CAT1_CLOCK_BLOCK_TIMER,
        IFX_CAT1_CLOCK_BLOCK_ALT_SYS_TICK,

        IFX_CAT1_CLOCK_BLOCK_FAST,
        IFX_CAT1_CLOCK_BLOCK_PERI,
        IFX_CAT1_CLOCK_BLOCK_SLOW,

#elif defined(COMPONENT_CAT1B)

        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_8BIT =
                CY_SYSCLK_DIV_8_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_16BIT =
                CY_SYSCLK_DIV_16_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_16_5BIT =
                CY_SYSCLK_DIV_16_5_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_24_5BIT =
                CY_SYSCLK_DIV_24_5_BIT,

/* The first four items are here for backwards compatibility with old clock APIs */
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 1)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 2)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(1),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 3)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(2),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 4)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(3),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 5)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(4),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 6)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(5),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 7)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(6),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 8)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(7),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 9)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(8),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 10)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(9),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 11)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(10),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 12)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(11),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 13)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(12),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 14)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(13),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 15)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(14),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 16)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(15),
#endif

        IFX_CAT1_CLOCK_BLOCK_IHO,
        IFX_CAT1_CLOCK_BLOCK_IMO,
        IFX_CAT1_CLOCK_BLOCK_ECO,
        IFX_CAT1_CLOCK_BLOCK_EXT,
        IFX_CAT1_CLOCK_BLOCK_ALTHF,
        IFX_CAT1_CLOCK_BLOCK_ALTLF,
        IFX_CAT1_CLOCK_BLOCK_ILO,
        IFX_CAT1_CLOCK_BLOCK_PILO,
        IFX_CAT1_CLOCK_BLOCK_WCO,
        IFX_CAT1_CLOCK_BLOCK_MFO,

        IFX_CAT1_CLOCK_BLOCK_PATHMUX,

        IFX_CAT1_CLOCK_BLOCK_FLL,
        IFX_CAT1_CLOCK_BLOCK_PLL200,
        IFX_CAT1_CLOCK_BLOCK_PLL400,
        IFX_CAT1_CLOCK_BLOCK_ECO_PRESCALER,

        IFX_CAT1_CLOCK_BLOCK_LF,
        IFX_CAT1_CLOCK_BLOCK_MF,
        IFX_CAT1_CLOCK_BLOCK_HF,

        IFX_CAT1_CLOCK_BLOCK_PUMP,
        IFX_CAT1_CLOCK_BLOCK_BAK,
        IFX_CAT1_CLOCK_BLOCK_ALT_SYS_TICK,
        IFX_CAT1_CLOCK_BLOCK_PERI,

#elif defined(COMPONENT_CAT1C)

        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_8BIT =
                CY_SYSCLK_DIV_8_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_16BIT =
                CY_SYSCLK_DIV_16_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_16_5BIT =
                CY_SYSCLK_DIV_16_5_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_24_5BIT =
                CY_SYSCLK_DIV_24_5_BIT,

/* The first four items are here for backwards compatibility with old clock APIs */
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 1)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 2)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(1),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 3)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(2),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 4)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(3),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 5)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(4),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 6)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(5),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 7)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(6),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 8)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(7),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 9)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(8),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 10)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(9),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 11)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(10),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 12)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(11),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 13)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(12),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 14)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(13),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 15)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(14),
#endif
#if (PERI_PERI_PCLK_PCLK_GROUP_NR >= 16)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(15),
#endif

        IFX_CAT1_CLOCK_BLOCK_IMO,
        IFX_CAT1_CLOCK_BLOCK_ECO,
        IFX_CAT1_CLOCK_BLOCK_EXT,
        IFX_CAT1_CLOCK_BLOCK_ILO,
        IFX_CAT1_CLOCK_BLOCK_WCO,

        IFX_CAT1_CLOCK_BLOCK_PATHMUX,

        IFX_CAT1_CLOCK_BLOCK_FLL,
        IFX_CAT1_CLOCK_BLOCK_PLL200,
        IFX_CAT1_CLOCK_BLOCK_PLL400,

        IFX_CAT1_CLOCK_BLOCK_LF,
        IFX_CAT1_CLOCK_BLOCK_HF,
        IFX_CAT1_CLOCK_BLOCK_BAK,
        IFX_CAT1_CLOCK_BLOCK_ALT_SYS_TICK,

        IFX_CAT1_CLOCK_BLOCK_PERI,
        IFX_CAT1_CLOCK_BLOCK_FAST,
        IFX_CAT1_CLOCK_BLOCK_SLOW,
        IFX_CAT1_CLOCK_BLOCK_MEM,
        IFX_CAT1_CLOCK_BLOCK_TIMER,
#elif defined(CONFIG_SOC_FAMILY_INFINEON_EDGE)

        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_8BIT =
                CY_SYSCLK_DIV_8_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_16BIT =
                CY_SYSCLK_DIV_16_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_16_5BIT =
                CY_SYSCLK_DIV_16_5_BIT,
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_24_5BIT =
                CY_SYSCLK_DIV_24_5_BIT,

#if (PERI0_PERI_PCLK_PCLK_GROUP_NR >= 1)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0, 0),
#endif
#if (PERI0_PERI_PCLK_PCLK_GROUP_NR >= 2)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0, 1),
#endif
#if (PERI0_PERI_PCLK_PCLK_GROUP_NR >= 3)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0, 2),
#endif
#if (PERI0_PERI_PCLK_PCLK_GROUP_NR >= 4)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0, 3),
#endif
#if (PERI0_PERI_PCLK_PCLK_GROUP_NR >= 5)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0, 4),
#endif
#if (PERI0_PERI_PCLK_PCLK_GROUP_NR >= 6)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0, 5),
#endif
#if (PERI0_PERI_PCLK_PCLK_GROUP_NR >= 7)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0, 6),
#endif
#if (PERI0_PERI_PCLK_PCLK_GROUP_NR >= 8)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0, 7),
#endif
#if (PERI0_PERI_PCLK_PCLK_GROUP_NR >= 9)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0, 8),
#endif
#if (PERI0_PERI_PCLK_PCLK_GROUP_NR >= 10)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(0, 9),
#endif
#if (PERI0_PERI_PCLK_PCLK_GROUP_NR >= 11)
#warning "Unhandled PERI0 PCLK number"
#endif

#if (PERI1_PERI_PCLK_PCLK_GROUP_NR >= 1)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(1, 0),
#endif
#if (PERI1_PERI_PCLK_PCLK_GROUP_NR >= 2)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(1, 1),
#endif
#if (PERI1_PERI_PCLK_PCLK_GROUP_NR >= 3)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(1, 2),
#endif
#if (PERI1_PERI_PCLK_PCLK_GROUP_NR >= 4)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(1, 3),
#endif
#if (PERI1_PERI_PCLK_PCLK_GROUP_NR >= 5)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(1, 4),
#endif
#if (PERI1_PERI_PCLK_PCLK_GROUP_NR >= 6)
        IFX_CAT1_CLOCK_BLOCK_PERI_GROUP(1, 5),
#endif
#if (PERI1_PERI_PCLK_PCLK_GROUP_NR >= 7)
#warning "Unhandled PERI1 PCLK number"
#endif

        IFX_CAT1_CLOCK_BLOCK_IHO,
        IFX_CAT1_CLOCK_BLOCK_ECO,
        IFX_CAT1_CLOCK_BLOCK_EXT,
        IFX_CAT1_CLOCK_BLOCK_PILO,
        IFX_CAT1_CLOCK_BLOCK_WCO,

        IFX_CAT1_CLOCK_BLOCK_PATHMUX,

        IFX_CAT1_CLOCK_BLOCK_DPLL250,
        IFX_CAT1_CLOCK_BLOCK_DPLL500,
        IFX_CAT1_CLOCK_BLOCK_ECO_PRESCALER,

        IFX_CAT1_CLOCK_BLOCK_LF,
        IFX_CAT1_CLOCK_BLOCK_MF,
        IFX_CAT1_CLOCK_BLOCK_HF,

        IFX_CAT1_CLOCK_BLOCK_BAK,
        IFX_CAT1_CLOCK_BLOCK_PERI,

#elif defined(CONFIG_SOC_FAMILY_INFINEON_PSOC4)
        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_16BIT =
                CY_SYSCLK_DIV_16_BIT, /* Equal to IFX_CAT1_CLOCK_BLOCK_PERIPHERAL0_16_BIT */

        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_16_5BIT =
                CY_SYSCLK_DIV_16_5_BIT, /* Equal to IFX_CAT1_CLOCK_BLOCK_PERIPHERAL0_16_5_BIT */

        IFX_CAT1_CLOCK_BLOCK_PERIPHERAL_24_5BIT =
                CY_SYSCLK_DIV_24_5_BIT, /* Equal to IFX_CAT1_CLOCK_BLOCK_PERIPHERAL0_24_5_BIT */
#endif
};

struct ifx_cat1_clock {
        enum ifx_cat1_clock_block block;
        uint8_t channel;
        uint8_t instance;
        uint8_t group;
        bool reserved;
        const void *funcs;
};

struct ifx_cat1_resource_inst {
        uint8_t type;
        uint8_t block_num;
        uint8_t channel_num;
};

int ifx_cat1_clock_control_get_frequency(uint32_t dt_ord, uint32_t *frequency);

static inline uint32_t
ifx_cat1_utils_peri_pclk_get_frequency(en_clk_dst_t clk_dest,
                                       const struct ifx_cat1_clock *peri_clock)
{
#if defined(COMPONENT_CAT1B) || defined(COMPONENT_CAT1C) || defined(CONFIG_SOC_FAMILY_INFINEON_EDGE)
        return Cy_SysClk_PeriPclkGetFrequency(
                clk_dest, IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block),
                peri_clock->channel);
#else
        CY_UNUSED_PARAMETER(clk_dest);
        return Cy_SysClk_PeriphGetFrequency(
                IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block), peri_clock->channel);
#endif
}

static inline cy_rslt_t
ifx_cat1_utils_peri_pclk_enable_divider(en_clk_dst_t clk_dest,
                                        const struct ifx_cat1_clock *peri_clock)
{
#if defined(COMPONENT_CAT1B) || defined(COMPONENT_CAT1C) || defined(CONFIG_SOC_FAMILY_INFINEON_EDGE)
        return Cy_SysClk_PeriPclkEnableDivider(
                clk_dest, IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block),
                peri_clock->channel);
#else
        CY_UNUSED_PARAMETER(clk_dest);
        return Cy_SysClk_PeriphEnableDivider(
                IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block), peri_clock->channel);
#endif
}

static inline cy_rslt_t
ifx_cat1_utils_peri_pclk_disable_divider(en_clk_dst_t clk_dest,
                                         const struct ifx_cat1_clock *peri_clock)
{
#if defined(COMPONENT_CAT1B) || defined(COMPONENT_CAT1C) || defined(CONFIG_SOC_FAMILY_INFINEON_EDGE)
        return Cy_SysClk_PeriPclkDisableDivider(
                clk_dest, IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block),
                peri_clock->channel);
#else
        CY_UNUSED_PARAMETER(clk_dest);
        return Cy_SysClk_PeriphDisableDivider(
                IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block), peri_clock->channel);
#endif
}

static inline bool ifx_cat1_utils_peri_is_fract_div(const struct ifx_cat1_clock *peri_clock)
{
        cy_en_divider_types_t type =
                IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block);

        return (type == CY_SYSCLK_DIV_16_5_BIT) || (type == CY_SYSCLK_DIV_24_5_BIT);
}

static inline cy_rslt_t
ifx_cat1_utils_peri_pclk_set_divider(en_clk_dst_t clk_dest,
                                     const struct ifx_cat1_clock *peri_clock, uint32_t div)
{
#if defined(COMPONENT_CAT1B) || defined(COMPONENT_CAT1C) || defined(CONFIG_SOC_FAMILY_INFINEON_EDGE)
        return Cy_SysClk_PeriPclkSetDivider(
                clk_dest, IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block),
                peri_clock->channel, div);
#else
        CY_UNUSED_PARAMETER(clk_dest);
        return Cy_SysClk_PeriphSetDivider(
                IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block), peri_clock->channel,
                div);
#endif
}

static inline cy_rslt_t
ifx_cat1_utils_peri_pclk_set_frac_divider(en_clk_dst_t clk_dest,
                                          const struct ifx_cat1_clock *peri_clock, uint32_t div_int,
                                          uint32_t div_frac)
{
#if defined(COMPONENT_CAT1B) || defined(COMPONENT_CAT1C) || defined(CONFIG_SOC_FAMILY_INFINEON_EDGE)
        return Cy_SysClk_PeriPclkSetFracDivider(
                clk_dest, IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block),
                peri_clock->channel, div_int, div_frac);
#else
        CY_UNUSED_PARAMETER(clk_dest);
        return Cy_SysClk_PeriphSetFracDivider(
                IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block), peri_clock->channel,
                div_int, div_frac);
#endif
}

static inline uint32_t ifx_cat1_utils_peri_pclk_get_divider(en_clk_dst_t clk_dest,
                                                            const struct ifx_cat1_clock *peri_clock)
{
#if defined(COMPONENT_CAT1B) || defined(COMPONENT_CAT1C) || defined(CONFIG_SOC_FAMILY_INFINEON_EDGE)
        return Cy_SysClk_PeriPclkGetDivider(
                clk_dest, IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block),
                peri_clock->channel);
#else
        CY_UNUSED_PARAMETER(clk_dest);
        return Cy_SysClk_PeriphGetDivider(
                IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block), peri_clock->channel);
#endif
}

static inline void
ifx_cat1_utils_peri_pclk_get_frac_divider(en_clk_dst_t clk_dest,
                                          const struct ifx_cat1_clock *peri_clock,
                                          uint32_t *div_int, uint32_t *div_frac)
{
#if defined(COMPONENT_CAT1B) || defined(COMPONENT_CAT1C) || defined(CONFIG_SOC_FAMILY_INFINEON_EDGE)
        Cy_SysClk_PeriPclkGetFracDivider(
                clk_dest, IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block),
                peri_clock->channel, div_int, div_frac);
#else
        CY_UNUSED_PARAMETER(clk_dest);
        Cy_SysClk_PeriphGetFracDivider(
                IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block), peri_clock->channel,
                div_int, div_frac);
#endif
}

static inline cy_rslt_t
ifx_cat1_utils_peri_pclk_assign_divider(en_clk_dst_t clk_dest,
                                        const struct ifx_cat1_clock *peri_clock)
{
#if defined(COMPONENT_CAT1B) || defined(COMPONENT_CAT1C) || defined(CONFIG_SOC_FAMILY_INFINEON_EDGE)
        return Cy_SysClk_PeriPclkAssignDivider(
                clk_dest, IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block),
                peri_clock->channel);
#else
        return Cy_SysClk_PeriphAssignDivider(
                clk_dest, IFX_CAT1_PERIPHERAL_GROUP_GET_DIVIDER_TYPE(peri_clock->block),
                peri_clock->channel);
#endif
}

#if defined(CONFIG_SOC_FAMILY_INFINEON_EDGE)
#define IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(instance, group) (((instance) << 4) | (group))

static inline uint8_t ifx_cat1_utils_peri_pclk_get_hfclk(uint8_t peri_group)
{
        switch (peri_group) {
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(0, 0):
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(1, 4):
                return CLK_HF0;
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(0, 7):
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(1, 0):
                return CLK_HF1;
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(0, 3):
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(1, 2):
                return CLK_HF5;
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(0, 4):
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(1, 3):
                return CLK_HF6;
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(1, 1):
                return CLK_HF7;
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(0, 2):
                return CLK_HF9;
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(0, 1):
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(0, 5):
                return CLK_HF10;
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(0, 8):
                return CLK_HF11;
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(0, 6):
        case IFX_CAT1_PERIPHERAL_INSTANCE_GROUP(0, 9):
                return CLK_HF13;
        default:
                break;
        }
        return -EINVAL;
}

#elif defined(CONFIG_SOC_FAMILY_INFINEON_CAT1B)
static inline uint8_t ifx_cat1_utils_peri_pclk_get_hfclk(uint8_t peri_group)
{
        switch (peri_group) {
        case 0:
        case 2:
                return CLK_HF0;
        case 1:
        case 3:
                return CLK_HF1;
        case 4:
                return CLK_HF2;
        case 5:
                return CLK_HF3;
        case 6:
                return CLK_HF4;
        default:
                break;
        }
        return -EINVAL;
}

#else /* !CONFIG_SOC_FAMILY_INFINEON_EDGE && !CONFIG_SOC_FAMILY_INFINEON_CAT1B */
static inline uint8_t ifx_cat1_utils_peri_pclk_get_hfclk(uint8_t peri_group)
{
        ARG_UNUSED(peri_group);

        return -EINVAL;
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_IFX_CAT1_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权所有（Copyright）2025 Cypress Semiconductor Corporation（Infineon 旗下公司）或 Cypress Semiconductor Corporation 的关联公司。

SPDX-License-Identifier: Apache-2.0。

### 注释 2：原第 31 行

将组／分频器组合（Group / Div Pair）转换为唯一块编号（Unique Block Number）。

### 注释 3：原第 44 行

将组／分频器组合（Group / Div Pair）转换为唯一块编号（Unique Block Number）。

### 注释 4：原第 86 行

前四项用于保持与旧时钟 API（Clock APIs）的向后兼容（Backwards Compatibility）。

### 注释 5：原第 144 行

前四项用于保持与旧时钟 API（Clock APIs）的向后兼容（Backwards Compatibility）。

### 注释 6：原第 234 行

前四项用于保持与旧时钟 API（Clock APIs）的向后兼容（Backwards Compatibility）。

### 注释 7：原第 396 行

等于 `IFX_CAT1_CLOCK_BLOCK_PERIPHERAL0_16_BIT`。

### 注释 8：原第 399 行

等于 `IFX_CAT1_CLOCK_BLOCK_PERIPHERAL0_16_5_BIT`。

### 注释 9：原第 402 行

等于 `IFX_CAT1_CLOCK_BLOCK_PERIPHERAL0_24_5_BIT`。

### 注释 10：原第 724 行

条件编译（Conditional Compilation）：`!CONFIG_SOC_FAMILY_INFINEON_EDGE && !CONFIG_SOC_FAMILY_INFINEON_CAT1B`。

### 注释 11：原第 744 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_IFX_CAT1_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx__cat1_8h.html)
- [ifx_cat1_clock_block](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gab62704a8cdfda5914cfb7dfe81afa8c0)
- [ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)
- [block](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#ae8032f282998a9d9a31c5d967f384a4e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [channel](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#ac02e464103810c9907c16194eba88979)
- [instance](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#a4361f9f52e5621aedc0b4f2e0e011896)
- [group](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#a0e1e36ab2abe21b227f8b76d195fc627)
- [reserved](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#af59f4aff030f57cffc4a44d761f18d66)
- [funcs](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#a95619b170032a2b9b111d2f59602fbe7)
- [ifx_cat1_resource_inst](../device_power_control_model_reference/P018_ifx_cat1_resource_inst_结构体.md)
- [type](../device_power_control_model_reference/P018_ifx_cat1_resource_inst_结构体.md#a711df9cb83f6d7545b939fd56a7e10e7)
- [block_num](../device_power_control_model_reference/P018_ifx_cat1_resource_inst_结构体.md#a50f1d0589e90b071ddc451efcbb56892)
- [channel_num](../device_power_control_model_reference/P018_ifx_cat1_resource_inst_结构体.md#ad71f2ec8d25fa0792e287b1e0a58ca3f)
- [ifx_cat1_clock_control_get_frequency](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga04bb0312c12347d0ceac9fc033993221)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ifx_cat1_utils_peri_pclk_get_frequency](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga0421e7b519bd9b829baa8a2e7b234931)
- [ifx_cat1_utils_peri_pclk_enable_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gadda478f75d4546b4de8d978e56dba1fa)
- [ifx_cat1_utils_peri_pclk_disable_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga6bfb0915441740364a239ca3a68d6d8b)
- [ifx_cat1_utils_peri_is_fract_div](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gacacef8eba03b64537cbd0f09c3425089)
- [ifx_cat1_utils_peri_pclk_set_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga933b6bafae3eef87ac8e0a4ae7a849d4)
- [ifx_cat1_utils_peri_pclk_set_frac_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga1dba84b96bf16b98d672369a4bbe58c8)
- [ifx_cat1_utils_peri_pclk_get_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gafe5b77c891a50a08f364fa4d85af29ac)
- [ifx_cat1_utils_peri_pclk_get_frac_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga1b13def736a7046ee628830ab686ef3a)
- [ifx_cat1_utils_peri_pclk_assign_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga9ffa2a2c7427ea6049d7790f725ec185)
- [ifx_cat1_utils_peri_pclk_get_hfclk](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gaf8c74267c99cdebf0ae977555336f65c)
- [CLK_HF0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga7585bc918f0435fcea3de69f5d2368c2)
- [CLK_HF1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gab9ed6e703b1b98d5a713a8ec4cfbab79)
- [CLK_HF5](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga5516442b0c25b62024b765545fa2b18f)
- [CLK_HF6](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gad55fafafdec37c322f2faf036e955dcf)
- [CLK_HF7](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gadf9e87e3582b2042993c3237afe20383)
- [CLK_HF9](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga4b7e7866dd86214ce5910c2d01dcf49c)
- [CLK_HF10](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga726332ad1db3729a208a2be1458478ec)
- [CLK_HF11](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gaf1b81772f3de1dfcd08b5eaf96b60b33)
- [CLK_HF13](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga4c10fa4f6073001fde1fd49fe3769181)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [CLK_HF2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gab111d1af9166ca01d139b3e0512a811b)
- [CLK_HF3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga5deb0165e6f3e18acd4d3b841f96c50b)
- [CLK_HF4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga16cf7a3976d594e17bdcb595d024a6f7)
- [ifx_cat1_clock::group](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#a0e1e36ab2abe21b227f8b76d195fc627)
- [ifx_cat1_clock::instance](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#a4361f9f52e5621aedc0b4f2e0e011896)
- [ifx_cat1_clock::funcs](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#a95619b170032a2b9b111d2f59602fbe7)
- [ifx_cat1_clock::channel](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#ac02e464103810c9907c16194eba88979)
- [ifx_cat1_clock::block](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#ae8032f282998a9d9a31c5d967f384a4e)
- [ifx_cat1_clock::reserved](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md#af59f4aff030f57cffc4a44d761f18d66)
- [ifx_cat1_resource_inst::block_num](../device_power_control_model_reference/P018_ifx_cat1_resource_inst_结构体.md#a50f1d0589e90b071ddc451efcbb56892)
- [ifx_cat1_resource_inst::type](../device_power_control_model_reference/P018_ifx_cat1_resource_inst_结构体.md#a711df9cb83f6d7545b939fd56a7e10e7)
- [ifx_cat1_resource_inst::channel_num](../device_power_control_model_reference/P018_ifx_cat1_resource_inst_结构体.md#ad71f2ec8d25fa0792e287b1e0a58ca3f)

---

[上一章](P001_ch32v20x_30x-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_cr.h_源码浏览.md)
