---
id: learning.zephyr-docs.api-source-configuration-reference.page-63
title: pinctrl-r8a77951.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a77951_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_pinctrl-r8a77951.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a77951_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a77951_8h.html)。

## 63.1\_原始可见代码（Source Code）

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
<a id="l00953"></a>
<a id="l00954"></a>
<a id="apinctrl-rcar-common_8h_html"></a>

```c
/*
 * Copyright (c) 2021 IoT.bzh
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A77951_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A77951_H_

#include "pinctrl-rcar-common.h"


/* Pins declaration */
#define PIN_NONE                   -1
#define PIN_D0                     RCAR_GP_PIN(0, 0)
#define PIN_D1                     RCAR_GP_PIN(0, 1)
#define PIN_D2                     RCAR_GP_PIN(0, 2)
#define PIN_D3                     RCAR_GP_PIN(0, 3)
#define PIN_D4                     RCAR_GP_PIN(0, 4)
#define PIN_D5                     RCAR_GP_PIN(0, 5)
#define PIN_D6                     RCAR_GP_PIN(0, 6)
#define PIN_D7                     RCAR_GP_PIN(0, 7)
#define PIN_D8                     RCAR_GP_PIN(0, 8)
#define PIN_D9                     RCAR_GP_PIN(0, 9)
#define PIN_D10                    RCAR_GP_PIN(0, 10)
#define PIN_D11                    RCAR_GP_PIN(0, 11)
#define PIN_D12                    RCAR_GP_PIN(0, 12)
#define PIN_D13                    RCAR_GP_PIN(0, 13)
#define PIN_D14                    RCAR_GP_PIN(0, 14)
#define PIN_D15                    RCAR_GP_PIN(0, 15)
#define PIN_A0                     RCAR_GP_PIN(1, 0)
#define PIN_A1                     RCAR_GP_PIN(1, 1)
#define PIN_A2                     RCAR_GP_PIN(1, 2)
#define PIN_A3                     RCAR_GP_PIN(1, 3)
#define PIN_A4                     RCAR_GP_PIN(1, 4)
#define PIN_A5                     RCAR_GP_PIN(1, 5)
#define PIN_A6                     RCAR_GP_PIN(1, 6)
#define PIN_A7                     RCAR_GP_PIN(1, 7)
#define PIN_A8                     RCAR_GP_PIN(1, 8)
#define PIN_A9                     RCAR_GP_PIN(1, 9)
#define PIN_A10                    RCAR_GP_PIN(1, 10)
#define PIN_A11                    RCAR_GP_PIN(1, 11)
#define PIN_A12                    RCAR_GP_PIN(1, 12)
#define PIN_A13                    RCAR_GP_PIN(1, 13)
#define PIN_A14                    RCAR_GP_PIN(1, 14)
#define PIN_A15                    RCAR_GP_PIN(1, 15)
#define PIN_A16                    RCAR_GP_PIN(1, 16)
#define PIN_A17                    RCAR_GP_PIN(1, 17)
#define PIN_A18                    RCAR_GP_PIN(1, 18)
#define PIN_A19                    RCAR_GP_PIN(1, 19)
#define PIN_CS0                    RCAR_GP_PIN(1, 20)
#define PIN_CS1                    RCAR_GP_PIN(1, 21)
#define PIN_BS                     RCAR_GP_PIN(1, 22)
#define PIN_RD                     RCAR_GP_PIN(1, 23)
#define PIN_RD_WR                  RCAR_GP_PIN(1, 24)
#define PIN_WE0                    RCAR_GP_PIN(1, 25)
#define PIN_WE1                    RCAR_GP_PIN(1, 26)
#define PIN_EX_WAIT0               RCAR_GP_PIN(1, 27)
#define PIN_CLKOUT                 RCAR_GP_PIN(1, 28)
#define PIN_IRQ0                   RCAR_GP_PIN(2, 0)
#define PIN_IRQ1                   RCAR_GP_PIN(2, 1)
#define PIN_IRQ2                   RCAR_GP_PIN(2, 2)
#define PIN_IRQ3                   RCAR_GP_PIN(2, 3)
#define PIN_IRQ4                   RCAR_GP_PIN(2, 4)
#define PIN_IRQ5                   RCAR_GP_PIN(2, 5)
#define PIN_PWM0                   RCAR_GP_PIN(2, 6)
#define PIN_PWM1_A                 RCAR_GP_PIN(2, 7)
#define PIN_PWM2_A                 RCAR_GP_PIN(2, 8)
#define PIN_AVB_MDC                RCAR_GP_PIN(2, 9)
#define PIN_AVB_MAGIC              RCAR_GP_PIN(2, 10)
#define PIN_AVB_PHY_INT            RCAR_GP_PIN(2, 11)
#define PIN_AVB_LINK               RCAR_GP_PIN(2, 12)
#define PIN_AVB_AVTP_MATCH_A       RCAR_GP_PIN(2, 13)
#define PIN_AVB_AVTP_CAPTURE_A     RCAR_GP_PIN(2, 14)
#define PIN_SD0_CLK                RCAR_GP_PIN(3, 0)
#define PIN_SD0_CMD                RCAR_GP_PIN(3, 1)
#define PIN_SD0_DATA0              RCAR_GP_PIN(3, 2)
#define PIN_SD0_DATA1              RCAR_GP_PIN(3, 3)
#define PIN_SD0_DATA2              RCAR_GP_PIN(3, 4)
#define PIN_SD0_DATA3              RCAR_GP_PIN(3, 5)
#define PIN_SD1_CLK                RCAR_GP_PIN(3, 6)
#define PIN_SD1_CMD                RCAR_GP_PIN(3, 7)
#define PIN_SD1_DATA0              RCAR_GP_PIN(3, 8)
#define PIN_SD1_DATA1              RCAR_GP_PIN(3, 9)
#define PIN_SD1_DATA2              RCAR_GP_PIN(3, 10)
#define PIN_SD1_DATA3              RCAR_GP_PIN(3, 11)
#define PIN_SD0_CD                 RCAR_GP_PIN(3, 12)
#define PIN_SD0_WP                 RCAR_GP_PIN(3, 13)
#define PIN_SD1_CD                 RCAR_GP_PIN(3, 14)
#define PIN_SD1_WP                 RCAR_GP_PIN(3, 15)
#define PIN_SD2_CLK                RCAR_GP_PIN(4, 0)
#define PIN_SD2_CMD                RCAR_GP_PIN(4,  1)
#define PIN_SD2_DATA0              RCAR_GP_PIN(4,  2)
#define PIN_SD2_DATA1              RCAR_GP_PIN(4,  3)
#define PIN_SD2_DATA2              RCAR_GP_PIN(4,  4)
#define PIN_SD2_DATA3              RCAR_GP_PIN(4,  5)
#define PIN_SD2_DS                 RCAR_GP_PIN(4,  6)
#define PIN_SD3_CLK                RCAR_GP_PIN(4,  7)
#define PIN_SD3_CMD                RCAR_GP_PIN(4,  8)
#define PIN_SD3_DATA0              RCAR_GP_PIN(4,  9)
#define PIN_SD3_DATA1              RCAR_GP_PIN(4,  10)
#define PIN_SD3_DATA2              RCAR_GP_PIN(4,  11)
#define PIN_SD3_DATA3              RCAR_GP_PIN(4,  12)
#define PIN_SD3_DATA4              RCAR_GP_PIN(4,  13)
#define PIN_SD3_DATA5              RCAR_GP_PIN(4,  14)
#define PIN_SD3_DATA6              RCAR_GP_PIN(4,  15)
#define PIN_SD3_DATA7              RCAR_GP_PIN(4,  16)
#define PIN_SD3_DS                 RCAR_GP_PIN(4,  17)
#define PIN_SCK0                   RCAR_GP_PIN(5, 0)
#define PIN_RX0                    RCAR_GP_PIN(5, 1)
#define PIN_TX0                    RCAR_GP_PIN(5, 2)
#define PIN_CTS0                   RCAR_GP_PIN(5, 3)
#define PIN_RTS0                   RCAR_GP_PIN(5, 4)
#define PIN_RX1_A                  RCAR_GP_PIN(5, 5)
#define PIN_TX1_A                  RCAR_GP_PIN(5, 6)
#define PIN_CTS1                   RCAR_GP_PIN(5, 7)
#define PIN_RTS1                   RCAR_GP_PIN(5, 8)
#define PIN_SCK2                   RCAR_GP_PIN(5, 9)
#define PIN_TX2_A                  RCAR_GP_PIN(5, 10)
#define PIN_RX2_A                  RCAR_GP_PIN(5, 11)
#define PIN_HSCK0                  RCAR_GP_PIN(5, 12)
#define PIN_HRX0                   RCAR_GP_PIN(5, 13)
#define PIN_HTX0                   RCAR_GP_PIN(5, 14)
#define PIN_HCTS0                  RCAR_GP_PIN(5, 15)
#define PIN_HRTS0                  RCAR_GP_PIN(5, 16)
#define PIN_MSIOF0_SCK             RCAR_GP_PIN(5, 17)
#define PIN_MSIOF0_SYNC            RCAR_GP_PIN(5, 18)
#define PIN_MSIOF0_SS1             RCAR_GP_PIN(5, 19)
#define PIN_MSIOF0_TXD             RCAR_GP_PIN(5, 20)
#define PIN_MSIOF0_SS2             RCAR_GP_PIN(5, 21)
#define PIN_MSIOF0_RXD             RCAR_GP_PIN(5, 22)
#define PIN_MLB_CLK                RCAR_GP_PIN(5, 23)
#define PIN_MLB_SIG                RCAR_GP_PIN(5, 24)
#define PIN_MLB_DAT                RCAR_GP_PIN(5, 25)
#define PIN_SSI_SCK01239           RCAR_GP_PIN(6, 0)
#define PIN_SSI_WS01239            RCAR_GP_PIN(6, 1)
#define PIN_SSI_SDATA0             RCAR_GP_PIN(6, 2)
#define PIN_SSI_SDATA1_A           RCAR_GP_PIN(6, 3)
#define PIN_SSI_SDATA2_A           RCAR_GP_PIN(6, 4)
#define PIN_SSI_SCK349             RCAR_GP_PIN(6, 5)
#define PIN_SSI_WS349              RCAR_GP_PIN(6, 6)
#define PIN_SSI_SDATA3             RCAR_GP_PIN(6, 7)
#define PIN_SSI_SCK4               RCAR_GP_PIN(6, 8)
#define PIN_SSI_WS4                RCAR_GP_PIN(6, 9)
#define PIN_SSI_SDAT_A4            RCAR_GP_PIN(6, 10)
#define PIN_SSI_SCK5               RCAR_GP_PIN(6, 11)
#define PIN_SSI_WS5                RCAR_GP_PIN(6, 12)
#define PIN_SSI_SDAT_A5            RCAR_GP_PIN(6, 13)
#define PIN_SSI_SCK6               RCAR_GP_PIN(6, 14)
#define PIN_SSI_WS6                RCAR_GP_PIN(6, 15)
#define PIN_SSI_SDATA6             RCAR_GP_PIN(6, 16)
#define PIN_SSI_SCK78              RCAR_GP_PIN(6, 17)
#define PIN_WS78                   RCAR_GP_PIN(6, 18)
#define PIN_SSI_SDATA7             RCAR_GP_PIN(6, 19)
#define PIN_SSI_SDATA8             RCAR_GP_PIN(6, 20)
#define PIN_SSI_SDATA9_A           RCAR_GP_PIN(6, 21)
#define PIN_AUDIO_CLKA_A           RCAR_GP_PIN(6, 22)
#define PIN_AUDIO_CLKB_B           RCAR_GP_PIN(6, 23)
#define PIN_USB0_PWEN              RCAR_GP_PIN(6, 24)
#define PIN_USB0_OVC               RCAR_GP_PIN(6, 25)
#define PIN_USB1_PWEN              RCAR_GP_PIN(6, 26)
#define PIN_USB1_OVC               RCAR_GP_PIN(6, 27)
#define PIN_USB30_PWEN             RCAR_GP_PIN(6, 28)
#define PIN_USB30_OVC              RCAR_GP_PIN(6, 29)
#define PIN_USB2_CH3_PWEN          RCAR_GP_PIN(6, 30)
#define PIN_USB2_CH3_OVC           RCAR_GP_PIN(6, 31)
#define PIN_AVS1                   RCAR_GP_PIN(7, 0)
#define PIN_AVS2                   RCAR_GP_PIN(7, 1)
#define PIN_GP7_02                 RCAR_GP_PIN(7, 2)
#define PIN_GP7_03                 RCAR_GP_PIN(7, 3)
#define PIN_ASEBRK                 RCAR_NOGP_PIN(1)
#define PIN_AVB_MDIO               RCAR_NOGP_PIN(2)
#define PIN_AVB_RD0                RCAR_NOGP_PIN(3)
#define PIN_AVB_RD1                RCAR_NOGP_PIN(4)
#define PIN_AVB_RD2                RCAR_NOGP_PIN(5)
#define PIN_AVB_RD3                RCAR_NOGP_PIN(6)
#define PIN_AVB_RXC                RCAR_NOGP_PIN(7)
#define PIN_AVB_RX_CTL             RCAR_NOGP_PIN(8)
#define PIN_AVB_TD0                RCAR_NOGP_PIN(9)
#define PIN_AVB_TD1                RCAR_NOGP_PIN(10)
#define PIN_AVB_TD2                RCAR_NOGP_PIN(11)
#define PIN_AVB_TD3                RCAR_NOGP_PIN(12)
#define PIN_AVB_TXC                RCAR_NOGP_PIN(13)
#define PIN_AVB_TXCREFCLK          RCAR_NOGP_PIN(14)
#define PIN_AVB_TX_CTL             RCAR_NOGP_PIN(15)
#define PIN_DU_DOTCLKIN0           RCAR_NOGP_PIN(16)
#define PIN_DU_DOTCLKIN1           RCAR_NOGP_PIN(17)
#define PIN_DU_DOTCLKIN2           RCAR_NOGP_PIN(18)
#define PIN_DU_DOTCLKIN3           RCAR_NOGP_PIN(19)
#define PIN_EXTALR                 RCAR_NOGP_PIN(20)
#define PIN_FSCLKST_N              RCAR_NOGP_PIN(21)
#define PIN_MLB_REF                RCAR_NOGP_PIN(22)
#define PIN_PRESETOUT_N            RCAR_NOGP_PIN(23)
#define PIN_QSPI0_IO2              RCAR_NOGP_PIN(24)
#define PIN_QSPI0_IO3              RCAR_NOGP_PIN(25)
#define PIN_QSPI0_MISO_IO1         RCAR_NOGP_PIN(26)
#define PIN_QSPI0_MOSI_IO0         RCAR_NOGP_PIN(27)
#define PIN_QSPI0_SPCLK            RCAR_NOGP_PIN(28)
#define PIN_QSPI0_SSL              RCAR_NOGP_PIN(29)
#define PIN_QSPI1_IO2              RCAR_NOGP_PIN(30)
#define PIN_QSPI1_IO3              RCAR_NOGP_PIN(31)
#define PIN_QSPI1_MISO_IO1         RCAR_NOGP_PIN(32)
#define PIN_QSPI1_MOSI_IO0         RCAR_NOGP_PIN(33)
#define PIN_QSPI1_SPCLK            RCAR_NOGP_PIN(34)
#define PIN_QSPI1_SSL              RCAR_NOGP_PIN(35)
#define PIN_RPC_INT_N              RCAR_NOGP_PIN(36)
#define PIN_RPC_RESET_N            RCAR_NOGP_PIN(37)
#define PIN_RPC_WP_N               RCAR_NOGP_PIN(38)
#define PIN_TCK                    RCAR_NOGP_PIN(39)
#define PIN_TDI                    RCAR_NOGP_PIN(40)
#define PIN_TDO                    RCAR_NOGP_PIN(41)
#define PIN_TMS                    RCAR_NOGP_PIN(42)
#define PIN_TRST_N                 RCAR_NOGP_PIN(43)

/* Pinmux function declarations */
#define FUNC_AVB_MDC                    IPSR(0, 0, 0)
#define FUNC_MSIOD2_SSI2_C              IPSR(0, 0, 3)
#define FUNC_AVB_MAGIC                  IPSR(0, 4, 0)
#define FUNC_MSIOF2_SSI1_C              IPSR(0, 4, 2)
#define FUNC_SCK4_A                     IPSR(0, 4, 3)
#define FUNC_AVB_PHY_INT                IPSR(0, 8, 0)
#define FUNC_MSIOF2_SYNC_C              IPSR(0, 8, 2)
#define FUNC_RX4_A                      IPSR(0, 8, 3)
#define FUNC_AVB_LINK                   IPSR(0, 12, 0)
#define FUNC_MSIOF2_SCK_C               IPSR(0, 12, 2)
#define FUNC_TX4_A                      IPSR(0, 12, 3)
#define FUNC_AVB_AVTP_MATCH_A           IPSR(0, 16, 0)
#define FUNC_MSIOF2_RXD_C               IPSR(0, 16, 2)
#define FUNC_CTS4_N_A                   IPSR(0, 16, 3)
#define FUNC_FSCLKST2_N_A               IPSR(0, 16, 5)
#define FUNC_AVB_AVTP_CAPTURE_A         IPSR(0, 20, 0)
#define FUNC_MSIOF2_TXD_C               IPSR(0, 20, 2)
#define FUNC_RTS4_N_A                   IPSR(0, 20, 3)
#define FUNC_IRQ0                       IPSR(0, 24, 0)
#define FUNC_QPOLB                      IPSR(0, 24, 1)
#define FUNC_DU_CDE                     IPSR(0, 24, 3)
#define FUNC_VI4_DATA0_B                IPSR(0, 24, 4)
#define FUNC_CAN0_TX_B                  IPSR(0, 24, 5)
#define FUNC_CANFD0_TX_B                IPSR(0, 24, 6)
#define FUNC_MSIOF3_SS2_E               IPSR(0, 24, 7)
#define FUNC_IRQ1                       IPSR(0, 28, 0)
#define FUNC_QPOLA                      IPSR(0, 28, 1)
#define FUNC_DU_DISP                    IPSR(0, 28, 3)
#define FUNC_VI4_DATA1_B                IPSR(0, 28, 4)
#define FUNC_CAN0_RX_B                  IPSR(0, 28, 5)
#define FUNC_CANFD0_RX_B                IPSR(0, 28, 6)
#define FUNC_MSIOF3_SS1_E               IPSR(0, 28, 7)
#define FUNC_IRQ2                       IPSR(1, 0, 0)
#define FUNC_QCPV_QDE                   IPSR(1, 0, 1)
#define FUNC_DU_EXODDF_DU_ODDF_DISP_CDE IPSR(1, 0, 3)
#define FUNC_VI4_DATA2_B                IPSR(1, 0, 4)
#define FUNC_MSIOF3_SYNC_E              IPSR(1, 0, 7)
#define FUNC_PWM3_B                     IPSR(1, 0, 9)
#define FUNC_IRQ3                       IPSR(1, 4, 0)
#define FUNC_QSTVB_QVE                  IPSR(1, 4, 1)
#define FUNC_DU_DOTCLKOUT1              IPSR(1, 4, 3)
#define FUNC_VI4_DATA3_B                IPSR(1, 4, 4)
#define FUNC_MSIOF3_SCK_E               IPSR(1, 4, 7)
#define FUNC_PWM4_B                     IPSR(1, 4, 9)
#define FUNC_IRQ4                       IPSR(1, 8, 0)
#define FUNC_QSTH_QHS                   IPSR(1, 8, 1)
#define FUNC_DU_EXHSYNC_DU_HSYNC        IPSR(1, 8, 3)
#define FUNC_VI4_DATA4_B                IPSR(1, 8, 4)
#define FUNC_MSIOF3_RXD_E               IPSR(1, 8, 7)
#define FUNC_PWM5_B                     IPSR(1, 8, 9)
#define FUNC_IRQ5                       IPSR(1, 12, 0)
#define FUNC_QSTB_QHE                   IPSR(1, 12, 1)
#define FUNC_DU_EXVSYNC_DU_VSYNC        IPSR(1, 12, 3)
#define FUNC_VI4_DATA5_B                IPSR(1, 12, 4)
#define FUNC_FSCLKST2_N_B               IPSR(1, 12, 5)
#define FUNC_MSIOF3_TXD_E               IPSR(1, 12, 7)
#define FUNC_PWM6_B                     IPSR(1, 12, 9)
#define FUNC_PWM0                       IPSR(1, 16, 0)
#define FUNC_AVB_AVTP_PPS               IPSR(1, 16, 1)
#define FUNC_VI4_DATA6_B                IPSR(1, 16, 4)
#define FUNC_IECLK_B                    IPSR(1, 16, 9)
#define FUNC_PWM1_A                     IPSR(1, 20, 0)
#define FUNC_HRX3_D                     IPSR(1, 20, 1)
#define FUNC_VI4_DATA7_B                IPSR(1, 20, 4)
#define FUNC_IERX_B                     IPSR(1, 20, 9)
#define FUNC_PWM2_A                     IPSR(1, 24, 0)
#define FUNC_HTX3_D                     IPSR(1, 24, 3)
#define FUNC_IETX_B                     IPSR(1, 24, 9)
#define FUNC_A0                         IPSR(1, 28, 0)
#define FUNC_LCDOUT16                   IPSR(1, 28, 1)
#define FUNC_MSIOF3_SYNC_B              IPSR(1, 28, 2)
#define FUNC_VI4_DATA8                  IPSR(1, 28, 4)
#define FUNC_DU_DB0                     IPSR(1, 28, 6)
#define FUNC_PWM3_A                     IPSR(1, 28, 9)
#define FUNC_A1                         IPSR(2, 0, 0)
#define FUNC_LCDOUT17                   IPSR(2, 0, 1)
#define FUNC_MSIOF3_TXD_B               IPSR(2, 0, 2)
#define FUNC_VI4_DATA9                  IPSR(2, 0, 4)
#define FUNC_DU_DB1                     IPSR(2, 0, 6)
#define FUNC_PWM4_A                     IPSR(2, 0, 9)
#define FUNC_A2                         IPSR(2, 4, 0)
#define FUNC_LCDOUT18                   IPSR(2, 4, 1)
#define FUNC_MSIOF3_SCK_B               IPSR(2, 4, 2)
#define FUNC_VI4_DATA10                 IPSR(2, 4, 4)
#define FUNC_DU_DB2                     IPSR(2, 4, 6)
#define FUNC_PWM5_A                     IPSR(2, 4, 9)
#define FUNC_A3                         IPSR(2, 8, 0)
#define FUNC_LCDOUT19                   IPSR(2, 8, 1)
#define FUNC_MSIOF3_RXD_B               IPSR(2, 8, 2)
#define FUNC_VI4_DATA11                 IPSR(2, 8, 4)
#define FUNC_DU_DB3                     IPSR(2, 8, 6)
#define FUNC_PWM6_A                     IPSR(2, 8, 9)
#define FUNC_A4                         IPSR(2, 12, 0)
#define FUNC_LCDOUT20                   IPSR(2, 12, 1)
#define FUNC_MSIOF3_SS1_B               IPSR(2, 12, 2)
#define FUNC_VI4_DATA12                 IPSR(2, 12, 4)
#define FUNC_VI5_DATA12                 IPSR(2, 12, 5)
#define FUNC_DU_DB4                     IPSR(2, 12, 6)
#define FUNC_A5                         IPSR(2, 16, 0)
#define FUNC_LCDOUT21                   IPSR(2, 16, 1)
#define FUNC_MSIOF3_SS2_B               IPSR(2, 16, 2)
#define FUNC_SCK4_B                     IPSR(2, 16, 3)
#define FUNC_VI4_DATA13                 IPSR(2, 16, 4)
#define FUNC_VI5_DATA13                 IPSR(2, 16, 5)
#define FUNC_DU_DB5                     IPSR(2, 16, 6)
#define FUNC_A6                         IPSR(2, 20, 0)
#define FUNC_LCDOUT22                   IPSR(2, 20, 1)
#define FUNC_MSIOF2_SS1_A               IPSR(2, 20, 2)
#define FUNC_RX4_B                      IPSR(2, 20, 3)
#define FUNC_VI4_DATA14                 IPSR(2, 20, 4)
#define FUNC_VI5_DATA14                 IPSR(2, 20, 5)
#define FUNC_DU_DB6                     IPSR(2, 20, 6)
#define FUNC_A7                         IPSR(2, 24, 0)
#define FUNC_LCDOUT23                   IPSR(2, 24, 1)
#define FUNC_MSIOF2_SS2_A               IPSR(2, 24, 2)
#define FUNC_TX4_B                      IPSR(2, 24, 3)
#define FUNC_VI4_DATA15                 IPSR(2, 24, 4)
#define FUNC_VI5_DATA15                 IPSR(2, 24, 5)
#define FUNC_DU_DB7                     IPSR(2, 24, 6)
#define FUNC_A8                         IPSR(2, 24, 0)
#define FUNC_RX3_B                      IPSR(2, 24, 1)
#define FUNC_MSIOF2_SYNC_A              IPSR(2, 24, 2)
#define FUNC_HRX4_B                     IPSR(2, 24, 3)
#define FUNC_SDA6_A                     IPSR(2, 24, 7)
#define FUNC_AVB_AVTP_MATCH_B           IPSR(2, 24, 8)
#define FUNC_PWM1_B                     IPSR(2, 24, 9)
#define FUNC_A9                         IPSR(3, 0, 0)
#define FUNC_MSIOF2_SCK_A               IPSR(3, 0, 2)
#define FUNC_CTS4_N_B                   IPSR(3, 0, 3)
#define FUNC_VI5_VSYNC_N                IPSR(3, 0, 5)
#define FUNC_A10                        IPSR(3, 4, 0)
#define FUNC_MSIOF2_RXD_A               IPSR(3, 4, 2)
#define FUNC_RTS4_N_B                   IPSR(3, 4, 3)
#define FUNC_VI5_HSYNC_N                IPSR(3, 4, 5)
#define FUNC_A11                        IPSR(3, 8, 0)
#define FUNC_TX3_B                      IPSR(3, 8, 1)
#define FUNC_MSIOF2_TXD_A               IPSR(3, 8, 2)
#define FUNC_HTX4_B                     IPSR(3, 8, 3)
#define FUNC_HSCK4                      IPSR(3, 8, 4)
#define FUNC_VI5_FIELD                  IPSR(3, 8, 5)
#define FUNC_SCL6_A                     IPSR(3, 8, 7)
#define FUNC_AVB_AVTP_CAPTURE_B         IPSR(3, 8, 8)
#define FUNC_PWM2_B                     IPSR(3, 8, 9)
#define FUNC_A12                        IPSR(3, 12, 0)
#define FUNC_LCDOUT12                   IPSR(3, 12, 1)
#define FUNC_MSIOF3_SCK_C               IPSR(3, 12, 2)
#define FUNC_HRX4_A                     IPSR(3, 12, 4)
#define FUNC_VI5_DATA8                  IPSR(3, 12, 5)
#define FUNC_DU_DG4                     IPSR(3, 12, 6)
#define FUNC_A13                        IPSR(3, 16, 0)
#define FUNC_LCDOUT13                   IPSR(3, 16, 1)
#define FUNC_MSIOF3_SYNC_C              IPSR(3, 16, 2)
#define FUNC_HTX4_A                     IPSR(3, 16, 5)
#define FUNC_VI5_DATA9                  IPSR(3, 16, 6)
#define FUNC_DU_DG5                     IPSR(3, 16, 7)
#define FUNC_A14                        IPSR(3, 20, 0)
#define FUNC_LCDOUT14                   IPSR(3, 20, 1)
#define FUNC_MSIOF3_RXD_C               IPSR(3, 20, 2)
#define FUNC_HCTS4_N                    IPSR(3, 20, 4)
#define FUNC_VI5_DATA10                 IPSR(3, 20, 5)
#define FUNC_DU_DG6                     IPSR(3, 20, 6)
#define FUNC_A15                        IPSR(3, 24, 0)
#define FUNC_LCDOUT15                   IPSR(3, 24, 1)
#define FUNC_MSIOF3_TXD_C               IPSR(3, 24, 2)
#define FUNC_HRTS4_N                    IPSR(3, 24, 4)
#define FUNC_VI5_DATA11                 IPSR(3, 24, 5)
#define FUNC_DU_DG7                     IPSR(3, 24, 6)
#define FUNC_A16                        IPSR(3, 28, 0)
#define FUNC_LCDOUT8                    IPSR(3, 28, 1)
#define FUNC_VI4_FIELD                  IPSR(3, 28, 4)
#define FUNC_DU_DG0                     IPSR(3, 28, 6)
#define FUNC_A17                        IPSR(4, 0, 0)
#define FUNC_LCDOUT9                    IPSR(4, 0, 1)
#define FUNC_VI4_VSYNC_N                IPSR(4, 0, 4)
#define FUNC_DU_DG1                     IPSR(4, 0, 6)
#define FUNC_A18                        IPSR(4, 4, 0)
#define FUNC_LCDOUT10                   IPSR(4, 4, 1)
#define FUNC_VI4_HSYNC_N                IPSR(4, 4, 4)
#define FUNC_DU_DG2                     IPSR(4, 4, 6)
#define FUNC_A19                        IPSR(4, 8, 0)
#define FUNC_LCDOUT11                   IPSR(4, 8, 1)
#define FUNC_VI4_CLKENB                 IPSR(4, 8, 4)
#define FUNC_DU_DG3                     IPSR(4, 8, 6)
#define FUNC_CS0_N                      IPSR(4, 12, 0)
#define FUNC_VI5_CLKENB                 IPSR(4, 12, 5)
#define FUNC_CS1_N                      IPSR(4, 16, 0)
#define FUNC_VI5_CLK                    IPSR(4, 16, 5)
#define FUNC_EX_WAIT0_B                 IPSR(4, 16, 7)
#define FUNC_BS_N                       IPSR(4, 20, 0)
#define FUNC_QSTVA_QVS                  IPSR(4, 20, 1)
#define FUNC_MSIOF3_SCK_D               IPSR(4, 20, 2)
#define FUNC_SCK3                       IPSR(4, 20, 3)
#define FUNC_HSCK3                      IPSR(4, 20, 4)
#define FUNC_CAN1_TX                    IPSR(4, 20, 8)
#define FUNC_CANFD1_TX                  IPSR(4, 20, 9)
#define FUNC_IETX_A                     IPSR(4, 20, 0xA)
#define FUNC_RD_N                       IPSR(4, 24, 0)
#define FUNC_MSIOF3_SYNC_D              IPSR(4, 24, 2)
#define FUNC_RX3_A                      IPSR(4, 24, 3)
#define FUNC_HRX3_A                     IPSR(4, 24, 4)
#define FUNC_CAN0_TX_A                  IPSR(4, 24, 8)
#define FUNC_CANFD0_TX_A                IPSR(4, 24, 9)
#define FUNC_RD_WR_N                    IPSR(4, 28, 0)
#define FUNC_MSIOF3_RXD_D               IPSR(4, 28, 2)
#define FUNC_TX3_A                      IPSR(4, 28, 3)
#define FUNC_HTX3_A                     IPSR(4, 28, 4)
#define FUNC_CAN0_RX_A                  IPSR(4, 28, 8)
#define FUNC_CANFD0_RX_A                IPSR(4, 28, 9)
#define FUNC_WE0_N                      IPSR(5, 0, 0)
#define FUNC_MSIOF3_TXD_D               IPSR(5, 0, 2)
#define FUNC_CTS3_N                     IPSR(5, 0, 3)
#define FUNC_HCTS3_N                    IPSR(5, 0, 4)
#define FUNC_SCL6_B                     IPSR(5, 0, 7)
#define FUNC_CAN_CLK                    IPSR(5, y, 8)
#define FUNC_IECLK_A                    IPSR(5, 0, 0xA)
#define FUNC_WE1_N                      IPSR(5, 4, 0)
#define FUNC_MSIOF3_SS1_D               IPSR(5, 4, 2)
#define FUNC_RTS3_N                     IPSR(5, 4, 3)
#define FUNC_HRTS3_N                    IPSR(5, 4, 4)
#define FUNC_SDA6_B                     IPSR(5, 4, 7)
#define FUNC_CAN1_RX                    IPSR(5, 4, 8)
#define FUNC_CANFD1_RX                  IPSR(5, 4, 9)
#define FUNC_IERX_A                     IPSR(5, 4, 0xA)
#define FUNC_EX_WAIT0_A                 IPSR(5, 8, 0)
#define FUNC_QCLK                       IPSR(5, 8, 1)
#define FUNC_VI4_CLK                    IPSR(5, 8, 4)
#define FUNC_DU_DOTCLKOUT0              IPSR(5, 8, 6)
#define FUNC_D0                         IPSR(5, 12, 0)
#define FUNC_MSIOF2_SS1_B               IPSR(5, 12, 1)
#define FUNC_MSIOF3_SCK_A               IPSR(5, 12, 2)
#define FUNC_VI4_DATA16                 IPSR(5, 12, 4)
#define FUNC_VI5_DATA0                  IPSR(5, 12, 5)
#define FUNC_D1                         IPSR(5, 16, 0)
#define FUNC_MSIOF2_SS2_B               IPSR(5, 16, 1)
#define FUNC_MSIOF3_SYNC_A              IPSR(5, 12, 2)
#define FUNC_VI4_DATA17                 IPSR(5, 16, 4)
#define FUNC_VI5_DATA1                  IPSR(5, 16, 5)
#define FUNC_D2                         IPSR(5, 20, 0)
#define FUNC_MSIOF3_RXD_A               IPSR(5, 20, 2)
#define FUNC_VI4_DATA18                 IPSR(5, 20, 4)
#define FUNC_VI5_DATA2                  IPSR(5, 20, 5)
#define FUNC_D3                         IPSR(5, 24, 0)
#define FUNC_MSIOF3_TXD_A               IPSR(5, 24, 2)
#define FUNC_VI4_DATA19                 IPSR(5, 24, 4)
#define FUNC_VI5_DATA3                  IPSR(5, 24, 5)
#define FUNC_D4                         IPSR(5, 28, 0)
#define FUNC_MSIOF2_SCK_B               IPSR(5, 28, 1)
#define FUNC_VI4_DATA20                 IPSR(5, 28, 4)
#define FUNC_VI5_DATA4                  IPSR(5, 28, 5)
#define FUNC_D5                         IPSR(6, 0, 0)
#define FUNC_MSIOF2_SYNC_B              IPSR(6, 0, 1)
#define FUNC_VI4_DATA21                 IPSR(6, 0, 4)
#define FUNC_VI5_DATA5                  IPSR(6, 0, 5)
#define FUNC_D6                         IPSR(6, 4, 0)
#define FUNC_MSIOF2_RXD_B               IPSR(6, 4, 1)
#define FUNC_VI4_DATA22                 IPSR(6, 4, 4)
#define FUNC_VI5_DATA6                  IPSR(6, 4, 5)
#define FUNC_D7                         IPSR(6, 8, 0)
#define FUNC_MSIOF2_TXD_B               IPSR(6, 8, 1)
#define FUNC_VI4_DATA23                 IPSR(6, 8, 4)
#define FUNC_VI5_DATA7                  IPSR(6, 8, 5)
#define FUNC_D8                         IPSR(6, 12, 0)
#define FUNC_LCDOUT0                    IPSR(6, 12, 1)
#define FUNC_MSIOF2_SCK_D               IPSR(6, 12, 2)
#define FUNC_SCK4_C                     IPSR(6, 12, 3)
#define FUNC_VI4_DATA0_A                IPSR(6, 12, 4)
#define FUNC_DU_DR0                     IPSR(6, 12, 6)
#define FUNC_D9                         IPSR(6, 16, 0)
#define FUNC_LCDOUT1                    IPSR(6, 16, 1)
#define FUNC_MSIOF2_SYNC_D              IPSR(6, 16, 2)
#define FUNC_VI4_DATA1_A                IPSR(6, 16, 4)
#define FUNC_DU_DR1                     IPSR(6, 16, 6)
#define FUNC_D10                        IPSR(6, 20, 0)
#define FUNC_LCDOUT2                    IPSR(6, 20, 1)
#define FUNC_MSIOF2_RXD_D               IPSR(6, 20, 2)
#define FUNC_HRX3_B                     IPSR(6, 20, 3)
#define FUNC_VI4_DATA2_A                IPSR(6, 20, 4)
#define FUNC_CTS4_N_C                   IPSR(6, 20, 5)
#define FUNC_DU_DR2                     IPSR(6, 20, 6)
#define FUNC_D11                        IPSR(6, 24, 0)
#define FUNC_LCDOUT3                    IPSR(6, 24, 1)
#define FUNC_MSIOF2_TXD_D               IPSR(6, 24, 2)
#define FUNC_HTX3_B                     IPSR(6, 24, 3)
#define FUNC_VI4_DATA3_A                IPSR(6, 24, 4)
#define FUNC_RTS4_N_C                   IPSR(6, 24, 5)
#define FUNC_DU_DR3                     IPSR(6, 24, 6)
#define FUNC_D12                        IPSR(6, 28, 0)
#define FUNC_LCDOUT4                    IPSR(6, 28, 1)
#define FUNC_MSIOF2_SS1_D               IPSR(6, 28, 2)
#define FUNC_RX4_C                      IPSR(6, 28, 3)
#define FUNC_VI4_DATA4_A                IPSR(6, 28, 4)
#define FUNC_DU_DR4                     IPSR(6, 28, 6)
#define FUNC_D13                        IPSR(7, 0, 0)
#define FUNC_LCDOUT5                    IPSR(7, 0, 1)
#define FUNC_MSIOF2_SS2_D               IPSR(7, 0, 2)
#define FUNC_TX4_C                      IPSR(7, 0, 3)
#define FUNC_VI4_DATA5_A                IPSR(7, 0, 4)
#define FUNC_DU_DR5                     IPSR(7, 0, 6)
#define FUNC_D14                        IPSR(7, 4, 0)
#define FUNC_LCDOUT6                    IPSR(7, 4, 1)
#define FUNC_MSIOF3_SS1_A               IPSR(7, 4, 2)
#define FUNC_HRX3_C                     IPSR(7, 4, 3)
#define FUNC_VI4_DATA6_A                IPSR(7, 4, 4)
#define FUNC_DU_DR6                     IPSR(7, 4, 6)
#define FUNC_SCL6_C                     IPSR(7, 4, 7)
#define FUNC_D15                        IPSR(7, 8, 0)
#define FUNC_LCDOUT7                    IPSR(7, 8, 1)
#define FUNC_MSIOF3_SS2_A               IPSR(7, 8, 2)
#define FUNC_HTX3_C                     IPSR(7, 8, 3)
#define FUNC_VI4_DATA7_A                IPSR(7, 8, 4)
#define FUNC_DU_DR7                     IPSR(7, 8, 6)
#define FUNC_SDA6_C                     IPSR(7, 8, 7)
#define FUNC_SD0_CLK                    IPSR(7, 12, 0)
#define FUNC_MSIOF1_SCK_E               IPSR(7, 12, 2)
#define FUNC_STP_OPWM_0_B               IPSR(7, 12, 6)
#define FUNC_SD0_CMD                    IPSR(7, 16, 0)
#define FUNC_MSIOF1_SYNC_E              IPSR(7, 16, 2)
#define FUNC_STP_IVCXO27_0_B            IPSR(7, 16, 6)
#define FUNC_SD0_DAT0                   IPSR(7, 20, 0)
#define FUNC_MSIOF1_RXD_E               IPSR(7, 20, 2)
#define FUNC_TS_SCK0_B                  IPSR(7, 20, 5)
#define FUNC_STP_ISCLK_0_B              IPSR(7, 20, 6)
#define FUNC_SD0_DAT1                   IPSR(7, 24, 0)
#define FUNC_MSIOF1_TXD_E               IPSR(7, 24, 2)
#define FUNC_TS_SPSYNC0_B               IPSR(7, 24, 5)
#define FUNC_STP_ISSYNC_0_B             IPSR(7, 24, 6)
#define FUNC_SD0_DAT2                   IPSR(8, 0, 0)
#define FUNC_MSIOF1_SS1_E               IPSR(8, 0, 2)
#define FUNC_TS_SDAT0_B                 IPSR(8, 0, 5)
#define FUNC_STP_ISD_0_B                IPSR(8, 0, 6)
#define FUNC_SD0_DAT3                   IPSR(8, 4, 0)
#define FUNC_MSIOF1_SS2_E               IPSR(8, 4, 2)
#define FUNC_TS_SDEN0_B                 IPSR(8, 4, 5)
#define FUNC_STP_ISEN_0_B               IPSR(8, 4, 6)
#define FUNC_SD1_CLK                    IPSR(8, 8, 0)
#define FUNC_MSIOF1_SCK_G               IPSR(8, 8, 2)
#define FUNC_SIM0_CLK_A                 IPSR(8, 8, 5)
#define FUNC_SD1_CMD                    IPSR(8, 12, 0)
#define FUNC_MSIOF1_SYNC_G              IPSR(8, 12, 2)
#define FUNC_NFCE_N_B                   IPSR(8, 12, 3)
#define FUNC_SIM0_D_A                   IPSR(8, 12, 5)
#define FUNC_STP_IVCXO27_1_B            IPSR(8, 12, 6)
#define FUNC_SD1_DAT0                   IPSR(8, 16, 0)
#define FUNC_SD2_DAT4                   IPSR(8, 16, 1)
#define FUNC_MSIOF1_RXD_G               IPSR(8, 16, 2)
#define FUNC_NFWP_N_B                   IPSR(8, 16, 3)
#define FUNC_TS_SCK1_B                  IPSR(8, 16, 5)
#define FUNC_STP_ISCLK_1_B              IPSR(8, 16, 6)
#define FUNC_SD1_DAT1                   IPSR(8, 20, 0)
#define FUNC_SD2_DAT5                   IPSR(8, 20, 1)
#define FUNC_MSIOF1_TXD_G               IPSR(8, 20, 2)
#define FUNC_NFDATA14_B                 IPSR(8, 20, 3)
#define FUNC_TS_SPSYNC1_B               IPSR(8, 20, 5)
#define FUNC_STP_ISSYNC_1_B             IPSR(8, 20, 6)
#define FUNC_SD1_DAT2                   IPSR(8, 24, 0)
#define FUNC_SD2_DAT6                   IPSR(8, 24, 1)
#define FUNC_MSIOF1_SS1_G               IPSR(8, 24, 2)
#define FUNC_NFDATA15_B                 IPSR(8, 24, 3)
#define FUNC_TS_SDAT1_B                 IPSR(8, 24, 5)
#define FUNC_STP_ISD_1_B                IPSR(8, 24, 6)
#define FUNC_SD1_DAT3                   IPSR(8, 28, 0)
#define FUNC_SD2_DAT7                   IPSR(8, 28, 1)
#define FUNC_MSIOF1_SS2_G               IPSR(8, 28, 2)
#define FUNC_NFRB_N_B                   IPSR(8, 28, 3)
#define FUNC_TS_SDEN1_B                 IPSR(8, 28, 5)
#define FUNC_STP_ISEN_1_B               IPSR(8, 28, 6)
#define FUNC_SD2_CLK                    IPSR(9, 0, 0)
#define FUNC_NFDATA8                    IPSR(9, 0, 2)
#define FUNC_SD2_CMD                    IPSR(9, 4, 0)
#define FUNC_NFDATA9                    IPSR(9, 4, 2)
#define FUNC_SD2_DAT0                   IPSR(9, 8, 0)
#define FUNC_NFDATA10                   IPSR(9, 8, 2)
#define FUNC_SD2_DAT1                   IPSR(9, 12, 0)
#define FUNC_NFDATA11                   IPSR(9, 12, 2)
#define FUNC_SD2_DAT2                   IPSR(9, 16, 0)
#define FUNC_NFDATA12                   IPSR(9, 16, 2)
#define FUNC_SD2_DAT3                   IPSR(9, 20, 0)
#define FUNC_NFDATA13                   IPSR(9, 20, 2)
#define FUNC_SD2_DS                     IPSR(9, 24, 0)
#define FUNC_NFALE                      IPSR(9, 24, 2)
#define FUNC_SATA_DEVSLP_B              IPSR(9, 24, 8)
#define FUNC_SD3_CLK                    IPSR(9, 28, 0)
#define FUNC_NFWE_N                     IPSR(9, 28, 2)
#define FUNC_SD3_CMD                    IPSR(10, 0, 0)
#define FUNC_NFRE_N                     IPSR(10, 0, 2)
#define FUNC_SD3_DAT0                   IPSR(10, 4, 0)
#define FUNC_NFDATA0                    IPSR(10, 4, 2)
#define FUNC_SD3_DAT1                   IPSR(10, 8, 0)
#define FUNC_NFDATA1                    IPSR(10, 8, 2)
#define FUNC_SD3_DAT2                   IPSR(10, 12, 0)
#define FUNC_NFDATA2                    IPSR(10, 12, 2)
#define FUNC_SD3_DAT3                   IPSR(10, 16, 0)
#define FUNC_NFDATA3                    IPSR(10, 16, 2)
#define FUNC_SD3_DAT4                   IPSR(10, 20, 0)
#define FUNC_SD2_CD_A                   IPSR(10, 20, 1)
#define FUNC_NFDATA4                    IPSR(10, 20, 2)
#define FUNC_SD3_DAT5                   IPSR(10, 24, 0)
#define FUNC_SD2_WP_A                   IPSR(10, 24, 1)
#define FUNC_NFDATA5                    IPSR(10, 24, 2)
#define FUNC_SD3_DAT6                   IPSR(10, 28, 0)
#define FUNC_SD3_CD                     IPSR(10, 28, 1)
#define FUNC_NFDATA6                    IPSR(10, 28, 2)
#define FUNC_SD3_DAT7                   IPSR(11, 0, 0)
#define FUNC_SD3_WP                     IPSR(11, 0, 1)
#define FUNC_NFDATA7                    IPSR(11, 0, 2)
#define FUNC_SD3_DS                     IPSR(11, 4, 0)
#define FUNC_NFCLE                      IPSR(11, 4, 2)
#define FUNC_SD0_CD                     IPSR(11, 8, 0)
#define FUNC_NFDATA14_A                 IPSR(11, 8, 2)
#define FUNC_SCL2_B                     IPSR(11, 8, 4)
#define FUNC_SIM0_RST_A                 IPSR(11, 8, 5)
#define FUNC_SD0_WP                     IPSR(11, 12, 0)
#define FUNC_NFDATA15_A                 IPSR(11, 12, 2)
#define FUNC_SDA2_B                     IPSR(11, 12, 4)
#define FUNC_SD1_CD                     IPSR(11, 16, 0)
#define FUNC_NFRB_N_A                   IPSR(11, 16, 2)
#define FUNC_SIM0_CLK_B                 IPSR(11, 16, 5)
#define FUNC_SD1_WP                     IPSR(11, 20, 0)
#define FUNC_NFCE_N_A                   IPSR(11, 20, 2)
#define FUNC_SIM0_D_B                   IPSR(11, 20, 5)
#define FUNC_SCK0                       IPSR(11, 24, 0)
#define FUNC_HSCK1_B                    IPSR(11, 24, 1)
#define FUNC_MSIOF1_SS2_B               IPSR(11, 24, 2)
#define FUNC_AUDIO_CLKC_B               IPSR(11, 24, 3)
#define FUNC_SDA2_A                     IPSR(11, 24, 4)
#define FUNC_SIM0_RST_B                 IPSR(11, 24, 5)
#define FUNC_STP_OPWM_0_C               IPSR(11, 24, 6)
#define FUNC_RIF0_CLK_B                 IPSR(11, 24, 7)
#define FUNC_ADICHS2                    IPSR(11, 24, 9)
#define FUNC_SCK5_B                     IPSR(11, 24, 0xA)
#define FUNC_RX0                        IPSR(11, 28, 0)
#define FUNC_HRX1_B                     IPSR(11, 28, 1)
#define FUNC_TS_SCK0_C                  IPSR(11, 28, 5)
#define FUNC_STP_ISCLK_0_C              IPSR(11, 28, 6)
#define FUNC_RIF0_D0_B                  IPSR(11, 28, 7)
#define FUNC_TX0                        IPSR(12, 0, 0)
#define FUNC_HTX1_B                     IPSR(12, 0, 1)
#define FUNC_TS_SPSYNC0_C               IPSR(12, 0, 5)
#define FUNC_STP_ISSYNC_0_C             IPSR(12, 0, 6)
#define FUNC_RIF0_D1_B                  IPSR(12, 0, 7)
#define FUNC_CTS0_N                     IPSR(12, 4, 0)
#define FUNC_HCTS1_N_B                  IPSR(12, 4, 1)
#define FUNC_MSIOF1_SYNC_B              IPSR(12, 4, 2)
#define FUNC_TS_SPSYNC1_C               IPSR(12, 4, 5)
#define FUNC_STP_ISSYNC_1_C             IPSR(12, 4, 6)
#define FUNC_RIF1_SYNC_B                IPSR(12, 4, 7)
#define FUNC_AUDIO_CLKOUT_C             IPSR(12, 4, 8)
#define FUNC_ADICS_SAMP                 IPSR(12, 4, 9)
#define FUNC_RTS0_N                     IPSR(12, 8, 0)
#define FUNC_HRTS1_N_B                  IPSR(12, 8, 1)
#define FUNC_MSIOF1_SS1_B               IPSR(12, 8, 2)
#define FUNC_AUDIO_CLKA_B               IPSR(12, 8, 3)
#define FUNC_SCL2_A                     IPSR(12, 8, 4)
#define FUNC_STP_IVCXO27_1_C            IPSR(12, 8, 6)
#define FUNC_RIF0_SYNC_B                IPSR(12, 8, 7)
#define FUNC_ADICHS1                    IPSR(12, 8, 9)
#define FUNC_RX1_A                      IPSR(12, 12, 0)
#define FUNC_HRX1_A                     IPSR(12, 12, 1)
#define FUNC_TS_SDAT0_C                 IPSR(12, 12, 5)
#define FUNC_STP_ISD_0_C                IPSR(12, 12, 6)
#define FUNC_RIF1_CLK_C                 IPSR(12, 12, 7)
#define FUNC_TX1_A                      IPSR(12, 16, 0)
#define FUNC_HTX1_A                     IPSR(12, 16, 1)
#define FUNC_TS_SDEN0_C                 IPSR(12, 16, 5)
#define FUNC_STP_ISEN_0_C               IPSR(12, 16, 6)
#define FUNC_RIF1_D0_C                  IPSR(12, 16, 7)
#define FUNC_CTS1_N                     IPSR(12, 20, 0)
#define FUNC_HCTS1_N_A                  IPSR(12, 20, 1)
#define FUNC_MSIOF1_RXD_B               IPSR(12, 20, 2)
#define FUNC_TS_SDEN1_C                 IPSR(12, 20, 5)
#define FUNC_STP_ISEN_1_C               IPSR(12, 20, 6)
#define FUNC_RIF1_D0_B                  IPSR(12, 20, 7)
#define FUNC_ADIDATA                    IPSR(12, 20, 9)
#define FUNC_RTS1_N                     IPSR(12, 24, 0)
#define FUNC_HRTS1_N_A                  IPSR(12, 24, 1)
#define FUNC_MSIOF1_TXD_B               IPSR(12, 24, 2)
#define FUNC_TS_SDAT1_C                 IPSR(12, 24, 5)
#define FUNC_STP_ISD_1_C                IPSR(12, 24, 6)
#define FUNC_RIF1_D1_B                  IPSR(12, 24, 7)
#define FUNC_ADICHS0                    IPSR(12, 24, 9)
#define FUNC_SCK2                       IPSR(12, 28, 0)
#define FUNC_SCIF_CLK_B                 IPSR(12, 28, 1)
#define FUNC_MSIOF1_SCK_B               IPSR(12, 28, 2)
#define FUNC_TS_SCK1_C                  IPSR(12, 28, 5)
#define FUNC_STP_ISCLK_1_C              IPSR(12, 28, 6)
#define FUNC_RIF1_CLK_B                 IPSR(12, 28, 7)
#define FUNC_ADICLK                     IPSR(12, 28, 9)
#define FUNC_TX2_A                      IPSR(13, 0, 0)
#define FUNC_SD2_CD_B                   IPSR(13, 0, 3)
#define FUNC_SCL1_A                     IPSR(13, 0, 4)
#define FUNC_FMCLK_A                    IPSR(13, 0, 6)
#define FUNC_RIF1_D1_C                  IPSR(13, 0, 7)
#define FUNC_FSO_CFE_0_N                IPSR(13, 0, 9)
#define FUNC_RX2_A                      IPSR(13, 4, 0)
#define FUNC_SD2_WP_B                   IPSR(13, 4, 3)
#define FUNC_SDA1_A                     IPSR(13, 4, 4)
#define FUNC_FMIN_A                     IPSR(13, 4, 6)
#define FUNC_RIF1_SYNC_C                IPSR(13, 4, 7)
#define FUNC_FSO_CFE_1_N                IPSR(13, 4, 9)
#define FUNC_HSCK0                      IPSR(13, 8, 0)
#define FUNC_MSIOF1_SCK_D               IPSR(13, 8, 2)
#define FUNC_AUDIO_CLKB_A               IPSR(13, 8, 3)
#define FUNC_SSI_SDATA1_B               IPSR(13, 8, 4)
#define FUNC_TS_SCK0_D                  IPSR(13, 8, 5)
#define FUNC_STP_ISCLK_0_D              IPSR(13, 8, 6)
#define FUNC_RIF0_CLK_C                 IPSR(13, 8, 7)
#define FUNC_RX5_B                      IPSR(13, 8, 0xA)
#define FUNC_HRX0                       IPSR(13, 12, 0)
#define FUNC_MSIOF1_RXD_D               IPSR(13, 12, 2)
#define FUNC_SSI_SDATA2_B               IPSR(13, 12, 4)
#define FUNC_TS_SDEN0_D                 IPSR(13, 12, 5)
#define FUNC_STP_ISEN_0_D               IPSR(13, 12, 6)
#define FUNC_RIF0_D0_C                  IPSR(13, 12, 7)
#define FUNC_HTX0                       IPSR(13, 16, 0)
#define FUNC_MSIOF1_TXD_D               IPSR(13, 16, 2)
#define FUNC_SSI_SDATA9_B               IPSR(13, 16, 4)
#define FUNC_TS_SDAT0_D                 IPSR(13, 16, 5)
#define FUNC_STP_ISD_0_D                IPSR(13, 16, 6)
#define FUNC_RIF0_D1_C                  IPSR(13, 16, 7)
#define FUNC_HCTS0_N                    IPSR(13, 20, 0)
#define FUNC_RX2_B                      IPSR(13, 20, 1)
#define FUNC_MSIOF1_SYNC_D              IPSR(13, 20, 2)
#define FUNC_SSI_SCK9_A                 IPSR(13, 20, 4)
#define FUNC_TS_SPSYNC0_D               IPSR(13, 20, 5)
#define FUNC_STP_ISSYNC_0_D             IPSR(13, 20, 6)
#define FUNC_RIF0_SYNC_C                IPSR(13, 20, 7)
#define FUNC_AUDIO_CLKOUT1_A            IPSR(13, 20, 8)
#define FUNC_HRTS0_N                    IPSR(13, 24, 0)
#define FUNC_TX2_B                      IPSR(13, 24, 1)
#define FUNC_MSIOF1_SS1_D               IPSR(13, 24, 2)
#define FUNC_SSI_WS9_A                  IPSR(13, 24, 4)
#define FUNC_STP_IVCXO27_0_D            IPSR(13, 24, 6)
#define FUNC_BPFCLK_A                   IPSR(13, 24, 7)
#define FUNC_AUDIO_CLKOUT2_A            IPSR(13, 24, 8)
#define FUNC_MSIOF0_SYNC                IPSR(13, 28, 0)
#define FUNC_AUDIO_CLKOUT_A             IPSR(13, 28, 8)
#define FUNC_TX5_B                      IPSR(13, 28, 0xA)
#define FUNC_MSIOF0_SS1                 IPSR(14, 0, 0)
#define FUNC_RX5_A                      IPSR(14, 0, 1)
#define FUNC_NFWP_N_A                   IPSR(14, 0, 2)
#define FUNC_AUDIO_CLKA_C               IPSR(14, 0, 3)
#define FUNC_SSI_SCK2_A                 IPSR(14, 0, 4)
#define FUNC_STP_IVCXO27_0_C            IPSR(14, 0, 6)
#define FUNC_AUDIO_CLKOUT3_A            IPSR(14, 0, 8)
#define FUNC_TCLK1_B                    IPSR(14, 0, 0xA)
#define FUNC_MSIOF0_SS2                 IPSR(14, 4, 0)
#define FUNC_TX5_A                      IPSR(14, 4, 1)
#define FUNC_MSIOF1_SS2_D               IPSR(14, 4, 2)
#define FUNC_AUDIO_CLKC_A               IPSR(14, 4, 3)
#define FUNC_SSI_WS2_A                  IPSR(14, 4, 4)
#define FUNC_STP_OPWM_0_D               IPSR(14, 4, 6)
#define FUNC_AUDIO_CLKOUT_D             IPSR(14, 4, 8)
#define FUNC_SPEEDIN_B                  IPSR(14, 4, 0xA)
#define FUNC_MLB_CLK                    IPSR(14, 4, 0)
#define FUNC_MSIOF1_SCK_F               IPSR(14, 4, 2)
#define FUNC_SCL1_B                     IPSR(14, 4, 4)
#define FUNC_MLB_SIG                    IPSR(14, 8, 0)
#define FUNC_RX1_B                      IPSR(14, 8, 1)
#define FUNC_MSIOF1_SYNC_F              IPSR(14, 8, 2)
#define FUNC_SDA1_B                     IPSR(14, 8, 4)
#define FUNC_MLB_DAT                    IPSR(14, 12, 0)
#define FUNC_TX1_B                      IPSR(14, 12, 1)
#define FUNC_MSIOF1_RXD_F               IPSR(14, 12, 2)
#define FUNC_SSI_SCK01239               IPSR(14, 16, 0)
#define FUNC_MSIOF1_TXD_F               IPSR(14, 16, 2)
#define FUNC_SSI_WS01239                IPSR(14, 16, 0)
#define FUNC_MSIOF1_SS1_F               IPSR(14, 16, 2)
#define FUNC_SSI_SDATA0                 IPSR(14, 20, 0)
#define FUNC_MSIOF1_SS2_F               IPSR(14, 20, 2)
#define FUNC_SSI_SDATA1_A               IPSR(15, 0, 0)
#define FUNC_SSI_SDATA2_A               IPSR(15, 4, 0)
#define FUNC_SSI_SCK1_B                 IPSR(15, 4, 4)
#define FUNC_SSI_SCK349                 IPSR(15, 8, 0)
#define FUNC_MSIOF1_SS1_A               IPSR(15, 8, 2)
#define FUNC_STP_OPWM_0_A               IPSR(15, 8, 6)
#define FUNC_SSI_WS349                  IPSR(15, 12, 0)
#define FUNC_HCTS2_N_A                  IPSR(15, 12, 1)
#define FUNC_MSIOF1_SS2_A               IPSR(15, 12, 2)
#define FUNC_STP_IVCXO27_0_A            IPSR(15, 12, 6)
#define FUNC_SSI_SDATA3                 IPSR(15, 16, 0)
#define FUNC_HRTS2_N_A                  IPSR(15, 16, 1)
#define FUNC_MSIOF1_TXD_A               IPSR(15, 16, 2)
#define FUNC_TS_SCK0_A                  IPSR(15, 16, 5)
#define FUNC_STP_ISCLK_0_A              IPSR(15, 16, 6)
#define FUNC_RIF0_D1_A                  IPSR(15, 16, 7)
#define FUNC_RIF2_D0_A                  IPSR(15, 16, 8)
#define FUNC_SSI_SCK4                   IPSR(15, 20, 0)
#define FUNC_HRX2_A                     IPSR(15, 20, 1)
#define FUNC_MSIOF1_SCK_A               IPSR(15, 20, 2)
#define FUNC_TS_SDAT0_A                 IPSR(15, 20, 5)
#define FUNC_STP_ISD_0_A                IPSR(15, 20, 6)
#define FUNC_RIF0_CLK_A                 IPSR(15, 20, 7)
#define FUNC_RIF2_CLK_A                 IPSR(15, 20, 8)
#define FUNC_SSI_WS4                    IPSR(15, 24, 0)
#define FUNC_HTX2_A                     IPSR(15, 24, 1)
#define FUNC_MSIOF1_SYNC_A              IPSR(15, 24, 2)
#define FUNC_TS_SDEN0_A                 IPSR(15, 24, 5)
#define FUNC_STP_ISEN_0_A               IPSR(15, 24, 6)
#define FUNC_RIF0_SYNC_A                IPSR(15, 24, 7)
#define FUNC_RIF2_SYNC_A                IPSR(15, 24, 8)
#define FUNC_SSI_SDATA4                 IPSR(15, 28, 0)
#define FUNC_HSCK2_A                    IPSR(15, 28, 1)
#define FUNC_MSIOF1_RXD_A               IPSR(15, 28, 2)
#define FUNC_TS_SPSYNC0_A               IPSR(15, 28, 5)
#define FUNC_STP_ISSYNC_0_A             IPSR(15, 28, 6)
#define FUNC_RIF0_D0_A                  IPSR(15, 28, 7)
#define FUNC_RIF2_D1_A                  IPSR(15, 28, 8)
#define FUNC_SSI_SCK6                   IPSR(16, 0, 0)
#define FUNC_USB2_PWEN                  IPSR(16, 0, 1)
#define FUNC_SIM0_RST_D                 IPSR(16, 0, 3)
#define FUNC_SSI_WS6                    IPSR(16, 4, 0)
#define FUNC_USB2_OVC                   IPSR(16, 4, 1)
#define FUNC_SIM0_D_D                   IPSR(16, 4, 3)
#define FUNC_SSI_SDATA6                 IPSR(16, 8, 0)
#define FUNC_SIM0_CLK_D                 IPSR(16, 8, 3)
#define FUNC_SATA_DEVSLP_A              IPSR(16, 8, 8)
#define FUNC_SSI_SCK78                  IPSR(16, 12, 0)
#define FUNC_HRX2_B                     IPSR(16, 12, 1)
#define FUNC_MSIOF1_SCK_C               IPSR(16, y, 2)
#define FUNC_TS_SCK1_A                  IPSR(16, y, 5)
#define FUNC_STP_ISCLK_1_A              IPSR(16, y, 6)
#define FUNC_RIF1_CLK_A                 IPSR(16, y, 7)
#define FUNC_RIF3_CLK_A                 IPSR(16, y, 8)
#define FUNC_SSI_WS78                   IPSR(16, 16, 0)
#define FUNC_HTX2_B                     IPSR(16, 16, 1)
#define FUNC_MSIOF1_SYNC_C              IPSR(16, 16, 2)
#define FUNC_TS_SDAT1_A                 IPSR(16, 16, 5)
#define FUNC_STP_ISD_1_A                IPSR(16, 16, 6)
#define FUNC_RIF1_SYNC_A                IPSR(16, 16, 7)
#define FUNC_RIF3_SYNC_A                IPSR(16, 16, 8)
#define FUNC_SSI_SDATA7                 IPSR(16, 20, 0)
#define FUNC_HCTS2_N_B                  IPSR(16, 20, 1)
#define FUNC_MSIOF1_RXD_C               IPSR(16, 20, 2)
#define FUNC_TS_SDEN1_A                 IPSR(16, 20, 5)
#define FUNC_STP_ISEN_1_A               IPSR(16, 20, 6)
#define FUNC_RIF1_D0_A                  IPSR(16, 20, 7)
#define FUNC_RIF3_D0_A                  IPSR(16, 20, 8)
#define FUNC_TCLK2_A                    IPSR(16, 20, 0xA)
#define FUNC_SSI_SDATA8                 IPSR(16, 24, 0)
#define FUNC_HRTS2_N_B                  IPSR(16, 24, 1)
#define FUNC_MSIOF1_TXD_C               IPSR(16, 24, 2)
#define FUNC_TS_SPSYNC1_A               IPSR(16, 24, 5)
#define FUNC_STP_ISSYNC_1_A             IPSR(16, 24, 6)
#define FUNC_RIF1_D1_A                  IPSR(16, 24, 7)
#define FUNC_RIF3_D1_A                  IPSR(16, 24, 8)
#define FUNC_SSI_SDATA9_A               IPSR(16, 28, 0)
#define FUNC_HSCK2_B                    IPSR(16, 28, 1)
#define FUNC_MSIOF1_SS1_C               IPSR(16, 28, 2)
#define FUNC_HSCK1_A                    IPSR(16, 28, 3)
#define FUNC_SSI_WS1_B                  IPSR(16, 28, 4)
#define FUNC_SCK1                       IPSR(16, 28, 5)
#define FUNC_STP_IVCXO27_1_A            IPSR(16, 28, 6)
#define FUNC_SCK5_A                     IPSR(16, 28, 7)
#define FUNC_AUDIO_CLKA_A               IPSR(17, 0, 0)
#define FUNC_AUDIO_CLKB_B               IPSR(17, 4, 0)
#define FUNC_SCIF_CLK_A                 IPSR(17, 4, 1)
#define FUNC_STP_IVCXO27_1_D            IPSR(17, 4, 6)
#define FUNC_REMOCON_A                  IPSR(17, 4, 7)
#define FUNC_TCLK1_A                    IPSR(17, 4, 0xA)
#define FUNC_USB0_PWEN                  IPSR(17, 8, 0)
#define FUNC_SIM0_RST_C                 IPSR(17, 8, 3)
#define FUNC_TS_SCK1_D                  IPSR(17, 8, 5)
#define FUNC_STP_ISCLK_1_D              IPSR(17, 8, 6)
#define FUNC_BPFCLK_B                   IPSR(17, 8, 7)
#define FUNC_RIF3_CLK_B                 IPSR(17, 8, 8)
#define FUNC_HSCK2_C                    IPSR(17, 8, 0xD)
#define FUNC_USB0_OVC                   IPSR(17, 12, 0)
#define FUNC_SIM0_D_C                   IPSR(17, 12, 3)
#define FUNC_TS_SDAT1_D                 IPSR(17, 12, 5)
#define FUNC_STP_ISD_1_D                IPSR(17, 12, 6)
#define FUNC_RIF3_SYNC_B                IPSR(17, 12, 8)
#define FUNC_HRX2_C                     IPSR(17, 12, 0xD)
#define FUNC_USB1_PWEN                  IPSR(17, 16, 0)
#define FUNC_SIM0_CLK_C                 IPSR(17, 16, 3)
#define FUNC_SSI_SCK1_A                 IPSR(17, 16, 4)
#define FUNC_TS_SCK0_E                  IPSR(17, 16, 5)
#define FUNC_STP_ISCLK_0_E              IPSR(17, 16, 6)
#define FUNC_FMCLK_B                    IPSR(17, 16, 7)
#define FUNC_RIF2_CLK_B                 IPSR(17, 16, 8)
#define FUNC_SPEEDIN_A                  IPSR(17, 16, 9)
#define FUNC_HTX2_C                     IPSR(17, 16, 0xD)
#define FUNC_USB1_OVC                   IPSR(17, 20, 0)
#define FUNC_MSIOF1_SS2_C               IPSR(17, 20, 2)
#define FUNC_SSI_WS1_A                  IPSR(17, 20, 4)
#define FUNC_TS_SDAT0_E                 IPSR(17, 20, 5)
#define FUNC_STP_ISD_0_E                IPSR(17, 20, 6)
#define FUNC_FMIN_B                     IPSR(17, 20, 7)
#define FUNC_RIF2_SYNC_B                IPSR(17, 20, 8)
#define FUNC_REMOCON_B                  IPSR(17, 20, 0xA)
#define FUNC_HCTS2_N_C                  IPSR(17, 20, 0xD)
#define FUNC_USB30_PWEN                 IPSR(17, 24, 0)
#define FUNC_AUDIO_CLKOUT_B             IPSR(17, 24, 3)
#define FUNC_SSI_SCK2_B                 IPSR(17, 24, 4)
#define FUNC_TS_SDEN1_D                 IPSR(17, 24, 5)
#define FUNC_STP_ISEN_1_D               IPSR(17, 24, 6)
#define FUNC_STP_OPWM_0_E               IPSR(17, 24, 7)
#define FUNC_RIF3_D0_B                  IPSR(17, 24, 8)
#define FUNC_TCLK2_B                    IPSR(17, 24, 0xA)
#define FUNC_TPU0TO0                    IPSR(17, 24, 0xB)
#define FUNC_BPFCLK_C                   IPSR(17, 24, 0xC)
#define FUNC_HRTS2_N_C                  IPSR(17, 24, 0xD)
#define FUNC_USB30_OVC                  IPSR(17, 28, 0)
#define FUNC_AUDIO_CLKOUT1_B            IPSR(17, 28, 3)
#define FUNC_SSI_WS2_B                  IPSR(17, 28, 4)
#define FUNC_TS_SPSYNC1_D               IPSR(17, 28, 5)
#define FUNC_STP_ISSYNC_1_D             IPSR(17, 28, 6)
#define FUNC_STP_IVCXO27_0_E            IPSR(17, 28, 7)
#define FUNC_RIF3_D1_B                  IPSR(17, 28, 8)
#define FUNC_FSO_TOE_N                  IPSR(17, 28, 0xA)
#define FUNC_TPU0TO1                    IPSR(17, 28, 0xB)
#define FUNC_USB2_CH3_PWEN              IPSR(18, 0, 0)
#define FUNC_AUDIO_CLKOUT2_B            IPSR(18, 0, 3)
#define FUNC_SSI_SCK9_B                 IPSR(18, 0, 4)
#define FUNC_TS_SDEN0_E                 IPSR(18, 0, 5)
#define FUNC_STP_ISEN_0_E               IPSR(18, 0, 6)
#define FUNC_RIF2_D0_B                  IPSR(18, 0, 8)
#define FUNC_TPU0TO2                    IPSR(18, 0, 0xB)
#define FUNC_FMCLK_C                    IPSR(18, 0, 0xC)
#define FUNC_FMCLK_D                    IPSR(18, 0, 0xD)
#define FUNC_USB2_CH3_OVC               IPSR(18, 4, 0)
#define FUNC_AUDIO_CLKOUT3_B            IPSR(18, 4, 3)
#define FUNC_SSI_WS9_B                  IPSR(18, 4, 4)
#define FUNC_TS_SPSYNC0_E               IPSR(18, 4, 5)
#define FUNC_STP_ISSYNC_0_E             IPSR(18, 4, 6)
#define FUNC_RIF2_D1_B                  IPSR(18, 4, 8)
#define FUNC_TPU0TO3                    IPSR(18, 4, 0xB)
#define FUNC_FMIN_C                     IPSR(18, 4, 0xC)
#define FUNC_FMIN_D                     IPSR(18, 4, 0xD)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A77951_H_ */
```

## 63.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 IoT.bzh。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 20 行

引脚声明（Pins declaration）。

### 注释 3：原第 222 行

引脚复用功能声明（Pinmux function declarations）。

### 注释 4：原第 954 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A77951_H_`。

## 63.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a77951_8h.html)
- [pinctrl-rcar-common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h.html)

---

[上一章](P062_obex.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P064_pinctrl-r8a77961.h_源码浏览.md)
