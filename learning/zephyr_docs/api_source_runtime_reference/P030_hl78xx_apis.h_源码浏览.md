---
id: learning.zephyr-docs.api-source-runtime-reference.page-30
title: hl78xx_apis.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_hl78xx\_apis.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h.html)。

## 30.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00062"></a>
<a id="l00068"></a>
<a id="l00074"></a>
<a id="l00075"></a>
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
<a id="foldopen00123"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="foldopen00152"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00165"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="foldopen00188"></a>
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
<a id="foldopen00213"></a>
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
<a id="foldopen00228"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00236"></a>
<a id="l00240"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="foldopen00257"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="foldopen00271"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="foldopen00305"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="foldopen00320"></a>
<a id="l00320"></a>
<a id="l00322"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="foldopen00330"></a>
<a id="l00330"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="foldopen00342"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="foldopen00364"></a>
<a id="l00364"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="foldopen00376"></a>
<a id="l00376"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="foldopen00388"></a>
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
<a id="l00419"></a>
<a id="l00420"></a>
<a id="foldopen00424"></a>
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
<a id="l00453"></a>
<a id="l00454"></a>
<a id="foldopen00458"></a>
<a id="l00458"></a>
<a id="l00460"></a>
<a id="l00462"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00468"></a>
<a id="l00470"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="foldopen00478"></a>
<a id="l00478"></a>
<a id="l00480"></a>
<a id="l00482"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="foldopen00492"></a>
<a id="l00492"></a>
<a id="l00494"></a>
<a id="l00496"></a>
<a id="l00498"></a>
<a id="l00500"></a>
<a id="l00502"></a>
<a id="l00504"></a>
<a id="l00506"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="foldopen00517"></a>
<a id="l00517"></a>
<a id="l00519"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="foldopen00531"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="l00535"></a>
<a id="l00537"></a>
<a id="l00539"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="foldopen00554"></a>
<a id="l00554"></a>
<a id="l00556"></a>
<a id="l00558"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="foldopen00572"></a>
<a id="l00572"></a>
<a id="l00574"></a>
<a id="l00576"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="foldopen00589"></a>
<a id="l00589"></a>
<a id="l00591"></a>
<a id="l00593"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="foldopen00609"></a>
<a id="l00609"></a>
<a id="l00611"></a>
<a id="l00613"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="foldopen00625"></a>
<a id="l00625"></a>
<a id="l00627"></a>
<a id="l00629"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="foldopen00640"></a>
<a id="l00640"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="foldopen00649"></a>
<a id="l00649"></a>
<a id="l00651"></a>
<a id="l00657"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="foldopen00668"></a>
<a id="l00668"></a>
<a id="l00670"></a>
<a id="l00672"></a>
<a id="l00674"></a>
<a id="l00676"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="foldopen00686"></a>
<a id="l00686"></a>
<a id="l00688"></a>
<a id="l00690"></a>
<a id="l00692"></a>
<a id="l00694"></a>
<a id="l00696"></a>
<a id="l00698"></a>
<a id="l00700"></a>
<a id="l00702"></a>
<a id="l00704"></a>
<a id="l00706"></a>
<a id="l00708"></a>
<a id="l00710"></a>
<a id="l00712"></a>
<a id="l00714"></a>
<a id="l00718"></a>
<a id="l00720"></a>
<a id="l00724"></a>
<a id="l00728"></a>
<a id="l00732"></a>
<a id="l00736"></a>
<a id="l00738"></a>
<a id="l00740"></a>
<a id="l00744"></a>
<a id="l00748"></a>
<a id="l00750"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="foldopen00761"></a>
<a id="l00761"></a>
<a id="l00763"></a>
<a id="l00765"></a>
<a id="l00767"></a>
<a id="l00769"></a>
<a id="l00771"></a>
<a id="l00773"></a>
<a id="l00775"></a>
<a id="l00777"></a>
<a id="l00779"></a>
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
<a id="l00800"></a>
<a id="l00801"></a>
<a id="foldopen00808"></a>
<a id="l00808"></a>
<a id="l00810"></a>
<a id="l00812"></a>
<a id="l00814"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="foldopen00825"></a>
<a id="l00825"></a>
<a id="l00827"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="foldopen00838"></a>
<a id="l00838"></a>
<a id="l00840"></a>
<a id="l00842"></a>
<a id="l00844"></a>
<a id="l00846"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="foldopen00857"></a>
<a id="l00857"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00862"></a>
<a id="l00864"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00871"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00875"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00879"></a>
<a id="l00880"></a>
<a id="l00882"></a>
<a id="l00883"></a>
<a id="l00884"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00888"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="l00894"></a>
<a id="l00896"></a>
<a id="l00898"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="foldopen00910"></a>
<a id="l00910"></a>
<a id="l00912"></a>
<a id="l00914"></a>
<a id="l00916"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="foldopen00927"></a>
<a id="l00927"></a>
<a id="l00929"></a>
<a id="l00931"></a>
<a id="l00933"></a>
<a id="l00935"></a>
<a id="l00937"></a>
<a id="l00939"></a>
<a id="l00941"></a>
<a id="l00943"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="foldopen00955"></a>
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
<a id="l00978"></a>
<a id="l00979"></a>
<a id="foldopen00986"></a>
<a id="l00986"></a>
<a id="l00988"></a>
<a id="l00990"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="l01016"></a>
<a id="l01017"></a>
<a id="l01018"></a>
<a id="l01019"></a>
<a id="foldopen01025"></a>
<a id="l01025"></a>
<a id="l01027"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="foldopen01038"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="l01040"></a>
<a id="l01041"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="foldopen01051"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01054"></a>
<a id="l01055"></a>
<a id="l01056"></a>
<a id="l01057"></a>
<a id="l01058"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="l01078"></a>
<a id="l01079"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01083"></a>
<a id="l01084"></a>
<a id="l01085"></a>
<a id="l01095"></a>
<a id="l01096"></a>
<a id="l01097"></a>
<a id="l01098"></a>
<a id="l01100"></a>
<a id="l01101"></a>
<a id="l01102"></a>
<a id="l01103"></a>
<a id="l01112"></a>
<a id="l01113"></a>
<a id="l01114"></a>
<a id="l01115"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01119"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="foldopen01132"></a>
<a id="l01132"></a>
<a id="l01134"></a>
<a id="l01136"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01154"></a>
<a id="l01155"></a>
<a id="l01156"></a>
<a id="l01164"></a>
<a id="l01165"></a>
<a id="foldopen01172"></a>
<a id="l01172"></a>
<a id="l01174"></a>
<a id="l01176"></a>
<a id="l01178"></a>
<a id="l01180"></a>
<a id="l01182"></a>
<a id="l01184"></a>
<a id="l01186"></a>
<a id="l01188"></a>
<a id="l01190"></a>
<a id="l01191"></a>
<a id="l01192"></a>
<a id="l01193"></a>
<a id="l01197"></a>
<a id="l01198"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01226"></a>
<a id="l01227"></a>
<a id="foldopen01233"></a>
<a id="l01233"></a>
<a id="l01235"></a>
<a id="l01237"></a>
<a id="l01239"></a>
<a id="l01241"></a>
<a id="l01243"></a>
<a id="l01245"></a>
<a id="l01247"></a>
<a id="l01249"></a>
<a id="l01250"></a>
<a id="l01251"></a>
<a id="l01252"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="l01266"></a>
<a id="l01267"></a>
<a id="l01291"></a>
<a id="l01292"></a>
<a id="l01303"></a>
<a id="l01304"></a>
<a id="l01305"></a>
<a id="l01317"></a>
<a id="l01318"></a>
<a id="l01319"></a>
<a id="l01332"></a>
<a id="l01333"></a>
<a id="l01334"></a>
<a id="l01347"></a>
<a id="l01348"></a>
<a id="l01349"></a>
<a id="l01350"></a>
<a id="l01363"></a>
<a id="l01364"></a>
<a id="l01365"></a>
<a id="l01376"></a>
<a id="l01377"></a>
<a id="l01388"></a>
<a id="l01389"></a>
<a id="l01400"></a>
<a id="l01401"></a>
<a id="l01409"></a>
<a id="l01410"></a>
<a id="l01411"></a>
<a id="l01428"></a>
<a id="l01429"></a>
<a id="l01441"></a>
<a id="l01442"></a>
<a id="l01460"></a>
<a id="l01461"></a>
<a id="l01475"></a>
<a id="l01476"></a>
<a id="l01489"></a>
<a id="l01490"></a>
<a id="l01491"></a>
<a id="l01505"></a>
<a id="l01506"></a>
<a id="l01507"></a>
<a id="l01508"></a>
<a id="l01509"></a>
<a id="l01522"></a>
<a id="l01523"></a>
<a id="l01538"></a>
<a id="l01539"></a>
<a id="l01540"></a>
<a id="foldopen01554"></a>
<a id="l01554"></a>
<a id="l01555"></a>
<a id="l01556"></a>
<a id="l01557"></a>
<a id="l01558"></a>
<a id="l01559"></a>
<a id="l01560"></a>
<a id="foldopen01574"></a>
<a id="l01574"></a>
<a id="l01575"></a>
<a id="l01576"></a>
<a id="l01577"></a>
<a id="l01578"></a>
<a id="l01579"></a>
<a id="l01580"></a>
<a id="foldopen01589"></a>
<a id="l01589"></a>
<a id="l01590"></a>
<a id="l01591"></a>
<a id="l01592"></a>
<a id="l01593"></a>
<a id="foldopen01602"></a>
<a id="l01602"></a>
<a id="l01603"></a>
<a id="l01604"></a>
<a id="l01605"></a>
<a id="l01606"></a>
<a id="foldopen01615"></a>
<a id="l01615"></a>
<a id="l01616"></a>
<a id="l01617"></a>
<a id="l01618"></a>
<a id="l01619"></a>
<a id="foldopen01632"></a>
<a id="l01632"></a>
<a id="l01633"></a>
<a id="l01634"></a>
<a id="l01635"></a>
<a id="l01636"></a>
<a id="foldopen01648"></a>
<a id="l01648"></a>
<a id="l01649"></a>
<a id="l01650"></a>
<a id="l01651"></a>
<a id="l01652"></a>
<a id="foldopen01662"></a>
<a id="l01662"></a>
<a id="l01663"></a>
<a id="l01664"></a>
<a id="l01665"></a>
<a id="l01666"></a>
<a id="foldopen01682"></a>
<a id="l01682"></a>
<a id="l01683"></a>
<a id="l01684"></a>
<a id="l01685"></a>
<a id="l01686"></a>
<a id="l01687"></a>
<a id="l01688"></a>
<a id="foldopen01698"></a>
<a id="l01698"></a>
<a id="l01699"></a>
<a id="l01700"></a>
<a id="l01701"></a>
<a id="l01702"></a>
<a id="l01703"></a>
<a id="foldopen01718"></a>
<a id="l01718"></a>
<a id="l01719"></a>
<a id="l01720"></a>
<a id="l01721"></a>
<a id="l01722"></a>
<a id="l01723"></a>
<a id="foldopen01742"></a>
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
<a id="foldopen01761"></a>
<a id="l01761"></a>
<a id="l01762"></a>
<a id="l01763"></a>
<a id="l01764"></a>
<a id="l01765"></a>
<a id="foldopen01773"></a>
<a id="l01773"></a>
<a id="l01774"></a>
<a id="l01775"></a>
<a id="l01776"></a>
<a id="l01777"></a>
<a id="foldopen01790"></a>
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
<a id="foldopen01819"></a>
<a id="l01819"></a>
<a id="l01820"></a>
<a id="l01821"></a>
<a id="l01822"></a>
<a id="l01823"></a>
<a id="l01824"></a>
<a id="l01825"></a>
<a id="l01826"></a>
<a id="l01827"></a>
<a id="l01828"></a>
<a id="l01829"></a>
<a id="l01830"></a>
<a id="l01831"></a>
<a id="l01832"></a>
<a id="l01833"></a>
<a id="l01834"></a>
<a id="l01835"></a>
<a id="l01836"></a>
<a id="l01837"></a>
<a id="l01838"></a>
<a id="l01839"></a>
<a id="foldopen01853"></a>
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
<a id="foldopen01873"></a>
<a id="l01873"></a>
<a id="l01874"></a>
<a id="l01875"></a>
<a id="l01876"></a>
<a id="l01877"></a>
<a id="foldopen01885"></a>
<a id="l01885"></a>
<a id="l01886"></a>
<a id="l01887"></a>
<a id="l01888"></a>
<a id="l01889"></a>
<a id="foldopen01897"></a>
<a id="l01897"></a>
<a id="l01898"></a>
<a id="l01899"></a>
<a id="l01900"></a>
<a id="l01901"></a>
<a id="foldopen01909"></a>
<a id="l01909"></a>
<a id="l01910"></a>
<a id="l01911"></a>
<a id="l01912"></a>
<a id="l01913"></a>
<a id="l01931"></a>
<a id="l01932"></a>
<a id="l01953"></a>
<a id="l01954"></a>
<a id="l01968"></a>
<a id="l01969"></a>
<a id="l01987"></a>
<a id="l01988"></a>
<a id="l02009"></a>
<a id="l02010"></a>
<a id="l02020"></a>
<a id="l02021"></a>
<a id="l02028"></a>
<a id="l02029"></a>
<a id="l02041"></a>
<a id="l02042"></a>
<a id="l02053"></a>
<a id="l02054"></a>
<a id="l02067"></a>
<a id="l02068"></a>
<a id="l02081"></a>
<a id="l02082"></a>
<a id="l02099"></a>
<a id="l02100"></a>
<a id="l02125"></a>
<a id="l02126"></a>
<a id="l02135"></a>
<a id="l02136"></a>
<a id="l02166"></a>
<a id="l02167"></a>
<a id="l02190"></a>
<a id="l02191"></a>
<a id="l02203"></a>
<a id="l02204"></a>
<a id="l02214"></a>
<a id="l02215"></a>
<a id="l02229"></a>
<a id="l02230"></a>
<a id="l02238"></a>
<a id="l02239"></a>
<a id="l02251"></a>
<a id="l02252"></a>
<a id="l02265"></a>
<a id="l02266"></a>
<a id="l02267"></a>
<a id="l02281"></a>
<a id="l02282"></a>
<a id="l02294"></a>
<a id="l02295"></a>
<a id="l02310"></a>
<a id="l02311"></a>
<a id="l02322"></a>
<a id="l02323"></a>
<a id="l02343"></a>
<a id="l02344"></a>
<a id="l02345"></a>
<a id="l02356"></a>
<a id="l02357"></a>
<a id="l02358"></a>
<a id="l02359"></a>
<a id="l02360"></a>
<a id="l02361"></a>
<a id="l02363"></a>
<a id="l02364"></a>
<a id="acellular_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__cellular__interface_html_ga168002533ce39996e68bda2c2e92428e"></a>
<a id="agroup__cellular__interface_html_ga7309390ed507748fdb72cf078b8e08a4"></a>
<a id="agroup__cellular__interface_html_ga746c0862b9a5da7c766e42e4d6025f47"></a>
<a id="agroup__cellular__interface_html_gad6e38e31d82075c51933fcbb2ff2de30"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__hl78xx__interface_html_ga0238b9a2de4683369a0be7a6ed481938"></a>
<a id="agroup__hl78xx__interface_html_ga03910e4575bfd4ed439e1c9a0220c7a2"></a>
<a id="agroup__hl78xx__interface_html_ga03c48d45ba1dfcdeabba881f2b1cd936"></a>
<a id="agroup__hl78xx__interface_html_ga051a63a86e9ca353434b23e1adf5d543"></a>
<a id="agroup__hl78xx__interface_html_ga06800817986b9a4b0291cc22c808dfae"></a>
<a id="agroup__hl78xx__interface_html_ga069a0709408fef75514dfaf12bc42cb5"></a>
<a id="agroup__hl78xx__interface_html_ga09f7b39a934d38a2d3da8deefc3d2758"></a>
<a id="agroup__hl78xx__interface_html_ga0b3efb75d166d9d4bf163ffc6bb68fc0"></a>
<a id="agroup__hl78xx__interface_html_ga0d3e4dcb509b56886297f2f451f4d952"></a>
<a id="agroup__hl78xx__interface_html_ga1244a8f6b7e5e488ab596aa5341ad66a"></a>
<a id="agroup__hl78xx__interface_html_ga13ead2b7a66530a1fbe15e5c4d9addeb"></a>
<a id="agroup__hl78xx__interface_html_ga1640ce244f1a4de52efa0b7c33f7b02a"></a>
<a id="agroup__hl78xx__interface_html_ga1dd356d88b67261a642ba50730b31b48"></a>
<a id="agroup__hl78xx__interface_html_ga209d0579899aef4ade5cf8de1251a323"></a>
<a id="agroup__hl78xx__interface_html_ga249a5bf6cdbd69ec930724bf2541de72"></a>
<a id="agroup__hl78xx__interface_html_ga2723fa7f912913d299629fdba4efb130"></a>
<a id="agroup__hl78xx__interface_html_ga298f953be96ab47be40b5440a2573182"></a>
<a id="agroup__hl78xx__interface_html_ga2a471bc1b92dba1e316b2b27e3778e1a"></a>
<a id="agroup__hl78xx__interface_html_ga2bcaada6a58dfbe3658fc6bcb3090fff"></a>
<a id="agroup__hl78xx__interface_html_ga2c4ff4a9b1d5d2530700327e1d4af6e0"></a>
<a id="agroup__hl78xx__interface_html_ga2d26ae6044baac5995f4184abe4faad3"></a>
<a id="agroup__hl78xx__interface_html_ga309cc2c1be1d4006e2ccb8d59cb3e916"></a>
<a id="agroup__hl78xx__interface_html_ga39a3de13bd706571cd7348ea46b7b708"></a>
<a id="agroup__hl78xx__interface_html_ga3e9edd942cbf32b5a2eec259c44e5ee4"></a>
<a id="agroup__hl78xx__interface_html_ga41d66fc0e8681bf6a68f47af5bcacb90"></a>
<a id="agroup__hl78xx__interface_html_ga452b1ee210417569b3cdfc30db25622a"></a>
<a id="agroup__hl78xx__interface_html_ga45a97bfc5f73d1877357dc1f410c61cd"></a>
<a id="agroup__hl78xx__interface_html_ga473c72484a8a758470ff7043de7ab48d"></a>
<a id="agroup__hl78xx__interface_html_ga475545d83cf5fd883fd11fb0db8400ed"></a>
<a id="agroup__hl78xx__interface_html_ga48f504b9bb41d4a13ac592f763aeb207"></a>
<a id="agroup__hl78xx__interface_html_ga4c2dc7d53dd4780d8f1e00e9889248d3"></a>
<a id="agroup__hl78xx__interface_html_ga50bd06a27371c5c79de5bef125d6b5f3"></a>
<a id="agroup__hl78xx__interface_html_ga517a58c85701991214ddb3a9d786f367"></a>
<a id="agroup__hl78xx__interface_html_ga536c21c42099fc04ac85a634ffa41d24"></a>
<a id="agroup__hl78xx__interface_html_ga5453000edbd52c54f7193de4852aa9a8"></a>
<a id="agroup__hl78xx__interface_html_ga563d651fff3621c1e21d7c47d19fd218"></a>
<a id="agroup__hl78xx__interface_html_ga586f65e3f3ea8852261be04ce7ba67ba"></a>
<a id="agroup__hl78xx__interface_html_ga5a1949cd23380056b4ee1775b1e6cc3b"></a>
<a id="agroup__hl78xx__interface_html_ga5d8a5b00f354e98abc2effa560f3bac8"></a>
<a id="agroup__hl78xx__interface_html_ga5f9c8c8087e1e6008f290ddfe42e3d97"></a>
<a id="agroup__hl78xx__interface_html_ga618c248d23a1db1b027333c92adf99a1"></a>
<a id="agroup__hl78xx__interface_html_ga6340324dcb76101c66b902bb9a14dbd3"></a>
<a id="agroup__hl78xx__interface_html_ga6590e5352cbd8ff6ea0580edd64eb0d0"></a>
<a id="agroup__hl78xx__interface_html_ga65f087ad92a0f2bfb15d4f7b627c754f"></a>
<a id="agroup__hl78xx__interface_html_ga694436b7ecedfd934f78afa9f404cadb"></a>
<a id="agroup__hl78xx__interface_html_ga6adcbc5395d078be2fc9c6e62612f603"></a>
<a id="agroup__hl78xx__interface_html_ga6bf75bd8e583b4e076b73268a712977d"></a>
<a id="agroup__hl78xx__interface_html_ga72dfe852d4d6365d80f33b918f631501"></a>
<a id="agroup__hl78xx__interface_html_ga774bbdee241bfb63374fdc74d2353a3d"></a>
<a id="agroup__hl78xx__interface_html_ga79c8b3e0581e6418526b3aa86e6bbb5a"></a>
<a id="agroup__hl78xx__interface_html_ga7b49e4c0cb9fdb2ef8a6baa5fcdd4f2a"></a>
<a id="agroup__hl78xx__interface_html_ga7cc4861b1449b551246204b84779c621"></a>
<a id="agroup__hl78xx__interface_html_ga7cf1c4b11a828c186771200cd00b3bc8"></a>
<a id="agroup__hl78xx__interface_html_ga7d02276973c71eded42d4242a34ca745"></a>
<a id="agroup__hl78xx__interface_html_ga7d4975dffccffac27c9dccb85c02d549"></a>
<a id="agroup__hl78xx__interface_html_ga803bf7a13a7b57477dbfa4d6b3faa14e"></a>
<a id="agroup__hl78xx__interface_html_ga8201489ac8055efa3019ffd8f3201644"></a>
<a id="agroup__hl78xx__interface_html_ga8265e020ad0d8c3e69f2219173530720"></a>
<a id="agroup__hl78xx__interface_html_ga82793d1f4c0c8f03ae27b29afa1c3d3f"></a>
<a id="agroup__hl78xx__interface_html_ga8a864475f6e9673f85ec7c56028992a5"></a>
<a id="agroup__hl78xx__interface_html_ga8abfb51de22c24f1870d2b5f4b3b60ee"></a>
<a id="agroup__hl78xx__interface_html_ga8c28a5a32edb83ea0b0120dd3b00451f"></a>
<a id="agroup__hl78xx__interface_html_ga9018c8332803eaada4083390c40ac3f0"></a>
<a id="agroup__hl78xx__interface_html_ga9198bafcc7c78243fc72ca2b0bc926ed"></a>
<a id="agroup__hl78xx__interface_html_ga95d1ccc5899adf1b2eda6aa0777b7e80"></a>
<a id="agroup__hl78xx__interface_html_ga98af31968e3bf0fc72dea5d56e97e122"></a>
<a id="agroup__hl78xx__interface_html_ga98fde2c3465abce3b4b7d94816bc029c"></a>
<a id="agroup__hl78xx__interface_html_ga9a4429e44439c5ebdd18ccd549f832f5"></a>
<a id="agroup__hl78xx__interface_html_ga9b9da1841754d723cddc103800b141ae"></a>
<a id="agroup__hl78xx__interface_html_ga9bac621e2f74d598329f61cd95b0291b"></a>
<a id="agroup__hl78xx__interface_html_ga9dd8be5c6d35de4122ab5604bf5b17ce"></a>
<a id="agroup__hl78xx__interface_html_ga9e9d288506708b275cc98e508bc8251d"></a>
<a id="agroup__hl78xx__interface_html_gaa1346c7b8b44abae64f59cc8d5fa9c01"></a>
<a id="agroup__hl78xx__interface_html_gaa7cb75a0ef3cd4cb607bb0e3f3b3468f"></a>
<a id="agroup__hl78xx__interface_html_gaab36b1992acffc8b25b8140da1a79577"></a>
<a id="agroup__hl78xx__interface_html_gaad6374b5c5ef64886c6d8fdde0cba3c4"></a>
<a id="agroup__hl78xx__interface_html_gaadcca229cbccc9832734bcc4e2a443e6"></a>
<a id="agroup__hl78xx__interface_html_gab08189be0b4dc7f03428d829f0170bbe"></a>
<a id="agroup__hl78xx__interface_html_gab2c8054a088aa6927aa10f1aed1587ae"></a>
<a id="agroup__hl78xx__interface_html_gab3a63acd15fc9bd6a7d9ded9ed1731fa"></a>
<a id="agroup__hl78xx__interface_html_gab3bcb3ba4cef24971acc41aa0815abe5"></a>
<a id="agroup__hl78xx__interface_html_gab49ab6eb5aa0cfcdea4e6e7bcabd1d48"></a>
<a id="agroup__hl78xx__interface_html_gab4a85c57d2f77c04a887f6552abff48a"></a>
<a id="agroup__hl78xx__interface_html_gab8e5ae21bd129d61735c9cfe3df557d2"></a>
<a id="agroup__hl78xx__interface_html_gaba7b5c599c1b9285b9dcfbae91ac5e7f"></a>
<a id="agroup__hl78xx__interface_html_gabb0e5a4dd5c2e29d62ba27f6022f01f5"></a>
<a id="agroup__hl78xx__interface_html_gabe520e9e9a5e48ab05e238f6b59b8cda"></a>
<a id="agroup__hl78xx__interface_html_gabf8fcaa1b5a59d5a2cac3c467f93c9f8"></a>
<a id="agroup__hl78xx__interface_html_gac08824e4662cb5fcb316e6a0e1e5ba17"></a>
<a id="agroup__hl78xx__interface_html_gac6ed6d4f41003cb2517f802762d5b239"></a>
<a id="agroup__hl78xx__interface_html_gac7291340f8699bb37cd864516615ea05"></a>
<a id="agroup__hl78xx__interface_html_gac9f87f986b0b745bf8e370896113066f"></a>
<a id="agroup__hl78xx__interface_html_gaca72419e4396a45b296a65f89877dbb8"></a>
<a id="agroup__hl78xx__interface_html_gacb02197961c70e98147ae25e4c11d4de"></a>
<a id="agroup__hl78xx__interface_html_gacddf878e52d0642279e147add9c8bdad"></a>
<a id="agroup__hl78xx__interface_html_gad2673b87d730da42b4d2109e849277cc"></a>
<a id="agroup__hl78xx__interface_html_gad39b680650d8a3f1ea20bc18fa6101d4"></a>
<a id="agroup__hl78xx__interface_html_gad564df9a12ad4ee40caeffec1099a93b"></a>
<a id="agroup__hl78xx__interface_html_gadd718f794b24c9610e97f7460519e577"></a>
<a id="agroup__hl78xx__interface_html_gade4999c5b603813020cd52a93687b76f"></a>
<a id="agroup__hl78xx__interface_html_gadfb6a494068c978908ed0bd968b81a5f"></a>
<a id="agroup__hl78xx__interface_html_gae349d6b96ef9ae67b5ed01d0a8fa2cb0"></a>
<a id="agroup__hl78xx__interface_html_gae3e97cdf80470496d6d8542f61f985c0"></a>
<a id="agroup__hl78xx__interface_html_gae3f2ed904a3b0784d64d2d1537ce9564"></a>
<a id="agroup__hl78xx__interface_html_gae50586b4f939abacda6739850c118982"></a>
<a id="agroup__hl78xx__interface_html_gae7102c14fda882e87bff0f0828ab4263"></a>
<a id="agroup__hl78xx__interface_html_gae891e3155a0ebf72433dd58ae4c36512"></a>
<a id="agroup__hl78xx__interface_html_gae9cf9c13242bc674dd7b0b79a69b8f31"></a>
<a id="agroup__hl78xx__interface_html_gaedfc9112048d6c987ee7fefa4e8abd55"></a>
<a id="agroup__hl78xx__interface_html_gaee99182459b5971ebaa7892989b0e8df"></a>
<a id="agroup__hl78xx__interface_html_gaf2ab6a096dff081e7cbbba13b06de3cc"></a>
<a id="agroup__hl78xx__interface_html_gaf34ed3d29904f1a18c0c75a0de4bc727"></a>
<a id="agroup__hl78xx__interface_html_gaf4c623e7bed92b6ea3964b59df04e98e"></a>
<a id="agroup__hl78xx__interface_html_gaf778d092ad7f9b67b0930c0da2375996"></a>
<a id="agroup__hl78xx__interface_html_gaf8cbf3de84df41d7066b9a07f106c17b"></a>
<a id="agroup__hl78xx__interface_html_gafc8c324c2beb2c59c9f15542d06b85ee"></a>
<a id="agroup__hl78xx__interface_html_gga0b3efb75d166d9d4bf163ffc6bb68fc0a0bd84025a4ab914d51e39f1a74dc7794"></a>
<a id="agroup__hl78xx__interface_html_gga0b3efb75d166d9d4bf163ffc6bb68fc0a8a18fd1d142338fa139a926831ed4576"></a>
<a id="agroup__hl78xx__interface_html_gga298f953be96ab47be40b5440a2573182a78b9fd47dd95d556af0924c2070e446d"></a>
<a id="agroup__hl78xx__interface_html_gga298f953be96ab47be40b5440a2573182a7c8d747fe24f8297d84e15955d936b5f"></a>
<a id="agroup__hl78xx__interface_html_gga298f953be96ab47be40b5440a2573182aab03d62c74493d0979c1a94c92d87f8d"></a>
<a id="agroup__hl78xx__interface_html_gga298f953be96ab47be40b5440a2573182aabc6a4c8e676510fe5f10a9acca1d422"></a>
<a id="agroup__hl78xx__interface_html_gga298f953be96ab47be40b5440a2573182abc0346af5e00e8f506effb9a6fc0694e"></a>
<a id="agroup__hl78xx__interface_html_gga298f953be96ab47be40b5440a2573182aea5264d590f823740963f57f8a2da91b"></a>
<a id="agroup__hl78xx__interface_html_gga298f953be96ab47be40b5440a2573182af80d7346afa3c9211e9280b5eede507b"></a>
<a id="agroup__hl78xx__interface_html_gga2a471bc1b92dba1e316b2b27e3778e1aa3f501dc908e8d5d0ee0019cb9f8560e8"></a>
<a id="agroup__hl78xx__interface_html_gga2a471bc1b92dba1e316b2b27e3778e1aa6182b271f30b1823a5b78e7a8b2e5306"></a>
<a id="agroup__hl78xx__interface_html_gga2a471bc1b92dba1e316b2b27e3778e1aa6c26e21bea35d8b23dd4002efb4a2d7d"></a>
<a id="agroup__hl78xx__interface_html_gga2a471bc1b92dba1e316b2b27e3778e1aa81de01932f8017e5c3cf866dbef309fa"></a>
<a id="agroup__hl78xx__interface_html_gga2a471bc1b92dba1e316b2b27e3778e1aaa444e753e453772c2ef68b49c3287407"></a>
<a id="agroup__hl78xx__interface_html_gga2d26ae6044baac5995f4184abe4faad3a7f3d8e1bf25092ed400496af83401164"></a>
<a id="agroup__hl78xx__interface_html_gga2d26ae6044baac5995f4184abe4faad3a96b0936754b3effa667deb39fabf6d4c"></a>
<a id="agroup__hl78xx__interface_html_gga2d26ae6044baac5995f4184abe4faad3a9dbc87f548dc297b1394c8c287a841b9"></a>
<a id="agroup__hl78xx__interface_html_gga39a3de13bd706571cd7348ea46b7b708a4c54c1a19aa628006b2ee6fb784678cf"></a>
<a id="agroup__hl78xx__interface_html_gga39a3de13bd706571cd7348ea46b7b708a727707489a7b4c16d6d0349c0444b570"></a>
<a id="agroup__hl78xx__interface_html_gga39a3de13bd706571cd7348ea46b7b708a9abfd8982d4ea25916070a82159e6cba"></a>
<a id="agroup__hl78xx__interface_html_gga50bd06a27371c5c79de5bef125d6b5f3ad1b7771088c528180c76181808e03a5e"></a>
<a id="agroup__hl78xx__interface_html_gga50bd06a27371c5c79de5bef125d6b5f3adeb8cba23aae92a082bebac7d3417985"></a>
<a id="agroup__hl78xx__interface_html_gga50bd06a27371c5c79de5bef125d6b5f3ae77730c9d1ad65be888ef47b160b114a"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a170bcb630bb629befdbfa836d6a00184"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a19574b7c2279ac2111df8e6d3186eea5"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a29d93a08da20d42c8178106f6367edbc"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a2af43270aca8930bd5aae44310e20ed1"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a40fd91ef5c30f68f5b6c2c966b06164f"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a51d8ee5b26b38415c00552ecab2714c2"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a5cf687bbb0be75db70158ef8724237c0"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a6056a26520c397f481233b759e20dbf2"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a61ffcb6d724c54639b580f3ef1416339"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a6e6c598f1193635add06421bf6072fc5"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a72a0e1beddb3fe3b261e10fac9d7b608"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a8c3fa8220a8971da702a89cb79789458"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a972aa73ba08dd231d784798bd50652f6"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8a9c10f1f3de92bc942fa1734b0263887d"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8aa3788211847f2604336a77c9ac63ee68"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8ab183f795c85e3909e256e8d09c105fbd"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8ad08eb04d48c458947c509ef780288fe7"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8ad4765a0d1b65fdfdbab81ad7510d91f8"></a>
<a id="agroup__hl78xx__interface_html_gga5453000edbd52c54f7193de4852aa9a8aec2dc59ad43eab4575e32f9ba5aa874a"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218a17d48aff76cf0944dd083add04d84650"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218a1c82ba0582491b289046298ae2f61b5f"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218a286208af6eb57a95635704a6658d653c"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218a29ba014d1f42f7492a37d1cd4291d771"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218a426d3785c73439e6b07cdd97ac564d73"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218a6914647a87d666f23268476b9ed6fa48"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218a78924a7342c9ba71264d2cb29379cebe"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218a7f2a1a1848dcd438e62db93ef54be520"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218a877dbafbeb15642bda562893e80dd3fc"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218a89dfb37411db5f120730745a9b8ff34c"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218a9167f4df382bca60ae4b97c1f12f59cb"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218ac98b93ea01bf22bd8d9e6bc8b5fb5da4"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218ad5e1d9aea137483f37e7312d7581818a"></a>
<a id="agroup__hl78xx__interface_html_gga563d651fff3621c1e21d7c47d19fd218ae589e3849313befefdee8a469a8754f6"></a>
<a id="agroup__hl78xx__interface_html_gga5d8a5b00f354e98abc2effa560f3bac8a300a530cffa64e515acc0791cc2e6db8"></a>
<a id="agroup__hl78xx__interface_html_gga5d8a5b00f354e98abc2effa560f3bac8a66047ead9b0c480d98552c448a83b5c5"></a>
<a id="agroup__hl78xx__interface_html_gga5d8a5b00f354e98abc2effa560f3bac8aafe6e1f8916befffd919fbb2c6de268a"></a>
<a id="agroup__hl78xx__interface_html_gga618c248d23a1db1b027333c92adf99a1a002353fb154ae25fcd8be8a7aea959fc"></a>
<a id="agroup__hl78xx__interface_html_gga618c248d23a1db1b027333c92adf99a1af3eaf31074c112910f9bbf2a255a99c8"></a>
<a id="agroup__hl78xx__interface_html_gga6340324dcb76101c66b902bb9a14dbd3a851e1360c22aae25876472dce866e93b"></a>
<a id="agroup__hl78xx__interface_html_gga6340324dcb76101c66b902bb9a14dbd3aca289a9bee6ebfa5e8b67fb221a8d5c1"></a>
<a id="agroup__hl78xx__interface_html_gga6340324dcb76101c66b902bb9a14dbd3ad9cb3a49a3624deab7bfd971c2c2b7aa"></a>
<a id="agroup__hl78xx__interface_html_gga7d4975dffccffac27c9dccb85c02d549aa553e73835a42bf35fe48e9632343288"></a>
<a id="agroup__hl78xx__interface_html_gga7d4975dffccffac27c9dccb85c02d549afb0c667dcd64c3bb41b73e06d286f16d"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a03122d21581271713faf37256588f8ae"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a0c5a07183e824fe03b89e64758ca7bb7"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a0cee4285190ea2c146f12860d06d9a95"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a1b387e9b0671d132fd67bdbd66855f52"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a21d1935e59ebf795d89d5a82165af2a5"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a28cdd117df9b2826b1068c6618a8fc73"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a3068a58b1b38ee45d773a98970e13b07"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a3d815405a16ae0ed27853462ec7e3790"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a4aac4ed8583b9a578df0520b2c60bc92"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a4f0a0834200a910bc1a18a3249bb5cb3"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a5453982090bb38fe747dac48a52dacb5"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a57bb01f9d4adbe81580e3d9ced2c904b"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a59235d90a373eeb25f6d0e832f2e1e63"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a63c67068793c9fabf8b67c8789a4a839"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a66e68cb9d725de54d218d569e95734fc"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a72df7d50699f4f96d02325f542f614b9"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a825fbf232cbc47a437f9d4e8783485a8"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5a9190aa3603a2f9393aaa9973e5924254"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5ac45e32555ac3905a997b6a198b8de7e5"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5ac87cc0d645f9902639957a963bd3b916"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5acd94ee0ae192d395930d750990970429"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5acfdaea2981c12857c3b798a94dfb56fe"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5ada32d74ea1b57da33c35cd7df917b9d6"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5ade12f00ad30395eb347351368c36ba61"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5aef6a7387e9e4529a150177da1eae3e4c"></a>
<a id="agroup__hl78xx__interface_html_gga8a864475f6e9673f85ec7c56028992a5afb198b40593360402b9b207fd7f633a2"></a>
<a id="agroup__hl78xx__interface_html_gga95d1ccc5899adf1b2eda6aa0777b7e80a2870c278c34bf045a74044f7f9b06533"></a>
<a id="agroup__hl78xx__interface_html_gga95d1ccc5899adf1b2eda6aa0777b7e80a366a2b67d8d3f26e32b420bb3b93e8da"></a>
<a id="agroup__hl78xx__interface_html_gga95d1ccc5899adf1b2eda6aa0777b7e80a804ea78a9bdd6f7ddc431e7110bdb740"></a>
<a id="agroup__hl78xx__interface_html_gga95d1ccc5899adf1b2eda6aa0777b7e80aed8b14739dd868eb2eef60c344814c21"></a>
<a id="agroup__hl78xx__interface_html_gga9b9da1841754d723cddc103800b141aea297ff80ceab088eaa0d9bcc1e15513cd"></a>
<a id="agroup__hl78xx__interface_html_gga9b9da1841754d723cddc103800b141aead514153518fec842a1b6cc921732d00e"></a>
<a id="agroup__hl78xx__interface_html_ggaadcca229cbccc9832734bcc4e2a443e6a2a33182a8e9f3af2f855911d3efb86cd"></a>
<a id="agroup__hl78xx__interface_html_ggaadcca229cbccc9832734bcc4e2a443e6a833446e30f39a5774ec64960d034d7f8"></a>
<a id="agroup__hl78xx__interface_html_ggaadcca229cbccc9832734bcc4e2a443e6ae51b7e16678087c053836e9e1e292aca"></a>
<a id="agroup__hl78xx__interface_html_ggab4a85c57d2f77c04a887f6552abff48aa05d1dd567db7374cd3d014bc09f520f9"></a>
<a id="agroup__hl78xx__interface_html_ggab4a85c57d2f77c04a887f6552abff48aa10412ece169f6a904dfe27e0f5bd40db"></a>
<a id="agroup__hl78xx__interface_html_ggab4a85c57d2f77c04a887f6552abff48aa10eb8b82197b435825210acc3a82d294"></a>
<a id="agroup__hl78xx__interface_html_ggab4a85c57d2f77c04a887f6552abff48aa256929b0f7607ed5cff628c6f4341cf3"></a>
<a id="agroup__hl78xx__interface_html_ggab4a85c57d2f77c04a887f6552abff48aab925138725807800ac98b509e1340820"></a>
<a id="agroup__hl78xx__interface_html_ggab4a85c57d2f77c04a887f6552abff48aaeac806332373d0add288ca9eabc9aee6"></a>
<a id="agroup__hl78xx__interface_html_ggab4a85c57d2f77c04a887f6552abff48aafce279daf75ac9295638671573a7983f"></a>
<a id="agroup__hl78xx__interface_html_ggabb0e5a4dd5c2e29d62ba27f6022f01f5a2a896155562e45fbf018196122a2172f"></a>
<a id="agroup__hl78xx__interface_html_ggabb0e5a4dd5c2e29d62ba27f6022f01f5a545f725ef187285b754c8ffd1a7cafa1"></a>
<a id="agroup__hl78xx__interface_html_ggabb0e5a4dd5c2e29d62ba27f6022f01f5a6b3402a65141facc4a321d128279ebd3"></a>
<a id="agroup__hl78xx__interface_html_ggabb0e5a4dd5c2e29d62ba27f6022f01f5a70a8a01cbbc9b852868f3ac89de2ddf9"></a>
<a id="agroup__hl78xx__interface_html_ggabb0e5a4dd5c2e29d62ba27f6022f01f5a77298645730698245d50ffd96ceb9589"></a>
<a id="agroup__hl78xx__interface_html_ggabb0e5a4dd5c2e29d62ba27f6022f01f5ad00f384fd5b1219ec6c6a20f5bce96bf"></a>
<a id="agroup__hl78xx__interface_html_ggabb0e5a4dd5c2e29d62ba27f6022f01f5af082d7aaf20780a7d92b34a2ac4a0c5c"></a>
<a id="agroup__hl78xx__interface_html_ggabb0e5a4dd5c2e29d62ba27f6022f01f5af39367ee7f46f704f35a04064b34c70d"></a>
<a id="agroup__hl78xx__interface_html_ggae891e3155a0ebf72433dd58ae4c36512a4e37f5ae41b41f0ab34cdad64a406a94"></a>
<a id="agroup__hl78xx__interface_html_ggae891e3155a0ebf72433dd58ae4c36512abc6511482660d1cbc9028c7a9c416dda"></a>
<a id="agroup__hl78xx__interface_html_ggae891e3155a0ebf72433dd58ae4c36512afffc6763941b03be63aa4a96b6442553"></a>
<a id="agroup__hl78xx__interface_html_ggae9cf9c13242bc674dd7b0b79a69b8f31a14ac3c208659e6be45c0502d30b8b876"></a>
<a id="agroup__hl78xx__interface_html_ggae9cf9c13242bc674dd7b0b79a69b8f31a4bb4b3122461421478ca130f26e3b3d8"></a>
<a id="agroup__hl78xx__interface_html_ggae9cf9c13242bc674dd7b0b79a69b8f31a8a74f2b00cd4c4e46e64132cc196f06a"></a>
<a id="agroup__hl78xx__interface_html_ggae9cf9c13242bc674dd7b0b79a69b8f31aafcbffebe034104de9ac4d75a78af816"></a>
<a id="agroup__hl78xx__interface_html_ggae9cf9c13242bc674dd7b0b79a69b8f31abba715db73ee7a99fffab7777be47459"></a>
<a id="agroup__hl78xx__interface_html_ggae9cf9c13242bc674dd7b0b79a69b8f31acaef50b4e3d06dfdc3c703dae8d82e34"></a>
<a id="agroup__hl78xx__interface_html_ggaf2ab6a096dff081e7cbbba13b06de3cca61375a298461738b794a8788618cc72f"></a>
<a id="agroup__hl78xx__interface_html_ggaf2ab6a096dff081e7cbbba13b06de3cca90e58676ada0b8eb4edbda7c8a5f88ca"></a>
<a id="agroup__hl78xx__interface_html_ggaf2ab6a096dff081e7cbbba13b06de3cca9ce65ccd085dc64dc47dcde5880edf30"></a>
<a id="agroup__hl78xx__interface_html_ggaf2ab6a096dff081e7cbbba13b06de3ccafd6bdf61c89c8ca8a24ae7095107a850"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructdevice_html"></a>
<a id="astructhl78xx__agnss__status_html"></a>
<a id="astructhl78xx__agnss__status_html_a5c3fa9011d3d5e71d5aaacc0ecfe7e95"></a>
<a id="astructhl78xx__agnss__status_html_a5e7e0613597dad81c06ca0b7b48a0aba"></a>
<a id="astructhl78xx__agnss__status_html_aa17d6323d9faeb81b1d3299898166a0b"></a>
<a id="astructhl78xx__agnss__status_html_aead701aedc1734a4f89bd628030b0850"></a>
<a id="astructhl78xx__at__monitor__entry_html"></a>
<a id="astructhl78xx__at__monitor__entry_html_a0ce16aebf50d69f6dbece9f34b1afe1c"></a>
<a id="astructhl78xx__at__monitor__entry_html_a0dbf62a2521370ab77e9edb1ea3f728a"></a>
<a id="astructhl78xx__at__monitor__entry_html_a378b71d4ebac3e4de62dcae118abe218"></a>
<a id="astructhl78xx__at__monitor__entry_html_a718aac1e812cf9466bb263cc3369533e"></a>
<a id="astructhl78xx__at__monitor__entry_html_a7d8c73e1cb6c9ddde19aa05c75e941c8"></a>
<a id="astructhl78xx__at__monitor__entry_html_aa8e084c925d5b57524c722f74f1b629c"></a>
<a id="astructhl78xx__at__monitor__entry_html_ad6d1767212a7cf7f69b113e55b56b99f"></a>
<a id="astructhl78xx__at__monitor__entry_html_af5f4bcca2ba5a4e9670694182ed8f6eb"></a>
<a id="astructhl78xx__at__monitor__entry_html_af7417e320aa5dabb1283d5593f4166fd"></a>
<a id="astructhl78xx__at__notification_html"></a>
<a id="astructhl78xx__at__notification_html_a36fd5f326795ace901b6ab0dc22ef934"></a>
<a id="astructhl78xx__at__notification_html_ac5e4004e705d5675716603171582a01c"></a>
<a id="astructhl78xx__at__notification_html_ad2cd1746e6a6eb2cca28d831de31d798"></a>
<a id="astructhl78xx__ctzeu__update_html"></a>
<a id="astructhl78xx__ctzeu__update_html_a0c90dddc2087e97afd6da421a7862323"></a>
<a id="astructhl78xx__ctzeu__update_html_a3b4a66b56a5632a7dc7a4964f949f7b1"></a>
<a id="astructhl78xx__ctzeu__update_html_a5e0f09445a9abda3c5f0b37b97473815"></a>
<a id="astructhl78xx__ctzeu__update_html_a9f0db53ae132db9a43e6a00b93807145"></a>
<a id="astructhl78xx__ctzeu__update_html_ae5eba83a8def3c9720797fd2f1ff46d0"></a>
<a id="astructhl78xx__cxreg__status_html"></a>
<a id="astructhl78xx__cxreg__status_html_a1b1616b638324a1073a81e2c51d7082a"></a>
<a id="astructhl78xx__cxreg__status_html_a4b5acff39666484d3aa7f4920a33c195"></a>
<a id="astructhl78xx__cxreg__status_html_a60f715d0323fa365590d6e6eb8f276fa"></a>
<a id="astructhl78xx__cxreg__status_html_a6c744edb85c63395147b1b55da6dcc9d"></a>
<a id="astructhl78xx__cxreg__status_html_a8674887283917c025827e2d24e07aa21"></a>
<a id="astructhl78xx__cxreg__status_html_a90f9a217168113e3b223e6fee7d3a484"></a>
<a id="astructhl78xx__cxreg__status_html_aa5277387244ff33df4622bcd966138d2"></a>
<a id="astructhl78xx__cxreg__status_html_aa79861dc75aa6db380d719bd291d6297"></a>
<a id="astructhl78xx__cxreg__status_html_aaec559842aa44a208c800c1056dc1960"></a>
<a id="astructhl78xx__cxreg__status_html_ab93a65b47faea7a583313bd74ea2be24"></a>
<a id="astructhl78xx__cxreg__status_html_ac35cd02f962b64890911b0792d7310e0"></a>
<a id="astructhl78xx__cxreg__status_html_ac5661b4086fb1be97cb562ac0080303c"></a>
<a id="astructhl78xx__cxreg__status_html_ae28a6c477536c15740ec07615b156d37"></a>
<a id="astructhl78xx__cxreg__status_html_aeb8daf30feb1b4c82888f5ce393b2adf"></a>
<a id="astructhl78xx__cxreg__status_html_afc07b878db1a4ebd74c1b642c5222866"></a>
<a id="astructhl78xx__evt__monitor__entry_html"></a>
<a id="astructhl78xx__evt__monitor__entry_html_a3c4abc63ba2c55c2e5e718a4873187bb"></a>
<a id="astructhl78xx__evt__monitor__entry_html_a4dbe58f2974287076a4629d9ca1ebe77"></a>
<a id="astructhl78xx__evt__monitor__entry_html_aa17d06c0c99da863e3eabecc43c89b7b"></a>
<a id="astructhl78xx__evt__monitor__entry_html_aac567b983a9bde01f6d34f6376c1c3c5"></a>
<a id="astructhl78xx__evt__monitor__entry_html_aad60b03dc6f1a53b0eaebd4c2e90bf77"></a>
<a id="astructhl78xx__evt__monitor__entry_html_ab53ac16078049c955f04edd1f26a6b7f"></a>
<a id="astructhl78xx__evt__monitor__entry_html_acb7a79b0dca67c9a719494c97ab3e710"></a>
<a id="astructhl78xx__evt__monitor__entry_html_ae1af8f99fe962deaf80f13f3d61552e3"></a>
<a id="astructhl78xx__evt_html"></a>
<a id="astructhl78xx__evt_html_a0943763d4df0904b6fd6299f405dc0b4"></a>
<a id="astructhl78xx__evt_html_a3dbdb39cc7be1dd57a965f7d4a86aebc"></a>
<a id="astructhl78xx__evt_html_a83a493750d68fca89be51eddd700dae1"></a>
<a id="astructhl78xx__evt_html_a8b207883087d39a428f02f1cc4997043"></a>
<a id="astructhl78xx__evt_html_aa142ce76ffc686074b6955437633feea"></a>
<a id="astructhl78xx__evt_html_aabfc3cb2d27cb2a1d7a473af9a6ad621"></a>
<a id="astructhl78xx__evt_html_abf9091f1c192664a55b7a8a50e21ee44"></a>
<a id="astructhl78xx__evt_html_ac919edeb1b552ce726527b20580303de"></a>
<a id="astructhl78xx__evt_html_accf5c9a1709eb7181aab995267757584"></a>
<a id="astructhl78xx__evt_html_ace5b13c268479f1e8a143e1673c4ea73"></a>
<a id="astructhl78xx__evt_html_ad81a188c46465fd7d044377393d362f3"></a>
<a id="astructhl78xx__evt_html_adfab3032ba9bf936a914e8ac02eed1ca"></a>
<a id="astructhl78xx__evt_html_aefc1d835f3244e680a33382c0f9d61fb"></a>
<a id="astructhl78xx__evt_html_af114567a2f292991f3c6de3a0b26a7ba"></a>
<a id="astructhl78xx__gnss__aux__data__callback_html"></a>
<a id="astructhl78xx__gnss__aux__data__callback_html_a2037bb2cfa4c6fb4d9e84489b8e48b8a"></a>
<a id="astructhl78xx__gnss__aux__data__callback_html_adcf42adad65b781ea9e5816c2f10b0db"></a>
<a id="astructhl78xx__gnss__nmea__aux__data_html"></a>
<a id="astructhl78xx__gnss__nmea__aux__data_html_a471784cde53ace4fda5ab532e428c6c8"></a>
<a id="astructhl78xx__gnss__nmea__aux__data_html_a529e929ce8878c329f0c370fd8155ce2"></a>
<a id="astructhl78xx__gnss__nmea__aux__data_html_a9d099e5d5baf20aa18dfd43e531aa202"></a>
<a id="astructhl78xx__network__info_html"></a>
<a id="astructhl78xx__network__info_html_a350369fc45a40a80fd563997042fed81"></a>
<a id="astructhl78xx__network__info_html_aa1e49eec0c60b7149ee943853983fc33"></a>
<a id="astructhl78xx__network__info_html_ab7f3c7f60d17167d8406dc977639128e"></a>
<a id="astructhl78xx__network__operator_html"></a>
<a id="astructhl78xx__network__operator_html_a1024bdecfbe35a84cb9cf6e9c65488ba"></a>
<a id="astructhl78xx__network__operator_html_a17dd8d113a540a311dc381f61a697012"></a>
<a id="astructhl78xx__network__operator_html_a775fa702eb42a7d520dff3d3a3a4b208"></a>
<a id="astructhl78xx__network__operator_html_a8118ab76929803d7f898a62bce1f4f18"></a>
<a id="astructhl78xx__network__operator_html_a9ca090484b881fa6343de3f8475982ed"></a>
<a id="astructhl78xx__network__operator_html_a9ce188616ea483281f6d600d69154cb3"></a>
<a id="astructhl78xx__network__operator_html_ab28ba8ce52648d02488efe2799d3337a"></a>
<a id="astructhl78xx__network_html"></a>
<a id="astructhl78xx__network_html_a0ef743013b5287ef8edd1c7414da2a81"></a>
<a id="astructhl78xx__network_html_a2c956f3333c56c34a197c5f3336030bb"></a>
<a id="astructhl78xx__network_html_adac6d7a38cd259a908d3e6f8b8ef9961"></a>
<a id="astructk__cellmeas__signal__info_html"></a>
<a id="astructk__cellmeas__signal__info_html_aedf20f274705729bd3c3b5246baec391"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructk__work_html"></a>
<a id="astructkselacq__syntax_html"></a>
<a id="astructkselacq__syntax_html_a0fe51e6bcae3f2195f62952a8022bda0"></a>
<a id="astructkselacq__syntax_html_a8c0973f97ef1cac8cf606e4420b2913b"></a>
<a id="astructkselacq__syntax_html_a96ce49c04407034f9f7b64bb28a1ab27"></a>
<a id="astructkselacq__syntax_html_ac62bc66e12deed5b1b7072f436d2cda8"></a>
<a id="astructmodem__chat__match_html"></a>
<a id="astructnmea__match__epu__data_html"></a>
<a id="astructnmea__match__epu__data_html_a00bc50a051125d483ecc0372939d3366"></a>
<a id="astructnmea__match__epu__data_html_a0b6709964409e68bfc1ec6053599c4d3"></a>
<a id="astructnmea__match__epu__data_html_a1545c6fbe045b9770b0701ba89b76353"></a>
<a id="astructnmea__match__epu__data_html_a1824d2be73ef8309c000e71fc28d685e"></a>
<a id="astructnmea__match__epu__data_html_a2bebe6e0c3b502cddb46ded81339c96d"></a>
<a id="astructnmea__match__epu__data_html_a342a008ff997d77e50be985807e09e39"></a>
<a id="astructnmea__match__epu__data_html_a4441cc16e1cb15ab6d631d6f2408ffd8"></a>
<a id="astructnmea__match__epu__data_html_a5fd2bd27efde367b4b8cee37a6f73cfe"></a>
<a id="astructnmea__match__epu__data_html_a854b002cd40b9803e8767136a9b100a5"></a>
<a id="astructnmea__match__epu__data_html_a869278cfd8e19efd76ab25c620d98972"></a>
<a id="astructnmea__match__epu__data_html_af001cd72af6d3f37d37b94e9c1c3f16b"></a>
<a id="astructnmea__match__gsa__data_html"></a>
<a id="astructnmea__match__gsa__data_html_a872c2e3cbcd0dcf5b0fff194f794622f"></a>
<a id="astructnmea__match__gsa__data_html_a9a785ec7d4c1ef2727e202927fd67440"></a>
<a id="astructnmea__match__gsa__data_html_aa4caab02bb1ab3a0c3014c4a3f993eae"></a>
<a id="astructnmea__match__gsa__data_html_aed176a2bc4f981221c69e1b08099df67"></a>
<a id="astructnmea__match__gst__data_html"></a>
<a id="astructnmea__match__gst__data_html_a4fdfb99f5c451ac7360613579a68416a"></a>
<a id="astructnmea__match__gst__data_html_a590ae7d7df7a4c78da267f0dc9f451f2"></a>
<a id="astructnmea__match__gst__data_html_a5bc62b0b55f62c0922fc00d13ff2f364"></a>
<a id="astructnmea__match__gst__data_html_a667027ebf56ecdd29be0321e982cb72f"></a>
<a id="astructnmea__match__gst__data_html_a7ba102be3748cdad0d9a44bd68d6c70f"></a>
<a id="astructnmea__match__gst__data_html_a8032be26aa57b4feb55dd119183b3d47"></a>
<a id="astructnmea__match__gst__data_html_a932c670f5a642ad7449806f69910328f"></a>
<a id="astructnmea__match__gst__data_html_aab1c6e9433619af20da9182d693ed692"></a>
<a id="astructnmea__match__gst__data_html_af7061a41e30e58c5cc58bebbd1663f9c"></a>
<a id="astructtm_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Netfeasa Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_HL78XX_APIS_H_
#define ZEPHYR_INCLUDE_DRIVERS_HL78XX_APIS_H_

