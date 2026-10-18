---
id: learning.zephyr-docs.api-source-reference.page-26
title: ambiq-apollo4-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo4-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_ambiq-apollo4-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo4-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo4-pinctrl_8h.html)。

## 26.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00050"></a>
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
<a id="l01164"></a>
<a id="l01166"></a>
<a id="l01167"></a>

```c
/*
 * Copyright (c) 2023 Antmicro <www.antmicro.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO4_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO4_PINCTRL_H_




#define APOLLO4_ALT_FUNC_POS 0
#define APOLLO4_ALT_FUNC_MASK 0xf

#define APOLLO4_PIN_NUM_POS 4
#define APOLLO4_PIN_NUM_MASK 0x7f

#define APOLLO4_PINMUX(pin_num, alt_func) (pin_num << APOLLO4_PIN_NUM_POS | \
                                        alt_func << APOLLO4_ALT_FUNC_POS)

#define SWTRACECLK_P0 APOLLO4_PINMUX(0, 0)
#define SLSCL_P0 APOLLO4_PINMUX(0, 1)
#define SLSCK_P0 APOLLO4_PINMUX(0, 2)
#define GPIO_P0 APOLLO4_PINMUX(0, 3)
#define UART0TX_P0 APOLLO4_PINMUX(0, 4)
#define UART1TX_P0 APOLLO4_PINMUX(0, 5)
#define CT0_P0 APOLLO4_PINMUX(0, 6)
#define NCE0_P0 APOLLO4_PINMUX(0, 7)
#define OBSBUS0_P0 APOLLO4_PINMUX(0, 8)
#define VCMPO_P0 APOLLO4_PINMUX(0, 9)
#define FPIO_P0 APOLLO4_PINMUX(0, 11)
#define SWTRACE0_P1 APOLLO4_PINMUX(1, 0)
#define SLSDAWIR3_P1 APOLLO4_PINMUX(1, 1)
#define SLMOSI_P1 APOLLO4_PINMUX(1, 2)
#define GPIO_P1 APOLLO4_PINMUX(1, 3)
#define UART2TX_P1 APOLLO4_PINMUX(1, 4)
#define UART3TX_P1 APOLLO4_PINMUX(1, 5)
#define CT1_P1 APOLLO4_PINMUX(1, 6)
#define NCE1_P1 APOLLO4_PINMUX(1, 7)
#define OBSBUS1_P1 APOLLO4_PINMUX(1, 8)
#define VCMPO_P1 APOLLO4_PINMUX(1, 9)
#define FPIO_P1 APOLLO4_PINMUX(1, 11)
#define SCANIN4_P1 APOLLO4_PINMUX(1, 15)
#define SWTRACE1_P2 APOLLO4_PINMUX(2, 0)
#define SLMISO_P2 APOLLO4_PINMUX(2, 1)
#define TRIG1_P2 APOLLO4_PINMUX(2, 2)
#define GPIO_P2 APOLLO4_PINMUX(2, 3)
#define UART0RX_P2 APOLLO4_PINMUX(2, 4)
#define UART1RX_P2 APOLLO4_PINMUX(2, 5)
#define CT2_P2 APOLLO4_PINMUX(2, 6)
#define NCE2_P2 APOLLO4_PINMUX(2, 7)
#define OBSBUS2_P2 APOLLO4_PINMUX(2, 8)
#define VCMPO_P2 APOLLO4_PINMUX(2, 9)
#define FPIO_P2 APOLLO4_PINMUX(2, 11)
#define SCANRSTN_P2 APOLLO4_PINMUX(2, 15)
#define SWTRACE2_P3 APOLLO4_PINMUX(3, 0)
#define SLNCE_P3 APOLLO4_PINMUX(3, 1)
#define SWO_P3 APOLLO4_PINMUX(3, 2)
#define GPIO_P3 APOLLO4_PINMUX(3, 3)
#define UART2RX_P3 APOLLO4_PINMUX(3, 4)
#define UART3RX_P3 APOLLO4_PINMUX(3, 5)
#define CT3_P3 APOLLO4_PINMUX(3, 6)
#define NCE3_P3 APOLLO4_PINMUX(3, 7)
#define OBSBUS3_P3 APOLLO4_PINMUX(3, 8)
#define FPIO_P3 APOLLO4_PINMUX(3, 11)
#define SCANIN5_P3 APOLLO4_PINMUX(3, 15)
#define SWTRACE3_P4 APOLLO4_PINMUX(4, 0)
#define SLINT_P4 APOLLO4_PINMUX(4, 1)
#define XT32KHZ_P4 APOLLO4_PINMUX(4, 2)
#define GPIO_P4 APOLLO4_PINMUX(4, 3)
#define UART0RTS_P4 APOLLO4_PINMUX(4, 4)
#define UART1RTS_P4 APOLLO4_PINMUX(4, 5)
#define CT4_P4 APOLLO4_PINMUX(4, 6)
#define NCE4_P4 APOLLO4_PINMUX(4, 7)
#define OBSBUS4_P4 APOLLO4_PINMUX(4, 8)
#define I2S0_SDIN_P4 APOLLO4_PINMUX(4, 9)
#define I2S1_SDIN_P4 APOLLO4_PINMUX(4, 10)
#define FPIO_P4 APOLLO4_PINMUX(4, 11)
#define FLB_TDO_P4 APOLLO4_PINMUX(4, 12)
#define FLLOAD_DIR_P4 APOLLO4_PINMUX(4, 13)
#define MDA_TDO_P4 APOLLO4_PINMUX(4, 14)
#define OPCG_TRIG_P4 APOLLO4_PINMUX(4, 15)
#define M0SCL_P5 APOLLO4_PINMUX(5, 0)
#define M0SCK_P5 APOLLO4_PINMUX(5, 1)
#define I2S0_CLK_P5 APOLLO4_PINMUX(5, 2)
#define GPIO_P5 APOLLO4_PINMUX(5, 3)
#define UART2RTS_P5 APOLLO4_PINMUX(5, 4)
#define UART3RTS_P5 APOLLO4_PINMUX(5, 5)
#define CT5_P5 APOLLO4_PINMUX(5, 6)
#define NCE5_P5 APOLLO4_PINMUX(5, 7)
#define OBSBUS5_P5 APOLLO4_PINMUX(5, 8)
#define I2S1_CLK_P5 APOLLO4_PINMUX(5, 10)
#define FPIO_P5 APOLLO4_PINMUX(5, 11)
#define FLB_TDI_P5 APOLLO4_PINMUX(5, 12)
#define FLLOAD_DATA_P5 APOLLO4_PINMUX(5, 13)
#define MDA_SRST_P5 APOLLO4_PINMUX(5, 14)
#define DFT_ISO_P5 APOLLO4_PINMUX(5, 15)
#define M0SDAWIR3_P6 APOLLO4_PINMUX(6, 0)
#define M0MOSI_P6 APOLLO4_PINMUX(6, 1)
#define I2S0_DATA_P6 APOLLO4_PINMUX(6, 2)
#define GPIO_P6 APOLLO4_PINMUX(6, 3)
#define UART0CTS_P6 APOLLO4_PINMUX(6, 4)
#define UART1CTS_P6 APOLLO4_PINMUX(6, 5)
#define CT6_P6 APOLLO4_PINMUX(6, 6)
#define NCE6_P6 APOLLO4_PINMUX(6, 7)
#define OBSBUS6_P6 APOLLO4_PINMUX(6, 8)
#define I2S0_SDOUT_P6 APOLLO4_PINMUX(6, 9)
#define I2S1_SDOUT_P6 APOLLO4_PINMUX(6, 10)
#define FPIO_P6 APOLLO4_PINMUX(6, 11)
#define SCANIN6_P6 APOLLO4_PINMUX(6, 15)
#define M0MISO_P7 APOLLO4_PINMUX(7, 0)
#define TRIG0_P7 APOLLO4_PINMUX(7, 1)
#define I2S0_WS_P7 APOLLO4_PINMUX(7, 2)
#define GPIO_P7 APOLLO4_PINMUX(7, 3)
#define UART2CTS_P7 APOLLO4_PINMUX(7, 4)
#define UART3CTS_P7 APOLLO4_PINMUX(7, 5)
#define CT7_P7 APOLLO4_PINMUX(7, 6)
#define NCE7_P7 APOLLO4_PINMUX(7, 7)
#define OBSBUS7_P7 APOLLO4_PINMUX(7, 8)
#define I2S1_WS_P7 APOLLO4_PINMUX(7, 10)
#define FPIO_P7 APOLLO4_PINMUX(7, 11)
#define SCANIN7_P7 APOLLO4_PINMUX(7, 15)
#define CMPRF1_P8 APOLLO4_PINMUX(8, 0)
#define TRIG1_P8 APOLLO4_PINMUX(8, 1)
#define GPIO_P8 APOLLO4_PINMUX(8, 3)
#define M1SCL_P8 APOLLO4_PINMUX(8, 4)
#define M1SCK_P8 APOLLO4_PINMUX(8, 5)
#define CT8_P8 APOLLO4_PINMUX(8, 6)
#define NCE8_P8 APOLLO4_PINMUX(8, 7)
#define OBSBUS8_P8 APOLLO4_PINMUX(8, 8)
#define FPIO_P8 APOLLO4_PINMUX(8, 11)
#define SCANOUT4_P8 APOLLO4_PINMUX(8, 15)
#define CMPRF0_P9 APOLLO4_PINMUX(9, 0)
#define TRIG2_P9 APOLLO4_PINMUX(9, 1)
#define GPIO_P9 APOLLO4_PINMUX(9, 3)
#define M1SDAWIR3_P9 APOLLO4_PINMUX(9, 4)
#define M1MOSI_P9 APOLLO4_PINMUX(9, 5)
#define CT9_P9 APOLLO4_PINMUX(9, 6)
#define NCE9_P9 APOLLO4_PINMUX(9, 7)
#define OBSBUS9_P9 APOLLO4_PINMUX(9, 8)
#define FPIO_P9 APOLLO4_PINMUX(9, 11)
#define SCANOUT5_P9 APOLLO4_PINMUX(9, 15)
#define CMPIN0_P10 APOLLO4_PINMUX(10, 0)
#define TRIG3_P10 APOLLO4_PINMUX(10, 1)
#define GPIO_P10 APOLLO4_PINMUX(10, 3)
#define M1MISO_P10 APOLLO4_PINMUX(10, 4)
#define CT10_P10 APOLLO4_PINMUX(10, 6)
#define NCE10_P10 APOLLO4_PINMUX(10, 7)
#define OBSBUS10_P10 APOLLO4_PINMUX(10, 8)
#define DISP_TE_P10 APOLLO4_PINMUX(10, 9)
#define FPIO_P10 APOLLO4_PINMUX(10, 11)
#define OPCG_LOAD_P10 APOLLO4_PINMUX(10, 15)
#define CMPIN1_P11 APOLLO4_PINMUX(11, 0)
#define TRIG0_P11 APOLLO4_PINMUX(11, 1)
#define I2S0_CLK_P11 APOLLO4_PINMUX(11, 2)
#define GPIO_P11 APOLLO4_PINMUX(11, 3)
#define UART2RX_P11 APOLLO4_PINMUX(11, 4)
#define UART3RX_P11 APOLLO4_PINMUX(11, 5)
#define CT11_P11 APOLLO4_PINMUX(11, 6)
#define NCE11_P11 APOLLO4_PINMUX(11, 7)
#define OBSBUS11_P11 APOLLO4_PINMUX(11, 8)
#define FPIO_P11 APOLLO4_PINMUX(11, 11)
#define FLB_TCLK_P11 APOLLO4_PINMUX(11, 12)
#define FLLOAD_ADDR_P11 APOLLO4_PINMUX(11, 13)
#define MDA_TCK_P11 APOLLO4_PINMUX(11, 14)
#define SCANIN0_P11 APOLLO4_PINMUX(11, 15)
#define ADCSE7_P12 APOLLO4_PINMUX(12, 0)
#define TRIG1_P12 APOLLO4_PINMUX(12, 1)
#define I2S0_DATA_P12 APOLLO4_PINMUX(12, 2)
#define GPIO_P12 APOLLO4_PINMUX(12, 3)
#define UART0TX_P12 APOLLO4_PINMUX(12, 4)
#define UART1TX_P12 APOLLO4_PINMUX(12, 5)
#define CT12_P12 APOLLO4_PINMUX(12, 6)
#define NCE12_P12 APOLLO4_PINMUX(12, 7)
#define OBSBUS12_P12 APOLLO4_PINMUX(12, 8)
#define CMPRF2_P12 APOLLO4_PINMUX(12, 9)
#define I2S0_SDOUT_P12 APOLLO4_PINMUX(12, 10)
#define FPIO_P12 APOLLO4_PINMUX(12, 11)
#define SCANOUT3_P12 APOLLO4_PINMUX(12, 15)
#define ADCSE6_P13 APOLLO4_PINMUX(13, 0)
#define TRIG2_P13 APOLLO4_PINMUX(13, 1)
#define I2S0_WS_P13 APOLLO4_PINMUX(13, 2)
#define GPIO_P13 APOLLO4_PINMUX(13, 3)
#define UART2TX_P13 APOLLO4_PINMUX(13, 4)
#define UART3TX_P13 APOLLO4_PINMUX(13, 5)
#define CT13_P13 APOLLO4_PINMUX(13, 6)
#define NCE13_P13 APOLLO4_PINMUX(13, 7)
#define OBSBUS13_P13 APOLLO4_PINMUX(13, 8)
#define FPIO_P13 APOLLO4_PINMUX(13, 11)
#define FLB_FCLK_P13 APOLLO4_PINMUX(13, 12)
#define FLLOAD_DATA_P13 APOLLO4_PINMUX(13, 13)
#define MDA_TDI_P13 APOLLO4_PINMUX(13, 14)
#define SCANOUT0_P13 APOLLO4_PINMUX(13, 15)
#define ADCSE5_P14 APOLLO4_PINMUX(14, 0)
#define TRIG3_P14 APOLLO4_PINMUX(14, 1)
#define GPIO_P14 APOLLO4_PINMUX(14, 3)
#define MILLI_CLK_P14 APOLLO4_PINMUX(14, 4)
#define UART1RX_P14 APOLLO4_PINMUX(14, 5)
#define CT14_P14 APOLLO4_PINMUX(14, 6)
#define NCE14_P14 APOLLO4_PINMUX(14, 7)
#define OBSBUS14_P14 APOLLO4_PINMUX(14, 8)
#define I2S0_SDIN_P14 APOLLO4_PINMUX(14, 10)
#define FPIO_P14 APOLLO4_PINMUX(14, 11)
#define FLLOAD_ADDR_P14 APOLLO4_PINMUX(14, 13)
#define MDA_TRSTN_P14 APOLLO4_PINMUX(14, 14)
#define SCANOUT2_P14 APOLLO4_PINMUX(14, 15)
#define ADCSE4_P15 APOLLO4_PINMUX(15, 0)
#define TRIG0_P15 APOLLO4_PINMUX(15, 1)
#define GPIO_P15 APOLLO4_PINMUX(15, 3)
#define MILLI_REC_DAT_P15 APOLLO4_PINMUX(15, 4)
#define UART3RX_P15 APOLLO4_PINMUX(15, 5)
#define CT15_P15 APOLLO4_PINMUX(15, 6)
#define NCE15_P15 APOLLO4_PINMUX(15, 7)
#define OBSBUS15_P15 APOLLO4_PINMUX(15, 8)
#define REFCLK_EXT_P15 APOLLO4_PINMUX(15, 10)
#define FPIO_P15 APOLLO4_PINMUX(15, 11)
#define FLLOAD_DATA_P15 APOLLO4_PINMUX(15, 13)
#define SCANOUT1_P15 APOLLO4_PINMUX(15, 15)
#define ADCSE3_P16 APOLLO4_PINMUX(16, 0)
#define TRIG1_P16 APOLLO4_PINMUX(16, 1)
#define I2S1_CLK_P16 APOLLO4_PINMUX(16, 2)
#define GPIO_P16 APOLLO4_PINMUX(16, 3)
#define MILLI_PBDATA1_P16 APOLLO4_PINMUX(16, 4)
#define UART1RTS_P16 APOLLO4_PINMUX(16, 5)
#define CT16_P16 APOLLO4_PINMUX(16, 6)
#define NCE16_P16 APOLLO4_PINMUX(16, 7)
#define OBSBUS0_P16 APOLLO4_PINMUX(16, 8)
#define FPIO_P16 APOLLO4_PINMUX(16, 11)
#define DFT_RET_P16 APOLLO4_PINMUX(16, 15)
#define ADCSE2_P17 APOLLO4_PINMUX(17, 0)
#define TRIG2_P17 APOLLO4_PINMUX(17, 1)
#define I2S1_DATA_P17 APOLLO4_PINMUX(17, 2)
#define GPIO_P17 APOLLO4_PINMUX(17, 3)
#define MILLI_PBDATA2_P17 APOLLO4_PINMUX(17, 4)
#define UART3RTS_P17 APOLLO4_PINMUX(17, 5)
#define CT17_P17 APOLLO4_PINMUX(17, 6)
#define NCE17_P17 APOLLO4_PINMUX(17, 7)
#define OBSBUS1_P17 APOLLO4_PINMUX(17, 8)
#define I2S1_SDOUT_P17 APOLLO4_PINMUX(17, 9)
#define FPIO_P17 APOLLO4_PINMUX(17, 11)
#define FLLOAD_STRB_P17 APOLLO4_PINMUX(17, 13)
#define MDA_TMS_P17 APOLLO4_PINMUX(17, 14)
#define OPCG_CLK_P17 APOLLO4_PINMUX(17, 15)
#define ADCSE1_P18 APOLLO4_PINMUX(18, 0)
#define ANATEST2_P18 APOLLO4_PINMUX(18, 1)
#define I2S1_WS_P18 APOLLO4_PINMUX(18, 2)
#define GPIO_P18 APOLLO4_PINMUX(18, 3)
#define UART0CTS_P18 APOLLO4_PINMUX(18, 4)
#define UART1CTS_P18 APOLLO4_PINMUX(18, 5)
#define CT18_P18 APOLLO4_PINMUX(18, 6)
#define NCE18_P18 APOLLO4_PINMUX(18, 7)
#define OBSBUS2_P18 APOLLO4_PINMUX(18, 8)
#define FPIO_P18 APOLLO4_PINMUX(18, 11)
#define FLB_TMS_P18 APOLLO4_PINMUX(18, 12)
#define FLLOAD_DATA_P18 APOLLO4_PINMUX(18, 13)
#define MDA_HFRC_EXT_P18 APOLLO4_PINMUX(18, 14)
#define SCANIN1_P18 APOLLO4_PINMUX(18, 15)
#define ADCSE0_P19 APOLLO4_PINMUX(19, 0)
#define ANATEST1_P19 APOLLO4_PINMUX(19, 1)
#define GPIO_P19 APOLLO4_PINMUX(19, 3)
#define UART2CTS_P19 APOLLO4_PINMUX(19, 4)
#define UART3CTS_P19 APOLLO4_PINMUX(19, 5)
#define CT19_P19 APOLLO4_PINMUX(19, 6)
#define NCE19_P19 APOLLO4_PINMUX(19, 7)
#define OBSBUS3_P19 APOLLO4_PINMUX(19, 8)
#define I2S1_SDIN_P19 APOLLO4_PINMUX(19, 9)
#define FPIO_P19 APOLLO4_PINMUX(19, 11)
#define FLB_TRSTN_P19 APOLLO4_PINMUX(19, 12)
#define FLLOAD_ADDR_P19 APOLLO4_PINMUX(19, 13)
#define SCANIN2_P19 APOLLO4_PINMUX(19, 15)
#define SWDCK_P20 APOLLO4_PINMUX(20, 0)
#define TRIG1_P20 APOLLO4_PINMUX(20, 1)
#define GPIO_P20 APOLLO4_PINMUX(20, 3)
#define UART0TX_P20 APOLLO4_PINMUX(20, 4)
#define UART1TX_P20 APOLLO4_PINMUX(20, 5)
#define CT20_P20 APOLLO4_PINMUX(20, 6)
#define NCE20_P20 APOLLO4_PINMUX(20, 7)
#define OBSBUS4_P20 APOLLO4_PINMUX(20, 8)
#define FPIO_P20 APOLLO4_PINMUX(20, 11)
#define SCANCLK_P20 APOLLO4_PINMUX(20, 15)
#define SWDIO_P21 APOLLO4_PINMUX(21, 0)
#define TRIG2_P21 APOLLO4_PINMUX(21, 1)
#define GPIO_P21 APOLLO4_PINMUX(21, 3)
#define UART2TX_P21 APOLLO4_PINMUX(21, 4)
#define UART3TX_P21 APOLLO4_PINMUX(21, 5)
#define CT21_P21 APOLLO4_PINMUX(21, 6)
#define NCE21_P21 APOLLO4_PINMUX(21, 7)
#define OBSBUS5_P21 APOLLO4_PINMUX(21, 8)
#define FPIO_P21 APOLLO4_PINMUX(21, 11)
#define SCANSHFT_P21 APOLLO4_PINMUX(21, 15)
#define M7SCL_P22 APOLLO4_PINMUX(22, 0)
#define M7SCK_P22 APOLLO4_PINMUX(22, 1)
#define SWO_P22 APOLLO4_PINMUX(22, 2)
#define GPIO_P22 APOLLO4_PINMUX(22, 3)
#define UART0RX_P22 APOLLO4_PINMUX(22, 4)
#define UART1RX_P22 APOLLO4_PINMUX(22, 5)
#define CT22_P22 APOLLO4_PINMUX(22, 6)
#define NCE22_P22 APOLLO4_PINMUX(22, 7)
#define OBSBUS6_P22 APOLLO4_PINMUX(22, 8)
#define VCMPO_P22 APOLLO4_PINMUX(22, 9)
#define I3CM1_SCL_P22 APOLLO4_PINMUX(22, 10)
#define FPIO_P22 APOLLO4_PINMUX(22, 11)
#define SCANIN3_P22 APOLLO4_PINMUX(22, 15)
#define M7SDAWIR3_P23 APOLLO4_PINMUX(23, 0)
#define M7MOSI_P23 APOLLO4_PINMUX(23, 1)
#define SWO_P23 APOLLO4_PINMUX(23, 2)
#define GPIO_P23 APOLLO4_PINMUX(23, 3)
#define UART2RX_P23 APOLLO4_PINMUX(23, 4)
#define UART3RX_P23 APOLLO4_PINMUX(23, 5)
#define CT23_P23 APOLLO4_PINMUX(23, 6)
#define NCE23_P23 APOLLO4_PINMUX(23, 7)
#define OBSBUS7_P23 APOLLO4_PINMUX(23, 8)
#define VCMPO_P23 APOLLO4_PINMUX(23, 9)
#define I3CM1_SDA_P23 APOLLO4_PINMUX(23, 10)
#define FPIO_P23 APOLLO4_PINMUX(23, 11)
#define SCANOUT6_P23 APOLLO4_PINMUX(23, 15)
#define M7MISO_P24 APOLLO4_PINMUX(24, 0)
#define TRIG3_P24 APOLLO4_PINMUX(24, 1)
#define SWO_P24 APOLLO4_PINMUX(24, 2)
#define GPIO_P24 APOLLO4_PINMUX(24, 3)
#define UART0RTS_P24 APOLLO4_PINMUX(24, 4)
#define UART1RTS_P24 APOLLO4_PINMUX(24, 5)
#define CT24_P24 APOLLO4_PINMUX(24, 6)
#define NCE24_P24 APOLLO4_PINMUX(24, 7)
#define OBSBUS8_P24 APOLLO4_PINMUX(24, 8)
#define FPIO_P24 APOLLO4_PINMUX(24, 11)
#define SCANOUT7_P24 APOLLO4_PINMUX(24, 15)
#define M2SCL_P25 APOLLO4_PINMUX(25, 0)
#define M2SCK_P25 APOLLO4_PINMUX(25, 1)
#define GPIO_P25 APOLLO4_PINMUX(25, 3)
#define LFRC_EXT_P25 APOLLO4_PINMUX(25, 4)
#define DSP_TMS_P25 APOLLO4_PINMUX(25, 5)
#define CT25_P25 APOLLO4_PINMUX(25, 6)
#define NCE25_P25 APOLLO4_PINMUX(25, 7)
#define OBSBUS9_P25 APOLLO4_PINMUX(25, 8)
#define FPIO_P25 APOLLO4_PINMUX(25, 11)
#define SCANIN8_P25 APOLLO4_PINMUX(25, 15)
#define M2SDAWIR3_P26 APOLLO4_PINMUX(26, 0)
#define M2MOSI_P26 APOLLO4_PINMUX(26, 1)
#define GPIO_P26 APOLLO4_PINMUX(26, 3)
#define HFRC_EXT_P26 APOLLO4_PINMUX(26, 4)
#define CT26_P26 APOLLO4_PINMUX(26, 6)
#define NCE26_P26 APOLLO4_PINMUX(26, 7)
#define OBSBUS10_P26 APOLLO4_PINMUX(26, 8)
#define VCMPO_P26 APOLLO4_PINMUX(26, 9)
#define FPIO_P26 APOLLO4_PINMUX(26, 11)
#define SCANIN9_P26 APOLLO4_PINMUX(26, 15)
#define M2MISO_P27 APOLLO4_PINMUX(27, 0)
#define TRIG0_P27 APOLLO4_PINMUX(27, 1)
#define GPIO_P27 APOLLO4_PINMUX(27, 3)
#define XT_EXT_P27 APOLLO4_PINMUX(27, 4)
#define DSP_TCK_P27 APOLLO4_PINMUX(27, 5)
#define CT27_P27 APOLLO4_PINMUX(27, 6)
#define NCE27_P27 APOLLO4_PINMUX(27, 7)
#define OBSBUS11_P27 APOLLO4_PINMUX(27, 8)
#define I2S0_SDIN_P27 APOLLO4_PINMUX(27, 9)
#define FPIO_P27 APOLLO4_PINMUX(27, 11)
#define SCANIN10_P27 APOLLO4_PINMUX(27, 15)
#define SWO_P28 APOLLO4_PINMUX(28, 0)
#define VCMPO_P28 APOLLO4_PINMUX(28, 1)
#define I2S0_CLK_P28 APOLLO4_PINMUX(28, 2)
#define GPIO_P28 APOLLO4_PINMUX(28, 3)
#define UART2CTS_P28 APOLLO4_PINMUX(28, 4)
#define DSP_TDO_P28 APOLLO4_PINMUX(28, 5)
#define CT28_P28 APOLLO4_PINMUX(28, 6)
#define NCE28_P28 APOLLO4_PINMUX(28, 7)
#define OBSBUS12_P28 APOLLO4_PINMUX(28, 8)
#define FPIO_P28 APOLLO4_PINMUX(28, 11)
#define CME_P28 APOLLO4_PINMUX(28, 15)
#define TRIG0_P29 APOLLO4_PINMUX(29, 0)
#define VCMPO_P29 APOLLO4_PINMUX(29, 1)
#define I2S0_DATA_P29 APOLLO4_PINMUX(29, 2)
#define GPIO_P29 APOLLO4_PINMUX(29, 3)
#define UART1CTS_P29 APOLLO4_PINMUX(29, 4)
#define DSP_TRSTN_P29 APOLLO4_PINMUX(29, 5)
#define CT29_P29 APOLLO4_PINMUX(29, 6)
#define NCE29_P29 APOLLO4_PINMUX(29, 7)
#define OBSBUS13_P29 APOLLO4_PINMUX(29, 8)
#define I2S0_SDOUT_P29 APOLLO4_PINMUX(29, 9)
#define FPIO_P29 APOLLO4_PINMUX(29, 11)
#define CMLE_P29 APOLLO4_PINMUX(29, 15)
#define TRIG1_P30 APOLLO4_PINMUX(30, 0)
#define VCMPO_P30 APOLLO4_PINMUX(30, 1)
#define I2S0_WS_P30 APOLLO4_PINMUX(30, 2)
#define GPIO_P30 APOLLO4_PINMUX(30, 3)
#define UART0TX_P30 APOLLO4_PINMUX(30, 4)
#define DSP_TDI_P30 APOLLO4_PINMUX(30, 5)
#define CT30_P30 APOLLO4_PINMUX(30, 6)
#define NCE30_P30 APOLLO4_PINMUX(30, 7)
#define OBSBUS14_P30 APOLLO4_PINMUX(30, 8)
#define FPIO_P30 APOLLO4_PINMUX(30, 11)
#define SCANOUT8_P30 APOLLO4_PINMUX(30, 15)
#define M3SCL_P31 APOLLO4_PINMUX(31, 0)
#define M3SCK_P31 APOLLO4_PINMUX(31, 1)
#define GPIO_P31 APOLLO4_PINMUX(31, 3)
#define UART2TX_P31 APOLLO4_PINMUX(31, 4)
#define CT31_P31 APOLLO4_PINMUX(31, 6)
#define NCE31_P31 APOLLO4_PINMUX(31, 7)
#define OBSBUS15_P31 APOLLO4_PINMUX(31, 8)
#define VCMPO_P31 APOLLO4_PINMUX(31, 9)
#define FPIO_P31 APOLLO4_PINMUX(31, 11)
#define SCANOUT9_P31 APOLLO4_PINMUX(31, 15)
#define M3SDAWIR3_P32 APOLLO4_PINMUX(32, 0)
#define M3MOSI_P32 APOLLO4_PINMUX(32, 1)
#define GPIO_P32 APOLLO4_PINMUX(32, 3)
#define UART0RX_P32 APOLLO4_PINMUX(32, 4)
#define CT32_P32 APOLLO4_PINMUX(32, 6)
#define NCE32_P32 APOLLO4_PINMUX(32, 7)
#define OBSBUS0_P32 APOLLO4_PINMUX(32, 8)
#define FPIO_P32 APOLLO4_PINMUX(32, 11)
#define SCANOUT10_P32 APOLLO4_PINMUX(32, 15)
#define M3MISO_P33 APOLLO4_PINMUX(33, 0)
#define CLKOUT_P33 APOLLO4_PINMUX(33, 1)
#define GPIO_P33 APOLLO4_PINMUX(33, 3)
#define UART2RX_P33 APOLLO4_PINMUX(33, 4)
#define CT33_P33 APOLLO4_PINMUX(33, 6)
#define NCE33_P33 APOLLO4_PINMUX(33, 7)
#define OBSBUS1_P33 APOLLO4_PINMUX(33, 8)
#define DISP_TE_P33 APOLLO4_PINMUX(33, 9)
#define FPIO_P33 APOLLO4_PINMUX(33, 11)
#define SCANOUT11_P33 APOLLO4_PINMUX(33, 15)
#define M4SCL_P34 APOLLO4_PINMUX(34, 0)
#define M4SCK_P34 APOLLO4_PINMUX(34, 1)
#define SWO_P34 APOLLO4_PINMUX(34, 2)
#define GPIO_P34 APOLLO4_PINMUX(34, 3)
#define UART0TX_P34 APOLLO4_PINMUX(34, 4)
#define CT34_P34 APOLLO4_PINMUX(34, 6)
#define NCE34_P34 APOLLO4_PINMUX(34, 7)
#define OBSBUS2_P34 APOLLO4_PINMUX(34, 8)
#define VCMPO_P34 APOLLO4_PINMUX(34, 9)
#define FPIO_P34 APOLLO4_PINMUX(34, 11)
#define M4SDAWIR3_P35 APOLLO4_PINMUX(35, 0)
#define M4MOSI_P35 APOLLO4_PINMUX(35, 1)
#define SWO_P35 APOLLO4_PINMUX(35, 2)
#define GPIO_P35 APOLLO4_PINMUX(35, 3)
#define UART2TX_P35 APOLLO4_PINMUX(35, 4)
#define UART3TX_P35 APOLLO4_PINMUX(35, 5)
#define CT35_P35 APOLLO4_PINMUX(35, 6)
#define NCE35_P35 APOLLO4_PINMUX(35, 7)
#define OBSBUS3_P35 APOLLO4_PINMUX(35, 8)
#define VCMPO_P35 APOLLO4_PINMUX(35, 9)
#define FPIO_P35 APOLLO4_PINMUX(35, 11)
#define M4MISO_P36 APOLLO4_PINMUX(36, 0)
#define TRIG0_P36 APOLLO4_PINMUX(36, 1)
#define SWO_P36 APOLLO4_PINMUX(36, 2)
#define GPIO_P36 APOLLO4_PINMUX(36, 3)
#define UART0RX_P36 APOLLO4_PINMUX(36, 4)
#define UART1RX_P36 APOLLO4_PINMUX(36, 5)
#define CT36_P36 APOLLO4_PINMUX(36, 6)
#define NCE36_P36 APOLLO4_PINMUX(36, 7)
#define OBSBUS4_P36 APOLLO4_PINMUX(36, 8)
#define FPIO_P36 APOLLO4_PINMUX(36, 11)
#define MSPI1_0_P37 APOLLO4_PINMUX(37, 0)
#define TRIG1_P37 APOLLO4_PINMUX(37, 1)
#define XT32KHZ_P37 APOLLO4_PINMUX(37, 2)
#define GPIO_P37 APOLLO4_PINMUX(37, 3)
#define UART2RX_P37 APOLLO4_PINMUX(37, 4)
#define DISP_D15_P37 APOLLO4_PINMUX(37, 5)
#define CT37_P37 APOLLO4_PINMUX(37, 6)
#define NCE37_P37 APOLLO4_PINMUX(37, 7)
#define OBSBUS5_P37 APOLLO4_PINMUX(37, 8)
#define FPIO_P37 APOLLO4_PINMUX(37, 11)
#define MSPI1_1_P38 APOLLO4_PINMUX(38, 0)
#define TRIG2_P38 APOLLO4_PINMUX(38, 1)
#define SWTRACECLK_P38 APOLLO4_PINMUX(38, 2)
#define GPIO_P38 APOLLO4_PINMUX(38, 3)
#define UART0RTS_P38 APOLLO4_PINMUX(38, 4)
#define DISP_D16_P38 APOLLO4_PINMUX(38, 5)
#define CT38_P38 APOLLO4_PINMUX(38, 6)
#define NCE38_P38 APOLLO4_PINMUX(38, 7)
#define OBSBUS6_P38 APOLLO4_PINMUX(38, 8)
#define FPIO_P38 APOLLO4_PINMUX(38, 11)
#define MSPI1_2_P39 APOLLO4_PINMUX(39, 0)
#define TRIG3_P39 APOLLO4_PINMUX(39, 1)
#define SWTRACE0_P39 APOLLO4_PINMUX(39, 2)
#define GPIO_P39 APOLLO4_PINMUX(39, 3)
#define UART2RTS_P39 APOLLO4_PINMUX(39, 4)
#define DISP_D17_P39 APOLLO4_PINMUX(39, 5)
#define CT39_P39 APOLLO4_PINMUX(39, 6)
#define NCE39_P39 APOLLO4_PINMUX(39, 7)
#define OBSBUS7_P39 APOLLO4_PINMUX(39, 8)
#define FPIO_P39 APOLLO4_PINMUX(39, 11)
#define MSPI1_3_P40 APOLLO4_PINMUX(40, 0)
#define TRIG1_P40 APOLLO4_PINMUX(40, 1)
#define SWTRACE1_P40 APOLLO4_PINMUX(40, 2)
#define GPIO_P40 APOLLO4_PINMUX(40, 3)
#define UART0CTS_P40 APOLLO4_PINMUX(40, 4)
#define DISP_D18_P40 APOLLO4_PINMUX(40, 5)
#define CT40_P40 APOLLO4_PINMUX(40, 6)
#define NCE40_P40 APOLLO4_PINMUX(40, 7)
#define OBSBUS8_P40 APOLLO4_PINMUX(40, 8)
#define FPIO_P40 APOLLO4_PINMUX(40, 11)
#define MSPI1_4_P41 APOLLO4_PINMUX(41, 0)
#define TRIG0_P41 APOLLO4_PINMUX(41, 1)
#define SWTRACE2_P41 APOLLO4_PINMUX(41, 2)
#define GPIO_P41 APOLLO4_PINMUX(41, 3)
#define UART0TX_P41 APOLLO4_PINMUX(41, 4)
#define DISP_D19_P41 APOLLO4_PINMUX(41, 5)
#define CT41_P41 APOLLO4_PINMUX(41, 6)
#define NCE41_P41 APOLLO4_PINMUX(41, 7)
#define OBSBUS9_P41 APOLLO4_PINMUX(41, 8)
#define SWO_P41 APOLLO4_PINMUX(41, 9)
#define FPIO_P41 APOLLO4_PINMUX(41, 11)
#define MSPI1_5_P42 APOLLO4_PINMUX(42, 0)
#define TRIG2_P42 APOLLO4_PINMUX(42, 1)
#define SWTRACE3_P42 APOLLO4_PINMUX(42, 2)
#define GPIO_P42 APOLLO4_PINMUX(42, 3)
#define UART2TX_P42 APOLLO4_PINMUX(42, 4)
#define DISP_D20_P42 APOLLO4_PINMUX(42, 5)
#define CT42_P42 APOLLO4_PINMUX(42, 6)
#define NCE42_P42 APOLLO4_PINMUX(42, 7)
#define OBSBUS10_P42 APOLLO4_PINMUX(42, 8)
#define FPIO_P42 APOLLO4_PINMUX(42, 11)
#define MSPI1_6_P43 APOLLO4_PINMUX(43, 0)
#define TRIG3_P43 APOLLO4_PINMUX(43, 1)
#define SWTRACECTL_P43 APOLLO4_PINMUX(43, 2)
#define GPIO_P43 APOLLO4_PINMUX(43, 3)
#define UART0RX_P43 APOLLO4_PINMUX(43, 4)
#define DISP_D21_P43 APOLLO4_PINMUX(43, 5)
#define CT43_P43 APOLLO4_PINMUX(43, 6)
#define NCE43_P43 APOLLO4_PINMUX(43, 7)
#define OBSBUS11_P43 APOLLO4_PINMUX(43, 8)
#define FPIO_P43 APOLLO4_PINMUX(43, 11)
#define MSPI1_7_P44 APOLLO4_PINMUX(44, 0)
#define TRIG1_P44 APOLLO4_PINMUX(44, 1)
#define SWO_P44 APOLLO4_PINMUX(44, 2)
#define GPIO_P44 APOLLO4_PINMUX(44, 3)
#define UART2RX_P44 APOLLO4_PINMUX(44, 4)
#define DISP_D22_P44 APOLLO4_PINMUX(44, 5)
#define CT44_P44 APOLLO4_PINMUX(44, 6)
#define NCE44_P44 APOLLO4_PINMUX(44, 7)
#define OBSBUS12_P44 APOLLO4_PINMUX(44, 8)
#define VCMPO_P44 APOLLO4_PINMUX(44, 9)
#define FPIO_P44 APOLLO4_PINMUX(44, 11)
#define MSPI1_8_P45 APOLLO4_PINMUX(45, 0)
#define TRIG2_P45 APOLLO4_PINMUX(45, 1)
#define XT32KHZ_P45 APOLLO4_PINMUX(45, 2)
#define GPIO_P45 APOLLO4_PINMUX(45, 3)
#define UART0TX_P45 APOLLO4_PINMUX(45, 4)
#define DISP_D23_P45 APOLLO4_PINMUX(45, 5)
#define CT45_P45 APOLLO4_PINMUX(45, 6)
#define NCE45_P45 APOLLO4_PINMUX(45, 7)
#define OBSBUS13_P45 APOLLO4_PINMUX(45, 8)
#define FPIO_P45 APOLLO4_PINMUX(45, 11)
#define MSPI1_9_P46 APOLLO4_PINMUX(46, 0)
#define TRIG3_P46 APOLLO4_PINMUX(46, 1)
#define CLKOUT_32M_P46 APOLLO4_PINMUX(46, 2)
#define GPIO_P46 APOLLO4_PINMUX(46, 3)
#define UART2TX_P46 APOLLO4_PINMUX(46, 4)
#define UART3TX_P46 APOLLO4_PINMUX(46, 5)
#define CT46_P46 APOLLO4_PINMUX(46, 6)
#define NCE46_P46 APOLLO4_PINMUX(46, 7)
#define OBSBUS14_P46 APOLLO4_PINMUX(46, 8)
#define I2S1_SDIN_P46 APOLLO4_PINMUX(46, 9)
#define I2S0_SDIN_P46 APOLLO4_PINMUX(46, 10)
#define FPIO_P46 APOLLO4_PINMUX(46, 11)
#define M5SCL_P47 APOLLO4_PINMUX(47, 0)
#define M5SCK_P47 APOLLO4_PINMUX(47, 1)
#define I2S1_CLK_P47 APOLLO4_PINMUX(47, 2)
#define GPIO_P47 APOLLO4_PINMUX(47, 3)
#define UART0RX_P47 APOLLO4_PINMUX(47, 4)
#define UART1RX_P47 APOLLO4_PINMUX(47, 5)
#define CT47_P47 APOLLO4_PINMUX(47, 6)
#define NCE47_P47 APOLLO4_PINMUX(47, 7)
#define OBSBUS15_P47 APOLLO4_PINMUX(47, 8)
#define I2S0_CLK_P47 APOLLO4_PINMUX(47, 10)
#define FPIO_P47 APOLLO4_PINMUX(47, 11)
#define M5SDAWIR3_P48 APOLLO4_PINMUX(48, 0)
#define M5MOSI_P48 APOLLO4_PINMUX(48, 1)
#define I2S1_DATA_P48 APOLLO4_PINMUX(48, 2)
#define GPIO_P48 APOLLO4_PINMUX(48, 3)
#define UART2RX_P48 APOLLO4_PINMUX(48, 4)
#define UART3RX_P48 APOLLO4_PINMUX(48, 5)
#define CT48_P48 APOLLO4_PINMUX(48, 6)
#define NCE48_P48 APOLLO4_PINMUX(48, 7)
#define OBSBUS0_P48 APOLLO4_PINMUX(48, 8)
#define I2S1_SDOUT_P48 APOLLO4_PINMUX(48, 9)
#define I2S0_SDOUT_P48 APOLLO4_PINMUX(48, 10)
#define FPIO_P48 APOLLO4_PINMUX(48, 11)
#define M5MISO_P49 APOLLO4_PINMUX(49, 0)
#define TRIG0_P49 APOLLO4_PINMUX(49, 1)
#define I2S1_WS_P49 APOLLO4_PINMUX(49, 2)
#define GPIO_P49 APOLLO4_PINMUX(49, 3)
#define UART0RTS_P49 APOLLO4_PINMUX(49, 4)
#define UART1RTS_P49 APOLLO4_PINMUX(49, 5)
#define CT49_P49 APOLLO4_PINMUX(49, 6)
#define NCE49_P49 APOLLO4_PINMUX(49, 7)
#define OBSBUS1_P49 APOLLO4_PINMUX(49, 8)
#define I2S0_WS_P49 APOLLO4_PINMUX(49, 10)
#define FPIO_P49 APOLLO4_PINMUX(49, 11)
#define PDM0_CLK_P50 APOLLO4_PINMUX(50, 0)
#define TRIG0_P50 APOLLO4_PINMUX(50, 1)
#define SWTRACECLK_P50 APOLLO4_PINMUX(50, 2)
#define GPIO_P50 APOLLO4_PINMUX(50, 3)
#define UART2RTS_P50 APOLLO4_PINMUX(50, 4)
#define UART3RTS_P50 APOLLO4_PINMUX(50, 5)
#define CT50_P50 APOLLO4_PINMUX(50, 6)
#define NCE50_P50 APOLLO4_PINMUX(50, 7)
#define OBSBUS2_P50 APOLLO4_PINMUX(50, 8)
#define DISP_TE_P50 APOLLO4_PINMUX(50, 9)
#define FPIO_P50 APOLLO4_PINMUX(50, 11)
#define PDM0_DATA_P51 APOLLO4_PINMUX(51, 0)
#define TRIG1_P51 APOLLO4_PINMUX(51, 1)
#define SWTRACE0_P51 APOLLO4_PINMUX(51, 2)
#define GPIO_P51 APOLLO4_PINMUX(51, 3)
#define UART0CTS_P51 APOLLO4_PINMUX(51, 4)
#define UART1CTS_P51 APOLLO4_PINMUX(51, 5)
#define CT51_P51 APOLLO4_PINMUX(51, 6)
#define NCE51_P51 APOLLO4_PINMUX(51, 7)
#define OBSBUS3_P51 APOLLO4_PINMUX(51, 8)
#define FPIO_P51 APOLLO4_PINMUX(51, 11)
#define PDM1_CLK_P52 APOLLO4_PINMUX(52, 0)
#define TRIG2_P52 APOLLO4_PINMUX(52, 1)
#define SWTRACE1_P52 APOLLO4_PINMUX(52, 2)
#define GPIO_P52 APOLLO4_PINMUX(52, 3)
#define UART2CTS_P52 APOLLO4_PINMUX(52, 4)
#define UART3CTS_P52 APOLLO4_PINMUX(52, 5)
#define CT52_P52 APOLLO4_PINMUX(52, 6)
#define NCE52_P52 APOLLO4_PINMUX(52, 7)
#define OBSBUS4_P52 APOLLO4_PINMUX(52, 8)
#define VCMPO_P52 APOLLO4_PINMUX(52, 9)
#define FPIO_P52 APOLLO4_PINMUX(52, 11)
#define PDM1_DATA_P53 APOLLO4_PINMUX(53, 0)
#define TRIG3_P53 APOLLO4_PINMUX(53, 1)
#define SWTRACE2_P53 APOLLO4_PINMUX(53, 2)
#define GPIO_P53 APOLLO4_PINMUX(53, 3)
#define UART0TX_P53 APOLLO4_PINMUX(53, 4)
#define UART1TX_P53 APOLLO4_PINMUX(53, 5)
#define CT53_P53 APOLLO4_PINMUX(53, 6)
#define NCE53_P53 APOLLO4_PINMUX(53, 7)
#define OBSBUS5_P53 APOLLO4_PINMUX(53, 8)
#define FPIO_P53 APOLLO4_PINMUX(53, 11)
#define PDM2_CLK_P54 APOLLO4_PINMUX(54, 0)
#define TRIG0_P54 APOLLO4_PINMUX(54, 1)
#define SWTRACE3_P54 APOLLO4_PINMUX(54, 2)
#define GPIO_P54 APOLLO4_PINMUX(54, 3)
#define UART2TX_P54 APOLLO4_PINMUX(54, 4)
#define UART3TX_P54 APOLLO4_PINMUX(54, 5)
#define CT54_P54 APOLLO4_PINMUX(54, 6)
#define NCE54_P54 APOLLO4_PINMUX(54, 7)
#define OBSBUS6_P54 APOLLO4_PINMUX(54, 8)
#define FPIO_P54 APOLLO4_PINMUX(54, 11)
#define PDM2_DATA_P55 APOLLO4_PINMUX(55, 0)
#define TRIG1_P55 APOLLO4_PINMUX(55, 1)
#define SWTRACECTL_P55 APOLLO4_PINMUX(55, 2)
#define GPIO_P55 APOLLO4_PINMUX(55, 3)
#define UART0RX_P55 APOLLO4_PINMUX(55, 4)
#define UART1RX_P55 APOLLO4_PINMUX(55, 5)
#define CT55_P55 APOLLO4_PINMUX(55, 6)
#define NCE55_P55 APOLLO4_PINMUX(55, 7)
#define OBSBUS7_P55 APOLLO4_PINMUX(55, 8)
#define FPIO_P55 APOLLO4_PINMUX(55, 11)
#define PDM3_CLK_P56 APOLLO4_PINMUX(56, 0)
#define TRIG2_P56 APOLLO4_PINMUX(56, 1)
#define SWO_P56 APOLLO4_PINMUX(56, 2)
#define GPIO_P56 APOLLO4_PINMUX(56, 3)
#define UART2RX_P56 APOLLO4_PINMUX(56, 4)
#define UART3RX_P56 APOLLO4_PINMUX(56, 5)
#define CT56_P56 APOLLO4_PINMUX(56, 6)
#define NCE56_P56 APOLLO4_PINMUX(56, 7)
#define OBSBUS8_P56 APOLLO4_PINMUX(56, 8)
#define FPIO_P56 APOLLO4_PINMUX(56, 11)
#define PDM3_DATA_P57 APOLLO4_PINMUX(57, 0)
#define TRIG3_P57 APOLLO4_PINMUX(57, 1)
#define SWO_P57 APOLLO4_PINMUX(57, 2)
#define GPIO_P57 APOLLO4_PINMUX(57, 3)
#define UART0RTS_P57 APOLLO4_PINMUX(57, 4)
#define UART1RTS_P57 APOLLO4_PINMUX(57, 5)
#define CT57_P57 APOLLO4_PINMUX(57, 6)
#define NCE57_P57 APOLLO4_PINMUX(57, 7)
#define OBSBUS9_P57 APOLLO4_PINMUX(57, 8)
#define VCMPO_P57 APOLLO4_PINMUX(57, 9)
#define FPIO_P57 APOLLO4_PINMUX(57, 11)
#define GPIO_P58 APOLLO4_PINMUX(58, 3)
#define UART0RTS_P58 APOLLO4_PINMUX(58, 4)
#define UART3RTS_P58 APOLLO4_PINMUX(58, 5)
#define CT58_P58 APOLLO4_PINMUX(58, 6)
#define NCE58_P58 APOLLO4_PINMUX(58, 7)
#define OBSBUS10_P58 APOLLO4_PINMUX(58, 8)
#define FPIO_P58 APOLLO4_PINMUX(58, 11)
#define TRIG0_P59 APOLLO4_PINMUX(59, 1)
#define GPIO_P59 APOLLO4_PINMUX(59, 3)
#define UART0CTS_P59 APOLLO4_PINMUX(59, 4)
#define UART1CTS_P59 APOLLO4_PINMUX(59, 5)
#define CT59_P59 APOLLO4_PINMUX(59, 6)
#define NCE59_P59 APOLLO4_PINMUX(59, 7)
#define OBSBUS11_P59 APOLLO4_PINMUX(59, 8)
#define FPIO_P59 APOLLO4_PINMUX(59, 11)
#define TRIG1_P60 APOLLO4_PINMUX(60, 1)
#define GPIO_P60 APOLLO4_PINMUX(60, 3)
#define UART0TX_P60 APOLLO4_PINMUX(60, 4)
#define UART3CTS_P60 APOLLO4_PINMUX(60, 5)
#define CT60_P60 APOLLO4_PINMUX(60, 6)
#define NCE60_P60 APOLLO4_PINMUX(60, 7)
#define OBSBUS12_P60 APOLLO4_PINMUX(60, 8)
#define FPIO_P60 APOLLO4_PINMUX(60, 11)
#define M6SCL_P61 APOLLO4_PINMUX(61, 0)
#define M6SCK_P61 APOLLO4_PINMUX(61, 1)
#define I2S1_CLK_P61 APOLLO4_PINMUX(61, 2)
#define GPIO_P61 APOLLO4_PINMUX(61, 3)
#define UART2TX_P61 APOLLO4_PINMUX(61, 4)
#define UART3TX_P61 APOLLO4_PINMUX(61, 5)
#define CT61_P61 APOLLO4_PINMUX(61, 6)
#define NCE61_P61 APOLLO4_PINMUX(61, 7)
#define OBSBUS13_P61 APOLLO4_PINMUX(61, 8)
#define I3CM0_SCL_P61 APOLLO4_PINMUX(61, 10)
#define FPIO_P61 APOLLO4_PINMUX(61, 11)
#define M6SDAWIR3_P62 APOLLO4_PINMUX(62, 0)
#define M6MOSI_P62 APOLLO4_PINMUX(62, 1)
#define I2S1_DATA_P62 APOLLO4_PINMUX(62, 2)
#define GPIO_P62 APOLLO4_PINMUX(62, 3)
#define UART0RX_P62 APOLLO4_PINMUX(62, 4)
#define UART1RX_P62 APOLLO4_PINMUX(62, 5)
#define CT62_P62 APOLLO4_PINMUX(62, 6)
#define NCE62_P62 APOLLO4_PINMUX(62, 7)
#define OBSBUS14_P62 APOLLO4_PINMUX(62, 8)
#define I2S1_SDOUT_P62 APOLLO4_PINMUX(62, 9)
#define I3CM0_SDA_P62 APOLLO4_PINMUX(62, 10)
#define FPIO_P62 APOLLO4_PINMUX(62, 11)
#define M6MISO_P63 APOLLO4_PINMUX(63, 0)
#define CLKOUT_P63 APOLLO4_PINMUX(63, 1)
#define I2S1_WS_P63 APOLLO4_PINMUX(63, 2)
#define GPIO_P63 APOLLO4_PINMUX(63, 3)
#define UART2RX_P63 APOLLO4_PINMUX(63, 4)
#define UART3RX_P63 APOLLO4_PINMUX(63, 5)
#define CT63_P63 APOLLO4_PINMUX(63, 6)
#define NCE63_P63 APOLLO4_PINMUX(63, 7)
#define OBSBUS15_P63 APOLLO4_PINMUX(63, 8)
#define DISP_TE_P63 APOLLO4_PINMUX(63, 9)
#define FPIO_P63 APOLLO4_PINMUX(63, 11)
#define MSPI0_0_P64 APOLLO4_PINMUX(64, 0)
#define XT32KHZ_P64 APOLLO4_PINMUX(64, 1)
#define SWO_P64 APOLLO4_PINMUX(64, 2)
#define GPIO_P64 APOLLO4_PINMUX(64, 3)
#define UART0RTS_P64 APOLLO4_PINMUX(64, 4)
#define DISP_D0_P64 APOLLO4_PINMUX(64, 5)
#define CT64_P64 APOLLO4_PINMUX(64, 6)
#define NCE64_P64 APOLLO4_PINMUX(64, 7)
#define OBSBUS0_P64 APOLLO4_PINMUX(64, 8)
#define I2S1_SDIN_P64 APOLLO4_PINMUX(64, 9)
#define FPIO_P64 APOLLO4_PINMUX(64, 11)
#define MSPI0_1_P65 APOLLO4_PINMUX(65, 0)
#define XT32KHZ_P65 APOLLO4_PINMUX(65, 1)
#define SWO_P65 APOLLO4_PINMUX(65, 2)
#define GPIO_P65 APOLLO4_PINMUX(65, 3)
#define UART0CTS_P65 APOLLO4_PINMUX(65, 4)
#define DISP_D1_P65 APOLLO4_PINMUX(65, 5)
#define CT65_P65 APOLLO4_PINMUX(65, 6)
#define NCE65_P65 APOLLO4_PINMUX(65, 7)
#define OBSBUS1_P65 APOLLO4_PINMUX(65, 8)
#define FPIO_P65 APOLLO4_PINMUX(65, 11)
#define MSPI0_2_P66 APOLLO4_PINMUX(66, 0)
#define CLKOUT_P66 APOLLO4_PINMUX(66, 1)
#define SWO_P66 APOLLO4_PINMUX(66, 2)
#define GPIO_P66 APOLLO4_PINMUX(66, 3)
#define UART0TX_P66 APOLLO4_PINMUX(66, 4)
#define DISP_D2_P66 APOLLO4_PINMUX(66, 5)
#define CT66_P66 APOLLO4_PINMUX(66, 6)
#define NCE66_P66 APOLLO4_PINMUX(66, 7)
#define OBSBUS2_P66 APOLLO4_PINMUX(66, 8)
#define FPIO_P66 APOLLO4_PINMUX(66, 11)
#define MSPI0_3_P67 APOLLO4_PINMUX(67, 0)
#define CLKOUT_P67 APOLLO4_PINMUX(67, 1)
#define SWO_P67 APOLLO4_PINMUX(67, 2)
#define GPIO_P67 APOLLO4_PINMUX(67, 3)
#define UART2TX_P67 APOLLO4_PINMUX(67, 4)
#define DISP_D3_P67 APOLLO4_PINMUX(67, 5)
#define CT67_P67 APOLLO4_PINMUX(67, 6)
#define NCE67_P67 APOLLO4_PINMUX(67, 7)
#define OBSBUS3_P67 APOLLO4_PINMUX(67, 8)
#define FPIO_P67 APOLLO4_PINMUX(67, 11)
#define MSPI0_4_P68 APOLLO4_PINMUX(68, 0)
#define SWO_P68 APOLLO4_PINMUX(68, 1)
#define GPIO_P68 APOLLO4_PINMUX(68, 3)
#define UART0RX_P68 APOLLO4_PINMUX(68, 4)
#define DISP_D4_P68 APOLLO4_PINMUX(68, 5)
#define CT68_P68 APOLLO4_PINMUX(68, 6)
#define NCE68_P68 APOLLO4_PINMUX(68, 7)
#define OBSBUS4_P68 APOLLO4_PINMUX(68, 8)
#define FPIO_P68 APOLLO4_PINMUX(68, 11)
#define MSPI0_5_P69 APOLLO4_PINMUX(69, 0)
#define XT32KHZ_P69 APOLLO4_PINMUX(69, 1)
#define SWO_P69 APOLLO4_PINMUX(69, 2)
#define GPIO_P69 APOLLO4_PINMUX(69, 3)
#define UART2RX_P69 APOLLO4_PINMUX(69, 4)
#define DISP_D5_P69 APOLLO4_PINMUX(69, 5)
#define CT69_P69 APOLLO4_PINMUX(69, 6)
#define NCE69_P69 APOLLO4_PINMUX(69, 7)
#define OBSBUS5_P69 APOLLO4_PINMUX(69, 8)
#define FPIO_P69 APOLLO4_PINMUX(69, 11)
#define MSPI0_6_P70 APOLLO4_PINMUX(70, 0)
#define XT32KHZ_P70 APOLLO4_PINMUX(70, 1)
#define SWTRACE0_P70 APOLLO4_PINMUX(70, 2)
#define GPIO_P70 APOLLO4_PINMUX(70, 3)
#define UART0RTS_P70 APOLLO4_PINMUX(70, 4)
#define DISP_D6_P70 APOLLO4_PINMUX(70, 5)
#define CT70_P70 APOLLO4_PINMUX(70, 6)
#define NCE70_P70 APOLLO4_PINMUX(70, 7)
#define OBSBUS6_P70 APOLLO4_PINMUX(70, 8)
#define FPIO_P70 APOLLO4_PINMUX(70, 11)
#define MSPI0_7_P71 APOLLO4_PINMUX(71, 0)
#define CLKOUT_P71 APOLLO4_PINMUX(71, 1)
#define SWTRACE1_P71 APOLLO4_PINMUX(71, 2)
#define GPIO_P71 APOLLO4_PINMUX(71, 3)
#define UART0CTS_P71 APOLLO4_PINMUX(71, 4)
#define DISP_D7_P71 APOLLO4_PINMUX(71, 5)
#define CT71_P71 APOLLO4_PINMUX(71, 6)
#define NCE71_P71 APOLLO4_PINMUX(71, 7)
#define OBSBUS7_P71 APOLLO4_PINMUX(71, 8)
#define FPIO_P71 APOLLO4_PINMUX(71, 11)
#define MSPI0_8_P72 APOLLO4_PINMUX(72, 0)
#define CLKOUT_P72 APOLLO4_PINMUX(72, 1)
#define SWTRACE2_P72 APOLLO4_PINMUX(72, 2)
#define GPIO_P72 APOLLO4_PINMUX(72, 3)
#define UART0TX_P72 APOLLO4_PINMUX(72, 4)
#define DISP_D8_P72 APOLLO4_PINMUX(72, 5)
#define CT72_P72 APOLLO4_PINMUX(72, 6)
#define NCE72_P72 APOLLO4_PINMUX(72, 7)
#define OBSBUS8_P72 APOLLO4_PINMUX(72, 8)
#define VCMPO_P72 APOLLO4_PINMUX(72, 9)
#define FPIO_P72 APOLLO4_PINMUX(72, 11)
#define MSPI0_9_P73 APOLLO4_PINMUX(73, 0)
#define SWTRACE3_P73 APOLLO4_PINMUX(73, 2)
#define GPIO_P73 APOLLO4_PINMUX(73, 3)
#define UART2TX_P73 APOLLO4_PINMUX(73, 4)
#define DISP_D9_P73 APOLLO4_PINMUX(73, 5)
#define CT73_P73 APOLLO4_PINMUX(73, 6)
#define NCE73_P73 APOLLO4_PINMUX(73, 7)
#define OBSBUS9_P73 APOLLO4_PINMUX(73, 8)
#define FPIO_P73 APOLLO4_PINMUX(73, 11)
#define MSPI2_0_P74 APOLLO4_PINMUX(74, 0)
#define DISP_QSPI_D0_OUT_P74 APOLLO4_PINMUX(74, 1)
#define DISP_QSPI_D0_P74 APOLLO4_PINMUX(74, 2)
#define GPIO_P74 APOLLO4_PINMUX(74, 3)
#define UART0RX_P74 APOLLO4_PINMUX(74, 4)
#define DISP_D10_P74 APOLLO4_PINMUX(74, 5)
#define CT74_P74 APOLLO4_PINMUX(74, 6)
#define NCE74_P74 APOLLO4_PINMUX(74, 7)
#define OBSBUS10_P74 APOLLO4_PINMUX(74, 8)
#define DISP_SPI_SD_P74 APOLLO4_PINMUX(74, 9)
#define DISP_SPI_SDO_P74 APOLLO4_PINMUX(74, 10)
#define FPIO_P74 APOLLO4_PINMUX(74, 11)
#define MSPI2_1_P75 APOLLO4_PINMUX(75, 0)
#define XT32KHZ_P75 APOLLO4_PINMUX(75, 1)
#define DISP_QSPI_D1_P75 APOLLO4_PINMUX(75, 2)
#define GPIO_P75 APOLLO4_PINMUX(75, 3)
#define UART2RX_P75 APOLLO4_PINMUX(75, 4)
#define DISP_D11_P75 APOLLO4_PINMUX(75, 5)
#define CT75_P75 APOLLO4_PINMUX(75, 6)
#define NCE75_P75 APOLLO4_PINMUX(75, 7)
#define OBSBUS11_P75 APOLLO4_PINMUX(75, 8)
#define DISP_SPI_DCX_P75 APOLLO4_PINMUX(75, 9)
#define FPIO_P75 APOLLO4_PINMUX(75, 11)
#define MSPI2_2_P76 APOLLO4_PINMUX(76, 0)
#define XT32KHZ_P76 APOLLO4_PINMUX(76, 1)
#define DISP_QSPI_D2_P76 APOLLO4_PINMUX(76, 2)
#define GPIO_P76 APOLLO4_PINMUX(76, 3)
#define UART0RTS_P76 APOLLO4_PINMUX(76, 4)
#define DISP_D12_P76 APOLLO4_PINMUX(76, 5)
#define CT76_P76 APOLLO4_PINMUX(76, 6)
#define NCE76_P76 APOLLO4_PINMUX(76, 7)
#define OBSBUS12_P76 APOLLO4_PINMUX(76, 8)
#define FPIO_P76 APOLLO4_PINMUX(76, 11)
#define MSPI2_3_P77 APOLLO4_PINMUX(77, 0)
#define DISP_QSPI_D3_P77 APOLLO4_PINMUX(77, 2)
#define GPIO_P77 APOLLO4_PINMUX(77, 3)
#define UART0CTS_P77 APOLLO4_PINMUX(77, 4)
#define DISP_D13_P77 APOLLO4_PINMUX(77, 5)
#define CT77_P77 APOLLO4_PINMUX(77, 6)
#define NCE77_P77 APOLLO4_PINMUX(77, 7)
#define OBSBUS13_P77 APOLLO4_PINMUX(77, 8)
#define FPIO_P77 APOLLO4_PINMUX(77, 11)
#define MSPI2_4_P78 APOLLO4_PINMUX(78, 0)
#define DISP_QSPI_SCK_P78 APOLLO4_PINMUX(78, 2)
#define GPIO_P78 APOLLO4_PINMUX(78, 3)
#define UART0TX_P78 APOLLO4_PINMUX(78, 4)
#define DISP_D14_P78 APOLLO4_PINMUX(78, 5)
#define CT78_P78 APOLLO4_PINMUX(78, 6)
#define NCE78_P78 APOLLO4_PINMUX(78, 7)
#define OBSBUS14_P78 APOLLO4_PINMUX(78, 8)
#define DISP_SPI_SCK_P78 APOLLO4_PINMUX(78, 9)
#define FPIO_P78 APOLLO4_PINMUX(78, 11)
#define MSPI2_5_P79 APOLLO4_PINMUX(79, 0)
#define SDIF_DAT4_P79 APOLLO4_PINMUX(79, 2)
#define GPIO_P79 APOLLO4_PINMUX(79, 3)
#define SWO_P79 APOLLO4_PINMUX(79, 4)
#define DISP_VS_P79 APOLLO4_PINMUX(79, 5)
#define CT79_P79 APOLLO4_PINMUX(79, 6)
#define NCE79_P79 APOLLO4_PINMUX(79, 7)
#define OBSBUS15_P79 APOLLO4_PINMUX(79, 8)
#define DISP_SPI_SDI_P79 APOLLO4_PINMUX(79, 9)
#define FPIO_P79 APOLLO4_PINMUX(79, 11)
#define MSPI2_6_P80 APOLLO4_PINMUX(80, 0)
#define CLKOUT_P80 APOLLO4_PINMUX(80, 1)
#define SDIF_DAT5_P80 APOLLO4_PINMUX(80, 2)
#define GPIO_P80 APOLLO4_PINMUX(80, 3)
#define SWTRACE0_P80 APOLLO4_PINMUX(80, 4)
#define DISP_HS_P80 APOLLO4_PINMUX(80, 5)
#define CT80_P80 APOLLO4_PINMUX(80, 6)
#define NCE80_P80 APOLLO4_PINMUX(80, 7)
#define OBSBUS0_P80 APOLLO4_PINMUX(80, 8)
#define FPIO_P80 APOLLO4_PINMUX(80, 11)
#define MSPI2_7_P81 APOLLO4_PINMUX(81, 0)
#define CLKOUT_P81 APOLLO4_PINMUX(81, 1)
#define SDIF_DAT6_P81 APOLLO4_PINMUX(81, 2)
#define GPIO_P81 APOLLO4_PINMUX(81, 3)
#define SWTRACE1_P81 APOLLO4_PINMUX(81, 4)
#define DISP_DE_P81 APOLLO4_PINMUX(81, 5)
#define CT81_P81 APOLLO4_PINMUX(81, 6)
#define NCE81_P81 APOLLO4_PINMUX(81, 7)
#define OBSBUS1_P81 APOLLO4_PINMUX(81, 8)
#define FPIO_P81 APOLLO4_PINMUX(81, 11)
#define MSPI2_8_P82 APOLLO4_PINMUX(82, 0)
#define XT32KHZ_P82 APOLLO4_PINMUX(82, 1)
#define SDIF_DAT7_P82 APOLLO4_PINMUX(82, 2)
#define GPIO_P82 APOLLO4_PINMUX(82, 3)
#define SWTRACE2_P82 APOLLO4_PINMUX(82, 4)
#define DISP_PCLK_P82 APOLLO4_PINMUX(82, 5)
#define CT82_P82 APOLLO4_PINMUX(82, 6)
#define NCE82_P82 APOLLO4_PINMUX(82, 7)
#define OBSBUS2_P82 APOLLO4_PINMUX(82, 8)
#define FPIO_P82 APOLLO4_PINMUX(82, 11)
#define MSPI2_9_P83 APOLLO4_PINMUX(83, 0)
#define XT32KHZ_P83 APOLLO4_PINMUX(83, 1)
#define SDIF_CMD_P83 APOLLO4_PINMUX(83, 2)
#define GPIO_P83 APOLLO4_PINMUX(83, 3)
#define SWTRACE3_P83 APOLLO4_PINMUX(83, 4)
#define DISP_SD_P83 APOLLO4_PINMUX(83, 5)
#define CT83_P83 APOLLO4_PINMUX(83, 6)
#define NCE83_P83 APOLLO4_PINMUX(83, 7)
#define OBSBUS3_P83 APOLLO4_PINMUX(83, 8)
#define FPIO_P83 APOLLO4_PINMUX(83, 11)
#define SDIF_DAT0_P84 APOLLO4_PINMUX(84, 2)
#define GPIO_P84 APOLLO4_PINMUX(84, 3)
#define CT84_P84 APOLLO4_PINMUX(84, 6)
#define NCE84_P84 APOLLO4_PINMUX(84, 7)
#define OBSBUS4_P84 APOLLO4_PINMUX(84, 8)
#define FPIO_P84 APOLLO4_PINMUX(84, 11)
#define SDIF_DAT1_P85 APOLLO4_PINMUX(85, 2)
#define GPIO_P85 APOLLO4_PINMUX(85, 3)
#define CT85_P85 APOLLO4_PINMUX(85, 6)
#define NCE85_P85 APOLLO4_PINMUX(85, 7)
#define OBSBUS5_P85 APOLLO4_PINMUX(85, 8)
#define FPIO_P85 APOLLO4_PINMUX(85, 11)
#define SDIF_DAT2_P86 APOLLO4_PINMUX(86, 2)
#define GPIO_P86 APOLLO4_PINMUX(86, 3)
#define CT86_P86 APOLLO4_PINMUX(86, 6)
#define NCE86_P86 APOLLO4_PINMUX(86, 7)
#define OBSBUS6_P86 APOLLO4_PINMUX(86, 8)
#define FPIO_P86 APOLLO4_PINMUX(86, 11)
#define SDIF_DAT3_P87 APOLLO4_PINMUX(87, 2)
#define GPIO_P87 APOLLO4_PINMUX(87, 3)
#define CT87_P87 APOLLO4_PINMUX(87, 6)
#define NCE87_P87 APOLLO4_PINMUX(87, 7)
#define OBSBUS7_P87 APOLLO4_PINMUX(87, 8)
#define DISP_TE_P87 APOLLO4_PINMUX(87, 9)
#define FPIO_P87 APOLLO4_PINMUX(87, 11)
#define SDIF_CLKOUT_P88 APOLLO4_PINMUX(88, 2)
#define GPIO_P88 APOLLO4_PINMUX(88, 3)
#define CT88_P88 APOLLO4_PINMUX(88, 6)
#define NCE88_P88 APOLLO4_PINMUX(88, 7)
#define OBSBUS8_P88 APOLLO4_PINMUX(88, 8)
#define FPIO_P88 APOLLO4_PINMUX(88, 11)
#define GPIO_P89 APOLLO4_PINMUX(89, 3)
#define DISP_CM_P89 APOLLO4_PINMUX(89, 5)
#define CT89_P89 APOLLO4_PINMUX(89, 6)
#define NCE89_P89 APOLLO4_PINMUX(89, 7)
#define OBSBUS9_P89 APOLLO4_PINMUX(89, 8)
#define FPIO_P89 APOLLO4_PINMUX(89, 11)
#define GPIO_P90 APOLLO4_PINMUX(90, 3)
#define CT90_P90 APOLLO4_PINMUX(90, 6)
#define NCE90_P90 APOLLO4_PINMUX(90, 7)
#define OBSBUS10_P90 APOLLO4_PINMUX(90, 8)
#define VCMPO_P90 APOLLO4_PINMUX(90, 9)
#define FPIO_P90 APOLLO4_PINMUX(90, 11)
#define GPIO_P91 APOLLO4_PINMUX(91, 3)
#define CT91_P91 APOLLO4_PINMUX(91, 6)
#define NCE91_P91 APOLLO4_PINMUX(91, 7)
#define OBSBUS11_P91 APOLLO4_PINMUX(91, 8)
#define VCMPO_P91 APOLLO4_PINMUX(91, 9)
#define FPIO_P91 APOLLO4_PINMUX(91, 11)
#define GPIO_P92 APOLLO4_PINMUX(92, 3)
#define CT92_P92 APOLLO4_PINMUX(92, 6)
#define NCE92_P92 APOLLO4_PINMUX(92, 7)
#define OBSBUS12_P92 APOLLO4_PINMUX(92, 8)
#define VCMPO_P92 APOLLO4_PINMUX(92, 9)
#define FPIO_P92 APOLLO4_PINMUX(92, 11)
#define MSPI2_9_P93 APOLLO4_PINMUX(93, 0)
#define GPIO_P93 APOLLO4_PINMUX(93, 3)
#define CT93_P93 APOLLO4_PINMUX(93, 6)
#define NCE93_P93 APOLLO4_PINMUX(93, 7)
#define OBSBUS13_P93 APOLLO4_PINMUX(93, 8)
#define VCMPO_P93 APOLLO4_PINMUX(93, 9)
#define FPIO_P93 APOLLO4_PINMUX(93, 11)
#define GPIO_P94 APOLLO4_PINMUX(94, 3)
#define CT94_P94 APOLLO4_PINMUX(94, 6)
#define NCE94_P94 APOLLO4_PINMUX(94, 7)
#define OBSBUS14_P94 APOLLO4_PINMUX(94, 8)
#define VCMPO_P94 APOLLO4_PINMUX(94, 9)
#define FPIO_P94 APOLLO4_PINMUX(94, 11)
#define GPIO_P95 APOLLO4_PINMUX(95, 3)
#define CT95_P95 APOLLO4_PINMUX(95, 6)
#define NCE95_P95 APOLLO4_PINMUX(95, 7)
#define OBSBUS15_P95 APOLLO4_PINMUX(95, 8)
#define FPIO_P95 APOLLO4_PINMUX(95, 11)
#define GPIO_P96 APOLLO4_PINMUX(96, 3)
#define CT96_P96 APOLLO4_PINMUX(96, 6)
#define NCE96_P96 APOLLO4_PINMUX(96, 7)
#define OBSBUS0_P96 APOLLO4_PINMUX(96, 8)
#define FPIO_P96 APOLLO4_PINMUX(96, 11)
#define GPIO_P97 APOLLO4_PINMUX(97, 3)
#define CT97_P97 APOLLO4_PINMUX(97, 6)
#define NCE97_P97 APOLLO4_PINMUX(97, 7)
#define OBSBUS1_P97 APOLLO4_PINMUX(97, 8)
#define FPIO_P97 APOLLO4_PINMUX(97, 11)
#define GPIO_P98 APOLLO4_PINMUX(98, 3)
#define CT98_P98 APOLLO4_PINMUX(98, 6)
#define NCE98_P98 APOLLO4_PINMUX(98, 7)
#define OBSBUS2_P98 APOLLO4_PINMUX(98, 8)
#define FPIO_P98 APOLLO4_PINMUX(98, 11)
#define GPIO_P99 APOLLO4_PINMUX(99, 3)
#define CT99_P99 APOLLO4_PINMUX(99, 6)
#define NCE99_P99 APOLLO4_PINMUX(99, 7)
#define OBSBUS3_P99 APOLLO4_PINMUX(99, 8)
#define FPIO_P99 APOLLO4_PINMUX(99, 11)
#define GPIO_P100 APOLLO4_PINMUX(100, 3)
#define CT100_P100 APOLLO4_PINMUX(100, 6)
#define NCE100_P100 APOLLO4_PINMUX(100, 7)
#define OBSBUS4_P100 APOLLO4_PINMUX(100, 8)
#define FPIO_P100 APOLLO4_PINMUX(100, 11)
#define GPIO_P101 APOLLO4_PINMUX(101, 3)
#define CT101_P101 APOLLO4_PINMUX(101, 6)
#define NCE101_P101 APOLLO4_PINMUX(101, 7)
#define OBSBUS5_P101 APOLLO4_PINMUX(101, 8)
#define FPIO_P101 APOLLO4_PINMUX(101, 11)
#define GPIO_P102 APOLLO4_PINMUX(102, 3)
#define CT102_P102 APOLLO4_PINMUX(102, 6)
#define NCE102_P102 APOLLO4_PINMUX(102, 7)
#define OBSBUS6_P102 APOLLO4_PINMUX(102, 8)
#define FPIO_P102 APOLLO4_PINMUX(102, 11)
#define GPIO_P103 APOLLO4_PINMUX(103, 3)
#define CT103_P103 APOLLO4_PINMUX(103, 6)
#define NCE103_P103 APOLLO4_PINMUX(103, 7)
#define OBSBUS7_P103 APOLLO4_PINMUX(103, 8)
#define FPIO_P103 APOLLO4_PINMUX(103, 11)
#define MSPI1_9_P104 APOLLO4_PINMUX(104, 0)
#define GPIO_P104 APOLLO4_PINMUX(104, 3)
#define CT104_P104 APOLLO4_PINMUX(104, 6)
#define NCE104_P104 APOLLO4_PINMUX(104, 7)
#define OBSBUS8_P104 APOLLO4_PINMUX(104, 8)
#define FPIO_P104 APOLLO4_PINMUX(104, 11)
#define GPIO_P105 APOLLO4_PINMUX(105, 3)
#define CT105_P105 APOLLO4_PINMUX(105, 6)
#define OBSBUS9_P105 APOLLO4_PINMUX(105, 8)
#define GPIO_P106 APOLLO4_PINMUX(106, 3)
#define CT106_P106 APOLLO4_PINMUX(106, 6)
#define OBSBUS10_P106 APOLLO4_PINMUX(106, 8)
#define GPIO_P107 APOLLO4_PINMUX(107, 3)
#define CT107_P107 APOLLO4_PINMUX(107, 6)
#define OBSBUS11_P107 APOLLO4_PINMUX(107, 8)
#define GPIO_P108 APOLLO4_PINMUX(108, 3)
#define CT108_P108 APOLLO4_PINMUX(108, 6)
#define OBSBUS12_P108 APOLLO4_PINMUX(108, 8)
#define GPIO_P109 APOLLO4_PINMUX(109, 3)
#define CT109_P109 APOLLO4_PINMUX(109, 6)
#define OBSBUS13_P109 APOLLO4_PINMUX(109, 8)
#define GPIO_P110 APOLLO4_PINMUX(110, 3)
#define CT110_P110 APOLLO4_PINMUX(110, 6)
#define OBSBUS14_P110 APOLLO4_PINMUX(110, 8)
#define GPIO_P111 APOLLO4_PINMUX(111, 3)
#define CT111_P111 APOLLO4_PINMUX(111, 6)
#define OBSBUS15_P111 APOLLO4_PINMUX(111, 8)
#define GPIO_P112 APOLLO4_PINMUX(112, 3)
#define CT112_P112 APOLLO4_PINMUX(112, 6)
#define OBSBUS0_P112 APOLLO4_PINMUX(112, 8)
#define GPIO_P113 APOLLO4_PINMUX(113, 3)
#define CT113_P113 APOLLO4_PINMUX(113, 6)
#define OBSBUS1_P113 APOLLO4_PINMUX(113, 8)
#define GPIO_P114 APOLLO4_PINMUX(114, 3)
#define CT114_P114 APOLLO4_PINMUX(114, 6)
#define OBSBUS2_P114 APOLLO4_PINMUX(114, 8)
#define GPIO_P115 APOLLO4_PINMUX(115, 3)
#define CT115_P115 APOLLO4_PINMUX(115, 6)
#define OBSBUS3_P115 APOLLO4_PINMUX(115, 8)
#define GPIO_P116 APOLLO4_PINMUX(116, 3)
#define CT116_P116 APOLLO4_PINMUX(116, 6)
#define OBSBUS4_P116 APOLLO4_PINMUX(116, 8)
#define GPIO_P117 APOLLO4_PINMUX(117, 3)
#define CT117_P117 APOLLO4_PINMUX(117, 6)
#define OBSBUS5_P117 APOLLO4_PINMUX(117, 8)
#define GPIO_P118 APOLLO4_PINMUX(118, 3)
#define CT118_P118 APOLLO4_PINMUX(118, 6)
#define OBSBUS6_P118 APOLLO4_PINMUX(118, 8)
#define GPIO_P119 APOLLO4_PINMUX(119, 3)
#define CT119_P119 APOLLO4_PINMUX(119, 6)
#define OBSBUS7_P119 APOLLO4_PINMUX(119, 8)
#define GPIO_P120 APOLLO4_PINMUX(120, 3)
#define CT120_P120 APOLLO4_PINMUX(120, 6)
#define OBSBUS8_P120 APOLLO4_PINMUX(120, 8)
#define GPIO_P121 APOLLO4_PINMUX(121, 3)
#define CT121_P121 APOLLO4_PINMUX(121, 6)
#define OBSBUS9_P121 APOLLO4_PINMUX(121, 8)
#define GPIO_P122 APOLLO4_PINMUX(122, 3)
#define CT122_P122 APOLLO4_PINMUX(122, 6)
#define OBSBUS10_P122 APOLLO4_PINMUX(122, 8)
#define GPIO_P123 APOLLO4_PINMUX(123, 3)
#define CT123_P123 APOLLO4_PINMUX(123, 6)
#define OBSBUS11_P123 APOLLO4_PINMUX(123, 8)
#define GPIO_P124 APOLLO4_PINMUX(124, 3)
#define CT124_P124 APOLLO4_PINMUX(124, 6)
#define OBSBUS12_P124 APOLLO4_PINMUX(124, 8)
#define GPIO_P125 APOLLO4_PINMUX(125, 3)
#define CT125_P125 APOLLO4_PINMUX(125, 6)
#define OBSBUS13_P125 APOLLO4_PINMUX(125, 8)
#define GPIO_P126 APOLLO4_PINMUX(126, 3)
#define CT126_P126 APOLLO4_PINMUX(126, 6)
#define OBSBUS14_P126 APOLLO4_PINMUX(126, 8)
#define GPIO_P127 APOLLO4_PINMUX(127, 3)
#define CT127_P127 APOLLO4_PINMUX(127, 6)
#define OBSBUS15_P127 APOLLO4_PINMUX(127, 8)



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO4_PINCTRL_H_ */
```

## 26.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Antmicro <www.antmicro.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 1167 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMBIQ_APOLLO4_PINCTRL_H_`。

## 26.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ambiq-apollo4-pinctrl_8h.html)

---

[上一章](P025_ambiq-apollo3-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P027_ambiq-apollo5-pinctrl.h_源码浏览.md)
