---
id: learning.zephyr-docs.api-source-socket-ethernet-reference.page-1
title: assigned_numbers.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_assigned\_numbers.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)。

## 1.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00037"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
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
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
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
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00304"></a>
<a id="l00306"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00312"></a>
<a id="l00314"></a>
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00320"></a>
<a id="l00322"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00372"></a>
<a id="l00374"></a>
<a id="l00376"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00390"></a>
<a id="l00392"></a>
<a id="l00394"></a>
<a id="l00396"></a>
<a id="l00398"></a>
<a id="l00400"></a>
<a id="l00402"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00408"></a>
<a id="l00410"></a>
<a id="l00412"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00420"></a>
<a id="l00422"></a>
<a id="l00424"></a>
<a id="l00426"></a>
<a id="l00428"></a>
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
<a id="l00454"></a>
<a id="l00456"></a>
<a id="l00458"></a>
<a id="l00460"></a>
<a id="l00462"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00468"></a>
<a id="l00470"></a>
<a id="l00472"></a>
<a id="l00474"></a>
<a id="l00476"></a>
<a id="l00478"></a>
<a id="l00480"></a>
<a id="l00482"></a>
<a id="l00484"></a>
<a id="l00486"></a>
<a id="l00488"></a>
<a id="l00490"></a>
<a id="l00492"></a>
<a id="l00494"></a>
<a id="l00496"></a>
<a id="l00498"></a>
<a id="l00500"></a>
<a id="l00502"></a>
<a id="l00504"></a>
<a id="l00506"></a>
<a id="l00508"></a>
<a id="l00510"></a>
<a id="l00512"></a>
<a id="l00514"></a>
<a id="l00516"></a>
<a id="l00518"></a>
<a id="l00520"></a>
<a id="l00522"></a>
<a id="l00524"></a>
<a id="l00526"></a>
<a id="l00528"></a>
<a id="l00530"></a>
<a id="l00532"></a>
<a id="l00534"></a>
<a id="l00536"></a>
<a id="l00538"></a>
<a id="l00540"></a>
<a id="l00542"></a>
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
<a id="l00590"></a>
<a id="l00592"></a>
<a id="l00594"></a>
<a id="l00596"></a>
<a id="l00598"></a>
<a id="l00600"></a>
<a id="l00602"></a>
<a id="l00604"></a>
<a id="l00606"></a>
<a id="l00608"></a>
<a id="l00610"></a>
<a id="l00612"></a>
<a id="l00614"></a>
<a id="l00616"></a>
<a id="l00618"></a>
<a id="l00620"></a>
<a id="l00622"></a>
<a id="l00624"></a>
<a id="l00626"></a>
<a id="l00628"></a>
<a id="l00630"></a>
<a id="l00632"></a>
<a id="l00634"></a>
<a id="l00636"></a>
<a id="l00638"></a>
<a id="l00640"></a>
<a id="l00642"></a>
<a id="l00644"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00649"></a>
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
<a id="l00708"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00720"></a>
<a id="l00727"></a>
<a id="l00733"></a>
<a id="l00735"></a>
<a id="l00737"></a>
<a id="l00739"></a>
<a id="l00741"></a>
<a id="l00743"></a>
<a id="l00745"></a>
<a id="l00747"></a>
<a id="l00749"></a>
<a id="l00751"></a>
<a id="l00753"></a>
<a id="l00755"></a>
<a id="l00757"></a>
<a id="l00759"></a>
<a id="l00761"></a>
<a id="l00763"></a>
<a id="l00765"></a>
<a id="l00767"></a>
<a id="l00769"></a>
<a id="l00771"></a>
<a id="l00775"></a>
<a id="l00781"></a>
<a id="l00783"></a>
<a id="l00785"></a>
<a id="l00787"></a>
<a id="l00789"></a>
<a id="l00791"></a>
<a id="l00793"></a>
<a id="l00795"></a>
<a id="l00797"></a>
<a id="l00799"></a>
<a id="l00801"></a>
<a id="l00803"></a>
<a id="l00805"></a>
<a id="l00807"></a>
<a id="l00809"></a>
<a id="l00811"></a>
<a id="l00813"></a>
<a id="l00815"></a>
<a id="l00817"></a>
<a id="l00819"></a>
<a id="l00821"></a>
<a id="l00823"></a>
<a id="l00825"></a>
<a id="l00827"></a>
<a id="l00829"></a>
<a id="l00831"></a>
<a id="l00833"></a>
<a id="l00835"></a>
<a id="l00837"></a>
<a id="l00839"></a>
<a id="l00841"></a>
<a id="l00843"></a>
<a id="l00845"></a>
<a id="l00847"></a>
<a id="l00849"></a>
<a id="l00851"></a>
<a id="l00853"></a>
<a id="l00855"></a>
<a id="l00857"></a>
<a id="l00859"></a>
<a id="l00861"></a>
<a id="l00863"></a>
<a id="l00865"></a>
<a id="l00867"></a>
<a id="l00869"></a>
<a id="l00871"></a>
<a id="l00873"></a>
<a id="l00875"></a>
<a id="l00877"></a>
<a id="l00879"></a>
<a id="l00881"></a>
<a id="l00883"></a>
<a id="l00887"></a>
<a id="l00893"></a>
<a id="l00895"></a>
<a id="l00899"></a>
<a id="l00905"></a>
<a id="l00907"></a>
<a id="l00909"></a>
<a id="l00911"></a>
<a id="l00915"></a>
<a id="l00917"></a>
<a id="l00924"></a>
<a id="foldopen00926"></a>
<a id="l00926"></a>
<a id="l00928"></a>
<a id="l00930"></a>
<a id="l00932"></a>
<a id="l00934"></a>
<a id="l00936"></a>
<a id="l00938"></a>
<a id="l00940"></a>
<a id="l00942"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="foldopen00954"></a>
<a id="l00954"></a>
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="foldopen00972"></a>
<a id="l00972"></a>
<a id="l00974"></a>
<a id="l00975"></a>
<a id="l00977"></a>
<a id="l00978"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="l00986"></a>
<a id="l00987"></a>
<a id="l00989"></a>
<a id="l00990"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="l00998"></a>
<a id="l00999"></a>
<a id="l01001"></a>
<a id="l01002"></a>
<a id="l01004"></a>
<a id="l01005"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="l01010"></a>
<a id="l01011"></a>
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
<a id="foldopen01024"></a>
<a id="l01024"></a>
<a id="l01026"></a>
<a id="l01027"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01032"></a>
<a id="l01033"></a>
<a id="l01034"></a>
<a id="l01041"></a>
<a id="l01042"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01051"></a>
<a id="foldopen01053"></a>
<a id="l01053"></a>
<a id="l01055"></a>
<a id="l01056"></a>
<a id="l01058"></a>
<a id="l01059"></a>
<a id="l01061"></a>
<a id="l01062"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01073"></a>
<a id="l01074"></a>
<a id="l01076"></a>
<a id="l01077"></a>
<a id="l01079"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01082"></a>
<a id="l01083"></a>
<a id="l01084"></a>
<a id="l01085"></a>
<a id="l01087"></a>
<a id="l01089"></a>
<a id="l01090"></a>
<a id="l01092"></a>
<a id="l01094"></a>
<a id="l01096"></a>
<a id="l01098"></a>
<a id="l01099"></a>
<a id="foldopen01106"></a>
<a id="l01106"></a>
<a id="l01108"></a>
<a id="l01109"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01114"></a>
<a id="l01115"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01120"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="foldopen01124"></a>
<a id="l01124"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="l01129"></a>
<a id="l01130"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01141"></a>
<a id="l01142"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01147"></a>
<a id="l01148"></a>
<a id="l01150"></a>
<a id="l01151"></a>
<a id="l01153"></a>
<a id="l01154"></a>
<a id="l01156"></a>
<a id="l01157"></a>
<a id="l01159"></a>
<a id="l01160"></a>
<a id="l01162"></a>
<a id="l01163"></a>
<a id="l01164"></a>
<a id="foldopen01166"></a>
<a id="l01166"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01173"></a>
<a id="foldopen01179"></a>
<a id="l01179"></a>
<a id="l01181"></a>
<a id="l01186"></a>
<a id="l01191"></a>
<a id="l01193"></a>
<a id="l01198"></a>
<a id="l01200"></a>
<a id="l01202"></a>
<a id="l01207"></a>
<a id="l01212"></a>
<a id="l01217"></a>
<a id="l01222"></a>
<a id="l01227"></a>
<a id="l01229"></a>
<a id="l01230"></a>
<a id="l01231"></a>
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
<a id="l01245"></a>
<a id="l01246"></a>
<a id="l01247"></a>
<a id="foldopen01254"></a>
<a id="l01254"></a>
<a id="l01256"></a>
<a id="l01258"></a>
<a id="l01260"></a>
<a id="l01262"></a>
<a id="l01264"></a>
<a id="l01266"></a>
<a id="l01268"></a>
<a id="l01270"></a>
<a id="l01272"></a>
<a id="l01274"></a>
<a id="l01276"></a>
<a id="l01278"></a>
<a id="l01280"></a>
<a id="l01282"></a>
<a id="l01284"></a>
<a id="l01286"></a>
<a id="l01287"></a>
<a id="l01288"></a>
<a id="foldopen01290"></a>
<a id="l01290"></a>
<a id="l01292"></a>
<a id="l01294"></a>
<a id="l01295"></a>
<a id="l01296"></a>
<a id="foldopen01298"></a>
<a id="l01298"></a>
<a id="l01300"></a>
<a id="l01301"></a>
<a id="l01302"></a>
<a id="foldopen01308"></a>
<a id="l01308"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01331"></a>
<a id="l01332"></a>
<a id="l01334"></a>
<a id="l01335"></a>
<a id="l01342"></a>
<a id="l01343"></a>
<a id="l01345"></a>
<a id="l01346"></a>
<a id="l01352"></a>
<a id="l01353"></a>
<a id="l01355"></a>
<a id="l01356"></a>
<a id="l01362"></a>
<a id="l01363"></a>
<a id="l01365"></a>
<a id="l01366"></a>
<a id="l01372"></a>
<a id="l01373"></a>
<a id="l01375"></a>
<a id="l01376"></a>
<a id="l01378"></a>
<a id="l01379"></a>
<a id="l01381"></a>
<a id="l01382"></a>
<a id="l01383"></a>
<a id="foldopen01389"></a>
<a id="l01389"></a>
<a id="l01391"></a>
<a id="l01393"></a>
<a id="l01395"></a>
<a id="l01397"></a>
<a id="l01399"></a>
<a id="l01401"></a>
<a id="l01403"></a>
<a id="l01405"></a>
<a id="l01407"></a>
<a id="l01409"></a>
<a id="l01411"></a>
<a id="l01413"></a>
<a id="l01415"></a>
<a id="l01417"></a>
<a id="l01419"></a>
<a id="l01421"></a>
<a id="l01423"></a>
<a id="l01425"></a>
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
<a id="l01448"></a>
<a id="l01449"></a>
<a id="foldopen01453"></a>
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
<a id="l01483"></a>
<a id="l01488"></a>
<a id="l01489"></a>
<a id="l01490"></a>
<a id="l01492"></a>
<a id="l01497"></a>
<a id="foldopen01498"></a>
<a id="l01498"></a>
<a id="l01499"></a>
<a id="l01500"></a>
<a id="l01501"></a>
<a id="foldopen01502"></a>
<a id="l01502"></a>
<a id="l01503"></a>
<a id="l01504"></a>
<a id="l01505"></a>
<a id="l01506"></a>
<a id="l01511"></a>
<a id="l01513"></a>
<a id="l01515"></a>
<a id="l01517"></a>
<a id="l01519"></a>
<a id="l01521"></a>
<a id="l01523"></a>
<a id="l01525"></a>
<a id="l01527"></a>
<a id="l01529"></a>
<a id="l01531"></a>
<a id="l01533"></a>
<a id="l01534"></a>
<a id="l01536"></a>
<a id="l01541"></a>
<a id="l01543"></a>
<a id="l01545"></a>
<a id="l01547"></a>
<a id="l01549"></a>
<a id="l01551"></a>
<a id="l01553"></a>
<a id="l01555"></a>
<a id="l01557"></a>
<a id="l01559"></a>
<a id="l01561"></a>
<a id="l01563"></a>
<a id="l01564"></a>
<a id="l01566"></a>
<a id="l01571"></a>
<a id="l01573"></a>
<a id="l01575"></a>
<a id="l01577"></a>
<a id="l01579"></a>
<a id="l01581"></a>
<a id="l01583"></a>
<a id="l01585"></a>
<a id="l01587"></a>
<a id="l01588"></a>
<a id="l01590"></a>
<a id="l01595"></a>
<a id="l01597"></a>
<a id="l01599"></a>
<a id="l01601"></a>
<a id="l01603"></a>
<a id="l01605"></a>
<a id="l01607"></a>
<a id="l01608"></a>
<a id="l01610"></a>
<a id="l01615"></a>
<a id="l01617"></a>
<a id="l01619"></a>
<a id="l01621"></a>
<a id="l01623"></a>
<a id="l01625"></a>
<a id="l01627"></a>
<a id="l01629"></a>
<a id="l01631"></a>
<a id="l01632"></a>
<a id="l01634"></a>
<a id="l01639"></a>
<a id="l01641"></a>
<a id="l01642"></a>
<a id="l01645"></a>
<a id="l01647"></a>
<a id="l01649"></a>
<a id="l01651"></a>
<a id="l01653"></a>
<a id="l01655"></a>
<a id="l01657"></a>
<a id="l01659"></a>
<a id="l01661"></a>
<a id="l01663"></a>
<a id="l01665"></a>
<a id="l01667"></a>
<a id="l01669"></a>
<a id="l01671"></a>
<a id="l01673"></a>
<a id="l01675"></a>
<a id="l01677"></a>
<a id="l01678"></a>
<a id="l01680"></a>
<a id="l01685"></a>
<a id="l01687"></a>
<a id="l01689"></a>
<a id="l01691"></a>
<a id="l01693"></a>
<a id="l01694"></a>
<a id="l01696"></a>
<a id="l01701"></a>
<a id="l01703"></a>
<a id="l01705"></a>
<a id="l01707"></a>
<a id="l01709"></a>
<a id="l01711"></a>
<a id="l01713"></a>
<a id="l01715"></a>
<a id="l01717"></a>
<a id="l01719"></a>
<a id="l01721"></a>
<a id="l01722"></a>
<a id="l01724"></a>
<a id="l01729"></a>
<a id="l01731"></a>
<a id="l01733"></a>
<a id="l01735"></a>
<a id="l01737"></a>
<a id="l01738"></a>
<a id="l01740"></a>
<a id="l01741"></a>
<a id="l01743"></a>
<a id="l01748"></a>
<a id="l01750"></a>
<a id="l01752"></a>
<a id="l01754"></a>
<a id="l01756"></a>
<a id="l01758"></a>
<a id="l01759"></a>
<a id="l01761"></a>
<a id="l01766"></a>
<a id="l01768"></a>
<a id="l01770"></a>
<a id="l01772"></a>
<a id="l01774"></a>
<a id="l01776"></a>
<a id="l01777"></a>
<a id="l01779"></a>
<a id="l01784"></a>
<a id="l01786"></a>
<a id="l01788"></a>
<a id="l01790"></a>
<a id="l01792"></a>
<a id="l01794"></a>
<a id="l01796"></a>
<a id="l01798"></a>
<a id="l01800"></a>
<a id="l01802"></a>
<a id="l01804"></a>
<a id="l01806"></a>
<a id="l01808"></a>
<a id="l01810"></a>
<a id="l01812"></a>
<a id="l01814"></a>
<a id="l01816"></a>
<a id="l01817"></a>
<a id="l01819"></a>
<a id="l01821"></a>
<a id="l01822"></a>
<a id="l01823"></a>
<a id="l01824"></a>
<a id="l01825"></a>
<a id="l01829"></a>
<a id="l01830"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga16d403ec4db7be997682331ad365ff5f"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga207fbf0fbca9b24cba02c7f1d184e7f5"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga4bf3f820b493361a9a3b393d0282420f"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga61230848c02098352320fe751332c4e8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga6d4aff1f93dc0b902e4b5d1355f15760"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga83701b5eadfcbc9b84dc0b1a85ebeb74"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga8e99fb678cc011bb8c9f6e1858bae0d7"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga9230ec4d7518bd243207ba2decb1a974"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gaafc1106d5d305874ee2f540c850ff5b4"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gab53d0dd62bceff97cf8eed7d8cf80354"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gae695b5d17359967703f2509db1671fa5"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gaf37e8e19f956afb3c3a413cbaa1a21f5"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gaf58823a56eb36cfd22e582ab1ea3d015"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gafb379ffa88388cc1397960155bbb2ab3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga207fbf0fbca9b24cba02c7f1d184e7f5ab1714206feaa04b3be586ddb33ed5285"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga4bf3f820b493361a9a3b393d0282420fa1ab62f67902936349103d33f1475a328"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga4bf3f820b493361a9a3b393d0282420fa1bd25e0325ebefc57bdac0968e84fd64"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga4bf3f820b493361a9a3b393d0282420fa231fe012027b8d279e325231d804ed29"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga4bf3f820b493361a9a3b393d0282420fa62dfe9fe5ac51927efef815b9ce6874e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga4bf3f820b493361a9a3b393d0282420fab74491db769e0ab918809ab244e2ad1c"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga4bf3f820b493361a9a3b393d0282420fac6789c1a3127b92c1d9c6a5ee6f02c8a"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga4bf3f820b493361a9a3b393d0282420fac6fad482035f2eab235dac4dffe77baa"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga4bf3f820b493361a9a3b393d0282420face445f78f84de0ef7c6d3ef23e3172b8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga4bf3f820b493361a9a3b393d0282420faf6494f280fa28f202ce28bb7bc66ee24"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a890d2723c8b23127ab4a1cb8b6b1118d"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="atoolchain_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2015-2025 Intel Corporation
 * Copyright (c) 2017-2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_ASSIGNED_NUMBERS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_ASSIGNED_NUMBERS_H_


