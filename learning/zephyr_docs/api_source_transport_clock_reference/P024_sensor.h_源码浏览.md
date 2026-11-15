---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-24
title: sensor.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_sensor.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)。

## 24.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00014"></a>
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
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
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
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="foldopen00269"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="foldopen00281"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="foldopen00293"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="foldopen00300"></a>
<a id="l00300"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="foldopen00374"></a>
<a id="l00374"></a>
<a id="l00376"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="foldopen00384"></a>
<a id="l00384"></a>
<a id="l00389"></a>
<a id="l00391"></a>
<a id="l00393"></a>
<a id="l00395"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00411"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00420"></a>
<a id="l00422"></a>
<a id="l00424"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00437"></a>
<a id="l00439"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00470"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="foldopen00535"></a>
<a id="l00535"></a>
<a id="l00539"></a>
<a id="l00543"></a>
<a id="l00547"></a>
<a id="l00551"></a>
<a id="l00555"></a>
<a id="l00559"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00568"></a>
<a id="foldopen00577"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00587"></a>
<a id="foldopen00596"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="foldopen00609"></a>
<a id="l00609"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="foldopen00699"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="foldopen00709"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="foldopen00725"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="foldopen00736"></a>
<a id="l00736"></a>
<a id="l00738"></a>
<a id="l00740"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="foldopen00745"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="foldopen00750"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="foldopen00759"></a>
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
<a id="foldopen00815"></a>
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
<a id="foldopen00916"></a>
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
<a id="l00947"></a>
<a id="l00948"></a>
<a id="l00949"></a>
<a id="l00950"></a>
<a id="l00951"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00975"></a>
<a id="l00976"></a>
<a id="l00977"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
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
<a id="foldopen01021"></a>
<a id="l01021"></a>
<a id="l01023"></a>
<a id="l01024"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01033"></a>
<a id="l01034"></a>
<a id="l01035"></a>
<a id="l01036"></a>
<a id="l01037"></a>
<a id="l01039"></a>
<a id="l01040"></a>
<a id="l01041"></a>
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
<a id="foldopen01108"></a>
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
<a id="foldopen01145"></a>
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
<a id="foldopen01187"></a>
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
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01231"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="l01234"></a>
<a id="l01238"></a>
<a id="l01239"></a>
<a id="l01243"></a>
<a id="l01244"></a>
<a id="foldopen01253"></a>
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
<a id="foldopen01270"></a>
<a id="l01270"></a>
<a id="l01271"></a>
<a id="l01272"></a>
<a id="l01273"></a>
<a id="l01274"></a>
<a id="l01275"></a>
<a id="foldopen01284"></a>
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
<a id="foldopen01303"></a>
<a id="l01303"></a>
<a id="l01304"></a>
<a id="l01305"></a>
<a id="l01306"></a>
<a id="l01307"></a>
<a id="l01308"></a>
<a id="l01309"></a>
<a id="foldopen01316"></a>
<a id="l01316"></a>
<a id="l01317"></a>
<a id="l01318"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="foldopen01329"></a>
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
<a id="foldopen01346"></a>
<a id="l01346"></a>
<a id="l01347"></a>
<a id="l01348"></a>
<a id="l01349"></a>
<a id="l01350"></a>
<a id="l01351"></a>
<a id="foldopen01363"></a>
<a id="l01363"></a>
<a id="l01364"></a>
<a id="l01365"></a>
<a id="l01366"></a>
<a id="l01367"></a>
<a id="l01368"></a>
<a id="l01369"></a>
<a id="foldopen01376"></a>
<a id="l01376"></a>
<a id="l01377"></a>
<a id="l01378"></a>
<a id="l01379"></a>
<a id="l01380"></a>
<a id="l01381"></a>
<a id="foldopen01388"></a>
<a id="l01388"></a>
<a id="l01389"></a>
<a id="l01390"></a>
<a id="l01391"></a>
<a id="l01392"></a>
<a id="foldopen01399"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01402"></a>
<a id="l01403"></a>
<a id="foldopen01414"></a>
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
<a id="foldopen01449"></a>
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
<a id="foldopen01471"></a>
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
<a id="foldopen01496"></a>
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
<a id="l01584"></a>
<a id="l01585"></a>
<a id="l01586"></a>
<a id="l01587"></a>
<a id="l01588"></a>
<a id="l01589"></a>
<a id="l01590"></a>
<a id="l01591"></a>
<a id="l01592"></a>
<a id="foldopen01602"></a>
<a id="l01602"></a>
<a id="l01603"></a>
<a id="l01604"></a>
<a id="foldopen01611"></a>
<a id="l01611"></a>
<a id="l01612"></a>
<a id="l01613"></a>
<a id="l01614"></a>
<a id="l01615"></a>
<a id="foldopen01622"></a>
<a id="l01622"></a>
<a id="l01623"></a>
<a id="l01624"></a>
<a id="l01625"></a>
<a id="l01626"></a>
<a id="foldopen01633"></a>
<a id="l01633"></a>
<a id="l01634"></a>
<a id="l01635"></a>
<a id="l01636"></a>
<a id="l01637"></a>
<a id="foldopen01644"></a>
<a id="l01644"></a>
<a id="l01645"></a>
<a id="l01646"></a>
<a id="l01647"></a>
<a id="l01648"></a>
<a id="foldopen01656"></a>
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
<a id="foldopen01676"></a>
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
<a id="foldopen01697"></a>
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
<a id="l01716"></a>
<a id="l01717"></a>
<a id="l01718"></a>
<a id="l01719"></a>
<a id="l01720"></a>
<a id="foldopen01729"></a>
<a id="l01729"></a>
<a id="l01730"></a>
<a id="l01731"></a>
<a id="l01732"></a>
<a id="l01733"></a>
<a id="l01734"></a>
<a id="l01735"></a>
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
<a id="l01746"></a>
<a id="l01747"></a>
<a id="l01748"></a>
<a id="l01749"></a>
<a id="l01750"></a>
<a id="l01751"></a>
<a id="l01752"></a>
<a id="foldopen01761"></a>
<a id="l01761"></a>
<a id="l01762"></a>
<a id="l01763"></a>
<a id="l01764"></a>
<a id="l01765"></a>
<a id="l01766"></a>
<a id="l01767"></a>
<a id="l01768"></a>
<a id="l01769"></a>
<a id="l01770"></a>
<a id="l01771"></a>
<a id="l01772"></a>
<a id="l01773"></a>
<a id="l01774"></a>
<a id="l01775"></a>
<a id="l01776"></a>
<a id="l01777"></a>
<a id="l01778"></a>
<a id="l01779"></a>
<a id="l01780"></a>
<a id="foldopen01789"></a>
<a id="l01789"></a>
<a id="l01790"></a>
<a id="l01791"></a>
<a id="l01792"></a>
<a id="l01793"></a>
<a id="l01794"></a>
<a id="l01795"></a>
<a id="l01796"></a>
<a id="l01797"></a>
<a id="l01798"></a>
<a id="l01799"></a>
<a id="l01800"></a>
<a id="l01801"></a>
<a id="l01802"></a>
<a id="l01803"></a>
<a id="l01804"></a>
<a id="l01805"></a>
<a id="l01806"></a>
<a id="l01807"></a>
<a id="l01811"></a>
<a id="l01817"></a>
<a id="l01818"></a>
<a id="foldopen01826"></a>
<a id="l01826"></a>
<a id="l01827"></a>
<a id="l01828"></a>
<a id="foldopen01844"></a>
<a id="l01844"></a>
<a id="l01845"></a>
<a id="l01846"></a>
<a id="l01847"></a>
<a id="l01848"></a>
<a id="l01849"></a>
<a id="l01850"></a>
<a id="l01851"></a>
<a id="l01852"></a>
<a id="l01853"></a>
<a id="l01854"></a>
<a id="l01855"></a>
<a id="l01856"></a>
<a id="l01857"></a>
<a id="l01858"></a>
<a id="l01859"></a>
<a id="l01860"></a>
<a id="l01861"></a>
<a id="l01862"></a>
<a id="l01863"></a>
<a id="l01864"></a>
<a id="l01865"></a>
<a id="l01866"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__devicetree-generic-foreach_html_ga926f68202042c9db05390e628787f916"></a>
<a id="agroup__rtio__sqe__prio_html_gab02e27e01b7dd4eb3439df557899ce92"></a>
<a id="agroup__rtio_html_ga15c1f623658d27d300d1a31a6f3d6b9d"></a>
<a id="agroup__rtio_html_ga4ac49ea0ef01717caadfcd8b781dcc7b"></a>
<a id="agroup__rtio_html_ga65e351af0a16dcf504a51ef4eb9316c7"></a>
<a id="agroup__rtio_html_ga77506a320d6e31c6aeb2951312890295"></a>
<a id="agroup__rtio_html_ga7ff7d0337e43b0a9380bb94a4a143a47"></a>
<a id="agroup__rtio_html_ga89c7cc2494e3dda50737f78f1a1376cf"></a>
<a id="agroup__rtio_html_ga8b47c954d15a334621def53acceb6799"></a>
<a id="agroup__rtio_html_ga9803aa829f8c0eeee746ea7d872c20cc"></a>
<a id="agroup__rtio_html_gaa0799a5f8ad98425d385a07c5d27d9cb"></a>
<a id="agroup__rtio_html_gaf617d05d9b59ce1f1d0697617ef6f249"></a>
<a id="agroup__rtio_html_gafee27c64a4a4989c4eb774addde8eb2e"></a>
<a id="agroup__sensor__interface__backend_html_ga00d05c82b46e56dca5f6e8f7f01c31b8"></a>
<a id="agroup__sensor__interface__backend_html_ga21e407d552d140cfb6bfd0d9513c7d42"></a>
<a id="agroup__sensor__interface__backend_html_ga38422ace4194a66a9a912a8ef1e088fb"></a>
<a id="agroup__sensor__interface__backend_html_ga5c9b5ed9097464562004b446856043fd"></a>
<a id="agroup__sensor__interface__backend_html_gacae110a4edb6f29dfb457cb1ea8d68c1"></a>
<a id="agroup__sensor__interface__backend_html_gad77732c8f0ec5520cdd71c2829787981"></a>
<a id="agroup__sensor__interface__backend_html_gad7f7a3d9e714cc16f23656ca06592aa4"></a>
<a id="agroup__sensor__interface_html_ga0066e049c4f084305ca2b978e5c7454d"></a>
<a id="agroup__sensor__interface_html_ga018bca56056ae2558f9e45aeb2fa5f53"></a>
<a id="agroup__sensor__interface_html_ga040a907c8934baab66d27b8dfb1ea220"></a>
<a id="agroup__sensor__interface_html_ga08215279400e8c9eb05ce4e4f0898ffd"></a>
<a id="agroup__sensor__interface_html_ga0dcb6842bc969492bd1c9eb49708940b"></a>
<a id="agroup__sensor__interface_html_ga12db6fc43adce48d34c25c16fd2336a3"></a>
<a id="agroup__sensor__interface_html_ga28a1c6cf74a391712a4697792f759d62"></a>
<a id="agroup__sensor__interface_html_ga29223b754dc436ab1e97ce6209a3ea06"></a>
<a id="agroup__sensor__interface_html_ga2ad1fc2abd1c8c38e7de6e99fa5c1f20"></a>
<a id="agroup__sensor__interface_html_ga2b045cdbd4d1ca37beed69970093945b"></a>
<a id="agroup__sensor__interface_html_ga39d4b84f5d792e27b2d6d5eb6a2ccb0d"></a>
<a id="agroup__sensor__interface_html_ga3db980100e634310a0a1623136048742"></a>
<a id="agroup__sensor__interface_html_ga58bb95758fc4bd2927c93671727e6080"></a>
<a id="agroup__sensor__interface_html_ga64d5a1725eda200c80daf42b1067c46c"></a>
<a id="agroup__sensor__interface_html_ga6ab9ce9c6ee2e52d197e5cb4ccd88979"></a>
<a id="agroup__sensor__interface_html_ga6d69a9644e08a9cd7773645fa11293e3"></a>
<a id="agroup__sensor__interface_html_ga6ebdc2f6942334de3cc248a53db7df33"></a>
<a id="agroup__sensor__interface_html_ga759d6581b83751bab5e56b9f8bb1676d"></a>
<a id="agroup__sensor__interface_html_ga767c7d0147699c556a2f4d429501ff99"></a>
<a id="agroup__sensor__interface_html_ga7c72aca732e0641612d2f9437c2e41b7"></a>
<a id="agroup__sensor__interface_html_ga8613a20521a37d40fd7371dc63ba2dac"></a>
<a id="agroup__sensor__interface_html_ga88b2605526e37420db871f066c5053b3"></a>
<a id="agroup__sensor__interface_html_ga890c1fb6d6974aea22a2d08829a75902"></a>
<a id="agroup__sensor__interface_html_ga8d6f33eeda04bdb648bd03a92e981b1d"></a>
<a id="agroup__sensor__interface_html_ga9bf7faf60aa54a7540e9b73a61864e25"></a>
<a id="agroup__sensor__interface_html_ga9e0e6c1408d32c52267984bae7cb268d"></a>
<a id="agroup__sensor__interface_html_ga9e0fb14f84dca02497ce5bff10b51ab8"></a>
<a id="agroup__sensor__interface_html_gaa75e25d93ee7cac0bf38399f3c006dff"></a>
<a id="agroup__sensor__interface_html_gaa8cd6e4fadb5d69e59d101733b4fb462"></a>
<a id="agroup__sensor__interface_html_gaaa1b502bc029b10d7b23b0a25ef4e934"></a>
<a id="agroup__sensor__interface_html_gab4c95b7857294a9148afe6e9bcb5eacf"></a>
<a id="agroup__sensor__interface_html_gab53418e1eb164364663d3ec3f40399a4"></a>
<a id="agroup__sensor__interface_html_gab797f2f578b1c9cc44f54ab5d503bbf8"></a>
<a id="agroup__sensor__interface_html_gabb076531445e1b128d515b28c7cc9dc8"></a>
<a id="agroup__sensor__interface_html_gabbcb8ad4b9484cba77ae65e2d3ba7457"></a>
<a id="agroup__sensor__interface_html_gabf3b46a1e88e65575e25acc1a43aba10"></a>
<a id="agroup__sensor__interface_html_gabff019c63c89cbc546c0981819040c99"></a>
<a id="agroup__sensor__interface_html_gac16192826432438a15274cf28d66e8a6"></a>
<a id="agroup__sensor__interface_html_gac17a55d53ccd2a2e8b45109e984cc80b"></a>
<a id="agroup__sensor__interface_html_gacdb8dc2095e6a15db0a58233cab8ffe2"></a>
<a id="agroup__sensor__interface_html_gace7f20e29b302e607ba274fe40a2c2bd"></a>
<a id="agroup__sensor__interface_html_gad80093a6cfe95428dd0ead85547838a6"></a>
<a id="agroup__sensor__interface_html_gae812fb481bfe3a8053f0fc23f8617434"></a>
<a id="agroup__sensor__interface_html_gae95715ffea5da18a9593ec2add029824"></a>
<a id="agroup__sensor__interface_html_gaedfdfc71dce702dc1fb1c6e60ff0f73a"></a>
<a id="agroup__sensor__interface_html_gaf01bbb251ad0c7f6c55c5b702e8a4048"></a>
<a id="agroup__sensor__interface_html_gaf53b015c47acab3c3acb4cb1d8ab827d"></a>
<a id="agroup__sensor__interface_html_gafbf65226a227e9f8824908bc38e336f5"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda2bc31b6e790488eb7c9031107676b409"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffdabbdff0ba5072a376190c4a1272b2c4cf"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba7f20835b052b1bd6374e56f66e0f285d"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba87d853ad38f41c897bda106a7c66c08c"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bac778fe666c284078117b2083779ba7a3"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="agroup__sensor__interface_html_gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315"></a>
<a id="agroup__sensor__interface_html_gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d"></a>
<a id="agroup__sensor__interface_html_gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a0893cbc829c2a3b896f12874cc96c872"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a17bcfa0e34eecf45e17988720471c8f9"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a26fe67f0313062c6bf841ff8b829f7ff"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a3905467a96940ada0dbdef6ff8ee1a8a"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a39b13669a3006ead32275d1578677127"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a3afc97258f1340ef047a055dc5a69e4c"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a486ea8968daed9d1c3802a3babcdcfad"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a4b5a3a92ce610a2b3c9f113c93aef212"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a4d8c9e992c590bb17291471d8634a3a2"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a6d19454f164337c9cf163dc1dfaf2b42"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a6dfcb28f053feeb7fca51a6c92b6c4ab"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a7746b596d101dde6afbf73f5994b5ec2"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a88001b6464b2419dbf2aa4ad59556110"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a9e45f64b48f96650f0e75c3728324379"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934aa659bdadf3905703afe9bcf6dd0be82e"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934aabd79bd1d8600c852260c0a8afc372e6"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934aadd0d7e0e77db8bd11da1866786b3a6a"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934aaee5947abb6490ec06d9f5984bfa4060"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934adcef73d7ea6cac2e251f96ecf9fa8ea4"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e"></a>
<a id="agroup__sys-util_html_ga0ba9d4ab383eba522e345594aaa2bb3f"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="agroup__sys-util_html_ga1a138896caafcb2429a6483ea7412d12"></a>
<a id="agroup__sys-util_html_ga1ffeb18b8ed73d37c2485c82988ed1ec"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_ga3c12c6d36ad0aa481a3436923d21f4f8"></a>
<a id="agroup__sys-util_html_gaea00fb0c11b73f77da8884374e2121b4"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__system__errno_html_ga6a05c923dad0c1208043e9c20a58c8e5"></a>
<a id="agroup__system__errno_html_gaa1591a4f3a86360108de5b9ba34980ca"></a>
<a id="ainclude_2zephyr_2dsp_2types_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="artio_2rtio_8h_html"></a>
<a id="asensor__data__types_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a181807730d4a375f848ba139813ce04f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_a688eb21a22db27c2b2bd5836943cdcbe"></a>
<a id="astdint_8h_html_ac58f2c111cc9989c86db2a7dc4fd84ca"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdlib_8h_html"></a>
<a id="astring_8h_html_af0f01bffcd16daa9143f6014d10a25ad"></a>
<a id="astructdevice_html"></a>
<a id="astructrtio__cqe_html"></a>
<a id="astructrtio__cqe_html_a15128387ccbea55812ef229eab7241e7"></a>
<a id="astructrtio__cqe_html_acbe2e6607a752b676d9336b9ca6ce435"></a>
<a id="astructrtio__iodev__api_html"></a>
<a id="astructrtio__iodev__sqe_html"></a>
<a id="astructrtio__iodev__sqe_html_a2bd98599678909c0ddb22f879affa12b"></a>
<a id="astructrtio__iodev_html"></a>
<a id="astructrtio__iodev_html_af0f3a27fe8dea2161c9a73cb838bdeec"></a>
<a id="astructrtio__sqe_html"></a>
<a id="astructrtio__sqe_html_a0ed519ee0b5867ff73bdaf37f983c971"></a>
<a id="astructrtio__sqe_html_a67376f40a13960b152a23da250275722"></a>
<a id="astructrtio__sqe_html_a6c784702f011592c84feacd57915bbfc"></a>
<a id="astructrtio__sqe_html_ab71176c084e8b8eb65dfeb3018ae2a49"></a>
<a id="astructrtio_html"></a>
<a id="astructsensor__chan__spec_html"></a>
<a id="astructsensor__chan__spec_html_a00d4a927cfeae33b2beea8cdc415dda1"></a>
<a id="astructsensor__chan__spec_html_a1b2f0ecdc23e0d235536eb5fcdeeb63c"></a>
<a id="astructsensor__data__generic__header_html"></a>
<a id="astructsensor__data__generic__header_html_a429e22b3191df271ccfe321b796e1ac9"></a>
<a id="astructsensor__data__generic__header_html_a68067521c1058b6802176e1d48fed788"></a>
<a id="astructsensor__data__generic__header_html_a7edbe674f28c95f3aa40b1df84ca61fe"></a>
<a id="astructsensor__data__generic__header_html_ac09f23959c66ff75b0854a95e8d4504b"></a>
<a id="astructsensor__decode__context_html"></a>
<a id="astructsensor__decode__context_html_a1ac0773e83a086455371d108264ef4f6"></a>
<a id="astructsensor__decode__context_html_a1c051bd8d0030f81cc561e32b2897d74"></a>
<a id="astructsensor__decode__context_html_a23e27eb0687d722be78e1b89278613d1"></a>
<a id="astructsensor__decode__context_html_ada9e40625829093087886c41f2fb7350"></a>
<a id="astructsensor__decoder__api_html"></a>
<a id="astructsensor__decoder__api_html_a026be8086386e9eea0a1cb25c1cd602e"></a>
<a id="astructsensor__decoder__api_html_a0693dd5369a21c12ce4539ad2dd8940e"></a>
<a id="astructsensor__decoder__api_html_a2d219ff0ea1ce71976a5e81814e3a3ff"></a>
<a id="astructsensor__decoder__api_html_a78706bae0f1314615b5804736ef43493"></a>
<a id="astructsensor__driver__api_html"></a>
<a id="astructsensor__driver__api_html_a004f9d342805dc72249ab9b8c17a544b"></a>
<a id="astructsensor__driver__api_html_a2d230a976b19a699d132034f58bb2b6a"></a>
<a id="astructsensor__driver__api_html_a3e28950f844c3f8b8da5ba9ff8052e46"></a>
<a id="astructsensor__driver__api_html_a4708070fd6654ecbbe631819aba319bd"></a>
<a id="astructsensor__driver__api_html_a4b40e25b81fe070e2f6bdcf7f8a4a31f"></a>
<a id="astructsensor__driver__api_html_a667b41bf51f2c7a6bb31713fbf889113"></a>
<a id="astructsensor__driver__api_html_ae3ba0adeba21351e8f660896e5a0e702"></a>
<a id="astructsensor__read__config_html"></a>
<a id="astructsensor__read__config_html_a2aff44f02b25fd4ad1d4bc217800fad1"></a>
<a id="astructsensor__read__config_html_a5236049e0563ebba754994d70e22383a"></a>
<a id="astructsensor__read__config_html_a6eaa6df7bc9378abe0f5b4b8c9a05909"></a>
<a id="astructsensor__read__config_html_aca96de2c23fb63f887c4c40dcb272798"></a>
<a id="astructsensor__read__config_html_ad49d5ab5293017d1ad2cf60adc542090"></a>
<a id="astructsensor__read__config_html_aecb9c899e292fdb25c3c990bdaf1c76b"></a>
<a id="astructsensor__stream__trigger_html"></a>
<a id="astructsensor__stream__trigger_html_a62ccdecf7253b1bfdff4f1d659563d76"></a>
<a id="astructsensor__stream__trigger_html_a9a367e746764e68140ec9120f2a016e6"></a>
<a id="astructsensor__trigger_html"></a>
<a id="astructsensor__trigger_html_ac2cce1ec6ff82f95cb06d0dccafd7af0"></a>
<a id="astructsensor__trigger_html_ae01f99b124aa99c59b9967818022e112"></a>
<a id="astructsensor__value_html"></a>
<a id="astructsensor__value_html_a91f81bd0f5da69084cf3c629fde68a1b"></a>
<a id="astructsensor__value_html_af21dddb084da4c42a7e77b48edf26fbe"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
* Copyright (c) 2016 Intel Corporation
*
* SPDX-License-Identifier: Apache-2.0
*/
#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_H_



