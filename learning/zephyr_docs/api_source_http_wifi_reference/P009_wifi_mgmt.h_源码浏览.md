---
id: learning.zephyr-docs.api-source-http-wifi-reference.page-9
title: wifi_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_wifi\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h.html)。

## 9.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
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
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
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
<a id="l00075"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="foldopen00162"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="foldopen00168"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="foldopen00174"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="foldopen00180"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="foldopen00186"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="foldopen00192"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="foldopen00198"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="foldopen00204"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="foldopen00210"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="foldopen00216"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="foldopen00222"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="foldopen00228"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="foldopen00234"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="foldopen00240"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="foldopen00246"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="foldopen00252"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="foldopen00258"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="foldopen00264"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="foldopen00270"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="foldopen00276"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="foldopen00282"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="foldopen00294"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="foldopen00321"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="foldopen00327"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="foldopen00333"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
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
<a id="foldopen00355"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="foldopen00361"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="foldopen00367"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="foldopen00373"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
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
<a id="l00412"></a>
<a id="foldopen00414"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00420"></a>
<a id="l00422"></a>
<a id="l00424"></a>
<a id="l00426"></a>
<a id="l00430"></a>
<a id="l00432"></a>
<a id="l00434"></a>
<a id="l00436"></a>
<a id="l00438"></a>
<a id="l00440"></a>
<a id="l00442"></a>
<a id="l00444"></a>
<a id="l00446"></a>
<a id="l00448"></a>
<a id="l00450"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00455"></a>
<a id="l00457"></a>
<a id="l00459"></a>
<a id="l00461"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="foldopen00468"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="foldopen00472"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="foldopen00476"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="foldopen00480"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="foldopen00484"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="foldopen00488"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="foldopen00492"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="foldopen00496"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="foldopen00500"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="foldopen00504"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="foldopen00508"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="foldopen00512"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="foldopen00516"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="foldopen00520"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="foldopen00524"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="foldopen00528"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="l00535"></a>
<a id="l00537"></a>
<a id="l00539"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00546"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00552"></a>
<a id="l00554"></a>
<a id="l00556"></a>
<a id="l00558"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00564"></a>
<a id="l00566"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="foldopen00595"></a>
<a id="l00595"></a>
<a id="l00597"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="foldopen00605"></a>
<a id="l00605"></a>
<a id="l00607"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="foldopen00617"></a>
<a id="l00617"></a>
<a id="l00625"></a>
<a id="l00629"></a>
<a id="l00632"></a>
<a id="l00635"></a>
<a id="l00638"></a>
<a id="l00646"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="foldopen00667"></a>
<a id="l00667"></a>
<a id="l00669"></a>
<a id="l00671"></a>
<a id="l00673"></a>
<a id="l00675"></a>
<a id="l00677"></a>
<a id="l00679"></a>
<a id="l00681"></a>
<a id="l00683"></a>
<a id="l00685"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="foldopen00691"></a>
<a id="l00691"></a>
<a id="l00693"></a>
<a id="l00695"></a>
<a id="l00697"></a>
<a id="l00699"></a>
<a id="l00705"></a>
<a id="l00707"></a>
<a id="l00709"></a>
<a id="l00711"></a>
<a id="l00713"></a>
<a id="l00715"></a>
<a id="l00717"></a>
<a id="l00719"></a>
<a id="l00721"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00847"></a>
<a id="l00853"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="l00858"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00863"></a>
<a id="l00865"></a>
<a id="l00870"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="foldopen00885"></a>
<a id="l00885"></a>
<a id="l00887"></a>
<a id="l00889"></a>
<a id="l00891"></a>
<a id="l00893"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="foldopen00904"></a>
<a id="l00904"></a>
<a id="l00906"></a>
<a id="l00908"></a>
<a id="l00910"></a>
<a id="l00912"></a>
<a id="l00914"></a>
<a id="l00916"></a>
<a id="l00918"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="foldopen00924"></a>
<a id="l00924"></a>
<a id="l00926"></a>
<a id="l00928"></a>
<a id="l00930"></a>
<a id="l00932"></a>
<a id="l00934"></a>
<a id="l00935"></a>
<a id="l00939"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="foldopen00947"></a>
<a id="l00947"></a>
<a id="l00949"></a>
<a id="l00951"></a>
<a id="l00953"></a>
<a id="l00955"></a>
<a id="l00957"></a>
<a id="l00959"></a>
<a id="l00961"></a>
<a id="l00963"></a>
<a id="l00965"></a>
<a id="l00967"></a>
<a id="l00969"></a>
<a id="l00971"></a>
<a id="l00973"></a>
<a id="l00975"></a>
<a id="l00977"></a>
<a id="l00979"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="foldopen00985"></a>
<a id="l00985"></a>
<a id="l00987"></a>
<a id="l00989"></a>
<a id="l00991"></a>
<a id="l00993"></a>
<a id="l01002"></a>
<a id="l01004"></a>
<a id="l01006"></a>
<a id="l01008"></a>
<a id="l01009"></a>
<a id="l01010"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="foldopen01015"></a>
<a id="l01015"></a>
<a id="l01017"></a>
<a id="l01019"></a>
<a id="l01021"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="l01025"></a>
<a id="foldopen01027"></a>
<a id="l01027"></a>
<a id="l01029"></a>
<a id="l01031"></a>
<a id="l01033"></a>
<a id="l01035"></a>
<a id="l01037"></a>
<a id="l01039"></a>
<a id="l01041"></a>
<a id="l01043"></a>
<a id="l01045"></a>
<a id="l01047"></a>
<a id="l01049"></a>
<a id="l01051"></a>
<a id="l01053"></a>
<a id="l01055"></a>
<a id="l01057"></a>
<a id="l01063"></a>
<a id="l01065"></a>
<a id="l01067"></a>
<a id="l01069"></a>
<a id="l01070"></a>
<a id="l01072"></a>
<a id="l01074"></a>
<a id="l01076"></a>
<a id="l01078"></a>
<a id="l01080"></a>
<a id="l01082"></a>
<a id="l01083"></a>
<a id="l01085"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01089"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="l01093"></a>
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
<a id="l01109"></a>
<a id="foldopen01111"></a>
<a id="l01111"></a>
<a id="l01113"></a>
<a id="l01115"></a>
<a id="l01117"></a>
<a id="l01119"></a>
<a id="l01121"></a>
<a id="l01123"></a>
<a id="l01125"></a>
<a id="l01127"></a>
<a id="l01129"></a>
<a id="l01131"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="foldopen01135"></a>
<a id="l01135"></a>
<a id="l01137"></a>
<a id="l01139"></a>
<a id="l01141"></a>
<a id="l01143"></a>
<a id="l01145"></a>
<a id="l01147"></a>
<a id="l01149"></a>
<a id="l01151"></a>
<a id="l01153"></a>
<a id="l01155"></a>
<a id="l01157"></a>
<a id="l01159"></a>
<a id="l01161"></a>
<a id="l01163"></a>
<a id="l01165"></a>
<a id="l01167"></a>
<a id="l01169"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01173"></a>
<a id="foldopen01175"></a>
<a id="l01175"></a>
<a id="l01177"></a>
<a id="l01179"></a>
<a id="l01181"></a>
<a id="l01182"></a>
<a id="l01183"></a>
<a id="foldopen01185"></a>
<a id="l01185"></a>
<a id="l01187"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="l01191"></a>
<a id="foldopen01193"></a>
<a id="l01193"></a>
<a id="l01195"></a>
<a id="l01197"></a>
<a id="l01199"></a>
<a id="l01200"></a>
<a id="l01201"></a>
<a id="l01203"></a>
<a id="l01204"></a>
<a id="foldopen01206"></a>
<a id="l01206"></a>
<a id="l01208"></a>
<a id="l01210"></a>
<a id="l01212"></a>
<a id="l01214"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="foldopen01220"></a>
<a id="l01220"></a>
<a id="l01222"></a>
<a id="l01226"></a>
<a id="l01228"></a>
<a id="l01230"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="l01234"></a>
<a id="foldopen01236"></a>
<a id="l01236"></a>
<a id="l01238"></a>
<a id="l01240"></a>
<a id="l01241"></a>
<a id="l01242"></a>
<a id="l01243"></a>
<a id="foldopen01245"></a>
<a id="l01245"></a>
<a id="l01247"></a>
<a id="l01249"></a>
<a id="l01251"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="foldopen01258"></a>
<a id="l01258"></a>
<a id="l01260"></a>
<a id="l01262"></a>
<a id="l01264"></a>
<a id="l01266"></a>
<a id="l01267"></a>
<a id="l01268"></a>
<a id="l01269"></a>
<a id="l01271"></a>
<a id="l01273"></a>
<a id="l01275"></a>
<a id="l01277"></a>
<a id="l01279"></a>
<a id="l01281"></a>
<a id="l01283"></a>
<a id="l01285"></a>
<a id="l01287"></a>
<a id="l01288"></a>
<a id="l01289"></a>
<a id="l01291"></a>
<a id="l01293"></a>
<a id="l01295"></a>
<a id="l01297"></a>
<a id="l01299"></a>
<a id="l01301"></a>
<a id="l01303"></a>
<a id="l01304"></a>
<a id="l01305"></a>
<a id="l01307"></a>
<a id="l01309"></a>
<a id="l01311"></a>
<a id="l01312"></a>
<a id="l01313"></a>
<a id="l01315"></a>
<a id="l01317"></a>
<a id="l01319"></a>
<a id="l01321"></a>
<a id="l01323"></a>
<a id="l01325"></a>
<a id="l01326"></a>
<a id="l01327"></a>
<a id="l01328"></a>
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
<a id="l01354"></a>
<a id="foldopen01356"></a>
<a id="l01356"></a>
<a id="l01358"></a>
<a id="l01360"></a>
<a id="l01362"></a>
<a id="l01363"></a>
<a id="l01364"></a>
<a id="foldopen01366"></a>
<a id="l01366"></a>
<a id="l01368"></a>
<a id="l01370"></a>
<a id="l01372"></a>
<a id="l01374"></a>
<a id="l01375"></a>
<a id="l01376"></a>
<a id="foldopen01378"></a>
<a id="l01378"></a>
<a id="l01380"></a>
<a id="l01385"></a>
<a id="l01387"></a>
<a id="l01389"></a>
<a id="l01390"></a>
<a id="l01391"></a>
<a id="l01393"></a>
<a id="l01394"></a>
<a id="l01396"></a>
<a id="foldopen01398"></a>
<a id="l01398"></a>
<a id="l01400"></a>
<a id="l01402"></a>
<a id="l01404"></a>
<a id="l01406"></a>
<a id="l01407"></a>
<a id="l01409"></a>
<a id="l01411"></a>
<a id="l01412"></a>
<a id="l01413"></a>
<a id="l01414"></a>
<a id="foldopen01416"></a>
<a id="l01416"></a>
<a id="l01418"></a>
<a id="l01420"></a>
<a id="l01421"></a>
<a id="l01422"></a>
<a id="l01423"></a>
<a id="l01426"></a>
<a id="l01427"></a>
<a id="l01429"></a>
<a id="l01431"></a>
<a id="l01433"></a>
<a id="l01435"></a>
<a id="l01437"></a>
<a id="l01439"></a>
<a id="l01441"></a>
<a id="l01443"></a>
<a id="l01445"></a>
<a id="l01447"></a>
<a id="l01449"></a>
<a id="l01451"></a>
<a id="l01452"></a>
<a id="l01453"></a>
<a id="l01455"></a>
<a id="l01457"></a>
<a id="l01459"></a>
<a id="l01461"></a>
<a id="l01463"></a>
<a id="l01465"></a>
<a id="l01467"></a>
<a id="l01469"></a>
<a id="l01470"></a>
<a id="l01471"></a>
<a id="l01473"></a>
<a id="l01475"></a>
<a id="l01477"></a>
<a id="l01479"></a>
<a id="l01481"></a>
<a id="l01482"></a>
<a id="l01483"></a>
<a id="l01488"></a>
<a id="l01490"></a>
<a id="l01492"></a>
<a id="l01494"></a>
<a id="l01496"></a>
<a id="l01497"></a>
<a id="l01498"></a>
<a id="l01503"></a>
<a id="l01505"></a>
<a id="l01507"></a>
<a id="l01509"></a>
<a id="l01511"></a>
<a id="l01512"></a>
<a id="l01513"></a>
<a id="l01515"></a>
<a id="l01517"></a>
<a id="l01519"></a>
<a id="l01520"></a>
<a id="l01521"></a>
<a id="l01523"></a>
<a id="l01525"></a>
<a id="l01527"></a>
<a id="l01529"></a>
<a id="l01531"></a>
<a id="l01533"></a>
<a id="l01534"></a>
<a id="l01535"></a>
<a id="l01537"></a>
<a id="l01539"></a>
<a id="l01541"></a>
<a id="l01542"></a>
<a id="l01543"></a>
<a id="l01545"></a>
<a id="l01547"></a>
<a id="l01549"></a>
<a id="l01550"></a>
<a id="l01551"></a>
<a id="l01553"></a>
<a id="l01555"></a>
<a id="l01557"></a>
<a id="l01559"></a>
<a id="l01561"></a>
<a id="l01563"></a>
<a id="l01564"></a>
<a id="l01565"></a>
<a id="l01567"></a>
<a id="l01569"></a>
<a id="l01571"></a>
<a id="l01573"></a>
<a id="l01575"></a>
<a id="l01577"></a>
<a id="l01579"></a>
<a id="l01581"></a>
<a id="l01582"></a>
<a id="l01583"></a>
<a id="l01586"></a>
<a id="l01588"></a>
<a id="l01589"></a>
<a id="l01591"></a>
<a id="l01593"></a>
<a id="l01595"></a>
<a id="l01597"></a>
<a id="l01599"></a>
<a id="l01601"></a>
<a id="l01603"></a>
<a id="l01605"></a>
<a id="l01607"></a>
<a id="l01609"></a>
<a id="l01614"></a>
<a id="l01615"></a>
<a id="l01616"></a>
<a id="l01617"></a>
<a id="l01618"></a>
<a id="l01619"></a>
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
<a id="l01636"></a>
<a id="l01638"></a>
<a id="l01640"></a>
<a id="l01642"></a>
<a id="l01643"></a>
<a id="l01644"></a>
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
<a id="l01711"></a>
<a id="l01713"></a>
<a id="l01715"></a>
<a id="l01716"></a>
<a id="l01717"></a>
<a id="l01719"></a>
<a id="l01721"></a>
<a id="l01722"></a>
<a id="l01724"></a>
<a id="l01726"></a>
<a id="l01728"></a>
<a id="l01730"></a>
<a id="l01732"></a>
<a id="l01734"></a>
<a id="l01736"></a>
<a id="l01737"></a>
<a id="l01738"></a>
<a id="l01739"></a>
<a id="l01740"></a>
<a id="l01741"></a>
<a id="l01742"></a>
<a id="l01743"></a>
<a id="l01744"></a>
<a id="l01745"></a>
<a id="l01747"></a>
<a id="l01748"></a>
<a id="foldopen01750"></a>
<a id="l01750"></a>
<a id="l01752"></a>
<a id="l01754"></a>
<a id="l01756"></a>
<a id="l01757"></a>
<a id="l01758"></a>
<a id="foldopen01760"></a>
<a id="l01760"></a>
<a id="l01762"></a>
<a id="l01764"></a>
<a id="l01765"></a>
<a id="l01766"></a>
<a id="l01767"></a>
<a id="l01769"></a>
<a id="l01771"></a>
<a id="l01773"></a>
<a id="l01777"></a>
<a id="l01779"></a>
<a id="l01781"></a>
<a id="l01783"></a>
<a id="l01785"></a>
<a id="l01787"></a>
<a id="l01789"></a>
<a id="l01791"></a>
<a id="l01793"></a>
<a id="l01795"></a>
<a id="l01796"></a>
<a id="l01797"></a>
<a id="l01799"></a>
<a id="l01801"></a>
<a id="l01803"></a>
<a id="l01805"></a>
<a id="l01806"></a>
<a id="l01807"></a>
<a id="l01809"></a>
<a id="l01811"></a>
<a id="l01813"></a>
<a id="l01815"></a>
<a id="l01816"></a>
<a id="l01817"></a>
<a id="l01819"></a>
<a id="l01820"></a>
<a id="l01821"></a>
<a id="l01822"></a>
<a id="l01824"></a>
<a id="l01826"></a>
<a id="l01828"></a>
<a id="l01830"></a>
<a id="l01832"></a>
<a id="l01834"></a>
<a id="l01836"></a>
<a id="l01838"></a>
<a id="l01840"></a>
<a id="l01842"></a>
<a id="l01844"></a>
<a id="l01846"></a>
<a id="l01851"></a>
<a id="l01853"></a>
<a id="l01855"></a>
<a id="l01857"></a>
<a id="l01859"></a>
<a id="l01860"></a>
<a id="l01862"></a>
<a id="l01864"></a>
<a id="l01866"></a>
<a id="l01868"></a>
<a id="l01870"></a>
<a id="l01872"></a>
<a id="l01874"></a>
<a id="l01876"></a>
<a id="l01878"></a>
<a id="l01880"></a>
<a id="l01881"></a>
<a id="l01883"></a>
<a id="l01885"></a>
<a id="l01886"></a>
<a id="l01888"></a>
<a id="l01890"></a>
<a id="l01891"></a>
<a id="l01892"></a>
<a id="l01893"></a>
<a id="l01895"></a>
<a id="l01897"></a>
<a id="l01899"></a>
<a id="l01901"></a>
<a id="l01903"></a>
<a id="l01905"></a>
<a id="l01906"></a>
<a id="l01908"></a>
<a id="l01910"></a>
<a id="l01912"></a>
<a id="l01913"></a>
<a id="l01915"></a>
<a id="l01920"></a>
<a id="l01921"></a>
<a id="l01923"></a>
<a id="l01925"></a>
<a id="l01927"></a>
<a id="l01928"></a>
<a id="l01929"></a>
<a id="l01930"></a>
<a id="l01931"></a>
<a id="foldopen01934"></a>
<a id="l01934"></a>
<a id="l01936"></a>
<a id="l01938"></a>
<a id="l01940"></a>
<a id="l01942"></a>
<a id="l01944"></a>
<a id="l01946"></a>
<a id="l01948"></a>
<a id="l01950"></a>
<a id="l01951"></a>
<a id="l01952"></a>
<a id="l01953"></a>
<a id="foldopen01955"></a>
<a id="l01955"></a>
<a id="l01957"></a>
<a id="l01959"></a>
<a id="l01961"></a>
<a id="l01962"></a>
<a id="l01963"></a>
<a id="foldopen01965"></a>
<a id="l01965"></a>
<a id="l01967"></a>
<a id="l01969"></a>
<a id="l01971"></a>
<a id="l01973"></a>
<a id="l01975"></a>
<a id="l01976"></a>
<a id="l01977"></a>
<a id="l01978"></a>
<a id="foldopen01980"></a>
<a id="l01980"></a>
<a id="l01982"></a>
<a id="l01984"></a>
<a id="l01986"></a>
<a id="l01988"></a>
<a id="l01990"></a>
<a id="l01991"></a>
<a id="l01992"></a>
<a id="l01993"></a>
<a id="l01994"></a>
<a id="l02001"></a>
<a id="l02002"></a>
<a id="l02003"></a>
<a id="l02004"></a>
<a id="l02011"></a>
<a id="l02012"></a>
<a id="l02013"></a>
<a id="l02014"></a>
<a id="foldopen02016"></a>
<a id="l02016"></a>
<a id="l02029"></a>
<a id="l02030"></a>
<a id="l02031"></a>
<a id="l02032"></a>
<a id="l02041"></a>
<a id="l02042"></a>
<a id="l02043"></a>
<a id="l02051"></a>
<a id="l02052"></a>
<a id="l02061"></a>
<a id="l02062"></a>
<a id="l02063"></a>
<a id="l02070"></a>
<a id="l02079"></a>
<a id="l02080"></a>
<a id="l02089"></a>
<a id="l02090"></a>
<a id="l02091"></a>
<a id="l02092"></a>
<a id="l02101"></a>
<a id="l02102"></a>
<a id="l02103"></a>
<a id="l02111"></a>
<a id="l02112"></a>
<a id="l02121"></a>
<a id="l02122"></a>
<a id="l02123"></a>
<a id="l02132"></a>
<a id="l02133"></a>
<a id="l02134"></a>
<a id="l02143"></a>
<a id="l02144"></a>
<a id="l02145"></a>
<a id="l02154"></a>
<a id="l02155"></a>
<a id="l02156"></a>
<a id="l02165"></a>
<a id="l02166"></a>
<a id="l02167"></a>
<a id="l02176"></a>
<a id="l02177"></a>
<a id="l02178"></a>
<a id="l02187"></a>
<a id="l02188"></a>
<a id="l02189"></a>
<a id="l02198"></a>
<a id="l02199"></a>
<a id="l02200"></a>
<a id="l02209"></a>
<a id="l02218"></a>
<a id="l02219"></a>
<a id="l02220"></a>
<a id="l02221"></a>
<a id="l02230"></a>
<a id="l02231"></a>
<a id="l02238"></a>
<a id="l02239"></a>
<a id="l02248"></a>
<a id="l02249"></a>
<a id="l02257"></a>
<a id="l02258"></a>
<a id="l02272"></a>
<a id="l02273"></a>
<a id="l02274"></a>
<a id="l02283"></a>
<a id="l02284"></a>
<a id="l02285"></a>
<a id="l02294"></a>
<a id="l02295"></a>
<a id="l02296"></a>
<a id="l02305"></a>
<a id="l02306"></a>
<a id="l02307"></a>
<a id="l02316"></a>
<a id="l02317"></a>
<a id="l02318"></a>
<a id="l02319"></a>
<a id="l02328"></a>
<a id="l02329"></a>
<a id="l02330"></a>
<a id="l02331"></a>
<a id="l02332"></a>
<a id="l02341"></a>
<a id="l02342"></a>
<a id="l02343"></a>
<a id="l02344"></a>
<a id="l02345"></a>
<a id="l02353"></a>
<a id="l02362"></a>
<a id="l02363"></a>
<a id="l02364"></a>
<a id="l02365"></a>
<a id="l02366"></a>
<a id="l02375"></a>
<a id="l02376"></a>
<a id="l02377"></a>
<a id="l02386"></a>
<a id="l02387"></a>
<a id="l02388"></a>
<a id="l02397"></a>
<a id="l02398"></a>
<a id="l02399"></a>
<a id="l02409"></a>
<a id="l02418"></a>
<a id="l02419"></a>
<a id="l02420"></a>
<a id="l02421"></a>
<a id="l02430"></a>
<a id="l02431"></a>
<a id="l02432"></a>
<a id="l02433"></a>
<a id="l02434"></a>
<a id="l02444"></a>
<a id="l02445"></a>
<a id="l02446"></a>
<a id="l02447"></a>
<a id="l02459"></a>
<a id="l02460"></a>
<a id="l02461"></a>
<a id="foldopen02463"></a>
<a id="l02463"></a>
<a id="l02470"></a>
<a id="l02472"></a>
<a id="l02473"></a>
<a id="l02475"></a>
<a id="l02476"></a>
<a id="l02478"></a>
<a id="l02479"></a>
<a id="l02480"></a>
<a id="l02482"></a>
<a id="l02483"></a>
<a id="l02484"></a>
<a id="l02485"></a>
<a id="l02486"></a>
<a id="l02487"></a>
<a id="l02488"></a>
<a id="l02489"></a>
<a id="l02490"></a>
<a id="l02491"></a>
<a id="l02492"></a>
<a id="l02493"></a>
<a id="l02494"></a>
<a id="l02495"></a>
<a id="l02496"></a>
<a id="l02502"></a>
<a id="l02503"></a>
<a id="l02512"></a>
<a id="l02513"></a>
<a id="l02514"></a>
<a id="l02520"></a>
<a id="l02521"></a>
<a id="l02530"></a>
<a id="l02531"></a>
<a id="l02532"></a>
<a id="l02538"></a>
<a id="l02539"></a>
<a id="l02540"></a>
<a id="l02546"></a>
<a id="l02547"></a>
<a id="l02548"></a>
<a id="l02554"></a>
<a id="l02555"></a>
<a id="l02556"></a>
<a id="l02562"></a>
<a id="l02563"></a>
<a id="l02564"></a>
<a id="l02565"></a>
<a id="l02571"></a>
<a id="l02572"></a>
<a id="l02573"></a>
<a id="l02580"></a>
<a id="l02581"></a>
<a id="l02582"></a>
<a id="l02583"></a>
<a id="l02589"></a>
<a id="l02590"></a>
<a id="l02596"></a>
<a id="l02597"></a>
<a id="l02603"></a>
<a id="l02604"></a>
<a id="l02605"></a>
<a id="l02610"></a>
<a id="l02611"></a>
<a id="l02612"></a>
<a id="l02613"></a>
<a id="l02620"></a>
<a id="l02621"></a>
<a id="l02622"></a>
<a id="l02623"></a>
<a id="l02627"></a>
<a id="l02628"></a>
<a id="l02629"></a>
<a id="l02630"></a>
<a id="l02631"></a>
<a id="aethernet_8h_html"></a>
<a id="agroup__net__mgmt_html_ga08bde8717fd8e12a338c517b22b87776"></a>
<a id="agroup__wifi__mgmt_html_ga036416696b1e3bc458ddbaf07a08d69d"></a>
<a id="agroup__wifi__mgmt_html_ga03ab29789adfe867c4ebaddc39482344"></a>
<a id="agroup__wifi__mgmt_html_ga0cc87c00cbee0d0aca833119dbf0d74e"></a>
<a id="agroup__wifi__mgmt_html_ga0fffeb57b68fb8cdef9d3d571368b8ca"></a>
<a id="agroup__wifi__mgmt_html_ga1032f3773cfe6130da4d4d498b044ee2"></a>
<a id="agroup__wifi__mgmt_html_ga18f09a3196588b51d6c0644f82f639d7"></a>
<a id="agroup__wifi__mgmt_html_ga1bea051b0c184cb859f27b36e3593bf2"></a>
<a id="agroup__wifi__mgmt_html_ga1c277da90986fa52dca182c4d922646f"></a>
<a id="agroup__wifi__mgmt_html_ga1e2f0439a322355fa7368ea880c9c15d"></a>
<a id="agroup__wifi__mgmt_html_ga1f252da47d9650023d7fff6d08e49c76"></a>
<a id="agroup__wifi__mgmt_html_ga22d80ef0ffb15e4286d7b1c3325d5334"></a>
<a id="agroup__wifi__mgmt_html_ga234d72d7c881e67ff49fb6c474c622e3"></a>
<a id="agroup__wifi__mgmt_html_ga2678ea372335af008d9bd3333f7a7de1"></a>
<a id="agroup__wifi__mgmt_html_ga29409ff83a53c6464decdde9bdd04de6"></a>
<a id="agroup__wifi__mgmt_html_ga2b27d102b779a6d846b375854768fb7f"></a>
<a id="agroup__wifi__mgmt_html_ga2d424d1711389fb784e916a87ff854b7"></a>
<a id="agroup__wifi__mgmt_html_ga3098e817d12bf4619c9fd2698508fb4e"></a>
<a id="agroup__wifi__mgmt_html_ga31c78afc89bfdc4b54cee177843f8022"></a>
<a id="agroup__wifi__mgmt_html_ga36992c3098d2a1e87f31a18ce369bcc8"></a>
<a id="agroup__wifi__mgmt_html_ga373031970a29331bf1b30d1654c128f0"></a>
<a id="agroup__wifi__mgmt_html_ga38c184ea35c02f304cccdf389ca6d552"></a>
<a id="agroup__wifi__mgmt_html_ga38d92ba342887e46c957b820d89a7a20"></a>
<a id="agroup__wifi__mgmt_html_ga39404d15243ca084b253cae8fc07e374"></a>
<a id="agroup__wifi__mgmt_html_ga3b01cead3c2eb4581fe85e2aaaffbd49"></a>
<a id="agroup__wifi__mgmt_html_ga3b6edcf9b51afbf7a327d1a344bd7b87"></a>
<a id="agroup__wifi__mgmt_html_ga3e45f6ee3801553619d8eb7d0af506eb"></a>
<a id="agroup__wifi__mgmt_html_ga3e60c29ca9ce95d17a7fff087290f7f1"></a>
<a id="agroup__wifi__mgmt_html_ga3f7c4f252ab9621fbf3b9bd937253858"></a>
<a id="agroup__wifi__mgmt_html_ga48fea1f0c7d2700cef47068f96c6b71a"></a>
<a id="agroup__wifi__mgmt_html_ga49fb9c3908be61d847b31c99be6afc42"></a>
<a id="agroup__wifi__mgmt_html_ga4a2b1e8befd7376749b1d4fbcf98376f"></a>
<a id="agroup__wifi__mgmt_html_ga4b3de0f402a8f0012ea65c4ab50d2761"></a>
<a id="agroup__wifi__mgmt_html_ga4c36ae1a5171d3fbaeebf95c16be496d"></a>
<a id="agroup__wifi__mgmt_html_ga4d03aedac13ee4512d7717ac624f319a"></a>
<a id="agroup__wifi__mgmt_html_ga4d9dbfcf719df5639a0d592b4b8d4322"></a>
<a id="agroup__wifi__mgmt_html_ga4f644b4c980628ffd556458eddc0933d"></a>
<a id="agroup__wifi__mgmt_html_ga584f6239ac14e2bedc5e6bd72756423b"></a>
<a id="agroup__wifi__mgmt_html_ga638d2eb0a5029c1af46a91b523ed8589"></a>
<a id="agroup__wifi__mgmt_html_ga649a63bc7d315ebdd89464ff48b3fada"></a>
<a id="agroup__wifi__mgmt_html_ga6766ef7bcb001f1fb526a4083b6cd8bc"></a>
<a id="agroup__wifi__mgmt_html_ga67b52edeff76c2211b038f4aa90b8982"></a>
<a id="agroup__wifi__mgmt_html_ga68aaced888f98e1ba4e6b61b53e5e2ba"></a>
<a id="agroup__wifi__mgmt_html_ga695123cd534e2499f516a07fdc5cafa8"></a>
<a id="agroup__wifi__mgmt_html_ga71c99913bded844c4ca32ed9155bc470"></a>
<a id="agroup__wifi__mgmt_html_ga7da6af0747bcba85f8afab30c92b5b43"></a>
<a id="agroup__wifi__mgmt_html_ga7ef91a39c2cc6bb454d870a8a80f8439"></a>
<a id="agroup__wifi__mgmt_html_ga83546cf946a9123c563609e8903d9642"></a>
<a id="agroup__wifi__mgmt_html_ga86a5741e54aeb3e290142b0de217b8a8"></a>
<a id="agroup__wifi__mgmt_html_ga89cc123bb5c30140d2ce0a8b741b1086"></a>
<a id="agroup__wifi__mgmt_html_ga9070995249eb35de37e2b60c4426f840"></a>
<a id="agroup__wifi__mgmt_html_ga90afd8d4e83056463ec6e667ed8ea60a"></a>
<a id="agroup__wifi__mgmt_html_ga97fa304f9a1db2294a93cccd4c93bcf6"></a>
<a id="agroup__wifi__mgmt_html_ga9918582d4e7bb0952daf993ee34e166d"></a>
<a id="agroup__wifi__mgmt_html_ga99a55137188119f65f9d2bb4f57cac77"></a>
<a id="agroup__wifi__mgmt_html_ga9b4da60a8108b0cc431ac1eecfca0cd0"></a>
<a id="agroup__wifi__mgmt_html_ga9d407a15b9804aea6673d603aec9f0e9"></a>
<a id="agroup__wifi__mgmt_html_gaa3e52e08d89a1104f07207e52b81d503"></a>
<a id="agroup__wifi__mgmt_html_gaa75246d6dc55dada389c9d31e2607d5c"></a>
<a id="agroup__wifi__mgmt_html_gaa7ab2a97950a22736bb69f60b459f0f6"></a>
<a id="agroup__wifi__mgmt_html_gaacc27e95277622f56ef35e129aaac4d0"></a>
<a id="agroup__wifi__mgmt_html_gaaf730bf76adc06434c7ac63bf0417884"></a>
<a id="agroup__wifi__mgmt_html_gab84fd7e9ca0bf0b2b9d08889dda26aad"></a>
<a id="agroup__wifi__mgmt_html_gabdb2a784d4727b71ab44cca04e422c62"></a>
<a id="agroup__wifi__mgmt_html_gabdf7753c247587eface6e829686d120c"></a>
<a id="agroup__wifi__mgmt_html_gabe45d132797047c098041331c8f6f912"></a>
<a id="agroup__wifi__mgmt_html_gac2638308cbb0d268831f1618cf8e1fa8"></a>
<a id="agroup__wifi__mgmt_html_gac6483341435ff380a2d4a69430899c1a"></a>
<a id="agroup__wifi__mgmt_html_gac782af0a60b202fd19597cabb7bd3a9a"></a>
<a id="agroup__wifi__mgmt_html_gac7f907644847e905d67c709fa4afae7f"></a>
<a id="agroup__wifi__mgmt_html_gac8f17f0aa3e426a5cdb731727b9b9ce3"></a>
<a id="agroup__wifi__mgmt_html_gad0e998aeb1b27c4f203ca76339d323a3"></a>
<a id="agroup__wifi__mgmt_html_gad30e29eda65ccafdbd7f11865937b8ea"></a>
<a id="agroup__wifi__mgmt_html_gad34b366f1c315207ce0da587ca96d8d8"></a>
<a id="agroup__wifi__mgmt_html_gad3709d07aaa3ed59b48f9dd7bd181989"></a>
<a id="agroup__wifi__mgmt_html_gad62c60666c9fdffe2e0e9c4388f87886"></a>
<a id="agroup__wifi__mgmt_html_gad9614d2368f8399850aaec05e40bdc78"></a>
<a id="agroup__wifi__mgmt_html_gad98099584d2222ede93aba42b1fbaff0"></a>
<a id="agroup__wifi__mgmt_html_gadd9b5b206c7ee2e40c30a37c7b4fc002"></a>
<a id="agroup__wifi__mgmt_html_gadde31a04fa25ed805115c6b31854cd9c"></a>
<a id="agroup__wifi__mgmt_html_gadee15c6a492a8ee13bea43812debb5d9"></a>
<a id="agroup__wifi__mgmt_html_gae129d0783276e662575af2314eef86cd"></a>
<a id="agroup__wifi__mgmt_html_gae5dc7835e11487187663dfe65a15f22b"></a>
<a id="agroup__wifi__mgmt_html_gaf1a806a89b0fd20de950c6e085351134"></a>
<a id="agroup__wifi__mgmt_html_gaf4a78d230f5e0743a6aaf152ddda1c67"></a>
<a id="agroup__wifi__mgmt_html_gaf81f62bf4c9e331a095acbf0d24ca1a2"></a>
<a id="agroup__wifi__mgmt_html_gafc901312b5988481b34d05a031d6c0db"></a>
<a id="agroup__wifi__mgmt_html_gaffae7d2a754be5eb952ad2b83edad54c"></a>
<a id="agroup__wifi__mgmt_html_gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7"></a>
<a id="agroup__wifi__mgmt_html_gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68"></a>
<a id="agroup__wifi__mgmt_html_gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba"></a>
<a id="agroup__wifi__mgmt_html_gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e"></a>
<a id="agroup__wifi__mgmt_html_gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056"></a>
<a id="agroup__wifi__mgmt_html_gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae"></a>
<a id="agroup__wifi__mgmt_html_gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69"></a>
<a id="agroup__wifi__mgmt_html_gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f"></a>
<a id="agroup__wifi__mgmt_html_gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda"></a>
<a id="agroup__wifi__mgmt_html_gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e"></a>
<a id="agroup__wifi__mgmt_html_gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0"></a>
<a id="agroup__wifi__mgmt_html_gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a"></a>
<a id="agroup__wifi__mgmt_html_gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113"></a>
<a id="agroup__wifi__mgmt_html_gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c"></a>
<a id="agroup__wifi__mgmt_html_gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0"></a>
<a id="agroup__wifi__mgmt_html_gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88"></a>
<a id="agroup__wifi__mgmt_html_gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552"></a>
<a id="agroup__wifi__mgmt_html_gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a2186b1d9553322b3ba8bab4acee63833"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a40104910a4d0258f63a03851de929474"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a41c1a99be1e0c7b32590b4d69034b282"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a812004756d95cd2d56982260f89f9178"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a94b310a457fdf82c04ce9e396965d512"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77aae4df4e8f0959ca7a198c31a0283924e"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77aaf770b48056af1f9d6d99deb3772027d"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77ab95b651107d819809cb5909dc25a5a56"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77ae496f72d75179a2d10e9fb326259e413"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9"></a>
<a id="agroup__wifi__mgmt_html_gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7"></a>
<a id="agroup__wifi__mgmt_html_ggaacc27e95277622f56ef35e129aaac4d0a40446bcc15ca3f09acba97029f68cbbe"></a>
<a id="agroup__wifi__mgmt_html_ggaacc27e95277622f56ef35e129aaac4d0ad22b7dc42e9713d08cc9242b801f24e9"></a>
<a id="agroup__wifi__mgmt_html_ggaacc27e95277622f56ef35e129aaac4d0ae682cebd0e3ef481bf53e187eb92d911"></a>
<a id="agroup__wifi__mgmt_html_ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15"></a>
<a id="agroup__wifi__mgmt_html_ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c"></a>
<a id="agroup__wifi__mgmt_html_ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca"></a>
<a id="agroup__wifi__mgmt_html_ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe"></a>
<a id="agroup__wifi__mgmt_html_ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b"></a>
<a id="agroup__wifi__mgmt_html_ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a"></a>
<a id="agroup__wifi__mgmt_html_ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8"></a>
<a id="agroup__wifi__mgmt_html_ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce"></a>
<a id="agroup__wifi__mgmt_html_ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6"></a>
<a id="agroup__wifi__mgmt_html_ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6"></a>
<a id="agroup__wifi__mgmt_html_ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204"></a>
<a id="agroup__wifi__mgmt_html_ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042"></a>
<a id="agroup__wifi__mgmt_html_ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c"></a>
<a id="agroup__wifi__mgmt_html_ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7"></a>
<a id="agroup__wifi__mgmt_html_ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd"></a>
<a id="agroup__wifi__mgmt_html_ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__mgmt_8h_html"></a>
<a id="aoffloaded__netdev_8h_html"></a>
<a id="aposix_2sys_2socket_8h_html_a7005ffbeeff92be5394ff3244da79028"></a>
<a id="aposix_2sys_2socket_8h_html_a90f0aa598d0f4ab4ea99ecf289a6a7fb"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructdevice_html"></a>
<a id="astructethernet__api_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__stats__wifi_html"></a>
<a id="astructnet__wifi__mgmt__offload_html"></a>
<a id="astructnet__wifi__mgmt__offload_html_a1d34a954a2f16d29f51dc51dd6fbb845"></a>
<a id="astructnet__wifi__mgmt__offload_html_a98fcc053d9820d2d981ed659520c9b3b"></a>
<a id="astructnet__wifi__mgmt__offload_html_a991e0bc6247578a3d1c9d2d3ab0b63d7"></a>
<a id="astructoffloaded__if__api_html"></a>
<a id="astructwifi__11k__params_html"></a>
<a id="astructwifi__11k__params_html_a64ace23c71837417678ceb9cc8d5f216"></a>
<a id="astructwifi__11k__params_html_a739c3e94b025aae2fcf5680aecf3d646"></a>
<a id="astructwifi__11k__params_html_ae6029ed4bada41f18df0329d0da7401e"></a>
<a id="astructwifi__ap__config__params_html"></a>
<a id="astructwifi__ap__config__params_html_a289866d9209450e893281b4c198a546a"></a>
<a id="astructwifi__ap__config__params_html_a4c391cf504a994ed0bc4971afdf76774"></a>
<a id="astructwifi__ap__config__params_html_a7fc0fad99f53ed8e1ac40b74ec98bf9a"></a>
<a id="astructwifi__ap__config__params_html_aba4e43dff01fa026c8dbbfff670d3097"></a>
<a id="astructwifi__ap__sta__info_html"></a>
<a id="astructwifi__ap__sta__info_html_a7d8bd52340d4937a4b5b7d2c00662441"></a>
<a id="astructwifi__ap__sta__info_html_a7db904376ec73b774aa9d8236c15b3f6"></a>
<a id="astructwifi__ap__sta__info_html_a7f7c8b144bb3464af5213708591eefda"></a>
<a id="astructwifi__ap__sta__info_html_a838c9a4288c9bc7e97afe2334c678f34"></a>
<a id="astructwifi__band__channel_html"></a>
<a id="astructwifi__band__channel_html_a4a932599429f37231f76c3064ec5efb3"></a>
<a id="astructwifi__band__channel_html_acd0dd7366de3650124dad7232a58ade0"></a>
<a id="astructwifi__bgscan__params_html"></a>
<a id="astructwifi__bgscan__params_html_a1a6cc39e71f94c9fae639a886f5c3030"></a>
<a id="astructwifi__bgscan__params_html_a5ec94a609155573cedfe7772b940d183"></a>
<a id="astructwifi__bgscan__params_html_a8d12ab3d7d589d06c79874ea374ae327"></a>
<a id="astructwifi__bgscan__params_html_ab73566a1db6e31c15c575cab21f24bfb"></a>
<a id="astructwifi__bgscan__params_html_ae1e3e6bf419e7f810e5ba7b085be7c12"></a>
<a id="astructwifi__btwt__params_html"></a>
<a id="astructwifi__btwt__params_html_a0192d3a9334fc55a135206e6b74ea5b5"></a>
<a id="astructwifi__btwt__params_html_a2c1b3551a714fbf1b948ce4bcf805934"></a>
<a id="astructwifi__btwt__params_html_a76c97bcc132405d6a1a54bcca77054ac"></a>
<a id="astructwifi__btwt__params_html_ae52281d9f53e106fb9ed813131d8085e"></a>
<a id="astructwifi__channel__info_html"></a>
<a id="astructwifi__channel__info_html_a43a7dd8c19d0c6540e3cc0b5d1d6165d"></a>
<a id="astructwifi__channel__info_html_a799cbc0a67764f6680322ba0f2ad3300"></a>
<a id="astructwifi__channel__info_html_aa8ef8a71b49ead3664fff9a4d61b1ce8"></a>
<a id="astructwifi__channel__info_html_aeda7667c89ca98c1f45a09331a2bfd47"></a>
<a id="astructwifi__config__params_html"></a>
<a id="astructwifi__config__params_html_a3a05f8b09eb2a74913c394f28fe7ab79"></a>
<a id="astructwifi__config__params_html_aada77f3f6f5909ebefb699d7252bb74c"></a>
<a id="astructwifi__connect__req__params_html"></a>
<a id="astructwifi__connect__req__params_html_a020fc58d7e5350cc803cd5d6fa575e6a"></a>
<a id="astructwifi__connect__req__params_html_a040d2bda9e1a6528814d4cb87bef2924"></a>
<a id="astructwifi__connect__req__params_html_a047b11e703fb646d778785dfcb14257b"></a>
<a id="astructwifi__connect__req__params_html_a0d44c86d9b9528041bbe7534e0c7597a"></a>
<a id="astructwifi__connect__req__params_html_a18dce6bb021086877a30e7a04f5b24b9"></a>
<a id="astructwifi__connect__req__params_html_a2163b50b6d466663404e1cb21ce6ae5d"></a>
<a id="astructwifi__connect__req__params_html_a265001d2309840d04bdca507896255d0"></a>
<a id="astructwifi__connect__req__params_html_a2892253024b70e5cb8eb2166b17ebe22"></a>
<a id="astructwifi__connect__req__params_html_a3833aaaaa78e31d2061e690564af200d"></a>
<a id="astructwifi__connect__req__params_html_a469fac5758b78fc425911837930b2060"></a>
<a id="astructwifi__connect__req__params_html_a4946647659a347667ee49bb6990bba66"></a>
<a id="astructwifi__connect__req__params_html_a4da02ff112c09f55dc5bddcda27d16a3"></a>
<a id="astructwifi__connect__req__params_html_a52b6d0323c35d03ec239f40be35cae72"></a>
<a id="astructwifi__connect__req__params_html_a547dddf6be5dd77eda74b1085a798400"></a>
<a id="astructwifi__connect__req__params_html_a56183ba7f4d8eaf5fc5b495856adecfd"></a>
<a id="astructwifi__connect__req__params_html_a562ce91f5eff43e85f84acf342d4e288"></a>
<a id="astructwifi__connect__req__params_html_a694a729632ab4e0c54fa739dd9bd9132"></a>
<a id="astructwifi__connect__req__params_html_a71770c2f2da378db2efedaa87b141627"></a>
<a id="astructwifi__connect__req__params_html_a745b3416172672a7e5b12bcc5b55e88c"></a>
<a id="astructwifi__connect__req__params_html_a74f0819e7a546ffb8bfb0ec587eccf20"></a>
<a id="astructwifi__connect__req__params_html_a781456e079357e2e1096218af3bd218c"></a>
<a id="astructwifi__connect__req__params_html_a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf"></a>
<a id="astructwifi__connect__req__params_html_a9f913fc0ccecafaba488e444d701fd68"></a>
<a id="astructwifi__connect__req__params_html_aa2fea1881a8ffdf5d7093ae295867f3e"></a>
<a id="astructwifi__connect__req__params_html_aa4577535a27b8d54d9b8c7543d359ade"></a>
<a id="astructwifi__connect__req__params_html_aa7743f0ecbc27a9595720ce13ce57c1d"></a>
<a id="astructwifi__connect__req__params_html_aa8081b9075ff9244cefd0ac1ef3f42cb"></a>
<a id="astructwifi__connect__req__params_html_aa8f18ace96e471eb0bc8bff8d8146f6f"></a>
<a id="astructwifi__connect__req__params_html_aaf071a51c7281e4d42197f266c729c04"></a>
<a id="astructwifi__connect__req__params_html_aaf7455a65590d19f047214b459a2dcb9"></a>
<a id="astructwifi__connect__req__params_html_ab9c65599409387af65a3c2895c3116da"></a>
<a id="astructwifi__connect__req__params_html_ac260c2cd17a3f36ea101edaf23d41083"></a>
<a id="astructwifi__connect__req__params_html_ac9675ace459d40d6e912d86b6b416305"></a>
<a id="astructwifi__connect__req__params_html_ad82589b9613dd52b63c9ea5ae0fcebeb"></a>
<a id="astructwifi__connect__req__params_html_ae0b94d870ecbee0b203caee6a6e3d8b2"></a>
<a id="astructwifi__connect__req__params_html_aeab22e95a04a1831b87beda1772d3db7"></a>
<a id="astructwifi__connect__req__params_html_af7b163cc2bffc59f7fa31f47c5e52062"></a>
<a id="astructwifi__connect__req__params_html_af94eefb87c15c53057e8f22b67a50494"></a>
<a id="astructwifi__connect__req__params_html_afac70366e509301f9a27ca51be30b88d"></a>
<a id="astructwifi__connect__req__params_html_afd046e702739c4a0d89322ee41b37acd"></a>
<a id="astructwifi__enterprise__creds__params_html"></a>
<a id="astructwifi__enterprise__creds__params_html_a09f5b34c81fe871e7513358499518d95"></a>
<a id="astructwifi__enterprise__creds__params_html_a133126e338d89563733268a03e2fa613"></a>
<a id="astructwifi__enterprise__creds__params_html_a3da90b8a8dfa848f617579760ad4f971"></a>
<a id="astructwifi__enterprise__creds__params_html_a5f122d59b25b00af2db7eeac93d5482e"></a>
<a id="astructwifi__enterprise__creds__params_html_a5f7060fcd2ca3db0b202faf15062564b"></a>
<a id="astructwifi__enterprise__creds__params_html_a81d61179feba627be5c6456130b9f2af"></a>
<a id="astructwifi__enterprise__creds__params_html_a8d88f5a8a6ccc8a9a883078af49ae96b"></a>
<a id="astructwifi__enterprise__creds__params_html_a9500252974bd15037d4dbc41eba3a27d"></a>
<a id="astructwifi__enterprise__creds__params_html_ab0fd7419d8a94d1d804e5554acfbf49a"></a>
<a id="astructwifi__enterprise__creds__params_html_abcda4d7820681d517d70d8f130b47050"></a>
<a id="astructwifi__enterprise__creds__params_html_abf35045e71afb0cb9ea25c635c5ac141"></a>
<a id="astructwifi__enterprise__creds__params_html_ac548e0b006a9f7b858409cda7c3d34ba"></a>
<a id="astructwifi__enterprise__creds__params_html_acb94a8885b5ab99d1a8fb33dffebc322"></a>
<a id="astructwifi__enterprise__creds__params_html_ad0bfb59d3691e5d21cb4b810c4d1279e"></a>
<a id="astructwifi__enterprise__creds__params_html_ad3621e92a1aa968c58a899ace72967db"></a>
<a id="astructwifi__enterprise__creds__params_html_ad9b867873709d7f2363fef49d7b6f2ca"></a>
<a id="astructwifi__enterprise__creds__params_html_adbe26c9b88f44eb6b875888f6a03e1bb"></a>
<a id="astructwifi__enterprise__creds__params_html_ae37381504a457b2f1d56dd5270c6711d"></a>
<a id="astructwifi__filter__info_html"></a>
<a id="astructwifi__filter__info_html_a1b2d0448fc7f62654e3f5aacfba62f8f"></a>
<a id="astructwifi__filter__info_html_ad9560be814299055cfa11b995a7dcf42"></a>
<a id="astructwifi__filter__info_html_aedd5e220cdde5768cb0f4aff920971cd"></a>
<a id="astructwifi__filter__info_html_af9ea91e31e78afcb7ffe1ff9a04277a3"></a>
<a id="astructwifi__iface__status_html"></a>
<a id="astructwifi__iface__status_html_a241bfbe70628006b515b5f9e4f97665c"></a>
<a id="astructwifi__iface__status_html_a361c0e8a385fdc21f16258c25c2bc8d1"></a>
<a id="astructwifi__iface__status_html_a3ab671471bcdfeb5b955d156d39f2bb3"></a>
<a id="astructwifi__iface__status_html_a43f239b0bc305e4c1c5f7fd9bb5753bf"></a>
<a id="astructwifi__iface__status_html_a4e593147b88eb4938d55a4de72fcc7f6"></a>
<a id="astructwifi__iface__status_html_a5d5d19056a1a15365fbdd94274a0fc5e"></a>
<a id="astructwifi__iface__status_html_a625ecec1abec8dd65cf155eab21a01b5"></a>
<a id="astructwifi__iface__status_html_a6432663156e5b2c424d254ed1eae0144"></a>
<a id="astructwifi__iface__status_html_a9a899c28b51158e8973886f84d7d8950"></a>
<a id="astructwifi__iface__status_html_aa1a9b644fd355526125ddd32416b7c24"></a>
<a id="astructwifi__iface__status_html_aae6c8cbaa16c81d308f08114d5103a3d"></a>
<a id="astructwifi__iface__status_html_ac52806155be3d64954ac6d109e76ec57"></a>
<a id="astructwifi__iface__status_html_acfde8d64b463a9f553aa4fb689dc1917"></a>
<a id="astructwifi__iface__status_html_ad33d2ec149a8d556e2472dd842ceadc0"></a>
<a id="astructwifi__iface__status_html_ad82f281941e4f6ce1ef0bca008e26d41"></a>
<a id="astructwifi__iface__status_html_ae1c141a18f4e225af2c22a8cb4f882a8"></a>
<a id="astructwifi__iface__status_html_ae2de076d79f2172793d65fe9cd31edc4"></a>
<a id="astructwifi__mgmt__ops_html"></a>
<a id="astructwifi__mgmt__ops_html_a01b2ac4cd8a1f039bdba3adb2586d3cb"></a>
<a id="astructwifi__mgmt__ops_html_a0aa02b0d69479b95d6e1a0971b16ee92"></a>
<a id="astructwifi__mgmt__ops_html_a0bfeb2a8f463dc49ca3d433ee17d3dd9"></a>
<a id="astructwifi__mgmt__ops_html_a16fc04b7572234f6e7c207d82e0b4625"></a>
<a id="astructwifi__mgmt__ops_html_a26eaabf9621b16d332e20777b188d4ad"></a>
<a id="astructwifi__mgmt__ops_html_a3264be8040227d1e91a8223cabcd4e53"></a>
<a id="astructwifi__mgmt__ops_html_a365e9aafc5399e1a9f37c9b4f347534c"></a>
<a id="astructwifi__mgmt__ops_html_a37e6c41f4b1223b8952171abb5cd9d89"></a>
<a id="astructwifi__mgmt__ops_html_a40d53afce76b5b7614ee95e41ea46635"></a>
<a id="astructwifi__mgmt__ops_html_a50421d54785d4f8d768c8a35fcda0ca5"></a>
<a id="astructwifi__mgmt__ops_html_a5642ca19f2f25ba7a53d9efb30d7bd59"></a>
<a id="astructwifi__mgmt__ops_html_a6198f23a4cdeb5b0e413b7a66c1fa442"></a>
<a id="astructwifi__mgmt__ops_html_a63e7bcc4d3bb9ee7e073a6c55abddcc2"></a>
<a id="astructwifi__mgmt__ops_html_a65a4e87ee94aa5c7a551aa9b39289708"></a>
<a id="astructwifi__mgmt__ops_html_a69f2ec3a03e77b4eb9d9fdd7315edf18"></a>
<a id="astructwifi__mgmt__ops_html_a76e76d96e307bc10bd14e4ea7b5dbed6"></a>
<a id="astructwifi__mgmt__ops_html_a7b788903271a427363d22808659a3ee9"></a>
<a id="astructwifi__mgmt__ops_html_a7bd0f326e9eeedbc3c768c5ecf207c06"></a>
<a id="astructwifi__mgmt__ops_html_a80b09c5ea77c99a4dfffb5a21f0c8867"></a>
<a id="astructwifi__mgmt__ops_html_a8489951fc1baee17e56070187f4d77b0"></a>
<a id="astructwifi__mgmt__ops_html_a8d37cec74b3d523257120b75f471e92f"></a>
<a id="astructwifi__mgmt__ops_html_a9278c8779748e64ad70cfbeef5a297dd"></a>
<a id="astructwifi__mgmt__ops_html_a930cbd9e4661d137ae37cd89afd451b2"></a>
<a id="astructwifi__mgmt__ops_html_aa34fff15f9e0aadf244f9e0cf37b367b"></a>
<a id="astructwifi__mgmt__ops_html_ab3b7dce2feb0ecbca3d4668dc9e41032"></a>
<a id="astructwifi__mgmt__ops_html_ab5368326d558de972ce5806dd9a99f22"></a>
<a id="astructwifi__mgmt__ops_html_ab8e11d463ff7000a090e0609f002a97c"></a>
<a id="astructwifi__mgmt__ops_html_abb2b7c033e77af36acde5d420effe8d1"></a>
<a id="astructwifi__mgmt__ops_html_ac4ed6d4d1088f6e23d5256d156e42955"></a>
<a id="astructwifi__mgmt__ops_html_ac6d82f5f2defdc657f056f0e6103e04b"></a>
<a id="astructwifi__mgmt__ops_html_acc20fd11dcd09edb72d03f8737801c06"></a>
<a id="astructwifi__mgmt__ops_html_ad241d490ac3e10c58c87da004d706407"></a>
<a id="astructwifi__mgmt__ops_html_ad3c8908b6a3752adf59d5a4170175f83"></a>
<a id="astructwifi__mgmt__ops_html_ad6e04312b0e7680f87ce801b2540db10"></a>
<a id="astructwifi__mgmt__ops_html_aed7b6daf7264c1450cc5d31530a2043a"></a>
<a id="astructwifi__mgmt__ops_html_af2089cba9ba73593b8d5b4329f2fddff"></a>
<a id="astructwifi__mode__info_html"></a>
<a id="astructwifi__mode__info_html_a57c101db8b81ab0ac5dd0a158057a64a"></a>
<a id="astructwifi__mode__info_html_aa29d3b88fc718aa3ac05daf38974707d"></a>
<a id="astructwifi__mode__info_html_add58dd3b45fd2ddaf684d1b0de81bef9"></a>
<a id="astructwifi__ps__config_html"></a>
<a id="astructwifi__ps__config_html_a357aafc2dedda37755b1cb1fc07fe5a6"></a>
<a id="astructwifi__ps__config_html_a9e83c10eaaa1d721cbc49b40aedb00df"></a>
<a id="astructwifi__ps__config_html_ab7460f0f253b2d552e49e98e2c770967"></a>
<a id="astructwifi__ps__params_html"></a>
<a id="astructwifi__ps__params_html_a5a022d89d43ecf2cd1f15fc72c0f2bed"></a>
<a id="astructwifi__ps__params_html_a63fa2ee03bc4aefada61c298ee14336c"></a>
<a id="astructwifi__ps__params_html_a7cb3e7fb7d9f8bd7c2cab41f879b3b66"></a>
<a id="astructwifi__ps__params_html_a8510c799ab0c5825f1c6349f9799c62f"></a>
<a id="astructwifi__ps__params_html_ab9fc62dd1e2928320274fa1554a550a6"></a>
<a id="astructwifi__ps__params_html_abb22aaa45833ac130922204bd2fe841b"></a>
<a id="astructwifi__ps__params_html_ad963f1bf78dc271f08b73f3aadb36a91"></a>
<a id="astructwifi__ps__params_html_aef62e5bf6216bf4dc461efe71735c4bd"></a>
<a id="astructwifi__raw__scan__result_html"></a>
<a id="astructwifi__raw__scan__result_html_a3f08580c6448a5fa28dd8a594fa7dad6"></a>
<a id="astructwifi__raw__scan__result_html_a5710e89199c147ce898602795f00aba3"></a>
<a id="astructwifi__raw__scan__result_html_a876966f469714eb481b42ccc8a63945c"></a>
<a id="astructwifi__raw__scan__result_html_aa2c7781882c6775616cbc8016b0842f6"></a>
<a id="astructwifi__reg__chan__info_html"></a>
<a id="astructwifi__reg__chan__info_html_a0addffc11ef29f50c01b700835e59930"></a>
<a id="astructwifi__reg__chan__info_html_a1ab137c142902d2de7d6be2626d7ac1f"></a>
<a id="astructwifi__reg__chan__info_html_aa044611e18b7332b8577e29f6a769e3f"></a>
<a id="astructwifi__reg__chan__info_html_acc7a88b004c9a61c8bf9ee1a97f85928"></a>
<a id="astructwifi__reg__chan__info_html_af9169ab4a41fac4c6f6766fc96799545"></a>
<a id="astructwifi__reg__domain_html"></a>
<a id="astructwifi__reg__domain_html_a3278e9f43893f49ab9f9d0d7f24009c1"></a>
<a id="astructwifi__reg__domain_html_a3bbfdf1497a87bbb6b6211c7035e1002"></a>
<a id="astructwifi__reg__domain_html_a4c8c9c11e41123cd7738fdb0d33ae5fb"></a>
<a id="astructwifi__reg__domain_html_a567c6fcae8032567aea83c18cd211c33"></a>
<a id="astructwifi__reg__domain_html_abf191495814c227fbbfaccb2f727762e"></a>
<a id="astructwifi__scan__params_html"></a>
<a id="astructwifi__scan__params_html_a12d5dea7d8fa8ad03ac2366720c46243"></a>
<a id="astructwifi__scan__params_html_a2453a75c23e04e3572559c0e7199c1b4"></a>
<a id="astructwifi__scan__params_html_a645acc54603cd4692527c1a028933078"></a>
<a id="astructwifi__scan__params_html_a6b571d960ed9d7419e31530e5fb6f97a"></a>
<a id="astructwifi__scan__params_html_a8e7a37ccda8de635e7b7066d7943e814"></a>
<a id="astructwifi__scan__params_html_aa5ddbd6bc97b7598288d4b0d38521681"></a>
<a id="astructwifi__scan__params_html_aac11ee8e0ec8a4fa24668f4820bd1a12"></a>
<a id="astructwifi__scan__result_html"></a>
<a id="astructwifi__scan__result_html_a2c1c2f4265b914df08fc75deb8b69d39"></a>
<a id="astructwifi__scan__result_html_a38201c9dd798dc11b5bda3ce97b02e92"></a>
<a id="astructwifi__scan__result_html_a4fdbc4dc4d5c8b279223e8c06624f434"></a>
<a id="astructwifi__scan__result_html_a76aa012136e3721fd4a482a22b93546f"></a>
<a id="astructwifi__scan__result_html_a8fca0dabec00ebd7ed4800098ec9d451"></a>
<a id="astructwifi__scan__result_html_aaefb8f5c9510e4f5002ae306d853ade8"></a>
<a id="astructwifi__scan__result_html_abb7de47c605ec05c8fe0a06ecbd2b7b6"></a>
<a id="astructwifi__scan__result_html_acaa3fb30ebf6df22bfac6380698ed28e"></a>
<a id="astructwifi__scan__result_html_adbbfd7692ee5ffd6344fe78b9d91c840"></a>
<a id="astructwifi__scan__result_html_af2d3dc5d115e3db76d3bc115510b0a5a"></a>
<a id="astructwifi__status_html"></a>
<a id="astructwifi__status_html_a02f0fcc7ef57661ca95d0c99f045aef1"></a>
<a id="astructwifi__status_html_a8c63d5fecc9d532366c144b4dd7bb2ad"></a>
<a id="astructwifi__status_html_a8f885e78366d0499e4ba8e15bef275ac"></a>
<a id="astructwifi__status_html_aa04b5033d93274badd27f702af9830bc"></a>
<a id="astructwifi__status_html_aa1dbff8154400f8353693d387977008b"></a>
<a id="astructwifi__status_html_ac8a85738dcfa60dfaf502d86b8294f78"></a>
<a id="astructwifi__twt__flow__info_html"></a>
<a id="astructwifi__twt__flow__info_html_a123ce10bed8b62b01919a7ea7644a0ba"></a>
<a id="astructwifi__twt__flow__info_html_a620ae8ba546e4091d74280cb1553b2cf"></a>
<a id="astructwifi__twt__flow__info_html_a6384d3829d54a58a53eafcb74c64a658"></a>
<a id="astructwifi__twt__flow__info_html_a952a67bd092c5dadba387bb13449c6f3"></a>
<a id="astructwifi__twt__flow__info_html_ac82e4de8ffc82f851061f8ba8d217dc1"></a>
<a id="astructwifi__twt__flow__info_html_acb0c618f1cebcb172f342cfe222683be"></a>
<a id="astructwifi__twt__flow__info_html_ae15ba49fa54f82cc6a1fb0d4572114b7"></a>
<a id="astructwifi__twt__flow__info_html_aede6cb0cfc999fac8ded49e2981a3762"></a>
<a id="astructwifi__twt__flow__info_html_afb480be82d1c6f351bd634fd83bfa5c7"></a>
<a id="astructwifi__twt__flow__info_html_afc81a5111c265fd9bb2aca5f9510bfa8"></a>
<a id="astructwifi__twt__params_html"></a>
<a id="astructwifi__twt__params_html_a02f2d822d530e5376f256503439a54f9"></a>
<a id="astructwifi__twt__params_html_a26d6bda00452f77832f69f4465c13efb"></a>
<a id="astructwifi__twt__params_html_a347f8cff73ee6b6ba6d15ddf6f376a2d"></a>
<a id="astructwifi__twt__params_html_a4459cf19226e199d23ae0cd1d7132b73"></a>
<a id="astructwifi__twt__params_html_a4e822c04b52fe6a9489e48e26b8f9382"></a>
<a id="astructwifi__twt__params_html_a5fd269328f68838b8a7e3a0b93eed894"></a>
<a id="astructwifi__twt__params_html_a6f0483861a387651c9c89ba182e064bd"></a>
<a id="astructwifi__twt__params_html_a6f907ca412251fdd7391f29bfa6d7713"></a>
<a id="astructwifi__twt__params_html_a70f58b502bb67ef3b2068ded2160b612"></a>
<a id="astructwifi__twt__params_html_a72ab809144b1dd3e7e121e489ef399e2"></a>
<a id="astructwifi__twt__params_html_a7c297459a17ed2fd232c62cca63e952f"></a>
<a id="astructwifi__twt__params_html_a7e7c786c51d3bc70af135bad88ebde4f"></a>
<a id="astructwifi__twt__params_html_a805a23284ed4afa46b84efcd43329beb"></a>
<a id="astructwifi__twt__params_html_a8ea1e2501c8b69dc3fa606eb360f8678"></a>
<a id="astructwifi__twt__params_html_a95ec4b32d37309efa47256ae1ea865da"></a>
<a id="astructwifi__twt__params_html_a9faff59e577775b3fe53f2139462ac71"></a>
<a id="astructwifi__twt__params_html_aa05e5fa6a519f700147bb99d6e69a06b"></a>
<a id="astructwifi__twt__params_html_aa11562186ea265b906861269bc8a692b"></a>
<a id="astructwifi__twt__params_html_aabb77296f007cb055f78fa1ec3d155a3"></a>
<a id="astructwifi__twt__params_html_aadad4556e2e5405b0703ebb4233a4d17"></a>
<a id="astructwifi__twt__params_html_aadf62f6386359ad15491d0073c9065bf"></a>
<a id="astructwifi__twt__params_html_ab92fe571559fcd5d97cdf7e6b7d86681"></a>
<a id="astructwifi__twt__params_html_ac02eab9593b1ec2c9a0453a67076df88"></a>
<a id="astructwifi__twt__params_html_adda47e302a87a766f18e28016963a561"></a>
<a id="astructwifi__twt__params_html_ae547c6fc1c7cbad15bebcfdaa43f59e7"></a>
<a id="astructwifi__twt__params_html_aee57c0189b210cfcc18e213e35b9479c"></a>
<a id="astructwifi__twt__params_html_afc563010a33624bf01feac1292f0871d"></a>
<a id="astructwifi__version_html"></a>
<a id="astructwifi__version_html_a4bf2cbdf5c43ff21718ccf19646c164e"></a>
<a id="astructwifi__version_html_aea828bdb512440d6aa3cc853525c4971"></a>
<a id="astructwifi__wps__config__params_html"></a>
<a id="astructwifi__wps__config__params_html_a962bd6513c564150e0c75112b96bbe15"></a>
<a id="astructwifi__wps__config__params_html_aa7a10889c5cd5124983b0f7242d23b7e"></a>
<a id="awifi_8h_html"></a>

