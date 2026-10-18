---
id: learning.zephyr-docs.api-source-supplement-reference.page-19
title: bip.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bip_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_bip.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h.html)。

## 19.1\_原始可见代码（Source Code）

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
<a id="l00011"></a>
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
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00084"></a>
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
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00141"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="foldopen00190"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="foldopen00239"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00243"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="foldopen00263"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="foldopen00277"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="foldopen00295"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="foldopen00313"></a>
<a id="l00313"></a>
<a id="l00315"></a>
<a id="l00317"></a>
<a id="l00319"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="foldopen00344"></a>
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
<a id="l00376"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="foldopen00386"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="foldopen00474"></a>
<a id="l00474"></a>
<a id="l00476"></a>
<a id="l00478"></a>
<a id="l00480"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="foldopen00493"></a>
<a id="l00493"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="foldopen00676"></a>
<a id="l00676"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00856"></a>
<a id="l00857"></a>
<a id="l00858"></a>
<a id="foldopen00864"></a>
<a id="l00864"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00869"></a>
<a id="l00870"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00878"></a>
<a id="l00879"></a>
<a id="l00881"></a>
<a id="l00882"></a>
<a id="l00884"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00889"></a>
<a id="l00890"></a>
<a id="l00892"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00898"></a>
<a id="l00899"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="foldopen00909"></a>
<a id="l00909"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00917"></a>
<a id="l00918"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00932"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00938"></a>
<a id="l00939"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00955"></a>
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="l00971"></a>
<a id="l00972"></a>
<a id="l00973"></a>
<a id="l00974"></a>
<a id="foldopen00980"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="l00985"></a>
<a id="foldopen00991"></a>
<a id="l00991"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="foldopen01002"></a>
<a id="l01002"></a>
<a id="l01003"></a>
<a id="l01004"></a>
<a id="l01005"></a>
<a id="l01006"></a>
<a id="l01007"></a>
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
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01032"></a>
<a id="l01033"></a>
<a id="l01034"></a>
<a id="l01035"></a>
<a id="l01036"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01047"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="foldopen01051"></a>
<a id="l01051"></a>
<a id="l01052"></a>
<a id="l01053"></a>
<a id="l01054"></a>
<a id="foldopen01056"></a>
<a id="l01056"></a>
<a id="l01057"></a>
<a id="l01058"></a>
<a id="l01059"></a>
<a id="foldopen01061"></a>
<a id="l01061"></a>
<a id="l01062"></a>
<a id="l01063"></a>
<a id="l01064"></a>
<a id="foldopen01066"></a>
<a id="l01066"></a>
<a id="l01067"></a>
<a id="l01068"></a>
<a id="l01069"></a>
<a id="foldopen01071"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01073"></a>
<a id="l01074"></a>
<a id="foldopen01076"></a>
<a id="l01076"></a>
<a id="l01077"></a>
<a id="l01078"></a>
<a id="l01079"></a>
<a id="foldopen01081"></a>
<a id="l01081"></a>
<a id="l01082"></a>
<a id="l01083"></a>
<a id="l01084"></a>
<a id="foldopen01086"></a>
<a id="l01086"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01089"></a>
<a id="l01103"></a>
<a id="l01104"></a>
<a id="l01105"></a>
<a id="l01106"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="foldopen01137"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="foldopen01157"></a>
<a id="l01157"></a>
<a id="l01158"></a>
<a id="l01159"></a>
<a id="l01160"></a>
<a id="l01161"></a>
<a id="l01162"></a>
<a id="l01163"></a>
<a id="l01164"></a>
<a id="l01165"></a>
<a id="foldopen01177"></a>
<a id="l01177"></a>
<a id="l01178"></a>
<a id="l01179"></a>
<a id="l01180"></a>
<a id="l01181"></a>
<a id="l01182"></a>
<a id="l01183"></a>
<a id="l01184"></a>
<a id="foldopen01196"></a>
<a id="l01196"></a>
<a id="l01197"></a>
<a id="l01198"></a>
<a id="l01199"></a>
<a id="l01200"></a>
<a id="l01201"></a>
<a id="l01202"></a>
<a id="l01203"></a>
<a id="l01204"></a>
<a id="foldopen01216"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01221"></a>
<a id="l01222"></a>
<a id="l01223"></a>
<a id="l01224"></a>
<a id="foldopen01236"></a>
<a id="l01236"></a>
<a id="l01237"></a>
<a id="l01238"></a>
<a id="l01239"></a>
<a id="l01240"></a>
<a id="l01241"></a>
<a id="l01242"></a>
<a id="l01243"></a>
<a id="l01244"></a>
<a id="foldopen01258"></a>
<a id="l01258"></a>
<a id="l01259"></a>
<a id="l01260"></a>
<a id="l01261"></a>
<a id="l01262"></a>
<a id="l01263"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="foldopen01279"></a>
<a id="l01279"></a>
<a id="l01280"></a>
<a id="l01281"></a>
<a id="l01282"></a>
<a id="l01283"></a>
<a id="l01284"></a>
<a id="l01285"></a>
<a id="l01286"></a>
<a id="l01297"></a>
<a id="l01298"></a>
<a id="l01312"></a>
<a id="l01313"></a>
<a id="l01314"></a>
<a id="l01315"></a>
<a id="l01330"></a>
<a id="l01331"></a>
<a id="l01332"></a>
<a id="l01333"></a>
<a id="foldopen01345"></a>
<a id="l01345"></a>
<a id="l01346"></a>
<a id="l01347"></a>
<a id="l01348"></a>
<a id="l01349"></a>
<a id="l01350"></a>
<a id="l01351"></a>
<a id="l01352"></a>
<a id="l01353"></a>
<a id="foldopen01365"></a>
<a id="l01365"></a>
<a id="l01366"></a>
<a id="l01367"></a>
<a id="l01368"></a>
<a id="l01369"></a>
<a id="l01370"></a>
<a id="l01371"></a>
<a id="l01372"></a>
<a id="l01373"></a>
<a id="foldopen01385"></a>
<a id="l01385"></a>
<a id="l01386"></a>
<a id="l01387"></a>
<a id="l01388"></a>
<a id="l01389"></a>
<a id="l01390"></a>
<a id="l01391"></a>
<a id="l01392"></a>
<a id="foldopen01404"></a>
<a id="l01404"></a>
<a id="l01405"></a>
<a id="l01406"></a>
<a id="l01407"></a>
<a id="l01408"></a>
<a id="l01409"></a>
<a id="l01410"></a>
<a id="l01411"></a>
<a id="l01412"></a>
<a id="foldopen01424"></a>
<a id="l01424"></a>
<a id="l01425"></a>
<a id="l01426"></a>
<a id="l01427"></a>
<a id="l01428"></a>
<a id="l01429"></a>
<a id="l01430"></a>
<a id="l01431"></a>
<a id="l01432"></a>
<a id="foldopen01444"></a>
<a id="l01444"></a>
<a id="l01445"></a>
<a id="l01446"></a>
<a id="l01447"></a>
<a id="l01448"></a>
<a id="l01449"></a>
<a id="l01450"></a>
<a id="l01451"></a>
<a id="l01452"></a>
<a id="foldopen01465"></a>
<a id="l01465"></a>
<a id="l01466"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01469"></a>
<a id="l01470"></a>
<a id="l01471"></a>
<a id="l01472"></a>
<a id="foldopen01485"></a>
<a id="l01485"></a>
<a id="l01486"></a>
<a id="l01487"></a>
<a id="l01488"></a>
<a id="l01489"></a>
<a id="l01490"></a>
<a id="l01491"></a>
<a id="l01492"></a>
<a id="l01493"></a>
<a id="l01494"></a>
<a id="l01505"></a>
<a id="l01506"></a>
<a id="l01516"></a>
<a id="l01517"></a>
<a id="l01528"></a>
<a id="l01529"></a>
<a id="l01539"></a>
<a id="l01540"></a>
<a id="l01551"></a>
<a id="l01552"></a>
<a id="l01566"></a>
<a id="l01567"></a>
<a id="l01580"></a>
<a id="l01581"></a>
<a id="l01582"></a>
<a id="l01600"></a>
<a id="l01601"></a>
<a id="l01615"></a>
<a id="l01616"></a>
<a id="l01631"></a>
<a id="l01632"></a>
<a id="l01647"></a>
<a id="l01648"></a>
<a id="l01649"></a>
<a id="l01664"></a>
<a id="l01665"></a>
<a id="l01679"></a>
<a id="l01680"></a>
<a id="l01695"></a>
<a id="l01696"></a>
<a id="l01709"></a>
<a id="l01710"></a>
<a id="l01711"></a>
<a id="l01726"></a>
<a id="l01727"></a>
<a id="l01740"></a>
<a id="l01741"></a>
<a id="l01742"></a>
<a id="l01759"></a>
<a id="l01760"></a>
<a id="l01773"></a>
<a id="l01774"></a>
<a id="l01775"></a>
<a id="l01791"></a>
<a id="l01792"></a>
<a id="l01806"></a>
<a id="l01807"></a>
<a id="l01808"></a>
<a id="l01822"></a>
<a id="l01823"></a>
<a id="l01834"></a>
<a id="l01835"></a>
<a id="l01850"></a>
<a id="l01851"></a>
<a id="l01864"></a>
<a id="l01865"></a>
<a id="l01880"></a>
<a id="l01881"></a>
<a id="l01892"></a>
<a id="l01893"></a>
<a id="l01894"></a>
<a id="l01909"></a>
<a id="l01910"></a>
<a id="l01921"></a>
<a id="l01922"></a>
<a id="l01923"></a>
<a id="l01939"></a>
<a id="l01940"></a>
<a id="l01953"></a>
<a id="l01954"></a>
<a id="l01969"></a>
<a id="l01970"></a>
<a id="l01981"></a>
<a id="l01982"></a>
<a id="l01998"></a>
<a id="l01999"></a>
<a id="l02010"></a>
<a id="l02011"></a>
<a id="l02027"></a>
<a id="l02028"></a>
<a id="l02039"></a>
<a id="l02040"></a>
<a id="l02052"></a>
<a id="l02053"></a>
<a id="l02065"></a>
<a id="l02066"></a>
<a id="l02067"></a>
<a id="l02068"></a>
<a id="l02069"></a>
<a id="l02070"></a>
<a id="l02074"></a>
<a id="l02075"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="abluetooth_2uuid_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agoep_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__bt__bip_html_ga002f7713a8269c0b00a415bbb8c53fce"></a>
<a id="agroup__bt__bip_html_ga0180461f24c6f741e056d64f9758b89e"></a>
<a id="agroup__bt__bip_html_ga021a5d82b292d04cd0e2d53b1b32344b"></a>
<a id="agroup__bt__bip_html_ga0987a342b43bdd1926f3730f471ca05f"></a>
<a id="agroup__bt__bip_html_ga0c54da02bc8dda26794f398e06e66cb3"></a>
<a id="agroup__bt__bip_html_ga17ae73bd6088b44206378afe3b0b9eb0"></a>
<a id="agroup__bt__bip_html_ga1975916aa3da40576499f6d05aac1285"></a>
<a id="agroup__bt__bip_html_ga1c341ad182ff418286b64b4eff491445"></a>
<a id="agroup__bt__bip_html_ga1fda174189b57c54f365784d1909152e"></a>
<a id="agroup__bt__bip_html_ga2b6a2a51fb00e7060e196051f8aea4c4"></a>
<a id="agroup__bt__bip_html_ga2d4919c1eb568f33a89d8b176f103601"></a>
<a id="agroup__bt__bip_html_ga301ff6e5a1e8775295659442b8c20e15"></a>
<a id="agroup__bt__bip_html_ga30d9309cbbd88b54508551285b21e575"></a>
<a id="agroup__bt__bip_html_ga30e3a6ad8c00c230ac3591a934cfb81f"></a>
<a id="agroup__bt__bip_html_ga34de6d20263274292543a7a8afbd2c6b"></a>
<a id="agroup__bt__bip_html_ga35c44217cbfcd8661c3f2e5725be9323"></a>
<a id="agroup__bt__bip_html_ga3848d86378912fbd9c896b14aed74161"></a>
<a id="agroup__bt__bip_html_ga39ec2019f86d42b02992b0a9d3ba094c"></a>
<a id="agroup__bt__bip_html_ga45f1ca2d2874500d6f8df3a62b01260e"></a>
<a id="agroup__bt__bip_html_ga4b236a8a28c359e392633d472a508405"></a>
<a id="agroup__bt__bip_html_ga4ca80902f04ea770c59c5e498fef615a"></a>
<a id="agroup__bt__bip_html_ga4e06b2fb9a99f89d7e65e8a52690442d"></a>
<a id="agroup__bt__bip_html_ga5167b2dab89a983fae9fca356e6fbcf9"></a>
<a id="agroup__bt__bip_html_ga5302af5beb7cd5c98a9cbdc288f09d3c"></a>
<a id="agroup__bt__bip_html_ga53fb15ff7d0728b09f1c4e8d2ceb6dee"></a>
<a id="agroup__bt__bip_html_ga54c37cced33fa72a2c6cea10e2996e6d"></a>
<a id="agroup__bt__bip_html_ga578c2b59fbc8afee530168452eb221fb"></a>
<a id="agroup__bt__bip_html_ga5c3cd3e39fc21a584d6955a160ca126a"></a>
<a id="agroup__bt__bip_html_ga5ed2a46482e4fe60ef23c540001b58a3"></a>
<a id="agroup__bt__bip_html_ga644ca479c156b10d920d87d862401fc7"></a>
<a id="agroup__bt__bip_html_ga66a86a399f73dba932dc05d63b3749bd"></a>
<a id="agroup__bt__bip_html_ga6768e59b79bb67b5d385fdaa3dfb8888"></a>
<a id="agroup__bt__bip_html_ga6e33bba952a9693d1fed7ee9bdf03df8"></a>
<a id="agroup__bt__bip_html_ga70bf0d46bd16d0207e13eeb9a7844f1c"></a>
<a id="agroup__bt__bip_html_ga72ef6cd266b7e57e1c80b6d8eba799e2"></a>
<a id="agroup__bt__bip_html_ga79831fc5fff332a891e6b9ff71f81d20"></a>
<a id="agroup__bt__bip_html_ga7abdde3a7e5dcda9c6187b5e45b75cc2"></a>
<a id="agroup__bt__bip_html_ga7b3c6cb1159e7b2ede57c66f20b23827"></a>
<a id="agroup__bt__bip_html_ga86085e98964dcfd19725b5d96f38a99b"></a>
<a id="agroup__bt__bip_html_ga8a948dcee431ced321e7b5d51c8d5f9c"></a>
<a id="agroup__bt__bip_html_ga8b730495f4dd4e6f8db85c5b060a3cae"></a>
<a id="agroup__bt__bip_html_ga9352b8309334a3fe89d77f5714443376"></a>
<a id="agroup__bt__bip_html_ga9542e030ea863b4379d36fa21de262dc"></a>
<a id="agroup__bt__bip_html_ga9674dc3dc2137a663a971f8521a41845"></a>
<a id="agroup__bt__bip_html_ga98dca7b222c8a09b1c44861c9060193b"></a>
<a id="agroup__bt__bip_html_ga9a91c35e91a0c30eab55da5b842427d9"></a>
<a id="agroup__bt__bip_html_ga9f1593748ffcf29015533d52266a8e19"></a>
<a id="agroup__bt__bip_html_gaa0f071c8c83a54b2d48f478594579719"></a>
<a id="agroup__bt__bip_html_gaafcd6a3503795299b6fb777ba0aa0cff"></a>
<a id="agroup__bt__bip_html_gab0a3b58b041ac4af2682fb96b8f00a7e"></a>
<a id="agroup__bt__bip_html_gab24c4f7144f8c43dcf1b82a4c33e4ffd"></a>
<a id="agroup__bt__bip_html_gab5a80d7a992d0afa0270eb09d6f3275c"></a>
<a id="agroup__bt__bip_html_gac4ba5cef40cd451bd4b505dbea0fa135"></a>
<a id="agroup__bt__bip_html_gac96e873a840b072f5213b7483d633aaa"></a>
<a id="agroup__bt__bip_html_gacfc8aaea3d27e3a42a14c49b880a5b90"></a>
<a id="agroup__bt__bip_html_gad062c0f3d2feeb92a866f0fe91a6f231"></a>
<a id="agroup__bt__bip_html_gad16038fa018919a10d9be7fa6deeb659"></a>
<a id="agroup__bt__bip_html_gad32c1b1118b606ab3ae0d9db889cbab9"></a>
<a id="agroup__bt__bip_html_gad53a7666b90a97034276fe341c2bd7a2"></a>
<a id="agroup__bt__bip_html_gad6a7df2b0c49c0df616ef170c7b9e431"></a>
<a id="agroup__bt__bip_html_gad95944f07cd9f7b6bb9c81f21fffd447"></a>
<a id="agroup__bt__bip_html_gad9c05d28e1e2124675b5906990c3408c"></a>
<a id="agroup__bt__bip_html_gaddfcee2eaea19b4819d83cf6ecb396da"></a>
<a id="agroup__bt__bip_html_gadf624e05a6d008bdcfd8a61ae6341f42"></a>
<a id="agroup__bt__bip_html_gae4d1ed3b7e27768c1dbb6ce448cb5cf9"></a>
<a id="agroup__bt__bip_html_gae557b198b9d5606ee05cd29ed16f9482"></a>
<a id="agroup__bt__bip_html_gae8b37b224ea419ca1f1761d98a34cb2d"></a>
<a id="agroup__bt__bip_html_gae9ea9f936aa75b287a2152a747fd687a"></a>
<a id="agroup__bt__bip_html_gaea5d5f5b6c29a44ae89939ee3e2d6efb"></a>
<a id="agroup__bt__bip_html_gaefd318b5dc2e813eea2cd7608be1170c"></a>
<a id="agroup__bt__bip_html_gaf48266502eacfc19938e1dfb29a3619b"></a>
<a id="agroup__bt__bip_html_gaf54b07acf22c5231b2de0fdeca7807c2"></a>
<a id="agroup__bt__bip_html_gaf551904672eda53e9dfcbb5a6bf4c2c3"></a>
<a id="agroup__bt__bip_html_gafcd2d4e6a8ad906c9692313421175431"></a>
<a id="agroup__bt__bip_html_gafe7df6ee236da3a11104f1aa6e948bfe"></a>
<a id="agroup__bt__bip_html_gaff38654d69104bebaaf5884283e197ef"></a>
<a id="agroup__bt__bip_html_gaffb77f6c80ba05046df03d62baad211b"></a>
<a id="agroup__bt__bip_html_gga30d9309cbbd88b54508551285b21e575a87d1fe99824b216780435898c2dfa968"></a>
<a id="agroup__bt__bip_html_gga30d9309cbbd88b54508551285b21e575aa5cdb11f2b0ac9c20c380dd48c9edaa5"></a>
<a id="agroup__bt__bip_html_gga30d9309cbbd88b54508551285b21e575aaa7de8d668d248049c5d5c75ae35d74b"></a>
<a id="agroup__bt__bip_html_gga34de6d20263274292543a7a8afbd2c6ba0f0d78c2da3d8f3d0caf015525b3e010"></a>
<a id="agroup__bt__bip_html_gga34de6d20263274292543a7a8afbd2c6ba0ff60914fb36e587b42a473c25bd6a2d"></a>
<a id="agroup__bt__bip_html_gga34de6d20263274292543a7a8afbd2c6ba2565f26c0322935acef85725ac8982e5"></a>
<a id="agroup__bt__bip_html_gga34de6d20263274292543a7a8afbd2c6ba683d101ea1babf1f147d1869ab7424f4"></a>
<a id="agroup__bt__bip_html_gga34de6d20263274292543a7a8afbd2c6ba9dbbb8ed95c7ccd86a74263fef1a1e92"></a>
<a id="agroup__bt__bip_html_gga34de6d20263274292543a7a8afbd2c6baa7b18ee3ae56c0f0e84a103c1e59f05d"></a>
<a id="agroup__bt__bip_html_gga34de6d20263274292543a7a8afbd2c6bab0e2dfb17de25f4ec3b27b29c2659afa"></a>
<a id="agroup__bt__bip_html_gga34de6d20263274292543a7a8afbd2c6bace4966644e9194273b635b916eac0871"></a>
<a id="agroup__bt__bip_html_gga34de6d20263274292543a7a8afbd2c6bad6511bb04da2cf325a39bfee93f51e0c"></a>
<a id="agroup__bt__bip_html_gga34de6d20263274292543a7a8afbd2c6baef58e631bfd6c511318c386308374274"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888a03c928dd502a98b72cb7d8eebad4b384"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888a045dfb07426eacb16fd69247eecf70b1"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888a0bde5efd58b339e53db3779a159239c1"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888a0ee047481a35e26fa0d03bf7594d7752"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888a2e1f3364145560587963402881bb2705"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888a3cae66cb380311938f83bb099a2d02da"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888a50271c1bac792020f0fb869bb523e506"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888a7843f4dece6ff449b97ba0a2c7298b90"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888a8a417f3073f017af866877f88ee10228"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888abf825fb7d634906f0204780ef81ca5b3"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888ac3ec252a63d494ce3e4dd696d05d94bc"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888adb0e03118b1cd62fe7e97b53e9f52d41"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888ae1312bb3417f901204ac592e4b9376df"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888ae1e97efb19d10ac2b508a9e65b5c43ce"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888af29095b3b5964062e98b9e357de87f89"></a>
<a id="agroup__bt__bip_html_gga6768e59b79bb67b5d385fdaa3dfb8888afb1777cefdbd00e3432ddf5180804f48"></a>
<a id="agroup__bt__bip_html_gga7b3c6cb1159e7b2ede57c66f20b23827a1af8a1481b10b53c58af8e36c7b91588"></a>
<a id="agroup__bt__bip_html_gga7b3c6cb1159e7b2ede57c66f20b23827a7340b2e209c71d9f944b303c22cb264d"></a>
<a id="agroup__bt__bip_html_gga7b3c6cb1159e7b2ede57c66f20b23827ad4444da19b4e0f499867ea967dfc578f"></a>
<a id="agroup__bt__bip_html_gga7b3c6cb1159e7b2ede57c66f20b23827ae78c865c0034d405391aaf9f72e4c9b2"></a>
<a id="agroup__bt__bip_html_ggacfc8aaea3d27e3a42a14c49b880a5b90a132dd77e79fbfda8a78d5034d4c618c5"></a>
<a id="agroup__bt__bip_html_ggacfc8aaea3d27e3a42a14c49b880a5b90a49668a596059e535bd59ac095dffa050"></a>
<a id="agroup__bt__bip_html_ggacfc8aaea3d27e3a42a14c49b880a5b90a8904b7b8288e1b47d2242f5d686e32d9"></a>
<a id="agroup__bt__bip_html_ggacfc8aaea3d27e3a42a14c49b880a5b90a97141e2764fad3714c03b6be69ff2a9a"></a>
<a id="agroup__bt__bip_html_ggacfc8aaea3d27e3a42a14c49b880a5b90aba576edd916dbf49118e78572f70320b"></a>
<a id="agroup__bt__bip_html_ggacfc8aaea3d27e3a42a14c49b880a5b90ac14657fd4af96f4c837916b832c25a0f"></a>
<a id="agroup__bt__bip_html_ggacfc8aaea3d27e3a42a14c49b880a5b90ac64d953311bc9b76bfe75dd3133f5563"></a>
<a id="agroup__bt__bip_html_ggacfc8aaea3d27e3a42a14c49b880a5b90add6c2e70541aae8124bad4b102d64b88"></a>
<a id="agroup__bt__bip_html_ggacfc8aaea3d27e3a42a14c49b880a5b90af72e05ca427f8c5091e50cddac522045"></a>
<a id="agroup__bt__bip_html_ggad062c0f3d2feeb92a866f0fe91a6f231a324c0590cefb5d7a39f90d90e3466334"></a>
<a id="agroup__bt__bip_html_ggad062c0f3d2feeb92a866f0fe91a6f231a4a738d195dcf0908a64bdd246672d4bb"></a>
<a id="agroup__bt__bip_html_ggad062c0f3d2feeb92a866f0fe91a6f231a786ef1ad1bde68f9b026c9d080cc41d4"></a>
<a id="agroup__bt__bip_html_ggad062c0f3d2feeb92a866f0fe91a6f231ac9c5d73b0d2d5eb25a962fa72ede6d5a"></a>
<a id="agroup__bt__bip_html_ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a96f12788ce6f56012ac4b1c25f63f67e"></a>
<a id="agroup__bt__bip_html_ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a984245e44981ad3d85518ab1c3f576e8"></a>
<a id="agroup__bt__bip_html_ggae4d1ed3b7e27768c1dbb6ce448cb5cf9acdc7fe9ee4c0d0ba447bc43817364478"></a>
<a id="agroup__bt__bip_html_ggae4d1ed3b7e27768c1dbb6ce448cb5cf9ae65c7b972effa225116ec8abfcf07bc3"></a>
<a id="agroup__bt__bip_html_ggaff38654d69104bebaaf5884283e197efa05372dbd0a01855f0863ce355a503c61"></a>
<a id="agroup__bt__bip_html_ggaff38654d69104bebaaf5884283e197efa05de3a972070aa4d1e29851479860d9f"></a>
<a id="agroup__bt__bip_html_ggaff38654d69104bebaaf5884283e197efa12873fc1888cd99703131ae71134f0c7"></a>
<a id="agroup__bt__bip_html_ggaff38654d69104bebaaf5884283e197efa4d5ab575c877aa2a43c29cbb52a361c7"></a>
<a id="agroup__bt__bip_html_ggaff38654d69104bebaaf5884283e197efa612cd818200f49e37235917fead216d2"></a>
<a id="agroup__bt__bip_html_ggaff38654d69104bebaaf5884283e197efa8b576c667b9c6458e44ec67674bdffbd"></a>
<a id="agroup__bt__bip_html_ggaff38654d69104bebaaf5884283e197efabe15f984d6907bdb40c10e893e1c3bf6"></a>
<a id="agroup__bt__bip_html_ggaff38654d69104bebaaf5884283e197efaf762949693b7cf70739ed0a0eb6a9d58"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="akernel_8h_html"></a>
<a id="al2cap_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__bip__client__cb_html"></a>
<a id="astructbt__bip__client__cb_html_a00575e54960da7eadb6c97603c15db76"></a>
<a id="astructbt__bip__client__cb_html_a0fb9d1c1bde99fab9f68997dcce31cca"></a>
<a id="astructbt__bip__client__cb_html_a1085306d4098491363df71e82baab9e3"></a>
<a id="astructbt__bip__client__cb_html_a16aea4cd3428723afee39332f6112c3e"></a>
<a id="astructbt__bip__client__cb_html_a287c05808d89726d5a3fbe965b29fd52"></a>
<a id="astructbt__bip__client__cb_html_a3aae2299cb0779cf517d40368dc9a97e"></a>
<a id="astructbt__bip__client__cb_html_a3ead32fbbe46d4ec0e73d0a840dc30b0"></a>
<a id="astructbt__bip__client__cb_html_a3f6e8efdbdee62d23532bff52850ddb3"></a>
<a id="astructbt__bip__client__cb_html_a5bb82c50c8e535457c17726e6133b4ef"></a>
<a id="astructbt__bip__client__cb_html_a6ad152e72050d05eb8b47ba00237b6c4"></a>
<a id="astructbt__bip__client__cb_html_a7228b45ce57155f308d6a9b983074997"></a>
<a id="astructbt__bip__client__cb_html_a72937856348fabd76696237a55ced1e9"></a>
<a id="astructbt__bip__client__cb_html_a9efe5d25e239144bb40e05ff6494f20d"></a>
<a id="astructbt__bip__client__cb_html_a9f7713e8e68233c5837edbb46de6c758"></a>
<a id="astructbt__bip__client__cb_html_aa551eac8ba777bbb7e286e36015a5a72"></a>
<a id="astructbt__bip__client__cb_html_aaedbc7f33eba36d176360c4806a3a27e"></a>
<a id="astructbt__bip__client__cb_html_acda8a5a4ae315bf1b65209df9ff6b8e4"></a>
<a id="astructbt__bip__client__cb_html_aec614697e4e4ccd3dd326ecffc311c9b"></a>
<a id="astructbt__bip__client__cb_html_afd9b65b4810a31a8bd48502fcf11eff1"></a>
<a id="astructbt__bip__client_html"></a>
<a id="astructbt__bip__l2cap__server_html"></a>
<a id="astructbt__bip__l2cap__server_html_a830f0f266401a3e95c21e5fbb25bc057"></a>
<a id="astructbt__bip__l2cap__server_html_aeb027a550bef264ef287e25cc3d9ffa9"></a>
<a id="astructbt__bip__rfcomm__server_html"></a>
<a id="astructbt__bip__rfcomm__server_html_a40ec65e156c02ad06b55aa1fc594ca71"></a>
<a id="astructbt__bip__rfcomm__server_html_ad7b714b584c18e41feb7385819c50511"></a>
<a id="astructbt__bip__server__cb_html"></a>
<a id="astructbt__bip__server__cb_html_a094c1d805d9e099cacb9b91315c799e7"></a>
<a id="astructbt__bip__server__cb_html_a0f8052f0ee8a4e5130b538e25231fc1b"></a>
<a id="astructbt__bip__server__cb_html_a27710e3871c031d4d787dc6f2223e71d"></a>
<a id="astructbt__bip__server__cb_html_a40c07a467ff5573400cc10ba58ee54f2"></a>
<a id="astructbt__bip__server__cb_html_a48d411ddb30784a729204080420c203d"></a>
<a id="astructbt__bip__server__cb_html_a4c8bf0f0791766e8c547ea10630e0948"></a>
<a id="astructbt__bip__server__cb_html_a6514602bea0d066abdf41d6f021d4d51"></a>
<a id="astructbt__bip__server__cb_html_a6c93a136a7677aa05928e762415af2de"></a>
<a id="astructbt__bip__server__cb_html_a6ca521f03e917b7354eaefac20b5b33f"></a>
<a id="astructbt__bip__server__cb_html_a755b097ab450d312a3e29f5b1a75dadf"></a>
<a id="astructbt__bip__server__cb_html_a7b0c02fd0c1546e730df162b14db745b"></a>
<a id="astructbt__bip__server__cb_html_a81f786528f0db0afc54f7518f3765df0"></a>
<a id="astructbt__bip__server__cb_html_a877caeb43927ab27b360cd27b628b683"></a>
<a id="astructbt__bip__server__cb_html_a904935d6a327b9eba0ea68e924d8c1c5"></a>
<a id="astructbt__bip__server__cb_html_ac38d13107bbd18400690196efeddb228"></a>
<a id="astructbt__bip__server__cb_html_ad2630977d48b11da5c70762f4e6cb49e"></a>
<a id="astructbt__bip__server__cb_html_aefa142e33e50b8d23f89c732fd79a125"></a>
<a id="astructbt__bip__server__cb_html_af41d62e8ff812c9ace9a5c916c08314d"></a>
<a id="astructbt__bip__server__cb_html_afc3ba204dd51bdc758cf3a6da9d72185"></a>
<a id="astructbt__bip__server_html"></a>
<a id="astructbt__bip__transport__ops_html"></a>
<a id="astructbt__bip__transport__ops_html_a49f1708ed03ebe8cfb6a2f11b76bda73"></a>
<a id="astructbt__bip__transport__ops_html_a80a1596a382b93366e13a857a5edf3ba"></a>
<a id="astructbt__bip_html"></a>
<a id="astructbt__bip_html_a245296151dcf59b69822e3122488c2c2"></a>
<a id="astructbt__bip_html_a9cee12abb9b8efadb1b7c3e21803f349"></a>
<a id="astructbt__bip_html_ac5b8a3fd23216a0894a47ac487835bc0"></a>
<a id="astructbt__bip_html_adba3573d8d8250c015cb5adca9bd77bb"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__goep__transport__l2cap__server_html"></a>
<a id="astructbt__goep__transport__rfcomm__server_html"></a>
<a id="astructbt__goep__transport_html"></a>
<a id="astructbt__goep_html"></a>
<a id="astructbt__obex__client_html"></a>
<a id="astructbt__obex__server_html"></a>
<a id="astructbt__uuid__128_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_ae75b7ca728fb7440ea483be8bf88bc38"></a>
<a id="astructuuid_html"></a>