#include <errno.h>
#include <stdlib.h>

#include <zephyr/device.h>
#include <zephyr/drivers/sensor_data_types.h>
#include <zephyr/dsp/types.h>
#include <zephyr/rtio/rtio.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/util.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

struct sensor_value {
        int32_t val1;
        int32_t val2;
};

enum sensor_channel {
        SENSOR_CHAN_ACCEL_X,
        SENSOR_CHAN_ACCEL_Y,
        SENSOR_CHAN_ACCEL_Z,
        SENSOR_CHAN_ACCEL_XYZ,
        SENSOR_CHAN_GYRO_X,
        SENSOR_CHAN_GYRO_Y,
        SENSOR_CHAN_GYRO_Z,
        SENSOR_CHAN_GYRO_XYZ,
        SENSOR_CHAN_MAGN_X,
        SENSOR_CHAN_MAGN_Y,
        SENSOR_CHAN_MAGN_Z,
        SENSOR_CHAN_MAGN_XYZ,
        SENSOR_CHAN_DIE_TEMP,
        SENSOR_CHAN_AMBIENT_TEMP,
        SENSOR_CHAN_PRESS,
        SENSOR_CHAN_PROX,
        SENSOR_CHAN_HUMIDITY,
        SENSOR_CHAN_AMBIENT_LIGHT,
        SENSOR_CHAN_LIGHT,
        SENSOR_CHAN_IR,
        SENSOR_CHAN_RED,
        SENSOR_CHAN_GREEN,
        SENSOR_CHAN_BLUE,
        SENSOR_CHAN_ALTITUDE,

