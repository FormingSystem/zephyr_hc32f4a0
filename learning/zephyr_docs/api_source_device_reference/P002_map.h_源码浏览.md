---
id: learning.zephyr-docs.api-source-device-reference.page-2
title: map.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_map.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h.html)。

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
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="foldopen00098"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00151"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="foldopen00168"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="foldopen00182"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="foldopen00275"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="foldopen00294"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="foldopen00307"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="foldopen00320"></a>
<a id="l00320"></a>
<a id="l00322"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="foldopen00331"></a>
<a id="l00331"></a>
<a id="l00333"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="foldopen00342"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="foldopen00353"></a>
<a id="l00353"></a>
<a id="l00355"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="foldopen00364"></a>
<a id="l00364"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="foldopen00375"></a>
<a id="l00375"></a>
<a id="l00377"></a>
<a id="l00379"></a>
<a id="l00381"></a>
<a id="l00383"></a>
<a id="l00385"></a>
<a id="l00387"></a>
<a id="l00389"></a>
<a id="l00391"></a>
<a id="l00393"></a>
<a id="l00395"></a>
<a id="l00397"></a>
<a id="l00399"></a>
<a id="l00401"></a>
<a id="l00403"></a>
<a id="l00405"></a>
<a id="l00407"></a>
<a id="l00409"></a>
<a id="l00411"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="foldopen00424"></a>
<a id="l00424"></a>
<a id="l00426"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="foldopen00435"></a>
<a id="l00435"></a>
<a id="l00437"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="foldopen00446"></a>
<a id="l00446"></a>
<a id="l00448"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="foldopen00457"></a>
<a id="l00457"></a>
<a id="l00459"></a>
<a id="l00461"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="foldopen00470"></a>
<a id="l00470"></a>
<a id="l00472"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="foldopen00481"></a>
<a id="l00481"></a>
<a id="l00483"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00489"></a>
<a id="l00491"></a>
<a id="l00493"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="foldopen00502"></a>
<a id="l00502"></a>
<a id="l00504"></a>
<a id="l00506"></a>
<a id="l00508"></a>
<a id="l00510"></a>
<a id="l00512"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="foldopen00521"></a>
<a id="l00521"></a>
<a id="l00523"></a>
<a id="l00525"></a>
<a id="l00527"></a>
<a id="l00529"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="l00535"></a>
<a id="l00537"></a>
<a id="l00539"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00545"></a>
<a id="l00547"></a>
<a id="l00549"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="foldopen00558"></a>
<a id="l00558"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00564"></a>
<a id="l00566"></a>
<a id="l00568"></a>
<a id="l00570"></a>
<a id="l00572"></a>
<a id="l00574"></a>
<a id="l00576"></a>
<a id="l00578"></a>
<a id="l00580"></a>
<a id="l00582"></a>
<a id="l00584"></a>
<a id="l00586"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="foldopen00595"></a>
<a id="l00595"></a>
<a id="l00597"></a>
<a id="l00599"></a>
<a id="l00601"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="foldopen00610"></a>
<a id="l00610"></a>
<a id="l00612"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00623"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="foldopen00631"></a>
<a id="l00631"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="foldopen00862"></a>
<a id="l00862"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00870"></a>
<a id="l00871"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00888"></a>
<a id="l00889"></a>
<a id="l00890"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00933"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00958"></a>
<a id="l00973"></a>
<a id="l00974"></a>
<a id="l00988"></a>
<a id="l00989"></a>
<a id="l01003"></a>
<a id="l01004"></a>
<a id="l01019"></a>
<a id="l01020"></a>
<a id="l01035"></a>
<a id="l01036"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01084"></a>
<a id="l01085"></a>
<a id="l01100"></a>
<a id="l01101"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01133"></a>
<a id="l01134"></a>
<a id="l01150"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="l01167"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01184"></a>
<a id="l01185"></a>
<a id="l01186"></a>
<a id="l01201"></a>
<a id="l01202"></a>
<a id="l01203"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01221"></a>
<a id="l01228"></a>
<a id="l01230"></a>
<a id="l01231"></a>
<a id="foldopen01236"></a>
<a id="l01236"></a>
<a id="l01238"></a>
<a id="l01249"></a>
<a id="l01250"></a>
<a id="l01251"></a>
<a id="l01252"></a>
<a id="foldopen01257"></a>
<a id="l01257"></a>
<a id="l01259"></a>
<a id="l01270"></a>
<a id="l01271"></a>
<a id="l01272"></a>
<a id="l01273"></a>
<a id="foldopen01278"></a>
<a id="l01278"></a>
<a id="l01287"></a>
<a id="l01288"></a>
<a id="l01295"></a>
<a id="l01296"></a>
<a id="l01305"></a>
<a id="l01306"></a>
<a id="l01313"></a>
<a id="l01314"></a>
<a id="l01325"></a>
<a id="l01326"></a>
<a id="l01327"></a>
<a id="l01336"></a>
<a id="l01337"></a>
<a id="l01346"></a>
<a id="l01347"></a>
<a id="l01358"></a>
<a id="l01359"></a>
<a id="l01360"></a>
<a id="foldopen01366"></a>
<a id="l01366"></a>
<a id="l01368"></a>
<a id="l01369"></a>
<a id="l01371"></a>
<a id="l01372"></a>
<a id="l01374"></a>
<a id="l01375"></a>
<a id="l01377"></a>
<a id="l01378"></a>
<a id="l01380"></a>
<a id="l01381"></a>
<a id="l01383"></a>
<a id="l01384"></a>
<a id="l01386"></a>
<a id="l01387"></a>
<a id="l01389"></a>
<a id="l01390"></a>
<a id="l01392"></a>
<a id="l01393"></a>
<a id="l01395"></a>
<a id="l01396"></a>
<a id="l01397"></a>
<a id="l01408"></a>
<a id="l01409"></a>
<a id="l01419"></a>
<a id="l01420"></a>
<a id="l01431"></a>
<a id="l01432"></a>
<a id="l01442"></a>
<a id="l01443"></a>
<a id="l01454"></a>
<a id="l01455"></a>
<a id="l01466"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01482"></a>
<a id="l01483"></a>
<a id="l01497"></a>
<a id="l01498"></a>
<a id="l01499"></a>
<a id="l01513"></a>
<a id="l01514"></a>
<a id="l01529"></a>
<a id="l01530"></a>
<a id="l01531"></a>
<a id="l01533"></a>
<a id="l01540"></a>
<a id="l01542"></a>
<a id="l01543"></a>
<a id="foldopen01548"></a>
<a id="l01548"></a>
<a id="l01550"></a>
<a id="l01551"></a>
<a id="l01562"></a>
<a id="l01563"></a>
<a id="l01564"></a>
<a id="l01565"></a>
<a id="foldopen01570"></a>
<a id="l01570"></a>
<a id="l01572"></a>
<a id="l01573"></a>
<a id="l01584"></a>
<a id="l01585"></a>
<a id="l01586"></a>
<a id="l01587"></a>
<a id="foldopen01592"></a>
<a id="l01592"></a>
<a id="l01601"></a>
<a id="l01602"></a>
<a id="l01609"></a>
<a id="l01610"></a>
<a id="l01619"></a>
<a id="l01620"></a>
<a id="l01627"></a>
<a id="l01628"></a>
<a id="l01639"></a>
<a id="l01640"></a>
<a id="l01641"></a>
<a id="l01650"></a>
<a id="l01651"></a>
<a id="l01660"></a>
<a id="l01661"></a>
<a id="l01672"></a>
<a id="l01673"></a>
<a id="l01683"></a>
<a id="l01684"></a>
<a id="l01695"></a>
<a id="l01696"></a>
<a id="l01707"></a>
<a id="l01708"></a>
<a id="l01719"></a>
<a id="l01720"></a>
<a id="l01731"></a>
<a id="l01732"></a>
<a id="l01743"></a>
<a id="l01744"></a>
<a id="l01755"></a>
<a id="l01756"></a>
<a id="l01767"></a>
<a id="l01768"></a>
<a id="l01779"></a>
<a id="l01780"></a>
<a id="l01791"></a>
<a id="l01792"></a>
<a id="l01803"></a>
<a id="l01804"></a>
<a id="l01815"></a>
<a id="l01816"></a>
<a id="l01817"></a>
<a id="foldopen01823"></a>
<a id="l01823"></a>
<a id="l01825"></a>
<a id="l01826"></a>
<a id="l01828"></a>
<a id="l01829"></a>
<a id="l01831"></a>
<a id="l01832"></a>
<a id="l01834"></a>
<a id="l01835"></a>
<a id="l01837"></a>
<a id="l01838"></a>
<a id="l01840"></a>
<a id="l01841"></a>
<a id="l01843"></a>
<a id="l01844"></a>
<a id="l01846"></a>
<a id="l01847"></a>
<a id="l01849"></a>
<a id="l01850"></a>
<a id="l01852"></a>
<a id="l01853"></a>
<a id="l01854"></a>
<a id="l01865"></a>
<a id="l01866"></a>
<a id="l01876"></a>
<a id="l01877"></a>
<a id="l01888"></a>
<a id="l01889"></a>
<a id="l01899"></a>
<a id="l01900"></a>
<a id="l01911"></a>
<a id="l01912"></a>
<a id="l01923"></a>
<a id="l01924"></a>
<a id="l01925"></a>
<a id="l01939"></a>
<a id="l01940"></a>
<a id="l01953"></a>
<a id="l01954"></a>
<a id="l01955"></a>
<a id="l01969"></a>
<a id="l01970"></a>
<a id="l01984"></a>
<a id="l01985"></a>
<a id="l01986"></a>
<a id="l02000"></a>
<a id="l02001"></a>
<a id="l02002"></a>
<a id="l02017"></a>
<a id="l02018"></a>
<a id="l02019"></a>
<a id="l02034"></a>
<a id="l02035"></a>
<a id="l02036"></a>
<a id="l02051"></a>
<a id="l02052"></a>
<a id="l02066"></a>
<a id="l02067"></a>
<a id="l02068"></a>
<a id="l02083"></a>
<a id="l02084"></a>
<a id="l02098"></a>
<a id="l02099"></a>
<a id="l02100"></a>
<a id="l02115"></a>
<a id="l02116"></a>
<a id="l02117"></a>
<a id="l02131"></a>
<a id="l02132"></a>
<a id="l02133"></a>
<a id="l02148"></a>
<a id="l02149"></a>
<a id="l02150"></a>
<a id="l02165"></a>
<a id="l02166"></a>
<a id="l02167"></a>
<a id="l02181"></a>
<a id="l02182"></a>
<a id="l02183"></a>
<a id="l02185"></a>
<a id="l02192"></a>
<a id="l02194"></a>
<a id="l02195"></a>
<a id="foldopen02200"></a>
<a id="l02200"></a>
<a id="l02209"></a>
<a id="l02210"></a>
<a id="l02218"></a>
<a id="l02219"></a>
<a id="l02228"></a>
<a id="l02229"></a>
<a id="l02237"></a>
<a id="l02238"></a>
<a id="l02250"></a>
<a id="l02251"></a>
<a id="l02252"></a>
<a id="l02261"></a>
<a id="l02262"></a>
<a id="l02272"></a>
<a id="l02273"></a>
<a id="l02284"></a>
<a id="l02285"></a>
<a id="l02286"></a>
<a id="foldopen02292"></a>
<a id="l02292"></a>
<a id="l02294"></a>
<a id="l02295"></a>
<a id="l02297"></a>
<a id="l02298"></a>
<a id="l02300"></a>
<a id="l02301"></a>
<a id="l02303"></a>
<a id="l02304"></a>
<a id="l02306"></a>
<a id="l02307"></a>
<a id="l02309"></a>
<a id="l02310"></a>
<a id="l02312"></a>
<a id="l02313"></a>
<a id="l02315"></a>
<a id="l02316"></a>
<a id="l02318"></a>
<a id="l02319"></a>
<a id="l02320"></a>
<a id="l02334"></a>
<a id="l02335"></a>
<a id="l02336"></a>
<a id="l02347"></a>
<a id="l02348"></a>
<a id="l02361"></a>
<a id="l02362"></a>
<a id="l02363"></a>
<a id="l02374"></a>
<a id="l02375"></a>
<a id="l02386"></a>
<a id="l02387"></a>
<a id="l02388"></a>
<a id="l02403"></a>
<a id="l02404"></a>
<a id="l02418"></a>
<a id="l02419"></a>
<a id="l02433"></a>
<a id="l02434"></a>
<a id="l02451"></a>
<a id="l02452"></a>
<a id="l02454"></a>
<a id="l02455"></a>
<a id="l02456"></a>
<a id="l02457"></a>
<a id="l02458"></a>
<a id="l02462"></a>
<a id="l02463"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="abluetooth_2uuid_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agoep_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__bt__map__mce__mas_html_ga01d1677204f204feb2474a61bfcc118a"></a>
<a id="agroup__bt__map__mce__mas_html_ga04bf8d4d99165e7cf49613fe82432ca7"></a>
<a id="agroup__bt__map__mce__mas_html_ga0c58e5c7f70c15409ae9241d0b412400"></a>
<a id="agroup__bt__map__mce__mas_html_ga1a00c2b646b9a10c3deb6f4953f04683"></a>
<a id="agroup__bt__map__mce__mas_html_ga2206f238364c04e180153c5cff10de94"></a>
<a id="agroup__bt__map__mce__mas_html_ga28b33d6c38af9479e56e9c2c2c0f795a"></a>
<a id="agroup__bt__map__mce__mas_html_ga3202aee97828ecd8ed6f39f9eb6c98f2"></a>
<a id="agroup__bt__map__mce__mas_html_ga39795b7002cf40984b130d38179a5472"></a>
<a id="agroup__bt__map__mce__mas_html_ga3b1dc36240679618c98df515a351a5e7"></a>
<a id="agroup__bt__map__mce__mas_html_ga539c08b47cc73a23d24bd54dcb5d6dc4"></a>
<a id="agroup__bt__map__mce__mas_html_ga54a2552080933e12b6b871bc9f898fce"></a>
<a id="agroup__bt__map__mce__mas_html_ga54fa7e185e5d949bec434935f51ae9fb"></a>
<a id="agroup__bt__map__mce__mas_html_ga666d58fd65852372fa22328b6cd9aa82"></a>
<a id="agroup__bt__map__mce__mas_html_ga9e6640177b225a5b7448cde8a17de4f0"></a>
<a id="agroup__bt__map__mce__mas_html_gaa03c3ea1d6ec10d02412b4525dd3ffe5"></a>
<a id="agroup__bt__map__mce__mas_html_gabbe39f067872a6c008269d483a97d234"></a>
<a id="agroup__bt__map__mce__mas_html_gabdd72751375fa9a0aa1f99e75137cb9e"></a>
<a id="agroup__bt__map__mce__mas_html_gad528c35977847525d781a39c50a3e793"></a>
<a id="agroup__bt__map__mce__mas_html_gae91fb531b7164b389994b9391fa8e51e"></a>
<a id="agroup__bt__map__mce__mas_html_gaf146e16f1b7950db4b5418bd27269ebb"></a>
<a id="agroup__bt__map__mce__mas_html_gaf9836663a18ecc62b5330a1682f4b42e"></a>
<a id="agroup__bt__map__mce__mns_html_ga029cb5034f7cbf059653c763e4c767c2"></a>
<a id="agroup__bt__map__mce__mns_html_ga14411f8c0e8ce90824d366d28d4a2d2e"></a>
<a id="agroup__bt__map__mce__mns_html_ga3e181d1bd37877dd8abf47a541c4b98e"></a>
<a id="agroup__bt__map__mce__mns_html_ga574790bc59c82d89010e61f535849a35"></a>
<a id="agroup__bt__map__mce__mns_html_ga7309e25833e6594dc0018afe8b0a403c"></a>
<a id="agroup__bt__map__mce__mns_html_ga904970bac58822ec5336ce2bab226300"></a>
<a id="agroup__bt__map__mce__mns_html_gaab9161c0524c74cb4b03938c26642f4a"></a>
<a id="agroup__bt__map__mce__mns_html_gabae24c99ada5dae44ca657ae96008a69"></a>
<a id="agroup__bt__map__mce__mns_html_gac6fa0bcfbea7b9a2a258678f5a2b8503"></a>
<a id="agroup__bt__map__mce__mns_html_gad4207d61fbe40c34e753132fc742aba3"></a>
<a id="agroup__bt__map__mse__mas_html_ga031515fbb0ca110532f5a1e971a01739"></a>
<a id="agroup__bt__map__mse__mas_html_ga14815828dbf7163ab8fb0b3a8c0165b4"></a>
<a id="agroup__bt__map__mse__mas_html_ga275eff320f980230d8d80873ad0ef3ce"></a>
<a id="agroup__bt__map__mse__mas_html_ga2833ef99d384109acf304532d1820a36"></a>
<a id="agroup__bt__map__mse__mas_html_ga2c0ed0fdc8fee3f98e671c5ec187c8ed"></a>
<a id="agroup__bt__map__mse__mas_html_ga37c155889cd0e2bb902da2bd25415509"></a>
<a id="agroup__bt__map__mse__mas_html_ga3aacf3e78b40f06bbf17baada2c59e04"></a>
<a id="agroup__bt__map__mse__mas_html_ga3cfbf0a8f1f1b6a730c401dac21e9f51"></a>
<a id="agroup__bt__map__mse__mas_html_ga3eee467070483854e1a84a940ee031e2"></a>
<a id="agroup__bt__map__mse__mas_html_ga55641e8681932d0e31021d3803625874"></a>
<a id="agroup__bt__map__mse__mas_html_ga670bebf0edd1e8d5f7a2de5403e042d0"></a>
<a id="agroup__bt__map__mse__mas_html_ga6df473fe69d8b3d183ee8385613f786f"></a>
<a id="agroup__bt__map__mse__mas_html_ga7db0773e3e0425f77e965fece30c3697"></a>
<a id="agroup__bt__map__mse__mas_html_ga8263ea5145edcfd277f73980a3fcea57"></a>
<a id="agroup__bt__map__mse__mas_html_ga852ae34e4f8b44fea3308a42baa15ec2"></a>
<a id="agroup__bt__map__mse__mas_html_gab1c7678b39dad5309efde0b5950a997f"></a>
<a id="agroup__bt__map__mse__mas_html_gab50e3d126e2d35e9b6724cf3112d0892"></a>
<a id="agroup__bt__map__mse__mas_html_gabc3a8d9eb9dbc3fd028d39e4a262388b"></a>
<a id="agroup__bt__map__mse__mas_html_gabcd127dc45e03820079be0dc92066b89"></a>
<a id="agroup__bt__map__mse__mas_html_gac972589b96cd3931044f994d4c94cf20"></a>
<a id="agroup__bt__map__mse__mas_html_gadd1da4acdd8043aa542c0fe36259898f"></a>
<a id="agroup__bt__map__mse__mas_html_gadeb8072cdca241b3ad15c2116733d155"></a>
<a id="agroup__bt__map__mse__mns_html_ga0513491439278cadc6897f9cb932cd67"></a>
<a id="agroup__bt__map__mse__mns_html_ga08513e5aa2b54e4474ee647232c0af91"></a>
<a id="agroup__bt__map__mse__mns_html_ga305dd055de4831ef68cff7b5346a4b5d"></a>
<a id="agroup__bt__map__mse__mns_html_ga46fc48dafd5c173199274be1a616a109"></a>
<a id="agroup__bt__map__mse__mns_html_ga7bedc538a126b8c4d4c6fb393fc06218"></a>
<a id="agroup__bt__map__mse__mns_html_gaa0298eb521d012a910eba4a552d55fa7"></a>
<a id="agroup__bt__map__mse__mns_html_gac8776edbbf4e2f891246cba86a1df589"></a>
<a id="agroup__bt__map__mse__mns_html_gadf2f434d2565703781a46851d4444a80"></a>
<a id="agroup__bt__map__mse__mns_html_gafc1be36425faa6242ed8eb4f21d76b5f"></a>
<a id="agroup__bt__map_html_ga0fa30e8b33826204f0625a2223cfaf1c"></a>
<a id="agroup__bt__map_html_ga215e8bd71131e739b19f5f5ee57904e6"></a>
<a id="agroup__bt__map_html_ga2fdf1a6a310fec131555fbdc62c524a2"></a>
<a id="agroup__bt__map_html_ga34cee2f295fee5b00bced31753f03b25"></a>
<a id="agroup__bt__map_html_ga3d3327344323fae6f7a2b1ebca459db0"></a>
<a id="agroup__bt__map_html_ga430b14f450167b13329f54377473b699"></a>
<a id="agroup__bt__map_html_ga4a9fc0bfa14b5e91491aec130e396429"></a>
<a id="agroup__bt__map_html_ga4f1f483d5edfaa151a11086caac24e5c"></a>
<a id="agroup__bt__map_html_ga5678131af7da533ff8b751555542933e"></a>
<a id="agroup__bt__map_html_ga5acd8d8cfc6358140438860067970e2b"></a>
<a id="agroup__bt__map_html_ga5bb2e0b7951bde5042fbb9c4e0c7cc26"></a>
<a id="agroup__bt__map_html_ga5f8e52ddea4d8e70373306c11e0bc7cf"></a>
<a id="agroup__bt__map_html_ga6d4c3231e2e64190c6ccc30b4d5f822c"></a>
<a id="agroup__bt__map_html_ga7310a116a939b40d7ee346371b5ccd88"></a>
<a id="agroup__bt__map_html_ga7af9d1e4244a00f8d2ae607f590fea94"></a>
<a id="agroup__bt__map_html_ga7c4ba8b9727c454a54a2178d584dfcb7"></a>
<a id="agroup__bt__map_html_ga8b805587e1abb311367e59d80d223516"></a>
<a id="agroup__bt__map_html_ga8dcd4f8704a2b1cab77b2279d7f2024f"></a>
<a id="agroup__bt__map_html_ga9523beb219a00ac4e6dba3e021b491d4"></a>
<a id="agroup__bt__map_html_gabd4c099cc62671f53edec84eb04c50ff"></a>
<a id="agroup__bt__map_html_gabf5f60778a9adf113e86e559095dd66f"></a>
<a id="agroup__bt__map_html_gace38e2a78aaba1e2c48572e0d247e68c"></a>
<a id="agroup__bt__map_html_gadec3f7d6faccc656739a7b7a88c10387"></a>
<a id="agroup__bt__map_html_gaef50be9a23daf42f669fde9e067b18f3"></a>
<a id="agroup__bt__map_html_gga0fa30e8b33826204f0625a2223cfaf1ca104a2dd364f1e86b9b5f4cd8fea38011"></a>
<a id="agroup__bt__map_html_gga0fa30e8b33826204f0625a2223cfaf1ca45f4dd02d1e4c1ce1ceef8be95684a51"></a>
<a id="agroup__bt__map_html_gga215e8bd71131e739b19f5f5ee57904e6a5f1552a26d09f1c696f828967222707f"></a>
<a id="agroup__bt__map_html_gga215e8bd71131e739b19f5f5ee57904e6addfabaeaa7d8903c81b41c9844514849"></a>
<a id="agroup__bt__map_html_gga2fdf1a6a310fec131555fbdc62c524a2a0aecdd208590887c87b783b9b42730e7"></a>
<a id="agroup__bt__map_html_gga2fdf1a6a310fec131555fbdc62c524a2a1e746d528718d93d50dba7770e6d128c"></a>
<a id="agroup__bt__map_html_gga2fdf1a6a310fec131555fbdc62c524a2a5ad011cef696acfa77ff9d36c80c727a"></a>
<a id="agroup__bt__map_html_gga2fdf1a6a310fec131555fbdc62c524a2abced9c6dcd9d3e6b11c2c73e7480a202"></a>
<a id="agroup__bt__map_html_gga34cee2f295fee5b00bced31753f03b25a089baca6845a803dda4b7e506e452b5b"></a>
<a id="agroup__bt__map_html_gga34cee2f295fee5b00bced31753f03b25a74198afdf437d36971d5cf4fdcaab5b8"></a>
<a id="agroup__bt__map_html_gga3d3327344323fae6f7a2b1ebca459db0ab4134b8e2c9987789fa541627d9ab19f"></a>
<a id="agroup__bt__map_html_gga3d3327344323fae6f7a2b1ebca459db0aebc96aeb807ea78da5d8714b1213e6f7"></a>
<a id="agroup__bt__map_html_gga430b14f450167b13329f54377473b699a1a041e3eed1744fe8d02908be402b0a4"></a>
<a id="agroup__bt__map_html_gga430b14f450167b13329f54377473b699a22d8803a6310974137af6d8bc0c9e6a8"></a>
<a id="agroup__bt__map_html_gga4a9fc0bfa14b5e91491aec130e396429a0215a73c93fe79bbd9fc28b34af31057"></a>
<a id="agroup__bt__map_html_gga4a9fc0bfa14b5e91491aec130e396429a4955b62b432b783eb774d704e2f2b4e2"></a>
<a id="agroup__bt__map_html_gga4f1f483d5edfaa151a11086caac24e5ca0f8654affc09e99bad440d2b9faeb163"></a>
<a id="agroup__bt__map_html_gga4f1f483d5edfaa151a11086caac24e5ca12b73e28e320ba1bf3aa8edf44b053cd"></a>
<a id="agroup__bt__map_html_gga4f1f483d5edfaa151a11086caac24e5ca66220e415b9164fe41a19e423b4aad90"></a>
<a id="agroup__bt__map_html_gga5678131af7da533ff8b751555542933ea8b13f5d7fc245c7b66a65e0845ed7edc"></a>
<a id="agroup__bt__map_html_gga5678131af7da533ff8b751555542933eaa5d3b0ad2bf7f8600ad059132aaed665"></a>
<a id="agroup__bt__map_html_gga5678131af7da533ff8b751555542933ead7b0402847a837a69055dcf4b6fad674"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2ba169927e375629a179d5326d9db81c6f1"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2ba3802bd6debad36401e16092e5837f382"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2ba47d696ec191c6a0463ce70d5742616ad"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2ba5e21b8db192673e5b6e3146ed5b04dba"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2ba77669e589a872268da67098ef008f3eb"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2ba83158a4308e7e89422541f2120e9baeb"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2ba8394516a5a3f2cc43b5facc1a39d29d4"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2ba88aa3bd1aeac147410ae96e8c7de43f9"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2ba9775c436fbf2f2211daea1b08f2a03e1"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2baa869867c70b17e91f726f27c6cbcacda"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2baa8e1626a89d2824b2fa3d6723a3a45cd"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2bab1a7d0518b5555eb63fb7ecee7e43bc9"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2bad0ef68fc6a11e2429f67e1d6564597ef"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2bae685c7a86ab34c48a1e36ef7c5a3c9de"></a>
<a id="agroup__bt__map_html_gga5acd8d8cfc6358140438860067970e2baf34804c0b883c1a172c92ba237e05817"></a>
<a id="agroup__bt__map_html_gga5bb2e0b7951bde5042fbb9c4e0c7cc26a038430c6eea453638a2fc3351315b638"></a>
<a id="agroup__bt__map_html_gga5bb2e0b7951bde5042fbb9c4e0c7cc26a0f4bd271fb4a331e66dafde2a04fd62a"></a>
<a id="agroup__bt__map_html_gga5bb2e0b7951bde5042fbb9c4e0c7cc26a803694148d134338a83f365390929505"></a>
<a id="agroup__bt__map_html_gga5bb2e0b7951bde5042fbb9c4e0c7cc26a9f65cf3b8d5a5855219599ed656ea56c"></a>
<a id="agroup__bt__map_html_gga5bb2e0b7951bde5042fbb9c4e0c7cc26ae0396ce6457b9792d564195f906fafe3"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfa219e72e5bda08cfc385be812c758e643"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfa2719dcdd029ab08b613199779d03ffb4"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfa3c2987c761d5b59e8dc2e32f86f2385b"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfa46cefe87f4e615449d6c455f7fb46ff6"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfa4a6ee544171c8b462b67e06ac83f1f82"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfa59c95bdc52ee0322073f77dd0e105793"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfa5d27a1c447d9f5a1b6c52b86915355c8"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfa5dc039eda9209a6d0e2fde493be3e539"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfa86c6406f1611ab59bec605c453e4de83"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfa8bdec6724248fb7c9c03dfc68a74685d"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfa99d249a960b62ff69f4f2a1a13709d3a"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfaa09c318962d5b45ec38803e76bdde12f"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfadb591e1a00ec2aa5769da57ad9fee449"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfaf249580f9df1595dfafe8ac26544c1cf"></a>
<a id="agroup__bt__map_html_gga5f8e52ddea4d8e70373306c11e0bc7cfafa05e0c6bd1e94c084c38576351e7aa1"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca1bc10abe061f68c3de72c37b5307c484"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca2843780dad72eaa1d84cec56077cff93"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca2c7cbab7fe254b975668563039c7ace8"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca2cbc347cb637a951868052e58eb3dab9"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca32cf970e22e8f082293225b5a614de8d"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca3353469789a5a72f4fc97dabed1d4dcf"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca35f15fe0fba34519ff0d1087c2e32c4c"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca572d7eb54deb371cee55c0149f21d6db"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca5e63f64fb534af8295995a0fbec364df"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca679c98163ee9b3114c7adf64b6976a9e"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca6aa30c2d7dccbe630756c1f1e4f7a141"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca71243a44c4d5a105c02b49318302fb7a"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca7467b703f0cf9d760d6d18e0dd6dfa7f"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca8d214b20b66be2264fb8da2d9feb93d0"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822ca9aaa859278454e081c5fe5e83dfded5d"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822caa6de591a1e2d5936263741f273c9fb8a"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822caa76c12d6babf2df623f28f58ed1912d0"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822caa7e8028e50f7903aefd379d76695408f"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822cac4a88df48198a497da4a94ec124bb735"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822caccc791a50cc33ef4d62d6b126c1ba898"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822cae28c62057713e3a7318cf85eaa7c337e"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822cae5fa5f417d064a1b85e9db70a5ce94e5"></a>
<a id="agroup__bt__map_html_gga6d4c3231e2e64190c6ccc30b4d5f822caec96609ac47f6cf1e779d049687f2e63"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a06ae16f7d6a3a247e5e1771254df0ea9"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a0bb8acb58e8983793bb787ae8e6d4033"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a15c0a2959d67e24ed18203cd8c9fe46a"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a161b7d1952483a47eee81dfd98ce831c"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a170d3717ab48a7f6a63e8bd66d1cb228"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a19b5e72c512c29b5cfbe58dbdaf63064"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a1aca8ccd385944cb73f03568123dc1e3"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a2071ba2e3ec0dc8b5adc8b97a37a010d"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a208c8d9ea3195b7d70ab2e7ccae6671d"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a2df85ffb7e034732fb608c6935af9297"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a4871d9d7da47983cd5fd7a7718ab2478"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a4ee0642cd16aa8e1ce5224118968f9ee"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a5622480195120444b2f200e79db09499"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a563fbb6001387da1389713be552fec13"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a595f6e5f7eac3c57dccf13e1e45dfd6b"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a5ec11c380b39a38cade5acd06545b1a1"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a600395d6f4620dffee2447ae8b9a4fbe"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a637ac76aafe5a586819b9897acc7d1da"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a6b4d28c95336af96c06a71f6cb40060b"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a6f5914896a591c0008fb744506ec98d4"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a706346ca21cb1f76c22dc02af1076b04"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a72083eddb755825e5899dfddbcc10085"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a7227e024472a421c86c3cb7a0db65e55"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a7627a7496631fbe6326e4c1c43e4877c"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a7636683c2efff7c4c8d59a141c6e12b6"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a79da1ebc8b5e7e0d1098d4b022fa8da7"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a7f9d301f9383d8179611344d18f03094"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a81297adf58afc780a00afe8ef4a70c95"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a8651767d6b1c5dc6f0affac25014aeaa"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a8f4a492c9619ec1b78124f0509b93857"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88a9f08b382471f807452d9cf7e1bff1b3b"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88aa1b59e01c63abc3ccc7ee54ca27e9296"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88aa9241c4f620f61717160d5dbc9dc5389"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88ac6118aa692c3c382ce7630ac2d499aac"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88acfef6214cbd687aa5ad7ee4d8d3a4a2d"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88ad1d1edb33a8147e1d96400607e8f3f1e"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88ad3058d06b585289586c5cccaab548bc2"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88ad49f0edd1a6e1c1da5a37abd552cc6b1"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88ad53697174462dfe4d2d592bf71bf180c"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88adaad04f88448466dd606527157d74cc7"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88adb08ba0bbc13653357e835dcd6fa5770"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88aee3ebbef8eb74deefedb414daea2dc1e"></a>
<a id="agroup__bt__map_html_gga7310a116a939b40d7ee346371b5ccd88af39bad93c459fcb86b9583a1519c070b"></a>
<a id="agroup__bt__map_html_gga7af9d1e4244a00f8d2ae607f590fea94a28da6d9711231be9117aec9feb9104f4"></a>
<a id="agroup__bt__map_html_gga7af9d1e4244a00f8d2ae607f590fea94af5d7d30b5e5d6f0e8a4dd5ae42104bf8"></a>
<a id="agroup__bt__map_html_gga7c4ba8b9727c454a54a2178d584dfcb7a1b10e235398a004168731de140b7e6d8"></a>
<a id="agroup__bt__map_html_gga7c4ba8b9727c454a54a2178d584dfcb7a2ab7b8a63e2dae0bf8d82e5c7aae3038"></a>
<a id="agroup__bt__map_html_gga7c4ba8b9727c454a54a2178d584dfcb7a37bca39682be9efa27f906754d972b7d"></a>
<a id="agroup__bt__map_html_gga7c4ba8b9727c454a54a2178d584dfcb7a9df74f88cb18833440816218a610527c"></a>
<a id="agroup__bt__map_html_gga7c4ba8b9727c454a54a2178d584dfcb7ab80d08d33c7fc5adc1483b1be64390c0"></a>
<a id="agroup__bt__map_html_gga7c4ba8b9727c454a54a2178d584dfcb7adfc6a259bbc5d1b6a0b30d57d1a5b7a9"></a>
<a id="agroup__bt__map_html_gga8b805587e1abb311367e59d80d223516a25fc04d24537a005dc4674d29ad48357"></a>
<a id="agroup__bt__map_html_gga8b805587e1abb311367e59d80d223516a8c7e4fd24ff699c52a7ecba484923cfb"></a>
<a id="agroup__bt__map_html_gga8dcd4f8704a2b1cab77b2279d7f2024fa735aac580ed7fae38d10bcc41f2b393a"></a>
<a id="agroup__bt__map_html_gga8dcd4f8704a2b1cab77b2279d7f2024fabe2ef316affe063b7634ca5e5f2e0351"></a>
<a id="agroup__bt__map_html_gga9523beb219a00ac4e6dba3e021b491d4a3c1a5486acfe0d06fa935f34c5bf0d1c"></a>
<a id="agroup__bt__map_html_gga9523beb219a00ac4e6dba3e021b491d4a4affc47380cbcbbfcb819092d9c5cfd5"></a>
<a id="agroup__bt__map_html_gga9523beb219a00ac4e6dba3e021b491d4a4d4a9258001731ffb4ea74d807394050"></a>
<a id="agroup__bt__map_html_gga9523beb219a00ac4e6dba3e021b491d4a98e509fe029643bb5f281b9274c70583"></a>
<a id="agroup__bt__map_html_gga9523beb219a00ac4e6dba3e021b491d4a9a458e69d88a1f2c3be14c4c69c99b39"></a>
<a id="agroup__bt__map_html_gga9523beb219a00ac4e6dba3e021b491d4ade1acc46b57740b9c113cdf4ea8a502f"></a>
<a id="agroup__bt__map_html_gga9523beb219a00ac4e6dba3e021b491d4afc2b4a0338e768d25f200efe3c14081a"></a>
<a id="agroup__bt__map_html_ggabd4c099cc62671f53edec84eb04c50ffa64afbc9334b9ee926b11dd473d70e0aa"></a>
<a id="agroup__bt__map_html_ggabd4c099cc62671f53edec84eb04c50ffad1adaa8853f8bca4f4d21b378caeaf19"></a>
<a id="agroup__bt__map_html_ggabd4c099cc62671f53edec84eb04c50ffaf9dd6096a95f6f75140d2d37d12e24b3"></a>
<a id="agroup__bt__map_html_ggabf5f60778a9adf113e86e559095dd66fa0c7b3c3b9c8f0d9c514a9730d57d7738"></a>
<a id="agroup__bt__map_html_ggabf5f60778a9adf113e86e559095dd66fae90806b4b223afc531d74dd1819ff7b3"></a>
<a id="agroup__bt__map_html_ggabf5f60778a9adf113e86e559095dd66faf9e8514d6411d25bc71a33e7f351f93f"></a>
<a id="agroup__bt__map_html_ggace38e2a78aaba1e2c48572e0d247e68ca179f10a2a6dd6184f4604794f2bb170f"></a>
<a id="agroup__bt__map_html_ggace38e2a78aaba1e2c48572e0d247e68ca1bb84095702eb5c6263a6ee908a6d1c6"></a>
<a id="agroup__bt__map_html_ggace38e2a78aaba1e2c48572e0d247e68ca496b9d0393213a460a0b0bd2c8e4ba33"></a>
<a id="agroup__bt__map_html_ggace38e2a78aaba1e2c48572e0d247e68ca95cb2a4eb0e6d8d2f2dd9f03a3c7c720"></a>
<a id="agroup__bt__map_html_ggace38e2a78aaba1e2c48572e0d247e68cacfffcf3cef8adddd1e1768fda9cdcf6d"></a>
<a id="agroup__bt__map_html_ggace38e2a78aaba1e2c48572e0d247e68cad9c127c32a580302536aa13cddd52085"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a001c4dc6084e12938867c4a1eb7316ea"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a07145a14474b470e1dc9143d115add4f"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a0c4cac1477808905597af3d1373663d4"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a1b55581c15bf6d915a748fff1655f2eb"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a1c86d02bc4003273da0e84ebaeaa4ae8"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a1cad006d6e9d8740e929a801a3a3593f"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a21a483901085035c22fc3baf02931df6"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a295391beee4e7f92c9e5745785da214d"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a302b63d08cb7ff36204c2f390b746375"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a47987b441c785b7657f9323ec7858d51"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a5b0a0672211d6e9a0e377baaa16f449a"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a898d380bc11251e69d4525c2e3f5fcbe"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a8c7c06f8ebdd5e433e926345d62c092b"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387a90f5931d1fe65f3f2b0718c357e45740"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387aac5a5819c4a284c9067951724cd5e794"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387aac91fbe72b91381095f4f2f32e7be327"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387ab62fbb3ed1d684c4e0e86e0d04ee6995"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387ac421a69062c73e6eeae9c1730072cfe8"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387acb4ed5200b771b50ec1481a779230850"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387aeaaa6e5cad8201d747248f40cef19038"></a>
<a id="agroup__bt__map_html_ggadec3f7d6faccc656739a7b7a88c10387afb8f5b6bde20c9526dc520dea12f5fc6"></a>
<a id="agroup__bt__map_html_ggaef50be9a23daf42f669fde9e067b18f3a219ffe5a4584dd6eb7fdc6150389cf4c"></a>
<a id="agroup__bt__map_html_ggaef50be9a23daf42f669fde9e067b18f3a8c6316a42d350cd845a68110708a146e"></a>
<a id="agroup__bt__obex_html_ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75"></a>
<a id="agroup__bt__obex_html_ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="akernel_8h_html"></a>
<a id="al2cap_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__goep__transport__l2cap__server_html"></a>
<a id="astructbt__goep__transport__rfcomm__server_html"></a>
<a id="astructbt__goep__transport_html"></a>
<a id="astructbt__goep_html"></a>
<a id="astructbt__map__mce__mas__cb_html"></a>
<a id="astructbt__map__mce__mas__cb_html_a096e8d15124959cbbfa5c3961c44b55b"></a>
<a id="astructbt__map__mce__mas__cb_html_a15c281a0eb09f8e249b629c30d8909d2"></a>
<a id="astructbt__map__mce__mas__cb_html_a1e11b4382657e6656b41058ba575d73d"></a>
<a id="astructbt__map__mce__mas__cb_html_a283872e83a71cc79e20c51fb1312b898"></a>
<a id="astructbt__map__mce__mas__cb_html_a2c1255b9c721c844222a98e8ab5c5301"></a>
<a id="astructbt__map__mce__mas__cb_html_a3554be8e90ec9605a0a2524cb37e2561"></a>
<a id="astructbt__map__mce__mas__cb_html_a3f245b9e735bca51f16b579dea049b71"></a>
<a id="astructbt__map__mce__mas__cb_html_a41ff659151ea8d312ed178907005c9fa"></a>
<a id="astructbt__map__mce__mas__cb_html_a42a9441ceab421f0ebd9accd8577ff05"></a>
<a id="astructbt__map__mce__mas__cb_html_a51523325824c0add586e97e4fc45b985"></a>
<a id="astructbt__map__mce__mas__cb_html_a6a5a53dd82f8f7ddce0fadc4284d9ebe"></a>
<a id="astructbt__map__mce__mas__cb_html_aa491f3f467f93536d8dcdb7897552d9b"></a>
<a id="astructbt__map__mce__mas__cb_html_aa74d509e4c1e792c1187aef27bfd5e8b"></a>
<a id="astructbt__map__mce__mas__cb_html_aabecb70ffb005db1048f8615712a358f"></a>
<a id="astructbt__map__mce__mas__cb_html_abb01bd4ee41818a5c11de09035255ad5"></a>
<a id="astructbt__map__mce__mas__cb_html_aca7392666d7b4ca34c38654ee8b37a63"></a>
<a id="astructbt__map__mce__mas__cb_html_acdc05fac490ad32b5f197c673b46565f"></a>
<a id="astructbt__map__mce__mas__cb_html_adaebc7b993824d27757a9482e56a211e"></a>
<a id="astructbt__map__mce__mas__cb_html_adea73e4018513fe3f5443e2a4c3450dd"></a>
<a id="astructbt__map__mce__mas__cb_html_adebef477e23b2534fb7f54665338b0e2"></a>
<a id="astructbt__map__mce__mas_html"></a>
<a id="astructbt__map__mce__mas_html_a19563520b905384652950963fb3f8d65"></a>
<a id="astructbt__map__mce__mas_html_a546fc4ab58f8e8525f4030138db23911"></a>
<a id="astructbt__map__mce__mns__cb_html"></a>
<a id="astructbt__map__mce__mns__cb_html_a25e17d9e4d775963aedfe4f1a337a4ee"></a>
<a id="astructbt__map__mce__mns__cb_html_a5b17ed8a8dcdf149924816fa07e4ff29"></a>
<a id="astructbt__map__mce__mns__cb_html_a7266e0e0d00994af225efd63615e595d"></a>
<a id="astructbt__map__mce__mns__cb_html_a8e3c2515dce12a6bee185ae4ac38a4e7"></a>
<a id="astructbt__map__mce__mns__cb_html_aa27a21b8c6a0d088ad487f9b51c7dfc1"></a>
<a id="astructbt__map__mce__mns__cb_html_ab3da25ab3b1d96914927e834e3ca45b6"></a>
<a id="astructbt__map__mce__mns__cb_html_ad19cefcd45105bab829a427ab12f774b"></a>
<a id="astructbt__map__mce__mns__cb_html_ad516d3cc29bc6f32e9f24415cfb5c56d"></a>
<a id="astructbt__map__mce__mns__l2cap__server_html"></a>
<a id="astructbt__map__mce__mns__l2cap__server_html_a53b201ac19eaced621ef2c3297e89392"></a>
<a id="astructbt__map__mce__mns__l2cap__server_html_afb98a55954ef0892f107a5920aa5ad2c"></a>
<a id="astructbt__map__mce__mns__rfcomm__server_html"></a>
<a id="astructbt__map__mce__mns__rfcomm__server_html_ac26fdeafe3edd7f811bdd3f0a53365fa"></a>
<a id="astructbt__map__mce__mns__rfcomm__server_html_af17c8e6b2d833a8720dbfed64f2e505c"></a>
<a id="astructbt__map__mce__mns_html"></a>
<a id="astructbt__map__mce__mns_html_a89d9f42721e0b5045120f4a7279e0ffb"></a>
<a id="astructbt__map__mce__mns_html_af403bfc88cdd300b27e96cacb477ba42"></a>
<a id="astructbt__map__mse__mas__cb_html"></a>
<a id="astructbt__map__mse__mas__cb_html_a0192c32ce2e08af30ba8288025ae0b55"></a>
<a id="astructbt__map__mse__mas__cb_html_a06897a7617ee1f68f56c1b230f9f12e9"></a>
<a id="astructbt__map__mse__mas__cb_html_a1b37e5006775590e91731e873c0c4dc9"></a>
<a id="astructbt__map__mse__mas__cb_html_a1fd7e912c55a267e303e347bdd419ebe"></a>
<a id="astructbt__map__mse__mas__cb_html_a3113a29c5a6e7ba149bad09449cb5da4"></a>
<a id="astructbt__map__mse__mas__cb_html_a32dfc15ce0c67ef9b68d43c51a685668"></a>
<a id="astructbt__map__mse__mas__cb_html_a462a2826086f8ebc40617752c463bf83"></a>
<a id="astructbt__map__mse__mas__cb_html_a47d93ccf18b704eaf8d0906e75b8ddff"></a>
<a id="astructbt__map__mse__mas__cb_html_a5094efadea33ad701eaad813fe2bde50"></a>
<a id="astructbt__map__mse__mas__cb_html_a58392850c26d91c10a6ed35c7d41d6eb"></a>
<a id="astructbt__map__mse__mas__cb_html_a5d5246c3d8e3a229fdd6d33f01d48e50"></a>
<a id="astructbt__map__mse__mas__cb_html_a5fc25a4ad534e3490297faabcd86f51e"></a>
<a id="astructbt__map__mse__mas__cb_html_a6aae3db4af23f0408f328cac2b9fbf14"></a>
<a id="astructbt__map__mse__mas__cb_html_a6d0489d861546f5e9501ff6527df7d3f"></a>
<a id="astructbt__map__mse__mas__cb_html_a91407e120e3a312061c8431fd3bb48a7"></a>
<a id="astructbt__map__mse__mas__cb_html_a92d897fa7c8f9d9e42a5b8e18b25a7e1"></a>
<a id="astructbt__map__mse__mas__cb_html_ab3039d3b0e740e9eda1b3efd392916f8"></a>
<a id="astructbt__map__mse__mas__cb_html_aed0b3894512dc0e3b363d3dd98b3dfbf"></a>
<a id="astructbt__map__mse__mas__cb_html_af016d7689a8546612c73bd41cdec6e5a"></a>
<a id="astructbt__map__mse__mas__cb_html_aff9b5da1a558e79eaa744677437e66cc"></a>
<a id="astructbt__map__mse__mas__l2cap__server_html"></a>
<a id="astructbt__map__mse__mas__l2cap__server_html_a79abbf43efffd58ebd330d003c375a7b"></a>
<a id="astructbt__map__mse__mas__l2cap__server_html_ac6ad1e9b0a106cc060d6269b20d4f9b7"></a>
<a id="astructbt__map__mse__mas__rfcomm__server_html"></a>
<a id="astructbt__map__mse__mas__rfcomm__server_html_a0890ac5bf7b837818c03af77ac64ff09"></a>
<a id="astructbt__map__mse__mas__rfcomm__server_html_ac3cc9b87f871e4bb2c188244e1c41fe0"></a>
<a id="astructbt__map__mse__mas_html"></a>
<a id="astructbt__map__mse__mas_html_a07ef39faccf3fdfca8c59d4076c99885"></a>
<a id="astructbt__map__mse__mas_html_ab024f8036f13c3a01154ea45fa7d11b6"></a>
<a id="astructbt__map__mse__mns__cb_html"></a>
<a id="astructbt__map__mse__mns__cb_html_a168facdd5cdcc695814e4e9dd517f807"></a>
<a id="astructbt__map__mse__mns__cb_html_a2afd0b35998943c07584a70fa6a6107a"></a>
<a id="astructbt__map__mse__mns__cb_html_a62f7d9e4661fce6976650c3d90245dc8"></a>
<a id="astructbt__map__mse__mns__cb_html_a8cc8665110f38287951012307ce8837b"></a>
<a id="astructbt__map__mse__mns__cb_html_aac533d7aa478d0645a1853de8a5fd354"></a>
<a id="astructbt__map__mse__mns__cb_html_ab38e352b61b54a9961f200c9cf30e5b8"></a>
<a id="astructbt__map__mse__mns__cb_html_abcf2bc6750a60d66cf9999d542d0c8c2"></a>
<a id="astructbt__map__mse__mns__cb_html_acbaddcaff6e7b5a4cedaccad97186dc4"></a>
<a id="astructbt__map__mse__mns_html"></a>
<a id="astructbt__map__mse__mns_html_a524c23c6e1513bb641b103cb8fde37cb"></a>
<a id="astructbt__map__mse__mns_html_a6815c3c6af06b8cf618e9cf83fead584"></a>
<a id="astructbt__obex__client_html"></a>
<a id="astructbt__obex__server_html"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>