```c
/* bip.h - Bluetooth Basic Imaging Profile handling */

/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_BIP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_BIP_H_


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

#define BT_BIP_HDR_TYPE_GET_CAPS              "x-bt/img-capabilities"
#define BT_BIP_HDR_TYPE_GET_IMAGE_LIST        "x-bt/img-listing"
#define BT_BIP_HDR_TYPE_GET_IMAGE_PROPERTIES  "x-bt/img-properties"
#define BT_BIP_HDR_TYPE_GET_IMAGE             "x-bt/img-img"
#define BT_BIP_HDR_TYPE_GET_LINKED_THUMBNAIL  "x-bt/img-thm"
#define BT_BIP_HDR_TYPE_GET_LINKED_ATTACHMENT "x-bt/img-attachment"
#define BT_BIP_HDR_TYPE_GET_PARTIAL_IMAGE     "x-bt/img-partial"
#define BT_BIP_HDR_TYPE_GET_MONITORING_IMAGE  "x-bt/img-monitoring"
#define BT_BIP_HDR_TYPE_GET_STATUS            "x-bt/img-status"
#define BT_BIP_HDR_TYPE_PUT_IMAGE             "x-bt/img-img"
#define BT_BIP_HDR_TYPE_PUT_LINKED_THUMBNAIL  "x-bt/img-thm"
#define BT_BIP_HDR_TYPE_PUT_LINKED_ATTACHMENT "x-bt/img-attachment"
#define BT_BIP_HDR_TYPE_REMOTE_DISPLAY        "x-bt/img-display"
#define BT_BIP_HDR_TYPE_DELETE_IMAGE          "x-bt/img-img"
#define BT_BIP_HDR_TYPE_START_PRINT           "x-bt/img-print"
#define BT_BIP_HDR_TYPE_START_ARCHIVE         "x-bt/img-archive"

#define BT_BIP_HEADER_ID_IMG_DESC 0x71

#define BT_BIP_HEADER_ID_IMG_HANDLE 0x30

enum bt_bip_appl_param_tag_id {
        BT_BIP_APPL_PARAM_TAG_ID_RETURNED_HANDLES = 0x01,
        BT_BIP_APPL_PARAM_TAG_ID_LIST_START_OFFSET = 0x02,
        BT_BIP_APPL_PARAM_TAG_ID_LATEST_CAPTURED_IMAGES = 0x03,
        BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_LEN = 0x04,
        BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_START_OFFSET = 0x05,
        BT_BIP_APPL_PARAM_TAG_ID_TOTAL_FILE_SIZE = 0x06,
        BT_BIP_APPL_PARAM_TAG_ID_END_FLAG = 0x07,
        BT_BIP_APPL_PARAM_TAG_ID_REMOTE_DISPLAY = 0x08,
        BT_BIP_APPL_PARAM_TAG_ID_SERVICE_ID = 0x09,
        BT_BIP_APPL_PARAM_TAG_ID_STORE_FLAG = 0x0a,
};

struct bt_bip;

struct bt_bip_transport_ops {
        void (*connected)(struct bt_conn *conn, struct bt_bip *bip);

        void (*disconnected)(struct bt_bip *bip);
};

struct bt_bip_rfcomm_server {
        struct bt_goep_transport_rfcomm_server server;

        int (*accept)(struct bt_conn *conn, struct bt_bip_rfcomm_server *server,
                      struct bt_bip **bip);
};

int bt_bip_rfcomm_register(struct bt_bip_rfcomm_server *server);

int bt_bip_rfcomm_connect(struct bt_conn *conn, struct bt_bip *bip, uint8_t channel);

int bt_bip_rfcomm_disconnect(struct bt_bip *bip);

struct bt_bip_l2cap_server {
        struct bt_goep_transport_l2cap_server server;

        int (*accept)(struct bt_conn *conn, struct bt_bip_l2cap_server *server,
                      struct bt_bip **bip);
};

int bt_bip_l2cap_register(struct bt_bip_l2cap_server *server);

int bt_bip_l2cap_connect(struct bt_conn *conn, struct bt_bip *bip, uint16_t psm);

int bt_bip_l2cap_disconnect(struct bt_bip *bip);

enum __packed bt_bip_conn_type {
        BT_BIP_PRIM_CONN_TYPE_IMAGE_PUSH = 0,
        BT_BIP_PRIM_CONN_TYPE_IMAGE_PULL = 1,
        BT_BIP_PRIM_CONN_TYPE_ADVANCED_IMAGE_PRINTING = 2,
        BT_BIP_PRIM_CONN_TYPE_AUTO_ARCHIVE = 3,
        BT_BIP_PRIM_CONN_TYPE_REMOTE_CAMERA = 4,
        BT_BIP_PRIM_CONN_TYPE_REMOTE_DISPLAY = 5,
        BT_BIP_2ND_CONN_TYPE_REFERENCED_OBJECTS = 10,
        BT_BIP_2ND_CONN_TYPE_ARCHIVED_OBJECTS = 11,
};

enum __packed bt_bip_role {
        BT_BIP_ROLE_UNKNOWN = 0,
        BT_BIP_ROLE_INITIATOR = 1,
        BT_BIP_ROLE_RESPONDER = 2,
};

enum __packed bt_bip_transport_state {
        BT_BIP_TRANSPORT_STATE_DISCONNECTED = 0,
        BT_BIP_TRANSPORT_STATE_CONNECTING = 1,
        BT_BIP_TRANSPORT_STATE_CONNECTED = 2,
        BT_BIP_TRANSPORT_STATE_DISCONNECTING = 3,
};

enum __packed bt_bip_supported_capabilities {
        BT_BIP_SUPP_CAP_GENERIC_IMAGE = 0,
        BT_BIP_SUPP_CAP_CAPTURING = 1,
        BT_BIP_SUPP_CAP_PRINTING = 2,
        BT_BIP_SUPP_CAP_DISPLAYING = 3,
};

enum __packed bt_bip_supported_features {
        BT_BIP_SUPP_FEAT_IMAGE_PUSH = 0,
        BT_BIP_SUPP_FEAT_IMAGE_PUSH_STORE = 1,
        BT_BIP_SUPP_FEAT_IMAGE_PUSH_PRINT = 2,
        BT_BIP_SUPP_FEAT_IMAGE_PUSH_DISPLAY = 3,
        BT_BIP_SUPP_FEAT_IMAGE_PULL = 4,
        BT_BIP_SUPP_FEAT_ADVANCED_IMAGE_PRINT = 5,
        BT_BIP_SUPP_FEAT_AUTO_ARCHIVE = 6,
        BT_BIP_SUPP_FEAT_REMOTE_CAMERA = 7,
        BT_BIP_SUPP_FEAT_REMOTE_DISPLAY = 8,
};

enum __packed bt_bip_supported_functions {
        BT_BIP_SUPP_FUNC_GET_CAPS = 0,
        BT_BIP_SUPP_FUNC_PUT_IMAGE = 1,
        BT_BIP_SUPP_FUNC_PUT_LINKED_ATTACHMENT = 2,
        BT_BIP_SUPP_FUNC_PUT_LINKED_THUMBNAIL = 3,
        BT_BIP_SUPP_FUNC_REMOTE_DISPLAY = 4,
        BT_BIP_SUPP_FUNC_GET_IMAGE_LIST = 5,
        BT_BIP_SUPP_FUNC_GET_IMAGE_PROPERTIES = 6,
        BT_BIP_SUPP_FUNC_GET_IMAGE = 7,
        BT_BIP_SUPP_FUNC_GET_LINKED_THUMBNAIL = 8,
        BT_BIP_SUPP_FUNC_GET_LINKED_ATTACHMENT = 9,
        BT_BIP_SUPP_FUNC_DELETE_IMAGE = 10,
        BT_BIP_SUPP_FUNC_START_PRINT = 11,
        BT_BIP_SUPP_FUNC_GET_PARTIAL_IMAGE = 12,
        BT_BIP_SUPP_FUNC_START_ARCHIVE = 13,
        BT_BIP_SUPP_FUNC_GET_MONITORING_IMAGE = 14,
        BT_BIP_SUPP_FUNC_GET_STATUS = 16,
};

struct bt_bip {
        struct bt_goep_transport goep_transport;

        struct bt_goep goep;

        enum bt_bip_role role;

        const struct bt_bip_transport_ops *ops;

        atomic_t _transport_state;

        uint8_t _supp_caps;

        uint16_t _supp_feats;

        uint32_t _supp_funcs;

        sys_slist_t _clients;

        sys_slist_t _servers;

        sys_snode_t _node;
};

int bt_bip_set_supported_capabilities(struct bt_bip *bip, uint8_t capabilities);

int bt_bip_set_supported_features(struct bt_bip *bip, uint16_t features);

int bt_bip_set_supported_functions(struct bt_bip *bip, uint32_t functions);

enum __packed bt_bip_state {
        BT_BIP_STATE_DISCONNECTED = 0,
        BT_BIP_STATE_CONNECTING = 1,
        BT_BIP_STATE_CONNECTED = 2,
        BT_BIP_STATE_DISCONNECTING = 3,
};

struct bt_bip_server;

struct bt_bip_server_cb {
        void (*connect)(struct bt_bip_server *server, uint8_t version, uint16_t mopl,
                        struct net_buf *buf);

        void (*disconnect)(struct bt_bip_server *server, struct net_buf *buf);

        void (*abort)(struct bt_bip_server *server, struct net_buf *buf);

        void (*get_caps)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*get_image_list)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*get_image_properties)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*get_image)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*get_linked_thumbnail)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*get_linked_attachment)(struct bt_bip_server *server, bool final,
                                      struct net_buf *buf);

        void (*get_partial_image)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*get_monitoring_image)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*get_status)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*put_image)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*put_linked_thumbnail)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*put_linked_attachment)(struct bt_bip_server *server, bool final,
                                      struct net_buf *buf);

        void (*remote_display)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*delete_image)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*start_print)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        void (*start_archive)(struct bt_bip_server *server, bool final, struct net_buf *buf);
};

struct bt_bip_client;

struct bt_bip_client_cb {
        void (*connect)(struct bt_bip_client *client, uint8_t rsp_code, uint8_t version,
                        uint16_t mopl, struct net_buf *buf);

        void (*disconnect)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*abort)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*get_caps)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*get_image_list)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*get_image_properties)(struct bt_bip_client *client, uint8_t rsp_code,
                                     struct net_buf *buf);

        void (*get_image)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*get_linked_thumbnail)(struct bt_bip_client *client, uint8_t rsp_code,
                                     struct net_buf *buf);

        void (*get_linked_attachment)(struct bt_bip_client *client, uint8_t rsp_code,
                                      struct net_buf *buf);

        void (*get_partial_image)(struct bt_bip_client *client, uint8_t rsp_code,
                                  struct net_buf *buf);

        void (*get_monitoring_image)(struct bt_bip_client *client, uint8_t rsp_code,
                                     struct net_buf *buf);

        void (*get_status)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*put_image)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*put_linked_thumbnail)(struct bt_bip_client *client, uint8_t rsp_code,
                                     struct net_buf *buf);

        void (*put_linked_attachment)(struct bt_bip_client *client, uint8_t rsp_code,
                                      struct net_buf *buf);

        void (*remote_display)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*delete_image)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*start_print)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*start_archive)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);
};

struct bt_bip_server {
        const struct bt_bip_server_cb *_cb;

        struct bt_bip *_bip;

        const struct bt_uuid_128 *_uuid;

        uint32_t _conn_id;

        enum bt_bip_conn_type _type;

        struct bt_obex_server _server;

        uint8_t _opcode;
        const char *_optype;

        atomic_t _state;

        union {
                struct bt_bip_client *_primary_client;
                struct bt_bip_client *_secondary_client;
        };

        void (*_req_cb)(struct bt_bip_server *server, bool final, struct net_buf *buf);

        sys_snode_t _node;
};

struct bt_bip_client {
        const struct bt_bip_client_cb *_cb;

        struct bt_bip *_bip;

        struct bt_uuid_128 _uuid;

        uint32_t _conn_id;

        enum bt_bip_conn_type _type;

        struct bt_obex_client _client;

        atomic_t _state;

        union {
                struct bt_bip_server *_primary_server;
                struct bt_bip_server *_secondary_server;
        };

        void (*_rsp_cb)(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf);

        const char *_req_type;

        sys_snode_t _node;
};

#define BT_BIP_PRIM_IMAGE_PUSH_CB(_connect, _disconnect, _get_caps, _put_image,                    \
                                  _put_linked_thumbnail, _put_linked_attachment)                   \
        {                                                                                          \
                .connect = _connect, .disconnect = _disconnect, .get_caps = _get_caps,             \
                .put_image = _put_image, .put_linked_thumbnail = _put_linked_thumbnail,            \
                .put_linked_attachment = _put_linked_attachment,                                   \
        }

#define BT_BIP_PRIM_IMAGE_PULL_CB(_connect, _disconnect, _get_caps, _get_image_list,               \
                                  _get_image_properties, _get_image, _get_linked_thumbnail,        \
                                  _get_linked_attachment, _delete_image)                           \
        {                                                                                          \
                .connect = _connect, .disconnect = _disconnect, .get_caps = _get_caps,             \
                .get_image_list = _get_image_list, .get_image_properties = _get_image_properties,  \
                .get_image = _get_image, .get_linked_thumbnail = _get_linked_thumbnail,            \
                .get_linked_attachment = _get_linked_attachment, .delete_image = _delete_image,    \
        }

#define BT_BIP_PRIM_IMAGE_PRINT_CB(_connect, _disconnect, _get_caps, _get_status, _start_print)    \
        {                                                                                          \
                .connect = _connect, .disconnect = _disconnect, .get_caps = _get_caps,             \
                .get_status = _get_status, .start_print = _start_print,                            \
        }

#define BT_BIP_2ND_IMAGE_PRINT_CB(_connect, _disconnect, _get_partial_image)                       \
        {                                                                                          \
                .connect = _connect, .disconnect = _disconnect,                                    \
                .get_partial_image = _get_partial_image,                                           \
        }

#define BT_BIP_PRIM_AUTO_ARCHIVE_CB(_connect, _disconnect, _get_status, _start_archive)            \
        {                                                                                          \
                .connect = _connect, .disconnect = _disconnect, .get_status = _get_status,         \
                .start_archive = _start_archive,                                                   \
        }

#define BT_BIP_2ND_AUTO_ARCHIVE_CB(_connect, _disconnect, _get_caps, _get_image_list,              \
                                   _get_image_properties, _get_image, _get_linked_thumbnail,       \
                                   _get_linked_attachment, _delete_image)                          \
        {                                                                                          \
                .connect = _connect, .disconnect = _disconnect, .get_caps = _get_caps,             \
                .get_image_list = _get_image_list, .get_image_properties = _get_image_properties,  \
                .get_image = _get_image, .get_linked_thumbnail = _get_linked_thumbnail,            \
                .get_linked_attachment = _get_linked_attachment, .delete_image = _delete_image,    \
        }

#define BT_BIP_PRIM_REMOTE_CAMERA_CB(_connect, _disconnect, _get_image_properties, _get_image,     \
                                     _get_linked_thumbnail, _get_monitoring_image)                 \
        {                                                                                          \
                .connect = _connect, .disconnect = _disconnect,                                    \
                .get_image_properties = _get_image_properties, .get_image = _get_image,            \
                .get_linked_thumbnail = _get_linked_thumbnail,                                     \
                .get_monitoring_image = _get_monitoring_image,                                     \
        }

#define BT_BIP_PRIM_REMOTE_DISPLAY_CB(_connect, _disconnect, _get_caps, _get_image_list,           \
                                      _put_image, _put_linked_thumbnail, _remote_display)          \
        {                                                                                          \
                .connect = _connect, .disconnect = _disconnect, .get_caps = _get_caps,             \
                .get_image_list = _get_image_list, .put_image = _put_image,                        \
                .put_linked_thumbnail = _put_linked_thumbnail, .remote_display = _remote_display,  \
        }

#define BT_BIP_UUID_IMAGE_PUSH                                                                     \
        (const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
                BT_UUID_128_ENCODE(0xE33D9545, 0x8374, 0x4AD7, 0x9EC5, 0xC16BE31EDE8E))

#define BT_BIP_UUID_IMAGE_PULL                                                                     \
        (const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
                BT_UUID_128_ENCODE(0x8EE9B3D0, 0x4608, 0x11D5, 0x841A, 0x0002A5325B4E))

#define BT_BIP_UUID_IMAGE_PRINT                                                                    \
        (const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
                BT_UUID_128_ENCODE(0x92353350, 0x4608, 0x11D5, 0x841A, 0x0002A5325B4E))

#define BT_BIP_UUID_AUTO_ARCHIVE                                                                   \
        (const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
                BT_UUID_128_ENCODE(0x940126C0, 0x4608, 0x11D5, 0x841A, 0x0002A5325B4E))

#define BT_BIP_UUID_REMOTE_CAMERA                                                                  \
        (const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
                BT_UUID_128_ENCODE(0x947E7420, 0x4608, 0x11D5, 0x841A, 0x0002A5325B4E))

#define BT_BIP_UUID_REMOTE_DISPLAY                                                                 \
        (const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
                BT_UUID_128_ENCODE(0x94C7CD20, 0x4608, 0x11D5, 0x841A, 0x0002A5325B4E))

#define BT_BIP_UUID_REFERENCED_OBJ                                                                 \
        (const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
                BT_UUID_128_ENCODE(0x8E61F95D, 0x1A79, 0x11D4, 0x8EA4, 0x00805F9B9834))

#define BT_BIP_UUID_ARCHIVED_OBJ                                                                   \
        (const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
                BT_UUID_128_ENCODE(0x8E61F95E, 0x1A79, 0x11D4, 0x8EA4, 0x00805F9B9834))

int bt_bip_primary_server_register(struct bt_bip *bip, struct bt_bip_server *server,
                                   enum bt_bip_conn_type type, const struct bt_uuid_128 *uuid,
                                   struct bt_bip_server_cb *cb);

int bt_bip_secondary_server_register(struct bt_bip *bip, struct bt_bip_server *server,
                                     enum bt_bip_conn_type type, const struct bt_uuid_128 *uuid,
                                     struct bt_bip_server_cb *cb,
                                     struct bt_bip_client *primary_client);

static inline int bt_bip_primary_image_push_server_register(struct bt_bip *bip,
                                                            struct bt_bip_server *server,
                                                            const struct bt_uuid_128 *uuid,
                                                            struct bt_bip_server_cb *cb)
{
        return bt_bip_primary_server_register(bip, server, BT_BIP_PRIM_CONN_TYPE_IMAGE_PUSH, uuid,
                                              cb);
}

static inline int bt_bip_primary_image_pull_server_register(struct bt_bip *bip,
                                                            struct bt_bip_server *server,
                                                            const struct bt_uuid_128 *uuid,
                                                            struct bt_bip_server_cb *cb)
{
        return bt_bip_primary_server_register(bip, server, BT_BIP_PRIM_CONN_TYPE_IMAGE_PULL, uuid,
                                              cb);
}

static inline int bt_bip_primary_advanced_image_printing_server_register(
        struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid,
        struct bt_bip_server_cb *cb)
{
        return bt_bip_primary_server_register(
                bip, server, BT_BIP_PRIM_CONN_TYPE_ADVANCED_IMAGE_PRINTING, uuid, cb);
}

static inline int bt_bip_primary_auto_archive_server_register(struct bt_bip *bip,
                                                              struct bt_bip_server *server,
                                                              const struct bt_uuid_128 *uuid,
                                                              struct bt_bip_server_cb *cb)
{
        return bt_bip_primary_server_register(bip, server, BT_BIP_PRIM_CONN_TYPE_AUTO_ARCHIVE, uuid,
                                              cb);
}

static inline int bt_bip_primary_remote_camera_server_register(struct bt_bip *bip,
                                                               struct bt_bip_server *server,
                                                               const struct bt_uuid_128 *uuid,
                                                               struct bt_bip_server_cb *cb)
{
        return bt_bip_primary_server_register(bip, server, BT_BIP_PRIM_CONN_TYPE_REMOTE_CAMERA,
                                              uuid, cb);
}

static inline int bt_bip_primary_remote_display_server_register(struct bt_bip *bip,
                                                                struct bt_bip_server *server,
                                                                const struct bt_uuid_128 *uuid,
                                                                struct bt_bip_server_cb *cb)
{
        return bt_bip_primary_server_register(bip, server, BT_BIP_PRIM_CONN_TYPE_REMOTE_DISPLAY,
                                              uuid, cb);
}

static inline int bt_bip_secondary_advanced_image_printing_server_register(
        struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid,
        struct bt_bip_server_cb *cb, struct bt_bip_client *primary_client)
{
        return bt_bip_secondary_server_register(
                bip, server, BT_BIP_2ND_CONN_TYPE_REFERENCED_OBJECTS, uuid, cb, primary_client);
}

static inline int bt_bip_secondary_auto_archive_server_register(
        struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid,
        struct bt_bip_server_cb *cb, struct bt_bip_client *primary_client)
{
        return bt_bip_secondary_server_register(bip, server, BT_BIP_2ND_CONN_TYPE_ARCHIVED_OBJECTS,
                                                uuid, cb, primary_client);
}

int bt_bip_server_unregister(struct bt_bip_server *server);

int bt_bip_primary_client_connect(struct bt_bip *bip, struct bt_bip_client *client,
                                  enum bt_bip_conn_type type, struct bt_bip_client_cb *cb,
                                  struct net_buf *buf);

int bt_bip_secondary_client_connect(struct bt_bip *bip, struct bt_bip_client *client,
                                    enum bt_bip_conn_type type, struct bt_bip_client_cb *cb,
                                    struct net_buf *buf, struct bt_bip_server *primary_server);

static inline int bt_bip_primary_image_push_client_connect(struct bt_bip *bip,
                                                           struct bt_bip_client *client,
                                                           struct bt_bip_client_cb *cb,
                                                           struct net_buf *buf)
{
        return bt_bip_primary_client_connect(bip, client, BT_BIP_PRIM_CONN_TYPE_IMAGE_PUSH, cb,
                                             buf);
}

static inline int bt_bip_primary_image_pull_client_connect(struct bt_bip *bip,
                                                           struct bt_bip_client *client,
                                                           struct bt_bip_client_cb *cb,
                                                           struct net_buf *buf)
{
        return bt_bip_primary_client_connect(bip, client, BT_BIP_PRIM_CONN_TYPE_IMAGE_PULL, cb,
                                             buf);
}

static inline int bt_bip_primary_advanced_image_printing_client_connect(
        struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb,
        struct net_buf *buf)
{
        return bt_bip_primary_client_connect(
                bip, client, BT_BIP_PRIM_CONN_TYPE_ADVANCED_IMAGE_PRINTING, cb, buf);
}

static inline int bt_bip_primary_auto_archive_client_connect(struct bt_bip *bip,
                                                             struct bt_bip_client *client,
                                                             struct bt_bip_client_cb *cb,
                                                             struct net_buf *buf)
{
        return bt_bip_primary_client_connect(bip, client, BT_BIP_PRIM_CONN_TYPE_AUTO_ARCHIVE, cb,
                                             buf);
}

static inline int bt_bip_primary_remote_camera_client_connect(struct bt_bip *bip,
                                                              struct bt_bip_client *client,
                                                              struct bt_bip_client_cb *cb,
                                                              struct net_buf *buf)
{
        return bt_bip_primary_client_connect(bip, client, BT_BIP_PRIM_CONN_TYPE_REMOTE_CAMERA, cb,
                                             buf);
}

static inline int bt_bip_primary_remote_display_client_connect(struct bt_bip *bip,
                                                               struct bt_bip_client *client,
                                                               struct bt_bip_client_cb *cb,
                                                               struct net_buf *buf)
{
        return bt_bip_primary_client_connect(bip, client, BT_BIP_PRIM_CONN_TYPE_REMOTE_DISPLAY, cb,
                                             buf);
}

static inline int bt_bip_secondary_advanced_image_printing_client_connect(
        struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb,
        struct net_buf *buf, struct bt_bip_server *primary_server)
{
        return bt_bip_secondary_client_connect(bip, client, BT_BIP_2ND_CONN_TYPE_REFERENCED_OBJECTS,
                                               cb, buf, primary_server);
}

static inline int bt_bip_secondary_auto_archive_client_connect(struct bt_bip *bip,
                                                               struct bt_bip_client *client,
                                                               struct bt_bip_client_cb *cb,
                                                               struct net_buf *buf,
                                                               struct bt_bip_server *primary_server)
{
        return bt_bip_secondary_client_connect(bip, client, BT_BIP_2ND_CONN_TYPE_ARCHIVED_OBJECTS,
                                               cb, buf, primary_server);
}

int bt_bip_connect_rsp(struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_bip_disconnect(struct bt_bip_client *client, struct net_buf *buf);

int bt_bip_disconnect_rsp(struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_bip_abort(struct bt_bip_client *client, struct net_buf *buf);

int bt_bip_abort_rsp(struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_bip_get_capabilities(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_get_capabilities_rsp(struct bt_bip_server *server, uint8_t rsp_code,
                                struct net_buf *buf);

int bt_bip_get_image_list(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_get_image_list_rsp(struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_bip_get_image_properties(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_get_image_properties_rsp(struct bt_bip_server *server, uint8_t rsp_code,
                                    struct net_buf *buf);

int bt_bip_get_image(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_get_image_rsp(struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_bip_get_linked_thumbnail(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_get_linked_thumbnail_rsp(struct bt_bip_server *server, uint8_t rsp_code,
                                    struct net_buf *buf);

int bt_bip_get_linked_attachment(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_get_linked_attachment_rsp(struct bt_bip_server *server, uint8_t rsp_code,
                                     struct net_buf *buf);

int bt_bip_get_partial_image(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_get_partial_image_rsp(struct bt_bip_server *server, uint8_t rsp_code,
                                 struct net_buf *buf);

int bt_bip_get_monitoring_image(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_get_monitoring_image_rsp(struct bt_bip_server *server, uint8_t rsp_code,
                                    struct net_buf *buf);

int bt_bip_get_status(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_get_status_rsp(struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_bip_put_image(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_put_image_rsp(struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_bip_put_linked_thumbnail(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_put_linked_thumbnail_rsp(struct bt_bip_server *server, uint8_t rsp_code,
                                    struct net_buf *buf);

int bt_bip_put_linked_attachment(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_put_linked_attachment_rsp(struct bt_bip_server *server, uint8_t rsp_code,
                                     struct net_buf *buf);

int bt_bip_remote_display(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_remote_display_rsp(struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_bip_delete_image(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_delete_image_rsp(struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_bip_start_print(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_start_print_rsp(struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_bip_start_archive(struct bt_bip_client *client, bool final, struct net_buf *buf);

int bt_bip_start_archive_rsp(struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_bip_add_header_image_desc(struct net_buf *buf, uint16_t len, const uint8_t *desc);

int bt_bip_add_header_image_handle(struct net_buf *buf, uint16_t len, const uint8_t *handle);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_BIP_H_ */
```