#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <errno.h>
#include <stddef.h>
#include <stdint.h>
#include <time.h>
#include <zephyr/drivers/cellular.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

/* clang-format off */
#define CSQ_RSSI_UNKNOWN  (99)
#define CSQ_RSSI_MAX      (31)
#define CESQ_RSRP_UNKNOWN (255)
#define CESQ_RSRP_MAX     (97)
#define CESQ_RSRQ_UNKNOWN (255)
#define CESQ_RSRQ_MAX     (34)

#define HL78XX_MODEM_AT_ERROR     1
#define HL78XX_MODEM_AT_CME_ERROR 2
#define HL78XX_MODEM_AT_CMS_ERROR 3

#define CSQ_RSSI_TO_DB(v)  (-113 + (2 * (v)))
#define CESQ_RSRP_TO_DB(v) (-141 + (v))
#define CESQ_RSRQ_TO_DB(v) (((v) == 0U) ? -21 : (-20 + ((v) / 2)))

#define PAUSED 1
#define ACTIVE 0
#define MDM_MANUFACTURER_LENGTH        20
#define MDM_MODEL_LENGTH               32
#define MDM_REVISION_LENGTH            64
#define MDM_IMEI_LENGTH                16
#define MDM_IMSI_LENGTH                23
#define MDM_ICCID_LENGTH               22
#define MDM_APN_MAX_LENGTH             64
#define MDM_MAX_CERT_LENGTH            4096
#define MDM_MAX_HOSTNAME_LEN           128
#define MDM_SERIAL_NUMBER_LENGTH       32
#define HL78XX_CTZEU_UTIME_MAX_LEN     32
#define HL78XX_CEREG_TIMER_STR_LEN     9
#define HL78XX_NETWORK_ADDRESS_MAX_LEN 46
#define MDM_HL78XX_EOF_PATTERN         "--EOF--Pattern--"
#define MDM_HL78XX_TERMINATION_PATTERN "+++"
#define MDM_HL78XX_CONNECT_STRING      "CONNECT"
#define MDM_HL78XX_NO_CARRIER_STRING   "NO CARRIER"
#define MDM_HL78XX_CME_ERROR_STRING    "+CME ERROR: "
#define MDM_HL78XX_CMS_ERROR_STRING    "+CMS ERROR: "
#define MDM_HL78XX_ERROR_STRING        "ERROR"
#define MDM_HL78XX_OK_STRING           "OK"
#define MDM_HL78XX_DESIRED_VERSION_STRING                                                          \
        (sizeof(CONFIG_MODEM_HL78XX_DESIRED_FW_VERSION) > 1                                        \
                 ? CONFIG_MODEM_HL78XX_DESIRED_FW_VERSION                                          \
                 : "HL7812.5.7.4.0")