#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif



#define BT_APPEARANCE_UNKNOWN                               0x0000
#define BT_APPEARANCE_GENERIC_PHONE                         0x0040
#define BT_APPEARANCE_GENERIC_COMPUTER                      0x0080
#define BT_APPEARANCE_COMPUTER_DESKTOP_WORKSTATION          0x0081
#define BT_APPEARANCE_COMPUTER_SERVER_CLASS                 0x0082
#define BT_APPEARANCE_COMPUTER_LAPTOP                       0x0083
#define BT_APPEARANCE_COMPUTER_HANDHELD_PCPDA               0x0084
#define BT_APPEARANCE_COMPUTER_PALMSIZE_PCPDA               0x0085
#define BT_APPEARANCE_COMPUTER_WEARABLE_COMPUTER            0x0086
#define BT_APPEARANCE_COMPUTER_TABLET                       0x0087
#define BT_APPEARANCE_COMPUTER_DOCKING_STATION              0x0088
#define BT_APPEARANCE_COMPUTER_ALL_IN_ONE                   0x0089
#define BT_APPEARANCE_COMPUTER_BLADE_SERVER                 0x008A
#define BT_APPEARANCE_COMPUTER_CONVERTIBLE                  0x008B
#define BT_APPEARANCE_COMPUTER_DETACHABLE                   0x008C
#define BT_APPEARANCE_COMPUTER_IOT_GATEWAY                  0x008D
#define BT_APPEARANCE_COMPUTER_MINI_PC                      0x008E
#define BT_APPEARANCE_COMPUTER_STICK_PC                     0x008F
#define BT_APPEARANCE_GENERIC_WATCH                         0x00C0
#define BT_APPEARANCE_SPORTS_WATCH                          0x00C1
#define BT_APPEARANCE_SMARTWATCH                            0x00C2
#define BT_APPEARANCE_GENERIC_CLOCK                         0x0100
#define BT_APPEARANCE_GENERIC_DISPLAY                       0x0140
#define BT_APPEARANCE_GENERIC_REMOTE                        0x0180
#define BT_APPEARANCE_GENERIC_EYEGLASSES                    0x01C0
#define BT_APPEARANCE_GENERIC_TAG                           0x0200
#define BT_APPEARANCE_GENERIC_KEYRING                       0x0240
#define BT_APPEARANCE_GENERIC_MEDIA_PLAYER                  0x0280
#define BT_APPEARANCE_GENERIC_BARCODE_SCANNER               0x02C0
#define BT_APPEARANCE_GENERIC_THERMOMETER                   0x0300
#define BT_APPEARANCE_THERMOMETER_EAR                       0x0301
#define BT_APPEARANCE_GENERIC_HEART_RATE                    0x0340
#define BT_APPEARANCE_HEART_RATE_BELT                       0x0341
#define BT_APPEARANCE_GENERIC_BLOOD_PRESSURE                0x0380
#define BT_APPEARANCE_BLOOD_PRESSURE_ARM                    0x0381
#define BT_APPEARANCE_BLOOD_PRESSURE_WRIST                  0x0382
#define BT_APPEARANCE_GENERIC_HID                           0x03C0
#define BT_APPEARANCE_HID_KEYBOARD                          0x03C1
#define BT_APPEARANCE_HID_MOUSE                             0x03C2
#define BT_APPEARANCE_HID_JOYSTICK                          0x03C3
#define BT_APPEARANCE_HID_GAMEPAD                           0x03C4
#define BT_APPEARANCE_HID_DIGITIZER_TABLET                  0x03C5
#define BT_APPEARANCE_HID_CARD_READER                       0x03C6
#define BT_APPEARANCE_HID_DIGITAL_PEN                       0x03C7
#define BT_APPEARANCE_HID_BARCODE_SCANNER                   0x03C8
#define BT_APPEARANCE_HID_TOUCHPAD                          0x03C9
#define BT_APPEARANCE_HID_PRESENTATION_REMOTE               0x03CA
#define BT_APPEARANCE_GENERIC_GLUCOSE                       0x0400
#define BT_APPEARANCE_GENERIC_WALKING                       0x0440
#define BT_APPEARANCE_WALKING_IN_SHOE                       0x0441
#define BT_APPEARANCE_WALKING_ON_SHOE                       0x0442
#define BT_APPEARANCE_WALKING_ON_HIP                        0x0443
#define BT_APPEARANCE_GENERIC_CYCLING                       0x0480
#define BT_APPEARANCE_CYCLING_COMPUTER                      0x0481
#define BT_APPEARANCE_CYCLING_SPEED                         0x0482
#define BT_APPEARANCE_CYCLING_CADENCE                       0x0483
#define BT_APPEARANCE_CYCLING_POWER                         0x0484
#define BT_APPEARANCE_CYCLING_SPEED_CADENCE                 0x0485
#define BT_APPEARANCE_GENERIC_CONTROL_DEVICE                0x04C0
#define BT_APPEARANCE_CONTROL_SWITCH                        0x04C1
#define BT_APPEARANCE_CONTROL_MULTI_SWITCH                  0x04C2
#define BT_APPEARANCE_CONTROL_BUTTON                        0x04C3
#define BT_APPEARANCE_CONTROL_SLIDER                        0x04C4
#define BT_APPEARANCE_CONTROL_ROTARY_SWITCH                 0x04C5
#define BT_APPEARANCE_CONTROL_TOUCH_PANEL                   0x04C6
#define BT_APPEARANCE_CONTROL_SINGLE_SWITCH                 0x04C7
#define BT_APPEARANCE_CONTROL_DOUBLE_SWITCH                 0x04C8
#define BT_APPEARANCE_CONTROL_TRIPLE_SWITCH                 0x04C9
#define BT_APPEARANCE_CONTROL_BATTERY_SWITCH                0x04CA
#define BT_APPEARANCE_CONTROL_ENERGY_HARVESTING_SWITCH      0x04CB
#define BT_APPEARANCE_CONTROL_PUSH_BUTTON                   0x04CC
#define BT_APPEARANCE_GENERIC_NETWORK_DEVICE                0x0500
#define BT_APPEARANCE_NETWORK_ACCESS_POINT                  0x0501
#define BT_APPEARANCE_NETWORK_MESH_DEVICE                   0x0502
#define BT_APPEARANCE_NETWORK_MESH_PROXY                    0x0503
#define BT_APPEARANCE_GENERIC_SENSOR                        0x0540
#define BT_APPEARANCE_SENSOR_MOTION                         0x0541
#define BT_APPEARANCE_SENSOR_AIR_QUALITY                    0x0542
#define BT_APPEARANCE_SENSOR_TEMPERATURE                    0x0543
#define BT_APPEARANCE_SENSOR_HUMIDITY                       0x0544
#define BT_APPEARANCE_SENSOR_LEAK                           0x0545
#define BT_APPEARANCE_SENSOR_SMOKE                          0x0546
#define BT_APPEARANCE_SENSOR_OCCUPANCY                      0x0547
#define BT_APPEARANCE_SENSOR_CONTACT                        0x0548
#define BT_APPEARANCE_SENSOR_CARBON_MONOXIDE                0x0549
#define BT_APPEARANCE_SENSOR_CARBON_DIOXIDE                 0x054A
#define BT_APPEARANCE_SENSOR_AMBIENT_LIGHT                  0x054B
#define BT_APPEARANCE_SENSOR_ENERGY                         0x054C
#define BT_APPEARANCE_SENSOR_COLOR_LIGHT                    0x054D
#define BT_APPEARANCE_SENSOR_RAIN                           0x054E
#define BT_APPEARANCE_SENSOR_FIRE                           0x054F
#define BT_APPEARANCE_SENSOR_WIND                           0x0550
#define BT_APPEARANCE_SENSOR_PROXIMITY                      0x0551
#define BT_APPEARANCE_SENSOR_MULTI                          0x0552
#define BT_APPEARANCE_SENSOR_FLUSH_MOUNTED                  0x0553
#define BT_APPEARANCE_SENSOR_CEILING_MOUNTED                0x0554
#define BT_APPEARANCE_SENSOR_WALL_MOUNTED                   0x0555
#define BT_APPEARANCE_MULTISENSOR                           0x0556
#define BT_APPEARANCE_SENSOR_ENERGY_METER                   0x0557
#define BT_APPEARANCE_SENSOR_FLAME_DETECTOR                 0x0558
#define BT_APPEARANCE_SENSOR_VEHICLE_TIRE_PRESSURE          0x0559
#define BT_APPEARANCE_GENERIC_LIGHT_FIXTURES                0x0580
#define BT_APPEARANCE_LIGHT_FIXTURES_WALL                   0x0581
#define BT_APPEARANCE_LIGHT_FIXTURES_CEILING                0x0582
#define BT_APPEARANCE_LIGHT_FIXTURES_FLOOR                  0x0583
#define BT_APPEARANCE_LIGHT_FIXTURES_CABINET                0x0584
#define BT_APPEARANCE_LIGHT_FIXTURES_DESK                   0x0585
#define BT_APPEARANCE_LIGHT_FIXTURES_TROFFER                0x0586
#define BT_APPEARANCE_LIGHT_FIXTURES_PENDANT                0x0587
#define BT_APPEARANCE_LIGHT_FIXTURES_IN_GROUND              0x0588
#define BT_APPEARANCE_LIGHT_FIXTURES_FLOOD                  0x0589
#define BT_APPEARANCE_LIGHT_FIXTURES_UNDERWATER             0x058A
#define BT_APPEARANCE_LIGHT_FIXTURES_BOLLARD_WITH           0x058B
#define BT_APPEARANCE_LIGHT_FIXTURES_PATHWAY                0x058C
#define BT_APPEARANCE_LIGHT_FIXTURES_GARDEN                 0x058D
#define BT_APPEARANCE_LIGHT_FIXTURES_POLE_TOP               0x058E
#define BT_APPEARANCE_SPOT_LIGHT                            0x058F
#define BT_APPEARANCE_LIGHT_FIXTURES_LINEAR                 0x0590
#define BT_APPEARANCE_LIGHT_FIXTURES_STREET                 0x0591
#define BT_APPEARANCE_LIGHT_FIXTURES_SHELVES                0x0592
#define BT_APPEARANCE_LIGHT_FIXTURES_BAY                    0x0593
#define BT_APPEARANCE_LIGHT_FIXTURES_EMERGENCY_EXIT         0x0594
#define BT_APPEARANCE_LIGHT_FIXTURES_CONTROLLER             0x0595
#define BT_APPEARANCE_LIGHT_FIXTURES_DRIVER                 0x0596
#define BT_APPEARANCE_LIGHT_FIXTURES_BULB                   0x0597
#define BT_APPEARANCE_LIGHT_FIXTURES_LOW_BAY                0x0598
#define BT_APPEARANCE_LIGHT_FIXTURES_HIGH_BAY               0x0599
#define BT_APPEARANCE_GENERIC_FAN                           0x05C0
#define BT_APPEARANCE_FAN_CEILING                           0x05C1
#define BT_APPEARANCE_FAN_AXIAL                             0x05C2
#define BT_APPEARANCE_FAN_EXHAUST                           0x05C3
#define BT_APPEARANCE_FAN_PEDESTAL                          0x05C4
#define BT_APPEARANCE_FAN_DESK                              0x05C5
#define BT_APPEARANCE_FAN_WALL                              0x05C6
#define BT_APPEARANCE_GENERIC_HVAC                          0x0600
#define BT_APPEARANCE_HVAC_THERMOSTAT                       0x0601
#define BT_APPEARANCE_HVAC_HUMIDIFIER                       0x0602
#define BT_APPEARANCE_HVAC_DEHUMIDIFIER                     0x0603
#define BT_APPEARANCE_HVAC_HEATER                           0x0604
#define BT_APPEARANCE_HVAC_RADIATOR                         0x0605
#define BT_APPEARANCE_HVAC_BOILER                           0x0606
#define BT_APPEARANCE_HVAC_HEAT_PUMP                        0x0607
#define BT_APPEARANCE_HVAC_INFRARED_HEATER                  0x0608
#define BT_APPEARANCE_HVAC_RADIANT_PANEL_HEATER             0x0609
#define BT_APPEARANCE_HVAC_FAN_HEATER                       0x060A
#define BT_APPEARANCE_HVAC_AIR_CURTAIN                      0x060B
#define BT_APPEARANCE_GENERIC_AIR_CONDITIONING              0x0640
#define BT_APPEARANCE_GENERIC_HUMIDIFIER                    0x0680
#define BT_APPEARANCE_GENERIC_HEATING                       0x06C0
#define BT_APPEARANCE_HEATING_RADIATOR                      0x06C1
#define BT_APPEARANCE_HEATING_BOILER                        0x06C2
#define BT_APPEARANCE_HEATING_HEAT_PUMP                     0x06C3
#define BT_APPEARANCE_HEATING_INFRARED_HEATER               0x06C4
#define BT_APPEARANCE_HEATING_RADIANT_PANEL_HEATER          0x06C5
#define BT_APPEARANCE_HEATING_FAN_HEATER                    0x06C6
#define BT_APPEARANCE_HEATING_AIR_CURTAIN                   0x06C7
#define BT_APPEARANCE_GENERIC_ACCESS_CONTROL                0x0700
#define BT_APPEARANCE_CONTROL_ACCESS_DOOR                   0x0701
#define BT_APPEARANCE_CONTROL_GARAGE_DOOR                   0x0702
#define BT_APPEARANCE_CONTROL_EMERGENCY_EXIT_DOOR           0x0703
#define BT_APPEARANCE_CONTROL_ACCESS_LOCK                   0x0704
#define BT_APPEARANCE_CONTROL_ELEVATOR                      0x0705
#define BT_APPEARANCE_CONTROL_WINDOW                        0x0706
#define BT_APPEARANCE_CONTROL_ENTRANCE_GATE                 0x0707
#define BT_APPEARANCE_CONTROL_DOOR_LOCK                     0x0708
#define BT_APPEARANCE_CONTROL_LOCKER                        0x0709
#define BT_APPEARANCE_GENERIC_MOTORIZED_DEVICE              0x0740
#define BT_APPEARANCE_MOTORIZED_GATE                        0x0741
#define BT_APPEARANCE_MOTORIZED_AWNING                      0x0742
#define BT_APPEARANCE_MOTORIZED_BLINDS_OR_SHADES            0x0743
#define BT_APPEARANCE_MOTORIZED_CURTAINS                    0x0744
#define BT_APPEARANCE_MOTORIZED_SCREEN                      0x0745
#define BT_APPEARANCE_GENERIC_POWER_DEVICE                  0x0780
#define BT_APPEARANCE_POWER_OUTLET                          0x0781
#define BT_APPEARANCE_POWER_STRIP                           0x0782
#define BT_APPEARANCE_POWER_PLUG                            0x0783
#define BT_APPEARANCE_POWER_SUPPLY                          0x0784
#define BT_APPEARANCE_POWER_LED_DRIVER                      0x0785
#define BT_APPEARANCE_POWER_FLUORESCENT_LAMP_GEAR           0x0786
#define BT_APPEARANCE_POWER_HID_LAMP_GEAR                   0x0787
#define BT_APPEARANCE_POWER_CHARGE_CASE                     0x0788
#define BT_APPEARANCE_POWER_POWER_BANK                      0x0789
#define BT_APPEARANCE_GENERIC_LIGHT_SOURCE                  0x07C0
#define BT_APPEARANCE_LIGHT_SOURCE_INCANDESCENT_BULB        0x07C1
#define BT_APPEARANCE_LIGHT_SOURCE_LED_LAMP                 0x07C2
#define BT_APPEARANCE_LIGHT_SOURCE_HID_LAMP                 0x07C3
#define BT_APPEARANCE_LIGHT_SOURCE_FLUORESCENT_LAMP         0x07C4
#define BT_APPEARANCE_LIGHT_SOURCE_LED_ARRAY                0x07C5
#define BT_APPEARANCE_LIGHT_SOURCE_MULTICOLOR_LED_ARRAY     0x07C6
#define BT_APPEARANCE_LIGHT_SOURCE_LOW_VOLTAGE_HALOGEN      0x07C7
#define BT_APPEARANCE_LIGHT_SOURCE_OLED                     0x07C8
#define BT_APPEARANCE_GENERIC_WINDOW_COVERING               0x0800
#define BT_APPEARANCE_WINDOW_SHADES                         0x0801
#define BT_APPEARANCE_WINDOW_BLINDS                         0x0802
#define BT_APPEARANCE_WINDOW_AWNING                         0x0803
#define BT_APPEARANCE_WINDOW_CURTAIN                        0x0804
#define BT_APPEARANCE_WINDOW_EXTERIOR_SHUTTER               0x0805
#define BT_APPEARANCE_WINDOW_EXTERIOR_SCREEN                0x0806
#define BT_APPEARANCE_GENERIC_AUDIO_SINK                    0x0840
#define BT_APPEARANCE_AUDIO_SINK_STANDALONE_SPEAKER         0x0841
#define BT_APPEARANCE_AUDIO_SINK_SOUNDBAR                   0x0842
#define BT_APPEARANCE_AUDIO_SINK_BOOKSHELF_SPEAKER          0x0843
#define BT_APPEARANCE_AUDIO_SINK_STANDMOUNTED_SPEAKER       0x0844
#define BT_APPEARANCE_AUDIO_SINK_SPEAKERPHONE               0x0845
#define BT_APPEARANCE_GENERIC_AUDIO_SOURCE                  0x0880
#define BT_APPEARANCE_AUDIO_SOURCE_MICROPHONE               0x0881
#define BT_APPEARANCE_AUDIO_SOURCE_ALARM                    0x0882
#define BT_APPEARANCE_AUDIO_SOURCE_BELL                     0x0883
#define BT_APPEARANCE_AUDIO_SOURCE_HORN                     0x0884
#define BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_DEVICE      0x0885
#define BT_APPEARANCE_AUDIO_SOURCE_SERVICE_DESK             0x0886
#define BT_APPEARANCE_AUDIO_SOURCE_KIOSK                    0x0887
#define BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_ROOM        0x0888
#define BT_APPEARANCE_AUDIO_SOURCE_AUDITORIUM               0x0889
#define BT_APPEARANCE_GENERIC_MOTORIZED_VEHICLE             0x08C0
#define BT_APPEARANCE_VEHICLE_CAR                           0x08C1
#define BT_APPEARANCE_VEHICLE_LARGE_GOODS                   0x08C2
#define BT_APPEARANCE_VEHICLE_TWO_WHEELED                   0x08C3
#define BT_APPEARANCE_VEHICLE_MOTORBIKE                     0x08C4
#define BT_APPEARANCE_VEHICLE_SCOOTER                       0x08C5
#define BT_APPEARANCE_VEHICLE_MOPED                         0x08C6
#define BT_APPEARANCE_VEHICLE_THREE_WHEELED                 0x08C7
#define BT_APPEARANCE_VEHICLE_LIGHT                         0x08C8
#define BT_APPEARANCE_VEHICLE_QUAD_BIKE                     0x08C9
#define BT_APPEARANCE_VEHICLE_MINIBUS                       0x08CA
#define BT_APPEARANCE_VEHICLE_BUS                           0x08CB
#define BT_APPEARANCE_VEHICLE_TROLLEY                       0x08CC
#define BT_APPEARANCE_VEHICLE_AGRICULTURAL                  0x08CD
#define BT_APPEARANCE_VEHICLE_CAMPER_OR_CARAVAN             0x08CE
#define BT_APPEARANCE_VEHICLE_RECREATIONAL                  0x08CF
#define BT_APPEARANCE_GENERIC_DOMESTIC_APPLIANCE            0x0900
#define BT_APPEARANCE_APPLIANCE_REFRIGERATOR                0x0901
#define BT_APPEARANCE_APPLIANCE_FREEZER                     0x0902
#define BT_APPEARANCE_APPLIANCE_OVEN                        0x0903
#define BT_APPEARANCE_APPLIANCE_MICROWAVE                   0x0904
#define BT_APPEARANCE_APPLIANCE_TOASTER                     0x0905
#define BT_APPEARANCE_APPLIANCE_WASHING_MACHINE             0x0906
#define BT_APPEARANCE_APPLIANCE_DRYER                       0x0907
#define BT_APPEARANCE_APPLIANCE_COFFEE_MAKER                0x0908
#define BT_APPEARANCE_APPLIANCE_CLOTHES_IRON                0x0909
#define BT_APPEARANCE_APPLIANCE_CURLING_IRON                0x090A
#define BT_APPEARANCE_APPLIANCE_HAIR_DRYER                  0x090B
#define BT_APPEARANCE_APPLIANCE_VACUUM_CLEANER              0x090C
#define BT_APPEARANCE_APPLIANCE_ROBOTIC_VACUUM_CLEANER      0x090D
#define BT_APPEARANCE_APPLIANCE_RICE_COOKER                 0x090E
#define BT_APPEARANCE_APPLIANCE_CLOTHES_STEAMER             0x090F
#define BT_APPEARANCE_GENERIC_WEARABLE_AUDIO_DEVICE         0x0940
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_EARBUD          0x0941
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADSET         0x0942
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADPHONES      0x0943
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_NECK_BAND       0x0944
#define BT_APPEARANCE_GENERIC_AIRCRAFT                      0x0980
#define BT_APPEARANCE_AIRCRAFT_LIGHT                        0x0981
#define BT_APPEARANCE_AIRCRAFT_MICROLIGHT                   0x0982
#define BT_APPEARANCE_AIRCRAFT_PARAGLIDER                   0x0983
#define BT_APPEARANCE_AIRCRAFT_LARGE_PASSENGER              0x0984
#define BT_APPEARANCE_GENERIC_AV_EQUIPMENT                  0x09C0
#define BT_APPEARANCE_AV_EQUIPMENT_AMPLIFIER                0x09C1
#define BT_APPEARANCE_AV_EQUIPMENT_RECEIVER                 0x09C2
#define BT_APPEARANCE_AV_EQUIPMENT_RADIO                    0x09C3
#define BT_APPEARANCE_AV_EQUIPMENT_TUNER                    0x09C4
#define BT_APPEARANCE_AV_EQUIPMENT_TURNTABLE                0x09C5
#define BT_APPEARANCE_AV_EQUIPMENT_CD_PLAYER                0x09C6
#define BT_APPEARANCE_AV_EQUIPMENT_DVD_PLAYER               0x09C7
#define BT_APPEARANCE_AV_EQUIPMENT_BLURAY_PLAYER            0x09C8
#define BT_APPEARANCE_AV_EQUIPMENT_OPTICAL_DISC_PLAYER      0x09C9
#define BT_APPEARANCE_AV_EQUIPMENT_SET_TOP_BOX              0x09CA
#define BT_APPEARANCE_GENERIC_DISPLAY_EQUIPMENT             0x0A00
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_TELEVISION          0x0A01
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_MONITOR             0x0A02
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_PROJECTOR           0x0A03
#define BT_APPEARANCE_GENERIC_HEARING_AID                   0x0A40
#define BT_APPEARANCE_HEARING_AID_IN_EAR                    0x0A41
#define BT_APPEARANCE_HEARING_AID_BEHIND_EAR                0x0A42
#define BT_APPEARANCE_HEARING_AID_COCHLEAR_IMPLANT          0x0A43
#define BT_APPEARANCE_GENERIC_GAMING                        0x0A80
#define BT_APPEARANCE_HOME_VIDEO_GAME_CONSOLE               0x0A81
#define BT_APPEARANCE_PORTABLE_HANDHELD_CONSOLE             0x0A82
#define BT_APPEARANCE_GENERIC_SIGNAGE                       0x0AC0
#define BT_APPEARANCE_SIGNAGE_DIGITAL                       0x0AC1
#define BT_APPEARANCE_SIGNAGE_ELECTRONIC_LABEL              0x0AC2
#define BT_APPEARANCE_GENERIC_PULSE_OXIMETER                0x0C40
#define BT_APPEARANCE_PULSE_OXIMETER_FINGERTIP              0x0C41
#define BT_APPEARANCE_PULSE_OXIMETER_WRIST                  0x0C42
#define BT_APPEARANCE_GENERIC_WEIGHT_SCALE                  0x0C80
#define BT_APPEARANCE_GENERIC_PERSONAL_MOBILITY_DEVICE      0x0CC0
#define BT_APPEARANCE_MOBILITY_POWERED_WHEELCHAIR           0x0CC1
#define BT_APPEARANCE_MOBILITY_SCOOTER                      0x0CC2
#define BT_APPEARANCE_CONTINUOUS_GLUCOSE_MONITOR            0x0D00
#define BT_APPEARANCE_GENERIC_INSULIN_PUMP                  0x0D40
#define BT_APPEARANCE_INSULIN_PUMP_DURABLE                  0x0D41
#define BT_APPEARANCE_INSULIN_PUMP_PATCH                    0x0D44
#define BT_APPEARANCE_INSULIN_PEN                           0x0D48
#define BT_APPEARANCE_GENERIC_MEDICATION_DELIVERY           0x0D80
#define BT_APPEARANCE_GENERIC_SPIROMETER                    0x0DC0
#define BT_APPEARANCE_SPIROMETER_HANDHELD                   0x0DC1
#define BT_APPEARANCE_GENERIC_OUTDOOR_SPORTS                0x1440
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION               0x1441
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_AND_NAV       0x1442
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD           0x1443
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD_AND_NAV   0x1444
 /* end of @name Appearance Numbers */