```c
/*
 * Copyright (c) 2017 Intel Corporation.
 * Copyright 2024 NXP
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_WIFI_MGMT_H_
#define ZEPHYR_INCLUDE_NET_WIFI_MGMT_H_

#include <zephyr/net/net_mgmt.h>
#include <zephyr/net/wifi.h>
#include <zephyr/net/ethernet.h>
#include <zephyr/net/offloaded_netdev.h>

#ifdef __cplusplus
extern "C" {
#endif


/* Management part definitions */


#define NET_WIFI_LAYER  NET_MGMT_LAYER_L2
#define NET_WIFI_CODE   NET_MGMT_LAYER_CODE_WIFI
#define NET_WIFI_BASE   (NET_MGMT_IFACE_BIT |                   \
                         NET_MGMT_LAYER(NET_WIFI_LAYER) |       \
                         NET_MGMT_LAYER_CODE(NET_WIFI_CODE))
#define NET_WIFI_EVENT  (NET_WIFI_BASE | NET_MGMT_EVENT_BIT)

#ifdef CONFIG_WIFI_MGMT_SCAN_SSID_FILT_MAX
#define WIFI_MGMT_SCAN_SSID_FILT_MAX CONFIG_WIFI_MGMT_SCAN_SSID_FILT_MAX
#else
#define WIFI_MGMT_SCAN_SSID_FILT_MAX 1
#endif /* CONFIG_WIFI_MGMT_SCAN_SSID_FILT_MAX */

#ifdef CONFIG_WIFI_MGMT_SCAN_CHAN_MAX_MANUAL
#define WIFI_MGMT_SCAN_CHAN_MAX_MANUAL CONFIG_WIFI_MGMT_SCAN_CHAN_MAX_MANUAL
#else
#define WIFI_MGMT_SCAN_CHAN_MAX_MANUAL 1
#endif /* CONFIG_WIFI_MGMT_SCAN_CHAN_MAX_MANUAL */

#ifdef CONFIG_WIFI_ENT_IDENTITY_MAX_USERS
#define WIFI_ENT_IDENTITY_MAX_USERS CONFIG_WIFI_ENT_IDENTITY_MAX_USERS
#else
#define WIFI_ENT_IDENTITY_MAX_USERS 1
#endif /* CONFIG_WIFI_ENT_IDENTITY_MAX_USERS */

#define WIFI_MGMT_BAND_STR_SIZE_MAX 8
#define WIFI_MGMT_SCAN_MAX_BSS_CNT 65535

#define WIFI_MGMT_SKIP_INACTIVITY_POLL IS_ENABLED(CONFIG_WIFI_MGMT_AP_STA_SKIP_INACTIVITY_POLL)

#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN
#define WIFI_NAN_MAX_SSI_LEN            CONFIG_WIFI_NAN_MAX_SSI_LEN
#define WIFI_NAN_MAX_SERVICE_NAME_LEN   64
/* Holds multi-line NAN_STATUS output from hostap. */
#define WIFI_NAN_RESP_SIZE              512
#define WIFI_NAN_MAX_SET_PARAM_LEN      32
#define WIFI_NAN_MAX_SET_VALUE_LEN      256
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN */

enum net_request_wifi_cmd {
        NET_REQUEST_WIFI_CMD_SCAN = 1,
        NET_REQUEST_WIFI_CMD_CONNECT,
        NET_REQUEST_WIFI_CMD_DISCONNECT,
        NET_REQUEST_WIFI_CMD_AP_ENABLE,
        NET_REQUEST_WIFI_CMD_AP_DISABLE,
        NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD,
        NET_REQUEST_WIFI_CMD_IFACE_STATUS,
        NET_REQUEST_WIFI_CMD_11K_CONFIG,
        NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST,
        NET_REQUEST_WIFI_CMD_PS,
        NET_REQUEST_WIFI_CMD_TWT,
        NET_REQUEST_WIFI_CMD_BTWT,
        NET_REQUEST_WIFI_CMD_PS_CONFIG,
        NET_REQUEST_WIFI_CMD_REG_DOMAIN,
        NET_REQUEST_WIFI_CMD_MODE,
        NET_REQUEST_WIFI_CMD_PACKET_FILTER,
        NET_REQUEST_WIFI_CMD_CHANNEL,
        NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT,
        NET_REQUEST_WIFI_CMD_VERSION,
        NET_REQUEST_WIFI_CMD_CONN_PARAMS,
        NET_REQUEST_WIFI_CMD_RTS_THRESHOLD,
        NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM,
        NET_REQUEST_WIFI_CMD_CONFIG_PARAM,
        NET_REQUEST_WIFI_CMD_DPP,
        NET_REQUEST_WIFI_CMD_NAN,
        NET_REQUEST_WIFI_CMD_BTM_QUERY,
        NET_REQUEST_WIFI_CMD_PMKSA_FLUSH,
        NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS,
        NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG,
        NET_REQUEST_WIFI_CMD_WPS_CONFIG,
#ifdef CONFIG_WIFI_CREDENTIALS_CONNECT_STORED
        NET_REQUEST_WIFI_CMD_CONNECT_STORED,
#endif
        NET_REQUEST_WIFI_CMD_START_ROAMING,
        NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE,
        NET_REQUEST_WIFI_CMD_CANDIDATE_SCAN,
        NET_REQUEST_WIFI_CMD_AP_WPS_CONFIG,
        NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD,
        NET_REQUEST_WIFI_CMD_BGSCAN,
        NET_REQUEST_WIFI_CMD_P2P_OPER,
        NET_REQUEST_WIFI_CMD_MAX
};

#define NET_REQUEST_WIFI_SCAN                                   \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_SCAN)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_SCAN);

#define NET_REQUEST_WIFI_CONNECT                                \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONNECT)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_CONNECT);

#define NET_REQUEST_WIFI_DISCONNECT                             \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_DISCONNECT)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_DISCONNECT);

#define NET_REQUEST_WIFI_AP_ENABLE                              \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_ENABLE)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_AP_ENABLE);

#define NET_REQUEST_WIFI_AP_DISABLE                             \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_DISABLE)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_AP_DISABLE);

#define NET_REQUEST_WIFI_AP_RTS_THRESHOLD                               \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_AP_RTS_THRESHOLD);

#define NET_REQUEST_WIFI_IFACE_STATUS                           \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_IFACE_STATUS)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_IFACE_STATUS);

#define NET_REQUEST_WIFI_11K_CONFIG                             \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_11K_CONFIG)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_11K_CONFIG);

#define NET_REQUEST_WIFI_11K_NEIGHBOR_REQUEST                   \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_11K_NEIGHBOR_REQUEST);

#define NET_REQUEST_WIFI_PS                                     \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PS)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_PS);

#define NET_REQUEST_WIFI_TWT                                    \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_TWT)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_TWT);

#define NET_REQUEST_WIFI_BTWT                   \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BTWT)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_BTWT);

#define NET_REQUEST_WIFI_PS_CONFIG                              \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PS_CONFIG)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_PS_CONFIG);

#define NET_REQUEST_WIFI_REG_DOMAIN                             \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_REG_DOMAIN)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_REG_DOMAIN);

#define NET_REQUEST_WIFI_MODE                                   \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_MODE)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_MODE);

#define NET_REQUEST_WIFI_PACKET_FILTER                          \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PACKET_FILTER)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_PACKET_FILTER);

#define NET_REQUEST_WIFI_CHANNEL                                \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CHANNEL)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_CHANNEL);

#define NET_REQUEST_WIFI_AP_STA_DISCONNECT                      \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_AP_STA_DISCONNECT);

#define NET_REQUEST_WIFI_VERSION                                \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_VERSION)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_VERSION);

#define NET_REQUEST_WIFI_CONN_PARAMS                           \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONN_PARAMS)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_CONN_PARAMS);

#define NET_REQUEST_WIFI_RTS_THRESHOLD                          \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_RTS_THRESHOLD)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_RTS_THRESHOLD);

#define NET_REQUEST_WIFI_AP_CONFIG_PARAM         \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_AP_CONFIG_PARAM);

#define NET_REQUEST_WIFI_CONFIG_PARAM         \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONFIG_PARAM)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_CONFIG_PARAM);

#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
#define NET_REQUEST_WIFI_DPP                    \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_DPP)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_DPP);
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP */

#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN
#define NET_REQUEST_WIFI_NAN                    \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_NAN)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_NAN);
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN */

#define NET_REQUEST_WIFI_BTM_QUERY (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BTM_QUERY)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_BTM_QUERY);

#define NET_REQUEST_WIFI_PMKSA_FLUSH                           \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_PMKSA_FLUSH)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_PMKSA_FLUSH);

#define NET_REQUEST_WIFI_ENTERPRISE_CREDS                               \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_ENTERPRISE_CREDS);

#define NET_REQUEST_WIFI_RTS_THRESHOLD_CONFIG                           \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_RTS_THRESHOLD_CONFIG);

#define NET_REQUEST_WIFI_WPS_CONFIG (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_WPS_CONFIG)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_WPS_CONFIG);
#ifdef CONFIG_WIFI_CREDENTIALS_CONNECT_STORED
#define NET_REQUEST_WIFI_CONNECT_STORED (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_CONNECT_STORED)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_CONNECT_STORED);
#endif

#define NET_REQUEST_WIFI_START_ROAMING                          \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_START_ROAMING)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_START_ROAMING);

#define NET_REQUEST_WIFI_NEIGHBOR_REP_COMPLETE                  \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_NEIGHBOR_REP_COMPLETE);

#define NET_REQUEST_WIFI_BSS_MAX_IDLE_PERIOD                            \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_BSS_MAX_IDLE_PERIOD);

#define NET_REQUEST_WIFI_BGSCAN                                 \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_BGSCAN)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_BGSCAN);

#define NET_REQUEST_WIFI_P2P_OPER                                               \
        (NET_WIFI_BASE | NET_REQUEST_WIFI_CMD_P2P_OPER)

NET_MGMT_DEFINE_REQUEST_HANDLER(NET_REQUEST_WIFI_P2P_OPER);


enum {
        NET_EVENT_WIFI_CMD_SCAN_RESULT_VAL,
        NET_EVENT_WIFI_CMD_SCAN_DONE_VAL,
        NET_EVENT_WIFI_CMD_CONNECT_RESULT_VAL,
        NET_EVENT_WIFI_CMD_DISCONNECT_RESULT_VAL,
        NET_EVENT_WIFI_CMD_IFACE_STATUS_VAL,
        NET_EVENT_WIFI_CMD_TWT_VAL,
        NET_EVENT_WIFI_CMD_TWT_SLEEP_STATE_VAL,
        NET_EVENT_WIFI_CMD_RAW_SCAN_RESULT_VAL,
        NET_EVENT_WIFI_CMD_DISCONNECT_COMPLETE_VAL,
        NET_EVENT_WIFI_CMD_SIGNAL_CHANGE_VAL,
        NET_EVENT_WIFI_CMD_NEIGHBOR_REP_RECEIVED_VAL,
        NET_EVENT_WIFI_CMD_NEIGHBOR_REP_COMPLETE_VAL,
        NET_EVENT_WIFI_CMD_AP_ENABLE_RESULT_VAL,
        NET_EVENT_WIFI_CMD_AP_DISABLE_RESULT_VAL,
        NET_EVENT_WIFI_CMD_AP_STA_CONNECTED_VAL,
        NET_EVENT_WIFI_CMD_AP_STA_DISCONNECTED_VAL,
        NET_EVENT_WIFI_CMD_SUPPLICANT_VAL,
        NET_EVENT_WIFI_CMD_P2P_DEVICE_FOUND_VAL,
        NET_EVENT_WIFI_CMD_NAN_DISCOVERY_RESULT_VAL,
        NET_EVENT_WIFI_CMD_NAN_REPLIED_VAL,
        NET_EVENT_WIFI_CMD_NAN_PUBLISH_TERMINATED_VAL,
        NET_EVENT_WIFI_CMD_NAN_SUBSCRIBE_TERMINATED_VAL,
        NET_EVENT_WIFI_CMD_NAN_RECEIVE_VAL,

        NET_EVENT_WIFI_CMD_MAX,
};

BUILD_ASSERT(NET_EVENT_WIFI_CMD_MAX <= NET_MGMT_MAX_COMMANDS,
             "Number of events in net_event_wifi_cmd exceeds the limit");


enum net_event_wifi_cmd {
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_SCAN_RESULT),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_SCAN_DONE),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_CONNECT_RESULT),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_DISCONNECT_RESULT),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_IFACE_STATUS),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_TWT),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_TWT_SLEEP_STATE),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_RAW_SCAN_RESULT),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_DISCONNECT_COMPLETE),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_SIGNAL_CHANGE),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_NEIGHBOR_REP_RECEIVED),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_NEIGHBOR_REP_COMPLETE),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_AP_ENABLE_RESULT),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_AP_DISABLE_RESULT),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_AP_STA_CONNECTED),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_AP_STA_DISCONNECTED),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_SUPPLICANT),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_P2P_DEVICE_FOUND),
#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_NAN_DISCOVERY_RESULT),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_NAN_REPLIED),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_NAN_PUBLISH_TERMINATED),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_NAN_SUBSCRIBE_TERMINATED),
        NET_MGMT_CMD(NET_EVENT_WIFI_CMD_NAN_RECEIVE),
#endif
};

#define NET_EVENT_WIFI_SCAN_RESULT                              \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SCAN_RESULT)

#define NET_EVENT_WIFI_SCAN_DONE                                \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SCAN_DONE)

#define NET_EVENT_WIFI_CONNECT_RESULT                           \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_CONNECT_RESULT)

#define NET_EVENT_WIFI_DISCONNECT_RESULT                        \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_DISCONNECT_RESULT)

#define NET_EVENT_WIFI_IFACE_STATUS                             \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_IFACE_STATUS)

#define NET_EVENT_WIFI_TWT                                      \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_TWT)

#define NET_EVENT_WIFI_TWT_SLEEP_STATE                          \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_TWT_SLEEP_STATE)

#define NET_EVENT_WIFI_RAW_SCAN_RESULT                          \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_RAW_SCAN_RESULT)

#define NET_EVENT_WIFI_DISCONNECT_COMPLETE                      \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_DISCONNECT_COMPLETE)

#define NET_EVENT_WIFI_SIGNAL_CHANGE                            \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_SIGNAL_CHANGE)

#define NET_EVENT_WIFI_NEIGHBOR_REP_COMP                        \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_NEIGHBOR_REP_COMPLETE)

#define NET_EVENT_WIFI_AP_ENABLE_RESULT                         \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_ENABLE_RESULT)

#define NET_EVENT_WIFI_AP_DISABLE_RESULT                        \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_DISABLE_RESULT)

#define NET_EVENT_WIFI_AP_STA_CONNECTED                         \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_STA_CONNECTED)

#define NET_EVENT_WIFI_AP_STA_DISCONNECTED                      \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_AP_STA_DISCONNECTED)

#define NET_EVENT_WIFI_P2P_DEVICE_FOUND                         \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_P2P_DEVICE_FOUND)

#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
#define WIFI_P2P_DEVICE_NAME_MAX_LEN 32
#define WIFI_P2P_PRI_DEV_TYPE_SIZE 8
#define WIFI_P2P_PRI_DEV_TYPE_STR_MAX_LEN 32
#define WIFI_P2P_CONFIG_METHODS_STR_MAX_LEN 16
#define WIFI_P2P_MANUFACTURER_MAX_LEN 64
#define WIFI_P2P_MODEL_NAME_MAX_LEN 32

struct wifi_p2p_device_info {
        uint8_t mac[WIFI_MAC_ADDR_LEN];
        char device_name[WIFI_P2P_DEVICE_NAME_MAX_LEN + 1];
        uint8_t pri_dev_type[WIFI_P2P_PRI_DEV_TYPE_SIZE];
        char pri_dev_type_str[WIFI_P2P_PRI_DEV_TYPE_STR_MAX_LEN];
        int8_t rssi;
        uint16_t config_methods;
        char config_methods_str[WIFI_P2P_CONFIG_METHODS_STR_MAX_LEN];
        uint8_t dev_capab;
        uint8_t group_capab;
        char manufacturer[WIFI_P2P_MANUFACTURER_MAX_LEN + 1];
        char model_name[WIFI_P2P_MODEL_NAME_MAX_LEN + 1];
};
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P */

#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN
#define NET_EVENT_WIFI_NAN_DISCOVERY_RESULT                     \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_NAN_DISCOVERY_RESULT)

#define NET_EVENT_WIFI_NAN_REPLIED                              \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_NAN_REPLIED)

#define NET_EVENT_WIFI_NAN_PUBLISH_TERMINATED                   \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_NAN_PUBLISH_TERMINATED)

#define NET_EVENT_WIFI_NAN_SUBSCRIBE_TERMINATED                 \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_NAN_SUBSCRIBE_TERMINATED)

#define NET_EVENT_WIFI_NAN_RECEIVE                              \
        (NET_WIFI_EVENT | NET_EVENT_WIFI_CMD_NAN_RECEIVE)
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN */

struct wifi_version {
        const char *drv_version;
        const char *fw_version;
};

struct wifi_band_channel {
        uint8_t band;
        uint8_t channel;
};

struct wifi_scan_params {
        enum wifi_scan_type scan_type;
        uint8_t bands;
        uint16_t dwell_time_active;
        uint16_t dwell_time_passive;
        const char *ssids[WIFI_MGMT_SCAN_SSID_FILT_MAX];
        uint16_t max_bss_cnt;
        struct wifi_band_channel band_chan[WIFI_MGMT_SCAN_CHAN_MAX_MANUAL];
};

struct wifi_scan_result {
        uint8_t ssid[WIFI_SSID_MAX_LEN + 1];
        uint8_t ssid_length;
        uint8_t band;
        uint8_t channel;
        enum wifi_security_type security;
        enum wifi_wpa3_enterprise_type wpa3_ent_type;
        enum wifi_mfp_options mfp;
        int8_t rssi;
        uint8_t mac[WIFI_MAC_ADDR_LEN];
        uint8_t mac_length;
};

struct wifi_connect_req_params {
        const uint8_t *ssid;
        uint8_t ssid_length; /* Max 32 */
        const uint8_t *psk;
        uint8_t psk_length; /* Min 8 - Max 64 */
        bool psk_is_pbkdf2;
        const uint8_t *sae_password;
        uint8_t sae_password_length; /* No length restrictions */
        uint8_t band;
        uint8_t channel;
        enum wifi_security_type security;
        enum wifi_mfp_options mfp;
        uint8_t bssid[WIFI_MAC_ADDR_LEN];
        int timeout;
        const uint8_t *anon_id;

        uint8_t aid_length;

        const uint8_t *key_passwd;

        uint8_t key_passwd_length;

        const uint8_t *key2_passwd;

        uint8_t key2_passwd_length;

        enum wifi_wpa3_enterprise_type wpa3_ent_mode;

        uint8_t TLS_cipher;

        int eap_ver;

        const uint8_t *eap_identity;

        uint8_t eap_id_length;

        const uint8_t *eap_password;

        uint8_t eap_passwd_length;

        bool verify_peer_cert;

        bool ft_used;

        int nusers;

        uint8_t passwds;

        const uint8_t *identities[WIFI_ENT_IDENTITY_MAX_USERS];

        const uint8_t *passwords[WIFI_ENT_IDENTITY_MAX_USERS];
        uint8_t ignore_broadcast_ssid;
        enum wifi_frequency_bandwidths bandwidth;

        const uint8_t *server_cert_domain_exact;
        uint8_t server_cert_domain_exact_len;

        const uint8_t *server_cert_domain_suffix;
        uint8_t server_cert_domain_suffix_len;
        uint8_t ssid_protection;
        uint8_t transition_disable;
};

enum wifi_disconn_reason {
        WIFI_REASON_DISCONN_SUCCESS = 0,
        WIFI_REASON_DISCONN_UNSPECIFIED,
        WIFI_REASON_DISCONN_USER_REQUEST,
        WIFI_REASON_DISCONN_AP_LEAVING,
        WIFI_REASON_DISCONN_INACTIVITY,
};

const char *wifi_disconn_reason_txt(enum wifi_disconn_reason reason);

enum wifi_ap_status {
        WIFI_STATUS_AP_SUCCESS = 0,
        WIFI_STATUS_AP_FAIL,
        WIFI_STATUS_AP_CHANNEL_NOT_SUPPORTED,
        WIFI_STATUS_AP_CHANNEL_NOT_ALLOWED,
        WIFI_STATUS_AP_SSID_NOT_ALLOWED,
        WIFI_STATUS_AP_AUTH_TYPE_NOT_SUPPORTED,
        WIFI_STATUS_AP_OP_NOT_SUPPORTED,
        WIFI_STATUS_AP_OP_NOT_PERMITTED,
};

struct wifi_status {
        union {
                int status;
                enum wifi_conn_status conn_status;
                enum wifi_disconn_reason disconn_reason;
                enum wifi_ap_status ap_status;
        };
        uint16_t status_code;
        uint16_t reason_code;
};

struct wifi_iface_status {
        int state;
        unsigned int ssid_len;
        char ssid[WIFI_SSID_MAX_LEN + 1];
        char bssid[WIFI_MAC_ADDR_LEN];
        enum wifi_frequency_bands band;
        unsigned int channel;
        enum wifi_iface_mode iface_mode;
        enum wifi_link_mode link_mode;
        enum wifi_wpa3_enterprise_type wpa3_ent_type;
        enum wifi_security_type security;
        enum wifi_wep_key_type wep_key_type;
        enum wifi_mfp_options mfp;
        int rssi;
        unsigned char dtim_period;
        unsigned short beacon_interval;
        bool twt_capable;
        float current_phy_tx_rate;
};

struct wifi_ps_params {
        enum wifi_ps enabled;
        unsigned short listen_interval;
        enum wifi_ps_wakeup_mode wakeup_mode;
        enum wifi_ps_mode mode;
        unsigned int timeout_ms;
        enum wifi_ps_param_type type;
        enum wifi_config_ps_param_fail_reason fail_reason;
        enum wifi_ps_exit_strategy exit_strategy;
};

#define WIFI_BTWT_AGREEMENT_MAX 5

struct wifi_btwt_params {
        uint8_t btwt_id;
        uint16_t btwt_mantissa;
        uint8_t btwt_exponent;
        uint8_t btwt_nominal_wake;
};

struct wifi_twt_params {
        enum wifi_twt_operation operation;
        enum wifi_twt_negotiation_type negotiation_type;
        enum wifi_twt_setup_cmd setup_cmd;
        enum wifi_twt_setup_resp_status resp_status;
        enum wifi_twt_teardown_status teardown_status;
        uint8_t dialog_token;
        uint8_t flow_id;
        union {
                struct {
                        uint64_t twt_interval;
                        bool responder;
                        bool trigger;
                        bool implicit;
                        bool announce;
                        uint32_t twt_wake_interval;
                        uint32_t twt_wake_ahead_duration;
                        bool twt_info_disable;
                        uint8_t twt_exponent;
                        uint16_t twt_mantissa;
                } setup;
                struct {
                        uint8_t btwt_sta_wait;
                        uint16_t btwt_offset;
                        uint8_t btwt_li;
                        uint8_t btwt_count;
                        struct wifi_btwt_params btwt_set_cfg[WIFI_BTWT_AGREEMENT_MAX];
                } btwt;
                struct {
                        bool teardown_all;
                } teardown;
        };
        enum wifi_twt_fail_reason fail_reason;
};


/* Flow ID is only 3 bits */
#define WIFI_MAX_TWT_FLOWS 8
/* The TWT interval is encoded per IEEE 802.11 as mantissa * 2^exponent
 * micro-seconds, with a 16-bit mantissa and a 5-bit exponent. The maximum
 * representable interval is therefore UINT16_MAX * 2^WIFI_MAX_TWT_EXPONENT us.
 */
#define WIFI_MAX_TWT_EXPONENT 31
#define WIFI_MAX_TWT_INTERVAL_US ((uint64_t)UINT16_MAX << WIFI_MAX_TWT_EXPONENT)
/* 256 (u8) * 1TU */
#define WIFI_MAX_TWT_WAKE_INTERVAL_US 262144
#define WIFI_MAX_TWT_WAKE_AHEAD_DURATION_US (LONG_MAX - 1)


struct wifi_twt_flow_info {
        uint64_t  twt_interval;
        uint8_t dialog_token;
        uint8_t flow_id;
        enum wifi_twt_negotiation_type negotiation_type;
        bool responder;
        bool trigger;
        bool implicit;
        bool announce;
        uint32_t twt_wake_interval;
        uint32_t twt_wake_ahead_duration;
};

struct wifi_enterprise_creds_params {
        uint8_t *ca_cert;
        uint32_t ca_cert_len;
        uint8_t *client_cert;
        uint32_t client_cert_len;
        uint8_t *client_key;
        uint32_t client_key_len;
        uint8_t *ca_cert2;
        uint32_t ca_cert2_len;
        uint8_t *client_cert2;
        uint32_t client_cert2_len;
        uint8_t *client_key2;
        uint32_t client_key2_len;
        uint8_t *server_cert;
        uint32_t server_cert_len;
        uint8_t *server_key;
        uint32_t server_key_len;
        uint8_t *dh_param;
        uint32_t dh_param_len;
};

struct wifi_ps_config {
        char num_twt_flows;
        struct wifi_twt_flow_info twt_flows[WIFI_MAX_TWT_FLOWS];
        struct wifi_ps_params ps_params;
};

enum wifi_mgmt_op {
        WIFI_MGMT_GET = 0,
        WIFI_MGMT_SET = 1,
};

struct wifi_11k_params {
        enum wifi_mgmt_op oper;
        bool enable_11k;
        uint8_t ssid[WIFI_SSID_MAX_LEN + 1];
};

#define MAX_REG_CHAN_NUM  42

struct wifi_reg_chan_info {
        unsigned short center_frequency;
        unsigned short max_power:8;
        unsigned short supported:1;
        unsigned short passive_only:1;
        unsigned short dfs:1;
} __packed;

struct wifi_reg_domain {
        enum wifi_mgmt_op oper;
        bool force;
        uint8_t country_code[WIFI_COUNTRY_CODE_LEN];
        unsigned int num_channels;
        struct wifi_reg_chan_info *chan_info;
};

enum wifi_twt_sleep_state {
        WIFI_TWT_STATE_SLEEP = 0,
        WIFI_TWT_STATE_AWAKE = 1,
};

#if defined(CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS) || defined(__DOXYGEN__)
struct wifi_raw_scan_result {
        int8_t rssi;
        int frame_length;
        unsigned short frequency;
        uint8_t data[CONFIG_WIFI_MGMT_RAW_SCAN_RESULT_LENGTH];
};
#endif /* CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS */

struct wifi_ap_sta_info {
        enum wifi_link_mode link_mode;
        uint8_t mac[WIFI_MAC_ADDR_LEN];
        uint8_t mac_length;
        bool twt_capable;
};

#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN
struct wifi_nan_discovery_result_event {
        uint8_t subscribe_id;
        uint8_t publish_id;
        uint8_t peer_addr[WIFI_MAC_ADDR_LEN];
        bool fsd;
        bool fsd_gas;
        uint8_t srv_proto_type;
        size_t ssi_len;
        uint8_t ssi[WIFI_NAN_MAX_SSI_LEN];
};

struct wifi_nan_replied_event {
        uint8_t publish_id;
        uint8_t peer_addr[WIFI_MAC_ADDR_LEN];
        uint8_t subscribe_id;
        uint8_t srv_proto_type;
        size_t ssi_len;
        uint8_t ssi[WIFI_NAN_MAX_SSI_LEN];
};

struct wifi_nan_terminated_event {
        uint8_t id;
        char reason[32];
};

struct wifi_nan_receive_event {
        uint8_t id;
        uint8_t peer_instance_id;
        uint8_t peer_addr[WIFI_MAC_ADDR_LEN];
        uint8_t ssi[WIFI_NAN_MAX_SSI_LEN];
        size_t ssi_len;
};
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN */


/* for use in max info size calculations */
union wifi_mgmt_events {
        struct wifi_scan_result scan_result;
        struct wifi_status connect_status;
        struct wifi_iface_status iface_status;
#ifdef CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS
        struct wifi_raw_scan_result raw_scan_result;
#endif /* CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS */
        struct wifi_twt_params twt_params;
        struct wifi_ap_sta_info ap_sta_info;
#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
        struct wifi_p2p_device_info p2p_device_info;
#endif
#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN
        struct wifi_nan_discovery_result_event nan_discovery_result;
        struct wifi_nan_replied_event nan_replied;
        struct wifi_nan_terminated_event nan_publish_terminated;
        struct wifi_nan_terminated_event nan_subscribe_terminated;
        struct wifi_nan_receive_event nan_receive;
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN */
};


struct wifi_mode_info {
        uint8_t mode;
        uint8_t if_index;
        enum wifi_mgmt_op oper;
};

struct wifi_filter_info {
        uint8_t filter;
        uint8_t if_index;
        uint16_t buffer_size;
        enum wifi_mgmt_op oper;
};

struct wifi_channel_info {
        uint16_t channel;
        enum wifi_frequency_bands band;
        uint8_t if_index;
        enum wifi_mgmt_op oper;
};

#define WIFI_AP_STA_MAX_INACTIVITY (LONG_MAX - 1)
#define WIFI_AP_IEEE_80211_CAPAB_MAX_LEN 64

struct wifi_ap_config_params {
        enum wifi_ap_config_param type;
        uint32_t max_inactivity;
        uint32_t max_num_sta;
        enum wifi_frequency_bandwidths bandwidth;
#if defined(CONFIG_WIFI_NM_HOSTAPD_AP)
        char ht_capab[WIFI_AP_IEEE_80211_CAPAB_MAX_LEN + 1];
        char vht_capab[WIFI_AP_IEEE_80211_CAPAB_MAX_LEN + 1];
#endif
};

struct wifi_config_params {
        enum wifi_config_param type;
        int okc;
};

#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
#define WIFI_DPP_QRCODE_MAX_LEN 255

enum wifi_dpp_op {
        WIFI_DPP_OP_INVALID = 0,
        WIFI_DPP_CONFIGURATOR_ADD,
        WIFI_DPP_AUTH_INIT,
        WIFI_DPP_QR_CODE,
        WIFI_DPP_CHIRP,
        WIFI_DPP_LISTEN,
        WIFI_DPP_BOOTSTRAP_GEN,
        WIFI_DPP_BOOTSTRAP_GET_URI,
        WIFI_DPP_SET_CONF_PARAM,
        WIFI_DPP_SET_WAIT_RESP_TIME,
        WIFI_DPP_RECONFIG
};

enum wifi_dpp_curves {
        WIFI_DPP_CURVES_DEFAULT = 0,
        WIFI_DPP_CURVES_P_256,
        WIFI_DPP_CURVES_P_384,
        WIFI_DPP_CURVES_P_512,
        WIFI_DPP_CURVES_BP_256,
        WIFI_DPP_CURVES_BP_384,
        WIFI_DPP_CURVES_BP_512
};

enum wifi_dpp_role {
        WIFI_DPP_ROLE_UNSET = 0,
        WIFI_DPP_ROLE_CONFIGURATOR,
        WIFI_DPP_ROLE_ENROLLEE,
        WIFI_DPP_ROLE_EITHER
};

enum wifi_dpp_conf {
        WIFI_DPP_CONF_UNSET = 0,
        WIFI_DPP_CONF_STA,
        WIFI_DPP_CONF_AP,
        WIFI_DPP_CONF_QUERY
};

enum wifi_dpp_bootstrap_type {
        WIFI_DPP_BOOTSTRAP_TYPE_UNSET = 0,
        WIFI_DPP_BOOTSTRAP_TYPE_QRCODE,
        WIFI_DPP_BOOTSTRAP_TYPE_PKEX,
        WIFI_DPP_BOOTSTRAP_TYPE_NFC_URI
};

struct wifi_dpp_configurator_add_params {
        int curve;
        int net_access_key_curve;
};

struct wifi_dpp_auth_init_params {
        int peer;
        int configurator;
        int role;
        int conf;
        char ssid[WIFI_SSID_MAX_LEN + 1];
};

struct wifi_dpp_chirp_params {
        int id;
        int freq;
};

struct wifi_dpp_listen_params {
        int freq;
        int role;
};

struct wifi_dpp_bootstrap_gen_params {
        int type;
        int op_class;
        int chan;
        int curve;
        uint8_t mac[WIFI_MAC_ADDR_LEN];
};

struct wifi_dpp_configurator_set_params {
        int peer;
        int configurator;
        int role;
        int conf;
        int curve;
        int net_access_key_curve;
        char ssid[WIFI_SSID_MAX_LEN + 1];
};

struct wifi_dpp_params {
        int action;
        union {
                struct wifi_dpp_configurator_add_params configurator_add;
                struct wifi_dpp_auth_init_params auth_init;
                struct wifi_dpp_chirp_params chirp;
                struct wifi_dpp_listen_params listen;
                struct wifi_dpp_bootstrap_gen_params bootstrap_gen;
                struct wifi_dpp_configurator_set_params configurator_set;
                int id;
                int dpp_resp_wait_time;
                int network_id;
                uint8_t dpp_qr_code[WIFI_DPP_QRCODE_MAX_LEN + 1];
                char resp[WIFI_DPP_QRCODE_MAX_LEN + 1];
        };
};
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP */

#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN
enum wifi_nan_operation {
        WIFI_NAN_OP_START,
        WIFI_NAN_OP_STOP,
        WIFI_NAN_OP_SET,
        WIFI_NAN_OP_UPDATE_CONF,
        WIFI_NAN_OP_STATUS,
        WIFI_NAN_OP_PUBLISH,
        WIFI_NAN_OP_CANCEL_PUBLISH,
        WIFI_NAN_OP_UPDATE_PUBLISH,
        WIFI_NAN_OP_SUBSCRIBE,
        WIFI_NAN_OP_CANCEL_SUBSCRIBE,
        WIFI_NAN_OP_TRANSMIT,
};

enum wifi_nan_service_protocol_type {
        WIFI_NAN_SRV_PROTO_BONJOUR = 1,
        WIFI_NAN_SRV_PROTO_GENERIC = 2,
        WIFI_NAN_SRV_PROTO_CSA_MATTER = 3,
};

struct wifi_nan_publish_params {
        /* Service name for NAN */
        char service_name[WIFI_NAN_MAX_SERVICE_NAME_LEN];
        /* NAN service protocol type */
        enum wifi_nan_service_protocol_type srv_proto_type;
        /* Time to live (in seconds); 0 = one TX only */
        uint32_t ttl;
        /* Default frequency in MHz (defaultPublishChannel) */
        uint32_t freq;
        /* Multi-channel frequencies */
        char freq_list[64];
        /* Service specific information (binary data) */
        uint8_t ssi[WIFI_NAN_MAX_SSI_LEN];
        /* Actual length of SSI data */
        uint16_t ssi_len;
        /* Unsolicited transmission (true by default) */
        bool unsolicited;
        /* Solicited transmission (true by default) */
        bool solicited;
        /* Further Service Discovery (true by default) */
        bool fsd;
};

/* This structure is used to configure nan update publish parameters */
struct wifi_nan_update_publish_params {
        uint8_t publish_id;
        /* Service specific information (binary data) */
        uint8_t ssi[WIFI_NAN_MAX_SSI_LEN];
        /* Actual length of SSI data */
        uint16_t ssi_len;
};

struct wifi_nan_subscribe_params {
        /* Service name for NAN */
        char service_name[WIFI_NAN_MAX_SERVICE_NAME_LEN];
        /* NAN service protocol type */
        enum wifi_nan_service_protocol_type srv_proto_type;
        /* Subscribe type */
        bool active;
        /* Time to live (in seconds); 0 = until first result */
        unsigned int ttl;
        /* Selected frequency in MHz */
        unsigned int freq;
        /* Service specific information (binary data) */
        uint8_t ssi[WIFI_NAN_MAX_SSI_LEN];
        /* Actual length of SSI data */
        uint16_t ssi_len;
};

struct wifi_nan_transmit_params {
        /* publish_id or subscribe_id */
        uint8_t handle;
        /* peer publish_id or subscribe_id */
        uint8_t req_instance_id;
        /* peer MAC address */
        uint8_t peer_addr[WIFI_MAC_ADDR_LEN];
        /* Service specific information (binary data) */
        uint8_t ssi[WIFI_NAN_MAX_SSI_LEN];
        /* Actual length of SSI data */
        uint16_t ssi_len;
};

struct wifi_nan_set_params {
        char param[WIFI_NAN_MAX_SET_PARAM_LEN];
        char value[WIFI_NAN_MAX_SET_VALUE_LEN];
};

struct wifi_nan_params {
        enum wifi_nan_operation op;

        union {
                struct wifi_nan_publish_params publish;
                struct wifi_nan_update_publish_params update_publish;
                struct wifi_nan_subscribe_params subscribe;
                struct wifi_nan_transmit_params transmit;
                struct wifi_nan_set_params set;
                uint8_t cancel_id;
        };

        /* Operation response */
        char resp[WIFI_NAN_RESP_SIZE];
};

#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN */


#define WIFI_WPS_PIN_MAX_LEN 8

enum wifi_wps_op {
        WIFI_WPS_PBC = 0,
        WIFI_WPS_PIN_GET = 1,
        WIFI_WPS_PIN_SET = 2,
};

struct wifi_wps_config_params {
        enum wifi_wps_op oper;
        char pin[WIFI_WPS_PIN_MAX_LEN + 1];
};

#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
enum wifi_p2p_op {
        WIFI_P2P_FIND = 0,
        WIFI_P2P_STOP_FIND,
        WIFI_P2P_PEER,
        WIFI_P2P_CONNECT,
        WIFI_P2P_GROUP_ADD,
        WIFI_P2P_GROUP_REMOVE,
        WIFI_P2P_INVITE,
        WIFI_P2P_POWER_SAVE,
        WIFI_P2P_LIST_NETWORKS,
        WIFI_P2P_PERSISTENT_REMOVE,
        WIFI_P2P_SET_DEV_NAME,
        WIFI_P2P_STATUS,
};

enum wifi_p2p_discovery_type {
        WIFI_P2P_FIND_START_WITH_FULL = 0,
        WIFI_P2P_FIND_ONLY_SOCIAL,
        WIFI_P2P_FIND_PROGRESSIVE,
};

enum wifi_p2p_connection_method {
        WIFI_P2P_METHOD_PBC = 0,
        WIFI_P2P_METHOD_DISPLAY,
        WIFI_P2P_METHOD_KEYPAD,
};

#define WIFI_P2P_MAX_PEERS CONFIG_WIFI_P2P_MAX_PEERS
#define WIFI_P2P_LIST_NETWORKS_BUF_SIZE 2048
#define WIFI_P2P_STATUS_BUF_SIZE 512

struct wifi_p2p_params {
        enum wifi_p2p_op oper;
        char device_name[WIFI_P2P_DEVICE_NAME_MAX_LEN + 1];
        enum wifi_p2p_discovery_type discovery_type;
        uint16_t timeout;
        uint8_t peer_addr[WIFI_MAC_ADDR_LEN];
        bool discovered_only;
        struct wifi_p2p_device_info *peers;
        uint16_t peer_count;
        bool power_save;
        struct {
                enum wifi_p2p_connection_method method;
                char pin[WIFI_WPS_PIN_MAX_LEN + 1];
                uint8_t go_intent;
                unsigned int freq;
                bool join;
                bool persistent_set;
        } connect;
        struct {
                int freq;
                int persistent;
                bool persistent_set;
                bool ht40;
                bool vht;
                bool he;
                bool edmg;
                uint8_t go_bssid[WIFI_MAC_ADDR_LEN];
                uint8_t go_bssid_length;
        } group_add;
        struct {
                char ifname[CONFIG_NET_INTERFACE_NAME_LEN + 1];
        } group_remove;
        struct {
                enum {
                        WIFI_P2P_INVITE_PERSISTENT = 0,
                        WIFI_P2P_INVITE_GROUP,
                } type;
                int persistent_id;
                char group_ifname[CONFIG_NET_INTERFACE_NAME_LEN + 1];
                uint8_t peer_addr[WIFI_MAC_ADDR_LEN];
                int freq;
                uint8_t go_dev_addr[WIFI_MAC_ADDR_LEN];
                uint8_t go_dev_addr_length;
        } invite;
        struct {
                char *buf;
                size_t buf_size;
        } list_networks;
        struct {
                int id;
        } persistent_remove;
        struct {
                char *buf;
                size_t buf_size;
        } status;
};
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P */

enum wifi_sap_iface_state {
        WIFI_SAP_IFACE_UNINITIALIZED,
        WIFI_SAP_IFACE_DISABLED,
        WIFI_SAP_IFACE_COUNTRY_UPDATE,
        WIFI_SAP_IFACE_ACS,
        WIFI_SAP_IFACE_HT_SCAN,
        WIFI_SAP_IFACE_DFS,
        WIFI_SAP_IFACE_NO_IR,
        WIFI_SAP_IFACE_ENABLED
};

#if defined(CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN) || defined(__DOXYGEN__)
enum wifi_bgscan_type {
        WIFI_BGSCAN_NONE = 0,
        WIFI_BGSCAN_SIMPLE,
        WIFI_BGSCAN_LEARN,
};

struct wifi_bgscan_params {
        enum wifi_bgscan_type type;
        uint16_t short_interval;
        uint16_t long_interval;
        int8_t rssi_threshold;
        uint16_t btm_queries;
};
#endif

enum wifi_ext_capab {
        WIFI_EXT_CAPAB_20_40_COEX = 0,
        WIFI_EXT_CAPAB_GLK = 1,
        WIFI_EXT_CAPAB_EXT_CHAN_SWITCH = 2,
        WIFI_EXT_CAPAB_TIM_BROADCAST = 18,
        WIFI_EXT_CAPAB_BSS_TRANSITION = 19,
};

#include <zephyr/net/net_if.h>

typedef void (*scan_result_cb_t)(struct net_if *iface, int status,
                                 struct wifi_scan_result *entry);

#ifdef CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS
typedef void (*raw_scan_result_cb_t)(struct net_if *iface, int status,
                                     struct wifi_raw_scan_result *entry);
#endif /* CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS */

struct wifi_mgmt_ops {
        int (*scan)(const struct device *dev,
                    struct net_if *iface,
                    struct wifi_scan_params *params,
                    scan_result_cb_t cb);
        int (*connect)(const struct device *dev,
                       struct net_if *iface,
                       struct wifi_connect_req_params *params);
        int (*disconnect)(const struct device *dev,
                          struct net_if *iface);
        int (*ap_enable)(const struct device *dev,
                         struct net_if *iface,
                         struct wifi_connect_req_params *params);
        int (*ap_disable)(const struct device *dev, struct net_if *iface);
        int (*ap_sta_disconnect)(const struct device *dev, struct net_if *iface,
                                 const uint8_t *mac);
        int (*iface_status)(const struct device *dev,
                            struct net_if *iface,
                            struct wifi_iface_status *status);
#if defined(CONFIG_NET_STATISTICS_WIFI) || defined(__DOXYGEN__)
        int (*get_stats)(const struct device *dev,
                         struct net_if *iface,
                         struct net_stats_wifi *stats);
        int (*reset_stats)(const struct device *dev, struct net_if *iface);
#endif /* CONFIG_NET_STATISTICS_WIFI */
        int (*cfg_11k)(const struct device *dev,
                       struct net_if *iface,
                       struct wifi_11k_params *params);
        int (*send_11k_neighbor_request)(const struct device *dev,
                                         struct net_if *iface,
                                         struct wifi_11k_params *params);
        int (*set_power_save)(const struct device *dev,
                              struct net_if *iface,
                              struct wifi_ps_params *params);
        int (*set_twt)(const struct device *dev,
                       struct net_if *iface,
                       struct wifi_twt_params *params);
        int (*set_btwt)(const struct device *dev,
                        struct net_if *iface,
                        struct wifi_twt_params *params);
        int (*get_power_save_config)(const struct device *dev,
                                     struct net_if *iface,
                                     struct wifi_ps_config *config);
        int (*reg_domain)(const struct device *dev,
                          struct net_if *iface,
                          struct wifi_reg_domain *reg_domain);
        int (*filter)(const struct device *dev,
                      struct net_if *iface,
                      struct wifi_filter_info *filter);
        int (*mode)(const struct device *dev, struct net_if *iface, struct wifi_mode_info *mode);
        int (*channel)(const struct device *dev,
                       struct net_if *iface,
                       struct wifi_channel_info *channel);

        int (*btm_query)(const struct device *dev, struct net_if *iface, uint8_t reason);

        bool (*bss_support_neighbor_rep)(const struct device *dev, struct net_if *iface);

        int (*bss_ext_capab)(const struct device *dev, struct net_if *iface, int capab);

        int (*legacy_roam)(const struct device *dev, struct net_if *iface);

        int (*get_version)(const struct device *dev,
                           struct net_if *iface,
                           struct wifi_version *params);
        int (*get_conn_params)(const struct device *dev,
                               struct net_if *iface,
                               struct wifi_connect_req_params *params);
        int (*set_rts_threshold)(const struct device *dev,
                                 struct net_if *iface,
                                 unsigned int rts_threshold);
        int (*ap_config_params)(const struct device *dev,
                                struct net_if *iface,
                                struct wifi_ap_config_params *params);
        int (*config_params)(const struct device *dev,
                             struct net_if *iface,
                             struct wifi_config_params *params);
#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP
        int (*dpp_dispatch)(const struct device *dev,
                            struct net_if *iface,
                            struct wifi_dpp_params *params);
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP */
#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN
        int (*nan_cfg)(const struct device *dev,
                       struct net_if *iface,
                       struct wifi_nan_params *params);
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN */

        int (*pmksa_flush)(const struct device *dev, struct net_if *iface);
#ifdef CONFIG_WIFI_CERTIFICATE_LIB
        int (*enterprise_creds)(const struct device *dev,
                                struct net_if *iface,
                                struct wifi_enterprise_creds_params *creds);
#endif
        int (*get_rts_threshold)(const struct device *dev,
                                 struct net_if *iface,
                                 unsigned int *rts_threshold);
        int (*wps_config)(const struct device *dev,
                          struct net_if *iface,
                          struct wifi_wps_config_params *params);
        int (*candidate_scan)(const struct device *dev,
                              struct net_if *iface,
                              struct wifi_scan_params *params);
        __deprecated int (*start_11r_roaming)(const struct device *dev, struct net_if *iface);
        int (*set_bss_max_idle_period)(const struct device *dev,
                                       struct net_if *iface,
                                       unsigned short bss_max_idle_period);
#if defined(CONFIG_WIFI_NM_WPA_SUPPLICANT_BGSCAN) || defined(__DOXYGEN__)
        int (*set_bgscan)(const struct device *dev,
                          struct net_if *iface,
                          struct wifi_bgscan_params *params);
#endif
#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
        int (*p2p_oper)(const struct device *dev,
                        struct net_if *iface,
                        struct wifi_p2p_params *params);
#endif
         uint32_t (*get_iface_caps)(const struct device *dev, struct net_if *iface);
};

struct net_wifi_mgmt_offload {
#if defined(CONFIG_WIFI_USE_NATIVE_NETWORKING) || defined(__DOXYGEN__)
        struct ethernet_api wifi_iface;
#else
        struct offloaded_if_api wifi_iface;
#endif
        const struct wifi_mgmt_ops *const wifi_mgmt_api;

#if defined(CONFIG_WIFI_NM_WPA_SUPPLICANT) || defined(__DOXYGEN__)
        const void *wifi_drv_ops;
#endif
};

#if defined(CONFIG_WIFI_NM_WPA_SUPPLICANT)
/* Make sure wifi_drv_ops is after wifi_mgmt_api */
BUILD_ASSERT(offsetof(struct net_wifi_mgmt_offload, wifi_mgmt_api) <
             offsetof(struct net_wifi_mgmt_offload, wifi_drv_ops));
#endif

/* Make sure that the network interface API is properly setup inside
 * Wifi mgmt offload API struct (it is the first one).
 */
BUILD_ASSERT(offsetof(struct net_wifi_mgmt_offload, wifi_iface) == 0);

void wifi_mgmt_raise_connect_result_event(struct net_if *iface, int status);

void wifi_mgmt_raise_connect_result_status_event(struct net_if *iface,
                                                 const struct wifi_status *status);

void wifi_mgmt_raise_disconnect_result_event(struct net_if *iface, int status);

void wifi_mgmt_raise_disconnect_result_status_event(struct net_if *iface,
                                                    const struct wifi_status *status);

void wifi_mgmt_raise_iface_status_event(struct net_if *iface,
                struct wifi_iface_status *iface_status);

void wifi_mgmt_raise_twt_event(struct net_if *iface,
                struct wifi_twt_params *twt_params);

void wifi_mgmt_raise_twt_sleep_state(struct net_if *iface, int twt_sleep_state);

#if defined(CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS) || defined(__DOXYGEN__)
void wifi_mgmt_raise_raw_scan_result_event(struct net_if *iface,
                struct wifi_raw_scan_result *raw_scan_info);
#endif /* CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS */

void wifi_mgmt_raise_disconnect_complete_event(struct net_if *iface, int status);

#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_ROAMING
void wifi_mgmt_raise_neighbor_rep_recv_event(struct net_if *iface,
                                             char *inbuf, size_t buf_len);
#endif

void wifi_mgmt_raise_ap_enable_result_event(struct net_if *iface, enum wifi_ap_status status);

void wifi_mgmt_raise_ap_disable_result_event(struct net_if *iface, enum wifi_ap_status status);

void wifi_mgmt_raise_ap_sta_connected_event(struct net_if *iface,
                struct wifi_ap_sta_info *sta_info);

void wifi_mgmt_raise_ap_sta_disconnected_event(struct net_if *iface,
                struct wifi_ap_sta_info *sta_info);

#ifdef CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P
void wifi_mgmt_raise_p2p_device_found_event(struct net_if *iface,
                struct wifi_p2p_device_info *peer_info);
#endif /* CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_WIFI_MGMT_H_ */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Intel Corporation.。

版权（Copyright）：2024 NXP。

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 32 行

管理部分定义（management part definitions）。

### 注释 3：原第 47 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_MGMT_SCAN_SSID_FILT_MAX`。

