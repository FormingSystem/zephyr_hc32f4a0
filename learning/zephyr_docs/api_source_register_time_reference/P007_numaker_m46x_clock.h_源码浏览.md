---
id: learning.zephyr-docs.api-source-register-time-reference.page-7
title: numaker_m46x_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/numaker__m46x__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_numaker\_m46x\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/numaker__m46x__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P269_zephyr__dt-bindings__clock__numaker_m46x_clock.h_文件参考.md)。

## 7.1\_原始可见代码（Source Code）

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
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
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
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
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
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
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
<a id="l00482"></a>
<a id="l00483"></a>
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
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
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
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
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
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="foldopen00597"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="foldopen00604"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="foldopen00611"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="foldopen00618"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="foldopen00625"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="foldopen00632"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="foldopen00639"></a>
<a id="l00639"></a>
<a id="l00640"></a>
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
<a id="foldopen00653"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="foldopen00660"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="foldopen00667"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="foldopen00674"></a>
<a id="l00674"></a>
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
<a id="foldopen00688"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00691"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="foldopen00695"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="foldopen00702"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="foldopen00709"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="foldopen00716"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="foldopen00723"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="foldopen00730"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="foldopen00737"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="foldopen00744"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="foldopen00751"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="foldopen00758"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="foldopen00765"></a>
<a id="l00765"></a>
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
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="foldopen00779"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="foldopen00787"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="foldopen00794"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="foldopen00801"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
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
<a id="l00814"></a>
<a id="foldopen00815"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="foldopen00822"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="foldopen00829"></a>
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
<a id="l00842"></a>
<a id="l00843"></a>
<a id="foldopen00844"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00846"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="foldopen00851"></a>
<a id="l00851"></a>
<a id="l00852"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="l00857"></a>
<a id="foldopen00858"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="foldopen00865"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00869"></a>
<a id="l00870"></a>
<a id="l00871"></a>
<a id="foldopen00872"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="foldopen00879"></a>
<a id="l00879"></a>
<a id="l00880"></a>
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
<a id="foldopen00900"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="foldopen00907"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="foldopen00914"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="foldopen00921"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="foldopen00928"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="foldopen00935"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="foldopen00942"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00948"></a>
<a id="foldopen00949"></a>
<a id="l00949"></a>
<a id="l00950"></a>
<a id="l00951"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00955"></a>
<a id="foldopen00956"></a>
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00961"></a>
<a id="l00962"></a>
<a id="foldopen00963"></a>
<a id="l00963"></a>
<a id="l00964"></a>
<a id="l00965"></a>
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
<a id="l00975"></a>
<a id="l00976"></a>
<a id="foldopen00977"></a>
<a id="l00977"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="foldopen00984"></a>
<a id="l00984"></a>
<a id="l00985"></a>
<a id="l00986"></a>
<a id="l00987"></a>
<a id="l00988"></a>
<a id="l00989"></a>
<a id="l00990"></a>
<a id="foldopen00991"></a>
<a id="l00991"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="l00997"></a>
<a id="foldopen00998"></a>
<a id="l00998"></a>
<a id="l00999"></a>
<a id="l01000"></a>
<a id="l01001"></a>
<a id="l01002"></a>
<a id="l01003"></a>
<a id="l01004"></a>
<a id="foldopen01005"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="foldopen01012"></a>
<a id="l01012"></a>
<a id="l01013"></a>
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
<a id="l01025"></a>
<a id="foldopen01026"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01032"></a>
<a id="foldopen01033"></a>
<a id="l01033"></a>
<a id="l01034"></a>
<a id="l01035"></a>
<a id="l01036"></a>
<a id="l01037"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="foldopen01040"></a>
<a id="l01040"></a>
<a id="l01041"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="foldopen01048"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01054"></a>
<a id="foldopen01055"></a>
<a id="l01055"></a>
<a id="l01056"></a>
<a id="l01057"></a>
<a id="l01058"></a>
<a id="l01059"></a>
<a id="l01060"></a>
<a id="l01061"></a>
<a id="foldopen01062"></a>
<a id="l01062"></a>
<a id="l01063"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01066"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="foldopen01069"></a>
<a id="l01069"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01073"></a>
<a id="l01074"></a>
<a id="l01075"></a>
<a id="foldopen01076"></a>
<a id="l01076"></a>
<a id="l01077"></a>
<a id="l01078"></a>
<a id="l01079"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01082"></a>
<a id="foldopen01083"></a>
<a id="l01083"></a>
<a id="l01084"></a>
<a id="l01085"></a>
<a id="l01086"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01089"></a>
<a id="foldopen01090"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="l01093"></a>
<a id="l01094"></a>
<a id="l01095"></a>
<a id="l01096"></a>
<a id="foldopen01097"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01101"></a>
<a id="l01102"></a>
<a id="l01103"></a>
<a id="foldopen01104"></a>
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
<a id="l01117"></a>
<a id="foldopen01118"></a>
<a id="l01118"></a>
<a id="l01119"></a>
<a id="l01120"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="foldopen01125"></a>
<a id="l01125"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="foldopen01132"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="l01134"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="foldopen01139"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="foldopen01146"></a>
<a id="l01146"></a>
<a id="l01147"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01150"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="foldopen01153"></a>
<a id="l01153"></a>
<a id="l01154"></a>
<a id="l01155"></a>
<a id="l01156"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01159"></a>
<a id="foldopen01160"></a>
<a id="l01160"></a>
<a id="l01161"></a>
<a id="l01162"></a>
<a id="l01163"></a>
<a id="l01164"></a>
<a id="l01165"></a>
<a id="l01166"></a>
<a id="foldopen01167"></a>
<a id="l01167"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01170"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01173"></a>
<a id="foldopen01174"></a>
<a id="l01174"></a>
<a id="l01175"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01179"></a>
<a id="l01180"></a>
<a id="foldopen01181"></a>
<a id="l01181"></a>
<a id="l01182"></a>
<a id="l01183"></a>
<a id="l01184"></a>
<a id="l01185"></a>
<a id="l01186"></a>
<a id="l01187"></a>
<a id="foldopen01188"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01190"></a>
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
<a id="l01200"></a>
<a id="l01201"></a>
<a id="foldopen01202"></a>
<a id="l01202"></a>
<a id="l01203"></a>
<a id="l01204"></a>
<a id="l01205"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="l01208"></a>
<a id="foldopen01209"></a>
<a id="l01209"></a>
<a id="l01210"></a>
<a id="l01211"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01215"></a>
<a id="foldopen01216"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01221"></a>
<a id="l01222"></a>
<a id="l01223"></a>
<a id="foldopen01224"></a>
<a id="l01224"></a>
<a id="l01225"></a>
<a id="l01226"></a>
<a id="l01227"></a>
<a id="l01228"></a>
<a id="l01229"></a>
<a id="l01230"></a>
<a id="foldopen01231"></a>
<a id="l01231"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="l01234"></a>
<a id="l01235"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="foldopen01238"></a>
<a id="l01238"></a>
<a id="l01239"></a>
<a id="l01240"></a>
<a id="l01241"></a>
<a id="l01242"></a>
<a id="l01243"></a>
<a id="l01244"></a>
<a id="foldopen01245"></a>
<a id="l01245"></a>
<a id="l01246"></a>
<a id="l01247"></a>
<a id="l01248"></a>
<a id="l01249"></a>
<a id="l01250"></a>
<a id="l01251"></a>
<a id="foldopen01252"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01258"></a>
<a id="foldopen01259"></a>
<a id="l01259"></a>
<a id="l01260"></a>
<a id="l01261"></a>
<a id="l01262"></a>
<a id="l01263"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="foldopen01266"></a>
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
<a id="l01278"></a>
<a id="l01279"></a>
<a id="foldopen01280"></a>
<a id="l01280"></a>
<a id="l01281"></a>
<a id="l01282"></a>
<a id="l01283"></a>
<a id="l01284"></a>
<a id="l01285"></a>
<a id="l01286"></a>
<a id="foldopen01287"></a>
<a id="l01287"></a>
<a id="l01288"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="l01291"></a>
<a id="l01292"></a>
<a id="l01293"></a>
<a id="foldopen01294"></a>
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
<a id="l01304"></a>
<a id="l01305"></a>
<a id="l01306"></a>
<a id="l01307"></a>
<a id="l01308"></a>
<a id="l01309"></a>

