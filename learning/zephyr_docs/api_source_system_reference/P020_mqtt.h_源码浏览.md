---
id: learning.zephyr-docs.api-source-system-reference.page-20
title: mqtt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_mqtt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h.html)。

## 20.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
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
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="foldopen00135"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="foldopen00162"></a>
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
<a id="foldopen00188"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="foldopen00203"></a>
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
<a id="foldopen00236"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="foldopen00243"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="foldopen00257"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="foldopen00261"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="foldopen00267"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="foldopen00285"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="foldopen00305"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="foldopen00311"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="foldopen00317"></a>
<a id="l00317"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00329"></a>
<a id="l00330"></a>
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
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00382"></a>
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
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="foldopen00426"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00437"></a>
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
<a id="foldopen00450"></a>
<a id="l00450"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="foldopen00464"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="foldopen00478"></a>
<a id="l00478"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="foldopen00492"></a>
<a id="l00492"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="foldopen00506"></a>
<a id="l00506"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="foldopen00524"></a>
<a id="l00524"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="foldopen00538"></a>
<a id="l00538"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00559"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00585"></a>
<a id="l00587"></a>
<a id="l00589"></a>
<a id="l00591"></a>
<a id="l00593"></a>
<a id="l00595"></a>
<a id="l00597"></a>
<a id="l00599"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="foldopen00608"></a>
<a id="l00608"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00620"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="foldopen00633"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00639"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00653"></a>
<a id="l00655"></a>
<a id="l00657"></a>
<a id="l00659"></a>
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
<a id="foldopen00673"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00692"></a>
<a id="l00694"></a>
<a id="l00696"></a>
<a id="l00698"></a>
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
<a id="foldopen00715"></a>
<a id="l00715"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="foldopen00755"></a>
<a id="l00755"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="foldopen00782"></a>
<a id="l00782"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="foldopen00824"></a>
<a id="l00824"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="foldopen00853"></a>
<a id="l00853"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00866"></a>
<a id="l00868"></a>
<a id="l00870"></a>
<a id="l00871"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00875"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00889"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00909"></a>
<a id="l00911"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="foldopen00923"></a>
<a id="l00923"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00948"></a>
<a id="l00949"></a>
<a id="foldopen00954"></a>
<a id="l00954"></a>
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00959"></a>
<a id="l00960"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00972"></a>
<a id="l00973"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00982"></a>
<a id="l00984"></a>
<a id="l00985"></a>
<a id="l00987"></a>
<a id="l00988"></a>
<a id="l00990"></a>
<a id="l00991"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l00996"></a>
<a id="l00997"></a>
<a id="l00999"></a>
<a id="l01000"></a>
<a id="l01002"></a>
<a id="l01003"></a>
<a id="l01004"></a>
<a id="l01005"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="l01016"></a>
<a id="l01017"></a>
<a id="l01019"></a>
<a id="l01020"></a>
<a id="l01022"></a>
<a id="l01023"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01033"></a>
<a id="l01034"></a>
<a id="l01036"></a>
<a id="l01037"></a>
<a id="l01039"></a>
<a id="l01040"></a>
<a id="l01041"></a>
<a id="l01043"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01054"></a>
<a id="l01055"></a>
<a id="l01057"></a>
<a id="l01058"></a>
<a id="l01060"></a>
<a id="l01061"></a>
<a id="l01063"></a>
<a id="l01064"></a>
<a id="l01066"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01072"></a>
<a id="l01073"></a>
<a id="l01077"></a>
<a id="l01078"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01082"></a>
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
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01156"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01170"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01183"></a>
<a id="l01184"></a>
<a id="l01185"></a>
<a id="l01197"></a>
<a id="l01198"></a>
<a id="l01199"></a>
<a id="l01209"></a>
<a id="l01210"></a>
<a id="l01211"></a>
<a id="l01224"></a>
<a id="l01225"></a>
<a id="l01226"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="l01248"></a>
<a id="l01249"></a>
<a id="l01250"></a>
<a id="l01251"></a>
<a id="l01262"></a>
<a id="l01263"></a>
<a id="l01264"></a>
<a id="l01275"></a>
<a id="l01276"></a>
<a id="l01291"></a>
<a id="l01292"></a>
<a id="l01303"></a>
<a id="l01304"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01337"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01351"></a>
<a id="l01352"></a>
<a id="l01353"></a>
<a id="l01366"></a>
<a id="l01367"></a>
<a id="l01368"></a>
<a id="l01369"></a>
<a id="l01370"></a>
<a id="l01371"></a>
<a id="l01372"></a>
<a id="l01373"></a>
<a id="l01374"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="agroup__mqtt__socket_html_ga0071fe013b9920711456ef51cc3e6d91"></a>
<a id="agroup__mqtt__socket_html_ga05213aceaa9e9cbbfaa9bab7a78b3d25"></a>
<a id="agroup__mqtt__socket_html_ga0bc7d91da88c2fbc25108d89ce4318c4"></a>
<a id="agroup__mqtt__socket_html_ga25ba4f0870fc2c01ee5fc2c06bd898c8"></a>
<a id="agroup__mqtt__socket_html_ga2b17999e845d613f5b0b20015b8204f3"></a>
<a id="agroup__mqtt__socket_html_ga2dbc3c158d63a6f57b362be94c22660a"></a>
<a id="agroup__mqtt__socket_html_ga31823965ec34a253793b40b50e800417"></a>
<a id="agroup__mqtt__socket_html_ga3559cdd6093d75c6fe6792ec2a453172"></a>
<a id="agroup__mqtt__socket_html_ga396015e492b0fee8da37c7168d9cdb33"></a>
<a id="agroup__mqtt__socket_html_ga40d226b891b8f62f2c486bbb11ce9678"></a>
<a id="agroup__mqtt__socket_html_ga4ff43a198e93e332b5553a4d0b59261d"></a>
<a id="agroup__mqtt__socket_html_ga57745efa1bf6fbdf7eb1b3f01623e4c7"></a>
<a id="agroup__mqtt__socket_html_ga6c952ed014f78774096bfb6099794803"></a>
<a id="agroup__mqtt__socket_html_ga8b87710d01076c8e51b1a75634168269"></a>
<a id="agroup__mqtt__socket_html_ga90d152a4b0986e9a07a12c7c56f5e2a0"></a>
<a id="agroup__mqtt__socket_html_gaa16bf7b0597ad00c4a3943235579e86b"></a>
<a id="agroup__mqtt__socket_html_gaa17b38ed9c7e65f3e01ad906b24bb618"></a>
<a id="agroup__mqtt__socket_html_gaaf563f26ca66841145643a657119d780"></a>
<a id="agroup__mqtt__socket_html_gabdf01ededb62ceb4c1608a64cb718a8c"></a>
<a id="agroup__mqtt__socket_html_gaca1e61c8b14b75544e253cea355274a8"></a>
<a id="agroup__mqtt__socket_html_gacbe41b83d9c0676d0d4cf01dd91765eb"></a>
<a id="agroup__mqtt__socket_html_gacdbeff0450bbcd438cdf35cd543fc6d6"></a>
<a id="agroup__mqtt__socket_html_gad1376509ae7c946c840d103d8b59e9a1"></a>
<a id="agroup__mqtt__socket_html_gad1d549d37b69a61e1bf8d9d213e02ca8"></a>
<a id="agroup__mqtt__socket_html_gad4d870f91a7d594c3a7325ab6de87a02"></a>
<a id="agroup__mqtt__socket_html_gad936f28553cb2e771a843512b0a315fa"></a>
<a id="agroup__mqtt__socket_html_gae4c3fb5313addb72961ff578113d183a"></a>
<a id="agroup__mqtt__socket_html_gae9069fceec2c018e64cc6beb16aa055c"></a>
<a id="agroup__mqtt__socket_html_gafb2df41fad7c318f9fe75919919139bd"></a>
<a id="agroup__mqtt__socket_html_gaffc2c3078004cf8d24935be086ad63b4"></a>
<a id="agroup__mqtt__socket_html_gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87"></a>
<a id="agroup__mqtt__socket_html_gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de"></a>
<a id="agroup__mqtt__socket_html_gga0071fe013b9920711456ef51cc3e6d91a4c5645869d17a4f9391999bfb6bbccde"></a>
<a id="agroup__mqtt__socket_html_gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5"></a>
<a id="agroup__mqtt__socket_html_gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb"></a>
<a id="agroup__mqtt__socket_html_gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032"></a>
<a id="agroup__mqtt__socket_html_gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2"></a>
<a id="agroup__mqtt__socket_html_gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9"></a>
<a id="agroup__mqtt__socket_html_gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2"></a>
<a id="agroup__mqtt__socket_html_gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3"></a>
<a id="agroup__mqtt__socket_html_gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8"></a>
<a id="agroup__mqtt__socket_html_gga25ba4f0870fc2c01ee5fc2c06bd898c8a1cd3179b4d1d791dbc9f0c99319603c4"></a>
<a id="agroup__mqtt__socket_html_gga25ba4f0870fc2c01ee5fc2c06bd898c8a359c9c2a716d046a74961ca9012f921d"></a>
<a id="agroup__mqtt__socket_html_gga25ba4f0870fc2c01ee5fc2c06bd898c8a804e0f2d820fbc89f83d02fa50b9a8fc"></a>
<a id="agroup__mqtt__socket_html_gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e"></a>
<a id="agroup__mqtt__socket_html_gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d"></a>
<a id="agroup__mqtt__socket_html_gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117"></a>
<a id="agroup__mqtt__socket_html_gga90d152a4b0986e9a07a12c7c56f5e2a0a6f11ad8ae7114d8c1fdf85bda376b97f"></a>
<a id="agroup__mqtt__socket_html_gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7"></a>
<a id="agroup__mqtt__socket_html_gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e"></a>
<a id="agroup__mqtt__socket_html_ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050"></a>
<a id="agroup__mqtt__socket_html_ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb"></a>
<a id="agroup__mqtt__socket_html_ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744"></a>
<a id="agroup__mqtt__socket_html_ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134"></a>
<a id="agroup__mqtt__socket_html_ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141"></a>
<a id="agroup__mqtt__socket_html_ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a053e8c2e553308869a31582cd85d1610"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a0cdcb8aed8cf188a50ca6094f3280f98"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a11c5eb260bb0d16faeca565aef4f79cf"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a2421954cb46644bc942827fdeb21cb9c"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a27eb2c713ee9957075da608d1da6ce6c"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a34cce9b17d556ca9d93d01302ec079e6"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a3639eb9318092b7c642001133e21158b"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a4d5c4ec55ee517078c47c59d81fadc78"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a55857c640fa90478873eed61a27fa2c0"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a625f16227444f6f306de49aa953acd9d"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a70754dd31cc50ca8963ecedf52087a0d"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a82b2e5d2b8358fe893d5c682093d13c4"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a9d383cae65f31d61bdcf1e38db92bbc4"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780a9e863b1f7632caa83efdb41f742f7c6a"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780aad7106c041af27373d4e3b87faddafec"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780ab418f144f1509e91332486a6f4ee9293"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780ab86eac24ac0829257a1b11c8b82e8194"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780abbca5c088ca0392dca55c87469c571fa"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780ac1db368d96389b585530954a493bcf9a"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780ac6db698ae6e2d24b480997adcff7e1a5"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780ace998d2c989d41195d40dda31cf19173"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780acfd3c3a5b146ed10efb32cd7c6e0cb65"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780ad9f253248e9fecaae14ee37f0c02d87c"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780adc4c0e7ee2f8a1ab654f23b8355b878b"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780adf78c69bb559f2b471ecdf4380fe21d1"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780ae3d9774a0f77be21b670512eb4a40b86"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780af4b7253dac64f072945054d02d9c2603"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780af95f658c0b71d44c6aab3dc3b01ac00c"></a>
<a id="agroup__mqtt__socket_html_ggaaf563f26ca66841145643a657119d780afb77e6ac6da08c7d21f093c6068bdd5a"></a>
<a id="agroup__mqtt__socket_html_ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7"></a>
<a id="agroup__mqtt__socket_html_ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01"></a>
<a id="agroup__mqtt__socket_html_ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b"></a>
<a id="agroup__mqtt__socket_html_ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c"></a>
<a id="agroup__mqtt__socket_html_ggacdbeff0450bbcd438cdf35cd543fc6d6a46e6b7c5ae59f315137cf0df3aec816a"></a>
<a id="agroup__mqtt__socket_html_ggacdbeff0450bbcd438cdf35cd543fc6d6a609d75c1d9d37d5340ac979c924efa60"></a>
<a id="agroup__mqtt__socket_html_ggacdbeff0450bbcd438cdf35cd543fc6d6add4e38c81c8e1a8b79d911c87612f863"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa04de5af39cb78ef43bb4c8e701287ed0"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa19f93ee28b2b6841289fade02c351989"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa1fd45d6623840524c7af93a4725025cc"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa2d5037f830538b73ea342bcdc24a9816"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa30546ae5648049fb5c14161b5ae42aa8"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa3819f991bd83ec9b4bf55754f7ef93ee"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa5838075a9ed66476838a3fcda7eeba33"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa6fc0c79bac3ec08435fbaec3f80a2eb5"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa75f011e782a11c1c594848daf63e2fb0"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa76a813a52ed0d4f53b2646176b2fb5aa"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa7ac5fefe2b6c3e7946dc84628fd560bd"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa83ec9ee9dfb3f649d06cf4d5f527ae4e"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa8ded9dc2d24ca21f67e97217047f876c"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa8eda2ef9f0e7cc719169370e2cdcf8fa"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aa930dc7b029c625730377653165736040"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aaa9386156438b2f5b71d57324c54c5f7f"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aab152dc910d3c55de3b64f0ac22611956"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aabd738258dd4eaabe5c4ebb4bcf69e5d7"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aae84b943ac946b53a1df9ec409746274e"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aaf5a1f0040353625ff72dee52fb13f75c"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aafae37cc54cb28707b473d20f53c335d4"></a>
<a id="agroup__mqtt__socket_html_ggae4c3fb5313addb72961ff578113d183aafe38d9cabe4bee5f3f28484a58c5137f"></a>
<a id="agroup__mqtt__socket_html_ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df"></a>
<a id="agroup__mqtt__socket_html_ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a"></a>
<a id="agroup__tls__credentials_html_gaadfe9694309e473f7be74ed98dfb36d3"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amutex_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructmqtt__auth__param_html"></a>
<a id="astructmqtt__auth__param_html_a1ad0e22ec7f3d5d1d304bacad06cb0c6"></a>
<a id="astructmqtt__auth__param_html_a32bfb124dbaa11a328e7300bc0890cfc"></a>
<a id="astructmqtt__auth__param_html_a500d1b239b9882a1625d5d6035dd3199"></a>
<a id="astructmqtt__auth__param_html_a50f570175c944f7e0dad4b276c07a6ea"></a>
<a id="astructmqtt__auth__param_html_a5602413c28ceadc87420f8c7a6c53489"></a>
<a id="astructmqtt__auth__param_html_a6bd366cb6479370f9db0abaa22e1b803"></a>
<a id="astructmqtt__auth__param_html_a6cf278bec874623fcd97a5c5e7d43940"></a>
<a id="astructmqtt__auth__param_html_a772343a4f3df425e54c00c43f5fdced4"></a>
<a id="astructmqtt__auth__param_html_a9403d927a86f90eb1847840d6f47fe37"></a>
<a id="astructmqtt__auth__param_html_aaa1aa29efd09cf58aaf79b4e279dc2a9"></a>
<a id="astructmqtt__auth__param_html_adace77cd3860024ece2252ee41dcd134"></a>
<a id="astructmqtt__binstr_html"></a>
<a id="astructmqtt__binstr_html_a1f61872edd09941155f60a242e582ff7"></a>
<a id="astructmqtt__binstr_html_abcc36b6c59c3da740a6b352fe846fd5f"></a>
<a id="astructmqtt__client_html"></a>
<a id="astructmqtt__client_html_a0a1669a8be16d37819704ac60911de73"></a>
<a id="astructmqtt__client_html_a1a8f71b8756219a20404782c9aeff431"></a>
<a id="astructmqtt__client_html_a1c5a0e00803a745b2569452ed127440a"></a>
<a id="astructmqtt__client_html_a1d0587f7b2be63eb74f9cba271c337fb"></a>
<a id="astructmqtt__client_html_a253bee13043ffe1ebe9c46299f8a238e"></a>
<a id="astructmqtt__client_html_a2d9fc66f26284f6ab90f79a4d7aef6d7"></a>
<a id="astructmqtt__client_html_a41cc1d3c5e5180af1d6376f88598678a"></a>
<a id="astructmqtt__client_html_a44c515b8b25d59554990f6193217d83f"></a>
<a id="astructmqtt__client_html_a485855e9b09d0c48fb09c5673f38b5ee"></a>
<a id="astructmqtt__client_html_a4b23a72831697b78dc4019a4b6ac97e4"></a>
<a id="astructmqtt__client_html_a4c456f4065e3bc20752d908f2d805667"></a>
<a id="astructmqtt__client_html_a63e3c1b470a7de9d179b1c0686504a68"></a>
<a id="astructmqtt__client_html_a66335741e991a2985ab5d4d7765651d2"></a>
<a id="astructmqtt__client_html_a6700818bb78880e8b10878f31680f3d3"></a>
<a id="astructmqtt__client_html_a67f76cd0feadf8ae11ed232dcc9ac1d1"></a>
<a id="astructmqtt__client_html_a726f5a806458d7dc9d6072dff74508fc"></a>
<a id="astructmqtt__client_html_a72d61d9c0e717010ff90c2ed7fcddf5c"></a>
<a id="astructmqtt__client_html_a7f4e9547b1d91edf21589334db711499"></a>
<a id="astructmqtt__client_html_a89ce07fe536a502c051e4082b708155e"></a>
<a id="astructmqtt__client_html_a8c48cec6d0f895d05a8f933240348818"></a>
<a id="astructmqtt__client_html_a9f63fb54f8557135c1aa38a60bb7053c"></a>
<a id="astructmqtt__client_html_aa65a4af5952634e4ff5c4bf700ccccd7"></a>
<a id="astructmqtt__client_html_aabd419115c8637e4e4c0e6d23a5a984d"></a>
<a id="astructmqtt__client_html_aac856189cedecf059f4ba723b06edda6"></a>
<a id="astructmqtt__client_html_aae9ecb0faf8dc4337579e0713d065184"></a>
<a id="astructmqtt__client_html_ab271f2061fe3c9e3c1a76158a1c00449"></a>
<a id="astructmqtt__client_html_abdf2c45264ba77d584655b0cb6562c6b"></a>
<a id="astructmqtt__client_html_ac31a2ea9d67886f83fd3af88f33f36d9"></a>
<a id="astructmqtt__client_html_ac6c53bf95f311a4df29d7db5f4c20b45"></a>
<a id="astructmqtt__client_html_ac899284f06f581cac0b647381c757287"></a>
<a id="astructmqtt__client_html_ac96879e15ccd829fbcf9b88913161c0d"></a>
<a id="astructmqtt__client_html_ae46c6695e9dfbf13cb895d8acad12d58"></a>
<a id="astructmqtt__client_html_ae582274bf396caa0a3427f1aeace639c"></a>
<a id="astructmqtt__client_html_aef6da1db6f600a2bfd1c7dd0d78d1b6d"></a>
<a id="astructmqtt__client_html_afe138435d59720cc2c8c4b2756134a49"></a>
<a id="astructmqtt__common__ack__properties_html"></a>
<a id="astructmqtt__common__ack__properties_html_a282e39c4e3bdcebf331969fdf0a60570"></a>
<a id="astructmqtt__common__ack__properties_html_a69d6a6795e309cb64bff1dd3eeb698c6"></a>
<a id="astructmqtt__common__ack__properties_html_a87c543e4eb14b9e1e1fbd9fe7d4b047b"></a>
<a id="astructmqtt__common__ack__properties_html_aa827f37cfc537e00e8ff4e774ec9b835"></a>
<a id="astructmqtt__common__ack__properties_html_abf672bc44df434fe2dd4f519343d6480"></a>
<a id="astructmqtt__connack__param_html"></a>
<a id="astructmqtt__connack__param_html_a0426044dfe84d5160d1116018265eda3"></a>
<a id="astructmqtt__connack__param_html_a09cdb8430a3ced98055b564716201bf1"></a>
<a id="astructmqtt__connack__param_html_a0d11efb926df6a0d65e879fee878bda0"></a>
<a id="astructmqtt__connack__param_html_a0f02175c92a22ad05f370dd944ad6b1a"></a>
<a id="astructmqtt__connack__param_html_a0f03ee47ace97ccaa841df5353e49f26"></a>
<a id="astructmqtt__connack__param_html_a1314e5735f128b905bd3d78beaee956e"></a>
<a id="astructmqtt__connack__param_html_a1802487e00937da8e4261083b7229219"></a>
<a id="astructmqtt__connack__param_html_a1c37aaf9f6cde9f251b79af7144a099e"></a>
<a id="astructmqtt__connack__param_html_a29eed1a34902519380aa59757bde501c"></a>
<a id="astructmqtt__connack__param_html_a351717d25bf8bc2d915506b5bc354214"></a>
<a id="astructmqtt__connack__param_html_a3a21965017d0e9d15ed046eb0cfb461f"></a>
<a id="astructmqtt__connack__param_html_a3a6f8b9f79f81c34bda7aca99fa0682f"></a>
<a id="astructmqtt__connack__param_html_a3a7a8a6dbef8d5026717b98b4e949c4e"></a>
<a id="astructmqtt__connack__param_html_a43ada81fd7746aab783a0d1cb4d4d645"></a>
<a id="astructmqtt__connack__param_html_a4d1b50d148189053879ec80aa2688a2b"></a>
<a id="astructmqtt__connack__param_html_a4f8092dc562fe27396c21e1329e19262"></a>
<a id="astructmqtt__connack__param_html_a54ae953abeec2d31e7c82869302b492e"></a>
<a id="astructmqtt__connack__param_html_a5fbdc09eff6fef2f06a98c8f9faf0a03"></a>
<a id="astructmqtt__connack__param_html_a6d7423e5c7234e97f79db2dd9e592d85"></a>
<a id="astructmqtt__connack__param_html_a7134eddbb0d497c6cfe85b6fcfc9efa1"></a>
<a id="astructmqtt__connack__param_html_a78dad1593aaa64c27263cafc61791a03"></a>
<a id="astructmqtt__connack__param_html_a7df963cce8b5ba99efe9888f742fad4f"></a>
<a id="astructmqtt__connack__param_html_a7e47864579e36ea469d198ceb9cdd3f4"></a>
<a id="astructmqtt__connack__param_html_a7f275e22d6cdf808b1f0a19c3f78f517"></a>
<a id="astructmqtt__connack__param_html_a80932b53f13d5cb5c299f384c176e1af"></a>
<a id="astructmqtt__connack__param_html_a8e5cab6b3479fc9e902feb622008386a"></a>
<a id="astructmqtt__connack__param_html_a9c400f66c3a7eade5df879b328f4cb42"></a>
<a id="astructmqtt__connack__param_html_a9eecd31595fa1332a1cf4b661cedeae2"></a>
<a id="astructmqtt__connack__param_html_aae7a54dd6f62887b618f652f260ed6bd"></a>
<a id="astructmqtt__connack__param_html_ab123a8236804082667ad93ddd7e40e7a"></a>
<a id="astructmqtt__connack__param_html_abbd4490c94846009f79c741e3067c743"></a>
<a id="astructmqtt__connack__param_html_ac3815c5ecaaeb8cea860ccd75f1d460a"></a>
<a id="astructmqtt__connack__param_html_ac3f6a6b22fcf1ed55dc46d4b9b2079e6"></a>
<a id="astructmqtt__connack__param_html_ad45d67943848406b290fee98e5d4d3ba"></a>
<a id="astructmqtt__connack__param_html_ae2c5b667e0e050611791160c8b7755ef"></a>
<a id="astructmqtt__connack__param_html_af0810d9762a46f0ac7376becb631a9f7"></a>
<a id="astructmqtt__connack__param_html_af21ff08751c63f17423500c33191fcdf"></a>
<a id="astructmqtt__connack__param_html_af2655b3164805704e68d8ed69621a168"></a>
<a id="astructmqtt__disconnect__param_html"></a>
<a id="astructmqtt__disconnect__param_html_a02b38f24432c8def5dcda439bc8e9ab7"></a>
<a id="astructmqtt__disconnect__param_html_a03050c6d4879f0d0eb62093b340bb99c"></a>
<a id="astructmqtt__disconnect__param_html_a2360cc037d244abed416ace079f82257"></a>
<a id="astructmqtt__disconnect__param_html_a6fb48a1ddf15d525f13f979758a06132"></a>
<a id="astructmqtt__disconnect__param_html_a7a3b72acdd5a2d239c9e3d78e59bb4c2"></a>
<a id="astructmqtt__disconnect__param_html_a8891e52deb9c40f4f838f1df67db9794"></a>
<a id="astructmqtt__disconnect__param_html_a9a0531c1fb9b95019bb49f1642d54b07"></a>
<a id="astructmqtt__disconnect__param_html_aa1b60dae11e0cad827e2d9942c1137e4"></a>
<a id="astructmqtt__disconnect__param_html_aa211770e88640378928e3ed3d09c23ac"></a>
<a id="astructmqtt__disconnect__param_html_aa44656e2663a058070a3d30e3bdabee9"></a>
<a id="astructmqtt__disconnect__param_html_ae2077e489cf38f4bccfebb78a840b9fe"></a>
<a id="astructmqtt__evt_html"></a>
<a id="astructmqtt__evt_html_a79d7a198d8ed9959bb7aae835b6301c2"></a>
<a id="astructmqtt__evt_html_aa1a4304d4aa70440ba630f3fe5e76d2f"></a>
<a id="astructmqtt__evt_html_aca1085171667c46b2438f66d9227e07c"></a>
<a id="astructmqtt__internal_html"></a>
<a id="astructmqtt__internal_html_a45aeafd71dadaf1d0fd0bc3969c921de"></a>
<a id="astructmqtt__internal_html_a897895965adaf781b3a426dd53da10a2"></a>
<a id="astructmqtt__internal_html_a8f30cb1440efecf8ae8fc448e4f462f8"></a>
<a id="astructmqtt__internal_html_a921477a9839447f4fe1c823911680c92"></a>
<a id="astructmqtt__internal_html_acf93a973de5a5430e767e2996f1cd048"></a>
<a id="astructmqtt__internal_html_ad41631ca4fbbae32e0a7042515c90ea9"></a>
<a id="astructmqtt__internal_html_af866a252b9e18496c8e1627704d8a8b2"></a>
<a id="astructmqtt__puback__param_html"></a>
<a id="astructmqtt__puback__param_html_a44307fc6b172729478f1d097bbaf34bb"></a>
<a id="astructmqtt__puback__param_html_a5fbbc6613660883a96aa37c8def6baa5"></a>
<a id="astructmqtt__puback__param_html_a727b919b853e77e480fb841e74a2dedf"></a>
<a id="astructmqtt__pubcomp__param_html"></a>
<a id="astructmqtt__pubcomp__param_html_a1e38cde0e4e18b091e893bf207fa6c6d"></a>
<a id="astructmqtt__pubcomp__param_html_a4e969aeee8c66a10e23731f8fe74db93"></a>
<a id="astructmqtt__pubcomp__param_html_ae8484ad4d62f953ecace6c990002e316"></a>
<a id="astructmqtt__publish__message_html"></a>
<a id="astructmqtt__publish__message_html_a6cfed92c8f8fb319d3cbf40b956cb94d"></a>
<a id="astructmqtt__publish__message_html_acf5dba605db61efe68ec29337eea95e9"></a>
<a id="astructmqtt__publish__param_html"></a>
<a id="astructmqtt__publish__param_html_a00413022cecf2a624506ab5da630aefa"></a>
<a id="astructmqtt__publish__param_html_a13bf77403471f79687fe63a93cd1627d"></a>
<a id="astructmqtt__publish__param_html_a2c2062c2b3ad027d5dfea56cb81c48e7"></a>
<a id="astructmqtt__publish__param_html_a36a4d07ed13c5d4befc51a6285606090"></a>
<a id="astructmqtt__publish__param_html_a4190ccdfbf97a4ef63121e6a841d5f79"></a>
<a id="astructmqtt__publish__param_html_a4a486b254bd8e0f081251f8ca087e9d2"></a>
<a id="astructmqtt__publish__param_html_a599f8830ef4b42a68955ad58411ef0f1"></a>
<a id="astructmqtt__publish__param_html_a5e4b146a69c82fa36fd43adb8658ef5f"></a>
<a id="astructmqtt__publish__param_html_a5e87084f72285ebdf5d26aca0eed6f00"></a>
<a id="astructmqtt__publish__param_html_a5edb680fe44b795b02e35fcb73b98efa"></a>
<a id="astructmqtt__publish__param_html_a63e9311cf0acf33386ceb8328b040d2a"></a>
<a id="astructmqtt__publish__param_html_a813b18b4c859fb5e703d90fc8eb9bd2e"></a>
<a id="astructmqtt__publish__param_html_a85e5a3a9c7347c506780627515dc84ea"></a>
<a id="astructmqtt__publish__param_html_a8d9905f31bfc9072516f00082eda9c50"></a>
<a id="astructmqtt__publish__param_html_a8f76494a04d91150aee2ed7e9a271243"></a>
<a id="astructmqtt__publish__param_html_a9841a4fbb30b597a9710863ce6034688"></a>
<a id="astructmqtt__publish__param_html_a9b2c6fad5bf830276d8d3f6b5ab04210"></a>
<a id="astructmqtt__publish__param_html_aab2664e89f086b62b9af5cd481fccde3"></a>
<a id="astructmqtt__publish__param_html_aac4c6ba605506c183d2d5bdd7e550b3e"></a>
<a id="astructmqtt__publish__param_html_aafc5473b88a64df887751903314f0fac"></a>
<a id="astructmqtt__publish__param_html_ab98e52ae704c6e988d554cf388b2ec0c"></a>
<a id="astructmqtt__pubrec__param_html"></a>
<a id="astructmqtt__pubrec__param_html_a4d52112e88d954a88e4c65c9be5b0b93"></a>
<a id="astructmqtt__pubrec__param_html_ab0f92884dbd6e63894210ff7f57fe62c"></a>
<a id="astructmqtt__pubrec__param_html_acf7d23d86fa5a7d935711459e52b092d"></a>
<a id="astructmqtt__pubrel__param_html"></a>
<a id="astructmqtt__pubrel__param_html_a4333fba7ac37d5a68fe921453b56b572"></a>
<a id="astructmqtt__pubrel__param_html_a4e2c97c37bc4c43fd4a63391372dfed3"></a>
<a id="astructmqtt__pubrel__param_html_a8fe8b7921add0b5fa2926a9eec68d102"></a>
<a id="astructmqtt__sec__config_html"></a>
<a id="astructmqtt__sec__config_html_a0e04768b6589823464c2d13c31230cad"></a>
<a id="astructmqtt__sec__config_html_a179a97d56a7a12d5afb60257a67ce46c"></a>
<a id="astructmqtt__sec__config_html_a25415e32e00808fb6a24187f4234059f"></a>
<a id="astructmqtt__sec__config_html_a5beac5704fec3e399e5c0099a57ce115"></a>
<a id="astructmqtt__sec__config_html_a6d59afc061a749ea31f5bd415918a3e0"></a>
<a id="astructmqtt__sec__config_html_a9bfafa25c9054fa0389927c72da60587"></a>
<a id="astructmqtt__sec__config_html_adeb8630a9e73c4b3226afa1c9a5060fe"></a>
<a id="astructmqtt__sec__config_html_af7a0ee827bf98fde264000f4c9020c15"></a>
<a id="astructmqtt__suback__param_html"></a>
<a id="astructmqtt__suback__param_html_a5f0eff81eef7d9dc0767addea0782bf5"></a>
<a id="astructmqtt__suback__param_html_a94ef5183aa3438db0521f445650c5868"></a>
<a id="astructmqtt__suback__param_html_a985b53444e7b2c10ab68844fcee34ee4"></a>
<a id="astructmqtt__subscription__list_html"></a>
<a id="astructmqtt__subscription__list_html_a0667dcd4bd5eb5fe1b13b4df1bf2c26f"></a>
<a id="astructmqtt__subscription__list_html_a314f91139b4a837b173a6a930c3bdc6b"></a>
<a id="astructmqtt__subscription__list_html_a677b9c49972b6d6ade2dd934c8518cc9"></a>
<a id="astructmqtt__subscription__list_html_a9736f9d14db3097c2081e81e765a60ec"></a>
<a id="astructmqtt__subscription__list_html_a97fefa83de8657d85b0f76013ca1f222"></a>
<a id="astructmqtt__subscription__list_html_aa44e0af3526ee0424627bb24a90ea6b1"></a>
<a id="astructmqtt__topic__alias_html"></a>
<a id="astructmqtt__topic__alias_html_aed7c3e3306dd3bf97073ca6b7f9c4902"></a>
<a id="astructmqtt__topic__alias_html_af056af89763a7d39f513759dd1f7e8a7"></a>
<a id="astructmqtt__topic_html"></a>
<a id="astructmqtt__topic_html_a52fbe1b4b5c793be0cad004829d57faa"></a>
<a id="astructmqtt__topic_html_a780e90d62c094557bd3918de3b3921e6"></a>
<a id="astructmqtt__topic_html_ab859d08baf88e6a1ac5135e1e55158d5"></a>
<a id="astructmqtt__topic_html_adce01c71f9b31f4ac0916ed1b8628fd4"></a>
<a id="astructmqtt__topic_html_afb71b709d04a1a2caf5acb2200f3bfaa"></a>
<a id="astructmqtt__transport_html"></a>
<a id="astructmqtt__transport_html_a3b4589dd05394589e7af460761b800bf"></a>
<a id="astructmqtt__transport_html_a47b49927c79e67b202112c68b53d83f4"></a>
<a id="astructmqtt__transport_html_a7cfdf50105a275612dbda28e7c02808e"></a>
<a id="astructmqtt__transport_html_af65e3f0284ba9d881c5b916749f097b2"></a>
<a id="astructmqtt__unsuback__param_html"></a>
<a id="astructmqtt__unsuback__param_html_a543fb60386725e9096bb0243beaa1181"></a>
<a id="astructmqtt__unsuback__param_html_a992c0c038413377c8edd701d2ef8455e"></a>
<a id="astructmqtt__unsuback__param_html_aa453177181e07cd0532b8cf591be0f32"></a>
<a id="astructmqtt__utf8__pair_html"></a>
<a id="astructmqtt__utf8__pair_html_a749e0afc65c06917ca2881b51c0c6763"></a>
<a id="astructmqtt__utf8__pair_html_aedea0e9eb2526c8e0da2319017427c2f"></a>
<a id="astructmqtt__utf8_html"></a>
<a id="astructmqtt__utf8_html_a2376f943335326dae74c798141326b70"></a>
<a id="astructmqtt__utf8_html_a69a949e3c9cb1794f8d28091601eba16"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructsys__mutex_html"></a>
<a id="atls__credentials_8h_html"></a>
<a id="aunionmqtt__evt__param_html"></a>
<a id="aunionmqtt__evt__param_html_a2269e07f580fb65df5f3d0832aa6b3af"></a>
<a id="aunionmqtt__evt__param_html_a24bf756db9fa8cc67c0b02c4e2cb602c"></a>
<a id="aunionmqtt__evt__param_html_a3b31e1d94c480b8d0244cc12d1c25524"></a>
<a id="aunionmqtt__evt__param_html_a41be40873e1ebb9bf6fbf6dc9566d6ff"></a>
<a id="aunionmqtt__evt__param_html_a6967703ed8a9f58eda8e9a94b5bc1f5f"></a>
<a id="aunionmqtt__evt__param_html_aa99a77bbade75b3f450088b32131f87a"></a>
<a id="aunionmqtt__evt__param_html_ac3d564095019ccf57c10678a433bc31a"></a>
<a id="aunionmqtt__evt__param_html_ad040b028ed0aaabcaddedc204fb709d8"></a>
<a id="aunionmqtt__evt__param_html_ad1bb0a46bab0442404e22627bcc6a0ef"></a>
<a id="aunionmqtt__evt__param_html_af6ce2426884d2faa443b3dfdaa45594c"></a>
<a id="awebsocket_8h_html"></a>

