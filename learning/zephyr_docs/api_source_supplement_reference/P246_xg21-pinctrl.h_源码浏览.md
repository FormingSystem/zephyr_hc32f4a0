---
id: learning.zephyr-docs.api-source-supplement-reference.page-246
title: xg21-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xg21-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第246章\_xg21-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/xg21-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/xg21-pinctrl_8h.html)。

## 246.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00026"></a>
<a id="l00080"></a>
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
<a id="l01301"></a>
<a id="l01303"></a>
<a id="l01304"></a>
<a id="asilabs-pinctrl-dbus_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Silicon Laboratories Inc.
 * SPDX-License-Identifier: Apache-2.0
 *
 * Pin Control for Silicon Labs xG21 devices
 *
 * This file was generated by the script gen_pinctrl.py in the hal_silabs module.
 * Do not manually edit.
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_XG21_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_XG21_PINCTRL_H_

#include <zephyr/dt-bindings/pinctrl/silabs-pinctrl-dbus.h>




#define SILABS_DBUS_ACMP0_ACMPOUT(port, pin) SILABS_DBUS(port, pin, 4, 1, 0, 1)

#define SILABS_DBUS_ACMP1_ACMPOUT(port, pin) SILABS_DBUS(port, pin, 7, 1, 0, 1)

#define SILABS_DBUS_CMU_CLKOUT0(port, pin) SILABS_DBUS(port, pin, 10, 1, 0, 2)
#define SILABS_DBUS_CMU_CLKOUT1(port, pin) SILABS_DBUS(port, pin, 10, 1, 1, 3)
#define SILABS_DBUS_CMU_CLKOUT2(port, pin) SILABS_DBUS(port, pin, 10, 1, 2, 4)
#define SILABS_DBUS_CMU_CLKIN0(port, pin)  SILABS_DBUS(port, pin, 10, 0, 0, 1)

#define SILABS_DBUS_PTI_DCLK(port, pin)   SILABS_DBUS(port, pin, 17, 1, 0, 1)
#define SILABS_DBUS_PTI_DFRAME(port, pin) SILABS_DBUS(port, pin, 17, 1, 1, 2)
#define SILABS_DBUS_PTI_DOUT(port, pin)   SILABS_DBUS(port, pin, 17, 1, 2, 3)

#define SILABS_DBUS_I2C0_SCL(port, pin) SILABS_DBUS(port, pin, 22, 1, 0, 1)
#define SILABS_DBUS_I2C0_SDA(port, pin) SILABS_DBUS(port, pin, 22, 1, 1, 2)

#define SILABS_DBUS_I2C1_SCL(port, pin) SILABS_DBUS(port, pin, 26, 1, 0, 1)
#define SILABS_DBUS_I2C1_SDA(port, pin) SILABS_DBUS(port, pin, 26, 1, 1, 2)

#define SILABS_DBUS_LETIMER0_OUT0(port, pin) SILABS_DBUS(port, pin, 30, 1, 0, 1)
#define SILABS_DBUS_LETIMER0_OUT1(port, pin) SILABS_DBUS(port, pin, 30, 1, 1, 2)

#define SILABS_DBUS_MODEM_ANT0(port, pin) SILABS_DBUS(port, pin, 34, 1, 0, 1)
#define SILABS_DBUS_MODEM_ANT1(port, pin) SILABS_DBUS(port, pin, 34, 1, 1, 2)
#define SILABS_DBUS_MODEM_DCLK(port, pin) SILABS_DBUS(port, pin, 34, 1, 2, 3)
#define SILABS_DBUS_MODEM_DOUT(port, pin) SILABS_DBUS(port, pin, 34, 1, 3, 5)
#define SILABS_DBUS_MODEM_DIN(port, pin)  SILABS_DBUS(port, pin, 34, 0, 0, 4)

#define SILABS_DBUS_PRS0_ASYNCH0(port, pin)  SILABS_DBUS(port, pin, 41, 1, 0, 1)
#define SILABS_DBUS_PRS0_ASYNCH1(port, pin)  SILABS_DBUS(port, pin, 41, 1, 1, 2)
#define SILABS_DBUS_PRS0_ASYNCH2(port, pin)  SILABS_DBUS(port, pin, 41, 1, 2, 3)
#define SILABS_DBUS_PRS0_ASYNCH3(port, pin)  SILABS_DBUS(port, pin, 41, 1, 3, 4)
#define SILABS_DBUS_PRS0_ASYNCH4(port, pin)  SILABS_DBUS(port, pin, 41, 1, 4, 5)
#define SILABS_DBUS_PRS0_ASYNCH5(port, pin)  SILABS_DBUS(port, pin, 41, 1, 5, 6)
#define SILABS_DBUS_PRS0_ASYNCH6(port, pin)  SILABS_DBUS(port, pin, 41, 1, 6, 7)
#define SILABS_DBUS_PRS0_ASYNCH7(port, pin)  SILABS_DBUS(port, pin, 41, 1, 7, 8)
#define SILABS_DBUS_PRS0_ASYNCH8(port, pin)  SILABS_DBUS(port, pin, 41, 1, 8, 9)
#define SILABS_DBUS_PRS0_ASYNCH9(port, pin)  SILABS_DBUS(port, pin, 41, 1, 9, 10)
#define SILABS_DBUS_PRS0_ASYNCH10(port, pin) SILABS_DBUS(port, pin, 41, 1, 10, 11)
#define SILABS_DBUS_PRS0_ASYNCH11(port, pin) SILABS_DBUS(port, pin, 41, 1, 11, 12)
#define SILABS_DBUS_PRS0_SYNCH0(port, pin)   SILABS_DBUS(port, pin, 41, 1, 12, 13)
#define SILABS_DBUS_PRS0_SYNCH1(port, pin)   SILABS_DBUS(port, pin, 41, 1, 13, 14)
#define SILABS_DBUS_PRS0_SYNCH2(port, pin)   SILABS_DBUS(port, pin, 41, 1, 14, 15)
#define SILABS_DBUS_PRS0_SYNCH3(port, pin)   SILABS_DBUS(port, pin, 41, 1, 15, 16)

#define SILABS_DBUS_TIMER0_CC0(port, pin)   SILABS_DBUS(port, pin, 59, 1, 0, 1)
#define SILABS_DBUS_TIMER0_CC1(port, pin)   SILABS_DBUS(port, pin, 59, 1, 1, 2)
#define SILABS_DBUS_TIMER0_CC2(port, pin)   SILABS_DBUS(port, pin, 59, 1, 2, 3)
#define SILABS_DBUS_TIMER0_CDTI0(port, pin) SILABS_DBUS(port, pin, 59, 1, 3, 4)
#define SILABS_DBUS_TIMER0_CDTI1(port, pin) SILABS_DBUS(port, pin, 59, 1, 4, 5)
#define SILABS_DBUS_TIMER0_CDTI2(port, pin) SILABS_DBUS(port, pin, 59, 1, 5, 6)

#define SILABS_DBUS_TIMER1_CC0(port, pin)   SILABS_DBUS(port, pin, 67, 1, 0, 1)
#define SILABS_DBUS_TIMER1_CC1(port, pin)   SILABS_DBUS(port, pin, 67, 1, 1, 2)
#define SILABS_DBUS_TIMER1_CC2(port, pin)   SILABS_DBUS(port, pin, 67, 1, 2, 3)
#define SILABS_DBUS_TIMER1_CDTI0(port, pin) SILABS_DBUS(port, pin, 67, 1, 3, 4)
#define SILABS_DBUS_TIMER1_CDTI1(port, pin) SILABS_DBUS(port, pin, 67, 1, 4, 5)
#define SILABS_DBUS_TIMER1_CDTI2(port, pin) SILABS_DBUS(port, pin, 67, 1, 5, 6)

#define SILABS_DBUS_TIMER2_CC0(port, pin)   SILABS_DBUS(port, pin, 75, 1, 0, 1)
#define SILABS_DBUS_TIMER2_CC1(port, pin)   SILABS_DBUS(port, pin, 75, 1, 1, 2)
#define SILABS_DBUS_TIMER2_CC2(port, pin)   SILABS_DBUS(port, pin, 75, 1, 2, 3)
#define SILABS_DBUS_TIMER2_CDTI0(port, pin) SILABS_DBUS(port, pin, 75, 1, 3, 4)
#define SILABS_DBUS_TIMER2_CDTI1(port, pin) SILABS_DBUS(port, pin, 75, 1, 4, 5)
#define SILABS_DBUS_TIMER2_CDTI2(port, pin) SILABS_DBUS(port, pin, 75, 1, 5, 6)

#define SILABS_DBUS_TIMER3_CC0(port, pin)   SILABS_DBUS(port, pin, 83, 1, 0, 1)
#define SILABS_DBUS_TIMER3_CC1(port, pin)   SILABS_DBUS(port, pin, 83, 1, 1, 2)
#define SILABS_DBUS_TIMER3_CC2(port, pin)   SILABS_DBUS(port, pin, 83, 1, 2, 3)
#define SILABS_DBUS_TIMER3_CDTI0(port, pin) SILABS_DBUS(port, pin, 83, 1, 3, 4)
#define SILABS_DBUS_TIMER3_CDTI1(port, pin) SILABS_DBUS(port, pin, 83, 1, 4, 5)
#define SILABS_DBUS_TIMER3_CDTI2(port, pin) SILABS_DBUS(port, pin, 83, 1, 5, 6)

#define SILABS_DBUS_USART0_CS(port, pin)  SILABS_DBUS(port, pin, 91, 1, 0, 1)
#define SILABS_DBUS_USART0_RTS(port, pin) SILABS_DBUS(port, pin, 91, 1, 1, 3)
#define SILABS_DBUS_USART0_RX(port, pin)  SILABS_DBUS(port, pin, 91, 1, 2, 4)
#define SILABS_DBUS_USART0_CLK(port, pin) SILABS_DBUS(port, pin, 91, 1, 3, 5)
#define SILABS_DBUS_USART0_TX(port, pin)  SILABS_DBUS(port, pin, 91, 1, 4, 6)
#define SILABS_DBUS_USART0_CTS(port, pin) SILABS_DBUS(port, pin, 91, 0, 0, 2)

#define SILABS_DBUS_USART1_CS(port, pin)  SILABS_DBUS(port, pin, 99, 1, 0, 1)
#define SILABS_DBUS_USART1_RTS(port, pin) SILABS_DBUS(port, pin, 99, 1, 1, 3)
#define SILABS_DBUS_USART1_RX(port, pin)  SILABS_DBUS(port, pin, 99, 1, 2, 4)
#define SILABS_DBUS_USART1_CLK(port, pin) SILABS_DBUS(port, pin, 99, 1, 3, 5)
#define SILABS_DBUS_USART1_TX(port, pin)  SILABS_DBUS(port, pin, 99, 1, 4, 6)
#define SILABS_DBUS_USART1_CTS(port, pin) SILABS_DBUS(port, pin, 99, 0, 0, 2)

#define SILABS_DBUS_USART2_CS(port, pin)  SILABS_DBUS(port, pin, 107, 1, 0, 1)
#define SILABS_DBUS_USART2_RTS(port, pin) SILABS_DBUS(port, pin, 107, 1, 1, 3)
#define SILABS_DBUS_USART2_RX(port, pin)  SILABS_DBUS(port, pin, 107, 1, 2, 4)
#define SILABS_DBUS_USART2_CLK(port, pin) SILABS_DBUS(port, pin, 107, 1, 3, 5)
#define SILABS_DBUS_USART2_TX(port, pin)  SILABS_DBUS(port, pin, 107, 1, 4, 6)
#define SILABS_DBUS_USART2_CTS(port, pin) SILABS_DBUS(port, pin, 107, 0, 0, 2)

#define GPIO_SWCLKTCK_PA1   SILABS_FIXED_ROUTE(0x0, 0x1, 0, 0)
#define GPIO_SWDIOTMS_PA2   SILABS_FIXED_ROUTE(0x0, 0x2, 0, 1)
#define GPIO_TDO_PA3        SILABS_FIXED_ROUTE(0x0, 0x3, 0, 2)
#define GPIO_TDI_PA4        SILABS_FIXED_ROUTE(0x0, 0x4, 0, 3)
#define GPIO_SWV_PA3        SILABS_FIXED_ROUTE(0x0, 0x3, 1, 0)
#define GPIO_TRACECLK_PA4   SILABS_FIXED_ROUTE(0x0, 0x4, 1, 1)
#define GPIO_TRACEDATA0_PA3 SILABS_FIXED_ROUTE(0x0, 0x3, 1, 2)

#define ACMP0_ACMPOUT_PA0 SILABS_DBUS_ACMP0_ACMPOUT(0x0, 0x0)
#define ACMP0_ACMPOUT_PA1 SILABS_DBUS_ACMP0_ACMPOUT(0x0, 0x1)
#define ACMP0_ACMPOUT_PA2 SILABS_DBUS_ACMP0_ACMPOUT(0x0, 0x2)
#define ACMP0_ACMPOUT_PA3 SILABS_DBUS_ACMP0_ACMPOUT(0x0, 0x3)
#define ACMP0_ACMPOUT_PA4 SILABS_DBUS_ACMP0_ACMPOUT(0x0, 0x4)
#define ACMP0_ACMPOUT_PA5 SILABS_DBUS_ACMP0_ACMPOUT(0x0, 0x5)
#define ACMP0_ACMPOUT_PA6 SILABS_DBUS_ACMP0_ACMPOUT(0x0, 0x6)
#define ACMP0_ACMPOUT_PB0 SILABS_DBUS_ACMP0_ACMPOUT(0x1, 0x0)
#define ACMP0_ACMPOUT_PB1 SILABS_DBUS_ACMP0_ACMPOUT(0x1, 0x1)
#define ACMP0_ACMPOUT_PC0 SILABS_DBUS_ACMP0_ACMPOUT(0x2, 0x0)
#define ACMP0_ACMPOUT_PC1 SILABS_DBUS_ACMP0_ACMPOUT(0x2, 0x1)
#define ACMP0_ACMPOUT_PC2 SILABS_DBUS_ACMP0_ACMPOUT(0x2, 0x2)
#define ACMP0_ACMPOUT_PC3 SILABS_DBUS_ACMP0_ACMPOUT(0x2, 0x3)
#define ACMP0_ACMPOUT_PC4 SILABS_DBUS_ACMP0_ACMPOUT(0x2, 0x4)
#define ACMP0_ACMPOUT_PC5 SILABS_DBUS_ACMP0_ACMPOUT(0x2, 0x5)
#define ACMP0_ACMPOUT_PD0 SILABS_DBUS_ACMP0_ACMPOUT(0x3, 0x0)
#define ACMP0_ACMPOUT_PD1 SILABS_DBUS_ACMP0_ACMPOUT(0x3, 0x1)
#define ACMP0_ACMPOUT_PD2 SILABS_DBUS_ACMP0_ACMPOUT(0x3, 0x2)
#define ACMP0_ACMPOUT_PD3 SILABS_DBUS_ACMP0_ACMPOUT(0x3, 0x3)
#define ACMP0_ACMPOUT_PD4 SILABS_DBUS_ACMP0_ACMPOUT(0x3, 0x4)

#define ACMP1_ACMPOUT_PA0 SILABS_DBUS_ACMP1_ACMPOUT(0x0, 0x0)
#define ACMP1_ACMPOUT_PA1 SILABS_DBUS_ACMP1_ACMPOUT(0x0, 0x1)
#define ACMP1_ACMPOUT_PA2 SILABS_DBUS_ACMP1_ACMPOUT(0x0, 0x2)
#define ACMP1_ACMPOUT_PA3 SILABS_DBUS_ACMP1_ACMPOUT(0x0, 0x3)
#define ACMP1_ACMPOUT_PA4 SILABS_DBUS_ACMP1_ACMPOUT(0x0, 0x4)
#define ACMP1_ACMPOUT_PA5 SILABS_DBUS_ACMP1_ACMPOUT(0x0, 0x5)
#define ACMP1_ACMPOUT_PA6 SILABS_DBUS_ACMP1_ACMPOUT(0x0, 0x6)
#define ACMP1_ACMPOUT_PB0 SILABS_DBUS_ACMP1_ACMPOUT(0x1, 0x0)
#define ACMP1_ACMPOUT_PB1 SILABS_DBUS_ACMP1_ACMPOUT(0x1, 0x1)
#define ACMP1_ACMPOUT_PC0 SILABS_DBUS_ACMP1_ACMPOUT(0x2, 0x0)
#define ACMP1_ACMPOUT_PC1 SILABS_DBUS_ACMP1_ACMPOUT(0x2, 0x1)
#define ACMP1_ACMPOUT_PC2 SILABS_DBUS_ACMP1_ACMPOUT(0x2, 0x2)
#define ACMP1_ACMPOUT_PC3 SILABS_DBUS_ACMP1_ACMPOUT(0x2, 0x3)
#define ACMP1_ACMPOUT_PC4 SILABS_DBUS_ACMP1_ACMPOUT(0x2, 0x4)
#define ACMP1_ACMPOUT_PC5 SILABS_DBUS_ACMP1_ACMPOUT(0x2, 0x5)
#define ACMP1_ACMPOUT_PD0 SILABS_DBUS_ACMP1_ACMPOUT(0x3, 0x0)
#define ACMP1_ACMPOUT_PD1 SILABS_DBUS_ACMP1_ACMPOUT(0x3, 0x1)
#define ACMP1_ACMPOUT_PD2 SILABS_DBUS_ACMP1_ACMPOUT(0x3, 0x2)
#define ACMP1_ACMPOUT_PD3 SILABS_DBUS_ACMP1_ACMPOUT(0x3, 0x3)
#define ACMP1_ACMPOUT_PD4 SILABS_DBUS_ACMP1_ACMPOUT(0x3, 0x4)

