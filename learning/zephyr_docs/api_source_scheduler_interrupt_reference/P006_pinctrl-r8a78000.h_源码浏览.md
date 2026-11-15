---
id: learning.zephyr-docs.api-source-scheduler-interrupt-reference.page-6
title: pinctrl-r8a78000.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a78000_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_pinctrl-r8a78000.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a78000_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P296_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a78000.h_文件参考.md)。

## 6.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
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
<a id="l00916"></a>
<a id="l00917"></a>
<a id="apinctrl-rcar-common_8h_html"></a>

```c
/*
 * Copyright (c) 2026 BayLibre, SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A78000_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A78000_H_


#include "pinctrl-rcar-common.h"


#define PIN_NONE -1

/* GP0 pins */
#define PIN_GP0_00       RCAR_GP_PIN(0, 0)
#define PIN_GP0_01       RCAR_GP_PIN(0, 1)
#define PIN_GP0_02       RCAR_GP_PIN(0, 2)
#define PIN_STPWT_EXTFXR RCAR_GP_PIN(0, 3)
#define PIN_FXR_CLKOUT1  RCAR_GP_PIN(0, 4)
#define PIN_FXR_CLKOUT2  RCAR_GP_PIN(0, 5)
#define PIN_CLK_EXTFXR   RCAR_GP_PIN(0, 6)
#define PIN_FXR_TXDA     RCAR_GP_PIN(0, 7)
#define PIN_FXR_TXENA    RCAR_GP_PIN(0, 8)
#define PIN_RXDA_EXTFXR  RCAR_GP_PIN(0, 9)
#define PIN_FXR_TXDB     RCAR_GP_PIN(0, 10)
#define PIN_FXR_TXENB    RCAR_GP_PIN(0, 11)
#define PIN_RXDB_EXTFXR  RCAR_GP_PIN(0, 12)
#define PIN_MSIOF0_SCK   RCAR_GP_PIN(0, 13)
#define PIN_MSIOF0_TXD   RCAR_GP_PIN(0, 14)
#define PIN_MSIOF0_RXD   RCAR_GP_PIN(0, 15)
#define PIN_MSIOF0_SYNC  RCAR_GP_PIN(0, 16)
#define PIN_MSIOF0_SS1   RCAR_GP_PIN(0, 17)
#define PIN_MSIOF0_SS2   RCAR_GP_PIN(0, 18)
#define PIN_MSIOF1_SCK   RCAR_GP_PIN(0, 19)
#define PIN_MSIOF1_TXD   RCAR_GP_PIN(0, 20)
#define PIN_MSIOF1_RXD   RCAR_GP_PIN(0, 21)
#define PIN_MSIOF1_SYNC  RCAR_GP_PIN(0, 22)
#define PIN_MSIOF1_SS1   RCAR_GP_PIN(0, 23)
#define PIN_MSIOF1_SS2   RCAR_GP_PIN(0, 24)
#define PIN_DP0_HOTPLUG  RCAR_GP_PIN(0, 25)
#define PIN_DP1_HOTPLUG  RCAR_GP_PIN(0, 26)
#define PIN_DP2_HOTPLUG  RCAR_GP_PIN(0, 27)

/* GP1 pins */
#define PIN_CAN0RX_INTP0    RCAR_GP_PIN(1, 0)
#define PIN_CAN0TX          RCAR_GP_PIN(1, 1)
#define PIN_CAN1RX_INTP1    RCAR_GP_PIN(1, 2)
#define PIN_CAN1TX          RCAR_GP_PIN(1, 3)
#define PIN_CAN2RX_INTP2    RCAR_GP_PIN(1, 4)
#define PIN_CAN2TX          RCAR_GP_PIN(1, 5)
#define PIN_CAN3RX_INTP3    RCAR_GP_PIN(1, 6)
#define PIN_CAN3TX          RCAR_GP_PIN(1, 7)
#define PIN_CAN4RX_INTP4    RCAR_GP_PIN(1, 8)
#define PIN_CAN4TX          RCAR_GP_PIN(1, 9)
#define PIN_CAN5RX_INTP5    RCAR_GP_PIN(1, 10)
#define PIN_CAN5TX          RCAR_GP_PIN(1, 11)
#define PIN_CAN6RX_INTP6    RCAR_GP_PIN(1, 12)
#define PIN_CAN6TX          RCAR_GP_PIN(1, 13)
#define PIN_RLIN30RX_INTP16 RCAR_GP_PIN(1, 14)
#define PIN_RLIN30TX        RCAR_GP_PIN(1, 15)
#define PIN_RLIN31RX_INTP17 RCAR_GP_PIN(1, 16)
#define PIN_RLIN31TX        RCAR_GP_PIN(1, 17)
#define PIN_RLIN32RX_INTP18 RCAR_GP_PIN(1, 18)
#define PIN_RLIN32TX        RCAR_GP_PIN(1, 19)
#define PIN_RLIN33RX_INTP19 RCAR_GP_PIN(1, 20)
#define PIN_RLIN33TX        RCAR_GP_PIN(1, 21)

/* GP2 pins */
#define PIN_RLIN34RX_INTP20 RCAR_GP_PIN(2, 0)
#define PIN_RLIN34TX        RCAR_GP_PIN(2, 1)
#define PIN_RLIN35RX_INTP21 RCAR_GP_PIN(2, 2)
#define PIN_RLIN35TX        RCAR_GP_PIN(2, 3)
#define PIN_RLIN36RX_INTP22 RCAR_GP_PIN(2, 4)
#define PIN_RLIN36TX        RCAR_GP_PIN(2, 5)
#define PIN_RLIN37RX_INTP23 RCAR_GP_PIN(2, 6)
#define PIN_RLIN37TX        RCAR_GP_PIN(2, 7)
#define PIN_CAN12RX_INTP12  RCAR_GP_PIN(2, 8)
#define PIN_CAN12TX         RCAR_GP_PIN(2, 9)
#define PIN_CAN13RX_INTP13  RCAR_GP_PIN(2, 10)
#define PIN_CAN13TX         RCAR_GP_PIN(2, 11)
#define PIN_CAN14RX_INTP14  RCAR_GP_PIN(2, 12)
#define PIN_CAN14TX         RCAR_GP_PIN(2, 13)
#define PIN_CAN15RX_INTP15  RCAR_GP_PIN(2, 14)
#define PIN_CAN15TX         RCAR_GP_PIN(2, 15)
#define PIN_CAN_CLK         RCAR_GP_PIN(2, 16)
#define PIN_INTP32          RCAR_GP_PIN(2, 17)
#define PIN_INTP33          RCAR_GP_PIN(2, 18)
#define PIN_SCL0            RCAR_GP_PIN(2, 19)
#define PIN_SDA0            RCAR_GP_PIN(2, 20)
#define PIN_AVS0            RCAR_GP_PIN(2, 21)
#define PIN_AVS1            RCAR_GP_PIN(2, 22)
#define PIN_EXTCLK0O        RCAR_GP_PIN(2, 23)
#define PIN_TAUD1O0         RCAR_GP_PIN(2, 24)
#define PIN_TAUD1O1         RCAR_GP_PIN(2, 25)
#define PIN_TAUD1O2         RCAR_GP_PIN(2, 26)
#define PIN_TAUD1O3         RCAR_GP_PIN(2, 27)
#define PIN_INTP34          RCAR_GP_PIN(2, 28)

/* GP3 pins */
#define PIN_QSPI0_SPCLK    RCAR_GP_PIN(3, 0)
#define PIN_QSPI0_MOSI_IO0 RCAR_GP_PIN(3, 1)
#define PIN_QSPI0_MISO_IO1 RCAR_GP_PIN(3, 2)
#define PIN_QSPI0_IO2      RCAR_GP_PIN(3, 3)
#define PIN_QSPI0_IO3      RCAR_GP_PIN(3, 4)
#define PIN_QSPI0_SSL      RCAR_GP_PIN(3, 5)
#define PIN_RPC_RESET      RCAR_GP_PIN(3, 6)
#define PIN_RPC_WP         RCAR_GP_PIN(3, 7)
#define PIN_RPC_INT        RCAR_GP_PIN(3, 8)
#define PIN_QSPI1_SPCLK    RCAR_GP_PIN(3, 9)
#define PIN_QSPI1_MOSI_IO0 RCAR_GP_PIN(3, 10)
#define PIN_QSPI1_MISO_IO1 RCAR_GP_PIN(3, 11)
#define PIN_QSPI1_IO2      RCAR_GP_PIN(3, 12)
#define PIN_QSPI1_IO3      RCAR_GP_PIN(3, 13)
#define PIN_QSPI1_SSL      RCAR_GP_PIN(3, 14)
#define PIN_ERROROUT       RCAR_GP_PIN(3, 15)
#define PIN_ERRORIN0       RCAR_GP_PIN(3, 16)

/* GP4 pins */
#define PIN_MMC0_SD_CLK   RCAR_GP_PIN(4, 0)
#define PIN_MMC0_SD_CMD   RCAR_GP_PIN(4, 1)
#define PIN_MMC0_SD_D0    RCAR_GP_PIN(4, 2)
#define PIN_MMC0_SD_D1    RCAR_GP_PIN(4, 3)
#define PIN_MMC0_SD_D2    RCAR_GP_PIN(4, 4)
#define PIN_MMC0_SD_D3    RCAR_GP_PIN(4, 5)
#define PIN_MMC0_D4       RCAR_GP_PIN(4, 6)
#define PIN_MMC0_D5       RCAR_GP_PIN(4, 7)
#define PIN_MMC0_D6       RCAR_GP_PIN(4, 8)
#define PIN_MMC0_D7       RCAR_GP_PIN(4, 9)
#define PIN_MMC0_DS       RCAR_GP_PIN(4, 10)
#define PIN_SD0_WP        RCAR_GP_PIN(4, 11)
#define PIN_SD0_CD        RCAR_GP_PIN(4, 12)
#define PIN_ERRORIN1      RCAR_GP_PIN(4, 13)
#define PIN_PCIE60_CLKREQ RCAR_GP_PIN(4, 14)
#define PIN_PCIE61_CLKREQ RCAR_GP_PIN(4, 15)

/* GP5 pins */
#define PIN_HTX0     RCAR_GP_PIN(5, 0)
#define PIN_HRX0     RCAR_GP_PIN(5, 1)
#define PIN_HRTS0    RCAR_GP_PIN(5, 2)
#define PIN_HCTS0    RCAR_GP_PIN(5, 3)
#define PIN_HSCK0    RCAR_GP_PIN(5, 4)
#define PIN_SCIF_CLK RCAR_GP_PIN(5, 5)
#define PIN_HTX1     RCAR_GP_PIN(5, 6)
#define PIN_HRX1     RCAR_GP_PIN(5, 7)
#define PIN_HRTS1    RCAR_GP_PIN(5, 8)
#define PIN_HCTS1    RCAR_GP_PIN(5, 9)
#define PIN_HSCK1    RCAR_GP_PIN(5, 10)
#define PIN_IRQ0     RCAR_GP_PIN(5, 11)
#define PIN_IRQ1     RCAR_GP_PIN(5, 12)
#define PIN_IRQ2     RCAR_GP_PIN(5, 13)
#define PIN_IRQ3     RCAR_GP_PIN(5, 14)
#define PIN_TCLK1    RCAR_GP_PIN(5, 15)
#define PIN_TCLK2    RCAR_GP_PIN(5, 16)
#define PIN_TCLK3    RCAR_GP_PIN(5, 17)
#define PIN_TCLK4    RCAR_GP_PIN(5, 18)
#define PIN_TPU0TO0  RCAR_GP_PIN(5, 19)
#define PIN_TPU0TO1  RCAR_GP_PIN(5, 20)
#define PIN_TPU0TO2  RCAR_GP_PIN(5, 21)
#define PIN_TPU0TO3  RCAR_GP_PIN(5, 22)

/* GP6 pins */
#define PIN_RIF6_D0        RCAR_GP_PIN(6, 0)
#define PIN_RIF6_D1        RCAR_GP_PIN(6, 1)
#define PIN_RIF6_SYNC      RCAR_GP_PIN(6, 2)
#define PIN_RIF6_CLK       RCAR_GP_PIN(6, 3)
#define PIN_MSIOF7_SCK     RCAR_GP_PIN(6, 4)
#define PIN_MSIOF7_TXD     RCAR_GP_PIN(6, 5)
#define PIN_MSIOF7_RXD     RCAR_GP_PIN(6, 6)
#define PIN_MSIOF7_SYNC    RCAR_GP_PIN(6, 7)
#define PIN_MSIOF7_SS1     RCAR_GP_PIN(6, 8)
#define PIN_MSIOF7_SS2     RCAR_GP_PIN(6, 9)
#define PIN_MSIOF4_SCK     RCAR_GP_PIN(6, 10)
#define PIN_MSIOF4_TXD     RCAR_GP_PIN(6, 11)
#define PIN_MSIOF4_RXD     RCAR_GP_PIN(6, 12)
#define PIN_MSIOF4_SYNC    RCAR_GP_PIN(6, 13)
#define PIN_MSIOF4_SS1     RCAR_GP_PIN(6, 14)
#define PIN_MSIOF4_SS2     RCAR_GP_PIN(6, 15)
#define PIN_SSI0_SCK       RCAR_GP_PIN(6, 16)
#define PIN_SSI0_WS        RCAR_GP_PIN(6, 17)
#define PIN_SSI0_SD        RCAR_GP_PIN(6, 18)
#define PIN_AUDIO0_CLKOUT0 RCAR_GP_PIN(6, 19)
#define PIN_AUDIO0_CLKOUT1 RCAR_GP_PIN(6, 20)
#define PIN_SSI1_SCK       RCAR_GP_PIN(6, 21)
#define PIN_SSI1_WS        RCAR_GP_PIN(6, 22)
#define PIN_SSI1_SD        RCAR_GP_PIN(6, 23)
#define PIN_AUDIO0_CLKOUT2 RCAR_GP_PIN(6, 24)
#define PIN_AUDIO0_CLKOUT3 RCAR_GP_PIN(6, 25)
#define PIN_SSI2_SCK       RCAR_GP_PIN(6, 26)
#define PIN_SSI2_WS        RCAR_GP_PIN(6, 27)
#define PIN_SSI2_SD        RCAR_GP_PIN(6, 28)
#define PIN_AUDIO1_CLKOUT0 RCAR_GP_PIN(6, 29)
#define PIN_AUDIO1_CLKOUT1 RCAR_GP_PIN(6, 30)

/* GP7 pins */
#define PIN_SSI3_SCK       RCAR_GP_PIN(7, 0)
#define PIN_SSI3_WS        RCAR_GP_PIN(7, 1)
#define PIN_SSI3_SD        RCAR_GP_PIN(7, 2)
#define PIN_AUDIO1_CLKOUT2 RCAR_GP_PIN(7, 3)
#define PIN_AUDIO1_CLKOUT3 RCAR_GP_PIN(7, 4)
#define PIN_SSI4_SCK       RCAR_GP_PIN(7, 5)
#define PIN_SSI4_WS        RCAR_GP_PIN(7, 6)
#define PIN_SSI4_SD        RCAR_GP_PIN(7, 7)
#define PIN_AUDIO_CLKA     RCAR_GP_PIN(7, 8)
#define PIN_SSI5_SCK       RCAR_GP_PIN(7, 9)
#define PIN_SSI5_WS        RCAR_GP_PIN(7, 10)
#define PIN_SSI5_SD        RCAR_GP_PIN(7, 11)
#define PIN_AUDIO_CLKB     RCAR_GP_PIN(7, 12)
#define PIN_SSI6_SCK       RCAR_GP_PIN(7, 13)
#define PIN_SSI6_WS        RCAR_GP_PIN(7, 14)
#define PIN_SSI6_SD        RCAR_GP_PIN(7, 15)
#define PIN_AUDIO_CLKC     RCAR_GP_PIN(7, 16)
#define PIN_MSIOF5_SCK     RCAR_GP_PIN(7, 17)
#define PIN_GP07_18        RCAR_GP_PIN(7, 18)
#define PIN_GP07_19        RCAR_GP_PIN(7, 19)
#define PIN_MSIOF5_TXD     RCAR_GP_PIN(7, 20)
#define PIN_MSIOF5_RXD     RCAR_GP_PIN(7, 21)
#define PIN_MSIOF5_SYNC    RCAR_GP_PIN(7, 22)
#define PIN_MSIOF5_SS1     RCAR_GP_PIN(7, 23)
#define PIN_MSIOF5_SS2     RCAR_GP_PIN(7, 24)
#define PIN_MSIOF6_SCK     RCAR_GP_PIN(7, 25)
#define PIN_MSIOF6_TXD     RCAR_GP_PIN(7, 26)
#define PIN_MSIOF6_RXD     RCAR_GP_PIN(7, 27)
#define PIN_MSIOF6_SYNC    RCAR_GP_PIN(7, 28)
#define PIN_MSIOF6_SS1     RCAR_GP_PIN(7, 29)
#define PIN_MSIOF6_SS2     RCAR_GP_PIN(7, 30)

/* GP8 pins */
#define PIN_SCL1  RCAR_GP_PIN(8, 0)
#define PIN_SDA1  RCAR_GP_PIN(8, 1)
#define PIN_SCL2  RCAR_GP_PIN(8, 2)
#define PIN_SDA2  RCAR_GP_PIN(8, 3)
#define PIN_SCL3  RCAR_GP_PIN(8, 4)
#define PIN_SDA3  RCAR_GP_PIN(8, 5)
#define PIN_SCL4  RCAR_GP_PIN(8, 6)
#define PIN_SDA4  RCAR_GP_PIN(8, 7)
#define PIN_SCL5  RCAR_GP_PIN(8, 8)
#define PIN_SDA5  RCAR_GP_PIN(8, 9)
#define PIN_SCL6  RCAR_GP_PIN(8, 10)
#define PIN_SDA6  RCAR_GP_PIN(8, 11)
#define PIN_SCL7  RCAR_GP_PIN(8, 12)
#define PIN_SDA7  RCAR_GP_PIN(8, 13)
#define PIN_SCL8  RCAR_GP_PIN(8, 14)
#define PIN_SDA8  RCAR_GP_PIN(8, 15)
#define PIN_S3CL0 RCAR_GP_PIN(8, 26)
#define PIN_S3DA0 RCAR_GP_PIN(8, 27)
#define PIN_S3CL1 RCAR_GP_PIN(8, 28)
#define PIN_S3DA1 RCAR_GP_PIN(8, 29)
#define PIN_S3CL2 RCAR_GP_PIN(8, 30)
#define PIN_S3DA2 RCAR_GP_PIN(8, 31)

/* GP9 pins */
#define PIN_ETHES0_PPS     RCAR_GP_PIN(9, 0)
#define PIN_ETHES0_CAPTURE RCAR_GP_PIN(9, 1)
#define PIN_ETHES0_MATCH   RCAR_GP_PIN(9, 2)
#define PIN_ETHES4_PPS     RCAR_GP_PIN(9, 3)
#define PIN_ETHES4_CAPTURE RCAR_GP_PIN(9, 4)
#define PIN_ETHES4_MATCH   RCAR_GP_PIN(9, 5)
#define PIN_ETH25G0_MDIO   RCAR_GP_PIN(9, 6)
#define PIN_ETH25G0_MDC    RCAR_GP_PIN(9, 7)
#define PIN_ETH25G0_LINK   RCAR_GP_PIN(9, 8)
#define PIN_ETH25G0_PHYINT RCAR_GP_PIN(9, 9)
#define PIN_ETH10G0_MDIO   RCAR_GP_PIN(9, 10)
#define PIN_ETH10G0_MDC    RCAR_GP_PIN(9, 11)
#define PIN_ETH10G0_LINK   RCAR_GP_PIN(9, 12)
#define PIN_ETH10G0_PHYINT RCAR_GP_PIN(9, 13)
#define PIN_RSW3_PPS       RCAR_GP_PIN(9, 14)
#define PIN_RSW3_CAPTURE   RCAR_GP_PIN(9, 15)
#define PIN_RSW3_MATCH     RCAR_GP_PIN(9, 16)

/* GP10 pins */
#define PIN_USB0_PWEN       RCAR_GP_PIN(10, 0)
#define PIN_USB0_OVC        RCAR_GP_PIN(10, 1)
#define PIN_USB0_VBUS_VALID RCAR_GP_PIN(10, 2)
#define PIN_USB1_PWEN       RCAR_GP_PIN(10, 3)
#define PIN_USB1_OVC        RCAR_GP_PIN(10, 4)
#define PIN_USB1_VBUS_VALID RCAR_GP_PIN(10, 5)
#define PIN_USB2_PWEN       RCAR_GP_PIN(10, 6)
#define PIN_USB2_OVC        RCAR_GP_PIN(10, 7)
#define PIN_USB2_VBUS_VALID RCAR_GP_PIN(10, 8)
#define PIN_USB3_PWEN       RCAR_GP_PIN(10, 9)
#define PIN_USB3_OVC        RCAR_GP_PIN(10, 10)
#define PIN_USB3_VBUS_VALID RCAR_GP_PIN(10, 11)
#define PIN_PCIE40_CLKREQ   RCAR_GP_PIN(10, 12)
#define PIN_PCIE41_CLKREQ   RCAR_GP_PIN(10, 13)

/* GP0 ALTSEL function 0 */
#define FUNC_DP2_HOTPLUG    RCAR_ALTSEL_FUNC(0, 27, 0)
#define FUNC_DP1_HOTPLUG    RCAR_ALTSEL_FUNC(0, 26, 0)
#define FUNC_DP0_HOTPLUG    RCAR_ALTSEL_FUNC(0, 25, 0)
#define FUNC_MSIOF1_SS2_A   RCAR_ALTSEL_FUNC(0, 24, 0)
#define FUNC_MSIOF1_SS1_A   RCAR_ALTSEL_FUNC(0, 23, 0)
#define FUNC_MSIOF1_SYNC_A  RCAR_ALTSEL_FUNC(0, 22, 0)
#define FUNC_MSIOF1_RXD_A   RCAR_ALTSEL_FUNC(0, 21, 0)
#define FUNC_MSIOF1_TXD_A   RCAR_ALTSEL_FUNC(0, 20, 0)
#define FUNC_MSIOF1_SCK_A   RCAR_ALTSEL_FUNC(0, 19, 0)
#define FUNC_MSIOF0_SS2     RCAR_ALTSEL_FUNC(0, 18, 0)
#define FUNC_MSIOF0_SS1     RCAR_ALTSEL_FUNC(0, 17, 0)
#define FUNC_MSIOF0_SYNC    RCAR_ALTSEL_FUNC(0, 16, 0)
#define FUNC_MSIOF0_RXD     RCAR_ALTSEL_FUNC(0, 15, 0)
#define FUNC_MSIOF0_TXD     RCAR_ALTSEL_FUNC(0, 14, 0)
#define FUNC_MSIOF0_SCK     RCAR_ALTSEL_FUNC(0, 13, 0)
#define FUNC_RXDB_EXTFXR_A  RCAR_ALTSEL_FUNC(0, 12, 0)
#define FUNC_FXR_TXENB_N_A  RCAR_ALTSEL_FUNC(0, 11, 0)
#define FUNC_FXR_TXDB_A     RCAR_ALTSEL_FUNC(0, 10, 0)
#define FUNC_RXDA_EXTFXR_A  RCAR_ALTSEL_FUNC(0, 9, 0)
#define FUNC_FXR_TXENA_N_A  RCAR_ALTSEL_FUNC(0, 8, 0)
#define FUNC_FXR_TXDA_A     RCAR_ALTSEL_FUNC(0, 7, 0)
#define FUNC_CLK_EXTFXR_A   RCAR_ALTSEL_FUNC(0, 6, 0)
#define FUNC_FXR_CLKOUT2_A  RCAR_ALTSEL_FUNC(0, 5, 0)
#define FUNC_FXR_CLKOUT1_A  RCAR_ALTSEL_FUNC(0, 4, 0)
#define FUNC_STPWT_EXTFXR_A RCAR_ALTSEL_FUNC(0, 3, 0)

/* GP0 ALTSEL function 1 */
#define FUNC_TAUD0O13       RCAR_ALTSEL_FUNC(0, 24, 1)
#define FUNC_TAUD0O12       RCAR_ALTSEL_FUNC(0, 23, 1)
#define FUNC_TAUD0O11       RCAR_ALTSEL_FUNC(0, 22, 1)
#define FUNC_TAUD0O10       RCAR_ALTSEL_FUNC(0, 21, 1)
#define FUNC_TAUD0O9        RCAR_ALTSEL_FUNC(0, 20, 1)
#define FUNC_TAUD0O8        RCAR_ALTSEL_FUNC(0, 19, 1)
#define FUNC_TAUD0O7        RCAR_ALTSEL_FUNC(0, 18, 1)
#define FUNC_TAUD0O6        RCAR_ALTSEL_FUNC(0, 17, 1)
#define FUNC_TAUD0O5        RCAR_ALTSEL_FUNC(0, 16, 1)
#define FUNC_TAUD0O4        RCAR_ALTSEL_FUNC(0, 15, 1)
#define FUNC_TAUD0O3        RCAR_ALTSEL_FUNC(0, 14, 1)
#define FUNC_TAUD0O2        RCAR_ALTSEL_FUNC(0, 13, 1)
#define FUNC_CAN11TX        RCAR_ALTSEL_FUNC(0, 12, 1)
#define FUNC_CAN11RX_INTP11 RCAR_ALTSEL_FUNC(0, 11, 1)
#define FUNC_CAN10TX        RCAR_ALTSEL_FUNC(0, 10, 1)
#define FUNC_CAN10RX_INTP10 RCAR_ALTSEL_FUNC(0, 9, 1)
#define FUNC_CAN9TX         RCAR_ALTSEL_FUNC(0, 8, 1)
#define FUNC_CAN9RX_INTP9   RCAR_ALTSEL_FUNC(0, 7, 1)
#define FUNC_CAN8TX         RCAR_ALTSEL_FUNC(0, 6, 1)
#define FUNC_CAN8RX_INTP8   RCAR_ALTSEL_FUNC(0, 5, 1)
#define FUNC_CAN7TX         RCAR_ALTSEL_FUNC(0, 4, 1)
#define FUNC_CAN7RX_INTP7   RCAR_ALTSEL_FUNC(0, 3, 1)

/* GP0 ALTSEL function 2 */
#define FUNC_RLIN311TX          RCAR_ALTSEL_FUNC(0, 12, 2)
#define FUNC_RLIN311RX_INTP27   RCAR_ALTSEL_FUNC(0, 11, 2)
#define FUNC_RLIN310TX          RCAR_ALTSEL_FUNC(0, 10, 2)
#define FUNC_RLIN310RX_INTP26   RCAR_ALTSEL_FUNC(0, 9, 2)
#define FUNC_RLIN39TX           RCAR_ALTSEL_FUNC(0, 8, 2)
#define FUNC_RLIN39RX_INTP25    RCAR_ALTSEL_FUNC(0, 7, 2)
#define FUNC_RLIN38TX           RCAR_ALTSEL_FUNC(0, 6, 2)
#define FUNC_RLIN38RX_INTP24    RCAR_ALTSEL_FUNC(0, 5, 2)
#define FUNC_RLIN315TX_A        RCAR_ALTSEL_FUNC(0, 4, 2)
#define FUNC_RLIN315RX_INTP31_A RCAR_ALTSEL_FUNC(0, 3, 2)

/* GP0 ALTSEL function 3 */
#define FUNC_RTCA0OUT_A RCAR_ALTSEL_FUNC(0, 12, 3)
#define FUNC_EXTCLK0O_A RCAR_ALTSEL_FUNC(0, 11, 3)
#define FUNC_TAUD1O15   RCAR_ALTSEL_FUNC(0, 8, 3)
#define FUNC_TAUD1O14   RCAR_ALTSEL_FUNC(0, 7, 3)
#define FUNC_TAUD1O13   RCAR_ALTSEL_FUNC(0, 6, 3)
#define FUNC_TAUD1O12   RCAR_ALTSEL_FUNC(0, 5, 3)
#define FUNC_TAUD1O11   RCAR_ALTSEL_FUNC(0, 4, 3)
#define FUNC_TAUD1O10   RCAR_ALTSEL_FUNC(0, 3, 3)

/* GP1 ALTSEL function 0 */
#define FUNC_RLIN33TX        RCAR_ALTSEL_FUNC(1, 21, 0)
#define FUNC_RLIN33RX_INTP19 RCAR_ALTSEL_FUNC(1, 20, 0)
#define FUNC_RLIN32TX        RCAR_ALTSEL_FUNC(1, 19, 0)
#define FUNC_RLIN32RX_INTP18 RCAR_ALTSEL_FUNC(1, 18, 0)
#define FUNC_RLIN31TX        RCAR_ALTSEL_FUNC(1, 17, 0)
#define FUNC_RLIN31RX_INTP17 RCAR_ALTSEL_FUNC(1, 16, 0)
#define FUNC_RLIN30TX        RCAR_ALTSEL_FUNC(1, 15, 0)
#define FUNC_RLIN30RX_INTP16 RCAR_ALTSEL_FUNC(1, 14, 0)
#define FUNC_CAN6TX          RCAR_ALTSEL_FUNC(1, 13, 0)
#define FUNC_CAN6RX_INTP6    RCAR_ALTSEL_FUNC(1, 12, 0)
#define FUNC_CAN5TX          RCAR_ALTSEL_FUNC(1, 11, 0)
#define FUNC_CAN5RX_INTP5    RCAR_ALTSEL_FUNC(1, 10, 0)
#define FUNC_CAN4TX          RCAR_ALTSEL_FUNC(1, 9, 0)
#define FUNC_CAN4RX_INTP4    RCAR_ALTSEL_FUNC(1, 8, 0)
#define FUNC_CAN3TX          RCAR_ALTSEL_FUNC(1, 7, 0)
#define FUNC_CAN3RX_INTP3    RCAR_ALTSEL_FUNC(1, 6, 0)
#define FUNC_CAN2TX          RCAR_ALTSEL_FUNC(1, 5, 0)
#define FUNC_CAN2RX_INTP2    RCAR_ALTSEL_FUNC(1, 4, 0)
#define FUNC_CAN1TX          RCAR_ALTSEL_FUNC(1, 3, 0)
#define FUNC_CAN1RX_INTP1    RCAR_ALTSEL_FUNC(1, 2, 0)
#define FUNC_CAN0TX          RCAR_ALTSEL_FUNC(1, 1, 0)
#define FUNC_CAN0RX_INTP0    RCAR_ALTSEL_FUNC(1, 0, 0)

/* GP1 ALTSEL function 1 */
#define FUNC_TAUJ1I3_TAUJ1O3    RCAR_ALTSEL_FUNC(1, 21, 1)
#define FUNC_TAUJ1I2_TAUJ1O2    RCAR_ALTSEL_FUNC(1, 20, 1)
#define FUNC_TAUJ1I1_TAUJ1O1    RCAR_ALTSEL_FUNC(1, 19, 1)
#define FUNC_TAUJ1I0_TAUJ1O0    RCAR_ALTSEL_FUNC(1, 18, 1)
#define FUNC_TAUJ3I3_TAUJ3O3    RCAR_ALTSEL_FUNC(1, 17, 1)
#define FUNC_TAUJ3I2_TAUJ3O2    RCAR_ALTSEL_FUNC(1, 16, 1)
#define FUNC_TAUJ3I1_TAUJ3O1    RCAR_ALTSEL_FUNC(1, 15, 1)
#define FUNC_TAUJ3I0_TAUJ3O0    RCAR_ALTSEL_FUNC(1, 14, 1)
#define FUNC_RLIN314TX_A        RCAR_ALTSEL_FUNC(1, 13, 1)
#define FUNC_RLIN314RX_INTP30_A RCAR_ALTSEL_FUNC(1, 12, 1)
#define FUNC_RLIN313TX_A        RCAR_ALTSEL_FUNC(1, 11, 1)
#define FUNC_RLIN313RX_INTP29_A RCAR_ALTSEL_FUNC(1, 10, 1)
#define FUNC_RLIN312TX_A        RCAR_ALTSEL_FUNC(1, 9, 1)
#define FUNC_RLIN312RX_INTP28_A RCAR_ALTSEL_FUNC(1, 8, 1)
#define FUNC_RLIN37TX_A         RCAR_ALTSEL_FUNC(1, 7, 1)
#define FUNC_RLIN37RX_INTP23_A  RCAR_ALTSEL_FUNC(1, 6, 1)
#define FUNC_RLIN36TX_A         RCAR_ALTSEL_FUNC(1, 5, 1)
#define FUNC_RLIN36RX_INTP22_A  RCAR_ALTSEL_FUNC(1, 4, 1)
#define FUNC_RLIN35TX_A         RCAR_ALTSEL_FUNC(1, 3, 1)
#define FUNC_RLIN35RX_INTP21_A  RCAR_ALTSEL_FUNC(1, 2, 1)
#define FUNC_RLIN34TX_A         RCAR_ALTSEL_FUNC(1, 1, 1)
#define FUNC_RLIN34RX_INTP20_A  RCAR_ALTSEL_FUNC(1, 0, 1)

/* GP1 ALTSEL function 2 */
#define FUNC_CAN15TX_A        RCAR_ALTSEL_FUNC(1, 21, 2)
#define FUNC_CAN15RX_INTP15_A RCAR_ALTSEL_FUNC(1, 20, 2)
#define FUNC_CAN14TX_A        RCAR_ALTSEL_FUNC(1, 19, 2)
#define FUNC_CAN14RX_INTP14_A RCAR_ALTSEL_FUNC(1, 18, 2)
#define FUNC_CAN13TX_A        RCAR_ALTSEL_FUNC(1, 17, 2)
#define FUNC_CAN13RX_INTP13_A RCAR_ALTSEL_FUNC(1, 16, 2)
#define FUNC_CAN12TX_A        RCAR_ALTSEL_FUNC(1, 15, 2)
#define FUNC_CAN12RX_INTP12_A RCAR_ALTSEL_FUNC(1, 14, 2)
#define FUNC_TAUD1O9          RCAR_ALTSEL_FUNC(1, 13, 2)
#define FUNC_TAUD1O8          RCAR_ALTSEL_FUNC(1, 12, 2)
#define FUNC_MSIOF3_SS2       RCAR_ALTSEL_FUNC(1, 11, 2)
#define FUNC_MSIOF3_SS1       RCAR_ALTSEL_FUNC(1, 10, 2)
#define FUNC_MSIOF3_SYNC      RCAR_ALTSEL_FUNC(1, 9, 2)
#define FUNC_MSIOF3_RXD       RCAR_ALTSEL_FUNC(1, 8, 2)
#define FUNC_MSIOF3_TXD       RCAR_ALTSEL_FUNC(1, 7, 2)
#define FUNC_MSIOF3_SCK       RCAR_ALTSEL_FUNC(1, 6, 2)
#define FUNC_MSIOF2_SS2       RCAR_ALTSEL_FUNC(1, 5, 2)
#define FUNC_MSIOF2_SS1       RCAR_ALTSEL_FUNC(1, 4, 2)
#define FUNC_MSIOF2_SYNC      RCAR_ALTSEL_FUNC(1, 3, 2)
#define FUNC_MSIOF2_RXD       RCAR_ALTSEL_FUNC(1, 2, 2)
#define FUNC_MSIOF2_TXD       RCAR_ALTSEL_FUNC(1, 1, 2)
#define FUNC_MSIOF2_SCK       RCAR_ALTSEL_FUNC(1, 0, 2)

/* GP1 ALTSEL function 3 */
#define FUNC_NMI1_A         RCAR_ALTSEL_FUNC(1, 19, 3)
#define FUNC_INTP34_A       RCAR_ALTSEL_FUNC(1, 18, 3)
#define FUNC_INTP33_A       RCAR_ALTSEL_FUNC(1, 17, 3)
#define FUNC_INTP32_A       RCAR_ALTSEL_FUNC(1, 16, 3)
#define FUNC_RXDB_EXTFXR_B  RCAR_ALTSEL_FUNC(1, 11, 3)
#define FUNC_FXR_TXENB_N_B  RCAR_ALTSEL_FUNC(1, 10, 3)
#define FUNC_FXR_TXDB_B     RCAR_ALTSEL_FUNC(1, 9, 3)
#define FUNC_RXDA_EXTFXR_B  RCAR_ALTSEL_FUNC(1, 8, 3)
#define FUNC_FXR_TXENA_N_B  RCAR_ALTSEL_FUNC(1, 7, 3)
#define FUNC_FXR_TXDA_B     RCAR_ALTSEL_FUNC(1, 6, 3)
#define FUNC_CLK_EXTFXR_B   RCAR_ALTSEL_FUNC(1, 5, 3)
#define FUNC_FXR_CLKOUT2_B  RCAR_ALTSEL_FUNC(1, 4, 3)
#define FUNC_FXR_CLKOUT1_B  RCAR_ALTSEL_FUNC(1, 3, 3)
#define FUNC_STPWT_EXTFXR_B RCAR_ALTSEL_FUNC(1, 2, 3)

/* GP2 ALTSEL function 0 */
#define FUNC_INTP34_B          RCAR_ALTSEL_FUNC(2, 28, 0)
#define FUNC_TAUD1O3           RCAR_ALTSEL_FUNC(2, 27, 0)
#define FUNC_TAUD1O2           RCAR_ALTSEL_FUNC(2, 26, 0)
#define FUNC_TAUD1O1           RCAR_ALTSEL_FUNC(2, 25, 0)
#define FUNC_TAUD1O0           RCAR_ALTSEL_FUNC(2, 24, 0)
#define FUNC_EXTCLK0O_B        RCAR_ALTSEL_FUNC(2, 23, 0)
#define FUNC_AVS1              RCAR_ALTSEL_FUNC(2, 22, 0)
#define FUNC_AVS0              RCAR_ALTSEL_FUNC(2, 21, 0)
#define FUNC_SDA0              RCAR_ALTSEL_FUNC(2, 20, 0)
#define FUNC_SCL0              RCAR_ALTSEL_FUNC(2, 19, 0)
#define FUNC_INTP33_B          RCAR_ALTSEL_FUNC(2, 18, 0)
#define FUNC_INTP32_B          RCAR_ALTSEL_FUNC(2, 17, 0)
#define FUNC_CAN_CLK           RCAR_ALTSEL_FUNC(2, 16, 0)
#define FUNC_CAN15TX_B         RCAR_ALTSEL_FUNC(2, 15, 0)
#define FUNC_CAN15RX_INTP15_B  RCAR_ALTSEL_FUNC(2, 14, 0)
#define FUNC_CAN14TX_B         RCAR_ALTSEL_FUNC(2, 13, 0)
#define FUNC_CAN14RX_INTP14_B  RCAR_ALTSEL_FUNC(2, 12, 0)
#define FUNC_CAN13TX_B         RCAR_ALTSEL_FUNC(2, 11, 0)
#define FUNC_CAN13RX_INTP13_B  RCAR_ALTSEL_FUNC(2, 10, 0)
#define FUNC_CAN12TX_B         RCAR_ALTSEL_FUNC(2, 9, 0)
#define FUNC_CAN12RX_INTP12_B  RCAR_ALTSEL_FUNC(2, 8, 0)
#define FUNC_RLIN37TX_B        RCAR_ALTSEL_FUNC(2, 7, 0)
#define FUNC_RLIN37RX_INTP23_B RCAR_ALTSEL_FUNC(2, 6, 0)
#define FUNC_RLIN36TX_B        RCAR_ALTSEL_FUNC(2, 5, 0)
#define FUNC_RLIN36RX_INTP22_B RCAR_ALTSEL_FUNC(2, 4, 0)
#define FUNC_RLIN35TX_B        RCAR_ALTSEL_FUNC(2, 3, 0)
#define FUNC_RLIN35RX_INTP21_B RCAR_ALTSEL_FUNC(2, 2, 0)
#define FUNC_RLIN34TX_B        RCAR_ALTSEL_FUNC(2, 1, 0)
#define FUNC_RLIN34RX_INTP20_B RCAR_ALTSEL_FUNC(2, 0, 0)

/* GP2 ALTSEL function 1 */
#define FUNC_TAUD0O1            RCAR_ALTSEL_FUNC(2, 18, 1)
#define FUNC_TAUD0O0            RCAR_ALTSEL_FUNC(2, 17, 1)
#define FUNC_RLIN315TX_B        RCAR_ALTSEL_FUNC(2, 15, 1)
#define FUNC_RLIN315RX_INTP31_B RCAR_ALTSEL_FUNC(2, 14, 1)
#define FUNC_RLIN314TX_B        RCAR_ALTSEL_FUNC(2, 13, 1)
#define FUNC_RLIN314RX_INTP30_B RCAR_ALTSEL_FUNC(2, 12, 1)
#define FUNC_RLIN313TX          RCAR_ALTSEL_FUNC(2, 11, 1)
#define FUNC_RLIN313RX_INTP29_B RCAR_ALTSEL_FUNC(2, 10, 1)
#define FUNC_RLIN312TX          RCAR_ALTSEL_FUNC(2, 9, 1)
#define FUNC_RLIN312RX_INTP28_B RCAR_ALTSEL_FUNC(2, 8, 1)
#define FUNC_RTCA0OUT_B         RCAR_ALTSEL_FUNC(2, 7, 1)
#define FUNC_MSIOF1_SS2_B       RCAR_ALTSEL_FUNC(2, 5, 1)
#define FUNC_MSIOF1_SS1_B       RCAR_ALTSEL_FUNC(2, 4, 1)
#define FUNC_MSIOF1_SYN_B       RCAR_ALTSEL_FUNC(2, 3, 1)
#define FUNC_MSIOF1_RXD_B       RCAR_ALTSEL_FUNC(2, 2, 1)
#define FUNC_MSIOF1_TXD_B       RCAR_ALTSEL_FUNC(2, 1, 1)
#define FUNC_MSIOF1_SCK_B       RCAR_ALTSEL_FUNC(2, 0, 1)

/* GP2 ALTSEL function 2 */
#define FUNC_TAUD1O7  RCAR_ALTSEL_FUNC(2, 9, 2)
#define FUNC_TAUD1O6  RCAR_ALTSEL_FUNC(2, 8, 2)
#define FUNC_TAUD1O5  RCAR_ALTSEL_FUNC(2, 7, 2)
#define FUNC_TAUD1O4  RCAR_ALTSEL_FUNC(2, 6, 2)
#define FUNC_TAUD0O15 RCAR_ALTSEL_FUNC(2, 1, 2)
#define FUNC_TAUD0O14 RCAR_ALTSEL_FUNC(2, 0, 2)

/* GP2 ALTSEL function 3 */
#define FUNC_CANXL1_TX RCAR_ALTSEL_FUNC(2, 11, 3)
#define FUNC_CANXL1_RX RCAR_ALTSEL_FUNC(2, 10, 3)
#define FUNC_CANXL0_TX RCAR_ALTSEL_FUNC(2, 9, 3)
#define FUNC_CANXL0_RX RCAR_ALTSEL_FUNC(2, 8, 3)
#define FUNC_CTIACK    RCAR_ALTSEL_FUNC(2, 4, 3)
#define FUNC_CTIREQ    RCAR_ALTSEL_FUNC(2, 3, 3)

/* GP3 ALTSEL function 0 */
#define FUNC_ERRORIN0_N     RCAR_ALTSEL_FUNC(3, 16, 0)
#define FUNC_ERROROUT_N     RCAR_ALTSEL_FUNC(3, 15, 0)
#define FUNC_QSPI1_SSL      RCAR_ALTSEL_FUNC(3, 14, 0)
#define FUNC_QSPI1_IO3      RCAR_ALTSEL_FUNC(3, 13, 0)
#define FUNC_QSPI1_IO2      RCAR_ALTSEL_FUNC(3, 12, 0)
#define FUNC_QSPI1_MISO_IO1 RCAR_ALTSEL_FUNC(3, 11, 0)
#define FUNC_QSPI1_MOSI_IO0 RCAR_ALTSEL_FUNC(3, 10, 0)
#define FUNC_QSPI1_SPCLK    RCAR_ALTSEL_FUNC(3, 9, 0)
#define FUNC_RPC_INT_N      RCAR_ALTSEL_FUNC(3, 8, 0)
#define FUNC_RPC_WP_N       RCAR_ALTSEL_FUNC(3, 7, 0)
#define FUNC_RPC_RESET_N    RCAR_ALTSEL_FUNC(3, 6, 0)
#define FUNC_QSPI0_SSL      RCAR_ALTSEL_FUNC(3, 5, 0)
#define FUNC_QSPI0_IO3      RCAR_ALTSEL_FUNC(3, 4, 0)
#define FUNC_QSPI0_IO2      RCAR_ALTSEL_FUNC(3, 3, 0)
#define FUNC_QSPI0_MISO_IO1 RCAR_ALTSEL_FUNC(3, 2, 0)
#define FUNC_QSPI0_MOSI_IO0 RCAR_ALTSEL_FUNC(3, 1, 0)
#define FUNC_QSPI0_SPCLK    RCAR_ALTSEL_FUNC(3, 0, 0)

/* GP4 ALTSEL function 0 */
#define FUNC_PCIE61_CLKREQ_N RCAR_ALTSEL_FUNC(4, 15, 0)
#define FUNC_PCIE60_CLKREQ_N RCAR_ALTSEL_FUNC(4, 14, 0)
#define FUNC_ERRORIN1_N      RCAR_ALTSEL_FUNC(4, 13, 0)
#define FUNC_SD0_CD          RCAR_ALTSEL_FUNC(4, 12, 0)
#define FUNC_SD0_WP          RCAR_ALTSEL_FUNC(4, 11, 0)
#define FUNC_MMC0_DS         RCAR_ALTSEL_FUNC(4, 10, 0)
#define FUNC_MMC0_D7         RCAR_ALTSEL_FUNC(4, 9, 0)
#define FUNC_MMC0_D6         RCAR_ALTSEL_FUNC(4, 8, 0)
#define FUNC_MMC0_D5         RCAR_ALTSEL_FUNC(4, 7, 0)
#define FUNC_MMC0_D4         RCAR_ALTSEL_FUNC(4, 6, 0)
#define FUNC_MMC0_SD_D3      RCAR_ALTSEL_FUNC(4, 5, 0)
#define FUNC_MMC0_SD_D2      RCAR_ALTSEL_FUNC(4, 4, 0)
#define FUNC_MMC0_SD_D1      RCAR_ALTSEL_FUNC(4, 3, 0)
#define FUNC_MMC0_SD_D0      RCAR_ALTSEL_FUNC(4, 2, 0)
#define FUNC_MMC0_SD_CMD     RCAR_ALTSEL_FUNC(4, 1, 0)
#define FUNC_MMC0_SD_CLK     RCAR_ALTSEL_FUNC(4, 0, 0)

/* GP5 ALTSEL function 0 */
#define FUNC_TPU0TO3  RCAR_ALTSEL_FUNC(5, 22, 0)
#define FUNC_TPU0TO2  RCAR_ALTSEL_FUNC(5, 21, 0)
#define FUNC_TPU0TO1  RCAR_ALTSEL_FUNC(5, 20, 0)
#define FUNC_TPU0TO0  RCAR_ALTSEL_FUNC(5, 19, 0)
#define FUNC_TCLK4    RCAR_ALTSEL_FUNC(5, 18, 0)
#define FUNC_TCLK3    RCAR_ALTSEL_FUNC(5, 17, 0)
#define FUNC_TCLK2    RCAR_ALTSEL_FUNC(5, 16, 0)
#define FUNC_TCLK1    RCAR_ALTSEL_FUNC(5, 15, 0)
#define FUNC_IRQ3_A   RCAR_ALTSEL_FUNC(5, 14, 0)
#define FUNC_IRQ2_A   RCAR_ALTSEL_FUNC(5, 13, 0)
#define FUNC_IRQ1_A   RCAR_ALTSEL_FUNC(5, 12, 0)
#define FUNC_IRQ0_A   RCAR_ALTSEL_FUNC(5, 11, 0)
#define FUNC_HSCK1    RCAR_ALTSEL_FUNC(5, 10, 0)
#define FUNC_HCTS1_N  RCAR_ALTSEL_FUNC(5, 9, 0)
#define FUNC_HRTS1_N  RCAR_ALTSEL_FUNC(5, 8, 0)
#define FUNC_HRX1     RCAR_ALTSEL_FUNC(5, 7, 0)
#define FUNC_HTX1     RCAR_ALTSEL_FUNC(5, 6, 0)
#define FUNC_SCIF_CLK RCAR_ALTSEL_FUNC(5, 5, 0)
#define FUNC_HSCK0    RCAR_ALTSEL_FUNC(5, 4, 0)
#define FUNC_HCTS0_N  RCAR_ALTSEL_FUNC(5, 3, 0)
#define FUNC_HRTS0_N  RCAR_ALTSEL_FUNC(5, 2, 0)
#define FUNC_HRX0     RCAR_ALTSEL_FUNC(5, 1, 0)
#define FUNC_HTX0     RCAR_ALTSEL_FUNC(5, 0, 0)

/* GP5 ALTSEL function 1 */
#define FUNC_SSI9_WS   RCAR_ALTSEL_FUNC(5, 22, 1)
#define FUNC_SSI9_SCK  RCAR_ALTSEL_FUNC(5, 21, 1)
#define FUNC_PWM5      RCAR_ALTSEL_FUNC(5, 20, 1)
#define FUNC_PWM4      RCAR_ALTSEL_FUNC(5, 19, 1)
#define FUNC_PWM3      RCAR_ALTSEL_FUNC(5, 18, 1)
#define FUNC_PWM2      RCAR_ALTSEL_FUNC(5, 17, 1)
#define FUNC_PWM1      RCAR_ALTSEL_FUNC(5, 16, 1)
#define FUNC_PWM0_A    RCAR_ALTSEL_FUNC(5, 15, 1)
#define FUNC_SSI17_SD  RCAR_ALTSEL_FUNC(5, 13, 1)
#define FUNC_SSI17_WS  RCAR_ALTSEL_FUNC(5, 12, 1)
#define FUNC_SSI17_SCK RCAR_ALTSEL_FUNC(5, 11, 1)
#define FUNC_SCK1      RCAR_ALTSEL_FUNC(5, 10, 1)
#define FUNC_CTS1_N    RCAR_ALTSEL_FUNC(5, 9, 1)
#define FUNC_RTS1_N    RCAR_ALTSEL_FUNC(5, 8, 1)
#define FUNC_RX1       RCAR_ALTSEL_FUNC(5, 7, 1)
#define FUNC_TX1       RCAR_ALTSEL_FUNC(5, 6, 1)
#define FUNC_SCK0      RCAR_ALTSEL_FUNC(5, 4, 1)
#define FUNC_CTS0_N    RCAR_ALTSEL_FUNC(5, 3, 1)
#define FUNC_RTS0_N    RCAR_ALTSEL_FUNC(5, 2, 1)
#define FUNC_RX0       RCAR_ALTSEL_FUNC(5, 1, 1)
#define FUNC_TX0       RCAR_ALTSEL_FUNC(5, 0, 1)

/* GP5 ALTSEL function 2 */
#define FUNC_SSI19_SD    RCAR_ALTSEL_FUNC(5, 18, 2)
#define FUNC_SSI19_WS    RCAR_ALTSEL_FUNC(5, 17, 2)
#define FUNC_SSI19_SCK   RCAR_ALTSEL_FUNC(5, 16, 2)
#define FUNC_SSI18_SD    RCAR_ALTSEL_FUNC(5, 15, 2)
#define FUNC_SSI13_SCK   RCAR_ALTSEL_FUNC(5, 10, 2)
#define FUNC_RIF0_SYNC_B RCAR_ALTSEL_FUNC(5, 8, 2)
#define FUNC_IRQ1_B      RCAR_ALTSEL_FUNC(5, 3, 2)
#define FUNC_IRQ0_B      RCAR_ALTSEL_FUNC(5, 2, 2)
#define FUNC_SSI13_SD    RCAR_ALTSEL_FUNC(5, 1, 2)
#define FUNC_SSI13_WS    RCAR_ALTSEL_FUNC(5, 0, 2)

/* GP5 ALTSEL function 3*/
#define FUNC_RIF7_D1    RCAR_ALTSEL_FUNC(5, 14, 3)
#define FUNC_RIF7_D0    RCAR_ALTSEL_FUNC(5, 13, 3)
#define FUNC_RIF7_SYNC  RCAR_ALTSEL_FUNC(5, 12, 3)
#define FUNC_RIF7_CLK   RCAR_ALTSEL_FUNC(5, 11, 3)
#define FUNC_RIF0_CLK_B RCAR_ALTSEL_FUNC(5, 10, 3)
#define FUNC_SSI16_SD   RCAR_ALTSEL_FUNC(5, 8, 3)
#define FUNC_SSI16_WS   RCAR_ALTSEL_FUNC(5, 7, 3)
#define FUNC_SSI16_SCK  RCAR_ALTSEL_FUNC(5, 6, 3)
#define FUNC_SSI15_SD   RCAR_ALTSEL_FUNC(5, 4, 3)
#define FUNC_SSI15_WS   RCAR_ALTSEL_FUNC(5, 3, 3)
#define FUNC_SSI15_SCK  RCAR_ALTSEL_FUNC(5, 2, 3)
#define FUNC_RIF0_D1_B  RCAR_ALTSEL_FUNC(5, 1, 3)
#define FUNC_RIF0_D0_B  RCAR_ALTSEL_FUNC(5, 0, 3)

/* GP6 ALTSEL function 0 */
#define FUNC_AUDIO1_CLKOUT1 RCAR_ALTSEL_FUNC(6, 30, 0)
#define FUNC_AUDIO1_CLKOUT0 RCAR_ALTSEL_FUNC(6, 29, 0)
#define FUNC_SSI2_SD        RCAR_ALTSEL_FUNC(6, 28, 0)
#define FUNC_SSI2_WS        RCAR_ALTSEL_FUNC(6, 27, 0)
#define FUNC_SSI2_SCK       RCAR_ALTSEL_FUNC(6, 26, 0)
#define FUNC_AUDIO0_CLKOUT3 RCAR_ALTSEL_FUNC(6, 25, 0)
#define FUNC_AUDIO0_CLKOUT2 RCAR_ALTSEL_FUNC(6, 24, 0)
#define FUNC_SSI1_SD        RCAR_ALTSEL_FUNC(6, 23, 0)
#define FUNC_SSI1_WS        RCAR_ALTSEL_FUNC(6, 22, 0)
#define FUNC_SSI1_SCK       RCAR_ALTSEL_FUNC(6, 21, 0)
#define FUNC_AUDIO0_CLKOUT1 RCAR_ALTSEL_FUNC(6, 20, 0)
#define FUNC_AUDIO0_CLKOUT0 RCAR_ALTSEL_FUNC(6, 19, 0)
#define FUNC_SSI0_SD        RCAR_ALTSEL_FUNC(6, 18, 0)
#define FUNC_SSI0_WS        RCAR_ALTSEL_FUNC(6, 17, 0)
#define FUNC_SSI0_SCK       RCAR_ALTSEL_FUNC(6, 16, 0)
#define FUNC_MSIOF4_SS2_B   RCAR_ALTSEL_FUNC(6, 15, 0)
#define FUNC_MSIOF4_SS1_B   RCAR_ALTSEL_FUNC(6, 14, 0)
#define FUNC_MSIOF4_SYNC_B  RCAR_ALTSEL_FUNC(6, 13, 0)
#define FUNC_MSIOF4_RXD_B   RCAR_ALTSEL_FUNC(6, 12, 0)
#define FUNC_MSIOF4_TXD_B   RCAR_ALTSEL_FUNC(6, 11, 0)
#define FUNC_MSIOF4_SCK_B   RCAR_ALTSEL_FUNC(6, 10, 0)
#define FUNC_MSIOF7_SS2_A   RCAR_ALTSEL_FUNC(6, 9, 0)
#define FUNC_MSIOF7_SS1_A   RCAR_ALTSEL_FUNC(6, 8, 0)
#define FUNC_MSIOF7_SYNC_A  RCAR_ALTSEL_FUNC(6, 7, 0)
#define FUNC_MSIOF7_RXD_A   RCAR_ALTSEL_FUNC(6, 6, 0)
#define FUNC_MSIOF7_TXD_A   RCAR_ALTSEL_FUNC(6, 5, 0)
#define FUNC_MSIOF7_SCK_A   RCAR_ALTSEL_FUNC(6, 4, 0)
#define FUNC_RIF6_CLK       RCAR_ALTSEL_FUNC(6, 3, 0)
#define FUNC_RIF6_SYNC      RCAR_ALTSEL_FUNC(6, 2, 0)
#define FUNC_RIF6_D1        RCAR_ALTSEL_FUNC(6, 1, 0)
#define FUNC_RIF6_D0        RCAR_ALTSEL_FUNC(6, 0, 0)

/* GP6 ALTSEL function 1 */
#define FUNC_MSIOF7_RXD_B  RCAR_ALTSEL_FUNC(6, 30, 1)
#define FUNC_MSIOF7_TXD_B  RCAR_ALTSEL_FUNC(6, 29, 1)
#define FUNC_MSIOF7_SCK_B  RCAR_ALTSEL_FUNC(6, 28, 1)
#define FUNC_MSIOF4_SS2_A  RCAR_ALTSEL_FUNC(6, 21, 1)
#define FUNC_MSIOF4_SS1_A  RCAR_ALTSEL_FUNC(6, 20, 1)
#define FUNC_MSIOF4_SYNC_A RCAR_ALTSEL_FUNC(6, 19, 1)
#define FUNC_MSIOF4_RXD_A  RCAR_ALTSEL_FUNC(6, 18, 1)
#define FUNC_MSIOF4_TXD_A  RCAR_ALTSEL_FUNC(6, 17, 1)
#define FUNC_MSIOF4_SCK_A  RCAR_ALTSEL_FUNC(6, 16, 1)
#define FUNC_SSI14_SD      RCAR_ALTSEL_FUNC(6, 15, 1)
#define FUNC_SSI12_SD      RCAR_ALTSEL_FUNC(6, 14, 1)
#define FUNC_SSI12_WS      RCAR_ALTSEL_FUNC(6, 13, 1)
#define FUNC_SSI12_SCK     RCAR_ALTSEL_FUNC(6, 11, 1)
#define FUNC_SSI14_WS      RCAR_ALTSEL_FUNC(6, 9, 1)
#define FUNC_SSI14_SCK     RCAR_ALTSEL_FUNC(6, 8, 1)
#define FUNC_RIF1_D1_B     RCAR_ALTSEL_FUNC(6, 7, 1)
#define FUNC_RIF1_D0_B     RCAR_ALTSEL_FUNC(6, 6, 1)
#define FUNC_RIF1_SYNC_B   RCAR_ALTSEL_FUNC(6, 5, 1)
#define FUNC_RIF1_CLK_B    RCAR_ALTSEL_FUNC(6, 4, 1)
#define FUNC_SSI10_SD      RCAR_ALTSEL_FUNC(6, 3, 1)
#define FUNC_SSI10_WS      RCAR_ALTSEL_FUNC(6, 2, 1)
#define FUNC_SSI10_SCK     RCAR_ALTSEL_FUNC(6, 1, 1)
#define FUNC_SSI9_SD       RCAR_ALTSEL_FUNC(6, 0, 1)

/* GP6 ALTSEL function 2 */
#define FUNC_RIF5_CLK     RCAR_ALTSEL_FUNC(6, 30, 2)
#define FUNC_RIF5_SYNC    RCAR_ALTSEL_FUNC(6, 28, 2)
#define FUNC_RIF1_D1_A    RCAR_ALTSEL_FUNC(6, 27, 2)
#define FUNC_RIF1_D0_A    RCAR_ALTSEL_FUNC(6, 26, 2)
#define FUNC_RIF1_CLK_A   RCAR_ALTSEL_FUNC(6, 25, 2)
#define FUNC_RIF2_D1      RCAR_ALTSEL_FUNC(6, 24, 2)
#define FUNC_HCTS3_N      RCAR_ALTSEL_FUNC(6, 23, 2)
#define FUNC_HRTS3_N      RCAR_ALTSEL_FUNC(6, 22, 2)
#define FUNC_HSCK3        RCAR_ALTSEL_FUNC(6, 21, 2)
#define FUNC_RIF2_D0      RCAR_ALTSEL_FUNC(6, 20, 2)
#define FUNC_RIF2_SYNC    RCAR_ALTSEL_FUNC(6, 19, 2)
#define FUNC_HRX3         RCAR_ALTSEL_FUNC(6, 18, 2)
#define FUNC_HTX3         RCAR_ALTSEL_FUNC(6, 17, 2)
#define FUNC_AUDIO_CLKC_B RCAR_ALTSEL_FUNC(6, 12, 2)
#define FUNC_AUDIO_CLKB_B RCAR_ALTSEL_FUNC(6, 10, 2)
#define FUNC_SSI11_SD     RCAR_ALTSEL_FUNC(6, 7, 2)
#define FUNC_SSI11_WS     RCAR_ALTSEL_FUNC(6, 6, 2)
#define FUNC_SSI11_SCK    RCAR_ALTSEL_FUNC(6, 5, 2)
#define FUNC_AUDIO_CLKA_B RCAR_ALTSEL_FUNC(6, 4, 2)

/* GP6 ALTSEL function 3 */
#define FUNC_CTS3_N      RCAR_ALTSEL_FUNC(6, 23, 3)
#define FUNC_RTS3_N      RCAR_ALTSEL_FUNC(6, 22, 3)
#define FUNC_SCK3        RCAR_ALTSEL_FUNC(6, 21, 3)
#define FUNC_RX3         RCAR_ALTSEL_FUNC(6, 18, 3)
#define FUNC_TX3         RCAR_ALTSEL_FUNC(6, 17, 3)
#define FUNC_RIF1_SYNC_A RCAR_ALTSEL_FUNC(6, 11, 3)

/* GP7 ALTSEL function 0 */
#define FUNC_MSIOF6_SS2_B   RCAR_ALTSEL_FUNC(7, 30, 0)
#define FUNC_MSIOF6_SS1_B   RCAR_ALTSEL_FUNC(7, 29, 0)
#define FUNC_MSIOF6_SYNC_B  RCAR_ALTSEL_FUNC(7, 28, 0)
#define FUNC_MSIOF6_RXD_B   RCAR_ALTSEL_FUNC(7, 27, 0)
#define FUNC_MSIOF6_TXD_B   RCAR_ALTSEL_FUNC(7, 26, 0)
#define FUNC_MSIOF6_SCK_B   RCAR_ALTSEL_FUNC(7, 25, 0)
#define FUNC_MSIOF5_SS2     RCAR_ALTSEL_FUNC(7, 24, 0)
#define FUNC_MSIOF5_SS1     RCAR_ALTSEL_FUNC(7, 23, 0)
#define FUNC_MSIOF5_SYNC    RCAR_ALTSEL_FUNC(7, 22, 0)
#define FUNC_MSIOF5_RXD     RCAR_ALTSEL_FUNC(7, 21, 0)
#define FUNC_MSIOF5_TXD     RCAR_ALTSEL_FUNC(7, 20, 0)
#define FUNC_MSIOF5_SCK     RCAR_ALTSEL_FUNC(7, 17, 0)
#define FUNC_AUDIO_CLKC_A   RCAR_ALTSEL_FUNC(7, 16, 0)
#define FUNC_SSI6_SD        RCAR_ALTSEL_FUNC(7, 15, 0)
#define FUNC_SSI6_WS        RCAR_ALTSEL_FUNC(7, 14, 0)
#define FUNC_SSI6_SCK       RCAR_ALTSEL_FUNC(7, 13, 0)
#define FUNC_AUDIO_CLKB_A   RCAR_ALTSEL_FUNC(7, 12, 0)
#define FUNC_SSI5_SD        RCAR_ALTSEL_FUNC(7, 11, 0)
#define FUNC_SSI5_WS        RCAR_ALTSEL_FUNC(7, 10, 0)
#define FUNC_SSI5_SCK       RCAR_ALTSEL_FUNC(7, 9, 0)
#define FUNC_AUDIO_CLKA_A   RCAR_ALTSEL_FUNC(7, 8, 0)
#define FUNC_SSI4_SD        RCAR_ALTSEL_FUNC(7, 7, 0)
#define FUNC_SSI4_WS        RCAR_ALTSEL_FUNC(7, 6, 0)
#define FUNC_SSI4_SCK       RCAR_ALTSEL_FUNC(7, 5, 0)
#define FUNC_AUDIO1_CLKOUT3 RCAR_ALTSEL_FUNC(7, 4, 0)
#define FUNC_AUDIO1_CLKOUT2 RCAR_ALTSEL_FUNC(7, 3, 0)
#define FUNC_SSI3_SD        RCAR_ALTSEL_FUNC(7, 2, 0)
#define FUNC_SSI3_WS        RCAR_ALTSEL_FUNC(7, 1, 0)
#define FUNC_SSI3_SCK       RCAR_ALTSEL_FUNC(7, 0, 0)

/* GP7 ALTSEL function 1 */
#define FUNC_HRX2_B        RCAR_ALTSEL_FUNC(7, 30, 1)
#define FUNC_SSI7_SD       RCAR_ALTSEL_FUNC(7, 29, 1)
#define FUNC_SSI7_WS       RCAR_ALTSEL_FUNC(7, 28, 1)
#define FUNC_SSI7_SCK      RCAR_ALTSEL_FUNC(7, 27, 1)
#define FUNC_HTX2_B        RCAR_ALTSEL_FUNC(7, 26, 1)
#define FUNC_SSI8_SD       RCAR_ALTSEL_FUNC(7, 25, 1)
#define FUNC_HCTS2_N_B     RCAR_ALTSEL_FUNC(7, 24, 1)
#define FUNC_RIF0_SYNC_A   RCAR_ALTSEL_FUNC(7, 23, 1)
#define FUNC_HRTS2_N_B     RCAR_ALTSEL_FUNC(7, 22, 1)
#define FUNC_RIF0_D1_A     RCAR_ALTSEL_FUNC(7, 21, 1)
#define FUNC_HSCK2_B       RCAR_ALTSEL_FUNC(7, 20, 1)
#define FUNC_MSIOF6_SS2_A  RCAR_ALTSEL_FUNC(7, 19, 1)
#define FUNC_MSIOF6_SS1_A  RCAR_ALTSEL_FUNC(7, 18, 1)
#define FUNC_MSIOF6_RXD_A  RCAR_ALTSEL_FUNC(7, 15, 1)
#define FUNC_MSIOF6_TXD_A  RCAR_ALTSEL_FUNC(7, 14, 1)
#define FUNC_MSIOF6_SCK_A  RCAR_ALTSEL_FUNC(7, 13, 1)
#define FUNC_MSIOF6_SYNC_A RCAR_ALTSEL_FUNC(7, 11, 1)
#define FUNC_RIF3_SYNC     RCAR_ALTSEL_FUNC(7, 10, 1)
#define FUNC_RIF3_CLK      RCAR_ALTSEL_FUNC(7, 9, 1)
#define FUNC_RIF3_D1       RCAR_ALTSEL_FUNC(7, 7, 1)
#define FUNC_RIF3_D0       RCAR_ALTSEL_FUNC(7, 6, 1)
#define FUNC_RIF2_CLK      RCAR_ALTSEL_FUNC(7, 5, 1)
#define FUNC_RIF0_D0_A     RCAR_ALTSEL_FUNC(7, 4, 1)
#define FUNC_RIF0_CLK_A    RCAR_ALTSEL_FUNC(7, 3, 1)
#define FUNC_MSIOF7_SS2_B  RCAR_ALTSEL_FUNC(7, 2, 1)
#define FUNC_MSIOF7_SS1_B  RCAR_ALTSEL_FUNC(7, 1, 1)
#define FUNC_MSIOF7_SYNC_B RCAR_ALTSEL_FUNC(7, 0, 1)

/* GP7 ALTSEL function 2 */
#define FUNC_RX4_B     RCAR_ALTSEL_FUNC(7, 30, 2)
#define FUNC_TX4_B     RCAR_ALTSEL_FUNC(7, 26, 2)
#define FUNC_CTS4_N_B  RCAR_ALTSEL_FUNC(7, 24, 2)
#define FUNC_RTS4_N_B  RCAR_ALTSEL_FUNC(7, 22, 2)
#define FUNC_SCK4_B    RCAR_ALTSEL_FUNC(7, 20, 2)
#define FUNC_RIF4_D1   RCAR_ALTSEL_FUNC(7, 15, 2)
#define FUNC_RIF4_D0   RCAR_ALTSEL_FUNC(7, 14, 2)
#define FUNC_RIF4_SYNC RCAR_ALTSEL_FUNC(7, 13, 2)
#define FUNC_RIF4_CLK  RCAR_ALTSEL_FUNC(7, 11, 2)
#define FUNC_RIF5_D1   RCAR_ALTSEL_FUNC(7, 1, 2)
#define FUNC_RIF5_D0   RCAR_ALTSEL_FUNC(7, 0, 2)

/* GP8 ALTSEL function 0 */
#define FUNC_S3DA2 RCAR_ALTSEL_FUNC(8, 31, 0)
#define FUNC_S3CL2 RCAR_ALTSEL_FUNC(8, 30, 0)
#define FUNC_S3DA1 RCAR_ALTSEL_FUNC(8, 29, 0)
#define FUNC_S3CL1 RCAR_ALTSEL_FUNC(8, 28, 0)
#define FUNC_S3DA0 RCAR_ALTSEL_FUNC(8, 27, 0)
#define FUNC_S3CL0 RCAR_ALTSEL_FUNC(8, 26, 0)
#define FUNC_SDA8  RCAR_ALTSEL_FUNC(8, 15, 0)
#define FUNC_SCL8  RCAR_ALTSEL_FUNC(8, 14, 0)
#define FUNC_SDA7  RCAR_ALTSEL_FUNC(8, 13, 0)
#define FUNC_SCL7  RCAR_ALTSEL_FUNC(8, 12, 0)
#define FUNC_SDA6  RCAR_ALTSEL_FUNC(8, 11, 0)
#define FUNC_SCL6  RCAR_ALTSEL_FUNC(8, 10, 0)
#define FUNC_SDA5  RCAR_ALTSEL_FUNC(8, 9, 0)
#define FUNC_SCL5  RCAR_ALTSEL_FUNC(8, 8, 0)
#define FUNC_SDA4  RCAR_ALTSEL_FUNC(8, 7, 0)
#define FUNC_SCL4  RCAR_ALTSEL_FUNC(8, 6, 0)
#define FUNC_SDA3  RCAR_ALTSEL_FUNC(8, 5, 0)
#define FUNC_SCL3  RCAR_ALTSEL_FUNC(8, 4, 0)
#define FUNC_SDA2  RCAR_ALTSEL_FUNC(8, 3, 0)
#define FUNC_SCL2  RCAR_ALTSEL_FUNC(8, 2, 0)
#define FUNC_SDA1  RCAR_ALTSEL_FUNC(8, 1, 0)
#define FUNC_SCL1  RCAR_ALTSEL_FUNC(8, 0, 0)

/* GP8 ALTSEL function 1 */
#define FUNC_HCTS2_N_A RCAR_ALTSEL_FUNC(8, 7, 1)
#define FUNC_HRTS2_N_A RCAR_ALTSEL_FUNC(8, 6, 1)
#define FUNC_HRX2_A    RCAR_ALTSEL_FUNC(8, 5, 1)
#define FUNC_HTX2_A    RCAR_ALTSEL_FUNC(8, 4, 1)
#define FUNC_HSCK2_A   RCAR_ALTSEL_FUNC(8, 3, 1)
#define FUNC_PWM0_B    RCAR_ALTSEL_FUNC(8, 2, 1)

/* GP8 ALTSEL function 2 */
#define FUNC_CTS4_N_A RCAR_ALTSEL_FUNC(8, 7, 2)
#define FUNC_RTS4_N_A RCAR_ALTSEL_FUNC(8, 6, 2)
#define FUNC_RX4_A    RCAR_ALTSEL_FUNC(8, 5, 2)
#define FUNC_TX4_A    RCAR_ALTSEL_FUNC(8, 4, 2)
#define FUNC_SCK4_A   RCAR_ALTSEL_FUNC(8, 3, 2)

/* GP8 ALTSEL function 3 */
#define FUNC_PWM7_B RCAR_ALTSEL_FUNC(8, 7, 3)
#define FUNC_PWM9_B RCAR_ALTSEL_FUNC(8, 6, 3)
#define FUNC_PWM8_B RCAR_ALTSEL_FUNC(8, 5, 3)
#define FUNC_PWM6_B RCAR_ALTSEL_FUNC(8, 4, 3)

/* GP9 ALTSEL function 0 */
#define FUNC_RSW3_MATCH     RCAR_ALTSEL_FUNC(9, 16, 0)
#define FUNC_RSW3_CAPTURE   RCAR_ALTSEL_FUNC(9, 15, 0)
#define FUNC_RSW3_PPS       RCAR_ALTSEL_FUNC(9, 14, 0)
#define FUNC_ETH10G0_PHYINT RCAR_ALTSEL_FUNC(9, 13, 0)
#define FUNC_ETH10G0_LINK   RCAR_ALTSEL_FUNC(9, 12, 0)
#define FUNC_ETH10G0_MDC    RCAR_ALTSEL_FUNC(9, 11, 0)
#define FUNC_ETH10G0_MDIO   RCAR_ALTSEL_FUNC(9, 10, 0)
#define FUNC_ETH25G0_PHYINT RCAR_ALTSEL_FUNC(9, 9, 0)
#define FUNC_ETH25G0_LINK   RCAR_ALTSEL_FUNC(9, 8, 0)
#define FUNC_ETH25G0_MDC    RCAR_ALTSEL_FUNC(9, 7, 0)
#define FUNC_ETH25G0_MDIO   RCAR_ALTSEL_FUNC(9, 6, 0)
#define FUNC_ETHES4_MATCH   RCAR_ALTSEL_FUNC(9, 5, 0)
#define FUNC_ETHES4_CAPTURE RCAR_ALTSEL_FUNC(9, 4, 0)
#define FUNC_ETHES4_PPS     RCAR_ALTSEL_FUNC(9, 3, 0)
#define FUNC_ETHES0_MATCH   RCAR_ALTSEL_FUNC(9, 2, 0)
#define FUNC_ETHES0_CAPTURE RCAR_ALTSEL_FUNC(9, 1, 0)
#define FUNC_ETHES0_PPS     RCAR_ALTSEL_FUNC(9, 0, 0)

/* GP9 ALTSEL function 1 */
#define FUNC_ETH10G1_PHYINT RCAR_ALTSEL_FUNC(9, 13, 1)
#define FUNC_ETH10G1_LINK   RCAR_ALTSEL_FUNC(9, 12, 1)
#define FUNC_ETH10G1_MDC    RCAR_ALTSEL_FUNC(9, 11, 1)
#define FUNC_ETH10G1_MDIO   RCAR_ALTSEL_FUNC(9, 10, 1)
#define FUNC_ETH25G1_PHYINT RCAR_ALTSEL_FUNC(9, 9, 1)
#define FUNC_ETH25G1_LINK   RCAR_ALTSEL_FUNC(9, 8, 1)
#define FUNC_ETH25G1_MDC    RCAR_ALTSEL_FUNC(9, 7, 1)
#define FUNC_ETH25G1_MDIO   RCAR_ALTSEL_FUNC(9, 6, 1)
#define FUNC_ETHES5_MATCH   RCAR_ALTSEL_FUNC(9, 5, 1)
#define FUNC_ETHES5_CAPTURE RCAR_ALTSEL_FUNC(9, 4, 1)
#define FUNC_ETHES5_PPS     RCAR_ALTSEL_FUNC(9, 3, 1)
#define FUNC_ETHES1_MATCH   RCAR_ALTSEL_FUNC(9, 2, 1)
#define FUNC_ETHES1_CAPTURE RCAR_ALTSEL_FUNC(9, 1, 1)
#define FUNC_ETHES1_PPS     RCAR_ALTSEL_FUNC(9, 0, 1)

/* GP9 ALTSEL function 2 */
#define FUNC_ETH25G2_PHYINT RCAR_ALTSEL_FUNC(9, 9, 2)
#define FUNC_ETH25G2_LINK   RCAR_ALTSEL_FUNC(9, 8, 2)
#define FUNC_ETH25G2_MDC    RCAR_ALTSEL_FUNC(9, 7, 2)
#define FUNC_ETH25G2_MDIO   RCAR_ALTSEL_FUNC(9, 6, 2)
#define FUNC_ETHES6_MATCH   RCAR_ALTSEL_FUNC(9, 5, 2)
#define FUNC_ETHES6_CAPTURE RCAR_ALTSEL_FUNC(9, 4, 2)
#define FUNC_ETHES6_PPS     RCAR_ALTSEL_FUNC(9, 3, 2)
#define FUNC_ETHES2_MATCH   RCAR_ALTSEL_FUNC(9, 2, 2)
#define FUNC_ETHES2_CAPTURE RCAR_ALTSEL_FUNC(9, 1, 2)
#define FUNC_ETHES2_PPS     RCAR_ALTSEL_FUNC(9, 0, 2)

/* GP9 ALTSEL function 3 */
#define FUNC_PWM9_A         RCAR_ALTSEL_FUNC(9, 16, 3)
#define FUNC_PWM8_A         RCAR_ALTSEL_FUNC(9, 15, 3)
#define FUNC_PWM7_A         RCAR_ALTSEL_FUNC(9, 12, 3)
#define FUNC_IRQ3_B         RCAR_ALTSEL_FUNC(9, 11, 3)
#define FUNC_IRQ2_B         RCAR_ALTSEL_FUNC(9, 10, 3)
#define FUNC_PWM6_A         RCAR_ALTSEL_FUNC(9, 8, 3)
#define FUNC_ETHES7_MATCH   RCAR_ALTSEL_FUNC(9, 5, 3)
#define FUNC_ETHES7_CAPTURE RCAR_ALTSEL_FUNC(9, 4, 3)
#define FUNC_ETHES7_PPS     RCAR_ALTSEL_FUNC(9, 3, 3)
#define FUNC_ETHES3_MATCH   RCAR_ALTSEL_FUNC(9, 2, 3)
#define FUNC_ETHES3_CAPTURE RCAR_ALTSEL_FUNC(9, 1, 3)
#define FUNC_ETHES3_PPS     RCAR_ALTSEL_FUNC(9, 0, 3)

/* GP10 ALTSEL function 0 */
#define FUNC_PCIE41_CLKREQ_N RCAR_ALTSEL_FUNC(10, 13, 0)
#define FUNC_PCIE40_CLKREQ_N RCAR_ALTSEL_FUNC(10, 12, 0)
#define FUNC_USB3_VBUS_VALID RCAR_ALTSEL_FUNC(10, 11, 0)
#define FUNC_USB3_OVC        RCAR_ALTSEL_FUNC(10, 10, 0)
#define FUNC_USB3_PWEN       RCAR_ALTSEL_FUNC(10, 9, 0)
#define FUNC_USB2_VBUS_VALID RCAR_ALTSEL_FUNC(10, 8, 0)
#define FUNC_USB2_OVC        RCAR_ALTSEL_FUNC(10, 7, 0)
#define FUNC_USB2_PWEN       RCAR_ALTSEL_FUNC(10, 6, 0)
#define FUNC_USB1_VBUS_VALID RCAR_ALTSEL_FUNC(10, 5, 0)
#define FUNC_USB1_OVC        RCAR_ALTSEL_FUNC(10, 4, 0)
#define FUNC_USB1_PWEN       RCAR_ALTSEL_FUNC(10, 3, 0)
#define FUNC_USB0_VBUS_VALID RCAR_ALTSEL_FUNC(10, 2, 0)
#define FUNC_USB0_OVC        RCAR_ALTSEL_FUNC(10, 1, 0)
#define FUNC_USB0_PWEN       RCAR_ALTSEL_FUNC(10, 0, 0)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A78000_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 BayLibre, SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 22 行

GP0 引脚（Pins）。

### 注释 3：原第 52 行

GP1 引脚（Pins）。

### 注释 4：原第 76 行

GP2 引脚（Pins）。

### 注释 5：原第 107 行

GP3 引脚（Pins）。

### 注释 6：原第 126 行

GP4 引脚（Pins）。

### 注释 7：原第 144 行

GP5 引脚（Pins）。

### 注释 8：原第 169 行

GP6 引脚（Pins）。

### 注释 9：原第 202 行

GP7 引脚（Pins）。

### 注释 10：原第 235 行

GP8 引脚（Pins）。

### 注释 11：原第 259 行

GP9 引脚（Pins）。

### 注释 12：原第 278 行

GP10 引脚（Pins）。

### 注释 13：原第 294 行

GP0 复用选择（ALTSEL）功能 0。

### 注释 14：原第 321 行

GP0 复用选择（ALTSEL）功能 1。

### 注释 15：原第 345 行

GP0 复用选择（ALTSEL）功能 2。

### 注释 16：原第 357 行

GP0 复用选择（ALTSEL）功能 3。

### 注释 17：原第 367 行

GP1 复用选择（ALTSEL）功能 0。

### 注释 18：原第 391 行

GP1 复用选择（ALTSEL）功能 1。

### 注释 19：原第 415 行

GP1 复用选择（ALTSEL）功能 2。

### 注释 20：原第 439 行

GP1 复用选择（ALTSEL）功能 3。

### 注释 21：原第 455 行

GP2 复用选择（ALTSEL）功能 0。

### 注释 22：原第 486 行

GP2 复用选择（ALTSEL）功能 1。

### 注释 23：原第 505 行

GP2 复用选择（ALTSEL）功能 2。

### 注释 24：原第 513 行

GP2 复用选择（ALTSEL）功能 3。

### 注释 25：原第 521 行

GP3 复用选择（ALTSEL）功能 0。

### 注释 26：原第 540 行

GP4 复用选择（ALTSEL）功能 0。

### 注释 27：原第 558 行

GP5 复用选择（ALTSEL）功能 0。

### 注释 28：原第 583 行

GP5 复用选择（ALTSEL）功能 1。

### 注释 29：原第 606 行

GP5 复用选择（ALTSEL）功能 2。

### 注释 30：原第 618 行

GP5 复用选择（ALTSEL）功能 3。

### 注释 31：原第 633 行

GP6 复用选择（ALTSEL）功能 0。

### 注释 32：原第 666 行

GP6 复用选择（ALTSEL）功能 1。

### 注释 33：原第 691 行

GP6 复用选择（ALTSEL）功能 2。

### 注释 34：原第 712 行

GP6 复用选择（ALTSEL）功能 3。

### 注释 35：原第 720 行

GP7 复用选择（ALTSEL）功能 0。

### 注释 36：原第 751 行

GP7 复用选择（ALTSEL）功能 1。

### 注释 37：原第 780 行

GP7 复用选择（ALTSEL）功能 2。

### 注释 38：原第 793 行

GP8 复用选择（ALTSEL）功能 0。

### 注释 39：原第 817 行

GP8 复用选择（ALTSEL）功能 1。

### 注释 40：原第 825 行

GP8 复用选择（ALTSEL）功能 2。

### 注释 41：原第 832 行

GP8 复用选择（ALTSEL）功能 3。

### 注释 42：原第 838 行

GP9 复用选择（ALTSEL）功能 0。

### 注释 43：原第 857 行

GP9 复用选择（ALTSEL）功能 1。

### 注释 44：原第 873 行

GP9 复用选择（ALTSEL）功能 2。

### 注释 45：原第 885 行

GP9 复用选择（ALTSEL）功能 3。

### 注释 46：原第 899 行

GP10 复用选择（ALTSEL）功能 0。

### 注释 47：原第 917 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A78000_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P296_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a78000.h_文件参考.md)
- [pinctrl-rcar-common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h.html)

---

[上一章](P005_loapic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_renesas_rza_clock.h_源码浏览.md)
