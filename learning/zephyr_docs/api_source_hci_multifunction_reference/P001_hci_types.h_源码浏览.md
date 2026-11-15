---
id: learning.zephyr-docs.api-source-hci-multifunction-reference.page-1
title: hci_types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_hci\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)。

## 1.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
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
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
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
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
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
<a id="foldopen00099"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="foldopen00101"></a>
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
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="foldopen00126"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
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
<a id="foldopen00216"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="foldopen00219"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="foldopen00221"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="foldopen00223"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="foldopen00225"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="foldopen00227"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="foldopen00229"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="foldopen00231"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="foldopen00234"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="foldopen00236"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="foldopen00238"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="foldopen00240"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="foldopen00242"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="foldopen00244"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="foldopen00246"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="foldopen00248"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="foldopen00250"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="foldopen00252"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="foldopen00254"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="foldopen00256"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="foldopen00258"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="foldopen00260"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="foldopen00262"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="foldopen00264"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="foldopen00266"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="foldopen00268"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="foldopen00270"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="foldopen00272"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="foldopen00274"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="foldopen00276"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="foldopen00280"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="foldopen00282"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="foldopen00284"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="foldopen00286"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="foldopen00290"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="foldopen00292"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="foldopen00294"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="foldopen00296"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="foldopen00298"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="foldopen00300"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="foldopen00303"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="foldopen00305"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="foldopen00307"></a>
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
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="foldopen00360"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="foldopen00366"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="foldopen00369"></a>
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
<a id="foldopen00400"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="foldopen00409"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="foldopen00419"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="foldopen00425"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="foldopen00428"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="foldopen00434"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
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
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="foldopen00464"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="foldopen00466"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="foldopen00468"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="foldopen00471"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="foldopen00474"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="foldopen00476"></a>
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
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="foldopen00496"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="foldopen00507"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="foldopen00518"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="foldopen00524"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="foldopen00530"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="foldopen00535"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="foldopen00540"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
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
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00555"></a>
<a id="foldopen00557"></a>
<a id="l00557"></a>
<a id="l00559"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00571"></a>
<a id="l00573"></a>
<a id="l00575"></a>
<a id="l00577"></a>
<a id="l00579"></a>
<a id="l00581"></a>
<a id="l00583"></a>
<a id="l00585"></a>
<a id="l00587"></a>
<a id="l00589"></a>
<a id="l00591"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="foldopen00596"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="foldopen00602"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="foldopen00607"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="foldopen00613"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="foldopen00621"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="foldopen00624"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="foldopen00630"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="foldopen00635"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="foldopen00641"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="foldopen00646"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="foldopen00655"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="foldopen00658"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="foldopen00664"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="foldopen00670"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="foldopen00675"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="foldopen00681"></a>
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
<a id="foldopen00691"></a>
<a id="l00691"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="foldopen00694"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="foldopen00701"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="foldopen00707"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="foldopen00713"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="foldopen00718"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="foldopen00727"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00732"></a>
<a id="foldopen00734"></a>
<a id="l00734"></a>
<a id="l00736"></a>
<a id="l00738"></a>
<a id="l00740"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="foldopen00746"></a>
<a id="l00746"></a>
<a id="l00748"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="foldopen00754"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="foldopen00761"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="foldopen00766"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="foldopen00772"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="foldopen00776"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00788"></a>
<a id="foldopen00790"></a>
<a id="l00790"></a>
<a id="l00792"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00798"></a>
<a id="foldopen00800"></a>
<a id="l00800"></a>
<a id="l00802"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="foldopen00808"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="foldopen00814"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="foldopen00821"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="foldopen00826"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="foldopen00837"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="foldopen00842"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00846"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00852"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="foldopen00855"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="l00857"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="foldopen00862"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00869"></a>
<a id="l00870"></a>
<a id="foldopen00871"></a>
<a id="l00871"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="foldopen00881"></a>
<a id="l00881"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="foldopen00886"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00888"></a>
<a id="l00889"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="foldopen00893"></a>
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
<a id="foldopen00903"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="foldopen00915"></a>
<a id="l00915"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="foldopen00920"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="foldopen00927"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="foldopen00933"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00939"></a>
<a id="foldopen00941"></a>
<a id="l00941"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="foldopen00946"></a>
<a id="l00946"></a>
<a id="l00948"></a>
<a id="l00950"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00956"></a>
<a id="foldopen00958"></a>
<a id="l00958"></a>
<a id="l00960"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="foldopen00966"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="foldopen00970"></a>
<a id="l00970"></a>
<a id="l00971"></a>
<a id="l00972"></a>
<a id="l00973"></a>
<a id="l00974"></a>
<a id="l00976"></a>
<a id="foldopen00978"></a>
<a id="l00978"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="foldopen00984"></a>
<a id="l00984"></a>
<a id="l00985"></a>
<a id="l00986"></a>
<a id="l00987"></a>
<a id="l00989"></a>
<a id="foldopen00991"></a>
<a id="l00991"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="l00997"></a>
<a id="l00999"></a>
<a id="foldopen01001"></a>
<a id="l01001"></a>
<a id="l01003"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="foldopen01009"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="foldopen01014"></a>
<a id="l01014"></a>
<a id="l01015"></a>
<a id="l01016"></a>
<a id="l01017"></a>
<a id="l01018"></a>
<a id="foldopen01019"></a>
<a id="l01019"></a>
<a id="l01020"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="foldopen01025"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="foldopen01030"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01032"></a>
<a id="l01033"></a>
<a id="foldopen01034"></a>
<a id="l01034"></a>
<a id="l01035"></a>
<a id="l01036"></a>
<a id="l01037"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="l01040"></a>
<a id="foldopen01041"></a>
<a id="l01041"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="foldopen01046"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01051"></a>
<a id="foldopen01052"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01054"></a>
<a id="l01055"></a>
<a id="l01056"></a>
<a id="l01057"></a>
<a id="l01058"></a>
<a id="foldopen01059"></a>
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
<a id="l01074"></a>
<a id="l01075"></a>
<a id="l01076"></a>
<a id="l01077"></a>
<a id="l01078"></a>
<a id="l01079"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01082"></a>
<a id="l01083"></a>
<a id="foldopen01084"></a>
<a id="l01084"></a>
<a id="l01085"></a>
<a id="l01086"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01089"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="l01093"></a>
<a id="foldopen01094"></a>
<a id="l01094"></a>
<a id="l01095"></a>
<a id="l01096"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01099"></a>
<a id="foldopen01100"></a>
<a id="l01100"></a>
<a id="l01101"></a>
<a id="l01102"></a>
<a id="foldopen01103"></a>
<a id="l01103"></a>
<a id="l01104"></a>
<a id="l01105"></a>
<a id="l01106"></a>
<a id="l01107"></a>
<a id="l01108"></a>
<a id="l01109"></a>
<a id="l01110"></a>
<a id="foldopen01111"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01113"></a>
<a id="l01114"></a>
<a id="l01115"></a>
<a id="l01116"></a>
<a id="foldopen01117"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01119"></a>
<a id="l01120"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="foldopen01126"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="l01134"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01142"></a>
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
<a id="l01158"></a>
<a id="l01159"></a>
<a id="l01160"></a>
<a id="l01161"></a>
<a id="l01162"></a>
<a id="l01163"></a>
<a id="l01164"></a>
<a id="foldopen01165"></a>
<a id="l01165"></a>
<a id="l01166"></a>
<a id="l01167"></a>
<a id="foldopen01168"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01170"></a>
<a id="l01171"></a>
<a id="foldopen01172"></a>
<a id="l01172"></a>
<a id="l01173"></a>
<a id="l01174"></a>
<a id="l01175"></a>
<a id="foldopen01176"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01179"></a>
<a id="foldopen01180"></a>
<a id="l01180"></a>
<a id="l01181"></a>
<a id="l01182"></a>
<a id="l01183"></a>
<a id="l01184"></a>
<a id="l01185"></a>
<a id="l01186"></a>
<a id="foldopen01187"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="foldopen01191"></a>
<a id="l01191"></a>
<a id="l01192"></a>
<a id="l01193"></a>
<a id="l01194"></a>
<a id="foldopen01195"></a>
<a id="l01195"></a>
<a id="l01196"></a>
<a id="l01197"></a>
<a id="l01198"></a>
<a id="l01199"></a>
<a id="foldopen01200"></a>
<a id="l01200"></a>
<a id="l01201"></a>
<a id="l01202"></a>
<a id="l01203"></a>
<a id="foldopen01204"></a>
<a id="l01204"></a>
<a id="l01205"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="l01208"></a>
<a id="l01209"></a>
<a id="foldopen01210"></a>
<a id="l01210"></a>
<a id="l01211"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01215"></a>
<a id="l01216"></a>
<a id="foldopen01217"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01221"></a>
<a id="foldopen01222"></a>
<a id="l01222"></a>
<a id="l01223"></a>
<a id="l01224"></a>
<a id="l01225"></a>
<a id="foldopen01226"></a>
<a id="l01226"></a>
<a id="l01227"></a>
<a id="l01228"></a>
<a id="l01229"></a>
<a id="l01230"></a>
<a id="l01231"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="foldopen01234"></a>
<a id="l01234"></a>
<a id="l01235"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="l01238"></a>
<a id="l01239"></a>
<a id="l01240"></a>
<a id="foldopen01241"></a>
<a id="l01241"></a>
<a id="l01242"></a>
<a id="l01243"></a>
<a id="l01244"></a>
<a id="l01245"></a>
<a id="l01246"></a>
<a id="l01247"></a>
<a id="foldopen01248"></a>
<a id="l01248"></a>
<a id="l01249"></a>
<a id="l01250"></a>
<a id="foldopen01251"></a>
<a id="l01251"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01258"></a>
<a id="l01259"></a>
<a id="l01260"></a>
<a id="foldopen01261"></a>
<a id="l01261"></a>
<a id="l01262"></a>
<a id="l01263"></a>
<a id="foldopen01264"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="l01266"></a>
<a id="l01267"></a>
<a id="l01268"></a>
<a id="l01269"></a>
<a id="l01270"></a>
<a id="l01271"></a>
<a id="l01272"></a>
<a id="foldopen01273"></a>
<a id="l01273"></a>
<a id="l01274"></a>
<a id="l01275"></a>
<a id="l01276"></a>
<a id="l01277"></a>
<a id="foldopen01278"></a>
<a id="l01278"></a>
<a id="l01279"></a>
<a id="l01280"></a>
<a id="l01281"></a>
<a id="l01282"></a>
<a id="l01283"></a>
<a id="l01284"></a>
<a id="foldopen01285"></a>
<a id="l01285"></a>
<a id="l01286"></a>
<a id="l01287"></a>
<a id="l01288"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="foldopen01291"></a>
<a id="l01291"></a>
<a id="l01292"></a>
<a id="l01293"></a>
<a id="l01294"></a>
<a id="l01295"></a>
<a id="l01296"></a>
<a id="l01297"></a>
<a id="l01298"></a>
<a id="l01299"></a>
<a id="l01300"></a>
<a id="l01301"></a>
<a id="l01302"></a>
<a id="l01303"></a>
<a id="l01305"></a>
<a id="l01306"></a>
<a id="l01307"></a>
<a id="l01308"></a>
<a id="l01309"></a>
<a id="l01310"></a>
<a id="l01311"></a>
<a id="l01312"></a>
<a id="l01313"></a>
<a id="l01314"></a>
<a id="l01315"></a>
<a id="l01316"></a>
<a id="l01317"></a>
<a id="l01318"></a>
<a id="foldopen01319"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01322"></a>
<a id="l01323"></a>
<a id="l01324"></a>
<a id="l01325"></a>
<a id="l01326"></a>
<a id="l01327"></a>
<a id="l01328"></a>
<a id="l01329"></a>
<a id="foldopen01330"></a>
<a id="l01330"></a>
<a id="l01331"></a>
<a id="l01332"></a>
<a id="l01333"></a>
<a id="l01334"></a>
<a id="l01335"></a>
<a id="foldopen01336"></a>
<a id="l01336"></a>
<a id="l01337"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01340"></a>
<a id="l01341"></a>
<a id="foldopen01342"></a>
<a id="l01342"></a>
<a id="l01343"></a>
<a id="l01344"></a>
<a id="l01345"></a>
<a id="l01346"></a>
<a id="l01347"></a>
<a id="l01348"></a>
<a id="l01349"></a>
<a id="l01350"></a>
<a id="foldopen01351"></a>
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
<a id="l01361"></a>
<a id="l01362"></a>
<a id="l01363"></a>
<a id="l01364"></a>
<a id="foldopen01365"></a>
<a id="l01365"></a>
<a id="l01366"></a>
<a id="l01367"></a>
<a id="l01368"></a>
<a id="l01369"></a>
<a id="l01370"></a>
<a id="l01371"></a>
<a id="l01372"></a>
<a id="l01373"></a>
<a id="l01374"></a>
<a id="l01375"></a>
<a id="l01376"></a>
<a id="l01377"></a>
<a id="l01378"></a>
<a id="l01379"></a>
<a id="l01380"></a>
<a id="foldopen01381"></a>
<a id="l01381"></a>
<a id="l01382"></a>
<a id="l01383"></a>
<a id="l01384"></a>
<a id="l01385"></a>
<a id="l01386"></a>
<a id="l01387"></a>
<a id="l01388"></a>
<a id="l01389"></a>
<a id="l01390"></a>
<a id="foldopen01391"></a>
<a id="l01391"></a>
<a id="l01392"></a>
<a id="l01393"></a>
<a id="l01394"></a>
<a id="l01395"></a>
<a id="l01396"></a>
<a id="l01397"></a>
<a id="l01398"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01402"></a>
<a id="l01403"></a>
<a id="l01404"></a>
<a id="l01405"></a>
<a id="l01406"></a>
<a id="l01407"></a>
<a id="foldopen01408"></a>
<a id="l01408"></a>
<a id="l01409"></a>
<a id="l01410"></a>
<a id="l01411"></a>
<a id="l01412"></a>
<a id="l01413"></a>
<a id="l01414"></a>
<a id="l01415"></a>
<a id="foldopen01416"></a>
<a id="l01416"></a>
<a id="l01417"></a>
<a id="l01418"></a>
<a id="l01419"></a>
<a id="l01420"></a>
<a id="foldopen01421"></a>
<a id="l01421"></a>
<a id="l01422"></a>
<a id="l01423"></a>
<a id="l01424"></a>
<a id="l01425"></a>
<a id="foldopen01426"></a>
<a id="l01426"></a>
<a id="l01427"></a>
<a id="l01428"></a>
<a id="l01429"></a>
<a id="l01430"></a>
<a id="l01431"></a>
<a id="l01432"></a>
<a id="l01433"></a>
<a id="l01434"></a>
<a id="l01435"></a>
<a id="l01436"></a>
<a id="foldopen01437"></a>
<a id="l01437"></a>
<a id="l01438"></a>
<a id="l01439"></a>
<a id="l01440"></a>
<a id="l01441"></a>
<a id="foldopen01442"></a>
<a id="l01442"></a>
<a id="l01443"></a>
<a id="l01444"></a>
<a id="foldopen01445"></a>
<a id="l01445"></a>
<a id="l01446"></a>
<a id="l01447"></a>
<a id="l01448"></a>
<a id="l01449"></a>
<a id="l01450"></a>
<a id="l01451"></a>
<a id="foldopen01452"></a>
<a id="l01452"></a>
<a id="l01453"></a>
<a id="l01454"></a>
<a id="l01455"></a>
<a id="l01456"></a>
<a id="foldopen01457"></a>
<a id="l01457"></a>
<a id="l01458"></a>
<a id="l01459"></a>
<a id="l01460"></a>
<a id="foldopen01461"></a>
<a id="l01461"></a>
<a id="l01462"></a>
<a id="l01463"></a>
<a id="l01464"></a>
<a id="l01465"></a>
<a id="l01466"></a>
<a id="foldopen01467"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01469"></a>
<a id="l01470"></a>
<a id="l01471"></a>
<a id="l01472"></a>
<a id="foldopen01473"></a>
<a id="l01473"></a>
<a id="l01474"></a>
<a id="l01476"></a>
<a id="l01478"></a>
<a id="l01479"></a>
<a id="l01480"></a>
<a id="l01481"></a>
<a id="l01482"></a>
<a id="foldopen01483"></a>
<a id="l01483"></a>
<a id="l01484"></a>
<a id="l01485"></a>
<a id="l01486"></a>
<a id="foldopen01487"></a>
<a id="l01487"></a>
<a id="l01488"></a>
<a id="l01489"></a>
<a id="l01490"></a>
<a id="l01491"></a>
<a id="l01492"></a>
<a id="foldopen01493"></a>
<a id="l01493"></a>
<a id="l01494"></a>
<a id="l01495"></a>
<a id="foldopen01496"></a>
<a id="l01496"></a>
<a id="l01497"></a>
<a id="l01498"></a>
<a id="l01499"></a>
<a id="l01500"></a>
<a id="l01501"></a>
<a id="foldopen01502"></a>
<a id="l01502"></a>
<a id="l01503"></a>
<a id="l01504"></a>
<a id="l01505"></a>
<a id="l01506"></a>
<a id="l01507"></a>
<a id="foldopen01508"></a>
<a id="l01508"></a>
<a id="l01509"></a>
<a id="l01510"></a>
<a id="l01511"></a>
<a id="l01512"></a>
<a id="l01513"></a>
<a id="l01514"></a>
<a id="l01515"></a>
<a id="l01516"></a>
<a id="l01517"></a>
<a id="l01518"></a>
<a id="l01519"></a>
<a id="l01520"></a>
<a id="l01521"></a>
<a id="foldopen01522"></a>
<a id="l01522"></a>
<a id="l01523"></a>
<a id="l01524"></a>
<a id="l01525"></a>
<a id="l01526"></a>
<a id="l01527"></a>
<a id="l01528"></a>
<a id="foldopen01529"></a>
<a id="l01529"></a>
<a id="l01530"></a>
<a id="l01531"></a>
<a id="l01532"></a>
<a id="l01533"></a>
<a id="l01534"></a>
<a id="foldopen01535"></a>
<a id="l01535"></a>
<a id="l01536"></a>
<a id="l01537"></a>
<a id="l01538"></a>
<a id="l01539"></a>
<a id="l01540"></a>
<a id="l01541"></a>
<a id="l01542"></a>
<a id="l01543"></a>
<a id="foldopen01544"></a>
<a id="l01544"></a>
<a id="l01545"></a>
<a id="l01546"></a>
<a id="l01547"></a>
<a id="l01548"></a>
<a id="l01549"></a>
<a id="foldopen01550"></a>
<a id="l01550"></a>
<a id="l01551"></a>
<a id="l01552"></a>
<a id="l01553"></a>
<a id="foldopen01554"></a>
<a id="l01554"></a>
<a id="l01555"></a>
<a id="l01556"></a>
<a id="l01557"></a>
<a id="l01558"></a>
<a id="l01559"></a>
<a id="foldopen01560"></a>
<a id="l01560"></a>
<a id="l01561"></a>
<a id="l01562"></a>
<a id="l01563"></a>
<a id="l01564"></a>
<a id="foldopen01565"></a>
<a id="l01565"></a>
<a id="l01566"></a>
<a id="l01567"></a>
<a id="l01568"></a>
<a id="l01569"></a>
<a id="l01570"></a>
<a id="foldopen01571"></a>
<a id="l01571"></a>
<a id="l01572"></a>
<a id="l01573"></a>
<a id="l01574"></a>
<a id="l01575"></a>
<a id="l01576"></a>
<a id="l01577"></a>
<a id="foldopen01578"></a>
<a id="l01578"></a>
<a id="l01579"></a>
<a id="l01580"></a>
<a id="l01581"></a>
<a id="l01582"></a>
<a id="l01583"></a>
<a id="l01584"></a>
<a id="l01585"></a>
<a id="foldopen01586"></a>
<a id="l01586"></a>
<a id="l01587"></a>
<a id="l01588"></a>
<a id="l01589"></a>
<a id="l01590"></a>
<a id="l01591"></a>
<a id="l01592"></a>
<a id="l01593"></a>
<a id="l01594"></a>
<a id="l01595"></a>
<a id="foldopen01596"></a>
<a id="l01596"></a>
<a id="l01597"></a>
<a id="l01598"></a>
<a id="l01599"></a>
<a id="l01600"></a>
<a id="l01601"></a>
<a id="l01602"></a>
<a id="foldopen01603"></a>
<a id="l01603"></a>
<a id="l01604"></a>
<a id="l01605"></a>
<a id="l01606"></a>
<a id="l01607"></a>
<a id="l01608"></a>
<a id="l01609"></a>
<a id="foldopen01610"></a>
<a id="l01610"></a>
<a id="l01611"></a>
<a id="l01612"></a>
<a id="l01613"></a>
<a id="l01614"></a>
<a id="l01615"></a>
<a id="l01616"></a>
<a id="foldopen01617"></a>
<a id="l01617"></a>
<a id="l01618"></a>
<a id="l01619"></a>
<a id="l01620"></a>
<a id="l01621"></a>
<a id="l01622"></a>
<a id="foldopen01623"></a>
<a id="l01623"></a>
<a id="l01624"></a>
<a id="l01625"></a>
<a id="foldopen01626"></a>
<a id="l01626"></a>
<a id="l01627"></a>
<a id="l01628"></a>
<a id="l01629"></a>
<a id="l01630"></a>
<a id="l01631"></a>
<a id="foldopen01632"></a>
<a id="l01632"></a>
<a id="l01633"></a>
<a id="l01634"></a>
<a id="foldopen01635"></a>
<a id="l01635"></a>
<a id="l01636"></a>
<a id="l01637"></a>
<a id="l01638"></a>
<a id="l01639"></a>
<a id="l01640"></a>
<a id="l01641"></a>
<a id="l01642"></a>
<a id="l01643"></a>
<a id="foldopen01644"></a>
<a id="l01644"></a>
<a id="l01645"></a>
<a id="l01646"></a>
<a id="l01647"></a>
<a id="l01648"></a>
<a id="foldopen01649"></a>
<a id="l01649"></a>
<a id="l01650"></a>
<a id="l01651"></a>
<a id="l01652"></a>
<a id="l01653"></a>
<a id="l01654"></a>
<a id="l01655"></a>
<a id="l01656"></a>
<a id="l01657"></a>
<a id="l01658"></a>
<a id="l01659"></a>
<a id="l01660"></a>
<a id="l01661"></a>
<a id="l01662"></a>
<a id="l01663"></a>
<a id="l01664"></a>
<a id="foldopen01665"></a>
<a id="l01665"></a>
<a id="l01666"></a>
<a id="l01667"></a>
<a id="l01668"></a>
<a id="l01669"></a>
<a id="l01670"></a>
<a id="l01671"></a>
<a id="l01672"></a>
<a id="l01673"></a>
<a id="l01674"></a>
<a id="l01675"></a>
<a id="l01676"></a>
<a id="l01677"></a>
<a id="foldopen01678"></a>
<a id="l01678"></a>
<a id="l01679"></a>
<a id="l01680"></a>
<a id="foldopen01681"></a>
<a id="l01681"></a>
<a id="l01682"></a>
<a id="l01683"></a>
<a id="l01684"></a>
<a id="l01685"></a>
<a id="l01686"></a>
<a id="l01687"></a>
<a id="l01688"></a>
<a id="l01689"></a>
<a id="l01690"></a>
<a id="l01691"></a>
<a id="l01692"></a>
<a id="l01693"></a>
<a id="l01694"></a>
<a id="l01695"></a>
<a id="foldopen01696"></a>
<a id="l01696"></a>
<a id="l01697"></a>
<a id="l01698"></a>
<a id="l01699"></a>
<a id="l01700"></a>
<a id="l01701"></a>
<a id="l01702"></a>
<a id="l01703"></a>
<a id="l01704"></a>
<a id="l01705"></a>
<a id="l01706"></a>
<a id="foldopen01707"></a>
<a id="l01707"></a>
<a id="l01708"></a>
<a id="l01709"></a>
<a id="l01710"></a>
<a id="l01711"></a>
<a id="l01712"></a>
<a id="l01713"></a>
<a id="l01714"></a>
<a id="l01715"></a>
<a id="l01716"></a>
<a id="l01717"></a>
<a id="l01718"></a>
<a id="l01719"></a>
<a id="l01720"></a>
<a id="l01721"></a>
<a id="l01722"></a>
<a id="foldopen01723"></a>
<a id="l01723"></a>
<a id="l01724"></a>
<a id="l01725"></a>
<a id="l01726"></a>
<a id="l01727"></a>
<a id="l01728"></a>
<a id="l01729"></a>
<a id="l01730"></a>
<a id="l01731"></a>
<a id="l01732"></a>
<a id="l01733"></a>
<a id="l01734"></a>
<a id="foldopen01735"></a>
<a id="l01735"></a>
<a id="l01736"></a>
<a id="l01737"></a>
<a id="l01738"></a>
<a id="l01739"></a>
<a id="l01740"></a>
<a id="l01741"></a>
<a id="l01742"></a>
<a id="foldopen01743"></a>
<a id="l01743"></a>
<a id="l01744"></a>
<a id="l01745"></a>
<a id="l01746"></a>
<a id="l01747"></a>
<a id="l01748"></a>
<a id="l01749"></a>
<a id="l01750"></a>
<a id="l01751"></a>
<a id="l01752"></a>
<a id="l01753"></a>
<a id="l01754"></a>
<a id="l01755"></a>
<a id="l01756"></a>
<a id="l01757"></a>
<a id="l01758"></a>
<a id="l01759"></a>
<a id="l01760"></a>
<a id="l01761"></a>
<a id="l01763"></a>
<a id="l01765"></a>
<a id="l01767"></a>
<a id="l01768"></a>
<a id="l01769"></a>
<a id="l01770"></a>
<a id="l01771"></a>
<a id="l01772"></a>
<a id="l01773"></a>
<a id="foldopen01774"></a>
<a id="l01774"></a>
<a id="l01775"></a>
<a id="l01776"></a>
<a id="l01777"></a>
<a id="l01778"></a>
<a id="l01779"></a>
<a id="l01780"></a>
<a id="l01781"></a>
<a id="l01782"></a>
<a id="l01783"></a>
<a id="l01784"></a>
<a id="l01785"></a>
<a id="l01786"></a>
<a id="l01787"></a>
<a id="l01788"></a>
<a id="l01789"></a>
<a id="foldopen01790"></a>
<a id="l01790"></a>
<a id="l01791"></a>
<a id="l01792"></a>
<a id="l01793"></a>
<a id="l01794"></a>
<a id="l01795"></a>
<a id="l01796"></a>
<a id="l01797"></a>
<a id="l01798"></a>
<a id="l01799"></a>
<a id="foldopen01800"></a>
<a id="l01800"></a>
<a id="l01801"></a>
<a id="l01802"></a>
<a id="l01803"></a>
<a id="l01804"></a>
<a id="l01805"></a>
<a id="l01806"></a>
<a id="l01807"></a>
<a id="l01808"></a>
<a id="l01809"></a>
<a id="l01810"></a>
<a id="l01811"></a>
<a id="l01812"></a>
<a id="l01813"></a>
<a id="l01814"></a>
<a id="l01815"></a>
<a id="l01816"></a>
<a id="l01817"></a>
<a id="l01818"></a>
<a id="l01819"></a>
<a id="l01820"></a>
<a id="l01821"></a>
<a id="l01822"></a>
<a id="l01823"></a>
<a id="l01824"></a>
<a id="l01825"></a>
<a id="l01826"></a>
<a id="l01827"></a>
<a id="l01828"></a>
<a id="l01829"></a>
<a id="l01830"></a>
<a id="foldopen01831"></a>
<a id="l01831"></a>
<a id="l01832"></a>
<a id="l01833"></a>
<a id="l01834"></a>
<a id="l01835"></a>
<a id="l01836"></a>
<a id="l01837"></a>
<a id="l01838"></a>
<a id="l01839"></a>
<a id="foldopen01840"></a>
<a id="l01840"></a>
<a id="l01841"></a>
<a id="l01842"></a>
<a id="l01843"></a>
<a id="l01844"></a>
<a id="l01845"></a>
<a id="l01846"></a>
<a id="l01847"></a>
<a id="l01848"></a>
<a id="foldopen01849"></a>
<a id="l01849"></a>
<a id="l01850"></a>
<a id="l01851"></a>
<a id="l01852"></a>
<a id="l01853"></a>
<a id="l01854"></a>
<a id="foldopen01855"></a>
<a id="l01855"></a>
<a id="l01856"></a>
<a id="l01857"></a>
<a id="l01858"></a>
<a id="l01859"></a>
<a id="l01860"></a>
<a id="l01861"></a>
<a id="foldopen01862"></a>
<a id="l01862"></a>
<a id="l01863"></a>
<a id="l01864"></a>
<a id="l01865"></a>
<a id="l01866"></a>
<a id="l01867"></a>
<a id="foldopen01868"></a>
<a id="l01868"></a>
<a id="l01869"></a>
<a id="l01870"></a>
<a id="l01871"></a>
<a id="l01872"></a>
<a id="l01873"></a>
<a id="foldopen01874"></a>
<a id="l01874"></a>
<a id="l01875"></a>
<a id="l01876"></a>
<a id="l01877"></a>
<a id="l01878"></a>
<a id="l01879"></a>
<a id="l01880"></a>
<a id="l01881"></a>
<a id="l01882"></a>
<a id="l01883"></a>
<a id="foldopen01884"></a>
<a id="l01884"></a>
<a id="l01885"></a>
<a id="l01886"></a>
<a id="l01887"></a>
<a id="l01888"></a>
<a id="l01889"></a>
<a id="l01890"></a>
<a id="l01891"></a>
<a id="l01892"></a>
<a id="l01893"></a>
<a id="l01894"></a>
<a id="l01895"></a>
<a id="l01896"></a>
<a id="l01897"></a>
<a id="l01898"></a>
<a id="foldopen01899"></a>
<a id="l01899"></a>
<a id="l01900"></a>
<a id="l01901"></a>
<a id="l01902"></a>
<a id="l01903"></a>
<a id="l01904"></a>
<a id="l01905"></a>
<a id="l01906"></a>
<a id="l01907"></a>
<a id="l01908"></a>
<a id="l01909"></a>
<a id="foldopen01910"></a>
<a id="l01910"></a>
<a id="l01911"></a>
<a id="l01912"></a>
<a id="l01913"></a>
<a id="l01914"></a>
<a id="l01915"></a>
<a id="foldopen01916"></a>
<a id="l01916"></a>
<a id="l01917"></a>
<a id="l01918"></a>
<a id="l01919"></a>
<a id="l01920"></a>
<a id="l01921"></a>
<a id="l01922"></a>
<a id="l01923"></a>
<a id="l01924"></a>
<a id="l01925"></a>
<a id="foldopen01926"></a>
<a id="l01926"></a>
<a id="l01927"></a>
<a id="l01928"></a>
<a id="l01929"></a>
<a id="l01930"></a>
<a id="l01931"></a>
<a id="l01932"></a>
<a id="l01933"></a>
<a id="l01934"></a>
<a id="l01935"></a>
<a id="l01936"></a>
<a id="foldopen01937"></a>
<a id="l01937"></a>
<a id="l01938"></a>
<a id="l01939"></a>
<a id="l01940"></a>
<a id="l01941"></a>
<a id="l01942"></a>
<a id="l01943"></a>
<a id="l01944"></a>
<a id="l01945"></a>
<a id="foldopen01946"></a>
<a id="l01946"></a>
<a id="l01947"></a>
<a id="l01948"></a>
<a id="l01949"></a>
<a id="l01950"></a>
<a id="l01951"></a>
<a id="l01952"></a>
<a id="l01953"></a>
<a id="l01954"></a>
<a id="l01955"></a>
<a id="l01956"></a>
<a id="foldopen01957"></a>
<a id="l01957"></a>
<a id="l01958"></a>
<a id="l01959"></a>
<a id="l01960"></a>
<a id="l01961"></a>
<a id="l01962"></a>
<a id="l01963"></a>
<a id="l01964"></a>
<a id="foldopen01965"></a>
<a id="l01965"></a>
<a id="l01966"></a>
<a id="l01967"></a>
<a id="l01968"></a>
<a id="l01969"></a>
<a id="l01970"></a>
<a id="l01971"></a>
<a id="l01972"></a>
<a id="l01973"></a>
<a id="l01974"></a>
<a id="l01975"></a>
<a id="foldopen01976"></a>
<a id="l01976"></a>
<a id="l01977"></a>
<a id="l01978"></a>
<a id="l01979"></a>
<a id="l01980"></a>
<a id="l01981"></a>
<a id="l01982"></a>
<a id="l01983"></a>
<a id="foldopen01984"></a>
<a id="l01984"></a>
<a id="l01985"></a>
<a id="l01986"></a>
<a id="l01987"></a>
<a id="l01988"></a>
<a id="l01989"></a>
<a id="l01990"></a>
<a id="l01991"></a>
<a id="foldopen01992"></a>
<a id="l01992"></a>
<a id="l01993"></a>
<a id="l01994"></a>
<a id="l01995"></a>
<a id="l01996"></a>
<a id="l01997"></a>
<a id="l01998"></a>
<a id="l01999"></a>
<a id="l02000"></a>
<a id="l02001"></a>
<a id="l02002"></a>
<a id="foldopen02003"></a>
<a id="l02003"></a>
<a id="l02004"></a>
<a id="l02005"></a>
<a id="l02006"></a>
<a id="l02007"></a>
<a id="l02008"></a>
<a id="l02009"></a>
<a id="l02010"></a>
<a id="l02011"></a>
<a id="foldopen02012"></a>
<a id="l02012"></a>
<a id="l02013"></a>
<a id="l02014"></a>
<a id="l02015"></a>
<a id="l02016"></a>
<a id="l02017"></a>
<a id="l02018"></a>
<a id="l02019"></a>
<a id="l02020"></a>
<a id="l02021"></a>
<a id="l02022"></a>
<a id="l02023"></a>
<a id="l02024"></a>
<a id="l02025"></a>
<a id="l02026"></a>
<a id="l02027"></a>
<a id="l02028"></a>
<a id="l02029"></a>
<a id="l02030"></a>
<a id="l02031"></a>
<a id="l02032"></a>
<a id="l02033"></a>
<a id="l02034"></a>
<a id="l02035"></a>
<a id="l02036"></a>
<a id="foldopen02037"></a>
<a id="l02037"></a>
<a id="l02038"></a>
<a id="l02039"></a>
<a id="l02040"></a>
<a id="foldopen02041"></a>
<a id="l02041"></a>
<a id="l02042"></a>
<a id="l02043"></a>
<a id="l02044"></a>
<a id="l02045"></a>
<a id="l02046"></a>
<a id="l02047"></a>
<a id="l02048"></a>
<a id="l02049"></a>
<a id="l02050"></a>
<a id="l02051"></a>
<a id="l02052"></a>
<a id="foldopen02053"></a>
<a id="l02053"></a>
<a id="l02054"></a>
<a id="l02055"></a>
<a id="l02056"></a>
<a id="l02057"></a>
<a id="foldopen02058"></a>
<a id="l02058"></a>
<a id="l02059"></a>
<a id="l02060"></a>
<a id="l02061"></a>
<a id="l02062"></a>
<a id="l02063"></a>
<a id="foldopen02064"></a>
<a id="l02064"></a>
<a id="l02065"></a>
<a id="l02066"></a>
<a id="l02067"></a>
<a id="l02068"></a>
<a id="l02069"></a>
<a id="l02070"></a>
<a id="l02071"></a>
<a id="foldopen02072"></a>
<a id="l02072"></a>
<a id="l02073"></a>
<a id="l02074"></a>
<a id="l02075"></a>
<a id="l02076"></a>
<a id="l02077"></a>
<a id="foldopen02078"></a>
<a id="l02078"></a>
<a id="l02079"></a>
<a id="l02080"></a>
<a id="l02081"></a>
<a id="l02082"></a>
<a id="l02083"></a>
<a id="l02084"></a>
<a id="foldopen02085"></a>
<a id="l02085"></a>
<a id="l02086"></a>
<a id="l02087"></a>
<a id="l02088"></a>
<a id="l02089"></a>
<a id="l02090"></a>
<a id="l02091"></a>
<a id="foldopen02092"></a>
<a id="l02092"></a>
<a id="l02093"></a>
<a id="l02094"></a>
<a id="l02095"></a>
<a id="l02096"></a>
<a id="l02097"></a>
<a id="l02098"></a>
<a id="l02099"></a>
<a id="l02100"></a>
<a id="foldopen02101"></a>
<a id="l02101"></a>
<a id="l02102"></a>
<a id="l02103"></a>
<a id="l02104"></a>
<a id="l02105"></a>
<a id="l02106"></a>
<a id="l02107"></a>
<a id="l02108"></a>
<a id="l02109"></a>
<a id="l02110"></a>
<a id="l02111"></a>
<a id="foldopen02112"></a>
<a id="l02112"></a>
<a id="l02113"></a>
<a id="l02114"></a>
<a id="l02115"></a>
<a id="l02116"></a>
<a id="l02117"></a>
<a id="l02118"></a>
<a id="l02119"></a>
<a id="l02120"></a>
<a id="l02121"></a>
<a id="l02122"></a>
<a id="l02123"></a>
<a id="l02124"></a>
<a id="foldopen02125"></a>
<a id="l02125"></a>
<a id="l02126"></a>
<a id="l02127"></a>
<a id="l02128"></a>
<a id="l02129"></a>
<a id="l02130"></a>
<a id="l02131"></a>
<a id="l02132"></a>
<a id="l02133"></a>
<a id="l02134"></a>
<a id="l02135"></a>
<a id="l02136"></a>
<a id="l02137"></a>
<a id="l02138"></a>
<a id="l02139"></a>
<a id="l02140"></a>
<a id="l02141"></a>
<a id="l02142"></a>
<a id="l02143"></a>
<a id="l02144"></a>
<a id="l02145"></a>
<a id="l02146"></a>
<a id="l02147"></a>
<a id="l02148"></a>
<a id="foldopen02149"></a>
<a id="l02149"></a>
<a id="l02150"></a>
<a id="l02151"></a>
<a id="l02152"></a>
<a id="l02153"></a>
<a id="l02154"></a>
<a id="l02155"></a>
<a id="l02156"></a>
<a id="l02157"></a>
<a id="l02158"></a>
<a id="foldopen02159"></a>
<a id="l02159"></a>
<a id="l02160"></a>
<a id="l02161"></a>
<a id="l02162"></a>
<a id="l02163"></a>
<a id="l02164"></a>
<a id="l02165"></a>
<a id="l02166"></a>
<a id="l02167"></a>
<a id="l02168"></a>
<a id="l02169"></a>
<a id="l02170"></a>
<a id="l02171"></a>
<a id="foldopen02172"></a>
<a id="l02172"></a>
<a id="l02173"></a>
<a id="l02174"></a>
<a id="l02175"></a>
<a id="l02176"></a>
<a id="l02177"></a>
<a id="l02178"></a>
<a id="l02179"></a>
<a id="l02180"></a>
<a id="foldopen02181"></a>
<a id="l02181"></a>
<a id="l02182"></a>
<a id="l02183"></a>
<a id="l02184"></a>
<a id="l02185"></a>
<a id="l02186"></a>
<a id="foldopen02187"></a>
<a id="l02187"></a>
<a id="l02188"></a>
<a id="l02189"></a>
<a id="l02190"></a>
<a id="l02191"></a>
<a id="l02192"></a>
<a id="l02193"></a>
<a id="l02194"></a>
<a id="foldopen02195"></a>
<a id="l02195"></a>
<a id="l02196"></a>
<a id="l02197"></a>
<a id="l02198"></a>
<a id="l02199"></a>
<a id="l02200"></a>
<a id="l02201"></a>
<a id="l02202"></a>
<a id="l02203"></a>
<a id="l02204"></a>
<a id="l02205"></a>
<a id="l02206"></a>
<a id="l02207"></a>
<a id="foldopen02208"></a>
<a id="l02208"></a>
<a id="l02209"></a>
<a id="l02210"></a>
<a id="l02211"></a>
<a id="l02212"></a>
<a id="l02213"></a>
<a id="l02214"></a>
<a id="foldopen02215"></a>
<a id="l02215"></a>
<a id="l02216"></a>
<a id="l02217"></a>
<a id="l02218"></a>
<a id="l02219"></a>
<a id="l02220"></a>
<a id="l02221"></a>
<a id="l02222"></a>
<a id="l02223"></a>
<a id="l02224"></a>
<a id="l02225"></a>
<a id="foldopen02226"></a>
<a id="l02226"></a>
<a id="l02227"></a>
<a id="l02228"></a>
<a id="l02229"></a>
<a id="l02230"></a>
<a id="l02231"></a>
<a id="l02232"></a>
<a id="l02233"></a>
<a id="foldopen02234"></a>
<a id="l02234"></a>
<a id="l02235"></a>
<a id="l02236"></a>
<a id="l02237"></a>
<a id="l02238"></a>
<a id="l02239"></a>
<a id="foldopen02240"></a>
<a id="l02240"></a>
<a id="l02241"></a>
<a id="l02242"></a>
<a id="l02243"></a>
<a id="l02244"></a>
<a id="foldopen02245"></a>
<a id="l02245"></a>
<a id="l02246"></a>
<a id="l02247"></a>
<a id="l02248"></a>
<a id="l02249"></a>
<a id="l02250"></a>
<a id="l02251"></a>
<a id="l02252"></a>
<a id="l02253"></a>
<a id="l02254"></a>
<a id="l02255"></a>
<a id="l02256"></a>
<a id="l02257"></a>
<a id="l02258"></a>
<a id="l02259"></a>
<a id="l02260"></a>
<a id="l02261"></a>
<a id="l02262"></a>
<a id="l02263"></a>
<a id="foldopen02264"></a>
<a id="l02264"></a>
<a id="l02265"></a>
<a id="l02266"></a>
<a id="l02267"></a>
<a id="l02268"></a>
<a id="l02269"></a>
<a id="l02270"></a>
<a id="l02271"></a>
<a id="l02272"></a>
<a id="l02273"></a>
<a id="l02274"></a>
<a id="l02275"></a>
<a id="foldopen02276"></a>
<a id="l02276"></a>
<a id="l02277"></a>
<a id="l02278"></a>
<a id="l02279"></a>
<a id="l02280"></a>
<a id="l02281"></a>
<a id="foldopen02282"></a>
<a id="l02282"></a>
<a id="l02283"></a>
<a id="l02284"></a>
<a id="l02285"></a>
<a id="l02286"></a>
<a id="l02287"></a>
<a id="foldopen02288"></a>
<a id="l02288"></a>
<a id="l02289"></a>
<a id="l02290"></a>
<a id="l02291"></a>
<a id="l02292"></a>
<a id="l02293"></a>
<a id="foldopen02294"></a>
<a id="l02294"></a>
<a id="l02295"></a>
<a id="l02296"></a>
<a id="l02297"></a>
<a id="l02298"></a>
<a id="l02299"></a>
<a id="foldopen02300"></a>
<a id="l02300"></a>
<a id="l02301"></a>
<a id="l02302"></a>
<a id="l02303"></a>
<a id="l02304"></a>
<a id="l02305"></a>
<a id="l02306"></a>
<a id="l02307"></a>
<a id="l02308"></a>
<a id="l02309"></a>
<a id="l02310"></a>
<a id="l02311"></a>
<a id="l02312"></a>
<a id="l02313"></a>
<a id="l02314"></a>
<a id="l02315"></a>
<a id="l02316"></a>
<a id="foldopen02317"></a>
<a id="l02317"></a>
<a id="l02318"></a>
<a id="l02319"></a>
<a id="l02320"></a>
<a id="l02321"></a>
<a id="l02322"></a>
<a id="l02323"></a>
<a id="l02324"></a>
<a id="foldopen02325"></a>
<a id="l02325"></a>
<a id="l02326"></a>
<a id="l02327"></a>
<a id="l02328"></a>
<a id="l02329"></a>
<a id="l02330"></a>
<a id="foldopen02331"></a>
<a id="l02331"></a>
<a id="l02332"></a>
<a id="l02333"></a>
<a id="l02334"></a>
<a id="l02335"></a>
<a id="l02336"></a>
<a id="l02337"></a>
<a id="foldopen02338"></a>
<a id="l02338"></a>
<a id="l02339"></a>
<a id="l02340"></a>
<a id="l02341"></a>
<a id="l02342"></a>
<a id="foldopen02343"></a>
<a id="l02343"></a>
<a id="l02344"></a>
<a id="l02345"></a>
<a id="l02346"></a>
<a id="l02347"></a>
<a id="l02348"></a>
<a id="l02349"></a>
<a id="l02350"></a>
<a id="l02351"></a>
<a id="foldopen02352"></a>
<a id="l02352"></a>
<a id="l02353"></a>
<a id="l02354"></a>
<a id="l02355"></a>
<a id="foldopen02356"></a>
<a id="l02356"></a>
<a id="l02357"></a>
<a id="l02358"></a>
<a id="l02359"></a>
<a id="l02360"></a>
<a id="l02361"></a>
<a id="l02362"></a>
<a id="l02363"></a>
<a id="l02364"></a>
<a id="l02365"></a>
<a id="l02366"></a>
<a id="l02367"></a>
<a id="l02368"></a>
<a id="l02369"></a>
<a id="l02370"></a>
<a id="l02371"></a>
<a id="l02372"></a>
<a id="l02373"></a>
<a id="l02374"></a>
<a id="l02375"></a>
<a id="l02376"></a>
<a id="l02377"></a>
<a id="l02378"></a>
<a id="l02379"></a>
<a id="foldopen02380"></a>
<a id="l02380"></a>
<a id="l02381"></a>
<a id="l02382"></a>
<a id="l02383"></a>
<a id="l02384"></a>
<a id="l02385"></a>
<a id="l02386"></a>
<a id="l02387"></a>
<a id="l02388"></a>
<a id="l02389"></a>
<a id="foldopen02390"></a>
<a id="l02390"></a>
<a id="l02391"></a>
<a id="l02392"></a>
<a id="l02393"></a>
<a id="l02394"></a>
<a id="l02395"></a>
<a id="l02396"></a>
<a id="l02397"></a>
<a id="l02398"></a>
<a id="l02399"></a>
<a id="l02400"></a>
<a id="l02401"></a>
<a id="l02402"></a>
<a id="foldopen02403"></a>
<a id="l02403"></a>
<a id="l02404"></a>
<a id="l02405"></a>
<a id="l02406"></a>
<a id="l02407"></a>
<a id="l02408"></a>
<a id="l02409"></a>
<a id="l02410"></a>
<a id="foldopen02411"></a>
<a id="l02411"></a>
<a id="l02412"></a>
<a id="l02413"></a>
<a id="l02414"></a>
<a id="l02415"></a>
<a id="l02416"></a>
<a id="l02417"></a>
<a id="l02418"></a>
<a id="l02419"></a>
<a id="l02420"></a>
<a id="l02421"></a>
<a id="l02422"></a>
<a id="l02423"></a>
<a id="foldopen02424"></a>
<a id="l02424"></a>
<a id="l02425"></a>
<a id="l02426"></a>
<a id="l02427"></a>
<a id="l02428"></a>
<a id="l02429"></a>
<a id="l02430"></a>
<a id="l02431"></a>
<a id="l02432"></a>
<a id="l02433"></a>
<a id="l02434"></a>
<a id="l02435"></a>
<a id="l02436"></a>
<a id="l02437"></a>
<a id="foldopen02438"></a>
<a id="l02438"></a>
<a id="l02439"></a>
<a id="l02440"></a>
<a id="l02441"></a>
<a id="l02442"></a>
<a id="l02443"></a>
<a id="l02444"></a>
<a id="l02445"></a>
<a id="foldopen02446"></a>
<a id="l02446"></a>
<a id="l02447"></a>
<a id="l02448"></a>
<a id="l02449"></a>
<a id="l02450"></a>
<a id="foldopen02451"></a>
<a id="l02451"></a>
<a id="l02452"></a>
<a id="l02453"></a>
<a id="l02454"></a>
<a id="l02455"></a>
<a id="l02456"></a>
<a id="foldopen02457"></a>
<a id="l02457"></a>
<a id="l02458"></a>
<a id="l02459"></a>
<a id="l02460"></a>
<a id="foldopen02461"></a>
<a id="l02461"></a>
<a id="l02462"></a>
<a id="l02463"></a>
<a id="l02464"></a>
<a id="l02465"></a>
<a id="l02466"></a>
<a id="foldopen02467"></a>
<a id="l02467"></a>
<a id="l02468"></a>
<a id="l02469"></a>
<a id="l02470"></a>
<a id="l02471"></a>
<a id="foldopen02472"></a>
<a id="l02472"></a>
<a id="l02473"></a>
<a id="l02474"></a>
<a id="l02475"></a>
<a id="l02476"></a>
<a id="foldopen02477"></a>
<a id="l02477"></a>
<a id="l02478"></a>
<a id="l02479"></a>
<a id="l02480"></a>
<a id="l02481"></a>
<a id="l02482"></a>
<a id="foldopen02483"></a>
<a id="l02483"></a>
<a id="l02484"></a>
<a id="l02485"></a>
<a id="l02486"></a>
<a id="l02487"></a>
<a id="l02488"></a>
<a id="l02489"></a>
<a id="l02490"></a>
<a id="l02491"></a>
<a id="l02492"></a>
<a id="l02493"></a>
<a id="l02494"></a>
<a id="l02495"></a>
<a id="l02496"></a>
<a id="l02497"></a>
<a id="l02498"></a>
<a id="foldopen02499"></a>
<a id="l02499"></a>
<a id="l02500"></a>
<a id="l02501"></a>
<a id="l02502"></a>
<a id="l02503"></a>
<a id="l02504"></a>
<a id="l02505"></a>
<a id="l02506"></a>
<a id="l02507"></a>
<a id="l02508"></a>
<a id="l02509"></a>
<a id="l02510"></a>
<a id="l02511"></a>
<a id="l02512"></a>
<a id="l02513"></a>
<a id="l02514"></a>
<a id="l02515"></a>
<a id="l02516"></a>
<a id="l02517"></a>
<a id="l02518"></a>
<a id="foldopen02519"></a>
<a id="l02519"></a>
<a id="l02520"></a>
<a id="l02521"></a>
<a id="l02522"></a>
<a id="l02523"></a>
<a id="l02524"></a>
<a id="foldopen02525"></a>
<a id="l02525"></a>
<a id="l02526"></a>
<a id="l02527"></a>
<a id="l02528"></a>
<a id="l02529"></a>
<a id="l02530"></a>
<a id="l02531"></a>
<a id="l02532"></a>
<a id="l02533"></a>
<a id="l02534"></a>
<a id="l02535"></a>
<a id="l02536"></a>
<a id="foldopen02537"></a>
<a id="l02537"></a>
<a id="l02538"></a>
<a id="l02539"></a>
<a id="l02540"></a>
<a id="foldopen02541"></a>
<a id="l02541"></a>
<a id="l02542"></a>
<a id="l02543"></a>
<a id="l02544"></a>
<a id="l02545"></a>
<a id="l02546"></a>
<a id="foldopen02547"></a>
<a id="l02547"></a>
<a id="l02548"></a>
<a id="l02549"></a>
<a id="l02550"></a>
<a id="l02551"></a>
<a id="foldopen02552"></a>
<a id="l02552"></a>
<a id="l02553"></a>
<a id="l02554"></a>
<a id="l02555"></a>
<a id="l02556"></a>
<a id="l02557"></a>
<a id="l02558"></a>
<a id="l02559"></a>
<a id="l02560"></a>
<a id="l02561"></a>
<a id="foldopen02562"></a>
<a id="l02562"></a>
<a id="l02563"></a>
<a id="l02564"></a>
<a id="l02565"></a>
<a id="l02566"></a>
<a id="l02567"></a>
<a id="foldopen02568"></a>
<a id="l02568"></a>
<a id="l02569"></a>
<a id="l02570"></a>
<a id="l02571"></a>
<a id="l02572"></a>
<a id="foldopen02573"></a>
<a id="l02573"></a>
<a id="l02574"></a>
<a id="l02575"></a>
<a id="l02576"></a>
<a id="l02577"></a>
<a id="l02578"></a>
<a id="l02579"></a>
<a id="l02580"></a>
<a id="l02581"></a>
<a id="l02582"></a>
<a id="foldopen02583"></a>
<a id="l02583"></a>
<a id="l02584"></a>
<a id="l02585"></a>
<a id="l02586"></a>
<a id="l02587"></a>
<a id="foldopen02588"></a>
<a id="l02588"></a>
<a id="l02589"></a>
<a id="l02590"></a>
<a id="l02591"></a>
<a id="l02592"></a>
<a id="l02593"></a>
<a id="foldopen02594"></a>
<a id="l02594"></a>
<a id="l02595"></a>
<a id="l02596"></a>
<a id="l02597"></a>
<a id="l02598"></a>
<a id="foldopen02599"></a>
<a id="l02599"></a>
<a id="l02600"></a>
<a id="l02601"></a>
<a id="l02602"></a>
<a id="l02603"></a>
<a id="l02604"></a>
<a id="foldopen02605"></a>
<a id="l02605"></a>
<a id="l02606"></a>
<a id="l02607"></a>
<a id="l02608"></a>
<a id="foldopen02609"></a>
<a id="l02609"></a>
<a id="l02610"></a>
<a id="l02611"></a>
<a id="l02612"></a>
<a id="l02613"></a>
<a id="l02614"></a>
<a id="l02615"></a>
<a id="l02616"></a>
<a id="l02617"></a>
<a id="foldopen02618"></a>
<a id="l02618"></a>
<a id="l02619"></a>
<a id="l02620"></a>
<a id="l02621"></a>
<a id="foldopen02622"></a>
<a id="l02622"></a>
<a id="l02623"></a>
<a id="l02624"></a>
<a id="l02625"></a>
<a id="l02626"></a>
<a id="l02627"></a>
<a id="l02628"></a>
<a id="l02629"></a>
<a id="l02630"></a>
<a id="foldopen02631"></a>
<a id="l02631"></a>
<a id="l02632"></a>
<a id="l02633"></a>
<a id="l02634"></a>
<a id="l02635"></a>
<a id="foldopen02636"></a>
<a id="l02636"></a>
<a id="l02637"></a>
<a id="l02638"></a>
<a id="l02639"></a>
<a id="l02640"></a>
<a id="foldopen02641"></a>
<a id="l02641"></a>
<a id="l02642"></a>
<a id="l02643"></a>
<a id="l02644"></a>
<a id="foldopen02645"></a>
<a id="l02645"></a>
<a id="l02646"></a>
<a id="l02647"></a>
<a id="l02648"></a>
<a id="l02649"></a>
<a id="l02650"></a>
<a id="l02651"></a>
<a id="l02652"></a>
<a id="l02653"></a>
<a id="l02654"></a>
<a id="l02655"></a>
<a id="l02656"></a>
<a id="l02657"></a>
<a id="l02658"></a>
<a id="foldopen02659"></a>
<a id="l02659"></a>
<a id="l02660"></a>
<a id="l02661"></a>
<a id="l02662"></a>
<a id="l02663"></a>
<a id="l02664"></a>
<a id="l02665"></a>
<a id="l02666"></a>
<a id="l02667"></a>
<a id="l02668"></a>
<a id="l02669"></a>
<a id="l02670"></a>
<a id="foldopen02671"></a>
<a id="l02671"></a>
<a id="l02672"></a>
<a id="l02673"></a>
<a id="l02674"></a>
<a id="l02675"></a>
<a id="l02676"></a>
<a id="foldopen02677"></a>
<a id="l02677"></a>
<a id="l02678"></a>
<a id="l02679"></a>
<a id="l02680"></a>
<a id="foldopen02681"></a>
<a id="l02681"></a>
<a id="l02682"></a>
<a id="l02683"></a>
<a id="l02684"></a>
<a id="l02685"></a>
<a id="l02686"></a>
<a id="l02687"></a>
<a id="l02688"></a>
<a id="l02689"></a>
<a id="l02690"></a>
<a id="l02691"></a>
<a id="l02692"></a>
<a id="l02693"></a>
<a id="l02694"></a>
<a id="l02695"></a>
<a id="foldopen02696"></a>
<a id="l02696"></a>
<a id="l02697"></a>
<a id="l02698"></a>
<a id="l02699"></a>
<a id="l02700"></a>
<a id="l02701"></a>
<a id="foldopen02702"></a>
<a id="l02702"></a>
<a id="l02703"></a>
<a id="l02704"></a>
<a id="l02705"></a>
<a id="l02706"></a>
<a id="l02707"></a>
<a id="l02708"></a>
<a id="l02709"></a>
<a id="l02710"></a>
<a id="l02711"></a>
<a id="l02712"></a>
<a id="l02713"></a>
<a id="l02714"></a>
<a id="l02715"></a>
<a id="l02716"></a>
<a id="l02717"></a>
<a id="l02718"></a>
<a id="l02719"></a>
<a id="l02720"></a>
<a id="l02721"></a>
<a id="l02722"></a>
<a id="l02723"></a>
<a id="l02724"></a>
<a id="l02725"></a>
<a id="l02727"></a>
<a id="foldopen02729"></a>
<a id="l02729"></a>
<a id="l02730"></a>
<a id="l02731"></a>
<a id="foldopen02733"></a>
<a id="l02733"></a>
<a id="l02735"></a>
<a id="l02737"></a>
<a id="l02739"></a>
<a id="l02741"></a>
<a id="l02743"></a>
<a id="l02745"></a>
<a id="l02747"></a>
<a id="l02749"></a>
<a id="l02751"></a>
<a id="l02753"></a>
<a id="l02755"></a>
<a id="l02757"></a>
<a id="l02759"></a>
<a id="l02761"></a>
<a id="l02763"></a>
<a id="l02765"></a>
<a id="l02767"></a>
<a id="l02769"></a>
<a id="l02771"></a>
<a id="l02773"></a>
<a id="l02775"></a>
<a id="l02777"></a>
<a id="l02779"></a>
<a id="l02780"></a>
<a id="l02781"></a>
<a id="l02782"></a>
<a id="l02783"></a>
<a id="foldopen02784"></a>
<a id="l02784"></a>
<a id="l02785"></a>
<a id="l02786"></a>
<a id="l02787"></a>
<a id="foldopen02788"></a>
<a id="l02788"></a>
<a id="l02789"></a>
<a id="l02790"></a>
<a id="foldopen02791"></a>
<a id="l02791"></a>
<a id="l02792"></a>
<a id="l02793"></a>
<a id="l02794"></a>
<a id="l02795"></a>
<a id="l02796"></a>
<a id="l02797"></a>
<a id="l02798"></a>
<a id="l02799"></a>
<a id="l02800"></a>
<a id="l02801"></a>
<a id="l02802"></a>
<a id="l02803"></a>
<a id="l02804"></a>
<a id="l02805"></a>
<a id="l02806"></a>
<a id="l02807"></a>
<a id="l02808"></a>
<a id="l02809"></a>
<a id="l02810"></a>
<a id="l02811"></a>
<a id="l02812"></a>
<a id="l02813"></a>
<a id="l02814"></a>
<a id="foldopen02816"></a>
<a id="l02816"></a>
<a id="l02817"></a>
<a id="l02818"></a>
<a id="foldopen02820"></a>
<a id="l02820"></a>
<a id="l02822"></a>
<a id="l02824"></a>
<a id="l02826"></a>
<a id="l02828"></a>
<a id="l02830"></a>
<a id="l02832"></a>
<a id="l02834"></a>
<a id="l02836"></a>
<a id="l02838"></a>
<a id="l02840"></a>
<a id="l02842"></a>
<a id="l02844"></a>
<a id="l02846"></a>
<a id="l02848"></a>
<a id="l02850"></a>
<a id="l02852"></a>
<a id="l02854"></a>
<a id="l02856"></a>
<a id="l02858"></a>
<a id="l02860"></a>
<a id="l02862"></a>
<a id="l02864"></a>
<a id="l02866"></a>
<a id="l02867"></a>
<a id="l02868"></a>
<a id="l02869"></a>
<a id="l02870"></a>
<a id="foldopen02871"></a>
<a id="l02871"></a>
<a id="l02872"></a>
<a id="l02873"></a>
<a id="l02874"></a>
<a id="l02875"></a>
<a id="l02876"></a>
<a id="l02877"></a>
<a id="l02878"></a>
<a id="l02879"></a>
<a id="l02880"></a>
<a id="l02881"></a>
<a id="l02882"></a>
<a id="l02883"></a>
<a id="l02884"></a>
<a id="l02885"></a>
<a id="l02886"></a>
<a id="l02887"></a>
<a id="l02888"></a>
<a id="l02889"></a>
<a id="foldopen02890"></a>
<a id="l02890"></a>
<a id="l02891"></a>
<a id="l02892"></a>
<a id="l02893"></a>
<a id="l02894"></a>
<a id="l02895"></a>
<a id="l02896"></a>
<a id="l02897"></a>
<a id="l02898"></a>
<a id="foldopen02899"></a>
<a id="l02899"></a>
<a id="l02900"></a>
<a id="l02901"></a>
<a id="l02902"></a>
<a id="l02903"></a>
<a id="l02904"></a>
<a id="foldopen02905"></a>
<a id="l02905"></a>
<a id="l02906"></a>
<a id="l02907"></a>
<a id="l02908"></a>
<a id="l02909"></a>
<a id="l02910"></a>
<a id="l02911"></a>
<a id="l02912"></a>
<a id="l02913"></a>
<a id="l02914"></a>
<a id="l02915"></a>
<a id="l02916"></a>
<a id="l02917"></a>
<a id="l02918"></a>
<a id="foldopen02919"></a>
<a id="l02919"></a>
<a id="l02920"></a>
<a id="l02921"></a>
<a id="l02922"></a>
<a id="l02923"></a>
<a id="l02924"></a>
<a id="l02925"></a>
<a id="l02926"></a>
<a id="l02927"></a>
<a id="l02928"></a>
<a id="l02929"></a>
<a id="l02930"></a>
<a id="l02931"></a>
<a id="l02932"></a>
<a id="l02933"></a>
<a id="l02934"></a>
<a id="l02935"></a>
<a id="l02936"></a>
<a id="l02937"></a>
<a id="l02938"></a>
<a id="l02939"></a>
<a id="l02940"></a>
<a id="foldopen02941"></a>
<a id="l02941"></a>
<a id="l02942"></a>
<a id="l02943"></a>
<a id="l02944"></a>
<a id="l02945"></a>
<a id="l02946"></a>
<a id="l02947"></a>
<a id="l02948"></a>
<a id="l02949"></a>
<a id="l02950"></a>
<a id="l02951"></a>
<a id="l02952"></a>
<a id="l02953"></a>
<a id="l02954"></a>
<a id="l02955"></a>
<a id="l02956"></a>
<a id="l02957"></a>
<a id="l02958"></a>
<a id="l02959"></a>
<a id="l02960"></a>
<a id="l02961"></a>
<a id="l02962"></a>
<a id="l02963"></a>
<a id="l02964"></a>
<a id="l02965"></a>
<a id="l02966"></a>
<a id="l02967"></a>
<a id="l02968"></a>
<a id="l02969"></a>
<a id="l02970"></a>
<a id="l02971"></a>
<a id="l02972"></a>
<a id="l02973"></a>
<a id="l02974"></a>
<a id="l02975"></a>
<a id="l02976"></a>
<a id="l02977"></a>
<a id="l02978"></a>
<a id="l02979"></a>
<a id="l02980"></a>
<a id="l02981"></a>
<a id="l02982"></a>
<a id="l02983"></a>
<a id="l02984"></a>
<a id="l02985"></a>
<a id="l02986"></a>
<a id="l02987"></a>
<a id="l02988"></a>
<a id="l02989"></a>
<a id="l02990"></a>
<a id="l02991"></a>
<a id="l02992"></a>
<a id="l02993"></a>
<a id="l02994"></a>
<a id="l02995"></a>
<a id="l02996"></a>
<a id="l02997"></a>
<a id="l02998"></a>
<a id="l02999"></a>
<a id="l03000"></a>
<a id="l03001"></a>
<a id="l03002"></a>
<a id="l03003"></a>
<a id="l03004"></a>
<a id="l03005"></a>
<a id="l03006"></a>
<a id="l03007"></a>
<a id="l03008"></a>
<a id="l03009"></a>
<a id="l03010"></a>
<a id="l03011"></a>
<a id="l03012"></a>
<a id="l03013"></a>
<a id="l03014"></a>
<a id="l03015"></a>
<a id="l03016"></a>
<a id="l03017"></a>
<a id="l03018"></a>
<a id="l03019"></a>
<a id="l03020"></a>
<a id="l03021"></a>
<a id="l03022"></a>
<a id="l03023"></a>
<a id="l03024"></a>
<a id="l03025"></a>
<a id="l03026"></a>
<a id="l03027"></a>
<a id="l03028"></a>
<a id="l03029"></a>
<a id="l03030"></a>
<a id="l03031"></a>
<a id="l03032"></a>
<a id="l03033"></a>
<a id="l03034"></a>
<a id="l03035"></a>
<a id="l03036"></a>
<a id="l03037"></a>
<a id="l03038"></a>
<a id="l03039"></a>
<a id="l03040"></a>
<a id="l03041"></a>
<a id="l03042"></a>
<a id="l03043"></a>
<a id="l03044"></a>
<a id="l03045"></a>
<a id="l03046"></a>
<a id="l03047"></a>
<a id="l03048"></a>
<a id="l03049"></a>
<a id="l03050"></a>
<a id="l03051"></a>
<a id="l03052"></a>
<a id="l03053"></a>
<a id="l03054"></a>
<a id="l03055"></a>
<a id="foldopen03056"></a>
<a id="l03056"></a>
<a id="l03057"></a>
<a id="l03058"></a>
<a id="l03059"></a>
<a id="l03060"></a>
<a id="l03061"></a>
<a id="l03062"></a>
<a id="l03063"></a>
<a id="l03064"></a>
<a id="l03065"></a>
<a id="l03066"></a>
<a id="l03067"></a>
<a id="l03068"></a>
<a id="l03069"></a>
<a id="l03070"></a>
<a id="l03071"></a>
<a id="l03072"></a>
<a id="l03073"></a>
<a id="l03074"></a>
<a id="l03076"></a>
<a id="l03077"></a>
<a id="l03078"></a>
<a id="l03079"></a>
<a id="l03080"></a>
<a id="l03081"></a>
<a id="l03082"></a>
<a id="l03083"></a>
<a id="l03084"></a>
<a id="l03085"></a>
<a id="l03086"></a>
<a id="l03087"></a>
<a id="foldopen03088"></a>
<a id="l03088"></a>
<a id="l03089"></a>
<a id="l03090"></a>
<a id="l03091"></a>
<a id="l03092"></a>
<a id="l03093"></a>
<a id="l03094"></a>
<a id="l03095"></a>
<a id="l03096"></a>
<a id="l03097"></a>
<a id="l03098"></a>
<a id="l03099"></a>
<a id="l03100"></a>
<a id="l03101"></a>
<a id="l03102"></a>
<a id="l03103"></a>
<a id="l03104"></a>
<a id="l03105"></a>
<a id="l03107"></a>
<a id="l03108"></a>
<a id="l03109"></a>
<a id="l03110"></a>
<a id="l03111"></a>
<a id="foldopen03112"></a>
<a id="l03112"></a>
<a id="l03113"></a>
<a id="l03114"></a>
<a id="l03115"></a>
<a id="l03116"></a>
<a id="l03117"></a>
<a id="l03118"></a>
<a id="l03119"></a>
<a id="l03120"></a>
<a id="l03121"></a>
<a id="l03122"></a>
<a id="l03123"></a>
<a id="l03124"></a>
<a id="l03125"></a>
<a id="l03126"></a>
<a id="l03127"></a>
<a id="l03128"></a>
<a id="l03129"></a>
<a id="l03130"></a>
<a id="l03131"></a>
<a id="l03132"></a>
<a id="foldopen03133"></a>
<a id="l03133"></a>
<a id="l03134"></a>
<a id="l03135"></a>
<a id="l03136"></a>
<a id="l03137"></a>
<a id="l03138"></a>
<a id="l03139"></a>
<a id="l03140"></a>
<a id="l03141"></a>
<a id="l03142"></a>
<a id="l03144"></a>
<a id="l03145"></a>
<a id="l03146"></a>
<a id="l03147"></a>
<a id="l03148"></a>
<a id="l03149"></a>
<a id="l03150"></a>
<a id="l03151"></a>
<a id="l03152"></a>
<a id="l03153"></a>
<a id="l03154"></a>
<a id="l03155"></a>
<a id="l03156"></a>
<a id="l03157"></a>
<a id="foldopen03158"></a>
<a id="l03158"></a>
<a id="l03159"></a>
<a id="l03160"></a>
<a id="l03161"></a>
<a id="l03162"></a>
<a id="l03163"></a>
<a id="foldopen03164"></a>
<a id="l03164"></a>
<a id="l03165"></a>
<a id="l03166"></a>
<a id="l03167"></a>
<a id="l03168"></a>
<a id="l03169"></a>
<a id="l03170"></a>
<a id="foldopen03171"></a>
<a id="l03171"></a>
<a id="l03172"></a>
<a id="l03173"></a>
<a id="foldopen03174"></a>
<a id="l03174"></a>
<a id="l03175"></a>
<a id="l03176"></a>
<a id="l03177"></a>
<a id="l03178"></a>
<a id="l03179"></a>
<a id="l03180"></a>
<a id="l03181"></a>
<a id="l03182"></a>
<a id="l03183"></a>
<a id="l03184"></a>
<a id="l03185"></a>
<a id="l03186"></a>
<a id="l03187"></a>
<a id="foldopen03188"></a>
<a id="l03188"></a>
<a id="l03189"></a>
<a id="l03190"></a>
<a id="l03191"></a>
<a id="l03192"></a>
<a id="l03193"></a>
<a id="l03194"></a>
<a id="l03195"></a>
<a id="l03196"></a>
<a id="l03197"></a>
<a id="l03198"></a>
<a id="l03199"></a>
<a id="l03200"></a>
<a id="l03201"></a>
<a id="l03202"></a>
<a id="l03203"></a>
<a id="l03204"></a>
<a id="l03205"></a>
<a id="l03206"></a>
<a id="l03207"></a>
<a id="l03208"></a>
<a id="foldopen03209"></a>
<a id="l03209"></a>
<a id="l03210"></a>
<a id="l03211"></a>
<a id="l03212"></a>
<a id="l03213"></a>
<a id="foldopen03214"></a>
<a id="l03214"></a>
<a id="l03215"></a>
<a id="l03216"></a>
<a id="l03217"></a>
<a id="l03218"></a>
<a id="l03219"></a>
<a id="l03220"></a>
<a id="l03221"></a>
<a id="l03222"></a>
<a id="foldopen03223"></a>
<a id="l03223"></a>
<a id="l03224"></a>
<a id="l03225"></a>
<a id="l03226"></a>
<a id="l03227"></a>
<a id="l03228"></a>
<a id="l03229"></a>
<a id="foldopen03230"></a>
<a id="l03230"></a>
<a id="l03231"></a>
<a id="l03232"></a>
<a id="l03233"></a>
<a id="l03234"></a>
<a id="l03235"></a>
<a id="l03236"></a>
<a id="foldopen03237"></a>
<a id="l03237"></a>
<a id="l03238"></a>
<a id="l03239"></a>
<a id="l03240"></a>
<a id="l03241"></a>
<a id="l03242"></a>
<a id="foldopen03243"></a>
<a id="l03243"></a>
<a id="l03244"></a>
<a id="l03245"></a>
<a id="l03246"></a>
<a id="l03247"></a>
<a id="l03248"></a>
<a id="l03249"></a>
<a id="l03250"></a>
<a id="l03251"></a>
<a id="l03252"></a>
<a id="l03253"></a>
<a id="l03254"></a>
<a id="l03255"></a>
<a id="foldopen03256"></a>
<a id="l03256"></a>
<a id="l03257"></a>
<a id="l03258"></a>
<a id="l03259"></a>
<a id="l03260"></a>
<a id="l03261"></a>
<a id="l03262"></a>
<a id="foldopen03263"></a>
<a id="l03263"></a>
<a id="l03264"></a>
<a id="l03265"></a>
<a id="l03266"></a>
<a id="l03267"></a>
<a id="l03268"></a>
<a id="l03269"></a>
<a id="foldopen03270"></a>
<a id="l03270"></a>
<a id="l03271"></a>
<a id="l03272"></a>
<a id="l03273"></a>
<a id="l03274"></a>
<a id="l03275"></a>
<a id="l03276"></a>
<a id="l03277"></a>
<a id="l03278"></a>
<a id="foldopen03279"></a>
<a id="l03279"></a>
<a id="l03280"></a>
<a id="l03281"></a>
<a id="l03282"></a>
<a id="l03283"></a>
<a id="foldopen03284"></a>
<a id="l03284"></a>
<a id="l03285"></a>
<a id="l03286"></a>
<a id="l03287"></a>
<a id="l03288"></a>
<a id="foldopen03289"></a>
<a id="l03289"></a>
<a id="l03290"></a>
<a id="l03291"></a>
<a id="l03292"></a>
<a id="l03293"></a>
<a id="l03294"></a>
<a id="l03295"></a>
<a id="foldopen03296"></a>
<a id="l03296"></a>
<a id="l03297"></a>
<a id="l03298"></a>
<a id="l03299"></a>
<a id="l03300"></a>
<a id="foldopen03301"></a>
<a id="l03301"></a>
<a id="l03302"></a>
<a id="l03303"></a>
<a id="l03304"></a>
<a id="l03305"></a>
<a id="l03306"></a>
<a id="l03307"></a>
<a id="foldopen03308"></a>
<a id="l03308"></a>
<a id="l03309"></a>
<a id="l03310"></a>
<a id="l03311"></a>
<a id="l03312"></a>
<a id="l03313"></a>
<a id="l03314"></a>
<a id="l03315"></a>
<a id="l03316"></a>
<a id="l03317"></a>
<a id="l03318"></a>
<a id="foldopen03319"></a>
<a id="l03319"></a>
<a id="l03320"></a>
<a id="l03321"></a>
<a id="l03322"></a>
<a id="l03323"></a>
<a id="l03324"></a>
<a id="l03325"></a>
<a id="l03326"></a>
<a id="foldopen03327"></a>
<a id="l03327"></a>
<a id="l03328"></a>
<a id="l03329"></a>
<a id="l03330"></a>
<a id="l03331"></a>
<a id="foldopen03332"></a>
<a id="l03332"></a>
<a id="l03333"></a>
<a id="l03334"></a>
<a id="l03335"></a>
<a id="l03336"></a>
<a id="l03337"></a>
<a id="l03338"></a>
<a id="l03339"></a>
<a id="l03340"></a>
<a id="l03341"></a>
<a id="l03342"></a>
<a id="l03343"></a>
<a id="l03344"></a>
<a id="l03345"></a>
<a id="l03346"></a>
<a id="l03347"></a>
<a id="foldopen03348"></a>
<a id="l03348"></a>
<a id="l03349"></a>
<a id="l03350"></a>
<a id="l03351"></a>
<a id="l03352"></a>
<a id="l03353"></a>
<a id="l03354"></a>
<a id="l03355"></a>
<a id="l03356"></a>
<a id="l03357"></a>
<a id="l03358"></a>
<a id="l03359"></a>
<a id="foldopen03360"></a>
<a id="l03360"></a>
<a id="l03361"></a>
<a id="l03362"></a>
<a id="l03363"></a>
<a id="l03365"></a>
<a id="foldopen03367"></a>
<a id="l03367"></a>
<a id="l03369"></a>
<a id="l03371"></a>
<a id="l03373"></a>
<a id="l03374"></a>
<a id="l03375"></a>
<a id="l03376"></a>
<a id="foldopen03377"></a>
<a id="l03377"></a>
<a id="l03378"></a>
<a id="l03379"></a>
<a id="l03380"></a>
<a id="l03381"></a>
<a id="l03382"></a>
<a id="l03383"></a>
<a id="l03384"></a>
<a id="l03385"></a>
<a id="l03386"></a>
<a id="foldopen03387"></a>
<a id="l03387"></a>
<a id="l03388"></a>
<a id="l03389"></a>
<a id="l03390"></a>
<a id="l03391"></a>
<a id="l03392"></a>
<a id="l03393"></a>
<a id="l03394"></a>
<a id="l03395"></a>
<a id="foldopen03396"></a>
<a id="l03396"></a>
<a id="l03397"></a>
<a id="l03398"></a>
<a id="l03399"></a>
<a id="l03400"></a>
<a id="l03401"></a>
<a id="l03402"></a>
<a id="l03403"></a>
<a id="l03404"></a>
<a id="l03405"></a>
<a id="l03406"></a>
<a id="l03407"></a>
<a id="l03408"></a>
<a id="l03409"></a>
<a id="l03410"></a>
<a id="foldopen03411"></a>
<a id="l03411"></a>
<a id="l03412"></a>
<a id="l03413"></a>
<a id="l03414"></a>
<a id="l03415"></a>
<a id="l03416"></a>
<a id="l03417"></a>
<a id="l03418"></a>
<a id="l03419"></a>
<a id="l03420"></a>
<a id="l03421"></a>
<a id="l03422"></a>
<a id="l03423"></a>
<a id="foldopen03424"></a>
<a id="l03424"></a>
<a id="l03425"></a>
<a id="l03426"></a>
<a id="l03427"></a>
<a id="l03428"></a>
<a id="l03429"></a>
<a id="l03430"></a>
<a id="l03431"></a>
<a id="l03432"></a>
<a id="l03433"></a>
<a id="l03434"></a>
<a id="l03435"></a>
<a id="l03436"></a>
<a id="l03437"></a>
<a id="l03438"></a>
<a id="l03439"></a>
<a id="l03440"></a>
<a id="foldopen03441"></a>
<a id="l03441"></a>
<a id="l03442"></a>
<a id="l03443"></a>
<a id="l03444"></a>
<a id="l03445"></a>
<a id="l03446"></a>
<a id="l03447"></a>
<a id="l03448"></a>
<a id="foldopen03449"></a>
<a id="l03449"></a>
<a id="l03450"></a>
<a id="l03451"></a>
<a id="l03452"></a>
<a id="l03453"></a>
<a id="l03454"></a>
<a id="l03455"></a>
<a id="l03456"></a>
<a id="l03457"></a>
<a id="l03458"></a>
<a id="foldopen03459"></a>
<a id="l03459"></a>
<a id="l03460"></a>
<a id="l03461"></a>
<a id="l03462"></a>
<a id="l03463"></a>
<a id="l03464"></a>
<a id="l03465"></a>
<a id="l03466"></a>
<a id="l03467"></a>
<a id="foldopen03468"></a>
<a id="l03468"></a>
<a id="l03469"></a>
<a id="l03470"></a>
<a id="l03471"></a>
<a id="l03472"></a>
<a id="l03473"></a>
<a id="l03474"></a>
<a id="l03475"></a>
<a id="l03476"></a>
<a id="l03477"></a>
<a id="l03478"></a>
<a id="l03479"></a>
<a id="l03480"></a>
<a id="l03481"></a>
<a id="l03482"></a>
<a id="l03483"></a>
<a id="foldopen03484"></a>
<a id="l03484"></a>
<a id="l03485"></a>
<a id="l03486"></a>
<a id="l03487"></a>
<a id="l03488"></a>
<a id="l03489"></a>
<a id="l03490"></a>
<a id="l03491"></a>
<a id="l03492"></a>
<a id="l03493"></a>
<a id="l03494"></a>
<a id="l03495"></a>
<a id="l03496"></a>
<a id="foldopen03497"></a>
<a id="l03497"></a>
<a id="l03498"></a>
<a id="l03499"></a>
<a id="l03500"></a>
<a id="l03501"></a>
<a id="l03502"></a>
<a id="l03503"></a>
<a id="l03504"></a>
<a id="l03505"></a>
<a id="l03506"></a>
<a id="l03507"></a>
<a id="l03508"></a>
<a id="foldopen03509"></a>
<a id="l03509"></a>
<a id="l03510"></a>
<a id="l03511"></a>
<a id="l03512"></a>
<a id="l03513"></a>
<a id="l03514"></a>
<a id="foldopen03515"></a>
<a id="l03515"></a>
<a id="l03516"></a>
<a id="l03517"></a>
<a id="l03518"></a>
<a id="l03519"></a>
<a id="foldopen03520"></a>
<a id="l03520"></a>
<a id="l03521"></a>
<a id="l03522"></a>
<a id="l03523"></a>
<a id="l03524"></a>
<a id="l03525"></a>
<a id="l03526"></a>
<a id="l03527"></a>
<a id="foldopen03528"></a>
<a id="l03528"></a>
<a id="l03529"></a>
<a id="l03530"></a>
<a id="l03531"></a>
<a id="l03532"></a>
<a id="l03533"></a>
<a id="foldopen03534"></a>
<a id="l03534"></a>
<a id="l03535"></a>
<a id="l03536"></a>
<a id="l03537"></a>
<a id="l03538"></a>
<a id="foldopen03539"></a>
<a id="l03539"></a>
<a id="l03540"></a>
<a id="l03541"></a>
<a id="l03542"></a>
<a id="l03543"></a>
<a id="l03544"></a>
<a id="foldopen03545"></a>
<a id="l03545"></a>
<a id="l03546"></a>
<a id="l03547"></a>
<a id="l03548"></a>
<a id="l03549"></a>
<a id="l03550"></a>
<a id="foldopen03551"></a>
<a id="l03551"></a>
<a id="l03552"></a>
<a id="l03553"></a>
<a id="l03554"></a>
<a id="l03555"></a>
<a id="l03556"></a>
<a id="foldopen03557"></a>
<a id="l03557"></a>
<a id="l03558"></a>
<a id="l03559"></a>
<a id="l03560"></a>
<a id="l03561"></a>
<a id="l03562"></a>
<a id="l03563"></a>
<a id="l03564"></a>
<a id="foldopen03565"></a>
<a id="l03565"></a>
<a id="l03566"></a>
<a id="l03567"></a>
<a id="l03568"></a>
<a id="l03569"></a>
<a id="l03570"></a>
<a id="l03571"></a>
<a id="l03572"></a>
<a id="l03573"></a>
<a id="l03574"></a>
<a id="l03575"></a>
<a id="l03576"></a>
<a id="l03577"></a>
<a id="l03578"></a>
<a id="foldopen03579"></a>
<a id="l03579"></a>
<a id="l03580"></a>
<a id="l03581"></a>
<a id="l03582"></a>
<a id="l03583"></a>
<a id="l03584"></a>
<a id="foldopen03585"></a>
<a id="l03585"></a>
<a id="l03586"></a>
<a id="l03587"></a>
<a id="l03588"></a>
<a id="l03589"></a>
<a id="l03591"></a>
<a id="l03592"></a>
<a id="l03593"></a>
<a id="l03594"></a>
<a id="l03596"></a>
<a id="l03598"></a>
<a id="l03599"></a>
<a id="l03600"></a>
<a id="l03601"></a>
<a id="l03602"></a>
<a id="l03603"></a>
<a id="l03604"></a>
<a id="l03605"></a>
<a id="foldopen03606"></a>
<a id="l03606"></a>
<a id="l03607"></a>
<a id="l03608"></a>
<a id="l03609"></a>
<a id="l03610"></a>
<a id="l03611"></a>
<a id="l03612"></a>
<a id="l03613"></a>
<a id="l03614"></a>
<a id="foldopen03615"></a>
<a id="l03615"></a>
<a id="l03616"></a>
<a id="l03617"></a>
<a id="l03618"></a>
<a id="l03619"></a>
<a id="l03620"></a>
<a id="l03621"></a>
<a id="foldopen03622"></a>
<a id="l03622"></a>
<a id="l03623"></a>
<a id="l03625"></a>
<a id="l03627"></a>
<a id="l03628"></a>
<a id="l03629"></a>
<a id="l03630"></a>
<a id="foldopen03631"></a>
<a id="l03631"></a>
<a id="l03632"></a>
<a id="l03633"></a>
<a id="l03634"></a>
<a id="l03635"></a>
<a id="l03636"></a>
<a id="l03637"></a>
<a id="l03638"></a>
<a id="l03639"></a>
<a id="foldopen03640"></a>
<a id="l03640"></a>
<a id="l03641"></a>
<a id="l03642"></a>
<a id="l03643"></a>
<a id="l03644"></a>
<a id="l03645"></a>
<a id="l03646"></a>
<a id="l03647"></a>
<a id="l03648"></a>
<a id="foldopen03649"></a>
<a id="l03649"></a>
<a id="l03650"></a>
<a id="l03651"></a>
<a id="l03652"></a>
<a id="l03653"></a>
<a id="l03654"></a>
<a id="foldopen03655"></a>
<a id="l03655"></a>
<a id="l03656"></a>
<a id="l03657"></a>
<a id="l03658"></a>
<a id="l03659"></a>
<a id="l03660"></a>
<a id="foldopen03661"></a>
<a id="l03661"></a>
<a id="l03662"></a>
<a id="l03663"></a>
<a id="l03664"></a>
<a id="l03665"></a>
<a id="l03666"></a>
<a id="l03667"></a>
<a id="l03668"></a>
<a id="l03669"></a>
<a id="l03670"></a>
<a id="l03671"></a>
<a id="l03672"></a>
<a id="l03673"></a>
<a id="l03674"></a>
<a id="foldopen03675"></a>
<a id="l03675"></a>
<a id="l03676"></a>
<a id="l03677"></a>
<a id="l03678"></a>
<a id="l03679"></a>
<a id="l03680"></a>
<a id="foldopen03681"></a>
<a id="l03681"></a>
<a id="l03682"></a>
<a id="l03683"></a>
<a id="l03684"></a>
<a id="l03685"></a>
<a id="l03686"></a>
<a id="foldopen03687"></a>
<a id="l03687"></a>
<a id="l03688"></a>
<a id="l03689"></a>
<a id="l03690"></a>
<a id="l03691"></a>
<a id="l03692"></a>
<a id="l03693"></a>
<a id="l03694"></a>
<a id="l03695"></a>
<a id="l03696"></a>
<a id="l03697"></a>
<a id="l03698"></a>
<a id="l03699"></a>
<a id="l03700"></a>
<a id="l03701"></a>
<a id="l03702"></a>
<a id="l03703"></a>
<a id="l03704"></a>
<a id="l03705"></a>
<a id="l03706"></a>
<a id="l03707"></a>
<a id="l03708"></a>
<a id="l03709"></a>
<a id="l03710"></a>
<a id="l03711"></a>
<a id="l03712"></a>
<a id="l03713"></a>
<a id="l03714"></a>
<a id="l03715"></a>
<a id="foldopen03716"></a>
<a id="l03716"></a>
<a id="l03717"></a>
<a id="l03718"></a>
<a id="l03719"></a>
<a id="l03720"></a>
<a id="l03721"></a>
<a id="l03722"></a>
<a id="l03723"></a>
<a id="l03724"></a>
<a id="l03725"></a>
<a id="l03726"></a>
<a id="l03727"></a>
<a id="l03728"></a>
<a id="l03729"></a>
<a id="l03731"></a>
<a id="foldopen03732"></a>
<a id="l03732"></a>
<a id="l03733"></a>
<a id="l03734"></a>
<a id="l03735"></a>
<a id="l03736"></a>
<a id="l03737"></a>
<a id="foldopen03738"></a>
<a id="l03738"></a>
<a id="l03739"></a>
<a id="l03740"></a>
<a id="l03741"></a>
<a id="l03742"></a>
<a id="l03743"></a>
<a id="l03744"></a>
<a id="l03745"></a>
<a id="l03746"></a>
<a id="l03747"></a>
<a id="l03748"></a>
<a id="foldopen03749"></a>
<a id="l03749"></a>
<a id="l03750"></a>
<a id="l03751"></a>
<a id="l03752"></a>
<a id="l03753"></a>
<a id="l03754"></a>
<a id="l03755"></a>
<a id="l03756"></a>
<a id="l03757"></a>
<a id="l03758"></a>
<a id="l03759"></a>
<a id="foldopen03760"></a>
<a id="l03760"></a>
<a id="l03761"></a>
<a id="l03762"></a>
<a id="l03763"></a>
<a id="l03764"></a>
<a id="l03765"></a>
<a id="l03766"></a>
<a id="foldopen03767"></a>
<a id="l03767"></a>
<a id="l03768"></a>
<a id="l03769"></a>
<a id="l03770"></a>
<a id="l03771"></a>
<a id="l03772"></a>
<a id="l03773"></a>
<a id="l03774"></a>
<a id="foldopen03775"></a>
<a id="l03775"></a>
<a id="l03776"></a>
<a id="l03777"></a>
<a id="l03778"></a>
<a id="l03779"></a>
<a id="l03780"></a>
<a id="l03781"></a>
<a id="l03782"></a>
<a id="l03783"></a>
<a id="foldopen03784"></a>
<a id="l03784"></a>
<a id="l03785"></a>
<a id="l03786"></a>
<a id="l03787"></a>
<a id="l03788"></a>
<a id="l03789"></a>
<a id="l03790"></a>
<a id="l03791"></a>
<a id="l03792"></a>
<a id="l03793"></a>
<a id="l03794"></a>
<a id="l03795"></a>
<a id="l03796"></a>
<a id="l03797"></a>
<a id="l03798"></a>
<a id="l03799"></a>
<a id="foldopen03800"></a>
<a id="l03800"></a>
<a id="l03801"></a>
<a id="l03802"></a>
<a id="l03803"></a>
<a id="l03804"></a>
<a id="foldopen03805"></a>
<a id="l03805"></a>
<a id="l03806"></a>
<a id="l03807"></a>
<a id="l03808"></a>
<a id="l03809"></a>
<a id="l03810"></a>
<a id="l03811"></a>
<a id="l03812"></a>
<a id="l03813"></a>
<a id="l03814"></a>
<a id="l03815"></a>
<a id="l03816"></a>
<a id="l03817"></a>
<a id="l03818"></a>
<a id="foldopen03819"></a>
<a id="l03819"></a>
<a id="l03820"></a>
<a id="l03821"></a>
<a id="l03822"></a>
<a id="l03823"></a>
<a id="l03824"></a>
<a id="l03825"></a>
<a id="l03826"></a>
<a id="l03827"></a>
<a id="l03828"></a>
<a id="l03829"></a>
<a id="l03830"></a>
<a id="l03831"></a>
<a id="l03832"></a>
<a id="l03833"></a>
<a id="l03834"></a>
<a id="l03835"></a>
<a id="foldopen03836"></a>
<a id="l03836"></a>
<a id="l03837"></a>
<a id="l03838"></a>
<a id="l03839"></a>
<a id="l03840"></a>
<a id="l03841"></a>
<a id="l03842"></a>
<a id="l03843"></a>
<a id="l03844"></a>
<a id="l03845"></a>
<a id="l03846"></a>
<a id="foldopen03847"></a>
<a id="l03847"></a>
<a id="l03848"></a>
<a id="l03849"></a>
<a id="l03850"></a>
<a id="l03851"></a>
<a id="l03852"></a>
<a id="l03853"></a>
<a id="l03854"></a>
<a id="l03855"></a>
<a id="l03856"></a>
<a id="l03857"></a>
<a id="l03858"></a>
<a id="l03860"></a>
<a id="l03862"></a>
<a id="l03864"></a>
<a id="l03866"></a>
<a id="l03869"></a>
<a id="l03872"></a>
<a id="l03875"></a>
<a id="l03878"></a>
<a id="l03879"></a>
<a id="l03880"></a>
<a id="foldopen03881"></a>
<a id="l03881"></a>
<a id="l03882"></a>
<a id="l03883"></a>
<a id="l03884"></a>
<a id="l03885"></a>
<a id="l03886"></a>
<a id="l03887"></a>
<a id="l03888"></a>
<a id="l03889"></a>
<a id="l03890"></a>
<a id="l03891"></a>
<a id="l03892"></a>
<a id="l03893"></a>
<a id="l03894"></a>
<a id="l03895"></a>
<a id="l03896"></a>
<a id="l03897"></a>
<a id="l03898"></a>
<a id="l03899"></a>
<a id="l03900"></a>
<a id="foldopen03901"></a>
<a id="l03901"></a>
<a id="l03902"></a>
<a id="l03903"></a>
<a id="l03904"></a>
<a id="l03905"></a>
<a id="l03906"></a>
<a id="l03907"></a>
<a id="l03908"></a>
<a id="l03909"></a>
<a id="l03910"></a>
<a id="l03911"></a>
<a id="l03912"></a>
<a id="l03913"></a>
<a id="l03914"></a>
<a id="l03915"></a>
<a id="foldopen03916"></a>
<a id="l03916"></a>
<a id="l03917"></a>
<a id="l03918"></a>
<a id="l03919"></a>
<a id="l03920"></a>
<a id="l03921"></a>
<a id="l03922"></a>
<a id="l03923"></a>
<a id="l03924"></a>
<a id="l03925"></a>
<a id="l03926"></a>
<a id="l03927"></a>
<a id="l03928"></a>
<a id="l03929"></a>
<a id="l03930"></a>
<a id="l03931"></a>
<a id="l03932"></a>
<a id="foldopen03933"></a>
<a id="l03933"></a>
<a id="l03934"></a>
<a id="l03935"></a>
<a id="l03936"></a>
<a id="l03937"></a>
<a id="l03938"></a>
<a id="foldopen03939"></a>
<a id="l03939"></a>
<a id="l03940"></a>
<a id="l03941"></a>
<a id="l03942"></a>
<a id="l03943"></a>
<a id="l03944"></a>
<a id="l03945"></a>
<a id="l03946"></a>
<a id="l03947"></a>
<a id="l03948"></a>
<a id="l03949"></a>
<a id="l03950"></a>
<a id="l03951"></a>
<a id="l03952"></a>
<a id="l03953"></a>
<a id="foldopen03954"></a>
<a id="l03954"></a>
<a id="l03955"></a>
<a id="l03956"></a>
<a id="l03957"></a>
<a id="l03958"></a>
<a id="l03959"></a>
<a id="foldopen03960"></a>
<a id="l03960"></a>
<a id="l03961"></a>
<a id="l03962"></a>
<a id="l03963"></a>
<a id="l03964"></a>
<a id="l03965"></a>
<a id="l03966"></a>
<a id="l03967"></a>
<a id="l03968"></a>
<a id="l03969"></a>
<a id="l03970"></a>
<a id="l03971"></a>
<a id="foldopen03972"></a>
<a id="l03972"></a>
<a id="l03973"></a>
<a id="l03974"></a>
<a id="l03975"></a>
<a id="l03976"></a>
<a id="l03977"></a>
<a id="l03980"></a>
<a id="l03981"></a>
<a id="l03982"></a>
<a id="l03983"></a>
<a id="l03984"></a>
<a id="l03985"></a>
<a id="l03986"></a>
<a id="l03987"></a>
<a id="foldopen03988"></a>
<a id="l03988"></a>
<a id="l03989"></a>
<a id="l03990"></a>
<a id="l03991"></a>
<a id="l03992"></a>
<a id="l03993"></a>
<a id="l03994"></a>
<a id="l03995"></a>
<a id="l03996"></a>
<a id="l03997"></a>
<a id="l03998"></a>
<a id="foldopen03999"></a>
<a id="l03999"></a>
<a id="l04000"></a>
<a id="l04001"></a>
<a id="l04002"></a>
<a id="l04003"></a>
<a id="l04004"></a>
<a id="l04005"></a>
<a id="l04006"></a>
<a id="l04007"></a>
<a id="l04008"></a>
<a id="l04009"></a>
<a id="l04010"></a>
<a id="l04011"></a>
<a id="l04012"></a>
<a id="l04013"></a>
<a id="l04014"></a>
<a id="l04016"></a>
<a id="l04017"></a>
<a id="l04018"></a>
<a id="l04019"></a>
<a id="l04020"></a>
<a id="l04021"></a>
<a id="foldopen04022"></a>
<a id="l04022"></a>
<a id="l04023"></a>
<a id="l04024"></a>
<a id="l04025"></a>
<a id="l04026"></a>
<a id="l04027"></a>
<a id="l04028"></a>
<a id="l04029"></a>
<a id="l04030"></a>
<a id="l04031"></a>
<a id="foldopen04032"></a>
<a id="l04032"></a>
<a id="l04033"></a>
<a id="l04034"></a>
<a id="l04035"></a>
<a id="l04036"></a>
<a id="l04037"></a>
<a id="l04038"></a>
<a id="l04039"></a>
<a id="l04040"></a>
<a id="l04041"></a>
<a id="l04042"></a>
<a id="l04043"></a>
<a id="l04044"></a>
<a id="l04045"></a>
<a id="l04046"></a>
<a id="l04047"></a>
<a id="l04048"></a>
<a id="l04049"></a>
<a id="l04050"></a>
<a id="l04051"></a>
<a id="l04052"></a>
<a id="l04053"></a>
<a id="l04054"></a>
<a id="l04055"></a>
<a id="l04056"></a>
<a id="l04057"></a>
<a id="l04058"></a>
<a id="l04059"></a>
<a id="l04060"></a>
<a id="l04061"></a>
<a id="l04062"></a>
<a id="foldopen04063"></a>
<a id="l04063"></a>
<a id="l04064"></a>
<a id="l04065"></a>
<a id="l04066"></a>
<a id="l04067"></a>
<a id="l04068"></a>
<a id="l04069"></a>
<a id="l04070"></a>
<a id="l04071"></a>
<a id="l04072"></a>
<a id="l04073"></a>
<a id="l04074"></a>
<a id="l04075"></a>
<a id="l04076"></a>
<a id="l04077"></a>
<a id="l04078"></a>
<a id="l04079"></a>
<a id="l04080"></a>
<a id="l04081"></a>
<a id="l04082"></a>
<a id="l04083"></a>
<a id="l04084"></a>
<a id="l04085"></a>
<a id="l04086"></a>
<a id="l04087"></a>
<a id="l04088"></a>
<a id="l04090"></a>
<a id="l04091"></a>
<a id="l04092"></a>
<a id="l04093"></a>
<a id="l04094"></a>
<a id="l04095"></a>
<a id="l04096"></a>
<a id="l04097"></a>
<a id="l04098"></a>
<a id="l04099"></a>
<a id="l04100"></a>
<a id="l04101"></a>
<a id="l04102"></a>
<a id="l04103"></a>
<a id="l04104"></a>
<a id="l04105"></a>
<a id="l04106"></a>
<a id="l04107"></a>
<a id="l04108"></a>
<a id="l04109"></a>
<a id="l04110"></a>
<a id="l04111"></a>
<a id="l04112"></a>
<a id="l04113"></a>
<a id="l04114"></a>
<a id="l04115"></a>
<a id="l04116"></a>
<a id="l04117"></a>
<a id="l04118"></a>
<a id="l04119"></a>
<a id="l04120"></a>
<a id="l04121"></a>
<a id="l04122"></a>
<a id="l04123"></a>
<a id="l04124"></a>
<a id="l04125"></a>
<a id="l04126"></a>
<a id="l04127"></a>
<a id="l04128"></a>
<a id="foldopen04129"></a>
<a id="l04129"></a>
<a id="l04130"></a>
<a id="l04131"></a>
<a id="l04132"></a>
<a id="l04133"></a>
<a id="l04134"></a>
<a id="l04135"></a>
<a id="l04136"></a>
<a id="l04137"></a>
<a id="l04138"></a>
<a id="l04139"></a>
<a id="l04140"></a>
<a id="l04141"></a>
<a id="l04142"></a>
<a id="l04143"></a>
<a id="l04144"></a>
<a id="l04145"></a>
<a id="l04146"></a>
<a id="l04147"></a>
<a id="l04148"></a>
<a id="l04149"></a>
<a id="l04150"></a>
<a id="l04151"></a>
<a id="l04152"></a>
<a id="l04153"></a>
<a id="l04155"></a>
<a id="l04156"></a>
<a id="foldopen04158"></a>
<a id="l04158"></a>
<a id="l04160"></a>
<a id="l04162"></a>
<a id="l04164"></a>
<a id="l04166"></a>
<a id="l04168"></a>
<a id="l04170"></a>
<a id="l04172"></a>
<a id="l04174"></a>
<a id="l04176"></a>
<a id="l04178"></a>
<a id="l04180"></a>
<a id="l04182"></a>
<a id="l04184"></a>
<a id="l04186"></a>
<a id="l04188"></a>
<a id="l04190"></a>
<a id="l04192"></a>
<a id="l04194"></a>
<a id="l04196"></a>
<a id="l04198"></a>
<a id="l04200"></a>
<a id="l04202"></a>
<a id="l04204"></a>
<a id="l04206"></a>
<a id="l04207"></a>
<a id="l04208"></a>
<a id="l04209"></a>
<a id="foldopen04210"></a>
<a id="l04210"></a>
<a id="l04211"></a>
<a id="l04212"></a>
<a id="l04213"></a>
<a id="l04214"></a>
<a id="l04215"></a>
<a id="l04216"></a>
<a id="l04217"></a>
<a id="l04218"></a>
<a id="l04219"></a>
<a id="foldopen04220"></a>
<a id="l04220"></a>
<a id="l04221"></a>
<a id="l04222"></a>
<a id="l04223"></a>
<a id="l04224"></a>
<a id="l04225"></a>
<a id="foldopen04226"></a>
<a id="l04226"></a>
<a id="l04227"></a>
<a id="l04228"></a>
<a id="l04229"></a>
<a id="l04230"></a>
<a id="l04231"></a>
<a id="l04232"></a>
<a id="l04233"></a>
<a id="l04234"></a>
<a id="l04235"></a>
<a id="l04236"></a>
<a id="l04237"></a>
<a id="l04238"></a>
<a id="l04239"></a>
<a id="l04240"></a>
<a id="l04241"></a>
<a id="l04242"></a>
<a id="l04243"></a>
<a id="l04244"></a>
<a id="l04246"></a>
<a id="l04247"></a>
<a id="l04248"></a>
<a id="l04249"></a>
<a id="l04250"></a>
<a id="l04251"></a>
<a id="l04252"></a>
<a id="l04253"></a>
<a id="l04254"></a>
<a id="l04255"></a>
<a id="l04256"></a>
<a id="l04257"></a>
<a id="l04258"></a>
<a id="l04259"></a>
<a id="l04260"></a>
<a id="l04261"></a>
<a id="l04262"></a>
<a id="l04263"></a>
<a id="l04264"></a>
<a id="l04265"></a>
<a id="l04266"></a>
<a id="l04267"></a>
<a id="l04268"></a>
<a id="l04269"></a>
<a id="l04270"></a>
<a id="l04271"></a>
<a id="l04272"></a>
<a id="l04273"></a>
<a id="l04274"></a>
<a id="l04275"></a>
<a id="l04276"></a>
<a id="l04277"></a>
<a id="l04278"></a>
<a id="l04279"></a>
<a id="l04280"></a>
<a id="l04281"></a>
<a id="l04282"></a>
<a id="l04283"></a>
<a id="l04284"></a>
<a id="l04285"></a>
<a id="l04286"></a>
<a id="l04287"></a>
<a id="l04288"></a>
<a id="l04289"></a>
<a id="l04290"></a>
<a id="l04291"></a>
<a id="l04292"></a>
<a id="l04293"></a>
<a id="l04294"></a>
<a id="l04295"></a>
<a id="l04296"></a>
<a id="l04297"></a>
<a id="l04298"></a>
<a id="l04299"></a>
<a id="l04300"></a>
<a id="l04301"></a>
<a id="l04302"></a>
<a id="l04303"></a>
<a id="l04304"></a>
<a id="l04305"></a>
<a id="l04306"></a>
<a id="l04307"></a>
<a id="l04308"></a>
<a id="l04309"></a>
<a id="l04310"></a>
<a id="l04311"></a>
<a id="l04312"></a>
<a id="l04313"></a>
<a id="l04314"></a>
<a id="l04315"></a>
<a id="l04316"></a>
<a id="foldopen04318"></a>
<a id="l04318"></a>
<a id="l04319"></a>
<a id="l04320"></a>
<a id="l04321"></a>
<a id="l04322"></a>
<a id="l04323"></a>
<a id="l04324"></a>
<a id="l04325"></a>
<a id="l04326"></a>
<a id="l04327"></a>
<a id="l04328"></a>
<a id="l04329"></a>
<a id="l04330"></a>
<a id="foldopen04332"></a>
<a id="l04332"></a>
<a id="l04333"></a>
<a id="l04334"></a>
<a id="l04335"></a>
<a id="l04336"></a>
<a id="l04337"></a>
<a id="l04338"></a>
<a id="l04339"></a>
<a id="l04340"></a>
<a id="l04341"></a>
<a id="l04342"></a>
<a id="l04343"></a>
<a id="foldopen04345"></a>
<a id="l04345"></a>
<a id="l04346"></a>
<a id="l04347"></a>
<a id="l04348"></a>
<a id="l04349"></a>
<a id="l04350"></a>
<a id="l04351"></a>
<a id="l04352"></a>
<a id="l04353"></a>
<a id="l04354"></a>
<a id="l04355"></a>
<a id="l04356"></a>
<a id="l04357"></a>
<a id="l04358"></a>
<a id="l04359"></a>
<a id="l04360"></a>
<a id="l04361"></a>
<a id="foldopen04363"></a>
<a id="l04363"></a>
<a id="l04364"></a>
<a id="l04365"></a>
<a id="l04366"></a>
<a id="l04367"></a>
<a id="l04368"></a>
<a id="l04369"></a>
<a id="l04370"></a>
<a id="l04371"></a>
<a id="l04372"></a>
<a id="l04373"></a>
<a id="l04374"></a>
<a id="l04375"></a>
<a id="l04376"></a>
<a id="l04377"></a>
<a id="l04378"></a>
<a id="l04379"></a>
<a id="l04380"></a>
<a id="l04381"></a>
<a id="l04382"></a>
<a id="foldopen04384"></a>
<a id="l04384"></a>
<a id="l04385"></a>
<a id="l04386"></a>
<a id="l04387"></a>
<a id="l04388"></a>
<a id="l04389"></a>
<a id="l04390"></a>
<a id="l04391"></a>
<a id="l04392"></a>
<a id="l04393"></a>
<a id="l04394"></a>
<a id="foldopen04396"></a>
<a id="l04396"></a>
<a id="l04397"></a>
<a id="l04398"></a>
<a id="l04399"></a>
<a id="l04400"></a>
<a id="foldopen04402"></a>
<a id="l04402"></a>
<a id="l04403"></a>
<a id="l04404"></a>
<a id="l04405"></a>
<a id="l04406"></a>
<a id="l04407"></a>
<a id="l04408"></a>
<a id="l04409"></a>
<a id="l04410"></a>
<a id="l04411"></a>
<a id="l04412"></a>
<a id="l04413"></a>
<a id="l04414"></a>
<a id="l04415"></a>
<a id="l04416"></a>
<a id="l04417"></a>
<a id="l04418"></a>
<a id="l04419"></a>
<a id="l04420"></a>
<a id="foldopen04422"></a>
<a id="l04422"></a>
<a id="l04423"></a>
<a id="l04424"></a>
<a id="l04425"></a>
<a id="l04426"></a>
<a id="l04427"></a>
<a id="l04428"></a>
<a id="l04429"></a>
<a id="l04430"></a>
<a id="l04431"></a>
<a id="l04432"></a>
<a id="l04433"></a>
<a id="l04434"></a>
<a id="l04435"></a>
<a id="l04436"></a>
<a id="l04437"></a>
<a id="l04438"></a>
<a id="l04439"></a>
<a id="l04440"></a>
<a id="l04441"></a>
<a id="l04442"></a>
<a id="foldopen04443"></a>
<a id="l04443"></a>
<a id="l04444"></a>
<a id="l04445"></a>
<a id="l04446"></a>
<a id="l04447"></a>
<a id="l04448"></a>
<a id="l04449"></a>
<a id="foldopen04450"></a>
<a id="l04450"></a>
<a id="l04451"></a>
<a id="l04452"></a>
<a id="l04453"></a>
<a id="l04454"></a>
<a id="l04455"></a>
<a id="l04456"></a>
<a id="l04457"></a>
<a id="l04458"></a>
<a id="l04459"></a>
<a id="l04460"></a>
<a id="l04461"></a>
<a id="l04462"></a>
<a id="l04463"></a>
<a id="l04464"></a>
<a id="l04465"></a>
<a id="l04466"></a>
<a id="l04467"></a>
<a id="l04468"></a>
<a id="l04469"></a>
<a id="l04470"></a>
<a id="l04471"></a>
<a id="l04472"></a>
<a id="foldopen04473"></a>
<a id="l04473"></a>
<a id="l04474"></a>
<a id="l04475"></a>
<a id="l04476"></a>
<a id="l04477"></a>
<a id="l04478"></a>
<a id="l04479"></a>
<a id="l04480"></a>
<a id="l04481"></a>
<a id="l04482"></a>
<a id="l04483"></a>
<a id="l04484"></a>
<a id="l04485"></a>
<a id="l04486"></a>
<a id="l04487"></a>
<a id="l04488"></a>
<a id="l04489"></a>
<a id="l04490"></a>
<a id="foldopen04491"></a>
<a id="l04491"></a>
<a id="l04492"></a>
<a id="l04493"></a>
<a id="l04494"></a>
<a id="l04495"></a>
<a id="foldopen04496"></a>
<a id="l04496"></a>
<a id="l04497"></a>
<a id="l04498"></a>
<a id="l04499"></a>
<a id="l04500"></a>
<a id="l04501"></a>
<a id="l04502"></a>
<a id="l04503"></a>
<a id="l04504"></a>
<a id="l04505"></a>
<a id="l04506"></a>
<a id="l04507"></a>
<a id="l04508"></a>
<a id="l04509"></a>
<a id="l04510"></a>
<a id="l04511"></a>
<a id="l04512"></a>
<a id="foldopen04513"></a>
<a id="l04513"></a>
<a id="l04514"></a>
<a id="l04515"></a>
<a id="l04516"></a>
<a id="l04517"></a>
<a id="l04518"></a>
<a id="l04519"></a>
<a id="l04520"></a>
<a id="l04521"></a>
<a id="l04522"></a>
<a id="foldopen04523"></a>
<a id="l04523"></a>
<a id="l04524"></a>
<a id="l04525"></a>
<a id="l04526"></a>
<a id="l04527"></a>
<a id="l04528"></a>
<a id="l04529"></a>
<a id="l04530"></a>
<a id="l04531"></a>
<a id="l04532"></a>
<a id="l04533"></a>
<a id="l04534"></a>
<a id="l04535"></a>
<a id="l04536"></a>
<a id="l04537"></a>
<a id="l04538"></a>
<a id="l04539"></a>
<a id="l04540"></a>
<a id="l04541"></a>
<a id="l04542"></a>
<a id="l04543"></a>
<a id="l04544"></a>
<a id="l04545"></a>
<a id="l04546"></a>
<a id="l04547"></a>
<a id="l04548"></a>
<a id="l04549"></a>
<a id="l04550"></a>
<a id="l04551"></a>
<a id="l04552"></a>
<a id="l04554"></a>
<a id="l04555"></a>
<a id="l04556"></a>
<a id="l04557"></a>
<a id="l04558"></a>
<a id="l04559"></a>
<a id="l04560"></a>
<a id="l04561"></a>
<a id="l04562"></a>
<a id="l04563"></a>
<a id="l04564"></a>
<a id="l04565"></a>
<a id="l04566"></a>
<a id="l04567"></a>
<a id="l04568"></a>
<a id="l04569"></a>
<a id="l04570"></a>
<a id="l04571"></a>
<a id="l04572"></a>
<a id="l04573"></a>
<a id="l04574"></a>
<a id="l04575"></a>
<a id="l04576"></a>
<a id="l04577"></a>
<a id="l04578"></a>
<a id="l04579"></a>
<a id="l04580"></a>
<a id="l04581"></a>
<a id="l04582"></a>
<a id="l04583"></a>
<a id="l04584"></a>
<a id="l04585"></a>
<a id="l04586"></a>
<a id="l04587"></a>
<a id="l04588"></a>
<a id="l04589"></a>
<a id="l04590"></a>
<a id="l04591"></a>
<a id="l04592"></a>
<a id="l04593"></a>
<a id="l04594"></a>
<a id="l04595"></a>
<a id="l04596"></a>
<a id="l04597"></a>
<a id="l04598"></a>
<a id="l04599"></a>
<a id="l04600"></a>
<a id="l04601"></a>
<a id="l04602"></a>
<a id="l04603"></a>
<a id="l04604"></a>
<a id="l04605"></a>
<a id="l04606"></a>
<a id="l04607"></a>
<a id="l04608"></a>
<a id="l04609"></a>
<a id="l04610"></a>
<a id="l04611"></a>
<a id="l04612"></a>
<a id="l04613"></a>
<a id="l04614"></a>
<a id="l04615"></a>
<a id="l04616"></a>
<a id="l04617"></a>
<a id="l04618"></a>
<a id="l04619"></a>
<a id="l04620"></a>
<a id="l04621"></a>
<a id="l04622"></a>
<a id="l04623"></a>
<a id="l04624"></a>
<a id="l04625"></a>
<a id="l04626"></a>
<a id="l04627"></a>
<a id="l04628"></a>
<a id="l04629"></a>
<a id="l04630"></a>
<a id="l04631"></a>
<a id="l04632"></a>
<a id="l04633"></a>
<a id="l04634"></a>
<a id="l04635"></a>
<a id="l04636"></a>
<a id="l04637"></a>
<a id="l04638"></a>
<a id="l04639"></a>
<a id="l04641"></a>
<a id="l04642"></a>
<a id="l04644"></a>
<a id="l04645"></a>
<a id="l04646"></a>
<a id="l04647"></a>
<a id="l04648"></a>
<a id="l04649"></a>
<a id="l04650"></a>
<a id="l04651"></a>
<a id="l04652"></a>
<a id="l04653"></a>
<a id="l04654"></a>
<a id="l04655"></a>
<a id="l04656"></a>
<a id="l04657"></a>
<a id="l04658"></a>
<a id="l04659"></a>
<a id="l04660"></a>
<a id="l04661"></a>
<a id="l04662"></a>
<a id="l04663"></a>
<a id="l04664"></a>
<a id="l04665"></a>
<a id="l04666"></a>
<a id="l04667"></a>
<a id="l04668"></a>
<a id="l04669"></a>
<a id="l04670"></a>
<a id="l04671"></a>
<a id="l04672"></a>
<a id="l04673"></a>
<a id="l04674"></a>
<a id="l04675"></a>
<a id="l04676"></a>
<a id="l04677"></a>
<a id="l04678"></a>
<a id="l04679"></a>
<a id="l04680"></a>
<a id="l04681"></a>
<a id="l04682"></a>
<a id="l04683"></a>
<a id="l04684"></a>
<a id="l04686"></a>
<a id="l04687"></a>
<a id="l04688"></a>
<a id="l04689"></a>
<a id="l04690"></a>
<a id="l04691"></a>
<a id="l04692"></a>
<a id="l04693"></a>
<a id="l04694"></a>
<a id="l04695"></a>
<a id="l04696"></a>
<a id="l04697"></a>
<a id="l04698"></a>
<a id="l04699"></a>
<a id="l04700"></a>
<a id="l04701"></a>
<a id="l04702"></a>
<a id="l04703"></a>
<a id="l04704"></a>
<a id="l04705"></a>
<a id="l04706"></a>
<a id="l04707"></a>
<a id="l04708"></a>
<a id="l04709"></a>
<a id="l04710"></a>
<a id="l04711"></a>
<a id="l04712"></a>
<a id="l04713"></a>
<a id="l04714"></a>
<a id="l04715"></a>
<a id="l04716"></a>
<a id="l04717"></a>
<a id="l04718"></a>
<a id="l04719"></a>
<a id="aaddr_8h_html"></a>
<a id="ahci__types_8h_html_a08260407c93741e254a4427ba42c274d"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructbt__addr__le__t_html"></a>
<a id="astructbt__addr__t_html"></a>
<a id="astructbt__hci__acl__hdr_html"></a>
<a id="astructbt__hci__acl__hdr_html_a8c88ef62a848699e06c49f97e1169363"></a>
<a id="astructbt__hci__acl__hdr_html_af55b9c9256f35ada5786e9e5dd1d01bf"></a>
<a id="astructbt__hci__cis__params__test_html"></a>
<a id="astructbt__hci__cis__params__test_html_a0a215b4dffac2aae4ae4310c54de073e"></a>
<a id="astructbt__hci__cis__params__test_html_a98a120efb1495dd90858bef45eb95891"></a>
<a id="astructbt__hci__cis__params__test_html_aa7ba56fb91718d43ca30ff643757e08e"></a>
<a id="astructbt__hci__cis__params__test_html_ab636126046023a329451673c57b4ce96"></a>
<a id="astructbt__hci__cis__params__test_html_abce4bd6045642b4d29668865655f1548"></a>
<a id="astructbt__hci__cis__params__test_html_ac66b7183d8148250246f17a157dc3d29"></a>
<a id="astructbt__hci__cis__params__test_html_ad0cc6d393a536cb3cd83d456b950fc52"></a>
<a id="astructbt__hci__cis__params__test_html_adc092a44b58bcc78f3dfe88528ca724c"></a>
<a id="astructbt__hci__cis__params__test_html_adf5dda2be46f3c2c1a1fe398672416ff"></a>
<a id="astructbt__hci__cis__params__test_html_aefeca493efe0141590570e8a44bb8f8d"></a>
<a id="astructbt__hci__cis__params_html"></a>
<a id="astructbt__hci__cis__params_html_a18bc8e4b531d9fd16f18e10a0d931f6c"></a>
<a id="astructbt__hci__cis__params_html_a5a5fcd9276d912446fe84d875ae74c2f"></a>
<a id="astructbt__hci__cis__params_html_a6dcfca11d7f827b1b7a62b507620d4de"></a>
<a id="astructbt__hci__cis__params_html_a8a85b914ba5585c6b362da3deb8d42d9"></a>
<a id="astructbt__hci__cis__params_html_aa7fa628692f959db63788c6580cc5c66"></a>
<a id="astructbt__hci__cis__params_html_ad55e197ccb70c83fcd4c1c6ba485f468"></a>
<a id="astructbt__hci__cis__params_html_ae2bffbaf0c4dde9144a7887177b3ffdb"></a>
<a id="astructbt__hci__cis_html"></a>
<a id="astructbt__hci__cis_html_a754c3c75c0ad13a11d89fa3347112e2c"></a>
<a id="astructbt__hci__cis_html_a84165d526c10a91fa42d306276d97c74"></a>
<a id="astructbt__hci__cmd__hdr_html"></a>
<a id="astructbt__hci__cmd__hdr_html_a09c63aab094ca0f39bab44708fdb83e4"></a>
<a id="astructbt__hci__cmd__hdr_html_afe2a97da8b473cafd3cc4e5e52dadf93"></a>
<a id="astructbt__hci__codec__capability__info_html"></a>
<a id="astructbt__hci__codec__capability__info_html_a24516347742a8fd9f3386d78b66a4e81"></a>
<a id="astructbt__hci__codec__capability__info_html_ac53f02f2abdb832ed82da35a36abc323"></a>
<a id="astructbt__hci__cp__accept__conn__req_html"></a>
<a id="astructbt__hci__cp__accept__conn__req_html_a95e445018d1b9da5a914f0845bb9dbad"></a>
<a id="astructbt__hci__cp__accept__conn__req_html_aa2954d98fdd42882cf7095e4ce7a3dc5"></a>
<a id="astructbt__hci__cp__accept__sync__conn__req_html"></a>
<a id="astructbt__hci__cp__accept__sync__conn__req_html_a4ba6dffd840ef868524b490d227fd085"></a>
<a id="astructbt__hci__cp__accept__sync__conn__req_html_a53fe4c6d61dbb99f99aa445b2c47a8ef"></a>
<a id="astructbt__hci__cp__accept__sync__conn__req_html_a6a5a56d3a9d1a6d1064e7bd4c9fd333e"></a>
<a id="astructbt__hci__cp__accept__sync__conn__req_html_ab5d9c27ebdf45fb54b0c6330b5b095be"></a>
<a id="astructbt__hci__cp__accept__sync__conn__req_html_ab5ece67c5a1e62fc4124556eef743c26"></a>
<a id="astructbt__hci__cp__accept__sync__conn__req_html_aceda6dbd3e221ad080850e9635886a86"></a>
<a id="astructbt__hci__cp__accept__sync__conn__req_html_adba31b588bf12e852cc43b85c006aaa3"></a>
<a id="astructbt__hci__cp__auth__requested_html"></a>
<a id="astructbt__hci__cp__auth__requested_html_a079490f8f8569e281ce16f13847cbf33"></a>
<a id="astructbt__hci__cp__change__conn__packet__type_html"></a>
<a id="astructbt__hci__cp__change__conn__packet__type_html_a082e5dae5f08a332cf6a1dd23917d87f"></a>
<a id="astructbt__hci__cp__change__conn__packet__type_html_a0b825740b5ff47db5bfaaea7950e7d53"></a>
<a id="astructbt__hci__cp__codec__id_html"></a>
<a id="astructbt__hci__cp__codec__id_html_a70296440c202544af11db2dc8e80fc5b"></a>
<a id="astructbt__hci__cp__codec__id_html_a98fd438270a64d843fa27c7c196645df"></a>
<a id="astructbt__hci__cp__codec__id_html_aec80c74b12edb9c63330cc5a404eed5d"></a>
<a id="astructbt__hci__cp__configure__data__path_html"></a>
<a id="astructbt__hci__cp__configure__data__path_html_a2573fe029e1774bf5fa7e8cffff08cec"></a>
<a id="astructbt__hci__cp__configure__data__path_html_a528ba2bd5a220d1b7db064f8b51a8718"></a>
<a id="astructbt__hci__cp__configure__data__path_html_a92967e6b5258b2acd6d82bfbfb8b7940"></a>
<a id="astructbt__hci__cp__configure__data__path_html_aa79c4aa6603b09f49a8c7f216f135e6e"></a>
<a id="astructbt__hci__cp__connect__cancel_html"></a>
<a id="astructbt__hci__cp__connect__cancel_html_a2adaf1b708689525e44e9a9572f5f357"></a>
<a id="astructbt__hci__cp__connect_html"></a>
<a id="astructbt__hci__cp__connect_html_a35b0e1f73f696aae2ca519e16d7bb668"></a>
<a id="astructbt__hci__cp__connect_html_a652a4e01641893a8588110dc505ceea0"></a>
<a id="astructbt__hci__cp__connect_html_a6f0753aad19d4c9591fa74152d151aa9"></a>
<a id="astructbt__hci__cp__connect_html_a7a3d772bfd4c83236f9f1ad657e33f17"></a>
<a id="astructbt__hci__cp__connect_html_ac379ec381ad4cf6760750203924e5dda"></a>
<a id="astructbt__hci__cp__connect_html_aef01fcac1b9792353bd8095e6911d6c3"></a>
<a id="astructbt__hci__cp__disconnect_html"></a>
<a id="astructbt__hci__cp__disconnect_html_a8e10edb1e700c1ef38f39bf20b9b374f"></a>
<a id="astructbt__hci__cp__disconnect_html_a9cb5bcd135082c37a19cce57ffa123ff"></a>
<a id="astructbt__hci__cp__exit__sniff__mode_html"></a>
<a id="astructbt__hci__cp__exit__sniff__mode_html_a706cc1a951f21889a28e0b555587bb98"></a>
<a id="astructbt__hci__cp__host__buffer__size_html"></a>
<a id="astructbt__hci__cp__host__buffer__size_html_a07039a81ba81c700a26009ea407744b6"></a>
<a id="astructbt__hci__cp__host__buffer__size_html_a1b1d8c7f60ecbb13699b815bc8fca550"></a>
<a id="astructbt__hci__cp__host__buffer__size_html_a8240837fecc7c50461724b697f0eda47"></a>
<a id="astructbt__hci__cp__host__buffer__size_html_a943252480194e1a8608951be08b6b91c"></a>
<a id="astructbt__hci__cp__host__num__completed__packets_html"></a>
<a id="astructbt__hci__cp__host__num__completed__packets_html_a127f146b4967de49bc74b90ce1643eb7"></a>
<a id="astructbt__hci__cp__host__num__completed__packets_html_a43a42e52757de9ec307e8a828dff416f"></a>
<a id="astructbt__hci__cp__io__capability__neg__reply_html"></a>
<a id="astructbt__hci__cp__io__capability__neg__reply_html_a82c54e5ad7fd4a6d81952832ae4de373"></a>
<a id="astructbt__hci__cp__io__capability__neg__reply_html_a8dba05bc84de2573eaea43ea9e428015"></a>
<a id="astructbt__hci__cp__io__capability__reply_html"></a>
<a id="astructbt__hci__cp__io__capability__reply_html_a0995c81ba1f653c59bda9a444fb17915"></a>
<a id="astructbt__hci__cp__io__capability__reply_html_a8983418dca3a7725f3b113a4d0ee177e"></a>
<a id="astructbt__hci__cp__io__capability__reply_html_ac002ea0b276200a15d603b5ac83666e5"></a>
<a id="astructbt__hci__cp__io__capability__reply_html_afbe2bc0c1dcc0791a98068b052aea1f2"></a>
<a id="astructbt__hci__cp__le__accept__cis_html"></a>
<a id="astructbt__hci__cp__le__accept__cis_html_aec6a6c80403d5827df10cd8722bc12e4"></a>
<a id="astructbt__hci__cp__le__add__dev__to__fal_html"></a>
<a id="astructbt__hci__cp__le__add__dev__to__fal_html_a11ec9f3cd9b80f34094e70d8eeb13be3"></a>
<a id="astructbt__hci__cp__le__add__dev__to__per__adv__list_html"></a>
<a id="astructbt__hci__cp__le__add__dev__to__per__adv__list_html_a97d9c5dd0cc4b3ab7f6ebfec206b7407"></a>
<a id="astructbt__hci__cp__le__add__dev__to__per__adv__list_html_ad93d72bfa7e4123ee9728f6bf73b69df"></a>
<a id="astructbt__hci__cp__le__add__dev__to__rl_html"></a>
<a id="astructbt__hci__cp__le__add__dev__to__rl_html_a3daf2041f04381a56c2cbcd4bb33f4c0"></a>
<a id="astructbt__hci__cp__le__add__dev__to__rl_html_ab5caa38e6eeab09b4a69084b1890317b"></a>
<a id="astructbt__hci__cp__le__add__dev__to__rl_html_aedc27c868a7a4cbd3c175f67db4e3242"></a>
<a id="astructbt__hci__cp__le__big__create__sync_html"></a>
<a id="astructbt__hci__cp__le__big__create__sync_html_a053475c3af12e6e37dc4befcf634d68f"></a>
<a id="astructbt__hci__cp__le__big__create__sync_html_a37050e3eb914ff06495695d44c3fdb50"></a>
<a id="astructbt__hci__cp__le__big__create__sync_html_a482edf3326e2dd720b14a03609c1256a"></a>
<a id="astructbt__hci__cp__le__big__create__sync_html_a55e83bc3722ce2dbf943879a80ef2872"></a>
<a id="astructbt__hci__cp__le__big__create__sync_html_a6692dae077ce1ce4f31bc94b9d391afd"></a>
<a id="astructbt__hci__cp__le__big__create__sync_html_a6d1050c2a0522be215d82d3874fed4b6"></a>
<a id="astructbt__hci__cp__le__big__create__sync_html_a70b031f24cdf231e5c168b155517eae0"></a>
<a id="astructbt__hci__cp__le__big__create__sync_html_a7efae2c8dc46d13fb2abca677ac152b0"></a>
<a id="astructbt__hci__cp__le__big__terminate__sync_html"></a>
<a id="astructbt__hci__cp__le__big__terminate__sync_html_ad7e4de2a9a3222c1bb8fa048cacd06fa"></a>
<a id="astructbt__hci__cp__le__conn__cte__req__enable_html"></a>
<a id="astructbt__hci__cp__le__conn__cte__req__enable_html_a4d4e41bbe95457ce5e8ad68ffeb85200"></a>
<a id="astructbt__hci__cp__le__conn__cte__req__enable_html_a5a7443a86e770de4bf7292d813e966e7"></a>
<a id="astructbt__hci__cp__le__conn__cte__req__enable_html_a956a1a8794b75e962d03cdcf81847cfc"></a>
<a id="astructbt__hci__cp__le__conn__cte__req__enable_html_aaf38e3d5664d81ae7ac8d3b1bb03c646"></a>
<a id="astructbt__hci__cp__le__conn__cte__req__enable_html_af340b3b97f9fb12c24baa38415620b44"></a>
<a id="astructbt__hci__cp__le__conn__cte__rsp__enable_html"></a>
<a id="astructbt__hci__cp__le__conn__cte__rsp__enable_html_a9d78072143513020620e02a744d4fa9b"></a>
<a id="astructbt__hci__cp__le__conn__cte__rsp__enable_html_ae5eaaae211732d772ea53f3936ab32d2"></a>
<a id="astructbt__hci__cp__le__conn__param__req__neg__reply_html"></a>
<a id="astructbt__hci__cp__le__conn__param__req__neg__reply_html_a0040e4a50c5c5479b539eb0bafb7b305"></a>
<a id="astructbt__hci__cp__le__conn__param__req__neg__reply_html_a8c283ac844805224b1ffeb9801e8b14b"></a>
<a id="astructbt__hci__cp__le__conn__param__req__reply_html"></a>
<a id="astructbt__hci__cp__le__conn__param__req__reply_html_a10547c7d4836980947d17bbde0d75a51"></a>
<a id="astructbt__hci__cp__le__conn__param__req__reply_html_a512d605d5c4aacf81b78794fcf260abf"></a>
<a id="astructbt__hci__cp__le__conn__param__req__reply_html_a8c76816cc230387c249ab8e05c402964"></a>
<a id="astructbt__hci__cp__le__conn__param__req__reply_html_a932e6a3a45ec0409656325f7246d5d7e"></a>
<a id="astructbt__hci__cp__le__conn__param__req__reply_html_aa3b938afe13d4e05806fb6cdfab5cb14"></a>
<a id="astructbt__hci__cp__le__conn__param__req__reply_html_aed58f9aa722a284ae39df842394c06cf"></a>
<a id="astructbt__hci__cp__le__conn__param__req__reply_html_af25a3f226ceccbe19e7f1482ed5f141e"></a>
<a id="astructbt__hci__cp__le__create__big__test_html"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a2652e0f340f13635a5da6335ec43e801"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a2f2eaa258463dd51a9f6042e75ecfec6"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a331b1a8ef66804cf20d6681e1bc5aefb"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a333319a03d2087067247c4f5e595b4e5"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a402c19da1ecf273bc942ecc560730567"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a49822f8e1617e30aab9b0d7d790697a3"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a50c4308abda01581b436b7867304e982"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a6475ae77af80e89bb65596bc6f907a58"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a66ce7ba0498053a588de9097cbbc0891"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a6ce270f0afd185c44fa5a2c67a7783fb"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a731ca2f90c17a4f3f868660e51649ce6"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a734174187486ac760b8bf0e566166842"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_a7ebbc81306109e035f89154738900395"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_ac202f5cee0c1d0456b200606860fd5ab"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_acc5b2c30db0c7642d12019f8241dab26"></a>
<a id="astructbt__hci__cp__le__create__big__test_html_aece09ae6264e0cc1a5548f1603a3f61a"></a>
<a id="astructbt__hci__cp__le__create__big_html"></a>
<a id="astructbt__hci__cp__le__create__big_html_a06fd74e9a5f172060835524da5851c71"></a>
<a id="astructbt__hci__cp__le__create__big_html_a0b4b2d77cd0f579aab190336b14597c5"></a>
<a id="astructbt__hci__cp__le__create__big_html_a15018e5ebc124bbe90644b38fe3e7e76"></a>
<a id="astructbt__hci__cp__le__create__big_html_a1cb0dd106bf4a1a0c473333d089c95e7"></a>
<a id="astructbt__hci__cp__le__create__big_html_a2960a9891b827529c9fa1b68a747e2d5"></a>
<a id="astructbt__hci__cp__le__create__big_html_a330916d60c05ec2ef7a71933b62c203a"></a>
<a id="astructbt__hci__cp__le__create__big_html_a490bd68d137f8cf60ea2ccd5ea4495e9"></a>
<a id="astructbt__hci__cp__le__create__big_html_a56cb773a03e4927c3b6bf4d2a6ed6ed9"></a>
<a id="astructbt__hci__cp__le__create__big_html_aa686eec31ca4c831262dd34d41f9a1fb"></a>
<a id="astructbt__hci__cp__le__create__big_html_ac027390db21320fb9d1002161c4c2f67"></a>
<a id="astructbt__hci__cp__le__create__big_html_ad8491c970417e63c6a98c12278a89c86"></a>
<a id="astructbt__hci__cp__le__create__big_html_af5412e4a69c05a09b2e818322636a98a"></a>
<a id="astructbt__hci__cp__le__create__cis_html"></a>
<a id="astructbt__hci__cp__le__create__cis_html_a5a323d09df7813fc9b834cc1d205d101"></a>
<a id="astructbt__hci__cp__le__create__cis_html_acd348a7d68947af8e7119b2e1a864481"></a>
<a id="astructbt__hci__cp__le__create__conn_html"></a>
<a id="astructbt__hci__cp__le__create__conn_html_a1a830a0f6cd961d534c338031b2b691b"></a>
<a id="astructbt__hci__cp__le__create__conn_html_a2ca5063f5082a0f330676e56253a21c7"></a>
<a id="astructbt__hci__cp__le__create__conn_html_a476501ccd209f3a52082decf906ca8f0"></a>
<a id="astructbt__hci__cp__le__create__conn_html_a5a9d5c1d44adac876680a517b1fad63f"></a>
<a id="astructbt__hci__cp__le__create__conn_html_a5b329aa8b48e03998e969b2436d35ab5"></a>
<a id="astructbt__hci__cp__le__create__conn_html_a63c7f9e89528105e484a60e41eeb8a30"></a>
<a id="astructbt__hci__cp__le__create__conn_html_a988cf154b0df1ff9af8d34ce73a920dd"></a>
<a id="astructbt__hci__cp__le__create__conn_html_aa009d54866d9c675c2785412bdbd182f"></a>
<a id="astructbt__hci__cp__le__create__conn_html_aa51da7602eb2b44528964c8b706bb043"></a>
<a id="astructbt__hci__cp__le__create__conn_html_abf61e67f5e20adc44b5b9314ed43bccc"></a>
<a id="astructbt__hci__cp__le__create__conn_html_ae8e0ad70a3b23ac035c237db0d57adc4"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_a0223c41abc034d515421fad8c3123387"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_a2c8be699bfd8eaaababd6d0de0b13e18"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_a34fa54e8bbd641bb0901b0b057134ffb"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_a3742081b071b992176b725448cc6ab29"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_a5a17d6c72daaefcb55fdfa24194cc886"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_a6088c8413ca175c0231fc53bfb168b29"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_a709938176023c5482c91af8995001782"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_a74c5fdfbc97b112c35ee318aa2b9b463"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_a8182f4becdef488b84f12fe7e4274193"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_a909e409d55ac539a119e932899a97204"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_a9dc7a6b577c33583b7ca7548e2b555ac"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_aa13e091f99114bb5217489757c1522bd"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_abab4907ec883430044bb9f9d6cf9f25d"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_ac6c9c568918c9ef9aa4f2038a4922020"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_acd11430a6c94b0f0c34e2788a2326a40"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_addaa3592a97bda96a4aba17e809e4018"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_ae833b5f02f878f54dca1a25753eca1f3"></a>
<a id="astructbt__hci__cp__le__cs__create__config_html_aeb26115c8b500829ef6bc238aa3a495f"></a>
<a id="astructbt__hci__cp__le__cs__remove__config_html"></a>
<a id="astructbt__hci__cp__le__cs__remove__config_html_a4591af2e952f514b185db12c5f1158d5"></a>
<a id="astructbt__hci__cp__le__cs__remove__config_html_a9be71a1360f1ed14e6a7e205f5704e39"></a>
<a id="astructbt__hci__cp__le__cs__set__default__settings_html"></a>
<a id="astructbt__hci__cp__le__cs__set__default__settings_html_a04aea510e26136f874ccfbabbbd080bb"></a>
<a id="astructbt__hci__cp__le__cs__set__default__settings_html_a096c3238ccc6624bae89d5a45dd95600"></a>
<a id="astructbt__hci__cp__le__cs__set__default__settings_html_a333341ec01554ab90fc5e340dbfb5130"></a>
<a id="astructbt__hci__cp__le__cs__set__default__settings_html_aa001c88ab42250c2cfd604af11e0ae27"></a>
<a id="astructbt__hci__cp__le__default__past__param_html"></a>
<a id="astructbt__hci__cp__le__default__past__param_html_a159f5245f86b27198264bdcf394d719f"></a>
<a id="astructbt__hci__cp__le__default__past__param_html_a214cb0597d0065bc2c056fe9c51a2220"></a>
<a id="astructbt__hci__cp__le__default__past__param_html_a2ef92304264ad0bf1560accf306bb6d9"></a>
<a id="astructbt__hci__cp__le__default__past__param_html_af18f679f5833c1d782b4e474af5d819c"></a>
<a id="astructbt__hci__cp__le__encrypt_html"></a>
<a id="astructbt__hci__cp__le__encrypt_html_ab64f1bab8ad3a98217db96e6765a7d24"></a>
<a id="astructbt__hci__cp__le__encrypt_html_ad520b84e6e2a4e62f7fefba248c4cf10"></a>
<a id="astructbt__hci__cp__le__enh__rx__test_html"></a>
<a id="astructbt__hci__cp__le__enh__rx__test_html_a3aa5b3947a4a0c87342695469bf056ec"></a>
<a id="astructbt__hci__cp__le__enh__rx__test_html_a9151393e9f05a2ded484a1248a6edb88"></a>
<a id="astructbt__hci__cp__le__enh__rx__test_html_aa2bf385221680b25ce184b4ea5d63cd4"></a>
<a id="astructbt__hci__cp__le__enh__tx__test_html"></a>
<a id="astructbt__hci__cp__le__enh__tx__test_html_a0b7883b36d511c6da1bac543f1aae446"></a>
<a id="astructbt__hci__cp__le__enh__tx__test_html_a718442db29c5ac455c3e2aac9844cdd0"></a>
<a id="astructbt__hci__cp__le__enh__tx__test_html_a9ccb91be1554172d6c724e438508bfe5"></a>
<a id="astructbt__hci__cp__le__enh__tx__test_html_af1e27be0ad23887c0e71024739b00f8d"></a>
<a id="astructbt__hci__cp__le__ext__create__conn__v2_html"></a>
<a id="astructbt__hci__cp__le__ext__create__conn__v2_html_a05fd0089a0fd43f98042835231407a60"></a>
<a id="astructbt__hci__cp__le__ext__create__conn__v2_html_a25466a04d224bdf495266b0064c424dd"></a>
<a id="astructbt__hci__cp__le__ext__create__conn__v2_html_a536da199958b3b54469f5b4b029e1bac"></a>
<a id="astructbt__hci__cp__le__ext__create__conn__v2_html_a66632dbac1605cff69e8da566e800347"></a>
<a id="astructbt__hci__cp__le__ext__create__conn__v2_html_a8d606c5aa480f54c8da9f42a35ad513e"></a>
<a id="astructbt__hci__cp__le__ext__create__conn__v2_html_addf1f80c4d3625e0c6d6e716f6e2e207"></a>
<a id="astructbt__hci__cp__le__ext__create__conn__v2_html_ae2d3e3079a2848907224bb7ff0efc64b"></a>
<a id="astructbt__hci__cp__le__ext__create__conn_html"></a>
<a id="astructbt__hci__cp__le__ext__create__conn_html_a0561b446effa3f735a405c0b307466bf"></a>
<a id="astructbt__hci__cp__le__ext__create__conn_html_a12a99044f54e3d5dae30a64392444cbf"></a>
<a id="astructbt__hci__cp__le__ext__create__conn_html_a79bc55d9f5b1d719de4fb404db9008f3"></a>
<a id="astructbt__hci__cp__le__ext__create__conn_html_acdb436d6bf2864745ec579622ae0d532"></a>
<a id="astructbt__hci__cp__le__ext__create__conn_html_ae859ff0da5e9cdc872943fd74774ef7e"></a>
<a id="astructbt__hci__cp__le__frame__space__update_html"></a>
<a id="astructbt__hci__cp__le__frame__space__update_html_a10fb9f808dec017325861c983beb6bc9"></a>
<a id="astructbt__hci__cp__le__frame__space__update_html_a6f8ae56a870c76d06e47aa15d22ca341"></a>
<a id="astructbt__hci__cp__le__frame__space__update_html_a9854593fb39c71bfd5ee3da6f606dd7f"></a>
<a id="astructbt__hci__cp__le__frame__space__update_html_ab449a9514f175ad73942582f07cdf792"></a>
<a id="astructbt__hci__cp__le__frame__space__update_html_acbb6b64086a5710449b4d4e228575325"></a>
<a id="astructbt__hci__cp__le__generate__dhkey__v2_html"></a>
<a id="astructbt__hci__cp__le__generate__dhkey__v2_html_a3d47ad6d9df4d4023d2586c915ee8f2c"></a>
<a id="astructbt__hci__cp__le__generate__dhkey__v2_html_acc3007adf301674b9e847297007c3cd1"></a>
<a id="astructbt__hci__cp__le__generate__dhkey_html"></a>
<a id="astructbt__hci__cp__le__generate__dhkey_html_a0f67195504d877a1d11b7dfb77d09fcc"></a>
<a id="astructbt__hci__cp__le__iso__receive__test_html"></a>
<a id="astructbt__hci__cp__le__iso__receive__test_html_a9ce7e13fc1c1a7c87c01e1ecb24c5324"></a>
<a id="astructbt__hci__cp__le__iso__receive__test_html_ac1272441f5c7b79e1ef5f644f099d19e"></a>
<a id="astructbt__hci__cp__le__iso__test__end_html"></a>
<a id="astructbt__hci__cp__le__iso__test__end_html_ab792ec021319024828bd7609e0fe7e96"></a>
<a id="astructbt__hci__cp__le__iso__transmit__test_html"></a>
<a id="astructbt__hci__cp__le__iso__transmit__test_html_a0653c77af723cc43a6b911816a8db437"></a>
<a id="astructbt__hci__cp__le__iso__transmit__test_html_adffb0d57afc090692ab36ebeaad21bbd"></a>
<a id="astructbt__hci__cp__le__ltk__req__neg__reply_html"></a>
<a id="astructbt__hci__cp__le__ltk__req__neg__reply_html_add8cc3b13432e233ceb5c2c11e0107c0"></a>
<a id="astructbt__hci__cp__le__ltk__req__reply_html"></a>
<a id="astructbt__hci__cp__le__ltk__req__reply_html_a2d16b44af344237a890341943c4a6582"></a>
<a id="astructbt__hci__cp__le__ltk__req__reply_html_a46d87451acc1f1ce2ff35dd0dd238db3"></a>
<a id="astructbt__hci__cp__le__past__param_html"></a>
<a id="astructbt__hci__cp__le__past__param_html_a47c571ff27a59e0a7cbcb460303ee194"></a>
<a id="astructbt__hci__cp__le__past__param_html_a622499d51e917f7828629de2291812e5"></a>
<a id="astructbt__hci__cp__le__past__param_html_a9c99cdd5ae5de58960677781c2287c4d"></a>
<a id="astructbt__hci__cp__le__past__param_html_aa36345a550dfabeef48b430d1a1b0030"></a>
<a id="astructbt__hci__cp__le__past__param_html_aec9aa4ffe41c6b6f5cfcbc59eb57efca"></a>
<a id="astructbt__hci__cp__le__per__adv__create__sync_html"></a>
<a id="astructbt__hci__cp__le__per__adv__create__sync_html_a3a0a0bc1bd5014f2ede0c4ef6cc30d24"></a>
<a id="astructbt__hci__cp__le__per__adv__create__sync_html_a46ea01403f68d42a315ff629374b2a95"></a>
<a id="astructbt__hci__cp__le__per__adv__create__sync_html_a554552684fa2a8d0022f9e31ade9c222"></a>
<a id="astructbt__hci__cp__le__per__adv__create__sync_html_a905b2a9166dd668df5929f0866769576"></a>
<a id="astructbt__hci__cp__le__per__adv__create__sync_html_ab5c4debe1babb98c60c1f1bfdf55359a"></a>
<a id="astructbt__hci__cp__le__per__adv__create__sync_html_aff300f352ec5f0fece90f88db811ef75"></a>
<a id="astructbt__hci__cp__le__per__adv__set__info__transfer_html"></a>
<a id="astructbt__hci__cp__le__per__adv__set__info__transfer_html_a3b2f0c510ef9b385cb42bf9a194fa574"></a>
<a id="astructbt__hci__cp__le__per__adv__set__info__transfer_html_a5f14c3265bffdf3e30a554a3686e9e0c"></a>
<a id="astructbt__hci__cp__le__per__adv__set__info__transfer_html_a75b2c0fa1d50ef9d3761ac25f487750b"></a>
<a id="astructbt__hci__cp__le__per__adv__sync__transfer_html"></a>
<a id="astructbt__hci__cp__le__per__adv__sync__transfer_html_a1327de0f9b2ebd1eaa97b51850087460"></a>
<a id="astructbt__hci__cp__le__per__adv__sync__transfer_html_a38537b7f01a93f7a3e8cfcb92098a172"></a>
<a id="astructbt__hci__cp__le__per__adv__sync__transfer_html_a991f77d6f2f0c301fe3322050b2d359f"></a>
<a id="astructbt__hci__cp__le__per__adv__terminate__sync_html"></a>
<a id="astructbt__hci__cp__le__per__adv__terminate__sync_html_a607fce7fd5c88e12f82e3d9731bd7f1a"></a>
<a id="astructbt__hci__cp__le__procedure__enable_html"></a>
<a id="astructbt__hci__cp__le__procedure__enable_html_a3a203b453bd913db8bec91be9310003a"></a>
<a id="astructbt__hci__cp__le__procedure__enable_html_ae1dc5c808bed301ddee6e9dd624c00a5"></a>
<a id="astructbt__hci__cp__le__procedure__enable_html_af94d81f71c2fe587c848e34a430825bf"></a>
<a id="astructbt__hci__cp__le__read__all__remote__features_html"></a>
<a id="astructbt__hci__cp__le__read__all__remote__features_html_a2baf8df3a24b1b883768278459a156c7"></a>
<a id="astructbt__hci__cp__le__read__all__remote__features_html_aa8cf7318871819cf425aa59ca15cc86d"></a>
<a id="astructbt__hci__cp__le__read__chan__map_html"></a>
<a id="astructbt__hci__cp__le__read__chan__map_html_abea9aec016a0433b3e4837d53d6b5d2b"></a>
<a id="astructbt__hci__cp__le__read__iso__link__quality_html"></a>
<a id="astructbt__hci__cp__le__read__iso__link__quality_html_a346fb3cf08203725d5943e42f03cb40d"></a>
<a id="astructbt__hci__cp__le__read__iso__tx__sync_html"></a>
<a id="astructbt__hci__cp__le__read__iso__tx__sync_html_a8edc469f73540d4300b1716c96e17c9f"></a>
<a id="astructbt__hci__cp__le__read__local__rpa_html"></a>
<a id="astructbt__hci__cp__le__read__local__rpa_html_aa96cd60066003e4a7a1f482fb81557f8"></a>
<a id="astructbt__hci__cp__le__read__peer__rpa_html"></a>
<a id="astructbt__hci__cp__le__read__peer__rpa_html_ab0c70a1dbe5152b1fc926b90ec3387b3"></a>
<a id="astructbt__hci__cp__le__read__phy_html"></a>
<a id="astructbt__hci__cp__le__read__phy_html_a7e0a4fa47b613c86364e6e94c2d0bef1"></a>
<a id="astructbt__hci__cp__le__read__remote__fae__table_html"></a>
<a id="astructbt__hci__cp__le__read__remote__fae__table_html_a10bdfc4808586f7cccf025c63a6e28a5"></a>
<a id="astructbt__hci__cp__le__read__remote__features_html"></a>
<a id="astructbt__hci__cp__le__read__remote__features_html_a843997555fd36f102c83a7d59f65eea9"></a>
<a id="astructbt__hci__cp__le__read__remote__supported__capabilities_html"></a>
<a id="astructbt__hci__cp__le__read__remote__supported__capabilities_html_ac6f083563e2c72d37cf4e9e8fa695733"></a>
<a id="astructbt__hci__cp__le__read__test__counters_html"></a>
<a id="astructbt__hci__cp__le__read__test__counters_html_a230d973c2db177c3595bb4808ebf5cd2"></a>
<a id="astructbt__hci__cp__le__read__tx__power__level_html"></a>
<a id="astructbt__hci__cp__le__read__tx__power__level_html_a4863396dfe4dca65aaef68293e29291b"></a>
<a id="astructbt__hci__cp__le__read__tx__power__level_html_af8c2d89b183d7bdc0f55a0bf783a373d"></a>
<a id="astructbt__hci__cp__le__reject__cis_html"></a>
<a id="astructbt__hci__cp__le__reject__cis_html_ad697d740bdf5a565090a548e7e8fd399"></a>
<a id="astructbt__hci__cp__le__reject__cis_html_aec5bd3e4d27b6e3a2653112b36a3d128"></a>
<a id="astructbt__hci__cp__le__rem__dev__from__fal_html"></a>
<a id="astructbt__hci__cp__le__rem__dev__from__fal_html_afe6054303093cc930d1089ca6a16101c"></a>
<a id="astructbt__hci__cp__le__rem__dev__from__per__adv__list_html"></a>
<a id="astructbt__hci__cp__le__rem__dev__from__per__adv__list_html_a6629f3ececf586792a14f3c028cc8e8c"></a>
<a id="astructbt__hci__cp__le__rem__dev__from__per__adv__list_html_adc420288f6a79c1a92f57241d3da3d81"></a>
<a id="astructbt__hci__cp__le__rem__dev__from__rl_html"></a>
<a id="astructbt__hci__cp__le__rem__dev__from__rl_html_aacb577a7ae13322145fccdffc3161541"></a>
<a id="astructbt__hci__cp__le__remove__adv__set_html"></a>
<a id="astructbt__hci__cp__le__remove__adv__set_html_ab33bf918b10d847bb8fb8ac2409780e6"></a>
<a id="astructbt__hci__cp__le__remove__cig_html"></a>
<a id="astructbt__hci__cp__le__remove__cig_html_addf395d945f14afbf2d39fa4d0d22f31"></a>
<a id="astructbt__hci__cp__le__remove__iso__path_html"></a>
<a id="astructbt__hci__cp__le__remove__iso__path_html_a46e4b28917ff963ff4b672749fde0971"></a>
<a id="astructbt__hci__cp__le__remove__iso__path_html_ad0106791003f9d1173f2a9f102903c45"></a>
<a id="astructbt__hci__cp__le__req__peer__sca_html"></a>
<a id="astructbt__hci__cp__le__req__peer__sca_html_a39d65681da55b26f2900f06cde637d88"></a>
<a id="astructbt__hci__cp__le__rx__test__v3_html"></a>
<a id="astructbt__hci__cp__le__rx__test__v3_html_a55b5c4739e456167f17bf3899d096e61"></a>
<a id="astructbt__hci__cp__le__rx__test__v3_html_a5cd5a44b0832b9f6e2198b9ad714b99b"></a>
<a id="astructbt__hci__cp__le__rx__test__v3_html_a7ffde9dc565194c0108177cf11b02b5b"></a>
<a id="astructbt__hci__cp__le__rx__test__v3_html_aa6cd0835068f378949da182af13e2438"></a>
<a id="astructbt__hci__cp__le__rx__test__v3_html_ab0832e72ef90b1269928378638fcb194"></a>
<a id="astructbt__hci__cp__le__rx__test__v3_html_abd33b70c948d4ee42d96d0d2e7f7cb1c"></a>
<a id="astructbt__hci__cp__le__rx__test__v3_html_ad1a1082d27b8a10e25eebd347404637c"></a>
<a id="astructbt__hci__cp__le__rx__test__v3_html_ad1c211c59cf34d76429d4d4548966630"></a>
<a id="astructbt__hci__cp__le__rx__test_html"></a>
<a id="astructbt__hci__cp__le__rx__test_html_a11cb21a7625d9c097eba0a7b68e93f3f"></a>
<a id="astructbt__hci__cp__le__security__enable_html"></a>
<a id="astructbt__hci__cp__le__security__enable_html_a772d3744d43f0447187040f2c6f0ac6e"></a>
<a id="astructbt__hci__cp__le__set__addr__res__enable_html"></a>
<a id="astructbt__hci__cp__le__set__addr__res__enable_html_ad0548178cbc9bc2db54612a748a2bd65"></a>
<a id="astructbt__hci__cp__le__set__adv__data_html"></a>
<a id="astructbt__hci__cp__le__set__adv__data_html_a664313db17c12adb0de14371e46d26a8"></a>
<a id="astructbt__hci__cp__le__set__adv__data_html_a6fb8734ff5a9b77586b3e283b83985bb"></a>
<a id="astructbt__hci__cp__le__set__adv__enable_html"></a>
<a id="astructbt__hci__cp__le__set__adv__enable_html_a15e92d187d586fef560adf9c793f776a"></a>
<a id="astructbt__hci__cp__le__set__adv__param_html"></a>
<a id="astructbt__hci__cp__le__set__adv__param_html_a2269ae424e47adddce5aa5f2f5b84c89"></a>
<a id="astructbt__hci__cp__le__set__adv__param_html_a2476c2a1858eab7e9b1449c1901363c4"></a>
<a id="astructbt__hci__cp__le__set__adv__param_html_a662c5ae81f25a897a8e597f7227a1e39"></a>
<a id="astructbt__hci__cp__le__set__adv__param_html_a9b09964156846fd480911dcc2d996a98"></a>
<a id="astructbt__hci__cp__le__set__adv__param_html_ab42c6b8f482e782d09386a3a1758903d"></a>
<a id="astructbt__hci__cp__le__set__adv__param_html_ac774ef72175e43b083d04ecac263941b"></a>
<a id="astructbt__hci__cp__le__set__adv__param_html_ad8c74cac74254354b314f07df7df1bf0"></a>
<a id="astructbt__hci__cp__le__set__adv__set__random__addr_html"></a>
<a id="astructbt__hci__cp__le__set__adv__set__random__addr_html_a2883e9bf7ef6a34712eda2594e23c146"></a>
<a id="astructbt__hci__cp__le__set__adv__set__random__addr_html_aafa39422a16cc4ff11c8073e9c0aab71"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html_a0cf0f3f7c10b29d74ab64aa30a4969de"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html_a161ae960cbd4f7833815285d04f87e46"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html_a1d060539ff26677c1326a6ed3394fb6e"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html_a1eae50a97188304852589fd95e994150"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html_a2cb6745b8f908cd2e7d5f12a092c3b69"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html_a50c345ef03c669f476e143728f42cd6d"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html_a5e07eb0d7d13e57be457d1b77a5dba12"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html_a7275312e8b1c8ebc2af7992f765b392c"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html_aa392cbac058beefd0e410fcc9821a0c3"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html_aa77765d90fde67c52e4f2d483f0a3ee0"></a>
<a id="astructbt__hci__cp__le__set__cig__params__test_html_af2ed1bf1a6beaff884c3ce3faf26bfb2"></a>
<a id="astructbt__hci__cp__le__set__cig__params_html"></a>
<a id="astructbt__hci__cp__le__set__cig__params_html_a14f5c0cf7f99ab406714501038048035"></a>
<a id="astructbt__hci__cp__le__set__cig__params_html_a46a657cdfbc7a49e6761d9f18d980c2a"></a>
<a id="astructbt__hci__cp__le__set__cig__params_html_a50a260a15f3a0ceae716da6c04c5b768"></a>
<a id="astructbt__hci__cp__le__set__cig__params_html_a79fc069492741f14f348650abef4c66b"></a>
<a id="astructbt__hci__cp__le__set__cig__params_html_a7dbf75c6ed92a053c4ec0d8f7268c92e"></a>
<a id="astructbt__hci__cp__le__set__cig__params_html_a810822396b97d54988ec57561b4ee7d5"></a>
<a id="astructbt__hci__cp__le__set__cig__params_html_a867bf5ddbcadd27dbec2c3059d67d6d6"></a>
<a id="astructbt__hci__cp__le__set__cig__params_html_ac922e59065920421f40468754d2ba5a2"></a>
<a id="astructbt__hci__cp__le__set__cig__params_html_adf468a8a195447a7bbed4dcd53d287f6"></a>
<a id="astructbt__hci__cp__le__set__cig__params_html_afec8ebd17cc6ca5b3d13ef54f406df62"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__sampling__enable_html"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__sampling__enable_html_a38e770b3e5f9d7d63a564dfa7c80451f"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__sampling__enable_html_a4f52142ef1d2365859189b7a2abe050b"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__sampling__enable_html_a67bb2dbfe1707f76a5e211e007459c22"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__sampling__enable_html_a91d3458e2049ab434e220403b7ba235d"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__sampling__enable_html_aaaed0fc39158c653041fd760a00cecec"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__sampling__enable_html_aca9e1316c716525f00308f64b8c6cec4"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__tx__enable_html"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__tx__enable_html_a3530dae940caefeafb9de4ac761ee080"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__tx__enable_html_a55125c808a888eeecfee9410bcb55859"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__tx__params_html"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__tx__params_html_a27a228653ea560a77369a6b1829a8a9d"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__tx__params_html_a8208571653e444221648d2a884eabfae"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__tx__params_html_a869192cea35f4cd57984614e4c8bb5a5"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__tx__params_html_a8f20e6e3bb408551d6cc494ad19391c4"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__tx__params_html_ab5c4742cf37cf7e802423beb4a9b4fa2"></a>
<a id="astructbt__hci__cp__le__set__cl__cte__tx__params_html_af5e82bf572b385904a0f24219bdc72ca"></a>
<a id="astructbt__hci__cp__le__set__conn__cte__rx__params_html"></a>
<a id="astructbt__hci__cp__le__set__conn__cte__rx__params_html_a519c37f5d797d8ddac5ba9be7c14b9f9"></a>
<a id="astructbt__hci__cp__le__set__conn__cte__rx__params_html_a615cae822878cf1344a990e30fa80044"></a>
<a id="astructbt__hci__cp__le__set__conn__cte__rx__params_html_a6246d492b94c67af9604b89912dbdb61"></a>
<a id="astructbt__hci__cp__le__set__conn__cte__rx__params_html_a76968866cf5c6ef4bfb983cb6b68a827"></a>
<a id="astructbt__hci__cp__le__set__conn__cte__rx__params_html_a89194a5b9e6c7f0c176c915e451911df"></a>
<a id="astructbt__hci__cp__le__set__conn__cte__tx__params_html"></a>
<a id="astructbt__hci__cp__le__set__conn__cte__tx__params_html_a8f0e5ee74662056f00eaa3a8c72f6fc4"></a>
<a id="astructbt__hci__cp__le__set__conn__cte__tx__params_html_ab47f852b476ac2c35fc0631180e19fb4"></a>
<a id="astructbt__hci__cp__le__set__conn__cte__tx__params_html_abff85d652b3b2fd55ad78e53887cd7ce"></a>
<a id="astructbt__hci__cp__le__set__conn__cte__tx__params_html_ae0a482982d804ffd7d16ea2b413e538d"></a>
<a id="astructbt__hci__cp__le__set__data__len_html"></a>
<a id="astructbt__hci__cp__le__set__data__len_html_a15285a4e8bf8e359bb326de4b30ba8f1"></a>
<a id="astructbt__hci__cp__le__set__data__len_html_a874869090428a7f380c5466353573eba"></a>
<a id="astructbt__hci__cp__le__set__data__len_html_ac579e84a004a09813bbe0ed61db11931"></a>
<a id="astructbt__hci__cp__le__set__default__phy_html"></a>
<a id="astructbt__hci__cp__le__set__default__phy_html_a0c4ab2d91021466fd136af3a0b6bde2a"></a>
<a id="astructbt__hci__cp__le__set__default__phy_html_a4c3410f2ce9fb2817bc5d143908936d1"></a>
<a id="astructbt__hci__cp__le__set__default__phy_html_abe1d83e372e874739588812040d0b540"></a>
<a id="astructbt__hci__cp__le__set__default__subrate_html"></a>
<a id="astructbt__hci__cp__le__set__default__subrate_html_a16adacc30fd5ae00b3944f068b075b1a"></a>
<a id="astructbt__hci__cp__le__set__default__subrate_html_a1906f4dd7955200c81093b8f7c5d55c0"></a>
<a id="astructbt__hci__cp__le__set__default__subrate_html_a9d8fd7cad5260c8943b90ab50c04b225"></a>
<a id="astructbt__hci__cp__le__set__default__subrate_html_ad18a8042c38a1b4d83d6fccad1ab5af8"></a>
<a id="astructbt__hci__cp__le__set__default__subrate_html_aff2e682b4c8e5c3078885be126c5b958"></a>
<a id="astructbt__hci__cp__le__set__event__mask_html"></a>
<a id="astructbt__hci__cp__le__set__event__mask_html_af7de4823aca253f15e57f54ee9b3879e"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__data_html"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__data_html_a7d7df52500eb53a64b6ba5e62f6cf14f"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__data_html_a803bb793eefcc714c6c4034123a2e487"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__data_html_ac5eaa1834f82024055923d08a3bef6b3"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__data_html_aea3055cc7ffbaf4cd14996d885e21ba3"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__data_html_af9eef9f59bfec5867ea36bdf33e3a9b1"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__enable_html"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__enable_html_a04911e19f3b2f0079d4e12980d11157f"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__enable_html_a06088af8b432ac134943d9ebb7778ac7"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__enable_html_ab7148b47bf052d8cba1f6bf3385051c8"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_a047656dd56bf883f1e307dcabe96f1de"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_a0c7994ef034270a7fd814386e7b76cc8"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_a1a96a88729e311c6a60571997aae9fc3"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_a25fec4dc9203bb50bb030087b42f473e"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_a5283a6a40d46e0fe787ed403acab9f90"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_a554f89f00700bc3ea4996b0a971fedbf"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_a6098216ae6ef0f9459aae16adecd193f"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_a6c2a953fab938f304e815bd9d59d05ae"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_a8767fb7f5492f0323edd9afb687318db"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_a92a215151c603c2f8dd1b7e730a8e979"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_a9f2a6f38e8965dabe17ad743d3aeda70"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_ac31b52df1033d11585781fbecc10f578"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_ad8fccd11fbea598de62e057a69b72156"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_ad9e43219b471e44884b33ea5ddd90513"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_aeb26f7f16e2c71542421aada577a993f"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param__v2_html_aff572d12a03ca9cbc2ee80f75e1f77c7"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_a048874197ccbdbc626f0563be5c41ec7"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_a08aa741a56e825a11424bf024ac65e14"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_a29a62f8989f89b014cadbad9b94e996a"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_a3594f7337ccd739f59ac7845757de0e8"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_a4af102ae90ca6917b3134491c5ff079f"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_a5793c6afe545290a1e792bcc73585b72"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_a5f7f3e477b5b0b8122b85f3e53dd7878"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_a65fe609dde9515212659087a024e7c65"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_a819e599df4025036fab2dabd7c61ea37"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_ab5a80941b3d832c2906daed8cf069a02"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_abc82ba984647eb00bc490c01ce746a15"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_ad7a0b9028bcdb57a9011d4677412aed5"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_ae694df46b1db4b029d1e177768b3821f"></a>
<a id="astructbt__hci__cp__le__set__ext__adv__param_html_af8bc3509fdd5e89c27db466727fe1cd9"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__enable_html"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__enable_html_a922d0c5a7ccb6c1e1864f662227b8307"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__enable_html_aa5b0939838ab13eb8299f4a4b2fd3f14"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__enable_html_aa60c8ade7047dcd202d83cfc3f18ada2"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__enable_html_adcd5e00a240f3e7395d0d25994b4013a"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__param_html"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__param_html_a3418aa8dbdb8062ee452f5756eb9f30c"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__param_html_a47f6cf7f83451dcc2feac1a8d5837ad8"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__param_html_a6c38b7d074eb3c0cf5c301eb6c03b60c"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__param_html_ab4eab9a52dca01bc19b35607d6ec5d36"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__rsp__data_html"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__rsp__data_html_a3323a0844680b71cb8aedffa034837d7"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__rsp__data_html_a6024eac85f600ed3b7051a84b91bdcfa"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__rsp__data_html_a8cf0624b9968686c7f6765ee25e11c90"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__rsp__data_html_ab086720e1a22523ba155cb238ad75197"></a>
<a id="astructbt__hci__cp__le__set__ext__scan__rsp__data_html_ac4e1691926df370b290c9e6d866d310d"></a>
<a id="astructbt__hci__cp__le__set__host__chan__classif_html"></a>
<a id="astructbt__hci__cp__le__set__host__chan__classif_html_a0fb81bcdebe7da416cc4317486106752"></a>
<a id="astructbt__hci__cp__le__set__host__feature_html"></a>
<a id="astructbt__hci__cp__le__set__host__feature_html_a78b67164bce232466ab348f8937682c3"></a>
<a id="astructbt__hci__cp__le__set__host__feature_html_adcca35df216061ea08bd27e10fefd5e9"></a>
<a id="astructbt__hci__cp__le__set__path__loss__reporting__enable_html"></a>
<a id="astructbt__hci__cp__le__set__path__loss__reporting__enable_html_a209a77ef3cf545150feaecdb814797f0"></a>
<a id="astructbt__hci__cp__le__set__path__loss__reporting__enable_html_a79487ac2235da100b41ec50c77bad808"></a>
<a id="astructbt__hci__cp__le__set__path__loss__reporting__parameters_html"></a>
<a id="astructbt__hci__cp__le__set__path__loss__reporting__parameters_html_a2289e8198eea1686030ffd3e225c8e7d"></a>
<a id="astructbt__hci__cp__le__set__path__loss__reporting__parameters_html_a28f79bd4ccec4ed108e20a0080ec842d"></a>
<a id="astructbt__hci__cp__le__set__path__loss__reporting__parameters_html_a2dec83b0269835538cf4bc5553483f19"></a>
<a id="astructbt__hci__cp__le__set__path__loss__reporting__parameters_html_a79a53ca3a481e013a5ee892d779e7bfd"></a>
<a id="astructbt__hci__cp__le__set__path__loss__reporting__parameters_html_ab5de762b7b82c8f453dafe1ea9bbf46d"></a>
<a id="astructbt__hci__cp__le__set__path__loss__reporting__parameters_html_ac8b7b832ba241c0448c80be22249b3ca"></a>
<a id="astructbt__hci__cp__le__set__pawr__response__data_html"></a>
<a id="astructbt__hci__cp__le__set__pawr__response__data_html_a034afaaacf4b2168b9cd54cfde583b5c"></a>
<a id="astructbt__hci__cp__le__set__pawr__response__data_html_a39cbc74ab95881b6dde8fa377d2951e5"></a>
<a id="astructbt__hci__cp__le__set__pawr__response__data_html_a4356344510833196533bb9582f6fe18a"></a>
<a id="astructbt__hci__cp__le__set__pawr__response__data_html_a675a223891b28f06e78df6223439dc28"></a>
<a id="astructbt__hci__cp__le__set__pawr__response__data_html_a8c546fa3c6d969d44c54926330e5cf85"></a>
<a id="astructbt__hci__cp__le__set__pawr__response__data_html_aaf2e0eb3b491b5ccd15ba5259fd900c7"></a>
<a id="astructbt__hci__cp__le__set__pawr__response__data_html_aaf5c337af93f13e243451b46a94ffb77"></a>
<a id="astructbt__hci__cp__le__set__pawr__subevent__data__element_html"></a>
<a id="astructbt__hci__cp__le__set__pawr__subevent__data__element_html_a90178bcd86c1bad0a768f391ce11613f"></a>
<a id="astructbt__hci__cp__le__set__pawr__subevent__data__element_html_a91c975189e409b733ac9a4af5763b12a"></a>
<a id="astructbt__hci__cp__le__set__pawr__subevent__data__element_html_abf33f93f0f1ddf3532c6cae13483ec1e"></a>
<a id="astructbt__hci__cp__le__set__pawr__subevent__data__element_html_ace5860dfa0f628eaed2b68b171d875da"></a>
<a id="astructbt__hci__cp__le__set__pawr__subevent__data__element_html_ad8da1cc672eedf8be8cfc7d0d7ec1b41"></a>
<a id="astructbt__hci__cp__le__set__pawr__subevent__data_html"></a>
<a id="astructbt__hci__cp__le__set__pawr__subevent__data_html_a47d84125d15cce1fc969db3e5caa07e1"></a>
<a id="astructbt__hci__cp__le__set__pawr__subevent__data_html_a9397eebd6771ad159d1bdae0d59e5f46"></a>
<a id="astructbt__hci__cp__le__set__pawr__subevent__data_html_aa932c1f19de96f89a79bbcb3ecbc1f5d"></a>
<a id="astructbt__hci__cp__le__set__pawr__sync__subevent_html"></a>
<a id="astructbt__hci__cp__le__set__pawr__sync__subevent_html_a2648ff50e0bad585e77e6f340836555a"></a>
<a id="astructbt__hci__cp__le__set__pawr__sync__subevent_html_a89f3092c2dd561e5469bb5bf57a06172"></a>
<a id="astructbt__hci__cp__le__set__pawr__sync__subevent_html_a9a362ae841e5305b3985c4b2d88c6753"></a>
<a id="astructbt__hci__cp__le__set__pawr__sync__subevent_html_aa73b23816e6c2c6546de15f6f6caff27"></a>
<a id="astructbt__hci__cp__le__set__per__adv__data_html"></a>
<a id="astructbt__hci__cp__le__set__per__adv__data_html_a93cbb46ce6664880487e009a0b47af02"></a>
<a id="astructbt__hci__cp__le__set__per__adv__data_html_aac34596f0970c976c4ef71250d326c2c"></a>
<a id="astructbt__hci__cp__le__set__per__adv__data_html_adaf581f8db6aafb4dc5df669df7ad26d"></a>
<a id="astructbt__hci__cp__le__set__per__adv__data_html_ae6ee631a153cb6fed88695e599f63e91"></a>
<a id="astructbt__hci__cp__le__set__per__adv__enable_html"></a>
<a id="astructbt__hci__cp__le__set__per__adv__enable_html_a998f4e38a56f771f234ce099b4528a3d"></a>
<a id="astructbt__hci__cp__le__set__per__adv__enable_html_afff649b908264c617b249bcfbebadd53"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param__v2_html"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param__v2_html_a2483eb4457f9dc22ff8473175662e260"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param__v2_html_a35fcc697e60d3c398f03be7503f611bd"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param__v2_html_a79dfc3b13068d9c51f0a756f025aaeba"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param__v2_html_a7bea764aa5d21e03946804566b1f9869"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param__v2_html_acc9718286ab0847a3444d3fc2d3c93bc"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param__v2_html_acdeb503c0a13291158ad389c9f6ac206"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param__v2_html_ad2d658bb0be35aee6b5c133fece89068"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param__v2_html_ae36e28210a515f73648e6f8b3984fb55"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param__v2_html_aee1088b46914c8e26d9e97ce573291c6"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param_html"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param_html_a1a2a69ea6e310710892184ced472eb8a"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param_html_a2b61031952b3893add7677d3802e368b"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param_html_a879ea10e1ab217b4aa49dfcf3b394691"></a>
<a id="astructbt__hci__cp__le__set__per__adv__param_html_af01696ef6bf02e7db37d45a0c9852ef5"></a>
<a id="astructbt__hci__cp__le__set__per__adv__recv__enable_html"></a>
<a id="astructbt__hci__cp__le__set__per__adv__recv__enable_html_a1e626eecf1d3f0820c3b2a13fd84b92f"></a>
<a id="astructbt__hci__cp__le__set__per__adv__recv__enable_html_a2187ec96822726daa5e43e910cc41cc3"></a>
<a id="astructbt__hci__cp__le__set__phy_html"></a>
<a id="astructbt__hci__cp__le__set__phy_html_a06880062ff486b532ebeb789adb57d1e"></a>
<a id="astructbt__hci__cp__le__set__phy_html_a458ab90f83b60fafa66167f474c0800d"></a>
<a id="astructbt__hci__cp__le__set__phy_html_ab30eb68920a0578b16794250e592b12a"></a>
<a id="astructbt__hci__cp__le__set__phy_html_ad0759eea02017674459d4ce0af0e526e"></a>
<a id="astructbt__hci__cp__le__set__phy_html_afb8d056dc7d8824eec0ef16fdf9ce924"></a>
<a id="astructbt__hci__cp__le__set__privacy__mode_html"></a>
<a id="astructbt__hci__cp__le__set__privacy__mode_html_a404cc9f04cd11924445f12eb4471ef2e"></a>
<a id="astructbt__hci__cp__le__set__privacy__mode_html_a8ca00418b0638bba6ef586d6cbf253a5"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_a22ecbaff0fd48a0716a15d265adc590e"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_a51fb8c789cefce09d5da2b86d5c862ce"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_a5de9205fdf1b6e342f53a12aa82c10c5"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_a7a61ff539f68a02ea7aa466f182dc5ab"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_a7d2f5d9242df436906b005e66c7bb75d"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_a8524fd01e35094d2b78488c0a2876832"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_aa5a6a677b6e0d57658041e891535d74b"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_aa783e0e63c38ceee503c0b73ac873ca7"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_aa9ec99aff85de173ccb2d3f144c85319"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_ab8a15269255fb7d960ae712a844b9f35"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_ac6bb66fa24aec17a964f27365ca65ec9"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_ad46165bc5f6d875940ee53a8b98cb5b4"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_ade09ca9d42b0db682cf677d9ac4326d2"></a>
<a id="astructbt__hci__cp__le__set__procedure__parameters_html_afcd4e8b390fd996ee134043ec2930fe8"></a>
<a id="astructbt__hci__cp__le__set__random__address_html"></a>
<a id="astructbt__hci__cp__le__set__random__address_html_a919ef74473f4f86d00595ec8606789d0"></a>
<a id="astructbt__hci__cp__le__set__rpa__timeout_html"></a>
<a id="astructbt__hci__cp__le__set__rpa__timeout_html_a6b1befe9d2131a889de17339ec1941fa"></a>
<a id="astructbt__hci__cp__le__set__scan__enable_html"></a>
<a id="astructbt__hci__cp__le__set__scan__enable_html_a5e429a0b11be1493515803a360932b06"></a>
<a id="astructbt__hci__cp__le__set__scan__enable_html_a77b0f05c0e76681ed633bd42b3f21811"></a>
<a id="astructbt__hci__cp__le__set__scan__param_html"></a>
<a id="astructbt__hci__cp__le__set__scan__param_html_a3b5b4767092fc69a63d2219d60722407"></a>
<a id="astructbt__hci__cp__le__set__scan__param_html_a694c74a6fc95f767d2e89e6596d51e98"></a>
<a id="astructbt__hci__cp__le__set__scan__param_html_ab7a268e17a5d564d475ff9dee5e6e14b"></a>
<a id="astructbt__hci__cp__le__set__scan__param_html_ad19a479cc3c27ab24286b537b646261e"></a>
<a id="astructbt__hci__cp__le__set__scan__param_html_adcd8be074a8b19e0e7d02c4ea8209c93"></a>
<a id="astructbt__hci__cp__le__set__scan__rsp__data_html"></a>
<a id="astructbt__hci__cp__le__set__scan__rsp__data_html_a0fe51008184419c9560bb5d8f287d8be"></a>
<a id="astructbt__hci__cp__le__set__scan__rsp__data_html_aa719449dc2b85f094081d66398b72c7d"></a>
<a id="astructbt__hci__cp__le__set__tx__power__report__enable_html"></a>
<a id="astructbt__hci__cp__le__set__tx__power__report__enable_html_a30580470d1ba516d86c8b157ca415ef3"></a>
<a id="astructbt__hci__cp__le__set__tx__power__report__enable_html_a4a37c87f8f6a966a90c5de09096d1356"></a>
<a id="astructbt__hci__cp__le__set__tx__power__report__enable_html_ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e"></a>
<a id="astructbt__hci__cp__le__setup__iso__path_html"></a>
<a id="astructbt__hci__cp__le__setup__iso__path_html_a0054fede0e583cef0dbcf6ef3134e480"></a>
<a id="astructbt__hci__cp__le__setup__iso__path_html_a1a816d8e8c434a05ea897b74bc4d89c7"></a>
<a id="astructbt__hci__cp__le__setup__iso__path_html_a31948436e6608f9943d34ce89a65c64c"></a>
<a id="astructbt__hci__cp__le__setup__iso__path_html_a5256fc99b362e3a5f986ef2b71b29ccb"></a>
<a id="astructbt__hci__cp__le__setup__iso__path_html_a7c07d69b2005af1f7f2618f2bfa60d50"></a>
<a id="astructbt__hci__cp__le__setup__iso__path_html_a89c1324359a4fc2f10fee9ebbac5cf2b"></a>
<a id="astructbt__hci__cp__le__setup__iso__path_html_ade4dee947e3d288f769d2d69fc57f96a"></a>
<a id="astructbt__hci__cp__le__start__encryption_html"></a>
<a id="astructbt__hci__cp__le__start__encryption_html_a4ac6d63f336e36a347242153aced4c71"></a>
<a id="astructbt__hci__cp__le__start__encryption_html_a896961309d9b3f136beecf70a7e6e8e4"></a>
<a id="astructbt__hci__cp__le__start__encryption_html_a99d2dd719ce38976e9da8a73f26839a1"></a>
<a id="astructbt__hci__cp__le__start__encryption_html_ac1e1fd8b6b97bbd6f27b6e4322b03530"></a>
<a id="astructbt__hci__cp__le__subrate__request_html"></a>
<a id="astructbt__hci__cp__le__subrate__request_html_a04ccc83303baabf30b663983883e7e77"></a>
<a id="astructbt__hci__cp__le__subrate__request_html_a18ba526d8a843ad9c74c22d0899d9c1f"></a>
<a id="astructbt__hci__cp__le__subrate__request_html_a2595419182358e3386a0fb6e523a3dda"></a>
<a id="astructbt__hci__cp__le__subrate__request_html_a5c95a2bea462fb72d34d6314046041b7"></a>
<a id="astructbt__hci__cp__le__subrate__request_html_a60bcbe27605063725422a0b1c35f21e7"></a>
<a id="astructbt__hci__cp__le__subrate__request_html_ab32a92ed52266c6b7d6d9ab08787e770"></a>
<a id="astructbt__hci__cp__le__terminate__big_html"></a>
<a id="astructbt__hci__cp__le__terminate__big_html_a958ab6b2f2bb30c825060498e6917a18"></a>
<a id="astructbt__hci__cp__le__terminate__big_html_acb5fb9451cf890245a85704579b1d1c8"></a>
<a id="astructbt__hci__cp__le__tx__test__v3_html"></a>
<a id="astructbt__hci__cp__le__tx__test__v3_html_a1c0828e51bb6c24e9dd1f12b5badcfea"></a>
<a id="astructbt__hci__cp__le__tx__test__v3_html_a459b850f35c61bf7f53d3730245cb4bb"></a>
<a id="astructbt__hci__cp__le__tx__test__v3_html_a52d2d6dcc188d5f02904e0e56f461841"></a>
<a id="astructbt__hci__cp__le__tx__test__v3_html_a6486882bc375f229a88bbfa53be49670"></a>
<a id="astructbt__hci__cp__le__tx__test__v3_html_a712a30d9d6afc7d302041e1de6721de4"></a>
<a id="astructbt__hci__cp__le__tx__test__v3_html_ad8f2d2ca3ad3be28c0aec9e8a0e1bc61"></a>
<a id="astructbt__hci__cp__le__tx__test__v3_html_adf6b1653902fb13cc1ccc32cd91c990f"></a>
<a id="astructbt__hci__cp__le__tx__test__v3_html_afdb6dd44108e9a4a21ac31a74c1e083f"></a>
<a id="astructbt__hci__cp__le__tx__test__v4__tx__power_html"></a>
<a id="astructbt__hci__cp__le__tx__test__v4__tx__power_html_a2a8b1c31787066ad2b471aec5c261085"></a>
<a id="astructbt__hci__cp__le__tx__test__v4_html"></a>
<a id="astructbt__hci__cp__le__tx__test__v4_html_a2039a87b5f32c4a45b8f858808df7cdc"></a>
<a id="astructbt__hci__cp__le__tx__test__v4_html_a3ccae40f09b2763b2b07dc16982f3973"></a>
<a id="astructbt__hci__cp__le__tx__test__v4_html_a3fe8ab7c0ee389dce8592cb7a38bc42c"></a>
<a id="astructbt__hci__cp__le__tx__test__v4_html_a5db011159fe75f4522e03ea1efdc57bd"></a>
<a id="astructbt__hci__cp__le__tx__test__v4_html_a7a8e2610fb8903ccfb6e4b08017f6112"></a>
<a id="astructbt__hci__cp__le__tx__test__v4_html_a8dea923a63e787de3bfe07611eb7a1ed"></a>
<a id="astructbt__hci__cp__le__tx__test__v4_html_abdd393eb264f04acf65e2dce4bd65ac0"></a>
<a id="astructbt__hci__cp__le__tx__test__v4_html_ae950f71a3fcfca0cf738bc28693256cf"></a>
<a id="astructbt__hci__cp__le__tx__test_html"></a>
<a id="astructbt__hci__cp__le__tx__test_html_a55c5f1621a51da03500910fc9664df54"></a>
<a id="astructbt__hci__cp__le__tx__test_html_aae634b277125066ecbc36d119bc4244f"></a>
<a id="astructbt__hci__cp__le__tx__test_html_ad93908905d370842f16e16cc45280495"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__fae__table_html"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__fae__table_html_a330531f1809cddea8f1527f3b0a92e31"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__fae__table_html_a8594dd89888d1388f2a45a33e12e94d0"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a0872c2a5399e1d82f334796dd35379ad"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a17d3094a1b93665e755b2111074de42c"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a1ff4fede6b4d942f64ec2b94b222703b"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a2077365a697d7085d7db97fb35c391f4"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a214f693e10c331091e34f09c2cfc9749"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a225720841ea95409879d51bd9a031fb7"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a22f1010c9f4de7902480d3f84d499fb1"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a2e8693852819f5e4afa8cae90f8ae92c"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a30cee084044918cb450060a164bd4b30"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a65a5b6ebdbc5793ca800ee202cb4676c"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a6bb274c4c2ff4dc2c6136b0bc7515be3"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a6eff7fb52e3ef1074eb875af4c79a8aa"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a8aa60cab3469fadd342a0a9b0d1b094f"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_a8c63e46cf58623b3ca9cbfa7b802744e"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_abf661cac9a1a2a5bf38180dbfc486bcd"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_ac370abefdc5a7acdf1e3c72093d11018"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_ac599d7323d560b8f554bbaaf70aabd8b"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_ac930e63945abfc0cdfdaa79164e114fa"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_ad342355fdc6396d6680b7e215ef4b16e"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_ad7c6799d86889b67d86ca44bac4238a6"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_ae757536a884e640451e35dd2fca90605"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_aead25f8f371ed85e66d05af852b90a9e"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities__v2_html_afbe4805ccd9db70a596afdabb6963885"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a0911e19deceb7f243ac706ddb4cf0a3a"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a257b38d937c1111a66f6c28f1e221211"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a25faaf2be6db05c44256b9f559841c87"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a29781bbe7e25c39b06047725f1d11426"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a2b5c828a30525eee5b1ce48f3ba98896"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a31c877363bd315786ef834215614d346"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a7a60c326707ebd60b96d25924e3c9e40"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a870e068fcc15dd44dca3ac24334000ee"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a8a884bca80550eb72a433f5ea280f702"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a8f98235e9238a80602806fb60e1261bb"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a908322e5c02500abbdd8891c5248998d"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a93f4973a1229273c51f6a20e741e42ed"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a94fb0f963f706c303729d7a0088ef617"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a96a49382bef8f3163cd82899f59ed5fe"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_a96b0c7868da711271e74b82fcfd32fc2"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_aa9e48c6f0d22e9a64e8591a34409988e"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_ab77f7bda7302cad94805e8ea43b8bf14"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_ae4b9b8ba0e83978f131541959062f691"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_ae88cf07e3c8e6ad64a1beb60270d8961"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_af959f1539f5bbf74b0e63db743a132f4"></a>
<a id="astructbt__hci__cp__le__write__cached__remote__supported__capabilities_html_afbfe48ddad696315d6e021a85d32559d"></a>
<a id="astructbt__hci__cp__le__write__default__data__len_html"></a>
<a id="astructbt__hci__cp__le__write__default__data__len_html_a0ffb8c52d9031dfe448eac0943a4a49c"></a>
<a id="astructbt__hci__cp__le__write__default__data__len_html_a2ada0ea5ee8ac8e6d59fc6adc18421b8"></a>
<a id="astructbt__hci__cp__le__write__rf__path__comp_html"></a>
<a id="astructbt__hci__cp__le__write__rf__path__comp_html_a11aad5607e444cf55dd5878f1f6f9436"></a>
<a id="astructbt__hci__cp__le__write__rf__path__comp_html_a5f99b131f3fba91706bdc8277c1abba1"></a>
<a id="astructbt__hci__cp__link__key__neg__reply_html"></a>
<a id="astructbt__hci__cp__link__key__neg__reply_html_aca3114707eb7c631af582626551619cd"></a>
<a id="astructbt__hci__cp__link__key__reply_html"></a>
<a id="astructbt__hci__cp__link__key__reply_html_a2af0b4b55a5ffcff0221da841ba0cbba"></a>
<a id="astructbt__hci__cp__link__key__reply_html_ab5221952fbcfe413d7c3bd3a441a9b17"></a>
<a id="astructbt__hci__cp__pin__code__neg__reply_html"></a>
<a id="astructbt__hci__cp__pin__code__neg__reply_html_a8aec3ba6c530850dce0a2d7b7f7f86ee"></a>
<a id="astructbt__hci__cp__pin__code__reply_html"></a>
<a id="astructbt__hci__cp__pin__code__reply_html_a627800dcb580110be785576dfcc49bb1"></a>
<a id="astructbt__hci__cp__pin__code__reply_html_aa0cbf668608c3eb4998356ad7b18c01a"></a>
<a id="astructbt__hci__cp__pin__code__reply_html_afc4ed5ae429087f4692af716d6b56997"></a>
<a id="astructbt__hci__cp__read__auth__payload__timeout_html"></a>
<a id="astructbt__hci__cp__read__auth__payload__timeout_html_adcdd657feb3ea6b892e2a5034365dd77"></a>
<a id="astructbt__hci__cp__read__codec__capabilities_html"></a>
<a id="astructbt__hci__cp__read__codec__capabilities_html_a237695f4d0a1359d5ce71d831708a69c"></a>
<a id="astructbt__hci__cp__read__codec__capabilities_html_a6479561573172356d7515ef92f75b8d4"></a>
<a id="astructbt__hci__cp__read__codec__capabilities_html_ad48b7f228742d86a71dffa314331bbe1"></a>
<a id="astructbt__hci__cp__read__ctlr__delay_html"></a>
<a id="astructbt__hci__cp__read__ctlr__delay_html_a2afb9ca8bc2e24cd479b29bc1a53c867"></a>
<a id="astructbt__hci__cp__read__ctlr__delay_html_a5e9f74d4f82809289038da29af0c663d"></a>
<a id="astructbt__hci__cp__read__ctlr__delay_html_a60a6a5b87896d0c27d734b56ead58a9b"></a>
<a id="astructbt__hci__cp__read__ctlr__delay_html_a6c15d141c40bca8bd095f4a86f5a93bd"></a>
<a id="astructbt__hci__cp__read__ctlr__delay_html_ac881526b479d5f1717efbe35cdcc7e87"></a>
<a id="astructbt__hci__cp__read__encryption__key__size_html"></a>
<a id="astructbt__hci__cp__read__encryption__key__size_html_af15765007fd0e2fc4186b54323553019"></a>
<a id="astructbt__hci__cp__read__link__policy__settings_html"></a>
<a id="astructbt__hci__cp__read__link__policy__settings_html_abd2d7c4074428367213b6599dee2f9d8"></a>
<a id="astructbt__hci__cp__read__link__supervision__timeout_html"></a>
<a id="astructbt__hci__cp__read__link__supervision__timeout_html_a96f55e4c89154f5ff911d114a23dc3e4"></a>
<a id="astructbt__hci__cp__read__local__ext__features_html"></a>
<a id="astructbt__hci__cp__read__local__ext__features_html_a79c6a6a6f1026a7e9ee774183ea7e132"></a>
<a id="astructbt__hci__cp__read__remote__ext__features_html"></a>
<a id="astructbt__hci__cp__read__remote__ext__features_html_a6aff189605b276998e58b051429a5cd2"></a>
<a id="astructbt__hci__cp__read__remote__ext__features_html_aaa236c11d148252e34fd20d794d991f3"></a>
<a id="astructbt__hci__cp__read__remote__features_html"></a>
<a id="astructbt__hci__cp__read__remote__features_html_ae14362a04c00b37342f3cc413f3933d3"></a>
<a id="astructbt__hci__cp__read__remote__version__info_html"></a>
<a id="astructbt__hci__cp__read__remote__version__info_html_a504b83f16a82b1e179d74547c7a29bf3"></a>
<a id="astructbt__hci__cp__read__rssi_html"></a>
<a id="astructbt__hci__cp__read__rssi_html_a0662bc56b344ca2bf9a2dcabe8a13c09"></a>
<a id="astructbt__hci__cp__read__tx__power__level_html"></a>
<a id="astructbt__hci__cp__read__tx__power__level_html_a1920e671ec2deda1daf47f06a86d2881"></a>
<a id="astructbt__hci__cp__read__tx__power__level_html_a1c268364fc80b9478d70b7eb997d9825"></a>
<a id="astructbt__hci__cp__reject__conn__req_html"></a>
<a id="astructbt__hci__cp__reject__conn__req_html_a1c2e234d6d00296bc01962b95e849df0"></a>
<a id="astructbt__hci__cp__reject__conn__req_html_a9a1cb4173367c6f018fbd30a47c590b4"></a>
<a id="astructbt__hci__cp__remote__name__cancel_html"></a>
<a id="astructbt__hci__cp__remote__name__cancel_html_a0b7b4362804077ce828aeeb2b8af86b9"></a>
<a id="astructbt__hci__cp__remote__name__request_html"></a>
<a id="astructbt__hci__cp__remote__name__request_html_a5093f7bb70fa36f4948039d02d594e27"></a>
<a id="astructbt__hci__cp__remote__name__request_html_a5d7ea30052f8e4e2b3564659ca187c48"></a>
<a id="astructbt__hci__cp__remote__name__request_html_ab1883aa2b08d89f9c3190f338808a43c"></a>
<a id="astructbt__hci__cp__remote__name__request_html_aed0aea58ca6f5dc15220083d377cbf5c"></a>
<a id="astructbt__hci__cp__set__conn__encrypt_html"></a>
<a id="astructbt__hci__cp__set__conn__encrypt_html_a39e0c40ed6e6e9387ae384fd122fca4b"></a>
<a id="astructbt__hci__cp__set__conn__encrypt_html_aa259563efd49d04a8886f74169fd30b1"></a>
<a id="astructbt__hci__cp__set__ctl__to__host__flow_html"></a>
<a id="astructbt__hci__cp__set__ctl__to__host__flow_html_a75b614de1ab1fbfc6aa9c11d833976a6"></a>
<a id="astructbt__hci__cp__set__event__mask__page__2_html"></a>
<a id="astructbt__hci__cp__set__event__mask__page__2_html_aacf1308d0892226e2c10216a07cd1fcc"></a>
<a id="astructbt__hci__cp__set__event__mask_html"></a>
<a id="astructbt__hci__cp__set__event__mask_html_ab3af227511f47ee03f2d6aba8ae65c5d"></a>
<a id="astructbt__hci__cp__setup__sync__conn_html"></a>
<a id="astructbt__hci__cp__setup__sync__conn_html_a137601ab44970782e2f3d4fcd2c8fcc2"></a>
<a id="astructbt__hci__cp__setup__sync__conn_html_a4d7df5b1aa714bc14d0b6c3cbccc5014"></a>
<a id="astructbt__hci__cp__setup__sync__conn_html_a5ffb5e552d4913974a10a16083f82864"></a>
<a id="astructbt__hci__cp__setup__sync__conn_html_a61ebbc775d3ca0724ea173d72a96e0c0"></a>
<a id="astructbt__hci__cp__setup__sync__conn_html_a6d4c16a4d77d3ee4f8f65ab18a0f192d"></a>
<a id="astructbt__hci__cp__setup__sync__conn_html_aa35718e13a7d778c779be535c2b1945e"></a>
<a id="astructbt__hci__cp__setup__sync__conn_html_ad065185846694fc0070bb366e642f1c7"></a>
<a id="astructbt__hci__cp__sniff__mode_html"></a>
<a id="astructbt__hci__cp__sniff__mode_html_a1896272c588ed2ffe0052353eed528c4"></a>
<a id="astructbt__hci__cp__sniff__mode_html_a37cc61e67148cf8993aa3c6410094d7e"></a>
<a id="astructbt__hci__cp__sniff__mode_html_aa0bfa66eb627378a820144b8ca748b5f"></a>
<a id="astructbt__hci__cp__sniff__mode_html_aaba62465c5fb76641715eed4bc8c25e9"></a>
<a id="astructbt__hci__cp__sniff__mode_html_ad765b1aebc101886d5e9805245252718"></a>
<a id="astructbt__hci__cp__sniff__subrating_html"></a>
<a id="astructbt__hci__cp__sniff__subrating_html_a3534ddbf9876a82855b569ef7e01fd96"></a>
<a id="astructbt__hci__cp__sniff__subrating_html_aa6de505cd8ba606d893dc74590083963"></a>
<a id="astructbt__hci__cp__sniff__subrating_html_ab11c374063c6219b942b839f10d6a74d"></a>
<a id="astructbt__hci__cp__sniff__subrating_html_af25eb1e9ee6eef5888ffa31b9fdd2887"></a>
<a id="astructbt__hci__cp__switch__role_html"></a>
<a id="astructbt__hci__cp__switch__role_html_ac6b6acdaf5993384eb3029c9e78407b6"></a>
<a id="astructbt__hci__cp__switch__role_html_afed76d83e552fa3666f8c84df4279938"></a>
<a id="astructbt__hci__cp__user__confirm__reply_html"></a>
<a id="astructbt__hci__cp__user__confirm__reply_html_abe0e8da3e590c565364ed30ba107a0e6"></a>
<a id="astructbt__hci__cp__user__passkey__neg__reply_html"></a>
<a id="astructbt__hci__cp__user__passkey__neg__reply_html_ade9d7068054b15089b8c238ecc3e4397"></a>
<a id="astructbt__hci__cp__user__passkey__reply_html"></a>
<a id="astructbt__hci__cp__user__passkey__reply_html_a56dbb4a858ecbf36eee61e24ed3742cf"></a>
<a id="astructbt__hci__cp__user__passkey__reply_html_a80483025a32f37e7f75b3a220d48148c"></a>
<a id="astructbt__hci__cp__write__auth__payload__timeout_html"></a>
<a id="astructbt__hci__cp__write__auth__payload__timeout_html_a385c88012b09ec561b9ba7edaadeb574"></a>
<a id="astructbt__hci__cp__write__auth__payload__timeout_html_ad99d5b9f416f11492ac0f412b400aeb6"></a>
<a id="astructbt__hci__cp__write__class__of__device_html"></a>
<a id="astructbt__hci__cp__write__class__of__device_html_acc3b940de1a5da095e8a4f18e69229f2"></a>
<a id="astructbt__hci__cp__write__conn__accept__timeout_html"></a>
<a id="astructbt__hci__cp__write__conn__accept__timeout_html_a13de5f88920c6a41dafa598734b7acf9"></a>
<a id="astructbt__hci__cp__write__current__iac__lap_html"></a>
<a id="astructbt__hci__cp__write__current__iac__lap_html_aaaf3e9c66729a3b4081abb5f8a954108"></a>
<a id="astructbt__hci__cp__write__current__iac__lap_html_ad44e9a0d65bc5140e313176f5b98e932"></a>
<a id="astructbt__hci__cp__write__default__link__policy__settings_html"></a>
<a id="astructbt__hci__cp__write__default__link__policy__settings_html_a644c1ef9ba45ee0675824628fcb9e88a"></a>
<a id="astructbt__hci__cp__write__ext__inquiry__response_html"></a>
<a id="astructbt__hci__cp__write__ext__inquiry__response_html_a755167d683df6c408de57122847bfce0"></a>
<a id="astructbt__hci__cp__write__ext__inquiry__response_html_ae9c89c1f4cac0f16d41b926dc6abc898"></a>
<a id="astructbt__hci__cp__write__inquiry__mode_html"></a>
<a id="astructbt__hci__cp__write__inquiry__mode_html_a827e138b7faaec54ec84a1cc1e0c480f"></a>
<a id="astructbt__hci__cp__write__inquiry__scan__activity_html"></a>
<a id="astructbt__hci__cp__write__inquiry__scan__activity_html_aca01d404676b965f2a03ae16080b8fae"></a>
<a id="astructbt__hci__cp__write__inquiry__scan__activity_html_affe95468faed405a95073b5ba811a053"></a>
<a id="astructbt__hci__cp__write__inquiry__scan__type_html"></a>
<a id="astructbt__hci__cp__write__inquiry__scan__type_html_a6342e77d0c83c1b7c8fd3bd1eeddf8b4"></a>
<a id="astructbt__hci__cp__write__le__host__supp_html"></a>
<a id="astructbt__hci__cp__write__le__host__supp_html_ace1838a80b6061231b536f36e8999ac0"></a>
<a id="astructbt__hci__cp__write__le__host__supp_html_ad2c27c0f98b2334490022e90563e1271"></a>
<a id="astructbt__hci__cp__write__link__policy__settings_html"></a>
<a id="astructbt__hci__cp__write__link__policy__settings_html_a1ba4bd293579e0175efff88429ca1aec"></a>
<a id="astructbt__hci__cp__write__link__policy__settings_html_af3ed335fb8a8774c19ee024c2750e6dc"></a>
<a id="astructbt__hci__cp__write__link__supervision__timeout_html"></a>
<a id="astructbt__hci__cp__write__link__supervision__timeout_html_a1f33613e27db275806eaaa909591e882"></a>
<a id="astructbt__hci__cp__write__link__supervision__timeout_html_a2dd05ca57e20ee4b4fbe2b29cc746bee"></a>
<a id="astructbt__hci__cp__write__page__scan__activity_html"></a>
<a id="astructbt__hci__cp__write__page__scan__activity_html_a8047c7b908154b23985c95a1d792007a"></a>
<a id="astructbt__hci__cp__write__page__scan__activity_html_a9b73713d2960e78a7d6cf1a96c611495"></a>
<a id="astructbt__hci__cp__write__page__scan__type_html"></a>
<a id="astructbt__hci__cp__write__page__scan__type_html_a1717b5ec6e83966e8ef4b61d2ee903a6"></a>
<a id="astructbt__hci__cp__write__sc__host__supp_html"></a>
<a id="astructbt__hci__cp__write__sc__host__supp_html_a48ef951f4de05c5772be5c08edca7cec"></a>
<a id="astructbt__hci__cp__write__ssp__mode_html"></a>
<a id="astructbt__hci__cp__write__ssp__mode_html_a8ebf7f7890adec53aa8c2307d2b1a33f"></a>
<a id="astructbt__hci__evt__auth__complete_html"></a>
<a id="astructbt__hci__evt__auth__complete_html_a7a78803e156218f138866fbb13fdadce"></a>
<a id="astructbt__hci__evt__auth__complete_html_ae2b4b5bcc7195247626004d46ee22dd5"></a>
<a id="astructbt__hci__evt__auth__payload__timeout__exp_html"></a>
<a id="astructbt__hci__evt__auth__payload__timeout__exp_html_a799bc3c63fe5083d61d8bf152ef4cee7"></a>
<a id="astructbt__hci__evt__cc__status_html"></a>
<a id="astructbt__hci__evt__cc__status_html_a97cceaa218700da9b529ebadbb08c42c"></a>
<a id="astructbt__hci__evt__cmd__complete_html"></a>
<a id="astructbt__hci__evt__cmd__complete_html_a3e61d980b4fa3084d3c50ead735fb76d"></a>
<a id="astructbt__hci__evt__cmd__complete_html_a4da0539f81057722c8c322685bc12a40"></a>
<a id="astructbt__hci__evt__cmd__status_html"></a>
<a id="astructbt__hci__evt__cmd__status_html_a34002b693dc201083be4be77cfddcdb5"></a>
<a id="astructbt__hci__evt__cmd__status_html_aed690e1cea2411df167e66cfaa742639"></a>
<a id="astructbt__hci__evt__cmd__status_html_aedd1560409005dbce409b892af1e3edf"></a>
<a id="astructbt__hci__evt__conn__complete_html"></a>
<a id="astructbt__hci__evt__conn__complete_html_a3dbf4fef53279003b7304ffee4a55e56"></a>
<a id="astructbt__hci__evt__conn__complete_html_a60a2ca6a8f16e4562c12b369685efa9b"></a>
<a id="astructbt__hci__evt__conn__complete_html_a975617e8b568675a3ed8883cbe411557"></a>
<a id="astructbt__hci__evt__conn__complete_html_ad8877912008ea7445a67abc43aab5021"></a>
<a id="astructbt__hci__evt__conn__complete_html_afd9a21adf7d35205fb7e222c2e9e0328"></a>
<a id="astructbt__hci__evt__conn__pkt__type__changed_html"></a>
<a id="astructbt__hci__evt__conn__pkt__type__changed_html_aa78e454d08e7c76b3e22242c4855ee62"></a>
<a id="astructbt__hci__evt__conn__pkt__type__changed_html_aabad2dfce94a19a83a5f52e334da18f8"></a>
<a id="astructbt__hci__evt__conn__pkt__type__changed_html_abde9bbcf2afa3c9a49662aa8192de868"></a>
<a id="astructbt__hci__evt__conn__request_html"></a>
<a id="astructbt__hci__evt__conn__request_html_a03a2ee7ff7754173dff0809e4ebce9e6"></a>
<a id="astructbt__hci__evt__conn__request_html_a6059d7c56f45d2fe047a7324db1e820d"></a>
<a id="astructbt__hci__evt__conn__request_html_ae11d550701f64717a7d6df5c89b92d0e"></a>
<a id="astructbt__hci__evt__data__buf__overflow_html"></a>
<a id="astructbt__hci__evt__data__buf__overflow_html_ae0201e03ebb9b9b33e9eae593a56355f"></a>
<a id="astructbt__hci__evt__disconn__complete_html"></a>
<a id="astructbt__hci__evt__disconn__complete_html_a172554fbacf7aaa4dfbafe58b60fa5e6"></a>
<a id="astructbt__hci__evt__disconn__complete_html_ab75f198a6495ad02a00bb3df99ab4258"></a>
<a id="astructbt__hci__evt__disconn__complete_html_aed22ac781e9d70d11e7ebbe6f2e063bd"></a>
<a id="astructbt__hci__evt__encrypt__change_html"></a>
<a id="astructbt__hci__evt__encrypt__change_html_a61cc0e3c209acbb289d071515b44860a"></a>
<a id="astructbt__hci__evt__encrypt__change_html_a7737f659115ca602c1224c364a4c7404"></a>
<a id="astructbt__hci__evt__encrypt__change_html_af063bbd28d29edbcc81e907631167de7"></a>
<a id="astructbt__hci__evt__encrypt__key__refresh__complete_html"></a>
<a id="astructbt__hci__evt__encrypt__key__refresh__complete_html_af5562687a4f6e3a1e82cd1a81cec5ad6"></a>
<a id="astructbt__hci__evt__encrypt__key__refresh__complete_html_afdd162cff0f1eedfe9e8ee7223b3226e"></a>
<a id="astructbt__hci__evt__extended__inquiry__result_html"></a>
<a id="astructbt__hci__evt__extended__inquiry__result_html_a1eba2841941f7cdbb00f548ebf0485e9"></a>
<a id="astructbt__hci__evt__extended__inquiry__result_html_a21f7f48422bcfb867c9ca2e4411a2fbd"></a>
<a id="astructbt__hci__evt__extended__inquiry__result_html_a30c5586d954585006238e8c2b33a7601"></a>
<a id="astructbt__hci__evt__extended__inquiry__result_html_a76e4e82d1dedaee94bd730a4134d7d77"></a>
<a id="astructbt__hci__evt__extended__inquiry__result_html_a955a7d36736badfae1f39fa9eda61ebb"></a>
<a id="astructbt__hci__evt__extended__inquiry__result_html_ab4ebcf09817827d1d10ddeee13832759"></a>
<a id="astructbt__hci__evt__extended__inquiry__result_html_ab6ec4b5efe058e225d173cbda9a16f2e"></a>
<a id="astructbt__hci__evt__extended__inquiry__result_html_aba4aac84e23ca9d283cb8af265dcaf0d"></a>
<a id="astructbt__hci__evt__hardware__error_html"></a>
<a id="astructbt__hci__evt__hardware__error_html_ab7be990e7cc32df43a3c976cb922e333"></a>
<a id="astructbt__hci__evt__hdr_html"></a>
<a id="astructbt__hci__evt__hdr_html_a2d580a0c12b29d23002ee9d494c9e16d"></a>
<a id="astructbt__hci__evt__hdr_html_a87654d507f7ce633a804299bff13abe2"></a>
<a id="astructbt__hci__evt__hdr_html_aba3aca89bfbe7e8cbd144765cb20fcea"></a>
<a id="astructbt__hci__evt__inquiry__complete_html"></a>
<a id="astructbt__hci__evt__inquiry__complete_html_aa8c1e8dc9807476f4759a3b3648b6332"></a>
<a id="astructbt__hci__evt__inquiry__result__with__rssi_html"></a>
<a id="astructbt__hci__evt__inquiry__result__with__rssi_html_a09914ee9998c0b59cb35ed74d08aa4f2"></a>
<a id="astructbt__hci__evt__inquiry__result__with__rssi_html_a0a5c188d0d40b4259cbeb613c0dd12cf"></a>
<a id="astructbt__hci__evt__inquiry__result__with__rssi_html_a1ee08f85103581994a88345cc94d7494"></a>
<a id="astructbt__hci__evt__inquiry__result__with__rssi_html_a6d19e6400d7015db7122516e570d7989"></a>
<a id="astructbt__hci__evt__inquiry__result__with__rssi_html_ad9b4920e2864ed8350de038dffe64574"></a>
<a id="astructbt__hci__evt__inquiry__result__with__rssi_html_af955dd1660f83e41e6d1b2b5aecf8133"></a>
<a id="astructbt__hci__evt__io__capa__req_html"></a>
<a id="astructbt__hci__evt__io__capa__req_html_a52412f7bd8f8dea391904b9f2444b50a"></a>
<a id="astructbt__hci__evt__io__capa__resp_html"></a>
<a id="astructbt__hci__evt__io__capa__resp_html_a160cb3aea96bf698520e11673a40b2d7"></a>
<a id="astructbt__hci__evt__io__capa__resp_html_a851eae620ad90067957d4dec2f04efbe"></a>
<a id="astructbt__hci__evt__io__capa__resp_html_ab12325d1536fe6a75d0a137bea301e8f"></a>
<a id="astructbt__hci__evt__io__capa__resp_html_adac9c9f3999099fd460651e3b012fd0f"></a>
<a id="astructbt__hci__evt__le__adv__set__terminated_html"></a>
<a id="astructbt__hci__evt__le__adv__set__terminated_html_a192f13d6223e437261a225e6b28d04db"></a>
<a id="astructbt__hci__evt__le__adv__set__terminated_html_a583409e2dc912af2bd5e83124fce3a72"></a>
<a id="astructbt__hci__evt__le__adv__set__terminated_html_af2503ee8e1c9add6927fa65b69c48551"></a>
<a id="astructbt__hci__evt__le__adv__set__terminated_html_af35564406269144cfa2532cd510aa0bd"></a>
<a id="astructbt__hci__evt__le__advertising__info_html"></a>
<a id="astructbt__hci__evt__le__advertising__info_html_a11c223103bf89300bd90cb8725746121"></a>
<a id="astructbt__hci__evt__le__advertising__info_html_a1d6863f1a601a2df9d772e3cc1fec118"></a>
<a id="astructbt__hci__evt__le__advertising__info_html_a5943685ccd3491a883ba9450f700bb86"></a>
<a id="astructbt__hci__evt__le__advertising__info_html_af7d9d720ca67714f2a809e2530a1ff98"></a>
<a id="astructbt__hci__evt__le__advertising__report_html"></a>
<a id="astructbt__hci__evt__le__advertising__report_html_a9762be19de1f24be4d4626e7e2f8205d"></a>
<a id="astructbt__hci__evt__le__advertising__report_html_ac69aab36aa421630357e4c6706c13e75"></a>
<a id="astructbt__hci__evt__le__big__complete_html"></a>
<a id="astructbt__hci__evt__le__big__complete_html_a07163dee904412d6d8faca8563a944d9"></a>
<a id="astructbt__hci__evt__le__big__complete_html_a0b0d19d442ed8f1025165c435786ba09"></a>
<a id="astructbt__hci__evt__le__big__complete_html_a14eaa705f1df38337722a41e8189f807"></a>
<a id="astructbt__hci__evt__le__big__complete_html_a2327e42013033767af233d1c2c3acc56"></a>
<a id="astructbt__hci__evt__le__big__complete_html_a2727d329c37e3b3644cfad02d86abb55"></a>
<a id="astructbt__hci__evt__le__big__complete_html_a2847d5fc997f80a3e21b7e03d80c9574"></a>
<a id="astructbt__hci__evt__le__big__complete_html_a6c295870732d65002ec21b4b607e7c0b"></a>
<a id="astructbt__hci__evt__le__big__complete_html_a8b433ac376e347bf391d4dd804c469f3"></a>
<a id="astructbt__hci__evt__le__big__complete_html_a995c8fe06ec087f16b771c38171745b1"></a>
<a id="astructbt__hci__evt__le__big__complete_html_abfa6d6bc135350737451e053aa7d212c"></a>
<a id="astructbt__hci__evt__le__big__complete_html_ad6787806a3622b3bd3da4512bb8ddffe"></a>
<a id="astructbt__hci__evt__le__big__complete_html_ae77364aafe179588f7b8414292e35f5e"></a>
<a id="astructbt__hci__evt__le__big__complete_html_af1c8bd66c3dba70df22f8655b4f27925"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html_a13db0d402636a71ed029575c1e5771c5"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html_a2fa405310a8fed0341001b316ca7bd4f"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html_a31a05f8afb69e5885700cc4ad3b161b2"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html_a383dc92f6d16ec971455e20665cd7496"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html_a451466916fbe2f220c277b4b4e62241d"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html_a48766968cb677614f525ea36551ad6c8"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html_a610313c11c65faf82e06a121affb8b2b"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html_a6b750de25b2a1afc38995030953364ce"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html_a8feb21ef6eacf45dfc09b09e0bce04b1"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html_aebb25f9a63fa013ec6ef891ca498dbb4"></a>
<a id="astructbt__hci__evt__le__big__sync__established_html_afd52315dafe02ee28bc26f058b12fe9e"></a>
<a id="astructbt__hci__evt__le__big__sync__lost_html"></a>
<a id="astructbt__hci__evt__le__big__sync__lost_html_a02b724a60e71805088aefca9989ad878"></a>
<a id="astructbt__hci__evt__le__big__sync__lost_html_ae59a9c18363f7aee67563494d98aa971"></a>
<a id="astructbt__hci__evt__le__big__terminate_html"></a>
<a id="astructbt__hci__evt__le__big__terminate_html_a0303ac64b825f93210dfc70a8a081ea6"></a>
<a id="astructbt__hci__evt__le__big__terminate_html_ad9c9e6d42661366d62d79163fa9ad1c7"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_a084c13c4b0c9c8dca0653b56e53a0c74"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_a12a000c049e85d2b24720d1a362d28df"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_a2301112acf22cf68d6495ff85f0f29bf"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_a81e236ceb24012bc267f656f20f1f8c4"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_a8be20bfc607e6ce34ea75c53e285b0d5"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_a9c1235653245b517a105570c60ddfa09"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_abe0636beae2f51004193ad5f7c9efeef"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_ada35f690706be1c6ee8f40787bbe53e5"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_ae28d5378a7e2ef59fabb62a3a430ccc8"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_ae63eaf93f728109b5fb77ca3179ba99c"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_ae68f803bbc3f06e7190f62be98d2fe66"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_ae92b69ab0bc257d4f50b98e071c6038b"></a>
<a id="astructbt__hci__evt__le__biginfo__adv__report_html_af3a871d3de34b90fc2b09b0725caf479"></a>
<a id="astructbt__hci__evt__le__chan__sel__algo_html"></a>
<a id="astructbt__hci__evt__le__chan__sel__algo_html_a16393279e08073dad549e111e610c8e8"></a>
<a id="astructbt__hci__evt__le__chan__sel__algo_html_a976a62e81b094a59ce42cb6ad3ce45ac"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a1f43b72368227f212511bb248b4a0e22"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a26b25e1615991977735cbfc679d747f3"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a2a060c0bb2831eb3df0dc8ffb74ecebd"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a2de704a032ac2379528991f2d01e6979"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a353409fe069aba91c5372ee8ae6e1b79"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a3b1fc27cca2bc85c36e257aabd8ea612"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a5a0b08098ac4e6ec93a6ecbbbf4ef587"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a5f68c3cba98ed96afef0949f6b14ded9"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a64b48b20283415100fc8bdf33edf2b0e"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a71762f8a31e20b233a252ac974f6d329"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a754ad7e68821da0bdb8da0bdeb3b4697"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a7a7b8303183a916225bb0a3ea11d5480"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a926a5faeb98a99333310d860da37f6f5"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_a9b7ba96597a5131927e365b7a45f8d6f"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_ac3a87b20b2f10e980639d232a013f702"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_acd8cf2d2d85b65d839256f3412a4bb43"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_acf30d6a745803fd4e984d66548ceff58"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_ad054af39ddad854423379b3cc7aafc26"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_ae580ff8c0ef4cd03365cbf1a06aed8bc"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_aeea230245aa75dd7f44bf5a4a286e9a5"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_af134783424a77274abac44613bf61264"></a>
<a id="astructbt__hci__evt__le__cis__established__v2_html_af59ca6d54ca770ef8334ea091bcc53f6"></a>
<a id="astructbt__hci__evt__le__cis__established_html"></a>
<a id="astructbt__hci__evt__le__cis__established_html_a0bcdc0d8b3b776660d2e51427f9634dd"></a>
<a id="astructbt__hci__evt__le__cis__established_html_a200afaff044b9eea653d8aee13297dc2"></a>
<a id="astructbt__hci__evt__le__cis__established_html_a25b84cf026775b582c7944e265ffb0b2"></a>
<a id="astructbt__hci__evt__le__cis__established_html_a4d90dbeda130a6142ff0b7f9e2ee7c16"></a>
<a id="astructbt__hci__evt__le__cis__established_html_a53ea1da3f31313ab73b511c72912bd33"></a>
<a id="astructbt__hci__evt__le__cis__established_html_a683856418764b1110d5c5fea0494fe1e"></a>
<a id="astructbt__hci__evt__le__cis__established_html_a877913bb4b9016c64793458de94d84a0"></a>
<a id="astructbt__hci__evt__le__cis__established_html_a932e8df0222eb3bcf7bee753414d529e"></a>
<a id="astructbt__hci__evt__le__cis__established_html_ab6b2d892e3c1e4f6aedee722049b75d3"></a>
<a id="astructbt__hci__evt__le__cis__established_html_ac4e5a2535e3e8d3782adac63a4c5a8d9"></a>
<a id="astructbt__hci__evt__le__cis__established_html_ad0a79bfadd413bf572b697069695c0a5"></a>
<a id="astructbt__hci__evt__le__cis__established_html_ad0f3bd5f81b660afbc4927a777c2c18e"></a>
<a id="astructbt__hci__evt__le__cis__established_html_ae71d6753849ae3c57327c8763cab1802"></a>
<a id="astructbt__hci__evt__le__cis__established_html_ae8b195f433570e28e42a5f9d321964de"></a>
<a id="astructbt__hci__evt__le__cis__established_html_ae9fdecff4342f25de30165a4531ad703"></a>
<a id="astructbt__hci__evt__le__cis__established_html_aefb2d4e0458cbe990903a9f449189c30"></a>
<a id="astructbt__hci__evt__le__cis__req_html"></a>
<a id="astructbt__hci__evt__le__cis__req_html_abdf99eeb7a30c8238bbabdcd60a4847a"></a>
<a id="astructbt__hci__evt__le__cis__req_html_ae0ef0ac224bde55de13df4e5eeaf26be"></a>
<a id="astructbt__hci__evt__le__cis__req_html_aeed6f4bf58cdb301d6b784a202722acc"></a>
<a id="astructbt__hci__evt__le__cis__req_html_af8529013adb87340298a89d4727e6867"></a>
<a id="astructbt__hci__evt__le__conn__complete_html"></a>
<a id="astructbt__hci__evt__le__conn__complete_html_a3fff4c3b30da5922f75d36d97fdeee33"></a>
<a id="astructbt__hci__evt__le__conn__complete_html_a4a90c9824d167b6c45b301e18bfe7f17"></a>
<a id="astructbt__hci__evt__le__conn__complete_html_a67618a1efa0149fadc1063a719d5b674"></a>
<a id="astructbt__hci__evt__le__conn__complete_html_a8455e714d4333d90c2f117892f3dcd6f"></a>
<a id="astructbt__hci__evt__le__conn__complete_html_a897981117139c0e53ea7275b689f3799"></a>
<a id="astructbt__hci__evt__le__conn__complete_html_a97e1aaa10832292ddfe4ee6731ef8999"></a>
<a id="astructbt__hci__evt__le__conn__complete_html_ab60cb42ecc83632c61656cd352b71cbe"></a>
<a id="astructbt__hci__evt__le__conn__complete_html_abe4bc0407d0295329631cb14672a7ee7"></a>
<a id="astructbt__hci__evt__le__conn__param__req_html"></a>
<a id="astructbt__hci__evt__le__conn__param__req_html_a0ed70d1a89f270073f78823d38af6ac9"></a>
<a id="astructbt__hci__evt__le__conn__param__req_html_a4746a001a070f152a3c1c870a7e74df1"></a>
<a id="astructbt__hci__evt__le__conn__param__req_html_a9a9dfc026feb46337b0a36920204b24e"></a>
<a id="astructbt__hci__evt__le__conn__param__req_html_a9f61f0a3e6b6d2e2c6af2f4aef625b75"></a>
<a id="astructbt__hci__evt__le__conn__param__req_html_ae34de4a3d3e3e4686391eb9d9585dc87"></a>
<a id="astructbt__hci__evt__le__conn__rate__change_html"></a>
<a id="astructbt__hci__evt__le__conn__rate__change_html_a10671dd6e9b30b112e5841c482ee3067"></a>
<a id="astructbt__hci__evt__le__conn__rate__change_html_a29d6bdbf04cb6bc68a84f3fafaf66a1f"></a>
<a id="astructbt__hci__evt__le__conn__rate__change_html_a3028aa8284c2f656f71d4b25da862cc9"></a>
<a id="astructbt__hci__evt__le__conn__rate__change_html_a31deb63251c897f7627b67c7cad2521f"></a>
<a id="astructbt__hci__evt__le__conn__rate__change_html_a5b3947e67027b5425c21a0d509e19dc5"></a>
<a id="astructbt__hci__evt__le__conn__rate__change_html_a67429e04fe601f367deeb5637d7d89c9"></a>
<a id="astructbt__hci__evt__le__conn__rate__change_html_a8ad1a15c8b26be65d92944b4fc3c0ae1"></a>
<a id="astructbt__hci__evt__le__conn__update__complete_html"></a>
<a id="astructbt__hci__evt__le__conn__update__complete_html_a69aa00c0c50978b2aa620aad671119f3"></a>
<a id="astructbt__hci__evt__le__conn__update__complete_html_a81c0688a5e3b4b3a4d92fbc756a068d5"></a>
<a id="astructbt__hci__evt__le__conn__update__complete_html_aca728975619a10a6e3280b127b59f2f1"></a>
<a id="astructbt__hci__evt__le__conn__update__complete_html_ad428bd5e29d40f7551ccdd0747e429d6"></a>
<a id="astructbt__hci__evt__le__conn__update__complete_html_ade2421709a35e0cd0fce3a4d992470c3"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html_a0188ce28a6c0a2002ae2c64a7bd95e52"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html_a135498a4abae604967f94840e2f88d2c"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html_a1f388ba96bd52f9ce0f68bacb2945ed8"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html_a446f4eab3db19452a84023a676333d1d"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html_a49e63523f7219174540666c7e5ab3550"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html_a5acc2683312523a1137db7897a7373a6"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html_a74670ca77bb2be81db2cee613dd9c82b"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html_a801dd9373935ba06175ac52237fea759"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html_aa052e03491647acc9f7a6dc7d91cedcc"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html_ac01a14c591c8bd8e6313aff021ca8d61"></a>
<a id="astructbt__hci__evt__le__connection__iq__report_html_af66e8f09a4442b658b80a6eb4dd3064b"></a>
<a id="astructbt__hci__evt__le__connectionless__iq__report_html"></a>
<a id="astructbt__hci__evt__le__connectionless__iq__report_html_a09112f3711aca00b56045c46958c0992"></a>
<a id="astructbt__hci__evt__le__connectionless__iq__report_html_a1a81f2c8653d85dc29582eed67b4a2a8"></a>
<a id="astructbt__hci__evt__le__connectionless__iq__report_html_a36f853d29b8dae1dd393546bbdec5ae2"></a>
<a id="astructbt__hci__evt__le__connectionless__iq__report_html_a39109ea3f657d0566a73c7ca81bdd2b1"></a>
<a id="astructbt__hci__evt__le__connectionless__iq__report_html_a6b11b00199b002129c569cfec6e83174"></a>
<a id="astructbt__hci__evt__le__connectionless__iq__report_html_a9d9f0cfe343d81c44e8342b81e2a0608"></a>
<a id="astructbt__hci__evt__le__connectionless__iq__report_html_ab6fb0f6e32e32a3364ae79d867d9e640"></a>
<a id="astructbt__hci__evt__le__connectionless__iq__report_html_abfeb0aaa411464bbd7bca927219144fb"></a>
<a id="astructbt__hci__evt__le__connectionless__iq__report_html_af50e710884a17191d22f652eaf5788fd"></a>
<a id="astructbt__hci__evt__le__connectionless__iq__report_html_af8c2055666a97f3c8d95747c59515c31"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a14f4c29a7f84463f048364389341c7b5"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a1e5ba3ebb5dcac2105a0f859683505bc"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a21928853b505764e64fcc9190905b12c"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a45a1b908385be6a5289698dd08d8a610"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a511021f717538d4ae25eb28ad82c5f99"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a544b3480034087ca01d64a41c1c4b8f9"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a55789928018a6124d87e76709b1b77d9"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a5f886c16acd561e143a8796fcc1ea5af"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a6f84ebf8a34a830ced1fc738d46fe244"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a705a7be2d5ce02c4d78319f4f842b87e"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a73bd134e9337a9a47e41bba04623ee0b"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a748fcb3cbd396851a3d159887b12b3e0"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a7aa0fd8a1c9c7270059725416dd0a90f"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a7d64425b6aa44b01332ce6fac7813471"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a7fe1af954bae025b9b8bbef70bd1c60e"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a8fafd0e139a9c85830468e5a056c42b7"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_a9b14655fa6bb3c7ac43561a399019a76"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_aa323b4a74f7fce33e884d0c32e4014d0"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_abcf0c43f33a85bcd860323212d57ce5b"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_ad0454e31d55ec25a21bc272cae999238"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_ae64ff5dbd9d704c3a7f4c5b98ada399c"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_ae94aa8c92a8d4b33213adc8fc029a02d"></a>
<a id="astructbt__hci__evt__le__cs__config__complete_html_afd62b1ffe5388c7f094cb086da4c86ba"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_a17b62e13cda5f47dee2e8873686b978e"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_a5822ff654eee794442a05033e0f10fae"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_a60a9e00cba665d73e65d0ee5b0d9efbc"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_a688bfcb6781b2e3480f021c66a3109fe"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_a7a38c8ced8720a428df42e821ec7e9e6"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_a7ff8f1e713d9b835f3a4e0e79cb1b3d1"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_a8f5485967662dbd1676d8edd6345fd13"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_aacc14948a9e6c384ec94051fb4323599"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_ac8489dc8ff5f9bf052a7c1a67a544106"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_ad7c21907a38747ec405c992ef14e8dd7"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_adcf8e32c2346073e0fbe273d261f6741"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_af5959274cb88a8e4fdf09e8dd756f31c"></a>
<a id="astructbt__hci__evt__le__cs__procedure__enable__complete_html_afd760c9b6809e6764a652ecb3ee4c2b5"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__fae__table__complete_html"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__fae__table__complete_html_a1ee4d133955f28f45d16226730344428"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__fae__table__complete_html_adcdfbfd2d9c19be0c41121235fbb8eaa"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__fae__table__complete_html_ae1ca6d2d4f4305565f1d491ef202fcad"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_a07642a2edeb882e5c9a2a7727e8a55fd"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_a0c60c0b2677a8635a185277453db9613"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_a2e7d55a93000730a565c93b3394186e3"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_a365c4afcf1c034bb42c24ce4bedbf1c3"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_a43a8dd8b09c9e498b64798fcfe73af53"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_a73b7054a056ca3256098608e565033b2"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_a77669a86a0c75439417d4e53629a9cfd"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_a8695548057df5e398f65de93fd097b04"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_a974007b9f1d81991f55c40cb1da1c51e"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_a9e2a36e0181a8cf5a9d61b8b31e21617"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_aa3e4e049cbb322a35171686635e2cc9c"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_aa78b03177bbfc69de0a066f610b1cfa6"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_ab21b4a5b2e3005fc3589251c7b8f77f1"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_ab692972f1388e6641493a5cc0faf2fac"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_ab93bb486d50a79c34a6002885436605b"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_aba890de001e752b497bc91bd6356c359"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_abe01a9d4d6fdb042fdfa5c045ac66519"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_ac130ecc14ce78f0c179ad56a1985d60c"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_ad1f03a6a550a5c5cb9b0c997c239ba6a"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_ad5c7c16d0b2096d4c00156800bf9181b"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_adb3ce0c00b922e72373a93cb5d0f2f1f"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_ae8091780f4153ead9a9414593b648f5a"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_af7f35ce7c16fc7cf1d76be1450d4566c"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2_html_aff9e1f081101d2eabc83a7a2ce99d64f"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a0a1d9dcdf184e49349e86980da2e4bed"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a1f303dc3aa8a23fccde27a2d2f64d732"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a21a322fc8efd0c410dda78e2652d506d"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a3f275ad58ca745347172ad0b89faf2c4"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a40980265955d4d58a9b5407ff845fde4"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a44869fd19ae813830e38f6e4b88dbb1d"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a4f8fe99c2392c06125ba94e61aed0e6c"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a50ad0408019dce16685215c6a1b6d0ef"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a7af3067f319be094af31512d4ee5101e"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a7f796e2eda8d3c7eae556932e37cd93d"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a843968ec69106d076596e110407d8a1a"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_a99f9f7b08de6b41e88cea10ba0ca6010"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_ab09a466b2a9a0be5f5021f1da0d7393a"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_ab7a35b1093ece7ae9cc5def4a3e473b2"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_ac73a8bf5425c80739e84cb30ce94f3e7"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_ac83543c17606e401d919fce841a12c6c"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_ace95740224b31c127f5e13550cb5a23a"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_ad330adf1ae5b9b84756d36801a4cf289"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_adcf35e055d04775c444fa28655b95337"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_adebb5328c7baeaa786bc185fec432e40"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_ae3d06bce4df7a2ca07c5d6dd01124743"></a>
<a id="astructbt__hci__evt__le__cs__read__remote__supported__capabilities__complete_html_afef9f37784d75f54521793f07b5baece"></a>
<a id="astructbt__hci__evt__le__cs__security__enable__complete_html"></a>
<a id="astructbt__hci__evt__le__cs__security__enable__complete_html_aaa96a8944598914e4439249ba489f726"></a>
<a id="astructbt__hci__evt__le__cs__security__enable__complete_html_aaf2de8591b18cd36709f7ef755bee917"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__continue_html"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__continue_html_a1801aeaac839831198e17b7d96a5532a"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__continue_html_a2f8e1f634e28100815c881a463b51f2c"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__continue_html_a3c7ac056a5898710ffbc0776ef551b4b"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__continue_html_a3e5b1e8a247fff36c06447c9ff7c3bb8"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__continue_html_a4126bebec093f6f4d1a22b43abec6b1c"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__continue_html_a49cf181c8518fb3015a0c54f7558aa8c"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__continue_html_abbddd0e27178e49abe6eef62bc094a16"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__continue_html_adefb9ad1f998460a6d235ebd39bbfe4a"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__continue_html_af127774b52c4e088f628999136b6cd7c"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__step_html"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__step_html_a1f074ff26f779292ea32bb405f37b877"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__step_html_a65f6ecf6355883df7924067edc277f35"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__step_html_a7fb65809d78fbf08528f177d98e72f6b"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result__step_html_aebb0c47275e4cf92802314a82ffba820"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_a0d6b2ca9f148173abb6207cf7c473c7f"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_a27a2848009838977f26df75bfc9bc3c3"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_a2e8bdef7f85a4cefeaf625d0c3a4db03"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_a3b9c8392fa3aadc2e0673923e0346278"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_a43b46a37648b9fde72634dd7dd6a68e6"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_a9931d5818b801a9c36853f88b259c25e"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_a9a7260f63122a94cf7eb6ddc3344f742"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_ab81c9c55697b2f2c92e3ea2073932ad1"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_aba480f7ad78069fd8b83493fac42244e"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_acf6f9c4e6fa5897be872d9953993517b"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_ad08558fd68eb6c43d95a3f0f62bafff0"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_aeda28dfb30c51ce2955e1c313069c111"></a>
<a id="astructbt__hci__evt__le__cs__subevent__result_html_af8c827d508614f553b9f503d0394411b"></a>
<a id="astructbt__hci__evt__le__cs__test__end__complete_html"></a>
<a id="astructbt__hci__evt__le__cs__test__end__complete_html_ae083dabff641736ed9a23ffc5a36a737"></a>
<a id="astructbt__hci__evt__le__cte__req__failed_html"></a>
<a id="astructbt__hci__evt__le__cte__req__failed_html_a1433f25dee38014dbd2d061b6d75741a"></a>
<a id="astructbt__hci__evt__le__cte__req__failed_html_aa903954fa411e4ae49a613b4e76219dc"></a>
<a id="astructbt__hci__evt__le__data__len__change_html"></a>
<a id="astructbt__hci__evt__le__data__len__change_html_a60ecd89a8bbf06ae55b577e3d708d16f"></a>
<a id="astructbt__hci__evt__le__data__len__change_html_a62ebc2f337f23f678c651bf3a276a2a7"></a>
<a id="astructbt__hci__evt__le__data__len__change_html_a8264e7ec4aa37e9a699f81d0c56afa40"></a>
<a id="astructbt__hci__evt__le__data__len__change_html_a90771e400b998565e7a8bbf4288edd01"></a>
<a id="astructbt__hci__evt__le__data__len__change_html_ae5ce481170336acafbe85687c672281b"></a>
<a id="astructbt__hci__evt__le__direct__adv__info_html"></a>
<a id="astructbt__hci__evt__le__direct__adv__info_html_a013e5d53ed53e4cd0b923a55c68e20bc"></a>
<a id="astructbt__hci__evt__le__direct__adv__info_html_a66bbb3e53d84e8c39b216edf91ad131d"></a>
<a id="astructbt__hci__evt__le__direct__adv__info_html_ad4ca2d5395bc4c5b95527ac1491c940e"></a>
<a id="astructbt__hci__evt__le__direct__adv__info_html_aed957c96860c5f92f9485ab743ce832b"></a>
<a id="astructbt__hci__evt__le__direct__adv__report_html"></a>
<a id="astructbt__hci__evt__le__direct__adv__report_html_a82800d58d4c3ed1fca49b6575bd8f957"></a>
<a id="astructbt__hci__evt__le__direct__adv__report_html_ae8d1f96739c8fda8827d1c0521f00f94"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_a014e8bf891684c4cd9e5ec53d986d412"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_a10a1cbf0e9e21bc127dc64adadd53773"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_a237b8313970cc63b7e57c0ce4913392e"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_a2b2ac4890eb9604a3f5cd40f55c2c066"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_a3343de57a24fa2ebdccf9411f388817d"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_a3daa32ac19c4eda4a49bebb64f3145be"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_a7bb168061803d1122e8ee47dc8af3ae9"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_a7df28c9ddec607d5a84572bb421b7f5a"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_a81dca94a6f2a8ea3da7a5a316daa5941"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_a883ba3aed9aed00ec0ce425999d97180"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_ad72ba07d766135a94474a9d004da1a66"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete__v2_html_affe2dba0634e0215579fb13d77016a8c"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete_html"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete_html_a13ceff445de6a89f6ea0e832e8b3fba9"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete_html_a4906d6991489e95f8c74aacf5ad8c22e"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete_html_a4ece4379733f1ab404fa03f4794192a4"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete_html_a5641e5cb17df4613cd85f5ad3ba8541c"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete_html_a7276bf433c21ffcd3582463492af107b"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete_html_aa99df131f3fb0330ff8051015d2b78dc"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete_html_ab275bcb4a3dd09525b446c01e4e5fdad"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete_html_ac0565ecf0c459275d147933bbdaa9fbc"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete_html_ae26575416658bf285c45f57ddf426eb2"></a>
<a id="astructbt__hci__evt__le__enh__conn__complete_html_af24298f8c1d58882b4962a14086fc5c7"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html_a040c27dbcb337162f7ca857b8cb84cfe"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html_a088f0e6ea0dfbad25d5f72d0741f7d6d"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html_a20ca10813f6b3aaba2756a5fe00d3878"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html_a37f4e4981566b43d6e7c7dfffc5b13fb"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html_a39217e77e495e8c4c6288917f8e4d2dc"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html_a5b4d4adff4d97c06311a76abd9847727"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html_a6213edbc3ae30f02a6bf2d8e069cd035"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html_a7da4e49c49eccbf009491bb7da01e111"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html_a9e5536277b0132c8374147677a787b68"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html_acec6858e41ae1b44a2a2ee6d6dbc294d"></a>
<a id="astructbt__hci__evt__le__ext__advertising__info_html_af4d863e12e6f8f19426a14af292fa6d2"></a>
<a id="astructbt__hci__evt__le__ext__advertising__report_html"></a>
<a id="astructbt__hci__evt__le__ext__advertising__report_html_a72fc9736934b415e88c51a1f96179871"></a>
<a id="astructbt__hci__evt__le__ext__advertising__report_html_a84b9c47a79ccea04198721e2f05ac1a8"></a>
<a id="astructbt__hci__evt__le__frame__space__update__complete_html"></a>
<a id="astructbt__hci__evt__le__frame__space__update__complete_html_a1b306ba860123344436f85914455d784"></a>
<a id="astructbt__hci__evt__le__frame__space__update__complete_html_a2ec660b66b28fe0ab69b9db5681a5b17"></a>
<a id="astructbt__hci__evt__le__frame__space__update__complete_html_a66d0db4fa276b0a839ce97b0c6868ae4"></a>
<a id="astructbt__hci__evt__le__frame__space__update__complete_html_a8da9f4e322bd41f5870ea5cec0092584"></a>
<a id="astructbt__hci__evt__le__frame__space__update__complete_html_adb081f887bc36892fc98fe78d170d93d"></a>
<a id="astructbt__hci__evt__le__frame__space__update__complete_html_af39f49f398848cfddda3edf70432a5fd"></a>
<a id="astructbt__hci__evt__le__generate__dhkey__complete_html"></a>
<a id="astructbt__hci__evt__le__generate__dhkey__complete_html_a3d10643dd45a71b71d35dfa455ed8590"></a>
<a id="astructbt__hci__evt__le__generate__dhkey__complete_html_a8cd8ece786c1443ed43bd3b8fcd4d9bf"></a>
<a id="astructbt__hci__evt__le__ltk__request_html"></a>
<a id="astructbt__hci__evt__le__ltk__request_html_a0fcb7c6f8c52af50caa41d446294d72c"></a>
<a id="astructbt__hci__evt__le__ltk__request_html_a14e8e3e380efd91ca5402b43bee7c9d3"></a>
<a id="astructbt__hci__evt__le__ltk__request_html_aed00ae384cb7d0deace8d0cc0f8e0068"></a>
<a id="astructbt__hci__evt__le__meta__event_html"></a>
<a id="astructbt__hci__evt__le__meta__event_html_a536464a525f8d0f9df915be5ee3d33da"></a>
<a id="astructbt__hci__evt__le__meta__event_html_a5f08a4c81ebab1638d251b3bf7f8bfab"></a>
<a id="astructbt__hci__evt__le__p256__public__key__complete_html"></a>
<a id="astructbt__hci__evt__le__p256__public__key__complete_html_a57d51fca3a707b445db2534d1e175241"></a>
<a id="astructbt__hci__evt__le__p256__public__key__complete_html_af482f81d438b878fb826edbac8d84833"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_a00bf4bdf12fce6cbf2874b9c4ae09f9f"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_a05d798c9415541ef7f5716992157b1a1"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_a736af2c2ee0afd3cb00e8eb4d103991c"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_a78853d14c3bf9a9aba3c4e15b2e06abb"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_a9f55d5f6d17d11e72f7cac363a69fe97"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_ab8a2a55fe071218284d60f1a2896945b"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_acf711399e575295dcef73cfeeb844eab"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_acffc2fa22a16a3a12a4f7dfc3bb45866"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_adb011949f592ec7f8843d4fd47eca2e9"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_ae7a73293519ab45aec40a9a1aeaa4e89"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_aefdc5ac7ef125f4dc5865c198b98c67d"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_aefe79f973eda8c7c5670c7a721d55d8a"></a>
<a id="astructbt__hci__evt__le__past__received__v2_html_aff78554e8980635290767e9877ac479b"></a>
<a id="astructbt__hci__evt__le__past__received_html"></a>
<a id="astructbt__hci__evt__le__past__received_html_a00d570636a55c1d84723ad3bc5705d80"></a>
<a id="astructbt__hci__evt__le__past__received_html_a110c7cdd2ff1178d1ca686abaae92b05"></a>
<a id="astructbt__hci__evt__le__past__received_html_a1b2c229c99d06f44057b88458f168e7c"></a>
<a id="astructbt__hci__evt__le__past__received_html_a1bdbaddb4003cea40738ee540ecb8789"></a>
<a id="astructbt__hci__evt__le__past__received_html_a2cea2f3b9d51ace91ddf63639e821328"></a>
<a id="astructbt__hci__evt__le__past__received_html_a3e368e95a6831f823d2efa0c0bc1ef51"></a>
<a id="astructbt__hci__evt__le__past__received_html_a41ea6099d3cca1caf37ff518a4e95492"></a>
<a id="astructbt__hci__evt__le__past__received_html_adaa1e432db60a2529ad6266f16604e15"></a>
<a id="astructbt__hci__evt__le__past__received_html_aedb668e6f3232b1db9035ea89ccf1b71"></a>
<a id="astructbt__hci__evt__le__path__loss__threshold_html"></a>
<a id="astructbt__hci__evt__le__path__loss__threshold_html_a19b1e37c5e35e1e18424615b5c25d37f"></a>
<a id="astructbt__hci__evt__le__path__loss__threshold_html_ac2b04c57137dcb6812fda06d4a22402a"></a>
<a id="astructbt__hci__evt__le__path__loss__threshold_html_add7984e06d523bb34e8380dae1710b7f"></a>
<a id="astructbt__hci__evt__le__per__adv__response__report_html"></a>
<a id="astructbt__hci__evt__le__per__adv__response__report_html_a37f3519eefe33e87d49c7c2ad0f8b40c"></a>
<a id="astructbt__hci__evt__le__per__adv__response__report_html_a3b1bcca7a7dbc6fcf5709f6152268b87"></a>
<a id="astructbt__hci__evt__le__per__adv__response__report_html_a46a5b74321a80697fd700a276be18ed3"></a>
<a id="astructbt__hci__evt__le__per__adv__response__report_html_a9d746015a9c2b48c54008319c892b063"></a>
<a id="astructbt__hci__evt__le__per__adv__response__report_html_ad4f8f61150f82f4ba420e3c0a1f333c2"></a>
<a id="astructbt__hci__evt__le__per__adv__response_html"></a>
<a id="astructbt__hci__evt__le__per__adv__response_html_a1100429baf398067a396a6ba8db6778a"></a>
<a id="astructbt__hci__evt__le__per__adv__response_html_a4197fbae54be038502312efc14b66320"></a>
<a id="astructbt__hci__evt__le__per__adv__response_html_a74e304822ec7a431802cf8a7539d640e"></a>
<a id="astructbt__hci__evt__le__per__adv__response_html_aa524756d2cce0718ecfd66704eaf389d"></a>
<a id="astructbt__hci__evt__le__per__adv__response_html_aa5b5467f4edd52fb8de078b0948141f0"></a>
<a id="astructbt__hci__evt__le__per__adv__response_html_ace3b58eba63b55ce5f3038d4a7877ec2"></a>
<a id="astructbt__hci__evt__le__per__adv__response_html_af68f0dc92118f78f6f5b0ffbf1854664"></a>
<a id="astructbt__hci__evt__le__per__adv__subevent__data__request_html"></a>
<a id="astructbt__hci__evt__le__per__adv__subevent__data__request_html_a45cdb248b80602a7f14f24e0324e6f97"></a>
<a id="astructbt__hci__evt__le__per__adv__subevent__data__request_html_a8f7fd9b149aa52422cb3eb874b91943d"></a>
<a id="astructbt__hci__evt__le__per__adv__subevent__data__request_html_ae6f6ef17edabfd210a7e6597087ff512"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html_a0ce9a9170d93ff69f25ff35eb163511f"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html_a13ab0e87d6673a34e51f3112a5fd5a0c"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html_a36b5c8454ee3635d2298592c83166f14"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html_a958630cb9e275ab6f8ed0c548958e5ee"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html_a96b975f5a2fcf193b0b58c230486ec36"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html_aacb6946dbfeb2ffbc251910853559329"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html_ab7d3793e782d7b2bb311b8a5ac3a871b"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html_abd67ec989479eb793e7bf99a4cf371b8"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html_ac4c2bc8789513692ce0f2cc81aa59476"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html_ad21df6269d8242d94ba9cbc1e0d4d344"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established__v2_html_af4fb92baa4f98c08c990ba505faf9226"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established_html"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established_html_a3af8529a858992f347ce9570c5696133"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established_html_a4873b917a5bc140bb2f04ad2bee5dd69"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established_html_a9ebe918fee3121168dc5b45e64aaf263"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established_html_ab11929ef8d3c71c6f2cb7c549be21282"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established_html_ab7ce6f56a69b54f02cde8fdae6860e42"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established_html_adf65527ea968f4ece37d7e3c91c795d1"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__established_html_aee68069899cc10bc38ad9fb95cf9b7b7"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__lost_html"></a>
<a id="astructbt__hci__evt__le__per__adv__sync__lost_html_a286d534634411da53a2bda8cdfb077f8"></a>
<a id="astructbt__hci__evt__le__per__advertising__report__v2_html"></a>
<a id="astructbt__hci__evt__le__per__advertising__report__v2_html_a30f4e81346957ad4f9f0488dd93fafc3"></a>
<a id="astructbt__hci__evt__le__per__advertising__report__v2_html_a3276c2e11c946744b73426f54bf62b8c"></a>
<a id="astructbt__hci__evt__le__per__advertising__report__v2_html_a34b15fb9b5b4f0d199ccf274dd489c6a"></a>
<a id="astructbt__hci__evt__le__per__advertising__report__v2_html_a37a9eb7d417da9285e22cc7f83071c69"></a>
<a id="astructbt__hci__evt__le__per__advertising__report__v2_html_a499d82e1e3cfc501d399f570ebbcdc42"></a>
<a id="astructbt__hci__evt__le__per__advertising__report__v2_html_a73496cc962721538e27e9924fff0f3db"></a>
<a id="astructbt__hci__evt__le__per__advertising__report__v2_html_a7af1cd4ec9df24e575a83a640eea36d2"></a>
<a id="astructbt__hci__evt__le__per__advertising__report__v2_html_ad598ffd0108825803a4734959a354bd8"></a>
<a id="astructbt__hci__evt__le__per__advertising__report__v2_html_af27b23fe38e9ff092d8839cd81749456"></a>
<a id="astructbt__hci__evt__le__per__advertising__report_html"></a>
<a id="astructbt__hci__evt__le__per__advertising__report_html_a0ab1d3c5d7eb1487862451cc65c66a76"></a>
<a id="astructbt__hci__evt__le__per__advertising__report_html_a1f9cdfc01e46e59e957b0c557bae620a"></a>
<a id="astructbt__hci__evt__le__per__advertising__report_html_a3a09aca94284a9e4af765d4da543698e"></a>
<a id="astructbt__hci__evt__le__per__advertising__report_html_aa683d1a4bd3a851f26b3028f566b76e4"></a>
<a id="astructbt__hci__evt__le__per__advertising__report_html_abf23b23a12cbfeb7f996e71e2fe8b11c"></a>
<a id="astructbt__hci__evt__le__per__advertising__report_html_af81ce5bb18ef7fa1d94d00412886b081"></a>
<a id="astructbt__hci__evt__le__per__advertising__report_html_af874c29b89326877b499f6be1052a626"></a>
<a id="astructbt__hci__evt__le__phy__update__complete_html"></a>
<a id="astructbt__hci__evt__le__phy__update__complete_html_a70f472edef3b25fb23490ea6dcce9d43"></a>
<a id="astructbt__hci__evt__le__phy__update__complete_html_a927a9e6982b29ecd4c3972b19a9bcdc2"></a>
<a id="astructbt__hci__evt__le__phy__update__complete_html_ad184e10b7af71582db64ec5d3a66cff9"></a>
<a id="astructbt__hci__evt__le__phy__update__complete_html_ad792ffec08aa8e383009e2e353a03fcd"></a>
<a id="astructbt__hci__evt__le__read__all__remote__feat__complete_html"></a>
<a id="astructbt__hci__evt__le__read__all__remote__feat__complete_html_a3582ff03fd6a680e006b94ff6080dc37"></a>
<a id="astructbt__hci__evt__le__read__all__remote__feat__complete_html_acab09b5b552faef296c6e0442c4a2bc9"></a>
<a id="astructbt__hci__evt__le__read__all__remote__feat__complete_html_aefc3508368f6a103c9b2d218f66f6a11"></a>
<a id="astructbt__hci__evt__le__read__all__remote__feat__complete_html_af4a77910c32dbbdb259a9532818a0746"></a>
<a id="astructbt__hci__evt__le__read__all__remote__feat__complete_html_afd04ae00d6ce4b2cb57861b0cd2e9a03"></a>
<a id="astructbt__hci__evt__le__remote__feat__complete_html"></a>
<a id="astructbt__hci__evt__le__remote__feat__complete_html_a61101c21e317aa07b08725a7ffbb4b81"></a>
<a id="astructbt__hci__evt__le__remote__feat__complete_html_a8a80bade7644f986fec41462843d8319"></a>
<a id="astructbt__hci__evt__le__remote__feat__complete_html_a9a0da26d9415169f02b6c9472120afe7"></a>
<a id="astructbt__hci__evt__le__req__peer__sca__complete_html"></a>
<a id="astructbt__hci__evt__le__req__peer__sca__complete_html_a814d17b8aae9dd68f57402c857ca1810"></a>
<a id="astructbt__hci__evt__le__req__peer__sca__complete_html_a88f93ead6ec67e1612b1a0e8402a30e7"></a>
<a id="astructbt__hci__evt__le__req__peer__sca__complete_html_ab6b648e7f4bff9e84b274e9e22a26166"></a>
<a id="astructbt__hci__evt__le__scan__req__received_html"></a>
<a id="astructbt__hci__evt__le__scan__req__received_html_a62c6d5e5b7079665c0aea8eb676a0433"></a>
<a id="astructbt__hci__evt__le__scan__req__received_html_a7dca5ad876dc97859a139d8bd4b207af"></a>
<a id="astructbt__hci__evt__le__subrate__change_html"></a>
<a id="astructbt__hci__evt__le__subrate__change_html_a2ad4a06feeb0d6d36461b4a4e53dfeb1"></a>
<a id="astructbt__hci__evt__le__subrate__change_html_a712b8b818115f1797787aab229040c8a"></a>
<a id="astructbt__hci__evt__le__subrate__change_html_a9387ffe45a856f7f443f5116a59a9ff2"></a>
<a id="astructbt__hci__evt__le__subrate__change_html_a95aaed5f8c93a1d6e8cab4c7ebfad8d7"></a>
<a id="astructbt__hci__evt__le__subrate__change_html_aa49286a63d565feaf3d9329cd024ee9f"></a>
<a id="astructbt__hci__evt__le__subrate__change_html_adc08125e663a99c7232d0755c4bd760b"></a>
<a id="astructbt__hci__evt__le__transmit__power__report_html"></a>
<a id="astructbt__hci__evt__le__transmit__power__report_html_a2dc33da8f36cceda362d0c87098b02d6"></a>
<a id="astructbt__hci__evt__le__transmit__power__report_html_a341cc0c5cc1ea969e2024b67056a5439"></a>
<a id="astructbt__hci__evt__le__transmit__power__report_html_a4feadb14800c1b51a9cc523c1d6a9063"></a>
<a id="astructbt__hci__evt__le__transmit__power__report_html_aa0df9c50a555fa40ed25a14f7b6a5e77"></a>
<a id="astructbt__hci__evt__le__transmit__power__report_html_ac42d60325235f517728ff44385361db2"></a>
<a id="astructbt__hci__evt__le__transmit__power__report_html_ad6130863713cf31a1cbe33de9fb5428f"></a>
<a id="astructbt__hci__evt__le__transmit__power__report_html_af1629e59dd651e1616b89f4958f47c92"></a>
<a id="astructbt__hci__evt__link__key__notify_html"></a>
<a id="astructbt__hci__evt__link__key__notify_html_a02647d66142c037b8bca2e748bc15319"></a>
<a id="astructbt__hci__evt__link__key__notify_html_a4a1b50d8874d01a6a5dc5c52524c9bed"></a>
<a id="astructbt__hci__evt__link__key__notify_html_a664580660a690af0d9ae3a62d79ad94b"></a>
<a id="astructbt__hci__evt__link__key__req_html"></a>
<a id="astructbt__hci__evt__link__key__req_html_aed882dfb6b632383543bd7e60536ccc6"></a>
<a id="astructbt__hci__evt__mode__change_html"></a>
<a id="astructbt__hci__evt__mode__change_html_a12092d35d2866f9c04da6e9e9889416e"></a>
<a id="astructbt__hci__evt__mode__change_html_a91a9d6e910fd1999003ae41dce8eaa69"></a>
<a id="astructbt__hci__evt__mode__change_html_abd35ca68cd0c371350ee49d95aa68454"></a>
<a id="astructbt__hci__evt__mode__change_html_af33d9335a8e9253b481c91dbd0716e40"></a>
<a id="astructbt__hci__evt__num__completed__packets_html"></a>
<a id="astructbt__hci__evt__num__completed__packets_html_a666ed2c19596a89ab0c77275cbe18d1e"></a>
<a id="astructbt__hci__evt__num__completed__packets_html_a94fb176924f7e844704be28851366052"></a>
<a id="astructbt__hci__evt__pin__code__req_html"></a>
<a id="astructbt__hci__evt__pin__code__req_html_a8649a30cd8c7ecf9ee006ddc2e625908"></a>
<a id="astructbt__hci__evt__remote__ext__features_html"></a>
<a id="astructbt__hci__evt__remote__ext__features_html_a0191b80b4f4d5360972faa6d5edf5055"></a>
<a id="astructbt__hci__evt__remote__ext__features_html_a084199f8e30669c2a1a631af26c0d69a"></a>
<a id="astructbt__hci__evt__remote__ext__features_html_a4f1d489aaa5626e485d34a9ae4cf9a34"></a>
<a id="astructbt__hci__evt__remote__ext__features_html_aeece2b8d46f4a3713d63df29058f2d9c"></a>
<a id="astructbt__hci__evt__remote__ext__features_html_afa577407f4ded5404394f42e7c73e10b"></a>
<a id="astructbt__hci__evt__remote__features_html"></a>
<a id="astructbt__hci__evt__remote__features_html_a2cedd8392c87914272ff250a56c80574"></a>
<a id="astructbt__hci__evt__remote__features_html_a70c97b9fbf7c363eab7b27f3a4e86e96"></a>
<a id="astructbt__hci__evt__remote__features_html_ada0249bdb7108c5d347fea1218c4f878"></a>
<a id="astructbt__hci__evt__remote__name__req__complete_html"></a>
<a id="astructbt__hci__evt__remote__name__req__complete_html_a380121873bf059b7c8a4abdf212f4235"></a>
<a id="astructbt__hci__evt__remote__name__req__complete_html_a3e54674692f7fc1670fa389e293714c7"></a>
<a id="astructbt__hci__evt__remote__name__req__complete_html_ab43d4a3c19d829b829cc7b40a67959f3"></a>
<a id="astructbt__hci__evt__remote__version__info_html"></a>
<a id="astructbt__hci__evt__remote__version__info_html_a02188119418a5a6dd8a4d0c37f5a060d"></a>
<a id="astructbt__hci__evt__remote__version__info_html_a1703a9ac9a5e1ba3ed396fe5799f9f51"></a>
<a id="astructbt__hci__evt__remote__version__info_html_a196f9489183d6e0116ff687df66c60c0"></a>
<a id="astructbt__hci__evt__remote__version__info_html_a8442b9f2bdc6cbce564c9bcec4169a20"></a>
<a id="astructbt__hci__evt__remote__version__info_html_aaa9c3875143700b6ed013715cb3c7107"></a>
<a id="astructbt__hci__evt__role__change_html"></a>
<a id="astructbt__hci__evt__role__change_html_a18dd22435ae40fcf1c4fd2b90b402c60"></a>
<a id="astructbt__hci__evt__role__change_html_a2e5736d63e30326c33bec8ebdf986c62"></a>
<a id="astructbt__hci__evt__role__change_html_aafe1a9e43a9a42d4030846180e55b8ef"></a>
<a id="astructbt__hci__evt__ssp__complete_html"></a>
<a id="astructbt__hci__evt__ssp__complete_html_a33d3d47c1cef71cfb787a1195d9b4ec2"></a>
<a id="astructbt__hci__evt__ssp__complete_html_a5030cf334f97cdd982001b3278ed9db1"></a>
<a id="astructbt__hci__evt__sync__conn__complete_html"></a>
<a id="astructbt__hci__evt__sync__conn__complete_html_a4b93873ad6f5388657511d87fc0a8c85"></a>
<a id="astructbt__hci__evt__sync__conn__complete_html_a5f6068569bf649bcd1d13928f56f9703"></a>
<a id="astructbt__hci__evt__sync__conn__complete_html_a68a31880c8aab9245be043c1719464d3"></a>
<a id="astructbt__hci__evt__sync__conn__complete_html_a6a455f56da4666cb602e6c05157e166d"></a>
<a id="astructbt__hci__evt__sync__conn__complete_html_a78f5560783400f1d1a63b2c9d69fa7ed"></a>
<a id="astructbt__hci__evt__sync__conn__complete_html_aa48aa29ff73e93e8d961013f066c1b5e"></a>
<a id="astructbt__hci__evt__sync__conn__complete_html_aacf9919945e9b755913da145f0fe78ae"></a>
<a id="astructbt__hci__evt__sync__conn__complete_html_ab4d4106d5120f10e8300834db12740d8"></a>
<a id="astructbt__hci__evt__sync__conn__complete_html_accd17a95f35ab1988122df7584830f60"></a>
<a id="astructbt__hci__evt__user__confirm__req_html"></a>
<a id="astructbt__hci__evt__user__confirm__req_html_aaeec83c50764c322af7cd64259e54a97"></a>
<a id="astructbt__hci__evt__user__confirm__req_html_ac333729f5a7d9241ac26aeb7d3f77935"></a>
<a id="astructbt__hci__evt__user__passkey__notify_html"></a>
<a id="astructbt__hci__evt__user__passkey__notify_html_a7f6a367e50d41cb7d8897db05db826be"></a>
<a id="astructbt__hci__evt__user__passkey__notify_html_af020e1cd131473fe06a193529a0499ac"></a>
<a id="astructbt__hci__evt__user__passkey__req_html"></a>
<a id="astructbt__hci__evt__user__passkey__req_html_a7f1005423296906e0374050bc30781ce"></a>
<a id="astructbt__hci__ext__adv__set_html"></a>
<a id="astructbt__hci__ext__adv__set_html_a4467ac9a564ea24bb701de46cda2579a"></a>
<a id="astructbt__hci__ext__adv__set_html_a9d0fd3f6659db172ff4efd74c2c2d216"></a>
<a id="astructbt__hci__ext__adv__set_html_acc2afc91fe5c0dfcb4c95eaade4a047a"></a>
<a id="astructbt__hci__ext__conn__phy_html"></a>
<a id="astructbt__hci__ext__conn__phy_html_a3c3ccb93014758b3215718d2672ce7f3"></a>
<a id="astructbt__hci__ext__conn__phy_html_a4f78503fe42ee81fea740ba1643a732e"></a>
<a id="astructbt__hci__ext__conn__phy_html_a7bcf66a3372d92c809d8427796915b88"></a>
<a id="astructbt__hci__ext__conn__phy_html_a7dd57b7ef0b13b15da47e92076f87d79"></a>
<a id="astructbt__hci__ext__conn__phy_html_a7fc06c1a458aedb6b29381450a5a4df0"></a>
<a id="astructbt__hci__ext__conn__phy_html_aaec54c0743dfc08923b5ccd8fc1a4015"></a>
<a id="astructbt__hci__ext__conn__phy_html_ae0e950c8004bd595631f95a289a5c871"></a>
<a id="astructbt__hci__ext__conn__phy_html_af48212961ce21f5222e57f70ffeb811b"></a>
<a id="astructbt__hci__ext__scan__phy_html"></a>
<a id="astructbt__hci__ext__scan__phy_html_a2f087d18bde86d0ac81a14a09ae5b9b0"></a>
<a id="astructbt__hci__ext__scan__phy_html_a4cfebc7b2709973953bed9a09a793b7e"></a>
<a id="astructbt__hci__ext__scan__phy_html_a9c0196f0d5f0064796c15a5df2ad4c07"></a>
<a id="astructbt__hci__handle__count_html"></a>
<a id="astructbt__hci__handle__count_html_a71577f376985909744fa14f246e69e1d"></a>
<a id="astructbt__hci__handle__count_html_acacc000905835724b7fe882a8ad85f82"></a>
<a id="astructbt__hci__iac__lap_html"></a>
<a id="astructbt__hci__iac__lap_html_ac729dc24f337c32b1ffd0e212ccf49ff"></a>
<a id="astructbt__hci__iso__hdr_html"></a>
<a id="astructbt__hci__iso__hdr_html_ab33ae914a9eba85b35c78e45e0f5255f"></a>
<a id="astructbt__hci__iso__hdr_html_af5113383fbcd0e70828f986720c38572"></a>
<a id="astructbt__hci__iso__sdu__hdr_html"></a>
<a id="astructbt__hci__iso__sdu__hdr_html_a626764862a3757a3119b6de799221ad1"></a>
<a id="astructbt__hci__iso__sdu__hdr_html_a683d493de5d00e3b4c5169f6de498c13"></a>
<a id="astructbt__hci__iso__sdu__ts__hdr_html"></a>
<a id="astructbt__hci__iso__sdu__ts__hdr_html_a3f81175b95f8eaeeeee71ee4bf401864"></a>
<a id="astructbt__hci__iso__sdu__ts__hdr_html_a657e03c5ef597f04cc21725f0bc227d4"></a>
<a id="astructbt__hci__le__cs__step__data__mode__0__initiator_html"></a>
<a id="astructbt__hci__le__cs__step__data__mode__0__initiator_html_a11edf6e1c1da5d24aa1136521a249f52"></a>
<a id="astructbt__hci__le__cs__step__data__mode__0__initiator_html_a339252cacafd05e85c0fb19776343e17"></a>
<a id="astructbt__hci__le__cs__step__data__mode__0__initiator_html_a48fc1fd87869d4ca2b70c42d5c4e1d75"></a>
<a id="astructbt__hci__le__cs__step__data__mode__0__initiator_html_a811eb38a04e63b12be9e25291126ccc1"></a>
<a id="astructbt__hci__le__cs__step__data__mode__0__initiator_html_ad9a2193cbe5381d30494dbf6f8d84482"></a>
<a id="astructbt__hci__le__cs__step__data__mode__0__reflector_html"></a>
<a id="astructbt__hci__le__cs__step__data__mode__0__reflector_html_a16fb71660c4f4afb1c36765fdbd2a96a"></a>
<a id="astructbt__hci__le__cs__step__data__mode__0__reflector_html_a9c34ecf0b79449754da1d1ba925b1ff2"></a>
<a id="astructbt__hci__le__cs__step__data__mode__0__reflector_html_aa058afab8cba3f5ce572b8e7d29ef34d"></a>
<a id="astructbt__hci__le__cs__step__data__mode__0__reflector_html_ad045baeaf6fbb75de002ffedc4b1a831"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1__ss__rtt_html"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1__ss__rtt_html_a3f8ba85b776f732ebc1086a4317849a1"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1__ss__rtt_html_a511b281fb1c16fd7d0eaf731906a4292"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1__ss__rtt_html_a515fde1d568a19ccf6ebefe9052866a4"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1__ss__rtt_html_a5ec9c30063c09285804973008533e5cb"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1__ss__rtt_html_a77bbcd9451360ad97813f9357e44766e"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1__ss__rtt_html_a9f969aa6fc134a9e618d07f177d2b7fd"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1__ss__rtt_html_abf20351ab0eaf3a7139a464f1d1a72b0"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1__ss__rtt_html_ace3843bc24616950f04150b2f86abad4"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1__ss__rtt_html_ad8f9ca9dda852b435848b988ad872797"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1_html"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1_html_a0cb4198466318a7a15cbbb172c582eeb"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1_html_a1365e601f422b98747f9909d3be56b60"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1_html_a1b9df39c01ab91ab225c809db5066f70"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1_html_a4025cf2b229ada27e258d3d519a7b1dd"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1_html_a8383926e95cd9d222b91704b2ca6883e"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1_html_ab3425181b2a625fcfbbfd14477d717d1"></a>
<a id="astructbt__hci__le__cs__step__data__mode__1_html_afc8221a5cab14d3842590e6cac52da4d"></a>
<a id="astructbt__hci__le__cs__step__data__mode__2_html"></a>
<a id="astructbt__hci__le__cs__step__data__mode__2_html_a9feb2b07f8862aa24772a733f451f7a8"></a>
<a id="astructbt__hci__le__cs__step__data__mode__2_html_aef5699cb9bfc522a12be9a284392fd0e"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html_a657ec3570e3ad6b2ddab87bada231587"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html_a9ce412ad8b18a9315b858cf1fe2a466a"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html_a9d2428083c401d931520addde0af54fd"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html_aada8b3ff1bb0d0b9eccb846da173b3f4"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html_ac4067e27caa12cf9f8c6525bf6a72973"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html_ada4d52f54f1efa804a812c65edd8f125"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html_adc4fe32bc6b7515e5bf1055f19f1a2bd"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html_ae2181a568ed6da32d3f60ba6d271c64f"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html_aea13fc3e16092dcede9fb46ea719f21c"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html_af5d8a8559400b45066bdac86fbdac411"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3__ss__rtt_html_afdebbafc06475dde12aaed73d2180f96"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3_html"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3_html_a183f3ee64a4482c9d3e0f041151fdcf9"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3_html_a42b8bdf1fd492be1daded674e3d733d6"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3_html_a60750ac38bf019a0c7a8656ca59fc402"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3_html_a609102fc9d42fe73c09907f54526bd40"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3_html_a9ae78aa83a22f0618491871d55f2f0b9"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3_html_a9b7373e7d3faa0cb5553d4f897c94ebc"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3_html_aa0f1918115a6e550d6fab17529bbb4f2"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3_html_ad20e9c1deba67aa5759881b52d13311d"></a>
<a id="astructbt__hci__le__cs__step__data__mode__3_html_ad4c30784cc2586b5b8dcfa22e7a1f8fb"></a>
<a id="astructbt__hci__le__cs__step__data__tone__info_html"></a>
<a id="astructbt__hci__le__cs__step__data__tone__info_html_a4d31c0759c17789cb4b9bdc90a8870ca"></a>
<a id="astructbt__hci__le__cs__step__data__tone__info_html_a5f2e5e95b97d2be49a8ff1d9376892e8"></a>
<a id="astructbt__hci__le__cs__step__data__tone__info_html_aeb76aeb54cb4e5613496431ec6d0093a"></a>
<a id="astructbt__hci__le__iq__sample_html"></a>
<a id="astructbt__hci__le__iq__sample_html_a775b6e0ab1842594bc00998faec613f3"></a>
<a id="astructbt__hci__le__iq__sample_html_aacf452456eecd4ad4dab083593b11104"></a>
<a id="astructbt__hci__le__read__min__supported__conn__interval__group_html"></a>
<a id="astructbt__hci__le__read__min__supported__conn__interval__group_html_a43ef933e3f445ac1366a3707b52ceffd"></a>
<a id="astructbt__hci__le__read__min__supported__conn__interval__group_html_a5cfd002c4dc82faa692ed1afa50692b5"></a>
<a id="astructbt__hci__le__read__min__supported__conn__interval__group_html_abcd7d0eadf485b82993d421072cc8ba4"></a>
<a id="astructbt__hci__op__inquiry_html"></a>
<a id="astructbt__hci__op__inquiry_html_abdd03feccecbdbbb5d2c7c7f3213b62f"></a>
<a id="astructbt__hci__op__inquiry_html_ac8ed23243dbd9a7c46fedd8abe9666f5"></a>
<a id="astructbt__hci__op__inquiry_html_ae77fa706c9875b5568a4af26a7724d08"></a>
<a id="astructbt__hci__op__le__connection__rate__request_html"></a>
<a id="astructbt__hci__op__le__connection__rate__request_html_a35033b89faecdaa053e8bcff590ad5e7"></a>
<a id="astructbt__hci__op__le__connection__rate__request_html_a523cde9caf261ca3f3766b4d9648c7eb"></a>
<a id="astructbt__hci__op__le__connection__rate__request_html_a5ac425326df618f446bc891ea0b329ec"></a>
<a id="astructbt__hci__op__le__connection__rate__request_html_a7178c6af0cdbf1376bd3e52a175be03e"></a>
<a id="astructbt__hci__op__le__connection__rate__request_html_a87ad44b9857515b42aff8200cfb42b37"></a>
<a id="astructbt__hci__op__le__connection__rate__request_html_aa1123f8a8eafa16785e440b8b8a7e885"></a>
<a id="astructbt__hci__op__le__connection__rate__request_html_ab06f3b29db55a6f56ab8cc1f2e7b95df"></a>
<a id="astructbt__hci__op__le__connection__rate__request_html_ae290b39a2ba9c37595de67b877a61f3b"></a>
<a id="astructbt__hci__op__le__connection__rate__request_html_aee4d2070f12c33c5c6f6d93435f1f4b5"></a>
<a id="astructbt__hci__op__le__connection__rate__request_html_af63ff615adc36c422d6be8db20e45c85"></a>
<a id="astructbt__hci__op__le__cs__test_html"></a>
<a id="astructbt__hci__op__le__cs__test_html_a0675dfbb050838d98f21cfa28af8615b"></a>
<a id="astructbt__hci__op__le__cs__test_html_a06ac1b5aa8951fe4769a1360af44df82"></a>
<a id="astructbt__hci__op__le__cs__test_html_a090c5d03cf829011196d644cd9f7c7db"></a>
<a id="astructbt__hci__op__le__cs__test_html_a09c40ecd0d4e325e0c0504a9d8cd977b"></a>
<a id="astructbt__hci__op__le__cs__test_html_a15a68fe7c98b2e242afd6eb67dd9b40a"></a>
<a id="astructbt__hci__op__le__cs__test_html_a1c105f7a4d48754322fee6992db8c175"></a>
<a id="astructbt__hci__op__le__cs__test_html_a373372a93d94e70d674c1c7b4c126734"></a>
<a id="astructbt__hci__op__le__cs__test_html_a3c949d9a7eb4f56427f6e9f8be7cb77b"></a>
<a id="astructbt__hci__op__le__cs__test_html_a551c06e651180867dd1d23b3fdf4c031"></a>
<a id="astructbt__hci__op__le__cs__test_html_a60cc9a7c46f8cd0933dc2f5a68cca627"></a>
<a id="astructbt__hci__op__le__cs__test_html_a7538e91b5ced2702965a21f8e754ebcc"></a>
<a id="astructbt__hci__op__le__cs__test_html_a8ad67a5a0138f32cc5295074011a3808"></a>
<a id="astructbt__hci__op__le__cs__test_html_a8c23c2e6e8c38bf33fcd6d1e343f5982"></a>
<a id="astructbt__hci__op__le__cs__test_html_a981da50e0594b8bc05f811e5170b10f5"></a>
<a id="astructbt__hci__op__le__cs__test_html_aa3d510663e5dcc44b5acd9d1c41746d5"></a>
<a id="astructbt__hci__op__le__cs__test_html_aaf480890608b5cfc9151dac844e9a337"></a>
<a id="astructbt__hci__op__le__cs__test_html_acaa428a37e68ff56c311397e53f46526"></a>
<a id="astructbt__hci__op__le__cs__test_html_acc2d0768b69e5f5b593e5aff71b17f20"></a>
<a id="astructbt__hci__op__le__cs__test_html_ad52cd2862d2544448a5e175c58541f89"></a>
<a id="astructbt__hci__op__le__cs__test_html_adf2f24dc6988f1f0e0457a6cf3141521"></a>
<a id="astructbt__hci__op__le__cs__test_html_ae0234031d94e93653dd45e6e657c199f"></a>
<a id="astructbt__hci__op__le__cs__test_html_aee8c125df0f7136a0ecdb9f04903aaef"></a>
<a id="astructbt__hci__op__le__cs__test_html_aef335dd7738634cb8f81c18e0350141e"></a>
<a id="astructbt__hci__op__le__cs__test_html_af42701651bca5fe0353ae1de9c453f47"></a>
<a id="astructbt__hci__op__le__cs__test_html_af4cdfd8c8cab500277c06a82ac088577"></a>
<a id="astructbt__hci__op__le__cs__test_html_afa0310f818002d7c1ac048f0db8c7f1c"></a>
<a id="astructbt__hci__op__le__read__min__supported__conn__interval_html"></a>
<a id="astructbt__hci__op__le__read__min__supported__conn__interval_html_a0c71077c8e7db5b1bdba1372bc7ac5ac"></a>
<a id="astructbt__hci__op__le__read__min__supported__conn__interval_html_a8bd4666fa42fb9a527fca5309e3bf0d6"></a>
<a id="astructbt__hci__op__le__read__min__supported__conn__interval_html_a92313039960815652380c301d4a5ce8d"></a>
<a id="astructbt__hci__op__le__read__min__supported__conn__interval_html_aa049350b4f8fafe3bf74780924e1eeff"></a>
<a id="astructbt__hci__op__le__set__default__rate__parameters_html"></a>
<a id="astructbt__hci__op__le__set__default__rate__parameters_html_a115579391f9fe7ec2536a21c3a42b3ab"></a>
<a id="astructbt__hci__op__le__set__default__rate__parameters_html_a4efb8757f63f15e37070b3046490edcf"></a>
<a id="astructbt__hci__op__le__set__default__rate__parameters_html_a630ae05aff2e511b37a522fadd831dd0"></a>
<a id="astructbt__hci__op__le__set__default__rate__parameters_html_aaa9dd1a946c7440e0a985276137ae096"></a>
<a id="astructbt__hci__op__le__set__default__rate__parameters_html_ad267cc8be963c1d16088a7c14bef19bf"></a>
<a id="astructbt__hci__op__le__set__default__rate__parameters_html_ad8051508f324d40bd95e9dbee97b1b2a"></a>
<a id="astructbt__hci__op__le__set__default__rate__parameters_html_adb818d82c1c38f573a31f22b0ebc817b"></a>
<a id="astructbt__hci__op__le__set__default__rate__parameters_html_af0fbd935b200c98b5ef6477d127ccdfe"></a>
<a id="astructbt__hci__op__le__set__default__rate__parameters_html_af9afc0e463f068c113c0042f58dcc63d"></a>
<a id="astructbt__hci__rp__configure__data__path_html"></a>
<a id="astructbt__hci__rp__configure__data__path_html_a10cfe9bf5a7be202706957d7b8e1f371"></a>
<a id="astructbt__hci__rp__connect__cancel_html"></a>
<a id="astructbt__hci__rp__connect__cancel_html_a05d0c9e4163bc62a57dba8618294eb65"></a>
<a id="astructbt__hci__rp__connect__cancel_html_a0ccfcbd294aa067879ab8d7a41bc41c9"></a>
<a id="astructbt__hci__rp__le__big__terminate__sync_html"></a>
<a id="astructbt__hci__rp__le__big__terminate__sync_html_a741ab80e08e7ecfc5a0158ec0cf14654"></a>
<a id="astructbt__hci__rp__le__big__terminate__sync_html_ad4d1d4238402ef829a1ff9ed3b1dc050"></a>
<a id="astructbt__hci__rp__le__conn__cte__req__enable_html"></a>
<a id="astructbt__hci__rp__le__conn__cte__req__enable_html_a1e76e7a6da194a433c1fa6ac2bc36b80"></a>
<a id="astructbt__hci__rp__le__conn__cte__req__enable_html_af00adb07a144156a37fb5fc47ca61ccb"></a>
<a id="astructbt__hci__rp__le__conn__cte__rsp__enable_html"></a>
<a id="astructbt__hci__rp__le__conn__cte__rsp__enable_html_a8a21bc015408cc77c5d229cd77289dcc"></a>
<a id="astructbt__hci__rp__le__conn__cte__rsp__enable_html_ab16f226d871d7d55c3f900614d59d8a1"></a>
<a id="astructbt__hci__rp__le__conn__param__req__neg__reply_html"></a>
<a id="astructbt__hci__rp__le__conn__param__req__neg__reply_html_a3804e64f9e8693e3e5899067212f6873"></a>
<a id="astructbt__hci__rp__le__conn__param__req__neg__reply_html_ac88f44127c0a1b9b191a27cc003c1052"></a>
<a id="astructbt__hci__rp__le__conn__param__req__reply_html"></a>
<a id="astructbt__hci__rp__le__conn__param__req__reply_html_a2f0a9f5b087d1f12c100ef4521e015ff"></a>
<a id="astructbt__hci__rp__le__conn__param__req__reply_html_a3e598cd87d5298a1cc62ac79a4f34a6e"></a>
<a id="astructbt__hci__rp__le__default__past__param_html"></a>
<a id="astructbt__hci__rp__le__default__past__param_html_a292e2d655c77e8cda0d01fc07b43b8c4"></a>
<a id="astructbt__hci__rp__le__encrypt_html"></a>
<a id="astructbt__hci__rp__le__encrypt_html_ac20cd9f4ceffea6999114f65437aefdc"></a>
<a id="astructbt__hci__rp__le__encrypt_html_aee480917cc6af7dea77717a9cb5840bb"></a>
<a id="astructbt__hci__rp__le__iso__receive__test_html"></a>
<a id="astructbt__hci__rp__le__iso__receive__test_html_a028a77001a5e24dda8fac38718103ef0"></a>
<a id="astructbt__hci__rp__le__iso__receive__test_html_a863a8a44af979a8b1b9d084563b2fe9a"></a>
<a id="astructbt__hci__rp__le__iso__test__end_html"></a>
<a id="astructbt__hci__rp__le__iso__test__end_html_a10b3ee6110bc0bb9279b22f9963715c1"></a>
<a id="astructbt__hci__rp__le__iso__test__end_html_a16feaeb739f6ed34d9ce3fc86248955c"></a>
<a id="astructbt__hci__rp__le__iso__test__end_html_a4a4625d7b78abf3c039842df2a72ce8b"></a>
<a id="astructbt__hci__rp__le__iso__test__end_html_a55490978e7416ecc308bf510f05afd4f"></a>
<a id="astructbt__hci__rp__le__iso__test__end_html_ab4352fd5d9b822fb7fb75f8f5e2db6a9"></a>
<a id="astructbt__hci__rp__le__iso__transmit__test_html"></a>
<a id="astructbt__hci__rp__le__iso__transmit__test_html_a01ae01d11c606f559107b8c54781d843"></a>
<a id="astructbt__hci__rp__le__iso__transmit__test_html_a0863c47551b328984e00c392f9f11660"></a>
<a id="astructbt__hci__rp__le__ltk__req__neg__reply_html"></a>
<a id="astructbt__hci__rp__le__ltk__req__neg__reply_html_a92306e47450b239233a3f39c645eaa4e"></a>
<a id="astructbt__hci__rp__le__ltk__req__neg__reply_html_ad0f4f9300d9a8b737b41211972151017"></a>
<a id="astructbt__hci__rp__le__ltk__req__reply_html"></a>
<a id="astructbt__hci__rp__le__ltk__req__reply_html_a2dfe012e641e5d8bd6c0f2e15e5a54c2"></a>
<a id="astructbt__hci__rp__le__ltk__req__reply_html_a831950bab8994f36c96c543310400752"></a>
<a id="astructbt__hci__rp__le__past__param_html"></a>
<a id="astructbt__hci__rp__le__past__param_html_a9630362b3d885b13869a4c0fe9e97b12"></a>
<a id="astructbt__hci__rp__le__past__param_html_ae6b8a5d7e790516de2f91e41fd893111"></a>
<a id="astructbt__hci__rp__le__per__adv__set__info__transfer_html"></a>
<a id="astructbt__hci__rp__le__per__adv__set__info__transfer_html_a696e5cab4d7507ea79b0e116c4bb92e2"></a>
<a id="astructbt__hci__rp__le__per__adv__set__info__transfer_html_ab1592bfadd45315ff47e86b7c50374ad"></a>
<a id="astructbt__hci__rp__le__per__adv__sync__transfer_html"></a>
<a id="astructbt__hci__rp__le__per__adv__sync__transfer_html_ab8b4357fd92e01a5f61d3127b04c0318"></a>
<a id="astructbt__hci__rp__le__per__adv__sync__transfer_html_adb536c4694d2e7c5b91e9f68986e97e1"></a>
<a id="astructbt__hci__rp__le__rand_html"></a>
<a id="astructbt__hci__rp__le__rand_html_a3f706af9d2baf9e2b199242a28cec9e5"></a>
<a id="astructbt__hci__rp__le__rand_html_a73320168836caa3caf724282402e80de"></a>
<a id="astructbt__hci__rp__le__read__all__local__supported__features_html"></a>
<a id="astructbt__hci__rp__le__read__all__local__supported__features_html_a3e200ffc8a5ecafc5e7173f1a48fe6b1"></a>
<a id="astructbt__hci__rp__le__read__all__local__supported__features_html_a8cecb341ec3dfb335940af0a6e4751c6"></a>
<a id="astructbt__hci__rp__le__read__all__local__supported__features_html_ac4aeb5159bb91c8faf9d12461b005e89"></a>
<a id="astructbt__hci__rp__le__read__ant__info_html"></a>
<a id="astructbt__hci__rp__le__read__ant__info_html_a1f79b45751d39ebb9349df93d0ff2e13"></a>
<a id="astructbt__hci__rp__le__read__ant__info_html_a2c78d3db239c9e00729d91834eb60f21"></a>
<a id="astructbt__hci__rp__le__read__ant__info_html_a625cc8fa8553eafbbb31cbc0b3f303c7"></a>
<a id="astructbt__hci__rp__le__read__ant__info_html_ae1388d3eee3085af7f2b0b57b2aa7b1e"></a>
<a id="astructbt__hci__rp__le__read__ant__info_html_ae75fe0b9f5fe8c88a8e8482eef299348"></a>
<a id="astructbt__hci__rp__le__read__buffer__size__v2_html"></a>
<a id="astructbt__hci__rp__le__read__buffer__size__v2_html_a1c7938defb076d973b8339c17cc930df"></a>
<a id="astructbt__hci__rp__le__read__buffer__size__v2_html_a3b9cc0577d0f5f3c2b934a28915f2177"></a>
<a id="astructbt__hci__rp__le__read__buffer__size__v2_html_a9758d477c502575a1c176eb6a63e1a1a"></a>
<a id="astructbt__hci__rp__le__read__buffer__size__v2_html_ac3379adf42f9bbee8ae72fb4a7606fd1"></a>
<a id="astructbt__hci__rp__le__read__buffer__size__v2_html_ac391149d3d7442e074aad4b98659bd02"></a>
<a id="astructbt__hci__rp__le__read__buffer__size_html"></a>
<a id="astructbt__hci__rp__le__read__buffer__size_html_a3e393d6c51d8c3f8a5d88413198e3f28"></a>
<a id="astructbt__hci__rp__le__read__buffer__size_html_a8bc64cd8743984cd5a8dedfc86aaee56"></a>
<a id="astructbt__hci__rp__le__read__buffer__size_html_a90a1206f1dbbefd298e5323ac07691f1"></a>
<a id="astructbt__hci__rp__le__read__chan__map_html"></a>
<a id="astructbt__hci__rp__le__read__chan__map_html_a2899c53f17ba2293b95477ba25fd1b3d"></a>
<a id="astructbt__hci__rp__le__read__chan__map_html_a73a51f243bf4881f9024ba67cf2426ad"></a>
<a id="astructbt__hci__rp__le__read__chan__map_html_a8fcec46574f5601bf0837aae8f745b38"></a>
<a id="astructbt__hci__rp__le__read__chan__tx__power_html"></a>
<a id="astructbt__hci__rp__le__read__chan__tx__power_html_a09a3805bccdabef399d21b29f84e3a4f"></a>
<a id="astructbt__hci__rp__le__read__chan__tx__power_html_a3b6b79d1d28c3e4bf565ae364089f365"></a>
<a id="astructbt__hci__rp__le__read__default__data__len_html"></a>
<a id="astructbt__hci__rp__le__read__default__data__len_html_a1ec4ba1c0286132e87fcffeb988a37f9"></a>
<a id="astructbt__hci__rp__le__read__default__data__len_html_a62d735826ad3ca5d4bea7d0fb87dea7e"></a>
<a id="astructbt__hci__rp__le__read__default__data__len_html_ae193eab40c2afa55b78a1906e6a26f26"></a>
<a id="astructbt__hci__rp__le__read__fal__size_html"></a>
<a id="astructbt__hci__rp__le__read__fal__size_html_aaceae885848bbdbf71241e7aa3881db5"></a>
<a id="astructbt__hci__rp__le__read__fal__size_html_ac5fcb88478c1faadf7f7ca6a9f838dde"></a>
<a id="astructbt__hci__rp__le__read__iso__link__quality_html"></a>
<a id="astructbt__hci__rp__le__read__iso__link__quality_html_a0d4468f6871716414ef4a601791bac58"></a>
<a id="astructbt__hci__rp__le__read__iso__link__quality_html_a12c0c3f9fe6c3c94742367f30bdcc630"></a>
<a id="astructbt__hci__rp__le__read__iso__link__quality_html_a353070a64655a39f5410fe76e9168e97"></a>
<a id="astructbt__hci__rp__le__read__iso__link__quality_html_a68c23277e65dc5694f5a27ee2cd364ff"></a>
<a id="astructbt__hci__rp__le__read__iso__link__quality_html_a6a16d0aa7ed220bac1ade12eb0f7703e"></a>
<a id="astructbt__hci__rp__le__read__iso__link__quality_html_a7be135da9607045f60b616b84a68f5db"></a>
<a id="astructbt__hci__rp__le__read__iso__link__quality_html_a9f2e8c26081ede43c7712b851d79f2cd"></a>
<a id="astructbt__hci__rp__le__read__iso__link__quality_html_aae42e05dff474062726b92c6d45eae4f"></a>
<a id="astructbt__hci__rp__le__read__iso__link__quality_html_aef80c600f8916c098e08c43ca718d630"></a>
<a id="astructbt__hci__rp__le__read__iso__tx__sync_html"></a>
<a id="astructbt__hci__rp__le__read__iso__tx__sync_html_a188ef5dba77c754c46094135cc52641c"></a>
<a id="astructbt__hci__rp__le__read__iso__tx__sync_html_a29770c3172d5e45409392aa8ffc835ef"></a>
<a id="astructbt__hci__rp__le__read__iso__tx__sync_html_a35520a3e50afc03ed969b6c5ca9e15d9"></a>
<a id="astructbt__hci__rp__le__read__iso__tx__sync_html_a8c0003043d3896b1ff93dc33dccc76b4"></a>
<a id="astructbt__hci__rp__le__read__iso__tx__sync_html_af2a02f68aa0a757757c490e707954952"></a>
<a id="astructbt__hci__rp__le__read__local__features_html"></a>
<a id="astructbt__hci__rp__le__read__local__features_html_ac1000822beba8a7be0dda684c0a86b6b"></a>
<a id="astructbt__hci__rp__le__read__local__features_html_ada42e525338cd5526ff211c359c93b3b"></a>
<a id="astructbt__hci__rp__le__read__local__rpa_html"></a>
<a id="astructbt__hci__rp__le__read__local__rpa_html_a55b1ac66c986c0a7879b144163064be2"></a>
<a id="astructbt__hci__rp__le__read__local__rpa_html_a5b27c5b02cb290452be62c22772fbc53"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a145d8fe34f80df9367105d1cfa7b59c1"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a1d2e82062c0c41dce9e7428e4982223a"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a1f97298da17187ea1ed96ec923f54523"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a28b801d5310e4fd7e8285ba6361191df"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a29667f70ea84458e304fe731d443e25a"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a2c51d311adcacada33b9dec7b4395865"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a2fc5417dbbd91b4099fb4a27f01c18fd"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a3307caaaf76bfc5cb1c88937ce788efd"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a36f4762d9053476e84088fe8807024a3"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a4fbd5c95fd7f2f9131cd16ff04e64adf"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a61458332899b95c752b6343eda90013e"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a6a88f321faeea9e61bd38c696468d90f"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a7131d361abdc12c29a886e338075ae8a"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a7cc90e1e81657d0b755df281ba6806fc"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a7d3faf86b443db272303d3b4ad45df2d"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a7e061a636d3d0432ca9eb65e69a44710"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a8704313f30e256e87460961f03e0719a"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_a998504553ee046759214d0d220d8a3d3"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_ac000a669ee53e1ca4ad99fd350fe72e6"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_acb720ede01b7041c9d5b6d6ade065048"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_ae3f61c13562d8dec1812fc3c91c23539"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_af21e203e96302114a411d9995cd63fa6"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities__v2_html_afc6a9b21d8926b589cf25941e75ecb31"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a0958a5426e0057e2b8ccb80c222d0248"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a0e0bd5b1c624c7143b0229b5d3eeec6e"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a115ffe697da3e09ece4091493fa8f2da"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a1806f2f5ec2738b026453bbdb8b38ce9"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a24ffa02b6a8bfbff8b7d32f5ee46bea5"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a3a16c62ea321620608d706a80d90575e"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a3eb4830443e7912bf8ca97f603b91545"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a5f59d0b65cc4e7e44e487fa5535b76a9"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a7975eb0ce27f0326d1d909bffef57840"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a81bd809a734b6cdde2d55e0b23e41237"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a88a4277c5dea41b8171c33c85ed760bf"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_a8e7cc92cc4099774e8d0b385fc5f3d79"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_aaf09d10c19980729ef04654114919211"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_aaf578336893980f2ec1b2343b81860e5"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_ab026e5abfdead47eca1c5d8d316bc62c"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_ababf476100298c2ba7d79bdadd7a9d1b"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_ad07b464737c59b33de4c89948d4c5686"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_ad667ba51ffdbaf7754dea6f519615cb7"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_ad90ce3e635b8bccd29eefe73303f6e42"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_ae0767bb41b7b57e955ddbede2f83c166"></a>
<a id="astructbt__hci__rp__le__read__local__supported__capabilities_html_af3d1e7588f2429bb400fac81733748c3"></a>
<a id="astructbt__hci__rp__le__read__max__adv__data__len_html"></a>
<a id="astructbt__hci__rp__le__read__max__adv__data__len_html_a978911dc5028d1f36820447de8e9e5f7"></a>
<a id="astructbt__hci__rp__le__read__max__adv__data__len_html_aa4084a89de4929c3e8e2630d0aad7f82"></a>
<a id="astructbt__hci__rp__le__read__max__data__len_html"></a>
<a id="astructbt__hci__rp__le__read__max__data__len_html_a2c0b159c6248cb9df458d587f82a4152"></a>
<a id="astructbt__hci__rp__le__read__max__data__len_html_a654b34b1ee038bf442550a340a26070c"></a>
<a id="astructbt__hci__rp__le__read__max__data__len_html_a6adc84bf3cc86f234e61982d871899b6"></a>
<a id="astructbt__hci__rp__le__read__max__data__len_html_a9273dac6614f1e120f0539b746bfd6cc"></a>
<a id="astructbt__hci__rp__le__read__max__data__len_html_a963ef9c097906c8db46c35459eb4ecab"></a>
<a id="astructbt__hci__rp__le__read__num__adv__sets_html"></a>
<a id="astructbt__hci__rp__le__read__num__adv__sets_html_a590934059fb851a14b2eec66f32a5334"></a>
<a id="astructbt__hci__rp__le__read__num__adv__sets_html_a7dd26bda7a8ab75fed2af19bb5af34fc"></a>
<a id="astructbt__hci__rp__le__read__peer__rpa_html"></a>
<a id="astructbt__hci__rp__le__read__peer__rpa_html_a4eeee179819865ba5d5171d9bd33e5e9"></a>
<a id="astructbt__hci__rp__le__read__peer__rpa_html_a9c8c799e8c9fbb9f64865e55cdb1f9ef"></a>
<a id="astructbt__hci__rp__le__read__per__adv__list__size_html"></a>
<a id="astructbt__hci__rp__le__read__per__adv__list__size_html_a70aa5b466bdbbd309fc59570625c35e5"></a>
<a id="astructbt__hci__rp__le__read__per__adv__list__size_html_ab6c4ed1037327669aef623f3a1e9d601"></a>
<a id="astructbt__hci__rp__le__read__phy_html"></a>
<a id="astructbt__hci__rp__le__read__phy_html_a5a060e0c0d1e5f33222ab10a5d3977e8"></a>
<a id="astructbt__hci__rp__le__read__phy_html_a644c0065d97e5de006dc28f7bca62268"></a>
<a id="astructbt__hci__rp__le__read__phy_html_a65d412e37eb2cd839fae262f4f9d5b28"></a>
<a id="astructbt__hci__rp__le__read__phy_html_ae708b4f8ad2632d73bedea640f138d9f"></a>
<a id="astructbt__hci__rp__le__read__rf__path__comp_html"></a>
<a id="astructbt__hci__rp__le__read__rf__path__comp_html_a0f46a99c74006dc0a4dfd1a49c72e077"></a>
<a id="astructbt__hci__rp__le__read__rf__path__comp_html_a827fa954277823efdc5838c317a1460a"></a>
<a id="astructbt__hci__rp__le__read__rf__path__comp_html_a84a04bcc64ea6d50fe41e9b416a5ada1"></a>
<a id="astructbt__hci__rp__le__read__rl__size_html"></a>
<a id="astructbt__hci__rp__le__read__rl__size_html_a90c28070ee094c99c21c4dd229ff6ce5"></a>
<a id="astructbt__hci__rp__le__read__rl__size_html_af8a10aab21d54cce3529b1307769f6c6"></a>
<a id="astructbt__hci__rp__le__read__supp__states_html"></a>
<a id="astructbt__hci__rp__le__read__supp__states_html_a9b60476cc158a701b29b28bd21375130"></a>
<a id="astructbt__hci__rp__le__read__supp__states_html_aeed0cc41ee521c27f07d8cbf4b377a4f"></a>
<a id="astructbt__hci__rp__le__read__test__counters_html"></a>
<a id="astructbt__hci__rp__le__read__test__counters_html_a8121f879a3fb5550cc1aa468aacb81b7"></a>
<a id="astructbt__hci__rp__le__read__test__counters_html_a8c4b2674fb129ca0de0bc45c608e13c7"></a>
<a id="astructbt__hci__rp__le__read__test__counters_html_ae1e78d68e9f55b31092a07575a66c1c0"></a>
<a id="astructbt__hci__rp__le__read__test__counters_html_ae96d05ffb2fbc681c804b04c8791aeab"></a>
<a id="astructbt__hci__rp__le__read__test__counters_html_af6261d3547cd9b377fedc7a36891c2f7"></a>
<a id="astructbt__hci__rp__le__read__tx__power__level_html"></a>
<a id="astructbt__hci__rp__le__read__tx__power__level_html_a4c83db208bfcb7c9fd2211d192a26d90"></a>
<a id="astructbt__hci__rp__le__read__tx__power__level_html_a5f9c59660f7c5842712a4ad9ae1d9527"></a>
<a id="astructbt__hci__rp__le__read__tx__power__level_html_ad14f660eb67f1014d1a62b0e5a113969"></a>
<a id="astructbt__hci__rp__le__read__tx__power__level_html_ae65a43aad74b1081e88afdb533cbe813"></a>
<a id="astructbt__hci__rp__le__read__tx__power__level_html_aec00dfb34abce2d95af183b74f63d1f3"></a>
<a id="astructbt__hci__rp__le__read__tx__power_html"></a>
<a id="astructbt__hci__rp__le__read__tx__power_html_a1d794f1f7ea77eceac7dae2546eab047"></a>
<a id="astructbt__hci__rp__le__read__tx__power_html_a6d4ab95efda5cfc97ae11d83787da8d7"></a>
<a id="astructbt__hci__rp__le__read__tx__power_html_a805629b92c65e006082d819f578ed555"></a>
<a id="astructbt__hci__rp__le__reject__cis_html"></a>
<a id="astructbt__hci__rp__le__reject__cis_html_acd8311e13bdfd7edb2d404d80006f9d4"></a>
<a id="astructbt__hci__rp__le__reject__cis_html_af2dc8a839d3e19821ab8ec0d3dc427ec"></a>
<a id="astructbt__hci__rp__le__remove__cig_html"></a>
<a id="astructbt__hci__rp__le__remove__cig_html_a1335f26f1dc67ff8e2a1960d1b24b1a0"></a>
<a id="astructbt__hci__rp__le__remove__cig_html_a82e74fbbce714b035b1e53fd5f1b09b5"></a>
<a id="astructbt__hci__rp__le__remove__iso__path_html"></a>
<a id="astructbt__hci__rp__le__remove__iso__path_html_ab22e50e594e19931526feacd9bff33a3"></a>
<a id="astructbt__hci__rp__le__remove__iso__path_html_ae3b7704359989ca13582a5cd3742f588"></a>
<a id="astructbt__hci__rp__le__set__cig__params__test_html"></a>
<a id="astructbt__hci__rp__le__set__cig__params__test_html_a08b07863ed63ab627401c0c80bc3c7b4"></a>
<a id="astructbt__hci__rp__le__set__cig__params__test_html_a10816d0875092c8e6bd4b13b819c43c7"></a>
<a id="astructbt__hci__rp__le__set__cig__params__test_html_a65c11059bc00244e58d2ab8373e3e725"></a>
<a id="astructbt__hci__rp__le__set__cig__params__test_html_a932eadb4d750f79b4a7a9c3feb90fdcd"></a>
<a id="astructbt__hci__rp__le__set__cig__params_html"></a>
<a id="astructbt__hci__rp__le__set__cig__params_html_a2e95c6217d11169a8a611ea95dce70b6"></a>
<a id="astructbt__hci__rp__le__set__cig__params_html_a8426a2b9927bee05fb9a46b4b261c743"></a>
<a id="astructbt__hci__rp__le__set__cig__params_html_a8aff643e0ae41455eb9391cfdb45ebda"></a>
<a id="astructbt__hci__rp__le__set__cig__params_html_a951dc88e0cde4e1f0274684498741eac"></a>
<a id="astructbt__hci__rp__le__set__cl__cte__sampling__enable_html"></a>
<a id="astructbt__hci__rp__le__set__cl__cte__sampling__enable_html_a44db7f831e8d730ec3c80c01ef9543aa"></a>
<a id="astructbt__hci__rp__le__set__cl__cte__sampling__enable_html_a5962f97cef6e53452cdccab1c3440519"></a>
<a id="astructbt__hci__rp__le__set__conn__cte__rx__params_html"></a>
<a id="astructbt__hci__rp__le__set__conn__cte__rx__params_html_a3c3fb92d422e7ccaf0c98706d46b3e5a"></a>
<a id="astructbt__hci__rp__le__set__conn__cte__rx__params_html_ad38bb356876c16904e408405607de73c"></a>
<a id="astructbt__hci__rp__le__set__conn__cte__tx__params_html"></a>
<a id="astructbt__hci__rp__le__set__conn__cte__tx__params_html_a56f62b6d2c42cd22f73026a2fabc6986"></a>
<a id="astructbt__hci__rp__le__set__conn__cte__tx__params_html_aad553d484daed7ca08de132f4fb849ee"></a>
<a id="astructbt__hci__rp__le__set__data__len_html"></a>
<a id="astructbt__hci__rp__le__set__data__len_html_a207c6da11e0bb145bed7a9e551ddc608"></a>
<a id="astructbt__hci__rp__le__set__data__len_html_a8667db355a95691d58845f89e919aea4"></a>
<a id="astructbt__hci__rp__le__set__ext__adv__param_html"></a>
<a id="astructbt__hci__rp__le__set__ext__adv__param_html_a6baae317455ffbb489066fcd1fb068c8"></a>
<a id="astructbt__hci__rp__le__set__ext__adv__param_html_a8a876d0e3d4d9d066a27c054569f0b9a"></a>
<a id="astructbt__hci__rp__le__set__host__feature_html"></a>
<a id="astructbt__hci__rp__le__set__host__feature_html_a2e7cfc16da9fc0d00c35111811bf7c28"></a>
<a id="astructbt__hci__rp__le__set__path__loss__reporting__enable_html"></a>
<a id="astructbt__hci__rp__le__set__path__loss__reporting__enable_html_a27991d6f123fabf13ecd926cff4e5637"></a>
<a id="astructbt__hci__rp__le__set__path__loss__reporting__enable_html_a3ea4ffd2a32c8fb720ce555db4585888"></a>
<a id="astructbt__hci__rp__le__set__path__loss__reporting__parameters_html"></a>
<a id="astructbt__hci__rp__le__set__path__loss__reporting__parameters_html_a7a2fb4061792d4cc004c77ac8d5e84dc"></a>
<a id="astructbt__hci__rp__le__set__path__loss__reporting__parameters_html_afeb9563db35ddba7ed9de6070463c508"></a>
<a id="astructbt__hci__rp__le__setup__iso__path_html"></a>
<a id="astructbt__hci__rp__le__setup__iso__path_html_aa8effdcc4ba155b840ef789f20bad19e"></a>
<a id="astructbt__hci__rp__le__setup__iso__path_html_adde60b0dc6ec3d8caccae1d55d78d9a4"></a>
<a id="astructbt__hci__rp__le__test__end_html"></a>
<a id="astructbt__hci__rp__le__test__end_html_a2ac412ef9a5fc7651315afe042856cce"></a>
<a id="astructbt__hci__rp__le__test__end_html_a9e283118e4ea48b0df66a4cd1c1cf9a1"></a>
<a id="astructbt__hci__rp__pin__code__neg__reply_html"></a>
<a id="astructbt__hci__rp__pin__code__neg__reply_html_a10bcc55407e22417256c464684a41e58"></a>
<a id="astructbt__hci__rp__pin__code__neg__reply_html_a168caf2a517aa573bd6acaf48e414e9b"></a>
<a id="astructbt__hci__rp__pin__code__reply_html"></a>
<a id="astructbt__hci__rp__pin__code__reply_html_a3f167661b8d3f63ab12e6f64fb33986b"></a>
<a id="astructbt__hci__rp__pin__code__reply_html_afc7c991fd8050e8aae56b8587b5ee01d"></a>
<a id="astructbt__hci__rp__read__auth__payload__timeout_html"></a>
<a id="astructbt__hci__rp__read__auth__payload__timeout_html_a3eadeab880eb75c914be654dbc685f3f"></a>
<a id="astructbt__hci__rp__read__auth__payload__timeout_html_ab4092720dad9a01f4e179eb2f0112aed"></a>
<a id="astructbt__hci__rp__read__auth__payload__timeout_html_ab53b7e03c68dcd040e38fdc7429b2d3b"></a>
<a id="astructbt__hci__rp__read__bd__addr_html"></a>
<a id="astructbt__hci__rp__read__bd__addr_html_a5230de2a3a6c4161d076b59901790e1e"></a>
<a id="astructbt__hci__rp__read__bd__addr_html_aec2c022a465982a3868100699c95f4e6"></a>
<a id="astructbt__hci__rp__read__buffer__size_html"></a>
<a id="astructbt__hci__rp__read__buffer__size_html_a6adf126acfcec722dc078d097d2b2ba8"></a>
<a id="astructbt__hci__rp__read__buffer__size_html_a7d475559145f469006b2ef147704cd99"></a>
<a id="astructbt__hci__rp__read__buffer__size_html_a87ff361282be71aa60c7f88c50a7492f"></a>
<a id="astructbt__hci__rp__read__buffer__size_html_aba3f1597c929e3721c769beb98000218"></a>
<a id="astructbt__hci__rp__read__buffer__size_html_abc01fa1df6d787f0a2cb865daed5f4cc"></a>
<a id="astructbt__hci__rp__read__class__of__device_html"></a>
<a id="astructbt__hci__rp__read__class__of__device_html_a221d175e8016fd04151c4969d1134910"></a>
<a id="astructbt__hci__rp__read__class__of__device_html_ac6483440d3095de548f477cd845c0cee"></a>
<a id="astructbt__hci__rp__read__codec__capabilities_html"></a>
<a id="astructbt__hci__rp__read__codec__capabilities_html_a71b7df63502bf42a26868e69893ddcfe"></a>
<a id="astructbt__hci__rp__read__codec__capabilities_html_ac224ea998e3af12f97232288266da8d2"></a>
<a id="astructbt__hci__rp__read__codec__capabilities_html_ae0c84013512c461f3b6231162d6f3020"></a>
<a id="astructbt__hci__rp__read__codecs__v2_html"></a>
<a id="astructbt__hci__rp__read__codecs__v2_html_a098563f274de085ac97415f1b5e15f3c"></a>
<a id="astructbt__hci__rp__read__codecs__v2_html_a2e9866d0f9fb42b54c406a9ea5890913"></a>
<a id="astructbt__hci__rp__read__codecs_html"></a>
<a id="astructbt__hci__rp__read__codecs_html_a017182988634c6acbfbfdd7c9609f5dc"></a>
<a id="astructbt__hci__rp__read__codecs_html_a44e615f375b35cce9f949562555c429b"></a>
<a id="astructbt__hci__rp__read__conn__accept__timeout_html"></a>
<a id="astructbt__hci__rp__read__conn__accept__timeout_html_a01ca30c92311ec1df19a4cf835ea74cf"></a>
<a id="astructbt__hci__rp__read__conn__accept__timeout_html_afeb5888722ee368e02c6b27b75ab2a70"></a>
<a id="astructbt__hci__rp__read__ctlr__delay_html"></a>
<a id="astructbt__hci__rp__read__ctlr__delay_html_a2f17081cf767643f3a9ad9d115ef5320"></a>
<a id="astructbt__hci__rp__read__ctlr__delay_html_a4c468053c4a86d1ab462c1e6f17f1013"></a>
<a id="astructbt__hci__rp__read__ctlr__delay_html_ab48d1d92cdf9470a93487434b3824d17"></a>
<a id="astructbt__hci__rp__read__default__link__policy__settings_html"></a>
<a id="astructbt__hci__rp__read__default__link__policy__settings_html_a0b4c5e26b1d7f387a86192edd1efcdf2"></a>
<a id="astructbt__hci__rp__read__default__link__policy__settings_html_ad2ba59e00a2f2931dd52809029373f46"></a>
<a id="astructbt__hci__rp__read__encryption__key__size_html"></a>
<a id="astructbt__hci__rp__read__encryption__key__size_html_a17213ccb9179739aa79c3749a2296f65"></a>
<a id="astructbt__hci__rp__read__encryption__key__size_html_af0b89b2035f956891244b10409be0f51"></a>
<a id="astructbt__hci__rp__read__encryption__key__size_html_af1cd71c6216b26d460c04a68405f05d5"></a>
<a id="astructbt__hci__rp__read__link__policy__settings_html"></a>
<a id="astructbt__hci__rp__read__link__policy__settings_html_a4ec0cdfa8ae48d9ed8ae2d46f16a9638"></a>
<a id="astructbt__hci__rp__read__link__policy__settings_html_a69fe8085d161bf87051a52dc9c511156"></a>
<a id="astructbt__hci__rp__read__link__policy__settings_html_ad73d8ed381f8bbc4914c38bb0ebcae01"></a>
<a id="astructbt__hci__rp__read__link__supervision__timeout_html"></a>
<a id="astructbt__hci__rp__read__link__supervision__timeout_html_a1400aa0d8172c0cbf6b24b6571e73f73"></a>
<a id="astructbt__hci__rp__read__link__supervision__timeout_html_ad1048becb6523d7302fdbbd739bc1b99"></a>
<a id="astructbt__hci__rp__read__link__supervision__timeout_html_aec86b11707e4728dd0849f12c32cf8f8"></a>
<a id="astructbt__hci__rp__read__local__ext__features_html"></a>
<a id="astructbt__hci__rp__read__local__ext__features_html_a3532e208b3fd347db80d8c55eade3c2d"></a>
<a id="astructbt__hci__rp__read__local__ext__features_html_a669e8c6faa4e45f472e4f8a3ebb03050"></a>
<a id="astructbt__hci__rp__read__local__ext__features_html_a7e3669651dc2c2ed9541b7e4945a27f9"></a>
<a id="astructbt__hci__rp__read__local__ext__features_html_a9011f2c89f75939fa92fcf249d2203da"></a>
<a id="astructbt__hci__rp__read__local__features_html"></a>
<a id="astructbt__hci__rp__read__local__features_html_a0ff73da5704ada47f8f79c113254820d"></a>
<a id="astructbt__hci__rp__read__local__features_html_ae660b4a772f96bf72bd08124bf26b352"></a>
<a id="astructbt__hci__rp__read__local__version__info_html"></a>
<a id="astructbt__hci__rp__read__local__version__info_html_a04161ed3cc0b9c3c442e3464501ce118"></a>
<a id="astructbt__hci__rp__read__local__version__info_html_a1cc521426e530344a328e935152dd488"></a>
<a id="astructbt__hci__rp__read__local__version__info_html_a43f29cf08a2399e818bfa441c6b7a1f3"></a>
<a id="astructbt__hci__rp__read__local__version__info_html_a634641751852f66aabb408bf1b4d0cd2"></a>
<a id="astructbt__hci__rp__read__local__version__info_html_a7cd6ba190137eaf7c4eb9c2d7e5b36ce"></a>
<a id="astructbt__hci__rp__read__local__version__info_html_a935f990f7c28f7c89660c2b8ab975f43"></a>
<a id="astructbt__hci__rp__read__rssi_html"></a>
<a id="astructbt__hci__rp__read__rssi_html_a1071300bd61fcaab65683187ae393cae"></a>
<a id="astructbt__hci__rp__read__rssi_html_a8f91b69a99bd61a7a59d84b3a9c3f235"></a>
<a id="astructbt__hci__rp__read__rssi_html_aa3c4041dd240b1185c7fc8bbef74a17a"></a>
<a id="astructbt__hci__rp__read__supported__commands_html"></a>
<a id="astructbt__hci__rp__read__supported__commands_html_a3d36d892f83cfcb1d2fc955ec71ff061"></a>
<a id="astructbt__hci__rp__read__supported__commands_html_afd0dc4411a4c7692515139392bffedd0"></a>
<a id="astructbt__hci__rp__read__tx__power__level_html"></a>
<a id="astructbt__hci__rp__read__tx__power__level_html_a46526b820038bb445a7824a7b4bfc870"></a>
<a id="astructbt__hci__rp__read__tx__power__level_html_ac2bd21e90145102bc483c2b0b3cdd416"></a>
<a id="astructbt__hci__rp__read__tx__power__level_html_af40a8e2e663872e8d9fdde839cc6d1b4"></a>
<a id="astructbt__hci__rp__remote__name__cancel_html"></a>
<a id="astructbt__hci__rp__remote__name__cancel_html_a455432799a1272f88b2b00a35a2e7ef5"></a>
<a id="astructbt__hci__rp__remote__name__cancel_html_ac7fadee392b126cb50cef7a6336926cb"></a>
<a id="astructbt__hci__rp__sniff__subrating_html"></a>
<a id="astructbt__hci__rp__sniff__subrating_html_a39e9f3ec6e7d9c534ca6160172990fa6"></a>
<a id="astructbt__hci__rp__sniff__subrating_html_aa5d11db99d6f467a1e93afe031c08e14"></a>
<a id="astructbt__hci__rp__user__confirm__reply_html"></a>
<a id="astructbt__hci__rp__user__confirm__reply_html_a91678db3ae2a696ba7b9dd5bc080c488"></a>
<a id="astructbt__hci__rp__user__confirm__reply_html_ab07114550c2da3c1e9925cb883bf3a89"></a>
<a id="astructbt__hci__rp__write__auth__payload__timeout_html"></a>
<a id="astructbt__hci__rp__write__auth__payload__timeout_html_a467c6585c913dba03dcfdf5bf4fa688e"></a>
<a id="astructbt__hci__rp__write__auth__payload__timeout_html_af1783a29e6a167fc20b62bd273215b35"></a>
<a id="astructbt__hci__rp__write__conn__accept__timeout_html"></a>
<a id="astructbt__hci__rp__write__conn__accept__timeout_html_a1f9eee1a5843747e0d224b86b602a3da"></a>
<a id="astructbt__hci__sco__hdr_html"></a>
<a id="astructbt__hci__sco__hdr_html_a158f67c3743684c28728b62db5cf2590"></a>
<a id="astructbt__hci__sco__hdr_html_a4b4c915bec966c17567c14e2df9c1581"></a>
<a id="astructbt__hci__std__codec__info__v2_html"></a>
<a id="astructbt__hci__std__codec__info__v2_html_ae82a0896904c7feb2634579b393bf05e"></a>
<a id="astructbt__hci__std__codec__info__v2_html_aea766ba4b911223eeb351e0123e54f5f"></a>
<a id="astructbt__hci__std__codec__info_html"></a>
<a id="astructbt__hci__std__codec__info_html_a56e21eca5bbc83cb081aea1c67a7a60d"></a>
<a id="astructbt__hci__std__codecs__v2_html"></a>
<a id="astructbt__hci__std__codecs__v2_html_aafdb6d96d99063a7a447d80e1830a624"></a>
<a id="astructbt__hci__std__codecs__v2_html_ab14fdde478e290235f68aae375969c09"></a>
<a id="astructbt__hci__std__codecs_html"></a>
<a id="astructbt__hci__std__codecs_html_a32767e90384ef74a3e740597eacfcf53"></a>
<a id="astructbt__hci__std__codecs_html_ad3e63bf445bb6b8e654baa8490cdf547"></a>
<a id="astructbt__hci__vs__codec__info__v2_html"></a>
<a id="astructbt__hci__vs__codec__info__v2_html_aa6ce27b4acd3dff516e4d7ed2e6434bc"></a>
<a id="astructbt__hci__vs__codec__info__v2_html_ac2a91a045e4b53315850b6d4f1d38b2c"></a>
<a id="astructbt__hci__vs__codec__info__v2_html_ae7b7d5d65629a1e3039b3c7cf167a9c1"></a>
<a id="astructbt__hci__vs__codec__info_html"></a>
<a id="astructbt__hci__vs__codec__info_html_a3c7eea7bae36c7a63457051401526382"></a>
<a id="astructbt__hci__vs__codec__info_html_a8170dac825b76f3dfb5fde5eed04c4c0"></a>
<a id="astructbt__hci__vs__codecs__v2_html"></a>
<a id="astructbt__hci__vs__codecs__v2_html_a6cd8aa58517d59d565474513f755cfee"></a>
<a id="astructbt__hci__vs__codecs__v2_html_ae4cb3a40401594f8e0f18391b9d31a23"></a>
<a id="astructbt__hci__vs__codecs_html"></a>
<a id="astructbt__hci__vs__codecs_html_a2caf18ce5905e3962da000f3b00b623f"></a>
<a id="astructbt__hci__vs__codecs_html_a4e72426599d5bc617fde4f1a4a095527"></a>
<a id="astructbt__hci__write__local__name_html"></a>
<a id="astructbt__hci__write__local__name_html_a8d2cd9a16525c3fc10ae0e3f196110da"></a>
<a id="astructhci__cp__le__conn__update_html"></a>
<a id="astructhci__cp__le__conn__update_html_a3ae86fccacf462463fe520eb1e06fa62"></a>
<a id="astructhci__cp__le__conn__update_html_a401169ccc5dbf6cf0abd6154738f00dc"></a>
<a id="astructhci__cp__le__conn__update_html_a5606b8795defc338b27d1a130064351e"></a>
<a id="astructhci__cp__le__conn__update_html_a8e48e5e195aea7f581cfc7246da79d72"></a>
<a id="astructhci__cp__le__conn__update_html_a99fc0b3b0f810f1d6e174aa9045d298a"></a>
<a id="astructhci__cp__le__conn__update_html_ab76ecdf6f7e5a5bb581cbd26f67d8f9f"></a>
<a id="astructhci__cp__le__conn__update_html_adcfee3c727118069897515a00e7ead66"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/* hci.h - Bluetooth Host Control Interface types */

/*
 * Copyright (c) 2015-2016 Intel Corporation
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_HCI_TYPES_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_HCI_TYPES_H_

#include <stdbool.h>
#include <stdint.h>

#include <zephyr/bluetooth/addr.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Bluetooth spec v5.4 Vol 4, Part A Table 2.1: HCI packet indicators
 * The following definitions are intended for use with the UART Transport Layer and
 * may be reused with other transport layers if desired.
 */
#define BT_HCI_H4_NONE                  0x00    /* None of the known packet types */
#define BT_HCI_H4_CMD                   0x01    /* HCI Command packet */
#define BT_HCI_H4_ACL                   0x02    /* HCI ACL Data packet */
#define BT_HCI_H4_SCO                   0x03    /* HCI Synchronous Data packet */
#define BT_HCI_H4_EVT                   0x04    /* HCI Event packet */
#define BT_HCI_H4_ISO                   0x05    /* HCI ISO Data packet */

#define BT_HCI_OWN_ADDR_PUBLIC          0x00
#define BT_HCI_OWN_ADDR_RANDOM          0x01
#define BT_HCI_OWN_ADDR_RPA_OR_PUBLIC   0x02
#define BT_HCI_OWN_ADDR_RPA_OR_RANDOM   0x03
#define BT_HCI_OWN_ADDR_RPA_MASK        0x02

#define BT_HCI_PEER_ADDR_RPA_UNRESOLVED 0xfe
#define BT_HCI_PEER_ADDR_ANONYMOUS      0xff

#define BT_ENC_KEY_SIZE_MIN             0x07
#define BT_ENC_KEY_SIZE_MAX             0x10

#define BT_HCI_ADV_HANDLE_INVALID       0xff
#define BT_HCI_SYNC_HANDLE_INVALID      0xffff
#define BT_HCI_PAWR_SUBEVENT_MAX        128

/* Bluetooth spec v5.4 Vol 4, Part E - 5.4.3 HCI Synchronous Data Packets */
struct bt_hci_sco_hdr {
        uint16_t handle; /* 12 bit handle, 2 bit Packet Status Flag, 1 bit RFU */
        uint8_t  len;
} __packed;
#define BT_HCI_SCO_HDR_SIZE             3

/* Bluetooth spec v5.4 Vol 4, Part E - 5.4.4 HCI Event Packet */
struct bt_hci_evt_hdr {
        uint8_t  evt;
        uint8_t  len;
        uint8_t  data[];
} __packed;
#define BT_HCI_EVT_HDR_SIZE             2

#define BT_ACL_START_NO_FLUSH           0x00
#define BT_ACL_CONT                     0x01
#define BT_ACL_START                    0x02
#define BT_ACL_COMPLETE                 0x03

#define BT_ACL_POINT_TO_POINT           0x00
#define BT_ACL_BROADCAST                0x01

#define BT_ACL_HANDLE_MASK              BIT_MASK(12)

#define bt_acl_handle(h)                ((h) & BT_ACL_HANDLE_MASK)
#define bt_acl_flags(h)                 ((h) >> 12)
#define bt_acl_flags_pb(f)              ((f) & BIT_MASK(2))
#define bt_acl_flags_bc(f)              ((f) >> 2)
#define bt_acl_handle_pack(h, f)        ((h) | ((f) << 12))

/* Bluetooth spec v5.4 Vol 4, Part E - 5.4.2 ACL Data Packets */
struct bt_hci_acl_hdr {
        uint16_t handle;
        uint16_t len;
} __packed;
#define BT_HCI_ACL_HDR_SIZE             4

#define BT_ISO_START                    0x00
#define BT_ISO_CONT                     0x01
#define BT_ISO_SINGLE                   0x02
#define BT_ISO_END                      0x03

#define bt_iso_handle(h)                ((h) & 0x0fff)
#define bt_iso_flags(h)                 ((h) >> 12)
#define bt_iso_flags_pb(f)              ((f) & 0x0003)
#define bt_iso_flags_ts(f)              (((f) >> 2) & 0x0001)
#define bt_iso_pack_flags(pb, ts) \
        (((pb) & 0x0003) | (((ts) & 0x0001) << 2))
#define bt_iso_handle_pack(h, pb, ts) \
        ((h) | (bt_iso_pack_flags(pb, ts) << 12))
#define bt_iso_hdr_len(h)                ((h) & BIT_MASK(14))

#define BT_ISO_DATA_VALID                0x00
#define BT_ISO_DATA_INVALID              0x01
#define BT_ISO_DATA_NOP                  0x02

#define bt_iso_pkt_len(h)                ((h) & BIT_MASK(12))
#define bt_iso_pkt_flags(h)              ((h) >> 14)
#define bt_iso_pkt_len_pack(h, f)        (((h) & BIT_MASK(12)) | ((f) << 14))

struct bt_hci_iso_sdu_hdr {
        uint16_t sn;
        uint16_t slen; /* 12 bit len, 2 bit RFU, 2 bit packet status */
} __packed;
#define BT_HCI_ISO_SDU_HDR_SIZE          4

struct bt_hci_iso_sdu_ts_hdr {
        uint32_t ts;
        struct bt_hci_iso_sdu_hdr sdu;
} __packed;
#define BT_HCI_ISO_SDU_TS_HDR_SIZE       8

/* Bluetooth spec v5.4 Vol 4, Part E - 5.4.5 HCI ISO Data Packets */
struct bt_hci_iso_hdr {
        uint16_t handle; /* 12 bit handle, 2 bit PB flags, 1 bit TS_Flag, 1 bit RFU */
        uint16_t len; /* 14 bits, 2 bits RFU */
} __packed;
#define BT_HCI_ISO_HDR_SIZE             4

/* Bluetooth spec v5.4 Vol 4, Part E - 5.4.1 HCI Command Packet */
struct bt_hci_cmd_hdr {
        uint16_t opcode;
        uint8_t  param_len;
} __packed;
#define BT_HCI_CMD_HDR_SIZE             3

/* Supported Commands */
#define BT_CMD_TEST(cmd, octet, bit)            (cmd[octet] & BIT(bit))
#define BT_CMD_LE_STATES(cmd)                   BT_CMD_TEST(cmd, 28, 3)

#define BT_FEAT_TEST(feat, page, octet, bit)    ((feat[page][octet] & BIT(bit)) != 0)

#define BT_FEAT_BREDR(feat)                     !BT_FEAT_TEST(feat, 0, 4, 5)
#define BT_FEAT_LE(feat)                        BT_FEAT_TEST(feat, 0, 4, 6)
#define BT_FEAT_EXT_FEATURES(feat)              BT_FEAT_TEST(feat, 0, 7, 7)
#define BT_FEAT_HOST_SSP(feat)                  BT_FEAT_TEST(feat, 1, 0, 0)
#define BT_FEAT_SC(feat)                        BT_FEAT_TEST(feat, 2, 1, 0)

#define BT_FEAT_LMP_SCO_CAPABLE(feat)           BT_FEAT_TEST(feat, 0, 1, 3)
#define BT_FEAT_LMP_ESCO_CAPABLE(feat)          BT_FEAT_TEST(feat, 0, 3, 7)
#define BT_FEAT_HV2_PKT(feat)                   BT_FEAT_TEST(feat, 0, 1, 4)
#define BT_FEAT_HV3_PKT(feat)                   BT_FEAT_TEST(feat, 0, 1, 5)
#define BT_FEAT_EV4_PKT(feat)                   BT_FEAT_TEST(feat, 0, 4, 0)
#define BT_FEAT_EV5_PKT(feat)                   BT_FEAT_TEST(feat, 0, 4, 1)
#define BT_FEAT_2EV3_PKT(feat)                  BT_FEAT_TEST(feat, 0, 5, 5)
#define BT_FEAT_3EV3_PKT(feat)                  BT_FEAT_TEST(feat, 0, 5, 6)
#define BT_FEAT_3SLOT_PKT(feat)                 BT_FEAT_TEST(feat, 0, 5, 7)

/* LE features */
#define BT_LE_FEAT_BIT_ENC                      0
#define BT_LE_FEAT_BIT_CONN_PARAM_REQ           1
#define BT_LE_FEAT_BIT_EXT_REJ_IND              2
#define BT_LE_FEAT_BIT_PER_INIT_FEAT_XCHG       3
#define BT_LE_FEAT_BIT_PING                     4
#define BT_LE_FEAT_BIT_DLE                      5
#define BT_LE_FEAT_BIT_PRIVACY                  6
#define BT_LE_FEAT_BIT_EXT_SCAN                 7
#define BT_LE_FEAT_BIT_PHY_2M                   8
#define BT_LE_FEAT_BIT_SMI_TX                   9
#define BT_LE_FEAT_BIT_SMI_RX                   10
#define BT_LE_FEAT_BIT_PHY_CODED                11
#define BT_LE_FEAT_BIT_EXT_ADV                  12
#define BT_LE_FEAT_BIT_PER_ADV                  13
#define BT_LE_FEAT_BIT_CHAN_SEL_ALGO_2          14
#define BT_LE_FEAT_BIT_PWR_CLASS_1              15
#define BT_LE_FEAT_BIT_MIN_USED_CHAN_PROC       16
#define BT_LE_FEAT_BIT_CONN_CTE_REQ             17
#define BT_LE_FEAT_BIT_CONN_CTE_RESP            18
#define BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_TX    19
#define BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_RX    20
#define BT_LE_FEAT_BIT_ANT_SWITCH_TX_AOD        21
#define BT_LE_FEAT_BIT_ANT_SWITCH_RX_AOA        22
#define BT_LE_FEAT_BIT_RX_CTE                   23
#define BT_LE_FEAT_BIT_PAST_SEND                24
#define BT_LE_FEAT_BIT_PAST_RECV                25
#define BT_LE_FEAT_BIT_SCA_UPDATE               26
#define BT_LE_FEAT_BIT_REMOTE_PUB_KEY_VALIDATE  27
#define BT_LE_FEAT_BIT_CIS_CENTRAL              28
#define BT_LE_FEAT_BIT_CIS_PERIPHERAL           29
#define BT_LE_FEAT_BIT_ISO_BROADCASTER          30
#define BT_LE_FEAT_BIT_SYNC_RECEIVER            31
#define BT_LE_FEAT_BIT_ISO_CHANNELS             32
#define BT_LE_FEAT_BIT_PWR_CTRL_REQ             33
#define BT_LE_FEAT_BIT_PWR_CHG_IND              34
#define BT_LE_FEAT_BIT_PATH_LOSS_MONITOR        35
#define BT_LE_FEAT_BIT_PER_ADV_ADI_SUPP         36
#define BT_LE_FEAT_BIT_CONN_SUBRATING           37
#define BT_LE_FEAT_BIT_CONN_SUBRATING_HOST_SUPP 38
#define BT_LE_FEAT_BIT_CHANNEL_CLASSIFICATION   39
#define BT_LE_FEAT_BIT_ADV_CODING_SEL           40
#define BT_LE_FEAT_BIT_ADV_CODING_SEL_HOST      41
#define BT_LE_FEAT_BIT_DECISION_ADV_FILTER      42
#define BT_LE_FEAT_BIT_PAWR_ADVERTISER          43
#define BT_LE_FEAT_BIT_PAWR_SCANNER             44
#define BT_LE_FEAT_BIT_UNSEG_FRAMED_MODE        45
#define BT_LE_FEAT_BIT_CHANNEL_SOUNDING         46
#define BT_LE_FEAT_BIT_CHANNEL_SOUNDING_HOST    47
#define BT_LE_FEAT_BIT_CHANNEL_SOUNDING_TONE_QUAL_IND    48
#define BT_LE_FEAT_BIT_EXTENDED_FEAT_SET        63
#define BT_LE_FEAT_BIT_FRAME_SPACE_UPDATE       65
#define BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS   72
#define BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS_HOST_SUPP  73

#define BT_LE_FEAT_TEST(feat, n)                (feat[(n) >> 3] & \
                                                 BIT((n) & 7))

#define BT_FEAT_LE_ENCR(feat)                     BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_ENC)
#define BT_FEAT_LE_CONN_PARAM_REQ_PROC(feat)      BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CONN_PARAM_REQ)
#define BT_FEAT_LE_PER_INIT_FEAT_XCHG(feat)       BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PER_INIT_FEAT_XCHG)
#define BT_FEAT_LE_DLE(feat)                      BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_DLE)
#define BT_FEAT_LE_PHY_2M(feat)                   BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PHY_2M)
#define BT_FEAT_LE_PHY_CODED(feat)                BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PHY_CODED)
#define BT_FEAT_LE_PRIVACY(feat)                  BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PRIVACY)

#define BT_FEAT_LE_EXT_SCAN(feat)                 BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_EXT_SCAN)
#define BT_FEAT_LE_EXT_ADV(feat)                  BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_EXT_ADV)
#define BT_FEAT_LE_EXT_PER_ADV(feat)              BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PER_ADV)
#define BT_FEAT_LE_CONNECTION_CTE_REQ(feat)       BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CONN_CTE_REQ)
#define BT_FEAT_LE_CONNECTION_CTE_RESP(feat)      BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CONN_CTE_RESP)
#define BT_FEAT_LE_CONNECTIONLESS_CTE_TX(feat)    BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_TX)
#define BT_FEAT_LE_CONNECTIONLESS_CTE_RX(feat)    BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_RX)
#define BT_FEAT_LE_ANT_SWITCH_TX_AOD(feat)        BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_ANT_SWITCH_TX_AOD)
#define BT_FEAT_LE_ANT_SWITCH_RX_AOA(feat)        BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_ANT_SWITCH_RX_AOA)
#define BT_FEAT_LE_RX_CTE(feat)                   BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_RX_CTE)
#define BT_FEAT_LE_PAST_SEND(feat)                BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PAST_SEND)
#define BT_FEAT_LE_PAST_RECV(feat)                BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PAST_RECV)
#define BT_FEAT_LE_CIS_CENTRAL(feat)              BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CIS_CENTRAL)
#define BT_FEAT_LE_CIS_PERIPHERAL(feat)           BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CIS_PERIPHERAL)
#define BT_FEAT_LE_ISO_BROADCASTER(feat)          BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_ISO_BROADCASTER)
#define BT_FEAT_LE_SYNC_RECEIVER(feat)            BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_SYNC_RECEIVER)
#define BT_FEAT_LE_ISO_CHANNELS(feat)             BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_ISO_CHANNELS)
#define BT_FEAT_LE_PWR_CTRL_REQ(feat)             BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PWR_CTRL_REQ)
#define BT_FEAT_LE_PWR_CHG_IND(feat)              BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PWR_CHG_IND)
#define BT_FEAT_LE_PATH_LOSS_MONITOR(feat)        BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PATH_LOSS_MONITOR)
#define BT_FEAT_LE_PER_ADV_ADI_SUPP(feat)         BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PER_ADV_ADI_SUPP)
#define BT_FEAT_LE_CONN_SUBRATING(feat)           BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CONN_SUBRATING)
#define BT_FEAT_LE_CONN_SUBRATING_HOST_SUPP(feat) BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CONN_SUBRATING_HOST_SUPP)
#define BT_FEAT_LE_CHANNEL_CLASSIFICATION(feat)   BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CHANNEL_CLASSIFICATION)
#define BT_FEAT_LE_ADV_CODING_SEL(feat)           BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_ADV_CODING_SEL)
#define BT_FEAT_LE_ADV_CODING_SEL_HOST(feat)      BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_ADV_CODING_SEL_HOST)
#define BT_FEAT_LE_PAWR_ADVERTISER(feat)          BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PAWR_ADVERTISER)
#define BT_FEAT_LE_PAWR_SCANNER(feat)             BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_PAWR_SCANNER)
#define BT_FEAT_LE_CHANNEL_SOUNDING(feat)         BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CHANNEL_SOUNDING)
#define BT_FEAT_LE_CHANNEL_SOUNDING_HOST(feat)    BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_CHANNEL_SOUNDING_HOST)
#define BT_FEAT_LE_EXTENDED_FEAT_SET(feat)        BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_EXTENDED_FEAT_SET)
#define BT_FEAT_LE_FRAME_SPACE_UPDATE_SET(feat)   BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_FRAME_SPACE_UPDATE)
#define BT_FEAT_LE_SHORTER_CONN_INTERVALS(feat)   BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS)
#define BT_FEAT_LE_SHORTER_CONN_INTERVALS_HOST_SUPP(feat) BT_LE_FEAT_TEST(feat, \
                                                  BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS_HOST_SUPP)

#define BT_FEAT_LE_CIS(feat)            (BT_FEAT_LE_CIS_CENTRAL(feat) | \
                                        BT_FEAT_LE_CIS_PERIPHERAL(feat))
#define BT_FEAT_LE_BIS(feat)            (BT_FEAT_LE_ISO_BROADCASTER(feat) | \
                                        BT_FEAT_LE_SYNC_RECEIVER(feat))
#define BT_FEAT_LE_ISO(feat)            (BT_FEAT_LE_CIS(feat) | \
                                        BT_FEAT_LE_BIS(feat))

/* LE States. See Core_v5.4, Vol 4, Part E, Section 7.8.27 */
#define BT_LE_STATES_PER_CONN_ADV(states)     (states & BIT64_MASK(38))

#if defined(CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL)
/* Both passive and active scanner can be run in parallel with initiator. */
#define BT_LE_STATES_SCAN_INIT(states) ((states) & BIT64_MASK(22) && \
                                        (states) & BIT64_MASK(23))

#else
#define BT_LE_STATES_SCAN_INIT(states)  0
#endif

/* Bonding/authentication types */
#define BT_HCI_NO_BONDING                       0x00
#define BT_HCI_NO_BONDING_MITM                  0x01
#define BT_HCI_DEDICATED_BONDING                0x02
#define BT_HCI_DEDICATED_BONDING_MITM           0x03
#define BT_HCI_GENERAL_BONDING                  0x04
#define BT_HCI_GENERAL_BONDING_MITM             0x05

/*
 * MITM protection is enabled in SSP authentication requirements octet when
 * LSB bit is set.
 */
#define BT_MITM                                 0x01

/* I/O capabilities */
#define BT_IO_DISPLAY_ONLY                      0x00
#define BT_IO_DISPLAY_YESNO                     0x01
#define BT_IO_KEYBOARD_ONLY                     0x02
#define BT_IO_NO_INPUT_OUTPUT                   0x03

/* SCO packet types */
#define HCI_PKT_TYPE_HV1                        0x0020
#define HCI_PKT_TYPE_HV2                        0x0040
#define HCI_PKT_TYPE_HV3                        0x0080

/* eSCO packet types */
#define HCI_PKT_TYPE_SCO_HV1                    0x0001
#define HCI_PKT_TYPE_SCO_HV2                    0x0002
#define HCI_PKT_TYPE_SCO_HV3                    0x0004
#define HCI_PKT_TYPE_ESCO_EV3                   0x0008
#define HCI_PKT_TYPE_ESCO_EV4                   0x0010
#define HCI_PKT_TYPE_ESCO_EV5                   0x0020
#define HCI_PKT_TYPE_ESCO_2EV3                  0x0040
#define HCI_PKT_TYPE_ESCO_3EV3                  0x0080
#define HCI_PKT_TYPE_ESCO_2EV5                  0x0100
#define HCI_PKT_TYPE_ESCO_3EV5                  0x0200


#define ESCO_PKT_MASK                           (HCI_PKT_TYPE_SCO_HV1 | \
                                                 HCI_PKT_TYPE_SCO_HV2 | \
                                                 HCI_PKT_TYPE_SCO_HV3 | \
                                                 HCI_PKT_TYPE_ESCO_EV3 | \
                                                 HCI_PKT_TYPE_ESCO_EV4 | \
                                                 HCI_PKT_TYPE_ESCO_EV5)
#define SCO_PKT_MASK                            (HCI_PKT_TYPE_SCO_HV1 | \
                                                 HCI_PKT_TYPE_SCO_HV2 | \
                                                 HCI_PKT_TYPE_SCO_HV3)
#define EDR_ESCO_PKT_MASK                       (HCI_PKT_TYPE_ESCO_2EV3 | \
                                                 HCI_PKT_TYPE_ESCO_3EV3 | \
                                                 HCI_PKT_TYPE_ESCO_2EV5 | \
                                                 HCI_PKT_TYPE_ESCO_3EV5)

/* HCI BR/EDR link types */
#define BT_HCI_SCO                              0x00
#define BT_HCI_ACL                              0x01
#define BT_HCI_ESCO                             0x02

/* OpCode Group Fields */
#define BT_OGF_LINK_CTRL                        0x01
#define BT_OGF_LINK_POLICY                      0x02
#define BT_OGF_BASEBAND                         0x03
#define BT_OGF_INFO                             0x04
#define BT_OGF_STATUS                           0x05
#define BT_OGF_LE                               0x08
#define BT_OGF_VS                               0x3f

/* Construct OpCode from OGF and OCF */
#define BT_OP(ogf, ocf)                         ((ocf) | ((ogf) << 10))

/* Invalid opcode */
#define BT_OP_NOP                               0x0000

/* Obtain OGF from OpCode */
#define BT_OGF(opcode)                          (((opcode) >> 10) & BIT_MASK(6))
/* Obtain OCF from OpCode */
#define BT_OCF(opcode)                          ((opcode) & BIT_MASK(10))

#define BT_HCI_OP_INQUIRY                       BT_OP(BT_OGF_LINK_CTRL, 0x0001) /* 0x0401 */
struct bt_hci_op_inquiry {
        uint8_t lap[3];
        uint8_t length;
        uint8_t num_rsp;
} __packed;

#define BT_HCI_OP_INQUIRY_CANCEL                BT_OP(BT_OGF_LINK_CTRL, 0x0002) /* 0x0402 */

#define BT_HCI_OP_CONNECT                       BT_OP(BT_OGF_LINK_CTRL, 0x0005) /* 0x0405 */
struct bt_hci_cp_connect {
        bt_addr_t bdaddr;
        uint16_t  packet_type;
        uint8_t   pscan_rep_mode;
        uint8_t   reserved;
        uint16_t  clock_offset;
        uint8_t   allow_role_switch;
} __packed;

#define BT_HCI_OP_DISCONNECT                    BT_OP(BT_OGF_LINK_CTRL, 0x0006) /* 0x0406 */
struct bt_hci_cp_disconnect {
        uint16_t handle;
        uint8_t  reason;
} __packed;

#define BT_HCI_OP_CONNECT_CANCEL                BT_OP(BT_OGF_LINK_CTRL, 0x0008) /* 0x0408 */
struct bt_hci_cp_connect_cancel {
        bt_addr_t bdaddr;
} __packed;
struct bt_hci_rp_connect_cancel {
        uint8_t   status;
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_OP_ACCEPT_CONN_REQ               BT_OP(BT_OGF_LINK_CTRL, 0x0009) /* 0x0409 */
struct bt_hci_cp_accept_conn_req {
        bt_addr_t bdaddr;
        uint8_t   role;
} __packed;

#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_CVSD        0x00
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_ULAW        0x01
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_ALAW        0x02
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_TRANSPARENT 0x03

#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_DEFAULT 0x00

#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_8_BITS  0x00
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_16_BITS 0x01

#define BT_HCI_VOICE_SETTING_DATA_FMT_1_COMPLEMENT 0x00
#define BT_HCI_VOICE_SETTING_DATA_FMT_2_COMPLEMENT 0x01
#define BT_HCI_VOICE_SETTING_DATA_FMT_SIGNED       0x02
#define BT_HCI_VOICE_SETTING_DATA_FMT_UNSIGNED     0x03

#define BT_HCI_VOICE_SETTING_CODING_FMT_LINEAR 0x00
#define BT_HCI_VOICE_SETTING_CODING_FMT_ULAW   0x01
#define BT_HCI_VOICE_SETTING_CODING_FMT_ALAW   0x02

#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_MASK GENMASK(1, 0)
#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_MASK    GENMASK(2, 4)
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_MASK    GENMASK(5, 5)
#define BT_HCI_VOICE_SETTING_DATA_FMT_MASK       GENMASK(7, 6)
#define BT_HCI_VOICE_SETTING_CODING_FMT_MASK     GENMASK(9, 8)

#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_PREP(val) \
        FIELD_PREP(BT_HCI_VOICE_SETTING_AIR_CODING_FMT_MASK, val)
#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_PREP(val) \
        FIELD_PREP(BT_HCI_VOICE_SETTING_PCM_BIT_POS_MASK, val)
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_PREP(val) \
        FIELD_PREP(BT_HCI_VOICE_SETTING_SAMPLE_SIZE_MASK, val)
#define BT_HCI_VOICE_SETTING_DATA_FMT_PREP(val) FIELD_PREP(BT_HCI_VOICE_SETTING_DATA_FMT_MASK, val)
#define BT_HCI_VOICE_SETTING_CODING_FMT_PREP(val) \
        FIELD_PREP(BT_HCI_VOICE_SETTING_CODING_FMT_MASK, val)

#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_GET(val) \
        FIELD_GET(BT_HCI_VOICE_SETTING_AIR_CODING_FMT_MASK, val)
#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_GET(val) \
        FIELD_GET(BT_HCI_VOICE_SETTING_PCM_BIT_POS_MASK, val)
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_GET(val) \
        FIELD_GET(BT_HCI_VOICE_SETTING_SAMPLE_SIZE_MASK, val)
#define BT_HCI_VOICE_SETTING_DATA_FMT_GET(val) FIELD_GET(BT_HCI_VOICE_SETTING_DATA_FMT_MASK, val)
#define BT_HCI_VOICE_SETTING_CODING_FMT_GET(val) \
        FIELD_GET(BT_HCI_VOICE_SETTING_CODING_FMT_MASK, val)

#define BT_HCI_VOICE_SETTINGS(air_coding_fmt, pcm_bit_pos, sample_size, data_fmt, coding_fmt) \
        (BT_HCI_VOICE_SETTING_AIR_CODING_FMT_PREP(air_coding_fmt) | \
         BT_HCI_VOICE_SETTING_PCM_BIT_POS_PREP(pcm_bit_pos) | \
         BT_HCI_VOICE_SETTING_SAMPLE_SIZE_PREP(sample_size) | \
         BT_HCI_VOICE_SETTING_DATA_FMT_PREP(data_fmt) | \
         BT_HCI_VOICE_SETTING_CODING_FMT_PREP(coding_fmt))

#define BT_HCI_SCO_MAX_LATENCY_DEFAULT 0xffff /* do not care about SCO link latency */

#define BT_HCI_SCO_RETRANS_EFFORT_DEFAULT 0xff /* do not care about SCO retransmission effort */

#define BT_HCI_OP_SETUP_SYNC_CONN               BT_OP(BT_OGF_LINK_CTRL, 0x0028) /* 0x0428 */
struct bt_hci_cp_setup_sync_conn {
        uint16_t  handle;
        uint32_t  tx_bandwidth;
        uint32_t  rx_bandwidth;
        uint16_t  max_latency;
        uint16_t  content_format;
        uint8_t   retrans_effort;
        uint16_t  pkt_type;
} __packed;

#define BT_HCI_OP_ACCEPT_SYNC_CONN_REQ          BT_OP(BT_OGF_LINK_CTRL, 0x0029) /* 0x0429 */
struct bt_hci_cp_accept_sync_conn_req {
        bt_addr_t bdaddr;
        uint32_t  tx_bandwidth;
        uint32_t  rx_bandwidth;
        uint16_t  max_latency;
        uint16_t  content_format;
        uint8_t   retrans_effort;
        uint16_t  pkt_type;
} __packed;

#define BT_HCI_OP_REJECT_CONN_REQ               BT_OP(BT_OGF_LINK_CTRL, 0x000a) /* 0x040a */
struct bt_hci_cp_reject_conn_req {
        bt_addr_t bdaddr;
        uint8_t   reason;
} __packed;

#define BT_HCI_OP_LINK_KEY_REPLY                BT_OP(BT_OGF_LINK_CTRL, 0x000b) /* 0x040b */
struct bt_hci_cp_link_key_reply {
        bt_addr_t bdaddr;
        uint8_t   link_key[16];
} __packed;

#define BT_HCI_OP_LINK_KEY_NEG_REPLY            BT_OP(BT_OGF_LINK_CTRL, 0x000c) /* 0x040c */
struct bt_hci_cp_link_key_neg_reply {
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_OP_PIN_CODE_REPLY                BT_OP(BT_OGF_LINK_CTRL, 0x000d) /* 0x040d */
struct bt_hci_cp_pin_code_reply {
        bt_addr_t bdaddr;
        uint8_t   pin_len;
        uint8_t   pin_code[16];
} __packed;
struct bt_hci_rp_pin_code_reply {
        uint8_t      status;
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_OP_PIN_CODE_NEG_REPLY            BT_OP(BT_OGF_LINK_CTRL, 0x000e) /* 0x040e */
struct bt_hci_cp_pin_code_neg_reply {
        bt_addr_t bdaddr;
} __packed;
struct bt_hci_rp_pin_code_neg_reply {
        uint8_t   status;
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_OP_CHANGE_CONN_PACKET_TYPE       BT_OP(BT_OGF_LINK_CTRL, 0x000f) /* 0x040f */
struct bt_hci_cp_change_conn_packet_type {
        uint16_t handle;
        uint16_t packet_type;
} __packed;

/* ACL packet type bits for HCI_Change_Connection_Packet_Type command.
 * BR packet types (set bit = may be used):
 *   See Core Spec v6.0, Vol 4, Part E, Section 7.1.14
 * EDR packet types (set bit = shall NOT be used):
 *   Note: EDR bits use reverse logic compared to BR bits.
 */
#define BT_HCI_ACL_PKT_TYPE_NO_2DH1            BIT(1)
#define BT_HCI_ACL_PKT_TYPE_NO_3DH1            BIT(2)
#define BT_HCI_ACL_PKT_TYPE_DM1                BIT(3)
#define BT_HCI_ACL_PKT_TYPE_DH1                BIT(4)
#define BT_HCI_ACL_PKT_TYPE_NO_2DH3            BIT(8)
#define BT_HCI_ACL_PKT_TYPE_NO_3DH3            BIT(9)
#define BT_HCI_ACL_PKT_TYPE_DM3                BIT(10)
#define BT_HCI_ACL_PKT_TYPE_DH3                BIT(11)
#define BT_HCI_ACL_PKT_TYPE_NO_2DH5            BIT(12)
#define BT_HCI_ACL_PKT_TYPE_NO_3DH5            BIT(13)
#define BT_HCI_ACL_PKT_TYPE_DM5                BIT(14)
#define BT_HCI_ACL_PKT_TYPE_DH5                BIT(15)

#define BT_HCI_ACL_PKT_TYPE_BR_MASK \
        (BT_HCI_ACL_PKT_TYPE_DM1 | BT_HCI_ACL_PKT_TYPE_DH1 | \
         BT_HCI_ACL_PKT_TYPE_DM3 | BT_HCI_ACL_PKT_TYPE_DH3 | \
         BT_HCI_ACL_PKT_TYPE_DM5 | BT_HCI_ACL_PKT_TYPE_DH5)

#define BT_HCI_OP_AUTH_REQUESTED                BT_OP(BT_OGF_LINK_CTRL, 0x0011) /* 0x0411 */
struct bt_hci_cp_auth_requested {
        uint16_t handle;
} __packed;

#define BT_HCI_OP_SET_CONN_ENCRYPT              BT_OP(BT_OGF_LINK_CTRL, 0x0013) /* 0x0413 */
struct bt_hci_cp_set_conn_encrypt {
        uint16_t handle;
        uint8_t  encrypt;
} __packed;

#define BT_HCI_OP_REMOTE_NAME_REQUEST           BT_OP(BT_OGF_LINK_CTRL, 0x0019) /* 0x0419 */
struct bt_hci_cp_remote_name_request {
        bt_addr_t bdaddr;
        uint8_t   pscan_rep_mode;
        uint8_t   reserved;
        uint16_t  clock_offset;
} __packed;

#define BT_HCI_OP_REMOTE_NAME_CANCEL            BT_OP(BT_OGF_LINK_CTRL, 0x001a) /* 0x041a */
struct bt_hci_cp_remote_name_cancel {
        bt_addr_t bdaddr;
} __packed;
struct bt_hci_rp_remote_name_cancel {
        uint8_t   status;
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_OP_READ_REMOTE_FEATURES          BT_OP(BT_OGF_LINK_CTRL, 0x001b) /* 0x041b */
struct bt_hci_cp_read_remote_features {
        uint16_t handle;
} __packed;

#define BT_HCI_OP_READ_REMOTE_EXT_FEATURES      BT_OP(BT_OGF_LINK_CTRL, 0x001c) /* 0x041c */
struct bt_hci_cp_read_remote_ext_features {
        uint16_t handle;
        uint8_t  page;
} __packed;

#define BT_HCI_OP_READ_REMOTE_VERSION_INFO      BT_OP(BT_OGF_LINK_CTRL, 0x001d) /* 0x041d */
struct bt_hci_cp_read_remote_version_info {
        uint16_t handle;
} __packed;

#define BT_HCI_OP_IO_CAPABILITY_REPLY           BT_OP(BT_OGF_LINK_CTRL, 0x002b) /* 0x042b */
struct bt_hci_cp_io_capability_reply {
        bt_addr_t bdaddr;
        uint8_t   capability;
        uint8_t   oob_data;
        uint8_t   authentication;
} __packed;

#define BT_HCI_OP_USER_CONFIRM_REPLY            BT_OP(BT_OGF_LINK_CTRL, 0x002c) /* 0x042c */
#define BT_HCI_OP_USER_CONFIRM_NEG_REPLY        BT_OP(BT_OGF_LINK_CTRL, 0x002d) /* 0x042d */
struct bt_hci_cp_user_confirm_reply {
        bt_addr_t bdaddr;
} __packed;
struct bt_hci_rp_user_confirm_reply {
        uint8_t   status;
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_OP_USER_PASSKEY_REPLY            BT_OP(BT_OGF_LINK_CTRL, 0x002e) /* 0x042e */
struct bt_hci_cp_user_passkey_reply {
        bt_addr_t bdaddr;
        uint32_t  passkey;
} __packed;

#define BT_HCI_OP_USER_PASSKEY_NEG_REPLY        BT_OP(BT_OGF_LINK_CTRL, 0x002f) /* 0x042f */
struct bt_hci_cp_user_passkey_neg_reply {
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_OP_IO_CAPABILITY_NEG_REPLY       BT_OP(BT_OGF_LINK_CTRL, 0x0034) /* 0x0434 */
struct bt_hci_cp_io_capability_neg_reply {
        bt_addr_t bdaddr;
        uint8_t   reason;
} __packed;

#define BT_HCI_OP_SWITCH_ROLE                   BT_OP(BT_OGF_LINK_POLICY, 0x000b)
struct bt_hci_cp_switch_role {
        bt_addr_t bdaddr;
        uint8_t   role;
} __packed;

#define BT_HCI_LINK_POLICY_SETTINGS_ENABLE_ROLE_SWITCH  BIT(0)
#define BT_HCI_LINK_POLICY_SETTINGS_ENABLE_HOLD_MODE    BIT(1)
#define BT_HCI_LINK_POLICY_SETTINGS_ENABLE_SNIFF_SWITCH BIT(2)

#define BT_HCI_OP_READ_LINK_POLICY_SETTINGS     BT_OP(BT_OGF_LINK_POLICY, 0x000c)
struct bt_hci_cp_read_link_policy_settings {
        uint16_t handle;
} __packed;
struct bt_hci_rp_read_link_policy_settings {
        uint8_t  status;
        uint16_t handle;
        uint16_t link_policy_settings;
} __packed;

#define BT_HCI_OP_WRITE_LINK_POLICY_SETTINGS    BT_OP(BT_OGF_LINK_POLICY, 0x000d)
struct bt_hci_cp_write_link_policy_settings {
        uint16_t handle;
        uint16_t link_policy_settings;
} __packed;

#define BT_HCI_OP_READ_DEFAULT_LINK_POLICY_SETTINGS  BT_OP(BT_OGF_LINK_POLICY, 0x000e)
struct bt_hci_rp_read_default_link_policy_settings {
        uint8_t  status;
        uint16_t default_link_policy_settings;
} __packed;

#define BT_HCI_OP_WRITE_DEFAULT_LINK_POLICY_SETTINGS BT_OP(BT_OGF_LINK_POLICY, 0x000f)
struct bt_hci_cp_write_default_link_policy_settings {
        uint16_t default_link_policy_settings;
} __packed;

#define BT_HCI_OP_SNIFF_MODE                    BT_OP(BT_OGF_LINK_POLICY, 0x0003) /* 0x0803 */
struct bt_hci_cp_sniff_mode {
        uint16_t handle;
        uint16_t max_interval;
        uint16_t min_interval;
        uint16_t attempt;
        uint16_t timeout;
} __packed;

#define BT_HCI_OP_EXIT_SNIFF_MODE               BT_OP(BT_OGF_LINK_POLICY, 0x0004) /* 0x0804 */
struct bt_hci_cp_exit_sniff_mode {
        uint16_t handle;
} __packed;

#define BT_HCI_OP_SNIFF_SUBRATING              BT_OP(BT_OGF_LINK_POLICY, 0x0011) /* 0x0811 */
struct bt_hci_cp_sniff_subrating {
        uint16_t handle;
        uint16_t max_latency;
        uint16_t min_remote_timeout;
        uint16_t min_local_timeout;
} __packed;

struct bt_hci_rp_sniff_subrating {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_SET_EVENT_MASK                BT_OP(BT_OGF_BASEBAND, 0x0001) /* 0x0c01 */
struct bt_hci_cp_set_event_mask {
        uint8_t  events[8];
} __packed;

#define BT_HCI_OP_RESET                         BT_OP(BT_OGF_BASEBAND, 0x0003) /* 0x0c03 */

#define BT_HCI_OP_WRITE_LOCAL_NAME              BT_OP(BT_OGF_BASEBAND, 0x0013) /* 0x0c13 */
struct bt_hci_write_local_name {
        uint8_t local_name[248];
} __packed;

#define BT_HCI_OP_READ_CONN_ACCEPT_TIMEOUT      BT_OP(BT_OGF_BASEBAND, 0x0015) /* 0x0c15 */
struct bt_hci_rp_read_conn_accept_timeout {
        uint8_t  status;
        uint16_t conn_accept_timeout;
} __packed;

#define BT_HCI_OP_WRITE_CONN_ACCEPT_TIMEOUT     BT_OP(BT_OGF_BASEBAND, 0x0016) /* 0x0c16 */
struct bt_hci_cp_write_conn_accept_timeout {
        uint16_t conn_accept_timeout;
} __packed;

struct bt_hci_rp_write_conn_accept_timeout {
        uint8_t  status;
} __packed;

#define BT_HCI_OP_WRITE_PAGE_TIMEOUT            BT_OP(BT_OGF_BASEBAND, 0x0018) /* 0x0c18 */

#define BT_HCI_OP_WRITE_SCAN_ENABLE             BT_OP(BT_OGF_BASEBAND, 0x001a) /* 0x0c1a */
#define BT_BREDR_SCAN_DISABLED                  0x00
#define BT_BREDR_SCAN_INQUIRY                   0x01
#define BT_BREDR_SCAN_PAGE                      0x02

#define BT_HCI_OP_WRITE_PAGE_SCAN_ACTIVITY      BT_OP(BT_OGF_BASEBAND, 0x001c) /* 0x0c1c */
struct bt_hci_cp_write_page_scan_activity {
        uint16_t interval;
        uint16_t window;
} __packed;

#define BT_HCI_OP_WRITE_INQUIRY_SCAN_ACTIVITY   BT_OP(BT_OGF_BASEBAND, 0x001e) /* 0x0c1e */
struct bt_hci_cp_write_inquiry_scan_activity {
        uint16_t interval;
        uint16_t window;
} __packed;

#define BT_HCI_OP_READ_CLASS_OF_DEVICE          BT_OP(BT_OGF_BASEBAND, 0x0023) /* 0x0c23 */
struct bt_hci_rp_read_class_of_device {
        uint8_t  status;
        uint8_t  class_of_device[3];
} __packed;

#define BT_HCI_OP_WRITE_CLASS_OF_DEVICE         BT_OP(BT_OGF_BASEBAND, 0x0024) /* 0x0c24 */
struct bt_hci_cp_write_class_of_device {
        uint8_t  class_of_device[3];
} __packed;

#define BT_TX_POWER_LEVEL_CURRENT               0x00
#define BT_TX_POWER_LEVEL_MAX                   0x01
#define BT_HCI_OP_READ_TX_POWER_LEVEL           BT_OP(BT_OGF_BASEBAND, 0x002d) /* 0x0c2d */
struct bt_hci_cp_read_tx_power_level {
        uint16_t handle;
        uint8_t  type;
} __packed;

struct bt_hci_rp_read_tx_power_level {
        uint8_t  status;
        uint16_t handle;
        int8_t   tx_power_level;
} __packed;

#define BT_HCI_LE_TX_POWER_PHY_1M               0x01
#define BT_HCI_LE_TX_POWER_PHY_2M               0x02
#define BT_HCI_LE_TX_POWER_PHY_CODED_S8         0x03
#define BT_HCI_LE_TX_POWER_PHY_CODED_S2         0x04
#define BT_HCI_OP_LE_ENH_READ_TX_POWER_LEVEL    BT_OP(BT_OGF_LE, 0x0076) /* 0x2076 */
struct bt_hci_cp_le_read_tx_power_level {
        uint16_t handle;
        uint8_t  phy;
} __packed;

struct bt_hci_rp_le_read_tx_power_level {
        uint8_t  status;
        uint16_t handle;
        uint8_t  phy;
        int8_t   current_tx_power_level;
        int8_t   max_tx_power_level;
} __packed;

#define BT_HCI_OP_LE_READ_REMOTE_TX_POWER_LEVEL BT_OP(BT_OGF_LE, 0x0077) /* 0x2077 */

#define BT_HCI_LE_TX_POWER_REPORT_DISABLE       0x00
#define BT_HCI_LE_TX_POWER_REPORT_ENABLE        0x01
#define BT_HCI_OP_LE_SET_TX_POWER_REPORT_ENABLE BT_OP(BT_OGF_LE, 0x007A) /* 0x207A */
struct bt_hci_cp_le_set_tx_power_report_enable {
        uint16_t handle;
        uint8_t  local_enable;
        uint8_t  remote_enable;
} __packed;

#define BT_HCI_OP_LE_SET_PATH_LOSS_REPORTING_PARAMETERS BT_OP(BT_OGF_LE, 0x0078) /* 0x2078 */
struct bt_hci_cp_le_set_path_loss_reporting_parameters {
        uint16_t handle;
        uint8_t  high_threshold;
        uint8_t  high_hysteresis;
        uint8_t  low_threshold;
        uint8_t  low_hysteresis;
        uint16_t min_time_spent;
} __packed;

struct bt_hci_rp_le_set_path_loss_reporting_parameters {
        uint16_t handle;
        uint8_t  status;
} __packed;


#define BT_HCI_LE_PATH_LOSS_REPORTING_DISABLE       0x00
#define BT_HCI_LE_PATH_LOSS_REPORTING_ENABLE        0x01
#define BT_HCI_OP_LE_SET_PATH_LOSS_REPORTING_ENABLE BT_OP(BT_OGF_LE, 0x0079) /* 0x2079 */

struct bt_hci_cp_le_set_path_loss_reporting_enable {
        uint16_t handle;
        uint8_t  enable;
} __packed;

struct bt_hci_rp_le_set_path_loss_reporting_enable {
        uint16_t handle;
        uint8_t  status;
} __packed;

#define BT_HCI_OP_LE_SET_DEFAULT_SUBRATE BT_OP(BT_OGF_LE, 0x007D) /* 0x207D */

struct bt_hci_cp_le_set_default_subrate {
        uint16_t subrate_min;
        uint16_t subrate_max;
        uint16_t max_latency;
        uint16_t continuation_number;
        uint16_t supervision_timeout;
} __packed;

#define BT_HCI_OP_LE_SUBRATE_REQUEST     BT_OP(BT_OGF_LE, 0x007E) /* 0x207E */

struct bt_hci_cp_le_subrate_request {
        uint16_t handle;
        uint16_t subrate_min;
        uint16_t subrate_max;
        uint16_t max_latency;
        uint16_t continuation_number;
        uint16_t supervision_timeout;
} __packed;

#define BT_HCI_CTL_TO_HOST_FLOW_DISABLE         0x00
#define BT_HCI_CTL_TO_HOST_FLOW_ENABLE          0x01
#define BT_HCI_OP_SET_CTL_TO_HOST_FLOW          BT_OP(BT_OGF_BASEBAND, 0x0031) /* 0x0c31 */
struct bt_hci_cp_set_ctl_to_host_flow {
        uint8_t  flow_enable;
} __packed;

#define BT_HCI_OP_HOST_BUFFER_SIZE              BT_OP(BT_OGF_BASEBAND, 0x0033) /* 0x0c33 */
struct bt_hci_cp_host_buffer_size {
        uint16_t acl_mtu;
        uint8_t  sco_mtu;
        uint16_t acl_pkts;
        uint16_t sco_pkts;
} __packed;

struct bt_hci_handle_count {
        uint16_t handle;
        uint16_t count;
} __packed;

#define BT_HCI_OP_HOST_NUM_COMPLETED_PACKETS    BT_OP(BT_OGF_BASEBAND, 0x0035) /* 0x0c35 */
struct bt_hci_cp_host_num_completed_packets {
        uint8_t  num_handles;
        struct bt_hci_handle_count h[0];
} __packed;

#define BT_HCI_OP_READ_LINK_SUPERVISION_TIMEOUT     BT_OP(BT_OGF_BASEBAND, 0x0036) /* 0x0c36 */
struct bt_hci_cp_read_link_supervision_timeout {
        uint16_t handle;
} __packed;

struct bt_hci_rp_read_link_supervision_timeout {
        uint8_t  status;
        uint16_t handle;
        uint16_t timeout;
} __packed;

#define BT_HCI_OP_WRITE_LINK_SUPERVISION_TIMEOUT    BT_OP(BT_OGF_BASEBAND, 0x0037) /* 0x0c37 */
struct bt_hci_cp_write_link_supervision_timeout {
        uint16_t handle;
        uint16_t timeout;
} __packed;

#define BT_HCI_OP_WRITE_CURRENT_IAC_LAP         BT_OP(BT_OGF_BASEBAND, 0x003a) /* 0x0c3a */
struct bt_hci_iac_lap {
        uint8_t iac[3];
} __packed;

struct bt_hci_cp_write_current_iac_lap {
        uint8_t  num_current_iac;
        struct bt_hci_iac_lap lap[0];
} __packed;

#define BT_HCI_OP_WRITE_INQUIRY_SCAN_TYPE       BT_OP(BT_OGF_BASEBAND, 0x0043) /* 0x0c43 */
struct bt_hci_cp_write_inquiry_scan_type {
        uint8_t type;
} __packed;

#define BT_HCI_OP_WRITE_INQUIRY_MODE            BT_OP(BT_OGF_BASEBAND, 0x0045) /* 0x0c45 */
struct bt_hci_cp_write_inquiry_mode {
        uint8_t  mode;
} __packed;

#define BT_HCI_OP_WRITE_PAGE_SCAN_TYPE          BT_OP(BT_OGF_BASEBAND, 0x0047) /* 0x0c47 */
struct bt_hci_cp_write_page_scan_type {
        uint8_t type;
} __packed;

#define BT_HCI_EIR_MAX_DATA_LEN                 240
#define BT_HCI_OP_WRITE_EXT_INQUIRY_RESPONSE    BT_OP(BT_OGF_BASEBAND, 0x0052) /* 0x0c52 */
struct bt_hci_cp_write_ext_inquiry_response {
        uint8_t fec_required;
        uint8_t eir[BT_HCI_EIR_MAX_DATA_LEN];
} __packed;

#define BT_HCI_OP_WRITE_SSP_MODE                BT_OP(BT_OGF_BASEBAND, 0x0056) /* 0x0c56 */
struct bt_hci_cp_write_ssp_mode {
        uint8_t mode;
} __packed;

#define BT_HCI_OP_SET_EVENT_MASK_PAGE_2         BT_OP(BT_OGF_BASEBAND, 0x0063) /* 0x0c63 */
struct bt_hci_cp_set_event_mask_page_2 {
        uint8_t  events_page_2[8];
} __packed;

#define BT_HCI_OP_LE_WRITE_LE_HOST_SUPP         BT_OP(BT_OGF_BASEBAND, 0x006d) /* 0x0c6d */
struct bt_hci_cp_write_le_host_supp {
        uint8_t  le;
        uint8_t  simul;
} __packed;

#define BT_HCI_OP_WRITE_SC_HOST_SUPP            BT_OP(BT_OGF_BASEBAND, 0x007a) /* 0x0c7a */
struct bt_hci_cp_write_sc_host_supp {
        uint8_t  sc_support;
} __packed;

#define BT_HCI_OP_READ_AUTH_PAYLOAD_TIMEOUT     BT_OP(BT_OGF_BASEBAND, 0x007b) /* 0x0c7b */
struct bt_hci_cp_read_auth_payload_timeout {
        uint16_t handle;
} __packed;

struct bt_hci_rp_read_auth_payload_timeout {
        uint8_t  status;
        uint16_t handle;
        uint16_t auth_payload_timeout;
} __packed;

#define BT_HCI_OP_WRITE_AUTH_PAYLOAD_TIMEOUT    BT_OP(BT_OGF_BASEBAND, 0x007c) /* 0x0c7c */
struct bt_hci_cp_write_auth_payload_timeout {
        uint16_t handle;
        uint16_t auth_payload_timeout;
} __packed;

struct bt_hci_rp_write_auth_payload_timeout {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_CONFIGURE_DATA_PATH           BT_OP(BT_OGF_BASEBAND, 0x0083) /* 0x0c83 */
struct bt_hci_cp_configure_data_path {
        uint8_t  data_path_dir;
        uint8_t  data_path_id;
        uint8_t  vs_config_len;
        uint8_t  vs_config[0];
} __packed;

struct bt_hci_rp_configure_data_path {
        uint8_t  status;
} __packed;

/* HCI version from Assigned Numbers */
#define BT_HCI_VERSION_1_0B                     0
#define BT_HCI_VERSION_1_1                      1
#define BT_HCI_VERSION_1_2                      2
#define BT_HCI_VERSION_2_0                      3
#define BT_HCI_VERSION_2_1                      4
#define BT_HCI_VERSION_3_0                      5
#define BT_HCI_VERSION_4_0                      6
#define BT_HCI_VERSION_4_1                      7
#define BT_HCI_VERSION_4_2                      8
#define BT_HCI_VERSION_5_0                      9
#define BT_HCI_VERSION_5_1                      10
#define BT_HCI_VERSION_5_2                      11
#define BT_HCI_VERSION_5_3                      12
#define BT_HCI_VERSION_5_4                      13
#define BT_HCI_VERSION_6_0                      14
#define BT_HCI_VERSION_6_1                      15
#define BT_HCI_VERSION_6_2                      16
#define BT_HCI_VERSION_6_3                      17

#define BT_HCI_OP_READ_LOCAL_VERSION_INFO       BT_OP(BT_OGF_INFO, 0x0001) /* 0x1001 */
struct bt_hci_rp_read_local_version_info {
        uint8_t  status;
        uint8_t  hci_version;
        uint16_t hci_revision;
        uint8_t  lmp_version;
        uint16_t manufacturer;
        uint16_t lmp_subversion;
} __packed;

#define BT_HCI_OP_READ_SUPPORTED_COMMANDS       BT_OP(BT_OGF_INFO, 0x0002) /* 0x1002 */
struct bt_hci_rp_read_supported_commands {
        uint8_t  status;
        uint8_t  commands[64];
} __packed;

#define BT_HCI_OP_READ_LOCAL_EXT_FEATURES       BT_OP(BT_OGF_INFO, 0x0004) /* 0x1004 */
struct bt_hci_cp_read_local_ext_features {
        uint8_t page;
};
struct bt_hci_rp_read_local_ext_features {
        uint8_t  status;
        uint8_t  page;
        uint8_t  max_page;
        uint8_t  ext_features[8];
} __packed;

#define BT_HCI_OP_READ_LOCAL_FEATURES           BT_OP(BT_OGF_INFO, 0x0003) /* 0x1003 */
struct bt_hci_rp_read_local_features {
        uint8_t  status;
        uint8_t  features[8];
} __packed;

#define BT_HCI_OP_READ_BUFFER_SIZE              BT_OP(BT_OGF_INFO, 0x0005) /* 0x1005 */
struct bt_hci_rp_read_buffer_size {
        uint8_t  status;
        uint16_t acl_max_len;
        uint8_t  sco_max_len;
        uint16_t acl_max_num;
        uint16_t sco_max_num;
} __packed;

#define BT_HCI_OP_READ_BD_ADDR                  BT_OP(BT_OGF_INFO, 0x0009) /* 0x1009 */
struct bt_hci_rp_read_bd_addr {
        uint8_t   status;
        bt_addr_t bdaddr;
} __packed;

/* logic transport type bits as returned when reading supported codecs */
#define BT_HCI_CODEC_TRANSPORT_MASK_BREDR_ACL BIT(0)
#define BT_HCI_CODEC_TRANSPORT_MASK_BREDR_SCO BIT(1)
#define BT_HCI_CODEC_TRANSPORT_MASK_LE_CIS    BIT(2)
#define BT_HCI_CODEC_TRANSPORT_MASK_LE_BIS    BIT(3)

/* logic transport types for reading codec capabilities and controller delays */
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_BREDR_ACL 0x00
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_BREDR_SCO 0x01
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_LE_CIS    0x02
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_LE_BIS    0x03

/* audio datapath directions */
#define BT_HCI_DATAPATH_DIR_HOST_TO_CTLR 0x00
#define BT_HCI_DATAPATH_DIR_CTLR_TO_HOST 0x01

/* audio datapath IDs */
#define BT_HCI_DATAPATH_ID_HCI      0x00
#define BT_HCI_DATAPATH_ID_VS       0x01
#define BT_HCI_DATAPATH_ID_VS_END   0xfe

/* coding format assigned numbers, used for codec IDs */
#define BT_HCI_CODING_FORMAT_ULAW_LOG    0x00
#define BT_HCI_CODING_FORMAT_ALAW_LOG    0x01
#define BT_HCI_CODING_FORMAT_CVSD        0x02
#define BT_HCI_CODING_FORMAT_TRANSPARENT 0x03
#define BT_HCI_CODING_FORMAT_LINEAR_PCM  0x04
#define BT_HCI_CODING_FORMAT_MSBC        0x05
#define BT_HCI_CODING_FORMAT_LC3         0x06
#define BT_HCI_CODING_FORMAT_G729A       0x07
#define BT_HCI_CODING_FORMAT_VS          0xFF


#define BT_HCI_OP_READ_CODECS                   BT_OP(BT_OGF_INFO, 0x000b) /* 0x100b */
struct bt_hci_std_codec_info {
        uint8_t codec_id;
} __packed;
struct bt_hci_std_codecs {
        uint8_t num_codecs;
        struct bt_hci_std_codec_info codec_info[0];
} __packed;
struct bt_hci_vs_codec_info {
        uint16_t company_id;
        uint16_t codec_id;
} __packed;
struct bt_hci_vs_codecs {
        uint8_t num_codecs;
        struct bt_hci_vs_codec_info codec_info[0];
} __packed;
struct bt_hci_rp_read_codecs {
        uint8_t status;
        /* other fields filled in dynamically */
        uint8_t codecs[0];
} __packed;

#define BT_HCI_OP_READ_CODECS_V2                BT_OP(BT_OGF_INFO, 0x000d) /* 0x100d */
struct bt_hci_std_codec_info_v2 {
        uint8_t codec_id;
        uint8_t transports; /* bitmap */
} __packed;
struct bt_hci_std_codecs_v2 {
        uint8_t num_codecs;
        struct bt_hci_std_codec_info_v2 codec_info[0];
} __packed;
struct bt_hci_vs_codec_info_v2 {
        uint16_t company_id;
        uint16_t codec_id;
        uint8_t transports; /* bitmap */
} __packed;
struct bt_hci_vs_codecs_v2 {
        uint8_t num_codecs;
        struct bt_hci_vs_codec_info_v2 codec_info[0];
} __packed;
struct bt_hci_rp_read_codecs_v2 {
        uint8_t status;
        /* other fields filled in dynamically */
        uint8_t codecs[0];
} __packed;

struct bt_hci_cp_codec_id {
        uint8_t coding_format;
        uint16_t company_id;
        uint16_t vs_codec_id;
} __packed;

#define BT_HCI_OP_READ_CODEC_CAPABILITIES       BT_OP(BT_OGF_INFO, 0x000e) /* 0x100e */
struct bt_hci_cp_read_codec_capabilities {
        struct bt_hci_cp_codec_id codec_id;
        uint8_t transport;
        uint8_t direction;
} __packed;
struct bt_hci_codec_capability_info {
        uint8_t length;
        uint8_t data[0];
} __packed;
struct bt_hci_rp_read_codec_capabilities {
        uint8_t status;
        uint8_t num_capabilities;
        /* other fields filled in dynamically */
        uint8_t capabilities[0];
} __packed;

#define BT_HCI_OP_READ_CTLR_DELAY               BT_OP(BT_OGF_INFO, 0x000f) /* 0x100f */
struct bt_hci_cp_read_ctlr_delay {
        struct bt_hci_cp_codec_id codec_id;
        uint8_t transport;
        uint8_t direction;
        uint8_t codec_config_len;
        uint8_t codec_config[0];
} __packed;
struct bt_hci_rp_read_ctlr_delay {
        uint8_t status;
        uint8_t min_ctlr_delay[3];
        uint8_t max_ctlr_delay[3];
} __packed;

#define BT_HCI_OP_READ_RSSI                     BT_OP(BT_OGF_STATUS, 0x0005) /* 0x1405 */
struct bt_hci_cp_read_rssi {
        uint16_t handle;
} __packed;
struct bt_hci_rp_read_rssi {
        uint8_t  status;
        uint16_t handle;
        int8_t   rssi;
} __packed;

#define BT_HCI_ENCRYPTION_KEY_SIZE_MIN          7
#define BT_HCI_ENCRYPTION_KEY_SIZE_MAX          16

#define BT_HCI_OP_READ_ENCRYPTION_KEY_SIZE      BT_OP(BT_OGF_STATUS, 0x0008) /* 0x1408 */
struct bt_hci_cp_read_encryption_key_size {
        uint16_t handle;
} __packed;
struct bt_hci_rp_read_encryption_key_size {
        uint8_t  status;
        uint16_t handle;
        uint8_t  key_size;
} __packed;

/* Bluetooth LE */

#define BT_HCI_OP_LE_SET_EVENT_MASK             BT_OP(BT_OGF_LE, 0x0001) /* 0x2001 */
struct bt_hci_cp_le_set_event_mask {
        uint8_t events[8];
} __packed;

#define BT_HCI_OP_LE_READ_BUFFER_SIZE           BT_OP(BT_OGF_LE, 0x0002) /* 0x2002 */
struct bt_hci_rp_le_read_buffer_size {
        uint8_t  status;
        uint16_t le_max_len;
        uint8_t  le_max_num;
} __packed;

#define BT_HCI_OP_LE_READ_LOCAL_FEATURES        BT_OP(BT_OGF_LE, 0x0003) /* 0x2003 */
struct bt_hci_rp_le_read_local_features {
        uint8_t  status;
        uint8_t  features[8];
} __packed;

#define BT_HCI_OP_LE_SET_RANDOM_ADDRESS         BT_OP(BT_OGF_LE, 0x0005) /* 0x2005 */
struct bt_hci_cp_le_set_random_address {
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_ADV_IND                          0x00
#define BT_HCI_ADV_DIRECT_IND                   0x01
#define BT_HCI_ADV_SCAN_IND                     0x02
#define BT_HCI_ADV_NONCONN_IND                  0x03
#define BT_HCI_ADV_DIRECT_IND_LOW_DUTY          0x04
#define BT_HCI_ADV_SCAN_RSP                     0x04

#define BT_LE_ADV_INTERVAL_MIN                  0x0020
#define BT_LE_ADV_INTERVAL_MAX                  0x4000
#define BT_LE_EXT_ADV_INTERVAL_MAX              0xFFFFFFU
#define BT_LE_ADV_INTERVAL_DEFAULT              0x0800

#define BT_LE_ADV_CHAN_MAP_CHAN_37              0x01
#define BT_LE_ADV_CHAN_MAP_CHAN_38              0x02
#define BT_LE_ADV_CHAN_MAP_CHAN_39              0x04
#define BT_LE_ADV_CHAN_MAP_ALL                  0x07

#define BT_LE_ADV_FP_NO_FILTER                  0x00
#define BT_LE_ADV_FP_FILTER_SCAN_REQ            0x01
#define BT_LE_ADV_FP_FILTER_CONN_IND            0x02
#define BT_LE_ADV_FP_FILTER_BOTH                0x03

#define BT_HCI_OP_LE_SET_ADV_PARAM              BT_OP(BT_OGF_LE, 0x0006) /* 0x2006 */
struct bt_hci_cp_le_set_adv_param {
        uint16_t     min_interval;
        uint16_t     max_interval;
        uint8_t      type;
        uint8_t      own_addr_type;
        bt_addr_le_t direct_addr;
        uint8_t      channel_map;
        uint8_t      filter_policy;
} __packed;

#define BT_HCI_OP_LE_READ_ADV_CHAN_TX_POWER     BT_OP(BT_OGF_LE, 0x0007) /* 0x2007 */
struct bt_hci_rp_le_read_chan_tx_power {
        uint8_t status;
        int8_t  tx_power_level;
} __packed;

#define BT_HCI_OP_LE_SET_ADV_DATA               BT_OP(BT_OGF_LE, 0x0008) /* 0x2008 */
struct bt_hci_cp_le_set_adv_data {
        uint8_t  len;
        uint8_t  data[31];
} __packed;

#define BT_HCI_OP_LE_SET_SCAN_RSP_DATA          BT_OP(BT_OGF_LE, 0x0009) /* 0x2009 */
struct bt_hci_cp_le_set_scan_rsp_data {
        uint8_t  len;
        uint8_t  data[31];
} __packed;

#define BT_HCI_LE_ADV_DISABLE                   0x00
#define BT_HCI_LE_ADV_ENABLE                    0x01

#define BT_HCI_OP_LE_SET_ADV_ENABLE             BT_OP(BT_OGF_LE, 0x000a) /* 0x200a */
struct bt_hci_cp_le_set_adv_enable {
        uint8_t  enable;
} __packed;

/* Scan types */
#define BT_HCI_OP_LE_SET_SCAN_PARAM             BT_OP(BT_OGF_LE, 0x000b) /* 0x200b */
#define BT_HCI_LE_SCAN_PASSIVE                  0x00
#define BT_HCI_LE_SCAN_ACTIVE                   0x01

#define BT_HCI_LE_SCAN_FP_BASIC_NO_FILTER       0x00
#define BT_HCI_LE_SCAN_FP_BASIC_FILTER          0x01
#define BT_HCI_LE_SCAN_FP_EXT_NO_FILTER         0x02
#define BT_HCI_LE_SCAN_FP_EXT_FILTER            0x03

struct bt_hci_cp_le_set_scan_param {
        uint8_t  scan_type;
        uint16_t interval;
        uint16_t window;
        uint8_t  addr_type;
        uint8_t  filter_policy;
} __packed;

#define BT_HCI_OP_LE_SET_SCAN_ENABLE            BT_OP(BT_OGF_LE, 0x000c) /* 0x200c */

#define BT_HCI_LE_SCAN_DISABLE                  0x00
#define BT_HCI_LE_SCAN_ENABLE                   0x01

#define BT_HCI_LE_SCAN_FILTER_DUP_DISABLE       0x00
#define BT_HCI_LE_SCAN_FILTER_DUP_ENABLE        0x01

struct bt_hci_cp_le_set_scan_enable {
        uint8_t  enable;
        uint8_t  filter_dup;
} __packed;

#define BT_HCI_OP_LE_CREATE_CONN                BT_OP(BT_OGF_LE, 0x000d) /* 0x200d */

#define BT_HCI_LE_CREATE_CONN_FP_NO_FILTER      0x00
#define BT_HCI_LE_CREATE_CONN_FP_FILTER         0x01

struct bt_hci_cp_le_create_conn {
        uint16_t     scan_interval;
        uint16_t     scan_window;
        uint8_t      filter_policy;
        bt_addr_le_t peer_addr;
        uint8_t      own_addr_type;
        uint16_t     conn_interval_min;
        uint16_t     conn_interval_max;
        uint16_t     conn_latency;
        uint16_t     supervision_timeout;
        uint16_t     min_ce_len;
        uint16_t     max_ce_len;
} __packed;

#define BT_HCI_OP_LE_CREATE_CONN_CANCEL         BT_OP(BT_OGF_LE, 0x000e) /* 0x200e */

#define BT_HCI_OP_LE_READ_FAL_SIZE               BT_OP(BT_OGF_LE, 0x000f) /* 0x200f */
struct bt_hci_rp_le_read_fal_size {
        uint8_t  status;
        uint8_t  fal_size;
} __packed;

#define BT_HCI_OP_LE_CLEAR_FAL                   BT_OP(BT_OGF_LE, 0x0010) /* 0x2010 */

#define BT_HCI_OP_LE_ADD_DEV_TO_FAL              BT_OP(BT_OGF_LE, 0x0011) /* 0x2011 */
struct bt_hci_cp_le_add_dev_to_fal {
        bt_addr_le_t  addr;
} __packed;

#define BT_HCI_OP_LE_REM_DEV_FROM_FAL            BT_OP(BT_OGF_LE, 0x0012) /* 0x2012 */
struct bt_hci_cp_le_rem_dev_from_fal {
        bt_addr_le_t  addr;
} __packed;

#define BT_HCI_OP_LE_CONN_UPDATE                BT_OP(BT_OGF_LE, 0x0013) /* 0x2013 */
struct hci_cp_le_conn_update {
        uint16_t handle;
        uint16_t conn_interval_min;
        uint16_t conn_interval_max;
        uint16_t conn_latency;
        uint16_t supervision_timeout;
        uint16_t min_ce_len;
        uint16_t max_ce_len;
} __packed;

#define BT_HCI_OP_LE_SET_HOST_CHAN_CLASSIF      BT_OP(BT_OGF_LE, 0x0014) /* 0x2014 */
struct bt_hci_cp_le_set_host_chan_classif {
        uint8_t  ch_map[5];
} __packed;

#define BT_HCI_OP_LE_READ_CHAN_MAP              BT_OP(BT_OGF_LE, 0x0015) /* 0x2015 */
struct bt_hci_cp_le_read_chan_map {
        uint16_t handle;
} __packed;
struct bt_hci_rp_le_read_chan_map {
        uint8_t  status;
        uint16_t handle;
        uint8_t  ch_map[5];
} __packed;

#define BT_HCI_OP_LE_READ_REMOTE_FEATURES       BT_OP(BT_OGF_LE, 0x0016) /* 0x2016 */
struct bt_hci_cp_le_read_remote_features {
        uint16_t  handle;
} __packed;

#define BT_HCI_OP_LE_ENCRYPT                    BT_OP(BT_OGF_LE, 0x0017) /* 0x2017 */
struct bt_hci_cp_le_encrypt {
        uint8_t  key[16];
        uint8_t  plaintext[16];
} __packed;
struct bt_hci_rp_le_encrypt {
        uint8_t  status;
        uint8_t  enc_data[16];
} __packed;

#define BT_HCI_OP_LE_RAND                       BT_OP(BT_OGF_LE, 0x0018) /* 0x2018 */
struct bt_hci_rp_le_rand {
        uint8_t  status;
        uint8_t  rand[8];
} __packed;

#define BT_HCI_OP_LE_START_ENCRYPTION           BT_OP(BT_OGF_LE, 0x0019) /* 0x2019 */
struct bt_hci_cp_le_start_encryption {
        uint16_t handle;
        uint8_t  rand[8];
        uint8_t  ediv[2];
        uint8_t  ltk[16];
} __packed;

#define BT_HCI_OP_LE_LTK_REQ_REPLY              BT_OP(BT_OGF_LE, 0x001a) /* 0x201a */
struct bt_hci_cp_le_ltk_req_reply {
        uint16_t handle;
        uint8_t  ltk[16];
} __packed;
struct bt_hci_rp_le_ltk_req_reply {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_LTK_REQ_NEG_REPLY          BT_OP(BT_OGF_LE, 0x001b) /* 0x201b */
struct bt_hci_cp_le_ltk_req_neg_reply {
        uint16_t handle;
} __packed;
struct bt_hci_rp_le_ltk_req_neg_reply {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_READ_SUPP_STATES           BT_OP(BT_OGF_LE, 0x001c) /* 0x201c */
struct bt_hci_rp_le_read_supp_states {
        uint8_t  status;
        uint8_t  le_states[8];
} __packed;

#define BT_HCI_OP_LE_RX_TEST                    BT_OP(BT_OGF_LE, 0x001d) /* 0x201d */
struct bt_hci_cp_le_rx_test {
        uint8_t  rx_ch;
} __packed;

#define BT_HCI_TEST_PKT_PAYLOAD_PRBS9           0x00
#define BT_HCI_TEST_PKT_PAYLOAD_11110000        0x01
#define BT_HCI_TEST_PKT_PAYLOAD_10101010        0x02
#define BT_HCI_TEST_PKT_PAYLOAD_PRBS15          0x03
#define BT_HCI_TEST_PKT_PAYLOAD_11111111        0x04
#define BT_HCI_TEST_PKT_PAYLOAD_00000000        0x05
#define BT_HCI_TEST_PKT_PAYLOAD_00001111        0x06
#define BT_HCI_TEST_PKT_PAYLOAD_01010101        0x07

#define BT_HCI_OP_LE_TX_TEST                    BT_OP(BT_OGF_LE, 0x001e) /* 0x201e */
struct bt_hci_cp_le_tx_test {
        uint8_t  tx_ch;
        uint8_t  test_data_len;
        uint8_t  pkt_payload;
} __packed;

#define BT_HCI_OP_LE_TEST_END                   BT_OP(BT_OGF_LE, 0x001f) /* 0x201f */
struct bt_hci_rp_le_test_end {
        uint8_t  status;
        uint16_t rx_pkt_count;
} __packed;

#define BT_HCI_OP_LE_CONN_PARAM_REQ_REPLY       BT_OP(BT_OGF_LE, 0x0020) /* 0x2020 */
struct bt_hci_cp_le_conn_param_req_reply {
        uint16_t handle;
        uint16_t interval_min;
        uint16_t interval_max;
        uint16_t latency;
        uint16_t timeout;
        uint16_t min_ce_len;
        uint16_t max_ce_len;
} __packed;
struct bt_hci_rp_le_conn_param_req_reply {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_CONN_PARAM_REQ_NEG_REPLY   BT_OP(BT_OGF_LE, 0x0021) /* 0x2021 */
struct bt_hci_cp_le_conn_param_req_neg_reply {
        uint16_t handle;
        uint8_t  reason;
} __packed;
struct bt_hci_rp_le_conn_param_req_neg_reply {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_SET_DATA_LEN               BT_OP(BT_OGF_LE, 0x0022) /* 0x2022 */
struct bt_hci_cp_le_set_data_len {
        uint16_t handle;
        uint16_t tx_octets;
        uint16_t tx_time;
} __packed;
struct bt_hci_rp_le_set_data_len {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_READ_DEFAULT_DATA_LEN      BT_OP(BT_OGF_LE, 0x0023) /* 0x2023 */
struct bt_hci_rp_le_read_default_data_len {
        uint8_t  status;
        uint16_t max_tx_octets;
        uint16_t max_tx_time;
} __packed;

#define BT_HCI_OP_LE_WRITE_DEFAULT_DATA_LEN     BT_OP(BT_OGF_LE, 0x0024) /* 0x2024 */
struct bt_hci_cp_le_write_default_data_len {
        uint16_t max_tx_octets;
        uint16_t max_tx_time;
} __packed;

#define BT_HCI_OP_LE_P256_PUBLIC_KEY            BT_OP(BT_OGF_LE, 0x0025) /* 0x2025 */

#define BT_HCI_OP_LE_GENERATE_DHKEY             BT_OP(BT_OGF_LE, 0x0026) /* 0x2026 */
struct bt_hci_cp_le_generate_dhkey {
        uint8_t key[64];
} __packed;


#define BT_HCI_OP_LE_GENERATE_DHKEY_V2          BT_OP(BT_OGF_LE, 0x005e) /* 0x205e */

#define BT_HCI_LE_KEY_TYPE_GENERATED            0x00
#define BT_HCI_LE_KEY_TYPE_DEBUG                0x01

struct bt_hci_cp_le_generate_dhkey_v2 {
        uint8_t key[64];
        uint8_t key_type;
} __packed;


#define BT_HCI_OP_LE_ADD_DEV_TO_RL              BT_OP(BT_OGF_LE, 0x0027) /* 0x2027 */
struct bt_hci_cp_le_add_dev_to_rl {
        bt_addr_le_t  peer_id_addr;
        uint8_t       peer_irk[16];
        uint8_t       local_irk[16];
} __packed;

#define BT_HCI_OP_LE_REM_DEV_FROM_RL            BT_OP(BT_OGF_LE, 0x0028) /* 0x2028 */
struct bt_hci_cp_le_rem_dev_from_rl {
        bt_addr_le_t  peer_id_addr;
} __packed;

#define BT_HCI_OP_LE_CLEAR_RL                   BT_OP(BT_OGF_LE, 0x0029) /* 0x2029 */

#define BT_HCI_OP_LE_READ_RL_SIZE               BT_OP(BT_OGF_LE, 0x002a) /* 0x202a */
struct bt_hci_rp_le_read_rl_size {
        uint8_t  status;
        uint8_t  rl_size;
} __packed;

#define BT_HCI_OP_LE_READ_PEER_RPA              BT_OP(BT_OGF_LE, 0x002b) /* 0x202b */
struct bt_hci_cp_le_read_peer_rpa {
        bt_addr_le_t  peer_id_addr;
} __packed;
struct bt_hci_rp_le_read_peer_rpa {
        uint8_t    status;
        bt_addr_t  peer_rpa;
} __packed;

#define BT_HCI_OP_LE_READ_LOCAL_RPA             BT_OP(BT_OGF_LE, 0x002c) /* 0x202c */
struct bt_hci_cp_le_read_local_rpa {
        bt_addr_le_t  peer_id_addr;
} __packed;
struct bt_hci_rp_le_read_local_rpa {
        uint8_t    status;
        bt_addr_t  local_rpa;
} __packed;

#define BT_HCI_ADDR_RES_DISABLE                 0x00
#define BT_HCI_ADDR_RES_ENABLE                  0x01

#define BT_HCI_OP_LE_SET_ADDR_RES_ENABLE        BT_OP(BT_OGF_LE, 0x002d) /* 0x202d */
struct bt_hci_cp_le_set_addr_res_enable {
        uint8_t  enable;
} __packed;

#define BT_HCI_OP_LE_SET_RPA_TIMEOUT            BT_OP(BT_OGF_LE, 0x002e) /* 0x202e */
struct bt_hci_cp_le_set_rpa_timeout {
        uint16_t rpa_timeout;
} __packed;

/* All limits according to BT Core spec 5.4 [Vol 4, Part E, 7.8.46] */
#define BT_HCI_LE_MAX_TX_OCTETS_MIN             0x001B
#define BT_HCI_LE_MAX_TX_OCTETS_MAX             0x00FB
#define BT_HCI_LE_MAX_RX_OCTETS_MIN             0x001B
#define BT_HCI_LE_MAX_RX_OCTETS_MAX             0x00FB

#define BT_HCI_LE_MAX_TX_TIME_MIN               0x0148
#define BT_HCI_LE_MAX_TX_TIME_MAX               0x4290
#define BT_HCI_LE_MAX_RX_TIME_MIN               0x0148
#define BT_HCI_LE_MAX_RX_TIME_MAX               0x4290

#define BT_HCI_OP_LE_READ_MAX_DATA_LEN          BT_OP(BT_OGF_LE, 0x002f) /* 0x202f */
struct bt_hci_rp_le_read_max_data_len {
        uint8_t  status;
        uint16_t max_tx_octets;
        uint16_t max_tx_time;
        uint16_t max_rx_octets;
        uint16_t max_rx_time;
} __packed;

#define BT_HCI_LE_PHY_1M                        0x01
#define BT_HCI_LE_PHY_2M                        0x02
#define BT_HCI_LE_PHY_CODED                     0x03

#define BT_HCI_OP_LE_READ_PHY                   BT_OP(BT_OGF_LE, 0x0030) /* 0x2030 */
struct bt_hci_cp_le_read_phy {
        uint16_t handle;
} __packed;
struct bt_hci_rp_le_read_phy {
        uint8_t  status;
        uint16_t handle;
        uint8_t  tx_phy;
        uint8_t  rx_phy;
} __packed;

#define BT_HCI_LE_PHY_TX_ANY                    BIT(0)
#define BT_HCI_LE_PHY_RX_ANY                    BIT(1)

#define BT_HCI_LE_PHY_PREFER_1M                 BIT(0)
#define BT_HCI_LE_PHY_PREFER_2M                 BIT(1)
#define BT_HCI_LE_PHY_PREFER_CODED              BIT(2)

#define BT_HCI_OP_LE_SET_DEFAULT_PHY            BT_OP(BT_OGF_LE, 0x0031) /* 0x2031 */
struct bt_hci_cp_le_set_default_phy {
        uint8_t all_phys;
        uint8_t tx_phys;
        uint8_t rx_phys;
} __packed;

#define BT_HCI_LE_PHY_CODED_ANY                 0x00
#define BT_HCI_LE_PHY_CODED_S2                  0x01
#define BT_HCI_LE_PHY_CODED_S8                  0x02

#define BT_HCI_OP_LE_SET_PHY                    BT_OP(BT_OGF_LE, 0x0032) /* 0x2032 */
struct bt_hci_cp_le_set_phy {
        uint16_t  handle;
        uint8_t   all_phys;
        uint8_t   tx_phys;
        uint8_t   rx_phys;
        uint16_t  phy_opts;
} __packed;

#define BT_HCI_LE_MOD_INDEX_STANDARD            0x00
#define BT_HCI_LE_MOD_INDEX_STABLE              0x01

#define BT_HCI_LE_RX_PHY_1M                     0x01
#define BT_HCI_LE_RX_PHY_2M                     0x02
#define BT_HCI_LE_RX_PHY_CODED                  0x03

#define BT_HCI_OP_LE_ENH_RX_TEST                BT_OP(BT_OGF_LE, 0x0033) /* 0x2033 */
struct bt_hci_cp_le_enh_rx_test {
        uint8_t  rx_ch;
        uint8_t  phy;
        uint8_t  mod_index;
} __packed;

#define BT_HCI_LE_TX_PHY_1M                     0x01
#define BT_HCI_LE_TX_PHY_2M                     0x02
#define BT_HCI_LE_TX_PHY_CODED_S8               0x03
#define BT_HCI_LE_TX_PHY_CODED_S2               0x04

#define BT_HCI_OP_LE_ENH_TX_TEST                BT_OP(BT_OGF_LE, 0x0034) /* 0x2034 */
struct bt_hci_cp_le_enh_tx_test {
        uint8_t  tx_ch;
        uint8_t  test_data_len;
        uint8_t  pkt_payload;
        uint8_t  phy;
} __packed;

#define BT_HCI_OP_LE_SET_ADV_SET_RANDOM_ADDR    BT_OP(BT_OGF_LE, 0x0035) /* 0x2035 */
struct bt_hci_cp_le_set_adv_set_random_addr {
        uint8_t   handle;
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_LE_ADV_PROP_CONN                 BIT(0)
#define BT_HCI_LE_ADV_PROP_SCAN                 BIT(1)
#define BT_HCI_LE_ADV_PROP_DIRECT               BIT(2)
#define BT_HCI_LE_ADV_PROP_HI_DC_CONN           BIT(3)
#define BT_HCI_LE_ADV_PROP_LEGACY               BIT(4)
#define BT_HCI_LE_ADV_PROP_ANON                 BIT(5)
#define BT_HCI_LE_ADV_PROP_TX_POWER             BIT(6)

#define BT_HCI_LE_PRIM_ADV_INTERVAL_MIN         0x000020
#define BT_HCI_LE_PRIM_ADV_INTERVAL_MAX         0xFFFFFF

#define BT_HCI_LE_ADV_SCAN_REQ_ENABLE  1
#define BT_HCI_LE_ADV_SCAN_REQ_DISABLE 0

#define BT_HCI_LE_ADV_TX_POWER_MIN     -127
#define BT_HCI_LE_ADV_TX_POWER_MAX      20
#define BT_HCI_LE_ADV_TX_POWER_NO_PREF 0x7F

#define BT_HCI_LE_ADV_HANDLE_MAX       0xEF

#define BT_HCI_LE_EXT_ADV_SID_INVALID  0xFF

#define BT_HCI_OP_LE_SET_EXT_ADV_PARAM          BT_OP(BT_OGF_LE, 0x0036) /* 0x2036 */
struct bt_hci_cp_le_set_ext_adv_param {
        uint8_t      handle;
        uint16_t     props;
        uint8_t      prim_min_interval[3];
        uint8_t      prim_max_interval[3];
        uint8_t      prim_channel_map;
        uint8_t      own_addr_type;
        bt_addr_le_t peer_addr;
        uint8_t      filter_policy;
        int8_t       tx_power;
        uint8_t      prim_adv_phy;
        uint8_t      sec_adv_max_skip;
        uint8_t      sec_adv_phy;
        uint8_t      sid;
        uint8_t      scan_req_notify_enable;
} __packed;
struct bt_hci_rp_le_set_ext_adv_param {
        uint8_t status;
        int8_t  tx_power;
} __packed;

#define BT_HCI_LE_ADV_PHY_OPTION_NO_REQUIRED 0x00
#define BT_HCI_LE_ADV_PHY_OPTION_REQUIRE_S2  0x03
#define BT_HCI_LE_ADV_PHY_OPTION_REQUIRE_S8  0x04

#define BT_HCI_OP_LE_SET_EXT_ADV_PARAM_V2        BT_OP(BT_OGF_LE, 0x007F) /* 0x207F */
struct bt_hci_cp_le_set_ext_adv_param_v2 {
        uint8_t      handle;
        uint16_t     props;
        uint8_t      prim_min_interval[3];
        uint8_t      prim_max_interval[3];
        uint8_t      prim_channel_map;
        uint8_t      own_addr_type;
        bt_addr_le_t peer_addr;
        uint8_t      filter_policy;
        int8_t       tx_power;
        uint8_t      prim_adv_phy;
        uint8_t      sec_adv_max_skip;
        uint8_t      sec_adv_phy;
        uint8_t      sid;
        uint8_t      scan_req_notify_enable;
        uint8_t      prim_adv_phy_opt;
        uint8_t      sec_adv_phy_opt;
} __packed;

#define BT_HCI_LE_EXT_ADV_OP_INTERM_FRAG        0x00
#define BT_HCI_LE_EXT_ADV_OP_FIRST_FRAG         0x01
#define BT_HCI_LE_EXT_ADV_OP_LAST_FRAG          0x02
#define BT_HCI_LE_EXT_ADV_OP_COMPLETE_DATA      0x03
#define BT_HCI_LE_EXT_ADV_OP_UNCHANGED_DATA     0x04

#define BT_HCI_LE_EXT_ADV_FRAG_ENABLED          0x00
#define BT_HCI_LE_EXT_ADV_FRAG_DISABLED         0x01

#define BT_HCI_LE_EXT_ADV_FRAG_MAX_LEN          251

#define BT_HCI_OP_LE_SET_EXT_ADV_DATA           BT_OP(BT_OGF_LE, 0x0037) /* 0x2037 */
struct bt_hci_cp_le_set_ext_adv_data {
        uint8_t  handle;
        uint8_t  op;
        uint8_t  frag_pref;
        uint8_t  len;
        uint8_t  data[0];
} __packed;

#define BT_HCI_OP_LE_SET_EXT_SCAN_RSP_DATA      BT_OP(BT_OGF_LE, 0x0038) /* 0x2038 */
struct bt_hci_cp_le_set_ext_scan_rsp_data {
        uint8_t  handle;
        uint8_t  op;
        uint8_t  frag_pref;
        uint8_t  len;
        uint8_t  data[0];
} __packed;

#define BT_HCI_OP_LE_SET_EXT_ADV_ENABLE         BT_OP(BT_OGF_LE, 0x0039) /* 0x2039 */
struct bt_hci_ext_adv_set {
        uint8_t  handle;
        uint16_t duration;
        uint8_t  max_ext_adv_evts;
} __packed;

struct bt_hci_cp_le_set_ext_adv_enable {
        uint8_t  enable;
        uint8_t  set_num;
        struct bt_hci_ext_adv_set s[0];
} __packed;

#define BT_HCI_OP_LE_READ_MAX_ADV_DATA_LEN      BT_OP(BT_OGF_LE, 0x003a) /* 0x203a */
struct bt_hci_rp_le_read_max_adv_data_len {
        uint8_t  status;
        uint16_t max_adv_data_len;
} __packed;

#define BT_HCI_OP_LE_READ_NUM_ADV_SETS          BT_OP(BT_OGF_LE, 0x003b) /* 0x203b */
struct bt_hci_rp_le_read_num_adv_sets {
        uint8_t  status;
        uint8_t  num_sets;
} __packed;

#define BT_HCI_OP_LE_REMOVE_ADV_SET             BT_OP(BT_OGF_LE, 0x003c) /* 0x203c */
struct bt_hci_cp_le_remove_adv_set {
        uint8_t  handle;
} __packed;

#define BT_HCI_OP_CLEAR_ADV_SETS                BT_OP(BT_OGF_LE, 0x003d) /* 0x203d */

#define BT_HCI_LE_PER_ADV_INTERVAL_MIN          0x0006
#define BT_HCI_LE_PER_ADV_INTERVAL_MAX          0xFFFF

#define BT_HCI_OP_LE_SET_PER_ADV_PARAM          BT_OP(BT_OGF_LE, 0x003e) /* 0x203e */
struct bt_hci_cp_le_set_per_adv_param {
        uint8_t  handle;
        uint16_t min_interval;
        uint16_t max_interval;
        uint16_t props;
} __packed;

#define BT_HCI_LE_PER_ADV_OP_INTERM_FRAG        0x00
#define BT_HCI_LE_PER_ADV_OP_FIRST_FRAG         0x01
#define BT_HCI_LE_PER_ADV_OP_LAST_FRAG          0x02
#define BT_HCI_LE_PER_ADV_OP_COMPLETE_DATA      0x03

#define BT_HCI_LE_PER_ADV_FRAG_MAX_LEN          252

#define BT_HCI_OP_LE_SET_PER_ADV_DATA           BT_OP(BT_OGF_LE, 0x003f) /* 0x203f */
struct bt_hci_cp_le_set_per_adv_data {
        uint8_t  handle;
        uint8_t  op;
        uint8_t  len;
        uint8_t  data[0];
} __packed;

#define BT_HCI_LE_SET_PER_ADV_ENABLE_ENABLE     BIT(0)
#define BT_HCI_LE_SET_PER_ADV_ENABLE_ADI        BIT(1)

#define BT_HCI_OP_LE_SET_PER_ADV_ENABLE         BT_OP(BT_OGF_LE, 0x0040) /* 0x2040 */
struct bt_hci_cp_le_set_per_adv_enable {
        uint8_t  enable;
        uint8_t  handle;
} __packed;

#define BT_HCI_OP_LE_SET_EXT_SCAN_PARAM         BT_OP(BT_OGF_LE, 0x0041) /* 0x2041 */
struct bt_hci_ext_scan_phy {
        uint8_t  type;
        uint16_t interval;
        uint16_t window;
} __packed;

#define BT_HCI_LE_EXT_SCAN_PHY_1M               BIT(0)
#define BT_HCI_LE_EXT_SCAN_PHY_2M               BIT(1)
#define BT_HCI_LE_EXT_SCAN_PHY_CODED            BIT(2)

struct bt_hci_cp_le_set_ext_scan_param {
        uint8_t  own_addr_type;
        uint8_t  filter_policy;
        uint8_t  phys;
        struct bt_hci_ext_scan_phy p[0];
} __packed;

/* Extends BT_HCI_LE_SCAN_FILTER_DUP */
#define BT_HCI_LE_EXT_SCAN_FILTER_DUP_ENABLE_RESET  0x02

#define BT_HCI_OP_LE_SET_EXT_SCAN_ENABLE        BT_OP(BT_OGF_LE, 0x0042) /* 0x2042 */
struct bt_hci_cp_le_set_ext_scan_enable {
        uint8_t  enable;
        uint8_t  filter_dup;
        uint16_t duration;
        uint16_t period;
} __packed;

#define BT_HCI_OP_LE_EXT_CREATE_CONN            BT_OP(BT_OGF_LE, 0x0043) /* 0x2043 */
#define BT_HCI_OP_LE_EXT_CREATE_CONN_V2         BT_OP(BT_OGF_LE, 0x0085) /* 0x2085 */
struct bt_hci_ext_conn_phy {
        uint16_t scan_interval;
        uint16_t scan_window;
        uint16_t conn_interval_min;
        uint16_t conn_interval_max;
        uint16_t conn_latency;
        uint16_t supervision_timeout;
        uint16_t min_ce_len;
        uint16_t max_ce_len;
} __packed;

struct bt_hci_cp_le_ext_create_conn {
        uint8_t      filter_policy;
        uint8_t      own_addr_type;
        bt_addr_le_t peer_addr;
        uint8_t      phys;
        struct bt_hci_ext_conn_phy p[0];
} __packed;

struct bt_hci_cp_le_ext_create_conn_v2 {
        uint8_t      adv_handle;
        uint8_t      subevent;
        uint8_t      filter_policy;
        uint8_t      own_addr_type;
        bt_addr_le_t peer_addr;
        uint8_t      phys;
        struct bt_hci_ext_conn_phy p[0];
} __packed;

#define BT_HCI_OP_LE_SET_PER_ADV_SUBEVENT_DATA  BT_OP(BT_OGF_LE, 0x0082) /* 0x2082 */
struct bt_hci_cp_le_set_pawr_subevent_data_element {
        uint8_t subevent;
        uint8_t response_slot_start;
        uint8_t response_slot_count;
        uint8_t subevent_data_length;
        uint8_t subevent_data[0];
} __packed;

struct bt_hci_cp_le_set_pawr_subevent_data {
        uint8_t adv_handle;
        uint8_t num_subevents;
        struct bt_hci_cp_le_set_pawr_subevent_data_element subevents[0];
} __packed;


#define BT_HCI_OP_LE_SET_PER_ADV_RESPONSE_DATA  BT_OP(BT_OGF_LE, 0x0083) /* 0x2083 */
struct bt_hci_cp_le_set_pawr_response_data {
        uint16_t sync_handle;
        uint16_t request_event;
        uint8_t  request_subevent;
        uint8_t  response_subevent;
        uint8_t  response_slot;
        uint8_t  response_data_length;
        uint8_t  response_data[0];
} __packed;

#define BT_HCI_OP_LE_SET_PER_ADV_SYNC_SUBEVENT  BT_OP(BT_OGF_LE, 0x0084) /* 0x2084 */
struct bt_hci_cp_le_set_pawr_sync_subevent {
        uint16_t sync_handle;
        uint16_t periodic_adv_properties;
        uint8_t  num_subevents;
        uint8_t  subevents[0];
} __packed;


#define BT_HCI_OP_LE_SET_PER_ADV_PARAM_V2       BT_OP(BT_OGF_LE, 0x0086) /* 0x2086 */
struct bt_hci_cp_le_set_per_adv_param_v2 {
        uint8_t  handle;
        uint16_t min_interval;
        uint16_t max_interval;
        uint16_t props;
        uint8_t  num_subevents;
        uint8_t  subevent_interval;
        uint8_t  response_slot_delay;
        uint8_t  response_slot_spacing;
        uint8_t  num_response_slots;
} __packed;


#define BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_USE_LIST               BIT(0)
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_REPORTS_DISABLED       BIT(1)
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_FILTER_DUPLICATE       BIT(2)

#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_FILTERING     0
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOA           BIT(0)
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOD_1US       BIT(1)
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOD_2US       BIT(2)
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_CTE           BIT(3)
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ONLY_CTE         BIT(4)
/* Constants to check correctness of CTE type */
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ALLOWED_BITS 5
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_INVALID_VALUE \
        (~BIT_MASK(BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ALLOWED_BITS))

#define BT_HCI_OP_LE_PER_ADV_CREATE_SYNC        BT_OP(BT_OGF_LE, 0x0044) /* 0x2044 */
struct bt_hci_cp_le_per_adv_create_sync {
        uint8_t      options;
        uint8_t      sid;
        bt_addr_le_t addr;
        uint16_t     skip;
        uint16_t     sync_timeout;
        uint8_t      cte_type;
} __packed;

#define BT_HCI_OP_LE_PER_ADV_CREATE_SYNC_CANCEL BT_OP(BT_OGF_LE, 0x0045) /* 0x2045 */

#define BT_HCI_OP_LE_PER_ADV_TERMINATE_SYNC     BT_OP(BT_OGF_LE, 0x0046) /* 0x2046 */
struct bt_hci_cp_le_per_adv_terminate_sync {
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_ADD_DEV_TO_PER_ADV_LIST    BT_OP(BT_OGF_LE, 0x0047) /* 0x2047 */
struct bt_hci_cp_le_add_dev_to_per_adv_list {
        bt_addr_le_t addr;
        uint8_t      sid;
} __packed;

#define BT_HCI_OP_LE_REM_DEV_FROM_PER_ADV_LIST  BT_OP(BT_OGF_LE, 0x0048) /* 0x2048 */
struct bt_hci_cp_le_rem_dev_from_per_adv_list {
        bt_addr_le_t addr;
        uint8_t      sid;
} __packed;

#define BT_HCI_OP_LE_CLEAR_PER_ADV_LIST         BT_OP(BT_OGF_LE, 0x0049) /* 0x2049 */

#define BT_HCI_OP_LE_READ_PER_ADV_LIST_SIZE     BT_OP(BT_OGF_LE, 0x004a) /* 0x204a */
struct bt_hci_rp_le_read_per_adv_list_size {
        uint8_t  status;
        uint8_t  list_size;
} __packed;

#define BT_HCI_OP_LE_READ_TX_POWER              BT_OP(BT_OGF_LE, 0x004b) /* 0x204b */
struct bt_hci_rp_le_read_tx_power {
        uint8_t status;
        int8_t  min_tx_power;
        int8_t  max_tx_power;
} __packed;

#define BT_HCI_OP_LE_READ_RF_PATH_COMP          BT_OP(BT_OGF_LE, 0x004c) /* 0x204c */
struct bt_hci_rp_le_read_rf_path_comp {
        uint8_t status;
        int16_t tx_path_comp;
        int16_t rx_path_comp;
} __packed;

#define BT_HCI_OP_LE_WRITE_RF_PATH_COMP         BT_OP(BT_OGF_LE, 0x004d) /* 0x204d */
struct bt_hci_cp_le_write_rf_path_comp {
        int16_t  tx_path_comp;
        int16_t  rx_path_comp;
} __packed;

#define BT_HCI_LE_PRIVACY_MODE_NETWORK          0x00
#define BT_HCI_LE_PRIVACY_MODE_DEVICE           0x01

#define BT_HCI_OP_LE_SET_PRIVACY_MODE           BT_OP(BT_OGF_LE, 0x004e) /* 0x204e */
struct bt_hci_cp_le_set_privacy_mode {
        bt_addr_le_t id_addr;
        uint8_t         mode;
} __packed;

#define BT_HCI_LE_TEST_CTE_DISABLED             0x00
#define BT_HCI_LE_TEST_CTE_TYPE_ANY             0x00
#define BT_HCI_LE_TEST_SLOT_DURATION_ANY        0x00
#define BT_HCI_LE_TEST_SWITCH_PATTERN_LEN_ANY   0x00

#define BT_HCI_OP_LE_RX_TEST_V3                 BT_OP(BT_OGF_LE, 0x004f) /* 0x204f */
struct bt_hci_cp_le_rx_test_v3 {
        uint8_t  rx_ch;
        uint8_t  phy;
        uint8_t  mod_index;
        uint8_t  expected_cte_len;
        uint8_t  expected_cte_type;
        uint8_t  slot_durations;
        uint8_t  switch_pattern_len;
        uint8_t  ant_ids[0];
} __packed;

#define BT_HCI_OP_LE_TX_TEST_V3                 BT_OP(BT_OGF_LE, 0x0050) /* 0x2050 */

struct bt_hci_cp_le_tx_test_v3 {
        uint8_t  tx_ch;
        uint8_t  test_data_len;
        uint8_t  pkt_payload;
        uint8_t  phy;
        uint8_t  cte_len;
        uint8_t  cte_type;
        uint8_t  switch_pattern_len;
        uint8_t  ant_ids[0];
} __packed;

/* Min and max Constant Tone Extension length in 8us units */
#define BT_HCI_LE_CTE_LEN_MIN                  0x2
#define BT_HCI_LE_CTE_LEN_MAX                  0x14

#define BT_HCI_LE_AOA_CTE                      0x0
#define BT_HCI_LE_AOD_CTE_1US                  0x1
#define BT_HCI_LE_AOD_CTE_2US                  0x2
#define BT_HCI_LE_NO_CTE                       0xFF

#define BT_HCI_LE_CTE_COUNT_MIN                0x1
#define BT_HCI_LE_CTE_COUNT_MAX                0x10

#define BT_HCI_OP_LE_SET_CL_CTE_TX_PARAMS      BT_OP(BT_OGF_LE, 0x0051) /* 0x2051 */
struct bt_hci_cp_le_set_cl_cte_tx_params {
        uint8_t handle;
        uint8_t cte_len;
        uint8_t cte_type;
        uint8_t cte_count;
        uint8_t switch_pattern_len;
        uint8_t ant_ids[0];
} __packed;

#define BT_HCI_OP_LE_SET_CL_CTE_TX_ENABLE      BT_OP(BT_OGF_LE, 0x0052) /* 0x2052 */
struct bt_hci_cp_le_set_cl_cte_tx_enable {
        uint8_t handle;
        uint8_t cte_enable;
} __packed;

#define BT_HCI_LE_ANTENNA_SWITCHING_SLOT_1US   0x1
#define BT_HCI_LE_ANTENNA_SWITCHING_SLOT_2US   0x2

#define BT_HCI_LE_SAMPLE_CTE_ALL               0x0
#define BT_HCI_LE_SAMPLE_CTE_COUNT_MIN         0x1
#define BT_HCI_LE_SAMPLE_CTE_COUNT_MAX         0x10

#define BT_HCI_OP_LE_SET_CL_CTE_SAMPLING_ENABLE BT_OP(BT_OGF_LE, 0x0053) /* 0x2053 */
struct bt_hci_cp_le_set_cl_cte_sampling_enable {
        uint16_t sync_handle;
        uint8_t  sampling_enable;
        uint8_t  slot_durations;
        uint8_t  max_sampled_cte;
        uint8_t  switch_pattern_len;
        uint8_t  ant_ids[0];
} __packed;

struct bt_hci_rp_le_set_cl_cte_sampling_enable {
        uint8_t  status;
        uint16_t sync_handle;
} __packed;

#define BT_HCI_OP_LE_SET_CONN_CTE_RX_PARAMS BT_OP(BT_OGF_LE, 0x0054) /* 0x2054 */
struct bt_hci_cp_le_set_conn_cte_rx_params {
        uint16_t handle;
        uint8_t  sampling_enable;
        uint8_t  slot_durations;
        uint8_t  switch_pattern_len;
        uint8_t  ant_ids[0];
} __packed;

struct bt_hci_rp_le_set_conn_cte_rx_params {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_LE_AOA_CTE_RSP                   BIT(0)
#define BT_HCI_LE_AOD_CTE_RSP_1US               BIT(1)
#define BT_HCI_LE_AOD_CTE_RSP_2US               BIT(2)

#define BT_HCI_LE_SWITCH_PATTERN_LEN_MIN        0x2
#define BT_HCI_LE_SWITCH_PATTERN_LEN_MAX        0x4B

#define BT_HCI_OP_LE_SET_CONN_CTE_TX_PARAMS     BT_OP(BT_OGF_LE, 0x0055) /* 0x2055 */
struct bt_hci_cp_le_set_conn_cte_tx_params {
        uint16_t handle;
        uint8_t  cte_types;
        uint8_t  switch_pattern_len;
        uint8_t  ant_ids[0];
} __packed;

struct bt_hci_rp_le_set_conn_cte_tx_params {
        uint8_t  status;
        uint16_t handle;
} __packed;

/* Interval between consecutive CTE request procedure starts in number of connection events. */
#define BT_HCI_REQUEST_CTE_ONCE                0x0
#define BT_HCI_REQUEST_CTE_INTERVAL_MIN        0x1
#define BT_HCI_REQUEST_CTE_INTERVAL_MAX        0xFFFF

#define BT_HCI_OP_LE_CONN_CTE_REQ_ENABLE       BT_OP(BT_OGF_LE, 0x0056) /* 0x2056 */
struct bt_hci_cp_le_conn_cte_req_enable {
        uint16_t handle;
        uint8_t  enable;
        uint16_t cte_request_interval;
        uint8_t  requested_cte_length;
        uint8_t  requested_cte_type;
} __packed;

struct bt_hci_rp_le_conn_cte_req_enable {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_CONN_CTE_RSP_ENABLE       BT_OP(BT_OGF_LE, 0x0057) /* 0x2057 */
struct bt_hci_cp_le_conn_cte_rsp_enable {
        uint16_t handle;
        uint8_t  enable;
} __packed;

struct bt_hci_rp_le_conn_cte_rsp_enable {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_LE_1US_AOD_TX                    BIT(0)
#define BT_HCI_LE_1US_AOD_RX                    BIT(1)
#define BT_HCI_LE_1US_AOA_RX                    BIT(2)

#define BT_HCI_LE_NUM_ANT_MIN                   0x1
#define BT_HCI_LE_NUM_ANT_MAX                   0x4B

#define BT_HCI_LE_MAX_SWITCH_PATTERN_LEN_MIN    0x2
#define BT_HCI_LE_MAX_SWITCH_PATTERN_LEN_MAX    0x4B

#define BT_HCI_LE_MAX_CTE_LEN_MIN               0x2
#define BT_HCI_LE_MAX_CTE_LEN_MAX               0x14

#define BT_HCI_OP_LE_READ_ANT_INFO              BT_OP(BT_OGF_LE, 0x0058) /* 0x2058 */
struct bt_hci_rp_le_read_ant_info {
        uint8_t status;
        uint8_t switch_sample_rates;
        uint8_t num_ant;
        uint8_t max_switch_pattern_len;
        uint8_t max_cte_len;
};

#define BT_HCI_LE_SET_PER_ADV_RECV_ENABLE_ENABLE           BIT(0)
#define BT_HCI_LE_SET_PER_ADV_RECV_ENABLE_FILTER_DUPLICATE BIT(1)

#define BT_HCI_OP_LE_SET_PER_ADV_RECV_ENABLE     BT_OP(BT_OGF_LE, 0x0059) /* 0x2059 */
struct bt_hci_cp_le_set_per_adv_recv_enable {
        uint16_t handle;
        uint8_t  enable;
} __packed;

#define BT_HCI_OP_LE_PER_ADV_SYNC_TRANSFER      BT_OP(BT_OGF_LE, 0x005a) /* 0x205a */
struct bt_hci_cp_le_per_adv_sync_transfer {
        uint16_t conn_handle;
        uint16_t service_data;
        uint16_t sync_handle;
} __packed;

struct bt_hci_rp_le_per_adv_sync_transfer {
        uint8_t  status;
        uint16_t conn_handle;
} __packed;

#define BT_HCI_OP_LE_PER_ADV_SET_INFO_TRANSFER  BT_OP(BT_OGF_LE, 0x005b) /* 0x205b */
struct bt_hci_cp_le_per_adv_set_info_transfer {
        uint16_t conn_handle;
        uint16_t service_data;
        uint8_t  adv_handle;
} __packed;

struct bt_hci_rp_le_per_adv_set_info_transfer {
        uint8_t  status;
        uint16_t conn_handle;
} __packed;

#define BT_HCI_LE_PAST_MODE_NO_SYNC                0x00
#define BT_HCI_LE_PAST_MODE_NO_REPORTS             0x01
#define BT_HCI_LE_PAST_MODE_SYNC                   0x02
#define BT_HCI_LE_PAST_MODE_SYNC_FILTER_DUPLICATES 0x03

#define BT_HCI_LE_PAST_CTE_TYPE_NO_AOA           BIT(0)
#define BT_HCI_LE_PAST_CTE_TYPE_NO_AOD_1US       BIT(1)
#define BT_HCI_LE_PAST_CTE_TYPE_NO_AOD_2US       BIT(2)
#define BT_HCI_LE_PAST_CTE_TYPE_NO_CTE           BIT(3)
#define BT_HCI_LE_PAST_CTE_TYPE_ONLY_CTE         BIT(4)

#define BT_HCI_OP_LE_PAST_PARAM                 BT_OP(BT_OGF_LE, 0x005c) /* 0x205c */
struct bt_hci_cp_le_past_param {
        uint16_t conn_handle;
        uint8_t  mode;
        uint16_t skip;
        uint16_t timeout;
        uint8_t  cte_type;
} __packed;

struct bt_hci_rp_le_past_param {
        uint8_t  status;
        uint16_t conn_handle;
} __packed;

#define BT_HCI_OP_LE_DEFAULT_PAST_PARAM         BT_OP(BT_OGF_LE, 0x005d) /* 0x205d */
struct bt_hci_cp_le_default_past_param {
        uint8_t  mode;
        uint16_t skip;
        uint16_t timeout;
        uint8_t  cte_type;
} __packed;

struct bt_hci_rp_le_default_past_param {
        uint8_t  status;
} __packed;

#define BT_HCI_OP_LE_READ_BUFFER_SIZE_V2        BT_OP(BT_OGF_LE, 0x0060) /* 0x2060 */
struct bt_hci_rp_le_read_buffer_size_v2 {
        uint8_t  status;
        uint16_t acl_max_len;
        uint8_t  acl_max_num;
        uint16_t iso_max_len;
        uint8_t  iso_max_num;
} __packed;

#define BT_HCI_OP_LE_READ_ISO_TX_SYNC           BT_OP(BT_OGF_LE, 0x0061) /* 0x2061 */
struct bt_hci_cp_le_read_iso_tx_sync {
        uint16_t handle;
} __packed;

struct bt_hci_rp_le_read_iso_tx_sync {
        uint8_t  status;
        uint16_t handle;
        uint16_t seq;
        uint32_t timestamp;
        uint8_t  offset[3];
} __packed;

#define BT_HCI_ISO_CIG_ID_MAX                   0xFE
#define BT_HCI_ISO_CIS_COUNT_MAX                0x1F
#define BT_HCI_ISO_SDU_INTERVAL_MIN             0x0000FF
#define BT_HCI_ISO_SDU_INTERVAL_MAX             0x0FFFFF
#define BT_HCI_ISO_WORST_CASE_SCA_VALID_MASK    0x07
#define BT_HCI_ISO_PACKING_VALID_MASK           0x01
#define BT_HCI_ISO_FRAMING_VALID_MASK           0x01
#define BT_HCI_ISO_MAX_TRANSPORT_LATENCY_MIN    0x0005
#define BT_HCI_ISO_MAX_TRANSPORT_LATENCY_MAX    0x0FA0
#define BT_HCI_ISO_CIS_ID_VALID_MAX             0xEF
#define BT_HCI_ISO_MAX_SDU_VALID_MASK           0x0FFF
#define BT_HCI_ISO_PHY_VALID_MASK               0x07
#define BT_HCI_ISO_INTERVAL_MIN                 0x0004
#define BT_HCI_ISO_INTERVAL_MAX                 0x0C80

#define BT_HCI_OP_LE_SET_CIG_PARAMS             BT_OP(BT_OGF_LE, 0x0062) /* 0x2062 */
struct bt_hci_cis_params {
        uint8_t  cis_id;
        uint16_t c_sdu;
        uint16_t p_sdu;
        uint8_t  c_phy;
        uint8_t  p_phy;
        uint8_t  c_rtn;
        uint8_t  p_rtn;
} __packed;

struct bt_hci_cp_le_set_cig_params {
        uint8_t  cig_id;
        uint8_t  c_interval[3];
        uint8_t  p_interval[3];
        uint8_t  sca;
        uint8_t  packing;
        uint8_t  framing;
        uint16_t c_latency;
        uint16_t p_latency;
        uint8_t  num_cis;
        struct bt_hci_cis_params cis[0];
} __packed;

struct bt_hci_rp_le_set_cig_params {
        uint8_t  status;
        uint8_t  cig_id;
        uint8_t  num_handles;
        uint16_t handle[0];
} __packed;

#define BT_HCI_OP_LE_SET_CIG_PARAMS_TEST        BT_OP(BT_OGF_LE, 0x0063) /* 0x2063 */
struct bt_hci_cis_params_test {
        uint8_t  cis_id;
        uint8_t  nse;
        uint16_t c_sdu;
        uint16_t p_sdu;
        uint16_t c_pdu;
        uint16_t p_pdu;
        uint8_t  c_phy;
        uint8_t  p_phy;
        uint8_t  c_bn;
        uint8_t  p_bn;
} __packed;

struct bt_hci_cp_le_set_cig_params_test {
        uint8_t  cig_id;
        uint8_t  c_interval[3];
        uint8_t  p_interval[3];
        uint8_t  c_ft;
        uint8_t  p_ft;
        uint16_t iso_interval;
        uint8_t  sca;
        uint8_t  packing;
        uint8_t  framing;
        uint8_t  num_cis;
        struct bt_hci_cis_params_test cis[0];
} __packed;

struct bt_hci_rp_le_set_cig_params_test {
        uint8_t  status;
        uint8_t  cig_id;
        uint8_t  num_handles;
        uint16_t handle[0];
} __packed;

#define BT_HCI_OP_LE_CREATE_CIS                 BT_OP(BT_OGF_LE, 0x0064) /* 0x2064 */
struct bt_hci_cis {
        uint16_t  cis_handle;
        uint16_t  acl_handle;
} __packed;

struct bt_hci_cp_le_create_cis {
        uint8_t  num_cis;
        struct bt_hci_cis cis[0];
} __packed;

#define BT_HCI_OP_LE_REMOVE_CIG                 BT_OP(BT_OGF_LE, 0x0065) /* 0x2065 */
struct bt_hci_cp_le_remove_cig {
        uint8_t  cig_id;
} __packed;

struct bt_hci_rp_le_remove_cig {
        uint8_t  status;
        uint8_t  cig_id;
} __packed;

#define BT_HCI_OP_LE_ACCEPT_CIS                 BT_OP(BT_OGF_LE, 0x0066) /* 0x2066 */
struct bt_hci_cp_le_accept_cis {
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_REJECT_CIS                 BT_OP(BT_OGF_LE, 0x0067) /* 0x2067 */
struct bt_hci_cp_le_reject_cis {
        uint16_t handle;
        uint8_t  reason;
} __packed;

struct bt_hci_rp_le_reject_cis {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_CREATE_BIG                 BT_OP(BT_OGF_LE, 0x0068) /* 0x2068 */
struct bt_hci_cp_le_create_big {
        uint8_t  big_handle;
        uint8_t  adv_handle;
        uint8_t  num_bis;
        uint8_t  sdu_interval[3];
        uint16_t max_sdu;
        uint16_t max_latency;
        uint8_t  rtn;
        uint8_t  phy;
        uint8_t  packing;
        uint8_t  framing;
        uint8_t  encryption;
        uint8_t  bcode[16];
} __packed;

#define BT_HCI_OP_LE_CREATE_BIG_TEST            BT_OP(BT_OGF_LE, 0x0069) /* 0x2069 */
struct bt_hci_cp_le_create_big_test {
        uint8_t  big_handle;
        uint8_t  adv_handle;
        uint8_t  num_bis;
        uint8_t  sdu_interval[3];
        uint16_t iso_interval;
        uint8_t  nse;
        uint16_t max_sdu;
        uint16_t max_pdu;
        uint8_t  phy;
        uint8_t  packing;
        uint8_t  framing;
        uint8_t  bn;
        uint8_t  irc;
        uint8_t  pto;
        uint8_t  encryption;
        uint8_t  bcode[16];
} __packed;

#define BT_HCI_OP_LE_TERMINATE_BIG              BT_OP(BT_OGF_LE, 0x006a) /* 0x206a */
struct bt_hci_cp_le_terminate_big {
        uint8_t  big_handle;
        uint8_t  reason;
} __packed;

#define BT_HCI_OP_LE_BIG_CREATE_SYNC            BT_OP(BT_OGF_LE, 0x006b) /* 0x206b */
struct bt_hci_cp_le_big_create_sync {
        uint8_t  big_handle;
        uint16_t sync_handle;
        uint8_t  encryption;
        uint8_t  bcode[16];
        uint8_t  mse;
        uint16_t sync_timeout;
        uint8_t  num_bis;
        uint8_t  bis[0];
} __packed;

#define BT_HCI_OP_LE_BIG_TERMINATE_SYNC         BT_OP(BT_OGF_LE, 0x006c) /* 0x206c */
struct bt_hci_cp_le_big_terminate_sync {
        uint8_t  big_handle;
} __packed;

struct bt_hci_rp_le_big_terminate_sync {
        uint8_t  status;
        uint8_t  big_handle;
} __packed;

#define BT_HCI_OP_LE_REQ_PEER_SC                BT_OP(BT_OGF_LE, 0x006d) /* 0x206d */
struct bt_hci_cp_le_req_peer_sca {
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_SETUP_ISO_PATH             BT_OP(BT_OGF_LE, 0x006e) /* 0x206e */
struct bt_hci_cp_le_setup_iso_path {
        uint16_t handle;
        uint8_t  path_dir;
        uint8_t  path_id;
        struct bt_hci_cp_codec_id codec_id;
        uint8_t  controller_delay[3];
        uint8_t  codec_config_len;
        uint8_t  codec_config[0];
} __packed;

struct bt_hci_rp_le_setup_iso_path {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_REMOVE_ISO_PATH            BT_OP(BT_OGF_LE, 0x006f) /* 0x206f */
struct bt_hci_cp_le_remove_iso_path {
        uint16_t handle;
        uint8_t  path_dir;
} __packed;

struct bt_hci_rp_le_remove_iso_path {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_ISO_TEST_ZERO_SIZE_SDU     0
#define BT_HCI_ISO_TEST_VARIABLE_SIZE_SDU 1
#define BT_HCI_ISO_TEST_MAX_SIZE_SDU      2

#define BT_HCI_OP_LE_ISO_TRANSMIT_TEST          BT_OP(BT_OGF_LE, 0x0070) /* 0x2070 */
struct bt_hci_cp_le_iso_transmit_test {
        uint16_t handle;
        uint8_t  payload_type;
} __packed;

struct bt_hci_rp_le_iso_transmit_test {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_ISO_RECEIVE_TEST           BT_OP(BT_OGF_LE, 0x0071) /* 0x2071 */
struct bt_hci_cp_le_iso_receive_test {
        uint16_t handle;
        uint8_t  payload_type;
} __packed;

struct bt_hci_rp_le_iso_receive_test {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_ISO_READ_TEST_COUNTERS     BT_OP(BT_OGF_LE, 0x0072) /* 0x2072 */
struct bt_hci_cp_le_read_test_counters {
        uint16_t handle;
} __packed;

struct bt_hci_rp_le_read_test_counters {
        uint8_t  status;
        uint16_t handle;
        uint32_t received_cnt;
        uint32_t missed_cnt;
        uint32_t failed_cnt;
} __packed;

#define BT_HCI_OP_LE_ISO_TEST_END               BT_OP(BT_OGF_LE, 0x0073) /* 0x2073 */
struct bt_hci_cp_le_iso_test_end {
        uint16_t handle;
} __packed;

struct bt_hci_rp_le_iso_test_end {
        uint8_t  status;
        uint16_t handle;
        uint32_t received_cnt;
        uint32_t missed_cnt;
        uint32_t failed_cnt;
} __packed;

#define BT_HCI_OP_LE_SET_HOST_FEATURE           BT_OP(BT_OGF_LE, 0x0074) /* 0x2074 */
struct bt_hci_cp_le_set_host_feature {
        uint8_t  bit_number;
        uint8_t  bit_value;
} __packed;

struct bt_hci_rp_le_set_host_feature {
        uint8_t  status;
} __packed;

#define BT_HCI_OP_LE_READ_ISO_LINK_QUALITY      BT_OP(BT_OGF_LE, 0x0075) /* 0x2075 */
struct bt_hci_cp_le_read_iso_link_quality {
        uint16_t handle;
} __packed;

struct bt_hci_rp_le_read_iso_link_quality {
        uint8_t  status;
        uint16_t handle;
        uint32_t tx_unacked_packets;
        uint32_t tx_flushed_packets;
        uint32_t tx_last_subevent_packets;
        uint32_t retransmitted_packets;
        uint32_t crc_error_packets;
        uint32_t rx_unreceived_packets;
        uint32_t duplicate_packets;
} __packed;

#define BT_HCI_OP_LE_TX_TEST_V4                 BT_OP(BT_OGF_LE, 0x007B) /* 0x207B */

struct bt_hci_cp_le_tx_test_v4 {
        uint8_t  tx_ch;
        uint8_t  test_data_len;
        uint8_t  pkt_payload;
        uint8_t  phy;
        uint8_t  cte_len;
        uint8_t  cte_type;
        uint8_t  switch_pattern_len;
        uint8_t  ant_ids[0];
} __packed;

#define BT_HCI_OP_LE_READ_ALL_LOCAL_SUPPORTED_FEATURES BT_OP(BT_OGF_LE, 0x0087) /* 0x2087 */
struct bt_hci_rp_le_read_all_local_supported_features {
        uint8_t  status;
        uint8_t  max_page;
        uint8_t  features[248];
} __packed;

#define BT_READ_ALL_LOCAL_FEATURES_SUPPORTED(supported_commands)                                   \
        BT_CMD_TEST(supported_commands, 47, 2)

#define BT_HCI_OP_LE_READ_ALL_REMOTE_FEATURES BT_OP(BT_OGF_LE, 0x0088) /* 0x2088 */
struct bt_hci_cp_le_read_all_remote_features {
        uint16_t handle;
        uint8_t  pages_requested;
} __packed;

#define BT_HCI_TX_TEST_POWER_MIN -0x7F
#define BT_HCI_TX_TEST_POWER_MAX 0x14

#define BT_HCI_TX_TEST_POWER_MIN_SET 0x7E
#define BT_HCI_TX_TEST_POWER_MAX_SET 0x7F

/* Helper structure for Tx power parameter in the HCI Tx Test v4 command.
 * Previous parameter of this command is variable size so having separated structure
 * for this parameter helps in command parameters unpacking.
 */
struct bt_hci_cp_le_tx_test_v4_tx_power {
        int8_t tx_power;
} __packed;

#define BT_HCI_OP_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES BT_OP(BT_OGF_LE, 0x0089) /* 0x2089 */

struct bt_hci_rp_le_read_local_supported_capabilities {
        uint8_t  status;
        uint8_t  num_config_supported;
        uint16_t max_consecutive_procedures_supported;
        uint8_t  num_antennas_supported;
        uint8_t  max_antenna_paths_supported;
        uint8_t  roles_supported;
        uint8_t  modes_supported;
        uint8_t  rtt_capability;
        uint8_t  rtt_aa_only_n;
        uint8_t  rtt_sounding_n;
        uint8_t  rtt_random_payload_n;
        uint16_t nadm_sounding_capability;
        uint16_t nadm_random_capability;
        uint8_t  cs_sync_phys_supported;
        uint16_t subfeatures_supported;
        uint16_t t_ip1_times_supported;
        uint16_t t_ip2_times_supported;
        uint16_t t_fcs_times_supported;
        uint16_t t_pm_times_supported;
        uint8_t  t_sw_time_supported;
        uint8_t  tx_snr_capability;
} __packed;

#define BT_HCI_OP_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES_V2 BT_OP(BT_OGF_LE, 0x00A5) /* 0x20A5 */
#define BT_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES_V2_SUPPORTED(cmd) \
        BT_CMD_TEST(cmd, 49, 2)

struct bt_hci_rp_le_read_local_supported_capabilities_v2 {
        uint8_t  status;
        uint8_t  num_config_supported;
        uint16_t max_consecutive_procedures_supported;
        uint8_t  num_antennas_supported;
        uint8_t  max_antenna_paths_supported;
        uint8_t  roles_supported;
        uint8_t  modes_supported;
        uint8_t  rtt_capability;
        uint8_t  rtt_aa_only_n;
        uint8_t  rtt_sounding_n;
        uint8_t  rtt_random_payload_n;
        uint16_t nadm_sounding_capability;
        uint16_t nadm_random_capability;
        uint8_t  cs_sync_phys_supported;
        uint16_t subfeatures_supported;
        uint16_t t_ip1_times_supported;
        uint16_t t_ip2_times_supported;
        uint16_t t_fcs_times_supported;
        uint16_t t_pm_times_supported;
        uint8_t  t_sw_time_supported;
        uint8_t  tx_snr_capability;
        uint16_t  t_ip2_ipt_times_supported;
        uint8_t  t_sw_ipt_time_supported;
} __packed;

#define BT_HCI_OP_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES BT_OP(BT_OGF_LE, 0x008A) /* 0x208A */

struct bt_hci_cp_le_read_remote_supported_capabilities {
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_SUPPORTED_CAPABILITIES \
        BT_OP(BT_OGF_LE, 0x008B) /* 0x208B */

struct bt_hci_cp_le_write_cached_remote_supported_capabilities {
        uint16_t handle;
        uint8_t  num_config_supported;
        uint16_t max_consecutive_procedures_supported;
        uint8_t  num_antennas_supported;
        uint8_t  max_antenna_paths_supported;
        uint8_t  roles_supported;
        uint8_t  modes_supported;
        uint8_t  rtt_capability;
        uint8_t  rtt_aa_only_n;
        uint8_t  rtt_sounding_n;
        uint8_t  rtt_random_payload_n;
        uint16_t nadm_sounding_capability;
        uint16_t nadm_random_capability;
        uint8_t  cs_sync_phys_supported;
        uint16_t subfeatures_supported;
        uint16_t t_ip1_times_supported;
        uint16_t t_ip2_times_supported;
        uint16_t t_fcs_times_supported;
        uint16_t t_pm_times_supported;
        uint8_t  t_sw_time_supported;
        uint8_t  tx_snr_capability;
} __packed;

#define BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_SUPPORTED_CAPABILITIES_V2 \
        BT_OP(BT_OGF_LE, 0x00A6) /* 0x20A6 */

struct bt_hci_cp_le_write_cached_remote_supported_capabilities_v2 {
        uint16_t handle;
        uint8_t  num_config_supported;
        uint16_t max_consecutive_procedures_supported;
        uint8_t  num_antennas_supported;
        uint8_t  max_antenna_paths_supported;
        uint8_t  roles_supported;
        uint8_t  modes_supported;
        uint8_t  rtt_capability;
        uint8_t  rtt_aa_only_n;
        uint8_t  rtt_sounding_n;
        uint8_t  rtt_random_payload_n;
        uint16_t nadm_sounding_capability;
        uint16_t nadm_random_capability;
        uint8_t  cs_sync_phys_supported;
        uint16_t subfeatures_supported;
        uint16_t t_ip1_times_supported;
        uint16_t t_ip2_times_supported;
        uint16_t t_fcs_times_supported;
        uint16_t t_pm_times_supported;
        uint8_t  t_sw_time_supported;
        uint8_t  tx_snr_capability;
        uint16_t  t_ip2_ipt_times_supported;
        uint8_t  t_sw_ipt_time_supported;
} __packed;

#define BT_HCI_OP_LE_CS_SECURITY_ENABLE BT_OP(BT_OGF_LE, 0x008C) /* 0x208C */

struct bt_hci_cp_le_security_enable {
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_CS_SET_DEFAULT_SETTINGS BT_OP(BT_OGF_LE, 0x008D) /* 0x208D */

#define BT_HCI_OP_LE_CS_INITIATOR_ROLE_MASK BIT(0)
#define BT_HCI_OP_LE_CS_REFLECTOR_ROLE_MASK BIT(1)

#define BT_HCI_OP_LE_CS_MIN_MAX_TX_POWER -127
#define BT_HCI_OP_LE_CS_MAX_MAX_TX_POWER 20

#define BT_HCI_OP_LE_CS_ANTENNA_SEL_ONE   0x01
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_TWO   0x02
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_THREE 0x03
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_FOUR  0x04
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_REP   0xFE
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_NONE  0xFF

struct bt_hci_cp_le_cs_set_default_settings {
        uint16_t handle;
        uint8_t  role_enable;
        uint8_t  cs_sync_antenna_selection;
        int8_t   max_tx_power;
} __packed;

#define BT_HCI_OP_LE_CS_READ_REMOTE_FAE_TABLE BT_OP(BT_OGF_LE, 0x008E) /* 0x208E */

struct bt_hci_cp_le_read_remote_fae_table {
        uint16_t handle;
} __packed;

#define BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_FAE_TABLE BT_OP(BT_OGF_LE, 0x008F) /* 0x208F */

struct bt_hci_cp_le_write_cached_remote_fae_table {
        uint16_t handle;
        int8_t   remote_fae_table[72];
} __packed;

#define BT_HCI_OP_LE_CS_SET_CHANNEL_CLASSIFICATION BT_OP(BT_OGF_LE, 0x0092) /* 0x2092 */

#define BT_HCI_OP_LE_CS_SET_PROCEDURE_PARAMETERS BT_OP(BT_OGF_LE, 0x0093) /* 0x2093 */

#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_1M       0x01
#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_2M       0x02
#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_CODED_S8 0x03
#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_CODED_S2 0x04

struct bt_hci_cp_le_set_procedure_parameters {
        uint16_t handle;
        uint8_t  config_id;
        uint16_t max_procedure_len;
        uint16_t min_procedure_interval;
        uint16_t max_procedure_interval;
        uint16_t max_procedure_count;
        uint8_t  min_subevent_len[3];
        uint8_t  max_subevent_len[3];
        uint8_t  tone_antenna_config_selection;
        uint8_t  phy;
        uint8_t  tx_power_delta;
        uint8_t  preferred_peer_antenna;
        uint8_t  snr_control_initiator;
        uint8_t  snr_control_reflector;
} __packed;

#define BT_HCI_OP_LE_CS_PROCEDURE_ENABLE BT_OP(BT_OGF_LE, 0x0094) /* 0x2094 */

#define BT_HCI_OP_LE_CS_PROCEDURES_DISABLED 0x00
#define BT_HCI_OP_LE_CS_PROCEDURES_ENABLED  0x01

struct bt_hci_cp_le_procedure_enable {
        uint16_t handle;
        uint8_t  config_id;
        uint8_t  enable;
} __packed;

#define BT_HCI_OP_LE_CS_TEST BT_OP(BT_OGF_LE, 0x0095) /* 0x2095 */

#define BT_HCI_OP_LE_CS_MAIN_MODE_1 0x1
#define BT_HCI_OP_LE_CS_MAIN_MODE_2 0x2
#define BT_HCI_OP_LE_CS_MAIN_MODE_3 0x3

#define BT_HCI_OP_LE_CS_SUB_MODE_1 0x1
#define BT_HCI_OP_LE_CS_SUB_MODE_2 0x2
#define BT_HCI_OP_LE_CS_SUB_MODE_3 0x3
#define BT_HCI_OP_LE_CS_SUB_MODE_UNUSED 0xFF

#define BT_HCI_OP_LE_CS_INITIATOR_ROLE 0x0
#define BT_HCI_OP_LE_CS_REFLECTOR_ROLE 0x1

#define BT_HCI_OP_LE_CS_RTT_TYPE_AA_ONLY     0x0
#define BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_SOUND 0x1
#define BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_SOUND 0x2
#define BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_RAND  0x3
#define BT_HCI_OP_LE_CS_RTT_TYPE_64BIT_RAND  0x4
#define BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_RAND  0x5
#define BT_HCI_OP_LE_CS_RTT_TYPE_128BIT_RAND 0x6

#define BT_HCI_OP_LE_CS_CS_SYNC_1M     0x1
#define BT_HCI_OP_LE_CS_CS_SYNC_2M     0x2
#define BT_HCI_OP_LE_CS_CS_SYNC_2M_2BT 0x3

#define BT_HCI_OP_LE_CS_TEST_MINIMIZE_TX_POWER 0x7E
#define BT_HCI_OP_LE_CS_TEST_MAXIMIZE_TX_POWER 0x7F

#define BT_HCI_OP_LE_CS_ACI_0 0x0
#define BT_HCI_OP_LE_CS_ACI_1 0x1
#define BT_HCI_OP_LE_CS_ACI_2 0x2
#define BT_HCI_OP_LE_CS_ACI_3 0x3
#define BT_HCI_OP_LE_CS_ACI_4 0x4
#define BT_HCI_OP_LE_CS_ACI_5 0x5
#define BT_HCI_OP_LE_CS_ACI_6 0x6
#define BT_HCI_OP_LE_CS_ACI_7 0x7

#define BT_HCI_OP_LE_CS_SNR_18 0x0
#define BT_HCI_OP_LE_CS_SNR_21 0x1
#define BT_HCI_OP_LE_CS_SNR_24 0x2
#define BT_HCI_OP_LE_CS_SNR_27 0x3
#define BT_HCI_OP_LE_CS_SNR_30 0x4
#define BT_HCI_OP_LE_CS_SNR_NOT_USED 0xFF

#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_0_MASK BIT(0)
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_2_MASK BIT(2)
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_3_MASK BIT(3)
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_4_MASK BIT(4)
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_5_MASK BIT(5)
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_6_MASK BIT(6)
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_7_MASK BIT(7)
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_8_MASK BIT(8)
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_10_MASK BIT(10)

#define BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3B 0x0
#define BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3C 0x1

#define BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_HAT 0x0
#define BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_X   0x1

#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_NONE 0x0
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_INIT 0x1
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_REFL 0x2
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_BOTH 0x3
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_REPEAT 0x4

#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_00 0x0
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_01 0x1
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_02 0x2
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_03 0x3
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_04 0x4
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_05 0x5
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_06 0x6
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_07 0x7
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_08 0x8
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_09 0x9
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_10 0xA
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_11 0xB
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_12 0xC
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_13 0xD
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_14 0xE
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_15 0xF
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_16 0x10
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_17 0x11
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_18 0x12
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_19 0x13
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_20 0x14
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_21 0x15
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_22 0x16
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_23 0x17
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_LOOP 0xFF

#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_2_POSITION_NOT_PRESENT 0xFF

#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_0011 0x0
#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_1100 0x1
#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_LOOP 0x2

#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_PRBS9    0x00
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_11110000 0x01
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_10101010 0x02
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_PRBS15   0x03
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_11111111 0x04
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_00000000 0x05
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_00001111 0x06
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_01010101 0x07
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_USER     0x80

struct bt_hci_op_le_cs_test {
        uint8_t  main_mode_type;
        uint8_t  sub_mode_type;
        uint8_t  main_mode_repetition;
        uint8_t  mode_0_steps;
        uint8_t  role;
        uint8_t  rtt_type;
        uint8_t  cs_sync_phy;
        uint8_t  cs_sync_antenna_selection;
        uint8_t  subevent_len[3];
        uint16_t subevent_interval;
        uint8_t  max_num_subevents;
        uint8_t  transmit_power_level;
        uint8_t  t_ip1_time;
        uint8_t  t_ip2_time;
        uint8_t  t_fcs_time;
        uint8_t  t_pm_time;
        uint8_t  t_sw_time;
        uint8_t  tone_antenna_config_selection;
        uint8_t  cs_enhancements_1;
        uint8_t  snr_control_initiator;
        uint8_t  snr_control_reflector;
        uint16_t drbg_nonce;
        uint8_t  channel_map_repetition;
        uint16_t override_config;
        uint8_t  override_parameters_length;
        uint8_t  override_parameters_data[];
} __packed;

#define BT_HCI_OP_LE_CS_CREATE_CONFIG BT_OP(BT_OGF_LE, 0x0090) /* 0x2090 */

struct bt_hci_cp_le_cs_create_config {
        uint16_t handle;
        uint8_t  config_id;
        uint8_t  create_context;
        uint8_t  main_mode_type;
        uint8_t  sub_mode_type;
        uint8_t  min_main_mode_steps;
        uint8_t  max_main_mode_steps;
        uint8_t  main_mode_repetition;
        uint8_t  mode_0_steps;
        uint8_t  role;
        uint8_t  rtt_type;
        uint8_t  cs_sync_phy;
        uint8_t  channel_map[10];
        uint8_t  channel_map_repetition;
        uint8_t  channel_selection_type;
        uint8_t  ch3c_shape;
        uint8_t  ch3c_jump;
        uint8_t  cs_enhancements_1;
} __packed;

#define BT_HCI_OP_LE_CS_REMOVE_CONFIG BT_OP(BT_OGF_LE, 0x0091) /* 0x2091 */

struct bt_hci_cp_le_cs_remove_config {
        uint16_t handle;
        uint8_t  config_id;
} __packed;

#define BT_HCI_OP_LE_CS_TEST_END BT_OP(BT_OGF_LE, 0x0096) /* 0x2096 */

#define BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_1M_MASK    BIT(0)
#define BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_2M_MASK    BIT(1)
#define BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_CODED_MASK BIT(2)

#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_CP_MASK BIT(0)
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_PC_MASK BIT(1)
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MCES_MASK       BIT(2)
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_CIS_MASK    BIT(3)
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MSS_CIS_MASK    BIT(4)

#define BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST       (0)
#define BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER (1)
#define BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER             (2)

struct bt_hci_cp_le_frame_space_update {
        uint16_t handle;
        uint16_t frame_space_min;
        uint16_t frame_space_max;
        uint8_t  phys;
        uint16_t spacing_types;
} __packed;

#define BT_HCI_OP_LE_FRAME_SPACE_UPDATE BT_OP(BT_OGF_LE, 0x009D) /* 0x209D */

#define BT_HCI_LE_SCI_INTERVAL_MIN_125US   (0x0003U)
#define BT_HCI_LE_SCI_INTERVAL_MAX_125US   (0x7D00U)
#define BT_HCI_LE_SCI_INTERVAL_MIN_US      (375U)
#define BT_HCI_LE_SCI_INTERVAL_MAX_US      (4000000U)
#define BT_HCI_LE_SCI_INTERVAL_UNIT_US     (125U)

#define BT_HCI_LE_SCI_STRIDE_MIN_125US     (0x0001U)

#define BT_HCI_LE_MIN_SUPP_CONN_INT_MIN_US (375U)
#define BT_HCI_LE_MIN_SUPP_CONN_INT_MAX_US (7500U)

#define BT_HCI_LE_SCI_CE_LEN_MIN_125US     (0x0001U)
#define BT_HCI_LE_SCI_CE_LEN_MAX_125US     (0x3E7FU)

struct bt_hci_le_read_min_supported_conn_interval_group {
        uint16_t group_min;
        uint16_t group_max;
        uint16_t group_stride;
} __packed;

struct bt_hci_op_le_read_min_supported_conn_interval {
        uint8_t status;
        uint8_t min_supported_conn_interval;
        uint8_t num_groups;
        struct bt_hci_le_read_min_supported_conn_interval_group groups[];
} __packed;

#define BT_HCI_OP_LE_READ_MIN_SUPPORTED_CONN_INTERVAL                                    \
        BT_OP(BT_OGF_LE, 0x00A3) /* 0x20A3 */

struct bt_hci_op_le_set_default_rate_parameters {
        uint16_t conn_interval_min;
        uint16_t conn_interval_max;
        uint16_t subrate_min;
        uint16_t subrate_max;
        uint16_t max_latency;
        uint16_t continuation_number;
        uint16_t supervision_timeout;
        uint16_t min_ce_len;
        uint16_t max_ce_len;
} __packed;

#define BT_HCI_OP_LE_SET_DEFAULT_RATE_PARAMETERS BT_OP(BT_OGF_LE, 0x00A2) /* 0x20A2 */

struct bt_hci_op_le_connection_rate_request {
        uint16_t handle;
        uint16_t conn_interval_min;
        uint16_t conn_interval_max;
        uint16_t subrate_min;
        uint16_t subrate_max;
        uint16_t max_latency;
        uint16_t continuation_number;
        uint16_t supervision_timeout;
        uint16_t min_ce_len;
        uint16_t max_ce_len;
} __packed;

#define BT_HCI_OP_LE_CONNECTION_RATE_REQUEST BT_OP(BT_OGF_LE, 0x00A1) /* 0x20A1 */

/* Event definitions */

#define BT_HCI_EVT_UNKNOWN                      0x00
#define BT_HCI_EVT_VENDOR                       0xff

#define BT_HCI_EVT_INQUIRY_COMPLETE             0x01
struct bt_hci_evt_inquiry_complete {
        uint8_t status;
} __packed;

#define BT_HCI_EVT_CONN_COMPLETE                0x03
struct bt_hci_evt_conn_complete {
        uint8_t   status;
        uint16_t  handle;
        bt_addr_t bdaddr;
        uint8_t   link_type;
        uint8_t   encr_enabled;
} __packed;

#define BT_HCI_EVT_CONN_REQUEST                 0x04
struct bt_hci_evt_conn_request {
        bt_addr_t bdaddr;
        uint8_t   dev_class[3];
        uint8_t   link_type;
} __packed;

#define BT_HCI_EVT_DISCONN_COMPLETE             0x05
struct bt_hci_evt_disconn_complete {
        uint8_t  status;
        uint16_t handle;
        uint8_t  reason;
} __packed;

#define BT_HCI_EVT_AUTH_COMPLETE                0x06
struct bt_hci_evt_auth_complete {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_EVT_REMOTE_NAME_REQ_COMPLETE     0x07
struct bt_hci_evt_remote_name_req_complete {
        uint8_t   status;
        bt_addr_t bdaddr;
        uint8_t   name[248];
} __packed;

/* Encryption Value */
#define BT_HCI_ENCRYPTION_OFF           0x00
#define BT_HCI_ENCRYPTION_ON_LE_AES_CCM 0x01
#define BT_HCI_ENCRYPTION_ON_BR_E0      0x01
#define BT_HCI_ENCRYPTION_ON_BR_AES_CCM 0x02

#define BT_HCI_EVT_ENCRYPT_CHANGE               0x08
struct bt_hci_evt_encrypt_change {
        uint8_t  status;
        uint16_t handle;
        uint8_t  encrypt;
} __packed;

#define BT_HCI_EVT_REMOTE_FEATURES              0x0b
struct bt_hci_evt_remote_features {
        uint8_t  status;
        uint16_t handle;
        uint8_t  features[8];
} __packed;

#define BT_HCI_EVT_REMOTE_VERSION_INFO          0x0c
struct bt_hci_evt_remote_version_info {
        uint8_t  status;
        uint16_t handle;
        uint8_t  version;
        uint16_t manufacturer;
        uint16_t subversion;
} __packed;

#define BT_HCI_EVT_CMD_COMPLETE                 0x0e
struct bt_hci_evt_cmd_complete {
        uint8_t  ncmd;
        uint16_t opcode;
} __packed;

struct bt_hci_evt_cc_status {
        uint8_t  status;
} __packed;

#define BT_HCI_EVT_CMD_STATUS                   0x0f
struct bt_hci_evt_cmd_status {
        uint8_t  status;
        uint8_t  ncmd;
        uint16_t opcode;
} __packed;

#define BT_HCI_EVT_HARDWARE_ERROR               0x10
struct bt_hci_evt_hardware_error {
        uint8_t  hardware_code;
} __packed;

#define BT_HCI_EVT_ROLE_CHANGE                  0x12
struct bt_hci_evt_role_change {
        uint8_t   status;
        bt_addr_t bdaddr;
        uint8_t   role;
} __packed;

#define BT_HCI_EVT_NUM_COMPLETED_PACKETS        0x13
struct bt_hci_evt_num_completed_packets {
        uint8_t  num_handles;
        struct bt_hci_handle_count h[0];
} __packed;

/* Current mode */
#define BT_ACTIVE_MODE 0x00
#define BT_HOLD_MODE   0x01
#define BT_SNIFF_MODE  0x02

#define BT_HCI_EVT_MODE_CHANGE                  0x14
struct bt_hci_evt_mode_change {
        uint8_t  status;
        uint16_t handle;
        uint8_t  mode;
        uint16_t interval;
} __packed;

#define BT_HCI_EVT_PIN_CODE_REQ                 0x16
struct bt_hci_evt_pin_code_req {
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_EVT_LINK_KEY_REQ                 0x17
struct bt_hci_evt_link_key_req {
        bt_addr_t bdaddr;
} __packed;

/* Link Key types */
#define BT_LK_COMBINATION                       0x00
#define BT_LK_LOCAL_UNIT                        0x01
#define BT_LK_REMOTE_UNIT                       0x02
#define BT_LK_DEBUG_COMBINATION                 0x03
#define BT_LK_UNAUTH_COMBINATION_P192           0x04
#define BT_LK_AUTH_COMBINATION_P192             0x05
#define BT_LK_CHANGED_COMBINATION               0x06
#define BT_LK_UNAUTH_COMBINATION_P256           0x07
#define BT_LK_AUTH_COMBINATION_P256             0x08

#define BT_HCI_EVT_LINK_KEY_NOTIFY              0x18
struct bt_hci_evt_link_key_notify {
        bt_addr_t bdaddr;
        uint8_t   link_key[16];
        uint8_t   key_type;
} __packed;

/* Overflow link types */
#define BT_OVERFLOW_LINK_SYNCH                  0x00
#define BT_OVERFLOW_LINK_ACL                    0x01
#define BT_OVERFLOW_LINK_ISO                    0x02

#define BT_HCI_EVT_DATA_BUF_OVERFLOW            0x1a
struct bt_hci_evt_data_buf_overflow {
        uint8_t  link_type;
} __packed;

#define BT_HCI_EVT_CONN_PKT_TYPE_CHANGED        0x1d
struct bt_hci_evt_conn_pkt_type_changed {
        uint8_t  status;
        uint16_t handle;
        uint16_t packet_type;
} __packed;

#define BT_HCI_EVT_INQUIRY_RESULT_WITH_RSSI     0x22
struct bt_hci_evt_inquiry_result_with_rssi {
        bt_addr_t addr;
        uint8_t   pscan_rep_mode;
        uint8_t   reserved;
        uint8_t   cod[3];
        uint16_t  clock_offset;
        int8_t    rssi;
} __packed;

#define BT_HCI_EVT_REMOTE_EXT_FEATURES          0x23
struct bt_hci_evt_remote_ext_features {
        uint8_t  status;
        uint16_t handle;
        uint8_t  page;
        uint8_t  max_page;
        uint8_t  features[8];
} __packed;

#define BT_HCI_EVT_LE_PER_ADV_SYNC_ESTABLISHED_V2 0x24
struct bt_hci_evt_le_per_adv_sync_established_v2 {
        uint8_t      status;
        uint16_t     handle;
        uint8_t      sid;
        bt_addr_le_t adv_addr;
        uint8_t      phy;
        uint16_t     interval;
        uint8_t      clock_accuracy;
        uint8_t      num_subevents;
        uint8_t      subevent_interval;
        uint8_t      response_slot_delay;
        uint8_t      response_slot_spacing;
} __packed;

#define BT_HCI_EVT_LE_PER_ADVERTISING_REPORT_V2 0x25
struct bt_hci_evt_le_per_advertising_report_v2 {
        uint16_t handle;
        int8_t   tx_power;
        int8_t   rssi;
        uint8_t  cte_type;
        uint16_t periodic_event_counter;
        uint8_t  subevent;
        uint8_t  data_status;
        uint8_t  length;
        uint8_t  data[0];
} __packed;

#define BT_HCI_EVT_LE_PAST_RECEIVED_V2 0x26
struct bt_hci_evt_le_past_received_v2 {
        uint8_t      status;
        uint16_t     conn_handle;
        uint16_t     service_data;
        uint16_t     sync_handle;
        uint8_t      adv_sid;
        bt_addr_le_t addr;
        uint8_t      phy;
        uint16_t     interval;
        uint8_t      clock_accuracy;
        uint8_t      num_subevents;
        uint8_t      subevent_interval;
        uint8_t      response_slot_delay;
        uint8_t      response_slot_spacing;
} __packed;

#define BT_HCI_EVT_LE_PER_ADV_SUBEVENT_DATA_REQUEST 0x27
struct bt_hci_evt_le_per_adv_subevent_data_request {
        uint8_t adv_handle;
        uint8_t subevent_start;
        uint8_t subevent_data_count;
} __packed;

#define BT_HCI_EVT_LE_PER_ADV_RESPONSE_REPORT 0x28

struct bt_hci_evt_le_per_adv_response {
        int8_t  tx_power;
        int8_t  rssi;
        uint8_t cte_type;
        uint8_t response_slot;
        uint8_t data_status;
        uint8_t data_length;
        uint8_t data[0];
} __packed;

struct bt_hci_evt_le_per_adv_response_report {
        uint8_t adv_handle;
        uint8_t subevent;
        uint8_t tx_status;
        uint8_t num_responses;
        struct bt_hci_evt_le_per_adv_response responses[0];
} __packed;

#define BT_HCI_EVT_LE_ENH_CONN_COMPLETE_V2 0x29
struct bt_hci_evt_le_enh_conn_complete_v2 {
        uint8_t      status;
        uint16_t     handle;
        uint8_t      role;
        bt_addr_le_t peer_addr;
        bt_addr_t    local_rpa;
        bt_addr_t    peer_rpa;
        uint16_t     interval;
        uint16_t     latency;
        uint16_t     supv_timeout;
        uint8_t      clock_accuracy;
        uint8_t      adv_handle;
        uint16_t     sync_handle;
} __packed;

#define BT_HCI_EVT_SYNC_CONN_COMPLETE           0x2c
struct bt_hci_evt_sync_conn_complete {
        uint8_t    status;
        uint16_t   handle;
        bt_addr_t  bdaddr;
        uint8_t    link_type;
        uint8_t    tx_interval;
        uint8_t    retansmission_window;
        uint16_t   rx_pkt_length;
        uint16_t   tx_pkt_length;
        uint8_t    air_mode;
} __packed;

#define BT_HCI_EVT_EXTENDED_INQUIRY_RESULT      0x2f
struct bt_hci_evt_extended_inquiry_result {
        uint8_t    num_reports;
        bt_addr_t  addr;
        uint8_t    pscan_rep_mode;
        uint8_t    reserved;
        uint8_t    cod[3];
        uint16_t   clock_offset;
        int8_t     rssi;
        uint8_t    eir[240];
} __packed;

#define BT_HCI_EVT_ENCRYPT_KEY_REFRESH_COMPLETE 0x30
struct bt_hci_evt_encrypt_key_refresh_complete {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_EVT_IO_CAPA_REQ                  0x31
struct bt_hci_evt_io_capa_req {
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_EVT_IO_CAPA_RESP                 0x32
struct bt_hci_evt_io_capa_resp {
        bt_addr_t bdaddr;
        uint8_t   capability;
        uint8_t   oob_data;
        uint8_t   authentication;
} __packed;

#define BT_HCI_EVT_USER_CONFIRM_REQ             0x33
struct bt_hci_evt_user_confirm_req {
        bt_addr_t bdaddr;
        uint32_t  passkey;
} __packed;

#define BT_HCI_EVT_USER_PASSKEY_REQ             0x34
struct bt_hci_evt_user_passkey_req {
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_EVT_SSP_COMPLETE                 0x36
struct bt_hci_evt_ssp_complete {
        uint8_t   status;
        bt_addr_t bdaddr;
} __packed;

#define BT_HCI_EVT_USER_PASSKEY_NOTIFY          0x3b
struct bt_hci_evt_user_passkey_notify {
        bt_addr_t bdaddr;
        uint32_t  passkey;
} __packed;

#define BT_HCI_EVT_LE_META_EVENT                0x3e
struct bt_hci_evt_le_meta_event {
        uint8_t  subevent;
        uint8_t  data[];
} __packed;

#define BT_HCI_EVT_AUTH_PAYLOAD_TIMEOUT_EXP     0x57
struct bt_hci_evt_auth_payload_timeout_exp {
        uint16_t handle;
} __packed;

#define BT_HCI_ROLE_CENTRAL                     0x00
#define BT_HCI_ROLE_PERIPHERAL                  0x01

#define BT_HCI_EVT_LE_CONN_COMPLETE             0x01
struct bt_hci_evt_le_conn_complete {
        uint8_t      status;
        uint16_t     handle;
        uint8_t      role;
        bt_addr_le_t peer_addr;
        uint16_t     interval;
        uint16_t     latency;
        uint16_t     supv_timeout;
        uint8_t      clock_accuracy;
} __packed;

#define BT_HCI_LE_RSSI_NOT_AVAILABLE            0x7F

#define BT_HCI_EVT_LE_ADVERTISING_REPORT        0x02
struct bt_hci_evt_le_advertising_info {
        uint8_t      evt_type;
        bt_addr_le_t addr;
        uint8_t      length;
        uint8_t      data[0];
} __packed;
struct bt_hci_evt_le_advertising_report {
        uint8_t num_reports;
        struct bt_hci_evt_le_advertising_info adv_info[0];
} __packed;

#define BT_HCI_LE_INTERVAL_MIN            0x0006
#define BT_HCI_LE_INTERVAL_MAX            0x0c80
#define BT_HCI_LE_PERIPHERAL_LATENCY_MIN (0x0000U)
#define BT_HCI_LE_PERIPHERAL_LATENCY_MAX  0x01f3
#define BT_HCI_LE_SUPERVISION_TIMEOUT_MIN 0x000a
#define BT_HCI_LE_SUPERVISION_TIMEOUT_MAX 0x0c80
/* Deprecated misspelled aliases: use BT_HCI_LE_SUPERVISION_TIMEOUT_{MIN,MAX} instead. */
#define BT_HCI_LE_SUPERVISON_TIMEOUT_MIN BT_HCI_LE_SUPERVISION_TIMEOUT_MIN __DEPRECATED_MACRO
#define BT_HCI_LE_SUPERVISON_TIMEOUT_MAX BT_HCI_LE_SUPERVISION_TIMEOUT_MAX __DEPRECATED_MACRO

#define BT_HCI_LE_INTERVAL_UNIT_US (1250U)

#define BT_HCI_EVT_LE_CONN_UPDATE_COMPLETE      0x03
struct bt_hci_evt_le_conn_update_complete {
        uint8_t  status;
        uint16_t handle;
        uint16_t interval;
        uint16_t latency;
        uint16_t supv_timeout;
} __packed;

#define BT_HCI_EVT_LE_REMOTE_FEAT_COMPLETE      0x04
struct bt_hci_evt_le_remote_feat_complete {
        uint8_t  status;
        uint16_t handle;
        uint8_t  features[8];
} __packed;

#define BT_HCI_EVT_LE_LTK_REQUEST               0x05
struct bt_hci_evt_le_ltk_request {
        uint16_t handle;
        uint8_t  rand[8];
        uint8_t  ediv[2];
} __packed;

#define BT_HCI_EVT_LE_CONN_PARAM_REQ            0x06
struct bt_hci_evt_le_conn_param_req {
        uint16_t handle;
        uint16_t interval_min;
        uint16_t interval_max;
        uint16_t latency;
        uint16_t timeout;
} __packed;

#define BT_HCI_EVT_LE_DATA_LEN_CHANGE           0x07
struct bt_hci_evt_le_data_len_change {
        uint16_t handle;
        uint16_t max_tx_octets;
        uint16_t max_tx_time;
        uint16_t max_rx_octets;
        uint16_t max_rx_time;
} __packed;

#define BT_HCI_EVT_LE_P256_PUBLIC_KEY_COMPLETE  0x08
struct bt_hci_evt_le_p256_public_key_complete {
        uint8_t status;
        uint8_t key[64];
} __packed;

#define BT_HCI_EVT_LE_GENERATE_DHKEY_COMPLETE   0x09
struct bt_hci_evt_le_generate_dhkey_complete {
        uint8_t status;
        uint8_t dhkey[32];
} __packed;

#define BT_HCI_EVT_LE_ENH_CONN_COMPLETE         0x0a
struct bt_hci_evt_le_enh_conn_complete {
        uint8_t      status;
        uint16_t     handle;
        uint8_t      role;
        bt_addr_le_t peer_addr;
        bt_addr_t    local_rpa;
        bt_addr_t    peer_rpa;
        uint16_t     interval;
        uint16_t     latency;
        uint16_t     supv_timeout;
        uint8_t      clock_accuracy;
} __packed;

#define BT_HCI_EVT_LE_DIRECT_ADV_REPORT         0x0b
struct bt_hci_evt_le_direct_adv_info {
        uint8_t      evt_type;
        bt_addr_le_t addr;
        bt_addr_le_t dir_addr;
        int8_t       rssi;
} __packed;
struct bt_hci_evt_le_direct_adv_report {
        uint8_t num_reports;
        struct bt_hci_evt_le_direct_adv_info direct_adv_info[0];
} __packed;

#define BT_HCI_EVT_LE_PHY_UPDATE_COMPLETE       0x0c
struct bt_hci_evt_le_phy_update_complete {
        uint8_t  status;
        uint16_t handle;
        uint8_t  tx_phy;
        uint8_t  rx_phy;
} __packed;

#define BT_HCI_EVT_LE_EXT_ADVERTISING_REPORT    0x0d

#define BT_HCI_LE_ADV_EVT_TYPE_CONN                 BIT(0)
#define BT_HCI_LE_ADV_EVT_TYPE_SCAN                 BIT(1)
#define BT_HCI_LE_ADV_EVT_TYPE_DIRECT               BIT(2)
#define BT_HCI_LE_ADV_EVT_TYPE_SCAN_RSP             BIT(3)
#define BT_HCI_LE_ADV_EVT_TYPE_LEGACY               BIT(4)

#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS(ev_type) (((ev_type) >> 5) & 0x03)
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_COMPLETE   0
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_PARTIAL    1
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_INCOMPLETE 2
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_RX_FAILED  0xFF

/* Advertising Coding Selection extended advertising report PHY values.
 * Only used when Kconfig BT_EXT_ADV_CODING_SELECTION is enabled.
 */
#define BT_HCI_LE_ADV_EVT_PHY_1M                0x01
#define BT_HCI_LE_ADV_EVT_PHY_2M                0x02
#define BT_HCI_LE_ADV_EVT_PHY_CODED_S8          0x03
#define BT_HCI_LE_ADV_EVT_PHY_CODED_S2          0x04

struct bt_hci_evt_le_ext_advertising_info {
        uint16_t     evt_type;
        bt_addr_le_t addr;
        uint8_t      prim_phy;
        uint8_t      sec_phy;
        uint8_t      sid;
        int8_t       tx_power;
        int8_t       rssi;
        uint16_t     interval;
        bt_addr_le_t direct_addr;
        uint8_t      length;
        uint8_t      data[0];
} __packed;

#define BT_HCI_LE_EXT_ADV_REPORT_MAX_NUM_REPORTS 0x0a
struct bt_hci_evt_le_ext_advertising_report {
        uint8_t num_reports;
        struct bt_hci_evt_le_ext_advertising_info adv_info[0];
} __packed;

#define BT_HCI_EVT_LE_PER_ADV_SYNC_ESTABLISHED  0x0e
struct bt_hci_evt_le_per_adv_sync_established {
        uint8_t      status;
        uint16_t     handle;
        uint8_t      sid;
        bt_addr_le_t adv_addr;
        uint8_t      phy;
        uint16_t     interval;
        uint8_t      clock_accuracy;
} __packed;

#define BT_HCI_EVT_LE_PER_ADVERTISING_REPORT    0x0f
struct bt_hci_evt_le_per_advertising_report {
        uint16_t handle;
        int8_t   tx_power;
        int8_t   rssi;
        uint8_t  cte_type;
        uint8_t  data_status;
        uint8_t  length;
        uint8_t  data[0];
} __packed;

#define BT_HCI_EVT_LE_PER_ADV_SYNC_LOST         0x10
struct bt_hci_evt_le_per_adv_sync_lost {
        uint16_t handle;
} __packed;

#define BT_HCI_EVT_LE_SCAN_TIMEOUT              0x11

#define BT_HCI_EVT_LE_ADV_SET_TERMINATED        0x12
struct bt_hci_evt_le_adv_set_terminated {
        uint8_t  status;
        uint8_t  adv_handle;
        uint16_t conn_handle;
        uint8_t  num_completed_ext_adv_evts;
} __packed;

#define BT_HCI_EVT_LE_SCAN_REQ_RECEIVED         0x13
struct bt_hci_evt_le_scan_req_received {
        uint8_t      handle;
        bt_addr_le_t addr;
} __packed;

#define BT_HCI_LE_CHAN_SEL_ALGO_1               0x00
#define BT_HCI_LE_CHAN_SEL_ALGO_2               0x01

#define BT_HCI_EVT_LE_CHAN_SEL_ALGO             0x14
struct bt_hci_evt_le_chan_sel_algo {
        uint16_t handle;
        uint8_t  chan_sel_algo;
} __packed;

#define BT_HCI_LE_CTE_CRC_OK                    0x0
#define BT_HCI_LE_CTE_CRC_ERR_CTE_BASED_TIME    0x1
#define BT_HCI_LE_CTE_CRC_ERR_CTE_BASED_OTHER   0x2
#define BT_HCI_LE_CTE_INSUFFICIENT_RESOURCES    0xFF

#define B_HCI_LE_CTE_REPORT_SAMPLE_COUNT_MIN    0x9
#define B_HCI_LE_CTE_REPORT_SAMPLE_COUNT_MAX    0x52

#define BT_HCI_LE_CTE_REPORT_NO_VALID_SAMPLE    0x80

#define BT_HCI_EVT_LE_CONNECTIONLESS_IQ_REPORT  0x15
struct bt_hci_le_iq_sample {
        int8_t i;
        int8_t q;
};

struct bt_hci_evt_le_connectionless_iq_report {
        uint16_t sync_handle;
        uint8_t  chan_idx;
        int16_t  rssi;
        uint8_t  rssi_ant_id;
        uint8_t  cte_type;
        uint8_t  slot_durations;
        uint8_t  packet_status;
        uint16_t per_evt_counter;
        uint8_t  sample_count;
        struct bt_hci_le_iq_sample sample[0];
} __packed;

#define BT_HCI_EVT_LE_CONNECTION_IQ_REPORT      0x16
struct bt_hci_evt_le_connection_iq_report {
        uint16_t conn_handle;
        uint8_t  rx_phy;
        uint8_t  data_chan_idx;
        int16_t  rssi;
        uint8_t  rssi_ant_id;
        uint8_t  cte_type;
        uint8_t  slot_durations;
        uint8_t  packet_status;
        uint16_t conn_evt_counter;
        uint8_t  sample_count;
        struct bt_hci_le_iq_sample sample[0];
} __packed;

#define BT_HCI_CTE_REQ_STATUS_RSP_WITHOUT_CTE  0x0

#define BT_HCI_EVT_LE_CTE_REQUEST_FAILED       0x17
struct bt_hci_evt_le_cte_req_failed {
        /* According to BT 5.3 Core Spec the status field may have following
         * values:
         * - BT_HCI_CTE_REQ_STATUS_RSP_WITHOUT_CTE when received LL_CTE_RSP_PDU without CTE.
         * - Other Controller error code for peer rejected request.
         */
        uint8_t  status;
        uint16_t conn_handle;
} __packed;

#define BT_HCI_EVT_LE_PAST_RECEIVED                0x18
struct bt_hci_evt_le_past_received {
        uint8_t      status;
        uint16_t     conn_handle;
        uint16_t     service_data;
        uint16_t     sync_handle;
        uint8_t      adv_sid;
        bt_addr_le_t addr;
        uint8_t      phy;
        uint16_t     interval;
        uint8_t      clock_accuracy;
} __packed;

#define BT_HCI_LE_CIG_SYNC_DELAY_MIN           0x0000F2U
#define BT_HCI_LE_CIG_SYNC_DELAY_MAX           0x7FFFFFU
#define BT_HCI_LE_CIS_SYNC_DELAY_MIN           0x0000F2U
#define BT_HCI_LE_CIS_SYNC_DELAY_MAX           0x7FFFFFU
#define BT_HCI_LE_TRANSPORT_LATENCY_C_TO_P_MIN 0x0000F2U
#define BT_HCI_LE_TRANSPORT_LATENCY_C_TO_P_MAX 0x7FFFFFU
#define BT_HCI_LE_TRANSPORT_LATENCY_P_TO_C_MIN 0x0000F2U
#define BT_HCI_LE_TRANSPORT_LATENCY_P_TO_C_MAX 0x7FFFFFU

#define BT_HCI_EVT_LE_CIS_ESTABLISHED           0x19
struct bt_hci_evt_le_cis_established {
        uint8_t  status;
        uint16_t conn_handle;
        uint8_t  cig_sync_delay[3];
        uint8_t  cis_sync_delay[3];
        uint8_t  c_latency[3];
        uint8_t  p_latency[3];
        uint8_t  c_phy;
        uint8_t  p_phy;
        uint8_t  nse;
        uint8_t  c_bn;
        uint8_t  p_bn;
        uint8_t  c_ft;
        uint8_t  p_ft;
        uint16_t c_max_pdu;
        uint16_t p_max_pdu;
        uint16_t interval;
} __packed;

#define BT_HCI_EVT_LE_CIS_REQ                   0x1a
struct bt_hci_evt_le_cis_req {
        uint16_t acl_handle;
        uint16_t cis_handle;
        uint8_t  cig_id;
        uint8_t  cis_id;
} __packed;

#define BT_HCI_LE_BIG_HANDLE_MIN            0x00U
#define BT_HCI_LE_BIG_HANDLE_MAX            0xEFU
#define BT_HCI_LE_BIG_SYNC_DELAY_MIN        0x000030U
#define BT_HCI_LE_BIG_SYNC_DELAY_MAX        0x7FFFFFU
#define BT_HCI_LE_TRANSPORT_LATENCY_BIG_MIN 0x000030U
#define BT_HCI_LE_TRANSPORT_LATENCY_BIG_MAX 0x7FFFFFU

#define BT_HCI_EVT_LE_BIG_COMPLETE              0x1b
struct bt_hci_evt_le_big_complete {
        uint8_t  status;
        uint8_t  big_handle;
        uint8_t  sync_delay[3];
        uint8_t  latency[3];
        uint8_t  phy;
        uint8_t  nse;
        uint8_t  bn;
        uint8_t  pto;
        uint8_t  irc;
        uint16_t max_pdu;
        uint16_t iso_interval;
        uint8_t  num_bis;
        uint16_t handle[0];
} __packed;

#define BT_HCI_EVT_LE_BIG_TERMINATE             0x1c
struct bt_hci_evt_le_big_terminate {
        uint8_t  big_handle;
        uint8_t  reason;
} __packed;

#define BT_HCI_EVT_LE_BIG_SYNC_ESTABLISHED      0x1d
struct bt_hci_evt_le_big_sync_established {
        uint8_t  status;
        uint8_t  big_handle;
        uint8_t  latency[3];
        uint8_t  nse;
        uint8_t  bn;
        uint8_t  pto;
        uint8_t  irc;
        uint16_t max_pdu;
        uint16_t iso_interval;
        uint8_t  num_bis;
        uint16_t handle[0];
} __packed;

#define BT_HCI_EVT_LE_BIG_SYNC_LOST             0x1e
struct bt_hci_evt_le_big_sync_lost {
        uint8_t  big_handle;
        uint8_t  reason;
} __packed;

#define BT_HCI_EVT_LE_REQ_PEER_SCA_COMPLETE     0x1f
struct bt_hci_evt_le_req_peer_sca_complete {
        uint8_t  status;
        uint16_t handle;
        uint8_t  sca;
} __packed;

#define BT_HCI_LE_ZONE_ENTERED_LOW      0x0
#define BT_HCI_LE_ZONE_ENTERED_MIDDLE   0x1
#define BT_HCI_LE_ZONE_ENTERED_HIGH     0x2
#define BT_HCI_LE_PATH_LOSS_UNAVAILABLE 0xFF

#define BT_HCI_EVT_LE_PATH_LOSS_THRESHOLD                   0x20
struct bt_hci_evt_le_path_loss_threshold {
        uint16_t handle;
        uint8_t  current_path_loss;
        uint8_t  zone_entered;
} __packed;

/* Local Transmit power changed. */
#define BT_HCI_LE_TX_POWER_REPORT_REASON_LOCAL_CHANGED         0x00
/* Remote Transmit power changed. */
#define BT_HCI_LE_TX_POWER_REPORT_REASON_REMOTE_CHANGED        0x01
/* HCI_LE_Read_Remote_Transmit_Power_Level command completed. */
#define BT_HCI_LE_TX_POWER_REPORT_REASON_READ_REMOTE_COMPLETED 0x02

#define BT_HCI_EVT_LE_TRANSMIT_POWER_REPORT     0x21
struct bt_hci_evt_le_transmit_power_report {
        uint8_t  status;
        uint16_t handle;
        uint8_t  reason;
        uint8_t  phy;
        int8_t   tx_power_level;
        uint8_t  tx_power_level_flag;
        int8_t   delta;
} __packed;

#define BT_HCI_EVT_LE_BIGINFO_ADV_REPORT        0x22
struct bt_hci_evt_le_biginfo_adv_report {
        uint16_t sync_handle;
        uint8_t  num_bis;
        uint8_t  nse;
        uint16_t iso_interval;
        uint8_t  bn;
        uint8_t  pto;
        uint8_t  irc;
        uint16_t max_pdu;
        uint8_t  sdu_interval[3];
        uint16_t max_sdu;
        uint8_t  phy;
        uint8_t  framing;
        uint8_t  encryption;
} __packed;

#define BT_HCI_LE_SUBRATE_FACTOR_MIN   0x0001
#define BT_HCI_LE_SUBRATE_FACTOR_MAX   0x01f4
#define BT_HCI_LE_CONTINUATION_NUM_MIN (0x0000U)
#define BT_HCI_LE_CONTINUATION_NUM_MAX 0x01f3

#define BT_HCI_EVT_LE_SUBRATE_CHANGE            0x23
struct bt_hci_evt_le_subrate_change {
        uint8_t  status;
        uint16_t handle;
        uint16_t subrate_factor;
        uint16_t peripheral_latency;
        uint16_t continuation_number;
        uint16_t supervision_timeout;
} __packed;

#define BT_HCI_EVT_LE_CIS_ESTABLISHED_V2 0x2a
struct bt_hci_evt_le_cis_established_v2 {
        uint8_t  status;
        uint16_t conn_handle;
        uint8_t  cig_sync_delay[3];
        uint8_t  cis_sync_delay[3];
        uint8_t  c_latency[3];
        uint8_t  p_latency[3];
        uint8_t  c_phy;
        uint8_t  p_phy;
        uint8_t  nse;
        uint8_t  c_bn;
        uint8_t  p_bn;
        uint8_t  c_ft;
        uint8_t  p_ft;
        uint16_t c_max_pdu;
        uint16_t p_max_pdu;
        uint16_t interval;
        uint8_t  sub_interval[3];
        uint16_t c_max_sdu;
        uint16_t p_max_sdu;
        uint8_t  c_sdu_interval[3];
        uint8_t  p_sdu_interval[3];
        uint8_t  framing;
} __packed;

#define BT_HCI_EVT_LE_READ_ALL_REMOTE_FEAT_COMPLETE 0x2b

#define BT_HCI_LE_FEATURE_PAGE_MAX          10
#define BT_HCI_LE_BYTES_PER_FEATURE_PAGE    24
#define BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE 8

struct bt_hci_evt_le_read_all_remote_feat_complete {
        uint8_t  status;
        uint16_t handle;
        uint8_t  max_remote_page;
        uint8_t  max_valid_page;
        uint8_t  features[248];
} __packed;

#define BT_HCI_LE_CS_INITIATOR_ROLE_MASK BIT(0)
#define BT_HCI_LE_CS_REFLECTOR_ROLE_MASK BIT(1)

#define BT_HCI_LE_CS_MODES_SUPPORTED_MODE_3_MASK BIT(0)

#define BT_HCI_LE_CS_RTT_AA_ONLY_N_10NS_MASK        BIT(0)
#define BT_HCI_LE_CS_RTT_SOUNDING_N_10NS_MASK       BIT(1)
#define BT_HCI_LE_CS_RTT_RANDOM_PAYLOAD_N_10NS_MASK BIT(2)

#define BT_HCI_LE_CS_NADM_SOUNDING_CAPABILITY_PHASE_BASED_MASK BIT(0)
#define BT_HCI_LE_CS_NADM_RANDOM_CAPABILITY_PHASE_BASED_MASK BIT(0)

#define BT_HCI_LE_CS_SYNC_PHYS_2M_MASK BIT(1)
#define BT_HCI_LE_CS_SYNC_PHYS_2M_2BT_MASK BIT(2)

#define BT_HCI_LE_CS_SUBFEATURE_NO_TX_FAE_MASK BIT(1)
#define BT_HCI_LE_CS_SUBFEATURE_CHSEL_ALG_3C_MASK BIT(2)
#define BT_HCI_LE_CS_SUBFEATURE_PBR_FROM_RTT_SOUNDING_SEQ_MASK BIT(3)
#define BT_HCI_LE_CS_SUBFEATURE_CS_IPT_REFLECTOR_MASK BIT(4)

#define BT_HCI_LE_CS_T_IP1_TIME_10US_MASK BIT(0)
#define BT_HCI_LE_CS_T_IP1_TIME_20US_MASK BIT(1)
#define BT_HCI_LE_CS_T_IP1_TIME_30US_MASK BIT(2)
#define BT_HCI_LE_CS_T_IP1_TIME_40US_MASK BIT(3)
#define BT_HCI_LE_CS_T_IP1_TIME_50US_MASK BIT(4)
#define BT_HCI_LE_CS_T_IP1_TIME_60US_MASK BIT(5)
#define BT_HCI_LE_CS_T_IP1_TIME_80US_MASK BIT(6)

#define BT_HCI_LE_CS_T_IP2_TIME_10US_MASK BIT(0)
#define BT_HCI_LE_CS_T_IP2_TIME_20US_MASK BIT(1)
#define BT_HCI_LE_CS_T_IP2_TIME_30US_MASK BIT(2)
#define BT_HCI_LE_CS_T_IP2_TIME_40US_MASK BIT(3)
#define BT_HCI_LE_CS_T_IP2_TIME_50US_MASK BIT(4)
#define BT_HCI_LE_CS_T_IP2_TIME_60US_MASK BIT(5)
#define BT_HCI_LE_CS_T_IP2_TIME_80US_MASK BIT(6)

#define BT_HCI_LE_CS_T_FCS_TIME_15US_MASK   BIT(0)
#define BT_HCI_LE_CS_T_FCS_TIME_20US_MASK   BIT(1)
#define BT_HCI_LE_CS_T_FCS_TIME_30US_MASK   BIT(2)
#define BT_HCI_LE_CS_T_FCS_TIME_40US_MASK   BIT(3)
#define BT_HCI_LE_CS_T_FCS_TIME_50US_MASK   BIT(4)
#define BT_HCI_LE_CS_T_FCS_TIME_60US_MASK   BIT(5)
#define BT_HCI_LE_CS_T_FCS_TIME_80US_MASK   BIT(6)
#define BT_HCI_LE_CS_T_FCS_TIME_100US_MASK  BIT(7)
#define BT_HCI_LE_CS_T_FCS_TIME_1200US_MASK BIT(8)

#define BT_HCI_LE_CS_T_PM_TIME_10US_MASK BIT(0)
#define BT_HCI_LE_CS_T_PM_TIME_20US_MASK BIT(1)

#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_18DB_MASK BIT(0)
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_21DB_MASK BIT(1)
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_24DB_MASK BIT(2)
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_27DB_MASK BIT(3)
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_30DB_MASK BIT(4)

#define BT_HCI_EVT_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE 0x2C

struct bt_hci_evt_le_cs_read_remote_supported_capabilities_complete {
        uint8_t  status;
        uint16_t conn_handle;
        uint8_t  num_config_supported;
        uint16_t max_consecutive_procedures_supported;
        uint8_t  num_antennas_supported;
        uint8_t  max_antenna_paths_supported;
        uint8_t  roles_supported;
        uint8_t  modes_supported;
        uint8_t  rtt_capability;
        uint8_t  rtt_aa_only_n;
        uint8_t  rtt_sounding_n;
        uint8_t  rtt_random_payload_n;
        uint16_t nadm_sounding_capability;
        uint16_t nadm_random_capability;
        uint8_t  cs_sync_phys_supported;
        uint16_t subfeatures_supported;
        uint16_t t_ip1_times_supported;
        uint16_t t_ip2_times_supported;
        uint16_t t_fcs_times_supported;
        uint16_t t_pm_times_supported;
        uint8_t  t_sw_time_supported;
        uint8_t  tx_snr_capability;
} __packed;

#define BT_HCI_EVT_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE_V2 0x38

struct bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2 {
        uint8_t  status;
        uint16_t conn_handle;
        uint8_t  num_config_supported;
        uint16_t max_consecutive_procedures_supported;
        uint8_t  num_antennas_supported;
        uint8_t  max_antenna_paths_supported;
        uint8_t  roles_supported;
        uint8_t  modes_supported;
        uint8_t  rtt_capability;
        uint8_t  rtt_aa_only_n;
        uint8_t  rtt_sounding_n;
        uint8_t  rtt_random_payload_n;
        uint16_t nadm_sounding_capability;
        uint16_t nadm_random_capability;
        uint8_t  cs_sync_phys_supported;
        uint16_t subfeatures_supported;
        uint16_t t_ip1_times_supported;
        uint16_t t_ip2_times_supported;
        uint16_t t_fcs_times_supported;
        uint16_t t_pm_times_supported;
        uint8_t  t_sw_time_supported;
        uint8_t  tx_snr_capability;
        uint16_t t_ip2_ipt_times_supported;
        uint8_t  t_sw_ipt_time_supported;
} __packed;

#define BT_HCI_EVT_LE_CS_READ_REMOTE_FAE_TABLE_COMPLETE 0x2D
struct bt_hci_evt_le_cs_read_remote_fae_table_complete {
        uint8_t  status;
        uint16_t conn_handle;
        int8_t   remote_fae_table[72];
} __packed;

#define BT_HCI_LE_CS_CONFIG_ACTION_REMOVED 0x00
#define BT_HCI_LE_CS_CONFIG_ACTION_CREATED 0x01

#define BT_HCI_EVT_LE_CS_SECURITY_ENABLE_COMPLETE 0x2E
struct bt_hci_evt_le_cs_security_enable_complete {
        uint8_t  status;
        uint16_t handle;
} __packed;

#define BT_HCI_EVT_LE_CS_CONFIG_COMPLETE 0x2F
struct bt_hci_evt_le_cs_config_complete {
        uint8_t  status;
        uint16_t handle;
        uint8_t  config_id;
        uint8_t  action;
        uint8_t  main_mode_type;
        uint8_t  sub_mode_type;
        uint8_t  min_main_mode_steps;
        uint8_t  max_main_mode_steps;
        uint8_t  main_mode_repetition;
        uint8_t  mode_0_steps;
        uint8_t  role;
        uint8_t  rtt_type;
        uint8_t  cs_sync_phy;
        uint8_t  channel_map[10];
        uint8_t  channel_map_repetition;
        uint8_t  channel_selection_type;
        uint8_t  ch3c_shape;
        uint8_t  ch3c_jump;
        uint8_t  cs_enhancements_1;
        uint8_t  t_ip1_time;
        uint8_t  t_ip2_time;
        uint8_t  t_fcs_time;
        uint8_t  t_pm_time;
} __packed;

#define BT_HCI_LE_CS_TEST_CONN_HANDLE 0x0FFF

#define BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_COMPLETE 0x0
#define BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_PARTIAL  0x1
#define BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_ABORTED  0xF

#define BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_COMPLETE 0x0
#define BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_PARTIAL  0x1
#define BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_ABORTED  0xF

#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_NO_ABORT                     0x0
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST 0x1
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_TOO_FEW_CHANNELS             0x2
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_CHMAP_INSTANT_PASSED         0x3
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_UNSPECIFIED                  0xF

#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_ABORT                     0x0
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST 0x1
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_CS_SYNC_RECEIVED          0x2
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_SCHED_CONFLICT               0x3
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_UNSPECIFIED                  0xF

#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_IGNORED 0x00
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_1       0x01
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_2       0x02
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_3       0x03
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_4       0x04

#define BT_HCI_LE_CS_SUBEVENT_RESULT_FREQ_COMPENSATION_NOT_AVAILABLE 0xC000

#define BT_HCI_LE_CS_SUBEVENT_RESULT_PCT_NOT_AVAILABLE 0xFFFFFFFF

#define BT_HCI_LE_CS_REF_POWER_LEVEL_UNAVAILABLE 0x7F

#define BT_HCI_LE_CS_PCT_I_MASK 0x000FFF
#define BT_HCI_LE_CS_PCT_Q_MASK 0xFFF000

#define BT_HCI_LE_CS_TONE_QUALITY_HIGH        0x0
#define BT_HCI_LE_CS_TONE_QUALITY_MED         0x1
#define BT_HCI_LE_CS_TONE_QUALITY_LOW         0x2
#define BT_HCI_LE_CS_TONE_QUALITY_UNAVAILABLE 0x3

#define BT_HCI_LE_CS_NOT_TONE_EXT_SLOT              0x0
#define BT_HCI_LE_CS_TONE_EXT_SLOT_EXT_NOT_EXPECTED 0x1
#define BT_HCI_LE_CS_TONE_EXT_SLOT_EXT_EXPECTED     0x2

#define BT_HCI_LE_CS_TIME_DIFFERENCE_NOT_AVAILABLE ((int16_t)0x8000)

#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_EXT_UNLIKELY  0x00
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_VERY_UNLIKELY 0x01
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_UNLIKELY      0x02
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_POSSIBLE      0x03
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_LIKELY        0x04
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_VERY_LIKELY   0x05
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_EXT_LIKELY    0x06
#define BT_HCI_LE_CS_PACKET_NADM_UNKNOWN              0xFF

#define BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_SUCCESSFUL       0x0
#define BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_BIT_ERRORS_FOUND 0x1
#define BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_AA_NOT_FOUND     0x2

#define BT_HCI_LE_CS_PACKET_RSSI_NOT_AVAILABLE 0x7F

#define BT_HCI_EVT_LE_CS_SUBEVENT_RESULT 0x31
struct bt_hci_le_cs_step_data_mode_0_initiator {
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t  packet_quality_aa_check: 4;
        uint8_t  packet_quality_bit_errors: 4;
#else
        uint8_t  packet_quality_bit_errors: 4;
        uint8_t  packet_quality_aa_check: 4;
#endif /* CONFIG_LITTLE_ENDIAN */
        uint8_t  packet_rssi;
        uint8_t  packet_antenna;
        uint16_t measured_freq_offset;
} __packed;

struct bt_hci_le_cs_step_data_mode_0_reflector {
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t packet_quality_aa_check: 4;
        uint8_t packet_quality_bit_errors: 4;
#else
        uint8_t packet_quality_bit_errors: 4;
        uint8_t packet_quality_aa_check: 4;
#endif /* CONFIG_LITTLE_ENDIAN */
        uint8_t packet_rssi;
        uint8_t packet_antenna;
} __packed;

struct bt_hci_le_cs_step_data_mode_1 {
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t packet_quality_aa_check: 4;
        uint8_t packet_quality_bit_errors: 4;
#else
        uint8_t packet_quality_bit_errors: 4;
        uint8_t packet_quality_aa_check: 4;
#endif /* CONFIG_LITTLE_ENDIAN */
        uint8_t packet_nadm;
        uint8_t packet_rssi;
        union {
                int16_t toa_tod_initiator;
                int16_t tod_toa_reflector;
        } __packed;
        uint8_t packet_antenna;
} __packed;

struct bt_hci_le_cs_step_data_mode_1_ss_rtt {
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t packet_quality_aa_check: 4;
        uint8_t packet_quality_bit_errors: 4;
#else
        uint8_t packet_quality_bit_errors: 4;
        uint8_t packet_quality_aa_check: 4;
#endif /* CONFIG_LITTLE_ENDIAN */
        uint8_t packet_nadm;
        uint8_t packet_rssi;
        union {
                int16_t toa_tod_initiator;
                int16_t tod_toa_reflector;
        } __packed;
        uint8_t packet_antenna;
        uint8_t packet_pct1[4];
        uint8_t packet_pct2[4];
} __packed;


struct bt_hci_le_cs_step_data_tone_info {
        uint8_t phase_correction_term[3];
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t quality_indicator: 4;
        uint8_t extension_indicator: 4;
#else
        uint8_t extension_indicator: 4;
        uint8_t quality_indicator: 4;
#endif /* CONFIG_LITTLE_ENDIAN */
} __packed;

struct bt_hci_le_cs_step_data_mode_2 {
        uint8_t antenna_permutation_index;
        struct bt_hci_le_cs_step_data_tone_info tone_info[];
} __packed;

struct bt_hci_le_cs_step_data_mode_3 {
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t packet_quality_aa_check: 4;
        uint8_t packet_quality_bit_errors: 4;
#else
        uint8_t packet_quality_bit_errors: 4;
        uint8_t packet_quality_aa_check: 4;
#endif /* CONFIG_LITTLE_ENDIAN */
        uint8_t packet_nadm;
        uint8_t packet_rssi;
        union {
                int16_t toa_tod_initiator;
                int16_t tod_toa_reflector;
        } __packed;
        uint8_t packet_antenna;
        uint8_t antenna_permutation_index;
        struct bt_hci_le_cs_step_data_tone_info tone_info[];
} __packed;

struct bt_hci_le_cs_step_data_mode_3_ss_rtt {
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t packet_quality_aa_check: 4;
        uint8_t packet_quality_bit_errors: 4;
#else
        uint8_t packet_quality_bit_errors: 4;
        uint8_t packet_quality_aa_check: 4;
#endif /* CONFIG_LITTLE_ENDIAN */
        uint8_t packet_nadm;
        uint8_t packet_rssi;
        union {
                int16_t toa_tod_initiator;
                int16_t tod_toa_reflector;
        } __packed;
        uint8_t packet_antenna;
        uint8_t packet_pct1[4];
        uint8_t packet_pct2[4];
        uint8_t antenna_permutation_index;
        struct bt_hci_le_cs_step_data_tone_info tone_info[];
} __packed;

struct bt_hci_evt_le_cs_subevent_result_step {
        uint8_t step_mode;
        uint8_t step_channel;
        uint8_t step_data_length;
        uint8_t step_data[];
} __packed;

struct bt_hci_evt_le_cs_subevent_result {
        uint16_t conn_handle;
        uint8_t  config_id;
        uint16_t start_acl_conn_event_counter;
        uint16_t procedure_counter;
        uint16_t frequency_compensation;
        uint8_t  reference_power_level;
        uint8_t  procedure_done_status;
        uint8_t  subevent_done_status;
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t  procedure_abort_reason: 4;
        uint8_t  subevent_abort_reason: 4;
#else
        uint8_t  subevent_abort_reason: 4;
        uint8_t  procedure_abort_reason: 4;
#endif /* CONFIG_LITTLE_ENDIAN */
        uint8_t  num_antenna_paths;
        uint8_t  num_steps_reported;
        uint8_t  steps[];
} __packed;

#define BT_HCI_EVT_LE_CS_SUBEVENT_RESULT_CONTINUE 0x32

struct bt_hci_evt_le_cs_subevent_result_continue {
        uint16_t conn_handle;
        uint8_t  config_id;
        uint8_t  procedure_done_status;
        uint8_t  subevent_done_status;
#ifdef CONFIG_LITTLE_ENDIAN
        uint8_t  procedure_abort_reason: 4;
        uint8_t  subevent_abort_reason: 4;
#else
        uint8_t  subevent_abort_reason: 4;
        uint8_t  procedure_abort_reason: 4;
#endif /* CONFIG_LITTLE_ENDIAN */
        uint8_t  num_antenna_paths;
        uint8_t  num_steps_reported;
        uint8_t  steps[];
} __packed;

#define BT_HCI_EVT_LE_CS_TEST_END_COMPLETE 0x33
struct bt_hci_evt_le_cs_test_end_complete {
        uint8_t status;
} __packed;

#define BT_HCI_EVT_LE_CS_PROCEDURE_ENABLE_COMPLETE 0x30
struct bt_hci_evt_le_cs_procedure_enable_complete {
        uint8_t  status;
        uint16_t handle;
        uint8_t  config_id;
        uint8_t  state;
        uint8_t  tone_antenna_config_selection;
        uint8_t  selected_tx_power;
        uint8_t  subevent_len[3];
        uint8_t  subevents_per_event;
        uint16_t subevent_interval;
        uint16_t event_interval;
        uint16_t procedure_interval;
        uint16_t procedure_count;
        uint16_t max_procedure_len;
} __packed;

#define BT_HCI_EVT_LE_FRAME_SPACE_UPDATE_COMPLETE 0x35
struct bt_hci_evt_le_frame_space_update_complete {
        uint8_t  status;
        uint16_t handle;
        uint8_t  initiator;
        uint16_t frame_space;
        uint8_t  phys;
        uint16_t spacing_types;
} __packed;

#define BT_HCI_EVT_LE_CONN_RATE_CHANGE 0x37
struct bt_hci_evt_le_conn_rate_change {
        uint8_t  status;
        uint16_t handle;
        uint16_t conn_interval;
        uint16_t subrate_factor;
        uint16_t peripheral_latency;
        uint16_t continuation_number;
        uint16_t supervision_timeout;
} __packed;

/* Event mask bits */

#define BT_EVT_BIT(n) (1ULL << (n))

#define BT_EVT_MASK_INQUIRY_COMPLETE             BT_EVT_BIT(0)
#define BT_EVT_MASK_CONN_COMPLETE                BT_EVT_BIT(2)
#define BT_EVT_MASK_CONN_REQUEST                 BT_EVT_BIT(3)
#define BT_EVT_MASK_DISCONN_COMPLETE             BT_EVT_BIT(4)
#define BT_EVT_MASK_AUTH_COMPLETE                BT_EVT_BIT(5)
#define BT_EVT_MASK_REMOTE_NAME_REQ_COMPLETE     BT_EVT_BIT(6)
#define BT_EVT_MASK_ENCRYPT_CHANGE               BT_EVT_BIT(7)
#define BT_EVT_MASK_REMOTE_FEATURES              BT_EVT_BIT(10)
#define BT_EVT_MASK_REMOTE_VERSION_INFO          BT_EVT_BIT(11)
#define BT_EVT_MASK_HARDWARE_ERROR               BT_EVT_BIT(15)
#define BT_EVT_MASK_ROLE_CHANGE                  BT_EVT_BIT(17)
#define BT_EVT_MASK_MODE_CHANGE                  BT_EVT_BIT(19)
#define BT_EVT_MASK_PIN_CODE_REQ                 BT_EVT_BIT(21)
#define BT_EVT_MASK_LINK_KEY_REQ                 BT_EVT_BIT(22)
#define BT_EVT_MASK_LINK_KEY_NOTIFY              BT_EVT_BIT(23)
#define BT_EVT_MASK_DATA_BUFFER_OVERFLOW         BT_EVT_BIT(25)
#define BT_EVT_MASK_CONN_PKT_TYPE_CHANGED        BT_EVT_BIT(28)
#define BT_EVT_MASK_INQUIRY_RESULT_WITH_RSSI     BT_EVT_BIT(33)
#define BT_EVT_MASK_REMOTE_EXT_FEATURES          BT_EVT_BIT(34)
#define BT_EVT_MASK_SYNC_CONN_COMPLETE           BT_EVT_BIT(43)
#define BT_EVT_MASK_EXTENDED_INQUIRY_RESULT      BT_EVT_BIT(46)
#define BT_EVT_MASK_ENCRYPT_KEY_REFRESH_COMPLETE BT_EVT_BIT(47)
#define BT_EVT_MASK_IO_CAPA_REQ                  BT_EVT_BIT(48)
#define BT_EVT_MASK_IO_CAPA_RESP                 BT_EVT_BIT(49)
#define BT_EVT_MASK_USER_CONFIRM_REQ             BT_EVT_BIT(50)
#define BT_EVT_MASK_USER_PASSKEY_REQ             BT_EVT_BIT(51)
#define BT_EVT_MASK_SSP_COMPLETE                 BT_EVT_BIT(53)
#define BT_EVT_MASK_USER_PASSKEY_NOTIFY          BT_EVT_BIT(58)
#define BT_EVT_MASK_LE_META_EVENT                BT_EVT_BIT(61)

/* Page 2 */
#define BT_EVT_MASK_NUM_COMPLETE_DATA_BLOCKS     BT_EVT_BIT(8)
#define BT_EVT_MASK_TRIGG_CLOCK_CAPTURE          BT_EVT_BIT(14)
#define BT_EVT_MASK_SYNCH_TRAIN_COMPLETE         BT_EVT_BIT(15)
#define BT_EVT_MASK_SYNCH_TRAIN_RX               BT_EVT_BIT(16)
#define BT_EVT_MASK_CL_PER_BC_RX                 BT_EVT_BIT(17)
#define BT_EVT_MASK_CL_PER_BC_TIMEOUT            BT_EVT_BIT(18)
#define BT_EVT_MASK_TRUNC_PAGE_COMPLETE          BT_EVT_BIT(19)
#define BT_EVT_MASK_PER_PAGE_RSP_TIMEOUT         BT_EVT_BIT(20)
#define BT_EVT_MASK_CL_PER_BC_CH_MAP_CHANGE      BT_EVT_BIT(21)
#define BT_EVT_MASK_INQUIRY_RSP_NOT              BT_EVT_BIT(22)
#define BT_EVT_MASK_AUTH_PAYLOAD_TIMEOUT_EXP     BT_EVT_BIT(23)
#define BT_EVT_MASK_SAM_STATUS_CHANGE            BT_EVT_BIT(24)

#define BT_EVT_MASK_LE_CONN_COMPLETE             BT_EVT_BIT(0)
#define BT_EVT_MASK_LE_ADVERTISING_REPORT        BT_EVT_BIT(1)
#define BT_EVT_MASK_LE_CONN_UPDATE_COMPLETE      BT_EVT_BIT(2)
#define BT_EVT_MASK_LE_REMOTE_FEAT_COMPLETE      BT_EVT_BIT(3)
#define BT_EVT_MASK_LE_LTK_REQUEST               BT_EVT_BIT(4)
#define BT_EVT_MASK_LE_CONN_PARAM_REQ            BT_EVT_BIT(5)
#define BT_EVT_MASK_LE_DATA_LEN_CHANGE           BT_EVT_BIT(6)
#define BT_EVT_MASK_LE_P256_PUBLIC_KEY_COMPLETE  BT_EVT_BIT(7)
#define BT_EVT_MASK_LE_GENERATE_DHKEY_COMPLETE   BT_EVT_BIT(8)
#define BT_EVT_MASK_LE_ENH_CONN_COMPLETE         BT_EVT_BIT(9)
#define BT_EVT_MASK_LE_DIRECT_ADV_REPORT         BT_EVT_BIT(10)
#define BT_EVT_MASK_LE_PHY_UPDATE_COMPLETE       BT_EVT_BIT(11)
#define BT_EVT_MASK_LE_EXT_ADVERTISING_REPORT    BT_EVT_BIT(12)
#define BT_EVT_MASK_LE_PER_ADV_SYNC_ESTABLISHED  BT_EVT_BIT(13)
#define BT_EVT_MASK_LE_PER_ADVERTISING_REPORT    BT_EVT_BIT(14)
#define BT_EVT_MASK_LE_PER_ADV_SYNC_LOST         BT_EVT_BIT(15)
#define BT_EVT_MASK_LE_SCAN_TIMEOUT              BT_EVT_BIT(16)
#define BT_EVT_MASK_LE_ADV_SET_TERMINATED        BT_EVT_BIT(17)
#define BT_EVT_MASK_LE_SCAN_REQ_RECEIVED         BT_EVT_BIT(18)
#define BT_EVT_MASK_LE_CHAN_SEL_ALGO             BT_EVT_BIT(19)
#define BT_EVT_MASK_LE_CONNECTIONLESS_IQ_REPORT  BT_EVT_BIT(20)
#define BT_EVT_MASK_LE_CONNECTION_IQ_REPORT      BT_EVT_BIT(21)
#define BT_EVT_MASK_LE_CTE_REQUEST_FAILED        BT_EVT_BIT(22)
#define BT_EVT_MASK_LE_PAST_RECEIVED             BT_EVT_BIT(23)
#define BT_EVT_MASK_LE_CIS_ESTABLISHED           BT_EVT_BIT(24)
#define BT_EVT_MASK_LE_CIS_REQ                   BT_EVT_BIT(25)
#define BT_EVT_MASK_LE_BIG_COMPLETE              BT_EVT_BIT(26)
#define BT_EVT_MASK_LE_BIG_TERMINATED            BT_EVT_BIT(27)
#define BT_EVT_MASK_LE_BIG_SYNC_ESTABLISHED      BT_EVT_BIT(28)
#define BT_EVT_MASK_LE_BIG_SYNC_LOST             BT_EVT_BIT(29)
#define BT_EVT_MASK_LE_REQ_PEER_SCA_COMPLETE     BT_EVT_BIT(30)
#define BT_EVT_MASK_LE_PATH_LOSS_THRESHOLD       BT_EVT_BIT(31)
#define BT_EVT_MASK_LE_TRANSMIT_POWER_REPORTING  BT_EVT_BIT(32)
#define BT_EVT_MASK_LE_BIGINFO_ADV_REPORT        BT_EVT_BIT(33)
#define BT_EVT_MASK_LE_SUBRATE_CHANGE            BT_EVT_BIT(34)

#define BT_EVT_MASK_LE_PER_ADV_SYNC_ESTABLISHED_V2 BT_EVT_BIT(35)
#define BT_EVT_MASK_LE_PER_ADVERTISING_REPORT_V2   BT_EVT_BIT(36)
#define BT_EVT_MASK_LE_PAST_RECEIVED_V2            BT_EVT_BIT(37)
#define BT_EVT_MASK_LE_PER_ADV_SUBEVENT_DATA_REQ   BT_EVT_BIT(38)
#define BT_EVT_MASK_LE_PER_ADV_RESPONSE_REPORT     BT_EVT_BIT(39)
#define BT_EVT_MASK_LE_ENH_CONN_COMPLETE_V2        BT_EVT_BIT(40)
#define BT_EVT_MASK_LE_CIS_ESTABLISHED_V2          BT_EVT_BIT(41)

#define BT_EVT_MASK_LE_READ_ALL_REMOTE_FEAT_COMPLETE BT_EVT_BIT(42)

#define BT_EVT_MASK_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE BT_EVT_BIT(43)
#define BT_EVT_MASK_LE_CS_READ_REMOTE_FAE_TABLE_COMPLETE              BT_EVT_BIT(44)
#define BT_EVT_MASK_LE_CS_SECURITY_ENABLE_COMPLETE                    BT_EVT_BIT(45)
#define BT_EVT_MASK_LE_CS_CONFIG_COMPLETE                             BT_EVT_BIT(46)
#define BT_EVT_MASK_LE_CS_PROCEDURE_ENABLE_COMPLETE                   BT_EVT_BIT(47)
#define BT_EVT_MASK_LE_CS_SUBEVENT_RESULT                             BT_EVT_BIT(48)
#define BT_EVT_MASK_LE_CS_SUBEVENT_RESULT_CONTINUE                    BT_EVT_BIT(49)
#define BT_EVT_MASK_LE_CS_TEST_END_COMPLETE                           BT_EVT_BIT(50)

#define BT_EVT_MASK_LE_FRAME_SPACE_UPDATE_COMPLETE BT_EVT_BIT(52)
#define BT_EVT_MASK_LE_CONN_RATE_CHANGE            BT_EVT_BIT(54)

#define BT_EVT_MASK_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE_V2 BT_EVT_BIT(55)

#define BT_HCI_ERR_SUCCESS                      0x00
#define BT_HCI_ERR_UNKNOWN_CMD                  0x01
#define BT_HCI_ERR_UNKNOWN_CONN_ID              0x02
#define BT_HCI_ERR_HW_FAILURE                   0x03
#define BT_HCI_ERR_PAGE_TIMEOUT                 0x04
#define BT_HCI_ERR_AUTH_FAIL                    0x05
#define BT_HCI_ERR_PIN_OR_KEY_MISSING           0x06
#define BT_HCI_ERR_MEM_CAPACITY_EXCEEDED        0x07
#define BT_HCI_ERR_CONN_TIMEOUT                 0x08
#define BT_HCI_ERR_CONN_LIMIT_EXCEEDED          0x09
#define BT_HCI_ERR_SYNC_CONN_LIMIT_EXCEEDED     0x0a
#define BT_HCI_ERR_CONN_ALREADY_EXISTS          0x0b
#define BT_HCI_ERR_CMD_DISALLOWED               0x0c
#define BT_HCI_ERR_INSUFFICIENT_RESOURCES       0x0d
#define BT_HCI_ERR_INSUFFICIENT_SECURITY        0x0e
#define BT_HCI_ERR_BD_ADDR_UNACCEPTABLE         0x0f
#define BT_HCI_ERR_CONN_ACCEPT_TIMEOUT          0x10
#define BT_HCI_ERR_UNSUPP_FEATURE_PARAM_VAL     0x11
#define BT_HCI_ERR_INVALID_PARAM                0x12
#define BT_HCI_ERR_REMOTE_USER_TERM_CONN        0x13
#define BT_HCI_ERR_REMOTE_LOW_RESOURCES         0x14
#define BT_HCI_ERR_REMOTE_POWER_OFF             0x15
#define BT_HCI_ERR_LOCALHOST_TERM_CONN          0x16
#define BT_HCI_ERR_REPEATED_ATTEMPTS            0x17
#define BT_HCI_ERR_PAIRING_NOT_ALLOWED          0x18
#define BT_HCI_ERR_UNKNOWN_LMP_PDU              0x19
#define BT_HCI_ERR_UNSUPP_REMOTE_FEATURE        0x1a
#define BT_HCI_ERR_SCO_OFFSET_REJECTED          0x1b
#define BT_HCI_ERR_SCO_INTERVAL_REJECTED        0x1c
#define BT_HCI_ERR_SCO_AIR_MODE_REJECTED        0x1d
#define BT_HCI_ERR_INVALID_LL_PARAM             0x1e
#define BT_HCI_ERR_UNSPECIFIED                  0x1f
#define BT_HCI_ERR_UNSUPP_LL_PARAM_VAL          0x20
#define BT_HCI_ERR_ROLE_CHANGE_NOT_ALLOWED      0x21
#define BT_HCI_ERR_LL_RESP_TIMEOUT              0x22
#define BT_HCI_ERR_LL_PROC_COLLISION            0x23
#define BT_HCI_ERR_LMP_PDU_NOT_ALLOWED          0x24
#define BT_HCI_ERR_ENC_MODE_NOT_ACCEPTABLE      0x25
#define BT_HCI_ERR_LINK_KEY_CANNOT_BE_CHANGED   0x26
#define BT_HCI_ERR_REQUESTED_QOS_NOT_SUPPORTED  0x27
#define BT_HCI_ERR_INSTANT_PASSED               0x28
#define BT_HCI_ERR_PAIRING_NOT_SUPPORTED        0x29
#define BT_HCI_ERR_DIFF_TRANS_COLLISION         0x2a
#define BT_HCI_ERR_QOS_UNACCEPTABLE_PARAM       0x2c
#define BT_HCI_ERR_QOS_REJECTED                 0x2d
#define BT_HCI_ERR_CHAN_ASSESS_NOT_SUPPORTED    0x2e
#define BT_HCI_ERR_INSUFF_SECURITY              0x2f
#define BT_HCI_ERR_PARAM_OUT_OF_MANDATORY_RANGE 0x30
#define BT_HCI_ERR_ROLE_SWITCH_PENDING          0x32
#define BT_HCI_ERR_RESERVED_SLOT_VIOLATION      0x34
#define BT_HCI_ERR_ROLE_SWITCH_FAILED           0x35
#define BT_HCI_ERR_EXT_INQ_RESP_TOO_LARGE       0x36
#define BT_HCI_ERR_SIMPLE_PAIR_NOT_SUPP_BY_HOST 0x37
#define BT_HCI_ERR_HOST_BUSY_PAIRING            0x38
#define BT_HCI_ERR_CONN_REJECTED_DUE_TO_NO_CHAN 0x39
#define BT_HCI_ERR_CONTROLLER_BUSY              0x3a
#define BT_HCI_ERR_UNACCEPT_CONN_PARAM          0x3b
#define BT_HCI_ERR_ADV_TIMEOUT                  0x3c
#define BT_HCI_ERR_TERM_DUE_TO_MIC_FAIL         0x3d
#define BT_HCI_ERR_CONN_FAIL_TO_ESTAB           0x3e
#define BT_HCI_ERR_MAC_CONN_FAILED              0x3f
#define BT_HCI_ERR_CLOCK_ADJUST_REJECTED        0x40
#define BT_HCI_ERR_SUBMAP_NOT_DEFINED           0x41
#define BT_HCI_ERR_UNKNOWN_ADV_IDENTIFIER       0x42
#define BT_HCI_ERR_LIMIT_REACHED                0x43
#define BT_HCI_ERR_OP_CANCELLED_BY_HOST         0x44
#define BT_HCI_ERR_PACKET_TOO_LONG              0x45
#define BT_HCI_ERR_TOO_LATE                     0x46
#define BT_HCI_ERR_TOO_EARLY                    0x47

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_HCI_TYPES_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`hci.h`：蓝牙主机控制器接口（Bluetooth HCI）类型。

### 注释 2：原第 3 行

版权（Copyright）：© 2015-2016 Intel Corporation。

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 25 行

蓝牙规范 v5.4 第 4 卷 A 部分表 2.1：HCI 数据包指示符（Packet Indicators）。以下定义供 UART 传输层（UART Transport Layer）使用，也可按需复用于其他传输层。

### 注释 4：原第 29 行

不属于任何已知的数据包类型（Packet Types）。

### 注释 5：原第 30 行

HCI 命令数据包（Command Packet）。

### 注释 6：原第 31 行

HCI 异步无连接链路数据包（ACL Data Packet）。

### 注释 7：原第 32 行

HCI 同步数据包（Synchronous Data Packet）。

### 注释 8：原第 33 行

HCI 事件数据包（Event Packet）。

### 注释 9：原第 34 行

HCI 等时数据包（ISO Data Packet）。

### 注释 10：原第 52 行

蓝牙规范 v5.4 第 4 卷 E 部分第 5.4.3 节：HCI 同步数据包（Synchronous Data Packets）。

### 注释 11：原第 54 行

12 位句柄（Handle）、2 位数据包状态标志（Packet Status Flag）、1 位保留供将来使用（RFU）。

### 注释 12：原第 59 行

蓝牙规范 v5.4 第 4 卷 E 部分第 5.4.4 节：HCI 事件数据包（Event Packet）。

### 注释 13：原第 83 行

蓝牙规范 v5.4 第 4 卷 E 部分第 5.4.2 节：ACL 数据包（Data Packets）。

### 注释 14：原第 115 行

12 位长度（Length）、2 位保留供将来使用（RFU）、2 位数据包状态（Packet Status）。

### 注释 15：原第 125 行

蓝牙规范 v5.4 第 4 卷 E 部分第 5.4.5 节：HCI 等时数据包（ISO Data Packets）。

### 注释 16：原第 127 行

12 位句柄（Handle）、2 位数据包边界标志（PB Flags）、1 位时间戳标志（TS_Flag）、1 位保留供将来使用（RFU）。

### 注释 17：原第 128 行

14 位数据，2 位保留供将来使用（RFU）。

### 注释 18：原第 132 行

蓝牙规范 v5.4 第 4 卷 E 部分第 5.4.1 节：HCI 命令数据包（Command Packet）。

### 注释 19：原第 139 行

支持的命令（Supported Commands）。

### 注释 20：原第 161 行

低功耗蓝牙（LE）特性。

### 注释 21：原第 310 行

低功耗蓝牙状态（LE States），参见 Core_v5.4 第 4 卷 E 部分第 7.8.27 节。

### 注释 22：原第 314 行

被动扫描器（Passive Scanner）和主动扫描器（Active Scanner）都可以与发起器（Initiator）并行运行。

### 注释 23：原第 322 行

绑定／认证类型（Bonding/Authentication Types）。

### 注释 24：原第 330 行

简单安全配对（SSP）的认证要求八位组中，最低有效位（LSB）置位时启用中间人攻击防护（MITM Protection）。

### 注释 25：原第 336 行

输入输出能力（I/O Capabilities）。

### 注释 26：原第 342 行

同步面向连接（SCO）数据包类型。

### 注释 27：原第 347 行

扩展同步面向连接（eSCO）数据包类型。

### 注释 28：原第 374 行

HCI 基本速率／增强数据速率（BR/EDR）链路类型。

### 注释 29：原第 379 行

操作码组字段（OpCode Group Fields）。

### 注释 30：原第 388 行

根据操作码组字段（OGF）和操作码命令字段（OCF）构造操作码（OpCode）。

### 注释 31：原第 391 行

无效操作码（Invalid Opcode）。

### 注释 32：原第 394 行

从操作码（OpCode）中获取操作码组字段（OGF）。

### 注释 33：原第 396 行

从操作码（OpCode）中获取操作码命令字段（OCF）。

### 注释 34：原第 399 行

十六进制值（Hexadecimal Value）：`0x0401`。

### 注释 35：原第 406 行

十六进制值（Hexadecimal Value）：`0x0402`。

### 注释 36：原第 408 行

十六进制值（Hexadecimal Value）：`0x0405`。

### 注释 37：原第 418 行

十六进制值（Hexadecimal Value）：`0x0406`。

### 注释 38：原第 424 行

十六进制值（Hexadecimal Value）：`0x0408`。

### 注释 39：原第 433 行

十六进制值（Hexadecimal Value）：`0x0409`。

### 注释 40：原第 491 行

不限制 SCO 链路延迟（Link Latency）。

### 注释 41：原第 493 行

不限制 SCO 重传努力程度（Retransmission Effort）。

### 注释 42：原第 495 行

十六进制值（Hexadecimal Value）：`0x0428`。

### 注释 43：原第 506 行

十六进制值（Hexadecimal Value）：`0x0429`。

### 注释 44：原第 517 行

十六进制值（Hexadecimal Value）：`0x040a`。

### 注释 45：原第 523 行

十六进制值（Hexadecimal Value）：`0x040b`。

### 注释 46：原第 529 行

十六进制值（Hexadecimal Value）：`0x040c`。

### 注释 47：原第 534 行

十六进制值（Hexadecimal Value）：`0x040d`。

### 注释 48：原第 545 行

十六进制值（Hexadecimal Value）：`0x040e`。

### 注释 49：原第 555 行

十六进制值（Hexadecimal Value）：`0x040f`。

### 注释 50：原第 564 行

`HCI_Change_Connection_Packet_Type` 命令的 ACL 数据包类型位（Packet Type Bits）。

- 基本速率（BR）数据包类型：置位表示可以使用；参见核心规范 v6.0 第 4 卷 E 部分第 7.1.14 节。
- 增强数据速率（EDR）数据包类型：置位表示不得使用。

注意：EDR 位的逻辑与 BR 位相反。

### 注释 51：原第 601 行

十六进制值（Hexadecimal Value）：`0x0411`。

### 注释 52：原第 606 行

十六进制值（Hexadecimal Value）：`0x0413`。

### 注释 53：原第 612 行

十六进制值（Hexadecimal Value）：`0x0419`。

### 注释 54：原第 620 行

十六进制值（Hexadecimal Value）：`0x041a`。

### 注释 55：原第 629 行

十六进制值（Hexadecimal Value）：`0x041b`。

### 注释 56：原第 634 行

十六进制值（Hexadecimal Value）：`0x041c`。

### 注释 57：原第 640 行

十六进制值（Hexadecimal Value）：`0x041d`。

### 注释 58：原第 645 行

十六进制值（Hexadecimal Value）：`0x042b`。

### 注释 59：原第 653 行

十六进制值（Hexadecimal Value）：`0x042c`。

### 注释 60：原第 654 行

十六进制值（Hexadecimal Value）：`0x042d`。

### 注释 61：原第 663 行

十六进制值（Hexadecimal Value）：`0x042e`。

### 注释 62：原第 669 行

十六进制值（Hexadecimal Value）：`0x042f`。

### 注释 63：原第 674 行

十六进制值（Hexadecimal Value）：`0x0434`。

### 注释 64：原第 717 行

十六进制值（Hexadecimal Value）：`0x0803`。

### 注释 65：原第 726 行

十六进制值（Hexadecimal Value）：`0x0804`。

### 注释 66：原第 732 行

十六进制值（Hexadecimal Value）：`0x0811`。

### 注释 67：原第 753 行

十六进制值（Hexadecimal Value）：`0x0c01`。

### 注释 68：原第 758 行

十六进制值（Hexadecimal Value）：`0x0c03`。

### 注释 69：原第 760 行

十六进制值（Hexadecimal Value）：`0x0c13`。

### 注释 70：原第 765 行

十六进制值（Hexadecimal Value）：`0x0c15`。

### 注释 71：原第 771 行

十六进制值（Hexadecimal Value）：`0x0c16`。

### 注释 72：原第 780 行

十六进制值（Hexadecimal Value）：`0x0c18`。

### 注释 73：原第 782 行

十六进制值（Hexadecimal Value）：`0x0c1a`。

### 注释 74：原第 788 行

十六进制值（Hexadecimal Value）：`0x0c1c`。

### 注释 75：原第 798 行

十六进制值（Hexadecimal Value）：`0x0c1e`。

### 注释 76：原第 807 行

十六进制值（Hexadecimal Value）：`0x0c23`。

### 注释 77：原第 813 行

十六进制值（Hexadecimal Value）：`0x0c24`。

### 注释 78：原第 820 行

十六进制值（Hexadecimal Value）：`0x0c2d`。

### 注释 79：原第 836 行

十六进制值（Hexadecimal Value）：`0x2076`。

### 注释 80：原第 850 行

十六进制值（Hexadecimal Value）：`0x2077`。

### 注释 81：原第 854 行

十六进制值（Hexadecimal Value）：`0x207A`。

### 注释 82：原第 861 行

十六进制值（Hexadecimal Value）：`0x2078`。

### 注释 83：原第 879 行

十六进制值（Hexadecimal Value）：`0x2079`。

### 注释 84：原第 891 行

十六进制值（Hexadecimal Value）：`0x207D`。

### 注释 85：原第 901 行

十六进制值（Hexadecimal Value）：`0x207E`。

### 注释 86：原第 914 行

十六进制值（Hexadecimal Value）：`0x0c31`。

### 注释 87：原第 919 行

十六进制值（Hexadecimal Value）：`0x0c33`。

### 注释 88：原第 932 行

十六进制值（Hexadecimal Value）：`0x0c35`。

### 注释 89：原第 939 行

十六进制值（Hexadecimal Value）：`0x0c36`。

### 注释 90：原第 956 行

十六进制值（Hexadecimal Value）：`0x0c37`。

### 注释 91：原第 965 行

十六进制值（Hexadecimal Value）：`0x0c3a`。

### 注释 92：原第 976 行

十六进制值（Hexadecimal Value）：`0x0c43`。

### 注释 93：原第 983 行

十六进制值（Hexadecimal Value）：`0x0c45`。

### 注释 94：原第 989 行

十六进制值（Hexadecimal Value）：`0x0c47`。

### 注释 95：原第 999 行

十六进制值（Hexadecimal Value）：`0x0c52`。

### 注释 96：原第 1008 行

十六进制值（Hexadecimal Value）：`0x0c56`。

### 注释 97：原第 1013 行

十六进制值（Hexadecimal Value）：`0x0c63`。

### 注释 98：原第 1018 行

十六进制值（Hexadecimal Value）：`0x0c6d`。

### 注释 99：原第 1024 行

十六进制值（Hexadecimal Value）：`0x0c7a`。

### 注释 100：原第 1029 行

十六进制值（Hexadecimal Value）：`0x0c7b`。

### 注释 101：原第 1040 行

十六进制值（Hexadecimal Value）：`0x0c7c`。

### 注释 102：原第 1051 行

十六进制值（Hexadecimal Value）：`0x0c83`。

### 注释 103：原第 1063 行

分配编号表（Assigned Numbers）中的 HCI 版本。

### 注释 104：原第 1083 行

十六进制值（Hexadecimal Value）：`0x1001`。

### 注释 105：原第 1093 行

十六进制值（Hexadecimal Value）：`0x1002`。

### 注释 106：原第 1099 行

十六进制值（Hexadecimal Value）：`0x1004`。

### 注释 107：原第 1110 行

十六进制值（Hexadecimal Value）：`0x1003`。

### 注释 108：原第 1116 行

十六进制值（Hexadecimal Value）：`0x1005`。

### 注释 109：原第 1125 行

十六进制值（Hexadecimal Value）：`0x1009`。

### 注释 110：原第 1131 行

读取支持的编解码器（Codecs）时返回的逻辑传输类型位（Logical Transport Type Bits）。

### 注释 111：原第 1137 行

读取编解码器能力（Codec Capabilities）和控制器延迟（Controller Delays）时使用的逻辑传输类型。

### 注释 112：原第 1143 行

音频数据路径方向（Audio Datapath Directions）。

### 注释 113：原第 1147 行

音频数据路径标识（Audio Datapath IDs）。

### 注释 114：原第 1152 行

编码格式分配编号（Coding Format Assigned Numbers），用于编解码器标识（Codec IDs）。

### 注释 115：原第 1164 行

十六进制值（Hexadecimal Value）：`0x100b`。

### 注释 116：原第 1182 行

其他字段动态填充（Filled Dynamically）。

### 注释 117：原第 1186 行

十六进制值（Hexadecimal Value）：`0x100d`。

### 注释 118：原第 1189 行

位图（Bitmap）。

### 注释 119：原第 1198 行

位图（Bitmap）。

### 注释 120：原第 1206 行

其他字段动态填充（Filled Dynamically）。

### 注释 121：原第 1216 行

十六进制值（Hexadecimal Value）：`0x100e`。

### 注释 122：原第 1229 行

其他字段动态填充（Filled Dynamically）。

### 注释 123：原第 1233 行

十六进制值（Hexadecimal Value）：`0x100f`。

### 注释 124：原第 1247 行

十六进制值（Hexadecimal Value）：`0x1405`。

### 注释 125：原第 1260 行

十六进制值（Hexadecimal Value）：`0x1408`。

### 注释 126：原第 1270 行

低功耗蓝牙（Bluetooth LE）。

### 注释 127：原第 1272 行

十六进制值（Hexadecimal Value）：`0x2001`。

### 注释 128：原第 1277 行

十六进制值（Hexadecimal Value）：`0x2002`。

### 注释 129：原第 1284 行

十六进制值（Hexadecimal Value）：`0x2003`。

### 注释 130：原第 1290 行

十六进制值（Hexadecimal Value）：`0x2005`。

### 注释 131：原第 1318 行

十六进制值（Hexadecimal Value）：`0x2006`。

### 注释 132：原第 1329 行

十六进制值（Hexadecimal Value）：`0x2007`。

### 注释 133：原第 1335 行

十六进制值（Hexadecimal Value）：`0x2008`。

### 注释 134：原第 1341 行

十六进制值（Hexadecimal Value）：`0x2009`。

### 注释 135：原第 1350 行

十六进制值（Hexadecimal Value）：`0x200a`。

### 注释 136：原第 1355 行

扫描类型（Scan Types）。

### 注释 137：原第 1356 行

十六进制值（Hexadecimal Value）：`0x200b`。

### 注释 138：原第 1373 行

十六进制值（Hexadecimal Value）：`0x200c`。

### 注释 139：原第 1386 行

十六进制值（Hexadecimal Value）：`0x200d`。

### 注释 140：原第 1405 行

十六进制值（Hexadecimal Value）：`0x200e`。

### 注释 141：原第 1407 行

十六进制值（Hexadecimal Value）：`0x200f`。

### 注释 142：原第 1413 行

十六进制值（Hexadecimal Value）：`0x2010`。

### 注释 143：原第 1415 行

十六进制值（Hexadecimal Value）：`0x2011`。

### 注释 144：原第 1420 行

十六进制值（Hexadecimal Value）：`0x2012`。

### 注释 145：原第 1425 行

十六进制值（Hexadecimal Value）：`0x2013`。

### 注释 146：原第 1436 行

十六进制值（Hexadecimal Value）：`0x2014`。

### 注释 147：原第 1441 行

十六进制值（Hexadecimal Value）：`0x2015`。

### 注释 148：原第 1451 行

十六进制值（Hexadecimal Value）：`0x2016`。

### 注释 149：原第 1456 行

十六进制值（Hexadecimal Value）：`0x2017`。

### 注释 150：原第 1466 行

十六进制值（Hexadecimal Value）：`0x2018`。

### 注释 151：原第 1472 行

十六进制值（Hexadecimal Value）：`0x2019`。

### 注释 152：原第 1482 行

十六进制值（Hexadecimal Value）：`0x201a`。

### 注释 153：原第 1492 行

十六进制值（Hexadecimal Value）：`0x201b`。

### 注释 154：原第 1501 行

十六进制值（Hexadecimal Value）：`0x201c`。

### 注释 155：原第 1507 行

十六进制值（Hexadecimal Value）：`0x201d`。

### 注释 156：原第 1521 行

十六进制值（Hexadecimal Value）：`0x201e`。

### 注释 157：原第 1528 行

十六进制值（Hexadecimal Value）：`0x201f`。

### 注释 158：原第 1534 行

十六进制值（Hexadecimal Value）：`0x2020`。

### 注释 159：原第 1549 行

十六进制值（Hexadecimal Value）：`0x2021`。

### 注释 160：原第 1559 行

十六进制值（Hexadecimal Value）：`0x2022`。

### 注释 161：原第 1570 行

十六进制值（Hexadecimal Value）：`0x2023`。

### 注释 162：原第 1577 行

十六进制值（Hexadecimal Value）：`0x2024`。

### 注释 163：原第 1583 行

十六进制值（Hexadecimal Value）：`0x2025`。

### 注释 164：原第 1585 行

十六进制值（Hexadecimal Value）：`0x2026`。

### 注释 165：原第 1591 行

十六进制值（Hexadecimal Value）：`0x205e`。

### 注释 166：原第 1602 行

十六进制值（Hexadecimal Value）：`0x2027`。

### 注释 167：原第 1609 行

十六进制值（Hexadecimal Value）：`0x2028`。

### 注释 168：原第 1614 行

十六进制值（Hexadecimal Value）：`0x2029`。

### 注释 169：原第 1616 行

十六进制值（Hexadecimal Value）：`0x202a`。

### 注释 170：原第 1622 行

十六进制值（Hexadecimal Value）：`0x202b`。

### 注释 171：原第 1631 行

十六进制值（Hexadecimal Value）：`0x202c`。

### 注释 172：原第 1643 行

十六进制值（Hexadecimal Value）：`0x202d`。

### 注释 173：原第 1648 行

十六进制值（Hexadecimal Value）：`0x202e`。

### 注释 174：原第 1653 行

所有限制均依据蓝牙核心规范 5.4 第 4 卷 E 部分第 7.8.46 节。

### 注释 175：原第 1664 行

十六进制值（Hexadecimal Value）：`0x202f`。

### 注释 176：原第 1677 行

十六进制值（Hexadecimal Value）：`0x2030`。

### 注释 177：原第 1695 行

十六进制值（Hexadecimal Value）：`0x2031`。

### 注释 178：原第 1706 行

十六进制值（Hexadecimal Value）：`0x2032`。

### 注释 179：原第 1722 行

十六进制值（Hexadecimal Value）：`0x2033`。

### 注释 180：原第 1734 行

十六进制值（Hexadecimal Value）：`0x2034`。

### 注释 181：原第 1742 行

十六进制值（Hexadecimal Value）：`0x2035`。

### 注释 182：原第 1773 行

十六进制值（Hexadecimal Value）：`0x2036`。

### 注释 183：原第 1799 行

十六进制值（Hexadecimal Value）：`0x207F`。

### 注释 184：原第 1830 行

十六进制值（Hexadecimal Value）：`0x2037`。

### 注释 185：原第 1839 行

十六进制值（Hexadecimal Value）：`0x2038`。

### 注释 186：原第 1848 行

十六进制值（Hexadecimal Value）：`0x2039`。

### 注释 187：原第 1861 行

十六进制值（Hexadecimal Value）：`0x203a`。

### 注释 188：原第 1867 行

十六进制值（Hexadecimal Value）：`0x203b`。

### 注释 189：原第 1873 行

十六进制值（Hexadecimal Value）：`0x203c`。

### 注释 190：原第 1878 行

十六进制值（Hexadecimal Value）：`0x203d`。

### 注释 191：原第 1883 行

十六进制值（Hexadecimal Value）：`0x203e`。

### 注释 192：原第 1898 行

十六进制值（Hexadecimal Value）：`0x203f`。

### 注释 193：原第 1909 行

十六进制值（Hexadecimal Value）：`0x2040`。

### 注释 194：原第 1915 行

十六进制值（Hexadecimal Value）：`0x2041`。

### 注释 195：原第 1933 行

扩展 `BT_HCI_LE_SCAN_FILTER_DUP`。

### 注释 196：原第 1936 行

十六进制值（Hexadecimal Value）：`0x2042`。

### 注释 197：原第 1944 行

十六进制值（Hexadecimal Value）：`0x2043`。

### 注释 198：原第 1945 行

十六进制值（Hexadecimal Value）：`0x2085`。

### 注释 199：原第 1975 行

十六进制值（Hexadecimal Value）：`0x2082`。

### 注释 200：原第 1991 行

十六进制值（Hexadecimal Value）：`0x2083`。

### 注释 201：原第 2002 行

十六进制值（Hexadecimal Value）：`0x2084`。

### 注释 202：原第 2011 行

十六进制值（Hexadecimal Value）：`0x2086`。

### 注释 203：原第 2035 行

用于检查恒定音调扩展（CTE）类型是否正确的常量。

### 注释 204：原第 2040 行

十六进制值（Hexadecimal Value）：`0x2044`。

### 注释 205：原第 2050 行

十六进制值（Hexadecimal Value）：`0x2045`。

### 注释 206：原第 2052 行

十六进制值（Hexadecimal Value）：`0x2046`。

### 注释 207：原第 2057 行

十六进制值（Hexadecimal Value）：`0x2047`。

### 注释 208：原第 2063 行

十六进制值（Hexadecimal Value）：`0x2048`。

### 注释 209：原第 2069 行

十六进制值（Hexadecimal Value）：`0x2049`。

### 注释 210：原第 2071 行

十六进制值（Hexadecimal Value）：`0x204a`。

### 注释 211：原第 2077 行

十六进制值（Hexadecimal Value）：`0x204b`。

### 注释 212：原第 2084 行

十六进制值（Hexadecimal Value）：`0x204c`。

### 注释 213：原第 2091 行

十六进制值（Hexadecimal Value）：`0x204d`。

### 注释 214：原第 2100 行

十六进制值（Hexadecimal Value）：`0x204e`。

### 注释 215：原第 2111 行

十六进制值（Hexadecimal Value）：`0x204f`。

### 注释 216：原第 2123 行

十六进制值（Hexadecimal Value）：`0x2050`。

### 注释 217：原第 2136 行

恒定音调扩展（Constant Tone Extension）的最小和最大长度，以 8 微秒为单位。

### 注释 218：原第 2148 行

十六进制值（Hexadecimal Value）：`0x2051`。

### 注释 219：原第 2158 行

十六进制值（Hexadecimal Value）：`0x2052`。

### 注释 220：原第 2171 行

十六进制值（Hexadecimal Value）：`0x2053`。

### 注释 221：原第 2186 行

十六进制值（Hexadecimal Value）：`0x2054`。

### 注释 222：原第 2207 行

十六进制值（Hexadecimal Value）：`0x2055`。

### 注释 223：原第 2220 行

连续两次恒定音调扩展（CTE）请求过程开始之间的间隔，以连接事件（Connection Events）的数量表示。

### 注释 224：原第 2225 行

十六进制值（Hexadecimal Value）：`0x2056`。

### 注释 225：原第 2239 行

十六进制值（Hexadecimal Value）：`0x2057`。

### 注释 226：原第 2263 行

十六进制值（Hexadecimal Value）：`0x2058`。

### 注释 227：原第 2275 行

十六进制值（Hexadecimal Value）：`0x2059`。

### 注释 228：原第 2281 行

十六进制值（Hexadecimal Value）：`0x205a`。

### 注释 229：原第 2293 行

十六进制值（Hexadecimal Value）：`0x205b`。

### 注释 230：原第 2316 行

十六进制值（Hexadecimal Value）：`0x205c`。

### 注释 231：原第 2330 行

十六进制值（Hexadecimal Value）：`0x205d`。

### 注释 232：原第 2342 行

十六进制值（Hexadecimal Value）：`0x2060`。

### 注释 233：原第 2351 行

十六进制值（Hexadecimal Value）：`0x2061`。

### 注释 234：原第 2379 行

十六进制值（Hexadecimal Value）：`0x2062`。

### 注释 235：原第 2410 行

十六进制值（Hexadecimal Value）：`0x2063`。

### 注释 236：原第 2445 行

十六进制值（Hexadecimal Value）：`0x2064`。

### 注释 237：原第 2456 行

十六进制值（Hexadecimal Value）：`0x2065`。

### 注释 238：原第 2466 行

十六进制值（Hexadecimal Value）：`0x2066`。

### 注释 239：原第 2471 行

十六进制值（Hexadecimal Value）：`0x2067`。

### 注释 240：原第 2482 行

十六进制值（Hexadecimal Value）：`0x2068`。

### 注释 241：原第 2498 行

十六进制值（Hexadecimal Value）：`0x2069`。

### 注释 242：原第 2518 行

十六进制值（Hexadecimal Value）：`0x206a`。

### 注释 243：原第 2524 行

十六进制值（Hexadecimal Value）：`0x206b`。

### 注释 244：原第 2536 行

十六进制值（Hexadecimal Value）：`0x206c`。

### 注释 245：原第 2546 行

十六进制值（Hexadecimal Value）：`0x206d`。

### 注释 246：原第 2551 行

十六进制值（Hexadecimal Value）：`0x206e`。

### 注释 247：原第 2567 行

十六进制值（Hexadecimal Value）：`0x206f`。

### 注释 248：原第 2582 行

十六进制值（Hexadecimal Value）：`0x2070`。

### 注释 249：原第 2593 行

十六进制值（Hexadecimal Value）：`0x2071`。

### 注释 250：原第 2604 行

十六进制值（Hexadecimal Value）：`0x2072`。

### 注释 251：原第 2617 行

十六进制值（Hexadecimal Value）：`0x2073`。

### 注释 252：原第 2630 行

十六进制值（Hexadecimal Value）：`0x2074`。

### 注释 253：原第 2640 行

十六进制值（Hexadecimal Value）：`0x2075`。

### 注释 254：原第 2657 行

十六进制值（Hexadecimal Value）：`0x207B`。

### 注释 255：原第 2670 行

十六进制值（Hexadecimal Value）：`0x2087`。

### 注释 256：原第 2680 行

十六进制值（Hexadecimal Value）：`0x2088`。

### 注释 257：原第 2692 行

HCI Tx Test v4 命令中发送功率（Tx Power）参数的辅助结构体。该命令的前一个参数长度可变，因此为此参数单独提供结构体，有助于解包命令参数（Command Parameter Unpacking）。

### 注释 258：原第 2700 行

十六进制值（Hexadecimal Value）：`0x2089`。

### 注释 259：原第 2727 行

十六进制值（Hexadecimal Value）：`0x20A5`。

### 注释 260：原第 2782 行

十六进制值（Hexadecimal Value）：`0x208A`。

### 注释 261：原第 2789 行

十六进制值（Hexadecimal Value）：`0x208B`。

### 注释 262：原第 2817 行

十六进制值（Hexadecimal Value）：`0x20A6`。

### 注释 263：原第 2869 行

十六进制值（Hexadecimal Value）：`0x208C`。

### 注释 264：原第 2875 行

十六进制值（Hexadecimal Value）：`0x208D`。

### 注释 265：原第 2897 行

十六进制值（Hexadecimal Value）：`0x208E`。

### 注释 266：原第 2903 行

十六进制值（Hexadecimal Value）：`0x208F`。

### 注释 267：原第 2910 行

十六进制值（Hexadecimal Value）：`0x2092`。

### 注释 268：原第 2912 行

十六进制值（Hexadecimal Value）：`0x2093`。

### 注释 269：原第 2936 行

十六进制值（Hexadecimal Value）：`0x2094`。

### 注释 270：原第 2947 行

十六进制值（Hexadecimal Value）：`0x2095`。

### 注释 271：原第 3086 行

十六进制值（Hexadecimal Value）：`0x2090`。

### 注释 272：原第 3110 行

十六进制值（Hexadecimal Value）：`0x2091`。

### 注释 273：原第 3117 行

十六进制值（Hexadecimal Value）：`0x2096`。

### 注释 274：原第 3141 行

十六进制值（Hexadecimal Value）：`0x209D`。

### 注释 275：原第 3172 行

十六进制值（Hexadecimal Value）：`0x20A3`。

### 注释 276：原第 3186 行

十六进制值（Hexadecimal Value）：`0x20A2`。

### 注释 277：原第 3201 行

十六进制值（Hexadecimal Value）：`0x20A1`。

### 注释 278：原第 3203 行

事件定义（Event Definitions）。

### 注释 279：原第 3249 行

加密值（Encryption Value）。

### 注释 280：原第 3313 行

当前模式（Current mode）。

### 注释 281：原第 3336 行

链路密钥类型（Link Key Types）。

### 注释 282：原第 3354 行

溢出链路类型（Overflow Link Types）。

### 注释 283：原第 3599 行

已弃用的拼写错误别名（Deprecated Misspelled Aliases）：请改用 `BT_HCI_LE_SUPERVISION_TIMEOUT_{MIN,MAX}`。

### 注释 284：原第 3708 行

广播编码选择（Advertising Coding Selection）扩展广播报告中的物理层（PHY）取值，仅在启用 Kconfig 选项 `BT_EXT_ADV_CODING_SELECTION` 时使用。

### 注释 285：原第 3837 行

根据蓝牙 5.3 核心规范，状态字段（Status Field）可以具有以下值：

- 收到不带恒定音调扩展（CTE）的 `LL_CTE_RSP_PDU` 时，为 `BT_HCI_CTE_REQ_STATUS_RSP_WITHOUT_CTE`。
- 对端拒绝请求时，为其他控制器错误码（Controller Error Code）。

### 注释 286：原第 3980 行

本地发送功率（Local Transmit Power）已改变。

### 注释 287：原第 3982 行

远端发送功率（Remote Transmit Power）已改变。

### 注释 288：原第 3984 行

`HCI_LE_Read_Remote_Transmit_Power_Level` 命令已完成。

### 注释 289：原第 4325 行

条件编译配置（Configuration）标记：`CONFIG_LITTLE_ENDIAN`。

### 注释 290：原第 4339 行

条件编译配置（Configuration）标记：`CONFIG_LITTLE_ENDIAN`。

### 注释 291：原第 4352 行

条件编译配置（Configuration）标记：`CONFIG_LITTLE_ENDIAN`。

### 注释 292：原第 4370 行

条件编译配置（Configuration）标记：`CONFIG_LITTLE_ENDIAN`。

### 注释 293：原第 4392 行

条件编译配置（Configuration）标记：`CONFIG_LITTLE_ENDIAN`。

### 注释 294：原第 4409 行

条件编译配置（Configuration）标记：`CONFIG_LITTLE_ENDIAN`。

### 注释 295：原第 4429 行

条件编译配置（Configuration）标记：`CONFIG_LITTLE_ENDIAN`。

### 注释 296：原第 4465 行

条件编译配置（Configuration）标记：`CONFIG_LITTLE_ENDIAN`。

### 注释 297：原第 4484 行

条件编译配置（Configuration）标记：`CONFIG_LITTLE_ENDIAN`。

### 注释 298：原第 4533 行

事件掩码位（Event Mask Bits）。

### 注释 299：原第 4568 行

第 2 页（Page 2）。

### 注释 300：原第 4719 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_HCI_TYPES_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [bt_hci_sco_hdr](../bluetooth_hci_model_reference/P436_bt_hci_sco_hdr_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [handle](../bluetooth_hci_model_reference/P436_bt_hci_sco_hdr_结构体.md#a4b4c915bec966c17567c14e2df9c1581)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [len](../bluetooth_hci_model_reference/P436_bt_hci_sco_hdr_结构体.md#a158f67c3743684c28728b62db5cf2590)
- [bt_hci_evt_hdr](../bluetooth_hci_model_reference/P217_bt_hci_evt_hdr_结构体.md)
- [evt](../bluetooth_hci_model_reference/P217_bt_hci_evt_hdr_结构体.md#aba3aca89bfbe7e8cbd144765cb20fcea)
- [len](../bluetooth_hci_model_reference/P217_bt_hci_evt_hdr_结构体.md#a2d580a0c12b29d23002ee9d494c9e16d)
- [data](../bluetooth_hci_model_reference/P217_bt_hci_evt_hdr_结构体.md#a87654d507f7ce633a804299bff13abe2)
- [bt_hci_acl_hdr](../bluetooth_hci_model_reference/P001_bt_hci_acl_hdr_结构体.md)
- [handle](../bluetooth_hci_model_reference/P001_bt_hci_acl_hdr_结构体.md#a8c88ef62a848699e06c49f97e1169363)
- [len](../bluetooth_hci_model_reference/P001_bt_hci_acl_hdr_结构体.md#af55b9c9256f35ada5786e9e5dd1d01bf)
- [bt_hci_iso_sdu_hdr](../bluetooth_hci_model_reference/P313_bt_hci_iso_sdu_hdr_结构体.md)
- [sn](../bluetooth_hci_model_reference/P313_bt_hci_iso_sdu_hdr_结构体.md#a683d493de5d00e3b4c5169f6de498c13)
- [slen](../bluetooth_hci_model_reference/P313_bt_hci_iso_sdu_hdr_结构体.md#a626764862a3757a3119b6de799221ad1)
- [bt_hci_iso_sdu_ts_hdr](../bluetooth_hci_model_reference/P314_bt_hci_iso_sdu_ts_hdr_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ts](../bluetooth_hci_model_reference/P314_bt_hci_iso_sdu_ts_hdr_结构体.md#a657e03c5ef597f04cc21725f0bc227d4)
- [sdu](../bluetooth_hci_model_reference/P314_bt_hci_iso_sdu_ts_hdr_结构体.md#a3f81175b95f8eaeeeee71ee4bf401864)
- [bt_hci_iso_hdr](../bluetooth_hci_model_reference/P312_bt_hci_iso_hdr_结构体.md)
- [handle](../bluetooth_hci_model_reference/P312_bt_hci_iso_hdr_结构体.md#af5113383fbcd0e70828f986720c38572)
- [len](../bluetooth_hci_model_reference/P312_bt_hci_iso_hdr_结构体.md#ab33ae914a9eba85b35c78e45e0f5255f)
- [bt_hci_cmd_hdr](../bluetooth_hci_model_reference/P005_bt_hci_cmd_hdr_结构体.md)
- [opcode](../bluetooth_hci_model_reference/P005_bt_hci_cmd_hdr_结构体.md#a09c63aab094ca0f39bab44708fdb83e4)
- [param_len](../bluetooth_hci_model_reference/P005_bt_hci_cmd_hdr_结构体.md#afe2a97da8b473cafd3cc4e5e52dadf93)
- [bt_hci_op_inquiry](../bluetooth_hci_model_reference/P328_bt_hci_op_inquiry_结构体.md)
- [lap](../bluetooth_hci_model_reference/P328_bt_hci_op_inquiry_结构体.md#abdd03feccecbdbbb5d2c7c7f3213b62f)
- [length](../bluetooth_hci_model_reference/P328_bt_hci_op_inquiry_结构体.md#ae77fa706c9875b5568a4af26a7724d08)
- [num_rsp](../bluetooth_hci_model_reference/P328_bt_hci_op_inquiry_结构体.md#ac8ed23243dbd9a7c46fedd8abe9666f5)
- [bt_hci_cp_connect](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#a6f0753aad19d4c9591fa74152d151aa9)
- [packet_type](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#a652a4e01641893a8588110dc505ceea0)
- [pscan_rep_mode](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#a35b0e1f73f696aae2ca519e16d7bb668)
- [reserved](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#aef01fcac1b9792353bd8095e6911d6c3)
- [clock_offset](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#ac379ec381ad4cf6760750203924e5dda)
- [allow_role_switch](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#a7a3d772bfd4c83236f9f1ad657e33f17)
- [bt_hci_cp_disconnect](../bluetooth_hci_model_reference/P015_bt_hci_cp_disconnect_结构体.md)
- [handle](../bluetooth_hci_model_reference/P015_bt_hci_cp_disconnect_结构体.md#a9cb5bcd135082c37a19cce57ffa123ff)
- [reason](../bluetooth_hci_model_reference/P015_bt_hci_cp_disconnect_结构体.md#a8e10edb1e700c1ef38f39bf20b9b374f)
- [bt_hci_cp_connect_cancel](../bluetooth_hci_model_reference/P014_bt_hci_cp_connect_cancel_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P014_bt_hci_cp_connect_cancel_结构体.md#a2adaf1b708689525e44e9a9572f5f357)
- [bt_hci_rp_connect_cancel](../bluetooth_hci_model_reference/P335_bt_hci_rp_connect_cancel_结构体.md)
- [status](../bluetooth_hci_model_reference/P335_bt_hci_rp_connect_cancel_结构体.md#a05d0c9e4163bc62a57dba8618294eb65)
- [bdaddr](../bluetooth_hci_model_reference/P335_bt_hci_rp_connect_cancel_结构体.md#a0ccfcbd294aa067879ab8d7a41bc41c9)
- [bt_hci_cp_accept_conn_req](../bluetooth_hci_model_reference/P007_bt_hci_cp_accept_conn_req_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P007_bt_hci_cp_accept_conn_req_结构体.md#aa2954d98fdd42882cf7095e4ce7a3dc5)
- [role](../bluetooth_hci_model_reference/P007_bt_hci_cp_accept_conn_req_结构体.md#a95e445018d1b9da5a914f0845bb9dbad)
- [bt_hci_cp_setup_sync_conn](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md)
- [handle](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#ad065185846694fc0070bb366e642f1c7)
- [tx_bandwidth](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#aa35718e13a7d778c779be535c2b1945e)
- [rx_bandwidth](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#a137601ab44970782e2f3d4fcd2c8fcc2)
- [max_latency](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#a5ffb5e552d4913974a10a16083f82864)
- [content_format](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#a4d7df5b1aa714bc14d0b6c3cbccc5014)
- [retrans_effort](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#a61ebbc775d3ca0724ea173d72a96e0c0)
- [pkt_type](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#a6d4c16a4d77d3ee4f8f65ab18a0f192d)
- [bt_hci_cp_accept_sync_conn_req](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#a6a5a56d3a9d1a6d1064e7bd4c9fd333e)
- [tx_bandwidth](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#a53fe4c6d61dbb99f99aa445b2c47a8ef)
- [rx_bandwidth](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#aceda6dbd3e221ad080850e9635886a86)
- [max_latency](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#a4ba6dffd840ef868524b490d227fd085)
- [content_format](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#adba31b588bf12e852cc43b85c006aaa3)
- [retrans_effort](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#ab5ece67c5a1e62fc4124556eef743c26)
- [pkt_type](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#ab5d9c27ebdf45fb54b0c6330b5b095be)
- [bt_hci_cp_reject_conn_req](../bluetooth_hci_model_reference/P161_bt_hci_cp_reject_conn_req_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P161_bt_hci_cp_reject_conn_req_结构体.md#a9a1cb4173367c6f018fbd30a47c590b4)
- [reason](../bluetooth_hci_model_reference/P161_bt_hci_cp_reject_conn_req_结构体.md#a1c2e234d6d00296bc01962b95e849df0)
- [bt_hci_cp_link_key_reply](../bluetooth_hci_model_reference/P140_bt_hci_cp_link_key_reply_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P140_bt_hci_cp_link_key_reply_结构体.md#ab5221952fbcfe413d7c3bd3a441a9b17)
- [link_key](../bluetooth_hci_model_reference/P140_bt_hci_cp_link_key_reply_结构体.md#a2af0b4b55a5ffcff0221da841ba0cbba)
- [bt_hci_cp_link_key_neg_reply](../bluetooth_hci_model_reference/P139_bt_hci_cp_link_key_neg_reply_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P139_bt_hci_cp_link_key_neg_reply_结构体.md#aca3114707eb7c631af582626551619cd)
- [bt_hci_cp_pin_code_reply](../bluetooth_hci_model_reference/P148_bt_hci_cp_pin_code_reply_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P148_bt_hci_cp_pin_code_reply_结构体.md#a627800dcb580110be785576dfcc49bb1)
- [pin_len](../bluetooth_hci_model_reference/P148_bt_hci_cp_pin_code_reply_结构体.md#aa0cbf668608c3eb4998356ad7b18c01a)
- [pin_code](../bluetooth_hci_model_reference/P148_bt_hci_cp_pin_code_reply_结构体.md#afc4ed5ae429087f4692af716d6b56997)
- [bt_hci_rp_pin_code_reply](../bluetooth_hci_model_reference/P400_bt_hci_rp_pin_code_reply_结构体.md)
- [status](../bluetooth_hci_model_reference/P400_bt_hci_rp_pin_code_reply_结构体.md#a3f167661b8d3f63ab12e6f64fb33986b)
- [bdaddr](../bluetooth_hci_model_reference/P400_bt_hci_rp_pin_code_reply_结构体.md#afc7c991fd8050e8aae56b8587b5ee01d)
- [bt_hci_cp_pin_code_neg_reply](../bluetooth_hci_model_reference/P147_bt_hci_cp_pin_code_neg_reply_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P147_bt_hci_cp_pin_code_neg_reply_结构体.md#a8aec3ba6c530850dce0a2d7b7f7f86ee)
- [bt_hci_rp_pin_code_neg_reply](../bluetooth_hci_model_reference/P399_bt_hci_rp_pin_code_neg_reply_结构体.md)
- [status](../bluetooth_hci_model_reference/P399_bt_hci_rp_pin_code_neg_reply_结构体.md#a10bcc55407e22417256c464684a41e58)
- [bdaddr](../bluetooth_hci_model_reference/P399_bt_hci_rp_pin_code_neg_reply_结构体.md#a168caf2a517aa573bd6acaf48e414e9b)
- [bt_hci_cp_change_conn_packet_type](../bluetooth_hci_model_reference/P010_bt_hci_cp_change_conn_packet_type_结构体.md)
- [handle](../bluetooth_hci_model_reference/P010_bt_hci_cp_change_conn_packet_type_结构体.md#a082e5dae5f08a332cf6a1dd23917d87f)
- [packet_type](../bluetooth_hci_model_reference/P010_bt_hci_cp_change_conn_packet_type_结构体.md#a0b825740b5ff47db5bfaaea7950e7d53)
- [bt_hci_cp_auth_requested](../bluetooth_hci_model_reference/P009_bt_hci_cp_auth_requested_结构体.md)
- [handle](../bluetooth_hci_model_reference/P009_bt_hci_cp_auth_requested_结构体.md#a079490f8f8569e281ce16f13847cbf33)
- [bt_hci_cp_set_conn_encrypt](../bluetooth_hci_model_reference/P164_bt_hci_cp_set_conn_encrypt_结构体.md)
- [handle](../bluetooth_hci_model_reference/P164_bt_hci_cp_set_conn_encrypt_结构体.md#a39e0c40ed6e6e9387ae384fd122fca4b)
- [encrypt](../bluetooth_hci_model_reference/P164_bt_hci_cp_set_conn_encrypt_结构体.md#aa259563efd49d04a8886f74169fd30b1)
- [bt_hci_cp_remote_name_request](../bluetooth_hci_model_reference/P163_bt_hci_cp_remote_name_request_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P163_bt_hci_cp_remote_name_request_结构体.md#a5093f7bb70fa36f4948039d02d594e27)
- [pscan_rep_mode](../bluetooth_hci_model_reference/P163_bt_hci_cp_remote_name_request_结构体.md#aed0aea58ca6f5dc15220083d377cbf5c)
- [reserved](../bluetooth_hci_model_reference/P163_bt_hci_cp_remote_name_request_结构体.md#ab1883aa2b08d89f9c3190f338808a43c)
- [clock_offset](../bluetooth_hci_model_reference/P163_bt_hci_cp_remote_name_request_结构体.md#a5d7ea30052f8e4e2b3564659ca187c48)
- [bt_hci_cp_remote_name_cancel](../bluetooth_hci_model_reference/P162_bt_hci_cp_remote_name_cancel_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P162_bt_hci_cp_remote_name_cancel_结构体.md#a0b7b4362804077ce828aeeb2b8af86b9)
- [bt_hci_rp_remote_name_cancel](../bluetooth_hci_model_reference/P420_bt_hci_rp_remote_name_cancel_结构体.md)
- [status](../bluetooth_hci_model_reference/P420_bt_hci_rp_remote_name_cancel_结构体.md#ac7fadee392b126cb50cef7a6336926cb)
- [bdaddr](../bluetooth_hci_model_reference/P420_bt_hci_rp_remote_name_cancel_结构体.md#a455432799a1272f88b2b00a35a2e7ef5)
- [bt_hci_cp_read_remote_features](../bluetooth_hci_model_reference/P157_bt_hci_cp_read_remote_features_结构体.md)
- [handle](../bluetooth_hci_model_reference/P157_bt_hci_cp_read_remote_features_结构体.md#ae14362a04c00b37342f3cc413f3933d3)
- [bt_hci_cp_read_remote_ext_features](../bluetooth_hci_model_reference/P156_bt_hci_cp_read_remote_ext_features_结构体.md)
- [handle](../bluetooth_hci_model_reference/P156_bt_hci_cp_read_remote_ext_features_结构体.md#aaa236c11d148252e34fd20d794d991f3)
- [page](../bluetooth_hci_model_reference/P156_bt_hci_cp_read_remote_ext_features_结构体.md#a6aff189605b276998e58b051429a5cd2)
- [bt_hci_cp_read_remote_version_info](../bluetooth_hci_model_reference/P158_bt_hci_cp_read_remote_version_info_结构体.md)
- [handle](../bluetooth_hci_model_reference/P158_bt_hci_cp_read_remote_version_info_结构体.md#a504b83f16a82b1e179d74547c7a29bf3)
- [bt_hci_cp_io_capability_reply](../bluetooth_hci_model_reference/P020_bt_hci_cp_io_capability_reply_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P020_bt_hci_cp_io_capability_reply_结构体.md#afbe2bc0c1dcc0791a98068b052aea1f2)
- [capability](../bluetooth_hci_model_reference/P020_bt_hci_cp_io_capability_reply_结构体.md#a0995c81ba1f653c59bda9a444fb17915)
- [oob_data](../bluetooth_hci_model_reference/P020_bt_hci_cp_io_capability_reply_结构体.md#ac002ea0b276200a15d603b5ac83666e5)
- [authentication](../bluetooth_hci_model_reference/P020_bt_hci_cp_io_capability_reply_结构体.md#a8983418dca3a7725f3b113a4d0ee177e)
- [bt_hci_cp_user_confirm_reply](../bluetooth_hci_model_reference/P172_bt_hci_cp_user_confirm_reply_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P172_bt_hci_cp_user_confirm_reply_结构体.md#abe0e8da3e590c565364ed30ba107a0e6)
- [bt_hci_rp_user_confirm_reply](../bluetooth_hci_model_reference/P422_bt_hci_rp_user_confirm_reply_结构体.md)
- [status](../bluetooth_hci_model_reference/P422_bt_hci_rp_user_confirm_reply_结构体.md#ab07114550c2da3c1e9925cb883bf3a89)
- [bdaddr](../bluetooth_hci_model_reference/P422_bt_hci_rp_user_confirm_reply_结构体.md#a91678db3ae2a696ba7b9dd5bc080c488)
- [bt_hci_cp_user_passkey_reply](../bluetooth_hci_model_reference/P174_bt_hci_cp_user_passkey_reply_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P174_bt_hci_cp_user_passkey_reply_结构体.md#a56dbb4a858ecbf36eee61e24ed3742cf)
- [passkey](../bluetooth_hci_model_reference/P174_bt_hci_cp_user_passkey_reply_结构体.md#a80483025a32f37e7f75b3a220d48148c)
- [bt_hci_cp_user_passkey_neg_reply](../bluetooth_hci_model_reference/P173_bt_hci_cp_user_passkey_neg_reply_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P173_bt_hci_cp_user_passkey_neg_reply_结构体.md#ade9d7068054b15089b8c238ecc3e4397)
- [bt_hci_cp_io_capability_neg_reply](../bluetooth_hci_model_reference/P019_bt_hci_cp_io_capability_neg_reply_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P019_bt_hci_cp_io_capability_neg_reply_结构体.md#a8dba05bc84de2573eaea43ea9e428015)
- [reason](../bluetooth_hci_model_reference/P019_bt_hci_cp_io_capability_neg_reply_结构体.md#a82c54e5ad7fd4a6d81952832ae4de373)
- [bt_hci_cp_switch_role](../bluetooth_hci_model_reference/P171_bt_hci_cp_switch_role_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P171_bt_hci_cp_switch_role_结构体.md#afed76d83e552fa3666f8c84df4279938)
- [role](../bluetooth_hci_model_reference/P171_bt_hci_cp_switch_role_结构体.md#ac6b6acdaf5993384eb3029c9e78407b6)
- [bt_hci_cp_read_link_policy_settings](../bluetooth_hci_model_reference/P153_bt_hci_cp_read_link_policy_settings_结构体.md)
- [handle](../bluetooth_hci_model_reference/P153_bt_hci_cp_read_link_policy_settings_结构体.md#abd2d7c4074428367213b6599dee2f9d8)
- [bt_hci_rp_read_link_policy_settings](../bluetooth_hci_model_reference/P412_bt_hci_rp_read_link_policy_settings_结构体.md)
- [status](../bluetooth_hci_model_reference/P412_bt_hci_rp_read_link_policy_settings_结构体.md#ad73d8ed381f8bbc4914c38bb0ebcae01)
- [handle](../bluetooth_hci_model_reference/P412_bt_hci_rp_read_link_policy_settings_结构体.md#a4ec0cdfa8ae48d9ed8ae2d46f16a9638)
- [link_policy_settings](../bluetooth_hci_model_reference/P412_bt_hci_rp_read_link_policy_settings_结构体.md#a69fe8085d161bf87051a52dc9c511156)
- [bt_hci_cp_write_link_policy_settings](../bluetooth_hci_model_reference/P194_bt_hci_cp_write_link_policy_settings_结构体.md)
- [handle](../bluetooth_hci_model_reference/P194_bt_hci_cp_write_link_policy_settings_结构体.md#af3ed335fb8a8774c19ee024c2750e6dc)
- [link_policy_settings](../bluetooth_hci_model_reference/P194_bt_hci_cp_write_link_policy_settings_结构体.md#a1ba4bd293579e0175efff88429ca1aec)
- [bt_hci_rp_read_default_link_policy_settings](../bluetooth_hci_model_reference/P410_bt_hci_rp_read_default_link_policy_settings_结构体.md)
- [status](../bluetooth_hci_model_reference/P410_bt_hci_rp_read_default_link_policy_settings_结构体.md#ad2ba59e00a2f2931dd52809029373f46)
- [default_link_policy_settings](../bluetooth_hci_model_reference/P410_bt_hci_rp_read_default_link_policy_settings_结构体.md#a0b4c5e26b1d7f387a86192edd1efcdf2)
- [bt_hci_cp_write_default_link_policy_settings](../bluetooth_hci_model_reference/P188_bt_hci_cp_write_default_link_policy_settings_结构体.md)
- [default_link_policy_settings](../bluetooth_hci_model_reference/P188_bt_hci_cp_write_default_link_policy_settings_结构体.md#a644c1ef9ba45ee0675824628fcb9e88a)
- [bt_hci_cp_sniff_mode](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md)
- [handle](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md#a37cc61e67148cf8993aa3c6410094d7e)
- [max_interval](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md#ad765b1aebc101886d5e9805245252718)
- [min_interval](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md#aaba62465c5fb76641715eed4bc8c25e9)
- [attempt](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md#a1896272c588ed2ffe0052353eed528c4)
- [timeout](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md#aa0bfa66eb627378a820144b8ca748b5f)
- [bt_hci_cp_exit_sniff_mode](../bluetooth_hci_model_reference/P016_bt_hci_cp_exit_sniff_mode_结构体.md)
- [handle](../bluetooth_hci_model_reference/P016_bt_hci_cp_exit_sniff_mode_结构体.md#a706cc1a951f21889a28e0b555587bb98)
- [bt_hci_cp_sniff_subrating](../bluetooth_hci_model_reference/P170_bt_hci_cp_sniff_subrating_结构体.md)
- [handle](../bluetooth_hci_model_reference/P170_bt_hci_cp_sniff_subrating_结构体.md#af25eb1e9ee6eef5888ffa31b9fdd2887)
- [max_latency](../bluetooth_hci_model_reference/P170_bt_hci_cp_sniff_subrating_结构体.md#a3534ddbf9876a82855b569ef7e01fd96)
- [min_remote_timeout](../bluetooth_hci_model_reference/P170_bt_hci_cp_sniff_subrating_结构体.md#ab11c374063c6219b942b839f10d6a74d)
- [min_local_timeout](../bluetooth_hci_model_reference/P170_bt_hci_cp_sniff_subrating_结构体.md#aa6de505cd8ba606d893dc74590083963)
- [bt_hci_rp_sniff_subrating](../bluetooth_hci_model_reference/P421_bt_hci_rp_sniff_subrating_结构体.md)
- [status](../bluetooth_hci_model_reference/P421_bt_hci_rp_sniff_subrating_结构体.md#aa5d11db99d6f467a1e93afe031c08e14)
- [handle](../bluetooth_hci_model_reference/P421_bt_hci_rp_sniff_subrating_结构体.md#a39e9f3ec6e7d9c534ca6160172990fa6)
- [bt_hci_cp_set_event_mask](../bluetooth_hci_model_reference/P166_bt_hci_cp_set_event_mask_结构体.md)
- [events](../bluetooth_hci_model_reference/P166_bt_hci_cp_set_event_mask_结构体.md#ab3af227511f47ee03f2d6aba8ae65c5d)
- [bt_hci_write_local_name](../bluetooth_hci_model_reference/P450_bt_hci_write_local_name_结构体.md)
- [local_name](../bluetooth_hci_model_reference/P450_bt_hci_write_local_name_结构体.md#a8d2cd9a16525c3fc10ae0e3f196110da)
- [bt_hci_rp_read_conn_accept_timeout](../bluetooth_hci_model_reference/P408_bt_hci_rp_read_conn_accept_timeout_结构体.md)
- [status](../bluetooth_hci_model_reference/P408_bt_hci_rp_read_conn_accept_timeout_结构体.md#afeb5888722ee368e02c6b27b75ab2a70)
- [conn_accept_timeout](../bluetooth_hci_model_reference/P408_bt_hci_rp_read_conn_accept_timeout_结构体.md#a01ca30c92311ec1df19a4cf835ea74cf)
- [bt_hci_cp_write_conn_accept_timeout](../bluetooth_hci_model_reference/P186_bt_hci_cp_write_conn_accept_timeout_结构体.md)
- [conn_accept_timeout](../bluetooth_hci_model_reference/P186_bt_hci_cp_write_conn_accept_timeout_结构体.md#a13de5f88920c6a41dafa598734b7acf9)
- [bt_hci_rp_write_conn_accept_timeout](../bluetooth_hci_model_reference/P435_bt_hci_rp_write_conn_accept_timeout_结构体.md)
- [status](../bluetooth_hci_model_reference/P435_bt_hci_rp_write_conn_accept_timeout_结构体.md#a1f9eee1a5843747e0d224b86b602a3da)
- [bt_hci_cp_write_page_scan_activity](../bluetooth_hci_model_reference/P196_bt_hci_cp_write_page_scan_activity_结构体.md)
- [interval](../bluetooth_hci_model_reference/P196_bt_hci_cp_write_page_scan_activity_结构体.md#a9b73713d2960e78a7d6cf1a96c611495)
- [window](../bluetooth_hci_model_reference/P196_bt_hci_cp_write_page_scan_activity_结构体.md#a8047c7b908154b23985c95a1d792007a)
- [bt_hci_cp_write_inquiry_scan_activity](../bluetooth_hci_model_reference/P191_bt_hci_cp_write_inquiry_scan_activity_结构体.md)
- [interval](../bluetooth_hci_model_reference/P191_bt_hci_cp_write_inquiry_scan_activity_结构体.md#affe95468faed405a95073b5ba811a053)
- [window](../bluetooth_hci_model_reference/P191_bt_hci_cp_write_inquiry_scan_activity_结构体.md#aca01d404676b965f2a03ae16080b8fae)
- [bt_hci_rp_read_class_of_device](../bluetooth_hci_model_reference/P404_bt_hci_rp_read_class_of_device_结构体.md)
- [status](../bluetooth_hci_model_reference/P404_bt_hci_rp_read_class_of_device_结构体.md#a221d175e8016fd04151c4969d1134910)
- [class_of_device](../bluetooth_hci_model_reference/P404_bt_hci_rp_read_class_of_device_结构体.md#ac6483440d3095de548f477cd845c0cee)
- [bt_hci_cp_write_class_of_device](../bluetooth_hci_model_reference/P185_bt_hci_cp_write_class_of_device_结构体.md)
- [class_of_device](../bluetooth_hci_model_reference/P185_bt_hci_cp_write_class_of_device_结构体.md#acc3b940de1a5da095e8a4f18e69229f2)
- [bt_hci_cp_read_tx_power_level](../bluetooth_hci_model_reference/P160_bt_hci_cp_read_tx_power_level_结构体.md)
- [handle](../bluetooth_hci_model_reference/P160_bt_hci_cp_read_tx_power_level_结构体.md#a1c268364fc80b9478d70b7eb997d9825)
- [type](../bluetooth_hci_model_reference/P160_bt_hci_cp_read_tx_power_level_结构体.md#a1920e671ec2deda1daf47f06a86d2881)
- [bt_hci_rp_read_tx_power_level](../bluetooth_hci_model_reference/P419_bt_hci_rp_read_tx_power_level_结构体.md)
- [status](../bluetooth_hci_model_reference/P419_bt_hci_rp_read_tx_power_level_结构体.md#af40a8e2e663872e8d9fdde839cc6d1b4)
- [handle](../bluetooth_hci_model_reference/P419_bt_hci_rp_read_tx_power_level_结构体.md#ac2bd21e90145102bc483c2b0b3cdd416)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [tx_power_level](../bluetooth_hci_model_reference/P419_bt_hci_rp_read_tx_power_level_结构体.md#a46526b820038bb445a7824a7b4bfc870)
- [bt_hci_cp_le_read_tx_power_level](../bluetooth_hci_model_reference/P069_bt_hci_cp_le_read_tx_power_level_结构体.md)
- [handle](../bluetooth_hci_model_reference/P069_bt_hci_cp_le_read_tx_power_level_结构体.md#af8c2d89b183d7bdc0f55a0bf783a373d)
- [phy](../bluetooth_hci_model_reference/P069_bt_hci_cp_le_read_tx_power_level_结构体.md#a4863396dfe4dca65aaef68293e29291b)
- [bt_hci_rp_le_read_tx_power_level](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md)
- [status](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md#a4c83db208bfcb7c9fd2211d192a26d90)
- [handle](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md#aec00dfb34abce2d95af183b74f63d1f3)
- [phy](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md#ae65a43aad74b1081e88afdb533cbe813)
- [current_tx_power_level](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md#ad14f660eb67f1014d1a62b0e5a113969)
- [max_tx_power_level](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md#a5f9c59660f7c5842712a4ad9ae1d9527)
- [bt_hci_cp_le_set_tx_power_report_enable](../bluetooth_hci_model_reference/P125_bt_hci_cp_le_set_tx_power_report_enable_结构体.md)
- [handle](../bluetooth_hci_model_reference/P125_bt_hci_cp_le_set_tx_power_report_enable_结构体.md#a4a37c87f8f6a966a90c5de09096d1356)
- [local_enable](../bluetooth_hci_model_reference/P125_bt_hci_cp_le_set_tx_power_report_enable_结构体.md#a30580470d1ba516d86c8b157ca415ef3)
- [remote_enable](../bluetooth_hci_model_reference/P125_bt_hci_cp_le_set_tx_power_report_enable_结构体.md#ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e)
- [bt_hci_cp_le_set_path_loss_reporting_parameters](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md)
- [handle](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#a2dec83b0269835538cf4bc5553483f19)
- [high_threshold](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#ac8b7b832ba241c0448c80be22249b3ca)
- [high_hysteresis](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#ab5de762b7b82c8f453dafe1ea9bbf46d)
- [low_threshold](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#a79a53ca3a481e013a5ee892d779e7bfd)
- [low_hysteresis](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#a28f79bd4ccec4ed108e20a0080ec842d)
- [min_time_spent](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#a2289e8198eea1686030ffd3e225c8e7d)
- [bt_hci_rp_le_set_path_loss_reporting_parameters](../bluetooth_hci_model_reference/P390_bt_hci_rp_le_set_path_loss_reporting_parameters_结构体.md)
- [handle](../bluetooth_hci_model_reference/P390_bt_hci_rp_le_set_path_loss_reporting_parameters_结构体.md#a7a2fb4061792d4cc004c77ac8d5e84dc)
- [status](../bluetooth_hci_model_reference/P390_bt_hci_rp_le_set_path_loss_reporting_parameters_结构体.md#afeb9563db35ddba7ed9de6070463c508)
- [bt_hci_cp_le_set_path_loss_reporting_enable](../bluetooth_hci_model_reference/P106_bt_hci_cp_le_set_path_loss_reporting_enable_结构体.md)
- [handle](../bluetooth_hci_model_reference/P106_bt_hci_cp_le_set_path_loss_reporting_enable_结构体.md#a79487ac2235da100b41ec50c77bad808)
- [enable](../bluetooth_hci_model_reference/P106_bt_hci_cp_le_set_path_loss_reporting_enable_结构体.md#a209a77ef3cf545150feaecdb814797f0)
- [bt_hci_rp_le_set_path_loss_reporting_enable](../bluetooth_hci_model_reference/P389_bt_hci_rp_le_set_path_loss_reporting_enable_结构体.md)
- [handle](../bluetooth_hci_model_reference/P389_bt_hci_rp_le_set_path_loss_reporting_enable_结构体.md#a3ea4ffd2a32c8fb720ce555db4585888)
- [status](../bluetooth_hci_model_reference/P389_bt_hci_rp_le_set_path_loss_reporting_enable_结构体.md#a27991d6f123fabf13ecd926cff4e5637)
- [bt_hci_cp_le_set_default_subrate](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md)
- [subrate_min](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md#a9d8fd7cad5260c8943b90ab50c04b225)
- [subrate_max](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md#ad18a8042c38a1b4d83d6fccad1ab5af8)
- [max_latency](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md#a16adacc30fd5ae00b3944f068b075b1a)
- [continuation_number](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md#aff2e682b4c8e5c3078885be126c5b958)
- [supervision_timeout](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md#a1906f4dd7955200c81093b8f7c5d55c0)
- [bt_hci_cp_le_subrate_request](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md)
- [handle](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#a2595419182358e3386a0fb6e523a3dda)
- [subrate_min](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#a18ba526d8a843ad9c74c22d0899d9c1f)
- [subrate_max](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#a5c95a2bea462fb72d34d6314046041b7)
- [max_latency](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#a04ccc83303baabf30b663983883e7e77)
- [continuation_number](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#ab32a92ed52266c6b7d6d9ab08787e770)
- [supervision_timeout](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#a60bcbe27605063725422a0b1c35f21e7)
- [bt_hci_cp_set_ctl_to_host_flow](../bluetooth_hci_model_reference/P165_bt_hci_cp_set_ctl_to_host_flow_结构体.md)
- [flow_enable](../bluetooth_hci_model_reference/P165_bt_hci_cp_set_ctl_to_host_flow_结构体.md#a75b614de1ab1fbfc6aa9c11d833976a6)
- [bt_hci_cp_host_buffer_size](../bluetooth_hci_model_reference/P017_bt_hci_cp_host_buffer_size_结构体.md)
- [acl_mtu](../bluetooth_hci_model_reference/P017_bt_hci_cp_host_buffer_size_结构体.md#a07039a81ba81c700a26009ea407744b6)
- [sco_mtu](../bluetooth_hci_model_reference/P017_bt_hci_cp_host_buffer_size_结构体.md#a1b1d8c7f60ecbb13699b815bc8fca550)
- [acl_pkts](../bluetooth_hci_model_reference/P017_bt_hci_cp_host_buffer_size_结构体.md#a8240837fecc7c50461724b697f0eda47)
- [sco_pkts](../bluetooth_hci_model_reference/P017_bt_hci_cp_host_buffer_size_结构体.md#a943252480194e1a8608951be08b6b91c)
- [bt_hci_handle_count](../bluetooth_hci_model_reference/P310_bt_hci_handle_count_结构体.md)
- [handle](../bluetooth_hci_model_reference/P310_bt_hci_handle_count_结构体.md#acacc000905835724b7fe882a8ad85f82)
- [count](../bluetooth_hci_model_reference/P310_bt_hci_handle_count_结构体.md#a71577f376985909744fa14f246e69e1d)
- [bt_hci_cp_host_num_completed_packets](../bluetooth_hci_model_reference/P018_bt_hci_cp_host_num_completed_packets_结构体.md)
- [num_handles](../bluetooth_hci_model_reference/P018_bt_hci_cp_host_num_completed_packets_结构体.md#a43a42e52757de9ec307e8a828dff416f)
- [h](../bluetooth_hci_model_reference/P018_bt_hci_cp_host_num_completed_packets_结构体.md#a127f146b4967de49bc74b90ce1643eb7)
- [bt_hci_cp_read_link_supervision_timeout](../bluetooth_hci_model_reference/P154_bt_hci_cp_read_link_supervision_timeout_结构体.md)
- [handle](../bluetooth_hci_model_reference/P154_bt_hci_cp_read_link_supervision_timeout_结构体.md#a96f55e4c89154f5ff911d114a23dc3e4)
- [bt_hci_rp_read_link_supervision_timeout](../bluetooth_hci_model_reference/P413_bt_hci_rp_read_link_supervision_timeout_结构体.md)
- [status](../bluetooth_hci_model_reference/P413_bt_hci_rp_read_link_supervision_timeout_结构体.md#a1400aa0d8172c0cbf6b24b6571e73f73)
- [handle](../bluetooth_hci_model_reference/P413_bt_hci_rp_read_link_supervision_timeout_结构体.md#aec86b11707e4728dd0849f12c32cf8f8)
- [timeout](../bluetooth_hci_model_reference/P413_bt_hci_rp_read_link_supervision_timeout_结构体.md#ad1048becb6523d7302fdbbd739bc1b99)
- [bt_hci_cp_write_link_supervision_timeout](../bluetooth_hci_model_reference/P195_bt_hci_cp_write_link_supervision_timeout_结构体.md)
- [handle](../bluetooth_hci_model_reference/P195_bt_hci_cp_write_link_supervision_timeout_结构体.md#a1f33613e27db275806eaaa909591e882)
- [timeout](../bluetooth_hci_model_reference/P195_bt_hci_cp_write_link_supervision_timeout_结构体.md#a2dd05ca57e20ee4b4fbe2b29cc746bee)
- [bt_hci_iac_lap](../bluetooth_hci_model_reference/P311_bt_hci_iac_lap_结构体.md)
- [iac](../bluetooth_hci_model_reference/P311_bt_hci_iac_lap_结构体.md#ac729dc24f337c32b1ffd0e212ccf49ff)
- [bt_hci_cp_write_current_iac_lap](../bluetooth_hci_model_reference/P187_bt_hci_cp_write_current_iac_lap_结构体.md)
- [num_current_iac](../bluetooth_hci_model_reference/P187_bt_hci_cp_write_current_iac_lap_结构体.md#aaaf3e9c66729a3b4081abb5f8a954108)
- [lap](../bluetooth_hci_model_reference/P187_bt_hci_cp_write_current_iac_lap_结构体.md#ad44e9a0d65bc5140e313176f5b98e932)
- [bt_hci_cp_write_inquiry_scan_type](../bluetooth_hci_model_reference/P192_bt_hci_cp_write_inquiry_scan_type_结构体.md)
- [type](../bluetooth_hci_model_reference/P192_bt_hci_cp_write_inquiry_scan_type_结构体.md#a6342e77d0c83c1b7c8fd3bd1eeddf8b4)
- [bt_hci_cp_write_inquiry_mode](../bluetooth_hci_model_reference/P190_bt_hci_cp_write_inquiry_mode_结构体.md)
- [mode](../bluetooth_hci_model_reference/P190_bt_hci_cp_write_inquiry_mode_结构体.md#a827e138b7faaec54ec84a1cc1e0c480f)
- [bt_hci_cp_write_page_scan_type](../bluetooth_hci_model_reference/P197_bt_hci_cp_write_page_scan_type_结构体.md)
- [type](../bluetooth_hci_model_reference/P197_bt_hci_cp_write_page_scan_type_结构体.md#a1717b5ec6e83966e8ef4b61d2ee903a6)
- [bt_hci_cp_write_ext_inquiry_response](../bluetooth_hci_model_reference/P189_bt_hci_cp_write_ext_inquiry_response_结构体.md)
- [fec_required](../bluetooth_hci_model_reference/P189_bt_hci_cp_write_ext_inquiry_response_结构体.md#a755167d683df6c408de57122847bfce0)
- [eir](../bluetooth_hci_model_reference/P189_bt_hci_cp_write_ext_inquiry_response_结构体.md#ae9c89c1f4cac0f16d41b926dc6abc898)
- [BT_HCI_EIR_MAX_DATA_LEN](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a08260407c93741e254a4427ba42c274d)
- [bt_hci_cp_write_ssp_mode](../bluetooth_hci_model_reference/P199_bt_hci_cp_write_ssp_mode_结构体.md)
- [mode](../bluetooth_hci_model_reference/P199_bt_hci_cp_write_ssp_mode_结构体.md#a8ebf7f7890adec53aa8c2307d2b1a33f)
- [bt_hci_cp_set_event_mask_page_2](../bluetooth_hci_model_reference/P167_bt_hci_cp_set_event_mask_page_2_结构体.md)
- [events_page_2](../bluetooth_hci_model_reference/P167_bt_hci_cp_set_event_mask_page_2_结构体.md#aacf1308d0892226e2c10216a07cd1fcc)
- [bt_hci_cp_write_le_host_supp](../bluetooth_hci_model_reference/P193_bt_hci_cp_write_le_host_supp_结构体.md)
- [le](../bluetooth_hci_model_reference/P193_bt_hci_cp_write_le_host_supp_结构体.md#ace1838a80b6061231b536f36e8999ac0)
- [simul](../bluetooth_hci_model_reference/P193_bt_hci_cp_write_le_host_supp_结构体.md#ad2c27c0f98b2334490022e90563e1271)
- [bt_hci_cp_write_sc_host_supp](../bluetooth_hci_model_reference/P198_bt_hci_cp_write_sc_host_supp_结构体.md)
- [sc_support](../bluetooth_hci_model_reference/P198_bt_hci_cp_write_sc_host_supp_结构体.md#a48ef951f4de05c5772be5c08edca7cec)
- [bt_hci_cp_read_auth_payload_timeout](../bluetooth_hci_model_reference/P149_bt_hci_cp_read_auth_payload_timeout_结构体.md)
- [handle](../bluetooth_hci_model_reference/P149_bt_hci_cp_read_auth_payload_timeout_结构体.md#adcdd657feb3ea6b892e2a5034365dd77)
- [bt_hci_rp_read_auth_payload_timeout](../bluetooth_hci_model_reference/P401_bt_hci_rp_read_auth_payload_timeout_结构体.md)
- [status](../bluetooth_hci_model_reference/P401_bt_hci_rp_read_auth_payload_timeout_结构体.md#a3eadeab880eb75c914be654dbc685f3f)
- [handle](../bluetooth_hci_model_reference/P401_bt_hci_rp_read_auth_payload_timeout_结构体.md#ab53b7e03c68dcd040e38fdc7429b2d3b)
- [auth_payload_timeout](../bluetooth_hci_model_reference/P401_bt_hci_rp_read_auth_payload_timeout_结构体.md#ab4092720dad9a01f4e179eb2f0112aed)
- [bt_hci_cp_write_auth_payload_timeout](../bluetooth_hci_model_reference/P184_bt_hci_cp_write_auth_payload_timeout_结构体.md)
- [handle](../bluetooth_hci_model_reference/P184_bt_hci_cp_write_auth_payload_timeout_结构体.md#ad99d5b9f416f11492ac0f412b400aeb6)
- [auth_payload_timeout](../bluetooth_hci_model_reference/P184_bt_hci_cp_write_auth_payload_timeout_结构体.md#a385c88012b09ec561b9ba7edaadeb574)
- [bt_hci_rp_write_auth_payload_timeout](../bluetooth_hci_model_reference/P434_bt_hci_rp_write_auth_payload_timeout_结构体.md)
- [status](../bluetooth_hci_model_reference/P434_bt_hci_rp_write_auth_payload_timeout_结构体.md#af1783a29e6a167fc20b62bd273215b35)
- [handle](../bluetooth_hci_model_reference/P434_bt_hci_rp_write_auth_payload_timeout_结构体.md#a467c6585c913dba03dcfdf5bf4fa688e)
- [bt_hci_cp_configure_data_path](../bluetooth_hci_model_reference/P012_bt_hci_cp_configure_data_path_结构体.md)
- [data_path_dir](../bluetooth_hci_model_reference/P012_bt_hci_cp_configure_data_path_结构体.md#a528ba2bd5a220d1b7db064f8b51a8718)
- [data_path_id](../bluetooth_hci_model_reference/P012_bt_hci_cp_configure_data_path_结构体.md#a92967e6b5258b2acd6d82bfbfb8b7940)
- [vs_config_len](../bluetooth_hci_model_reference/P012_bt_hci_cp_configure_data_path_结构体.md#a2573fe029e1774bf5fa7e8cffff08cec)
- [vs_config](../bluetooth_hci_model_reference/P012_bt_hci_cp_configure_data_path_结构体.md#aa79c4aa6603b09f49a8c7f216f135e6e)
- [bt_hci_rp_configure_data_path](../bluetooth_hci_model_reference/P334_bt_hci_rp_configure_data_path_结构体.md)
- [status](../bluetooth_hci_model_reference/P334_bt_hci_rp_configure_data_path_结构体.md#a10cfe9bf5a7be202706957d7b8e1f371)
- [bt_hci_rp_read_local_version_info](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md)
- [status](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a935f990f7c28f7c89660c2b8ab975f43)
- [hci_version](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a1cc521426e530344a328e935152dd488)
- [hci_revision](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a04161ed3cc0b9c3c442e3464501ce118)
- [lmp_version](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a634641751852f66aabb408bf1b4d0cd2)
- [manufacturer](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a7cd6ba190137eaf7c4eb9c2d7e5b36ce)
- [lmp_subversion](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a43f29cf08a2399e818bfa441c6b7a1f3)
- [bt_hci_rp_read_supported_commands](../bluetooth_hci_model_reference/P418_bt_hci_rp_read_supported_commands_结构体.md)
- [status](../bluetooth_hci_model_reference/P418_bt_hci_rp_read_supported_commands_结构体.md#a3d36d892f83cfcb1d2fc955ec71ff061)
- [commands](../bluetooth_hci_model_reference/P418_bt_hci_rp_read_supported_commands_结构体.md#afd0dc4411a4c7692515139392bffedd0)
- [bt_hci_cp_read_local_ext_features](../bluetooth_hci_model_reference/P155_bt_hci_cp_read_local_ext_features_结构体.md)
- [page](../bluetooth_hci_model_reference/P155_bt_hci_cp_read_local_ext_features_结构体.md#a79c6a6a6f1026a7e9ee774183ea7e132)
- [bt_hci_rp_read_local_ext_features](../bluetooth_hci_model_reference/P414_bt_hci_rp_read_local_ext_features_结构体.md)
- [status](../bluetooth_hci_model_reference/P414_bt_hci_rp_read_local_ext_features_结构体.md#a9011f2c89f75939fa92fcf249d2203da)
- [page](../bluetooth_hci_model_reference/P414_bt_hci_rp_read_local_ext_features_结构体.md#a7e3669651dc2c2ed9541b7e4945a27f9)
- [max_page](../bluetooth_hci_model_reference/P414_bt_hci_rp_read_local_ext_features_结构体.md#a3532e208b3fd347db80d8c55eade3c2d)
- [ext_features](../bluetooth_hci_model_reference/P414_bt_hci_rp_read_local_ext_features_结构体.md#a669e8c6faa4e45f472e4f8a3ebb03050)
- [bt_hci_rp_read_local_features](../bluetooth_hci_model_reference/P415_bt_hci_rp_read_local_features_结构体.md)
- [status](../bluetooth_hci_model_reference/P415_bt_hci_rp_read_local_features_结构体.md#a0ff73da5704ada47f8f79c113254820d)
- [features](../bluetooth_hci_model_reference/P415_bt_hci_rp_read_local_features_结构体.md#ae660b4a772f96bf72bd08124bf26b352)
- [bt_hci_rp_read_buffer_size](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md)
- [status](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md#a6adf126acfcec722dc078d097d2b2ba8)
- [acl_max_len](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md#aba3f1597c929e3721c769beb98000218)
- [sco_max_len](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md#a7d475559145f469006b2ef147704cd99)
- [acl_max_num](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md#a87ff361282be71aa60c7f88c50a7492f)
- [sco_max_num](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md#abc01fa1df6d787f0a2cb865daed5f4cc)
- [bt_hci_rp_read_bd_addr](../bluetooth_hci_model_reference/P402_bt_hci_rp_read_bd_addr_结构体.md)
- [status](../bluetooth_hci_model_reference/P402_bt_hci_rp_read_bd_addr_结构体.md#a5230de2a3a6c4161d076b59901790e1e)
- [bdaddr](../bluetooth_hci_model_reference/P402_bt_hci_rp_read_bd_addr_结构体.md#aec2c022a465982a3868100699c95f4e6)
- [bt_hci_std_codec_info](../bluetooth_hci_model_reference/P438_bt_hci_std_codec_info_结构体.md)
- [codec_id](../bluetooth_hci_model_reference/P438_bt_hci_std_codec_info_结构体.md#a56e21eca5bbc83cb081aea1c67a7a60d)
- [bt_hci_std_codecs](../bluetooth_hci_model_reference/P440_bt_hci_std_codecs_结构体.md)
- [num_codecs](../bluetooth_hci_model_reference/P440_bt_hci_std_codecs_结构体.md#ad3e63bf445bb6b8e654baa8490cdf547)
- [codec_info](../bluetooth_hci_model_reference/P440_bt_hci_std_codecs_结构体.md#a32767e90384ef74a3e740597eacfcf53)
- [bt_hci_vs_codec_info](../bluetooth_hci_model_reference/P443_bt_hci_vs_codec_info_结构体.md)
- [company_id](../bluetooth_hci_model_reference/P443_bt_hci_vs_codec_info_结构体.md#a8170dac825b76f3dfb5fde5eed04c4c0)
- [codec_id](../bluetooth_hci_model_reference/P443_bt_hci_vs_codec_info_结构体.md#a3c7eea7bae36c7a63457051401526382)
- [bt_hci_vs_codecs](../bluetooth_hci_model_reference/P445_bt_hci_vs_codecs_结构体.md)
- [num_codecs](../bluetooth_hci_model_reference/P445_bt_hci_vs_codecs_结构体.md#a2caf18ce5905e3962da000f3b00b623f)
- [codec_info](../bluetooth_hci_model_reference/P445_bt_hci_vs_codecs_结构体.md#a4e72426599d5bc617fde4f1a4a095527)
- [bt_hci_rp_read_codecs](../bluetooth_hci_model_reference/P406_bt_hci_rp_read_codecs_结构体.md)
- [status](../bluetooth_hci_model_reference/P406_bt_hci_rp_read_codecs_结构体.md#a017182988634c6acbfbfdd7c9609f5dc)
- [codecs](../bluetooth_hci_model_reference/P406_bt_hci_rp_read_codecs_结构体.md#a44e615f375b35cce9f949562555c429b)
- [bt_hci_std_codec_info_v2](../bluetooth_hci_model_reference/P439_bt_hci_std_codec_info_v2_结构体.md)
- [codec_id](../bluetooth_hci_model_reference/P439_bt_hci_std_codec_info_v2_结构体.md#ae82a0896904c7feb2634579b393bf05e)
- [transports](../bluetooth_hci_model_reference/P439_bt_hci_std_codec_info_v2_结构体.md#aea766ba4b911223eeb351e0123e54f5f)
- [bt_hci_std_codecs_v2](../bluetooth_hci_model_reference/P441_bt_hci_std_codecs_v2_结构体.md)
- [num_codecs](../bluetooth_hci_model_reference/P441_bt_hci_std_codecs_v2_结构体.md#ab14fdde478e290235f68aae375969c09)
- [codec_info](../bluetooth_hci_model_reference/P441_bt_hci_std_codecs_v2_结构体.md#aafdb6d96d99063a7a447d80e1830a624)
- [bt_hci_vs_codec_info_v2](../bluetooth_hci_model_reference/P444_bt_hci_vs_codec_info_v2_结构体.md)
- [company_id](../bluetooth_hci_model_reference/P444_bt_hci_vs_codec_info_v2_结构体.md#aa6ce27b4acd3dff516e4d7ed2e6434bc)
- [codec_id](../bluetooth_hci_model_reference/P444_bt_hci_vs_codec_info_v2_结构体.md#ae7b7d5d65629a1e3039b3c7cf167a9c1)
- [transports](../bluetooth_hci_model_reference/P444_bt_hci_vs_codec_info_v2_结构体.md#ac2a91a045e4b53315850b6d4f1d38b2c)
- [bt_hci_vs_codecs_v2](../bluetooth_hci_model_reference/P446_bt_hci_vs_codecs_v2_结构体.md)
- [num_codecs](../bluetooth_hci_model_reference/P446_bt_hci_vs_codecs_v2_结构体.md#ae4cb3a40401594f8e0f18391b9d31a23)
- [codec_info](../bluetooth_hci_model_reference/P446_bt_hci_vs_codecs_v2_结构体.md#a6cd8aa58517d59d565474513f755cfee)
- [bt_hci_rp_read_codecs_v2](../bluetooth_hci_model_reference/P407_bt_hci_rp_read_codecs_v2_结构体.md)
- [status](../bluetooth_hci_model_reference/P407_bt_hci_rp_read_codecs_v2_结构体.md#a2e9866d0f9fb42b54c406a9ea5890913)
- [codecs](../bluetooth_hci_model_reference/P407_bt_hci_rp_read_codecs_v2_结构体.md#a098563f274de085ac97415f1b5e15f3c)
- [bt_hci_cp_codec_id](../bluetooth_hci_model_reference/P011_bt_hci_cp_codec_id_结构体.md)
- [coding_format](../bluetooth_hci_model_reference/P011_bt_hci_cp_codec_id_结构体.md#aec80c74b12edb9c63330cc5a404eed5d)
- [company_id](../bluetooth_hci_model_reference/P011_bt_hci_cp_codec_id_结构体.md#a98fd438270a64d843fa27c7c196645df)
- [vs_codec_id](../bluetooth_hci_model_reference/P011_bt_hci_cp_codec_id_结构体.md#a70296440c202544af11db2dc8e80fc5b)
- [bt_hci_cp_read_codec_capabilities](../bluetooth_hci_model_reference/P150_bt_hci_cp_read_codec_capabilities_结构体.md)
- [codec_id](../bluetooth_hci_model_reference/P150_bt_hci_cp_read_codec_capabilities_结构体.md#ad48b7f228742d86a71dffa314331bbe1)
- [transport](../bluetooth_hci_model_reference/P150_bt_hci_cp_read_codec_capabilities_结构体.md#a6479561573172356d7515ef92f75b8d4)
- [direction](../bluetooth_hci_model_reference/P150_bt_hci_cp_read_codec_capabilities_结构体.md#a237695f4d0a1359d5ce71d831708a69c)
- [bt_hci_codec_capability_info](../bluetooth_hci_model_reference/P006_bt_hci_codec_capability_info_结构体.md)
- [length](../bluetooth_hci_model_reference/P006_bt_hci_codec_capability_info_结构体.md#a24516347742a8fd9f3386d78b66a4e81)
- [data](../bluetooth_hci_model_reference/P006_bt_hci_codec_capability_info_结构体.md#ac53f02f2abdb832ed82da35a36abc323)
- [bt_hci_rp_read_codec_capabilities](../bluetooth_hci_model_reference/P405_bt_hci_rp_read_codec_capabilities_结构体.md)
- [status](../bluetooth_hci_model_reference/P405_bt_hci_rp_read_codec_capabilities_结构体.md#ac224ea998e3af12f97232288266da8d2)
- [num_capabilities](../bluetooth_hci_model_reference/P405_bt_hci_rp_read_codec_capabilities_结构体.md#a71b7df63502bf42a26868e69893ddcfe)
- [capabilities](../bluetooth_hci_model_reference/P405_bt_hci_rp_read_codec_capabilities_结构体.md#ae0c84013512c461f3b6231162d6f3020)
- [bt_hci_cp_read_ctlr_delay](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md)
- [codec_id](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md#a2afb9ca8bc2e24cd479b29bc1a53c867)
- [transport](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md#a60a6a5b87896d0c27d734b56ead58a9b)
- [direction](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md#a5e9f74d4f82809289038da29af0c663d)
- [codec_config_len](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md#ac881526b479d5f1717efbe35cdcc7e87)
- [codec_config](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md#a6c15d141c40bca8bd095f4a86f5a93bd)
- [bt_hci_rp_read_ctlr_delay](../bluetooth_hci_model_reference/P409_bt_hci_rp_read_ctlr_delay_结构体.md)
- [status](../bluetooth_hci_model_reference/P409_bt_hci_rp_read_ctlr_delay_结构体.md#a2f17081cf767643f3a9ad9d115ef5320)
- [min_ctlr_delay](../bluetooth_hci_model_reference/P409_bt_hci_rp_read_ctlr_delay_结构体.md#ab48d1d92cdf9470a93487434b3824d17)
- [max_ctlr_delay](../bluetooth_hci_model_reference/P409_bt_hci_rp_read_ctlr_delay_结构体.md#a4c468053c4a86d1ab462c1e6f17f1013)
- [bt_hci_cp_read_rssi](../bluetooth_hci_model_reference/P159_bt_hci_cp_read_rssi_结构体.md)
- [handle](../bluetooth_hci_model_reference/P159_bt_hci_cp_read_rssi_结构体.md#a0662bc56b344ca2bf9a2dcabe8a13c09)
- [bt_hci_rp_read_rssi](../bluetooth_hci_model_reference/P417_bt_hci_rp_read_rssi_结构体.md)
- [status](../bluetooth_hci_model_reference/P417_bt_hci_rp_read_rssi_结构体.md#a8f91b69a99bd61a7a59d84b3a9c3f235)
- [handle](../bluetooth_hci_model_reference/P417_bt_hci_rp_read_rssi_结构体.md#aa3c4041dd240b1185c7fc8bbef74a17a)
- [rssi](../bluetooth_hci_model_reference/P417_bt_hci_rp_read_rssi_结构体.md#a1071300bd61fcaab65683187ae393cae)
- [bt_hci_cp_read_encryption_key_size](../bluetooth_hci_model_reference/P152_bt_hci_cp_read_encryption_key_size_结构体.md)
- [handle](../bluetooth_hci_model_reference/P152_bt_hci_cp_read_encryption_key_size_结构体.md#af15765007fd0e2fc4186b54323553019)
- [bt_hci_rp_read_encryption_key_size](../bluetooth_hci_model_reference/P411_bt_hci_rp_read_encryption_key_size_结构体.md)
- [status](../bluetooth_hci_model_reference/P411_bt_hci_rp_read_encryption_key_size_结构体.md#a17213ccb9179739aa79c3749a2296f65)
- [handle](../bluetooth_hci_model_reference/P411_bt_hci_rp_read_encryption_key_size_结构体.md#af0b89b2035f956891244b10409be0f51)
- [key_size](../bluetooth_hci_model_reference/P411_bt_hci_rp_read_encryption_key_size_结构体.md#af1cd71c6216b26d460c04a68405f05d5)
- [bt_hci_cp_le_set_event_mask](../bluetooth_hci_model_reference/P096_bt_hci_cp_le_set_event_mask_结构体.md)
- [events](../bluetooth_hci_model_reference/P096_bt_hci_cp_le_set_event_mask_结构体.md#af7de4823aca253f15e57f54ee9b3879e)
- [bt_hci_rp_le_read_buffer_size](../bluetooth_hci_model_reference/P354_bt_hci_rp_le_read_buffer_size_结构体.md)
- [status](../bluetooth_hci_model_reference/P354_bt_hci_rp_le_read_buffer_size_结构体.md#a90a1206f1dbbefd298e5323ac07691f1)
- [le_max_len](../bluetooth_hci_model_reference/P354_bt_hci_rp_le_read_buffer_size_结构体.md#a8bc64cd8743984cd5a8dedfc86aaee56)
- [le_max_num](../bluetooth_hci_model_reference/P354_bt_hci_rp_le_read_buffer_size_结构体.md#a3e393d6c51d8c3f8a5d88413198e3f28)
- [bt_hci_rp_le_read_local_features](../bluetooth_hci_model_reference/P362_bt_hci_rp_le_read_local_features_结构体.md)
- [status](../bluetooth_hci_model_reference/P362_bt_hci_rp_le_read_local_features_结构体.md#ac1000822beba8a7be0dda684c0a86b6b)
- [features](../bluetooth_hci_model_reference/P362_bt_hci_rp_le_read_local_features_结构体.md#ada42e525338cd5526ff211c359c93b3b)
- [bt_hci_cp_le_set_random_address](../bluetooth_hci_model_reference/P120_bt_hci_cp_le_set_random_address_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P120_bt_hci_cp_le_set_random_address_结构体.md#a919ef74473f4f86d00595ec8606789d0)
- [bt_hci_cp_le_set_adv_param](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md)
- [min_interval](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#a2476c2a1858eab7e9b1449c1901363c4)
- [max_interval](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#ab42c6b8f482e782d09386a3a1758903d)
- [type](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#a9b09964156846fd480911dcc2d996a98)
- [own_addr_type](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#ad8c74cac74254354b314f07df7df1bf0)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [direct_addr](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#ac774ef72175e43b083d04ecac263941b)
- [channel_map](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#a2269ae424e47adddce5aa5f2f5b84c89)
- [filter_policy](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#a662c5ae81f25a897a8e597f7227a1e39)
- [bt_hci_rp_le_read_chan_tx_power](../bluetooth_hci_model_reference/P357_bt_hci_rp_le_read_chan_tx_power_结构体.md)
- [status](../bluetooth_hci_model_reference/P357_bt_hci_rp_le_read_chan_tx_power_结构体.md#a09a3805bccdabef399d21b29f84e3a4f)
- [tx_power_level](../bluetooth_hci_model_reference/P357_bt_hci_rp_le_read_chan_tx_power_结构体.md#a3b6b79d1d28c3e4bf565ae364089f365)
- [bt_hci_cp_le_set_adv_data](../bluetooth_hci_model_reference/P082_bt_hci_cp_le_set_adv_data_结构体.md)
- [len](../bluetooth_hci_model_reference/P082_bt_hci_cp_le_set_adv_data_结构体.md#a664313db17c12adb0de14371e46d26a8)
- [data](../bluetooth_hci_model_reference/P082_bt_hci_cp_le_set_adv_data_结构体.md#a6fb8734ff5a9b77586b3e283b83985bb)
- [bt_hci_cp_le_set_scan_rsp_data](../bluetooth_hci_model_reference/P124_bt_hci_cp_le_set_scan_rsp_data_结构体.md)
- [len](../bluetooth_hci_model_reference/P124_bt_hci_cp_le_set_scan_rsp_data_结构体.md#a0fe51008184419c9560bb5d8f287d8be)
- [data](../bluetooth_hci_model_reference/P124_bt_hci_cp_le_set_scan_rsp_data_结构体.md#aa719449dc2b85f094081d66398b72c7d)
- [bt_hci_cp_le_set_adv_enable](../bluetooth_hci_model_reference/P083_bt_hci_cp_le_set_adv_enable_结构体.md)
- [enable](../bluetooth_hci_model_reference/P083_bt_hci_cp_le_set_adv_enable_结构体.md#a15e92d187d586fef560adf9c793f776a)
- [bt_hci_cp_le_set_scan_param](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md)
- [scan_type](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md#ad19a479cc3c27ab24286b537b646261e)
- [interval](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md#adcd8be074a8b19e0e7d02c4ea8209c93)
- [window](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md#a3b5b4767092fc69a63d2219d60722407)
- [addr_type](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md#a694c74a6fc95f767d2e89e6596d51e98)
- [filter_policy](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md#ab7a268e17a5d564d475ff9dee5e6e14b)
- [bt_hci_cp_le_set_scan_enable](../bluetooth_hci_model_reference/P122_bt_hci_cp_le_set_scan_enable_结构体.md)
- [enable](../bluetooth_hci_model_reference/P122_bt_hci_cp_le_set_scan_enable_结构体.md#a5e429a0b11be1493515803a360932b06)
- [filter_dup](../bluetooth_hci_model_reference/P122_bt_hci_cp_le_set_scan_enable_结构体.md#a77b0f05c0e76681ed633bd42b3f21811)
- [bt_hci_cp_le_create_conn](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md)
- [scan_interval](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a1a830a0f6cd961d534c338031b2b691b)
- [scan_window](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#abf61e67f5e20adc44b5b9314ed43bccc)
- [filter_policy](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a2ca5063f5082a0f330676e56253a21c7)
- [peer_addr](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#aa51da7602eb2b44528964c8b706bb043)
- [own_addr_type](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a63c7f9e89528105e484a60e41eeb8a30)
- [conn_interval_min](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a988cf154b0df1ff9af8d34ce73a920dd)
- [conn_interval_max](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#aa009d54866d9c675c2785412bdbd182f)
- [conn_latency](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a5a9d5c1d44adac876680a517b1fad63f)
- [supervision_timeout](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#ae8e0ad70a3b23ac035c237db0d57adc4)
- [min_ce_len](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a476501ccd209f3a52082decf906ca8f0)
- [max_ce_len](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a5b329aa8b48e03998e969b2436d35ab5)
- [bt_hci_rp_le_read_fal_size](../bluetooth_hci_model_reference/P359_bt_hci_rp_le_read_fal_size_结构体.md)
- [status](../bluetooth_hci_model_reference/P359_bt_hci_rp_le_read_fal_size_结构体.md#aaceae885848bbdbf71241e7aa3881db5)
- [fal_size](../bluetooth_hci_model_reference/P359_bt_hci_rp_le_read_fal_size_结构体.md#ac5fcb88478c1faadf7f7ca6a9f838dde)
- [bt_hci_cp_le_add_dev_to_fal](../bluetooth_hci_model_reference/P022_bt_hci_cp_le_add_dev_to_fal_结构体.md)
- [addr](../bluetooth_hci_model_reference/P022_bt_hci_cp_le_add_dev_to_fal_结构体.md#a11ec9f3cd9b80f34094e70d8eeb13be3)
- [bt_hci_cp_le_rem_dev_from_fal](../bluetooth_hci_model_reference/P071_bt_hci_cp_le_rem_dev_from_fal_结构体.md)
- [addr](../bluetooth_hci_model_reference/P071_bt_hci_cp_le_rem_dev_from_fal_结构体.md#afe6054303093cc930d1089ca6a16101c)
- [hci_cp_le_conn_update](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md)
- [handle](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#a5606b8795defc338b27d1a130064351e)
- [conn_interval_min](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#adcfee3c727118069897515a00e7ead66)
- [conn_interval_max](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#a99fc0b3b0f810f1d6e174aa9045d298a)
- [conn_latency](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#a8e48e5e195aea7f581cfc7246da79d72)
- [supervision_timeout](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#ab76ecdf6f7e5a5bb581cbd26f67d8f9f)
- [min_ce_len](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#a3ae86fccacf462463fe520eb1e06fa62)
- [max_ce_len](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#a401169ccc5dbf6cf0abd6154738f00dc)
- [bt_hci_cp_le_set_host_chan_classif](../bluetooth_hci_model_reference/P104_bt_hci_cp_le_set_host_chan_classif_结构体.md)
- [ch_map](../bluetooth_hci_model_reference/P104_bt_hci_cp_le_set_host_chan_classif_结构体.md#a0fb81bcdebe7da416cc4317486106752)
- [bt_hci_cp_le_read_chan_map](../bluetooth_hci_model_reference/P059_bt_hci_cp_le_read_chan_map_结构体.md)
- [handle](../bluetooth_hci_model_reference/P059_bt_hci_cp_le_read_chan_map_结构体.md#abea9aec016a0433b3e4837d53d6b5d2b)
- [bt_hci_rp_le_read_chan_map](../bluetooth_hci_model_reference/P356_bt_hci_rp_le_read_chan_map_结构体.md)
- [status](../bluetooth_hci_model_reference/P356_bt_hci_rp_le_read_chan_map_结构体.md#a73a51f243bf4881f9024ba67cf2426ad)
- [handle](../bluetooth_hci_model_reference/P356_bt_hci_rp_le_read_chan_map_结构体.md#a8fcec46574f5601bf0837aae8f745b38)
- [ch_map](../bluetooth_hci_model_reference/P356_bt_hci_rp_le_read_chan_map_结构体.md#a2899c53f17ba2293b95477ba25fd1b3d)
- [bt_hci_cp_le_read_remote_features](../bluetooth_hci_model_reference/P066_bt_hci_cp_le_read_remote_features_结构体.md)
- [handle](../bluetooth_hci_model_reference/P066_bt_hci_cp_le_read_remote_features_结构体.md#a843997555fd36f102c83a7d59f65eea9)
- [bt_hci_cp_le_encrypt](../bluetooth_hci_model_reference/P039_bt_hci_cp_le_encrypt_结构体.md)
- [key](../bluetooth_hci_model_reference/P039_bt_hci_cp_le_encrypt_结构体.md#ab64f1bab8ad3a98217db96e6765a7d24)
- [plaintext](../bluetooth_hci_model_reference/P039_bt_hci_cp_le_encrypt_结构体.md#ad520b84e6e2a4e62f7fefba248c4cf10)
- [bt_hci_rp_le_encrypt](../bluetooth_hci_model_reference/P342_bt_hci_rp_le_encrypt_结构体.md)
- [status](../bluetooth_hci_model_reference/P342_bt_hci_rp_le_encrypt_结构体.md#aee480917cc6af7dea77717a9cb5840bb)
- [enc_data](../bluetooth_hci_model_reference/P342_bt_hci_rp_le_encrypt_结构体.md#ac20cd9f4ceffea6999114f65437aefdc)
- [bt_hci_rp_le_rand](../bluetooth_hci_model_reference/P351_bt_hci_rp_le_rand_结构体.md)
- [status](../bluetooth_hci_model_reference/P351_bt_hci_rp_le_rand_结构体.md#a73320168836caa3caf724282402e80de)
- [rand](../bluetooth_hci_model_reference/P351_bt_hci_rp_le_rand_结构体.md#a3f706af9d2baf9e2b199242a28cec9e5)
- [bt_hci_cp_le_start_encryption](../bluetooth_hci_model_reference/P127_bt_hci_cp_le_start_encryption_结构体.md)
- [handle](../bluetooth_hci_model_reference/P127_bt_hci_cp_le_start_encryption_结构体.md#a4ac6d63f336e36a347242153aced4c71)
- [rand](../bluetooth_hci_model_reference/P127_bt_hci_cp_le_start_encryption_结构体.md#a896961309d9b3f136beecf70a7e6e8e4)
- [ediv](../bluetooth_hci_model_reference/P127_bt_hci_cp_le_start_encryption_结构体.md#ac1e1fd8b6b97bbd6f27b6e4322b03530)
- [ltk](../bluetooth_hci_model_reference/P127_bt_hci_cp_le_start_encryption_结构体.md#a99d2dd719ce38976e9da8a73f26839a1)
- [bt_hci_cp_le_ltk_req_reply](../bluetooth_hci_model_reference/P051_bt_hci_cp_le_ltk_req_reply_结构体.md)
- [handle](../bluetooth_hci_model_reference/P051_bt_hci_cp_le_ltk_req_reply_结构体.md#a46d87451acc1f1ce2ff35dd0dd238db3)
- [ltk](../bluetooth_hci_model_reference/P051_bt_hci_cp_le_ltk_req_reply_结构体.md#a2d16b44af344237a890341943c4a6582)
- [bt_hci_rp_le_ltk_req_reply](../bluetooth_hci_model_reference/P347_bt_hci_rp_le_ltk_req_reply_结构体.md)
- [status](../bluetooth_hci_model_reference/P347_bt_hci_rp_le_ltk_req_reply_结构体.md#a831950bab8994f36c96c543310400752)
- [handle](../bluetooth_hci_model_reference/P347_bt_hci_rp_le_ltk_req_reply_结构体.md#a2dfe012e641e5d8bd6c0f2e15e5a54c2)
- [bt_hci_cp_le_ltk_req_neg_reply](../bluetooth_hci_model_reference/P050_bt_hci_cp_le_ltk_req_neg_reply_结构体.md)
- [handle](../bluetooth_hci_model_reference/P050_bt_hci_cp_le_ltk_req_neg_reply_结构体.md#add8cc3b13432e233ceb5c2c11e0107c0)
- [bt_hci_rp_le_ltk_req_neg_reply](../bluetooth_hci_model_reference/P346_bt_hci_rp_le_ltk_req_neg_reply_结构体.md)
- [status](../bluetooth_hci_model_reference/P346_bt_hci_rp_le_ltk_req_neg_reply_结构体.md#a92306e47450b239233a3f39c645eaa4e)
- [handle](../bluetooth_hci_model_reference/P346_bt_hci_rp_le_ltk_req_neg_reply_结构体.md#ad0f4f9300d9a8b737b41211972151017)
- [bt_hci_rp_le_read_supp_states](../bluetooth_hci_model_reference/P374_bt_hci_rp_le_read_supp_states_结构体.md)
- [status](../bluetooth_hci_model_reference/P374_bt_hci_rp_le_read_supp_states_结构体.md#aeed0cc41ee521c27f07d8cbf4b377a4f)
- [le_states](../bluetooth_hci_model_reference/P374_bt_hci_rp_le_read_supp_states_结构体.md#a9b60476cc158a701b29b28bd21375130)
- [bt_hci_cp_le_rx_test](../bluetooth_hci_model_reference/P078_bt_hci_cp_le_rx_test_结构体.md)
- [rx_ch](../bluetooth_hci_model_reference/P078_bt_hci_cp_le_rx_test_结构体.md#a11cb21a7625d9c097eba0a7b68e93f3f)
- [bt_hci_cp_le_tx_test](../bluetooth_hci_model_reference/P130_bt_hci_cp_le_tx_test_结构体.md)
- [tx_ch](../bluetooth_hci_model_reference/P130_bt_hci_cp_le_tx_test_结构体.md#aae634b277125066ecbc36d119bc4244f)
- [test_data_len](../bluetooth_hci_model_reference/P130_bt_hci_cp_le_tx_test_结构体.md#a55c5f1621a51da03500910fc9664df54)
- [pkt_payload](../bluetooth_hci_model_reference/P130_bt_hci_cp_le_tx_test_结构体.md#ad93908905d370842f16e16cc45280495)
- [bt_hci_rp_le_test_end](../bluetooth_hci_model_reference/P392_bt_hci_rp_le_test_end_结构体.md)
- [status](../bluetooth_hci_model_reference/P392_bt_hci_rp_le_test_end_结构体.md#a2ac412ef9a5fc7651315afe042856cce)
- [rx_pkt_count](../bluetooth_hci_model_reference/P392_bt_hci_rp_le_test_end_结构体.md#a9e283118e4ea48b0df66a4cd1c1cf9a1)
- [bt_hci_cp_le_conn_param_req_reply](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md)
- [handle](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#aa3b938afe13d4e05806fb6cdfab5cb14)
- [interval_min](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#a10547c7d4836980947d17bbde0d75a51)
- [interval_max](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#aed58f9aa722a284ae39df842394c06cf)
- [latency](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#a8c76816cc230387c249ab8e05c402964)
- [timeout](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#af25a3f226ceccbe19e7f1482ed5f141e)
- [min_ce_len](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#a512d605d5c4aacf81b78794fcf260abf)
- [max_ce_len](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#a932e6a3a45ec0409656325f7246d5d7e)
- [bt_hci_rp_le_conn_param_req_reply](../bluetooth_hci_model_reference/P340_bt_hci_rp_le_conn_param_req_reply_结构体.md)
- [status](../bluetooth_hci_model_reference/P340_bt_hci_rp_le_conn_param_req_reply_结构体.md#a2f0a9f5b087d1f12c100ef4521e015ff)
- [handle](../bluetooth_hci_model_reference/P340_bt_hci_rp_le_conn_param_req_reply_结构体.md#a3e598cd87d5298a1cc62ac79a4f34a6e)
- [bt_hci_cp_le_conn_param_req_neg_reply](../bluetooth_hci_model_reference/P029_bt_hci_cp_le_conn_param_req_neg_reply_结构体.md)
- [handle](../bluetooth_hci_model_reference/P029_bt_hci_cp_le_conn_param_req_neg_reply_结构体.md#a0040e4a50c5c5479b539eb0bafb7b305)
- [reason](../bluetooth_hci_model_reference/P029_bt_hci_cp_le_conn_param_req_neg_reply_结构体.md#a8c283ac844805224b1ffeb9801e8b14b)
- [bt_hci_rp_le_conn_param_req_neg_reply](../bluetooth_hci_model_reference/P339_bt_hci_rp_le_conn_param_req_neg_reply_结构体.md)
- [status](../bluetooth_hci_model_reference/P339_bt_hci_rp_le_conn_param_req_neg_reply_结构体.md#a3804e64f9e8693e3e5899067212f6873)
- [handle](../bluetooth_hci_model_reference/P339_bt_hci_rp_le_conn_param_req_neg_reply_结构体.md#ac88f44127c0a1b9b191a27cc003c1052)
- [bt_hci_cp_le_set_data_len](../bluetooth_hci_model_reference/P093_bt_hci_cp_le_set_data_len_结构体.md)
- [handle](../bluetooth_hci_model_reference/P093_bt_hci_cp_le_set_data_len_结构体.md#a874869090428a7f380c5466353573eba)
- [tx_octets](../bluetooth_hci_model_reference/P093_bt_hci_cp_le_set_data_len_结构体.md#ac579e84a004a09813bbe0ed61db11931)
- [tx_time](../bluetooth_hci_model_reference/P093_bt_hci_cp_le_set_data_len_结构体.md#a15285a4e8bf8e359bb326de4b30ba8f1)
- [bt_hci_rp_le_set_data_len](../bluetooth_hci_model_reference/P386_bt_hci_rp_le_set_data_len_结构体.md)
- [status](../bluetooth_hci_model_reference/P386_bt_hci_rp_le_set_data_len_结构体.md#a8667db355a95691d58845f89e919aea4)
- [handle](../bluetooth_hci_model_reference/P386_bt_hci_rp_le_set_data_len_结构体.md#a207c6da11e0bb145bed7a9e551ddc608)
- [bt_hci_rp_le_read_default_data_len](../bluetooth_hci_model_reference/P358_bt_hci_rp_le_read_default_data_len_结构体.md)
- [status](../bluetooth_hci_model_reference/P358_bt_hci_rp_le_read_default_data_len_结构体.md#a62d735826ad3ca5d4bea7d0fb87dea7e)
- [max_tx_octets](../bluetooth_hci_model_reference/P358_bt_hci_rp_le_read_default_data_len_结构体.md#a1ec4ba1c0286132e87fcffeb988a37f9)
- [max_tx_time](../bluetooth_hci_model_reference/P358_bt_hci_rp_le_read_default_data_len_结构体.md#ae193eab40c2afa55b78a1906e6a26f26)
- [bt_hci_cp_le_write_default_data_len](../bluetooth_hci_model_reference/P137_bt_hci_cp_le_write_default_data_len_结构体.md)
- [max_tx_octets](../bluetooth_hci_model_reference/P137_bt_hci_cp_le_write_default_data_len_结构体.md#a0ffb8c52d9031dfe448eac0943a4a49c)
- [max_tx_time](../bluetooth_hci_model_reference/P137_bt_hci_cp_le_write_default_data_len_结构体.md#a2ada0ea5ee8ac8e6d59fc6adc18421b8)
- [bt_hci_cp_le_generate_dhkey](../bluetooth_hci_model_reference/P045_bt_hci_cp_le_generate_dhkey_结构体.md)
- [key](../bluetooth_hci_model_reference/P045_bt_hci_cp_le_generate_dhkey_结构体.md#a0f67195504d877a1d11b7dfb77d09fcc)
- [bt_hci_cp_le_generate_dhkey_v2](../bluetooth_hci_model_reference/P046_bt_hci_cp_le_generate_dhkey_v2_结构体.md)
- [key](../bluetooth_hci_model_reference/P046_bt_hci_cp_le_generate_dhkey_v2_结构体.md#acc3007adf301674b9e847297007c3cd1)
- [key_type](../bluetooth_hci_model_reference/P046_bt_hci_cp_le_generate_dhkey_v2_结构体.md#a3d47ad6d9df4d4023d2586c915ee8f2c)
- [bt_hci_cp_le_add_dev_to_rl](../bluetooth_hci_model_reference/P024_bt_hci_cp_le_add_dev_to_rl_结构体.md)
- [peer_id_addr](../bluetooth_hci_model_reference/P024_bt_hci_cp_le_add_dev_to_rl_结构体.md#a3daf2041f04381a56c2cbcd4bb33f4c0)
- [peer_irk](../bluetooth_hci_model_reference/P024_bt_hci_cp_le_add_dev_to_rl_结构体.md#aedc27c868a7a4cbd3c175f67db4e3242)
- [local_irk](../bluetooth_hci_model_reference/P024_bt_hci_cp_le_add_dev_to_rl_结构体.md#ab5caa38e6eeab09b4a69084b1890317b)
- [bt_hci_cp_le_rem_dev_from_rl](../bluetooth_hci_model_reference/P073_bt_hci_cp_le_rem_dev_from_rl_结构体.md)
- [peer_id_addr](../bluetooth_hci_model_reference/P073_bt_hci_cp_le_rem_dev_from_rl_结构体.md#aacb577a7ae13322145fccdffc3161541)
- [bt_hci_rp_le_read_rl_size](../bluetooth_hci_model_reference/P373_bt_hci_rp_le_read_rl_size_结构体.md)
- [status](../bluetooth_hci_model_reference/P373_bt_hci_rp_le_read_rl_size_结构体.md#af8a10aab21d54cce3529b1307769f6c6)
- [rl_size](../bluetooth_hci_model_reference/P373_bt_hci_rp_le_read_rl_size_结构体.md#a90c28070ee094c99c21c4dd229ff6ce5)
- [bt_hci_cp_le_read_peer_rpa](../bluetooth_hci_model_reference/P063_bt_hci_cp_le_read_peer_rpa_结构体.md)
- [peer_id_addr](../bluetooth_hci_model_reference/P063_bt_hci_cp_le_read_peer_rpa_结构体.md#ab0c70a1dbe5152b1fc926b90ec3387b3)
- [bt_hci_rp_le_read_peer_rpa](../bluetooth_hci_model_reference/P369_bt_hci_rp_le_read_peer_rpa_结构体.md)
- [status](../bluetooth_hci_model_reference/P369_bt_hci_rp_le_read_peer_rpa_结构体.md#a9c8c799e8c9fbb9f64865e55cdb1f9ef)
- [peer_rpa](../bluetooth_hci_model_reference/P369_bt_hci_rp_le_read_peer_rpa_结构体.md#a4eeee179819865ba5d5171d9bd33e5e9)
- [bt_hci_cp_le_read_local_rpa](../bluetooth_hci_model_reference/P062_bt_hci_cp_le_read_local_rpa_结构体.md)
- [peer_id_addr](../bluetooth_hci_model_reference/P062_bt_hci_cp_le_read_local_rpa_结构体.md#aa96cd60066003e4a7a1f482fb81557f8)
- [bt_hci_rp_le_read_local_rpa](../bluetooth_hci_model_reference/P363_bt_hci_rp_le_read_local_rpa_结构体.md)
- [status](../bluetooth_hci_model_reference/P363_bt_hci_rp_le_read_local_rpa_结构体.md#a55b1ac66c986c0a7879b144163064be2)
- [local_rpa](../bluetooth_hci_model_reference/P363_bt_hci_rp_le_read_local_rpa_结构体.md#a5b27c5b02cb290452be62c22772fbc53)
- [bt_hci_cp_le_set_addr_res_enable](../bluetooth_hci_model_reference/P081_bt_hci_cp_le_set_addr_res_enable_结构体.md)
- [enable](../bluetooth_hci_model_reference/P081_bt_hci_cp_le_set_addr_res_enable_结构体.md#ad0548178cbc9bc2db54612a748a2bd65)
- [bt_hci_cp_le_set_rpa_timeout](../bluetooth_hci_model_reference/P121_bt_hci_cp_le_set_rpa_timeout_结构体.md)
- [rpa_timeout](../bluetooth_hci_model_reference/P121_bt_hci_cp_le_set_rpa_timeout_结构体.md#a6b1befe9d2131a889de17339ec1941fa)
- [bt_hci_rp_le_read_max_data_len](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md)
- [status](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md#a654b34b1ee038bf442550a340a26070c)
- [max_tx_octets](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md#a2c0b159c6248cb9df458d587f82a4152)
- [max_tx_time](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md#a6adc84bf3cc86f234e61982d871899b6)
- [max_rx_octets](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md#a9273dac6614f1e120f0539b746bfd6cc)
- [max_rx_time](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md#a963ef9c097906c8db46c35459eb4ecab)
- [bt_hci_cp_le_read_phy](../bluetooth_hci_model_reference/P064_bt_hci_cp_le_read_phy_结构体.md)
- [handle](../bluetooth_hci_model_reference/P064_bt_hci_cp_le_read_phy_结构体.md#a7e0a4fa47b613c86364e6e94c2d0bef1)
- [bt_hci_rp_le_read_phy](../bluetooth_hci_model_reference/P371_bt_hci_rp_le_read_phy_结构体.md)
- [status](../bluetooth_hci_model_reference/P371_bt_hci_rp_le_read_phy_结构体.md#a65d412e37eb2cd839fae262f4f9d5b28)
- [handle](../bluetooth_hci_model_reference/P371_bt_hci_rp_le_read_phy_结构体.md#ae708b4f8ad2632d73bedea640f138d9f)
- [tx_phy](../bluetooth_hci_model_reference/P371_bt_hci_rp_le_read_phy_结构体.md#a644c0065d97e5de006dc28f7bca62268)
- [rx_phy](../bluetooth_hci_model_reference/P371_bt_hci_rp_le_read_phy_结构体.md#a5a060e0c0d1e5f33222ab10a5d3977e8)
- [bt_hci_cp_le_set_default_phy](../bluetooth_hci_model_reference/P094_bt_hci_cp_le_set_default_phy_结构体.md)
- [all_phys](../bluetooth_hci_model_reference/P094_bt_hci_cp_le_set_default_phy_结构体.md#abe1d83e372e874739588812040d0b540)
- [tx_phys](../bluetooth_hci_model_reference/P094_bt_hci_cp_le_set_default_phy_结构体.md#a0c4ab2d91021466fd136af3a0b6bde2a)
- [rx_phys](../bluetooth_hci_model_reference/P094_bt_hci_cp_le_set_default_phy_结构体.md#a4c3410f2ce9fb2817bc5d143908936d1)
- [bt_hci_cp_le_set_phy](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md)
- [handle](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md#ad0759eea02017674459d4ce0af0e526e)
- [all_phys](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md#afb8d056dc7d8824eec0ef16fdf9ce924)
- [tx_phys](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md#a06880062ff486b532ebeb789adb57d1e)
- [rx_phys](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md#ab30eb68920a0578b16794250e592b12a)
- [phy_opts](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md#a458ab90f83b60fafa66167f474c0800d)
- [bt_hci_cp_le_enh_rx_test](../bluetooth_hci_model_reference/P040_bt_hci_cp_le_enh_rx_test_结构体.md)
- [rx_ch](../bluetooth_hci_model_reference/P040_bt_hci_cp_le_enh_rx_test_结构体.md#a3aa5b3947a4a0c87342695469bf056ec)
- [phy](../bluetooth_hci_model_reference/P040_bt_hci_cp_le_enh_rx_test_结构体.md#aa2bf385221680b25ce184b4ea5d63cd4)
- [mod_index](../bluetooth_hci_model_reference/P040_bt_hci_cp_le_enh_rx_test_结构体.md#a9151393e9f05a2ded484a1248a6edb88)
- [bt_hci_cp_le_enh_tx_test](../bluetooth_hci_model_reference/P041_bt_hci_cp_le_enh_tx_test_结构体.md)
- [tx_ch](../bluetooth_hci_model_reference/P041_bt_hci_cp_le_enh_tx_test_结构体.md#a0b7883b36d511c6da1bac543f1aae446)
- [test_data_len](../bluetooth_hci_model_reference/P041_bt_hci_cp_le_enh_tx_test_结构体.md#af1e27be0ad23887c0e71024739b00f8d)
- [pkt_payload](../bluetooth_hci_model_reference/P041_bt_hci_cp_le_enh_tx_test_结构体.md#a9ccb91be1554172d6c724e438508bfe5)
- [phy](../bluetooth_hci_model_reference/P041_bt_hci_cp_le_enh_tx_test_结构体.md#a718442db29c5ac455c3e2aac9844cdd0)
- [bt_hci_cp_le_set_adv_set_random_addr](../bluetooth_hci_model_reference/P085_bt_hci_cp_le_set_adv_set_random_addr_结构体.md)
- [handle](../bluetooth_hci_model_reference/P085_bt_hci_cp_le_set_adv_set_random_addr_结构体.md#aafa39422a16cc4ff11c8073e9c0aab71)
- [bdaddr](../bluetooth_hci_model_reference/P085_bt_hci_cp_le_set_adv_set_random_addr_结构体.md#a2883e9bf7ef6a34712eda2594e23c146)
- [bt_hci_cp_le_set_ext_adv_param](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md)
- [handle](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a65fe609dde9515212659087a024e7c65)
- [props](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a4af102ae90ca6917b3134491c5ff079f)
- [prim_min_interval](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#ab5a80941b3d832c2906daed8cf069a02)
- [prim_max_interval](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a08aa741a56e825a11424bf024ac65e14)
- [prim_channel_map](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#ad7a0b9028bcdb57a9011d4677412aed5)
- [own_addr_type](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a3594f7337ccd739f59ac7845757de0e8)
- [peer_addr](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a819e599df4025036fab2dabd7c61ea37)
- [filter_policy](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a29a62f8989f89b014cadbad9b94e996a)
- [tx_power](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a5f7f3e477b5b0b8122b85f3e53dd7878)
- [prim_adv_phy](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a048874197ccbdbc626f0563be5c41ec7)
- [sec_adv_max_skip](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a5793c6afe545290a1e792bcc73585b72)
- [sec_adv_phy](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#abc82ba984647eb00bc490c01ce746a15)
- [sid](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#af8bc3509fdd5e89c27db466727fe1cd9)
- [scan_req_notify_enable](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#ae694df46b1db4b029d1e177768b3821f)
- [bt_hci_rp_le_set_ext_adv_param](../bluetooth_hci_model_reference/P387_bt_hci_rp_le_set_ext_adv_param_结构体.md)
- [status](../bluetooth_hci_model_reference/P387_bt_hci_rp_le_set_ext_adv_param_结构体.md#a6baae317455ffbb489066fcd1fb068c8)
- [tx_power](../bluetooth_hci_model_reference/P387_bt_hci_rp_le_set_ext_adv_param_结构体.md#a8a876d0e3d4d9d066a27c054569f0b9a)
- [bt_hci_cp_le_set_ext_adv_param_v2](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md)
- [handle](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#ad9e43219b471e44884b33ea5ddd90513)
- [props](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#aff572d12a03ca9cbc2ee80f75e1f77c7)
- [prim_min_interval](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a25fec4dc9203bb50bb030087b42f473e)
- [prim_max_interval](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a6098216ae6ef0f9459aae16adecd193f)
- [prim_channel_map](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a1a96a88729e311c6a60571997aae9fc3)
- [own_addr_type](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a554f89f00700bc3ea4996b0a971fedbf)
- [peer_addr](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#ad8fccd11fbea598de62e057a69b72156)
- [filter_policy](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a047656dd56bf883f1e307dcabe96f1de)
- [tx_power](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a5283a6a40d46e0fe787ed403acab9f90)
- [prim_adv_phy](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a92a215151c603c2f8dd1b7e730a8e979)
- [sec_adv_max_skip](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#ac31b52df1033d11585781fbecc10f578)
- [sec_adv_phy](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a6c2a953fab938f304e815bd9d59d05ae)
- [sid](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#aeb26f7f16e2c71542421aada577a993f)
- [scan_req_notify_enable](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a9f2a6f38e8965dabe17ad743d3aeda70)
- [prim_adv_phy_opt](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a8767fb7f5492f0323edd9afb687318db)
- [sec_adv_phy_opt](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a0c7994ef034270a7fd814386e7b76cc8)
- [bt_hci_cp_le_set_ext_adv_data](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md)
- [handle](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md#a803bb793eefcc714c6c4034123a2e487)
- [op](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md#ac5eaa1834f82024055923d08a3bef6b3)
- [frag_pref](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md#af9eef9f59bfec5867ea36bdf33e3a9b1)
- [len](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md#aea3055cc7ffbaf4cd14996d885e21ba3)
- [data](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md#a7d7df52500eb53a64b6ba5e62f6cf14f)
- [bt_hci_cp_le_set_ext_scan_rsp_data](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md)
- [handle](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md#a8cf0624b9968686c7f6765ee25e11c90)
- [op](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md#a3323a0844680b71cb8aedffa034837d7)
- [frag_pref](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md#ac4e1691926df370b290c9e6d866d310d)
- [len](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md#a6024eac85f600ed3b7051a84b91bdcfa)
- [data](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md#ab086720e1a22523ba155cb238ad75197)
- [bt_hci_ext_adv_set](../bluetooth_hci_model_reference/P307_bt_hci_ext_adv_set_结构体.md)
- [handle](../bluetooth_hci_model_reference/P307_bt_hci_ext_adv_set_结构体.md#a9d0fd3f6659db172ff4efd74c2c2d216)
- [duration](../bluetooth_hci_model_reference/P307_bt_hci_ext_adv_set_结构体.md#acc2afc91fe5c0dfcb4c95eaade4a047a)
- [max_ext_adv_evts](../bluetooth_hci_model_reference/P307_bt_hci_ext_adv_set_结构体.md#a4467ac9a564ea24bb701de46cda2579a)
- [bt_hci_cp_le_set_ext_adv_enable](../bluetooth_hci_model_reference/P098_bt_hci_cp_le_set_ext_adv_enable_结构体.md)
- [enable](../bluetooth_hci_model_reference/P098_bt_hci_cp_le_set_ext_adv_enable_结构体.md#ab7148b47bf052d8cba1f6bf3385051c8)
- [set_num](../bluetooth_hci_model_reference/P098_bt_hci_cp_le_set_ext_adv_enable_结构体.md#a06088af8b432ac134943d9ebb7778ac7)
- [s](../bluetooth_hci_model_reference/P098_bt_hci_cp_le_set_ext_adv_enable_结构体.md#a04911e19f3b2f0079d4e12980d11157f)
- [bt_hci_rp_le_read_max_adv_data_len](../bluetooth_hci_model_reference/P366_bt_hci_rp_le_read_max_adv_data_len_结构体.md)
- [status](../bluetooth_hci_model_reference/P366_bt_hci_rp_le_read_max_adv_data_len_结构体.md#a978911dc5028d1f36820447de8e9e5f7)
- [max_adv_data_len](../bluetooth_hci_model_reference/P366_bt_hci_rp_le_read_max_adv_data_len_结构体.md#aa4084a89de4929c3e8e2630d0aad7f82)
- [bt_hci_rp_le_read_num_adv_sets](../bluetooth_hci_model_reference/P368_bt_hci_rp_le_read_num_adv_sets_结构体.md)
- [status](../bluetooth_hci_model_reference/P368_bt_hci_rp_le_read_num_adv_sets_结构体.md#a590934059fb851a14b2eec66f32a5334)
- [num_sets](../bluetooth_hci_model_reference/P368_bt_hci_rp_le_read_num_adv_sets_结构体.md#a7dd26bda7a8ab75fed2af19bb5af34fc)
- [bt_hci_cp_le_remove_adv_set](../bluetooth_hci_model_reference/P074_bt_hci_cp_le_remove_adv_set_结构体.md)
- [handle](../bluetooth_hci_model_reference/P074_bt_hci_cp_le_remove_adv_set_结构体.md#ab33bf918b10d847bb8fb8ac2409780e6)
- [bt_hci_cp_le_set_per_adv_param](../bluetooth_hci_model_reference/P114_bt_hci_cp_le_set_per_adv_param_结构体.md)
- [handle](../bluetooth_hci_model_reference/P114_bt_hci_cp_le_set_per_adv_param_结构体.md#a2b61031952b3893add7677d3802e368b)
- [min_interval](../bluetooth_hci_model_reference/P114_bt_hci_cp_le_set_per_adv_param_结构体.md#af01696ef6bf02e7db37d45a0c9852ef5)
- [max_interval](../bluetooth_hci_model_reference/P114_bt_hci_cp_le_set_per_adv_param_结构体.md#a1a2a69ea6e310710892184ced472eb8a)
- [props](../bluetooth_hci_model_reference/P114_bt_hci_cp_le_set_per_adv_param_结构体.md#a879ea10e1ab217b4aa49dfcf3b394691)
- [bt_hci_cp_le_set_per_adv_data](../bluetooth_hci_model_reference/P112_bt_hci_cp_le_set_per_adv_data_结构体.md)
- [handle](../bluetooth_hci_model_reference/P112_bt_hci_cp_le_set_per_adv_data_结构体.md#a93cbb46ce6664880487e009a0b47af02)
- [op](../bluetooth_hci_model_reference/P112_bt_hci_cp_le_set_per_adv_data_结构体.md#aac34596f0970c976c4ef71250d326c2c)
- [len](../bluetooth_hci_model_reference/P112_bt_hci_cp_le_set_per_adv_data_结构体.md#ae6ee631a153cb6fed88695e599f63e91)
- [data](../bluetooth_hci_model_reference/P112_bt_hci_cp_le_set_per_adv_data_结构体.md#adaf581f8db6aafb4dc5df669df7ad26d)
- [bt_hci_cp_le_set_per_adv_enable](../bluetooth_hci_model_reference/P113_bt_hci_cp_le_set_per_adv_enable_结构体.md)
- [enable](../bluetooth_hci_model_reference/P113_bt_hci_cp_le_set_per_adv_enable_结构体.md#afff649b908264c617b249bcfbebadd53)
- [handle](../bluetooth_hci_model_reference/P113_bt_hci_cp_le_set_per_adv_enable_结构体.md#a998f4e38a56f771f234ce099b4528a3d)
- [bt_hci_ext_scan_phy](../bluetooth_hci_model_reference/P309_bt_hci_ext_scan_phy_结构体.md)
- [type](../bluetooth_hci_model_reference/P309_bt_hci_ext_scan_phy_结构体.md#a4cfebc7b2709973953bed9a09a793b7e)
- [interval](../bluetooth_hci_model_reference/P309_bt_hci_ext_scan_phy_结构体.md#a2f087d18bde86d0ac81a14a09ae5b9b0)
- [window](../bluetooth_hci_model_reference/P309_bt_hci_ext_scan_phy_结构体.md#a9c0196f0d5f0064796c15a5df2ad4c07)
- [bt_hci_cp_le_set_ext_scan_param](../bluetooth_hci_model_reference/P102_bt_hci_cp_le_set_ext_scan_param_结构体.md)
- [own_addr_type](../bluetooth_hci_model_reference/P102_bt_hci_cp_le_set_ext_scan_param_结构体.md#a3418aa8dbdb8062ee452f5756eb9f30c)
- [filter_policy](../bluetooth_hci_model_reference/P102_bt_hci_cp_le_set_ext_scan_param_结构体.md#a47f6cf7f83451dcc2feac1a8d5837ad8)
- [phys](../bluetooth_hci_model_reference/P102_bt_hci_cp_le_set_ext_scan_param_结构体.md#a6c38b7d074eb3c0cf5c301eb6c03b60c)
- [p](../bluetooth_hci_model_reference/P102_bt_hci_cp_le_set_ext_scan_param_结构体.md#ab4eab9a52dca01bc19b35607d6ec5d36)
- [bt_hci_cp_le_set_ext_scan_enable](../bluetooth_hci_model_reference/P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md)
- [enable](../bluetooth_hci_model_reference/P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md#a922d0c5a7ccb6c1e1864f662227b8307)
- [filter_dup](../bluetooth_hci_model_reference/P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md#aa5b0939838ab13eb8299f4a4b2fd3f14)
- [duration](../bluetooth_hci_model_reference/P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md#adcd5e00a240f3e7395d0d25994b4013a)
- [period](../bluetooth_hci_model_reference/P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md#aa60c8ade7047dcd202d83cfc3f18ada2)
- [bt_hci_ext_conn_phy](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md)
- [scan_interval](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#a4f78503fe42ee81fea740ba1643a732e)
- [scan_window](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#ae0e950c8004bd595631f95a289a5c871)
- [conn_interval_min](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#a7fc06c1a458aedb6b29381450a5a4df0)
- [conn_interval_max](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#a7bcf66a3372d92c809d8427796915b88)
- [conn_latency](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#a7dd57b7ef0b13b15da47e92076f87d79)
- [supervision_timeout](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#aaec54c0743dfc08923b5ccd8fc1a4015)
- [min_ce_len](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#af48212961ce21f5222e57f70ffeb811b)
- [max_ce_len](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#a3c3ccb93014758b3215718d2672ce7f3)
- [bt_hci_cp_le_ext_create_conn](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md)
- [filter_policy](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md#a0561b446effa3f735a405c0b307466bf)
- [own_addr_type](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md#a12a99044f54e3d5dae30a64392444cbf)
- [peer_addr](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md#a79bc55d9f5b1d719de4fb404db9008f3)
- [phys](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md#ae859ff0da5e9cdc872943fd74774ef7e)
- [p](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md#acdb436d6bf2864745ec579622ae0d532)
- [bt_hci_cp_le_ext_create_conn_v2](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md)
- [adv_handle](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#addf1f80c4d3625e0c6d6e716f6e2e207)
- [subevent](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#a536da199958b3b54469f5b4b029e1bac)
- [filter_policy](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#a66632dbac1605cff69e8da566e800347)
- [own_addr_type](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#a05fd0089a0fd43f98042835231407a60)
- [peer_addr](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#a25466a04d224bdf495266b0064c424dd)
- [phys](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#ae2d3e3079a2848907224bb7ff0efc64b)
- [p](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#a8d606c5aa480f54c8da9f42a35ad513e)
- [bt_hci_cp_le_set_pawr_subevent_data_element](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md)
- [subevent](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md#abf33f93f0f1ddf3532c6cae13483ec1e)
- [response_slot_start](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md#a90178bcd86c1bad0a768f391ce11613f)
- [response_slot_count](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md#ad8da1cc672eedf8be8cfc7d0d7ec1b41)
- [subevent_data_length](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md#ace5860dfa0f628eaed2b68b171d875da)
- [subevent_data](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md#a91c975189e409b733ac9a4af5763b12a)
- [bt_hci_cp_le_set_pawr_subevent_data](../bluetooth_hci_model_reference/P109_bt_hci_cp_le_set_pawr_subevent_data_结构体.md)
- [adv_handle](../bluetooth_hci_model_reference/P109_bt_hci_cp_le_set_pawr_subevent_data_结构体.md#a47d84125d15cce1fc969db3e5caa07e1)
- [num_subevents](../bluetooth_hci_model_reference/P109_bt_hci_cp_le_set_pawr_subevent_data_结构体.md#a9397eebd6771ad159d1bdae0d59e5f46)
- [subevents](../bluetooth_hci_model_reference/P109_bt_hci_cp_le_set_pawr_subevent_data_结构体.md#aa932c1f19de96f89a79bbcb3ecbc1f5d)
- [bt_hci_cp_le_set_pawr_response_data](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md)
- [sync_handle](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#a034afaaacf4b2168b9cd54cfde583b5c)
- [request_event](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#aaf5c337af93f13e243451b46a94ffb77)
- [request_subevent](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#a675a223891b28f06e78df6223439dc28)
- [response_subevent](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#aaf2e0eb3b491b5ccd15ba5259fd900c7)
- [response_slot](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#a4356344510833196533bb9582f6fe18a)
- [response_data_length](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#a8c546fa3c6d969d44c54926330e5cf85)
- [response_data](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#a39cbc74ab95881b6dde8fa377d2951e5)
- [bt_hci_cp_le_set_pawr_sync_subevent](../bluetooth_hci_model_reference/P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md)
- [sync_handle](../bluetooth_hci_model_reference/P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md#a89f3092c2dd561e5469bb5bf57a06172)
- [periodic_adv_properties](../bluetooth_hci_model_reference/P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md#aa73b23816e6c2c6546de15f6f6caff27)
- [num_subevents](../bluetooth_hci_model_reference/P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md#a2648ff50e0bad585e77e6f340836555a)
- [subevents](../bluetooth_hci_model_reference/P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md#a9a362ae841e5305b3985c4b2d88c6753)
- [bt_hci_cp_le_set_per_adv_param_v2](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md)
- [handle](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#aee1088b46914c8e26d9e97ce573291c6)
- [min_interval](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#ae36e28210a515f73648e6f8b3984fb55)
- [max_interval](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#acc9718286ab0847a3444d3fc2d3c93bc)
- [props](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#ad2d658bb0be35aee6b5c133fece89068)
- [num_subevents](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#a7bea764aa5d21e03946804566b1f9869)
- [subevent_interval](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#a79dfc3b13068d9c51f0a756f025aaeba)
- [response_slot_delay](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#acdeb503c0a13291158ad389c9f6ac206)
- [response_slot_spacing](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#a35fcc697e60d3c398f03be7503f611bd)
- [num_response_slots](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#a2483eb4457f9dc22ff8473175662e260)
- [bt_hci_cp_le_per_adv_create_sync](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md)
- [options](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#aff300f352ec5f0fece90f88db811ef75)
- [sid](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#ab5c4debe1babb98c60c1f1bfdf55359a)
- [addr](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#a3a0a0bc1bd5014f2ede0c4ef6cc30d24)
- [skip](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#a554552684fa2a8d0022f9e31ade9c222)
- [sync_timeout](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#a46ea01403f68d42a315ff629374b2a95)
- [cte_type](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#a905b2a9166dd668df5929f0866769576)
- [bt_hci_cp_le_per_adv_terminate_sync](../bluetooth_hci_model_reference/P056_bt_hci_cp_le_per_adv_terminate_sync_结构体.md)
- [handle](../bluetooth_hci_model_reference/P056_bt_hci_cp_le_per_adv_terminate_sync_结构体.md#a607fce7fd5c88e12f82e3d9731bd7f1a)
- [bt_hci_cp_le_add_dev_to_per_adv_list](../bluetooth_hci_model_reference/P023_bt_hci_cp_le_add_dev_to_per_adv_list_结构体.md)
- [addr](../bluetooth_hci_model_reference/P023_bt_hci_cp_le_add_dev_to_per_adv_list_结构体.md#ad93d72bfa7e4123ee9728f6bf73b69df)
- [sid](../bluetooth_hci_model_reference/P023_bt_hci_cp_le_add_dev_to_per_adv_list_结构体.md#a97d9c5dd0cc4b3ab7f6ebfec206b7407)
- [bt_hci_cp_le_rem_dev_from_per_adv_list](../bluetooth_hci_model_reference/P072_bt_hci_cp_le_rem_dev_from_per_adv_list_结构体.md)
- [addr](../bluetooth_hci_model_reference/P072_bt_hci_cp_le_rem_dev_from_per_adv_list_结构体.md#adc420288f6a79c1a92f57241d3da3d81)
- [sid](../bluetooth_hci_model_reference/P072_bt_hci_cp_le_rem_dev_from_per_adv_list_结构体.md#a6629f3ececf586792a14f3c028cc8e8c)
- [bt_hci_rp_le_read_per_adv_list_size](../bluetooth_hci_model_reference/P370_bt_hci_rp_le_read_per_adv_list_size_结构体.md)
- [status](../bluetooth_hci_model_reference/P370_bt_hci_rp_le_read_per_adv_list_size_结构体.md#a70aa5b466bdbbd309fc59570625c35e5)
- [list_size](../bluetooth_hci_model_reference/P370_bt_hci_rp_le_read_per_adv_list_size_结构体.md#ab6c4ed1037327669aef623f3a1e9d601)
- [bt_hci_rp_le_read_tx_power](../bluetooth_hci_model_reference/P376_bt_hci_rp_le_read_tx_power_结构体.md)
- [status](../bluetooth_hci_model_reference/P376_bt_hci_rp_le_read_tx_power_结构体.md#a805629b92c65e006082d819f578ed555)
- [min_tx_power](../bluetooth_hci_model_reference/P376_bt_hci_rp_le_read_tx_power_结构体.md#a6d4ab95efda5cfc97ae11d83787da8d7)
- [max_tx_power](../bluetooth_hci_model_reference/P376_bt_hci_rp_le_read_tx_power_结构体.md#a1d794f1f7ea77eceac7dae2546eab047)
- [bt_hci_rp_le_read_rf_path_comp](../bluetooth_hci_model_reference/P372_bt_hci_rp_le_read_rf_path_comp_结构体.md)
- [status](../bluetooth_hci_model_reference/P372_bt_hci_rp_le_read_rf_path_comp_结构体.md#a84a04bcc64ea6d50fe41e9b416a5ada1)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [tx_path_comp](../bluetooth_hci_model_reference/P372_bt_hci_rp_le_read_rf_path_comp_结构体.md#a827fa954277823efdc5838c317a1460a)
- [rx_path_comp](../bluetooth_hci_model_reference/P372_bt_hci_rp_le_read_rf_path_comp_结构体.md#a0f46a99c74006dc0a4dfd1a49c72e077)
- [bt_hci_cp_le_write_rf_path_comp](../bluetooth_hci_model_reference/P138_bt_hci_cp_le_write_rf_path_comp_结构体.md)
- [tx_path_comp](../bluetooth_hci_model_reference/P138_bt_hci_cp_le_write_rf_path_comp_结构体.md#a5f99b131f3fba91706bdc8277c1abba1)
- [rx_path_comp](../bluetooth_hci_model_reference/P138_bt_hci_cp_le_write_rf_path_comp_结构体.md#a11aad5607e444cf55dd5878f1f6f9436)
- [bt_hci_cp_le_set_privacy_mode](../bluetooth_hci_model_reference/P118_bt_hci_cp_le_set_privacy_mode_结构体.md)
- [id_addr](../bluetooth_hci_model_reference/P118_bt_hci_cp_le_set_privacy_mode_结构体.md#a404cc9f04cd11924445f12eb4471ef2e)
- [mode](../bluetooth_hci_model_reference/P118_bt_hci_cp_le_set_privacy_mode_结构体.md#a8ca00418b0638bba6ef586d6cbf253a5)
- [bt_hci_cp_le_rx_test_v3](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md)
- [rx_ch](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#abd33b70c948d4ee42d96d0d2e7f7cb1c)
- [phy](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#ad1c211c59cf34d76429d4d4548966630)
- [mod_index](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#a7ffde9dc565194c0108177cf11b02b5b)
- [expected_cte_len](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#ad1a1082d27b8a10e25eebd347404637c)
- [expected_cte_type](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#a55b5c4739e456167f17bf3899d096e61)
- [slot_durations](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#a5cd5a44b0832b9f6e2198b9ad714b99b)
- [switch_pattern_len](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#ab0832e72ef90b1269928378638fcb194)
- [ant_ids](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#aa6cd0835068f378949da182af13e2438)
- [bt_hci_cp_le_tx_test_v3](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md)
- [tx_ch](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#a6486882bc375f229a88bbfa53be49670)
- [test_data_len](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#a1c0828e51bb6c24e9dd1f12b5badcfea)
- [pkt_payload](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#ad8f2d2ca3ad3be28c0aec9e8a0e1bc61)
- [phy](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#a712a30d9d6afc7d302041e1de6721de4)
- [cte_len](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#a52d2d6dcc188d5f02904e0e56f461841)
- [cte_type](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#adf6b1653902fb13cc1ccc32cd91c990f)
- [switch_pattern_len](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#a459b850f35c61bf7f53d3730245cb4bb)
- [ant_ids](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#afdb6dd44108e9a4a21ac31a74c1e083f)
- [bt_hci_cp_le_set_cl_cte_tx_params](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md)
- [handle](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#a8f20e6e3bb408551d6cc494ad19391c4)
- [cte_len](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#ab5c4742cf37cf7e802423beb4a9b4fa2)
- [cte_type](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#a869192cea35f4cd57984614e4c8bb5a5)
- [cte_count](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#af5e82bf572b385904a0f24219bdc72ca)
- [switch_pattern_len](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#a8208571653e444221648d2a884eabfae)
- [ant_ids](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#a27a228653ea560a77369a6b1829a8a9d)
- [bt_hci_cp_le_set_cl_cte_tx_enable](../bluetooth_hci_model_reference/P089_bt_hci_cp_le_set_cl_cte_tx_enable_结构体.md)
- [handle](../bluetooth_hci_model_reference/P089_bt_hci_cp_le_set_cl_cte_tx_enable_结构体.md#a55125c808a888eeecfee9410bcb55859)
- [cte_enable](../bluetooth_hci_model_reference/P089_bt_hci_cp_le_set_cl_cte_tx_enable_结构体.md#a3530dae940caefeafb9de4ac761ee080)
- [bt_hci_cp_le_set_cl_cte_sampling_enable](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md)
- [sync_handle](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#a91d3458e2049ab434e220403b7ba235d)
- [sampling_enable](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#aca9e1316c716525f00308f64b8c6cec4)
- [slot_durations](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#aaaed0fc39158c653041fd760a00cecec)
- [max_sampled_cte](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#a38e770b3e5f9d7d63a564dfa7c80451f)
- [switch_pattern_len](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#a4f52142ef1d2365859189b7a2abe050b)
- [ant_ids](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#a67bb2dbfe1707f76a5e211e007459c22)
- [bt_hci_rp_le_set_cl_cte_sampling_enable](../bluetooth_hci_model_reference/P383_bt_hci_rp_le_set_cl_cte_sampling_enable_结构体.md)
- [status](../bluetooth_hci_model_reference/P383_bt_hci_rp_le_set_cl_cte_sampling_enable_结构体.md#a5962f97cef6e53452cdccab1c3440519)
- [sync_handle](../bluetooth_hci_model_reference/P383_bt_hci_rp_le_set_cl_cte_sampling_enable_结构体.md#a44db7f831e8d730ec3c80c01ef9543aa)
- [bt_hci_cp_le_set_conn_cte_rx_params](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md)
- [handle](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md#a76968866cf5c6ef4bfb983cb6b68a827)
- [sampling_enable](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md#a615cae822878cf1344a990e30fa80044)
- [slot_durations](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md#a6246d492b94c67af9604b89912dbdb61)
- [switch_pattern_len](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md#a89194a5b9e6c7f0c176c915e451911df)
- [ant_ids](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md#a519c37f5d797d8ddac5ba9be7c14b9f9)
- [bt_hci_rp_le_set_conn_cte_rx_params](../bluetooth_hci_model_reference/P384_bt_hci_rp_le_set_conn_cte_rx_params_结构体.md)
- [status](../bluetooth_hci_model_reference/P384_bt_hci_rp_le_set_conn_cte_rx_params_结构体.md#ad38bb356876c16904e408405607de73c)
- [handle](../bluetooth_hci_model_reference/P384_bt_hci_rp_le_set_conn_cte_rx_params_结构体.md#a3c3fb92d422e7ccaf0c98706d46b3e5a)
- [bt_hci_cp_le_set_conn_cte_tx_params](../bluetooth_hci_model_reference/P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md)
- [handle](../bluetooth_hci_model_reference/P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md#ae0a482982d804ffd7d16ea2b413e538d)
- [cte_types](../bluetooth_hci_model_reference/P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md#ab47f852b476ac2c35fc0631180e19fb4)
- [switch_pattern_len](../bluetooth_hci_model_reference/P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md#a8f0e5ee74662056f00eaa3a8c72f6fc4)
- [ant_ids](../bluetooth_hci_model_reference/P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md#abff85d652b3b2fd55ad78e53887cd7ce)
- [bt_hci_rp_le_set_conn_cte_tx_params](../bluetooth_hci_model_reference/P385_bt_hci_rp_le_set_conn_cte_tx_params_结构体.md)
- [status](../bluetooth_hci_model_reference/P385_bt_hci_rp_le_set_conn_cte_tx_params_结构体.md#a56f62b6d2c42cd22f73026a2fabc6986)
- [handle](../bluetooth_hci_model_reference/P385_bt_hci_rp_le_set_conn_cte_tx_params_结构体.md#aad553d484daed7ca08de132f4fb849ee)
- [bt_hci_cp_le_conn_cte_req_enable](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md)
- [handle](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md#af340b3b97f9fb12c24baa38415620b44)
- [enable](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md#aaf38e3d5664d81ae7ac8d3b1bb03c646)
- [cte_request_interval](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md#a956a1a8794b75e962d03cdcf81847cfc)
- [requested_cte_length](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md#a4d4e41bbe95457ce5e8ad68ffeb85200)
- [requested_cte_type](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md#a5a7443a86e770de4bf7292d813e966e7)
- [bt_hci_rp_le_conn_cte_req_enable](../bluetooth_hci_model_reference/P337_bt_hci_rp_le_conn_cte_req_enable_结构体.md)
- [status](../bluetooth_hci_model_reference/P337_bt_hci_rp_le_conn_cte_req_enable_结构体.md#a1e76e7a6da194a433c1fa6ac2bc36b80)
- [handle](../bluetooth_hci_model_reference/P337_bt_hci_rp_le_conn_cte_req_enable_结构体.md#af00adb07a144156a37fb5fc47ca61ccb)
- [bt_hci_cp_le_conn_cte_rsp_enable](../bluetooth_hci_model_reference/P028_bt_hci_cp_le_conn_cte_rsp_enable_结构体.md)
- [handle](../bluetooth_hci_model_reference/P028_bt_hci_cp_le_conn_cte_rsp_enable_结构体.md#a9d78072143513020620e02a744d4fa9b)
- [enable](../bluetooth_hci_model_reference/P028_bt_hci_cp_le_conn_cte_rsp_enable_结构体.md#ae5eaaae211732d772ea53f3936ab32d2)
- [bt_hci_rp_le_conn_cte_rsp_enable](../bluetooth_hci_model_reference/P338_bt_hci_rp_le_conn_cte_rsp_enable_结构体.md)
- [status](../bluetooth_hci_model_reference/P338_bt_hci_rp_le_conn_cte_rsp_enable_结构体.md#a8a21bc015408cc77c5d229cd77289dcc)
- [handle](../bluetooth_hci_model_reference/P338_bt_hci_rp_le_conn_cte_rsp_enable_结构体.md#ab16f226d871d7d55c3f900614d59d8a1)
- [bt_hci_rp_le_read_ant_info](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md)
- [status](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md#ae1388d3eee3085af7f2b0b57b2aa7b1e)
- [switch_sample_rates](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md#a2c78d3db239c9e00729d91834eb60f21)
- [num_ant](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md#a1f79b45751d39ebb9349df93d0ff2e13)
- [max_switch_pattern_len](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md#ae75fe0b9f5fe8c88a8e8482eef299348)
- [max_cte_len](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md#a625cc8fa8553eafbbb31cbc0b3f303c7)
- [bt_hci_cp_le_set_per_adv_recv_enable](../bluetooth_hci_model_reference/P116_bt_hci_cp_le_set_per_adv_recv_enable_结构体.md)
- [handle](../bluetooth_hci_model_reference/P116_bt_hci_cp_le_set_per_adv_recv_enable_结构体.md#a1e626eecf1d3f0820c3b2a13fd84b92f)
- [enable](../bluetooth_hci_model_reference/P116_bt_hci_cp_le_set_per_adv_recv_enable_结构体.md#a2187ec96822726daa5e43e910cc41cc3)
- [bt_hci_cp_le_per_adv_sync_transfer](../bluetooth_hci_model_reference/P055_bt_hci_cp_le_per_adv_sync_transfer_结构体.md)
- [conn_handle](../bluetooth_hci_model_reference/P055_bt_hci_cp_le_per_adv_sync_transfer_结构体.md#a991f77d6f2f0c301fe3322050b2d359f)
- [service_data](../bluetooth_hci_model_reference/P055_bt_hci_cp_le_per_adv_sync_transfer_结构体.md#a1327de0f9b2ebd1eaa97b51850087460)
- [sync_handle](../bluetooth_hci_model_reference/P055_bt_hci_cp_le_per_adv_sync_transfer_结构体.md#a38537b7f01a93f7a3e8cfcb92098a172)
- [bt_hci_rp_le_per_adv_sync_transfer](../bluetooth_hci_model_reference/P350_bt_hci_rp_le_per_adv_sync_transfer_结构体.md)
- [status](../bluetooth_hci_model_reference/P350_bt_hci_rp_le_per_adv_sync_transfer_结构体.md#adb536c4694d2e7c5b91e9f68986e97e1)
- [conn_handle](../bluetooth_hci_model_reference/P350_bt_hci_rp_le_per_adv_sync_transfer_结构体.md#ab8b4357fd92e01a5f61d3127b04c0318)
- [bt_hci_cp_le_per_adv_set_info_transfer](../bluetooth_hci_model_reference/P054_bt_hci_cp_le_per_adv_set_info_transfer_结构体.md)
- [conn_handle](../bluetooth_hci_model_reference/P054_bt_hci_cp_le_per_adv_set_info_transfer_结构体.md#a3b2f0c510ef9b385cb42bf9a194fa574)
- [service_data](../bluetooth_hci_model_reference/P054_bt_hci_cp_le_per_adv_set_info_transfer_结构体.md#a5f14c3265bffdf3e30a554a3686e9e0c)
- [adv_handle](../bluetooth_hci_model_reference/P054_bt_hci_cp_le_per_adv_set_info_transfer_结构体.md#a75b2c0fa1d50ef9d3761ac25f487750b)
- [bt_hci_rp_le_per_adv_set_info_transfer](../bluetooth_hci_model_reference/P349_bt_hci_rp_le_per_adv_set_info_transfer_结构体.md)
- [status](../bluetooth_hci_model_reference/P349_bt_hci_rp_le_per_adv_set_info_transfer_结构体.md#ab1592bfadd45315ff47e86b7c50374ad)
- [conn_handle](../bluetooth_hci_model_reference/P349_bt_hci_rp_le_per_adv_set_info_transfer_结构体.md#a696e5cab4d7507ea79b0e116c4bb92e2)
- [bt_hci_cp_le_past_param](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md)
- [conn_handle](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md#a9c99cdd5ae5de58960677781c2287c4d)
- [mode](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md#aa36345a550dfabeef48b430d1a1b0030)
- [skip](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md#a622499d51e917f7828629de2291812e5)
- [timeout](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md#aec9aa4ffe41c6b6f5cfcbc59eb57efca)
- [cte_type](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md#a47c571ff27a59e0a7cbcb460303ee194)
- [bt_hci_rp_le_past_param](../bluetooth_hci_model_reference/P348_bt_hci_rp_le_past_param_结构体.md)
- [status](../bluetooth_hci_model_reference/P348_bt_hci_rp_le_past_param_结构体.md#a9630362b3d885b13869a4c0fe9e97b12)
- [conn_handle](../bluetooth_hci_model_reference/P348_bt_hci_rp_le_past_param_结构体.md#ae6b8a5d7e790516de2f91e41fd893111)
- [bt_hci_cp_le_default_past_param](../bluetooth_hci_model_reference/P038_bt_hci_cp_le_default_past_param_结构体.md)
- [mode](../bluetooth_hci_model_reference/P038_bt_hci_cp_le_default_past_param_结构体.md#a2ef92304264ad0bf1560accf306bb6d9)
- [skip](../bluetooth_hci_model_reference/P038_bt_hci_cp_le_default_past_param_结构体.md#a214cb0597d0065bc2c056fe9c51a2220)
- [timeout](../bluetooth_hci_model_reference/P038_bt_hci_cp_le_default_past_param_结构体.md#a159f5245f86b27198264bdcf394d719f)
- [cte_type](../bluetooth_hci_model_reference/P038_bt_hci_cp_le_default_past_param_结构体.md#af18f679f5833c1d782b4e474af5d819c)
- [bt_hci_rp_le_default_past_param](../bluetooth_hci_model_reference/P341_bt_hci_rp_le_default_past_param_结构体.md)
- [status](../bluetooth_hci_model_reference/P341_bt_hci_rp_le_default_past_param_结构体.md#a292e2d655c77e8cda0d01fc07b43b8c4)
- [bt_hci_rp_le_read_buffer_size_v2](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md)
- [status](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md#a3b9cc0577d0f5f3c2b934a28915f2177)
- [acl_max_len](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md#ac391149d3d7442e074aad4b98659bd02)
- [acl_max_num](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md#a1c7938defb076d973b8339c17cc930df)
- [iso_max_len](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md#a9758d477c502575a1c176eb6a63e1a1a)
- [iso_max_num](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md#ac3379adf42f9bbee8ae72fb4a7606fd1)
- [bt_hci_cp_le_read_iso_tx_sync](../bluetooth_hci_model_reference/P061_bt_hci_cp_le_read_iso_tx_sync_结构体.md)
- [handle](../bluetooth_hci_model_reference/P061_bt_hci_cp_le_read_iso_tx_sync_结构体.md#a8edc469f73540d4300b1716c96e17c9f)
- [bt_hci_rp_le_read_iso_tx_sync](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md)
- [status](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md#a188ef5dba77c754c46094135cc52641c)
- [handle](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md#a8c0003043d3896b1ff93dc33dccc76b4)
- [seq](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md#af2a02f68aa0a757757c490e707954952)
- [timestamp](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md#a35520a3e50afc03ed969b6c5ca9e15d9)
- [offset](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md#a29770c3172d5e45409392aa8ffc835ef)
- [bt_hci_cis_params](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md)
- [cis_id](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#a6dcfca11d7f827b1b7a62b507620d4de)
- [c_sdu](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#a8a85b914ba5585c6b362da3deb8d42d9)
- [p_sdu](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#ae2bffbaf0c4dde9144a7887177b3ffdb)
- [c_phy](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#a5a5fcd9276d912446fe84d875ae74c2f)
- [p_phy](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#a18bc8e4b531d9fd16f18e10a0d931f6c)
- [c_rtn](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#aa7fa628692f959db63788c6580cc5c66)
- [p_rtn](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#ad55e197ccb70c83fcd4c1c6ba485f468)
- [bt_hci_cp_le_set_cig_params](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md)
- [cig_id](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a7dbf75c6ed92a053c4ec0d8f7268c92e)
- [c_interval](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a14f5c0cf7f99ab406714501038048035)
- [p_interval](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a50a260a15f3a0ceae716da6c04c5b768)
- [sca](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a46a657cdfbc7a49e6761d9f18d980c2a)
- [packing](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a79fc069492741f14f348650abef4c66b)
- [framing](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a867bf5ddbcadd27dbec2c3059d67d6d6)
- [c_latency](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#afec8ebd17cc6ca5b3d13ef54f406df62)
- [p_latency](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a810822396b97d54988ec57561b4ee7d5)
- [num_cis](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#adf468a8a195447a7bbed4dcd53d287f6)
- [cis](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#ac922e59065920421f40468754d2ba5a2)
- [bt_hci_rp_le_set_cig_params](../bluetooth_hci_model_reference/P381_bt_hci_rp_le_set_cig_params_结构体.md)
- [status](../bluetooth_hci_model_reference/P381_bt_hci_rp_le_set_cig_params_结构体.md#a8426a2b9927bee05fb9a46b4b261c743)
- [cig_id](../bluetooth_hci_model_reference/P381_bt_hci_rp_le_set_cig_params_结构体.md#a951dc88e0cde4e1f0274684498741eac)
- [num_handles](../bluetooth_hci_model_reference/P381_bt_hci_rp_le_set_cig_params_结构体.md#a8aff643e0ae41455eb9391cfdb45ebda)
- [handle](../bluetooth_hci_model_reference/P381_bt_hci_rp_le_set_cig_params_结构体.md#a2e95c6217d11169a8a611ea95dce70b6)
- [bt_hci_cis_params_test](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md)
- [cis_id](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#a0a215b4dffac2aae4ae4310c54de073e)
- [nse](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#ad0cc6d393a536cb3cd83d456b950fc52)
- [c_sdu](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#a98a120efb1495dd90858bef45eb95891)
- [p_sdu](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#aefeca493efe0141590570e8a44bb8f8d)
- [c_pdu](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#adc092a44b58bcc78f3dfe88528ca724c)
- [p_pdu](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#abce4bd6045642b4d29668865655f1548)
- [c_phy](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#aa7ba56fb91718d43ca30ff643757e08e)
- [p_phy](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#ab636126046023a329451673c57b4ce96)
- [c_bn](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#adf5dda2be46f3c2c1a1fe398672416ff)
- [p_bn](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#ac66b7183d8148250246f17a157dc3d29)
- [bt_hci_cp_le_set_cig_params_test](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md)
- [cig_id](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a161ae960cbd4f7833815285d04f87e46)
- [c_interval](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#aa392cbac058beefd0e410fcc9821a0c3)
- [p_interval](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a0cf0f3f7c10b29d74ab64aa30a4969de)
- [c_ft](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a1eae50a97188304852589fd95e994150)
- [p_ft](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#af2ed1bf1a6beaff884c3ce3faf26bfb2)
- [iso_interval](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#aa77765d90fde67c52e4f2d483f0a3ee0)
- [sca](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a1d060539ff26677c1326a6ed3394fb6e)
- [packing](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a7275312e8b1c8ebc2af7992f765b392c)
- [framing](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a2cb6745b8f908cd2e7d5f12a092c3b69)
- [num_cis](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a50c345ef03c669f476e143728f42cd6d)
- [cis](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a5e07eb0d7d13e57be457d1b77a5dba12)
- [bt_hci_rp_le_set_cig_params_test](../bluetooth_hci_model_reference/P382_bt_hci_rp_le_set_cig_params_test_结构体.md)
- [status](../bluetooth_hci_model_reference/P382_bt_hci_rp_le_set_cig_params_test_结构体.md#a932eadb4d750f79b4a7a9c3feb90fdcd)
- [cig_id](../bluetooth_hci_model_reference/P382_bt_hci_rp_le_set_cig_params_test_结构体.md#a65c11059bc00244e58d2ab8373e3e725)
- [num_handles](../bluetooth_hci_model_reference/P382_bt_hci_rp_le_set_cig_params_test_结构体.md#a10816d0875092c8e6bd4b13b819c43c7)
- [handle](../bluetooth_hci_model_reference/P382_bt_hci_rp_le_set_cig_params_test_结构体.md#a08b07863ed63ab627401c0c80bc3c7b4)
- [bt_hci_cis](../bluetooth_hci_model_reference/P002_bt_hci_cis_结构体.md)
- [cis_handle](../bluetooth_hci_model_reference/P002_bt_hci_cis_结构体.md#a84165d526c10a91fa42d306276d97c74)
- [acl_handle](../bluetooth_hci_model_reference/P002_bt_hci_cis_结构体.md#a754c3c75c0ad13a11d89fa3347112e2c)
- [bt_hci_cp_le_create_cis](../bluetooth_hci_model_reference/P033_bt_hci_cp_le_create_cis_结构体.md)
- [num_cis](../bluetooth_hci_model_reference/P033_bt_hci_cp_le_create_cis_结构体.md#acd348a7d68947af8e7119b2e1a864481)
- [cis](../bluetooth_hci_model_reference/P033_bt_hci_cp_le_create_cis_结构体.md#a5a323d09df7813fc9b834cc1d205d101)
- [bt_hci_cp_le_remove_cig](../bluetooth_hci_model_reference/P075_bt_hci_cp_le_remove_cig_结构体.md)
- [cig_id](../bluetooth_hci_model_reference/P075_bt_hci_cp_le_remove_cig_结构体.md#addf395d945f14afbf2d39fa4d0d22f31)
- [bt_hci_rp_le_remove_cig](../bluetooth_hci_model_reference/P379_bt_hci_rp_le_remove_cig_结构体.md)
- [status](../bluetooth_hci_model_reference/P379_bt_hci_rp_le_remove_cig_结构体.md#a1335f26f1dc67ff8e2a1960d1b24b1a0)
- [cig_id](../bluetooth_hci_model_reference/P379_bt_hci_rp_le_remove_cig_结构体.md#a82e74fbbce714b035b1e53fd5f1b09b5)
- [bt_hci_cp_le_accept_cis](../bluetooth_hci_model_reference/P021_bt_hci_cp_le_accept_cis_结构体.md)
- [handle](../bluetooth_hci_model_reference/P021_bt_hci_cp_le_accept_cis_结构体.md#aec6a6c80403d5827df10cd8722bc12e4)
- [bt_hci_cp_le_reject_cis](../bluetooth_hci_model_reference/P070_bt_hci_cp_le_reject_cis_结构体.md)
- [handle](../bluetooth_hci_model_reference/P070_bt_hci_cp_le_reject_cis_结构体.md#ad697d740bdf5a565090a548e7e8fd399)
- [reason](../bluetooth_hci_model_reference/P070_bt_hci_cp_le_reject_cis_结构体.md#aec5bd3e4d27b6e3a2653112b36a3d128)
- [bt_hci_rp_le_reject_cis](../bluetooth_hci_model_reference/P378_bt_hci_rp_le_reject_cis_结构体.md)
- [status](../bluetooth_hci_model_reference/P378_bt_hci_rp_le_reject_cis_结构体.md#af2dc8a839d3e19821ab8ec0d3dc427ec)
- [handle](../bluetooth_hci_model_reference/P378_bt_hci_rp_le_reject_cis_结构体.md#acd8311e13bdfd7edb2d404d80006f9d4)
- [bt_hci_cp_le_create_big](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md)
- [big_handle](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#af5412e4a69c05a09b2e818322636a98a)
- [adv_handle](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#aa686eec31ca4c831262dd34d41f9a1fb)
- [num_bis](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#ad8491c970417e63c6a98c12278a89c86)
- [sdu_interval](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a2960a9891b827529c9fa1b68a747e2d5)
- [max_sdu](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a06fd74e9a5f172060835524da5851c71)
- [max_latency](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a15018e5ebc124bbe90644b38fe3e7e76)
- [rtn](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a1cb0dd106bf4a1a0c473333d089c95e7)
- [phy](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a56cb773a03e4927c3b6bf4d2a6ed6ed9)
- [packing](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#ac027390db21320fb9d1002161c4c2f67)
- [framing](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a330916d60c05ec2ef7a71933b62c203a)
- [encryption](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a490bd68d137f8cf60ea2ccd5ea4495e9)
- [bcode](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a0b4b2d77cd0f579aab190336b14597c5)
- [bt_hci_cp_le_create_big_test](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md)
- [big_handle](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#ac202f5cee0c1d0456b200606860fd5ab)
- [adv_handle](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#aece09ae6264e0cc1a5548f1603a3f61a)
- [num_bis](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a6ce270f0afd185c44fa5a2c67a7783fb)
- [sdu_interval](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a331b1a8ef66804cf20d6681e1bc5aefb)
- [iso_interval](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a6475ae77af80e89bb65596bc6f907a58)
- [nse](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a402c19da1ecf273bc942ecc560730567)
- [max_sdu](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a7ebbc81306109e035f89154738900395)
- [max_pdu](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a2652e0f340f13635a5da6335ec43e801)
- [phy](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a731ca2f90c17a4f3f868660e51649ce6)
- [packing](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a49822f8e1617e30aab9b0d7d790697a3)
- [framing](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#acc5b2c30db0c7642d12019f8241dab26)
- [bn](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a734174187486ac760b8bf0e566166842)
- [irc](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a66ce7ba0498053a588de9097cbbc0891)
- [pto](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a2f2eaa258463dd51a9f6042e75ecfec6)
- [encryption](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a50c4308abda01581b436b7867304e982)
- [bcode](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a333319a03d2087067247c4f5e595b4e5)
- [bt_hci_cp_le_terminate_big](../bluetooth_hci_model_reference/P129_bt_hci_cp_le_terminate_big_结构体.md)
- [big_handle](../bluetooth_hci_model_reference/P129_bt_hci_cp_le_terminate_big_结构体.md#acb5fb9451cf890245a85704579b1d1c8)
- [reason](../bluetooth_hci_model_reference/P129_bt_hci_cp_le_terminate_big_结构体.md#a958ab6b2f2bb30c825060498e6917a18)
- [bt_hci_cp_le_big_create_sync](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md)
- [big_handle](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a6692dae077ce1ce4f31bc94b9d391afd)
- [sync_handle](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a70b031f24cdf231e5c168b155517eae0)
- [encryption](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a482edf3326e2dd720b14a03609c1256a)
- [bcode](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a053475c3af12e6e37dc4befcf634d68f)
- [mse](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a37050e3eb914ff06495695d44c3fdb50)
- [sync_timeout](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a55e83bc3722ce2dbf943879a80ef2872)
- [num_bis](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a7efae2c8dc46d13fb2abca677ac152b0)
- [bis](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a6d1050c2a0522be215d82d3874fed4b6)
- [bt_hci_cp_le_big_terminate_sync](../bluetooth_hci_model_reference/P026_bt_hci_cp_le_big_terminate_sync_结构体.md)
- [big_handle](../bluetooth_hci_model_reference/P026_bt_hci_cp_le_big_terminate_sync_结构体.md#ad7e4de2a9a3222c1bb8fa048cacd06fa)
- [bt_hci_rp_le_big_terminate_sync](../bluetooth_hci_model_reference/P336_bt_hci_rp_le_big_terminate_sync_结构体.md)
- [status](../bluetooth_hci_model_reference/P336_bt_hci_rp_le_big_terminate_sync_结构体.md#ad4d1d4238402ef829a1ff9ed3b1dc050)
- [big_handle](../bluetooth_hci_model_reference/P336_bt_hci_rp_le_big_terminate_sync_结构体.md#a741ab80e08e7ecfc5a0158ec0cf14654)
- [bt_hci_cp_le_req_peer_sca](../bluetooth_hci_model_reference/P077_bt_hci_cp_le_req_peer_sca_结构体.md)
- [handle](../bluetooth_hci_model_reference/P077_bt_hci_cp_le_req_peer_sca_结构体.md#a39d65681da55b26f2900f06cde637d88)
- [bt_hci_cp_le_setup_iso_path](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md)
- [handle](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a0054fede0e583cef0dbcf6ef3134e480)
- [path_dir](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a89c1324359a4fc2f10fee9ebbac5cf2b)
- [path_id](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a7c07d69b2005af1f7f2618f2bfa60d50)
- [codec_id](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a5256fc99b362e3a5f986ef2b71b29ccb)
- [controller_delay](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a31948436e6608f9943d34ce89a65c64c)
- [codec_config_len](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a1a816d8e8c434a05ea897b74bc4d89c7)
- [codec_config](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#ade4dee947e3d288f769d2d69fc57f96a)
- [bt_hci_rp_le_setup_iso_path](../bluetooth_hci_model_reference/P391_bt_hci_rp_le_setup_iso_path_结构体.md)
- [status](../bluetooth_hci_model_reference/P391_bt_hci_rp_le_setup_iso_path_结构体.md#adde60b0dc6ec3d8caccae1d55d78d9a4)
- [handle](../bluetooth_hci_model_reference/P391_bt_hci_rp_le_setup_iso_path_结构体.md#aa8effdcc4ba155b840ef789f20bad19e)
- [bt_hci_cp_le_remove_iso_path](../bluetooth_hci_model_reference/P076_bt_hci_cp_le_remove_iso_path_结构体.md)
- [handle](../bluetooth_hci_model_reference/P076_bt_hci_cp_le_remove_iso_path_结构体.md#ad0106791003f9d1173f2a9f102903c45)
- [path_dir](../bluetooth_hci_model_reference/P076_bt_hci_cp_le_remove_iso_path_结构体.md#a46e4b28917ff963ff4b672749fde0971)
- [bt_hci_rp_le_remove_iso_path](../bluetooth_hci_model_reference/P380_bt_hci_rp_le_remove_iso_path_结构体.md)
- [status](../bluetooth_hci_model_reference/P380_bt_hci_rp_le_remove_iso_path_结构体.md#ab22e50e594e19931526feacd9bff33a3)
- [handle](../bluetooth_hci_model_reference/P380_bt_hci_rp_le_remove_iso_path_结构体.md#ae3b7704359989ca13582a5cd3742f588)
- [bt_hci_cp_le_iso_transmit_test](../bluetooth_hci_model_reference/P049_bt_hci_cp_le_iso_transmit_test_结构体.md)
- [handle](../bluetooth_hci_model_reference/P049_bt_hci_cp_le_iso_transmit_test_结构体.md#adffb0d57afc090692ab36ebeaad21bbd)
- [payload_type](../bluetooth_hci_model_reference/P049_bt_hci_cp_le_iso_transmit_test_结构体.md#a0653c77af723cc43a6b911816a8db437)
- [bt_hci_rp_le_iso_transmit_test](../bluetooth_hci_model_reference/P345_bt_hci_rp_le_iso_transmit_test_结构体.md)
- [status](../bluetooth_hci_model_reference/P345_bt_hci_rp_le_iso_transmit_test_结构体.md#a01ae01d11c606f559107b8c54781d843)
- [handle](../bluetooth_hci_model_reference/P345_bt_hci_rp_le_iso_transmit_test_结构体.md#a0863c47551b328984e00c392f9f11660)
- [bt_hci_cp_le_iso_receive_test](../bluetooth_hci_model_reference/P047_bt_hci_cp_le_iso_receive_test_结构体.md)
- [handle](../bluetooth_hci_model_reference/P047_bt_hci_cp_le_iso_receive_test_结构体.md#ac1272441f5c7b79e1ef5f644f099d19e)
- [payload_type](../bluetooth_hci_model_reference/P047_bt_hci_cp_le_iso_receive_test_结构体.md#a9ce7e13fc1c1a7c87c01e1ecb24c5324)
- [bt_hci_rp_le_iso_receive_test](../bluetooth_hci_model_reference/P343_bt_hci_rp_le_iso_receive_test_结构体.md)
- [status](../bluetooth_hci_model_reference/P343_bt_hci_rp_le_iso_receive_test_结构体.md#a028a77001a5e24dda8fac38718103ef0)
- [handle](../bluetooth_hci_model_reference/P343_bt_hci_rp_le_iso_receive_test_结构体.md#a863a8a44af979a8b1b9d084563b2fe9a)
- [bt_hci_cp_le_read_test_counters](../bluetooth_hci_model_reference/P068_bt_hci_cp_le_read_test_counters_结构体.md)
- [handle](../bluetooth_hci_model_reference/P068_bt_hci_cp_le_read_test_counters_结构体.md#a230d973c2db177c3595bb4808ebf5cd2)
- [bt_hci_rp_le_read_test_counters](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md)
- [status](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md#ae1e78d68e9f55b31092a07575a66c1c0)
- [handle](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md#a8121f879a3fb5550cc1aa468aacb81b7)
- [received_cnt](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md#a8c4b2674fb129ca0de0bc45c608e13c7)
- [missed_cnt](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md#ae96d05ffb2fbc681c804b04c8791aeab)
- [failed_cnt](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md#af6261d3547cd9b377fedc7a36891c2f7)
- [bt_hci_cp_le_iso_test_end](../bluetooth_hci_model_reference/P048_bt_hci_cp_le_iso_test_end_结构体.md)
- [handle](../bluetooth_hci_model_reference/P048_bt_hci_cp_le_iso_test_end_结构体.md#ab792ec021319024828bd7609e0fe7e96)
- [bt_hci_rp_le_iso_test_end](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md)
- [status](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md#a16feaeb739f6ed34d9ce3fc86248955c)
- [handle](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md#a4a4625d7b78abf3c039842df2a72ce8b)
- [received_cnt](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md#a55490978e7416ecc308bf510f05afd4f)
- [missed_cnt](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md#a10b3ee6110bc0bb9279b22f9963715c1)
- [failed_cnt](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md#ab4352fd5d9b822fb7fb75f8f5e2db6a9)
- [bt_hci_cp_le_set_host_feature](../bluetooth_hci_model_reference/P105_bt_hci_cp_le_set_host_feature_结构体.md)
- [bit_number](../bluetooth_hci_model_reference/P105_bt_hci_cp_le_set_host_feature_结构体.md#adcca35df216061ea08bd27e10fefd5e9)
- [bit_value](../bluetooth_hci_model_reference/P105_bt_hci_cp_le_set_host_feature_结构体.md#a78b67164bce232466ab348f8937682c3)
- [bt_hci_rp_le_set_host_feature](../bluetooth_hci_model_reference/P388_bt_hci_rp_le_set_host_feature_结构体.md)
- [status](../bluetooth_hci_model_reference/P388_bt_hci_rp_le_set_host_feature_结构体.md#a2e7cfc16da9fc0d00c35111811bf7c28)
- [bt_hci_cp_le_read_iso_link_quality](../bluetooth_hci_model_reference/P060_bt_hci_cp_le_read_iso_link_quality_结构体.md)
- [handle](../bluetooth_hci_model_reference/P060_bt_hci_cp_le_read_iso_link_quality_结构体.md#a346fb3cf08203725d5943e42f03cb40d)
- [bt_hci_rp_le_read_iso_link_quality](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md)
- [status](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#aef80c600f8916c098e08c43ca718d630)
- [handle](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a9f2e8c26081ede43c7712b851d79f2cd)
- [tx_unacked_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#aae42e05dff474062726b92c6d45eae4f)
- [tx_flushed_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a12c0c3f9fe6c3c94742367f30bdcc630)
- [tx_last_subevent_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a0d4468f6871716414ef4a601791bac58)
- [retransmitted_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a7be135da9607045f60b616b84a68f5db)
- [crc_error_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a353070a64655a39f5410fe76e9168e97)
- [rx_unreceived_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a6a16d0aa7ed220bac1ade12eb0f7703e)
- [duplicate_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a68c23277e65dc5694f5a27ee2cd364ff)
- [bt_hci_cp_le_tx_test_v4](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md)
- [tx_ch](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a3ccae40f09b2763b2b07dc16982f3973)
- [test_data_len](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a7a8e2610fb8903ccfb6e4b08017f6112)
- [pkt_payload](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#abdd393eb264f04acf65e2dce4bd65ac0)
- [phy](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a5db011159fe75f4522e03ea1efdc57bd)
- [cte_len](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a8dea923a63e787de3bfe07611eb7a1ed)
- [cte_type](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#ae950f71a3fcfca0cf738bc28693256cf)
- [switch_pattern_len](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a2039a87b5f32c4a45b8f858808df7cdc)
- [ant_ids](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a3fe8ab7c0ee389dce8592cb7a38bc42c)
- [bt_hci_rp_le_read_all_local_supported_features](../bluetooth_hci_model_reference/P352_bt_hci_rp_le_read_all_local_supported_features_结构体.md)
- [status](../bluetooth_hci_model_reference/P352_bt_hci_rp_le_read_all_local_supported_features_结构体.md#ac4aeb5159bb91c8faf9d12461b005e89)
- [max_page](../bluetooth_hci_model_reference/P352_bt_hci_rp_le_read_all_local_supported_features_结构体.md#a3e200ffc8a5ecafc5e7173f1a48fe6b1)
- [features](../bluetooth_hci_model_reference/P352_bt_hci_rp_le_read_all_local_supported_features_结构体.md#a8cecb341ec3dfb335940af0a6e4751c6)
- [bt_hci_cp_le_read_all_remote_features](../bluetooth_hci_model_reference/P058_bt_hci_cp_le_read_all_remote_features_结构体.md)
- [handle](../bluetooth_hci_model_reference/P058_bt_hci_cp_le_read_all_remote_features_结构体.md#a2baf8df3a24b1b883768278459a156c7)
- [pages_requested](../bluetooth_hci_model_reference/P058_bt_hci_cp_le_read_all_remote_features_结构体.md#aa8cf7318871819cf425aa59ca15cc86d)
- [bt_hci_cp_le_tx_test_v4_tx_power](../bluetooth_hci_model_reference/P133_bt_hci_cp_le_tx_test_v4_tx_power_结构体.md)
- [tx_power](../bluetooth_hci_model_reference/P133_bt_hci_cp_le_tx_test_v4_tx_power_结构体.md#a2a8b1c31787066ad2b471aec5c261085)
- [bt_hci_rp_le_read_local_supported_capabilities](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md)
- [status](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#aaf578336893980f2ec1b2343b81860e5)
- [num_config_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a5f59d0b65cc4e7e44e487fa5535b76a9)
- [max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ad667ba51ffdbaf7754dea6f519615cb7)
- [num_antennas_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ae0767bb41b7b57e955ddbede2f83c166)
- [max_antenna_paths_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a7975eb0ce27f0326d1d909bffef57840)
- [roles_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a0958a5426e0057e2b8ccb80c222d0248)
- [modes_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#aaf09d10c19980729ef04654114919211)
- [rtt_capability](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a24ffa02b6a8bfbff8b7d32f5ee46bea5)
- [rtt_aa_only_n](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a3a16c62ea321620608d706a80d90575e)
- [rtt_sounding_n](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ababf476100298c2ba7d79bdadd7a9d1b)
- [rtt_random_payload_n](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ad90ce3e635b8bccd29eefe73303f6e42)
- [nadm_sounding_capability](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a3eb4830443e7912bf8ca97f603b91545)
- [nadm_random_capability](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a0e0bd5b1c624c7143b0229b5d3eeec6e)
- [cs_sync_phys_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#af3d1e7588f2429bb400fac81733748c3)
- [subfeatures_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a8e7cc92cc4099774e8d0b385fc5f3d79)
- [t_ip1_times_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a115ffe697da3e09ece4091493fa8f2da)
- [t_ip2_times_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a88a4277c5dea41b8171c33c85ed760bf)
- [t_fcs_times_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a81bd809a734b6cdde2d55e0b23e41237)
- [t_pm_times_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ab026e5abfdead47eca1c5d8d316bc62c)
- [t_sw_time_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ad07b464737c59b33de4c89948d4c5686)
- [tx_snr_capability](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a1806f2f5ec2738b026453bbdb8b38ce9)
- [bt_hci_rp_le_read_local_supported_capabilities_v2](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md)
- [status](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a4fbd5c95fd7f2f9131cd16ff04e64adf)
- [num_config_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a7d3faf86b443db272303d3b4ad45df2d)
- [max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a998504553ee046759214d0d220d8a3d3)
- [num_antennas_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#af21e203e96302114a411d9995cd63fa6)
- [max_antenna_paths_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a3307caaaf76bfc5cb1c88937ce788efd)
- [roles_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a7e061a636d3d0432ca9eb65e69a44710)
- [modes_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a7131d361abdc12c29a886e338075ae8a)
- [rtt_capability](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#afc6a9b21d8926b589cf25941e75ecb31)
- [rtt_aa_only_n](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a29667f70ea84458e304fe731d443e25a)
- [rtt_sounding_n](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a145d8fe34f80df9367105d1cfa7b59c1)
- [rtt_random_payload_n](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a7cc90e1e81657d0b755df281ba6806fc)
- [nadm_sounding_capability](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a36f4762d9053476e84088fe8807024a3)
- [nadm_random_capability](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#ae3f61c13562d8dec1812fc3c91c23539)
- [cs_sync_phys_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#acb720ede01b7041c9d5b6d6ade065048)
- [subfeatures_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a28b801d5310e4fd7e8285ba6361191df)
- [t_ip1_times_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a8704313f30e256e87460961f03e0719a)
- [t_ip2_times_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a1f97298da17187ea1ed96ec923f54523)
- [t_fcs_times_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a1d2e82062c0c41dce9e7428e4982223a)
- [t_pm_times_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a6a88f321faeea9e61bd38c696468d90f)
- [t_sw_time_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a61458332899b95c752b6343eda90013e)
- [tx_snr_capability](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a2fc5417dbbd91b4099fb4a27f01c18fd)
- [t_ip2_ipt_times_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#ac000a669ee53e1ca4ad99fd350fe72e6)
- [t_sw_ipt_time_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a2c51d311adcacada33b9dec7b4395865)
- [bt_hci_cp_le_read_remote_supported_capabilities](../bluetooth_hci_model_reference/P067_bt_hci_cp_le_read_remote_supported_capabilities_结构体.md)
- [handle](../bluetooth_hci_model_reference/P067_bt_hci_cp_le_read_remote_supported_capabilities_结构体.md#ac6f083563e2c72d37cf4e9e8fa695733)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md)
- [handle](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a8a884bca80550eb72a433f5ea280f702)
- [num_config_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a7a60c326707ebd60b96d25924e3c9e40)
- [max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#afbfe48ddad696315d6e021a85d32559d)
- [num_antennas_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a96b0c7868da711271e74b82fcfd32fc2)
- [max_antenna_paths_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a96a49382bef8f3163cd82899f59ed5fe)
- [roles_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#ae88cf07e3c8e6ad64a1beb60270d8961)
- [modes_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a93f4973a1229273c51f6a20e741e42ed)
- [rtt_capability](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a94fb0f963f706c303729d7a0088ef617)
- [rtt_aa_only_n](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#ae4b9b8ba0e83978f131541959062f691)
- [rtt_sounding_n](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a31c877363bd315786ef834215614d346)
- [rtt_random_payload_n](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a8f98235e9238a80602806fb60e1261bb)
- [nadm_sounding_capability](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a29781bbe7e25c39b06047725f1d11426)
- [nadm_random_capability](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a25faaf2be6db05c44256b9f559841c87)
- [cs_sync_phys_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a908322e5c02500abbdd8891c5248998d)
- [subfeatures_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a2b5c828a30525eee5b1ce48f3ba98896)
- [t_ip1_times_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a257b38d937c1111a66f6c28f1e221211)
- [t_ip2_times_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a0911e19deceb7f243ac706ddb4cf0a3a)
- [t_fcs_times_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#af959f1539f5bbf74b0e63db743a132f4)
- [t_pm_times_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a870e068fcc15dd44dca3ac24334000ee)
- [t_sw_time_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#ab77f7bda7302cad94805e8ea43b8bf14)
- [tx_snr_capability](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#aa9e48c6f0d22e9a64e8591a34409988e)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md)
- [handle](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ac599d7323d560b8f554bbaaf70aabd8b)
- [num_config_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a65a5b6ebdbc5793ca800ee202cb4676c)
- [max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#aead25f8f371ed85e66d05af852b90a9e)
- [num_antennas_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a6bb274c4c2ff4dc2c6136b0bc7515be3)
- [max_antenna_paths_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ad7c6799d86889b67d86ca44bac4238a6)
- [roles_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a6eff7fb52e3ef1074eb875af4c79a8aa)
- [modes_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a1ff4fede6b4d942f64ec2b94b222703b)
- [rtt_capability](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a0872c2a5399e1d82f334796dd35379ad)
- [rtt_aa_only_n](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a17d3094a1b93665e755b2111074de42c)
- [rtt_sounding_n](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ad342355fdc6396d6680b7e215ef4b16e)
- [rtt_random_payload_n](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a214f693e10c331091e34f09c2cfc9749)
- [nadm_sounding_capability](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a225720841ea95409879d51bd9a031fb7)
- [nadm_random_capability](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a22f1010c9f4de7902480d3f84d499fb1)
- [cs_sync_phys_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a2077365a697d7085d7db97fb35c391f4)
- [subfeatures_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a2e8693852819f5e4afa8cae90f8ae92c)
- [t_ip1_times_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ac370abefdc5a7acdf1e3c72093d11018)
- [t_ip2_times_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a8c63e46cf58623b3ca9cbfa7b802744e)
- [t_fcs_times_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#abf661cac9a1a2a5bf38180dbfc486bcd)
- [t_pm_times_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ac930e63945abfc0cdfdaa79164e114fa)
- [t_sw_time_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#afbe4805ccd9db70a596afdabb6963885)
- [tx_snr_capability](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ae757536a884e640451e35dd2fca90605)
- [t_ip2_ipt_times_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a30cee084044918cb450060a164bd4b30)
- [t_sw_ipt_time_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a8aa60cab3469fadd342a0a9b0d1b094f)
- [bt_hci_cp_le_security_enable](../bluetooth_hci_model_reference/P080_bt_hci_cp_le_security_enable_结构体.md)
- [handle](../bluetooth_hci_model_reference/P080_bt_hci_cp_le_security_enable_结构体.md#a772d3744d43f0447187040f2c6f0ac6e)
- [bt_hci_cp_le_cs_set_default_settings](../bluetooth_hci_model_reference/P037_bt_hci_cp_le_cs_set_default_settings_结构体.md)
- [handle](../bluetooth_hci_model_reference/P037_bt_hci_cp_le_cs_set_default_settings_结构体.md#a096c3238ccc6624bae89d5a45dd95600)
- [role_enable](../bluetooth_hci_model_reference/P037_bt_hci_cp_le_cs_set_default_settings_结构体.md#a04aea510e26136f874ccfbabbbd080bb)
- [cs_sync_antenna_selection](../bluetooth_hci_model_reference/P037_bt_hci_cp_le_cs_set_default_settings_结构体.md#aa001c88ab42250c2cfd604af11e0ae27)
- [max_tx_power](../bluetooth_hci_model_reference/P037_bt_hci_cp_le_cs_set_default_settings_结构体.md#a333341ec01554ab90fc5e340dbfb5130)
- [bt_hci_cp_le_read_remote_fae_table](../bluetooth_hci_model_reference/P065_bt_hci_cp_le_read_remote_fae_table_结构体.md)
- [handle](../bluetooth_hci_model_reference/P065_bt_hci_cp_le_read_remote_fae_table_结构体.md#a10bdfc4808586f7cccf025c63a6e28a5)
- [bt_hci_cp_le_write_cached_remote_fae_table](../bluetooth_hci_model_reference/P134_bt_hci_cp_le_write_cached_remote_fae_table_结构体.md)
- [handle](../bluetooth_hci_model_reference/P134_bt_hci_cp_le_write_cached_remote_fae_table_结构体.md#a330531f1809cddea8f1527f3b0a92e31)
- [remote_fae_table](../bluetooth_hci_model_reference/P134_bt_hci_cp_le_write_cached_remote_fae_table_结构体.md#a8594dd89888d1388f2a45a33e12e94d0)
- [bt_hci_cp_le_set_procedure_parameters](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md)
- [handle](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#ab8a15269255fb7d960ae712a844b9f35)
- [config_id](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a7d2f5d9242df436906b005e66c7bb75d)
- [max_procedure_len](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a5de9205fdf1b6e342f53a12aa82c10c5)
- [min_procedure_interval](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a22ecbaff0fd48a0716a15d265adc590e)
- [max_procedure_interval](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#ad46165bc5f6d875940ee53a8b98cb5b4)
- [max_procedure_count](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#ac6bb66fa24aec17a964f27365ca65ec9)
- [min_subevent_len](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a51fb8c789cefce09d5da2b86d5c862ce)
- [max_subevent_len](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#aa9ec99aff85de173ccb2d3f144c85319)
- [tone_antenna_config_selection](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#aa783e0e63c38ceee503c0b73ac873ca7)
- [phy](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#afcd4e8b390fd996ee134043ec2930fe8)
- [tx_power_delta](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#ade09ca9d42b0db682cf677d9ac4326d2)
- [preferred_peer_antenna](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a7a61ff539f68a02ea7aa466f182dc5ab)
- [snr_control_initiator](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a8524fd01e35094d2b78488c0a2876832)
- [snr_control_reflector](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#aa5a6a677b6e0d57658041e891535d74b)
- [bt_hci_cp_le_procedure_enable](../bluetooth_hci_model_reference/P057_bt_hci_cp_le_procedure_enable_结构体.md)
- [handle](../bluetooth_hci_model_reference/P057_bt_hci_cp_le_procedure_enable_结构体.md#af94d81f71c2fe587c848e34a430825bf)
- [config_id](../bluetooth_hci_model_reference/P057_bt_hci_cp_le_procedure_enable_结构体.md#ae1dc5c808bed301ddee6e9dd624c00a5)
- [enable](../bluetooth_hci_model_reference/P057_bt_hci_cp_le_procedure_enable_结构体.md#a3a203b453bd913db8bec91be9310003a)
- [bt_hci_op_le_cs_test](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md)
- [main_mode_type](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#af4cdfd8c8cab500277c06a82ac088577)
- [sub_mode_type](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a090c5d03cf829011196d644cd9f7c7db)
- [main_mode_repetition](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a60cc9a7c46f8cd0933dc2f5a68cca627)
- [mode_0_steps](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#aaf480890608b5cfc9151dac844e9a337)
- [role](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#afa0310f818002d7c1ac048f0db8c7f1c)
- [rtt_type](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#ae0234031d94e93653dd45e6e657c199f)
- [cs_sync_phy](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#af42701651bca5fe0353ae1de9c453f47)
- [cs_sync_antenna_selection](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#aef335dd7738634cb8f81c18e0350141e)
- [subevent_len](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a8ad67a5a0138f32cc5295074011a3808)
- [subevent_interval](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#ad52cd2862d2544448a5e175c58541f89)
- [max_num_subevents](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a1c105f7a4d48754322fee6992db8c175)
- [transmit_power_level](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#adf2f24dc6988f1f0e0457a6cf3141521)
- [t_ip1_time](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a0675dfbb050838d98f21cfa28af8615b)
- [t_ip2_time](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a7538e91b5ced2702965a21f8e754ebcc)
- [t_fcs_time](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#aa3d510663e5dcc44b5acd9d1c41746d5)
- [t_pm_time](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a981da50e0594b8bc05f811e5170b10f5)
- [t_sw_time](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a09c40ecd0d4e325e0c0504a9d8cd977b)
- [tone_antenna_config_selection](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#acaa428a37e68ff56c311397e53f46526)
- [cs_enhancements_1](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a06ac1b5aa8951fe4769a1360af44df82)
- [snr_control_initiator](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a551c06e651180867dd1d23b3fdf4c031)
- [snr_control_reflector](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a3c949d9a7eb4f56427f6e9f8be7cb77b)
- [drbg_nonce](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#aee8c125df0f7136a0ecdb9f04903aaef)
- [channel_map_repetition](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a8c23c2e6e8c38bf33fcd6d1e343f5982)
- [override_config](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#acc2d0768b69e5f5b593e5aff71b17f20)
- [override_parameters_length](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a373372a93d94e70d674c1c7b4c126734)
- [override_parameters_data](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a15a68fe7c98b2e242afd6eb67dd9b40a)
- [bt_hci_cp_le_cs_create_config](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md)
- [handle](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a3742081b071b992176b725448cc6ab29)
- [config_id](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#ae833b5f02f878f54dca1a25753eca1f3)
- [create_context](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a9dc7a6b577c33583b7ca7548e2b555ac)
- [main_mode_type](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a74c5fdfbc97b112c35ee318aa2b9b463)
- [sub_mode_type](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a34fa54e8bbd641bb0901b0b057134ffb)
- [min_main_mode_steps](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#aeb26115c8b500829ef6bc238aa3a495f)
- [max_main_mode_steps](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#aa13e091f99114bb5217489757c1522bd)
- [main_mode_repetition](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#acd11430a6c94b0f0c34e2788a2326a40)
- [mode_0_steps](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a909e409d55ac539a119e932899a97204)
- [role](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a5a17d6c72daaefcb55fdfa24194cc886)
- [rtt_type](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a709938176023c5482c91af8995001782)
- [cs_sync_phy](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#ac6c9c568918c9ef9aa4f2038a4922020)
- [channel_map](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#abab4907ec883430044bb9f9d6cf9f25d)
- [channel_map_repetition](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a8182f4becdef488b84f12fe7e4274193)
- [channel_selection_type](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a2c8be699bfd8eaaababd6d0de0b13e18)
- [ch3c_shape](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#addaa3592a97bda96a4aba17e809e4018)
- [ch3c_jump](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a0223c41abc034d515421fad8c3123387)
- [cs_enhancements_1](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a6088c8413ca175c0231fc53bfb168b29)
- [bt_hci_cp_le_cs_remove_config](../bluetooth_hci_model_reference/P036_bt_hci_cp_le_cs_remove_config_结构体.md)
- [handle](../bluetooth_hci_model_reference/P036_bt_hci_cp_le_cs_remove_config_结构体.md#a4591af2e952f514b185db12c5f1158d5)
- [config_id](../bluetooth_hci_model_reference/P036_bt_hci_cp_le_cs_remove_config_结构体.md#a9be71a1360f1ed14e6a7e205f5704e39)
- [bt_hci_cp_le_frame_space_update](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md)
- [handle](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md#a6f8ae56a870c76d06e47aa15d22ca341)
- [frame_space_min](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md#a9854593fb39c71bfd5ee3da6f606dd7f)
- [frame_space_max](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md#ab449a9514f175ad73942582f07cdf792)
- [phys](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md#a10fb9f808dec017325861c983beb6bc9)
- [spacing_types](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md#acbb6b64086a5710449b4d4e228575325)
- [bt_hci_le_read_min_supported_conn_interval_group](../bluetooth_hci_model_reference/P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md)
- [group_min](../bluetooth_hci_model_reference/P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md#a5cfd002c4dc82faa692ed1afa50692b5)
- [group_max](../bluetooth_hci_model_reference/P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md#abcd7d0eadf485b82993d421072cc8ba4)
- [group_stride](../bluetooth_hci_model_reference/P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md#a43ef933e3f445ac1366a3707b52ceffd)
- [bt_hci_op_le_read_min_supported_conn_interval](../bluetooth_hci_model_reference/P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md)
- [status](../bluetooth_hci_model_reference/P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md#aa049350b4f8fafe3bf74780924e1eeff)
- [min_supported_conn_interval](../bluetooth_hci_model_reference/P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md#a0c71077c8e7db5b1bdba1372bc7ac5ac)
- [num_groups](../bluetooth_hci_model_reference/P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md#a8bd4666fa42fb9a527fca5309e3bf0d6)
- [groups](../bluetooth_hci_model_reference/P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md#a92313039960815652380c301d4a5ce8d)
- [bt_hci_op_le_set_default_rate_parameters](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md)
- [conn_interval_min](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#af9afc0e463f068c113c0042f58dcc63d)
- [conn_interval_max](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#ad8051508f324d40bd95e9dbee97b1b2a)
- [subrate_min](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#a115579391f9fe7ec2536a21c3a42b3ab)
- [subrate_max](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#ad267cc8be963c1d16088a7c14bef19bf)
- [max_latency](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#a4efb8757f63f15e37070b3046490edcf)
- [continuation_number](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#aaa9dd1a946c7440e0a985276137ae096)
- [supervision_timeout](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#af0fbd935b200c98b5ef6477d127ccdfe)
- [min_ce_len](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#adb818d82c1c38f573a31f22b0ebc817b)
- [max_ce_len](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#a630ae05aff2e511b37a522fadd831dd0)
- [bt_hci_op_le_connection_rate_request](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md)
- [handle](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#a7178c6af0cdbf1376bd3e52a175be03e)
- [conn_interval_min](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#aee4d2070f12c33c5c6f6d93435f1f4b5)
- [conn_interval_max](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#ae290b39a2ba9c37595de67b877a61f3b)
- [subrate_min](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#ab06f3b29db55a6f56ab8cc1f2e7b95df)
- [subrate_max](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#a5ac425326df618f446bc891ea0b329ec)
- [max_latency](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#a35033b89faecdaa053e8bcff590ad5e7)
- [continuation_number](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#aa1123f8a8eafa16785e440b8b8a7e885)
- [supervision_timeout](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#a523cde9caf261ca3f3766b4d9648c7eb)
- [min_ce_len](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#a87ad44b9857515b42aff8200cfb42b37)
- [max_ce_len](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#af63ff615adc36c422d6be8db20e45c85)
- [bt_hci_evt_inquiry_complete](../bluetooth_hci_model_reference/P218_bt_hci_evt_inquiry_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P218_bt_hci_evt_inquiry_complete_结构体.md#aa8c1e8dc9807476f4759a3b3648b6332)
- [bt_hci_evt_conn_complete](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md#a3dbf4fef53279003b7304ffee4a55e56)
- [handle](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md#ad8877912008ea7445a67abc43aab5021)
- [bdaddr](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md#a60a2ca6a8f16e4562c12b369685efa9b)
- [link_type](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md#afd9a21adf7d35205fb7e222c2e9e0328)
- [encr_enabled](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md#a975617e8b568675a3ed8883cbe411557)
- [bt_hci_evt_conn_request](../bluetooth_hci_model_reference/P210_bt_hci_evt_conn_request_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P210_bt_hci_evt_conn_request_结构体.md#a03a2ee7ff7754173dff0809e4ebce9e6)
- [dev_class](../bluetooth_hci_model_reference/P210_bt_hci_evt_conn_request_结构体.md#a6059d7c56f45d2fe047a7324db1e820d)
- [link_type](../bluetooth_hci_model_reference/P210_bt_hci_evt_conn_request_结构体.md#ae11d550701f64717a7d6df5c89b92d0e)
- [bt_hci_evt_disconn_complete](../bluetooth_hci_model_reference/P212_bt_hci_evt_disconn_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P212_bt_hci_evt_disconn_complete_结构体.md#aed22ac781e9d70d11e7ebbe6f2e063bd)
- [handle](../bluetooth_hci_model_reference/P212_bt_hci_evt_disconn_complete_结构体.md#ab75f198a6495ad02a00bb3df99ab4258)
- [reason](../bluetooth_hci_model_reference/P212_bt_hci_evt_disconn_complete_结构体.md#a172554fbacf7aaa4dfbafe58b60fa5e6)
- [bt_hci_evt_auth_complete](../bluetooth_hci_model_reference/P203_bt_hci_evt_auth_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P203_bt_hci_evt_auth_complete_结构体.md#ae2b4b5bcc7195247626004d46ee22dd5)
- [handle](../bluetooth_hci_model_reference/P203_bt_hci_evt_auth_complete_结构体.md#a7a78803e156218f138866fbb13fdadce)
- [bt_hci_evt_remote_name_req_complete](../bluetooth_hci_model_reference/P292_bt_hci_evt_remote_name_req_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P292_bt_hci_evt_remote_name_req_complete_结构体.md#ab43d4a3c19d829b829cc7b40a67959f3)
- [bdaddr](../bluetooth_hci_model_reference/P292_bt_hci_evt_remote_name_req_complete_结构体.md#a380121873bf059b7c8a4abdf212f4235)
- [name](../bluetooth_hci_model_reference/P292_bt_hci_evt_remote_name_req_complete_结构体.md#a3e54674692f7fc1670fa389e293714c7)
- [bt_hci_evt_encrypt_change](../bluetooth_hci_model_reference/P213_bt_hci_evt_encrypt_change_结构体.md)
- [status](../bluetooth_hci_model_reference/P213_bt_hci_evt_encrypt_change_结构体.md#af063bbd28d29edbcc81e907631167de7)
- [handle](../bluetooth_hci_model_reference/P213_bt_hci_evt_encrypt_change_结构体.md#a7737f659115ca602c1224c364a4c7404)
- [encrypt](../bluetooth_hci_model_reference/P213_bt_hci_evt_encrypt_change_结构体.md#a61cc0e3c209acbb289d071515b44860a)
- [bt_hci_evt_remote_features](../bluetooth_hci_model_reference/P291_bt_hci_evt_remote_features_结构体.md)
- [status](../bluetooth_hci_model_reference/P291_bt_hci_evt_remote_features_结构体.md#a2cedd8392c87914272ff250a56c80574)
- [handle](../bluetooth_hci_model_reference/P291_bt_hci_evt_remote_features_结构体.md#ada0249bdb7108c5d347fea1218c4f878)
- [features](../bluetooth_hci_model_reference/P291_bt_hci_evt_remote_features_结构体.md#a70c97b9fbf7c363eab7b27f3a4e86e96)
- [bt_hci_evt_remote_version_info](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md)
- [status](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md#a196f9489183d6e0116ff687df66c60c0)
- [handle](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md#a1703a9ac9a5e1ba3ed396fe5799f9f51)
- [version](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md#a8442b9f2bdc6cbce564c9bcec4169a20)
- [manufacturer](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md#aaa9c3875143700b6ed013715cb3c7107)
- [subversion](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md#a02188119418a5a6dd8a4d0c37f5a060d)
- [bt_hci_evt_cmd_complete](../bluetooth_hci_model_reference/P206_bt_hci_evt_cmd_complete_结构体.md)
- [ncmd](../bluetooth_hci_model_reference/P206_bt_hci_evt_cmd_complete_结构体.md#a4da0539f81057722c8c322685bc12a40)
- [opcode](../bluetooth_hci_model_reference/P206_bt_hci_evt_cmd_complete_结构体.md#a3e61d980b4fa3084d3c50ead735fb76d)
- [bt_hci_evt_cc_status](../bluetooth_hci_model_reference/P205_bt_hci_evt_cc_status_结构体.md)
- [status](../bluetooth_hci_model_reference/P205_bt_hci_evt_cc_status_结构体.md#a97cceaa218700da9b529ebadbb08c42c)
- [bt_hci_evt_cmd_status](../bluetooth_hci_model_reference/P207_bt_hci_evt_cmd_status_结构体.md)
- [status](../bluetooth_hci_model_reference/P207_bt_hci_evt_cmd_status_结构体.md#aedd1560409005dbce409b892af1e3edf)
- [ncmd](../bluetooth_hci_model_reference/P207_bt_hci_evt_cmd_status_结构体.md#aed690e1cea2411df167e66cfaa742639)
- [opcode](../bluetooth_hci_model_reference/P207_bt_hci_evt_cmd_status_结构体.md#a34002b693dc201083be4be77cfddcdb5)
- [bt_hci_evt_hardware_error](../bluetooth_hci_model_reference/P216_bt_hci_evt_hardware_error_结构体.md)
- [hardware_code](../bluetooth_hci_model_reference/P216_bt_hci_evt_hardware_error_结构体.md#ab7be990e7cc32df43a3c976cb922e333)
- [bt_hci_evt_role_change](../bluetooth_hci_model_reference/P294_bt_hci_evt_role_change_结构体.md)
- [status](../bluetooth_hci_model_reference/P294_bt_hci_evt_role_change_结构体.md#aafe1a9e43a9a42d4030846180e55b8ef)
- [bdaddr](../bluetooth_hci_model_reference/P294_bt_hci_evt_role_change_结构体.md#a18dd22435ae40fcf1c4fd2b90b402c60)
- [role](../bluetooth_hci_model_reference/P294_bt_hci_evt_role_change_结构体.md#a2e5736d63e30326c33bec8ebdf986c62)
- [bt_hci_evt_num_completed_packets](../bluetooth_hci_model_reference/P288_bt_hci_evt_num_completed_packets_结构体.md)
- [num_handles](../bluetooth_hci_model_reference/P288_bt_hci_evt_num_completed_packets_结构体.md#a666ed2c19596a89ab0c77275cbe18d1e)
- [h](../bluetooth_hci_model_reference/P288_bt_hci_evt_num_completed_packets_结构体.md#a94fb176924f7e844704be28851366052)
- [bt_hci_evt_mode_change](../bluetooth_hci_model_reference/P287_bt_hci_evt_mode_change_结构体.md)
- [status](../bluetooth_hci_model_reference/P287_bt_hci_evt_mode_change_结构体.md#abd35ca68cd0c371350ee49d95aa68454)
- [handle](../bluetooth_hci_model_reference/P287_bt_hci_evt_mode_change_结构体.md#af33d9335a8e9253b481c91dbd0716e40)
- [mode](../bluetooth_hci_model_reference/P287_bt_hci_evt_mode_change_结构体.md#a91a9d6e910fd1999003ae41dce8eaa69)
- [interval](../bluetooth_hci_model_reference/P287_bt_hci_evt_mode_change_结构体.md#a12092d35d2866f9c04da6e9e9889416e)
- [bt_hci_evt_pin_code_req](../bluetooth_hci_model_reference/P289_bt_hci_evt_pin_code_req_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P289_bt_hci_evt_pin_code_req_结构体.md#a8649a30cd8c7ecf9ee006ddc2e625908)
- [bt_hci_evt_link_key_req](../bluetooth_hci_model_reference/P282_bt_hci_evt_link_key_req_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P282_bt_hci_evt_link_key_req_结构体.md#aed882dfb6b632383543bd7e60536ccc6)
- [bt_hci_evt_link_key_notify](../bluetooth_hci_model_reference/P281_bt_hci_evt_link_key_notify_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P281_bt_hci_evt_link_key_notify_结构体.md#a02647d66142c037b8bca2e748bc15319)
- [link_key](../bluetooth_hci_model_reference/P281_bt_hci_evt_link_key_notify_结构体.md#a4a1b50d8874d01a6a5dc5c52524c9bed)
- [key_type](../bluetooth_hci_model_reference/P281_bt_hci_evt_link_key_notify_结构体.md#a664580660a690af0d9ae3a62d79ad94b)
- [bt_hci_evt_data_buf_overflow](../bluetooth_hci_model_reference/P211_bt_hci_evt_data_buf_overflow_结构体.md)
- [link_type](../bluetooth_hci_model_reference/P211_bt_hci_evt_data_buf_overflow_结构体.md#ae0201e03ebb9b9b33e9eae593a56355f)
- [bt_hci_evt_conn_pkt_type_changed](../bluetooth_hci_model_reference/P209_bt_hci_evt_conn_pkt_type_changed_结构体.md)
- [status](../bluetooth_hci_model_reference/P209_bt_hci_evt_conn_pkt_type_changed_结构体.md#aabad2dfce94a19a83a5f52e334da18f8)
- [handle](../bluetooth_hci_model_reference/P209_bt_hci_evt_conn_pkt_type_changed_结构体.md#abde9bbcf2afa3c9a49662aa8192de868)
- [packet_type](../bluetooth_hci_model_reference/P209_bt_hci_evt_conn_pkt_type_changed_结构体.md#aa78e454d08e7c76b3e22242c4855ee62)
- [bt_hci_evt_inquiry_result_with_rssi](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md)
- [addr](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#af955dd1660f83e41e6d1b2b5aecf8133)
- [pscan_rep_mode](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#a0a5c188d0d40b4259cbeb613c0dd12cf)
- [reserved](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#a09914ee9998c0b59cb35ed74d08aa4f2)
- [cod](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#ad9b4920e2864ed8350de038dffe64574)
- [clock_offset](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#a1ee08f85103581994a88345cc94d7494)
- [rssi](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#a6d19e6400d7015db7122516e570d7989)
- [bt_hci_evt_remote_ext_features](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md)
- [status](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md#a4f1d489aaa5626e485d34a9ae4cf9a34)
- [handle](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md#a0191b80b4f4d5360972faa6d5edf5055)
- [page](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md#aeece2b8d46f4a3713d63df29058f2d9c)
- [max_page](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md#afa577407f4ded5404394f42e7c73e10b)
- [features](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md#a084199f8e30669c2a1a631af26c0d69a)
- [bt_hci_evt_le_per_adv_sync_established_v2](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md)
- [status](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#a96b975f5a2fcf193b0b58c230486ec36)
- [handle](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#ab7d3793e782d7b2bb311b8a5ac3a871b)
- [sid](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#a0ce9a9170d93ff69f25ff35eb163511f)
- [adv_addr](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#abd67ec989479eb793e7bf99a4cf371b8)
- [phy](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#a36b5c8454ee3635d2298592c83166f14)
- [interval](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#a958630cb9e275ab6f8ed0c548958e5ee)
- [clock_accuracy](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#a13ab0e87d6673a34e51f3112a5fd5a0c)
- [num_subevents](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#af4fb92baa4f98c08c990ba505faf9226)
- [subevent_interval](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#ad21df6269d8242d94ba9cbc1e0d4d344)
- [response_slot_delay](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#ac4c2bc8789513692ce0f2cc81aa59476)
- [response_slot_spacing](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#aacb6946dbfeb2ffbc251910853559329)
- [bt_hci_evt_le_per_advertising_report_v2](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md)
- [handle](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a34b15fb9b5b4f0d199ccf274dd489c6a)
- [tx_power](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a37a9eb7d417da9285e22cc7f83071c69)
- [rssi](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#ad598ffd0108825803a4734959a354bd8)
- [cte_type](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a3276c2e11c946744b73426f54bf62b8c)
- [periodic_event_counter](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a499d82e1e3cfc501d399f570ebbcdc42)
- [subevent](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#af27b23fe38e9ff092d8839cd81749456)
- [data_status](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a73496cc962721538e27e9924fff0f3db)
- [length](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a30f4e81346957ad4f9f0488dd93fafc3)
- [data](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a7af1cd4ec9df24e575a83a640eea36d2)
- [bt_hci_evt_le_past_received_v2](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md)
- [status](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#aefe79f973eda8c7c5670c7a721d55d8a)
- [conn_handle](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#adb011949f592ec7f8843d4fd47eca2e9)
- [service_data](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#acffc2fa22a16a3a12a4f7dfc3bb45866)
- [sync_handle](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#a00bf4bdf12fce6cbf2874b9c4ae09f9f)
- [adv_sid](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#a05d798c9415541ef7f5716992157b1a1)
- [addr](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#aff78554e8980635290767e9877ac479b)
- [phy](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#ae7a73293519ab45aec40a9a1aeaa4e89)
- [interval](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#a736af2c2ee0afd3cb00e8eb4d103991c)
- [clock_accuracy](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#a78853d14c3bf9a9aba3c4e15b2e06abb)
- [num_subevents](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#ab8a2a55fe071218284d60f1a2896945b)
- [subevent_interval](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#aefdc5ac7ef125f4dc5865c198b98c67d)
- [response_slot_delay](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#a9f55d5f6d17d11e72f7cac363a69fe97)
- [response_slot_spacing](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#acf711399e575295dcef73cfeeb844eab)
- [bt_hci_evt_le_per_adv_subevent_data_request](../bluetooth_hci_model_reference/P268_bt_hci_evt_le_per_adv_subevent_data_request_结构体.md)
- [adv_handle](../bluetooth_hci_model_reference/P268_bt_hci_evt_le_per_adv_subevent_data_request_结构体.md#ae6f6ef17edabfd210a7e6597087ff512)
- [subevent_start](../bluetooth_hci_model_reference/P268_bt_hci_evt_le_per_adv_subevent_data_request_结构体.md#a8f7fd9b149aa52422cb3eb874b91943d)
- [subevent_data_count](../bluetooth_hci_model_reference/P268_bt_hci_evt_le_per_adv_subevent_data_request_结构体.md#a45cdb248b80602a7f14f24e0324e6f97)
- [bt_hci_evt_le_per_adv_response](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md)
- [tx_power](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#a74e304822ec7a431802cf8a7539d640e)
- [rssi](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#a1100429baf398067a396a6ba8db6778a)
- [cte_type](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#a4197fbae54be038502312efc14b66320)
- [response_slot](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#aa5b5467f4edd52fb8de078b0948141f0)
- [data_status](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#aa524756d2cce0718ecfd66704eaf389d)
- [data_length](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#af68f0dc92118f78f6f5b0ffbf1854664)
- [data](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#ace3b58eba63b55ce5f3038d4a7877ec2)
- [bt_hci_evt_le_per_adv_response_report](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md)
- [adv_handle](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md#a9d746015a9c2b48c54008319c892b063)
- [subevent](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md#ad4f8f61150f82f4ba420e3c0a1f333c2)
- [tx_status](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md#a46a5b74321a80697fd700a276be18ed3)
- [num_responses](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md#a37f3519eefe33e87d49c7c2ad0f8b40c)
- [responses](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md#a3b1bcca7a7dbc6fcf5709f6152268b87)
- [bt_hci_evt_le_enh_conn_complete_v2](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md)
- [status](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#ad72ba07d766135a94474a9d004da1a66)
- [handle](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#affe2dba0634e0215579fb13d77016a8c)
- [role](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a3343de57a24fa2ebdccf9411f388817d)
- [peer_addr](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a7df28c9ddec607d5a84572bb421b7f5a)
- [local_rpa](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a10a1cbf0e9e21bc127dc64adadd53773)
- [peer_rpa](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a014e8bf891684c4cd9e5ec53d986d412)
- [interval](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a237b8313970cc63b7e57c0ce4913392e)
- [latency](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a3daa32ac19c4eda4a49bebb64f3145be)
- [supv_timeout](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a2b2ac4890eb9604a3f5cd40f55c2c066)
- [clock_accuracy](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a7bb168061803d1122e8ee47dc8af3ae9)
- [adv_handle](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a883ba3aed9aed00ec0ce425999d97180)
- [sync_handle](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a81dca94a6f2a8ea3da7a5a316daa5941)
- [bt_hci_evt_sync_conn_complete](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#accd17a95f35ab1988122df7584830f60)
- [handle](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#aa48aa29ff73e93e8d961013f066c1b5e)
- [bdaddr](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#a78f5560783400f1d1a63b2c9d69fa7ed)
- [link_type](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#aacf9919945e9b755913da145f0fe78ae)
- [tx_interval](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#a4b93873ad6f5388657511d87fc0a8c85)
- [retansmission_window](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#a68a31880c8aab9245be043c1719464d3)
- [rx_pkt_length](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#a6a455f56da4666cb602e6c05157e166d)
- [tx_pkt_length](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#ab4d4106d5120f10e8300834db12740d8)
- [air_mode](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#a5f6068569bf649bcd1d13928f56f9703)
- [bt_hci_evt_extended_inquiry_result](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md)
- [num_reports](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#a76e4e82d1dedaee94bd730a4134d7d77)
- [addr](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#a955a7d36736badfae1f39fa9eda61ebb)
- [pscan_rep_mode](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#aba4aac84e23ca9d283cb8af265dcaf0d)
- [reserved](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#ab6ec4b5efe058e225d173cbda9a16f2e)
- [cod](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#ab4ebcf09817827d1d10ddeee13832759)
- [clock_offset](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#a30c5586d954585006238e8c2b33a7601)
- [rssi](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#a21f7f48422bcfb867c9ca2e4411a2fbd)
- [eir](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#a1eba2841941f7cdbb00f548ebf0485e9)
- [bt_hci_evt_encrypt_key_refresh_complete](../bluetooth_hci_model_reference/P214_bt_hci_evt_encrypt_key_refresh_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P214_bt_hci_evt_encrypt_key_refresh_complete_结构体.md#afdd162cff0f1eedfe9e8ee7223b3226e)
- [handle](../bluetooth_hci_model_reference/P214_bt_hci_evt_encrypt_key_refresh_complete_结构体.md#af5562687a4f6e3a1e82cd1a81cec5ad6)
- [bt_hci_evt_io_capa_req](../bluetooth_hci_model_reference/P220_bt_hci_evt_io_capa_req_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P220_bt_hci_evt_io_capa_req_结构体.md#a52412f7bd8f8dea391904b9f2444b50a)
- [bt_hci_evt_io_capa_resp](../bluetooth_hci_model_reference/P221_bt_hci_evt_io_capa_resp_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P221_bt_hci_evt_io_capa_resp_结构体.md#adac9c9f3999099fd460651e3b012fd0f)
- [capability](../bluetooth_hci_model_reference/P221_bt_hci_evt_io_capa_resp_结构体.md#a851eae620ad90067957d4dec2f04efbe)
- [oob_data](../bluetooth_hci_model_reference/P221_bt_hci_evt_io_capa_resp_结构体.md#ab12325d1536fe6a75d0a137bea301e8f)
- [authentication](../bluetooth_hci_model_reference/P221_bt_hci_evt_io_capa_resp_结构体.md#a160cb3aea96bf698520e11673a40b2d7)
- [bt_hci_evt_user_confirm_req](../bluetooth_hci_model_reference/P297_bt_hci_evt_user_confirm_req_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P297_bt_hci_evt_user_confirm_req_结构体.md#aaeec83c50764c322af7cd64259e54a97)
- [passkey](../bluetooth_hci_model_reference/P297_bt_hci_evt_user_confirm_req_结构体.md#ac333729f5a7d9241ac26aeb7d3f77935)
- [bt_hci_evt_user_passkey_req](../bluetooth_hci_model_reference/P299_bt_hci_evt_user_passkey_req_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P299_bt_hci_evt_user_passkey_req_结构体.md#a7f1005423296906e0374050bc30781ce)
- [bt_hci_evt_ssp_complete](../bluetooth_hci_model_reference/P295_bt_hci_evt_ssp_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P295_bt_hci_evt_ssp_complete_结构体.md#a33d3d47c1cef71cfb787a1195d9b4ec2)
- [bdaddr](../bluetooth_hci_model_reference/P295_bt_hci_evt_ssp_complete_结构体.md#a5030cf334f97cdd982001b3278ed9db1)
- [bt_hci_evt_user_passkey_notify](../bluetooth_hci_model_reference/P298_bt_hci_evt_user_passkey_notify_结构体.md)
- [bdaddr](../bluetooth_hci_model_reference/P298_bt_hci_evt_user_passkey_notify_结构体.md#af020e1cd131473fe06a193529a0499ac)
- [passkey](../bluetooth_hci_model_reference/P298_bt_hci_evt_user_passkey_notify_结构体.md#a7f6a367e50d41cb7d8897db05db826be)
- [bt_hci_evt_le_meta_event](../bluetooth_hci_model_reference/P261_bt_hci_evt_le_meta_event_结构体.md)
- [subevent](../bluetooth_hci_model_reference/P261_bt_hci_evt_le_meta_event_结构体.md#a536464a525f8d0f9df915be5ee3d33da)
- [data](../bluetooth_hci_model_reference/P261_bt_hci_evt_le_meta_event_结构体.md#a5f08a4c81ebab1638d251b3bf7f8bfab)
- [bt_hci_evt_auth_payload_timeout_exp](../bluetooth_hci_model_reference/P204_bt_hci_evt_auth_payload_timeout_exp_结构体.md)
- [handle](../bluetooth_hci_model_reference/P204_bt_hci_evt_auth_payload_timeout_exp_结构体.md#a799bc3c63fe5083d61d8bf152ef4cee7)
- [bt_hci_evt_le_conn_complete](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a897981117139c0e53ea7275b689f3799)
- [handle](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a67618a1efa0149fadc1063a719d5b674)
- [role](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a8455e714d4333d90c2f117892f3dcd6f)
- [peer_addr](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a97e1aaa10832292ddfe4ee6731ef8999)
- [interval](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#abe4bc0407d0295329631cb14672a7ee7)
- [latency](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#ab60cb42ecc83632c61656cd352b71cbe)
- [supv_timeout](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a4a90c9824d167b6c45b301e18bfe7f17)
- [clock_accuracy](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a3fff4c3b30da5922f75d36d97fdeee33)
- [bt_hci_evt_le_advertising_info](../bluetooth_hci_model_reference/P223_bt_hci_evt_le_advertising_info_结构体.md)
- [evt_type](../bluetooth_hci_model_reference/P223_bt_hci_evt_le_advertising_info_结构体.md#a5943685ccd3491a883ba9450f700bb86)
- [addr](../bluetooth_hci_model_reference/P223_bt_hci_evt_le_advertising_info_结构体.md#a1d6863f1a601a2df9d772e3cc1fec118)
- [length](../bluetooth_hci_model_reference/P223_bt_hci_evt_le_advertising_info_结构体.md#a11c223103bf89300bd90cb8725746121)
- [data](../bluetooth_hci_model_reference/P223_bt_hci_evt_le_advertising_info_结构体.md#af7d9d720ca67714f2a809e2530a1ff98)
- [bt_hci_evt_le_advertising_report](../bluetooth_hci_model_reference/P224_bt_hci_evt_le_advertising_report_结构体.md)
- [num_reports](../bluetooth_hci_model_reference/P224_bt_hci_evt_le_advertising_report_结构体.md#ac69aab36aa421630357e4c6706c13e75)
- [adv_info](../bluetooth_hci_model_reference/P224_bt_hci_evt_le_advertising_report_结构体.md#a9762be19de1f24be4d4626e7e2f8205d)
- [bt_hci_evt_le_conn_update_complete](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md#ad428bd5e29d40f7551ccdd0747e429d6)
- [handle](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md#a81c0688a5e3b4b3a4d92fbc756a068d5)
- [interval](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md#a69aa00c0c50978b2aa620aad671119f3)
- [latency](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md#ade2421709a35e0cd0fce3a4d992470c3)
- [supv_timeout](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md#aca728975619a10a6e3280b127b59f2f1)
- [bt_hci_evt_le_remote_feat_complete](../bluetooth_hci_model_reference/P276_bt_hci_evt_le_remote_feat_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P276_bt_hci_evt_le_remote_feat_complete_结构体.md#a8a80bade7644f986fec41462843d8319)
- [handle](../bluetooth_hci_model_reference/P276_bt_hci_evt_le_remote_feat_complete_结构体.md#a9a0da26d9415169f02b6c9472120afe7)
- [features](../bluetooth_hci_model_reference/P276_bt_hci_evt_le_remote_feat_complete_结构体.md#a61101c21e317aa07b08725a7ffbb4b81)
- [bt_hci_evt_le_ltk_request](../bluetooth_hci_model_reference/P260_bt_hci_evt_le_ltk_request_结构体.md)
- [handle](../bluetooth_hci_model_reference/P260_bt_hci_evt_le_ltk_request_结构体.md#aed00ae384cb7d0deace8d0cc0f8e0068)
- [rand](../bluetooth_hci_model_reference/P260_bt_hci_evt_le_ltk_request_结构体.md#a0fcb7c6f8c52af50caa41d446294d72c)
- [ediv](../bluetooth_hci_model_reference/P260_bt_hci_evt_le_ltk_request_结构体.md#a14e8e3e380efd91ca5402b43bee7c9d3)
- [bt_hci_evt_le_conn_param_req](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md)
- [handle](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md#a4746a001a070f152a3c1c870a7e74df1)
- [interval_min](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md#a9a9dfc026feb46337b0a36920204b24e)
- [interval_max](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md#a0ed70d1a89f270073f78823d38af6ac9)
- [latency](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md#a9f61f0a3e6b6d2e2c6af2f4aef625b75)
- [timeout](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md#ae34de4a3d3e3e4686391eb9d9585dc87)
- [bt_hci_evt_le_data_len_change](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md)
- [handle](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md#a62ebc2f337f23f678c651bf3a276a2a7)
- [max_tx_octets](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md#ae5ce481170336acafbe85687c672281b)
- [max_tx_time](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md#a8264e7ec4aa37e9a699f81d0c56afa40)
- [max_rx_octets](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md#a60ecd89a8bbf06ae55b577e3d708d16f)
- [max_rx_time](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md#a90771e400b998565e7a8bbf4288edd01)
- [bt_hci_evt_le_p256_public_key_complete](../bluetooth_hci_model_reference/P262_bt_hci_evt_le_p256_public_key_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P262_bt_hci_evt_le_p256_public_key_complete_结构体.md#a57d51fca3a707b445db2534d1e175241)
- [key](../bluetooth_hci_model_reference/P262_bt_hci_evt_le_p256_public_key_complete_结构体.md#af482f81d438b878fb826edbac8d84833)
- [bt_hci_evt_le_generate_dhkey_complete](../bluetooth_hci_model_reference/P259_bt_hci_evt_le_generate_dhkey_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P259_bt_hci_evt_le_generate_dhkey_complete_结构体.md#a3d10643dd45a71b71d35dfa455ed8590)
- [dhkey](../bluetooth_hci_model_reference/P259_bt_hci_evt_le_generate_dhkey_complete_结构体.md#a8cd8ece786c1443ed43bd3b8fcd4d9bf)
- [bt_hci_evt_le_enh_conn_complete](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#ae26575416658bf285c45f57ddf426eb2)
- [handle](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#a13ceff445de6a89f6ea0e832e8b3fba9)
- [role](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#af24298f8c1d58882b4962a14086fc5c7)
- [peer_addr](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#a4906d6991489e95f8c74aacf5ad8c22e)
- [local_rpa](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#ab275bcb4a3dd09525b446c01e4e5fdad)
- [peer_rpa](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#a4ece4379733f1ab404fa03f4794192a4)
- [interval](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#ac0565ecf0c459275d147933bbdaa9fbc)
- [latency](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#a7276bf433c21ffcd3582463492af107b)
- [supv_timeout](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#aa99df131f3fb0330ff8051015d2b78dc)
- [clock_accuracy](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#a5641e5cb17df4613cd85f5ad3ba8541c)
- [bt_hci_evt_le_direct_adv_info](../bluetooth_hci_model_reference/P252_bt_hci_evt_le_direct_adv_info_结构体.md)
- [evt_type](../bluetooth_hci_model_reference/P252_bt_hci_evt_le_direct_adv_info_结构体.md#aed957c96860c5f92f9485ab743ce832b)
- [addr](../bluetooth_hci_model_reference/P252_bt_hci_evt_le_direct_adv_info_结构体.md#a66bbb3e53d84e8c39b216edf91ad131d)
- [dir_addr](../bluetooth_hci_model_reference/P252_bt_hci_evt_le_direct_adv_info_结构体.md#ad4ca2d5395bc4c5b95527ac1491c940e)
- [rssi](../bluetooth_hci_model_reference/P252_bt_hci_evt_le_direct_adv_info_结构体.md#a013e5d53ed53e4cd0b923a55c68e20bc)
- [bt_hci_evt_le_direct_adv_report](../bluetooth_hci_model_reference/P253_bt_hci_evt_le_direct_adv_report_结构体.md)
- [num_reports](../bluetooth_hci_model_reference/P253_bt_hci_evt_le_direct_adv_report_结构体.md#ae8d1f96739c8fda8827d1c0521f00f94)
- [direct_adv_info](../bluetooth_hci_model_reference/P253_bt_hci_evt_le_direct_adv_report_结构体.md#a82800d58d4c3ed1fca49b6575bd8f957)
- [bt_hci_evt_le_phy_update_complete](../bluetooth_hci_model_reference/P274_bt_hci_evt_le_phy_update_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P274_bt_hci_evt_le_phy_update_complete_结构体.md#a927a9e6982b29ecd4c3972b19a9bcdc2)
- [handle](../bluetooth_hci_model_reference/P274_bt_hci_evt_le_phy_update_complete_结构体.md#a70f472edef3b25fb23490ea6dcce9d43)
- [tx_phy](../bluetooth_hci_model_reference/P274_bt_hci_evt_le_phy_update_complete_结构体.md#ad184e10b7af71582db64ec5d3a66cff9)
- [rx_phy](../bluetooth_hci_model_reference/P274_bt_hci_evt_le_phy_update_complete_结构体.md#ad792ffec08aa8e383009e2e353a03fcd)
- [bt_hci_evt_le_ext_advertising_info](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md)
- [evt_type](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a040c27dbcb337162f7ca857b8cb84cfe)
- [addr](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#acec6858e41ae1b44a2a2ee6d6dbc294d)
- [prim_phy](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a088f0e6ea0dfbad25d5f72d0741f7d6d)
- [sec_phy](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#af4d863e12e6f8f19426a14af292fa6d2)
- [sid](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a5b4d4adff4d97c06311a76abd9847727)
- [tx_power](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a39217e77e495e8c4c6288917f8e4d2dc)
- [rssi](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a6213edbc3ae30f02a6bf2d8e069cd035)
- [interval](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a7da4e49c49eccbf009491bb7da01e111)
- [direct_addr](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a37f4e4981566b43d6e7c7dfffc5b13fb)
- [length](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a20ca10813f6b3aaba2756a5fe00d3878)
- [data](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a9e5536277b0132c8374147677a787b68)
- [bt_hci_evt_le_ext_advertising_report](../bluetooth_hci_model_reference/P257_bt_hci_evt_le_ext_advertising_report_结构体.md)
- [num_reports](../bluetooth_hci_model_reference/P257_bt_hci_evt_le_ext_advertising_report_结构体.md#a72fc9736934b415e88c51a1f96179871)
- [adv_info](../bluetooth_hci_model_reference/P257_bt_hci_evt_le_ext_advertising_report_结构体.md#a84b9c47a79ccea04198721e2f05ac1a8)
- [bt_hci_evt_le_per_adv_sync_established](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md)
- [status](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#a9ebe918fee3121168dc5b45e64aaf263)
- [handle](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#a3af8529a858992f347ce9570c5696133)
- [sid](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#ab11929ef8d3c71c6f2cb7c549be21282)
- [adv_addr](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#adf65527ea968f4ece37d7e3c91c795d1)
- [phy](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#ab7ce6f56a69b54f02cde8fdae6860e42)
- [interval](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#a4873b917a5bc140bb2f04ad2bee5dd69)
- [clock_accuracy](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#aee68069899cc10bc38ad9fb95cf9b7b7)
- [bt_hci_evt_le_per_advertising_report](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md)
- [handle](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#af81ce5bb18ef7fa1d94d00412886b081)
- [tx_power](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#a3a09aca94284a9e4af765d4da543698e)
- [rssi](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#af874c29b89326877b499f6be1052a626)
- [cte_type](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#aa683d1a4bd3a851f26b3028f566b76e4)
- [data_status](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#abf23b23a12cbfeb7f996e71e2fe8b11c)
- [length](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#a0ab1d3c5d7eb1487862451cc65c66a76)
- [data](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#a1f9cdfc01e46e59e957b0c557bae620a)
- [bt_hci_evt_le_per_adv_sync_lost](../bluetooth_hci_model_reference/P271_bt_hci_evt_le_per_adv_sync_lost_结构体.md)
- [handle](../bluetooth_hci_model_reference/P271_bt_hci_evt_le_per_adv_sync_lost_结构体.md#a286d534634411da53a2bda8cdfb077f8)
- [bt_hci_evt_le_adv_set_terminated](../bluetooth_hci_model_reference/P222_bt_hci_evt_le_adv_set_terminated_结构体.md)
- [status](../bluetooth_hci_model_reference/P222_bt_hci_evt_le_adv_set_terminated_结构体.md#a583409e2dc912af2bd5e83124fce3a72)
- [adv_handle](../bluetooth_hci_model_reference/P222_bt_hci_evt_le_adv_set_terminated_结构体.md#af35564406269144cfa2532cd510aa0bd)
- [conn_handle](../bluetooth_hci_model_reference/P222_bt_hci_evt_le_adv_set_terminated_结构体.md#af2503ee8e1c9add6927fa65b69c48551)
- [num_completed_ext_adv_evts](../bluetooth_hci_model_reference/P222_bt_hci_evt_le_adv_set_terminated_结构体.md#a192f13d6223e437261a225e6b28d04db)
- [bt_hci_evt_le_scan_req_received](../bluetooth_hci_model_reference/P278_bt_hci_evt_le_scan_req_received_结构体.md)
- [handle](../bluetooth_hci_model_reference/P278_bt_hci_evt_le_scan_req_received_结构体.md#a62c6d5e5b7079665c0aea8eb676a0433)
- [addr](../bluetooth_hci_model_reference/P278_bt_hci_evt_le_scan_req_received_结构体.md#a7dca5ad876dc97859a139d8bd4b207af)
- [bt_hci_evt_le_chan_sel_algo](../bluetooth_hci_model_reference/P230_bt_hci_evt_le_chan_sel_algo_结构体.md)
- [handle](../bluetooth_hci_model_reference/P230_bt_hci_evt_le_chan_sel_algo_结构体.md#a16393279e08073dad549e111e610c8e8)
- [chan_sel_algo](../bluetooth_hci_model_reference/P230_bt_hci_evt_le_chan_sel_algo_结构体.md#a976a62e81b094a59ce42cb6ad3ce45ac)
- [bt_hci_le_iq_sample](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md)
- [i](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md#aacf452456eecd4ad4dab083593b11104)
- [q](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md#a775b6e0ab1842594bc00998faec613f3)
- [bt_hci_evt_le_connectionless_iq_report](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md)
- [sync_handle](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a36f853d29b8dae1dd393546bbdec5ae2)
- [chan_idx](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#af50e710884a17191d22f652eaf5788fd)
- [rssi](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a09112f3711aca00b56045c46958c0992)
- [rssi_ant_id](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#af8c2055666a97f3c8d95747c59515c31)
- [cte_type](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a6b11b00199b002129c569cfec6e83174)
- [slot_durations](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a9d9f0cfe343d81c44e8342b81e2a0608)
- [packet_status](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#ab6fb0f6e32e32a3364ae79d867d9e640)
- [per_evt_counter](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#abfeb0aaa411464bbd7bca927219144fb)
- [sample_count](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a39109ea3f657d0566a73c7ca81bdd2b1)
- [sample](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a1a81f2c8653d85dc29582eed67b4a2a8)
- [bt_hci_evt_le_connection_iq_report](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md)
- [conn_handle](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a446f4eab3db19452a84023a676333d1d)
- [rx_phy](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#aa052e03491647acc9f7a6dc7d91cedcc)
- [data_chan_idx](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#ac01a14c591c8bd8e6313aff021ca8d61)
- [rssi](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a49e63523f7219174540666c7e5ab3550)
- [rssi_ant_id](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a135498a4abae604967f94840e2f88d2c)
- [cte_type](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a0188ce28a6c0a2002ae2c64a7bd95e52)
- [slot_durations](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a74670ca77bb2be81db2cee613dd9c82b)
- [packet_status](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#af66e8f09a4442b658b80a6eb4dd3064b)
- [conn_evt_counter](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a1f388ba96bd52f9ce0f68bacb2945ed8)
- [sample_count](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a801dd9373935ba06175ac52237fea759)
- [sample](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a5acc2683312523a1137db7897a7373a6)
- [bt_hci_evt_le_cte_req_failed](../bluetooth_hci_model_reference/P250_bt_hci_evt_le_cte_req_failed_结构体.md)
- [status](../bluetooth_hci_model_reference/P250_bt_hci_evt_le_cte_req_failed_结构体.md#a1433f25dee38014dbd2d061b6d75741a)
- [conn_handle](../bluetooth_hci_model_reference/P250_bt_hci_evt_le_cte_req_failed_结构体.md#aa903954fa411e4ae49a613b4e76219dc)
- [bt_hci_evt_le_past_received](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md)
- [status](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a1b2c229c99d06f44057b88458f168e7c)
- [conn_handle](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a1bdbaddb4003cea40738ee540ecb8789)
- [service_data](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#adaa1e432db60a2529ad6266f16604e15)
- [sync_handle](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a2cea2f3b9d51ace91ddf63639e821328)
- [adv_sid](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a110c7cdd2ff1178d1ca686abaae92b05)
- [addr](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a3e368e95a6831f823d2efa0c0bc1ef51)
- [phy](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#aedb668e6f3232b1db9035ea89ccf1b71)
- [interval](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a41ea6099d3cca1caf37ff518a4e95492)
- [clock_accuracy](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a00d570636a55c1d84723ad3bc5705d80)
- [bt_hci_evt_le_cis_established](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md)
- [status](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a4d90dbeda130a6142ff0b7f9e2ee7c16)
- [conn_handle](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a932e8df0222eb3bcf7bee753414d529e)
- [cig_sync_delay](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ac4e5a2535e3e8d3782adac63a4c5a8d9)
- [cis_sync_delay](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ae71d6753849ae3c57327c8763cab1802)
- [c_latency](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a877913bb4b9016c64793458de94d84a0)
- [p_latency](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#aefb2d4e0458cbe990903a9f449189c30)
- [c_phy](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a53ea1da3f31313ab73b511c72912bd33)
- [p_phy](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a25b84cf026775b582c7944e265ffb0b2)
- [nse](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a683856418764b1110d5c5fea0494fe1e)
- [c_bn](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ab6b2d892e3c1e4f6aedee722049b75d3)
- [p_bn](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ad0a79bfadd413bf572b697069695c0a5)
- [c_ft](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ad0f3bd5f81b660afbc4927a777c2c18e)
- [p_ft](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a200afaff044b9eea653d8aee13297dc2)
- [c_max_pdu](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ae9fdecff4342f25de30165a4531ad703)
- [p_max_pdu](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ae8b195f433570e28e42a5f9d321964de)
- [interval](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a0bcdc0d8b3b776660d2e51427f9634dd)
- [bt_hci_evt_le_cis_req](../bluetooth_hci_model_reference/P233_bt_hci_evt_le_cis_req_结构体.md)
- [acl_handle](../bluetooth_hci_model_reference/P233_bt_hci_evt_le_cis_req_结构体.md#af8529013adb87340298a89d4727e6867)
- [cis_handle](../bluetooth_hci_model_reference/P233_bt_hci_evt_le_cis_req_结构体.md#aeed6f4bf58cdb301d6b784a202722acc)
- [cig_id](../bluetooth_hci_model_reference/P233_bt_hci_evt_le_cis_req_结构体.md#ae0ef0ac224bde55de13df4e5eeaf26be)
- [cis_id](../bluetooth_hci_model_reference/P233_bt_hci_evt_le_cis_req_结构体.md#abdf99eeb7a30c8238bbabdcd60a4847a)
- [bt_hci_evt_le_big_complete](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#ad6787806a3622b3bd3da4512bb8ddffe)
- [big_handle](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a14eaa705f1df38337722a41e8189f807)
- [sync_delay](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a2847d5fc997f80a3e21b7e03d80c9574)
- [latency](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a2727d329c37e3b3644cfad02d86abb55)
- [phy](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#abfa6d6bc135350737451e053aa7d212c)
- [nse](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#ae77364aafe179588f7b8414292e35f5e)
- [bn](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a2327e42013033767af233d1c2c3acc56)
- [pto](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a6c295870732d65002ec21b4b607e7c0b)
- [irc](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a07163dee904412d6d8faca8563a944d9)
- [max_pdu](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a8b433ac376e347bf391d4dd804c469f3)
- [iso_interval](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a0b0d19d442ed8f1025165c435786ba09)
- [num_bis](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a995c8fe06ec087f16b771c38171745b1)
- [handle](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#af1c8bd66c3dba70df22f8655b4f27925)
- [bt_hci_evt_le_big_terminate](../bluetooth_hci_model_reference/P228_bt_hci_evt_le_big_terminate_结构体.md)
- [big_handle](../bluetooth_hci_model_reference/P228_bt_hci_evt_le_big_terminate_结构体.md#ad9c9e6d42661366d62d79163fa9ad1c7)
- [reason](../bluetooth_hci_model_reference/P228_bt_hci_evt_le_big_terminate_结构体.md#a0303ac64b825f93210dfc70a8a081ea6)
- [bt_hci_evt_le_big_sync_established](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md)
- [status](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a8feb21ef6eacf45dfc09b09e0bce04b1)
- [big_handle](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a31a05f8afb69e5885700cc4ad3b161b2)
- [latency](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#aebb25f9a63fa013ec6ef891ca498dbb4)
- [nse](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a383dc92f6d16ec971455e20665cd7496)
- [bn](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a451466916fbe2f220c277b4b4e62241d)
- [pto](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a6b750de25b2a1afc38995030953364ce)
- [irc](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#afd52315dafe02ee28bc26f058b12fe9e)
- [max_pdu](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a13db0d402636a71ed029575c1e5771c5)
- [iso_interval](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a610313c11c65faf82e06a121affb8b2b)
- [num_bis](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a2fa405310a8fed0341001b316ca7bd4f)
- [handle](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a48766968cb677614f525ea36551ad6c8)
- [bt_hci_evt_le_big_sync_lost](../bluetooth_hci_model_reference/P227_bt_hci_evt_le_big_sync_lost_结构体.md)
- [big_handle](../bluetooth_hci_model_reference/P227_bt_hci_evt_le_big_sync_lost_结构体.md#ae59a9c18363f7aee67563494d98aa971)
- [reason](../bluetooth_hci_model_reference/P227_bt_hci_evt_le_big_sync_lost_结构体.md#a02b724a60e71805088aefca9989ad878)
- [bt_hci_evt_le_req_peer_sca_complete](../bluetooth_hci_model_reference/P277_bt_hci_evt_le_req_peer_sca_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P277_bt_hci_evt_le_req_peer_sca_complete_结构体.md#a814d17b8aae9dd68f57402c857ca1810)
- [handle](../bluetooth_hci_model_reference/P277_bt_hci_evt_le_req_peer_sca_complete_结构体.md#ab6b648e7f4bff9e84b274e9e22a26166)
- [sca](../bluetooth_hci_model_reference/P277_bt_hci_evt_le_req_peer_sca_complete_结构体.md#a88f93ead6ec67e1612b1a0e8402a30e7)
- [bt_hci_evt_le_path_loss_threshold](../bluetooth_hci_model_reference/P265_bt_hci_evt_le_path_loss_threshold_结构体.md)
- [handle](../bluetooth_hci_model_reference/P265_bt_hci_evt_le_path_loss_threshold_结构体.md#a19b1e37c5e35e1e18424615b5c25d37f)
- [current_path_loss](../bluetooth_hci_model_reference/P265_bt_hci_evt_le_path_loss_threshold_结构体.md#ac2b04c57137dcb6812fda06d4a22402a)
- [zone_entered](../bluetooth_hci_model_reference/P265_bt_hci_evt_le_path_loss_threshold_结构体.md#add7984e06d523bb34e8380dae1710b7f)
- [bt_hci_evt_le_transmit_power_report](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md)
- [status](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#af1629e59dd651e1616b89f4958f47c92)
- [handle](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#a4feadb14800c1b51a9cc523c1d6a9063)
- [reason](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#a341cc0c5cc1ea969e2024b67056a5439)
- [phy](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#ad6130863713cf31a1cbe33de9fb5428f)
- [tx_power_level](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#aa0df9c50a555fa40ed25a14f7b6a5e77)
- [tx_power_level_flag](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#a2dc33da8f36cceda362d0c87098b02d6)
- [delta](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#ac42d60325235f517728ff44385361db2)
- [bt_hci_evt_le_biginfo_adv_report](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md)
- [sync_handle](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a8be20bfc607e6ce34ea75c53e285b0d5)
- [num_bis](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#ae68f803bbc3f06e7190f62be98d2fe66)
- [nse](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#ae28d5378a7e2ef59fabb62a3a430ccc8)
- [iso_interval](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#ae92b69ab0bc257d4f50b98e071c6038b)
- [bn](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#ada35f690706be1c6ee8f40787bbe53e5)
- [pto](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#af3a871d3de34b90fc2b09b0725caf479)
- [irc](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a9c1235653245b517a105570c60ddfa09)
- [max_pdu](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a12a000c049e85d2b24720d1a362d28df)
- [sdu_interval](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a81e236ceb24012bc267f656f20f1f8c4)
- [max_sdu](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a084c13c4b0c9c8dca0653b56e53a0c74)
- [phy](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a2301112acf22cf68d6495ff85f0f29bf)
- [framing](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#abe0636beae2f51004193ad5f7c9efeef)
- [encryption](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#ae63eaf93f728109b5fb77ca3179ba99c)
- [bt_hci_evt_le_subrate_change](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md)
- [status](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#aa49286a63d565feaf3d9329cd024ee9f)
- [handle](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#adc08125e663a99c7232d0755c4bd760b)
- [subrate_factor](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#a9387ffe45a856f7f443f5116a59a9ff2)
- [peripheral_latency](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#a95aaed5f8c93a1d6e8cab4c7ebfad8d7)
- [continuation_number](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#a712b8b818115f1797787aab229040c8a)
- [supervision_timeout](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#a2ad4a06feeb0d6d36461b4a4e53dfeb1)
- [bt_hci_evt_le_cis_established_v2](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md)
- [status](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a1f43b72368227f212511bb248b4a0e22)
- [conn_handle](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a7a7b8303183a916225bb0a3ea11d5480)
- [cig_sync_delay](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a754ad7e68821da0bdb8da0bdeb3b4697)
- [cis_sync_delay](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#af134783424a77274abac44613bf61264)
- [c_latency](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#ae580ff8c0ef4cd03365cbf1a06aed8bc)
- [p_latency](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a26b25e1615991977735cbfc679d747f3)
- [c_phy](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a9b7ba96597a5131927e365b7a45f8d6f)
- [p_phy](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a5a0b08098ac4e6ec93a6ecbbbf4ef587)
- [nse](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#ac3a87b20b2f10e980639d232a013f702)
- [c_bn](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a5f68c3cba98ed96afef0949f6b14ded9)
- [p_bn](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a64b48b20283415100fc8bdf33edf2b0e)
- [c_ft](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a2de704a032ac2379528991f2d01e6979)
- [p_ft](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a3b1fc27cca2bc85c36e257aabd8ea612)
- [c_max_pdu](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#acd8cf2d2d85b65d839256f3412a4bb43)
- [p_max_pdu](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#aeea230245aa75dd7f44bf5a4a286e9a5)
- [interval](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a71762f8a31e20b233a252ac974f6d329)
- [sub_interval](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a353409fe069aba91c5372ee8ae6e1b79)
- [c_max_sdu](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#ad054af39ddad854423379b3cc7aafc26)
- [p_max_sdu](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a2a060c0bb2831eb3df0dc8ffb74ecebd)
- [c_sdu_interval](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a926a5faeb98a99333310d860da37f6f5)
- [p_sdu_interval](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#acf30d6a745803fd4e984d66548ceff58)
- [framing](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#af59ca6d54ca770ef8334ea091bcc53f6)
- [bt_hci_evt_le_read_all_remote_feat_complete](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md#acab09b5b552faef296c6e0442c4a2bc9)
- [handle](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md#af4a77910c32dbbdb259a9532818a0746)
- [max_remote_page](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md#a3582ff03fd6a680e006b94ff6080dc37)
- [max_valid_page](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md#aefc3508368f6a103c9b2d218f66f6a11)
- [features](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md#afd04ae00d6ce4b2cb57861b0cd2e9a03)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a40980265955d4d58a9b5407ff845fde4)
- [conn_handle](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a4f8fe99c2392c06125ba94e61aed0e6c)
- [num_config_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ab09a466b2a9a0be5f5021f1da0d7393a)
- [max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ac73a8bf5425c80739e84cb30ce94f3e7)
- [num_antennas_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#adcf35e055d04775c444fa28655b95337)
- [max_antenna_paths_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a50ad0408019dce16685215c6a1b6d0ef)
- [roles_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a99f9f7b08de6b41e88cea10ba0ca6010)
- [modes_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ab7a35b1093ece7ae9cc5def4a3e473b2)
- [rtt_capability](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ace95740224b31c127f5e13550cb5a23a)
- [rtt_aa_only_n](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a843968ec69106d076596e110407d8a1a)
- [rtt_sounding_n](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a7f796e2eda8d3c7eae556932e37cd93d)
- [rtt_random_payload_n](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a3f275ad58ca745347172ad0b89faf2c4)
- [nadm_sounding_capability](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#adebb5328c7baeaa786bc185fec432e40)
- [nadm_random_capability](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a7af3067f319be094af31512d4ee5101e)
- [cs_sync_phys_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a1f303dc3aa8a23fccde27a2d2f64d732)
- [subfeatures_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ac83543c17606e401d919fce841a12c6c)
- [t_ip1_times_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ad330adf1ae5b9b84756d36801a4cf289)
- [t_ip2_times_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a0a1d9dcdf184e49349e86980da2e4bed)
- [t_fcs_times_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a44869fd19ae813830e38f6e4b88dbb1d)
- [t_pm_times_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#afef9f37784d75f54521793f07b5baece)
- [t_sw_time_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a21a322fc8efd0c410dda78e2652d506d)
- [tx_snr_capability](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ae3d06bce4df7a2ca07c5d6dd01124743)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md)
- [status](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a8695548057df5e398f65de93fd097b04)
- [conn_handle](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#adb3ce0c00b922e72373a93cb5d0f2f1f)
- [num_config_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ab21b4a5b2e3005fc3589251c7b8f77f1)
- [max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a9e2a36e0181a8cf5a9d61b8b31e21617)
- [num_antennas_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ad1f03a6a550a5c5cb9b0c997c239ba6a)
- [max_antenna_paths_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ac130ecc14ce78f0c179ad56a1985d60c)
- [roles_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a2e7d55a93000730a565c93b3394186e3)
- [modes_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#aa78b03177bbfc69de0a066f610b1cfa6)
- [rtt_capability](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#aba890de001e752b497bc91bd6356c359)
- [rtt_aa_only_n](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ae8091780f4153ead9a9414593b648f5a)
- [rtt_sounding_n](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ab93bb486d50a79c34a6002885436605b)
- [rtt_random_payload_n](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a73b7054a056ca3256098608e565033b2)
- [nadm_sounding_capability](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a43a8dd8b09c9e498b64798fcfe73af53)
- [nadm_random_capability](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a974007b9f1d81991f55c40cb1da1c51e)
- [cs_sync_phys_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#aff9e1f081101d2eabc83a7a2ce99d64f)
- [subfeatures_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#abe01a9d4d6fdb042fdfa5c045ac66519)
- [t_ip1_times_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ab692972f1388e6641493a5cc0faf2fac)
- [t_ip2_times_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#aa3e4e049cbb322a35171686635e2cc9c)
- [t_fcs_times_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a77669a86a0c75439417d4e53629a9cfd)
- [t_pm_times_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ad5c7c16d0b2096d4c00156800bf9181b)
- [t_sw_time_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a0c60c0b2677a8635a185277453db9613)
- [tx_snr_capability](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a07642a2edeb882e5c9a2a7727e8a55fd)
- [t_ip2_ipt_times_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a365c4afcf1c034bb42c24ce4bedbf1c3)
- [t_sw_ipt_time_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#af7f35ce7c16fc7cf1d76be1450d4566c)
- [bt_hci_evt_le_cs_read_remote_fae_table_complete](../bluetooth_hci_model_reference/P242_bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P242_bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体.md#a1ee4d133955f28f45d16226730344428)
- [conn_handle](../bluetooth_hci_model_reference/P242_bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体.md#adcdfbfd2d9c19be0c41121235fbb8eaa)
- [remote_fae_table](../bluetooth_hci_model_reference/P242_bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体.md#ae1ca6d2d4f4305565f1d491ef202fcad)
- [bt_hci_evt_le_cs_security_enable_complete](../bluetooth_hci_model_reference/P245_bt_hci_evt_le_cs_security_enable_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P245_bt_hci_evt_le_cs_security_enable_complete_结构体.md#aaf2de8591b18cd36709f7ef755bee917)
- [handle](../bluetooth_hci_model_reference/P245_bt_hci_evt_le_cs_security_enable_complete_结构体.md#aaa96a8944598914e4439249ba489f726)
- [bt_hci_evt_le_cs_config_complete](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#ae94aa8c92a8d4b33213adc8fc029a02d)
- [handle](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a511021f717538d4ae25eb28ad82c5f99)
- [config_id](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a544b3480034087ca01d64a41c1c4b8f9)
- [action](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a748fcb3cbd396851a3d159887b12b3e0)
- [main_mode_type](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a14f4c29a7f84463f048364389341c7b5)
- [sub_mode_type](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a55789928018a6124d87e76709b1b77d9)
- [min_main_mode_steps](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a21928853b505764e64fcc9190905b12c)
- [max_main_mode_steps](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a9b14655fa6bb3c7ac43561a399019a76)
- [main_mode_repetition](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a7fe1af954bae025b9b8bbef70bd1c60e)
- [mode_0_steps](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a705a7be2d5ce02c4d78319f4f842b87e)
- [role](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a6f84ebf8a34a830ced1fc738d46fe244)
- [rtt_type](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#ae64ff5dbd9d704c3a7f4c5b98ada399c)
- [cs_sync_phy](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#ad0454e31d55ec25a21bc272cae999238)
- [channel_map](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#abcf0c43f33a85bcd860323212d57ce5b)
- [channel_map_repetition](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a1e5ba3ebb5dcac2105a0f859683505bc)
- [channel_selection_type](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#aa323b4a74f7fce33e884d0c32e4014d0)
- [ch3c_shape](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a73bd134e9337a9a47e41bba04623ee0b)
- [ch3c_jump](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a5f886c16acd561e143a8796fcc1ea5af)
- [cs_enhancements_1](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a45a1b908385be6a5289698dd08d8a610)
- [t_ip1_time](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#afd62b1ffe5388c7f094cb086da4c86ba)
- [t_ip2_time](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a8fafd0e139a9c85830468e5a056c42b7)
- [t_fcs_time](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a7aa0fd8a1c9c7270059725416dd0a90f)
- [t_pm_time](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a7d64425b6aa44b01332ce6fac7813471)
- [bt_hci_le_cs_step_data_mode_0_initiator](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md)
- [packet_quality_aa_check](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md#a811eb38a04e63b12be9e25291126ccc1)
- [packet_quality_bit_errors](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md#a339252cacafd05e85c0fb19776343e17)
- [packet_rssi](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md#a11edf6e1c1da5d24aa1136521a249f52)
- [packet_antenna](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md#ad9a2193cbe5381d30494dbf6f8d84482)
- [measured_freq_offset](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md#a48fc1fd87869d4ca2b70c42d5c4e1d75)
- [bt_hci_le_cs_step_data_mode_0_reflector](../bluetooth_hci_model_reference/P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md)
- [packet_quality_aa_check](../bluetooth_hci_model_reference/P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md#a9c34ecf0b79449754da1d1ba925b1ff2)
- [packet_quality_bit_errors](../bluetooth_hci_model_reference/P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md#a16fb71660c4f4afb1c36765fdbd2a96a)
- [packet_rssi](../bluetooth_hci_model_reference/P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md#aa058afab8cba3f5ce572b8e7d29ef34d)
- [packet_antenna](../bluetooth_hci_model_reference/P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md#ad045baeaf6fbb75de002ffedc4b1a831)
- [bt_hci_le_cs_step_data_mode_1](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md)
- [packet_quality_aa_check](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#a8383926e95cd9d222b91704b2ca6883e)
- [packet_quality_bit_errors](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#a0cb4198466318a7a15cbbb172c582eeb)
- [packet_nadm](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#a4025cf2b229ada27e258d3d519a7b1dd)
- [packet_rssi](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#a1b9df39c01ab91ab225c809db5066f70)
- [toa_tod_initiator](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#a1365e601f422b98747f9909d3be56b60)
- [tod_toa_reflector](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#ab3425181b2a625fcfbbfd14477d717d1)
- [packet_antenna](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#afc8221a5cab14d3842590e6cac52da4d)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md)
- [packet_quality_aa_check](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#ad8f9ca9dda852b435848b988ad872797)
- [packet_quality_bit_errors](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a515fde1d568a19ccf6ebefe9052866a4)
- [packet_nadm](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a511b281fb1c16fd7d0eaf731906a4292)
- [packet_rssi](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a5ec9c30063c09285804973008533e5cb)
- [toa_tod_initiator](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a77bbcd9451360ad97813f9357e44766e)
- [tod_toa_reflector](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#ace3843bc24616950f04150b2f86abad4)
- [packet_antenna](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#abf20351ab0eaf3a7139a464f1d1a72b0)
- [packet_pct1](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a3f8ba85b776f732ebc1086a4317849a1)
- [packet_pct2](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a9f969aa6fc134a9e618d07f177d2b7fd)
- [bt_hci_le_cs_step_data_tone_info](../bluetooth_hci_model_reference/P322_bt_hci_le_cs_step_data_tone_info_结构体.md)
- [phase_correction_term](../bluetooth_hci_model_reference/P322_bt_hci_le_cs_step_data_tone_info_结构体.md#aeb76aeb54cb4e5613496431ec6d0093a)
- [quality_indicator](../bluetooth_hci_model_reference/P322_bt_hci_le_cs_step_data_tone_info_结构体.md#a4d31c0759c17789cb4b9bdc90a8870ca)
- [extension_indicator](../bluetooth_hci_model_reference/P322_bt_hci_le_cs_step_data_tone_info_结构体.md#a5f2e5e95b97d2be49a8ff1d9376892e8)
- [bt_hci_le_cs_step_data_mode_2](../bluetooth_hci_model_reference/P319_bt_hci_le_cs_step_data_mode_2_结构体.md)
- [antenna_permutation_index](../bluetooth_hci_model_reference/P319_bt_hci_le_cs_step_data_mode_2_结构体.md#a9feb2b07f8862aa24772a733f451f7a8)
- [tone_info](../bluetooth_hci_model_reference/P319_bt_hci_le_cs_step_data_mode_2_结构体.md#aef5699cb9bfc522a12be9a284392fd0e)
- [bt_hci_le_cs_step_data_mode_3](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md)
- [packet_quality_aa_check](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#ad4c30784cc2586b5b8dcfa22e7a1f8fb)
- [packet_quality_bit_errors](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a42b8bdf1fd492be1daded674e3d733d6)
- [packet_nadm](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a9b7373e7d3faa0cb5553d4f897c94ebc)
- [packet_rssi](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a60750ac38bf019a0c7a8656ca59fc402)
- [toa_tod_initiator](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a183f3ee64a4482c9d3e0f041151fdcf9)
- [tod_toa_reflector](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#aa0f1918115a6e550d6fab17529bbb4f2)
- [packet_antenna](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#ad20e9c1deba67aa5759881b52d13311d)
- [antenna_permutation_index](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a609102fc9d42fe73c09907f54526bd40)
- [tone_info](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a9ae78aa83a22f0618491871d55f2f0b9)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md)
- [packet_quality_aa_check](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#a657ec3570e3ad6b2ddab87bada231587)
- [packet_quality_bit_errors](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#af5d8a8559400b45066bdac86fbdac411)
- [packet_nadm](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#a9d2428083c401d931520addde0af54fd)
- [packet_rssi](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#adc4fe32bc6b7515e5bf1055f19f1a2bd)
- [toa_tod_initiator](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#ae2181a568ed6da32d3f60ba6d271c64f)
- [tod_toa_reflector](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#ada4d52f54f1efa804a812c65edd8f125)
- [packet_antenna](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#a9ce412ad8b18a9315b858cf1fe2a466a)
- [packet_pct1](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#aada8b3ff1bb0d0b9eccb846da173b3f4)
- [packet_pct2](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#afdebbafc06475dde12aaed73d2180f96)
- [antenna_permutation_index](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#ac4067e27caa12cf9f8c6525bf6a72973)
- [tone_info](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#aea13fc3e16092dcede9fb46ea719f21c)
- [bt_hci_evt_le_cs_subevent_result_step](../bluetooth_hci_model_reference/P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md)
- [step_mode](../bluetooth_hci_model_reference/P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md#a65f6ecf6355883df7924067edc277f35)
- [step_channel](../bluetooth_hci_model_reference/P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md#a1f074ff26f779292ea32bb405f37b877)
- [step_data_length](../bluetooth_hci_model_reference/P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md#a7fb65809d78fbf08528f177d98e72f6b)
- [step_data](../bluetooth_hci_model_reference/P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md#aebb0c47275e4cf92802314a82ffba820)
- [bt_hci_evt_le_cs_subevent_result](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md)
- [conn_handle](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a3b9c8392fa3aadc2e0673923e0346278)
- [config_id](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a2e8bdef7f85a4cefeaf625d0c3a4db03)
- [start_acl_conn_event_counter](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a0d6b2ca9f148173abb6207cf7c473c7f)
- [procedure_counter](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#ad08558fd68eb6c43d95a3f0f62bafff0)
- [frequency_compensation](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#aba480f7ad78069fd8b83493fac42244e)
- [reference_power_level](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a9a7260f63122a94cf7eb6ddc3344f742)
- [procedure_done_status](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a27a2848009838977f26df75bfc9bc3c3)
- [subevent_done_status](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#aeda28dfb30c51ce2955e1c313069c111)
- [procedure_abort_reason](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#ab81c9c55697b2f2c92e3ea2073932ad1)
- [subevent_abort_reason](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#acf6f9c4e6fa5897be872d9953993517b)
- [num_antenna_paths](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a9931d5818b801a9c36853f88b259c25e)
- [num_steps_reported](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#af8c827d508614f553b9f503d0394411b)
- [steps](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a43b46a37648b9fde72634dd7dd6a68e6)
- [bt_hci_evt_le_cs_subevent_result_continue](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md)
- [conn_handle](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a4126bebec093f6f4d1a22b43abec6b1c)
- [config_id](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#adefb9ad1f998460a6d235ebd39bbfe4a)
- [procedure_done_status](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a3e5b1e8a247fff36c06447c9ff7c3bb8)
- [subevent_done_status](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a49cf181c8518fb3015a0c54f7558aa8c)
- [procedure_abort_reason](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a3c7ac056a5898710ffbc0776ef551b4b)
- [subevent_abort_reason](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a1801aeaac839831198e17b7d96a5532a)
- [num_antenna_paths](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a2f8e1f634e28100815c881a463b51f2c)
- [num_steps_reported](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#af127774b52c4e088f628999136b6cd7c)
- [steps](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#abbddd0e27178e49abe6eef62bc094a16)
- [bt_hci_evt_le_cs_test_end_complete](../bluetooth_hci_model_reference/P249_bt_hci_evt_le_cs_test_end_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P249_bt_hci_evt_le_cs_test_end_complete_结构体.md#ae083dabff641736ed9a23ffc5a36a737)
- [bt_hci_evt_le_cs_procedure_enable_complete](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a5822ff654eee794442a05033e0f10fae)
- [handle](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#adcf8e32c2346073e0fbe273d261f6741)
- [config_id](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a17b62e13cda5f47dee2e8873686b978e)
- [state](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a7ff8f1e713d9b835f3a4e0e79cb1b3d1)
- [tone_antenna_config_selection](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a60a9e00cba665d73e65d0ee5b0d9efbc)
- [selected_tx_power](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#afd760c9b6809e6764a652ecb3ee4c2b5)
- [subevent_len](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#af5959274cb88a8e4fdf09e8dd756f31c)
- [subevents_per_event](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#aacc14948a9e6c384ec94051fb4323599)
- [subevent_interval](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a8f5485967662dbd1676d8edd6345fd13)
- [event_interval](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a688bfcb6781b2e3480f021c66a3109fe)
- [procedure_interval](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#ad7c21907a38747ec405c992ef14e8dd7)
- [procedure_count](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#ac8489dc8ff5f9bf052a7c1a67a544106)
- [max_procedure_len](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a7a38c8ced8720a428df42e821ec7e9e6)
- [bt_hci_evt_le_frame_space_update_complete](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md)
- [status](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#a2ec660b66b28fe0ab69b9db5681a5b17)
- [handle](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#a8da9f4e322bd41f5870ea5cec0092584)
- [initiator](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#adb081f887bc36892fc98fe78d170d93d)
- [frame_space](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#a1b306ba860123344436f85914455d784)
- [phys](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#a66d0db4fa276b0a839ce97b0c6868ae4)
- [spacing_types](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#af39f49f398848cfddda3edf70432a5fd)
- [bt_hci_evt_le_conn_rate_change](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md)
- [status](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a8ad1a15c8b26be65d92944b4fc3c0ae1)
- [handle](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a5b3947e67027b5425c21a0d509e19dc5)
- [conn_interval](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a31deb63251c897f7627b67c7cad2521f)
- [subrate_factor](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a29d6bdbf04cb6bc68a84f3fafaf66a1f)
- [peripheral_latency](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a67429e04fe601f367deeb5637d7d89c9)
- [continuation_number](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a10671dd6e9b30b112e5841c482ee3067)
- [supervision_timeout](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a3028aa8284c2f656f71d4b25da862cc9)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [bt_hci_acl_hdr::handle](../bluetooth_hci_model_reference/P001_bt_hci_acl_hdr_结构体.md#a8c88ef62a848699e06c49f97e1169363)
- [bt_hci_acl_hdr::len](../bluetooth_hci_model_reference/P001_bt_hci_acl_hdr_结构体.md#af55b9c9256f35ada5786e9e5dd1d01bf)
- [bt_hci_cis_params_test::cis_id](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#a0a215b4dffac2aae4ae4310c54de073e)
- [bt_hci_cis_params_test::c_sdu](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#a98a120efb1495dd90858bef45eb95891)
- [bt_hci_cis_params_test::c_phy](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#aa7ba56fb91718d43ca30ff643757e08e)
- [bt_hci_cis_params_test::p_phy](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#ab636126046023a329451673c57b4ce96)
- [bt_hci_cis_params_test::p_pdu](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#abce4bd6045642b4d29668865655f1548)
- [bt_hci_cis_params_test::p_bn](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#ac66b7183d8148250246f17a157dc3d29)
- [bt_hci_cis_params_test::nse](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#ad0cc6d393a536cb3cd83d456b950fc52)
- [bt_hci_cis_params_test::c_pdu](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#adc092a44b58bcc78f3dfe88528ca724c)
- [bt_hci_cis_params_test::c_bn](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#adf5dda2be46f3c2c1a1fe398672416ff)
- [bt_hci_cis_params_test::p_sdu](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md#aefeca493efe0141590570e8a44bb8f8d)
- [bt_hci_cis_params::p_phy](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#a18bc8e4b531d9fd16f18e10a0d931f6c)
- [bt_hci_cis_params::c_phy](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#a5a5fcd9276d912446fe84d875ae74c2f)
- [bt_hci_cis_params::cis_id](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#a6dcfca11d7f827b1b7a62b507620d4de)
- [bt_hci_cis_params::c_sdu](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#a8a85b914ba5585c6b362da3deb8d42d9)
- [bt_hci_cis_params::c_rtn](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#aa7fa628692f959db63788c6580cc5c66)
- [bt_hci_cis_params::p_rtn](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#ad55e197ccb70c83fcd4c1c6ba485f468)
- [bt_hci_cis_params::p_sdu](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md#ae2bffbaf0c4dde9144a7887177b3ffdb)
- [bt_hci_cis::acl_handle](../bluetooth_hci_model_reference/P002_bt_hci_cis_结构体.md#a754c3c75c0ad13a11d89fa3347112e2c)
- [bt_hci_cis::cis_handle](../bluetooth_hci_model_reference/P002_bt_hci_cis_结构体.md#a84165d526c10a91fa42d306276d97c74)
- [bt_hci_cmd_hdr::opcode](../bluetooth_hci_model_reference/P005_bt_hci_cmd_hdr_结构体.md#a09c63aab094ca0f39bab44708fdb83e4)
- [bt_hci_cmd_hdr::param_len](../bluetooth_hci_model_reference/P005_bt_hci_cmd_hdr_结构体.md#afe2a97da8b473cafd3cc4e5e52dadf93)
- [bt_hci_codec_capability_info::length](../bluetooth_hci_model_reference/P006_bt_hci_codec_capability_info_结构体.md#a24516347742a8fd9f3386d78b66a4e81)
- [bt_hci_codec_capability_info::data](../bluetooth_hci_model_reference/P006_bt_hci_codec_capability_info_结构体.md#ac53f02f2abdb832ed82da35a36abc323)
- [bt_hci_cp_accept_conn_req::role](../bluetooth_hci_model_reference/P007_bt_hci_cp_accept_conn_req_结构体.md#a95e445018d1b9da5a914f0845bb9dbad)
- [bt_hci_cp_accept_conn_req::bdaddr](../bluetooth_hci_model_reference/P007_bt_hci_cp_accept_conn_req_结构体.md#aa2954d98fdd42882cf7095e4ce7a3dc5)
- [bt_hci_cp_accept_sync_conn_req::max_latency](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#a4ba6dffd840ef868524b490d227fd085)
- [bt_hci_cp_accept_sync_conn_req::tx_bandwidth](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#a53fe4c6d61dbb99f99aa445b2c47a8ef)
- [bt_hci_cp_accept_sync_conn_req::bdaddr](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#a6a5a56d3a9d1a6d1064e7bd4c9fd333e)
- [bt_hci_cp_accept_sync_conn_req::pkt_type](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#ab5d9c27ebdf45fb54b0c6330b5b095be)
- [bt_hci_cp_accept_sync_conn_req::retrans_effort](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#ab5ece67c5a1e62fc4124556eef743c26)
- [bt_hci_cp_accept_sync_conn_req::rx_bandwidth](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#aceda6dbd3e221ad080850e9635886a86)
- [bt_hci_cp_accept_sync_conn_req::content_format](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md#adba31b588bf12e852cc43b85c006aaa3)
- [bt_hci_cp_auth_requested::handle](../bluetooth_hci_model_reference/P009_bt_hci_cp_auth_requested_结构体.md#a079490f8f8569e281ce16f13847cbf33)
- [bt_hci_cp_change_conn_packet_type::handle](../bluetooth_hci_model_reference/P010_bt_hci_cp_change_conn_packet_type_结构体.md#a082e5dae5f08a332cf6a1dd23917d87f)
- [bt_hci_cp_change_conn_packet_type::packet_type](../bluetooth_hci_model_reference/P010_bt_hci_cp_change_conn_packet_type_结构体.md#a0b825740b5ff47db5bfaaea7950e7d53)
- [bt_hci_cp_codec_id::vs_codec_id](../bluetooth_hci_model_reference/P011_bt_hci_cp_codec_id_结构体.md#a70296440c202544af11db2dc8e80fc5b)
- [bt_hci_cp_codec_id::company_id](../bluetooth_hci_model_reference/P011_bt_hci_cp_codec_id_结构体.md#a98fd438270a64d843fa27c7c196645df)
- [bt_hci_cp_codec_id::coding_format](../bluetooth_hci_model_reference/P011_bt_hci_cp_codec_id_结构体.md#aec80c74b12edb9c63330cc5a404eed5d)
- [bt_hci_cp_configure_data_path::vs_config_len](../bluetooth_hci_model_reference/P012_bt_hci_cp_configure_data_path_结构体.md#a2573fe029e1774bf5fa7e8cffff08cec)
- [bt_hci_cp_configure_data_path::data_path_dir](../bluetooth_hci_model_reference/P012_bt_hci_cp_configure_data_path_结构体.md#a528ba2bd5a220d1b7db064f8b51a8718)
- [bt_hci_cp_configure_data_path::data_path_id](../bluetooth_hci_model_reference/P012_bt_hci_cp_configure_data_path_结构体.md#a92967e6b5258b2acd6d82bfbfb8b7940)
- [bt_hci_cp_configure_data_path::vs_config](../bluetooth_hci_model_reference/P012_bt_hci_cp_configure_data_path_结构体.md#aa79c4aa6603b09f49a8c7f216f135e6e)
- [bt_hci_cp_connect_cancel::bdaddr](../bluetooth_hci_model_reference/P014_bt_hci_cp_connect_cancel_结构体.md#a2adaf1b708689525e44e9a9572f5f357)
- [bt_hci_cp_connect::pscan_rep_mode](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#a35b0e1f73f696aae2ca519e16d7bb668)
- [bt_hci_cp_connect::packet_type](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#a652a4e01641893a8588110dc505ceea0)
- [bt_hci_cp_connect::bdaddr](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#a6f0753aad19d4c9591fa74152d151aa9)
- [bt_hci_cp_connect::allow_role_switch](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#a7a3d772bfd4c83236f9f1ad657e33f17)
- [bt_hci_cp_connect::clock_offset](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#ac379ec381ad4cf6760750203924e5dda)
- [bt_hci_cp_connect::reserved](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md#aef01fcac1b9792353bd8095e6911d6c3)
- [bt_hci_cp_disconnect::reason](../bluetooth_hci_model_reference/P015_bt_hci_cp_disconnect_结构体.md#a8e10edb1e700c1ef38f39bf20b9b374f)
- [bt_hci_cp_disconnect::handle](../bluetooth_hci_model_reference/P015_bt_hci_cp_disconnect_结构体.md#a9cb5bcd135082c37a19cce57ffa123ff)
- [bt_hci_cp_exit_sniff_mode::handle](../bluetooth_hci_model_reference/P016_bt_hci_cp_exit_sniff_mode_结构体.md#a706cc1a951f21889a28e0b555587bb98)
- [bt_hci_cp_host_buffer_size::acl_mtu](../bluetooth_hci_model_reference/P017_bt_hci_cp_host_buffer_size_结构体.md#a07039a81ba81c700a26009ea407744b6)
- [bt_hci_cp_host_buffer_size::sco_mtu](../bluetooth_hci_model_reference/P017_bt_hci_cp_host_buffer_size_结构体.md#a1b1d8c7f60ecbb13699b815bc8fca550)
- [bt_hci_cp_host_buffer_size::acl_pkts](../bluetooth_hci_model_reference/P017_bt_hci_cp_host_buffer_size_结构体.md#a8240837fecc7c50461724b697f0eda47)
- [bt_hci_cp_host_buffer_size::sco_pkts](../bluetooth_hci_model_reference/P017_bt_hci_cp_host_buffer_size_结构体.md#a943252480194e1a8608951be08b6b91c)
- [bt_hci_cp_host_num_completed_packets::h](../bluetooth_hci_model_reference/P018_bt_hci_cp_host_num_completed_packets_结构体.md#a127f146b4967de49bc74b90ce1643eb7)
- [bt_hci_cp_host_num_completed_packets::num_handles](../bluetooth_hci_model_reference/P018_bt_hci_cp_host_num_completed_packets_结构体.md#a43a42e52757de9ec307e8a828dff416f)
- [bt_hci_cp_io_capability_neg_reply::reason](../bluetooth_hci_model_reference/P019_bt_hci_cp_io_capability_neg_reply_结构体.md#a82c54e5ad7fd4a6d81952832ae4de373)
- [bt_hci_cp_io_capability_neg_reply::bdaddr](../bluetooth_hci_model_reference/P019_bt_hci_cp_io_capability_neg_reply_结构体.md#a8dba05bc84de2573eaea43ea9e428015)
- [bt_hci_cp_io_capability_reply::capability](../bluetooth_hci_model_reference/P020_bt_hci_cp_io_capability_reply_结构体.md#a0995c81ba1f653c59bda9a444fb17915)
- [bt_hci_cp_io_capability_reply::authentication](../bluetooth_hci_model_reference/P020_bt_hci_cp_io_capability_reply_结构体.md#a8983418dca3a7725f3b113a4d0ee177e)
- [bt_hci_cp_io_capability_reply::oob_data](../bluetooth_hci_model_reference/P020_bt_hci_cp_io_capability_reply_结构体.md#ac002ea0b276200a15d603b5ac83666e5)
- [bt_hci_cp_io_capability_reply::bdaddr](../bluetooth_hci_model_reference/P020_bt_hci_cp_io_capability_reply_结构体.md#afbe2bc0c1dcc0791a98068b052aea1f2)
- [bt_hci_cp_le_accept_cis::handle](../bluetooth_hci_model_reference/P021_bt_hci_cp_le_accept_cis_结构体.md#aec6a6c80403d5827df10cd8722bc12e4)
- [bt_hci_cp_le_add_dev_to_fal::addr](../bluetooth_hci_model_reference/P022_bt_hci_cp_le_add_dev_to_fal_结构体.md#a11ec9f3cd9b80f34094e70d8eeb13be3)
- [bt_hci_cp_le_add_dev_to_per_adv_list::sid](../bluetooth_hci_model_reference/P023_bt_hci_cp_le_add_dev_to_per_adv_list_结构体.md#a97d9c5dd0cc4b3ab7f6ebfec206b7407)
- [bt_hci_cp_le_add_dev_to_per_adv_list::addr](../bluetooth_hci_model_reference/P023_bt_hci_cp_le_add_dev_to_per_adv_list_结构体.md#ad93d72bfa7e4123ee9728f6bf73b69df)
- [bt_hci_cp_le_add_dev_to_rl::peer_id_addr](../bluetooth_hci_model_reference/P024_bt_hci_cp_le_add_dev_to_rl_结构体.md#a3daf2041f04381a56c2cbcd4bb33f4c0)
- [bt_hci_cp_le_add_dev_to_rl::local_irk](../bluetooth_hci_model_reference/P024_bt_hci_cp_le_add_dev_to_rl_结构体.md#ab5caa38e6eeab09b4a69084b1890317b)
- [bt_hci_cp_le_add_dev_to_rl::peer_irk](../bluetooth_hci_model_reference/P024_bt_hci_cp_le_add_dev_to_rl_结构体.md#aedc27c868a7a4cbd3c175f67db4e3242)
- [bt_hci_cp_le_big_create_sync::bcode](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a053475c3af12e6e37dc4befcf634d68f)
- [bt_hci_cp_le_big_create_sync::mse](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a37050e3eb914ff06495695d44c3fdb50)
- [bt_hci_cp_le_big_create_sync::encryption](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a482edf3326e2dd720b14a03609c1256a)
- [bt_hci_cp_le_big_create_sync::sync_timeout](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a55e83bc3722ce2dbf943879a80ef2872)
- [bt_hci_cp_le_big_create_sync::big_handle](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a6692dae077ce1ce4f31bc94b9d391afd)
- [bt_hci_cp_le_big_create_sync::bis](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a6d1050c2a0522be215d82d3874fed4b6)
- [bt_hci_cp_le_big_create_sync::sync_handle](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a70b031f24cdf231e5c168b155517eae0)
- [bt_hci_cp_le_big_create_sync::num_bis](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md#a7efae2c8dc46d13fb2abca677ac152b0)
- [bt_hci_cp_le_big_terminate_sync::big_handle](../bluetooth_hci_model_reference/P026_bt_hci_cp_le_big_terminate_sync_结构体.md#ad7e4de2a9a3222c1bb8fa048cacd06fa)
- [bt_hci_cp_le_conn_cte_req_enable::requested_cte_length](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md#a4d4e41bbe95457ce5e8ad68ffeb85200)
- [bt_hci_cp_le_conn_cte_req_enable::requested_cte_type](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md#a5a7443a86e770de4bf7292d813e966e7)
- [bt_hci_cp_le_conn_cte_req_enable::cte_request_interval](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md#a956a1a8794b75e962d03cdcf81847cfc)
- [bt_hci_cp_le_conn_cte_req_enable::enable](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md#aaf38e3d5664d81ae7ac8d3b1bb03c646)
- [bt_hci_cp_le_conn_cte_req_enable::handle](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md#af340b3b97f9fb12c24baa38415620b44)
- [bt_hci_cp_le_conn_cte_rsp_enable::handle](../bluetooth_hci_model_reference/P028_bt_hci_cp_le_conn_cte_rsp_enable_结构体.md#a9d78072143513020620e02a744d4fa9b)
- [bt_hci_cp_le_conn_cte_rsp_enable::enable](../bluetooth_hci_model_reference/P028_bt_hci_cp_le_conn_cte_rsp_enable_结构体.md#ae5eaaae211732d772ea53f3936ab32d2)
- [bt_hci_cp_le_conn_param_req_neg_reply::handle](../bluetooth_hci_model_reference/P029_bt_hci_cp_le_conn_param_req_neg_reply_结构体.md#a0040e4a50c5c5479b539eb0bafb7b305)
- [bt_hci_cp_le_conn_param_req_neg_reply::reason](../bluetooth_hci_model_reference/P029_bt_hci_cp_le_conn_param_req_neg_reply_结构体.md#a8c283ac844805224b1ffeb9801e8b14b)
- [bt_hci_cp_le_conn_param_req_reply::interval_min](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#a10547c7d4836980947d17bbde0d75a51)
- [bt_hci_cp_le_conn_param_req_reply::min_ce_len](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#a512d605d5c4aacf81b78794fcf260abf)
- [bt_hci_cp_le_conn_param_req_reply::latency](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#a8c76816cc230387c249ab8e05c402964)
- [bt_hci_cp_le_conn_param_req_reply::max_ce_len](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#a932e6a3a45ec0409656325f7246d5d7e)
- [bt_hci_cp_le_conn_param_req_reply::handle](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#aa3b938afe13d4e05806fb6cdfab5cb14)
- [bt_hci_cp_le_conn_param_req_reply::interval_max](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#aed58f9aa722a284ae39df842394c06cf)
- [bt_hci_cp_le_conn_param_req_reply::timeout](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md#af25a3f226ceccbe19e7f1482ed5f141e)
- [bt_hci_cp_le_create_big_test::max_pdu](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a2652e0f340f13635a5da6335ec43e801)
- [bt_hci_cp_le_create_big_test::pto](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a2f2eaa258463dd51a9f6042e75ecfec6)
- [bt_hci_cp_le_create_big_test::sdu_interval](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a331b1a8ef66804cf20d6681e1bc5aefb)
- [bt_hci_cp_le_create_big_test::bcode](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a333319a03d2087067247c4f5e595b4e5)
- [bt_hci_cp_le_create_big_test::nse](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a402c19da1ecf273bc942ecc560730567)
- [bt_hci_cp_le_create_big_test::packing](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a49822f8e1617e30aab9b0d7d790697a3)
- [bt_hci_cp_le_create_big_test::encryption](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a50c4308abda01581b436b7867304e982)
- [bt_hci_cp_le_create_big_test::iso_interval](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a6475ae77af80e89bb65596bc6f907a58)
- [bt_hci_cp_le_create_big_test::irc](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a66ce7ba0498053a588de9097cbbc0891)
- [bt_hci_cp_le_create_big_test::num_bis](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a6ce270f0afd185c44fa5a2c67a7783fb)
- [bt_hci_cp_le_create_big_test::phy](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a731ca2f90c17a4f3f868660e51649ce6)
- [bt_hci_cp_le_create_big_test::bn](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a734174187486ac760b8bf0e566166842)
- [bt_hci_cp_le_create_big_test::max_sdu](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#a7ebbc81306109e035f89154738900395)
- [bt_hci_cp_le_create_big_test::big_handle](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#ac202f5cee0c1d0456b200606860fd5ab)
- [bt_hci_cp_le_create_big_test::framing](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#acc5b2c30db0c7642d12019f8241dab26)
- [bt_hci_cp_le_create_big_test::adv_handle](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md#aece09ae6264e0cc1a5548f1603a3f61a)
- [bt_hci_cp_le_create_big::max_sdu](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a06fd74e9a5f172060835524da5851c71)
- [bt_hci_cp_le_create_big::bcode](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a0b4b2d77cd0f579aab190336b14597c5)
- [bt_hci_cp_le_create_big::max_latency](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a15018e5ebc124bbe90644b38fe3e7e76)
- [bt_hci_cp_le_create_big::rtn](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a1cb0dd106bf4a1a0c473333d089c95e7)
- [bt_hci_cp_le_create_big::sdu_interval](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a2960a9891b827529c9fa1b68a747e2d5)
- [bt_hci_cp_le_create_big::framing](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a330916d60c05ec2ef7a71933b62c203a)
- [bt_hci_cp_le_create_big::encryption](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a490bd68d137f8cf60ea2ccd5ea4495e9)
- [bt_hci_cp_le_create_big::phy](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#a56cb773a03e4927c3b6bf4d2a6ed6ed9)
- [bt_hci_cp_le_create_big::adv_handle](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#aa686eec31ca4c831262dd34d41f9a1fb)
- [bt_hci_cp_le_create_big::packing](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#ac027390db21320fb9d1002161c4c2f67)
- [bt_hci_cp_le_create_big::num_bis](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#ad8491c970417e63c6a98c12278a89c86)
- [bt_hci_cp_le_create_big::big_handle](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md#af5412e4a69c05a09b2e818322636a98a)
- [bt_hci_cp_le_create_cis::cis](../bluetooth_hci_model_reference/P033_bt_hci_cp_le_create_cis_结构体.md#a5a323d09df7813fc9b834cc1d205d101)
- [bt_hci_cp_le_create_cis::num_cis](../bluetooth_hci_model_reference/P033_bt_hci_cp_le_create_cis_结构体.md#acd348a7d68947af8e7119b2e1a864481)
- [bt_hci_cp_le_create_conn::scan_interval](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a1a830a0f6cd961d534c338031b2b691b)
- [bt_hci_cp_le_create_conn::filter_policy](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a2ca5063f5082a0f330676e56253a21c7)
- [bt_hci_cp_le_create_conn::min_ce_len](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a476501ccd209f3a52082decf906ca8f0)
- [bt_hci_cp_le_create_conn::conn_latency](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a5a9d5c1d44adac876680a517b1fad63f)
- [bt_hci_cp_le_create_conn::max_ce_len](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a5b329aa8b48e03998e969b2436d35ab5)
- [bt_hci_cp_le_create_conn::own_addr_type](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a63c7f9e89528105e484a60e41eeb8a30)
- [bt_hci_cp_le_create_conn::conn_interval_min](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#a988cf154b0df1ff9af8d34ce73a920dd)
- [bt_hci_cp_le_create_conn::conn_interval_max](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#aa009d54866d9c675c2785412bdbd182f)
- [bt_hci_cp_le_create_conn::peer_addr](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#aa51da7602eb2b44528964c8b706bb043)
- [bt_hci_cp_le_create_conn::scan_window](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#abf61e67f5e20adc44b5b9314ed43bccc)
- [bt_hci_cp_le_create_conn::supervision_timeout](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md#ae8e0ad70a3b23ac035c237db0d57adc4)
- [bt_hci_cp_le_cs_create_config::ch3c_jump](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a0223c41abc034d515421fad8c3123387)
- [bt_hci_cp_le_cs_create_config::channel_selection_type](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a2c8be699bfd8eaaababd6d0de0b13e18)
- [bt_hci_cp_le_cs_create_config::sub_mode_type](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a34fa54e8bbd641bb0901b0b057134ffb)
- [bt_hci_cp_le_cs_create_config::handle](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a3742081b071b992176b725448cc6ab29)
- [bt_hci_cp_le_cs_create_config::role](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a5a17d6c72daaefcb55fdfa24194cc886)
- [bt_hci_cp_le_cs_create_config::cs_enhancements_1](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a6088c8413ca175c0231fc53bfb168b29)
- [bt_hci_cp_le_cs_create_config::rtt_type](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a709938176023c5482c91af8995001782)
- [bt_hci_cp_le_cs_create_config::main_mode_type](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a74c5fdfbc97b112c35ee318aa2b9b463)
- [bt_hci_cp_le_cs_create_config::channel_map_repetition](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a8182f4becdef488b84f12fe7e4274193)
- [bt_hci_cp_le_cs_create_config::mode_0_steps](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a909e409d55ac539a119e932899a97204)
- [bt_hci_cp_le_cs_create_config::create_context](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#a9dc7a6b577c33583b7ca7548e2b555ac)
- [bt_hci_cp_le_cs_create_config::max_main_mode_steps](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#aa13e091f99114bb5217489757c1522bd)
- [bt_hci_cp_le_cs_create_config::channel_map](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#abab4907ec883430044bb9f9d6cf9f25d)
- [bt_hci_cp_le_cs_create_config::cs_sync_phy](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#ac6c9c568918c9ef9aa4f2038a4922020)
- [bt_hci_cp_le_cs_create_config::main_mode_repetition](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#acd11430a6c94b0f0c34e2788a2326a40)
- [bt_hci_cp_le_cs_create_config::ch3c_shape](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#addaa3592a97bda96a4aba17e809e4018)
- [bt_hci_cp_le_cs_create_config::config_id](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#ae833b5f02f878f54dca1a25753eca1f3)
- [bt_hci_cp_le_cs_create_config::min_main_mode_steps](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md#aeb26115c8b500829ef6bc238aa3a495f)
- [bt_hci_cp_le_cs_remove_config::handle](../bluetooth_hci_model_reference/P036_bt_hci_cp_le_cs_remove_config_结构体.md#a4591af2e952f514b185db12c5f1158d5)
- [bt_hci_cp_le_cs_remove_config::config_id](../bluetooth_hci_model_reference/P036_bt_hci_cp_le_cs_remove_config_结构体.md#a9be71a1360f1ed14e6a7e205f5704e39)
- [bt_hci_cp_le_cs_set_default_settings::role_enable](../bluetooth_hci_model_reference/P037_bt_hci_cp_le_cs_set_default_settings_结构体.md#a04aea510e26136f874ccfbabbbd080bb)
- [bt_hci_cp_le_cs_set_default_settings::handle](../bluetooth_hci_model_reference/P037_bt_hci_cp_le_cs_set_default_settings_结构体.md#a096c3238ccc6624bae89d5a45dd95600)
- [bt_hci_cp_le_cs_set_default_settings::max_tx_power](../bluetooth_hci_model_reference/P037_bt_hci_cp_le_cs_set_default_settings_结构体.md#a333341ec01554ab90fc5e340dbfb5130)
- [bt_hci_cp_le_cs_set_default_settings::cs_sync_antenna_selection](../bluetooth_hci_model_reference/P037_bt_hci_cp_le_cs_set_default_settings_结构体.md#aa001c88ab42250c2cfd604af11e0ae27)
- [bt_hci_cp_le_default_past_param::timeout](../bluetooth_hci_model_reference/P038_bt_hci_cp_le_default_past_param_结构体.md#a159f5245f86b27198264bdcf394d719f)
- [bt_hci_cp_le_default_past_param::skip](../bluetooth_hci_model_reference/P038_bt_hci_cp_le_default_past_param_结构体.md#a214cb0597d0065bc2c056fe9c51a2220)
- [bt_hci_cp_le_default_past_param::mode](../bluetooth_hci_model_reference/P038_bt_hci_cp_le_default_past_param_结构体.md#a2ef92304264ad0bf1560accf306bb6d9)
- [bt_hci_cp_le_default_past_param::cte_type](../bluetooth_hci_model_reference/P038_bt_hci_cp_le_default_past_param_结构体.md#af18f679f5833c1d782b4e474af5d819c)
- [bt_hci_cp_le_encrypt::key](../bluetooth_hci_model_reference/P039_bt_hci_cp_le_encrypt_结构体.md#ab64f1bab8ad3a98217db96e6765a7d24)
- [bt_hci_cp_le_encrypt::plaintext](../bluetooth_hci_model_reference/P039_bt_hci_cp_le_encrypt_结构体.md#ad520b84e6e2a4e62f7fefba248c4cf10)
- [bt_hci_cp_le_enh_rx_test::rx_ch](../bluetooth_hci_model_reference/P040_bt_hci_cp_le_enh_rx_test_结构体.md#a3aa5b3947a4a0c87342695469bf056ec)
- [bt_hci_cp_le_enh_rx_test::mod_index](../bluetooth_hci_model_reference/P040_bt_hci_cp_le_enh_rx_test_结构体.md#a9151393e9f05a2ded484a1248a6edb88)
- [bt_hci_cp_le_enh_rx_test::phy](../bluetooth_hci_model_reference/P040_bt_hci_cp_le_enh_rx_test_结构体.md#aa2bf385221680b25ce184b4ea5d63cd4)
- [bt_hci_cp_le_enh_tx_test::tx_ch](../bluetooth_hci_model_reference/P041_bt_hci_cp_le_enh_tx_test_结构体.md#a0b7883b36d511c6da1bac543f1aae446)
- [bt_hci_cp_le_enh_tx_test::phy](../bluetooth_hci_model_reference/P041_bt_hci_cp_le_enh_tx_test_结构体.md#a718442db29c5ac455c3e2aac9844cdd0)
- [bt_hci_cp_le_enh_tx_test::pkt_payload](../bluetooth_hci_model_reference/P041_bt_hci_cp_le_enh_tx_test_结构体.md#a9ccb91be1554172d6c724e438508bfe5)
- [bt_hci_cp_le_enh_tx_test::test_data_len](../bluetooth_hci_model_reference/P041_bt_hci_cp_le_enh_tx_test_结构体.md#af1e27be0ad23887c0e71024739b00f8d)
- [bt_hci_cp_le_ext_create_conn_v2::own_addr_type](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#a05fd0089a0fd43f98042835231407a60)
- [bt_hci_cp_le_ext_create_conn_v2::peer_addr](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#a25466a04d224bdf495266b0064c424dd)
- [bt_hci_cp_le_ext_create_conn_v2::subevent](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#a536da199958b3b54469f5b4b029e1bac)
- [bt_hci_cp_le_ext_create_conn_v2::filter_policy](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#a66632dbac1605cff69e8da566e800347)
- [bt_hci_cp_le_ext_create_conn_v2::p](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#a8d606c5aa480f54c8da9f42a35ad513e)
- [bt_hci_cp_le_ext_create_conn_v2::adv_handle](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#addf1f80c4d3625e0c6d6e716f6e2e207)
- [bt_hci_cp_le_ext_create_conn_v2::phys](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md#ae2d3e3079a2848907224bb7ff0efc64b)
- [bt_hci_cp_le_ext_create_conn::filter_policy](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md#a0561b446effa3f735a405c0b307466bf)
- [bt_hci_cp_le_ext_create_conn::own_addr_type](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md#a12a99044f54e3d5dae30a64392444cbf)
- [bt_hci_cp_le_ext_create_conn::peer_addr](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md#a79bc55d9f5b1d719de4fb404db9008f3)
- [bt_hci_cp_le_ext_create_conn::p](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md#acdb436d6bf2864745ec579622ae0d532)
- [bt_hci_cp_le_ext_create_conn::phys](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md#ae859ff0da5e9cdc872943fd74774ef7e)
- [bt_hci_cp_le_frame_space_update::phys](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md#a10fb9f808dec017325861c983beb6bc9)
- [bt_hci_cp_le_frame_space_update::handle](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md#a6f8ae56a870c76d06e47aa15d22ca341)
- [bt_hci_cp_le_frame_space_update::frame_space_min](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md#a9854593fb39c71bfd5ee3da6f606dd7f)
- [bt_hci_cp_le_frame_space_update::frame_space_max](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md#ab449a9514f175ad73942582f07cdf792)
- [bt_hci_cp_le_frame_space_update::spacing_types](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md#acbb6b64086a5710449b4d4e228575325)
- [bt_hci_cp_le_generate_dhkey_v2::key_type](../bluetooth_hci_model_reference/P046_bt_hci_cp_le_generate_dhkey_v2_结构体.md#a3d47ad6d9df4d4023d2586c915ee8f2c)
- [bt_hci_cp_le_generate_dhkey_v2::key](../bluetooth_hci_model_reference/P046_bt_hci_cp_le_generate_dhkey_v2_结构体.md#acc3007adf301674b9e847297007c3cd1)
- [bt_hci_cp_le_generate_dhkey::key](../bluetooth_hci_model_reference/P045_bt_hci_cp_le_generate_dhkey_结构体.md#a0f67195504d877a1d11b7dfb77d09fcc)
- [bt_hci_cp_le_iso_receive_test::payload_type](../bluetooth_hci_model_reference/P047_bt_hci_cp_le_iso_receive_test_结构体.md#a9ce7e13fc1c1a7c87c01e1ecb24c5324)
- [bt_hci_cp_le_iso_receive_test::handle](../bluetooth_hci_model_reference/P047_bt_hci_cp_le_iso_receive_test_结构体.md#ac1272441f5c7b79e1ef5f644f099d19e)
- [bt_hci_cp_le_iso_test_end::handle](../bluetooth_hci_model_reference/P048_bt_hci_cp_le_iso_test_end_结构体.md#ab792ec021319024828bd7609e0fe7e96)
- [bt_hci_cp_le_iso_transmit_test::payload_type](../bluetooth_hci_model_reference/P049_bt_hci_cp_le_iso_transmit_test_结构体.md#a0653c77af723cc43a6b911816a8db437)
- [bt_hci_cp_le_iso_transmit_test::handle](../bluetooth_hci_model_reference/P049_bt_hci_cp_le_iso_transmit_test_结构体.md#adffb0d57afc090692ab36ebeaad21bbd)
- [bt_hci_cp_le_ltk_req_neg_reply::handle](../bluetooth_hci_model_reference/P050_bt_hci_cp_le_ltk_req_neg_reply_结构体.md#add8cc3b13432e233ceb5c2c11e0107c0)
- [bt_hci_cp_le_ltk_req_reply::ltk](../bluetooth_hci_model_reference/P051_bt_hci_cp_le_ltk_req_reply_结构体.md#a2d16b44af344237a890341943c4a6582)
- [bt_hci_cp_le_ltk_req_reply::handle](../bluetooth_hci_model_reference/P051_bt_hci_cp_le_ltk_req_reply_结构体.md#a46d87451acc1f1ce2ff35dd0dd238db3)
- [bt_hci_cp_le_past_param::cte_type](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md#a47c571ff27a59e0a7cbcb460303ee194)
- [bt_hci_cp_le_past_param::skip](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md#a622499d51e917f7828629de2291812e5)
- [bt_hci_cp_le_past_param::conn_handle](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md#a9c99cdd5ae5de58960677781c2287c4d)
- [bt_hci_cp_le_past_param::mode](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md#aa36345a550dfabeef48b430d1a1b0030)
- [bt_hci_cp_le_past_param::timeout](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md#aec9aa4ffe41c6b6f5cfcbc59eb57efca)
- [bt_hci_cp_le_per_adv_create_sync::addr](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#a3a0a0bc1bd5014f2ede0c4ef6cc30d24)
- [bt_hci_cp_le_per_adv_create_sync::sync_timeout](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#a46ea01403f68d42a315ff629374b2a95)
- [bt_hci_cp_le_per_adv_create_sync::skip](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#a554552684fa2a8d0022f9e31ade9c222)
- [bt_hci_cp_le_per_adv_create_sync::cte_type](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#a905b2a9166dd668df5929f0866769576)
- [bt_hci_cp_le_per_adv_create_sync::sid](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#ab5c4debe1babb98c60c1f1bfdf55359a)
- [bt_hci_cp_le_per_adv_create_sync::options](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md#aff300f352ec5f0fece90f88db811ef75)
- [bt_hci_cp_le_per_adv_set_info_transfer::conn_handle](../bluetooth_hci_model_reference/P054_bt_hci_cp_le_per_adv_set_info_transfer_结构体.md#a3b2f0c510ef9b385cb42bf9a194fa574)
- [bt_hci_cp_le_per_adv_set_info_transfer::service_data](../bluetooth_hci_model_reference/P054_bt_hci_cp_le_per_adv_set_info_transfer_结构体.md#a5f14c3265bffdf3e30a554a3686e9e0c)
- [bt_hci_cp_le_per_adv_set_info_transfer::adv_handle](../bluetooth_hci_model_reference/P054_bt_hci_cp_le_per_adv_set_info_transfer_结构体.md#a75b2c0fa1d50ef9d3761ac25f487750b)
- [bt_hci_cp_le_per_adv_sync_transfer::service_data](../bluetooth_hci_model_reference/P055_bt_hci_cp_le_per_adv_sync_transfer_结构体.md#a1327de0f9b2ebd1eaa97b51850087460)
- [bt_hci_cp_le_per_adv_sync_transfer::sync_handle](../bluetooth_hci_model_reference/P055_bt_hci_cp_le_per_adv_sync_transfer_结构体.md#a38537b7f01a93f7a3e8cfcb92098a172)
- [bt_hci_cp_le_per_adv_sync_transfer::conn_handle](../bluetooth_hci_model_reference/P055_bt_hci_cp_le_per_adv_sync_transfer_结构体.md#a991f77d6f2f0c301fe3322050b2d359f)
- [bt_hci_cp_le_per_adv_terminate_sync::handle](../bluetooth_hci_model_reference/P056_bt_hci_cp_le_per_adv_terminate_sync_结构体.md#a607fce7fd5c88e12f82e3d9731bd7f1a)
- [bt_hci_cp_le_procedure_enable::enable](../bluetooth_hci_model_reference/P057_bt_hci_cp_le_procedure_enable_结构体.md#a3a203b453bd913db8bec91be9310003a)
- [bt_hci_cp_le_procedure_enable::config_id](../bluetooth_hci_model_reference/P057_bt_hci_cp_le_procedure_enable_结构体.md#ae1dc5c808bed301ddee6e9dd624c00a5)
- [bt_hci_cp_le_procedure_enable::handle](../bluetooth_hci_model_reference/P057_bt_hci_cp_le_procedure_enable_结构体.md#af94d81f71c2fe587c848e34a430825bf)
- [bt_hci_cp_le_read_all_remote_features::handle](../bluetooth_hci_model_reference/P058_bt_hci_cp_le_read_all_remote_features_结构体.md#a2baf8df3a24b1b883768278459a156c7)
- [bt_hci_cp_le_read_all_remote_features::pages_requested](../bluetooth_hci_model_reference/P058_bt_hci_cp_le_read_all_remote_features_结构体.md#aa8cf7318871819cf425aa59ca15cc86d)
- [bt_hci_cp_le_read_chan_map::handle](../bluetooth_hci_model_reference/P059_bt_hci_cp_le_read_chan_map_结构体.md#abea9aec016a0433b3e4837d53d6b5d2b)
- [bt_hci_cp_le_read_iso_link_quality::handle](../bluetooth_hci_model_reference/P060_bt_hci_cp_le_read_iso_link_quality_结构体.md#a346fb3cf08203725d5943e42f03cb40d)
- [bt_hci_cp_le_read_iso_tx_sync::handle](../bluetooth_hci_model_reference/P061_bt_hci_cp_le_read_iso_tx_sync_结构体.md#a8edc469f73540d4300b1716c96e17c9f)
- [bt_hci_cp_le_read_local_rpa::peer_id_addr](../bluetooth_hci_model_reference/P062_bt_hci_cp_le_read_local_rpa_结构体.md#aa96cd60066003e4a7a1f482fb81557f8)
- [bt_hci_cp_le_read_peer_rpa::peer_id_addr](../bluetooth_hci_model_reference/P063_bt_hci_cp_le_read_peer_rpa_结构体.md#ab0c70a1dbe5152b1fc926b90ec3387b3)
- [bt_hci_cp_le_read_phy::handle](../bluetooth_hci_model_reference/P064_bt_hci_cp_le_read_phy_结构体.md#a7e0a4fa47b613c86364e6e94c2d0bef1)
- [bt_hci_cp_le_read_remote_fae_table::handle](../bluetooth_hci_model_reference/P065_bt_hci_cp_le_read_remote_fae_table_结构体.md#a10bdfc4808586f7cccf025c63a6e28a5)
- [bt_hci_cp_le_read_remote_features::handle](../bluetooth_hci_model_reference/P066_bt_hci_cp_le_read_remote_features_结构体.md#a843997555fd36f102c83a7d59f65eea9)
- [bt_hci_cp_le_read_remote_supported_capabilities::handle](../bluetooth_hci_model_reference/P067_bt_hci_cp_le_read_remote_supported_capabilities_结构体.md#ac6f083563e2c72d37cf4e9e8fa695733)
- [bt_hci_cp_le_read_test_counters::handle](../bluetooth_hci_model_reference/P068_bt_hci_cp_le_read_test_counters_结构体.md#a230d973c2db177c3595bb4808ebf5cd2)
- [bt_hci_cp_le_read_tx_power_level::phy](../bluetooth_hci_model_reference/P069_bt_hci_cp_le_read_tx_power_level_结构体.md#a4863396dfe4dca65aaef68293e29291b)
- [bt_hci_cp_le_read_tx_power_level::handle](../bluetooth_hci_model_reference/P069_bt_hci_cp_le_read_tx_power_level_结构体.md#af8c2d89b183d7bdc0f55a0bf783a373d)
- [bt_hci_cp_le_reject_cis::handle](../bluetooth_hci_model_reference/P070_bt_hci_cp_le_reject_cis_结构体.md#ad697d740bdf5a565090a548e7e8fd399)
- [bt_hci_cp_le_reject_cis::reason](../bluetooth_hci_model_reference/P070_bt_hci_cp_le_reject_cis_结构体.md#aec5bd3e4d27b6e3a2653112b36a3d128)
- [bt_hci_cp_le_rem_dev_from_fal::addr](../bluetooth_hci_model_reference/P071_bt_hci_cp_le_rem_dev_from_fal_结构体.md#afe6054303093cc930d1089ca6a16101c)
- [bt_hci_cp_le_rem_dev_from_per_adv_list::sid](../bluetooth_hci_model_reference/P072_bt_hci_cp_le_rem_dev_from_per_adv_list_结构体.md#a6629f3ececf586792a14f3c028cc8e8c)
- [bt_hci_cp_le_rem_dev_from_per_adv_list::addr](../bluetooth_hci_model_reference/P072_bt_hci_cp_le_rem_dev_from_per_adv_list_结构体.md#adc420288f6a79c1a92f57241d3da3d81)
- [bt_hci_cp_le_rem_dev_from_rl::peer_id_addr](../bluetooth_hci_model_reference/P073_bt_hci_cp_le_rem_dev_from_rl_结构体.md#aacb577a7ae13322145fccdffc3161541)
- [bt_hci_cp_le_remove_adv_set::handle](../bluetooth_hci_model_reference/P074_bt_hci_cp_le_remove_adv_set_结构体.md#ab33bf918b10d847bb8fb8ac2409780e6)
- [bt_hci_cp_le_remove_cig::cig_id](../bluetooth_hci_model_reference/P075_bt_hci_cp_le_remove_cig_结构体.md#addf395d945f14afbf2d39fa4d0d22f31)
- [bt_hci_cp_le_remove_iso_path::path_dir](../bluetooth_hci_model_reference/P076_bt_hci_cp_le_remove_iso_path_结构体.md#a46e4b28917ff963ff4b672749fde0971)
- [bt_hci_cp_le_remove_iso_path::handle](../bluetooth_hci_model_reference/P076_bt_hci_cp_le_remove_iso_path_结构体.md#ad0106791003f9d1173f2a9f102903c45)
- [bt_hci_cp_le_req_peer_sca::handle](../bluetooth_hci_model_reference/P077_bt_hci_cp_le_req_peer_sca_结构体.md#a39d65681da55b26f2900f06cde637d88)
- [bt_hci_cp_le_rx_test_v3::expected_cte_type](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#a55b5c4739e456167f17bf3899d096e61)
- [bt_hci_cp_le_rx_test_v3::slot_durations](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#a5cd5a44b0832b9f6e2198b9ad714b99b)
- [bt_hci_cp_le_rx_test_v3::mod_index](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#a7ffde9dc565194c0108177cf11b02b5b)
- [bt_hci_cp_le_rx_test_v3::ant_ids](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#aa6cd0835068f378949da182af13e2438)
- [bt_hci_cp_le_rx_test_v3::switch_pattern_len](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#ab0832e72ef90b1269928378638fcb194)
- [bt_hci_cp_le_rx_test_v3::rx_ch](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#abd33b70c948d4ee42d96d0d2e7f7cb1c)
- [bt_hci_cp_le_rx_test_v3::expected_cte_len](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#ad1a1082d27b8a10e25eebd347404637c)
- [bt_hci_cp_le_rx_test_v3::phy](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md#ad1c211c59cf34d76429d4d4548966630)
- [bt_hci_cp_le_rx_test::rx_ch](../bluetooth_hci_model_reference/P078_bt_hci_cp_le_rx_test_结构体.md#a11cb21a7625d9c097eba0a7b68e93f3f)
- [bt_hci_cp_le_security_enable::handle](../bluetooth_hci_model_reference/P080_bt_hci_cp_le_security_enable_结构体.md#a772d3744d43f0447187040f2c6f0ac6e)
- [bt_hci_cp_le_set_addr_res_enable::enable](../bluetooth_hci_model_reference/P081_bt_hci_cp_le_set_addr_res_enable_结构体.md#ad0548178cbc9bc2db54612a748a2bd65)
- [bt_hci_cp_le_set_adv_data::len](../bluetooth_hci_model_reference/P082_bt_hci_cp_le_set_adv_data_结构体.md#a664313db17c12adb0de14371e46d26a8)
- [bt_hci_cp_le_set_adv_data::data](../bluetooth_hci_model_reference/P082_bt_hci_cp_le_set_adv_data_结构体.md#a6fb8734ff5a9b77586b3e283b83985bb)
- [bt_hci_cp_le_set_adv_enable::enable](../bluetooth_hci_model_reference/P083_bt_hci_cp_le_set_adv_enable_结构体.md#a15e92d187d586fef560adf9c793f776a)
- [bt_hci_cp_le_set_adv_param::channel_map](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#a2269ae424e47adddce5aa5f2f5b84c89)
- [bt_hci_cp_le_set_adv_param::min_interval](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#a2476c2a1858eab7e9b1449c1901363c4)
- [bt_hci_cp_le_set_adv_param::filter_policy](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#a662c5ae81f25a897a8e597f7227a1e39)
- [bt_hci_cp_le_set_adv_param::type](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#a9b09964156846fd480911dcc2d996a98)
- [bt_hci_cp_le_set_adv_param::max_interval](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#ab42c6b8f482e782d09386a3a1758903d)
- [bt_hci_cp_le_set_adv_param::direct_addr](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#ac774ef72175e43b083d04ecac263941b)
- [bt_hci_cp_le_set_adv_param::own_addr_type](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md#ad8c74cac74254354b314f07df7df1bf0)
- [bt_hci_cp_le_set_adv_set_random_addr::bdaddr](../bluetooth_hci_model_reference/P085_bt_hci_cp_le_set_adv_set_random_addr_结构体.md#a2883e9bf7ef6a34712eda2594e23c146)
- [bt_hci_cp_le_set_adv_set_random_addr::handle](../bluetooth_hci_model_reference/P085_bt_hci_cp_le_set_adv_set_random_addr_结构体.md#aafa39422a16cc4ff11c8073e9c0aab71)
- [bt_hci_cp_le_set_cig_params_test::p_interval](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a0cf0f3f7c10b29d74ab64aa30a4969de)
- [bt_hci_cp_le_set_cig_params_test::cig_id](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a161ae960cbd4f7833815285d04f87e46)
- [bt_hci_cp_le_set_cig_params_test::sca](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a1d060539ff26677c1326a6ed3394fb6e)
- [bt_hci_cp_le_set_cig_params_test::c_ft](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a1eae50a97188304852589fd95e994150)
- [bt_hci_cp_le_set_cig_params_test::framing](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a2cb6745b8f908cd2e7d5f12a092c3b69)
- [bt_hci_cp_le_set_cig_params_test::num_cis](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a50c345ef03c669f476e143728f42cd6d)
- [bt_hci_cp_le_set_cig_params_test::cis](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a5e07eb0d7d13e57be457d1b77a5dba12)
- [bt_hci_cp_le_set_cig_params_test::packing](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#a7275312e8b1c8ebc2af7992f765b392c)
- [bt_hci_cp_le_set_cig_params_test::c_interval](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#aa392cbac058beefd0e410fcc9821a0c3)
- [bt_hci_cp_le_set_cig_params_test::iso_interval](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#aa77765d90fde67c52e4f2d483f0a3ee0)
- [bt_hci_cp_le_set_cig_params_test::p_ft](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md#af2ed1bf1a6beaff884c3ce3faf26bfb2)
- [bt_hci_cp_le_set_cig_params::c_interval](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a14f5c0cf7f99ab406714501038048035)
- [bt_hci_cp_le_set_cig_params::sca](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a46a657cdfbc7a49e6761d9f18d980c2a)
- [bt_hci_cp_le_set_cig_params::p_interval](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a50a260a15f3a0ceae716da6c04c5b768)
- [bt_hci_cp_le_set_cig_params::packing](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a79fc069492741f14f348650abef4c66b)
- [bt_hci_cp_le_set_cig_params::cig_id](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a7dbf75c6ed92a053c4ec0d8f7268c92e)
- [bt_hci_cp_le_set_cig_params::p_latency](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a810822396b97d54988ec57561b4ee7d5)
- [bt_hci_cp_le_set_cig_params::framing](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#a867bf5ddbcadd27dbec2c3059d67d6d6)
- [bt_hci_cp_le_set_cig_params::cis](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#ac922e59065920421f40468754d2ba5a2)
- [bt_hci_cp_le_set_cig_params::num_cis](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#adf468a8a195447a7bbed4dcd53d287f6)
- [bt_hci_cp_le_set_cig_params::c_latency](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md#afec8ebd17cc6ca5b3d13ef54f406df62)
- [bt_hci_cp_le_set_cl_cte_sampling_enable::max_sampled_cte](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#a38e770b3e5f9d7d63a564dfa7c80451f)
- [bt_hci_cp_le_set_cl_cte_sampling_enable::switch_pattern_len](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#a4f52142ef1d2365859189b7a2abe050b)
- [bt_hci_cp_le_set_cl_cte_sampling_enable::ant_ids](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#a67bb2dbfe1707f76a5e211e007459c22)
- [bt_hci_cp_le_set_cl_cte_sampling_enable::sync_handle](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#a91d3458e2049ab434e220403b7ba235d)
- [bt_hci_cp_le_set_cl_cte_sampling_enable::slot_durations](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#aaaed0fc39158c653041fd760a00cecec)
- [bt_hci_cp_le_set_cl_cte_sampling_enable::sampling_enable](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md#aca9e1316c716525f00308f64b8c6cec4)
- [bt_hci_cp_le_set_cl_cte_tx_enable::cte_enable](../bluetooth_hci_model_reference/P089_bt_hci_cp_le_set_cl_cte_tx_enable_结构体.md#a3530dae940caefeafb9de4ac761ee080)
- [bt_hci_cp_le_set_cl_cte_tx_enable::handle](../bluetooth_hci_model_reference/P089_bt_hci_cp_le_set_cl_cte_tx_enable_结构体.md#a55125c808a888eeecfee9410bcb55859)
- [bt_hci_cp_le_set_cl_cte_tx_params::ant_ids](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#a27a228653ea560a77369a6b1829a8a9d)
- [bt_hci_cp_le_set_cl_cte_tx_params::switch_pattern_len](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#a8208571653e444221648d2a884eabfae)
- [bt_hci_cp_le_set_cl_cte_tx_params::cte_type](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#a869192cea35f4cd57984614e4c8bb5a5)
- [bt_hci_cp_le_set_cl_cte_tx_params::handle](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#a8f20e6e3bb408551d6cc494ad19391c4)
- [bt_hci_cp_le_set_cl_cte_tx_params::cte_len](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#ab5c4742cf37cf7e802423beb4a9b4fa2)
- [bt_hci_cp_le_set_cl_cte_tx_params::cte_count](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md#af5e82bf572b385904a0f24219bdc72ca)
- [bt_hci_cp_le_set_conn_cte_rx_params::ant_ids](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md#a519c37f5d797d8ddac5ba9be7c14b9f9)
- [bt_hci_cp_le_set_conn_cte_rx_params::sampling_enable](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md#a615cae822878cf1344a990e30fa80044)
- [bt_hci_cp_le_set_conn_cte_rx_params::slot_durations](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md#a6246d492b94c67af9604b89912dbdb61)
- [bt_hci_cp_le_set_conn_cte_rx_params::handle](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md#a76968866cf5c6ef4bfb983cb6b68a827)
- [bt_hci_cp_le_set_conn_cte_rx_params::switch_pattern_len](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md#a89194a5b9e6c7f0c176c915e451911df)
- [bt_hci_cp_le_set_conn_cte_tx_params::switch_pattern_len](../bluetooth_hci_model_reference/P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md#a8f0e5ee74662056f00eaa3a8c72f6fc4)
- [bt_hci_cp_le_set_conn_cte_tx_params::cte_types](../bluetooth_hci_model_reference/P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md#ab47f852b476ac2c35fc0631180e19fb4)
- [bt_hci_cp_le_set_conn_cte_tx_params::ant_ids](../bluetooth_hci_model_reference/P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md#abff85d652b3b2fd55ad78e53887cd7ce)
- [bt_hci_cp_le_set_conn_cte_tx_params::handle](../bluetooth_hci_model_reference/P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md#ae0a482982d804ffd7d16ea2b413e538d)
- [bt_hci_cp_le_set_data_len::tx_time](../bluetooth_hci_model_reference/P093_bt_hci_cp_le_set_data_len_结构体.md#a15285a4e8bf8e359bb326de4b30ba8f1)
- [bt_hci_cp_le_set_data_len::handle](../bluetooth_hci_model_reference/P093_bt_hci_cp_le_set_data_len_结构体.md#a874869090428a7f380c5466353573eba)
- [bt_hci_cp_le_set_data_len::tx_octets](../bluetooth_hci_model_reference/P093_bt_hci_cp_le_set_data_len_结构体.md#ac579e84a004a09813bbe0ed61db11931)
- [bt_hci_cp_le_set_default_phy::tx_phys](../bluetooth_hci_model_reference/P094_bt_hci_cp_le_set_default_phy_结构体.md#a0c4ab2d91021466fd136af3a0b6bde2a)
- [bt_hci_cp_le_set_default_phy::rx_phys](../bluetooth_hci_model_reference/P094_bt_hci_cp_le_set_default_phy_结构体.md#a4c3410f2ce9fb2817bc5d143908936d1)
- [bt_hci_cp_le_set_default_phy::all_phys](../bluetooth_hci_model_reference/P094_bt_hci_cp_le_set_default_phy_结构体.md#abe1d83e372e874739588812040d0b540)
- [bt_hci_cp_le_set_default_subrate::max_latency](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md#a16adacc30fd5ae00b3944f068b075b1a)
- [bt_hci_cp_le_set_default_subrate::supervision_timeout](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md#a1906f4dd7955200c81093b8f7c5d55c0)
- [bt_hci_cp_le_set_default_subrate::subrate_min](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md#a9d8fd7cad5260c8943b90ab50c04b225)
- [bt_hci_cp_le_set_default_subrate::subrate_max](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md#ad18a8042c38a1b4d83d6fccad1ab5af8)
- [bt_hci_cp_le_set_default_subrate::continuation_number](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md#aff2e682b4c8e5c3078885be126c5b958)
- [bt_hci_cp_le_set_event_mask::events](../bluetooth_hci_model_reference/P096_bt_hci_cp_le_set_event_mask_结构体.md#af7de4823aca253f15e57f54ee9b3879e)
- [bt_hci_cp_le_set_ext_adv_data::data](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md#a7d7df52500eb53a64b6ba5e62f6cf14f)
- [bt_hci_cp_le_set_ext_adv_data::handle](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md#a803bb793eefcc714c6c4034123a2e487)
- [bt_hci_cp_le_set_ext_adv_data::op](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md#ac5eaa1834f82024055923d08a3bef6b3)
- [bt_hci_cp_le_set_ext_adv_data::len](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md#aea3055cc7ffbaf4cd14996d885e21ba3)
- [bt_hci_cp_le_set_ext_adv_data::frag_pref](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md#af9eef9f59bfec5867ea36bdf33e3a9b1)
- [bt_hci_cp_le_set_ext_adv_enable::s](../bluetooth_hci_model_reference/P098_bt_hci_cp_le_set_ext_adv_enable_结构体.md#a04911e19f3b2f0079d4e12980d11157f)
- [bt_hci_cp_le_set_ext_adv_enable::set_num](../bluetooth_hci_model_reference/P098_bt_hci_cp_le_set_ext_adv_enable_结构体.md#a06088af8b432ac134943d9ebb7778ac7)
- [bt_hci_cp_le_set_ext_adv_enable::enable](../bluetooth_hci_model_reference/P098_bt_hci_cp_le_set_ext_adv_enable_结构体.md#ab7148b47bf052d8cba1f6bf3385051c8)
- [bt_hci_cp_le_set_ext_adv_param_v2::filter_policy](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a047656dd56bf883f1e307dcabe96f1de)
- [bt_hci_cp_le_set_ext_adv_param_v2::sec_adv_phy_opt](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a0c7994ef034270a7fd814386e7b76cc8)
- [bt_hci_cp_le_set_ext_adv_param_v2::prim_channel_map](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a1a96a88729e311c6a60571997aae9fc3)
- [bt_hci_cp_le_set_ext_adv_param_v2::prim_min_interval](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a25fec4dc9203bb50bb030087b42f473e)
- [bt_hci_cp_le_set_ext_adv_param_v2::tx_power](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a5283a6a40d46e0fe787ed403acab9f90)
- [bt_hci_cp_le_set_ext_adv_param_v2::own_addr_type](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a554f89f00700bc3ea4996b0a971fedbf)
- [bt_hci_cp_le_set_ext_adv_param_v2::prim_max_interval](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a6098216ae6ef0f9459aae16adecd193f)
- [bt_hci_cp_le_set_ext_adv_param_v2::sec_adv_phy](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a6c2a953fab938f304e815bd9d59d05ae)
- [bt_hci_cp_le_set_ext_adv_param_v2::prim_adv_phy_opt](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a8767fb7f5492f0323edd9afb687318db)
- [bt_hci_cp_le_set_ext_adv_param_v2::prim_adv_phy](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a92a215151c603c2f8dd1b7e730a8e979)
- [bt_hci_cp_le_set_ext_adv_param_v2::scan_req_notify_enable](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#a9f2a6f38e8965dabe17ad743d3aeda70)
- [bt_hci_cp_le_set_ext_adv_param_v2::sec_adv_max_skip](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#ac31b52df1033d11585781fbecc10f578)
- [bt_hci_cp_le_set_ext_adv_param_v2::peer_addr](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#ad8fccd11fbea598de62e057a69b72156)
- [bt_hci_cp_le_set_ext_adv_param_v2::handle](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#ad9e43219b471e44884b33ea5ddd90513)
- [bt_hci_cp_le_set_ext_adv_param_v2::sid](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#aeb26f7f16e2c71542421aada577a993f)
- [bt_hci_cp_le_set_ext_adv_param_v2::props](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md#aff572d12a03ca9cbc2ee80f75e1f77c7)
- [bt_hci_cp_le_set_ext_adv_param::prim_adv_phy](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a048874197ccbdbc626f0563be5c41ec7)
- [bt_hci_cp_le_set_ext_adv_param::prim_max_interval](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a08aa741a56e825a11424bf024ac65e14)
- [bt_hci_cp_le_set_ext_adv_param::filter_policy](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a29a62f8989f89b014cadbad9b94e996a)
- [bt_hci_cp_le_set_ext_adv_param::own_addr_type](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a3594f7337ccd739f59ac7845757de0e8)
- [bt_hci_cp_le_set_ext_adv_param::props](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a4af102ae90ca6917b3134491c5ff079f)
- [bt_hci_cp_le_set_ext_adv_param::sec_adv_max_skip](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a5793c6afe545290a1e792bcc73585b72)
- [bt_hci_cp_le_set_ext_adv_param::tx_power](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a5f7f3e477b5b0b8122b85f3e53dd7878)
- [bt_hci_cp_le_set_ext_adv_param::handle](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a65fe609dde9515212659087a024e7c65)
- [bt_hci_cp_le_set_ext_adv_param::peer_addr](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#a819e599df4025036fab2dabd7c61ea37)
- [bt_hci_cp_le_set_ext_adv_param::prim_min_interval](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#ab5a80941b3d832c2906daed8cf069a02)
- [bt_hci_cp_le_set_ext_adv_param::sec_adv_phy](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#abc82ba984647eb00bc490c01ce746a15)
- [bt_hci_cp_le_set_ext_adv_param::prim_channel_map](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#ad7a0b9028bcdb57a9011d4677412aed5)
- [bt_hci_cp_le_set_ext_adv_param::scan_req_notify_enable](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#ae694df46b1db4b029d1e177768b3821f)
- [bt_hci_cp_le_set_ext_adv_param::sid](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md#af8bc3509fdd5e89c27db466727fe1cd9)
- [bt_hci_cp_le_set_ext_scan_enable::enable](../bluetooth_hci_model_reference/P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md#a922d0c5a7ccb6c1e1864f662227b8307)
- [bt_hci_cp_le_set_ext_scan_enable::filter_dup](../bluetooth_hci_model_reference/P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md#aa5b0939838ab13eb8299f4a4b2fd3f14)
- [bt_hci_cp_le_set_ext_scan_enable::period](../bluetooth_hci_model_reference/P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md#aa60c8ade7047dcd202d83cfc3f18ada2)
- [bt_hci_cp_le_set_ext_scan_enable::duration](../bluetooth_hci_model_reference/P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md#adcd5e00a240f3e7395d0d25994b4013a)
- [bt_hci_cp_le_set_ext_scan_param::own_addr_type](../bluetooth_hci_model_reference/P102_bt_hci_cp_le_set_ext_scan_param_结构体.md#a3418aa8dbdb8062ee452f5756eb9f30c)
- [bt_hci_cp_le_set_ext_scan_param::filter_policy](../bluetooth_hci_model_reference/P102_bt_hci_cp_le_set_ext_scan_param_结构体.md#a47f6cf7f83451dcc2feac1a8d5837ad8)
- [bt_hci_cp_le_set_ext_scan_param::phys](../bluetooth_hci_model_reference/P102_bt_hci_cp_le_set_ext_scan_param_结构体.md#a6c38b7d074eb3c0cf5c301eb6c03b60c)
- [bt_hci_cp_le_set_ext_scan_param::p](../bluetooth_hci_model_reference/P102_bt_hci_cp_le_set_ext_scan_param_结构体.md#ab4eab9a52dca01bc19b35607d6ec5d36)
- [bt_hci_cp_le_set_ext_scan_rsp_data::op](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md#a3323a0844680b71cb8aedffa034837d7)
- [bt_hci_cp_le_set_ext_scan_rsp_data::len](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md#a6024eac85f600ed3b7051a84b91bdcfa)
- [bt_hci_cp_le_set_ext_scan_rsp_data::handle](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md#a8cf0624b9968686c7f6765ee25e11c90)
- [bt_hci_cp_le_set_ext_scan_rsp_data::data](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md#ab086720e1a22523ba155cb238ad75197)
- [bt_hci_cp_le_set_ext_scan_rsp_data::frag_pref](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md#ac4e1691926df370b290c9e6d866d310d)
- [bt_hci_cp_le_set_host_chan_classif::ch_map](../bluetooth_hci_model_reference/P104_bt_hci_cp_le_set_host_chan_classif_结构体.md#a0fb81bcdebe7da416cc4317486106752)
- [bt_hci_cp_le_set_host_feature::bit_value](../bluetooth_hci_model_reference/P105_bt_hci_cp_le_set_host_feature_结构体.md#a78b67164bce232466ab348f8937682c3)
- [bt_hci_cp_le_set_host_feature::bit_number](../bluetooth_hci_model_reference/P105_bt_hci_cp_le_set_host_feature_结构体.md#adcca35df216061ea08bd27e10fefd5e9)
- [bt_hci_cp_le_set_path_loss_reporting_enable::enable](../bluetooth_hci_model_reference/P106_bt_hci_cp_le_set_path_loss_reporting_enable_结构体.md#a209a77ef3cf545150feaecdb814797f0)
- [bt_hci_cp_le_set_path_loss_reporting_enable::handle](../bluetooth_hci_model_reference/P106_bt_hci_cp_le_set_path_loss_reporting_enable_结构体.md#a79487ac2235da100b41ec50c77bad808)
- [bt_hci_cp_le_set_path_loss_reporting_parameters::min_time_spent](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#a2289e8198eea1686030ffd3e225c8e7d)
- [bt_hci_cp_le_set_path_loss_reporting_parameters::low_hysteresis](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#a28f79bd4ccec4ed108e20a0080ec842d)
- [bt_hci_cp_le_set_path_loss_reporting_parameters::handle](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#a2dec83b0269835538cf4bc5553483f19)
- [bt_hci_cp_le_set_path_loss_reporting_parameters::low_threshold](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#a79a53ca3a481e013a5ee892d779e7bfd)
- [bt_hci_cp_le_set_path_loss_reporting_parameters::high_hysteresis](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#ab5de762b7b82c8f453dafe1ea9bbf46d)
- [bt_hci_cp_le_set_path_loss_reporting_parameters::high_threshold](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md#ac8b7b832ba241c0448c80be22249b3ca)
- [bt_hci_cp_le_set_pawr_response_data::sync_handle](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#a034afaaacf4b2168b9cd54cfde583b5c)
- [bt_hci_cp_le_set_pawr_response_data::response_data](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#a39cbc74ab95881b6dde8fa377d2951e5)
- [bt_hci_cp_le_set_pawr_response_data::response_slot](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#a4356344510833196533bb9582f6fe18a)
- [bt_hci_cp_le_set_pawr_response_data::request_subevent](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#a675a223891b28f06e78df6223439dc28)
- [bt_hci_cp_le_set_pawr_response_data::response_data_length](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#a8c546fa3c6d969d44c54926330e5cf85)
- [bt_hci_cp_le_set_pawr_response_data::response_subevent](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#aaf2e0eb3b491b5ccd15ba5259fd900c7)
- [bt_hci_cp_le_set_pawr_response_data::request_event](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md#aaf5c337af93f13e243451b46a94ffb77)
- [bt_hci_cp_le_set_pawr_subevent_data_element::response_slot_start](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md#a90178bcd86c1bad0a768f391ce11613f)
- [bt_hci_cp_le_set_pawr_subevent_data_element::subevent_data](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md#a91c975189e409b733ac9a4af5763b12a)
- [bt_hci_cp_le_set_pawr_subevent_data_element::subevent](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md#abf33f93f0f1ddf3532c6cae13483ec1e)
- [bt_hci_cp_le_set_pawr_subevent_data_element::subevent_data_length](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md#ace5860dfa0f628eaed2b68b171d875da)
- [bt_hci_cp_le_set_pawr_subevent_data_element::response_slot_count](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md#ad8da1cc672eedf8be8cfc7d0d7ec1b41)
- [bt_hci_cp_le_set_pawr_subevent_data::adv_handle](../bluetooth_hci_model_reference/P109_bt_hci_cp_le_set_pawr_subevent_data_结构体.md#a47d84125d15cce1fc969db3e5caa07e1)
- [bt_hci_cp_le_set_pawr_subevent_data::num_subevents](../bluetooth_hci_model_reference/P109_bt_hci_cp_le_set_pawr_subevent_data_结构体.md#a9397eebd6771ad159d1bdae0d59e5f46)
- [bt_hci_cp_le_set_pawr_subevent_data::subevents](../bluetooth_hci_model_reference/P109_bt_hci_cp_le_set_pawr_subevent_data_结构体.md#aa932c1f19de96f89a79bbcb3ecbc1f5d)
- [bt_hci_cp_le_set_pawr_sync_subevent::num_subevents](../bluetooth_hci_model_reference/P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md#a2648ff50e0bad585e77e6f340836555a)
- [bt_hci_cp_le_set_pawr_sync_subevent::sync_handle](../bluetooth_hci_model_reference/P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md#a89f3092c2dd561e5469bb5bf57a06172)
- [bt_hci_cp_le_set_pawr_sync_subevent::subevents](../bluetooth_hci_model_reference/P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md#a9a362ae841e5305b3985c4b2d88c6753)
- [bt_hci_cp_le_set_pawr_sync_subevent::periodic_adv_properties](../bluetooth_hci_model_reference/P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md#aa73b23816e6c2c6546de15f6f6caff27)
- [bt_hci_cp_le_set_per_adv_data::handle](../bluetooth_hci_model_reference/P112_bt_hci_cp_le_set_per_adv_data_结构体.md#a93cbb46ce6664880487e009a0b47af02)
- [bt_hci_cp_le_set_per_adv_data::op](../bluetooth_hci_model_reference/P112_bt_hci_cp_le_set_per_adv_data_结构体.md#aac34596f0970c976c4ef71250d326c2c)
- [bt_hci_cp_le_set_per_adv_data::data](../bluetooth_hci_model_reference/P112_bt_hci_cp_le_set_per_adv_data_结构体.md#adaf581f8db6aafb4dc5df669df7ad26d)
- [bt_hci_cp_le_set_per_adv_data::len](../bluetooth_hci_model_reference/P112_bt_hci_cp_le_set_per_adv_data_结构体.md#ae6ee631a153cb6fed88695e599f63e91)
- [bt_hci_cp_le_set_per_adv_enable::handle](../bluetooth_hci_model_reference/P113_bt_hci_cp_le_set_per_adv_enable_结构体.md#a998f4e38a56f771f234ce099b4528a3d)
- [bt_hci_cp_le_set_per_adv_enable::enable](../bluetooth_hci_model_reference/P113_bt_hci_cp_le_set_per_adv_enable_结构体.md#afff649b908264c617b249bcfbebadd53)
- [bt_hci_cp_le_set_per_adv_param_v2::num_response_slots](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#a2483eb4457f9dc22ff8473175662e260)
- [bt_hci_cp_le_set_per_adv_param_v2::response_slot_spacing](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#a35fcc697e60d3c398f03be7503f611bd)
- [bt_hci_cp_le_set_per_adv_param_v2::subevent_interval](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#a79dfc3b13068d9c51f0a756f025aaeba)
- [bt_hci_cp_le_set_per_adv_param_v2::num_subevents](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#a7bea764aa5d21e03946804566b1f9869)
- [bt_hci_cp_le_set_per_adv_param_v2::max_interval](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#acc9718286ab0847a3444d3fc2d3c93bc)
- [bt_hci_cp_le_set_per_adv_param_v2::response_slot_delay](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#acdeb503c0a13291158ad389c9f6ac206)
- [bt_hci_cp_le_set_per_adv_param_v2::props](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#ad2d658bb0be35aee6b5c133fece89068)
- [bt_hci_cp_le_set_per_adv_param_v2::min_interval](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#ae36e28210a515f73648e6f8b3984fb55)
- [bt_hci_cp_le_set_per_adv_param_v2::handle](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md#aee1088b46914c8e26d9e97ce573291c6)
- [bt_hci_cp_le_set_per_adv_param::max_interval](../bluetooth_hci_model_reference/P114_bt_hci_cp_le_set_per_adv_param_结构体.md#a1a2a69ea6e310710892184ced472eb8a)
- [bt_hci_cp_le_set_per_adv_param::handle](../bluetooth_hci_model_reference/P114_bt_hci_cp_le_set_per_adv_param_结构体.md#a2b61031952b3893add7677d3802e368b)
- [bt_hci_cp_le_set_per_adv_param::props](../bluetooth_hci_model_reference/P114_bt_hci_cp_le_set_per_adv_param_结构体.md#a879ea10e1ab217b4aa49dfcf3b394691)
- [bt_hci_cp_le_set_per_adv_param::min_interval](../bluetooth_hci_model_reference/P114_bt_hci_cp_le_set_per_adv_param_结构体.md#af01696ef6bf02e7db37d45a0c9852ef5)
- [bt_hci_cp_le_set_per_adv_recv_enable::handle](../bluetooth_hci_model_reference/P116_bt_hci_cp_le_set_per_adv_recv_enable_结构体.md#a1e626eecf1d3f0820c3b2a13fd84b92f)
- [bt_hci_cp_le_set_per_adv_recv_enable::enable](../bluetooth_hci_model_reference/P116_bt_hci_cp_le_set_per_adv_recv_enable_结构体.md#a2187ec96822726daa5e43e910cc41cc3)
- [bt_hci_cp_le_set_phy::tx_phys](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md#a06880062ff486b532ebeb789adb57d1e)
- [bt_hci_cp_le_set_phy::phy_opts](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md#a458ab90f83b60fafa66167f474c0800d)
- [bt_hci_cp_le_set_phy::rx_phys](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md#ab30eb68920a0578b16794250e592b12a)
- [bt_hci_cp_le_set_phy::handle](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md#ad0759eea02017674459d4ce0af0e526e)
- [bt_hci_cp_le_set_phy::all_phys](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md#afb8d056dc7d8824eec0ef16fdf9ce924)
- [bt_hci_cp_le_set_privacy_mode::id_addr](../bluetooth_hci_model_reference/P118_bt_hci_cp_le_set_privacy_mode_结构体.md#a404cc9f04cd11924445f12eb4471ef2e)
- [bt_hci_cp_le_set_privacy_mode::mode](../bluetooth_hci_model_reference/P118_bt_hci_cp_le_set_privacy_mode_结构体.md#a8ca00418b0638bba6ef586d6cbf253a5)
- [bt_hci_cp_le_set_procedure_parameters::min_procedure_interval](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a22ecbaff0fd48a0716a15d265adc590e)
- [bt_hci_cp_le_set_procedure_parameters::min_subevent_len](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a51fb8c789cefce09d5da2b86d5c862ce)
- [bt_hci_cp_le_set_procedure_parameters::max_procedure_len](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a5de9205fdf1b6e342f53a12aa82c10c5)
- [bt_hci_cp_le_set_procedure_parameters::preferred_peer_antenna](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a7a61ff539f68a02ea7aa466f182dc5ab)
- [bt_hci_cp_le_set_procedure_parameters::config_id](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a7d2f5d9242df436906b005e66c7bb75d)
- [bt_hci_cp_le_set_procedure_parameters::snr_control_initiator](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#a8524fd01e35094d2b78488c0a2876832)
- [bt_hci_cp_le_set_procedure_parameters::snr_control_reflector](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#aa5a6a677b6e0d57658041e891535d74b)
- [bt_hci_cp_le_set_procedure_parameters::tone_antenna_config_selection](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#aa783e0e63c38ceee503c0b73ac873ca7)
- [bt_hci_cp_le_set_procedure_parameters::max_subevent_len](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#aa9ec99aff85de173ccb2d3f144c85319)
- [bt_hci_cp_le_set_procedure_parameters::handle](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#ab8a15269255fb7d960ae712a844b9f35)
- [bt_hci_cp_le_set_procedure_parameters::max_procedure_count](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#ac6bb66fa24aec17a964f27365ca65ec9)
- [bt_hci_cp_le_set_procedure_parameters::max_procedure_interval](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#ad46165bc5f6d875940ee53a8b98cb5b4)
- [bt_hci_cp_le_set_procedure_parameters::tx_power_delta](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#ade09ca9d42b0db682cf677d9ac4326d2)
- [bt_hci_cp_le_set_procedure_parameters::phy](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md#afcd4e8b390fd996ee134043ec2930fe8)
- [bt_hci_cp_le_set_random_address::bdaddr](../bluetooth_hci_model_reference/P120_bt_hci_cp_le_set_random_address_结构体.md#a919ef74473f4f86d00595ec8606789d0)
- [bt_hci_cp_le_set_rpa_timeout::rpa_timeout](../bluetooth_hci_model_reference/P121_bt_hci_cp_le_set_rpa_timeout_结构体.md#a6b1befe9d2131a889de17339ec1941fa)
- [bt_hci_cp_le_set_scan_enable::enable](../bluetooth_hci_model_reference/P122_bt_hci_cp_le_set_scan_enable_结构体.md#a5e429a0b11be1493515803a360932b06)
- [bt_hci_cp_le_set_scan_enable::filter_dup](../bluetooth_hci_model_reference/P122_bt_hci_cp_le_set_scan_enable_结构体.md#a77b0f05c0e76681ed633bd42b3f21811)
- [bt_hci_cp_le_set_scan_param::window](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md#a3b5b4767092fc69a63d2219d60722407)
- [bt_hci_cp_le_set_scan_param::addr_type](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md#a694c74a6fc95f767d2e89e6596d51e98)
- [bt_hci_cp_le_set_scan_param::filter_policy](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md#ab7a268e17a5d564d475ff9dee5e6e14b)
- [bt_hci_cp_le_set_scan_param::scan_type](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md#ad19a479cc3c27ab24286b537b646261e)
- [bt_hci_cp_le_set_scan_param::interval](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md#adcd8be074a8b19e0e7d02c4ea8209c93)
- [bt_hci_cp_le_set_scan_rsp_data::len](../bluetooth_hci_model_reference/P124_bt_hci_cp_le_set_scan_rsp_data_结构体.md#a0fe51008184419c9560bb5d8f287d8be)
- [bt_hci_cp_le_set_scan_rsp_data::data](../bluetooth_hci_model_reference/P124_bt_hci_cp_le_set_scan_rsp_data_结构体.md#aa719449dc2b85f094081d66398b72c7d)
- [bt_hci_cp_le_set_tx_power_report_enable::local_enable](../bluetooth_hci_model_reference/P125_bt_hci_cp_le_set_tx_power_report_enable_结构体.md#a30580470d1ba516d86c8b157ca415ef3)
- [bt_hci_cp_le_set_tx_power_report_enable::handle](../bluetooth_hci_model_reference/P125_bt_hci_cp_le_set_tx_power_report_enable_结构体.md#a4a37c87f8f6a966a90c5de09096d1356)
- [bt_hci_cp_le_set_tx_power_report_enable::remote_enable](../bluetooth_hci_model_reference/P125_bt_hci_cp_le_set_tx_power_report_enable_结构体.md#ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e)
- [bt_hci_cp_le_setup_iso_path::handle](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a0054fede0e583cef0dbcf6ef3134e480)
- [bt_hci_cp_le_setup_iso_path::codec_config_len](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a1a816d8e8c434a05ea897b74bc4d89c7)
- [bt_hci_cp_le_setup_iso_path::controller_delay](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a31948436e6608f9943d34ce89a65c64c)
- [bt_hci_cp_le_setup_iso_path::codec_id](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a5256fc99b362e3a5f986ef2b71b29ccb)
- [bt_hci_cp_le_setup_iso_path::path_id](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a7c07d69b2005af1f7f2618f2bfa60d50)
- [bt_hci_cp_le_setup_iso_path::path_dir](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#a89c1324359a4fc2f10fee9ebbac5cf2b)
- [bt_hci_cp_le_setup_iso_path::codec_config](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md#ade4dee947e3d288f769d2d69fc57f96a)
- [bt_hci_cp_le_start_encryption::handle](../bluetooth_hci_model_reference/P127_bt_hci_cp_le_start_encryption_结构体.md#a4ac6d63f336e36a347242153aced4c71)
- [bt_hci_cp_le_start_encryption::rand](../bluetooth_hci_model_reference/P127_bt_hci_cp_le_start_encryption_结构体.md#a896961309d9b3f136beecf70a7e6e8e4)
- [bt_hci_cp_le_start_encryption::ltk](../bluetooth_hci_model_reference/P127_bt_hci_cp_le_start_encryption_结构体.md#a99d2dd719ce38976e9da8a73f26839a1)
- [bt_hci_cp_le_start_encryption::ediv](../bluetooth_hci_model_reference/P127_bt_hci_cp_le_start_encryption_结构体.md#ac1e1fd8b6b97bbd6f27b6e4322b03530)
- [bt_hci_cp_le_subrate_request::max_latency](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#a04ccc83303baabf30b663983883e7e77)
- [bt_hci_cp_le_subrate_request::subrate_min](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#a18ba526d8a843ad9c74c22d0899d9c1f)
- [bt_hci_cp_le_subrate_request::handle](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#a2595419182358e3386a0fb6e523a3dda)
- [bt_hci_cp_le_subrate_request::subrate_max](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#a5c95a2bea462fb72d34d6314046041b7)
- [bt_hci_cp_le_subrate_request::supervision_timeout](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#a60bcbe27605063725422a0b1c35f21e7)
- [bt_hci_cp_le_subrate_request::continuation_number](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md#ab32a92ed52266c6b7d6d9ab08787e770)
- [bt_hci_cp_le_terminate_big::reason](../bluetooth_hci_model_reference/P129_bt_hci_cp_le_terminate_big_结构体.md#a958ab6b2f2bb30c825060498e6917a18)
- [bt_hci_cp_le_terminate_big::big_handle](../bluetooth_hci_model_reference/P129_bt_hci_cp_le_terminate_big_结构体.md#acb5fb9451cf890245a85704579b1d1c8)
- [bt_hci_cp_le_tx_test_v3::test_data_len](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#a1c0828e51bb6c24e9dd1f12b5badcfea)
- [bt_hci_cp_le_tx_test_v3::switch_pattern_len](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#a459b850f35c61bf7f53d3730245cb4bb)
- [bt_hci_cp_le_tx_test_v3::cte_len](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#a52d2d6dcc188d5f02904e0e56f461841)
- [bt_hci_cp_le_tx_test_v3::tx_ch](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#a6486882bc375f229a88bbfa53be49670)
- [bt_hci_cp_le_tx_test_v3::phy](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#a712a30d9d6afc7d302041e1de6721de4)
- [bt_hci_cp_le_tx_test_v3::pkt_payload](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#ad8f2d2ca3ad3be28c0aec9e8a0e1bc61)
- [bt_hci_cp_le_tx_test_v3::cte_type](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#adf6b1653902fb13cc1ccc32cd91c990f)
- [bt_hci_cp_le_tx_test_v3::ant_ids](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md#afdb6dd44108e9a4a21ac31a74c1e083f)
- [bt_hci_cp_le_tx_test_v4_tx_power::tx_power](../bluetooth_hci_model_reference/P133_bt_hci_cp_le_tx_test_v4_tx_power_结构体.md#a2a8b1c31787066ad2b471aec5c261085)
- [bt_hci_cp_le_tx_test_v4::switch_pattern_len](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a2039a87b5f32c4a45b8f858808df7cdc)
- [bt_hci_cp_le_tx_test_v4::tx_ch](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a3ccae40f09b2763b2b07dc16982f3973)
- [bt_hci_cp_le_tx_test_v4::ant_ids](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a3fe8ab7c0ee389dce8592cb7a38bc42c)
- [bt_hci_cp_le_tx_test_v4::phy](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a5db011159fe75f4522e03ea1efdc57bd)
- [bt_hci_cp_le_tx_test_v4::test_data_len](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a7a8e2610fb8903ccfb6e4b08017f6112)
- [bt_hci_cp_le_tx_test_v4::cte_len](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#a8dea923a63e787de3bfe07611eb7a1ed)
- [bt_hci_cp_le_tx_test_v4::pkt_payload](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#abdd393eb264f04acf65e2dce4bd65ac0)
- [bt_hci_cp_le_tx_test_v4::cte_type](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md#ae950f71a3fcfca0cf738bc28693256cf)
- [bt_hci_cp_le_tx_test::test_data_len](../bluetooth_hci_model_reference/P130_bt_hci_cp_le_tx_test_结构体.md#a55c5f1621a51da03500910fc9664df54)
- [bt_hci_cp_le_tx_test::tx_ch](../bluetooth_hci_model_reference/P130_bt_hci_cp_le_tx_test_结构体.md#aae634b277125066ecbc36d119bc4244f)
- [bt_hci_cp_le_tx_test::pkt_payload](../bluetooth_hci_model_reference/P130_bt_hci_cp_le_tx_test_结构体.md#ad93908905d370842f16e16cc45280495)
- [bt_hci_cp_le_write_cached_remote_fae_table::handle](../bluetooth_hci_model_reference/P134_bt_hci_cp_le_write_cached_remote_fae_table_结构体.md#a330531f1809cddea8f1527f3b0a92e31)
- [bt_hci_cp_le_write_cached_remote_fae_table::remote_fae_table](../bluetooth_hci_model_reference/P134_bt_hci_cp_le_write_cached_remote_fae_table_结构体.md#a8594dd89888d1388f2a45a33e12e94d0)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::rtt_capability](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a0872c2a5399e1d82f334796dd35379ad)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::rtt_aa_only_n](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a17d3094a1b93665e755b2111074de42c)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::modes_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a1ff4fede6b4d942f64ec2b94b222703b)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::cs_sync_phys_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a2077365a697d7085d7db97fb35c391f4)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::rtt_random_payload_n](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a214f693e10c331091e34f09c2cfc9749)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::nadm_sounding_capability](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a225720841ea95409879d51bd9a031fb7)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::nadm_random_capability](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a22f1010c9f4de7902480d3f84d499fb1)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::subfeatures_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a2e8693852819f5e4afa8cae90f8ae92c)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_ip2_ipt_times_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a30cee084044918cb450060a164bd4b30)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::num_config_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a65a5b6ebdbc5793ca800ee202cb4676c)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::num_antennas_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a6bb274c4c2ff4dc2c6136b0bc7515be3)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::roles_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a6eff7fb52e3ef1074eb875af4c79a8aa)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_sw_ipt_time_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a8aa60cab3469fadd342a0a9b0d1b094f)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_ip2_times_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#a8c63e46cf58623b3ca9cbfa7b802744e)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_fcs_times_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#abf661cac9a1a2a5bf38180dbfc486bcd)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_ip1_times_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ac370abefdc5a7acdf1e3c72093d11018)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::handle](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ac599d7323d560b8f554bbaaf70aabd8b)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_pm_times_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ac930e63945abfc0cdfdaa79164e114fa)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::rtt_sounding_n](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ad342355fdc6396d6680b7e215ef4b16e)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::max_antenna_paths_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ad7c6799d86889b67d86ca44bac4238a6)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::tx_snr_capability](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#ae757536a884e640451e35dd2fca90605)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#aead25f8f371ed85e66d05af852b90a9e)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_sw_time_supported](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md#afbe4805ccd9db70a596afdabb6963885)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::t_ip2_times_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a0911e19deceb7f243ac706ddb4cf0a3a)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::t_ip1_times_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a257b38d937c1111a66f6c28f1e221211)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::nadm_random_capability](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a25faaf2be6db05c44256b9f559841c87)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::nadm_sounding_capability](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a29781bbe7e25c39b06047725f1d11426)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::subfeatures_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a2b5c828a30525eee5b1ce48f3ba98896)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::rtt_sounding_n](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a31c877363bd315786ef834215614d346)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::num_config_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a7a60c326707ebd60b96d25924e3c9e40)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::t_pm_times_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a870e068fcc15dd44dca3ac24334000ee)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::handle](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a8a884bca80550eb72a433f5ea280f702)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::rtt_random_payload_n](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a8f98235e9238a80602806fb60e1261bb)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::cs_sync_phys_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a908322e5c02500abbdd8891c5248998d)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::modes_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a93f4973a1229273c51f6a20e741e42ed)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::rtt_capability](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a94fb0f963f706c303729d7a0088ef617)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::max_antenna_paths_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a96a49382bef8f3163cd82899f59ed5fe)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::num_antennas_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#a96b0c7868da711271e74b82fcfd32fc2)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::tx_snr_capability](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#aa9e48c6f0d22e9a64e8591a34409988e)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::t_sw_time_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#ab77f7bda7302cad94805e8ea43b8bf14)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::rtt_aa_only_n](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#ae4b9b8ba0e83978f131541959062f691)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::roles_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#ae88cf07e3c8e6ad64a1beb60270d8961)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::t_fcs_times_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#af959f1539f5bbf74b0e63db743a132f4)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities::max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md#afbfe48ddad696315d6e021a85d32559d)
- [bt_hci_cp_le_write_default_data_len::max_tx_octets](../bluetooth_hci_model_reference/P137_bt_hci_cp_le_write_default_data_len_结构体.md#a0ffb8c52d9031dfe448eac0943a4a49c)
- [bt_hci_cp_le_write_default_data_len::max_tx_time](../bluetooth_hci_model_reference/P137_bt_hci_cp_le_write_default_data_len_结构体.md#a2ada0ea5ee8ac8e6d59fc6adc18421b8)
- [bt_hci_cp_le_write_rf_path_comp::rx_path_comp](../bluetooth_hci_model_reference/P138_bt_hci_cp_le_write_rf_path_comp_结构体.md#a11aad5607e444cf55dd5878f1f6f9436)
- [bt_hci_cp_le_write_rf_path_comp::tx_path_comp](../bluetooth_hci_model_reference/P138_bt_hci_cp_le_write_rf_path_comp_结构体.md#a5f99b131f3fba91706bdc8277c1abba1)
- [bt_hci_cp_link_key_neg_reply::bdaddr](../bluetooth_hci_model_reference/P139_bt_hci_cp_link_key_neg_reply_结构体.md#aca3114707eb7c631af582626551619cd)
- [bt_hci_cp_link_key_reply::link_key](../bluetooth_hci_model_reference/P140_bt_hci_cp_link_key_reply_结构体.md#a2af0b4b55a5ffcff0221da841ba0cbba)
- [bt_hci_cp_link_key_reply::bdaddr](../bluetooth_hci_model_reference/P140_bt_hci_cp_link_key_reply_结构体.md#ab5221952fbcfe413d7c3bd3a441a9b17)
- [bt_hci_cp_pin_code_neg_reply::bdaddr](../bluetooth_hci_model_reference/P147_bt_hci_cp_pin_code_neg_reply_结构体.md#a8aec3ba6c530850dce0a2d7b7f7f86ee)
- [bt_hci_cp_pin_code_reply::bdaddr](../bluetooth_hci_model_reference/P148_bt_hci_cp_pin_code_reply_结构体.md#a627800dcb580110be785576dfcc49bb1)
- [bt_hci_cp_pin_code_reply::pin_len](../bluetooth_hci_model_reference/P148_bt_hci_cp_pin_code_reply_结构体.md#aa0cbf668608c3eb4998356ad7b18c01a)
- [bt_hci_cp_pin_code_reply::pin_code](../bluetooth_hci_model_reference/P148_bt_hci_cp_pin_code_reply_结构体.md#afc4ed5ae429087f4692af716d6b56997)
- [bt_hci_cp_read_auth_payload_timeout::handle](../bluetooth_hci_model_reference/P149_bt_hci_cp_read_auth_payload_timeout_结构体.md#adcdd657feb3ea6b892e2a5034365dd77)
- [bt_hci_cp_read_codec_capabilities::direction](../bluetooth_hci_model_reference/P150_bt_hci_cp_read_codec_capabilities_结构体.md#a237695f4d0a1359d5ce71d831708a69c)
- [bt_hci_cp_read_codec_capabilities::transport](../bluetooth_hci_model_reference/P150_bt_hci_cp_read_codec_capabilities_结构体.md#a6479561573172356d7515ef92f75b8d4)
- [bt_hci_cp_read_codec_capabilities::codec_id](../bluetooth_hci_model_reference/P150_bt_hci_cp_read_codec_capabilities_结构体.md#ad48b7f228742d86a71dffa314331bbe1)
- [bt_hci_cp_read_ctlr_delay::codec_id](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md#a2afb9ca8bc2e24cd479b29bc1a53c867)
- [bt_hci_cp_read_ctlr_delay::direction](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md#a5e9f74d4f82809289038da29af0c663d)
- [bt_hci_cp_read_ctlr_delay::transport](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md#a60a6a5b87896d0c27d734b56ead58a9b)
- [bt_hci_cp_read_ctlr_delay::codec_config](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md#a6c15d141c40bca8bd095f4a86f5a93bd)
- [bt_hci_cp_read_ctlr_delay::codec_config_len](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md#ac881526b479d5f1717efbe35cdcc7e87)
- [bt_hci_cp_read_encryption_key_size::handle](../bluetooth_hci_model_reference/P152_bt_hci_cp_read_encryption_key_size_结构体.md#af15765007fd0e2fc4186b54323553019)
- [bt_hci_cp_read_link_policy_settings::handle](../bluetooth_hci_model_reference/P153_bt_hci_cp_read_link_policy_settings_结构体.md#abd2d7c4074428367213b6599dee2f9d8)
- [bt_hci_cp_read_link_supervision_timeout::handle](../bluetooth_hci_model_reference/P154_bt_hci_cp_read_link_supervision_timeout_结构体.md#a96f55e4c89154f5ff911d114a23dc3e4)
- [bt_hci_cp_read_local_ext_features::page](../bluetooth_hci_model_reference/P155_bt_hci_cp_read_local_ext_features_结构体.md#a79c6a6a6f1026a7e9ee774183ea7e132)
- [bt_hci_cp_read_remote_ext_features::page](../bluetooth_hci_model_reference/P156_bt_hci_cp_read_remote_ext_features_结构体.md#a6aff189605b276998e58b051429a5cd2)
- [bt_hci_cp_read_remote_ext_features::handle](../bluetooth_hci_model_reference/P156_bt_hci_cp_read_remote_ext_features_结构体.md#aaa236c11d148252e34fd20d794d991f3)
- [bt_hci_cp_read_remote_features::handle](../bluetooth_hci_model_reference/P157_bt_hci_cp_read_remote_features_结构体.md#ae14362a04c00b37342f3cc413f3933d3)
- [bt_hci_cp_read_remote_version_info::handle](../bluetooth_hci_model_reference/P158_bt_hci_cp_read_remote_version_info_结构体.md#a504b83f16a82b1e179d74547c7a29bf3)
- [bt_hci_cp_read_rssi::handle](../bluetooth_hci_model_reference/P159_bt_hci_cp_read_rssi_结构体.md#a0662bc56b344ca2bf9a2dcabe8a13c09)
- [bt_hci_cp_read_tx_power_level::type](../bluetooth_hci_model_reference/P160_bt_hci_cp_read_tx_power_level_结构体.md#a1920e671ec2deda1daf47f06a86d2881)
- [bt_hci_cp_read_tx_power_level::handle](../bluetooth_hci_model_reference/P160_bt_hci_cp_read_tx_power_level_结构体.md#a1c268364fc80b9478d70b7eb997d9825)
- [bt_hci_cp_reject_conn_req::reason](../bluetooth_hci_model_reference/P161_bt_hci_cp_reject_conn_req_结构体.md#a1c2e234d6d00296bc01962b95e849df0)
- [bt_hci_cp_reject_conn_req::bdaddr](../bluetooth_hci_model_reference/P161_bt_hci_cp_reject_conn_req_结构体.md#a9a1cb4173367c6f018fbd30a47c590b4)
- [bt_hci_cp_remote_name_cancel::bdaddr](../bluetooth_hci_model_reference/P162_bt_hci_cp_remote_name_cancel_结构体.md#a0b7b4362804077ce828aeeb2b8af86b9)
- [bt_hci_cp_remote_name_request::bdaddr](../bluetooth_hci_model_reference/P163_bt_hci_cp_remote_name_request_结构体.md#a5093f7bb70fa36f4948039d02d594e27)
- [bt_hci_cp_remote_name_request::clock_offset](../bluetooth_hci_model_reference/P163_bt_hci_cp_remote_name_request_结构体.md#a5d7ea30052f8e4e2b3564659ca187c48)
- [bt_hci_cp_remote_name_request::reserved](../bluetooth_hci_model_reference/P163_bt_hci_cp_remote_name_request_结构体.md#ab1883aa2b08d89f9c3190f338808a43c)
- [bt_hci_cp_remote_name_request::pscan_rep_mode](../bluetooth_hci_model_reference/P163_bt_hci_cp_remote_name_request_结构体.md#aed0aea58ca6f5dc15220083d377cbf5c)
- [bt_hci_cp_set_conn_encrypt::handle](../bluetooth_hci_model_reference/P164_bt_hci_cp_set_conn_encrypt_结构体.md#a39e0c40ed6e6e9387ae384fd122fca4b)
- [bt_hci_cp_set_conn_encrypt::encrypt](../bluetooth_hci_model_reference/P164_bt_hci_cp_set_conn_encrypt_结构体.md#aa259563efd49d04a8886f74169fd30b1)
- [bt_hci_cp_set_ctl_to_host_flow::flow_enable](../bluetooth_hci_model_reference/P165_bt_hci_cp_set_ctl_to_host_flow_结构体.md#a75b614de1ab1fbfc6aa9c11d833976a6)
- [bt_hci_cp_set_event_mask_page_2::events_page_2](../bluetooth_hci_model_reference/P167_bt_hci_cp_set_event_mask_page_2_结构体.md#aacf1308d0892226e2c10216a07cd1fcc)
- [bt_hci_cp_set_event_mask::events](../bluetooth_hci_model_reference/P166_bt_hci_cp_set_event_mask_结构体.md#ab3af227511f47ee03f2d6aba8ae65c5d)
- [bt_hci_cp_setup_sync_conn::rx_bandwidth](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#a137601ab44970782e2f3d4fcd2c8fcc2)
- [bt_hci_cp_setup_sync_conn::content_format](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#a4d7df5b1aa714bc14d0b6c3cbccc5014)
- [bt_hci_cp_setup_sync_conn::max_latency](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#a5ffb5e552d4913974a10a16083f82864)
- [bt_hci_cp_setup_sync_conn::retrans_effort](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#a61ebbc775d3ca0724ea173d72a96e0c0)
- [bt_hci_cp_setup_sync_conn::pkt_type](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#a6d4c16a4d77d3ee4f8f65ab18a0f192d)
- [bt_hci_cp_setup_sync_conn::tx_bandwidth](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#aa35718e13a7d778c779be535c2b1945e)
- [bt_hci_cp_setup_sync_conn::handle](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md#ad065185846694fc0070bb366e642f1c7)
- [bt_hci_cp_sniff_mode::attempt](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md#a1896272c588ed2ffe0052353eed528c4)
- [bt_hci_cp_sniff_mode::handle](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md#a37cc61e67148cf8993aa3c6410094d7e)
- [bt_hci_cp_sniff_mode::timeout](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md#aa0bfa66eb627378a820144b8ca748b5f)
- [bt_hci_cp_sniff_mode::min_interval](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md#aaba62465c5fb76641715eed4bc8c25e9)
- [bt_hci_cp_sniff_mode::max_interval](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md#ad765b1aebc101886d5e9805245252718)
- [bt_hci_cp_sniff_subrating::max_latency](../bluetooth_hci_model_reference/P170_bt_hci_cp_sniff_subrating_结构体.md#a3534ddbf9876a82855b569ef7e01fd96)
- [bt_hci_cp_sniff_subrating::min_local_timeout](../bluetooth_hci_model_reference/P170_bt_hci_cp_sniff_subrating_结构体.md#aa6de505cd8ba606d893dc74590083963)
- [bt_hci_cp_sniff_subrating::min_remote_timeout](../bluetooth_hci_model_reference/P170_bt_hci_cp_sniff_subrating_结构体.md#ab11c374063c6219b942b839f10d6a74d)
- [bt_hci_cp_sniff_subrating::handle](../bluetooth_hci_model_reference/P170_bt_hci_cp_sniff_subrating_结构体.md#af25eb1e9ee6eef5888ffa31b9fdd2887)
- [bt_hci_cp_switch_role::role](../bluetooth_hci_model_reference/P171_bt_hci_cp_switch_role_结构体.md#ac6b6acdaf5993384eb3029c9e78407b6)
- [bt_hci_cp_switch_role::bdaddr](../bluetooth_hci_model_reference/P171_bt_hci_cp_switch_role_结构体.md#afed76d83e552fa3666f8c84df4279938)
- [bt_hci_cp_user_confirm_reply::bdaddr](../bluetooth_hci_model_reference/P172_bt_hci_cp_user_confirm_reply_结构体.md#abe0e8da3e590c565364ed30ba107a0e6)
- [bt_hci_cp_user_passkey_neg_reply::bdaddr](../bluetooth_hci_model_reference/P173_bt_hci_cp_user_passkey_neg_reply_结构体.md#ade9d7068054b15089b8c238ecc3e4397)
- [bt_hci_cp_user_passkey_reply::bdaddr](../bluetooth_hci_model_reference/P174_bt_hci_cp_user_passkey_reply_结构体.md#a56dbb4a858ecbf36eee61e24ed3742cf)
- [bt_hci_cp_user_passkey_reply::passkey](../bluetooth_hci_model_reference/P174_bt_hci_cp_user_passkey_reply_结构体.md#a80483025a32f37e7f75b3a220d48148c)
- [bt_hci_cp_write_auth_payload_timeout::auth_payload_timeout](../bluetooth_hci_model_reference/P184_bt_hci_cp_write_auth_payload_timeout_结构体.md#a385c88012b09ec561b9ba7edaadeb574)
- [bt_hci_cp_write_auth_payload_timeout::handle](../bluetooth_hci_model_reference/P184_bt_hci_cp_write_auth_payload_timeout_结构体.md#ad99d5b9f416f11492ac0f412b400aeb6)
- [bt_hci_cp_write_class_of_device::class_of_device](../bluetooth_hci_model_reference/P185_bt_hci_cp_write_class_of_device_结构体.md#acc3b940de1a5da095e8a4f18e69229f2)
- [bt_hci_cp_write_conn_accept_timeout::conn_accept_timeout](../bluetooth_hci_model_reference/P186_bt_hci_cp_write_conn_accept_timeout_结构体.md#a13de5f88920c6a41dafa598734b7acf9)
- [bt_hci_cp_write_current_iac_lap::num_current_iac](../bluetooth_hci_model_reference/P187_bt_hci_cp_write_current_iac_lap_结构体.md#aaaf3e9c66729a3b4081abb5f8a954108)
- [bt_hci_cp_write_current_iac_lap::lap](../bluetooth_hci_model_reference/P187_bt_hci_cp_write_current_iac_lap_结构体.md#ad44e9a0d65bc5140e313176f5b98e932)
- [bt_hci_cp_write_default_link_policy_settings::default_link_policy_settings](../bluetooth_hci_model_reference/P188_bt_hci_cp_write_default_link_policy_settings_结构体.md#a644c1ef9ba45ee0675824628fcb9e88a)
- [bt_hci_cp_write_ext_inquiry_response::fec_required](../bluetooth_hci_model_reference/P189_bt_hci_cp_write_ext_inquiry_response_结构体.md#a755167d683df6c408de57122847bfce0)
- [bt_hci_cp_write_ext_inquiry_response::eir](../bluetooth_hci_model_reference/P189_bt_hci_cp_write_ext_inquiry_response_结构体.md#ae9c89c1f4cac0f16d41b926dc6abc898)
- [bt_hci_cp_write_inquiry_mode::mode](../bluetooth_hci_model_reference/P190_bt_hci_cp_write_inquiry_mode_结构体.md#a827e138b7faaec54ec84a1cc1e0c480f)
- [bt_hci_cp_write_inquiry_scan_activity::window](../bluetooth_hci_model_reference/P191_bt_hci_cp_write_inquiry_scan_activity_结构体.md#aca01d404676b965f2a03ae16080b8fae)
- [bt_hci_cp_write_inquiry_scan_activity::interval](../bluetooth_hci_model_reference/P191_bt_hci_cp_write_inquiry_scan_activity_结构体.md#affe95468faed405a95073b5ba811a053)
- [bt_hci_cp_write_inquiry_scan_type::type](../bluetooth_hci_model_reference/P192_bt_hci_cp_write_inquiry_scan_type_结构体.md#a6342e77d0c83c1b7c8fd3bd1eeddf8b4)
- [bt_hci_cp_write_le_host_supp::le](../bluetooth_hci_model_reference/P193_bt_hci_cp_write_le_host_supp_结构体.md#ace1838a80b6061231b536f36e8999ac0)
- [bt_hci_cp_write_le_host_supp::simul](../bluetooth_hci_model_reference/P193_bt_hci_cp_write_le_host_supp_结构体.md#ad2c27c0f98b2334490022e90563e1271)
- [bt_hci_cp_write_link_policy_settings::link_policy_settings](../bluetooth_hci_model_reference/P194_bt_hci_cp_write_link_policy_settings_结构体.md#a1ba4bd293579e0175efff88429ca1aec)
- [bt_hci_cp_write_link_policy_settings::handle](../bluetooth_hci_model_reference/P194_bt_hci_cp_write_link_policy_settings_结构体.md#af3ed335fb8a8774c19ee024c2750e6dc)
- [bt_hci_cp_write_link_supervision_timeout::handle](../bluetooth_hci_model_reference/P195_bt_hci_cp_write_link_supervision_timeout_结构体.md#a1f33613e27db275806eaaa909591e882)
- [bt_hci_cp_write_link_supervision_timeout::timeout](../bluetooth_hci_model_reference/P195_bt_hci_cp_write_link_supervision_timeout_结构体.md#a2dd05ca57e20ee4b4fbe2b29cc746bee)
- [bt_hci_cp_write_page_scan_activity::window](../bluetooth_hci_model_reference/P196_bt_hci_cp_write_page_scan_activity_结构体.md#a8047c7b908154b23985c95a1d792007a)
- [bt_hci_cp_write_page_scan_activity::interval](../bluetooth_hci_model_reference/P196_bt_hci_cp_write_page_scan_activity_结构体.md#a9b73713d2960e78a7d6cf1a96c611495)
- [bt_hci_cp_write_page_scan_type::type](../bluetooth_hci_model_reference/P197_bt_hci_cp_write_page_scan_type_结构体.md#a1717b5ec6e83966e8ef4b61d2ee903a6)
- [bt_hci_cp_write_sc_host_supp::sc_support](../bluetooth_hci_model_reference/P198_bt_hci_cp_write_sc_host_supp_结构体.md#a48ef951f4de05c5772be5c08edca7cec)
- [bt_hci_cp_write_ssp_mode::mode](../bluetooth_hci_model_reference/P199_bt_hci_cp_write_ssp_mode_结构体.md#a8ebf7f7890adec53aa8c2307d2b1a33f)
- [bt_hci_evt_auth_complete::handle](../bluetooth_hci_model_reference/P203_bt_hci_evt_auth_complete_结构体.md#a7a78803e156218f138866fbb13fdadce)
- [bt_hci_evt_auth_complete::status](../bluetooth_hci_model_reference/P203_bt_hci_evt_auth_complete_结构体.md#ae2b4b5bcc7195247626004d46ee22dd5)
- [bt_hci_evt_auth_payload_timeout_exp::handle](../bluetooth_hci_model_reference/P204_bt_hci_evt_auth_payload_timeout_exp_结构体.md#a799bc3c63fe5083d61d8bf152ef4cee7)
- [bt_hci_evt_cc_status::status](../bluetooth_hci_model_reference/P205_bt_hci_evt_cc_status_结构体.md#a97cceaa218700da9b529ebadbb08c42c)
- [bt_hci_evt_cmd_complete::opcode](../bluetooth_hci_model_reference/P206_bt_hci_evt_cmd_complete_结构体.md#a3e61d980b4fa3084d3c50ead735fb76d)
- [bt_hci_evt_cmd_complete::ncmd](../bluetooth_hci_model_reference/P206_bt_hci_evt_cmd_complete_结构体.md#a4da0539f81057722c8c322685bc12a40)
- [bt_hci_evt_cmd_status::opcode](../bluetooth_hci_model_reference/P207_bt_hci_evt_cmd_status_结构体.md#a34002b693dc201083be4be77cfddcdb5)
- [bt_hci_evt_cmd_status::ncmd](../bluetooth_hci_model_reference/P207_bt_hci_evt_cmd_status_结构体.md#aed690e1cea2411df167e66cfaa742639)
- [bt_hci_evt_cmd_status::status](../bluetooth_hci_model_reference/P207_bt_hci_evt_cmd_status_结构体.md#aedd1560409005dbce409b892af1e3edf)
- [bt_hci_evt_conn_complete::status](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md#a3dbf4fef53279003b7304ffee4a55e56)
- [bt_hci_evt_conn_complete::bdaddr](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md#a60a2ca6a8f16e4562c12b369685efa9b)
- [bt_hci_evt_conn_complete::encr_enabled](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md#a975617e8b568675a3ed8883cbe411557)
- [bt_hci_evt_conn_complete::handle](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md#ad8877912008ea7445a67abc43aab5021)
- [bt_hci_evt_conn_complete::link_type](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md#afd9a21adf7d35205fb7e222c2e9e0328)
- [bt_hci_evt_conn_pkt_type_changed::packet_type](../bluetooth_hci_model_reference/P209_bt_hci_evt_conn_pkt_type_changed_结构体.md#aa78e454d08e7c76b3e22242c4855ee62)
- [bt_hci_evt_conn_pkt_type_changed::status](../bluetooth_hci_model_reference/P209_bt_hci_evt_conn_pkt_type_changed_结构体.md#aabad2dfce94a19a83a5f52e334da18f8)
- [bt_hci_evt_conn_pkt_type_changed::handle](../bluetooth_hci_model_reference/P209_bt_hci_evt_conn_pkt_type_changed_结构体.md#abde9bbcf2afa3c9a49662aa8192de868)
- [bt_hci_evt_conn_request::bdaddr](../bluetooth_hci_model_reference/P210_bt_hci_evt_conn_request_结构体.md#a03a2ee7ff7754173dff0809e4ebce9e6)
- [bt_hci_evt_conn_request::dev_class](../bluetooth_hci_model_reference/P210_bt_hci_evt_conn_request_结构体.md#a6059d7c56f45d2fe047a7324db1e820d)
- [bt_hci_evt_conn_request::link_type](../bluetooth_hci_model_reference/P210_bt_hci_evt_conn_request_结构体.md#ae11d550701f64717a7d6df5c89b92d0e)
- [bt_hci_evt_data_buf_overflow::link_type](../bluetooth_hci_model_reference/P211_bt_hci_evt_data_buf_overflow_结构体.md#ae0201e03ebb9b9b33e9eae593a56355f)
- [bt_hci_evt_disconn_complete::reason](../bluetooth_hci_model_reference/P212_bt_hci_evt_disconn_complete_结构体.md#a172554fbacf7aaa4dfbafe58b60fa5e6)
- [bt_hci_evt_disconn_complete::handle](../bluetooth_hci_model_reference/P212_bt_hci_evt_disconn_complete_结构体.md#ab75f198a6495ad02a00bb3df99ab4258)
- [bt_hci_evt_disconn_complete::status](../bluetooth_hci_model_reference/P212_bt_hci_evt_disconn_complete_结构体.md#aed22ac781e9d70d11e7ebbe6f2e063bd)
- [bt_hci_evt_encrypt_change::encrypt](../bluetooth_hci_model_reference/P213_bt_hci_evt_encrypt_change_结构体.md#a61cc0e3c209acbb289d071515b44860a)
- [bt_hci_evt_encrypt_change::handle](../bluetooth_hci_model_reference/P213_bt_hci_evt_encrypt_change_结构体.md#a7737f659115ca602c1224c364a4c7404)
- [bt_hci_evt_encrypt_change::status](../bluetooth_hci_model_reference/P213_bt_hci_evt_encrypt_change_结构体.md#af063bbd28d29edbcc81e907631167de7)
- [bt_hci_evt_encrypt_key_refresh_complete::handle](../bluetooth_hci_model_reference/P214_bt_hci_evt_encrypt_key_refresh_complete_结构体.md#af5562687a4f6e3a1e82cd1a81cec5ad6)
- [bt_hci_evt_encrypt_key_refresh_complete::status](../bluetooth_hci_model_reference/P214_bt_hci_evt_encrypt_key_refresh_complete_结构体.md#afdd162cff0f1eedfe9e8ee7223b3226e)
- [bt_hci_evt_extended_inquiry_result::eir](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#a1eba2841941f7cdbb00f548ebf0485e9)
- [bt_hci_evt_extended_inquiry_result::rssi](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#a21f7f48422bcfb867c9ca2e4411a2fbd)
- [bt_hci_evt_extended_inquiry_result::clock_offset](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#a30c5586d954585006238e8c2b33a7601)
- [bt_hci_evt_extended_inquiry_result::num_reports](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#a76e4e82d1dedaee94bd730a4134d7d77)
- [bt_hci_evt_extended_inquiry_result::addr](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#a955a7d36736badfae1f39fa9eda61ebb)
- [bt_hci_evt_extended_inquiry_result::cod](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#ab4ebcf09817827d1d10ddeee13832759)
- [bt_hci_evt_extended_inquiry_result::reserved](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#ab6ec4b5efe058e225d173cbda9a16f2e)
- [bt_hci_evt_extended_inquiry_result::pscan_rep_mode](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md#aba4aac84e23ca9d283cb8af265dcaf0d)
- [bt_hci_evt_hardware_error::hardware_code](../bluetooth_hci_model_reference/P216_bt_hci_evt_hardware_error_结构体.md#ab7be990e7cc32df43a3c976cb922e333)
- [bt_hci_evt_hdr::len](../bluetooth_hci_model_reference/P217_bt_hci_evt_hdr_结构体.md#a2d580a0c12b29d23002ee9d494c9e16d)
- [bt_hci_evt_hdr::data](../bluetooth_hci_model_reference/P217_bt_hci_evt_hdr_结构体.md#a87654d507f7ce633a804299bff13abe2)
- [bt_hci_evt_hdr::evt](../bluetooth_hci_model_reference/P217_bt_hci_evt_hdr_结构体.md#aba3aca89bfbe7e8cbd144765cb20fcea)
- [bt_hci_evt_inquiry_complete::status](../bluetooth_hci_model_reference/P218_bt_hci_evt_inquiry_complete_结构体.md#aa8c1e8dc9807476f4759a3b3648b6332)
- [bt_hci_evt_inquiry_result_with_rssi::reserved](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#a09914ee9998c0b59cb35ed74d08aa4f2)
- [bt_hci_evt_inquiry_result_with_rssi::pscan_rep_mode](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#a0a5c188d0d40b4259cbeb613c0dd12cf)
- [bt_hci_evt_inquiry_result_with_rssi::clock_offset](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#a1ee08f85103581994a88345cc94d7494)
- [bt_hci_evt_inquiry_result_with_rssi::rssi](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#a6d19e6400d7015db7122516e570d7989)
- [bt_hci_evt_inquiry_result_with_rssi::cod](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#ad9b4920e2864ed8350de038dffe64574)
- [bt_hci_evt_inquiry_result_with_rssi::addr](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md#af955dd1660f83e41e6d1b2b5aecf8133)
- [bt_hci_evt_io_capa_req::bdaddr](../bluetooth_hci_model_reference/P220_bt_hci_evt_io_capa_req_结构体.md#a52412f7bd8f8dea391904b9f2444b50a)
- [bt_hci_evt_io_capa_resp::authentication](../bluetooth_hci_model_reference/P221_bt_hci_evt_io_capa_resp_结构体.md#a160cb3aea96bf698520e11673a40b2d7)
- [bt_hci_evt_io_capa_resp::capability](../bluetooth_hci_model_reference/P221_bt_hci_evt_io_capa_resp_结构体.md#a851eae620ad90067957d4dec2f04efbe)
- [bt_hci_evt_io_capa_resp::oob_data](../bluetooth_hci_model_reference/P221_bt_hci_evt_io_capa_resp_结构体.md#ab12325d1536fe6a75d0a137bea301e8f)
- [bt_hci_evt_io_capa_resp::bdaddr](../bluetooth_hci_model_reference/P221_bt_hci_evt_io_capa_resp_结构体.md#adac9c9f3999099fd460651e3b012fd0f)
- [bt_hci_evt_le_adv_set_terminated::num_completed_ext_adv_evts](../bluetooth_hci_model_reference/P222_bt_hci_evt_le_adv_set_terminated_结构体.md#a192f13d6223e437261a225e6b28d04db)
- [bt_hci_evt_le_adv_set_terminated::status](../bluetooth_hci_model_reference/P222_bt_hci_evt_le_adv_set_terminated_结构体.md#a583409e2dc912af2bd5e83124fce3a72)
- [bt_hci_evt_le_adv_set_terminated::conn_handle](../bluetooth_hci_model_reference/P222_bt_hci_evt_le_adv_set_terminated_结构体.md#af2503ee8e1c9add6927fa65b69c48551)
- [bt_hci_evt_le_adv_set_terminated::adv_handle](../bluetooth_hci_model_reference/P222_bt_hci_evt_le_adv_set_terminated_结构体.md#af35564406269144cfa2532cd510aa0bd)
- [bt_hci_evt_le_advertising_info::length](../bluetooth_hci_model_reference/P223_bt_hci_evt_le_advertising_info_结构体.md#a11c223103bf89300bd90cb8725746121)
- [bt_hci_evt_le_advertising_info::addr](../bluetooth_hci_model_reference/P223_bt_hci_evt_le_advertising_info_结构体.md#a1d6863f1a601a2df9d772e3cc1fec118)
- [bt_hci_evt_le_advertising_info::evt_type](../bluetooth_hci_model_reference/P223_bt_hci_evt_le_advertising_info_结构体.md#a5943685ccd3491a883ba9450f700bb86)
- [bt_hci_evt_le_advertising_info::data](../bluetooth_hci_model_reference/P223_bt_hci_evt_le_advertising_info_结构体.md#af7d9d720ca67714f2a809e2530a1ff98)
- [bt_hci_evt_le_advertising_report::adv_info](../bluetooth_hci_model_reference/P224_bt_hci_evt_le_advertising_report_结构体.md#a9762be19de1f24be4d4626e7e2f8205d)
- [bt_hci_evt_le_advertising_report::num_reports](../bluetooth_hci_model_reference/P224_bt_hci_evt_le_advertising_report_结构体.md#ac69aab36aa421630357e4c6706c13e75)
- [bt_hci_evt_le_big_complete::irc](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a07163dee904412d6d8faca8563a944d9)
- [bt_hci_evt_le_big_complete::iso_interval](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a0b0d19d442ed8f1025165c435786ba09)
- [bt_hci_evt_le_big_complete::big_handle](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a14eaa705f1df38337722a41e8189f807)
- [bt_hci_evt_le_big_complete::bn](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a2327e42013033767af233d1c2c3acc56)
- [bt_hci_evt_le_big_complete::latency](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a2727d329c37e3b3644cfad02d86abb55)
- [bt_hci_evt_le_big_complete::sync_delay](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a2847d5fc997f80a3e21b7e03d80c9574)
- [bt_hci_evt_le_big_complete::pto](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a6c295870732d65002ec21b4b607e7c0b)
- [bt_hci_evt_le_big_complete::max_pdu](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a8b433ac376e347bf391d4dd804c469f3)
- [bt_hci_evt_le_big_complete::num_bis](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#a995c8fe06ec087f16b771c38171745b1)
- [bt_hci_evt_le_big_complete::phy](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#abfa6d6bc135350737451e053aa7d212c)
- [bt_hci_evt_le_big_complete::status](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#ad6787806a3622b3bd3da4512bb8ddffe)
- [bt_hci_evt_le_big_complete::nse](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#ae77364aafe179588f7b8414292e35f5e)
- [bt_hci_evt_le_big_complete::handle](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md#af1c8bd66c3dba70df22f8655b4f27925)
- [bt_hci_evt_le_big_sync_established::max_pdu](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a13db0d402636a71ed029575c1e5771c5)
- [bt_hci_evt_le_big_sync_established::num_bis](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a2fa405310a8fed0341001b316ca7bd4f)
- [bt_hci_evt_le_big_sync_established::big_handle](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a31a05f8afb69e5885700cc4ad3b161b2)
- [bt_hci_evt_le_big_sync_established::nse](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a383dc92f6d16ec971455e20665cd7496)
- [bt_hci_evt_le_big_sync_established::bn](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a451466916fbe2f220c277b4b4e62241d)
- [bt_hci_evt_le_big_sync_established::handle](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a48766968cb677614f525ea36551ad6c8)
- [bt_hci_evt_le_big_sync_established::iso_interval](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a610313c11c65faf82e06a121affb8b2b)
- [bt_hci_evt_le_big_sync_established::pto](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a6b750de25b2a1afc38995030953364ce)
- [bt_hci_evt_le_big_sync_established::status](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#a8feb21ef6eacf45dfc09b09e0bce04b1)
- [bt_hci_evt_le_big_sync_established::latency](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#aebb25f9a63fa013ec6ef891ca498dbb4)
- [bt_hci_evt_le_big_sync_established::irc](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md#afd52315dafe02ee28bc26f058b12fe9e)
- [bt_hci_evt_le_big_sync_lost::reason](../bluetooth_hci_model_reference/P227_bt_hci_evt_le_big_sync_lost_结构体.md#a02b724a60e71805088aefca9989ad878)
- [bt_hci_evt_le_big_sync_lost::big_handle](../bluetooth_hci_model_reference/P227_bt_hci_evt_le_big_sync_lost_结构体.md#ae59a9c18363f7aee67563494d98aa971)
- [bt_hci_evt_le_big_terminate::reason](../bluetooth_hci_model_reference/P228_bt_hci_evt_le_big_terminate_结构体.md#a0303ac64b825f93210dfc70a8a081ea6)
- [bt_hci_evt_le_big_terminate::big_handle](../bluetooth_hci_model_reference/P228_bt_hci_evt_le_big_terminate_结构体.md#ad9c9e6d42661366d62d79163fa9ad1c7)
- [bt_hci_evt_le_biginfo_adv_report::max_sdu](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a084c13c4b0c9c8dca0653b56e53a0c74)
- [bt_hci_evt_le_biginfo_adv_report::max_pdu](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a12a000c049e85d2b24720d1a362d28df)
- [bt_hci_evt_le_biginfo_adv_report::phy](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a2301112acf22cf68d6495ff85f0f29bf)
- [bt_hci_evt_le_biginfo_adv_report::sdu_interval](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a81e236ceb24012bc267f656f20f1f8c4)
- [bt_hci_evt_le_biginfo_adv_report::sync_handle](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a8be20bfc607e6ce34ea75c53e285b0d5)
- [bt_hci_evt_le_biginfo_adv_report::irc](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#a9c1235653245b517a105570c60ddfa09)
- [bt_hci_evt_le_biginfo_adv_report::framing](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#abe0636beae2f51004193ad5f7c9efeef)
- [bt_hci_evt_le_biginfo_adv_report::bn](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#ada35f690706be1c6ee8f40787bbe53e5)
- [bt_hci_evt_le_biginfo_adv_report::nse](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#ae28d5378a7e2ef59fabb62a3a430ccc8)
- [bt_hci_evt_le_biginfo_adv_report::encryption](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#ae63eaf93f728109b5fb77ca3179ba99c)
- [bt_hci_evt_le_biginfo_adv_report::num_bis](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#ae68f803bbc3f06e7190f62be98d2fe66)
- [bt_hci_evt_le_biginfo_adv_report::iso_interval](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#ae92b69ab0bc257d4f50b98e071c6038b)
- [bt_hci_evt_le_biginfo_adv_report::pto](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md#af3a871d3de34b90fc2b09b0725caf479)
- [bt_hci_evt_le_chan_sel_algo::handle](../bluetooth_hci_model_reference/P230_bt_hci_evt_le_chan_sel_algo_结构体.md#a16393279e08073dad549e111e610c8e8)
- [bt_hci_evt_le_chan_sel_algo::chan_sel_algo](../bluetooth_hci_model_reference/P230_bt_hci_evt_le_chan_sel_algo_结构体.md#a976a62e81b094a59ce42cb6ad3ce45ac)
- [bt_hci_evt_le_cis_established_v2::status](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a1f43b72368227f212511bb248b4a0e22)
- [bt_hci_evt_le_cis_established_v2::p_latency](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a26b25e1615991977735cbfc679d747f3)
- [bt_hci_evt_le_cis_established_v2::p_max_sdu](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a2a060c0bb2831eb3df0dc8ffb74ecebd)
- [bt_hci_evt_le_cis_established_v2::c_ft](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a2de704a032ac2379528991f2d01e6979)
- [bt_hci_evt_le_cis_established_v2::sub_interval](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a353409fe069aba91c5372ee8ae6e1b79)
- [bt_hci_evt_le_cis_established_v2::p_ft](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a3b1fc27cca2bc85c36e257aabd8ea612)
- [bt_hci_evt_le_cis_established_v2::p_phy](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a5a0b08098ac4e6ec93a6ecbbbf4ef587)
- [bt_hci_evt_le_cis_established_v2::c_bn](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a5f68c3cba98ed96afef0949f6b14ded9)
- [bt_hci_evt_le_cis_established_v2::p_bn](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a64b48b20283415100fc8bdf33edf2b0e)
- [bt_hci_evt_le_cis_established_v2::interval](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a71762f8a31e20b233a252ac974f6d329)
- [bt_hci_evt_le_cis_established_v2::cig_sync_delay](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a754ad7e68821da0bdb8da0bdeb3b4697)
- [bt_hci_evt_le_cis_established_v2::conn_handle](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a7a7b8303183a916225bb0a3ea11d5480)
- [bt_hci_evt_le_cis_established_v2::c_sdu_interval](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a926a5faeb98a99333310d860da37f6f5)
- [bt_hci_evt_le_cis_established_v2::c_phy](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#a9b7ba96597a5131927e365b7a45f8d6f)
- [bt_hci_evt_le_cis_established_v2::nse](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#ac3a87b20b2f10e980639d232a013f702)
- [bt_hci_evt_le_cis_established_v2::c_max_pdu](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#acd8cf2d2d85b65d839256f3412a4bb43)
- [bt_hci_evt_le_cis_established_v2::p_sdu_interval](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#acf30d6a745803fd4e984d66548ceff58)
- [bt_hci_evt_le_cis_established_v2::c_max_sdu](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#ad054af39ddad854423379b3cc7aafc26)
- [bt_hci_evt_le_cis_established_v2::c_latency](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#ae580ff8c0ef4cd03365cbf1a06aed8bc)
- [bt_hci_evt_le_cis_established_v2::p_max_pdu](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#aeea230245aa75dd7f44bf5a4a286e9a5)
- [bt_hci_evt_le_cis_established_v2::cis_sync_delay](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#af134783424a77274abac44613bf61264)
- [bt_hci_evt_le_cis_established_v2::framing](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md#af59ca6d54ca770ef8334ea091bcc53f6)
- [bt_hci_evt_le_cis_established::interval](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a0bcdc0d8b3b776660d2e51427f9634dd)
- [bt_hci_evt_le_cis_established::p_ft](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a200afaff044b9eea653d8aee13297dc2)
- [bt_hci_evt_le_cis_established::p_phy](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a25b84cf026775b582c7944e265ffb0b2)
- [bt_hci_evt_le_cis_established::status](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a4d90dbeda130a6142ff0b7f9e2ee7c16)
- [bt_hci_evt_le_cis_established::c_phy](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a53ea1da3f31313ab73b511c72912bd33)
- [bt_hci_evt_le_cis_established::nse](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a683856418764b1110d5c5fea0494fe1e)
- [bt_hci_evt_le_cis_established::c_latency](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a877913bb4b9016c64793458de94d84a0)
- [bt_hci_evt_le_cis_established::conn_handle](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#a932e8df0222eb3bcf7bee753414d529e)
- [bt_hci_evt_le_cis_established::c_bn](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ab6b2d892e3c1e4f6aedee722049b75d3)
- [bt_hci_evt_le_cis_established::cig_sync_delay](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ac4e5a2535e3e8d3782adac63a4c5a8d9)
- [bt_hci_evt_le_cis_established::p_bn](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ad0a79bfadd413bf572b697069695c0a5)
- [bt_hci_evt_le_cis_established::c_ft](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ad0f3bd5f81b660afbc4927a777c2c18e)
- [bt_hci_evt_le_cis_established::cis_sync_delay](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ae71d6753849ae3c57327c8763cab1802)
- [bt_hci_evt_le_cis_established::p_max_pdu](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ae8b195f433570e28e42a5f9d321964de)
- [bt_hci_evt_le_cis_established::c_max_pdu](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#ae9fdecff4342f25de30165a4531ad703)
- [bt_hci_evt_le_cis_established::p_latency](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md#aefb2d4e0458cbe990903a9f449189c30)
- [bt_hci_evt_le_cis_req::cis_id](../bluetooth_hci_model_reference/P233_bt_hci_evt_le_cis_req_结构体.md#abdf99eeb7a30c8238bbabdcd60a4847a)
- [bt_hci_evt_le_cis_req::cig_id](../bluetooth_hci_model_reference/P233_bt_hci_evt_le_cis_req_结构体.md#ae0ef0ac224bde55de13df4e5eeaf26be)
- [bt_hci_evt_le_cis_req::cis_handle](../bluetooth_hci_model_reference/P233_bt_hci_evt_le_cis_req_结构体.md#aeed6f4bf58cdb301d6b784a202722acc)
- [bt_hci_evt_le_cis_req::acl_handle](../bluetooth_hci_model_reference/P233_bt_hci_evt_le_cis_req_结构体.md#af8529013adb87340298a89d4727e6867)
- [bt_hci_evt_le_conn_complete::clock_accuracy](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a3fff4c3b30da5922f75d36d97fdeee33)
- [bt_hci_evt_le_conn_complete::supv_timeout](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a4a90c9824d167b6c45b301e18bfe7f17)
- [bt_hci_evt_le_conn_complete::handle](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a67618a1efa0149fadc1063a719d5b674)
- [bt_hci_evt_le_conn_complete::role](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a8455e714d4333d90c2f117892f3dcd6f)
- [bt_hci_evt_le_conn_complete::status](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a897981117139c0e53ea7275b689f3799)
- [bt_hci_evt_le_conn_complete::peer_addr](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#a97e1aaa10832292ddfe4ee6731ef8999)
- [bt_hci_evt_le_conn_complete::latency](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#ab60cb42ecc83632c61656cd352b71cbe)
- [bt_hci_evt_le_conn_complete::interval](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md#abe4bc0407d0295329631cb14672a7ee7)
- [bt_hci_evt_le_conn_param_req::interval_max](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md#a0ed70d1a89f270073f78823d38af6ac9)
- [bt_hci_evt_le_conn_param_req::handle](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md#a4746a001a070f152a3c1c870a7e74df1)
- [bt_hci_evt_le_conn_param_req::interval_min](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md#a9a9dfc026feb46337b0a36920204b24e)
- [bt_hci_evt_le_conn_param_req::latency](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md#a9f61f0a3e6b6d2e2c6af2f4aef625b75)
- [bt_hci_evt_le_conn_param_req::timeout](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md#ae34de4a3d3e3e4686391eb9d9585dc87)
- [bt_hci_evt_le_conn_rate_change::continuation_number](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a10671dd6e9b30b112e5841c482ee3067)
- [bt_hci_evt_le_conn_rate_change::subrate_factor](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a29d6bdbf04cb6bc68a84f3fafaf66a1f)
- [bt_hci_evt_le_conn_rate_change::supervision_timeout](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a3028aa8284c2f656f71d4b25da862cc9)
- [bt_hci_evt_le_conn_rate_change::conn_interval](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a31deb63251c897f7627b67c7cad2521f)
- [bt_hci_evt_le_conn_rate_change::handle](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a5b3947e67027b5425c21a0d509e19dc5)
- [bt_hci_evt_le_conn_rate_change::peripheral_latency](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a67429e04fe601f367deeb5637d7d89c9)
- [bt_hci_evt_le_conn_rate_change::status](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md#a8ad1a15c8b26be65d92944b4fc3c0ae1)
- [bt_hci_evt_le_conn_update_complete::interval](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md#a69aa00c0c50978b2aa620aad671119f3)
- [bt_hci_evt_le_conn_update_complete::handle](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md#a81c0688a5e3b4b3a4d92fbc756a068d5)
- [bt_hci_evt_le_conn_update_complete::supv_timeout](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md#aca728975619a10a6e3280b127b59f2f1)
- [bt_hci_evt_le_conn_update_complete::status](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md#ad428bd5e29d40f7551ccdd0747e429d6)
- [bt_hci_evt_le_conn_update_complete::latency](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md#ade2421709a35e0cd0fce3a4d992470c3)
- [bt_hci_evt_le_connection_iq_report::cte_type](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a0188ce28a6c0a2002ae2c64a7bd95e52)
- [bt_hci_evt_le_connection_iq_report::rssi_ant_id](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a135498a4abae604967f94840e2f88d2c)
- [bt_hci_evt_le_connection_iq_report::conn_evt_counter](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a1f388ba96bd52f9ce0f68bacb2945ed8)
- [bt_hci_evt_le_connection_iq_report::conn_handle](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a446f4eab3db19452a84023a676333d1d)
- [bt_hci_evt_le_connection_iq_report::rssi](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a49e63523f7219174540666c7e5ab3550)
- [bt_hci_evt_le_connection_iq_report::sample](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a5acc2683312523a1137db7897a7373a6)
- [bt_hci_evt_le_connection_iq_report::slot_durations](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a74670ca77bb2be81db2cee613dd9c82b)
- [bt_hci_evt_le_connection_iq_report::sample_count](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#a801dd9373935ba06175ac52237fea759)
- [bt_hci_evt_le_connection_iq_report::rx_phy](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#aa052e03491647acc9f7a6dc7d91cedcc)
- [bt_hci_evt_le_connection_iq_report::data_chan_idx](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#ac01a14c591c8bd8e6313aff021ca8d61)
- [bt_hci_evt_le_connection_iq_report::packet_status](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md#af66e8f09a4442b658b80a6eb4dd3064b)
- [bt_hci_evt_le_connectionless_iq_report::rssi](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a09112f3711aca00b56045c46958c0992)
- [bt_hci_evt_le_connectionless_iq_report::sample](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a1a81f2c8653d85dc29582eed67b4a2a8)
- [bt_hci_evt_le_connectionless_iq_report::sync_handle](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a36f853d29b8dae1dd393546bbdec5ae2)
- [bt_hci_evt_le_connectionless_iq_report::sample_count](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a39109ea3f657d0566a73c7ca81bdd2b1)
- [bt_hci_evt_le_connectionless_iq_report::cte_type](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a6b11b00199b002129c569cfec6e83174)
- [bt_hci_evt_le_connectionless_iq_report::slot_durations](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#a9d9f0cfe343d81c44e8342b81e2a0608)
- [bt_hci_evt_le_connectionless_iq_report::packet_status](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#ab6fb0f6e32e32a3364ae79d867d9e640)
- [bt_hci_evt_le_connectionless_iq_report::per_evt_counter](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#abfeb0aaa411464bbd7bca927219144fb)
- [bt_hci_evt_le_connectionless_iq_report::chan_idx](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#af50e710884a17191d22f652eaf5788fd)
- [bt_hci_evt_le_connectionless_iq_report::rssi_ant_id](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md#af8c2055666a97f3c8d95747c59515c31)
- [bt_hci_evt_le_cs_config_complete::main_mode_type](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a14f4c29a7f84463f048364389341c7b5)
- [bt_hci_evt_le_cs_config_complete::channel_map_repetition](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a1e5ba3ebb5dcac2105a0f859683505bc)
- [bt_hci_evt_le_cs_config_complete::min_main_mode_steps](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a21928853b505764e64fcc9190905b12c)
- [bt_hci_evt_le_cs_config_complete::cs_enhancements_1](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a45a1b908385be6a5289698dd08d8a610)
- [bt_hci_evt_le_cs_config_complete::handle](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a511021f717538d4ae25eb28ad82c5f99)
- [bt_hci_evt_le_cs_config_complete::config_id](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a544b3480034087ca01d64a41c1c4b8f9)
- [bt_hci_evt_le_cs_config_complete::sub_mode_type](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a55789928018a6124d87e76709b1b77d9)
- [bt_hci_evt_le_cs_config_complete::ch3c_jump](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a5f886c16acd561e143a8796fcc1ea5af)
- [bt_hci_evt_le_cs_config_complete::role](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a6f84ebf8a34a830ced1fc738d46fe244)
- [bt_hci_evt_le_cs_config_complete::mode_0_steps](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a705a7be2d5ce02c4d78319f4f842b87e)
- [bt_hci_evt_le_cs_config_complete::ch3c_shape](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a73bd134e9337a9a47e41bba04623ee0b)
- [bt_hci_evt_le_cs_config_complete::action](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a748fcb3cbd396851a3d159887b12b3e0)
- [bt_hci_evt_le_cs_config_complete::t_fcs_time](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a7aa0fd8a1c9c7270059725416dd0a90f)
- [bt_hci_evt_le_cs_config_complete::t_pm_time](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a7d64425b6aa44b01332ce6fac7813471)
- [bt_hci_evt_le_cs_config_complete::main_mode_repetition](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a7fe1af954bae025b9b8bbef70bd1c60e)
- [bt_hci_evt_le_cs_config_complete::t_ip2_time](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a8fafd0e139a9c85830468e5a056c42b7)
- [bt_hci_evt_le_cs_config_complete::max_main_mode_steps](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#a9b14655fa6bb3c7ac43561a399019a76)
- [bt_hci_evt_le_cs_config_complete::channel_selection_type](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#aa323b4a74f7fce33e884d0c32e4014d0)
- [bt_hci_evt_le_cs_config_complete::channel_map](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#abcf0c43f33a85bcd860323212d57ce5b)
- [bt_hci_evt_le_cs_config_complete::cs_sync_phy](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#ad0454e31d55ec25a21bc272cae999238)
- [bt_hci_evt_le_cs_config_complete::rtt_type](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#ae64ff5dbd9d704c3a7f4c5b98ada399c)
- [bt_hci_evt_le_cs_config_complete::status](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#ae94aa8c92a8d4b33213adc8fc029a02d)
- [bt_hci_evt_le_cs_config_complete::t_ip1_time](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md#afd62b1ffe5388c7f094cb086da4c86ba)
- [bt_hci_evt_le_cs_procedure_enable_complete::config_id](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a17b62e13cda5f47dee2e8873686b978e)
- [bt_hci_evt_le_cs_procedure_enable_complete::status](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a5822ff654eee794442a05033e0f10fae)
- [bt_hci_evt_le_cs_procedure_enable_complete::tone_antenna_config_selection](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a60a9e00cba665d73e65d0ee5b0d9efbc)
- [bt_hci_evt_le_cs_procedure_enable_complete::event_interval](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a688bfcb6781b2e3480f021c66a3109fe)
- [bt_hci_evt_le_cs_procedure_enable_complete::max_procedure_len](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a7a38c8ced8720a428df42e821ec7e9e6)
- [bt_hci_evt_le_cs_procedure_enable_complete::state](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a7ff8f1e713d9b835f3a4e0e79cb1b3d1)
- [bt_hci_evt_le_cs_procedure_enable_complete::subevent_interval](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#a8f5485967662dbd1676d8edd6345fd13)
- [bt_hci_evt_le_cs_procedure_enable_complete::subevents_per_event](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#aacc14948a9e6c384ec94051fb4323599)
- [bt_hci_evt_le_cs_procedure_enable_complete::procedure_count](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#ac8489dc8ff5f9bf052a7c1a67a544106)
- [bt_hci_evt_le_cs_procedure_enable_complete::procedure_interval](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#ad7c21907a38747ec405c992ef14e8dd7)
- [bt_hci_evt_le_cs_procedure_enable_complete::handle](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#adcf8e32c2346073e0fbe273d261f6741)
- [bt_hci_evt_le_cs_procedure_enable_complete::subevent_len](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#af5959274cb88a8e4fdf09e8dd756f31c)
- [bt_hci_evt_le_cs_procedure_enable_complete::selected_tx_power](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md#afd760c9b6809e6764a652ecb3ee4c2b5)
- [bt_hci_evt_le_cs_read_remote_fae_table_complete::status](../bluetooth_hci_model_reference/P242_bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体.md#a1ee4d133955f28f45d16226730344428)
- [bt_hci_evt_le_cs_read_remote_fae_table_complete::conn_handle](../bluetooth_hci_model_reference/P242_bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体.md#adcdfbfd2d9c19be0c41121235fbb8eaa)
- [bt_hci_evt_le_cs_read_remote_fae_table_complete::remote_fae_table](../bluetooth_hci_model_reference/P242_bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体.md#ae1ca6d2d4f4305565f1d491ef202fcad)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::tx_snr_capability](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a07642a2edeb882e5c9a2a7727e8a55fd)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_sw_time_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a0c60c0b2677a8635a185277453db9613)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::roles_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a2e7d55a93000730a565c93b3394186e3)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_ip2_ipt_times_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a365c4afcf1c034bb42c24ce4bedbf1c3)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::nadm_sounding_capability](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a43a8dd8b09c9e498b64798fcfe73af53)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::rtt_random_payload_n](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a73b7054a056ca3256098608e565033b2)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_fcs_times_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a77669a86a0c75439417d4e53629a9cfd)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::status](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a8695548057df5e398f65de93fd097b04)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::nadm_random_capability](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a974007b9f1d81991f55c40cb1da1c51e)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#a9e2a36e0181a8cf5a9d61b8b31e21617)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_ip2_times_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#aa3e4e049cbb322a35171686635e2cc9c)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::modes_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#aa78b03177bbfc69de0a066f610b1cfa6)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::num_config_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ab21b4a5b2e3005fc3589251c7b8f77f1)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_ip1_times_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ab692972f1388e6641493a5cc0faf2fac)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::rtt_sounding_n](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ab93bb486d50a79c34a6002885436605b)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::rtt_capability](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#aba890de001e752b497bc91bd6356c359)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::subfeatures_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#abe01a9d4d6fdb042fdfa5c045ac66519)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::max_antenna_paths_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ac130ecc14ce78f0c179ad56a1985d60c)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::num_antennas_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ad1f03a6a550a5c5cb9b0c997c239ba6a)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_pm_times_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ad5c7c16d0b2096d4c00156800bf9181b)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::conn_handle](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#adb3ce0c00b922e72373a93cb5d0f2f1f)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::rtt_aa_only_n](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#ae8091780f4153ead9a9414593b648f5a)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_sw_ipt_time_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#af7f35ce7c16fc7cf1d76be1450d4566c)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::cs_sync_phys_supported](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md#aff9e1f081101d2eabc83a7a2ce99d64f)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::t_ip2_times_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a0a1d9dcdf184e49349e86980da2e4bed)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::cs_sync_phys_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a1f303dc3aa8a23fccde27a2d2f64d732)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::t_sw_time_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a21a322fc8efd0c410dda78e2652d506d)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::rtt_random_payload_n](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a3f275ad58ca745347172ad0b89faf2c4)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::status](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a40980265955d4d58a9b5407ff845fde4)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::t_fcs_times_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a44869fd19ae813830e38f6e4b88dbb1d)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::conn_handle](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a4f8fe99c2392c06125ba94e61aed0e6c)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::max_antenna_paths_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a50ad0408019dce16685215c6a1b6d0ef)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::nadm_random_capability](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a7af3067f319be094af31512d4ee5101e)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::rtt_sounding_n](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a7f796e2eda8d3c7eae556932e37cd93d)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::rtt_aa_only_n](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a843968ec69106d076596e110407d8a1a)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::roles_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#a99f9f7b08de6b41e88cea10ba0ca6010)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::num_config_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ab09a466b2a9a0be5f5021f1da0d7393a)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::modes_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ab7a35b1093ece7ae9cc5def4a3e473b2)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ac73a8bf5425c80739e84cb30ce94f3e7)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::subfeatures_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ac83543c17606e401d919fce841a12c6c)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::rtt_capability](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ace95740224b31c127f5e13550cb5a23a)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::t_ip1_times_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ad330adf1ae5b9b84756d36801a4cf289)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::num_antennas_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#adcf35e055d04775c444fa28655b95337)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::nadm_sounding_capability](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#adebb5328c7baeaa786bc185fec432e40)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::tx_snr_capability](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#ae3d06bce4df7a2ca07c5d6dd01124743)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::t_pm_times_supported](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md#afef9f37784d75f54521793f07b5baece)
- [bt_hci_evt_le_cs_security_enable_complete::handle](../bluetooth_hci_model_reference/P245_bt_hci_evt_le_cs_security_enable_complete_结构体.md#aaa96a8944598914e4439249ba489f726)
- [bt_hci_evt_le_cs_security_enable_complete::status](../bluetooth_hci_model_reference/P245_bt_hci_evt_le_cs_security_enable_complete_结构体.md#aaf2de8591b18cd36709f7ef755bee917)
- [bt_hci_evt_le_cs_subevent_result_continue::subevent_abort_reason](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a1801aeaac839831198e17b7d96a5532a)
- [bt_hci_evt_le_cs_subevent_result_continue::num_antenna_paths](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a2f8e1f634e28100815c881a463b51f2c)
- [bt_hci_evt_le_cs_subevent_result_continue::procedure_abort_reason](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a3c7ac056a5898710ffbc0776ef551b4b)
- [bt_hci_evt_le_cs_subevent_result_continue::procedure_done_status](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a3e5b1e8a247fff36c06447c9ff7c3bb8)
- [bt_hci_evt_le_cs_subevent_result_continue::conn_handle](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a4126bebec093f6f4d1a22b43abec6b1c)
- [bt_hci_evt_le_cs_subevent_result_continue::subevent_done_status](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#a49cf181c8518fb3015a0c54f7558aa8c)
- [bt_hci_evt_le_cs_subevent_result_continue::steps](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#abbddd0e27178e49abe6eef62bc094a16)
- [bt_hci_evt_le_cs_subevent_result_continue::config_id](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#adefb9ad1f998460a6d235ebd39bbfe4a)
- [bt_hci_evt_le_cs_subevent_result_continue::num_steps_reported](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md#af127774b52c4e088f628999136b6cd7c)
- [bt_hci_evt_le_cs_subevent_result_step::step_channel](../bluetooth_hci_model_reference/P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md#a1f074ff26f779292ea32bb405f37b877)
- [bt_hci_evt_le_cs_subevent_result_step::step_mode](../bluetooth_hci_model_reference/P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md#a65f6ecf6355883df7924067edc277f35)
- [bt_hci_evt_le_cs_subevent_result_step::step_data_length](../bluetooth_hci_model_reference/P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md#a7fb65809d78fbf08528f177d98e72f6b)
- [bt_hci_evt_le_cs_subevent_result_step::step_data](../bluetooth_hci_model_reference/P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md#aebb0c47275e4cf92802314a82ffba820)
- [bt_hci_evt_le_cs_subevent_result::start_acl_conn_event_counter](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a0d6b2ca9f148173abb6207cf7c473c7f)
- [bt_hci_evt_le_cs_subevent_result::procedure_done_status](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a27a2848009838977f26df75bfc9bc3c3)
- [bt_hci_evt_le_cs_subevent_result::config_id](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a2e8bdef7f85a4cefeaf625d0c3a4db03)
- [bt_hci_evt_le_cs_subevent_result::conn_handle](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a3b9c8392fa3aadc2e0673923e0346278)
- [bt_hci_evt_le_cs_subevent_result::steps](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a43b46a37648b9fde72634dd7dd6a68e6)
- [bt_hci_evt_le_cs_subevent_result::num_antenna_paths](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a9931d5818b801a9c36853f88b259c25e)
- [bt_hci_evt_le_cs_subevent_result::reference_power_level](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#a9a7260f63122a94cf7eb6ddc3344f742)
- [bt_hci_evt_le_cs_subevent_result::procedure_abort_reason](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#ab81c9c55697b2f2c92e3ea2073932ad1)
- [bt_hci_evt_le_cs_subevent_result::frequency_compensation](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#aba480f7ad78069fd8b83493fac42244e)
- [bt_hci_evt_le_cs_subevent_result::subevent_abort_reason](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#acf6f9c4e6fa5897be872d9953993517b)
- [bt_hci_evt_le_cs_subevent_result::procedure_counter](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#ad08558fd68eb6c43d95a3f0f62bafff0)
- [bt_hci_evt_le_cs_subevent_result::subevent_done_status](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#aeda28dfb30c51ce2955e1c313069c111)
- [bt_hci_evt_le_cs_subevent_result::num_steps_reported](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md#af8c827d508614f553b9f503d0394411b)
- [bt_hci_evt_le_cs_test_end_complete::status](../bluetooth_hci_model_reference/P249_bt_hci_evt_le_cs_test_end_complete_结构体.md#ae083dabff641736ed9a23ffc5a36a737)
- [bt_hci_evt_le_cte_req_failed::status](../bluetooth_hci_model_reference/P250_bt_hci_evt_le_cte_req_failed_结构体.md#a1433f25dee38014dbd2d061b6d75741a)
- [bt_hci_evt_le_cte_req_failed::conn_handle](../bluetooth_hci_model_reference/P250_bt_hci_evt_le_cte_req_failed_结构体.md#aa903954fa411e4ae49a613b4e76219dc)
- [bt_hci_evt_le_data_len_change::max_rx_octets](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md#a60ecd89a8bbf06ae55b577e3d708d16f)
- [bt_hci_evt_le_data_len_change::handle](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md#a62ebc2f337f23f678c651bf3a276a2a7)
- [bt_hci_evt_le_data_len_change::max_tx_time](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md#a8264e7ec4aa37e9a699f81d0c56afa40)
- [bt_hci_evt_le_data_len_change::max_rx_time](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md#a90771e400b998565e7a8bbf4288edd01)
- [bt_hci_evt_le_data_len_change::max_tx_octets](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md#ae5ce481170336acafbe85687c672281b)
- [bt_hci_evt_le_direct_adv_info::rssi](../bluetooth_hci_model_reference/P252_bt_hci_evt_le_direct_adv_info_结构体.md#a013e5d53ed53e4cd0b923a55c68e20bc)
- [bt_hci_evt_le_direct_adv_info::addr](../bluetooth_hci_model_reference/P252_bt_hci_evt_le_direct_adv_info_结构体.md#a66bbb3e53d84e8c39b216edf91ad131d)
- [bt_hci_evt_le_direct_adv_info::dir_addr](../bluetooth_hci_model_reference/P252_bt_hci_evt_le_direct_adv_info_结构体.md#ad4ca2d5395bc4c5b95527ac1491c940e)
- [bt_hci_evt_le_direct_adv_info::evt_type](../bluetooth_hci_model_reference/P252_bt_hci_evt_le_direct_adv_info_结构体.md#aed957c96860c5f92f9485ab743ce832b)
- [bt_hci_evt_le_direct_adv_report::direct_adv_info](../bluetooth_hci_model_reference/P253_bt_hci_evt_le_direct_adv_report_结构体.md#a82800d58d4c3ed1fca49b6575bd8f957)
- [bt_hci_evt_le_direct_adv_report::num_reports](../bluetooth_hci_model_reference/P253_bt_hci_evt_le_direct_adv_report_结构体.md#ae8d1f96739c8fda8827d1c0521f00f94)
- [bt_hci_evt_le_enh_conn_complete_v2::peer_rpa](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a014e8bf891684c4cd9e5ec53d986d412)
- [bt_hci_evt_le_enh_conn_complete_v2::local_rpa](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a10a1cbf0e9e21bc127dc64adadd53773)
- [bt_hci_evt_le_enh_conn_complete_v2::interval](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a237b8313970cc63b7e57c0ce4913392e)
- [bt_hci_evt_le_enh_conn_complete_v2::supv_timeout](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a2b2ac4890eb9604a3f5cd40f55c2c066)
- [bt_hci_evt_le_enh_conn_complete_v2::role](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a3343de57a24fa2ebdccf9411f388817d)
- [bt_hci_evt_le_enh_conn_complete_v2::latency](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a3daa32ac19c4eda4a49bebb64f3145be)
- [bt_hci_evt_le_enh_conn_complete_v2::clock_accuracy](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a7bb168061803d1122e8ee47dc8af3ae9)
- [bt_hci_evt_le_enh_conn_complete_v2::peer_addr](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a7df28c9ddec607d5a84572bb421b7f5a)
- [bt_hci_evt_le_enh_conn_complete_v2::sync_handle](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a81dca94a6f2a8ea3da7a5a316daa5941)
- [bt_hci_evt_le_enh_conn_complete_v2::adv_handle](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#a883ba3aed9aed00ec0ce425999d97180)
- [bt_hci_evt_le_enh_conn_complete_v2::status](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#ad72ba07d766135a94474a9d004da1a66)
- [bt_hci_evt_le_enh_conn_complete_v2::handle](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md#affe2dba0634e0215579fb13d77016a8c)
- [bt_hci_evt_le_enh_conn_complete::handle](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#a13ceff445de6a89f6ea0e832e8b3fba9)
- [bt_hci_evt_le_enh_conn_complete::peer_addr](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#a4906d6991489e95f8c74aacf5ad8c22e)
- [bt_hci_evt_le_enh_conn_complete::peer_rpa](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#a4ece4379733f1ab404fa03f4794192a4)
- [bt_hci_evt_le_enh_conn_complete::clock_accuracy](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#a5641e5cb17df4613cd85f5ad3ba8541c)
- [bt_hci_evt_le_enh_conn_complete::latency](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#a7276bf433c21ffcd3582463492af107b)
- [bt_hci_evt_le_enh_conn_complete::supv_timeout](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#aa99df131f3fb0330ff8051015d2b78dc)
- [bt_hci_evt_le_enh_conn_complete::local_rpa](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#ab275bcb4a3dd09525b446c01e4e5fdad)
- [bt_hci_evt_le_enh_conn_complete::interval](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#ac0565ecf0c459275d147933bbdaa9fbc)
- [bt_hci_evt_le_enh_conn_complete::status](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#ae26575416658bf285c45f57ddf426eb2)
- [bt_hci_evt_le_enh_conn_complete::role](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md#af24298f8c1d58882b4962a14086fc5c7)
- [bt_hci_evt_le_ext_advertising_info::evt_type](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a040c27dbcb337162f7ca857b8cb84cfe)
- [bt_hci_evt_le_ext_advertising_info::prim_phy](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a088f0e6ea0dfbad25d5f72d0741f7d6d)
- [bt_hci_evt_le_ext_advertising_info::length](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a20ca10813f6b3aaba2756a5fe00d3878)
- [bt_hci_evt_le_ext_advertising_info::direct_addr](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a37f4e4981566b43d6e7c7dfffc5b13fb)
- [bt_hci_evt_le_ext_advertising_info::tx_power](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a39217e77e495e8c4c6288917f8e4d2dc)
- [bt_hci_evt_le_ext_advertising_info::sid](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a5b4d4adff4d97c06311a76abd9847727)
- [bt_hci_evt_le_ext_advertising_info::rssi](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a6213edbc3ae30f02a6bf2d8e069cd035)
- [bt_hci_evt_le_ext_advertising_info::interval](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a7da4e49c49eccbf009491bb7da01e111)
- [bt_hci_evt_le_ext_advertising_info::data](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#a9e5536277b0132c8374147677a787b68)
- [bt_hci_evt_le_ext_advertising_info::addr](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#acec6858e41ae1b44a2a2ee6d6dbc294d)
- [bt_hci_evt_le_ext_advertising_info::sec_phy](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md#af4d863e12e6f8f19426a14af292fa6d2)
- [bt_hci_evt_le_ext_advertising_report::num_reports](../bluetooth_hci_model_reference/P257_bt_hci_evt_le_ext_advertising_report_结构体.md#a72fc9736934b415e88c51a1f96179871)
- [bt_hci_evt_le_ext_advertising_report::adv_info](../bluetooth_hci_model_reference/P257_bt_hci_evt_le_ext_advertising_report_结构体.md#a84b9c47a79ccea04198721e2f05ac1a8)
- [bt_hci_evt_le_frame_space_update_complete::frame_space](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#a1b306ba860123344436f85914455d784)
- [bt_hci_evt_le_frame_space_update_complete::status](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#a2ec660b66b28fe0ab69b9db5681a5b17)
- [bt_hci_evt_le_frame_space_update_complete::phys](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#a66d0db4fa276b0a839ce97b0c6868ae4)
- [bt_hci_evt_le_frame_space_update_complete::handle](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#a8da9f4e322bd41f5870ea5cec0092584)
- [bt_hci_evt_le_frame_space_update_complete::initiator](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#adb081f887bc36892fc98fe78d170d93d)
- [bt_hci_evt_le_frame_space_update_complete::spacing_types](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md#af39f49f398848cfddda3edf70432a5fd)
- [bt_hci_evt_le_generate_dhkey_complete::status](../bluetooth_hci_model_reference/P259_bt_hci_evt_le_generate_dhkey_complete_结构体.md#a3d10643dd45a71b71d35dfa455ed8590)
- [bt_hci_evt_le_generate_dhkey_complete::dhkey](../bluetooth_hci_model_reference/P259_bt_hci_evt_le_generate_dhkey_complete_结构体.md#a8cd8ece786c1443ed43bd3b8fcd4d9bf)
- [bt_hci_evt_le_ltk_request::rand](../bluetooth_hci_model_reference/P260_bt_hci_evt_le_ltk_request_结构体.md#a0fcb7c6f8c52af50caa41d446294d72c)
- [bt_hci_evt_le_ltk_request::ediv](../bluetooth_hci_model_reference/P260_bt_hci_evt_le_ltk_request_结构体.md#a14e8e3e380efd91ca5402b43bee7c9d3)
- [bt_hci_evt_le_ltk_request::handle](../bluetooth_hci_model_reference/P260_bt_hci_evt_le_ltk_request_结构体.md#aed00ae384cb7d0deace8d0cc0f8e0068)
- [bt_hci_evt_le_meta_event::subevent](../bluetooth_hci_model_reference/P261_bt_hci_evt_le_meta_event_结构体.md#a536464a525f8d0f9df915be5ee3d33da)
- [bt_hci_evt_le_meta_event::data](../bluetooth_hci_model_reference/P261_bt_hci_evt_le_meta_event_结构体.md#a5f08a4c81ebab1638d251b3bf7f8bfab)
- [bt_hci_evt_le_p256_public_key_complete::status](../bluetooth_hci_model_reference/P262_bt_hci_evt_le_p256_public_key_complete_结构体.md#a57d51fca3a707b445db2534d1e175241)
- [bt_hci_evt_le_p256_public_key_complete::key](../bluetooth_hci_model_reference/P262_bt_hci_evt_le_p256_public_key_complete_结构体.md#af482f81d438b878fb826edbac8d84833)
- [bt_hci_evt_le_past_received_v2::sync_handle](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#a00bf4bdf12fce6cbf2874b9c4ae09f9f)
- [bt_hci_evt_le_past_received_v2::adv_sid](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#a05d798c9415541ef7f5716992157b1a1)
- [bt_hci_evt_le_past_received_v2::interval](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#a736af2c2ee0afd3cb00e8eb4d103991c)
- [bt_hci_evt_le_past_received_v2::clock_accuracy](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#a78853d14c3bf9a9aba3c4e15b2e06abb)
- [bt_hci_evt_le_past_received_v2::response_slot_delay](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#a9f55d5f6d17d11e72f7cac363a69fe97)
- [bt_hci_evt_le_past_received_v2::num_subevents](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#ab8a2a55fe071218284d60f1a2896945b)
- [bt_hci_evt_le_past_received_v2::response_slot_spacing](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#acf711399e575295dcef73cfeeb844eab)
- [bt_hci_evt_le_past_received_v2::service_data](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#acffc2fa22a16a3a12a4f7dfc3bb45866)
- [bt_hci_evt_le_past_received_v2::conn_handle](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#adb011949f592ec7f8843d4fd47eca2e9)
- [bt_hci_evt_le_past_received_v2::phy](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#ae7a73293519ab45aec40a9a1aeaa4e89)
- [bt_hci_evt_le_past_received_v2::subevent_interval](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#aefdc5ac7ef125f4dc5865c198b98c67d)
- [bt_hci_evt_le_past_received_v2::status](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#aefe79f973eda8c7c5670c7a721d55d8a)
- [bt_hci_evt_le_past_received_v2::addr](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md#aff78554e8980635290767e9877ac479b)
- [bt_hci_evt_le_past_received::clock_accuracy](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a00d570636a55c1d84723ad3bc5705d80)
- [bt_hci_evt_le_past_received::adv_sid](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a110c7cdd2ff1178d1ca686abaae92b05)
- [bt_hci_evt_le_past_received::status](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a1b2c229c99d06f44057b88458f168e7c)
- [bt_hci_evt_le_past_received::conn_handle](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a1bdbaddb4003cea40738ee540ecb8789)
- [bt_hci_evt_le_past_received::sync_handle](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a2cea2f3b9d51ace91ddf63639e821328)
- [bt_hci_evt_le_past_received::addr](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a3e368e95a6831f823d2efa0c0bc1ef51)
- [bt_hci_evt_le_past_received::interval](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#a41ea6099d3cca1caf37ff518a4e95492)
- [bt_hci_evt_le_past_received::service_data](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#adaa1e432db60a2529ad6266f16604e15)
- [bt_hci_evt_le_past_received::phy](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md#aedb668e6f3232b1db9035ea89ccf1b71)
- [bt_hci_evt_le_path_loss_threshold::handle](../bluetooth_hci_model_reference/P265_bt_hci_evt_le_path_loss_threshold_结构体.md#a19b1e37c5e35e1e18424615b5c25d37f)
- [bt_hci_evt_le_path_loss_threshold::current_path_loss](../bluetooth_hci_model_reference/P265_bt_hci_evt_le_path_loss_threshold_结构体.md#ac2b04c57137dcb6812fda06d4a22402a)
- [bt_hci_evt_le_path_loss_threshold::zone_entered](../bluetooth_hci_model_reference/P265_bt_hci_evt_le_path_loss_threshold_结构体.md#add7984e06d523bb34e8380dae1710b7f)
- [bt_hci_evt_le_per_adv_response_report::num_responses](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md#a37f3519eefe33e87d49c7c2ad0f8b40c)
- [bt_hci_evt_le_per_adv_response_report::responses](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md#a3b1bcca7a7dbc6fcf5709f6152268b87)
- [bt_hci_evt_le_per_adv_response_report::tx_status](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md#a46a5b74321a80697fd700a276be18ed3)
- [bt_hci_evt_le_per_adv_response_report::adv_handle](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md#a9d746015a9c2b48c54008319c892b063)
- [bt_hci_evt_le_per_adv_response_report::subevent](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md#ad4f8f61150f82f4ba420e3c0a1f333c2)
- [bt_hci_evt_le_per_adv_response::rssi](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#a1100429baf398067a396a6ba8db6778a)
- [bt_hci_evt_le_per_adv_response::cte_type](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#a4197fbae54be038502312efc14b66320)
- [bt_hci_evt_le_per_adv_response::tx_power](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#a74e304822ec7a431802cf8a7539d640e)
- [bt_hci_evt_le_per_adv_response::data_status](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#aa524756d2cce0718ecfd66704eaf389d)
- [bt_hci_evt_le_per_adv_response::response_slot](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#aa5b5467f4edd52fb8de078b0948141f0)
- [bt_hci_evt_le_per_adv_response::data](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#ace3b58eba63b55ce5f3038d4a7877ec2)
- [bt_hci_evt_le_per_adv_response::data_length](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md#af68f0dc92118f78f6f5b0ffbf1854664)
- [bt_hci_evt_le_per_adv_subevent_data_request::subevent_data_count](../bluetooth_hci_model_reference/P268_bt_hci_evt_le_per_adv_subevent_data_request_结构体.md#a45cdb248b80602a7f14f24e0324e6f97)
- [bt_hci_evt_le_per_adv_subevent_data_request::subevent_start](../bluetooth_hci_model_reference/P268_bt_hci_evt_le_per_adv_subevent_data_request_结构体.md#a8f7fd9b149aa52422cb3eb874b91943d)
- [bt_hci_evt_le_per_adv_subevent_data_request::adv_handle](../bluetooth_hci_model_reference/P268_bt_hci_evt_le_per_adv_subevent_data_request_结构体.md#ae6f6ef17edabfd210a7e6597087ff512)
- [bt_hci_evt_le_per_adv_sync_established_v2::sid](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#a0ce9a9170d93ff69f25ff35eb163511f)
- [bt_hci_evt_le_per_adv_sync_established_v2::clock_accuracy](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#a13ab0e87d6673a34e51f3112a5fd5a0c)
- [bt_hci_evt_le_per_adv_sync_established_v2::phy](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#a36b5c8454ee3635d2298592c83166f14)
- [bt_hci_evt_le_per_adv_sync_established_v2::interval](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#a958630cb9e275ab6f8ed0c548958e5ee)
- [bt_hci_evt_le_per_adv_sync_established_v2::status](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#a96b975f5a2fcf193b0b58c230486ec36)
- [bt_hci_evt_le_per_adv_sync_established_v2::response_slot_spacing](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#aacb6946dbfeb2ffbc251910853559329)
- [bt_hci_evt_le_per_adv_sync_established_v2::handle](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#ab7d3793e782d7b2bb311b8a5ac3a871b)
- [bt_hci_evt_le_per_adv_sync_established_v2::adv_addr](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#abd67ec989479eb793e7bf99a4cf371b8)
- [bt_hci_evt_le_per_adv_sync_established_v2::response_slot_delay](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#ac4c2bc8789513692ce0f2cc81aa59476)
- [bt_hci_evt_le_per_adv_sync_established_v2::subevent_interval](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#ad21df6269d8242d94ba9cbc1e0d4d344)
- [bt_hci_evt_le_per_adv_sync_established_v2::num_subevents](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md#af4fb92baa4f98c08c990ba505faf9226)
- [bt_hci_evt_le_per_adv_sync_established::handle](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#a3af8529a858992f347ce9570c5696133)
- [bt_hci_evt_le_per_adv_sync_established::interval](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#a4873b917a5bc140bb2f04ad2bee5dd69)
- [bt_hci_evt_le_per_adv_sync_established::status](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#a9ebe918fee3121168dc5b45e64aaf263)
- [bt_hci_evt_le_per_adv_sync_established::sid](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#ab11929ef8d3c71c6f2cb7c549be21282)
- [bt_hci_evt_le_per_adv_sync_established::phy](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#ab7ce6f56a69b54f02cde8fdae6860e42)
- [bt_hci_evt_le_per_adv_sync_established::adv_addr](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#adf65527ea968f4ece37d7e3c91c795d1)
- [bt_hci_evt_le_per_adv_sync_established::clock_accuracy](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md#aee68069899cc10bc38ad9fb95cf9b7b7)
- [bt_hci_evt_le_per_adv_sync_lost::handle](../bluetooth_hci_model_reference/P271_bt_hci_evt_le_per_adv_sync_lost_结构体.md#a286d534634411da53a2bda8cdfb077f8)
- [bt_hci_evt_le_per_advertising_report_v2::length](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a30f4e81346957ad4f9f0488dd93fafc3)
- [bt_hci_evt_le_per_advertising_report_v2::cte_type](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a3276c2e11c946744b73426f54bf62b8c)
- [bt_hci_evt_le_per_advertising_report_v2::handle](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a34b15fb9b5b4f0d199ccf274dd489c6a)
- [bt_hci_evt_le_per_advertising_report_v2::tx_power](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a37a9eb7d417da9285e22cc7f83071c69)
- [bt_hci_evt_le_per_advertising_report_v2::periodic_event_counter](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a499d82e1e3cfc501d399f570ebbcdc42)
- [bt_hci_evt_le_per_advertising_report_v2::data_status](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a73496cc962721538e27e9924fff0f3db)
- [bt_hci_evt_le_per_advertising_report_v2::data](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#a7af1cd4ec9df24e575a83a640eea36d2)
- [bt_hci_evt_le_per_advertising_report_v2::rssi](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#ad598ffd0108825803a4734959a354bd8)
- [bt_hci_evt_le_per_advertising_report_v2::subevent](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md#af27b23fe38e9ff092d8839cd81749456)
- [bt_hci_evt_le_per_advertising_report::length](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#a0ab1d3c5d7eb1487862451cc65c66a76)
- [bt_hci_evt_le_per_advertising_report::data](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#a1f9cdfc01e46e59e957b0c557bae620a)
- [bt_hci_evt_le_per_advertising_report::tx_power](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#a3a09aca94284a9e4af765d4da543698e)
- [bt_hci_evt_le_per_advertising_report::cte_type](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#aa683d1a4bd3a851f26b3028f566b76e4)
- [bt_hci_evt_le_per_advertising_report::data_status](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#abf23b23a12cbfeb7f996e71e2fe8b11c)
- [bt_hci_evt_le_per_advertising_report::handle](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#af81ce5bb18ef7fa1d94d00412886b081)
- [bt_hci_evt_le_per_advertising_report::rssi](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md#af874c29b89326877b499f6be1052a626)
- [bt_hci_evt_le_phy_update_complete::handle](../bluetooth_hci_model_reference/P274_bt_hci_evt_le_phy_update_complete_结构体.md#a70f472edef3b25fb23490ea6dcce9d43)
- [bt_hci_evt_le_phy_update_complete::status](../bluetooth_hci_model_reference/P274_bt_hci_evt_le_phy_update_complete_结构体.md#a927a9e6982b29ecd4c3972b19a9bcdc2)
- [bt_hci_evt_le_phy_update_complete::tx_phy](../bluetooth_hci_model_reference/P274_bt_hci_evt_le_phy_update_complete_结构体.md#ad184e10b7af71582db64ec5d3a66cff9)
- [bt_hci_evt_le_phy_update_complete::rx_phy](../bluetooth_hci_model_reference/P274_bt_hci_evt_le_phy_update_complete_结构体.md#ad792ffec08aa8e383009e2e353a03fcd)
- [bt_hci_evt_le_read_all_remote_feat_complete::max_remote_page](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md#a3582ff03fd6a680e006b94ff6080dc37)
- [bt_hci_evt_le_read_all_remote_feat_complete::status](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md#acab09b5b552faef296c6e0442c4a2bc9)
- [bt_hci_evt_le_read_all_remote_feat_complete::max_valid_page](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md#aefc3508368f6a103c9b2d218f66f6a11)
- [bt_hci_evt_le_read_all_remote_feat_complete::handle](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md#af4a77910c32dbbdb259a9532818a0746)
- [bt_hci_evt_le_read_all_remote_feat_complete::features](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md#afd04ae00d6ce4b2cb57861b0cd2e9a03)
- [bt_hci_evt_le_remote_feat_complete::features](../bluetooth_hci_model_reference/P276_bt_hci_evt_le_remote_feat_complete_结构体.md#a61101c21e317aa07b08725a7ffbb4b81)
- [bt_hci_evt_le_remote_feat_complete::status](../bluetooth_hci_model_reference/P276_bt_hci_evt_le_remote_feat_complete_结构体.md#a8a80bade7644f986fec41462843d8319)
- [bt_hci_evt_le_remote_feat_complete::handle](../bluetooth_hci_model_reference/P276_bt_hci_evt_le_remote_feat_complete_结构体.md#a9a0da26d9415169f02b6c9472120afe7)
- [bt_hci_evt_le_req_peer_sca_complete::status](../bluetooth_hci_model_reference/P277_bt_hci_evt_le_req_peer_sca_complete_结构体.md#a814d17b8aae9dd68f57402c857ca1810)
- [bt_hci_evt_le_req_peer_sca_complete::sca](../bluetooth_hci_model_reference/P277_bt_hci_evt_le_req_peer_sca_complete_结构体.md#a88f93ead6ec67e1612b1a0e8402a30e7)
- [bt_hci_evt_le_req_peer_sca_complete::handle](../bluetooth_hci_model_reference/P277_bt_hci_evt_le_req_peer_sca_complete_结构体.md#ab6b648e7f4bff9e84b274e9e22a26166)
- [bt_hci_evt_le_scan_req_received::handle](../bluetooth_hci_model_reference/P278_bt_hci_evt_le_scan_req_received_结构体.md#a62c6d5e5b7079665c0aea8eb676a0433)
- [bt_hci_evt_le_scan_req_received::addr](../bluetooth_hci_model_reference/P278_bt_hci_evt_le_scan_req_received_结构体.md#a7dca5ad876dc97859a139d8bd4b207af)
- [bt_hci_evt_le_subrate_change::supervision_timeout](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#a2ad4a06feeb0d6d36461b4a4e53dfeb1)
- [bt_hci_evt_le_subrate_change::continuation_number](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#a712b8b818115f1797787aab229040c8a)
- [bt_hci_evt_le_subrate_change::subrate_factor](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#a9387ffe45a856f7f443f5116a59a9ff2)
- [bt_hci_evt_le_subrate_change::peripheral_latency](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#a95aaed5f8c93a1d6e8cab4c7ebfad8d7)
- [bt_hci_evt_le_subrate_change::status](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#aa49286a63d565feaf3d9329cd024ee9f)
- [bt_hci_evt_le_subrate_change::handle](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md#adc08125e663a99c7232d0755c4bd760b)
- [bt_hci_evt_le_transmit_power_report::tx_power_level_flag](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#a2dc33da8f36cceda362d0c87098b02d6)
- [bt_hci_evt_le_transmit_power_report::reason](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#a341cc0c5cc1ea969e2024b67056a5439)
- [bt_hci_evt_le_transmit_power_report::handle](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#a4feadb14800c1b51a9cc523c1d6a9063)
- [bt_hci_evt_le_transmit_power_report::tx_power_level](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#aa0df9c50a555fa40ed25a14f7b6a5e77)
- [bt_hci_evt_le_transmit_power_report::delta](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#ac42d60325235f517728ff44385361db2)
- [bt_hci_evt_le_transmit_power_report::phy](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#ad6130863713cf31a1cbe33de9fb5428f)
- [bt_hci_evt_le_transmit_power_report::status](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md#af1629e59dd651e1616b89f4958f47c92)
- [bt_hci_evt_link_key_notify::bdaddr](../bluetooth_hci_model_reference/P281_bt_hci_evt_link_key_notify_结构体.md#a02647d66142c037b8bca2e748bc15319)
- [bt_hci_evt_link_key_notify::link_key](../bluetooth_hci_model_reference/P281_bt_hci_evt_link_key_notify_结构体.md#a4a1b50d8874d01a6a5dc5c52524c9bed)
- [bt_hci_evt_link_key_notify::key_type](../bluetooth_hci_model_reference/P281_bt_hci_evt_link_key_notify_结构体.md#a664580660a690af0d9ae3a62d79ad94b)
- [bt_hci_evt_link_key_req::bdaddr](../bluetooth_hci_model_reference/P282_bt_hci_evt_link_key_req_结构体.md#aed882dfb6b632383543bd7e60536ccc6)
- [bt_hci_evt_mode_change::interval](../bluetooth_hci_model_reference/P287_bt_hci_evt_mode_change_结构体.md#a12092d35d2866f9c04da6e9e9889416e)
- [bt_hci_evt_mode_change::mode](../bluetooth_hci_model_reference/P287_bt_hci_evt_mode_change_结构体.md#a91a9d6e910fd1999003ae41dce8eaa69)
- [bt_hci_evt_mode_change::status](../bluetooth_hci_model_reference/P287_bt_hci_evt_mode_change_结构体.md#abd35ca68cd0c371350ee49d95aa68454)
- [bt_hci_evt_mode_change::handle](../bluetooth_hci_model_reference/P287_bt_hci_evt_mode_change_结构体.md#af33d9335a8e9253b481c91dbd0716e40)
- [bt_hci_evt_num_completed_packets::num_handles](../bluetooth_hci_model_reference/P288_bt_hci_evt_num_completed_packets_结构体.md#a666ed2c19596a89ab0c77275cbe18d1e)
- [bt_hci_evt_num_completed_packets::h](../bluetooth_hci_model_reference/P288_bt_hci_evt_num_completed_packets_结构体.md#a94fb176924f7e844704be28851366052)
- [bt_hci_evt_pin_code_req::bdaddr](../bluetooth_hci_model_reference/P289_bt_hci_evt_pin_code_req_结构体.md#a8649a30cd8c7ecf9ee006ddc2e625908)
- [bt_hci_evt_remote_ext_features::handle](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md#a0191b80b4f4d5360972faa6d5edf5055)
- [bt_hci_evt_remote_ext_features::features](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md#a084199f8e30669c2a1a631af26c0d69a)
- [bt_hci_evt_remote_ext_features::status](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md#a4f1d489aaa5626e485d34a9ae4cf9a34)
- [bt_hci_evt_remote_ext_features::page](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md#aeece2b8d46f4a3713d63df29058f2d9c)
- [bt_hci_evt_remote_ext_features::max_page](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md#afa577407f4ded5404394f42e7c73e10b)
- [bt_hci_evt_remote_features::status](../bluetooth_hci_model_reference/P291_bt_hci_evt_remote_features_结构体.md#a2cedd8392c87914272ff250a56c80574)
- [bt_hci_evt_remote_features::features](../bluetooth_hci_model_reference/P291_bt_hci_evt_remote_features_结构体.md#a70c97b9fbf7c363eab7b27f3a4e86e96)
- [bt_hci_evt_remote_features::handle](../bluetooth_hci_model_reference/P291_bt_hci_evt_remote_features_结构体.md#ada0249bdb7108c5d347fea1218c4f878)
- [bt_hci_evt_remote_name_req_complete::bdaddr](../bluetooth_hci_model_reference/P292_bt_hci_evt_remote_name_req_complete_结构体.md#a380121873bf059b7c8a4abdf212f4235)
- [bt_hci_evt_remote_name_req_complete::name](../bluetooth_hci_model_reference/P292_bt_hci_evt_remote_name_req_complete_结构体.md#a3e54674692f7fc1670fa389e293714c7)
- [bt_hci_evt_remote_name_req_complete::status](../bluetooth_hci_model_reference/P292_bt_hci_evt_remote_name_req_complete_结构体.md#ab43d4a3c19d829b829cc7b40a67959f3)
- [bt_hci_evt_remote_version_info::subversion](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md#a02188119418a5a6dd8a4d0c37f5a060d)
- [bt_hci_evt_remote_version_info::handle](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md#a1703a9ac9a5e1ba3ed396fe5799f9f51)
- [bt_hci_evt_remote_version_info::status](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md#a196f9489183d6e0116ff687df66c60c0)
- [bt_hci_evt_remote_version_info::version](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md#a8442b9f2bdc6cbce564c9bcec4169a20)
- [bt_hci_evt_remote_version_info::manufacturer](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md#aaa9c3875143700b6ed013715cb3c7107)
- [bt_hci_evt_role_change::bdaddr](../bluetooth_hci_model_reference/P294_bt_hci_evt_role_change_结构体.md#a18dd22435ae40fcf1c4fd2b90b402c60)
- [bt_hci_evt_role_change::role](../bluetooth_hci_model_reference/P294_bt_hci_evt_role_change_结构体.md#a2e5736d63e30326c33bec8ebdf986c62)
- [bt_hci_evt_role_change::status](../bluetooth_hci_model_reference/P294_bt_hci_evt_role_change_结构体.md#aafe1a9e43a9a42d4030846180e55b8ef)
- [bt_hci_evt_ssp_complete::status](../bluetooth_hci_model_reference/P295_bt_hci_evt_ssp_complete_结构体.md#a33d3d47c1cef71cfb787a1195d9b4ec2)
- [bt_hci_evt_ssp_complete::bdaddr](../bluetooth_hci_model_reference/P295_bt_hci_evt_ssp_complete_结构体.md#a5030cf334f97cdd982001b3278ed9db1)
- [bt_hci_evt_sync_conn_complete::tx_interval](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#a4b93873ad6f5388657511d87fc0a8c85)
- [bt_hci_evt_sync_conn_complete::air_mode](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#a5f6068569bf649bcd1d13928f56f9703)
- [bt_hci_evt_sync_conn_complete::retansmission_window](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#a68a31880c8aab9245be043c1719464d3)
- [bt_hci_evt_sync_conn_complete::rx_pkt_length](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#a6a455f56da4666cb602e6c05157e166d)
- [bt_hci_evt_sync_conn_complete::bdaddr](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#a78f5560783400f1d1a63b2c9d69fa7ed)
- [bt_hci_evt_sync_conn_complete::handle](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#aa48aa29ff73e93e8d961013f066c1b5e)
- [bt_hci_evt_sync_conn_complete::link_type](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#aacf9919945e9b755913da145f0fe78ae)
- [bt_hci_evt_sync_conn_complete::tx_pkt_length](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#ab4d4106d5120f10e8300834db12740d8)
- [bt_hci_evt_sync_conn_complete::status](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md#accd17a95f35ab1988122df7584830f60)
- [bt_hci_evt_user_confirm_req::bdaddr](../bluetooth_hci_model_reference/P297_bt_hci_evt_user_confirm_req_结构体.md#aaeec83c50764c322af7cd64259e54a97)
- [bt_hci_evt_user_confirm_req::passkey](../bluetooth_hci_model_reference/P297_bt_hci_evt_user_confirm_req_结构体.md#ac333729f5a7d9241ac26aeb7d3f77935)
- [bt_hci_evt_user_passkey_notify::passkey](../bluetooth_hci_model_reference/P298_bt_hci_evt_user_passkey_notify_结构体.md#a7f6a367e50d41cb7d8897db05db826be)
- [bt_hci_evt_user_passkey_notify::bdaddr](../bluetooth_hci_model_reference/P298_bt_hci_evt_user_passkey_notify_结构体.md#af020e1cd131473fe06a193529a0499ac)
- [bt_hci_evt_user_passkey_req::bdaddr](../bluetooth_hci_model_reference/P299_bt_hci_evt_user_passkey_req_结构体.md#a7f1005423296906e0374050bc30781ce)
- [bt_hci_ext_adv_set::max_ext_adv_evts](../bluetooth_hci_model_reference/P307_bt_hci_ext_adv_set_结构体.md#a4467ac9a564ea24bb701de46cda2579a)
- [bt_hci_ext_adv_set::handle](../bluetooth_hci_model_reference/P307_bt_hci_ext_adv_set_结构体.md#a9d0fd3f6659db172ff4efd74c2c2d216)
- [bt_hci_ext_adv_set::duration](../bluetooth_hci_model_reference/P307_bt_hci_ext_adv_set_结构体.md#acc2afc91fe5c0dfcb4c95eaade4a047a)
- [bt_hci_ext_conn_phy::max_ce_len](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#a3c3ccb93014758b3215718d2672ce7f3)
- [bt_hci_ext_conn_phy::scan_interval](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#a4f78503fe42ee81fea740ba1643a732e)
- [bt_hci_ext_conn_phy::conn_interval_max](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#a7bcf66a3372d92c809d8427796915b88)
- [bt_hci_ext_conn_phy::conn_latency](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#a7dd57b7ef0b13b15da47e92076f87d79)
- [bt_hci_ext_conn_phy::conn_interval_min](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#a7fc06c1a458aedb6b29381450a5a4df0)
- [bt_hci_ext_conn_phy::supervision_timeout](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#aaec54c0743dfc08923b5ccd8fc1a4015)
- [bt_hci_ext_conn_phy::scan_window](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#ae0e950c8004bd595631f95a289a5c871)
- [bt_hci_ext_conn_phy::min_ce_len](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md#af48212961ce21f5222e57f70ffeb811b)
- [bt_hci_ext_scan_phy::interval](../bluetooth_hci_model_reference/P309_bt_hci_ext_scan_phy_结构体.md#a2f087d18bde86d0ac81a14a09ae5b9b0)
- [bt_hci_ext_scan_phy::type](../bluetooth_hci_model_reference/P309_bt_hci_ext_scan_phy_结构体.md#a4cfebc7b2709973953bed9a09a793b7e)
- [bt_hci_ext_scan_phy::window](../bluetooth_hci_model_reference/P309_bt_hci_ext_scan_phy_结构体.md#a9c0196f0d5f0064796c15a5df2ad4c07)
- [bt_hci_handle_count::count](../bluetooth_hci_model_reference/P310_bt_hci_handle_count_结构体.md#a71577f376985909744fa14f246e69e1d)
- [bt_hci_handle_count::handle](../bluetooth_hci_model_reference/P310_bt_hci_handle_count_结构体.md#acacc000905835724b7fe882a8ad85f82)
- [bt_hci_iac_lap::iac](../bluetooth_hci_model_reference/P311_bt_hci_iac_lap_结构体.md#ac729dc24f337c32b1ffd0e212ccf49ff)
- [bt_hci_iso_hdr::len](../bluetooth_hci_model_reference/P312_bt_hci_iso_hdr_结构体.md#ab33ae914a9eba85b35c78e45e0f5255f)
- [bt_hci_iso_hdr::handle](../bluetooth_hci_model_reference/P312_bt_hci_iso_hdr_结构体.md#af5113383fbcd0e70828f986720c38572)
- [bt_hci_iso_sdu_hdr::slen](../bluetooth_hci_model_reference/P313_bt_hci_iso_sdu_hdr_结构体.md#a626764862a3757a3119b6de799221ad1)
- [bt_hci_iso_sdu_hdr::sn](../bluetooth_hci_model_reference/P313_bt_hci_iso_sdu_hdr_结构体.md#a683d493de5d00e3b4c5169f6de498c13)
- [bt_hci_iso_sdu_ts_hdr::sdu](../bluetooth_hci_model_reference/P314_bt_hci_iso_sdu_ts_hdr_结构体.md#a3f81175b95f8eaeeeee71ee4bf401864)
- [bt_hci_iso_sdu_ts_hdr::ts](../bluetooth_hci_model_reference/P314_bt_hci_iso_sdu_ts_hdr_结构体.md#a657e03c5ef597f04cc21725f0bc227d4)
- [bt_hci_le_cs_step_data_mode_0_initiator::packet_rssi](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md#a11edf6e1c1da5d24aa1136521a249f52)
- [bt_hci_le_cs_step_data_mode_0_initiator::packet_quality_bit_errors](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md#a339252cacafd05e85c0fb19776343e17)
- [bt_hci_le_cs_step_data_mode_0_initiator::measured_freq_offset](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md#a48fc1fd87869d4ca2b70c42d5c4e1d75)
- [bt_hci_le_cs_step_data_mode_0_initiator::packet_quality_aa_check](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md#a811eb38a04e63b12be9e25291126ccc1)
- [bt_hci_le_cs_step_data_mode_0_initiator::packet_antenna](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md#ad9a2193cbe5381d30494dbf6f8d84482)
- [bt_hci_le_cs_step_data_mode_0_reflector::packet_quality_bit_errors](../bluetooth_hci_model_reference/P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md#a16fb71660c4f4afb1c36765fdbd2a96a)
- [bt_hci_le_cs_step_data_mode_0_reflector::packet_quality_aa_check](../bluetooth_hci_model_reference/P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md#a9c34ecf0b79449754da1d1ba925b1ff2)
- [bt_hci_le_cs_step_data_mode_0_reflector::packet_rssi](../bluetooth_hci_model_reference/P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md#aa058afab8cba3f5ce572b8e7d29ef34d)
- [bt_hci_le_cs_step_data_mode_0_reflector::packet_antenna](../bluetooth_hci_model_reference/P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md#ad045baeaf6fbb75de002ffedc4b1a831)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_pct1](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a3f8ba85b776f732ebc1086a4317849a1)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_nadm](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a511b281fb1c16fd7d0eaf731906a4292)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_quality_bit_errors](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a515fde1d568a19ccf6ebefe9052866a4)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_rssi](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a5ec9c30063c09285804973008533e5cb)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt::toa_tod_initiator](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a77bbcd9451360ad97813f9357e44766e)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_pct2](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#a9f969aa6fc134a9e618d07f177d2b7fd)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_antenna](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#abf20351ab0eaf3a7139a464f1d1a72b0)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt::tod_toa_reflector](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#ace3843bc24616950f04150b2f86abad4)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_quality_aa_check](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md#ad8f9ca9dda852b435848b988ad872797)
- [bt_hci_le_cs_step_data_mode_1::packet_quality_bit_errors](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#a0cb4198466318a7a15cbbb172c582eeb)
- [bt_hci_le_cs_step_data_mode_1::toa_tod_initiator](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#a1365e601f422b98747f9909d3be56b60)
- [bt_hci_le_cs_step_data_mode_1::packet_rssi](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#a1b9df39c01ab91ab225c809db5066f70)
- [bt_hci_le_cs_step_data_mode_1::packet_nadm](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#a4025cf2b229ada27e258d3d519a7b1dd)
- [bt_hci_le_cs_step_data_mode_1::packet_quality_aa_check](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#a8383926e95cd9d222b91704b2ca6883e)
- [bt_hci_le_cs_step_data_mode_1::tod_toa_reflector](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#ab3425181b2a625fcfbbfd14477d717d1)
- [bt_hci_le_cs_step_data_mode_1::packet_antenna](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md#afc8221a5cab14d3842590e6cac52da4d)
- [bt_hci_le_cs_step_data_mode_2::antenna_permutation_index](../bluetooth_hci_model_reference/P319_bt_hci_le_cs_step_data_mode_2_结构体.md#a9feb2b07f8862aa24772a733f451f7a8)
- [bt_hci_le_cs_step_data_mode_2::tone_info](../bluetooth_hci_model_reference/P319_bt_hci_le_cs_step_data_mode_2_结构体.md#aef5699cb9bfc522a12be9a284392fd0e)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_quality_aa_check](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#a657ec3570e3ad6b2ddab87bada231587)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_antenna](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#a9ce412ad8b18a9315b858cf1fe2a466a)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_nadm](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#a9d2428083c401d931520addde0af54fd)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_pct1](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#aada8b3ff1bb0d0b9eccb846da173b3f4)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt::antenna_permutation_index](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#ac4067e27caa12cf9f8c6525bf6a72973)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt::tod_toa_reflector](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#ada4d52f54f1efa804a812c65edd8f125)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_rssi](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#adc4fe32bc6b7515e5bf1055f19f1a2bd)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt::toa_tod_initiator](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#ae2181a568ed6da32d3f60ba6d271c64f)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt::tone_info](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#aea13fc3e16092dcede9fb46ea719f21c)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_quality_bit_errors](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#af5d8a8559400b45066bdac86fbdac411)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_pct2](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md#afdebbafc06475dde12aaed73d2180f96)
- [bt_hci_le_cs_step_data_mode_3::toa_tod_initiator](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a183f3ee64a4482c9d3e0f041151fdcf9)
- [bt_hci_le_cs_step_data_mode_3::packet_quality_bit_errors](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a42b8bdf1fd492be1daded674e3d733d6)
- [bt_hci_le_cs_step_data_mode_3::packet_rssi](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a60750ac38bf019a0c7a8656ca59fc402)
- [bt_hci_le_cs_step_data_mode_3::antenna_permutation_index](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a609102fc9d42fe73c09907f54526bd40)
- [bt_hci_le_cs_step_data_mode_3::tone_info](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a9ae78aa83a22f0618491871d55f2f0b9)
- [bt_hci_le_cs_step_data_mode_3::packet_nadm](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#a9b7373e7d3faa0cb5553d4f897c94ebc)
- [bt_hci_le_cs_step_data_mode_3::tod_toa_reflector](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#aa0f1918115a6e550d6fab17529bbb4f2)
- [bt_hci_le_cs_step_data_mode_3::packet_antenna](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#ad20e9c1deba67aa5759881b52d13311d)
- [bt_hci_le_cs_step_data_mode_3::packet_quality_aa_check](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md#ad4c30784cc2586b5b8dcfa22e7a1f8fb)
- [bt_hci_le_cs_step_data_tone_info::quality_indicator](../bluetooth_hci_model_reference/P322_bt_hci_le_cs_step_data_tone_info_结构体.md#a4d31c0759c17789cb4b9bdc90a8870ca)
- [bt_hci_le_cs_step_data_tone_info::extension_indicator](../bluetooth_hci_model_reference/P322_bt_hci_le_cs_step_data_tone_info_结构体.md#a5f2e5e95b97d2be49a8ff1d9376892e8)
- [bt_hci_le_cs_step_data_tone_info::phase_correction_term](../bluetooth_hci_model_reference/P322_bt_hci_le_cs_step_data_tone_info_结构体.md#aeb76aeb54cb4e5613496431ec6d0093a)
- [bt_hci_le_iq_sample::q](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md#a775b6e0ab1842594bc00998faec613f3)
- [bt_hci_le_iq_sample::i](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md#aacf452456eecd4ad4dab083593b11104)
- [bt_hci_le_read_min_supported_conn_interval_group::group_stride](../bluetooth_hci_model_reference/P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md#a43ef933e3f445ac1366a3707b52ceffd)
- [bt_hci_le_read_min_supported_conn_interval_group::group_min](../bluetooth_hci_model_reference/P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md#a5cfd002c4dc82faa692ed1afa50692b5)
- [bt_hci_le_read_min_supported_conn_interval_group::group_max](../bluetooth_hci_model_reference/P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md#abcd7d0eadf485b82993d421072cc8ba4)
- [bt_hci_op_inquiry::lap](../bluetooth_hci_model_reference/P328_bt_hci_op_inquiry_结构体.md#abdd03feccecbdbbb5d2c7c7f3213b62f)
- [bt_hci_op_inquiry::num_rsp](../bluetooth_hci_model_reference/P328_bt_hci_op_inquiry_结构体.md#ac8ed23243dbd9a7c46fedd8abe9666f5)
- [bt_hci_op_inquiry::length](../bluetooth_hci_model_reference/P328_bt_hci_op_inquiry_结构体.md#ae77fa706c9875b5568a4af26a7724d08)
- [bt_hci_op_le_connection_rate_request::max_latency](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#a35033b89faecdaa053e8bcff590ad5e7)
- [bt_hci_op_le_connection_rate_request::supervision_timeout](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#a523cde9caf261ca3f3766b4d9648c7eb)
- [bt_hci_op_le_connection_rate_request::subrate_max](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#a5ac425326df618f446bc891ea0b329ec)
- [bt_hci_op_le_connection_rate_request::handle](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#a7178c6af0cdbf1376bd3e52a175be03e)
- [bt_hci_op_le_connection_rate_request::min_ce_len](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#a87ad44b9857515b42aff8200cfb42b37)
- [bt_hci_op_le_connection_rate_request::continuation_number](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#aa1123f8a8eafa16785e440b8b8a7e885)
- [bt_hci_op_le_connection_rate_request::subrate_min](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#ab06f3b29db55a6f56ab8cc1f2e7b95df)
- [bt_hci_op_le_connection_rate_request::conn_interval_max](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#ae290b39a2ba9c37595de67b877a61f3b)
- [bt_hci_op_le_connection_rate_request::conn_interval_min](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#aee4d2070f12c33c5c6f6d93435f1f4b5)
- [bt_hci_op_le_connection_rate_request::max_ce_len](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md#af63ff615adc36c422d6be8db20e45c85)
- [bt_hci_op_le_cs_test::t_ip1_time](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a0675dfbb050838d98f21cfa28af8615b)
- [bt_hci_op_le_cs_test::cs_enhancements_1](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a06ac1b5aa8951fe4769a1360af44df82)
- [bt_hci_op_le_cs_test::sub_mode_type](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a090c5d03cf829011196d644cd9f7c7db)
- [bt_hci_op_le_cs_test::t_sw_time](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a09c40ecd0d4e325e0c0504a9d8cd977b)
- [bt_hci_op_le_cs_test::override_parameters_data](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a15a68fe7c98b2e242afd6eb67dd9b40a)
- [bt_hci_op_le_cs_test::max_num_subevents](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a1c105f7a4d48754322fee6992db8c175)
- [bt_hci_op_le_cs_test::override_parameters_length](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a373372a93d94e70d674c1c7b4c126734)
- [bt_hci_op_le_cs_test::snr_control_reflector](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a3c949d9a7eb4f56427f6e9f8be7cb77b)
- [bt_hci_op_le_cs_test::snr_control_initiator](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a551c06e651180867dd1d23b3fdf4c031)
- [bt_hci_op_le_cs_test::main_mode_repetition](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a60cc9a7c46f8cd0933dc2f5a68cca627)
- [bt_hci_op_le_cs_test::t_ip2_time](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a7538e91b5ced2702965a21f8e754ebcc)
- [bt_hci_op_le_cs_test::subevent_len](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a8ad67a5a0138f32cc5295074011a3808)
- [bt_hci_op_le_cs_test::channel_map_repetition](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a8c23c2e6e8c38bf33fcd6d1e343f5982)
- [bt_hci_op_le_cs_test::t_pm_time](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#a981da50e0594b8bc05f811e5170b10f5)
- [bt_hci_op_le_cs_test::t_fcs_time](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#aa3d510663e5dcc44b5acd9d1c41746d5)
- [bt_hci_op_le_cs_test::mode_0_steps](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#aaf480890608b5cfc9151dac844e9a337)
- [bt_hci_op_le_cs_test::tone_antenna_config_selection](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#acaa428a37e68ff56c311397e53f46526)
- [bt_hci_op_le_cs_test::override_config](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#acc2d0768b69e5f5b593e5aff71b17f20)
- [bt_hci_op_le_cs_test::subevent_interval](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#ad52cd2862d2544448a5e175c58541f89)
- [bt_hci_op_le_cs_test::transmit_power_level](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#adf2f24dc6988f1f0e0457a6cf3141521)
- [bt_hci_op_le_cs_test::rtt_type](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#ae0234031d94e93653dd45e6e657c199f)
- [bt_hci_op_le_cs_test::drbg_nonce](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#aee8c125df0f7136a0ecdb9f04903aaef)
- [bt_hci_op_le_cs_test::cs_sync_antenna_selection](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#aef335dd7738634cb8f81c18e0350141e)
- [bt_hci_op_le_cs_test::cs_sync_phy](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#af42701651bca5fe0353ae1de9c453f47)
- [bt_hci_op_le_cs_test::main_mode_type](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#af4cdfd8c8cab500277c06a82ac088577)
- [bt_hci_op_le_cs_test::role](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md#afa0310f818002d7c1ac048f0db8c7f1c)
- [bt_hci_op_le_read_min_supported_conn_interval::min_supported_conn_interval](../bluetooth_hci_model_reference/P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md#a0c71077c8e7db5b1bdba1372bc7ac5ac)
- [bt_hci_op_le_read_min_supported_conn_interval::num_groups](../bluetooth_hci_model_reference/P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md#a8bd4666fa42fb9a527fca5309e3bf0d6)
- [bt_hci_op_le_read_min_supported_conn_interval::groups](../bluetooth_hci_model_reference/P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md#a92313039960815652380c301d4a5ce8d)
- [bt_hci_op_le_read_min_supported_conn_interval::status](../bluetooth_hci_model_reference/P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md#aa049350b4f8fafe3bf74780924e1eeff)
- [bt_hci_op_le_set_default_rate_parameters::subrate_min](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#a115579391f9fe7ec2536a21c3a42b3ab)
- [bt_hci_op_le_set_default_rate_parameters::max_latency](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#a4efb8757f63f15e37070b3046490edcf)
- [bt_hci_op_le_set_default_rate_parameters::max_ce_len](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#a630ae05aff2e511b37a522fadd831dd0)
- [bt_hci_op_le_set_default_rate_parameters::continuation_number](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#aaa9dd1a946c7440e0a985276137ae096)
- [bt_hci_op_le_set_default_rate_parameters::subrate_max](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#ad267cc8be963c1d16088a7c14bef19bf)
- [bt_hci_op_le_set_default_rate_parameters::conn_interval_max](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#ad8051508f324d40bd95e9dbee97b1b2a)
- [bt_hci_op_le_set_default_rate_parameters::min_ce_len](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#adb818d82c1c38f573a31f22b0ebc817b)
- [bt_hci_op_le_set_default_rate_parameters::supervision_timeout](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#af0fbd935b200c98b5ef6477d127ccdfe)
- [bt_hci_op_le_set_default_rate_parameters::conn_interval_min](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md#af9afc0e463f068c113c0042f58dcc63d)
- [bt_hci_rp_configure_data_path::status](../bluetooth_hci_model_reference/P334_bt_hci_rp_configure_data_path_结构体.md#a10cfe9bf5a7be202706957d7b8e1f371)
- [bt_hci_rp_connect_cancel::status](../bluetooth_hci_model_reference/P335_bt_hci_rp_connect_cancel_结构体.md#a05d0c9e4163bc62a57dba8618294eb65)
- [bt_hci_rp_connect_cancel::bdaddr](../bluetooth_hci_model_reference/P335_bt_hci_rp_connect_cancel_结构体.md#a0ccfcbd294aa067879ab8d7a41bc41c9)
- [bt_hci_rp_le_big_terminate_sync::big_handle](../bluetooth_hci_model_reference/P336_bt_hci_rp_le_big_terminate_sync_结构体.md#a741ab80e08e7ecfc5a0158ec0cf14654)
- [bt_hci_rp_le_big_terminate_sync::status](../bluetooth_hci_model_reference/P336_bt_hci_rp_le_big_terminate_sync_结构体.md#ad4d1d4238402ef829a1ff9ed3b1dc050)
- [bt_hci_rp_le_conn_cte_req_enable::status](../bluetooth_hci_model_reference/P337_bt_hci_rp_le_conn_cte_req_enable_结构体.md#a1e76e7a6da194a433c1fa6ac2bc36b80)
- [bt_hci_rp_le_conn_cte_req_enable::handle](../bluetooth_hci_model_reference/P337_bt_hci_rp_le_conn_cte_req_enable_结构体.md#af00adb07a144156a37fb5fc47ca61ccb)
- [bt_hci_rp_le_conn_cte_rsp_enable::status](../bluetooth_hci_model_reference/P338_bt_hci_rp_le_conn_cte_rsp_enable_结构体.md#a8a21bc015408cc77c5d229cd77289dcc)
- [bt_hci_rp_le_conn_cte_rsp_enable::handle](../bluetooth_hci_model_reference/P338_bt_hci_rp_le_conn_cte_rsp_enable_结构体.md#ab16f226d871d7d55c3f900614d59d8a1)
- [bt_hci_rp_le_conn_param_req_neg_reply::status](../bluetooth_hci_model_reference/P339_bt_hci_rp_le_conn_param_req_neg_reply_结构体.md#a3804e64f9e8693e3e5899067212f6873)
- [bt_hci_rp_le_conn_param_req_neg_reply::handle](../bluetooth_hci_model_reference/P339_bt_hci_rp_le_conn_param_req_neg_reply_结构体.md#ac88f44127c0a1b9b191a27cc003c1052)
- [bt_hci_rp_le_conn_param_req_reply::status](../bluetooth_hci_model_reference/P340_bt_hci_rp_le_conn_param_req_reply_结构体.md#a2f0a9f5b087d1f12c100ef4521e015ff)
- [bt_hci_rp_le_conn_param_req_reply::handle](../bluetooth_hci_model_reference/P340_bt_hci_rp_le_conn_param_req_reply_结构体.md#a3e598cd87d5298a1cc62ac79a4f34a6e)
- [bt_hci_rp_le_default_past_param::status](../bluetooth_hci_model_reference/P341_bt_hci_rp_le_default_past_param_结构体.md#a292e2d655c77e8cda0d01fc07b43b8c4)
- [bt_hci_rp_le_encrypt::enc_data](../bluetooth_hci_model_reference/P342_bt_hci_rp_le_encrypt_结构体.md#ac20cd9f4ceffea6999114f65437aefdc)
- [bt_hci_rp_le_encrypt::status](../bluetooth_hci_model_reference/P342_bt_hci_rp_le_encrypt_结构体.md#aee480917cc6af7dea77717a9cb5840bb)
- [bt_hci_rp_le_iso_receive_test::status](../bluetooth_hci_model_reference/P343_bt_hci_rp_le_iso_receive_test_结构体.md#a028a77001a5e24dda8fac38718103ef0)
- [bt_hci_rp_le_iso_receive_test::handle](../bluetooth_hci_model_reference/P343_bt_hci_rp_le_iso_receive_test_结构体.md#a863a8a44af979a8b1b9d084563b2fe9a)
- [bt_hci_rp_le_iso_test_end::missed_cnt](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md#a10b3ee6110bc0bb9279b22f9963715c1)
- [bt_hci_rp_le_iso_test_end::status](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md#a16feaeb739f6ed34d9ce3fc86248955c)
- [bt_hci_rp_le_iso_test_end::handle](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md#a4a4625d7b78abf3c039842df2a72ce8b)
- [bt_hci_rp_le_iso_test_end::received_cnt](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md#a55490978e7416ecc308bf510f05afd4f)
- [bt_hci_rp_le_iso_test_end::failed_cnt](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md#ab4352fd5d9b822fb7fb75f8f5e2db6a9)
- [bt_hci_rp_le_iso_transmit_test::status](../bluetooth_hci_model_reference/P345_bt_hci_rp_le_iso_transmit_test_结构体.md#a01ae01d11c606f559107b8c54781d843)
- [bt_hci_rp_le_iso_transmit_test::handle](../bluetooth_hci_model_reference/P345_bt_hci_rp_le_iso_transmit_test_结构体.md#a0863c47551b328984e00c392f9f11660)
- [bt_hci_rp_le_ltk_req_neg_reply::status](../bluetooth_hci_model_reference/P346_bt_hci_rp_le_ltk_req_neg_reply_结构体.md#a92306e47450b239233a3f39c645eaa4e)
- [bt_hci_rp_le_ltk_req_neg_reply::handle](../bluetooth_hci_model_reference/P346_bt_hci_rp_le_ltk_req_neg_reply_结构体.md#ad0f4f9300d9a8b737b41211972151017)
- [bt_hci_rp_le_ltk_req_reply::handle](../bluetooth_hci_model_reference/P347_bt_hci_rp_le_ltk_req_reply_结构体.md#a2dfe012e641e5d8bd6c0f2e15e5a54c2)
- [bt_hci_rp_le_ltk_req_reply::status](../bluetooth_hci_model_reference/P347_bt_hci_rp_le_ltk_req_reply_结构体.md#a831950bab8994f36c96c543310400752)
- [bt_hci_rp_le_past_param::status](../bluetooth_hci_model_reference/P348_bt_hci_rp_le_past_param_结构体.md#a9630362b3d885b13869a4c0fe9e97b12)
- [bt_hci_rp_le_past_param::conn_handle](../bluetooth_hci_model_reference/P348_bt_hci_rp_le_past_param_结构体.md#ae6b8a5d7e790516de2f91e41fd893111)
- [bt_hci_rp_le_per_adv_set_info_transfer::conn_handle](../bluetooth_hci_model_reference/P349_bt_hci_rp_le_per_adv_set_info_transfer_结构体.md#a696e5cab4d7507ea79b0e116c4bb92e2)
- [bt_hci_rp_le_per_adv_set_info_transfer::status](../bluetooth_hci_model_reference/P349_bt_hci_rp_le_per_adv_set_info_transfer_结构体.md#ab1592bfadd45315ff47e86b7c50374ad)
- [bt_hci_rp_le_per_adv_sync_transfer::conn_handle](../bluetooth_hci_model_reference/P350_bt_hci_rp_le_per_adv_sync_transfer_结构体.md#ab8b4357fd92e01a5f61d3127b04c0318)
- [bt_hci_rp_le_per_adv_sync_transfer::status](../bluetooth_hci_model_reference/P350_bt_hci_rp_le_per_adv_sync_transfer_结构体.md#adb536c4694d2e7c5b91e9f68986e97e1)
- [bt_hci_rp_le_rand::rand](../bluetooth_hci_model_reference/P351_bt_hci_rp_le_rand_结构体.md#a3f706af9d2baf9e2b199242a28cec9e5)
- [bt_hci_rp_le_rand::status](../bluetooth_hci_model_reference/P351_bt_hci_rp_le_rand_结构体.md#a73320168836caa3caf724282402e80de)
- [bt_hci_rp_le_read_all_local_supported_features::max_page](../bluetooth_hci_model_reference/P352_bt_hci_rp_le_read_all_local_supported_features_结构体.md#a3e200ffc8a5ecafc5e7173f1a48fe6b1)
- [bt_hci_rp_le_read_all_local_supported_features::features](../bluetooth_hci_model_reference/P352_bt_hci_rp_le_read_all_local_supported_features_结构体.md#a8cecb341ec3dfb335940af0a6e4751c6)
- [bt_hci_rp_le_read_all_local_supported_features::status](../bluetooth_hci_model_reference/P352_bt_hci_rp_le_read_all_local_supported_features_结构体.md#ac4aeb5159bb91c8faf9d12461b005e89)
- [bt_hci_rp_le_read_ant_info::num_ant](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md#a1f79b45751d39ebb9349df93d0ff2e13)
- [bt_hci_rp_le_read_ant_info::switch_sample_rates](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md#a2c78d3db239c9e00729d91834eb60f21)
- [bt_hci_rp_le_read_ant_info::max_cte_len](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md#a625cc8fa8553eafbbb31cbc0b3f303c7)
- [bt_hci_rp_le_read_ant_info::status](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md#ae1388d3eee3085af7f2b0b57b2aa7b1e)
- [bt_hci_rp_le_read_ant_info::max_switch_pattern_len](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md#ae75fe0b9f5fe8c88a8e8482eef299348)
- [bt_hci_rp_le_read_buffer_size_v2::acl_max_num](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md#a1c7938defb076d973b8339c17cc930df)
- [bt_hci_rp_le_read_buffer_size_v2::status](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md#a3b9cc0577d0f5f3c2b934a28915f2177)
- [bt_hci_rp_le_read_buffer_size_v2::iso_max_len](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md#a9758d477c502575a1c176eb6a63e1a1a)
- [bt_hci_rp_le_read_buffer_size_v2::iso_max_num](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md#ac3379adf42f9bbee8ae72fb4a7606fd1)
- [bt_hci_rp_le_read_buffer_size_v2::acl_max_len](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md#ac391149d3d7442e074aad4b98659bd02)
- [bt_hci_rp_le_read_buffer_size::le_max_num](../bluetooth_hci_model_reference/P354_bt_hci_rp_le_read_buffer_size_结构体.md#a3e393d6c51d8c3f8a5d88413198e3f28)
- [bt_hci_rp_le_read_buffer_size::le_max_len](../bluetooth_hci_model_reference/P354_bt_hci_rp_le_read_buffer_size_结构体.md#a8bc64cd8743984cd5a8dedfc86aaee56)
- [bt_hci_rp_le_read_buffer_size::status](../bluetooth_hci_model_reference/P354_bt_hci_rp_le_read_buffer_size_结构体.md#a90a1206f1dbbefd298e5323ac07691f1)
- [bt_hci_rp_le_read_chan_map::ch_map](../bluetooth_hci_model_reference/P356_bt_hci_rp_le_read_chan_map_结构体.md#a2899c53f17ba2293b95477ba25fd1b3d)
- [bt_hci_rp_le_read_chan_map::status](../bluetooth_hci_model_reference/P356_bt_hci_rp_le_read_chan_map_结构体.md#a73a51f243bf4881f9024ba67cf2426ad)
- [bt_hci_rp_le_read_chan_map::handle](../bluetooth_hci_model_reference/P356_bt_hci_rp_le_read_chan_map_结构体.md#a8fcec46574f5601bf0837aae8f745b38)
- [bt_hci_rp_le_read_chan_tx_power::status](../bluetooth_hci_model_reference/P357_bt_hci_rp_le_read_chan_tx_power_结构体.md#a09a3805bccdabef399d21b29f84e3a4f)
- [bt_hci_rp_le_read_chan_tx_power::tx_power_level](../bluetooth_hci_model_reference/P357_bt_hci_rp_le_read_chan_tx_power_结构体.md#a3b6b79d1d28c3e4bf565ae364089f365)
- [bt_hci_rp_le_read_default_data_len::max_tx_octets](../bluetooth_hci_model_reference/P358_bt_hci_rp_le_read_default_data_len_结构体.md#a1ec4ba1c0286132e87fcffeb988a37f9)
- [bt_hci_rp_le_read_default_data_len::status](../bluetooth_hci_model_reference/P358_bt_hci_rp_le_read_default_data_len_结构体.md#a62d735826ad3ca5d4bea7d0fb87dea7e)
- [bt_hci_rp_le_read_default_data_len::max_tx_time](../bluetooth_hci_model_reference/P358_bt_hci_rp_le_read_default_data_len_结构体.md#ae193eab40c2afa55b78a1906e6a26f26)
- [bt_hci_rp_le_read_fal_size::status](../bluetooth_hci_model_reference/P359_bt_hci_rp_le_read_fal_size_结构体.md#aaceae885848bbdbf71241e7aa3881db5)
- [bt_hci_rp_le_read_fal_size::fal_size](../bluetooth_hci_model_reference/P359_bt_hci_rp_le_read_fal_size_结构体.md#ac5fcb88478c1faadf7f7ca6a9f838dde)
- [bt_hci_rp_le_read_iso_link_quality::tx_last_subevent_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a0d4468f6871716414ef4a601791bac58)
- [bt_hci_rp_le_read_iso_link_quality::tx_flushed_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a12c0c3f9fe6c3c94742367f30bdcc630)
- [bt_hci_rp_le_read_iso_link_quality::crc_error_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a353070a64655a39f5410fe76e9168e97)
- [bt_hci_rp_le_read_iso_link_quality::duplicate_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a68c23277e65dc5694f5a27ee2cd364ff)
- [bt_hci_rp_le_read_iso_link_quality::rx_unreceived_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a6a16d0aa7ed220bac1ade12eb0f7703e)
- [bt_hci_rp_le_read_iso_link_quality::retransmitted_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a7be135da9607045f60b616b84a68f5db)
- [bt_hci_rp_le_read_iso_link_quality::handle](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#a9f2e8c26081ede43c7712b851d79f2cd)
- [bt_hci_rp_le_read_iso_link_quality::tx_unacked_packets](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#aae42e05dff474062726b92c6d45eae4f)
- [bt_hci_rp_le_read_iso_link_quality::status](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md#aef80c600f8916c098e08c43ca718d630)
- [bt_hci_rp_le_read_iso_tx_sync::status](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md#a188ef5dba77c754c46094135cc52641c)
- [bt_hci_rp_le_read_iso_tx_sync::offset](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md#a29770c3172d5e45409392aa8ffc835ef)
- [bt_hci_rp_le_read_iso_tx_sync::timestamp](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md#a35520a3e50afc03ed969b6c5ca9e15d9)
- [bt_hci_rp_le_read_iso_tx_sync::handle](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md#a8c0003043d3896b1ff93dc33dccc76b4)
- [bt_hci_rp_le_read_iso_tx_sync::seq](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md#af2a02f68aa0a757757c490e707954952)
- [bt_hci_rp_le_read_local_features::status](../bluetooth_hci_model_reference/P362_bt_hci_rp_le_read_local_features_结构体.md#ac1000822beba8a7be0dda684c0a86b6b)
- [bt_hci_rp_le_read_local_features::features](../bluetooth_hci_model_reference/P362_bt_hci_rp_le_read_local_features_结构体.md#ada42e525338cd5526ff211c359c93b3b)
- [bt_hci_rp_le_read_local_rpa::status](../bluetooth_hci_model_reference/P363_bt_hci_rp_le_read_local_rpa_结构体.md#a55b1ac66c986c0a7879b144163064be2)
- [bt_hci_rp_le_read_local_rpa::local_rpa](../bluetooth_hci_model_reference/P363_bt_hci_rp_le_read_local_rpa_结构体.md#a5b27c5b02cb290452be62c22772fbc53)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::rtt_sounding_n](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a145d8fe34f80df9367105d1cfa7b59c1)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::t_fcs_times_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a1d2e82062c0c41dce9e7428e4982223a)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::t_ip2_times_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a1f97298da17187ea1ed96ec923f54523)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::subfeatures_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a28b801d5310e4fd7e8285ba6361191df)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::rtt_aa_only_n](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a29667f70ea84458e304fe731d443e25a)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::t_sw_ipt_time_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a2c51d311adcacada33b9dec7b4395865)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::tx_snr_capability](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a2fc5417dbbd91b4099fb4a27f01c18fd)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::max_antenna_paths_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a3307caaaf76bfc5cb1c88937ce788efd)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::nadm_sounding_capability](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a36f4762d9053476e84088fe8807024a3)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::status](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a4fbd5c95fd7f2f9131cd16ff04e64adf)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::t_sw_time_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a61458332899b95c752b6343eda90013e)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::t_pm_times_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a6a88f321faeea9e61bd38c696468d90f)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::modes_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a7131d361abdc12c29a886e338075ae8a)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::rtt_random_payload_n](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a7cc90e1e81657d0b755df281ba6806fc)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::num_config_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a7d3faf86b443db272303d3b4ad45df2d)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::roles_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a7e061a636d3d0432ca9eb65e69a44710)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::t_ip1_times_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a8704313f30e256e87460961f03e0719a)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#a998504553ee046759214d0d220d8a3d3)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::t_ip2_ipt_times_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#ac000a669ee53e1ca4ad99fd350fe72e6)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::cs_sync_phys_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#acb720ede01b7041c9d5b6d6ade065048)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::nadm_random_capability](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#ae3f61c13562d8dec1812fc3c91c23539)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::num_antennas_supported](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#af21e203e96302114a411d9995cd63fa6)
- [bt_hci_rp_le_read_local_supported_capabilities_v2::rtt_capability](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md#afc6a9b21d8926b589cf25941e75ecb31)
- [bt_hci_rp_le_read_local_supported_capabilities::roles_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a0958a5426e0057e2b8ccb80c222d0248)
- [bt_hci_rp_le_read_local_supported_capabilities::nadm_random_capability](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a0e0bd5b1c624c7143b0229b5d3eeec6e)
- [bt_hci_rp_le_read_local_supported_capabilities::t_ip1_times_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a115ffe697da3e09ece4091493fa8f2da)
- [bt_hci_rp_le_read_local_supported_capabilities::tx_snr_capability](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a1806f2f5ec2738b026453bbdb8b38ce9)
- [bt_hci_rp_le_read_local_supported_capabilities::rtt_capability](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a24ffa02b6a8bfbff8b7d32f5ee46bea5)
- [bt_hci_rp_le_read_local_supported_capabilities::rtt_aa_only_n](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a3a16c62ea321620608d706a80d90575e)
- [bt_hci_rp_le_read_local_supported_capabilities::nadm_sounding_capability](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a3eb4830443e7912bf8ca97f603b91545)
- [bt_hci_rp_le_read_local_supported_capabilities::num_config_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a5f59d0b65cc4e7e44e487fa5535b76a9)
- [bt_hci_rp_le_read_local_supported_capabilities::max_antenna_paths_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a7975eb0ce27f0326d1d909bffef57840)
- [bt_hci_rp_le_read_local_supported_capabilities::t_fcs_times_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a81bd809a734b6cdde2d55e0b23e41237)
- [bt_hci_rp_le_read_local_supported_capabilities::t_ip2_times_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a88a4277c5dea41b8171c33c85ed760bf)
- [bt_hci_rp_le_read_local_supported_capabilities::subfeatures_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#a8e7cc92cc4099774e8d0b385fc5f3d79)
- [bt_hci_rp_le_read_local_supported_capabilities::modes_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#aaf09d10c19980729ef04654114919211)
- [bt_hci_rp_le_read_local_supported_capabilities::status](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#aaf578336893980f2ec1b2343b81860e5)
- [bt_hci_rp_le_read_local_supported_capabilities::t_pm_times_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ab026e5abfdead47eca1c5d8d316bc62c)
- [bt_hci_rp_le_read_local_supported_capabilities::rtt_sounding_n](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ababf476100298c2ba7d79bdadd7a9d1b)
- [bt_hci_rp_le_read_local_supported_capabilities::t_sw_time_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ad07b464737c59b33de4c89948d4c5686)
- [bt_hci_rp_le_read_local_supported_capabilities::max_consecutive_procedures_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ad667ba51ffdbaf7754dea6f519615cb7)
- [bt_hci_rp_le_read_local_supported_capabilities::rtt_random_payload_n](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ad90ce3e635b8bccd29eefe73303f6e42)
- [bt_hci_rp_le_read_local_supported_capabilities::num_antennas_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#ae0767bb41b7b57e955ddbede2f83c166)
- [bt_hci_rp_le_read_local_supported_capabilities::cs_sync_phys_supported](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md#af3d1e7588f2429bb400fac81733748c3)
- [bt_hci_rp_le_read_max_adv_data_len::status](../bluetooth_hci_model_reference/P366_bt_hci_rp_le_read_max_adv_data_len_结构体.md#a978911dc5028d1f36820447de8e9e5f7)
- [bt_hci_rp_le_read_max_adv_data_len::max_adv_data_len](../bluetooth_hci_model_reference/P366_bt_hci_rp_le_read_max_adv_data_len_结构体.md#aa4084a89de4929c3e8e2630d0aad7f82)
- [bt_hci_rp_le_read_max_data_len::max_tx_octets](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md#a2c0b159c6248cb9df458d587f82a4152)
- [bt_hci_rp_le_read_max_data_len::status](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md#a654b34b1ee038bf442550a340a26070c)
- [bt_hci_rp_le_read_max_data_len::max_tx_time](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md#a6adc84bf3cc86f234e61982d871899b6)
- [bt_hci_rp_le_read_max_data_len::max_rx_octets](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md#a9273dac6614f1e120f0539b746bfd6cc)
- [bt_hci_rp_le_read_max_data_len::max_rx_time](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md#a963ef9c097906c8db46c35459eb4ecab)
- [bt_hci_rp_le_read_num_adv_sets::status](../bluetooth_hci_model_reference/P368_bt_hci_rp_le_read_num_adv_sets_结构体.md#a590934059fb851a14b2eec66f32a5334)
- [bt_hci_rp_le_read_num_adv_sets::num_sets](../bluetooth_hci_model_reference/P368_bt_hci_rp_le_read_num_adv_sets_结构体.md#a7dd26bda7a8ab75fed2af19bb5af34fc)
- [bt_hci_rp_le_read_peer_rpa::peer_rpa](../bluetooth_hci_model_reference/P369_bt_hci_rp_le_read_peer_rpa_结构体.md#a4eeee179819865ba5d5171d9bd33e5e9)
- [bt_hci_rp_le_read_peer_rpa::status](../bluetooth_hci_model_reference/P369_bt_hci_rp_le_read_peer_rpa_结构体.md#a9c8c799e8c9fbb9f64865e55cdb1f9ef)
- [bt_hci_rp_le_read_per_adv_list_size::status](../bluetooth_hci_model_reference/P370_bt_hci_rp_le_read_per_adv_list_size_结构体.md#a70aa5b466bdbbd309fc59570625c35e5)
- [bt_hci_rp_le_read_per_adv_list_size::list_size](../bluetooth_hci_model_reference/P370_bt_hci_rp_le_read_per_adv_list_size_结构体.md#ab6c4ed1037327669aef623f3a1e9d601)
- [bt_hci_rp_le_read_phy::rx_phy](../bluetooth_hci_model_reference/P371_bt_hci_rp_le_read_phy_结构体.md#a5a060e0c0d1e5f33222ab10a5d3977e8)
- [bt_hci_rp_le_read_phy::tx_phy](../bluetooth_hci_model_reference/P371_bt_hci_rp_le_read_phy_结构体.md#a644c0065d97e5de006dc28f7bca62268)
- [bt_hci_rp_le_read_phy::status](../bluetooth_hci_model_reference/P371_bt_hci_rp_le_read_phy_结构体.md#a65d412e37eb2cd839fae262f4f9d5b28)
- [bt_hci_rp_le_read_phy::handle](../bluetooth_hci_model_reference/P371_bt_hci_rp_le_read_phy_结构体.md#ae708b4f8ad2632d73bedea640f138d9f)
- [bt_hci_rp_le_read_rf_path_comp::rx_path_comp](../bluetooth_hci_model_reference/P372_bt_hci_rp_le_read_rf_path_comp_结构体.md#a0f46a99c74006dc0a4dfd1a49c72e077)
- [bt_hci_rp_le_read_rf_path_comp::tx_path_comp](../bluetooth_hci_model_reference/P372_bt_hci_rp_le_read_rf_path_comp_结构体.md#a827fa954277823efdc5838c317a1460a)
- [bt_hci_rp_le_read_rf_path_comp::status](../bluetooth_hci_model_reference/P372_bt_hci_rp_le_read_rf_path_comp_结构体.md#a84a04bcc64ea6d50fe41e9b416a5ada1)
- [bt_hci_rp_le_read_rl_size::rl_size](../bluetooth_hci_model_reference/P373_bt_hci_rp_le_read_rl_size_结构体.md#a90c28070ee094c99c21c4dd229ff6ce5)
- [bt_hci_rp_le_read_rl_size::status](../bluetooth_hci_model_reference/P373_bt_hci_rp_le_read_rl_size_结构体.md#af8a10aab21d54cce3529b1307769f6c6)
- [bt_hci_rp_le_read_supp_states::le_states](../bluetooth_hci_model_reference/P374_bt_hci_rp_le_read_supp_states_结构体.md#a9b60476cc158a701b29b28bd21375130)
- [bt_hci_rp_le_read_supp_states::status](../bluetooth_hci_model_reference/P374_bt_hci_rp_le_read_supp_states_结构体.md#aeed0cc41ee521c27f07d8cbf4b377a4f)
- [bt_hci_rp_le_read_test_counters::handle](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md#a8121f879a3fb5550cc1aa468aacb81b7)
- [bt_hci_rp_le_read_test_counters::received_cnt](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md#a8c4b2674fb129ca0de0bc45c608e13c7)
- [bt_hci_rp_le_read_test_counters::status](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md#ae1e78d68e9f55b31092a07575a66c1c0)
- [bt_hci_rp_le_read_test_counters::missed_cnt](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md#ae96d05ffb2fbc681c804b04c8791aeab)
- [bt_hci_rp_le_read_test_counters::failed_cnt](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md#af6261d3547cd9b377fedc7a36891c2f7)
- [bt_hci_rp_le_read_tx_power_level::status](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md#a4c83db208bfcb7c9fd2211d192a26d90)
- [bt_hci_rp_le_read_tx_power_level::max_tx_power_level](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md#a5f9c59660f7c5842712a4ad9ae1d9527)
- [bt_hci_rp_le_read_tx_power_level::current_tx_power_level](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md#ad14f660eb67f1014d1a62b0e5a113969)
- [bt_hci_rp_le_read_tx_power_level::phy](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md#ae65a43aad74b1081e88afdb533cbe813)
- [bt_hci_rp_le_read_tx_power_level::handle](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md#aec00dfb34abce2d95af183b74f63d1f3)
- [bt_hci_rp_le_read_tx_power::max_tx_power](../bluetooth_hci_model_reference/P376_bt_hci_rp_le_read_tx_power_结构体.md#a1d794f1f7ea77eceac7dae2546eab047)
- [bt_hci_rp_le_read_tx_power::min_tx_power](../bluetooth_hci_model_reference/P376_bt_hci_rp_le_read_tx_power_结构体.md#a6d4ab95efda5cfc97ae11d83787da8d7)
- [bt_hci_rp_le_read_tx_power::status](../bluetooth_hci_model_reference/P376_bt_hci_rp_le_read_tx_power_结构体.md#a805629b92c65e006082d819f578ed555)
- [bt_hci_rp_le_reject_cis::handle](../bluetooth_hci_model_reference/P378_bt_hci_rp_le_reject_cis_结构体.md#acd8311e13bdfd7edb2d404d80006f9d4)
- [bt_hci_rp_le_reject_cis::status](../bluetooth_hci_model_reference/P378_bt_hci_rp_le_reject_cis_结构体.md#af2dc8a839d3e19821ab8ec0d3dc427ec)
- [bt_hci_rp_le_remove_cig::status](../bluetooth_hci_model_reference/P379_bt_hci_rp_le_remove_cig_结构体.md#a1335f26f1dc67ff8e2a1960d1b24b1a0)
- [bt_hci_rp_le_remove_cig::cig_id](../bluetooth_hci_model_reference/P379_bt_hci_rp_le_remove_cig_结构体.md#a82e74fbbce714b035b1e53fd5f1b09b5)
- [bt_hci_rp_le_remove_iso_path::status](../bluetooth_hci_model_reference/P380_bt_hci_rp_le_remove_iso_path_结构体.md#ab22e50e594e19931526feacd9bff33a3)
- [bt_hci_rp_le_remove_iso_path::handle](../bluetooth_hci_model_reference/P380_bt_hci_rp_le_remove_iso_path_结构体.md#ae3b7704359989ca13582a5cd3742f588)
- [bt_hci_rp_le_set_cig_params_test::handle](../bluetooth_hci_model_reference/P382_bt_hci_rp_le_set_cig_params_test_结构体.md#a08b07863ed63ab627401c0c80bc3c7b4)
- [bt_hci_rp_le_set_cig_params_test::num_handles](../bluetooth_hci_model_reference/P382_bt_hci_rp_le_set_cig_params_test_结构体.md#a10816d0875092c8e6bd4b13b819c43c7)
- [bt_hci_rp_le_set_cig_params_test::cig_id](../bluetooth_hci_model_reference/P382_bt_hci_rp_le_set_cig_params_test_结构体.md#a65c11059bc00244e58d2ab8373e3e725)
- [bt_hci_rp_le_set_cig_params_test::status](../bluetooth_hci_model_reference/P382_bt_hci_rp_le_set_cig_params_test_结构体.md#a932eadb4d750f79b4a7a9c3feb90fdcd)
- [bt_hci_rp_le_set_cig_params::handle](../bluetooth_hci_model_reference/P381_bt_hci_rp_le_set_cig_params_结构体.md#a2e95c6217d11169a8a611ea95dce70b6)
- [bt_hci_rp_le_set_cig_params::status](../bluetooth_hci_model_reference/P381_bt_hci_rp_le_set_cig_params_结构体.md#a8426a2b9927bee05fb9a46b4b261c743)
- [bt_hci_rp_le_set_cig_params::num_handles](../bluetooth_hci_model_reference/P381_bt_hci_rp_le_set_cig_params_结构体.md#a8aff643e0ae41455eb9391cfdb45ebda)
- [bt_hci_rp_le_set_cig_params::cig_id](../bluetooth_hci_model_reference/P381_bt_hci_rp_le_set_cig_params_结构体.md#a951dc88e0cde4e1f0274684498741eac)
- [bt_hci_rp_le_set_cl_cte_sampling_enable::sync_handle](../bluetooth_hci_model_reference/P383_bt_hci_rp_le_set_cl_cte_sampling_enable_结构体.md#a44db7f831e8d730ec3c80c01ef9543aa)
- [bt_hci_rp_le_set_cl_cte_sampling_enable::status](../bluetooth_hci_model_reference/P383_bt_hci_rp_le_set_cl_cte_sampling_enable_结构体.md#a5962f97cef6e53452cdccab1c3440519)
- [bt_hci_rp_le_set_conn_cte_rx_params::handle](../bluetooth_hci_model_reference/P384_bt_hci_rp_le_set_conn_cte_rx_params_结构体.md#a3c3fb92d422e7ccaf0c98706d46b3e5a)
- [bt_hci_rp_le_set_conn_cte_rx_params::status](../bluetooth_hci_model_reference/P384_bt_hci_rp_le_set_conn_cte_rx_params_结构体.md#ad38bb356876c16904e408405607de73c)
- [bt_hci_rp_le_set_conn_cte_tx_params::status](../bluetooth_hci_model_reference/P385_bt_hci_rp_le_set_conn_cte_tx_params_结构体.md#a56f62b6d2c42cd22f73026a2fabc6986)
- [bt_hci_rp_le_set_conn_cte_tx_params::handle](../bluetooth_hci_model_reference/P385_bt_hci_rp_le_set_conn_cte_tx_params_结构体.md#aad553d484daed7ca08de132f4fb849ee)
- [bt_hci_rp_le_set_data_len::handle](../bluetooth_hci_model_reference/P386_bt_hci_rp_le_set_data_len_结构体.md#a207c6da11e0bb145bed7a9e551ddc608)
- [bt_hci_rp_le_set_data_len::status](../bluetooth_hci_model_reference/P386_bt_hci_rp_le_set_data_len_结构体.md#a8667db355a95691d58845f89e919aea4)
- [bt_hci_rp_le_set_ext_adv_param::status](../bluetooth_hci_model_reference/P387_bt_hci_rp_le_set_ext_adv_param_结构体.md#a6baae317455ffbb489066fcd1fb068c8)
- [bt_hci_rp_le_set_ext_adv_param::tx_power](../bluetooth_hci_model_reference/P387_bt_hci_rp_le_set_ext_adv_param_结构体.md#a8a876d0e3d4d9d066a27c054569f0b9a)
- [bt_hci_rp_le_set_host_feature::status](../bluetooth_hci_model_reference/P388_bt_hci_rp_le_set_host_feature_结构体.md#a2e7cfc16da9fc0d00c35111811bf7c28)
- [bt_hci_rp_le_set_path_loss_reporting_enable::status](../bluetooth_hci_model_reference/P389_bt_hci_rp_le_set_path_loss_reporting_enable_结构体.md#a27991d6f123fabf13ecd926cff4e5637)
- [bt_hci_rp_le_set_path_loss_reporting_enable::handle](../bluetooth_hci_model_reference/P389_bt_hci_rp_le_set_path_loss_reporting_enable_结构体.md#a3ea4ffd2a32c8fb720ce555db4585888)
- [bt_hci_rp_le_set_path_loss_reporting_parameters::handle](../bluetooth_hci_model_reference/P390_bt_hci_rp_le_set_path_loss_reporting_parameters_结构体.md#a7a2fb4061792d4cc004c77ac8d5e84dc)
- [bt_hci_rp_le_set_path_loss_reporting_parameters::status](../bluetooth_hci_model_reference/P390_bt_hci_rp_le_set_path_loss_reporting_parameters_结构体.md#afeb9563db35ddba7ed9de6070463c508)
- [bt_hci_rp_le_setup_iso_path::handle](../bluetooth_hci_model_reference/P391_bt_hci_rp_le_setup_iso_path_结构体.md#aa8effdcc4ba155b840ef789f20bad19e)
- [bt_hci_rp_le_setup_iso_path::status](../bluetooth_hci_model_reference/P391_bt_hci_rp_le_setup_iso_path_结构体.md#adde60b0dc6ec3d8caccae1d55d78d9a4)
- [bt_hci_rp_le_test_end::status](../bluetooth_hci_model_reference/P392_bt_hci_rp_le_test_end_结构体.md#a2ac412ef9a5fc7651315afe042856cce)
- [bt_hci_rp_le_test_end::rx_pkt_count](../bluetooth_hci_model_reference/P392_bt_hci_rp_le_test_end_结构体.md#a9e283118e4ea48b0df66a4cd1c1cf9a1)
- [bt_hci_rp_pin_code_neg_reply::status](../bluetooth_hci_model_reference/P399_bt_hci_rp_pin_code_neg_reply_结构体.md#a10bcc55407e22417256c464684a41e58)
- [bt_hci_rp_pin_code_neg_reply::bdaddr](../bluetooth_hci_model_reference/P399_bt_hci_rp_pin_code_neg_reply_结构体.md#a168caf2a517aa573bd6acaf48e414e9b)
- [bt_hci_rp_pin_code_reply::status](../bluetooth_hci_model_reference/P400_bt_hci_rp_pin_code_reply_结构体.md#a3f167661b8d3f63ab12e6f64fb33986b)
- [bt_hci_rp_pin_code_reply::bdaddr](../bluetooth_hci_model_reference/P400_bt_hci_rp_pin_code_reply_结构体.md#afc7c991fd8050e8aae56b8587b5ee01d)
- [bt_hci_rp_read_auth_payload_timeout::status](../bluetooth_hci_model_reference/P401_bt_hci_rp_read_auth_payload_timeout_结构体.md#a3eadeab880eb75c914be654dbc685f3f)
- [bt_hci_rp_read_auth_payload_timeout::auth_payload_timeout](../bluetooth_hci_model_reference/P401_bt_hci_rp_read_auth_payload_timeout_结构体.md#ab4092720dad9a01f4e179eb2f0112aed)
- [bt_hci_rp_read_auth_payload_timeout::handle](../bluetooth_hci_model_reference/P401_bt_hci_rp_read_auth_payload_timeout_结构体.md#ab53b7e03c68dcd040e38fdc7429b2d3b)
- [bt_hci_rp_read_bd_addr::status](../bluetooth_hci_model_reference/P402_bt_hci_rp_read_bd_addr_结构体.md#a5230de2a3a6c4161d076b59901790e1e)
- [bt_hci_rp_read_bd_addr::bdaddr](../bluetooth_hci_model_reference/P402_bt_hci_rp_read_bd_addr_结构体.md#aec2c022a465982a3868100699c95f4e6)
- [bt_hci_rp_read_buffer_size::status](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md#a6adf126acfcec722dc078d097d2b2ba8)
- [bt_hci_rp_read_buffer_size::sco_max_len](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md#a7d475559145f469006b2ef147704cd99)
- [bt_hci_rp_read_buffer_size::acl_max_num](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md#a87ff361282be71aa60c7f88c50a7492f)
- [bt_hci_rp_read_buffer_size::acl_max_len](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md#aba3f1597c929e3721c769beb98000218)
- [bt_hci_rp_read_buffer_size::sco_max_num](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md#abc01fa1df6d787f0a2cb865daed5f4cc)
- [bt_hci_rp_read_class_of_device::status](../bluetooth_hci_model_reference/P404_bt_hci_rp_read_class_of_device_结构体.md#a221d175e8016fd04151c4969d1134910)
- [bt_hci_rp_read_class_of_device::class_of_device](../bluetooth_hci_model_reference/P404_bt_hci_rp_read_class_of_device_结构体.md#ac6483440d3095de548f477cd845c0cee)
- [bt_hci_rp_read_codec_capabilities::num_capabilities](../bluetooth_hci_model_reference/P405_bt_hci_rp_read_codec_capabilities_结构体.md#a71b7df63502bf42a26868e69893ddcfe)
- [bt_hci_rp_read_codec_capabilities::status](../bluetooth_hci_model_reference/P405_bt_hci_rp_read_codec_capabilities_结构体.md#ac224ea998e3af12f97232288266da8d2)
- [bt_hci_rp_read_codec_capabilities::capabilities](../bluetooth_hci_model_reference/P405_bt_hci_rp_read_codec_capabilities_结构体.md#ae0c84013512c461f3b6231162d6f3020)
- [bt_hci_rp_read_codecs_v2::codecs](../bluetooth_hci_model_reference/P407_bt_hci_rp_read_codecs_v2_结构体.md#a098563f274de085ac97415f1b5e15f3c)
- [bt_hci_rp_read_codecs_v2::status](../bluetooth_hci_model_reference/P407_bt_hci_rp_read_codecs_v2_结构体.md#a2e9866d0f9fb42b54c406a9ea5890913)
- [bt_hci_rp_read_codecs::status](../bluetooth_hci_model_reference/P406_bt_hci_rp_read_codecs_结构体.md#a017182988634c6acbfbfdd7c9609f5dc)
- [bt_hci_rp_read_codecs::codecs](../bluetooth_hci_model_reference/P406_bt_hci_rp_read_codecs_结构体.md#a44e615f375b35cce9f949562555c429b)
- [bt_hci_rp_read_conn_accept_timeout::conn_accept_timeout](../bluetooth_hci_model_reference/P408_bt_hci_rp_read_conn_accept_timeout_结构体.md#a01ca30c92311ec1df19a4cf835ea74cf)
- [bt_hci_rp_read_conn_accept_timeout::status](../bluetooth_hci_model_reference/P408_bt_hci_rp_read_conn_accept_timeout_结构体.md#afeb5888722ee368e02c6b27b75ab2a70)
- [bt_hci_rp_read_ctlr_delay::status](../bluetooth_hci_model_reference/P409_bt_hci_rp_read_ctlr_delay_结构体.md#a2f17081cf767643f3a9ad9d115ef5320)
- [bt_hci_rp_read_ctlr_delay::max_ctlr_delay](../bluetooth_hci_model_reference/P409_bt_hci_rp_read_ctlr_delay_结构体.md#a4c468053c4a86d1ab462c1e6f17f1013)
- [bt_hci_rp_read_ctlr_delay::min_ctlr_delay](../bluetooth_hci_model_reference/P409_bt_hci_rp_read_ctlr_delay_结构体.md#ab48d1d92cdf9470a93487434b3824d17)
- [bt_hci_rp_read_default_link_policy_settings::default_link_policy_settings](../bluetooth_hci_model_reference/P410_bt_hci_rp_read_default_link_policy_settings_结构体.md#a0b4c5e26b1d7f387a86192edd1efcdf2)
- [bt_hci_rp_read_default_link_policy_settings::status](../bluetooth_hci_model_reference/P410_bt_hci_rp_read_default_link_policy_settings_结构体.md#ad2ba59e00a2f2931dd52809029373f46)
- [bt_hci_rp_read_encryption_key_size::status](../bluetooth_hci_model_reference/P411_bt_hci_rp_read_encryption_key_size_结构体.md#a17213ccb9179739aa79c3749a2296f65)
- [bt_hci_rp_read_encryption_key_size::handle](../bluetooth_hci_model_reference/P411_bt_hci_rp_read_encryption_key_size_结构体.md#af0b89b2035f956891244b10409be0f51)
- [bt_hci_rp_read_encryption_key_size::key_size](../bluetooth_hci_model_reference/P411_bt_hci_rp_read_encryption_key_size_结构体.md#af1cd71c6216b26d460c04a68405f05d5)
- [bt_hci_rp_read_link_policy_settings::handle](../bluetooth_hci_model_reference/P412_bt_hci_rp_read_link_policy_settings_结构体.md#a4ec0cdfa8ae48d9ed8ae2d46f16a9638)
- [bt_hci_rp_read_link_policy_settings::link_policy_settings](../bluetooth_hci_model_reference/P412_bt_hci_rp_read_link_policy_settings_结构体.md#a69fe8085d161bf87051a52dc9c511156)
- [bt_hci_rp_read_link_policy_settings::status](../bluetooth_hci_model_reference/P412_bt_hci_rp_read_link_policy_settings_结构体.md#ad73d8ed381f8bbc4914c38bb0ebcae01)
- [bt_hci_rp_read_link_supervision_timeout::status](../bluetooth_hci_model_reference/P413_bt_hci_rp_read_link_supervision_timeout_结构体.md#a1400aa0d8172c0cbf6b24b6571e73f73)
- [bt_hci_rp_read_link_supervision_timeout::timeout](../bluetooth_hci_model_reference/P413_bt_hci_rp_read_link_supervision_timeout_结构体.md#ad1048becb6523d7302fdbbd739bc1b99)
- [bt_hci_rp_read_link_supervision_timeout::handle](../bluetooth_hci_model_reference/P413_bt_hci_rp_read_link_supervision_timeout_结构体.md#aec86b11707e4728dd0849f12c32cf8f8)
- [bt_hci_rp_read_local_ext_features::max_page](../bluetooth_hci_model_reference/P414_bt_hci_rp_read_local_ext_features_结构体.md#a3532e208b3fd347db80d8c55eade3c2d)
- [bt_hci_rp_read_local_ext_features::ext_features](../bluetooth_hci_model_reference/P414_bt_hci_rp_read_local_ext_features_结构体.md#a669e8c6faa4e45f472e4f8a3ebb03050)
- [bt_hci_rp_read_local_ext_features::page](../bluetooth_hci_model_reference/P414_bt_hci_rp_read_local_ext_features_结构体.md#a7e3669651dc2c2ed9541b7e4945a27f9)
- [bt_hci_rp_read_local_ext_features::status](../bluetooth_hci_model_reference/P414_bt_hci_rp_read_local_ext_features_结构体.md#a9011f2c89f75939fa92fcf249d2203da)
- [bt_hci_rp_read_local_features::status](../bluetooth_hci_model_reference/P415_bt_hci_rp_read_local_features_结构体.md#a0ff73da5704ada47f8f79c113254820d)
- [bt_hci_rp_read_local_features::features](../bluetooth_hci_model_reference/P415_bt_hci_rp_read_local_features_结构体.md#ae660b4a772f96bf72bd08124bf26b352)
- [bt_hci_rp_read_local_version_info::hci_revision](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a04161ed3cc0b9c3c442e3464501ce118)
- [bt_hci_rp_read_local_version_info::hci_version](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a1cc521426e530344a328e935152dd488)
- [bt_hci_rp_read_local_version_info::lmp_subversion](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a43f29cf08a2399e818bfa441c6b7a1f3)
- [bt_hci_rp_read_local_version_info::lmp_version](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a634641751852f66aabb408bf1b4d0cd2)
- [bt_hci_rp_read_local_version_info::manufacturer](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a7cd6ba190137eaf7c4eb9c2d7e5b36ce)
- [bt_hci_rp_read_local_version_info::status](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md#a935f990f7c28f7c89660c2b8ab975f43)
- [bt_hci_rp_read_rssi::rssi](../bluetooth_hci_model_reference/P417_bt_hci_rp_read_rssi_结构体.md#a1071300bd61fcaab65683187ae393cae)
- [bt_hci_rp_read_rssi::status](../bluetooth_hci_model_reference/P417_bt_hci_rp_read_rssi_结构体.md#a8f91b69a99bd61a7a59d84b3a9c3f235)
- [bt_hci_rp_read_rssi::handle](../bluetooth_hci_model_reference/P417_bt_hci_rp_read_rssi_结构体.md#aa3c4041dd240b1185c7fc8bbef74a17a)
- [bt_hci_rp_read_supported_commands::status](../bluetooth_hci_model_reference/P418_bt_hci_rp_read_supported_commands_结构体.md#a3d36d892f83cfcb1d2fc955ec71ff061)
- [bt_hci_rp_read_supported_commands::commands](../bluetooth_hci_model_reference/P418_bt_hci_rp_read_supported_commands_结构体.md#afd0dc4411a4c7692515139392bffedd0)
- [bt_hci_rp_read_tx_power_level::tx_power_level](../bluetooth_hci_model_reference/P419_bt_hci_rp_read_tx_power_level_结构体.md#a46526b820038bb445a7824a7b4bfc870)
- [bt_hci_rp_read_tx_power_level::handle](../bluetooth_hci_model_reference/P419_bt_hci_rp_read_tx_power_level_结构体.md#ac2bd21e90145102bc483c2b0b3cdd416)
- [bt_hci_rp_read_tx_power_level::status](../bluetooth_hci_model_reference/P419_bt_hci_rp_read_tx_power_level_结构体.md#af40a8e2e663872e8d9fdde839cc6d1b4)
- [bt_hci_rp_remote_name_cancel::bdaddr](../bluetooth_hci_model_reference/P420_bt_hci_rp_remote_name_cancel_结构体.md#a455432799a1272f88b2b00a35a2e7ef5)
- [bt_hci_rp_remote_name_cancel::status](../bluetooth_hci_model_reference/P420_bt_hci_rp_remote_name_cancel_结构体.md#ac7fadee392b126cb50cef7a6336926cb)
- [bt_hci_rp_sniff_subrating::handle](../bluetooth_hci_model_reference/P421_bt_hci_rp_sniff_subrating_结构体.md#a39e9f3ec6e7d9c534ca6160172990fa6)
- [bt_hci_rp_sniff_subrating::status](../bluetooth_hci_model_reference/P421_bt_hci_rp_sniff_subrating_结构体.md#aa5d11db99d6f467a1e93afe031c08e14)
- [bt_hci_rp_user_confirm_reply::bdaddr](../bluetooth_hci_model_reference/P422_bt_hci_rp_user_confirm_reply_结构体.md#a91678db3ae2a696ba7b9dd5bc080c488)
- [bt_hci_rp_user_confirm_reply::status](../bluetooth_hci_model_reference/P422_bt_hci_rp_user_confirm_reply_结构体.md#ab07114550c2da3c1e9925cb883bf3a89)
- [bt_hci_rp_write_auth_payload_timeout::handle](../bluetooth_hci_model_reference/P434_bt_hci_rp_write_auth_payload_timeout_结构体.md#a467c6585c913dba03dcfdf5bf4fa688e)
- [bt_hci_rp_write_auth_payload_timeout::status](../bluetooth_hci_model_reference/P434_bt_hci_rp_write_auth_payload_timeout_结构体.md#af1783a29e6a167fc20b62bd273215b35)
- [bt_hci_rp_write_conn_accept_timeout::status](../bluetooth_hci_model_reference/P435_bt_hci_rp_write_conn_accept_timeout_结构体.md#a1f9eee1a5843747e0d224b86b602a3da)
- [bt_hci_sco_hdr::len](../bluetooth_hci_model_reference/P436_bt_hci_sco_hdr_结构体.md#a158f67c3743684c28728b62db5cf2590)
- [bt_hci_sco_hdr::handle](../bluetooth_hci_model_reference/P436_bt_hci_sco_hdr_结构体.md#a4b4c915bec966c17567c14e2df9c1581)
- [bt_hci_std_codec_info_v2::codec_id](../bluetooth_hci_model_reference/P439_bt_hci_std_codec_info_v2_结构体.md#ae82a0896904c7feb2634579b393bf05e)
- [bt_hci_std_codec_info_v2::transports](../bluetooth_hci_model_reference/P439_bt_hci_std_codec_info_v2_结构体.md#aea766ba4b911223eeb351e0123e54f5f)
- [bt_hci_std_codec_info::codec_id](../bluetooth_hci_model_reference/P438_bt_hci_std_codec_info_结构体.md#a56e21eca5bbc83cb081aea1c67a7a60d)
- [bt_hci_std_codecs_v2::codec_info](../bluetooth_hci_model_reference/P441_bt_hci_std_codecs_v2_结构体.md#aafdb6d96d99063a7a447d80e1830a624)
- [bt_hci_std_codecs_v2::num_codecs](../bluetooth_hci_model_reference/P441_bt_hci_std_codecs_v2_结构体.md#ab14fdde478e290235f68aae375969c09)
- [bt_hci_std_codecs::codec_info](../bluetooth_hci_model_reference/P440_bt_hci_std_codecs_结构体.md#a32767e90384ef74a3e740597eacfcf53)
- [bt_hci_std_codecs::num_codecs](../bluetooth_hci_model_reference/P440_bt_hci_std_codecs_结构体.md#ad3e63bf445bb6b8e654baa8490cdf547)
- [bt_hci_vs_codec_info_v2::company_id](../bluetooth_hci_model_reference/P444_bt_hci_vs_codec_info_v2_结构体.md#aa6ce27b4acd3dff516e4d7ed2e6434bc)
- [bt_hci_vs_codec_info_v2::transports](../bluetooth_hci_model_reference/P444_bt_hci_vs_codec_info_v2_结构体.md#ac2a91a045e4b53315850b6d4f1d38b2c)
- [bt_hci_vs_codec_info_v2::codec_id](../bluetooth_hci_model_reference/P444_bt_hci_vs_codec_info_v2_结构体.md#ae7b7d5d65629a1e3039b3c7cf167a9c1)
- [bt_hci_vs_codec_info::codec_id](../bluetooth_hci_model_reference/P443_bt_hci_vs_codec_info_结构体.md#a3c7eea7bae36c7a63457051401526382)
- [bt_hci_vs_codec_info::company_id](../bluetooth_hci_model_reference/P443_bt_hci_vs_codec_info_结构体.md#a8170dac825b76f3dfb5fde5eed04c4c0)
- [bt_hci_vs_codecs_v2::codec_info](../bluetooth_hci_model_reference/P446_bt_hci_vs_codecs_v2_结构体.md#a6cd8aa58517d59d565474513f755cfee)
- [bt_hci_vs_codecs_v2::num_codecs](../bluetooth_hci_model_reference/P446_bt_hci_vs_codecs_v2_结构体.md#ae4cb3a40401594f8e0f18391b9d31a23)
- [bt_hci_vs_codecs::num_codecs](../bluetooth_hci_model_reference/P445_bt_hci_vs_codecs_结构体.md#a2caf18ce5905e3962da000f3b00b623f)
- [bt_hci_vs_codecs::codec_info](../bluetooth_hci_model_reference/P445_bt_hci_vs_codecs_结构体.md#a4e72426599d5bc617fde4f1a4a095527)
- [bt_hci_write_local_name::local_name](../bluetooth_hci_model_reference/P450_bt_hci_write_local_name_结构体.md#a8d2cd9a16525c3fc10ae0e3f196110da)
- [hci_cp_le_conn_update::min_ce_len](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#a3ae86fccacf462463fe520eb1e06fa62)
- [hci_cp_le_conn_update::max_ce_len](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#a401169ccc5dbf6cf0abd6154738f00dc)
- [hci_cp_le_conn_update::handle](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#a5606b8795defc338b27d1a130064351e)
- [hci_cp_le_conn_update::conn_latency](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#a8e48e5e195aea7f581cfc7246da79d72)
- [hci_cp_le_conn_update::conn_interval_max](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#a99fc0b3b0f810f1d6e174aa9045d298a)
- [hci_cp_le_conn_update::supervision_timeout](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#ab76ecdf6f7e5a5bb581cbd26f67d8f9f)
- [hci_cp_le_conn_update::conn_interval_min](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md#adcfee3c727118069897515a00e7ead66)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[返回大纲](大纲.md) · [下一章](P002_numaker-m46x-pinctrl.h_源码浏览.md)
