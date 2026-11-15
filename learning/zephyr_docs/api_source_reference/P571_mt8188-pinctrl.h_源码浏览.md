---
id: learning.zephyr-docs.api-source-reference.page-571
title: mt8188-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mt8188-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第571章\_mt8188-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mt8188-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mt8188-pinctrl_8h.html)。

## 571.1\_原始可见代码（Source Code）

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
<a id="amtk-common-pinctrl_8h_html"></a>

```c
/*
 * Copyright (c) 2026 MediaTek Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MT8188_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MT8188_PINCTRL_H_

#include <zephyr/dt-bindings/pinctrl/mtk-common-pinctrl.h>

#ifdef __cplusplus
extern "C" {
#endif

#define PINMUX_PIN_0__FUNC_B_GPIO0        (MTK_PIN_NO(0) | 0)
#define PINMUX_PIN_0__FUNC_B0_TP_GPIO0_AO (MTK_PIN_NO(0) | 1)
#define PINMUX_PIN_0__FUNC_O_SPIM5_CSB    (MTK_PIN_NO(0) | 2)
#define PINMUX_PIN_0__FUNC_O_UTXD1        (MTK_PIN_NO(0) | 3)
#define PINMUX_PIN_0__FUNC_O_DMIC3_CLK    (MTK_PIN_NO(0) | 4)
#define PINMUX_PIN_0__FUNC_B0_I2SIN_MCK   (MTK_PIN_NO(0) | 5)
#define PINMUX_PIN_0__FUNC_O_I2SO2_MCK    (MTK_PIN_NO(0) | 6)
#define PINMUX_PIN_0__FUNC_B0_DBG_MON_A0  (MTK_PIN_NO(0) | 7)

#define PINMUX_PIN_1__FUNC_B_GPIO1        (MTK_PIN_NO(1) | 0)
#define PINMUX_PIN_1__FUNC_B0_TP_GPIO1_AO (MTK_PIN_NO(1) | 1)
#define PINMUX_PIN_1__FUNC_O_SPIM5_CLK    (MTK_PIN_NO(1) | 2)
#define PINMUX_PIN_1__FUNC_I1_URXD1       (MTK_PIN_NO(1) | 3)
#define PINMUX_PIN_1__FUNC_I0_DMIC3_DAT   (MTK_PIN_NO(1) | 4)
#define PINMUX_PIN_1__FUNC_B0_I2SIN_BCK   (MTK_PIN_NO(1) | 5)
#define PINMUX_PIN_1__FUNC_B0_I2SO2_BCK   (MTK_PIN_NO(1) | 6)
#define PINMUX_PIN_1__FUNC_B0_DBG_MON_A1  (MTK_PIN_NO(1) | 7)

#define PINMUX_PIN_2__FUNC_B_GPIO2        (MTK_PIN_NO(2) | 0)
#define PINMUX_PIN_2__FUNC_B0_TP_GPIO2_AO (MTK_PIN_NO(2) | 1)
#define PINMUX_PIN_2__FUNC_B0_SPIM5_MOSI  (MTK_PIN_NO(2) | 2)
#define PINMUX_PIN_2__FUNC_O_URTS1        (MTK_PIN_NO(2) | 3)
#define PINMUX_PIN_2__FUNC_I0_DMIC3_DAT_R (MTK_PIN_NO(2) | 4)
#define PINMUX_PIN_2__FUNC_B0_I2SIN_WS    (MTK_PIN_NO(2) | 5)
#define PINMUX_PIN_2__FUNC_B0_I2SO2_WS    (MTK_PIN_NO(2) | 6)
#define PINMUX_PIN_2__FUNC_B0_DBG_MON_A2  (MTK_PIN_NO(2) | 7)

#define PINMUX_PIN_3__FUNC_B_GPIO3        (MTK_PIN_NO(3) | 0)
#define PINMUX_PIN_3__FUNC_B0_TP_GPIO3_AO (MTK_PIN_NO(3) | 1)
#define PINMUX_PIN_3__FUNC_B0_SPIM5_MISO  (MTK_PIN_NO(3) | 2)
#define PINMUX_PIN_3__FUNC_I1_UCTS1       (MTK_PIN_NO(3) | 3)
#define PINMUX_PIN_3__FUNC_O_DMIC4_CLK    (MTK_PIN_NO(3) | 4)
#define PINMUX_PIN_3__FUNC_I0_I2SIN_D0    (MTK_PIN_NO(3) | 5)
#define PINMUX_PIN_3__FUNC_O_I2SO2_D0     (MTK_PIN_NO(3) | 6)
#define PINMUX_PIN_3__FUNC_B0_DBG_MON_A3  (MTK_PIN_NO(3) | 7)

#define PINMUX_PIN_4__FUNC_B_GPIO4        (MTK_PIN_NO(4) | 0)
#define PINMUX_PIN_4__FUNC_B0_TP_GPIO4_AO (MTK_PIN_NO(4) | 1)
#define PINMUX_PIN_4__FUNC_I0_SPDIF_IN2   (MTK_PIN_NO(4) | 2)
#define PINMUX_PIN_4__FUNC_O_I2SO1_MCK    (MTK_PIN_NO(4) | 3)
#define PINMUX_PIN_4__FUNC_I0_DMIC4_DAT   (MTK_PIN_NO(4) | 4)
#define PINMUX_PIN_4__FUNC_I0_I2SIN_D1    (MTK_PIN_NO(4) | 5)
#define PINMUX_PIN_4__FUNC_O_I2SO2_D1     (MTK_PIN_NO(4) | 6)
#define PINMUX_PIN_4__FUNC_B0_DBG_MON_A4  (MTK_PIN_NO(4) | 7)

#define PINMUX_PIN_5__FUNC_B_GPIO5        (MTK_PIN_NO(5) | 0)
#define PINMUX_PIN_5__FUNC_B0_TP_GPIO5_AO (MTK_PIN_NO(5) | 1)
#define PINMUX_PIN_5__FUNC_I0_SPDIF_IN1   (MTK_PIN_NO(5) | 2)
#define PINMUX_PIN_5__FUNC_O_I2SO1_BCK    (MTK_PIN_NO(5) | 3)
#define PINMUX_PIN_5__FUNC_I0_DMIC4_DAT_R (MTK_PIN_NO(5) | 4)
#define PINMUX_PIN_5__FUNC_I0_I2SIN_D2    (MTK_PIN_NO(5) | 5)
#define PINMUX_PIN_5__FUNC_O_I2SO2_D2     (MTK_PIN_NO(5) | 6)
#define PINMUX_PIN_5__FUNC_B0_DBG_MON_A5  (MTK_PIN_NO(5) | 7)

#define PINMUX_PIN_6__FUNC_B_GPIO6         (MTK_PIN_NO(6) | 0)
#define PINMUX_PIN_6__FUNC_B0_TP_GPIO6_AO  (MTK_PIN_NO(6) | 1)
#define PINMUX_PIN_6__FUNC_I0_SPDIF_IN0    (MTK_PIN_NO(6) | 2)
#define PINMUX_PIN_6__FUNC_O_I2SO1_WS      (MTK_PIN_NO(6) | 3)
#define PINMUX_PIN_6__FUNC_O_DMIC1_CLK     (MTK_PIN_NO(6) | 4)
#define PINMUX_PIN_6__FUNC_I0_I2SIN_D3     (MTK_PIN_NO(6) | 5)
#define PINMUX_PIN_6__FUNC_O_I2SO2_D3      (MTK_PIN_NO(6) | 6)
#define PINMUX_PIN_6__FUNC_B0_MD32_0_GPIO0 (MTK_PIN_NO(6) | 7)

#define PINMUX_PIN_7__FUNC_B_GPIO7        (MTK_PIN_NO(7) | 0)
#define PINMUX_PIN_7__FUNC_B0_TP_GPIO7_AO (MTK_PIN_NO(7) | 1)
#define PINMUX_PIN_7__FUNC_O_SPIM3_CSB    (MTK_PIN_NO(7) | 2)
#define PINMUX_PIN_7__FUNC_B0_TDMIN_MCK   (MTK_PIN_NO(7) | 3)
#define PINMUX_PIN_7__FUNC_I0_DMIC1_DAT   (MTK_PIN_NO(7) | 4)
#define PINMUX_PIN_7__FUNC_O_CMVREF0      (MTK_PIN_NO(7) | 5)
#define PINMUX_PIN_7__FUNC_O_CLKM0        (MTK_PIN_NO(7) | 6)
#define PINMUX_PIN_7__FUNC_B0_DBG_MON_A6  (MTK_PIN_NO(7) | 7)

#define PINMUX_PIN_8__FUNC_B_GPIO8        (MTK_PIN_NO(8) | 0)
#define PINMUX_PIN_8__FUNC_B0_TP_GPIO0_AO (MTK_PIN_NO(8) | 1)
#define PINMUX_PIN_8__FUNC_O_SPIM3_CLK    (MTK_PIN_NO(8) | 2)
#define PINMUX_PIN_8__FUNC_B0_TDMIN_BCK   (MTK_PIN_NO(8) | 3)
#define PINMUX_PIN_8__FUNC_I0_DMIC1_DAT_R (MTK_PIN_NO(8) | 4)
#define PINMUX_PIN_8__FUNC_O_CMVREF1      (MTK_PIN_NO(8) | 5)
#define PINMUX_PIN_8__FUNC_O_CLKM1        (MTK_PIN_NO(8) | 6)
#define PINMUX_PIN_8__FUNC_B0_DBG_MON_A7  (MTK_PIN_NO(8) | 7)

#define PINMUX_PIN_9__FUNC_B_GPIO9        (MTK_PIN_NO(9) | 0)
#define PINMUX_PIN_9__FUNC_B0_TP_GPIO1_AO (MTK_PIN_NO(9) | 1)
#define PINMUX_PIN_9__FUNC_B0_SPIM3_MOSI  (MTK_PIN_NO(9) | 2)
#define PINMUX_PIN_9__FUNC_B0_TDMIN_LRCK  (MTK_PIN_NO(9) | 3)
#define PINMUX_PIN_9__FUNC_O_DMIC2_CLK    (MTK_PIN_NO(9) | 4)
#define PINMUX_PIN_9__FUNC_O_CMFLASH0     (MTK_PIN_NO(9) | 5)
#define PINMUX_PIN_9__FUNC_O_PWM_0        (MTK_PIN_NO(9) | 6)
#define PINMUX_PIN_9__FUNC_B0_DBG_MON_A8  (MTK_PIN_NO(9) | 7)

#define PINMUX_PIN_10__FUNC_B_GPIO10       (MTK_PIN_NO(10) | 0)
#define PINMUX_PIN_10__FUNC_B0_TP_GPIO2_AO (MTK_PIN_NO(10) | 1)
#define PINMUX_PIN_10__FUNC_B0_SPIM3_MISO  (MTK_PIN_NO(10) | 2)
#define PINMUX_PIN_10__FUNC_I0_TDMIN_DI    (MTK_PIN_NO(10) | 3)
#define PINMUX_PIN_10__FUNC_I0_DMIC2_DAT   (MTK_PIN_NO(10) | 4)
#define PINMUX_PIN_10__FUNC_O_CMFLASH1     (MTK_PIN_NO(10) | 5)
#define PINMUX_PIN_10__FUNC_O_PWM_1        (MTK_PIN_NO(10) | 6)
#define PINMUX_PIN_10__FUNC_B0_DBG_MON_A9  (MTK_PIN_NO(10) | 7)

#define PINMUX_PIN_11__FUNC_B_GPIO11          (MTK_PIN_NO(11) | 0)
#define PINMUX_PIN_11__FUNC_B0_TP_GPIO3_AO    (MTK_PIN_NO(11) | 1)
#define PINMUX_PIN_11__FUNC_O_SPDIF_OUT       (MTK_PIN_NO(11) | 2)
#define PINMUX_PIN_11__FUNC_O_I2SO1_D0        (MTK_PIN_NO(11) | 3)
#define PINMUX_PIN_11__FUNC_I0_DMIC2_DAT_R    (MTK_PIN_NO(11) | 4)
#define PINMUX_PIN_11__FUNC_I0_DVFSRC_EXT_REQ (MTK_PIN_NO(11) | 5)
#define PINMUX_PIN_11__FUNC_O_CMVREF6         (MTK_PIN_NO(11) | 6)
#define PINMUX_PIN_11__FUNC_B0_DBG_MON_A10    (MTK_PIN_NO(11) | 7)

#define PINMUX_PIN_12__FUNC_B_GPIO12          (MTK_PIN_NO(12) | 0)
#define PINMUX_PIN_12__FUNC_B0_TP_GPIO4_AO    (MTK_PIN_NO(12) | 1)
#define PINMUX_PIN_12__FUNC_O_SPIM4_CSB       (MTK_PIN_NO(12) | 2)
#define PINMUX_PIN_12__FUNC_B1_JTMS_SEL3      (MTK_PIN_NO(12) | 3)
#define PINMUX_PIN_12__FUNC_B1_APU_JTAG_TMS   (MTK_PIN_NO(12) | 4)
#define PINMUX_PIN_12__FUNC_I0_VPU_UDI_TMS    (MTK_PIN_NO(12) | 5)
#define PINMUX_PIN_12__FUNC_I0_IPU_JTAG_TMS   (MTK_PIN_NO(12) | 6)
#define PINMUX_PIN_12__FUNC_I0_HDMITX20_HTPLG (MTK_PIN_NO(12) | 7)

#define PINMUX_PIN_13__FUNC_B_GPIO13        (MTK_PIN_NO(13) | 0)
#define PINMUX_PIN_13__FUNC_B0_TP_GPIO5_AO  (MTK_PIN_NO(13) | 1)
#define PINMUX_PIN_13__FUNC_O_SPIM4_CLK     (MTK_PIN_NO(13) | 2)
#define PINMUX_PIN_13__FUNC_I0_JTCK_SEL3    (MTK_PIN_NO(13) | 3)
#define PINMUX_PIN_13__FUNC_I0_APU_JTAG_TCK (MTK_PIN_NO(13) | 4)
#define PINMUX_PIN_13__FUNC_I0_VPU_UDI_TCK  (MTK_PIN_NO(13) | 5)
#define PINMUX_PIN_13__FUNC_I0_IPU_JTAG_TCK (MTK_PIN_NO(13) | 6)
#define PINMUX_PIN_13__FUNC_B1_HDMITX20_CEC (MTK_PIN_NO(13) | 7)

#define PINMUX_PIN_14__FUNC_B_GPIO14        (MTK_PIN_NO(14) | 0)
#define PINMUX_PIN_14__FUNC_B0_TP_GPIO6_AO  (MTK_PIN_NO(14) | 1)
#define PINMUX_PIN_14__FUNC_B0_SPIM4_MOSI   (MTK_PIN_NO(14) | 2)
#define PINMUX_PIN_14__FUNC_I1_JTDI_SEL3    (MTK_PIN_NO(14) | 3)
#define PINMUX_PIN_14__FUNC_I1_APU_JTAG_TDI (MTK_PIN_NO(14) | 4)
#define PINMUX_PIN_14__FUNC_I0_VPU_UDI_TDI  (MTK_PIN_NO(14) | 5)
#define PINMUX_PIN_14__FUNC_I0_IPU_JTAG_TDI (MTK_PIN_NO(14) | 6)
#define PINMUX_PIN_14__FUNC_B1_HDMITX20_SCL (MTK_PIN_NO(14) | 7)

#define PINMUX_PIN_15__FUNC_B_GPIO15        (MTK_PIN_NO(15) | 0)
#define PINMUX_PIN_15__FUNC_B0_TP_GPIO7_AO  (MTK_PIN_NO(15) | 1)
#define PINMUX_PIN_15__FUNC_B0_SPIM4_MISO   (MTK_PIN_NO(15) | 2)
#define PINMUX_PIN_15__FUNC_O_JTDO_SEL3     (MTK_PIN_NO(15) | 3)
#define PINMUX_PIN_15__FUNC_O_APU_JTAG_TDO  (MTK_PIN_NO(15) | 4)
#define PINMUX_PIN_15__FUNC_O_VPU_UDI_TDO   (MTK_PIN_NO(15) | 5)
#define PINMUX_PIN_15__FUNC_O_IPU_JTAG_TDO  (MTK_PIN_NO(15) | 6)
#define PINMUX_PIN_15__FUNC_B1_HDMITX20_SDA (MTK_PIN_NO(15) | 7)

#define PINMUX_PIN_16__FUNC_B_GPIO16         (MTK_PIN_NO(16) | 0)
#define PINMUX_PIN_16__FUNC_B0_TP_GPIO0_AO   (MTK_PIN_NO(16) | 1)
#define PINMUX_PIN_16__FUNC_O_UTXD3          (MTK_PIN_NO(16) | 2)
#define PINMUX_PIN_16__FUNC_I1_JTRSTn_SEL3   (MTK_PIN_NO(16) | 3)
#define PINMUX_PIN_16__FUNC_I0_APU_JTAG_TRST (MTK_PIN_NO(16) | 4)
#define PINMUX_PIN_16__FUNC_I0_VPU_UDI_NTRST (MTK_PIN_NO(16) | 5)
#define PINMUX_PIN_16__FUNC_I0_IPU_JTAG_TRST (MTK_PIN_NO(16) | 6)
#define PINMUX_PIN_16__FUNC_O_HDMITX20_PWR5V (MTK_PIN_NO(16) | 7)

#define PINMUX_PIN_17__FUNC_B_GPIO17          (MTK_PIN_NO(17) | 0)
#define PINMUX_PIN_17__FUNC_B0_TP_GPIO1_AO    (MTK_PIN_NO(17) | 1)
#define PINMUX_PIN_17__FUNC_I1_URXD3          (MTK_PIN_NO(17) | 2)
#define PINMUX_PIN_17__FUNC_O_CMFLASH2        (MTK_PIN_NO(17) | 3)
#define PINMUX_PIN_17__FUNC_I0_EDP_TX_HPD     (MTK_PIN_NO(17) | 4)
#define PINMUX_PIN_17__FUNC_I0_DVFSRC_EXT_REQ (MTK_PIN_NO(17) | 5)
#define PINMUX_PIN_17__FUNC_O_CMVREF7         (MTK_PIN_NO(17) | 6)
#define PINMUX_PIN_17__FUNC_B0_MD32_0_GPIO1   (MTK_PIN_NO(17) | 7)

#define PINMUX_PIN_18__FUNC_B_GPIO18       (MTK_PIN_NO(18) | 0)
#define PINMUX_PIN_18__FUNC_B0_TP_GPIO2_AO (MTK_PIN_NO(18) | 1)
#define PINMUX_PIN_18__FUNC_O_CMFLASH0     (MTK_PIN_NO(18) | 2)
#define PINMUX_PIN_18__FUNC_O_CMVREF4      (MTK_PIN_NO(18) | 3)
#define PINMUX_PIN_18__FUNC_B0_TDMIN_MCK   (MTK_PIN_NO(18) | 4)
#define PINMUX_PIN_18__FUNC_O_UTXD1        (MTK_PIN_NO(18) | 5)
#define PINMUX_PIN_18__FUNC_O_TP_UTXD1_AO  (MTK_PIN_NO(18) | 6)
#define PINMUX_PIN_18__FUNC_B0_DBG_MON_A11 (MTK_PIN_NO(18) | 7)

#define PINMUX_PIN_19__FUNC_B_GPIO19       (MTK_PIN_NO(19) | 0)
#define PINMUX_PIN_19__FUNC_B0_TP_GPIO3_AO (MTK_PIN_NO(19) | 1)
#define PINMUX_PIN_19__FUNC_O_CMFLASH1     (MTK_PIN_NO(19) | 2)
#define PINMUX_PIN_19__FUNC_O_CMVREF5      (MTK_PIN_NO(19) | 3)
#define PINMUX_PIN_19__FUNC_B0_TDMIN_BCK   (MTK_PIN_NO(19) | 4)
#define PINMUX_PIN_19__FUNC_I1_URXD1       (MTK_PIN_NO(19) | 5)
#define PINMUX_PIN_19__FUNC_I1_TP_URXD1_AO (MTK_PIN_NO(19) | 6)
#define PINMUX_PIN_19__FUNC_B0_DBG_MON_A12 (MTK_PIN_NO(19) | 7)

#define PINMUX_PIN_20__FUNC_B_GPIO20       (MTK_PIN_NO(20) | 0)
#define PINMUX_PIN_20__FUNC_B0_TP_GPIO4_AO (MTK_PIN_NO(20) | 1)
#define PINMUX_PIN_20__FUNC_O_CMFLASH2     (MTK_PIN_NO(20) | 2)
#define PINMUX_PIN_20__FUNC_O_CLKM2        (MTK_PIN_NO(20) | 3)
#define PINMUX_PIN_20__FUNC_B0_TDMIN_LRCK  (MTK_PIN_NO(20) | 4)
#define PINMUX_PIN_20__FUNC_O_URTS1        (MTK_PIN_NO(20) | 5)
#define PINMUX_PIN_20__FUNC_O_TP_URTS1_AO  (MTK_PIN_NO(20) | 6)
#define PINMUX_PIN_20__FUNC_B0_DBG_MON_A13 (MTK_PIN_NO(20) | 7)

#define PINMUX_PIN_21__FUNC_B_GPIO21       (MTK_PIN_NO(21) | 0)
#define PINMUX_PIN_21__FUNC_B0_TP_GPIO5_AO (MTK_PIN_NO(21) | 1)
#define PINMUX_PIN_21__FUNC_O_CMFLASH3     (MTK_PIN_NO(21) | 2)
#define PINMUX_PIN_21__FUNC_O_CLKM3        (MTK_PIN_NO(21) | 3)
#define PINMUX_PIN_21__FUNC_I0_TDMIN_DI    (MTK_PIN_NO(21) | 4)
#define PINMUX_PIN_21__FUNC_I1_UCTS1       (MTK_PIN_NO(21) | 5)
#define PINMUX_PIN_21__FUNC_I1_TP_UCTS1_AO (MTK_PIN_NO(21) | 6)
#define PINMUX_PIN_21__FUNC_B0_DBG_MON_A14 (MTK_PIN_NO(21) | 7)

#define PINMUX_PIN_22__FUNC_B_GPIO22       (MTK_PIN_NO(22) | 0)
#define PINMUX_PIN_22__FUNC_O_CMMCLK0      (MTK_PIN_NO(22) | 1)
#define PINMUX_PIN_22__FUNC_B0_TP_GPIO6_AO (MTK_PIN_NO(22) | 5)
#define PINMUX_PIN_22__FUNC_B0_DBG_MON_A15 (MTK_PIN_NO(22) | 7)

#define PINMUX_PIN_23__FUNC_B_GPIO23            (MTK_PIN_NO(23) | 0)
#define PINMUX_PIN_23__FUNC_O_CMMCLK1           (MTK_PIN_NO(23) | 1)
#define PINMUX_PIN_23__FUNC_O_PWM_2             (MTK_PIN_NO(23) | 3)
#define PINMUX_PIN_23__FUNC_B1_PCIE_PHY_I2C_SCL (MTK_PIN_NO(23) | 4)
#define PINMUX_PIN_23__FUNC_B0_TP_GPIO7_AO      (MTK_PIN_NO(23) | 5)
#define PINMUX_PIN_23__FUNC_I0_DP_TX_HPD        (MTK_PIN_NO(23) | 6)
#define PINMUX_PIN_23__FUNC_B0_DBG_MON_A16      (MTK_PIN_NO(23) | 7)

#define PINMUX_PIN_24__FUNC_B_GPIO24            (MTK_PIN_NO(24) | 0)
#define PINMUX_PIN_24__FUNC_O_CMMCLK2           (MTK_PIN_NO(24) | 1)
#define PINMUX_PIN_24__FUNC_O_PWM_3             (MTK_PIN_NO(24) | 3)
#define PINMUX_PIN_24__FUNC_B1_PCIE_PHY_I2C_SDA (MTK_PIN_NO(24) | 4)
#define PINMUX_PIN_24__FUNC_I0_DVFSRC_EXT_REQ   (MTK_PIN_NO(24) | 5)
#define PINMUX_PIN_24__FUNC_I0_EDP_TX_HPD       (MTK_PIN_NO(24) | 6)
#define PINMUX_PIN_24__FUNC_B0_MD32_0_GPIO2     (MTK_PIN_NO(24) | 7)

#define PINMUX_PIN_25__FUNC_B_GPIO25     (MTK_PIN_NO(25) | 0)
#define PINMUX_PIN_25__FUNC_O_LCM_RST    (MTK_PIN_NO(25) | 1)
#define PINMUX_PIN_25__FUNC_O_LCM1_RST   (MTK_PIN_NO(25) | 2)
#define PINMUX_PIN_25__FUNC_I0_DP_TX_HPD (MTK_PIN_NO(25) | 3)

#define PINMUX_PIN_26__FUNC_B_GPIO26      (MTK_PIN_NO(26) | 0)
#define PINMUX_PIN_26__FUNC_I0_DSI_TE     (MTK_PIN_NO(26) | 1)
#define PINMUX_PIN_26__FUNC_I0_DSI1_TE    (MTK_PIN_NO(26) | 2)
#define PINMUX_PIN_26__FUNC_I0_EDP_TX_HPD (MTK_PIN_NO(26) | 3)

#define PINMUX_PIN_27__FUNC_B_GPIO27               (MTK_PIN_NO(27) | 0)
#define PINMUX_PIN_27__FUNC_O_LCM1_RST             (MTK_PIN_NO(27) | 1)
#define PINMUX_PIN_27__FUNC_O_LCM_RST              (MTK_PIN_NO(27) | 2)
#define PINMUX_PIN_27__FUNC_I0_DP_TX_HPD           (MTK_PIN_NO(27) | 3)
#define PINMUX_PIN_27__FUNC_O_CMVREF2              (MTK_PIN_NO(27) | 4)
#define PINMUX_PIN_27__FUNC_O_mbistwriteen_trigger (MTK_PIN_NO(27) | 5)
#define PINMUX_PIN_27__FUNC_O_PWM_2                (MTK_PIN_NO(27) | 6)
#define PINMUX_PIN_27__FUNC_B0_DBG_MON_A17         (MTK_PIN_NO(27) | 7)

#define PINMUX_PIN_28__FUNC_B_GPIO28              (MTK_PIN_NO(28) | 0)
#define PINMUX_PIN_28__FUNC_I0_DSI1_TE            (MTK_PIN_NO(28) | 1)
#define PINMUX_PIN_28__FUNC_I0_DSI_TE             (MTK_PIN_NO(28) | 2)
#define PINMUX_PIN_28__FUNC_I0_EDP_TX_HPD         (MTK_PIN_NO(28) | 3)
#define PINMUX_PIN_28__FUNC_O_CMVREF3             (MTK_PIN_NO(28) | 4)
#define PINMUX_PIN_28__FUNC_O_mbistreaden_trigger (MTK_PIN_NO(28) | 5)
#define PINMUX_PIN_28__FUNC_O_PWM_3               (MTK_PIN_NO(28) | 6)
#define PINMUX_PIN_28__FUNC_B0_DBG_MON_A18        (MTK_PIN_NO(28) | 7)

#define PINMUX_PIN_29__FUNC_B_GPIO29    (MTK_PIN_NO(29) | 0)
#define PINMUX_PIN_29__FUNC_O_DISP_PWM0 (MTK_PIN_NO(29) | 1)
#define PINMUX_PIN_29__FUNC_O_DISP_PWM1 (MTK_PIN_NO(29) | 2)

#define PINMUX_PIN_30__FUNC_B_GPIO30       (MTK_PIN_NO(30) | 0)
#define PINMUX_PIN_30__FUNC_O_DISP_PWM1    (MTK_PIN_NO(30) | 1)
#define PINMUX_PIN_30__FUNC_O_DISP_PWM0    (MTK_PIN_NO(30) | 2)
#define PINMUX_PIN_30__FUNC_O_CMFLASH3     (MTK_PIN_NO(30) | 3)
#define PINMUX_PIN_30__FUNC_O_PWM_1        (MTK_PIN_NO(30) | 4)
#define PINMUX_PIN_30__FUNC_B0_DBG_MON_A19 (MTK_PIN_NO(30) | 7)

#define PINMUX_PIN_31__FUNC_B_GPIO31       (MTK_PIN_NO(31) | 0)
#define PINMUX_PIN_31__FUNC_O_UTXD0        (MTK_PIN_NO(31) | 1)
#define PINMUX_PIN_31__FUNC_O_TP_UTXD1_AO  (MTK_PIN_NO(31) | 2)
#define PINMUX_PIN_31__FUNC_O_ADSP_UTXD0   (MTK_PIN_NO(31) | 3)
#define PINMUX_PIN_31__FUNC_O_TP_UTXD2_AO  (MTK_PIN_NO(31) | 4)
#define PINMUX_PIN_31__FUNC_O_MD32_0_TXD   (MTK_PIN_NO(31) | 5)
#define PINMUX_PIN_31__FUNC_O_MD32_1_TXD   (MTK_PIN_NO(31) | 6)
#define PINMUX_PIN_31__FUNC_O_SSPM_UTXD_AO (MTK_PIN_NO(31) | 7)

#define PINMUX_PIN_32__FUNC_B_GPIO32        (MTK_PIN_NO(32) | 0)
#define PINMUX_PIN_32__FUNC_I1_URXD0        (MTK_PIN_NO(32) | 1)
#define PINMUX_PIN_32__FUNC_I1_TP_URXD1_AO  (MTK_PIN_NO(32) | 2)
#define PINMUX_PIN_32__FUNC_I1_ADSP_URXD0   (MTK_PIN_NO(32) | 3)
#define PINMUX_PIN_32__FUNC_I1_TP_URXD2_AO  (MTK_PIN_NO(32) | 4)
#define PINMUX_PIN_32__FUNC_I1_MD32_0_RXD   (MTK_PIN_NO(32) | 5)
#define PINMUX_PIN_32__FUNC_I1_MD32_1_RXD   (MTK_PIN_NO(32) | 6)
#define PINMUX_PIN_32__FUNC_I1_SSPM_URXD_AO (MTK_PIN_NO(32) | 7)

#define PINMUX_PIN_33__FUNC_B_GPIO33               (MTK_PIN_NO(33) | 0)
#define PINMUX_PIN_33__FUNC_O_UTXD1                (MTK_PIN_NO(33) | 1)
#define PINMUX_PIN_33__FUNC_O_URTS2                (MTK_PIN_NO(33) | 2)
#define PINMUX_PIN_33__FUNC_O_ADSP_UTXD0           (MTK_PIN_NO(33) | 3)
#define PINMUX_PIN_33__FUNC_O_TP_UTXD1_AO          (MTK_PIN_NO(33) | 4)
#define PINMUX_PIN_33__FUNC_O_mbistwriteen_trigger (MTK_PIN_NO(33) | 5)
#define PINMUX_PIN_33__FUNC_O_MD32_0_TXD           (MTK_PIN_NO(33) | 6)
#define PINMUX_PIN_33__FUNC_O_SSPM_UTXD_AO         (MTK_PIN_NO(33) | 7)

#define PINMUX_PIN_34__FUNC_B_GPIO34              (MTK_PIN_NO(34) | 0)
#define PINMUX_PIN_34__FUNC_I1_URXD1              (MTK_PIN_NO(34) | 1)
#define PINMUX_PIN_34__FUNC_I1_UCTS2              (MTK_PIN_NO(34) | 2)
#define PINMUX_PIN_34__FUNC_I1_ADSP_URXD0         (MTK_PIN_NO(34) | 3)
#define PINMUX_PIN_34__FUNC_I1_TP_URXD1_AO        (MTK_PIN_NO(34) | 4)
#define PINMUX_PIN_34__FUNC_O_mbistreaden_trigger (MTK_PIN_NO(34) | 5)
#define PINMUX_PIN_34__FUNC_I1_MD32_0_RXD         (MTK_PIN_NO(34) | 6)
#define PINMUX_PIN_34__FUNC_I1_SSPM_URXD_AO       (MTK_PIN_NO(34) | 7)

#define PINMUX_PIN_35__FUNC_B_GPIO35       (MTK_PIN_NO(35) | 0)
#define PINMUX_PIN_35__FUNC_O_UTXD2        (MTK_PIN_NO(35) | 1)
#define PINMUX_PIN_35__FUNC_O_URTS1        (MTK_PIN_NO(35) | 2)
#define PINMUX_PIN_35__FUNC_O_ADSP_UTXD0   (MTK_PIN_NO(35) | 3)
#define PINMUX_PIN_35__FUNC_O_TP_URTS1_AO  (MTK_PIN_NO(35) | 4)
#define PINMUX_PIN_35__FUNC_O_TP_UTXD2_AO  (MTK_PIN_NO(35) | 5)
#define PINMUX_PIN_35__FUNC_O_MD32_1_TXD   (MTK_PIN_NO(35) | 6)
#define PINMUX_PIN_35__FUNC_B0_DBG_MON_A20 (MTK_PIN_NO(35) | 7)

#define PINMUX_PIN_36__FUNC_B_GPIO36       (MTK_PIN_NO(36) | 0)
#define PINMUX_PIN_36__FUNC_I1_URXD2       (MTK_PIN_NO(36) | 1)
#define PINMUX_PIN_36__FUNC_I1_UCTS1       (MTK_PIN_NO(36) | 2)
#define PINMUX_PIN_36__FUNC_I1_ADSP_URXD0  (MTK_PIN_NO(36) | 3)
#define PINMUX_PIN_36__FUNC_I1_TP_UCTS1_AO (MTK_PIN_NO(36) | 4)
#define PINMUX_PIN_36__FUNC_I1_TP_URXD2_AO (MTK_PIN_NO(36) | 5)
#define PINMUX_PIN_36__FUNC_I1_MD32_1_RXD  (MTK_PIN_NO(36) | 6)
#define PINMUX_PIN_36__FUNC_B0_DBG_MON_A21 (MTK_PIN_NO(36) | 7)

#define PINMUX_PIN_37__FUNC_B_GPIO37          (MTK_PIN_NO(37) | 0)
#define PINMUX_PIN_37__FUNC_B1_JTMS_SEL1      (MTK_PIN_NO(37) | 1)
#define PINMUX_PIN_37__FUNC_I0_UDI_TMS        (MTK_PIN_NO(37) | 2)
#define PINMUX_PIN_37__FUNC_I1_SPM_JTAG_TMS   (MTK_PIN_NO(37) | 3)
#define PINMUX_PIN_37__FUNC_I1_ADSP_JTAG0_TMS (MTK_PIN_NO(37) | 4)
#define PINMUX_PIN_37__FUNC_I1_SCP_JTAG0_TMS  (MTK_PIN_NO(37) | 5)
#define PINMUX_PIN_37__FUNC_I1_CCU0_JTAG_TMS  (MTK_PIN_NO(37) | 6)
#define PINMUX_PIN_37__FUNC_I1_MCUPM_JTAG_TMS (MTK_PIN_NO(37) | 7)

#define PINMUX_PIN_38__FUNC_B_GPIO38          (MTK_PIN_NO(38) | 0)
#define PINMUX_PIN_38__FUNC_I0_JTCK_SEL1      (MTK_PIN_NO(38) | 1)
#define PINMUX_PIN_38__FUNC_I0_UDI_TCK        (MTK_PIN_NO(38) | 2)
#define PINMUX_PIN_38__FUNC_I1_SPM_JTAG_TCK   (MTK_PIN_NO(38) | 3)
#define PINMUX_PIN_38__FUNC_I0_ADSP_JTAG0_TCK (MTK_PIN_NO(38) | 4)
#define PINMUX_PIN_38__FUNC_I1_SCP_JTAG0_TCK  (MTK_PIN_NO(38) | 5)
#define PINMUX_PIN_38__FUNC_I1_CCU0_JTAG_TCK  (MTK_PIN_NO(38) | 6)
#define PINMUX_PIN_38__FUNC_I1_MCUPM_JTAG_TCK (MTK_PIN_NO(38) | 7)

#define PINMUX_PIN_39__FUNC_B_GPIO39          (MTK_PIN_NO(39) | 0)
#define PINMUX_PIN_39__FUNC_I1_JTDI_SEL1      (MTK_PIN_NO(39) | 1)
#define PINMUX_PIN_39__FUNC_I0_UDI_TDI        (MTK_PIN_NO(39) | 2)
#define PINMUX_PIN_39__FUNC_I1_SPM_JTAG_TDI   (MTK_PIN_NO(39) | 3)
#define PINMUX_PIN_39__FUNC_I1_ADSP_JTAG0_TDI (MTK_PIN_NO(39) | 4)
#define PINMUX_PIN_39__FUNC_I1_SCP_JTAG0_TDI  (MTK_PIN_NO(39) | 5)
#define PINMUX_PIN_39__FUNC_I1_CCU0_JTAG_TDI  (MTK_PIN_NO(39) | 6)
#define PINMUX_PIN_39__FUNC_I1_MCUPM_JTAG_TDI (MTK_PIN_NO(39) | 7)

#define PINMUX_PIN_40__FUNC_B_GPIO40         (MTK_PIN_NO(40) | 0)
#define PINMUX_PIN_40__FUNC_O_JTDO_SEL1      (MTK_PIN_NO(40) | 1)
#define PINMUX_PIN_40__FUNC_O_UDI_TDO        (MTK_PIN_NO(40) | 2)
#define PINMUX_PIN_40__FUNC_O_SPM_JTAG_TDO   (MTK_PIN_NO(40) | 3)
#define PINMUX_PIN_40__FUNC_O_ADSP_JTAG0_TDO (MTK_PIN_NO(40) | 4)
#define PINMUX_PIN_40__FUNC_O_SCP_JTAG0_TDO  (MTK_PIN_NO(40) | 5)
#define PINMUX_PIN_40__FUNC_O_CCU0_JTAG_TDO  (MTK_PIN_NO(40) | 6)
#define PINMUX_PIN_40__FUNC_O_MCUPM_JTAG_TDO (MTK_PIN_NO(40) | 7)

#define PINMUX_PIN_41__FUNC_B_GPIO41            (MTK_PIN_NO(41) | 0)
#define PINMUX_PIN_41__FUNC_I1_JTRSTn_SEL1      (MTK_PIN_NO(41) | 1)
#define PINMUX_PIN_41__FUNC_I0_UDI_NTRST        (MTK_PIN_NO(41) | 2)
#define PINMUX_PIN_41__FUNC_I0_SPM_JTAG_TRSTN   (MTK_PIN_NO(41) | 3)
#define PINMUX_PIN_41__FUNC_I1_ADSP_JTAG0_TRSTN (MTK_PIN_NO(41) | 4)
#define PINMUX_PIN_41__FUNC_I0_SCP_JTAG0_TRSTN  (MTK_PIN_NO(41) | 5)
#define PINMUX_PIN_41__FUNC_I1_CCU0_JTAG_TRST   (MTK_PIN_NO(41) | 6)
#define PINMUX_PIN_41__FUNC_I0_MCUPM_JTAG_TRSTN (MTK_PIN_NO(41) | 7)

#define PINMUX_PIN_42__FUNC_B_GPIO42  (MTK_PIN_NO(42) | 0)
#define PINMUX_PIN_42__FUNC_B1_KPCOL0 (MTK_PIN_NO(42) | 1)

#define PINMUX_PIN_43__FUNC_B_GPIO43               (MTK_PIN_NO(43) | 0)
#define PINMUX_PIN_43__FUNC_B1_KPCOL1              (MTK_PIN_NO(43) | 1)
#define PINMUX_PIN_43__FUNC_I0_DP_TX_HPD           (MTK_PIN_NO(43) | 2)
#define PINMUX_PIN_43__FUNC_O_CMFLASH2             (MTK_PIN_NO(43) | 3)
#define PINMUX_PIN_43__FUNC_I0_DVFSRC_EXT_REQ      (MTK_PIN_NO(43) | 4)
#define PINMUX_PIN_43__FUNC_O_mbistwriteen_trigger (MTK_PIN_NO(43) | 7)

#define PINMUX_PIN_44__FUNC_B_GPIO44  (MTK_PIN_NO(44) | 0)
#define PINMUX_PIN_44__FUNC_B1_KPROW0 (MTK_PIN_NO(44) | 1)

#define PINMUX_PIN_45__FUNC_B_GPIO45              (MTK_PIN_NO(45) | 0)
#define PINMUX_PIN_45__FUNC_B1_KPROW1             (MTK_PIN_NO(45) | 1)
#define PINMUX_PIN_45__FUNC_I0_EDP_TX_HPD         (MTK_PIN_NO(45) | 2)
#define PINMUX_PIN_45__FUNC_O_CMFLASH3            (MTK_PIN_NO(45) | 3)
#define PINMUX_PIN_45__FUNC_B0_I2SIN_MCK          (MTK_PIN_NO(45) | 4)
#define PINMUX_PIN_45__FUNC_O_mbistreaden_trigger (MTK_PIN_NO(45) | 7)

#define PINMUX_PIN_46__FUNC_B_GPIO46        (MTK_PIN_NO(46) | 0)
#define PINMUX_PIN_46__FUNC_I0_DP_TX_HPD    (MTK_PIN_NO(46) | 1)
#define PINMUX_PIN_46__FUNC_O_PWM_0         (MTK_PIN_NO(46) | 2)
#define PINMUX_PIN_46__FUNC_I0_VBUSVALID_2P (MTK_PIN_NO(46) | 3)
#define PINMUX_PIN_46__FUNC_B0_DBG_MON_A22  (MTK_PIN_NO(46) | 7)

#define PINMUX_PIN_47__FUNC_B_GPIO47          (MTK_PIN_NO(47) | 0)
#define PINMUX_PIN_47__FUNC_I1_WAKEN          (MTK_PIN_NO(47) | 1)
#define PINMUX_PIN_47__FUNC_O_GDU_TROOPS_DET0 (MTK_PIN_NO(47) | 6)

#define PINMUX_PIN_48__FUNC_B_GPIO48          (MTK_PIN_NO(48) | 0)
#define PINMUX_PIN_48__FUNC_O_PERSTN          (MTK_PIN_NO(48) | 1)
#define PINMUX_PIN_48__FUNC_O_GDU_TROOPS_DET1 (MTK_PIN_NO(48) | 6)

#define PINMUX_PIN_49__FUNC_B_GPIO49          (MTK_PIN_NO(49) | 0)
#define PINMUX_PIN_49__FUNC_B1_CLKREQN        (MTK_PIN_NO(49) | 1)
#define PINMUX_PIN_49__FUNC_O_GDU_TROOPS_DET2 (MTK_PIN_NO(49) | 6)

#define PINMUX_PIN_50__FUNC_B_GPIO50           (MTK_PIN_NO(50) | 0)
#define PINMUX_PIN_50__FUNC_O_HDMITX20_PWR5V   (MTK_PIN_NO(50) | 1)
#define PINMUX_PIN_50__FUNC_I1_IDDIG_1P        (MTK_PIN_NO(50) | 3)
#define PINMUX_PIN_50__FUNC_I1_SCP_JTAG1_TMS   (MTK_PIN_NO(50) | 4)
#define PINMUX_PIN_50__FUNC_I1_SSPM_JTAG_TMS   (MTK_PIN_NO(50) | 5)
#define PINMUX_PIN_50__FUNC_I1_MD32_0_JTAG_TMS (MTK_PIN_NO(50) | 6)
#define PINMUX_PIN_50__FUNC_I1_MD32_1_JTAG_TMS (MTK_PIN_NO(50) | 7)

#define PINMUX_PIN_51__FUNC_B_GPIO51           (MTK_PIN_NO(51) | 0)
#define PINMUX_PIN_51__FUNC_I0_HDMITX20_HTPLG  (MTK_PIN_NO(51) | 1)
#define PINMUX_PIN_51__FUNC_I0_EDP_TX_HPD      (MTK_PIN_NO(51) | 2)
#define PINMUX_PIN_51__FUNC_O_USB_DRVVBUS_1P   (MTK_PIN_NO(51) | 3)
#define PINMUX_PIN_51__FUNC_I1_SCP_JTAG1_TCK   (MTK_PIN_NO(51) | 4)
#define PINMUX_PIN_51__FUNC_I1_SSPM_JTAG_TCK   (MTK_PIN_NO(51) | 5)
#define PINMUX_PIN_51__FUNC_I1_MD32_0_JTAG_TCK (MTK_PIN_NO(51) | 6)
#define PINMUX_PIN_51__FUNC_I1_MD32_1_JTAG_TCK (MTK_PIN_NO(51) | 7)

#define PINMUX_PIN_52__FUNC_B_GPIO52           (MTK_PIN_NO(52) | 0)
#define PINMUX_PIN_52__FUNC_B1_HDMITX20_CEC    (MTK_PIN_NO(52) | 1)
#define PINMUX_PIN_52__FUNC_I0_VBUSVALID_1P    (MTK_PIN_NO(52) | 3)
#define PINMUX_PIN_52__FUNC_I1_SCP_JTAG1_TDI   (MTK_PIN_NO(52) | 4)
#define PINMUX_PIN_52__FUNC_I1_SSPM_JTAG_TDI   (MTK_PIN_NO(52) | 5)
#define PINMUX_PIN_52__FUNC_I1_MD32_0_JTAG_TDI (MTK_PIN_NO(52) | 6)
#define PINMUX_PIN_52__FUNC_I1_MD32_1_JTAG_TDI (MTK_PIN_NO(52) | 7)

#define PINMUX_PIN_53__FUNC_B_GPIO53          (MTK_PIN_NO(53) | 0)
#define PINMUX_PIN_53__FUNC_B1_HDMITX20_SCL   (MTK_PIN_NO(53) | 1)
#define PINMUX_PIN_53__FUNC_I1_IDDIG_2P       (MTK_PIN_NO(53) | 3)
#define PINMUX_PIN_53__FUNC_O_SCP_JTAG1_TDO   (MTK_PIN_NO(53) | 4)
#define PINMUX_PIN_53__FUNC_O_SSPM_JTAG_TDO   (MTK_PIN_NO(53) | 5)
#define PINMUX_PIN_53__FUNC_O_MD32_0_JTAG_TDO (MTK_PIN_NO(53) | 6)
#define PINMUX_PIN_53__FUNC_O_MD32_1_JTAG_TDO (MTK_PIN_NO(53) | 7)

#define PINMUX_PIN_54__FUNC_B_GPIO54            (MTK_PIN_NO(54) | 0)
#define PINMUX_PIN_54__FUNC_B1_HDMITX20_SDA     (MTK_PIN_NO(54) | 1)
#define PINMUX_PIN_54__FUNC_O_USB_DRVVBUS_2P    (MTK_PIN_NO(54) | 3)
#define PINMUX_PIN_54__FUNC_I0_SCP_JTAG1_TRSTN  (MTK_PIN_NO(54) | 4)
#define PINMUX_PIN_54__FUNC_I0_SSPM_JTAG_TRSTN  (MTK_PIN_NO(54) | 5)
#define PINMUX_PIN_54__FUNC_I1_MD32_0_JTAG_TRST (MTK_PIN_NO(54) | 6)
#define PINMUX_PIN_54__FUNC_I1_MD32_1_JTAG_TRST (MTK_PIN_NO(54) | 7)

#define PINMUX_PIN_55__FUNC_B_GPIO55            (MTK_PIN_NO(55) | 0)
#define PINMUX_PIN_55__FUNC_B1_SCL0             (MTK_PIN_NO(55) | 1)
#define PINMUX_PIN_55__FUNC_B1_SCP_SCL0         (MTK_PIN_NO(55) | 2)
#define PINMUX_PIN_55__FUNC_B1_SCP_SCL1         (MTK_PIN_NO(55) | 3)
#define PINMUX_PIN_55__FUNC_B1_PCIE_PHY_I2C_SCL (MTK_PIN_NO(55) | 4)

#define PINMUX_PIN_56__FUNC_B_GPIO56            (MTK_PIN_NO(56) | 0)
#define PINMUX_PIN_56__FUNC_B1_SDA0             (MTK_PIN_NO(56) | 1)
#define PINMUX_PIN_56__FUNC_B1_SCP_SDA0         (MTK_PIN_NO(56) | 2)
#define PINMUX_PIN_56__FUNC_B1_SCP_SDA1         (MTK_PIN_NO(56) | 3)
#define PINMUX_PIN_56__FUNC_B1_PCIE_PHY_I2C_SDA (MTK_PIN_NO(56) | 4)

#define PINMUX_PIN_57__FUNC_B_GPIO57 (MTK_PIN_NO(57) | 0)
#define PINMUX_PIN_57__FUNC_B1_SCL1  (MTK_PIN_NO(57) | 1)

#define PINMUX_PIN_58__FUNC_B_GPIO58 (MTK_PIN_NO(58) | 0)
#define PINMUX_PIN_58__FUNC_B1_SDA1  (MTK_PIN_NO(58) | 1)

#define PINMUX_PIN_59__FUNC_B_GPIO59    (MTK_PIN_NO(59) | 0)
#define PINMUX_PIN_59__FUNC_B1_SCL2     (MTK_PIN_NO(59) | 1)
#define PINMUX_PIN_59__FUNC_B1_SCP_SCL0 (MTK_PIN_NO(59) | 2)
#define PINMUX_PIN_59__FUNC_B1_SCP_SCL1 (MTK_PIN_NO(59) | 3)

#define PINMUX_PIN_60__FUNC_B_GPIO60    (MTK_PIN_NO(60) | 0)
#define PINMUX_PIN_60__FUNC_B1_SDA2     (MTK_PIN_NO(60) | 1)
#define PINMUX_PIN_60__FUNC_B1_SCP_SDA0 (MTK_PIN_NO(60) | 2)
#define PINMUX_PIN_60__FUNC_B1_SCP_SDA1 (MTK_PIN_NO(60) | 3)

#define PINMUX_PIN_61__FUNC_B_GPIO61            (MTK_PIN_NO(61) | 0)
#define PINMUX_PIN_61__FUNC_B1_SCL3             (MTK_PIN_NO(61) | 1)
#define PINMUX_PIN_61__FUNC_B1_SCP_SCL0         (MTK_PIN_NO(61) | 2)
#define PINMUX_PIN_61__FUNC_B1_SCP_SCL1         (MTK_PIN_NO(61) | 3)
#define PINMUX_PIN_61__FUNC_B1_PCIE_PHY_I2C_SCL (MTK_PIN_NO(61) | 4)

#define PINMUX_PIN_62__FUNC_B_GPIO62            (MTK_PIN_NO(62) | 0)
#define PINMUX_PIN_62__FUNC_B1_SDA3             (MTK_PIN_NO(62) | 1)
#define PINMUX_PIN_62__FUNC_B1_SCP_SDA0         (MTK_PIN_NO(62) | 2)
#define PINMUX_PIN_62__FUNC_B1_SCP_SDA1         (MTK_PIN_NO(62) | 3)
#define PINMUX_PIN_62__FUNC_B1_PCIE_PHY_I2C_SDA (MTK_PIN_NO(62) | 4)

#define PINMUX_PIN_63__FUNC_B_GPIO63 (MTK_PIN_NO(63) | 0)
#define PINMUX_PIN_63__FUNC_B1_SCL4  (MTK_PIN_NO(63) | 1)

#define PINMUX_PIN_64__FUNC_B_GPIO64 (MTK_PIN_NO(64) | 0)
#define PINMUX_PIN_64__FUNC_B1_SDA4  (MTK_PIN_NO(64) | 1)

#define PINMUX_PIN_65__FUNC_B_GPIO65    (MTK_PIN_NO(65) | 0)
#define PINMUX_PIN_65__FUNC_B1_SCL5     (MTK_PIN_NO(65) | 1)
#define PINMUX_PIN_65__FUNC_B1_SCP_SCL0 (MTK_PIN_NO(65) | 2)
#define PINMUX_PIN_65__FUNC_B1_SCP_SCL1 (MTK_PIN_NO(65) | 3)

#define PINMUX_PIN_66__FUNC_B_GPIO66    (MTK_PIN_NO(66) | 0)
#define PINMUX_PIN_66__FUNC_B1_SDA5     (MTK_PIN_NO(66) | 1)
#define PINMUX_PIN_66__FUNC_B1_SCP_SDA0 (MTK_PIN_NO(66) | 2)
#define PINMUX_PIN_66__FUNC_B1_SCP_SDA1 (MTK_PIN_NO(66) | 3)

#define PINMUX_PIN_67__FUNC_B_GPIO67            (MTK_PIN_NO(67) | 0)
#define PINMUX_PIN_67__FUNC_B1_SCL6             (MTK_PIN_NO(67) | 1)
#define PINMUX_PIN_67__FUNC_B1_SCP_SCL0         (MTK_PIN_NO(67) | 2)
#define PINMUX_PIN_67__FUNC_B1_SCP_SCL1         (MTK_PIN_NO(67) | 3)
#define PINMUX_PIN_67__FUNC_B1_PCIE_PHY_I2C_SCL (MTK_PIN_NO(67) | 4)

#define PINMUX_PIN_68__FUNC_B_GPIO68            (MTK_PIN_NO(68) | 0)
#define PINMUX_PIN_68__FUNC_B1_SDA6             (MTK_PIN_NO(68) | 1)
#define PINMUX_PIN_68__FUNC_B1_SCP_SDA0         (MTK_PIN_NO(68) | 2)
#define PINMUX_PIN_68__FUNC_B1_SCP_SDA1         (MTK_PIN_NO(68) | 3)
#define PINMUX_PIN_68__FUNC_B1_PCIE_PHY_I2C_SDA (MTK_PIN_NO(68) | 4)

#define PINMUX_PIN_69__FUNC_B_GPIO69           (MTK_PIN_NO(69) | 0)
#define PINMUX_PIN_69__FUNC_O_SPIM0_CSB        (MTK_PIN_NO(69) | 1)
#define PINMUX_PIN_69__FUNC_O_SCP_SPI0_CS      (MTK_PIN_NO(69) | 2)
#define PINMUX_PIN_69__FUNC_O_DMIC3_CLK        (MTK_PIN_NO(69) | 3)
#define PINMUX_PIN_69__FUNC_B0_MD32_1_GPIO0    (MTK_PIN_NO(69) | 4)
#define PINMUX_PIN_69__FUNC_O_CMVREF0          (MTK_PIN_NO(69) | 5)
#define PINMUX_PIN_69__FUNC_O_GDU_SUM_TROOP0_0 (MTK_PIN_NO(69) | 6)
#define PINMUX_PIN_69__FUNC_B0_DBG_MON_A23     (MTK_PIN_NO(69) | 7)

#define PINMUX_PIN_70__FUNC_B_GPIO70           (MTK_PIN_NO(70) | 0)
#define PINMUX_PIN_70__FUNC_O_SPIM0_CLK        (MTK_PIN_NO(70) | 1)
#define PINMUX_PIN_70__FUNC_O_SCP_SPI0_CK      (MTK_PIN_NO(70) | 2)
#define PINMUX_PIN_70__FUNC_I0_DMIC3_DAT       (MTK_PIN_NO(70) | 3)
#define PINMUX_PIN_70__FUNC_B0_MD32_1_GPIO1    (MTK_PIN_NO(70) | 4)
#define PINMUX_PIN_70__FUNC_O_CMVREF1          (MTK_PIN_NO(70) | 5)
#define PINMUX_PIN_70__FUNC_O_GDU_SUM_TROOP0_1 (MTK_PIN_NO(70) | 6)
#define PINMUX_PIN_70__FUNC_B0_DBG_MON_A24     (MTK_PIN_NO(70) | 7)

#define PINMUX_PIN_71__FUNC_B_GPIO71           (MTK_PIN_NO(71) | 0)
#define PINMUX_PIN_71__FUNC_B0_SPIM0_MOSI      (MTK_PIN_NO(71) | 1)
#define PINMUX_PIN_71__FUNC_O_SCP_SPI0_MO      (MTK_PIN_NO(71) | 2)
#define PINMUX_PIN_71__FUNC_I0_DMIC3_DAT_R     (MTK_PIN_NO(71) | 3)
#define PINMUX_PIN_71__FUNC_B0_MD32_1_GPIO2    (MTK_PIN_NO(71) | 4)
#define PINMUX_PIN_71__FUNC_O_CMVREF2          (MTK_PIN_NO(71) | 5)
#define PINMUX_PIN_71__FUNC_O_GDU_SUM_TROOP0_2 (MTK_PIN_NO(71) | 6)
#define PINMUX_PIN_71__FUNC_B0_DBG_MON_A25     (MTK_PIN_NO(71) | 7)

#define PINMUX_PIN_72__FUNC_B_GPIO72           (MTK_PIN_NO(72) | 0)
#define PINMUX_PIN_72__FUNC_B0_SPIM0_MISO      (MTK_PIN_NO(72) | 1)
#define PINMUX_PIN_72__FUNC_I0_SCP_SPI0_MI     (MTK_PIN_NO(72) | 2)
#define PINMUX_PIN_72__FUNC_O_DMIC4_CLK        (MTK_PIN_NO(72) | 3)
#define PINMUX_PIN_72__FUNC_O_CMVREF3          (MTK_PIN_NO(72) | 5)
#define PINMUX_PIN_72__FUNC_O_GDU_SUM_TROOP1_0 (MTK_PIN_NO(72) | 6)
#define PINMUX_PIN_72__FUNC_B0_DBG_MON_A26     (MTK_PIN_NO(72) | 7)

#define PINMUX_PIN_73__FUNC_B_GPIO73           (MTK_PIN_NO(73) | 0)
#define PINMUX_PIN_73__FUNC_B0_SPIM0_MIO2      (MTK_PIN_NO(73) | 1)
#define PINMUX_PIN_73__FUNC_O_UTXD3            (MTK_PIN_NO(73) | 2)
#define PINMUX_PIN_73__FUNC_I0_DMIC4_DAT       (MTK_PIN_NO(73) | 3)
#define PINMUX_PIN_73__FUNC_O_CLKM0            (MTK_PIN_NO(73) | 4)
#define PINMUX_PIN_73__FUNC_O_CMVREF4          (MTK_PIN_NO(73) | 5)
#define PINMUX_PIN_73__FUNC_O_GDU_SUM_TROOP1_1 (MTK_PIN_NO(73) | 6)
#define PINMUX_PIN_73__FUNC_B0_DBG_MON_A27     (MTK_PIN_NO(73) | 7)

#define PINMUX_PIN_74__FUNC_B_GPIO74           (MTK_PIN_NO(74) | 0)
#define PINMUX_PIN_74__FUNC_B0_SPIM0_MIO3      (MTK_PIN_NO(74) | 1)
#define PINMUX_PIN_74__FUNC_I1_URXD3           (MTK_PIN_NO(74) | 2)
#define PINMUX_PIN_74__FUNC_I0_DMIC4_DAT_R     (MTK_PIN_NO(74) | 3)
#define PINMUX_PIN_74__FUNC_O_CLKM1            (MTK_PIN_NO(74) | 4)
#define PINMUX_PIN_74__FUNC_O_CMVREF5          (MTK_PIN_NO(74) | 5)
#define PINMUX_PIN_74__FUNC_O_GDU_SUM_TROOP1_2 (MTK_PIN_NO(74) | 6)
#define PINMUX_PIN_74__FUNC_B0_DBG_MON_A28     (MTK_PIN_NO(74) | 7)

#define PINMUX_PIN_75__FUNC_B_GPIO75           (MTK_PIN_NO(75) | 0)
#define PINMUX_PIN_75__FUNC_O_SPIM1_CSB        (MTK_PIN_NO(75) | 1)
#define PINMUX_PIN_75__FUNC_O_SCP_SPI1_A_CS    (MTK_PIN_NO(75) | 2)
#define PINMUX_PIN_75__FUNC_B0_TDMIN_MCK       (MTK_PIN_NO(75) | 3)
#define PINMUX_PIN_75__FUNC_B1_SCP_SCL0        (MTK_PIN_NO(75) | 4)
#define PINMUX_PIN_75__FUNC_O_CMVREF6          (MTK_PIN_NO(75) | 5)
#define PINMUX_PIN_75__FUNC_O_GDU_SUM_TROOP2_0 (MTK_PIN_NO(75) | 6)
#define PINMUX_PIN_75__FUNC_B0_DBG_MON_A29     (MTK_PIN_NO(75) | 7)

#define PINMUX_PIN_76__FUNC_B_GPIO76           (MTK_PIN_NO(76) | 0)
#define PINMUX_PIN_76__FUNC_O_SPIM1_CLK        (MTK_PIN_NO(76) | 1)
#define PINMUX_PIN_76__FUNC_O_SCP_SPI1_A_CK    (MTK_PIN_NO(76) | 2)
#define PINMUX_PIN_76__FUNC_B0_TDMIN_BCK       (MTK_PIN_NO(76) | 3)
#define PINMUX_PIN_76__FUNC_B1_SCP_SDA0        (MTK_PIN_NO(76) | 4)
#define PINMUX_PIN_76__FUNC_O_CMVREF7          (MTK_PIN_NO(76) | 5)
#define PINMUX_PIN_76__FUNC_O_GDU_SUM_TROOP2_1 (MTK_PIN_NO(76) | 6)
#define PINMUX_PIN_76__FUNC_B0_DBG_MON_A30     (MTK_PIN_NO(76) | 7)

#define PINMUX_PIN_77__FUNC_B_GPIO77           (MTK_PIN_NO(77) | 0)
#define PINMUX_PIN_77__FUNC_B0_SPIM1_MOSI      (MTK_PIN_NO(77) | 1)
#define PINMUX_PIN_77__FUNC_O_SCP_SPI1_A_MO    (MTK_PIN_NO(77) | 2)
#define PINMUX_PIN_77__FUNC_B0_TDMIN_LRCK      (MTK_PIN_NO(77) | 3)
#define PINMUX_PIN_77__FUNC_B1_SCP_SCL1        (MTK_PIN_NO(77) | 4)
#define PINMUX_PIN_77__FUNC_O_GDU_SUM_TROOP2_2 (MTK_PIN_NO(77) | 6)
#define PINMUX_PIN_77__FUNC_B0_DBG_MON_A31     (MTK_PIN_NO(77) | 7)

#define PINMUX_PIN_78__FUNC_B_GPIO78         (MTK_PIN_NO(78) | 0)
#define PINMUX_PIN_78__FUNC_B0_SPIM1_MISO    (MTK_PIN_NO(78) | 1)
#define PINMUX_PIN_78__FUNC_I0_SCP_SPI1_A_MI (MTK_PIN_NO(78) | 2)
#define PINMUX_PIN_78__FUNC_I0_TDMIN_DI      (MTK_PIN_NO(78) | 3)
#define PINMUX_PIN_78__FUNC_B1_SCP_SDA1      (MTK_PIN_NO(78) | 4)
#define PINMUX_PIN_78__FUNC_B0_DBG_MON_A32   (MTK_PIN_NO(78) | 7)

#define PINMUX_PIN_79__FUNC_B_GPIO79      (MTK_PIN_NO(79) | 0)
#define PINMUX_PIN_79__FUNC_O_SPIM2_CSB   (MTK_PIN_NO(79) | 1)
#define PINMUX_PIN_79__FUNC_O_SCP_SPI2_CS (MTK_PIN_NO(79) | 2)
#define PINMUX_PIN_79__FUNC_O_I2SO1_MCK   (MTK_PIN_NO(79) | 3)
#define PINMUX_PIN_79__FUNC_O_UTXD2       (MTK_PIN_NO(79) | 4)
#define PINMUX_PIN_79__FUNC_O_TP_UTXD2_AO (MTK_PIN_NO(79) | 5)
#define PINMUX_PIN_79__FUNC_B0_PCM_SYNC   (MTK_PIN_NO(79) | 6)
#define PINMUX_PIN_79__FUNC_B0_DBG_MON_B0 (MTK_PIN_NO(79) | 7)

#define PINMUX_PIN_80__FUNC_B_GPIO80       (MTK_PIN_NO(80) | 0)
#define PINMUX_PIN_80__FUNC_O_SPIM2_CLK    (MTK_PIN_NO(80) | 1)
#define PINMUX_PIN_80__FUNC_O_SCP_SPI2_CK  (MTK_PIN_NO(80) | 2)
#define PINMUX_PIN_80__FUNC_O_I2SO1_BCK    (MTK_PIN_NO(80) | 3)
#define PINMUX_PIN_80__FUNC_I1_URXD2       (MTK_PIN_NO(80) | 4)
#define PINMUX_PIN_80__FUNC_I1_TP_URXD2_AO (MTK_PIN_NO(80) | 5)
#define PINMUX_PIN_80__FUNC_B0_PCM_CLK     (MTK_PIN_NO(80) | 6)
#define PINMUX_PIN_80__FUNC_B0_DBG_MON_B1  (MTK_PIN_NO(80) | 7)

#define PINMUX_PIN_81__FUNC_B_GPIO81      (MTK_PIN_NO(81) | 0)
#define PINMUX_PIN_81__FUNC_B0_SPIM2_MOSI (MTK_PIN_NO(81) | 1)
#define PINMUX_PIN_81__FUNC_O_SCP_SPI2_MO (MTK_PIN_NO(81) | 2)
#define PINMUX_PIN_81__FUNC_O_I2SO1_WS    (MTK_PIN_NO(81) | 3)
#define PINMUX_PIN_81__FUNC_O_URTS2       (MTK_PIN_NO(81) | 4)
#define PINMUX_PIN_81__FUNC_O_TP_URTS2_AO (MTK_PIN_NO(81) | 5)
#define PINMUX_PIN_81__FUNC_O_PCM_DO      (MTK_PIN_NO(81) | 6)
#define PINMUX_PIN_81__FUNC_B0_DBG_MON_B2 (MTK_PIN_NO(81) | 7)

#define PINMUX_PIN_82__FUNC_B_GPIO82       (MTK_PIN_NO(82) | 0)
#define PINMUX_PIN_82__FUNC_B0_SPIM2_MISO  (MTK_PIN_NO(82) | 1)
#define PINMUX_PIN_82__FUNC_I0_SCP_SPI2_MI (MTK_PIN_NO(82) | 2)
#define PINMUX_PIN_82__FUNC_O_I2SO1_D0     (MTK_PIN_NO(82) | 3)
#define PINMUX_PIN_82__FUNC_I1_UCTS2       (MTK_PIN_NO(82) | 4)
#define PINMUX_PIN_82__FUNC_I1_TP_UCTS2_AO (MTK_PIN_NO(82) | 5)
#define PINMUX_PIN_82__FUNC_I0_PCM_DI      (MTK_PIN_NO(82) | 6)
#define PINMUX_PIN_82__FUNC_B0_DBG_MON_B3  (MTK_PIN_NO(82) | 7)

#define PINMUX_PIN_83__FUNC_B_GPIO83 (MTK_PIN_NO(83) | 0)
#define PINMUX_PIN_83__FUNC_I1_IDDIG (MTK_PIN_NO(83) | 1)

#define PINMUX_PIN_84__FUNC_B_GPIO84      (MTK_PIN_NO(84) | 0)
#define PINMUX_PIN_84__FUNC_O_USB_DRVVBUS (MTK_PIN_NO(84) | 1)

#define PINMUX_PIN_85__FUNC_B_GPIO85     (MTK_PIN_NO(85) | 0)
#define PINMUX_PIN_85__FUNC_I0_VBUSVALID (MTK_PIN_NO(85) | 1)

#define PINMUX_PIN_86__FUNC_B_GPIO86       (MTK_PIN_NO(86) | 0)
#define PINMUX_PIN_86__FUNC_I1_IDDIG_1P    (MTK_PIN_NO(86) | 1)
#define PINMUX_PIN_86__FUNC_O_UTXD1        (MTK_PIN_NO(86) | 2)
#define PINMUX_PIN_86__FUNC_O_URTS2        (MTK_PIN_NO(86) | 3)
#define PINMUX_PIN_86__FUNC_O_PWM_2        (MTK_PIN_NO(86) | 4)
#define PINMUX_PIN_86__FUNC_B0_TP_GPIO4_AO (MTK_PIN_NO(86) | 5)
#define PINMUX_PIN_86__FUNC_O_AUXIF_ST0    (MTK_PIN_NO(86) | 6)
#define PINMUX_PIN_86__FUNC_B0_DBG_MON_B4  (MTK_PIN_NO(86) | 7)

#define PINMUX_PIN_87__FUNC_B_GPIO87         (MTK_PIN_NO(87) | 0)
#define PINMUX_PIN_87__FUNC_O_USB_DRVVBUS_1P (MTK_PIN_NO(87) | 1)
#define PINMUX_PIN_87__FUNC_I1_URXD1         (MTK_PIN_NO(87) | 2)
#define PINMUX_PIN_87__FUNC_I1_UCTS2         (MTK_PIN_NO(87) | 3)
#define PINMUX_PIN_87__FUNC_O_PWM_3          (MTK_PIN_NO(87) | 4)
#define PINMUX_PIN_87__FUNC_B0_TP_GPIO5_AO   (MTK_PIN_NO(87) | 5)
#define PINMUX_PIN_87__FUNC_O_AUXIF_CLK0     (MTK_PIN_NO(87) | 6)
#define PINMUX_PIN_87__FUNC_B0_DBG_MON_B5    (MTK_PIN_NO(87) | 7)

#define PINMUX_PIN_88__FUNC_B_GPIO88        (MTK_PIN_NO(88) | 0)
#define PINMUX_PIN_88__FUNC_I0_VBUSVALID_1P (MTK_PIN_NO(88) | 1)
#define PINMUX_PIN_88__FUNC_O_UTXD2         (MTK_PIN_NO(88) | 2)
#define PINMUX_PIN_88__FUNC_O_URTS1         (MTK_PIN_NO(88) | 3)
#define PINMUX_PIN_88__FUNC_O_CLKM2         (MTK_PIN_NO(88) | 4)
#define PINMUX_PIN_88__FUNC_B0_TP_GPIO6_AO  (MTK_PIN_NO(88) | 5)
#define PINMUX_PIN_88__FUNC_O_AUXIF_ST1     (MTK_PIN_NO(88) | 6)
#define PINMUX_PIN_88__FUNC_B0_DBG_MON_B6   (MTK_PIN_NO(88) | 7)

#define PINMUX_PIN_89__FUNC_B_GPIO89       (MTK_PIN_NO(89) | 0)
#define PINMUX_PIN_89__FUNC_I1_IDDIG_2P    (MTK_PIN_NO(89) | 1)
#define PINMUX_PIN_89__FUNC_I1_URXD2       (MTK_PIN_NO(89) | 2)
#define PINMUX_PIN_89__FUNC_I1_UCTS1       (MTK_PIN_NO(89) | 3)
#define PINMUX_PIN_89__FUNC_O_CLKM3        (MTK_PIN_NO(89) | 4)
#define PINMUX_PIN_89__FUNC_B0_TP_GPIO7_AO (MTK_PIN_NO(89) | 5)
#define PINMUX_PIN_89__FUNC_O_AUXIF_CLK1   (MTK_PIN_NO(89) | 6)
#define PINMUX_PIN_89__FUNC_B0_DBG_MON_B7  (MTK_PIN_NO(89) | 7)

#define PINMUX_PIN_90__FUNC_B_GPIO90         (MTK_PIN_NO(90) | 0)
#define PINMUX_PIN_90__FUNC_O_USB_DRVVBUS_2P (MTK_PIN_NO(90) | 1)
#define PINMUX_PIN_90__FUNC_O_UTXD3          (MTK_PIN_NO(90) | 2)
#define PINMUX_PIN_90__FUNC_O_ADSP_UTXD0     (MTK_PIN_NO(90) | 3)
#define PINMUX_PIN_90__FUNC_O_SSPM_UTXD_AO   (MTK_PIN_NO(90) | 4)
#define PINMUX_PIN_90__FUNC_O_MD32_0_TXD     (MTK_PIN_NO(90) | 5)
#define PINMUX_PIN_90__FUNC_O_MD32_1_TXD     (MTK_PIN_NO(90) | 6)
#define PINMUX_PIN_90__FUNC_B0_DBG_MON_B8    (MTK_PIN_NO(90) | 7)

#define PINMUX_PIN_91__FUNC_B_GPIO91        (MTK_PIN_NO(91) | 0)
#define PINMUX_PIN_91__FUNC_I0_VBUSVALID_2P (MTK_PIN_NO(91) | 1)
#define PINMUX_PIN_91__FUNC_I1_URXD3        (MTK_PIN_NO(91) | 2)
#define PINMUX_PIN_91__FUNC_I1_ADSP_URXD0   (MTK_PIN_NO(91) | 3)
#define PINMUX_PIN_91__FUNC_I1_SSPM_URXD_AO (MTK_PIN_NO(91) | 4)
#define PINMUX_PIN_91__FUNC_I1_MD32_0_RXD   (MTK_PIN_NO(91) | 5)
#define PINMUX_PIN_91__FUNC_I1_MD32_1_RXD   (MTK_PIN_NO(91) | 6)
#define PINMUX_PIN_91__FUNC_B0_DBG_MON_B9   (MTK_PIN_NO(91) | 7)

#define PINMUX_PIN_92__FUNC_B_GPIO92         (MTK_PIN_NO(92) | 0)
#define PINMUX_PIN_92__FUNC_O_PWRAP_SPI0_CSN (MTK_PIN_NO(92) | 1)

#define PINMUX_PIN_93__FUNC_B_GPIO93        (MTK_PIN_NO(93) | 0)
#define PINMUX_PIN_93__FUNC_O_PWRAP_SPI0_CK (MTK_PIN_NO(93) | 1)

#define PINMUX_PIN_94__FUNC_B_GPIO94         (MTK_PIN_NO(94) | 0)
#define PINMUX_PIN_94__FUNC_B0_PWRAP_SPI0_MO (MTK_PIN_NO(94) | 1)
#define PINMUX_PIN_94__FUNC_B0_PWRAP_SPI0_MI (MTK_PIN_NO(94) | 2)

#define PINMUX_PIN_95__FUNC_B_GPIO95         (MTK_PIN_NO(95) | 0)
#define PINMUX_PIN_95__FUNC_B0_PWRAP_SPI0_MI (MTK_PIN_NO(95) | 1)
#define PINMUX_PIN_95__FUNC_B0_PWRAP_SPI0_MO (MTK_PIN_NO(95) | 2)

#define PINMUX_PIN_96__FUNC_B_GPIO96    (MTK_PIN_NO(96) | 0)
#define PINMUX_PIN_96__FUNC_O_SRCLKENA0 (MTK_PIN_NO(96) | 1)

#define PINMUX_PIN_97__FUNC_B_GPIO97    (MTK_PIN_NO(97) | 0)
#define PINMUX_PIN_97__FUNC_O_SRCLKENA1 (MTK_PIN_NO(97) | 1)

#define PINMUX_PIN_98__FUNC_B_GPIO98          (MTK_PIN_NO(98) | 0)
#define PINMUX_PIN_98__FUNC_O_SCP_VREQ_VAO    (MTK_PIN_NO(98) | 1)
#define PINMUX_PIN_98__FUNC_I0_DVFSRC_EXT_REQ (MTK_PIN_NO(98) | 2)

#define PINMUX_PIN_99__FUNC_B_GPIO99     (MTK_PIN_NO(99) | 0)
#define PINMUX_PIN_99__FUNC_I0_RTC32K_CK (MTK_PIN_NO(99) | 1)

#define PINMUX_PIN_100__FUNC_B_GPIO100  (MTK_PIN_NO(100) | 0)
#define PINMUX_PIN_100__FUNC_O_WATCHDOG (MTK_PIN_NO(100) | 1)

#define PINMUX_PIN_101__FUNC_B_GPIO101      (MTK_PIN_NO(101) | 0)
#define PINMUX_PIN_101__FUNC_O_AUD_CLK_MOSI (MTK_PIN_NO(101) | 1)
#define PINMUX_PIN_101__FUNC_O_I2SO1_MCK    (MTK_PIN_NO(101) | 2)
#define PINMUX_PIN_101__FUNC_B0_I2SIN_BCK   (MTK_PIN_NO(101) | 3)

#define PINMUX_PIN_102__FUNC_B_GPIO102       (MTK_PIN_NO(102) | 0)
#define PINMUX_PIN_102__FUNC_O_AUD_SYNC_MOSI (MTK_PIN_NO(102) | 1)
#define PINMUX_PIN_102__FUNC_O_I2SO1_BCK     (MTK_PIN_NO(102) | 2)
#define PINMUX_PIN_102__FUNC_B0_I2SIN_WS     (MTK_PIN_NO(102) | 3)

#define PINMUX_PIN_103__FUNC_B_GPIO103       (MTK_PIN_NO(103) | 0)
#define PINMUX_PIN_103__FUNC_O_AUD_DAT_MOSI0 (MTK_PIN_NO(103) | 1)
#define PINMUX_PIN_103__FUNC_O_I2SO1_WS      (MTK_PIN_NO(103) | 2)
#define PINMUX_PIN_103__FUNC_I0_I2SIN_D0     (MTK_PIN_NO(103) | 3)

#define PINMUX_PIN_104__FUNC_B_GPIO104       (MTK_PIN_NO(104) | 0)
#define PINMUX_PIN_104__FUNC_O_AUD_DAT_MOSI1 (MTK_PIN_NO(104) | 1)
#define PINMUX_PIN_104__FUNC_O_I2SO1_D0      (MTK_PIN_NO(104) | 2)
#define PINMUX_PIN_104__FUNC_I0_I2SIN_D1     (MTK_PIN_NO(104) | 3)

#define PINMUX_PIN_105__FUNC_B_GPIO105        (MTK_PIN_NO(105) | 0)
#define PINMUX_PIN_105__FUNC_I0_AUD_DAT_MISO0 (MTK_PIN_NO(105) | 1)
#define PINMUX_PIN_105__FUNC_I0_VOW_DAT_MISO  (MTK_PIN_NO(105) | 2)
#define PINMUX_PIN_105__FUNC_I0_I2SIN_D2      (MTK_PIN_NO(105) | 3)

#define PINMUX_PIN_106__FUNC_B_GPIO106        (MTK_PIN_NO(106) | 0)
#define PINMUX_PIN_106__FUNC_I0_AUD_DAT_MISO1 (MTK_PIN_NO(106) | 1)
#define PINMUX_PIN_106__FUNC_I0_VOW_CLK_MISO  (MTK_PIN_NO(106) | 2)
#define PINMUX_PIN_106__FUNC_I0_I2SIN_D3      (MTK_PIN_NO(106) | 3)

#define PINMUX_PIN_107__FUNC_B_GPIO107         (MTK_PIN_NO(107) | 0)
#define PINMUX_PIN_107__FUNC_B0_I2SIN_MCK      (MTK_PIN_NO(107) | 1)
#define PINMUX_PIN_107__FUNC_I0_SPLIN_MCK      (MTK_PIN_NO(107) | 2)
#define PINMUX_PIN_107__FUNC_I0_SPDIF_IN0      (MTK_PIN_NO(107) | 3)
#define PINMUX_PIN_107__FUNC_O_CMVREF4         (MTK_PIN_NO(107) | 4)
#define PINMUX_PIN_107__FUNC_O_AUXIF_ST0       (MTK_PIN_NO(107) | 5)
#define PINMUX_PIN_107__FUNC_O_PGD_LV_LSC_PWR0 (MTK_PIN_NO(107) | 6)

#define PINMUX_PIN_108__FUNC_B_GPIO108         (MTK_PIN_NO(108) | 0)
#define PINMUX_PIN_108__FUNC_B0_I2SIN_BCK      (MTK_PIN_NO(108) | 1)
#define PINMUX_PIN_108__FUNC_I0_SPLIN_LRCK     (MTK_PIN_NO(108) | 2)
#define PINMUX_PIN_108__FUNC_O_DMIC4_CLK       (MTK_PIN_NO(108) | 3)
#define PINMUX_PIN_108__FUNC_O_CMVREF5         (MTK_PIN_NO(108) | 4)
#define PINMUX_PIN_108__FUNC_O_AUXIF_CLK0      (MTK_PIN_NO(108) | 5)
#define PINMUX_PIN_108__FUNC_O_PGD_LV_LSC_PWR1 (MTK_PIN_NO(108) | 6)
#define PINMUX_PIN_108__FUNC_B0_DBG_MON_B10    (MTK_PIN_NO(108) | 7)

#define PINMUX_PIN_109__FUNC_B_GPIO109         (MTK_PIN_NO(109) | 0)
#define PINMUX_PIN_109__FUNC_B0_I2SIN_WS       (MTK_PIN_NO(109) | 1)
#define PINMUX_PIN_109__FUNC_I0_SPLIN_BCK      (MTK_PIN_NO(109) | 2)
#define PINMUX_PIN_109__FUNC_I0_DMIC4_DAT      (MTK_PIN_NO(109) | 3)
#define PINMUX_PIN_109__FUNC_O_CMVREF6         (MTK_PIN_NO(109) | 4)
#define PINMUX_PIN_109__FUNC_O_AUXIF_ST1       (MTK_PIN_NO(109) | 5)
#define PINMUX_PIN_109__FUNC_O_PGD_LV_LSC_PWR2 (MTK_PIN_NO(109) | 6)
#define PINMUX_PIN_109__FUNC_B0_DBG_MON_B11    (MTK_PIN_NO(109) | 7)

#define PINMUX_PIN_110__FUNC_B_GPIO110         (MTK_PIN_NO(110) | 0)
#define PINMUX_PIN_110__FUNC_I0_I2SIN_D0       (MTK_PIN_NO(110) | 1)
#define PINMUX_PIN_110__FUNC_I0_SPLIN_D0       (MTK_PIN_NO(110) | 2)
#define PINMUX_PIN_110__FUNC_I0_DMIC4_DAT_R    (MTK_PIN_NO(110) | 3)
#define PINMUX_PIN_110__FUNC_O_CMVREF7         (MTK_PIN_NO(110) | 4)
#define PINMUX_PIN_110__FUNC_O_AUXIF_CLK1      (MTK_PIN_NO(110) | 5)
#define PINMUX_PIN_110__FUNC_O_PGD_LV_LSC_PWR3 (MTK_PIN_NO(110) | 6)
#define PINMUX_PIN_110__FUNC_B0_DBG_MON_B12    (MTK_PIN_NO(110) | 7)

#define PINMUX_PIN_111__FUNC_B_GPIO111         (MTK_PIN_NO(111) | 0)
#define PINMUX_PIN_111__FUNC_I0_I2SIN_D1       (MTK_PIN_NO(111) | 1)
#define PINMUX_PIN_111__FUNC_I0_SPLIN_D1       (MTK_PIN_NO(111) | 2)
#define PINMUX_PIN_111__FUNC_O_DMIC3_CLK       (MTK_PIN_NO(111) | 3)
#define PINMUX_PIN_111__FUNC_O_SPDIF_OUT       (MTK_PIN_NO(111) | 4)
#define PINMUX_PIN_111__FUNC_O_PGD_LV_LSC_PWR4 (MTK_PIN_NO(111) | 6)
#define PINMUX_PIN_111__FUNC_B0_DBG_MON_B13    (MTK_PIN_NO(111) | 7)

#define PINMUX_PIN_112__FUNC_B_GPIO112         (MTK_PIN_NO(112) | 0)
#define PINMUX_PIN_112__FUNC_I0_I2SIN_D2       (MTK_PIN_NO(112) | 1)
#define PINMUX_PIN_112__FUNC_I0_SPLIN_D2       (MTK_PIN_NO(112) | 2)
#define PINMUX_PIN_112__FUNC_I0_DMIC3_DAT      (MTK_PIN_NO(112) | 3)
#define PINMUX_PIN_112__FUNC_B0_TDMIN_MCK      (MTK_PIN_NO(112) | 4)
#define PINMUX_PIN_112__FUNC_O_I2SO1_WS        (MTK_PIN_NO(112) | 5)
#define PINMUX_PIN_112__FUNC_O_PGD_LV_LSC_PWR5 (MTK_PIN_NO(112) | 6)
#define PINMUX_PIN_112__FUNC_B0_DBG_MON_B14    (MTK_PIN_NO(112) | 7)

#define PINMUX_PIN_113__FUNC_B_GPIO113      (MTK_PIN_NO(113) | 0)
#define PINMUX_PIN_113__FUNC_I0_I2SIN_D3    (MTK_PIN_NO(113) | 1)
#define PINMUX_PIN_113__FUNC_I0_SPLIN_D3    (MTK_PIN_NO(113) | 2)
#define PINMUX_PIN_113__FUNC_I0_DMIC3_DAT_R (MTK_PIN_NO(113) | 3)
#define PINMUX_PIN_113__FUNC_B0_TDMIN_BCK   (MTK_PIN_NO(113) | 4)
#define PINMUX_PIN_113__FUNC_O_I2SO1_D0     (MTK_PIN_NO(113) | 5)
#define PINMUX_PIN_113__FUNC_B0_DBG_MON_B15 (MTK_PIN_NO(113) | 7)

#define PINMUX_PIN_114__FUNC_B_GPIO114         (MTK_PIN_NO(114) | 0)
#define PINMUX_PIN_114__FUNC_O_I2SO2_MCK       (MTK_PIN_NO(114) | 1)
#define PINMUX_PIN_114__FUNC_B0_I2SIN_MCK      (MTK_PIN_NO(114) | 2)
#define PINMUX_PIN_114__FUNC_I1_MCUPM_JTAG_TMS (MTK_PIN_NO(114) | 3)
#define PINMUX_PIN_114__FUNC_B1_APU_JTAG_TMS   (MTK_PIN_NO(114) | 4)
#define PINMUX_PIN_114__FUNC_I1_SCP_JTAG1_TMS  (MTK_PIN_NO(114) | 5)
#define PINMUX_PIN_114__FUNC_I1_SPM_JTAG_TMS   (MTK_PIN_NO(114) | 6)
#define PINMUX_PIN_114__FUNC_B0_DBG_MON_B16    (MTK_PIN_NO(114) | 7)

#define PINMUX_PIN_115__FUNC_B_GPIO115         (MTK_PIN_NO(115) | 0)
#define PINMUX_PIN_115__FUNC_B0_I2SO2_BCK      (MTK_PIN_NO(115) | 1)
#define PINMUX_PIN_115__FUNC_B0_I2SIN_BCK      (MTK_PIN_NO(115) | 2)
#define PINMUX_PIN_115__FUNC_I1_MCUPM_JTAG_TCK (MTK_PIN_NO(115) | 3)
#define PINMUX_PIN_115__FUNC_I0_APU_JTAG_TCK   (MTK_PIN_NO(115) | 4)
#define PINMUX_PIN_115__FUNC_I1_SCP_JTAG1_TCK  (MTK_PIN_NO(115) | 5)
#define PINMUX_PIN_115__FUNC_I1_SPM_JTAG_TCK   (MTK_PIN_NO(115) | 6)
#define PINMUX_PIN_115__FUNC_B0_DBG_MON_B17    (MTK_PIN_NO(115) | 7)

#define PINMUX_PIN_116__FUNC_B_GPIO116         (MTK_PIN_NO(116) | 0)
#define PINMUX_PIN_116__FUNC_B0_I2SO2_WS       (MTK_PIN_NO(116) | 1)
#define PINMUX_PIN_116__FUNC_B0_I2SIN_WS       (MTK_PIN_NO(116) | 2)
#define PINMUX_PIN_116__FUNC_I1_MCUPM_JTAG_TDI (MTK_PIN_NO(116) | 3)
#define PINMUX_PIN_116__FUNC_I1_APU_JTAG_TDI   (MTK_PIN_NO(116) | 4)
#define PINMUX_PIN_116__FUNC_I1_SCP_JTAG1_TDI  (MTK_PIN_NO(116) | 5)
#define PINMUX_PIN_116__FUNC_I1_SPM_JTAG_TDI   (MTK_PIN_NO(116) | 6)
#define PINMUX_PIN_116__FUNC_B0_DBG_MON_B18    (MTK_PIN_NO(116) | 7)

#define PINMUX_PIN_117__FUNC_B_GPIO117        (MTK_PIN_NO(117) | 0)
#define PINMUX_PIN_117__FUNC_O_I2SO2_D0       (MTK_PIN_NO(117) | 1)
#define PINMUX_PIN_117__FUNC_I0_I2SIN_D0      (MTK_PIN_NO(117) | 2)
#define PINMUX_PIN_117__FUNC_O_MCUPM_JTAG_TDO (MTK_PIN_NO(117) | 3)
#define PINMUX_PIN_117__FUNC_O_APU_JTAG_TDO   (MTK_PIN_NO(117) | 4)
#define PINMUX_PIN_117__FUNC_O_SCP_JTAG1_TDO  (MTK_PIN_NO(117) | 5)
#define PINMUX_PIN_117__FUNC_O_SPM_JTAG_TDO   (MTK_PIN_NO(117) | 6)
#define PINMUX_PIN_117__FUNC_B0_DBG_MON_B19   (MTK_PIN_NO(117) | 7)

#define PINMUX_PIN_118__FUNC_B_GPIO118           (MTK_PIN_NO(118) | 0)
#define PINMUX_PIN_118__FUNC_O_I2SO2_D1          (MTK_PIN_NO(118) | 1)
#define PINMUX_PIN_118__FUNC_I0_I2SIN_D1         (MTK_PIN_NO(118) | 2)
#define PINMUX_PIN_118__FUNC_I0_MCUPM_JTAG_TRSTN (MTK_PIN_NO(118) | 3)
#define PINMUX_PIN_118__FUNC_I0_APU_JTAG_TRST    (MTK_PIN_NO(118) | 4)
#define PINMUX_PIN_118__FUNC_I0_SCP_JTAG1_TRSTN  (MTK_PIN_NO(118) | 5)
#define PINMUX_PIN_118__FUNC_I0_SPM_JTAG_TRSTN   (MTK_PIN_NO(118) | 6)
#define PINMUX_PIN_118__FUNC_B0_DBG_MON_B20      (MTK_PIN_NO(118) | 7)

#define PINMUX_PIN_119__FUNC_B_GPIO119      (MTK_PIN_NO(119) | 0)
#define PINMUX_PIN_119__FUNC_O_I2SO2_D2     (MTK_PIN_NO(119) | 1)
#define PINMUX_PIN_119__FUNC_I0_I2SIN_D2    (MTK_PIN_NO(119) | 2)
#define PINMUX_PIN_119__FUNC_O_UTXD3        (MTK_PIN_NO(119) | 3)
#define PINMUX_PIN_119__FUNC_B0_TDMIN_LRCK  (MTK_PIN_NO(119) | 4)
#define PINMUX_PIN_119__FUNC_O_I2SO1_MCK    (MTK_PIN_NO(119) | 5)
#define PINMUX_PIN_119__FUNC_O_SSPM_UTXD_AO (MTK_PIN_NO(119) | 6)
#define PINMUX_PIN_119__FUNC_B0_DBG_MON_B21 (MTK_PIN_NO(119) | 7)

#define PINMUX_PIN_120__FUNC_B_GPIO120       (MTK_PIN_NO(120) | 0)
#define PINMUX_PIN_120__FUNC_O_I2SO2_D3      (MTK_PIN_NO(120) | 1)
#define PINMUX_PIN_120__FUNC_I0_I2SIN_D3     (MTK_PIN_NO(120) | 2)
#define PINMUX_PIN_120__FUNC_I1_URXD3        (MTK_PIN_NO(120) | 3)
#define PINMUX_PIN_120__FUNC_I0_TDMIN_DI     (MTK_PIN_NO(120) | 4)
#define PINMUX_PIN_120__FUNC_O_I2SO1_BCK     (MTK_PIN_NO(120) | 5)
#define PINMUX_PIN_120__FUNC_I1_SSPM_URXD_AO (MTK_PIN_NO(120) | 6)
#define PINMUX_PIN_120__FUNC_B0_DBG_MON_B22  (MTK_PIN_NO(120) | 7)

#define PINMUX_PIN_121__FUNC_B_GPIO121          (MTK_PIN_NO(121) | 0)
#define PINMUX_PIN_121__FUNC_B0_PCM_CLK         (MTK_PIN_NO(121) | 1)
#define PINMUX_PIN_121__FUNC_O_SPIM4_CSB        (MTK_PIN_NO(121) | 2)
#define PINMUX_PIN_121__FUNC_O_SCP_SPI1_B_CS    (MTK_PIN_NO(121) | 3)
#define PINMUX_PIN_121__FUNC_O_TP_UTXD2_AO      (MTK_PIN_NO(121) | 4)
#define PINMUX_PIN_121__FUNC_O_AUXIF_ST0        (MTK_PIN_NO(121) | 5)
#define PINMUX_PIN_121__FUNC_O_PGD_DA_EFUSE_RDY (MTK_PIN_NO(121) | 6)
#define PINMUX_PIN_121__FUNC_B0_DBG_MON_B23     (MTK_PIN_NO(121) | 7)

#define PINMUX_PIN_122__FUNC_B_GPIO122              (MTK_PIN_NO(122) | 0)
#define PINMUX_PIN_122__FUNC_B0_PCM_SYNC            (MTK_PIN_NO(122) | 1)
#define PINMUX_PIN_122__FUNC_O_SPIM4_CLK            (MTK_PIN_NO(122) | 2)
#define PINMUX_PIN_122__FUNC_O_SCP_SPI1_B_CK        (MTK_PIN_NO(122) | 3)
#define PINMUX_PIN_122__FUNC_I1_TP_URXD2_AO         (MTK_PIN_NO(122) | 4)
#define PINMUX_PIN_122__FUNC_O_AUXIF_CLK0           (MTK_PIN_NO(122) | 5)
#define PINMUX_PIN_122__FUNC_O_PGD_DA_EFUSE_RDY_PRE (MTK_PIN_NO(122) | 6)
#define PINMUX_PIN_122__FUNC_B0_DBG_MON_B24         (MTK_PIN_NO(122) | 7)

#define PINMUX_PIN_123__FUNC_B_GPIO123            (MTK_PIN_NO(123) | 0)
#define PINMUX_PIN_123__FUNC_O_PCM_DO             (MTK_PIN_NO(123) | 1)
#define PINMUX_PIN_123__FUNC_B0_SPIM4_MOSI        (MTK_PIN_NO(123) | 2)
#define PINMUX_PIN_123__FUNC_O_SCP_SPI1_B_MO      (MTK_PIN_NO(123) | 3)
#define PINMUX_PIN_123__FUNC_O_TP_URTS2_AO        (MTK_PIN_NO(123) | 4)
#define PINMUX_PIN_123__FUNC_O_AUXIF_ST1          (MTK_PIN_NO(123) | 5)
#define PINMUX_PIN_123__FUNC_O_PGD_DA_PWRGD_RESET (MTK_PIN_NO(123) | 6)
#define PINMUX_PIN_123__FUNC_B0_DBG_MON_B25       (MTK_PIN_NO(123) | 7)

#define PINMUX_PIN_124__FUNC_B_GPIO124          (MTK_PIN_NO(124) | 0)
#define PINMUX_PIN_124__FUNC_I0_PCM_DI          (MTK_PIN_NO(124) | 1)
#define PINMUX_PIN_124__FUNC_B0_SPIM4_MISO      (MTK_PIN_NO(124) | 2)
#define PINMUX_PIN_124__FUNC_I0_SCP_SPI1_B_MI   (MTK_PIN_NO(124) | 3)
#define PINMUX_PIN_124__FUNC_I1_TP_UCTS2_AO     (MTK_PIN_NO(124) | 4)
#define PINMUX_PIN_124__FUNC_O_AUXIF_CLK1       (MTK_PIN_NO(124) | 5)
#define PINMUX_PIN_124__FUNC_O_PGD_DA_PWRGD_ENB (MTK_PIN_NO(124) | 6)
#define PINMUX_PIN_124__FUNC_B0_DBG_MON_B26     (MTK_PIN_NO(124) | 7)

#define PINMUX_PIN_125__FUNC_B_GPIO125      (MTK_PIN_NO(125) | 0)
#define PINMUX_PIN_125__FUNC_O_DMIC1_CLK    (MTK_PIN_NO(125) | 1)
#define PINMUX_PIN_125__FUNC_O_SPINOR_CK    (MTK_PIN_NO(125) | 2)
#define PINMUX_PIN_125__FUNC_B0_TDMIN_MCK   (MTK_PIN_NO(125) | 3)
#define PINMUX_PIN_125__FUNC_O_LVTS_FOUT    (MTK_PIN_NO(125) | 6)
#define PINMUX_PIN_125__FUNC_B0_DBG_MON_B27 (MTK_PIN_NO(125) | 7)

#define PINMUX_PIN_126__FUNC_B_GPIO126      (MTK_PIN_NO(126) | 0)
#define PINMUX_PIN_126__FUNC_I0_DMIC1_DAT   (MTK_PIN_NO(126) | 1)
#define PINMUX_PIN_126__FUNC_O_SPINOR_CS    (MTK_PIN_NO(126) | 2)
#define PINMUX_PIN_126__FUNC_B0_TDMIN_BCK   (MTK_PIN_NO(126) | 3)
#define PINMUX_PIN_126__FUNC_O_LVTS_SDO     (MTK_PIN_NO(126) | 6)
#define PINMUX_PIN_126__FUNC_B0_DBG_MON_B28 (MTK_PIN_NO(126) | 7)

#define PINMUX_PIN_127__FUNC_B_GPIO127      (MTK_PIN_NO(127) | 0)
#define PINMUX_PIN_127__FUNC_I0_DMIC1_DAT_R (MTK_PIN_NO(127) | 1)
#define PINMUX_PIN_127__FUNC_B0_SPINOR_IO0  (MTK_PIN_NO(127) | 2)
#define PINMUX_PIN_127__FUNC_B0_TDMIN_LRCK  (MTK_PIN_NO(127) | 3)
#define PINMUX_PIN_127__FUNC_I0_LVTS_26M    (MTK_PIN_NO(127) | 6)
#define PINMUX_PIN_127__FUNC_B0_DBG_MON_B29 (MTK_PIN_NO(127) | 7)

#define PINMUX_PIN_128__FUNC_B_GPIO128      (MTK_PIN_NO(128) | 0)
#define PINMUX_PIN_128__FUNC_O_DMIC2_CLK    (MTK_PIN_NO(128) | 1)
#define PINMUX_PIN_128__FUNC_B0_SPINOR_IO1  (MTK_PIN_NO(128) | 2)
#define PINMUX_PIN_128__FUNC_I0_TDMIN_DI    (MTK_PIN_NO(128) | 3)
#define PINMUX_PIN_128__FUNC_I0_LVTS_SCF    (MTK_PIN_NO(128) | 6)
#define PINMUX_PIN_128__FUNC_B0_DBG_MON_B30 (MTK_PIN_NO(128) | 7)

#define PINMUX_PIN_129__FUNC_B_GPIO129      (MTK_PIN_NO(129) | 0)
#define PINMUX_PIN_129__FUNC_I0_DMIC2_DAT   (MTK_PIN_NO(129) | 1)
#define PINMUX_PIN_129__FUNC_B0_SPINOR_IO2  (MTK_PIN_NO(129) | 2)
#define PINMUX_PIN_129__FUNC_I0_SPDIF_IN1   (MTK_PIN_NO(129) | 3)
#define PINMUX_PIN_129__FUNC_I0_LVTS_SCK    (MTK_PIN_NO(129) | 6)
#define PINMUX_PIN_129__FUNC_B0_DBG_MON_B31 (MTK_PIN_NO(129) | 7)

#define PINMUX_PIN_130__FUNC_B_GPIO130      (MTK_PIN_NO(130) | 0)
#define PINMUX_PIN_130__FUNC_I0_DMIC2_DAT_R (MTK_PIN_NO(130) | 1)
#define PINMUX_PIN_130__FUNC_B0_SPINOR_IO3  (MTK_PIN_NO(130) | 2)
#define PINMUX_PIN_130__FUNC_I0_SPDIF_IN2   (MTK_PIN_NO(130) | 3)
#define PINMUX_PIN_130__FUNC_I0_LVTS_SDI    (MTK_PIN_NO(130) | 6)
#define PINMUX_PIN_130__FUNC_B0_DBG_MON_B32 (MTK_PIN_NO(130) | 7)

#define PINMUX_PIN_131__FUNC_B_GPIO131         (MTK_PIN_NO(131) | 0)
#define PINMUX_PIN_131__FUNC_O_DPI_D0          (MTK_PIN_NO(131) | 1)
#define PINMUX_PIN_131__FUNC_O_GBE_TXD3        (MTK_PIN_NO(131) | 2)
#define PINMUX_PIN_131__FUNC_O_DMIC1_CLK       (MTK_PIN_NO(131) | 3)
#define PINMUX_PIN_131__FUNC_O_I2SO2_MCK       (MTK_PIN_NO(131) | 4)
#define PINMUX_PIN_131__FUNC_B0_TP_GPIO0_AO    (MTK_PIN_NO(131) | 5)
#define PINMUX_PIN_131__FUNC_O_SPIM5_CSB       (MTK_PIN_NO(131) | 6)
#define PINMUX_PIN_131__FUNC_O_PGD_LV_HSC_PWR0 (MTK_PIN_NO(131) | 7)

#define PINMUX_PIN_132__FUNC_B_GPIO132         (MTK_PIN_NO(132) | 0)
#define PINMUX_PIN_132__FUNC_O_DPI_D1          (MTK_PIN_NO(132) | 1)
#define PINMUX_PIN_132__FUNC_O_GBE_TXD2        (MTK_PIN_NO(132) | 2)
#define PINMUX_PIN_132__FUNC_I0_DMIC1_DAT      (MTK_PIN_NO(132) | 3)
#define PINMUX_PIN_132__FUNC_B0_I2SO2_BCK      (MTK_PIN_NO(132) | 4)
#define PINMUX_PIN_132__FUNC_B0_TP_GPIO1_AO    (MTK_PIN_NO(132) | 5)
#define PINMUX_PIN_132__FUNC_O_SPIM5_CLK       (MTK_PIN_NO(132) | 6)
#define PINMUX_PIN_132__FUNC_O_PGD_LV_HSC_PWR1 (MTK_PIN_NO(132) | 7)

#define PINMUX_PIN_133__FUNC_B_GPIO133         (MTK_PIN_NO(133) | 0)
#define PINMUX_PIN_133__FUNC_O_DPI_D2          (MTK_PIN_NO(133) | 1)
#define PINMUX_PIN_133__FUNC_O_GBE_TXD1        (MTK_PIN_NO(133) | 2)
#define PINMUX_PIN_133__FUNC_I0_DMIC1_DAT_R    (MTK_PIN_NO(133) | 3)
#define PINMUX_PIN_133__FUNC_B0_I2SO2_WS       (MTK_PIN_NO(133) | 4)
#define PINMUX_PIN_133__FUNC_B0_TP_GPIO2_AO    (MTK_PIN_NO(133) | 5)
#define PINMUX_PIN_133__FUNC_B0_SPIM5_MOSI     (MTK_PIN_NO(133) | 6)
#define PINMUX_PIN_133__FUNC_O_PGD_LV_HSC_PWR2 (MTK_PIN_NO(133) | 7)

#define PINMUX_PIN_134__FUNC_B_GPIO134         (MTK_PIN_NO(134) | 0)
#define PINMUX_PIN_134__FUNC_O_DPI_D3          (MTK_PIN_NO(134) | 1)
#define PINMUX_PIN_134__FUNC_O_GBE_TXD0        (MTK_PIN_NO(134) | 2)
#define PINMUX_PIN_134__FUNC_O_DMIC2_CLK       (MTK_PIN_NO(134) | 3)
#define PINMUX_PIN_134__FUNC_O_I2SO2_D0        (MTK_PIN_NO(134) | 4)
#define PINMUX_PIN_134__FUNC_B0_TP_GPIO3_AO    (MTK_PIN_NO(134) | 5)
#define PINMUX_PIN_134__FUNC_B0_SPIM5_MISO     (MTK_PIN_NO(134) | 6)
#define PINMUX_PIN_134__FUNC_O_PGD_LV_HSC_PWR3 (MTK_PIN_NO(134) | 7)

#define PINMUX_PIN_135__FUNC_B_GPIO135         (MTK_PIN_NO(135) | 0)
#define PINMUX_PIN_135__FUNC_O_DPI_D4          (MTK_PIN_NO(135) | 1)
#define PINMUX_PIN_135__FUNC_I0_GBE_RXD3       (MTK_PIN_NO(135) | 2)
#define PINMUX_PIN_135__FUNC_I0_DMIC2_DAT      (MTK_PIN_NO(135) | 3)
#define PINMUX_PIN_135__FUNC_O_I2SO2_D1        (MTK_PIN_NO(135) | 4)
#define PINMUX_PIN_135__FUNC_B0_TP_GPIO4_AO    (MTK_PIN_NO(135) | 5)
#define PINMUX_PIN_135__FUNC_I1_WAKEN          (MTK_PIN_NO(135) | 6)
#define PINMUX_PIN_135__FUNC_O_PGD_LV_HSC_PWR4 (MTK_PIN_NO(135) | 7)

#define PINMUX_PIN_136__FUNC_B_GPIO136         (MTK_PIN_NO(136) | 0)
#define PINMUX_PIN_136__FUNC_O_DPI_D5          (MTK_PIN_NO(136) | 1)
#define PINMUX_PIN_136__FUNC_I0_GBE_RXD2       (MTK_PIN_NO(136) | 2)
#define PINMUX_PIN_136__FUNC_I0_DMIC2_DAT_R    (MTK_PIN_NO(136) | 3)
#define PINMUX_PIN_136__FUNC_O_I2SO2_D2        (MTK_PIN_NO(136) | 4)
#define PINMUX_PIN_136__FUNC_B0_TP_GPIO5_AO    (MTK_PIN_NO(136) | 5)
#define PINMUX_PIN_136__FUNC_O_PERSTN          (MTK_PIN_NO(136) | 6)
#define PINMUX_PIN_136__FUNC_O_PGD_LV_HSC_PWR5 (MTK_PIN_NO(136) | 7)

#define PINMUX_PIN_137__FUNC_B_GPIO137      (MTK_PIN_NO(137) | 0)
#define PINMUX_PIN_137__FUNC_O_DPI_D6       (MTK_PIN_NO(137) | 1)
#define PINMUX_PIN_137__FUNC_I0_GBE_RXD1    (MTK_PIN_NO(137) | 2)
#define PINMUX_PIN_137__FUNC_O_DMIC3_CLK    (MTK_PIN_NO(137) | 3)
#define PINMUX_PIN_137__FUNC_O_I2SO2_D3     (MTK_PIN_NO(137) | 4)
#define PINMUX_PIN_137__FUNC_B0_TP_GPIO6_AO (MTK_PIN_NO(137) | 5)
#define PINMUX_PIN_137__FUNC_B1_CLKREQN     (MTK_PIN_NO(137) | 6)
#define PINMUX_PIN_137__FUNC_O_PWM_0        (MTK_PIN_NO(137) | 7)

#define PINMUX_PIN_138__FUNC_B_GPIO138       (MTK_PIN_NO(138) | 0)
#define PINMUX_PIN_138__FUNC_O_DPI_D7        (MTK_PIN_NO(138) | 1)
#define PINMUX_PIN_138__FUNC_I0_GBE_RXD0     (MTK_PIN_NO(138) | 2)
#define PINMUX_PIN_138__FUNC_I0_DMIC3_DAT    (MTK_PIN_NO(138) | 3)
#define PINMUX_PIN_138__FUNC_O_CLKM2         (MTK_PIN_NO(138) | 4)
#define PINMUX_PIN_138__FUNC_B0_TP_GPIO7_AO  (MTK_PIN_NO(138) | 5)
#define PINMUX_PIN_138__FUNC_B0_MD32_0_GPIO0 (MTK_PIN_NO(138) | 7)

#define PINMUX_PIN_139__FUNC_B_GPIO139       (MTK_PIN_NO(139) | 0)
#define PINMUX_PIN_139__FUNC_O_DPI_D8        (MTK_PIN_NO(139) | 1)
#define PINMUX_PIN_139__FUNC_B0_GBE_TXC      (MTK_PIN_NO(139) | 2)
#define PINMUX_PIN_139__FUNC_I0_DMIC3_DAT_R  (MTK_PIN_NO(139) | 3)
#define PINMUX_PIN_139__FUNC_O_CLKM3         (MTK_PIN_NO(139) | 4)
#define PINMUX_PIN_139__FUNC_O_TP_UTXD2_AO   (MTK_PIN_NO(139) | 5)
#define PINMUX_PIN_139__FUNC_O_UTXD2         (MTK_PIN_NO(139) | 6)
#define PINMUX_PIN_139__FUNC_B0_MD32_0_GPIO1 (MTK_PIN_NO(139) | 7)

#define PINMUX_PIN_140__FUNC_B_GPIO140       (MTK_PIN_NO(140) | 0)
#define PINMUX_PIN_140__FUNC_O_DPI_D9        (MTK_PIN_NO(140) | 1)
#define PINMUX_PIN_140__FUNC_I0_GBE_RXC      (MTK_PIN_NO(140) | 2)
#define PINMUX_PIN_140__FUNC_O_DMIC4_CLK     (MTK_PIN_NO(140) | 3)
#define PINMUX_PIN_140__FUNC_O_PWM_2         (MTK_PIN_NO(140) | 4)
#define PINMUX_PIN_140__FUNC_I1_TP_URXD2_AO  (MTK_PIN_NO(140) | 5)
#define PINMUX_PIN_140__FUNC_I1_URXD2        (MTK_PIN_NO(140) | 6)
#define PINMUX_PIN_140__FUNC_B0_MD32_0_GPIO2 (MTK_PIN_NO(140) | 7)

#define PINMUX_PIN_141__FUNC_B_GPIO141       (MTK_PIN_NO(141) | 0)
#define PINMUX_PIN_141__FUNC_O_DPI_D10       (MTK_PIN_NO(141) | 1)
#define PINMUX_PIN_141__FUNC_I0_GBE_RXDV     (MTK_PIN_NO(141) | 2)
#define PINMUX_PIN_141__FUNC_I0_DMIC4_DAT    (MTK_PIN_NO(141) | 3)
#define PINMUX_PIN_141__FUNC_O_PWM_3         (MTK_PIN_NO(141) | 4)
#define PINMUX_PIN_141__FUNC_O_TP_URTS2_AO   (MTK_PIN_NO(141) | 5)
#define PINMUX_PIN_141__FUNC_O_URTS2         (MTK_PIN_NO(141) | 6)
#define PINMUX_PIN_141__FUNC_B0_MD32_1_GPIO0 (MTK_PIN_NO(141) | 7)

#define PINMUX_PIN_142__FUNC_B_GPIO142       (MTK_PIN_NO(142) | 0)
#define PINMUX_PIN_142__FUNC_O_DPI_D11       (MTK_PIN_NO(142) | 1)
#define PINMUX_PIN_142__FUNC_O_GBE_TXEN      (MTK_PIN_NO(142) | 2)
#define PINMUX_PIN_142__FUNC_I0_DMIC4_DAT_R  (MTK_PIN_NO(142) | 3)
#define PINMUX_PIN_142__FUNC_O_PWM_1         (MTK_PIN_NO(142) | 4)
#define PINMUX_PIN_142__FUNC_I1_TP_UCTS2_AO  (MTK_PIN_NO(142) | 5)
#define PINMUX_PIN_142__FUNC_I1_UCTS2        (MTK_PIN_NO(142) | 6)
#define PINMUX_PIN_142__FUNC_B0_MD32_1_GPIO1 (MTK_PIN_NO(142) | 7)

#define PINMUX_PIN_143__FUNC_B_GPIO143       (MTK_PIN_NO(143) | 0)
#define PINMUX_PIN_143__FUNC_O_DPI_D12       (MTK_PIN_NO(143) | 1)
#define PINMUX_PIN_143__FUNC_O_GBE_MDC       (MTK_PIN_NO(143) | 2)
#define PINMUX_PIN_143__FUNC_B0_MD32_0_GPIO0 (MTK_PIN_NO(143) | 3)
#define PINMUX_PIN_143__FUNC_O_CLKM0         (MTK_PIN_NO(143) | 4)
#define PINMUX_PIN_143__FUNC_O_SPIM3_CSB     (MTK_PIN_NO(143) | 5)
#define PINMUX_PIN_143__FUNC_O_UTXD1         (MTK_PIN_NO(143) | 6)
#define PINMUX_PIN_143__FUNC_B0_MD32_1_GPIO2 (MTK_PIN_NO(143) | 7)

#define PINMUX_PIN_144__FUNC_B_GPIO144         (MTK_PIN_NO(144) | 0)
#define PINMUX_PIN_144__FUNC_O_DPI_D13         (MTK_PIN_NO(144) | 1)
#define PINMUX_PIN_144__FUNC_B1_GBE_MDIO       (MTK_PIN_NO(144) | 2)
#define PINMUX_PIN_144__FUNC_B0_MD32_0_GPIO1   (MTK_PIN_NO(144) | 3)
#define PINMUX_PIN_144__FUNC_O_CLKM1           (MTK_PIN_NO(144) | 4)
#define PINMUX_PIN_144__FUNC_O_SPIM3_CLK       (MTK_PIN_NO(144) | 5)
#define PINMUX_PIN_144__FUNC_I1_URXD1          (MTK_PIN_NO(144) | 6)
#define PINMUX_PIN_144__FUNC_O_PGD_HV_HSC_PWR0 (MTK_PIN_NO(144) | 7)

#define PINMUX_PIN_145__FUNC_B_GPIO145         (MTK_PIN_NO(145) | 0)
#define PINMUX_PIN_145__FUNC_O_DPI_D14         (MTK_PIN_NO(145) | 1)
#define PINMUX_PIN_145__FUNC_O_GBE_TXER        (MTK_PIN_NO(145) | 2)
#define PINMUX_PIN_145__FUNC_B0_MD32_1_GPIO0   (MTK_PIN_NO(145) | 3)
#define PINMUX_PIN_145__FUNC_O_CMFLASH0        (MTK_PIN_NO(145) | 4)
#define PINMUX_PIN_145__FUNC_B0_SPIM3_MOSI     (MTK_PIN_NO(145) | 5)
#define PINMUX_PIN_145__FUNC_B0_GBE_AUX_PPS2   (MTK_PIN_NO(145) | 6)
#define PINMUX_PIN_145__FUNC_O_PGD_HV_HSC_PWR1 (MTK_PIN_NO(145) | 7)

#define PINMUX_PIN_146__FUNC_B_GPIO146         (MTK_PIN_NO(146) | 0)
#define PINMUX_PIN_146__FUNC_O_DPI_D15         (MTK_PIN_NO(146) | 1)
#define PINMUX_PIN_146__FUNC_I0_GBE_RXER       (MTK_PIN_NO(146) | 2)
#define PINMUX_PIN_146__FUNC_B0_MD32_1_GPIO1   (MTK_PIN_NO(146) | 3)
#define PINMUX_PIN_146__FUNC_O_CMFLASH1        (MTK_PIN_NO(146) | 4)
#define PINMUX_PIN_146__FUNC_B0_SPIM3_MISO     (MTK_PIN_NO(146) | 5)
#define PINMUX_PIN_146__FUNC_B0_GBE_AUX_PPS3   (MTK_PIN_NO(146) | 6)
#define PINMUX_PIN_146__FUNC_O_PGD_HV_HSC_PWR2 (MTK_PIN_NO(146) | 7)

#define PINMUX_PIN_147__FUNC_B_GPIO147         (MTK_PIN_NO(147) | 0)
#define PINMUX_PIN_147__FUNC_O_DPI_HSYNC       (MTK_PIN_NO(147) | 1)
#define PINMUX_PIN_147__FUNC_I0_GBE_COL        (MTK_PIN_NO(147) | 2)
#define PINMUX_PIN_147__FUNC_O_I2SO1_MCK       (MTK_PIN_NO(147) | 3)
#define PINMUX_PIN_147__FUNC_O_CMVREF0         (MTK_PIN_NO(147) | 4)
#define PINMUX_PIN_147__FUNC_O_SPDIF_OUT       (MTK_PIN_NO(147) | 5)
#define PINMUX_PIN_147__FUNC_O_URTS1           (MTK_PIN_NO(147) | 6)
#define PINMUX_PIN_147__FUNC_O_PGD_HV_HSC_PWR3 (MTK_PIN_NO(147) | 7)

#define PINMUX_PIN_148__FUNC_B_GPIO148         (MTK_PIN_NO(148) | 0)
#define PINMUX_PIN_148__FUNC_O_DPI_VSYNC       (MTK_PIN_NO(148) | 1)
#define PINMUX_PIN_148__FUNC_I0_GBE_INTR       (MTK_PIN_NO(148) | 2)
#define PINMUX_PIN_148__FUNC_O_I2SO1_BCK       (MTK_PIN_NO(148) | 3)
#define PINMUX_PIN_148__FUNC_O_CMVREF1         (MTK_PIN_NO(148) | 4)
#define PINMUX_PIN_148__FUNC_I0_SPDIF_IN0      (MTK_PIN_NO(148) | 5)
#define PINMUX_PIN_148__FUNC_I1_UCTS1          (MTK_PIN_NO(148) | 6)
#define PINMUX_PIN_148__FUNC_O_PGD_HV_HSC_PWR4 (MTK_PIN_NO(148) | 7)

#define PINMUX_PIN_149__FUNC_B_GPIO149         (MTK_PIN_NO(149) | 0)
#define PINMUX_PIN_149__FUNC_O_DPI_DE          (MTK_PIN_NO(149) | 1)
#define PINMUX_PIN_149__FUNC_B0_GBE_AUX_PPS0   (MTK_PIN_NO(149) | 2)
#define PINMUX_PIN_149__FUNC_O_I2SO1_WS        (MTK_PIN_NO(149) | 3)
#define PINMUX_PIN_149__FUNC_O_CMVREF2         (MTK_PIN_NO(149) | 4)
#define PINMUX_PIN_149__FUNC_I0_SPDIF_IN1      (MTK_PIN_NO(149) | 5)
#define PINMUX_PIN_149__FUNC_O_UTXD3           (MTK_PIN_NO(149) | 6)
#define PINMUX_PIN_149__FUNC_O_PGD_HV_HSC_PWR5 (MTK_PIN_NO(149) | 7)

#define PINMUX_PIN_150__FUNC_B_GPIO150       (MTK_PIN_NO(150) | 0)
#define PINMUX_PIN_150__FUNC_O_DPI_CK        (MTK_PIN_NO(150) | 1)
#define PINMUX_PIN_150__FUNC_B0_GBE_AUX_PPS1 (MTK_PIN_NO(150) | 2)
#define PINMUX_PIN_150__FUNC_O_I2SO1_D0      (MTK_PIN_NO(150) | 3)
#define PINMUX_PIN_150__FUNC_O_CMVREF3       (MTK_PIN_NO(150) | 4)
#define PINMUX_PIN_150__FUNC_I0_SPDIF_IN2    (MTK_PIN_NO(150) | 5)
#define PINMUX_PIN_150__FUNC_I1_URXD3        (MTK_PIN_NO(150) | 6)

#define PINMUX_PIN_151__FUNC_B_GPIO151     (MTK_PIN_NO(151) | 0)
#define PINMUX_PIN_151__FUNC_B1_MSDC0_DAT7 (MTK_PIN_NO(151) | 1)

#define PINMUX_PIN_152__FUNC_B_GPIO152     (MTK_PIN_NO(152) | 0)
#define PINMUX_PIN_152__FUNC_B1_MSDC0_DAT6 (MTK_PIN_NO(152) | 1)

#define PINMUX_PIN_153__FUNC_B_GPIO153     (MTK_PIN_NO(153) | 0)
#define PINMUX_PIN_153__FUNC_B1_MSDC0_DAT5 (MTK_PIN_NO(153) | 1)

#define PINMUX_PIN_154__FUNC_B_GPIO154     (MTK_PIN_NO(154) | 0)
#define PINMUX_PIN_154__FUNC_B1_MSDC0_DAT4 (MTK_PIN_NO(154) | 1)

#define PINMUX_PIN_155__FUNC_B_GPIO155    (MTK_PIN_NO(155) | 0)
#define PINMUX_PIN_155__FUNC_O_MSDC0_RSTB (MTK_PIN_NO(155) | 1)

#define PINMUX_PIN_156__FUNC_B_GPIO156    (MTK_PIN_NO(156) | 0)
#define PINMUX_PIN_156__FUNC_B1_MSDC0_CMD (MTK_PIN_NO(156) | 1)

#define PINMUX_PIN_157__FUNC_B_GPIO157    (MTK_PIN_NO(157) | 0)
#define PINMUX_PIN_157__FUNC_B1_MSDC0_CLK (MTK_PIN_NO(157) | 1)

#define PINMUX_PIN_158__FUNC_B_GPIO158     (MTK_PIN_NO(158) | 0)
#define PINMUX_PIN_158__FUNC_B1_MSDC0_DAT3 (MTK_PIN_NO(158) | 1)

#define PINMUX_PIN_159__FUNC_B_GPIO159     (MTK_PIN_NO(159) | 0)
#define PINMUX_PIN_159__FUNC_B1_MSDC0_DAT2 (MTK_PIN_NO(159) | 1)

#define PINMUX_PIN_160__FUNC_B_GPIO160     (MTK_PIN_NO(160) | 0)
#define PINMUX_PIN_160__FUNC_B1_MSDC0_DAT1 (MTK_PIN_NO(160) | 1)

#define PINMUX_PIN_161__FUNC_B_GPIO161     (MTK_PIN_NO(161) | 0)
#define PINMUX_PIN_161__FUNC_B1_MSDC0_DAT0 (MTK_PIN_NO(161) | 1)

#define PINMUX_PIN_162__FUNC_B_GPIO162    (MTK_PIN_NO(162) | 0)
#define PINMUX_PIN_162__FUNC_B0_MSDC0_DSL (MTK_PIN_NO(162) | 1)

#define PINMUX_PIN_163__FUNC_B_GPIO163          (MTK_PIN_NO(163) | 0)
#define PINMUX_PIN_163__FUNC_B1_MSDC1_CMD       (MTK_PIN_NO(163) | 1)
#define PINMUX_PIN_163__FUNC_O_SPDIF_OUT        (MTK_PIN_NO(163) | 2)
#define PINMUX_PIN_163__FUNC_I1_MD32_0_JTAG_TMS (MTK_PIN_NO(163) | 3)
#define PINMUX_PIN_163__FUNC_I1_ADSP_JTAG0_TMS  (MTK_PIN_NO(163) | 4)
#define PINMUX_PIN_163__FUNC_I1_SCP_JTAG0_TMS   (MTK_PIN_NO(163) | 5)
#define PINMUX_PIN_163__FUNC_I1_CCU0_JTAG_TMS   (MTK_PIN_NO(163) | 6)
#define PINMUX_PIN_163__FUNC_I0_IPU_JTAG_TMS    (MTK_PIN_NO(163) | 7)

#define PINMUX_PIN_164__FUNC_B_GPIO164          (MTK_PIN_NO(164) | 0)
#define PINMUX_PIN_164__FUNC_B1_MSDC1_CLK       (MTK_PIN_NO(164) | 1)
#define PINMUX_PIN_164__FUNC_I0_SPDIF_IN0       (MTK_PIN_NO(164) | 2)
#define PINMUX_PIN_164__FUNC_I1_MD32_0_JTAG_TCK (MTK_PIN_NO(164) | 3)
#define PINMUX_PIN_164__FUNC_I0_ADSP_JTAG0_TCK  (MTK_PIN_NO(164) | 4)
#define PINMUX_PIN_164__FUNC_I1_SCP_JTAG0_TCK   (MTK_PIN_NO(164) | 5)
#define PINMUX_PIN_164__FUNC_I1_CCU0_JTAG_TCK   (MTK_PIN_NO(164) | 6)
#define PINMUX_PIN_164__FUNC_I0_IPU_JTAG_TCK    (MTK_PIN_NO(164) | 7)

#define PINMUX_PIN_165__FUNC_B_GPIO165          (MTK_PIN_NO(165) | 0)
#define PINMUX_PIN_165__FUNC_B1_MSDC1_DAT0      (MTK_PIN_NO(165) | 1)
#define PINMUX_PIN_165__FUNC_I0_SPDIF_IN1       (MTK_PIN_NO(165) | 2)
#define PINMUX_PIN_165__FUNC_I1_MD32_0_JTAG_TDI (MTK_PIN_NO(165) | 3)
#define PINMUX_PIN_165__FUNC_I1_ADSP_JTAG0_TDI  (MTK_PIN_NO(165) | 4)
#define PINMUX_PIN_165__FUNC_I1_SCP_JTAG0_TDI   (MTK_PIN_NO(165) | 5)
#define PINMUX_PIN_165__FUNC_I1_CCU0_JTAG_TDI   (MTK_PIN_NO(165) | 6)
#define PINMUX_PIN_165__FUNC_I0_IPU_JTAG_TDI    (MTK_PIN_NO(165) | 7)

#define PINMUX_PIN_166__FUNC_B_GPIO166         (MTK_PIN_NO(166) | 0)
#define PINMUX_PIN_166__FUNC_B1_MSDC1_DAT1     (MTK_PIN_NO(166) | 1)
#define PINMUX_PIN_166__FUNC_I0_SPDIF_IN2      (MTK_PIN_NO(166) | 2)
#define PINMUX_PIN_166__FUNC_O_MD32_0_JTAG_TDO (MTK_PIN_NO(166) | 3)
#define PINMUX_PIN_166__FUNC_O_ADSP_JTAG0_TDO  (MTK_PIN_NO(166) | 4)
#define PINMUX_PIN_166__FUNC_O_SCP_JTAG0_TDO   (MTK_PIN_NO(166) | 5)
#define PINMUX_PIN_166__FUNC_O_CCU0_JTAG_TDO   (MTK_PIN_NO(166) | 6)
#define PINMUX_PIN_166__FUNC_O_IPU_JTAG_TDO    (MTK_PIN_NO(166) | 7)

#define PINMUX_PIN_167__FUNC_B_GPIO167           (MTK_PIN_NO(167) | 0)
#define PINMUX_PIN_167__FUNC_B1_MSDC1_DAT2       (MTK_PIN_NO(167) | 1)
#define PINMUX_PIN_167__FUNC_O_PWM_0             (MTK_PIN_NO(167) | 2)
#define PINMUX_PIN_167__FUNC_I1_MD32_0_JTAG_TRST (MTK_PIN_NO(167) | 3)
#define PINMUX_PIN_167__FUNC_I1_ADSP_JTAG0_TRSTN (MTK_PIN_NO(167) | 4)
#define PINMUX_PIN_167__FUNC_I0_SCP_JTAG0_TRSTN  (MTK_PIN_NO(167) | 5)
#define PINMUX_PIN_167__FUNC_I1_CCU0_JTAG_TRST   (MTK_PIN_NO(167) | 6)
#define PINMUX_PIN_167__FUNC_I0_IPU_JTAG_TRST    (MTK_PIN_NO(167) | 7)

#define PINMUX_PIN_168__FUNC_B_GPIO168     (MTK_PIN_NO(168) | 0)
#define PINMUX_PIN_168__FUNC_B1_MSDC1_DAT3 (MTK_PIN_NO(168) | 1)
#define PINMUX_PIN_168__FUNC_O_PWM_1       (MTK_PIN_NO(168) | 2)
#define PINMUX_PIN_168__FUNC_O_CLKM0       (MTK_PIN_NO(168) | 3)

#define PINMUX_PIN_169__FUNC_B_GPIO169          (MTK_PIN_NO(169) | 0)
#define PINMUX_PIN_169__FUNC_B1_MSDC2_CMD       (MTK_PIN_NO(169) | 1)
#define PINMUX_PIN_169__FUNC_O_LVTS_FOUT        (MTK_PIN_NO(169) | 2)
#define PINMUX_PIN_169__FUNC_I1_MD32_1_JTAG_TMS (MTK_PIN_NO(169) | 3)
#define PINMUX_PIN_169__FUNC_I0_UDI_TMS         (MTK_PIN_NO(169) | 4)
#define PINMUX_PIN_169__FUNC_I0_VPU_UDI_TMS     (MTK_PIN_NO(169) | 5)
#define PINMUX_PIN_169__FUNC_B0_TDMIN_MCK       (MTK_PIN_NO(169) | 6)
#define PINMUX_PIN_169__FUNC_I1_SSPM_JTAG_TMS   (MTK_PIN_NO(169) | 7)

#define PINMUX_PIN_170__FUNC_B_GPIO170          (MTK_PIN_NO(170) | 0)
#define PINMUX_PIN_170__FUNC_B1_MSDC2_CLK       (MTK_PIN_NO(170) | 1)
#define PINMUX_PIN_170__FUNC_O_LVTS_SDO         (MTK_PIN_NO(170) | 2)
#define PINMUX_PIN_170__FUNC_I1_MD32_1_JTAG_TCK (MTK_PIN_NO(170) | 3)
#define PINMUX_PIN_170__FUNC_I0_UDI_TCK         (MTK_PIN_NO(170) | 4)
#define PINMUX_PIN_170__FUNC_I0_VPU_UDI_TCK     (MTK_PIN_NO(170) | 5)
#define PINMUX_PIN_170__FUNC_B0_TDMIN_BCK       (MTK_PIN_NO(170) | 6)
#define PINMUX_PIN_170__FUNC_I1_SSPM_JTAG_TCK   (MTK_PIN_NO(170) | 7)

#define PINMUX_PIN_171__FUNC_B_GPIO171          (MTK_PIN_NO(171) | 0)
#define PINMUX_PIN_171__FUNC_B1_MSDC2_DAT0      (MTK_PIN_NO(171) | 1)
#define PINMUX_PIN_171__FUNC_I0_LVTS_26M        (MTK_PIN_NO(171) | 2)
#define PINMUX_PIN_171__FUNC_I1_MD32_1_JTAG_TDI (MTK_PIN_NO(171) | 3)
#define PINMUX_PIN_171__FUNC_I0_UDI_TDI         (MTK_PIN_NO(171) | 4)
#define PINMUX_PIN_171__FUNC_I0_VPU_UDI_TDI     (MTK_PIN_NO(171) | 5)
#define PINMUX_PIN_171__FUNC_B0_TDMIN_LRCK      (MTK_PIN_NO(171) | 6)
#define PINMUX_PIN_171__FUNC_I1_SSPM_JTAG_TDI   (MTK_PIN_NO(171) | 7)

#define PINMUX_PIN_172__FUNC_B_GPIO172         (MTK_PIN_NO(172) | 0)
#define PINMUX_PIN_172__FUNC_B1_MSDC2_DAT1     (MTK_PIN_NO(172) | 1)
#define PINMUX_PIN_172__FUNC_I0_LVTS_SCF       (MTK_PIN_NO(172) | 2)
#define PINMUX_PIN_172__FUNC_O_MD32_1_JTAG_TDO (MTK_PIN_NO(172) | 3)
#define PINMUX_PIN_172__FUNC_O_UDI_TDO         (MTK_PIN_NO(172) | 4)
#define PINMUX_PIN_172__FUNC_O_VPU_UDI_TDO     (MTK_PIN_NO(172) | 5)
#define PINMUX_PIN_172__FUNC_I0_TDMIN_DI       (MTK_PIN_NO(172) | 6)
#define PINMUX_PIN_172__FUNC_O_SSPM_JTAG_TDO   (MTK_PIN_NO(172) | 7)

#define PINMUX_PIN_173__FUNC_B_GPIO173           (MTK_PIN_NO(173) | 0)
#define PINMUX_PIN_173__FUNC_B1_MSDC2_DAT2       (MTK_PIN_NO(173) | 1)
#define PINMUX_PIN_173__FUNC_I0_LVTS_SCK         (MTK_PIN_NO(173) | 2)
#define PINMUX_PIN_173__FUNC_I1_MD32_1_JTAG_TRST (MTK_PIN_NO(173) | 3)
#define PINMUX_PIN_173__FUNC_I0_UDI_NTRST        (MTK_PIN_NO(173) | 4)
#define PINMUX_PIN_173__FUNC_I0_VPU_UDI_NTRST    (MTK_PIN_NO(173) | 5)
#define PINMUX_PIN_173__FUNC_I0_SSPM_JTAG_TRSTN  (MTK_PIN_NO(173) | 7)

#define PINMUX_PIN_174__FUNC_B_GPIO174     (MTK_PIN_NO(174) | 0)
#define PINMUX_PIN_174__FUNC_B1_MSDC2_DAT3 (MTK_PIN_NO(174) | 1)
#define PINMUX_PIN_174__FUNC_I0_LVTS_SDI   (MTK_PIN_NO(174) | 2)

#define PINMUX_PIN_175__FUNC_B_GPIO175     (MTK_PIN_NO(175) | 0)
#define PINMUX_PIN_175__FUNC_B0_SPMI_M_SCL (MTK_PIN_NO(175) | 1)

#define PINMUX_PIN_176__FUNC_B_GPIO176     (MTK_PIN_NO(176) | 0)
#define PINMUX_PIN_176__FUNC_B0_SPMI_M_SDA (MTK_PIN_NO(176) | 1)

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MT8188_PINCTRL_H_ */
```

## 571.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 MediaTek Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 1288 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MT8188_PINCTRL_H_`。

## 571.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mt8188-pinctrl_8h.html)
- [zephyr/dt-bindings/pinctrl/mtk-common-pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/mtk-common-pinctrl_8h.html)
- [mtk-common-pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/mtk-common-pinctrl_8h.html)

---

[上一章](P570_mspm0_vref.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P572_navigation.h_源码浏览.md)
