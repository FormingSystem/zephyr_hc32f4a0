---
id: learning.zephyr-docs.api-source-interrupt-modem-reference.page-7
title: net_stats.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_net\_stats.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_configuration_reference/P059_zephyr__net__net_stats.h_文件参考.md)。

## 7.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00040"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00087"></a>
<a id="l00087"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00114"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="foldopen00180"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="foldopen00197"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="foldopen00214"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="foldopen00228"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="foldopen00242"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="foldopen00256"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="foldopen00270"></a>
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="foldopen00284"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="foldopen00298"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="foldopen00309"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
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
<a id="l00332"></a>
<a id="foldopen00336"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00349"></a>
<a id="l00351"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00357"></a>
<a id="l00359"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="foldopen00380"></a>
<a id="l00380"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="foldopen00394"></a>
<a id="l00394"></a>
<a id="l00396"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="foldopen00423"></a>
<a id="l00423"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="foldopen00533"></a>
<a id="l00533"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="foldopen00595"></a>
<a id="l00595"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="foldopen00612"></a>
<a id="l00612"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="foldopen00623"></a>
<a id="l00623"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="foldopen00647"></a>
<a id="l00647"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="foldopen00699"></a>
<a id="l00699"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="foldopen00716"></a>
<a id="l00716"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="foldopen00727"></a>
<a id="l00727"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
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
<a id="l00787"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
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
<a id="l00820"></a>
<a id="l00821"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00827"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00837"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00847"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="l00857"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00867"></a>
<a id="l00869"></a>
<a id="l00870"></a>
<a id="l00871"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00877"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00887"></a>
<a id="l00889"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00897"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00907"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00917"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00927"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="l00935"></a>
<a id="l00937"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00949"></a>
<a id="l00951"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00955"></a>
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00959"></a>
<a id="l00961"></a>
<a id="l00963"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="l00967"></a>
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
<a id="l01196"></a>
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
<a id="foldopen01494"></a>
<a id="l01494"></a>
<a id="l01495"></a>
<a id="l01496"></a>
<a id="l01497"></a>
<a id="l01498"></a>
<a id="l01499"></a>
<a id="l01500"></a>
<a id="l01501"></a>
<a id="l01502"></a>
<a id="foldopen01503"></a>
<a id="l01503"></a>
<a id="l01504"></a>
<a id="l01505"></a>
<a id="l01506"></a>
<a id="l01507"></a>
<a id="l01508"></a>
<a id="l01509"></a>
<a id="l01510"></a>
<a id="l01511"></a>
<a id="foldopen01512"></a>
<a id="l01512"></a>
<a id="l01513"></a>
<a id="l01514"></a>
<a id="l01515"></a>
<a id="l01516"></a>
<a id="l01517"></a>
<a id="l01518"></a>
<a id="l01519"></a>
<a id="l01520"></a>
<a id="foldopen01521"></a>
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
<a id="foldopen01544"></a>
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
<a id="l01630"></a>
<a id="l01631"></a>
<a id="l01632"></a>
<a id="l01633"></a>
<a id="l01634"></a>
<a id="l01635"></a>
<a id="acollector_8h_html"></a>
<a id="agauge_8h_html"></a>
<a id="agroup__net__mgmt_html_ga08bde8717fd8e12a338c517b22b87776"></a>
<a id="agroup__net__stats_html_ga05ec15873e79256c287f21b6b6fcd752"></a>
<a id="ahistogram_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="ametric_8h_html"></a>
<a id="anet_2prometheus_2counter_8h_html"></a>
<a id="anet__core_8h_html"></a>
<a id="anet__mgmt_8h_html"></a>
<a id="aposix_2sys_2socket_8h_html_adee01662b0cf762a014efd87ab811276"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__stats__bytes_html"></a>
<a id="astructnet__stats__bytes_html_a360bdbf177d60b0677beec2037f34cb0"></a>
<a id="astructnet__stats__bytes_html_a9f87e32d63bc4239ef7db03feedd495e"></a>
<a id="astructnet__stats__dns_html"></a>
<a id="astructnet__stats__dns_html_a04756603a183f35dbf6f55000556b546"></a>
<a id="astructnet__stats__dns_html_abc9be2039a3ff9e62b956ae27fd0ab84"></a>
<a id="astructnet__stats__dns_html_ac07b9f4d084b978cc11e7799fb71a435"></a>
<a id="astructnet__stats__eth__csum_html"></a>
<a id="astructnet__stats__eth__csum_html_a1f1ba5c01c6232cd739d069ddb871b17"></a>
<a id="astructnet__stats__eth__csum_html_ac4fc04d66193070d4f52a4c07f29ccce"></a>
<a id="astructnet__stats__eth__errors_html"></a>
<a id="astructnet__stats__eth__errors_html_a0043d1a1481040a6d7439bd23423ec12"></a>
<a id="astructnet__stats__eth__errors_html_a07d0a435f2129556520c732571d28edf"></a>
<a id="astructnet__stats__eth__errors_html_a0e83e270a35222ed3e927800be4159e7"></a>
<a id="astructnet__stats__eth__errors_html_a17624a12d6473bdd78698076fed0d122"></a>
<a id="astructnet__stats__eth__errors_html_a257113639f0e0e3085febb7a147f498f"></a>
<a id="astructnet__stats__eth__errors_html_a2d2b2c4e3764ebec841f1ecbe7058d99"></a>
<a id="astructnet__stats__eth__errors_html_a4dab70cf219269bb393ce14faf0ed77e"></a>
<a id="astructnet__stats__eth__errors_html_a5e3d39d8417bb180cbfcb8c901006e81"></a>
<a id="astructnet__stats__eth__errors_html_a7618f10af3443c49a6e256bb41e77781"></a>
<a id="astructnet__stats__eth__errors_html_a7bcfbb13836f162ceeb5f021304b5c76"></a>
<a id="astructnet__stats__eth__errors_html_a82622736d226b4d3b999f1f22ccf8529"></a>
<a id="astructnet__stats__eth__errors_html_a84630da9b82557f56dc35cd59ca2f7ae"></a>
<a id="astructnet__stats__eth__errors_html_a8dfcc5cd1b4decec5783d01ba7033b05"></a>
<a id="astructnet__stats__eth__errors_html_a9afee89f5bb01907e7cd515e2a0ff1b5"></a>
<a id="astructnet__stats__eth__errors_html_abfbf6478b7afdd5935d7c6948c9ef426"></a>
<a id="astructnet__stats__eth__errors_html_aca0e2e4807fa70279dee8ddaad2d7ef7"></a>
<a id="astructnet__stats__eth__errors_html_adbcae9c10c081f1cdf304bcdce740aa4"></a>
<a id="astructnet__stats__eth__errors_html_ae2a13733c1a5f0cc3e00efca0c3f429d"></a>
<a id="astructnet__stats__eth__errors_html_afec6a7e24c6f3cc74dd9f739f27b3e48"></a>
<a id="astructnet__stats__eth__flow_html"></a>
<a id="astructnet__stats__eth__flow_html_a08e5da4ff78fe3893b9c9a628cefe4f2"></a>
<a id="astructnet__stats__eth__flow_html_a31412e8bf9d38ba630ea856e958a48d7"></a>
<a id="astructnet__stats__eth__flow_html_a8f9b93537b3c11be70f276aaa72cb637"></a>
<a id="astructnet__stats__eth__flow_html_a969d81f9db20312d2d2aa7f70f93bdd5"></a>
<a id="astructnet__stats__eth__hw__timestamp_html"></a>
<a id="astructnet__stats__eth__hw__timestamp_html_a41f605499dbf88a879522fdfa4633d9e"></a>
<a id="astructnet__stats__eth__hw__timestamp_html_acd3d5f72d7df568110d96093e0c9534d"></a>
<a id="astructnet__stats__eth__hw__timestamp_html_ae1f983faf4a999308c464e4af5a5284b"></a>
<a id="astructnet__stats__eth_html"></a>
<a id="astructnet__stats__eth_html_a054beb909134b0e0f22f5df599549128"></a>
<a id="astructnet__stats__eth_html_a2169ae06bace1a93663bccf88c8d7a29"></a>
<a id="astructnet__stats__eth_html_a257c349cf3d32d38796e3899e702454a"></a>
<a id="astructnet__stats__eth_html_a44667efff73c17c089ed22d5b0da5ad3"></a>
<a id="astructnet__stats__eth_html_a4f6a2903330518a132e7e547820e0bf2"></a>
<a id="astructnet__stats__eth_html_a643010ac6360c8c0c08016725ba12222"></a>
<a id="astructnet__stats__eth_html_a6699012226e25e8bad39076fed6dbfb5"></a>
<a id="astructnet__stats__eth_html_a822d4205791f59999c842610522f6fc5"></a>
<a id="astructnet__stats__eth_html_a8c5cf1ead8ba214425a16fed1c2ad0fb"></a>
<a id="astructnet__stats__eth_html_a922feddb17fc020371f1bcc52c709415"></a>
<a id="astructnet__stats__eth_html_a97bd6026b16890743f344751a21107f1"></a>
<a id="astructnet__stats__eth_html_a9c869740f416fbe0b54d7fefacb1fe29"></a>
<a id="astructnet__stats__eth_html_ab351258ae82abd09759d37774559d8bc"></a>
<a id="astructnet__stats__eth_html_afaacee7cc1d0a35ae2344175421c40dd"></a>
<a id="astructnet__stats__icmp_html"></a>
<a id="astructnet__stats__icmp_html_a2d6eb7dfc8f4b439b399b039022f2889"></a>
<a id="astructnet__stats__icmp_html_a6662bc547107a08c52e902a2446629bf"></a>
<a id="astructnet__stats__icmp_html_a755f3388c05d4bd2988ddd16d1a4cf32"></a>
<a id="astructnet__stats__icmp_html_ae1a29dd9b8e1ce9a737fa7f36c805cd4"></a>
<a id="astructnet__stats__icmp_html_ae6f226b55565c11fca0c9e099f08c267"></a>
<a id="astructnet__stats__ip__errors_html"></a>
<a id="astructnet__stats__ip__errors_html_a06b35742c418ebc6414fcb5c7002edde"></a>
<a id="astructnet__stats__ip__errors_html_a3e476f659ebeaa5c5f7b6dad2d90326f"></a>
<a id="astructnet__stats__ip__errors_html_a872cc0beca45bbe87ae794dd8ca4e301"></a>
<a id="astructnet__stats__ip__errors_html_a978b1c23847e707ac1fa27c2b34fa85d"></a>
<a id="astructnet__stats__ip__errors_html_a9b4bf05e9df13e1d99518125b9067bef"></a>
<a id="astructnet__stats__ip__errors_html_ab84ee9dfbe5da391d60c6e3ae9abea16"></a>
<a id="astructnet__stats__ip_html"></a>
<a id="astructnet__stats__ip_html_a4bb82a5ebebaa3e8a11973c07eed96a0"></a>
<a id="astructnet__stats__ip_html_ab6a6373368dd24cb51504c5729d535d3"></a>
<a id="astructnet__stats__ip_html_abbe676bbe9faa89b2b6b8c4950b1c9d5"></a>
<a id="astructnet__stats__ip_html_ac86399b70d7f761162e5336dd15589eb"></a>
<a id="astructnet__stats__ipv4__igmp_html"></a>
<a id="astructnet__stats__ipv4__igmp_html_a1c37702ff837b8c5cc9df5f690e7678c"></a>
<a id="astructnet__stats__ipv4__igmp_html_a469113de7af0ba42dbd1b0365d00602c"></a>
<a id="astructnet__stats__ipv4__igmp_html_a955e20a6ee5e19e08000b3114b9d71a6"></a>
<a id="astructnet__stats__ipv4__pmtu_html"></a>
<a id="astructnet__stats__ipv4__pmtu_html_a44f1028694d4001cd4a43f925f0bf0da"></a>
<a id="astructnet__stats__ipv4__pmtu_html_a64245eb7b9b1fcfa0f0efcb53eff7ec2"></a>
<a id="astructnet__stats__ipv4__pmtu_html_ad35f9defad7c5ce29e510b8051788977"></a>
<a id="astructnet__stats__ipv6__mld_html"></a>
<a id="astructnet__stats__ipv6__mld_html_a4879ff9e31f8b60973d3b169598e921d"></a>
<a id="astructnet__stats__ipv6__mld_html_ab397b74b14ce7047bf2fc63ca72ce1e5"></a>
<a id="astructnet__stats__ipv6__mld_html_ad85dc87f57296a1e7d64e959b0370ee8"></a>
<a id="astructnet__stats__ipv6__nd_html"></a>
<a id="astructnet__stats__ipv6__nd_html_a0129f7892a4439c20deb2f32b9001277"></a>
<a id="astructnet__stats__ipv6__nd_html_a0bf6f67d9112996a3b002ea160aec769"></a>
<a id="astructnet__stats__ipv6__nd_html_a31074d5d44138fcabdc5f7750f9f2c47"></a>
<a id="astructnet__stats__ipv6__pmtu_html"></a>
<a id="astructnet__stats__ipv6__pmtu_html_a66346cd9140e30727d77648f65345762"></a>
<a id="astructnet__stats__ipv6__pmtu_html_a68b19ebb61e84eb876178a31c7a4e327"></a>
<a id="astructnet__stats__ipv6__pmtu_html_a698f5794b73896f7a66def2d3209fafd"></a>
<a id="astructnet__stats__pkt__filter_html"></a>
<a id="astructnet__stats__pkt__filter_html_a5e88001e143c0adb129ca93b108c277d"></a>
<a id="astructnet__stats__pkt__filter_html_a62d2d86781e6224b09f21929f27b2ef7"></a>
<a id="astructnet__stats__pkt__filter_html_a8cf9912d574873832b85a614eb776789"></a>
<a id="astructnet__stats__pkts_html"></a>
<a id="astructnet__stats__pkts_html_ac9784b5a245e6c57e39318aaf314f0cf"></a>
<a id="astructnet__stats__pkts_html_aee1e302d0f8dac79b693a06d8fa3b3c5"></a>
<a id="astructnet__stats__pm_html"></a>
<a id="astructnet__stats__pm_html_a0bdf9c3676298e2df4ff3bfa03f5e823"></a>
<a id="astructnet__stats__pm_html_a6784806eaa093431ed3c0f7acfe5a89c"></a>
<a id="astructnet__stats__pm_html_ab43935fcfe9efc1cd5f3e7e329996805"></a>
<a id="astructnet__stats__pm_html_ac14122a4765c499c045f18c70af355a0"></a>
<a id="astructnet__stats__ppp_html"></a>
<a id="astructnet__stats__ppp_html_a1332b31980f82236aeb0c3f9444e2ac6"></a>
<a id="astructnet__stats__ppp_html_a71fc81f3c5f3e65a476b3391f086d340"></a>
<a id="astructnet__stats__ppp_html_ab2b48da7f19d4b83e3f41b41979b7ed8"></a>
<a id="astructnet__stats__ppp_html_ae2e0a47a539e9d7bc97f9c63f889b276"></a>
<a id="astructnet__stats__raw_html"></a>
<a id="astructnet__stats__raw_html_a0decb52f848bf006f52cd575e181ffeb"></a>
<a id="astructnet__stats__raw_html_ab78de1ea1ec2ff46e6f1f248cebd5fac"></a>
<a id="astructnet__stats__raw_html_ac83a096e59c4483528a67f7209fba257"></a>
<a id="astructnet__stats__raw_html_aea0d3bd2836853e9f8ed6af489ad42ef"></a>
<a id="astructnet__stats__rx__time_html"></a>
<a id="astructnet__stats__rx__time_html_a4b84c2ae2fda8fcd75fdf1bf0b2aae8d"></a>
<a id="astructnet__stats__rx__time_html_a68247051b064de081fa2e84118192958"></a>
<a id="astructnet__stats__sta__mgmt_html"></a>
<a id="astructnet__stats__sta__mgmt_html_a29ae0079b4c780e0de2656a85ec15fe9"></a>
<a id="astructnet__stats__sta__mgmt_html_ac6e68fded8e19b20259442436923f815"></a>
<a id="astructnet__stats__tc_html"></a>
<a id="astructnet__stats__tc_html_a1794f71f7fe7b3d20d406be4b28eb032"></a>
<a id="astructnet__stats__tc_html_a30288ef3bb0796cd18c3cf0aedbe875a"></a>
<a id="astructnet__stats__tc_html_a6614b5f5186635415a7d787260c39248"></a>
<a id="astructnet__stats__tc_html_a74b471b77fb1c72933daa656319cc2af"></a>
<a id="astructnet__stats__tc_html_a8a5c2e59990407ddbfc7973a1c183bf6"></a>
<a id="astructnet__stats__tc_html_a8d6a3ebcc49ce8c34a5faae986f648e2"></a>
<a id="astructnet__stats__tc_html_a8ea00824bb0fb18e4d8912343e01c3b7"></a>
<a id="astructnet__stats__tcp_html"></a>
<a id="astructnet__stats__tcp_html_a0d40abc85776f0a9b9510a909b7f6d18"></a>
<a id="astructnet__stats__tcp_html_a471fcd5578f79ce77d20547b28503ac1"></a>
<a id="astructnet__stats__tcp_html_a4a4ea6e5d87ef58b4271bd708cf39635"></a>
<a id="astructnet__stats__tcp_html_a5099e174b0eafa322f0630f1f5c73a8b"></a>
<a id="astructnet__stats__tcp_html_a5f045704859331918511e9c2281ac155"></a>
<a id="astructnet__stats__tcp_html_a67f55954a4c51f2b957c7d974e78c1c0"></a>
<a id="astructnet__stats__tcp_html_aa549f7b6d5828009a09190fd64afa8e3"></a>
<a id="astructnet__stats__tcp_html_aa618cf86b962aca0f14eb9178c8ae61a"></a>
<a id="astructnet__stats__tcp_html_aa987bebf96000b6b4e92bfafc218759a"></a>
<a id="astructnet__stats__tcp_html_abe567032cb4a267a984aec28c1e3cca4"></a>
<a id="astructnet__stats__tcp_html_ac557ac0d8917bc2c2dfed74126f993c8"></a>
<a id="astructnet__stats__tcp_html_ad25edb2b39a6acc8152c35ad43a5042f"></a>
<a id="astructnet__stats__tcp_html_af80c18bcc253133ce5f0597ac190b349"></a>
<a id="astructnet__stats__tx__time_html"></a>
<a id="astructnet__stats__tx__time_html_a7a652350ed04e53ba02aec294f8444b4"></a>
<a id="astructnet__stats__tx__time_html_af6f7a26c0344a0f93306e105a8917c3e"></a>
<a id="astructnet__stats__udp_html"></a>
<a id="astructnet__stats__udp_html_a0ea91d85fe322661fb909f5e94e55a34"></a>
<a id="astructnet__stats__udp_html_a2d884bf9106e60d430ffec7c7964a609"></a>
<a id="astructnet__stats__udp_html_a4c57d5f68ebda7981400729b9c7fe0f7"></a>
<a id="astructnet__stats__udp_html_ab4e8228c221901d3ded55f3f823bfa1c"></a>
<a id="astructnet__stats__wifi_html"></a>
<a id="astructnet__stats__wifi_html_a03dc04638c4b670bd7f3520d45fc1eda"></a>
<a id="astructnet__stats__wifi_html_a7e7f68215101885fd51c70e981da26e7"></a>
<a id="astructnet__stats__wifi_html_a8bee22961545674e6ab100b58a04bf91"></a>
<a id="astructnet__stats__wifi_html_aa055b1e8bd8f1e50815c1028b562be07"></a>
<a id="astructnet__stats__wifi_html_ac498c9e517f2cb2eb01d251e84159e7e"></a>
<a id="astructnet__stats__wifi_html_adbcdb2dd8733f2917c00a0b2d365393b"></a>
<a id="astructnet__stats__wifi_html_ae0149e64a94a9f96eb6680f94793c8c4"></a>
<a id="astructnet__stats__wifi_html_ae80dcd73a3c5ce3ec3282d1ae827b338"></a>
<a id="astructnet__stats_html"></a>
<a id="astructnet__stats_html_a3a4c90661d6b310b628262228a341fe2"></a>
<a id="astructnet__stats_html_a7a28233e6d23efdce0143469b9bb6c05"></a>
<a id="astructnet__stats_html_ac42cb13954d164e92a1ef60919a2a34e"></a>
<a id="asummary_8h_html"></a>

