---
id: learning.zephyr-docs.api-source-supplement-reference.page-155
title: r8a78000_cpg_mssr.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/r8a78000__cpg__mssr_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第155章\_r8a78000\_cpg\_mssr.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/r8a78000__cpg__mssr_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/r8a78000__cpg__mssr_8h.html)。

## 155.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00014"></a>
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
<a id="l00597"></a>
<a id="l00598"></a>
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
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
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
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
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
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
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
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
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
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
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
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00841"></a>
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
<a id="l00855"></a>
<a id="l00856"></a>
<a id="l00857"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00862"></a>
<a id="l00863"></a>
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
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00888"></a>
<a id="l00889"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00892"></a>
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
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00916"></a>
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
<a id="l00947"></a>
<a id="l00948"></a>
<a id="l00949"></a>
<a id="l00950"></a>
<a id="l00951"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00955"></a>
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
<a id="l00973"></a>
<a id="l00974"></a>
<a id="l00975"></a>
<a id="l00976"></a>
<a id="l00977"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="l00985"></a>
<a id="l00986"></a>
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
<a id="l00998"></a>
<a id="l00999"></a>
<a id="l01000"></a>
<a id="l01001"></a>
<a id="l01002"></a>
<a id="l01003"></a>
<a id="l01004"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="l01009"></a>
<a id="l01010"></a>
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
<a id="l01022"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01032"></a>
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
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01054"></a>
<a id="l01055"></a>
<a id="l01056"></a>
<a id="l01057"></a>
<a id="l01058"></a>
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
<a id="l01094"></a>
<a id="l01095"></a>
<a id="l01096"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01101"></a>
<a id="l01102"></a>
<a id="l01103"></a>
<a id="l01104"></a>
<a id="l01105"></a>
<a id="l01106"></a>
<a id="l01107"></a>
<a id="l01108"></a>
<a id="l01109"></a>
<a id="l01110"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01113"></a>
<a id="l01114"></a>
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
<a id="l01165"></a>
<a id="l01166"></a>
<a id="l01167"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01170"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01173"></a>
<a id="l01174"></a>
<a id="l01175"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01179"></a>
<a id="l01180"></a>
<a id="l01181"></a>
<a id="l01182"></a>
<a id="l01183"></a>
<a id="l01184"></a>
<a id="l01185"></a>
<a id="l01186"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="l01191"></a>
<a id="l01192"></a>
<a id="l01193"></a>
<a id="l01194"></a>
<a id="l01195"></a>
<a id="l01196"></a>
<a id="l01197"></a>
<a id="l01198"></a>
<a id="l01199"></a>
<a id="l01200"></a>
<a id="l01201"></a>
<a id="l01202"></a>
<a id="l01203"></a>
<a id="l01204"></a>
<a id="l01205"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="l01208"></a>
<a id="l01209"></a>
<a id="l01210"></a>
<a id="l01211"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01215"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01221"></a>
<a id="l01222"></a>
<a id="l01223"></a>
<a id="l01224"></a>
<a id="l01225"></a>
<a id="l01226"></a>
<a id="l01227"></a>
<a id="l01228"></a>
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
<a id="l01240"></a>
<a id="l01241"></a>
<a id="l01242"></a>
<a id="l01243"></a>
<a id="l01244"></a>
<a id="l01245"></a>
<a id="l01246"></a>
<a id="l01247"></a>
<a id="l01248"></a>
<a id="l01249"></a>
<a id="l01250"></a>
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
<a id="l01261"></a>
<a id="l01262"></a>
<a id="l01263"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="l01266"></a>
<a id="l01267"></a>
<a id="l01268"></a>
<a id="l01269"></a>
<a id="l01270"></a>
<a id="l01271"></a>
<a id="l01272"></a>
<a id="l01273"></a>
<a id="l01274"></a>
<a id="l01275"></a>
<a id="l01276"></a>
<a id="l01277"></a>
<a id="l01278"></a>
<a id="l01279"></a>
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
<a id="l01304"></a>
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
<a id="l01330"></a>
<a id="l01331"></a>
<a id="l01332"></a>
<a id="l01333"></a>
<a id="l01334"></a>
<a id="l01335"></a>
<a id="l01336"></a>
<a id="l01337"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01340"></a>
<a id="l01341"></a>
<a id="l01342"></a>
<a id="l01343"></a>
<a id="l01344"></a>
<a id="l01345"></a>
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
<a id="l01361"></a>
<a id="l01362"></a>
<a id="l01363"></a>
<a id="l01364"></a>
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
<a id="l01408"></a>
<a id="l01409"></a>
<a id="l01410"></a>
<a id="l01411"></a>
<a id="l01412"></a>
<a id="l01413"></a>
<a id="l01414"></a>
<a id="l01415"></a>
<a id="l01416"></a>
<a id="l01417"></a>
<a id="l01418"></a>
<a id="l01419"></a>
<a id="l01420"></a>
<a id="l01421"></a>
<a id="l01422"></a>
<a id="l01423"></a>
<a id="l01424"></a>
<a id="l01425"></a>
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
<a id="l01437"></a>
<a id="l01438"></a>
<a id="l01439"></a>
<a id="l01440"></a>
<a id="l01441"></a>
<a id="l01442"></a>
<a id="l01443"></a>
<a id="l01444"></a>
<a id="l01445"></a>
<a id="l01446"></a>
<a id="l01447"></a>
<a id="l01448"></a>
<a id="l01449"></a>
<a id="l01450"></a>
<a id="l01451"></a>
<a id="l01452"></a>
<a id="l01453"></a>
<a id="l01454"></a>
<a id="l01455"></a>
<a id="l01456"></a>
<a id="l01457"></a>
<a id="l01458"></a>
<a id="l01459"></a>
<a id="l01460"></a>
<a id="l01461"></a>
<a id="l01462"></a>
<a id="l01463"></a>
<a id="l01464"></a>
<a id="l01465"></a>
<a id="l01466"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01469"></a>
<a id="l01470"></a>
<a id="l01471"></a>
<a id="l01472"></a>
<a id="l01473"></a>
<a id="l01474"></a>
<a id="l01475"></a>
<a id="l01476"></a>
<a id="l01477"></a>
<a id="l01478"></a>
<a id="l01479"></a>
<a id="l01480"></a>
<a id="l01481"></a>
<a id="l01482"></a>
<a id="l01483"></a>
<a id="l01484"></a>
<a id="l01485"></a>
<a id="l01486"></a>
<a id="l01487"></a>
<a id="l01488"></a>
<a id="l01489"></a>
<a id="l01490"></a>
<a id="l01491"></a>
<a id="l01492"></a>
<a id="l01493"></a>
<a id="l01494"></a>
<a id="l01495"></a>
<a id="l01496"></a>
<a id="l01497"></a>
<a id="l01498"></a>
<a id="l01499"></a>
<a id="l01500"></a>
<a id="l01501"></a>
<a id="l01502"></a>
<a id="l01503"></a>
<a id="l01504"></a>
<a id="l01505"></a>
<a id="l01506"></a>
<a id="l01507"></a>
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
<a id="l01522"></a>
<a id="l01523"></a>
<a id="l01524"></a>
<a id="l01525"></a>
<a id="l01526"></a>
<a id="l01527"></a>
<a id="l01528"></a>
<a id="l01529"></a>
<a id="l01530"></a>
<a id="l01531"></a>
<a id="l01532"></a>
<a id="l01533"></a>
<a id="l01534"></a>
<a id="l01535"></a>
<a id="l01536"></a>
<a id="l01537"></a>
<a id="l01538"></a>
<a id="l01539"></a>
<a id="l01540"></a>
<a id="l01541"></a>
<a id="l01542"></a>
<a id="l01543"></a>
<a id="l01544"></a>
<a id="l01545"></a>
<a id="l01546"></a>
<a id="l01547"></a>
<a id="l01548"></a>
<a id="l01549"></a>
<a id="l01550"></a>
<a id="l01551"></a>
<a id="l01552"></a>
<a id="l01553"></a>
<a id="l01554"></a>
<a id="l01555"></a>
<a id="l01556"></a>
<a id="l01557"></a>
<a id="l01558"></a>
<a id="l01559"></a>
<a id="l01560"></a>
<a id="l01561"></a>
<a id="l01562"></a>
<a id="l01563"></a>
<a id="l01564"></a>
<a id="l01565"></a>
<a id="l01566"></a>
<a id="l01567"></a>
<a id="l01568"></a>
<a id="l01569"></a>
<a id="l01570"></a>
<a id="l01571"></a>
<a id="l01572"></a>
<a id="l01573"></a>
<a id="l01574"></a>
<a id="l01575"></a>
<a id="l01576"></a>
<a id="l01577"></a>
<a id="l01578"></a>
<a id="l01579"></a>
<a id="l01580"></a>
<a id="l01581"></a>
<a id="l01582"></a>
<a id="l01583"></a>
<a id="l01584"></a>
<a id="l01585"></a>
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
<a id="l01596"></a>
<a id="l01597"></a>
<a id="l01598"></a>
<a id="l01599"></a>
<a id="l01600"></a>
<a id="l01601"></a>
<a id="l01602"></a>
<a id="l01603"></a>
<a id="l01604"></a>
<a id="l01605"></a>
<a id="l01606"></a>
<a id="l01607"></a>
<a id="l01608"></a>
<a id="l01609"></a>
<a id="l01610"></a>
<a id="l01611"></a>
<a id="l01612"></a>
<a id="l01613"></a>
<a id="l01614"></a>
<a id="l01615"></a>
<a id="l01616"></a>
<a id="l01617"></a>
<a id="l01618"></a>
<a id="l01619"></a>
<a id="l01620"></a>
<a id="l01621"></a>
<a id="l01622"></a>
<a id="l01623"></a>
<a id="l01624"></a>
<a id="l01625"></a>
<a id="l01626"></a>
<a id="l01627"></a>
<a id="l01628"></a>
<a id="l01629"></a>
<a id="l01630"></a>
<a id="l01631"></a>
<a id="l01632"></a>
<a id="l01633"></a>
<a id="l01634"></a>
<a id="l01635"></a>
<a id="l01636"></a>
<a id="l01637"></a>
<a id="l01638"></a>
<a id="l01639"></a>
<a id="l01640"></a>
<a id="l01641"></a>
<a id="l01642"></a>
<a id="l01643"></a>
<a id="l01644"></a>
<a id="l01645"></a>
<a id="l01646"></a>
<a id="l01647"></a>
<a id="l01648"></a>
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
<a id="l01678"></a>
<a id="l01679"></a>
<a id="l01680"></a>
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
<a id="l01707"></a>
<a id="l01708"></a>
<a id="l01709"></a>
<a id="l01710"></a>
<a id="l01711"></a>
<a id="l01712"></a>
<a id="l01713"></a>
<a id="l01714"></a>
<a id="l01715"></a>
<a id="l01717"></a>
<a id="l01718"></a>