        SENSOR_CHAN_PM_1_0_CF,
        SENSOR_CHAN_PM_2_5_CF,
        SENSOR_CHAN_PM_10_CF,
        SENSOR_CHAN_PM_1_0,
        SENSOR_CHAN_PM_2_5,
        SENSOR_CHAN_PM_10,
        SENSOR_CHAN_PM_0_3_COUNT,
        SENSOR_CHAN_PM_0_5_COUNT,
        SENSOR_CHAN_PM_1_0_COUNT,
        SENSOR_CHAN_PM_2_5_COUNT,
        SENSOR_CHAN_PM_5_COUNT,
        SENSOR_CHAN_PM_10_COUNT,

        SENSOR_CHAN_DISTANCE,

        SENSOR_CHAN_CO2,
        SENSOR_CHAN_O2,
        SENSOR_CHAN_VOC,
        SENSOR_CHAN_GAS_RES,
        SENSOR_CHAN_FLOW_RATE,
        SENSOR_CHAN_VOLUME,

        SENSOR_CHAN_VOLTAGE,

        SENSOR_CHAN_VSHUNT,

        SENSOR_CHAN_CURRENT,
        SENSOR_CHAN_POWER,

        SENSOR_CHAN_RESISTANCE,

        SENSOR_CHAN_ROTATION,

        SENSOR_CHAN_POS_DX,
        SENSOR_CHAN_POS_DY,
        SENSOR_CHAN_POS_DZ,
        SENSOR_CHAN_POS_DXYZ,

        SENSOR_CHAN_RPM,

        SENSOR_CHAN_FREQUENCY,

        SENSOR_CHAN_GAUGE_VOLTAGE,
        SENSOR_CHAN_GAUGE_AVG_CURRENT,
        SENSOR_CHAN_GAUGE_STDBY_CURRENT,
        SENSOR_CHAN_GAUGE_MAX_LOAD_CURRENT,
        SENSOR_CHAN_GAUGE_TEMP,
        SENSOR_CHAN_GAUGE_STATE_OF_CHARGE,
        SENSOR_CHAN_GAUGE_FULL_CHARGE_CAPACITY,
        SENSOR_CHAN_GAUGE_REMAINING_CHARGE_CAPACITY,
        SENSOR_CHAN_GAUGE_NOM_AVAIL_CAPACITY,
        SENSOR_CHAN_GAUGE_FULL_AVAIL_CAPACITY,
        SENSOR_CHAN_GAUGE_AVG_POWER,
        SENSOR_CHAN_GAUGE_STATE_OF_HEALTH,
        SENSOR_CHAN_GAUGE_TIME_TO_EMPTY,
        SENSOR_CHAN_GAUGE_TIME_TO_FULL,
        SENSOR_CHAN_GAUGE_CYCLE_COUNT,
        SENSOR_CHAN_GAUGE_DESIGN_VOLTAGE,
        SENSOR_CHAN_GAUGE_DESIRED_VOLTAGE,
        SENSOR_CHAN_GAUGE_DESIRED_CHARGING_CURRENT,
        SENSOR_CHAN_GAME_ROTATION_VECTOR,
        SENSOR_CHAN_GRAVITY_VECTOR,
        SENSOR_CHAN_GBIAS_XYZ,

        SENSOR_CHAN_ENCODER_COUNT,

        SENSOR_CHAN_ENCODER_REVOLUTIONS,

        SENSOR_CHAN_ALL,

        SENSOR_CHAN_COMMON_COUNT,

        SENSOR_CHAN_PRIV_START = SENSOR_CHAN_COMMON_COUNT,

        SENSOR_CHAN_MAX = INT16_MAX,
};

#define SENSOR_CHANNEL_3_AXIS(chan)                                                                \
        ((chan) == SENSOR_CHAN_ACCEL_XYZ || (chan) == SENSOR_CHAN_GYRO_XYZ ||                      \
         (chan) == SENSOR_CHAN_MAGN_XYZ || (chan) == SENSOR_CHAN_POS_DXYZ)

#define SENSOR_CHANNEL_IS_ACCEL(chan)                                          \
        ((chan) == SENSOR_CHAN_ACCEL_XYZ || (chan) == SENSOR_CHAN_ACCEL_X ||   \
         (chan) == SENSOR_CHAN_ACCEL_Y || (chan) == SENSOR_CHAN_ACCEL_Z)

#define SENSOR_CHANNEL_IS_GYRO(chan)                                           \
        ((chan) == SENSOR_CHAN_GYRO_XYZ || (chan) == SENSOR_CHAN_GYRO_X ||     \
         (chan) == SENSOR_CHAN_GYRO_Y || (chan) == SENSOR_CHAN_GYRO_Z)

enum sensor_trigger_type {
        SENSOR_TRIG_TIMER,
        SENSOR_TRIG_DATA_READY,
        SENSOR_TRIG_DELTA,
        SENSOR_TRIG_NEAR_FAR,
        SENSOR_TRIG_THRESHOLD,

        SENSOR_TRIG_TAP,

        SENSOR_TRIG_DOUBLE_TAP,

        SENSOR_TRIG_FREEFALL,

        SENSOR_TRIG_MOTION,

        SENSOR_TRIG_STATIONARY,

        SENSOR_TRIG_FIFO_WATERMARK,

        SENSOR_TRIG_FIFO_FULL,

        SENSOR_TRIG_TILT,

        SENSOR_TRIG_OVERFLOW,

        SENSOR_TRIG_COMMON_COUNT,

        SENSOR_TRIG_PRIV_START = SENSOR_TRIG_COMMON_COUNT,

        SENSOR_TRIG_MAX = INT16_MAX,
};

struct sensor_trigger {
        enum sensor_trigger_type type;
        enum sensor_channel chan;
};

enum sensor_attribute {
        SENSOR_ATTR_SAMPLING_FREQUENCY,
        SENSOR_ATTR_LOWER_THRESH,
        SENSOR_ATTR_UPPER_THRESH,
        SENSOR_ATTR_SLOPE_TH,
        SENSOR_ATTR_SLOPE_DUR,
        /* Hysteresis for trigger thresholds. */
        SENSOR_ATTR_HYSTERESIS,
        SENSOR_ATTR_OVERSAMPLING,
        SENSOR_ATTR_FULL_SCALE,
        SENSOR_ATTR_OFFSET,
        SENSOR_ATTR_CALIB_TARGET,
        SENSOR_ATTR_CONFIGURATION,
        SENSOR_ATTR_CALIBRATION,
        SENSOR_ATTR_FEATURE_MASK,
        SENSOR_ATTR_ALERT,
        SENSOR_ATTR_FF_DUR,

        SENSOR_ATTR_BATCH_DURATION,
        SENSOR_ATTR_GAIN,
        SENSOR_ATTR_RESOLUTION,
        SENSOR_ATTR_CHIP_ID,
        SENSOR_ATTR_COMMON_COUNT,

        SENSOR_ATTR_PRIV_START = SENSOR_ATTR_COMMON_COUNT,

        SENSOR_ATTR_MAX = INT16_MAX,
};

