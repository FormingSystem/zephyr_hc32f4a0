---
id: learning.zephyr-docs.api-source-supplement-reference.page-23
title: ccc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ccc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_ccc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ccc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ccc_8h.html)。

## 23.1\_原始可见代码（Source Code）

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
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00180"></a>
<a id="l00181"></a>
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
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="foldopen00243"></a>
<a id="l00243"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="foldopen00283"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="foldopen00337"></a>
<a id="l00337"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="foldopen00359"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="foldopen00371"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="foldopen00389"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="foldopen00400"></a>
<a id="l00400"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="foldopen00413"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="foldopen00427"></a>
<a id="l00427"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="foldopen00447"></a>
<a id="l00447"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="foldopen00477"></a>
<a id="l00477"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="foldopen00491"></a>
<a id="l00491"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="foldopen00514"></a>
<a id="l00514"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="foldopen00535"></a>
<a id="l00535"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="foldopen00547"></a>
<a id="l00547"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="foldopen00555"></a>
<a id="l00555"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="foldopen00564"></a>
<a id="l00564"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="foldopen00575"></a>
<a id="l00575"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="foldopen00589"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="foldopen00647"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="foldopen00664"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="foldopen00676"></a>
<a id="l00676"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="foldopen00703"></a>
<a id="l00703"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="foldopen00714"></a>
<a id="l00714"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="foldopen00728"></a>
<a id="l00728"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="foldopen00746"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="foldopen00834"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="foldopen00851"></a>
<a id="l00851"></a>
<a id="l00852"></a>
<a id="l00853"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="foldopen00865"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00869"></a>
<a id="l00870"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="foldopen00882"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="foldopen00888"></a>
<a id="l00888"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="foldopen00899"></a>
<a id="l00899"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="foldopen00926"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="l00971"></a>
<a id="l00972"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="l01010"></a>
<a id="l01011"></a>
<a id="l01013"></a>
<a id="l01014"></a>
<a id="l01016"></a>
<a id="l01017"></a>
<a id="l01019"></a>
<a id="l01020"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01031"></a>
<a id="l01032"></a>
<a id="l01034"></a>
<a id="l01035"></a>
<a id="l01037"></a>
<a id="l01038"></a>
<a id="l01040"></a>
<a id="l01041"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01049"></a>
<a id="l01050"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01055"></a>
<a id="l01056"></a>
<a id="l01058"></a>
<a id="l01059"></a>
<a id="l01064"></a>
<a id="l01065"></a>
<a id="foldopen01074"></a>
<a id="l01074"></a>
<a id="l01075"></a>
<a id="l01076"></a>
<a id="l01081"></a>
<a id="l01082"></a>
<a id="foldopen01092"></a>
<a id="l01092"></a>
<a id="l01093"></a>
<a id="l01094"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01105"></a>
<a id="l01106"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="l01129"></a>
<a id="l01130"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01141"></a>
<a id="l01142"></a>
<a id="l01147"></a>
<a id="l01148"></a>
<a id="l01153"></a>
<a id="l01154"></a>
<a id="l01159"></a>
<a id="l01160"></a>
<a id="l01165"></a>
<a id="l01166"></a>
<a id="l01171"></a>
<a id="l01172"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01183"></a>
<a id="l01184"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="l01195"></a>
<a id="l01196"></a>
<a id="l01201"></a>
<a id="l01202"></a>
<a id="l01207"></a>
<a id="l01208"></a>
<a id="l01210"></a>
<a id="l01211"></a>
<a id="foldopen01220"></a>
<a id="l01220"></a>
<a id="l01221"></a>
<a id="l01222"></a>
<a id="l01227"></a>
<a id="l01228"></a>
<a id="l01233"></a>
<a id="l01234"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="foldopen01246"></a>
<a id="l01246"></a>
<a id="l01247"></a>
<a id="l01248"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="foldopen01266"></a>
<a id="l01266"></a>
<a id="l01267"></a>
<a id="l01268"></a>
<a id="foldopen01272"></a>
<a id="l01272"></a>
<a id="l01274"></a>
<a id="l01275"></a>
<a id="l01277"></a>
<a id="l01278"></a>
<a id="l01280"></a>
<a id="l01281"></a>
<a id="l01283"></a>
<a id="l01284"></a>
<a id="l01286"></a>
<a id="l01287"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="l01292"></a>
<a id="l01293"></a>
<a id="l01295"></a>
<a id="l01296"></a>
<a id="l01298"></a>
<a id="l01299"></a>
<a id="l01300"></a>
<a id="l01327"></a>
<a id="l01329"></a>
<a id="l01330"></a>
<a id="foldopen01338"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01340"></a>
<a id="l01342"></a>
<a id="l01343"></a>
<a id="l01345"></a>
<a id="l01346"></a>
<a id="l01348"></a>
<a id="l01349"></a>
<a id="l01351"></a>
<a id="l01352"></a>
<a id="l01354"></a>
<a id="l01361"></a>
<a id="l01367"></a>
<a id="l01368"></a>
<a id="l01376"></a>
<a id="l01377"></a>
<a id="l01384"></a>
<a id="l01385"></a>
<a id="l01387"></a>
<a id="foldopen01398"></a>
<a id="l01398"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01402"></a>
<a id="l01414"></a>
<a id="l01415"></a>
<a id="l01416"></a>
<a id="l01428"></a>
<a id="l01429"></a>
<a id="l01430"></a>
<a id="l01442"></a>
<a id="l01443"></a>
<a id="l01444"></a>
<a id="l01456"></a>
<a id="l01457"></a>
<a id="l01458"></a>
<a id="l01472"></a>
<a id="l01473"></a>
<a id="l01474"></a>
<a id="l01475"></a>
<a id="l01476"></a>
<a id="foldopen01488"></a>
<a id="l01488"></a>
<a id="l01489"></a>
<a id="l01490"></a>
<a id="l01491"></a>
<a id="l01492"></a>
<a id="l01493"></a>
<a id="foldopen01506"></a>
<a id="l01506"></a>
<a id="l01507"></a>
<a id="l01508"></a>
<a id="l01509"></a>
<a id="l01510"></a>
<a id="l01511"></a>
<a id="l01512"></a>
<a id="l01526"></a>
<a id="l01527"></a>
<a id="l01537"></a>
<a id="l01538"></a>
<a id="l01553"></a>
<a id="l01554"></a>
<a id="l01555"></a>
<a id="l01569"></a>
<a id="l01570"></a>
<a id="l01571"></a>
<a id="l01584"></a>
<a id="l01585"></a>
<a id="l01586"></a>
<a id="l01599"></a>
<a id="l01600"></a>
<a id="l01601"></a>
<a id="l01613"></a>
<a id="l01614"></a>
<a id="foldopen01625"></a>
<a id="l01625"></a>
<a id="l01626"></a>
<a id="l01627"></a>
<a id="l01628"></a>
<a id="l01629"></a>
<a id="foldopen01640"></a>
<a id="l01640"></a>
<a id="l01641"></a>
<a id="l01642"></a>
<a id="l01643"></a>
<a id="l01644"></a>
<a id="foldopen01655"></a>
<a id="l01655"></a>
<a id="l01656"></a>
<a id="l01657"></a>
<a id="l01658"></a>
<a id="l01659"></a>
<a id="foldopen01670"></a>
<a id="l01670"></a>
<a id="l01671"></a>
<a id="l01672"></a>
<a id="l01673"></a>
<a id="l01674"></a>
<a id="l01685"></a>
<a id="l01686"></a>
<a id="foldopen01696"></a>
<a id="l01696"></a>
<a id="l01697"></a>
<a id="l01698"></a>
<a id="l01699"></a>
<a id="l01700"></a>
<a id="foldopen01710"></a>
<a id="l01710"></a>
<a id="l01711"></a>
<a id="l01712"></a>
<a id="l01713"></a>
<a id="l01714"></a>
<a id="foldopen01724"></a>
<a id="l01724"></a>
<a id="l01725"></a>
<a id="l01726"></a>
<a id="l01727"></a>
<a id="l01728"></a>
<a id="foldopen01738"></a>
<a id="l01738"></a>
<a id="l01739"></a>
<a id="l01740"></a>
<a id="l01741"></a>
<a id="l01742"></a>
<a id="l01754"></a>
<a id="l01755"></a>
<a id="l01756"></a>
<a id="l01768"></a>
<a id="l01769"></a>
<a id="l01770"></a>
<a id="l01782"></a>
<a id="l01783"></a>
<a id="l01784"></a>
<a id="l01798"></a>
<a id="l01799"></a>
<a id="l01800"></a>
<a id="l01801"></a>
<a id="l01816"></a>
<a id="l01817"></a>
<a id="l01818"></a>
<a id="l01833"></a>
<a id="l01834"></a>
<a id="l01835"></a>
<a id="l01846"></a>
<a id="l01847"></a>
<a id="l01848"></a>
<a id="l01865"></a>
<a id="l01866"></a>
<a id="l01867"></a>
<a id="l01868"></a>
<a id="l01869"></a>
<a id="foldopen01881"></a>
<a id="l01881"></a>
<a id="l01882"></a>
<a id="l01883"></a>
<a id="l01884"></a>
<a id="l01885"></a>
<a id="l01886"></a>
<a id="l01887"></a>
<a id="l01888"></a>
<a id="foldopen01901"></a>
<a id="l01901"></a>
<a id="l01902"></a>
<a id="l01903"></a>
<a id="l01904"></a>
<a id="l01905"></a>
<a id="l01906"></a>
<a id="l01907"></a>
<a id="l01908"></a>
<a id="l01925"></a>
<a id="l01926"></a>
<a id="l01927"></a>
<a id="l01928"></a>
<a id="l01929"></a>
<a id="foldopen01941"></a>
<a id="l01941"></a>
<a id="l01942"></a>
<a id="l01943"></a>
<a id="l01944"></a>
<a id="l01945"></a>
<a id="l01946"></a>
<a id="l01947"></a>
<a id="l01948"></a>
<a id="foldopen01961"></a>
<a id="l01961"></a>
<a id="l01962"></a>
<a id="l01963"></a>
<a id="l01964"></a>
<a id="l01965"></a>
<a id="l01966"></a>
<a id="l01967"></a>
<a id="l01968"></a>
<a id="l01982"></a>
<a id="l01983"></a>
<a id="l01984"></a>
<a id="l01985"></a>
<a id="l01986"></a>
<a id="l02001"></a>
<a id="l02002"></a>
<a id="l02003"></a>
<a id="l02004"></a>
<a id="l02005"></a>
<a id="l02006"></a>
<a id="l02023"></a>
<a id="l02024"></a>
<a id="l02025"></a>
<a id="l02026"></a>
<a id="l02027"></a>
<a id="l02028"></a>
<a id="l02029"></a>
<a id="l02042"></a>
<a id="l02043"></a>
<a id="l02044"></a>
<a id="l02045"></a>
<a id="l02046"></a>
<a id="l02058"></a>
<a id="l02059"></a>
<a id="l02076"></a>
<a id="l02077"></a>
<a id="l02078"></a>
<a id="l02079"></a>
<a id="l02080"></a>
<a id="foldopen02092"></a>
<a id="l02092"></a>
<a id="l02093"></a>
<a id="l02094"></a>
<a id="l02095"></a>
<a id="l02096"></a>
<a id="l02097"></a>
<a id="l02098"></a>
<a id="l02099"></a>
<a id="foldopen02111"></a>
<a id="l02111"></a>
<a id="l02112"></a>
<a id="l02113"></a>
<a id="l02114"></a>
<a id="l02115"></a>
<a id="l02116"></a>
<a id="l02117"></a>
<a id="l02118"></a>
<a id="foldopen02131"></a>
<a id="l02131"></a>
<a id="l02132"></a>
<a id="l02133"></a>
<a id="l02134"></a>
<a id="l02135"></a>
<a id="l02136"></a>
<a id="l02137"></a>
<a id="l02138"></a>
<a id="l02147"></a>
<a id="l02148"></a>
<a id="l02149"></a>
<a id="l02161"></a>
<a id="l02162"></a>
<a id="l02163"></a>
<a id="l02179"></a>
<a id="l02180"></a>
<a id="l02181"></a>
<a id="l02182"></a>
<a id="l02183"></a>
<a id="l02184"></a>
<a id="l02185"></a>
<a id="l02189"></a>
<a id="l02190"></a>
<a id="adevice_8h_html"></a>
<a id="aerror__types_8h_html_a79ba58b71019ccd9b76f65aaf4ebe1b0"></a>
<a id="agroup__i3c__ccc_html_ga0d4c999391fca23598a4339b6c9d4ad6"></a>
<a id="agroup__i3c__ccc_html_ga0f04a73d8b26b93091108fc55d7a54d3"></a>
<a id="agroup__i3c__ccc_html_ga1977f86d4865a97047119e5b3fbcb172"></a>
<a id="agroup__i3c__ccc_html_ga1a91a7d29fc73ea18b9da614773b475f"></a>
<a id="agroup__i3c__ccc_html_ga1cb2804fc7dcbb322cd26001d7953c95"></a>
<a id="agroup__i3c__ccc_html_ga2542f4ebcc0c2bb31bc8e334955620b0"></a>
<a id="agroup__i3c__ccc_html_ga2a1786ee4a809b50dad7e1d42c9afb0b"></a>
<a id="agroup__i3c__ccc_html_ga35bf3fe8816d9fce44d70c8a3c8f69cb"></a>
<a id="agroup__i3c__ccc_html_ga364bcd9863f82fcc13aeb59ca7ad6504"></a>
<a id="agroup__i3c__ccc_html_ga40294e43357f46338a6542f9a03d7ce7"></a>
<a id="agroup__i3c__ccc_html_ga4cbdcbc2d991bc1e542a562fdbc2563c"></a>
<a id="agroup__i3c__ccc_html_ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb"></a>
<a id="agroup__i3c__ccc_html_ga4fe9d056a5ac78ff83513763a71c7dfe"></a>
<a id="agroup__i3c__ccc_html_ga58a37d7bb50937a936923e3e6b74fc96"></a>
<a id="agroup__i3c__ccc_html_ga5a111a0e9ba5037861585d5356d4e950"></a>
<a id="agroup__i3c__ccc_html_ga5c1b2aa3b5915db2540a1affb17a4f10"></a>
<a id="agroup__i3c__ccc_html_ga600409049ad66072d94d39623977c137"></a>
<a id="agroup__i3c__ccc_html_ga609cbfc817ec24b36c71f75092b2d4bf"></a>
<a id="agroup__i3c__ccc_html_ga61e1a1945a39b374edee5b75fbeb27d1"></a>
<a id="agroup__i3c__ccc_html_ga66c8c6318134d6287f4a14f6c31af02d"></a>
<a id="agroup__i3c__ccc_html_ga66ffb47bf3dcf53c31fbbf6fd451a221"></a>
<a id="agroup__i3c__ccc_html_ga6949426eaf9c3a30dc402e2e11da1dcd"></a>
<a id="agroup__i3c__ccc_html_ga6d19dc9d3b421b4c936c6183977c4eec"></a>
<a id="agroup__i3c__ccc_html_ga6e4f26d23919a619c89624b15d16390a"></a>
<a id="agroup__i3c__ccc_html_ga71e5cbf818b17eb35196ef773b992ed5"></a>
<a id="agroup__i3c__ccc_html_ga72e76917e96f8ac572c42c6598f3bce4"></a>
<a id="agroup__i3c__ccc_html_ga75934ea02ef8eb1c737da3ebfd368648"></a>
<a id="agroup__i3c__ccc_html_ga7ce52b4e19f3721e3b054455be42e3d0"></a>
<a id="agroup__i3c__ccc_html_ga7d5bb9c8fd88721b858180f503c1af4c"></a>
<a id="agroup__i3c__ccc_html_ga7f886c0dbe0afec07f5678b574dc1101"></a>
<a id="agroup__i3c__ccc_html_ga87c42055b8b03871558df6be56dc1bd6"></a>
<a id="agroup__i3c__ccc_html_ga8a74bb1b461c6a4cad12220db55d6d7a"></a>
<a id="agroup__i3c__ccc_html_ga93b5f2cf21cf7a201bf76e3d665fc40f"></a>
<a id="agroup__i3c__ccc_html_ga949810a9a7c862d00ce4eec7e2c4d7df"></a>
<a id="agroup__i3c__ccc_html_ga94df3bbf8d0de54edd57e2ab4d44474e"></a>
<a id="agroup__i3c__ccc_html_gaa14442ecb3768cb4c3c435c0c1138778"></a>
<a id="agroup__i3c__ccc_html_gaa22cc011b619b1819416b0aa26f85958"></a>
<a id="agroup__i3c__ccc_html_gaa58e1bff5cc9b9e4a32ae4159494125b"></a>
<a id="agroup__i3c__ccc_html_gaaa684ac58000e05316eac016a7f048cd"></a>
<a id="agroup__i3c__ccc_html_gaaf692d0b89fd62a61d93f1577b25ce25"></a>
<a id="agroup__i3c__ccc_html_gab1102467bb92a2aff7c9c1a66dd273a7"></a>
<a id="agroup__i3c__ccc_html_gab3c93ba0a6e606508a59e65c931dd144"></a>
<a id="agroup__i3c__ccc_html_gab3de109c73dd58f6d2cf0a9229408f49"></a>
<a id="agroup__i3c__ccc_html_gab5bb29579181747c1b7e1eafa98160e6"></a>
<a id="agroup__i3c__ccc_html_gac4331a4c7dbb7af0eaea63b01bb08485"></a>
<a id="agroup__i3c__ccc_html_gac8bdf8d14db5e7fd06846637253cbb76"></a>
<a id="agroup__i3c__ccc_html_gacf89ee65aafdcab713f30c8e2675e58b"></a>
<a id="agroup__i3c__ccc_html_gad8a5fcaa2dd494f20795ee716ebf0895"></a>
<a id="agroup__i3c__ccc_html_gadf1c0363ec0d6db7634cb03bd2d402c2"></a>
<a id="agroup__i3c__ccc_html_gaeb58d2e7c779ae8e07b185f9fa290a9b"></a>
<a id="agroup__i3c__ccc_html_gaeca8e7c74ee867cdeedf586f5af07a89"></a>
<a id="agroup__i3c__ccc_html_gaeecb153a2cb3bdc196d00fb60c3e3b24"></a>
<a id="agroup__i3c__ccc_html_gaf1077e3d6cf8a7e1f0e02e985058e507"></a>
<a id="agroup__i3c__ccc_html_gaf26a8d605ec5d0e95d6ee1f90571946d"></a>
<a id="agroup__i3c__ccc_html_gaf4836548527c1a7fe54767c2a7e2ebb9"></a>
<a id="agroup__i3c__ccc_html_gaf5fbaf2108053df855c95233181dc580"></a>
<a id="agroup__i3c__ccc_html_gaf6575647b4b8f858f90bf2785a0f0d49"></a>
<a id="agroup__i3c__ccc_html_gaf7b1cbdc790aa1d2c307e1f4ba773ba2"></a>
<a id="agroup__i3c__ccc_html_gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877"></a>
<a id="agroup__i3c__ccc_html_gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19"></a>
<a id="agroup__i3c__ccc_html_gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb"></a>
<a id="agroup__i3c__ccc_html_gga1a91a7d29fc73ea18b9da614773b475fa1bbc19ae8831c87bc3756bf9d8d587f9"></a>
<a id="agroup__i3c__ccc_html_gga1a91a7d29fc73ea18b9da614773b475fa76fbd4e41066bf448f2d39f238ade990"></a>
<a id="agroup__i3c__ccc_html_gga1a91a7d29fc73ea18b9da614773b475fac4b63e2655bce05f0a02c08599208f0c"></a>
<a id="agroup__i3c__ccc_html_gga364bcd9863f82fcc13aeb59ca7ad6504a67ee57431fe7b181792507f9ec7d7207"></a>
<a id="agroup__i3c__ccc_html_gga364bcd9863f82fcc13aeb59ca7ad6504aaf523080c395d41aaf0ea5112d93e530"></a>
<a id="agroup__i3c__ccc_html_gga609cbfc817ec24b36c71f75092b2d4bfa140bcd34752bd931fc44268035a389d6"></a>
<a id="agroup__i3c__ccc_html_gga609cbfc817ec24b36c71f75092b2d4bfa2b24114d14a6d43638c3a226a13abaf7"></a>
<a id="agroup__i3c__ccc_html_gga609cbfc817ec24b36c71f75092b2d4bfad7bea353891962a2942cb0f58fcff2dd"></a>
<a id="agroup__i3c__ccc_html_gga61e1a1945a39b374edee5b75fbeb27d1a0e5a066d008689305ae455bc96b644f4"></a>
<a id="agroup__i3c__ccc_html_gga61e1a1945a39b374edee5b75fbeb27d1a236748388eb84292c65c204b79ae1454"></a>
<a id="agroup__i3c__ccc_html_gga61e1a1945a39b374edee5b75fbeb27d1a30d784f66b28d3a3937e136ec1e38d95"></a>
<a id="agroup__i3c__ccc_html_gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476"></a>
<a id="agroup__i3c__ccc_html_gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519"></a>
<a id="agroup__i3c__ccc_html_gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2"></a>
<a id="agroup__i3c__ccc_html_gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e"></a>
<a id="agroup__i3c__ccc_html_gga61e1a1945a39b374edee5b75fbeb27d1adc3e1d5dfe97ba25fdd1d4d270a65024"></a>
<a id="agroup__i3c__ccc_html_gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879"></a>
<a id="agroup__i3c__ccc_html_gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f"></a>
<a id="agroup__i3c__ccc_html_gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b"></a>
<a id="agroup__i3c__ccc_html_ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0"></a>
<a id="agroup__i3c__ccc_html_ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620"></a>
<a id="agroup__i3c__ccc_html_ggadf1c0363ec0d6db7634cb03bd2d402c2a2081a7f62d3175a8b84454daf54f3484"></a>
<a id="agroup__i3c__ccc_html_ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86"></a>
<a id="agroup__i3c__ccc_html_ggadf1c0363ec0d6db7634cb03bd2d402c2a494b6a8c368d34d96433041de7e7448e"></a>
<a id="agroup__i3c__ccc_html_ggadf1c0363ec0d6db7634cb03bd2d402c2aaf97763f5fe2819c502e3923501c86d0"></a>
<a id="agroup__i3c__ccc_html_ggadf1c0363ec0d6db7634cb03bd2d402c2ab37ceea59619902ac073183694852984"></a>
<a id="agroup__i3c__ccc_html_ggadf1c0363ec0d6db7634cb03bd2d402c2ae4cd2f2c4638057ae8fdcceb9d7ba740"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructi3c__ccc__address_html"></a>
<a id="astructi3c__ccc__address_html_afc3d7db034b3fd72c6118790a18a677b"></a>
<a id="astructi3c__ccc__deftgts__active__controller_html"></a>
<a id="astructi3c__ccc__deftgts__active__controller_html_a4d7671db542bb70ef623be26804c154a"></a>
<a id="astructi3c__ccc__deftgts__active__controller_html_a7acd12fad49f565a6b8a71993b6ad5d4"></a>
<a id="astructi3c__ccc__deftgts__active__controller_html_ae2fb1ebc28ef1f69c6114af0b25875d3"></a>
<a id="astructi3c__ccc__deftgts__active__controller_html_aeb56808d9b998c51d5b30307e0212328"></a>
<a id="astructi3c__ccc__deftgts__target_html"></a>
<a id="astructi3c__ccc__deftgts__target_html_a08689c18d74fa4b74fc2ada055394e65"></a>
<a id="astructi3c__ccc__deftgts__target_html_a34a02df3d4dc456733746437b2cd983a"></a>
<a id="astructi3c__ccc__deftgts__target_html_a7374dd59c060462af7ca366ae7165107"></a>
<a id="astructi3c__ccc__deftgts__target_html_a7c234182e16da66c308e86d72591063d"></a>
<a id="astructi3c__ccc__deftgts__target_html_ab4fbe6aac8d5860ef90613e51b15ef83"></a>
<a id="astructi3c__ccc__deftgts_html"></a>
<a id="astructi3c__ccc__deftgts_html_a1f59c280bd388eb7e7818eb674b5f12f"></a>
<a id="astructi3c__ccc__deftgts_html_a3ead83f46d63c4dd4723ef76dba770ee"></a>
<a id="astructi3c__ccc__deftgts_html_a82a12e711417111855d76171fbd008c2"></a>
<a id="astructi3c__ccc__events_html"></a>
<a id="astructi3c__ccc__events_html_ac34bcdae31cdc718eb54962d6b707320"></a>
<a id="astructi3c__ccc__getbcr_html"></a>
<a id="astructi3c__ccc__getbcr_html_a09df0a49b57a38b91fe2e51c4de5c334"></a>
<a id="astructi3c__ccc__getdcr_html"></a>
<a id="astructi3c__ccc__getdcr_html_a0615f439c4d556b08f7ecba8dff1c007"></a>
<a id="astructi3c__ccc__getpid_html"></a>
<a id="astructi3c__ccc__getpid_html_a060023fcb180e44b39a73c0f955f02c7"></a>
<a id="astructi3c__ccc__mrl_html"></a>
<a id="astructi3c__ccc__mrl_html_a381d52439049c6a13d232e4e94d17335"></a>
<a id="astructi3c__ccc__mrl_html_a7480df4486c9eb8a11581e42ff3b6b67"></a>
<a id="astructi3c__ccc__mwl_html"></a>
<a id="astructi3c__ccc__mwl_html_a5312fa1fc7cc93dfdf88d490352cf08e"></a>
<a id="astructi3c__ccc__payload_html"></a>
<a id="astructi3c__ccc__payload_html_a2a16fe7d2989159e6815f5de92e2953e"></a>
<a id="astructi3c__ccc__payload_html_a3dcab72bf5b627426f963df56514c38d"></a>
<a id="astructi3c__ccc__payload_html_a45b2f35955bbb2bcaf89077e5abf3466"></a>
<a id="astructi3c__ccc__payload_html_a9d0f7efcc7774941f057c2ab0fb14439"></a>
<a id="astructi3c__ccc__payload_html_aa93b97b77f8dff8e931731c1f9edcd86"></a>
<a id="astructi3c__ccc__payload_html_ac52dbf51c5d7903c02c9f149e47a1b0b"></a>
<a id="astructi3c__ccc__payload_html_ae6aa0a3465af855872ae0006def29fea"></a>
<a id="astructi3c__ccc__payload_html_afc1706d47d22300e7fa44754920b2685"></a>
<a id="astructi3c__ccc__payload_html_afcc17965b8bdd0e5e26cd15cebe49cee"></a>
<a id="astructi3c__ccc__setbrgtgt__tgt_html"></a>
<a id="astructi3c__ccc__setbrgtgt__tgt_html_a1dca2717ca9502f11b300a0d9a1fc0e6"></a>
<a id="astructi3c__ccc__setbrgtgt__tgt_html_a6fa24f8354e856031464aaaa2c8fd1bb"></a>
<a id="astructi3c__ccc__setbrgtgt_html"></a>
<a id="astructi3c__ccc__setbrgtgt_html_a9099e2979baca2c3fbbb7a6b781edbf3"></a>
<a id="astructi3c__ccc__setbrgtgt_html_aa019eb13d7da60941382c6e43884b60d"></a>
<a id="astructi3c__ccc__target__payload_html"></a>
<a id="astructi3c__ccc__target__payload_html_a2669978506b20ef01569357fbd3a9eef"></a>
<a id="astructi3c__ccc__target__payload_html_a5ddda39b2aeb2818b389d4df1e25ba0a"></a>
<a id="astructi3c__ccc__target__payload_html_aa09ebbfdff5d9d97be1558a63bb3535e"></a>
<a id="astructi3c__ccc__target__payload_html_abc655b08df77701275038e80bfb5ba85"></a>
<a id="astructi3c__ccc__target__payload_html_ae6091f0b1cc804f9658d941f6ab493ef"></a>
<a id="astructi3c__ccc__target__payload_html_af061d387258ee3e2454ceae0b7c0dcf7"></a>
<a id="astructi3c__device__desc_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="aunioni3c__ccc__getcaps_html"></a>
<a id="aunioni3c__ccc__getcaps_html_a4b09537b6b796aa2b4fb962d7a4c446d"></a>
<a id="aunioni3c__ccc__getcaps_html_a6266e60251e02ed9f1009ce1721adef8"></a>
<a id="aunioni3c__ccc__getcaps_html_a908096a7dc051b59b9953575f9e5bf3b"></a>
<a id="aunioni3c__ccc__getcaps_html_a99f11e2283bde1d4370a792a46ef8bad"></a>
<a id="aunioni3c__ccc__getcaps_html_ab16e2b0e084371a9cbf57abf518f3e7e"></a>
<a id="aunioni3c__ccc__getcaps_html_ac3a378ed34efc38aa2f9605208e24cef"></a>
<a id="aunioni3c__ccc__getcaps_html_ae7ab28922904daa7ef7380f0ddb41cb3"></a>
<a id="aunioni3c__ccc__getcaps_html_afd68057c626bb954cee2b6b46350ebae"></a>
<a id="aunioni3c__ccc__getmxds_html"></a>
<a id="aunioni3c__ccc__getmxds_html_a242470090b40e40f0b0febfba966d766"></a>
<a id="aunioni3c__ccc__getmxds_html_a3782b5dce0db847362b9413a02d90baa"></a>
<a id="aunioni3c__ccc__getmxds_html_a668e1ed30b96a40534d96e4b56ce7e98"></a>
<a id="aunioni3c__ccc__getmxds_html_a6bb902a7335f2244365cde9782659dce"></a>
<a id="aunioni3c__ccc__getmxds_html_a9307643fd53554053b38cda5a0663a13"></a>
<a id="aunioni3c__ccc__getmxds_html_aa3c5a9fa7bc805d4cd63cb3ba774a808"></a>
<a id="aunioni3c__ccc__getmxds_html_ad55160abc13a3ad04d5d6f827714f48b"></a>
<a id="aunioni3c__ccc__getmxds_html_adfb70b06d5e769fccc7630a356067fcd"></a>
<a id="aunioni3c__ccc__getstatus_html"></a>
<a id="aunioni3c__ccc__getstatus_html_a104f75402b9ea4b07c9aafc376349d84"></a>
<a id="aunioni3c__ccc__getstatus_html_a18b3c86f3157b3dfb30dc51127de2b69"></a>
<a id="aunioni3c__ccc__getstatus_html_a23fe55c75741457ea399a6c7074017f6"></a>
<a id="aunioni3c__ccc__getstatus_html_ab7a174cc76dd5da060cf420de1f3093e"></a>
<a id="aunioni3c__ccc__getstatus_html_ac3a7629c6d213beff8ab38863a366b11"></a>
<a id="aunioni3c__ccc__getstatus_html_adbc4805456634d5602ab74c2cde4d903"></a>