## 19.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`bip.h`：蓝牙基本成像配置文件（Basic Imaging Profile）的处理。

### 注释 2：原第 3 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 2075 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_BIP_H_`。

## 19.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)
- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html)
- [bt_bip_appl_param_tag_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga34de6d20263274292543a7a8afbd2c6b)
- [BT_BIP_APPL_PARAM_TAG_ID_RETURNED_HANDLES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6bace4966644e9194273b635b916eac0871)
- [BT_BIP_APPL_PARAM_TAG_ID_LIST_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba0f0d78c2da3d8f3d0caf015525b3e010)
- [BT_BIP_APPL_PARAM_TAG_ID_LATEST_CAPTURED_IMAGES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba9dbbb8ed95c7ccd86a74263fef1a1e92)
- [BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6bad6511bb04da2cf325a39bfee93f51e0c)
- [BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba0ff60914fb36e587b42a473c25bd6a2d)
- [BT_BIP_APPL_PARAM_TAG_ID_TOTAL_FILE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba2565f26c0322935acef85725ac8982e5)
- [BT_BIP_APPL_PARAM_TAG_ID_END_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6baa7b18ee3ae56c0f0e84a103c1e59f05d)
- [BT_BIP_APPL_PARAM_TAG_ID_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6bab0e2dfb17de25f4ec3b27b29c2659afa)
- [BT_BIP_APPL_PARAM_TAG_ID_SERVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba683d101ea1babf1f147d1869ab7424f4)
- [BT_BIP_APPL_PARAM_TAG_ID_STORE_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6baef58e631bfd6c511318c386308374274)
- [bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)
- [bt_bip_transport_ops](../bluetooth_service_model_reference/P008_bt_bip_transport_ops_结构体.md)
- [connected](../bluetooth_service_model_reference/P008_bt_bip_transport_ops_结构体.md#a80a1596a382b93366e13a857a5edf3ba)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [disconnected](../bluetooth_service_model_reference/P008_bt_bip_transport_ops_结构体.md#a49f1708ed03ebe8cfb6a2f11b76bda73)
- [bt_bip_rfcomm_server](../bluetooth_service_model_reference/P005_bt_bip_rfcomm_server_结构体.md)
- [bt_goep_transport_rfcomm_server](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md)
- [server](../bluetooth_service_model_reference/P005_bt_bip_rfcomm_server_结构体.md#a40ec65e156c02ad06b55aa1fc594ca71)
- [accept](../bluetooth_service_model_reference/P005_bt_bip_rfcomm_server_结构体.md#ad7b714b584c18e41feb7385819c50511)
- [bt_bip_rfcomm_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga644ca479c156b10d920d87d862401fc7)
- [bt_bip_rfcomm_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5ed2a46482e4fe60ef23c540001b58a3)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_bip_rfcomm_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga66a86a399f73dba932dc05d63b3749bd)
- [bt_bip_l2cap_server](../bluetooth_service_model_reference/P004_bt_bip_l2cap_server_结构体.md)
- [bt_goep_transport_l2cap_server](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md)
- [server](../bluetooth_service_model_reference/P004_bt_bip_l2cap_server_结构体.md#a830f0f266401a3e95c21e5fbb25bc057)
- [accept](../bluetooth_service_model_reference/P004_bt_bip_l2cap_server_结构体.md#aeb027a550bef264ef287e25cc3d9ffa9)
- [bt_bip_l2cap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaffb77f6c80ba05046df03d62baad211b)
- [bt_bip_l2cap_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf54b07acf22c5231b2de0fdeca7807c2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_bip_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga1fda174189b57c54f365784d1909152e)
- [bt_bip_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaff38654d69104bebaaf5884283e197ef)
- [BT_BIP_PRIM_CONN_TYPE_IMAGE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa612cd818200f49e37235917fead216d2)
- [BT_BIP_PRIM_CONN_TYPE_IMAGE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa05372dbd0a01855f0863ce355a503c61)
- [BT_BIP_PRIM_CONN_TYPE_ADVANCED_IMAGE_PRINTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa05de3a972070aa4d1e29851479860d9f)
- [BT_BIP_PRIM_CONN_TYPE_AUTO_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efaf762949693b7cf70739ed0a0eb6a9d58)
- [BT_BIP_PRIM_CONN_TYPE_REMOTE_CAMERA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa8b576c667b9c6458e44ec67674bdffbd)
- [BT_BIP_PRIM_CONN_TYPE_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa12873fc1888cd99703131ae71134f0c7)
- [BT_BIP_2ND_CONN_TYPE_REFERENCED_OBJECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa4d5ab575c877aa2a43c29cbb52a361c7)
- [BT_BIP_2ND_CONN_TYPE_ARCHIVED_OBJECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efabe15f984d6907bdb40c10e893e1c3bf6)
- [bt_bip_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga30d9309cbbd88b54508551285b21e575)
- [BT_BIP_ROLE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga30d9309cbbd88b54508551285b21e575aaa7de8d668d248049c5d5c75ae35d74b)
- [BT_BIP_ROLE_INITIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga30d9309cbbd88b54508551285b21e575aa5cdb11f2b0ac9c20c380dd48c9edaa5)
- [BT_BIP_ROLE_RESPONDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga30d9309cbbd88b54508551285b21e575a87d1fe99824b216780435898c2dfa968)
- [bt_bip_transport_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga7b3c6cb1159e7b2ede57c66f20b23827)
- [BT_BIP_TRANSPORT_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827ae78c865c0034d405391aaf9f72e4c9b2)
- [BT_BIP_TRANSPORT_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827ad4444da19b4e0f499867ea967dfc578f)
- [BT_BIP_TRANSPORT_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827a1af8a1481b10b53c58af8e36c7b91588)
- [BT_BIP_TRANSPORT_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827a7340b2e209c71d9f944b303c22cb264d)
- [bt_bip_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad062c0f3d2feeb92a866f0fe91a6f231)
- [BT_BIP_SUPP_CAP_GENERIC_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231a786ef1ad1bde68f9b026c9d080cc41d4)
- [BT_BIP_SUPP_CAP_CAPTURING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231ac9c5d73b0d2d5eb25a962fa72ede6d5a)
- [BT_BIP_SUPP_CAP_PRINTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231a4a738d195dcf0908a64bdd246672d4bb)
- [BT_BIP_SUPP_CAP_DISPLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231a324c0590cefb5d7a39f90d90e3466334)
- [bt_bip_supported_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gacfc8aaea3d27e3a42a14c49b880a5b90)
- [BT_BIP_SUPP_FEAT_IMAGE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90ac14657fd4af96f4c837916b832c25a0f)
- [BT_BIP_SUPP_FEAT_IMAGE_PUSH_STORE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a8904b7b8288e1b47d2242f5d686e32d9)
- [BT_BIP_SUPP_FEAT_IMAGE_PUSH_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90add6c2e70541aae8124bad4b102d64b88)
- [BT_BIP_SUPP_FEAT_IMAGE_PUSH_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a49668a596059e535bd59ac095dffa050)
- [BT_BIP_SUPP_FEAT_IMAGE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90aba576edd916dbf49118e78572f70320b)
- [BT_BIP_SUPP_FEAT_ADVANCED_IMAGE_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90ac64d953311bc9b76bfe75dd3133f5563)
- [BT_BIP_SUPP_FEAT_AUTO_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90af72e05ca427f8c5091e50cddac522045)
- [BT_BIP_SUPP_FEAT_REMOTE_CAMERA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a97141e2764fad3714c03b6be69ff2a9a)
- [BT_BIP_SUPP_FEAT_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a132dd77e79fbfda8a78d5034d4c618c5)
- [bt_bip_supported_functions](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga6768e59b79bb67b5d385fdaa3dfb8888)
- [BT_BIP_SUPP_FUNC_GET_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a2e1f3364145560587963402881bb2705)
- [BT_BIP_SUPP_FUNC_PUT_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888afb1777cefdbd00e3432ddf5180804f48)
- [BT_BIP_SUPP_FUNC_PUT_LINKED_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a8a417f3073f017af866877f88ee10228)
- [BT_BIP_SUPP_FUNC_PUT_LINKED_THUMBNAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a0ee047481a35e26fa0d03bf7594d7752)
- [BT_BIP_SUPP_FUNC_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888adb0e03118b1cd62fe7e97b53e9f52d41)
- [BT_BIP_SUPP_FUNC_GET_IMAGE_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a7843f4dece6ff449b97ba0a2c7298b90)
- [BT_BIP_SUPP_FUNC_GET_IMAGE_PROPERTIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888af29095b3b5964062e98b9e357de87f89)
- [BT_BIP_SUPP_FUNC_GET_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a50271c1bac792020f0fb869bb523e506)
- [BT_BIP_SUPP_FUNC_GET_LINKED_THUMBNAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a03c928dd502a98b72cb7d8eebad4b384)
- [BT_BIP_SUPP_FUNC_GET_LINKED_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888ac3ec252a63d494ce3e4dd696d05d94bc)
- [BT_BIP_SUPP_FUNC_DELETE_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a045dfb07426eacb16fd69247eecf70b1)
- [BT_BIP_SUPP_FUNC_START_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888ae1312bb3417f901204ac592e4b9376df)
- [BT_BIP_SUPP_FUNC_GET_PARTIAL_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888ae1e97efb19d10ac2b508a9e65b5c43ce)
- [BT_BIP_SUPP_FUNC_START_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a3cae66cb380311938f83bb099a2d02da)
- [BT_BIP_SUPP_FUNC_GET_MONITORING_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a0bde5efd58b339e53db3779a159239c1)
- [BT_BIP_SUPP_FUNC_GET_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888abf825fb7d634906f0204780ef81ca5b3)
- [bt_goep_transport](../bluetooth_service_model_reference/P071_bt_goep_transport_结构体.md)
- [goep_transport](../bluetooth_service_model_reference/P001_bt_bip_结构体.md#a245296151dcf59b69822e3122488c2c2)
- [bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)
- [goep](../bluetooth_service_model_reference/P001_bt_bip_结构体.md#adba3573d8d8250c015cb5adca9bd77bb)
- [role](../bluetooth_service_model_reference/P001_bt_bip_结构体.md#a9cee12abb9b8efadb1b7c3e21803f349)
- [ops](../bluetooth_service_model_reference/P001_bt_bip_结构体.md#ac5b8a3fd23216a0894a47ac487835bc0)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_bip_set_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga0180461f24c6f741e056d64f9758b89e)
- [bt_bip_set_supported_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gab5a80d7a992d0afa0270eb09d6f3275c)
- [bt_bip_set_supported_functions](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gafe7df6ee236da3a11104f1aa6e948bfe)
- [bt_bip_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae4d1ed3b7e27768c1dbb6ce448cb5cf9)
- [BT_BIP_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a984245e44981ad3d85518ab1c3f576e8)
- [BT_BIP_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9acdc7fe9ee4c0d0ba447bc43817364478)
- [BT_BIP_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9ae65c7b972effa225116ec8abfcf07bc3)
- [BT_BIP_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a96f12788ce6f56012ac4b1c25f63f67e)
- [bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)
- [bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)
- [connect](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a094c1d805d9e099cacb9b91315c799e7)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [disconnect](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#aefa142e33e50b8d23f89c732fd79a125)
- [abort](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a877caeb43927ab27b360cd27b628b683)
- [get_caps](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a6c93a136a7677aa05928e762415af2de)
- [get_image_list](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#ad2630977d48b11da5c70762f4e6cb49e)
- [get_image_properties](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#af41d62e8ff812c9ace9a5c916c08314d)
- [get_image](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a27710e3871c031d4d787dc6f2223e71d)
- [get_linked_thumbnail](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#afc3ba204dd51bdc758cf3a6da9d72185)
- [get_linked_attachment](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#ac38d13107bbd18400690196efeddb228)
- [get_partial_image](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a755b097ab450d312a3e29f5b1a75dadf)
- [get_monitoring_image](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a904935d6a327b9eba0ea68e924d8c1c5)
- [get_status](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a40c07a467ff5573400cc10ba58ee54f2)
- [put_image](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a7b0c02fd0c1546e730df162b14db745b)
- [put_linked_thumbnail](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a4c8bf0f0791766e8c547ea10630e0948)
- [put_linked_attachment](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a48d411ddb30784a729204080420c203d)
- [remote_display](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a81f786528f0db0afc54f7518f3765df0)
- [delete_image](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a0f8052f0ee8a4e5130b538e25231fc1b)
- [start_print](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a6ca521f03e917b7354eaefac20b5b33f)
- [start_archive](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a6514602bea0d066abdf41d6f021d4d51)
- [bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)
- [bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)
- [connect](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#afd9b65b4810a31a8bd48502fcf11eff1)
- [disconnect](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a00575e54960da7eadb6c97603c15db76)
- [abort](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#aaedbc7f33eba36d176360c4806a3a27e)
- [get_caps](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a3f6e8efdbdee62d23532bff52850ddb3)
- [get_image_list](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#acda8a5a4ae315bf1b65209df9ff6b8e4)
- [get_image_properties](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a16aea4cd3428723afee39332f6112c3e)
- [get_image](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#aa551eac8ba777bbb7e286e36015a5a72)
- [get_linked_thumbnail](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a9f7713e8e68233c5837edbb46de6c758)
- [get_linked_attachment](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a72937856348fabd76696237a55ced1e9)
- [get_partial_image](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a9efe5d25e239144bb40e05ff6494f20d)
- [get_monitoring_image](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a1085306d4098491363df71e82baab9e3)
- [get_status](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a287c05808d89726d5a3fbe965b29fd52)
- [put_image](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a0fb9d1c1bde99fab9f68997dcce31cca)
- [put_linked_thumbnail](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#aec614697e4e4ccd3dd326ecffc311c9b)
- [put_linked_attachment](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a3aae2299cb0779cf517d40368dc9a97e)
- [remote_display](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a3ead32fbbe46d4ec0e73d0a840dc30b0)
- [delete_image](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a5bb82c50c8e535457c17726e6133b4ef)
- [start_print](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a7228b45ce57155f308d6a9b983074997)
- [start_archive](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a6ad152e72050d05eb8b47ba00237b6c4)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)
- [bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)
- [bt_bip_primary_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga45f1ca2d2874500d6f8df3a62b01260e)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_bip_secondary_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gab0a3b58b041ac4af2682fb96b8f00a7e)
- [bt_bip_primary_image_push_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaefd318b5dc2e813eea2cd7608be1170c)
- [bt_bip_primary_image_pull_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga35c44217cbfcd8661c3f2e5725be9323)
- [bt_bip_primary_advanced_image_printing_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae8b37b224ea419ca1f1761d98a34cb2d)
- [bt_bip_primary_auto_archive_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga3848d86378912fbd9c896b14aed74161)
- [bt_bip_primary_remote_camera_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga4b236a8a28c359e392633d472a508405)
- [bt_bip_primary_remote_display_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5167b2dab89a983fae9fca356e6fbcf9)
- [bt_bip_secondary_advanced_image_printing_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga54c37cced33fa72a2c6cea10e2996e6d)
- [bt_bip_secondary_auto_archive_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gab24c4f7144f8c43dcf1b82a4c33e4ffd)
- [bt_bip_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga4e06b2fb9a99f89d7e65e8a52690442d)
- [bt_bip_primary_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad32c1b1118b606ab3ae0d9db889cbab9)
- [bt_bip_secondary_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae557b198b9d5606ee05cd29ed16f9482)
- [bt_bip_primary_image_push_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga39ec2019f86d42b02992b0a9d3ba094c)
- [bt_bip_primary_image_pull_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga2d4919c1eb568f33a89d8b176f103601)
- [bt_bip_primary_advanced_image_printing_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9352b8309334a3fe89d77f5714443376)
- [bt_bip_primary_auto_archive_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga98dca7b222c8a09b1c44861c9060193b)
- [bt_bip_primary_remote_camera_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga30e3a6ad8c00c230ac3591a934cfb81f)
- [bt_bip_primary_remote_display_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gac4ba5cef40cd451bd4b505dbea0fa135)
- [bt_bip_secondary_advanced_image_printing_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga72ef6cd266b7e57e1c80b6d8eba799e2)
- [bt_bip_secondary_auto_archive_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga1975916aa3da40576499f6d05aac1285)
- [bt_bip_connect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga0987a342b43bdd1926f3730f471ca05f)
- [bt_bip_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaafcd6a3503795299b6fb777ba0aa0cff)
- [bt_bip_disconnect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaddfcee2eaea19b4819d83cf6ecb396da)
- [bt_bip_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaa0f071c8c83a54b2d48f478594579719)
- [bt_bip_abort_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga1c341ad182ff418286b64b4eff491445)
- [bt_bip_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gafcd2d4e6a8ad906c9692313421175431)
- [bt_bip_get_capabilities_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaea5d5f5b6c29a44ae89939ee3e2d6efb)
- [bt_bip_get_image_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9542e030ea863b4379d36fa21de262dc)
- [bt_bip_get_image_list_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga6e33bba952a9693d1fed7ee9bdf03df8)
- [bt_bip_get_image_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga17ae73bd6088b44206378afe3b0b9eb0)
- [bt_bip_get_image_properties_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9a91c35e91a0c30eab55da5b842427d9)
- [bt_bip_get_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga79831fc5fff332a891e6b9ff71f81d20)
- [bt_bip_get_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga53fb15ff7d0728b09f1c4e8d2ceb6dee)
- [bt_bip_get_linked_thumbnail](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad9c05d28e1e2124675b5906990c3408c)
- [bt_bip_get_linked_thumbnail_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5c3cd3e39fc21a584d6955a160ca126a)
- [bt_bip_get_linked_attachment](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad95944f07cd9f7b6bb9c81f21fffd447)
- [bt_bip_get_linked_attachment_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga70bf0d46bd16d0207e13eeb9a7844f1c)
- [bt_bip_get_partial_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga2b6a2a51fb00e7060e196051f8aea4c4)
- [bt_bip_get_partial_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gadf624e05a6d008bdcfd8a61ae6341f42)
- [bt_bip_get_monitoring_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9f1593748ffcf29015533d52266a8e19)
- [bt_bip_get_monitoring_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga301ff6e5a1e8775295659442b8c20e15)
- [bt_bip_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga578c2b59fbc8afee530168452eb221fb)
- [bt_bip_get_status_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga7abdde3a7e5dcda9c6187b5e45b75cc2)
- [bt_bip_put_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf551904672eda53e9dfcbb5a6bf4c2c3)
- [bt_bip_put_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga002f7713a8269c0b00a415bbb8c53fce)
- [bt_bip_put_linked_thumbnail](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga8b730495f4dd4e6f8db85c5b060a3cae)
- [bt_bip_put_linked_thumbnail_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gac96e873a840b072f5213b7483d633aaa)
- [bt_bip_put_linked_attachment](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga86085e98964dcfd19725b5d96f38a99b)
- [bt_bip_put_linked_attachment_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad6a7df2b0c49c0df616ef170c7b9e431)
- [bt_bip_remote_display](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga021a5d82b292d04cd0e2d53b1b32344b)
- [bt_bip_remote_display_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga0c54da02bc8dda26794f398e06e66cb3)
- [bt_bip_delete_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5302af5beb7cd5c98a9cbdc288f09d3c)
- [bt_bip_delete_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad53a7666b90a97034276fe341c2bd7a2)
- [bt_bip_start_print](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga8a948dcee431ced321e7b5d51c8d5f9c)
- [bt_bip_start_print_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae9ea9f936aa75b287a2152a747fd687a)
- [bt_bip_start_archive](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9674dc3dc2137a663a971f8521a41845)
- [bt_bip_start_archive_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad16038fa018919a10d9be7fa6deeb659)
- [bt_bip_add_header_image_desc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf48266502eacfc19938e1dfb29a3619b)
- [len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [bt_bip_add_header_image_handle](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga4ca80902f04ea770c59c5e498fef615a)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)
- [bt_bip_client_cb::disconnect](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a00575e54960da7eadb6c97603c15db76)
- [bt_bip_client_cb::put_image](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a0fb9d1c1bde99fab9f68997dcce31cca)
- [bt_bip_client_cb::get_monitoring_image](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a1085306d4098491363df71e82baab9e3)
- [bt_bip_client_cb::get_image_properties](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a16aea4cd3428723afee39332f6112c3e)
- [bt_bip_client_cb::get_status](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a287c05808d89726d5a3fbe965b29fd52)
- [bt_bip_client_cb::put_linked_attachment](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a3aae2299cb0779cf517d40368dc9a97e)
- [bt_bip_client_cb::remote_display](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a3ead32fbbe46d4ec0e73d0a840dc30b0)
- [bt_bip_client_cb::get_caps](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a3f6e8efdbdee62d23532bff52850ddb3)
- [bt_bip_client_cb::delete_image](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a5bb82c50c8e535457c17726e6133b4ef)
- [bt_bip_client_cb::start_archive](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a6ad152e72050d05eb8b47ba00237b6c4)
- [bt_bip_client_cb::start_print](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a7228b45ce57155f308d6a9b983074997)
- [bt_bip_client_cb::get_linked_attachment](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a72937856348fabd76696237a55ced1e9)
- [bt_bip_client_cb::get_partial_image](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a9efe5d25e239144bb40e05ff6494f20d)
- [bt_bip_client_cb::get_linked_thumbnail](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#a9f7713e8e68233c5837edbb46de6c758)
- [bt_bip_client_cb::get_image](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#aa551eac8ba777bbb7e286e36015a5a72)
- [bt_bip_client_cb::abort](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#aaedbc7f33eba36d176360c4806a3a27e)
- [bt_bip_client_cb::get_image_list](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#acda8a5a4ae315bf1b65209df9ff6b8e4)
- [bt_bip_client_cb::put_linked_thumbnail](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#aec614697e4e4ccd3dd326ecffc311c9b)
- [bt_bip_client_cb::connect](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md#afd9b65b4810a31a8bd48502fcf11eff1)
- [bt_bip_l2cap_server::server](../bluetooth_service_model_reference/P004_bt_bip_l2cap_server_结构体.md#a830f0f266401a3e95c21e5fbb25bc057)
- [bt_bip_l2cap_server::accept](../bluetooth_service_model_reference/P004_bt_bip_l2cap_server_结构体.md#aeb027a550bef264ef287e25cc3d9ffa9)
- [bt_bip_rfcomm_server::server](../bluetooth_service_model_reference/P005_bt_bip_rfcomm_server_结构体.md#a40ec65e156c02ad06b55aa1fc594ca71)
- [bt_bip_rfcomm_server::accept](../bluetooth_service_model_reference/P005_bt_bip_rfcomm_server_结构体.md#ad7b714b584c18e41feb7385819c50511)
- [bt_bip_server_cb::connect](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a094c1d805d9e099cacb9b91315c799e7)
- [bt_bip_server_cb::delete_image](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a0f8052f0ee8a4e5130b538e25231fc1b)
- [bt_bip_server_cb::get_image](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a27710e3871c031d4d787dc6f2223e71d)
- [bt_bip_server_cb::get_status](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a40c07a467ff5573400cc10ba58ee54f2)
- [bt_bip_server_cb::put_linked_attachment](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a48d411ddb30784a729204080420c203d)
- [bt_bip_server_cb::put_linked_thumbnail](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a4c8bf0f0791766e8c547ea10630e0948)
- [bt_bip_server_cb::start_archive](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a6514602bea0d066abdf41d6f021d4d51)
- [bt_bip_server_cb::get_caps](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a6c93a136a7677aa05928e762415af2de)
- [bt_bip_server_cb::start_print](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a6ca521f03e917b7354eaefac20b5b33f)
- [bt_bip_server_cb::get_partial_image](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a755b097ab450d312a3e29f5b1a75dadf)
- [bt_bip_server_cb::put_image](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a7b0c02fd0c1546e730df162b14db745b)
- [bt_bip_server_cb::remote_display](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a81f786528f0db0afc54f7518f3765df0)
- [bt_bip_server_cb::abort](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a877caeb43927ab27b360cd27b628b683)
- [bt_bip_server_cb::get_monitoring_image](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#a904935d6a327b9eba0ea68e924d8c1c5)
- [bt_bip_server_cb::get_linked_attachment](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#ac38d13107bbd18400690196efeddb228)
- [bt_bip_server_cb::get_image_list](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#ad2630977d48b11da5c70762f4e6cb49e)
- [bt_bip_server_cb::disconnect](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#aefa142e33e50b8d23f89c732fd79a125)
- [bt_bip_server_cb::get_image_properties](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#af41d62e8ff812c9ace9a5c916c08314d)
- [bt_bip_server_cb::get_linked_thumbnail](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md#afc3ba204dd51bdc758cf3a6da9d72185)
- [bt_bip_transport_ops::disconnected](../bluetooth_service_model_reference/P008_bt_bip_transport_ops_结构体.md#a49f1708ed03ebe8cfb6a2f11b76bda73)
- [bt_bip_transport_ops::connected](../bluetooth_service_model_reference/P008_bt_bip_transport_ops_结构体.md#a80a1596a382b93366e13a857a5edf3ba)
- [bt_bip::goep_transport](../bluetooth_service_model_reference/P001_bt_bip_结构体.md#a245296151dcf59b69822e3122488c2c2)
- [bt_bip::role](../bluetooth_service_model_reference/P001_bt_bip_结构体.md#a9cee12abb9b8efadb1b7c3e21803f349)
- [bt_bip::ops](../bluetooth_service_model_reference/P001_bt_bip_结构体.md#ac5b8a3fd23216a0894a47ac487835bc0)
- [bt_bip::goep](../bluetooth_service_model_reference/P001_bt_bip_结构体.md#adba3573d8d8250c015cb5adca9bd77bb)
- [net_buf::len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)

---

[上一章](P018_avdtp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P020_uuid.h_源码浏览.md)