#define CMU_CLKOUT0_PC0 SILABS_DBUS_CMU_CLKOUT0(0x2, 0x0)
#define CMU_CLKOUT0_PC1 SILABS_DBUS_CMU_CLKOUT0(0x2, 0x1)
#define CMU_CLKOUT0_PC2 SILABS_DBUS_CMU_CLKOUT0(0x2, 0x2)
#define CMU_CLKOUT0_PC3 SILABS_DBUS_CMU_CLKOUT0(0x2, 0x3)
#define CMU_CLKOUT0_PC4 SILABS_DBUS_CMU_CLKOUT0(0x2, 0x4)
#define CMU_CLKOUT0_PC5 SILABS_DBUS_CMU_CLKOUT0(0x2, 0x5)
#define CMU_CLKOUT0_PD0 SILABS_DBUS_CMU_CLKOUT0(0x3, 0x0)
#define CMU_CLKOUT0_PD1 SILABS_DBUS_CMU_CLKOUT0(0x3, 0x1)
#define CMU_CLKOUT0_PD2 SILABS_DBUS_CMU_CLKOUT0(0x3, 0x2)
#define CMU_CLKOUT0_PD3 SILABS_DBUS_CMU_CLKOUT0(0x3, 0x3)
#define CMU_CLKOUT0_PD4 SILABS_DBUS_CMU_CLKOUT0(0x3, 0x4)
#define CMU_CLKOUT1_PC0 SILABS_DBUS_CMU_CLKOUT1(0x2, 0x0)
#define CMU_CLKOUT1_PC1 SILABS_DBUS_CMU_CLKOUT1(0x2, 0x1)
#define CMU_CLKOUT1_PC2 SILABS_DBUS_CMU_CLKOUT1(0x2, 0x2)
#define CMU_CLKOUT1_PC3 SILABS_DBUS_CMU_CLKOUT1(0x2, 0x3)
#define CMU_CLKOUT1_PC4 SILABS_DBUS_CMU_CLKOUT1(0x2, 0x4)
#define CMU_CLKOUT1_PC5 SILABS_DBUS_CMU_CLKOUT1(0x2, 0x5)
#define CMU_CLKOUT1_PD0 SILABS_DBUS_CMU_CLKOUT1(0x3, 0x0)
#define CMU_CLKOUT1_PD1 SILABS_DBUS_CMU_CLKOUT1(0x3, 0x1)
#define CMU_CLKOUT1_PD2 SILABS_DBUS_CMU_CLKOUT1(0x3, 0x2)
#define CMU_CLKOUT1_PD3 SILABS_DBUS_CMU_CLKOUT1(0x3, 0x3)
#define CMU_CLKOUT1_PD4 SILABS_DBUS_CMU_CLKOUT1(0x3, 0x4)
#define CMU_CLKOUT2_PA0 SILABS_DBUS_CMU_CLKOUT2(0x0, 0x0)
#define CMU_CLKOUT2_PA1 SILABS_DBUS_CMU_CLKOUT2(0x0, 0x1)
#define CMU_CLKOUT2_PA2 SILABS_DBUS_CMU_CLKOUT2(0x0, 0x2)
#define CMU_CLKOUT2_PA3 SILABS_DBUS_CMU_CLKOUT2(0x0, 0x3)
#define CMU_CLKOUT2_PA4 SILABS_DBUS_CMU_CLKOUT2(0x0, 0x4)
#define CMU_CLKOUT2_PA5 SILABS_DBUS_CMU_CLKOUT2(0x0, 0x5)
#define CMU_CLKOUT2_PA6 SILABS_DBUS_CMU_CLKOUT2(0x0, 0x6)
#define CMU_CLKOUT2_PB0 SILABS_DBUS_CMU_CLKOUT2(0x1, 0x0)
#define CMU_CLKOUT2_PB1 SILABS_DBUS_CMU_CLKOUT2(0x1, 0x1)
#define CMU_CLKIN0_PC0  SILABS_DBUS_CMU_CLKIN0(0x2, 0x0)
#define CMU_CLKIN0_PC1  SILABS_DBUS_CMU_CLKIN0(0x2, 0x1)
#define CMU_CLKIN0_PC2  SILABS_DBUS_CMU_CLKIN0(0x2, 0x2)
#define CMU_CLKIN0_PC3  SILABS_DBUS_CMU_CLKIN0(0x2, 0x3)
#define CMU_CLKIN0_PC4  SILABS_DBUS_CMU_CLKIN0(0x2, 0x4)
#define CMU_CLKIN0_PC5  SILABS_DBUS_CMU_CLKIN0(0x2, 0x5)
#define CMU_CLKIN0_PD0  SILABS_DBUS_CMU_CLKIN0(0x3, 0x0)
#define CMU_CLKIN0_PD1  SILABS_DBUS_CMU_CLKIN0(0x3, 0x1)
#define CMU_CLKIN0_PD2  SILABS_DBUS_CMU_CLKIN0(0x3, 0x2)
#define CMU_CLKIN0_PD3  SILABS_DBUS_CMU_CLKIN0(0x3, 0x3)
#define CMU_CLKIN0_PD4  SILABS_DBUS_CMU_CLKIN0(0x3, 0x4)

#define PTI_DCLK_PC0   SILABS_DBUS_PTI_DCLK(0x2, 0x0)
#define PTI_DCLK_PC1   SILABS_DBUS_PTI_DCLK(0x2, 0x1)
#define PTI_DCLK_PC2   SILABS_DBUS_PTI_DCLK(0x2, 0x2)
#define PTI_DCLK_PC3   SILABS_DBUS_PTI_DCLK(0x2, 0x3)
#define PTI_DCLK_PC4   SILABS_DBUS_PTI_DCLK(0x2, 0x4)
#define PTI_DCLK_PC5   SILABS_DBUS_PTI_DCLK(0x2, 0x5)
#define PTI_DCLK_PD0   SILABS_DBUS_PTI_DCLK(0x3, 0x0)
#define PTI_DCLK_PD1   SILABS_DBUS_PTI_DCLK(0x3, 0x1)
#define PTI_DCLK_PD2   SILABS_DBUS_PTI_DCLK(0x3, 0x2)
#define PTI_DCLK_PD3   SILABS_DBUS_PTI_DCLK(0x3, 0x3)
#define PTI_DCLK_PD4   SILABS_DBUS_PTI_DCLK(0x3, 0x4)
#define PTI_DFRAME_PC0 SILABS_DBUS_PTI_DFRAME(0x2, 0x0)
#define PTI_DFRAME_PC1 SILABS_DBUS_PTI_DFRAME(0x2, 0x1)
#define PTI_DFRAME_PC2 SILABS_DBUS_PTI_DFRAME(0x2, 0x2)
#define PTI_DFRAME_PC3 SILABS_DBUS_PTI_DFRAME(0x2, 0x3)
#define PTI_DFRAME_PC4 SILABS_DBUS_PTI_DFRAME(0x2, 0x4)
#define PTI_DFRAME_PC5 SILABS_DBUS_PTI_DFRAME(0x2, 0x5)
#define PTI_DFRAME_PD0 SILABS_DBUS_PTI_DFRAME(0x3, 0x0)
#define PTI_DFRAME_PD1 SILABS_DBUS_PTI_DFRAME(0x3, 0x1)
#define PTI_DFRAME_PD2 SILABS_DBUS_PTI_DFRAME(0x3, 0x2)
#define PTI_DFRAME_PD3 SILABS_DBUS_PTI_DFRAME(0x3, 0x3)
#define PTI_DFRAME_PD4 SILABS_DBUS_PTI_DFRAME(0x3, 0x4)
#define PTI_DOUT_PC0   SILABS_DBUS_PTI_DOUT(0x2, 0x0)
#define PTI_DOUT_PC1   SILABS_DBUS_PTI_DOUT(0x2, 0x1)
#define PTI_DOUT_PC2   SILABS_DBUS_PTI_DOUT(0x2, 0x2)
#define PTI_DOUT_PC3   SILABS_DBUS_PTI_DOUT(0x2, 0x3)
#define PTI_DOUT_PC4   SILABS_DBUS_PTI_DOUT(0x2, 0x4)
#define PTI_DOUT_PC5   SILABS_DBUS_PTI_DOUT(0x2, 0x5)
#define PTI_DOUT_PD0   SILABS_DBUS_PTI_DOUT(0x3, 0x0)
#define PTI_DOUT_PD1   SILABS_DBUS_PTI_DOUT(0x3, 0x1)
#define PTI_DOUT_PD2   SILABS_DBUS_PTI_DOUT(0x3, 0x2)
#define PTI_DOUT_PD3   SILABS_DBUS_PTI_DOUT(0x3, 0x3)
#define PTI_DOUT_PD4   SILABS_DBUS_PTI_DOUT(0x3, 0x4)

#define I2C0_SCL_PA0 SILABS_DBUS_I2C0_SCL(0x0, 0x0)
#define I2C0_SCL_PA1 SILABS_DBUS_I2C0_SCL(0x0, 0x1)
#define I2C0_SCL_PA2 SILABS_DBUS_I2C0_SCL(0x0, 0x2)
#define I2C0_SCL_PA3 SILABS_DBUS_I2C0_SCL(0x0, 0x3)
#define I2C0_SCL_PA4 SILABS_DBUS_I2C0_SCL(0x0, 0x4)
#define I2C0_SCL_PA5 SILABS_DBUS_I2C0_SCL(0x0, 0x5)
#define I2C0_SCL_PA6 SILABS_DBUS_I2C0_SCL(0x0, 0x6)
#define I2C0_SCL_PB0 SILABS_DBUS_I2C0_SCL(0x1, 0x0)
#define I2C0_SCL_PB1 SILABS_DBUS_I2C0_SCL(0x1, 0x1)
#define I2C0_SCL_PC0 SILABS_DBUS_I2C0_SCL(0x2, 0x0)
#define I2C0_SCL_PC1 SILABS_DBUS_I2C0_SCL(0x2, 0x1)
#define I2C0_SCL_PC2 SILABS_DBUS_I2C0_SCL(0x2, 0x2)
#define I2C0_SCL_PC3 SILABS_DBUS_I2C0_SCL(0x2, 0x3)
#define I2C0_SCL_PC4 SILABS_DBUS_I2C0_SCL(0x2, 0x4)
#define I2C0_SCL_PC5 SILABS_DBUS_I2C0_SCL(0x2, 0x5)
#define I2C0_SCL_PD0 SILABS_DBUS_I2C0_SCL(0x3, 0x0)
#define I2C0_SCL_PD1 SILABS_DBUS_I2C0_SCL(0x3, 0x1)
#define I2C0_SCL_PD2 SILABS_DBUS_I2C0_SCL(0x3, 0x2)
#define I2C0_SCL_PD3 SILABS_DBUS_I2C0_SCL(0x3, 0x3)
#define I2C0_SCL_PD4 SILABS_DBUS_I2C0_SCL(0x3, 0x4)
#define I2C0_SDA_PA0 SILABS_DBUS_I2C0_SDA(0x0, 0x0)
#define I2C0_SDA_PA1 SILABS_DBUS_I2C0_SDA(0x0, 0x1)
#define I2C0_SDA_PA2 SILABS_DBUS_I2C0_SDA(0x0, 0x2)
#define I2C0_SDA_PA3 SILABS_DBUS_I2C0_SDA(0x0, 0x3)
#define I2C0_SDA_PA4 SILABS_DBUS_I2C0_SDA(0x0, 0x4)
#define I2C0_SDA_PA5 SILABS_DBUS_I2C0_SDA(0x0, 0x5)
#define I2C0_SDA_PA6 SILABS_DBUS_I2C0_SDA(0x0, 0x6)
#define I2C0_SDA_PB0 SILABS_DBUS_I2C0_SDA(0x1, 0x0)
#define I2C0_SDA_PB1 SILABS_DBUS_I2C0_SDA(0x1, 0x1)
#define I2C0_SDA_PC0 SILABS_DBUS_I2C0_SDA(0x2, 0x0)
#define I2C0_SDA_PC1 SILABS_DBUS_I2C0_SDA(0x2, 0x1)
#define I2C0_SDA_PC2 SILABS_DBUS_I2C0_SDA(0x2, 0x2)
#define I2C0_SDA_PC3 SILABS_DBUS_I2C0_SDA(0x2, 0x3)
#define I2C0_SDA_PC4 SILABS_DBUS_I2C0_SDA(0x2, 0x4)
#define I2C0_SDA_PC5 SILABS_DBUS_I2C0_SDA(0x2, 0x5)
#define I2C0_SDA_PD0 SILABS_DBUS_I2C0_SDA(0x3, 0x0)
#define I2C0_SDA_PD1 SILABS_DBUS_I2C0_SDA(0x3, 0x1)
#define I2C0_SDA_PD2 SILABS_DBUS_I2C0_SDA(0x3, 0x2)
#define I2C0_SDA_PD3 SILABS_DBUS_I2C0_SDA(0x3, 0x3)
#define I2C0_SDA_PD4 SILABS_DBUS_I2C0_SDA(0x3, 0x4)

#define I2C1_SCL_PC0 SILABS_DBUS_I2C1_SCL(0x2, 0x0)
#define I2C1_SCL_PC1 SILABS_DBUS_I2C1_SCL(0x2, 0x1)
#define I2C1_SCL_PC2 SILABS_DBUS_I2C1_SCL(0x2, 0x2)
#define I2C1_SCL_PC3 SILABS_DBUS_I2C1_SCL(0x2, 0x3)
#define I2C1_SCL_PC4 SILABS_DBUS_I2C1_SCL(0x2, 0x4)
#define I2C1_SCL_PC5 SILABS_DBUS_I2C1_SCL(0x2, 0x5)
#define I2C1_SCL_PD0 SILABS_DBUS_I2C1_SCL(0x3, 0x0)
#define I2C1_SCL_PD1 SILABS_DBUS_I2C1_SCL(0x3, 0x1)
#define I2C1_SCL_PD2 SILABS_DBUS_I2C1_SCL(0x3, 0x2)
#define I2C1_SCL_PD3 SILABS_DBUS_I2C1_SCL(0x3, 0x3)
#define I2C1_SCL_PD4 SILABS_DBUS_I2C1_SCL(0x3, 0x4)
#define I2C1_SDA_PC0 SILABS_DBUS_I2C1_SDA(0x2, 0x0)
#define I2C1_SDA_PC1 SILABS_DBUS_I2C1_SDA(0x2, 0x1)
#define I2C1_SDA_PC2 SILABS_DBUS_I2C1_SDA(0x2, 0x2)
#define I2C1_SDA_PC3 SILABS_DBUS_I2C1_SDA(0x2, 0x3)
#define I2C1_SDA_PC4 SILABS_DBUS_I2C1_SDA(0x2, 0x4)
#define I2C1_SDA_PC5 SILABS_DBUS_I2C1_SDA(0x2, 0x5)
#define I2C1_SDA_PD0 SILABS_DBUS_I2C1_SDA(0x3, 0x0)
#define I2C1_SDA_PD1 SILABS_DBUS_I2C1_SDA(0x3, 0x1)
#define I2C1_SDA_PD2 SILABS_DBUS_I2C1_SDA(0x3, 0x2)
#define I2C1_SDA_PD3 SILABS_DBUS_I2C1_SDA(0x3, 0x3)
#define I2C1_SDA_PD4 SILABS_DBUS_I2C1_SDA(0x3, 0x4)

#define LETIMER0_OUT0_PA0 SILABS_DBUS_LETIMER0_OUT0(0x0, 0x0)
#define LETIMER0_OUT0_PA1 SILABS_DBUS_LETIMER0_OUT0(0x0, 0x1)
#define LETIMER0_OUT0_PA2 SILABS_DBUS_LETIMER0_OUT0(0x0, 0x2)
#define LETIMER0_OUT0_PA3 SILABS_DBUS_LETIMER0_OUT0(0x0, 0x3)
#define LETIMER0_OUT0_PA4 SILABS_DBUS_LETIMER0_OUT0(0x0, 0x4)
#define LETIMER0_OUT0_PA5 SILABS_DBUS_LETIMER0_OUT0(0x0, 0x5)
#define LETIMER0_OUT0_PA6 SILABS_DBUS_LETIMER0_OUT0(0x0, 0x6)
#define LETIMER0_OUT0_PB0 SILABS_DBUS_LETIMER0_OUT0(0x1, 0x0)
#define LETIMER0_OUT0_PB1 SILABS_DBUS_LETIMER0_OUT0(0x1, 0x1)
#define LETIMER0_OUT1_PA0 SILABS_DBUS_LETIMER0_OUT1(0x0, 0x0)
#define LETIMER0_OUT1_PA1 SILABS_DBUS_LETIMER0_OUT1(0x0, 0x1)
#define LETIMER0_OUT1_PA2 SILABS_DBUS_LETIMER0_OUT1(0x0, 0x2)
#define LETIMER0_OUT1_PA3 SILABS_DBUS_LETIMER0_OUT1(0x0, 0x3)
#define LETIMER0_OUT1_PA4 SILABS_DBUS_LETIMER0_OUT1(0x0, 0x4)
#define LETIMER0_OUT1_PA5 SILABS_DBUS_LETIMER0_OUT1(0x0, 0x5)
#define LETIMER0_OUT1_PA6 SILABS_DBUS_LETIMER0_OUT1(0x0, 0x6)
#define LETIMER0_OUT1_PB0 SILABS_DBUS_LETIMER0_OUT1(0x1, 0x0)
#define LETIMER0_OUT1_PB1 SILABS_DBUS_LETIMER0_OUT1(0x1, 0x1)