```c
/*
 * Copyright (c) 2018 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_MQTT_H_
#define ZEPHYR_INCLUDE_NET_MQTT_H_

#include <stddef.h>

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/net/tls_credentials.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/sys/mutex.h>
#include <zephyr/net/websocket.h>

#ifdef __cplusplus
extern "C" {
#endif

enum mqtt_evt_type {
        MQTT_EVT_CONNACK,

        MQTT_EVT_DISCONNECT,

        MQTT_EVT_PUBLISH,

        MQTT_EVT_PUBACK,

        MQTT_EVT_PUBREC,

        MQTT_EVT_PUBREL,

        MQTT_EVT_PUBCOMP,

        MQTT_EVT_SUBACK,

        MQTT_EVT_UNSUBACK,

        MQTT_EVT_PINGRESP,

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        MQTT_EVT_AUTH,
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

enum mqtt_version {
        MQTT_VERSION_3_1_0 = 3,
        MQTT_VERSION_3_1_1 = 4,
        MQTT_VERSION_5_0 = 5,
};

enum mqtt_qos {
        MQTT_QOS_0_AT_MOST_ONCE = 0x00,

        MQTT_QOS_1_AT_LEAST_ONCE = 0x01,

        MQTT_QOS_2_EXACTLY_ONCE  = 0x02
};

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
enum mqtt_retain_handling {
        MQTT_RH_0_SEND_AT_SUBSCRIBE = 0x00,

        MQTT_RH_1_SEND_IF_NEW = 0x01,

        MQTT_RH_2_DO_NOT_SEND = 0x02
};
#endif /* CONFIG_MQTT_VERSION_5_0 */

enum mqtt_conn_return_code {
        MQTT_CONNECTION_ACCEPTED                = 0x00,

        MQTT_UNACCEPTABLE_PROTOCOL_VERSION      = 0x01,

        MQTT_IDENTIFIER_REJECTED                = 0x02,

        MQTT_SERVER_UNAVAILABLE                 = 0x03,

        MQTT_BAD_USER_NAME_OR_PASSWORD          = 0x04,

        MQTT_NOT_AUTHORIZED                     = 0x05
};

enum mqtt_connack_reason_code {
        MQTT_CONNACK_SUCCESS = 0,
        MQTT_CONNACK_UNSPECIFIED_ERROR = 128,
        MQTT_CONNACK_MALFORMED_PACKET = 129,
        MQTT_CONNACK_PROTOCOL_ERROR = 130,
        MQTT_CONNACK_IMPL_SPECIFIC_ERROR = 131,
        MQTT_CONNACK_UNSUPPORTED_PROTO_ERROR = 132,
        MQTT_CONNACK_CLIENT_ID_NOT_VALID = 133,
        MQTT_CONNACK_BAD_USERNAME_OR_PASS = 134,
        MQTT_CONNACK_NOT_AUTHORIZED = 135,
        MQTT_CONNACK_SERVER_UNAVAILABLE = 136,
        MQTT_CONNACK_SERVER_BUSY = 137,
        MQTT_CONNACK_BANNED = 138,
        MQTT_CONNACK_BAD_AUTH_METHOD = 140,
        MQTT_CONNACK_TOPIC_NAME_INVALID = 144,
        MQTT_CONNACK_PACKET_TOO_LARGE = 149,
        MQTT_CONNACK_QUOTA_EXCEEDED = 151,
        MQTT_CONNACK_PAYLOAD_FORMAT_INVALID = 153,
        MQTT_CONNACK_RETAIN_NOT_SUPPORTED = 154,
        MQTT_CONNACK_QOS_NOT_SUPPORTED = 155,
        MQTT_CONNACK_USE_ANOTHER_SERVER = 156,
        MQTT_CONNACK_SERVER_MOVED = 157,
        MQTT_CONNACK_CONNECTION_RATE_EXCEEDED = 159,
};

enum mqtt_suback_return_code {
        MQTT_SUBACK_SUCCESS_QoS_0 = 0x00,

        MQTT_SUBACK_SUCCESS_QoS_1 = 0x01,

        MQTT_SUBACK_SUCCESS_QoS_2 = 0x02,

        MQTT_SUBACK_FAILURE = 0x80
};

enum mqtt_disconnect_reason_code {
        MQTT_DISCONNECT_NORMAL = 0,
        MQTT_DISCONNECT_WITH_WILL_MSG = 4,
        MQTT_DISCONNECT_UNSPECIFIED_ERROR = 128,
        MQTT_DISCONNECT_MALFORMED_PACKET = 129,
        MQTT_DISCONNECT_PROTOCOL_ERROR = 130,
        MQTT_DISCONNECT_IMPL_SPECIFIC_ERROR = 131,
        MQTT_DISCONNECT_NOT_AUTHORIZED = 135,
        MQTT_DISCONNECT_SERVER_BUSY = 137,
        MQTT_DISCONNECT_SERVER_SHUTTING_DOWN = 139,
        MQTT_DISCONNECT_KEEP_ALIVE_TIMEOUT = 141,
        MQTT_DISCONNECT_SESSION_TAKE_OVER = 142,
        MQTT_DISCONNECT_TOPIC_FILTER_INVALID = 143,
        MQTT_DISCONNECT_TOPIC_NAME_INVALID = 144,
        MQTT_DISCONNECT_RECV_MAX_EXCEEDED = 147,
        MQTT_DISCONNECT_TOPIC_ALIAS_INVALID = 148,
        MQTT_DISCONNECT_PACKET_TOO_LARGE = 149,
        MQTT_DISCONNECT_MESSAGE_RATE_TOO_HIGH = 150,
        MQTT_DISCONNECT_QUOTA_EXCEEDED = 151,
        MQTT_DISCONNECT_ADMIN_ACTION = 152,
        MQTT_DISCONNECT_PAYLOAD_FORMAT_INVALID = 153,
        MQTT_DISCONNECT_RETAIN_NOT_SUPPORTED = 154,
        MQTT_DISCONNECT_QOS_NOT_SUPPORTED = 155,
        MQTT_DISCONNECT_USE_ANOTHER_SERVER = 156,
        MQTT_DISCONNECT_SERVER_MOVED = 157,
        MQTT_DISCONNECT_SHARED_SUB_NOT_SUPPORTED = 158,
        MQTT_DISCONNECT_CONNECTION_RATE_EXCEEDED = 159,
        MQTT_DISCONNECT_MAX_CONNECT_TIME = 160,
        MQTT_DISCONNECT_SUB_ID_NOT_SUPPORTED = 161,
        MQTT_DISCONNECT_WILDCARD_SUB_NOT_SUPPORTED = 162,
};

enum mqtt_auth_reason_code {
        MQTT_AUTH_SUCCESS = 0,
        MQTT_AUTH_CONTINUE_AUTHENTICATION = 24,
        MQTT_AUTH_RE_AUTHENTICATE = 25,
};

struct mqtt_utf8 {
        const uint8_t *utf8;
        uint32_t size;
};

#define MQTT_UTF8_LITERAL(literal)                              \
        ((struct mqtt_utf8) {literal, sizeof(literal) - 1})

struct mqtt_binstr {
        uint8_t *data;
        uint32_t len;
};

struct mqtt_topic_alias {
#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        uint8_t topic_buf[CONFIG_MQTT_TOPIC_ALIAS_STRING_MAX];

        uint16_t topic_size;
#elif defined(CONFIG_CPP)
        /* An empty struct is not valid C, and compilers that accept it give
         * it size 0 while C++ gives 1. Keep a byte so both languages agree.
         */
        uint8_t c;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_topic {
        struct mqtt_utf8 topic;

        uint8_t qos;
#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        uint8_t no_local;
        uint8_t retain_as_published;
        uint8_t retain_handling;
#endif
};

struct mqtt_utf8_pair {
        struct mqtt_utf8 name;
        struct mqtt_utf8 value;
};

struct mqtt_publish_message {
        struct mqtt_topic topic;
        struct mqtt_binstr payload;
};

struct mqtt_connack_param {
        uint8_t session_present_flag;

        uint8_t return_code;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        struct {
                struct mqtt_utf8_pair user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX];

                struct mqtt_utf8 assigned_client_id;

                struct mqtt_utf8 reason_string;

                struct mqtt_utf8 response_information;

                struct mqtt_utf8 server_reference;

                struct mqtt_utf8 auth_method;

                struct mqtt_binstr auth_data;

                uint32_t session_expiry_interval;

                uint32_t maximum_packet_size;

                uint16_t receive_maximum;

                uint16_t topic_alias_maximum;

                uint16_t server_keep_alive;

                uint8_t maximum_qos;

                uint8_t retain_available;

                uint8_t wildcard_sub_available;

                uint8_t subscription_ids_available;

                uint8_t shared_sub_available;

                struct {
                        bool has_session_expiry_interval;
                        bool has_receive_maximum;
                        bool has_maximum_qos;
                        bool has_retain_available;
                        bool has_maximum_packet_size;
                        bool has_assigned_client_id;
                        bool has_topic_alias_maximum;
                        bool has_reason_string;
                        bool has_user_prop;
                        bool has_wildcard_sub_available;
                        bool has_subscription_ids_available;
                        bool has_shared_sub_available;
                        bool has_server_keep_alive;
                        bool has_response_information;
                        bool has_server_reference;
                        bool has_auth_method;
                        bool has_auth_data;
                } rx;
        } prop;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_common_ack_properties {
#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        struct mqtt_utf8_pair user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX];

        struct mqtt_utf8 reason_string;

        struct {
                bool has_reason_string;
                bool has_user_prop;
        } rx;
#elif defined(CONFIG_CPP)
        /* An empty struct is not valid C, and compilers that accept it give
         * it size 0 while C++ gives 1. Keep a byte so both languages agree.
         */
        uint8_t c;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_puback_param {
        uint16_t message_id;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        uint8_t reason_code;

        struct mqtt_common_ack_properties prop;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_pubrec_param {
        uint16_t message_id;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        uint8_t reason_code;

        struct mqtt_common_ack_properties prop;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_pubrel_param {
        uint16_t message_id;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        uint8_t reason_code;

        struct mqtt_common_ack_properties prop;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_pubcomp_param {
        uint16_t message_id;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        uint8_t reason_code;

        struct mqtt_common_ack_properties prop;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_suback_param {
        uint16_t message_id;

        struct mqtt_binstr return_codes;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        struct mqtt_common_ack_properties prop;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_unsuback_param {
        uint16_t message_id;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        struct mqtt_binstr reason_codes;

        struct mqtt_common_ack_properties prop;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_publish_param {
        struct mqtt_publish_message message;

        uint16_t message_id;

        uint8_t dup_flag : 1;

        uint8_t retain_flag : 1;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        struct {
                struct mqtt_utf8_pair user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX];

                struct mqtt_utf8 response_topic;

                struct mqtt_binstr correlation_data;

                struct mqtt_utf8 content_type;

                uint32_t subscription_identifier[CONFIG_MQTT_SUBSCRIPTION_ID_PROPERTIES_MAX];

                uint32_t message_expiry_interval;

                uint16_t topic_alias;

                uint8_t payload_format_indicator;

                struct {
                        bool has_payload_format_indicator;
                        bool has_message_expiry_interval;
                        bool has_topic_alias;
                        bool has_response_topic;
                        bool has_correlation_data;
                        bool has_user_prop;
                        bool has_subscription_identifier;
                        bool has_content_type;
                } rx;
        } prop;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_subscription_list {
        const struct mqtt_topic *list;

        uint16_t list_count;

        uint16_t message_id;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        struct {
                struct mqtt_utf8_pair user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX];

                uint32_t subscription_identifier;
        } prop;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_disconnect_param {
#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        /* MQTT 5.0 Disconnect reason code. */
        enum mqtt_disconnect_reason_code reason_code;

        struct {
                struct mqtt_utf8_pair user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX];

                struct mqtt_utf8 reason_string;

                struct mqtt_utf8 server_reference;

                uint32_t session_expiry_interval;

                struct {
                        bool has_session_expiry_interval;
                        bool has_reason_string;
                        bool has_user_prop;
                        bool has_server_reference;
                } rx;
        } prop;
#elif defined(CONFIG_CPP)
        /* An empty struct is not valid C, and compilers that accept it give
         * it size 0 while C++ gives 1. Keep a byte so both languages agree.
         */
        uint8_t c;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_auth_param {
#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        /* MQTT 5.0, chapter 3.15.2.1 Authenticate Reason Code */
        enum mqtt_auth_reason_code reason_code;

        struct {
                struct mqtt_utf8_pair user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX];

                struct mqtt_utf8 auth_method;

                struct mqtt_binstr auth_data;

                struct mqtt_utf8 reason_string;

                struct {
                        bool has_auth_method;
                        bool has_auth_data;
                        bool has_reason_string;
                        bool has_user_prop;
                } rx;
        } prop;
#elif defined(CONFIG_CPP)
        /* An empty struct is not valid C, and compilers that accept it give
         * it size 0 while C++ gives 1. Keep a byte so both languages agree.
         */
        uint8_t c;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

union mqtt_evt_param {
        struct mqtt_connack_param connack;

        struct mqtt_publish_param publish;

        struct mqtt_puback_param puback;

        struct mqtt_pubrec_param pubrec;

        struct mqtt_pubrel_param pubrel;

        struct mqtt_pubcomp_param pubcomp;

        struct mqtt_suback_param suback;

        struct mqtt_unsuback_param unsuback;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        struct mqtt_disconnect_param disconnect;

        struct mqtt_auth_param auth;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_evt {
        enum mqtt_evt_type type;

        union mqtt_evt_param param;

        int result;
};

struct mqtt_client;

typedef void (*mqtt_evt_cb_t)(struct mqtt_client *client,
                              const struct mqtt_evt *evt);

struct mqtt_sec_config {
        int peer_verify;

        uint32_t cipher_count;

        const int *cipher_list;

        uint32_t sec_tag_count;

        const sec_tag_t *sec_tag_list;

#if defined(CONFIG_MQTT_LIB_TLS_USE_ALPN)
        const char **alpn_protocol_name_list;

        uint32_t alpn_protocol_name_count;
#endif

        const char *hostname;

        int cert_nocopy;

        bool set_native_tls;
};

enum mqtt_transport_type {
        MQTT_TRANSPORT_NON_SECURE,

#if defined(CONFIG_MQTT_LIB_TLS)
        MQTT_TRANSPORT_SECURE,
#endif /* CONFIG_MQTT_LIB_TLS */

#if defined(CONFIG_MQTT_LIB_WEBSOCKET)
        MQTT_TRANSPORT_NON_SECURE_WEBSOCKET,
#if defined(CONFIG_MQTT_LIB_TLS)
        MQTT_TRANSPORT_SECURE_WEBSOCKET,
#endif
#endif /* CONFIG_MQTT_LIB_WEBSOCKET */
#if defined(CONFIG_MQTT_LIB_CUSTOM_TRANSPORT)
        MQTT_TRANSPORT_CUSTOM,
#endif /* CONFIG_MQTT_LIB_CUSTOM_TRANSPORT */

        MQTT_TRANSPORT_NUM
};

struct mqtt_transport {
        enum mqtt_transport_type type;

        const char *if_name;

        union {
                struct {
                        int sock;
                } tcp;

#if defined(CONFIG_MQTT_LIB_TLS)
                struct {
                        int sock;

                        struct mqtt_sec_config config;
                } tls;
#endif /* CONFIG_MQTT_LIB_TLS */
        };

#if defined(CONFIG_MQTT_LIB_WEBSOCKET)
        struct {
                struct websocket_request config;

                int sock;

                int32_t timeout;
        } websocket;
#endif

#if defined(CONFIG_MQTT_LIB_CUSTOM_TRANSPORT)
        void *custom_transport_data;
#endif /* CONFIG_MQTT_LIB_CUSTOM_TRANSPORT */

#if defined(CONFIG_SOCKS)
        struct {
                union {
                        struct net_sockaddr_storage addr_storage;
                        /* Use the addr_storage instead of this one. */
                        struct net_sockaddr addr;
                };
                net_socklen_t addrlen;
        } proxy;
#endif
};

struct mqtt_internal {
        struct sys_mutex mutex;

        uint32_t last_activity;

        uint32_t state;

        uint32_t rx_buf_datalen;

        uint32_t remaining_payload;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        struct mqtt_topic_alias topic_aliases[CONFIG_MQTT_TOPIC_ALIAS_MAX];

        enum mqtt_disconnect_reason_code disconnect_reason;
#endif /* CONFIG_MQTT_VERSION_5_0 */
};

struct mqtt_client {
        struct mqtt_internal internal;

        struct mqtt_transport transport;

        struct mqtt_utf8 client_id;

        const void *broker;

        struct mqtt_utf8 *user_name;

        struct mqtt_utf8 *password;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        struct {
                struct mqtt_utf8_pair user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX];

                struct mqtt_utf8 content_type;

                struct mqtt_utf8 response_topic;

                struct mqtt_binstr correlation_data;

                uint32_t will_delay_interval;

                uint32_t message_expiry_interval;

                uint8_t payload_format_indicator;
        } will_prop;
#endif /* CONFIG_MQTT_VERSION_5_0 */

        struct mqtt_topic *will_topic;

        struct mqtt_utf8 *will_message;

        mqtt_evt_cb_t evt_cb;

        uint8_t *rx_buf;

        uint32_t rx_buf_size;

        uint8_t *tx_buf;

        uint32_t tx_buf_size;

        uint16_t keepalive;

        uint8_t protocol_version;

        int8_t unacked_ping;

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
        struct {
                struct mqtt_utf8_pair user_prop[CONFIG_MQTT_USER_PROPERTIES_MAX];

                struct mqtt_utf8 auth_method;

                struct mqtt_binstr auth_data;

                uint32_t session_expiry_interval;

                uint32_t maximum_packet_size;

                uint16_t receive_maximum;

                bool request_response_info;

                bool request_problem_info;
        } prop;
#endif /* CONFIG_MQTT_VERSION_5_0 */

        uint8_t will_retain : 1;

        uint8_t clean_session : 1;

        void *user_data;
};

void mqtt_client_init(struct mqtt_client *client);

#if defined(CONFIG_SOCKS)
/*
 * @brief Set proxy server details
 *
 * @param[in] client Client instance for which the procedure is requested,
 *                   Shall not be NULL.
 * @param[in] proxy_addr Proxy server address.
 * @param[in] addrlen Proxy server address length.
 *
 * @return 0 or a negative error code (errno.h) indicating reason of failure.
 *
 * @note Must be called before calling mqtt_connect().
 */
int mqtt_client_set_proxy(struct mqtt_client *client,
                          struct net_sockaddr *proxy_addr,
                          net_socklen_t addrlen);
#endif

int mqtt_connect(struct mqtt_client *client);

int mqtt_publish(struct mqtt_client *client,
                 const struct mqtt_publish_param *param);

int mqtt_publish_qos1_ack(struct mqtt_client *client,
                          const struct mqtt_puback_param *param);

int mqtt_publish_qos2_receive(struct mqtt_client *client,
                              const struct mqtt_pubrec_param *param);

int mqtt_publish_qos2_release(struct mqtt_client *client,
                              const struct mqtt_pubrel_param *param);

int mqtt_publish_qos2_complete(struct mqtt_client *client,
                               const struct mqtt_pubcomp_param *param);

int mqtt_subscribe(struct mqtt_client *client,
                   const struct mqtt_subscription_list *param);

int mqtt_unsubscribe(struct mqtt_client *client,
                     const struct mqtt_subscription_list *param);

int mqtt_ping(struct mqtt_client *client);

int mqtt_disconnect(struct mqtt_client *client,
                    const struct mqtt_disconnect_param *param);

#if defined(CONFIG_MQTT_VERSION_5_0) || defined(__DOXYGEN__)
int mqtt_auth(struct mqtt_client *client, const struct mqtt_auth_param *param);
#endif /* CONFIG_MQTT_VERSION_5_0 */

int mqtt_abort(struct mqtt_client *client);

int mqtt_live(struct mqtt_client *client);

int mqtt_keepalive_time_left(const struct mqtt_client *client);

int mqtt_input(struct mqtt_client *client);

int mqtt_read_publish_payload(struct mqtt_client *client, void *buffer,
                              size_t length);

int mqtt_read_publish_payload_blocking(struct mqtt_client *client, void *buffer,
                                       size_t length);

int mqtt_readall_publish_payload(struct mqtt_client *client, uint8_t *buffer,
                                 size_t length);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_MQTT_H_ */

```

