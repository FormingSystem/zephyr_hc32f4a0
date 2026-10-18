---
id: learning.zephyr-docs.api-source-socket-ethernet-reference.page-3
title: ethernet.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_ethernet.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)。

## 3.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
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
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
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
<a id="l00145"></a>
<a id="foldopen00147"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
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
<a id="l00244"></a>
<a id="foldopen00246"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
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
<a id="l00286"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
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
<a id="l00353"></a>
<a id="foldopen00355"></a>
<a id="l00355"></a>
<a id="l00357"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00393"></a>
<a id="foldopen00395"></a>
<a id="l00395"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="foldopen00428"></a>
<a id="l00428"></a>
<a id="l00430"></a>
<a id="l00432"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
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
<a id="l00457"></a>
<a id="foldopen00464"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00486"></a>
<a id="foldopen00488"></a>
<a id="l00488"></a>
<a id="l00490"></a>
<a id="l00492"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="foldopen00498"></a>
<a id="l00498"></a>
<a id="l00500"></a>
<a id="l00502"></a>
<a id="l00504"></a>
<a id="l00506"></a>
<a id="l00508"></a>
<a id="l00510"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
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
<a id="l00541"></a>
<a id="foldopen00543"></a>
<a id="l00543"></a>
<a id="l00545"></a>
<a id="l00547"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="foldopen00553"></a>
<a id="l00553"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
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
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00648"></a>
<a id="foldopen00650"></a>
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
<a id="l00669"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00677"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
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
<a id="l00762"></a>
<a id="foldopen00770"></a>
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
<a id="foldopen00791"></a>
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
<a id="foldopen00812"></a>
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
<a id="foldopen00833"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="foldopen00845"></a>
<a id="l00845"></a>
<a id="l00846"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="foldopen00857"></a>
<a id="l00857"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="foldopen00869"></a>
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
<a id="foldopen00890"></a>
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
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00961"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="l00997"></a>
<a id="l01011"></a>
<a id="l01012"></a>
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
<a id="l01060"></a>
<a id="foldopen01061"></a>
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
<a id="l01096"></a>
<a id="foldopen01097"></a>
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
<a id="l01125"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="foldopen01128"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="l01134"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01145"></a>
<a id="l01146"></a>
<a id="l01147"></a>
<a id="foldopen01148"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01150"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="l01153"></a>
<a id="l01154"></a>
<a id="l01155"></a>
<a id="l01156"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01170"></a>
<a id="foldopen01171"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01173"></a>
<a id="l01174"></a>
<a id="l01175"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="l01191"></a>
<a id="foldopen01192"></a>
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
<a id="foldopen01212"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01215"></a>
<a id="l01216"></a>
<a id="l01231"></a>
<a id="l01232"></a>
<a id="l01233"></a>
<a id="l01234"></a>
<a id="foldopen01235"></a>
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
<a id="l01252"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="foldopen01255"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01258"></a>
<a id="l01259"></a>
<a id="l01260"></a>
<a id="l01261"></a>
<a id="l01262"></a>
<a id="l01270"></a>
<a id="l01271"></a>
<a id="l01272"></a>
<a id="foldopen01273"></a>
<a id="l01273"></a>
<a id="l01274"></a>
<a id="l01275"></a>
<a id="l01276"></a>
<a id="l01277"></a>
<a id="l01278"></a>
<a id="l01279"></a>
<a id="l01280"></a>
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
<a id="l01313"></a>
<a id="l01331"></a>
<a id="l01332"></a>
<a id="l01333"></a>
<a id="l01334"></a>
<a id="l01335"></a>
<a id="l01358"></a>
<a id="l01359"></a>
<a id="l01360"></a>
<a id="l01361"></a>
<a id="l01362"></a>
<a id="l01363"></a>
<a id="l01380"></a>
<a id="l01381"></a>
<a id="l01382"></a>
<a id="l01383"></a>
<a id="l01384"></a>
<a id="l01385"></a>
<a id="foldopen01395"></a>
<a id="l01395"></a>
<a id="l01396"></a>
<a id="l01397"></a>
<a id="foldopen01405"></a>
<a id="l01405"></a>
<a id="l01406"></a>
<a id="l01407"></a>
<a id="foldopen01409"></a>
<a id="l01409"></a>
<a id="l01411"></a>
<a id="l01413"></a>
<a id="l01418"></a>
<a id="l01420"></a>
<a id="l01421"></a>
<a id="l01422"></a>
<a id="foldopen01424"></a>
<a id="l01424"></a>
<a id="l01426"></a>
<a id="l01433"></a>
<a id="l01435"></a>
<a id="l01436"></a>
<a id="l01441"></a>
<a id="l01442"></a>
<a id="l01443"></a>
<a id="l01444"></a>
<a id="foldopen01459"></a>
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
<a id="l01494"></a>
<a id="l01495"></a>
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
<a id="l01536"></a>
<a id="foldopen01542"></a>
<a id="l01542"></a>
<a id="l01543"></a>
<a id="l01544"></a>
<a id="l01545"></a>
<a id="l01546"></a>
<a id="l01547"></a>
<a id="l01548"></a>
<a id="l01549"></a>
<a id="l01550"></a>
<a id="foldopen01558"></a>
<a id="l01558"></a>
<a id="l01559"></a>
<a id="l01560"></a>
<a id="l01568"></a>
<a id="l01569"></a>
<a id="foldopen01576"></a>
<a id="l01576"></a>
<a id="l01577"></a>
<a id="l01578"></a>
<a id="l01579"></a>
<a id="l01580"></a>
<a id="foldopen01587"></a>
<a id="l01587"></a>
<a id="l01588"></a>
<a id="l01589"></a>
<a id="l01590"></a>
<a id="l01591"></a>
<a id="l01601"></a>
<a id="l01602"></a>
<a id="l01612"></a>
<a id="l01613"></a>
<a id="l01632"></a>
<a id="l01633"></a>
<a id="l01634"></a>
<a id="l01642"></a>
<a id="l01643"></a>
<a id="l01652"></a>
<a id="l01653"></a>
<a id="l01654"></a>
<a id="foldopen01655"></a>
<a id="l01655"></a>
<a id="l01656"></a>
<a id="l01657"></a>
<a id="l01658"></a>
<a id="l01659"></a>
<a id="l01660"></a>
<a id="l01661"></a>
<a id="l01662"></a>
<a id="l01672"></a>
<a id="l01673"></a>
<a id="foldopen01681"></a>
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
<a id="foldopen01698"></a>
<a id="l01698"></a>
<a id="l01699"></a>
<a id="l01700"></a>
<a id="l01701"></a>
<a id="l01702"></a>
<a id="l01703"></a>
<a id="l01704"></a>
<a id="l01705"></a>
<a id="l01706"></a>
<a id="foldopen01712"></a>
<a id="l01712"></a>
<a id="l01713"></a>
<a id="l01714"></a>
<a id="l01715"></a>
<a id="l01716"></a>
<a id="l01717"></a>
<a id="l01718"></a>
<a id="l01719"></a>
<a id="l01720"></a>
<a id="l01724"></a>
<a id="l01725"></a>
<a id="l01726"></a>
<a id="l01727"></a>
<a id="l01728"></a>
<a id="l01729"></a>
<a id="l01730"></a>
<a id="l01731"></a>
<a id="aatomic_8h_html"></a>
<a id="aclock_8h_html"></a>
<a id="aethernet__vlan_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__ethernet_html_ga010a95a0239a800131ac3d43dd54737f"></a>
<a id="agroup__ethernet_html_ga1246be489eb7130100bbaebbb73961c5"></a>
<a id="agroup__ethernet_html_ga139cc696837611a522b289f2ea7bf6fc"></a>
<a id="agroup__ethernet_html_ga16cbc14e3a0a470bbbd5aeb5e73dc1de"></a>
<a id="agroup__ethernet_html_ga237aab2d07ffa84355981d02a4576ebe"></a>
<a id="agroup__ethernet_html_ga26984472437a98b00c31156f75558134"></a>
<a id="agroup__ethernet_html_ga2755ecb84e9759c24302e33a56a1fc84"></a>
<a id="agroup__ethernet_html_ga37ff48434c56bbb24422dd805449b6f3"></a>
<a id="agroup__ethernet_html_ga399425f810c00bcf9babec019bc2ff12"></a>
<a id="agroup__ethernet_html_ga3cd2e9abc38bdd7eb0cb3932d96fd90e"></a>
<a id="agroup__ethernet_html_ga3e578035be797bbbafafa56dedaa8320"></a>
<a id="agroup__ethernet_html_ga42a3c6b04ef8827e3443c5aebe5541b9"></a>
<a id="agroup__ethernet_html_ga6184c43a62e4af9958412f99991358c9"></a>
<a id="agroup__ethernet_html_ga62b33344256bbe228689e2cb541a0874"></a>
<a id="agroup__ethernet_html_ga6e603f6f74e6d7e988e7119a6df2ab4d"></a>
<a id="agroup__ethernet_html_ga7225d06fbaa12d4668fa165d9e8f0845"></a>
<a id="agroup__ethernet_html_ga76a5fe39ce12478c666d87f4aec3d579"></a>
<a id="agroup__ethernet_html_ga78aad58ec66710034cab8891ad638a2c"></a>
<a id="agroup__ethernet_html_ga80adc03695a8fbb9dbc9dd3adec78c04"></a>
<a id="agroup__ethernet_html_ga84c37db5687c5264bec99976a1108ab6"></a>
<a id="agroup__ethernet_html_ga89964de263029223d119f361fbd94bfd"></a>
<a id="agroup__ethernet_html_ga8ca1eccc88a351241298d358ec28fdf5"></a>
<a id="agroup__ethernet_html_ga8d28addcef0038c4ba1daa84bc104143"></a>
<a id="agroup__ethernet_html_ga9162ff11d626813fc840df0b67820ac5"></a>
<a id="agroup__ethernet_html_ga920bddac077675d544a21fb5650c945e"></a>
<a id="agroup__ethernet_html_ga93e498e99c155fc402a26a4429d044a0"></a>
<a id="agroup__ethernet_html_ga97ef5a8ad9157e2db12e9caf6faef5e7"></a>
<a id="agroup__ethernet_html_gaa0ef2f94fd18da9c5ea675b46faac8d0"></a>
<a id="agroup__ethernet_html_gaa64462598843dd9f6e731198498aea31"></a>
<a id="agroup__ethernet_html_gaa7f447129b5b8392640f849d18e9246b"></a>
<a id="agroup__ethernet_html_gab0a3b4584bb6ce1d27b98b063fd3fcbd"></a>
<a id="agroup__ethernet_html_gab71a741cea5f645f4354a1abc9c95a50"></a>
<a id="agroup__ethernet_html_gabf86b7f09a9d041eea25357cd7a85ede"></a>
<a id="agroup__ethernet_html_gabfab900bfd7a9078e7ac2fd6aed9ce83"></a>
<a id="agroup__ethernet_html_gac2433b0d82ef25373b2c0f994e248e92"></a>
<a id="agroup__ethernet_html_gac536aa7154c4a8d194ec67efb68e275c"></a>
<a id="agroup__ethernet_html_gad9d890dcf7f5ee3659bf3bd5949faa4e"></a>
<a id="agroup__ethernet_html_gae617887d42a288697f2507c5b0907909"></a>
<a id="agroup__ethernet_html_gae66b24a847f8e0ad119c6c466331afd6"></a>
<a id="agroup__ethernet_html_gae91a64c96e0a480927d92271092a158d"></a>
<a id="agroup__ethernet_html_gaec6fb3c05792bdd30596137686f3251a"></a>
<a id="agroup__ethernet_html_gaeddfa5b3ff6e356393114b351f87fe43"></a>
<a id="agroup__ethernet_html_gaf20472f9d60e5cddffed2919b3091030"></a>
<a id="agroup__ethernet_html_gafbb76d53f9f80628d18d39368a28f984"></a>
<a id="agroup__ethernet_html_gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530"></a>
<a id="agroup__ethernet_html_gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a12991c85e1a7405bd145b3fff8aeecf1"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a2c59d7d5a1d5eff15976806d237960c1"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a2eeaa2befc2d7a38f0318addef88f072"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a4508489dc8a67ef908757a9e2338babb"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a55e8d0ee975acc9eabf5096d1b926f6b"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5a9ab79aee30b73747fceff86fd3b967f9"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861"></a>
<a id="agroup__ethernet_html_gga9162ff11d626813fc840df0b67820ac5afe48cf59ca4d1db42e768ca272159d55"></a>
<a id="agroup__ethernet_html_ggabf86b7f09a9d041eea25357cd7a85edea03e31130ecef7ac032bceed6f3091af8"></a>
<a id="agroup__ethernet_html_ggabf86b7f09a9d041eea25357cd7a85edea3346f0e3d0b350c7fe663cfe389c1e02"></a>
<a id="agroup__ethernet_html_ggabf86b7f09a9d041eea25357cd7a85edea557127c3bc97969fe57fcd8ac55567b5"></a>
<a id="agroup__ethernet_html_ggabf86b7f09a9d041eea25357cd7a85edea5671ade139cb0cd28d02e3215337acb9"></a>
<a id="agroup__ethernet_html_ggabf86b7f09a9d041eea25357cd7a85edea6485d2abcd3dae6786022aa286234ed4"></a>
<a id="agroup__ethernet_html_ggabf86b7f09a9d041eea25357cd7a85edea90314c44dca3c123d1a0bd70f108524d"></a>
<a id="agroup__ethernet_html_ggabf86b7f09a9d041eea25357cd7a85edeac64b392a0591cfe7aa5564a476fe20be"></a>
<a id="agroup__ethernet_html_ggabfab900bfd7a9078e7ac2fd6aed9ce83a3a094b0237833d4523e04d7b6bb5fbab"></a>
<a id="agroup__ethernet_html_ggabfab900bfd7a9078e7ac2fd6aed9ce83a6bb1bfaf79f232101bc91ab02f54e4a7"></a>
<a id="agroup__ethernet_html_ggabfab900bfd7a9078e7ac2fd6aed9ce83ad41e45f16877f28b44ec23fadb35d355"></a>
<a id="agroup__ethernet_html_ggac2433b0d82ef25373b2c0f994e248e92a3fad5d3a2578e83da31f3188add46b87"></a>
<a id="agroup__ethernet_html_ggac2433b0d82ef25373b2c0f994e248e92a730e86dd6e257352afb233fdcc189955"></a>
<a id="agroup__ethernet_html_ggac2433b0d82ef25373b2c0f994e248e92a8b1eb5edcd9f4953d56c9c10088d6bb5"></a>
<a id="agroup__ethernet_html_ggac2433b0d82ef25373b2c0f994e248e92a9e0096f69300cf30c1f78c33074c1bda"></a>
<a id="agroup__lldp_html_ga1e9fb662d7cdfc3c4c68cfd0312987cf"></a>
<a id="agroup__net__if_html_ga3cad2d51fc9cc225619585e06e252db0"></a>
<a id="agroup__net__if_html_gaeb8c703f273bc07ae9bb7a0d8bfe6f3d"></a>
<a id="agroup__net__l2_html_gac7db0cc6c56d371a5803873074ec2516"></a>
<a id="agroup__nvmem__interface_html_ga5db94733cecfd4b46dd87ee07128d58d"></a>
<a id="agroup__random__api_html_gaf4f6792ac29c876d59ace1deae53bbd7"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga0030614bc864d1b24eaedd71585acc27"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="agroup__virtual_html_gabadf14eaa02978cde7030c99ddd3e279"></a>
<a id="agroup__vlan__api_html_ga665458f4b8f9c83ea0c1609207d3dd70"></a>
<a id="agroup__vlan__api_html_gad1db5bb85a9744c8a8af8d2e1ebcfe69"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="alldp_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="anvmem_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aptp__time_8h_html"></a>
<a id="arandom_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astring_8h_html_af0f01bffcd16daa9143f6014d10a25ad"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a4a2e6a2cfeb6efed7d5383c33458f46d"></a>
<a id="astructethernet__api_html"></a>
<a id="astructethernet__api_html_a03dfbaed9cdf2bdd17b0bfd28d5a1056"></a>
<a id="astructethernet__api_html_a4ebe0d6cf70a7b5a1fff87c3ca6cb86e"></a>
<a id="astructethernet__api_html_a8dba118b707305e1b909a82f7742dd5e"></a>
<a id="astructethernet__api_html_a8f6fd0d640b5a883c9f5150d9ed71241"></a>
<a id="astructethernet__api_html_aa283f6f201f50ffdd976275374f5c828"></a>
<a id="astructethernet__api_html_aa34137c564f84fdb3160a767348c4a58"></a>
<a id="astructethernet__api_html_ae7c0f0b5162f5fb6b1a49ce4b52249b0"></a>
<a id="astructethernet__filter_html"></a>
<a id="astructethernet__filter_html_aaacda9b89d6b21934654e0f2b19624e0"></a>
<a id="astructethernet__filter_html_ad83053c859c65e0c0432fe3f59671335"></a>
<a id="astructethernet__filter_html_aec00b1ecd6af658a5164d375bccdaa10"></a>
<a id="astructethernet__lldp_html"></a>
<a id="astructethernet__lldp_html_a732d685dd27d2be5cb6b51175b8af70f"></a>
<a id="astructethernet__lldp_html_a8cf37774b067ffbc4876e42c3b28e536"></a>
<a id="astructethernet__lldp_html_a8d2452f182c52000bec93f4c53501220"></a>
<a id="astructethernet__lldp_html_a9a1123c7f9e799b6fe815c554df6f023"></a>
<a id="astructethernet__lldp_html_aabc1141bbc72a17e3884138c61bd5b0c"></a>
<a id="astructethernet__lldp_html_aede4281b7f53be43f524d47bb2c606d1"></a>
<a id="astructethernet__qav__param_html"></a>
<a id="astructethernet__qav__param_html_a031d3896b14eb8b32c3c050738421b85"></a>
<a id="astructethernet__qav__param_html_a0691f10a338d3c49a58d94a1adced477"></a>
<a id="astructethernet__qav__param_html_a38861d9f790a61aa88801cb1373077a8"></a>
<a id="astructethernet__qav__param_html_a4a795e4a0c7d5bcbe8212d79f772dc6f"></a>
<a id="astructethernet__qav__param_html_a4e2d2967669b758422c166140af0c1ba"></a>
<a id="astructethernet__qav__param_html_a6d43b199549cade0a07dc10adac85bff"></a>
<a id="astructethernet__qav__param_html_a6fde906da905c0598aaa2056c330b6f4"></a>
<a id="astructethernet__qbu__param_html"></a>
<a id="astructethernet__qbu__param_html_a3f5dfd9cfbc1ec86896eaf517bdc5c88"></a>
<a id="astructethernet__qbu__param_html_a3f62d0462376225c8609c7e26ebd314b"></a>
<a id="astructethernet__qbu__param_html_a4a8a3d26a12a06a787ae6b35ea40c37a"></a>
<a id="astructethernet__qbu__param_html_a8ffde09a540817b7a68c7180c327196f"></a>
<a id="astructethernet__qbu__param_html_a9717dd68adde62a454593d72fdbc43a5"></a>
<a id="astructethernet__qbu__param_html_ad8c92a7f7b4aa124adaa62dd4e65b5ca"></a>
<a id="astructethernet__qbu__param_html_ae6d61f0c9d2f2e56eb494db953a5e846"></a>
<a id="astructethernet__qbu__param_html_afb455507b29d84de42638e47ecacadeb"></a>
<a id="astructethernet__qbv__param_html"></a>
<a id="astructethernet__qbv__param_html_a037492458f47905b894a2269ff7365cd"></a>
<a id="astructethernet__qbv__param_html_a0742dbe52f01addbb319e2fcb354d064"></a>
<a id="astructethernet__qbv__param_html_a216046de6134584ae05b53609d368bb9"></a>
<a id="astructethernet__qbv__param_html_a2184250d397bd749764adc52ec3a1621"></a>
<a id="astructethernet__qbv__param_html_a2c256aa3f65dfa75434752903daa809c"></a>
<a id="astructethernet__qbv__param_html_a36702c57bea42c37c1341e144ced4f7d"></a>
<a id="astructethernet__qbv__param_html_a44b6ce52faeae761c5ebe49fad5338cd"></a>
<a id="astructethernet__qbv__param_html_a53646a44e8b0e1f6588c357d49d97693"></a>
<a id="astructethernet__qbv__param_html_a76220e58aa31ae6cfd92268277716c7a"></a>
<a id="astructethernet__qbv__param_html_a8471f7eb20a72bb16fe7abb0b2bb24f7"></a>
<a id="astructethernet__qbv__param_html_aa6b2be0014988752e326bdc1fe6ef161"></a>
<a id="astructethernet__qbv__param_html_ad07589ae6802a9c3c4c3f809427129be"></a>
<a id="astructethernet__qbv__param_html_afc0c26fcdeee1a921a2f549de4d1c33e"></a>
<a id="astructethernet__txtime__param_html"></a>
<a id="astructethernet__txtime__param_html_a74b1e05cf0fac8aa435ba966e110ae27"></a>
<a id="astructethernet__txtime__param_html_aa4a46b7153b2a69ca0134f4e10bc7165"></a>
<a id="astructethernet__txtime__param_html_ab4a709e6907e76f9cf23c085f5be5d99"></a>
<a id="astructk__timepoint__t_html"></a>
<a id="astructnet__eth__addr_html"></a>
<a id="astructnet__eth__addr_html_af370baeb1f10475331db8628c3c9efbe"></a>
<a id="astructnet__eth__mac__config_html"></a>
<a id="astructnet__eth__mac__config_html_a0bac0f7f2af6cb03eeb90435799c7a2d"></a>
<a id="astructnet__eth__mac__config_html_a344aa4435360014cc6080dc0ba2d7dc3"></a>
<a id="astructnet__eth__mac__config_html_a66656331031d3324e4fd0429028311f4"></a>
<a id="astructnet__eth__mac__config_html_aa9e496b7d76e2920381365275a405412"></a>
<a id="astructnet__eth__mcast__addr_html"></a>
<a id="astructnet__eth__mcast__addr_html_a5c7f1a2351a493681525a5c610389e15"></a>
<a id="astructnet__eth__mcast__addr_html_ab8a4a73276b5236befb1ac34a379f689"></a>
<a id="astructnet__eth__mcast__addr_html_af8dec139bae61ede5a2233ab0f3c66a4"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__in6__addr_html"></a>
<a id="astructnet__in__addr_html"></a>
<a id="astructnet__lldpdu_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__ptp__extended__time_html"></a>
<a id="astructnet__ptp__time_html"></a>
<a id="astructnet__stats__eth_html"></a>
<a id="astructnvmem__cell_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="avirtual_8h_html"></a>