### 注释 4：原第 53 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_MGMT_SCAN_CHAN_MAX_MANUAL`。

### 注释 5：原第 59 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_ENT_IDENTITY_MAX_USERS`。

### 注释 6：原第 69 行

保存 hostap 输出的多行 `NAN_STATUS`。

### 注释 7：原第 73 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN`。

### 注释 8：原第 305 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP`。

### 注释 9：原第 313 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN`。

### 注释 10：原第 570 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`。

### 注释 11：原第 592 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN`。

### 注释 12：原第 695 行

最大值为 32（Max 32）。

### 注释 13：原第 699 行

最小值为 8，最大值为 64（Min 8 – Max 64）。

### 注释 14：原第 709 行

没有长度限制（No Length Restrictions）。

### 注释 15：原第 1096 行

流标识（Flow ID）只有 3 位。

### 注释 16：原第 1098 行

目标唤醒时间（TWT）间隔按 IEEE 802.11 编码为 `mantissa * 2^exponent` 微秒，其中尾数（Mantissa）为 16 位，指数（Exponent）为 5 位。因此，能够表示的最大间隔为 `UINT16_MAX * 2^WIFI_MAX_TWT_EXPONENT` 微秒。

### 注释 17：原第 1104 行

`256 (u8) * 1TU`，以时间单位（TU）计。