## 20.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 86 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 3：原第 132 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 4：原第 275 行

空结构体（Empty Struct）不符合 C 语言要求；接受空结构体的编译器会将其大小设为 0，而 C++ 将其大小设为 1。保留一个字节，使两种语言的结果一致。

### 注释 5：原第 279 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 6：原第 422 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 7：原第 442 行

空结构体（Empty Struct）不符合 C 语言要求；接受空结构体的编译器会将其大小设为 0，而 C++ 将其大小设为 1。保留一个字节，使两种语言的结果一致。

### 注释 8：原第 446 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 9：原第 460 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 10：原第 474 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 11：原第 488 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 12：原第 502 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 13：原第 520 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 14：原第 534 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 15：原第 604 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 16：原第 629 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 17：原第 635 行

MQTT 5.0 断开连接原因码（Disconnect Reason Code）。

### 注释 18：原第 665 行

空结构体（Empty Struct）不符合 C 语言要求；接受空结构体的编译器会将其大小设为 0，而 C++ 将其大小设为 1。保留一个字节，使两种语言的结果一致。

### 注释 19：原第 669 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 20：原第 675 行

MQTT 5.0，第 3.15.2.1 节：认证原因码（Authenticate Reason Code）。

### 注释 21：原第 704 行

空结构体（Empty Struct）不符合 C 语言要求；接受空结构体的编译器会将其大小设为 0，而 C++ 将其大小设为 1。保留一个字节，使两种语言的结果一致。

