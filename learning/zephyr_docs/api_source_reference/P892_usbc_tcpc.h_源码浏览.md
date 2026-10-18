---
id: learning.zephyr-docs.api-source-reference.page-892
title: usbc_tcpc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbc__tcpc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第892章\_usbc\_tcpc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tcpc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tcpc_8h.html)。

## 892.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
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
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00169"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="foldopen00383"></a>
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
<a id="l00421"></a>
<a id="l00423"></a>
<a id="l00425"></a>
<a id="l00427"></a>
<a id="l00429"></a>
<a id="l00431"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00437"></a>
<a id="l00439"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00445"></a>
<a id="foldopen00449"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="foldopen00457"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="foldopen00465"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="foldopen00473"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="foldopen00481"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="foldopen00489"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="foldopen00498"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="foldopen00512"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="foldopen00532"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="foldopen00554"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="foldopen00575"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="foldopen00595"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="foldopen00615"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="foldopen00636"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="foldopen00660"></a>
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
<a id="foldopen00684"></a>
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
<a id="foldopen00708"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="foldopen00733"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="foldopen00753"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="foldopen00773"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="foldopen00792"></a>
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
<a id="foldopen00836"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="foldopen00858"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00869"></a>
<a id="foldopen00880"></a>
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
<a id="foldopen00900"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="foldopen00921"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="foldopen00941"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00948"></a>
<a id="l00949"></a>
<a id="l00950"></a>
<a id="l00951"></a>
<a id="foldopen00960"></a>
<a id="l00960"></a>
<a id="l00961"></a>
<a id="l00962"></a>
<a id="l00963"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="foldopen00980"></a>
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
<a id="foldopen00999"></a>
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
<a id="foldopen01021"></a>
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
<a id="foldopen01042"></a>
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
<a id="foldopen01063"></a>
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
<a id="foldopen01085"></a>
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
<a id="foldopen01106"></a>
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
<a id="l01120"></a>
<a id="l01121"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga0dfa332e501412fb407ef2490a042e11"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga232b5d184f585aab94eb22daaf06c86b"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga238a927c4602269c48325d06d0f72215"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga26217be69c8bc7ea24e6cabe489445da"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga2da6efeb17079086b4dc7ac52d2e60e7"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga39981c9b68e280de660ca15e137ffbd0"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga483cbf6d74b5a892d8d241ccc8f6060e"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga511cdf626c88790199edbd2fd578a833"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga56db121a729ffbb9173fe03fe867add1"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga7cd4aae87502bf5ebb1939edceea81f3"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga8863bafbd43a21204b990aa74d710285"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_ga99bb0b6056fb353fe15fc2d717f1a724"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gaa309db76ccb877d1cd9797d34bc55900"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gaa791f068d25e28abbd7d45071a5016be"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gaaed7c7d360c5eb455d84164fc4ee2d1d"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gab0828b95c31b6d6523ca471dd68ec065"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gab1f1d2db116913e4c0e451f57fb76d2c"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gab503f46443ce870dd0baeebf8dd48e8f"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gabafb00fd478d682be7d33379b2c2487e"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gac524dbe59d67fb5bdfad78bc1a4d64c9"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gac6f9724f73200ca20f1aa0a519928e50"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gad1db9d036dd666846065bbf35ea22177"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gad8d3e1b467e6ee4fb58dcfed16117737"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gadc6b26855f37fe94391f294c7f63d5bd"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gae28524287fdb5504883afb66003d035c"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gae3339cd538cf4025f9f6e0959647e430"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gae749f76083de380e2edd602dc0e30402"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gaea02443c9aeb62583903291908a660cd"></a>
<a id="agroup__usb__type__c__port__controller__api__backend_html_gaf8d6f41fdd6fe99a1b629d361556966d"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga01687aa218b25ba137e994a2a55bce23"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga03849a7a4fd7f468b18838c443d1ecd8"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga03c8c6fc6f4c6adefacbc809588e1f85"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga073ad4a46a5ea1f9e5cad45488d672f0"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga0c1cd7bc86c89abf5e348987d34e4623"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga0d1868d555e99877e062fb7135d9db8f"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga0db896e395812603a03548b8faac6791"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga153054be89d5f21148fe3ee750c718ee"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga1f057bcddc5a7757370f2e6de8170128"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga247f0ea91249753d6f5eefe006617e41"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga25a110be90977e768623f3a0c9a222d5"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga34e4caefb0f660b170f97956ac57b707"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga3937d66636a2b22422caf11c48f7628a"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga3958eac0cc0b9b2ac782e0cdb235036c"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga4687047910cad0dd970bbd28adcf22ed"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga4d2b77f6ee685d1bff1117843150e664"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga53f0207ecb63011c6dfc3c298a841ed4"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga5f42fa12f90d34961eeeb67c0dc4f925"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga66ab7a9f3cd1b80cd5bc8e99040c5627"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga6dfd68915ffe093058f6187b770a2436"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga71981a635ad82b9db41d549f29ad5c68"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga75f0dc246dac576f14c5ac51b45fd489"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga7a63d55cbe5de1d89aa76e10df0140ed"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga894d24140f8675b4f48d759c27f52076"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga8bf8fd202d582a4cc179a0fc4aff35e1"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga8d30c961335f62faa33aa7d842422da0"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga8f06b257d1bd0a17eb3042d204b2e6cd"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga905176a77ff127f4df8f6a4f2c61a1b7"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga91c3c40ea82ce5a081918183d8b76c06"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga91eef7084b523f1991e000f0592b8cbd"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga961a4dc393d58dc44ea19a62c943ed48"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gaa06e156bef46ff3f70cc8c302ddf0a4d"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gaa0d2059c3a53df986150141f73b9a98a"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gaaa38e56e6bc8c41e936d8ed70aaa8a23"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gaac29d0958fd377db24f1911cfa03188c"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gab0f1f5d47c1e2b8ee9eb3d7875a0051e"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gab4e9cc812679cf8cb0189f73a28d7cd2"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gabc50daa9cc713b1d0e340007e3850ca8"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gac5737d02caa2b9e649b469bcd648440f"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gaccc728a1f27c59a163a5c0a221ab7c18"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gafd8253dfa6abc80d0717b17271ed8916"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22eda284b478e32999fd923ba3064088274a9"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22eda302c30d41b09b4bf1949ce0c945c71fe"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22eda30b8a2c88cc2309849efa9d478271a3f"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22eda4356cb85ef371e72badad22110172e25"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22eda449d3f9271aa42feb43e54a1f36114eb"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22eda57eedbbbb9b1d899e1607e25c2799eeb"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22eda61c51ceb776d0432c657f6c16d5595e0"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22eda642e2b837d88dc983177546a06d938b2"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22eda64f5af2ef616a1adf90ff3549a114a66"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22eda8aa0d4566f11e6079f59500ac03929cd"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22edabbce6e484dc5373597097a664a6b5af4"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22edac44bb12fb7bd9de2f49af7d5f72744b0"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22edac5675390dfba5276227ff8d2be783992"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22edacd3a5188b6be126dfd00a4676e2a768e"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22edadff8e9cab783e22eedad2971baae77ec"></a>
<a id="agroup__usb__type__c__port__controller__api_html_gga4687047910cad0dd970bbd28adcf22edaefb353c046fa8346a4736d02a3003752"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ggafd8253dfa6abc80d0717b17271ed8916a14723bbaaae32413e2399159a6def440"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ggafd8253dfa6abc80d0717b17271ed8916a3b639f1629de38eb9c29d6af24f5011b"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ggafd8253dfa6abc80d0717b17271ed8916a45f424f2f0e126085d3e49e0cc4d7c61"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ggafd8253dfa6abc80d0717b17271ed8916a5e15cc2aae46edf6b7e0f5316b37a9db"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ggafd8253dfa6abc80d0717b17271ed8916aa42f110436df796f5cfdadab921aac7f"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ggafd8253dfa6abc80d0717b17271ed8916aaf41a51cc8e4c849780af463ea63a0c4"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ggafd8253dfa6abc80d0717b17271ed8916afe72a3bc04d7f92bd74e754129e99c6d"></a>
<a id="agroup__usb__type__c_html_ga0200c820510eb786f3ca30a9b5f7aada"></a>
<a id="agroup__usb__type__c_html_ga4e0eec97f7c5c97b87eff9561deea2d5"></a>
<a id="agroup__usb__type__c_html_ga64e32ec2da97f70fd5b96975317cb92c"></a>
<a id="agroup__usb__type__c_html_ga6b98bbe238e62cfd5531688494a63de2"></a>
<a id="agroup__usb__type__c_html_gaa6dda0612045b5f55b9d8ba63d2b9f9d"></a>
<a id="agroup__usb__type__c_html_gac5b4b58840c9b076a869a5816ba100db"></a>
<a id="agroup__usb__type__c_html_gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293"></a>
<a id="agroup__usb__type__c_html_gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea"></a>
<a id="agroup__usb__type__c_html_gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9"></a>
<a id="agroup__usb__type__c_html_gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca"></a>
<a id="agroup__usb__type__c_html_gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructpd__msg_html"></a>
<a id="astructtcpc__chip__info_html"></a>
<a id="astructtcpc__chip__info_html_a14c11999ef548e41f4338f3e7208b7a9"></a>
<a id="astructtcpc__chip__info_html_a677a85ef27f0d5db969ce3232506d1bb"></a>
<a id="astructtcpc__chip__info_html_a7789339580e2774d18a8f4c78332f774"></a>
<a id="astructtcpc__chip__info_html_a8d66f33379493e1a0ed707b3715f863a"></a>
<a id="astructtcpc__chip__info_html_a9e76ee3bcc395dbb77d7a065f6181cd6"></a>
<a id="astructtcpc__chip__info_html_ab48400ea4209d5443e5b7e0bfee6c4fc"></a>
<a id="astructtcpc__driver__api_html"></a>
<a id="astructtcpc__driver__api_html_a022918a3098b5b2cbba9d660f8f05a0a"></a>
<a id="astructtcpc__driver__api_html_a0239a44cb7c1977ad96423e0c11f3ad6"></a>
<a id="astructtcpc__driver__api_html_a212ac07d41716e76742a3db2aea2301c"></a>
<a id="astructtcpc__driver__api_html_a385a741aa402403637e3f2f3f7c4c456"></a>
<a id="astructtcpc__driver__api_html_a3bfecb52f9ed73b2a1eb081914197f01"></a>
<a id="astructtcpc__driver__api_html_a3ca4d4e9ff4658ae2c805cc0a7613b8a"></a>
<a id="astructtcpc__driver__api_html_a3ef2690b032843d0d8e3ca3c675428cf"></a>
<a id="astructtcpc__driver__api_html_a485a6e3409a73015fc479ada7c5170b0"></a>
<a id="astructtcpc__driver__api_html_a49f69dcc86e944e7d922bcadab949194"></a>
<a id="astructtcpc__driver__api_html_a536fbd074107f6a2b65e553f8acd1d0b"></a>
<a id="astructtcpc__driver__api_html_a6938fec4089908809cbd101095a5c4f8"></a>
<a id="astructtcpc__driver__api_html_a6f8756d7b4f4d6e2beea20b3e5176bcd"></a>
<a id="astructtcpc__driver__api_html_a70571ced311498d1065b94d81cbf5d4e"></a>
<a id="astructtcpc__driver__api_html_a72ac506119d63dc10be9b497fe479e6f"></a>
<a id="astructtcpc__driver__api_html_a85c30801d61470a3bf41c27117a847ee"></a>
<a id="astructtcpc__driver__api_html_a895901166eeedac50b48918b436ee6bc"></a>
<a id="astructtcpc__driver__api_html_a8cc43981c1047cc92dbed8843e6f72f0"></a>
<a id="astructtcpc__driver__api_html_aa1b59f3aa1ccc8684445f119d4ea75aa"></a>
<a id="astructtcpc__driver__api_html_aaa0956282b1b9cf3e41dc45a9f31e073"></a>
<a id="astructtcpc__driver__api_html_aaa2b59daf061965dc6ed6cb7a42b684f"></a>
<a id="astructtcpc__driver__api_html_ab5ef4ec81c532dc054b53058b199a7e0"></a>
<a id="astructtcpc__driver__api_html_ac79a47b9a94fb4481bc9ecdba86b898d"></a>
<a id="astructtcpc__driver__api_html_aca835517376e241345d05bf66119cb6c"></a>
<a id="astructtcpc__driver__api_html_adc65471e8ae2b106575b25d5c30653dd"></a>
<a id="astructtcpc__driver__api_html_adc8f34eefe17f59953bba2029fcaa4bc"></a>
<a id="astructtcpc__driver__api_html_ae4cf25f8c0c5f0020c0d57b9dc6bdb4c"></a>
<a id="astructtcpc__driver__api_html_ae5c9719810866d0fcc03f329c84b3a58"></a>
<a id="astructtcpc__driver__api_html_af04de5dd092efeb32a23e21cda5033c0"></a>
<a id="astructtcpc__driver__api_html_af483dc0041006ad9bb717ffc4b570978"></a>
<a id="ausbc__pd_8h_html"></a>
<a id="ausbc__tc_8h_html"></a>