```c


/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_NET_STATS_H_
#define ZEPHYR_INCLUDE_NET_NET_STATS_H_

#include <zephyr/types.h>
#include <zephyr/net/net_core.h>
#include <zephyr/net/net_mgmt.h>

#include <zephyr/net/prometheus/collector.h>
#include <zephyr/net/prometheus/counter.h>
#include <zephyr/net/prometheus/metric.h>
#include <zephyr/net/prometheus/gauge.h>
#include <zephyr/net/prometheus/histogram.h>
#include <zephyr/net/prometheus/summary.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef uint32_t net_stats_t;

struct net_stats_bytes {
        uint64_t sent;
        uint64_t received;
};

struct net_stats_pkts {
        net_stats_t tx;
        net_stats_t rx;
};

struct net_stats_ip {
        net_stats_t recv;

        net_stats_t sent;

        net_stats_t forwarded;

        net_stats_t drop;
};

struct net_stats_ip_errors {
        net_stats_t vhlerr;

        net_stats_t hblenerr;

        net_stats_t lblenerr;

        net_stats_t fragerr;

        net_stats_t chkerr;

        net_stats_t protoerr;
};

struct net_stats_icmp {
        net_stats_t recv;

        net_stats_t sent;

        net_stats_t drop;

        net_stats_t typeerr;

        net_stats_t chkerr;
};

struct net_stats_tcp {
        struct net_stats_bytes bytes;

        net_stats_t resent;

        net_stats_t drop;

        net_stats_t recv;

        net_stats_t sent;

        net_stats_t seg_drop;

        net_stats_t chkerr;

        net_stats_t ackerr;

        net_stats_t rsterr;

        net_stats_t rst;

        net_stats_t rexmit;

        net_stats_t conndrop;

        net_stats_t connrst;
};

struct net_stats_udp {
        net_stats_t drop;

        net_stats_t recv;

        net_stats_t sent;

        net_stats_t chkerr;
};

struct net_stats_raw {
        struct net_stats_bytes bytes;

        net_stats_t drop;

        net_stats_t recv;

        net_stats_t sent;
};

struct net_stats_ipv6_nd {
        net_stats_t drop;

        net_stats_t recv;

        net_stats_t sent;
};

struct net_stats_ipv6_pmtu {
        net_stats_t drop;

        net_stats_t recv;

        net_stats_t sent;
};

struct net_stats_ipv4_pmtu {
        net_stats_t drop;

        net_stats_t recv;

        net_stats_t sent;
};

struct net_stats_ipv6_mld {
        net_stats_t recv;

        net_stats_t sent;

        net_stats_t drop;
};

struct net_stats_ipv4_igmp {
        net_stats_t recv;

        net_stats_t sent;

        net_stats_t drop;
};

struct net_stats_dns {
        net_stats_t recv;

        net_stats_t sent;

        net_stats_t drop;
};

struct net_stats_tx_time {
        uint64_t sum;

        net_stats_t count;
};

struct net_stats_rx_time {
        uint64_t sum;

        net_stats_t count;
};


#if NET_TC_TX_COUNT == 0
#define NET_TC_TX_STATS_COUNT 1
#else
#define NET_TC_TX_STATS_COUNT NET_TC_TX_COUNT
#endif

#if NET_TC_RX_COUNT == 0
#define NET_TC_RX_STATS_COUNT 1
#else
#define NET_TC_RX_STATS_COUNT NET_TC_RX_COUNT
#endif


struct net_stats_tc {
        struct {
                uint64_t bytes;
                struct net_stats_tx_time tx_time;
#if defined(CONFIG_NET_PKT_TXTIME_STATS_DETAIL)
                struct net_stats_tx_time
                                tx_time_detail[NET_PKT_DETAIL_STATS_COUNT];
#endif
                net_stats_t pkts;
                net_stats_t dropped;
                uint8_t priority;
        } sent[NET_TC_TX_STATS_COUNT];

        struct {
                uint64_t bytes;
                struct net_stats_rx_time rx_time;
#if defined(CONFIG_NET_PKT_RXTIME_STATS_DETAIL)
                struct net_stats_rx_time
                                rx_time_detail[NET_PKT_DETAIL_STATS_COUNT];
#endif
                net_stats_t pkts;
                net_stats_t dropped;
                uint8_t priority;
        } recv[NET_TC_RX_STATS_COUNT];
};


struct net_stats_pm {
        uint64_t overall_suspend_time;
        net_stats_t suspend_count;
        uint32_t last_suspend_time;
        uint32_t start_time;
};

struct net_stats_pkt_filter {
        struct {
                net_stats_t drop;
#if defined(CONFIG_NET_PKT_FILTER_IPV4_HOOK)
                net_stats_t ipv4_drop;
#endif
#if defined(CONFIG_NET_PKT_FILTER_IPV6_HOOK)
                net_stats_t ipv6_drop;
#endif
#if defined(CONFIG_NET_PKT_FILTER_LOCAL_IN_HOOK)
                net_stats_t local_drop;
#endif
        } rx;

        struct {
                net_stats_t drop;
        } tx;
};

struct net_stats {
        struct net_stats_bytes bytes;

        net_stats_t processing_error;

        struct net_stats_ip_errors ip_errors;

#if defined(CONFIG_NET_STATISTICS_PKT_FILTER)
        struct net_stats_pkt_filter pkt_filter;
#endif

#if defined(CONFIG_NET_STATISTICS_IPV6)
        struct net_stats_ip ipv6;
#endif

#if defined(CONFIG_NET_STATISTICS_IPV4)
        struct net_stats_ip ipv4;
#endif

#if defined(CONFIG_NET_STATISTICS_ICMP)
        struct net_stats_icmp icmp;
#endif

#if defined(CONFIG_NET_STATISTICS_TCP)
        struct net_stats_tcp tcp;
#endif

#if defined(CONFIG_NET_STATISTICS_UDP)
        struct net_stats_udp udp;
#endif

#if defined(CONFIG_NET_STATISTICS_RAW)
        struct net_stats_raw raw;
#endif

#if defined(CONFIG_NET_STATISTICS_IPV6_ND)
        struct net_stats_ipv6_nd ipv6_nd;
#endif

#if defined(CONFIG_NET_STATISTICS_IPV6_PMTU)
        struct net_stats_ipv6_pmtu ipv6_pmtu;
#endif

#if defined(CONFIG_NET_STATISTICS_IPV4_PMTU)
        struct net_stats_ipv4_pmtu ipv4_pmtu;
#endif

#if defined(CONFIG_NET_STATISTICS_MLD)
        struct net_stats_ipv6_mld ipv6_mld;
#endif

#if defined(CONFIG_NET_STATISTICS_IGMP)
        struct net_stats_ipv4_igmp ipv4_igmp;
#endif

#if defined(CONFIG_NET_STATISTICS_DNS)
        struct net_stats_dns dns;
#endif

#if NET_TC_COUNT > 1
        struct net_stats_tc tc;
#endif

#if defined(CONFIG_NET_PKT_TXTIME_STATS)
        struct net_stats_tx_time tx_time;
#endif

#if defined(CONFIG_NET_PKT_RXTIME_STATS)
        struct net_stats_rx_time rx_time;
#endif

#if defined(CONFIG_NET_PKT_TXTIME_STATS_DETAIL)
        struct net_stats_tx_time tx_time_detail[NET_PKT_DETAIL_STATS_COUNT];
#endif
#if defined(CONFIG_NET_PKT_RXTIME_STATS_DETAIL)
        struct net_stats_rx_time rx_time_detail[NET_PKT_DETAIL_STATS_COUNT];
#endif

#if defined(CONFIG_NET_STATISTICS_POWER_MANAGEMENT)
        struct net_stats_pm pm;
#endif
};

struct net_stats_eth_errors {
        net_stats_t rx_length_errors;

        net_stats_t rx_over_errors;

        net_stats_t rx_crc_errors;

        net_stats_t rx_frame_errors;

        net_stats_t rx_no_buffer_count;

        net_stats_t rx_missed_errors;

        net_stats_t rx_long_length_errors;

        net_stats_t rx_short_length_errors;

        net_stats_t rx_align_errors;

        net_stats_t rx_dma_failed;

        net_stats_t rx_buf_alloc_failed;

        net_stats_t tx_aborted_errors;

        net_stats_t tx_carrier_errors;

        net_stats_t tx_fifo_errors;

        net_stats_t tx_heartbeat_errors;

        net_stats_t tx_window_errors;

        net_stats_t tx_dma_failed;

        net_stats_t uncorr_ecc_errors;

        net_stats_t corr_ecc_errors;
};

struct net_stats_eth_flow {
        net_stats_t rx_flow_control_xon;

        net_stats_t rx_flow_control_xoff;

        net_stats_t tx_flow_control_xon;

        net_stats_t tx_flow_control_xoff;
};

struct net_stats_eth_csum {
        net_stats_t rx_csum_offload_good;

        net_stats_t rx_csum_offload_errors;
};

struct net_stats_eth_hw_timestamp {
        net_stats_t rx_hwtstamp_cleared;

        net_stats_t tx_hwtstamp_timeouts;

        net_stats_t tx_hwtstamp_skipped;
};

#ifdef CONFIG_NET_STATISTICS_ETHERNET_VENDOR
struct net_stats_eth_vendor {
        const char * const key;
        uint32_t value;
};
#endif

struct net_stats_eth {
        struct net_stats_bytes bytes;

        struct net_stats_pkts pkts;

        struct net_stats_pkts broadcast;

        struct net_stats_pkts multicast;

        struct net_stats_pkts errors;

        struct net_stats_eth_errors error_details;

        struct net_stats_eth_flow flow_control;

        struct net_stats_eth_csum csum;

        struct net_stats_eth_hw_timestamp hw_timestamp;

        net_stats_t collisions;

        net_stats_t tx_dropped;

        net_stats_t tx_timeout_count;

        net_stats_t tx_restart_queue;

        net_stats_t unknown_protocol;

#ifdef CONFIG_NET_STATISTICS_ETHERNET_VENDOR
        struct net_stats_eth_vendor *vendor;
#endif
};

struct net_stats_ppp {
        struct net_stats_bytes bytes;

        struct net_stats_pkts pkts;

        net_stats_t drop;

        net_stats_t chkerr;
};

struct net_stats_sta_mgmt {
        net_stats_t beacons_rx;

        net_stats_t beacons_miss;
};

struct net_stats_wifi {
        struct net_stats_sta_mgmt sta_mgmt;

        struct net_stats_bytes bytes;

        struct net_stats_pkts pkts;

        struct net_stats_pkts broadcast;

        struct net_stats_pkts multicast;

        struct net_stats_pkts errors;

        struct net_stats_pkts unicast;

        net_stats_t overrun_count;
};

#if defined(CONFIG_NET_STATISTICS_USER_API)
/* Management part definitions */


#define NET_STATS_LAYER NET_MGMT_LAYER_L3
#define NET_STATS_CODE          NET_MGMT_LAYER_CODE_STATS
#define NET_STATS_BASE          (NET_MGMT_LAYER(NET_STATS_LAYER) |      \
                                 NET_MGMT_LAYER_CODE(NET_STATS_CODE))

enum net_request_stats_cmd {
        NET_REQUEST_STATS_CMD_GET_ALL = 1,
        NET_REQUEST_STATS_CMD_GET_PROCESSING_ERROR,
        NET_REQUEST_STATS_CMD_GET_PKT_FILTER_DROP,
        NET_REQUEST_STATS_CMD_GET_BYTES,
        NET_REQUEST_STATS_CMD_GET_IP_ERRORS,
        NET_REQUEST_STATS_CMD_GET_IPV4,
        NET_REQUEST_STATS_CMD_GET_IPV6,
        NET_REQUEST_STATS_CMD_GET_IPV6_ND,
        NET_REQUEST_STATS_CMD_GET_IPV6_PMTU,
        NET_REQUEST_STATS_CMD_GET_IPV4_PMTU,
        NET_REQUEST_STATS_CMD_GET_ICMP,
        NET_REQUEST_STATS_CMD_GET_UDP,
        NET_REQUEST_STATS_CMD_GET_RAW,
        NET_REQUEST_STATS_CMD_GET_TCP,
        NET_REQUEST_STATS_CMD_GET_ETHERNET,
        NET_REQUEST_STATS_CMD_GET_PPP,
        NET_REQUEST_STATS_CMD_GET_PM,
        NET_REQUEST_STATS_CMD_GET_WIFI,
        NET_REQUEST_STATS_CMD_RESET_WIFI,
        NET_REQUEST_STATS_CMD_GET_VPN,
};


#define NET_REQUEST_STATS_GET_ALL                               \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_ALL)

#define NET_REQUEST_STATS_GET_PROCESSING_ERROR                          \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_PROCESSING_ERROR)

#define NET_REQUEST_STATS_GET_PKT_FILTER_DROP                   \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_PKT_FILTER_DROP)

#define NET_REQUEST_STATS_GET_BYTES                             \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_BYTES)

#define NET_REQUEST_STATS_GET_IP_ERRORS                         \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_IP_ERRORS)


NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_ALL);
NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_PROCESSING_ERROR);
NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_BYTES);
NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_IP_ERRORS);

#if defined(CONFIG_NET_STATISTICS_PKT_FILTER)
NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_PKT_FILTER_DROP);
#endif /* CONFIG_NET_STATISTICS_PKT_FILTER */


#if defined(CONFIG_NET_STATISTICS_IPV4)
#define NET_REQUEST_STATS_GET_IPV4                              \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_IPV4)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_IPV4);
#endif /* CONFIG_NET_STATISTICS_IPV4 */

#if defined(CONFIG_NET_STATISTICS_IPV6)
#define NET_REQUEST_STATS_GET_IPV6                              \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_IPV6)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_IPV6);
#endif /* CONFIG_NET_STATISTICS_IPV6 */

#if defined(CONFIG_NET_STATISTICS_IPV6_ND)
#define NET_REQUEST_STATS_GET_IPV6_ND                           \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_IPV6_ND)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_IPV6_ND);
#endif /* CONFIG_NET_STATISTICS_IPV6_ND */

#if defined(CONFIG_NET_STATISTICS_IPV6_PMTU)
#define NET_REQUEST_STATS_GET_IPV6_PMTU                         \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_IPV6_PMTU)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_IPV6_PMTU);
#endif /* CONFIG_NET_STATISTICS_IPV6_PMTU */

#if defined(CONFIG_NET_STATISTICS_IPV4_PMTU)
#define NET_REQUEST_STATS_GET_IPV4_PMTU                         \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_IPV4_PMTU)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_IPV4_PMTU);
#endif /* CONFIG_NET_STATISTICS_IPV4_PMTU */

#if defined(CONFIG_NET_STATISTICS_ICMP)
#define NET_REQUEST_STATS_GET_ICMP                              \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_ICMP)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_ICMP);
#endif /* CONFIG_NET_STATISTICS_ICMP */

#if defined(CONFIG_NET_STATISTICS_UDP)
#define NET_REQUEST_STATS_GET_UDP                               \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_UDP)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_UDP);
#endif /* CONFIG_NET_STATISTICS_UDP */

#if defined(CONFIG_NET_STATISTICS_RAW)
#define NET_REQUEST_STATS_GET_RAW                               \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_RAW)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_RAW);
#endif /* CONFIG_NET_STATISTICS_RAW */

#if defined(CONFIG_NET_STATISTICS_TCP)
#define NET_REQUEST_STATS_GET_TCP                               \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_TCP)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_TCP);
#endif /* CONFIG_NET_STATISTICS_TCP */

#if defined(CONFIG_NET_STATISTICS_ETHERNET)
#define NET_REQUEST_STATS_GET_ETHERNET                          \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_ETHERNET)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_ETHERNET);
#endif /* CONFIG_NET_STATISTICS_ETHERNET */

#if defined(CONFIG_NET_STATISTICS_PPP)
#define NET_REQUEST_STATS_GET_PPP                               \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_PPP)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_PPP);
#endif /* CONFIG_NET_STATISTICS_PPP */

#if defined(CONFIG_NET_STATISTICS_VPN)
#define NET_REQUEST_STATS_GET_VPN                               \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_VPN)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_VPN);
#endif /* CONFIG_NET_STATISTICS_VPN */

#endif /* CONFIG_NET_STATISTICS_USER_API */

#if defined(CONFIG_NET_STATISTICS_POWER_MANAGEMENT)
#define NET_REQUEST_STATS_GET_PM                                \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_PM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_PM);
#endif /* CONFIG_NET_STATISTICS_POWER_MANAGEMENT */

#if defined(CONFIG_NET_STATISTICS_WIFI)
#define NET_REQUEST_STATS_GET_WIFI                              \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_GET_WIFI)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_GET_WIFI);

#define NET_REQUEST_STATS_RESET_WIFI                              \
        (NET_STATS_BASE | NET_REQUEST_STATS_CMD_RESET_WIFI)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_STATS_RESET_WIFI);
#endif /* CONFIG_NET_STATISTICS_WIFI */

#define NET_STATS_GET_METRIC_NAME(_name) _name
#define NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx) net_stats_##dev_id##_##sfx##_collector
#define NET_STATS_GET_VAR(dev_id, sfx, var) zephyr_net_##dev_id##_##sfx##_##var
#define NET_STATS_GET_INSTANCE(dev_id, sfx, _not_used) STRINGIFY(_##dev_id##_##sfx)

/* The label value is set to be the network interface name. Note that we skip
 * the first character (_) when setting the label value. This can be changed
 * if there is a way to token paste the instance name without the prefix character.
 * Note also that the below macros have some parameters that are not used atm.
 */
#define NET_STATS_PROMETHEUS_COUNTER_DEFINE(_desc, _labelval, _not_used,        \
                                            _collector, _name, _stat_var_ptr)   \
        static PROMETHEUS_COUNTER_DEFINE(                                       \
                NET_STATS_GET_METRIC_NAME(_name),                               \
                _desc, ({ .key = "nic", .value = &_labelval[1] }),              \
                &(_collector), _stat_var_ptr)

#define NET_STATS_PROMETHEUS_GAUGE_DEFINE(_desc,  _labelval, _not_used,         \
                                          _collector, _name, _stat_var_ptr)     \
        static PROMETHEUS_GAUGE_DEFINE(                                         \
                NET_STATS_GET_METRIC_NAME(_name),                               \
                _desc, ({ .key = "nic", .value = &_labelval[1] }),              \
                &(_collector), _stat_var_ptr)

#define NET_STATS_PROMETHEUS_SUMMARY_DEFINE(_desc,  _labelval, _not_used,       \
                                            _collector, _name, _stat_var_ptr)   \
        static PROMETHEUS_SUMMARY_DEFINE(                                       \
                NET_STATS_GET_METRIC_NAME(_name),                               \
                _desc, ({ .key = "nic", .value = &_labelval[1] }),              \
                &(_collector), _stat_var_ptr)

#define NET_STATS_PROMETHEUS_HISTOGRAM_DEFINE(_desc, _labelval, _not_used,      \
                                              _collector, _name, _stat_var_ptr) \
        static PROMETHEUS_HISTOGRAM_DEFINE(                                     \
                NET_STATS_GET_METRIC_NAME(_name),                               \
                _desc, ({ .key = "nic", .value = &_labelval[1] }),              \
                &(_collector), _stat_var_ptr)

/* IPv6 layer statistics */
#if defined(CONFIG_NET_STATISTICS_IPV6)
#define NET_STATS_PROMETHEUS_IPV6(iface, dev_id, sfx)                   \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 packets sent",                                    \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_sent),         \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_sent),              \
                &(iface)->stats.ipv6.sent);                             \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 packets received",                                \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_recv),         \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_recv),              \
                &(iface)->stats.ipv6.recv);                             \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 packets dropped",                                 \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_drop),         \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_drop),              \
                &(iface)->stats.ipv6.drop);                             \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 packets forwarded",                               \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_forward),      \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_forwarded),         \
                &(iface)->stats.ipv6.forwarded)
#else
#define NET_STATS_PROMETHEUS_IPV6(iface, dev_id, sfx)
#endif

/* IPv4 layer statistics */
#if defined(CONFIG_NET_STATISTICS_IPV4)
#define NET_STATS_PROMETHEUS_IPV4(iface, dev_id, sfx)                   \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv4 packets sent",                                    \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv4_sent),         \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv4_sent),              \
                &(iface)->stats.ipv4.sent);                             \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv4 packets received",                                \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv4_recv),         \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv4_recv),              \
                &(iface)->stats.ipv4.recv);                             \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv4 packets dropped",                                 \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv4_drop),         \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv4_drop),              \
                &(iface)->stats.ipv4.drop);                             \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv4 packets forwarded",                               \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv4_forwarded),    \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv4_forwarded),         \
                &(iface)->stats.ipv4.forwarded)
#else
#define NET_STATS_PROMETHEUS_IPV4(iface, dev_id, sfx)
#endif

/* ICMP layer statistics */
#if defined(CONFIG_NET_STATISTICS_ICMP)
#define NET_STATS_PROMETHEUS_ICMP(iface, dev_id, sfx)                   \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "ICMP packets sent",                                    \
                NET_STATS_GET_INSTANCE(dev_id, sfx, icmp_sent),         \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, icmp_sent),              \
                &(iface)->stats.icmp.sent);                             \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "ICMP packets received",                                \
                NET_STATS_GET_INSTANCE(dev_id, sfx, icmp_recv),         \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, icmp_recv),              \
                &(iface)->stats.icmp.recv);                             \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "ICMP packets dropped",                                 \
                NET_STATS_GET_INSTANCE(dev_id, sfx, icmp_drop),         \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, icmp_drop),              \
                &(iface)->stats.icmp.drop);                             \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "ICMP packets checksum error",                          \
                NET_STATS_GET_INSTANCE(dev_id, sfx, icmp_chkerr),       \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, icmp_chkerr),            \
                &(iface)->stats.icmp.chkerr);                           \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "ICMP packets type error",                              \
                NET_STATS_GET_INSTANCE(dev_id, sfx, icmp_typeerr),      \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, icmp_typeerr),           \
                &(iface)->stats.icmp.typeerr)
#else
#define NET_STATS_PROMETHEUS_ICMP(iface, dev_id, sfx)
#endif

/* UDP layer statistics */
#if defined(CONFIG_NET_STATISTICS_UDP)
#define NET_STATS_PROMETHEUS_UDP(iface, dev_id, sfx)                    \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "UDP packets sent",                                     \
                NET_STATS_GET_INSTANCE(dev_id, sfx, udp_sent),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, udp_sent),               \
                &(iface)->stats.udp.sent);                              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "UDP packets received",                                 \
                NET_STATS_GET_INSTANCE(dev_id, sfx, udp_recv),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, udp_recv),               \
                &(iface)->stats.udp.recv);                              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "UDP packets dropped",                                  \
                NET_STATS_GET_INSTANCE(dev_id, sfx, udp_drop),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, udp_drop),               \
                &(iface)->stats.udp.drop);                              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "UDP packets checksum error",                           \
                NET_STATS_GET_INSTANCE(dev_id, sfx, udp_chkerr),        \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, udp_chkerr),             \
                &(iface)->stats.udp.chkerr)
#else
#define NET_STATS_PROMETHEUS_UDP(iface, dev_id, sfx)
#endif

/* Raw packet socket statistics */
#if defined(CONFIG_NET_STATISTICS_RAW)
#define NET_STATS_PROMETHEUS_RAW(iface, dev_id, sfx)                    \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Raw packets sent",                                     \
                NET_STATS_GET_INSTANCE(dev_id, sfx, raw_sent),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, raw_sent),               \
                &(iface)->stats.raw.sent);                              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Raw packets received",                                 \
                NET_STATS_GET_INSTANCE(dev_id, sfx, raw_recv),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, raw_recv),               \
                &(iface)->stats.raw.recv);                              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Raw packets dropped",                                  \
                NET_STATS_GET_INSTANCE(dev_id, sfx, raw_drop),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, raw_drop),               \
                &(iface)->stats.raw.drop);                              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Raw bytes sent",                                       \
                NET_STATS_GET_INSTANCE(dev_id, sfx, raw_bytes_sent),    \
                "byte_count",                                           \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, raw_bytes_sent),         \
                &(iface)->stats.raw.bytes.sent);                        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Raw bytes received",                                   \
                NET_STATS_GET_INSTANCE(dev_id, sfx, raw_bytes_recv),    \
                "byte_count",                                           \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, raw_bytes_recv),         \
                &(iface)->stats.raw.bytes.received)
#else
#define NET_STATS_PROMETHEUS_RAW(iface, dev_id, sfx)
#endif

/* TCP layer statistics */
#if defined(CONFIG_NET_STATISTICS_TCP)
#define NET_STATS_PROMETHEUS_TCP(iface, dev_id, sfx)                    \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP bytes sent",                                       \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_bytes_sent),    \
                "byte_count",                                           \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_bytes_sent),         \
                &(iface)->stats.tcp.bytes.sent);                        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP bytes received",                                   \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_bytes_recv),    \
                "byte_count",                                           \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_bytes_recv),         \
                &(iface)->stats.tcp.bytes.received);                    \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP bytes resent",                                     \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_bytes_resent),  \
                "byte_count",                                           \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_bytes_resent),       \
                &(iface)->stats.tcp.resent);                            \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP packets sent",                                     \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_sent),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_sent),               \
                &(iface)->stats.tcp.sent);                              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP packets received",                                 \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_recv),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_recv),               \
                &(iface)->stats.tcp.recv);                              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP packets dropped",                                  \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_drop),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_drop),               \
                &(iface)->stats.tcp.drop);                              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP packets checksum error",                           \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_chkerr),        \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_chkerr),             \
                &(iface)->stats.tcp.chkerr);                            \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP packets ack error",                                \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_ackerr),        \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_ackerr),             \
                &(iface)->stats.tcp.ackerr);                            \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP packets reset error",                              \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_rsterr),        \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_rsterr),             \
                &(iface)->stats.tcp.rsterr);                            \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP packets retransmitted",                            \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_rexmit),        \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_rexmit),             \
                &(iface)->stats.tcp.rexmit);                            \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP reset received",                                   \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_rst_recv),      \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_rst),                \
                &(iface)->stats.tcp.rst);                               \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP connection drop",                                  \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_conndrop),      \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_conndrop),           \
                &(iface)->stats.tcp.conndrop);                          \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "TCP connection reset",                                 \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tcp_connrst),       \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tcp_connrst),            \
                &(iface)->stats.tcp.connrst)
#else
#define NET_STATS_PROMETHEUS_TCP(iface, dev_id, sfx)
#endif

/* IPv6 Neighbor Discovery statistics */
#if defined(CONFIG_NET_STATISTICS_IPV6_ND)
#define NET_STATS_PROMETHEUS_IPV6_ND(iface, dev_id, sfx)                \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 ND packets sent",                                 \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_nd_sent),      \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_nd_sent),           \
                &(iface)->stats.ipv6_nd.sent);                          \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 ND packets received",                             \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_nd_recv),      \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_nd_recv),           \
                &(iface)->stats.ipv6_nd.recv);                          \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 ND packets dropped",                              \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_nd_drop),      \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_nd_drop),           \
                &(iface)->stats.ipv6_nd.drop)
#else
#define NET_STATS_PROMETHEUS_IPV6_ND(iface, dev_id, sfx)
#endif

/* IPv6 Path MTU Discovery statistics */
#if defined(CONFIG_NET_STATISTICS_IPV6_PMTU)
#define NET_STATS_PROMETHEUS_IPV6_PMTU(iface, dev_id, sfx)              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 PMTU packets sent",                               \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_pmtu_sent),    \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_pmtu_sent),         \
                &(iface)->stats.ipv6_pmtu.sent);                        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 PMTU packets received",                           \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_pmtu_recv),    \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_pmtu_recv),         \
                &(iface)->stats.ipv6_pmtu.recv);                        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 PMTU packets dropped",                            \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_pmtu_drop),    \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_pmtu_drop),         \
                &(iface)->stats.ipv6_pmtu.drop)
#else
#define NET_STATS_PROMETHEUS_IPV6_PMTU(iface, dev_id, sfx)
#endif

/* IPv4 Path MTU Discovery statistics */
#if defined(CONFIG_NET_STATISTICS_IPV4_PMTU)
#define NET_STATS_PROMETHEUS_IPV4_PMTU(iface, dev_id, sfx)              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv4 PMTU packets sent",                               \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv4_pmtu_sent),    \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv4_pmtu_sent),         \
                &(iface)->stats.ipv4_pmtu.sent);                        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv4 PMTU packets received",                           \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv4_pmtu_recv),    \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv4_pmtu_recv),         \
                &(iface)->stats.ipv4_pmtu.recv);                        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv4 PMTU packets dropped",                            \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv4_pmtu_drop),    \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv4_pmtu_drop),         \
                &(iface)->stats.ipv4_pmtu.drop)
#else
#define NET_STATS_PROMETHEUS_IPV4_PMTU(iface, dev_id, sfx)
#endif

/* IPv6 Multicast Listener Discovery statistics */
#if defined(CONFIG_NET_STATISTICS_MLD)
#define NET_STATS_PROMETHEUS_MLD(iface, dev_id, sfx)                    \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 MLD packets sent",                                \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_mld_sent),     \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_mld_sent),          \
                &(iface)->stats.ipv6_mld.sent);                         \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 MLD packets received",                            \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_mld_recv),     \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_mld_recv),          \
                &(iface)->stats.ipv6_mld.recv);                         \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv6 MLD packets dropped",                             \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv6_mld_drop),     \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv6_mld_drop),          \
                &(iface)->stats.ipv6_mld.drop)
#else
#define NET_STATS_PROMETHEUS_MLD(iface, dev_id, sfx)
#endif

/* IPv4 IGMP statistics */
#if defined(CONFIG_NET_STATISTICS_IGMP)
#define NET_STATS_PROMETHEUS_IGMP(iface, dev_id, sfx)                   \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv4 IGMP packets sent",                               \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv4_igmp_sent),    \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv4_igmp_sent),         \
                &(iface)->stats.ipv4_igmp.sent);                        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv4 IGMP packets received",                           \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv4_igmp_recv),    \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv4_igmp_recv),         \
                &(iface)->stats.ipv4_igmp.recv);                        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IPv4 IGMP packets dropped",                            \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ipv4_igmp_drop),    \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ipv4_igmp_drop),         \
                &(iface)->stats.ipv4_igmp.drop)
#else
#define NET_STATS_PROMETHEUS_IGMP(iface, dev_id, sfx)
#endif

/* DNS statistics */
#if defined(CONFIG_NET_STATISTICS_DNS)
#define NET_STATS_PROMETHEUS_DNS(iface, dev_id, sfx)                    \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "DNS packets sent",                                     \
                NET_STATS_GET_INSTANCE(dev_id, sfx, dns_sent),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, dns_sent),               \
                &(iface)->stats.dns.sent);                              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "DNS packets received",                                 \
                NET_STATS_GET_INSTANCE(dev_id, sfx, dns_recv),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, dns_recv),               \
                &(iface)->stats.dns.recv);                              \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "DNS packets dropped",                                  \
                NET_STATS_GET_INSTANCE(dev_id, sfx, dns_drop),          \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, dns_drop),               \
                &(iface)->stats.dns.drop)
#else
#define NET_STATS_PROMETHEUS_DNS(iface, dev_id, sfx)
#endif

/* TX time statistics */
#if defined(CONFIG_NET_PKT_TXTIME_STATS)
#define NET_STATS_PROMETHEUS_TX_TIME(iface, dev_id, sfx)                \
        NET_STATS_PROMETHEUS_SUMMARY_DEFINE(                            \
                "TX time in microseconds",                              \
                NET_STATS_GET_INSTANCE(dev_id, sfx, tx_time),           \
                "time",                                                 \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, tx_time),                \
                &(iface)->stats.tx_time)
#else
#define NET_STATS_PROMETHEUS_TX_TIME(iface, dev_id, sfx)
#endif

/* RX time statistics */
#if defined(CONFIG_NET_PKT_RXTIME_STATS)
#define NET_STATS_PROMETHEUS_RX_TIME(iface, dev_id, sfx)                \
        NET_STATS_PROMETHEUS_SUMMARY_DEFINE(                            \
                "RX time in microseconds",                              \
                NET_STATS_GET_INSTANCE(dev_id, sfx, rx_time),           \
                "time",                                                 \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, rx_time),                \
                &(iface)->stats.rx_time)
#else
#define NET_STATS_PROMETHEUS_RX_TIME(iface, dev_id, sfx)
#endif

#define NET_STATS_PROMETHEUS_PKT_FILTER_IPV4(iface, dev_id, sfx)        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Packet filter RX IPv4 drop",                           \
                NET_STATS_GET_INSTANCE(dev_id, sfx, pkt_filter_rx_ipv4_drop), \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, pkt_filter_rx_ipv4_drop),\
                &(iface)->stats.pkt_filter.rx.ipv4_drop);

#define NET_STATS_PROMETHEUS_PKT_FILTER_IPV6(iface, dev_id, sfx)        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Packet filter RX IPv6 drop",                           \
                NET_STATS_GET_INSTANCE(dev_id, sfx, pkt_filter_rx_ipv6_drop), \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, pkt_filter_rx_ipv6_drop),\
                &(iface)->stats.pkt_filter.rx.ipv6_drop);

#define NET_STATS_PROMETHEUS_PKT_FILTER_LOCAL(iface, dev_id, sfx)       \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Packet filter RX local drop",                          \
                NET_STATS_GET_INSTANCE(dev_id, sfx, pkt_filter_rx_local_drop), \
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, pkt_filter_rx_local_drop),\
                &(iface)->stats.pkt_filter.rx.local_drop);

#define NET_STATS_PROMETHEUS_PKT_FILTER(iface, dev_id, sfx)             \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Packet filter RX drop",                                \
                NET_STATS_GET_INSTANCE(dev_id, sfx, pkt_filter_rx_drop),\
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, pkt_filter_rx_drop),     \
                &(iface)->stats.pkt_filter.rx.drop);                    \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Packet filter TX drop",                                \
                NET_STATS_GET_INSTANCE(dev_id, sfx, pkt_filter_tx_drop),\
                "packet_count",                                         \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, pkt_filter_tx_drop),     \
                &(iface)->stats.pkt_filter.tx.drop);                    \
        IF_ENABLED(CONFIG_NET_PKT_FILTER_IPV4_HOOK,                     \
                   (NET_STATS_PROMETHEUS_PKT_FILTER_IPV4(iface, dev_id, sfx))) \
        IF_ENABLED(CONFIG_NET_PKT_FILTER_IPV6_HOOK,                     \
                   (NET_STATS_PROMETHEUS_PKT_FILTER_IPV6(iface, dev_id, sfx))) \
        IF_ENABLED(CONFIG_NET_PKT_FILTER_LOCAL_IN_HOOK,                 \
                   (NET_STATS_PROMETHEUS_PKT_FILTER_LOCAL(iface, dev_id, sfx)))

/* Per network interface statistics via Prometheus */
#define NET_STATS_PROMETHEUS(iface, dev_id, sfx)                        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Processing error",                                     \
                NET_STATS_GET_INSTANCE(dev_id, sfx, process_error),     \
                "error_count",                                          \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, processing_error),       \
                &(iface)->stats.processing_error);                      \
        IF_ENABLED(CONFIG_NET_STATISTICS_PKT_FILTER,                    \
                   (NET_STATS_PROMETHEUS_PKT_FILTER(iface, dev_id, sfx))) \
        /* IP layer error statistics */                                 \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IP proto error",                                       \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ip_proto_error),    \
                "error_count",                                          \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ip_errors_protoerr),     \
                &(iface)->stats.ip_errors.protoerr);                    \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IP version/header len error",                          \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ip_vhl_error),      \
                "error_count",                                          \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ip_errors_vhlerr),       \
                &(iface)->stats.ip_errors.vhlerr);                      \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IP header len error (high byte)",                      \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ip_hblen_error),    \
                "error_count",                                          \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ip_errors_hblenerr),     \
                &(iface)->stats.ip_errors.hblenerr);                    \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IP header len error (low byte)",                       \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ip_lblen_error),    \
                "error_count",                                          \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ip_errors_lblenerr),     \
                &(iface)->stats.ip_errors.lblenerr);                    \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IP fragment error",                                    \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ip_frag_error),     \
                "error_count",                                          \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ip_errors_fragerr),      \
                &(iface)->stats.ip_errors.fragerr);                     \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "IP checksum error",                                    \
                NET_STATS_GET_INSTANCE(dev_id, sfx, ip_chk_error),      \
                "error_count",                                          \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, ip_errors_chkerr),       \
                &(iface)->stats.ip_errors.chkerr);                      \
        /* General network statistics */                                \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Bytes received",                                       \
                NET_STATS_GET_INSTANCE(dev_id, sfx, bytes_recv),        \
                "byte_count",                                           \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, bytes_recv),             \
                &(iface)->stats.bytes.received);                        \
        NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
                "Bytes sent",                                           \
                NET_STATS_GET_INSTANCE(dev_id, sfx, bytes_sent),        \
                "byte_count",                                           \
                NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
                NET_STATS_GET_VAR(dev_id, sfx, bytes_sent),             \
                &(iface)->stats.bytes.sent);                            \
        NET_STATS_PROMETHEUS_IPV6(iface, dev_id, sfx);                  \
        NET_STATS_PROMETHEUS_IPV4(iface, dev_id, sfx);                  \
        NET_STATS_PROMETHEUS_ICMP(iface, dev_id, sfx);                  \
        NET_STATS_PROMETHEUS_UDP(iface, dev_id, sfx);                   \
        NET_STATS_PROMETHEUS_RAW(iface, dev_id, sfx);                   \
        NET_STATS_PROMETHEUS_TCP(iface, dev_id, sfx);                   \
        NET_STATS_PROMETHEUS_IPV6_ND(iface, dev_id, sfx);               \
        NET_STATS_PROMETHEUS_IPV6_PMTU(iface, dev_id, sfx);             \
        NET_STATS_PROMETHEUS_IPV4_PMTU(iface, dev_id, sfx);             \
        NET_STATS_PROMETHEUS_MLD(iface, dev_id, sfx);                   \
        NET_STATS_PROMETHEUS_IGMP(iface, dev_id, sfx);                  \
        NET_STATS_PROMETHEUS_DNS(iface, dev_id, sfx);                   \
        NET_STATS_PROMETHEUS_TX_TIME(iface, dev_id, sfx);               \
        NET_STATS_PROMETHEUS_RX_TIME(iface, dev_id, sfx)


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_NET_STATS_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 8 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 754 行

管理部分定义（management part definitions）。

### 注释 3：原第 817 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_PKT_FILTER`。