#define HL78XX_MONITOR_ACTIVE false

#define HL78XX_MONITOR_PAUSED true

#define HL78XX_MONITOR_INITIAL_PAUSED(...) \
        COND_CODE_1(IS_EMPTY(__VA_ARGS__), (false), (__VA_ARGS__))

/* clang-format on */

#define HL78XX_EVT_MONITOR(name, _handler, ...)                                                    \
        static STRUCT_SECTION_ITERABLE(hl78xx_evt_monitor_entry, name) = {                         \
                .handler = _handler,                                                               \
                .next = NULL,                                                                      \
                .flags = {                                                                         \
                        .direct = false,                                                           \
                        .paused = HL78XX_MONITOR_INITIAL_PAUSED(__VA_ARGS__),                      \
                }}

#define HL78XX_AT_MONITOR_ANY NULL

#define HL78XX_AT_MONITOR(name, _filter, _handler, ...)                                            \
        static STRUCT_SECTION_ITERABLE(hl78xx_at_monitor_entry, name) = {                          \
                .filter = _filter,                                                                 \
                .handler = _handler,                                                               \
                .next = NULL,                                                                      \
                .flags = {                                                                         \
                        .direct = false,                                                           \
                        .paused = HL78XX_MONITOR_INITIAL_PAUSED(__VA_ARGS__),                      \
                }}