```c
/*
 * Copyright 2022 The Chromium OS Authors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_TCPC_H_
#define ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_TCPC_H_


#include <zephyr/types.h>
#include <zephyr/device.h>
#include <errno.h>

#include "usbc_tc.h"
#include "usbc_pd.h"

#ifdef __cplusplus
extern "C" {
#endif

enum tcpc_alert {
        TCPC_ALERT_CC_STATUS,
        TCPC_ALERT_POWER_STATUS,
        TCPC_ALERT_MSG_STATUS,
        TCPC_ALERT_HARD_RESET_RECEIVED,
        TCPC_ALERT_TRANSMIT_MSG_FAILED,
        TCPC_ALERT_TRANSMIT_MSG_DISCARDED,
        TCPC_ALERT_TRANSMIT_MSG_SUCCESS,
        TCPC_ALERT_VBUS_ALARM_HI,
        TCPC_ALERT_VBUS_ALARM_LO,
        TCPC_ALERT_FAULT_STATUS,
        TCPC_ALERT_RX_BUFFER_OVERFLOW,
        TCPC_ALERT_VBUS_SNK_DISCONNECT,
        TCPC_ALERT_BEGINNING_MSG_STATUS,
        TCPC_ALERT_EXTENDED_STATUS,
        TCPC_ALERT_EXTENDED,
        TCPC_ALERT_VENDOR_DEFINED
};

enum tcpc_status_reg {
        TCPC_ALERT_STATUS,
        TCPC_CC_STATUS,
        TCPC_POWER_STATUS,
        TCPC_FAULT_STATUS,
        TCPC_EXTENDED_STATUS,
        TCPC_EXTENDED_ALERT_STATUS,
        TCPC_VENDOR_DEFINED_STATUS
};

struct tcpc_chip_info {
        uint16_t vendor_id;
        uint16_t product_id;
        uint16_t device_id;
        uint64_t fw_version_number;

        union {
                uint8_t min_req_fw_version_string[8];
                uint64_t min_req_fw_version_number;
        };
};

typedef int (*tcpc_vconn_control_cb_t)(const struct device *tcpc_dev, const struct device *usbc_dev,
                                       enum tc_cc_polarity pol, bool enable);

typedef int (*tcpc_vconn_discharge_cb_t)(const struct device *tcpc_dev,
                                         const struct device *usbc_dev, enum tc_cc_polarity pol,
                                         bool enable);

typedef void (*tcpc_alert_handler_cb_t)(const struct device *dev, void *data,
                                        enum tcpc_alert alert);


typedef int (*tcpc_api_init_t)(const struct device *dev);

typedef int (*tcpc_api_get_cc_t)(const struct device *dev, enum tc_cc_voltage_state *cc1,
                                 enum tc_cc_voltage_state *cc2);

typedef int (*tcpc_api_select_rp_value_t)(const struct device *dev, enum tc_rp_value rp);

typedef int (*tcpc_api_get_rp_value_t)(const struct device *dev, enum tc_rp_value *rp);

typedef int (*tcpc_api_set_cc_t)(const struct device *dev, enum tc_cc_pull pull);

typedef void (*tcpc_api_set_vconn_discharge_cb_t)(const struct device *dev,
                                                  tcpc_vconn_discharge_cb_t cb,
                                                  const struct device *usbc_dev);

typedef void (*tcpc_api_set_vconn_cb_t)(const struct device *dev, tcpc_vconn_control_cb_t vconn_cb,
                                        const struct device *usbc_dev);

typedef int (*tcpc_api_vconn_discharge_t)(const struct device *dev, bool enable);

typedef int (*tcpc_api_set_vconn_t)(const struct device *dev, bool enable);

typedef int (*tcpc_api_set_roles_t)(const struct device *dev, enum tc_power_role power_role,
                                    enum tc_data_role data_role);

typedef int (*tcpc_api_get_rx_pending_msg_t)(const struct device *dev, struct pd_msg *msg);

typedef int (*tcpc_api_set_rx_enable_t)(const struct device *dev, bool enable);

typedef int (*tcpc_api_set_cc_polarity_t)(const struct device *dev, enum tc_cc_polarity polarity);

typedef int (*tcpc_api_transmit_data_t)(const struct device *dev, struct pd_msg *msg);

typedef int (*tcpc_api_dump_std_reg_t)(const struct device *dev);

typedef int (*tcpc_api_mask_status_register_t)(const struct device *dev, enum tcpc_status_reg reg,
                                               uint32_t mask);

typedef int (*tcpc_api_set_debug_accessory_t)(const struct device *dev, bool enable);

typedef int (*tcpc_api_set_debug_detach_t)(const struct device *dev);

typedef int (*tcpc_api_set_drp_toggle_t)(const struct device *dev, bool enable);

typedef int (*tcpc_api_get_snk_ctrl_t)(const struct device *dev);

typedef int (*tcpc_api_set_snk_ctrl_t)(const struct device *dev, bool enable);

typedef int (*tcpc_api_get_src_ctrl_t)(const struct device *dev);

typedef int (*tcpc_api_set_src_ctrl_t)(const struct device *dev, bool enable);

typedef int (*tcpc_api_get_chip_info_t)(const struct device *dev, struct tcpc_chip_info *chip_info);

typedef int (*tcpc_api_set_low_power_mode_t)(const struct device *dev, bool enable);

typedef int (*tcpc_api_sop_prime_enable_t)(const struct device *dev, bool enable);

typedef int (*tcpc_api_set_bist_test_mode_t)(const struct device *dev, bool enable);

typedef int (*tcpc_api_set_alert_handler_cb_t)(const struct device *dev,
                                               tcpc_alert_handler_cb_t handler, void *data);

typedef int (*tcpc_api_dead_battery_enabled_t)(const struct device *dev, bool *enabled);

__subsystem struct tcpc_driver_api {
        tcpc_api_init_t init;
        tcpc_api_get_cc_t get_cc;
        tcpc_api_select_rp_value_t select_rp_value;
        tcpc_api_get_rp_value_t get_rp_value;
        tcpc_api_set_cc_t set_cc;
        tcpc_api_set_vconn_discharge_cb_t set_vconn_discharge_cb;
        tcpc_api_set_vconn_cb_t set_vconn_cb;
        tcpc_api_vconn_discharge_t vconn_discharge;
        tcpc_api_set_vconn_t set_vconn;
        tcpc_api_set_roles_t set_roles;
        tcpc_api_get_rx_pending_msg_t get_rx_pending_msg;
        tcpc_api_set_rx_enable_t set_rx_enable;
        tcpc_api_set_cc_polarity_t set_cc_polarity;
        tcpc_api_transmit_data_t transmit_data;
        tcpc_api_dump_std_reg_t dump_std_reg;
        tcpc_api_mask_status_register_t mask_status_register;
        tcpc_api_set_debug_accessory_t set_debug_accessory;
        tcpc_api_set_debug_detach_t set_debug_detach;
        tcpc_api_set_drp_toggle_t set_drp_toggle;
        tcpc_api_get_snk_ctrl_t get_snk_ctrl;
        tcpc_api_set_snk_ctrl_t set_snk_ctrl;
        tcpc_api_get_src_ctrl_t get_src_ctrl;
        tcpc_api_set_src_ctrl_t set_src_ctrl;
        tcpc_api_get_chip_info_t get_chip_info;
        tcpc_api_set_low_power_mode_t set_low_power_mode;
        tcpc_api_sop_prime_enable_t sop_prime_enable;
        tcpc_api_set_bist_test_mode_t set_bist_test_mode;
        tcpc_api_set_alert_handler_cb_t set_alert_handler_cb;
        tcpc_api_dead_battery_enabled_t dead_battery_enabled;
};


static inline int tcpc_is_cc_rp(enum tc_cc_voltage_state cc)
{
        return (cc == TC_CC_VOLT_RP_DEF) || (cc == TC_CC_VOLT_RP_1A5) || (cc == TC_CC_VOLT_RP_3A0);
}

static inline int tcpc_is_cc_open(enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
{
        return (cc1 < TC_CC_VOLT_RD) && (cc2 < TC_CC_VOLT_RD);
}

static inline int tcpc_is_cc_snk_dbg_acc(enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
{
        return cc1 == TC_CC_VOLT_RD && cc2 == TC_CC_VOLT_RD;
}

static inline int tcpc_is_cc_src_dbg_acc(enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
{
        return tcpc_is_cc_rp(cc1) && tcpc_is_cc_rp(cc2);
}

static inline int tcpc_is_cc_audio_acc(enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
{
        return cc1 == TC_CC_VOLT_RA && cc2 == TC_CC_VOLT_RA;
}

static inline int tcpc_is_cc_at_least_one_rd(enum tc_cc_voltage_state cc1,
                                             enum tc_cc_voltage_state cc2)
{
        return cc1 == TC_CC_VOLT_RD || cc2 == TC_CC_VOLT_RD;
}

static inline int tcpc_is_cc_only_one_rd(enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
{
        return tcpc_is_cc_at_least_one_rd(cc1, cc2) && cc1 != cc2;
}

static inline int tcpc_init(const struct device *dev)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        __ASSERT(api->init != NULL, "Callback pointer should not be NULL");

        return api->init(dev);
}

static inline int tcpc_get_cc(const struct device *dev, enum tc_cc_voltage_state *cc1,
                              enum tc_cc_voltage_state *cc2)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->get_cc == NULL) {
                return -ENOSYS;
        }

        return api->get_cc(dev, cc1, cc2);
}

static inline int tcpc_select_rp_value(const struct device *dev, enum tc_rp_value rp)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->select_rp_value == NULL) {
                return -ENOSYS;
        }

        return api->select_rp_value(dev, rp);
}

static inline int tcpc_get_rp_value(const struct device *dev, enum tc_rp_value *rp)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->get_rp_value == NULL) {
                return -ENOSYS;
        }

        return api->get_rp_value(dev, rp);
}

static inline int tcpc_set_cc(const struct device *dev, enum tc_cc_pull pull)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        __ASSERT(api->set_cc != NULL, "Callback pointer should not be NULL");

        return api->set_cc(dev, pull);
}

static inline void tcpc_set_vconn_cb(const struct device *dev, tcpc_vconn_control_cb_t vconn_cb,
                                     const struct device *usbc_dev)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        __ASSERT(api->set_vconn_cb != NULL, "Callback pointer should not be NULL");

        api->set_vconn_cb(dev, vconn_cb, usbc_dev);
}

static inline void tcpc_set_vconn_discharge_cb(const struct device *dev,
                                               tcpc_vconn_discharge_cb_t cb,
                                               const struct device *usbc_dev)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        __ASSERT(api->set_vconn_discharge_cb != NULL, "Callback pointer should not be NULL");

        api->set_vconn_discharge_cb(dev, cb, usbc_dev);
}

static inline int tcpc_vconn_discharge(const struct device *dev, bool enable)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->vconn_discharge == NULL) {
                return -ENOSYS;
        }

        return api->vconn_discharge(dev, enable);
}

static inline int tcpc_set_vconn(const struct device *dev, bool enable)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->set_vconn == NULL) {
                return -ENOSYS;
        }

        return api->set_vconn(dev, enable);
}

static inline int tcpc_set_roles(const struct device *dev, enum tc_power_role power_role,
                                 enum tc_data_role data_role)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->set_roles == NULL) {
                return -ENOSYS;
        }

        return api->set_roles(dev, power_role, data_role);
}

static inline int tcpc_get_rx_pending_msg(const struct device *dev, struct pd_msg *buf)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        __ASSERT(api->get_rx_pending_msg != NULL, "Callback pointer should not be NULL");

        return api->get_rx_pending_msg(dev, buf);
}

static inline int tcpc_set_rx_enable(const struct device *dev, bool enable)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->set_rx_enable == NULL) {
                return -ENOSYS;
        }

        return api->set_rx_enable(dev, enable);
}

static inline int tcpc_set_cc_polarity(const struct device *dev, enum tc_cc_polarity polarity)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        __ASSERT(api->set_cc_polarity != NULL, "Callback pointer should not be NULL");

        return api->set_cc_polarity(dev, polarity);
}

static inline int tcpc_transmit_data(const struct device *dev, struct pd_msg *msg)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->transmit_data == NULL) {
                return -ENOSYS;
        }

        return api->transmit_data(dev, msg);
}

static inline int tcpc_dump_std_reg(const struct device *dev)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->dump_std_reg == NULL) {
                return -ENOSYS;
        }

        return api->dump_std_reg(dev);
}

static inline int tcpc_set_alert_handler_cb(const struct device *dev,
                                            tcpc_alert_handler_cb_t handler, void *data)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        __ASSERT(api->set_alert_handler_cb != NULL, "Callback pointer should not be NULL");

        return api->set_alert_handler_cb(dev, handler, data);
}

static inline int tcpc_mask_status_register(const struct device *dev, enum tcpc_status_reg reg,
                                            uint32_t mask)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->mask_status_register == NULL) {
                return -ENOSYS;
        }

        return api->mask_status_register(dev, reg, mask);
}

static inline int tcpc_set_debug_accessory(const struct device *dev, bool enable)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->set_debug_accessory == NULL) {
                return -ENOSYS;
        }

        return api->set_debug_accessory(dev, enable);
}

static inline int tcpc_set_debug_detach(const struct device *dev)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->set_debug_detach == NULL) {
                return -ENOSYS;
        }

        return api->set_debug_detach(dev);
}

static inline int tcpc_set_drp_toggle(const struct device *dev, bool enable)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->set_drp_toggle == NULL) {
                return -ENOSYS;
        }

        return api->set_drp_toggle(dev, enable);
}

static inline int tcpc_get_snk_ctrl(const struct device *dev)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->get_snk_ctrl == NULL) {
                return -ENOSYS;
        }

        return api->get_snk_ctrl(dev);
}

static inline int tcpc_set_snk_ctrl(const struct device *dev, bool enable)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->set_snk_ctrl == NULL) {
                return -ENOSYS;
        }

        return api->set_snk_ctrl(dev, enable);
}

static inline int tcpc_get_src_ctrl(const struct device *dev)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->get_src_ctrl == NULL) {
                return -ENOSYS;
        }

        return api->get_src_ctrl(dev);
}

static inline int tcpc_set_src_ctrl(const struct device *dev, bool enable)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->set_src_ctrl == NULL) {
                return -ENOSYS;
        }

        return api->set_src_ctrl(dev, enable);
}

static inline int tcpc_set_bist_test_mode(const struct device *dev, bool enable)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->set_bist_test_mode == NULL) {
                return -ENOSYS;
        }

        return api->set_bist_test_mode(dev, enable);
}

static inline int tcpc_get_chip_info(const struct device *dev, struct tcpc_chip_info *chip_info)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->get_chip_info == NULL) {
                return -ENOSYS;
        }

        return api->get_chip_info(dev, chip_info);
}

static inline int tcpc_set_low_power_mode(const struct device *dev, bool enable)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->set_low_power_mode == NULL) {
                return -ENOSYS;
        }

        return api->set_low_power_mode(dev, enable);
}

static inline int tcpc_sop_prime_enable(const struct device *dev, bool enable)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->sop_prime_enable == NULL) {
                return -ENOSYS;
        }

        return api->sop_prime_enable(dev, enable);
}

static inline int tcpc_dead_battery_enabled(const struct device *dev, bool *enabled)
{
        const struct tcpc_driver_api *api = DEVICE_API_GET(tcpc, dev);

        if (api->dead_battery_enabled == NULL) {
                return -ENOSYS;
        }

        return api->dead_battery_enabled(dev, enabled);
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_TCPC_H_ */
```

