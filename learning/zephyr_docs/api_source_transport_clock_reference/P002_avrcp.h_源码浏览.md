---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-2
title: avrcp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_avrcp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h.html)。

## 2.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00037"></a>
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
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00063"></a>
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
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00081"></a>
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
<a id="foldopen00147"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="foldopen00157"></a>
<a id="l00157"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00294"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="foldopen00301"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="foldopen00306"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="foldopen00313"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="foldopen00315"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="foldopen00317"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="foldopen00320"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="foldopen00325"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="foldopen00331"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="foldopen00337"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="foldopen00344"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="foldopen00349"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="foldopen00357"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="foldopen00363"></a>
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
<a id="foldopen00374"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="foldopen00380"></a>
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
<a id="foldopen00392"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="foldopen00401"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="foldopen00408"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="foldopen00414"></a>
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
<a id="foldopen00427"></a>
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
<a id="foldopen00438"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="foldopen00446"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="foldopen00453"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="foldopen00464"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="foldopen00489"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="foldopen00497"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="foldopen00504"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="foldopen00510"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="foldopen00519"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="foldopen00526"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="foldopen00531"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="foldopen00536"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="foldopen00543"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="foldopen00550"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="foldopen00557"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="foldopen00563"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="foldopen00573"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="foldopen00583"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="foldopen00590"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="foldopen00602"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="foldopen00609"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="foldopen00615"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="foldopen00623"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="foldopen00629"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="foldopen00637"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="foldopen00644"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="foldopen00651"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="foldopen00657"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="foldopen00662"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="foldopen00668"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="foldopen00674"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="foldopen00680"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="foldopen00686"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="foldopen00692"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="foldopen00698"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="foldopen00706"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="foldopen00712"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="foldopen00719"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="foldopen00727"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="foldopen00733"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="foldopen00739"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="foldopen00744"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="foldopen00751"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="foldopen00757"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="foldopen00762"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="foldopen00767"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="foldopen00772"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="foldopen00779"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="foldopen00785"></a>
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
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="foldopen00845"></a>
<a id="l00845"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01036"></a>
<a id="l01037"></a>
<a id="l01063"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01086"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01109"></a>
<a id="l01110"></a>
<a id="l01111"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="l01134"></a>
<a id="l01146"></a>
<a id="l01147"></a>
<a id="l01167"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="l01191"></a>
<a id="l01203"></a>
<a id="l01204"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01230"></a>
<a id="l01231"></a>
<a id="l01232"></a>
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01274"></a>
<a id="l01275"></a>
<a id="l01276"></a>
<a id="l01288"></a>
<a id="l01289"></a>
<a id="l01301"></a>
<a id="l01302"></a>
<a id="l01314"></a>
<a id="l01315"></a>
<a id="l01316"></a>
<a id="l01328"></a>
<a id="l01329"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01351"></a>
<a id="l01352"></a>
<a id="l01366"></a>
<a id="l01367"></a>
<a id="l01377"></a>
<a id="l01378"></a>
<a id="l01387"></a>
<a id="l01388"></a>
<a id="l01397"></a>
<a id="l01398"></a>
<a id="l01409"></a>
<a id="l01410"></a>
<a id="l01420"></a>
<a id="l01421"></a>
<a id="l01432"></a>
<a id="l01433"></a>
<a id="l01448"></a>
<a id="l01449"></a>
<a id="l01450"></a>
<a id="l01461"></a>
<a id="l01462"></a>
<a id="l01477"></a>
<a id="l01478"></a>
<a id="l01479"></a>
<a id="l01487"></a>
<a id="l01488"></a>
<a id="l01498"></a>
<a id="l01499"></a>
<a id="l01511"></a>
<a id="l01512"></a>
<a id="l01513"></a>
<a id="l01525"></a>
<a id="l01526"></a>
<a id="l01527"></a>
<a id="l01539"></a>
<a id="l01540"></a>
<a id="l01541"></a>
<a id="l01553"></a>
<a id="l01554"></a>
<a id="l01555"></a>
<a id="l01567"></a>
<a id="l01568"></a>
<a id="l01569"></a>
<a id="l01578"></a>
<a id="l01579"></a>
<a id="l01580"></a>
<a id="l01591"></a>
<a id="l01592"></a>
<a id="l01604"></a>
<a id="l01605"></a>
<a id="l01613"></a>
<a id="l01614"></a>
<a id="l01623"></a>
<a id="l01624"></a>
<a id="l01636"></a>
<a id="l01637"></a>
<a id="l01649"></a>
<a id="l01650"></a>
<a id="l01663"></a>
<a id="l01664"></a>
<a id="l01677"></a>
<a id="l01678"></a>
<a id="l01691"></a>
<a id="l01692"></a>
<a id="l01703"></a>
<a id="l01704"></a>
<a id="l01717"></a>
<a id="l01718"></a>
<a id="foldopen01719"></a>
<a id="l01719"></a>
<a id="l01728"></a>
<a id="l01729"></a>
<a id="l01737"></a>
<a id="l01738"></a>
<a id="l01746"></a>
<a id="l01747"></a>
<a id="l01758"></a>
<a id="l01759"></a>
<a id="l01760"></a>
<a id="l01768"></a>
<a id="l01769"></a>
<a id="l01778"></a>
<a id="l01779"></a>
<a id="l01788"></a>
<a id="l01789"></a>
<a id="l01797"></a>
<a id="l01798"></a>
<a id="l01807"></a>
<a id="l01808"></a>
<a id="l01821"></a>
<a id="l01822"></a>
<a id="l01835"></a>
<a id="l01836"></a>
<a id="l01849"></a>
<a id="l01850"></a>
<a id="l01861"></a>
<a id="l01862"></a>
<a id="l01876"></a>
<a id="l01877"></a>
<a id="l01889"></a>
<a id="l01890"></a>
<a id="l01898"></a>
<a id="l01899"></a>
<a id="l01909"></a>
<a id="l01910"></a>
<a id="l01921"></a>
<a id="l01922"></a>
<a id="l01923"></a>
<a id="l01934"></a>
<a id="l01935"></a>
<a id="l01936"></a>
<a id="l01947"></a>
<a id="l01948"></a>
<a id="l01949"></a>
<a id="l01960"></a>
<a id="l01961"></a>
<a id="l01962"></a>
<a id="l01973"></a>
<a id="l01974"></a>
<a id="l01975"></a>
<a id="l01984"></a>
<a id="l01985"></a>
<a id="l01986"></a>
<a id="l01997"></a>
<a id="l01998"></a>
<a id="l02007"></a>
<a id="l02008"></a>
<a id="l02016"></a>
<a id="l02017"></a>
<a id="l02026"></a>
<a id="l02027"></a>
<a id="l02038"></a>
<a id="l02039"></a>
<a id="l02050"></a>
<a id="l02051"></a>
<a id="l02052"></a>
<a id="l02061"></a>
<a id="l02062"></a>
<a id="l02073"></a>
<a id="l02074"></a>
<a id="l02075"></a>
<a id="l02085"></a>
<a id="l02086"></a>
<a id="l02100"></a>
<a id="l02101"></a>
<a id="l02127"></a>
<a id="l02128"></a>
<a id="l02129"></a>
<a id="l02140"></a>
<a id="l02141"></a>
<a id="l02157"></a>
<a id="l02158"></a>
<a id="l02159"></a>
<a id="l02171"></a>
<a id="l02172"></a>
<a id="l02173"></a>
<a id="l02185"></a>
<a id="l02186"></a>
<a id="l02187"></a>
<a id="l02199"></a>
<a id="l02200"></a>
<a id="l02201"></a>
<a id="l02210"></a>
<a id="l02211"></a>
<a id="l02223"></a>
<a id="l02224"></a>
<a id="l02225"></a>
<a id="l02237"></a>
<a id="l02238"></a>
<a id="l02239"></a>
<a id="l02248"></a>
<a id="l02249"></a>
<a id="l02258"></a>
<a id="l02259"></a>
<a id="l02271"></a>
<a id="l02272"></a>
<a id="l02273"></a>
<a id="l02285"></a>
<a id="l02286"></a>
<a id="l02287"></a>
<a id="l02299"></a>
<a id="l02300"></a>
<a id="l02301"></a>
<a id="l02310"></a>
<a id="l02311"></a>
<a id="l02320"></a>
<a id="l02321"></a>
<a id="l02330"></a>
<a id="l02331"></a>
<a id="l02348"></a>
<a id="l02349"></a>
<a id="l02362"></a>
<a id="l02363"></a>
<a id="l02364"></a>
<a id="l02381"></a>
<a id="l02382"></a>
<a id="l02400"></a>
<a id="l02401"></a>
<a id="l02417"></a>
<a id="l02418"></a>
<a id="l02434"></a>
<a id="l02435"></a>
<a id="l02436"></a>
<a id="l02437"></a>
<a id="l02438"></a>
<a id="l02442"></a>
<a id="l02443"></a>
<a id="agroup__bt__avrcp_html_ga014c353ff7f2fc54eefad6a6e20112ec"></a>
<a id="agroup__bt__avrcp_html_ga02d67e84b4a48ebecf3b307cbd4bb61c"></a>
<a id="agroup__bt__avrcp_html_ga09d191c490efcfb9f8139975090be0d5"></a>
<a id="agroup__bt__avrcp_html_ga0d59de3bbcfd036f267354fa4ee290dd"></a>
<a id="agroup__bt__avrcp_html_ga0ebc5d2657688b70119e11ac20d24592"></a>
<a id="agroup__bt__avrcp_html_ga11f34256317663cec599d7cb1b250243"></a>
<a id="agroup__bt__avrcp_html_ga123f5528b62f48faaf020f19dcc321c1"></a>
<a id="agroup__bt__avrcp_html_ga128458626d5fe6ffbac7cf97867621aa"></a>
<a id="agroup__bt__avrcp_html_ga136fda008bf5d5f7e9cad3855a4173f9"></a>
<a id="agroup__bt__avrcp_html_ga15bf2602f37ef83b3bcefd85920658eb"></a>
<a id="agroup__bt__avrcp_html_ga15f9f868b056f17ea12d96530b7da881"></a>
<a id="agroup__bt__avrcp_html_ga16f8e224bc80ed0bca5ce04a93670320"></a>
<a id="agroup__bt__avrcp_html_ga197fc46b498c5d4f52e4868bb85480b9"></a>
<a id="agroup__bt__avrcp_html_ga1ef0065fd9fa73bcd03491fe700fac65"></a>
<a id="agroup__bt__avrcp_html_ga22bf1b16b383ef473624769ae6ae893a"></a>
<a id="agroup__bt__avrcp_html_ga232182eaa8d04921d85a68e35268212e"></a>
<a id="agroup__bt__avrcp_html_ga27b0a9e2d86fcc91d2e7b19f1bc5df2d"></a>
<a id="agroup__bt__avrcp_html_ga2a4c610e00ba9832f954f30bd6b6618e"></a>
<a id="agroup__bt__avrcp_html_ga311233e84ef1c0fc8c28baacbb77b831"></a>
<a id="agroup__bt__avrcp_html_ga33825b183b12a2b29d5148a7366c0e77"></a>
<a id="agroup__bt__avrcp_html_ga3c997d96028343a0a5a4948dabe19b84"></a>
<a id="agroup__bt__avrcp_html_ga433775fa2758df43ee1d26c78e9122d1"></a>
<a id="agroup__bt__avrcp_html_ga4426612c49f8456f2543f373db72d3f2"></a>
<a id="agroup__bt__avrcp_html_ga4ae38864d35a66a306ced13544e442d4"></a>
<a id="agroup__bt__avrcp_html_ga4ddceec722d768a0f0c86b3701e0e693"></a>
<a id="agroup__bt__avrcp_html_ga4f37f0c696ea98f44bd5e8ce2905d9f4"></a>
<a id="agroup__bt__avrcp_html_ga509746020e487d769f94174a4071b673"></a>
<a id="agroup__bt__avrcp_html_ga52368f4cc655bab75f96da80ddaaabe0"></a>
<a id="agroup__bt__avrcp_html_ga5f72112c0887ed3efc3455ead567126d"></a>
<a id="agroup__bt__avrcp_html_ga6261635bf3925766bb7af10696df6fd5"></a>
<a id="agroup__bt__avrcp_html_ga69561453ade3e8ba07b2122efcddcfad"></a>
<a id="agroup__bt__avrcp_html_ga6a212dd4765adc82eda6e35cd9742f0c"></a>
<a id="agroup__bt__avrcp_html_ga7129d3dc93ea77140ae192099f4a4f92"></a>
<a id="agroup__bt__avrcp_html_ga78ba828636b731b2c43e088a581bfee9"></a>
<a id="agroup__bt__avrcp_html_ga7ba6030ff079e3c47bf6e5838b61ebdb"></a>
<a id="agroup__bt__avrcp_html_ga7e997ce46f322887227623b43e84ff28"></a>
<a id="agroup__bt__avrcp_html_ga7ec468b9a50413ba478186c88728e13b"></a>
<a id="agroup__bt__avrcp_html_ga8047dddc873566ee372e77c6eecd008f"></a>
<a id="agroup__bt__avrcp_html_ga81330413af9eba049da6557b14ae082c"></a>
<a id="agroup__bt__avrcp_html_ga81333eaee7ca1838424ce9b513e6e2c5"></a>
<a id="agroup__bt__avrcp_html_ga851b0c30ac0b382658b5ce040d7755eb"></a>
<a id="agroup__bt__avrcp_html_ga8cc324a60a3480524336bc399d62c1ed"></a>
<a id="agroup__bt__avrcp_html_ga8e6ce46ba46268c2c80f4ec7570859c8"></a>
<a id="agroup__bt__avrcp_html_ga962f7727f10ca2827c60d4d9a5dd2bde"></a>
<a id="agroup__bt__avrcp_html_ga9d471d9a932dfd43b71e894ddec013b4"></a>
<a id="agroup__bt__avrcp_html_gaa00ea2046f2fe87676fe990e0d34de8b"></a>
<a id="agroup__bt__avrcp_html_gaa2aca5a011a99a20a3bd3fd7154a864a"></a>
<a id="agroup__bt__avrcp_html_gaabab9a4f37b3f9653ca95dd4b5944707"></a>
<a id="agroup__bt__avrcp_html_gaad6d011fe84aaa6cec8665aa87d4cc41"></a>
<a id="agroup__bt__avrcp_html_gab0886ea325dddc67167bed86ec6c31e9"></a>
<a id="agroup__bt__avrcp_html_gab18ce4d9348698272eedff52ddb3052e"></a>
<a id="agroup__bt__avrcp_html_gab268d545750bd22b0625779d735d344a"></a>
<a id="agroup__bt__avrcp_html_gab2e6565627deefd8dc5c79a08d02aa85"></a>
<a id="agroup__bt__avrcp_html_gab442ef3962bebd8dbe0d5681498f8453"></a>
<a id="agroup__bt__avrcp_html_gab8730a40ab9bc208a53a035243b8cb1b"></a>
<a id="agroup__bt__avrcp_html_gab8b765fab76ba2585730f328c0abc167"></a>
<a id="agroup__bt__avrcp_html_gab8d46ac46d35b711209f9a8572c1f8bd"></a>
<a id="agroup__bt__avrcp_html_gab9bd888ef5443bd0a3d34a34b972f409"></a>
<a id="agroup__bt__avrcp_html_gaba2d8faec2c3baf7403199ea8a509326"></a>
<a id="agroup__bt__avrcp_html_gabc170c5c0aa39827b4efc43880dbf258"></a>
<a id="agroup__bt__avrcp_html_gac02fed37e267996d4de50b06292d0668"></a>
<a id="agroup__bt__avrcp_html_gac311dc7b5f99162b954271529eeb84ea"></a>
<a id="agroup__bt__avrcp_html_gac3ccb5386c756bc2688ee5d4499aa29b"></a>
<a id="agroup__bt__avrcp_html_gac66d9b3fc6352e66716da3e10b25ccdb"></a>
<a id="agroup__bt__avrcp_html_gac927c7e7c59f6f0e6243ca0887945d5a"></a>
<a id="agroup__bt__avrcp_html_gac92854e7f567f6088a5cf3ad3c209343"></a>
<a id="agroup__bt__avrcp_html_gaccbb023e5051601e27ab1ca193152f7b"></a>
<a id="agroup__bt__avrcp_html_gad0207b2d16d616b628e7bd2dd7fe4e41"></a>
<a id="agroup__bt__avrcp_html_gad0d937d50eccfbedc81cc575a3e238f2"></a>
<a id="agroup__bt__avrcp_html_gad160c86f1647509e10d741284b9bbb03"></a>
<a id="agroup__bt__avrcp_html_gad77454a6d56942ffe57d5b716f7aa39d"></a>
<a id="agroup__bt__avrcp_html_gadcf3f892a1d492a2743cdb4f8d205505"></a>
<a id="agroup__bt__avrcp_html_gadda57eb5c28f6b77bda5efe9286bc5f4"></a>
<a id="agroup__bt__avrcp_html_gadef2624ec50c0bb138d7eae8525784c5"></a>
<a id="agroup__bt__avrcp_html_gadfafc60888e73a92c1d16fe9696565df"></a>
<a id="agroup__bt__avrcp_html_gae4e7573280179717124104858629122a"></a>
<a id="agroup__bt__avrcp_html_gae76f2666d10e6f46a1e5d68327fc7607"></a>
<a id="agroup__bt__avrcp_html_gae8b42aada8be4c9fac13fbd90e751a7b"></a>
<a id="agroup__bt__avrcp_html_gae8cb7f3d8dbb8ae91167916e5c99ec39"></a>
<a id="agroup__bt__avrcp_html_gaecb26512e8b1d267bca0d3ea01438c9b"></a>
<a id="agroup__bt__avrcp_html_gaf521ea00d597fced528d86befd9b5bbb"></a>
<a id="agroup__bt__avrcp_html_gaf55aae17f67a1361279ae208b17e4a75"></a>
<a id="agroup__bt__avrcp_html_gaf5b49460a1037b0f146e7b16d89215e1"></a>
<a id="agroup__bt__avrcp_html_gafc84238ea566bef4d2789e7cdba193dd"></a>
<a id="agroup__bt__avrcp_html_gga02d67e84b4a48ebecf3b307cbd4bb61ca5cbd84478163171359044825050dd172"></a>
<a id="agroup__bt__avrcp_html_gga02d67e84b4a48ebecf3b307cbd4bb61ca8914559b14b7529fc5f1df764036748d"></a>
<a id="agroup__bt__avrcp_html_gga09d191c490efcfb9f8139975090be0d5a06308eb3786579cf5aeb0f19f0ab37ac"></a>
<a id="agroup__bt__avrcp_html_gga09d191c490efcfb9f8139975090be0d5a0a60cb99cd19d203618b1264e2a3cca6"></a>
<a id="agroup__bt__avrcp_html_gga09d191c490efcfb9f8139975090be0d5a0ab0ffb986db900ece2146a347dae06d"></a>
<a id="agroup__bt__avrcp_html_gga09d191c490efcfb9f8139975090be0d5a702f9974cf5d51a77757fd7e1ef4ab0f"></a>
<a id="agroup__bt__avrcp_html_gga09d191c490efcfb9f8139975090be0d5a708dfb5de11ae783b413d2d99202f9b5"></a>
<a id="agroup__bt__avrcp_html_gga09d191c490efcfb9f8139975090be0d5a89aaeb11e807c44479ff47164d99c4f7"></a>
<a id="agroup__bt__avrcp_html_gga09d191c490efcfb9f8139975090be0d5ab33fca5f57f5b80785df367ab788a8fc"></a>
<a id="agroup__bt__avrcp_html_gga0ebc5d2657688b70119e11ac20d24592a0ba1f760a733cd00923970d01bb85293"></a>
<a id="agroup__bt__avrcp_html_gga0ebc5d2657688b70119e11ac20d24592a2b7e8439c8050cdeda97c43d07774001"></a>
<a id="agroup__bt__avrcp_html_gga0ebc5d2657688b70119e11ac20d24592a3dcfd47034d7890e80a05fd4f600f6bf"></a>
<a id="agroup__bt__avrcp_html_gga0ebc5d2657688b70119e11ac20d24592a436c4847edcad7121f7d2ed97169fe61"></a>
<a id="agroup__bt__avrcp_html_gga0ebc5d2657688b70119e11ac20d24592a8fd312d2869f38b6d7446716a30392b1"></a>
<a id="agroup__bt__avrcp_html_gga0ebc5d2657688b70119e11ac20d24592a958ef736372f39d8e180f8fdeb025121"></a>
<a id="agroup__bt__avrcp_html_gga0ebc5d2657688b70119e11ac20d24592ac66e18f0843901209f9004a62ab55624"></a>
<a id="agroup__bt__avrcp_html_gga0ebc5d2657688b70119e11ac20d24592acce73266473e0a14580fa337d2fe53b3"></a>
<a id="agroup__bt__avrcp_html_gga128458626d5fe6ffbac7cf97867621aaa1e1ed998f24038e6095f802144e240c2"></a>
<a id="agroup__bt__avrcp_html_gga128458626d5fe6ffbac7cf97867621aaa4d4a454f0b8a0a84b557a4075eff1215"></a>
<a id="agroup__bt__avrcp_html_gga128458626d5fe6ffbac7cf97867621aaaea875986bd59d1da9650c5d5f2de20a2"></a>
<a id="agroup__bt__avrcp_html_gga15f9f868b056f17ea12d96530b7da881a0eb47ec4ca3d7e0bf613de53d5e50706"></a>
<a id="agroup__bt__avrcp_html_gga15f9f868b056f17ea12d96530b7da881a1465f08940f04a7b35832e6d5f73a4e3"></a>
<a id="agroup__bt__avrcp_html_gga22bf1b16b383ef473624769ae6ae893aa24914c843056b7fc58f534aec1693948"></a>
<a id="agroup__bt__avrcp_html_gga22bf1b16b383ef473624769ae6ae893aa4192bdec6c45e76769ca55ee6a3ab190"></a>
<a id="agroup__bt__avrcp_html_gga22bf1b16b383ef473624769ae6ae893aa926fe6e1fc4fee9bb108c9b0c2e46c9a"></a>
<a id="agroup__bt__avrcp_html_gga22bf1b16b383ef473624769ae6ae893aabf4b962a513c908baa7fac9454511aaa"></a>
<a id="agroup__bt__avrcp_html_gga2a4c610e00ba9832f954f30bd6b6618ea0eefcdda49616cf818efdc0a7b5975f7"></a>
<a id="agroup__bt__avrcp_html_gga2a4c610e00ba9832f954f30bd6b6618ea1a2aa36da42f3751f3a94b218118ae04"></a>
<a id="agroup__bt__avrcp_html_gga2a4c610e00ba9832f954f30bd6b6618ea9a1b0564c98a0637a2ca5a0b97c3e6ce"></a>
<a id="agroup__bt__avrcp_html_gga2a4c610e00ba9832f954f30bd6b6618eac4c9dfbce497d9a043d7ac42ee932bdb"></a>
<a id="agroup__bt__avrcp_html_gga2a4c610e00ba9832f954f30bd6b6618ead58dcc95df3973a7bed94068be913290"></a>
<a id="agroup__bt__avrcp_html_gga33825b183b12a2b29d5148a7366c0e77a2883875f5d5441e7eb7976a38573c178"></a>
<a id="agroup__bt__avrcp_html_gga33825b183b12a2b29d5148a7366c0e77a4f7cb6c1917180ca96b10d2c73df9fad"></a>
<a id="agroup__bt__avrcp_html_gga33825b183b12a2b29d5148a7366c0e77a72880bd811f5cf87fedfa0ff006412b4"></a>
<a id="agroup__bt__avrcp_html_gga33825b183b12a2b29d5148a7366c0e77adafb0292944a3d4236608ca13d900c98"></a>
<a id="agroup__bt__avrcp_html_gga33825b183b12a2b29d5148a7366c0e77aeaba1597c6c1854d46df1eaaff8862a2"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a002efdb93a2dd52bb5bbec05d9537f87"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a0030ffc7149baf83def17e4e2be76f23"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a004689a6684c527035f06fa8d715a09e"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a01fc4e91d59b8c530fe142d2f1c95283"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a029017bcc52cf7c4ffac3db5f92f4e2a"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a07ed4fda3e230d4e95576a25c6d02dcb"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a0d81584ba5cc6bb9c790b87fcf638537"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a0e7877d88781dbacdac095c7d36f186a"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a1380078d446b892a25b8b2d28a405e40"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a1fb2420a2130a9f22f1837c0c3e0896b"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a23d18efccc7b1940e72b62b08fa5ab6c"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a28d5c8b1960aa1e70c0659c40cac32ae"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a300bbf8fe3236a55bfc97e2d7d8323de"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a3078b64d3c759e83d04923ca6bcf079a"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a3e59a9dc846182d2bc26cf2e5960558e"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a470fa709a8a7e35ec12a593ae9dd1574"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a49d2a954862bdf45c30ed734e5a29a62"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a4bba25ed6730766902ecb92e4f546dc8"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a5c37fbe03a5e7b8cda842262f7a504e1"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a5d3a33be8473fc401e3f38a9f234debf"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a61d7145a6aa482256cd8aaad7bb96745"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a6660a000e5bc1d8ead271924a3780366"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a69254767fc4183e1534b12cd6bd88f60"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a6c83aff2115939aa17f6bbd68c792e4f"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a734fa5664a306957cb28eec36806e4ba"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a735b97b85b1183c862955131a09b1eef"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a827d1eaa2f12a37219fc1f78f617d372"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a831592a4b2634815f9716e80252dce63"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a8364f5d44be3b666f5d995368e3dda27"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a8445dd492ab9e6a9b387162f2f7ab779"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a86a61c08b203d0bcc8b8a3ed5090ef7d"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a8b0656fed7b936e131a5c9dbdb32a7a4"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a8fa3d0ac9fc3feefedf3b2d370df748c"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a9030a666a42a54b02b4c7f876f1ae9d2"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a91595d93490cfe27e239c799e927b2b5"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a91a40f7dfb02c38cd7998adf5fe948b5"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a93ffda310d3a0999256b42cd4652e321"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a94ca82a18f2c06379160e69675d927d0"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a9623c492b7a04750fb3938dde65a9358"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84a9ecca98aa1f55ee6a2b6824e0940a7c3"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84aa9d64afb98b2fc91cae3810990451472"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84aac755d13a6f53ead21818a9fb90217ff"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84aae8fe4a27cf2b70bb289f38d4016b9d9"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84ab3a7619c2c3cafe2eab868d471c8066b"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84ac1e3dd409b98c71eaf12567ce5028a98"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84ac751478296cc6a9e5de77fdf3c8fce06"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84acb3f6e1f71628853bb457bfb8163c566"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84acbaded78ac1e41d16464ea9db667c27f"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84ad39e69c55c571eb3c2492d5aa086e586"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84ad6eac39b4aced31534fde97a411b8c4d"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84ae34d68953054ef4446403a1e240e3344"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84ae6046a270ff9f8939059248cddc7a8a2"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84ae6430b447ccd9e15d0ef2ae62152bade"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84ae76461b7c08169ad190a83545b9e584b"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84af1d1ea7e57a0a16c8e6ad8b9961d4459"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84af5f5b89b6f81961f7bf235c91f59b487"></a>
<a id="agroup__bt__avrcp_html_gga3c997d96028343a0a5a4948dabe19b84afc51d7bc6acd64c3dbeb1f10a06113c2"></a>
<a id="agroup__bt__avrcp_html_gga433775fa2758df43ee1d26c78e9122d1a05cd93eef7ee39f8e7111d23131de6de"></a>
<a id="agroup__bt__avrcp_html_gga433775fa2758df43ee1d26c78e9122d1a2509a9b77091db4ff185448d17d44244"></a>
<a id="agroup__bt__avrcp_html_gga433775fa2758df43ee1d26c78e9122d1a5dedf3d49340e3371b118215414aa8d8"></a>
<a id="agroup__bt__avrcp_html_gga433775fa2758df43ee1d26c78e9122d1a71ddb79b742f9acbd5d14a7639a09fe8"></a>
<a id="agroup__bt__avrcp_html_gga433775fa2758df43ee1d26c78e9122d1ab97050ae05ba6cdff052ac6181eed119"></a>
<a id="agroup__bt__avrcp_html_gga433775fa2758df43ee1d26c78e9122d1ae620f45ad0ecb63be8a8a0b446b5817a"></a>
<a id="agroup__bt__avrcp_html_gga4426612c49f8456f2543f373db72d3f2a0819f5ffd937f0d4a379ae5e7b9a2ebf"></a>
<a id="agroup__bt__avrcp_html_gga4426612c49f8456f2543f373db72d3f2abde23c31bbb6ab1c7daf85e3cd977cf9"></a>
<a id="agroup__bt__avrcp_html_gga4426612c49f8456f2543f373db72d3f2ae12700ce9b55f758572b0fbfab18ea90"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a033e10d03bf56df95ec1e888a07cedf9"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a0e77e1782b5a0f88f4d45b6560df2b09"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a14868dd213f59e09dbdb066d5ca39c96"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a14e183c33a64cdac271ee7f320796bd6"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a28925d094d4c3e55b259a55440a5c044"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a2f8ca7c1fe4ba52a1a418612c094158a"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a359810fbbdf875adb89a192deaae6a6d"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a3dfa01e069c517e7e466fa6edcc1c9cb"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a402038758703ee9f8543ad546681a3c5"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a43e59407a44f87d85fa71cdb627524e3"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a448e1c0383e4e4b5fc3c0c80e2040af9"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a4ee781cc845d8b1211217f8338b97023"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a5544c22cad94dadb9eccf47669fabafb"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a5cd415ba8d307dc5153a9a0b2f9958e3"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a6fee8c927f897fff59b7690c3e1732c2"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a7cba04973b3753b50f63e6b0bc205638"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a81094560261826c16be6ebba9d99081c"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a8a767466ac8069e20f6d9e0f30c33420"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0a9f552377c6bb93b3e52b29228a6feaa5"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0aaddaf4f6439aa6a52e3a4fdbb3f0c071"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0ad3a41ce04f27cc349c7466aae18bcee2"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0ae63cf3ffada01f268498151d88c3a3ec"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0af48dcc2c65e4af461c1a6ece622a2f5a"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0af72a55b60fda9c157cdef8b1c6038780"></a>
<a id="agroup__bt__avrcp_html_gga52368f4cc655bab75f96da80ddaaabe0afbff25149bb9c35756dfb7bb6f2516c3"></a>
<a id="agroup__bt__avrcp_html_gga78ba828636b731b2c43e088a581bfee9a6db3104fa9727594b842b4ae9b64a605"></a>
<a id="agroup__bt__avrcp_html_gga78ba828636b731b2c43e088a581bfee9a8be8c211cd26a849c1c89e482aa10030"></a>
<a id="agroup__bt__avrcp_html_gga8047dddc873566ee372e77c6eecd008fa226313d1f90779c47142ba4966ee968f"></a>
<a id="agroup__bt__avrcp_html_gga8047dddc873566ee372e77c6eecd008fa278d43d52aa33cb54705e7d75ddd98b7"></a>
<a id="agroup__bt__avrcp_html_gga8047dddc873566ee372e77c6eecd008fa4157b63056caa15282fab2712a855cec"></a>
<a id="agroup__bt__avrcp_html_gga8047dddc873566ee372e77c6eecd008fa4cfad017fc5870b099a8d4521e422dca"></a>
<a id="agroup__bt__avrcp_html_gga81330413af9eba049da6557b14ae082ca29f70165632222ae40ac3e44554130b0"></a>
<a id="agroup__bt__avrcp_html_gga8e6ce46ba46268c2c80f4ec7570859c8a11a1b2613018ad24861a72313af4189a"></a>
<a id="agroup__bt__avrcp_html_gga8e6ce46ba46268c2c80f4ec7570859c8aac7dce4d43e84c3d80f9eb0791db7a8d"></a>
<a id="agroup__bt__avrcp_html_gga8e6ce46ba46268c2c80f4ec7570859c8ab36d34793768772409794570f740964a"></a>
<a id="agroup__bt__avrcp_html_ggaabab9a4f37b3f9653ca95dd4b5944707a37002574948081d7b42001a62755636b"></a>
<a id="agroup__bt__avrcp_html_ggaabab9a4f37b3f9653ca95dd4b5944707a4db7699a5f22c8d5986f6f1ba7219dac"></a>
<a id="agroup__bt__avrcp_html_ggaabab9a4f37b3f9653ca95dd4b5944707a7a388bb84fbe14f8931ab9bf41b9823d"></a>
<a id="agroup__bt__avrcp_html_ggaabab9a4f37b3f9653ca95dd4b5944707a7baa6442aafc4d00635df52f44d0d608"></a>
<a id="agroup__bt__avrcp_html_ggaba2d8faec2c3baf7403199ea8a509326a1775849a3c303b61975c569cc85e943c"></a>
<a id="agroup__bt__avrcp_html_ggaba2d8faec2c3baf7403199ea8a509326a2c93dc0bfd19305d8012b73001989cd8"></a>
<a id="agroup__bt__avrcp_html_ggaba2d8faec2c3baf7403199ea8a509326a4136d697a8a0ea5daa1a6e89b314b992"></a>
<a id="agroup__bt__avrcp_html_ggaba2d8faec2c3baf7403199ea8a509326a4a2ed58a814be12b93753a6458b15e88"></a>
<a id="agroup__bt__avrcp_html_ggaba2d8faec2c3baf7403199ea8a509326a8a4cfe6ca8f5b92402c029d02b625696"></a>
<a id="agroup__bt__avrcp_html_ggaba2d8faec2c3baf7403199ea8a509326aa49f2871cf4e5f493128f574ad0d6144"></a>
<a id="agroup__bt__avrcp_html_ggaba2d8faec2c3baf7403199ea8a509326ab4b63e5cf84ea34895702ceea5ae81ad"></a>
<a id="agroup__bt__avrcp_html_ggaba2d8faec2c3baf7403199ea8a509326acf6f13da82b371efbcdf03fbedcb6988"></a>
<a id="agroup__bt__avrcp_html_ggac02fed37e267996d4de50b06292d0668aca944e6647d353290b4e5c25fde28bd8"></a>
<a id="agroup__bt__avrcp_html_ggac02fed37e267996d4de50b06292d0668ad8dd8a59776d9d29655cbd083fae6535"></a>
<a id="agroup__bt__avrcp_html_ggac02fed37e267996d4de50b06292d0668aeb7289d0102af72c607d42a8f1c6dfa5"></a>
<a id="agroup__bt__avrcp_html_ggac311dc7b5f99162b954271529eeb84eaa2a7b326aded772c09cf01387145d2802"></a>
<a id="agroup__bt__avrcp_html_ggac311dc7b5f99162b954271529eeb84eaa89fecce56afb09791a2253a7ad840430"></a>
<a id="agroup__bt__avrcp_html_ggac927c7e7c59f6f0e6243ca0887945d5aa76bd7c8c80d6ad9985430148cfd44e82"></a>
<a id="agroup__bt__avrcp_html_ggac927c7e7c59f6f0e6243ca0887945d5aa9847baed2a6d09d4ac81039c7302832b"></a>
<a id="agroup__bt__avrcp_html_ggae76f2666d10e6f46a1e5d68327fc7607a31587fdac3ae979f111287a924115d4a"></a>
<a id="agroup__bt__avrcp_html_ggae76f2666d10e6f46a1e5d68327fc7607aed029088c6bb73d0928ec19b9029e95e"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75a25f8e3e08b5988e833eb0d47452d12a9"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75a412a9b7cbb891bc50fb77c1e6de9faaf"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75a892f2928d634b675426f2fe597a45f6d"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75a8ac593400cda085fbdff36e403bd2a91"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75a8d526498fdcb1380e8e3944da2a5ef85"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75a9ff1d99bc0c83399961ef23d4a75f9b6"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75ab2b2287a0db9be97af8c20298bebba2d"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75ab6fdeacb536067660f754b3c586e073a"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75abd82dd6ba6d5d76cf22a8c703c76c6e0"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75ac0b720defdd8716d757e0c8a7e57db83"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75ae6237555b0051b2395e0bf2287e954c1"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75af4f9e221522cd57461920d22e7a290b9"></a>
<a id="agroup__bt__avrcp_html_ggaf55aae17f67a1361279ae208b17e4a75afc4ef6f8a80a9067ad9dfd30bf2a6958"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__avrcp__add__to__now__playing__cmd_html"></a>
<a id="astructbt__avrcp__add__to__now__playing__cmd_html_a0dd07ff85b7cedcc8b20dfddf3ed5d91"></a>
<a id="astructbt__avrcp__add__to__now__playing__cmd_html_ad73c5b034f7017f05ee3c491bf8bdc10"></a>
<a id="astructbt__avrcp__add__to__now__playing__cmd_html_af0676fbaab14bfd3e3330c3c1ea701c5"></a>
<a id="astructbt__avrcp__app__setting__attr__text_html"></a>
<a id="astructbt__avrcp__app__setting__attr__text_html_a2e3311b3067919aa8feacf24c6a4e37d"></a>
<a id="astructbt__avrcp__app__setting__attr__text_html_a38306c0921d308a9127befe8b14b2780"></a>
<a id="astructbt__avrcp__app__setting__attr__text_html_aa2fc3a684134034a6e34b72d8aed2d94"></a>
<a id="astructbt__avrcp__app__setting__attr__text_html_ac135cdad9f6db11162f11078a5a88f08"></a>
<a id="astructbt__avrcp__app__setting__attr__val_html"></a>
<a id="astructbt__avrcp__app__setting__attr__val_html_a0ca2b498edfaa0199973ece7fcf304bc"></a>
<a id="astructbt__avrcp__app__setting__attr__val_html_ab6c7e9c0cf3097fff571cc93e3b2283b"></a>
<a id="astructbt__avrcp__app__setting__val__text_html"></a>
<a id="astructbt__avrcp__app__setting__val__text_html_a1445e315c485a9486339d183db1c76ad"></a>
<a id="astructbt__avrcp__app__setting__val__text_html_a64c7b1c1fdedea5d8979e2f7b2311446"></a>
<a id="astructbt__avrcp__app__setting__val__text_html_a880d2c79a341c575f05f380fadaade7c"></a>
<a id="astructbt__avrcp__app__setting__val__text_html_af4d28d332712cd8a07b3dc9e6ee2f0d6"></a>
<a id="astructbt__avrcp__change__path__cmd_html"></a>
<a id="astructbt__avrcp__change__path__cmd_html_a026e337b5bcf6f827f32314eabd19832"></a>
<a id="astructbt__avrcp__change__path__cmd_html_a1ced4e12dd7d1c3b31213dce355cf165"></a>
<a id="astructbt__avrcp__change__path__cmd_html_ac575ced16bc5e61043b035b406f732a4"></a>
<a id="astructbt__avrcp__change__path__rsp_html"></a>
<a id="astructbt__avrcp__change__path__rsp_html_a801ddd082bbdbb824943cfd8fd417dea"></a>
<a id="astructbt__avrcp__change__path__rsp_html_ae56d599dc7aade35910b894ad464611a"></a>
<a id="astructbt__avrcp__ct__cb_html"></a>
<a id="astructbt__avrcp__ct__cb_html_a02a9fa26f9827f327b6030758c539210"></a>
<a id="astructbt__avrcp__ct__cb_html_a0c8b90004b116751f94b2c5c1af02af8"></a>
<a id="astructbt__avrcp__ct__cb_html_a0e361f81921ae80e89947e1ede29b66c"></a>
<a id="astructbt__avrcp__ct__cb_html_a134720ca0e05d4e6c893f391ca842344"></a>
<a id="astructbt__avrcp__ct__cb_html_a15e7780c8c5c4037434c2ab20f47a8f6"></a>
<a id="astructbt__avrcp__ct__cb_html_a1b88debebdf19263d760f9f8e3d447d6"></a>
<a id="astructbt__avrcp__ct__cb_html_a2350f1a00f68008b73ca1400f8954b4b"></a>
<a id="astructbt__avrcp__ct__cb_html_a3035cc2cace9a3e8d463d54c72dd1fed"></a>
<a id="astructbt__avrcp__ct__cb_html_a3c37bfd2f03a8c76a725b38210794e21"></a>
<a id="astructbt__avrcp__ct__cb_html_a4b74108af0ab8cb0119af8c477ff9b33"></a>
<a id="astructbt__avrcp__ct__cb_html_a4e33bc54f28204959ccd4fa2c766980d"></a>
<a id="astructbt__avrcp__ct__cb_html_a5990204dc0d6b0437308e69eef8f7f47"></a>
<a id="astructbt__avrcp__ct__cb_html_a6748f42e5ba39a1a6b2d7a50729c0316"></a>
<a id="astructbt__avrcp__ct__cb_html_a69ab87eb920eae066034054e7bf89c7b"></a>
<a id="astructbt__avrcp__ct__cb_html_a768c099504dd24ee67556f69b493ddb0"></a>
<a id="astructbt__avrcp__ct__cb_html_a7ae520df749b156f9875cf3e6ee62a96"></a>
<a id="astructbt__avrcp__ct__cb_html_a80f78ad02b0b7e9db9de19a0dceeea50"></a>
<a id="astructbt__avrcp__ct__cb_html_a81e9799d9efe9133dedd91386e49960c"></a>
<a id="astructbt__avrcp__ct__cb_html_a8b16ac730eb5c9dc95e7c3e660f802cc"></a>
<a id="astructbt__avrcp__ct__cb_html_aae8977ac1f58e40bbf52c1c52e571395"></a>
<a id="astructbt__avrcp__ct__cb_html_ac25d85d11c28d64225b42a6e5f3fa3ce"></a>
<a id="astructbt__avrcp__ct__cb_html_ac41f9cfa20c1b1a092515b345b468a10"></a>
<a id="astructbt__avrcp__ct__cb_html_ac5fd1a8d9927edbd56cb24f8760c8401"></a>
<a id="astructbt__avrcp__ct__cb_html_ac842ad673b8a943e9f1b188346b8d92d"></a>
<a id="astructbt__avrcp__ct__cb_html_accb0eaa7ae05c888b963278fe320c17c"></a>
<a id="astructbt__avrcp__ct__cb_html_ad102ac42003f1013b14809c4dd1057a4"></a>
<a id="astructbt__avrcp__ct__cb_html_ad7b512d997a5326cee867651ad7cbfaf"></a>
<a id="astructbt__avrcp__ct__cb_html_ae5f09e516a212e97c36e0c32074c9477"></a>
<a id="astructbt__avrcp__ct__cb_html_ae92ce375dd6cff3b2b719b39b02e99af"></a>
<a id="astructbt__avrcp__ct__cb_html_afc0ef62c71331961f3196bc2668f4dbb"></a>
<a id="astructbt__avrcp__ct_html"></a>
<a id="astructbt__avrcp__event__data_html"></a>
<a id="astructbt__avrcp__event__data_html_a4aae90303b04cab680045b88a636e22a"></a>
<a id="astructbt__avrcp__event__data_html_a5471d42d0e9a589690304811028931c4"></a>
<a id="astructbt__avrcp__event__data_html_a5eeea0ad88794d23965a83e68c93015f"></a>
<a id="astructbt__avrcp__event__data_html_a77e7bb507e86be528ad40cbae329c7fc"></a>
<a id="astructbt__avrcp__event__data_html_a9c650742790ded89f1a9c583a22b7895"></a>
<a id="astructbt__avrcp__event__data_html_ad23631ca5ca2dd4dd33ba3b76f281c44"></a>
<a id="astructbt__avrcp__event__data_html_adf71db04b3c1821ceafe0e1071af5c38"></a>
<a id="astructbt__avrcp__event__data_html_ae47d1a2379088e929bfb44df7c172511"></a>
<a id="astructbt__avrcp__event__data_html_ae5a21b8f540b69791b65e2ec565c876e"></a>
<a id="astructbt__avrcp__event__data_html_ae7f5a7e755f7dfd6d1d962e9df5ca716"></a>
<a id="astructbt__avrcp__event__data_html_aed5c7ed3f0a1cc935544cf12ee0dcda9"></a>
<a id="astructbt__avrcp__event__data_html_af8aadd59a58de168cba94cdfa22549db"></a>
<a id="astructbt__avrcp__folder__item_html"></a>
<a id="astructbt__avrcp__folder__item_html_a168cb4f00af9685d8b9023b09f5dcbe2"></a>
<a id="astructbt__avrcp__folder__item_html_a682d5d56c49f82e04a812249042353ca"></a>
<a id="astructbt__avrcp__folder__item_html_a8bfa3c0f6854961df4378f0cbe4918e4"></a>
<a id="astructbt__avrcp__folder__item_html_a99a9de89c0d2e7f1b95f80f245e4126c"></a>
<a id="astructbt__avrcp__folder__item_html_ab6cd2f27e38730e3137dd739f4483585"></a>
<a id="astructbt__avrcp__folder__item_html_ab6fa897bd3c15801955592c972220391"></a>
<a id="astructbt__avrcp__folder__item_html_abeb5d94d8a9f91be8769403b6f360991"></a>
<a id="astructbt__avrcp__folder__name_html"></a>
<a id="astructbt__avrcp__folder__name_html_a0c339a18965911d0c3f52af9ae49f5dc"></a>
<a id="astructbt__avrcp__folder__name_html_a54673f0419fa51cee9250e5f5f1487fe"></a>
<a id="astructbt__avrcp__get__caps__rsp_html"></a>
<a id="astructbt__avrcp__get__caps__rsp_html_a1f588c2e4204c2f43c4872ee9d6ff6b1"></a>
<a id="astructbt__avrcp__get__caps__rsp_html_a587d32dcd5abe2e1751a75bcc4bbe5b2"></a>
<a id="astructbt__avrcp__get__caps__rsp_html_a8a4c9b7c09cf3db137431ff788006e87"></a>
<a id="astructbt__avrcp__get__curr__player__app__setting__val__cmd_html"></a>
<a id="astructbt__avrcp__get__curr__player__app__setting__val__cmd_html_a7676edfb915d4468660888f636eb6c4d"></a>
<a id="astructbt__avrcp__get__curr__player__app__setting__val__cmd_html_a76bbe05f5b05beaa4d9ae65efd8a4c5a"></a>
<a id="astructbt__avrcp__get__curr__player__app__setting__val__rsp_html"></a>
<a id="astructbt__avrcp__get__curr__player__app__setting__val__rsp_html_a1b289cd52db9fa5c34b69f6d68b3312d"></a>
<a id="astructbt__avrcp__get__curr__player__app__setting__val__rsp_html_a6b978fe837d5e082729dd5df013d48a6"></a>
<a id="astructbt__avrcp__get__element__attrs__cmd_html"></a>
<a id="astructbt__avrcp__get__element__attrs__cmd_html_a02c96f2e1a1b747a041b663b4532fdc2"></a>
<a id="astructbt__avrcp__get__element__attrs__cmd_html_a1404b06ec564c9ae57f3fc6a920b6407"></a>
<a id="astructbt__avrcp__get__element__attrs__cmd_html_a82826b71e51eb7ccc296c753c9d855f3"></a>
<a id="astructbt__avrcp__get__element__attrs__rsp_html"></a>
<a id="astructbt__avrcp__get__element__attrs__rsp_html_a952a0a601b1dcf69abccaab92ef51eea"></a>
<a id="astructbt__avrcp__get__element__attrs__rsp_html_ae93d33489d91b07a521055032e88b171"></a>
<a id="astructbt__avrcp__get__folder__items__cmd_html"></a>
<a id="astructbt__avrcp__get__folder__items__cmd_html_a7068f5115cf58c075f1deefbb10e4627"></a>
<a id="astructbt__avrcp__get__folder__items__cmd_html_a790f3718f2e6e3d32d1824794a146e4e"></a>
<a id="astructbt__avrcp__get__folder__items__cmd_html_abf2e154d28317043a88ea00475d777a2"></a>
<a id="astructbt__avrcp__get__folder__items__cmd_html_ae362914e3f3be32d6381035176431c88"></a>
<a id="astructbt__avrcp__get__folder__items__cmd_html_af89fb8a745c45a3b768d16d93d5d4287"></a>
<a id="astructbt__avrcp__get__folder__items__rsp_html"></a>
<a id="astructbt__avrcp__get__folder__items__rsp_html_a073136a279ed9b5f2aaf9db8c6f17607"></a>
<a id="astructbt__avrcp__get__folder__items__rsp_html_a0b95f4d78a16bea65f18690f0081e099"></a>
<a id="astructbt__avrcp__get__folder__items__rsp_html_a387d5ed3a962e27632821505fd6f0b03"></a>
<a id="astructbt__avrcp__get__folder__items__rsp_html_a7ef2c44e62e2e35b86db3398a84fa88c"></a>
<a id="astructbt__avrcp__get__item__attrs__cmd_html"></a>
<a id="astructbt__avrcp__get__item__attrs__cmd_html_a350e99496274adbdc452d69c88aa0691"></a>
<a id="astructbt__avrcp__get__item__attrs__cmd_html_a3d111f69d7cd25de618fc36fc2e054cb"></a>
<a id="astructbt__avrcp__get__item__attrs__cmd_html_ab08431ab53f8fec8854d85dd695eeb16"></a>
<a id="astructbt__avrcp__get__item__attrs__cmd_html_ab611ce1a434f4db21899980120c6fc6d"></a>
<a id="astructbt__avrcp__get__item__attrs__cmd_html_aebe4e58e9b48d6145b66eebf01b86632"></a>
<a id="astructbt__avrcp__get__item__attrs__rsp_html"></a>
<a id="astructbt__avrcp__get__item__attrs__rsp_html_a0e20dc5a812fe5901ba04d772c625903"></a>
<a id="astructbt__avrcp__get__item__attrs__rsp_html_a3a9f9dcb6df5de3d0012cd0a33e34a96"></a>
<a id="astructbt__avrcp__get__item__attrs__rsp_html_a8911f071972b08d9c190e365f63496ea"></a>
<a id="astructbt__avrcp__get__play__status__rsp_html"></a>
<a id="astructbt__avrcp__get__play__status__rsp_html_a1a2d2ba12925e8424da262a5d2698beb"></a>
<a id="astructbt__avrcp__get__play__status__rsp_html_a22ca5e4357d8c92cb690995973964b88"></a>
<a id="astructbt__avrcp__get__play__status__rsp_html_a51c7a55875e13bb8ff442d8deef0963c"></a>
<a id="astructbt__avrcp__get__player__app__setting__attr__text__cmd_html"></a>
<a id="astructbt__avrcp__get__player__app__setting__attr__text__cmd_html_a7cec43cbd74ad7f916e76bb63e989eec"></a>
<a id="astructbt__avrcp__get__player__app__setting__attr__text__cmd_html_a8606b94d15d9642f5319ded86ec2eb8c"></a>
<a id="astructbt__avrcp__get__player__app__setting__attr__text__rsp_html"></a>
<a id="astructbt__avrcp__get__player__app__setting__attr__text__rsp_html_a6eab2bcedb9be8e62ab490a20ecabb20"></a>
<a id="astructbt__avrcp__get__player__app__setting__attr__text__rsp_html_a984773df60443fd834e2e381883f4557"></a>
<a id="astructbt__avrcp__get__player__app__setting__val__text__cmd_html"></a>
<a id="astructbt__avrcp__get__player__app__setting__val__text__cmd_html_a6d71fc4760fe6a78ce030c256e1d3326"></a>
<a id="astructbt__avrcp__get__player__app__setting__val__text__cmd_html_acad6d1ebe3ae55fb12d29e38d6183640"></a>
<a id="astructbt__avrcp__get__player__app__setting__val__text__cmd_html_af4b5e65b4a22b36c42d8e545c43ebd7e"></a>
<a id="astructbt__avrcp__get__player__app__setting__val__text__rsp_html"></a>
<a id="astructbt__avrcp__get__player__app__setting__val__text__rsp_html_a45368c39caa9b87ff8101de5801807c3"></a>
<a id="astructbt__avrcp__get__player__app__setting__val__text__rsp_html_a49b1ebb7ebce5ccc9f7d5e77f79f107c"></a>
<a id="astructbt__avrcp__get__total__number__of__items__cmd_html"></a>
<a id="astructbt__avrcp__get__total__number__of__items__cmd_html_a1d6f1eaa83bdaf37a77bffd10f370ca7"></a>
<a id="astructbt__avrcp__get__total__number__of__items__rsp_html"></a>
<a id="astructbt__avrcp__get__total__number__of__items__rsp_html_a6f1686ad482eb271bfcdfaf27a7c5f56"></a>
<a id="astructbt__avrcp__get__total__number__of__items__rsp_html_a7717d866cd7ea275015309b5c8128b2b"></a>
<a id="astructbt__avrcp__get__total__number__of__items__rsp_html_ab1d378b127df00c87593187a8ec25765"></a>
<a id="astructbt__avrcp__inform__batt__status__of__ct__cmd_html"></a>
<a id="astructbt__avrcp__inform__batt__status__of__ct__cmd_html_ae79067d210d7484c18adc3570ec20af1"></a>
<a id="astructbt__avrcp__inform__displayable__char__set__cmd_html"></a>
<a id="astructbt__avrcp__inform__displayable__char__set__cmd_html_a157b2006ac2032335cc75cf14a6b4849"></a>
<a id="astructbt__avrcp__inform__displayable__char__set__cmd_html_a1c283439e475592935395c90b372233f"></a>
<a id="astructbt__avrcp__item__hdr_html"></a>
<a id="astructbt__avrcp__item__hdr_html_ac9327e576791370bcb7b2f7140f99ee4"></a>
<a id="astructbt__avrcp__item__hdr_html_aee91353e20e227cdf095153b101bc69a"></a>
<a id="astructbt__avrcp__list__player__app__setting__attrs__rsp_html"></a>
<a id="astructbt__avrcp__list__player__app__setting__attrs__rsp_html_a2e3313ae520d0d174f8b48589f54e355"></a>
<a id="astructbt__avrcp__list__player__app__setting__attrs__rsp_html_a43432a70ba4acc8e17db8d2effa3c964"></a>
<a id="astructbt__avrcp__list__player__app__setting__vals__cmd_html"></a>
<a id="astructbt__avrcp__list__player__app__setting__vals__cmd_html_ae5dc4c95f535c3ce721c0f3d4d34fecf"></a>
<a id="astructbt__avrcp__list__player__app__setting__vals__rsp_html"></a>
<a id="astructbt__avrcp__list__player__app__setting__vals__rsp_html_a129bdffa4fbd075371ecf6114c614ea5"></a>
<a id="astructbt__avrcp__list__player__app__setting__vals__rsp_html_acf0b62de5a89ea69da09172ca6199535"></a>
<a id="astructbt__avrcp__media__attr_html"></a>
<a id="astructbt__avrcp__media__attr_html_a07ad1a91103fcec7b69d02b7967f1815"></a>
<a id="astructbt__avrcp__media__attr_html_a48e88ae5b4c448e0fad0325891ed82d1"></a>
<a id="astructbt__avrcp__media__attr_html_ae9389f3574be88638cce4e478c532a2b"></a>
<a id="astructbt__avrcp__media__attr_html_af8b744485f601d694fc43ae3e6d8b28a"></a>
<a id="astructbt__avrcp__media__element__item_html"></a>
<a id="astructbt__avrcp__media__element__item_html_a1695ec1cf7ff0b5f379d31f5137c893a"></a>
<a id="astructbt__avrcp__media__element__item_html_a198a755a9f0c6ff88f139ac0911ed54d"></a>
<a id="astructbt__avrcp__media__element__item_html_ac0c12c790e4544eaec7d5766969ff152"></a>
<a id="astructbt__avrcp__media__element__item_html_afe49a107dd657a16336087d2d518f1a7"></a>
<a id="astructbt__avrcp__media__player__item_html"></a>
<a id="astructbt__avrcp__media__player__item_html_a02f71111fc2b4e4f53cd186aaf4372cf"></a>
<a id="astructbt__avrcp__media__player__item_html_a15488d00a442bc3cdfdf44c383bb6738"></a>
<a id="astructbt__avrcp__media__player__item_html_a39c8b80e71c70d4cf84ecb25a03b4f8f"></a>
<a id="astructbt__avrcp__media__player__item_html_a62c18bb03aed36dda87eff9599100dec"></a>
<a id="astructbt__avrcp__media__player__item_html_a9e6f3f5621a76b8ab37c0833916dae69"></a>
<a id="astructbt__avrcp__media__player__item_html_ac8571c557795c5fec5512c7868e34dfc"></a>
<a id="astructbt__avrcp__media__player__item_html_ad3d1c3443f1a4d0b28623e0a3e1a6607"></a>
<a id="astructbt__avrcp__media__player__item_html_aeca27933a1892ac6c6b0951a4bf68370"></a>
<a id="astructbt__avrcp__media__player__item_html_afda406082181582f7fcf4b44d2f6fc8c"></a>
<a id="astructbt__avrcp__passthrough__cmd_html"></a>
<a id="astructbt__avrcp__passthrough__cmd_html_a96b9081498ddac9f8140651b0dfab1ee"></a>
<a id="astructbt__avrcp__passthrough__cmd_html_a9facd7635f3768ac8e5351b6542b7a52"></a>
<a id="astructbt__avrcp__passthrough__cmd_html_aaaa7657a9942d463bbe2647a0a20c0e1"></a>
<a id="astructbt__avrcp__passthrough__opvu__data_html"></a>
<a id="astructbt__avrcp__passthrough__opvu__data_html_a13db1521501ab7c24643b2d1fd6e956a"></a>
<a id="astructbt__avrcp__passthrough__opvu__data_html_a17f6d3c32417102c04502336235f94fa"></a>
<a id="astructbt__avrcp__passthrough__rsp_html"></a>
<a id="astructbt__avrcp__passthrough__rsp_html_a16c0388be437f140c5aaa1364cdfb3fe"></a>
<a id="astructbt__avrcp__passthrough__rsp_html_a735fca5cd5e5d85e987af9748f9d0ab0"></a>
<a id="astructbt__avrcp__passthrough__rsp_html_a91aaa705b91cc9ca0954645a9a43c504"></a>
<a id="astructbt__avrcp__play__item__cmd_html"></a>
<a id="astructbt__avrcp__play__item__cmd_html_a80ca2390bfa44bf2509161f4c6a5421a"></a>
<a id="astructbt__avrcp__play__item__cmd_html_ad2fa5d9e38a3ef5edc4430749ed13515"></a>
<a id="astructbt__avrcp__play__item__cmd_html_aebf33c2d1fa1a2574c485f777f114c0a"></a>
<a id="astructbt__avrcp__play__item__rsp_html"></a>
<a id="astructbt__avrcp__play__item__rsp_html_a36f361a78dbceaac63508fe75ce907b4"></a>
<a id="astructbt__avrcp__register__notification__cmd_html"></a>
<a id="astructbt__avrcp__register__notification__cmd_html_a3bc85acb4c0b45be4fc082890f9fa744"></a>
<a id="astructbt__avrcp__register__notification__cmd_html_a631509c0abadf1f4f2bdf5a5c58f0b80"></a>
<a id="astructbt__avrcp__search__cmd_html"></a>
<a id="astructbt__avrcp__search__cmd_html_a390c55e028e54b1c655d2dc1de35e87c"></a>
<a id="astructbt__avrcp__search__cmd_html_a953e7210d1d0f8ff2cb86e4742a4af7a"></a>
<a id="astructbt__avrcp__search__cmd_html_aa3b1bda62dc37d4c003ea3b3af9567da"></a>
<a id="astructbt__avrcp__search__rsp_html"></a>
<a id="astructbt__avrcp__search__rsp_html_abbaacf359228e5c56e8cf4147dafe258"></a>
<a id="astructbt__avrcp__search__rsp_html_ac1dadb58aa8852476a79799af8b8bd1e"></a>
<a id="astructbt__avrcp__search__rsp_html_ad58679ba2fee9137b3d8c7808b5dfcba"></a>
<a id="astructbt__avrcp__set__absolute__volume__cmd_html"></a>
<a id="astructbt__avrcp__set__absolute__volume__cmd_html_adc69d9de75995fdd1658b38d50566ec4"></a>
<a id="astructbt__avrcp__set__absolute__volume__rsp_html"></a>
<a id="astructbt__avrcp__set__absolute__volume__rsp_html_ae542d562193e9b42e14b04b7a91f1500"></a>
<a id="astructbt__avrcp__set__addressed__player__cmd_html"></a>
<a id="astructbt__avrcp__set__addressed__player__cmd_html_a0cb667cb10375fcd16570fd3fbda20d7"></a>
<a id="astructbt__avrcp__set__browsed__player__rsp_html"></a>
<a id="astructbt__avrcp__set__browsed__player__rsp_html_a5c0a40b5fbcd85dca0b904a106cfede9"></a>
<a id="astructbt__avrcp__set__browsed__player__rsp_html_a61e93ead82b56cb3f61d1337423af05d"></a>
<a id="astructbt__avrcp__set__browsed__player__rsp_html_a7d07c8595a14800385db33662b3096c5"></a>
<a id="astructbt__avrcp__set__browsed__player__rsp_html_a889cfb87961402d8a41b17292ec89b11"></a>
<a id="astructbt__avrcp__set__browsed__player__rsp_html_a995907daaada393c045265583d0bad92"></a>
<a id="astructbt__avrcp__set__browsed__player__rsp_html_a9c7989c84c89790673a0f25922a72f59"></a>
<a id="astructbt__avrcp__set__player__app__setting__val__cmd_html"></a>
<a id="astructbt__avrcp__set__player__app__setting__val__cmd_html_a6eda2876b27b4e137ff80bf0283f96ae"></a>
<a id="astructbt__avrcp__set__player__app__setting__val__cmd_html_a8de91e220969f26121ea08d4e93b11ce"></a>
<a id="astructbt__avrcp__subunit__info__rsp_html"></a>
<a id="astructbt__avrcp__subunit__info__rsp_html_a0be33096e6edf251c23a5322b3c30421"></a>
<a id="astructbt__avrcp__subunit__info__rsp_html_a144ad1d366436c8b2502a17833a36dc3"></a>
<a id="astructbt__avrcp__subunit__info__rsp_html_a47b69412c61682ed336737f34ac614dc"></a>
<a id="astructbt__avrcp__subunit__info__rsp_html_a85cf595920ba2dbf9f0e4deca1d27483"></a>
<a id="astructbt__avrcp__tg__cb_html"></a>
<a id="astructbt__avrcp__tg__cb_html_a0f117772eb0f55e20214b0be8d93a6fa"></a>
<a id="astructbt__avrcp__tg__cb_html_a19308d4734cdd9bf397f7ba721920e97"></a>
<a id="astructbt__avrcp__tg__cb_html_a1ab779d9b5142590f9dcb42990d9d3cb"></a>
<a id="astructbt__avrcp__tg__cb_html_a20215fb3b4bb2d7c73f2d08ac3e801ec"></a>
<a id="astructbt__avrcp__tg__cb_html_a2f022902183a0db38c65a41fdc0a8478"></a>
<a id="astructbt__avrcp__tg__cb_html_a37d8a221b66cf3bad74790532b559cff"></a>
<a id="astructbt__avrcp__tg__cb_html_a4179686bbe4030c44f0a277532dcb96b"></a>
<a id="astructbt__avrcp__tg__cb_html_a45954c3a1f3e8dffb1bc111845c875ce"></a>
<a id="astructbt__avrcp__tg__cb_html_a48b25910cffb470139e2a562b15802ce"></a>
<a id="astructbt__avrcp__tg__cb_html_a51caea0e045788bbce8073f720eb7e19"></a>
<a id="astructbt__avrcp__tg__cb_html_a64bf13cf36066568ecbbe1006c717970"></a>
<a id="astructbt__avrcp__tg__cb_html_a6946e152d68e5650f683ed6a449709d7"></a>
<a id="astructbt__avrcp__tg__cb_html_a82c5ca1100844e5119224aa6bac19bd2"></a>
<a id="astructbt__avrcp__tg__cb_html_a8442f74b35a70c88defe84e948ced8d6"></a>
<a id="astructbt__avrcp__tg__cb_html_a878eaaf2358b0773e964dc68c910a377"></a>
<a id="astructbt__avrcp__tg__cb_html_a883db478d1a35f0fe61f867d78366c91"></a>
<a id="astructbt__avrcp__tg__cb_html_a889d781b5275ca24bf0603c370bb2a4e"></a>
<a id="astructbt__avrcp__tg__cb_html_a8f0994f1b59d16ef74a7430221f53db0"></a>
<a id="astructbt__avrcp__tg__cb_html_a933eb30910fef1e916e60ff21d4255ec"></a>
<a id="astructbt__avrcp__tg__cb_html_a9c64cc44157e6cedec9decc00f0022b3"></a>
<a id="astructbt__avrcp__tg__cb_html_ab3fe452afec12ff31975763c5269c94f"></a>
<a id="astructbt__avrcp__tg__cb_html_ab9f1a086a71522986808f3ebc2cbd2de"></a>
<a id="astructbt__avrcp__tg__cb_html_acd0d716aa960230b3e8f7c5c0bdb9b19"></a>
<a id="astructbt__avrcp__tg__cb_html_ad66a2945e2cb464bf7324a0685106d47"></a>
<a id="astructbt__avrcp__tg__cb_html_ad8701332c6415915d32454788772dd09"></a>
<a id="astructbt__avrcp__tg__cb_html_adf7e869f632ebc1ccbe7d8213a7c4f05"></a>
<a id="astructbt__avrcp__tg__cb_html_ae496f717332ea6a42507e3772793ba0e"></a>
<a id="astructbt__avrcp__tg__cb_html_ae5a45a624cf6d9224aca975260e954c8"></a>
<a id="astructbt__avrcp__tg__cb_html_af07da9dc841518013c6f6a1796f957f1"></a>
<a id="astructbt__avrcp__tg_html"></a>
<a id="astructbt__avrcp__unit__info__rsp_html"></a>
<a id="astructbt__avrcp__unit__info__rsp_html_a0225755bf457bc6d4046d8172af49217"></a>
<a id="astructbt__avrcp__unit__info__rsp_html_a92b869b3200841ea1d10aca41cdd9f77"></a>
<a id="astructbt__conn_html"></a>
<a id="astructmedia__element__item__attr_html"></a>
<a id="astructmedia__element__item__attr_html_a00c0f6e1b42a8b6448574105acb0481d"></a>
<a id="astructmedia__element__item__attr_html_aee96c7d393f086f89e995a96eb95cce9"></a>
<a id="astructmedia__element__item__name_html"></a>
<a id="astructmedia__element__item__name_html_a51866bcc43ed3ed31feb87ac60f97171"></a>
<a id="astructmedia__element__item__name_html_a66b939713a0b4f7aadfbbf65e5b8cef3"></a>
<a id="astructmedia__element__item__name_html_a9ab8705023810277a63566d5b05bc777"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_ac6eef59915e7ce167442fdacbbfb5e56"></a>
<a id="astructnet__buf_html_ae75b7ca728fb7440ea483be8bf88bc38"></a>