#define MODEM_ANT0_PA0 SILABS_DBUS_MODEM_ANT0(0x0, 0x0)
#define MODEM_ANT0_PA1 SILABS_DBUS_MODEM_ANT0(0x0, 0x1)
#define MODEM_ANT0_PA2 SILABS_DBUS_MODEM_ANT0(0x0, 0x2)
#define MODEM_ANT0_PA3 SILABS_DBUS_MODEM_ANT0(0x0, 0x3)
#define MODEM_ANT0_PA4 SILABS_DBUS_MODEM_ANT0(0x0, 0x4)
#define MODEM_ANT0_PA5 SILABS_DBUS_MODEM_ANT0(0x0, 0x5)
#define MODEM_ANT0_PA6 SILABS_DBUS_MODEM_ANT0(0x0, 0x6)
#define MODEM_ANT0_PB0 SILABS_DBUS_MODEM_ANT0(0x1, 0x0)
#define MODEM_ANT0_PB1 SILABS_DBUS_MODEM_ANT0(0x1, 0x1)
#define MODEM_ANT0_PC0 SILABS_DBUS_MODEM_ANT0(0x2, 0x0)
#define MODEM_ANT0_PC1 SILABS_DBUS_MODEM_ANT0(0x2, 0x1)
#define MODEM_ANT0_PC2 SILABS_DBUS_MODEM_ANT0(0x2, 0x2)
#define MODEM_ANT0_PC3 SILABS_DBUS_MODEM_ANT0(0x2, 0x3)
#define MODEM_ANT0_PC4 SILABS_DBUS_MODEM_ANT0(0x2, 0x4)
#define MODEM_ANT0_PC5 SILABS_DBUS_MODEM_ANT0(0x2, 0x5)
#define MODEM_ANT0_PD0 SILABS_DBUS_MODEM_ANT0(0x3, 0x0)
#define MODEM_ANT0_PD1 SILABS_DBUS_MODEM_ANT0(0x3, 0x1)
#define MODEM_ANT0_PD2 SILABS_DBUS_MODEM_ANT0(0x3, 0x2)
#define MODEM_ANT0_PD3 SILABS_DBUS_MODEM_ANT0(0x3, 0x3)
#define MODEM_ANT0_PD4 SILABS_DBUS_MODEM_ANT0(0x3, 0x4)
#define MODEM_ANT1_PA0 SILABS_DBUS_MODEM_ANT1(0x0, 0x0)
#define MODEM_ANT1_PA1 SILABS_DBUS_MODEM_ANT1(0x0, 0x1)
#define MODEM_ANT1_PA2 SILABS_DBUS_MODEM_ANT1(0x0, 0x2)
#define MODEM_ANT1_PA3 SILABS_DBUS_MODEM_ANT1(0x0, 0x3)
#define MODEM_ANT1_PA4 SILABS_DBUS_MODEM_ANT1(0x0, 0x4)
#define MODEM_ANT1_PA5 SILABS_DBUS_MODEM_ANT1(0x0, 0x5)
#define MODEM_ANT1_PA6 SILABS_DBUS_MODEM_ANT1(0x0, 0x6)
#define MODEM_ANT1_PB0 SILABS_DBUS_MODEM_ANT1(0x1, 0x0)
#define MODEM_ANT1_PB1 SILABS_DBUS_MODEM_ANT1(0x1, 0x1)
#define MODEM_ANT1_PC0 SILABS_DBUS_MODEM_ANT1(0x2, 0x0)
#define MODEM_ANT1_PC1 SILABS_DBUS_MODEM_ANT1(0x2, 0x1)
#define MODEM_ANT1_PC2 SILABS_DBUS_MODEM_ANT1(0x2, 0x2)
#define MODEM_ANT1_PC3 SILABS_DBUS_MODEM_ANT1(0x2, 0x3)
#define MODEM_ANT1_PC4 SILABS_DBUS_MODEM_ANT1(0x2, 0x4)
#define MODEM_ANT1_PC5 SILABS_DBUS_MODEM_ANT1(0x2, 0x5)
#define MODEM_ANT1_PD0 SILABS_DBUS_MODEM_ANT1(0x3, 0x0)
#define MODEM_ANT1_PD1 SILABS_DBUS_MODEM_ANT1(0x3, 0x1)
#define MODEM_ANT1_PD2 SILABS_DBUS_MODEM_ANT1(0x3, 0x2)
#define MODEM_ANT1_PD3 SILABS_DBUS_MODEM_ANT1(0x3, 0x3)
#define MODEM_ANT1_PD4 SILABS_DBUS_MODEM_ANT1(0x3, 0x4)
#define MODEM_DCLK_PA0 SILABS_DBUS_MODEM_DCLK(0x0, 0x0)
#define MODEM_DCLK_PA1 SILABS_DBUS_MODEM_DCLK(0x0, 0x1)
#define MODEM_DCLK_PA2 SILABS_DBUS_MODEM_DCLK(0x0, 0x2)
#define MODEM_DCLK_PA3 SILABS_DBUS_MODEM_DCLK(0x0, 0x3)
#define MODEM_DCLK_PA4 SILABS_DBUS_MODEM_DCLK(0x0, 0x4)
#define MODEM_DCLK_PA5 SILABS_DBUS_MODEM_DCLK(0x0, 0x5)
#define MODEM_DCLK_PA6 SILABS_DBUS_MODEM_DCLK(0x0, 0x6)
#define MODEM_DCLK_PB0 SILABS_DBUS_MODEM_DCLK(0x1, 0x0)
#define MODEM_DCLK_PB1 SILABS_DBUS_MODEM_DCLK(0x1, 0x1)
#define MODEM_DOUT_PA0 SILABS_DBUS_MODEM_DOUT(0x0, 0x0)
#define MODEM_DOUT_PA1 SILABS_DBUS_MODEM_DOUT(0x0, 0x1)
#define MODEM_DOUT_PA2 SILABS_DBUS_MODEM_DOUT(0x0, 0x2)
#define MODEM_DOUT_PA3 SILABS_DBUS_MODEM_DOUT(0x0, 0x3)
#define MODEM_DOUT_PA4 SILABS_DBUS_MODEM_DOUT(0x0, 0x4)
#define MODEM_DOUT_PA5 SILABS_DBUS_MODEM_DOUT(0x0, 0x5)
#define MODEM_DOUT_PA6 SILABS_DBUS_MODEM_DOUT(0x0, 0x6)
#define MODEM_DOUT_PB0 SILABS_DBUS_MODEM_DOUT(0x1, 0x0)
#define MODEM_DOUT_PB1 SILABS_DBUS_MODEM_DOUT(0x1, 0x1)
#define MODEM_DIN_PA0  SILABS_DBUS_MODEM_DIN(0x0, 0x0)
#define MODEM_DIN_PA1  SILABS_DBUS_MODEM_DIN(0x0, 0x1)
#define MODEM_DIN_PA2  SILABS_DBUS_MODEM_DIN(0x0, 0x2)
#define MODEM_DIN_PA3  SILABS_DBUS_MODEM_DIN(0x0, 0x3)
#define MODEM_DIN_PA4  SILABS_DBUS_MODEM_DIN(0x0, 0x4)
#define MODEM_DIN_PA5  SILABS_DBUS_MODEM_DIN(0x0, 0x5)
#define MODEM_DIN_PA6  SILABS_DBUS_MODEM_DIN(0x0, 0x6)
#define MODEM_DIN_PB0  SILABS_DBUS_MODEM_DIN(0x1, 0x0)
#define MODEM_DIN_PB1  SILABS_DBUS_MODEM_DIN(0x1, 0x1)