```c
/*
 * Copyright 2022 Intel Corporation
 * Copyright 2023 Meta Platforms, Inc. and its affiliates
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_I3C_CCC_H_
#define ZEPHYR_INCLUDE_DRIVERS_I3C_CCC_H_


#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/toolchain.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif

#define I3C_CCC_BROADCAST_MAX_ID                0x7FU

#define I3C_CCC_ENEC(broadcast)                 ((broadcast) ? 0x00U : 0x80U)

#define I3C_CCC_DISEC(broadcast)                ((broadcast) ? 0x01U : 0x81U)

#define I3C_CCC_ENTAS(as, broadcast)            (((broadcast) ? 0x02U : 0x82U) + (as))

#define I3C_CCC_ENTAS0(broadcast)               I3C_CCC_ENTAS(0, broadcast)

#define I3C_CCC_ENTAS1(broadcast)               I3C_CCC_ENTAS(1, broadcast)

#define I3C_CCC_ENTAS2(broadcast)               I3C_CCC_ENTAS(2, broadcast)

#define I3C_CCC_ENTAS3(broadcast)               I3C_CCC_ENTAS(3, broadcast)

#define I3C_CCC_RSTDAA                          0x06U

#define I3C_CCC_ENTDAA                          0x07U

#define I3C_CCC_DEFTGTS                         0x08U

#define I3C_CCC_SETMWL(broadcast)               ((broadcast) ? 0x09U : 0x89U)

#define I3C_CCC_SETMRL(broadcast)               ((broadcast) ? 0x0AU : 0x8AU)

#define I3C_CCC_ENTTM                           0x0BU

#define I3C_CCC_SETBUSCON                       0x0CU

#define I3C_CCC_ENDXFER(broadcast)              ((broadcast) ? 0x12U : 0x92U)

#define I3C_CCC_ENTHDR(x)                       (0x20U + (x))

#define I3C_CCC_ENTHDR0                         0x20U

#define I3C_CCC_ENTHDR1                         0x21U

#define I3C_CCC_ENTHDR2                         0x22U

#define I3C_CCC_ENTHDR3                         0x23U

#define I3C_CCC_ENTHDR4                         0x24U

#define I3C_CCC_ENTHDR5                         0x25U

#define I3C_CCC_ENTHDR6                         0x26U

#define I3C_CCC_ENTHDR7                         0x27U

#define I3C_CCC_SETXTIME(broadcast)             ((broadcast) ? 0x28U : 0x98U)

#define I3C_CCC_SETAASA                         0x29U

#define I3C_CCC_RSTACT(broadcast)               ((broadcast) ? 0x2AU : 0x9AU)

#define I3C_CCC_DEFGRPA                         0x2BU

#define I3C_CCC_RSTGRPA(broadcast)              ((broadcast) ? 0x2CU : 0x9CU)

#define I3C_CCC_MLANE(broadcast)                ((broadcast) ? 0x2DU : 0x9DU)

#define I3C_CCC_VENDOR(broadcast, id)           ((id) + ((broadcast) ? 0x61U : 0xE0U))

#define I3C_CCC_RSTDAA_DC                       0x86U

#define I3C_CCC_SETDASA                         0x87U

#define I3C_CCC_SETNEWDA                        0x88U

#define I3C_CCC_GETMWL                          0x8BU

#define I3C_CCC_GETMRL                          0x8CU

#define I3C_CCC_GETPID                          0x8DU

#define I3C_CCC_GETBCR                          0x8EU

#define I3C_CCC_GETDCR                          0x8FU

#define I3C_CCC_GETSTATUS                       0x90U

#define I3C_CCC_GETACCCR                        0x91U

#define I3C_CCC_SETBRGTGT                       0x93U

#define I3C_CCC_GETMXDS                         0x94U

#define I3C_CCC_GETCAPS                         0x95U

#define I3C_CCC_SETROUTE                        0x96U

#define I3C_CCC_D2DXFER                         0x97U

#define I3C_CCC_GETXTIME                        0x99U

#define I3C_CCC_SETGRPA                         0x9BU

struct i3c_device_desc;

struct i3c_ccc_target_payload {
        uint8_t addr;

        uint8_t rnw:1;

        uint8_t *data;

        size_t data_len;

        size_t num_xfer;

        enum i3c_sdr_controller_error_types err;
};

struct i3c_ccc_payload {
        struct {
                uint8_t id;

                uint8_t *data;

                size_t data_len;

                size_t num_xfer;

                enum i3c_sdr_controller_error_types err;
        } ccc;

        struct {
                struct i3c_ccc_target_payload *payloads;

                size_t num_targets;
        } targets;
};

struct i3c_ccc_events {
        uint8_t events;
} __packed;

#define I3C_CCC_ENEC_EVT_ENINTR         BIT(0)

#define I3C_CCC_ENEC_EVT_ENCR           BIT(1)

#define I3C_CCC_ENEC_EVT_ENHJ           BIT(3)

#define I3C_CCC_ENEC_EVT_ALL            \
        (I3C_CCC_ENEC_EVT_ENINTR | I3C_CCC_ENEC_EVT_ENCR | I3C_CCC_ENEC_EVT_ENHJ)

#define I3C_CCC_DISEC_EVT_DISINTR       BIT(0)

#define I3C_CCC_DISEC_EVT_DISCR         BIT(1)

#define I3C_CCC_DISEC_EVT_DISHJ         BIT(3)

#define I3C_CCC_DISEC_EVT_ALL           \
        (I3C_CCC_DISEC_EVT_DISINTR | I3C_CCC_DISEC_EVT_DISCR | I3C_CCC_DISEC_EVT_DISHJ)

/*
 * Events for both enabling and disabling since
 * they have the same bits.
 */

#define I3C_CCC_EVT_INTR                BIT(0)

#define I3C_CCC_EVT_CR                  BIT(1)

#define I3C_CCC_EVT_HJ                  BIT(3)

#define I3C_CCC_EVT_ALL                 \
        (I3C_CCC_EVT_INTR | I3C_CCC_EVT_CR | I3C_CCC_EVT_HJ)

struct i3c_ccc_mwl {
        uint16_t len;
} __packed;

struct i3c_ccc_mrl {
        uint16_t len;

        uint8_t ibi_len;
} __packed;

struct i3c_ccc_deftgts_active_controller {
        uint8_t addr;

        uint8_t dcr;

        uint8_t bcr;

        uint8_t static_addr;
};

struct i3c_ccc_deftgts_target {
        uint8_t addr;

        union {
                uint8_t dcr;

                uint8_t lvr;
        };

        uint8_t bcr;

        uint8_t static_addr;
};

struct i3c_ccc_deftgts {
        uint8_t count;

        struct i3c_ccc_deftgts_active_controller active_controller;

        struct i3c_ccc_deftgts_target targets[];
} __packed;

enum i3c_ccc_enttm_defbyte {
        ENTTM_EXIT_TEST_MODE = 0x00U,

        ENTTM_VENDOR_TEST_MODE = 0x01U,
};

struct i3c_ccc_address {
        uint8_t addr;
} __packed;

struct i3c_ccc_getpid {
        uint8_t pid[6];
} __packed;

struct i3c_ccc_getbcr {
        uint8_t bcr;
} __packed;

struct i3c_ccc_getdcr {
        uint8_t dcr;
} __packed;


enum i3c_ccc_getstatus_fmt {
        GETSTATUS_FORMAT_1,

        GETSTATUS_FORMAT_2,
};

enum i3c_ccc_getstatus_defbyte {
        GETSTATUS_FORMAT_2_TGTSTAT = 0x00U,

        GETSTATUS_FORMAT_2_PRECR = 0x91U,

        GETSTATUS_FORMAT_2_INVALID = 0x100U
};

union i3c_ccc_getstatus {
        struct {
                uint16_t status;
        } fmt1;

        union {
                uint16_t tgtstat;

                uint16_t precr;

                uint16_t raw_u16;
        } fmt2;
} __packed;

#define I3C_CCC_GETSTATUS_PROTOCOL_ERR                          BIT(5)

#define I3C_CCC_GETSTATUS_ACTIVITY_MODE_MASK                    GENMASK(7U, 6U)

#define I3C_CCC_GETSTATUS_ACTIVITY_MODE(status)                 \
        FIELD_GET(I3C_CCC_GETSTATUS_ACTIVITY_MODE_MASK, (status))

#define I3C_CCC_GETSTATUS_ACTIVITY_MODE_NCH                     0x3

#define I3C_CCC_GETSTATUS_NUM_INT_MASK                          GENMASK(3U, 0U)

#define I3C_CCC_GETSTATUS_NUM_INT(status)                       \
        FIELD_GET(I3C_CCC_GETSTATUS_NUM_INT_MASK, (status))

#define I3C_CCC_GETSTATUS_PRECR_DEEP_SLEEP_DETECTED             BIT(0)

#define I3C_CCC_GETSTATUS_PRECR_HANDOFF_DELAY_NACK              BIT(1)

struct i3c_ccc_setbrgtgt_tgt {
        uint8_t addr;

        uint16_t id;
} __packed;

struct i3c_ccc_setbrgtgt {
        uint8_t count;

        struct i3c_ccc_setbrgtgt_tgt targets[];
} __packed;

enum i3c_ccc_getmxds_fmt {
        GETMXDS_FORMAT_1,

        GETMXDS_FORMAT_2,

        GETMXDS_FORMAT_3,
};

enum i3c_ccc_getmxds_defbyte {
        GETMXDS_FORMAT_3_WRRDTURN = 0x00U,

        GETMXDS_FORMAT_3_CRHDLY = 0x91U,

        GETMXDS_FORMAT_3_INVALID = 0x100,
};


union i3c_ccc_getmxds {
        struct {
                uint8_t maxwr;

                uint8_t maxrd;
        } fmt1;

        struct {
                uint8_t maxwr;

                uint8_t maxrd;

                uint8_t maxrdturn[3];
        } fmt2;

        struct {
                uint8_t wrrdturn[5];

                uint8_t crhdly1;
        } fmt3;
} __packed;

#define I3C_CCC_GETMXDS_MAX_SDR_FSCL_MAX                        0

#define I3C_CCC_GETMXDS_MAX_SDR_FSCL_8MHZ                       1

#define I3C_CCC_GETMXDS_MAX_SDR_FSCL_6MHZ                       2

#define I3C_CCC_GETMXDS_MAX_SDR_FSCL_4MHZ                       3

#define I3C_CCC_GETMXDS_MAX_SDR_FSCL_2MHZ                       4

#define I3C_CCC_GETMXDS_TSCO_8NS                                0

#define I3C_CCC_GETMXDS_TSCO_9NS                                1

#define I3C_CCC_GETMXDS_TSCO_10NS                               2

#define I3C_CCC_GETMXDS_TSCO_11NS                               3

#define I3C_CCC_GETMXDS_TSCO_12NS                               4

#define I3C_CCC_GETMXDS_TSCO_GT_12NS                            7

#define I3C_CCC_GETMXDS_MAXWR_DEFINING_BYTE_SUPPORT             BIT(3)

#define I3C_CCC_GETMXDS_MAXWR_MAX_SDR_FSCL_MASK                 GENMASK(2U, 0U)

#define I3C_CCC_GETMXDS_MAXWR_MAX_SDR_FSCL(maxwr)               \
        FIELD_GET(I3C_CCC_GETMXDS_MAXWR_MAX_SDR_FSCL_MASK, (maxwr))

#define I3C_CCC_GETMXDS_MAXRD_W2R_PERMITS_STOP_BETWEEN          BIT(6)

#define I3C_CCC_GETMXDS_MAXRD_TSCO_MASK                         GENMASK(5U, 3U)

#define I3C_CCC_GETMXDS_MAXRD_TSCO(maxrd)                       \
        FIELD_GET(I3C_CCC_GETMXDS_MAXRD_TSCO_MASK, (maxrd))

#define I3C_CCC_GETMXDS_MAXRD_MAX_SDR_FSCL_MASK                 GENMASK(2U, 0U)

#define I3C_CCC_GETMXDS_MAXRD_MAX_SDR_FSCL(maxrd)               \
        FIELD_GET(I3C_CCC_GETMXDS_MAXRD_MAX_SDR_FSCL_MASK, (maxrd))

#define I3C_CCC_GETMXDS_CRDHLY1_SET_BUS_ACT_STATE               BIT(2)

#define I3C_CCC_GETMXDS_CRDHLY1_CTRL_HANDOFF_ACT_STATE_MASK     GENMASK(1U, 0U)

#define I3C_CCC_GETMXDS_CRDHLY1_CTRL_HANDOFF_ACT_STATE(crhdly1) \
        FIELD_GET(I3C_CCC_GETMXDS_CRDHLY1_CTRL_HANDOFF_ACT_STATE_MASK, (crhdly1))

enum i3c_ccc_getcaps_fmt {
        GETCAPS_FORMAT_1,

        GETCAPS_FORMAT_2,
};

enum i3c_ccc_getcaps_defbyte {
        GETCAPS_FORMAT_2_TGTCAPS = 0x00U,

        GETCAPS_FORMAT_2_TESTPAT = 0x5AU,

        GETCAPS_FORMAT_2_CRCAPS = 0x91U,

        GETCAPS_FORMAT_2_VTCAPS = 0x93U,

        GETCAPS_FORMAT_2_DBGCAPS = 0xD7U,

        GETCAPS_FORMAT_2_INVALID = 0x100,
};

union i3c_ccc_getcaps {
        union {
                uint8_t gethdrcap;

                uint8_t getcaps[4];
        } fmt1;

        union {
                uint8_t tgtcaps[4];

                uint32_t testpat;

                uint8_t crcaps[2];

                uint8_t vtcaps[2];
        } fmt2;
} __packed;

#define I3C_CCC_GETCAPS1_HDR_DDR                                BIT(0)

#define I3C_CCC_GETCAPS1_HDR_TSP                                BIT(1)

#define I3C_CCC_GETCAPS1_HDR_TSL                                BIT(2)

#define I3C_CCC_GETCAPS1_HDR_BT                                 BIT(3)

#define I3C_CCC_GETCAPS1_HDR_MODE(x)                            BIT(x)

#define I3C_CCC_GETCAPS1_HDR_MODE0                              BIT(0)

#define I3C_CCC_GETCAPS1_HDR_MODE1                              BIT(1)

#define I3C_CCC_GETCAPS1_HDR_MODE2                              BIT(2)

#define I3C_CCC_GETCAPS1_HDR_MODE3                              BIT(3)

#define I3C_CCC_GETCAPS1_HDR_MODE4                              BIT(4)

#define I3C_CCC_GETCAPS1_HDR_MODE5                              BIT(5)

#define I3C_CCC_GETCAPS1_HDR_MODE6                              BIT(6)

#define I3C_CCC_GETCAPS1_HDR_MODE7                              BIT(7)

#define I3C_CCC_GETCAPS2_HDRDDR_WRITE_ABORT                     BIT(6)

#define I3C_CCC_GETCAPS2_HDRDDR_ABORT_CRC                       BIT(7)

#define I3C_CCC_GETCAPS2_GRPADDR_CAP_MASK                       GENMASK(5U, 4U)

#define I3C_CCC_GETCAPS2_GRPADDR_CAP(getcaps2)                  \
        FIELD_GET(I3C_CCC_GETCAPS2_GRPADDR_CAP_MASK, (getcaps2))

#define I3C_CCC_GETCAPS2_SPEC_VER_MASK                          GENMASK(3U, 0U)

#define I3C_CCC_GETCAPS2_SPEC_VER(getcaps2)                     \
        FIELD_GET(I3C_CCC_GETCAPS2_SPEC_VER_MASK, (getcaps2))

#define I3C_CCC_GETCAPS3_MLANE_SUPPORT                          BIT(0)

#define I3C_CCC_GETCAPS3_D2DXFER_SUPPORT                        BIT(1)

#define I3C_CCC_GETCAPS3_D2DXFER_IBI_CAPABLE                    BIT(2)

#define I3C_CCC_GETCAPS3_GETCAPS_DEFINING_BYTE_SUPPORT          BIT(3)

#define I3C_CCC_GETCAPS3_GETSTATUS_DEFINING_BYTE_SUPPORT        BIT(4)

#define I3C_CCC_GETCAPS3_HDRBT_CRC32_SUPPORT                    BIT(5)

#define I3C_CCC_GETCAPS3_IBI_MDR_PENDING_READ_NOTIFICATION      BIT(6)

#define I3C_CCC_GETCAPS_TESTPAT1                                0xA5

#define I3C_CCC_GETCAPS_TESTPAT2                                0x5A

#define I3C_CCC_GETCAPS_TESTPAT3                                0xA5

#define I3C_CCC_GETCAPS_TESTPAT4                                0x5A

#define I3C_CCC_GETCAPS_TESTPAT                                 0xA55AA55A

#define I3C_CCC_GETCAPS_CRCAPS1_HJ_SUPPORT                      BIT(0)

#define I3C_CCC_GETCAPS_CRCAPS1_GRP_MANAGEMENT_SUPPORT          BIT(1)

#define I3C_CCC_GETCAPS_CRCAPS1_ML_SUPPORT                      BIT(2)

#define I3C_CCC_GETCAPS_CRCAPS2_IBI_TIR_SUPPORT                 BIT(0)

#define I3C_CCC_GETCAPS_CRCAPS2_CONTROLLER_PASSBACK             BIT(1)

#define I3C_CCC_GETCAPS_CRCAPS2_DEEP_SLEEP_CAPABLE              BIT(2)

#define I3C_CCC_GETCAPS_CRCAPS2_DELAYED_CONTROLLER_HANDOFF      BIT(3)

#define I3C_CCC_GETCAPS_VTCAP1_VITRUAL_TARGET_TYPE_MASK         GENMASK(2U, 0U)

#define I3C_CCC_GETCAPS_VTCAP1_VITRUAL_TARGET_TYPE(vtcap1)      \
        FIELD_GET(I3C_CCC_GETCAPS_VTCAP1_VITRUAL_TARGET_TYPE_MASK, (vtcap1))

#define I3C_CCC_GETCAPS_VTCAP1_SIDE_EFFECTS                     BIT(4)

#define I3C_CCC_GETCAPS_VTCAP1_SHARED_PERIPH_DETECT             BIT(5)

#define I3C_CCC_GETCAPS_VTCAP2_INTERRUPT_REQUESTS_MASK          GENMASK(1U, 0U)

#define I3C_CCC_GETCAPS_VTCAP2_INTERRUPT_REQUESTS(vtcap2)       \
        FIELD_GET(I3C_CCC_GETCAPS_VTCAP2_INTERRUPT_REQUESTS_MASK, (vtcap2))

#define I3C_CCC_GETCAPS_VTCAP2_ADDRESS_REMAPPING                BIT(2)

#define I3C_CCC_GETCAPS_VTCAP2_BUS_CONTEXT_AND_COND_MASK        GENMASK(4U, 3U)

#define I3C_CCC_GETCAPS_VTCAP2_BUS_CONTEXT_AND_COND(vtcap2)     \
        FIELD_GET(I3C_CCC_GETCAPS_VTCAP2_BUS_CONTEXT_AND_COND_MASK, (vtcap2))

enum i3c_ccc_rstact_defining_byte {
        I3C_CCC_RSTACT_NO_RESET = 0x00U,

        I3C_CCC_RSTACT_PERIPHERAL_ONLY = 0x01U,

        I3C_CCC_RSTACT_RESET_WHOLE_TARGET = 0x02U,

        I3C_CCC_RSTACT_DEBUG_NETWORK_ADAPTER = 0x03U,

        I3C_CCC_RSTACT_VIRTUAL_TARGET_DETECT = 0x04U,

        I3C_CCC_RSTACT_RETURN_TIME_TO_RESET_PERIPHERAL = 0x81U,

        I3C_CCC_RSTACT_RETURN_TIME_TO_WHOLE_TARGET = 0x82U,

        I3C_CCC_RSTACT_RETURN_TIME_FOR_DEBUG_NETWORK_ADAPTER_RESET = 0x83U,

        I3C_CCC_RSTACT_RETURN_VIRTUAL_TARGET_INDICATION = 0x84U,
};


#define I3C_CCC_SETBUSCON_I3C_SPEC_MINOR_VER_MASK               GENMASK(3U, 0U)

#define I3C_CCC_SETBUSCON_I3C_SPEC_MINOR_VER(y)                 \
        FIELD_PREP(I3C_CCC_SETBUSCON_I3C_SPEC_MINOR_VER_MASK, (y))

#define I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC                     0

#define I3C_CCC_SETBUSCON_I3C_SPEC_I3C_BASIC_SPEC               BIT(4)

#define I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC_EDITORIAL_1_Y_0     0

#define I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC_EDITORIAL_1_Y_1     BIT(5)



#define I3C_CCC_SETBUSCON_OTHER_STANDARDS_JEDEC_SIDEBAND        128

#define I3C_CCC_SETBUSCON_OTHER_STANDARDS_MCTP                  129

#define I3C_CCC_SETBUSCON_OTHER_STANDARDS_ETSI                  130


static inline bool i3c_ccc_is_payload_broadcast(const struct i3c_ccc_payload *payload)
{
        return (payload->ccc.id <= I3C_CCC_BROADCAST_MAX_ID);
}

int i3c_ccc_do_getbcr(struct i3c_device_desc *target,
                      struct i3c_ccc_getbcr *bcr);

int i3c_ccc_do_getdcr(struct i3c_device_desc *target,
                      struct i3c_ccc_getdcr *dcr);

int i3c_ccc_do_getpid(struct i3c_device_desc *target,
                      struct i3c_ccc_getpid *pid);

int i3c_ccc_do_rstact_all(const struct device *controller,
                          enum i3c_ccc_rstact_defining_byte action);

int i3c_ccc_do_rstact(const struct i3c_device_desc *target,
                          enum i3c_ccc_rstact_defining_byte action,
                          bool get,
                          uint8_t *data);

static inline int i3c_ccc_do_rstact_fmt2(const struct i3c_device_desc *target,
                          enum i3c_ccc_rstact_defining_byte action)
{
        return i3c_ccc_do_rstact(target, action, false, NULL);
}

static inline int i3c_ccc_do_rstact_fmt3(const struct i3c_device_desc *target,
                          enum i3c_ccc_rstact_defining_byte action,
                          uint8_t *data)
{
        return i3c_ccc_do_rstact(target, action, true, data);
}

int i3c_ccc_do_rstdaa(struct i3c_device_desc *target);

int i3c_ccc_do_rstdaa_all(const struct device *controller);

int i3c_ccc_do_setdasa(const struct i3c_device_desc *target,
                          struct i3c_ccc_address da);

int i3c_ccc_do_setnewda(const struct i3c_device_desc *target,
                          struct i3c_ccc_address new_da);

int i3c_ccc_do_events_all_set(const struct device *controller,
                              bool enable, struct i3c_ccc_events *events);

int i3c_ccc_do_events_set(struct i3c_device_desc *target,
                          bool enable, struct i3c_ccc_events *events);

int i3c_ccc_do_entas(const struct i3c_device_desc *target, uint8_t as);

static inline int i3c_ccc_do_entas0(const struct i3c_device_desc *target)
{
        return i3c_ccc_do_entas(target, 0);
}

static inline int i3c_ccc_do_entas1(const struct i3c_device_desc *target)
{
        return i3c_ccc_do_entas(target, 1);
}

static inline int i3c_ccc_do_entas2(const struct i3c_device_desc *target)
{
        return i3c_ccc_do_entas(target, 2);
}

static inline int i3c_ccc_do_entas3(const struct i3c_device_desc *target)
{
        return i3c_ccc_do_entas(target, 3);
}

int i3c_ccc_do_entas_all(const struct device *controller, uint8_t as);

static inline int i3c_ccc_do_entas0_all(const struct device *controller)
{
        return i3c_ccc_do_entas_all(controller, 0);
}

static inline int i3c_ccc_do_entas1_all(const struct device *controller)
{
        return i3c_ccc_do_entas_all(controller, 1);
}

static inline int i3c_ccc_do_entas2_all(const struct device *controller)
{
        return i3c_ccc_do_entas_all(controller, 2);
}

static inline int i3c_ccc_do_entas3_all(const struct device *controller)
{
        return i3c_ccc_do_entas_all(controller, 3);
}

int i3c_ccc_do_setmwl_all(const struct device *controller,
                          const struct i3c_ccc_mwl *mwl);

int i3c_ccc_do_setmwl(const struct i3c_device_desc *target,
                      const struct i3c_ccc_mwl *mwl);

int i3c_ccc_do_getmwl(const struct i3c_device_desc *target,
                      struct i3c_ccc_mwl *mwl);

int i3c_ccc_do_setmrl_all(const struct device *controller,
                          const struct i3c_ccc_mrl *mrl,
                          bool has_ibi_size);

int i3c_ccc_do_setmrl(const struct i3c_device_desc *target,
                      const struct i3c_ccc_mrl *mrl);

int i3c_ccc_do_getmrl(const struct i3c_device_desc *target,
                      struct i3c_ccc_mrl *mrl);

int i3c_ccc_do_enttm(const struct device *controller,
                         enum i3c_ccc_enttm_defbyte defbyte);

int i3c_ccc_do_getstatus(const struct i3c_device_desc *target,
                         union i3c_ccc_getstatus *status,
                         enum i3c_ccc_getstatus_fmt fmt,
                         enum i3c_ccc_getstatus_defbyte defbyte);

static inline int i3c_ccc_do_getstatus_fmt1(const struct i3c_device_desc *target,
                                            union i3c_ccc_getstatus *status)
{
        return i3c_ccc_do_getstatus(target, status,
                                    GETSTATUS_FORMAT_1,
                                    GETSTATUS_FORMAT_2_INVALID);
}

static inline int i3c_ccc_do_getstatus_fmt2(const struct i3c_device_desc *target,
                                            union i3c_ccc_getstatus *status,
                                            enum i3c_ccc_getstatus_defbyte defbyte)
{
        return i3c_ccc_do_getstatus(target, status,
                                    GETSTATUS_FORMAT_2, defbyte);
}

int i3c_ccc_do_getcaps(const struct i3c_device_desc *target,
                         union i3c_ccc_getcaps *caps,
                         enum i3c_ccc_getcaps_fmt fmt,
                         enum i3c_ccc_getcaps_defbyte defbyte);

static inline int i3c_ccc_do_getcaps_fmt1(const struct i3c_device_desc *target,
                                            union i3c_ccc_getcaps *caps)
{
        return i3c_ccc_do_getcaps(target, caps,
                                    GETCAPS_FORMAT_1,
                                    GETCAPS_FORMAT_2_INVALID);
}

static inline int i3c_ccc_do_getcaps_fmt2(const struct i3c_device_desc *target,
                                            union i3c_ccc_getcaps *caps,
                                            enum i3c_ccc_getcaps_defbyte defbyte)
{
        return i3c_ccc_do_getcaps(target, caps,
                                    GETCAPS_FORMAT_2, defbyte);
}

int i3c_ccc_do_setvendor(const struct i3c_device_desc *target,
                        uint8_t id,
                        uint8_t *payload,
                        size_t len);

int i3c_ccc_do_getvendor(const struct i3c_device_desc *target,
                        uint8_t id,
                        uint8_t *payload,
                        size_t len,
                        size_t *num_xfer);

int i3c_ccc_do_getvendor_defbyte(const struct i3c_device_desc *target,
                        uint8_t id,
                        uint8_t defbyte,
                        uint8_t *payload,
                        size_t len,
                        size_t *num_xfer);

int i3c_ccc_do_setvendor_all(const struct device *controller,
                        uint8_t id,
                        uint8_t *payload,
                        size_t len);

int i3c_ccc_do_setaasa_all(const struct device *controller);

int i3c_ccc_do_getmxds(const struct i3c_device_desc *target,
                         union i3c_ccc_getmxds *caps,
                         enum i3c_ccc_getmxds_fmt fmt,
                         enum i3c_ccc_getmxds_defbyte defbyte);

static inline int i3c_ccc_do_getmxds_fmt1(const struct i3c_device_desc *target,
                                            union i3c_ccc_getmxds *caps)
{
        return i3c_ccc_do_getmxds(target, caps,
                                    GETMXDS_FORMAT_1,
                                    GETMXDS_FORMAT_3_INVALID);
}

static inline int i3c_ccc_do_getmxds_fmt2(const struct i3c_device_desc *target,
                                            union i3c_ccc_getmxds *caps)
{
        return i3c_ccc_do_getmxds(target, caps,
                                    GETMXDS_FORMAT_2,
                                        GETMXDS_FORMAT_3_INVALID);
}

static inline int i3c_ccc_do_getmxds_fmt3(const struct i3c_device_desc *target,
                                            union i3c_ccc_getmxds *caps,
                                            enum i3c_ccc_getmxds_defbyte defbyte)
{
        return i3c_ccc_do_getmxds(target, caps,
                                    GETMXDS_FORMAT_3, defbyte);
}

int i3c_ccc_do_deftgts_all(const struct device *controller,
                           struct i3c_ccc_deftgts *deftgts);

int i3c_ccc_do_setbuscon(const struct device *controller,
                                uint8_t *context, uint16_t length);

int i3c_ccc_do_getacccr(const struct i3c_device_desc *target,
                           struct i3c_ccc_address *handoff_address);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_I3C_CCC_H_ */
```