```c
/*
 * Copyright (c) 2026 BayLibre, SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A78000_CPG_MSSR_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A78000_CPG_MSSR_H_



/* Clock IDs */
#define R8A78000_CLK_VIPN_FCPCS0        0
#define R8A78000_CLK_VIPN_FCPCS1        1
#define R8A78000_CLK_VIPN_VCP5X0        2
#define R8A78000_CLK_VIPN_VCP5X1        3
#define R8A78000_CLK_VIPN_MSYNC         4
#define R8A78000_CLK_VIPS_FCPCS0        5
#define R8A78000_CLK_VIPS_FCPCS1        6
#define R8A78000_CLK_VIPS_VCP5X0        7
#define R8A78000_CLK_VIPS_VCP5X1        8
#define R8A78000_CLK_VIPS_MSYNC         9
#define R8A78000_CLK_MTI                10
#define R8A78000_CLK_ISP0               11
#define R8A78000_CLK_ISP1               12
#define R8A78000_CLK_ISP2               13
#define R8A78000_CLK_ISP3               14
#define R8A78000_CLK_ISPCS0             15
#define R8A78000_CLK_ISPCS1             16
#define R8A78000_CLK_ISPCS2             17
#define R8A78000_CLK_ISPCS3             18
#define R8A78000_CLK_CSITOP0            19
#define R8A78000_CLK_CSITOP1            20
#define R8A78000_CLK_CSITOP2            21
#define R8A78000_CLK_CSITOP3            22
#define R8A78000_CLK_DPTX0              23
#define R8A78000_CLK_DPTX1              24
#define R8A78000_CLK_DPTX2              25
#define R8A78000_CLK_VSPD0              26
#define R8A78000_CLK_VSPD1              27
#define R8A78000_CLK_VSPD2              28
#define R8A78000_CLK_VSPD3              29
#define R8A78000_CLK_VSPD4              30
#define R8A78000_CLK_VSPDB0             31
#define R8A78000_CLK_VSPDB1             32
#define R8A78000_CLK_VSPDB2             33
#define R8A78000_CLK_VSPDB3             34
#define R8A78000_CLK_VSPDB4             35
#define R8A78000_CLK_VSPX0              36
#define R8A78000_CLK_VSPX1              37
#define R8A78000_CLK_VSPX2              38
#define R8A78000_CLK_VSPX3              39
#define R8A78000_CLK_FCPVD0             40
#define R8A78000_CLK_FCPVD1             41
#define R8A78000_CLK_FCPVD2             42
#define R8A78000_CLK_FCPVD3             43
#define R8A78000_CLK_FCPVD4             44
#define R8A78000_CLK_FCPVD5             45
#define R8A78000_CLK_FCPVD6             46
#define R8A78000_CLK_FCPVD7             47
#define R8A78000_CLK_FCPVD8             48
#define R8A78000_CLK_FCPVD9             49
#define R8A78000_CLK_DOC2CH1            50
#define R8A78000_CLK_DOC2CH2            51
#define R8A78000_CLK_FCPVX0             52
#define R8A78000_CLK_FCPVX1             53
#define R8A78000_CLK_FCPVX2             54
#define R8A78000_CLK_FCPVX3             55
#define R8A78000_CLK_VIN000             56
#define R8A78000_CLK_VIN001             57
#define R8A78000_CLK_VIN002             58
#define R8A78000_CLK_VIN003             59
#define R8A78000_CLK_VIN004             60
#define R8A78000_CLK_VIN005             61
#define R8A78000_CLK_VIN006             62
#define R8A78000_CLK_VIN007             63
#define R8A78000_CLK_VIN010             64
#define R8A78000_CLK_VIN011             65
#define R8A78000_CLK_VIN012             66
#define R8A78000_CLK_VIN013             67
#define R8A78000_CLK_VIN014             68
#define R8A78000_CLK_VIN015             69
#define R8A78000_CLK_VIN016             70
#define R8A78000_CLK_VIN017             71
#define R8A78000_CLK_VIN020             72
#define R8A78000_CLK_VIN021             73
#define R8A78000_CLK_VIN022             74
#define R8A78000_CLK_VIN023             75
#define R8A78000_CLK_VIN024             76
#define R8A78000_CLK_VIN025             77
#define R8A78000_CLK_VIN026             78
#define R8A78000_CLK_VIN027             79
#define R8A78000_CLK_VIN030             80
#define R8A78000_CLK_VIN031             81
#define R8A78000_CLK_VIN032             82
#define R8A78000_CLK_VIN033             83
#define R8A78000_CLK_VIN034             84
#define R8A78000_CLK_VIN035             85
#define R8A78000_CLK_VIN036             86
#define R8A78000_CLK_VIN037             87
#define R8A78000_CLK_VIN040             88
#define R8A78000_CLK_VIN041             89
#define R8A78000_CLK_VIN042             90
#define R8A78000_CLK_VIN043             91
#define R8A78000_CLK_VIN044             92
#define R8A78000_CLK_VIN045             93
#define R8A78000_CLK_VIN046             94
#define R8A78000_CLK_VIN047             95
#define R8A78000_CLK_VIN050             96
#define R8A78000_CLK_VIN051             97
#define R8A78000_CLK_VIN052             98
#define R8A78000_CLK_VIN053             99
#define R8A78000_CLK_VIN054             100
#define R8A78000_CLK_VIN055             101
#define R8A78000_CLK_VIN056             102
#define R8A78000_CLK_VIN057             103
#define R8A78000_CLK_VIN060             104
#define R8A78000_CLK_VIN061             105
#define R8A78000_CLK_VIN062             106
#define R8A78000_CLK_VIN063             107
#define R8A78000_CLK_VIN064             108
#define R8A78000_CLK_VIN065             109
#define R8A78000_CLK_VIN066             110
#define R8A78000_CLK_VIN067             111
#define R8A78000_CLK_VIN070             112
#define R8A78000_CLK_VIN071             113
#define R8A78000_CLK_VIN072             114
#define R8A78000_CLK_VIN073             115
#define R8A78000_CLK_VIN074             116
#define R8A78000_CLK_VIN075             117
#define R8A78000_CLK_VIN076             118
#define R8A78000_CLK_VIN077             119
#define R8A78000_CLK_VIN080             120
#define R8A78000_CLK_VIN081             121
#define R8A78000_CLK_VIN082             122
#define R8A78000_CLK_VIN083             123
#define R8A78000_CLK_VIN084             124
#define R8A78000_CLK_VIN085             125
#define R8A78000_CLK_VIN086             126
#define R8A78000_CLK_VIN087             127
#define R8A78000_CLK_VIN090             128
#define R8A78000_CLK_VIN091             129
#define R8A78000_CLK_VIN092             130
#define R8A78000_CLK_VIN093             131
#define R8A78000_CLK_VIN094             132
#define R8A78000_CLK_VIN095             133
#define R8A78000_CLK_VIN096             134
#define R8A78000_CLK_VIN097             135
#define R8A78000_CLK_VIN100             136
#define R8A78000_CLK_VIN101             137
#define R8A78000_CLK_VIN102             138
#define R8A78000_CLK_VIN103             139
#define R8A78000_CLK_VIN104             140
#define R8A78000_CLK_VIN105             141
#define R8A78000_CLK_VIN106             142
#define R8A78000_CLK_VIN107             143
#define R8A78000_CLK_VIN110             144
#define R8A78000_CLK_VIN111             145
#define R8A78000_CLK_VIN112             146
#define R8A78000_CLK_VIN113             147
#define R8A78000_CLK_VIN114             148
#define R8A78000_CLK_VIN115             149
#define R8A78000_CLK_VIN116             150
#define R8A78000_CLK_VIN117             151
#define R8A78000_CLK_DOC2CH0            152
#define R8A78000_CLK_VCON0              153
#define R8A78000_CLK_VCON1              154
#define R8A78000_CLK_VCON2              155
#define R8A78000_CLK_VCON3              156
#define R8A78000_CLK_VCON4              157
#define R8A78000_CLK_VCON5              158
#define R8A78000_CLK_VCON6              159
#define R8A78000_CLK_VCON7              160
#define R8A78000_CLK_VCON8              161
#define R8A78000_CLK_VCON9              162
#define R8A78000_CLK_VSPB0              163
#define R8A78000_CLK_VSPB1              164
#define R8A78000_CLK_VSPB2              165
#define R8A78000_CLK_VSPB3              166
#define R8A78000_CLK_VSPB4              167
#define R8A78000_CLK_VSPI0              168
#define R8A78000_CLK_VSPI1              169
#define R8A78000_CLK_VSPI2              170
#define R8A78000_CLK_VSPI3              171
#define R8A78000_CLK_FCPVB0             172
#define R8A78000_CLK_FCPVB1             173
#define R8A78000_CLK_FCPVB2             174
#define R8A78000_CLK_FCPVB3             175
#define R8A78000_CLK_FCPVB4             176
#define R8A78000_CLK_FCPVI0             177
#define R8A78000_CLK_FCPVI1             178
#define R8A78000_CLK_FCPVI2             179
#define R8A78000_CLK_FCPVI3             180
#define R8A78000_CLK_VIN0               181
#define R8A78000_CLK_VIN1               182
#define R8A78000_CLK_VIN2               183
#define R8A78000_CLK_VIN3               184
#define R8A78000_CLK_VIN4               185
#define R8A78000_CLK_VIN5               186
#define R8A78000_CLK_VIN6               187
#define R8A78000_CLK_VIN7               188
#define R8A78000_CLK_VIN8               189
#define R8A78000_CLK_VIN9               190
#define R8A78000_CLK_VIN10              191
#define R8A78000_CLK_VIN11              192
#define R8A78000_CLK_PERE_GPIODM0       193
#define R8A78000_CLK_PERE_GPIODM1       194
#define R8A78000_CLK_PERE_GPIODM2       195
#define R8A78000_CLK_PERE_GPIODM3       196
#define R8A78000_CLK_RPC                197
#define R8A78000_CLK_UFS0               198
#define R8A78000_CLK_UFS1               199
#define R8A78000_CLK_SDHI0              200
#define R8A78000_CLK_PERW_GPIODM0       201
#define R8A78000_CLK_PERW_GPIODM1       202
#define R8A78000_CLK_PERW_GPIODM2       203
#define R8A78000_CLK_PERW_GPIODM3       204
#define R8A78000_CLK_SCIF0              205
#define R8A78000_CLK_SCIF1              206
#define R8A78000_CLK_SCIF2              207
#define R8A78000_CLK_SCIF3              208
#define R8A78000_CLK_I2C1               209
#define R8A78000_CLK_I2C2               210
#define R8A78000_CLK_I2C3               211
#define R8A78000_CLK_I2C4               212
#define R8A78000_CLK_I2C5               213
#define R8A78000_CLK_I2C6               214
#define R8A78000_CLK_I2C7               215
#define R8A78000_CLK_I2C8               216
#define R8A78000_CLK_I3C0               217
#define R8A78000_CLK_I3C1               218
#define R8A78000_CLK_I3C2               219
#define R8A78000_CLK_MSI4               220
#define R8A78000_CLK_MSI5               221
#define R8A78000_CLK_MSI6               222
#define R8A78000_CLK_MSI7               223
#define R8A78000_CLK_HSCIF0             224
#define R8A78000_CLK_HSCIF1             225
#define R8A78000_CLK_HSCIF2             226
#define R8A78000_CLK_HSCIF3             227
#define R8A78000_CLK_DRI00              228
#define R8A78000_CLK_DRI01              229
#define R8A78000_CLK_DRI10              230
#define R8A78000_CLK_DRI11              231
#define R8A78000_CLK_DRI20              232
#define R8A78000_CLK_DRI21              233
#define R8A78000_CLK_DRI30              234
#define R8A78000_CLK_DRI31              235
#define R8A78000_CLK_DRI40              236
#define R8A78000_CLK_DRI41              237
#define R8A78000_CLK_DRI50              238
#define R8A78000_CLK_DRI51              239
#define R8A78000_CLK_DRI60              240
#define R8A78000_CLK_DRI61              241
#define R8A78000_CLK_DRI70              242
#define R8A78000_CLK_DRI71              243
#define R8A78000_CLK_PWM0               244
#define R8A78000_CLK_TMU1               245
#define R8A78000_CLK_TMU2               246
#define R8A78000_CLK_TMU3               247
#define R8A78000_CLK_TMU4               248
#define R8A78000_CLK_TPU0               249
#define R8A78000_CLK_ADG0               250
#define R8A78000_CLK_ADG1               251
#define R8A78000_CLK_SSI0               252
#define R8A78000_CLK_SSI00              253
#define R8A78000_CLK_SSI01              254
#define R8A78000_CLK_SSI02              255
#define R8A78000_CLK_SSI03              256
#define R8A78000_CLK_SSI04              257
#define R8A78000_CLK_SSI05              258
#define R8A78000_CLK_SSI06              259
#define R8A78000_CLK_SSI07              260
#define R8A78000_CLK_SSI08              261
#define R8A78000_CLK_SSI09              262
#define R8A78000_CLK_SSI1               263
#define R8A78000_CLK_SSI10              264
#define R8A78000_CLK_SSI11              265
#define R8A78000_CLK_SSI12              266
#define R8A78000_CLK_SSI13              267
#define R8A78000_CLK_SSI14              268
#define R8A78000_CLK_SSI15              269
#define R8A78000_CLK_SSI16              270
#define R8A78000_CLK_SSI17              271
#define R8A78000_CLK_SSI18              272
#define R8A78000_CLK_SSI19              273
#define R8A78000_CLK_SCU0               274
#define R8A78000_CLK_SRC00              275
#define R8A78000_CLK_SRC01              276
#define R8A78000_CLK_SRC02              277
#define R8A78000_CLK_SRC03              278
#define R8A78000_CLK_SRC04              279
#define R8A78000_CLK_SRC05              280
#define R8A78000_CLK_SRC06              281
#define R8A78000_CLK_SRC07              282
#define R8A78000_CLK_SRC08              283
#define R8A78000_CLK_SRC09              284
#define R8A78000_CLK_SCU00              285
#define R8A78000_CLK_SCU01              286
#define R8A78000_CLK_DVC00              287
#define R8A78000_CLK_DVC01              288
#define R8A78000_CLK_SCU1               289
#define R8A78000_CLK_SRC10              290
#define R8A78000_CLK_SRC11              291
#define R8A78000_CLK_SRC12              292
#define R8A78000_CLK_SRC13              293
#define R8A78000_CLK_SRC14              294
#define R8A78000_CLK_SRC15              295
#define R8A78000_CLK_SRC16              296
#define R8A78000_CLK_SRC17              297
#define R8A78000_CLK_SRC18              298
#define R8A78000_CLK_SRC19              299
#define R8A78000_CLK_SCU10              300
#define R8A78000_CLK_SCU11              301
#define R8A78000_CLK_DVC10              302
#define R8A78000_CLK_DVC11              303
#define R8A78000_CLK_APD00              304
#define R8A78000_CLK_APD01              305
#define R8A78000_CLK_APD10              306
#define R8A78000_CLK_APD11              307
#define R8A78000_CLK_APD02              308
#define R8A78000_CLK_APD12              309
#define R8A78000_CLK_AULK2P             310
#define R8A78000_CLK_AULK4P             311
#define R8A78000_CLK_XPCS0              312
#define R8A78000_CLK_XPCS1              313
#define R8A78000_CLK_XPCS2              314
#define R8A78000_CLK_XPCS3              315
#define R8A78000_CLK_XPCS4              316
#define R8A78000_CLK_XPCS5              317
#define R8A78000_CLK_XPCS6              318
#define R8A78000_CLK_XPCS7              319
#define R8A78000_CLK_RSW3               320
#define R8A78000_CLK_RSW3TSN            321
#define R8A78000_CLK_RSW3AES            322
#define R8A78000_CLK_RSW3TSNTES0        323
#define R8A78000_CLK_RSW3TSNTES1        324
#define R8A78000_CLK_RSW3TSNTES2        325
#define R8A78000_CLK_RSW3TSNTES3        326
#define R8A78000_CLK_RSW3TSNTES4        327
#define R8A78000_CLK_RSW3TSNTES5        328
#define R8A78000_CLK_RSW3TSNTES6        329
#define R8A78000_CLK_RSW3TSNTES7        330
#define R8A78000_CLK_RSW3MFWD           331
#define R8A78000_CLK_HSCN_GPIODM0       332
#define R8A78000_CLK_HSCN_GPIODM1       333
#define R8A78000_CLK_HSCN_GPIODM2       334
#define R8A78000_CLK_HSCN_GPIODM3       335
#define R8A78000_CLK_US30               336
#define R8A78000_CLK_US31               337
#define R8A78000_CLK_US32               338
#define R8A78000_CLK_US33               339
#define R8A78000_CLK_MPPHY01            340
#define R8A78000_CLK_MPPHY11            341
#define R8A78000_CLK_MPPHY21            342
#define R8A78000_CLK_MPPHY31            343
#define R8A78000_CLK_MPPHY02            344
#define R8A78000_CLK_PCI401             345
#define R8A78000_CLK_PCI411             346
#define R8A78000_CLK_PCI402             347
#define R8A78000_CLK_PCI412             348
#define R8A78000_CLK_CR52TOP0           349
#define R8A78000_CLK_CR52TOP0_BD        350
#define R8A78000_CLK_CR52CORE0          351
#define R8A78000_CLK_CR52CORE0_PO       352
#define R8A78000_CLK_CR52CORE1          353
#define R8A78000_CLK_CR52CORE1_PO       354
#define R8A78000_CLK_CR52SHADOW0        355
#define R8A78000_CLK_CR52SHADOW0_PO     356
#define R8A78000_CLK_CR52SHADOW1        357
#define R8A78000_CLK_CR52SHADOW1_PO     358
#define R8A78000_CLK_CR52TOP1           359
#define R8A78000_CLK_CR52TOP1_DEB       360
#define R8A78000_CLK_CR52CORE2          361
#define R8A78000_CLK_CR52CORE2_PO       362
#define R8A78000_CLK_CR52CORE3          363
#define R8A78000_CLK_CR52CORE3_PO       364
#define R8A78000_CLK_CR52SHADOW2        365
#define R8A78000_CLK_CR52SHADOW2_PO     366
#define R8A78000_CLK_CR52SHADOW3        367
#define R8A78000_CLK_CR52SHADOW3_PO     368
#define R8A78000_CLK_CR52TOP2           369
#define R8A78000_CLK_CR52TOP2_DB        370
#define R8A78000_CLK_CR52CORE4          371
#define R8A78000_CLK_CR52CORE4_PO       372
#define R8A78000_CLK_CR52CORE5          373
#define R8A78000_CLK_CR52CORE5_PO       374
#define R8A78000_CLK_CR52SHADOW4        375
#define R8A78000_CLK_CR52SHADOW4_PO     376
#define R8A78000_CLK_CR52SHADOW5        377
#define R8A78000_CLK_CR52SHADOW5_PO     378
#define R8A78000_CLK_CSD                379
#define R8A78000_CLK_OSTM0              380
#define R8A78000_CLK_OSTM1              381
#define R8A78000_CLK_OSTM2              382
#define R8A78000_CLK_OSTM3              383
#define R8A78000_CLK_OSTM4              384
#define R8A78000_CLK_OSTM5              385
#define R8A78000_CLK_TMU0               386
#define R8A78000_CLK_WDT0               387
#define R8A78000_CLK_WDT1               388
#define R8A78000_CLK_WWDT00             389
#define R8A78000_CLK_WWDT10             390
#define R8A78000_CLK_WWDT20             391
#define R8A78000_CLK_WWDT30             392
#define R8A78000_CLK_WWDT40             393
#define R8A78000_CLK_WWDT50             394
#define R8A78000_CLK_WWDT60             395
#define R8A78000_CLK_WWDT70             396
#define R8A78000_CLK_WWDT80             397
#define R8A78000_CLK_WWDT90             398
#define R8A78000_CLK_WWDT100            399
#define R8A78000_CLK_WWDT110            400
#define R8A78000_CLK_WWDT120            401
#define R8A78000_CLK_WWDT130            402
#define R8A78000_CLK_WWDT01             403
#define R8A78000_CLK_WWDT11             404
#define R8A78000_CLK_WWDT21             405
#define R8A78000_CLK_WWDT31             406
#define R8A78000_CLK_WWDT41             407
#define R8A78000_CLK_WWDT51             408
#define R8A78000_CLK_WWDT61             409
#define R8A78000_CLK_WWDT71             410
#define R8A78000_CLK_WWDT81             411
#define R8A78000_CLK_WWDT91             412
#define R8A78000_CLK_WWDT101            413
#define R8A78000_CLK_WWDT111            414
#define R8A78000_CLK_WWDT121            415
#define R8A78000_CLK_WWDT131            416
#define R8A78000_CLK_WWDT140            417
#define R8A78000_CLK_WWDT141            418
#define R8A78000_CLK_WWDT150            419
#define R8A78000_CLK_WWDT151            420
#define R8A78000_CLK_WWDT160            421
#define R8A78000_CLK_WWDT161            422
#define R8A78000_CLK_WWDT170            423
#define R8A78000_CLK_WWDT171            424
#define R8A78000_CLK_WWDT180            425
#define R8A78000_CLK_WWDT181            426
#define R8A78000_CLK_WWDT190            427
#define R8A78000_CLK_WWDT191            428
#define R8A78000_CLK_SWDT0              429
#define R8A78000_CLK_SWDT1              430
#define R8A78000_CLK_WCRC0              431
#define R8A78000_CLK_WCRC1              432
#define R8A78000_CLK_WCRC2              433
#define R8A78000_CLK_WCRC3              434
#define R8A78000_CLK_WCRC4              435
#define R8A78000_CLK_WCRC5              436
#define R8A78000_CLK_WCRC6              437
#define R8A78000_CLK_WCRC7              438
#define R8A78000_CLK_WCRC8              439
#define R8A78000_CLK_WCRC9              440
#define R8A78000_CLK_WCRC10             441
#define R8A78000_CLK_CRC0               442
#define R8A78000_CLK_CRC1               443
#define R8A78000_CLK_CRC2               444
#define R8A78000_CLK_CRC3               445
#define R8A78000_CLK_CRC4               446
#define R8A78000_CLK_CRC5               447
#define R8A78000_CLK_CRC6               448
#define R8A78000_CLK_CRC7               449
#define R8A78000_CLK_CRC8               450
#define R8A78000_CLK_CRC9               451
#define R8A78000_CLK_CRC10              452
#define R8A78000_CLK_KCRC0              453
#define R8A78000_CLK_KCRC1              454
#define R8A78000_CLK_KCRC2              455
#define R8A78000_CLK_KCRC3              456
#define R8A78000_CLK_KCRC4              457
#define R8A78000_CLK_KCRC5              458
#define R8A78000_CLK_KCRC6              459
#define R8A78000_CLK_KCRC7              460
#define R8A78000_CLK_KCRC8              461
#define R8A78000_CLK_KCRC9              462
#define R8A78000_CLK_KCRC10             463
#define R8A78000_CLK_INTAP0             464
#define R8A78000_CLK_INTTP              465
#define R8A78000_CLK_INTAP1             466
#define R8A78000_CLK_RTDM0              467
#define R8A78000_CLK_RTDM1              468
#define R8A78000_CLK_RTDM2              469
#define R8A78000_CLK_RTDM3              470
#define R8A78000_CLK_FBDM0              471
#define R8A78000_CLK_FBDM1              472
#define R8A78000_CLK_SECROM             473
#define R8A78000_CLK_CRAC0              474
#define R8A78000_CLK_CRAC1              475
#define R8A78000_CLK_CRAC2              476
#define R8A78000_CLK_CRAC3              477
#define R8A78000_CLK_CRAC4              478
#define R8A78000_CLK_CRAC5              479
#define R8A78000_CLK_CRAC6              480
#define R8A78000_CLK_CRAC7              481
#define R8A78000_CLK_CRAC8              482
#define R8A78000_CLK_CRAC9              483
#define R8A78000_CLK_CRAC10             484
#define R8A78000_CLK_CRAC11             485
#define R8A78000_CLK_CRAC12             486
#define R8A78000_CLK_CRAC13             487
#define R8A78000_CLK_CRAC14             488
#define R8A78000_CLK_CRAC15             489
#define R8A78000_CLK_CRAC16             490
#define R8A78000_CLK_CRAC17             491
#define R8A78000_CLK_CRAC18             492
#define R8A78000_CLK_CRAC19             493
#define R8A78000_CLK_APRTMGINT0         494
#define R8A78000_CLK_APRTMGINT1         495
#define R8A78000_CLK_APRTMGINT2         496
#define R8A78000_CLK_APRTMGINT3         497
#define R8A78000_CLK_APRTMGINT4         498
#define R8A78000_CLK_APRTMGINT5         499
#define R8A78000_CLK_APRTMGINT6         500
#define R8A78000_CLK_APRTMGINT7         501
#define R8A78000_CLK_C0RTMG             502
#define R8A78000_CLK_CMN_TOPN_GIC       503
#define R8A78000_CLK_CMN_TOPN_DBG       504
#define R8A78000_CLK_CMN_TOPE           505
#define R8A78000_CLK_CMN_TOPS           506
#define R8A78000_CLK_CMN_TOPW           507
#define R8A78000_CLK_UCIEBG0ICN0        508
#define R8A78000_CLK_UCIEBG0ICN1        509
#define R8A78000_CLK_CSBRG_DSPTOP       510
#define R8A78000_CLK_CSBRG_NPUTOP0      511
#define R8A78000_CLK_CSBRG_NPUTOP1      512
#define R8A78000_CLK_SCMT               513
#define R8A78000_CLK_UCMT               514
#define R8A78000_CLK_CMT0               515
#define R8A78000_CLK_CMT1               516
#define R8A78000_CLK_CMT2               517
#define R8A78000_CLK_CMT3               518
#define R8A78000_CLK_LTM0               519
#define R8A78000_CLK_LTM1               520
#define R8A78000_CLK_LTM2               521
#define R8A78000_CLK_INTAP_CMN2TOP0     522
#define R8A78000_CLK_PCI60BG0           523
#define R8A78000_CLK_PCI60BG1           524
#define R8A78000_CLK_ADVFSC             525
#define R8A78000_CLK_ADVFSC_KEN         526
#define R8A78000_CLK_TSC1               527
#define R8A78000_CLK_UCIE01             528
#define R8A78000_CLK_UCIE02             529
#define R8A78000_CLK_UCIE11             530
#define R8A78000_CLK_UCIE12             531
#define R8A78000_CLK_UCIEBG1DEV0        532
#define R8A78000_CLK_UCIEBG1DEV1        533
#define R8A78000_CLK_UCIEBG1ICN0        534
#define R8A78000_CLK_UCIEBG1ICN1        535
#define R8A78000_CLK_UCIEBG0DEV0        536
#define R8A78000_CLK_UCIEBG0DEV1        537
#define R8A78000_CLK_PCI601             538
#define R8A78000_CLK_PCI611             539
#define R8A78000_CLK_PCI602             540
#define R8A78000_CLK_PCI612             541
#define R8A78000_CLK_IMN_IMR000         542
#define R8A78000_CLK_IMN_IMR001         543
#define R8A78000_CLK_IMN_IMS00          544
#define R8A78000_CLK_IMN_IMS01          545
#define R8A78000_CLK_IMN_IMS02          546
#define R8A78000_CLK_IMN_IMS03          547
#define R8A78000_CLK_IMS_IMR000         548
#define R8A78000_CLK_IMS_IMR001         549
#define R8A78000_CLK_IMS_IMS00          550
#define R8A78000_CLK_IMS_IMS01          551
#define R8A78000_CLK_IMS_IMS02          552
#define R8A78000_CLK_IMS_IMS03          553
#define R8A78000_CLK_RGX_JONES0         554
#define R8A78000_CLK_RGX_MERCER0        555
#define R8A78000_CLK_RGX_MERCER1        556
#define R8A78000_CLK_RGX_MERCER2        557
#define R8A78000_CLK_RGX_MERCER3        558
#define R8A78000_CLK_RGX_TEXAS0         559
#define R8A78000_CLK_RGX_TEXAS1         560
#define R8A78000_CLK_RGX_SWIFT0         561
#define R8A78000_CLK_RGX_SWIFT1         562
#define R8A78000_CLK_RGX_SWIFT2         563
#define R8A78000_CLK_RGX_SWIFT3         564
#define R8A78000_CLK_RGX_JONES1         565
#define R8A78000_CLK_RGX_MERCER4        566
#define R8A78000_CLK_RGX_MERCER5        567
#define R8A78000_CLK_RGX_MERCER6        568
#define R8A78000_CLK_RGX_MERCER7        569
#define R8A78000_CLK_RGX_TEXAS2         570
#define R8A78000_CLK_RGX_TEXAS3         571
#define R8A78000_CLK_RGX_SWIFT4         572
#define R8A78000_CLK_RGX_SWIFT5         573
#define R8A78000_CLK_RGX_SWIFT6         574
#define R8A78000_CLK_RGX_SWIFT7         575
#define R8A78000_CLK_CSDBG_DSP          576
#define R8A78000_CLK_DSPARCSYN_RST      577
#define R8A78000_CLK_DSPARCSYN_AXI      578
#define R8A78000_CLK_DSPARCSYN_REG      579
#define R8A78000_CLK_DSP2_MISC_RST      580
#define R8A78000_CLK_DSP2_MISC_PORES    581
#define R8A78000_CLK_DSP2_MISC_ATRES    582
#define R8A78000_CLK_DSP2_CORE0_RST     583
#define R8A78000_CLK_DSP2_CORE0_CSD     584
#define R8A78000_CLK_DSP2_CORE1_RST     585
#define R8A78000_CLK_DSP2_CORE1_CSD     586
#define R8A78000_CLK_DSP2_CORE2_RST     587
#define R8A78000_CLK_DSP2_CORE2_CSD     588
#define R8A78000_CLK_DSP2_CORE3_RST     589
#define R8A78000_CLK_DSP2_CORE3_CSD     590
#define R8A78000_CLK_DSP_REG0           591
#define R8A78000_CLK_DSP3_MISC_RST      592
#define R8A78000_CLK_DSP3_MISC_PORES    593
#define R8A78000_CLK_DSP3_MISC_ATRES    594
#define R8A78000_CLK_DSP3_CORE0_RST     595
#define R8A78000_CLK_DSP3_CORE0_CSD     596
#define R8A78000_CLK_DSP3_CORE1_RST     597
#define R8A78000_CLK_DSP3_CORE1_CSD     598
#define R8A78000_CLK_DSP3_CORE2_RST     599
#define R8A78000_CLK_DSP3_CORE2_CSD     600
#define R8A78000_CLK_DSP3_CORE3_RST     601
#define R8A78000_CLK_DSP3_CORE3_CSD     602
#define R8A78000_CLK_DSP_REG1           603
#define R8A78000_CLK_DSP4_MISC_RST      604
#define R8A78000_CLK_DSP4_MISC_PORES    605
#define R8A78000_CLK_DSP4_MISC_ATRES    606
#define R8A78000_CLK_DSP4_CORE0_RST     607
#define R8A78000_CLK_DSP4_CORE0_CSD     608
#define R8A78000_CLK_DSP4_CORE1_RST     609
#define R8A78000_CLK_DSP4_CORE1_CSD     610
#define R8A78000_CLK_DSP4_CORE2_RST     611
#define R8A78000_CLK_DSP4_CORE2_CSD     612
#define R8A78000_CLK_DSP4_CORE3_RST     613
#define R8A78000_CLK_DSP4_CORE3_CSD     614
#define R8A78000_CLK_DSP_REG2           615
#define R8A78000_CLK_DSP5_MISC_RST      616
#define R8A78000_CLK_DSP5_MISC_PORES    617
#define R8A78000_CLK_DSP5_MISC_ATRES    618
#define R8A78000_CLK_DSP5_CORE0_RST     619
#define R8A78000_CLK_DSP5_CORE0_CSD     620
#define R8A78000_CLK_DSP5_CORE1_RST     621
#define R8A78000_CLK_DSP5_CORE1_CSD     622
#define R8A78000_CLK_DSP5_CORE2_RST     623
#define R8A78000_CLK_DSP5_CORE2_CSD     624
#define R8A78000_CLK_DSP5_CORE3_RST     625
#define R8A78000_CLK_DSP5_CORE3_CSD     626
#define R8A78000_CLK_DSP_REG3           627
#define R8A78000_CLK_DSP6_MISC_RST      628
#define R8A78000_CLK_DSP6_MISC_PORES    629
#define R8A78000_CLK_DSP6_MISC_ATRES    630
#define R8A78000_CLK_DSP6_CORE0_RST     631
#define R8A78000_CLK_DSP6_CORE0_CSD     632
#define R8A78000_CLK_DSP6_CORE1_RST     633
#define R8A78000_CLK_DSP6_CORE1_CSD     634
#define R8A78000_CLK_DSP6_CORE2_RST     635
#define R8A78000_CLK_DSP6_CORE2_CSD     636
#define R8A78000_CLK_DSP6_CORE3_RST     637
#define R8A78000_CLK_DSP6_CORE3_CSD     638
#define R8A78000_CLK_DSP_REG4           639
#define R8A78000_CLK_FCPRS0             640
#define R8A78000_CLK_FCPRS1             641
#define R8A78000_CLK_FCPRS2             642
#define R8A78000_CLK_FCPRS3             643
#define R8A78000_CLK_FCPRS4             644
#define R8A78000_CLK_FCPRS5             645
#define R8A78000_CLK_FCPRS6             646
#define R8A78000_CLK_FCPRS7             647
#define R8A78000_CLK_FCPRC0             648
#define R8A78000_CLK_FCPRC1             649
#define R8A78000_CLK_FCPRC2             650
#define R8A78000_CLK_FCPRC3             651
#define R8A78000_CLK_FCPRC4             652
#define R8A78000_CLK_FCPRC5             653
#define R8A78000_CLK_FCPRC6             654
#define R8A78000_CLK_FCPRC7             655
#define R8A78000_CLK_NPU0_CSDBG         656
#define R8A78000_CLK_NPU0_ATRES         657
#define R8A78000_CLK_NPU0_RST           658
#define R8A78000_CLK_NPU0_AXI           659
#define R8A78000_CLK_NPU0_NL2           660
#define R8A78000_CLK_NPU0_NL2ARC0       661
#define R8A78000_CLK_NPU0_NL2ARC1       662
#define R8A78000_CLK_NPU0_NL1GRP0       663
#define R8A78000_CLK_NPU0_SL0NL1ARC     664
#define R8A78000_CLK_NPU0_SL1NL1ARC     665
#define R8A78000_CLK_NPU0_SL2NL1ARC     666
#define R8A78000_CLK_NPU0_NL1GRP1       667
#define R8A78000_CLK_NPU0_SL3NL1ARC     668
#define R8A78000_CLK_NPU0_SL4NL1ARC     669
#define R8A78000_CLK_NPU0_SL5NL1ARC     670
#define R8A78000_CLK_NPU0_NL1GRP2       671
#define R8A78000_CLK_NPU0_SL6NL1ARC     672
#define R8A78000_CLK_NPU0_SL7NL1ARC     673
#define R8A78000_CLK_NPU0_SL8NL1ARC     674
#define R8A78000_CLK_NPU0_NL1GRP3       675
#define R8A78000_CLK_NPU0_SL9NL1ARC     676
#define R8A78000_CLK_NPU0_SL10NL1ARC    677
#define R8A78000_CLK_NPU0_SL11NL1ARC    678
#define R8A78000_CLK_NPU0_ARC_REG0      679
#define R8A78000_CLK_NPU0_AON_CORE      680
#define R8A78000_CLK_NPU0_AON_NOC       681
#define R8A78000_CLK_NPU0_AON_CFG       682
#define R8A78000_CLK_NPU0_AON_CSD       683
#define R8A78000_CLK_NPU0_CORE0_GRP0    684
#define R8A78000_CLK_NPU0_CORE1_GRP0    685
#define R8A78000_CLK_NPU0_CORE2_GRP0    686
#define R8A78000_CLK_NPU0_CORE0_GRP1    687
#define R8A78000_CLK_NPU0_CORE1_GRP1    688
#define R8A78000_CLK_NPU0_CORE2_GRP1    689
#define R8A78000_CLK_NPU0_CORE0_GRP2    690
#define R8A78000_CLK_NPU0_CORE1_GRP2    691
#define R8A78000_CLK_NPU0_CORE2_GRP2    692
#define R8A78000_CLK_NPU0_CORE0_GRP3    693
#define R8A78000_CLK_NPU0_CORE1_GRP3    694
#define R8A78000_CLK_NPU0_CORE2_GRP3    695
#define R8A78000_CLK_NPU0_PRES          696
#define R8A78000_CLK_NPU0_REG0          697
#define R8A78000_CLK_NPU0_MISC_RST      698
#define R8A78000_CLK_NPU0_MISC_PRES     699
#define R8A78000_CLK_NPU0_MISC_ATRES    700
#define R8A78000_CLK_NPU0_C0_DSP_RST    701
#define R8A78000_CLK_NPU0_C0_DSP_CSD    702
#define R8A78000_CLK_NPU0_C1_DSP_RST    703
#define R8A78000_CLK_NPU0_C1_DSP_CSD    704
#define R8A78000_CLK_NPU0_C2_DSP_RST    705
#define R8A78000_CLK_NPU0_C2_DSP_CSD    706
#define R8A78000_CLK_NPU0_C3_DSP_RST    707
#define R8A78000_CLK_NPU0_C3_DSP_CSD    708
#define R8A78000_CLK_NPU0_DSP_REG0      709
#define R8A78000_CLK_NPU1_CSDBG         710
#define R8A78000_CLK_NPU1_ATRES         711
#define R8A78000_CLK_NPU1_RST           712
#define R8A78000_CLK_NPU1_AXI           713
#define R8A78000_CLK_NPU1_NL2           714
#define R8A78000_CLK_NPU1_NL2ARC0       715
#define R8A78000_CLK_NPU1_NL2ARC1       716
#define R8A78000_CLK_NPU1_NL1GRP0       717
#define R8A78000_CLK_NPU1_SL0NL1ARC     718
#define R8A78000_CLK_NPU1_SL1NL1ARC     719
#define R8A78000_CLK_NPU1_SL2NL1ARC     720
#define R8A78000_CLK_NPU1_NL1GRP1       721
#define R8A78000_CLK_NPU1_SL3NL1ARC     722
#define R8A78000_CLK_NPU1_SL4NL1ARC     723
#define R8A78000_CLK_NPU1_SL5NL1ARC     724
#define R8A78000_CLK_NPU1_NL1GRP2       725
#define R8A78000_CLK_NPU1_SL6NL1ARC     726
#define R8A78000_CLK_NPU1_SL7NL1ARC     727
#define R8A78000_CLK_NPU1_SL8NL1ARC     728
#define R8A78000_CLK_NPU1_NL1GRP3       729
#define R8A78000_CLK_NPU1_SL9NL1ARC     730
#define R8A78000_CLK_NPU1_SL10NL1ARC    731
#define R8A78000_CLK_NPU1_SL11NL1ARC    732
#define R8A78000_CLK_NPU1_ARC_REG0      733
#define R8A78000_CLK_NPU1_AON_CORE      734
#define R8A78000_CLK_NPU1_AON_NOC       735
#define R8A78000_CLK_NPU1_AON_CFG       736
#define R8A78000_CLK_NPU1_AON_CSD       737
#define R8A78000_CLK_NPU1_CORE0_GRP0    738
#define R8A78000_CLK_NPU1_CORE1_GRP0    739
#define R8A78000_CLK_NPU1_CORE2_GRP0    740
#define R8A78000_CLK_NPU1_CORE0_GRP1    741
#define R8A78000_CLK_NPU1_CORE1_GRP1    742
#define R8A78000_CLK_NPU1_CORE2_GRP1    743
#define R8A78000_CLK_NPU1_CORE0_GRP2    744
#define R8A78000_CLK_NPU1_CORE1_GRP2    745
#define R8A78000_CLK_NPU1_CORE2_GRP2    746
#define R8A78000_CLK_NPU1_CORE0_GRP3    747
#define R8A78000_CLK_NPU1_CORE1_GRP3    748
#define R8A78000_CLK_NPU1_CORE2_GRP3    749
#define R8A78000_CLK_NPU1_PRES          750
#define R8A78000_CLK_NPU1_REG0          751
#define R8A78000_CLK_NPU1_MISC_RST      752
#define R8A78000_CLK_NPU1_MISC_PRES     753
#define R8A78000_CLK_NPU1_MISC_ATRES    754
#define R8A78000_CLK_NPU1_C0_DSP_RST    755
#define R8A78000_CLK_NPU1_C0_DSP_CSD    756
#define R8A78000_CLK_NPU1_C1_DSP_RST    757
#define R8A78000_CLK_NPU1_C1_DSP_CSD    758
#define R8A78000_CLK_NPU1_C2_DSP_RST    759
#define R8A78000_CLK_NPU1_C2_DSP_CSD    760
#define R8A78000_CLK_NPU1_C3_DSP_RST    761
#define R8A78000_CLK_NPU1_C3_DSP_CSD    762
#define R8A78000_CLK_NPU1_DSP_REG0      763
#define R8A78000_CLK_CMN_CORE0_PORES    764
#define R8A78000_CLK_CMN_CORE0_SYRES    765
#define R8A78000_CLK_CMN_CORE1_PORES    766
#define R8A78000_CLK_CMN_CORE1_SYRES    767
#define R8A78000_CLK_CMN_CORE2_PORES    768
#define R8A78000_CLK_CMN_CORE2_SYRES    769
#define R8A78000_CLK_CMN_CORE3_PORES    770
#define R8A78000_CLK_CMN_CORE3_SYRES    771
#define R8A78000_CLK_SCP                772
#define R8A78000_CLK_TAUD0              773
#define R8A78000_CLK_TAUD1              774
#define R8A78000_CLK_TAUJ1              775
#define R8A78000_CLK_MSI0               776
#define R8A78000_CLK_MSI1               777
#define R8A78000_CLK_MSI2               778
#define R8A78000_CLK_MSI3               779
#define R8A78000_CLK_I2C0               780
#define R8A78000_CLK_CANXL0             781
#define R8A78000_CLK_CANXL1             782
#define R8A78000_CLK_LIN00              783
#define R8A78000_CLK_LIN01              784
#define R8A78000_CLK_LIN02              785
#define R8A78000_CLK_LIN03              786
#define R8A78000_CLK_LIN10              787
#define R8A78000_CLK_LIN11              788
#define R8A78000_CLK_LIN12              789
#define R8A78000_CLK_LIN13              790
#define R8A78000_CLK_LIN20              791
#define R8A78000_CLK_LIN21              792
#define R8A78000_CLK_LIN22              793
#define R8A78000_CLK_LIN23              794
#define R8A78000_CLK_LIN30              795
#define R8A78000_CLK_LIN31              796
#define R8A78000_CLK_LIN32              797
#define R8A78000_CLK_LIN33              798
#define R8A78000_CLK_CANFD0             799
#define R8A78000_CLK_CANFD1             800
#define R8A78000_CLK_FRAY00             801
#define R8A78000_CLK_FRAY01             802
#define R8A78000_CLK_TSYN               803
#define R8A78000_CLK_WWDT200            804
#define R8A78000_CLK_WWDT201            805
#define R8A78000_CLK_SCDM0              806
#define R8A78000_CLK_SCDM1              807
#define R8A78000_CLK_INTSCP             808
#define R8A78000_CLK_TAUJ3              809
#define R8A78000_CLK_RTCA               810
#define R8A78000_CLK_GPIODM0            811
#define R8A78000_CLK_GPIODM1            812
#define R8A78000_CLK_GPIODM2            813
#define R8A78000_CLK_GPIODM3            814
#define R8A78000_CLK_S0D1               815
#define R8A78000_CLK_S0D2               816
#define R8A78000_CLK_S0D4               817
#define R8A78000_CLK_S0D8               818
#define R8A78000_CLK_CL                 819
#define R8A78000_CLK_SGD1               820
#define R8A78000_CLK_SGD2               821
#define R8A78000_CLK_ZT                 822
#define R8A78000_CLK_ZTR                823
#define R8A78000_CLK_CL16M              824
#define R8A78000_CLK_ZB3_TOP_0          825
#define R8A78000_CLK_ZB3_TOP_1          826
#define R8A78000_CLK_ZB3_TOP_2          827
#define R8A78000_CLK_ZB3_TOP_3          828
#define R8A78000_CLK_ZB3_TOP_4          829
#define R8A78000_CLK_ZB3_TOP_5          830
#define R8A78000_CLK_ZB3_TOP_6          831
#define R8A78000_CLK_ZB3_TOP_7          832
#define R8A78000_CLK_ZX                 833
#define R8A78000_CLK_ZC0_APU0           834
#define R8A78000_CLK_ZC1_APU0           835
#define R8A78000_CLK_ZD_APU0            836
#define R8A78000_CLK_ZC0_APU1           837
#define R8A78000_CLK_ZC1_APU1           838
#define R8A78000_CLK_ZD_APU1            839
#define R8A78000_CLK_ZC0_APU2           840
#define R8A78000_CLK_ZC1_APU2           841
#define R8A78000_CLK_ZD_APU2            842
#define R8A78000_CLK_ZC0_APU3           843
#define R8A78000_CLK_ZC1_APU3           844
#define R8A78000_CLK_ZD_APU3            845
#define R8A78000_CLK_ZC0_APU4           846
#define R8A78000_CLK_ZC1_APU4           847
#define R8A78000_CLK_ZD_APU4            848
#define R8A78000_CLK_ZC0_APU5           849
#define R8A78000_CLK_ZC1_APU5           850
#define R8A78000_CLK_ZD_APU5            851
#define R8A78000_CLK_ZC0_APU6           852
#define R8A78000_CLK_ZC1_APU6           853
#define R8A78000_CLK_ZD_APU6            854
#define R8A78000_CLK_ZC0_APU7           855
#define R8A78000_CLK_ZC1_APU7           856
#define R8A78000_CLK_ZD_APU7            857
#define R8A78000_CLK_S0D1_CMN_BUSN      858
#define R8A78000_CLK_S0D2_CMN_BUSN      859
#define R8A78000_CLK_S0D4_CMN_BUSN      860
#define R8A78000_CLK_ZX_CMN_BUSN        861
#define R8A78000_CLK_S0D1_CMN_BUSS      862
#define R8A78000_CLK_S0D2_CMN_BUSS      863
#define R8A78000_CLK_S0D4_CMN_BUSS      864
#define R8A78000_CLK_ZX_CMN_BUSS        865
#define R8A78000_CLK_ZX_CMN_MAIN0       866
#define R8A78000_CLK_ZX_CMN_MAIN1       867
#define R8A78000_CLK_CMN_CORE_GRP2      868
#define R8A78000_CLK_CMN_CORE_GRP3      869
#define R8A78000_CLK_CMN_CCG2_GRP0      870
#define R8A78000_CLK_CMN_CCG2_GRP1      871
#define R8A78000_CLK_CMN_CCG2_GRP2      872
#define R8A78000_CLK_CMN_CCG2_GRP3      873
#define R8A78000_CLK_CMN_CCG3_GRP0      874
#define R8A78000_CLK_CMN_CCG3_GRP1      875
#define R8A78000_CLK_CMN_CCG3_GRP2      876
#define R8A78000_CLK_CMN_CCG3_GRP3      877
#define R8A78000_CLK_SGD1_VIO_OTHER     878
#define R8A78000_CLK_SGD2_VIO_OTHER     879
#define R8A78000_CLK_SGD4_VIO_OTHER     880
#define R8A78000_CLK_SGD8_VIO_OTHER     881
#define R8A78000_CLK_SGD16_VIO_OTHER    882
#define R8A78000_CLK_VCON_VIO_OTHER     883
#define R8A78000_CLK_SGD1_VIO_BUS       884
#define R8A78000_CLK_SGD2_VIO_BUS       885
#define R8A78000_CLK_SGD4_VIO_BUS       886
#define R8A78000_CLK_SGD8_VIO_BUS       887
#define R8A78000_CLK_SGD16_VIO_BUS      888
#define R8A78000_CLK_SGD1_VIO_CSI0      889
#define R8A78000_CLK_SGD2_VIO_CSI0      890
#define R8A78000_CLK_SGD4_VIO_CSI0      891
#define R8A78000_CLK_SGD8_VIO_CSI0      892
#define R8A78000_CLK_SGD16_VIO_CSI0     893
#define R8A78000_CLK_CSI_VIO_CSI0       894
#define R8A78000_CLK_SGD1_VIO_CSI1      895
#define R8A78000_CLK_SGD2_VIO_CSI1      896
#define R8A78000_CLK_SGD4_VIO_CSI1      897
#define R8A78000_CLK_SGD8_VIO_CSI1      898
#define R8A78000_CLK_SGD16_VIO_CSI1     899
#define R8A78000_CLK_CSI_VIO_CSI1       900
#define R8A78000_CLK_SGD1_VIO_CSI2      901
#define R8A78000_CLK_SGD2_VIO_CSI2      902
#define R8A78000_CLK_SGD4_VIO_CSI2      903
#define R8A78000_CLK_SGD8_VIO_CSI2      904
#define R8A78000_CLK_SGD16_VIO_CSI2     905
#define R8A78000_CLK_CSI_VIO_CSI2       906
#define R8A78000_CLK_SGD1_VIO_ISP0      907
#define R8A78000_CLK_SGD2_VIO_ISP0      908
#define R8A78000_CLK_SGD4_VIO_ISP0      909
#define R8A78000_CLK_SGD8_VIO_ISP0      910
#define R8A78000_CLK_SGD16_VIO_ISP0     911
#define R8A78000_CLK_SGD1_VIO_ISP1      912
#define R8A78000_CLK_SGD2_VIO_ISP1      913
#define R8A78000_CLK_SGD4_VIO_ISP1      914
#define R8A78000_CLK_SGD8_VIO_ISP1      915
#define R8A78000_CLK_SGD16_VIO_ISP1     916
#define R8A78000_CLK_SGD1_VIO_ISP2      917
#define R8A78000_CLK_SGD2_VIO_ISP2      918
#define R8A78000_CLK_SGD4_VIO_ISP2      919
#define R8A78000_CLK_SGD8_VIO_ISP2      920
#define R8A78000_CLK_SGD16_VIO_ISP2     921
#define R8A78000_CLK_SGD1_VIO_ISP3      922
#define R8A78000_CLK_SGD2_VIO_ISP3      923
#define R8A78000_CLK_SGD4_VIO_ISP3      924
#define R8A78000_CLK_SGD8_VIO_ISP3      925
#define R8A78000_CLK_SGD16_VIO_ISP3     926
#define R8A78000_CLK_S0D1_VIO_IM0       927
#define R8A78000_CLK_S0D2_VIO_IM0       928
#define R8A78000_CLK_S0D4_VIO_IM0       929
#define R8A78000_CLK_S0D1_VIO_IM1       930
#define R8A78000_CLK_S0D2_VIO_IM1       931
#define R8A78000_CLK_S0D4_VIO_IM1       932
#define R8A78000_CLK_S0D1_VIO_IM2       933
#define R8A78000_CLK_S0D2_VIO_IM2       934
#define R8A78000_CLK_S0D4_VIO_IM2       935
#define R8A78000_CLK_SGD1_OTHER0        936
#define R8A78000_CLK_SGD2_OTHER0        937
#define R8A78000_CLK_SGD4_OTHER0        938
#define R8A78000_CLK_SGD8_OTHER0        939
#define R8A78000_CLK_SGD16_OTHER0       940
#define R8A78000_CLK_VCONCK_OTHER0      941
#define R8A78000_CLK_DP_EXT_OTHER0      942
#define R8A78000_CLK_SGD1_OTHER1        943
#define R8A78000_CLK_SGD2_OTHER1        944
#define R8A78000_CLK_SGD4_OTHER1        945
#define R8A78000_CLK_SGD8_OTHER1        946
#define R8A78000_CLK_SGD16_OTHER1       947
#define R8A78000_CLK_VCONCK_OTHER1      948
#define R8A78000_CLK_DP_EXT_OTHER1      949
#define R8A78000_CLK_SGD1_OTHER2        950
#define R8A78000_CLK_SGD2_OTHER2        951
#define R8A78000_CLK_SGD4_OTHER2        952
#define R8A78000_CLK_SGD8_OTHER2        953
#define R8A78000_CLK_SGD16_OTHER2       954
#define R8A78000_CLK_VCONCK_OTHER2      955
#define R8A78000_CLK_DP_EXT_OTHER2      956
#define R8A78000_CLK_SGD1_VIO_DP_TX     957
#define R8A78000_CLK_SGD2_VIO_DP_TX     958
#define R8A78000_CLK_SGD4_VIO_DP_TX     959
#define R8A78000_CLK_SGD8_VIO_DP_TX     960
#define R8A78000_CLK_SGD16_VIO_DP_TX    961
#define R8A78000_CLK_VCONCK_TX          962
#define R8A78000_CLK_DP_EXT_TX          963
#define R8A78000_CLK_S0D1_VIPN_OTHER    964
#define R8A78000_CLK_S0D2_VIPN_OTHER    965
#define R8A78000_CLK_S0D4_VIPN_OTHER    966
#define R8A78000_CLK_S0D1_VIPS_OTHER    967
#define R8A78000_CLK_S0D2_VIPS_OTHER    968
#define R8A78000_CLK_S0D4_VIPS_OTHER    969
#define R8A78000_CLK_S0D1_IMN_OTHER     970
#define R8A78000_CLK_S0D2_IMN_OTHER     971
#define R8A78000_CLK_S0D4_IMN_OTHER     972
#define R8A78000_CLK_S0D1_IMN_CORE0     973
#define R8A78000_CLK_S0D2_IMN_CORE0     974
#define R8A78000_CLK_S0D4_IMN_CORE0     975
#define R8A78000_CLK_S0D1_IMN_CORE1     976
#define R8A78000_CLK_S0D2_IMN_CORE1     977
#define R8A78000_CLK_S0D4_IMN_CORE1     978
#define R8A78000_CLK_S0D1_IMS_OTHER     979
#define R8A78000_CLK_S0D2_IMS_OTHER     980
#define R8A78000_CLK_S0D4_IMS_OTHER     981
#define R8A78000_CLK_S0D1_IMS_CORE0     982
#define R8A78000_CLK_S0D2_IMS_CORE0     983
#define R8A78000_CLK_S0D4_IMS_CORE0     984
#define R8A78000_CLK_S0D1_IMS_CORE1     985
#define R8A78000_CLK_S0D2_IMS_CORE1     986
#define R8A78000_CLK_S0D4_IMS_CORE1     987
#define R8A78000_CLK_ZGD1_GPC_OTHER     988
#define R8A78000_CLK_ZGD2_GPC_OTHER     989
#define R8A78000_CLK_ZGD4_GPC_OTHER     990
#define R8A78000_CLK_ZGD1_GPC_JONES0    991
#define R8A78000_CLK_ZGD2_GPC_JONES0    992
#define R8A78000_CLK_ZGD4_GPC_JONES0    993
#define R8A78000_CLK_ZGD1_GPC_JONES1    994
#define R8A78000_CLK_ZGD2_GPC_JONES1    995
#define R8A78000_CLK_ZGD4_GPC_JONES1    996
#define R8A78000_CLK_ZGD1_GPC_MER0      997
#define R8A78000_CLK_ZGD2_GPC_MER0      998
#define R8A78000_CLK_ZGD4_GPC_MER0      999
#define R8A78000_CLK_ZGD1_GPC_MER1      1000
#define R8A78000_CLK_ZGD2_GPC_MER1      1001
#define R8A78000_CLK_ZGD4_GPC_MER1      1002
#define R8A78000_CLK_ZGD1_GPC_MER2      1003
#define R8A78000_CLK_ZGD2_GPC_MER2      1004
#define R8A78000_CLK_ZGD4_GPC_MER2      1005
#define R8A78000_CLK_ZGD1_GPC_MER3      1006
#define R8A78000_CLK_ZGD2_GPC_MER3      1007
#define R8A78000_CLK_ZGD4_GPC_MER3      1008
#define R8A78000_CLK_ZGD1_GPC_MER4      1009
#define R8A78000_CLK_ZGD2_GPC_MER4      1010
#define R8A78000_CLK_ZGD4_GPC_MER4      1011
#define R8A78000_CLK_ZGD1_GPC_MER5      1012
#define R8A78000_CLK_ZGD2_GPC_MER5      1013
#define R8A78000_CLK_ZGD4_GPC_MER5      1014
#define R8A78000_CLK_ZGD1_GPC_MER6      1015
#define R8A78000_CLK_ZGD2_GPC_MER6      1016
#define R8A78000_CLK_ZGD4_GPC_MER6      1017
#define R8A78000_CLK_ZGD1_GPC_MER7      1018
#define R8A78000_CLK_ZGD2_GPC_MER7      1019
#define R8A78000_CLK_ZGD4_GPC_MER7      1020
#define R8A78000_CLK_ZGD1_GPC_TEXAS0    1021
#define R8A78000_CLK_ZGD2_GPC_TEXAS0    1022
#define R8A78000_CLK_ZGD4_GPC_TEXAS0    1023
#define R8A78000_CLK_ZGD1_GPC_TEXAS1    1024
#define R8A78000_CLK_ZGD2_GPC_TEXAS1    1025
#define R8A78000_CLK_ZGD4_GPC_TEXAS1    1026
#define R8A78000_CLK_ZGD1_GPC_TEXAS2    1027
#define R8A78000_CLK_ZGD2_GPC_TEXAS2    1028
#define R8A78000_CLK_ZGD4_GPC_TEXAS2    1029
#define R8A78000_CLK_ZGD1_GPC_TEXAS3    1030
#define R8A78000_CLK_ZGD2_GPC_TEXAS3    1031
#define R8A78000_CLK_ZGD4_GPC_TEXAS3    1032
#define R8A78000_CLK_ZGD1_GPC_SWIFT0    1033
#define R8A78000_CLK_ZGD2_GPC_SWIFT0    1034
#define R8A78000_CLK_ZGD4_GPC_SWIFT0    1035
#define R8A78000_CLK_ZGD1_GPC_SWIFT1    1036
#define R8A78000_CLK_ZGD2_GPC_SWIFT1    1037
#define R8A78000_CLK_ZGD4_GPC_SWIFT1    1038
#define R8A78000_CLK_ZGD1_GPC_SWIFT2    1039
#define R8A78000_CLK_ZGD2_GPC_SWIFT2    1040
#define R8A78000_CLK_ZGD4_GPC_SWIFT2    1041
#define R8A78000_CLK_ZGD1_GPC_SWIFT3    1042
#define R8A78000_CLK_ZGD2_GPC_SWIFT3    1043
#define R8A78000_CLK_ZGD4_GPC_SWIFT3    1044
#define R8A78000_CLK_ZGD1_GPC_SWIFT4    1045
#define R8A78000_CLK_ZGD2_GPC_SWIFT4    1046
#define R8A78000_CLK_ZGD4_GPC_SWIFT4    1047
#define R8A78000_CLK_ZGD1_GPC_SWIFT5    1048
#define R8A78000_CLK_ZGD2_GPC_SWIFT5    1049
#define R8A78000_CLK_ZGD4_GPC_SWIFT5    1050
#define R8A78000_CLK_ZGD1_GPC_SWIFT6    1051
#define R8A78000_CLK_ZGD2_GPC_SWIFT6    1052
#define R8A78000_CLK_ZGD4_GPC_SWIFT6    1053
#define R8A78000_CLK_ZGD1_GPC_SWIFT7    1054
#define R8A78000_CLK_ZGD2_GPC_SWIFT7    1055
#define R8A78000_CLK_ZGD4_GPC_SWIFT7    1056
#define R8A78000_CLK_SGD1_DSP_OTHER     1057
#define R8A78000_CLK_SGD2_DSP_OTHER     1058
#define R8A78000_CLK_SGD4_DSP_OTHER     1059
#define R8A78000_CLK_ZT_DSP_OTHER       1060
#define R8A78000_CLK_SGD1_DSP_BUS0      1061
#define R8A78000_CLK_SGD2_DSP_BUS0      1062
#define R8A78000_CLK_SGD4_DSP_BUS0      1063
#define R8A78000_CLK_ZT_DSP_BUS0        1064
#define R8A78000_CLK_SGD1_DSP_BUS1      1065
#define R8A78000_CLK_SGD2_DSP_BUS1      1066
#define R8A78000_CLK_SGD4_DSP_BUS1      1067
#define R8A78000_CLK_ZT_DSP_BUS1        1068
#define R8A78000_CLK_SGD1_DSP2_VPX0     1069
#define R8A78000_CLK_SGD2_DSP2_VPX0     1070
#define R8A78000_CLK_SGD4_DSP2_VPX0     1071
#define R8A78000_CLK_ZT_DSP2_VPX0       1072
#define R8A78000_CLK_WDT_DSP2_VPX0      1073
#define R8A78000_CLK_SGD1_DSP2_VPX1     1074
#define R8A78000_CLK_SGD2_DSP2_VPX1     1075
#define R8A78000_CLK_SGD4_DSP2_VPX1     1076
#define R8A78000_CLK_ZT_DSP2_VPX1       1077
#define R8A78000_CLK_WDT_DSP2_VPX1      1078
#define R8A78000_CLK_SGD1_DSP2_VPX2     1079
#define R8A78000_CLK_SGD2_DSP2_VPX2     1080
#define R8A78000_CLK_SGD4_DSP2_VPX2     1081
#define R8A78000_CLK_ZT_DSP2_VPX2       1082
#define R8A78000_CLK_WDT_DSP2_VPX2      1083
#define R8A78000_CLK_SGD1_DSP2_VPX3     1084
#define R8A78000_CLK_SGD2_DSP2_VPX3     1085
#define R8A78000_CLK_SGD4_DSP2_VPX3     1086
#define R8A78000_CLK_ZT_DSP2_VPX3       1087
#define R8A78000_CLK_WDT_DSP2_VPX3      1088
#define R8A78000_CLK_SGD1_DSP3_VPX0     1089
#define R8A78000_CLK_SGD2_DSP3_VPX0     1090
#define R8A78000_CLK_SGD4_DSP3_VPX0     1091
#define R8A78000_CLK_ZT_DSP3_VPX0       1092
#define R8A78000_CLK_WDT_DSP3_VPX0      1093
#define R8A78000_CLK_SGD1_DSP3_VPX1     1094
#define R8A78000_CLK_SGD2_DSP3_VPX1     1095
#define R8A78000_CLK_SGD4_DSP3_VPX1     1096
#define R8A78000_CLK_ZT_DSP3_VPX1       1097
#define R8A78000_CLK_WDT_DSP3_VPX1      1098
#define R8A78000_CLK_SGD1_DSP3_VPX2     1099
#define R8A78000_CLK_SGD2_DSP3_VPX2     1100
#define R8A78000_CLK_SGD4_DSP3_VPX2     1101
#define R8A78000_CLK_ZT_DSP3_VPX2       1102
#define R8A78000_CLK_WDT_DSP3_VPX2      1103
#define R8A78000_CLK_SGD1_DSP3_VPX3     1104
#define R8A78000_CLK_SGD2_DSP3_VPX3     1105
#define R8A78000_CLK_SGD4_DSP3_VPX3     1106
#define R8A78000_CLK_ZT_DSP3_VPX3       1107
#define R8A78000_CLK_WDT_DSP3_VPX3      1108
#define R8A78000_CLK_SGD1_DSP4_VPX0     1109
#define R8A78000_CLK_SGD2_DSP4_VPX0     1110
#define R8A78000_CLK_SGD4_DSP4_VPX0     1111
#define R8A78000_CLK_ZT_DSP4_VPX0       1112
#define R8A78000_CLK_WDT_DSP4_VPX0      1113
#define R8A78000_CLK_SGD1_DSP4_VPX1     1114
#define R8A78000_CLK_SGD2_DSP4_VPX1     1115
#define R8A78000_CLK_SGD4_DSP4_VPX1     1116
#define R8A78000_CLK_ZT_DSP4_VPX1       1117
#define R8A78000_CLK_WDT_DSP4_VPX1      1118
#define R8A78000_CLK_SGD1_DSP4_VPX2     1119
#define R8A78000_CLK_SGD2_DSP4_VPX2     1120
#define R8A78000_CLK_SGD4_DSP4_VPX2     1121
#define R8A78000_CLK_ZT_DSP4_VPX2       1122
#define R8A78000_CLK_WDT_DSP4_VPX2      1123
#define R8A78000_CLK_SGD1_DSP4_VPX3     1124
#define R8A78000_CLK_SGD2_DSP4_VPX3     1125
#define R8A78000_CLK_SGD4_DSP4_VPX3     1126
#define R8A78000_CLK_ZT_DSP4_VPX3       1127
#define R8A78000_CLK_WDT_DSP4_VPX3      1128
#define R8A78000_CLK_SGD1_DSP5_VPX0     1129
#define R8A78000_CLK_SGD2_DSP5_VPX0     1130
#define R8A78000_CLK_SGD4_DSP5_VPX0     1131
#define R8A78000_CLK_ZT_DSP5_VPX0       1132
#define R8A78000_CLK_WDT_DSP5_VPX0      1133
#define R8A78000_CLK_SGD1_DSP5_VPX1     1134
#define R8A78000_CLK_SGD2_DSP5_VPX1     1135
#define R8A78000_CLK_SGD4_DSP5_VPX1     1136
#define R8A78000_CLK_ZT_DSP5_VPX1       1137
#define R8A78000_CLK_WDT_DSP5_VPX1      1138
#define R8A78000_CLK_SGD1_DSP5_VPX2     1139
#define R8A78000_CLK_SGD2_DSP5_VPX2     1140
#define R8A78000_CLK_SGD4_DSP5_VPX2     1141
#define R8A78000_CLK_ZT_DSP5_VPX2       1142
#define R8A78000_CLK_WDT_DSP5_VPX2      1143
#define R8A78000_CLK_SGD1_DSP5_VPX3     1144
#define R8A78000_CLK_SGD2_DSP5_VPX3     1145
#define R8A78000_CLK_SGD4_DSP5_VPX3     1146
#define R8A78000_CLK_ZT_DSP5_VPX3       1147
#define R8A78000_CLK_WDT_DSP5_VPX3      1148
#define R8A78000_CLK_SGD1_DSP6_VPX0     1149
#define R8A78000_CLK_SGD2_DSP6_VPX0     1150
#define R8A78000_CLK_SGD4_DSP6_VPX0     1151
#define R8A78000_CLK_ZT_DSP6_VPX0       1152
#define R8A78000_CLK_WDT_DSP6_VPX0      1153
#define R8A78000_CLK_SGD1_DSP6_VPX1     1154
#define R8A78000_CLK_SGD2_DSP6_VPX1     1155
#define R8A78000_CLK_SGD4_DSP6_VPX1     1156
#define R8A78000_CLK_ZT_DSP6_VPX1       1157
#define R8A78000_CLK_WDT_DSP6_VPX1      1158
#define R8A78000_CLK_SGD1_DSP6_VPX2     1159
#define R8A78000_CLK_SGD2_DSP6_VPX2     1160
#define R8A78000_CLK_SGD4_DSP6_VPX2     1161
#define R8A78000_CLK_ZT_DSP6_VPX2       1162
#define R8A78000_CLK_WDT_DSP6_VPX2      1163
#define R8A78000_CLK_SGD1_DSP6_VPX3     1164
#define R8A78000_CLK_SGD2_DSP6_VPX3     1165
#define R8A78000_CLK_SGD4_DSP6_VPX3     1166
#define R8A78000_CLK_ZT_DSP6_VPX3       1167
#define R8A78000_CLK_WDT_DSP6_VPX3      1168
#define R8A78000_CLK_SGD1_DSP2_VPXL2    1169
#define R8A78000_CLK_SGD2_DSP2_VPXL2    1170
#define R8A78000_CLK_SGD4_DSP2_VPXL2    1171
#define R8A78000_CLK_ZT_DSP2_VPXL2      1172
#define R8A78000_CLK_WDT_DSP_VPXL2      1173
#define R8A78000_CLK_SGD1_DSP3_VPXL2    1174
#define R8A78000_CLK_SGD2_DSP3_VPXL2    1175
#define R8A78000_CLK_SGD4_DSP3_VPXL2    1176
#define R8A78000_CLK_ZT_DSP3_VPXL2      1177
#define R8A78000_CLK_WDT_DSP3_VPXL2     1178
#define R8A78000_CLK_SGD1_DSP4_VPXL2    1179
#define R8A78000_CLK_SGD2_DSP4_VPXL2    1180
#define R8A78000_CLK_SGD4_DSP4_VPXL2    1181
#define R8A78000_CLK_ZT_DSP4_VPXL2      1182
#define R8A78000_CLK_WDT_DSP4_VPXL2     1183
#define R8A78000_CLK_SGD1_DSP5_VPXL2    1184
#define R8A78000_CLK_SGD2_DSP5_VPXL2    1185
#define R8A78000_CLK_SGD4_DSP5_VPXL2    1186
#define R8A78000_CLK_ZT_DSP5_VPXL2      1187
#define R8A78000_CLK_WDT_DSP5_VPXL2     1188
#define R8A78000_CLK_SGD1_DSP6_VPXL2    1189
#define R8A78000_CLK_SGD2_DSP6_VPXL2    1190
#define R8A78000_CLK_SGD4_DSP6_VPXL2    1191
#define R8A78000_CLK_ZT_DSP6_VPXL2      1192
#define R8A78000_CLK_WDT_DSP6_VPXL2     1193
#define R8A78000_CLK_SGD1_NPU0_OTHER    1194
#define R8A78000_CLK_SGD2_NPU0_OTHER    1195
#define R8A78000_CLK_SGD4_NPU0_OTHER    1196
#define R8A78000_CLK_ZT_NPU0_OTHER      1197
#define R8A78000_CLK_SGD1_NPU0_NPUL2    1198
#define R8A78000_CLK_SGD2_NPU0_NPUL2    1199
#define R8A78000_CLK_SGD4_NPU0_NPUL2    1200
#define R8A78000_CLK_ZT_NPU0_NPU_L2     1201
#define R8A78000_CLK_WDT_NPU0_NPUL2     1202
#define R8A78000_CLK_SGD1_NPU0_VPXL2    1203
#define R8A78000_CLK_SGD2_NPU0_VPXL2    1204
#define R8A78000_CLK_SGD4_NPU0_VPXL2    1205
#define R8A78000_CLK_ZT_NPU0_VPX_L2     1206
#define R8A78000_CLK_WDT_NPU0_VPX_L2    1207
#define R8A78000_CLK_SGD1_N0_GRP0_C0    1208
#define R8A78000_CLK_SGD2_N0_GRP0_C0    1209
#define R8A78000_CLK_SGD4_N0_GRP0_C0    1210
#define R8A78000_CLK_ZT_N0_GRP0_C0      1211
#define R8A78000_CLK_WDT_N0_GRP0_C0     1212
#define R8A78000_CLK_SGD1_N0_GRP0_C1    1213
#define R8A78000_CLK_SGD2_N0_GRP0_C1    1214
#define R8A78000_CLK_SGD4_N0_GRP0_C1    1215
#define R8A78000_CLK_ZT_N0_GRP0_C1      1216
#define R8A78000_CLK_WDT_N0_GRP0_C1     1217
#define R8A78000_CLK_SGD1_N0_GRP0_C2    1218
#define R8A78000_CLK_SGD2_N0_GRP0_C2    1219
#define R8A78000_CLK_SGD4_N0_GRP0_C2    1220
#define R8A78000_CLK_ZT_N0_GRP0_C2      1221
#define R8A78000_CLK_WDT_N0_C02         1222
#define R8A78000_CLK_SGD1_N0_GRP1_C0    1223
#define R8A78000_CLK_SGD2_N0_GRP1_C0    1224
#define R8A78000_CLK_SGD4_N0_GRP1_C0    1225
#define R8A78000_CLK_ZT_N0_GRP1_C0      1226
#define R8A78000_CLK_WDT_N0_GRP1_C0     1227
#define R8A78000_CLK_SGD1_N0_GRP1_C1    1228
#define R8A78000_CLK_SGD2_N0_GRP1_C1    1229
#define R8A78000_CLK_SGD4_N0_GRP1_C1    1230
#define R8A78000_CLK_ZT_N0_GRP1_C1      1231
#define R8A78000_CLK_WDT_N0_GRP1_C1     1232
#define R8A78000_CLK_SGD1_N0_GRP1_C2    1233
#define R8A78000_CLK_SGD2_N0_GRP1_C2    1234
#define R8A78000_CLK_SGD4_N0_GRP1_C2    1235
#define R8A78000_CLK_ZT_N0_GRP1_C2      1236
#define R8A78000_CLK_WDT_N0_GRP1_C2     1237
#define R8A78000_CLK_SGD1_N0_GRP2_C0    1238
#define R8A78000_CLK_SGD2_N0_GRP2_C0    1239
#define R8A78000_CLK_SGD4_N0_GRP2_C0    1240
#define R8A78000_CLK_ZT_N0_GRP2_C0      1241
#define R8A78000_CLK_WDT_N0_GRP2_C0     1242
#define R8A78000_CLK_SGD1_N0_GRP2_C1    1243
#define R8A78000_CLK_SGD2_N0_GRP2_C1    1244
#define R8A78000_CLK_SGD4_N0_GRP2_C1    1245
#define R8A78000_CLK_ZT_N0_GRP2_C1      1246
#define R8A78000_CLK_WDT_N0_GRP2_C1     1247
#define R8A78000_CLK_SGD1_N0_GRP2_C2    1248
#define R8A78000_CLK_SGD2_N0_GRP2_C2    1249
#define R8A78000_CLK_SGD4_N0_GRP2_C2    1250
#define R8A78000_CLK_ZT_N0_GRP2_C2      1251
#define R8A78000_CLK_WDT_N0_GRP2_C2     1252
#define R8A78000_CLK_SGD1_N0_GRP3_C0    1253
#define R8A78000_CLK_SGD2_N0_GRP3_C0    1254
#define R8A78000_CLK_SGD4_N0_GRP3_C0    1255
#define R8A78000_CLK_ZT_N0_GRP3_C0      1256
#define R8A78000_CLK_WDT_N0_GRP3_C0     1257
#define R8A78000_CLK_SGD1_N0_GRP3_C1    1258
#define R8A78000_CLK_SGD2_N0_GRP3_C1    1259
#define R8A78000_CLK_SGD4_N0_GRP3_C1    1260
#define R8A78000_CLK_ZT_N0_GRP3_C1      1261
#define R8A78000_CLK_WDT_N0_GRP3_C1     1262
#define R8A78000_CLK_SGD1_N0_GRP3_C2    1263
#define R8A78000_CLK_SGD2_N0_GRP3_C2    1264
#define R8A78000_CLK_SGD4_N0_GRP3_C2    1265
#define R8A78000_CLK_ZT_N0_GRP3_C2      1266
#define R8A78000_CLK_WDT_N0_GRP3_C2     1267
#define R8A78000_CLK_SGD1_N0_VPX_C0     1268
#define R8A78000_CLK_SGD2_N0_VPX_C0     1269
#define R8A78000_CLK_SGD4_N0_VPX_C0     1270
#define R8A78000_CLK_ZT_N0_VPX_C0       1271
#define R8A78000_CLK_WDT_N0_VPX_C0      1272
#define R8A78000_CLK_SGD1_N0_VPX_C1     1273
#define R8A78000_CLK_SGD2_N0_VPX_C1     1274
#define R8A78000_CLK_SGD4_N0_VPX_C1     1275
#define R8A78000_CLK_ZT_N0_VPX_C1       1276
#define R8A78000_CLK_WDT_N0_VPX_C1      1277
#define R8A78000_CLK_SGD1_N0_VPX_C2     1278
#define R8A78000_CLK_SGD2_N0_VPX_C2     1279
#define R8A78000_CLK_SGD4_N0_VPX_C2     1280
#define R8A78000_CLK_ZT_N0_VPX_C2       1281
#define R8A78000_CLK_WDT_N0_VPX_C2      1282
#define R8A78000_CLK_SGD1_N0_VPX_C3     1283
#define R8A78000_CLK_SGD2_N0_VPX_C3     1284
#define R8A78000_CLK_SGD4_N0_VPX_C3     1285
#define R8A78000_CLK_ZT_N0_VPX_C3       1286
#define R8A78000_CLK_WDT_N0_VPX_C3      1287
#define R8A78000_CLK_SGD1_NPU1_OTHER    1288
#define R8A78000_CLK_SGD2_NPU1_OTHER    1289
#define R8A78000_CLK_SGD4_NPU1_OTHER    1290
#define R8A78000_CLK_ZT_NPU1_OTHER      1291
#define R8A78000_CLK_SGD1_NPU1_NPUL2    1292
#define R8A78000_CLK_SGD2_NPU1_NPUL2    1293
#define R8A78000_CLK_SGD4_NPU1_NPUL2    1294
#define R8A78000_CLK_ZT_NPU1_NPU_L2     1295
#define R8A78000_CLK_WDT_NPU1_NPUL2     1296
#define R8A78000_CLK_SGD1_NPU1_VPXL2    1297
#define R8A78000_CLK_SGD2_NPU1_VPXL2    1298
#define R8A78000_CLK_SGD4_NPU1_VPXL2    1299
#define R8A78000_CLK_ZT_NPU1_VPX_L2     1300
#define R8A78000_CLK_WDT_N1_VPX_L2      1301
#define R8A78000_CLK_SGD1_N1_GRP0_C0    1302
#define R8A78000_CLK_SGD2_N1_GRP0_C0    1303
#define R8A78000_CLK_SGD4_N1_GRP0_C0    1304
#define R8A78000_CLK_ZT_N1_GRP0_C0      1305
#define R8A78000_CLK_WDT_N1_GRP0_C0     1306
#define R8A78000_CLK_SGD1_N1_GRP0_C1    1307
#define R8A78000_CLK_SGD2_N1_GRP0_C1    1308
#define R8A78000_CLK_SGD4_N1_GRP0_C1    1309
#define R8A78000_CLK_ZT_N1_GRP0_C1      1310
#define R8A78000_CLK_WDT_N1_GRP0_C1     1311
#define R8A78000_CLK_SGD1_N1_GRP0_C2    1312
#define R8A78000_CLK_SGD2_N1_GRP0_C2    1313
#define R8A78000_CLK_SGD4_N1_GRP0_C2    1314
#define R8A78000_CLK_ZT_N1_GRP0_C2      1315
#define R8A78000_CLK_WDT_N1_C02         1316
#define R8A78000_CLK_SGD1_N1_GRP1_C0    1317
#define R8A78000_CLK_SGD2_N1_GRP1_C0    1318
#define R8A78000_CLK_SGD4_N1_GRP1_C0    1319
#define R8A78000_CLK_ZT_N1_GRP1_C0      1320
#define R8A78000_CLK_WDT_N1_GRP1_C0     1321
#define R8A78000_CLK_SGD1_N1_GRP1_C1    1322
#define R8A78000_CLK_SGD2_N1_GRP1_C1    1323
#define R8A78000_CLK_SGD4_N1_GRP1_C1    1324
#define R8A78000_CLK_ZT_N1_GRP1_C1      1325
#define R8A78000_CLK_WDT_N1_GRP1_C1     1326
#define R8A78000_CLK_SGD1_N1_GRP1_C2    1327
#define R8A78000_CLK_SGD2_N1_GRP1_C2    1328
#define R8A78000_CLK_SGD4_N1_GRP1_C2    1329
#define R8A78000_CLK_ZT_N1_GRP1_C2      1330
#define R8A78000_CLK_WDT_N1_GRP1_C2     1331
#define R8A78000_CLK_SGD1_N1_GRP2_C0    1332
#define R8A78000_CLK_SGD2_N1_GRP2_C0    1333
#define R8A78000_CLK_SGD4_N1_GRP2_C0    1334
#define R8A78000_CLK_ZT_N1_GRP2_C0      1335
#define R8A78000_CLK_WDT_N1_GRP2_C0     1336
#define R8A78000_CLK_SGD1_N1_GRP2_C1    1337
#define R8A78000_CLK_SGD2_N1_GRP2_C1    1338
#define R8A78000_CLK_SGD4_N1_GRP2_C1    1339
#define R8A78000_CLK_ZT_N1_GRP2_C1      1340
#define R8A78000_CLK_WDT_N1_GRP2_C1     1341
#define R8A78000_CLK_SGD1_N1_GRP2_C2    1342
#define R8A78000_CLK_SGD2_N1_GRP2_C2    1343
#define R8A78000_CLK_SGD4_N1_GRP2_C2    1344
#define R8A78000_CLK_ZT_N1_GRP2_C2      1345
#define R8A78000_CLK_WDT_N1_GRP2_C2     1346
#define R8A78000_CLK_SGD1_N1_GRP3_C0    1347
#define R8A78000_CLK_SGD2_N1_GRP3_C0    1348
#define R8A78000_CLK_SGD4_N1_GRP3_C0    1349
#define R8A78000_CLK_ZT_N1_GRP3_C0      1350
#define R8A78000_CLK_WDT_N1_GRP3_C0     1351
#define R8A78000_CLK_SGD1_N1_GRP3_C1    1352
#define R8A78000_CLK_SGD2_N1_GRP3_C1    1353
#define R8A78000_CLK_SGD4_N1_GRP3_C1    1354
#define R8A78000_CLK_ZT_N1_GRP3_C1      1355
#define R8A78000_CLK_WDT_N1_GRP3_C1     1356
#define R8A78000_CLK_SGD1_N1_GRP3_C2    1357
#define R8A78000_CLK_SGD2_N1_GRP3_C2    1358
#define R8A78000_CLK_SGD4_N1_GRP3_C2    1359
#define R8A78000_CLK_ZT_N1_GRP3_C2      1360
#define R8A78000_CLK_WDT_N1_GRP3_C2     1361
#define R8A78000_CLK_SGD1_N1_VPX_C0     1362
#define R8A78000_CLK_SGD2_N1_VPX_C0     1363
#define R8A78000_CLK_SGD4_N1_VPX_C0     1364
#define R8A78000_CLK_ZT_N1_VPX_C0       1365
#define R8A78000_CLK_WDT_N1_VPX_C0      1366
#define R8A78000_CLK_SGD1_N1_VPX_C1     1367
#define R8A78000_CLK_SGD2_N1_VPX_C1     1368
#define R8A78000_CLK_SGD4_N1_VPX_C1     1369
#define R8A78000_CLK_ZT_N1_VPX_C1       1370
#define R8A78000_CLK_WDT_N1_VPX_C1      1371
#define R8A78000_CLK_SGD1_N1_VPX_C2     1372
#define R8A78000_CLK_SGD2_N1_VPX_C2     1373
#define R8A78000_CLK_SGD4_N1_VPX_C2     1374
#define R8A78000_CLK_ZT_N1_VPX_C2       1375
#define R8A78000_CLK_WDT_N1_VPX_C2      1376
#define R8A78000_CLK_SGD1_N1_VPX_C3     1377
#define R8A78000_CLK_SGD2_N1_VPX_C3     1378
#define R8A78000_CLK_SGD4_N1_VPX_C3     1379
#define R8A78000_CLK_ZT_N1_VPX_C3       1380
#define R8A78000_CLK_WDT_N1_VPX_C3      1381
#define R8A78000_CLK_ZRD6_RT_MAIN       1382
#define R8A78000_CLK_ZRD12_RT_MAIN      1383
#define R8A78000_CLK_ZRD24_RT_MAIN      1384
#define R8A78000_CLK_ZRD48_RT_MAIN      1385
#define R8A78000_CLK_ZRD96_RT_MAIN      1386
#define R8A78000_CLK_ZT_RT_MAIN         1387
#define R8A78000_CLK_ZTR_RT_MAIN        1388
#define R8A78000_CLK_CL16M_RT_MAIN      1389
#define R8A78000_CLK_SAD1_RT_MAIN       1390
#define R8A78000_CLK_SAD2_RT_MAIN       1391
#define R8A78000_CLK_SAD4_RT_MAIN       1392
#define R8A78000_CLK_ZRD6_RT_DMAC       1393
#define R8A78000_CLK_ZRD12_RT_DMAC      1394
#define R8A78000_CLK_ZRD24_RT_DMAC      1395
#define R8A78000_CLK_ZRD48_RT_DMAC      1396
#define R8A78000_CLK_ZRD96_RT_DMAC      1397
#define R8A78000_CLK_ZT_RT_DMAC         1398
#define R8A78000_CLK_ZTR_RT_DMAC        1399
#define R8A78000_CLK_CL16M_RT_DMAC      1400
#define R8A78000_CLK_ZRD6_RT_CR52SS0    1401
#define R8A78000_CLK_ZRD12_RT_SS0       1402
#define R8A78000_CLK_ZRD24_RT_SS0       1403
#define R8A78000_CLK_ZRD48_RT_SS0       1404
#define R8A78000_CLK_ZRD96_RT_SS0       1405
#define R8A78000_CLK_ZT_RT_CR52SS0      1406
#define R8A78000_CLK_ZTR_RT_CR52SS0     1407
#define R8A78000_CLK_ZR_RT_CR52SS0      1408
#define R8A78000_CLK_ZRD6_RT_CR52SS1    1409
#define R8A78000_CLK_ZRD12_RT_SS1       1410
#define R8A78000_CLK_ZRD24_RT_SS1       1411
#define R8A78000_CLK_ZRD48_RT_SS1       1412
#define R8A78000_CLK_ZRD96_RT_SS1       1413
#define R8A78000_CLK_ZT_RT_CR52SS1      1414
#define R8A78000_CLK_ZTR_RT_CR52SS1     1415
#define R8A78000_CLK_ZR_RT_CR52SS1      1416
#define R8A78000_CLK_ZRD6_RT_CR52SS2    1417
#define R8A78000_CLK_ZRD12_RT_SS2       1418
#define R8A78000_CLK_ZRD24_RT_SS2       1419
#define R8A78000_CLK_ZRD48_RT_SS2       1420
#define R8A78000_CLK_ZRD96_RT_SS2       1421
#define R8A78000_CLK_ZT_RT_CR52SS2      1422
#define R8A78000_CLK_ZTR_RT_CR52SS2     1423
#define R8A78000_CLK_ZR_RT_CR52SS2      1424
#define R8A78000_CLK_ZR_RT_C00          1425
#define R8A78000_CLK_ZR_RT_C01          1426
#define R8A78000_CLK_ZR_RT_C10          1427
#define R8A78000_CLK_ZR_RT_C11          1428
#define R8A78000_CLK_ZR_RT_C20          1429
#define R8A78000_CLK_ZR_RT_C21          1430
#define R8A78000_CLK_ZR_RT_SHADOW00     1431
#define R8A78000_CLK_ZR_RT_SHADOW01     1432
#define R8A78000_CLK_ZR_RT_SHADOW10     1433
#define R8A78000_CLK_ZR_RT_SHADOW11     1434
#define R8A78000_CLK_ZR_RT_SHADOW20     1435
#define R8A78000_CLK_ZR_RT_SHADOW21     1436
#define R8A78000_CLK_ZRD6_RT_SEC        1437
#define R8A78000_CLK_ZRD12_RT_SEC       1438
#define R8A78000_CLK_ZRD24_RT_SEC       1439
#define R8A78000_CLK_ZRD48_RT_SEC       1440
#define R8A78000_CLK_ZRD96_RT_SEC       1441
#define R8A78000_CLK_ZRD6_RT_MEM        1442
#define R8A78000_CLK_ZRD12_RT_MEM       1443
#define R8A78000_CLK_ZRD24_RT_MEM       1444
#define R8A78000_CLK_ZRD48_RT_MEM       1445
#define R8A78000_CLK_ZRD96_RT_MEM       1446
#define R8A78000_CLK_ZT_RT_MEM          1447
#define R8A78000_CLK_ZTR_RT_MEM         1448
#define R8A78000_CLK_BUSD1_SCP_MAIN     1449
#define R8A78000_CLK_BUSD2_SCP_MAIN     1450
#define R8A78000_CLK_BUSD4_SCP_MAIN     1451
#define R8A78000_CLK_BUSD6_SCP_MAIN     1452
#define R8A78000_CLK_BUSD8_SCP_MAIN     1453
#define R8A78000_CLK_BUSD16_SCP_MAIN    1454
#define R8A78000_CLK_BUSD32_SCP_MAIN    1455
#define R8A78000_CLK_CANFD_SCP_MAIN     1456
#define R8A78000_CLK_FRAY_SCP_MAIN      1457
#define R8A78000_CLK_LIN_SCP_MAIN       1458
#define R8A78000_CLK_MSO_SCP_MAIN       1459
#define R8A78000_CLK_CANXL_SCP_MAIN     1460
#define R8A78000_CLK_CL16M_SCP_MAIN     1461
#define R8A78000_CLK_ZT_SCP_MAIN        1462
#define R8A78000_CLK_SGD1_HSCS_OTHER    1463
#define R8A78000_CLK_SGD2_HSCS_OTHER    1464
#define R8A78000_CLK_SGD4_HSCS_OTHER    1465
#define R8A78000_CLK_SGD8_HSCS_OTHER    1466
#define R8A78000_CLK_SGD16_HSCS_OTH     1467
#define R8A78000_CLK_PCICK_HSCS_OTH     1468
#define R8A78000_CLK_SGD1_HSCS_PCI      1469
#define R8A78000_CLK_SGD2_HSCS_PCI      1470
#define R8A78000_CLK_SGD4_HSCS_PCI      1471
#define R8A78000_CLK_SGD8_HSCS_PCI      1472
#define R8A78000_CLK_SGD16_HSCS_PCI     1473
#define R8A78000_CLK_PCICK_HSCS_PC      1474
#define R8A78000_CLK_SGD1_HSCS_UCI0     1475
#define R8A78000_CLK_SGD12_HSCS_UCI0    1476
#define R8A78000_CLK_SGD24_HSCS_UCI0    1477
#define R8A78000_CLK_SGD48_HSCS_UCI0    1478
#define R8A78000_CLK_SGD96_HSCS_UCI0    1479
#define R8A78000_CLK_SB_HSCS_UCI0       1480
#define R8A78000_CLK_CD1_HSCS_UCI0      1481
#define R8A78000_CLK_CD2_HSCS_UCI0      1482
#define R8A78000_CLK_REF_HSCS_UCI0      1483
#define R8A78000_CLK_SGD1_HSCS_UCI1     1484
#define R8A78000_CLK_SGD12_HSCS_UCI1    1485
#define R8A78000_CLK_SGD24_HSCS_UCI1    1486
#define R8A78000_CLK_SGD48_HSCS_UCI1    1487
#define R8A78000_CLK_SGD96_HSCS_UCI1    1488
#define R8A78000_CLK_SB_HSCS_UCI1       1489
#define R8A78000_CLK_CD1_HSCS_UCI1      1490
#define R8A78000_CLK_CD2_HSCS_UCI1      1491
#define R8A78000_CLK_REF_HSCS_UCI1      1492
#define R8A78000_CLK_S0D1_HSCN_OTHER    1493
#define R8A78000_CLK_S0D2_HSCN_OTHER    1494
#define R8A78000_CLK_S0D4_HSCN_OTHER    1495
#define R8A78000_CLK_S0D8_HSCN_OTHER    1496
#define R8A78000_CLK_S0D12_HSCN_OTH     1497
#define R8A78000_CLK_S0D16_HSCN_OTH     1498
#define R8A78000_CLK_S0D24_HSCN_OTH     1499
#define R8A78000_CLK_ZT_HSCN_OTHER      1500
#define R8A78000_CLK_ZTR_HSCN_OTHER     1501
#define R8A78000_CLK_CL16M_HSCN_OTH     1502
#define R8A78000_CLK_S0D1_HSCN_PCI4     1503
#define R8A78000_CLK_S0D2_HSCN_PCI4     1504
#define R8A78000_CLK_S0D4_HSCN_PCI4     1505
#define R8A78000_CLK_S0D8_HSCN_PCI4     1506
#define R8A78000_CLK_S0D12_HSCN_PCI4    1507
#define R8A78000_CLK_S0D16_HSCN_PCI4    1508
#define R8A78000_CLK_S0D24_HSCN_PCI4    1509
#define R8A78000_CLK_ZT_HSCN_PCI4       1510
#define R8A78000_CLK_ZTR_HSCN_PCI4      1511
#define R8A78000_CLK_CL16M_HSCN_PCI4    1512
#define R8A78000_CLK_S0D1_HSCN_USB      1513
#define R8A78000_CLK_S0D2_HSCN_USB      1514
#define R8A78000_CLK_S0D4_HSCN_USB      1515
#define R8A78000_CLK_S0D8_HSCN_USB      1516
#define R8A78000_CLK_S0D12_HSCN_USB     1517
#define R8A78000_CLK_S0D16_HSCN_USB     1518
#define R8A78000_CLK_S0D24_HSCN_USB     1519
#define R8A78000_CLK_ZT_HSCN_USB        1520
#define R8A78000_CLK_ZTR_HSCN_USB       1521
#define R8A78000_CLK_CL16M_HSCN_USB     1522
#define R8A78000_CLK_S0D1_RSW3_MFWD     1523
#define R8A78000_CLK_S0D2_RSW3_MFWD     1524
#define R8A78000_CLK_S0D4_RSW3_MFWD     1525
#define R8A78000_CLK_S0D8_RSW3_MFWD     1526
#define R8A78000_CLK_S0D12_RSW3_MFWD    1527
#define R8A78000_CLK_S0D16_RSW3_MFWD    1528
#define R8A78000_CLK_S0D24_RSW3_MFWD    1529
#define R8A78000_CLK_SUBD1_RSW3_MFWD    1530
#define R8A78000_CLK_SUBD2_RSW3_MFWD    1531
#define R8A78000_CLK_CORE_RSW3_MFWD     1532
#define R8A78000_CLK_S0D1_RSW3_MAIN     1533
#define R8A78000_CLK_S0D2_RSW3_MAIN     1534
#define R8A78000_CLK_S0D4_RSW3_MAIN     1535
#define R8A78000_CLK_S0D8_RSW3_MAIN     1536
#define R8A78000_CLK_S0D12_RSW3_MAIN    1537
#define R8A78000_CLK_S0D16_RSW3_MAIN    1538
#define R8A78000_CLK_S0D24_RSW3_MAIN    1539
#define R8A78000_CLK_SUBD1_RSW3_MAIN    1540
#define R8A78000_CLK_SUBD2_RSW3_MAIN    1541
#define R8A78000_CLK_CORE_RSW3_MAIN     1542
#define R8A78000_CLK_S0D1_RSW3_AES      1543
#define R8A78000_CLK_S0D2_RSW3_AES      1544
#define R8A78000_CLK_S0D4_RSW3_AES      1545
#define R8A78000_CLK_S0D8_RSW3_AES      1546
#define R8A78000_CLK_S0D12_RSW3_AES     1547
#define R8A78000_CLK_S0D16_RSW3_AES     1548
#define R8A78000_CLK_S0D24_RSW3_AES     1549
#define R8A78000_CLK_SUBD1_RSW3_AES     1550
#define R8A78000_CLK_SUBD2_RSW3_AES     1551
#define R8A78000_CLK_CORE_RSW3_AES      1552
#define R8A78000_CLK_S0D1_RSW3_TSN      1553
#define R8A78000_CLK_S0D2_RSW3_TSN      1554
#define R8A78000_CLK_S0D4_RSW3_TSN      1555
#define R8A78000_CLK_S0D8_RSW3_TSN      1556
#define R8A78000_CLK_S0D12_RSW3_TSN     1557
#define R8A78000_CLK_S0D16_RSW3_TSN     1558
#define R8A78000_CLK_S0D24_RSW3_TSN     1559
#define R8A78000_CLK_SUBD1_RSW3_TSN     1560
#define R8A78000_CLK_SUBD2_RSW3_TSN     1561
#define R8A78000_CLK_CORE_RSW3_TSN      1562
#define R8A78000_CLK_S0D1_MM_BUS        1563
#define R8A78000_CLK_S0D2_MM_BUS        1564
#define R8A78000_CLK_S0D4_MM_BUS        1565
#define R8A78000_CLK_S0D1_MM_INIU       1566
#define R8A78000_CLK_S0D2_MM_INIU       1567
#define R8A78000_CLK_S0D4_MM_INIU       1568
#define R8A78000_CLK_S0D1_MM_AXCIDB     1569
#define R8A78000_CLK_S0D2_MM_AXCIDB     1570
#define R8A78000_CLK_S0D4_MM_AXCIDB     1571
#define R8A78000_CLK_S0D1_MM_TNIU0      1572
#define R8A78000_CLK_S0D2_MM_TNIU0      1573
#define R8A78000_CLK_S0D4_MM_TNIU0      1574
#define R8A78000_CLK_S0D1_MM_TNIU1      1575
#define R8A78000_CLK_S0D2_MM_TNIU1      1576
#define R8A78000_CLK_S0D4_MM_TNIU1      1577
#define R8A78000_CLK_S0D1_MM_OTHER      1578
#define R8A78000_CLK_S0D2_MM_OTHER      1579
#define R8A78000_CLK_S0D4_MM_OTHER      1580
#define R8A78000_CLK_S0D1_MM_DBSC0      1581
#define R8A78000_CLK_S0D2_MM_DBSC0      1582
#define R8A78000_CLK_S0D4_MM_DBSC0      1583
#define R8A78000_CLK_ZB3D1_MM_DBSC0     1584
#define R8A78000_CLK_S0D1_MM_DBSC1      1585
#define R8A78000_CLK_S0D2_MM_DBSC1      1586
#define R8A78000_CLK_S0D4_MM_DBSC1      1587
#define R8A78000_CLK_ZB3D1_MM_DBSC1     1588
#define R8A78000_CLK_S0D1_MM_DBSC2      1589
#define R8A78000_CLK_S0D2_MM_DBSC2      1590
#define R8A78000_CLK_S0D4_MM_DBSC2      1591
#define R8A78000_CLK_ZB3D1_MM_DBSC2     1592
#define R8A78000_CLK_S0D1_MM_DBSC3      1593
#define R8A78000_CLK_S0D2_MM_DBSC3      1594
#define R8A78000_CLK_S0D4_MM_DBSC3      1595
#define R8A78000_CLK_ZB3D1_MM_DBSC3     1596
#define R8A78000_CLK_S0D1_MM_DBSC4      1597
#define R8A78000_CLK_S0D2_MM_DBSC4      1598
#define R8A78000_CLK_S0D4_MM_DBSC4      1599
#define R8A78000_CLK_ZB3D1_MM_DBSC4     1600
#define R8A78000_CLK_S0D1_MM_DBSC5      1601
#define R8A78000_CLK_S0D2_MM_DBSC5      1602
#define R8A78000_CLK_S0D4_MM_DBSC5      1603
#define R8A78000_CLK_ZB3D1_MM_DBSC5     1604
#define R8A78000_CLK_S0D1_MM_DBSC6      1605
#define R8A78000_CLK_S0D2_MM_DBSC6      1606
#define R8A78000_CLK_S0D4_MM_DBSC6      1607
#define R8A78000_CLK_ZB3D1_MM_DBSC6     1608
#define R8A78000_CLK_S0D1_MM_DBSC7      1609
#define R8A78000_CLK_S0D2_MM_DBSC7      1610
#define R8A78000_CLK_S0D4_MM_DBSC7      1611
#define R8A78000_CLK_ZB3D1_MM_DBSC7     1612
#define R8A78000_CLK_S0D1_DDR0_MAIN     1613
#define R8A78000_CLK_S0D2_DDR0_MAIN     1614
#define R8A78000_CLK_S0D4_DDR0_MAIN     1615
#define R8A78000_CLK_ZB3D1_DDR0_MAIN    1616
#define R8A78000_CLK_S0D1_DDR1_MAIN     1617
#define R8A78000_CLK_S0D2_DDR1_MAIN     1618
#define R8A78000_CLK_S0D4_DDR1_MAIN     1619
#define R8A78000_CLK_ZB3D1_DDR1_MAIN    1620
#define R8A78000_CLK_S0D1_DDR2_MAIN     1621
#define R8A78000_CLK_S0D2_DDR2_MAIN     1622
#define R8A78000_CLK_S0D4_DDR2_MAIN     1623
#define R8A78000_CLK_ZB3D1_DDR2_MAIN    1624
#define R8A78000_CLK_S0D1_DDR3_MAIN     1625
#define R8A78000_CLK_S0D2_DDR3_MAIN     1626
#define R8A78000_CLK_S0D4_DDR3_MAIN     1627
#define R8A78000_CLK_ZB3D1_DDR3_MAIN    1628
#define R8A78000_CLK_S0D1_DDR4_MAIN     1629
#define R8A78000_CLK_S0D2_DDR4_MAIN     1630
#define R8A78000_CLK_S0D4_DDR4_MAIN     1631
#define R8A78000_CLK_ZB3D1_DDR4_MAIN    1632
#define R8A78000_CLK_S0D1_DDR5_MAIN     1633
#define R8A78000_CLK_S0D2_DDR5_MAIN     1634
#define R8A78000_CLK_S0D4_DDR5_MAIN     1635
#define R8A78000_CLK_ZB3D1_DDR5_MAIN    1636
#define R8A78000_CLK_S0D1_DDR6_MAIN     1637
#define R8A78000_CLK_S0D2_DDR6_MAIN     1638
#define R8A78000_CLK_S0D4_DDR6_MAIN     1639
#define R8A78000_CLK_ZB3D1_DDR6_MAIN    1640
#define R8A78000_CLK_S0D1_DDR7_MAIN     1641
#define R8A78000_CLK_S0D2_DDR7_MAIN     1642
#define R8A78000_CLK_S0D4_DDR7_MAIN     1643
#define R8A78000_CLK_ZB3D1_DDR7_MAIN    1644
#define R8A78000_CLK_SGD4_PERW_MAIN     1645
#define R8A78000_CLK_SGD8_PERW_MAIN     1646
#define R8A78000_CLK_SGD16_PERW_MAIN    1647
#define R8A78000_CLK_SGD32_PERW_MAIN    1648
#define R8A78000_CLK_SGAD4_PERW_M       1649
#define R8A78000_CLK_SGAD8_PERW_M       1650
#define R8A78000_CLK_SGAD16_PERW_M      1651
#define R8A78000_CLK_SGAD32_PERW_M      1652
#define R8A78000_CLK_S0AD8_PERW_M       1653
#define R8A78000_CLK_CL16M_PERW_MAIN    1654
#define R8A78000_CLK_MSOCK_PERW_MAIN    1655
#define R8A78000_CLK_SA_I3C_PERW_M      1656
#define R8A78000_CLK_SGD4_PERW_BUS      1657
#define R8A78000_CLK_SGD8_PERW_BUS      1658
#define R8A78000_CLK_SGD16_PERW_BUS     1659
#define R8A78000_CLK_SGD32_PERW_BUS     1660
#define R8A78000_CLK_SGAD4_PERW_BUS     1661
#define R8A78000_CLK_SGAD8_PERW_BUS     1662
#define R8A78000_CLK_SGAD16_PERW_BUS    1663
#define R8A78000_CLK_SGAD32_PERW_BUS    1664
#define R8A78000_CLK_S0AD8_PERW_BUS     1665
#define R8A78000_CLK_CL16M_PERW_BUS     1666
#define R8A78000_CLK_MSOCK_PERW_BUS     1667
#define R8A78000_CLK_SA_I3C_PERW_BUS    1668
#define R8A78000_CLK_SGD4_MP_MAIN       1669
#define R8A78000_CLK_SGD8_MP_MAIN       1670
#define R8A78000_CLK_SGD16_MP_MAIN      1671
#define R8A78000_CLK_SGD32_MP_MAIN      1672
#define R8A78000_CLK_CL16M_MP_MAIN      1673
#define R8A78000_CLK_ADGHD1_MP_MAIN     1674
#define R8A78000_CLK_ADGHD4_MP_MAIN     1675
#define R8A78000_CLK_SGD4_MP_BUS        1676
#define R8A78000_CLK_SGD8_MP_BUS        1677
#define R8A78000_CLK_SGD16_MP_BUS       1678
#define R8A78000_CLK_SGD32_MP_BUS       1679
#define R8A78000_CLK_CL16M_MP_BUS       1680
#define R8A78000_CLK_ADGHD1CK_MP_BUS    1681
#define R8A78000_CLK_ADGHD4CK_MP_BUS    1682
#define R8A78000_CLK_S0D1_PERE_MAIN     1683
#define R8A78000_CLK_S0D2_PERE_MAIN     1684
#define R8A78000_CLK_S0D3_PERE_MAIN     1685
#define R8A78000_CLK_S0D4_PERE_MAIN     1686
#define R8A78000_CLK_S0D6_PERE_MAIN     1687
#define R8A78000_CLK_S0D8_PERE_MAIN     1688
#define R8A78000_CLK_S0D12_PERE_MAIN    1689
#define R8A78000_CLK_S0D24_PERE_MAIN    1690
#define R8A78000_CLK_SD0H_PERE_MAIN     1691
#define R8A78000_CLK_SD0_PERE_MAIN      1692
#define R8A78000_CLK_RPCCK_PERE_MAIN    1693
#define R8A78000_CLK_RPCD2_PERE_MAIN    1694
#define R8A78000_CLK_CL16M_PERE_MAIN    1695
#define R8A78000_CLK_UFS_PERE_MAIN      1696


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A78000_CPG_MSSR_H_ */
```

## 155.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 BayLibre, SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 17 行

时钟标识符（Clock IDs）。

### 注释 3：原第 1718 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_R8A78000_CPG_MSSR_H_`。

## 155.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/r8a78000__cpg__mssr_8h.html)

---

[上一章](P154_r8a779g0_cpg_mssr.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P156_r8a78000_pd.h_源码浏览.md)