typedef void (*sensor_trigger_handler_t)(const struct device *dev,
                                         const struct sensor_trigger *trigger);


typedef int (*sensor_attr_set_t)(const struct device *dev,
                                 enum sensor_channel chan,
                                 enum sensor_attribute attr,
                                 const struct sensor_value *val);

typedef int (*sensor_attr_get_t)(const struct device *dev,
                                 enum sensor_channel chan,
                                 enum sensor_attribute attr,
                                 struct sensor_value *val);

typedef int (*sensor_trigger_set_t)(const struct device *dev,
                                    const struct sensor_trigger *trig,
                                    sensor_trigger_handler_t handler);

typedef int (*sensor_sample_fetch_t)(const struct device *dev,
                                     enum sensor_channel chan);

typedef int (*sensor_channel_get_t)(const struct device *dev,
                                    enum sensor_channel chan,
                                    struct sensor_value *val);

/* Forward declaration */
struct sensor_decoder_api;

typedef int (*sensor_get_decoder_t)(const struct device *dev,
                                    const struct sensor_decoder_api **api);

typedef void (*sensor_submit_t)(const struct device *sensor, struct rtio_iodev_sqe *sqe);

__subsystem struct sensor_driver_api {
        sensor_attr_set_t attr_set;
        sensor_attr_get_t attr_get;
        sensor_trigger_set_t trigger_set;
        sensor_sample_fetch_t sample_fetch;
        sensor_channel_get_t channel_get;
        sensor_get_decoder_t get_decoder;
        sensor_submit_t submit;
};


struct sensor_chan_spec {
        uint16_t chan_type;
        uint16_t chan_idx;
};

/* Ensure sensor_chan_spec is sensibly sized to pass by value */
BUILD_ASSERT(sizeof(struct sensor_chan_spec) <= sizeof(uintptr_t),
             "sensor_chan_spec size should be equal or less than the size of a machine word");

static inline bool sensor_chan_spec_eq(struct sensor_chan_spec chan_spec0,
                                       struct sensor_chan_spec chan_spec1)
{
        return chan_spec0.chan_type == chan_spec1.chan_type &&
                chan_spec0.chan_idx == chan_spec1.chan_idx;
}

struct sensor_decoder_api {
        int (*get_frame_count)(const uint8_t *buffer, struct sensor_chan_spec chan_spec,
                               uint16_t *frame_count);

        int (*get_size_info)(struct sensor_chan_spec channel, size_t *base_size,
                             size_t *frame_size);

        int (*decode)(const uint8_t *buffer, struct sensor_chan_spec chan_spec, uint32_t *fit,
                      uint16_t max_count, void *data_out);

        bool (*has_trigger)(const uint8_t *buffer, enum sensor_trigger_type trigger);
};

struct sensor_decode_context {
        const struct sensor_decoder_api *decoder;
        const uint8_t *buffer;
        struct sensor_chan_spec channel;
        uint32_t fit;
};

#define SENSOR_DECODE_CONTEXT_INIT(decoder_, buffer_, channel_type_, channel_index_)               \
        {                                                                                          \
                .decoder = (decoder_),                                                             \
                .buffer = (buffer_),                                                               \
                .channel = {.chan_type = (channel_type_), .chan_idx = (channel_index_)},           \
                .fit = 0,                                                                          \
        }

static inline int sensor_decode(struct sensor_decode_context *ctx, void *out, uint16_t max_count)
{
        return ctx->decoder->decode(ctx->buffer, ctx->channel, &ctx->fit, max_count, out);
}

int sensor_natively_supported_channel_size_info(struct sensor_chan_spec channel, size_t *base_size,
                                                size_t *frame_size);

enum sensor_stream_data_opt {
        SENSOR_STREAM_DATA_INCLUDE = 0,
        SENSOR_STREAM_DATA_NOP = 1,
        SENSOR_STREAM_DATA_DROP = 2,
};

struct sensor_stream_trigger {
        enum sensor_trigger_type trigger;
        enum sensor_stream_data_opt opt;
};

#define SENSOR_STREAM_TRIGGER_PREP(_trigger, _opt)                                                 \
        {                                                                                          \
                .trigger = (_trigger), .opt = (_opt),                                              \
        }

/*
 * Internal data structure used to store information about the IODevice for async reading and
 * streaming sensor data.
 */
struct sensor_read_config {
        const struct device *sensor;
        const bool is_streaming;
        union {
                struct sensor_chan_spec *const channels;
                struct sensor_stream_trigger *const triggers;
        };
        size_t count;
        const size_t max;
};

#define SENSOR_DT_READ_IODEV(name, dt_node, ...)                                                   \
        static struct sensor_chan_spec _CONCAT(__channel_array_, name)[] = {__VA_ARGS__};          \
        static struct sensor_read_config _CONCAT(__sensor_read_config_, name) = {                  \
                .sensor = DEVICE_DT_GET(dt_node),                                                  \
                .is_streaming = false,                                                             \
                .channels = _CONCAT(__channel_array_, name),                                       \
                .count = ARRAY_SIZE(_CONCAT(__channel_array_, name)),                              \
                .max = ARRAY_SIZE(_CONCAT(__channel_array_, name)),                                \
        };                                                                                         \
        RTIO_IODEV_DEFINE(name, &__sensor_iodev_api, _CONCAT(&__sensor_read_config_, name))

#define SENSOR_DT_STREAM_IODEV(name, dt_node, ...)                                                 \
        static struct sensor_stream_trigger _CONCAT(__trigger_array_, name)[] = {__VA_ARGS__};     \
        static struct sensor_read_config _CONCAT(__sensor_read_config_, name) = {                  \
                .sensor = DEVICE_DT_GET(dt_node),                                                  \
                .is_streaming = true,                                                              \
                .triggers = _CONCAT(__trigger_array_, name),                                       \
                .count = ARRAY_SIZE(_CONCAT(__trigger_array_, name)),                              \
                .max = ARRAY_SIZE(_CONCAT(__trigger_array_, name)),                                \
        };                                                                                         \
        RTIO_IODEV_DEFINE(name, &__sensor_iodev_api, &_CONCAT(__sensor_read_config_, name))

/* The default decoder API */
extern const struct sensor_decoder_api __sensor_default_decoder;

/* The default sensor iodev API */
extern const struct rtio_iodev_api __sensor_iodev_api;

__syscall int sensor_attr_set(const struct device *dev,
                              enum sensor_channel chan,
                              enum sensor_attribute attr,
                              const struct sensor_value *val);

static inline int z_impl_sensor_attr_set(const struct device *dev,
                                         enum sensor_channel chan,
                                         enum sensor_attribute attr,
                                         const struct sensor_value *val)
{
        const struct sensor_driver_api *api = DEVICE_API_GET(sensor, dev);

        if (api->attr_set == NULL) {
                return -ENOSYS;
        }

        return api->attr_set(dev, chan, attr, val);
}

__syscall int sensor_attr_get(const struct device *dev,
                              enum sensor_channel chan,
                              enum sensor_attribute attr,
                              struct sensor_value *val);

static inline int z_impl_sensor_attr_get(const struct device *dev,
                                         enum sensor_channel chan,
                                         enum sensor_attribute attr,
                                         struct sensor_value *val)
{
        const struct sensor_driver_api *api = DEVICE_API_GET(sensor, dev);

        if (api->attr_get == NULL) {
                return -ENOSYS;
        }

        return api->attr_get(dev, chan, attr, val);
}

static inline int sensor_trigger_set(const struct device *dev,
                                     const struct sensor_trigger *trig,
                                     sensor_trigger_handler_t handler)
{
        const struct sensor_driver_api *api = DEVICE_API_GET(sensor, dev);

        if (api->trigger_set == NULL) {
                return -ENOSYS;
        }

        return api->trigger_set(dev, trig, handler);
}

__syscall int sensor_sample_fetch(const struct device *dev);

static inline int z_impl_sensor_sample_fetch(const struct device *dev)
{
        return DEVICE_API_GET(sensor, dev)->sample_fetch(dev, SENSOR_CHAN_ALL);
}

__syscall int sensor_sample_fetch_chan(const struct device *dev,
                                       enum sensor_channel type);

static inline int z_impl_sensor_sample_fetch_chan(const struct device *dev,
                                                  enum sensor_channel type)
{
        return DEVICE_API_GET(sensor, dev)->sample_fetch(dev, type);
}

__syscall int sensor_channel_get(const struct device *dev,
                                 enum sensor_channel chan,
                                 struct sensor_value *val);

static inline int z_impl_sensor_channel_get(const struct device *dev,
                                            enum sensor_channel chan,
                                            struct sensor_value *val)
{
        return DEVICE_API_GET(sensor, dev)->channel_get(dev, chan, val);
}

#if defined(CONFIG_SENSOR_ASYNC_API) || defined(__DOXYGEN__)

/*
 * Generic data structure used for encoding the sample timestamp and number of channels sampled.
 */
struct __attribute__((__packed__)) sensor_data_generic_header {
        uint64_t timestamp_ns;

        /*
         ** The number of channels present in the frame.
         * This will be the true number of elements in channel_info and in the q31 values that
         * follow the header.
         */
        uint32_t num_channels;

        int8_t shift;

        /* This padding is needed to make sure that the 'channels' field is aligned */
        int8_t _padding[sizeof(struct sensor_chan_spec) - 1];

        struct sensor_chan_spec channels[0];
};

__syscall int sensor_get_decoder(const struct device *dev,
                                 const struct sensor_decoder_api **decoder);

static inline int z_impl_sensor_get_decoder(const struct device *dev,
                                            const struct sensor_decoder_api **decoder)
{
        const struct sensor_driver_api *api = DEVICE_API_GET(sensor, dev);

        __ASSERT_NO_MSG(api != NULL);

        if (api->get_decoder == NULL) {
                *decoder = &__sensor_default_decoder;
                return 0;
        }

        return api->get_decoder(dev, decoder);
}

__syscall int sensor_reconfigure_read_iodev(const struct rtio_iodev *iodev,
                                            const struct device *sensor,
                                            const struct sensor_chan_spec *channels,
                                            size_t num_channels);

static inline int z_impl_sensor_reconfigure_read_iodev(const struct rtio_iodev *iodev,
                                                       const struct device *sensor,
                                                       const struct sensor_chan_spec *channels,
                                                       size_t num_channels)
{
        struct sensor_read_config *cfg = (struct sensor_read_config *)iodev->data;

        if (cfg->max < num_channels || cfg->is_streaming) {
                return -ENOMEM;
        }

        cfg->sensor = sensor;
        memcpy(cfg->channels, channels, num_channels * sizeof(struct sensor_chan_spec));
        cfg->count = num_channels;
        return 0;
}