```c


/*
 * Copyright (c) 2015-2016 Intel Corporation
 * Copyright (C) 2024 Xiaomi Corporation
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVRCP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVRCP_H_


#ifdef __cplusplus
extern "C" {
#endif

#define BT_AVRCP_COMPANY_ID_SIZE          (3)
#define BT_AVRCP_COMPANY_ID_BLUETOOTH_SIG (0x001958)

typedef enum __packed {
        BT_AVRCP_CAP_COMPANY_ID = 0x2,
        BT_AVRCP_CAP_EVENTS_SUPPORTED = 0x3,
} bt_avrcp_cap_t;

typedef enum __packed {
        BT_AVRCP_EVT_PLAYBACK_STATUS_CHANGED = 0x01,
        BT_AVRCP_EVT_TRACK_CHANGED = 0x02,
        BT_AVRCP_EVT_TRACK_REACHED_END = 0x03,
        BT_AVRCP_EVT_TRACK_REACHED_START = 0x04,
        BT_AVRCP_EVT_PLAYBACK_POS_CHANGED = 0x05,
        BT_AVRCP_EVT_BATT_STATUS_CHANGED = 0x06,
        BT_AVRCP_EVT_SYSTEM_STATUS_CHANGED = 0x07,
        BT_AVRCP_EVT_PLAYER_APP_SETTING_CHANGED = 0x08,
        BT_AVRCP_EVT_NOW_PLAYING_CONTENT_CHANGED = 0x09,
        BT_AVRCP_EVT_AVAILABLE_PLAYERS_CHANGED = 0x0a,
        BT_AVRCP_EVT_ADDRESSED_PLAYER_CHANGED = 0x0b,
        BT_AVRCP_EVT_UIDS_CHANGED = 0x0c,
        BT_AVRCP_EVT_VOLUME_CHANGED = 0x0d,
} bt_avrcp_evt_t;

typedef enum __packed {
        BT_AVRCP_CTYPE_CONTROL = 0x0,
        BT_AVRCP_CTYPE_STATUS = 0x1,
        BT_AVRCP_CTYPE_SPECIFIC_INQUIRY = 0x2,
        BT_AVRCP_CTYPE_NOTIFY = 0x3,
        BT_AVRCP_CTYPE_GENERAL_INQUIRY = 0x4,
} bt_avrcp_ctype_t;

typedef enum __packed {
        BT_AVRCP_RSP_NOT_IMPLEMENTED = 0x8,
        BT_AVRCP_RSP_ACCEPTED = 0x9,
        BT_AVRCP_RSP_REJECTED = 0xa,
        BT_AVRCP_RSP_IN_TRANSITION = 0xb,
        BT_AVRCP_RSP_IMPLEMENTED = 0xc,
        BT_AVRCP_RSP_STABLE = 0xc,
        BT_AVRCP_RSP_CHANGED = 0xd,
        BT_AVRCP_RSP_INTERIM = 0xf,
} bt_avrcp_rsp_t;

typedef enum __packed {
        BT_AVRCP_SUBUNIT_TYPE_PANEL = 0x09,
        BT_AVRCP_SUBUNIT_TYPE_UNIT = 0x1f,
} bt_avrcp_subunit_type_t;

typedef enum __packed {
        BT_AVRCP_OPID_SELECT = 0x00,
        BT_AVRCP_OPID_UP = 0x01,
        BT_AVRCP_OPID_DOWN = 0x02,
        BT_AVRCP_OPID_LEFT = 0x03,
        BT_AVRCP_OPID_RIGHT = 0x04,
        BT_AVRCP_OPID_RIGHT_UP = 0x05,
        BT_AVRCP_OPID_RIGHT_DOWN = 0x06,
        BT_AVRCP_OPID_LEFT_UP = 0x07,
        BT_AVRCP_OPID_LEFT_DOWN = 0x08,
        BT_AVRCP_OPID_ROOT_MENU = 0x09,
        BT_AVRCP_OPID_SETUP_MENU = 0x0a,
        BT_AVRCP_OPID_CONTENTS_MENU = 0x0b,
        BT_AVRCP_OPID_FAVORITE_MENU = 0x0c,
        BT_AVRCP_OPID_EXIT = 0x0d,

        BT_AVRCP_OPID_0 = 0x20,
        BT_AVRCP_OPID_1 = 0x21,
        BT_AVRCP_OPID_2 = 0x22,
        BT_AVRCP_OPID_3 = 0x23,
        BT_AVRCP_OPID_4 = 0x24,
        BT_AVRCP_OPID_5 = 0x25,
        BT_AVRCP_OPID_6 = 0x26,
        BT_AVRCP_OPID_7 = 0x27,
        BT_AVRCP_OPID_8 = 0x28,
        BT_AVRCP_OPID_9 = 0x29,
        BT_AVRCP_OPID_DOT = 0x2a,
        BT_AVRCP_OPID_ENTER = 0x2b,
        BT_AVRCP_OPID_CLEAR = 0x2c,

        BT_AVRCP_OPID_CHANNEL_UP = 0x30,
        BT_AVRCP_OPID_CHANNEL_DOWN = 0x31,
        BT_AVRCP_OPID_PREVIOUS_CHANNEL = 0x32,
        BT_AVRCP_OPID_SOUND_SELECT = 0x33,
        BT_AVRCP_OPID_INPUT_SELECT = 0x34,
        BT_AVRCP_OPID_DISPLAY_INFORMATION = 0x35,
        BT_AVRCP_OPID_HELP = 0x36,
        BT_AVRCP_OPID_PAGE_UP = 0x37,
        BT_AVRCP_OPID_PAGE_DOWN = 0x38,

        BT_AVRCP_OPID_POWER = 0x40,
        BT_AVRCP_OPID_VOLUME_UP = 0x41,
        BT_AVRCP_OPID_VOLUME_DOWN = 0x42,
        BT_AVRCP_OPID_MUTE = 0x43,
        BT_AVRCP_OPID_PLAY = 0x44,
        BT_AVRCP_OPID_STOP = 0x45,
        BT_AVRCP_OPID_PAUSE = 0x46,
        BT_AVRCP_OPID_RECORD = 0x47,
        BT_AVRCP_OPID_REWIND = 0x48,
        BT_AVRCP_OPID_FAST_FORWARD = 0x49,
        BT_AVRCP_OPID_EJECT = 0x4a,
        BT_AVRCP_OPID_FORWARD = 0x4b,
        BT_AVRCP_OPID_BACKWARD = 0x4c,

        BT_AVRCP_OPID_ANGLE = 0x50,
        BT_AVRCP_OPID_SUBPICTURE = 0x51,

        BT_AVRCP_OPID_F1 = 0x71,
        BT_AVRCP_OPID_F2 = 0x72,
        BT_AVRCP_OPID_F3 = 0x73,
        BT_AVRCP_OPID_F4 = 0x74,
        BT_AVRCP_OPID_F5 = 0x75,
        BT_AVRCP_OPID_VENDOR_UNIQUE = 0x7e,
} bt_avrcp_opid_t;

typedef enum __packed {
        BT_AVRCP_BUTTON_PRESSED = 0,
        BT_AVRCP_BUTTON_RELEASED = 1,
} bt_avrcp_button_state_t;

typedef enum __packed {
        BT_AVRCP_STATUS_INVALID_COMMAND = 0x00,

        BT_AVRCP_STATUS_INVALID_PARAMETER = 0x01,

        BT_AVRCP_STATUS_PARAMETER_CONTENT_ERROR = 0x02,

        BT_AVRCP_STATUS_INTERNAL_ERROR = 0x03,

        BT_AVRCP_STATUS_OPERATION_COMPLETED = 0x04,

        BT_AVRCP_STATUS_UID_CHANGED = 0x05,

        BT_AVRCP_STATUS_INVALID_DIRECTION = 0x07,

        BT_AVRCP_STATUS_NOT_A_DIRECTORY = 0x08,

        BT_AVRCP_STATUS_DOES_NOT_EXIST = 0x09,

        BT_AVRCP_STATUS_INVALID_SCOPE = 0x0a,

        BT_AVRCP_STATUS_RANGE_OUT_OF_BOUNDS = 0x0b,

        BT_AVRCP_STATUS_FOLDER_ITEM_IS_NOT_PLAYABLE = 0x0c,

        BT_AVRCP_STATUS_MEDIA_IN_USE = 0x0d,

        BT_AVRCP_STATUS_NOW_PLAYING_LIST_FULL = 0x0e,

        BT_AVRCP_STATUS_SEARCH_NOT_SUPPORTED = 0x0f,

        BT_AVRCP_STATUS_SEARCH_IN_PROGRESS = 0x10,

        BT_AVRCP_STATUS_INVALID_PLAYER_ID = 0x11,

        BT_AVRCP_STATUS_PLAYER_NOT_BROWSABLE = 0x12,

        BT_AVRCP_STATUS_PLAYER_NOT_ADDRESSED = 0x13,

        BT_AVRCP_STATUS_NO_VALID_SEARCH_RESULTS = 0x14,

        BT_AVRCP_STATUS_NO_AVAILABLE_PLAYERS = 0x15,

        BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED = 0x16,

        BT_AVRCP_STATUS_IN_TRANSITION = 0xfd,

        BT_AVRCP_STATUS_NOT_IMPLEMENTED = 0xfe,

        BT_AVRCP_STATUS_SUCCESS = BT_AVRCP_STATUS_OPERATION_COMPLETED,
} bt_avrcp_status_t;

struct bt_avrcp_ct;
struct bt_avrcp_tg;

struct bt_avrcp_unit_info_rsp {
        bt_avrcp_subunit_type_t unit_type;
        uint32_t company_id;
};

struct bt_avrcp_subunit_info_rsp {
        bt_avrcp_subunit_type_t subunit_type;
        uint8_t max_subunit_id;
        const uint8_t *extended_subunit_type;
        const uint8_t *extended_subunit_id;
};

#define BT_AVRCP_PASSTHROUGH_GET_STATE(payload)                                                    \
        ((bt_avrcp_button_state_t)(FIELD_GET(BIT(7), ((payload)->opid_state))))
#define BT_AVRCP_PASSTHROUGH_GET_OPID(payload)                                                     \
        ((bt_avrcp_opid_t)(FIELD_GET(GENMASK(6, 0), ((payload)->opid_state))))
#define BT_AVRCP_PASSTHROUGH_SET_STATE_OPID(payload, state, opid)                                  \
        (payload)->opid_state = FIELD_PREP(BIT(7), state) | FIELD_PREP(GENMASK(6, 0), opid)

struct bt_avrcp_passthrough_opvu_data {
        uint8_t company_id[BT_AVRCP_COMPANY_ID_SIZE];
        uint16_t opid_vu;
} __packed;

struct bt_avrcp_passthrough_cmd {
        uint8_t opid_state;
        uint8_t data_len;
        struct bt_avrcp_passthrough_opvu_data data[0];
} __packed;

struct bt_avrcp_passthrough_rsp {
        uint8_t opid_state;
        uint8_t data_len;
        struct bt_avrcp_passthrough_opvu_data data[0];
} __packed;

struct bt_avrcp_get_caps_rsp {
        uint8_t cap_id;
        uint8_t cap_cnt;
        uint8_t cap[];
} __packed;

typedef enum __packed {
        BT_AVRCP_CHARSET_UTF8 = 0x006a,
} bt_avrcp_charset_t;

typedef enum __packed {
        BT_AVRCP_SCOPE_MEDIA_PLAYER_LIST = 0x00,
        BT_AVRCP_SCOPE_VFS               = 0x01,
        BT_AVRCP_SCOPE_SEARCH            = 0x02,
        BT_AVRCP_SCOPE_NOW_PLAYING       = 0x03,
} bt_avrcp_scope_t;

typedef enum __packed {
        BT_AVRCP_CHANGE_PATH_PARENT = 0x00,
        BT_AVRCP_CHANGE_PATH_CHILD  = 0x01,
} bt_avrcp_change_path_t;

typedef enum __packed {
        BT_AVRCP_FOLDER_TYPE_MIXED     = 0x00,
        BT_AVRCP_FOLDER_TYPE_TITLES    = 0x01,
        BT_AVRCP_FOLDER_TYPE_ALBUMS    = 0x02,
        BT_AVRCP_FOLDER_TYPE_ARTISTS   = 0x03,
        BT_AVRCP_FOLDER_TYPE_GENRES    = 0x04,
        BT_AVRCP_FOLDER_TYPE_PLAYLISTS = 0x05,
        BT_AVRCP_FOLDER_TYPE_YEARS     = 0x06,
} bt_avrcp_folder_type_t;

typedef enum __packed {
        BT_AVRCP_MEDIA_TYPE_AUDIO = 0x00,
        BT_AVRCP_MEDIA_TYPE_VIDEO = 0x01,
} bt_avrcp_media_type_t;

typedef enum __packed {
        BT_AVRCP_MEDIA_ATTR_ID_TITLE = 0x01,
        BT_AVRCP_MEDIA_ATTR_ID_ARTIST = 0x02,
        BT_AVRCP_MEDIA_ATTR_ID_ALBUM = 0x03,
        BT_AVRCP_MEDIA_ATTR_ID_TRACK_NUMBER = 0x04,
        BT_AVRCP_MEDIA_ATTR_ID_TOTAL_TRACKS = 0x05,
        BT_AVRCP_MEDIA_ATTR_ID_GENRE = 0x06,
        BT_AVRCP_MEDIA_ATTR_ID_PLAYING_TIME = 0x07,
        BT_AVRCP_MEDIA_ATTR_ID_DEFAULT_COVER_ART = 0x08,
} bt_avrcp_media_attr_id_t;

struct bt_avrcp_get_folder_items_cmd {
        uint8_t  scope;
        uint32_t start_item;
        uint32_t end_item;
        uint8_t  attr_count;
        uint32_t attr_ids[];
} __packed;

typedef enum __packed {
        BT_AVRCP_ITEM_TYPE_MEDIA_PLAYER  = 0x01,
        BT_AVRCP_ITEM_TYPE_FOLDER        = 0x02,
        BT_AVRCP_ITEM_TYPE_MEDIA_ELEMENT = 0x03,
} bt_avrcp_item_type_t;

struct bt_avrcp_item_hdr {
        uint8_t  item_type;
        uint16_t item_len;
} __packed;

struct bt_avrcp_media_player_item {
        struct bt_avrcp_item_hdr hdr;
        uint16_t player_id;
        uint8_t  major_type;
        uint32_t player_subtype;
        uint8_t  play_status;
        uint8_t  feature_bitmask[16];
        uint16_t charset_id;
        uint16_t name_len;
        uint8_t  name[];
} __packed;

struct bt_avrcp_folder_item {
        struct bt_avrcp_item_hdr hdr;
        uint8_t uid[8];
        uint8_t  folder_type;
        uint8_t  playable;
        uint16_t charset_id;
        uint16_t name_len;
        uint8_t  name[];
} __packed;

struct bt_avrcp_media_attr {
        uint32_t attr_id;
        uint16_t charset_id;
        uint16_t attr_len;
        uint8_t attr_val[];
} __packed;

struct media_element_item_name {
        uint16_t charset_id;
        uint16_t name_len;
        uint8_t  name[];
} __packed;

struct media_element_item_attr {
        uint8_t  num_attrs;
        struct bt_avrcp_media_attr attrs[];
} __packed;

struct bt_avrcp_media_element_item {
        struct bt_avrcp_item_hdr hdr;
        uint8_t  uid[8];
        uint8_t  media_type;
        uint8_t  data[];
} __packed;

struct bt_avrcp_get_folder_items_rsp {
        uint8_t  status;
        uint16_t uid_counter;
        uint16_t num_items;
        uint8_t  items[];
} __packed;

struct bt_avrcp_change_path_cmd {
        uint16_t uid_counter;
        uint8_t  direction;
        uint8_t folder_uid[8];
} __packed;

struct bt_avrcp_change_path_rsp {
        uint8_t  status;
        uint32_t num_items;
} __packed;

struct bt_avrcp_get_item_attrs_cmd {
        uint8_t  scope;
        uint8_t uid[8];
        uint16_t uid_counter;
        uint8_t  num_attrs;
        uint32_t attr_ids[];
} __packed;

struct bt_avrcp_get_item_attrs_rsp {
        uint8_t  status;
        uint8_t  num_attrs;
        struct bt_avrcp_media_attr attrs[];
} __packed;

struct bt_avrcp_play_item_rsp {
        uint8_t status;
} __packed;

struct bt_avrcp_get_total_number_of_items_cmd {
        uint8_t scope;
} __packed;

struct bt_avrcp_get_total_number_of_items_rsp {
        uint8_t  status;
        uint16_t uid_counter;
        uint32_t num_items;
} __packed;

struct bt_avrcp_search_cmd {
        uint16_t charset_id;
        uint16_t search_str_len;
        uint8_t  search_str[];
} __packed;

struct bt_avrcp_search_rsp {
        uint8_t  status;
        uint16_t uid_counter;
        uint32_t num_items;
} __packed;

struct bt_avrcp_folder_name {
        uint16_t folder_name_len;
        uint8_t folder_name[];
} __packed;

struct bt_avrcp_set_browsed_player_rsp {
        uint8_t status;
        uint16_t uid_counter;
        uint32_t num_items;
        uint16_t charset_id;
        uint8_t folder_depth;
        struct bt_avrcp_folder_name folder_names[0];
} __packed;

typedef enum __packed {
        BT_AVRCP_PLAYBACK_STATUS_STOPPED  = 0x00,
        BT_AVRCP_PLAYBACK_STATUS_PLAYING  = 0x01,
        BT_AVRCP_PLAYBACK_STATUS_PAUSED   = 0x02,
        BT_AVRCP_PLAYBACK_STATUS_FWD_SEEK = 0x03,
        BT_AVRCP_PLAYBACK_STATUS_REV_SEEK = 0x04,
        BT_AVRCP_PLAYBACK_STATUS_ERROR    = 0xff,
} bt_avrcp_playback_status_t;

typedef enum __packed {
        BT_AVRCP_SYSTEM_STATUS_POWER_ON  = 0x00,
        BT_AVRCP_SYSTEM_STATUS_POWER_OFF = 0x01,
        BT_AVRCP_SYSTEM_STATUS_UNPLUGGED = 0x02,
} bt_avrcp_system_status_t;

typedef enum __packed {
        BT_AVRCP_BATTERY_STATUS_NORMAL   = 0x00,
        BT_AVRCP_BATTERY_STATUS_WARNING  = 0x01,
        BT_AVRCP_BATTERY_STATUS_CRITICAL = 0x02,
        BT_AVRCP_BATTERY_STATUS_EXTERNAL = 0x03,
        BT_AVRCP_BATTERY_STATUS_FULL     = 0x04,
} bt_avrcp_battery_status_t;

#define BT_AVRCP_MAX_ABSOLUTE_VOLUME 0x7F

struct bt_avrcp_get_element_attrs_cmd {
        uint8_t identifier[8];
        uint8_t num_attrs;
        uint32_t attr_ids[];
} __packed;

struct bt_avrcp_get_element_attrs_rsp {
        uint8_t num_attrs;
        struct bt_avrcp_media_attr attrs[];
} __packed;

typedef enum __packed {
        BT_AVRCP_PLAYER_ATTR_EQUALIZER = 0x01,
        BT_AVRCP_PLAYER_ATTR_REPEAT_MODE = 0x02,
        BT_AVRCP_PLAYER_ATTR_SHUFFLE = 0x03,
        BT_AVRCP_PLAYER_ATTR_SCAN = 0x04,
} bt_avrcp_player_attr_id_t;

typedef enum __packed {
        BT_AVRCP_EQUALIZER_OFF = 0x01,
        BT_AVRCP_EQUALIZER_ON = 0x02,
} bt_avrcp_equalizer_value_t;

typedef enum __packed {
        BT_AVRCP_REPEAT_MODE_OFF = 0x01,
        BT_AVRCP_REPEAT_MODE_SINGLE_TRACK = 0x02,
        BT_AVRCP_REPEAT_MODE_ALL_TRACKS = 0x03,
        BT_AVRCP_REPEAT_MODE_GROUP = 0x04,
} bt_avrcp_repeat_mode_value_t;

typedef enum __packed {
        BT_AVRCP_SHUFFLE_OFF = 0x01,
        BT_AVRCP_SHUFFLE_ALL_TRACKS = 0x02,
        BT_AVRCP_SHUFFLE_GROUP = 0x03,
} bt_avrcp_shuffle_value_t;

typedef enum __packed {
        BT_AVRCP_SCAN_OFF = 0x01,
        BT_AVRCP_SCAN_ALL_TRACKS = 0x02,
        BT_AVRCP_SCAN_GROUP = 0x03,
} bt_avrcp_scan_value_t;

struct bt_avrcp_list_player_app_setting_attrs_rsp {
        uint8_t num_attrs;
        uint8_t attr_ids[];
} __packed;

struct bt_avrcp_list_player_app_setting_vals_cmd {
        uint8_t attr_id;
} __packed;

struct bt_avrcp_list_player_app_setting_vals_rsp {
        uint8_t num_values;
        uint8_t values[];
} __packed;

struct bt_avrcp_get_curr_player_app_setting_val_cmd {
        uint8_t num_attrs;
        uint8_t attr_ids[];
} __packed;

struct bt_avrcp_app_setting_attr_val {
        uint8_t attr_id;
        uint8_t value_id;
} __packed;

struct bt_avrcp_get_curr_player_app_setting_val_rsp {
        uint8_t num_attrs;
        struct bt_avrcp_app_setting_attr_val attr_vals[];
} __packed;

struct bt_avrcp_set_player_app_setting_val_cmd {
        uint8_t num_attrs;
        struct bt_avrcp_app_setting_attr_val attr_vals[];
} __packed;

struct bt_avrcp_get_player_app_setting_attr_text_cmd {
        uint8_t num_attrs;
        uint8_t attr_ids[];
} __packed;

struct bt_avrcp_app_setting_attr_text {
        uint8_t attr_id;
        uint16_t charset_id;
        uint8_t text_len;
        uint8_t text[];
} __packed;

struct bt_avrcp_get_player_app_setting_attr_text_rsp {
        uint8_t num_attrs;
        struct bt_avrcp_app_setting_attr_text attr_text[];
} __packed;

struct bt_avrcp_get_player_app_setting_val_text_cmd {
        uint8_t attr_id;
        uint8_t num_values;
        uint8_t value_ids[];
} __packed;

struct bt_avrcp_app_setting_val_text {
        uint8_t value_id;
        uint16_t charset_id;
        uint8_t text_len;
        uint8_t text[];
} __packed;

struct bt_avrcp_get_player_app_setting_val_text_rsp {
        uint8_t num_values;
        struct bt_avrcp_app_setting_val_text value_text[];
} __packed;

struct bt_avrcp_inform_displayable_char_set_cmd {
        uint8_t num_charsets;
        uint16_t charset_ids[];
} __packed;

struct bt_avrcp_inform_batt_status_of_ct_cmd {
        uint8_t battery_status;
} __packed;

struct bt_avrcp_get_play_status_rsp {
        uint32_t song_length;
        uint32_t song_position;
        uint8_t play_status;
} __packed;

struct bt_avrcp_register_notification_cmd {
        uint8_t event_id;
        uint32_t interval;
} __packed;

struct bt_avrcp_set_absolute_volume_cmd {
        uint8_t absolute_volume;
} __packed;

struct bt_avrcp_set_absolute_volume_rsp {
        uint8_t absolute_volume;
} __packed;

struct bt_avrcp_set_addressed_player_cmd {
        uint16_t player_id;
} __packed;

struct bt_avrcp_play_item_cmd {
        uint8_t scope;
        uint8_t uid[8];
        uint16_t uid_counter;
} __packed;

struct bt_avrcp_add_to_now_playing_cmd {
        uint8_t scope;
        uint8_t uid[8];
        uint16_t uid_counter;
} __packed;

struct bt_avrcp_event_data {
        union {
                /* EVENT_PLAYBACK_STATUS_CHANGED */
                uint8_t play_status;

                /* EVENT_TRACK_CHANGED */
                uint8_t identifier[8];

                /* EVENT_PLAYBACK_POS_CHANGED */
                uint32_t playback_pos;

                /* EVENT_BATT_STATUS_CHANGED */
                uint8_t battery_status;

                /* EVENT_SYSTEM_STATUS_CHANGED */
                uint8_t system_status;

                /* EVENT_PLAYER_APPLICATION_SETTING_CHANGED */
                struct __packed {
                        uint8_t num_of_attr;
                        struct bt_avrcp_app_setting_attr_val *attr_vals;
                } setting_changed;

                /* EVENT_ADDRESSED_PLAYER_CHANGED */
                struct __packed {
                        uint16_t player_id;
                        uint16_t uid_counter;
                } addressed_player_changed;

                /* EVENT_UIDS_CHANGED */
                uint16_t uid_counter;

                /* EVENT_VOLUME_CHANGED */
                uint8_t absolute_volume;
        };
};

typedef void(*bt_avrcp_notify_changed_cb_t)(struct bt_avrcp_ct *ct, uint8_t event_id,
                                            struct bt_avrcp_event_data *data);

struct bt_avrcp_ct_cb {
        void (*connected)(struct bt_conn *conn, struct bt_avrcp_ct *ct);

        void (*disconnected)(struct bt_avrcp_ct *ct);

        void (*browsing_connected)(struct bt_conn *conn, struct bt_avrcp_ct *ct);

        void (*browsing_disconnected)(struct bt_avrcp_ct *ct);

        void (*get_caps)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, struct net_buf *buf);

        void (*unit_info_rsp)(struct bt_avrcp_ct *ct, uint8_t tid,
                              struct bt_avrcp_unit_info_rsp *rsp);

        void (*subunit_info_rsp)(struct bt_avrcp_ct *ct, uint8_t tid,
                                 struct bt_avrcp_subunit_info_rsp *rsp);

        void (*passthrough_rsp)(struct bt_avrcp_ct *ct, uint8_t tid, bt_avrcp_rsp_t result,
                                const struct bt_avrcp_passthrough_rsp *rsp);

        void (*set_browsed_player)(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

        void (*get_folder_items)(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

        void (*change_path)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status,
                            uint32_t num_items);

        void (*get_item_attrs)(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

        void (*get_total_number_of_items)(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

        void (*search)(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

        void (*browsing_general_reject)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status);

        void (*notification)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status, uint8_t event_id,
                             struct bt_avrcp_event_data *data);

        void (*list_player_app_setting_attrs)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status,
                                              struct net_buf *buf);

        void (*list_player_app_setting_vals)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status,
                                             struct net_buf *buf);

        void (*get_curr_player_app_setting_val)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status,
                                                struct net_buf *buf);

        void (*set_player_app_setting_val)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status);

        void (*get_player_app_setting_attr_text)(struct bt_avrcp_ct *ct, uint8_t tid,
                                                 uint8_t status, struct net_buf *buf);

        void (*get_player_app_setting_val_text)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status,
                                                struct net_buf *buf);

        void (*inform_displayable_char_set)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status);

        void (*inform_batt_status_of_ct)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status);

        void (*set_absolute_volume)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status,
                                   uint8_t absolute_volume);

        void (*get_element_attrs)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status,
                                  struct net_buf *buf);

        void (*get_play_status)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status,
                                struct net_buf *buf);

        void (*set_addressed_player)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status);

        void (*play_item)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status);

        void (*add_to_now_playing)(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t status);
};

int bt_avrcp_connect(struct bt_conn *conn);

int bt_avrcp_disconnect(struct bt_conn *conn);

struct net_buf *bt_avrcp_create_pdu(struct net_buf_pool *pool);

struct net_buf *bt_avrcp_create_vendor_pdu(struct net_buf_pool *pool);

int bt_avrcp_browsing_connect(struct bt_conn *conn);

int bt_avrcp_browsing_disconnect(struct bt_conn *conn);

int bt_avrcp_ct_register_cb(const struct bt_avrcp_ct_cb *cb);

int bt_avrcp_ct_get_caps(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t cap_id);

int bt_avrcp_ct_get_unit_info(struct bt_avrcp_ct *ct, uint8_t tid);

int bt_avrcp_ct_get_subunit_info(struct bt_avrcp_ct *ct, uint8_t tid);

int bt_avrcp_ct_passthrough(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t opid, uint8_t state,
                            const uint8_t *payload, uint8_t len);

int bt_avrcp_ct_set_browsed_player(struct bt_avrcp_ct *ct, uint8_t tid, uint16_t player_id);

int bt_avrcp_ct_register_notification(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t event_id,
                                      uint32_t interval, bt_avrcp_notify_changed_cb_t cb);

int bt_avrcp_ct_list_player_app_setting_attrs(struct bt_avrcp_ct *ct, uint8_t tid);

int bt_avrcp_ct_list_player_app_setting_vals(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t attr_id);

int bt_avrcp_ct_get_curr_player_app_setting_val(struct bt_avrcp_ct *ct, uint8_t tid,
                                                struct net_buf *buf);

int bt_avrcp_ct_set_player_app_setting_val(struct bt_avrcp_ct *ct, uint8_t tid,
                                           struct net_buf *buf);

int bt_avrcp_ct_get_player_app_setting_attr_text(struct bt_avrcp_ct *ct, uint8_t tid,
                                                 struct net_buf *buf);

int bt_avrcp_ct_get_player_app_setting_val_text(struct bt_avrcp_ct *ct, uint8_t tid,
                                                struct net_buf *buf);

int bt_avrcp_ct_inform_displayable_char_set(struct bt_avrcp_ct *ct, uint8_t tid,
                                            struct net_buf *buf);

int bt_avrcp_ct_inform_batt_status_of_ct(struct bt_avrcp_ct *ct, uint8_t tid,
                                         uint8_t battery_status);

int bt_avrcp_ct_set_absolute_volume(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t absolute_volume);

int bt_avrcp_ct_get_element_attrs(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

int bt_avrcp_ct_get_play_status(struct bt_avrcp_ct *ct, uint8_t tid);

int bt_avrcp_ct_set_addressed_player(struct bt_avrcp_ct *ct, uint8_t tid, uint16_t player_id);

int bt_avrcp_ct_play_item(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

int bt_avrcp_ct_add_to_now_playing(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

int bt_avrcp_ct_get_folder_items(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

int bt_avrcp_ct_change_path(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

int bt_avrcp_ct_get_item_attrs(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

int bt_avrcp_ct_get_total_number_of_items(struct bt_avrcp_ct *ct, uint8_t tid, uint8_t scope);

int bt_avrcp_ct_search(struct bt_avrcp_ct *ct, uint8_t tid, struct net_buf *buf);

struct bt_avrcp_tg_cb {
        void (*connected)(struct bt_conn *conn, struct bt_avrcp_tg *tg);

        void (*disconnected)(struct bt_avrcp_tg *tg);

        void (*unit_info_req)(struct bt_avrcp_tg *tg, uint8_t tid);

        void (*register_notification)(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t event_id,
                                      uint32_t interval);

        void (*subunit_info_req)(struct bt_avrcp_tg *tg, uint8_t tid);

        void (*get_caps)(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t cap_id);

        void (*browsing_connected)(struct bt_conn *conn, struct bt_avrcp_tg *tg);

        void (*browsing_disconnected)(struct bt_avrcp_tg *tg);

        void (*set_browsed_player)(struct bt_avrcp_tg *tg, uint8_t tid, uint16_t player_id);

        void (*get_folder_items)(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

        void (*change_path)(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

        void (*get_item_attrs)(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

        void (*get_total_number_of_items)(struct bt_avrcp_tg *tg, uint8_t tid,  uint8_t scope);

        void (*search)(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

        void (*passthrough_req)(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

        void (*list_player_app_setting_attrs)(struct bt_avrcp_tg *tg, uint8_t tid);

        void (*list_player_app_setting_vals)(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t attr_id);

        void (*get_curr_player_app_setting_val)(struct bt_avrcp_tg *tg, uint8_t tid,
                                                struct net_buf *buf);

        void (*set_player_app_setting_val)(struct bt_avrcp_tg *tg, uint8_t tid,
                                           struct net_buf *buf);

        void (*get_player_app_setting_attr_text)(struct bt_avrcp_tg *tg, uint8_t tid,
                                                 struct net_buf *buf);

        void (*get_player_app_setting_val_text)(struct bt_avrcp_tg *tg, uint8_t tid,
                                                struct net_buf *buf);

        void (*inform_displayable_char_set)(struct bt_avrcp_tg *tg, uint8_t tid,
                                            struct net_buf *buf);

        void (*inform_batt_status_of_ct)(struct bt_avrcp_tg *tg, uint8_t tid,
                                         uint8_t battery_status);

        void (*get_element_attrs)(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

        void (*set_absolute_volume)(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t absolute_volume);

        void (*get_play_status)(struct bt_avrcp_tg *tg, uint8_t tid);

        void (*set_addressed_player)(struct bt_avrcp_tg *tg, uint8_t tid, uint16_t player_id);

        void (*play_item)(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

        void (*add_to_now_playing)(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);
};

int bt_avrcp_tg_register_cb(const struct bt_avrcp_tg_cb *cb);

int bt_avrcp_tg_send_unit_info_rsp(struct bt_avrcp_tg *tg, uint8_t tid,
                                   struct bt_avrcp_unit_info_rsp *rsp);

int bt_avrcp_tg_send_subunit_info_rsp(struct bt_avrcp_tg *tg, uint8_t tid);

int bt_avrcp_tg_get_caps(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, struct net_buf *buf);

int bt_avrcp_tg_notification(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status, uint8_t event_id,
                             struct bt_avrcp_event_data *data);

int bt_avrcp_tg_set_browsed_player(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

int bt_avrcp_tg_send_passthrough_rsp(struct bt_avrcp_tg *tg, uint8_t tid, bt_avrcp_rsp_t result,
                                     struct net_buf *buf);

int bt_avrcp_tg_list_player_app_setting_attrs(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status,
                                              struct net_buf *buf);

int bt_avrcp_tg_list_player_app_setting_vals(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status,
                                             struct net_buf *buf);

int bt_avrcp_tg_get_curr_player_app_setting_val(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status,
                                                struct net_buf *buf);

int bt_avrcp_tg_set_player_app_setting_val(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status);

int bt_avrcp_tg_get_player_app_setting_attr_text(struct bt_avrcp_tg *tg, uint8_t tid,
                                                 uint8_t status, struct net_buf *buf);

int bt_avrcp_tg_get_player_app_setting_val_text(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status,
                                                struct net_buf *buf);

int bt_avrcp_tg_inform_displayable_char_set(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status);

int bt_avrcp_tg_inform_batt_status_of_ct(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status);

int bt_avrcp_tg_absolute_volume(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status,
                                uint8_t absolute_volume);

int bt_avrcp_tg_get_element_attrs(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status,
                                  struct net_buf *buf);

int bt_avrcp_tg_get_play_status(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status,
                                struct net_buf *buf);

int bt_avrcp_tg_set_addressed_player(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status);

int bt_avrcp_tg_play_item(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status);

int bt_avrcp_tg_add_to_now_playing(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status);

int bt_avrcp_tg_get_folder_items(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

int bt_avrcp_tg_change_path(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status,
                            uint32_t num_items);

int bt_avrcp_tg_get_item_attrs(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

int bt_avrcp_tg_get_total_number_of_items(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

int bt_avrcp_tg_search(struct bt_avrcp_tg *tg, uint8_t tid, struct net_buf *buf);

int bt_avrcp_tg_browsing_general_reject(struct bt_avrcp_tg *tg, uint8_t tid, uint8_t status);
#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVRCP_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015-2016 Intel Corporation。

版权（Copyright）：(C) 2024 Xiaomi Corporation。

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 787 行

播放状态变化事件：`EVENT_PLAYBACK_STATUS_CHANGED`。

### 注释 3：原第 790 行

曲目变化事件：`EVENT_TRACK_CHANGED`。

### 注释 4：原第 793 行

播放位置变化事件：`EVENT_PLAYBACK_POS_CHANGED`。

### 注释 5：原第 796 行

电池状态变化事件：`EVENT_BATT_STATUS_CHANGED`。

### 注释 6：原第 799 行

系统状态变化事件：`EVENT_SYSTEM_STATUS_CHANGED`。

### 注释 7：原第 802 行

播放器应用设置变化事件：`EVENT_PLAYER_APPLICATION_SETTING_CHANGED`。

### 注释 8：原第 808 行

被寻址播放器变化事件：`EVENT_ADDRESSED_PLAYER_CHANGED`。

### 注释 9：原第 814 行

唯一标识符变化事件：`EVENT_UIDS_CHANGED`。

### 注释 10：原第 817 行

音量变化事件：`EVENT_VOLUME_CHANGED`。

### 注释 11：原第 2443 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_AVRCP_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h.html)
- [BT_AVRCP_CAP_COMPANY_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac311dc7b5f99162b954271529eeb84eaa89fecce56afb09791a2253a7ad840430)
- [BT_AVRCP_CAP_EVENTS_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac311dc7b5f99162b954271529eeb84eaa2a7b326aded772c09cf01387145d2802)
- [bt_avrcp_cap_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac311dc7b5f99162b954271529eeb84ea)
- [BT_AVRCP_EVT_PLAYBACK_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a892f2928d634b675426f2fe597a45f6d)
- [BT_AVRCP_EVT_TRACK_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a25f8e3e08b5988e833eb0d47452d12a9)
- [BT_AVRCP_EVT_TRACK_REACHED_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a412a9b7cbb891bc50fb77c1e6de9faaf)
- [BT_AVRCP_EVT_TRACK_REACHED_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75af4f9e221522cd57461920d22e7a290b9)
- [BT_AVRCP_EVT_PLAYBACK_POS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75afc4ef6f8a80a9067ad9dfd30bf2a6958)
- [BT_AVRCP_EVT_BATT_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a9ff1d99bc0c83399961ef23d4a75f9b6)
- [BT_AVRCP_EVT_SYSTEM_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ae6237555b0051b2395e0bf2287e954c1)
- [BT_AVRCP_EVT_PLAYER_APP_SETTING_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ab2b2287a0db9be97af8c20298bebba2d)
- [BT_AVRCP_EVT_NOW_PLAYING_CONTENT_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ac0b720defdd8716d757e0c8a7e57db83)
- [BT_AVRCP_EVT_AVAILABLE_PLAYERS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75abd82dd6ba6d5d76cf22a8c703c76c6e0)
- [BT_AVRCP_EVT_ADDRESSED_PLAYER_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75ab6fdeacb536067660f754b3c586e073a)
- [BT_AVRCP_EVT_UIDS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a8ac593400cda085fbdff36e403bd2a91)
- [BT_AVRCP_EVT_VOLUME_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaf55aae17f67a1361279ae208b17e4a75a8d526498fdcb1380e8e3944da2a5ef85)
- [bt_avrcp_evt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaf55aae17f67a1361279ae208b17e4a75)
- [BT_AVRCP_CTYPE_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ea1a2aa36da42f3751f3a94b218118ae04)
- [BT_AVRCP_CTYPE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ea9a1b0564c98a0637a2ca5a0b97c3e6ce)
- [BT_AVRCP_CTYPE_SPECIFIC_INQUIRY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618eac4c9dfbce497d9a043d7ac42ee932bdb)
- [BT_AVRCP_CTYPE_NOTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ead58dcc95df3973a7bed94068be913290)
- [BT_AVRCP_CTYPE_GENERAL_INQUIRY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga2a4c610e00ba9832f954f30bd6b6618ea0eefcdda49616cf818efdc0a7b5975f7)
- [bt_avrcp_ctype_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga2a4c610e00ba9832f954f30bd6b6618e)
- [BT_AVRCP_RSP_NOT_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a8a4cfe6ca8f5b92402c029d02b625696)
- [BT_AVRCP_RSP_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a2c93dc0bfd19305d8012b73001989cd8)
- [BT_AVRCP_RSP_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a1775849a3c303b61975c569cc85e943c)
- [BT_AVRCP_RSP_IN_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326ab4b63e5cf84ea34895702ceea5ae81ad)
- [BT_AVRCP_RSP_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326aa49f2871cf4e5f493128f574ad0d6144)
- [BT_AVRCP_RSP_STABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a4136d697a8a0ea5daa1a6e89b314b992)
- [BT_AVRCP_RSP_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326acf6f13da82b371efbcdf03fbedcb6988)
- [BT_AVRCP_RSP_INTERIM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaba2d8faec2c3baf7403199ea8a509326a4a2ed58a814be12b93753a6458b15e88)
- [bt_avrcp_rsp_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaba2d8faec2c3baf7403199ea8a509326)
- [BT_AVRCP_SUBUNIT_TYPE_PANEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga78ba828636b731b2c43e088a581bfee9a6db3104fa9727594b842b4ae9b64a605)
- [BT_AVRCP_SUBUNIT_TYPE_UNIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga78ba828636b731b2c43e088a581bfee9a8be8c211cd26a849c1c89e482aa10030)
- [bt_avrcp_subunit_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga78ba828636b731b2c43e088a581bfee9)
- [BT_AVRCP_OPID_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84acbaded78ac1e41d16464ea9db667c27f)
- [BT_AVRCP_OPID_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84aae8fe4a27cf2b70bb289f38d4016b9d9)
- [BT_AVRCP_OPID_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a0d81584ba5cc6bb9c790b87fcf638537)
- [BT_AVRCP_OPID_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a734fa5664a306957cb28eec36806e4ba)
- [BT_AVRCP_OPID_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a9030a666a42a54b02b4c7f876f1ae9d2)
- [BT_AVRCP_OPID_RIGHT_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a831592a4b2634815f9716e80252dce63)
- [BT_AVRCP_OPID_RIGHT_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a61d7145a6aa482256cd8aaad7bb96745)
- [BT_AVRCP_OPID_LEFT_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8445dd492ab9e6a9b387162f2f7ab779)
- [BT_AVRCP_OPID_LEFT_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a6660a000e5bc1d8ead271924a3780366)
- [BT_AVRCP_OPID_ROOT_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a002efdb93a2dd52bb5bbec05d9537f87)
- [BT_AVRCP_OPID_SETUP_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a827d1eaa2f12a37219fc1f78f617d372)
- [BT_AVRCP_OPID_CONTENTS_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84aa9d64afb98b2fc91cae3810990451472)
- [BT_AVRCP_OPID_FAVORITE_MENU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a470fa709a8a7e35ec12a593ae9dd1574)
- [BT_AVRCP_OPID_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a9ecca98aa1f55ee6a2b6824e0940a7c3)
- [BT_AVRCP_OPID_0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae6430b447ccd9e15d0ef2ae62152bade)
- [BT_AVRCP_OPID_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a94ca82a18f2c06379160e69675d927d0)
- [BT_AVRCP_OPID_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84acb3f6e1f71628853bb457bfb8163c566)
- [BT_AVRCP_OPID_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84af1d1ea7e57a0a16c8e6ad8b9961d4459)
- [BT_AVRCP_OPID_4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a23d18efccc7b1940e72b62b08fa5ab6c)
- [BT_AVRCP_OPID_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a91a40f7dfb02c38cd7998adf5fe948b5)
- [BT_AVRCP_OPID_6](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a029017bcc52cf7c4ffac3db5f92f4e2a)
- [BT_AVRCP_OPID_7](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84aac755d13a6f53ead21818a9fb90217ff)
- [BT_AVRCP_OPID_8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ac751478296cc6a9e5de77fdf3c8fce06)
- [BT_AVRCP_OPID_9](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a07ed4fda3e230d4e95576a25c6d02dcb)
- [BT_AVRCP_OPID_DOT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a5d3a33be8473fc401e3f38a9f234debf)
- [BT_AVRCP_OPID_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a28d5c8b1960aa1e70c0659c40cac32ae)
- [BT_AVRCP_OPID_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae6046a270ff9f8939059248cddc7a8a2)
- [BT_AVRCP_OPID_CHANNEL_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ad39e69c55c571eb3c2492d5aa086e586)
- [BT_AVRCP_OPID_CHANNEL_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a300bbf8fe3236a55bfc97e2d7d8323de)
- [BT_AVRCP_OPID_PREVIOUS_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a3e59a9dc846182d2bc26cf2e5960558e)
- [BT_AVRCP_OPID_SOUND_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a1fb2420a2130a9f22f1837c0c3e0896b)
- [BT_AVRCP_OPID_INPUT_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8fa3d0ac9fc3feefedf3b2d370df748c)
- [BT_AVRCP_OPID_DISPLAY_INFORMATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a735b97b85b1183c862955131a09b1eef)
- [BT_AVRCP_OPID_HELP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ab3a7619c2c3cafe2eab868d471c8066b)
- [BT_AVRCP_OPID_PAGE_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a93ffda310d3a0999256b42cd4652e321)
- [BT_AVRCP_OPID_PAGE_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a3078b64d3c759e83d04923ca6bcf079a)
- [BT_AVRCP_OPID_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a9623c492b7a04750fb3938dde65a9358)
- [BT_AVRCP_OPID_VOLUME_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84af5f5b89b6f81961f7bf235c91f59b487)
- [BT_AVRCP_OPID_VOLUME_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a49d2a954862bdf45c30ed734e5a29a62)
- [BT_AVRCP_OPID_MUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a5c37fbe03a5e7b8cda842262f7a504e1)
- [BT_AVRCP_OPID_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae76461b7c08169ad190a83545b9e584b)
- [BT_AVRCP_OPID_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a69254767fc4183e1534b12cd6bd88f60)
- [BT_AVRCP_OPID_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a0e7877d88781dbacdac095c7d36f186a)
- [BT_AVRCP_OPID_RECORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8364f5d44be3b666f5d995368e3dda27)
- [BT_AVRCP_OPID_REWIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a4bba25ed6730766902ecb92e4f546dc8)
- [BT_AVRCP_OPID_FAST_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a6c83aff2115939aa17f6bbd68c792e4f)
- [BT_AVRCP_OPID_EJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ae34d68953054ef4446403a1e240e3344)
- [BT_AVRCP_OPID_FORWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a004689a6684c527035f06fa8d715a09e)
- [BT_AVRCP_OPID_BACKWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a0030ffc7149baf83def17e4e2be76f23)
- [BT_AVRCP_OPID_ANGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84afc51d7bc6acd64c3dbeb1f10a06113c2)
- [BT_AVRCP_OPID_SUBPICTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ac1e3dd409b98c71eaf12567ce5028a98)
- [BT_AVRCP_OPID_F1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a91595d93490cfe27e239c799e927b2b5)
- [BT_AVRCP_OPID_F2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a8b0656fed7b936e131a5c9dbdb32a7a4)
- [BT_AVRCP_OPID_F3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a1380078d446b892a25b8b2d28a405e40)
- [BT_AVRCP_OPID_F4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a01fc4e91d59b8c530fe142d2f1c95283)
- [BT_AVRCP_OPID_F5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84a86a61c08b203d0bcc8b8a3ed5090ef7d)
- [BT_AVRCP_OPID_VENDOR_UNIQUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga3c997d96028343a0a5a4948dabe19b84ad6eac39b4aced31534fde97a411b8c4d)
- [bt_avrcp_opid_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga3c997d96028343a0a5a4948dabe19b84)
- [BT_AVRCP_BUTTON_PRESSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga15f9f868b056f17ea12d96530b7da881a1465f08940f04a7b35832e6d5f73a4e3)
- [BT_AVRCP_BUTTON_RELEASED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga15f9f868b056f17ea12d96530b7da881a0eb47ec4ca3d7e0bf613de53d5e50706)
- [bt_avrcp_button_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga15f9f868b056f17ea12d96530b7da881)
- [BT_AVRCP_STATUS_INVALID_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a14e183c33a64cdac271ee7f320796bd6)
- [BT_AVRCP_STATUS_INVALID_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a8a767466ac8069e20f6d9e0f30c33420)
- [BT_AVRCP_STATUS_PARAMETER_CONTENT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a7cba04973b3753b50f63e6b0bc205638)
- [BT_AVRCP_STATUS_INTERNAL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0af48dcc2c65e4af461c1a6ece622a2f5a)
- [BT_AVRCP_STATUS_OPERATION_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0ad3a41ce04f27cc349c7466aae18bcee2)
- [BT_AVRCP_STATUS_UID_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a0e77e1782b5a0f88f4d45b6560df2b09)
- [BT_AVRCP_STATUS_INVALID_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a448e1c0383e4e4b5fc3c0c80e2040af9)
- [BT_AVRCP_STATUS_NOT_A_DIRECTORY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a6fee8c927f897fff59b7690c3e1732c2)
- [BT_AVRCP_STATUS_DOES_NOT_EXIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a9f552377c6bb93b3e52b29228a6feaa5)
- [BT_AVRCP_STATUS_INVALID_SCOPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0aaddaf4f6439aa6a52e3a4fdbb3f0c071)
- [BT_AVRCP_STATUS_RANGE_OUT_OF_BOUNDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a81094560261826c16be6ebba9d99081c)
- [BT_AVRCP_STATUS_FOLDER_ITEM_IS_NOT_PLAYABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a2f8ca7c1fe4ba52a1a418612c094158a)
- [BT_AVRCP_STATUS_MEDIA_IN_USE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0ae63cf3ffada01f268498151d88c3a3ec)
- [BT_AVRCP_STATUS_NOW_PLAYING_LIST_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a359810fbbdf875adb89a192deaae6a6d)
- [BT_AVRCP_STATUS_SEARCH_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a4ee781cc845d8b1211217f8338b97023)
- [BT_AVRCP_STATUS_SEARCH_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a402038758703ee9f8543ad546681a3c5)
- [BT_AVRCP_STATUS_INVALID_PLAYER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a5cd415ba8d307dc5153a9a0b2f9958e3)
- [BT_AVRCP_STATUS_PLAYER_NOT_BROWSABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a28925d094d4c3e55b259a55440a5c044)
- [BT_AVRCP_STATUS_PLAYER_NOT_ADDRESSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a3dfa01e069c517e7e466fa6edcc1c9cb)
- [BT_AVRCP_STATUS_NO_VALID_SEARCH_RESULTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a033e10d03bf56df95ec1e888a07cedf9)
- [BT_AVRCP_STATUS_NO_AVAILABLE_PLAYERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a5544c22cad94dadb9eccf47669fabafb)
- [BT_AVRCP_STATUS_ADDRESSED_PLAYER_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a43e59407a44f87d85fa71cdb627524e3)
- [BT_AVRCP_STATUS_IN_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0af72a55b60fda9c157cdef8b1c6038780)
- [BT_AVRCP_STATUS_NOT_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0a14868dd213f59e09dbdb066d5ca39c96)
- [BT_AVRCP_STATUS_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga52368f4cc655bab75f96da80ddaaabe0afbff25149bb9c35756dfb7bb6f2516c3)
- [bt_avrcp_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga52368f4cc655bab75f96da80ddaaabe0)
- [bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)
- [bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)
- [bt_avrcp_unit_info_rsp](../bluetooth_classic_model_reference/P072_bt_avrcp_unit_info_rsp_结构体.md)
- [unit_type](../bluetooth_classic_model_reference/P072_bt_avrcp_unit_info_rsp_结构体.md#a92b869b3200841ea1d10aca41cdd9f77)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [company_id](../bluetooth_classic_model_reference/P072_bt_avrcp_unit_info_rsp_结构体.md#a0225755bf457bc6d4046d8172af49217)
- [bt_avrcp_subunit_info_rsp](../bluetooth_classic_model_reference/P069_bt_avrcp_subunit_info_rsp_结构体.md)
- [subunit_type](../bluetooth_classic_model_reference/P069_bt_avrcp_subunit_info_rsp_结构体.md#a144ad1d366436c8b2502a17833a36dc3)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [max_subunit_id](../bluetooth_classic_model_reference/P069_bt_avrcp_subunit_info_rsp_结构体.md#a85cf595920ba2dbf9f0e4deca1d27483)
- [extended_subunit_type](../bluetooth_classic_model_reference/P069_bt_avrcp_subunit_info_rsp_结构体.md#a47b69412c61682ed336737f34ac614dc)
- [extended_subunit_id](../bluetooth_classic_model_reference/P069_bt_avrcp_subunit_info_rsp_结构体.md#a0be33096e6edf251c23a5322b3c30421)
- [bt_avrcp_passthrough_opvu_data](../bluetooth_classic_model_reference/P057_bt_avrcp_passthrough_opvu_data_结构体.md)
- [company_id](../bluetooth_classic_model_reference/P057_bt_avrcp_passthrough_opvu_data_结构体.md#a17f6d3c32417102c04502336235f94fa)
- [BT_AVRCP_COMPANY_ID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae4e7573280179717124104858629122a)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [opid_vu](../bluetooth_classic_model_reference/P057_bt_avrcp_passthrough_opvu_data_结构体.md#a13db1521501ab7c24643b2d1fd6e956a)
- [bt_avrcp_passthrough_cmd](../bluetooth_classic_model_reference/P056_bt_avrcp_passthrough_cmd_结构体.md)
- [opid_state](../bluetooth_classic_model_reference/P056_bt_avrcp_passthrough_cmd_结构体.md#aaaa7657a9942d463bbe2647a0a20c0e1)
- [data_len](../bluetooth_classic_model_reference/P056_bt_avrcp_passthrough_cmd_结构体.md#a9facd7635f3768ac8e5351b6542b7a52)
- [data](../bluetooth_classic_model_reference/P056_bt_avrcp_passthrough_cmd_结构体.md#a96b9081498ddac9f8140651b0dfab1ee)
- [bt_avrcp_passthrough_rsp](../bluetooth_classic_model_reference/P058_bt_avrcp_passthrough_rsp_结构体.md)
- [opid_state](../bluetooth_classic_model_reference/P058_bt_avrcp_passthrough_rsp_结构体.md#a91aaa705b91cc9ca0954645a9a43c504)
- [data_len](../bluetooth_classic_model_reference/P058_bt_avrcp_passthrough_rsp_结构体.md#a16c0388be437f140c5aaa1364cdfb3fe)
- [data](../bluetooth_classic_model_reference/P058_bt_avrcp_passthrough_rsp_结构体.md#a735fca5cd5e5d85e987af9748f9d0ab0)
- [bt_avrcp_get_caps_rsp](../bluetooth_classic_model_reference/P031_bt_avrcp_get_caps_rsp_结构体.md)
- [cap_id](../bluetooth_classic_model_reference/P031_bt_avrcp_get_caps_rsp_结构体.md#a587d32dcd5abe2e1751a75bcc4bbe5b2)
- [cap_cnt](../bluetooth_classic_model_reference/P031_bt_avrcp_get_caps_rsp_结构体.md#a1f588c2e4204c2f43c4872ee9d6ff6b1)
- [cap](../bluetooth_classic_model_reference/P031_bt_avrcp_get_caps_rsp_结构体.md#a8a4c9b7c09cf3db137431ff788006e87)
- [BT_AVRCP_CHARSET_UTF8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga81330413af9eba049da6557b14ae082ca29f70165632222ae40ac3e44554130b0)
- [bt_avrcp_charset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81330413af9eba049da6557b14ae082c)
- [BT_AVRCP_SCOPE_MEDIA_PLAYER_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a7a388bb84fbe14f8931ab9bf41b9823d)
- [BT_AVRCP_SCOPE_VFS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a37002574948081d7b42001a62755636b)
- [BT_AVRCP_SCOPE_SEARCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a4db7699a5f22c8d5986f6f1ba7219dac)
- [BT_AVRCP_SCOPE_NOW_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggaabab9a4f37b3f9653ca95dd4b5944707a7baa6442aafc4d00635df52f44d0d608)
- [bt_avrcp_scope_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaabab9a4f37b3f9653ca95dd4b5944707)
- [BT_AVRCP_CHANGE_PATH_PARENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga02d67e84b4a48ebecf3b307cbd4bb61ca8914559b14b7529fc5f1df764036748d)
- [BT_AVRCP_CHANGE_PATH_CHILD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga02d67e84b4a48ebecf3b307cbd4bb61ca5cbd84478163171359044825050dd172)
- [bt_avrcp_change_path_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga02d67e84b4a48ebecf3b307cbd4bb61c)
- [BT_AVRCP_FOLDER_TYPE_MIXED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a06308eb3786579cf5aeb0f19f0ab37ac)
- [BT_AVRCP_FOLDER_TYPE_TITLES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a702f9974cf5d51a77757fd7e1ef4ab0f)
- [BT_AVRCP_FOLDER_TYPE_ALBUMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5ab33fca5f57f5b80785df367ab788a8fc)
- [BT_AVRCP_FOLDER_TYPE_ARTISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a89aaeb11e807c44479ff47164d99c4f7)
- [BT_AVRCP_FOLDER_TYPE_GENRES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a0ab0ffb986db900ece2146a347dae06d)
- [BT_AVRCP_FOLDER_TYPE_PLAYLISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a708dfb5de11ae783b413d2d99202f9b5)
- [BT_AVRCP_FOLDER_TYPE_YEARS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga09d191c490efcfb9f8139975090be0d5a0a60cb99cd19d203618b1264e2a3cca6)
- [bt_avrcp_folder_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga09d191c490efcfb9f8139975090be0d5)
- [BT_AVRCP_MEDIA_TYPE_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac927c7e7c59f6f0e6243ca0887945d5aa9847baed2a6d09d4ac81039c7302832b)
- [BT_AVRCP_MEDIA_TYPE_VIDEO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac927c7e7c59f6f0e6243ca0887945d5aa76bd7c8c80d6ad9985430148cfd44e82)
- [bt_avrcp_media_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac927c7e7c59f6f0e6243ca0887945d5a)
- [BT_AVRCP_MEDIA_ATTR_ID_TITLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592acce73266473e0a14580fa337d2fe53b3)
- [BT_AVRCP_MEDIA_ATTR_ID_ARTIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a436c4847edcad7121f7d2ed97169fe61)
- [BT_AVRCP_MEDIA_ATTR_ID_ALBUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a2b7e8439c8050cdeda97c43d07774001)
- [BT_AVRCP_MEDIA_ATTR_ID_TRACK_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592ac66e18f0843901209f9004a62ab55624)
- [BT_AVRCP_MEDIA_ATTR_ID_TOTAL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a3dcfd47034d7890e80a05fd4f600f6bf)
- [BT_AVRCP_MEDIA_ATTR_ID_GENRE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a8fd312d2869f38b6d7446716a30392b1)
- [BT_AVRCP_MEDIA_ATTR_ID_PLAYING_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a0ba1f760a733cd00923970d01bb85293)
- [BT_AVRCP_MEDIA_ATTR_ID_DEFAULT_COVER_ART](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga0ebc5d2657688b70119e11ac20d24592a958ef736372f39d8e180f8fdeb025121)
- [bt_avrcp_media_attr_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga0ebc5d2657688b70119e11ac20d24592)
- [bt_avrcp_get_folder_items_cmd](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md)
- [scope](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md#af89fb8a745c45a3b768d16d93d5d4287)
- [start_item](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md#ae362914e3f3be32d6381035176431c88)
- [end_item](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md#abf2e154d28317043a88ea00475d777a2)
- [attr_count](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md#a7068f5115cf58c075f1deefbb10e4627)
- [attr_ids](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md#a790f3718f2e6e3d32d1824794a146e4e)
- [BT_AVRCP_ITEM_TYPE_MEDIA_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac02fed37e267996d4de50b06292d0668ad8dd8a59776d9d29655cbd083fae6535)
- [BT_AVRCP_ITEM_TYPE_FOLDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac02fed37e267996d4de50b06292d0668aeb7289d0102af72c607d42a8f1c6dfa5)
- [BT_AVRCP_ITEM_TYPE_MEDIA_ELEMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggac02fed37e267996d4de50b06292d0668aca944e6647d353290b4e5c25fde28bd8)
- [bt_avrcp_item_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac02fed37e267996d4de50b06292d0668)
- [bt_avrcp_item_hdr](../bluetooth_classic_model_reference/P049_bt_avrcp_item_hdr_结构体.md)
- [item_type](../bluetooth_classic_model_reference/P049_bt_avrcp_item_hdr_结构体.md#ac9327e576791370bcb7b2f7140f99ee4)
- [item_len](../bluetooth_classic_model_reference/P049_bt_avrcp_item_hdr_结构体.md#aee91353e20e227cdf095153b101bc69a)
- [bt_avrcp_media_player_item](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md)
- [hdr](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#a15488d00a442bc3cdfdf44c383bb6738)
- [player_id](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#a39c8b80e71c70d4cf84ecb25a03b4f8f)
- [major_type](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#aeca27933a1892ac6c6b0951a4bf68370)
- [player_subtype](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#a62c18bb03aed36dda87eff9599100dec)
- [play_status](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#ac8571c557795c5fec5512c7868e34dfc)
- [feature_bitmask](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#ad3d1c3443f1a4d0b28623e0a3e1a6607)
- [charset_id](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#afda406082181582f7fcf4b44d2f6fc8c)
- [name_len](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#a02f71111fc2b4e4f53cd186aaf4372cf)
- [name](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#a9e6f3f5621a76b8ab37c0833916dae69)
- [bt_avrcp_folder_item](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md)
- [hdr](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#a8bfa3c0f6854961df4378f0cbe4918e4)
- [uid](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#ab6cd2f27e38730e3137dd739f4483585)
- [folder_type](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#abeb5d94d8a9f91be8769403b6f360991)
- [playable](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#a168cb4f00af9685d8b9023b09f5dcbe2)
- [charset_id](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#ab6fa897bd3c15801955592c972220391)
- [name_len](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#a99a9de89c0d2e7f1b95f80f245e4126c)
- [name](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#a682d5d56c49f82e04a812249042353ca)
- [bt_avrcp_media_attr](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md)
- [attr_id](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md#ae9389f3574be88638cce4e478c532a2b)
- [charset_id](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md#a48e88ae5b4c448e0fad0325891ed82d1)
- [attr_len](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md#a07ad1a91103fcec7b69d02b7967f1815)
- [attr_val](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md#af8b744485f601d694fc43ae3e6d8b28a)
- [media_element_item_name](../device_power_control_model_reference/P028_media_element_item_name_结构体.md)
- [charset_id](../device_power_control_model_reference/P028_media_element_item_name_结构体.md#a9ab8705023810277a63566d5b05bc777)
- [name_len](../device_power_control_model_reference/P028_media_element_item_name_结构体.md#a51866bcc43ed3ed31feb87ac60f97171)
- [name](../device_power_control_model_reference/P028_media_element_item_name_结构体.md#a66b939713a0b4f7aadfbbf65e5b8cef3)
- [media_element_item_attr](../device_power_control_model_reference/P027_media_element_item_attr_结构体.md)
- [num_attrs](../device_power_control_model_reference/P027_media_element_item_attr_结构体.md#aee96c7d393f086f89e995a96eb95cce9)
- [attrs](../device_power_control_model_reference/P027_media_element_item_attr_结构体.md#a00c0f6e1b42a8b6448574105acb0481d)
- [bt_avrcp_media_element_item](../bluetooth_classic_model_reference/P054_bt_avrcp_media_element_item_结构体.md)
- [hdr](../bluetooth_classic_model_reference/P054_bt_avrcp_media_element_item_结构体.md#afe49a107dd657a16336087d2d518f1a7)
- [uid](../bluetooth_classic_model_reference/P054_bt_avrcp_media_element_item_结构体.md#ac0c12c790e4544eaec7d5766969ff152)
- [media_type](../bluetooth_classic_model_reference/P054_bt_avrcp_media_element_item_结构体.md#a1695ec1cf7ff0b5f379d31f5137c893a)
- [data](../bluetooth_classic_model_reference/P054_bt_avrcp_media_element_item_结构体.md#a198a755a9f0c6ff88f139ac0911ed54d)
- [bt_avrcp_get_folder_items_rsp](../bluetooth_classic_model_reference/P037_bt_avrcp_get_folder_items_rsp_结构体.md)
- [status](../bluetooth_classic_model_reference/P037_bt_avrcp_get_folder_items_rsp_结构体.md#a7ef2c44e62e2e35b86db3398a84fa88c)
- [uid_counter](../bluetooth_classic_model_reference/P037_bt_avrcp_get_folder_items_rsp_结构体.md#a387d5ed3a962e27632821505fd6f0b03)
- [num_items](../bluetooth_classic_model_reference/P037_bt_avrcp_get_folder_items_rsp_结构体.md#a0b95f4d78a16bea65f18690f0081e099)
- [items](../bluetooth_classic_model_reference/P037_bt_avrcp_get_folder_items_rsp_结构体.md#a073136a279ed9b5f2aaf9db8c6f17607)
- [bt_avrcp_change_path_cmd](../bluetooth_classic_model_reference/P020_bt_avrcp_change_path_cmd_结构体.md)
- [uid_counter](../bluetooth_classic_model_reference/P020_bt_avrcp_change_path_cmd_结构体.md#ac575ced16bc5e61043b035b406f732a4)
- [direction](../bluetooth_classic_model_reference/P020_bt_avrcp_change_path_cmd_结构体.md#a1ced4e12dd7d1c3b31213dce355cf165)
- [folder_uid](../bluetooth_classic_model_reference/P020_bt_avrcp_change_path_cmd_结构体.md#a026e337b5bcf6f827f32314eabd19832)
- [bt_avrcp_change_path_rsp](../bluetooth_classic_model_reference/P021_bt_avrcp_change_path_rsp_结构体.md)
- [status](../bluetooth_classic_model_reference/P021_bt_avrcp_change_path_rsp_结构体.md#ae56d599dc7aade35910b894ad464611a)
- [num_items](../bluetooth_classic_model_reference/P021_bt_avrcp_change_path_rsp_结构体.md#a801ddd082bbdbb824943cfd8fd417dea)
- [bt_avrcp_get_item_attrs_cmd](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md)
- [scope](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md#a3d111f69d7cd25de618fc36fc2e054cb)
- [uid](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md#aebe4e58e9b48d6145b66eebf01b86632)
- [uid_counter](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md#ab611ce1a434f4db21899980120c6fc6d)
- [num_attrs](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md#ab08431ab53f8fec8854d85dd695eeb16)
- [attr_ids](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md#a350e99496274adbdc452d69c88aa0691)
- [bt_avrcp_get_item_attrs_rsp](../bluetooth_classic_model_reference/P039_bt_avrcp_get_item_attrs_rsp_结构体.md)
- [status](../bluetooth_classic_model_reference/P039_bt_avrcp_get_item_attrs_rsp_结构体.md#a0e20dc5a812fe5901ba04d772c625903)
- [num_attrs](../bluetooth_classic_model_reference/P039_bt_avrcp_get_item_attrs_rsp_结构体.md#a8911f071972b08d9c190e365f63496ea)
- [attrs](../bluetooth_classic_model_reference/P039_bt_avrcp_get_item_attrs_rsp_结构体.md#a3a9f9dcb6df5de3d0012cd0a33e34a96)
- [bt_avrcp_play_item_rsp](../bluetooth_classic_model_reference/P060_bt_avrcp_play_item_rsp_结构体.md)
- [status](../bluetooth_classic_model_reference/P060_bt_avrcp_play_item_rsp_结构体.md#a36f361a78dbceaac63508fe75ce907b4)
- [bt_avrcp_get_total_number_of_items_cmd](../bluetooth_classic_model_reference/P045_bt_avrcp_get_total_number_of_items_cmd_结构体.md)
- [scope](../bluetooth_classic_model_reference/P045_bt_avrcp_get_total_number_of_items_cmd_结构体.md#a1d6f1eaa83bdaf37a77bffd10f370ca7)
- [bt_avrcp_get_total_number_of_items_rsp](../bluetooth_classic_model_reference/P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md)
- [status](../bluetooth_classic_model_reference/P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md#a7717d866cd7ea275015309b5c8128b2b)
- [uid_counter](../bluetooth_classic_model_reference/P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md#a6f1686ad482eb271bfcdfaf27a7c5f56)
- [num_items](../bluetooth_classic_model_reference/P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md#ab1d378b127df00c87593187a8ec25765)
- [bt_avrcp_search_cmd](../bluetooth_classic_model_reference/P062_bt_avrcp_search_cmd_结构体.md)
- [charset_id](../bluetooth_classic_model_reference/P062_bt_avrcp_search_cmd_结构体.md#aa3b1bda62dc37d4c003ea3b3af9567da)
- [search_str_len](../bluetooth_classic_model_reference/P062_bt_avrcp_search_cmd_结构体.md#a390c55e028e54b1c655d2dc1de35e87c)
- [search_str](../bluetooth_classic_model_reference/P062_bt_avrcp_search_cmd_结构体.md#a953e7210d1d0f8ff2cb86e4742a4af7a)
- [bt_avrcp_search_rsp](../bluetooth_classic_model_reference/P063_bt_avrcp_search_rsp_结构体.md)
- [status](../bluetooth_classic_model_reference/P063_bt_avrcp_search_rsp_结构体.md#abbaacf359228e5c56e8cf4147dafe258)
- [uid_counter](../bluetooth_classic_model_reference/P063_bt_avrcp_search_rsp_结构体.md#ac1dadb58aa8852476a79799af8b8bd1e)
- [num_items](../bluetooth_classic_model_reference/P063_bt_avrcp_search_rsp_结构体.md#ad58679ba2fee9137b3d8c7808b5dfcba)
- [bt_avrcp_folder_name](../bluetooth_classic_model_reference/P030_bt_avrcp_folder_name_结构体.md)
- [folder_name_len](../bluetooth_classic_model_reference/P030_bt_avrcp_folder_name_结构体.md#a54673f0419fa51cee9250e5f5f1487fe)
- [folder_name](../bluetooth_classic_model_reference/P030_bt_avrcp_folder_name_结构体.md#a0c339a18965911d0c3f52af9ae49f5dc)
- [bt_avrcp_set_browsed_player_rsp](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md)
- [status](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a7d07c8595a14800385db33662b3096c5)
- [uid_counter](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a5c0a40b5fbcd85dca0b904a106cfede9)
- [num_items](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a995907daaada393c045265583d0bad92)
- [charset_id](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a61e93ead82b56cb3f61d1337423af05d)
- [folder_depth](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a9c7989c84c89790673a0f25922a72f59)
- [folder_names](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a889cfb87961402d8a41b17292ec89b11)
- [BT_AVRCP_PLAYBACK_STATUS_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a71ddb79b742f9acbd5d14a7639a09fe8)
- [BT_AVRCP_PLAYBACK_STATUS_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1ae620f45ad0ecb63be8a8a0b446b5817a)
- [BT_AVRCP_PLAYBACK_STATUS_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a2509a9b77091db4ff185448d17d44244)
- [BT_AVRCP_PLAYBACK_STATUS_FWD_SEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1ab97050ae05ba6cdff052ac6181eed119)
- [BT_AVRCP_PLAYBACK_STATUS_REV_SEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a5dedf3d49340e3371b118215414aa8d8)
- [BT_AVRCP_PLAYBACK_STATUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga433775fa2758df43ee1d26c78e9122d1a05cd93eef7ee39f8e7111d23131de6de)
- [bt_avrcp_playback_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga433775fa2758df43ee1d26c78e9122d1)
- [BT_AVRCP_SYSTEM_STATUS_POWER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga128458626d5fe6ffbac7cf97867621aaaea875986bd59d1da9650c5d5f2de20a2)
- [BT_AVRCP_SYSTEM_STATUS_POWER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga128458626d5fe6ffbac7cf97867621aaa4d4a454f0b8a0a84b557a4075eff1215)
- [BT_AVRCP_SYSTEM_STATUS_UNPLUGGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga128458626d5fe6ffbac7cf97867621aaa1e1ed998f24038e6095f802144e240c2)
- [bt_avrcp_system_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga128458626d5fe6ffbac7cf97867621aa)
- [BT_AVRCP_BATTERY_STATUS_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77aeaba1597c6c1854d46df1eaaff8862a2)
- [BT_AVRCP_BATTERY_STATUS_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77a4f7cb6c1917180ca96b10d2c73df9fad)
- [BT_AVRCP_BATTERY_STATUS_CRITICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77adafb0292944a3d4236608ca13d900c98)
- [BT_AVRCP_BATTERY_STATUS_EXTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77a2883875f5d5441e7eb7976a38573c178)
- [BT_AVRCP_BATTERY_STATUS_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga33825b183b12a2b29d5148a7366c0e77a72880bd811f5cf87fedfa0ff006412b4)
- [bt_avrcp_battery_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga33825b183b12a2b29d5148a7366c0e77)
- [bt_avrcp_get_element_attrs_cmd](../bluetooth_classic_model_reference/P034_bt_avrcp_get_element_attrs_cmd_结构体.md)
- [identifier](../bluetooth_classic_model_reference/P034_bt_avrcp_get_element_attrs_cmd_结构体.md#a82826b71e51eb7ccc296c753c9d855f3)
- [num_attrs](../bluetooth_classic_model_reference/P034_bt_avrcp_get_element_attrs_cmd_结构体.md#a1404b06ec564c9ae57f3fc6a920b6407)
- [attr_ids](../bluetooth_classic_model_reference/P034_bt_avrcp_get_element_attrs_cmd_结构体.md#a02c96f2e1a1b747a041b663b4532fdc2)
- [bt_avrcp_get_element_attrs_rsp](../bluetooth_classic_model_reference/P035_bt_avrcp_get_element_attrs_rsp_结构体.md)
- [num_attrs](../bluetooth_classic_model_reference/P035_bt_avrcp_get_element_attrs_rsp_结构体.md#ae93d33489d91b07a521055032e88b171)
- [attrs](../bluetooth_classic_model_reference/P035_bt_avrcp_get_element_attrs_rsp_结构体.md#a952a0a601b1dcf69abccaab92ef51eea)
- [BT_AVRCP_PLAYER_ATTR_EQUALIZER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa226313d1f90779c47142ba4966ee968f)
- [BT_AVRCP_PLAYER_ATTR_REPEAT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa4cfad017fc5870b099a8d4521e422dca)
- [BT_AVRCP_PLAYER_ATTR_SHUFFLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa278d43d52aa33cb54705e7d75ddd98b7)
- [BT_AVRCP_PLAYER_ATTR_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8047dddc873566ee372e77c6eecd008fa4157b63056caa15282fab2712a855cec)
- [bt_avrcp_player_attr_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8047dddc873566ee372e77c6eecd008f)
- [BT_AVRCP_EQUALIZER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggae76f2666d10e6f46a1e5d68327fc7607a31587fdac3ae979f111287a924115d4a)
- [BT_AVRCP_EQUALIZER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ggae76f2666d10e6f46a1e5d68327fc7607aed029088c6bb73d0928ec19b9029e95e)
- [bt_avrcp_equalizer_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae76f2666d10e6f46a1e5d68327fc7607)
- [BT_AVRCP_REPEAT_MODE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aa4192bdec6c45e76769ca55ee6a3ab190)
- [BT_AVRCP_REPEAT_MODE_SINGLE_TRACK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aa24914c843056b7fc58f534aec1693948)
- [BT_AVRCP_REPEAT_MODE_ALL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aabf4b962a513c908baa7fac9454511aaa)
- [BT_AVRCP_REPEAT_MODE_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga22bf1b16b383ef473624769ae6ae893aa926fe6e1fc4fee9bb108c9b0c2e46c9a)
- [bt_avrcp_repeat_mode_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga22bf1b16b383ef473624769ae6ae893a)
- [BT_AVRCP_SHUFFLE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8e6ce46ba46268c2c80f4ec7570859c8aac7dce4d43e84c3d80f9eb0791db7a8d)
- [BT_AVRCP_SHUFFLE_ALL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8e6ce46ba46268c2c80f4ec7570859c8ab36d34793768772409794570f740964a)
- [BT_AVRCP_SHUFFLE_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga8e6ce46ba46268c2c80f4ec7570859c8a11a1b2613018ad24861a72313af4189a)
- [bt_avrcp_shuffle_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8e6ce46ba46268c2c80f4ec7570859c8)
- [BT_AVRCP_SCAN_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga4426612c49f8456f2543f373db72d3f2ae12700ce9b55f758572b0fbfab18ea90)
- [BT_AVRCP_SCAN_ALL_TRACKS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga4426612c49f8456f2543f373db72d3f2a0819f5ffd937f0d4a379ae5e7b9a2ebf)
- [BT_AVRCP_SCAN_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gga4426612c49f8456f2543f373db72d3f2abde23c31bbb6ab1c7daf85e3cd977cf9)
- [bt_avrcp_scan_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4426612c49f8456f2543f373db72d3f2)
- [bt_avrcp_list_player_app_setting_attrs_rsp](../bluetooth_classic_model_reference/P050_bt_avrcp_list_player_app_setting_attrs_rsp_结构体.md)
- [num_attrs](../bluetooth_classic_model_reference/P050_bt_avrcp_list_player_app_setting_attrs_rsp_结构体.md#a43432a70ba4acc8e17db8d2effa3c964)
- [attr_ids](../bluetooth_classic_model_reference/P050_bt_avrcp_list_player_app_setting_attrs_rsp_结构体.md#a2e3313ae520d0d174f8b48589f54e355)
- [bt_avrcp_list_player_app_setting_vals_cmd](../bluetooth_classic_model_reference/P051_bt_avrcp_list_player_app_setting_vals_cmd_结构体.md)
- [attr_id](../bluetooth_classic_model_reference/P051_bt_avrcp_list_player_app_setting_vals_cmd_结构体.md#ae5dc4c95f535c3ce721c0f3d4d34fecf)
- [bt_avrcp_list_player_app_setting_vals_rsp](../bluetooth_classic_model_reference/P052_bt_avrcp_list_player_app_setting_vals_rsp_结构体.md)
- [num_values](../bluetooth_classic_model_reference/P052_bt_avrcp_list_player_app_setting_vals_rsp_结构体.md#acf0b62de5a89ea69da09172ca6199535)
- [values](../bluetooth_classic_model_reference/P052_bt_avrcp_list_player_app_setting_vals_rsp_结构体.md#a129bdffa4fbd075371ecf6114c614ea5)
- [bt_avrcp_get_curr_player_app_setting_val_cmd](../bluetooth_classic_model_reference/P032_bt_avrcp_get_curr_player_app_setting_val_cmd_结构体.md)
- [num_attrs](../bluetooth_classic_model_reference/P032_bt_avrcp_get_curr_player_app_setting_val_cmd_结构体.md#a76bbe05f5b05beaa4d9ae65efd8a4c5a)
- [attr_ids](../bluetooth_classic_model_reference/P032_bt_avrcp_get_curr_player_app_setting_val_cmd_结构体.md#a7676edfb915d4468660888f636eb6c4d)
- [bt_avrcp_app_setting_attr_val](../bluetooth_classic_model_reference/P018_bt_avrcp_app_setting_attr_val_结构体.md)
- [attr_id](../bluetooth_classic_model_reference/P018_bt_avrcp_app_setting_attr_val_结构体.md#ab6c7e9c0cf3097fff571cc93e3b2283b)
- [value_id](../bluetooth_classic_model_reference/P018_bt_avrcp_app_setting_attr_val_结构体.md#a0ca2b498edfaa0199973ece7fcf304bc)
- [bt_avrcp_get_curr_player_app_setting_val_rsp](../bluetooth_classic_model_reference/P033_bt_avrcp_get_curr_player_app_setting_val_rsp_结构体.md)
- [num_attrs](../bluetooth_classic_model_reference/P033_bt_avrcp_get_curr_player_app_setting_val_rsp_结构体.md#a1b289cd52db9fa5c34b69f6d68b3312d)
- [attr_vals](../bluetooth_classic_model_reference/P033_bt_avrcp_get_curr_player_app_setting_val_rsp_结构体.md#a6b978fe837d5e082729dd5df013d48a6)
- [bt_avrcp_set_player_app_setting_val_cmd](../bluetooth_classic_model_reference/P068_bt_avrcp_set_player_app_setting_val_cmd_结构体.md)
- [num_attrs](../bluetooth_classic_model_reference/P068_bt_avrcp_set_player_app_setting_val_cmd_结构体.md#a8de91e220969f26121ea08d4e93b11ce)
- [attr_vals](../bluetooth_classic_model_reference/P068_bt_avrcp_set_player_app_setting_val_cmd_结构体.md#a6eda2876b27b4e137ff80bf0283f96ae)
- [bt_avrcp_get_player_app_setting_attr_text_cmd](../bluetooth_classic_model_reference/P041_bt_avrcp_get_player_app_setting_attr_text_cmd_结构体.md)
- [num_attrs](../bluetooth_classic_model_reference/P041_bt_avrcp_get_player_app_setting_attr_text_cmd_结构体.md#a7cec43cbd74ad7f916e76bb63e989eec)
- [attr_ids](../bluetooth_classic_model_reference/P041_bt_avrcp_get_player_app_setting_attr_text_cmd_结构体.md#a8606b94d15d9642f5319ded86ec2eb8c)
- [bt_avrcp_app_setting_attr_text](../bluetooth_classic_model_reference/P017_bt_avrcp_app_setting_attr_text_结构体.md)
- [attr_id](../bluetooth_classic_model_reference/P017_bt_avrcp_app_setting_attr_text_结构体.md#a38306c0921d308a9127befe8b14b2780)
- [charset_id](../bluetooth_classic_model_reference/P017_bt_avrcp_app_setting_attr_text_结构体.md#ac135cdad9f6db11162f11078a5a88f08)
- [text_len](../bluetooth_classic_model_reference/P017_bt_avrcp_app_setting_attr_text_结构体.md#aa2fc3a684134034a6e34b72d8aed2d94)
- [text](../bluetooth_classic_model_reference/P017_bt_avrcp_app_setting_attr_text_结构体.md#a2e3311b3067919aa8feacf24c6a4e37d)
- [bt_avrcp_get_player_app_setting_attr_text_rsp](../bluetooth_classic_model_reference/P042_bt_avrcp_get_player_app_setting_attr_text_rsp_结构体.md)
- [num_attrs](../bluetooth_classic_model_reference/P042_bt_avrcp_get_player_app_setting_attr_text_rsp_结构体.md#a984773df60443fd834e2e381883f4557)
- [attr_text](../bluetooth_classic_model_reference/P042_bt_avrcp_get_player_app_setting_attr_text_rsp_结构体.md#a6eab2bcedb9be8e62ab490a20ecabb20)
- [bt_avrcp_get_player_app_setting_val_text_cmd](../bluetooth_classic_model_reference/P043_bt_avrcp_get_player_app_setting_val_text_cmd_结构体.md)
- [attr_id](../bluetooth_classic_model_reference/P043_bt_avrcp_get_player_app_setting_val_text_cmd_结构体.md#a6d71fc4760fe6a78ce030c256e1d3326)
- [num_values](../bluetooth_classic_model_reference/P043_bt_avrcp_get_player_app_setting_val_text_cmd_结构体.md#af4b5e65b4a22b36c42d8e545c43ebd7e)
- [value_ids](../bluetooth_classic_model_reference/P043_bt_avrcp_get_player_app_setting_val_text_cmd_结构体.md#acad6d1ebe3ae55fb12d29e38d6183640)
- [bt_avrcp_app_setting_val_text](../bluetooth_classic_model_reference/P019_bt_avrcp_app_setting_val_text_结构体.md)
- [value_id](../bluetooth_classic_model_reference/P019_bt_avrcp_app_setting_val_text_结构体.md#a64c7b1c1fdedea5d8979e2f7b2311446)
- [charset_id](../bluetooth_classic_model_reference/P019_bt_avrcp_app_setting_val_text_结构体.md#a1445e315c485a9486339d183db1c76ad)
- [text_len](../bluetooth_classic_model_reference/P019_bt_avrcp_app_setting_val_text_结构体.md#af4d28d332712cd8a07b3dc9e6ee2f0d6)
- [text](../bluetooth_classic_model_reference/P019_bt_avrcp_app_setting_val_text_结构体.md#a880d2c79a341c575f05f380fadaade7c)
- [bt_avrcp_get_player_app_setting_val_text_rsp](../bluetooth_classic_model_reference/P044_bt_avrcp_get_player_app_setting_val_text_rsp_结构体.md)
- [num_values](../bluetooth_classic_model_reference/P044_bt_avrcp_get_player_app_setting_val_text_rsp_结构体.md#a45368c39caa9b87ff8101de5801807c3)
- [value_text](../bluetooth_classic_model_reference/P044_bt_avrcp_get_player_app_setting_val_text_rsp_结构体.md#a49b1ebb7ebce5ccc9f7d5e77f79f107c)
- [bt_avrcp_inform_displayable_char_set_cmd](../bluetooth_classic_model_reference/P048_bt_avrcp_inform_displayable_char_set_cmd_结构体.md)
- [num_charsets](../bluetooth_classic_model_reference/P048_bt_avrcp_inform_displayable_char_set_cmd_结构体.md#a157b2006ac2032335cc75cf14a6b4849)
- [charset_ids](../bluetooth_classic_model_reference/P048_bt_avrcp_inform_displayable_char_set_cmd_结构体.md#a1c283439e475592935395c90b372233f)
- [bt_avrcp_inform_batt_status_of_ct_cmd](../bluetooth_classic_model_reference/P047_bt_avrcp_inform_batt_status_of_ct_cmd_结构体.md)
- [battery_status](../bluetooth_classic_model_reference/P047_bt_avrcp_inform_batt_status_of_ct_cmd_结构体.md#ae79067d210d7484c18adc3570ec20af1)
- [bt_avrcp_get_play_status_rsp](../bluetooth_classic_model_reference/P040_bt_avrcp_get_play_status_rsp_结构体.md)
- [song_length](../bluetooth_classic_model_reference/P040_bt_avrcp_get_play_status_rsp_结构体.md#a51c7a55875e13bb8ff442d8deef0963c)
- [song_position](../bluetooth_classic_model_reference/P040_bt_avrcp_get_play_status_rsp_结构体.md#a22ca5e4357d8c92cb690995973964b88)
- [play_status](../bluetooth_classic_model_reference/P040_bt_avrcp_get_play_status_rsp_结构体.md#a1a2d2ba12925e8424da262a5d2698beb)
- [bt_avrcp_register_notification_cmd](../bluetooth_classic_model_reference/P061_bt_avrcp_register_notification_cmd_结构体.md)
- [event_id](../bluetooth_classic_model_reference/P061_bt_avrcp_register_notification_cmd_结构体.md#a631509c0abadf1f4f2bdf5a5c58f0b80)
- [interval](../bluetooth_classic_model_reference/P061_bt_avrcp_register_notification_cmd_结构体.md#a3bc85acb4c0b45be4fc082890f9fa744)
- [bt_avrcp_set_absolute_volume_cmd](../bluetooth_classic_model_reference/P064_bt_avrcp_set_absolute_volume_cmd_结构体.md)
- [absolute_volume](../bluetooth_classic_model_reference/P064_bt_avrcp_set_absolute_volume_cmd_结构体.md#adc69d9de75995fdd1658b38d50566ec4)
- [bt_avrcp_set_absolute_volume_rsp](../bluetooth_classic_model_reference/P065_bt_avrcp_set_absolute_volume_rsp_结构体.md)
- [absolute_volume](../bluetooth_classic_model_reference/P065_bt_avrcp_set_absolute_volume_rsp_结构体.md#ae542d562193e9b42e14b04b7a91f1500)
- [bt_avrcp_set_addressed_player_cmd](../bluetooth_classic_model_reference/P066_bt_avrcp_set_addressed_player_cmd_结构体.md)
- [player_id](../bluetooth_classic_model_reference/P066_bt_avrcp_set_addressed_player_cmd_结构体.md#a0cb667cb10375fcd16570fd3fbda20d7)
- [bt_avrcp_play_item_cmd](../bluetooth_classic_model_reference/P059_bt_avrcp_play_item_cmd_结构体.md)
- [scope](../bluetooth_classic_model_reference/P059_bt_avrcp_play_item_cmd_结构体.md#a80ca2390bfa44bf2509161f4c6a5421a)
- [uid](../bluetooth_classic_model_reference/P059_bt_avrcp_play_item_cmd_结构体.md#aebf33c2d1fa1a2574c485f777f114c0a)
- [uid_counter](../bluetooth_classic_model_reference/P059_bt_avrcp_play_item_cmd_结构体.md#ad2fa5d9e38a3ef5edc4430749ed13515)
- [bt_avrcp_add_to_now_playing_cmd](../bluetooth_classic_model_reference/P016_bt_avrcp_add_to_now_playing_cmd_结构体.md)
- [scope](../bluetooth_classic_model_reference/P016_bt_avrcp_add_to_now_playing_cmd_结构体.md#af0676fbaab14bfd3e3330c3c1ea701c5)
- [uid](../bluetooth_classic_model_reference/P016_bt_avrcp_add_to_now_playing_cmd_结构体.md#ad73c5b034f7017f05ee3c491bf8bdc10)
- [uid_counter](../bluetooth_classic_model_reference/P016_bt_avrcp_add_to_now_playing_cmd_结构体.md#a0dd07ff85b7cedcc8b20dfddf3ed5d91)
- [bt_avrcp_event_data](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md)
- [play_status](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#aed5c7ed3f0a1cc935544cf12ee0dcda9)
- [identifier](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#a4aae90303b04cab680045b88a636e22a)
- [playback_pos](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#adf71db04b3c1821ceafe0e1071af5c38)
- [battery_status](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#ae47d1a2379088e929bfb44df7c172511)
- [system_status](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#a5eeea0ad88794d23965a83e68c93015f)
- [num_of_attr](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#a77e7bb507e86be528ad40cbae329c7fc)
- [attr_vals](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#ae7f5a7e755f7dfd6d1d962e9df5ca716)
- [setting_changed](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#ad23631ca5ca2dd4dd33ba3b76f281c44)
- [player_id](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#ae5a21b8f540b69791b65e2ec565c876e)
- [uid_counter](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#a9c650742790ded89f1a9c583a22b7895)
- [addressed_player_changed](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#a5471d42d0e9a589690304811028931c4)
- [absolute_volume](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#af8aadd59a58de168cba94cdfa22549db)
- [bt_avrcp_notify_changed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab9bd888ef5443bd0a3d34a34b972f409)
- [bt_avrcp_ct_cb](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md)
- [connected](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a134720ca0e05d4e6c893f391ca842344)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [disconnected](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#aae8977ac1f58e40bbf52c1c52e571395)
- [browsing_connected](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a3035cc2cace9a3e8d463d54c72dd1fed)
- [browsing_disconnected](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ae92ce375dd6cff3b2b719b39b02e99af)
- [get_caps](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a15e7780c8c5c4037434c2ab20f47a8f6)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [unit_info_rsp](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ac842ad673b8a943e9f1b188346b8d92d)
- [subunit_info_rsp](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a4e33bc54f28204959ccd4fa2c766980d)
- [passthrough_rsp](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a69ab87eb920eae066034054e7bf89c7b)
- [set_browsed_player](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a768c099504dd24ee67556f69b493ddb0)
- [get_folder_items](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a2350f1a00f68008b73ca1400f8954b4b)
- [change_path](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#afc0ef62c71331961f3196bc2668f4dbb)
- [get_item_attrs](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ad7b512d997a5326cee867651ad7cbfaf)
- [get_total_number_of_items](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a4b74108af0ab8cb0119af8c477ff9b33)
- [search](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a0e361f81921ae80e89947e1ede29b66c)
- [browsing_general_reject](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a81e9799d9efe9133dedd91386e49960c)
- [notification](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a0c8b90004b116751f94b2c5c1af02af8)
- [list_player_app_setting_attrs](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a3c37bfd2f03a8c76a725b38210794e21)
- [list_player_app_setting_vals](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a8b16ac730eb5c9dc95e7c3e660f802cc)
- [get_curr_player_app_setting_val](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ac5fd1a8d9927edbd56cb24f8760c8401)
- [set_player_app_setting_val](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a5990204dc0d6b0437308e69eef8f7f47)
- [get_player_app_setting_attr_text](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a02a9fa26f9827f327b6030758c539210)
- [get_player_app_setting_val_text](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ac41f9cfa20c1b1a092515b345b468a10)
- [inform_displayable_char_set](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a80f78ad02b0b7e9db9de19a0dceeea50)
- [inform_batt_status_of_ct](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a1b88debebdf19263d760f9f8e3d447d6)
- [set_absolute_volume](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ad102ac42003f1013b14809c4dd1057a4)
- [get_element_attrs](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#accb0eaa7ae05c888b963278fe320c17c)
- [get_play_status](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ac25d85d11c28d64225b42a6e5f3fa3ce)
- [set_addressed_player](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a6748f42e5ba39a1a6b2d7a50729c0316)
- [play_item](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a7ae520df749b156f9875cf3e6ee62a96)
- [add_to_now_playing](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ae5f09e516a212e97c36e0c32074c9477)
- [bt_avrcp_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga6a212dd4765adc82eda6e35cd9742f0c)
- [bt_avrcp_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7ec468b9a50413ba478186c88728e13b)
- [bt_avrcp_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac3ccb5386c756bc2688ee5d4499aa29b)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bt_avrcp_create_vendor_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad0207b2d16d616b628e7bd2dd7fe4e41)
- [bt_avrcp_browsing_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac66d9b3fc6352e66716da3e10b25ccdb)
- [bt_avrcp_browsing_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaa00ea2046f2fe87676fe990e0d34de8b)
- [bt_avrcp_ct_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7129d3dc93ea77140ae192099f4a4f92)
- [bt_avrcp_ct_get_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga311233e84ef1c0fc8c28baacbb77b831)
- [bt_avrcp_ct_get_unit_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga0d59de3bbcfd036f267354fa4ee290dd)
- [bt_avrcp_ct_get_subunit_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4ddceec722d768a0f0c86b3701e0e693)
- [bt_avrcp_ct_passthrough](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga16f8e224bc80ed0bca5ce04a93670320)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [bt_avrcp_ct_set_browsed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab0886ea325dddc67167bed86ec6c31e9)
- [bt_avrcp_ct_register_notification](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab2e6565627deefd8dc5c79a08d02aa85)
- [bt_avrcp_ct_list_player_app_setting_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadfafc60888e73a92c1d16fe9696565df)
- [bt_avrcp_ct_list_player_app_setting_vals](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga11f34256317663cec599d7cb1b250243)
- [bt_avrcp_ct_get_curr_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga232182eaa8d04921d85a68e35268212e)
- [bt_avrcp_ct_set_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga962f7727f10ca2827c60d4d9a5dd2bde)
- [bt_avrcp_ct_get_player_app_setting_attr_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga197fc46b498c5d4f52e4868bb85480b9)
- [bt_avrcp_ct_get_player_app_setting_val_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaccbb023e5051601e27ab1ca193152f7b)
- [bt_avrcp_ct_inform_displayable_char_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab268d545750bd22b0625779d735d344a)
- [bt_avrcp_ct_inform_batt_status_of_ct](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae8cb7f3d8dbb8ae91167916e5c99ec39)
- [bt_avrcp_ct_set_absolute_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga27b0a9e2d86fcc91d2e7b19f1bc5df2d)
- [bt_avrcp_ct_get_element_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaf5b49460a1037b0f146e7b16d89215e1)
- [bt_avrcp_ct_get_play_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga014c353ff7f2fc54eefad6a6e20112ec)
- [bt_avrcp_ct_set_addressed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga69561453ade3e8ba07b2122efcddcfad)
- [bt_avrcp_ct_play_item](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab8d46ac46d35b711209f9a8572c1f8bd)
- [bt_avrcp_ct_add_to_now_playing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7e997ce46f322887227623b43e84ff28)
- [bt_avrcp_ct_get_folder_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad77454a6d56942ffe57d5b716f7aa39d)
- [bt_avrcp_ct_change_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab8730a40ab9bc208a53a035243b8cb1b)
- [bt_avrcp_ct_get_item_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4ae38864d35a66a306ced13544e442d4)
- [bt_avrcp_ct_get_total_number_of_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadef2624ec50c0bb138d7eae8525784c5)
- [bt_avrcp_ct_search](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab8b765fab76ba2585730f328c0abc167)
- [bt_avrcp_tg_cb](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md)
- [connected](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a8f0994f1b59d16ef74a7430221f53db0)
- [disconnected](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a9c64cc44157e6cedec9decc00f0022b3)
- [unit_info_req](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a933eb30910fef1e916e60ff21d4255ec)
- [register_notification](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a45954c3a1f3e8dffb1bc111845c875ce)
- [subunit_info_req](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ab9f1a086a71522986808f3ebc2cbd2de)
- [get_caps](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ab3fe452afec12ff31975763c5269c94f)
- [browsing_connected](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a82c5ca1100844e5119224aa6bac19bd2)
- [browsing_disconnected](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ad66a2945e2cb464bf7324a0685106d47)
- [set_browsed_player](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a4179686bbe4030c44f0a277532dcb96b)
- [get_folder_items](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a0f117772eb0f55e20214b0be8d93a6fa)
- [change_path](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a37d8a221b66cf3bad74790532b559cff)
- [get_item_attrs](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a878eaaf2358b0773e964dc68c910a377)
- [get_total_number_of_items](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ae5a45a624cf6d9224aca975260e954c8)
- [search](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a8442f74b35a70c88defe84e948ced8d6)
- [passthrough_req](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a48b25910cffb470139e2a562b15802ce)
- [list_player_app_setting_attrs](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ae496f717332ea6a42507e3772793ba0e)
- [list_player_app_setting_vals](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#acd0d716aa960230b3e8f7c5c0bdb9b19)
- [get_curr_player_app_setting_val](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a51caea0e045788bbce8073f720eb7e19)
- [set_player_app_setting_val](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a19308d4734cdd9bf397f7ba721920e97)
- [get_player_app_setting_attr_text](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a20215fb3b4bb2d7c73f2d08ac3e801ec)
- [get_player_app_setting_val_text](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a64bf13cf36066568ecbbe1006c717970)
- [inform_displayable_char_set](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ad8701332c6415915d32454788772dd09)
- [inform_batt_status_of_ct](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a883db478d1a35f0fe61f867d78366c91)
- [get_element_attrs](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#adf7e869f632ebc1ccbe7d8213a7c4f05)
- [set_absolute_volume](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a2f022902183a0db38c65a41fdc0a8478)
- [get_play_status](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a889d781b5275ca24bf0603c370bb2a4e)
- [set_addressed_player](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a1ab779d9b5142590f9dcb42990d9d3cb)
- [play_item](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#af07da9dc841518013c6f6a1796f957f1)
- [add_to_now_playing](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a6946e152d68e5650f683ed6a449709d7)
- [bt_avrcp_tg_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga7ba6030ff079e3c47bf6e5838b61ebdb)
- [bt_avrcp_tg_send_unit_info_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaecb26512e8b1d267bca0d3ea01438c9b)
- [bt_avrcp_tg_send_subunit_info_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gabc170c5c0aa39827b4efc43880dbf258)
- [bt_avrcp_tg_get_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad160c86f1647509e10d741284b9bbb03)
- [bt_avrcp_tg_notification](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga1ef0065fd9fa73bcd03491fe700fac65)
- [data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [bt_avrcp_tg_set_browsed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga15bf2602f37ef83b3bcefd85920658eb)
- [bt_avrcp_tg_send_passthrough_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac92854e7f567f6088a5cf3ad3c209343)
- [bt_avrcp_tg_list_player_app_setting_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab442ef3962bebd8dbe0d5681498f8453)
- [bt_avrcp_tg_list_player_app_setting_vals](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gae8b42aada8be4c9fac13fbd90e751a7b)
- [bt_avrcp_tg_get_curr_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gab18ce4d9348698272eedff52ddb3052e)
- [bt_avrcp_tg_set_player_app_setting_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga9d471d9a932dfd43b71e894ddec013b4)
- [bt_avrcp_tg_get_player_app_setting_attr_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga123f5528b62f48faaf020f19dcc321c1)
- [bt_avrcp_tg_get_player_app_setting_val_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga8cc324a60a3480524336bc399d62c1ed)
- [bt_avrcp_tg_inform_displayable_char_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadda57eb5c28f6b77bda5efe9286bc5f4)
- [bt_avrcp_tg_inform_batt_status_of_ct](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaa2aca5a011a99a20a3bd3fd7154a864a)
- [bt_avrcp_tg_absolute_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gad0d937d50eccfbedc81cc575a3e238f2)
- [bt_avrcp_tg_get_element_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81333eaee7ca1838424ce9b513e6e2c5)
- [bt_avrcp_tg_get_play_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga4f37f0c696ea98f44bd5e8ce2905d9f4)
- [bt_avrcp_tg_set_addressed_player](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gadcf3f892a1d492a2743cdb4f8d205505)
- [bt_avrcp_tg_play_item](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga5f72112c0887ed3efc3455ead567126d)
- [bt_avrcp_tg_add_to_now_playing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gafc84238ea566bef4d2789e7cdba193dd)
- [bt_avrcp_tg_get_folder_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga6261635bf3925766bb7af10696df6fd5)
- [bt_avrcp_tg_change_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga851b0c30ac0b382658b5ce040d7755eb)
- [bt_avrcp_tg_get_item_attrs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga509746020e487d769f94174a4071b673)
- [bt_avrcp_tg_get_total_number_of_items](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaf521ea00d597fced528d86befd9b5bbb)
- [bt_avrcp_tg_search](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga136fda008bf5d5f7e9cad3855a4173f9)
- [bt_avrcp_tg_browsing_general_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gaad6d011fe84aaa6cec8665aa87d4cc41)
- [bt_avrcp_add_to_now_playing_cmd::uid_counter](../bluetooth_classic_model_reference/P016_bt_avrcp_add_to_now_playing_cmd_结构体.md#a0dd07ff85b7cedcc8b20dfddf3ed5d91)
- [bt_avrcp_add_to_now_playing_cmd::uid](../bluetooth_classic_model_reference/P016_bt_avrcp_add_to_now_playing_cmd_结构体.md#ad73c5b034f7017f05ee3c491bf8bdc10)
- [bt_avrcp_add_to_now_playing_cmd::scope](../bluetooth_classic_model_reference/P016_bt_avrcp_add_to_now_playing_cmd_结构体.md#af0676fbaab14bfd3e3330c3c1ea701c5)
- [bt_avrcp_app_setting_attr_text::text](../bluetooth_classic_model_reference/P017_bt_avrcp_app_setting_attr_text_结构体.md#a2e3311b3067919aa8feacf24c6a4e37d)
- [bt_avrcp_app_setting_attr_text::attr_id](../bluetooth_classic_model_reference/P017_bt_avrcp_app_setting_attr_text_结构体.md#a38306c0921d308a9127befe8b14b2780)
- [bt_avrcp_app_setting_attr_text::text_len](../bluetooth_classic_model_reference/P017_bt_avrcp_app_setting_attr_text_结构体.md#aa2fc3a684134034a6e34b72d8aed2d94)
- [bt_avrcp_app_setting_attr_text::charset_id](../bluetooth_classic_model_reference/P017_bt_avrcp_app_setting_attr_text_结构体.md#ac135cdad9f6db11162f11078a5a88f08)
- [bt_avrcp_app_setting_attr_val::value_id](../bluetooth_classic_model_reference/P018_bt_avrcp_app_setting_attr_val_结构体.md#a0ca2b498edfaa0199973ece7fcf304bc)
- [bt_avrcp_app_setting_attr_val::attr_id](../bluetooth_classic_model_reference/P018_bt_avrcp_app_setting_attr_val_结构体.md#ab6c7e9c0cf3097fff571cc93e3b2283b)
- [bt_avrcp_app_setting_val_text::charset_id](../bluetooth_classic_model_reference/P019_bt_avrcp_app_setting_val_text_结构体.md#a1445e315c485a9486339d183db1c76ad)
- [bt_avrcp_app_setting_val_text::value_id](../bluetooth_classic_model_reference/P019_bt_avrcp_app_setting_val_text_结构体.md#a64c7b1c1fdedea5d8979e2f7b2311446)
- [bt_avrcp_app_setting_val_text::text](../bluetooth_classic_model_reference/P019_bt_avrcp_app_setting_val_text_结构体.md#a880d2c79a341c575f05f380fadaade7c)
- [bt_avrcp_app_setting_val_text::text_len](../bluetooth_classic_model_reference/P019_bt_avrcp_app_setting_val_text_结构体.md#af4d28d332712cd8a07b3dc9e6ee2f0d6)
- [bt_avrcp_change_path_cmd::folder_uid](../bluetooth_classic_model_reference/P020_bt_avrcp_change_path_cmd_结构体.md#a026e337b5bcf6f827f32314eabd19832)
- [bt_avrcp_change_path_cmd::direction](../bluetooth_classic_model_reference/P020_bt_avrcp_change_path_cmd_结构体.md#a1ced4e12dd7d1c3b31213dce355cf165)
- [bt_avrcp_change_path_cmd::uid_counter](../bluetooth_classic_model_reference/P020_bt_avrcp_change_path_cmd_结构体.md#ac575ced16bc5e61043b035b406f732a4)
- [bt_avrcp_change_path_rsp::num_items](../bluetooth_classic_model_reference/P021_bt_avrcp_change_path_rsp_结构体.md#a801ddd082bbdbb824943cfd8fd417dea)
- [bt_avrcp_change_path_rsp::status](../bluetooth_classic_model_reference/P021_bt_avrcp_change_path_rsp_结构体.md#ae56d599dc7aade35910b894ad464611a)
- [bt_avrcp_ct_cb::get_player_app_setting_attr_text](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a02a9fa26f9827f327b6030758c539210)
- [bt_avrcp_ct_cb::notification](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a0c8b90004b116751f94b2c5c1af02af8)
- [bt_avrcp_ct_cb::search](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a0e361f81921ae80e89947e1ede29b66c)
- [bt_avrcp_ct_cb::connected](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a134720ca0e05d4e6c893f391ca842344)
- [bt_avrcp_ct_cb::get_caps](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a15e7780c8c5c4037434c2ab20f47a8f6)
- [bt_avrcp_ct_cb::inform_batt_status_of_ct](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a1b88debebdf19263d760f9f8e3d447d6)
- [bt_avrcp_ct_cb::get_folder_items](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a2350f1a00f68008b73ca1400f8954b4b)
- [bt_avrcp_ct_cb::browsing_connected](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a3035cc2cace9a3e8d463d54c72dd1fed)
- [bt_avrcp_ct_cb::list_player_app_setting_attrs](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a3c37bfd2f03a8c76a725b38210794e21)
- [bt_avrcp_ct_cb::get_total_number_of_items](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a4b74108af0ab8cb0119af8c477ff9b33)
- [bt_avrcp_ct_cb::subunit_info_rsp](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a4e33bc54f28204959ccd4fa2c766980d)
- [bt_avrcp_ct_cb::set_player_app_setting_val](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a5990204dc0d6b0437308e69eef8f7f47)
- [bt_avrcp_ct_cb::set_addressed_player](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a6748f42e5ba39a1a6b2d7a50729c0316)
- [bt_avrcp_ct_cb::passthrough_rsp](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a69ab87eb920eae066034054e7bf89c7b)
- [bt_avrcp_ct_cb::set_browsed_player](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a768c099504dd24ee67556f69b493ddb0)
- [bt_avrcp_ct_cb::play_item](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a7ae520df749b156f9875cf3e6ee62a96)
- [bt_avrcp_ct_cb::inform_displayable_char_set](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a80f78ad02b0b7e9db9de19a0dceeea50)
- [bt_avrcp_ct_cb::browsing_general_reject](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a81e9799d9efe9133dedd91386e49960c)
- [bt_avrcp_ct_cb::list_player_app_setting_vals](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#a8b16ac730eb5c9dc95e7c3e660f802cc)
- [bt_avrcp_ct_cb::disconnected](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#aae8977ac1f58e40bbf52c1c52e571395)
- [bt_avrcp_ct_cb::get_play_status](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ac25d85d11c28d64225b42a6e5f3fa3ce)
- [bt_avrcp_ct_cb::get_player_app_setting_val_text](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ac41f9cfa20c1b1a092515b345b468a10)
- [bt_avrcp_ct_cb::get_curr_player_app_setting_val](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ac5fd1a8d9927edbd56cb24f8760c8401)
- [bt_avrcp_ct_cb::unit_info_rsp](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ac842ad673b8a943e9f1b188346b8d92d)
- [bt_avrcp_ct_cb::get_element_attrs](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#accb0eaa7ae05c888b963278fe320c17c)
- [bt_avrcp_ct_cb::set_absolute_volume](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ad102ac42003f1013b14809c4dd1057a4)
- [bt_avrcp_ct_cb::get_item_attrs](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ad7b512d997a5326cee867651ad7cbfaf)
- [bt_avrcp_ct_cb::add_to_now_playing](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ae5f09e516a212e97c36e0c32074c9477)
- [bt_avrcp_ct_cb::browsing_disconnected](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#ae92ce375dd6cff3b2b719b39b02e99af)
- [bt_avrcp_ct_cb::change_path](../bluetooth_classic_model_reference/P027_bt_avrcp_ct_cb_结构体.md#afc0ef62c71331961f3196bc2668f4dbb)
- [bt_avrcp_event_data::identifier](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#a4aae90303b04cab680045b88a636e22a)
- [bt_avrcp_event_data::addressed_player_changed](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#a5471d42d0e9a589690304811028931c4)
- [bt_avrcp_event_data::system_status](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#a5eeea0ad88794d23965a83e68c93015f)
- [bt_avrcp_event_data::num_of_attr](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#a77e7bb507e86be528ad40cbae329c7fc)
- [bt_avrcp_event_data::uid_counter](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#a9c650742790ded89f1a9c583a22b7895)
- [bt_avrcp_event_data::setting_changed](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#ad23631ca5ca2dd4dd33ba3b76f281c44)
- [bt_avrcp_event_data::playback_pos](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#adf71db04b3c1821ceafe0e1071af5c38)
- [bt_avrcp_event_data::battery_status](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#ae47d1a2379088e929bfb44df7c172511)
- [bt_avrcp_event_data::player_id](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#ae5a21b8f540b69791b65e2ec565c876e)
- [bt_avrcp_event_data::attr_vals](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#ae7f5a7e755f7dfd6d1d962e9df5ca716)
- [bt_avrcp_event_data::play_status](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#aed5c7ed3f0a1cc935544cf12ee0dcda9)
- [bt_avrcp_event_data::absolute_volume](../bluetooth_classic_model_reference/P028_bt_avrcp_event_data_结构体.md#af8aadd59a58de168cba94cdfa22549db)
- [bt_avrcp_folder_item::playable](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#a168cb4f00af9685d8b9023b09f5dcbe2)
- [bt_avrcp_folder_item::name](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#a682d5d56c49f82e04a812249042353ca)
- [bt_avrcp_folder_item::hdr](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#a8bfa3c0f6854961df4378f0cbe4918e4)
- [bt_avrcp_folder_item::name_len](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#a99a9de89c0d2e7f1b95f80f245e4126c)
- [bt_avrcp_folder_item::uid](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#ab6cd2f27e38730e3137dd739f4483585)
- [bt_avrcp_folder_item::charset_id](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#ab6fa897bd3c15801955592c972220391)
- [bt_avrcp_folder_item::folder_type](../bluetooth_classic_model_reference/P029_bt_avrcp_folder_item_结构体.md#abeb5d94d8a9f91be8769403b6f360991)
- [bt_avrcp_folder_name::folder_name](../bluetooth_classic_model_reference/P030_bt_avrcp_folder_name_结构体.md#a0c339a18965911d0c3f52af9ae49f5dc)
- [bt_avrcp_folder_name::folder_name_len](../bluetooth_classic_model_reference/P030_bt_avrcp_folder_name_结构体.md#a54673f0419fa51cee9250e5f5f1487fe)
- [bt_avrcp_get_caps_rsp::cap_cnt](../bluetooth_classic_model_reference/P031_bt_avrcp_get_caps_rsp_结构体.md#a1f588c2e4204c2f43c4872ee9d6ff6b1)
- [bt_avrcp_get_caps_rsp::cap_id](../bluetooth_classic_model_reference/P031_bt_avrcp_get_caps_rsp_结构体.md#a587d32dcd5abe2e1751a75bcc4bbe5b2)
- [bt_avrcp_get_caps_rsp::cap](../bluetooth_classic_model_reference/P031_bt_avrcp_get_caps_rsp_结构体.md#a8a4c9b7c09cf3db137431ff788006e87)
- [bt_avrcp_get_curr_player_app_setting_val_cmd::attr_ids](../bluetooth_classic_model_reference/P032_bt_avrcp_get_curr_player_app_setting_val_cmd_结构体.md#a7676edfb915d4468660888f636eb6c4d)
- [bt_avrcp_get_curr_player_app_setting_val_cmd::num_attrs](../bluetooth_classic_model_reference/P032_bt_avrcp_get_curr_player_app_setting_val_cmd_结构体.md#a76bbe05f5b05beaa4d9ae65efd8a4c5a)
- [bt_avrcp_get_curr_player_app_setting_val_rsp::num_attrs](../bluetooth_classic_model_reference/P033_bt_avrcp_get_curr_player_app_setting_val_rsp_结构体.md#a1b289cd52db9fa5c34b69f6d68b3312d)
- [bt_avrcp_get_curr_player_app_setting_val_rsp::attr_vals](../bluetooth_classic_model_reference/P033_bt_avrcp_get_curr_player_app_setting_val_rsp_结构体.md#a6b978fe837d5e082729dd5df013d48a6)
- [bt_avrcp_get_element_attrs_cmd::attr_ids](../bluetooth_classic_model_reference/P034_bt_avrcp_get_element_attrs_cmd_结构体.md#a02c96f2e1a1b747a041b663b4532fdc2)
- [bt_avrcp_get_element_attrs_cmd::num_attrs](../bluetooth_classic_model_reference/P034_bt_avrcp_get_element_attrs_cmd_结构体.md#a1404b06ec564c9ae57f3fc6a920b6407)
- [bt_avrcp_get_element_attrs_cmd::identifier](../bluetooth_classic_model_reference/P034_bt_avrcp_get_element_attrs_cmd_结构体.md#a82826b71e51eb7ccc296c753c9d855f3)
- [bt_avrcp_get_element_attrs_rsp::attrs](../bluetooth_classic_model_reference/P035_bt_avrcp_get_element_attrs_rsp_结构体.md#a952a0a601b1dcf69abccaab92ef51eea)
- [bt_avrcp_get_element_attrs_rsp::num_attrs](../bluetooth_classic_model_reference/P035_bt_avrcp_get_element_attrs_rsp_结构体.md#ae93d33489d91b07a521055032e88b171)
- [bt_avrcp_get_folder_items_cmd::attr_count](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md#a7068f5115cf58c075f1deefbb10e4627)
- [bt_avrcp_get_folder_items_cmd::attr_ids](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md#a790f3718f2e6e3d32d1824794a146e4e)
- [bt_avrcp_get_folder_items_cmd::end_item](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md#abf2e154d28317043a88ea00475d777a2)
- [bt_avrcp_get_folder_items_cmd::start_item](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md#ae362914e3f3be32d6381035176431c88)
- [bt_avrcp_get_folder_items_cmd::scope](../bluetooth_classic_model_reference/P036_bt_avrcp_get_folder_items_cmd_结构体.md#af89fb8a745c45a3b768d16d93d5d4287)
- [bt_avrcp_get_folder_items_rsp::items](../bluetooth_classic_model_reference/P037_bt_avrcp_get_folder_items_rsp_结构体.md#a073136a279ed9b5f2aaf9db8c6f17607)
- [bt_avrcp_get_folder_items_rsp::num_items](../bluetooth_classic_model_reference/P037_bt_avrcp_get_folder_items_rsp_结构体.md#a0b95f4d78a16bea65f18690f0081e099)
- [bt_avrcp_get_folder_items_rsp::uid_counter](../bluetooth_classic_model_reference/P037_bt_avrcp_get_folder_items_rsp_结构体.md#a387d5ed3a962e27632821505fd6f0b03)
- [bt_avrcp_get_folder_items_rsp::status](../bluetooth_classic_model_reference/P037_bt_avrcp_get_folder_items_rsp_结构体.md#a7ef2c44e62e2e35b86db3398a84fa88c)
- [bt_avrcp_get_item_attrs_cmd::attr_ids](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md#a350e99496274adbdc452d69c88aa0691)
- [bt_avrcp_get_item_attrs_cmd::scope](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md#a3d111f69d7cd25de618fc36fc2e054cb)
- [bt_avrcp_get_item_attrs_cmd::num_attrs](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md#ab08431ab53f8fec8854d85dd695eeb16)
- [bt_avrcp_get_item_attrs_cmd::uid_counter](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md#ab611ce1a434f4db21899980120c6fc6d)
- [bt_avrcp_get_item_attrs_cmd::uid](../bluetooth_classic_model_reference/P038_bt_avrcp_get_item_attrs_cmd_结构体.md#aebe4e58e9b48d6145b66eebf01b86632)
- [bt_avrcp_get_item_attrs_rsp::status](../bluetooth_classic_model_reference/P039_bt_avrcp_get_item_attrs_rsp_结构体.md#a0e20dc5a812fe5901ba04d772c625903)
- [bt_avrcp_get_item_attrs_rsp::attrs](../bluetooth_classic_model_reference/P039_bt_avrcp_get_item_attrs_rsp_结构体.md#a3a9f9dcb6df5de3d0012cd0a33e34a96)
- [bt_avrcp_get_item_attrs_rsp::num_attrs](../bluetooth_classic_model_reference/P039_bt_avrcp_get_item_attrs_rsp_结构体.md#a8911f071972b08d9c190e365f63496ea)
- [bt_avrcp_get_play_status_rsp::play_status](../bluetooth_classic_model_reference/P040_bt_avrcp_get_play_status_rsp_结构体.md#a1a2d2ba12925e8424da262a5d2698beb)
- [bt_avrcp_get_play_status_rsp::song_position](../bluetooth_classic_model_reference/P040_bt_avrcp_get_play_status_rsp_结构体.md#a22ca5e4357d8c92cb690995973964b88)
- [bt_avrcp_get_play_status_rsp::song_length](../bluetooth_classic_model_reference/P040_bt_avrcp_get_play_status_rsp_结构体.md#a51c7a55875e13bb8ff442d8deef0963c)
- [bt_avrcp_get_player_app_setting_attr_text_cmd::num_attrs](../bluetooth_classic_model_reference/P041_bt_avrcp_get_player_app_setting_attr_text_cmd_结构体.md#a7cec43cbd74ad7f916e76bb63e989eec)
- [bt_avrcp_get_player_app_setting_attr_text_cmd::attr_ids](../bluetooth_classic_model_reference/P041_bt_avrcp_get_player_app_setting_attr_text_cmd_结构体.md#a8606b94d15d9642f5319ded86ec2eb8c)
- [bt_avrcp_get_player_app_setting_attr_text_rsp::attr_text](../bluetooth_classic_model_reference/P042_bt_avrcp_get_player_app_setting_attr_text_rsp_结构体.md#a6eab2bcedb9be8e62ab490a20ecabb20)
- [bt_avrcp_get_player_app_setting_attr_text_rsp::num_attrs](../bluetooth_classic_model_reference/P042_bt_avrcp_get_player_app_setting_attr_text_rsp_结构体.md#a984773df60443fd834e2e381883f4557)
- [bt_avrcp_get_player_app_setting_val_text_cmd::attr_id](../bluetooth_classic_model_reference/P043_bt_avrcp_get_player_app_setting_val_text_cmd_结构体.md#a6d71fc4760fe6a78ce030c256e1d3326)
- [bt_avrcp_get_player_app_setting_val_text_cmd::value_ids](../bluetooth_classic_model_reference/P043_bt_avrcp_get_player_app_setting_val_text_cmd_结构体.md#acad6d1ebe3ae55fb12d29e38d6183640)
- [bt_avrcp_get_player_app_setting_val_text_cmd::num_values](../bluetooth_classic_model_reference/P043_bt_avrcp_get_player_app_setting_val_text_cmd_结构体.md#af4b5e65b4a22b36c42d8e545c43ebd7e)
- [bt_avrcp_get_player_app_setting_val_text_rsp::num_values](../bluetooth_classic_model_reference/P044_bt_avrcp_get_player_app_setting_val_text_rsp_结构体.md#a45368c39caa9b87ff8101de5801807c3)
- [bt_avrcp_get_player_app_setting_val_text_rsp::value_text](../bluetooth_classic_model_reference/P044_bt_avrcp_get_player_app_setting_val_text_rsp_结构体.md#a49b1ebb7ebce5ccc9f7d5e77f79f107c)
- [bt_avrcp_get_total_number_of_items_cmd::scope](../bluetooth_classic_model_reference/P045_bt_avrcp_get_total_number_of_items_cmd_结构体.md#a1d6f1eaa83bdaf37a77bffd10f370ca7)
- [bt_avrcp_get_total_number_of_items_rsp::uid_counter](../bluetooth_classic_model_reference/P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md#a6f1686ad482eb271bfcdfaf27a7c5f56)
- [bt_avrcp_get_total_number_of_items_rsp::status](../bluetooth_classic_model_reference/P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md#a7717d866cd7ea275015309b5c8128b2b)
- [bt_avrcp_get_total_number_of_items_rsp::num_items](../bluetooth_classic_model_reference/P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md#ab1d378b127df00c87593187a8ec25765)
- [bt_avrcp_inform_batt_status_of_ct_cmd::battery_status](../bluetooth_classic_model_reference/P047_bt_avrcp_inform_batt_status_of_ct_cmd_结构体.md#ae79067d210d7484c18adc3570ec20af1)
- [bt_avrcp_inform_displayable_char_set_cmd::num_charsets](../bluetooth_classic_model_reference/P048_bt_avrcp_inform_displayable_char_set_cmd_结构体.md#a157b2006ac2032335cc75cf14a6b4849)
- [bt_avrcp_inform_displayable_char_set_cmd::charset_ids](../bluetooth_classic_model_reference/P048_bt_avrcp_inform_displayable_char_set_cmd_结构体.md#a1c283439e475592935395c90b372233f)
- [bt_avrcp_item_hdr::item_type](../bluetooth_classic_model_reference/P049_bt_avrcp_item_hdr_结构体.md#ac9327e576791370bcb7b2f7140f99ee4)
- [bt_avrcp_item_hdr::item_len](../bluetooth_classic_model_reference/P049_bt_avrcp_item_hdr_结构体.md#aee91353e20e227cdf095153b101bc69a)
- [bt_avrcp_list_player_app_setting_attrs_rsp::attr_ids](../bluetooth_classic_model_reference/P050_bt_avrcp_list_player_app_setting_attrs_rsp_结构体.md#a2e3313ae520d0d174f8b48589f54e355)
- [bt_avrcp_list_player_app_setting_attrs_rsp::num_attrs](../bluetooth_classic_model_reference/P050_bt_avrcp_list_player_app_setting_attrs_rsp_结构体.md#a43432a70ba4acc8e17db8d2effa3c964)
- [bt_avrcp_list_player_app_setting_vals_cmd::attr_id](../bluetooth_classic_model_reference/P051_bt_avrcp_list_player_app_setting_vals_cmd_结构体.md#ae5dc4c95f535c3ce721c0f3d4d34fecf)
- [bt_avrcp_list_player_app_setting_vals_rsp::values](../bluetooth_classic_model_reference/P052_bt_avrcp_list_player_app_setting_vals_rsp_结构体.md#a129bdffa4fbd075371ecf6114c614ea5)
- [bt_avrcp_list_player_app_setting_vals_rsp::num_values](../bluetooth_classic_model_reference/P052_bt_avrcp_list_player_app_setting_vals_rsp_结构体.md#acf0b62de5a89ea69da09172ca6199535)
- [bt_avrcp_media_attr::attr_len](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md#a07ad1a91103fcec7b69d02b7967f1815)
- [bt_avrcp_media_attr::charset_id](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md#a48e88ae5b4c448e0fad0325891ed82d1)
- [bt_avrcp_media_attr::attr_id](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md#ae9389f3574be88638cce4e478c532a2b)
- [bt_avrcp_media_attr::attr_val](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md#af8b744485f601d694fc43ae3e6d8b28a)
- [bt_avrcp_media_element_item::media_type](../bluetooth_classic_model_reference/P054_bt_avrcp_media_element_item_结构体.md#a1695ec1cf7ff0b5f379d31f5137c893a)
- [bt_avrcp_media_element_item::data](../bluetooth_classic_model_reference/P054_bt_avrcp_media_element_item_结构体.md#a198a755a9f0c6ff88f139ac0911ed54d)
- [bt_avrcp_media_element_item::uid](../bluetooth_classic_model_reference/P054_bt_avrcp_media_element_item_结构体.md#ac0c12c790e4544eaec7d5766969ff152)
- [bt_avrcp_media_element_item::hdr](../bluetooth_classic_model_reference/P054_bt_avrcp_media_element_item_结构体.md#afe49a107dd657a16336087d2d518f1a7)
- [bt_avrcp_media_player_item::name_len](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#a02f71111fc2b4e4f53cd186aaf4372cf)
- [bt_avrcp_media_player_item::hdr](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#a15488d00a442bc3cdfdf44c383bb6738)
- [bt_avrcp_media_player_item::player_id](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#a39c8b80e71c70d4cf84ecb25a03b4f8f)
- [bt_avrcp_media_player_item::player_subtype](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#a62c18bb03aed36dda87eff9599100dec)
- [bt_avrcp_media_player_item::name](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#a9e6f3f5621a76b8ab37c0833916dae69)
- [bt_avrcp_media_player_item::play_status](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#ac8571c557795c5fec5512c7868e34dfc)
- [bt_avrcp_media_player_item::feature_bitmask](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#ad3d1c3443f1a4d0b28623e0a3e1a6607)
- [bt_avrcp_media_player_item::major_type](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#aeca27933a1892ac6c6b0951a4bf68370)
- [bt_avrcp_media_player_item::charset_id](../bluetooth_classic_model_reference/P055_bt_avrcp_media_player_item_结构体.md#afda406082181582f7fcf4b44d2f6fc8c)
- [bt_avrcp_passthrough_cmd::data](../bluetooth_classic_model_reference/P056_bt_avrcp_passthrough_cmd_结构体.md#a96b9081498ddac9f8140651b0dfab1ee)
- [bt_avrcp_passthrough_cmd::data_len](../bluetooth_classic_model_reference/P056_bt_avrcp_passthrough_cmd_结构体.md#a9facd7635f3768ac8e5351b6542b7a52)
- [bt_avrcp_passthrough_cmd::opid_state](../bluetooth_classic_model_reference/P056_bt_avrcp_passthrough_cmd_结构体.md#aaaa7657a9942d463bbe2647a0a20c0e1)
- [bt_avrcp_passthrough_opvu_data::opid_vu](../bluetooth_classic_model_reference/P057_bt_avrcp_passthrough_opvu_data_结构体.md#a13db1521501ab7c24643b2d1fd6e956a)
- [bt_avrcp_passthrough_opvu_data::company_id](../bluetooth_classic_model_reference/P057_bt_avrcp_passthrough_opvu_data_结构体.md#a17f6d3c32417102c04502336235f94fa)
- [bt_avrcp_passthrough_rsp::data_len](../bluetooth_classic_model_reference/P058_bt_avrcp_passthrough_rsp_结构体.md#a16c0388be437f140c5aaa1364cdfb3fe)
- [bt_avrcp_passthrough_rsp::data](../bluetooth_classic_model_reference/P058_bt_avrcp_passthrough_rsp_结构体.md#a735fca5cd5e5d85e987af9748f9d0ab0)
- [bt_avrcp_passthrough_rsp::opid_state](../bluetooth_classic_model_reference/P058_bt_avrcp_passthrough_rsp_结构体.md#a91aaa705b91cc9ca0954645a9a43c504)
- [bt_avrcp_play_item_cmd::scope](../bluetooth_classic_model_reference/P059_bt_avrcp_play_item_cmd_结构体.md#a80ca2390bfa44bf2509161f4c6a5421a)
- [bt_avrcp_play_item_cmd::uid_counter](../bluetooth_classic_model_reference/P059_bt_avrcp_play_item_cmd_结构体.md#ad2fa5d9e38a3ef5edc4430749ed13515)
- [bt_avrcp_play_item_cmd::uid](../bluetooth_classic_model_reference/P059_bt_avrcp_play_item_cmd_结构体.md#aebf33c2d1fa1a2574c485f777f114c0a)
- [bt_avrcp_play_item_rsp::status](../bluetooth_classic_model_reference/P060_bt_avrcp_play_item_rsp_结构体.md#a36f361a78dbceaac63508fe75ce907b4)
- [bt_avrcp_register_notification_cmd::interval](../bluetooth_classic_model_reference/P061_bt_avrcp_register_notification_cmd_结构体.md#a3bc85acb4c0b45be4fc082890f9fa744)
- [bt_avrcp_register_notification_cmd::event_id](../bluetooth_classic_model_reference/P061_bt_avrcp_register_notification_cmd_结构体.md#a631509c0abadf1f4f2bdf5a5c58f0b80)
- [bt_avrcp_search_cmd::search_str_len](../bluetooth_classic_model_reference/P062_bt_avrcp_search_cmd_结构体.md#a390c55e028e54b1c655d2dc1de35e87c)
- [bt_avrcp_search_cmd::search_str](../bluetooth_classic_model_reference/P062_bt_avrcp_search_cmd_结构体.md#a953e7210d1d0f8ff2cb86e4742a4af7a)
- [bt_avrcp_search_cmd::charset_id](../bluetooth_classic_model_reference/P062_bt_avrcp_search_cmd_结构体.md#aa3b1bda62dc37d4c003ea3b3af9567da)
- [bt_avrcp_search_rsp::status](../bluetooth_classic_model_reference/P063_bt_avrcp_search_rsp_结构体.md#abbaacf359228e5c56e8cf4147dafe258)
- [bt_avrcp_search_rsp::uid_counter](../bluetooth_classic_model_reference/P063_bt_avrcp_search_rsp_结构体.md#ac1dadb58aa8852476a79799af8b8bd1e)
- [bt_avrcp_search_rsp::num_items](../bluetooth_classic_model_reference/P063_bt_avrcp_search_rsp_结构体.md#ad58679ba2fee9137b3d8c7808b5dfcba)
- [bt_avrcp_set_absolute_volume_cmd::absolute_volume](../bluetooth_classic_model_reference/P064_bt_avrcp_set_absolute_volume_cmd_结构体.md#adc69d9de75995fdd1658b38d50566ec4)
- [bt_avrcp_set_absolute_volume_rsp::absolute_volume](../bluetooth_classic_model_reference/P065_bt_avrcp_set_absolute_volume_rsp_结构体.md#ae542d562193e9b42e14b04b7a91f1500)
- [bt_avrcp_set_addressed_player_cmd::player_id](../bluetooth_classic_model_reference/P066_bt_avrcp_set_addressed_player_cmd_结构体.md#a0cb667cb10375fcd16570fd3fbda20d7)
- [bt_avrcp_set_browsed_player_rsp::uid_counter](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a5c0a40b5fbcd85dca0b904a106cfede9)
- [bt_avrcp_set_browsed_player_rsp::charset_id](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a61e93ead82b56cb3f61d1337423af05d)
- [bt_avrcp_set_browsed_player_rsp::status](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a7d07c8595a14800385db33662b3096c5)
- [bt_avrcp_set_browsed_player_rsp::folder_names](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a889cfb87961402d8a41b17292ec89b11)
- [bt_avrcp_set_browsed_player_rsp::num_items](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a995907daaada393c045265583d0bad92)
- [bt_avrcp_set_browsed_player_rsp::folder_depth](../bluetooth_classic_model_reference/P067_bt_avrcp_set_browsed_player_rsp_结构体.md#a9c7989c84c89790673a0f25922a72f59)
- [bt_avrcp_set_player_app_setting_val_cmd::attr_vals](../bluetooth_classic_model_reference/P068_bt_avrcp_set_player_app_setting_val_cmd_结构体.md#a6eda2876b27b4e137ff80bf0283f96ae)
- [bt_avrcp_set_player_app_setting_val_cmd::num_attrs](../bluetooth_classic_model_reference/P068_bt_avrcp_set_player_app_setting_val_cmd_结构体.md#a8de91e220969f26121ea08d4e93b11ce)
- [bt_avrcp_subunit_info_rsp::extended_subunit_id](../bluetooth_classic_model_reference/P069_bt_avrcp_subunit_info_rsp_结构体.md#a0be33096e6edf251c23a5322b3c30421)
- [bt_avrcp_subunit_info_rsp::subunit_type](../bluetooth_classic_model_reference/P069_bt_avrcp_subunit_info_rsp_结构体.md#a144ad1d366436c8b2502a17833a36dc3)
- [bt_avrcp_subunit_info_rsp::extended_subunit_type](../bluetooth_classic_model_reference/P069_bt_avrcp_subunit_info_rsp_结构体.md#a47b69412c61682ed336737f34ac614dc)
- [bt_avrcp_subunit_info_rsp::max_subunit_id](../bluetooth_classic_model_reference/P069_bt_avrcp_subunit_info_rsp_结构体.md#a85cf595920ba2dbf9f0e4deca1d27483)
- [bt_avrcp_tg_cb::get_folder_items](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a0f117772eb0f55e20214b0be8d93a6fa)
- [bt_avrcp_tg_cb::set_player_app_setting_val](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a19308d4734cdd9bf397f7ba721920e97)
- [bt_avrcp_tg_cb::set_addressed_player](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a1ab779d9b5142590f9dcb42990d9d3cb)
- [bt_avrcp_tg_cb::get_player_app_setting_attr_text](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a20215fb3b4bb2d7c73f2d08ac3e801ec)
- [bt_avrcp_tg_cb::set_absolute_volume](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a2f022902183a0db38c65a41fdc0a8478)
- [bt_avrcp_tg_cb::change_path](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a37d8a221b66cf3bad74790532b559cff)
- [bt_avrcp_tg_cb::set_browsed_player](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a4179686bbe4030c44f0a277532dcb96b)
- [bt_avrcp_tg_cb::register_notification](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a45954c3a1f3e8dffb1bc111845c875ce)
- [bt_avrcp_tg_cb::passthrough_req](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a48b25910cffb470139e2a562b15802ce)
- [bt_avrcp_tg_cb::get_curr_player_app_setting_val](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a51caea0e045788bbce8073f720eb7e19)
- [bt_avrcp_tg_cb::get_player_app_setting_val_text](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a64bf13cf36066568ecbbe1006c717970)
- [bt_avrcp_tg_cb::add_to_now_playing](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a6946e152d68e5650f683ed6a449709d7)
- [bt_avrcp_tg_cb::browsing_connected](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a82c5ca1100844e5119224aa6bac19bd2)
- [bt_avrcp_tg_cb::search](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a8442f74b35a70c88defe84e948ced8d6)
- [bt_avrcp_tg_cb::get_item_attrs](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a878eaaf2358b0773e964dc68c910a377)
- [bt_avrcp_tg_cb::inform_batt_status_of_ct](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a883db478d1a35f0fe61f867d78366c91)
- [bt_avrcp_tg_cb::get_play_status](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a889d781b5275ca24bf0603c370bb2a4e)
- [bt_avrcp_tg_cb::connected](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a8f0994f1b59d16ef74a7430221f53db0)
- [bt_avrcp_tg_cb::unit_info_req](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a933eb30910fef1e916e60ff21d4255ec)
- [bt_avrcp_tg_cb::disconnected](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#a9c64cc44157e6cedec9decc00f0022b3)
- [bt_avrcp_tg_cb::get_caps](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ab3fe452afec12ff31975763c5269c94f)
- [bt_avrcp_tg_cb::subunit_info_req](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ab9f1a086a71522986808f3ebc2cbd2de)
- [bt_avrcp_tg_cb::list_player_app_setting_vals](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#acd0d716aa960230b3e8f7c5c0bdb9b19)
- [bt_avrcp_tg_cb::browsing_disconnected](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ad66a2945e2cb464bf7324a0685106d47)
- [bt_avrcp_tg_cb::inform_displayable_char_set](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ad8701332c6415915d32454788772dd09)
- [bt_avrcp_tg_cb::get_element_attrs](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#adf7e869f632ebc1ccbe7d8213a7c4f05)
- [bt_avrcp_tg_cb::list_player_app_setting_attrs](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ae496f717332ea6a42507e3772793ba0e)
- [bt_avrcp_tg_cb::get_total_number_of_items](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#ae5a45a624cf6d9224aca975260e954c8)
- [bt_avrcp_tg_cb::play_item](../bluetooth_classic_model_reference/P071_bt_avrcp_tg_cb_结构体.md#af07da9dc841518013c6f6a1796f957f1)
- [bt_avrcp_unit_info_rsp::company_id](../bluetooth_classic_model_reference/P072_bt_avrcp_unit_info_rsp_结构体.md#a0225755bf457bc6d4046d8172af49217)
- [bt_avrcp_unit_info_rsp::unit_type](../bluetooth_classic_model_reference/P072_bt_avrcp_unit_info_rsp_结构体.md#a92b869b3200841ea1d10aca41cdd9f77)
- [media_element_item_attr::attrs](../device_power_control_model_reference/P027_media_element_item_attr_结构体.md#a00c0f6e1b42a8b6448574105acb0481d)
- [media_element_item_attr::num_attrs](../device_power_control_model_reference/P027_media_element_item_attr_结构体.md#aee96c7d393f086f89e995a96eb95cce9)
- [media_element_item_name::name_len](../device_power_control_model_reference/P028_media_element_item_name_结构体.md#a51866bcc43ed3ed31feb87ac60f97171)
- [media_element_item_name::name](../device_power_control_model_reference/P028_media_element_item_name_结构体.md#a66b939713a0b4f7aadfbbf65e5b8cef3)
- [media_element_item_name::charset_id](../device_power_control_model_reference/P028_media_element_item_name_结构体.md#a9ab8705023810277a63566d5b05bc777)
- [net_buf::data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [net_buf::len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)

---

[上一章](P001_amebad_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_bap.h_源码浏览.md)