### 注释 4：原第 829 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_IPV4`。

### 注释 5：原第 839 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_IPV6`。

### 注释 6：原第 849 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_IPV6_ND`。

### 注释 7：原第 859 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_IPV6_PMTU`。

### 注释 8：原第 869 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_IPV4_PMTU`。

### 注释 9：原第 879 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_ICMP`。

### 注释 10：原第 889 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_UDP`。

### 注释 11：原第 899 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_RAW`。

### 注释 12：原第 909 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_TCP`。

### 注释 13：原第 919 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_ETHERNET`。

### 注释 14：原第 929 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_PPP`。

### 注释 15：原第 939 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_VPN`。

### 注释 16：原第 941 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_USER_API`。

### 注释 17：原第 951 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_POWER_MANAGEMENT`。

### 注释 18：原第 969 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_WIFI`。

### 注释 19：原第 976 行

标签值（label value）设为网络接口名称。注意，设置标签值时会跳过第一个字符 `_`。如果有办法在不带前缀字符的情况下通过令牌拼接（token paste）形成实例名称，可以修改此行为。另请注意，下方宏的部分参数目前未使用。

### 注释 20：原第 1009 行

IPv6 层统计（statistics）。

### 注释 21：原第 1044 行

IPv4 层统计（statistics）。