#define BT_DATA_FLAGS                    0x01
#define BT_DATA_UUID16_SOME              0x02
#define BT_DATA_UUID16_ALL               0x03
#define BT_DATA_UUID32_SOME              0x04
#define BT_DATA_UUID32_ALL               0x05
#define BT_DATA_UUID128_SOME             0x06
#define BT_DATA_UUID128_ALL              0x07
#define BT_DATA_NAME_SHORTENED           0x08
#define BT_DATA_NAME_COMPLETE            0x09
#define BT_DATA_TX_POWER                 0x0a
#define BT_DATA_DEVICE_CLASS             0x0d
#define BT_DATA_SIMPLE_PAIRING_HASH_C192 0x0e
#define BT_DATA_SIMPLE_PAIRING_RAND_C192 0x0f
#define BT_DATA_DEVICE_ID                0x10
#define BT_DATA_SM_TK_VALUE              0x10
#define BT_DATA_SM_OOB_FLAGS             0x11
#define BT_DATA_PERIPHERAL_INT_RANGE     0x12
#define BT_DATA_SOLICIT16                0x14
#define BT_DATA_SOLICIT128               0x15
#define BT_DATA_SVC_DATA16               0x16
#define BT_DATA_PUB_TARGET_ADDR          0x17
#define BT_DATA_RAND_TARGET_ADDR         0x18
#define BT_DATA_GAP_APPEARANCE           0x19
#define BT_DATA_ADV_INT                  0x1a
#define BT_DATA_LE_BT_DEVICE_ADDRESS     0x1b
#define BT_DATA_LE_ROLE                  0x1c
#define BT_DATA_SIMPLE_PAIRING_HASH      0x1d
#define BT_DATA_SIMPLE_PAIRING_RAND      0x1e
#define BT_DATA_SOLICIT32                0x1f
#define BT_DATA_SVC_DATA32               0x20
#define BT_DATA_SVC_DATA128              0x21
#define BT_DATA_LE_SC_CONFIRM_VALUE      0x22
#define BT_DATA_LE_SC_RANDOM_VALUE       0x23
#define BT_DATA_URI                      0x24
#define BT_DATA_INDOOR_POS               0x25
#define BT_DATA_TRANS_DISCOVER_DATA      0x26
#define BT_DATA_LE_SUPPORTED_FEATURES    0x27
#define BT_DATA_CHANNEL_MAP_UPDATE_IND   0x28
#define BT_DATA_MESH_PROV                0x29
#define BT_DATA_MESH_MESSAGE             0x2a
#define BT_DATA_MESH_BEACON              0x2b
#define BT_DATA_BIG_INFO                 0x2c
#define BT_DATA_BROADCAST_CODE           0x2d
#define BT_DATA_CSIS_RSI                 0x2e
#define BT_DATA_ADV_INT_LONG             0x2f
#define BT_DATA_BROADCAST_NAME           0x30
#define BT_DATA_ENCRYPTED_AD_DATA        0x31
#define BT_DATA_PAWR_TIMING_INFO         0x32
#define BT_DATA_ESL                      0x34
#define BT_DATA_3D_INFO                  0x3D