```c


/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_MAP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_MAP_H_


#include <zephyr/kernel.h>
#include <errno.h>

#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/l2cap.h>
#include <zephyr/bluetooth/classic/goep.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_MAP_MANDATORY_SUPPORTED_FEATURES (0x0000001FU)

#define BT_MAP_UUID_MAS                                                                            \
        (const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
                BT_UUID_128_ENCODE(0xBB582B40, 0x420C, 0x11DB, 0xB0DE, 0x0800200C9A66))

#define BT_MAP_UUID_MNS                                                                            \
        (const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
                BT_UUID_128_ENCODE(0xBB582B41, 0x420C, 0x11DB, 0xB0DE, 0x0800200C9A66))

#define BT_MAP_FILLER_BYTE "0"

#define BT_MAP_HDR_TYPE_SEND_EVENT         "x-bt/MAP-event-report"
#define BT_MAP_HDR_TYPE_SET_NTF_REG        "x-bt/MAP-NotificationRegistration"
#define BT_MAP_HDR_TYPE_GET_FOLDER_LISTING "x-obex/folder-listing"
#define BT_MAP_HDR_TYPE_GET_MSG_LISTING    "x-bt/MAP-msg-listing"
#define BT_MAP_HDR_TYPE_GET_MSG            "x-bt/message"
#define BT_MAP_HDR_TYPE_SET_MSG_STATUS     "x-bt/messageStatus"
#define BT_MAP_HDR_TYPE_PUSH_MSG           "x-bt/message"
#define BT_MAP_HDR_TYPE_UPDATE_INBOX       "x-bt/MAP-messageUpdate"
#define BT_MAP_HDR_TYPE_GET_MAS_INST_INFO  "x-bt/MASInstanceInformation"
#define BT_MAP_HDR_TYPE_SET_OWNER_STATUS   "x-bt/ownerStatus"
#define BT_MAP_HDR_TYPE_GET_OWNER_STATUS   "x-bt/ownerStatus"
#define BT_MAP_HDR_TYPE_GET_CONVO_LISTING  "x-bt/MAP-convo-listing"
#define BT_MAP_HDR_TYPE_SET_NTF_FILTER     "x-bt/MAP-notification-filter"

enum __packed bt_map_supported_features {
        BT_MAP_NTF_REG_FEATURE = BIT(0),
        BT_MAP_NTF_FEATURE = BIT(1),
        BT_MAP_BROWSING_FEATURE = BIT(2),
        BT_MAP_UPLOADING_FEATURE = BIT(3),
        BT_MAP_DELETE_FEATURE = BIT(4),
        BT_MAP_INST_INFO_FEATURE = BIT(5),
        BT_MAP_EXT_EVENT_REPORT_V11 = BIT(6),
        BT_MAP_EXT_EVENT_REPORT_V12 = BIT(7),
        BT_MAP_MSG_FORMAT_V11 = BIT(8),
        BT_MAP_MSG_LISTING_FORMAT_V11 = BIT(9),
        BT_MAP_PERSISTENT_MSG_HANDLE = BIT(10),
        BT_MAP_DB_ID = BIT(11),
        BT_MAP_FOLDER_VER_CNTR = BIT(12),
        BT_MAP_CONVO_VER_CNTR = BIT(13),
        BT_MAP_PARTICIPANT_PRESENCE_CHANGE_NTF = BIT(14),
        BT_MAP_PARTICIPANT_CHAT_STATE_CHANGE_NTF = BIT(15),
        BT_MAP_PBAP_CONTACT_XREF = BIT(16),
        BT_MAP_NTF_FILTERING = BIT(17),
        BT_MAP_UTC_OFFSET_TIMESTAMP_FORMAT = BIT(18),
        BT_MAP_SUPPORTED_FEATURES_CONN_REQ = BIT(19),
        BT_MAP_CONVO_LISTING = BIT(20),
        BT_MAP_OWNER_STATUS = BIT(21),
        BT_MAP_MSG_FORWARDING = BIT(22),
};

enum __packed bt_map_supported_msg_type {
        BT_MAP_MSG_TYPE_EMAIL = BIT(0),
        BT_MAP_MSG_TYPE_SMS_GSM = BIT(1),
        BT_MAP_MSG_TYPE_SMS_CDMA = BIT(2),
        BT_MAP_MSG_TYPE_MMS = BIT(3),
        BT_MAP_MSG_TYPE_IM = BIT(4),
};

enum __packed bt_map_set_folder_flags {
        BT_MAP_SET_FOLDER_FLAGS_ROOT = BT_OBEX_SETPATH_FLAG_NO_CREATE,
        BT_MAP_SET_FOLDER_FLAGS_DOWN = BT_OBEX_SETPATH_FLAG_NO_CREATE,
        BT_MAP_SET_FOLDER_FLAGS_UP = BT_OBEX_SETPATH_FLAG_BACKUP | BT_OBEX_SETPATH_FLAG_NO_CREATE,
};

enum __packed bt_map_appl_param_tag_id {
        BT_MAP_APPL_PARAM_TAG_ID_MAX_LIST_CNT = 0x01,
        BT_MAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET = 0x02,
        BT_MAP_APPL_PARAM_TAG_ID_FILTER_MSG_TYPE = 0x03,
        BT_MAP_APPL_PARAM_TAG_ID_FILTER_PERIOD_BEGIN = 0x04,
        BT_MAP_APPL_PARAM_TAG_ID_FILTER_PERIOD_END = 0x05,
        BT_MAP_APPL_PARAM_TAG_ID_FILTER_READ_STATUS = 0x06,
        BT_MAP_APPL_PARAM_TAG_ID_FILTER_RECIPIENT = 0x07,
        BT_MAP_APPL_PARAM_TAG_ID_FILTER_ORIGINATOR = 0x08,
        BT_MAP_APPL_PARAM_TAG_ID_FILTER_PRIORITY = 0x09,
        BT_MAP_APPL_PARAM_TAG_ID_ATTACHMENT = 0x0a,
        BT_MAP_APPL_PARAM_TAG_ID_TRANSPARENT = 0x0b,
        BT_MAP_APPL_PARAM_TAG_ID_RETRY = 0x0c,
        BT_MAP_APPL_PARAM_TAG_ID_NEW_MSG = 0x0d,
        BT_MAP_APPL_PARAM_TAG_ID_NTF_STATUS = 0x0e,
        BT_MAP_APPL_PARAM_TAG_ID_MAS_INST_ID = 0x0f,
        BT_MAP_APPL_PARAM_TAG_ID_PARAM_MASK = 0x10,
        BT_MAP_APPL_PARAM_TAG_ID_FOLDER_LISTING_SIZE = 0x11,
        BT_MAP_APPL_PARAM_TAG_ID_LISTING_SIZE = 0x12,
        BT_MAP_APPL_PARAM_TAG_ID_SUBJECT_LEN = 0x13,
        BT_MAP_APPL_PARAM_TAG_ID_CHARSET = 0x14,
        BT_MAP_APPL_PARAM_TAG_ID_FRACTION_REQUEST = 0x15,
        BT_MAP_APPL_PARAM_TAG_ID_FRACTION_DELIVER = 0x16,
        BT_MAP_APPL_PARAM_TAG_ID_STATUS_IND = 0x17,
        BT_MAP_APPL_PARAM_TAG_ID_STATUS_VAL = 0x18,
        BT_MAP_APPL_PARAM_TAG_ID_MSE_TIME = 0x19,
        BT_MAP_APPL_PARAM_TAG_ID_DB_ID = 0x1a,
        BT_MAP_APPL_PARAM_TAG_ID_CONVO_LISTING_VER_CNTR = 0x1b,
        BT_MAP_APPL_PARAM_TAG_ID_PRESENCE_AVAIL = 0x1c,
        BT_MAP_APPL_PARAM_TAG_ID_PRESENCE_TEXT = 0x1d,
        BT_MAP_APPL_PARAM_TAG_ID_LAST_ACTIVITY = 0x1e,
        BT_MAP_APPL_PARAM_TAG_ID_FILTER_LAST_ACTIVITY_BEGIN = 0x1f,
        BT_MAP_APPL_PARAM_TAG_ID_FILTER_LAST_ACTIVITY_END = 0x20,
        BT_MAP_APPL_PARAM_TAG_ID_CHAT_STATE = 0x21,
        BT_MAP_APPL_PARAM_TAG_ID_CONVO_ID = 0x22,
        BT_MAP_APPL_PARAM_TAG_ID_FOLDER_VER_CNTR = 0x23,
        BT_MAP_APPL_PARAM_TAG_ID_FILTER_MSG_HANDLE = 0x24,
        BT_MAP_APPL_PARAM_TAG_ID_NTF_FILTER_MASK = 0x25,
        BT_MAP_APPL_PARAM_TAG_ID_CONVO_PARAM_MASK = 0x26,
        BT_MAP_APPL_PARAM_TAG_ID_OWNER_UCI = 0x27,
        BT_MAP_APPL_PARAM_TAG_ID_EXT_DATA = 0x28,
        BT_MAP_APPL_PARAM_TAG_ID_MAP_SUPPORTED_FEATURES = 0x29,
        BT_MAP_APPL_PARAM_TAG_ID_MSG_HANDLE = 0x2a,
        BT_MAP_APPL_PARAM_TAG_ID_MODIFY_TEXT = 0x2b,
};

enum __packed bt_map_filter_msg_type {
        BT_MAP_FILTER_MSG_TYPE_NO_FILTERING = 0x00,
        BT_MAP_FILTER_MSG_TYPE_SMS_GSM = BIT(0),
        BT_MAP_FILTER_MSG_TYPE_SMS_CDMA = BIT(1),
        BT_MAP_FILTER_MSG_TYPE_EMAIL = BIT(2),
        BT_MAP_FILTER_MSG_TYPE_MMS = BIT(3),
        BT_MAP_FILTER_MSG_TYPE_IM = BIT(4),
};

enum __packed bt_map_filter_read_status {
        BT_MAP_FILTER_READ_STATUS_NO_FILTERING = 0x00,
        BT_MAP_FILTER_READ_STATUS_UNREAD = 0x01,
        BT_MAP_FILTER_READ_STATUS_READ = 0x02,
};

enum __packed bt_map_filter_priority {
        BT_MAP_FILTER_PRIORITY_NO_FILTERING = 0x00,
        BT_MAP_FILTER_PRIORITY_HIGH = 0x01,
        BT_MAP_FILTER_PRIORITY_NON_HIGH = 0x02,
};

enum __packed bt_map_attachment {
        BT_MAP_ATTACHMENT_OFF = 0x00,
        BT_MAP_ATTACHMENT_ON = 0x01,
};

enum __packed bt_map_transparent {
        BT_MAP_TRANSPARENT_OFF = 0x00,
        BT_MAP_TRANSPARENT_ON = 0x01,
};

enum __packed bt_map_retry {
        BT_MAP_RETRY_OFF = 0x00,
        BT_MAP_RETRY_ON = 0x01,
};

enum __packed bt_map_new_msg {
        BT_MAP_NEW_MSG_OFF = 0x00,
        BT_MAP_NEW_MSG_ON = 0x01,
};

enum __packed bt_map_ntf_status {
        BT_MAP_NTF_STATUS_OFF = 0x00,
        BT_MAP_NTF_STATUS_ON = 0x01,
};

enum __packed bt_map_param_mask {
        BT_MAP_PARAM_MASK_SUBJECT = BIT(0),
        BT_MAP_PARAM_MASK_DATETIME = BIT(1),
        BT_MAP_PARAM_MASK_SENDER_NAME = BIT(2),
        BT_MAP_PARAM_MASK_SENDER_ADDRESSING = BIT(3),
        BT_MAP_PARAM_MASK_RECIPIENT_NAME = BIT(4),
        BT_MAP_PARAM_MASK_RECIPIENT_ADDRESSING = BIT(5),
        BT_MAP_PARAM_MASK_TYPE = BIT(6),
        BT_MAP_PARAM_MASK_SIZE = BIT(7),
        BT_MAP_PARAM_MASK_RECEPTION_STATUS = BIT(8),
        BT_MAP_PARAM_MASK_TEXT = BIT(9),
        BT_MAP_PARAM_MASK_ATTACHMENT_SIZE = BIT(10),
        BT_MAP_PARAM_MASK_PRIORITY = BIT(11),
        BT_MAP_PARAM_MASK_READ = BIT(12),
        BT_MAP_PARAM_MASK_SENT = BIT(13),
        BT_MAP_PARAM_MASK_PROTECTED = BIT(14),
        BT_MAP_PARAM_MASK_REPLYTO_ADDRESSING = BIT(15),
        BT_MAP_PARAM_MASK_DELIVERY_STATUS = BIT(16),
        BT_MAP_PARAM_MASK_CONVO_ID = BIT(17),
        BT_MAP_PARAM_MASK_CONVO_NAME = BIT(18),
        BT_MAP_PARAM_MASK_DIRECTION = BIT(19),
        BT_MAP_PARAM_MASK_ATTACHMENT_MIME = BIT(20),
};

enum __packed bt_map_charset {
        BT_MAP_CHARSET_NATIVE = 0x00,
        BT_MAP_CHARSET_UTF8 = 0x01,
};

enum __packed bt_map_fraction_request {
        BT_MAP_FRACTION_REQUEST_FIRST = 0x00,
        BT_MAP_FRACTION_REQUEST_NEXT = 0x01,
};

enum __packed bt_map_fraction_deliver {
        BT_MAP_FRACTION_DELIVER_MORE = 0x00,
        BT_MAP_FRACTION_DELIVER_LAST = 0x01,
};

enum __packed bt_map_status_ind {
        BT_MAP_STATUS_IND_READ = 0x00,
        BT_MAP_STATUS_IND_DELETED = 0x01,
        BT_MAP_STATUS_IND_EXTENDED_DATA = 0x02,
};

enum __packed bt_map_status_val {
        BT_MAP_STATUS_VAL_NO = 0x00,
        BT_MAP_STATUS_VAL_YES = 0x01,
};

enum __packed bt_map_presence {
        BT_MAP_PRESENCE_UNKNOWN = 0x00,
        BT_MAP_PRESENCE_OFFLINE = 0x01,
        BT_MAP_PRESENCE_ONLINE = 0x02,
        BT_MAP_PRESENCE_AWAY = 0x03,
        BT_MAP_PRESENCE_DO_NOT_DISTURB = 0x04,
        BT_MAP_PRESENCE_BUSY = 0x05,
        BT_MAP_PRESENCE_IN_A_MEETING = 0x06,
};

enum __packed bt_map_chat_state {
        BT_MAP_CHAT_STATE_UNKNOWN = 0x00,
        BT_MAP_CHAT_STATE_INACTIVE = 0x01,
        BT_MAP_CHAT_STATE_ACTIVE = 0x02,
        BT_MAP_CHAT_STATE_COMPOSING = 0x03,
        BT_MAP_CHAT_STATE_PAUSED_COMPOSING = 0x04,
        BT_MAP_CHAT_STATE_GONE = 0x05,
};

enum __packed bt_map_ntf_filter_mask {
        BT_MAP_NTF_FILTER_MASK_NEW_MSG = BIT(0),
        BT_MAP_NTF_FILTER_MASK_MSG_DELETED = BIT(1),
        BT_MAP_NTF_FILTER_MASK_MSG_SHIFT = BIT(2),
        BT_MAP_NTF_FILTER_MASK_SENDING_SUCCESS = BIT(3),
        BT_MAP_NTF_FILTER_MASK_SENDING_FAILURE = BIT(4),
        BT_MAP_NTF_FILTER_MASK_DELIVERY_SUCCESS = BIT(5),
        BT_MAP_NTF_FILTER_MASK_DELIVERY_FAILURE = BIT(6),
        BT_MAP_NTF_FILTER_MASK_MEM_FULL = BIT(7),
        BT_MAP_NTF_FILTER_MASK_MEM_AVAIL = BIT(8),
        BT_MAP_NTF_FILTER_MASK_READ_STATUS_CHANGED = BIT(9),
        BT_MAP_NTF_FILTER_MASK_CONVO_CHANGED = BIT(10),
        BT_MAP_NTF_FILTER_MASK_PARTICIPANT_PRESENCE_CHANGED = BIT(11),
        BT_MAP_NTF_FILTER_MASK_PARTICIPANT_CHAT_STATE_CHANGED = BIT(12),
        BT_MAP_NTF_FILTER_MASK_MSG_EXT_DATA_CHANGED = BIT(13),
        BT_MAP_NTF_FILTER_MASK_MSG_REMOVED = BIT(14),
};

enum __packed bt_map_convo_param_mask {
        BT_MAP_CONVO_PARAM_MASK_CONVO_NAME = BIT(0),
        BT_MAP_CONVO_PARAM_MASK_CONVO_LAST_ACTIVITY = BIT(1),
        BT_MAP_CONVO_PARAM_MASK_READ_STATUS = BIT(2),
        BT_MAP_CONVO_PARAM_MASK_VER_CNTR = BIT(3),
        BT_MAP_CONVO_PARAM_MASK_SUMMARY = BIT(4),
        BT_MAP_CONVO_PARAM_MASK_PARTICIPANTS = BIT(5),
        BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_UCI = BIT(6),
        BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_DISP_NAME = BIT(7),
        BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_CHAT_STATE = BIT(8),
        BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_LAST_ACTIVITY = BIT(9),
        BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_X_BT_UID = BIT(10),
        BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_NAME = BIT(11),
        BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRESENCE_AVAIL = BIT(12),
        BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRESENCE_TEXT = BIT(13),
        BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRIORITY = BIT(14),
};

enum __packed bt_map_msg_ext_data {
        BT_MAP_MSG_EXT_DATA_FACEBOOK_LIKES = 0x00,
        BT_MAP_MSG_EXT_DATA_TWITTER_FOLLOWERS = 0x01,
        BT_MAP_MSG_EXT_DATA_TWITTER_RETWEETS = 0x02,
        BT_MAP_MSG_EXT_DATA_GOOGLE_1S = 0x03,
};

enum __packed bt_map_modify_text {
        BT_MAP_MODIFY_TEXT_REPLACE = 0x00,
        BT_MAP_MODIFY_TEXT_PREPEND = 0x01,
};


struct bt_map_mce_mas;

struct bt_map_mce_mas_cb {
        void (*rfcomm_connected)(struct bt_conn *conn, struct bt_map_mce_mas *mce_mas);

        void (*rfcomm_disconnected)(struct bt_map_mce_mas *mce_mas);

        void (*l2cap_connected)(struct bt_conn *conn, struct bt_map_mce_mas *mce_mas);

        void (*l2cap_disconnected)(struct bt_map_mce_mas *mce_mas);

        void (*connect)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, uint8_t version,
                        uint16_t mopl, struct net_buf *buf);

        void (*disconnect)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf);

        void (*abort)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf);

        void (*set_ntf_reg)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf);

        void (*set_folder)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf);

        void (*get_folder_listing)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code,
                                   struct net_buf *buf);

        void (*get_msg_listing)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code,
                                struct net_buf *buf);

        void (*get_msg)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf);

        void (*set_msg_status)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code,
                               struct net_buf *buf);

        void (*push_msg)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf);

        void (*update_inbox)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf);

        void (*get_mas_inst_info)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code,
                                  struct net_buf *buf);

        void (*set_owner_status)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code,
                                 struct net_buf *buf);

        void (*get_owner_status)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code,
                                 struct net_buf *buf);

        void (*get_convo_listing)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code,
                                  struct net_buf *buf);

        void (*set_ntf_filter)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code,
                               struct net_buf *buf);
};

struct bt_map_mce_mas {
        struct bt_goep_transport goep_transport;

        struct bt_goep goep;

        const struct bt_map_mce_mas_cb *_cb;

        atomic_t _transport_state;

        uint32_t _conn_id;

        struct bt_obex_client _client;

        atomic_t _state;

        void (*_rsp_cb)(struct bt_map_mce_mas *mce_mas, uint8_t rsp_code, struct net_buf *buf);

        const char *_req_type;
};

int bt_map_mce_mas_rfcomm_connect(struct bt_conn *conn, struct bt_map_mce_mas *mce_mas,
                                  const struct bt_map_mce_mas_cb *cb, uint8_t channel);

int bt_map_mce_mas_rfcomm_disconnect(struct bt_map_mce_mas *mce_mas);

int bt_map_mce_mas_l2cap_connect(struct bt_conn *conn, struct bt_map_mce_mas *mce_mas,
                                 const struct bt_map_mce_mas_cb *cb, uint16_t psm);

int bt_map_mce_mas_l2cap_disconnect(struct bt_map_mce_mas *mce_mas);

struct net_buf *bt_map_mce_mas_create_pdu(struct bt_map_mce_mas *mce_mas,
                                          struct net_buf_pool *pool);

int bt_map_mce_mas_connect(struct bt_map_mce_mas *mce_mas, struct net_buf *buf);

int bt_map_mce_mas_disconnect(struct bt_map_mce_mas *mce_mas, struct net_buf *buf);

int bt_map_mce_mas_abort(struct bt_map_mce_mas *mce_mas, struct net_buf *buf);

int bt_map_mce_mas_set_folder(struct bt_map_mce_mas *mce_mas, uint8_t flags, struct net_buf *buf);

int bt_map_mce_mas_set_ntf_reg(struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf);

int bt_map_mce_mas_get_folder_listing(struct bt_map_mce_mas *mce_mas, bool final,
                                      struct net_buf *buf);

int bt_map_mce_mas_get_msg_listing(struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf);

int bt_map_mce_mas_get_msg(struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf);

int bt_map_mce_mas_set_msg_status(struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf);

int bt_map_mce_mas_push_msg(struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf);

int bt_map_mce_mas_update_inbox(struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf);

int bt_map_mce_mas_get_mas_inst_info(struct bt_map_mce_mas *mce_mas, bool final,
                                     struct net_buf *buf);

int bt_map_mce_mas_set_owner_status(struct bt_map_mce_mas *mce_mas, bool final,
                                    struct net_buf *buf);

int bt_map_mce_mas_get_owner_status(struct bt_map_mce_mas *mce_mas, bool final,
                                    struct net_buf *buf);

int bt_map_mce_mas_get_convo_listing(struct bt_map_mce_mas *mce_mas, bool final,
                                     struct net_buf *buf);

int bt_map_mce_mas_set_ntf_filter(struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf);
 /* end of bt_map_mce_mas */


struct bt_map_mce_mns;

struct bt_map_mce_mns_rfcomm_server {
        struct bt_goep_transport_rfcomm_server server;
        int (*accept)(struct bt_conn *conn, struct bt_map_mce_mns_rfcomm_server *server,
                      struct bt_map_mce_mns **mce_mns);
};

struct bt_map_mce_mns_l2cap_server {
        struct bt_goep_transport_l2cap_server server;
        int (*accept)(struct bt_conn *conn, struct bt_map_mce_mns_l2cap_server *server,
                      struct bt_map_mce_mns **mce_mns);
};

struct bt_map_mce_mns_cb {
        void (*rfcomm_connected)(struct bt_conn *conn, struct bt_map_mce_mns *mce_mns);

        void (*rfcomm_disconnected)(struct bt_map_mce_mns *mce_mns);

        void (*l2cap_connected)(struct bt_conn *conn, struct bt_map_mce_mns *mce_mns);

        void (*l2cap_disconnected)(struct bt_map_mce_mns *mce_mns);

        void (*connect)(struct bt_map_mce_mns *mce_mns, uint8_t version, uint16_t mopl,
                        struct net_buf *buf);

        void (*disconnect)(struct bt_map_mce_mns *mce_mns, struct net_buf *buf);

        void (*abort)(struct bt_map_mce_mns *mce_mns, struct net_buf *buf);

        void (*send_event)(struct bt_map_mce_mns *mce_mns, bool final, struct net_buf *buf);
};

struct bt_map_mce_mns {
        struct bt_goep_transport goep_transport;

        struct bt_goep goep;

        const struct bt_map_mce_mns_cb *_cb;

        atomic_t _transport_state;

        uint32_t _conn_id;

        struct bt_obex_server _server;

        atomic_t _state;

        void (*_req_cb)(struct bt_map_mce_mns *mce_mns, bool final, struct net_buf *buf);

        const char *_optype;

        uint8_t _opcode;
};

int bt_map_mce_mns_register(struct bt_map_mce_mns *mce_mns, const struct bt_map_mce_mns_cb *cb);

int bt_map_mce_mns_rfcomm_register(struct bt_map_mce_mns_rfcomm_server *server);

int bt_map_mce_mns_rfcomm_disconnect(struct bt_map_mce_mns *mce_mns);

int bt_map_mce_mns_l2cap_register(struct bt_map_mce_mns_l2cap_server *server);

int bt_map_mce_mns_l2cap_disconnect(struct bt_map_mce_mns *mce_mns);

struct net_buf *bt_map_mce_mns_create_pdu(struct bt_map_mce_mns *mce_mns,
                                          struct net_buf_pool *pool);

int bt_map_mce_mns_connect(struct bt_map_mce_mns *mce_mns, uint8_t rsp_code, struct net_buf *buf);

int bt_map_mce_mns_disconnect(struct bt_map_mce_mns *mce_mns, uint8_t rsp_code,
                              struct net_buf *buf);

int bt_map_mce_mns_abort(struct bt_map_mce_mns *mce_mns, uint8_t rsp_code, struct net_buf *buf);

int bt_map_mce_mns_send_event(struct bt_map_mce_mns *mce_mns, uint8_t rsp_code,
                              struct net_buf *buf);
 /* end of bt_map_mce_mns */


struct bt_map_mse_mas;

struct bt_map_mse_mas_rfcomm_server {
        struct bt_goep_transport_rfcomm_server server;

        int (*accept)(struct bt_conn *conn, struct bt_map_mse_mas_rfcomm_server *server,
                      struct bt_map_mse_mas **mse_mas);
};

struct bt_map_mse_mas_l2cap_server {
        struct bt_goep_transport_l2cap_server server;

        int (*accept)(struct bt_conn *conn, struct bt_map_mse_mas_l2cap_server *server,
                      struct bt_map_mse_mas **mse_mas);
};

struct bt_map_mse_mas_cb {
        void (*rfcomm_connected)(struct bt_conn *conn, struct bt_map_mse_mas *mse_mas);

        void (*rfcomm_disconnected)(struct bt_map_mse_mas *mse_mas);

        void (*l2cap_connected)(struct bt_conn *conn, struct bt_map_mse_mas *mse_mas);

        void (*l2cap_disconnected)(struct bt_map_mse_mas *mse_mas);

        void (*connect)(struct bt_map_mse_mas *mse_mas, uint8_t version, uint16_t mopl,
                        struct net_buf *buf);

        void (*disconnect)(struct bt_map_mse_mas *mse_mas, struct net_buf *buf);

        void (*abort)(struct bt_map_mse_mas *mse_mas, struct net_buf *buf);

        void (*set_ntf_reg)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        void (*set_folder)(struct bt_map_mse_mas *mse_mas, uint8_t flags, struct net_buf *buf);

        void (*get_folder_listing)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        void (*get_msg_listing)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        void (*get_msg)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        void (*set_msg_status)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        void (*push_msg)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        void (*update_inbox)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        void (*get_mas_inst_info)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        void (*set_owner_status)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        void (*get_owner_status)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        void (*get_convo_listing)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        void (*set_ntf_filter)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);
};

struct bt_map_mse_mas {
        struct bt_goep_transport goep_transport;

        struct bt_goep goep;

        const struct bt_map_mse_mas_cb *_cb;

        atomic_t _transport_state;

        uint32_t _conn_id;

        struct bt_obex_server _server;

        atomic_t _state;

        void (*_req_cb)(struct bt_map_mse_mas *mse_mas, bool final, struct net_buf *buf);

        const char *_optype;

        uint8_t _opcode;
};

int bt_map_mse_mas_register(struct bt_map_mse_mas *mse_mas, const struct bt_map_mse_mas_cb *cb);

int bt_map_mse_mas_rfcomm_register(struct bt_map_mse_mas_rfcomm_server *server);

int bt_map_mse_mas_rfcomm_disconnect(struct bt_map_mse_mas *mse_mas);

int bt_map_mse_mas_l2cap_register(struct bt_map_mse_mas_l2cap_server *server);

int bt_map_mse_mas_l2cap_disconnect(struct bt_map_mse_mas *mse_mas);

struct net_buf *bt_map_mse_mas_create_pdu(struct bt_map_mse_mas *mse_mas,
                                          struct net_buf_pool *pool);

int bt_map_mse_mas_connect(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf);

int bt_map_mse_mas_disconnect(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                              struct net_buf *buf);

int bt_map_mse_mas_abort(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf);

int bt_map_mse_mas_set_folder(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                              struct net_buf *buf);

int bt_map_mse_mas_set_ntf_reg(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                               struct net_buf *buf);

int bt_map_mse_mas_get_folder_listing(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                                      struct net_buf *buf);

int bt_map_mse_mas_get_msg_listing(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                                   struct net_buf *buf);

int bt_map_mse_mas_get_msg(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf);

int bt_map_mse_mas_set_msg_status(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                                  struct net_buf *buf);

int bt_map_mse_mas_push_msg(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf);

int bt_map_mse_mas_update_inbox(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                                struct net_buf *buf);

int bt_map_mse_mas_get_mas_inst_info(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                                     struct net_buf *buf);

int bt_map_mse_mas_set_owner_status(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                                    struct net_buf *buf);

int bt_map_mse_mas_get_owner_status(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                                    struct net_buf *buf);

int bt_map_mse_mas_get_convo_listing(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                                     struct net_buf *buf);

int bt_map_mse_mas_set_ntf_filter(struct bt_map_mse_mas *mse_mas, uint8_t rsp_code,
                                  struct net_buf *buf);
 /* end of bt_map_mse_mas */


struct bt_map_mse_mns;

struct bt_map_mse_mns_cb {
        void (*rfcomm_connected)(struct bt_conn *conn, struct bt_map_mse_mns *mse_mns);

        void (*rfcomm_disconnected)(struct bt_map_mse_mns *mse_mns);

        void (*l2cap_connected)(struct bt_conn *conn, struct bt_map_mse_mns *mse_mns);

        void (*l2cap_disconnected)(struct bt_map_mse_mns *mse_mns);

        void (*connect)(struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, uint8_t version,
                        uint16_t mopl, struct net_buf *buf);

        void (*disconnect)(struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, struct net_buf *buf);

        void (*abort)(struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, struct net_buf *buf);

        void (*send_event)(struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, struct net_buf *buf);
};

struct bt_map_mse_mns {
        struct bt_goep_transport goep_transport;

        struct bt_goep goep;

        const struct bt_map_mse_mns_cb *_cb;

        atomic_t _transport_state;

        uint32_t _conn_id;

        struct bt_obex_client _client;

        atomic_t _state;

        void (*_rsp_cb)(struct bt_map_mse_mns *mse_mns, uint8_t rsp_code, struct net_buf *buf);

        const char *_req_type;
};

int bt_map_mse_mns_rfcomm_connect(struct bt_conn *conn, struct bt_map_mse_mns *mse_mns,
                                  const struct bt_map_mse_mns_cb *cb, uint8_t channel);

int bt_map_mse_mns_rfcomm_disconnect(struct bt_map_mse_mns *mse_mns);

int bt_map_mse_mns_l2cap_connect(struct bt_conn *conn, struct bt_map_mse_mns *mse_mns,
                                 const struct bt_map_mse_mns_cb *cb, uint16_t psm);

int bt_map_mse_mns_l2cap_disconnect(struct bt_map_mse_mns *mse_mns);

struct net_buf *bt_map_mse_mns_create_pdu(struct bt_map_mse_mns *mse_mns,
                                          struct net_buf_pool *pool);

int bt_map_mse_mns_connect(struct bt_map_mse_mns *mse_mns, struct net_buf *buf);

int bt_map_mse_mns_disconnect(struct bt_map_mse_mns *mse_mns, struct net_buf *buf);

int bt_map_mse_mns_abort(struct bt_map_mse_mns *mse_mns, struct net_buf *buf);

int bt_map_mse_mns_send_event(struct bt_map_mse_mns *mse_mns, bool final, struct net_buf *buf);
 /* end of bt_map_mse_mns */

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_MAP_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 1219 行

`bt_map_mce_mas` 分组结束（End）。

### 注释 3：原第 1531 行

`bt_map_mce_mns` 分组结束（End）。

### 注释 4：原第 2183 行

`bt_map_mse_mas` 分组结束（End）。

### 注释 5：原第 2452 行

`bt_map_mse_mns` 分组结束（End）。

### 注释 6：原第 2463 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_MAP_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)
- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html)
- [bt_map_supported_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga6d4c3231e2e64190c6ccc30b4d5f822c)
- [BT_MAP_NTF_REG_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822cae5fa5f417d064a1b85e9db70a5ce94e5)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_MAP_NTF_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822cac4a88df48198a497da4a94ec124bb735)
- [BT_MAP_BROWSING_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caec96609ac47f6cf1e779d049687f2e63)
- [BT_MAP_UPLOADING_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca572d7eb54deb371cee55c0149f21d6db)
- [BT_MAP_DELETE_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caa7e8028e50f7903aefd379d76695408f)
- [BT_MAP_INST_INFO_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca32cf970e22e8f082293225b5a614de8d)
- [BT_MAP_EXT_EVENT_REPORT_V11](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca7467b703f0cf9d760d6d18e0dd6dfa7f)
- [BT_MAP_EXT_EVENT_REPORT_V12](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca2cbc347cb637a951868052e58eb3dab9)
- [BT_MAP_MSG_FORMAT_V11](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caa6de591a1e2d5936263741f273c9fb8a)
- [BT_MAP_MSG_LISTING_FORMAT_V11](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822cae28c62057713e3a7318cf85eaa7c337e)
- [BT_MAP_PERSISTENT_MSG_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca5e63f64fb534af8295995a0fbec364df)
- [BT_MAP_DB_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca71243a44c4d5a105c02b49318302fb7a)
- [BT_MAP_FOLDER_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca2c7cbab7fe254b975668563039c7ace8)
- [BT_MAP_CONVO_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca8d214b20b66be2264fb8da2d9feb93d0)
- [BT_MAP_PARTICIPANT_PRESENCE_CHANGE_NTF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca2843780dad72eaa1d84cec56077cff93)
- [BT_MAP_PARTICIPANT_CHAT_STATE_CHANGE_NTF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca1bc10abe061f68c3de72c37b5307c484)
- [BT_MAP_PBAP_CONTACT_XREF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca679c98163ee9b3114c7adf64b6976a9e)
- [BT_MAP_NTF_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca3353469789a5a72f4fc97dabed1d4dcf)
- [BT_MAP_UTC_OFFSET_TIMESTAMP_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca9aaa859278454e081c5fe5e83dfded5d)
- [BT_MAP_SUPPORTED_FEATURES_CONN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caa76c12d6babf2df623f28f58ed1912d0)
- [BT_MAP_CONVO_LISTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca35f15fe0fba34519ff0d1087c2e32c4c)
- [BT_MAP_OWNER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca6aa30c2d7dccbe630756c1f1e4f7a141)
- [BT_MAP_MSG_FORWARDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caccc791a50cc33ef4d62d6b126c1ba898)
- [bt_map_supported_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5bb2e0b7951bde5042fbb9c4e0c7cc26)
- [BT_MAP_MSG_TYPE_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26ae0396ce6457b9792d564195f906fafe3)
- [BT_MAP_MSG_TYPE_SMS_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a0f4bd271fb4a331e66dafde2a04fd62a)
- [BT_MAP_MSG_TYPE_SMS_CDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a803694148d134338a83f365390929505)
- [BT_MAP_MSG_TYPE_MMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a9f65cf3b8d5a5855219599ed656ea56c)
- [BT_MAP_MSG_TYPE_IM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a038430c6eea453638a2fc3351315b638)
- [bt_map_set_folder_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5678131af7da533ff8b751555542933e)
- [BT_MAP_SET_FOLDER_FLAGS_ROOT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5678131af7da533ff8b751555542933eaa5d3b0ad2bf7f8600ad059132aaed665)
- [BT_OBEX_SETPATH_FLAG_NO_CREATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553)
- [BT_MAP_SET_FOLDER_FLAGS_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5678131af7da533ff8b751555542933ead7b0402847a837a69055dcf4b6fad674)
- [BT_MAP_SET_FOLDER_FLAGS_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5678131af7da533ff8b751555542933ea8b13f5d7fc245c7b66a65e0845ed7edc)
- [BT_OBEX_SETPATH_FLAG_BACKUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75)
- [bt_map_appl_param_tag_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga7310a116a939b40d7ee346371b5ccd88)
- [BT_MAP_APPL_PARAM_TAG_ID_MAX_LIST_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a2df85ffb7e034732fb608c6935af9297)
- [BT_MAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7227e024472a421c86c3cb7a0db65e55)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_MSG_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88af39bad93c459fcb86b9583a1519c070b)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_PERIOD_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7627a7496631fbe6326e4c1c43e4877c)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_PERIOD_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a2071ba2e3ec0dc8b5adc8b97a37a010d)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_READ_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88aa1b59e01c63abc3ccc7ee54ca27e9296)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_RECIPIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ac6118aa692c3c382ce7630ac2d499aac)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_ORIGINATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88adb08ba0bbc13653357e835dcd6fa5770)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a637ac76aafe5a586819b9897acc7d1da)
- [BT_MAP_APPL_PARAM_TAG_ID_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad53697174462dfe4d2d592bf71bf180c)
- [BT_MAP_APPL_PARAM_TAG_ID_TRANSPARENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a595f6e5f7eac3c57dccf13e1e45dfd6b)
- [BT_MAP_APPL_PARAM_TAG_ID_RETRY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a19b5e72c512c29b5cfbe58dbdaf63064)
- [BT_MAP_APPL_PARAM_TAG_ID_NEW_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a4871d9d7da47983cd5fd7a7718ab2478)
- [BT_MAP_APPL_PARAM_TAG_ID_NTF_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88aee3ebbef8eb74deefedb414daea2dc1e)
- [BT_MAP_APPL_PARAM_TAG_ID_MAS_INST_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a170d3717ab48a7f6a63e8bd66d1cb228)
- [BT_MAP_APPL_PARAM_TAG_ID_PARAM_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a563fbb6001387da1389713be552fec13)
- [BT_MAP_APPL_PARAM_TAG_ID_FOLDER_LISTING_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a1aca8ccd385944cb73f03568123dc1e3)
- [BT_MAP_APPL_PARAM_TAG_ID_LISTING_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88aa9241c4f620f61717160d5dbc9dc5389)
- [BT_MAP_APPL_PARAM_TAG_ID_SUBJECT_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a15c0a2959d67e24ed18203cd8c9fe46a)
- [BT_MAP_APPL_PARAM_TAG_ID_CHARSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad1d1edb33a8147e1d96400607e8f3f1e)
- [BT_MAP_APPL_PARAM_TAG_ID_FRACTION_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88acfef6214cbd687aa5ad7ee4d8d3a4a2d)
- [BT_MAP_APPL_PARAM_TAG_ID_FRACTION_DELIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a8651767d6b1c5dc6f0affac25014aeaa)
- [BT_MAP_APPL_PARAM_TAG_ID_STATUS_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a5622480195120444b2f200e79db09499)
- [BT_MAP_APPL_PARAM_TAG_ID_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a4ee0642cd16aa8e1ce5224118968f9ee)
- [BT_MAP_APPL_PARAM_TAG_ID_MSE_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a0bb8acb58e8983793bb787ae8e6d4033)
- [BT_MAP_APPL_PARAM_TAG_ID_DB_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7f9d301f9383d8179611344d18f03094)
- [BT_MAP_APPL_PARAM_TAG_ID_CONVO_LISTING_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a8f4a492c9619ec1b78124f0509b93857)
- [BT_MAP_APPL_PARAM_TAG_ID_PRESENCE_AVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7636683c2efff7c4c8d59a141c6e12b6)
- [BT_MAP_APPL_PARAM_TAG_ID_PRESENCE_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a06ae16f7d6a3a247e5e1771254df0ea9)
- [BT_MAP_APPL_PARAM_TAG_ID_LAST_ACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a6f5914896a591c0008fb744506ec98d4)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_LAST_ACTIVITY_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a5ec11c380b39a38cade5acd06545b1a1)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_LAST_ACTIVITY_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad49f0edd1a6e1c1da5a37abd552cc6b1)
- [BT_MAP_APPL_PARAM_TAG_ID_CHAT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88adaad04f88448466dd606527157d74cc7)
- [BT_MAP_APPL_PARAM_TAG_ID_CONVO_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a72083eddb755825e5899dfddbcc10085)
- [BT_MAP_APPL_PARAM_TAG_ID_FOLDER_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a706346ca21cb1f76c22dc02af1076b04)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_MSG_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a600395d6f4620dffee2447ae8b9a4fbe)
- [BT_MAP_APPL_PARAM_TAG_ID_NTF_FILTER_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a161b7d1952483a47eee81dfd98ce831c)
- [BT_MAP_APPL_PARAM_TAG_ID_CONVO_PARAM_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a79da1ebc8b5e7e0d1098d4b022fa8da7)
- [BT_MAP_APPL_PARAM_TAG_ID_OWNER_UCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad3058d06b585289586c5cccaab548bc2)
- [BT_MAP_APPL_PARAM_TAG_ID_EXT_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a81297adf58afc780a00afe8ef4a70c95)
- [BT_MAP_APPL_PARAM_TAG_ID_MAP_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a9f08b382471f807452d9cf7e1bff1b3b)
- [BT_MAP_APPL_PARAM_TAG_ID_MSG_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a6b4d28c95336af96c06a71f6cb40060b)
- [BT_MAP_APPL_PARAM_TAG_ID_MODIFY_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a208c8d9ea3195b7d70ab2e7ccae6671d)
- [bt_map_filter_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga7c4ba8b9727c454a54a2178d584dfcb7)
- [BT_MAP_FILTER_MSG_TYPE_NO_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7adfc6a259bbc5d1b6a0b30d57d1a5b7a9)
- [BT_MAP_FILTER_MSG_TYPE_SMS_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a2ab7b8a63e2dae0bf8d82e5c7aae3038)
- [BT_MAP_FILTER_MSG_TYPE_SMS_CDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a9df74f88cb18833440816218a610527c)
- [BT_MAP_FILTER_MSG_TYPE_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a37bca39682be9efa27f906754d972b7d)
- [BT_MAP_FILTER_MSG_TYPE_MMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a1b10e235398a004168731de140b7e6d8)
- [BT_MAP_FILTER_MSG_TYPE_IM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7ab80d08d33c7fc5adc1483b1be64390c0)
- [bt_map_filter_read_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gabf5f60778a9adf113e86e559095dd66f)
- [BT_MAP_FILTER_READ_STATUS_NO_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabf5f60778a9adf113e86e559095dd66fa0c7b3c3b9c8f0d9c514a9730d57d7738)
- [BT_MAP_FILTER_READ_STATUS_UNREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabf5f60778a9adf113e86e559095dd66fae90806b4b223afc531d74dd1819ff7b3)
- [BT_MAP_FILTER_READ_STATUS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabf5f60778a9adf113e86e559095dd66faf9e8514d6411d25bc71a33e7f351f93f)
- [bt_map_filter_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga4f1f483d5edfaa151a11086caac24e5c)
- [BT_MAP_FILTER_PRIORITY_NO_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4f1f483d5edfaa151a11086caac24e5ca0f8654affc09e99bad440d2b9faeb163)
- [BT_MAP_FILTER_PRIORITY_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4f1f483d5edfaa151a11086caac24e5ca66220e415b9164fe41a19e423b4aad90)
- [BT_MAP_FILTER_PRIORITY_NON_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4f1f483d5edfaa151a11086caac24e5ca12b73e28e320ba1bf3aa8edf44b053cd)
- [bt_map_attachment](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga34cee2f295fee5b00bced31753f03b25)
- [BT_MAP_ATTACHMENT_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga34cee2f295fee5b00bced31753f03b25a74198afdf437d36971d5cf4fdcaab5b8)
- [BT_MAP_ATTACHMENT_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga34cee2f295fee5b00bced31753f03b25a089baca6845a803dda4b7e506e452b5b)
- [bt_map_transparent](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga215e8bd71131e739b19f5f5ee57904e6)
- [BT_MAP_TRANSPARENT_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga215e8bd71131e739b19f5f5ee57904e6a5f1552a26d09f1c696f828967222707f)
- [BT_MAP_TRANSPARENT_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga215e8bd71131e739b19f5f5ee57904e6addfabaeaa7d8903c81b41c9844514849)
- [bt_map_retry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga4a9fc0bfa14b5e91491aec130e396429)
- [BT_MAP_RETRY_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4a9fc0bfa14b5e91491aec130e396429a4955b62b432b783eb774d704e2f2b4e2)
- [BT_MAP_RETRY_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4a9fc0bfa14b5e91491aec130e396429a0215a73c93fe79bbd9fc28b34af31057)
- [bt_map_new_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga8dcd4f8704a2b1cab77b2279d7f2024f)
- [BT_MAP_NEW_MSG_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8dcd4f8704a2b1cab77b2279d7f2024fabe2ef316affe063b7634ca5e5f2e0351)
- [BT_MAP_NEW_MSG_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8dcd4f8704a2b1cab77b2279d7f2024fa735aac580ed7fae38d10bcc41f2b393a)
- [bt_map_ntf_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga8b805587e1abb311367e59d80d223516)
- [BT_MAP_NTF_STATUS_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8b805587e1abb311367e59d80d223516a8c7e4fd24ff699c52a7ecba484923cfb)
- [BT_MAP_NTF_STATUS_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8b805587e1abb311367e59d80d223516a25fc04d24537a005dc4674d29ad48357)
- [bt_map_param_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gadec3f7d6faccc656739a7b7a88c10387)
- [BT_MAP_PARAM_MASK_SUBJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387aac91fbe72b91381095f4f2f32e7be327)
- [BT_MAP_PARAM_MASK_DATETIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a898d380bc11251e69d4525c2e3f5fcbe)
- [BT_MAP_PARAM_MASK_SENDER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a1cad006d6e9d8740e929a801a3a3593f)
- [BT_MAP_PARAM_MASK_SENDER_ADDRESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a0c4cac1477808905597af3d1373663d4)
- [BT_MAP_PARAM_MASK_RECIPIENT_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a90f5931d1fe65f3f2b0718c357e45740)
- [BT_MAP_PARAM_MASK_RECIPIENT_ADDRESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387aeaaa6e5cad8201d747248f40cef19038)
- [BT_MAP_PARAM_MASK_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387ab62fbb3ed1d684c4e0e86e0d04ee6995)
- [BT_MAP_PARAM_MASK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a8c7c06f8ebdd5e433e926345d62c092b)
- [BT_MAP_PARAM_MASK_RECEPTION_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a1b55581c15bf6d915a748fff1655f2eb)
- [BT_MAP_PARAM_MASK_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a5b0a0672211d6e9a0e377baaa16f449a)
- [BT_MAP_PARAM_MASK_ATTACHMENT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a1c86d02bc4003273da0e84ebaeaa4ae8)
- [BT_MAP_PARAM_MASK_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a07145a14474b470e1dc9143d115add4f)
- [BT_MAP_PARAM_MASK_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387afb8f5b6bde20c9526dc520dea12f5fc6)
- [BT_MAP_PARAM_MASK_SENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a47987b441c785b7657f9323ec7858d51)
- [BT_MAP_PARAM_MASK_PROTECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a302b63d08cb7ff36204c2f390b746375)
- [BT_MAP_PARAM_MASK_REPLYTO_ADDRESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a295391beee4e7f92c9e5745785da214d)
- [BT_MAP_PARAM_MASK_DELIVERY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387acb4ed5200b771b50ec1481a779230850)
- [BT_MAP_PARAM_MASK_CONVO_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387ac421a69062c73e6eeae9c1730072cfe8)
- [BT_MAP_PARAM_MASK_CONVO_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a21a483901085035c22fc3baf02931df6)
- [BT_MAP_PARAM_MASK_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a001c4dc6084e12938867c4a1eb7316ea)
- [BT_MAP_PARAM_MASK_ATTACHMENT_MIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387aac5a5819c4a284c9067951724cd5e794)
- [bt_map_charset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga0fa30e8b33826204f0625a2223cfaf1c)
- [BT_MAP_CHARSET_NATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga0fa30e8b33826204f0625a2223cfaf1ca104a2dd364f1e86b9b5f4cd8fea38011)
- [BT_MAP_CHARSET_UTF8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga0fa30e8b33826204f0625a2223cfaf1ca45f4dd02d1e4c1ce1ceef8be95684a51)
- [bt_map_fraction_request](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga430b14f450167b13329f54377473b699)
- [BT_MAP_FRACTION_REQUEST_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga430b14f450167b13329f54377473b699a1a041e3eed1744fe8d02908be402b0a4)
- [BT_MAP_FRACTION_REQUEST_NEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga430b14f450167b13329f54377473b699a22d8803a6310974137af6d8bc0c9e6a8)
- [bt_map_fraction_deliver](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga3d3327344323fae6f7a2b1ebca459db0)
- [BT_MAP_FRACTION_DELIVER_MORE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga3d3327344323fae6f7a2b1ebca459db0ab4134b8e2c9987789fa541627d9ab19f)
- [BT_MAP_FRACTION_DELIVER_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga3d3327344323fae6f7a2b1ebca459db0aebc96aeb807ea78da5d8714b1213e6f7)
- [bt_map_status_ind](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gabd4c099cc62671f53edec84eb04c50ff)
- [BT_MAP_STATUS_IND_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabd4c099cc62671f53edec84eb04c50ffa64afbc9334b9ee926b11dd473d70e0aa)
- [BT_MAP_STATUS_IND_DELETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabd4c099cc62671f53edec84eb04c50ffad1adaa8853f8bca4f4d21b378caeaf19)
- [BT_MAP_STATUS_IND_EXTENDED_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabd4c099cc62671f53edec84eb04c50ffaf9dd6096a95f6f75140d2d37d12e24b3)
- [bt_map_status_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga7af9d1e4244a00f8d2ae607f590fea94)
- [BT_MAP_STATUS_VAL_NO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7af9d1e4244a00f8d2ae607f590fea94a28da6d9711231be9117aec9feb9104f4)
- [BT_MAP_STATUS_VAL_YES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7af9d1e4244a00f8d2ae607f590fea94af5d7d30b5e5d6f0e8a4dd5ae42104bf8)
- [bt_map_presence](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga9523beb219a00ac4e6dba3e021b491d4)
- [BT_MAP_PRESENCE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a9a458e69d88a1f2c3be14c4c69c99b39)
- [BT_MAP_PRESENCE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a4affc47380cbcbbfcb819092d9c5cfd5)
- [BT_MAP_PRESENCE_ONLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4ade1acc46b57740b9c113cdf4ea8a502f)
- [BT_MAP_PRESENCE_AWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a98e509fe029643bb5f281b9274c70583)
- [BT_MAP_PRESENCE_DO_NOT_DISTURB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a3c1a5486acfe0d06fa935f34c5bf0d1c)
- [BT_MAP_PRESENCE_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4afc2b4a0338e768d25f200efe3c14081a)
- [BT_MAP_PRESENCE_IN_A_MEETING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a4d4a9258001731ffb4ea74d807394050)
- [bt_map_chat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gace38e2a78aaba1e2c48572e0d247e68c)
- [BT_MAP_CHAT_STATE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68cad9c127c32a580302536aa13cddd52085)
- [BT_MAP_CHAT_STATE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca179f10a2a6dd6184f4604794f2bb170f)
- [BT_MAP_CHAT_STATE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca1bb84095702eb5c6263a6ee908a6d1c6)
- [BT_MAP_CHAT_STATE_COMPOSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca95cb2a4eb0e6d8d2f2dd9f03a3c7c720)
- [BT_MAP_CHAT_STATE_PAUSED_COMPOSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68cacfffcf3cef8adddd1e1768fda9cdcf6d)
- [BT_MAP_CHAT_STATE_GONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca496b9d0393213a460a0b0bd2c8e4ba33)
- [bt_map_ntf_filter_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5acd8d8cfc6358140438860067970e2b)
- [BT_MAP_NTF_FILTER_MASK_NEW_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba77669e589a872268da67098ef008f3eb)
- [BT_MAP_NTF_FILTER_MASK_MSG_DELETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba88aa3bd1aeac147410ae96e8c7de43f9)
- [BT_MAP_NTF_FILTER_MASK_MSG_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2bad0ef68fc6a11e2429f67e1d6564597ef)
- [BT_MAP_NTF_FILTER_MASK_SENDING_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba5e21b8db192673e5b6e3146ed5b04dba)
- [BT_MAP_NTF_FILTER_MASK_SENDING_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba47d696ec191c6a0463ce70d5742616ad)
- [BT_MAP_NTF_FILTER_MASK_DELIVERY_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2baf34804c0b883c1a172c92ba237e05817)
- [BT_MAP_NTF_FILTER_MASK_DELIVERY_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2baa8e1626a89d2824b2fa3d6723a3a45cd)
- [BT_MAP_NTF_FILTER_MASK_MEM_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba83158a4308e7e89422541f2120e9baeb)
- [BT_MAP_NTF_FILTER_MASK_MEM_AVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2baa869867c70b17e91f726f27c6cbcacda)
- [BT_MAP_NTF_FILTER_MASK_READ_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2bab1a7d0518b5555eb63fb7ecee7e43bc9)
- [BT_MAP_NTF_FILTER_MASK_CONVO_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba8394516a5a3f2cc43b5facc1a39d29d4)
- [BT_MAP_NTF_FILTER_MASK_PARTICIPANT_PRESENCE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba9775c436fbf2f2211daea1b08f2a03e1)
- [BT_MAP_NTF_FILTER_MASK_PARTICIPANT_CHAT_STATE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba3802bd6debad36401e16092e5837f382)
- [BT_MAP_NTF_FILTER_MASK_MSG_EXT_DATA_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2bae685c7a86ab34c48a1e36ef7c5a3c9de)
- [BT_MAP_NTF_FILTER_MASK_MSG_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba169927e375629a179d5326d9db81c6f1)
- [bt_map_convo_param_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5f8e52ddea4d8e70373306c11e0bc7cf)
- [BT_MAP_CONVO_PARAM_MASK_CONVO_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa8bdec6724248fb7c9c03dfc68a74685d)
- [BT_MAP_CONVO_PARAM_MASK_CONVO_LAST_ACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfaa09c318962d5b45ec38803e76bdde12f)
- [BT_MAP_CONVO_PARAM_MASK_READ_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa219e72e5bda08cfc385be812c758e643)
- [BT_MAP_CONVO_PARAM_MASK_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa59c95bdc52ee0322073f77dd0e105793)
- [BT_MAP_CONVO_PARAM_MASK_SUMMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfadb591e1a00ec2aa5769da57ad9fee449)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa46cefe87f4e615449d6c455f7fb46ff6)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_UCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfafa05e0c6bd1e94c084c38576351e7aa1)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_DISP_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa4a6ee544171c8b462b67e06ac83f1f82)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_CHAT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa86c6406f1611ab59bec605c453e4de83)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_LAST_ACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa5dc039eda9209a6d0e2fde493be3e539)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_X_BT_UID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa3c2987c761d5b59e8dc2e32f86f2385b)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa2719dcdd029ab08b613199779d03ffb4)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRESENCE_AVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfaf249580f9df1595dfafe8ac26544c1cf)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRESENCE_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa99d249a960b62ff69f4f2a1a13709d3a)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa5d27a1c447d9f5a1b6c52b86915355c8)
- [bt_map_msg_ext_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga2fdf1a6a310fec131555fbdc62c524a2)
- [BT_MAP_MSG_EXT_DATA_FACEBOOK_LIKES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2abced9c6dcd9d3e6b11c2c73e7480a202)
- [BT_MAP_MSG_EXT_DATA_TWITTER_FOLLOWERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2a5ad011cef696acfa77ff9d36c80c727a)
- [BT_MAP_MSG_EXT_DATA_TWITTER_RETWEETS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2a0aecdd208590887c87b783b9b42730e7)
- [BT_MAP_MSG_EXT_DATA_GOOGLE_1S](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2a1e746d528718d93d50dba7770e6d128c)
- [bt_map_modify_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gaef50be9a23daf42f669fde9e067b18f3)
- [BT_MAP_MODIFY_TEXT_REPLACE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggaef50be9a23daf42f669fde9e067b18f3a8c6316a42d350cd845a68110708a146e)
- [BT_MAP_MODIFY_TEXT_PREPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggaef50be9a23daf42f669fde9e067b18f3a219ffe5a4584dd6eb7fdc6150389cf4c)
- [bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)
- [bt_map_mce_mas_cb](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md)
- [rfcomm_connected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a2c1255b9c721c844222a98e8ab5c5301)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [rfcomm_disconnected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a3f245b9e735bca51f16b579dea049b71)
- [l2cap_connected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a6a5a53dd82f8f7ddce0fadc4284d9ebe)
- [l2cap_disconnected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#abb01bd4ee41818a5c11de09035255ad5)
- [connect](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a41ff659151ea8d312ed178907005c9fa)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [disconnect](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#adebef477e23b2534fb7f54665338b0e2)
- [abort](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#adea73e4018513fe3f5443e2a4c3450dd)
- [set_ntf_reg](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a283872e83a71cc79e20c51fb1312b898)
- [set_folder](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a3554be8e90ec9605a0a2524cb37e2561)
- [get_folder_listing](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aca7392666d7b4ca34c38654ee8b37a63)
- [get_msg_listing](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#acdc05fac490ad32b5f197c673b46565f)
- [get_msg](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a42a9441ceab421f0ebd9accd8577ff05)
- [set_msg_status](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a1e11b4382657e6656b41058ba575d73d)
- [push_msg](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aabecb70ffb005db1048f8615712a358f)
- [update_inbox](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a51523325824c0add586e97e4fc45b985)
- [get_mas_inst_info](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a096e8d15124959cbbfa5c3961c44b55b)
- [set_owner_status](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aa74d509e4c1e792c1187aef27bfd5e8b)
- [get_owner_status](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aa491f3f467f93536d8dcdb7897552d9b)
- [get_convo_listing](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#adaebc7b993824d27757a9482e56a211e)
- [set_ntf_filter](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a15c281a0eb09f8e249b629c30d8909d2)
- [bt_goep_transport](../bluetooth_service_model_reference/P071_bt_goep_transport_结构体.md)
- [goep_transport](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md#a19563520b905384652950963fb3f8d65)
- [bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)
- [goep](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md#a546fc4ab58f8e8525f4030138db23911)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)
- [bt_map_mce_mas_rfcomm_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga04bf8d4d99165e7cf49613fe82432ca7)
- [bt_map_mce_mas_rfcomm_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga3202aee97828ecd8ed6f39f9eb6c98f2)
- [bt_map_mce_mas_l2cap_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga539c08b47cc73a23d24bd54dcb5d6dc4)
- [bt_map_mce_mas_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga1a00c2b646b9a10c3deb6f4953f04683)
- [bt_map_mce_mas_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga666d58fd65852372fa22328b6cd9aa82)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bt_map_mce_mas_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga01d1677204f204feb2474a61bfcc118a)
- [bt_map_mce_mas_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga0c58e5c7f70c15409ae9241d0b412400)
- [bt_map_mce_mas_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#gaf9836663a18ecc62b5330a1682f4b42e)
- [bt_map_mce_mas_set_folder](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga9e6640177b225a5b7448cde8a17de4f0)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_map_mce_mas_set_ntf_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#gad528c35977847525d781a39c50a3e793)
- [bt_map_mce_mas_get_folder_listing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga54fa7e185e5d949bec434935f51ae9fb)
- [bt_map_mce_mas_get_msg_listing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#gaf146e16f1b7950db4b5418bd27269ebb)
- [bt_map_mce_mas_get_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga39795b7002cf40984b130d38179a5472)
- [bt_map_mce_mas_set_msg_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#gaa03c3ea1d6ec10d02412b4525dd3ffe5)
- [bt_map_mce_mas_push_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga54a2552080933e12b6b871bc9f898fce)
- [bt_map_mce_mas_update_inbox](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#gae91fb531b7164b389994b9391fa8e51e)
- [bt_map_mce_mas_get_mas_inst_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#gabbe39f067872a6c008269d483a97d234)
- [bt_map_mce_mas_set_owner_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga3b1dc36240679618c98df515a351a5e7)
- [bt_map_mce_mas_get_owner_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga2206f238364c04e180153c5cff10de94)
- [bt_map_mce_mas_get_convo_listing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#gabdd72751375fa9a0aa1f99e75137cb9e)
- [bt_map_mce_mas_set_ntf_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mas.html#ga28b33d6c38af9479e56e9c2c2c0f795a)
- [bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)
- [bt_map_mce_mns_rfcomm_server](../bluetooth_service_model_reference/P112_bt_map_mce_mns_rfcomm_server_结构体.md)
- [bt_goep_transport_rfcomm_server](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md)
- [server](../bluetooth_service_model_reference/P112_bt_map_mce_mns_rfcomm_server_结构体.md#ac26fdeafe3edd7f811bdd3f0a53365fa)
- [accept](../bluetooth_service_model_reference/P112_bt_map_mce_mns_rfcomm_server_结构体.md#af17c8e6b2d833a8720dbfed64f2e505c)
- [bt_map_mce_mns_l2cap_server](../bluetooth_service_model_reference/P111_bt_map_mce_mns_l2cap_server_结构体.md)
- [bt_goep_transport_l2cap_server](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md)
- [server](../bluetooth_service_model_reference/P111_bt_map_mce_mns_l2cap_server_结构体.md#a53b201ac19eaced621ef2c3297e89392)
- [accept](../bluetooth_service_model_reference/P111_bt_map_mce_mns_l2cap_server_结构体.md#afb98a55954ef0892f107a5920aa5ad2c)
- [bt_map_mce_mns_cb](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md)
- [rfcomm_connected](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#a5b17ed8a8dcdf149924816fa07e4ff29)
- [rfcomm_disconnected](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#ad516d3cc29bc6f32e9f24415cfb5c56d)
- [l2cap_connected](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#a25e17d9e4d775963aedfe4f1a337a4ee)
- [l2cap_disconnected](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#ad19cefcd45105bab829a427ab12f774b)
- [connect](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#ab3da25ab3b1d96914927e834e3ca45b6)
- [disconnect](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#a8e3c2515dce12a6bee185ae4ac38a4e7)
- [abort](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#aa27a21b8c6a0d088ad487f9b51c7dfc1)
- [send_event](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#a7266e0e0d00994af225efd63615e595d)
- [goep_transport](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md#a89d9f42721e0b5045120f4a7279e0ffb)
- [goep](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md#af403bfc88cdd300b27e96cacb477ba42)
- [bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)
- [bt_map_mce_mns_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#gabae24c99ada5dae44ca657ae96008a69)
- [bt_map_mce_mns_rfcomm_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#ga574790bc59c82d89010e61f535849a35)
- [bt_map_mce_mns_rfcomm_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#gac6fa0bcfbea7b9a2a258678f5a2b8503)
- [bt_map_mce_mns_l2cap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#ga904970bac58822ec5336ce2bab226300)
- [bt_map_mce_mns_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#gad4207d61fbe40c34e753132fc742aba3)
- [bt_map_mce_mns_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#ga029cb5034f7cbf059653c763e4c767c2)
- [bt_map_mce_mns_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#gaab9161c0524c74cb4b03938c26642f4a)
- [bt_map_mce_mns_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#ga14411f8c0e8ce90824d366d28d4a2d2e)
- [bt_map_mce_mns_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#ga7309e25833e6594dc0018afe8b0a403c)
- [bt_map_mce_mns_send_event](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mce__mns.html#ga3e181d1bd37877dd8abf47a541c4b98e)
- [bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)
- [bt_map_mse_mas_rfcomm_server](../bluetooth_service_model_reference/P116_bt_map_mse_mas_rfcomm_server_结构体.md)
- [server](../bluetooth_service_model_reference/P116_bt_map_mse_mas_rfcomm_server_结构体.md#ac3cc9b87f871e4bb2c188244e1c41fe0)
- [accept](../bluetooth_service_model_reference/P116_bt_map_mse_mas_rfcomm_server_结构体.md#a0890ac5bf7b837818c03af77ac64ff09)
- [bt_map_mse_mas_l2cap_server](../bluetooth_service_model_reference/P115_bt_map_mse_mas_l2cap_server_结构体.md)
- [server](../bluetooth_service_model_reference/P115_bt_map_mse_mas_l2cap_server_结构体.md#ac6ad1e9b0a106cc060d6269b20d4f9b7)
- [accept](../bluetooth_service_model_reference/P115_bt_map_mse_mas_l2cap_server_结构体.md#a79abbf43efffd58ebd330d003c375a7b)
- [bt_map_mse_mas_cb](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md)
- [rfcomm_connected](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a92d897fa7c8f9d9e42a5b8e18b25a7e1)
- [rfcomm_disconnected](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a462a2826086f8ebc40617752c463bf83)
- [l2cap_connected](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a5d5246c3d8e3a229fdd6d33f01d48e50)
- [l2cap_disconnected](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a32dfc15ce0c67ef9b68d43c51a685668)
- [connect](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a1fd7e912c55a267e303e347bdd419ebe)
- [disconnect](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a0192c32ce2e08af30ba8288025ae0b55)
- [abort](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a58392850c26d91c10a6ed35c7d41d6eb)
- [set_ntf_reg](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a6d0489d861546f5e9501ff6527df7d3f)
- [set_folder](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a06897a7617ee1f68f56c1b230f9f12e9)
- [get_folder_listing](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a1b37e5006775590e91731e873c0c4dc9)
- [get_msg_listing](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#ab3039d3b0e740e9eda1b3efd392916f8)
- [get_msg](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a47d93ccf18b704eaf8d0906e75b8ddff)
- [set_msg_status](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a5fc25a4ad534e3490297faabcd86f51e)
- [push_msg](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a3113a29c5a6e7ba149bad09449cb5da4)
- [update_inbox](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#aed0b3894512dc0e3b363d3dd98b3dfbf)
- [get_mas_inst_info](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a6aae3db4af23f0408f328cac2b9fbf14)
- [set_owner_status](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a5094efadea33ad701eaad813fe2bde50)
- [get_owner_status](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#af016d7689a8546612c73bd41cdec6e5a)
- [get_convo_listing](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#aff9b5da1a558e79eaa744677437e66cc)
- [set_ntf_filter](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a91407e120e3a312061c8431fd3bb48a7)
- [goep_transport](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md#ab024f8036f13c3a01154ea45fa7d11b6)
- [goep](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md#a07ef39faccf3fdfca8c59d4076c99885)
- [bt_map_mse_mas_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga14815828dbf7163ab8fb0b3a8c0165b4)
- [bt_map_mse_mas_rfcomm_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga670bebf0edd1e8d5f7a2de5403e042d0)
- [bt_map_mse_mas_rfcomm_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga7db0773e3e0425f77e965fece30c3697)
- [bt_map_mse_mas_l2cap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga031515fbb0ca110532f5a1e971a01739)
- [bt_map_mse_mas_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga6df473fe69d8b3d183ee8385613f786f)
- [bt_map_mse_mas_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gab1c7678b39dad5309efde0b5950a997f)
- [bt_map_mse_mas_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gadd1da4acdd8043aa542c0fe36259898f)
- [bt_map_mse_mas_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gabc3a8d9eb9dbc3fd028d39e4a262388b)
- [bt_map_mse_mas_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga3eee467070483854e1a84a940ee031e2)
- [bt_map_mse_mas_set_folder](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gac972589b96cd3931044f994d4c94cf20)
- [bt_map_mse_mas_set_ntf_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga55641e8681932d0e31021d3803625874)
- [bt_map_mse_mas_get_folder_listing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga8263ea5145edcfd277f73980a3fcea57)
- [bt_map_mse_mas_get_msg_listing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga2833ef99d384109acf304532d1820a36)
- [bt_map_mse_mas_get_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga852ae34e4f8b44fea3308a42baa15ec2)
- [bt_map_mse_mas_set_msg_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga3cfbf0a8f1f1b6a730c401dac21e9f51)
- [bt_map_mse_mas_push_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gabcd127dc45e03820079be0dc92066b89)
- [bt_map_mse_mas_update_inbox](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga2c0ed0fdc8fee3f98e671c5ec187c8ed)
- [bt_map_mse_mas_get_mas_inst_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gab50e3d126e2d35e9b6724cf3112d0892)
- [bt_map_mse_mas_set_owner_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga275eff320f980230d8d80873ad0ef3ce)
- [bt_map_mse_mas_get_owner_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga37c155889cd0e2bb902da2bd25415509)
- [bt_map_mse_mas_get_convo_listing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#gadeb8072cdca241b3ad15c2116733d155)
- [bt_map_mse_mas_set_ntf_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mas.html#ga3aacf3e78b40f06bbf17baada2c59e04)
- [bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)
- [bt_map_mse_mns_cb](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md)
- [rfcomm_connected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#acbaddcaff6e7b5a4cedaccad97186dc4)
- [rfcomm_disconnected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a8cc8665110f38287951012307ce8837b)
- [l2cap_connected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a62f7d9e4661fce6976650c3d90245dc8)
- [l2cap_disconnected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#abcf2bc6750a60d66cf9999d542d0c8c2)
- [connect](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#aac533d7aa478d0645a1853de8a5fd354)
- [disconnect](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a2afd0b35998943c07584a70fa6a6107a)
- [abort](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a168facdd5cdcc695814e4e9dd517f807)
- [send_event](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#ab38e352b61b54a9961f200c9cf30e5b8)
- [goep_transport](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md#a524c23c6e1513bb641b103cb8fde37cb)
- [goep](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md#a6815c3c6af06b8cf618e9cf83fead584)
- [bt_map_mse_mns_rfcomm_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html#gadf2f434d2565703781a46851d4444a80)
- [bt_map_mse_mns_rfcomm_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html#ga0513491439278cadc6897f9cb932cd67)
- [bt_map_mse_mns_l2cap_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html#ga46fc48dafd5c173199274be1a616a109)
- [bt_map_mse_mns_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html#ga305dd055de4831ef68cff7b5346a4b5d)
- [bt_map_mse_mns_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html#gaa0298eb521d012a910eba4a552d55fa7)
- [bt_map_mse_mns_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html#ga7bedc538a126b8c4d4c6fb393fc06218)
- [bt_map_mse_mns_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html#ga08513e5aa2b54e4474ee647232c0af91)
- [bt_map_mse_mns_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html#gafc1be36425faa6242ed8eb4f21d76b5f)
- [bt_map_mse_mns_send_event](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map__mse__mns.html#gac8776edbbf4e2f891246cba86a1df589)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)
- [bt_map_mce_mas_cb::get_mas_inst_info](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a096e8d15124959cbbfa5c3961c44b55b)
- [bt_map_mce_mas_cb::set_ntf_filter](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a15c281a0eb09f8e249b629c30d8909d2)
- [bt_map_mce_mas_cb::set_msg_status](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a1e11b4382657e6656b41058ba575d73d)
- [bt_map_mce_mas_cb::set_ntf_reg](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a283872e83a71cc79e20c51fb1312b898)
- [bt_map_mce_mas_cb::rfcomm_connected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a2c1255b9c721c844222a98e8ab5c5301)
- [bt_map_mce_mas_cb::set_folder](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a3554be8e90ec9605a0a2524cb37e2561)
- [bt_map_mce_mas_cb::rfcomm_disconnected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a3f245b9e735bca51f16b579dea049b71)
- [bt_map_mce_mas_cb::connect](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a41ff659151ea8d312ed178907005c9fa)
- [bt_map_mce_mas_cb::get_msg](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a42a9441ceab421f0ebd9accd8577ff05)
- [bt_map_mce_mas_cb::update_inbox](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a51523325824c0add586e97e4fc45b985)
- [bt_map_mce_mas_cb::l2cap_connected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#a6a5a53dd82f8f7ddce0fadc4284d9ebe)
- [bt_map_mce_mas_cb::get_owner_status](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aa491f3f467f93536d8dcdb7897552d9b)
- [bt_map_mce_mas_cb::set_owner_status](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aa74d509e4c1e792c1187aef27bfd5e8b)
- [bt_map_mce_mas_cb::push_msg](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aabecb70ffb005db1048f8615712a358f)
- [bt_map_mce_mas_cb::l2cap_disconnected](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#abb01bd4ee41818a5c11de09035255ad5)
- [bt_map_mce_mas_cb::get_folder_listing](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#aca7392666d7b4ca34c38654ee8b37a63)
- [bt_map_mce_mas_cb::get_msg_listing](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#acdc05fac490ad32b5f197c673b46565f)
- [bt_map_mce_mas_cb::get_convo_listing](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#adaebc7b993824d27757a9482e56a211e)
- [bt_map_mce_mas_cb::abort](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#adea73e4018513fe3f5443e2a4c3450dd)
- [bt_map_mce_mas_cb::disconnect](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md#adebef477e23b2534fb7f54665338b0e2)
- [bt_map_mce_mas::goep_transport](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md#a19563520b905384652950963fb3f8d65)
- [bt_map_mce_mas::goep](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md#a546fc4ab58f8e8525f4030138db23911)
- [bt_map_mce_mns_cb::l2cap_connected](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#a25e17d9e4d775963aedfe4f1a337a4ee)
- [bt_map_mce_mns_cb::rfcomm_connected](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#a5b17ed8a8dcdf149924816fa07e4ff29)
- [bt_map_mce_mns_cb::send_event](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#a7266e0e0d00994af225efd63615e595d)
- [bt_map_mce_mns_cb::disconnect](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#a8e3c2515dce12a6bee185ae4ac38a4e7)
- [bt_map_mce_mns_cb::abort](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#aa27a21b8c6a0d088ad487f9b51c7dfc1)
- [bt_map_mce_mns_cb::connect](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#ab3da25ab3b1d96914927e834e3ca45b6)
- [bt_map_mce_mns_cb::l2cap_disconnected](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#ad19cefcd45105bab829a427ab12f774b)
- [bt_map_mce_mns_cb::rfcomm_disconnected](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md#ad516d3cc29bc6f32e9f24415cfb5c56d)
- [bt_map_mce_mns_l2cap_server::server](../bluetooth_service_model_reference/P111_bt_map_mce_mns_l2cap_server_结构体.md#a53b201ac19eaced621ef2c3297e89392)
- [bt_map_mce_mns_l2cap_server::accept](../bluetooth_service_model_reference/P111_bt_map_mce_mns_l2cap_server_结构体.md#afb98a55954ef0892f107a5920aa5ad2c)
- [bt_map_mce_mns_rfcomm_server::server](../bluetooth_service_model_reference/P112_bt_map_mce_mns_rfcomm_server_结构体.md#ac26fdeafe3edd7f811bdd3f0a53365fa)
- [bt_map_mce_mns_rfcomm_server::accept](../bluetooth_service_model_reference/P112_bt_map_mce_mns_rfcomm_server_结构体.md#af17c8e6b2d833a8720dbfed64f2e505c)
- [bt_map_mce_mns::goep_transport](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md#a89d9f42721e0b5045120f4a7279e0ffb)
- [bt_map_mce_mns::goep](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md#af403bfc88cdd300b27e96cacb477ba42)
- [bt_map_mse_mas_cb::disconnect](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a0192c32ce2e08af30ba8288025ae0b55)
- [bt_map_mse_mas_cb::set_folder](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a06897a7617ee1f68f56c1b230f9f12e9)
- [bt_map_mse_mas_cb::get_folder_listing](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a1b37e5006775590e91731e873c0c4dc9)
- [bt_map_mse_mas_cb::connect](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a1fd7e912c55a267e303e347bdd419ebe)
- [bt_map_mse_mas_cb::push_msg](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a3113a29c5a6e7ba149bad09449cb5da4)
- [bt_map_mse_mas_cb::l2cap_disconnected](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a32dfc15ce0c67ef9b68d43c51a685668)
- [bt_map_mse_mas_cb::rfcomm_disconnected](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a462a2826086f8ebc40617752c463bf83)
- [bt_map_mse_mas_cb::get_msg](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a47d93ccf18b704eaf8d0906e75b8ddff)
- [bt_map_mse_mas_cb::set_owner_status](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a5094efadea33ad701eaad813fe2bde50)
- [bt_map_mse_mas_cb::abort](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a58392850c26d91c10a6ed35c7d41d6eb)
- [bt_map_mse_mas_cb::l2cap_connected](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a5d5246c3d8e3a229fdd6d33f01d48e50)
- [bt_map_mse_mas_cb::set_msg_status](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a5fc25a4ad534e3490297faabcd86f51e)
- [bt_map_mse_mas_cb::get_mas_inst_info](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a6aae3db4af23f0408f328cac2b9fbf14)
- [bt_map_mse_mas_cb::set_ntf_reg](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a6d0489d861546f5e9501ff6527df7d3f)
- [bt_map_mse_mas_cb::set_ntf_filter](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a91407e120e3a312061c8431fd3bb48a7)
- [bt_map_mse_mas_cb::rfcomm_connected](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#a92d897fa7c8f9d9e42a5b8e18b25a7e1)
- [bt_map_mse_mas_cb::get_msg_listing](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#ab3039d3b0e740e9eda1b3efd392916f8)
- [bt_map_mse_mas_cb::update_inbox](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#aed0b3894512dc0e3b363d3dd98b3dfbf)
- [bt_map_mse_mas_cb::get_owner_status](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#af016d7689a8546612c73bd41cdec6e5a)
- [bt_map_mse_mas_cb::get_convo_listing](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md#aff9b5da1a558e79eaa744677437e66cc)
- [bt_map_mse_mas_l2cap_server::accept](../bluetooth_service_model_reference/P115_bt_map_mse_mas_l2cap_server_结构体.md#a79abbf43efffd58ebd330d003c375a7b)
- [bt_map_mse_mas_l2cap_server::server](../bluetooth_service_model_reference/P115_bt_map_mse_mas_l2cap_server_结构体.md#ac6ad1e9b0a106cc060d6269b20d4f9b7)
- [bt_map_mse_mas_rfcomm_server::accept](../bluetooth_service_model_reference/P116_bt_map_mse_mas_rfcomm_server_结构体.md#a0890ac5bf7b837818c03af77ac64ff09)
- [bt_map_mse_mas_rfcomm_server::server](../bluetooth_service_model_reference/P116_bt_map_mse_mas_rfcomm_server_结构体.md#ac3cc9b87f871e4bb2c188244e1c41fe0)
- [bt_map_mse_mas::goep](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md#a07ef39faccf3fdfca8c59d4076c99885)
- [bt_map_mse_mas::goep_transport](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md#ab024f8036f13c3a01154ea45fa7d11b6)
- [bt_map_mse_mns_cb::abort](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a168facdd5cdcc695814e4e9dd517f807)
- [bt_map_mse_mns_cb::disconnect](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a2afd0b35998943c07584a70fa6a6107a)
- [bt_map_mse_mns_cb::l2cap_connected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a62f7d9e4661fce6976650c3d90245dc8)
- [bt_map_mse_mns_cb::rfcomm_disconnected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#a8cc8665110f38287951012307ce8837b)
- [bt_map_mse_mns_cb::connect](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#aac533d7aa478d0645a1853de8a5fd354)
- [bt_map_mse_mns_cb::send_event](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#ab38e352b61b54a9961f200c9cf30e5b8)
- [bt_map_mse_mns_cb::l2cap_disconnected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#abcf2bc6750a60d66cf9999d542d0c8c2)
- [bt_map_mse_mns_cb::rfcomm_connected](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md#acbaddcaff6e7b5a4cedaccad97186dc4)
- [bt_map_mse_mns::goep_transport](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md#a524c23c6e1513bb641b103cb8fde37cb)
- [bt_map_mse_mns::goep](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md#a6815c3c6af06b8cf618e9cf83fead584)

---

[上一章](P001_bap_lc3_preset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_clock_control_bflb_common.h_源码浏览.md)