## 892.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 The Chromium OS Authors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 1125 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_TCPC_H_`。

## 892.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tcpc_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [usbc_tc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tc_8h.html)
- [usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h.html)
- [tcpc_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4687047910cad0dd970bbd28adcf22ed)
- [TCPC_ALERT_CC_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda30b8a2c88cc2309849efa9d478271a3f)
- [TCPC_ALERT_POWER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edabbce6e484dc5373597097a664a6b5af4)
- [TCPC_ALERT_MSG_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda57eedbbbb9b1d899e1607e25c2799eeb)
- [TCPC_ALERT_HARD_RESET_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda61c51ceb776d0432c657f6c16d5595e0)
- [TCPC_ALERT_TRANSMIT_MSG_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edadff8e9cab783e22eedad2971baae77ec)
- [TCPC_ALERT_TRANSMIT_MSG_DISCARDED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda302c30d41b09b4bf1949ce0c945c71fe)
- [TCPC_ALERT_TRANSMIT_MSG_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda642e2b837d88dc983177546a06d938b2)
- [TCPC_ALERT_VBUS_ALARM_HI](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda64f5af2ef616a1adf90ff3549a114a66)
- [TCPC_ALERT_VBUS_ALARM_LO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edac44bb12fb7bd9de2f49af7d5f72744b0)
- [TCPC_ALERT_FAULT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edacd3a5188b6be126dfd00a4676e2a768e)
- [TCPC_ALERT_RX_BUFFER_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edaefb353c046fa8346a4736d02a3003752)
- [TCPC_ALERT_VBUS_SNK_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda8aa0d4566f11e6079f59500ac03929cd)
- [TCPC_ALERT_BEGINNING_MSG_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda449d3f9271aa42feb43e54a1f36114eb)
- [TCPC_ALERT_EXTENDED_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda284b478e32999fd923ba3064088274a9)
- [TCPC_ALERT_EXTENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda4356cb85ef371e72badad22110172e25)
- [TCPC_ALERT_VENDOR_DEFINED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edac5675390dfba5276227ff8d2be783992)
- [tcpc_status_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gafd8253dfa6abc80d0717b17271ed8916)
- [TCPC_ALERT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a3b639f1629de38eb9c29d6af24f5011b)
- [TCPC_CC_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916aaf41a51cc8e4c849780af463ea63a0c4)
- [TCPC_POWER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916aa42f110436df796f5cfdadab921aac7f)
- [TCPC_FAULT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a14723bbaaae32413e2399159a6def440)
- [TCPC_EXTENDED_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916afe72a3bc04d7f92bd74e754129e99c6d)
- [TCPC_EXTENDED_ALERT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a5e15cc2aae46edf6b7e0f5316b37a9db)
- [TCPC_VENDOR_DEFINED_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a45f424f2f0e126085d3e49e0cc4d7c61)
- [tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [vendor_id](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#ab48400ea4209d5443e5b7e0bfee6c4fc)
- [product_id](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#a14c11999ef548e41f4338f3e7208b7a9)
- [device_id](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#a9e76ee3bcc395dbb77d7a065f6181cd6)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [fw_version_number](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#a7789339580e2774d18a8f4c78332f774)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [min_req_fw_version_string](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#a677a85ef27f0d5db969ce3232506d1bb)
- [min_req_fw_version_number](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#a8d66f33379493e1a0ed707b3715f863a)
- [tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)
- [device](../device_reference/P002_设备对象结构.md)
- [tc_cc_polarity](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gac5b4b58840c9b076a869a5816ba100db)
- [tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)
- [tcpc_alert_handler_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga5f42fa12f90d34961eeeb67c0dc4f925)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [tcpc_api_init_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gae28524287fdb5504883afb66003d035c)
- [tcpc_api_get_cc_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga39981c9b68e280de660ca15e137ffbd0)
- [tc_cc_voltage_state](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga64e32ec2da97f70fd5b96975317cb92c)
- [tcpc_api_select_rp_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gae749f76083de380e2edd602dc0e30402)
- [tc_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga4e0eec97f7c5c97b87eff9561deea2d5)
- [tcpc_api_get_rp_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gad1db9d036dd666846065bbf35ea22177)
- [tcpc_api_set_cc_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gac524dbe59d67fb5bdfad78bc1a4d64c9)
- [tc_cc_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga0200c820510eb786f3ca30a9b5f7aada)
- [tcpc_api_set_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gad8d3e1b467e6ee4fb58dcfed16117737)
- [tcpc_api_set_vconn_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga26217be69c8bc7ea24e6cabe489445da)
- [tcpc_api_vconn_discharge_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gab503f46443ce870dd0baeebf8dd48e8f)
- [tcpc_api_set_vconn_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaf8d6f41fdd6fe99a1b629d361556966d)
- [tcpc_api_set_roles_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gadc6b26855f37fe94391f294c7f63d5bd)
- [tc_power_role](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gaa6dda0612045b5f55b9d8ba63d2b9f9d)
- [tc_data_role](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga6b98bbe238e62cfd5531688494a63de2)
- [tcpc_api_get_rx_pending_msg_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gab0828b95c31b6d6523ca471dd68ec065)
- [pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)
- [tcpc_api_set_rx_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga7cd4aae87502bf5ebb1939edceea81f3)
- [tcpc_api_set_cc_polarity_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaa791f068d25e28abbd7d45071a5016be)
- [tcpc_api_transmit_data_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gab1f1d2db116913e4c0e451f57fb76d2c)
- [tcpc_api_dump_std_reg_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga99bb0b6056fb353fe15fc2d717f1a724)
- [tcpc_api_mask_status_register_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaa309db76ccb877d1cd9797d34bc55900)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [tcpc_api_set_debug_accessory_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga238a927c4602269c48325d06d0f72215)
- [tcpc_api_set_debug_detach_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga483cbf6d74b5a892d8d241ccc8f6060e)
- [tcpc_api_set_drp_toggle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga56db121a729ffbb9173fe03fe867add1)
- [tcpc_api_get_snk_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gabafb00fd478d682be7d33379b2c2487e)
- [tcpc_api_set_snk_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaaed7c7d360c5eb455d84164fc4ee2d1d)
- [tcpc_api_get_src_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga2da6efeb17079086b4dc7ac52d2e60e7)
- [tcpc_api_set_src_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga8863bafbd43a21204b990aa74d710285)
- [tcpc_api_get_chip_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gac6f9724f73200ca20f1aa0a519928e50)
- [tcpc_api_set_low_power_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gae3339cd538cf4025f9f6e0959647e430)
- [tcpc_api_sop_prime_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga232b5d184f585aab94eb22daaf06c86b)
- [tcpc_api_set_bist_test_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaea02443c9aeb62583903291908a660cd)
- [tcpc_api_set_alert_handler_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga511cdf626c88790199edbd2fd578a833)
- [tcpc_api_dead_battery_enabled_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga0dfa332e501412fb407ef2490a042e11)
- [tcpc_driver_api](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md)
- [init](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#ae4cf25f8c0c5f0020c0d57b9dc6bdb4c)
- [get_cc](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#af483dc0041006ad9bb717ffc4b570978)
- [select_rp_value](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a3ef2690b032843d0d8e3ca3c675428cf)
- [get_rp_value](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a49f69dcc86e944e7d922bcadab949194)
- [set_cc](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a6938fec4089908809cbd101095a5c4f8)
- [set_vconn_discharge_cb](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#af04de5dd092efeb32a23e21cda5033c0)
- [set_vconn_cb](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a022918a3098b5b2cbba9d660f8f05a0a)
- [vconn_discharge](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#adc8f34eefe17f59953bba2029fcaa4bc)
- [set_vconn](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a536fbd074107f6a2b65e553f8acd1d0b)
- [set_roles](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#ae5c9719810866d0fcc03f329c84b3a58)
- [get_rx_pending_msg](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a385a741aa402403637e3f2f3f7c4c456)
- [set_rx_enable](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#ac79a47b9a94fb4481bc9ecdba86b898d)
- [set_cc_polarity](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a0239a44cb7c1977ad96423e0c11f3ad6)
- [transmit_data](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#aaa0956282b1b9cf3e41dc45a9f31e073)
- [dump_std_reg](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a212ac07d41716e76742a3db2aea2301c)
- [mask_status_register](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#adc65471e8ae2b106575b25d5c30653dd)
- [set_debug_accessory](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#aaa2b59daf061965dc6ed6cb7a42b684f)
- [set_debug_detach](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a85c30801d61470a3bf41c27117a847ee)
- [set_drp_toggle](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a3ca4d4e9ff4658ae2c805cc0a7613b8a)
- [get_snk_ctrl](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a6f8756d7b4f4d6e2beea20b3e5176bcd)
- [set_snk_ctrl](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#aca835517376e241345d05bf66119cb6c)
- [get_src_ctrl](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a895901166eeedac50b48918b436ee6bc)
- [set_src_ctrl](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a70571ced311498d1065b94d81cbf5d4e)
- [get_chip_info](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a72ac506119d63dc10be9b497fe479e6f)
- [set_low_power_mode](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a3bfecb52f9ed73b2a1eb081914197f01)
- [sop_prime_enable](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#aa1b59f3aa1ccc8684445f119d4ea75aa)
- [set_bist_test_mode](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#ab5ef4ec81c532dc054b53058b199a7e0)
- [set_alert_handler_cb](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a8cc43981c1047cc92dbed8843e6f72f0)
- [dead_battery_enabled](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a485a6e3409a73015fc479ada7c5170b0)
- [tcpc_is_cc_rp](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga6dfd68915ffe093058f6187b770a2436)
- [TC_CC_VOLT_RP_DEF](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293)
- [TC_CC_VOLT_RP_1A5](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72)
- [TC_CC_VOLT_RP_3A0](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca)
- [tcpc_is_cc_open](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga0db896e395812603a03548b8faac6791)
- [TC_CC_VOLT_RD](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9)
- [tcpc_is_cc_snk_dbg_acc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaa0d2059c3a53df986150141f73b9a98a)
- [tcpc_is_cc_src_dbg_acc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga03849a7a4fd7f468b18838c443d1ecd8)
- [tcpc_is_cc_audio_acc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga153054be89d5f21148fe3ee750c718ee)
- [TC_CC_VOLT_RA](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea)
- [tcpc_is_cc_at_least_one_rd](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gab4e9cc812679cf8cb0189f73a28d7cd2)
- [tcpc_is_cc_only_one_rd](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga91c3c40ea82ce5a081918183d8b76c06)
- [tcpc_init](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gabc50daa9cc713b1d0e340007e3850ca8)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [tcpc_get_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga66ab7a9f3cd1b80cd5bc8e99040c5627)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [tcpc_select_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga3958eac0cc0b9b2ac782e0cdb235036c)
- [tcpc_get_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga25a110be90977e768623f3a0c9a222d5)
- [tcpc_set_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gac5737d02caa2b9e649b469bcd648440f)
- [tcpc_set_vconn_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga1f057bcddc5a7757370f2e6de8170128)
- [tcpc_set_vconn_discharge_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga71981a635ad82b9db41d549f29ad5c68)
- [tcpc_vconn_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga3937d66636a2b22422caf11c48f7628a)
- [tcpc_set_vconn](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga247f0ea91249753d6f5eefe006617e41)
- [tcpc_set_roles](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8d30c961335f62faa33aa7d842422da0)
- [tcpc_get_rx_pending_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga34e4caefb0f660b170f97956ac57b707)
- [tcpc_set_rx_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga905176a77ff127f4df8f6a4f2c61a1b7)
- [tcpc_set_cc_polarity](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga53f0207ecb63011c6dfc3c298a841ed4)
- [tcpc_transmit_data](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8bf8fd202d582a4cc179a0fc4aff35e1)
- [tcpc_dump_std_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga91eef7084b523f1991e000f0592b8cbd)
- [tcpc_set_alert_handler_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga75f0dc246dac576f14c5ac51b45fd489)
- [tcpc_mask_status_register](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga0d1868d555e99877e062fb7135d9db8f)
- [tcpc_set_debug_accessory](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga01687aa218b25ba137e994a2a55bce23)
- [tcpc_set_debug_detach](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaaa38e56e6bc8c41e936d8ed70aaa8a23)
- [tcpc_set_drp_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaa06e156bef46ff3f70cc8c302ddf0a4d)
- [tcpc_get_snk_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga0c1cd7bc86c89abf5e348987d34e4623)
- [tcpc_set_snk_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga7a63d55cbe5de1d89aa76e10df0140ed)
- [tcpc_get_src_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga03c8c6fc6f4c6adefacbc809588e1f85)
- [tcpc_set_src_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8f06b257d1bd0a17eb3042d204b2e6cd)
- [tcpc_set_bist_test_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaccc728a1f27c59a163a5c0a221ab7c18)
- [tcpc_get_chip_info](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga894d24140f8675b4f48d759c27f52076)
- [tcpc_set_low_power_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga961a4dc393d58dc44ea19a62c943ed48)
- [tcpc_sop_prime_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gab0f1f5d47c1e2b8ee9eb3d7875a0051e)
- [tcpc_dead_battery_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaac29d0958fd377db24f1911cfa03188c)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [tcpc_chip_info::product_id](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#a14c11999ef548e41f4338f3e7208b7a9)
- [tcpc_chip_info::min_req_fw_version_string](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#a677a85ef27f0d5db969ce3232506d1bb)
- [tcpc_chip_info::fw_version_number](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#a7789339580e2774d18a8f4c78332f774)
- [tcpc_chip_info::min_req_fw_version_number](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#a8d66f33379493e1a0ed707b3715f863a)
- [tcpc_chip_info::device_id](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#a9e76ee3bcc395dbb77d7a065f6181cd6)
- [tcpc_chip_info::vendor_id](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md#ab48400ea4209d5443e5b7e0bfee6c4fc)
- [tcpc_driver_api::set_vconn_cb](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a022918a3098b5b2cbba9d660f8f05a0a)
- [tcpc_driver_api::set_cc_polarity](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a0239a44cb7c1977ad96423e0c11f3ad6)
- [tcpc_driver_api::dump_std_reg](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a212ac07d41716e76742a3db2aea2301c)
- [tcpc_driver_api::get_rx_pending_msg](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a385a741aa402403637e3f2f3f7c4c456)
- [tcpc_driver_api::set_low_power_mode](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a3bfecb52f9ed73b2a1eb081914197f01)
- [tcpc_driver_api::set_drp_toggle](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a3ca4d4e9ff4658ae2c805cc0a7613b8a)
- [tcpc_driver_api::select_rp_value](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a3ef2690b032843d0d8e3ca3c675428cf)
- [tcpc_driver_api::dead_battery_enabled](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a485a6e3409a73015fc479ada7c5170b0)
- [tcpc_driver_api::get_rp_value](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a49f69dcc86e944e7d922bcadab949194)
- [tcpc_driver_api::set_vconn](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a536fbd074107f6a2b65e553f8acd1d0b)
- [tcpc_driver_api::set_cc](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a6938fec4089908809cbd101095a5c4f8)
- [tcpc_driver_api::get_snk_ctrl](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a6f8756d7b4f4d6e2beea20b3e5176bcd)
- [tcpc_driver_api::set_src_ctrl](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a70571ced311498d1065b94d81cbf5d4e)
- [tcpc_driver_api::get_chip_info](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a72ac506119d63dc10be9b497fe479e6f)
- [tcpc_driver_api::set_debug_detach](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a85c30801d61470a3bf41c27117a847ee)
- [tcpc_driver_api::get_src_ctrl](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a895901166eeedac50b48918b436ee6bc)
- [tcpc_driver_api::set_alert_handler_cb](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#a8cc43981c1047cc92dbed8843e6f72f0)
- [tcpc_driver_api::sop_prime_enable](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#aa1b59f3aa1ccc8684445f119d4ea75aa)
- [tcpc_driver_api::transmit_data](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#aaa0956282b1b9cf3e41dc45a9f31e073)
- [tcpc_driver_api::set_debug_accessory](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#aaa2b59daf061965dc6ed6cb7a42b684f)
- [tcpc_driver_api::set_bist_test_mode](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#ab5ef4ec81c532dc054b53058b199a7e0)
- [tcpc_driver_api::set_rx_enable](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#ac79a47b9a94fb4481bc9ecdba86b898d)
- [tcpc_driver_api::set_snk_ctrl](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#aca835517376e241345d05bf66119cb6c)
- [tcpc_driver_api::mask_status_register](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#adc65471e8ae2b106575b25d5c30653dd)
- [tcpc_driver_api::vconn_discharge](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#adc8f34eefe17f59953bba2029fcaa4bc)
- [tcpc_driver_api::init](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#ae4cf25f8c0c5f0020c0d57b9dc6bdb4c)
- [tcpc_driver_api::set_roles](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#ae5c9719810866d0fcc03f329c84b3a58)
- [tcpc_driver_api::set_vconn_discharge_cb](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#af04de5dd092efeb32a23e21cda5033c0)
- [tcpc_driver_api::get_cc](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md#af483dc0041006ad9bb717ffc4b570978)

---

[上一章](P891_usbc_tc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P893_usbc_vbus.h_源码浏览.md)