#define BT_DATA_MANUFACTURER_DATA        0xff
 /* end of @name Common Data Types */


#define BT_LE_AD_LIMITED                 0x01
#define BT_LE_AD_GENERAL                 0x02
#define BT_LE_AD_NO_BREDR                0x04
 /* end of @name Flags data type values */ /* end of bt_assigned_numbers_core */


#define BT_MESH_MODEL_ID_CFG_SRV                   0x0000
#define BT_MESH_MODEL_ID_CFG_CLI                   0x0001
#define BT_MESH_MODEL_ID_HEALTH_SRV                0x0002
#define BT_MESH_MODEL_ID_HEALTH_CLI                0x0003
#define BT_MESH_MODEL_ID_REMOTE_PROV_SRV           0x0004
#define BT_MESH_MODEL_ID_REMOTE_PROV_CLI           0x0005
#define BT_MESH_MODEL_ID_BRG_CFG_SRV               0x0008
#define BT_MESH_MODEL_ID_BRG_CFG_CLI               0x0009
#define BT_MESH_MODEL_ID_PRIV_BEACON_SRV           0x000a
#define BT_MESH_MODEL_ID_PRIV_BEACON_CLI           0x000b
#define BT_MESH_MODEL_ID_SAR_CFG_SRV               0x000e
#define BT_MESH_MODEL_ID_SAR_CFG_CLI               0x000f
#define BT_MESH_MODEL_ID_OP_AGG_SRV                0x0010
#define BT_MESH_MODEL_ID_OP_AGG_CLI                0x0011
#define BT_MESH_MODEL_ID_LARGE_COMP_DATA_SRV       0x0012
#define BT_MESH_MODEL_ID_LARGE_COMP_DATA_CLI       0x0013
#define BT_MESH_MODEL_ID_SOL_PDU_RPL_SRV           0x0014
#define BT_MESH_MODEL_ID_SOL_PDU_RPL_CLI           0x0015
#define BT_MESH_MODEL_ID_ON_DEMAND_PROXY_SRV       0x000c
#define BT_MESH_MODEL_ID_ON_DEMAND_PROXY_CLI       0x000d