static inline int sensor_stream(const struct rtio_iodev *iodev, struct rtio *ctx, void *userdata,
                                rtio_sqe_handle_t *handle)
{
        if (IS_ENABLED(CONFIG_USERSPACE)) {
                struct rtio_sqe sqe;

                rtio_sqe_prep_read_multishot(&sqe, iodev, RTIO_PRIO_NORM, userdata);
                rtio_sqe_copy_in_get_handles(ctx, &sqe, handle, 1);
        } else {
                struct rtio_sqe *sqe = rtio_sqe_acquire(ctx);

                if (sqe == NULL) {
                        return -ENOMEM;
                }
                if (handle != NULL) {
                        *handle = rtio_sqe_handle(ctx, sqe);
                }
                rtio_sqe_prep_read_multishot(sqe, iodev, RTIO_PRIO_NORM, userdata);
        }
        rtio_submit(ctx, 0);
        return 0;
}

static inline int sensor_read(const struct rtio_iodev *iodev, struct rtio *ctx, uint8_t *buf,
                              size_t buf_len)
{
        if (IS_ENABLED(CONFIG_USERSPACE)) {
                struct rtio_sqe sqe;

                rtio_sqe_prep_read(&sqe, iodev, RTIO_PRIO_NORM, buf, buf_len, buf);
                rtio_sqe_copy_in(ctx, &sqe, 1);
        } else {
                struct rtio_sqe *sqe = rtio_sqe_acquire(ctx);

                if (sqe == NULL) {
                        return -ENOMEM;
                }
                rtio_sqe_prep_read(sqe, iodev, RTIO_PRIO_NORM, buf, buf_len, buf);
        }
        rtio_submit(ctx, 0);

        struct rtio_cqe *cqe = rtio_cqe_consume_block(ctx);
        int res = cqe->result;

        __ASSERT(cqe->userdata == buf,
                 "consumed non-matching completion for sensor read into buffer %p\n", buf);

        rtio_cqe_release(ctx, cqe);

        return res;
}

static inline int sensor_read_async_mempool(const struct rtio_iodev *iodev, struct rtio *ctx,
                                            void *userdata)
{
        if (IS_ENABLED(CONFIG_USERSPACE)) {
                struct rtio_sqe sqe;

                rtio_sqe_prep_read_with_pool(&sqe, iodev, RTIO_PRIO_NORM, userdata);
                rtio_sqe_copy_in(ctx, &sqe, 1);
        } else {
                struct rtio_sqe *sqe = rtio_sqe_acquire(ctx);

                if (sqe == NULL) {
                        return -ENOMEM;
                }
                rtio_sqe_prep_read_with_pool(sqe, iodev, RTIO_PRIO_NORM, userdata);
        }
        rtio_submit(ctx, 0);
        return 0;
}

typedef void (*sensor_processing_callback_t)(int result, uint8_t *buf, uint32_t buf_len,
                                             void *userdata);

void sensor_processing_with_callback(struct rtio *ctx, sensor_processing_callback_t cb);

#endif /* defined(CONFIG_SENSOR_ASYNC_API) || defined(__DOXYGEN__) */

#define SENSOR_G                9806650LL

#define SENSOR_PI               3141592LL

static inline int32_t sensor_ms2_to_g(const struct sensor_value *ms2)
{
        int64_t micro_ms2 = ms2->val1 * 1000000LL + ms2->val2;

        if (micro_ms2 > 0) {
                return (micro_ms2 + SENSOR_G / 2) / SENSOR_G;
        } else {
                return (micro_ms2 - SENSOR_G / 2) / SENSOR_G;
        }
}

static inline void sensor_g_to_ms2(int32_t g, struct sensor_value *ms2)
{
        ms2->val1 = ((int64_t)g * SENSOR_G) / 1000000LL;
        ms2->val2 = ((int64_t)g * SENSOR_G) % 1000000LL;
}

static inline int32_t sensor_ms2_to_mg(const struct sensor_value *ms2)
{
        int64_t nano_ms2 = (ms2->val1 * 1000000LL + ms2->val2) * 1000LL;

        if (nano_ms2 > 0) {
                return (nano_ms2 + SENSOR_G / 2) / SENSOR_G;
        } else {
                return (nano_ms2 - SENSOR_G / 2) / SENSOR_G;
        }
}

static inline int32_t sensor_ms2_to_ug(const struct sensor_value *ms2)
{
        int64_t micro_ms2 = (ms2->val1 * INT64_C(1000000)) + ms2->val2;

        return (micro_ms2 * 1000000LL) / SENSOR_G;
}

static inline void sensor_ug_to_ms2(int32_t ug, struct sensor_value *ms2)
{
        ms2->val1 = ((int64_t)ug * SENSOR_G / 1000000LL) / 1000000LL;
        ms2->val2 = ((int64_t)ug * SENSOR_G / 1000000LL) % 1000000LL;
}

static inline int32_t sensor_rad_to_degrees(const struct sensor_value *rad)
{
        int64_t micro_rad_s = rad->val1 * 1000000LL + rad->val2;

        if (micro_rad_s > 0) {
                return (micro_rad_s * 180LL + SENSOR_PI / 2) / SENSOR_PI;
        } else {
                return (micro_rad_s * 180LL - SENSOR_PI / 2) / SENSOR_PI;
        }
}

static inline void sensor_degrees_to_rad(int32_t d, struct sensor_value *rad)
{
        rad->val1 = ((int64_t)d * SENSOR_PI / 180LL) / 1000000LL;
        rad->val2 = ((int64_t)d * SENSOR_PI / 180LL) % 1000000LL;
}

static inline int32_t sensor_rad_to_10udegrees(const struct sensor_value *rad)
{
        int64_t micro_rad_s = rad->val1 * 1000000LL + rad->val2;

        return (micro_rad_s * 180LL * 100000LL) / SENSOR_PI;
}

static inline void sensor_10udegrees_to_rad(int32_t d, struct sensor_value *rad)
{
        rad->val1 = ((int64_t)d * SENSOR_PI / 180LL / 100000LL) / 1000000LL;
        rad->val2 = ((int64_t)d * SENSOR_PI / 180LL / 100000LL) % 1000000LL;
}

static inline double sensor_value_to_double(const struct sensor_value *val)
{
        return (double)val->val1 + (double)val->val2 / 1000000;
}

static inline float sensor_value_to_float(const struct sensor_value *val)
{
        return (float)val->val1 + (float)val->val2 / 1000000;
}

static inline int sensor_value_to_fixed_point(uint32_t *val, struct sensor_value *inp, uint8_t m,
                                              uint8_t n, bool is_signed)
{
        uint8_t num_bits = m + n + (is_signed ? 1U : 0U);

        if (m > 31 || !IN_RANGE(n, 1, 32) || !IN_RANGE(num_bits, 1, 32)) {
                return -EINVAL;
        }

        int64_t raw = ((int64_t)inp->val1 << n) + ((int64_t)inp->val2 << n) / 1000000LL;

        if (is_signed) {
                if (!IN_RANGE(raw, -(int64_t)BIT(num_bits - 1), (int64_t)BIT_MASK(num_bits - 1))) {
                        return -ERANGE;
                }

                *val = (uint32_t)(raw & BIT64_MASK(num_bits));
        } else {
                if (!IN_RANGE(raw, 0, (int64_t)BIT64_MASK(num_bits))) {
                        return -ERANGE;
                }

                *val = (uint32_t)raw;
        }

        return 0;
}

static inline int sensor_value_from_double(struct sensor_value *val, double inp)
{
        if (inp < (double)INT32_MIN || inp > (double)INT32_MAX) {
                return -ERANGE;
        }

        int32_t val1 = (int32_t)inp;
        int32_t val2 = (int32_t)((inp - (double)val1) * 1000000.0);

        val->val1 = val1;
        val->val2 = val2;

        return 0;
}

static inline int sensor_value_from_float(struct sensor_value *val, float inp)
{
        if (inp < (float)INT32_MIN || inp >= (float)INT32_MAX) {
                return -ERANGE;
        }

        int32_t val1 = (int32_t)inp;
        int32_t val2 = (int32_t)((inp - (float)val1) * 1000000.0f);

        val->val1 = val1;
        val->val2 = val2;

        return 0;
}

static inline int sensor_value_from_fixed_point(struct sensor_value *val, uint32_t inp, uint8_t m,
                                                uint8_t n, bool is_signed)
{
        uint8_t num_bits = m + n + (is_signed ? 1U : 0U);

        if (m > 31 || !IN_RANGE(n, 1, 32) || !IN_RANGE(num_bits, 1, 32)) {
                return -EINVAL;
        }

        inp &= BIT64_MASK(num_bits);

        int64_t inp_int64 = is_signed ? sign_extend_64((uint64_t)inp, m + n) : (int64_t)inp;

        val->val1 = arithmetic_shift_right(inp_int64 + (inp_int64 < 0 ? BIT64_MASK(n) : 0), n);

        inp_int64 -= ((int64_t)val->val1 << n);
        inp_int64 *= 1000000LL;

        val->val2 = arithmetic_shift_right(inp_int64 + (inp_int64 < 0 ? BIT64_MASK(n) : 0), n);

        return 0;
}

#ifdef CONFIG_SENSOR_INFO

struct sensor_info {
        const struct device *dev;
        const char *vendor;
        const char *model;
        const char *friendly_name;
};

#define SENSOR_INFO_INITIALIZER(_dev, _vendor, _model, _friendly_name)  \
        {                                                               \
                .dev = _dev,                                            \
                .vendor = _vendor,                                      \
                .model = _model,                                        \
                .friendly_name = _friendly_name,                        \
        }

#define SENSOR_INFO_DEFINE(name, ...)                                   \
        static const STRUCT_SECTION_ITERABLE(sensor_info, name) =       \
                SENSOR_INFO_INITIALIZER(__VA_ARGS__)

#define SENSOR_INFO_DT_NAME(node_id)                                    \
        _CONCAT(__sensor_info, DEVICE_DT_NAME_GET(node_id))

#define SENSOR_INFO_DT_DEFINE(node_id)                                  \
        SENSOR_INFO_DEFINE(SENSOR_INFO_DT_NAME(node_id),                \
                           DEVICE_DT_GET(node_id),                      \
                           DT_NODE_VENDOR_OR(node_id, NULL),            \
                           DT_NODE_MODEL_OR(node_id, NULL),             \
                           DT_PROP_OR(node_id, friendly_name, NULL))    \

#else

#define SENSOR_INFO_DEFINE(name, ...)
#define SENSOR_INFO_DT_DEFINE(node_id)

#endif /* CONFIG_SENSOR_INFO */

#define SENSOR_DEVICE_DT_DEFINE(node_id, init_fn, pm_device,            \
                                data_ptr, cfg_ptr, level, prio,         \
                                api_ptr, ...)                           \
        DEVICE_DT_DEFINE(node_id, init_fn, pm_device,                   \
                         data_ptr, cfg_ptr, level, prio,                \
                         api_ptr, __VA_ARGS__);                         \
                                                                        \
        SENSOR_INFO_DT_DEFINE(node_id);