#define PRS0_ASYNCH0_PA0  SILABS_DBUS_PRS0_ASYNCH0(0x0, 0x0)
#define PRS0_ASYNCH0_PA1  SILABS_DBUS_PRS0_ASYNCH0(0x0, 0x1)
#define PRS0_ASYNCH0_PA2  SILABS_DBUS_PRS0_ASYNCH0(0x0, 0x2)
#define PRS0_ASYNCH0_PA3  SILABS_DBUS_PRS0_ASYNCH0(0x0, 0x3)
#define PRS0_ASYNCH0_PA4  SILABS_DBUS_PRS0_ASYNCH0(0x0, 0x4)
#define PRS0_ASYNCH0_PA5  SILABS_DBUS_PRS0_ASYNCH0(0x0, 0x5)
#define PRS0_ASYNCH0_PA6  SILABS_DBUS_PRS0_ASYNCH0(0x0, 0x6)
#define PRS0_ASYNCH0_PB0  SILABS_DBUS_PRS0_ASYNCH0(0x1, 0x0)
#define PRS0_ASYNCH0_PB1  SILABS_DBUS_PRS0_ASYNCH0(0x1, 0x1)
#define PRS0_ASYNCH1_PA0  SILABS_DBUS_PRS0_ASYNCH1(0x0, 0x0)
#define PRS0_ASYNCH1_PA1  SILABS_DBUS_PRS0_ASYNCH1(0x0, 0x1)
#define PRS0_ASYNCH1_PA2  SILABS_DBUS_PRS0_ASYNCH1(0x0, 0x2)
#define PRS0_ASYNCH1_PA3  SILABS_DBUS_PRS0_ASYNCH1(0x0, 0x3)
#define PRS0_ASYNCH1_PA4  SILABS_DBUS_PRS0_ASYNCH1(0x0, 0x4)
#define PRS0_ASYNCH1_PA5  SILABS_DBUS_PRS0_ASYNCH1(0x0, 0x5)
#define PRS0_ASYNCH1_PA6  SILABS_DBUS_PRS0_ASYNCH1(0x0, 0x6)
#define PRS0_ASYNCH1_PB0  SILABS_DBUS_PRS0_ASYNCH1(0x1, 0x0)
#define PRS0_ASYNCH1_PB1  SILABS_DBUS_PRS0_ASYNCH1(0x1, 0x1)
#define PRS0_ASYNCH2_PA0  SILABS_DBUS_PRS0_ASYNCH2(0x0, 0x0)
#define PRS0_ASYNCH2_PA1  SILABS_DBUS_PRS0_ASYNCH2(0x0, 0x1)
#define PRS0_ASYNCH2_PA2  SILABS_DBUS_PRS0_ASYNCH2(0x0, 0x2)
#define PRS0_ASYNCH2_PA3  SILABS_DBUS_PRS0_ASYNCH2(0x0, 0x3)
#define PRS0_ASYNCH2_PA4  SILABS_DBUS_PRS0_ASYNCH2(0x0, 0x4)
#define PRS0_ASYNCH2_PA5  SILABS_DBUS_PRS0_ASYNCH2(0x0, 0x5)
#define PRS0_ASYNCH2_PA6  SILABS_DBUS_PRS0_ASYNCH2(0x0, 0x6)
#define PRS0_ASYNCH2_PB0  SILABS_DBUS_PRS0_ASYNCH2(0x1, 0x0)
#define PRS0_ASYNCH2_PB1  SILABS_DBUS_PRS0_ASYNCH2(0x1, 0x1)
#define PRS0_ASYNCH3_PA0  SILABS_DBUS_PRS0_ASYNCH3(0x0, 0x0)
#define PRS0_ASYNCH3_PA1  SILABS_DBUS_PRS0_ASYNCH3(0x0, 0x1)
#define PRS0_ASYNCH3_PA2  SILABS_DBUS_PRS0_ASYNCH3(0x0, 0x2)
#define PRS0_ASYNCH3_PA3  SILABS_DBUS_PRS0_ASYNCH3(0x0, 0x3)
#define PRS0_ASYNCH3_PA4  SILABS_DBUS_PRS0_ASYNCH3(0x0, 0x4)
#define PRS0_ASYNCH3_PA5  SILABS_DBUS_PRS0_ASYNCH3(0x0, 0x5)
#define PRS0_ASYNCH3_PA6  SILABS_DBUS_PRS0_ASYNCH3(0x0, 0x6)
#define PRS0_ASYNCH3_PB0  SILABS_DBUS_PRS0_ASYNCH3(0x1, 0x0)
#define PRS0_ASYNCH3_PB1  SILABS_DBUS_PRS0_ASYNCH3(0x1, 0x1)
#define PRS0_ASYNCH4_PA0  SILABS_DBUS_PRS0_ASYNCH4(0x0, 0x0)
#define PRS0_ASYNCH4_PA1  SILABS_DBUS_PRS0_ASYNCH4(0x0, 0x1)
#define PRS0_ASYNCH4_PA2  SILABS_DBUS_PRS0_ASYNCH4(0x0, 0x2)
#define PRS0_ASYNCH4_PA3  SILABS_DBUS_PRS0_ASYNCH4(0x0, 0x3)
#define PRS0_ASYNCH4_PA4  SILABS_DBUS_PRS0_ASYNCH4(0x0, 0x4)
#define PRS0_ASYNCH4_PA5  SILABS_DBUS_PRS0_ASYNCH4(0x0, 0x5)
#define PRS0_ASYNCH4_PA6  SILABS_DBUS_PRS0_ASYNCH4(0x0, 0x6)
#define PRS0_ASYNCH4_PB0  SILABS_DBUS_PRS0_ASYNCH4(0x1, 0x0)
#define PRS0_ASYNCH4_PB1  SILABS_DBUS_PRS0_ASYNCH4(0x1, 0x1)
#define PRS0_ASYNCH5_PA0  SILABS_DBUS_PRS0_ASYNCH5(0x0, 0x0)
#define PRS0_ASYNCH5_PA1  SILABS_DBUS_PRS0_ASYNCH5(0x0, 0x1)
#define PRS0_ASYNCH5_PA2  SILABS_DBUS_PRS0_ASYNCH5(0x0, 0x2)
#define PRS0_ASYNCH5_PA3  SILABS_DBUS_PRS0_ASYNCH5(0x0, 0x3)
#define PRS0_ASYNCH5_PA4  SILABS_DBUS_PRS0_ASYNCH5(0x0, 0x4)
#define PRS0_ASYNCH5_PA5  SILABS_DBUS_PRS0_ASYNCH5(0x0, 0x5)
#define PRS0_ASYNCH5_PA6  SILABS_DBUS_PRS0_ASYNCH5(0x0, 0x6)
#define PRS0_ASYNCH5_PB0  SILABS_DBUS_PRS0_ASYNCH5(0x1, 0x0)
#define PRS0_ASYNCH5_PB1  SILABS_DBUS_PRS0_ASYNCH5(0x1, 0x1)
#define PRS0_ASYNCH6_PC0  SILABS_DBUS_PRS0_ASYNCH6(0x2, 0x0)
#define PRS0_ASYNCH6_PC1  SILABS_DBUS_PRS0_ASYNCH6(0x2, 0x1)
#define PRS0_ASYNCH6_PC2  SILABS_DBUS_PRS0_ASYNCH6(0x2, 0x2)
#define PRS0_ASYNCH6_PC3  SILABS_DBUS_PRS0_ASYNCH6(0x2, 0x3)
#define PRS0_ASYNCH6_PC4  SILABS_DBUS_PRS0_ASYNCH6(0x2, 0x4)
#define PRS0_ASYNCH6_PC5  SILABS_DBUS_PRS0_ASYNCH6(0x2, 0x5)
#define PRS0_ASYNCH6_PD0  SILABS_DBUS_PRS0_ASYNCH6(0x3, 0x0)
#define PRS0_ASYNCH6_PD1  SILABS_DBUS_PRS0_ASYNCH6(0x3, 0x1)
#define PRS0_ASYNCH6_PD2  SILABS_DBUS_PRS0_ASYNCH6(0x3, 0x2)
#define PRS0_ASYNCH6_PD3  SILABS_DBUS_PRS0_ASYNCH6(0x3, 0x3)
#define PRS0_ASYNCH6_PD4  SILABS_DBUS_PRS0_ASYNCH6(0x3, 0x4)
#define PRS0_ASYNCH7_PC0  SILABS_DBUS_PRS0_ASYNCH7(0x2, 0x0)
#define PRS0_ASYNCH7_PC1  SILABS_DBUS_PRS0_ASYNCH7(0x2, 0x1)
#define PRS0_ASYNCH7_PC2  SILABS_DBUS_PRS0_ASYNCH7(0x2, 0x2)
#define PRS0_ASYNCH7_PC3  SILABS_DBUS_PRS0_ASYNCH7(0x2, 0x3)
#define PRS0_ASYNCH7_PC4  SILABS_DBUS_PRS0_ASYNCH7(0x2, 0x4)
#define PRS0_ASYNCH7_PC5  SILABS_DBUS_PRS0_ASYNCH7(0x2, 0x5)
#define PRS0_ASYNCH7_PD0  SILABS_DBUS_PRS0_ASYNCH7(0x3, 0x0)
#define PRS0_ASYNCH7_PD1  SILABS_DBUS_PRS0_ASYNCH7(0x3, 0x1)
#define PRS0_ASYNCH7_PD2  SILABS_DBUS_PRS0_ASYNCH7(0x3, 0x2)
#define PRS0_ASYNCH7_PD3  SILABS_DBUS_PRS0_ASYNCH7(0x3, 0x3)
#define PRS0_ASYNCH7_PD4  SILABS_DBUS_PRS0_ASYNCH7(0x3, 0x4)
#define PRS0_ASYNCH8_PC0  SILABS_DBUS_PRS0_ASYNCH8(0x2, 0x0)
#define PRS0_ASYNCH8_PC1  SILABS_DBUS_PRS0_ASYNCH8(0x2, 0x1)
#define PRS0_ASYNCH8_PC2  SILABS_DBUS_PRS0_ASYNCH8(0x2, 0x2)
#define PRS0_ASYNCH8_PC3  SILABS_DBUS_PRS0_ASYNCH8(0x2, 0x3)
#define PRS0_ASYNCH8_PC4  SILABS_DBUS_PRS0_ASYNCH8(0x2, 0x4)
#define PRS0_ASYNCH8_PC5  SILABS_DBUS_PRS0_ASYNCH8(0x2, 0x5)
#define PRS0_ASYNCH8_PD0  SILABS_DBUS_PRS0_ASYNCH8(0x3, 0x0)
#define PRS0_ASYNCH8_PD1  SILABS_DBUS_PRS0_ASYNCH8(0x3, 0x1)
#define PRS0_ASYNCH8_PD2  SILABS_DBUS_PRS0_ASYNCH8(0x3, 0x2)
#define PRS0_ASYNCH8_PD3  SILABS_DBUS_PRS0_ASYNCH8(0x3, 0x3)
#define PRS0_ASYNCH8_PD4  SILABS_DBUS_PRS0_ASYNCH8(0x3, 0x4)
#define PRS0_ASYNCH9_PC0  SILABS_DBUS_PRS0_ASYNCH9(0x2, 0x0)
#define PRS0_ASYNCH9_PC1  SILABS_DBUS_PRS0_ASYNCH9(0x2, 0x1)
#define PRS0_ASYNCH9_PC2  SILABS_DBUS_PRS0_ASYNCH9(0x2, 0x2)
#define PRS0_ASYNCH9_PC3  SILABS_DBUS_PRS0_ASYNCH9(0x2, 0x3)
#define PRS0_ASYNCH9_PC4  SILABS_DBUS_PRS0_ASYNCH9(0x2, 0x4)
#define PRS0_ASYNCH9_PC5  SILABS_DBUS_PRS0_ASYNCH9(0x2, 0x5)
#define PRS0_ASYNCH9_PD0  SILABS_DBUS_PRS0_ASYNCH9(0x3, 0x0)
#define PRS0_ASYNCH9_PD1  SILABS_DBUS_PRS0_ASYNCH9(0x3, 0x1)
#define PRS0_ASYNCH9_PD2  SILABS_DBUS_PRS0_ASYNCH9(0x3, 0x2)
#define PRS0_ASYNCH9_PD3  SILABS_DBUS_PRS0_ASYNCH9(0x3, 0x3)
#define PRS0_ASYNCH9_PD4  SILABS_DBUS_PRS0_ASYNCH9(0x3, 0x4)
#define PRS0_ASYNCH10_PC0 SILABS_DBUS_PRS0_ASYNCH10(0x2, 0x0)
#define PRS0_ASYNCH10_PC1 SILABS_DBUS_PRS0_ASYNCH10(0x2, 0x1)
#define PRS0_ASYNCH10_PC2 SILABS_DBUS_PRS0_ASYNCH10(0x2, 0x2)
#define PRS0_ASYNCH10_PC3 SILABS_DBUS_PRS0_ASYNCH10(0x2, 0x3)
#define PRS0_ASYNCH10_PC4 SILABS_DBUS_PRS0_ASYNCH10(0x2, 0x4)
#define PRS0_ASYNCH10_PC5 SILABS_DBUS_PRS0_ASYNCH10(0x2, 0x5)
#define PRS0_ASYNCH10_PD0 SILABS_DBUS_PRS0_ASYNCH10(0x3, 0x0)
#define PRS0_ASYNCH10_PD1 SILABS_DBUS_PRS0_ASYNCH10(0x3, 0x1)
#define PRS0_ASYNCH10_PD2 SILABS_DBUS_PRS0_ASYNCH10(0x3, 0x2)
#define PRS0_ASYNCH10_PD3 SILABS_DBUS_PRS0_ASYNCH10(0x3, 0x3)
#define PRS0_ASYNCH10_PD4 SILABS_DBUS_PRS0_ASYNCH10(0x3, 0x4)
#define PRS0_ASYNCH11_PC0 SILABS_DBUS_PRS0_ASYNCH11(0x2, 0x0)
#define PRS0_ASYNCH11_PC1 SILABS_DBUS_PRS0_ASYNCH11(0x2, 0x1)
#define PRS0_ASYNCH11_PC2 SILABS_DBUS_PRS0_ASYNCH11(0x2, 0x2)
#define PRS0_ASYNCH11_PC3 SILABS_DBUS_PRS0_ASYNCH11(0x2, 0x3)
#define PRS0_ASYNCH11_PC4 SILABS_DBUS_PRS0_ASYNCH11(0x2, 0x4)
#define PRS0_ASYNCH11_PC5 SILABS_DBUS_PRS0_ASYNCH11(0x2, 0x5)
#define PRS0_ASYNCH11_PD0 SILABS_DBUS_PRS0_ASYNCH11(0x3, 0x0)
#define PRS0_ASYNCH11_PD1 SILABS_DBUS_PRS0_ASYNCH11(0x3, 0x1)
#define PRS0_ASYNCH11_PD2 SILABS_DBUS_PRS0_ASYNCH11(0x3, 0x2)
#define PRS0_ASYNCH11_PD3 SILABS_DBUS_PRS0_ASYNCH11(0x3, 0x3)
#define PRS0_ASYNCH11_PD4 SILABS_DBUS_PRS0_ASYNCH11(0x3, 0x4)
#define PRS0_SYNCH0_PA0   SILABS_DBUS_PRS0_SYNCH0(0x0, 0x0)
#define PRS0_SYNCH0_PA1   SILABS_DBUS_PRS0_SYNCH0(0x0, 0x1)
#define PRS0_SYNCH0_PA2   SILABS_DBUS_PRS0_SYNCH0(0x0, 0x2)
#define PRS0_SYNCH0_PA3   SILABS_DBUS_PRS0_SYNCH0(0x0, 0x3)
#define PRS0_SYNCH0_PA4   SILABS_DBUS_PRS0_SYNCH0(0x0, 0x4)
#define PRS0_SYNCH0_PA5   SILABS_DBUS_PRS0_SYNCH0(0x0, 0x5)
#define PRS0_SYNCH0_PA6   SILABS_DBUS_PRS0_SYNCH0(0x0, 0x6)
#define PRS0_SYNCH0_PB0   SILABS_DBUS_PRS0_SYNCH0(0x1, 0x0)
#define PRS0_SYNCH0_PB1   SILABS_DBUS_PRS0_SYNCH0(0x1, 0x1)
#define PRS0_SYNCH0_PC0   SILABS_DBUS_PRS0_SYNCH0(0x2, 0x0)
#define PRS0_SYNCH0_PC1   SILABS_DBUS_PRS0_SYNCH0(0x2, 0x1)
#define PRS0_SYNCH0_PC2   SILABS_DBUS_PRS0_SYNCH0(0x2, 0x2)
#define PRS0_SYNCH0_PC3   SILABS_DBUS_PRS0_SYNCH0(0x2, 0x3)
#define PRS0_SYNCH0_PC4   SILABS_DBUS_PRS0_SYNCH0(0x2, 0x4)
#define PRS0_SYNCH0_PC5   SILABS_DBUS_PRS0_SYNCH0(0x2, 0x5)
#define PRS0_SYNCH0_PD0   SILABS_DBUS_PRS0_SYNCH0(0x3, 0x0)
#define PRS0_SYNCH0_PD1   SILABS_DBUS_PRS0_SYNCH0(0x3, 0x1)
#define PRS0_SYNCH0_PD2   SILABS_DBUS_PRS0_SYNCH0(0x3, 0x2)
#define PRS0_SYNCH0_PD3   SILABS_DBUS_PRS0_SYNCH0(0x3, 0x3)
#define PRS0_SYNCH0_PD4   SILABS_DBUS_PRS0_SYNCH0(0x3, 0x4)
#define PRS0_SYNCH1_PA0   SILABS_DBUS_PRS0_SYNCH1(0x0, 0x0)
#define PRS0_SYNCH1_PA1   SILABS_DBUS_PRS0_SYNCH1(0x0, 0x1)
#define PRS0_SYNCH1_PA2   SILABS_DBUS_PRS0_SYNCH1(0x0, 0x2)
#define PRS0_SYNCH1_PA3   SILABS_DBUS_PRS0_SYNCH1(0x0, 0x3)
#define PRS0_SYNCH1_PA4   SILABS_DBUS_PRS0_SYNCH1(0x0, 0x4)
#define PRS0_SYNCH1_PA5   SILABS_DBUS_PRS0_SYNCH1(0x0, 0x5)
#define PRS0_SYNCH1_PA6   SILABS_DBUS_PRS0_SYNCH1(0x0, 0x6)
#define PRS0_SYNCH1_PB0   SILABS_DBUS_PRS0_SYNCH1(0x1, 0x0)
#define PRS0_SYNCH1_PB1   SILABS_DBUS_PRS0_SYNCH1(0x1, 0x1)
#define PRS0_SYNCH1_PC0   SILABS_DBUS_PRS0_SYNCH1(0x2, 0x0)
#define PRS0_SYNCH1_PC1   SILABS_DBUS_PRS0_SYNCH1(0x2, 0x1)
#define PRS0_SYNCH1_PC2   SILABS_DBUS_PRS0_SYNCH1(0x2, 0x2)
#define PRS0_SYNCH1_PC3   SILABS_DBUS_PRS0_SYNCH1(0x2, 0x3)
#define PRS0_SYNCH1_PC4   SILABS_DBUS_PRS0_SYNCH1(0x2, 0x4)
#define PRS0_SYNCH1_PC5   SILABS_DBUS_PRS0_SYNCH1(0x2, 0x5)
#define PRS0_SYNCH1_PD0   SILABS_DBUS_PRS0_SYNCH1(0x3, 0x0)
#define PRS0_SYNCH1_PD1   SILABS_DBUS_PRS0_SYNCH1(0x3, 0x1)
#define PRS0_SYNCH1_PD2   SILABS_DBUS_PRS0_SYNCH1(0x3, 0x2)
#define PRS0_SYNCH1_PD3   SILABS_DBUS_PRS0_SYNCH1(0x3, 0x3)
#define PRS0_SYNCH1_PD4   SILABS_DBUS_PRS0_SYNCH1(0x3, 0x4)
#define PRS0_SYNCH2_PA0   SILABS_DBUS_PRS0_SYNCH2(0x0, 0x0)
#define PRS0_SYNCH2_PA1   SILABS_DBUS_PRS0_SYNCH2(0x0, 0x1)
#define PRS0_SYNCH2_PA2   SILABS_DBUS_PRS0_SYNCH2(0x0, 0x2)
#define PRS0_SYNCH2_PA3   SILABS_DBUS_PRS0_SYNCH2(0x0, 0x3)
#define PRS0_SYNCH2_PA4   SILABS_DBUS_PRS0_SYNCH2(0x0, 0x4)
#define PRS0_SYNCH2_PA5   SILABS_DBUS_PRS0_SYNCH2(0x0, 0x5)
#define PRS0_SYNCH2_PA6   SILABS_DBUS_PRS0_SYNCH2(0x0, 0x6)
#define PRS0_SYNCH2_PB0   SILABS_DBUS_PRS0_SYNCH2(0x1, 0x0)
#define PRS0_SYNCH2_PB1   SILABS_DBUS_PRS0_SYNCH2(0x1, 0x1)
#define PRS0_SYNCH2_PC0   SILABS_DBUS_PRS0_SYNCH2(0x2, 0x0)
#define PRS0_SYNCH2_PC1   SILABS_DBUS_PRS0_SYNCH2(0x2, 0x1)
#define PRS0_SYNCH2_PC2   SILABS_DBUS_PRS0_SYNCH2(0x2, 0x2)
#define PRS0_SYNCH2_PC3   SILABS_DBUS_PRS0_SYNCH2(0x2, 0x3)
#define PRS0_SYNCH2_PC4   SILABS_DBUS_PRS0_SYNCH2(0x2, 0x4)
#define PRS0_SYNCH2_PC5   SILABS_DBUS_PRS0_SYNCH2(0x2, 0x5)
#define PRS0_SYNCH2_PD0   SILABS_DBUS_PRS0_SYNCH2(0x3, 0x0)
#define PRS0_SYNCH2_PD1   SILABS_DBUS_PRS0_SYNCH2(0x3, 0x1)
#define PRS0_SYNCH2_PD2   SILABS_DBUS_PRS0_SYNCH2(0x3, 0x2)
#define PRS0_SYNCH2_PD3   SILABS_DBUS_PRS0_SYNCH2(0x3, 0x3)
#define PRS0_SYNCH2_PD4   SILABS_DBUS_PRS0_SYNCH2(0x3, 0x4)
#define PRS0_SYNCH3_PA0   SILABS_DBUS_PRS0_SYNCH3(0x0, 0x0)
#define PRS0_SYNCH3_PA1   SILABS_DBUS_PRS0_SYNCH3(0x0, 0x1)
#define PRS0_SYNCH3_PA2   SILABS_DBUS_PRS0_SYNCH3(0x0, 0x2)
#define PRS0_SYNCH3_PA3   SILABS_DBUS_PRS0_SYNCH3(0x0, 0x3)
#define PRS0_SYNCH3_PA4   SILABS_DBUS_PRS0_SYNCH3(0x0, 0x4)
#define PRS0_SYNCH3_PA5   SILABS_DBUS_PRS0_SYNCH3(0x0, 0x5)
#define PRS0_SYNCH3_PA6   SILABS_DBUS_PRS0_SYNCH3(0x0, 0x6)
#define PRS0_SYNCH3_PB0   SILABS_DBUS_PRS0_SYNCH3(0x1, 0x0)
#define PRS0_SYNCH3_PB1   SILABS_DBUS_PRS0_SYNCH3(0x1, 0x1)
#define PRS0_SYNCH3_PC0   SILABS_DBUS_PRS0_SYNCH3(0x2, 0x0)
#define PRS0_SYNCH3_PC1   SILABS_DBUS_PRS0_SYNCH3(0x2, 0x1)
#define PRS0_SYNCH3_PC2   SILABS_DBUS_PRS0_SYNCH3(0x2, 0x2)
#define PRS0_SYNCH3_PC3   SILABS_DBUS_PRS0_SYNCH3(0x2, 0x3)
#define PRS0_SYNCH3_PC4   SILABS_DBUS_PRS0_SYNCH3(0x2, 0x4)
#define PRS0_SYNCH3_PC5   SILABS_DBUS_PRS0_SYNCH3(0x2, 0x5)
#define PRS0_SYNCH3_PD0   SILABS_DBUS_PRS0_SYNCH3(0x3, 0x0)
#define PRS0_SYNCH3_PD1   SILABS_DBUS_PRS0_SYNCH3(0x3, 0x1)
#define PRS0_SYNCH3_PD2   SILABS_DBUS_PRS0_SYNCH3(0x3, 0x2)
#define PRS0_SYNCH3_PD3   SILABS_DBUS_PRS0_SYNCH3(0x3, 0x3)
#define PRS0_SYNCH3_PD4   SILABS_DBUS_PRS0_SYNCH3(0x3, 0x4)