#define BT_MESH_MODEL_ID_GEN_ONOFF_SRV             0x1000
#define BT_MESH_MODEL_ID_GEN_ONOFF_CLI             0x1001
#define BT_MESH_MODEL_ID_GEN_LEVEL_SRV             0x1002
#define BT_MESH_MODEL_ID_GEN_LEVEL_CLI             0x1003
#define BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_SRV    0x1004
#define BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_CLI    0x1005
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SRV       0x1006
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SETUP_SRV 0x1007
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_CLI       0x1008
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SRV       0x1009
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SETUP_SRV 0x100a
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_CLI       0x100b
#define BT_MESH_MODEL_ID_GEN_BATTERY_SRV           0x100c
#define BT_MESH_MODEL_ID_GEN_BATTERY_CLI           0x100d
#define BT_MESH_MODEL_ID_GEN_LOCATION_SRV          0x100e
#define BT_MESH_MODEL_ID_GEN_LOCATION_SETUPSRV     0x100f
#define BT_MESH_MODEL_ID_GEN_LOCATION_CLI          0x1010
#define BT_MESH_MODEL_ID_GEN_ADMIN_PROP_SRV        0x1011
#define BT_MESH_MODEL_ID_GEN_MANUFACTURER_PROP_SRV 0x1012
#define BT_MESH_MODEL_ID_GEN_USER_PROP_SRV         0x1013
#define BT_MESH_MODEL_ID_GEN_CLIENT_PROP_SRV       0x1014
#define BT_MESH_MODEL_ID_GEN_PROP_CLI              0x1015
#define BT_MESH_MODEL_ID_SENSOR_SRV                0x1100
#define BT_MESH_MODEL_ID_SENSOR_SETUP_SRV          0x1101
#define BT_MESH_MODEL_ID_SENSOR_CLI                0x1102
#define BT_MESH_MODEL_ID_TIME_SRV                  0x1200
#define BT_MESH_MODEL_ID_TIME_SETUP_SRV            0x1201
#define BT_MESH_MODEL_ID_TIME_CLI                  0x1202
#define BT_MESH_MODEL_ID_SCENE_SRV                 0x1203
#define BT_MESH_MODEL_ID_SCENE_SETUP_SRV           0x1204
#define BT_MESH_MODEL_ID_SCENE_CLI                 0x1205
#define BT_MESH_MODEL_ID_SCHEDULER_SRV             0x1206
#define BT_MESH_MODEL_ID_SCHEDULER_SETUP_SRV       0x1207
#define BT_MESH_MODEL_ID_SCHEDULER_CLI             0x1208
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SRV       0x1300
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SETUP_SRV 0x1301
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_CLI       0x1302
#define BT_MESH_MODEL_ID_LIGHT_CTL_SRV             0x1303
#define BT_MESH_MODEL_ID_LIGHT_CTL_SETUP_SRV       0x1304
#define BT_MESH_MODEL_ID_LIGHT_CTL_CLI             0x1305
#define BT_MESH_MODEL_ID_LIGHT_CTL_TEMP_SRV        0x1306
#define BT_MESH_MODEL_ID_LIGHT_HSL_SRV             0x1307
#define BT_MESH_MODEL_ID_LIGHT_HSL_SETUP_SRV       0x1308
#define BT_MESH_MODEL_ID_LIGHT_HSL_CLI             0x1309
#define BT_MESH_MODEL_ID_LIGHT_HSL_HUE_SRV         0x130a
#define BT_MESH_MODEL_ID_LIGHT_HSL_SAT_SRV         0x130b
#define BT_MESH_MODEL_ID_LIGHT_XYL_SRV             0x130c
#define BT_MESH_MODEL_ID_LIGHT_XYL_SETUP_SRV       0x130d
#define BT_MESH_MODEL_ID_LIGHT_XYL_CLI             0x130e
#define BT_MESH_MODEL_ID_LIGHT_LC_SRV              0x130f
#define BT_MESH_MODEL_ID_LIGHT_LC_SETUPSRV         0x1310
#define BT_MESH_MODEL_ID_LIGHT_LC_CLI              0x1311

#define BT_MESH_MODEL_ID_BLOB_SRV                  0x1400
#define BT_MESH_MODEL_ID_BLOB_CLI                  0x1401

#define BT_MESH_MODEL_ID_DFU_SRV                   0x1402
#define BT_MESH_MODEL_ID_DFU_CLI                   0x1403
#define BT_MESH_MODEL_ID_DFD_SRV                   0x1404
#define BT_MESH_MODEL_ID_DFD_CLI                   0x1405
 /* end of bt_assigned_numbers_mesh */


enum __packed bt_bearer_tech {
        BT_BEARER_TECH_3G = 0x01,
        BT_BEARER_TECH_4G = 0x02,
        BT_BEARER_TECH_LTE = 0x03,
        BT_BEARER_TECH_WIFI = 0x04,
        BT_BEARER_TECH_5G = 0x05,
        BT_BEARER_TECH_GSM = 0x06,
        BT_BEARER_TECH_CDMA = 0x07,
        BT_BEARER_TECH_2G = 0x08,
        BT_BEARER_TECH_WCDMA = 0x09,
        /* Values 0x0A to 0xFF are reserved for future use */
};

enum bt_audio_codec_cap_type {
        BT_AUDIO_CODEC_CAP_TYPE_FREQ = 0x01,

        BT_AUDIO_CODEC_CAP_TYPE_DURATION = 0x02,

        BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT = 0x03,

        BT_AUDIO_CODEC_CAP_TYPE_FRAME_LEN = 0x04,

        BT_AUDIO_CODEC_CAP_TYPE_FRAME_COUNT = 0x05,
};

enum bt_audio_codec_cap_freq {
        BT_AUDIO_CODEC_CAP_FREQ_8KHZ = BIT(0),

        BT_AUDIO_CODEC_CAP_FREQ_11KHZ = BIT(1),

        BT_AUDIO_CODEC_CAP_FREQ_16KHZ = BIT(2),

        BT_AUDIO_CODEC_CAP_FREQ_22KHZ = BIT(3),

        BT_AUDIO_CODEC_CAP_FREQ_24KHZ = BIT(4),

        BT_AUDIO_CODEC_CAP_FREQ_32KHZ = BIT(5),

        BT_AUDIO_CODEC_CAP_FREQ_44KHZ = BIT(6),

        BT_AUDIO_CODEC_CAP_FREQ_48KHZ = BIT(7),

        BT_AUDIO_CODEC_CAP_FREQ_88KHZ = BIT(8),

        BT_AUDIO_CODEC_CAP_FREQ_96KHZ = BIT(9),

        BT_AUDIO_CODEC_CAP_FREQ_176KHZ = BIT(10),

        BT_AUDIO_CODEC_CAP_FREQ_192KHZ = BIT(11),

        BT_AUDIO_CODEC_CAP_FREQ_384KHZ = BIT(12),