### 注释 22：原第 708 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 23：原第 751 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 24：原第 831 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_LIB_TLS`。

### 注释 25：原第 840 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_LIB_WEBSOCKET`。

### 注释 26：原第 844 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_LIB_CUSTOM_TRANSPORT`。

### 注释 27：原第 884 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_LIB_TLS`。

### 注释 28：原第 904 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_LIB_CUSTOM_TRANSPORT`。

### 注释 29：原第 913 行

请改用 `addr_storage`，不要使用此成员。

### 注释 30：原第 947 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 31：原第 1004 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 32：原第 1068 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 33：原第 1095 行

设置代理服务器详情（Proxy Server Details）。

- 输入参数 `client`：请求执行此过程的客户端实例（Client Instance），不得为 `NULL`。
- 输入参数 `proxy_addr`：代理服务器地址（Proxy Server Address）。
- 输入参数 `addrlen`：代理服务器地址长度（Address Length）。

返回（`@return`）：0，或 `errno.h` 中表示失败原因的负错误码（Negative Error Code）。

注意（`@note`）：必须在调用 `mqtt_connect()` 之前调用。

### 注释 34：原第 1263 行

条件编译配置（Configuration）标记：`CONFIG_MQTT_VERSION_5_0`。

### 注释 35：原第 1373 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_MQTT_H_`。