```c


/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_ETHERNET_H_
#define ZEPHYR_INCLUDE_NET_ETHERNET_H_

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/sys/atomic.h>

#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_pkt.h>
#include <zephyr/net/lldp.h>
#include <zephyr/sys/clock.h>
#include <zephyr/sys/util.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/ethernet_vlan.h>
#include <zephyr/net/ptp_time.h>
#include <zephyr/net/virtual.h>
#include <zephyr/random/random.h>

#if defined(CONFIG_NVMEM)
#include <zephyr/nvmem.h>
#endif

#ifdef __cplusplus
extern "C" {
#endif


#define NET_ETH_ADDR_LEN                6U

struct net_eth_addr {
        uint8_t addr[NET_ETH_ADDR_LEN];
};


#define NET_ETH_HDR(pkt) ((struct net_eth_hdr *)net_pkt_data(pkt))

/* clang-format off */
/* zephyr-keep-sorted-start */
#define NET_ETH_PTYPE_ALL               0x0003 /* from linux/if_ether.h */
#define NET_ETH_PTYPE_ARP               0x0806
#define NET_ETH_PTYPE_CAN               0x000C /* CAN: Controller Area Network */
#define NET_ETH_PTYPE_CANFD             0x000D /* CANFD: CAN flexible data rate*/
#define NET_ETH_PTYPE_EAPOL             0x888e
#define NET_ETH_PTYPE_ECAT              0x88a4
#define NET_ETH_PTYPE_HDLC              0x0019 /* HDLC frames (like in PPP) */
#define NET_ETH_PTYPE_IEEE802154        0x00F6 /* from linux/if_ether.h: IEEE802.15.4 frame */
#define NET_ETH_PTYPE_IP                0x0800
#define NET_ETH_PTYPE_IPV6              0x86dd
#define NET_ETH_PTYPE_LLDP              0x88cc
#define NET_ETH_PTYPE_OAM               0x8902
#define NET_ETH_PTYPE_PTP               0x88f7
#define NET_ETH_PTYPE_TSN               0x22f0 /* TSN (IEEE 1722) packet */
#define NET_ETH_PTYPE_VLAN              0x8100
/* zephyr-keep-sorted-stop */
/* clang-format on */

/* zephyr-keep-sorted-start re(^#define) */
#if !defined(ETH_P_8021Q)
#define ETH_P_8021Q     NET_ETH_PTYPE_VLAN
#endif
#if !defined(ETH_P_ALL)
#define ETH_P_ALL       NET_ETH_PTYPE_ALL
#endif
#if !defined(ETH_P_ARP)
#define ETH_P_ARP       NET_ETH_PTYPE_ARP
#endif
#if !defined(ETH_P_CAN)
#define ETH_P_CAN       NET_ETH_PTYPE_CAN
#endif
#if !defined(ETH_P_CANFD)
#define ETH_P_CANFD     NET_ETH_PTYPE_CANFD
#endif
#if !defined(ETH_P_EAPOL)
#define ETH_P_EAPOL     NET_ETH_PTYPE_EAPOL
#endif
#if !defined(ETH_P_ECAT)
#define ETH_P_ECAT      NET_ETH_PTYPE_ECAT
#endif
#if !defined(ETH_P_HDLC)
#define ETH_P_HDLC      NET_ETH_PTYPE_HDLC
#endif
#if !defined(ETH_P_IEEE802154)
#define ETH_P_IEEE802154 NET_ETH_PTYPE_IEEE802154
#endif
#if !defined(ETH_P_IP)
#define ETH_P_IP        NET_ETH_PTYPE_IP
#endif
#if !defined(ETH_P_IPV6)
#define ETH_P_IPV6      NET_ETH_PTYPE_IPV6
#endif
#if !defined(ETH_P_TSN)
#define ETH_P_TSN       NET_ETH_PTYPE_TSN
#endif
/* zephyr-keep-sorted-stop */


#define NET_ETH_MINIMAL_FRAME_SIZE      60
#define NET_ETH_MTU                     1500


#if defined(CONFIG_NET_VLAN)
#define _NET_ETH_MAX_HDR_SIZE           (sizeof(struct net_eth_vlan_hdr))
#else
#define _NET_ETH_MAX_HDR_SIZE           (sizeof(struct net_eth_hdr))
#endif

#define _NET_ETH_MAX_FRAME_SIZE (NET_ETH_MTU + _NET_ETH_MAX_HDR_SIZE)

#if defined(CONFIG_DSA_TAG_SIZE)
#define DSA_TAG_SIZE CONFIG_DSA_TAG_SIZE
#else
#define DSA_TAG_SIZE 0
#endif

#define NET_ETH_MAX_FRAME_SIZE (_NET_ETH_MAX_FRAME_SIZE + DSA_TAG_SIZE)
#define NET_ETH_MAX_HDR_SIZE (_NET_ETH_MAX_HDR_SIZE + DSA_TAG_SIZE)

#define NET_ETH_VLAN_HDR_SIZE   4


enum ethernet_hw_caps {
        ETHERNET_HW_TX_CHKSUM_OFFLOAD   = BIT(0),

        ETHERNET_HW_RX_CHKSUM_OFFLOAD   = BIT(1),

        ETHERNET_HW_VLAN                = BIT(2),

        ETHERNET_LINK_10BASE            = BIT(3),

        ETHERNET_LINK_100BASE           = BIT(4),

        ETHERNET_LINK_1000BASE          = BIT(5),

        ETHERNET_LINK_2500BASE          = BIT(6),

        ETHERNET_LINK_5000BASE          = BIT(7),

        ETHERNET_QAV                    = BIT(9),

        ETHERNET_PROMISC_MODE           = BIT(10),

        ETHERNET_PRIORITY_QUEUES        = BIT(11),

        ETHERNET_HW_FILTERING           = BIT(12),

        ETHERNET_LLDP                   = BIT(13),

        ETHERNET_HW_VLAN_TAG_STRIP      = BIT(14),

        ETHERNET_DSA_USER_PORT          = BIT(15),

        ETHERNET_DSA_CONDUIT_PORT       = BIT(16),

        ETHERNET_QBV                    = BIT(17),

        ETHERNET_QBU                    = BIT(18),

        ETHERNET_TXTIME                 = BIT(19),

        ETHERNET_TXINJECTION_MODE       = BIT(20),
};


enum dsa_port_type {
        NON_DSA_PORT,
        DSA_CONDUIT_PORT,
        DSA_USER_PORT,
        DSA_CPU_PORT,
        DSA_PORT,
};

enum ethernet_config_type {
        ETHERNET_CONFIG_TYPE_MAC_ADDRESS,
        ETHERNET_CONFIG_TYPE_QAV_PARAM,
        ETHERNET_CONFIG_TYPE_QBV_PARAM,
        ETHERNET_CONFIG_TYPE_QBU_PARAM,
        ETHERNET_CONFIG_TYPE_TXTIME_PARAM,
        ETHERNET_CONFIG_TYPE_PROMISC_MODE,
        ETHERNET_CONFIG_TYPE_PRIORITY_QUEUES_NUM,
        ETHERNET_CONFIG_TYPE_FILTER,
        ETHERNET_CONFIG_TYPE_PORTS_NUM,
        ETHERNET_CONFIG_TYPE_TXINJECTION_MODE,
        ETHERNET_CONFIG_TYPE_RX_CHECKSUM_SUPPORT,
        ETHERNET_CONFIG_TYPE_TX_CHECKSUM_SUPPORT,
        ETHERNET_CONFIG_TYPE_EXTRA_TX_PKT_HEADROOM,
};

enum ethernet_qav_param_type {
        ETHERNET_QAV_PARAM_TYPE_DELTA_BANDWIDTH,
        ETHERNET_QAV_PARAM_TYPE_IDLE_SLOPE,
        ETHERNET_QAV_PARAM_TYPE_OPER_IDLE_SLOPE,
        ETHERNET_QAV_PARAM_TYPE_TRAFFIC_CLASS,
        ETHERNET_QAV_PARAM_TYPE_STATUS,
};


struct ethernet_qav_param {
        int queue_id;
        enum ethernet_qav_param_type type;
        union {
                bool enabled;
                unsigned int delta_bandwidth;
                unsigned int idle_slope;
                unsigned int oper_idle_slope;
                unsigned int traffic_class;
        } ;
};


enum ethernet_qbv_param_type {
        ETHERNET_QBV_PARAM_TYPE_STATUS,
        ETHERNET_QBV_PARAM_TYPE_GATE_CONTROL_LIST,
        ETHERNET_QBV_PARAM_TYPE_GATE_CONTROL_LIST_LEN,
        ETHERNET_QBV_PARAM_TYPE_TIME,
};

enum ethernet_qbv_state_type {
        ETHERNET_QBV_STATE_TYPE_ADMIN,
        ETHERNET_QBV_STATE_TYPE_OPER,
};

enum ethernet_gate_state_operation {
        ETHERNET_SET_GATE_STATE,
        ETHERNET_SET_AND_HOLD_MAC_STATE,
        ETHERNET_SET_AND_RELEASE_MAC_STATE,
};


struct ethernet_qbv_param {
        int port_id;
        enum ethernet_qbv_param_type type;
        enum ethernet_qbv_state_type state;
        union {
                bool enabled;

                struct {
                        bool gate_status[NET_TC_TX_COUNT];

                        enum ethernet_gate_state_operation operation;

                        uint32_t time_interval;

                        uint16_t row;
                } gate_control;

                uint32_t gate_control_list_len;

                struct {
                        struct net_ptp_extended_time base_time;

                        struct net_ptp_time cycle_time;

                        uint32_t extension_time;
                };
        } ;
};


enum ethernet_qbu_param_type {
        ETHERNET_QBU_PARAM_TYPE_STATUS,
        ETHERNET_QBU_PARAM_TYPE_RELEASE_ADVANCE,
        ETHERNET_QBU_PARAM_TYPE_HOLD_ADVANCE,
        ETHERNET_QBU_PARAM_TYPE_PREEMPTION_STATUS_TABLE,

        /* Some preemption settings are from Qbr spec. */
        ETHERNET_QBR_PARAM_TYPE_LINK_PARTNER_STATUS,
        ETHERNET_QBR_PARAM_TYPE_ADDITIONAL_FRAGMENT_SIZE,
};

enum ethernet_qbu_preempt_status {
        ETHERNET_QBU_STATUS_EXPRESS,
        ETHERNET_QBU_STATUS_PREEMPTABLE
} __packed;


struct ethernet_qbu_param {
        int port_id;
        enum ethernet_qbu_param_type type;
        union {
                uint32_t hold_advance;

                uint32_t release_advance;

                enum ethernet_qbu_preempt_status
                                frame_preempt_statuses[NET_TC_TX_COUNT];

                bool enabled;

                bool link_partner_status;

                uint8_t additional_fragment_size : 2;
        } ;
};


enum ethernet_filter_type {
        ETHERNET_FILTER_TYPE_SRC_MAC_ADDRESS,
        ETHERNET_FILTER_TYPE_DST_MAC_ADDRESS,
};


enum ethernet_if_types {
        L2_ETH_IF_TYPE_ETHERNET,

        L2_ETH_IF_TYPE_WIFI,
} __packed;

struct ethernet_filter {
        enum ethernet_filter_type type;
        struct net_eth_addr mac_address;
        bool set;
};


/* How many L2 multicast addresses one interface can track. The build system
 * sums up what the subsystems asked for and gives the result here, the
 * Kconfig value is only the floor and is used if the header is compiled
 * outside of a Zephyr build.
 */
#ifndef NET_ETH_MCAST_FILTER_COUNT
#define NET_ETH_MCAST_FILTER_COUNT CONFIG_NET_L2_ETHERNET_MCAST_FILTER_COUNT
#endif

/* The L2 multicast addresses are tracked only if something joins the groups,
 * either the IP level, a packet socket, or other parts of the system.
 */
#if defined(CONFIG_NET_L2_ETHERNET) && !defined(CONFIG_NET_RAW_MODE) && \
        (NET_ETH_MCAST_FILTER_COUNT > 0)
#define NET_ETH_MCAST_FILTER_SUPPORTED 1
#endif


struct net_eth_mcast_addr {
        struct net_eth_addr addr;

        atomic_t atomic_ref;

        uint8_t is_used : 1;

        uint8_t _unused : 7;
};


enum ethernet_txtime_param_type {
        ETHERNET_TXTIME_PARAM_TYPE_ENABLE_QUEUES,
};


struct ethernet_txtime_param {
        enum ethernet_txtime_param_type type;
        int queue_id;
        bool enable_txtime;
};

enum ethernet_checksum_support {
        ETHERNET_CHECKSUM_SUPPORT_NONE                  = NET_IF_CHECKSUM_NONE_BIT,
        ETHERNET_CHECKSUM_SUPPORT_IPV4_HEADER           = NET_IF_CHECKSUM_IPV4_HEADER_BIT,
        ETHERNET_CHECKSUM_SUPPORT_IPV4_ICMP             = NET_IF_CHECKSUM_IPV4_ICMP_BIT,
        ETHERNET_CHECKSUM_SUPPORT_IPV6_HEADER           = NET_IF_CHECKSUM_IPV6_HEADER_BIT,
        ETHERNET_CHECKSUM_SUPPORT_IPV6_ICMP             = NET_IF_CHECKSUM_IPV6_ICMP_BIT,
        ETHERNET_CHECKSUM_SUPPORT_TCP                   = NET_IF_CHECKSUM_TCP_BIT,
        ETHERNET_CHECKSUM_SUPPORT_UDP                   = NET_IF_CHECKSUM_UDP_BIT,
};


struct ethernet_config {
        union {
                bool promisc_mode;
                bool txinjection_mode;

                struct net_eth_addr mac_address;

                struct ethernet_qav_param qav_param;
                struct ethernet_qbv_param qbv_param;
                struct ethernet_qbu_param qbu_param;
                struct ethernet_txtime_param txtime_param;

                int priority_queues_num;
                int ports_num;

                enum ethernet_checksum_support chksum_support;

                struct ethernet_filter filter;

                uint16_t extra_tx_pkt_headroom;
        } ;
};


enum ethernet_stats_type {
        ETHERNET_STATS_TYPE_COMMON = BIT(0),
        ETHERNET_STATS_TYPE_VENDOR = BIT(1),
        ETHERNET_STATS_TYPE_ALL = 0xFFFFFFFFU,
};

struct ethernet_api {
        struct net_if_api iface_api;

#if defined(CONFIG_NET_STATISTICS_ETHERNET)
        struct net_stats_eth *(*get_stats)(const struct device *dev, struct net_if *iface);

        struct net_stats_eth *(*get_stats_type)(const struct device *dev,
                                                 struct net_if *iface,
                                                 uint32_t type);
#endif

        int (*start)(const struct device *dev, struct net_if *iface);

        int (*stop)(const struct device *dev, struct net_if *iface);

        enum ethernet_hw_caps (*get_capabilities)(const struct device *dev, struct net_if *iface);

        int (*set_config)(const struct device *dev,
                          struct net_if *iface,
                          enum ethernet_config_type type,
                          const struct ethernet_config *config);

        int (*get_config)(const struct device *dev,
                          struct net_if *iface,
                          enum ethernet_config_type type,
                          struct ethernet_config *config);

#if defined(CONFIG_NET_VLAN)
        int (*vlan_setup)(const struct device *dev, struct net_if *iface,
                          uint16_t tag, bool enable);
#endif /* CONFIG_NET_VLAN */

#if defined(CONFIG_PTP_CLOCK)
        const struct device *(*get_ptp_clock)(const struct device *dev, struct net_if *iface);
#endif /* CONFIG_PTP_CLOCK */

        const struct device *(*get_phy)(const struct device *dev, struct net_if *iface);

        int (*send)(const struct device *dev, struct net_pkt *pkt);
};


/* Make sure that the network interface API is properly setup inside
 * Ethernet API struct (it is the first one).
 */
BUILD_ASSERT(offsetof(struct ethernet_api, iface_api) == 0);

struct net_eth_hdr {
        struct net_eth_addr dst;
        struct net_eth_addr src;
        uint16_t type;
} __packed;

struct ethernet_vlan {
        struct net_if *iface;

        uint16_t tag;
};

#if defined(CONFIG_NET_VLAN_COUNT)
#define NET_VLAN_MAX_COUNT CONFIG_NET_VLAN_COUNT
#else
#define NET_VLAN_MAX_COUNT 0
#endif


struct ethernet_lldp {
        sys_snode_t node;

        const struct net_lldpdu *lldpdu;

        const uint8_t *optional_du;

        size_t optional_len;

        k_timepoint_t tx_timer_timeout;

        net_lldp_recv_cb_t cb;
};


enum ethernet_flags {
        ETH_CARRIER_UP,
};

struct ethernet_context {
        atomic_t flags;

#if defined(CONFIG_NET_ETHERNET_BRIDGE)
        struct net_if *bridge;
#endif

        struct k_work carrier_work;

        struct net_if *iface;

#if defined(CONFIG_NET_LLDP)
        struct ethernet_lldp lldp;
#endif

        enum net_l2_flags ethernet_l2_flags;

#if defined(CONFIG_NET_GPTP)
        uint16_t gptp_port;
#endif

#if defined(CONFIG_NET_DSA)
        enum dsa_port_type dsa_port;

        void *dsa_switch_ctx;
#endif

#if defined(NET_ETH_MCAST_FILTER_SUPPORTED)
        struct net_eth_mcast_addr mcast_addrs[NET_ETH_MCAST_FILTER_COUNT];
#endif

        bool is_net_carrier_up : 1;

        bool is_init : 1;

        enum ethernet_if_types eth_if_type;
};

void ethernet_init(struct net_if *iface);

#define ETHERNET_L2_CTX_TYPE    struct ethernet_context

/* Separate header for VLAN as some of device interfaces might not
 * support VLAN.
 */
struct net_eth_vlan_hdr {
        struct net_eth_addr dst;
        struct net_eth_addr src;
        struct {
                uint16_t tpid; /* tag protocol id  */
                uint16_t tci;  /* tag control info */
        } vlan;
        uint16_t type;
} __packed;


static inline bool net_eth_is_addr_broadcast(struct net_eth_addr *addr)
{
        if (addr->addr[0] == 0xff &&
            addr->addr[1] == 0xff &&
            addr->addr[2] == 0xff &&
            addr->addr[3] == 0xff &&
            addr->addr[4] == 0xff &&
            addr->addr[5] == 0xff) {
                return true;
        }

        return false;
}

static inline bool net_eth_is_addr_all_zeroes(struct net_eth_addr *addr)
{
        if (addr->addr[0] == 0x00 &&
            addr->addr[1] == 0x00 &&
            addr->addr[2] == 0x00 &&
            addr->addr[3] == 0x00 &&
            addr->addr[4] == 0x00 &&
            addr->addr[5] == 0x00) {
                return true;
        }

        return false;
}

static inline bool net_eth_is_addr_unspecified(struct net_eth_addr *addr)
{
        if (addr->addr[0] == 0x00 &&
            addr->addr[1] == 0x00 &&
            addr->addr[2] == 0x00 &&
            addr->addr[3] == 0x00 &&
            addr->addr[4] == 0x00 &&
            addr->addr[5] == 0x00) {
                return true;
        }

        return false;
}

static inline bool net_eth_is_addr_multicast(struct net_eth_addr *addr)
{
        return addr->addr[0] & 0x01;
}

static inline bool net_eth_is_addr_unicast(struct net_eth_addr *addr)
{
        return !net_eth_is_addr_unspecified(addr) && !net_eth_is_addr_multicast(addr);
}

static inline bool net_eth_is_addr_valid(struct net_eth_addr *addr)
{
        return !net_eth_is_addr_unspecified(addr) && !net_eth_is_addr_multicast(addr);
}

static inline bool net_eth_is_addr_lldp_multicast(struct net_eth_addr *addr)
{
        if (addr->addr[0] == 0x01 &&
            addr->addr[1] == 0x80 &&
            addr->addr[2] == 0xc2 &&
            addr->addr[3] == 0x00 &&
            addr->addr[4] == 0x00 &&
            addr->addr[5] == 0x0e) {
                return true;
        }

        return false;
}

static inline bool net_eth_is_addr_ptp_multicast(struct net_eth_addr *addr)
{
        if (addr->addr[0] == 0x01 &&
            addr->addr[1] == 0x1b &&
            addr->addr[2] == 0x19 &&
            addr->addr[3] == 0x00 &&
            addr->addr[4] == 0x00 &&
            addr->addr[5] == 0x00) {
                return true;
        }

        return false;
}

const struct net_eth_addr *net_eth_broadcast_addr(void);

void net_eth_ipv4_mcast_to_mac_addr(const struct net_in_addr *ipv4_addr,
                                    struct net_eth_addr *mac_addr);

void net_eth_ipv6_mcast_to_mac_addr(const struct net_in6_addr *ipv6_addr,
                                    struct net_eth_addr *mac_addr);

typedef void (*net_eth_mcast_addr_cb_t)(struct net_if *iface,
                                        const struct net_eth_mcast_addr *addr,
                                        void *user_data);

#if defined(NET_ETH_MCAST_FILTER_SUPPORTED) || defined(__DOXYGEN__)

int net_eth_mcast_addr_add(struct net_if *iface,
                           const struct net_eth_addr *addr);

int net_eth_mcast_addr_rm(struct net_if *iface,
                          const struct net_eth_addr *addr);

void net_eth_mcast_addr_foreach(struct net_if *iface,
                                net_eth_mcast_addr_cb_t cb,
                                void *user_data);


int net_eth_mcast_ip_addr_update(struct net_if *iface, const struct net_addr *addr, bool add);


#else /* NET_ETH_MCAST_FILTER_SUPPORTED */

static inline int net_eth_mcast_addr_add(struct net_if *iface,
                                         const struct net_eth_addr *addr)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(addr);

        return -ENOTSUP;
}

static inline int net_eth_mcast_addr_rm(struct net_if *iface,
                                        const struct net_eth_addr *addr)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(addr);

        return -ENOTSUP;
}

static inline void net_eth_mcast_addr_foreach(struct net_if *iface,
                                              net_eth_mcast_addr_cb_t cb,
                                              void *user_data)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(cb);
        ARG_UNUSED(user_data);
}

static inline int net_eth_mcast_ip_addr_update(struct net_if *iface __unused,
                                               const struct net_addr *addr __unused,
                                               bool add __unused)
{
        return -ENOTSUP;
}

#endif /* NET_ETH_MCAST_FILTER_SUPPORTED */

static inline
enum ethernet_hw_caps net_eth_get_hw_capabilities(struct net_if *iface)
{
        const struct device *dev = net_if_get_device(iface);
        const struct ethernet_api *api;
        enum ethernet_hw_caps caps = (enum ethernet_hw_caps)0;
#if defined(CONFIG_NET_DSA)
        struct ethernet_context *eth_ctx = net_if_l2_data(iface);

        NET_ASSERT(eth_ctx != NULL);

        if (eth_ctx->dsa_port == DSA_CONDUIT_PORT) {
                caps = ETHERNET_DSA_CONDUIT_PORT;
        } else if (eth_ctx->dsa_port == DSA_USER_PORT) {
                caps = ETHERNET_DSA_USER_PORT;
        }
#endif
        NET_ASSERT(dev != NULL);

        api = (const struct ethernet_api *)dev->api;
        if (api == NULL || api->get_capabilities == NULL) {
                return caps;
        }

        return (enum ethernet_hw_caps)(caps | api->get_capabilities(dev, iface));
}

static inline
int net_eth_get_hw_config(struct net_if *iface, enum ethernet_config_type type,
                         struct ethernet_config *config)
{
        const struct device *dev = net_if_get_device(iface);
        const struct ethernet_api *eth;

        NET_ASSERT(dev != NULL);

        eth = (const struct ethernet_api *)dev->api;

        NET_ASSERT(eth != NULL);

        if (!eth->get_config) {
                return -ENOTSUP;
        }

        return eth->get_config(dev, iface, type, config);
}


#if defined(CONFIG_NET_VLAN) && NET_VLAN_MAX_COUNT > 0
int net_eth_vlan_enable(struct net_if *iface, uint16_t tag);
#else
static inline int net_eth_vlan_enable(struct net_if *iface, uint16_t tag)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(tag);

        return -EINVAL;
}
#endif

#if defined(CONFIG_NET_VLAN) && NET_VLAN_MAX_COUNT > 0
int net_eth_vlan_disable(struct net_if *iface, uint16_t tag);
#else
static inline int net_eth_vlan_disable(struct net_if *iface, uint16_t tag)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(tag);

        return -EINVAL;
}
#endif

#if defined(CONFIG_NET_VLAN) && NET_VLAN_MAX_COUNT > 0
uint16_t net_eth_get_vlan_tag(struct net_if *iface);
#else
static inline uint16_t net_eth_get_vlan_tag(struct net_if *iface)
{
        ARG_UNUSED(iface);

        return NET_VLAN_TAG_UNSPEC;
}
#endif

#if defined(CONFIG_NET_VLAN) && NET_VLAN_MAX_COUNT > 0
struct net_if *net_eth_get_vlan_iface(struct net_if *iface, uint16_t tag);
#else
static inline
struct net_if *net_eth_get_vlan_iface(struct net_if *iface, uint16_t tag)
{
        /* Special case for priority tagged frames, without vlan ifaces being present */
        if (IS_ENABLED(CONFIG_NET_VLAN) && (tag == NET_VLAN_TAG_PRIORITY)) {
                return iface;
        }

        return NULL;
}
#endif

static inline struct net_if *net_eth_get_vlan_main(struct net_if *iface)
{
        return net_virtual_get_iface(iface);
}

#if defined(CONFIG_NET_VLAN) && NET_VLAN_MAX_COUNT > 0
bool net_eth_is_vlan_enabled(struct ethernet_context *ctx,
                             struct net_if *iface);
#else
static inline bool net_eth_is_vlan_enabled(struct ethernet_context *ctx,
                                           struct net_if *iface)
{
        ARG_UNUSED(ctx);
        ARG_UNUSED(iface);

        return IS_ENABLED(CONFIG_NET_VLAN);
}
#endif

#if defined(CONFIG_NET_VLAN) && NET_VLAN_MAX_COUNT > 0
bool net_eth_get_vlan_status(struct net_if *iface);
#else
static inline bool net_eth_get_vlan_status(struct net_if *iface)
{
        ARG_UNUSED(iface);

        return false;
}
#endif

#if defined(CONFIG_NET_VLAN) && NET_VLAN_MAX_COUNT > 0
bool net_eth_is_vlan_interface(struct net_if *iface);
#else
static inline bool net_eth_is_vlan_interface(struct net_if *iface)
{
        ARG_UNUSED(iface);

        return false;
}
#endif


#if !defined(CONFIG_ETH_DRIVER_RAW_MODE)

#define Z_ETH_NET_DEVICE_INIT_INSTANCE(node_id, dev_id, name, instance, \
                                       init_fn, pm, data, config, prio, \
                                       api, mtu)                        \
        Z_NET_DEVICE_INIT_INSTANCE(node_id, dev_id, name, instance,     \
                                   init_fn, pm, data, config, prio,     \
                                   api, ETHERNET_L2,                    \
                                   NET_L2_GET_CTX_TYPE(ETHERNET_L2), mtu)

#else /* CONFIG_ETH_DRIVER_RAW_MODE */

#define Z_ETH_NET_DEVICE_INIT_INSTANCE(node_id, dev_id, name, instance, \
                                       init_fn, pm, data, config, prio, \
                                       api, mtu)                        \
        Z_DEVICE_STATE_DEFINE(dev_id);                                  \
        Z_DEVICE_DEFINE(node_id, dev_id, name, init_fn, NULL,           \
                        Z_DEVICE_DT_FLAGS(node_id), pm, data,           \
                        config, POST_KERNEL, prio, api,                 \
                        &Z_DEVICE_STATE_NAME(dev_id));

#endif /* CONFIG_ETH_DRIVER_RAW_MODE */

#define Z_ETH_NET_DEVICE_INIT(node_id, dev_id, name, init_fn, pm, data, \
                              config, prio, api, mtu)                   \
        Z_ETH_NET_DEVICE_INIT_INSTANCE(node_id, dev_id, name, 0,        \
                                       init_fn, pm, data, config, prio, \
                                       api, mtu)


#define ETH_NET_DEVICE_INIT(dev_id, name, init_fn, pm, data, config,    \
                            prio, api, mtu)                             \
        Z_ETH_NET_DEVICE_INIT(DT_INVALID_NODE, dev_id, name, init_fn,   \
                              pm, data, config, prio, api, mtu)

#define ETH_NET_DEVICE_INIT_INSTANCE(dev_id, name, instance, init_fn,   \
                                     pm, data, config, prio, api, mtu)  \
        Z_ETH_NET_DEVICE_INIT_INSTANCE(DT_INVALID_NODE, dev_id, name,   \
                                       instance, init_fn, pm, data,     \
                                       config, prio, api, mtu)

#define ETH_NET_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config,    \
                                 prio, api, mtu)                        \
        Z_ETH_NET_DEVICE_INIT(node_id, Z_DEVICE_DT_DEV_ID(node_id),     \
                              DEVICE_DT_NAME(node_id), init_fn, pm,     \
                              data, config, prio, api, mtu)

#define ETH_NET_DEVICE_DT_INST_DEFINE(inst, ...) \
        ETH_NET_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)

#define ETH_NET_L3_REGISTER(name, ptype, handler) \
        NET_L3_REGISTER(&NET_L2_GET_NAME(ETHERNET), name, ptype, handler)

enum net_eth_mac_type {
        NET_ETH_MAC_DEFAULT = 0,
        NET_ETH_MAC_RANDOM,
        NET_ETH_MAC_NVMEM,
        NET_ETH_MAC_STATIC,
};

struct net_eth_mac_config {
        enum net_eth_mac_type type;
        uint8_t addr[NET_ETH_ADDR_LEN];
        uint8_t addr_len;
#if defined(CONFIG_NVMEM) || defined(__DOXYGEN__)
        struct nvmem_cell cell;
#endif
};

static inline int net_eth_mac_load(const struct net_eth_mac_config *cfg, uint8_t *mac_addr)
{
        if (cfg == NULL || cfg->type == NET_ETH_MAC_DEFAULT) {
                return -ENODATA;
        }

        /* Copy the static part */
        memcpy(mac_addr, cfg->addr, cfg->addr_len);

        if (cfg->type == NET_ETH_MAC_RANDOM) {
                sys_rand_get(&mac_addr[cfg->addr_len], NET_ETH_ADDR_LEN - cfg->addr_len);

                /* Clear group bit, multicast (I/G) */
                mac_addr[0] &= ~0x01;
                /* Set MAC address locally administered, unicast (LAA) */
                mac_addr[0] |= 0x02;

                return 0;
        }

#if defined(CONFIG_NVMEM)
        if (cfg->type == NET_ETH_MAC_NVMEM) {
                return nvmem_cell_read(&cfg->cell, &mac_addr[cfg->addr_len], 0,
                                       NET_ETH_ADDR_LEN - cfg->addr_len);
        }
#endif

        if (cfg->type == NET_ETH_MAC_STATIC) {
                return 0;
        }

        return -ENODATA;
}


#if defined(CONFIG_NVMEM) || defined(__DOXYGEN__)
#define Z_NET_ETH_MAC_DEV_CONFIG_INIT_CELL(node_id)                                                \
        .cell = NVMEM_CELL_GET_BY_NAME_OR(node_id, mac_address, {0}),
#else
#define Z_NET_ETH_MAC_DEV_CONFIG_INIT_CELL(node_id)
#endif

#define Z_NET_ETH_MAC_DT_CONFIG_INIT_RANDOM(node_id)                                               \
        {                                                                                          \
                .type = NET_ETH_MAC_RANDOM,                                                        \
                .addr = DT_PROP_OR(node_id, zephyr_mac_address_prefix, {0}),                       \
                .addr_len = DT_PROP_LEN_OR(node_id, zephyr_mac_address_prefix, 0),                 \
        }

#define Z_NET_ETH_MAC_DT_CONFIG_INIT_NVMEM(node_id)                                                \
        {                                                                                          \
                .type = NET_ETH_MAC_NVMEM,                                                         \
                .addr = DT_PROP_OR(node_id, zephyr_mac_address_prefix, {0}),                       \
                .addr_len = DT_PROP_LEN_OR(node_id, zephyr_mac_address_prefix, 0),                 \
                Z_NET_ETH_MAC_DEV_CONFIG_INIT_CELL(node_id)                                        \
        }

#define Z_NET_ETH_MAC_DT_CONFIG_INIT_STATIC(node_id)                                               \
        {                                                                                          \
                .type = NET_ETH_MAC_STATIC,                                                        \
                .addr = DT_PROP(node_id, local_mac_address),                                       \
                .addr_len = DT_PROP_LEN(node_id, local_mac_address),                               \
        }

#define Z_NET_ETH_MAC_DT_CONFIG_INIT_DEFAULT(node_id)                                              \
        {                                                                                          \
                .type = NET_ETH_MAC_DEFAULT,                                                       \
        }


#define NET_ETH_MAC_DT_CONFIG_INIT(node_id)                                                        \
        COND_CASE_1(DT_PROP(node_id, zephyr_random_mac_address),                                   \
                    (Z_NET_ETH_MAC_DT_CONFIG_INIT_RANDOM(node_id)),                                \
                    DT_NVMEM_CELLS_HAS_NAME(node_id, mac_address),                                 \
                    (Z_NET_ETH_MAC_DT_CONFIG_INIT_NVMEM(node_id)),                                 \
                    DT_NODE_HAS_PROP(node_id, local_mac_address),                                  \
                    (Z_NET_ETH_MAC_DT_CONFIG_INIT_STATIC(node_id)),                                \
                    (Z_NET_ETH_MAC_DT_CONFIG_INIT_DEFAULT(node_id)))

#define NET_ETH_MAC_DT_INST_CONFIG_INIT(inst)                                                      \
        NET_ETH_MAC_DT_CONFIG_INIT(DT_DRV_INST(inst))

void net_eth_carrier_set(struct net_if *iface, bool carrier_up);

static inline void net_eth_carrier_on(struct net_if *iface)
{
        net_eth_carrier_set(iface, true);
}

static inline void net_eth_carrier_off(struct net_if *iface)
{
        net_eth_carrier_set(iface, false);
}

int net_eth_promisc_mode(struct net_if *iface, bool enable);

int net_eth_txinjection_mode(struct net_if *iface, bool enable);

int net_eth_mac_filter(struct net_if *iface, struct net_eth_addr *mac,
                       enum ethernet_filter_type type, bool enable);

const struct device *net_eth_get_phy(struct net_if *iface);

#if defined(CONFIG_PTP_CLOCK)
const struct device *net_eth_get_ptp_clock(struct net_if *iface);
#else
static inline const struct device *net_eth_get_ptp_clock(struct net_if *iface)
{
        ARG_UNUSED(iface);

        return NULL;
}
#endif

__syscall const struct device *net_eth_get_ptp_clock_by_index(int index);

static inline bool net_eth_type_is_wifi(struct net_if *iface)
{
        const struct ethernet_context *ctx = (struct ethernet_context *)
                net_if_l2_data(iface);

        NET_ASSERT(ctx != NULL);

        return ctx->eth_if_type == L2_ETH_IF_TYPE_WIFI;
}

static inline bool net_eth_type_is_ethernet(struct net_if *iface)
{
        const struct ethernet_context *ctx = (struct ethernet_context *)net_if_l2_data(iface);

        NET_ASSERT(ctx != NULL);

        return ctx->eth_if_type == L2_ETH_IF_TYPE_ETHERNET;
}

static inline void net_eth_set_if_type_wifi(struct net_if *iface)
{
        struct ethernet_context *ctx = (struct ethernet_context *)net_if_l2_data(iface);

        NET_ASSERT(ctx != NULL);

        ctx->eth_if_type = L2_ETH_IF_TYPE_WIFI;
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/ethernet.h>

#endif /* ZEPHYR_INCLUDE_NET_ETHERNET_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 59 行

关闭 clang-format 自动排版（clang-format off）。

### 注释 3：原第 60 行

保持排序区域的起始标记：`zephyr-keep-sorted-start`。

### 注释 4：原第 61 行

来自 `linux/if_ether.h`。

### 注释 5：原第 63 行

控制器局域网（Controller Area Network，CAN）。

### 注释 6：原第 64 行

灵活数据速率 CAN（CAN Flexible Data Rate，CAN FD）。

### 注释 7：原第 67 行

高级数据链路控制（HDLC）帧，例如 PPP 使用的帧。

### 注释 8：原第 68 行

来自 `linux/if_ether.h`：IEEE 802.15.4 帧（Frame）。

### 注释 9：原第 74 行

时间敏感网络（Time-Sensitive Networking，TSN）的 IEEE 1722 数据包。

### 注释 10：原第 76 行

保持排序区域的结束标记：`zephyr-keep-sorted-stop`。

### 注释 11：原第 77 行

开启 clang-format 自动排版（clang-format on）。

### 注释 12：原第 79 行

自动保持排序的起始标记：`zephyr-keep-sorted-start re(^#define)`。

### 注释 13：原第 116 行

保持排序区域的结束标记：`zephyr-keep-sorted-stop`。

### 注释 14：原第 342 行

部分抢占（Preemption）设置来自 Qbr 规范。

### 注释 15：原第 439 行

单个接口可跟踪的二层多播地址（L2 Multicast Addresses）数量。构建系统汇总各子系统请求的数量，并在此提供结果。Kconfig 值只作为下限；在 Zephyr 构建之外编译该头文件时，也使用该值。

### 注释 16：原第 448 行

只有当 IP 层、数据包套接字（Packet Socket）或系统其他部分加入相应组时，才跟踪二层多播地址（L2 Multicast Addresses）。

### 注释 17：原第 606 行

条件编译配置（Configuration）标记：`CONFIG_NET_VLAN`。

### 注释 18：原第 611 行

条件编译配置（Configuration）标记：`CONFIG_PTP_CLOCK`。

### 注释 19：原第 622 行

确保以太网 API 结构体（Ethernet API Struct）中的网络接口 API 正确设置，且位于第一个成员。

### 注释 20：原第 748 行

将虚拟局域网（VLAN）放在独立头文件中，因为某些设备接口可能不支持 VLAN。

### 注释 21：原第 755 行

标签协议标识（Tag Protocol ID）。

### 注释 22：原第 756 行

标签控制信息（Tag Control Information）。

### 注释 23：原第 1015 行

`NET_ETH_MCAST_FILTER_SUPPORTED` 条件标记，表示支持以太网多播过滤（Multicast Filter）。

### 注释 24：原第 1051 行

`NET_ETH_MCAST_FILTER_SUPPORTED` 条件标记，表示支持以太网多播过滤（Multicast Filter）。

### 注释 25：原第 1194 行

不存在 VLAN 接口时，优先级标记帧（Priority Tagged Frames）的特殊情况。

### 注释 26：原第 1293 行

条件编译配置（Configuration）标记：`CONFIG_ETH_DRIVER_RAW_MODE`。

### 注释 27：原第 1304 行

条件编译配置（Configuration）标记：`CONFIG_ETH_DRIVER_RAW_MODE`。

### 注释 28：原第 1465 行

复制静态部分（Static Part）。

### 注释 29：原第 1471 行

清除组地址位（Group Bit），即多播的 I/G 位。

### 注释 30：原第 1473 行

将 MAC 地址设为本地管理的单播地址（Locally Administered Address，LAA）。

### 注释 31：原第 1731 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_ETHERNET_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [zephyr/net/lldp.h](https://docs.zephyrproject.org/latest/doxygen/html/lldp_8h.html)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/ethernet_vlan.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__vlan_8h.html)
- [zephyr/net/ptp_time.h](../api_file_runtime_reference/P052_zephyr__net__ptp_time.h_文件参考.md)
- [zephyr/net/virtual.h](https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h.html)
- [zephyr/random/random.h](../data_utilities/P008_随机数头文件.md)
- [zephyr/nvmem.h](../storage/P020_NVMEM公共头文件.md)
- [net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [addr](../network_core_model_reference/P059_net_eth_addr_结构体.md#af370baeb1f10475331db8628c3c9efbe)
- [NET_ETH_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga399425f810c00bcf9babec019bc2ff12)
- [ethernet_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9162ff11d626813fc840df0b67820ac5)
- [ETHERNET_HW_TX_CHKSUM_OFFLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [ETHERNET_HW_RX_CHKSUM_OFFLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33)
- [ETHERNET_HW_VLAN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95)
- [ETHERNET_LINK_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a4508489dc8a67ef908757a9e2338babb)
- [ETHERNET_LINK_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a2c59d7d5a1d5eff15976806d237960c1)
- [ETHERNET_LINK_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a55e8d0ee975acc9eabf5096d1b926f6b)
- [ETHERNET_LINK_2500BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5afe48cf59ca4d1db42e768ca272159d55)
- [ETHERNET_LINK_5000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a9ab79aee30b73747fceff86fd3b967f9)
- [ETHERNET_QAV](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42)
- [ETHERNET_PROMISC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d)
- [ETHERNET_PRIORITY_QUEUES](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475)
- [ETHERNET_HW_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe)
- [ETHERNET_LLDP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2)
- [ETHERNET_HW_VLAN_TAG_STRIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5)
- [ETHERNET_DSA_USER_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a12991c85e1a7405bd145b3fff8aeecf1)
- [ETHERNET_DSA_CONDUIT_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a2eeaa2befc2d7a38f0318addef88f072)
- [ETHERNET_QBV](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85)
- [ETHERNET_QBU](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08)
- [ETHERNET_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2)
- [ETHERNET_TXINJECTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b)
- [ethernet_qav_param](../network_service_model_reference/P010_ethernet_qav_param_结构体.md)
- [queue_id](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a4e2d2967669b758422c166140af0c1ba)
- [type](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a38861d9f790a61aa88801cb1373077a8)
- [enabled](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a031d3896b14eb8b32c3c050738421b85)
- [delta_bandwidth](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a6fde906da905c0598aaa2056c330b6f4)
- [idle_slope](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a6d43b199549cade0a07dc10adac85bff)
- [oper_idle_slope](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a0691f10a338d3c49a58d94a1adced477)
- [traffic_class](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a4a795e4a0c7d5bcbe8212d79f772dc6f)
- [ethernet_qbv_param](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md)
- [port_id](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a037492458f47905b894a2269ff7365cd)
- [type](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a2184250d397bd749764adc52ec3a1621)
- [state](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a36702c57bea42c37c1341e144ced4f7d)
- [enabled](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a0742dbe52f01addbb319e2fcb354d064)
- [gate_status](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a44b6ce52faeae761c5ebe49fad5338cd)
- [operation](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a8471f7eb20a72bb16fe7abb0b2bb24f7)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [time_interval](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#aa6b2be0014988752e326bdc1fe6ef161)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [row](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a2c256aa3f65dfa75434752903daa809c)
- [gate_control](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a216046de6134584ae05b53609d368bb9)
- [gate_control_list_len](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#afc0c26fcdeee1a921a2f549de4d1c33e)
- [net_ptp_extended_time](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md)
- [base_time](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a53646a44e8b0e1f6588c357d49d97693)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [cycle_time](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#ad07589ae6802a9c3c4c3f809427129be)
- [extension_time](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a76220e58aa31ae6cfd92268277716c7a)
- [ethernet_qbu_param](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md)
- [port_id](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#ae6d61f0c9d2f2e56eb494db953a5e846)
- [type](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#a4a8a3d26a12a06a787ae6b35ea40c37a)
- [hold_advance](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#a8ffde09a540817b7a68c7180c327196f)
- [release_advance](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#a3f62d0462376225c8609c7e26ebd314b)
- [frame_preempt_statuses](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#a3f5dfd9cfbc1ec86896eaf517bdc5c88)
- [enabled](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#a9717dd68adde62a454593d72fdbc43a5)
- [link_partner_status](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#ad8c92a7f7b4aa124adaa62dd4e65b5ca)
- [additional_fragment_size](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#afb455507b29d84de42638e47ecacadeb)
- [ethernet_if_types](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga139cc696837611a522b289f2ea7bf6fc)
- [L2_ETH_IF_TYPE_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530)
- [L2_ETH_IF_TYPE_WIFI](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671)
- [ethernet_filter](../network_service_model_reference/P008_ethernet_filter_结构体.md)
- [type](../network_service_model_reference/P008_ethernet_filter_结构体.md#aec00b1ecd6af658a5164d375bccdaa10)
- [mac_address](../network_service_model_reference/P008_ethernet_filter_结构体.md#aaacda9b89d6b21934654e0f2b19624e0)
- [set](../network_service_model_reference/P008_ethernet_filter_结构体.md#ad83053c859c65e0c0432fe3f59671335)
- [net_eth_mcast_addr](../network_core_model_reference/P061_net_eth_mcast_addr_结构体.md)
- [addr](../network_core_model_reference/P061_net_eth_mcast_addr_结构体.md#a5c7f1a2351a493681525a5c610389e15)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [atomic_ref](../network_core_model_reference/P061_net_eth_mcast_addr_结构体.md#af8dec139bae61ede5a2233ab0f3c66a4)
- [is_used](../network_core_model_reference/P061_net_eth_mcast_addr_结构体.md#ab8a4a73276b5236befb1ac34a379f689)
- [ethernet_txtime_param](../network_service_model_reference/P013_ethernet_txtime_param_结构体.md)
- [type](../network_service_model_reference/P013_ethernet_txtime_param_结构体.md#ab4a709e6907e76f9cf23c085f5be5d99)
- [queue_id](../network_service_model_reference/P013_ethernet_txtime_param_结构体.md#aa4a46b7153b2a69ca0134f4e10bc7165)
- [enable_txtime](../network_service_model_reference/P013_ethernet_txtime_param_结构体.md#a74b1e05cf0fac8aa435ba966e110ae27)
- [ethernet_checksum_support](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gabf86b7f09a9d041eea25357cd7a85ede)
- [ETHERNET_CHECKSUM_SUPPORT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea90314c44dca3c123d1a0bd70f108524d)
- [ETHERNET_CHECKSUM_SUPPORT_IPV4_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea6485d2abcd3dae6786022aa286234ed4)
- [ETHERNET_CHECKSUM_SUPPORT_IPV4_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea5671ade139cb0cd28d02e3215337acb9)
- [ETHERNET_CHECKSUM_SUPPORT_IPV6_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea557127c3bc97969fe57fcd8ac55567b5)
- [ETHERNET_CHECKSUM_SUPPORT_IPV6_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edeac64b392a0591cfe7aa5564a476fe20be)
- [ETHERNET_CHECKSUM_SUPPORT_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea3346f0e3d0b350c7fe663cfe389c1e02)
- [ETHERNET_CHECKSUM_SUPPORT_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea03e31130ecef7ac032bceed6f3091af8)
- [ethernet_stats_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gabfab900bfd7a9078e7ac2fd6aed9ce83)
- [ETHERNET_STATS_TYPE_COMMON](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabfab900bfd7a9078e7ac2fd6aed9ce83ad41e45f16877f28b44ec23fadb35d355)
- [ETHERNET_STATS_TYPE_VENDOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabfab900bfd7a9078e7ac2fd6aed9ce83a3a094b0237833d4523e04d7b6bb5fbab)
- [ETHERNET_STATS_TYPE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabfab900bfd7a9078e7ac2fd6aed9ce83a6bb1bfaf79f232101bc91ab02f54e4a7)
- [ethernet_api](../network_service_model_reference/P007_ethernet_api_结构体.md)
- [iface_api](../network_service_model_reference/P007_ethernet_api_结构体.md#a03dfbaed9cdf2bdd17b0bfd28d5a1056)
- [net_stats_eth](../network_core_model_reference/P128_net_stats_eth_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [start](../network_service_model_reference/P007_ethernet_api_结构体.md#a4ebe0d6cf70a7b5a1fff87c3ca6cb86e)
- [stop](../network_service_model_reference/P007_ethernet_api_结构体.md#a8dba118b707305e1b909a82f7742dd5e)
- [get_capabilities](../network_service_model_reference/P007_ethernet_api_结构体.md#ae7c0f0b5162f5fb6b1a49ce4b52249b0)
- [set_config](../network_service_model_reference/P007_ethernet_api_结构体.md#aa283f6f201f50ffdd976275374f5c828)
- [get_config](../network_service_model_reference/P007_ethernet_api_结构体.md#aa34137c564f84fdb3160a767348c4a58)
- [send](../network_service_model_reference/P007_ethernet_api_结构体.md#a8f6fd0d640b5a883c9f5150d9ed71241)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [ethernet_lldp](../network_service_model_reference/P009_ethernet_lldp_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../network_service_model_reference/P009_ethernet_lldp_结构体.md#a8cf37774b067ffbc4876e42c3b28e536)
- [net_lldpdu](../network_core_model_reference/P109_net_lldpdu_结构体.md)
- [lldpdu](../network_service_model_reference/P009_ethernet_lldp_结构体.md#aede4281b7f53be43f524d47bb2c606d1)
- [optional_du](../network_service_model_reference/P009_ethernet_lldp_结构体.md#a732d685dd27d2be5cb6b51175b8af70f)
- [optional_len](../network_service_model_reference/P009_ethernet_lldp_结构体.md#aabc1141bbc72a17e3884138c61bd5b0c)
- [k_timepoint_t](../timer_reference/P088_内核时间点类型.md)
- [tx_timer_timeout](../network_service_model_reference/P009_ethernet_lldp_结构体.md#a9a1123c7f9e799b6fe815c554df6f023)
- [net_lldp_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga1e9fb662d7cdfc3c4c68cfd0312987cf)
- [cb](../network_service_model_reference/P009_ethernet_lldp_结构体.md#a8d2452f182c52000bec93f4c53501220)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [net_l2_flags](../api_protocol_topic_reference/P040_网络二层抽象层（Network L2 Abstraction Layer）.md#gac7db0cc6c56d371a5803873074ec2516)
- [net_eth_is_addr_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga76a5fe39ce12478c666d87f4aec3d579)
- [net_eth_is_addr_all_zeroes](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga237aab2d07ffa84355981d02a4576ebe)
- [net_eth_is_addr_unspecified](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga89964de263029223d119f361fbd94bfd)
- [net_eth_is_addr_multicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga2755ecb84e9759c24302e33a56a1fc84)
- [net_eth_is_addr_unicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gae91a64c96e0a480927d92271092a158d)
- [net_eth_is_addr_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaf20472f9d60e5cddffed2919b3091030)
- [net_eth_is_addr_lldp_multicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaec6fb3c05792bdd30596137686f3251a)
- [net_eth_is_addr_ptp_multicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaeddfa5b3ff6e356393114b351f87fe43)
- [net_eth_broadcast_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gae66b24a847f8e0ad119c6c466331afd6)
- [net_eth_ipv4_mcast_to_mac_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga26984472437a98b00c31156f75558134)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_eth_ipv6_mcast_to_mac_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga93e498e99c155fc402a26a4429d044a0)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [net_eth_mcast_addr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga8d28addcef0038c4ba1daa84bc104143)
- [net_eth_mcast_addr_add](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga3e578035be797bbbafafa56dedaa8320)
- [net_eth_mcast_addr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga3cd2e9abc38bdd7eb0cb3932d96fd90e)
- [net_eth_mcast_addr_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga80adc03695a8fbb9dbc9dd3adec78c04)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [net_eth_get_hw_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gab0a3b4584bb6ce1d27b98b063fd3fcbd)
- [net_if_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)
- [net_if_l2_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3cad2d51fc9cc225619585e06e252db0)
- [api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [net_eth_get_hw_config](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga1246be489eb7130100bbaebbb73961c5)
- [net_eth_vlan_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [net_eth_vlan_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gab71a741cea5f645f4354a1abc9c95a50)
- [net_eth_get_vlan_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga6184c43a62e4af9958412f99991358c9)
- [NET_VLAN_TAG_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga665458f4b8f9c83ea0c1609207d3dd70)
- [net_eth_get_vlan_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gad9d890dcf7f5ee3659bf3bd5949faa4e)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [NET_VLAN_TAG_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gad1db5bb85a9744c8a8af8d2e1ebcfe69)
- [net_eth_get_vlan_main](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga010a95a0239a800131ac3d43dd54737f)
- [net_virtual_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__virtual.html#gabadf14eaa02978cde7030c99ddd3e279)
- [net_eth_is_vlan_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac536aa7154c4a8d194ec67efb68e275c)
- [net_eth_get_vlan_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga78aad58ec66710034cab8891ad638a2c)
- [net_eth_is_vlan_interface](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga8ca1eccc88a351241298d358ec28fdf5)
- [net_eth_mac_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac2433b0d82ef25373b2c0f994e248e92)
- [NET_ETH_MAC_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a8b1eb5edcd9f4953d56c9c10088d6bb5)
- [NET_ETH_MAC_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a3fad5d3a2578e83da31f3188add46b87)
- [NET_ETH_MAC_NVMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a730e86dd6e257352afb233fdcc189955)
- [NET_ETH_MAC_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a9e0096f69300cf30c1f78c33074c1bda)
- [net_eth_mac_config](../network_core_model_reference/P060_net_eth_mac_config_结构体.md)
- [type](../network_core_model_reference/P060_net_eth_mac_config_结构体.md#a0bac0f7f2af6cb03eeb90435799c7a2d)
- [addr](../network_core_model_reference/P060_net_eth_mac_config_结构体.md#a66656331031d3324e4fd0429028311f4)
- [addr_len](../network_core_model_reference/P060_net_eth_mac_config_结构体.md#aa9e496b7d76e2920381365275a405412)
- [nvmem_cell](../storage/P019_NVMEM数据单元结构.md)
- [cell](../network_core_model_reference/P060_net_eth_mac_config_结构体.md#a344aa4435360014cc6080dc0ba2d7dc3)
- [net_eth_mac_load](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa0ef2f94fd18da9c5ea675b46faac8d0)
- [ENODATA](../error_reference/P003_系统错误号公共接口.md#ga0030614bc864d1b24eaedd71585acc27)
- [memcpy](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md#af0f01bffcd16daa9143f6014d10a25ad)
- [sys_rand_get](../data_utilities/P007_随机数接口.md#gaf4f6792ac29c876d59ace1deae53bbd7)
- [nvmem_cell_read](../storage/P013_NVMEM接口参考.md#ga5db94733cecfd4b46dd87ee07128d58d)
- [net_eth_carrier_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa7f447129b5b8392640f849d18e9246b)
- [net_eth_carrier_on](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga62b33344256bbe228689e2cb541a0874)
- [net_eth_carrier_off](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga97ef5a8ad9157e2db12e9caf6faef5e7)
- [net_eth_promisc_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga42a3c6b04ef8827e3443c5aebe5541b9)
- [net_eth_txinjection_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gafbb76d53f9f80628d18d39368a28f984)
- [net_eth_mac_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga920bddac077675d544a21fb5650c945e)
- [net_eth_get_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga7225d06fbaa12d4668fa165d9e8f0845)
- [net_eth_get_ptp_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga37ff48434c56bbb24422dd805449b6f3)
- [net_eth_get_ptp_clock_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga84c37db5687c5264bec99976a1108ab6)
- [net_eth_type_is_wifi](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga6e603f6f74e6d7e988e7119a6df2ab4d)
- [net_eth_type_is_ethernet](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gae617887d42a288697f2507c5b0907909)
- [net_eth_set_if_type_wifi](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa64462598843dd9f6e731198498aea31)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [ethernet_vlan.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__vlan_8h.html)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [lldp.h](https://docs.zephyrproject.org/latest/doxygen/html/lldp_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [nvmem.h](../storage/P020_NVMEM公共头文件.md)
- [ptp_time.h](../api_file_runtime_reference/P052_zephyr__net__ptp_time.h_文件参考.md)
- [random.h](../data_utilities/P008_随机数头文件.md)
- [device::api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [ethernet_api::iface_api](../network_service_model_reference/P007_ethernet_api_结构体.md#a03dfbaed9cdf2bdd17b0bfd28d5a1056)
- [ethernet_api::start](../network_service_model_reference/P007_ethernet_api_结构体.md#a4ebe0d6cf70a7b5a1fff87c3ca6cb86e)
- [ethernet_api::stop](../network_service_model_reference/P007_ethernet_api_结构体.md#a8dba118b707305e1b909a82f7742dd5e)
- [ethernet_api::send](../network_service_model_reference/P007_ethernet_api_结构体.md#a8f6fd0d640b5a883c9f5150d9ed71241)
- [ethernet_api::set_config](../network_service_model_reference/P007_ethernet_api_结构体.md#aa283f6f201f50ffdd976275374f5c828)
- [ethernet_api::get_config](../network_service_model_reference/P007_ethernet_api_结构体.md#aa34137c564f84fdb3160a767348c4a58)
- [ethernet_api::get_capabilities](../network_service_model_reference/P007_ethernet_api_结构体.md#ae7c0f0b5162f5fb6b1a49ce4b52249b0)
- [ethernet_filter::mac_address](../network_service_model_reference/P008_ethernet_filter_结构体.md#aaacda9b89d6b21934654e0f2b19624e0)
- [ethernet_filter::set](../network_service_model_reference/P008_ethernet_filter_结构体.md#ad83053c859c65e0c0432fe3f59671335)
- [ethernet_filter::type](../network_service_model_reference/P008_ethernet_filter_结构体.md#aec00b1ecd6af658a5164d375bccdaa10)
- [ethernet_lldp::optional_du](../network_service_model_reference/P009_ethernet_lldp_结构体.md#a732d685dd27d2be5cb6b51175b8af70f)
- [ethernet_lldp::node](../network_service_model_reference/P009_ethernet_lldp_结构体.md#a8cf37774b067ffbc4876e42c3b28e536)
- [ethernet_lldp::cb](../network_service_model_reference/P009_ethernet_lldp_结构体.md#a8d2452f182c52000bec93f4c53501220)
- [ethernet_lldp::tx_timer_timeout](../network_service_model_reference/P009_ethernet_lldp_结构体.md#a9a1123c7f9e799b6fe815c554df6f023)
- [ethernet_lldp::optional_len](../network_service_model_reference/P009_ethernet_lldp_结构体.md#aabc1141bbc72a17e3884138c61bd5b0c)
- [ethernet_lldp::lldpdu](../network_service_model_reference/P009_ethernet_lldp_结构体.md#aede4281b7f53be43f524d47bb2c606d1)
- [ethernet_qav_param::enabled](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a031d3896b14eb8b32c3c050738421b85)
- [ethernet_qav_param::oper_idle_slope](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a0691f10a338d3c49a58d94a1adced477)
- [ethernet_qav_param::type](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a38861d9f790a61aa88801cb1373077a8)
- [ethernet_qav_param::traffic_class](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a4a795e4a0c7d5bcbe8212d79f772dc6f)
- [ethernet_qav_param::queue_id](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a4e2d2967669b758422c166140af0c1ba)
- [ethernet_qav_param::idle_slope](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a6d43b199549cade0a07dc10adac85bff)
- [ethernet_qav_param::delta_bandwidth](../network_service_model_reference/P010_ethernet_qav_param_结构体.md#a6fde906da905c0598aaa2056c330b6f4)
- [ethernet_qbu_param::frame_preempt_statuses](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#a3f5dfd9cfbc1ec86896eaf517bdc5c88)
- [ethernet_qbu_param::release_advance](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#a3f62d0462376225c8609c7e26ebd314b)
- [ethernet_qbu_param::type](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#a4a8a3d26a12a06a787ae6b35ea40c37a)
- [ethernet_qbu_param::hold_advance](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#a8ffde09a540817b7a68c7180c327196f)
- [ethernet_qbu_param::enabled](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#a9717dd68adde62a454593d72fdbc43a5)
- [ethernet_qbu_param::link_partner_status](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#ad8c92a7f7b4aa124adaa62dd4e65b5ca)
- [ethernet_qbu_param::port_id](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#ae6d61f0c9d2f2e56eb494db953a5e846)
- [ethernet_qbu_param::additional_fragment_size](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md#afb455507b29d84de42638e47ecacadeb)
- [ethernet_qbv_param::port_id](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a037492458f47905b894a2269ff7365cd)
- [ethernet_qbv_param::enabled](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a0742dbe52f01addbb319e2fcb354d064)
- [ethernet_qbv_param::gate_control](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a216046de6134584ae05b53609d368bb9)
- [ethernet_qbv_param::type](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a2184250d397bd749764adc52ec3a1621)
- [ethernet_qbv_param::row](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a2c256aa3f65dfa75434752903daa809c)
- [ethernet_qbv_param::state](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a36702c57bea42c37c1341e144ced4f7d)
- [ethernet_qbv_param::gate_status](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a44b6ce52faeae761c5ebe49fad5338cd)
- [ethernet_qbv_param::base_time](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a53646a44e8b0e1f6588c357d49d97693)
- [ethernet_qbv_param::extension_time](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a76220e58aa31ae6cfd92268277716c7a)
- [ethernet_qbv_param::operation](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#a8471f7eb20a72bb16fe7abb0b2bb24f7)
- [ethernet_qbv_param::time_interval](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#aa6b2be0014988752e326bdc1fe6ef161)
- [ethernet_qbv_param::cycle_time](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#ad07589ae6802a9c3c4c3f809427129be)
- [ethernet_qbv_param::gate_control_list_len](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md#afc0c26fcdeee1a921a2f549de4d1c33e)
- [ethernet_txtime_param::enable_txtime](../network_service_model_reference/P013_ethernet_txtime_param_结构体.md#a74b1e05cf0fac8aa435ba966e110ae27)
- [ethernet_txtime_param::queue_id](../network_service_model_reference/P013_ethernet_txtime_param_结构体.md#aa4a46b7153b2a69ca0134f4e10bc7165)
- [ethernet_txtime_param::type](../network_service_model_reference/P013_ethernet_txtime_param_结构体.md#ab4a709e6907e76f9cf23c085f5be5d99)
- [net_eth_addr::addr](../network_core_model_reference/P059_net_eth_addr_结构体.md#af370baeb1f10475331db8628c3c9efbe)
- [net_eth_mac_config::type](../network_core_model_reference/P060_net_eth_mac_config_结构体.md#a0bac0f7f2af6cb03eeb90435799c7a2d)
- [net_eth_mac_config::cell](../network_core_model_reference/P060_net_eth_mac_config_结构体.md#a344aa4435360014cc6080dc0ba2d7dc3)
- [net_eth_mac_config::addr](../network_core_model_reference/P060_net_eth_mac_config_结构体.md#a66656331031d3324e4fd0429028311f4)
- [net_eth_mac_config::addr_len](../network_core_model_reference/P060_net_eth_mac_config_结构体.md#aa9e496b7d76e2920381365275a405412)
- [net_eth_mcast_addr::addr](../network_core_model_reference/P061_net_eth_mcast_addr_结构体.md#a5c7f1a2351a493681525a5c610389e15)
- [net_eth_mcast_addr::is_used](../network_core_model_reference/P061_net_eth_mcast_addr_结构体.md#ab8a4a73276b5236befb1ac34a379f689)
- [net_eth_mcast_addr::atomic_ref](../network_core_model_reference/P061_net_eth_mcast_addr_结构体.md#af8dec139bae61ede5a2233ab0f3c66a4)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [virtual.h](https://docs.zephyrproject.org/latest/doxygen/html/virtual_8h.html)

---

[上一章](P002_esp32c61-gpio-sigmap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_imx_ccm_rev2.h_源码浏览.md)