        BT_AUDIO_CODEC_CAP_FREQ_ANY =
                (BT_AUDIO_CODEC_CAP_FREQ_8KHZ | BT_AUDIO_CODEC_CAP_FREQ_11KHZ |
                 BT_AUDIO_CODEC_CAP_FREQ_16KHZ | BT_AUDIO_CODEC_CAP_FREQ_22KHZ |
                 BT_AUDIO_CODEC_CAP_FREQ_24KHZ | BT_AUDIO_CODEC_CAP_FREQ_32KHZ |
                 BT_AUDIO_CODEC_CAP_FREQ_44KHZ | BT_AUDIO_CODEC_CAP_FREQ_48KHZ |
                 BT_AUDIO_CODEC_CAP_FREQ_88KHZ | BT_AUDIO_CODEC_CAP_FREQ_96KHZ |
                 BT_AUDIO_CODEC_CAP_FREQ_176KHZ | BT_AUDIO_CODEC_CAP_FREQ_192KHZ |
                 BT_AUDIO_CODEC_CAP_FREQ_384KHZ),
};

enum bt_audio_codec_cap_frame_dur {
        BT_AUDIO_CODEC_CAP_DURATION_7_5 = BIT(0),

        BT_AUDIO_CODEC_CAP_DURATION_10 = BIT(1),

        BT_AUDIO_CODEC_CAP_DURATION_ANY =
                (BT_AUDIO_CODEC_CAP_DURATION_7_5 | BT_AUDIO_CODEC_CAP_DURATION_10),

        BT_AUDIO_CODEC_CAP_DURATION_PREFER_7_5 = BIT(4),

        BT_AUDIO_CODEC_CAP_DURATION_PREFER_10 = BIT(5),
};

enum bt_audio_codec_cap_chan_count {
        BT_AUDIO_CODEC_CAP_CHAN_COUNT_1 = BIT(0),

        BT_AUDIO_CODEC_CAP_CHAN_COUNT_2 = BIT(1),

        BT_AUDIO_CODEC_CAP_CHAN_COUNT_3 = BIT(2),

        BT_AUDIO_CODEC_CAP_CHAN_COUNT_4 = BIT(3),

        BT_AUDIO_CODEC_CAP_CHAN_COUNT_5 = BIT(4),

        BT_AUDIO_CODEC_CAP_CHAN_COUNT_6 = BIT(5),

        BT_AUDIO_CODEC_CAP_CHAN_COUNT_7 = BIT(6),

        BT_AUDIO_CODEC_CAP_CHAN_COUNT_8 = BIT(7),

        BT_AUDIO_CODEC_CAP_CHAN_COUNT_ANY =
                (BT_AUDIO_CODEC_CAP_CHAN_COUNT_1 | BT_AUDIO_CODEC_CAP_CHAN_COUNT_2 |
                 BT_AUDIO_CODEC_CAP_CHAN_COUNT_3 | BT_AUDIO_CODEC_CAP_CHAN_COUNT_4 |
                 BT_AUDIO_CODEC_CAP_CHAN_COUNT_5 | BT_AUDIO_CODEC_CAP_CHAN_COUNT_6 |
                 BT_AUDIO_CODEC_CAP_CHAN_COUNT_7 | BT_AUDIO_CODEC_CAP_CHAN_COUNT_8),
};

#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_MIN 1
#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_MAX 8

#define BT_AUDIO_BROADCAST_NAME_LEN_MIN  4U
#define BT_AUDIO_BROADCAST_NAME_LEN_MAX  128U
#define BT_AUDIO_BROADCAST_NAME_CHAR_MIN 4U
#define BT_AUDIO_BROADCAST_NAME_CHAR_MAX 32U

enum bt_audio_codec_cfg_type {
        BT_AUDIO_CODEC_CFG_FREQ = 0x01,

        BT_AUDIO_CODEC_CFG_DURATION = 0x02,

        BT_AUDIO_CODEC_CFG_CHAN_ALLOC = 0x03,

        BT_AUDIO_CODEC_CFG_FRAME_LEN = 0x04,

        BT_AUDIO_CODEC_CFG_FRAME_BLKS_PER_SDU = 0x05,
};

enum bt_audio_codec_cfg_freq {
        BT_AUDIO_CODEC_CFG_FREQ_8KHZ = 0x01,

        BT_AUDIO_CODEC_CFG_FREQ_11KHZ = 0x02,

        BT_AUDIO_CODEC_CFG_FREQ_16KHZ = 0x03,

        BT_AUDIO_CODEC_CFG_FREQ_22KHZ = 0x04,

        BT_AUDIO_CODEC_CFG_FREQ_24KHZ = 0x05,

        BT_AUDIO_CODEC_CFG_FREQ_32KHZ = 0x06,

        BT_AUDIO_CODEC_CFG_FREQ_44KHZ = 0x07,

        BT_AUDIO_CODEC_CFG_FREQ_48KHZ = 0x08,

        BT_AUDIO_CODEC_CFG_FREQ_88KHZ = 0x09,

        BT_AUDIO_CODEC_CFG_FREQ_96KHZ = 0x0a,

        BT_AUDIO_CODEC_CFG_FREQ_176KHZ = 0x0b,

        BT_AUDIO_CODEC_CFG_FREQ_192KHZ = 0x0c,

        BT_AUDIO_CODEC_CFG_FREQ_384KHZ = 0x0d,
};

enum bt_audio_codec_cfg_frame_dur {
        BT_AUDIO_CODEC_CFG_DURATION_7_5 = 0x00,

        BT_AUDIO_CODEC_CFG_DURATION_10 = 0x01,
};

enum bt_audio_context {
        BT_AUDIO_CONTEXT_TYPE_NONE = 0,
        BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED = BIT(0),
        BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL = BIT(1),
        BT_AUDIO_CONTEXT_TYPE_MEDIA = BIT(2),
        BT_AUDIO_CONTEXT_TYPE_GAME = BIT(3),
        BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL = BIT(4),
        BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS = BIT(5),
        BT_AUDIO_CONTEXT_TYPE_LIVE = BIT(6),
        BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS = BIT(7),
        BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS = BIT(8),
        BT_AUDIO_CONTEXT_TYPE_RINGTONE = BIT(9),
        BT_AUDIO_CONTEXT_TYPE_ALERTS = BIT(10),
        BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM = BIT(11),
};

#define BT_AUDIO_CONTEXT_TYPE_ANY        (BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED | \
                                          BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL | \
                                          BT_AUDIO_CONTEXT_TYPE_MEDIA | \
                                          BT_AUDIO_CONTEXT_TYPE_GAME | \
                                          BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL | \
                                          BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS | \
                                          BT_AUDIO_CONTEXT_TYPE_LIVE | \
                                          BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS | \
                                          BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS | \
                                          BT_AUDIO_CONTEXT_TYPE_RINGTONE | \
                                          BT_AUDIO_CONTEXT_TYPE_ALERTS | \
                                          BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM)

enum bt_audio_parental_rating {
        BT_AUDIO_PARENTAL_RATING_NO_RATING        = 0x00,
        BT_AUDIO_PARENTAL_RATING_AGE_ANY          = 0x01,
        BT_AUDIO_PARENTAL_RATING_AGE_5_OR_ABOVE   = 0x02,
        BT_AUDIO_PARENTAL_RATING_AGE_6_OR_ABOVE   = 0x03,
        BT_AUDIO_PARENTAL_RATING_AGE_7_OR_ABOVE   = 0x04,
        BT_AUDIO_PARENTAL_RATING_AGE_8_OR_ABOVE   = 0x05,
        BT_AUDIO_PARENTAL_RATING_AGE_9_OR_ABOVE   = 0x06,
        BT_AUDIO_PARENTAL_RATING_AGE_10_OR_ABOVE  = 0x07,
        BT_AUDIO_PARENTAL_RATING_AGE_11_OR_ABOVE  = 0x08,
        BT_AUDIO_PARENTAL_RATING_AGE_12_OR_ABOVE  = 0x09,
        BT_AUDIO_PARENTAL_RATING_AGE_13_OR_ABOVE  = 0x0A,
        BT_AUDIO_PARENTAL_RATING_AGE_14_OR_ABOVE  = 0x0B,
        BT_AUDIO_PARENTAL_RATING_AGE_15_OR_ABOVE  = 0x0C,
        BT_AUDIO_PARENTAL_RATING_AGE_16_OR_ABOVE  = 0x0D,
        BT_AUDIO_PARENTAL_RATING_AGE_17_OR_ABOVE  = 0x0E,
        BT_AUDIO_PARENTAL_RATING_AGE_18_OR_ABOVE  = 0x0F
};

enum bt_audio_active_state {
        BT_AUDIO_ACTIVE_STATE_DISABLED       = 0x00,
        BT_AUDIO_ACTIVE_STATE_ENABLED        = 0x01,
};

enum bt_audio_assisted_listening_stream {
        BT_AUDIO_ASSISTED_LISTENING_STREAM_UNSPECIFIED = 0x00,
};

enum bt_audio_metadata_type {
        BT_AUDIO_METADATA_TYPE_PREF_CONTEXT = 0x01,

        BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT = 0x02,

        BT_AUDIO_METADATA_TYPE_PROGRAM_INFO = 0x03,

        BT_AUDIO_METADATA_TYPE_LANG = 0x04,

        BT_AUDIO_METADATA_TYPE_CCID_LIST = 0x05,

        BT_AUDIO_METADATA_TYPE_PARENTAL_RATING = 0x06,

        BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI = 0x07,

        BT_AUDIO_METADATA_TYPE_AUDIO_STATE = 0x08,

        BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE = 0x09,

        BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM = 0x0A,

        BT_AUDIO_METADATA_TYPE_BROADCAST_NAME = 0x0B,

        BT_AUDIO_METADATA_TYPE_EXTENDED = 0xFE,

        BT_AUDIO_METADATA_TYPE_VENDOR = 0xFF,
};

enum bt_audio_location {
        BT_AUDIO_LOCATION_MONO_AUDIO = 0,
        BT_AUDIO_LOCATION_FRONT_LEFT = BIT(0),
        BT_AUDIO_LOCATION_FRONT_RIGHT = BIT(1),
        BT_AUDIO_LOCATION_FRONT_CENTER = BIT(2),
        BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1 = BIT(3),
        BT_AUDIO_LOCATION_BACK_LEFT = BIT(4),
        BT_AUDIO_LOCATION_BACK_RIGHT = BIT(5),
        BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER = BIT(6),
        BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER = BIT(7),
        BT_AUDIO_LOCATION_BACK_CENTER = BIT(8),
        BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2 = BIT(9),
        BT_AUDIO_LOCATION_SIDE_LEFT = BIT(10),
        BT_AUDIO_LOCATION_SIDE_RIGHT = BIT(11),
        BT_AUDIO_LOCATION_TOP_FRONT_LEFT = BIT(12),
        BT_AUDIO_LOCATION_TOP_FRONT_RIGHT = BIT(13),
        BT_AUDIO_LOCATION_TOP_FRONT_CENTER = BIT(14),
        BT_AUDIO_LOCATION_TOP_CENTER = BIT(15),
        BT_AUDIO_LOCATION_TOP_BACK_LEFT = BIT(16),
        BT_AUDIO_LOCATION_TOP_BACK_RIGHT = BIT(17),
        BT_AUDIO_LOCATION_TOP_SIDE_LEFT = BIT(18),
        BT_AUDIO_LOCATION_TOP_SIDE_RIGHT = BIT(19),
        BT_AUDIO_LOCATION_TOP_BACK_CENTER = BIT(20),
        BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER = BIT(21),
        BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT = BIT(22),
        BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT = BIT(23),
        BT_AUDIO_LOCATION_FRONT_LEFT_WIDE = BIT(24),
        BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE = BIT(25),
        BT_AUDIO_LOCATION_LEFT_SURROUND = BIT(26),
        BT_AUDIO_LOCATION_RIGHT_SURROUND = BIT(27),
};

