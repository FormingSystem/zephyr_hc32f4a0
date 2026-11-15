---
id: learning.zephyr-docs.api-source-reference.page-714
title: renesas_rza2m_dma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza2m__dma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第714章\_renesas\_rza2m\_dma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza2m__dma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza2m__dma_8h.html)。

## 714.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00084"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00095"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00098"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="foldopen00114"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00120"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00127"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="foldopen00140"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="foldopen00147"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="foldopen00153"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="foldopen00156"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="foldopen00159"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="foldopen00163"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="foldopen00166"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="foldopen00169"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="foldopen00176"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="foldopen00179"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="foldopen00182"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="foldopen00185"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="foldopen00188"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="foldopen00191"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="foldopen00197"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="foldopen00200"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="foldopen00203"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="foldopen00207"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="foldopen00210"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="foldopen00213"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="foldopen00216"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="foldopen00219"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="foldopen00222"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="foldopen00225"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="foldopen00228"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="foldopen00231"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="foldopen00234"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="foldopen00238"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="foldopen00241"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="foldopen00244"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="foldopen00247"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="foldopen00250"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="foldopen00253"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="foldopen00256"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="foldopen00259"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="foldopen00262"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="foldopen00265"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="foldopen00269"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="foldopen00272"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="foldopen00275"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="foldopen00281"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="foldopen00284"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="foldopen00287"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="foldopen00290"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="foldopen00293"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="foldopen00296"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="foldopen00300"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="foldopen00303"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="foldopen00306"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="foldopen00309"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="foldopen00312"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="foldopen00315"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="foldopen00318"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="foldopen00321"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="foldopen00324"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="foldopen00327"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="foldopen00331"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="foldopen00334"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="foldopen00337"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="foldopen00340"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="foldopen00343"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="foldopen00346"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="foldopen00349"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="foldopen00352"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="foldopen00355"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="foldopen00358"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="foldopen00362"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="foldopen00365"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="foldopen00368"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="foldopen00371"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="foldopen00374"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="foldopen00377"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="foldopen00380"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="foldopen00383"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="foldopen00386"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="foldopen00389"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="foldopen00393"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="foldopen00396"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="foldopen00399"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="foldopen00402"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="foldopen00405"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="foldopen00408"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="foldopen00411"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="foldopen00414"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="foldopen00417"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="foldopen00420"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="foldopen00424"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="foldopen00427"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="foldopen00430"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="foldopen00434"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="foldopen00437"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="foldopen00440"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="foldopen00443"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="foldopen00446"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="foldopen00449"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="foldopen00452"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="foldopen00455"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="foldopen00459"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="foldopen00462"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="foldopen00466"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="foldopen00469"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="foldopen00472"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="foldopen00475"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="foldopen00478"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="foldopen00481"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="foldopen00484"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="foldopen00487"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="foldopen00491"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="foldopen00494"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="foldopen00497"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="foldopen00500"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="foldopen00503"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="foldopen00506"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="foldopen00509"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="foldopen00512"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="foldopen00515"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="foldopen00518"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="foldopen00522"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="foldopen00525"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="foldopen00528"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="foldopen00531"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="foldopen00534"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="foldopen00537"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="foldopen00540"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="foldopen00543"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="foldopen00546"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="foldopen00549"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="foldopen00553"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="foldopen00556"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="foldopen00559"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="foldopen00562"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="foldopen00565"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="foldopen00568"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="foldopen00572"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="foldopen00575"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="foldopen00578"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="foldopen00581"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="foldopen00585"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="foldopen00589"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="foldopen00592"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="foldopen00595"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="foldopen00598"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="foldopen00601"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="foldopen00604"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="foldopen00607"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="foldopen00610"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="foldopen00613"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="foldopen00616"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="foldopen00619"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="foldopen00622"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="foldopen00629"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RENESAS_RZA2M_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RENESAS_RZA2M_H_