### 注释 18：原第 1255 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS`。

### 注释 19：原第 1327 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN`。

### 注释 20：原第 1331 行

用于计算最大信息大小（Maximum Information Size）。

### 注释 21：原第 1338 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS`。

### 注释 22：原第 1350 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN`。

### 注释 23：原第 1617 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP`。

### 注释 24：原第 1647 行

邻居感知网络（NAN）的服务名称（Service Name）。

### 注释 25：原第 1649 行

NAN 服务协议类型（Service Protocol Type）。

### 注释 26：原第 1651 行

生存时间（Time to Live），单位为秒；0 表示仅发送一次（One TX Only）。

### 注释 27：原第 1653 行

默认频率（Default Frequency），单位为 MHz，对应 `defaultPublishChannel`。

### 注释 28：原第 1655 行

多信道频率（Multi-channel Frequencies）。

### 注释 29：原第 1657 行

服务专用信息（Service Specific Information），采用二进制数据。

### 注释 30：原第 1659 行

服务专用信息（SSI）数据的实际长度。

### 注释 31：原第 1661 行

非请求发送（Unsolicited Transmission），默认值为 `true`。

### 注释 32：原第 1663 行

请求式发送（Solicited Transmission），默认值为 `true`。

### 注释 33：原第 1665 行