#define BT_AUDIO_LOCATION_ANY (BT_AUDIO_LOCATION_FRONT_LEFT | \
                               BT_AUDIO_LOCATION_FRONT_RIGHT | \
                               BT_AUDIO_LOCATION_FRONT_CENTER | \
                               BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1 | \
                               BT_AUDIO_LOCATION_BACK_LEFT | \
                               BT_AUDIO_LOCATION_BACK_RIGHT | \
                               BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER | \
                               BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER | \
                               BT_AUDIO_LOCATION_BACK_CENTER | \
                               BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2 | \
                               BT_AUDIO_LOCATION_SIDE_LEFT | \
                               BT_AUDIO_LOCATION_SIDE_RIGHT | \
                               BT_AUDIO_LOCATION_TOP_FRONT_LEFT | \
                               BT_AUDIO_LOCATION_TOP_FRONT_RIGHT | \
                               BT_AUDIO_LOCATION_TOP_FRONT_CENTER | \
                               BT_AUDIO_LOCATION_TOP_CENTER | \
                               BT_AUDIO_LOCATION_TOP_BACK_LEFT | \
                               BT_AUDIO_LOCATION_TOP_BACK_RIGHT | \
                               BT_AUDIO_LOCATION_TOP_SIDE_LEFT | \
                               BT_AUDIO_LOCATION_TOP_SIDE_RIGHT | \
                               BT_AUDIO_LOCATION_TOP_BACK_CENTER | \
                               BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER | \
                               BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT | \
                               BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT | \
                               BT_AUDIO_LOCATION_FRONT_LEFT_WIDE | \
                               BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE | \
                               BT_AUDIO_LOCATION_LEFT_SURROUND | \
                               BT_AUDIO_LOCATION_RIGHT_SURROUND)
 /* end of bt_assigned_numbers_audio */


#define BT_COMP_ID_LF           0x05f1
 /* end of @name Company Identifiers */


#define BT_COD(major_service, major_device, minor_device)                                          \
        (((uint32_t)major_service << 13) | ((uint32_t)major_device << 8) |                         \
         ((uint32_t)minor_device << 2))
#define BT_COD_VALID(cod) ((0 == (cod[0] & (BIT(0) | BIT(1)))) ? true : false)
#define BT_COD_MAJOR_SERVICE_CLASSES(cod)                                                          \
        ((((uint32_t)cod[2] & 0xFF) >> 5) | (((uint32_t)cod[1] & 0xD0) >> 5))
#define BT_COD_MAJOR_DEVICE_CLASS(cod) ((((uint32_t)cod[1]) & 0x1FUL))
#define BT_COD_MINOR_DEVICE_CLASS(cod) (((((uint32_t)cod[0]) & 0xFF) >> 2))


#define BT_COD_MAJOR_SVC_CLASS_LIMITED_DISCOVER BIT(13)
#define BT_COD_MAJOR_SVC_CLASS_LE_AUDIO         BIT(14)
#define BT_COD_MAJOR_SVC_CLASS_RESERVED         BIT(15)
#define BT_COD_MAJOR_SVC_CLASS_POSITIONING      BIT(16)
#define BT_COD_MAJOR_SVC_CLASS_NETWORKING       BIT(17)
#define BT_COD_MAJOR_SVC_CLASS_RENDERING        BIT(18)
#define BT_COD_MAJOR_SVC_CLASS_CAPTURING        BIT(19)
#define BT_COD_MAJOR_SVC_CLASS_OBJECT_TRANSFER  BIT(20)
#define BT_COD_MAJOR_SVC_CLASS_AUDIO            BIT(21)
#define BT_COD_MAJOR_SVC_CLASS_TELEPHONY        BIT(22)
#define BT_COD_MAJOR_SVC_CLASS_INFORMATION      BIT(23)
 /* end of Major Service Classes */


#define BT_COD_MAJOR_DEVICE_CLASS_MISCELLANEOUS 0x00
#define BT_COD_MAJOR_DEVICE_CLASS_COMPUTER      0x01
#define BT_COD_MAJOR_DEVICE_CLASS_PHONE         0x02
#define BT_COD_MAJOR_DEVICE_CLASS_LAN_NETWORK   0x03
#define BT_COD_MAJOR_DEVICE_CLASS_AUDIO_VIDEO   0x04
#define BT_COD_MAJOR_DEVICE_CLASS_PERIPHERAL    0x05
#define BT_COD_MAJOR_DEVICE_CLASS_IMAGING       0x06
#define BT_COD_MAJOR_DEVICE_CLASS_WEARABLE      0x07
#define BT_COD_MAJOR_DEVICE_CLASS_TOY           0x08
#define BT_COD_MAJOR_DEVICE_CLASS_HEALTH        0x09
#define BT_COD_MAJOR_DEVICE_CLASS_UNCATEGORIZED 0x1F
 /* end of Major Device Class */


#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_UNCATEGORIZED       0x00
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_DESKTOP_WORKSTATION 0x01
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_SERVER              0x02
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_LAPTOP              0x03
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_HANDHELD_PC_PDA     0x04
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_PALM_SIZED_PC_PDA   0x05
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_WEARABLE_COMPUTER   0x06
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_TABLET              0x07
 /* end of Minor Device Class - Computer Major Class */


#define BT_COD_MINOR_DEVICE_CLASS_PHONE_UNCATEGORIZED      0x00
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_CELLULAR           0x01
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_CORDLESS           0x02
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_SMARTPHONE         0x03
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_WIRED_MODEM        0x04
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_COMMON_ISDN_ACCESS 0x05
 /* end of Minor Device Class - Phone Major Class */


#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_FULLY_AVAILABLE      0x00
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_1_17_UTILIZED        0x01
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_17_33_UTILIZED       0x02
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_33_50_UTILIZED       0x03
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_50_67_UTILIZED       0x04
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_67_83_UTILIZED       0x05
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_83_99_UTILIZED       0x06
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_NO_SERVICE_AVAILABLE 0x07
 /* end of Minor Device Class - LAN/Network Major Class - Service Utilization */


#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_DEVICE_TYPE_UNCATEGORIZED 0x00

#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_UNCATEGORIZED             0x00
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_WEARABLE_HEADSET          0x01
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HANDSFREE                 0x02
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_MICROPHONE                0x04
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_LOUDSPEAKER               0x05
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HEADPHONES                0x06
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_PORTABLE_AUDIO            0x07
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAR_AUDIO                 0x08
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_SETTOP_BOX                0x09
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HIFI_AUDIO                0x0A
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VCR                       0x0B
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CAMERA              0x0C
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAMCORDER                 0x0D
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_MONITOR             0x0E
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_DISPLAY_LOUDSPEAKER 0x0F
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CONFERENCING        0x10
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_GAMING_TOY                0x12
 /* end of Minor Device Class - Audio/Video Major Class */


#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_NO_KEYBOARD_NO_POINTING 0x00
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_KEYBOARD                0x01
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_POINTING_DEVICE         0x02
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_COMBO_KEYBOARD_POINTING 0x03
 /* end of Minor Device Class - Peripheral Major Class - Input Device Type */


#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_UNCATEGORIZED           0x00
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_JOYSTICK                0x01
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_GAMEPAD                 0x02
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_REMOTE_CONTROL          0x03
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_SENSING_DEVICE          0x04
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITIZER_TABLET        0x05
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_CARD_READER             0x06
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITAL_PEN             0x07
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_SCANNER        0x08
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_GESTURAL_INPUT 0x09
 /* end of Minor Device Class - Peripheral Major Class - Device Type */


#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_DISPLAY 0x01
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_CAMERA  0x02
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_SCANNER 0x04
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_PRINTER 0x08

#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_UNCATEGORIZED 0x00
 /* end of Minor Device Class - Imaging Major Class */


#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HEADSET 0x01
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_PAGER   0x02
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_JACKET  0x03
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HELMET  0x04
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_GLASSES 0x05
 /* end of Minor Device Class - Wearable Major Class */


#define BT_COD_MINOR_DEVICE_CLASS_TOY_ROBOT      0x01
#define BT_COD_MINOR_DEVICE_CLASS_TOY_VEHICLE    0x02
#define BT_COD_MINOR_DEVICE_CLASS_TOY_DOLL       0x03
#define BT_COD_MINOR_DEVICE_CLASS_TOY_CONTROLLER 0x04
#define BT_COD_MINOR_DEVICE_CLASS_TOY_GAME       0x05
 /* end of Minor Device Class - Toy Major Class */


#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_UNDEFINED                 0x00
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_BLOOD_PRESSURE_MONITOR    0x01
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_THERMOMETER               0x02
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_WEIGHING_SCALE            0x03
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_GLUCOSE_METER             0x04
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PULSE_OXIMETER            0x05
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEART_PULSE_MONITOR       0x06
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEALTH_DATA_DISPLAY       0x07
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_STEP_COUNTER              0x08
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_BODY_COMPOSITION_ANALYZER 0x09
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PEAK_FLOW_MONITOR         0x0A
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_MEDICATION_MONITOR        0x0B
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_KNEE_PROSTHESIS           0x0C
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_ANKLE_PROSTHESIS          0x0D
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_GENERIC_HEALTH_MANAGER    0x0E
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PERSONAL_MOBILITY_DEVICE  0x0F
 /* end of Minor Device Class - Health Major Class */
 /* end of @name BR Class of Device */

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_ASSIGNED_NUMBERS_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015-2025 Intel Corporation。

版权（Copyright）：© 2017-2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 647 行

外观编号（Appearance Numbers）`@name` 分组结束。

### 注释 3：原第 706 行

常用数据类型（Common Data Types）`@name` 分组结束。

### 注释 4：原第 717 行

标志数据类型取值（Flags Data Type Values）`@name` 分组结束。

### 注释 5：原第 717 行

`bt_assigned_numbers_core` 分组结束。

### 注释 6：原第 915 行

`bt_assigned_numbers_mesh` 分组结束。

### 注释 7：原第 945 行

`0x0A` 至 `0xFF` 的值保留供将来使用（Reserved for Future Use）。

### 注释 8：原第 1481 行

`bt_assigned_numbers_audio` 分组结束。

### 注释 9：原第 1490 行

公司标识符（Company Identifiers）`@name` 分组结束。

### 注释 10：原第 1534 行

主要服务类别（Major Service Classes）分组结束。

### 注释 11：原第 1564 行

主要设备类别（Major Device Class）分组结束。

### 注释 12：原第 1588 行

次要设备类别（Minor Device Class）中的计算机主类别（Computer Major Class）分组结束。

### 注释 13：原第 1608 行

次要设备类别（Minor Device Class）中的电话主类别（Phone Major Class）分组结束。

### 注释 14：原第 1632 行

次要设备类别（Minor Device Class）中的局域网／网络主类别（LAN/Network Major Class）服务利用率（Service Utilization）分组结束。

### 注释 15：原第 1678 行