#define TIMER0_CC0_PA0   SILABS_DBUS_TIMER0_CC0(0x0, 0x0)
#define TIMER0_CC0_PA1   SILABS_DBUS_TIMER0_CC0(0x0, 0x1)
#define TIMER0_CC0_PA2   SILABS_DBUS_TIMER0_CC0(0x0, 0x2)
#define TIMER0_CC0_PA3   SILABS_DBUS_TIMER0_CC0(0x0, 0x3)
#define TIMER0_CC0_PA4   SILABS_DBUS_TIMER0_CC0(0x0, 0x4)
#define TIMER0_CC0_PA5   SILABS_DBUS_TIMER0_CC0(0x0, 0x5)
#define TIMER0_CC0_PA6   SILABS_DBUS_TIMER0_CC0(0x0, 0x6)
#define TIMER0_CC0_PB0   SILABS_DBUS_TIMER0_CC0(0x1, 0x0)
#define TIMER0_CC0_PB1   SILABS_DBUS_TIMER0_CC0(0x1, 0x1)
#define TIMER0_CC0_PC0   SILABS_DBUS_TIMER0_CC0(0x2, 0x0)
#define TIMER0_CC0_PC1   SILABS_DBUS_TIMER0_CC0(0x2, 0x1)
#define TIMER0_CC0_PC2   SILABS_DBUS_TIMER0_CC0(0x2, 0x2)
#define TIMER0_CC0_PC3   SILABS_DBUS_TIMER0_CC0(0x2, 0x3)
#define TIMER0_CC0_PC4   SILABS_DBUS_TIMER0_CC0(0x2, 0x4)
#define TIMER0_CC0_PC5   SILABS_DBUS_TIMER0_CC0(0x2, 0x5)
#define TIMER0_CC0_PD0   SILABS_DBUS_TIMER0_CC0(0x3, 0x0)
#define TIMER0_CC0_PD1   SILABS_DBUS_TIMER0_CC0(0x3, 0x1)
#define TIMER0_CC0_PD2   SILABS_DBUS_TIMER0_CC0(0x3, 0x2)
#define TIMER0_CC0_PD3   SILABS_DBUS_TIMER0_CC0(0x3, 0x3)
#define TIMER0_CC0_PD4   SILABS_DBUS_TIMER0_CC0(0x3, 0x4)
#define TIMER0_CC1_PA0   SILABS_DBUS_TIMER0_CC1(0x0, 0x0)
#define TIMER0_CC1_PA1   SILABS_DBUS_TIMER0_CC1(0x0, 0x1)
#define TIMER0_CC1_PA2   SILABS_DBUS_TIMER0_CC1(0x0, 0x2)
#define TIMER0_CC1_PA3   SILABS_DBUS_TIMER0_CC1(0x0, 0x3)
#define TIMER0_CC1_PA4   SILABS_DBUS_TIMER0_CC1(0x0, 0x4)
#define TIMER0_CC1_PA5   SILABS_DBUS_TIMER0_CC1(0x0, 0x5)
#define TIMER0_CC1_PA6   SILABS_DBUS_TIMER0_CC1(0x0, 0x6)
#define TIMER0_CC1_PB0   SILABS_DBUS_TIMER0_CC1(0x1, 0x0)
#define TIMER0_CC1_PB1   SILABS_DBUS_TIMER0_CC1(0x1, 0x1)
#define TIMER0_CC1_PC0   SILABS_DBUS_TIMER0_CC1(0x2, 0x0)
#define TIMER0_CC1_PC1   SILABS_DBUS_TIMER0_CC1(0x2, 0x1)
#define TIMER0_CC1_PC2   SILABS_DBUS_TIMER0_CC1(0x2, 0x2)
#define TIMER0_CC1_PC3   SILABS_DBUS_TIMER0_CC1(0x2, 0x3)
#define TIMER0_CC1_PC4   SILABS_DBUS_TIMER0_CC1(0x2, 0x4)
#define TIMER0_CC1_PC5   SILABS_DBUS_TIMER0_CC1(0x2, 0x5)
#define TIMER0_CC1_PD0   SILABS_DBUS_TIMER0_CC1(0x3, 0x0)
#define TIMER0_CC1_PD1   SILABS_DBUS_TIMER0_CC1(0x3, 0x1)
#define TIMER0_CC1_PD2   SILABS_DBUS_TIMER0_CC1(0x3, 0x2)
#define TIMER0_CC1_PD3   SILABS_DBUS_TIMER0_CC1(0x3, 0x3)
#define TIMER0_CC1_PD4   SILABS_DBUS_TIMER0_CC1(0x3, 0x4)
#define TIMER0_CC2_PA0   SILABS_DBUS_TIMER0_CC2(0x0, 0x0)
#define TIMER0_CC2_PA1   SILABS_DBUS_TIMER0_CC2(0x0, 0x1)
#define TIMER0_CC2_PA2   SILABS_DBUS_TIMER0_CC2(0x0, 0x2)
#define TIMER0_CC2_PA3   SILABS_DBUS_TIMER0_CC2(0x0, 0x3)
#define TIMER0_CC2_PA4   SILABS_DBUS_TIMER0_CC2(0x0, 0x4)
#define TIMER0_CC2_PA5   SILABS_DBUS_TIMER0_CC2(0x0, 0x5)
#define TIMER0_CC2_PA6   SILABS_DBUS_TIMER0_CC2(0x0, 0x6)
#define TIMER0_CC2_PB0   SILABS_DBUS_TIMER0_CC2(0x1, 0x0)
#define TIMER0_CC2_PB1   SILABS_DBUS_TIMER0_CC2(0x1, 0x1)
#define TIMER0_CC2_PC0   SILABS_DBUS_TIMER0_CC2(0x2, 0x0)
#define TIMER0_CC2_PC1   SILABS_DBUS_TIMER0_CC2(0x2, 0x1)
#define TIMER0_CC2_PC2   SILABS_DBUS_TIMER0_CC2(0x2, 0x2)
#define TIMER0_CC2_PC3   SILABS_DBUS_TIMER0_CC2(0x2, 0x3)
#define TIMER0_CC2_PC4   SILABS_DBUS_TIMER0_CC2(0x2, 0x4)
#define TIMER0_CC2_PC5   SILABS_DBUS_TIMER0_CC2(0x2, 0x5)
#define TIMER0_CC2_PD0   SILABS_DBUS_TIMER0_CC2(0x3, 0x0)
#define TIMER0_CC2_PD1   SILABS_DBUS_TIMER0_CC2(0x3, 0x1)
#define TIMER0_CC2_PD2   SILABS_DBUS_TIMER0_CC2(0x3, 0x2)
#define TIMER0_CC2_PD3   SILABS_DBUS_TIMER0_CC2(0x3, 0x3)
#define TIMER0_CC2_PD4   SILABS_DBUS_TIMER0_CC2(0x3, 0x4)
#define TIMER0_CDTI0_PA0 SILABS_DBUS_TIMER0_CDTI0(0x0, 0x0)
#define TIMER0_CDTI0_PA1 SILABS_DBUS_TIMER0_CDTI0(0x0, 0x1)
#define TIMER0_CDTI0_PA2 SILABS_DBUS_TIMER0_CDTI0(0x0, 0x2)
#define TIMER0_CDTI0_PA3 SILABS_DBUS_TIMER0_CDTI0(0x0, 0x3)
#define TIMER0_CDTI0_PA4 SILABS_DBUS_TIMER0_CDTI0(0x0, 0x4)
#define TIMER0_CDTI0_PA5 SILABS_DBUS_TIMER0_CDTI0(0x0, 0x5)
#define TIMER0_CDTI0_PA6 SILABS_DBUS_TIMER0_CDTI0(0x0, 0x6)
#define TIMER0_CDTI0_PB0 SILABS_DBUS_TIMER0_CDTI0(0x1, 0x0)
#define TIMER0_CDTI0_PB1 SILABS_DBUS_TIMER0_CDTI0(0x1, 0x1)
#define TIMER0_CDTI0_PC0 SILABS_DBUS_TIMER0_CDTI0(0x2, 0x0)
#define TIMER0_CDTI0_PC1 SILABS_DBUS_TIMER0_CDTI0(0x2, 0x1)
#define TIMER0_CDTI0_PC2 SILABS_DBUS_TIMER0_CDTI0(0x2, 0x2)
#define TIMER0_CDTI0_PC3 SILABS_DBUS_TIMER0_CDTI0(0x2, 0x3)
#define TIMER0_CDTI0_PC4 SILABS_DBUS_TIMER0_CDTI0(0x2, 0x4)
#define TIMER0_CDTI0_PC5 SILABS_DBUS_TIMER0_CDTI0(0x2, 0x5)
#define TIMER0_CDTI0_PD0 SILABS_DBUS_TIMER0_CDTI0(0x3, 0x0)
#define TIMER0_CDTI0_PD1 SILABS_DBUS_TIMER0_CDTI0(0x3, 0x1)
#define TIMER0_CDTI0_PD2 SILABS_DBUS_TIMER0_CDTI0(0x3, 0x2)
#define TIMER0_CDTI0_PD3 SILABS_DBUS_TIMER0_CDTI0(0x3, 0x3)
#define TIMER0_CDTI0_PD4 SILABS_DBUS_TIMER0_CDTI0(0x3, 0x4)
#define TIMER0_CDTI1_PA0 SILABS_DBUS_TIMER0_CDTI1(0x0, 0x0)
#define TIMER0_CDTI1_PA1 SILABS_DBUS_TIMER0_CDTI1(0x0, 0x1)
#define TIMER0_CDTI1_PA2 SILABS_DBUS_TIMER0_CDTI1(0x0, 0x2)
#define TIMER0_CDTI1_PA3 SILABS_DBUS_TIMER0_CDTI1(0x0, 0x3)
#define TIMER0_CDTI1_PA4 SILABS_DBUS_TIMER0_CDTI1(0x0, 0x4)
#define TIMER0_CDTI1_PA5 SILABS_DBUS_TIMER0_CDTI1(0x0, 0x5)
#define TIMER0_CDTI1_PA6 SILABS_DBUS_TIMER0_CDTI1(0x0, 0x6)
#define TIMER0_CDTI1_PB0 SILABS_DBUS_TIMER0_CDTI1(0x1, 0x0)
#define TIMER0_CDTI1_PB1 SILABS_DBUS_TIMER0_CDTI1(0x1, 0x1)
#define TIMER0_CDTI1_PC0 SILABS_DBUS_TIMER0_CDTI1(0x2, 0x0)
#define TIMER0_CDTI1_PC1 SILABS_DBUS_TIMER0_CDTI1(0x2, 0x1)
#define TIMER0_CDTI1_PC2 SILABS_DBUS_TIMER0_CDTI1(0x2, 0x2)
#define TIMER0_CDTI1_PC3 SILABS_DBUS_TIMER0_CDTI1(0x2, 0x3)
#define TIMER0_CDTI1_PC4 SILABS_DBUS_TIMER0_CDTI1(0x2, 0x4)
#define TIMER0_CDTI1_PC5 SILABS_DBUS_TIMER0_CDTI1(0x2, 0x5)
#define TIMER0_CDTI1_PD0 SILABS_DBUS_TIMER0_CDTI1(0x3, 0x0)
#define TIMER0_CDTI1_PD1 SILABS_DBUS_TIMER0_CDTI1(0x3, 0x1)
#define TIMER0_CDTI1_PD2 SILABS_DBUS_TIMER0_CDTI1(0x3, 0x2)
#define TIMER0_CDTI1_PD3 SILABS_DBUS_TIMER0_CDTI1(0x3, 0x3)
#define TIMER0_CDTI1_PD4 SILABS_DBUS_TIMER0_CDTI1(0x3, 0x4)
#define TIMER0_CDTI2_PA0 SILABS_DBUS_TIMER0_CDTI2(0x0, 0x0)
#define TIMER0_CDTI2_PA1 SILABS_DBUS_TIMER0_CDTI2(0x0, 0x1)
#define TIMER0_CDTI2_PA2 SILABS_DBUS_TIMER0_CDTI2(0x0, 0x2)
#define TIMER0_CDTI2_PA3 SILABS_DBUS_TIMER0_CDTI2(0x0, 0x3)
#define TIMER0_CDTI2_PA4 SILABS_DBUS_TIMER0_CDTI2(0x0, 0x4)
#define TIMER0_CDTI2_PA5 SILABS_DBUS_TIMER0_CDTI2(0x0, 0x5)
#define TIMER0_CDTI2_PA6 SILABS_DBUS_TIMER0_CDTI2(0x0, 0x6)
#define TIMER0_CDTI2_PB0 SILABS_DBUS_TIMER0_CDTI2(0x1, 0x0)
#define TIMER0_CDTI2_PB1 SILABS_DBUS_TIMER0_CDTI2(0x1, 0x1)
#define TIMER0_CDTI2_PC0 SILABS_DBUS_TIMER0_CDTI2(0x2, 0x0)
#define TIMER0_CDTI2_PC1 SILABS_DBUS_TIMER0_CDTI2(0x2, 0x1)
#define TIMER0_CDTI2_PC2 SILABS_DBUS_TIMER0_CDTI2(0x2, 0x2)
#define TIMER0_CDTI2_PC3 SILABS_DBUS_TIMER0_CDTI2(0x2, 0x3)
#define TIMER0_CDTI2_PC4 SILABS_DBUS_TIMER0_CDTI2(0x2, 0x4)
#define TIMER0_CDTI2_PC5 SILABS_DBUS_TIMER0_CDTI2(0x2, 0x5)
#define TIMER0_CDTI2_PD0 SILABS_DBUS_TIMER0_CDTI2(0x3, 0x0)
#define TIMER0_CDTI2_PD1 SILABS_DBUS_TIMER0_CDTI2(0x3, 0x1)
#define TIMER0_CDTI2_PD2 SILABS_DBUS_TIMER0_CDTI2(0x3, 0x2)
#define TIMER0_CDTI2_PD3 SILABS_DBUS_TIMER0_CDTI2(0x3, 0x3)
#define TIMER0_CDTI2_PD4 SILABS_DBUS_TIMER0_CDTI2(0x3, 0x4)