进一步服务发现（Further Service Discovery），默认值为 `true`。

### 注释 34：原第 1669 行

此结构体用于配置 NAN 更新发布参数（Update Publish Parameters）。

### 注释 35：原第 1672 行

服务专用信息（Service Specific Information），采用二进制数据。

### 注释 36：原第 1674 行

服务专用信息（SSI）数据的实际长度。

### 注释 37：原第 1680 行

邻居感知网络（NAN）的服务名称（Service Name）。

### 注释 38：原第 1682 行

NAN 服务协议类型（Service Protocol Type）。

### 注释 39：原第 1684 行

订阅类型（Subscribe Type）。

### 注释 40：原第 1686 行

生存时间（Time to Live），单位为秒；0 表示持续到获得第一个结果。

### 注释 41：原第 1688 行

选定频率（Selected Frequency），单位为 MHz。

### 注释 42：原第 1690 行

服务专用信息（Service Specific Information），采用二进制数据。

### 注释 43：原第 1692 行

服务专用信息（SSI）数据的实际长度。

### 注释 44：原第 1698 行

本端的 `publish_id` 或 `subscribe_id`。

### 注释 45：原第 1700 行

对端的 `publish_id` 或 `subscribe_id`。

### 注释 46：原第 1702 行

对端 MAC 地址（Peer MAC Address）。

### 注释 47：原第 1704 行

服务专用信息（Service Specific Information），采用二进制数据。

### 注释 48：原第 1706 行

服务专用信息（SSI）数据的实际长度。

### 注释 49：原第 1739 行

操作响应（Operation Response）。

### 注释 50：原第 1743 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN`。

### 注释 51：原第 1930 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`。

### 注释 52：原第 2013 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS`。

### 注释 53：原第 2112 行

条件编译配置（Configuration）标记：`CONFIG_NET_STATISTICS_WIFI`。

### 注释 54：原第 2331 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP`。

### 注释 55：原第 2344 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_NAN`。

### 注释 56：原第 2487 行

确保 `wifi_drv_ops` 位于 `wifi_mgmt_api` 之后。

### 注释 57：原第 2492 行

确保 Wi-Fi 管理卸载 API 结构体（Wi-Fi Management Offload API Struct）中的网络接口 API 正确设置，且位于第一个成员。

### 注释 58：原第 2564 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_MGMT_RAW_SCAN_RESULTS`。

### 注释 59：原第 2622 行

条件编译配置（Configuration）标记：`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`。