#define SENSOR_DEVICE_DT_INST_DEFINE(inst, ...)                         \
        SENSOR_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)

static inline int64_t sensor_value_to_deci(const struct sensor_value *val)
{
        return ((int64_t)val->val1 * 10) + val->val2 / 100000;
}

static inline int64_t sensor_value_to_centi(const struct sensor_value *val)
{
        return ((int64_t)val->val1 * 100) + val->val2 / 10000;
}

static inline int64_t sensor_value_to_milli(const struct sensor_value *val)
{
        return ((int64_t)val->val1 * 1000) + val->val2 / 1000;
}

static inline int64_t sensor_value_to_micro(const struct sensor_value *val)
{
        return ((int64_t)val->val1 * 1000000) + val->val2;
}

static inline int sensor_value_from_milli(struct sensor_value *val, int64_t milli)
{
        if (milli < ((int64_t)INT32_MIN - 1) * 1000LL ||
                        milli > ((int64_t)INT32_MAX + 1) * 1000LL) {
                return -ERANGE;
        }

        val->val1 = (int32_t)(milli / 1000);
        val->val2 = (int32_t)(milli % 1000) * 1000;

        return 0;
}

static inline int sensor_value_from_micro(struct sensor_value *val, int64_t micro)
{
        if (micro < ((int64_t)INT32_MIN - 1) * 1000000LL ||
                        micro > ((int64_t)INT32_MAX + 1) * 1000000LL) {
                return -ERANGE;
        }

        val->val1 = (int32_t)(micro / 1000000LL);
        val->val2 = (int32_t)(micro % 1000000LL);

        return 0;
}

static inline int sensor_value_add(struct sensor_value *inp1, struct sensor_value *inp2,
                                   struct sensor_value *out)
{
        int64_t val1 = (int64_t)inp1->val1 + (int64_t)inp2->val1;
        int32_t val2 = inp1->val2 + inp2->val2;

        if (val2 >= 1000000LL || (val1 < 0 && val2 > 0)) {
                val1 += 1;
                val2 -= 1000000LL;
        } else if (val2 <= -1000000LL || (val1 > 0 && val2 < 0)) {
                val1 -= 1;
                val2 += 1000000LL;
        }

        if (!IN_RANGE(val1, INT32_MIN, INT32_MAX)) {
                return -ERANGE;
        }

        out->val1 = val1;
        out->val2 = val2;

        return 0;
}

static inline int sensor_value_subtract(struct sensor_value *inp1, struct sensor_value *inp2,
                                        struct sensor_value *out)
{
        int64_t val1 = (int64_t)inp1->val1 - (int64_t)inp2->val1;
        int32_t val2 = inp1->val2 - inp2->val2;

        if (val2 >= 1000000LL || (val1 < 0 && val2 > 0)) {
                val1 += 1;
                val2 -= 1000000LL;
        } else if (val2 <= -1000000LL || (val1 > 0 && val2 < 0)) {
                val1 -= 1;
                val2 += 1000000LL;
        }

        if (!IN_RANGE(val1, INT32_MIN, INT32_MAX)) {
                return -ERANGE;
        }

        out->val1 = val1;
        out->val2 = val2;

        return 0;
}

static inline int sensor_value_multiply(struct sensor_value *inp1, struct sensor_value *inp2,
                                        struct sensor_value *out)
{
        int64_t val1 = (int64_t)inp1->val1 * inp2->val1;
        int64_t val2 = (int64_t)inp1->val1 * inp2->val2 + (int64_t)inp1->val2 * inp2->val1 +
                       ((int64_t)inp1->val2 * inp2->val2) / 1000000LL;

        val1 += val2 / 1000000LL;
        val2 %= 1000000LL;

        if (!IN_RANGE(val1, INT32_MIN, INT32_MAX)) {
                return -ERANGE;
        }

        out->val1 = val1;
        out->val2 = val2;

        return 0;
}

static inline int sensor_value_scale(struct sensor_value *inp, int32_t scalar,
                                     struct sensor_value *out)
{
        int64_t val1 = (int64_t)inp->val1 * scalar;
        int64_t val2 = (int64_t)inp->val2 * scalar;

        val1 += val2 / 1000000LL;
        val2 %= 1000000LL;

        if (!IN_RANGE(val1, INT32_MIN, INT32_MAX)) {
                return -ERANGE;
        }

        out->val1 = val1;
        out->val2 = val2;

        return 0;
}


#define SENSOR_DECODER_NAME() UTIL_CAT(DT_DRV_COMPAT, __decoder_api)

#define SENSOR_DECODER_DT_GET(node_id)                                                             \
        &UTIL_CAT(DT_STRING_TOKEN_BY_IDX(node_id, compatible, 0), __decoder_api)

#define SENSOR_DECODER_API_DT_DEFINE()                                                             \
        COND_CODE_1(DT_HAS_COMPAT_STATUS_OKAY(DT_DRV_COMPAT), (), (static))                        \
        const STRUCT_SECTION_ITERABLE(sensor_decoder_api, SENSOR_DECODER_NAME())

#define Z_MAYBE_SENSOR_DECODER_DECLARE_INTERNAL_IDX(node_id, prop, idx)                            \
        extern const struct sensor_decoder_api UTIL_CAT(                                           \
                DT_STRING_TOKEN_BY_IDX(node_id, prop, idx), __decoder_api);

#define Z_MAYBE_SENSOR_DECODER_DECLARE_INTERNAL(node_id)                                           \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, compatible),                                         \
                    (DT_FOREACH_PROP_ELEM(node_id, compatible,                                     \
                                          Z_MAYBE_SENSOR_DECODER_DECLARE_INTERNAL_IDX)),           \
                    ())

DT_FOREACH_STATUS_OKAY_NODE(Z_MAYBE_SENSOR_DECODER_DECLARE_INTERNAL)

#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/sensor.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_H_ */
```

## 24.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 401 行

触发阈值的迟滞（hysteresis）。

### 注释 3：原第 512 行

前向声明（Forward declaration）。

### 注释 4：原第 583 行

确保 `sensor_chan_spec` 的大小适合按值传递（pass by value）。

### 注释 5：原第 755 行

内部数据结构，用于保存异步读取（async reading）及流式传输（streaming）传感器数据所用 I/O 设备（IODevice）的信息。

### 注释 6：原第 826 行

默认解码器 API（decoder API）。

### 注释 7：原第 829 行

默认传感器 I/O 设备 API（sensor iodev API）。

### 注释 8：原第 1018 行

通用数据结构，用于编码样本时间戳（sample timestamp）及已采样通道数。

### 注释 9：原第 1025 行

帧（frame）中包含的通道数量。这是 `channel_info` 中的实际元素数量，也是首部后面跟随的 Q31 值的实际数量。

### 注释 10：原第 1035 行

需要此填充（padding），以确保 `channels` 字段对齐（aligned）。

### 注释 11：原第 1233 行

条件表达式：`defined(CONFIG_SENSOR_ASYNC_API) || defined(__DOXYGEN__)`。

### 注释 12：原第 1555 行

条件编译配置（Configuration）标记：`CONFIG_SENSOR_INFO`。

### 注释 13：原第 1866 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_H_`。