### 注释 22：原第 1079 行

互联网控制报文协议（ICMP）层统计。

### 注释 23：原第 1121 行

用户数据报协议（UDP）层统计。

### 注释 24：原第 1156 行

原始数据包套接字（Raw Packet Socket）统计信息。

### 注释 25：原第 1200 行

传输控制协议（TCP）层统计。

### 注释 26：原第 1298 行

IPv6 邻居发现（Neighbor Discovery）统计。

### 注释 27：原第 1326 行

IPv6路径MTU发现（Path MTU Discovery）统计信息。

### 注释 28：原第 1354 行

IPv4路径MTU发现（Path MTU Discovery）统计信息。

### 注释 29：原第 1382 行

IPv6 多播侦听者发现（Multicast Listener Discovery）统计。

### 注释 30：原第 1410 行

IPv4 互联网组管理协议（IGMP）统计。

### 注释 31：原第 1438 行

DNS统计信息（Statistics）。

### 注释 32：原第 1466 行

发送时间（TX time）统计。

### 注释 33：原第 1480 行

接收时间（RX time）统计。

### 注释 34：原第 1543 行

通过 Prometheus 提供的逐网络接口统计（per-network-interface statistics）。

### 注释 35：原第 1554 行

IP层错误（Error）统计信息。

### 注释 36：原第 1597 行