```c
/*
 * Copyright (c) 2023 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NUMAKER_M46X_CLOCK_H
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NUMAKER_M46X_CLOCK_H

/* Beginning of M460 BSP clk_reg.h copy */

#define NUMAKER_CLK_AHBCLK0_PDMA0CKEN_Pos  (1)
#define NUMAKER_CLK_AHBCLK0_ISPCKEN_Pos    (2)
#define NUMAKER_CLK_AHBCLK0_EBICKEN_Pos    (3)
#define NUMAKER_CLK_AHBCLK0_STCKEN_Pos     (4)
#define NUMAKER_CLK_AHBCLK0_EMAC0CKEN_Pos  (5)
#define NUMAKER_CLK_AHBCLK0_SDH0CKEN_Pos   (6)
#define NUMAKER_CLK_AHBCLK0_CRCCKEN_Pos    (7)
#define NUMAKER_CLK_AHBCLK0_CCAPCKEN_Pos   (8)
#define NUMAKER_CLK_AHBCLK0_SENCKEN_Pos    (9)
#define NUMAKER_CLK_AHBCLK0_HSUSBDCKEN_Pos (10)
#define NUMAKER_CLK_AHBCLK0_HBICKEN_Pos    (11)
#define NUMAKER_CLK_AHBCLK0_CRPTCKEN_Pos   (12)
#define NUMAKER_CLK_AHBCLK0_KSCKEN_Pos     (13)
#define NUMAKER_CLK_AHBCLK0_SPIMCKEN_Pos   (14)
#define NUMAKER_CLK_AHBCLK0_FMCIDLE_Pos    (15)
#define NUMAKER_CLK_AHBCLK0_USBHCKEN_Pos   (16)
#define NUMAKER_CLK_AHBCLK0_SDH1CKEN_Pos   (17)
#define NUMAKER_CLK_AHBCLK0_PDMA1CKEN_Pos  (18)
#define NUMAKER_CLK_AHBCLK0_TRACECKEN_Pos  (19)
#define NUMAKER_CLK_AHBCLK0_GPACKEN_Pos    (24)
#define NUMAKER_CLK_AHBCLK0_GPBCKEN_Pos    (25)
#define NUMAKER_CLK_AHBCLK0_GPCCKEN_Pos    (26)
#define NUMAKER_CLK_AHBCLK0_GPDCKEN_Pos    (27)
#define NUMAKER_CLK_AHBCLK0_GPECKEN_Pos    (28)
#define NUMAKER_CLK_AHBCLK0_GPFCKEN_Pos    (29)
#define NUMAKER_CLK_AHBCLK0_GPGCKEN_Pos    (30)
#define NUMAKER_CLK_AHBCLK0_GPHCKEN_Pos    (31)

#define NUMAKER_CLK_APBCLK0_WDTCKEN_Pos    (0)
#define NUMAKER_CLK_APBCLK0_RTCCKEN_Pos    (1)
#define NUMAKER_CLK_APBCLK0_TMR0CKEN_Pos   (2)
#define NUMAKER_CLK_APBCLK0_TMR1CKEN_Pos   (3)
#define NUMAKER_CLK_APBCLK0_TMR2CKEN_Pos   (4)
#define NUMAKER_CLK_APBCLK0_TMR3CKEN_Pos   (5)
#define NUMAKER_CLK_APBCLK0_CLKOCKEN_Pos   (6)
#define NUMAKER_CLK_APBCLK0_ACMP01CKEN_Pos (7)
#define NUMAKER_CLK_APBCLK0_I2C0CKEN_Pos   (8)
#define NUMAKER_CLK_APBCLK0_I2C1CKEN_Pos   (9)
#define NUMAKER_CLK_APBCLK0_I2C2CKEN_Pos   (10)
#define NUMAKER_CLK_APBCLK0_I2C3CKEN_Pos   (11)
#define NUMAKER_CLK_APBCLK0_QSPI0CKEN_Pos  (12)
#define NUMAKER_CLK_APBCLK0_SPI0CKEN_Pos   (13)
#define NUMAKER_CLK_APBCLK0_SPI1CKEN_Pos   (14)
#define NUMAKER_CLK_APBCLK0_SPI2CKEN_Pos   (15)
#define NUMAKER_CLK_APBCLK0_UART0CKEN_Pos  (16)
#define NUMAKER_CLK_APBCLK0_UART1CKEN_Pos  (17)
#define NUMAKER_CLK_APBCLK0_UART2CKEN_Pos  (18)
#define NUMAKER_CLK_APBCLK0_UART3CKEN_Pos  (19)
#define NUMAKER_CLK_APBCLK0_UART4CKEN_Pos  (20)
#define NUMAKER_CLK_APBCLK0_UART5CKEN_Pos  (21)
#define NUMAKER_CLK_APBCLK0_UART6CKEN_Pos  (22)
#define NUMAKER_CLK_APBCLK0_UART7CKEN_Pos  (23)
#define NUMAKER_CLK_APBCLK0_OTGCKEN_Pos    (26)
#define NUMAKER_CLK_APBCLK0_USBDCKEN_Pos   (27)
#define NUMAKER_CLK_APBCLK0_EADC0CKEN_Pos  (28)
#define NUMAKER_CLK_APBCLK0_I2S0CKEN_Pos   (29)
#define NUMAKER_CLK_APBCLK0_HSOTGCKEN_Pos  (30)
#define NUMAKER_CLK_APBCLK1_SC0CKEN_Pos    (0)
#define NUMAKER_CLK_APBCLK1_SC1CKEN_Pos    (1)
#define NUMAKER_CLK_APBCLK1_SC2CKEN_Pos    (2)
#define NUMAKER_CLK_APBCLK1_I2C4CKEN_Pos   (3)
#define NUMAKER_CLK_APBCLK1_QSPI1CKEN_Pos  (4)
#define NUMAKER_CLK_APBCLK1_SPI3CKEN_Pos   (6)
#define NUMAKER_CLK_APBCLK1_SPI4CKEN_Pos   (7)
#define NUMAKER_CLK_APBCLK1_USCI0CKEN_Pos  (8)
#define NUMAKER_CLK_APBCLK1_PSIOCKEN_Pos   (10)
#define NUMAKER_CLK_APBCLK1_DACCKEN_Pos    (12)
#define NUMAKER_CLK_APBCLK1_ECAP2CKEN_Pos  (13)
#define NUMAKER_CLK_APBCLK1_ECAP3CKEN_Pos  (14)
#define NUMAKER_CLK_APBCLK1_EPWM0CKEN_Pos  (16)
#define NUMAKER_CLK_APBCLK1_EPWM1CKEN_Pos  (17)
#define NUMAKER_CLK_APBCLK1_BPWM0CKEN_Pos  (18)
#define NUMAKER_CLK_APBCLK1_BPWM1CKEN_Pos  (19)
#define NUMAKER_CLK_APBCLK1_EQEI2CKEN_Pos  (20)
#define NUMAKER_CLK_APBCLK1_EQEI3CKEN_Pos  (21)
#define NUMAKER_CLK_APBCLK1_EQEI0CKEN_Pos  (22)
#define NUMAKER_CLK_APBCLK1_EQEI1CKEN_Pos  (23)
#define NUMAKER_CLK_APBCLK1_TRNGCKEN_Pos   (25)
#define NUMAKER_CLK_APBCLK1_ECAP0CKEN_Pos  (26)
#define NUMAKER_CLK_APBCLK1_ECAP1CKEN_Pos  (27)
#define NUMAKER_CLK_APBCLK1_I2S1CKEN_Pos   (29)
#define NUMAKER_CLK_APBCLK1_EADC1CKEN_Pos  (31)

#define NUMAKER_CLK_CLKSEL0_HCLKSEL_Pos   (0)
#define NUMAKER_CLK_CLKSEL0_STCLKSEL_Pos  (3)
#define NUMAKER_CLK_CLKSEL0_USBSEL_Pos    (8)
#define NUMAKER_CLK_CLKSEL0_EADC0SEL_Pos  (10)
#define NUMAKER_CLK_CLKSEL0_EADC1SEL_Pos  (12)
#define NUMAKER_CLK_CLKSEL0_EADC2SEL_Pos  (14)
#define NUMAKER_CLK_CLKSEL0_CCAPSEL_Pos   (16)
#define NUMAKER_CLK_CLKSEL0_SDH0SEL_Pos   (20)
#define NUMAKER_CLK_CLKSEL0_SDH1SEL_Pos   (22)
#define NUMAKER_CLK_CLKSEL0_CANFD0SEL_Pos (24)
#define NUMAKER_CLK_CLKSEL0_CANFD1SEL_Pos (26)
#define NUMAKER_CLK_CLKSEL0_CANFD2SEL_Pos (28)
#define NUMAKER_CLK_CLKSEL0_CANFD3SEL_Pos (30)
#define NUMAKER_CLK_CLKSEL1_WDTSEL_Pos    (0)
#define NUMAKER_CLK_CLKSEL1_CLKOSEL_Pos   (4)
#define NUMAKER_CLK_CLKSEL1_TMR0SEL_Pos   (8)
#define NUMAKER_CLK_CLKSEL1_TMR1SEL_Pos   (12)
#define NUMAKER_CLK_CLKSEL1_TMR2SEL_Pos   (16)
#define NUMAKER_CLK_CLKSEL1_TMR3SEL_Pos   (20)
#define NUMAKER_CLK_CLKSEL1_UART0SEL_Pos  (24)
#define NUMAKER_CLK_CLKSEL1_UART1SEL_Pos  (26)
#define NUMAKER_CLK_CLKSEL1_WWDTSEL_Pos   (30)
#define NUMAKER_CLK_CLKSEL2_EPWM0SEL_Pos  (0)
#define NUMAKER_CLK_CLKSEL2_EPWM1SEL_Pos  (1)
#define NUMAKER_CLK_CLKSEL2_QSPI0SEL_Pos  (2)
#define NUMAKER_CLK_CLKSEL2_SPI0SEL_Pos   (4)
#define NUMAKER_CLK_CLKSEL2_BPWM0SEL_Pos  (8)
#define NUMAKER_CLK_CLKSEL2_BPWM1SEL_Pos  (9)
#define NUMAKER_CLK_CLKSEL2_QSPI1SEL_Pos  (10)
#define NUMAKER_CLK_CLKSEL2_SPI1SEL_Pos   (12)
#define NUMAKER_CLK_CLKSEL2_I2S1SEL_Pos   (16)
#define NUMAKER_CLK_CLKSEL2_UART8SEL_Pos  (20)
#define NUMAKER_CLK_CLKSEL2_UART9SEL_Pos  (22)
#define NUMAKER_CLK_CLKSEL2_TRNGSEL_Pos   (27)
#define NUMAKER_CLK_CLKSEL2_PSIOSEL_Pos   (28)
#define NUMAKER_CLK_CLKSEL3_SC0SEL_Pos    (0)
#define NUMAKER_CLK_CLKSEL3_SC1SEL_Pos    (2)
#define NUMAKER_CLK_CLKSEL3_SC2SEL_Pos    (4)
#define NUMAKER_CLK_CLKSEL3_KPISEL_Pos    (6)
#define NUMAKER_CLK_CLKSEL3_SPI2SEL_Pos   (9)
#define NUMAKER_CLK_CLKSEL3_SPI3SEL_Pos   (12)
#define NUMAKER_CLK_CLKSEL3_I2S0SEL_Pos   (16)
#define NUMAKER_CLK_CLKSEL3_UART6SEL_Pos  (20)
#define NUMAKER_CLK_CLKSEL3_UART7SEL_Pos  (22)
#define NUMAKER_CLK_CLKSEL3_UART2SEL_Pos  (24)
#define NUMAKER_CLK_CLKSEL3_UART3SEL_Pos  (26)
#define NUMAKER_CLK_CLKSEL3_UART4SEL_Pos  (28)
#define NUMAKER_CLK_CLKSEL3_UART5SEL_Pos  (30)

#define NUMAKER_CLK_CLKDIV0_HCLKDIV_Pos   (0)
#define NUMAKER_CLK_CLKDIV0_USBDIV_Pos    (4)
#define NUMAKER_CLK_CLKDIV0_UART0DIV_Pos  (8)
#define NUMAKER_CLK_CLKDIV0_UART1DIV_Pos  (12)
#define NUMAKER_CLK_CLKDIV0_EADC0DIV_Pos  (16)
#define NUMAKER_CLK_CLKDIV0_SDH0DIV_Pos   (24)
#define NUMAKER_CLK_CLKDIV1_SC0DIV_Pos    (0)
#define NUMAKER_CLK_CLKDIV1_SC1DIV_Pos    (8)
#define NUMAKER_CLK_CLKDIV1_SC2DIV_Pos    (16)
#define NUMAKER_CLK_CLKDIV1_PSIODIV_Pos   (24)
#define NUMAKER_CLK_CLKDIV2_I2S0DIV_Pos   (0)
#define NUMAKER_CLK_CLKDIV2_I2S1DIV_Pos   (4)
#define NUMAKER_CLK_CLKDIV2_KPIDIV_Pos    (8)
#define NUMAKER_CLK_CLKDIV2_EADC1DIV_Pos  (24)
#define NUMAKER_CLK_CLKDIV3_VSENSEDIV_Pos (8)
#define NUMAKER_CLK_CLKDIV3_EMAC0DIV_Pos  (16)
#define NUMAKER_CLK_CLKDIV3_SDH1DIV_Pos   (24)
#define NUMAKER_CLK_CLKDIV4_UART2DIV_Pos  (0)
#define NUMAKER_CLK_CLKDIV4_UART3DIV_Pos  (4)
#define NUMAKER_CLK_CLKDIV4_UART4DIV_Pos  (8)
#define NUMAKER_CLK_CLKDIV4_UART5DIV_Pos  (12)
#define NUMAKER_CLK_CLKDIV4_UART6DIV_Pos  (16)
#define NUMAKER_CLK_CLKDIV4_UART7DIV_Pos  (20)

#define NUMAKER_CLK_PCLKDIV_APB0DIV_Pos (0)
#define NUMAKER_CLK_PCLKDIV_APB1DIV_Pos (4)

#define NUMAKER_CLK_APBCLK2_KPICKEN_Pos    (0)
#define NUMAKER_CLK_APBCLK2_EADC2CKEN_Pos  (6)
#define NUMAKER_CLK_APBCLK2_ACMP23CKEN_Pos (7)
#define NUMAKER_CLK_APBCLK2_SPI5CKEN_Pos   (8)
#define NUMAKER_CLK_APBCLK2_SPI6CKEN_Pos   (9)
#define NUMAKER_CLK_APBCLK2_SPI7CKEN_Pos   (10)
#define NUMAKER_CLK_APBCLK2_SPI8CKEN_Pos   (11)
#define NUMAKER_CLK_APBCLK2_SPI9CKEN_Pos   (12)
#define NUMAKER_CLK_APBCLK2_SPI10CKEN_Pos  (13)
#define NUMAKER_CLK_APBCLK2_UART8CKEN_Pos  (16)
#define NUMAKER_CLK_APBCLK2_UART9CKEN_Pos  (17)

#define NUMAKER_CLK_CLKDIV5_CANFD0DIV_Pos (0)
#define NUMAKER_CLK_CLKDIV5_CANFD1DIV_Pos (4)
#define NUMAKER_CLK_CLKDIV5_CANFD2DIV_Pos (8)
#define NUMAKER_CLK_CLKDIV5_CANFD3DIV_Pos (12)
#define NUMAKER_CLK_CLKDIV5_UART8DIV_Pos  (16)
#define NUMAKER_CLK_CLKDIV5_UART9DIV_Pos  (20)
#define NUMAKER_CLK_CLKDIV5_EADC2DIV_Pos  (24)

#define NUMAKER_CLK_AHBCLK1_CANFD0CKEN_Pos (20)
#define NUMAKER_CLK_AHBCLK1_CANFD1CKEN_Pos (21)
#define NUMAKER_CLK_AHBCLK1_CANFD2CKEN_Pos (22)
#define NUMAKER_CLK_AHBCLK1_CANFD3CKEN_Pos (23)
#define NUMAKER_CLK_AHBCLK1_GPICKEN_Pos    (24)
#define NUMAKER_CLK_AHBCLK1_GPJCKEN_Pos    (25)
#define NUMAKER_CLK_AHBCLK1_BMCCKEN_Pos    (28)

#define NUMAKER_CLK_CLKSEL4_SPI4SEL_Pos  (0)
#define NUMAKER_CLK_CLKSEL4_SPI5SEL_Pos  (4)
#define NUMAKER_CLK_CLKSEL4_SPI6SEL_Pos  (8)
#define NUMAKER_CLK_CLKSEL4_SPI7SEL_Pos  (12)
#define NUMAKER_CLK_CLKSEL4_SPI8SEL_Pos  (16)
#define NUMAKER_CLK_CLKSEL4_SPI9SEL_Pos  (20)
#define NUMAKER_CLK_CLKSEL4_SPI10SEL_Pos (24)

/* End of M460 BSP clk_reg.h copy */

/* Beginning of M460 BSP clk.h copy */

/*  CLKSEL0 constant definitions.  (Write-protection) */

#define NUMAKER_CLK_CLKSEL0_HCLKSEL_HXT  (0x0UL << NUMAKER_CLK_CLKSEL0_HCLKSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_HCLKSEL_LXT  (0x1UL << NUMAKER_CLK_CLKSEL0_HCLKSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_HCLKSEL_PLL  (0x2UL << NUMAKER_CLK_CLKSEL0_HCLKSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_HCLKSEL_LIRC (0x3UL << NUMAKER_CLK_CLKSEL0_HCLKSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_HCLKSEL_HIRC (0x7UL << NUMAKER_CLK_CLKSEL0_HCLKSEL_Pos)

#define NUMAKER_CLK_CLKSEL0_STCLKSEL_HXT       (0x0UL << NUMAKER_CLK_CLKSEL0_STCLKSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_STCLKSEL_LXT       (0x1UL << NUMAKER_CLK_CLKSEL0_STCLKSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_STCLKSEL_HXT_DIV2  (0x2UL << NUMAKER_CLK_CLKSEL0_STCLKSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_STCLKSEL_HCLK_DIV2 (0x3UL << NUMAKER_CLK_CLKSEL0_STCLKSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_STCLKSEL_HIRC_DIV2 (0x7UL << NUMAKER_CLK_CLKSEL0_STCLKSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_STCLKSEL_HCLK      (0x1UL << SysTick_CTRL_CLKSOURCE_Pos)

#define NUMAKER_CLK_CLKSEL0_USBSEL_HIRC48M  (0x0UL << NUMAKER_CLK_CLKSEL0_USBSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_USBSEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL0_USBSEL_Pos)

#define NUMAKER_CLK_CLKSEL0_EADC0SEL_PLLFN_DIV2 (0x0UL << NUMAKER_CLK_CLKSEL0_EADC0SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_EADC0SEL_PLL_DIV2   (0x1UL << NUMAKER_CLK_CLKSEL0_EADC0SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_EADC0SEL_HCLK       (0x2UL << NUMAKER_CLK_CLKSEL0_EADC0SEL_Pos)

#define NUMAKER_CLK_CLKSEL0_EADC1SEL_PLLFN_DIV2 (0x0UL << NUMAKER_CLK_CLKSEL0_EADC1SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_EADC1SEL_PLL_DIV2   (0x1UL << NUMAKER_CLK_CLKSEL0_EADC1SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_EADC1SEL_HCLK       (0x2UL << NUMAKER_CLK_CLKSEL0_EADC1SEL_Pos)

#define NUMAKER_CLK_CLKSEL0_EADC2SEL_PLLFN_DIV2 (0x0UL << NUMAKER_CLK_CLKSEL0_EADC2SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_EADC2SEL_PLL_DIV2   (0x1UL << NUMAKER_CLK_CLKSEL0_EADC2SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_EADC2SEL_HCLK       (0x2UL << NUMAKER_CLK_CLKSEL0_EADC2SEL_Pos)

#define NUMAKER_CLK_CLKSEL0_CCAPSEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL0_CCAPSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CCAPSEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL0_CCAPSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CCAPSEL_HCLK     (0x2UL << NUMAKER_CLK_CLKSEL0_CCAPSEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CCAPSEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL0_CCAPSEL_Pos)

#define NUMAKER_CLK_CLKSEL0_SDH0SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL0_SDH0SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_SDH0SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL0_SDH0SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_SDH0SEL_HCLK     (0x2UL << NUMAKER_CLK_CLKSEL0_SDH0SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_SDH0SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL0_SDH0SEL_Pos)

#define NUMAKER_CLK_CLKSEL0_SDH1SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL0_SDH1SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_SDH1SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL0_SDH1SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_SDH1SEL_HCLK     (0x2UL << NUMAKER_CLK_CLKSEL0_SDH1SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_SDH1SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL0_SDH1SEL_Pos)

#define NUMAKER_CLK_CLKSEL0_CANFD0SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL0_CANFD0SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD0SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL0_CANFD0SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD0SEL_HCLK     (0x2UL << NUMAKER_CLK_CLKSEL0_CANFD0SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD0SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL0_CANFD0SEL_Pos)

#define NUMAKER_CLK_CLKSEL0_CANFD1SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL0_CANFD1SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD1SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL0_CANFD1SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD1SEL_HCLK     (0x2UL << NUMAKER_CLK_CLKSEL0_CANFD1SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD1SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL0_CANFD1SEL_Pos)

#define NUMAKER_CLK_CLKSEL0_CANFD2SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL0_CANFD2SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD2SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL0_CANFD2SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD2SEL_HCLK     (0x2UL << NUMAKER_CLK_CLKSEL0_CANFD2SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD2SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL0_CANFD2SEL_Pos)

#define NUMAKER_CLK_CLKSEL0_CANFD3SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL0_CANFD3SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD3SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL0_CANFD3SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD3SEL_HCLK     (0x2UL << NUMAKER_CLK_CLKSEL0_CANFD3SEL_Pos)
#define NUMAKER_CLK_CLKSEL0_CANFD3SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL0_CANFD3SEL_Pos)

/*  CLKSEL1 constant definitions. */

#define NUMAKER_CLK_CLKSEL1_WDTSEL_LXT          (0x1UL << NUMAKER_CLK_CLKSEL1_WDTSEL_Pos)
#define NUMAKER_CLK_CLKSEL1_WDTSEL_HCLK_DIV2048 (0x2UL << NUMAKER_CLK_CLKSEL1_WDTSEL_Pos)
#define NUMAKER_CLK_CLKSEL1_WDTSEL_LIRC         (0x3UL << NUMAKER_CLK_CLKSEL1_WDTSEL_Pos)

#define NUMAKER_CLK_CLKSEL1_CLKOSEL_HXT        (0x0UL << NUMAKER_CLK_CLKSEL1_CLKOSEL_Pos)
#define NUMAKER_CLK_CLKSEL1_CLKOSEL_LXT        (0x1UL << NUMAKER_CLK_CLKSEL1_CLKOSEL_Pos)
#define NUMAKER_CLK_CLKSEL1_CLKOSEL_HCLK       (0x2UL << NUMAKER_CLK_CLKSEL1_CLKOSEL_Pos)
#define NUMAKER_CLK_CLKSEL1_CLKOSEL_HIRC       (0x3UL << NUMAKER_CLK_CLKSEL1_CLKOSEL_Pos)
#define NUMAKER_CLK_CLKSEL1_CLKOSEL_LIRC       (0x4UL << NUMAKER_CLK_CLKSEL1_CLKOSEL_Pos)
#define NUMAKER_CLK_CLKSEL1_CLKOSEL_PLLFN_DIV2 (0x5UL << NUMAKER_CLK_CLKSEL1_CLKOSEL_Pos)
#define NUMAKER_CLK_CLKSEL1_CLKOSEL_PLL_DIV2   (0x6UL << NUMAKER_CLK_CLKSEL1_CLKOSEL_Pos)

#define NUMAKER_CLK_CLKSEL1_TMR0SEL_HXT   (0x0UL << NUMAKER_CLK_CLKSEL1_TMR0SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR0SEL_LXT   (0x1UL << NUMAKER_CLK_CLKSEL1_TMR0SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR0SEL_PCLK0 (0x2UL << NUMAKER_CLK_CLKSEL1_TMR0SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR0SEL_EXT   (0x3UL << NUMAKER_CLK_CLKSEL1_TMR0SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR0SEL_LIRC  (0x5UL << NUMAKER_CLK_CLKSEL1_TMR0SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR0SEL_HIRC  (0x7UL << NUMAKER_CLK_CLKSEL1_TMR0SEL_Pos)

#define NUMAKER_CLK_CLKSEL1_TMR1SEL_HXT   (0x0UL << NUMAKER_CLK_CLKSEL1_TMR1SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR1SEL_LXT   (0x1UL << NUMAKER_CLK_CLKSEL1_TMR1SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR1SEL_PCLK0 (0x2UL << NUMAKER_CLK_CLKSEL1_TMR1SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR1SEL_EXT   (0x3UL << NUMAKER_CLK_CLKSEL1_TMR1SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR1SEL_LIRC  (0x5UL << NUMAKER_CLK_CLKSEL1_TMR1SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR1SEL_HIRC  (0x7UL << NUMAKER_CLK_CLKSEL1_TMR1SEL_Pos)

#define NUMAKER_CLK_CLKSEL1_TMR2SEL_HXT   (0x0UL << NUMAKER_CLK_CLKSEL1_TMR2SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR2SEL_LXT   (0x1UL << NUMAKER_CLK_CLKSEL1_TMR2SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR2SEL_PCLK1 (0x2UL << NUMAKER_CLK_CLKSEL1_TMR2SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR2SEL_EXT   (0x3UL << NUMAKER_CLK_CLKSEL1_TMR2SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR2SEL_LIRC  (0x5UL << NUMAKER_CLK_CLKSEL1_TMR2SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR2SEL_HIRC  (0x7UL << NUMAKER_CLK_CLKSEL1_TMR2SEL_Pos)

#define NUMAKER_CLK_CLKSEL1_TMR3SEL_HXT   (0x0UL << NUMAKER_CLK_CLKSEL1_TMR3SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR3SEL_LXT   (0x1UL << NUMAKER_CLK_CLKSEL1_TMR3SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR3SEL_PCLK1 (0x2UL << NUMAKER_CLK_CLKSEL1_TMR3SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR3SEL_EXT   (0x3UL << NUMAKER_CLK_CLKSEL1_TMR3SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR3SEL_LIRC  (0x5UL << NUMAKER_CLK_CLKSEL1_TMR3SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_TMR3SEL_HIRC  (0x7UL << NUMAKER_CLK_CLKSEL1_TMR3SEL_Pos)

#define NUMAKER_CLK_CLKSEL1_UART0SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL1_UART0SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_UART0SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL1_UART0SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_UART0SEL_LXT      (0x2UL << NUMAKER_CLK_CLKSEL1_UART0SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_UART0SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL1_UART0SEL_Pos)

#define NUMAKER_CLK_CLKSEL1_UART1SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL1_UART1SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_UART1SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL1_UART1SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_UART1SEL_LXT      (0x2UL << NUMAKER_CLK_CLKSEL1_UART1SEL_Pos)
#define NUMAKER_CLK_CLKSEL1_UART1SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL1_UART1SEL_Pos)

#define NUMAKER_CLK_CLKSEL1_WWDTSEL_HCLK_DIV2048 (0x2UL << NUMAKER_CLK_CLKSEL1_WWDTSEL_Pos)
#define NUMAKER_CLK_CLKSEL1_WWDTSEL_LIRC         (0x3UL << NUMAKER_CLK_CLKSEL1_WWDTSEL_Pos)

/*  CLKSEL2 constant definitions. */

#define NUMAKER_CLK_CLKSEL2_EPWM0SEL_HCLK  (0x0UL << NUMAKER_CLK_CLKSEL2_EPWM0SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_EPWM0SEL_PCLK0 (0x1UL << NUMAKER_CLK_CLKSEL2_EPWM0SEL_Pos)

#define NUMAKER_CLK_CLKSEL2_EPWM1SEL_HCLK  (0x0UL << NUMAKER_CLK_CLKSEL2_EPWM1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_EPWM1SEL_PCLK1 (0x1UL << NUMAKER_CLK_CLKSEL2_EPWM1SEL_Pos)

#define NUMAKER_CLK_CLKSEL2_QSPI0SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL2_QSPI0SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_QSPI0SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL2_QSPI0SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_QSPI0SEL_PCLK0    (0x2UL << NUMAKER_CLK_CLKSEL2_QSPI0SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_QSPI0SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL2_QSPI0SEL_Pos)

#define NUMAKER_CLK_CLKSEL2_SPI0SEL_HXT        (0x0UL << NUMAKER_CLK_CLKSEL2_SPI0SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_SPI0SEL_PLL_DIV2   (0x1UL << NUMAKER_CLK_CLKSEL2_SPI0SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_SPI0SEL_PCLK1      (0x2UL << NUMAKER_CLK_CLKSEL2_SPI0SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_SPI0SEL_HIRC       (0x3UL << NUMAKER_CLK_CLKSEL2_SPI0SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_SPI0SEL_HIRC48M    (0x4UL << NUMAKER_CLK_CLKSEL2_SPI0SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_SPI0SEL_PLLFN_DIV2 (0x5UL << NUMAKER_CLK_CLKSEL2_SPI0SEL_Pos)

#define NUMAKER_CLK_CLKSEL2_BPWM0SEL_HCLK  (0x0UL << NUMAKER_CLK_CLKSEL2_BPWM0SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_BPWM0SEL_PCLK0 (0x1UL << NUMAKER_CLK_CLKSEL2_BPWM0SEL_Pos)

#define NUMAKER_CLK_CLKSEL2_BPWM1SEL_HCLK  (0x0UL << NUMAKER_CLK_CLKSEL2_BPWM1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_BPWM1SEL_PCLK1 (0x1UL << NUMAKER_CLK_CLKSEL2_BPWM1SEL_Pos)

#define NUMAKER_CLK_CLKSEL2_QSPI1SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL2_QSPI1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_QSPI1SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL2_QSPI1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_QSPI1SEL_PCLK1    (0x2UL << NUMAKER_CLK_CLKSEL2_QSPI1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_QSPI1SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL2_QSPI1SEL_Pos)

#define NUMAKER_CLK_CLKSEL2_SPI1SEL_HXT        (0x0UL << NUMAKER_CLK_CLKSEL2_SPI1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_SPI1SEL_PLL_DIV2   (0x1UL << NUMAKER_CLK_CLKSEL2_SPI1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_SPI1SEL_PCLK0      (0x2UL << NUMAKER_CLK_CLKSEL2_SPI1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_SPI1SEL_HIRC       (0x3UL << NUMAKER_CLK_CLKSEL2_SPI1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_SPI1SEL_HIRC48M    (0x4UL << NUMAKER_CLK_CLKSEL2_SPI1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_SPI1SEL_PLLFN_DIV2 (0x5UL << NUMAKER_CLK_CLKSEL2_SPI1SEL_Pos)

#define NUMAKER_CLK_CLKSEL2_I2S1SEL_HXT        (0x0UL << NUMAKER_CLK_CLKSEL2_I2S1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_I2S1SEL_PLL_DIV2   (0x1UL << NUMAKER_CLK_CLKSEL2_I2S1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_I2S1SEL_PCLK1      (0x2UL << NUMAKER_CLK_CLKSEL2_I2S1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_I2S1SEL_HIRC       (0x3UL << NUMAKER_CLK_CLKSEL2_I2S1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_I2S1SEL_HIRC48M    (0x4UL << NUMAKER_CLK_CLKSEL2_I2S1SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_I2S1SEL_PLLFN_DIV2 (0x5UL << NUMAKER_CLK_CLKSEL2_I2S1SEL_Pos)

#define NUMAKER_CLK_CLKSEL2_UART8SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL2_UART8SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_UART8SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL2_UART8SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_UART8SEL_LXT      (0x2UL << NUMAKER_CLK_CLKSEL2_UART8SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_UART8SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL2_UART8SEL_Pos)

#define NUMAKER_CLK_CLKSEL2_UART9SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL2_UART9SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_UART9SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL2_UART9SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_UART9SEL_LXT      (0x2UL << NUMAKER_CLK_CLKSEL2_UART9SEL_Pos)
#define NUMAKER_CLK_CLKSEL2_UART9SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL2_UART9SEL_Pos)

#define NUMAKER_CLK_CLKSEL2_TRNGSEL_LXT  (0x0UL << NUMAKER_CLK_CLKSEL2_TRNGSEL_Pos)
#define NUMAKER_CLK_CLKSEL2_TRNGSEL_LIRC (0x1UL << NUMAKER_CLK_CLKSEL2_TRNGSEL_Pos)

#define NUMAKER_CLK_CLKSEL2_PSIOSEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL2_PSIOSEL_Pos)
#define NUMAKER_CLK_CLKSEL2_PSIOSEL_LXT      (0x1UL << NUMAKER_CLK_CLKSEL2_PSIOSEL_Pos)
#define NUMAKER_CLK_CLKSEL2_PSIOSEL_PCLK1    (0x2UL << NUMAKER_CLK_CLKSEL2_PSIOSEL_Pos)
#define NUMAKER_CLK_CLKSEL2_PSIOSEL_PLL_DIV2 (0x3UL << NUMAKER_CLK_CLKSEL2_PSIOSEL_Pos)
#define NUMAKER_CLK_CLKSEL2_PSIOSEL_LIRC     (0x4UL << NUMAKER_CLK_CLKSEL2_PSIOSEL_Pos)
#define NUMAKER_CLK_CLKSEL2_PSIOSEL_HIRC     (0x5UL << NUMAKER_CLK_CLKSEL2_PSIOSEL_Pos)

/*  CLKSEL3 constant definitions. */

#define NUMAKER_CLK_CLKSEL3_SC0SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL3_SC0SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SC0SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL3_SC0SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SC0SEL_PCLK0    (0x2UL << NUMAKER_CLK_CLKSEL3_SC0SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SC0SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL3_SC0SEL_Pos)

#define NUMAKER_CLK_CLKSEL3_SC1SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL3_SC1SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SC1SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL3_SC1SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SC1SEL_PCLK1    (0x2UL << NUMAKER_CLK_CLKSEL3_SC1SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SC1SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL3_SC1SEL_Pos)

#define NUMAKER_CLK_CLKSEL3_SC2SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL3_SC2SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SC2SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL3_SC2SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SC2SEL_PCLK0    (0x2UL << NUMAKER_CLK_CLKSEL3_SC2SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SC2SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL3_SC2SEL_Pos)

#define NUMAKER_CLK_CLKSEL3_KPISEL_HXT  (0x0UL << NUMAKER_CLK_CLKSEL3_KPISEL_Pos)
#define NUMAKER_CLK_CLKSEL3_KPISEL_LIRC (0x1UL << NUMAKER_CLK_CLKSEL3_KPISEL_Pos)
#define NUMAKER_CLK_CLKSEL3_KPISEL_HIRC (0x2UL << NUMAKER_CLK_CLKSEL3_KPISEL_Pos)

#define NUMAKER_CLK_CLKSEL3_SPI2SEL_HXT        (0x0UL << NUMAKER_CLK_CLKSEL3_SPI2SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SPI2SEL_PLL_DIV2   (0x1UL << NUMAKER_CLK_CLKSEL3_SPI2SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SPI2SEL_PCLK1      (0x2UL << NUMAKER_CLK_CLKSEL3_SPI2SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SPI2SEL_HIRC       (0x3UL << NUMAKER_CLK_CLKSEL3_SPI2SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SPI2SEL_HIRC48M    (0x4UL << NUMAKER_CLK_CLKSEL3_SPI2SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SPI2SEL_PLLFN_DIV2 (0x5UL << NUMAKER_CLK_CLKSEL3_SPI2SEL_Pos)

#define NUMAKER_CLK_CLKSEL3_SPI3SEL_HXT        (0x0UL << NUMAKER_CLK_CLKSEL3_SPI3SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SPI3SEL_PLL_DIV2   (0x1UL << NUMAKER_CLK_CLKSEL3_SPI3SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SPI3SEL_PCLK0      (0x2UL << NUMAKER_CLK_CLKSEL3_SPI3SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SPI3SEL_HIRC       (0x3UL << NUMAKER_CLK_CLKSEL3_SPI3SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SPI3SEL_HIRC48M    (0x4UL << NUMAKER_CLK_CLKSEL3_SPI3SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_SPI3SEL_PLLFN_DIV2 (0x5UL << NUMAKER_CLK_CLKSEL3_SPI3SEL_Pos)

#define NUMAKER_CLK_CLKSEL3_I2S0SEL_HXT        (0x0UL << NUMAKER_CLK_CLKSEL3_I2S0SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_I2S0SEL_PLL_DIV2   (0x1UL << NUMAKER_CLK_CLKSEL3_I2S0SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_I2S0SEL_PCLK0      (0x2UL << NUMAKER_CLK_CLKSEL3_I2S0SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_I2S0SEL_HIRC       (0x3UL << NUMAKER_CLK_CLKSEL3_I2S0SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_I2S0SEL_HIRC48M    (0x4UL << NUMAKER_CLK_CLKSEL3_I2S0SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_I2S0SEL_PLLFN_DIV2 (0x5UL << NUMAKER_CLK_CLKSEL3_I2S0SEL_Pos)

#define NUMAKER_CLK_CLKSEL3_UART6SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL3_UART6SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART6SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL3_UART6SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART6SEL_LXT      (0x2UL << NUMAKER_CLK_CLKSEL3_UART6SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART6SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL3_UART6SEL_Pos)

#define NUMAKER_CLK_CLKSEL3_UART7SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL3_UART7SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART7SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL3_UART7SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART7SEL_LXT      (0x2UL << NUMAKER_CLK_CLKSEL3_UART7SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART7SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL3_UART7SEL_Pos)

#define NUMAKER_CLK_CLKSEL3_UART2SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL3_UART2SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART2SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL3_UART2SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART2SEL_LXT      (0x2UL << NUMAKER_CLK_CLKSEL3_UART2SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART2SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL3_UART2SEL_Pos)

#define NUMAKER_CLK_CLKSEL3_UART3SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL3_UART3SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART3SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL3_UART3SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART3SEL_LXT      (0x2UL << NUMAKER_CLK_CLKSEL3_UART3SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART3SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL3_UART3SEL_Pos)

#define NUMAKER_CLK_CLKSEL3_UART4SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL3_UART4SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART4SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL3_UART4SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART4SEL_LXT      (0x2UL << NUMAKER_CLK_CLKSEL3_UART4SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART4SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL3_UART4SEL_Pos)

#define NUMAKER_CLK_CLKSEL3_UART5SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL3_UART5SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART5SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL3_UART5SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART5SEL_LXT      (0x2UL << NUMAKER_CLK_CLKSEL3_UART5SEL_Pos)
#define NUMAKER_CLK_CLKSEL3_UART5SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL3_UART5SEL_Pos)

/*  CLKSEL4 constant definitions. */

#define NUMAKER_CLK_CLKSEL4_SPI4SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL4_SPI4SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI4SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL4_SPI4SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI4SEL_PCLK1    (0x2UL << NUMAKER_CLK_CLKSEL4_SPI4SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI4SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL4_SPI4SEL_Pos)

#define NUMAKER_CLK_CLKSEL4_SPI5SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL4_SPI5SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI5SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL4_SPI5SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI5SEL_PCLK0    (0x2UL << NUMAKER_CLK_CLKSEL4_SPI5SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI5SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL4_SPI5SEL_Pos)

#define NUMAKER_CLK_CLKSEL4_SPI6SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL4_SPI6SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI6SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL4_SPI6SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI6SEL_PCLK1    (0x2UL << NUMAKER_CLK_CLKSEL4_SPI6SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI6SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL4_SPI6SEL_Pos)

#define NUMAKER_CLK_CLKSEL4_SPI7SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL4_SPI7SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI7SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL4_SPI7SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI7SEL_PCLK0    (0x2UL << NUMAKER_CLK_CLKSEL4_SPI7SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI7SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL4_SPI7SEL_Pos)

#define NUMAKER_CLK_CLKSEL4_SPI8SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL4_SPI8SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI8SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL4_SPI8SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI8SEL_PCLK1    (0x2UL << NUMAKER_CLK_CLKSEL4_SPI8SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI8SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL4_SPI8SEL_Pos)

#define NUMAKER_CLK_CLKSEL4_SPI9SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL4_SPI9SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI9SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL4_SPI9SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI9SEL_PCLK0    (0x2UL << NUMAKER_CLK_CLKSEL4_SPI9SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI9SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL4_SPI9SEL_Pos)

#define NUMAKER_CLK_CLKSEL4_SPI10SEL_HXT      (0x0UL << NUMAKER_CLK_CLKSEL4_SPI10SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI10SEL_PLL_DIV2 (0x1UL << NUMAKER_CLK_CLKSEL4_SPI10SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI10SEL_PCLK1    (0x2UL << NUMAKER_CLK_CLKSEL4_SPI10SEL_Pos)
#define NUMAKER_CLK_CLKSEL4_SPI10SEL_HIRC     (0x3UL << NUMAKER_CLK_CLKSEL4_SPI10SEL_Pos)

/*  CLKDIV0 constant definitions. */

#define NUMAKER_CLK_CLKDIV0_HCLK(x)  (((x)-1UL) << NUMAKER_CLK_CLKDIV0_HCLKDIV_Pos)
#define NUMAKER_CLK_CLKDIV0_USB(x)   (((x)-1UL) << NUMAKER_CLK_CLKDIV0_USBDIV_Pos)
#define NUMAKER_CLK_CLKDIV0_SDH0(x)  (((x)-1UL) << NUMAKER_CLK_CLKDIV0_SDH0DIV_Pos)
#define NUMAKER_CLK_CLKDIV0_UART0(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV0_UART0DIV_Pos)
#define NUMAKER_CLK_CLKDIV0_UART1(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV0_UART1DIV_Pos)
#define NUMAKER_CLK_CLKDIV0_EADC0(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV0_EADC0DIV_Pos)

/*  CLKDIV1 constant definitions. */

#define NUMAKER_CLK_CLKDIV1_SC0(x)  (((x)-1UL) << NUMAKER_CLK_CLKDIV1_SC0DIV_Pos)
#define NUMAKER_CLK_CLKDIV1_SC1(x)  (((x)-1UL) << NUMAKER_CLK_CLKDIV1_SC1DIV_Pos)
#define NUMAKER_CLK_CLKDIV1_SC2(x)  (((x)-1UL) << NUMAKER_CLK_CLKDIV1_SC2DIV_Pos)
#define NUMAKER_CLK_CLKDIV1_PSIO(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV1_PSIODIV_Pos)

/*  CLKDIV2 constant definitions. */

#define NUMAKER_CLK_CLKDIV2_I2S0(x)  (((x)-1UL) << NUMAKER_CLK_CLKDIV2_I2S0DIV_Pos)
#define NUMAKER_CLK_CLKDIV2_I2S1(x)  (((x)-1UL) << NUMAKER_CLK_CLKDIV2_I2S1DIV_Pos)
#define NUMAKER_CLK_CLKDIV2_KPI(x)   (((x)-1UL) << NUMAKER_CLK_CLKDIV2_KPIDIV_Pos)
#define NUMAKER_CLK_CLKDIV2_EADC1(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV2_EADC1DIV_Pos)

/*  CLKDIV3 constant definitions. */

#define NUMAKER_CLK_CLKDIV3_VSENSE(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV3_VSENSEDIV_Pos)
#define NUMAKER_CLK_CLKDIV3_EMAC0(x)  (((x)-1UL) << NUMAKER_CLK_CLKDIV3_EMAC0DIV_Pos)
#define NUMAKER_CLK_CLKDIV3_SDH1(x)   (((x)-1UL) << NUMAKER_CLK_CLKDIV3_SDH1DIV_Pos)

/*  CLKDIV4 constant definitions. */

#define NUMAKER_CLK_CLKDIV4_UART2(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV4_UART2DIV_Pos)
#define NUMAKER_CLK_CLKDIV4_UART3(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV4_UART3DIV_Pos)
#define NUMAKER_CLK_CLKDIV4_UART4(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV4_UART4DIV_Pos)
#define NUMAKER_CLK_CLKDIV4_UART5(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV4_UART5DIV_Pos)
#define NUMAKER_CLK_CLKDIV4_UART6(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV4_UART6DIV_Pos)
#define NUMAKER_CLK_CLKDIV4_UART7(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV4_UART7DIV_Pos)

/*  CLKDIV5 constant definitions. */

#define NUMAKER_CLK_CLKDIV5_CANFD0(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV5_CANFD0DIV_Pos)
#define NUMAKER_CLK_CLKDIV5_CANFD1(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV5_CANFD1DIV_Pos)
#define NUMAKER_CLK_CLKDIV5_CANFD2(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV5_CANFD2DIV_Pos)
#define NUMAKER_CLK_CLKDIV5_CANFD3(x) (((x)-1UL) << NUMAKER_CLK_CLKDIV5_CANFD3DIV_Pos)
#define NUMAKER_CLK_CLKDIV5_UART8(x)  (((x)-1UL) << NUMAKER_CLK_CLKDIV5_UART8DIV_Pos)
#define NUMAKER_CLK_CLKDIV5_UART9(x)  (((x)-1UL) << NUMAKER_CLK_CLKDIV5_UART9DIV_Pos)
#define NUMAKER_CLK_CLKDIV5_EADC2(x)  (((x)-1UL) << NUMAKER_CLK_CLKDIV5_EADC2DIV_Pos)

/*  PCLKDIV constant definitions. */

#define NUMAKER_CLK_PCLKDIV_PCLK0DIV1  (0x0UL << NUMAKER_CLK_PCLKDIV_APB0DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_PCLK0DIV2  (0x1UL << NUMAKER_CLK_PCLKDIV_APB0DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_PCLK0DIV4  (0x2UL << NUMAKER_CLK_PCLKDIV_APB0DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_PCLK0DIV8  (0x3UL << NUMAKER_CLK_PCLKDIV_APB0DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_PCLK0DIV16 (0x4UL << NUMAKER_CLK_PCLKDIV_APB0DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_PCLK1DIV1  (0x0UL << NUMAKER_CLK_PCLKDIV_APB1DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_PCLK1DIV2  (0x1UL << NUMAKER_CLK_PCLKDIV_APB1DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_PCLK1DIV4  (0x2UL << NUMAKER_CLK_PCLKDIV_APB1DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_PCLK1DIV8  (0x3UL << NUMAKER_CLK_PCLKDIV_APB1DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_PCLK1DIV16 (0x4UL << NUMAKER_CLK_PCLKDIV_APB1DIV_Pos)

#define NUMAKER_CLK_PCLKDIV_APB0DIV_DIV1  (0x0UL << NUMAKER_CLK_PCLKDIV_APB0DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_APB0DIV_DIV2  (0x1UL << NUMAKER_CLK_PCLKDIV_APB0DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_APB0DIV_DIV4  (0x2UL << NUMAKER_CLK_PCLKDIV_APB0DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_APB0DIV_DIV8  (0x3UL << NUMAKER_CLK_PCLKDIV_APB0DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_APB0DIV_DIV16 (0x4UL << NUMAKER_CLK_PCLKDIV_APB0DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_APB1DIV_DIV1  (0x0UL << NUMAKER_CLK_PCLKDIV_APB1DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_APB1DIV_DIV2  (0x1UL << NUMAKER_CLK_PCLKDIV_APB1DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_APB1DIV_DIV4  (0x2UL << NUMAKER_CLK_PCLKDIV_APB1DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_APB1DIV_DIV8  (0x3UL << NUMAKER_CLK_PCLKDIV_APB1DIV_Pos)
#define NUMAKER_CLK_PCLKDIV_APB1DIV_DIV16 (0x4UL << NUMAKER_CLK_PCLKDIV_APB1DIV_Pos)

/*  MODULE constant definitions. */

/*
 * APBCLK(31:29)|CLKSEL(28:26)|CLKSEL_Msk(25:22)|CLKSEL_Pos(21:17)|CLKDIV(16:14)|
 * CLKDIV_Msk(13:10)|CLKDIV_Pos(9:5)|IP_EN_Pos(4:0)
 */

#define NUMAKER_MODULE_NoMsk 0x0UL
#define NUMAKER_NA           NUMAKER_MODULE_NoMsk

#define NUMAKER_MODULE_APBCLK_ENC(x)     (((x)&0x07UL) << 29)
#define NUMAKER_MODULE_CLKSEL_ENC(x)     (((x)&0x07UL) << 26)
#define NUMAKER_MODULE_CLKSEL_Msk_ENC(x) (((x)&0x0fUL) << 22)
#define NUMAKER_MODULE_CLKSEL_Pos_ENC(x) (((x)&0x1fUL) << 17)
#define NUMAKER_MODULE_CLKDIV_ENC(x)     (((x)&0x07UL) << 14)
#define NUMAKER_MODULE_CLKDIV_Msk_ENC(x) (((x)&0x0fUL) << 10)
#define NUMAKER_MODULE_CLKDIV_Pos_ENC(x) (((x)&0x1fUL) << 5)
#define NUMAKER_MODULE_IP_EN_Pos_ENC(x)  (((x)&0x1fUL) << 0)

/* AHBCLK0 */
#define NUMAKER_PDMA0_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_PDMA0CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_ISP_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_ISPCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_EBI_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_EBICKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_ST_MODULE                                                                          \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_STCKEN_Pos) |                            \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_EMAC0_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_EMAC0CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SDH0_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_SDH0CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(20UL) | NUMAKER_MODULE_CLKDIV_ENC(0UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(24UL))

#define NUMAKER_CRC_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_CRCCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_CCAP_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_CCAPCKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SEN_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_SENCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(16UL) | NUMAKER_MODULE_CLKDIV_ENC(3UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(8UL))

#define NUMAKER_HSUSBD_MODULE                                                                      \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_HSUSBDCKEN_Pos) |                        \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_HBI_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_HBICKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_CRPT_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_CRPTCKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_KS_MODULE                                                                          \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_KSCKEN_Pos) |                            \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPIM_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_SPIMCKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_FMCIDLE_MODULE                                                                     \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_FMCIDLE_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_USBH_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_USBHCKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(1UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(8UL) | NUMAKER_MODULE_CLKDIV_ENC(0UL) |                     \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0xFUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(4UL))

#define NUMAKER_SDH1_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_SDH1CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(22UL) | NUMAKER_MODULE_CLKDIV_ENC(3UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(24UL))

#define NUMAKER_PDMA1_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_PDMA1CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_TRACE_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_TRACECKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_GPA_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_GPACKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_GPB_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_GPBCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_GPC_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_GPCCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_GPD_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_GPDCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_GPE_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_GPECKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_GPF_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_GPFCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_GPG_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_GPGCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_GPH_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(0UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK0_GPHCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

/* AHBCLK1 */
#define NUMAKER_CANFD0_MODULE                                                                      \
        (NUMAKER_MODULE_APBCLK_ENC(4UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK1_CANFD0CKEN_Pos) |                        \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(24UL) | NUMAKER_MODULE_CLKDIV_ENC(5UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(0UL))

#define NUMAKER_CANFD1_MODULE                                                                      \
        (NUMAKER_MODULE_APBCLK_ENC(4UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK1_CANFD1CKEN_Pos) |                        \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(26UL) | NUMAKER_MODULE_CLKDIV_ENC(5UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(4UL))

#define NUMAKER_CANFD2_MODULE                                                                      \
        (NUMAKER_MODULE_APBCLK_ENC(4UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK1_CANFD2CKEN_Pos) |                        \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(28UL) | NUMAKER_MODULE_CLKDIV_ENC(5UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(8UL))

#define NUMAKER_CANFD3_MODULE                                                                      \
        (NUMAKER_MODULE_APBCLK_ENC(4UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK1_CANFD3CKEN_Pos) |                        \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(30UL) | NUMAKER_MODULE_CLKDIV_ENC(5UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(12UL))

#define NUMAKER_GPI_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(4UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK1_GPICKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_GPJ_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(4UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK1_GPJCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_BMC_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(4UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_AHBCLK1_BMCCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

/* APBCLK0 */
#define NUMAKER_WDT_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_WDTCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(1UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(0UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_WWDT_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_WDTCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(1UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(30UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_RTC_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_RTCCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_TMR0_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_TMR0CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(1UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(8UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_TMR1_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_TMR1CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(1UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(12UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_TMR2_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_TMR2CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(1UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(16UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_TMR3_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_TMR3CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(1UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(20UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_CLKO_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_CLKOCKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(1UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(4UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_ACMP01_MODULE                                                                      \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_ACMP01CKEN_Pos) |                        \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_I2C0_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_I2C0CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_I2C1_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_I2C1CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_I2C2_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_I2C2CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_I2C3_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_I2C3CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_QSPI0_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_QSPI0CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(2UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPI0_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_SPI0CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(4UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPI1_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_SPI1CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(12UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPI2_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_SPI2CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(9UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_UART0_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_UART0CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(1UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(24UL) | NUMAKER_MODULE_CLKDIV_ENC(0UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(8UL))

#define NUMAKER_UART1_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_UART1CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(1UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(26UL) | NUMAKER_MODULE_CLKDIV_ENC(0UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(12UL))

#define NUMAKER_UART2_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_UART2CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(24UL) | NUMAKER_MODULE_CLKDIV_ENC(4UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(0UL))

#define NUMAKER_UART3_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_UART3CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(26UL) | NUMAKER_MODULE_CLKDIV_ENC(4UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(4UL))

#define NUMAKER_UART4_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_UART4CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(28UL) | NUMAKER_MODULE_CLKDIV_ENC(4UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(8UL))

#define NUMAKER_UART5_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_UART5CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(30UL) | NUMAKER_MODULE_CLKDIV_ENC(4UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(12UL))

#define NUMAKER_UART6_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_UART6CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(20UL) | NUMAKER_MODULE_CLKDIV_ENC(4UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(16UL))

#define NUMAKER_UART7_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_UART7CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(22UL) | NUMAKER_MODULE_CLKDIV_ENC(4UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(20UL))

#define NUMAKER_OTG_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_OTGCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(1UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(8UL) | NUMAKER_MODULE_CLKDIV_ENC(0UL) |                     \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0xFUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(4UL))

#define NUMAKER_USBD_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_USBDCKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(1UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(8UL) | NUMAKER_MODULE_CLKDIV_ENC(0UL) |                     \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0xFUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(4UL))

#define NUMAKER_EADC0_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_EADC0CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(10UL) | NUMAKER_MODULE_CLKDIV_ENC(0UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(16UL))

#define NUMAKER_I2S0_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_I2S0CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(16UL) | NUMAKER_MODULE_CLKDIV_ENC(2UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(0UL))

#define NUMAKER_HSOTG_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(1UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK0_HSOTGCKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

/* APBCLK1 */
#define NUMAKER_SC0_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_SC0CKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(0UL) | NUMAKER_MODULE_CLKDIV_ENC(1UL) |                     \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(0UL))

#define NUMAKER_SC1_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_SC1CKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(2UL) | NUMAKER_MODULE_CLKDIV_ENC(1UL) |                     \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(8UL))

#define NUMAKER_SC2_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_SC2CKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(4UL) | NUMAKER_MODULE_CLKDIV_ENC(1UL) |                     \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(16UL))

#define NUMAKER_I2C4_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_I2C4CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_QSPI1_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_QSPI1CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(10UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPI3_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_SPI3CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(12UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPI4_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_SPI4CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(4UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(0UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_USCI0_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_USCI0CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_PSIO_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_PSIOCKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(28UL) | NUMAKER_MODULE_CLKDIV_ENC(1UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(24UL))

#define NUMAKER_DAC_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_DACCKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_ECAP2_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_ECAP2CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_ECAP3_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_ECAP3CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_EPWM0_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_EPWM0CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(1UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(0UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_EPWM1_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_EPWM1CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(1UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(1UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_BPWM0_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_BPWM0CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(1UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(8UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_BPWM1_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_BPWM1CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(1UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(9UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_EQEI0_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_EQEI0CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_EQEI1_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_EQEI1CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_EQEI2_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_EQEI2CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_EQEI3_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_EQEI3CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_TRNG_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_TRNGCKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(1UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(27UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_ECAP0_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_ECAP0CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_ECAP1_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_ECAP1CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_I2S1_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_I2S1CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(16UL) | NUMAKER_MODULE_CLKDIV_ENC(2UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(4UL))

#define NUMAKER_EADC1_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(2UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK1_EADC1CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(12UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

/* APBCLK2 */
#define NUMAKER_KPI_MODULE                                                                         \
        (NUMAKER_MODULE_APBCLK_ENC(3UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK2_KPICKEN_Pos) |                           \
         NUMAKER_MODULE_CLKSEL_ENC(3UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(6UL) | NUMAKER_MODULE_CLKDIV_ENC(2UL) |                     \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(8UL))

#define NUMAKER_EADC2_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(3UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK2_EADC2CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(0UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(14UL) | NUMAKER_MODULE_CLKDIV_ENC(2UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(24UL))

#define NUMAKER_ACMP23_MODULE                                                                      \
        (NUMAKER_MODULE_APBCLK_ENC(3UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK2_ACMP23CKEN_Pos) |                        \
         NUMAKER_MODULE_CLKSEL_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKSEL_Msk_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |       \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPI5_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(3UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK2_SPI5CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(4UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(4UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPI6_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(3UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK2_SPI6CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(4UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(8UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |              \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPI7_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(3UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK2_SPI7CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(4UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(12UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPI8_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(3UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK2_SPI8CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(4UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(16UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPI9_MODULE                                                                        \
        (NUMAKER_MODULE_APBCLK_ENC(3UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK2_SPI9CKEN_Pos) |                          \
         NUMAKER_MODULE_CLKSEL_ENC(4UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(20UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_SPI10_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(3UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK2_SPI10CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(4UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(7UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(24UL) | NUMAKER_MODULE_CLKDIV_ENC(NUMAKER_NA) |             \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(NUMAKER_NA) | NUMAKER_MODULE_CLKDIV_Pos_ENC(NUMAKER_NA))

#define NUMAKER_UART8_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(3UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK2_UART8CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(20UL) | NUMAKER_MODULE_CLKDIV_ENC(5UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(16UL))

#define NUMAKER_UART9_MODULE                                                                       \
        (NUMAKER_MODULE_APBCLK_ENC(3UL) |                                                          \
         NUMAKER_MODULE_IP_EN_Pos_ENC(NUMAKER_CLK_APBCLK2_UART9CKEN_Pos) |                         \
         NUMAKER_MODULE_CLKSEL_ENC(2UL) | NUMAKER_MODULE_CLKSEL_Msk_ENC(3UL) |                     \
         NUMAKER_MODULE_CLKSEL_Pos_ENC(22UL) | NUMAKER_MODULE_CLKDIV_ENC(5UL) |                    \
         NUMAKER_MODULE_CLKDIV_Msk_ENC(0x0FUL) | NUMAKER_MODULE_CLKDIV_Pos_ENC(20UL))

/* End of M460 BSP clk.h copy */

#define NUMAKER_CLK_PMUCTL_PDMSEL_PD 0x00000000
#define NUMAKER_CLK_PMUCTL_PDMSEL_LLPD 0x00000001
#define NUMAKER_CLK_PMUCTL_PDMSEL_FWPD 0x00000002
#define NUMAKER_CLK_PMUCTL_PDMSEL_SPD 0x00000004
#define NUMAKER_CLK_PMUCTL_PDMSEL_DPD 0x00000006

#endif
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

M460 板级支持包（BSP）`clk_reg.h` 复制内容开始。

### 注释 3：原第 207 行

M460 板级支持包（BSP）`clk_reg.h` 复制内容结束。

### 注释 4：原第 209 行

M460 板级支持包（BSP）`clk.h` 复制内容开始。

### 注释 5：原第 211 行

`CLKSEL0` 常量定义，具有写保护（write-protection）。

### 注释 6：原第 276 行

`CLKSEL1` 常量定义。

### 注释 7：原第 331 行

`CLKSEL2` 常量定义。

### 注释 8：原第 396 行

`CLKSEL3` 常量定义。

### 注释 9：原第 468 行

`CLKSEL4` 常量定义。

### 注释 10：原第 505 行

`CLKDIV0` 常量定义。

### 注释 11：原第 514 行

`CLKDIV1` 常量定义。

### 注释 12：原第 521 行

`CLKDIV2` 常量定义。

### 注释 13：原第 528 行

`CLKDIV3` 常量定义。

### 注释 14：原第 534 行

`CLKDIV4` 常量定义。

### 注释 15：原第 543 行

`CLKDIV5` 常量定义。

### 注释 16：原第 553 行

`PCLKDIV` 常量定义。

### 注释 17：原第 577 行

`MODULE` 常量定义。

### 注释 18：原第 579 行

模块标识的位域布局（bit-field layout）：`APBCLK(31:29) | CLKSEL(28:26) | CLKSEL_Msk(25:22) | CLKSEL_Pos(21:17) | CLKDIV(16:14) | CLKDIV_Msk(13:10) | CLKDIV_Pos(9:5) | IP_EN_Pos(4:0)`。

### 注释 19：原第 596 行

`AHBCLK0` 时钟寄存器组。

### 注释 20：原第 786 行

`AHBCLK1` 时钟寄存器组。

### 注释 21：原第 836 行

`APBCLK0` 时钟寄存器组。

### 注释 22：原第 1047 行

`APBCLK1` 时钟寄存器组。

### 注释 23：原第 1223 行

`APBCLK2` 时钟寄存器组。

### 注释 24：原第 1301 行

M460 板级支持包（BSP）`clk.h` 复制内容结束。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P269_zephyr__dt-bindings__clock__numaker_m46x_clock.h_文件参考.md)

---

[上一章](P006_mdio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_posix_time.h_源码浏览.md)