#define TIMER1_CC0_PA0   SILABS_DBUS_TIMER1_CC0(0x0, 0x0)
#define TIMER1_CC0_PA1   SILABS_DBUS_TIMER1_CC0(0x0, 0x1)
#define TIMER1_CC0_PA2   SILABS_DBUS_TIMER1_CC0(0x0, 0x2)
#define TIMER1_CC0_PA3   SILABS_DBUS_TIMER1_CC0(0x0, 0x3)
#define TIMER1_CC0_PA4   SILABS_DBUS_TIMER1_CC0(0x0, 0x4)
#define TIMER1_CC0_PA5   SILABS_DBUS_TIMER1_CC0(0x0, 0x5)
#define TIMER1_CC0_PA6   SILABS_DBUS_TIMER1_CC0(0x0, 0x6)
#define TIMER1_CC0_PB0   SILABS_DBUS_TIMER1_CC0(0x1, 0x0)
#define TIMER1_CC0_PB1   SILABS_DBUS_TIMER1_CC0(0x1, 0x1)
#define TIMER1_CC0_PC0   SILABS_DBUS_TIMER1_CC0(0x2, 0x0)
#define TIMER1_CC0_PC1   SILABS_DBUS_TIMER1_CC0(0x2, 0x1)
#define TIMER1_CC0_PC2   SILABS_DBUS_TIMER1_CC0(0x2, 0x2)
#define TIMER1_CC0_PC3   SILABS_DBUS_TIMER1_CC0(0x2, 0x3)
#define TIMER1_CC0_PC4   SILABS_DBUS_TIMER1_CC0(0x2, 0x4)
#define TIMER1_CC0_PC5   SILABS_DBUS_TIMER1_CC0(0x2, 0x5)
#define TIMER1_CC0_PD0   SILABS_DBUS_TIMER1_CC0(0x3, 0x0)
#define TIMER1_CC0_PD1   SILABS_DBUS_TIMER1_CC0(0x3, 0x1)
#define TIMER1_CC0_PD2   SILABS_DBUS_TIMER1_CC0(0x3, 0x2)
#define TIMER1_CC0_PD3   SILABS_DBUS_TIMER1_CC0(0x3, 0x3)
#define TIMER1_CC0_PD4   SILABS_DBUS_TIMER1_CC0(0x3, 0x4)
#define TIMER1_CC1_PA0   SILABS_DBUS_TIMER1_CC1(0x0, 0x0)
#define TIMER1_CC1_PA1   SILABS_DBUS_TIMER1_CC1(0x0, 0x1)
#define TIMER1_CC1_PA2   SILABS_DBUS_TIMER1_CC1(0x0, 0x2)
#define TIMER1_CC1_PA3   SILABS_DBUS_TIMER1_CC1(0x0, 0x3)
#define TIMER1_CC1_PA4   SILABS_DBUS_TIMER1_CC1(0x0, 0x4)
#define TIMER1_CC1_PA5   SILABS_DBUS_TIMER1_CC1(0x0, 0x5)
#define TIMER1_CC1_PA6   SILABS_DBUS_TIMER1_CC1(0x0, 0x6)
#define TIMER1_CC1_PB0   SILABS_DBUS_TIMER1_CC1(0x1, 0x0)
#define TIMER1_CC1_PB1   SILABS_DBUS_TIMER1_CC1(0x1, 0x1)
#define TIMER1_CC1_PC0   SILABS_DBUS_TIMER1_CC1(0x2, 0x0)
#define TIMER1_CC1_PC1   SILABS_DBUS_TIMER1_CC1(0x2, 0x1)
#define TIMER1_CC1_PC2   SILABS_DBUS_TIMER1_CC1(0x2, 0x2)
#define TIMER1_CC1_PC3   SILABS_DBUS_TIMER1_CC1(0x2, 0x3)
#define TIMER1_CC1_PC4   SILABS_DBUS_TIMER1_CC1(0x2, 0x4)
#define TIMER1_CC1_PC5   SILABS_DBUS_TIMER1_CC1(0x2, 0x5)
#define TIMER1_CC1_PD0   SILABS_DBUS_TIMER1_CC1(0x3, 0x0)
#define TIMER1_CC1_PD1   SILABS_DBUS_TIMER1_CC1(0x3, 0x1)
#define TIMER1_CC1_PD2   SILABS_DBUS_TIMER1_CC1(0x3, 0x2)
#define TIMER1_CC1_PD3   SILABS_DBUS_TIMER1_CC1(0x3, 0x3)
#define TIMER1_CC1_PD4   SILABS_DBUS_TIMER1_CC1(0x3, 0x4)
#define TIMER1_CC2_PA0   SILABS_DBUS_TIMER1_CC2(0x0, 0x0)
#define TIMER1_CC2_PA1   SILABS_DBUS_TIMER1_CC2(0x0, 0x1)
#define TIMER1_CC2_PA2   SILABS_DBUS_TIMER1_CC2(0x0, 0x2)
#define TIMER1_CC2_PA3   SILABS_DBUS_TIMER1_CC2(0x0, 0x3)
#define TIMER1_CC2_PA4   SILABS_DBUS_TIMER1_CC2(0x0, 0x4)
#define TIMER1_CC2_PA5   SILABS_DBUS_TIMER1_CC2(0x0, 0x5)
#define TIMER1_CC2_PA6   SILABS_DBUS_TIMER1_CC2(0x0, 0x6)
#define TIMER1_CC2_PB0   SILABS_DBUS_TIMER1_CC2(0x1, 0x0)
#define TIMER1_CC2_PB1   SILABS_DBUS_TIMER1_CC2(0x1, 0x1)
#define TIMER1_CC2_PC0   SILABS_DBUS_TIMER1_CC2(0x2, 0x0)
#define TIMER1_CC2_PC1   SILABS_DBUS_TIMER1_CC2(0x2, 0x1)
#define TIMER1_CC2_PC2   SILABS_DBUS_TIMER1_CC2(0x2, 0x2)
#define TIMER1_CC2_PC3   SILABS_DBUS_TIMER1_CC2(0x2, 0x3)
#define TIMER1_CC2_PC4   SILABS_DBUS_TIMER1_CC2(0x2, 0x4)
#define TIMER1_CC2_PC5   SILABS_DBUS_TIMER1_CC2(0x2, 0x5)
#define TIMER1_CC2_PD0   SILABS_DBUS_TIMER1_CC2(0x3, 0x0)
#define TIMER1_CC2_PD1   SILABS_DBUS_TIMER1_CC2(0x3, 0x1)
#define TIMER1_CC2_PD2   SILABS_DBUS_TIMER1_CC2(0x3, 0x2)
#define TIMER1_CC2_PD3   SILABS_DBUS_TIMER1_CC2(0x3, 0x3)
#define TIMER1_CC2_PD4   SILABS_DBUS_TIMER1_CC2(0x3, 0x4)
#define TIMER1_CDTI0_PA0 SILABS_DBUS_TIMER1_CDTI0(0x0, 0x0)
#define TIMER1_CDTI0_PA1 SILABS_DBUS_TIMER1_CDTI0(0x0, 0x1)
#define TIMER1_CDTI0_PA2 SILABS_DBUS_TIMER1_CDTI0(0x0, 0x2)
#define TIMER1_CDTI0_PA3 SILABS_DBUS_TIMER1_CDTI0(0x0, 0x3)
#define TIMER1_CDTI0_PA4 SILABS_DBUS_TIMER1_CDTI0(0x0, 0x4)
#define TIMER1_CDTI0_PA5 SILABS_DBUS_TIMER1_CDTI0(0x0, 0x5)
#define TIMER1_CDTI0_PA6 SILABS_DBUS_TIMER1_CDTI0(0x0, 0x6)
#define TIMER1_CDTI0_PB0 SILABS_DBUS_TIMER1_CDTI0(0x1, 0x0)
#define TIMER1_CDTI0_PB1 SILABS_DBUS_TIMER1_CDTI0(0x1, 0x1)
#define TIMER1_CDTI0_PC0 SILABS_DBUS_TIMER1_CDTI0(0x2, 0x0)
#define TIMER1_CDTI0_PC1 SILABS_DBUS_TIMER1_CDTI0(0x2, 0x1)
#define TIMER1_CDTI0_PC2 SILABS_DBUS_TIMER1_CDTI0(0x2, 0x2)
#define TIMER1_CDTI0_PC3 SILABS_DBUS_TIMER1_CDTI0(0x2, 0x3)
#define TIMER1_CDTI0_PC4 SILABS_DBUS_TIMER1_CDTI0(0x2, 0x4)
#define TIMER1_CDTI0_PC5 SILABS_DBUS_TIMER1_CDTI0(0x2, 0x5)
#define TIMER1_CDTI0_PD0 SILABS_DBUS_TIMER1_CDTI0(0x3, 0x0)
#define TIMER1_CDTI0_PD1 SILABS_DBUS_TIMER1_CDTI0(0x3, 0x1)
#define TIMER1_CDTI0_PD2 SILABS_DBUS_TIMER1_CDTI0(0x3, 0x2)
#define TIMER1_CDTI0_PD3 SILABS_DBUS_TIMER1_CDTI0(0x3, 0x3)
#define TIMER1_CDTI0_PD4 SILABS_DBUS_TIMER1_CDTI0(0x3, 0x4)
#define TIMER1_CDTI1_PA0 SILABS_DBUS_TIMER1_CDTI1(0x0, 0x0)
#define TIMER1_CDTI1_PA1 SILABS_DBUS_TIMER1_CDTI1(0x0, 0x1)
#define TIMER1_CDTI1_PA2 SILABS_DBUS_TIMER1_CDTI1(0x0, 0x2)
#define TIMER1_CDTI1_PA3 SILABS_DBUS_TIMER1_CDTI1(0x0, 0x3)
#define TIMER1_CDTI1_PA4 SILABS_DBUS_TIMER1_CDTI1(0x0, 0x4)
#define TIMER1_CDTI1_PA5 SILABS_DBUS_TIMER1_CDTI1(0x0, 0x5)
#define TIMER1_CDTI1_PA6 SILABS_DBUS_TIMER1_CDTI1(0x0, 0x6)
#define TIMER1_CDTI1_PB0 SILABS_DBUS_TIMER1_CDTI1(0x1, 0x0)
#define TIMER1_CDTI1_PB1 SILABS_DBUS_TIMER1_CDTI1(0x1, 0x1)
#define TIMER1_CDTI1_PC0 SILABS_DBUS_TIMER1_CDTI1(0x2, 0x0)
#define TIMER1_CDTI1_PC1 SILABS_DBUS_TIMER1_CDTI1(0x2, 0x1)
#define TIMER1_CDTI1_PC2 SILABS_DBUS_TIMER1_CDTI1(0x2, 0x2)
#define TIMER1_CDTI1_PC3 SILABS_DBUS_TIMER1_CDTI1(0x2, 0x3)
#define TIMER1_CDTI1_PC4 SILABS_DBUS_TIMER1_CDTI1(0x2, 0x4)
#define TIMER1_CDTI1_PC5 SILABS_DBUS_TIMER1_CDTI1(0x2, 0x5)
#define TIMER1_CDTI1_PD0 SILABS_DBUS_TIMER1_CDTI1(0x3, 0x0)
#define TIMER1_CDTI1_PD1 SILABS_DBUS_TIMER1_CDTI1(0x3, 0x1)
#define TIMER1_CDTI1_PD2 SILABS_DBUS_TIMER1_CDTI1(0x3, 0x2)
#define TIMER1_CDTI1_PD3 SILABS_DBUS_TIMER1_CDTI1(0x3, 0x3)
#define TIMER1_CDTI1_PD4 SILABS_DBUS_TIMER1_CDTI1(0x3, 0x4)
#define TIMER1_CDTI2_PA0 SILABS_DBUS_TIMER1_CDTI2(0x0, 0x0)
#define TIMER1_CDTI2_PA1 SILABS_DBUS_TIMER1_CDTI2(0x0, 0x1)
#define TIMER1_CDTI2_PA2 SILABS_DBUS_TIMER1_CDTI2(0x0, 0x2)
#define TIMER1_CDTI2_PA3 SILABS_DBUS_TIMER1_CDTI2(0x0, 0x3)
#define TIMER1_CDTI2_PA4 SILABS_DBUS_TIMER1_CDTI2(0x0, 0x4)
#define TIMER1_CDTI2_PA5 SILABS_DBUS_TIMER1_CDTI2(0x0, 0x5)
#define TIMER1_CDTI2_PA6 SILABS_DBUS_TIMER1_CDTI2(0x0, 0x6)
#define TIMER1_CDTI2_PB0 SILABS_DBUS_TIMER1_CDTI2(0x1, 0x0)
#define TIMER1_CDTI2_PB1 SILABS_DBUS_TIMER1_CDTI2(0x1, 0x1)
#define TIMER1_CDTI2_PC0 SILABS_DBUS_TIMER1_CDTI2(0x2, 0x0)
#define TIMER1_CDTI2_PC1 SILABS_DBUS_TIMER1_CDTI2(0x2, 0x1)
#define TIMER1_CDTI2_PC2 SILABS_DBUS_TIMER1_CDTI2(0x2, 0x2)
#define TIMER1_CDTI2_PC3 SILABS_DBUS_TIMER1_CDTI2(0x2, 0x3)
#define TIMER1_CDTI2_PC4 SILABS_DBUS_TIMER1_CDTI2(0x2, 0x4)
#define TIMER1_CDTI2_PC5 SILABS_DBUS_TIMER1_CDTI2(0x2, 0x5)
#define TIMER1_CDTI2_PD0 SILABS_DBUS_TIMER1_CDTI2(0x3, 0x0)
#define TIMER1_CDTI2_PD1 SILABS_DBUS_TIMER1_CDTI2(0x3, 0x1)
#define TIMER1_CDTI2_PD2 SILABS_DBUS_TIMER1_CDTI2(0x3, 0x2)
#define TIMER1_CDTI2_PD3 SILABS_DBUS_TIMER1_CDTI2(0x3, 0x3)
#define TIMER1_CDTI2_PD4 SILABS_DBUS_TIMER1_CDTI2(0x3, 0x4)

#define TIMER2_CC0_PA0   SILABS_DBUS_TIMER2_CC0(0x0, 0x0)
#define TIMER2_CC0_PA1   SILABS_DBUS_TIMER2_CC0(0x0, 0x1)
#define TIMER2_CC0_PA2   SILABS_DBUS_TIMER2_CC0(0x0, 0x2)
#define TIMER2_CC0_PA3   SILABS_DBUS_TIMER2_CC0(0x0, 0x3)
#define TIMER2_CC0_PA4   SILABS_DBUS_TIMER2_CC0(0x0, 0x4)
#define TIMER2_CC0_PA5   SILABS_DBUS_TIMER2_CC0(0x0, 0x5)
#define TIMER2_CC0_PA6   SILABS_DBUS_TIMER2_CC0(0x0, 0x6)
#define TIMER2_CC0_PB0   SILABS_DBUS_TIMER2_CC0(0x1, 0x0)
#define TIMER2_CC0_PB1   SILABS_DBUS_TIMER2_CC0(0x1, 0x1)
#define TIMER2_CC1_PA0   SILABS_DBUS_TIMER2_CC1(0x0, 0x0)
#define TIMER2_CC1_PA1   SILABS_DBUS_TIMER2_CC1(0x0, 0x1)
#define TIMER2_CC1_PA2   SILABS_DBUS_TIMER2_CC1(0x0, 0x2)
#define TIMER2_CC1_PA3   SILABS_DBUS_TIMER2_CC1(0x0, 0x3)
#define TIMER2_CC1_PA4   SILABS_DBUS_TIMER2_CC1(0x0, 0x4)
#define TIMER2_CC1_PA5   SILABS_DBUS_TIMER2_CC1(0x0, 0x5)
#define TIMER2_CC1_PA6   SILABS_DBUS_TIMER2_CC1(0x0, 0x6)
#define TIMER2_CC1_PB0   SILABS_DBUS_TIMER2_CC1(0x1, 0x0)
#define TIMER2_CC1_PB1   SILABS_DBUS_TIMER2_CC1(0x1, 0x1)
#define TIMER2_CC2_PA0   SILABS_DBUS_TIMER2_CC2(0x0, 0x0)
#define TIMER2_CC2_PA1   SILABS_DBUS_TIMER2_CC2(0x0, 0x1)
#define TIMER2_CC2_PA2   SILABS_DBUS_TIMER2_CC2(0x0, 0x2)
#define TIMER2_CC2_PA3   SILABS_DBUS_TIMER2_CC2(0x0, 0x3)
#define TIMER2_CC2_PA4   SILABS_DBUS_TIMER2_CC2(0x0, 0x4)
#define TIMER2_CC2_PA5   SILABS_DBUS_TIMER2_CC2(0x0, 0x5)
#define TIMER2_CC2_PA6   SILABS_DBUS_TIMER2_CC2(0x0, 0x6)
#define TIMER2_CC2_PB0   SILABS_DBUS_TIMER2_CC2(0x1, 0x0)
#define TIMER2_CC2_PB1   SILABS_DBUS_TIMER2_CC2(0x1, 0x1)
#define TIMER2_CDTI0_PA0 SILABS_DBUS_TIMER2_CDTI0(0x0, 0x0)
#define TIMER2_CDTI0_PA1 SILABS_DBUS_TIMER2_CDTI0(0x0, 0x1)
#define TIMER2_CDTI0_PA2 SILABS_DBUS_TIMER2_CDTI0(0x0, 0x2)
#define TIMER2_CDTI0_PA3 SILABS_DBUS_TIMER2_CDTI0(0x0, 0x3)
#define TIMER2_CDTI0_PA4 SILABS_DBUS_TIMER2_CDTI0(0x0, 0x4)
#define TIMER2_CDTI0_PA5 SILABS_DBUS_TIMER2_CDTI0(0x0, 0x5)
#define TIMER2_CDTI0_PA6 SILABS_DBUS_TIMER2_CDTI0(0x0, 0x6)
#define TIMER2_CDTI0_PB0 SILABS_DBUS_TIMER2_CDTI0(0x1, 0x0)
#define TIMER2_CDTI0_PB1 SILABS_DBUS_TIMER2_CDTI0(0x1, 0x1)
#define TIMER2_CDTI1_PA0 SILABS_DBUS_TIMER2_CDTI1(0x0, 0x0)
#define TIMER2_CDTI1_PA1 SILABS_DBUS_TIMER2_CDTI1(0x0, 0x1)
#define TIMER2_CDTI1_PA2 SILABS_DBUS_TIMER2_CDTI1(0x0, 0x2)
#define TIMER2_CDTI1_PA3 SILABS_DBUS_TIMER2_CDTI1(0x0, 0x3)
#define TIMER2_CDTI1_PA4 SILABS_DBUS_TIMER2_CDTI1(0x0, 0x4)
#define TIMER2_CDTI1_PA5 SILABS_DBUS_TIMER2_CDTI1(0x0, 0x5)
#define TIMER2_CDTI1_PA6 SILABS_DBUS_TIMER2_CDTI1(0x0, 0x6)
#define TIMER2_CDTI1_PB0 SILABS_DBUS_TIMER2_CDTI1(0x1, 0x0)
#define TIMER2_CDTI1_PB1 SILABS_DBUS_TIMER2_CDTI1(0x1, 0x1)
#define TIMER2_CDTI2_PA0 SILABS_DBUS_TIMER2_CDTI2(0x0, 0x0)
#define TIMER2_CDTI2_PA1 SILABS_DBUS_TIMER2_CDTI2(0x0, 0x1)
#define TIMER2_CDTI2_PA2 SILABS_DBUS_TIMER2_CDTI2(0x0, 0x2)
#define TIMER2_CDTI2_PA3 SILABS_DBUS_TIMER2_CDTI2(0x0, 0x3)
#define TIMER2_CDTI2_PA4 SILABS_DBUS_TIMER2_CDTI2(0x0, 0x4)
#define TIMER2_CDTI2_PA5 SILABS_DBUS_TIMER2_CDTI2(0x0, 0x5)
#define TIMER2_CDTI2_PA6 SILABS_DBUS_TIMER2_CDTI2(0x0, 0x6)
#define TIMER2_CDTI2_PB0 SILABS_DBUS_TIMER2_CDTI2(0x1, 0x0)
#define TIMER2_CDTI2_PB1 SILABS_DBUS_TIMER2_CDTI2(0x1, 0x1)