#define HL78XX_AT_MONITOR_DIRECT(name, _filter, _handler, ...)                                     \
        static STRUCT_SECTION_ITERABLE(hl78xx_at_monitor_entry, name) = {                          \
                .filter = _filter,                                                                 \
                .handler = _handler,                                                               \
                .next = NULL,                                                                      \
                .flags = {                                                                         \
                        .direct = true,                                                            \
                        .paused = HL78XX_MONITOR_INITIAL_PAUSED(__VA_ARGS__),                      \
                }}

enum hl78xx_cell_rat_mode {
        HL78XX_RAT_CAT_M1 = 0,
        HL78XX_RAT_NB1,
        HL78XX_RAT_GSM,
        HL78XX_RAT_NBNTN,
        HL78XX_RAT_MODE_AUTO,
        HL78XX_RAT_MODE_NONE,
        HL78XX_RAT_COUNT = HL78XX_RAT_MODE_NONE
};

enum hl78xx_kselacq_rat {
        HL78XX_KSELACQ_RAT_CLEAR = 0,
        HL78XX_KSELACQ_RAT_CAT_M1 = 1,
        HL78XX_KSELACQ_RAT_NB1 = 2,
        HL78XX_KSELACQ_RAT_GSM = 3,
};

struct kselacq_syntax {
        bool mode;
        enum hl78xx_kselacq_rat rat1;
        enum hl78xx_kselacq_rat rat2;
        enum hl78xx_kselacq_rat rat3;
};

typedef bool (*hl78xx_runtime_band_provider_t)(const struct device *dev,
                                               enum hl78xx_cell_rat_mode rat, uint16_t *band,
                                               void *user_data);

enum hl78xx_phone_functionality {
        HL78XX_SIM_POWER_OFF,
        HL78XX_FULLY_FUNCTIONAL,
        HL78XX_AIRPLANE = 4,
};

enum hl78xx_sim_slot {
        HL78XX_SIM_SLOT_1 = 0,
        HL78XX_SIM_SLOT_2 = 1,
};

enum hl78xx_modem_restart_mode {
        HL78XX_MODEM_RESTART_HARD = 0,
        HL78XX_MODEM_RESTART_SOFT,
};

enum hl78xx_module_status {
        HL78XX_MODULE_READY = 0,
        HL78XX_MODULE_WAITING_FOR_ACCESS_CODE,
        HL78XX_MODULE_SIM_NOT_PRESENT,
        HL78XX_MODULE_SIMLOCK,
        HL78XX_MODULE_UNRECOVERABLE_ERROR,
        HL78XX_MODULE_UNKNOWN_STATE,
        HL78XX_MODULE_INACTIVE_SIM
};

enum hl78xx_modem_info_type {
        HL78XX_MODEM_INFO_SERIAL_NUMBER,
        HL78XX_MODEM_INFO_CURRENT_BAUD_RATE,
        HL78XX_MODEM_INFO_FW_VERSION
};

enum hl78xx_operator_format {
        HL78XX_OPERATOR_FORMAT_LONG_ALPHANUMERIC = 0,
        HL78XX_OPERATOR_FORMAT_SHORT_ALPHANUMERIC,
        HL78XX_OPERATOR_FORMAT_NUMERIC,
};

struct hl78xx_cxreg_status {
        enum cellular_registration_status reg_status;
        bool has_tac;
        uint32_t tac;
        bool has_cell_id;
        uint32_t cell_id;
        bool has_rat_mode;
        enum hl78xx_cell_rat_mode rat_mode;
        bool has_cause_type;
        int cause_type;
        bool has_reject_cause;
        int reject_cause;
        bool has_active_time;
        char active_time[HL78XX_CEREG_TIMER_STR_LEN];
        bool has_tau;
        char tau[HL78XX_CEREG_TIMER_STR_LEN];
};

enum hl78xx_network_info_type {
        HL78XX_NETWORK_INFO_APN,
        HL78XX_NETWORK_INFO_CURRENT_RAT,
        HL78XX_NETWORK_INFO_NETWORK_OPERATOR_LONG_ALPHA,
        HL78XX_NETWORK_INFO_NETWORK_OPERATOR_SHORT_ALPHA,
        HL78XX_NETWORK_INFO_NETWORK_OPERATOR_NUMERIC,
        HL78XX_NETWORK_INFO_OPERATOR_FORMAT,
        HL78XX_NETWORK_INFO_TAC,
        HL78XX_NETWORK_INFO_MCC,
        HL78XX_NETWORK_INFO_MNC,
        HL78XX_NETWORK_INFO_CELL_ID,
        HL78XX_NETWORK_INFO_IP_ADDRESS,
        HL78XX_NETWORK_INFO_DNS_PRIMARY,
        HL78XX_NETWORK_INFO_ACTIVE_BAND,
        HL78XX_NETWORK_INFO_SINR,
};

struct hl78xx_network_operator {
        bool has_operator;
        char operator_name[MDM_MODEL_LENGTH];
        bool has_mcc;
        uint16_t mcc;
        bool has_mnc;
        uint16_t mnc;
        enum hl78xx_operator_format format;
};

struct hl78xx_network_info {
        struct hl78xx_network_operator operator_info;
        char ip_address[HL78XX_NETWORK_ADDRESS_MAX_LEN];
        char dns_primary[HL78XX_NETWORK_ADDRESS_MAX_LEN];
};

enum nmea_output_port {
        NMEA_OUTPUT_NONE = 0x00,
        NMEA_OUTPUT_USB_NMEA_PORT = 0x01,
        NMEA_OUTPUT_UART1 = 0x03,
        NMEA_OUTPUT_SAME_PORT = 0x04,
        NMEA_OUTPUT_CMUX_DLC1 = 0x05,
        NMEA_OUTPUT_CMUX_DLC2 = 0x06,
        NMEA_OUTPUT_CMUX_DLC3 = 0x07,
        NMEA_OUTPUT_CMUX_DLC4 = 0x08
};

enum hl78xx_agnss_mode {
        HL78XX_AGNSS_MODE_INVALID = 0,
        HL78XX_AGNSS_MODE_VALID = 1,
};

enum hl78xx_agnss_days {
        HL78XX_AGNSS_DAYS_1 = 1,
        HL78XX_AGNSS_DAYS_2 = 2,
        HL78XX_AGNSS_DAYS_3 = 3,
        HL78XX_AGNSS_DAYS_7 = 7,
        HL78XX_AGNSS_DAYS_14 = 14,
        HL78XX_AGNSS_DAYS_28 = 28,
};

struct hl78xx_agnss_status {
        enum hl78xx_agnss_mode mode;
        uint8_t days;
        uint8_t hours;
        uint8_t minutes;
};

enum power_down_event {
        POWER_DOWN_EVENT_ENTER = 0,
        POWER_DOWN_EVENT_EXIT,
        POWER_DOWN_EVENT_NONE,
};

enum hl78xx_power_down_response {
        HL78XX_POWER_DOWN_RESPONSE_IMMEDIATE = 0,
        HL78XX_POWER_DOWN_RESPONSE_RESCHEDULE,
        HL78XX_POWER_DOWN_RESPONSE_ABORT,
};

enum hl78xx_edrx_event {
        HL78XX_EDRX_EVENT_IDLE_EXIT = 0,
        HL78XX_EDRX_EVENT_IDLE_ENTER,
        HL78XX_EDRX_EVENT_IDLE_NONE,
};

enum hl78xx_psmev_event {
        HL78XX_PSM_EVENT_EXIT = 0,
        HL78XX_PSM_EVENT_ENTER,
        HL78XX_PSM_EVENT_NONE,
};

struct k_cellmeas_signal_info {
        int16_t rsrp;
};

struct hl78xx_network {
        enum hl78xx_cell_rat_mode technology;
        uint16_t *bands;
        uint16_t size;
};

struct hl78xx_ctzeu_update {
        int tz;
        int dst;
        bool has_utime;
        int64_t date_time_ms;
        struct tm utc_time;
};

enum hl78xx_evt_type {
        HL78XX_LTE_RAT_UPDATE,
        HL78XX_LTE_REGISTRATION_STAT_UPDATE,
        HL78XX_LTE_SIM_REGISTRATION,
        HL78XX_LTE_MODEM_STARTUP,
        HL78XX_LTE_FOTA_UPDATE_STATUS,
        HL78XX_LTE_DNS_READY,
        HL78XX_LTE_AT_CMD_READY,
        HL78XX_LTE_PHONE_FUNCTIONALITY_UPDATE,
        HL78XX_LTE_CTZEU_UPDATE,
        HL78XX_GNSS_ENGINE_READY,
        HL78XX_GNSS_EVENT_INIT,
        HL78XX_GNSS_EVENT_START,
        HL78XX_GNSS_EVENT_STOP,
        HL78XX_GNSS_EVENT_POSITION,
        HL78XX_GNSS_EVENT_START_BLOCKED,
        HL78XX_GNSS_EVENT_SEARCH_TIMEOUT,
        HL78XX_GNSS_EVENT_MODE_EXITED,
        HL78XX_EDRX_IDLE_UPDATE,
        HL78XX_LTE_PSMEV_UPDATE,
        HL78XX_POWER_DOWN_UPDATE,
        HL78XX_VGPIO_LOW,
        HL78XX_VGPIO_HIGH,
        HL78XX_GPIO6_LOW,
        HL78XX_GPIO6_HIGH,
        HL78XX_CELLMEAS_UPDATE,
        HL78XX_EVT_TYPE_COUNT
};

enum wdsi_indication {
        WDSI_BOOTSTRAP_CREDENTIALS_PRESENT = 0,
        WDSI_USER_AGREEMENT_REQUEST = 1,
        WDSI_FIRMWARE_DOWNLOAD_REQUEST = 2,
        WDSI_FIRMWARE_INSTALL_REQUEST = 3,
        WDSI_AUTHENTICATION_START = 4,
        WDSI_AUTHENTICATION_FAILED = 5,
        WDSI_AUTHENTICATION_SUCCESS = 6,
        WDSI_CONNECTION_DENIED = 7,
        WDSI_DM_SESSION_CLOSED = 8,
        WDSI_FIRMWARE_AVAILABLE = 9,
        WDSI_FIRMWARE_DOWNLOADED = 10,
        WDSI_FIRMWARE_DOWNLOAD_ISSUE = 11,
        WDSI_PACKAGE_VERIFIED_CERTIFIED = 12,
        WDSI_PACKAGE_VERIFIED_NOT_CERTIFIED = 13,
        WDSI_FIRMWARE_UPDATE_START = 14,
        WDSI_FIRMWARE_UPDATE_FAILED = 15,
        WDSI_FIRMWARE_UPDATE_SUCCESS = 16,
        WDSI_DOWNLOAD_IN_PROGRESS = 18,
        WDSI_SESSION_STARTED = 23
};