## 24.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdlib.h](../api_file_reference/P410_____w__zephyr__zephyr__lib__libc__minimal__include__stdlib.h_文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/sensor_data_types.h](../api_file_reference/P384_zephyr__drivers__sensor_data_types.h_文件参考.md)
- [zephyr/dsp/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [val2](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#a91f81bd0f5da69084cf3c629fde68a1b)
- [sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)
- [SENSOR_CHAN_ACCEL_X](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c)
- [SENSOR_CHAN_ACCEL_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8)
- [SENSOR_CHAN_ACCEL_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f)
- [SENSOR_CHAN_ACCEL_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9)
- [SENSOR_CHAN_GYRO_X](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015)
- [SENSOR_CHAN_GYRO_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847)
- [SENSOR_CHAN_GYRO_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39)
- [SENSOR_CHAN_GYRO_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e)
- [SENSOR_CHAN_MAGN_X](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240)
- [SENSOR_CHAN_MAGN_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942)
- [SENSOR_CHAN_MAGN_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61)
- [SENSOR_CHAN_MAGN_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32)
- [SENSOR_CHAN_DIE_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1)
- [SENSOR_CHAN_AMBIENT_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c)
- [SENSOR_CHAN_PRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9)
- [SENSOR_CHAN_PROX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774)
- [SENSOR_CHAN_HUMIDITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042)
- [SENSOR_CHAN_AMBIENT_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a39b13669a3006ead32275d1578677127)
- [SENSOR_CHAN_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d)
- [SENSOR_CHAN_IR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c)
- [SENSOR_CHAN_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa)
- [SENSOR_CHAN_GREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378)
- [SENSOR_CHAN_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5)
- [SENSOR_CHAN_ALTITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512)
- [SENSOR_CHAN_PM_1_0_CF](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a0893cbc829c2a3b896f12874cc96c872)
- [SENSOR_CHAN_PM_2_5_CF](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4d8c9e992c590bb17291471d8634a3a2)
- [SENSOR_CHAN_PM_10_CF](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a9e45f64b48f96650f0e75c3728324379)
- [SENSOR_CHAN_PM_1_0](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815)
- [SENSOR_CHAN_PM_2_5](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945)
- [SENSOR_CHAN_PM_10](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225)
- [SENSOR_CHAN_PM_0_3_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aadd0d7e0e77db8bd11da1866786b3a6a)
- [SENSOR_CHAN_PM_0_5_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a3afc97258f1340ef047a055dc5a69e4c)
- [SENSOR_CHAN_PM_1_0_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aabd79bd1d8600c852260c0a8afc372e6)
- [SENSOR_CHAN_PM_2_5_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934adcef73d7ea6cac2e251f96ecf9fa8ea4)
- [SENSOR_CHAN_PM_5_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a7746b596d101dde6afbf73f5994b5ec2)
- [SENSOR_CHAN_PM_10_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aaee5947abb6490ec06d9f5984bfa4060)
- [SENSOR_CHAN_DISTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08)
- [SENSOR_CHAN_CO2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133)
- [SENSOR_CHAN_O2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a17bcfa0e34eecf45e17988720471c8f9)
- [SENSOR_CHAN_VOC](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e)
- [SENSOR_CHAN_GAS_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01)
- [SENSOR_CHAN_FLOW_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6d19454f164337c9cf163dc1dfaf2b42)
- [SENSOR_CHAN_VOLUME](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6dfcb28f053feeb7fca51a6c92b6c4ab)
- [SENSOR_CHAN_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d)
- [SENSOR_CHAN_VSHUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9)
- [SENSOR_CHAN_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950)
- [SENSOR_CHAN_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177)
- [SENSOR_CHAN_RESISTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b)
- [SENSOR_CHAN_ROTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf)
- [SENSOR_CHAN_POS_DX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517)
- [SENSOR_CHAN_POS_DY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76)
- [SENSOR_CHAN_POS_DZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9)
- [SENSOR_CHAN_POS_DXYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740)
- [SENSOR_CHAN_RPM](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1)
- [SENSOR_CHAN_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4b5a3a92ce610a2b3c9f113c93aef212)
- [SENSOR_CHAN_GAUGE_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d)
- [SENSOR_CHAN_GAUGE_AVG_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8)
- [SENSOR_CHAN_GAUGE_STDBY_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8)
- [SENSOR_CHAN_GAUGE_MAX_LOAD_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf)
- [SENSOR_CHAN_GAUGE_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214)
- [SENSOR_CHAN_GAUGE_STATE_OF_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139)
- [SENSOR_CHAN_GAUGE_FULL_CHARGE_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649)
- [SENSOR_CHAN_GAUGE_REMAINING_CHARGE_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad)
- [SENSOR_CHAN_GAUGE_NOM_AVAIL_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a)
- [SENSOR_CHAN_GAUGE_FULL_AVAIL_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8)
- [SENSOR_CHAN_GAUGE_AVG_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228)
- [SENSOR_CHAN_GAUGE_STATE_OF_HEALTH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6)
- [SENSOR_CHAN_GAUGE_TIME_TO_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65)
- [SENSOR_CHAN_GAUGE_TIME_TO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb)
- [SENSOR_CHAN_GAUGE_CYCLE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46)
- [SENSOR_CHAN_GAUGE_DESIGN_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0)
- [SENSOR_CHAN_GAUGE_DESIRED_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf)
- [SENSOR_CHAN_GAUGE_DESIRED_CHARGING_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f)
- [SENSOR_CHAN_GAME_ROTATION_VECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a3905467a96940ada0dbdef6ff8ee1a8a)
- [SENSOR_CHAN_GRAVITY_VECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a26fe67f0313062c6bf841ff8b829f7ff)
- [SENSOR_CHAN_GBIAS_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a88001b6464b2419dbf2aa4ad59556110)
- [SENSOR_CHAN_ENCODER_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a486ea8968daed9d1c3802a3babcdcfad)
- [SENSOR_CHAN_ENCODER_REVOLUTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa659bdadf3905703afe9bcf6dd0be82e)
- [SENSOR_CHAN_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c)
- [SENSOR_CHAN_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [SENSOR_CHAN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1)
- [INT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac58f2c111cc9989c86db2a7dc4fd84ca)
- [sensor_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga08215279400e8c9eb05ce4e4f0898ffd)
- [SENSOR_TRIG_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023)
- [SENSOR_TRIG_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f)
- [SENSOR_TRIG_DELTA](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855)
- [SENSOR_TRIG_NEAR_FAR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5)
- [SENSOR_TRIG_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606)
- [SENSOR_TRIG_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d)
- [SENSOR_TRIG_DOUBLE_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef)
- [SENSOR_TRIG_FREEFALL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c)
- [SENSOR_TRIG_MOTION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276)
- [SENSOR_TRIG_STATIONARY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d)
- [SENSOR_TRIG_FIFO_WATERMARK](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4)
- [SENSOR_TRIG_FIFO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c)
- [SENSOR_TRIG_TILT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdabbdff0ba5072a376190c4a1272b2c4cf)
- [SENSOR_TRIG_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda2bc31b6e790488eb7c9031107676b409)
- [SENSOR_TRIG_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5)
- [SENSOR_TRIG_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)
- [SENSOR_TRIG_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4)
- [sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)
- [type](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md#ac2cce1ec6ff82f95cb06d0dccafd7af0)
- [chan](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md#ae01f99b124aa99c59b9967818022e112)
- [sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)
- [SENSOR_ATTR_SAMPLING_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291)
- [SENSOR_ATTR_LOWER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa)
- [SENSOR_ATTR_UPPER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b)
- [SENSOR_ATTR_SLOPE_TH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302)
- [SENSOR_ATTR_SLOPE_DUR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1)
- [SENSOR_ATTR_HYSTERESIS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94)
- [SENSOR_ATTR_OVERSAMPLING](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd)
- [SENSOR_ATTR_FULL_SCALE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3)
- [SENSOR_ATTR_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd)
- [SENSOR_ATTR_CALIB_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf)
- [SENSOR_ATTR_CONFIGURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9)
- [SENSOR_ATTR_CALIBRATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e)
- [SENSOR_ATTR_FEATURE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52)
- [SENSOR_ATTR_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a)
- [SENSOR_ATTR_FF_DUR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a)
- [SENSOR_ATTR_BATCH_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced)
- [SENSOR_ATTR_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bac778fe666c284078117b2083779ba7a3)
- [SENSOR_ATTR_RESOLUTION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba7f20835b052b1bd6374e56f66e0f285d)
- [SENSOR_ATTR_CHIP_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba87d853ad38f41c897bda106a7c66c08c)
- [SENSOR_ATTR_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [SENSOR_ATTR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b)
- [sensor_trigger_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga890c1fb6d6974aea22a2d08829a75902)
- [device](../device_reference/P002_设备对象结构.md)
- [sensor_attr_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga38422ace4194a66a9a912a8ef1e088fb)
- [sensor_attr_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga00d05c82b46e56dca5f6e8f7f01c31b8)
- [sensor_trigger_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#gad7f7a3d9e714cc16f23656ca06592aa4)
- [sensor_sample_fetch_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#gacae110a4edb6f29dfb457cb1ea8d68c1)
- [sensor_channel_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga5c9b5ed9097464562004b446856043fd)
- [sensor_decoder_api](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md)
- [sensor_get_decoder_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga21e407d552d140cfb6bfd0d9513c7d42)
- [sensor_submit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#gad77732c8f0ec5520cdd71c2829787981)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [sqe](../rtio_model_reference/P005_RTIO设备提交条目.md#a2bd98599678909c0ddb22f879affa12b)
- [sensor_driver_api](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md)
- [attr_set](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a2d230a976b19a699d132034f58bb2b6a)
- [attr_get](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a3e28950f844c3f8b8da5ba9ff8052e46)
- [trigger_set](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a4708070fd6654ecbbe631819aba319bd)
- [sample_fetch](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a4b40e25b81fe070e2f6bdcf7f8a4a31f)
- [channel_get](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a667b41bf51f2c7a6bb31713fbf889113)
- [get_decoder](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a004f9d342805dc72249ab9b8c17a544b)
- [submit](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#ae3ba0adeba21351e8f660896e5a0e702)
- [sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [chan_type](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c)
- [chan_idx](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md#a00d4a927cfeae33b2beea8cdc415dda1)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [sensor_chan_spec_eq](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gae95715ffea5da18a9593ec2add029824)
- [get_frame_count](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md#a0693dd5369a21c12ce4539ad2dd8940e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [get_size_info](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md#a026be8086386e9eea0a1cb25c1cd602e)
- [decode](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md#a2d219ff0ea1ce71976a5e81814e3a3ff)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [has_trigger](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md#a78706bae0f1314615b5804736ef43493)
- [sensor_decode_context](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md)
- [decoder](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md#a1ac0773e83a086455371d108264ef4f6)
- [buffer](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md#a23e27eb0687d722be78e1b89278613d1)
- [channel](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md#a1c051bd8d0030f81cc561e32b2897d74)
- [fit](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md#ada9e40625829093087886c41f2fb7350)
- [sensor_decode](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga018bca56056ae2558f9e45aeb2fa5f53)
- [sensor_natively_supported_channel_size_info](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga2b045cdbd4d1ca37beed69970093945b)
- [sensor_stream_data_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga8613a20521a37d40fd7371dc63ba2dac)
- [SENSOR_STREAM_DATA_INCLUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315)
- [SENSOR_STREAM_DATA_NOP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d)
- [SENSOR_STREAM_DATA_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e)
- [sensor_stream_trigger](../sensor_navigation_model_reference/P048_sensor_stream_trigger_结构体.md)
- [trigger](../sensor_navigation_model_reference/P048_sensor_stream_trigger_结构体.md#a9a367e746764e68140ec9120f2a016e6)
- [opt](../sensor_navigation_model_reference/P048_sensor_stream_trigger_结构体.md#a62ccdecf7253b1bfdff4f1d659563d76)
- [sensor_read_config](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md)
- [sensor](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#ad49d5ab5293017d1ad2cf60adc542090)
- [is_streaming](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#aca96de2c23fb63f887c4c40dcb272798)
- [channels](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#a2aff44f02b25fd4ad1d4bc217800fad1)
- [triggers](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#a6eaa6df7bc9378abe0f5b4b8c9a05909)
- [count](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#a5236049e0563ebba754994d70e22383a)
- [max](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#aecb9c899e292fdb25c3c990bdaf1c76b)
- [rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)
- [sensor_attr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gafbf65226a227e9f8824908bc38e336f5)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [sensor_attr_get](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaedfdfc71dce702dc1fb1c6e60ff0f73a)
- [sensor_trigger_set](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga7c72aca732e0641612d2f9437c2e41b7)
- [sensor_sample_fetch](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa75e25d93ee7cac0bf38399f3c006dff)
- [sensor_sample_fetch_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gac16192826432438a15274cf28d66e8a6)
- [sensor_channel_get](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9e0e6c1408d32c52267984bae7cb268d)
- [sensor_data_generic_header](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [timestamp_ns](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md#a429e22b3191df271ccfe321b796e1ac9)
- [num_channels](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md#a7edbe674f28c95f3aa40b1df84ca61fe)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [shift](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md#a68067521c1058b6802176e1d48fed788)
- [channels](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md#ac09f23959c66ff75b0854a95e8d4504b)
- [sensor_get_decoder](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga12db6fc43adce48d34c25c16fd2336a3)
- [sensor_reconfigure_read_iodev](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga759d6581b83751bab5e56b9f8bb1676d)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [data](../rtio_model_reference/P003_RTIO输入输出设备.md#af0f3a27fe8dea2161c9a73cb838bdeec)
- [ENOMEM](../error_reference/P003_系统错误号公共接口.md#ga6a05c923dad0c1208043e9c20a58c8e5)
- [memcpy](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md#af0f01bffcd16daa9143f6014d10a25ad)
- [sensor_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga58bb95758fc4bd2927c93671727e6080)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_sqe_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga7ff7d0337e43b0a9380bb94a4a143a47)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)
- [rtio_sqe_prep_read_multishot](../rtio_core_reference/P001_RTIO公共接口.md#ga9803aa829f8c0eeee746ea7d872c20cc)
- [iodev](../rtio_model_reference/P007_RTIO提交事件.md#a6c784702f011592c84feacd57915bbfc)
- [RTIO_PRIO_NORM](../rtio_model_reference/P011_RTIO优先级.md#gab02e27e01b7dd4eb3439df557899ce92)
- [userdata](../rtio_model_reference/P007_RTIO提交事件.md#a0ed519ee0b5867ff73bdaf37f983c971)
- [rtio_sqe_copy_in_get_handles](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga77506a320d6e31c6aeb2951312890295)
- [rtio_sqe_acquire](../rtio_core_reference/P001_RTIO公共接口.md#ga8b47c954d15a334621def53acceb6799)
- [rtio_sqe_handle](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga4ac49ea0ef01717caadfcd8b781dcc7b)
- [rtio_submit](../rtio_core_reference/P001_RTIO公共接口.md#gafee27c64a4a4989c4eb774addde8eb2e)
- [sensor_read](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gace7f20e29b302e607ba274fe40a2c2bd)
- [buf](../rtio_model_reference/P007_RTIO提交事件.md#ab71176c084e8b8eb65dfeb3018ae2a49)
- [buf_len](../rtio_model_reference/P007_RTIO提交事件.md#a67376f40a13960b152a23da250275722)
- [rtio_sqe_prep_read](../rtio_core_reference/P001_RTIO公共接口.md#ga89c7cc2494e3dda50737f78f1a1376cf)
- [rtio_sqe_copy_in](../rtio_core_reference/P001_RTIO公共接口.md#ga65e351af0a16dcf504a51ef4eb9316c7)
- [rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)
- [rtio_cqe_consume_block](../rtio_core_reference/P001_RTIO公共接口.md#gaf617d05d9b59ce1f1d0697617ef6f249)
- [result](../rtio_model_reference/P002_RTIO完成事件.md#acbe2e6607a752b676d9336b9ca6ce435)
- [userdata](../rtio_model_reference/P002_RTIO完成事件.md#a15128387ccbea55812ef229eab7241e7)
- [rtio_cqe_release](../rtio_core_reference/P001_RTIO公共接口.md#gaa0799a5f8ad98425d385a07c5d27d9cb)
- [sensor_read_async_mempool](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaf53b015c47acab3c3acb4cb1d8ab827d)
- [rtio_sqe_prep_read_with_pool](../rtio_core_reference/P001_RTIO公共接口.md#ga15c1f623658d27d300d1a31a6f3d6b9d)
- [sensor_processing_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa8cd6e4fadb5d69e59d101733b4fb462)
- [sensor_processing_with_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabb076531445e1b128d515b28c7cc9dc8)
- [sensor_ms2_to_g](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gab797f2f578b1c9cc44f54ab5d503bbf8)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [SENSOR_G](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0066e049c4f084305ca2b978e5c7454d)
- [sensor_g_to_ms2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)
- [sensor_ms2_to_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9e0fb14f84dca02497ce5bff10b51ab8)
- [sensor_ms2_to_ug](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga3db980100e634310a0a1623136048742)
- [sensor_ug_to_ms2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga28a1c6cf74a391712a4697792f759d62)
- [sensor_rad_to_degrees](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga040a907c8934baab66d27b8dfb1ea220)
- [SENSOR_PI](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga6ebdc2f6942334de3cc248a53db7df33)
- [sensor_degrees_to_rad](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)
- [sensor_rad_to_10udegrees](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gad80093a6cfe95428dd0ead85547838a6)
- [sensor_10udegrees_to_rad](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gab53418e1eb164364663d3ec3f40399a4)
- [sensor_value_to_double](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga29223b754dc436ab1e97ce6209a3ea06)
- [sensor_value_to_float](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)
- [sensor_value_to_fixed_point](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gab4c95b7857294a9148afe6e9bcb5eacf)
- [IN_RANGE](../util_reference/P001_通用工具公共接口.md#gaea00fb0c11b73f77da8884374e2121b4)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)
- [ERANGE](../error_reference/P003_系统错误号公共接口.md#gaa1591a4f3a86360108de5b9ba34980ca)
- [BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)
- [sensor_value_from_double](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaf01bbb251ad0c7f6c55c5b702e8a4048)
- [INT32_MIN](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a688eb21a22db27c2b2bd5836943cdcbe)
- [INT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a181807730d4a375f848ba139813ce04f)
- [sensor_value_from_float](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga64d5a1725eda200c80daf42b1067c46c)
- [sensor_value_from_fixed_point](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga767c7d0147699c556a2f4d429501ff99)
- [sign_extend_64](../util_reference/P001_通用工具公共接口.md#ga0ba9d4ab383eba522e345594aaa2bb3f)
- [arithmetic_shift_right](../util_reference/P001_通用工具公共接口.md#ga1ffeb18b8ed73d37c2485c82988ed1ec)
- [sensor_value_to_deci](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabbcb8ad4b9484cba77ae65e2d3ba7457)
- [sensor_value_to_centi](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gae812fb481bfe3a8053f0fc23f8617434)
- [sensor_value_to_milli](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga6d69a9644e08a9cd7773645fa11293e3)
- [sensor_value_to_micro](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9bf7faf60aa54a7540e9b73a61864e25)
- [sensor_value_from_milli](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga88b2605526e37420db871f066c5053b3)
- [sensor_value_from_micro](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabff019c63c89cbc546c0981819040c99)
- [sensor_value_add](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabf3b46a1e88e65575e25acc1a43aba10)
- [sensor_value_subtract](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gac17a55d53ccd2a2e8b45109e984cc80b)
- [sensor_value_multiply](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gacdb8dc2095e6a15db0a58233cab8ffe2)
- [sensor_value_scale](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga8d6f33eeda04bdb648bd03a92e981b1d)
- [DT_FOREACH_STATUS_OKAY_NODE](../dt_foreach_reference/P001_设备树遍历宏.md#ga926f68202042c9db05390e628787f916)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)
- [sensor_data_types.h](../api_file_reference/P384_zephyr__drivers__sensor_data_types.h_文件参考.md)
- [rtio_cqe::userdata](../rtio_model_reference/P002_RTIO完成事件.md#a15128387ccbea55812ef229eab7241e7)
- [rtio_cqe::result](../rtio_model_reference/P002_RTIO完成事件.md#acbe2e6607a752b676d9336b9ca6ce435)
- [rtio_iodev_sqe::sqe](../rtio_model_reference/P005_RTIO设备提交条目.md#a2bd98599678909c0ddb22f879affa12b)
- [rtio_iodev::data](../rtio_model_reference/P003_RTIO输入输出设备.md#af0f3a27fe8dea2161c9a73cb838bdeec)
- [rtio_sqe::userdata](../rtio_model_reference/P007_RTIO提交事件.md#a0ed519ee0b5867ff73bdaf37f983c971)
- [rtio_sqe::buf_len](../rtio_model_reference/P007_RTIO提交事件.md#a67376f40a13960b152a23da250275722)
- [rtio_sqe::iodev](../rtio_model_reference/P007_RTIO提交事件.md#a6c784702f011592c84feacd57915bbfc)
- [rtio_sqe::buf](../rtio_model_reference/P007_RTIO提交事件.md#ab71176c084e8b8eb65dfeb3018ae2a49)
- [sensor_chan_spec::chan_idx](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md#a00d4a927cfeae33b2beea8cdc415dda1)
- [sensor_chan_spec::chan_type](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c)
- [sensor_data_generic_header::timestamp_ns](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md#a429e22b3191df271ccfe321b796e1ac9)
- [sensor_data_generic_header::shift](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md#a68067521c1058b6802176e1d48fed788)
- [sensor_data_generic_header::num_channels](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md#a7edbe674f28c95f3aa40b1df84ca61fe)
- [sensor_data_generic_header::channels](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md#ac09f23959c66ff75b0854a95e8d4504b)
- [sensor_decode_context::decoder](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md#a1ac0773e83a086455371d108264ef4f6)
- [sensor_decode_context::channel](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md#a1c051bd8d0030f81cc561e32b2897d74)
- [sensor_decode_context::buffer](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md#a23e27eb0687d722be78e1b89278613d1)
- [sensor_decode_context::fit](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md#ada9e40625829093087886c41f2fb7350)
- [sensor_decoder_api::get_size_info](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md#a026be8086386e9eea0a1cb25c1cd602e)
- [sensor_decoder_api::get_frame_count](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md#a0693dd5369a21c12ce4539ad2dd8940e)
- [sensor_decoder_api::decode](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md#a2d219ff0ea1ce71976a5e81814e3a3ff)
- [sensor_decoder_api::has_trigger](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md#a78706bae0f1314615b5804736ef43493)
- [sensor_driver_api::get_decoder](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a004f9d342805dc72249ab9b8c17a544b)
- [sensor_driver_api::attr_set](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a2d230a976b19a699d132034f58bb2b6a)
- [sensor_driver_api::attr_get](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a3e28950f844c3f8b8da5ba9ff8052e46)
- [sensor_driver_api::trigger_set](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a4708070fd6654ecbbe631819aba319bd)
- [sensor_driver_api::sample_fetch](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a4b40e25b81fe070e2f6bdcf7f8a4a31f)
- [sensor_driver_api::channel_get](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#a667b41bf51f2c7a6bb31713fbf889113)
- [sensor_driver_api::submit](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md#ae3ba0adeba21351e8f660896e5a0e702)
- [sensor_read_config::channels](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#a2aff44f02b25fd4ad1d4bc217800fad1)
- [sensor_read_config::count](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#a5236049e0563ebba754994d70e22383a)
- [sensor_read_config::triggers](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#a6eaa6df7bc9378abe0f5b4b8c9a05909)
- [sensor_read_config::is_streaming](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#aca96de2c23fb63f887c4c40dcb272798)
- [sensor_read_config::sensor](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#ad49d5ab5293017d1ad2cf60adc542090)
- [sensor_read_config::max](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md#aecb9c899e292fdb25c3c990bdaf1c76b)
- [sensor_stream_trigger::opt](../sensor_navigation_model_reference/P048_sensor_stream_trigger_结构体.md#a62ccdecf7253b1bfdff4f1d659563d76)
- [sensor_stream_trigger::trigger](../sensor_navigation_model_reference/P048_sensor_stream_trigger_结构体.md#a9a367e746764e68140ec9120f2a016e6)
- [sensor_trigger::type](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md#ac2cce1ec6ff82f95cb06d0dccafd7af0)
- [sensor_trigger::chan](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md#ae01f99b124aa99c59b9967818022e112)
- [sensor_value::val2](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#a91f81bd0f5da69084cf3c629fde68a1b)
- [sensor_value::val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P023_riscv_imsic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P025_symbol.h_源码浏览.md)