#define TIMER3_CC0_PC0   SILABS_DBUS_TIMER3_CC0(0x2, 0x0)
#define TIMER3_CC0_PC1   SILABS_DBUS_TIMER3_CC0(0x2, 0x1)
#define TIMER3_CC0_PC2   SILABS_DBUS_TIMER3_CC0(0x2, 0x2)
#define TIMER3_CC0_PC3   SILABS_DBUS_TIMER3_CC0(0x2, 0x3)
#define TIMER3_CC0_PC4   SILABS_DBUS_TIMER3_CC0(0x2, 0x4)
#define TIMER3_CC0_PC5   SILABS_DBUS_TIMER3_CC0(0x2, 0x5)
#define TIMER3_CC0_PD0   SILABS_DBUS_TIMER3_CC0(0x3, 0x0)
#define TIMER3_CC0_PD1   SILABS_DBUS_TIMER3_CC0(0x3, 0x1)
#define TIMER3_CC0_PD2   SILABS_DBUS_TIMER3_CC0(0x3, 0x2)
#define TIMER3_CC0_PD3   SILABS_DBUS_TIMER3_CC0(0x3, 0x3)
#define TIMER3_CC0_PD4   SILABS_DBUS_TIMER3_CC0(0x3, 0x4)
#define TIMER3_CC1_PC0   SILABS_DBUS_TIMER3_CC1(0x2, 0x0)
#define TIMER3_CC1_PC1   SILABS_DBUS_TIMER3_CC1(0x2, 0x1)
#define TIMER3_CC1_PC2   SILABS_DBUS_TIMER3_CC1(0x2, 0x2)
#define TIMER3_CC1_PC3   SILABS_DBUS_TIMER3_CC1(0x2, 0x3)
#define TIMER3_CC1_PC4   SILABS_DBUS_TIMER3_CC1(0x2, 0x4)
#define TIMER3_CC1_PC5   SILABS_DBUS_TIMER3_CC1(0x2, 0x5)
#define TIMER3_CC1_PD0   SILABS_DBUS_TIMER3_CC1(0x3, 0x0)
#define TIMER3_CC1_PD1   SILABS_DBUS_TIMER3_CC1(0x3, 0x1)
#define TIMER3_CC1_PD2   SILABS_DBUS_TIMER3_CC1(0x3, 0x2)
#define TIMER3_CC1_PD3   SILABS_DBUS_TIMER3_CC1(0x3, 0x3)
#define TIMER3_CC1_PD4   SILABS_DBUS_TIMER3_CC1(0x3, 0x4)
#define TIMER3_CC2_PC0   SILABS_DBUS_TIMER3_CC2(0x2, 0x0)
#define TIMER3_CC2_PC1   SILABS_DBUS_TIMER3_CC2(0x2, 0x1)
#define TIMER3_CC2_PC2   SILABS_DBUS_TIMER3_CC2(0x2, 0x2)
#define TIMER3_CC2_PC3   SILABS_DBUS_TIMER3_CC2(0x2, 0x3)
#define TIMER3_CC2_PC4   SILABS_DBUS_TIMER3_CC2(0x2, 0x4)
#define TIMER3_CC2_PC5   SILABS_DBUS_TIMER3_CC2(0x2, 0x5)
#define TIMER3_CC2_PD0   SILABS_DBUS_TIMER3_CC2(0x3, 0x0)
#define TIMER3_CC2_PD1   SILABS_DBUS_TIMER3_CC2(0x3, 0x1)
#define TIMER3_CC2_PD2   SILABS_DBUS_TIMER3_CC2(0x3, 0x2)
#define TIMER3_CC2_PD3   SILABS_DBUS_TIMER3_CC2(0x3, 0x3)
#define TIMER3_CC2_PD4   SILABS_DBUS_TIMER3_CC2(0x3, 0x4)
#define TIMER3_CDTI0_PC0 SILABS_DBUS_TIMER3_CDTI0(0x2, 0x0)
#define TIMER3_CDTI0_PC1 SILABS_DBUS_TIMER3_CDTI0(0x2, 0x1)
#define TIMER3_CDTI0_PC2 SILABS_DBUS_TIMER3_CDTI0(0x2, 0x2)
#define TIMER3_CDTI0_PC3 SILABS_DBUS_TIMER3_CDTI0(0x2, 0x3)
#define TIMER3_CDTI0_PC4 SILABS_DBUS_TIMER3_CDTI0(0x2, 0x4)
#define TIMER3_CDTI0_PC5 SILABS_DBUS_TIMER3_CDTI0(0x2, 0x5)
#define TIMER3_CDTI0_PD0 SILABS_DBUS_TIMER3_CDTI0(0x3, 0x0)
#define TIMER3_CDTI0_PD1 SILABS_DBUS_TIMER3_CDTI0(0x3, 0x1)
#define TIMER3_CDTI0_PD2 SILABS_DBUS_TIMER3_CDTI0(0x3, 0x2)
#define TIMER3_CDTI0_PD3 SILABS_DBUS_TIMER3_CDTI0(0x3, 0x3)
#define TIMER3_CDTI0_PD4 SILABS_DBUS_TIMER3_CDTI0(0x3, 0x4)
#define TIMER3_CDTI1_PC0 SILABS_DBUS_TIMER3_CDTI1(0x2, 0x0)
#define TIMER3_CDTI1_PC1 SILABS_DBUS_TIMER3_CDTI1(0x2, 0x1)
#define TIMER3_CDTI1_PC2 SILABS_DBUS_TIMER3_CDTI1(0x2, 0x2)
#define TIMER3_CDTI1_PC3 SILABS_DBUS_TIMER3_CDTI1(0x2, 0x3)
#define TIMER3_CDTI1_PC4 SILABS_DBUS_TIMER3_CDTI1(0x2, 0x4)
#define TIMER3_CDTI1_PC5 SILABS_DBUS_TIMER3_CDTI1(0x2, 0x5)
#define TIMER3_CDTI1_PD0 SILABS_DBUS_TIMER3_CDTI1(0x3, 0x0)
#define TIMER3_CDTI1_PD1 SILABS_DBUS_TIMER3_CDTI1(0x3, 0x1)
#define TIMER3_CDTI1_PD2 SILABS_DBUS_TIMER3_CDTI1(0x3, 0x2)
#define TIMER3_CDTI1_PD3 SILABS_DBUS_TIMER3_CDTI1(0x3, 0x3)
#define TIMER3_CDTI1_PD4 SILABS_DBUS_TIMER3_CDTI1(0x3, 0x4)
#define TIMER3_CDTI2_PC0 SILABS_DBUS_TIMER3_CDTI2(0x2, 0x0)
#define TIMER3_CDTI2_PC1 SILABS_DBUS_TIMER3_CDTI2(0x2, 0x1)
#define TIMER3_CDTI2_PC2 SILABS_DBUS_TIMER3_CDTI2(0x2, 0x2)
#define TIMER3_CDTI2_PC3 SILABS_DBUS_TIMER3_CDTI2(0x2, 0x3)
#define TIMER3_CDTI2_PC4 SILABS_DBUS_TIMER3_CDTI2(0x2, 0x4)
#define TIMER3_CDTI2_PC5 SILABS_DBUS_TIMER3_CDTI2(0x2, 0x5)
#define TIMER3_CDTI2_PD0 SILABS_DBUS_TIMER3_CDTI2(0x3, 0x0)
#define TIMER3_CDTI2_PD1 SILABS_DBUS_TIMER3_CDTI2(0x3, 0x1)
#define TIMER3_CDTI2_PD2 SILABS_DBUS_TIMER3_CDTI2(0x3, 0x2)
#define TIMER3_CDTI2_PD3 SILABS_DBUS_TIMER3_CDTI2(0x3, 0x3)
#define TIMER3_CDTI2_PD4 SILABS_DBUS_TIMER3_CDTI2(0x3, 0x4)

#define USART0_CS_PA0  SILABS_DBUS_USART0_CS(0x0, 0x0)
#define USART0_CS_PA1  SILABS_DBUS_USART0_CS(0x0, 0x1)
#define USART0_CS_PA2  SILABS_DBUS_USART0_CS(0x0, 0x2)
#define USART0_CS_PA3  SILABS_DBUS_USART0_CS(0x0, 0x3)
#define USART0_CS_PA4  SILABS_DBUS_USART0_CS(0x0, 0x4)
#define USART0_CS_PA5  SILABS_DBUS_USART0_CS(0x0, 0x5)
#define USART0_CS_PA6  SILABS_DBUS_USART0_CS(0x0, 0x6)
#define USART0_CS_PB0  SILABS_DBUS_USART0_CS(0x1, 0x0)
#define USART0_CS_PB1  SILABS_DBUS_USART0_CS(0x1, 0x1)
#define USART0_CS_PC0  SILABS_DBUS_USART0_CS(0x2, 0x0)
#define USART0_CS_PC1  SILABS_DBUS_USART0_CS(0x2, 0x1)
#define USART0_CS_PC2  SILABS_DBUS_USART0_CS(0x2, 0x2)
#define USART0_CS_PC3  SILABS_DBUS_USART0_CS(0x2, 0x3)
#define USART0_CS_PC4  SILABS_DBUS_USART0_CS(0x2, 0x4)
#define USART0_CS_PC5  SILABS_DBUS_USART0_CS(0x2, 0x5)
#define USART0_CS_PD0  SILABS_DBUS_USART0_CS(0x3, 0x0)
#define USART0_CS_PD1  SILABS_DBUS_USART0_CS(0x3, 0x1)
#define USART0_CS_PD2  SILABS_DBUS_USART0_CS(0x3, 0x2)
#define USART0_CS_PD3  SILABS_DBUS_USART0_CS(0x3, 0x3)
#define USART0_CS_PD4  SILABS_DBUS_USART0_CS(0x3, 0x4)
#define USART0_RTS_PA0 SILABS_DBUS_USART0_RTS(0x0, 0x0)
#define USART0_RTS_PA1 SILABS_DBUS_USART0_RTS(0x0, 0x1)
#define USART0_RTS_PA2 SILABS_DBUS_USART0_RTS(0x0, 0x2)
#define USART0_RTS_PA3 SILABS_DBUS_USART0_RTS(0x0, 0x3)
#define USART0_RTS_PA4 SILABS_DBUS_USART0_RTS(0x0, 0x4)
#define USART0_RTS_PA5 SILABS_DBUS_USART0_RTS(0x0, 0x5)
#define USART0_RTS_PA6 SILABS_DBUS_USART0_RTS(0x0, 0x6)
#define USART0_RTS_PB0 SILABS_DBUS_USART0_RTS(0x1, 0x0)
#define USART0_RTS_PB1 SILABS_DBUS_USART0_RTS(0x1, 0x1)
#define USART0_RTS_PC0 SILABS_DBUS_USART0_RTS(0x2, 0x0)
#define USART0_RTS_PC1 SILABS_DBUS_USART0_RTS(0x2, 0x1)
#define USART0_RTS_PC2 SILABS_DBUS_USART0_RTS(0x2, 0x2)
#define USART0_RTS_PC3 SILABS_DBUS_USART0_RTS(0x2, 0x3)
#define USART0_RTS_PC4 SILABS_DBUS_USART0_RTS(0x2, 0x4)
#define USART0_RTS_PC5 SILABS_DBUS_USART0_RTS(0x2, 0x5)
#define USART0_RTS_PD0 SILABS_DBUS_USART0_RTS(0x3, 0x0)
#define USART0_RTS_PD1 SILABS_DBUS_USART0_RTS(0x3, 0x1)
#define USART0_RTS_PD2 SILABS_DBUS_USART0_RTS(0x3, 0x2)
#define USART0_RTS_PD3 SILABS_DBUS_USART0_RTS(0x3, 0x3)
#define USART0_RTS_PD4 SILABS_DBUS_USART0_RTS(0x3, 0x4)
#define USART0_RX_PA0  SILABS_DBUS_USART0_RX(0x0, 0x0)
#define USART0_RX_PA1  SILABS_DBUS_USART0_RX(0x0, 0x1)
#define USART0_RX_PA2  SILABS_DBUS_USART0_RX(0x0, 0x2)
#define USART0_RX_PA3  SILABS_DBUS_USART0_RX(0x0, 0x3)
#define USART0_RX_PA4  SILABS_DBUS_USART0_RX(0x0, 0x4)
#define USART0_RX_PA5  SILABS_DBUS_USART0_RX(0x0, 0x5)
#define USART0_RX_PA6  SILABS_DBUS_USART0_RX(0x0, 0x6)
#define USART0_RX_PB0  SILABS_DBUS_USART0_RX(0x1, 0x0)
#define USART0_RX_PB1  SILABS_DBUS_USART0_RX(0x1, 0x1)
#define USART0_RX_PC0  SILABS_DBUS_USART0_RX(0x2, 0x0)
#define USART0_RX_PC1  SILABS_DBUS_USART0_RX(0x2, 0x1)
#define USART0_RX_PC2  SILABS_DBUS_USART0_RX(0x2, 0x2)
#define USART0_RX_PC3  SILABS_DBUS_USART0_RX(0x2, 0x3)
#define USART0_RX_PC4  SILABS_DBUS_USART0_RX(0x2, 0x4)
#define USART0_RX_PC5  SILABS_DBUS_USART0_RX(0x2, 0x5)
#define USART0_RX_PD0  SILABS_DBUS_USART0_RX(0x3, 0x0)
#define USART0_RX_PD1  SILABS_DBUS_USART0_RX(0x3, 0x1)
#define USART0_RX_PD2  SILABS_DBUS_USART0_RX(0x3, 0x2)
#define USART0_RX_PD3  SILABS_DBUS_USART0_RX(0x3, 0x3)
#define USART0_RX_PD4  SILABS_DBUS_USART0_RX(0x3, 0x4)
#define USART0_CLK_PA0 SILABS_DBUS_USART0_CLK(0x0, 0x0)
#define USART0_CLK_PA1 SILABS_DBUS_USART0_CLK(0x0, 0x1)
#define USART0_CLK_PA2 SILABS_DBUS_USART0_CLK(0x0, 0x2)
#define USART0_CLK_PA3 SILABS_DBUS_USART0_CLK(0x0, 0x3)
#define USART0_CLK_PA4 SILABS_DBUS_USART0_CLK(0x0, 0x4)
#define USART0_CLK_PA5 SILABS_DBUS_USART0_CLK(0x0, 0x5)
#define USART0_CLK_PA6 SILABS_DBUS_USART0_CLK(0x0, 0x6)
#define USART0_CLK_PB0 SILABS_DBUS_USART0_CLK(0x1, 0x0)
#define USART0_CLK_PB1 SILABS_DBUS_USART0_CLK(0x1, 0x1)
#define USART0_CLK_PC0 SILABS_DBUS_USART0_CLK(0x2, 0x0)
#define USART0_CLK_PC1 SILABS_DBUS_USART0_CLK(0x2, 0x1)
#define USART0_CLK_PC2 SILABS_DBUS_USART0_CLK(0x2, 0x2)
#define USART0_CLK_PC3 SILABS_DBUS_USART0_CLK(0x2, 0x3)
#define USART0_CLK_PC4 SILABS_DBUS_USART0_CLK(0x2, 0x4)
#define USART0_CLK_PC5 SILABS_DBUS_USART0_CLK(0x2, 0x5)
#define USART0_CLK_PD0 SILABS_DBUS_USART0_CLK(0x3, 0x0)
#define USART0_CLK_PD1 SILABS_DBUS_USART0_CLK(0x3, 0x1)
#define USART0_CLK_PD2 SILABS_DBUS_USART0_CLK(0x3, 0x2)
#define USART0_CLK_PD3 SILABS_DBUS_USART0_CLK(0x3, 0x3)
#define USART0_CLK_PD4 SILABS_DBUS_USART0_CLK(0x3, 0x4)
#define USART0_TX_PA0  SILABS_DBUS_USART0_TX(0x0, 0x0)
#define USART0_TX_PA1  SILABS_DBUS_USART0_TX(0x0, 0x1)
#define USART0_TX_PA2  SILABS_DBUS_USART0_TX(0x0, 0x2)
#define USART0_TX_PA3  SILABS_DBUS_USART0_TX(0x0, 0x3)
#define USART0_TX_PA4  SILABS_DBUS_USART0_TX(0x0, 0x4)
#define USART0_TX_PA5  SILABS_DBUS_USART0_TX(0x0, 0x5)
#define USART0_TX_PA6  SILABS_DBUS_USART0_TX(0x0, 0x6)
#define USART0_TX_PB0  SILABS_DBUS_USART0_TX(0x1, 0x0)
#define USART0_TX_PB1  SILABS_DBUS_USART0_TX(0x1, 0x1)
#define USART0_TX_PC0  SILABS_DBUS_USART0_TX(0x2, 0x0)
#define USART0_TX_PC1  SILABS_DBUS_USART0_TX(0x2, 0x1)
#define USART0_TX_PC2  SILABS_DBUS_USART0_TX(0x2, 0x2)
#define USART0_TX_PC3  SILABS_DBUS_USART0_TX(0x2, 0x3)
#define USART0_TX_PC4  SILABS_DBUS_USART0_TX(0x2, 0x4)
#define USART0_TX_PC5  SILABS_DBUS_USART0_TX(0x2, 0x5)
#define USART0_TX_PD0  SILABS_DBUS_USART0_TX(0x3, 0x0)
#define USART0_TX_PD1  SILABS_DBUS_USART0_TX(0x3, 0x1)
#define USART0_TX_PD2  SILABS_DBUS_USART0_TX(0x3, 0x2)
#define USART0_TX_PD3  SILABS_DBUS_USART0_TX(0x3, 0x3)
#define USART0_TX_PD4  SILABS_DBUS_USART0_TX(0x3, 0x4)
#define USART0_CTS_PA0 SILABS_DBUS_USART0_CTS(0x0, 0x0)
#define USART0_CTS_PA1 SILABS_DBUS_USART0_CTS(0x0, 0x1)
#define USART0_CTS_PA2 SILABS_DBUS_USART0_CTS(0x0, 0x2)
#define USART0_CTS_PA3 SILABS_DBUS_USART0_CTS(0x0, 0x3)
#define USART0_CTS_PA4 SILABS_DBUS_USART0_CTS(0x0, 0x4)
#define USART0_CTS_PA5 SILABS_DBUS_USART0_CTS(0x0, 0x5)
#define USART0_CTS_PA6 SILABS_DBUS_USART0_CTS(0x0, 0x6)
#define USART0_CTS_PB0 SILABS_DBUS_USART0_CTS(0x1, 0x0)
#define USART0_CTS_PB1 SILABS_DBUS_USART0_CTS(0x1, 0x1)
#define USART0_CTS_PC0 SILABS_DBUS_USART0_CTS(0x2, 0x0)
#define USART0_CTS_PC1 SILABS_DBUS_USART0_CTS(0x2, 0x1)
#define USART0_CTS_PC2 SILABS_DBUS_USART0_CTS(0x2, 0x2)
#define USART0_CTS_PC3 SILABS_DBUS_USART0_CTS(0x2, 0x3)
#define USART0_CTS_PC4 SILABS_DBUS_USART0_CTS(0x2, 0x4)
#define USART0_CTS_PC5 SILABS_DBUS_USART0_CTS(0x2, 0x5)
#define USART0_CTS_PD0 SILABS_DBUS_USART0_CTS(0x3, 0x0)
#define USART0_CTS_PD1 SILABS_DBUS_USART0_CTS(0x3, 0x1)
#define USART0_CTS_PD2 SILABS_DBUS_USART0_CTS(0x3, 0x2)
#define USART0_CTS_PD3 SILABS_DBUS_USART0_CTS(0x3, 0x3)
#define USART0_CTS_PD4 SILABS_DBUS_USART0_CTS(0x3, 0x4)