enum hl78xx_gnss_event_type {
        HL78XX_GNSSEV_INITIALISATION = 0,
        HL78XX_GNSSEV_START = 1,
        HL78XX_GNSSEV_STOP = 2,
        HL78XX_GNSSEV_POSITION = 3
};

enum hl78xx_event_status {
        HL78XX_STATUS_FAILED = 0,
        HL78XX_STATUS_SUCCESS = 1
};

enum gnss_position_events {
        GNSS_FIX_LOST_OR_UNAVAILABLE = 0,
        GNSS_ESTIMATED_POSITION_AVAILABLE = 1,
        GNSS_2D_POSITION_AVAILABLE = 2,
        GNSS_3D_POSITION_AVAILABLE = 3,
        GNSS_FIX_CHANGED_TO_INVALID = 4
};

struct hl78xx_evt {
        enum hl78xx_evt_type type;

        union {
                enum cellular_registration_status reg_status;
                enum hl78xx_cell_rat_mode rat_mode;
#if defined(CONFIG_MODEM_HL78XX_AIRVANTAGE) || defined(__DOXYGEN__)
                enum wdsi_indication wdsi_indication;
#endif /* CONFIG_MODEM_HL78XX_AIRVANTAGE */
#if defined(CONFIG_HL78XX_GNSS) || defined(__DOXYGEN__)
                enum hl78xx_event_status event_status;
                enum gnss_position_events position_event;
#endif /* CONFIG_HL78XX_GNSS */
#if defined(CONFIG_MODEM_HL78XX_LOW_POWER_MODE) || defined(__DOXYGEN__)
#if defined(CONFIG_MODEM_HL78XX_PSM) || defined(__DOXYGEN__)
                enum hl78xx_psmev_event psm_event;
#endif /* CONFIG_MODEM_HL78XX_PSM */
#if defined(CONFIG_MODEM_HL78XX_EDRX) || defined(__DOXYGEN__)
                enum hl78xx_edrx_event edrx_event;
#endif /* CONFIG_MODEM_HL78XX_EDRX */
#if defined(CONFIG_MODEM_HL78XX_POWER_DOWN) || defined(__DOXYGEN__)
                enum power_down_event power_down_event;
#endif /* CONFIG_MODEM_HL78XX_POWER_DOWN */
#endif /* CONFIG_MODEM_HL78XX_LOW_POWER_MODE */
                struct k_cellmeas_signal_info cellmeas;
                struct hl78xx_ctzeu_update ctzeu;
                bool status;
                int value;
        } content;
};

struct nmea_match_gsa_data {
        int32_t fix_type;
        int64_t pdop;
        int64_t hdop;
        int64_t vdop;
};

struct nmea_match_gst_data {
        int32_t i32;
        uint32_t gst_utc;
        int64_t rms;
        int64_t sd_major;
        int64_t sd_minor;
        int64_t orient;
        int64_t lat_err;
        int64_t lon_err;
        int64_t alt_err;
};

struct nmea_match_epu_data {
        int64_t pos_3d;
        int64_t pos_2d;
        int64_t pos_lat;
        int64_t pos_lon;
        int64_t pos_alt;
        int64_t vel_3d;
        int64_t vel_2d;
        int64_t vel_hdg;
        int64_t vel_east;
        int64_t vel_north;
        int64_t vel_up;
};

struct hl78xx_gnss_nmea_aux_data {
        struct nmea_match_gsa_data gsa;
        struct nmea_match_gst_data gst;
        struct nmea_match_epu_data epu;
};

struct modem_chat_match;

typedef void (*hl78xx_gnss_aux_data_callback_t)(const struct device *dev,
                                                const struct hl78xx_gnss_nmea_aux_data *aux_data,
                                                uint16_t size);

struct hl78xx_gnss_aux_data_callback {
        const struct device *dev;
        hl78xx_gnss_aux_data_callback_t callback;
};

#define GNSS_AUX_DATA_CALLBACK_DEFINE(_dev, _callback)                                             \
        static const STRUCT_SECTION_ITERABLE(hl78xx_gnss_aux_data_callback,                        \
                                             _hl78xx_gnss_aux_data_callback__##_callback) = {      \
                .dev = _dev,                                                                       \
                .callback = _callback,                                                             \
        }

#define GNSS_DT_AUX_DATA_CALLBACK_DEFINE(_node_id, _callback)                                      \
        static const STRUCT_SECTION_ITERABLE(hl78xx_gnss_aux_data_callback,                        \
                                             _CONCAT_4(_hl78xx_gnss_aux_data_callback_,            \
                                                       DT_DEP_ORD(_node_id), _, _callback)) = {    \
                .dev = DEVICE_DT_GET(_node_id),                                                    \
                .callback = _callback,                                                             \
        }

typedef int (*hl78xx_api_configure_networks)(const struct device *dev,
                                             const struct hl78xx_network *networks, uint8_t size);

typedef int (*hl78xx_api_get_supported_networks)(const struct device *dev,
                                                 const struct hl78xx_network **networks,
                                                 uint8_t *size);

typedef int (*hl78xx_api_get_signal)(const struct device *dev, const enum cellular_signal_type type,
                                     int16_t *value);

typedef int (*hl78xx_api_get_modem_info)(const struct device *dev,
                                         const enum cellular_modem_info_type type, char *info,
                                         size_t size);

typedef int (*hl78xx_api_get_registration_status)(const struct device *dev,
                                                  enum cellular_access_technology tech,
                                                  enum cellular_registration_status *status);

typedef int (*hl78xx_api_set_phone_functionality)(const struct device *dev,
                                                  enum hl78xx_phone_functionality functionality,
                                                  bool reset);

typedef int (*hl78xx_api_get_phone_functionality)(const struct device *dev,
                                                  enum hl78xx_phone_functionality *functionality);

typedef int (*hl78xx_api_send_at_cmd)(const struct device *dev, const char *cmd, uint16_t cmd_size,
                                      const struct modem_chat_match *response_matches,
                                      uint16_t matches_size);

struct hl78xx_at_notification {
        const char *pattern;
        const char *const *argv;
        uint16_t argc;
};

struct hl78xx_at_monitor_entry;

typedef void (*hl78xx_at_monitor_handler_t)(const struct hl78xx_at_notification *notif,
                                            struct hl78xx_at_monitor_entry *mon);

typedef void (*hl78xx_at_monitor_release_t)(struct hl78xx_at_monitor_entry *mon);

struct hl78xx_at_monitor_entry {
        const char *filter;
        const hl78xx_at_monitor_handler_t handler;
        hl78xx_at_monitor_release_t release;
        struct hl78xx_at_monitor_entry *next;
        atomic_t refcnt;
        struct k_work release_work;
        struct {
                uint8_t paused: 1;
                uint8_t direct: 1;
        } flags;
};

struct hl78xx_evt_monitor_entry;

typedef void (*hl78xx_evt_monitor_dispatcher_t)(struct hl78xx_evt *notif);

typedef void (*hl78xx_evt_monitor_handler_t)(struct hl78xx_evt *notif,
                                             struct hl78xx_evt_monitor_entry *mon);

typedef void (*hl78xx_evt_monitor_release_t)(struct hl78xx_evt_monitor_entry *mon);

struct hl78xx_evt_monitor_entry {
        const hl78xx_evt_monitor_handler_t handler;
        hl78xx_evt_monitor_release_t release;
        struct hl78xx_evt_monitor_entry *next;
        atomic_t refcnt;
        struct k_work release_work;
        struct {
                uint8_t paused: 1;
                uint8_t direct: 1;
        } flags;
};

int hl78xx_api_func_set_phone_functionality(const struct device *dev,
                                            enum hl78xx_phone_functionality functionality,
                                            bool reset);

int hl78xx_api_func_restart(const struct device *dev, enum hl78xx_modem_restart_mode mode);

int hl78xx_api_func_get_phone_functionality(const struct device *dev,
                                            enum hl78xx_phone_functionality *functionality);

int hl78xx_api_func_get_signal(const struct device *dev, const enum cellular_signal_type type,
                               int16_t *value);

int hl78xx_api_func_get_modem_info(const struct device *dev, enum hl78xx_modem_info_type type,
                                   void *info, size_t size);

int hl78xx_api_func_get_modem_info_standard(const struct device *dev,
                                            enum cellular_modem_info_type type, char *info,
                                            size_t size);

int hl78xx_api_func_get_network_info(const struct device *dev, enum hl78xx_network_info_type type,
                                     void *info, size_t size);

int hl78xx_api_func_get_rsrp_validity(const struct device *dev, bool *is_valid);

int hl78xx_api_func_get_rsrq_validity(const struct device *dev, bool *is_valid);

int hl78xx_api_func_get_sinr_validity(const struct device *dev, bool *is_valid);

int hl78xx_api_func_set_network_operator_format(const struct device *dev,
                                                enum hl78xx_operator_format format);

int hl78xx_api_func_set_prl(const struct device *dev, const struct kselacq_syntax kselacq_rats);

int hl78xx_api_func_get_prl(const struct device *dev, struct kselacq_syntax *kselacq_rats);

int hl78xx_api_func_set_autorat_inhibit(const struct device *dev, bool inhibit);

bool hl78xx_api_func_at_is_busy(const struct device *dev);

int hl78xx_set_runtime_band_provider(const struct device *dev,
                                     hl78xx_runtime_band_provider_t provider, void *user_data);

int hl78xx_api_func_modem_dynamic_cmd_send(const struct device *dev, const char *cmd,
                                           uint16_t cmd_size,
                                           const struct modem_chat_match *response_matches,
                                           uint16_t matches_size);

int hl78xx_modem_at_send(const struct device *dev, const char *cmd);

int hl78xx_modem_at_cmd(const struct device *dev, char *response, size_t response_size,
                        const char *cmd);

static inline int hl78xx_get_modem_info(const struct device *dev,
                                        const enum hl78xx_modem_info_type type, void *info,
                                        size_t size)
{
        return hl78xx_api_func_get_modem_info(dev, type, info, size);
}

static inline int hl78xx_get_network_info(const struct device *dev,
                                          enum hl78xx_network_info_type type, void *info,
                                          size_t size)
{
        return hl78xx_api_func_get_network_info(dev, type, info, size);
}

static inline int hl78xx_get_rsrp_validity(const struct device *dev, bool *is_valid)
{
        return hl78xx_api_func_get_rsrp_validity(dev, is_valid);
}

static inline int hl78xx_get_rsrq_validity(const struct device *dev, bool *is_valid)
{
        return hl78xx_api_func_get_rsrq_validity(dev, is_valid);
}

static inline int hl78xx_get_sinr_validity(const struct device *dev, bool *is_valid)
{
        return hl78xx_api_func_get_sinr_validity(dev, is_valid);
}

static inline int hl78xx_set_prl(const struct device *dev, struct kselacq_syntax prl)
{
        return hl78xx_api_func_set_prl(dev, prl);
}

static inline int hl78xx_set_autorat_inhibit(const struct device *dev, bool inhibit)
{
        return hl78xx_api_func_set_autorat_inhibit(dev, inhibit);
}

static inline bool hl78xx_at_is_busy(const struct device *dev)
{
        return hl78xx_api_func_at_is_busy(dev);
}

static inline int hl78xx_set_phone_functionality(const struct device *dev,
                                                 enum hl78xx_phone_functionality functionality,
                                                 bool reset)
{
        return hl78xx_api_func_set_phone_functionality(dev, functionality, reset);
}

static inline int hl78xx_restart_modem(const struct device *dev,
                                       enum hl78xx_modem_restart_mode mode)
{
        return hl78xx_api_func_restart(dev, mode);
}

static inline int hl78xx_get_phone_functionality(const struct device *dev,
                                                 enum hl78xx_phone_functionality *functionality)
{
        return hl78xx_api_func_get_phone_functionality(dev, functionality);
}

static inline int hl78xx_modem_cmd_send(const struct device *dev, const char *cmd,
                                        uint16_t cmd_size,
                                        const struct modem_chat_match *response_matches,
                                        uint16_t matches_size)
{

        return hl78xx_api_func_modem_dynamic_cmd_send(dev, cmd, cmd_size, response_matches,
                                                      matches_size);
}

static inline int hl78xx_modem_at_err_type(int error)
{
        return (error & 0x00ff0000U) >> 16;
}

static inline int hl78xx_modem_at_err(int error)
{
        return (error & 0xff00ffffU);
}

static inline int hl78xx_parse_rssi(uint8_t rssi, int16_t *value)
{
        /* AT+CSQ returns a response +CSQ: <rssi>,<ber> where:
         * - rssi is a integer from 0 to 31 whose values describes a signal strength
         *   between -113 dBm for 0 and -51dbM for 31 or unknown for 99
         * - ber is an integer from 0 to 7 that describes the error rate, it can also
         *   be 99 for an unknown error rate
         */
        if ((rssi == CSQ_RSSI_UNKNOWN) || (rssi > CSQ_RSSI_MAX)) {
                return -EINVAL;
        }

        *value = (int16_t)CSQ_RSSI_TO_DB(rssi);
        return 0;
}

static inline int hl78xx_parse_rsrp(uint8_t rsrp, int16_t *value)
{
        /* AT+CESQ returns a response
         * +CESQ: <rxlev>,<ber>,<rscp>,<ecn0>,<rsrq>,<rsrp> where:
         * rsrq is a integer from 0 to 34 whose values describes the Reference
         * Signal Receive Quality between -20 dB for 0 and -3 dB for 34
         * (0.5 dB steps), or unknown for 255
         * rsrp is an integer from 0 to 97 that describes the Reference Signal
         * Receive Power between below -140 dBm for 0 and -44 dBm for 97
         * (1 dBm steps), or unknown for 255. Return a conservative lower-bound
         * integer so threshold comparisons do not treat code 0 as valid for a
         * -140 dBm minimum.
         */
        if ((rsrp == CESQ_RSRP_UNKNOWN) || (rsrp > CESQ_RSRP_MAX)) {
                return -EINVAL;
        }

        *value = (int16_t)CESQ_RSRP_TO_DB(rsrp);
        return 0;
}

static inline int hl78xx_parse_rsrq(uint8_t rsrq, int16_t *value)
{
        /* AT+CESQ encodes RSRQ in 0.5 dB steps. Return a conservative integer dB
         * representative so code 0 stays below a -20 dB threshold.
         */
        if ((rsrq == CESQ_RSRQ_UNKNOWN) || (rsrq > CESQ_RSRQ_MAX)) {
                return -EINVAL;
        }

        *value = (int16_t)CESQ_RSRQ_TO_DB(rsrq);
        return 0;
}

static inline void hl78xx_evt_monitor_pause(struct hl78xx_evt_monitor_entry *mon)
{
        mon->flags.paused = true;
}

static inline void hl78xx_evt_monitor_resume(struct hl78xx_evt_monitor_entry *mon)
{
        mon->flags.paused = false;
}

static inline void hl78xx_at_monitor_pause(struct hl78xx_at_monitor_entry *mon)
{
        mon->flags.paused = true;
}

static inline void hl78xx_at_monitor_resume(struct hl78xx_at_monitor_entry *mon)
{
        mon->flags.paused = false;
}

int hl78xx_at_monitor_register(struct hl78xx_at_monitor_entry *mon);

int hl78xx_at_monitor_unregister(struct hl78xx_at_monitor_entry *mon);

int hl78xx_evt_notif_handler_set(hl78xx_evt_monitor_dispatcher_t handler);

int hl78xx_evt_monitor_register(struct hl78xx_evt_monitor_entry *mon);

int hl78xx_evt_monitor_unregister(struct hl78xx_evt_monitor_entry *mon);

enum cellular_access_technology hl78xx_rat_to_access_tech(enum hl78xx_cell_rat_mode rat_mode);

enum hl78xx_cell_rat_mode hl78xx_access_tech_to_rat(enum cellular_access_technology access_tech);

int hl78xx_start_airvantage_dm_session(const struct device *dev);

int hl78xx_stop_airvantage_dm_session(const struct device *dev);

int hl78xx_set_wake_pin_low(const struct device *dev);

int hl78xx_set_wake_pin_high(const struct device *dev);

int hl78xx_set_active_sim(const struct device *dev, enum hl78xx_sim_slot sim_slot);

int hl78xx_wakeup_modem(const struct device *dev);

int hl78xx_edrx_get_time_to_sleep(const struct device *dev);

int hl78xx_enter_gnss_mode(const struct device *dev);

int hl78xx_exit_gnss_mode(const struct device *dev);

int hl78xx_queue_gnss_search(const struct device *dev);

int hl78xx_gnss_set_nmea_output(const struct device *dev, enum nmea_output_port port);

int hl78xx_gnss_set_search_timeout(const struct device *dev, uint32_t timeout_ms);

int hl78xx_gnss_get_search_timeout_remaining(const struct device *dev, uint32_t *timeout_ms);

int hl78xx_gnss_get_latest_known_fix(const struct device *dev);

int hl78xx_gnss_assist_data_get_status(const struct device *dev,
                                       struct hl78xx_agnss_status *status);

int hl78xx_gnss_assist_data_download(const struct device *dev, enum hl78xx_agnss_days days);

int hl78xx_gnss_assist_data_delete(const struct device *dev);

int hl78xx_power_down_trigger(const struct device *dev, k_timeout_t delay);

int hl78xx_power_down_cancel(const struct device *dev);

int hl78xx_power_down_respond(const struct device *dev, enum hl78xx_power_down_response response,
                              uint32_t timeout_s);