#define RZA2M_DMA_F_LVL_EDGE  0x0U
#define RZA2M_DMA_F_LVL_LEVEL 0x10000U
#define RZA2M_DMA_F_AM_NONE   0x0U
#define RZA2M_DMA_F_AM_LEVEL  0x20000U
#define RZA2M_DMA_F_AM_BUS    0x40000U
#define RZA2M_DMA_F_AM_NO_ACK 0x80000U
#define RZA2M_DMA_F_REQD_AUTO 0x0U
#define RZA2M_DMA_F_REQD_SRC  0x100000U
#define RZA2M_DMA_F_REQD_DST  0x200000U



#define RZA2M_DMA_RS(dmars, lvl, am, reqd) (((dmars) & 0xFFFFU) | (lvl) | (am) | (reqd))

#define RZA2M_DMA_MEM_2_MEM 0x0U

#define RZA2M_DMA_RS_OSTM0TINT                                                                     \
        RZA2M_DMA_RS(0x023U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_OSTM1TINT                                                                     \
        RZA2M_DMA_RS(0x027U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_OSTM2TINT                                                                     \
        RZA2M_DMA_RS(0x02BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIA_0                                                                        \
        RZA2M_DMA_RS(0x043U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIB_0                                                                        \
        RZA2M_DMA_RS(0x047U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIC_0                                                                        \
        RZA2M_DMA_RS(0x04BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGID_0                                                                        \
        RZA2M_DMA_RS(0x04FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIA_1                                                                        \
        RZA2M_DMA_RS(0x053U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIB_1                                                                        \
        RZA2M_DMA_RS(0x057U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIA_2                                                                        \
        RZA2M_DMA_RS(0x05BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIB_2                                                                        \
        RZA2M_DMA_RS(0x05FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIA_3                                                                        \
        RZA2M_DMA_RS(0x063U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIB_3                                                                        \
        RZA2M_DMA_RS(0x067U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIC_3                                                                        \
        RZA2M_DMA_RS(0x06BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGID_3                                                                        \
        RZA2M_DMA_RS(0x06FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIA_4                                                                        \
        RZA2M_DMA_RS(0x073U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIB_4                                                                        \
        RZA2M_DMA_RS(0x077U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIC_4                                                                        \
        RZA2M_DMA_RS(0x07BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGID_4                                                                        \
        RZA2M_DMA_RS(0x07FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TCIV_4                                                                        \
        RZA2M_DMA_RS(0x083U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIU_5                                                                        \
        RZA2M_DMA_RS(0x087U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIV_5                                                                        \
        RZA2M_DMA_RS(0x08BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIW_5                                                                        \
        RZA2M_DMA_RS(0x08FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIA_6                                                                        \
        RZA2M_DMA_RS(0x093U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIB_6                                                                        \
        RZA2M_DMA_RS(0x097U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIC_6                                                                        \
        RZA2M_DMA_RS(0x09BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGID_6                                                                        \
        RZA2M_DMA_RS(0x09FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIA_7                                                                        \
        RZA2M_DMA_RS(0x0A3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIB_7                                                                        \
        RZA2M_DMA_RS(0x0A7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIC_7                                                                        \
        RZA2M_DMA_RS(0x0ABU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGID_7                                                                        \
        RZA2M_DMA_RS(0x0AFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TCIV_7                                                                        \
        RZA2M_DMA_RS(0x0B3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIA_8                                                                        \
        RZA2M_DMA_RS(0x0B7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIB_8                                                                        \
        RZA2M_DMA_RS(0x0BBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGIC_8                                                                        \
        RZA2M_DMA_RS(0x0BFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TGID_8                                                                        \
        RZA2M_DMA_RS(0x0C3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPA_0                                                                       \
        RZA2M_DMA_RS(0x0C7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPB_0                                                                       \
        RZA2M_DMA_RS(0x0CBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPC_0                                                                        \
        RZA2M_DMA_RS(0x0CFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPD_0                                                                        \
        RZA2M_DMA_RS(0x0D3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPE_0                                                                        \
        RZA2M_DMA_RS(0x0E3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPF_0                                                                        \
        RZA2M_DMA_RS(0x0E7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGA_0                                                                      \
        RZA2M_DMA_RS(0x0EBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGB_0                                                                      \
        RZA2M_DMA_RS(0x0EFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_OVF_0                                                                         \
        RZA2M_DMA_RS(0x0F3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_UNF_0                                                                         \
        RZA2M_DMA_RS(0x0F7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPA_1                                                                       \
        RZA2M_DMA_RS(0x0FBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPB_1                                                                       \
        RZA2M_DMA_RS(0x0FFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPC_1                                                                        \
        RZA2M_DMA_RS(0x103U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPD_1                                                                        \
        RZA2M_DMA_RS(0x107U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPE_1                                                                        \
        RZA2M_DMA_RS(0x117U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPF_1                                                                        \
        RZA2M_DMA_RS(0x11BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGA_1                                                                      \
        RZA2M_DMA_RS(0x11FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGB_1                                                                      \
        RZA2M_DMA_RS(0x123U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_OVF_1                                                                         \
        RZA2M_DMA_RS(0x127U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_UNF_1                                                                         \
        RZA2M_DMA_RS(0x12BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPA_2                                                                       \
        RZA2M_DMA_RS(0x12FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPB_2                                                                       \
        RZA2M_DMA_RS(0x133U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPC_2                                                                        \
        RZA2M_DMA_RS(0x137U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPD_2                                                                        \
        RZA2M_DMA_RS(0x13BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPE_2                                                                        \
        RZA2M_DMA_RS(0x14BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPF_2                                                                        \
        RZA2M_DMA_RS(0x14FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGA_2                                                                      \
        RZA2M_DMA_RS(0x153U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGB_2                                                                      \
        RZA2M_DMA_RS(0x157U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_OVF_2                                                                         \
        RZA2M_DMA_RS(0x15BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_UNF_2                                                                         \
        RZA2M_DMA_RS(0x15FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPA_3                                                                       \
        RZA2M_DMA_RS(0x163U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPB_3                                                                       \
        RZA2M_DMA_RS(0x167U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPC_3                                                                        \
        RZA2M_DMA_RS(0x16BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPD_3                                                                        \
        RZA2M_DMA_RS(0x16FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPE_3                                                                        \
        RZA2M_DMA_RS(0x17FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPF_3                                                                        \
        RZA2M_DMA_RS(0x183U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGA_3                                                                      \
        RZA2M_DMA_RS(0x187U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGB_3                                                                      \
        RZA2M_DMA_RS(0x18BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_OVF_3                                                                         \
        RZA2M_DMA_RS(0x18FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_UNF_3                                                                         \
        RZA2M_DMA_RS(0x193U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPA_4                                                                       \
        RZA2M_DMA_RS(0x197U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPB_4                                                                       \
        RZA2M_DMA_RS(0x19BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPC_4                                                                        \
        RZA2M_DMA_RS(0x19FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPD_4                                                                        \
        RZA2M_DMA_RS(0x1A3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPE_4                                                                        \
        RZA2M_DMA_RS(0x1B3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPF_4                                                                        \
        RZA2M_DMA_RS(0x1B7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGA_4                                                                      \
        RZA2M_DMA_RS(0x1BBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGB_4                                                                      \
        RZA2M_DMA_RS(0x1BFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_OVF_4                                                                         \
        RZA2M_DMA_RS(0x1C3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_UNF_4                                                                         \
        RZA2M_DMA_RS(0x1C7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPA_5                                                                       \
        RZA2M_DMA_RS(0x1CBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPB_5                                                                       \
        RZA2M_DMA_RS(0x1CFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPC_5                                                                        \
        RZA2M_DMA_RS(0x1D3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPD_5                                                                        \
        RZA2M_DMA_RS(0x1D7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPE_5                                                                        \
        RZA2M_DMA_RS(0x1E7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPF_5                                                                        \
        RZA2M_DMA_RS(0x1EBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGA_5                                                                      \
        RZA2M_DMA_RS(0x1EFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGB_5                                                                      \
        RZA2M_DMA_RS(0x1F3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_OVF_5                                                                         \
        RZA2M_DMA_RS(0x1F7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_UNF_5                                                                         \
        RZA2M_DMA_RS(0x1FBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPA_6                                                                       \
        RZA2M_DMA_RS(0x1FFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPB_6                                                                       \
        RZA2M_DMA_RS(0x203U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPC_6                                                                        \
        RZA2M_DMA_RS(0x207U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPD_6                                                                        \
        RZA2M_DMA_RS(0x20BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPE_6                                                                        \
        RZA2M_DMA_RS(0x21BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPF_6                                                                        \
        RZA2M_DMA_RS(0x21FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGA_6                                                                      \
        RZA2M_DMA_RS(0x223U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGB_6                                                                      \
        RZA2M_DMA_RS(0x227U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_OVF_6                                                                         \
        RZA2M_DMA_RS(0x22BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_UNF_6                                                                         \
        RZA2M_DMA_RS(0x22FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPA_7                                                                       \
        RZA2M_DMA_RS(0x233U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CCMPB_7                                                                       \
        RZA2M_DMA_RS(0x237U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPC_7                                                                        \
        RZA2M_DMA_RS(0x23BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPD_7                                                                        \
        RZA2M_DMA_RS(0x23FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPE_7                                                                        \
        RZA2M_DMA_RS(0x24FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_CMPF_7                                                                        \
        RZA2M_DMA_RS(0x253U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGA_7                                                                      \
        RZA2M_DMA_RS(0x257U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_ADTRGB_7                                                                      \
        RZA2M_DMA_RS(0x25BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_OVF_7                                                                         \
        RZA2M_DMA_RS(0x25FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_UNF_7                                                                         \
        RZA2M_DMA_RS(0x263U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_S12ADI_0                                                                      \
        RZA2M_DMA_RS(0x267U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_S12GBADI_0                                                                    \
        RZA2M_DMA_RS(0x26BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_S12GCADI_0                                                                    \
        RZA2M_DMA_RS(0x26FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_0                                                             \
        RZA2M_DMA_RS(0x272U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_0                                                             \
        RZA2M_DMA_RS(0x271U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_1                                                             \
        RZA2M_DMA_RS(0x276U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_1                                                             \
        RZA2M_DMA_RS(0x275U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_2                                                             \
        RZA2M_DMA_RS(0x27BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_2                                                             \
        RZA2M_DMA_RS(0x27BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_3                                                             \
        RZA2M_DMA_RS(0x27EU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_3                                                             \
        RZA2M_DMA_RS(0x27DU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_SPDIFTXI                                                                      \
        RZA2M_DMA_RS(0x283U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_SPDIFRXI                                                                      \
        RZA2M_DMA_RS(0x287U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_INTRIIC_RI0                                                                   \
        RZA2M_DMA_RS(0x28AU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_INTRIIC_TI0                                                                   \
        RZA2M_DMA_RS(0x289U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_INTRIIC_RI1                                                                   \
        RZA2M_DMA_RS(0x28EU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_INTRIIC_TI1                                                                   \
        RZA2M_DMA_RS(0x28DU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_INTRIIC_RI2                                                                   \
        RZA2M_DMA_RS(0x292U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_INTRIIC_TI2                                                                   \
        RZA2M_DMA_RS(0x291U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_INTRIIC_RI3                                                                   \
        RZA2M_DMA_RS(0x296U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_INTRIIC_TI3                                                                   \
        RZA2M_DMA_RS(0x295U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_RXI0                                                                          \
        RZA2M_DMA_RS(0x29AU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_TXI0                                                                          \
        RZA2M_DMA_RS(0x299U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_RXI1                                                                          \
        RZA2M_DMA_RS(0x29EU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_TXI1                                                                          \
        RZA2M_DMA_RS(0x29DU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_RXI2                                                                          \
        RZA2M_DMA_RS(0x2A2U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_TXI2                                                                          \
        RZA2M_DMA_RS(0x2A1U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_RXI3                                                                          \
        RZA2M_DMA_RS(0x2A6U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_TXI3                                                                          \
        RZA2M_DMA_RS(0x2A5U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_RXI4                                                                          \
        RZA2M_DMA_RS(0x2AAU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_TXI4                                                                          \
        RZA2M_DMA_RS(0x2A9U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_RXF_DMA0                                                                      \
        RZA2M_DMA_RS(0x2AFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_RXF_DMA1                                                                      \
        RZA2M_DMA_RS(0x2B3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_RXF_DMA2                                                                      \
        RZA2M_DMA_RS(0x2B7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_RXF_DMA3                                                                      \
        RZA2M_DMA_RS(0x2BBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_RXF_DMA4                                                                      \
        RZA2M_DMA_RS(0x2BFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_RXF_DMA5                                                                      \
        RZA2M_DMA_RS(0x2C3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_RXF_DMA6                                                                      \
        RZA2M_DMA_RS(0x2C7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_RXF_DMA7                                                                      \
        RZA2M_DMA_RS(0x2CBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_COM_DMA0                                                                      \
        RZA2M_DMA_RS(0x2CFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_COM_DMA1                                                                      \
        RZA2M_DMA_RS(0x2D3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_SPRI0                                                                         \
        RZA2M_DMA_RS(0x2D6U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_SPTI0                                                                         \
        RZA2M_DMA_RS(0x2D5U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_SPRI1                                                                         \
        RZA2M_DMA_RS(0x2DAU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_SPTI1                                                                         \
        RZA2M_DMA_RS(0x2D9U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_SPRI2                                                                         \
        RZA2M_DMA_RS(0x2DEU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_SPTI2                                                                         \
        RZA2M_DMA_RS(0x2DDU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_SCI_RXI0                                                                      \
        RZA2M_DMA_RS(0x2E2U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_SCI_TXI0                                                                      \
        RZA2M_DMA_RS(0x2E1U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_SCI_RXI1                                                                      \
        RZA2M_DMA_RS(0x2E6U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_SCI_TXI1                                                                      \
        RZA2M_DMA_RS(0x2E5U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_IPLS                                                                          \
        RZA2M_DMA_RS(0x2EBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)

#define RZA2M_DMA_RS_TILE_0_PAFI                                                                   \
        RZA2M_DMA_RS(0x3CEU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_TILE_0_PAEI                                                                   \
        RZA2M_DMA_RS(0x3CDU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_TILE_1_PAFI                                                                   \
        RZA2M_DMA_RS(0x3D2U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_TILE_1_PAEI                                                                   \
        RZA2M_DMA_RS(0x3D1U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_TILE_2_PAFI                                                                   \
        RZA2M_DMA_RS(0x3D6U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_TILE_2_PAEI                                                                   \
        RZA2M_DMA_RS(0x3D5U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_TILE_3_PAFI                                                                   \
        RZA2M_DMA_RS(0x3DAU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_TILE_3_PAEI                                                                   \
        RZA2M_DMA_RS(0x3D9U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_TILE_4_PAFI                                                                   \
        RZA2M_DMA_RS(0x3DEU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_TILE_4_PAEI                                                                   \
        RZA2M_DMA_RS(0x3DDU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_RS_TILE_5_PAFI                                                                   \
        RZA2M_DMA_RS(0x3E2U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)

#define RZA2M_DMA_RS_TILE_5_PAEI                                                                   \
        RZA2M_DMA_RS(0x3E1U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)

#define RZA2M_DMA_DMARS_EXT_DREQ0 0x003U

#define RZA2M_DMA_RS_DREQ0                                                                         \
        RZA2M_DMA_RS(RZA2M_DMA_DMARS_EXT_DREQ0, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_NONE,         \
                     RZA2M_DMA_F_REQD_AUTO)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RENESAS_RZA2M_H_ */
```

## 714.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 633 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_RENESAS_RZA2M_H_`。

## 714.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza2m__dma_8h.html)

---

[上一章](P713_renesas_rz_cgc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P715_riscv_aia.h_源码浏览.md)