## 23.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 Intel Corporation。

版权（Copyright）：2023 Meta Platforms, Inc. and its affiliates。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 374 行

事件同时用于启用和禁用，因为二者使用相同的位。

### 注释 3：原第 2190 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_I3C_CCC_H_`。

## 23.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ccc_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [i3c_device_desc](../hardware/P401_I3C设备描述符.md)
- [i3c_ccc_target_payload](../hardware/P418_I3C通用命令目标载荷.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#a2669978506b20ef01569357fbd3a9eef)
- [rnw](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#aa09ebbfdff5d9d97be1558a63bb3535e)
- [data](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#abc655b08df77701275038e80bfb5ba85)
- [data_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#a5ddda39b2aeb2818b389d4df1e25ba0a)
- [num_xfer](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#ae6091f0b1cc804f9658d941f6ab493ef)
- [i3c_sdr_controller_error_types](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a79ba58b71019ccd9b76f65aaf4ebe1b0)
- [err](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#af061d387258ee3e2454ceae0b7c0dcf7)
- [i3c_ccc_payload](../hardware/P417_I3C通用命令传输载荷.md)
- [id](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#ae6aa0a3465af855872ae0006def29fea)
- [data](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#ac52dbf51c5d7903c02c9f149e47a1b0b)
- [data_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#afcc17965b8bdd0e5e26cd15cebe49cee)
- [num_xfer](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#a9d0f7efcc7774941f057c2ab0fb14439)
- [err](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#a2a16fe7d2989159e6815f5de92e2953e)
- [ccc](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#a45b2f35955bbb2bcaf89077e5abf3466)
- [payloads](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#a3dcab72bf5b627426f963df56514c38d)
- [num_targets](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#afc1706d47d22300e7fa44754920b2685)
- [targets](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#aa93b97b77f8dff8e931731c1f9edcd86)
- [i3c_ccc_events](../hardware/P411_I3C通用命令事件.md)
- [events](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__events.html#ac34bcdae31cdc718eb54962d6b707320)
- [i3c_ccc_mwl](../hardware/P416_I3C最大写入长度命令数据.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__mwl.html#a5312fa1fc7cc93dfdf88d490352cf08e)
- [i3c_ccc_mrl](../hardware/P415_I3C最大读取长度命令数据.md)
- [len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__mrl.html#a381d52439049c6a13d232e4e94d17335)
- [ibi_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__mrl.html#a7480df4486c9eb8a11581e42ff3b6b67)
- [i3c_ccc_deftgts_active_controller](../hardware/P420_I3C目标清单活动控制器.md)
- [addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__active__controller.html#a4d7671db542bb70ef623be26804c154a)
- [dcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__active__controller.html#a7acd12fad49f565a6b8a71993b6ad5d4)
- [bcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__active__controller.html#aeb56808d9b998c51d5b30307e0212328)
- [static_addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__active__controller.html#ae2fb1ebc28ef1f69c6114af0b25875d3)
- [i3c_ccc_deftgts_target](../hardware/P421_I3C目标清单设备项.md)
- [addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__target.html#a34a02df3d4dc456733746437b2cd983a)
- [dcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__target.html#a08689c18d74fa4b74fc2ada055394e65)
- [lvr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__target.html#ab4fbe6aac8d5860ef90613e51b15ef83)
- [bcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__target.html#a7c234182e16da66c308e86d72591063d)
- [static_addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__target.html#a7374dd59c060462af7ca366ae7165107)
- [i3c_ccc_deftgts](../hardware/P419_I3C目标清单命令数据.md)
- [count](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts.html#a82a12e711417111855d76171fbd008c2)
- [active_controller](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts.html#a1f59c280bd388eb7e7818eb674b5f12f)
- [targets](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts.html#a3ead83f46d63c4dd4723ef76dba770ee)
- [i3c_ccc_enttm_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga364bcd9863f82fcc13aeb59ca7ad6504)
- [ENTTM_EXIT_TEST_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga364bcd9863f82fcc13aeb59ca7ad6504a67ee57431fe7b181792507f9ec7d7207)
- [ENTTM_VENDOR_TEST_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga364bcd9863f82fcc13aeb59ca7ad6504aaf523080c395d41aaf0ea5112d93e530)
- [i3c_ccc_address](../hardware/P410_I3C通用命令地址.md)
- [addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__address.html#afc3d7db034b3fd72c6118790a18a677b)
- [i3c_ccc_getpid](../hardware/P414_I3C预置标识返回数据.md)
- [pid](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__getpid.html#a060023fcb180e44b39a73c0f955f02c7)
- [i3c_ccc_getbcr](../hardware/P412_I3C总线特征返回数据.md)
- [bcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__getbcr.html#a09df0a49b57a38b91fe2e51c4de5c334)
- [i3c_ccc_getdcr](../hardware/P413_I3C设备特征返回数据.md)
- [dcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__getdcr.html#a0615f439c4d556b08f7ecba8dff1c007)
- [i3c_ccc_getstatus_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga75934ea02ef8eb1c737da3ebfd368648)
- [GETSTATUS_FORMAT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b)
- [GETSTATUS_FORMAT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f)
- [i3c_ccc_getstatus_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1977f86d4865a97047119e5b3fbcb172)
- [GETSTATUS_FORMAT_2_TGTSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb)
- [GETSTATUS_FORMAT_2_PRECR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877)
- [GETSTATUS_FORMAT_2_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19)
- [i3c_ccc_getstatus](../hardware/P426_I3C状态返回联合体.md)
- [status](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#a23fe55c75741457ea399a6c7074017f6)
- [fmt1](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#adbc4805456634d5602ab74c2cde4d903)
- [tgtstat](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#a18b3c86f3157b3dfb30dc51127de2b69)
- [precr](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#a104f75402b9ea4b07c9aafc376349d84)
- [raw_u16](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#ab7a174cc76dd5da060cf420de1f3093e)
- [fmt2](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#ac3a7629c6d213beff8ab38863a366b11)
- [i3c_ccc_setbrgtgt_tgt](../hardware/P423_I3C桥接目标设备项.md)
- [addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__setbrgtgt__tgt.html#a6fa24f8354e856031464aaaa2c8fd1bb)
- [id](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__setbrgtgt__tgt.html#a1dca2717ca9502f11b300a0d9a1fc0e6)
- [i3c_ccc_setbrgtgt](../hardware/P422_I3C桥接目标命令数据.md)
- [count](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__setbrgtgt.html#a9099e2979baca2c3fbbb7a6b781edbf3)
- [targets](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__setbrgtgt.html#aa019eb13d7da60941382c6e43884b60d)
- [i3c_ccc_getmxds_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1a91a7d29fc73ea18b9da614773b475f)
- [GETMXDS_FORMAT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1a91a7d29fc73ea18b9da614773b475fa76fbd4e41066bf448f2d39f238ade990)
- [GETMXDS_FORMAT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1a91a7d29fc73ea18b9da614773b475fa1bbc19ae8831c87bc3756bf9d8d587f9)
- [GETMXDS_FORMAT_3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1a91a7d29fc73ea18b9da614773b475fac4b63e2655bce05f0a02c08599208f0c)
- [i3c_ccc_getmxds_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga609cbfc817ec24b36c71f75092b2d4bf)
- [GETMXDS_FORMAT_3_WRRDTURN](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga609cbfc817ec24b36c71f75092b2d4bfad7bea353891962a2942cb0f58fcff2dd)
- [GETMXDS_FORMAT_3_CRHDLY](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga609cbfc817ec24b36c71f75092b2d4bfa2b24114d14a6d43638c3a226a13abaf7)
- [GETMXDS_FORMAT_3_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga609cbfc817ec24b36c71f75092b2d4bfa140bcd34752bd931fc44268035a389d6)
- [i3c_ccc_getmxds](../hardware/P427_I3C最大速度返回联合体.md)
- [maxwr](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#a9307643fd53554053b38cda5a0663a13)
- [maxrd](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#a668e1ed30b96a40534d96e4b56ce7e98)
- [fmt1](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#a242470090b40e40f0b0febfba966d766)
- [maxrdturn](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#a3782b5dce0db847362b9413a02d90baa)
- [fmt2](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#adfb70b06d5e769fccc7630a356067fcd)
- [wrrdturn](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#aa3c5a9fa7bc805d4cd63cb3ba774a808)
- [crhdly1](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#ad55160abc13a3ad04d5d6f827714f48b)
- [fmt3](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#a6bb902a7335f2244365cde9782659dce)
- [i3c_ccc_getcaps_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa22cc011b619b1819416b0aa26f85958)
- [GETCAPS_FORMAT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0)
- [GETCAPS_FORMAT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620)
- [i3c_ccc_getcaps_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadf1c0363ec0d6db7634cb03bd2d402c2)
- [GETCAPS_FORMAT_2_TGTCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2a494b6a8c368d34d96433041de7e7448e)
- [GETCAPS_FORMAT_2_TESTPAT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2ae4cd2f2c4638057ae8fdcceb9d7ba740)
- [GETCAPS_FORMAT_2_CRCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2a2081a7f62d3175a8b84454daf54f3484)
- [GETCAPS_FORMAT_2_VTCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2ab37ceea59619902ac073183694852984)
- [GETCAPS_FORMAT_2_DBGCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2aaf97763f5fe2819c502e3923501c86d0)
- [GETCAPS_FORMAT_2_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86)
- [i3c_ccc_getcaps](../hardware/P428_I3C能力返回联合体.md)
- [gethdrcap](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#ac3a378ed34efc38aa2f9605208e24cef)
- [getcaps](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#ab16e2b0e084371a9cbf57abf518f3e7e)
- [fmt1](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#a908096a7dc051b59b9953575f9e5bf3b)
- [tgtcaps](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#a99f11e2283bde1d4370a792a46ef8bad)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [testpat](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#afd68057c626bb954cee2b6b46350ebae)
- [crcaps](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#a6266e60251e02ed9f1009ce1721adef8)
- [vtcaps](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#ae7ab28922904daa7ef7380f0ddb41cb3)
- [fmt2](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#a4b09537b6b796aa2b4fb962d7a4c446d)
- [i3c_ccc_rstact_defining_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga61e1a1945a39b374edee5b75fbeb27d1)
- [I3C_CCC_RSTACT_NO_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2)
- [I3C_CCC_RSTACT_PERIPHERAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476)
- [I3C_CCC_RSTACT_RESET_WHOLE_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879)
- [I3C_CCC_RSTACT_DEBUG_NETWORK_ADAPTER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519)
- [I3C_CCC_RSTACT_VIRTUAL_TARGET_DETECT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e)
- [I3C_CCC_RSTACT_RETURN_TIME_TO_RESET_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a236748388eb84292c65c204b79ae1454)
- [I3C_CCC_RSTACT_RETURN_TIME_TO_WHOLE_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a30d784f66b28d3a3937e136ec1e38d95)
- [I3C_CCC_RSTACT_RETURN_TIME_FOR_DEBUG_NETWORK_ADAPTER_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1adc3e1d5dfe97ba25fdd1d4d270a65024)
- [I3C_CCC_RSTACT_RETURN_VIRTUAL_TARGET_INDICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a0e5a066d008689305ae455bc96b644f4)
- [i3c_ccc_is_payload_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaaf692d0b89fd62a61d93f1577b25ce25)
- [I3C_CCC_BROADCAST_MAX_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf7b1cbdc790aa1d2c307e1f4ba773ba2)
- [i3c_ccc_do_getbcr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7d5bb9c8fd88721b858180f503c1af4c)
- [i3c_ccc_do_getdcr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7f886c0dbe0afec07f5678b574dc1101)
- [i3c_ccc_do_getpid](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga949810a9a7c862d00ce4eec7e2c4d7df)
- [i3c_ccc_do_rstact_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga40294e43357f46338a6542f9a03d7ce7)
- [device](../device_reference/P002_设备对象结构.md)
- [i3c_ccc_do_rstact](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8a74bb1b461c6a4cad12220db55d6d7a)
- [i3c_ccc_do_rstact_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad8a5fcaa2dd494f20795ee716ebf0895)
- [i3c_ccc_do_rstact_fmt3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf26a8d605ec5d0e95d6ee1f90571946d)
- [i3c_ccc_do_rstdaa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac8bdf8d14db5e7fd06846637253cbb76)
- [i3c_ccc_do_rstdaa_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab1102467bb92a2aff7c9c1a66dd273a7)
- [i3c_ccc_do_setdasa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf4836548527c1a7fe54767c2a7e2ebb9)
- [i3c_ccc_do_setnewda](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga6d19dc9d3b421b4c936c6183977c4eec)
- [i3c_ccc_do_events_all_set](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf5fbaf2108053df855c95233181dc580)
- [i3c_ccc_do_events_set](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf6575647b4b8f858f90bf2785a0f0d49)
- [i3c_ccc_do_entas](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga66ffb47bf3dcf53c31fbbf6fd451a221)
- [i3c_ccc_do_entas0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab5bb29579181747c1b7e1eafa98160e6)
- [i3c_ccc_do_entas1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga600409049ad66072d94d39623977c137)
- [i3c_ccc_do_entas2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeb58d2e7c779ae8e07b185f9fa290a9b)
- [i3c_ccc_do_entas3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga35bf3fe8816d9fce44d70c8a3c8f69cb)
- [i3c_ccc_do_entas_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa14442ecb3768cb4c3c435c0c1138778)
- [i3c_ccc_do_entas0_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga0d4c999391fca23598a4339b6c9d4ad6)
- [i3c_ccc_do_entas1_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga93b5f2cf21cf7a201bf76e3d665fc40f)
- [i3c_ccc_do_entas2_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gacf89ee65aafdcab713f30c8e2675e58b)
- [i3c_ccc_do_entas3_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeecb153a2cb3bdc196d00fb60c3e3b24)
- [i3c_ccc_do_setmwl_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga66c8c6318134d6287f4a14f6c31af02d)
- [i3c_ccc_do_setmwl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab3de109c73dd58f6d2cf0a9229408f49)
- [i3c_ccc_do_getmwl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf1077e3d6cf8a7e1f0e02e985058e507)
- [i3c_ccc_do_setmrl_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2542f4ebcc0c2bb31bc8e334955620b0)
- [i3c_ccc_do_setmrl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga6e4f26d23919a619c89624b15d16390a)
- [i3c_ccc_do_getmrl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac4331a4c7dbb7af0eaea63b01bb08485)
- [i3c_ccc_do_enttm](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5c1b2aa3b5915db2540a1affb17a4f10)
- [i3c_ccc_do_getstatus](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4fe9d056a5ac78ff83513763a71c7dfe)
- [i3c_ccc_do_getstatus_fmt1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1cb2804fc7dcbb322cd26001d7953c95)
- [i3c_ccc_do_getstatus_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb)
- [i3c_ccc_do_getcaps](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga94df3bbf8d0de54edd57e2ab4d44474e)
- [i3c_ccc_do_getcaps_fmt1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeca8e7c74ee867cdeedf586f5af07a89)
- [i3c_ccc_do_getcaps_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaaa684ac58000e05316eac016a7f048cd)
- [i3c_ccc_do_setvendor](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga72e76917e96f8ac572c42c6598f3bce4)
- [i3c_ccc_do_getvendor](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2a1786ee4a809b50dad7e1d42c9afb0b)
- [i3c_ccc_do_getvendor_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4cbdcbc2d991bc1e542a562fdbc2563c)
- [i3c_ccc_do_setvendor_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7ce52b4e19f3721e3b054455be42e3d0)
- [i3c_ccc_do_setaasa_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab3c93ba0a6e606508a59e65c931dd144)
- [i3c_ccc_do_getmxds](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga6949426eaf9c3a30dc402e2e11da1dcd)
- [i3c_ccc_do_getmxds_fmt1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa58e1bff5cc9b9e4a32ae4159494125b)
- [i3c_ccc_do_getmxds_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5a111a0e9ba5037861585d5356d4e950)
- [i3c_ccc_do_getmxds_fmt3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga58a37d7bb50937a936923e3e6b74fc96)
- [i3c_ccc_do_deftgts_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga0f04a73d8b26b93091108fc55d7a54d3)
- [i3c_ccc_do_setbuscon](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga71e5cbf818b17eb35196ef773b992ed5)
- [i3c_ccc_do_getacccr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga87c42055b8b03871558df6be56dc1bd6)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [i3c_ccc_address::addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__address.html#afc3d7db034b3fd72c6118790a18a677b)
- [i3c_ccc_deftgts_active_controller::addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__active__controller.html#a4d7671db542bb70ef623be26804c154a)
- [i3c_ccc_deftgts_active_controller::dcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__active__controller.html#a7acd12fad49f565a6b8a71993b6ad5d4)
- [i3c_ccc_deftgts_active_controller::static_addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__active__controller.html#ae2fb1ebc28ef1f69c6114af0b25875d3)
- [i3c_ccc_deftgts_active_controller::bcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__active__controller.html#aeb56808d9b998c51d5b30307e0212328)
- [i3c_ccc_deftgts_target::dcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__target.html#a08689c18d74fa4b74fc2ada055394e65)
- [i3c_ccc_deftgts_target::addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__target.html#a34a02df3d4dc456733746437b2cd983a)
- [i3c_ccc_deftgts_target::static_addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__target.html#a7374dd59c060462af7ca366ae7165107)
- [i3c_ccc_deftgts_target::bcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__target.html#a7c234182e16da66c308e86d72591063d)
- [i3c_ccc_deftgts_target::lvr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts__target.html#ab4fbe6aac8d5860ef90613e51b15ef83)
- [i3c_ccc_deftgts::active_controller](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts.html#a1f59c280bd388eb7e7818eb674b5f12f)
- [i3c_ccc_deftgts::targets](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts.html#a3ead83f46d63c4dd4723ef76dba770ee)
- [i3c_ccc_deftgts::count](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__deftgts.html#a82a12e711417111855d76171fbd008c2)
- [i3c_ccc_events::events](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__events.html#ac34bcdae31cdc718eb54962d6b707320)
- [i3c_ccc_getbcr::bcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__getbcr.html#a09df0a49b57a38b91fe2e51c4de5c334)
- [i3c_ccc_getdcr::dcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__getdcr.html#a0615f439c4d556b08f7ecba8dff1c007)
- [i3c_ccc_getpid::pid](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__getpid.html#a060023fcb180e44b39a73c0f955f02c7)
- [i3c_ccc_mrl::len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__mrl.html#a381d52439049c6a13d232e4e94d17335)
- [i3c_ccc_mrl::ibi_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__mrl.html#a7480df4486c9eb8a11581e42ff3b6b67)
- [i3c_ccc_mwl::len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__mwl.html#a5312fa1fc7cc93dfdf88d490352cf08e)
- [i3c_ccc_payload::err](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#a2a16fe7d2989159e6815f5de92e2953e)
- [i3c_ccc_payload::payloads](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#a3dcab72bf5b627426f963df56514c38d)
- [i3c_ccc_payload::ccc](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#a45b2f35955bbb2bcaf89077e5abf3466)
- [i3c_ccc_payload::num_xfer](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#a9d0f7efcc7774941f057c2ab0fb14439)
- [i3c_ccc_payload::targets](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#aa93b97b77f8dff8e931731c1f9edcd86)
- [i3c_ccc_payload::data](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#ac52dbf51c5d7903c02c9f149e47a1b0b)
- [i3c_ccc_payload::id](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#ae6aa0a3465af855872ae0006def29fea)
- [i3c_ccc_payload::num_targets](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#afc1706d47d22300e7fa44754920b2685)
- [i3c_ccc_payload::data_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__payload.html#afcc17965b8bdd0e5e26cd15cebe49cee)
- [i3c_ccc_setbrgtgt_tgt::id](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__setbrgtgt__tgt.html#a1dca2717ca9502f11b300a0d9a1fc0e6)
- [i3c_ccc_setbrgtgt_tgt::addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__setbrgtgt__tgt.html#a6fa24f8354e856031464aaaa2c8fd1bb)
- [i3c_ccc_setbrgtgt::count](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__setbrgtgt.html#a9099e2979baca2c3fbbb7a6b781edbf3)
- [i3c_ccc_setbrgtgt::targets](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__setbrgtgt.html#aa019eb13d7da60941382c6e43884b60d)
- [i3c_ccc_target_payload::addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#a2669978506b20ef01569357fbd3a9eef)
- [i3c_ccc_target_payload::data_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#a5ddda39b2aeb2818b389d4df1e25ba0a)
- [i3c_ccc_target_payload::rnw](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#aa09ebbfdff5d9d97be1558a63bb3535e)
- [i3c_ccc_target_payload::data](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#abc655b08df77701275038e80bfb5ba85)
- [i3c_ccc_target_payload::num_xfer](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#ae6091f0b1cc804f9658d941f6ab493ef)
- [i3c_ccc_target_payload::err](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__ccc__target__payload.html#af061d387258ee3e2454ceae0b7c0dcf7)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [i3c_ccc_getcaps::fmt2](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#a4b09537b6b796aa2b4fb962d7a4c446d)
- [i3c_ccc_getcaps::crcaps](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#a6266e60251e02ed9f1009ce1721adef8)
- [i3c_ccc_getcaps::fmt1](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#a908096a7dc051b59b9953575f9e5bf3b)
- [i3c_ccc_getcaps::tgtcaps](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#a99f11e2283bde1d4370a792a46ef8bad)
- [i3c_ccc_getcaps::getcaps](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#ab16e2b0e084371a9cbf57abf518f3e7e)
- [i3c_ccc_getcaps::gethdrcap](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#ac3a378ed34efc38aa2f9605208e24cef)
- [i3c_ccc_getcaps::vtcaps](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#ae7ab28922904daa7ef7380f0ddb41cb3)
- [i3c_ccc_getcaps::testpat](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getcaps.html#afd68057c626bb954cee2b6b46350ebae)
- [i3c_ccc_getmxds::fmt1](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#a242470090b40e40f0b0febfba966d766)
- [i3c_ccc_getmxds::maxrdturn](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#a3782b5dce0db847362b9413a02d90baa)
- [i3c_ccc_getmxds::maxrd](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#a668e1ed30b96a40534d96e4b56ce7e98)
- [i3c_ccc_getmxds::fmt3](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#a6bb902a7335f2244365cde9782659dce)
- [i3c_ccc_getmxds::maxwr](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#a9307643fd53554053b38cda5a0663a13)
- [i3c_ccc_getmxds::wrrdturn](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#aa3c5a9fa7bc805d4cd63cb3ba774a808)
- [i3c_ccc_getmxds::crhdly1](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#ad55160abc13a3ad04d5d6f827714f48b)
- [i3c_ccc_getmxds::fmt2](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getmxds.html#adfb70b06d5e769fccc7630a356067fcd)
- [i3c_ccc_getstatus::precr](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#a104f75402b9ea4b07c9aafc376349d84)
- [i3c_ccc_getstatus::tgtstat](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#a18b3c86f3157b3dfb30dc51127de2b69)
- [i3c_ccc_getstatus::status](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#a23fe55c75741457ea399a6c7074017f6)
- [i3c_ccc_getstatus::raw_u16](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#ab7a174cc76dd5da060cf420de1f3093e)
- [i3c_ccc_getstatus::fmt2](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#ac3a7629c6d213beff8ab38863a366b11)
- [i3c_ccc_getstatus::fmt1](https://docs.zephyrproject.org/latest/doxygen/html/unioni3c__ccc__getstatus.html#adbc4805456634d5602ab74c2cde4d903)

---

[上一章](P022_capture.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P024_cdc_acm.h_源码浏览.md)