### 注释 60：原第 2631 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_WIFI_MGMT_H_`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [zephyr/net/wifi.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html)
- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [zephyr/net/offloaded_netdev.h](../api_file_runtime_reference/P049_zephyr__net__offloaded_netdev.h_文件参考.md)
- [net_request_wifi_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga99a55137188119f65f9d2bb4f57cac77)
- [NET_REQUEST_WIFI_CMD_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)
- [NET_REQUEST_WIFI_CMD_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)
- [NET_REQUEST_WIFI_CMD_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)
- [NET_REQUEST_WIFI_CMD_AP_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)
- [NET_REQUEST_WIFI_CMD_AP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)
- [NET_REQUEST_WIFI_CMD_AP_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a40104910a4d0258f63a03851de929474)
- [NET_REQUEST_WIFI_CMD_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)
- [NET_REQUEST_WIFI_CMD_11K_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6)
- [NET_REQUEST_WIFI_CMD_11K_NEIGHBOR_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede)
- [NET_REQUEST_WIFI_CMD_PS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)
- [NET_REQUEST_WIFI_CMD_TWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)
- [NET_REQUEST_WIFI_CMD_BTWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aaf770b48056af1f9d6d99deb3772027d)
- [NET_REQUEST_WIFI_CMD_PS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)
- [NET_REQUEST_WIFI_CMD_REG_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)
- [NET_REQUEST_WIFI_CMD_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)
- [NET_REQUEST_WIFI_CMD_PACKET_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)
- [NET_REQUEST_WIFI_CMD_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)
- [NET_REQUEST_WIFI_CMD_AP_STA_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)
- [NET_REQUEST_WIFI_CMD_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)
- [NET_REQUEST_WIFI_CMD_CONN_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a)
- [NET_REQUEST_WIFI_CMD_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)
- [NET_REQUEST_WIFI_CMD_AP_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)
- [NET_REQUEST_WIFI_CMD_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a94b310a457fdf82c04ce9e396965d512)
- [NET_REQUEST_WIFI_CMD_DPP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104)
- [NET_REQUEST_WIFI_CMD_NAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aae4df4e8f0959ca7a198c31a0283924e)
- [NET_REQUEST_WIFI_CMD_BTM_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab95b651107d819809cb5909dc25a5a56)
- [NET_REQUEST_WIFI_CMD_PMKSA_FLUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad)
- [NET_REQUEST_WIFI_CMD_ENTERPRISE_CREDS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb)
- [NET_REQUEST_WIFI_CMD_RTS_THRESHOLD_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89)
- [NET_REQUEST_WIFI_CMD_WPS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7)
- [NET_REQUEST_WIFI_CMD_START_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676)
- [NET_REQUEST_WIFI_CMD_NEIGHBOR_REP_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55)
- [NET_REQUEST_WIFI_CMD_CANDIDATE_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed)
- [NET_REQUEST_WIFI_CMD_AP_WPS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77ae496f72d75179a2d10e9fb326259e413)
- [NET_REQUEST_WIFI_CMD_BSS_MAX_IDLE_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a41c1a99be1e0c7b32590b4d69034b282)
- [NET_REQUEST_WIFI_CMD_BGSCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a812004756d95cd2d56982260f89f9178)
- [NET_REQUEST_WIFI_CMD_P2P_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga99a55137188119f65f9d2bb4f57cac77a2186b1d9553322b3ba8bab4acee63833)
- [NET_MGMT_DEFINE_REQUEST_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga08bde8717fd8e12a338c517b22b87776)
- [NET_REQUEST_WIFI_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1c277da90986fa52dca182c4d922646f)
- [NET_REQUEST_WIFI_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa7ab2a97950a22736bb69f60b459f0f6)
- [NET_REQUEST_WIFI_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga90afd8d4e83056463ec6e667ed8ea60a)
- [NET_REQUEST_WIFI_AP_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga638d2eb0a5029c1af46a91b523ed8589)
- [NET_REQUEST_WIFI_AP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf81f62bf4c9e331a095acbf0d24ca1a2)
- [NET_REQUEST_WIFI_AP_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9918582d4e7bb0952daf993ee34e166d)
- [NET_REQUEST_WIFI_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3e45f6ee3801553619d8eb7d0af506eb)
- [NET_REQUEST_WIFI_11K_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadd9b5b206c7ee2e40c30a37c7b4fc002)
- [NET_REQUEST_WIFI_11K_NEIGHBOR_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4a2b1e8befd7376749b1d4fbcf98376f)
- [NET_REQUEST_WIFI_PS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga68aaced888f98e1ba4e6b61b53e5e2ba)
- [NET_REQUEST_WIFI_TWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gab84fd7e9ca0bf0b2b9d08889dda26aad)
- [NET_REQUEST_WIFI_BTWT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf1a806a89b0fd20de950c6e085351134)
- [NET_REQUEST_WIFI_PS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1032f3773cfe6130da4d4d498b044ee2)
- [NET_REQUEST_WIFI_REG_DOMAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2b27d102b779a6d846b375854768fb7f)
- [NET_REQUEST_WIFI_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9b4da60a8108b0cc431ac1eecfca0cd0)
- [NET_REQUEST_WIFI_PACKET_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3098e817d12bf4619c9fd2698508fb4e)
- [NET_REQUEST_WIFI_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad9614d2368f8399850aaec05e40bdc78)
- [NET_REQUEST_WIFI_AP_STA_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa3e52e08d89a1104f07207e52b81d503)
- [NET_REQUEST_WIFI_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3e60c29ca9ce95d17a7fff087290f7f1)
- [NET_REQUEST_WIFI_CONN_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac6483341435ff380a2d4a69430899c1a)
- [NET_REQUEST_WIFI_RTS_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga22d80ef0ffb15e4286d7b1c3325d5334)
- [NET_REQUEST_WIFI_AP_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf4a78d230f5e0743a6aaf152ddda1c67)
- [NET_REQUEST_WIFI_CONFIG_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4d9dbfcf719df5639a0d592b4b8d4322)
- [NET_REQUEST_WIFI_BTM_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4f644b4c980628ffd556458eddc0933d)
- [NET_REQUEST_WIFI_PMKSA_FLUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9070995249eb35de37e2b60c4426f840)
- [NET_REQUEST_WIFI_ENTERPRISE_CREDS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae5dc7835e11487187663dfe65a15f22b)
- [NET_REQUEST_WIFI_RTS_THRESHOLD_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2678ea372335af008d9bd3333f7a7de1)
- [NET_REQUEST_WIFI_WPS_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga649a63bc7d315ebdd89464ff48b3fada)
- [NET_REQUEST_WIFI_START_ROAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga89cc123bb5c30140d2ce0a8b741b1086)
- [NET_REQUEST_WIFI_NEIGHBOR_REP_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga373031970a29331bf1b30d1654c128f0)
- [NET_REQUEST_WIFI_BSS_MAX_IDLE_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga36992c3098d2a1e87f31a18ce369bcc8)
- [NET_REQUEST_WIFI_BGSCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9d407a15b9804aea6673d603aec9f0e9)
- [NET_REQUEST_WIFI_P2P_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4b3de0f402a8f0012ea65c4ab50d2761)
- [net_event_wifi_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac2638308cbb0d268831f1618cf8e1fa8)
- [NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [wifi_version](../network_core_model_reference/P190_wifi_version_结构体.md)
- [drv_version](../network_core_model_reference/P190_wifi_version_结构体.md#aea828bdb512440d6aa3cc853525c4971)
- [fw_version](../network_core_model_reference/P190_wifi_version_结构体.md#a4bf2cbdf5c43ff21718ccf19646c164e)
- [wifi_band_channel](../network_core_model_reference/P161_wifi_band_channel_结构体.md)
- [band](../network_core_model_reference/P161_wifi_band_channel_结构体.md#a4a932599429f37231f76c3064ec5efb3)
- [channel](../network_core_model_reference/P161_wifi_band_channel_结构体.md#acd0dd7366de3650124dad7232a58ade0)
- [wifi_scan_params](../network_core_model_reference/P185_wifi_scan_params_结构体.md)
- [wifi_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad30e29eda65ccafdbd7f11865937b8ea)
- [scan_type](../network_core_model_reference/P185_wifi_scan_params_结构体.md#a645acc54603cd4692527c1a028933078)
- [bands](../network_core_model_reference/P185_wifi_scan_params_结构体.md#a6b571d960ed9d7419e31530e5fb6f97a)
- [dwell_time_active](../network_core_model_reference/P185_wifi_scan_params_结构体.md#a2453a75c23e04e3572559c0e7199c1b4)
- [dwell_time_passive](../network_core_model_reference/P185_wifi_scan_params_结构体.md#a8e7a37ccda8de635e7b7066d7943e814)
- [ssids](../network_core_model_reference/P185_wifi_scan_params_结构体.md#aac11ee8e0ec8a4fa24668f4820bd1a12)
- [max_bss_cnt](../network_core_model_reference/P185_wifi_scan_params_结构体.md#a12d5dea7d8fa8ad03ac2366720c46243)
- [band_chan](../network_core_model_reference/P185_wifi_scan_params_结构体.md#aa5ddbd6bc97b7598288d4b0d38521681)
- [wifi_scan_result](../network_core_model_reference/P186_wifi_scan_result_结构体.md)
- [ssid](../network_core_model_reference/P186_wifi_scan_result_结构体.md#aaefb8f5c9510e4f5002ae306d853ade8)
- [WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)
- [ssid_length](../network_core_model_reference/P186_wifi_scan_result_结构体.md#a2c1c2f4265b914df08fc75deb8b69d39)
- [band](../network_core_model_reference/P186_wifi_scan_result_结构体.md#a38201c9dd798dc11b5bda3ce97b02e92)
- [channel](../network_core_model_reference/P186_wifi_scan_result_结构体.md#adbbfd7692ee5ffd6344fe78b9d91c840)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [security](../network_core_model_reference/P186_wifi_scan_result_结构体.md#af2d3dc5d115e3db76d3bc115510b0a5a)
- [wifi_wpa3_enterprise_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga48fea1f0c7d2700cef47068f96c6b71a)
- [wpa3_ent_type](../network_core_model_reference/P186_wifi_scan_result_结构体.md#abb7de47c605ec05c8fe0a06ecbd2b7b6)
- [wifi_mfp_options](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1f252da47d9650023d7fff6d08e49c76)
- [mfp](../network_core_model_reference/P186_wifi_scan_result_结构体.md#acaa3fb30ebf6df22bfac6380698ed28e)
- [rssi](../network_core_model_reference/P186_wifi_scan_result_结构体.md#a76aa012136e3721fd4a482a22b93546f)
- [mac](../network_core_model_reference/P186_wifi_scan_result_结构体.md#a4fdbc4dc4d5c8b279223e8c06624f434)
- [mac_length](../network_core_model_reference/P186_wifi_scan_result_结构体.md#a8fca0dabec00ebd7ed4800098ec9d451)
- [wifi_connect_req_params](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md)
- [ssid](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#ac260c2cd17a3f36ea101edaf23d41083)
- [ssid_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a547dddf6be5dd77eda74b1085a798400)
- [psk](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aa7743f0ecbc27a9595720ce13ce57c1d)
- [psk_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aaf7455a65590d19f047214b459a2dcb9)
- [psk_is_pbkdf2](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a694a729632ab4e0c54fa739dd9bd9132)
- [sae_password](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a469fac5758b78fc425911837930b2060)
- [sae_password_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a74f0819e7a546ffb8bfb0ec587eccf20)
- [band](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aa2fea1881a8ffdf5d7093ae295867f3e)
- [channel](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a52b6d0323c35d03ec239f40be35cae72)
- [security](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a18dce6bb021086877a30e7a04f5b24b9)
- [mfp](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a745b3416172672a7e5b12bcc5b55e88c)
- [bssid](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aa8081b9075ff9244cefd0ac1ef3f42cb)
- [timeout](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a56183ba7f4d8eaf5fc5b495856adecfd)
- [anon_id](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a781456e079357e2e1096218af3bd218c)
- [aid_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a2892253024b70e5cb8eb2166b17ebe22)
- [key_passwd](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a4946647659a347667ee49bb6990bba66)
- [key_passwd_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a9f913fc0ccecafaba488e444d701fd68)
- [key2_passwd](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a020fc58d7e5350cc803cd5d6fa575e6a)
- [key2_passwd_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#af7b163cc2bffc59f7fa31f47c5e52062)
- [wpa3_ent_mode](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#ae0b94d870ecbee0b203caee6a6e3d8b2)
- [TLS_cipher](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aa4577535a27b8d54d9b8c7543d359ade)
- [eap_ver](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf)
- [eap_identity](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#ab9c65599409387af65a3c2895c3116da)
- [eap_id_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a4da02ff112c09f55dc5bddcda27d16a3)
- [eap_password](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#afd046e702739c4a0d89322ee41b37acd)
- [eap_passwd_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aeab22e95a04a1831b87beda1772d3db7)
- [verify_peer_cert](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aa8f18ace96e471eb0bc8bff8d8146f6f)
- [ft_used](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a047b11e703fb646d778785dfcb14257b)
- [nusers](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a71770c2f2da378db2efedaa87b141627)
- [passwds](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aaf071a51c7281e4d42197f266c729c04)
- [identities](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a265001d2309840d04bdca507896255d0)
- [passwords](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a2163b50b6d466663404e1cb21ce6ae5d)
- [ignore_broadcast_ssid](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#afac70366e509301f9a27ca51be30b88d)
- [wifi_frequency_bandwidths](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b01cead3c2eb4581fe85e2aaaffbd49)
- [bandwidth](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a0d44c86d9b9528041bbe7534e0c7597a)
- [server_cert_domain_exact](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a3833aaaaa78e31d2061e690564af200d)
- [server_cert_domain_exact_len](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a040d2bda9e1a6528814d4cb87bef2924)
- [server_cert_domain_suffix](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#ad82589b9613dd52b63c9ea5ae0fcebeb)
- [server_cert_domain_suffix_len](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#af94eefb87c15c53057e8f22b67a50494)
- [ssid_protection](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#ac9675ace459d40d6e912d86b6b416305)
- [transition_disable](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a562ce91f5eff43e85f84acf342d4e288)
- [wifi_disconn_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac782af0a60b202fd19597cabb7bd3a9a)
- [WIFI_REASON_DISCONN_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042)
- [WIFI_REASON_DISCONN_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c)
- [WIFI_REASON_DISCONN_USER_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7)
- [WIFI_REASON_DISCONN_AP_LEAVING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204)
- [WIFI_REASON_DISCONN_INACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6)
- [wifi_disconn_reason_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1bea051b0c184cb859f27b36e3593bf2)
- [wifi_ap_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaaf730bf76adc06434c7ac63bf0417884)
- [WIFI_STATUS_AP_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c)
- [WIFI_STATUS_AP_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a)
- [WIFI_STATUS_AP_CHANNEL_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b)
- [WIFI_STATUS_AP_CHANNEL_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15)
- [WIFI_STATUS_AP_SSID_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce)
- [WIFI_STATUS_AP_AUTH_TYPE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8)
- [WIFI_STATUS_AP_OP_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca)
- [WIFI_STATUS_AP_OP_NOT_PERMITTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe)
- [wifi_status](../network_core_model_reference/P187_wifi_status_结构体.md)
- [status](../network_core_model_reference/P187_wifi_status_结构体.md#aa1dbff8154400f8353693d387977008b)
- [wifi_conn_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga86a5741e54aeb3e290142b0de217b8a8)
- [conn_status](../network_core_model_reference/P187_wifi_status_结构体.md#a8f885e78366d0499e4ba8e15bef275ac)
- [disconn_reason](../network_core_model_reference/P187_wifi_status_结构体.md#aa04b5033d93274badd27f702af9830bc)
- [ap_status](../network_core_model_reference/P187_wifi_status_结构体.md#a02f0fcc7ef57661ca95d0c99f045aef1)
- [status_code](../network_core_model_reference/P187_wifi_status_结构体.md#ac8a85738dcfa60dfaf502d86b8294f78)
- [reason_code](../network_core_model_reference/P187_wifi_status_结构体.md#a8c63d5fecc9d532366c144b4dd7bb2ad)
- [wifi_iface_status](../network_core_model_reference/P175_wifi_iface_status_结构体.md)
- [state](../network_core_model_reference/P175_wifi_iface_status_结构体.md#ac52806155be3d64954ac6d109e76ec57)
- [ssid_len](../network_core_model_reference/P175_wifi_iface_status_结构体.md#ad82f281941e4f6ce1ef0bca008e26d41)
- [ssid](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a3ab671471bcdfeb5b955d156d39f2bb3)
- [bssid](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a5d5d19056a1a15365fbdd94274a0fc5e)
- [wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)
- [band](../network_core_model_reference/P175_wifi_iface_status_结构体.md#ae1c141a18f4e225af2c22a8cb4f882a8)
- [channel](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a6432663156e5b2c424d254ed1eae0144)
- [wifi_iface_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga584f6239ac14e2bedc5e6bd72756423b)
- [iface_mode](../network_core_model_reference/P175_wifi_iface_status_结构体.md#ad33d2ec149a8d556e2472dd842ceadc0)
- [wifi_link_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdb2a784d4727b71ab44cca04e422c62)
- [link_mode](../network_core_model_reference/P175_wifi_iface_status_结构体.md#ae2de076d79f2172793d65fe9cd31edc4)
- [wpa3_ent_type](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a361c0e8a385fdc21f16258c25c2bc8d1)
- [security](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a625ecec1abec8dd65cf155eab21a01b5)
- [wifi_wep_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gafc901312b5988481b34d05a031d6c0db)
- [wep_key_type](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a9a899c28b51158e8973886f84d7d8950)
- [mfp](../network_core_model_reference/P175_wifi_iface_status_结构体.md#aa1a9b644fd355526125ddd32416b7c24)
- [rssi](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a4e593147b88eb4938d55a4de72fcc7f6)
- [dtim_period](../network_core_model_reference/P175_wifi_iface_status_结构体.md#aae6c8cbaa16c81d308f08114d5103a3d)
- [beacon_interval](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a241bfbe70628006b515b5f9e4f97665c)
- [twt_capable](../network_core_model_reference/P175_wifi_iface_status_结构体.md#acfde8d64b463a9f553aa4fb689dc1917)
- [current_phy_tx_rate](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a43f239b0bc305e4c1c5f7fd9bb5753bf)
- [wifi_ps_params](../network_core_model_reference/P181_wifi_ps_params_结构体.md)
- [wifi_ps](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0fffeb57b68fb8cdef9d3d571368b8ca)
- [enabled](../network_core_model_reference/P181_wifi_ps_params_结构体.md#abb22aaa45833ac130922204bd2fe841b)
- [listen_interval](../network_core_model_reference/P181_wifi_ps_params_结构体.md#a8510c799ab0c5825f1c6349f9799c62f)
- [wifi_ps_wakeup_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac7f907644847e905d67c709fa4afae7f)
- [wakeup_mode](../network_core_model_reference/P181_wifi_ps_params_结构体.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66)
- [wifi_ps_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaffae7d2a754be5eb952ad2b83edad54c)
- [mode](../network_core_model_reference/P181_wifi_ps_params_结构体.md#a5a022d89d43ecf2cd1f15fc72c0f2bed)
- [timeout_ms](../network_core_model_reference/P181_wifi_ps_params_结构体.md#ad963f1bf78dc271f08b73f3aadb36a91)
- [wifi_ps_param_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabe45d132797047c098041331c8f6f912)
- [type](../network_core_model_reference/P181_wifi_ps_params_结构体.md#aef62e5bf6216bf4dc461efe71735c4bd)
- [wifi_config_ps_param_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad98099584d2222ede93aba42b1fbaff0)
- [fail_reason](../network_core_model_reference/P181_wifi_ps_params_结构体.md#a63fa2ee03bc4aefada61c298ee14336c)
- [wifi_ps_exit_strategy](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2d424d1711389fb784e916a87ff854b7)
- [exit_strategy](../network_core_model_reference/P181_wifi_ps_params_结构体.md#ab9fc62dd1e2928320274fa1554a550a6)
- [wifi_btwt_params](../network_core_model_reference/P163_wifi_btwt_params_结构体.md)
- [btwt_id](../network_core_model_reference/P163_wifi_btwt_params_结构体.md#ae52281d9f53e106fb9ed813131d8085e)
- [btwt_mantissa](../network_core_model_reference/P163_wifi_btwt_params_结构体.md#a2c1b3551a714fbf1b948ce4bcf805934)
- [btwt_exponent](../network_core_model_reference/P163_wifi_btwt_params_结构体.md#a76c97bcc132405d6a1a54bcca77054ac)
- [btwt_nominal_wake](../network_core_model_reference/P163_wifi_btwt_params_结构体.md#a0192d3a9334fc55a135206e6b74ea5b5)
- [wifi_twt_params](../network_core_model_reference/P189_wifi_twt_params_结构体.md)
- [wifi_twt_operation](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad0e998aeb1b27c4f203ca76339d323a3)
- [operation](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a6f0483861a387651c9c89ba182e064bd)
- [wifi_twt_negotiation_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga695123cd534e2499f516a07fdc5cafa8)
- [negotiation_type](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a5fd269328f68838b8a7e3a0b93eed894)
- [wifi_twt_setup_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga31c78afc89bfdc4b54cee177843f8022)
- [setup_cmd](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a347f8cff73ee6b6ba6d15ddf6f376a2d)
- [wifi_twt_setup_resp_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4d03aedac13ee4512d7717ac624f319a)
- [resp_status](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a805a23284ed4afa46b84efcd43329beb)
- [wifi_twt_teardown_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad3709d07aaa3ed59b48f9dd7bd181989)
- [teardown_status](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a9faff59e577775b3fe53f2139462ac71)
- [dialog_token](../network_core_model_reference/P189_wifi_twt_params_结构体.md#adda47e302a87a766f18e28016963a561)
- [flow_id](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a95ec4b32d37309efa47256ae1ea865da)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [twt_interval](../network_core_model_reference/P189_wifi_twt_params_结构体.md#ab92fe571559fcd5d97cdf7e6b7d86681)
- [responder](../network_core_model_reference/P189_wifi_twt_params_结构体.md#ae547c6fc1c7cbad15bebcfdaa43f59e7)
- [trigger](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a4e822c04b52fe6a9489e48e26b8f9382)
- [implicit](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a8ea1e2501c8b69dc3fa606eb360f8678)
- [announce](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a02f2d822d530e5376f256503439a54f9)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [twt_wake_interval](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a7c297459a17ed2fd232c62cca63e952f)
- [twt_wake_ahead_duration](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a6f907ca412251fdd7391f29bfa6d7713)
- [twt_info_disable](../network_core_model_reference/P189_wifi_twt_params_结构体.md#ac02eab9593b1ec2c9a0453a67076df88)
- [twt_exponent](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aabb77296f007cb055f78fa1ec3d155a3)
- [twt_mantissa](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aadad4556e2e5405b0703ebb4233a4d17)
- [setup](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aee57c0189b210cfcc18e213e35b9479c)
- [btwt_sta_wait](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aa05e5fa6a519f700147bb99d6e69a06b)
- [btwt_offset](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a4459cf19226e199d23ae0cd1d7132b73)
- [btwt_li](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a7e7c786c51d3bc70af135bad88ebde4f)
- [btwt_count](../network_core_model_reference/P189_wifi_twt_params_结构体.md#afc563010a33624bf01feac1292f0871d)
- [btwt_set_cfg](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aa11562186ea265b906861269bc8a692b)
- [WIFI_BTWT_AGREEMENT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga38d92ba342887e46c957b820d89a7a20)
- [btwt](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a72ab809144b1dd3e7e121e489ef399e2)
- [teardown_all](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a26d6bda00452f77832f69f4465c13efb)
- [teardown](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aadf62f6386359ad15491d0073c9065bf)
- [wifi_twt_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga97fa304f9a1db2294a93cccd4c93bcf6)
- [fail_reason](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a70f58b502bb67ef3b2068ded2160b612)
- [wifi_twt_flow_info](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md)
- [twt_interval](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#ae15ba49fa54f82cc6a1fb0d4572114b7)
- [dialog_token](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#a123ce10bed8b62b01919a7ea7644a0ba)
- [flow_id](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#acb0c618f1cebcb172f342cfe222683be)
- [negotiation_type](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#a620ae8ba546e4091d74280cb1553b2cf)
- [responder](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#ac82e4de8ffc82f851061f8ba8d217dc1)
- [trigger](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#a952a67bd092c5dadba387bb13449c6f3)
- [implicit](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#afb480be82d1c6f351bd634fd83bfa5c7)
- [announce](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#afc81a5111c265fd9bb2aca5f9510bfa8)
- [twt_wake_interval](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#aede6cb0cfc999fac8ded49e2981a3762)
- [twt_wake_ahead_duration](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#a6384d3829d54a58a53eafcb74c64a658)
- [wifi_enterprise_creds_params](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md)
- [ca_cert](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ae37381504a457b2f1d56dd5270c6711d)
- [ca_cert_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a5f7060fcd2ca3db0b202faf15062564b)
- [client_cert](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a81d61179feba627be5c6456130b9f2af)
- [client_cert_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a5f122d59b25b00af2db7eeac93d5482e)
- [client_key](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a8d88f5a8a6ccc8a9a883078af49ae96b)
- [client_key_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a09f5b34c81fe871e7513358499518d95)
- [ca_cert2](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ad9b867873709d7f2363fef49d7b6f2ca)
- [ca_cert2_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#abf35045e71afb0cb9ea25c635c5ac141)
- [client_cert2](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a133126e338d89563733268a03e2fa613)
- [client_cert2_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#adbe26c9b88f44eb6b875888f6a03e1bb)
- [client_key2](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#abcda4d7820681d517d70d8f130b47050)
- [client_key2_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a3da90b8a8dfa848f617579760ad4f971)
- [server_cert](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ad3621e92a1aa968c58a899ace72967db)
- [server_cert_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ad0bfb59d3691e5d21cb4b810c4d1279e)
- [server_key](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#acb94a8885b5ab99d1a8fb33dffebc322)
- [server_key_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a9500252974bd15037d4dbc41eba3a27d)
- [dh_param](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ab0fd7419d8a94d1d804e5554acfbf49a)
- [dh_param_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ac548e0b006a9f7b858409cda7c3d34ba)
- [wifi_ps_config](../network_core_model_reference/P180_wifi_ps_config_结构体.md)
- [num_twt_flows](../network_core_model_reference/P180_wifi_ps_config_结构体.md#a9e83c10eaaa1d721cbc49b40aedb00df)
- [twt_flows](../network_core_model_reference/P180_wifi_ps_config_结构体.md#ab7460f0f253b2d552e49e98e2c770967)
- [ps_params](../network_core_model_reference/P180_wifi_ps_config_结构体.md#a357aafc2dedda37755b1cb1fc07fe5a6)
- [wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)
- [WIFI_MGMT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd)
- [WIFI_MGMT_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1)
- [wifi_11k_params](../network_core_model_reference/P158_wifi_11k_params_结构体.md)
- [oper](../network_core_model_reference/P158_wifi_11k_params_结构体.md#ae6029ed4bada41f18df0329d0da7401e)
- [enable_11k](../network_core_model_reference/P158_wifi_11k_params_结构体.md#a739c3e94b025aae2fcf5680aecf3d646)
- [ssid](../network_core_model_reference/P158_wifi_11k_params_结构体.md#a64ace23c71837417678ceb9cc8d5f216)
- [wifi_reg_chan_info](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md)
- [center_frequency](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md#a0addffc11ef29f50c01b700835e59930)
- [max_power](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md#af9169ab4a41fac4c6f6766fc96799545)
- [supported](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md#aa044611e18b7332b8577e29f6a769e3f)
- [passive_only](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md#acc7a88b004c9a61c8bf9ee1a97f85928)
- [dfs](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md#a1ab137c142902d2de7d6be2626d7ac1f)
- [wifi_reg_domain](../network_core_model_reference/P184_wifi_reg_domain_结构体.md)
- [oper](../network_core_model_reference/P184_wifi_reg_domain_结构体.md#a3bbfdf1497a87bbb6b6211c7035e1002)
- [force](../network_core_model_reference/P184_wifi_reg_domain_结构体.md#a567c6fcae8032567aea83c18cd211c33)
- [country_code](../network_core_model_reference/P184_wifi_reg_domain_结构体.md#abf191495814c227fbbfaccb2f727762e)
- [WIFI_COUNTRY_CODE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6766ef7bcb001f1fb526a4083b6cd8bc)
- [num_channels](../network_core_model_reference/P184_wifi_reg_domain_结构体.md#a3278e9f43893f49ab9f9d0d7f24009c1)
- [chan_info](../network_core_model_reference/P184_wifi_reg_domain_结构体.md#a4c8c9c11e41123cd7738fdb0d33ae5fb)
- [wifi_twt_sleep_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga38c184ea35c02f304cccdf389ca6d552)
- [WIFI_TWT_STATE_SLEEP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c)
- [WIFI_TWT_STATE_AWAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0)
- [wifi_raw_scan_result](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md)
- [rssi](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md#a3f08580c6448a5fa28dd8a594fa7dad6)
- [frame_length](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md#a876966f469714eb481b42ccc8a63945c)
- [frequency](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md#aa2c7781882c6775616cbc8016b0842f6)
- [data](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md#a5710e89199c147ce898602795f00aba3)
- [wifi_ap_sta_info](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md)
- [link_mode](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md#a7d8bd52340d4937a4b5b7d2c00662441)
- [mac](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md#a7db904376ec73b774aa9d8236c15b3f6)
- [mac_length](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md#a7f7c8b144bb3464af5213708591eefda)
- [twt_capable](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md#a838c9a4288c9bc7e97afe2334c678f34)
- [wifi_mode_info](../network_core_model_reference/P177_wifi_mode_info_结构体.md)
- [mode](../network_core_model_reference/P177_wifi_mode_info_结构体.md#aa29d3b88fc718aa3ac05daf38974707d)
- [if_index](../network_core_model_reference/P177_wifi_mode_info_结构体.md#add58dd3b45fd2ddaf684d1b0de81bef9)
- [oper](../network_core_model_reference/P177_wifi_mode_info_结构体.md#a57c101db8b81ab0ac5dd0a158057a64a)
- [wifi_filter_info](../network_core_model_reference/P174_wifi_filter_info_结构体.md)
- [filter](../network_core_model_reference/P174_wifi_filter_info_结构体.md#ad9560be814299055cfa11b995a7dcf42)
- [if_index](../network_core_model_reference/P174_wifi_filter_info_结构体.md#af9ea91e31e78afcb7ffe1ff9a04277a3)
- [buffer_size](../network_core_model_reference/P174_wifi_filter_info_结构体.md#a1b2d0448fc7f62654e3f5aacfba62f8f)
- [oper](../network_core_model_reference/P174_wifi_filter_info_结构体.md#aedd5e220cdde5768cb0f4aff920971cd)
- [wifi_channel_info](../network_core_model_reference/P164_wifi_channel_info_结构体.md)
- [channel](../network_core_model_reference/P164_wifi_channel_info_结构体.md#a799cbc0a67764f6680322ba0f2ad3300)
- [band](../network_core_model_reference/P164_wifi_channel_info_结构体.md#aeda7667c89ca98c1f45a09331a2bfd47)
- [if_index](../network_core_model_reference/P164_wifi_channel_info_结构体.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d)
- [oper](../network_core_model_reference/P164_wifi_channel_info_结构体.md#aa8ef8a71b49ead3664fff9a4d61b1ce8)
- [wifi_ap_config_params](../network_core_model_reference/P159_wifi_ap_config_params_结构体.md)
- [wifi_ap_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga83546cf946a9123c563609e8903d9642)
- [type](../network_core_model_reference/P159_wifi_ap_config_params_结构体.md#a4c391cf504a994ed0bc4971afdf76774)
- [max_inactivity](../network_core_model_reference/P159_wifi_ap_config_params_结构体.md#a289866d9209450e893281b4c198a546a)
- [max_num_sta](../network_core_model_reference/P159_wifi_ap_config_params_结构体.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a)
- [bandwidth](../network_core_model_reference/P159_wifi_ap_config_params_结构体.md#aba4e43dff01fa026c8dbbfff670d3097)
- [wifi_config_params](../network_core_model_reference/P166_wifi_config_params_结构体.md)
- [wifi_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7ef91a39c2cc6bb454d870a8a80f8439)
- [type](../network_core_model_reference/P166_wifi_config_params_结构体.md#aada77f3f6f5909ebefb699d7252bb74c)
- [okc](../network_core_model_reference/P166_wifi_config_params_结构体.md#a3a05f8b09eb2a74913c394f28fe7ab79)
- [listen](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a7005ffbeeff92be5394ff3244da79028)
- [wifi_wps_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4c36ae1a5171d3fbaeebf95c16be496d)
- [WIFI_WPS_PBC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88)
- [WIFI_WPS_PIN_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d)
- [WIFI_WPS_PIN_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552)
- [wifi_wps_config_params](../network_core_model_reference/P191_wifi_wps_config_params_结构体.md)
- [oper](../network_core_model_reference/P191_wifi_wps_config_params_结构体.md#aa7a10889c5cd5124983b0f7242d23b7e)
- [pin](../network_core_model_reference/P191_wifi_wps_config_params_结构体.md#a962bd6513c564150e0c75112b96bbe15)
- [WIFI_WPS_PIN_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga234d72d7c881e67ff49fb6c474c622e3)
- [connect](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)
- [wifi_sap_iface_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0cc87c00cbee0d0aca833119dbf0d74e)
- [WIFI_SAP_IFACE_UNINITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74ead92795c629fe828e7efde485eb2761c0)
- [WIFI_SAP_IFACE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74ea59a8530057e9839d89243558cc366d69)
- [WIFI_SAP_IFACE_COUNTRY_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74ea403d84f907f84492eed8e33713e828ae)
- [WIFI_SAP_IFACE_ACS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eab3fea1a0ef90043699cb7d8ab064be7e)
- [WIFI_SAP_IFACE_HT_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eaa3a6e6e367c7384379f3c562d1fc358f)
- [WIFI_SAP_IFACE_DFS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eafdf99a461cf5878240cc40ae4ea7e113)
- [WIFI_SAP_IFACE_NO_IR](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eaea74f039e6a5abe976e9956b5a01ff1a)
- [WIFI_SAP_IFACE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0cc87c00cbee0d0aca833119dbf0d74eaa9133b73b886f2ec543acd282b33eeda)
- [wifi_bgscan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaacc27e95277622f56ef35e129aaac4d0)
- [WIFI_BGSCAN_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaacc27e95277622f56ef35e129aaac4d0ad22b7dc42e9713d08cc9242b801f24e9)
- [WIFI_BGSCAN_SIMPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaacc27e95277622f56ef35e129aaac4d0a40446bcc15ca3f09acba97029f68cbbe)
- [WIFI_BGSCAN_LEARN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaacc27e95277622f56ef35e129aaac4d0ae682cebd0e3ef481bf53e187eb92d911)
- [wifi_bgscan_params](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md)
- [type](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md#a1a6cc39e71f94c9fae639a886f5c3030)
- [short_interval](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md#ae1e3e6bf419e7f810e5ba7b085be7c12)
- [long_interval](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md#a5ec94a609155573cedfe7772b940d183)
- [rssi_threshold](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md#ab73566a1db6e31c15c575cab21f24bfb)
- [btm_queries](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md#a8d12ab3d7d589d06c79874ea374ae327)
- [wifi_ext_capab](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga03ab29789adfe867c4ebaddc39482344)
- [WIFI_EXT_CAPAB_20_40_COEX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344abf275508c3f69321cdf704779e976d68)
- [WIFI_EXT_CAPAB_GLK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344a1363c1318e4281e057d848194396feb7)
- [WIFI_EXT_CAPAB_EXT_CHAN_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344acf854adfca2bb41dd5d75df2b16c3e5e)
- [WIFI_EXT_CAPAB_TIM_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344af42762fd723afef7fae98cbefbfff056)
- [WIFI_EXT_CAPAB_BSS_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga03ab29789adfe867c4ebaddc39482344ac5c648efedadc82fae7d9e0851ff71ba)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [scan_result_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad34b366f1c315207ce0da587ca96d8d8)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [wifi_mgmt_ops](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md)
- [scan](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#acc20fd11dcd09edb72d03f8737801c06)
- [device](../device_reference/P002_设备对象结构.md)
- [connect](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a65a4e87ee94aa5c7a551aa9b39289708)
- [disconnect](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a8489951fc1baee17e56070187f4d77b0)
- [ap_enable](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#aa34fff15f9e0aadf244f9e0cf37b367b)
- [ap_disable](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a3264be8040227d1e91a8223cabcd4e53)
- [ap_sta_disconnect](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ad6e04312b0e7680f87ce801b2540db10)
- [iface_status](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a930cbd9e4661d137ae37cd89afd451b2)
- [get_stats](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#abb2b7c033e77af36acde5d420effe8d1)
- [net_stats_wifi](../network_core_model_reference/P153_net_stats_wifi_结构体.md)
- [reset_stats](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a7bd0f326e9eeedbc3c768c5ecf207c06)
- [cfg_11k](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ab3b7dce2feb0ecbca3d4668dc9e41032)
- [send_11k_neighbor_request](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a16fc04b7572234f6e7c207d82e0b4625)
- [set_power_save](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a37e6c41f4b1223b8952171abb5cd9d89)
- [set_twt](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#af2089cba9ba73593b8d5b4329f2fddff)
- [set_btwt](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a50421d54785d4f8d768c8a35fcda0ca5)
- [get_power_save_config](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a9278c8779748e64ad70cfbeef5a297dd)
- [reg_domain](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a80b09c5ea77c99a4dfffb5a21f0c8867)
- [filter](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a5642ca19f2f25ba7a53d9efb30d7bd59)
- [mode](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a0bfeb2a8f463dc49ca3d433ee17d3dd9)
- [channel](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a365e9aafc5399e1a9f37c9b4f347534c)
- [btm_query](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ad241d490ac3e10c58c87da004d706407)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bss_support_neighbor_rep](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a6198f23a4cdeb5b0e413b7a66c1fa442)
- [bss_ext_capab](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ac6d82f5f2defdc657f056f0e6103e04b)
- [legacy_roam](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a8d37cec74b3d523257120b75f471e92f)
- [get_version](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a7b788903271a427363d22808659a3ee9)
- [get_conn_params](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ab5368326d558de972ce5806dd9a99f22)
- [set_rts_threshold](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#aed7b6daf7264c1450cc5d31530a2043a)
- [ap_config_params](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a01b2ac4cd8a1f039bdba3adb2586d3cb)
- [config_params](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a63e7bcc4d3bb9ee7e073a6c55abddcc2)
- [pmksa_flush](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a76e76d96e307bc10bd14e4ea7b5dbed6)
- [get_rts_threshold](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ad3c8908b6a3752adf59d5a4170175f83)
- [wps_config](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ab8e11d463ff7000a090e0609f002a97c)
- [candidate_scan](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a69f2ec3a03e77b4eb9d9fdd7315edf18)
- [start_11r_roaming](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ac4ed6d4d1088f6e23d5256d156e42955)
- [set_bss_max_idle_period](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a26eaabf9621b16d332e20777b188d4ad)
- [set_bgscan](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a0aa02b0d69479b95d6e1a0971b16ee92)
- [get_iface_caps](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a40d53afce76b5b7614ee95e41ea46635)
- [net_wifi_mgmt_offload](../network_core_model_reference/P157_net_wifi_mgmt_offload_结构体.md)
- [ethernet_api](../network_service_model_reference/P007_ethernet_api_结构体.md)
- [wifi_iface](../network_core_model_reference/P157_net_wifi_mgmt_offload_结构体.md#a1d34a954a2f16d29f51dc51dd6fbb845)
- [offloaded_if_api](../network_service_model_reference/P038_offloaded_if_api_结构体.md)
- [wifi_mgmt_api](../network_core_model_reference/P157_net_wifi_mgmt_offload_结构体.md#a98fcc053d9820d2d981ed659520c9b3b)
- [wifi_drv_ops](../network_core_model_reference/P157_net_wifi_mgmt_offload_结构体.md#a991e0bc6247578a3d1c9d2d3ab0b63d7)
- [wifi_mgmt_raise_connect_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga036416696b1e3bc458ddbaf07a08d69d)
- [wifi_mgmt_raise_connect_result_status_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdf7753c247587eface6e829686d120c)
- [wifi_mgmt_raise_disconnect_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b6edcf9b51afbf7a327d1a344bd7b87)
- [wifi_mgmt_raise_disconnect_result_status_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3f7c4f252ab9621fbf3b9bd937253858)
- [wifi_mgmt_raise_iface_status_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7da6af0747bcba85f8afab30c92b5b43)
- [wifi_mgmt_raise_twt_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga39404d15243ca084b253cae8fc07e374)
- [wifi_mgmt_raise_twt_sleep_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga18f09a3196588b51d6c0644f82f639d7)
- [wifi_mgmt_raise_raw_scan_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga71c99913bded844c4ca32ed9155bc470)
- [wifi_mgmt_raise_disconnect_complete_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa75246d6dc55dada389c9d31e2607d5c)
- [wifi_mgmt_raise_ap_enable_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga67b52edeff76c2211b038f4aa90b8982)
- [wifi_mgmt_raise_ap_disable_result_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadee15c6a492a8ee13bea43812debb5d9)
- [wifi_mgmt_raise_ap_sta_connected_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac8f17f0aa3e426a5cdb731727b9b9ce3)
- [wifi_mgmt_raise_ap_sta_disconnected_event](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga49fb9c3908be61d847b31c99be6afc42)
- [ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [offloaded_netdev.h](../api_file_runtime_reference/P049_zephyr__net__offloaded_netdev.h_文件参考.md)
- [net_wifi_mgmt_offload::wifi_iface](../network_core_model_reference/P157_net_wifi_mgmt_offload_结构体.md#a1d34a954a2f16d29f51dc51dd6fbb845)
- [net_wifi_mgmt_offload::wifi_mgmt_api](../network_core_model_reference/P157_net_wifi_mgmt_offload_结构体.md#a98fcc053d9820d2d981ed659520c9b3b)
- [net_wifi_mgmt_offload::wifi_drv_ops](../network_core_model_reference/P157_net_wifi_mgmt_offload_结构体.md#a991e0bc6247578a3d1c9d2d3ab0b63d7)
- [wifi_11k_params::ssid](../network_core_model_reference/P158_wifi_11k_params_结构体.md#a64ace23c71837417678ceb9cc8d5f216)
- [wifi_11k_params::enable_11k](../network_core_model_reference/P158_wifi_11k_params_结构体.md#a739c3e94b025aae2fcf5680aecf3d646)
- [wifi_11k_params::oper](../network_core_model_reference/P158_wifi_11k_params_结构体.md#ae6029ed4bada41f18df0329d0da7401e)
- [wifi_ap_config_params::max_inactivity](../network_core_model_reference/P159_wifi_ap_config_params_结构体.md#a289866d9209450e893281b4c198a546a)
- [wifi_ap_config_params::type](../network_core_model_reference/P159_wifi_ap_config_params_结构体.md#a4c391cf504a994ed0bc4971afdf76774)
- [wifi_ap_config_params::max_num_sta](../network_core_model_reference/P159_wifi_ap_config_params_结构体.md#a7fc0fad99f53ed8e1ac40b74ec98bf9a)
- [wifi_ap_config_params::bandwidth](../network_core_model_reference/P159_wifi_ap_config_params_结构体.md#aba4e43dff01fa026c8dbbfff670d3097)
- [wifi_ap_sta_info::link_mode](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md#a7d8bd52340d4937a4b5b7d2c00662441)
- [wifi_ap_sta_info::mac](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md#a7db904376ec73b774aa9d8236c15b3f6)
- [wifi_ap_sta_info::mac_length](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md#a7f7c8b144bb3464af5213708591eefda)
- [wifi_ap_sta_info::twt_capable](../network_core_model_reference/P160_wifi_ap_sta_info_结构体.md#a838c9a4288c9bc7e97afe2334c678f34)
- [wifi_band_channel::band](../network_core_model_reference/P161_wifi_band_channel_结构体.md#a4a932599429f37231f76c3064ec5efb3)
- [wifi_band_channel::channel](../network_core_model_reference/P161_wifi_band_channel_结构体.md#acd0dd7366de3650124dad7232a58ade0)
- [wifi_bgscan_params::type](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md#a1a6cc39e71f94c9fae639a886f5c3030)
- [wifi_bgscan_params::long_interval](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md#a5ec94a609155573cedfe7772b940d183)
- [wifi_bgscan_params::btm_queries](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md#a8d12ab3d7d589d06c79874ea374ae327)
- [wifi_bgscan_params::rssi_threshold](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md#ab73566a1db6e31c15c575cab21f24bfb)
- [wifi_bgscan_params::short_interval](../network_core_model_reference/P162_wifi_bgscan_params_结构体.md#ae1e3e6bf419e7f810e5ba7b085be7c12)
- [wifi_btwt_params::btwt_nominal_wake](../network_core_model_reference/P163_wifi_btwt_params_结构体.md#a0192d3a9334fc55a135206e6b74ea5b5)
- [wifi_btwt_params::btwt_mantissa](../network_core_model_reference/P163_wifi_btwt_params_结构体.md#a2c1b3551a714fbf1b948ce4bcf805934)
- [wifi_btwt_params::btwt_exponent](../network_core_model_reference/P163_wifi_btwt_params_结构体.md#a76c97bcc132405d6a1a54bcca77054ac)
- [wifi_btwt_params::btwt_id](../network_core_model_reference/P163_wifi_btwt_params_结构体.md#ae52281d9f53e106fb9ed813131d8085e)
- [wifi_channel_info::if_index](../network_core_model_reference/P164_wifi_channel_info_结构体.md#a43a7dd8c19d0c6540e3cc0b5d1d6165d)
- [wifi_channel_info::channel](../network_core_model_reference/P164_wifi_channel_info_结构体.md#a799cbc0a67764f6680322ba0f2ad3300)
- [wifi_channel_info::oper](../network_core_model_reference/P164_wifi_channel_info_结构体.md#aa8ef8a71b49ead3664fff9a4d61b1ce8)
- [wifi_channel_info::band](../network_core_model_reference/P164_wifi_channel_info_结构体.md#aeda7667c89ca98c1f45a09331a2bfd47)
- [wifi_config_params::okc](../network_core_model_reference/P166_wifi_config_params_结构体.md#a3a05f8b09eb2a74913c394f28fe7ab79)
- [wifi_config_params::type](../network_core_model_reference/P166_wifi_config_params_结构体.md#aada77f3f6f5909ebefb699d7252bb74c)
- [wifi_connect_req_params::key2_passwd](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a020fc58d7e5350cc803cd5d6fa575e6a)
- [wifi_connect_req_params::server_cert_domain_exact_len](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a040d2bda9e1a6528814d4cb87bef2924)
- [wifi_connect_req_params::ft_used](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a047b11e703fb646d778785dfcb14257b)
- [wifi_connect_req_params::bandwidth](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a0d44c86d9b9528041bbe7534e0c7597a)
- [wifi_connect_req_params::security](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a18dce6bb021086877a30e7a04f5b24b9)
- [wifi_connect_req_params::passwords](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a2163b50b6d466663404e1cb21ce6ae5d)
- [wifi_connect_req_params::identities](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a265001d2309840d04bdca507896255d0)
- [wifi_connect_req_params::aid_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a2892253024b70e5cb8eb2166b17ebe22)
- [wifi_connect_req_params::server_cert_domain_exact](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a3833aaaaa78e31d2061e690564af200d)
- [wifi_connect_req_params::sae_password](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a469fac5758b78fc425911837930b2060)
- [wifi_connect_req_params::key_passwd](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a4946647659a347667ee49bb6990bba66)
- [wifi_connect_req_params::eap_id_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a4da02ff112c09f55dc5bddcda27d16a3)
- [wifi_connect_req_params::channel](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a52b6d0323c35d03ec239f40be35cae72)
- [wifi_connect_req_params::ssid_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a547dddf6be5dd77eda74b1085a798400)
- [wifi_connect_req_params::timeout](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a56183ba7f4d8eaf5fc5b495856adecfd)
- [wifi_connect_req_params::transition_disable](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a562ce91f5eff43e85f84acf342d4e288)
- [wifi_connect_req_params::psk_is_pbkdf2](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a694a729632ab4e0c54fa739dd9bd9132)
- [wifi_connect_req_params::nusers](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a71770c2f2da378db2efedaa87b141627)
- [wifi_connect_req_params::mfp](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a745b3416172672a7e5b12bcc5b55e88c)
- [wifi_connect_req_params::sae_password_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a74f0819e7a546ffb8bfb0ec587eccf20)
- [wifi_connect_req_params::anon_id](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a781456e079357e2e1096218af3bd218c)
- [wifi_connect_req_params::eap_ver](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf)
- [wifi_connect_req_params::key_passwd_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#a9f913fc0ccecafaba488e444d701fd68)
- [wifi_connect_req_params::band](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aa2fea1881a8ffdf5d7093ae295867f3e)
- [wifi_connect_req_params::TLS_cipher](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aa4577535a27b8d54d9b8c7543d359ade)
- [wifi_connect_req_params::psk](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aa7743f0ecbc27a9595720ce13ce57c1d)
- [wifi_connect_req_params::bssid](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aa8081b9075ff9244cefd0ac1ef3f42cb)
- [wifi_connect_req_params::verify_peer_cert](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aa8f18ace96e471eb0bc8bff8d8146f6f)
- [wifi_connect_req_params::passwds](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aaf071a51c7281e4d42197f266c729c04)
- [wifi_connect_req_params::psk_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aaf7455a65590d19f047214b459a2dcb9)
- [wifi_connect_req_params::eap_identity](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#ab9c65599409387af65a3c2895c3116da)
- [wifi_connect_req_params::ssid](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#ac260c2cd17a3f36ea101edaf23d41083)
- [wifi_connect_req_params::ssid_protection](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#ac9675ace459d40d6e912d86b6b416305)
- [wifi_connect_req_params::server_cert_domain_suffix](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#ad82589b9613dd52b63c9ea5ae0fcebeb)
- [wifi_connect_req_params::wpa3_ent_mode](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#ae0b94d870ecbee0b203caee6a6e3d8b2)
- [wifi_connect_req_params::eap_passwd_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#aeab22e95a04a1831b87beda1772d3db7)
- [wifi_connect_req_params::key2_passwd_length](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#af7b163cc2bffc59f7fa31f47c5e52062)
- [wifi_connect_req_params::server_cert_domain_suffix_len](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#af94eefb87c15c53057e8f22b67a50494)
- [wifi_connect_req_params::ignore_broadcast_ssid](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#afac70366e509301f9a27ca51be30b88d)
- [wifi_connect_req_params::eap_password](../network_core_model_reference/P167_wifi_connect_req_params_结构体.md#afd046e702739c4a0d89322ee41b37acd)
- [wifi_enterprise_creds_params::client_key_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a09f5b34c81fe871e7513358499518d95)
- [wifi_enterprise_creds_params::client_cert2](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a133126e338d89563733268a03e2fa613)
- [wifi_enterprise_creds_params::client_key2_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a3da90b8a8dfa848f617579760ad4f971)
- [wifi_enterprise_creds_params::client_cert_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a5f122d59b25b00af2db7eeac93d5482e)
- [wifi_enterprise_creds_params::ca_cert_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a5f7060fcd2ca3db0b202faf15062564b)
- [wifi_enterprise_creds_params::client_cert](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a81d61179feba627be5c6456130b9f2af)
- [wifi_enterprise_creds_params::client_key](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a8d88f5a8a6ccc8a9a883078af49ae96b)
- [wifi_enterprise_creds_params::server_key_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#a9500252974bd15037d4dbc41eba3a27d)
- [wifi_enterprise_creds_params::dh_param](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ab0fd7419d8a94d1d804e5554acfbf49a)
- [wifi_enterprise_creds_params::client_key2](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#abcda4d7820681d517d70d8f130b47050)
- [wifi_enterprise_creds_params::ca_cert2_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#abf35045e71afb0cb9ea25c635c5ac141)
- [wifi_enterprise_creds_params::dh_param_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ac548e0b006a9f7b858409cda7c3d34ba)
- [wifi_enterprise_creds_params::server_key](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#acb94a8885b5ab99d1a8fb33dffebc322)
- [wifi_enterprise_creds_params::server_cert_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ad0bfb59d3691e5d21cb4b810c4d1279e)
- [wifi_enterprise_creds_params::server_cert](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ad3621e92a1aa968c58a899ace72967db)
- [wifi_enterprise_creds_params::ca_cert2](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ad9b867873709d7f2363fef49d7b6f2ca)
- [wifi_enterprise_creds_params::client_cert2_len](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#adbe26c9b88f44eb6b875888f6a03e1bb)
- [wifi_enterprise_creds_params::ca_cert](../network_core_model_reference/P173_wifi_enterprise_creds_params_结构体.md#ae37381504a457b2f1d56dd5270c6711d)
- [wifi_filter_info::buffer_size](../network_core_model_reference/P174_wifi_filter_info_结构体.md#a1b2d0448fc7f62654e3f5aacfba62f8f)
- [wifi_filter_info::filter](../network_core_model_reference/P174_wifi_filter_info_结构体.md#ad9560be814299055cfa11b995a7dcf42)
- [wifi_filter_info::oper](../network_core_model_reference/P174_wifi_filter_info_结构体.md#aedd5e220cdde5768cb0f4aff920971cd)
- [wifi_filter_info::if_index](../network_core_model_reference/P174_wifi_filter_info_结构体.md#af9ea91e31e78afcb7ffe1ff9a04277a3)
- [wifi_iface_status::beacon_interval](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a241bfbe70628006b515b5f9e4f97665c)
- [wifi_iface_status::wpa3_ent_type](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a361c0e8a385fdc21f16258c25c2bc8d1)
- [wifi_iface_status::ssid](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a3ab671471bcdfeb5b955d156d39f2bb3)
- [wifi_iface_status::current_phy_tx_rate](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a43f239b0bc305e4c1c5f7fd9bb5753bf)
- [wifi_iface_status::rssi](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a4e593147b88eb4938d55a4de72fcc7f6)
- [wifi_iface_status::bssid](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a5d5d19056a1a15365fbdd94274a0fc5e)
- [wifi_iface_status::security](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a625ecec1abec8dd65cf155eab21a01b5)
- [wifi_iface_status::channel](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a6432663156e5b2c424d254ed1eae0144)
- [wifi_iface_status::wep_key_type](../network_core_model_reference/P175_wifi_iface_status_结构体.md#a9a899c28b51158e8973886f84d7d8950)
- [wifi_iface_status::mfp](../network_core_model_reference/P175_wifi_iface_status_结构体.md#aa1a9b644fd355526125ddd32416b7c24)
- [wifi_iface_status::dtim_period](../network_core_model_reference/P175_wifi_iface_status_结构体.md#aae6c8cbaa16c81d308f08114d5103a3d)
- [wifi_iface_status::state](../network_core_model_reference/P175_wifi_iface_status_结构体.md#ac52806155be3d64954ac6d109e76ec57)
- [wifi_iface_status::twt_capable](../network_core_model_reference/P175_wifi_iface_status_结构体.md#acfde8d64b463a9f553aa4fb689dc1917)
- [wifi_iface_status::iface_mode](../network_core_model_reference/P175_wifi_iface_status_结构体.md#ad33d2ec149a8d556e2472dd842ceadc0)
- [wifi_iface_status::ssid_len](../network_core_model_reference/P175_wifi_iface_status_结构体.md#ad82f281941e4f6ce1ef0bca008e26d41)
- [wifi_iface_status::band](../network_core_model_reference/P175_wifi_iface_status_结构体.md#ae1c141a18f4e225af2c22a8cb4f882a8)
- [wifi_iface_status::link_mode](../network_core_model_reference/P175_wifi_iface_status_结构体.md#ae2de076d79f2172793d65fe9cd31edc4)
- [wifi_mgmt_ops::ap_config_params](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a01b2ac4cd8a1f039bdba3adb2586d3cb)
- [wifi_mgmt_ops::set_bgscan](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a0aa02b0d69479b95d6e1a0971b16ee92)
- [wifi_mgmt_ops::mode](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a0bfeb2a8f463dc49ca3d433ee17d3dd9)
- [wifi_mgmt_ops::send_11k_neighbor_request](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a16fc04b7572234f6e7c207d82e0b4625)
- [wifi_mgmt_ops::set_bss_max_idle_period](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a26eaabf9621b16d332e20777b188d4ad)
- [wifi_mgmt_ops::ap_disable](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a3264be8040227d1e91a8223cabcd4e53)
- [wifi_mgmt_ops::channel](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a365e9aafc5399e1a9f37c9b4f347534c)
- [wifi_mgmt_ops::set_power_save](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a37e6c41f4b1223b8952171abb5cd9d89)
- [wifi_mgmt_ops::get_iface_caps](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a40d53afce76b5b7614ee95e41ea46635)
- [wifi_mgmt_ops::set_btwt](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a50421d54785d4f8d768c8a35fcda0ca5)
- [wifi_mgmt_ops::filter](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a5642ca19f2f25ba7a53d9efb30d7bd59)
- [wifi_mgmt_ops::bss_support_neighbor_rep](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a6198f23a4cdeb5b0e413b7a66c1fa442)
- [wifi_mgmt_ops::config_params](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a63e7bcc4d3bb9ee7e073a6c55abddcc2)
- [wifi_mgmt_ops::connect](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a65a4e87ee94aa5c7a551aa9b39289708)
- [wifi_mgmt_ops::candidate_scan](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a69f2ec3a03e77b4eb9d9fdd7315edf18)
- [wifi_mgmt_ops::pmksa_flush](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a76e76d96e307bc10bd14e4ea7b5dbed6)
- [wifi_mgmt_ops::get_version](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a7b788903271a427363d22808659a3ee9)
- [wifi_mgmt_ops::reset_stats](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a7bd0f326e9eeedbc3c768c5ecf207c06)
- [wifi_mgmt_ops::reg_domain](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a80b09c5ea77c99a4dfffb5a21f0c8867)
- [wifi_mgmt_ops::disconnect](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a8489951fc1baee17e56070187f4d77b0)
- [wifi_mgmt_ops::legacy_roam](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a8d37cec74b3d523257120b75f471e92f)
- [wifi_mgmt_ops::get_power_save_config](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a9278c8779748e64ad70cfbeef5a297dd)
- [wifi_mgmt_ops::iface_status](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#a930cbd9e4661d137ae37cd89afd451b2)
- [wifi_mgmt_ops::ap_enable](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#aa34fff15f9e0aadf244f9e0cf37b367b)
- [wifi_mgmt_ops::cfg_11k](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ab3b7dce2feb0ecbca3d4668dc9e41032)
- [wifi_mgmt_ops::get_conn_params](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ab5368326d558de972ce5806dd9a99f22)
- [wifi_mgmt_ops::wps_config](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ab8e11d463ff7000a090e0609f002a97c)
- [wifi_mgmt_ops::get_stats](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#abb2b7c033e77af36acde5d420effe8d1)
- [wifi_mgmt_ops::start_11r_roaming](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ac4ed6d4d1088f6e23d5256d156e42955)
- [wifi_mgmt_ops::bss_ext_capab](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ac6d82f5f2defdc657f056f0e6103e04b)
- [wifi_mgmt_ops::scan](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#acc20fd11dcd09edb72d03f8737801c06)
- [wifi_mgmt_ops::btm_query](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ad241d490ac3e10c58c87da004d706407)
- [wifi_mgmt_ops::get_rts_threshold](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ad3c8908b6a3752adf59d5a4170175f83)
- [wifi_mgmt_ops::ap_sta_disconnect](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#ad6e04312b0e7680f87ce801b2540db10)
- [wifi_mgmt_ops::set_rts_threshold](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#aed7b6daf7264c1450cc5d31530a2043a)
- [wifi_mgmt_ops::set_twt](../network_core_model_reference/P176_wifi_mgmt_ops_结构体.md#af2089cba9ba73593b8d5b4329f2fddff)
- [wifi_mode_info::oper](../network_core_model_reference/P177_wifi_mode_info_结构体.md#a57c101db8b81ab0ac5dd0a158057a64a)
- [wifi_mode_info::mode](../network_core_model_reference/P177_wifi_mode_info_结构体.md#aa29d3b88fc718aa3ac05daf38974707d)
- [wifi_mode_info::if_index](../network_core_model_reference/P177_wifi_mode_info_结构体.md#add58dd3b45fd2ddaf684d1b0de81bef9)
- [wifi_ps_config::ps_params](../network_core_model_reference/P180_wifi_ps_config_结构体.md#a357aafc2dedda37755b1cb1fc07fe5a6)
- [wifi_ps_config::num_twt_flows](../network_core_model_reference/P180_wifi_ps_config_结构体.md#a9e83c10eaaa1d721cbc49b40aedb00df)
- [wifi_ps_config::twt_flows](../network_core_model_reference/P180_wifi_ps_config_结构体.md#ab7460f0f253b2d552e49e98e2c770967)
- [wifi_ps_params::mode](../network_core_model_reference/P181_wifi_ps_params_结构体.md#a5a022d89d43ecf2cd1f15fc72c0f2bed)
- [wifi_ps_params::fail_reason](../network_core_model_reference/P181_wifi_ps_params_结构体.md#a63fa2ee03bc4aefada61c298ee14336c)
- [wifi_ps_params::wakeup_mode](../network_core_model_reference/P181_wifi_ps_params_结构体.md#a7cb3e7fb7d9f8bd7c2cab41f879b3b66)
- [wifi_ps_params::listen_interval](../network_core_model_reference/P181_wifi_ps_params_结构体.md#a8510c799ab0c5825f1c6349f9799c62f)
- [wifi_ps_params::exit_strategy](../network_core_model_reference/P181_wifi_ps_params_结构体.md#ab9fc62dd1e2928320274fa1554a550a6)
- [wifi_ps_params::enabled](../network_core_model_reference/P181_wifi_ps_params_结构体.md#abb22aaa45833ac130922204bd2fe841b)
- [wifi_ps_params::timeout_ms](../network_core_model_reference/P181_wifi_ps_params_结构体.md#ad963f1bf78dc271f08b73f3aadb36a91)
- [wifi_ps_params::type](../network_core_model_reference/P181_wifi_ps_params_结构体.md#aef62e5bf6216bf4dc461efe71735c4bd)
- [wifi_raw_scan_result::rssi](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md#a3f08580c6448a5fa28dd8a594fa7dad6)
- [wifi_raw_scan_result::data](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md#a5710e89199c147ce898602795f00aba3)
- [wifi_raw_scan_result::frame_length](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md#a876966f469714eb481b42ccc8a63945c)
- [wifi_raw_scan_result::frequency](../network_core_model_reference/P182_wifi_raw_scan_result_结构体.md#aa2c7781882c6775616cbc8016b0842f6)
- [wifi_reg_chan_info::center_frequency](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md#a0addffc11ef29f50c01b700835e59930)
- [wifi_reg_chan_info::dfs](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md#a1ab137c142902d2de7d6be2626d7ac1f)
- [wifi_reg_chan_info::supported](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md#aa044611e18b7332b8577e29f6a769e3f)
- [wifi_reg_chan_info::passive_only](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md#acc7a88b004c9a61c8bf9ee1a97f85928)
- [wifi_reg_chan_info::max_power](../network_core_model_reference/P183_wifi_reg_chan_info_结构体.md#af9169ab4a41fac4c6f6766fc96799545)
- [wifi_reg_domain::num_channels](../network_core_model_reference/P184_wifi_reg_domain_结构体.md#a3278e9f43893f49ab9f9d0d7f24009c1)
- [wifi_reg_domain::oper](../network_core_model_reference/P184_wifi_reg_domain_结构体.md#a3bbfdf1497a87bbb6b6211c7035e1002)
- [wifi_reg_domain::chan_info](../network_core_model_reference/P184_wifi_reg_domain_结构体.md#a4c8c9c11e41123cd7738fdb0d33ae5fb)
- [wifi_reg_domain::force](../network_core_model_reference/P184_wifi_reg_domain_结构体.md#a567c6fcae8032567aea83c18cd211c33)
- [wifi_reg_domain::country_code](../network_core_model_reference/P184_wifi_reg_domain_结构体.md#abf191495814c227fbbfaccb2f727762e)
- [wifi_scan_params::max_bss_cnt](../network_core_model_reference/P185_wifi_scan_params_结构体.md#a12d5dea7d8fa8ad03ac2366720c46243)
- [wifi_scan_params::dwell_time_active](../network_core_model_reference/P185_wifi_scan_params_结构体.md#a2453a75c23e04e3572559c0e7199c1b4)
- [wifi_scan_params::scan_type](../network_core_model_reference/P185_wifi_scan_params_结构体.md#a645acc54603cd4692527c1a028933078)
- [wifi_scan_params::bands](../network_core_model_reference/P185_wifi_scan_params_结构体.md#a6b571d960ed9d7419e31530e5fb6f97a)
- [wifi_scan_params::dwell_time_passive](../network_core_model_reference/P185_wifi_scan_params_结构体.md#a8e7a37ccda8de635e7b7066d7943e814)
- [wifi_scan_params::band_chan](../network_core_model_reference/P185_wifi_scan_params_结构体.md#aa5ddbd6bc97b7598288d4b0d38521681)
- [wifi_scan_params::ssids](../network_core_model_reference/P185_wifi_scan_params_结构体.md#aac11ee8e0ec8a4fa24668f4820bd1a12)
- [wifi_scan_result::ssid_length](../network_core_model_reference/P186_wifi_scan_result_结构体.md#a2c1c2f4265b914df08fc75deb8b69d39)
- [wifi_scan_result::band](../network_core_model_reference/P186_wifi_scan_result_结构体.md#a38201c9dd798dc11b5bda3ce97b02e92)
- [wifi_scan_result::mac](../network_core_model_reference/P186_wifi_scan_result_结构体.md#a4fdbc4dc4d5c8b279223e8c06624f434)
- [wifi_scan_result::rssi](../network_core_model_reference/P186_wifi_scan_result_结构体.md#a76aa012136e3721fd4a482a22b93546f)
- [wifi_scan_result::mac_length](../network_core_model_reference/P186_wifi_scan_result_结构体.md#a8fca0dabec00ebd7ed4800098ec9d451)
- [wifi_scan_result::ssid](../network_core_model_reference/P186_wifi_scan_result_结构体.md#aaefb8f5c9510e4f5002ae306d853ade8)
- [wifi_scan_result::wpa3_ent_type](../network_core_model_reference/P186_wifi_scan_result_结构体.md#abb7de47c605ec05c8fe0a06ecbd2b7b6)
- [wifi_scan_result::mfp](../network_core_model_reference/P186_wifi_scan_result_结构体.md#acaa3fb30ebf6df22bfac6380698ed28e)
- [wifi_scan_result::channel](../network_core_model_reference/P186_wifi_scan_result_结构体.md#adbbfd7692ee5ffd6344fe78b9d91c840)
- [wifi_scan_result::security](../network_core_model_reference/P186_wifi_scan_result_结构体.md#af2d3dc5d115e3db76d3bc115510b0a5a)
- [wifi_status::ap_status](../network_core_model_reference/P187_wifi_status_结构体.md#a02f0fcc7ef57661ca95d0c99f045aef1)
- [wifi_status::reason_code](../network_core_model_reference/P187_wifi_status_结构体.md#a8c63d5fecc9d532366c144b4dd7bb2ad)
- [wifi_status::conn_status](../network_core_model_reference/P187_wifi_status_结构体.md#a8f885e78366d0499e4ba8e15bef275ac)
- [wifi_status::disconn_reason](../network_core_model_reference/P187_wifi_status_结构体.md#aa04b5033d93274badd27f702af9830bc)
- [wifi_status::status](../network_core_model_reference/P187_wifi_status_结构体.md#aa1dbff8154400f8353693d387977008b)
- [wifi_status::status_code](../network_core_model_reference/P187_wifi_status_结构体.md#ac8a85738dcfa60dfaf502d86b8294f78)
- [wifi_twt_flow_info::dialog_token](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#a123ce10bed8b62b01919a7ea7644a0ba)
- [wifi_twt_flow_info::negotiation_type](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#a620ae8ba546e4091d74280cb1553b2cf)
- [wifi_twt_flow_info::twt_wake_ahead_duration](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#a6384d3829d54a58a53eafcb74c64a658)
- [wifi_twt_flow_info::trigger](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#a952a67bd092c5dadba387bb13449c6f3)
- [wifi_twt_flow_info::responder](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#ac82e4de8ffc82f851061f8ba8d217dc1)
- [wifi_twt_flow_info::flow_id](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#acb0c618f1cebcb172f342cfe222683be)
- [wifi_twt_flow_info::twt_interval](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#ae15ba49fa54f82cc6a1fb0d4572114b7)
- [wifi_twt_flow_info::twt_wake_interval](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#aede6cb0cfc999fac8ded49e2981a3762)
- [wifi_twt_flow_info::implicit](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#afb480be82d1c6f351bd634fd83bfa5c7)
- [wifi_twt_flow_info::announce](../network_core_model_reference/P188_wifi_twt_flow_info_结构体.md#afc81a5111c265fd9bb2aca5f9510bfa8)
- [wifi_twt_params::announce](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a02f2d822d530e5376f256503439a54f9)
- [wifi_twt_params::teardown_all](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a26d6bda00452f77832f69f4465c13efb)
- [wifi_twt_params::setup_cmd](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a347f8cff73ee6b6ba6d15ddf6f376a2d)
- [wifi_twt_params::btwt_offset](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a4459cf19226e199d23ae0cd1d7132b73)
- [wifi_twt_params::trigger](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a4e822c04b52fe6a9489e48e26b8f9382)
- [wifi_twt_params::negotiation_type](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a5fd269328f68838b8a7e3a0b93eed894)
- [wifi_twt_params::operation](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a6f0483861a387651c9c89ba182e064bd)
- [wifi_twt_params::twt_wake_ahead_duration](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a6f907ca412251fdd7391f29bfa6d7713)
- [wifi_twt_params::fail_reason](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a70f58b502bb67ef3b2068ded2160b612)
- [wifi_twt_params::btwt](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a72ab809144b1dd3e7e121e489ef399e2)
- [wifi_twt_params::twt_wake_interval](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a7c297459a17ed2fd232c62cca63e952f)
- [wifi_twt_params::btwt_li](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a7e7c786c51d3bc70af135bad88ebde4f)
- [wifi_twt_params::resp_status](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a805a23284ed4afa46b84efcd43329beb)
- [wifi_twt_params::implicit](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a8ea1e2501c8b69dc3fa606eb360f8678)
- [wifi_twt_params::flow_id](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a95ec4b32d37309efa47256ae1ea865da)
- [wifi_twt_params::teardown_status](../network_core_model_reference/P189_wifi_twt_params_结构体.md#a9faff59e577775b3fe53f2139462ac71)
- [wifi_twt_params::btwt_sta_wait](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aa05e5fa6a519f700147bb99d6e69a06b)
- [wifi_twt_params::btwt_set_cfg](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aa11562186ea265b906861269bc8a692b)
- [wifi_twt_params::twt_exponent](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aabb77296f007cb055f78fa1ec3d155a3)
- [wifi_twt_params::twt_mantissa](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aadad4556e2e5405b0703ebb4233a4d17)
- [wifi_twt_params::teardown](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aadf62f6386359ad15491d0073c9065bf)
- [wifi_twt_params::twt_interval](../network_core_model_reference/P189_wifi_twt_params_结构体.md#ab92fe571559fcd5d97cdf7e6b7d86681)
- [wifi_twt_params::twt_info_disable](../network_core_model_reference/P189_wifi_twt_params_结构体.md#ac02eab9593b1ec2c9a0453a67076df88)
- [wifi_twt_params::dialog_token](../network_core_model_reference/P189_wifi_twt_params_结构体.md#adda47e302a87a766f18e28016963a561)
- [wifi_twt_params::responder](../network_core_model_reference/P189_wifi_twt_params_结构体.md#ae547c6fc1c7cbad15bebcfdaa43f59e7)
- [wifi_twt_params::setup](../network_core_model_reference/P189_wifi_twt_params_结构体.md#aee57c0189b210cfcc18e213e35b9479c)
- [wifi_twt_params::btwt_count](../network_core_model_reference/P189_wifi_twt_params_结构体.md#afc563010a33624bf01feac1292f0871d)
- [wifi_version::fw_version](../network_core_model_reference/P190_wifi_version_结构体.md#a4bf2cbdf5c43ff21718ccf19646c164e)
- [wifi_version::drv_version](../network_core_model_reference/P190_wifi_version_结构体.md#aea828bdb512440d6aa3cc853525c4971)
- [wifi_wps_config_params::pin](../network_core_model_reference/P191_wifi_wps_config_params_结构体.md#a962bd6513c564150e0c75112b96bbe15)
- [wifi_wps_config_params::oper](../network_core_model_reference/P191_wifi_wps_config_params_结构体.md#aa7a10889c5cd5124983b0f7242d23b7e)
- [wifi.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html)

---

[上一章](P008_posix_signal.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P010_wuc_nxp_wuu.h_源码浏览.md)