void hl78xx_power_down_confirm(const struct device *dev);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_HL78XX_APIS_H_ */
```

## 30.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Netfeasa Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 36 行

关闭 clang-format 自动排版（clang-format off）。

### 注释 3：原第 155 行

开启 clang-format 自动排版（clang-format on）。

### 注释 4：原第 872 行

条件编译配置（Configuration）标记：`CONFIG_MODEM_HL78XX_AIRVANTAGE`。

### 注释 5：原第 878 行

条件编译配置（Configuration）标记：`CONFIG_HL78XX_GNSS`。

### 注释 6：原第 883 行

条件编译配置（Configuration）标记：`CONFIG_MODEM_HL78XX_PSM`。

### 注释 7：原第 887 行

条件编译配置（Configuration）标记：`CONFIG_MODEM_HL78XX_EDRX`。

### 注释 8：原第 891 行

条件编译配置（Configuration）标记：`CONFIG_MODEM_HL78XX_POWER_DOWN`。

### 注释 9：原第 892 行

条件编译配置（Configuration）标记：`CONFIG_MODEM_HL78XX_LOW_POWER_MODE`。

### 注释 10：原第 1792 行

`AT+CSQ` 返回响应 `+CSQ: <rssi>,<ber>`，其中：

- `rssi` 是 0–31 的整数，表示信号强度，0 对应 -113 dBm，31 对应 -51 dBm；99 表示未知。
- `ber` 是 0–7 的整数，表示误码率（Bit error rate）；也可为 99，表示未知误码率。

### 注释 11：原第 1821 行

`AT+CESQ` 返回响应 `+CESQ: <rxlev>,<ber>,<rscp>,<ecn0>,<rsrq>,<rsrp>`，其中：

- `rsrq` 是 0–34 的整数，表示参考信号接收质量（Reference Signal Receive Quality）：0 对应 -20 dB，34 对应 -3 dB，步长为 0.5 dB；255 表示未知。
- `rsrp` 是 0–97 的整数，表示参考信号接收功率（Reference Signal Receive Power）：0 对应低于 -140 dBm，97 对应 -44 dBm，步长为 1 dBm；255 表示未知。返回保守的下界整数，使阈值比较不会将代码 0 视为满足 -140 dBm 最低要求的有效值。

### 注释 12：原第 1855 行

`AT+CESQ` 以 0.5 dB 步长编码 RSRQ。返回一个保守的整数 dB 代表值，使代码 0 仍低于 -20 dB 阈值。

### 注释 13：原第 2364 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_HL78XX_APIS_H_`。