## 20.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/net/tls_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/sys/mutex.h](../userspace_sync_reference/P005_用户模式互斥量头文件参考.md)
- [zephyr/net/websocket.h](https://docs.zephyrproject.org/latest/doxygen/html/websocket_8h.html)
- [mqtt_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga0071fe013b9920711456ef51cc3e6d91)
- [MQTT_EVT_CONNACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3)
- [MQTT_EVT_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032)
- [MQTT_EVT_PUBLISH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9)
- [MQTT_EVT_PUBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de)
- [MQTT_EVT_PUBREC](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87)
- [MQTT_EVT_PUBREL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2)
- [MQTT_EVT_PUBCOMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8)
- [MQTT_EVT_SUBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb)
- [MQTT_EVT_UNSUBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2)
- [MQTT_EVT_PINGRESP](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5)
- [MQTT_EVT_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga0071fe013b9920711456ef51cc3e6d91a4c5645869d17a4f9391999bfb6bbccde)
- [mqtt_version](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga90d152a4b0986e9a07a12c7c56f5e2a0)
- [MQTT_VERSION_3_1_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7)
- [MQTT_VERSION_3_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e)
- [MQTT_VERSION_5_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga90d152a4b0986e9a07a12c7c56f5e2a0a6f11ad8ae7114d8c1fdf85bda376b97f)
- [mqtt_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga396015e492b0fee8da37c7168d9cdb33)
- [MQTT_QOS_0_AT_MOST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e)
- [MQTT_QOS_1_AT_LEAST_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d)
- [MQTT_QOS_2_EXACTLY_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117)
- [mqtt_retain_handling](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga25ba4f0870fc2c01ee5fc2c06bd898c8)
- [MQTT_RH_0_SEND_AT_SUBSCRIBE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga25ba4f0870fc2c01ee5fc2c06bd898c8a804e0f2d820fbc89f83d02fa50b9a8fc)
- [MQTT_RH_1_SEND_IF_NEW](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga25ba4f0870fc2c01ee5fc2c06bd898c8a359c9c2a716d046a74961ca9012f921d)
- [MQTT_RH_2_DO_NOT_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gga25ba4f0870fc2c01ee5fc2c06bd898c8a1cd3179b4d1d791dbc9f0c99319603c4)
- [mqtt_conn_return_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaa17b38ed9c7e65f3e01ad906b24bb618)
- [MQTT_CONNECTION_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050)
- [MQTT_UNACCEPTABLE_PROTOCOL_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744)
- [MQTT_IDENTIFIER_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141)
- [MQTT_SERVER_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3)
- [MQTT_BAD_USER_NAME_OR_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134)
- [MQTT_NOT_AUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb)
- [mqtt_connack_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gae4c3fb5313addb72961ff578113d183a)
- [MQTT_CONNACK_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aabd738258dd4eaabe5c4ebb4bcf69e5d7)
- [MQTT_CONNACK_UNSPECIFIED_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa19f93ee28b2b6841289fade02c351989)
- [MQTT_CONNACK_MALFORMED_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa04de5af39cb78ef43bb4c8e701287ed0)
- [MQTT_CONNACK_PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa1fd45d6623840524c7af93a4725025cc)
- [MQTT_CONNACK_IMPL_SPECIFIC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa3819f991bd83ec9b4bf55754f7ef93ee)
- [MQTT_CONNACK_UNSUPPORTED_PROTO_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa2d5037f830538b73ea342bcdc24a9816)
- [MQTT_CONNACK_CLIENT_ID_NOT_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aafe38d9cabe4bee5f3f28484a58c5137f)
- [MQTT_CONNACK_BAD_USERNAME_OR_PASS](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa7ac5fefe2b6c3e7946dc84628fd560bd)
- [MQTT_CONNACK_NOT_AUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa83ec9ee9dfb3f649d06cf4d5f527ae4e)
- [MQTT_CONNACK_SERVER_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa76a813a52ed0d4f53b2646176b2fb5aa)
- [MQTT_CONNACK_SERVER_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa30546ae5648049fb5c14161b5ae42aa8)
- [MQTT_CONNACK_BANNED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa5838075a9ed66476838a3fcda7eeba33)
- [MQTT_CONNACK_BAD_AUTH_METHOD](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aafae37cc54cb28707b473d20f53c335d4)
- [MQTT_CONNACK_TOPIC_NAME_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa6fc0c79bac3ec08435fbaec3f80a2eb5)
- [MQTT_CONNACK_PACKET_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa930dc7b029c625730377653165736040)
- [MQTT_CONNACK_QUOTA_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aaa9386156438b2f5b71d57324c54c5f7f)
- [MQTT_CONNACK_PAYLOAD_FORMAT_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa8ded9dc2d24ca21f67e97217047f876c)
- [MQTT_CONNACK_RETAIN_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aab152dc910d3c55de3b64f0ac22611956)
- [MQTT_CONNACK_QOS_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa75f011e782a11c1c594848daf63e2fb0)
- [MQTT_CONNACK_USE_ANOTHER_SERVER](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aaf5a1f0040353625ff72dee52fb13f75c)
- [MQTT_CONNACK_SERVER_MOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aa8eda2ef9f0e7cc719169370e2cdcf8fa)
- [MQTT_CONNACK_CONNECTION_RATE_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggae4c3fb5313addb72961ff578113d183aae84b943ac946b53a1df9ec409746274e)
- [mqtt_suback_return_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaca1e61c8b14b75544e253cea355274a8)
- [MQTT_SUBACK_SUCCESS_QoS_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01)
- [MQTT_SUBACK_SUCCESS_QoS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c)
- [MQTT_SUBACK_SUCCESS_QoS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b)
- [MQTT_SUBACK_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7)
- [mqtt_disconnect_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaaf563f26ca66841145643a657119d780)
- [MQTT_DISCONNECT_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ac1db368d96389b585530954a493bcf9a)
- [MQTT_DISCONNECT_WITH_WILL_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780adc4c0e7ee2f8a1ab654f23b8355b878b)
- [MQTT_DISCONNECT_UNSPECIFIED_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ad9f253248e9fecaae14ee37f0c02d87c)
- [MQTT_DISCONNECT_MALFORMED_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780abbca5c088ca0392dca55c87469c571fa)
- [MQTT_DISCONNECT_PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780aad7106c041af27373d4e3b87faddafec)
- [MQTT_DISCONNECT_IMPL_SPECIFIC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a27eb2c713ee9957075da608d1da6ce6c)
- [MQTT_DISCONNECT_NOT_AUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a4d5c4ec55ee517078c47c59d81fadc78)
- [MQTT_DISCONNECT_SERVER_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ae3d9774a0f77be21b670512eb4a40b86)
- [MQTT_DISCONNECT_SERVER_SHUTTING_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a625f16227444f6f306de49aa953acd9d)
- [MQTT_DISCONNECT_KEEP_ALIVE_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780af4b7253dac64f072945054d02d9c2603)
- [MQTT_DISCONNECT_SESSION_TAKE_OVER](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a11c5eb260bb0d16faeca565aef4f79cf)
- [MQTT_DISCONNECT_TOPIC_FILTER_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a9e863b1f7632caa83efdb41f742f7c6a)
- [MQTT_DISCONNECT_TOPIC_NAME_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a053e8c2e553308869a31582cd85d1610)
- [MQTT_DISCONNECT_RECV_MAX_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a55857c640fa90478873eed61a27fa2c0)
- [MQTT_DISCONNECT_TOPIC_ALIAS_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a2421954cb46644bc942827fdeb21cb9c)
- [MQTT_DISCONNECT_PACKET_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a3639eb9318092b7c642001133e21158b)
- [MQTT_DISCONNECT_MESSAGE_RATE_TOO_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ab86eac24ac0829257a1b11c8b82e8194)
- [MQTT_DISCONNECT_QUOTA_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ac6db698ae6e2d24b480997adcff7e1a5)
- [MQTT_DISCONNECT_ADMIN_ACTION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ace998d2c989d41195d40dda31cf19173)
- [MQTT_DISCONNECT_PAYLOAD_FORMAT_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780afb77e6ac6da08c7d21f093c6068bdd5a)
- [MQTT_DISCONNECT_RETAIN_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780acfd3c3a5b146ed10efb32cd7c6e0cb65)
- [MQTT_DISCONNECT_QOS_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a70754dd31cc50ca8963ecedf52087a0d)
- [MQTT_DISCONNECT_USE_ANOTHER_SERVER](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a34cce9b17d556ca9d93d01302ec079e6)
- [MQTT_DISCONNECT_SERVER_MOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780adf78c69bb559f2b471ecdf4380fe21d1)
- [MQTT_DISCONNECT_SHARED_SUB_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a0cdcb8aed8cf188a50ca6094f3280f98)
- [MQTT_DISCONNECT_CONNECTION_RATE_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780ab418f144f1509e91332486a6f4ee9293)
- [MQTT_DISCONNECT_MAX_CONNECT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780af95f658c0b71d44c6aab3dc3b01ac00c)
- [MQTT_DISCONNECT_SUB_ID_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a9d383cae65f31d61bdcf1e38db92bbc4)
- [MQTT_DISCONNECT_WILDCARD_SUB_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaaf563f26ca66841145643a657119d780a82b2e5d2b8358fe893d5c682093d13c4)
- [mqtt_auth_reason_code](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gacdbeff0450bbcd438cdf35cd543fc6d6)
- [MQTT_AUTH_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggacdbeff0450bbcd438cdf35cd543fc6d6a609d75c1d9d37d5340ac979c924efa60)
- [MQTT_AUTH_CONTINUE_AUTHENTICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggacdbeff0450bbcd438cdf35cd543fc6d6add4e38c81c8e1a8b79d911c87612f863)
- [MQTT_AUTH_RE_AUTHENTICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggacdbeff0450bbcd438cdf35cd543fc6d6a46e6b7c5ae59f315137cf0df3aec816a)
- [mqtt_utf8](../network_application_model_reference/P079_mqtt_utf8_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [utf8](../network_application_model_reference/P079_mqtt_utf8_结构体.md#a69a949e3c9cb1794f8d28091601eba16)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [size](../network_application_model_reference/P079_mqtt_utf8_结构体.md#a2376f943335326dae74c798141326b70)
- [mqtt_binstr](../network_application_model_reference/P053_mqtt_binstr_结构体.md)
- [data](../network_application_model_reference/P053_mqtt_binstr_结构体.md#a1f61872edd09941155f60a242e582ff7)
- [len](../network_application_model_reference/P053_mqtt_binstr_结构体.md#abcc36b6c59c3da740a6b352fe846fd5f)
- [mqtt_topic_alias](../network_application_model_reference/P076_mqtt_topic_alias_结构体.md)
- [topic_buf](../network_application_model_reference/P076_mqtt_topic_alias_结构体.md#af056af89763a7d39f513759dd1f7e8a7)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [topic_size](../network_application_model_reference/P076_mqtt_topic_alias_结构体.md#aed7c3e3306dd3bf97073ca6b7f9c4902)
- [mqtt_topic](../network_application_model_reference/P075_mqtt_topic_结构体.md)
- [topic](../network_application_model_reference/P075_mqtt_topic_结构体.md#ab859d08baf88e6a1ac5135e1e55158d5)
- [qos](../network_application_model_reference/P075_mqtt_topic_结构体.md#a780e90d62c094557bd3918de3b3921e6)
- [no_local](../network_application_model_reference/P075_mqtt_topic_结构体.md#adce01c71f9b31f4ac0916ed1b8628fd4)
- [retain_as_published](../network_application_model_reference/P075_mqtt_topic_结构体.md#afb71b709d04a1a2caf5acb2200f3bfaa)
- [retain_handling](../network_application_model_reference/P075_mqtt_topic_结构体.md#a52fbe1b4b5c793be0cad004829d57faa)
- [mqtt_utf8_pair](../network_application_model_reference/P080_mqtt_utf8_pair_结构体.md)
- [name](../network_application_model_reference/P080_mqtt_utf8_pair_结构体.md#aedea0e9eb2526c8e0da2319017427c2f)
- [value](../network_application_model_reference/P080_mqtt_utf8_pair_结构体.md#a749e0afc65c06917ca2881b51c0c6763)
- [mqtt_publish_message](../network_application_model_reference/P062_mqtt_publish_message_结构体.md)
- [topic](../network_application_model_reference/P062_mqtt_publish_message_结构体.md#acf5dba605db61efe68ec29337eea95e9)
- [payload](../network_application_model_reference/P062_mqtt_publish_message_结构体.md#a6cfed92c8f8fb319d3cbf40b956cb94d)
- [mqtt_connack_param](../network_application_model_reference/P056_mqtt_connack_param_结构体.md)
- [session_present_flag](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#ab123a8236804082667ad93ddd7e40e7a)
- [return_code](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#aae7a54dd6f62887b618f652f260ed6bd)
- [user_prop](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a29eed1a34902519380aa59757bde501c)
- [assigned_client_id](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a7f275e22d6cdf808b1f0a19c3f78f517)
- [reason_string](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a5fbdc09eff6fef2f06a98c8f9faf0a03)
- [response_information](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a1314e5735f128b905bd3d78beaee956e)
- [server_reference](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a0426044dfe84d5160d1116018265eda3)
- [auth_method](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#abbd4490c94846009f79c741e3067c743)
- [auth_data](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#ad45d67943848406b290fee98e5d4d3ba)
- [session_expiry_interval](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a7e47864579e36ea469d198ceb9cdd3f4)
- [maximum_packet_size](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a8e5cab6b3479fc9e902feb622008386a)
- [receive_maximum](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a9eecd31595fa1332a1cf4b661cedeae2)
- [topic_alias_maximum](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a09cdb8430a3ced98055b564716201bf1)
- [server_keep_alive](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#af21ff08751c63f17423500c33191fcdf)
- [maximum_qos](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a9c400f66c3a7eade5df879b328f4cb42)
- [retain_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#af0810d9762a46f0ac7376becb631a9f7)
- [wildcard_sub_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a1802487e00937da8e4261083b7229219)
- [subscription_ids_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#ac3815c5ecaaeb8cea860ccd75f1d460a)
- [shared_sub_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a3a21965017d0e9d15ed046eb0cfb461f)
- [has_session_expiry_interval](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#ae2c5b667e0e050611791160c8b7755ef)
- [has_receive_maximum](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a1c37aaf9f6cde9f251b79af7144a099e)
- [has_maximum_qos](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a0f02175c92a22ad05f370dd944ad6b1a)
- [has_retain_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a7df963cce8b5ba99efe9888f742fad4f)
- [has_maximum_packet_size](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a80932b53f13d5cb5c299f384c176e1af)
- [has_assigned_client_id](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#af2655b3164805704e68d8ed69621a168)
- [has_topic_alias_maximum](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#ac3f6a6b22fcf1ed55dc46d4b9b2079e6)
- [has_reason_string](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a4f8092dc562fe27396c21e1329e19262)
- [has_user_prop](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a4d1b50d148189053879ec80aa2688a2b)
- [has_wildcard_sub_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a3a6f8b9f79f81c34bda7aca99fa0682f)
- [has_subscription_ids_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a43ada81fd7746aab783a0d1cb4d4d645)
- [has_shared_sub_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a78dad1593aaa64c27263cafc61791a03)
- [has_server_keep_alive](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a0d11efb926df6a0d65e879fee878bda0)
- [has_response_information](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a0f03ee47ace97ccaa841df5353e49f26)
- [has_server_reference](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a351717d25bf8bc2d915506b5bc354214)
- [has_auth_method](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a7134eddbb0d497c6cfe85b6fcfc9efa1)
- [has_auth_data](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a6d7423e5c7234e97f79db2dd9e592d85)
- [rx](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a3a7a8a6dbef8d5026717b98b4e949c4e)
- [prop](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a54ae953abeec2d31e7c82869302b492e)
- [mqtt_common_ack_properties](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md)
- [user_prop](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md#aa827f37cfc537e00e8ff4e774ec9b835)
- [reason_string](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md#a282e39c4e3bdcebf331969fdf0a60570)
- [has_reason_string](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md#abf672bc44df434fe2dd4f519343d6480)
- [has_user_prop](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md#a69d6a6795e309cb64bff1dd3eeb698c6)
- [rx](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md#a87c543e4eb14b9e1e1fbd9fe7d4b047b)
- [mqtt_puback_param](../network_application_model_reference/P060_mqtt_puback_param_结构体.md)
- [message_id](../network_application_model_reference/P060_mqtt_puback_param_结构体.md#a727b919b853e77e480fb841e74a2dedf)
- [reason_code](../network_application_model_reference/P060_mqtt_puback_param_结构体.md#a44307fc6b172729478f1d097bbaf34bb)
- [prop](../network_application_model_reference/P060_mqtt_puback_param_结构体.md#a5fbbc6613660883a96aa37c8def6baa5)
- [mqtt_pubrec_param](../network_application_model_reference/P064_mqtt_pubrec_param_结构体.md)
- [message_id](../network_application_model_reference/P064_mqtt_pubrec_param_结构体.md#ab0f92884dbd6e63894210ff7f57fe62c)
- [reason_code](../network_application_model_reference/P064_mqtt_pubrec_param_结构体.md#a4d52112e88d954a88e4c65c9be5b0b93)
- [prop](../network_application_model_reference/P064_mqtt_pubrec_param_结构体.md#acf7d23d86fa5a7d935711459e52b092d)
- [mqtt_pubrel_param](../network_application_model_reference/P065_mqtt_pubrel_param_结构体.md)
- [message_id](../network_application_model_reference/P065_mqtt_pubrel_param_结构体.md#a4333fba7ac37d5a68fe921453b56b572)
- [reason_code](../network_application_model_reference/P065_mqtt_pubrel_param_结构体.md#a8fe8b7921add0b5fa2926a9eec68d102)
- [prop](../network_application_model_reference/P065_mqtt_pubrel_param_结构体.md#a4e2c97c37bc4c43fd4a63391372dfed3)
- [mqtt_pubcomp_param](../network_application_model_reference/P061_mqtt_pubcomp_param_结构体.md)
- [message_id](../network_application_model_reference/P061_mqtt_pubcomp_param_结构体.md#ae8484ad4d62f953ecace6c990002e316)
- [reason_code](../network_application_model_reference/P061_mqtt_pubcomp_param_结构体.md#a4e969aeee8c66a10e23731f8fe74db93)
- [prop](../network_application_model_reference/P061_mqtt_pubcomp_param_结构体.md#a1e38cde0e4e18b091e893bf207fa6c6d)
- [mqtt_suback_param](../network_application_model_reference/P073_mqtt_suback_param_结构体.md)
- [message_id](../network_application_model_reference/P073_mqtt_suback_param_结构体.md#a985b53444e7b2c10ab68844fcee34ee4)
- [return_codes](../network_application_model_reference/P073_mqtt_suback_param_结构体.md#a94ef5183aa3438db0521f445650c5868)
- [prop](../network_application_model_reference/P073_mqtt_suback_param_结构体.md#a5f0eff81eef7d9dc0767addea0782bf5)
- [mqtt_unsuback_param](../network_application_model_reference/P078_mqtt_unsuback_param_结构体.md)
- [message_id](../network_application_model_reference/P078_mqtt_unsuback_param_结构体.md#aa453177181e07cd0532b8cf591be0f32)
- [reason_codes](../network_application_model_reference/P078_mqtt_unsuback_param_结构体.md#a992c0c038413377c8edd701d2ef8455e)
- [prop](../network_application_model_reference/P078_mqtt_unsuback_param_结构体.md#a543fb60386725e9096bb0243beaa1181)
- [mqtt_publish_param](../network_application_model_reference/P063_mqtt_publish_param_结构体.md)
- [message](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a9841a4fbb30b597a9710863ce6034688)
- [message_id](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#aac4c6ba605506c183d2d5bdd7e550b3e)
- [dup_flag](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a2c2062c2b3ad027d5dfea56cb81c48e7)
- [retain_flag](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a9b2c6fad5bf830276d8d3f6b5ab04210)
- [user_prop](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a813b18b4c859fb5e703d90fc8eb9bd2e)
- [response_topic](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a63e9311cf0acf33386ceb8328b040d2a)
- [correlation_data](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#ab98e52ae704c6e988d554cf388b2ec0c)
- [content_type](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a8f76494a04d91150aee2ed7e9a271243)
- [subscription_identifier](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a5edb680fe44b795b02e35fcb73b98efa)
- [message_expiry_interval](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a4a486b254bd8e0f081251f8ca087e9d2)
- [topic_alias](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a13bf77403471f79687fe63a93cd1627d)
- [payload_format_indicator](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a8d9905f31bfc9072516f00082eda9c50)
- [has_payload_format_indicator](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a4190ccdfbf97a4ef63121e6a841d5f79)
- [has_message_expiry_interval](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a85e5a3a9c7347c506780627515dc84ea)
- [has_topic_alias](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a36a4d07ed13c5d4befc51a6285606090)
- [has_response_topic](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#aafc5473b88a64df887751903314f0fac)
- [has_correlation_data](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a599f8830ef4b42a68955ad58411ef0f1)
- [has_user_prop](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a5e4b146a69c82fa36fd43adb8658ef5f)
- [has_subscription_identifier](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#aab2664e89f086b62b9af5cd481fccde3)
- [has_content_type](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a00413022cecf2a624506ab5da630aefa)
- [prop](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a5e87084f72285ebdf5d26aca0eed6f00)
- [mqtt_subscription_list](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md)
- [list](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#a677b9c49972b6d6ade2dd934c8518cc9)
- [list_count](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#aa44e0af3526ee0424627bb24a90ea6b1)
- [message_id](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#a0667dcd4bd5eb5fe1b13b4df1bf2c26f)
- [user_prop](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#a9736f9d14db3097c2081e81e765a60ec)
- [subscription_identifier](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#a314f91139b4a837b173a6a930c3bdc6b)
- [prop](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#a97fefa83de8657d85b0f76013ca1f222)
- [mqtt_disconnect_param](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md)
- [reason_code](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#aa1b60dae11e0cad827e2d9942c1137e4)
- [user_prop](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a03050c6d4879f0d0eb62093b340bb99c)
- [reason_string](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a7a3b72acdd5a2d239c9e3d78e59bb4c2)
- [server_reference](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#aa44656e2663a058070a3d30e3bdabee9)
- [session_expiry_interval](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a9a0531c1fb9b95019bb49f1642d54b07)
- [has_session_expiry_interval](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a2360cc037d244abed416ace079f82257)
- [has_reason_string](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#ae2077e489cf38f4bccfebb78a840b9fe)
- [has_user_prop](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a02b38f24432c8def5dcda439bc8e9ab7)
- [has_server_reference](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a8891e52deb9c40f4f838f1df67db9794)
- [rx](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a6fb48a1ddf15d525f13f979758a06132)
- [prop](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#aa211770e88640378928e3ed3d09c23ac)
- [mqtt_auth_param](../network_application_model_reference/P052_mqtt_auth_param_结构体.md)
- [reason_code](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#adace77cd3860024ece2252ee41dcd134)
- [user_prop](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a1ad0e22ec7f3d5d1d304bacad06cb0c6)
- [auth_method](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a5602413c28ceadc87420f8c7a6c53489)
- [auth_data](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#aaa1aa29efd09cf58aaf79b4e279dc2a9)
- [reason_string](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a500d1b239b9882a1625d5d6035dd3199)
- [has_auth_method](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a6cf278bec874623fcd97a5c5e7d43940)
- [has_auth_data](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a32bfb124dbaa11a328e7300bc0890cfc)
- [has_reason_string](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a772343a4f3df425e54c00c43f5fdced4)
- [has_user_prop](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a50f570175c944f7e0dad4b276c07a6ea)
- [rx](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a9403d927a86f90eb1847840d6f47fe37)
- [prop](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a6bd366cb6479370f9db0abaa22e1b803)
- [mqtt_evt_param](../network_application_model_reference/P091_mqtt_evt_param_联合体.md)
- [connack](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#aa99a77bbade75b3f450088b32131f87a)
- [publish](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#a41be40873e1ebb9bf6fbf6dc9566d6ff)
- [puback](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#a24bf756db9fa8cc67c0b02c4e2cb602c)
- [pubrec](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#a3b31e1d94c480b8d0244cc12d1c25524)
- [pubrel](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#a2269e07f580fb65df5f3d0832aa6b3af)
- [pubcomp](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#ac3d564095019ccf57c10678a433bc31a)
- [suback](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#af6ce2426884d2faa443b3dfdaa45594c)
- [unsuback](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#ad040b028ed0aaabcaddedc204fb709d8)
- [disconnect](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#a6967703ed8a9f58eda8e9a94b5bc1f5f)
- [auth](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#ad1bb0a46bab0442404e22627bcc6a0ef)
- [mqtt_evt](../network_application_model_reference/P058_mqtt_evt_结构体.md)
- [type](../network_application_model_reference/P058_mqtt_evt_结构体.md#a79d7a198d8ed9959bb7aae835b6301c2)
- [param](../network_application_model_reference/P058_mqtt_evt_结构体.md#aca1085171667c46b2438f66d9227e07c)
- [result](../network_application_model_reference/P058_mqtt_evt_结构体.md#aa1a4304d4aa70440ba630f3fe5e76d2f)
- [mqtt_client](../network_application_model_reference/P054_mqtt_client_结构体.md)
- [mqtt_evt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gabdf01ededb62ceb4c1608a64cb718a8c)
- [mqtt_sec_config](../network_application_model_reference/P066_mqtt_sec_config_结构体.md)
- [peer_verify](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a0e04768b6589823464c2d13c31230cad)
- [cipher_count](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a25415e32e00808fb6a24187f4234059f)
- [cipher_list](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a179a97d56a7a12d5afb60257a67ce46c)
- [sec_tag_count](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a6d59afc061a749ea31f5bd415918a3e0)
- [sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)
- [sec_tag_list](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#adeb8630a9e73c4b3226afa1c9a5060fe)
- [hostname](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#af7a0ee827bf98fde264000f4c9020c15)
- [cert_nocopy](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a5beac5704fec3e399e5c0099a57ce115)
- [set_native_tls](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a9bfafa25c9054fa0389927c72da60587)
- [mqtt_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaffc2c3078004cf8d24935be086ad63b4)
- [MQTT_TRANSPORT_NON_SECURE](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a)
- [MQTT_TRANSPORT_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df)
- [mqtt_transport](../network_application_model_reference/P077_mqtt_transport_结构体.md)
- [type](../network_application_model_reference/P077_mqtt_transport_结构体.md#a47b49927c79e67b202112c68b53d83f4)
- [if_name](../network_application_model_reference/P077_mqtt_transport_结构体.md#a7cfdf50105a275612dbda28e7c02808e)
- [sock](../network_application_model_reference/P077_mqtt_transport_结构体.md#a3b4589dd05394589e7af460761b800bf)
- [tcp](../network_application_model_reference/P077_mqtt_transport_结构体.md#af65e3f0284ba9d881c5b916749f097b2)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [mqtt_internal](../network_application_model_reference/P059_mqtt_internal_结构体.md)
- [sys_mutex](../userspace_sync_reference/P004_用户模式互斥量结构.md)
- [mutex](../network_application_model_reference/P059_mqtt_internal_结构体.md#af866a252b9e18496c8e1627704d8a8b2)
- [last_activity](../network_application_model_reference/P059_mqtt_internal_结构体.md#a8f30cb1440efecf8ae8fc448e4f462f8)
- [state](../network_application_model_reference/P059_mqtt_internal_结构体.md#acf93a973de5a5430e767e2996f1cd048)
- [rx_buf_datalen](../network_application_model_reference/P059_mqtt_internal_结构体.md#a45aeafd71dadaf1d0fd0bc3969c921de)
- [remaining_payload](../network_application_model_reference/P059_mqtt_internal_结构体.md#a921477a9839447f4fe1c823911680c92)
- [topic_aliases](../network_application_model_reference/P059_mqtt_internal_结构体.md#a897895965adaf781b3a426dd53da10a2)
- [disconnect_reason](../network_application_model_reference/P059_mqtt_internal_结构体.md#ad41631ca4fbbae32e0a7042515c90ea9)
- [internal](../network_application_model_reference/P054_mqtt_client_结构体.md#a41cc1d3c5e5180af1d6376f88598678a)
- [transport](../network_application_model_reference/P054_mqtt_client_结构体.md#ac31a2ea9d67886f83fd3af88f33f36d9)
- [client_id](../network_application_model_reference/P054_mqtt_client_结构体.md#aabd419115c8637e4e4c0e6d23a5a984d)
- [broker](../network_application_model_reference/P054_mqtt_client_结构体.md#a72d61d9c0e717010ff90c2ed7fcddf5c)
- [user_name](../network_application_model_reference/P054_mqtt_client_结构体.md#ab271f2061fe3c9e3c1a76158a1c00449)
- [password](../network_application_model_reference/P054_mqtt_client_结构体.md#aef6da1db6f600a2bfd1c7dd0d78d1b6d)
- [user_prop](../network_application_model_reference/P054_mqtt_client_结构体.md#a726f5a806458d7dc9d6072dff74508fc)
- [content_type](../network_application_model_reference/P054_mqtt_client_结构体.md#a89ce07fe536a502c051e4082b708155e)
- [response_topic](../network_application_model_reference/P054_mqtt_client_结构体.md#ac6c53bf95f311a4df29d7db5f4c20b45)
- [correlation_data](../network_application_model_reference/P054_mqtt_client_结构体.md#aac856189cedecf059f4ba723b06edda6)
- [will_delay_interval](../network_application_model_reference/P054_mqtt_client_结构体.md#a253bee13043ffe1ebe9c46299f8a238e)
- [message_expiry_interval](../network_application_model_reference/P054_mqtt_client_结构体.md#a485855e9b09d0c48fb09c5673f38b5ee)
- [payload_format_indicator](../network_application_model_reference/P054_mqtt_client_结构体.md#abdf2c45264ba77d584655b0cb6562c6b)
- [will_prop](../network_application_model_reference/P054_mqtt_client_结构体.md#a0a1669a8be16d37819704ac60911de73)
- [will_topic](../network_application_model_reference/P054_mqtt_client_结构体.md#a4b23a72831697b78dc4019a4b6ac97e4)
- [will_message](../network_application_model_reference/P054_mqtt_client_结构体.md#a7f4e9547b1d91edf21589334db711499)
- [evt_cb](../network_application_model_reference/P054_mqtt_client_结构体.md#a44c515b8b25d59554990f6193217d83f)
- [rx_buf](../network_application_model_reference/P054_mqtt_client_结构体.md#a9f63fb54f8557135c1aa38a60bb7053c)
- [rx_buf_size](../network_application_model_reference/P054_mqtt_client_结构体.md#a66335741e991a2985ab5d4d7765651d2)
- [tx_buf](../network_application_model_reference/P054_mqtt_client_结构体.md#ae582274bf396caa0a3427f1aeace639c)
- [tx_buf_size](../network_application_model_reference/P054_mqtt_client_结构体.md#a4c456f4065e3bc20752d908f2d805667)
- [keepalive](../network_application_model_reference/P054_mqtt_client_结构体.md#aa65a4af5952634e4ff5c4bf700ccccd7)
- [protocol_version](../network_application_model_reference/P054_mqtt_client_结构体.md#a63e3c1b470a7de9d179b1c0686504a68)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [unacked_ping](../network_application_model_reference/P054_mqtt_client_结构体.md#a67f76cd0feadf8ae11ed232dcc9ac1d1)
- [auth_method](../network_application_model_reference/P054_mqtt_client_结构体.md#ac899284f06f581cac0b647381c757287)
- [auth_data](../network_application_model_reference/P054_mqtt_client_结构体.md#ae46c6695e9dfbf13cb895d8acad12d58)
- [session_expiry_interval](../network_application_model_reference/P054_mqtt_client_结构体.md#a1d0587f7b2be63eb74f9cba271c337fb)
- [maximum_packet_size](../network_application_model_reference/P054_mqtt_client_结构体.md#a2d9fc66f26284f6ab90f79a4d7aef6d7)
- [receive_maximum](../network_application_model_reference/P054_mqtt_client_结构体.md#a6700818bb78880e8b10878f31680f3d3)
- [request_response_info](../network_application_model_reference/P054_mqtt_client_结构体.md#a1c5a0e00803a745b2569452ed127440a)
- [request_problem_info](../network_application_model_reference/P054_mqtt_client_结构体.md#a1a8f71b8756219a20404782c9aeff431)
- [prop](../network_application_model_reference/P054_mqtt_client_结构体.md#a8c48cec6d0f895d05a8f933240348818)
- [will_retain](../network_application_model_reference/P054_mqtt_client_结构体.md#ac96879e15ccd829fbcf9b88913161c0d)
- [clean_session](../network_application_model_reference/P054_mqtt_client_结构体.md#aae9ecb0faf8dc4337579e0713d065184)
- [user_data](../network_application_model_reference/P054_mqtt_client_结构体.md#afe138435d59720cc2c8c4b2756134a49)
- [mqtt_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad1376509ae7c946c840d103d8b59e9a1)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [mqtt_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad936f28553cb2e771a843512b0a315fa)
- [mqtt_publish](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga57745efa1bf6fbdf7eb1b3f01623e4c7)
- [mqtt_publish_qos1_ack](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gae9069fceec2c018e64cc6beb16aa055c)
- [mqtt_publish_qos2_receive](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gacbe41b83d9c0676d0d4cf01dd91765eb)
- [mqtt_publish_qos2_release](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga6c952ed014f78774096bfb6099794803)
- [mqtt_publish_qos2_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga2b17999e845d613f5b0b20015b8204f3)
- [mqtt_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga40d226b891b8f62f2c486bbb11ce9678)
- [mqtt_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga4ff43a198e93e332b5553a4d0b59261d)
- [mqtt_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad1d549d37b69a61e1bf8d9d213e02ca8)
- [mqtt_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga0bc7d91da88c2fbc25108d89ce4318c4)
- [mqtt_auth](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gad4d870f91a7d594c3a7325ab6de87a02)
- [mqtt_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gafb2df41fad7c318f9fe75919919139bd)
- [mqtt_live](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga8b87710d01076c8e51b1a75634168269)
- [mqtt_keepalive_time_left](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#gaa16bf7b0597ad00c4a3943235579e86b)
- [mqtt_input](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga2dbc3c158d63a6f57b362be94c22660a)
- [mqtt_read_publish_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga3559cdd6093d75c6fe6792ec2a453172)
- [mqtt_read_publish_payload_blocking](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga05213aceaa9e9cbbfaa9bab7a78b3d25)
- [mqtt_readall_publish_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga31823965ec34a253793b40b50e800417)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mutex.h](../userspace_sync_reference/P005_用户模式互斥量头文件参考.md)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [mqtt_auth_param::user_prop](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a1ad0e22ec7f3d5d1d304bacad06cb0c6)
- [mqtt_auth_param::has_auth_data](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a32bfb124dbaa11a328e7300bc0890cfc)
- [mqtt_auth_param::reason_string](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a500d1b239b9882a1625d5d6035dd3199)
- [mqtt_auth_param::has_user_prop](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a50f570175c944f7e0dad4b276c07a6ea)
- [mqtt_auth_param::auth_method](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a5602413c28ceadc87420f8c7a6c53489)
- [mqtt_auth_param::prop](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a6bd366cb6479370f9db0abaa22e1b803)
- [mqtt_auth_param::has_auth_method](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a6cf278bec874623fcd97a5c5e7d43940)
- [mqtt_auth_param::has_reason_string](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a772343a4f3df425e54c00c43f5fdced4)
- [mqtt_auth_param::rx](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#a9403d927a86f90eb1847840d6f47fe37)
- [mqtt_auth_param::auth_data](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#aaa1aa29efd09cf58aaf79b4e279dc2a9)
- [mqtt_auth_param::reason_code](../network_application_model_reference/P052_mqtt_auth_param_结构体.md#adace77cd3860024ece2252ee41dcd134)
- [mqtt_binstr::data](../network_application_model_reference/P053_mqtt_binstr_结构体.md#a1f61872edd09941155f60a242e582ff7)
- [mqtt_binstr::len](../network_application_model_reference/P053_mqtt_binstr_结构体.md#abcc36b6c59c3da740a6b352fe846fd5f)
- [mqtt_client::will_prop](../network_application_model_reference/P054_mqtt_client_结构体.md#a0a1669a8be16d37819704ac60911de73)
- [mqtt_client::request_problem_info](../network_application_model_reference/P054_mqtt_client_结构体.md#a1a8f71b8756219a20404782c9aeff431)
- [mqtt_client::request_response_info](../network_application_model_reference/P054_mqtt_client_结构体.md#a1c5a0e00803a745b2569452ed127440a)
- [mqtt_client::session_expiry_interval](../network_application_model_reference/P054_mqtt_client_结构体.md#a1d0587f7b2be63eb74f9cba271c337fb)
- [mqtt_client::will_delay_interval](../network_application_model_reference/P054_mqtt_client_结构体.md#a253bee13043ffe1ebe9c46299f8a238e)
- [mqtt_client::maximum_packet_size](../network_application_model_reference/P054_mqtt_client_结构体.md#a2d9fc66f26284f6ab90f79a4d7aef6d7)
- [mqtt_client::internal](../network_application_model_reference/P054_mqtt_client_结构体.md#a41cc1d3c5e5180af1d6376f88598678a)
- [mqtt_client::evt_cb](../network_application_model_reference/P054_mqtt_client_结构体.md#a44c515b8b25d59554990f6193217d83f)
- [mqtt_client::message_expiry_interval](../network_application_model_reference/P054_mqtt_client_结构体.md#a485855e9b09d0c48fb09c5673f38b5ee)
- [mqtt_client::will_topic](../network_application_model_reference/P054_mqtt_client_结构体.md#a4b23a72831697b78dc4019a4b6ac97e4)
- [mqtt_client::tx_buf_size](../network_application_model_reference/P054_mqtt_client_结构体.md#a4c456f4065e3bc20752d908f2d805667)
- [mqtt_client::protocol_version](../network_application_model_reference/P054_mqtt_client_结构体.md#a63e3c1b470a7de9d179b1c0686504a68)
- [mqtt_client::rx_buf_size](../network_application_model_reference/P054_mqtt_client_结构体.md#a66335741e991a2985ab5d4d7765651d2)
- [mqtt_client::receive_maximum](../network_application_model_reference/P054_mqtt_client_结构体.md#a6700818bb78880e8b10878f31680f3d3)
- [mqtt_client::unacked_ping](../network_application_model_reference/P054_mqtt_client_结构体.md#a67f76cd0feadf8ae11ed232dcc9ac1d1)
- [mqtt_client::user_prop](../network_application_model_reference/P054_mqtt_client_结构体.md#a726f5a806458d7dc9d6072dff74508fc)
- [mqtt_client::broker](../network_application_model_reference/P054_mqtt_client_结构体.md#a72d61d9c0e717010ff90c2ed7fcddf5c)
- [mqtt_client::will_message](../network_application_model_reference/P054_mqtt_client_结构体.md#a7f4e9547b1d91edf21589334db711499)
- [mqtt_client::content_type](../network_application_model_reference/P054_mqtt_client_结构体.md#a89ce07fe536a502c051e4082b708155e)
- [mqtt_client::prop](../network_application_model_reference/P054_mqtt_client_结构体.md#a8c48cec6d0f895d05a8f933240348818)
- [mqtt_client::rx_buf](../network_application_model_reference/P054_mqtt_client_结构体.md#a9f63fb54f8557135c1aa38a60bb7053c)
- [mqtt_client::keepalive](../network_application_model_reference/P054_mqtt_client_结构体.md#aa65a4af5952634e4ff5c4bf700ccccd7)
- [mqtt_client::client_id](../network_application_model_reference/P054_mqtt_client_结构体.md#aabd419115c8637e4e4c0e6d23a5a984d)
- [mqtt_client::correlation_data](../network_application_model_reference/P054_mqtt_client_结构体.md#aac856189cedecf059f4ba723b06edda6)
- [mqtt_client::clean_session](../network_application_model_reference/P054_mqtt_client_结构体.md#aae9ecb0faf8dc4337579e0713d065184)
- [mqtt_client::user_name](../network_application_model_reference/P054_mqtt_client_结构体.md#ab271f2061fe3c9e3c1a76158a1c00449)
- [mqtt_client::payload_format_indicator](../network_application_model_reference/P054_mqtt_client_结构体.md#abdf2c45264ba77d584655b0cb6562c6b)
- [mqtt_client::transport](../network_application_model_reference/P054_mqtt_client_结构体.md#ac31a2ea9d67886f83fd3af88f33f36d9)
- [mqtt_client::response_topic](../network_application_model_reference/P054_mqtt_client_结构体.md#ac6c53bf95f311a4df29d7db5f4c20b45)
- [mqtt_client::auth_method](../network_application_model_reference/P054_mqtt_client_结构体.md#ac899284f06f581cac0b647381c757287)
- [mqtt_client::will_retain](../network_application_model_reference/P054_mqtt_client_结构体.md#ac96879e15ccd829fbcf9b88913161c0d)
- [mqtt_client::auth_data](../network_application_model_reference/P054_mqtt_client_结构体.md#ae46c6695e9dfbf13cb895d8acad12d58)
- [mqtt_client::tx_buf](../network_application_model_reference/P054_mqtt_client_结构体.md#ae582274bf396caa0a3427f1aeace639c)
- [mqtt_client::password](../network_application_model_reference/P054_mqtt_client_结构体.md#aef6da1db6f600a2bfd1c7dd0d78d1b6d)
- [mqtt_client::user_data](../network_application_model_reference/P054_mqtt_client_结构体.md#afe138435d59720cc2c8c4b2756134a49)
- [mqtt_common_ack_properties::reason_string](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md#a282e39c4e3bdcebf331969fdf0a60570)
- [mqtt_common_ack_properties::has_user_prop](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md#a69d6a6795e309cb64bff1dd3eeb698c6)
- [mqtt_common_ack_properties::rx](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md#a87c543e4eb14b9e1e1fbd9fe7d4b047b)
- [mqtt_common_ack_properties::user_prop](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md#aa827f37cfc537e00e8ff4e774ec9b835)
- [mqtt_common_ack_properties::has_reason_string](../network_application_model_reference/P055_mqtt_common_ack_properties_结构体.md#abf672bc44df434fe2dd4f519343d6480)
- [mqtt_connack_param::server_reference](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a0426044dfe84d5160d1116018265eda3)
- [mqtt_connack_param::topic_alias_maximum](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a09cdb8430a3ced98055b564716201bf1)
- [mqtt_connack_param::has_server_keep_alive](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a0d11efb926df6a0d65e879fee878bda0)
- [mqtt_connack_param::has_maximum_qos](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a0f02175c92a22ad05f370dd944ad6b1a)
- [mqtt_connack_param::has_response_information](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a0f03ee47ace97ccaa841df5353e49f26)
- [mqtt_connack_param::response_information](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a1314e5735f128b905bd3d78beaee956e)
- [mqtt_connack_param::wildcard_sub_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a1802487e00937da8e4261083b7229219)
- [mqtt_connack_param::has_receive_maximum](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a1c37aaf9f6cde9f251b79af7144a099e)
- [mqtt_connack_param::user_prop](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a29eed1a34902519380aa59757bde501c)
- [mqtt_connack_param::has_server_reference](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a351717d25bf8bc2d915506b5bc354214)
- [mqtt_connack_param::shared_sub_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a3a21965017d0e9d15ed046eb0cfb461f)
- [mqtt_connack_param::has_wildcard_sub_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a3a6f8b9f79f81c34bda7aca99fa0682f)
- [mqtt_connack_param::rx](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a3a7a8a6dbef8d5026717b98b4e949c4e)
- [mqtt_connack_param::has_subscription_ids_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a43ada81fd7746aab783a0d1cb4d4d645)
- [mqtt_connack_param::has_user_prop](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a4d1b50d148189053879ec80aa2688a2b)
- [mqtt_connack_param::has_reason_string](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a4f8092dc562fe27396c21e1329e19262)
- [mqtt_connack_param::prop](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a54ae953abeec2d31e7c82869302b492e)
- [mqtt_connack_param::reason_string](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a5fbdc09eff6fef2f06a98c8f9faf0a03)
- [mqtt_connack_param::has_auth_data](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a6d7423e5c7234e97f79db2dd9e592d85)
- [mqtt_connack_param::has_auth_method](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a7134eddbb0d497c6cfe85b6fcfc9efa1)
- [mqtt_connack_param::has_shared_sub_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a78dad1593aaa64c27263cafc61791a03)
- [mqtt_connack_param::has_retain_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a7df963cce8b5ba99efe9888f742fad4f)
- [mqtt_connack_param::session_expiry_interval](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a7e47864579e36ea469d198ceb9cdd3f4)
- [mqtt_connack_param::assigned_client_id](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a7f275e22d6cdf808b1f0a19c3f78f517)
- [mqtt_connack_param::has_maximum_packet_size](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a80932b53f13d5cb5c299f384c176e1af)
- [mqtt_connack_param::maximum_packet_size](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a8e5cab6b3479fc9e902feb622008386a)
- [mqtt_connack_param::maximum_qos](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a9c400f66c3a7eade5df879b328f4cb42)
- [mqtt_connack_param::receive_maximum](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#a9eecd31595fa1332a1cf4b661cedeae2)
- [mqtt_connack_param::return_code](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#aae7a54dd6f62887b618f652f260ed6bd)
- [mqtt_connack_param::session_present_flag](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#ab123a8236804082667ad93ddd7e40e7a)
- [mqtt_connack_param::auth_method](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#abbd4490c94846009f79c741e3067c743)
- [mqtt_connack_param::subscription_ids_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#ac3815c5ecaaeb8cea860ccd75f1d460a)
- [mqtt_connack_param::has_topic_alias_maximum](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#ac3f6a6b22fcf1ed55dc46d4b9b2079e6)
- [mqtt_connack_param::auth_data](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#ad45d67943848406b290fee98e5d4d3ba)
- [mqtt_connack_param::has_session_expiry_interval](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#ae2c5b667e0e050611791160c8b7755ef)
- [mqtt_connack_param::retain_available](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#af0810d9762a46f0ac7376becb631a9f7)
- [mqtt_connack_param::server_keep_alive](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#af21ff08751c63f17423500c33191fcdf)
- [mqtt_connack_param::has_assigned_client_id](../network_application_model_reference/P056_mqtt_connack_param_结构体.md#af2655b3164805704e68d8ed69621a168)
- [mqtt_disconnect_param::has_user_prop](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a02b38f24432c8def5dcda439bc8e9ab7)
- [mqtt_disconnect_param::user_prop](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a03050c6d4879f0d0eb62093b340bb99c)
- [mqtt_disconnect_param::has_session_expiry_interval](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a2360cc037d244abed416ace079f82257)
- [mqtt_disconnect_param::rx](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a6fb48a1ddf15d525f13f979758a06132)
- [mqtt_disconnect_param::reason_string](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a7a3b72acdd5a2d239c9e3d78e59bb4c2)
- [mqtt_disconnect_param::has_server_reference](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a8891e52deb9c40f4f838f1df67db9794)
- [mqtt_disconnect_param::session_expiry_interval](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#a9a0531c1fb9b95019bb49f1642d54b07)
- [mqtt_disconnect_param::reason_code](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#aa1b60dae11e0cad827e2d9942c1137e4)
- [mqtt_disconnect_param::prop](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#aa211770e88640378928e3ed3d09c23ac)
- [mqtt_disconnect_param::server_reference](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#aa44656e2663a058070a3d30e3bdabee9)
- [mqtt_disconnect_param::has_reason_string](../network_application_model_reference/P057_mqtt_disconnect_param_结构体.md#ae2077e489cf38f4bccfebb78a840b9fe)
- [mqtt_evt::type](../network_application_model_reference/P058_mqtt_evt_结构体.md#a79d7a198d8ed9959bb7aae835b6301c2)
- [mqtt_evt::result](../network_application_model_reference/P058_mqtt_evt_结构体.md#aa1a4304d4aa70440ba630f3fe5e76d2f)
- [mqtt_evt::param](../network_application_model_reference/P058_mqtt_evt_结构体.md#aca1085171667c46b2438f66d9227e07c)
- [mqtt_internal::rx_buf_datalen](../network_application_model_reference/P059_mqtt_internal_结构体.md#a45aeafd71dadaf1d0fd0bc3969c921de)
- [mqtt_internal::topic_aliases](../network_application_model_reference/P059_mqtt_internal_结构体.md#a897895965adaf781b3a426dd53da10a2)
- [mqtt_internal::last_activity](../network_application_model_reference/P059_mqtt_internal_结构体.md#a8f30cb1440efecf8ae8fc448e4f462f8)
- [mqtt_internal::remaining_payload](../network_application_model_reference/P059_mqtt_internal_结构体.md#a921477a9839447f4fe1c823911680c92)
- [mqtt_internal::state](../network_application_model_reference/P059_mqtt_internal_结构体.md#acf93a973de5a5430e767e2996f1cd048)
- [mqtt_internal::disconnect_reason](../network_application_model_reference/P059_mqtt_internal_结构体.md#ad41631ca4fbbae32e0a7042515c90ea9)
- [mqtt_internal::mutex](../network_application_model_reference/P059_mqtt_internal_结构体.md#af866a252b9e18496c8e1627704d8a8b2)
- [mqtt_puback_param::reason_code](../network_application_model_reference/P060_mqtt_puback_param_结构体.md#a44307fc6b172729478f1d097bbaf34bb)
- [mqtt_puback_param::prop](../network_application_model_reference/P060_mqtt_puback_param_结构体.md#a5fbbc6613660883a96aa37c8def6baa5)
- [mqtt_puback_param::message_id](../network_application_model_reference/P060_mqtt_puback_param_结构体.md#a727b919b853e77e480fb841e74a2dedf)
- [mqtt_pubcomp_param::prop](../network_application_model_reference/P061_mqtt_pubcomp_param_结构体.md#a1e38cde0e4e18b091e893bf207fa6c6d)
- [mqtt_pubcomp_param::reason_code](../network_application_model_reference/P061_mqtt_pubcomp_param_结构体.md#a4e969aeee8c66a10e23731f8fe74db93)
- [mqtt_pubcomp_param::message_id](../network_application_model_reference/P061_mqtt_pubcomp_param_结构体.md#ae8484ad4d62f953ecace6c990002e316)
- [mqtt_publish_message::payload](../network_application_model_reference/P062_mqtt_publish_message_结构体.md#a6cfed92c8f8fb319d3cbf40b956cb94d)
- [mqtt_publish_message::topic](../network_application_model_reference/P062_mqtt_publish_message_结构体.md#acf5dba605db61efe68ec29337eea95e9)
- [mqtt_publish_param::has_content_type](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a00413022cecf2a624506ab5da630aefa)
- [mqtt_publish_param::topic_alias](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a13bf77403471f79687fe63a93cd1627d)
- [mqtt_publish_param::dup_flag](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a2c2062c2b3ad027d5dfea56cb81c48e7)
- [mqtt_publish_param::has_topic_alias](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a36a4d07ed13c5d4befc51a6285606090)
- [mqtt_publish_param::has_payload_format_indicator](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a4190ccdfbf97a4ef63121e6a841d5f79)
- [mqtt_publish_param::message_expiry_interval](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a4a486b254bd8e0f081251f8ca087e9d2)
- [mqtt_publish_param::has_correlation_data](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a599f8830ef4b42a68955ad58411ef0f1)
- [mqtt_publish_param::has_user_prop](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a5e4b146a69c82fa36fd43adb8658ef5f)
- [mqtt_publish_param::prop](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a5e87084f72285ebdf5d26aca0eed6f00)
- [mqtt_publish_param::subscription_identifier](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a5edb680fe44b795b02e35fcb73b98efa)
- [mqtt_publish_param::response_topic](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a63e9311cf0acf33386ceb8328b040d2a)
- [mqtt_publish_param::user_prop](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a813b18b4c859fb5e703d90fc8eb9bd2e)
- [mqtt_publish_param::has_message_expiry_interval](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a85e5a3a9c7347c506780627515dc84ea)
- [mqtt_publish_param::payload_format_indicator](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a8d9905f31bfc9072516f00082eda9c50)
- [mqtt_publish_param::content_type](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a8f76494a04d91150aee2ed7e9a271243)
- [mqtt_publish_param::message](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a9841a4fbb30b597a9710863ce6034688)
- [mqtt_publish_param::retain_flag](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#a9b2c6fad5bf830276d8d3f6b5ab04210)
- [mqtt_publish_param::has_subscription_identifier](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#aab2664e89f086b62b9af5cd481fccde3)
- [mqtt_publish_param::message_id](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#aac4c6ba605506c183d2d5bdd7e550b3e)
- [mqtt_publish_param::has_response_topic](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#aafc5473b88a64df887751903314f0fac)
- [mqtt_publish_param::correlation_data](../network_application_model_reference/P063_mqtt_publish_param_结构体.md#ab98e52ae704c6e988d554cf388b2ec0c)
- [mqtt_pubrec_param::reason_code](../network_application_model_reference/P064_mqtt_pubrec_param_结构体.md#a4d52112e88d954a88e4c65c9be5b0b93)
- [mqtt_pubrec_param::message_id](../network_application_model_reference/P064_mqtt_pubrec_param_结构体.md#ab0f92884dbd6e63894210ff7f57fe62c)
- [mqtt_pubrec_param::prop](../network_application_model_reference/P064_mqtt_pubrec_param_结构体.md#acf7d23d86fa5a7d935711459e52b092d)
- [mqtt_pubrel_param::message_id](../network_application_model_reference/P065_mqtt_pubrel_param_结构体.md#a4333fba7ac37d5a68fe921453b56b572)
- [mqtt_pubrel_param::prop](../network_application_model_reference/P065_mqtt_pubrel_param_结构体.md#a4e2c97c37bc4c43fd4a63391372dfed3)
- [mqtt_pubrel_param::reason_code](../network_application_model_reference/P065_mqtt_pubrel_param_结构体.md#a8fe8b7921add0b5fa2926a9eec68d102)
- [mqtt_sec_config::peer_verify](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a0e04768b6589823464c2d13c31230cad)
- [mqtt_sec_config::cipher_list](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a179a97d56a7a12d5afb60257a67ce46c)
- [mqtt_sec_config::cipher_count](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a25415e32e00808fb6a24187f4234059f)
- [mqtt_sec_config::cert_nocopy](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a5beac5704fec3e399e5c0099a57ce115)
- [mqtt_sec_config::sec_tag_count](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a6d59afc061a749ea31f5bd415918a3e0)
- [mqtt_sec_config::set_native_tls](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#a9bfafa25c9054fa0389927c72da60587)
- [mqtt_sec_config::sec_tag_list](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#adeb8630a9e73c4b3226afa1c9a5060fe)
- [mqtt_sec_config::hostname](../network_application_model_reference/P066_mqtt_sec_config_结构体.md#af7a0ee827bf98fde264000f4c9020c15)
- [mqtt_suback_param::prop](../network_application_model_reference/P073_mqtt_suback_param_结构体.md#a5f0eff81eef7d9dc0767addea0782bf5)
- [mqtt_suback_param::return_codes](../network_application_model_reference/P073_mqtt_suback_param_结构体.md#a94ef5183aa3438db0521f445650c5868)
- [mqtt_suback_param::message_id](../network_application_model_reference/P073_mqtt_suback_param_结构体.md#a985b53444e7b2c10ab68844fcee34ee4)
- [mqtt_subscription_list::message_id](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#a0667dcd4bd5eb5fe1b13b4df1bf2c26f)
- [mqtt_subscription_list::subscription_identifier](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#a314f91139b4a837b173a6a930c3bdc6b)
- [mqtt_subscription_list::list](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#a677b9c49972b6d6ade2dd934c8518cc9)
- [mqtt_subscription_list::user_prop](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#a9736f9d14db3097c2081e81e765a60ec)
- [mqtt_subscription_list::prop](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#a97fefa83de8657d85b0f76013ca1f222)
- [mqtt_subscription_list::list_count](../network_application_model_reference/P074_mqtt_subscription_list_结构体.md#aa44e0af3526ee0424627bb24a90ea6b1)
- [mqtt_topic_alias::topic_size](../network_application_model_reference/P076_mqtt_topic_alias_结构体.md#aed7c3e3306dd3bf97073ca6b7f9c4902)
- [mqtt_topic_alias::topic_buf](../network_application_model_reference/P076_mqtt_topic_alias_结构体.md#af056af89763a7d39f513759dd1f7e8a7)
- [mqtt_topic::retain_handling](../network_application_model_reference/P075_mqtt_topic_结构体.md#a52fbe1b4b5c793be0cad004829d57faa)
- [mqtt_topic::qos](../network_application_model_reference/P075_mqtt_topic_结构体.md#a780e90d62c094557bd3918de3b3921e6)
- [mqtt_topic::topic](../network_application_model_reference/P075_mqtt_topic_结构体.md#ab859d08baf88e6a1ac5135e1e55158d5)
- [mqtt_topic::no_local](../network_application_model_reference/P075_mqtt_topic_结构体.md#adce01c71f9b31f4ac0916ed1b8628fd4)
- [mqtt_topic::retain_as_published](../network_application_model_reference/P075_mqtt_topic_结构体.md#afb71b709d04a1a2caf5acb2200f3bfaa)
- [mqtt_transport::sock](../network_application_model_reference/P077_mqtt_transport_结构体.md#a3b4589dd05394589e7af460761b800bf)
- [mqtt_transport::type](../network_application_model_reference/P077_mqtt_transport_结构体.md#a47b49927c79e67b202112c68b53d83f4)
- [mqtt_transport::if_name](../network_application_model_reference/P077_mqtt_transport_结构体.md#a7cfdf50105a275612dbda28e7c02808e)
- [mqtt_transport::tcp](../network_application_model_reference/P077_mqtt_transport_结构体.md#af65e3f0284ba9d881c5b916749f097b2)
- [mqtt_unsuback_param::prop](../network_application_model_reference/P078_mqtt_unsuback_param_结构体.md#a543fb60386725e9096bb0243beaa1181)
- [mqtt_unsuback_param::reason_codes](../network_application_model_reference/P078_mqtt_unsuback_param_结构体.md#a992c0c038413377c8edd701d2ef8455e)
- [mqtt_unsuback_param::message_id](../network_application_model_reference/P078_mqtt_unsuback_param_结构体.md#aa453177181e07cd0532b8cf591be0f32)
- [mqtt_utf8_pair::value](../network_application_model_reference/P080_mqtt_utf8_pair_结构体.md#a749e0afc65c06917ca2881b51c0c6763)
- [mqtt_utf8_pair::name](../network_application_model_reference/P080_mqtt_utf8_pair_结构体.md#aedea0e9eb2526c8e0da2319017427c2f)
- [mqtt_utf8::size](../network_application_model_reference/P079_mqtt_utf8_结构体.md#a2376f943335326dae74c798141326b70)
- [mqtt_utf8::utf8](../network_application_model_reference/P079_mqtt_utf8_结构体.md#a69a949e3c9cb1794f8d28091601eba16)
- [tls_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)
- [mqtt_evt_param::pubrel](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#a2269e07f580fb65df5f3d0832aa6b3af)
- [mqtt_evt_param::puback](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#a24bf756db9fa8cc67c0b02c4e2cb602c)
- [mqtt_evt_param::pubrec](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#a3b31e1d94c480b8d0244cc12d1c25524)
- [mqtt_evt_param::publish](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#a41be40873e1ebb9bf6fbf6dc9566d6ff)
- [mqtt_evt_param::disconnect](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#a6967703ed8a9f58eda8e9a94b5bc1f5f)
- [mqtt_evt_param::connack](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#aa99a77bbade75b3f450088b32131f87a)
- [mqtt_evt_param::pubcomp](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#ac3d564095019ccf57c10678a433bc31a)
- [mqtt_evt_param::unsuback](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#ad040b028ed0aaabcaddedc204fb709d8)
- [mqtt_evt_param::auth](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#ad1bb0a46bab0442404e22627bcc6a0ef)
- [mqtt_evt_param::suback](../network_application_model_reference/P091_mqtt_evt_param_联合体.md#af6ce2426884d2faa443b3dfdaa45594c)
- [websocket.h](https://docs.zephyrproject.org/latest/doxygen/html/websocket_8h.html)

---

[上一章](P019_mm_drv_intel_adsp_mtl_tlb.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P021_net_buf.h_源码浏览.md)