通用网络统计（general network statistics）。

### 注释 37：原第 1635 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_STATS_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_configuration_reference/P059_zephyr__net__net_stats.h_文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/net/net_core.h](../api_file_interface_reference/P037_zephyr__net__net_core.h_文件参考.md)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [zephyr/net/prometheus/collector.h](../api_file_management_reference/P004_zephyr__net__prometheus__collector.h_文件参考.md)
- [zephyr/net/prometheus/counter.h](../api_file_service_reference/P028_zephyr__net__prometheus__counter.h_文件参考.md)
- [zephyr/net/prometheus/metric.h](../api_file_supplement_reference/P066_zephyr__net__prometheus__metric.h_文件参考.md)
- [zephyr/net/prometheus/gauge.h](../api_file_configuration_reference/P031_zephyr__net__prometheus__gauge.h_文件参考.md)
- [zephyr/net/prometheus/histogram.h](../api_file_configuration_reference/P037_zephyr__net__prometheus__histogram.h_文件参考.md)
- [zephyr/net/prometheus/summary.h](../api_file_runtime_reference/P068_zephyr__net__prometheus__summary.h_文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [net_stats_t](../api_platform_topic_reference/P068_网络统计库（Network Statistics Library）.md#ga05ec15873e79256c287f21b6b6fcd752)
- [net_stats_bytes](../network_core_model_reference/P126_net_stats_bytes_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [sent](../network_core_model_reference/P126_net_stats_bytes_结构体.md#a360bdbf177d60b0677beec2037f34cb0)
- [received](../network_core_model_reference/P126_net_stats_bytes_结构体.md#a9f87e32d63bc4239ef7db03feedd495e)
- [net_stats_pkts](../network_core_model_reference/P142_net_stats_pkts_结构体.md)
- [tx](../network_core_model_reference/P142_net_stats_pkts_结构体.md#aee1e302d0f8dac79b693a06d8fa3b3c5)
- [rx](../network_core_model_reference/P142_net_stats_pkts_结构体.md#ac9784b5a245e6c57e39318aaf314f0cf)
- [net_stats_ip](../network_core_model_reference/P134_net_stats_ip_结构体.md)
- [recv](../network_core_model_reference/P134_net_stats_ip_结构体.md#ab6a6373368dd24cb51504c5729d535d3)
- [sent](../network_core_model_reference/P134_net_stats_ip_结构体.md#abbe676bbe9faa89b2b6b8c4950b1c9d5)
- [forwarded](../network_core_model_reference/P134_net_stats_ip_结构体.md#a4bb82a5ebebaa3e8a11973c07eed96a0)
- [drop](../network_core_model_reference/P134_net_stats_ip_结构体.md#ac86399b70d7f761162e5336dd15589eb)
- [net_stats_ip_errors](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md)
- [vhlerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#a3e476f659ebeaa5c5f7b6dad2d90326f)
- [hblenerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#a06b35742c418ebc6414fcb5c7002edde)
- [lblenerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#a9b4bf05e9df13e1d99518125b9067bef)
- [fragerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#ab84ee9dfbe5da391d60c6e3ae9abea16)
- [chkerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#a872cc0beca45bbe87ae794dd8ca4e301)
- [protoerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#a978b1c23847e707ac1fa27c2b34fa85d)
- [net_stats_icmp](../network_core_model_reference/P133_net_stats_icmp_结构体.md)
- [recv](../network_core_model_reference/P133_net_stats_icmp_结构体.md#ae6f226b55565c11fca0c9e099f08c267)
- [sent](../network_core_model_reference/P133_net_stats_icmp_结构体.md#a2d6eb7dfc8f4b439b399b039022f2889)
- [drop](../network_core_model_reference/P133_net_stats_icmp_结构体.md#a755f3388c05d4bd2988ddd16d1a4cf32)
- [typeerr](../network_core_model_reference/P133_net_stats_icmp_结构体.md#ae1a29dd9b8e1ce9a737fa7f36c805cd4)
- [chkerr](../network_core_model_reference/P133_net_stats_icmp_结构体.md#a6662bc547107a08c52e902a2446629bf)
- [net_stats_tcp](../network_core_model_reference/P149_net_stats_tcp_结构体.md)
- [bytes](../network_core_model_reference/P149_net_stats_tcp_结构体.md#af80c18bcc253133ce5f0597ac190b349)
- [resent](../network_core_model_reference/P149_net_stats_tcp_结构体.md#abe567032cb4a267a984aec28c1e3cca4)
- [drop](../network_core_model_reference/P149_net_stats_tcp_结构体.md#aa549f7b6d5828009a09190fd64afa8e3)
- [recv](../network_core_model_reference/P149_net_stats_tcp_结构体.md#ad25edb2b39a6acc8152c35ad43a5042f)
- [sent](../network_core_model_reference/P149_net_stats_tcp_结构体.md#aa987bebf96000b6b4e92bfafc218759a)
- [seg_drop](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a5f045704859331918511e9c2281ac155)
- [chkerr](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a5099e174b0eafa322f0630f1f5c73a8b)
- [ackerr](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a0d40abc85776f0a9b9510a909b7f6d18)
- [rsterr](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a471fcd5578f79ce77d20547b28503ac1)
- [rst](../network_core_model_reference/P149_net_stats_tcp_结构体.md#aa618cf86b962aca0f14eb9178c8ae61a)
- [rexmit](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a4a4ea6e5d87ef58b4271bd708cf39635)
- [conndrop](../network_core_model_reference/P149_net_stats_tcp_结构体.md#ac557ac0d8917bc2c2dfed74126f993c8)
- [connrst](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a67f55954a4c51f2b957c7d974e78c1c0)
- [net_stats_udp](../network_core_model_reference/P151_net_stats_udp_结构体.md)
- [drop](../network_core_model_reference/P151_net_stats_udp_结构体.md#a2d884bf9106e60d430ffec7c7964a609)
- [recv](../network_core_model_reference/P151_net_stats_udp_结构体.md#a0ea91d85fe322661fb909f5e94e55a34)
- [sent](../network_core_model_reference/P151_net_stats_udp_结构体.md#ab4e8228c221901d3ded55f3f823bfa1c)
- [chkerr](../network_core_model_reference/P151_net_stats_udp_结构体.md#a4c57d5f68ebda7981400729b9c7fe0f7)
- [net_stats_raw](../network_core_model_reference/P145_net_stats_raw_结构体.md)
- [bytes](../network_core_model_reference/P145_net_stats_raw_结构体.md#ac83a096e59c4483528a67f7209fba257)
- [drop](../network_core_model_reference/P145_net_stats_raw_结构体.md#aea0d3bd2836853e9f8ed6af489ad42ef)
- [recv](../network_core_model_reference/P145_net_stats_raw_结构体.md#a0decb52f848bf006f52cd575e181ffeb)
- [sent](../network_core_model_reference/P145_net_stats_raw_结构体.md#ab78de1ea1ec2ff46e6f1f248cebd5fac)
- [net_stats_ipv6_nd](../network_core_model_reference/P139_net_stats_ipv6_nd_结构体.md)
- [drop](../network_core_model_reference/P139_net_stats_ipv6_nd_结构体.md#a31074d5d44138fcabdc5f7750f9f2c47)
- [recv](../network_core_model_reference/P139_net_stats_ipv6_nd_结构体.md#a0bf6f67d9112996a3b002ea160aec769)
- [sent](../network_core_model_reference/P139_net_stats_ipv6_nd_结构体.md#a0129f7892a4439c20deb2f32b9001277)
- [net_stats_ipv6_pmtu](../network_core_model_reference/P140_net_stats_ipv6_pmtu_结构体.md)
- [drop](../network_core_model_reference/P140_net_stats_ipv6_pmtu_结构体.md#a68b19ebb61e84eb876178a31c7a4e327)
- [recv](../network_core_model_reference/P140_net_stats_ipv6_pmtu_结构体.md#a66346cd9140e30727d77648f65345762)
- [sent](../network_core_model_reference/P140_net_stats_ipv6_pmtu_结构体.md#a698f5794b73896f7a66def2d3209fafd)
- [net_stats_ipv4_pmtu](../network_core_model_reference/P137_net_stats_ipv4_pmtu_结构体.md)
- [drop](../network_core_model_reference/P137_net_stats_ipv4_pmtu_结构体.md#ad35f9defad7c5ce29e510b8051788977)
- [recv](../network_core_model_reference/P137_net_stats_ipv4_pmtu_结构体.md#a64245eb7b9b1fcfa0f0efcb53eff7ec2)
- [sent](../network_core_model_reference/P137_net_stats_ipv4_pmtu_结构体.md#a44f1028694d4001cd4a43f925f0bf0da)
- [net_stats_ipv6_mld](../network_core_model_reference/P138_net_stats_ipv6_mld_结构体.md)
- [recv](../network_core_model_reference/P138_net_stats_ipv6_mld_结构体.md#a4879ff9e31f8b60973d3b169598e921d)
- [sent](../network_core_model_reference/P138_net_stats_ipv6_mld_结构体.md#ab397b74b14ce7047bf2fc63ca72ce1e5)
- [drop](../network_core_model_reference/P138_net_stats_ipv6_mld_结构体.md#ad85dc87f57296a1e7d64e959b0370ee8)
- [net_stats_ipv4_igmp](../network_core_model_reference/P136_net_stats_ipv4_igmp_结构体.md)
- [recv](../network_core_model_reference/P136_net_stats_ipv4_igmp_结构体.md#a469113de7af0ba42dbd1b0365d00602c)
- [sent](../network_core_model_reference/P136_net_stats_ipv4_igmp_结构体.md#a955e20a6ee5e19e08000b3114b9d71a6)
- [drop](../network_core_model_reference/P136_net_stats_ipv4_igmp_结构体.md#a1c37702ff837b8c5cc9df5f690e7678c)
- [net_stats_dns](../network_core_model_reference/P127_net_stats_dns_结构体.md)
- [recv](../network_core_model_reference/P127_net_stats_dns_结构体.md#abc9be2039a3ff9e62b956ae27fd0ab84)
- [sent](../network_core_model_reference/P127_net_stats_dns_结构体.md#ac07b9f4d084b978cc11e7799fb71a435)
- [drop](../network_core_model_reference/P127_net_stats_dns_结构体.md#a04756603a183f35dbf6f55000556b546)
- [net_stats_tx_time](../network_core_model_reference/P150_net_stats_tx_time_结构体.md)
- [sum](../network_core_model_reference/P150_net_stats_tx_time_结构体.md#af6f7a26c0344a0f93306e105a8917c3e)
- [count](../network_core_model_reference/P150_net_stats_tx_time_结构体.md#a7a652350ed04e53ba02aec294f8444b4)
- [net_stats_rx_time](../network_core_model_reference/P146_net_stats_rx_time_结构体.md)
- [sum](../network_core_model_reference/P146_net_stats_rx_time_结构体.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d)
- [count](../network_core_model_reference/P146_net_stats_rx_time_结构体.md#a68247051b064de081fa2e84118192958)
- [net_stats_tc](../network_core_model_reference/P148_net_stats_tc_结构体.md)
- [bytes](../network_core_model_reference/P148_net_stats_tc_结构体.md#a74b471b77fb1c72933daa656319cc2af)
- [tx_time](../network_core_model_reference/P148_net_stats_tc_结构体.md#a30288ef3bb0796cd18c3cf0aedbe875a)
- [pkts](../network_core_model_reference/P148_net_stats_tc_结构体.md#a6614b5f5186635415a7d787260c39248)
- [dropped](../network_core_model_reference/P148_net_stats_tc_结构体.md#a1794f71f7fe7b3d20d406be4b28eb032)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [priority](../network_core_model_reference/P148_net_stats_tc_结构体.md#a8a5c2e59990407ddbfc7973a1c183bf6)
- [sent](../network_core_model_reference/P148_net_stats_tc_结构体.md#a8d6a3ebcc49ce8c34a5faae986f648e2)
- [rx_time](../network_core_model_reference/P148_net_stats_tc_结构体.md#a8ea00824bb0fb18e4d8912343e01c3b7)
- [recv](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)
- [net_stats_pm](../network_core_model_reference/P143_net_stats_pm_结构体.md)
- [overall_suspend_time](../network_core_model_reference/P143_net_stats_pm_结构体.md#ab43935fcfe9efc1cd5f3e7e329996805)
- [suspend_count](../network_core_model_reference/P143_net_stats_pm_结构体.md#ac14122a4765c499c045f18c70af355a0)
- [last_suspend_time](../network_core_model_reference/P143_net_stats_pm_结构体.md#a0bdf9c3676298e2df4ff3bfa03f5e823)
- [start_time](../network_core_model_reference/P143_net_stats_pm_结构体.md#a6784806eaa093431ed3c0f7acfe5a89c)
- [net_stats_pkt_filter](../network_core_model_reference/P141_net_stats_pkt_filter_结构体.md)
- [drop](../network_core_model_reference/P141_net_stats_pkt_filter_结构体.md#a62d2d86781e6224b09f21929f27b2ef7)
- [rx](../network_core_model_reference/P141_net_stats_pkt_filter_结构体.md#a8cf9912d574873832b85a614eb776789)
- [tx](../network_core_model_reference/P141_net_stats_pkt_filter_结构体.md#a5e88001e143c0adb129ca93b108c277d)
- [net_stats](../network_core_model_reference/P125_net_stats_结构体.md)
- [bytes](../network_core_model_reference/P125_net_stats_结构体.md#a7a28233e6d23efdce0143469b9bb6c05)
- [processing_error](../network_core_model_reference/P125_net_stats_结构体.md#a3a4c90661d6b310b628262228a341fe2)
- [ip_errors](../network_core_model_reference/P125_net_stats_结构体.md#ac42cb13954d164e92a1ef60919a2a34e)
- [net_stats_eth_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md)
- [rx_length_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#aca0e2e4807fa70279dee8ddaad2d7ef7)
- [rx_over_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a9afee89f5bb01907e7cd515e2a0ff1b5)
- [rx_crc_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a4dab70cf219269bb393ce14faf0ed77e)
- [rx_frame_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a8dfcc5cd1b4decec5783d01ba7033b05)
- [rx_no_buffer_count](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a82622736d226b4d3b999f1f22ccf8529)
- [rx_missed_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a2d2b2c4e3764ebec841f1ecbe7058d99)
- [rx_long_length_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a0e83e270a35222ed3e927800be4159e7)
- [rx_short_length_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a5e3d39d8417bb180cbfcb8c901006e81)
- [rx_align_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a7618f10af3443c49a6e256bb41e77781)
- [rx_dma_failed](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a7bcfbb13836f162ceeb5f021304b5c76)
- [rx_buf_alloc_failed](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#adbcae9c10c081f1cdf304bcdce740aa4)
- [tx_aborted_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#afec6a7e24c6f3cc74dd9f739f27b3e48)
- [tx_carrier_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a0043d1a1481040a6d7439bd23423ec12)
- [tx_fifo_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a84630da9b82557f56dc35cd59ca2f7ae)
- [tx_heartbeat_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#ae2a13733c1a5f0cc3e00efca0c3f429d)
- [tx_window_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a17624a12d6473bdd78698076fed0d122)
- [tx_dma_failed](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#abfbf6478b7afdd5935d7c6948c9ef426)
- [uncorr_ecc_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a07d0a435f2129556520c732571d28edf)
- [corr_ecc_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a257113639f0e0e3085febb7a147f498f)
- [net_stats_eth_flow](../network_core_model_reference/P131_net_stats_eth_flow_结构体.md)
- [rx_flow_control_xon](../network_core_model_reference/P131_net_stats_eth_flow_结构体.md#a08e5da4ff78fe3893b9c9a628cefe4f2)
- [rx_flow_control_xoff](../network_core_model_reference/P131_net_stats_eth_flow_结构体.md#a8f9b93537b3c11be70f276aaa72cb637)
- [tx_flow_control_xon](../network_core_model_reference/P131_net_stats_eth_flow_结构体.md#a31412e8bf9d38ba630ea856e958a48d7)
- [tx_flow_control_xoff](../network_core_model_reference/P131_net_stats_eth_flow_结构体.md#a969d81f9db20312d2d2aa7f70f93bdd5)
- [net_stats_eth_csum](../network_core_model_reference/P129_net_stats_eth_csum_结构体.md)
- [rx_csum_offload_good](../network_core_model_reference/P129_net_stats_eth_csum_结构体.md#a1f1ba5c01c6232cd739d069ddb871b17)
- [rx_csum_offload_errors](../network_core_model_reference/P129_net_stats_eth_csum_结构体.md#ac4fc04d66193070d4f52a4c07f29ccce)
- [net_stats_eth_hw_timestamp](../network_core_model_reference/P132_net_stats_eth_hw_timestamp_结构体.md)
- [rx_hwtstamp_cleared](../network_core_model_reference/P132_net_stats_eth_hw_timestamp_结构体.md#acd3d5f72d7df568110d96093e0c9534d)
- [tx_hwtstamp_timeouts](../network_core_model_reference/P132_net_stats_eth_hw_timestamp_结构体.md#a41f605499dbf88a879522fdfa4633d9e)
- [tx_hwtstamp_skipped](../network_core_model_reference/P132_net_stats_eth_hw_timestamp_结构体.md#ae1f983faf4a999308c464e4af5a5284b)
- [net_stats_eth](../network_core_model_reference/P128_net_stats_eth_结构体.md)
- [bytes](../network_core_model_reference/P128_net_stats_eth_结构体.md#a8c5cf1ead8ba214425a16fed1c2ad0fb)
- [pkts](../network_core_model_reference/P128_net_stats_eth_结构体.md#a97bd6026b16890743f344751a21107f1)
- [broadcast](../network_core_model_reference/P128_net_stats_eth_结构体.md#a054beb909134b0e0f22f5df599549128)
- [multicast](../network_core_model_reference/P128_net_stats_eth_结构体.md#a4f6a2903330518a132e7e547820e0bf2)
- [errors](../network_core_model_reference/P128_net_stats_eth_结构体.md#a9c869740f416fbe0b54d7fefacb1fe29)
- [error_details](../network_core_model_reference/P128_net_stats_eth_结构体.md#a922feddb17fc020371f1bcc52c709415)
- [flow_control](../network_core_model_reference/P128_net_stats_eth_结构体.md#a643010ac6360c8c0c08016725ba12222)
- [csum](../network_core_model_reference/P128_net_stats_eth_结构体.md#a2169ae06bace1a93663bccf88c8d7a29)
- [hw_timestamp](../network_core_model_reference/P128_net_stats_eth_结构体.md#a44667efff73c17c089ed22d5b0da5ad3)
- [collisions](../network_core_model_reference/P128_net_stats_eth_结构体.md#a822d4205791f59999c842610522f6fc5)
- [tx_dropped](../network_core_model_reference/P128_net_stats_eth_结构体.md#a257c349cf3d32d38796e3899e702454a)
- [tx_timeout_count](../network_core_model_reference/P128_net_stats_eth_结构体.md#ab351258ae82abd09759d37774559d8bc)
- [tx_restart_queue](../network_core_model_reference/P128_net_stats_eth_结构体.md#a6699012226e25e8bad39076fed6dbfb5)
- [unknown_protocol](../network_core_model_reference/P128_net_stats_eth_结构体.md#afaacee7cc1d0a35ae2344175421c40dd)
- [net_stats_ppp](../network_core_model_reference/P144_net_stats_ppp_结构体.md)
- [bytes](../network_core_model_reference/P144_net_stats_ppp_结构体.md#ab2b48da7f19d4b83e3f41b41979b7ed8)
- [pkts](../network_core_model_reference/P144_net_stats_ppp_结构体.md#a71fc81f3c5f3e65a476b3391f086d340)
- [drop](../network_core_model_reference/P144_net_stats_ppp_结构体.md#ae2e0a47a539e9d7bc97f9c63f889b276)
- [chkerr](../network_core_model_reference/P144_net_stats_ppp_结构体.md#a1332b31980f82236aeb0c3f9444e2ac6)
- [net_stats_sta_mgmt](../network_core_model_reference/P147_net_stats_sta_mgmt_结构体.md)
- [beacons_rx](../network_core_model_reference/P147_net_stats_sta_mgmt_结构体.md#ac6e68fded8e19b20259442436923f815)
- [beacons_miss](../network_core_model_reference/P147_net_stats_sta_mgmt_结构体.md#a29ae0079b4c780e0de2656a85ec15fe9)
- [net_stats_wifi](../network_core_model_reference/P153_net_stats_wifi_结构体.md)
- [sta_mgmt](../network_core_model_reference/P153_net_stats_wifi_结构体.md#a8bee22961545674e6ab100b58a04bf91)
- [bytes](../network_core_model_reference/P153_net_stats_wifi_结构体.md#aa055b1e8bd8f1e50815c1028b562be07)
- [pkts](../network_core_model_reference/P153_net_stats_wifi_结构体.md#adbcdb2dd8733f2917c00a0b2d365393b)
- [broadcast](../network_core_model_reference/P153_net_stats_wifi_结构体.md#a03dc04638c4b670bd7f3520d45fc1eda)
- [multicast](../network_core_model_reference/P153_net_stats_wifi_结构体.md#a7e7f68215101885fd51c70e981da26e7)
- [errors](../network_core_model_reference/P153_net_stats_wifi_结构体.md#ae0149e64a94a9f96eb6680f94793c8c4)
- [unicast](../network_core_model_reference/P153_net_stats_wifi_结构体.md#ae80dcd73a3c5ce3ec3282d1ae827b338)
- [overrun_count](../network_core_model_reference/P153_net_stats_wifi_结构体.md#ac498c9e517f2cb2eb01d251e84159e7e)
- [NET_MGMT_DEFINE_REQUEST_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga08bde8717fd8e12a338c517b22b87776)
- [collector.h](../api_file_management_reference/P004_zephyr__net__prometheus__collector.h_文件参考.md)
- [gauge.h](../api_file_configuration_reference/P031_zephyr__net__prometheus__gauge.h_文件参考.md)
- [histogram.h](../api_file_configuration_reference/P037_zephyr__net__prometheus__histogram.h_文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [metric.h](../api_file_supplement_reference/P066_zephyr__net__prometheus__metric.h_文件参考.md)
- [counter.h](../api_file_service_reference/P028_zephyr__net__prometheus__counter.h_文件参考.md)
- [net_core.h](../api_file_interface_reference/P037_zephyr__net__net_core.h_文件参考.md)
- [net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [net_stats_bytes::sent](../network_core_model_reference/P126_net_stats_bytes_结构体.md#a360bdbf177d60b0677beec2037f34cb0)
- [net_stats_bytes::received](../network_core_model_reference/P126_net_stats_bytes_结构体.md#a9f87e32d63bc4239ef7db03feedd495e)
- [net_stats_dns::drop](../network_core_model_reference/P127_net_stats_dns_结构体.md#a04756603a183f35dbf6f55000556b546)
- [net_stats_dns::recv](../network_core_model_reference/P127_net_stats_dns_结构体.md#abc9be2039a3ff9e62b956ae27fd0ab84)
- [net_stats_dns::sent](../network_core_model_reference/P127_net_stats_dns_结构体.md#ac07b9f4d084b978cc11e7799fb71a435)
- [net_stats_eth_csum::rx_csum_offload_good](../network_core_model_reference/P129_net_stats_eth_csum_结构体.md#a1f1ba5c01c6232cd739d069ddb871b17)
- [net_stats_eth_csum::rx_csum_offload_errors](../network_core_model_reference/P129_net_stats_eth_csum_结构体.md#ac4fc04d66193070d4f52a4c07f29ccce)
- [net_stats_eth_errors::tx_carrier_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a0043d1a1481040a6d7439bd23423ec12)
- [net_stats_eth_errors::uncorr_ecc_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a07d0a435f2129556520c732571d28edf)
- [net_stats_eth_errors::rx_long_length_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a0e83e270a35222ed3e927800be4159e7)
- [net_stats_eth_errors::tx_window_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a17624a12d6473bdd78698076fed0d122)
- [net_stats_eth_errors::corr_ecc_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a257113639f0e0e3085febb7a147f498f)
- [net_stats_eth_errors::rx_missed_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a2d2b2c4e3764ebec841f1ecbe7058d99)
- [net_stats_eth_errors::rx_crc_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a4dab70cf219269bb393ce14faf0ed77e)
- [net_stats_eth_errors::rx_short_length_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a5e3d39d8417bb180cbfcb8c901006e81)
- [net_stats_eth_errors::rx_align_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a7618f10af3443c49a6e256bb41e77781)
- [net_stats_eth_errors::rx_dma_failed](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a7bcfbb13836f162ceeb5f021304b5c76)
- [net_stats_eth_errors::rx_no_buffer_count](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a82622736d226b4d3b999f1f22ccf8529)
- [net_stats_eth_errors::tx_fifo_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a84630da9b82557f56dc35cd59ca2f7ae)
- [net_stats_eth_errors::rx_frame_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a8dfcc5cd1b4decec5783d01ba7033b05)
- [net_stats_eth_errors::rx_over_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#a9afee89f5bb01907e7cd515e2a0ff1b5)
- [net_stats_eth_errors::tx_dma_failed](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#abfbf6478b7afdd5935d7c6948c9ef426)
- [net_stats_eth_errors::rx_length_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#aca0e2e4807fa70279dee8ddaad2d7ef7)
- [net_stats_eth_errors::rx_buf_alloc_failed](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#adbcae9c10c081f1cdf304bcdce740aa4)
- [net_stats_eth_errors::tx_heartbeat_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#ae2a13733c1a5f0cc3e00efca0c3f429d)
- [net_stats_eth_errors::tx_aborted_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md#afec6a7e24c6f3cc74dd9f739f27b3e48)
- [net_stats_eth_flow::rx_flow_control_xon](../network_core_model_reference/P131_net_stats_eth_flow_结构体.md#a08e5da4ff78fe3893b9c9a628cefe4f2)
- [net_stats_eth_flow::tx_flow_control_xon](../network_core_model_reference/P131_net_stats_eth_flow_结构体.md#a31412e8bf9d38ba630ea856e958a48d7)
- [net_stats_eth_flow::rx_flow_control_xoff](../network_core_model_reference/P131_net_stats_eth_flow_结构体.md#a8f9b93537b3c11be70f276aaa72cb637)
- [net_stats_eth_flow::tx_flow_control_xoff](../network_core_model_reference/P131_net_stats_eth_flow_结构体.md#a969d81f9db20312d2d2aa7f70f93bdd5)
- [net_stats_eth_hw_timestamp::tx_hwtstamp_timeouts](../network_core_model_reference/P132_net_stats_eth_hw_timestamp_结构体.md#a41f605499dbf88a879522fdfa4633d9e)
- [net_stats_eth_hw_timestamp::rx_hwtstamp_cleared](../network_core_model_reference/P132_net_stats_eth_hw_timestamp_结构体.md#acd3d5f72d7df568110d96093e0c9534d)
- [net_stats_eth_hw_timestamp::tx_hwtstamp_skipped](../network_core_model_reference/P132_net_stats_eth_hw_timestamp_结构体.md#ae1f983faf4a999308c464e4af5a5284b)
- [net_stats_eth::broadcast](../network_core_model_reference/P128_net_stats_eth_结构体.md#a054beb909134b0e0f22f5df599549128)
- [net_stats_eth::csum](../network_core_model_reference/P128_net_stats_eth_结构体.md#a2169ae06bace1a93663bccf88c8d7a29)
- [net_stats_eth::tx_dropped](../network_core_model_reference/P128_net_stats_eth_结构体.md#a257c349cf3d32d38796e3899e702454a)
- [net_stats_eth::hw_timestamp](../network_core_model_reference/P128_net_stats_eth_结构体.md#a44667efff73c17c089ed22d5b0da5ad3)
- [net_stats_eth::multicast](../network_core_model_reference/P128_net_stats_eth_结构体.md#a4f6a2903330518a132e7e547820e0bf2)
- [net_stats_eth::flow_control](../network_core_model_reference/P128_net_stats_eth_结构体.md#a643010ac6360c8c0c08016725ba12222)
- [net_stats_eth::tx_restart_queue](../network_core_model_reference/P128_net_stats_eth_结构体.md#a6699012226e25e8bad39076fed6dbfb5)
- [net_stats_eth::collisions](../network_core_model_reference/P128_net_stats_eth_结构体.md#a822d4205791f59999c842610522f6fc5)
- [net_stats_eth::bytes](../network_core_model_reference/P128_net_stats_eth_结构体.md#a8c5cf1ead8ba214425a16fed1c2ad0fb)
- [net_stats_eth::error_details](../network_core_model_reference/P128_net_stats_eth_结构体.md#a922feddb17fc020371f1bcc52c709415)
- [net_stats_eth::pkts](../network_core_model_reference/P128_net_stats_eth_结构体.md#a97bd6026b16890743f344751a21107f1)
- [net_stats_eth::errors](../network_core_model_reference/P128_net_stats_eth_结构体.md#a9c869740f416fbe0b54d7fefacb1fe29)
- [net_stats_eth::tx_timeout_count](../network_core_model_reference/P128_net_stats_eth_结构体.md#ab351258ae82abd09759d37774559d8bc)
- [net_stats_eth::unknown_protocol](../network_core_model_reference/P128_net_stats_eth_结构体.md#afaacee7cc1d0a35ae2344175421c40dd)
- [net_stats_icmp::sent](../network_core_model_reference/P133_net_stats_icmp_结构体.md#a2d6eb7dfc8f4b439b399b039022f2889)
- [net_stats_icmp::chkerr](../network_core_model_reference/P133_net_stats_icmp_结构体.md#a6662bc547107a08c52e902a2446629bf)
- [net_stats_icmp::drop](../network_core_model_reference/P133_net_stats_icmp_结构体.md#a755f3388c05d4bd2988ddd16d1a4cf32)
- [net_stats_icmp::typeerr](../network_core_model_reference/P133_net_stats_icmp_结构体.md#ae1a29dd9b8e1ce9a737fa7f36c805cd4)
- [net_stats_icmp::recv](../network_core_model_reference/P133_net_stats_icmp_结构体.md#ae6f226b55565c11fca0c9e099f08c267)
- [net_stats_ip_errors::hblenerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#a06b35742c418ebc6414fcb5c7002edde)
- [net_stats_ip_errors::vhlerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#a3e476f659ebeaa5c5f7b6dad2d90326f)
- [net_stats_ip_errors::chkerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#a872cc0beca45bbe87ae794dd8ca4e301)
- [net_stats_ip_errors::protoerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#a978b1c23847e707ac1fa27c2b34fa85d)
- [net_stats_ip_errors::lblenerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#a9b4bf05e9df13e1d99518125b9067bef)
- [net_stats_ip_errors::fragerr](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md#ab84ee9dfbe5da391d60c6e3ae9abea16)
- [net_stats_ip::forwarded](../network_core_model_reference/P134_net_stats_ip_结构体.md#a4bb82a5ebebaa3e8a11973c07eed96a0)
- [net_stats_ip::recv](../network_core_model_reference/P134_net_stats_ip_结构体.md#ab6a6373368dd24cb51504c5729d535d3)
- [net_stats_ip::sent](../network_core_model_reference/P134_net_stats_ip_结构体.md#abbe676bbe9faa89b2b6b8c4950b1c9d5)
- [net_stats_ip::drop](../network_core_model_reference/P134_net_stats_ip_结构体.md#ac86399b70d7f761162e5336dd15589eb)
- [net_stats_ipv4_igmp::drop](../network_core_model_reference/P136_net_stats_ipv4_igmp_结构体.md#a1c37702ff837b8c5cc9df5f690e7678c)
- [net_stats_ipv4_igmp::recv](../network_core_model_reference/P136_net_stats_ipv4_igmp_结构体.md#a469113de7af0ba42dbd1b0365d00602c)
- [net_stats_ipv4_igmp::sent](../network_core_model_reference/P136_net_stats_ipv4_igmp_结构体.md#a955e20a6ee5e19e08000b3114b9d71a6)
- [net_stats_ipv4_pmtu::sent](../network_core_model_reference/P137_net_stats_ipv4_pmtu_结构体.md#a44f1028694d4001cd4a43f925f0bf0da)
- [net_stats_ipv4_pmtu::recv](../network_core_model_reference/P137_net_stats_ipv4_pmtu_结构体.md#a64245eb7b9b1fcfa0f0efcb53eff7ec2)
- [net_stats_ipv4_pmtu::drop](../network_core_model_reference/P137_net_stats_ipv4_pmtu_结构体.md#ad35f9defad7c5ce29e510b8051788977)
- [net_stats_ipv6_mld::recv](../network_core_model_reference/P138_net_stats_ipv6_mld_结构体.md#a4879ff9e31f8b60973d3b169598e921d)
- [net_stats_ipv6_mld::sent](../network_core_model_reference/P138_net_stats_ipv6_mld_结构体.md#ab397b74b14ce7047bf2fc63ca72ce1e5)
- [net_stats_ipv6_mld::drop](../network_core_model_reference/P138_net_stats_ipv6_mld_结构体.md#ad85dc87f57296a1e7d64e959b0370ee8)
- [net_stats_ipv6_nd::sent](../network_core_model_reference/P139_net_stats_ipv6_nd_结构体.md#a0129f7892a4439c20deb2f32b9001277)
- [net_stats_ipv6_nd::recv](../network_core_model_reference/P139_net_stats_ipv6_nd_结构体.md#a0bf6f67d9112996a3b002ea160aec769)
- [net_stats_ipv6_nd::drop](../network_core_model_reference/P139_net_stats_ipv6_nd_结构体.md#a31074d5d44138fcabdc5f7750f9f2c47)
- [net_stats_ipv6_pmtu::recv](../network_core_model_reference/P140_net_stats_ipv6_pmtu_结构体.md#a66346cd9140e30727d77648f65345762)
- [net_stats_ipv6_pmtu::drop](../network_core_model_reference/P140_net_stats_ipv6_pmtu_结构体.md#a68b19ebb61e84eb876178a31c7a4e327)
- [net_stats_ipv6_pmtu::sent](../network_core_model_reference/P140_net_stats_ipv6_pmtu_结构体.md#a698f5794b73896f7a66def2d3209fafd)
- [net_stats_pkt_filter::tx](../network_core_model_reference/P141_net_stats_pkt_filter_结构体.md#a5e88001e143c0adb129ca93b108c277d)
- [net_stats_pkt_filter::drop](../network_core_model_reference/P141_net_stats_pkt_filter_结构体.md#a62d2d86781e6224b09f21929f27b2ef7)
- [net_stats_pkt_filter::rx](../network_core_model_reference/P141_net_stats_pkt_filter_结构体.md#a8cf9912d574873832b85a614eb776789)
- [net_stats_pkts::rx](../network_core_model_reference/P142_net_stats_pkts_结构体.md#ac9784b5a245e6c57e39318aaf314f0cf)
- [net_stats_pkts::tx](../network_core_model_reference/P142_net_stats_pkts_结构体.md#aee1e302d0f8dac79b693a06d8fa3b3c5)
- [net_stats_pm::last_suspend_time](../network_core_model_reference/P143_net_stats_pm_结构体.md#a0bdf9c3676298e2df4ff3bfa03f5e823)
- [net_stats_pm::start_time](../network_core_model_reference/P143_net_stats_pm_结构体.md#a6784806eaa093431ed3c0f7acfe5a89c)
- [net_stats_pm::overall_suspend_time](../network_core_model_reference/P143_net_stats_pm_结构体.md#ab43935fcfe9efc1cd5f3e7e329996805)
- [net_stats_pm::suspend_count](../network_core_model_reference/P143_net_stats_pm_结构体.md#ac14122a4765c499c045f18c70af355a0)
- [net_stats_ppp::chkerr](../network_core_model_reference/P144_net_stats_ppp_结构体.md#a1332b31980f82236aeb0c3f9444e2ac6)
- [net_stats_ppp::pkts](../network_core_model_reference/P144_net_stats_ppp_结构体.md#a71fc81f3c5f3e65a476b3391f086d340)
- [net_stats_ppp::bytes](../network_core_model_reference/P144_net_stats_ppp_结构体.md#ab2b48da7f19d4b83e3f41b41979b7ed8)
- [net_stats_ppp::drop](../network_core_model_reference/P144_net_stats_ppp_结构体.md#ae2e0a47a539e9d7bc97f9c63f889b276)
- [net_stats_raw::recv](../network_core_model_reference/P145_net_stats_raw_结构体.md#a0decb52f848bf006f52cd575e181ffeb)
- [net_stats_raw::sent](../network_core_model_reference/P145_net_stats_raw_结构体.md#ab78de1ea1ec2ff46e6f1f248cebd5fac)
- [net_stats_raw::bytes](../network_core_model_reference/P145_net_stats_raw_结构体.md#ac83a096e59c4483528a67f7209fba257)
- [net_stats_raw::drop](../network_core_model_reference/P145_net_stats_raw_结构体.md#aea0d3bd2836853e9f8ed6af489ad42ef)
- [net_stats_rx_time::sum](../network_core_model_reference/P146_net_stats_rx_time_结构体.md#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d)
- [net_stats_rx_time::count](../network_core_model_reference/P146_net_stats_rx_time_结构体.md#a68247051b064de081fa2e84118192958)
- [net_stats_sta_mgmt::beacons_miss](../network_core_model_reference/P147_net_stats_sta_mgmt_结构体.md#a29ae0079b4c780e0de2656a85ec15fe9)
- [net_stats_sta_mgmt::beacons_rx](../network_core_model_reference/P147_net_stats_sta_mgmt_结构体.md#ac6e68fded8e19b20259442436923f815)
- [net_stats_tc::dropped](../network_core_model_reference/P148_net_stats_tc_结构体.md#a1794f71f7fe7b3d20d406be4b28eb032)
- [net_stats_tc::tx_time](../network_core_model_reference/P148_net_stats_tc_结构体.md#a30288ef3bb0796cd18c3cf0aedbe875a)
- [net_stats_tc::pkts](../network_core_model_reference/P148_net_stats_tc_结构体.md#a6614b5f5186635415a7d787260c39248)
- [net_stats_tc::bytes](../network_core_model_reference/P148_net_stats_tc_结构体.md#a74b471b77fb1c72933daa656319cc2af)
- [net_stats_tc::priority](../network_core_model_reference/P148_net_stats_tc_结构体.md#a8a5c2e59990407ddbfc7973a1c183bf6)
- [net_stats_tc::sent](../network_core_model_reference/P148_net_stats_tc_结构体.md#a8d6a3ebcc49ce8c34a5faae986f648e2)
- [net_stats_tc::rx_time](../network_core_model_reference/P148_net_stats_tc_结构体.md#a8ea00824bb0fb18e4d8912343e01c3b7)
- [net_stats_tcp::ackerr](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a0d40abc85776f0a9b9510a909b7f6d18)
- [net_stats_tcp::rsterr](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a471fcd5578f79ce77d20547b28503ac1)
- [net_stats_tcp::rexmit](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a4a4ea6e5d87ef58b4271bd708cf39635)
- [net_stats_tcp::chkerr](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a5099e174b0eafa322f0630f1f5c73a8b)
- [net_stats_tcp::seg_drop](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a5f045704859331918511e9c2281ac155)
- [net_stats_tcp::connrst](../network_core_model_reference/P149_net_stats_tcp_结构体.md#a67f55954a4c51f2b957c7d974e78c1c0)
- [net_stats_tcp::drop](../network_core_model_reference/P149_net_stats_tcp_结构体.md#aa549f7b6d5828009a09190fd64afa8e3)
- [net_stats_tcp::rst](../network_core_model_reference/P149_net_stats_tcp_结构体.md#aa618cf86b962aca0f14eb9178c8ae61a)
- [net_stats_tcp::sent](../network_core_model_reference/P149_net_stats_tcp_结构体.md#aa987bebf96000b6b4e92bfafc218759a)
- [net_stats_tcp::resent](../network_core_model_reference/P149_net_stats_tcp_结构体.md#abe567032cb4a267a984aec28c1e3cca4)
- [net_stats_tcp::conndrop](../network_core_model_reference/P149_net_stats_tcp_结构体.md#ac557ac0d8917bc2c2dfed74126f993c8)
- [net_stats_tcp::recv](../network_core_model_reference/P149_net_stats_tcp_结构体.md#ad25edb2b39a6acc8152c35ad43a5042f)
- [net_stats_tcp::bytes](../network_core_model_reference/P149_net_stats_tcp_结构体.md#af80c18bcc253133ce5f0597ac190b349)
- [net_stats_tx_time::count](../network_core_model_reference/P150_net_stats_tx_time_结构体.md#a7a652350ed04e53ba02aec294f8444b4)
- [net_stats_tx_time::sum](../network_core_model_reference/P150_net_stats_tx_time_结构体.md#af6f7a26c0344a0f93306e105a8917c3e)
- [net_stats_udp::recv](../network_core_model_reference/P151_net_stats_udp_结构体.md#a0ea91d85fe322661fb909f5e94e55a34)
- [net_stats_udp::drop](../network_core_model_reference/P151_net_stats_udp_结构体.md#a2d884bf9106e60d430ffec7c7964a609)
- [net_stats_udp::chkerr](../network_core_model_reference/P151_net_stats_udp_结构体.md#a4c57d5f68ebda7981400729b9c7fe0f7)
- [net_stats_udp::sent](../network_core_model_reference/P151_net_stats_udp_结构体.md#ab4e8228c221901d3ded55f3f823bfa1c)
- [net_stats_wifi::broadcast](../network_core_model_reference/P153_net_stats_wifi_结构体.md#a03dc04638c4b670bd7f3520d45fc1eda)
- [net_stats_wifi::multicast](../network_core_model_reference/P153_net_stats_wifi_结构体.md#a7e7f68215101885fd51c70e981da26e7)
- [net_stats_wifi::sta_mgmt](../network_core_model_reference/P153_net_stats_wifi_结构体.md#a8bee22961545674e6ab100b58a04bf91)
- [net_stats_wifi::bytes](../network_core_model_reference/P153_net_stats_wifi_结构体.md#aa055b1e8bd8f1e50815c1028b562be07)
- [net_stats_wifi::overrun_count](../network_core_model_reference/P153_net_stats_wifi_结构体.md#ac498c9e517f2cb2eb01d251e84159e7e)
- [net_stats_wifi::pkts](../network_core_model_reference/P153_net_stats_wifi_结构体.md#adbcdb2dd8733f2917c00a0b2d365393b)
- [net_stats_wifi::errors](../network_core_model_reference/P153_net_stats_wifi_结构体.md#ae0149e64a94a9f96eb6680f94793c8c4)
- [net_stats_wifi::unicast](../network_core_model_reference/P153_net_stats_wifi_结构体.md#ae80dcd73a3c5ce3ec3282d1ae827b338)
- [net_stats::processing_error](../network_core_model_reference/P125_net_stats_结构体.md#a3a4c90661d6b310b628262228a341fe2)
- [net_stats::bytes](../network_core_model_reference/P125_net_stats_结构体.md#a7a28233e6d23efdce0143469b9bb6c05)
- [net_stats::ip_errors](../network_core_model_reference/P125_net_stats_结构体.md#ac42cb13954d164e92a1ef60919a2a34e)
- [summary.h](../api_file_runtime_reference/P068_zephyr__net__prometheus__summary.h_文件参考.md)

---

[上一章](P006_modem_cellular.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_numicro_m48x_clock.h_源码浏览.md)