## 30.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/drivers/cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)
- [HL78XX_RAT_CAT_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182aea5264d590f823740963f57f8a2da91b)
- [HL78XX_RAT_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182abc0346af5e00e8f506effb9a6fc0694e)
- [HL78XX_RAT_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182aab03d62c74493d0979c1a94c92d87f8d)
- [HL78XX_RAT_NBNTN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182a78b9fd47dd95d556af0924c2070e446d)
- [HL78XX_RAT_MODE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182af80d7346afa3c9211e9280b5eede507b)
- [HL78XX_RAT_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182a7c8d747fe24f8297d84e15955d936b5f)
- [HL78XX_RAT_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga298f953be96ab47be40b5440a2573182aabc6a4c8e676510fe5f10a9acca1d422)
- [hl78xx_kselacq_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf2ab6a096dff081e7cbbba13b06de3cc)
- [HL78XX_KSELACQ_RAT_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3ccafd6bdf61c89c8ca8a24ae7095107a850)
- [HL78XX_KSELACQ_RAT_CAT_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3cca61375a298461738b794a8788618cc72f)
- [HL78XX_KSELACQ_RAT_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3cca90e58676ada0b8eb4edbda7c8a5f88ca)
- [HL78XX_KSELACQ_RAT_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaf2ab6a096dff081e7cbbba13b06de3cca9ce65ccd085dc64dc47dcde5880edf30)
- [kselacq_syntax](../system_service_model_reference/P059_kselacq_syntax_结构体.md)
- [mode](../system_service_model_reference/P059_kselacq_syntax_结构体.md#a96ce49c04407034f9f7b64bb28a1ab27)
- [rat1](../system_service_model_reference/P059_kselacq_syntax_结构体.md#ac62bc66e12deed5b1b7072f436d2cda8)
- [rat2](../system_service_model_reference/P059_kselacq_syntax_结构体.md#a0fe51e6bcae3f2195f62952a8022bda0)
- [rat3](../system_service_model_reference/P059_kselacq_syntax_结构体.md#a8c0973f97ef1cac8cf606e4420b2913b)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [hl78xx_runtime_band_provider_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga82793d1f4c0c8f03ae27b29afa1c3d3f)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [hl78xx_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga39a3de13bd706571cd7348ea46b7b708)
- [HL78XX_SIM_POWER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga39a3de13bd706571cd7348ea46b7b708a4c54c1a19aa628006b2ee6fb784678cf)
- [HL78XX_FULLY_FUNCTIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga39a3de13bd706571cd7348ea46b7b708a9abfd8982d4ea25916070a82159e6cba)
- [HL78XX_AIRPLANE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga39a3de13bd706571cd7348ea46b7b708a727707489a7b4c16d6d0349c0444b570)
- [hl78xx_sim_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0b3efb75d166d9d4bf163ffc6bb68fc0)
- [HL78XX_SIM_SLOT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga0b3efb75d166d9d4bf163ffc6bb68fc0a8a18fd1d142338fa139a926831ed4576)
- [HL78XX_SIM_SLOT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga0b3efb75d166d9d4bf163ffc6bb68fc0a0bd84025a4ab914d51e39f1a74dc7794)
- [hl78xx_modem_restart_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga618c248d23a1db1b027333c92adf99a1)
- [HL78XX_MODEM_RESTART_HARD](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga618c248d23a1db1b027333c92adf99a1a002353fb154ae25fcd8be8a7aea959fc)
- [HL78XX_MODEM_RESTART_SOFT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga618c248d23a1db1b027333c92adf99a1af3eaf31074c112910f9bbf2a255a99c8)
- [hl78xx_module_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab4a85c57d2f77c04a887f6552abff48a)
- [HL78XX_MODULE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa10412ece169f6a904dfe27e0f5bd40db)
- [HL78XX_MODULE_WAITING_FOR_ACCESS_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aab925138725807800ac98b509e1340820)
- [HL78XX_MODULE_SIM_NOT_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa05d1dd567db7374cd3d014bc09f520f9)
- [HL78XX_MODULE_SIMLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aafce279daf75ac9295638671573a7983f)
- [HL78XX_MODULE_UNRECOVERABLE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa10eb8b82197b435825210acc3a82d294)
- [HL78XX_MODULE_UNKNOWN_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aaeac806332373d0add288ca9eabc9aee6)
- [HL78XX_MODULE_INACTIVE_SIM](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggab4a85c57d2f77c04a887f6552abff48aa256929b0f7607ed5cff628c6f4341cf3)
- [hl78xx_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaadcca229cbccc9832734bcc4e2a443e6)
- [HL78XX_MODEM_INFO_SERIAL_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaadcca229cbccc9832734bcc4e2a443e6a833446e30f39a5774ec64960d034d7f8)
- [HL78XX_MODEM_INFO_CURRENT_BAUD_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaadcca229cbccc9832734bcc4e2a443e6a2a33182a8e9f3af2f855911d3efb86cd)
- [HL78XX_MODEM_INFO_FW_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggaadcca229cbccc9832734bcc4e2a443e6ae51b7e16678087c053836e9e1e292aca)
- [hl78xx_operator_format](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2d26ae6044baac5995f4184abe4faad3)
- [HL78XX_OPERATOR_FORMAT_LONG_ALPHANUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2d26ae6044baac5995f4184abe4faad3a96b0936754b3effa667deb39fabf6d4c)
- [HL78XX_OPERATOR_FORMAT_SHORT_ALPHANUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2d26ae6044baac5995f4184abe4faad3a7f3d8e1bf25092ed400496af83401164)
- [HL78XX_OPERATOR_FORMAT_NUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2d26ae6044baac5995f4184abe4faad3a9dbc87f548dc297b1394c8c287a841b9)
- [hl78xx_cxreg_status](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md)
- [cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)
- [reg_status](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a4b5acff39666484d3aa7f4920a33c195)
- [has_tac](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a8674887283917c025827e2d24e07aa21)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [tac](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#ae28a6c477536c15740ec07615b156d37)
- [has_cell_id](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a60f715d0323fa365590d6e6eb8f276fa)
- [cell_id](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a6c744edb85c63395147b1b55da6dcc9d)
- [has_rat_mode](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#aa5277387244ff33df4622bcd966138d2)
- [rat_mode](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#ac5661b4086fb1be97cb562ac0080303c)
- [has_cause_type](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#ab93a65b47faea7a583313bd74ea2be24)
- [cause_type](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#aa79861dc75aa6db380d719bd291d6297)
- [has_reject_cause](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#ac35cd02f962b64890911b0792d7310e0)
- [reject_cause](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#afc07b878db1a4ebd74c1b642c5222866)
- [has_active_time](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a1b1616b638324a1073a81e2c51d7082a)
- [active_time](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#aaec559842aa44a208c800c1056dc1960)
- [HL78XX_CEREG_TIMER_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0d3e4dcb509b56886297f2f451f4d952)
- [has_tau](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#aeb8daf30feb1b4c82888f5ce393b2adf)
- [tau](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a90f9a217168113e3b223e6fee7d3a484)
- [hl78xx_network_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga563d651fff3621c1e21d7c47d19fd218)
- [HL78XX_NETWORK_INFO_APN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a78924a7342c9ba71264d2cb29379cebe)
- [HL78XX_NETWORK_INFO_CURRENT_RAT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218ae589e3849313befefdee8a469a8754f6)
- [HL78XX_NETWORK_INFO_NETWORK_OPERATOR_LONG_ALPHA](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218ac98b93ea01bf22bd8d9e6bc8b5fb5da4)
- [HL78XX_NETWORK_INFO_NETWORK_OPERATOR_SHORT_ALPHA](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a89dfb37411db5f120730745a9b8ff34c)
- [HL78XX_NETWORK_INFO_NETWORK_OPERATOR_NUMERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218ad5e1d9aea137483f37e7312d7581818a)
- [HL78XX_NETWORK_INFO_OPERATOR_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a7f2a1a1848dcd438e62db93ef54be520)
- [HL78XX_NETWORK_INFO_TAC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a1c82ba0582491b289046298ae2f61b5f)
- [HL78XX_NETWORK_INFO_MCC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a286208af6eb57a95635704a6658d653c)
- [HL78XX_NETWORK_INFO_MNC](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a9167f4df382bca60ae4b97c1f12f59cb)
- [HL78XX_NETWORK_INFO_CELL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a17d48aff76cf0944dd083add04d84650)
- [HL78XX_NETWORK_INFO_IP_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a29ba014d1f42f7492a37d1cd4291d771)
- [HL78XX_NETWORK_INFO_DNS_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a426d3785c73439e6b07cdd97ac564d73)
- [HL78XX_NETWORK_INFO_ACTIVE_BAND](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a877dbafbeb15642bda562893e80dd3fc)
- [HL78XX_NETWORK_INFO_SINR](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga563d651fff3621c1e21d7c47d19fd218a6914647a87d666f23268476b9ed6fa48)
- [hl78xx_network_operator](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md)
- [has_operator](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a775fa702eb42a7d520dff3d3a3a4b208)
- [operator_name](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#ab28ba8ce52648d02488efe2799d3337a)
- [MDM_MODEL_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga694436b7ecedfd934f78afa9f404cadb)
- [has_mcc](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a1024bdecfbe35a84cb9cf6e9c65488ba)
- [mcc](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a9ce188616ea483281f6d600d69154cb3)
- [has_mnc](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a17dd8d113a540a311dc381f61a697012)
- [mnc](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a8118ab76929803d7f898a62bce1f4f18)
- [format](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a9ca090484b881fa6343de3f8475982ed)
- [hl78xx_network_info](../modem_wireless_model_reference/P026_hl78xx_network_info_结构体.md)
- [operator_info](../modem_wireless_model_reference/P026_hl78xx_network_info_结构体.md#aa1e49eec0c60b7149ee943853983fc33)
- [ip_address](../modem_wireless_model_reference/P026_hl78xx_network_info_结构体.md#a350369fc45a40a80fd563997042fed81)
- [HL78XX_NETWORK_ADDRESS_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga1dd356d88b67261a642ba50730b31b48)
- [dns_primary](../modem_wireless_model_reference/P026_hl78xx_network_info_结构体.md#ab7f3c7f60d17167d8406dc977639128e)
- [nmea_output_port](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabb0e5a4dd5c2e29d62ba27f6022f01f5)
- [NMEA_OUTPUT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a70a8a01cbbc9b852868f3ac89de2ddf9)
- [NMEA_OUTPUT_USB_NMEA_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5af082d7aaf20780a7d92b34a2ac4a0c5c)
- [NMEA_OUTPUT_UART1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a77298645730698245d50ffd96ceb9589)
- [NMEA_OUTPUT_SAME_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a6b3402a65141facc4a321d128279ebd3)
- [NMEA_OUTPUT_CMUX_DLC1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5ad00f384fd5b1219ec6c6a20f5bce96bf)
- [NMEA_OUTPUT_CMUX_DLC2](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a2a896155562e45fbf018196122a2172f)
- [NMEA_OUTPUT_CMUX_DLC3](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5af39367ee7f46f704f35a04064b34c70d)
- [NMEA_OUTPUT_CMUX_DLC4](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggabb0e5a4dd5c2e29d62ba27f6022f01f5a545f725ef187285b754c8ffd1a7cafa1)
- [hl78xx_agnss_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7d4975dffccffac27c9dccb85c02d549)
- [HL78XX_AGNSS_MODE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga7d4975dffccffac27c9dccb85c02d549aa553e73835a42bf35fe48e9632343288)
- [HL78XX_AGNSS_MODE_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga7d4975dffccffac27c9dccb85c02d549afb0c667dcd64c3bb41b73e06d286f16d)
- [hl78xx_agnss_days](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae9cf9c13242bc674dd7b0b79a69b8f31)
- [HL78XX_AGNSS_DAYS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31a14ac3c208659e6be45c0502d30b8b876)
- [HL78XX_AGNSS_DAYS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31acaef50b4e3d06dfdc3c703dae8d82e34)
- [HL78XX_AGNSS_DAYS_3](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31a4bb4b3122461421478ca130f26e3b3d8)
- [HL78XX_AGNSS_DAYS_7](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31a8a74f2b00cd4c4e46e64132cc196f06a)
- [HL78XX_AGNSS_DAYS_14](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31aafcbffebe034104de9ac4d75a78af816)
- [HL78XX_AGNSS_DAYS_28](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae9cf9c13242bc674dd7b0b79a69b8f31abba715db73ee7a99fffab7777be47459)
- [hl78xx_agnss_status](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md)
- [mode](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md#aead701aedc1734a4f89bd628030b0850)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [days](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md#a5c3fa9011d3d5e71d5aaacc0ecfe7e95)
- [hours](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md#a5e7e0613597dad81c06ca0b7b48a0aba)
- [minutes](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md#aa17d6323d9faeb81b1d3299898166a0b)
- [power_down_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6340324dcb76101c66b902bb9a14dbd3)
- [POWER_DOWN_EVENT_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga6340324dcb76101c66b902bb9a14dbd3ad9cb3a49a3624deab7bfd971c2c2b7aa)
- [POWER_DOWN_EVENT_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga6340324dcb76101c66b902bb9a14dbd3aca289a9bee6ebfa5e8b67fb221a8d5c1)
- [POWER_DOWN_EVENT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga6340324dcb76101c66b902bb9a14dbd3a851e1360c22aae25876472dce866e93b)
- [hl78xx_power_down_response](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga50bd06a27371c5c79de5bef125d6b5f3)
- [HL78XX_POWER_DOWN_RESPONSE_IMMEDIATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga50bd06a27371c5c79de5bef125d6b5f3ae77730c9d1ad65be888ef47b160b114a)
- [HL78XX_POWER_DOWN_RESPONSE_RESCHEDULE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga50bd06a27371c5c79de5bef125d6b5f3adeb8cba23aae92a082bebac7d3417985)
- [HL78XX_POWER_DOWN_RESPONSE_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga50bd06a27371c5c79de5bef125d6b5f3ad1b7771088c528180c76181808e03a5e)
- [hl78xx_edrx_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5d8a5b00f354e98abc2effa560f3bac8)
- [HL78XX_EDRX_EVENT_IDLE_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5d8a5b00f354e98abc2effa560f3bac8a300a530cffa64e515acc0791cc2e6db8)
- [HL78XX_EDRX_EVENT_IDLE_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5d8a5b00f354e98abc2effa560f3bac8a66047ead9b0c480d98552c448a83b5c5)
- [HL78XX_EDRX_EVENT_IDLE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5d8a5b00f354e98abc2effa560f3bac8aafe6e1f8916befffd919fbb2c6de268a)
- [hl78xx_psmev_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae891e3155a0ebf72433dd58ae4c36512)
- [HL78XX_PSM_EVENT_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae891e3155a0ebf72433dd58ae4c36512a4e37f5ae41b41f0ab34cdad64a406a94)
- [HL78XX_PSM_EVENT_ENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae891e3155a0ebf72433dd58ae4c36512abc6511482660d1cbc9028c7a9c416dda)
- [HL78XX_PSM_EVENT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ggae891e3155a0ebf72433dd58ae4c36512afffc6763941b03be63aa4a96b6442553)
- [k_cellmeas_signal_info](../system_service_model_reference/P058_k_cellmeas_signal_info_结构体.md)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [rsrp](../system_service_model_reference/P058_k_cellmeas_signal_info_结构体.md#aedf20f274705729bd3c3b5246baec391)
- [hl78xx_network](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md)
- [technology](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md#a0ef743013b5287ef8edd1c7414da2a81)
- [bands](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md#a2c956f3333c56c34a197c5f3336030bb)
- [size](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md#adac6d7a38cd259a908d3e6f8b8ef9961)
- [hl78xx_ctzeu_update](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md)
- [tz](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md#a5e0f09445a9abda3c5f0b37b97473815)
- [dst](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md#ae5eba83a8def3c9720797fd2f1ff46d0)
- [has_utime](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md#a9f0db53ae132db9a43e6a00b93807145)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [date_time_ms](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md#a0c90dddc2087e97afd6da421a7862323)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [utc_time](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md#a3b4a66b56a5632a7dc7a4964f949f7b1)
- [hl78xx_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8a864475f6e9673f85ec7c56028992a5)
- [HL78XX_LTE_RAT_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a21d1935e59ebf795d89d5a82165af2a5)
- [HL78XX_LTE_REGISTRATION_STAT_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a0cee4285190ea2c146f12860d06d9a95)
- [HL78XX_LTE_SIM_REGISTRATION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a72df7d50699f4f96d02325f542f614b9)
- [HL78XX_LTE_MODEM_STARTUP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a63c67068793c9fabf8b67c8789a4a839)
- [HL78XX_LTE_FOTA_UPDATE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a4aac4ed8583b9a578df0520b2c60bc92)
- [HL78XX_LTE_DNS_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a825fbf232cbc47a437f9d4e8783485a8)
- [HL78XX_LTE_AT_CMD_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a28cdd117df9b2826b1068c6618a8fc73)
- [HL78XX_LTE_PHONE_FUNCTIONALITY_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ac45e32555ac3905a997b6a198b8de7e5)
- [HL78XX_LTE_CTZEU_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ada32d74ea1b57da33c35cd7df917b9d6)
- [HL78XX_GNSS_ENGINE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a57bb01f9d4adbe81580e3d9ced2c904b)
- [HL78XX_GNSS_EVENT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a03122d21581271713faf37256588f8ae)
- [HL78XX_GNSS_EVENT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a5453982090bb38fe747dac48a52dacb5)
- [HL78XX_GNSS_EVENT_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ade12f00ad30395eb347351368c36ba61)
- [HL78XX_GNSS_EVENT_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5aef6a7387e9e4529a150177da1eae3e4c)
- [HL78XX_GNSS_EVENT_START_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a3068a58b1b38ee45d773a98970e13b07)
- [HL78XX_GNSS_EVENT_SEARCH_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5acd94ee0ae192d395930d750990970429)
- [HL78XX_GNSS_EVENT_MODE_EXITED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5ac87cc0d645f9902639957a963bd3b916)
- [HL78XX_EDRX_IDLE_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a4f0a0834200a910bc1a18a3249bb5cb3)
- [HL78XX_LTE_PSMEV_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a0c5a07183e824fe03b89e64758ca7bb7)
- [HL78XX_POWER_DOWN_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5afb198b40593360402b9b207fd7f633a2)
- [HL78XX_VGPIO_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a66e68cb9d725de54d218d569e95734fc)
- [HL78XX_VGPIO_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a59235d90a373eeb25f6d0e832f2e1e63)
- [HL78XX_GPIO6_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5acfdaea2981c12857c3b798a94dfb56fe)
- [HL78XX_GPIO6_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a1b387e9b0671d132fd67bdbd66855f52)
- [HL78XX_CELLMEAS_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a9190aa3603a2f9393aaa9973e5924254)
- [HL78XX_EVT_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga8a864475f6e9673f85ec7c56028992a5a3d815405a16ae0ed27853462ec7e3790)
- [wdsi_indication](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5453000edbd52c54f7193de4852aa9a8)
- [WDSI_BOOTSTRAP_CREDENTIALS_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a61ffcb6d724c54639b580f3ef1416339)
- [WDSI_USER_AGREEMENT_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a6056a26520c397f481233b759e20dbf2)
- [WDSI_FIRMWARE_DOWNLOAD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8aa3788211847f2604336a77c9ac63ee68)
- [WDSI_FIRMWARE_INSTALL_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a19574b7c2279ac2111df8e6d3186eea5)
- [WDSI_AUTHENTICATION_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a2af43270aca8930bd5aae44310e20ed1)
- [WDSI_AUTHENTICATION_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a972aa73ba08dd231d784798bd50652f6)
- [WDSI_AUTHENTICATION_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a72a0e1beddb3fe3b261e10fac9d7b608)
- [WDSI_CONNECTION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8aec2dc59ad43eab4575e32f9ba5aa874a)
- [WDSI_DM_SESSION_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a51d8ee5b26b38415c00552ecab2714c2)
- [WDSI_FIRMWARE_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8ad4765a0d1b65fdfdbab81ad7510d91f8)
- [WDSI_FIRMWARE_DOWNLOADED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8ab183f795c85e3909e256e8d09c105fbd)
- [WDSI_FIRMWARE_DOWNLOAD_ISSUE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a170bcb630bb629befdbfa836d6a00184)
- [WDSI_PACKAGE_VERIFIED_CERTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8ad08eb04d48c458947c509ef780288fe7)
- [WDSI_PACKAGE_VERIFIED_NOT_CERTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a6e6c598f1193635add06421bf6072fc5)
- [WDSI_FIRMWARE_UPDATE_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a8c3fa8220a8971da702a89cb79789458)
- [WDSI_FIRMWARE_UPDATE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a29d93a08da20d42c8178106f6367edbc)
- [WDSI_FIRMWARE_UPDATE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a40fd91ef5c30f68f5b6c2c966b06164f)
- [WDSI_DOWNLOAD_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a5cf687bbb0be75db70158ef8724237c0)
- [WDSI_SESSION_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga5453000edbd52c54f7193de4852aa9a8a9c10f1f3de92bc942fa1734b0263887d)
- [hl78xx_gnss_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga95d1ccc5899adf1b2eda6aa0777b7e80)
- [HL78XX_GNSSEV_INITIALISATION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80aed8b14739dd868eb2eef60c344814c21)
- [HL78XX_GNSSEV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80a804ea78a9bdd6f7ddc431e7110bdb740)
- [HL78XX_GNSSEV_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80a366a2b67d8d3f26e32b420bb3b93e8da)
- [HL78XX_GNSSEV_POSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga95d1ccc5899adf1b2eda6aa0777b7e80a2870c278c34bf045a74044f7f9b06533)
- [hl78xx_event_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9b9da1841754d723cddc103800b141ae)
- [HL78XX_STATUS_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga9b9da1841754d723cddc103800b141aead514153518fec842a1b6cc921732d00e)
- [HL78XX_STATUS_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga9b9da1841754d723cddc103800b141aea297ff80ceab088eaa0d9bcc1e15513cd)
- [gnss_position_events](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2a471bc1b92dba1e316b2b27e3778e1a)
- [GNSS_FIX_LOST_OR_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa6c26e21bea35d8b23dd4002efb4a2d7d)
- [GNSS_ESTIMATED_POSITION_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa6182b271f30b1823a5b78e7a8b2e5306)
- [GNSS_2D_POSITION_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa3f501dc908e8d5d0ee0019cb9f8560e8)
- [GNSS_3D_POSITION_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aaa444e753e453772c2ef68b49c3287407)
- [GNSS_FIX_CHANGED_TO_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gga2a471bc1b92dba1e316b2b27e3778e1aa81de01932f8017e5c3cf866dbef309fa)
- [hl78xx_evt](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md)
- [type](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#a0943763d4df0904b6fd6299f405dc0b4)
- [reg_status](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#af114567a2f292991f3c6de3a0b26a7ba)
- [rat_mode](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#adfab3032ba9bf936a914e8ac02eed1ca)
- [wdsi_indication](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#aefc1d835f3244e680a33382c0f9d61fb)
- [event_status](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#accf5c9a1709eb7181aab995267757584)
- [position_event](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#ace5b13c268479f1e8a143e1673c4ea73)
- [psm_event](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#aabfc3cb2d27cb2a1d7a473af9a6ad621)
- [edrx_event](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#a8b207883087d39a428f02f1cc4997043)
- [power_down_event](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#a83a493750d68fca89be51eddd700dae1)
- [cellmeas](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#abf9091f1c192664a55b7a8a50e21ee44)
- [ctzeu](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#ac919edeb1b552ce726527b20580303de)
- [status](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#a3dbdb39cc7be1dd57a965f7d4a86aebc)
- [value](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#ad81a188c46465fd7d044377393d362f3)
- [content](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#aa142ce76ffc686074b6955437633feea)
- [nmea_match_gsa_data](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [fix_type](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md#aed176a2bc4f981221c69e1b08099df67)
- [pdop](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md#aa4caab02bb1ab3a0c3014c4a3f993eae)
- [hdop](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md#a9a785ec7d4c1ef2727e202927fd67440)
- [vdop](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md#a872c2e3cbcd0dcf5b0fff194f794622f)
- [nmea_match_gst_data](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md)
- [i32](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#af7061a41e30e58c5cc58bebbd1663f9c)
- [gst_utc](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a932c670f5a642ad7449806f69910328f)
- [rms](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a7ba102be3748cdad0d9a44bd68d6c70f)
- [sd_major](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a5bc62b0b55f62c0922fc00d13ff2f364)
- [sd_minor](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#aab1c6e9433619af20da9182d693ed692)
- [orient](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a8032be26aa57b4feb55dd119183b3d47)
- [lat_err](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a4fdfb99f5c451ac7360613579a68416a)
- [lon_err](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a667027ebf56ecdd29be0321e982cb72f)
- [alt_err](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a590ae7d7df7a4c78da267f0dc9f451f2)
- [nmea_match_epu_data](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md)
- [pos_3d](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a869278cfd8e19efd76ab25c620d98972)
- [pos_2d](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a1824d2be73ef8309c000e71fc28d685e)
- [pos_lat](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#af001cd72af6d3f37d37b94e9c1c3f16b)
- [pos_lon](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a4441cc16e1cb15ab6d631d6f2408ffd8)
- [pos_alt](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a1545c6fbe045b9770b0701ba89b76353)
- [vel_3d](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a854b002cd40b9803e8767136a9b100a5)
- [vel_2d](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a2bebe6e0c3b502cddb46ded81339c96d)
- [vel_hdg](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a0b6709964409e68bfc1ec6053599c4d3)
- [vel_east](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a00bc50a051125d483ecc0372939d3366)
- [vel_north](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a342a008ff997d77e50be985807e09e39)
- [vel_up](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a5fd2bd27efde367b4b8cee37a6f73cfe)
- [hl78xx_gnss_nmea_aux_data](../modem_wireless_model_reference/P024_hl78xx_gnss_nmea_aux_data_结构体.md)
- [gsa](../modem_wireless_model_reference/P024_hl78xx_gnss_nmea_aux_data_结构体.md#a529e929ce8878c329f0c370fd8155ce2)
- [gst](../modem_wireless_model_reference/P024_hl78xx_gnss_nmea_aux_data_结构体.md#a9d099e5d5baf20aa18dfd43e531aa202)
- [epu](../modem_wireless_model_reference/P024_hl78xx_gnss_nmea_aux_data_结构体.md#a471784cde53ace4fda5ab532e428c6c8)
- [modem_chat_match](../modem_wireless_model_reference/P054_modem_chat_match_结构体.md)
- [hl78xx_gnss_aux_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9198bafcc7c78243fc72ca2b0bc926ed)
- [hl78xx_gnss_aux_data_callback](../modem_wireless_model_reference/P023_hl78xx_gnss_aux_data_callback_结构体.md)
- [dev](../modem_wireless_model_reference/P023_hl78xx_gnss_aux_data_callback_结构体.md#adcf42adad65b781ea9e5816c2f10b0db)
- [callback](../modem_wireless_model_reference/P023_hl78xx_gnss_aux_data_callback_结构体.md#a2037bb2cfa4c6fb4d9e84489b8e48b8a)
- [hl78xx_api_configure_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga03910e4575bfd4ed439e1c9a0220c7a2)
- [hl78xx_api_get_supported_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6bf75bd8e583b4e076b73268a712977d)
- [hl78xx_api_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7b49e4c0cb9fdb2ef8a6baa5fcdd4f2a)
- [cellular_signal_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga746c0862b9a5da7c766e42e4d6025f47)
- [hl78xx_api_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa7cb75a0ef3cd4cb607bb0e3f3b3468f)
- [cellular_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad6e38e31d82075c51933fcbb2ff2de30)
- [hl78xx_api_get_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga586f65e3f3ea8852261be04ce7ba67ba)
- [cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)
- [hl78xx_api_set_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7cf1c4b11a828c186771200cd00b3bc8)
- [hl78xx_api_get_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab3bcb3ba4cef24971acc41aa0815abe5)
- [hl78xx_api_send_at_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8201489ac8055efa3019ffd8f3201644)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [hl78xx_at_notification](../modem_wireless_model_reference/P018_hl78xx_at_notification_结构体.md)
- [pattern](../modem_wireless_model_reference/P018_hl78xx_at_notification_结构体.md#ac5e4004e705d5675716603171582a01c)
- [argv](../modem_wireless_model_reference/P018_hl78xx_at_notification_结构体.md#a36fd5f326795ace901b6ab0dc22ef934)
- [argc](../modem_wireless_model_reference/P018_hl78xx_at_notification_结构体.md#ad2cd1746e6a6eb2cca28d831de31d798)
- [hl78xx_at_monitor_entry](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md)
- [hl78xx_at_monitor_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga98fde2c3465abce3b4b7d94816bc029c)
- [hl78xx_at_monitor_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga517a58c85701991214ddb3a9d786f367)
- [filter](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#a0ce16aebf50d69f6dbece9f34b1afe1c)
- [handler](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#a7d8c73e1cb6c9ddde19aa05c75e941c8)
- [release](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#af7417e320aa5dabb1283d5593f4166fd)
- [next](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#a0dbf62a2521370ab77e9edb1ea3f728a)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [refcnt](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#ad6d1767212a7cf7f69b113e55b56b99f)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [release_work](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#a378b71d4ebac3e4de62dcae118abe218)
- [paused](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#a718aac1e812cf9466bb263cc3369533e)
- [direct](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#af5f4bcca2ba5a4e9670694182ed8f6eb)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [hl78xx_evt_monitor_entry](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md)
- [hl78xx_evt_monitor_dispatcher_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gade4999c5b603813020cd52a93687b76f)
- [hl78xx_evt_monitor_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaa1346c7b8b44abae64f59cc8d5fa9c01)
- [hl78xx_evt_monitor_release_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga774bbdee241bfb63374fdc74d2353a3d)
- [handler](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#ae1af8f99fe962deaf80f13f3d61552e3)
- [release](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#aa17d06c0c99da863e3eabecc43c89b7b)
- [next](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#aad60b03dc6f1a53b0eaebd4c2e90bf77)
- [refcnt](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#a3c4abc63ba2c55c2e5e718a4873187bb)
- [release_work](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#ab53ac16078049c955f04edd1f26a6b7f)
- [paused](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#aac567b983a9bde01f6d34f6376c1c3c5)
- [direct](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#a4dbe58f2974287076a4629d9ca1ebe77)
- [hl78xx_api_func_set_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaab36b1992acffc8b25b8140da1a79577)
- [hl78xx_api_func_restart](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gad39b680650d8a3f1ea20bc18fa6101d4)
- [hl78xx_api_func_get_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaca72419e4396a45b296a65f89877dbb8)
- [hl78xx_api_func_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae50586b4f939abacda6739850c118982)
- [hl78xx_api_func_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5f9c8c8087e1e6008f290ddfe42e3d97)
- [hl78xx_api_func_get_modem_info_standard](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gacddf878e52d0642279e147add9c8bdad)
- [hl78xx_api_func_get_network_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac08824e4662cb5fcb316e6a0e1e5ba17)
- [hl78xx_api_func_get_rsrp_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gadd718f794b24c9610e97f7460519e577)
- [hl78xx_api_func_get_rsrq_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga79c8b3e0581e6418526b3aa86e6bbb5a)
- [hl78xx_api_func_get_sinr_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga069a0709408fef75514dfaf12bc42cb5)
- [hl78xx_api_func_set_network_operator_format](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab8e5ae21bd129d61735c9cfe3df557d2)
- [hl78xx_api_func_set_prl](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gafc8c324c2beb2c59c9f15542d06b85ee)
- [hl78xx_api_func_get_prl](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga4c2dc7d53dd4780d8f1e00e9889248d3)
- [hl78xx_api_func_set_autorat_inhibit](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga1640ce244f1a4de52efa0b7c33f7b02a)
- [hl78xx_api_func_at_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6adcbc5395d078be2fc9c6e62612f603)
- [hl78xx_set_runtime_band_provider](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac6ed6d4f41003cb2517f802762d5b239)
- [hl78xx_api_func_modem_dynamic_cmd_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae3f2ed904a3b0784d64d2d1537ce9564)
- [hl78xx_modem_at_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga45a97bfc5f73d1877357dc1f410c61cd)
- [hl78xx_modem_at_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga3e9edd942cbf32b5a2eec259c44e5ee4)
- [hl78xx_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabe520e9e9a5e48ab05e238f6b59b8cda)
- [hl78xx_get_network_info](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaedfc9112048d6c987ee7fefa4e8abd55)
- [hl78xx_get_rsrp_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga65f087ad92a0f2bfb15d4f7b627c754f)
- [hl78xx_get_rsrq_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab49ab6eb5aa0cfcdea4e6e7bcabd1d48)
- [hl78xx_get_sinr_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga06800817986b9a4b0291cc22c808dfae)
- [hl78xx_set_prl](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gad564df9a12ad4ee40caeffec1099a93b)
- [hl78xx_set_autorat_inhibit](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaad6374b5c5ef64886c6d8fdde0cba3c4)
- [hl78xx_at_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gad2673b87d730da42b4d2109e849277cc)
- [hl78xx_set_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaee99182459b5971ebaa7892989b0e8df)
- [hl78xx_restart_modem](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2c4ff4a9b1d5d2530700327e1d4af6e0)
- [hl78xx_get_phone_functionality](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf778d092ad7f9b67b0930c0da2375996)
- [hl78xx_modem_cmd_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae7102c14fda882e87bff0f0828ab4263)
- [hl78xx_modem_at_err_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaba7b5c599c1b9285b9dcfbae91ac5e7f)
- [hl78xx_modem_at_err](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga13ead2b7a66530a1fbe15e5c4d9addeb)
- [hl78xx_parse_rssi](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9dd8be5c6d35de4122ab5604bf5b17ce)
- [CSQ_RSSI_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8c28a5a32edb83ea0b0120dd3b00451f)
- [CSQ_RSSI_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab2c8054a088aa6927aa10f1aed1587ae)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [CSQ_RSSI_TO_DB](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga72dfe852d4d6365d80f33b918f631501)
- [hl78xx_parse_rsrp](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8abfb51de22c24f1870d2b5f4b3b60ee)
- [CESQ_RSRP_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga03c48d45ba1dfcdeabba881f2b1cd936)
- [CESQ_RSRP_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gacb02197961c70e98147ae25e4c11d4de)
- [CESQ_RSRP_TO_DB](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga309cc2c1be1d4006e2ccb8d59cb3e916)
- [hl78xx_parse_rsrq](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga09f7b39a934d38a2d3da8deefc3d2758)
- [CESQ_RSRQ_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9a4429e44439c5ebdd18ccd549f832f5)
- [CESQ_RSRQ_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7d02276973c71eded42d4242a34ca745)
- [CESQ_RSRQ_TO_DB](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga536c21c42099fc04ac85a634ffa41d24)
- [hl78xx_evt_monitor_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gadfb6a494068c978908ed0bd968b81a5f)
- [flags](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#acb7a79b0dca67c9a719494c97ab3e710)
- [hl78xx_evt_monitor_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab3a63acd15fc9bd6a7d9ded9ed1731fa)
- [hl78xx_at_monitor_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gab08189be0b4dc7f03428d829f0170bbe)
- [flags](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#aa8e084c925d5b57524c722f74f1b629c)
- [hl78xx_at_monitor_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2723fa7f912913d299629fdba4efb130)
- [hl78xx_at_monitor_register](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga051a63a86e9ca353434b23e1adf5d543)
- [hl78xx_at_monitor_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga1244a8f6b7e5e488ab596aa5341ad66a)
- [hl78xx_evt_notif_handler_set](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8265e020ad0d8c3e69f2219173530720)
- [hl78xx_evt_monitor_register](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6590e5352cbd8ff6ea0580edd64eb0d0)
- [hl78xx_evt_monitor_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf4c623e7bed92b6ea3964b59df04e98e)
- [hl78xx_rat_to_access_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf8cbf3de84df41d7066b9a07f106c17b)
- [hl78xx_access_tech_to_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac9f87f986b0b745bf8e370896113066f)
- [hl78xx_start_airvantage_dm_session](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gaf34ed3d29904f1a18c0c75a0de4bc727)
- [hl78xx_stop_airvantage_dm_session](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9018c8332803eaada4083390c40ac3f0)
- [hl78xx_set_wake_pin_low](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga803bf7a13a7b57477dbfa4d6b3faa14e)
- [hl78xx_set_wake_pin_high](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae3e97cdf80470496d6d8542f61f985c0)
- [hl78xx_set_active_sim](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9bac621e2f74d598329f61cd95b0291b)
- [hl78xx_wakeup_modem](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7cc4861b1449b551246204b84779c621)
- [hl78xx_edrx_get_time_to_sleep](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga41d66fc0e8681bf6a68f47af5bcacb90)
- [hl78xx_enter_gnss_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9e9d288506708b275cc98e508bc8251d)
- [hl78xx_exit_gnss_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga475545d83cf5fd883fd11fb0db8400ed)
- [hl78xx_queue_gnss_search](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga48f504b9bb41d4a13ac592f763aeb207)
- [hl78xx_gnss_set_nmea_output](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5a1949cd23380056b4ee1775b1e6cc3b)
- [hl78xx_gnss_set_search_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae349d6b96ef9ae67b5ed01d0a8fa2cb0)
- [hl78xx_gnss_get_search_timeout_remaining](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga209d0579899aef4ade5cf8de1251a323)
- [hl78xx_gnss_get_latest_known_fix](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga0238b9a2de4683369a0be7a6ed481938)
- [hl78xx_gnss_assist_data_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga473c72484a8a758470ff7043de7ab48d)
- [hl78xx_gnss_assist_data_download](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gabf8fcaa1b5a59d5a2cac3c467f93c9f8)
- [hl78xx_gnss_assist_data_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga452b1ee210417569b3cdfc30db25622a)
- [hl78xx_power_down_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gac7291340f8699bb37cd864516615ea05)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [hl78xx_power_down_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga98af31968e3bf0fc72dea5d56e97e122)
- [hl78xx_power_down_respond](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga249a5bf6cdbd69ec930724bf2541de72)
- [hl78xx_power_down_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2bcaada6a58dfbe3658fc6bcb3090fff)
- [cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h.html)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [hl78xx_agnss_status::days](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md#a5c3fa9011d3d5e71d5aaacc0ecfe7e95)
- [hl78xx_agnss_status::hours](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md#a5e7e0613597dad81c06ca0b7b48a0aba)
- [hl78xx_agnss_status::minutes](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md#aa17d6323d9faeb81b1d3299898166a0b)
- [hl78xx_agnss_status::mode](../modem_wireless_model_reference/P016_hl78xx_agnss_status_结构体.md#aead701aedc1734a4f89bd628030b0850)
- [hl78xx_at_monitor_entry::filter](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#a0ce16aebf50d69f6dbece9f34b1afe1c)
- [hl78xx_at_monitor_entry::next](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#a0dbf62a2521370ab77e9edb1ea3f728a)
- [hl78xx_at_monitor_entry::release_work](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#a378b71d4ebac3e4de62dcae118abe218)
- [hl78xx_at_monitor_entry::paused](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#a718aac1e812cf9466bb263cc3369533e)
- [hl78xx_at_monitor_entry::handler](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#a7d8c73e1cb6c9ddde19aa05c75e941c8)
- [hl78xx_at_monitor_entry::flags](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#aa8e084c925d5b57524c722f74f1b629c)
- [hl78xx_at_monitor_entry::refcnt](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#ad6d1767212a7cf7f69b113e55b56b99f)
- [hl78xx_at_monitor_entry::direct](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#af5f4bcca2ba5a4e9670694182ed8f6eb)
- [hl78xx_at_monitor_entry::release](../modem_wireless_model_reference/P017_hl78xx_at_monitor_entry_结构体.md#af7417e320aa5dabb1283d5593f4166fd)
- [hl78xx_at_notification::argv](../modem_wireless_model_reference/P018_hl78xx_at_notification_结构体.md#a36fd5f326795ace901b6ab0dc22ef934)
- [hl78xx_at_notification::pattern](../modem_wireless_model_reference/P018_hl78xx_at_notification_结构体.md#ac5e4004e705d5675716603171582a01c)
- [hl78xx_at_notification::argc](../modem_wireless_model_reference/P018_hl78xx_at_notification_结构体.md#ad2cd1746e6a6eb2cca28d831de31d798)
- [hl78xx_ctzeu_update::date_time_ms](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md#a0c90dddc2087e97afd6da421a7862323)
- [hl78xx_ctzeu_update::utc_time](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md#a3b4a66b56a5632a7dc7a4964f949f7b1)
- [hl78xx_ctzeu_update::tz](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md#a5e0f09445a9abda3c5f0b37b97473815)
- [hl78xx_ctzeu_update::has_utime](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md#a9f0db53ae132db9a43e6a00b93807145)
- [hl78xx_ctzeu_update::dst](../modem_wireless_model_reference/P019_hl78xx_ctzeu_update_结构体.md#ae5eba83a8def3c9720797fd2f1ff46d0)
- [hl78xx_cxreg_status::has_active_time](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a1b1616b638324a1073a81e2c51d7082a)
- [hl78xx_cxreg_status::reg_status](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a4b5acff39666484d3aa7f4920a33c195)
- [hl78xx_cxreg_status::has_cell_id](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a60f715d0323fa365590d6e6eb8f276fa)
- [hl78xx_cxreg_status::cell_id](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a6c744edb85c63395147b1b55da6dcc9d)
- [hl78xx_cxreg_status::has_tac](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a8674887283917c025827e2d24e07aa21)
- [hl78xx_cxreg_status::tau](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#a90f9a217168113e3b223e6fee7d3a484)
- [hl78xx_cxreg_status::has_rat_mode](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#aa5277387244ff33df4622bcd966138d2)
- [hl78xx_cxreg_status::cause_type](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#aa79861dc75aa6db380d719bd291d6297)
- [hl78xx_cxreg_status::active_time](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#aaec559842aa44a208c800c1056dc1960)
- [hl78xx_cxreg_status::has_cause_type](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#ab93a65b47faea7a583313bd74ea2be24)
- [hl78xx_cxreg_status::has_reject_cause](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#ac35cd02f962b64890911b0792d7310e0)
- [hl78xx_cxreg_status::rat_mode](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#ac5661b4086fb1be97cb562ac0080303c)
- [hl78xx_cxreg_status::tac](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#ae28a6c477536c15740ec07615b156d37)
- [hl78xx_cxreg_status::has_tau](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#aeb8daf30feb1b4c82888f5ce393b2adf)
- [hl78xx_cxreg_status::reject_cause](../modem_wireless_model_reference/P020_hl78xx_cxreg_status_结构体.md#afc07b878db1a4ebd74c1b642c5222866)
- [hl78xx_evt_monitor_entry::refcnt](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#a3c4abc63ba2c55c2e5e718a4873187bb)
- [hl78xx_evt_monitor_entry::direct](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#a4dbe58f2974287076a4629d9ca1ebe77)
- [hl78xx_evt_monitor_entry::release](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#aa17d06c0c99da863e3eabecc43c89b7b)
- [hl78xx_evt_monitor_entry::paused](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#aac567b983a9bde01f6d34f6376c1c3c5)
- [hl78xx_evt_monitor_entry::next](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#aad60b03dc6f1a53b0eaebd4c2e90bf77)
- [hl78xx_evt_monitor_entry::release_work](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#ab53ac16078049c955f04edd1f26a6b7f)
- [hl78xx_evt_monitor_entry::flags](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#acb7a79b0dca67c9a719494c97ab3e710)
- [hl78xx_evt_monitor_entry::handler](../modem_wireless_model_reference/P022_hl78xx_evt_monitor_entry_结构体.md#ae1af8f99fe962deaf80f13f3d61552e3)
- [hl78xx_evt::type](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#a0943763d4df0904b6fd6299f405dc0b4)
- [hl78xx_evt::status](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#a3dbdb39cc7be1dd57a965f7d4a86aebc)
- [hl78xx_evt::power_down_event](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#a83a493750d68fca89be51eddd700dae1)
- [hl78xx_evt::edrx_event](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#a8b207883087d39a428f02f1cc4997043)
- [hl78xx_evt::content](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#aa142ce76ffc686074b6955437633feea)
- [hl78xx_evt::psm_event](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#aabfc3cb2d27cb2a1d7a473af9a6ad621)
- [hl78xx_evt::cellmeas](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#abf9091f1c192664a55b7a8a50e21ee44)
- [hl78xx_evt::ctzeu](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#ac919edeb1b552ce726527b20580303de)
- [hl78xx_evt::event_status](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#accf5c9a1709eb7181aab995267757584)
- [hl78xx_evt::position_event](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#ace5b13c268479f1e8a143e1673c4ea73)
- [hl78xx_evt::value](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#ad81a188c46465fd7d044377393d362f3)
- [hl78xx_evt::rat_mode](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#adfab3032ba9bf936a914e8ac02eed1ca)
- [hl78xx_evt::wdsi_indication](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#aefc1d835f3244e680a33382c0f9d61fb)
- [hl78xx_evt::reg_status](../modem_wireless_model_reference/P021_hl78xx_evt_结构体.md#af114567a2f292991f3c6de3a0b26a7ba)
- [hl78xx_gnss_aux_data_callback::callback](../modem_wireless_model_reference/P023_hl78xx_gnss_aux_data_callback_结构体.md#a2037bb2cfa4c6fb4d9e84489b8e48b8a)
- [hl78xx_gnss_aux_data_callback::dev](../modem_wireless_model_reference/P023_hl78xx_gnss_aux_data_callback_结构体.md#adcf42adad65b781ea9e5816c2f10b0db)
- [hl78xx_gnss_nmea_aux_data::epu](../modem_wireless_model_reference/P024_hl78xx_gnss_nmea_aux_data_结构体.md#a471784cde53ace4fda5ab532e428c6c8)
- [hl78xx_gnss_nmea_aux_data::gsa](../modem_wireless_model_reference/P024_hl78xx_gnss_nmea_aux_data_结构体.md#a529e929ce8878c329f0c370fd8155ce2)
- [hl78xx_gnss_nmea_aux_data::gst](../modem_wireless_model_reference/P024_hl78xx_gnss_nmea_aux_data_结构体.md#a9d099e5d5baf20aa18dfd43e531aa202)
- [hl78xx_network_info::ip_address](../modem_wireless_model_reference/P026_hl78xx_network_info_结构体.md#a350369fc45a40a80fd563997042fed81)
- [hl78xx_network_info::operator_info](../modem_wireless_model_reference/P026_hl78xx_network_info_结构体.md#aa1e49eec0c60b7149ee943853983fc33)
- [hl78xx_network_info::dns_primary](../modem_wireless_model_reference/P026_hl78xx_network_info_结构体.md#ab7f3c7f60d17167d8406dc977639128e)
- [hl78xx_network_operator::has_mcc](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a1024bdecfbe35a84cb9cf6e9c65488ba)
- [hl78xx_network_operator::has_mnc](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a17dd8d113a540a311dc381f61a697012)
- [hl78xx_network_operator::has_operator](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a775fa702eb42a7d520dff3d3a3a4b208)
- [hl78xx_network_operator::mnc](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a8118ab76929803d7f898a62bce1f4f18)
- [hl78xx_network_operator::format](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a9ca090484b881fa6343de3f8475982ed)
- [hl78xx_network_operator::mcc](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#a9ce188616ea483281f6d600d69154cb3)
- [hl78xx_network_operator::operator_name](../modem_wireless_model_reference/P027_hl78xx_network_operator_结构体.md#ab28ba8ce52648d02488efe2799d3337a)
- [hl78xx_network::technology](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md#a0ef743013b5287ef8edd1c7414da2a81)
- [hl78xx_network::bands](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md#a2c956f3333c56c34a197c5f3336030bb)
- [hl78xx_network::size](../modem_wireless_model_reference/P025_hl78xx_network_结构体.md#adac6d7a38cd259a908d3e6f8b8ef9961)
- [k_cellmeas_signal_info::rsrp](../system_service_model_reference/P058_k_cellmeas_signal_info_结构体.md#aedf20f274705729bd3c3b5246baec391)
- [kselacq_syntax::rat2](../system_service_model_reference/P059_kselacq_syntax_结构体.md#a0fe51e6bcae3f2195f62952a8022bda0)
- [kselacq_syntax::rat3](../system_service_model_reference/P059_kselacq_syntax_结构体.md#a8c0973f97ef1cac8cf606e4420b2913b)
- [kselacq_syntax::mode](../system_service_model_reference/P059_kselacq_syntax_结构体.md#a96ce49c04407034f9f7b64bb28a1ab27)
- [kselacq_syntax::rat1](../system_service_model_reference/P059_kselacq_syntax_结构体.md#ac62bc66e12deed5b1b7072f436d2cda8)
- [nmea_match_epu_data::vel_east](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a00bc50a051125d483ecc0372939d3366)
- [nmea_match_epu_data::vel_hdg](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a0b6709964409e68bfc1ec6053599c4d3)
- [nmea_match_epu_data::pos_alt](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a1545c6fbe045b9770b0701ba89b76353)
- [nmea_match_epu_data::pos_2d](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a1824d2be73ef8309c000e71fc28d685e)
- [nmea_match_epu_data::vel_2d](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a2bebe6e0c3b502cddb46ded81339c96d)
- [nmea_match_epu_data::vel_north](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a342a008ff997d77e50be985807e09e39)
- [nmea_match_epu_data::pos_lon](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a4441cc16e1cb15ab6d631d6f2408ffd8)
- [nmea_match_epu_data::vel_up](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a5fd2bd27efde367b4b8cee37a6f73cfe)
- [nmea_match_epu_data::vel_3d](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a854b002cd40b9803e8767136a9b100a5)
- [nmea_match_epu_data::pos_3d](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#a869278cfd8e19efd76ab25c620d98972)
- [nmea_match_epu_data::pos_lat](../sensor_navigation_model_reference/P019_nmea_match_epu_data_结构体.md#af001cd72af6d3f37d37b94e9c1c3f16b)
- [nmea_match_gsa_data::vdop](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md#a872c2e3cbcd0dcf5b0fff194f794622f)
- [nmea_match_gsa_data::hdop](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md#a9a785ec7d4c1ef2727e202927fd67440)
- [nmea_match_gsa_data::pdop](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md#aa4caab02bb1ab3a0c3014c4a3f993eae)
- [nmea_match_gsa_data::fix_type](../sensor_navigation_model_reference/P020_nmea_match_gsa_data_结构体.md#aed176a2bc4f981221c69e1b08099df67)
- [nmea_match_gst_data::lat_err](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a4fdfb99f5c451ac7360613579a68416a)
- [nmea_match_gst_data::alt_err](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a590ae7d7df7a4c78da267f0dc9f451f2)
- [nmea_match_gst_data::sd_major](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a5bc62b0b55f62c0922fc00d13ff2f364)
- [nmea_match_gst_data::lon_err](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a667027ebf56ecdd29be0321e982cb72f)
- [nmea_match_gst_data::rms](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a7ba102be3748cdad0d9a44bd68d6c70f)
- [nmea_match_gst_data::orient](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a8032be26aa57b4feb55dd119183b3d47)
- [nmea_match_gst_data::gst_utc](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#a932c670f5a642ad7449806f69910328f)
- [nmea_match_gst_data::sd_minor](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#aab1c6e9433619af20da9182d693ed692)
- [nmea_match_gst_data::i32](../sensor_navigation_model_reference/P021_nmea_match_gst_data_结构体.md#af7061a41e30e58c5cc58bebbd1663f9c)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P029_gd32vf103.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P031_ifx_cat1-pinctrl.h_源码浏览.md)