#define USART1_CS_PA0  SILABS_DBUS_USART1_CS(0x0, 0x0)
#define USART1_CS_PA1  SILABS_DBUS_USART1_CS(0x0, 0x1)
#define USART1_CS_PA2  SILABS_DBUS_USART1_CS(0x0, 0x2)
#define USART1_CS_PA3  SILABS_DBUS_USART1_CS(0x0, 0x3)
#define USART1_CS_PA4  SILABS_DBUS_USART1_CS(0x0, 0x4)
#define USART1_CS_PA5  SILABS_DBUS_USART1_CS(0x0, 0x5)
#define USART1_CS_PA6  SILABS_DBUS_USART1_CS(0x0, 0x6)
#define USART1_CS_PB0  SILABS_DBUS_USART1_CS(0x1, 0x0)
#define USART1_CS_PB1  SILABS_DBUS_USART1_CS(0x1, 0x1)
#define USART1_RTS_PA0 SILABS_DBUS_USART1_RTS(0x0, 0x0)
#define USART1_RTS_PA1 SILABS_DBUS_USART1_RTS(0x0, 0x1)
#define USART1_RTS_PA2 SILABS_DBUS_USART1_RTS(0x0, 0x2)
#define USART1_RTS_PA3 SILABS_DBUS_USART1_RTS(0x0, 0x3)
#define USART1_RTS_PA4 SILABS_DBUS_USART1_RTS(0x0, 0x4)
#define USART1_RTS_PA5 SILABS_DBUS_USART1_RTS(0x0, 0x5)
#define USART1_RTS_PA6 SILABS_DBUS_USART1_RTS(0x0, 0x6)
#define USART1_RTS_PB0 SILABS_DBUS_USART1_RTS(0x1, 0x0)
#define USART1_RTS_PB1 SILABS_DBUS_USART1_RTS(0x1, 0x1)
#define USART1_RX_PA0  SILABS_DBUS_USART1_RX(0x0, 0x0)
#define USART1_RX_PA1  SILABS_DBUS_USART1_RX(0x0, 0x1)
#define USART1_RX_PA2  SILABS_DBUS_USART1_RX(0x0, 0x2)
#define USART1_RX_PA3  SILABS_DBUS_USART1_RX(0x0, 0x3)
#define USART1_RX_PA4  SILABS_DBUS_USART1_RX(0x0, 0x4)
#define USART1_RX_PA5  SILABS_DBUS_USART1_RX(0x0, 0x5)
#define USART1_RX_PA6  SILABS_DBUS_USART1_RX(0x0, 0x6)
#define USART1_RX_PB0  SILABS_DBUS_USART1_RX(0x1, 0x0)
#define USART1_RX_PB1  SILABS_DBUS_USART1_RX(0x1, 0x1)
#define USART1_CLK_PA0 SILABS_DBUS_USART1_CLK(0x0, 0x0)
#define USART1_CLK_PA1 SILABS_DBUS_USART1_CLK(0x0, 0x1)
#define USART1_CLK_PA2 SILABS_DBUS_USART1_CLK(0x0, 0x2)
#define USART1_CLK_PA3 SILABS_DBUS_USART1_CLK(0x0, 0x3)
#define USART1_CLK_PA4 SILABS_DBUS_USART1_CLK(0x0, 0x4)
#define USART1_CLK_PA5 SILABS_DBUS_USART1_CLK(0x0, 0x5)
#define USART1_CLK_PA6 SILABS_DBUS_USART1_CLK(0x0, 0x6)
#define USART1_CLK_PB0 SILABS_DBUS_USART1_CLK(0x1, 0x0)
#define USART1_CLK_PB1 SILABS_DBUS_USART1_CLK(0x1, 0x1)
#define USART1_TX_PA0  SILABS_DBUS_USART1_TX(0x0, 0x0)
#define USART1_TX_PA1  SILABS_DBUS_USART1_TX(0x0, 0x1)
#define USART1_TX_PA2  SILABS_DBUS_USART1_TX(0x0, 0x2)
#define USART1_TX_PA3  SILABS_DBUS_USART1_TX(0x0, 0x3)
#define USART1_TX_PA4  SILABS_DBUS_USART1_TX(0x0, 0x4)
#define USART1_TX_PA5  SILABS_DBUS_USART1_TX(0x0, 0x5)
#define USART1_TX_PA6  SILABS_DBUS_USART1_TX(0x0, 0x6)
#define USART1_TX_PB0  SILABS_DBUS_USART1_TX(0x1, 0x0)
#define USART1_TX_PB1  SILABS_DBUS_USART1_TX(0x1, 0x1)
#define USART1_CTS_PA0 SILABS_DBUS_USART1_CTS(0x0, 0x0)
#define USART1_CTS_PA1 SILABS_DBUS_USART1_CTS(0x0, 0x1)
#define USART1_CTS_PA2 SILABS_DBUS_USART1_CTS(0x0, 0x2)
#define USART1_CTS_PA3 SILABS_DBUS_USART1_CTS(0x0, 0x3)
#define USART1_CTS_PA4 SILABS_DBUS_USART1_CTS(0x0, 0x4)
#define USART1_CTS_PA5 SILABS_DBUS_USART1_CTS(0x0, 0x5)
#define USART1_CTS_PA6 SILABS_DBUS_USART1_CTS(0x0, 0x6)
#define USART1_CTS_PB0 SILABS_DBUS_USART1_CTS(0x1, 0x0)
#define USART1_CTS_PB1 SILABS_DBUS_USART1_CTS(0x1, 0x1)

#define USART2_CS_PC0  SILABS_DBUS_USART2_CS(0x2, 0x0)
#define USART2_CS_PC1  SILABS_DBUS_USART2_CS(0x2, 0x1)
#define USART2_CS_PC2  SILABS_DBUS_USART2_CS(0x2, 0x2)
#define USART2_CS_PC3  SILABS_DBUS_USART2_CS(0x2, 0x3)
#define USART2_CS_PC4  SILABS_DBUS_USART2_CS(0x2, 0x4)
#define USART2_CS_PC5  SILABS_DBUS_USART2_CS(0x2, 0x5)
#define USART2_CS_PD0  SILABS_DBUS_USART2_CS(0x3, 0x0)
#define USART2_CS_PD1  SILABS_DBUS_USART2_CS(0x3, 0x1)
#define USART2_CS_PD2  SILABS_DBUS_USART2_CS(0x3, 0x2)
#define USART2_CS_PD3  SILABS_DBUS_USART2_CS(0x3, 0x3)
#define USART2_CS_PD4  SILABS_DBUS_USART2_CS(0x3, 0x4)
#define USART2_RTS_PC0 SILABS_DBUS_USART2_RTS(0x2, 0x0)
#define USART2_RTS_PC1 SILABS_DBUS_USART2_RTS(0x2, 0x1)
#define USART2_RTS_PC2 SILABS_DBUS_USART2_RTS(0x2, 0x2)
#define USART2_RTS_PC3 SILABS_DBUS_USART2_RTS(0x2, 0x3)
#define USART2_RTS_PC4 SILABS_DBUS_USART2_RTS(0x2, 0x4)
#define USART2_RTS_PC5 SILABS_DBUS_USART2_RTS(0x2, 0x5)
#define USART2_RTS_PD0 SILABS_DBUS_USART2_RTS(0x3, 0x0)
#define USART2_RTS_PD1 SILABS_DBUS_USART2_RTS(0x3, 0x1)
#define USART2_RTS_PD2 SILABS_DBUS_USART2_RTS(0x3, 0x2)
#define USART2_RTS_PD3 SILABS_DBUS_USART2_RTS(0x3, 0x3)
#define USART2_RTS_PD4 SILABS_DBUS_USART2_RTS(0x3, 0x4)
#define USART2_RX_PC0  SILABS_DBUS_USART2_RX(0x2, 0x0)
#define USART2_RX_PC1  SILABS_DBUS_USART2_RX(0x2, 0x1)
#define USART2_RX_PC2  SILABS_DBUS_USART2_RX(0x2, 0x2)
#define USART2_RX_PC3  SILABS_DBUS_USART2_RX(0x2, 0x3)
#define USART2_RX_PC4  SILABS_DBUS_USART2_RX(0x2, 0x4)
#define USART2_RX_PC5  SILABS_DBUS_USART2_RX(0x2, 0x5)
#define USART2_RX_PD0  SILABS_DBUS_USART2_RX(0x3, 0x0)
#define USART2_RX_PD1  SILABS_DBUS_USART2_RX(0x3, 0x1)
#define USART2_RX_PD2  SILABS_DBUS_USART2_RX(0x3, 0x2)
#define USART2_RX_PD3  SILABS_DBUS_USART2_RX(0x3, 0x3)
#define USART2_RX_PD4  SILABS_DBUS_USART2_RX(0x3, 0x4)
#define USART2_CLK_PC0 SILABS_DBUS_USART2_CLK(0x2, 0x0)
#define USART2_CLK_PC1 SILABS_DBUS_USART2_CLK(0x2, 0x1)
#define USART2_CLK_PC2 SILABS_DBUS_USART2_CLK(0x2, 0x2)
#define USART2_CLK_PC3 SILABS_DBUS_USART2_CLK(0x2, 0x3)
#define USART2_CLK_PC4 SILABS_DBUS_USART2_CLK(0x2, 0x4)
#define USART2_CLK_PC5 SILABS_DBUS_USART2_CLK(0x2, 0x5)
#define USART2_CLK_PD0 SILABS_DBUS_USART2_CLK(0x3, 0x0)
#define USART2_CLK_PD1 SILABS_DBUS_USART2_CLK(0x3, 0x1)
#define USART2_CLK_PD2 SILABS_DBUS_USART2_CLK(0x3, 0x2)
#define USART2_CLK_PD3 SILABS_DBUS_USART2_CLK(0x3, 0x3)
#define USART2_CLK_PD4 SILABS_DBUS_USART2_CLK(0x3, 0x4)
#define USART2_TX_PC0  SILABS_DBUS_USART2_TX(0x2, 0x0)
#define USART2_TX_PC1  SILABS_DBUS_USART2_TX(0x2, 0x1)
#define USART2_TX_PC2  SILABS_DBUS_USART2_TX(0x2, 0x2)
#define USART2_TX_PC3  SILABS_DBUS_USART2_TX(0x2, 0x3)
#define USART2_TX_PC4  SILABS_DBUS_USART2_TX(0x2, 0x4)
#define USART2_TX_PC5  SILABS_DBUS_USART2_TX(0x2, 0x5)
#define USART2_TX_PD0  SILABS_DBUS_USART2_TX(0x3, 0x0)
#define USART2_TX_PD1  SILABS_DBUS_USART2_TX(0x3, 0x1)
#define USART2_TX_PD2  SILABS_DBUS_USART2_TX(0x3, 0x2)
#define USART2_TX_PD3  SILABS_DBUS_USART2_TX(0x3, 0x3)
#define USART2_TX_PD4  SILABS_DBUS_USART2_TX(0x3, 0x4)
#define USART2_CTS_PC0 SILABS_DBUS_USART2_CTS(0x2, 0x0)
#define USART2_CTS_PC1 SILABS_DBUS_USART2_CTS(0x2, 0x1)
#define USART2_CTS_PC2 SILABS_DBUS_USART2_CTS(0x2, 0x2)
#define USART2_CTS_PC3 SILABS_DBUS_USART2_CTS(0x2, 0x3)
#define USART2_CTS_PC4 SILABS_DBUS_USART2_CTS(0x2, 0x4)
#define USART2_CTS_PC5 SILABS_DBUS_USART2_CTS(0x2, 0x5)
#define USART2_CTS_PD0 SILABS_DBUS_USART2_CTS(0x3, 0x0)
#define USART2_CTS_PD1 SILABS_DBUS_USART2_CTS(0x3, 0x1)
#define USART2_CTS_PD2 SILABS_DBUS_USART2_CTS(0x3, 0x2)
#define USART2_CTS_PD3 SILABS_DBUS_USART2_CTS(0x3, 0x3)
#define USART2_CTS_PD4 SILABS_DBUS_USART2_CTS(0x3, 0x4)

#define ABUS_AEVEN0_IADC0  SILABS_ABUS(0x0, 0x0, 0x1)
#define ABUS_AEVEN0_ACMP0  SILABS_ABUS(0x0, 0x0, 0x2)
#define ABUS_AEVEN0_ACMP1  SILABS_ABUS(0x0, 0x0, 0x3)
#define ABUS_AEVEN1_IADC0  SILABS_ABUS(0x0, 0x1, 0x1)
#define ABUS_AEVEN1_ACMP0  SILABS_ABUS(0x0, 0x1, 0x2)
#define ABUS_AEVEN1_ACMP1  SILABS_ABUS(0x0, 0x1, 0x3)
#define ABUS_AODD0_IADC0   SILABS_ABUS(0x0, 0x2, 0x1)
#define ABUS_AODD0_ACMP0   SILABS_ABUS(0x0, 0x2, 0x2)
#define ABUS_AODD0_ACMP1   SILABS_ABUS(0x0, 0x2, 0x3)
#define ABUS_AODD1_IADC0   SILABS_ABUS(0x0, 0x3, 0x1)
#define ABUS_AODD1_ACMP0   SILABS_ABUS(0x0, 0x3, 0x2)
#define ABUS_AODD1_ACMP1   SILABS_ABUS(0x0, 0x3, 0x3)
#define ABUS_BEVEN0_IADC0  SILABS_ABUS(0x1, 0x0, 0x1)
#define ABUS_BEVEN0_ACMP0  SILABS_ABUS(0x1, 0x0, 0x2)
#define ABUS_BEVEN0_ACMP1  SILABS_ABUS(0x1, 0x0, 0x3)
#define ABUS_BEVEN1_IADC0  SILABS_ABUS(0x1, 0x1, 0x1)
#define ABUS_BEVEN1_ACMP0  SILABS_ABUS(0x1, 0x1, 0x2)
#define ABUS_BEVEN1_ACMP1  SILABS_ABUS(0x1, 0x1, 0x3)
#define ABUS_BODD0_IADC0   SILABS_ABUS(0x1, 0x2, 0x1)
#define ABUS_BODD0_ACMP0   SILABS_ABUS(0x1, 0x2, 0x2)
#define ABUS_BODD0_ACMP1   SILABS_ABUS(0x1, 0x2, 0x3)
#define ABUS_BODD1_IADC0   SILABS_ABUS(0x1, 0x3, 0x1)
#define ABUS_BODD1_ACMP0   SILABS_ABUS(0x1, 0x3, 0x2)
#define ABUS_BODD1_ACMP1   SILABS_ABUS(0x1, 0x3, 0x3)
#define ABUS_CDEVEN0_IADC0 SILABS_ABUS(0x2, 0x0, 0x1)
#define ABUS_CDEVEN0_ACMP0 SILABS_ABUS(0x2, 0x0, 0x2)
#define ABUS_CDEVEN0_ACMP1 SILABS_ABUS(0x2, 0x0, 0x3)
#define ABUS_CDEVEN1_IADC0 SILABS_ABUS(0x2, 0x1, 0x1)
#define ABUS_CDEVEN1_ACMP0 SILABS_ABUS(0x2, 0x1, 0x2)
#define ABUS_CDEVEN1_ACMP1 SILABS_ABUS(0x2, 0x1, 0x3)
#define ABUS_CDODD0_IADC0  SILABS_ABUS(0x2, 0x2, 0x1)
#define ABUS_CDODD0_ACMP0  SILABS_ABUS(0x2, 0x2, 0x2)
#define ABUS_CDODD0_ACMP1  SILABS_ABUS(0x2, 0x2, 0x3)
#define ABUS_CDODD1_IADC0  SILABS_ABUS(0x2, 0x3, 0x1)
#define ABUS_CDODD1_ACMP0  SILABS_ABUS(0x2, 0x3, 0x2)
#define ABUS_CDODD1_ACMP1  SILABS_ABUS(0x2, 0x3, 0x3)



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_XG21_PINCTRL_H_ */
```

## 246.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Silicon Laboratories Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

Silicon Labs xG21 设备的引脚控制（Pin Control）。

本文件由 `hal_silabs` 模块中的 `gen_pinctrl.py` 脚本生成。请勿手动编辑。

### 注释 2：原第 1304 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_XG21_PINCTRL_H_`。

## 246.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/xg21-pinctrl_8h.html)
- [zephyr/dt-bindings/pinctrl/silabs-pinctrl-dbus.h](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-dbus_8h.html)
- [silabs-pinctrl-dbus.h](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-dbus_8h.html)

---

[上一章](P245_console.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P247_xg22-pinctrl.h_源码浏览.md)