次要设备类别（Minor Device Class）中的音频／视频主类别（Audio/Video Major Class）分组结束。

### 注释 16：原第 1694 行

次要设备类别（Minor Device Class）中的外设主类别（Peripheral Major Class）输入设备类型（Input Device Type）分组结束。

### 注释 17：原第 1722 行

次要设备类别（Minor Device Class）中的外设主类别（Peripheral Major Class）设备类型（Device Type）分组结束。

### 注释 18：原第 1741 行

次要设备类别（Minor Device Class）中的成像主类别（Imaging Major Class）分组结束。

### 注释 19：原第 1759 行

次要设备类别（Minor Device Class）中的可穿戴主类别（Wearable Major Class）分组结束。

### 注释 20：原第 1777 行

次要设备类别（Minor Device Class）中的玩具主类别（Toy Major Class）分组结束。

### 注释 21：原第 1817 行

次要设备类别（Minor Device Class）中的健康主类别（Health Major Class）分组结束。

### 注释 22：原第 1819 行

基本速率设备类别（BR Class of Device）`@name` 分组结束。

### 注释 23：原第 1830 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_ASSIGNED_NUMBERS_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)
- [BT_BEARER_TECH_3G](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga4bf3f820b493361a9a3b393d0282420fa62dfe9fe5ac51927efef815b9ce6874e)
- [BT_BEARER_TECH_4G](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga4bf3f820b493361a9a3b393d0282420fa231fe012027b8d279e325231d804ed29)
- [BT_BEARER_TECH_LTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga4bf3f820b493361a9a3b393d0282420fa1bd25e0325ebefc57bdac0968e84fd64)
- [BT_BEARER_TECH_WIFI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga4bf3f820b493361a9a3b393d0282420fab74491db769e0ab918809ab244e2ad1c)
- [BT_BEARER_TECH_5G](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga4bf3f820b493361a9a3b393d0282420faf6494f280fa28f202ce28bb7bc66ee24)
- [BT_BEARER_TECH_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga4bf3f820b493361a9a3b393d0282420fac6789c1a3127b92c1d9c6a5ee6f02c8a)
- [BT_BEARER_TECH_CDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga4bf3f820b493361a9a3b393d0282420fa1ab62f67902936349103d33f1475a328)
- [BT_BEARER_TECH_2G](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga4bf3f820b493361a9a3b393d0282420face445f78f84de0ef7c6d3ef23e3172b8)
- [BT_BEARER_TECH_WCDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga4bf3f820b493361a9a3b393d0282420fac6fad482035f2eab235dac4dffe77baa)
- [bt_audio_codec_cap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf58823a56eb36cfd22e582ab1ea3d015)
- [BT_AUDIO_CODEC_CAP_TYPE_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b)
- [BT_AUDIO_CODEC_CAP_TYPE_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510)
- [BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191)
- [BT_AUDIO_CODEC_CAP_TYPE_FRAME_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46)
- [BT_AUDIO_CODEC_CAP_TYPE_FRAME_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41)
- [bt_audio_codec_cap_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaafc1106d5d305874ee2f540c850ff5b4)
- [BT_AUDIO_CODEC_CAP_FREQ_8KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_AUDIO_CODEC_CAP_FREQ_11KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81)
- [BT_AUDIO_CODEC_CAP_FREQ_16KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361)
- [BT_AUDIO_CODEC_CAP_FREQ_22KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982)
- [BT_AUDIO_CODEC_CAP_FREQ_24KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956)
- [BT_AUDIO_CODEC_CAP_FREQ_32KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c)
- [BT_AUDIO_CODEC_CAP_FREQ_44KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3)
- [BT_AUDIO_CODEC_CAP_FREQ_48KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91)
- [BT_AUDIO_CODEC_CAP_FREQ_88KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211)
- [BT_AUDIO_CODEC_CAP_FREQ_96KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663)
- [BT_AUDIO_CODEC_CAP_FREQ_176KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b)
- [BT_AUDIO_CODEC_CAP_FREQ_192KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890)
- [BT_AUDIO_CODEC_CAP_FREQ_384KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2)
- [BT_AUDIO_CODEC_CAP_FREQ_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02)
- [bt_audio_codec_cap_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf37e8e19f956afb3c3a413cbaa1a21f5)
- [BT_AUDIO_CODEC_CAP_DURATION_7_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441)
- [BT_AUDIO_CODEC_CAP_DURATION_10](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b)
- [BT_AUDIO_CODEC_CAP_DURATION_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a)
- [BT_AUDIO_CODEC_CAP_DURATION_PREFER_7_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91)
- [BT_AUDIO_CODEC_CAP_DURATION_PREFER_10](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e)
- [bt_audio_codec_cap_chan_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gae695b5d17359967703f2509db1671fa5)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_6](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_7](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219)
- [bt_audio_codec_cfg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga9230ec4d7518bd243207ba2decb1a974)
- [BT_AUDIO_CODEC_CFG_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3)
- [BT_AUDIO_CODEC_CFG_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223)
- [BT_AUDIO_CODEC_CFG_CHAN_ALLOC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2)
- [BT_AUDIO_CODEC_CFG_FRAME_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2)
- [BT_AUDIO_CODEC_CFG_FRAME_BLKS_PER_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8)
- [bt_audio_codec_cfg_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga8e99fb678cc011bb8c9f6e1858bae0d7)
- [BT_AUDIO_CODEC_CFG_FREQ_8KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a)
- [BT_AUDIO_CODEC_CFG_FREQ_11KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8)
- [BT_AUDIO_CODEC_CFG_FREQ_16KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245)
- [BT_AUDIO_CODEC_CFG_FREQ_22KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048)
- [BT_AUDIO_CODEC_CFG_FREQ_24KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275)
- [BT_AUDIO_CODEC_CFG_FREQ_32KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e)
- [BT_AUDIO_CODEC_CFG_FREQ_44KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84)
- [BT_AUDIO_CODEC_CFG_FREQ_48KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11)
- [BT_AUDIO_CODEC_CFG_FREQ_88KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409)
- [BT_AUDIO_CODEC_CFG_FREQ_96KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60)
- [BT_AUDIO_CODEC_CFG_FREQ_176KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126)
- [BT_AUDIO_CODEC_CFG_FREQ_192KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7)
- [BT_AUDIO_CODEC_CFG_FREQ_384KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4)
- [bt_audio_codec_cfg_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga83701b5eadfcbc9b84dc0b1a85ebeb74)
- [BT_AUDIO_CODEC_CFG_DURATION_7_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272)
- [BT_AUDIO_CODEC_CFG_DURATION_10](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7)
- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [BT_AUDIO_CONTEXT_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a890d2723c8b23127ab4a1cb8b6b1118d)
- [BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5)
- [BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e)
- [BT_AUDIO_CONTEXT_TYPE_MEDIA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e)
- [BT_AUDIO_CONTEXT_TYPE_GAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730)
- [BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4)
- [BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e)
- [BT_AUDIO_CONTEXT_TYPE_LIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55)
- [BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9)
- [BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377)
- [BT_AUDIO_CONTEXT_TYPE_RINGTONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3)
- [BT_AUDIO_CONTEXT_TYPE_ALERTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6)
- [BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1)
- [bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)
- [BT_AUDIO_PARENTAL_RATING_NO_RATING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c)
- [BT_AUDIO_PARENTAL_RATING_AGE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1)
- [BT_AUDIO_PARENTAL_RATING_AGE_5_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526)
- [BT_AUDIO_PARENTAL_RATING_AGE_6_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc)
- [BT_AUDIO_PARENTAL_RATING_AGE_7_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a)
- [BT_AUDIO_PARENTAL_RATING_AGE_8_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4)
- [BT_AUDIO_PARENTAL_RATING_AGE_9_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd)
- [BT_AUDIO_PARENTAL_RATING_AGE_10_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2)
- [BT_AUDIO_PARENTAL_RATING_AGE_11_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0)
- [BT_AUDIO_PARENTAL_RATING_AGE_12_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7)
- [BT_AUDIO_PARENTAL_RATING_AGE_13_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d)
- [BT_AUDIO_PARENTAL_RATING_AGE_14_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86)
- [BT_AUDIO_PARENTAL_RATING_AGE_15_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077)
- [BT_AUDIO_PARENTAL_RATING_AGE_16_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92)
- [BT_AUDIO_PARENTAL_RATING_AGE_17_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff)
- [BT_AUDIO_PARENTAL_RATING_AGE_18_OR_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071)
- [bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)
- [BT_AUDIO_ACTIVE_STATE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3)
- [BT_AUDIO_ACTIVE_STATE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940)
- [bt_audio_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga207fbf0fbca9b24cba02c7f1d184e7f5)
- [BT_AUDIO_ASSISTED_LISTENING_STREAM_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga207fbf0fbca9b24cba02c7f1d184e7f5ab1714206feaa04b3be586ddb33ed5285)
- [bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)
- [BT_AUDIO_METADATA_TYPE_PREF_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)
- [BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)
- [BT_AUDIO_METADATA_TYPE_PROGRAM_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7)
- [BT_AUDIO_METADATA_TYPE_LANG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1)
- [BT_AUDIO_METADATA_TYPE_CCID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b)
- [BT_AUDIO_METADATA_TYPE_PARENTAL_RATING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613)
- [BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922)
- [BT_AUDIO_METADATA_TYPE_AUDIO_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc)
- [BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1)
- [BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf)
- [BT_AUDIO_METADATA_TYPE_BROADCAST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6)
- [BT_AUDIO_METADATA_TYPE_EXTENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39)
- [BT_AUDIO_METADATA_TYPE_VENDOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [BT_AUDIO_LOCATION_MONO_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df)
- [BT_AUDIO_LOCATION_FRONT_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b)
- [BT_AUDIO_LOCATION_FRONT_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3)
- [BT_AUDIO_LOCATION_FRONT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337)
- [BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6)
- [BT_AUDIO_LOCATION_BACK_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896)
- [BT_AUDIO_LOCATION_BACK_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa)
- [BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e)
- [BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692)
- [BT_AUDIO_LOCATION_BACK_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983)
- [BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b)
- [BT_AUDIO_LOCATION_SIDE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064)
- [BT_AUDIO_LOCATION_SIDE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd)
- [BT_AUDIO_LOCATION_TOP_FRONT_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9)
- [BT_AUDIO_LOCATION_TOP_FRONT_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d)
- [BT_AUDIO_LOCATION_TOP_FRONT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e)
- [BT_AUDIO_LOCATION_TOP_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f)
- [BT_AUDIO_LOCATION_TOP_BACK_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06)
- [BT_AUDIO_LOCATION_TOP_BACK_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69)
- [BT_AUDIO_LOCATION_TOP_SIDE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6)
- [BT_AUDIO_LOCATION_TOP_SIDE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59)
- [BT_AUDIO_LOCATION_TOP_BACK_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd)
- [BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376)
- [BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29)
- [BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8)
- [BT_AUDIO_LOCATION_FRONT_LEFT_WIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d)
- [BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71)
- [BT_AUDIO_LOCATION_LEFT_SURROUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6)
- [BT_AUDIO_LOCATION_RIGHT_SURROUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[返回大纲](大纲.md) · [下一章](P002_esp32c61-gpio-sigmap.h_源码浏览.md)
