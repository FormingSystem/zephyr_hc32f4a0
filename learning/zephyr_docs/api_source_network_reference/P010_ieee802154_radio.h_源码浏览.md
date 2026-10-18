---
id: learning.zephyr-docs.api-source-network-reference.page-10
title: ieee802154_radio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_ieee802154\_radio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h.html)。

## 10.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00065"></a>
<a id="l00070"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00093"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00134"></a>
<a id="foldopen00169"></a>
<a id="l00169"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="foldopen00235"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="foldopen00244"></a>
<a id="l00244"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="foldopen00282"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00302"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="foldopen00313"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00330"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00347"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00370"></a>
<a id="l00372"></a>
<a id="l00374"></a>
<a id="l00376"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="foldopen00381"></a>
<a id="l00381"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="foldopen00399"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="foldopen00404"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00415"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00423"></a>
<a id="l00428"></a>
<a id="foldopen00437"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="foldopen00522"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="foldopen00531"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="l00535"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="foldopen00547"></a>
<a id="l00547"></a>
<a id="l00549"></a>
<a id="l00551"></a>
<a id="l00553"></a>
<a id="l00555"></a>
<a id="l00557"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="foldopen00572"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00575"></a>
<a id="l00577"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="foldopen00587"></a>
<a id="l00587"></a>
<a id="l00589"></a>
<a id="l00591"></a>
<a id="l00593"></a>
<a id="l00595"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="foldopen00601"></a>
<a id="l00601"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="foldopen00644"></a>
<a id="l00644"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="foldopen00655"></a>
<a id="l00655"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l01063"></a>
<a id="l01064"></a>
<a id="l01092"></a>
<a id="l01093"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01102"></a>
<a id="l01103"></a>
<a id="l01105"></a>
<a id="l01106"></a>
<a id="l01107"></a>
<a id="l01112"></a>
<a id="l01113"></a>
<a id="l01122"></a>
<a id="l01123"></a>
<a id="foldopen01125"></a>
<a id="l01125"></a>
<a id="l01127"></a>
<a id="l01129"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="l01132"></a>
<a id="l01133"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01137"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01140"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01145"></a>
<a id="l01146"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01151"></a>
<a id="l01152"></a>
<a id="l01154"></a>
<a id="l01155"></a>
<a id="l01170"></a>
<a id="l01171"></a>
<a id="l01173"></a>
<a id="l01174"></a>
<a id="l01176"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01200"></a>
<a id="l01201"></a>
<a id="l01205"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01221"></a>
<a id="l01231"></a>
<a id="l01232"></a>
<a id="l01242"></a>
<a id="l01243"></a>
<a id="l01253"></a>
<a id="l01254"></a>
<a id="l01262"></a>
<a id="l01263"></a>
<a id="l01264"></a>
<a id="l01265"></a>
<a id="l01266"></a>
<a id="foldopen01273"></a>
<a id="l01273"></a>
<a id="l01278"></a>
<a id="l01279"></a>
<a id="l01285"></a>
<a id="l01286"></a>
<a id="l01292"></a>
<a id="l01293"></a>
<a id="l01295"></a>
<a id="l01296"></a>
<a id="l01300"></a>
<a id="l01301"></a>
<a id="l01302"></a>
<a id="foldopen01316"></a>
<a id="l01316"></a>
<a id="l01317"></a>
<a id="l01318"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01337"></a>
<a id="l01338"></a>
<a id="l01374"></a>
<a id="l01375"></a>
<a id="l01376"></a>
<a id="l01377"></a>
<a id="l01378"></a>
<a id="l01390"></a>
<a id="l01391"></a>
<a id="l01392"></a>
<a id="l01393"></a>
<a id="foldopen01408"></a>
<a id="l01408"></a>
<a id="l01409"></a>
<a id="l01410"></a>
<a id="l01411"></a>
<a id="l01412"></a>
<a id="l01413"></a>
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
<a id="foldopen01503"></a>
<a id="l01503"></a>
<a id="l01511"></a>
<a id="l01512"></a>
<a id="l01524"></a>
<a id="l01525"></a>
<a id="l01542"></a>
<a id="l01543"></a>
<a id="l01564"></a>
<a id="l01565"></a>
<a id="l01589"></a>
<a id="l01590"></a>
<a id="l01591"></a>
<a id="l01592"></a>
<a id="l01593"></a>
<a id="l01610"></a>
<a id="l01611"></a>
<a id="l01704"></a>
<a id="l01705"></a>
<a id="l01706"></a>
<a id="l01728"></a>
<a id="l01729"></a>
<a id="l01752"></a>
<a id="l01753"></a>
<a id="l01754"></a>
<a id="l01774"></a>
<a id="l01775"></a>
<a id="l01797"></a>
<a id="l01798"></a>
<a id="l01799"></a>
<a id="l01835"></a>
<a id="l01836"></a>
<a id="l01837"></a>
<a id="l01838"></a>
<a id="l01863"></a>
<a id="l01864"></a>
<a id="l01865"></a>
<a id="l01866"></a>
<a id="l01884"></a>
<a id="l01885"></a>
<a id="l01906"></a>
<a id="l01907"></a>
<a id="l01929"></a>
<a id="l01930"></a>
<a id="l01931"></a>
<a id="l01932"></a>
<a id="l01933"></a>
<a id="l01934"></a>
<a id="l01935"></a>
<a id="l01936"></a>
<a id="l01937"></a>
<a id="l01938"></a>
<a id="l01940"></a>
<a id="l01945"></a>
<a id="l01947"></a>
<a id="l01949"></a>
<a id="foldopen01960"></a>
<a id="l01960"></a>
<a id="l01961"></a>
<a id="l01962"></a>
<a id="l01963"></a>
<a id="l01964"></a>
<a id="l01966"></a>
<a id="l01971"></a>
<a id="l01972"></a>
<a id="l01973"></a>
<a id="l01974"></a>
<a id="l01997"></a>
<a id="l01998"></a>
<a id="l02012"></a>
<a id="l02013"></a>
<a id="l02014"></a>
<a id="l02015"></a>
<a id="l02016"></a>
<a id="l02017"></a>
<a id="l02019"></a>
<a id="l02020"></a>
<a id="l02021"></a>
<a id="l02022"></a>
<a id="l02023"></a>
<a id="l02027"></a>
<a id="l02028"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__ieee802154__driver_html_ga04febbd15f9e6f6540d711ada5a4a1c8"></a>
<a id="agroup__ieee802154__driver_html_ga13610aeef06372bc47d84464537fdded"></a>
<a id="agroup__ieee802154__driver_html_ga3491982b677941442d904ce69fce7c5e"></a>
<a id="agroup__ieee802154__driver_html_ga34aecc5996174a812b295a3a4693ad09"></a>
<a id="agroup__ieee802154__driver_html_ga68e1f89571ccbefef61a5496577337fc"></a>
<a id="agroup__ieee802154__driver_html_ga8219b80b8b179fc3a2ffac0dfdfb4e4b"></a>
<a id="agroup__ieee802154__driver_html_ga8c9ab3cecefe641a25f003eb6d014fc5"></a>
<a id="agroup__ieee802154__driver_html_gaa1971591e72866d0f3f0d4db2931e25a"></a>
<a id="agroup__ieee802154__driver_html_gab2bee8752291e082cb277145cef1225d"></a>
<a id="agroup__ieee802154__driver_html_gab593bc6640ddea23c951982ca2f4c0bf"></a>
<a id="agroup__ieee802154__driver_html_gacabc7386bea701373dfb36ab65bd36a9"></a>
<a id="agroup__ieee802154__driver_html_gad2a4cb5df84ffe20b83fc54dc9bcfc91"></a>
<a id="agroup__ieee802154__driver_html_gaf4deddd3f23ebfd65fa47c5d62634430"></a>
<a id="agroup__ieee802154__driver_html_gaf5d7bdde2a9774f9d90604a6e203bb07"></a>
<a id="agroup__ieee802154__driver_html_gaf69d2b65aa46ec4483c6bab419413ba5"></a>
<a id="agroup__ieee802154__driver_html_gaf99cda89c29df3c0088fc57ec09cbcd4"></a>
<a id="agroup__ieee802154__driver_html_gga04febbd15f9e6f6540d711ada5a4a1c8a103f6683ff71f4f7248ee1a0d09d6be4"></a>
<a id="agroup__ieee802154__driver_html_gga04febbd15f9e6f6540d711ada5a4a1c8a5baa9dd683a717f7fbdfc5ab85935a3b"></a>
<a id="agroup__ieee802154__driver_html_gga04febbd15f9e6f6540d711ada5a4a1c8a7bd7daaf3823d86ed48782138b671e57"></a>
<a id="agroup__ieee802154__driver_html_gga04febbd15f9e6f6540d711ada5a4a1c8a7e180466cd23edf5f030c3fbefadf2d1"></a>
<a id="agroup__ieee802154__driver_html_gga04febbd15f9e6f6540d711ada5a4a1c8a7ff9cfcc5e4dfc2bf7abe1860a39410f"></a>
<a id="agroup__ieee802154__driver_html_gga04febbd15f9e6f6540d711ada5a4a1c8ad584824b4813626d04a85499371b9c32"></a>
<a id="agroup__ieee802154__driver_html_gga13610aeef06372bc47d84464537fddeda2b24236d3531cab7d21673d065b7c29e"></a>
<a id="agroup__ieee802154__driver_html_gga13610aeef06372bc47d84464537fddeda4369c745ed378d8273a1014322f3029a"></a>
<a id="agroup__ieee802154__driver_html_gga13610aeef06372bc47d84464537fddeda9dc3c58366502aeab04a208937536369"></a>
<a id="agroup__ieee802154__driver_html_gga13610aeef06372bc47d84464537fddedacb66442cf2a5e4c539b6b7edf8419be1"></a>
<a id="agroup__ieee802154__driver_html_gga13610aeef06372bc47d84464537fddedad920ae285cdcc2a4d59f7c23e29dce27"></a>
<a id="agroup__ieee802154__driver_html_gga13610aeef06372bc47d84464537fddedadf9230e6ef62ce66129bfe24f537c88a"></a>
<a id="agroup__ieee802154__driver_html_gga13610aeef06372bc47d84464537fddedae6c88efd301a449b1a31e8aedf4e30ca"></a>
<a id="agroup__ieee802154__driver_html_gga3491982b677941442d904ce69fce7c5eaacd61f4466f1ef926adc9e1afe6c1648"></a>
<a id="agroup__ieee802154__driver_html_gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273"></a>
<a id="agroup__ieee802154__driver_html_gga3491982b677941442d904ce69fce7c5eaf7ed46b9d13a232a2ea6b650514eea3d"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a2b8dbb8a7de613b8ca81513242958837"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a61df14aeb348cfc694d539b506dc23ac"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09aa34da77f0966ff5a0e8ac73ed68554a8"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6"></a>
<a id="agroup__ieee802154__driver_html_ggaa1971591e72866d0f3f0d4db2931e25aa2fa1ac98a3b870fcf6e85e7ec82cfbe9"></a>
<a id="agroup__ieee802154__driver_html_ggaa1971591e72866d0f3f0d4db2931e25aa928a93b536c6408b3d77aa329c274fe8"></a>
<a id="agroup__ieee802154__driver_html_ggaa1971591e72866d0f3f0d4db2931e25aab44cc830999926a5d232aedabef52653"></a>
<a id="agroup__ieee802154__driver_html_ggaa1971591e72866d0f3f0d4db2931e25aac6dbb68674e7594fd4cd69bbe4ea60de"></a>
<a id="agroup__ieee802154__driver_html_ggaa1971591e72866d0f3f0d4db2931e25aade18e03611339f5f7ec4fdcdee409c21"></a>
<a id="agroup__ieee802154__driver_html_ggab2bee8752291e082cb277145cef1225da1e23f1ad3f9d0832fd4d67fc00fd8eb5"></a>
<a id="agroup__ieee802154__driver_html_ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e"></a>
<a id="agroup__ieee802154__driver_html_ggab2bee8752291e082cb277145cef1225da51a0e7cb482447779634062655a1ec47"></a>
<a id="agroup__ieee802154__driver_html_ggab2bee8752291e082cb277145cef1225da6904c3c7f53d46c5c8b41dd1a82b2650"></a>
<a id="agroup__ieee802154__driver_html_ggab2bee8752291e082cb277145cef1225da9a7b8ba25603b72aecbf7f66abf26508"></a>
<a id="agroup__ieee802154__driver_html_ggab2bee8752291e082cb277145cef1225daa389aeccad62a0516678564e68fcd595"></a>
<a id="agroup__ieee802154__driver_html_ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2"></a>
<a id="agroup__ieee802154__driver_html_ggab593bc6640ddea23c951982ca2f4c0bfa012874ab4d234bbeb2954756cf2dc9d6"></a>
<a id="agroup__ieee802154__driver_html_ggab593bc6640ddea23c951982ca2f4c0bfac7c839b7c0649d6151f90ff1d51ae417"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9a02a17ea787e99528b2a6a8f5107f2544"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9a1f33467ec7659ef411b08f7a23663311"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9a371a12ec5d762b03058fb2532fa04e45"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9a56dd4ae42595ef0edb109c729e333b08"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9a5776e0160927b83f4e4e8d6479aaf804"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9a68b93381ddc1184ff0ed13456cf4b6a8"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9a6d4023088a3607c072acebd3940340c7"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9a6ea456573a6ff8aed348a9dc547b2db7"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9a6f71c162be118b0c2edce139753c867e"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9a72b17a977aeb6792f7d2016117f4b2f9"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9a996b529c9c277d6d653d0e0ffb8b2902"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9aa0ab080c8cdac42dbf80622d075854dc"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9aad0644244fb5b6cba5a295e246722e94"></a>
<a id="agroup__ieee802154__driver_html_ggacabc7386bea701373dfb36ab65bd36a9ac13dda08becd3d4799d45ef02f774cc1"></a>
<a id="agroup__ieee802154__driver_html_ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a"></a>
<a id="agroup__ieee802154__driver_html_ggaf4deddd3f23ebfd65fa47c5d62634430aa0830214987de7a89297777c0d1004de"></a>
<a id="agroup__ieee802154__driver_html_ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d"></a>
<a id="agroup__ieee802154__driver_html_ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511"></a>
<a id="agroup__ieee802154__driver_html_ggaf4deddd3f23ebfd65fa47c5d62634430ad90b4a118866c4942ef6f6a8ae56eb3f"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4a0ea21cab335dd9082feb2d08be0eb5fa"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4a179ad073a5bd34e4e4af587d07ca3f73"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4a2ee53f11e1ed6853e1f5d9dfe7d7bdf7"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4a435d032f42d509bd78a992de6e4d7b1d"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4a4adb33f2ca81a24244dead6b379cd916"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4a68ae68c83a87f0efc25f74edd80c4600"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4a752472a994bdcbdf9cdf86deb0231849"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4ab383a932c0ac9deece68f02210089119"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4ac1e00966043e5884c4cbd65fb26f0c0b"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03"></a>
<a id="agroup__ieee802154__driver_html_ggaf99cda89c29df3c0088fc57ec09cbcd4afd09f329a708d00f1384a50c59ddde27"></a>
<a id="agroup__net__core_html_ga8e5393f3bdd85491f221324e637c3896"></a>
<a id="agroup__net__time_html_gaf1da332e3909fca30de991cc2f950e56"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga03e689f378f643d16ea7537918528a48"></a>
<a id="aieee802154_8h_html"></a>
<a id="aieee802154__ie_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="anet__time_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructdevice_html"></a>
<a id="astructieee802154__attr__value_html"></a>
<a id="astructieee802154__attr__value_html_a75913597f93de1a80f96bb9dc32d38df"></a>
<a id="astructieee802154__attr__value_html_a840d2f3a2502f87806ef79c6926f73f0"></a>
<a id="astructieee802154__attr__value_html_af157805fb8acffb634cba4b37472bdb3"></a>
<a id="astructieee802154__config_html"></a>
<a id="astructieee802154__config_html_a03d6ec1a371312961f3a1ee42e113bbf"></a>
<a id="astructieee802154__config_html_a078ec577af3d170781ed770c80c54b72"></a>
<a id="astructieee802154__config_html_a1558e71a1d5ab74990964ff4deabbdb7"></a>
<a id="astructieee802154__config_html_a272cfd864c7d47c6f06f26871ce07fb6"></a>
<a id="astructieee802154__config_html_a39c06e32cb4a74b4d8a9864f714e8c93"></a>
<a id="astructieee802154__config_html_a3a5e597e53bfcc9e3bed8bac2edb74d2"></a>
<a id="astructieee802154__config_html_a5106a759148ec20c6c6c83a2581c9e88"></a>
<a id="astructieee802154__config_html_a5343dec0de835943c0bef2c2d603a91d"></a>
<a id="astructieee802154__config_html_a55823097d62a69d0c92dc70fb4ff1dd5"></a>
<a id="astructieee802154__config_html_a673f5cceb6439bc1c3527c62062151d1"></a>
<a id="astructieee802154__config_html_a8124aed4a4af36c0e21fd8f1b1c97e3e"></a>
<a id="astructieee802154__config_html_a86b72101b0b21622f3cc8a2b3877e356"></a>
<a id="astructieee802154__config_html_a8971a91be8748bd45027fcb730b99639"></a>
<a id="astructieee802154__config_html_a8b7d4804cd051d69f3602f35cb4a8630"></a>
<a id="astructieee802154__config_html_a8f7efaa743e070479632d139f0fc57c0"></a>
<a id="astructieee802154__config_html_a942c0d4fb244c7256530536dc132a727"></a>
<a id="astructieee802154__config_html_aa27066dd9e54dab6795332b7413670f5"></a>
<a id="astructieee802154__config_html_aadc2714bf31484cce071e9ef7b9a4007"></a>
<a id="astructieee802154__config_html_aafb11c4130ff39e5c40dfe5d32c0d4e7"></a>
<a id="astructieee802154__config_html_ab27a654a0d53f268199e95dc21e18fd4"></a>
<a id="astructieee802154__config_html_ab36833b4311b03f08f67290f4edd8e41"></a>
<a id="astructieee802154__config_html_ad139acde94327d4b8ceb76760751521d"></a>
<a id="astructieee802154__config_html_ad9361f9ba1652e46d0be25e0de39afdf"></a>
<a id="astructieee802154__config_html_afa1d230e1059013a7a99e737da3a0266"></a>
<a id="astructieee802154__filter_html"></a>
<a id="astructieee802154__filter_html_a16a1779ff43accda31bba35b9bdd61c3"></a>
<a id="astructieee802154__filter_html_a40f77239924af29d40f7595e23475e9b"></a>
<a id="astructieee802154__filter_html_a636ec85ca79b2880de51ed93f6788909"></a>
<a id="astructieee802154__key_html"></a>
<a id="astructieee802154__key_html_a01b760f3e622ad0a60888170e5688b9d"></a>
<a id="astructieee802154__key_html_a357419c2d16a527a2417f4eded566aac"></a>
<a id="astructieee802154__key_html_a5ca5258422db14b99fd37e7126cfc85d"></a>
<a id="astructieee802154__key_html_a732a2a89e74139bd1d8e9b358c0306c7"></a>
<a id="astructieee802154__key_html_ae0a1e354b5718e8135fb6198ea12276a"></a>
<a id="astructieee802154__phy__channel__range_html"></a>
<a id="astructieee802154__phy__channel__range_html_a78af593807753dbfcfce88166f4c1f58"></a>
<a id="astructieee802154__phy__channel__range_html_aec90e36227a7d9cc1dfc18231341dd03"></a>
<a id="astructieee802154__phy__supported__channels_html"></a>
<a id="astructieee802154__phy__supported__channels_html_a73ccabf887b567a0ce3ddc5f8a3eeed1"></a>
<a id="astructieee802154__phy__supported__channels_html_a8fb56a7fc6be96035cf4b51891582da9"></a>
<a id="astructieee802154__radio__api_html"></a>
<a id="astructieee802154__radio__api_html_a01fc17f85f2be33877a9347f59a84c54"></a>
<a id="astructieee802154__radio__api_html_a09a4b5df81822845f718952c6029442c"></a>
<a id="astructieee802154__radio__api_html_a0b3e0ed1385dd428c861e08c79849ef4"></a>
<a id="astructieee802154__radio__api_html_a0e4d57dc3a53299ddedf2140e172103d"></a>
<a id="astructieee802154__radio__api_html_a2cbbd0e64fae28f748bb3e4d654a92bf"></a>
<a id="astructieee802154__radio__api_html_a70139acec22642c1fc09f2323c383fe6"></a>
<a id="astructieee802154__radio__api_html_a75cfcfe2b9e69c2e4af53f00c8294b36"></a>
<a id="astructieee802154__radio__api_html_a829a0d59fdcda5b6cb029ef1334a6b8b"></a>
<a id="astructieee802154__radio__api_html_a9acaf4810bd5d3b026cc381bff301071"></a>
<a id="astructieee802154__radio__api_html_a9ad27a2ff0a839dc5b9a4e6317cc59b1"></a>
<a id="astructieee802154__radio__api_html_aa9502e0e014a8d05ffe235567e8c98f3"></a>
<a id="astructieee802154__radio__api_html_aa955462d8c6950dc4b5935973f4575d8"></a>
<a id="astructieee802154__radio__api_html_ae4a3ef40a5b8031c868d72ead163c97d"></a>
<a id="astructieee802154__radio__api_html_aeeab6dfcde08af23357ea40f8af68f66"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_ac6eef59915e7ce167442fdacbbfb5e56"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation.
 * Copyright (c) 2023 F. Grandel, Zephyr Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_IEEE802154_RADIO_H_
#define ZEPHYR_INCLUDE_NET_IEEE802154_RADIO_H_

#include <zephyr/device.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_pkt.h>
#include <zephyr/net/net_time.h>
#include <zephyr/net/ieee802154.h>
#include <zephyr/net/ieee802154_ie.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif



#define IEEE802154_PHY_SYMBOLS_PER_SECOND(symbol_period_ns) (NSEC_PER_SEC / symbol_period_ns)




#define IEEE802154_MAC_A_BASE_SLOT_DURATION 60U

#define IEEE802154_MAC_A_NUM_SUPERFRAME_SLOTS 16U

#define IEEE802154_MAC_A_BASE_SUPERFRAME_DURATION                                                  \
        (IEEE802154_MAC_A_BASE_SLOT_DURATION * IEEE802154_MAC_A_NUM_SUPERFRAME_SLOTS)

#define IEEE802154_MAC_A_UNIT_BACKOFF_PERIOD(turnaround_time)                                      \
        (turnaround_time + IEEE802154_PHY_A_CCA_TIME)

#define IEEE802154_MAC_RESPONSE_WAIT_TIME_DEFAULT 32U




enum ieee802154_phy_channel_page {
        IEEE802154_ATTR_PHY_CHANNEL_PAGE_ZERO_OQPSK_2450_BPSK_868_915 = BIT(0),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_ONE_DEPRECATED = BIT(1),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_TWO_OQPSK_868_915 = BIT(2),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_THREE_CSS = BIT(3),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_FOUR_HRP_UWB = BIT(4),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_FIVE_OQPSK_780 = BIT(5),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_SIX_RESERVED = BIT(6),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_SEVEN_MSK = BIT(7),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_EIGHT_LRP_UWB = BIT(8),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_NINE_SUN_PREDEFINED = BIT(9),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_TEN_SUN_FSK_GENERIC = BIT(10),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_ELEVEN_OQPSK_2380 = BIT(11),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_TWELVE_LECIM = BIT(12),

        IEEE802154_ATTR_PHY_CHANNEL_PAGE_THIRTEEN_RCC = BIT(13),
};

struct ieee802154_phy_channel_range {
        uint16_t from_channel;
        uint16_t to_channel;
};

struct ieee802154_phy_supported_channels {
        const struct ieee802154_phy_channel_range *const ranges;

        const uint8_t num_ranges;
};

#define IEEE802154_DEFINE_PHY_SUPPORTED_CHANNELS(drv_attr, from, to)                               \
        static const struct {                                                                      \
                const struct ieee802154_phy_channel_range phy_channel_range;                       \
                const struct ieee802154_phy_supported_channels phy_supported_channels;             \
        } drv_attr = {                                                                             \
                .phy_channel_range = {.from_channel = (from), .to_channel = (to)},                 \
                .phy_supported_channels =                                                          \
                        {                                                                          \
                                .ranges = &drv_attr.phy_channel_range,                             \
                                .num_ranges = 1U,                                                  \
                        },                                                                         \
        }




#define IEEE802154_PHY_A_TURNAROUND_TIME_DEFAULT 12U

#define IEEE802154_PHY_A_TURNAROUND_TIME_1MS(symbol_period_ns)                                     \
        DIV_ROUND_UP(NSEC_PER_MSEC, symbol_period_ns)

#define IEEE802154_PHY_A_CCA_TIME 8U





#define IEEE802154_PHY_OQPSK_868MHZ_SYMBOL_PERIOD_NS         40000LL

#define IEEE802154_PHY_OQPSK_780_TO_2450MHZ_SYMBOL_PERIOD_NS 16000LL




#define IEEE802154_PHY_BPSK_868MHZ_SYMBOL_PERIOD_NS 50000LL

#define IEEE802154_PHY_BPSK_915MHZ_SYMBOL_PERIOD_NS 25000LL




#define IEEE802154_PHY_HRP_UWB_PRF4_TPSYM_SYMBOL_PERIOD_NS  3974.36F
#define IEEE802154_PHY_HRP_UWB_PRF16_TPSYM_SYMBOL_PERIOD_NS 993.59F
#define IEEE802154_PHY_HRP_UWB_PRF64_TPSYM_SYMBOL_PERIOD_NS 1017.63F
#define IEEE802154_PHY_HRP_UWB_ERDEV_TPSYM_SYMBOL_PERIOD_NS 729.17F

enum ieee802154_phy_hrp_uwb_nominal_prf {
        IEEE802154_PHY_HRP_UWB_PRF_OFF = 0,
        IEEE802154_PHY_HRP_UWB_NOMINAL_4_M = BIT(0),
        IEEE802154_PHY_HRP_UWB_NOMINAL_16_M = BIT(1),
        IEEE802154_PHY_HRP_UWB_NOMINAL_64_M = BIT(2),

        IEEE802154_PHY_HRP_UWB_NOMINAL_64_M_BPRF = BIT(3),
        IEEE802154_PHY_HRP_UWB_NOMINAL_128_M_HPRF = BIT(4),
        IEEE802154_PHY_HRP_UWB_NOMINAL_256_M_HPRF = BIT(5),
};

#define IEEE802154_PHY_HRP_UWB_RDEV                                                                \
        (IEEE802154_PHY_HRP_UWB_NOMINAL_4_M | IEEE802154_PHY_HRP_UWB_NOMINAL_16_M |                \
         IEEE802154_PHY_HRP_UWB_NOMINAL_64_M)

#define IEEE802154_PHY_HRP_UWB_ERDEV                                                               \
        (IEEE802154_PHY_HRP_UWB_NOMINAL_64_M_BPRF | IEEE802154_PHY_HRP_UWB_NOMINAL_128_M_HPRF |    \
         IEEE802154_PHY_HRP_UWB_NOMINAL_256_M_HPRF)




#define IEEE802154_PHY_SUN_FSK_863MHZ_915MHZ_SYMBOL_PERIOD_NS 20000LL

#define IEEE802154_PHY_SUN_FSK_PHR_LEN 2



enum ieee802154_hw_caps {

        /*
         * PHY capabilities
         *
         * The following capabilities describe features of the underlying radio
         * hardware (PHY/L1).
         */

        IEEE802154_HW_ENERGY_SCAN = BIT(0),

        /*
         * MAC offloading capabilities (optional)
         *
         * The following MAC/L2 features may optionally be offloaded to
         * specialized hardware or proprietary driver firmware ("hard MAC").
         *
         * L2 implementations will have to provide a "soft MAC" fallback for
         * these features in case the driver does not support them natively.
         *
         * Note: Some of these offloading capabilities may be mandatory in
         * practice to stay within timing requirements of certain IEEE 802.15.4
         * protocols, e.g. CPUs may not be fast enough to send ACKs within the
         * required delays in the 2.4 GHz band without hard MAC support.
         */

        IEEE802154_HW_FCS = BIT(1),

        IEEE802154_HW_FILTER = BIT(2),

        IEEE802154_HW_PROMISC = BIT(3),

        IEEE802154_HW_CSMA = BIT(4),

        IEEE802154_HW_TX_RX_ACK = BIT(5),

        IEEE802154_HW_RETRANSMISSION = BIT(6),

        IEEE802154_HW_RX_TX_ACK = BIT(7),

        IEEE802154_HW_TXTIME = BIT(8),

        IEEE802154_HW_RXTIME = BIT(9),

        IEEE802154_HW_TX_SEC = BIT(10),

        IEEE802154_RX_ON_WHEN_IDLE = BIT(11),

        IEEE802154_HW_SELECTIVE_TXCHANNEL = BIT(12),

        /* Note: Update also IEEE802154_HW_CAPS_BITS_COMMON_COUNT when changing
         * the ieee802154_hw_caps type.
         */
};

#define IEEE802154_HW_CAPS_BITS_COMMON_COUNT (13)

#define IEEE802154_HW_CAPS_BITS_PRIV_START IEEE802154_HW_CAPS_BITS_COMMON_COUNT

enum ieee802154_filter_type {
        IEEE802154_FILTER_TYPE_IEEE_ADDR,
        IEEE802154_FILTER_TYPE_SHORT_ADDR,
        IEEE802154_FILTER_TYPE_PAN_ID,
        IEEE802154_FILTER_TYPE_SRC_IEEE_ADDR,
        IEEE802154_FILTER_TYPE_SRC_SHORT_ADDR,
};

enum ieee802154_event {
        IEEE802154_EVENT_TX_STARTED,
        IEEE802154_EVENT_RX_FAILED,
        IEEE802154_EVENT_RX_OFF,
};

enum ieee802154_rx_fail_reason {
        IEEE802154_RX_FAIL_NOT_RECEIVED,
        IEEE802154_RX_FAIL_INVALID_FCS,
        IEEE802154_RX_FAIL_ADDR_FILTERED,
        IEEE802154_RX_FAIL_NO_BUFS,
        IEEE802154_RX_FAIL_ABORT,
        IEEE802154_RX_FAIL_OTHER
};

typedef void (*energy_scan_done_cb_t)(const struct device *dev,
                                      int16_t max_ed);

typedef void (*ieee802154_event_cb_t)(const struct device *dev,
                                      enum ieee802154_event evt,
                                      void *event_params);

struct ieee802154_filter {
        union {
                uint8_t *ieee_addr;
                uint16_t short_addr;
                uint16_t pan_id;
        };
};

struct ieee802154_key {
        uint8_t *key_value;
        uint32_t key_frame_counter;
        bool frame_counter_per_key;
        uint8_t key_id_mode;
        uint8_t *key_id;
};

enum ieee802154_tx_mode {
        IEEE802154_TX_MODE_DIRECT,

        IEEE802154_TX_MODE_CCA,

        IEEE802154_TX_MODE_CSMA_CA,

        IEEE802154_TX_MODE_TXTIME,

        IEEE802154_TX_MODE_TXTIME_CCA,

        IEEE802154_TX_MODE_COMMON_COUNT,

        IEEE802154_TX_MODE_PRIV_START = IEEE802154_TX_MODE_COMMON_COUNT,
};

enum ieee802154_fpb_mode {
        IEEE802154_FPB_ADDR_MATCH_THREAD,

        IEEE802154_FPB_ADDR_MATCH_ZIGBEE,
};

enum ieee802154_config_type {
        IEEE802154_CONFIG_AUTO_ACK_FPB,

        IEEE802154_CONFIG_ACK_FPB,

        IEEE802154_CONFIG_PAN_COORDINATOR,

        IEEE802154_CONFIG_PROMISCUOUS,

        IEEE802154_CONFIG_EVENT_HANDLER,

        IEEE802154_CONFIG_MAC_KEYS,

        IEEE802154_CONFIG_FRAME_COUNTER,

        IEEE802154_CONFIG_FRAME_COUNTER_IF_LARGER,

        IEEE802154_CONFIG_RX_SLOT,

        IEEE802154_CONFIG_CSL_PERIOD,

        IEEE802154_CONFIG_EXPECTED_RX_TIME,

        IEEE802154_CONFIG_ENH_ACK_HEADER_IE,

        IEEE802154_CONFIG_RX_ON_WHEN_IDLE,

        IEEE802154_CONFIG_CSMA_CA_BACKOFFS,

        IEEE802154_CONFIG_COMMON_COUNT,

        IEEE802154_CONFIG_PRIV_START = IEEE802154_CONFIG_COMMON_COUNT,
};

#define IEEE802154_CONFIG_RX_SLOT_NONE -1LL

#define IEEE802154_CONFIG_RX_SLOT_OFF  0LL

struct ieee802154_config {
        union {
                struct {
                        bool enabled;
                        enum ieee802154_fpb_mode mode;
                } auto_ack_fpb;

                struct {
                        uint8_t *addr;
                        bool extended;
                        bool enabled;
                } ack_fpb;

                bool pan_coordinator;

                bool promiscuous;

                bool rx_on_when_idle;

                ieee802154_event_cb_t event_handler;

                uint8_t csma_ca_backoffs;

                struct ieee802154_key *mac_keys;

                uint32_t frame_counter;

                struct {
                        net_time_t start;

                        net_time_t duration;

                        uint8_t channel;
                } rx_slot;

                uint32_t csl_period;

                net_time_t expected_rx_time;

                struct {
                        struct ieee802154_header_ie *header_ie;

                        const uint8_t *ext_addr;

                        uint16_t short_addr;

                        bool purge_ie;
                } ack_ie;
        };
};

enum ieee802154_attr {
        IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_PAGES,

        IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES,

        IEEE802154_ATTR_PHY_HRP_UWB_SUPPORTED_PRFS,

        IEEE802154_ATTR_COMMON_COUNT,

        IEEE802154_ATTR_PRIV_START = IEEE802154_ATTR_COMMON_COUNT,
};

struct ieee802154_attr_value {
        union {
                /* TODO: Implement configuration of phyCurrentPage once drivers
                 * need to support channel page switching at runtime.
                 */
                uint32_t phy_supported_channel_pages;

                const struct ieee802154_phy_supported_channels *phy_supported_channels;

                /* TODO: Allow the PRF to be configured for each TX call once
                 * drivers need to support PRF switching at runtime.
                 */
                uint32_t phy_hrp_uwb_supported_nominal_prfs;
        };
};

static inline int ieee802154_attr_get_channel_page_and_range(
        enum ieee802154_attr attr,
        const enum ieee802154_phy_channel_page phy_supported_channel_page,
        const struct ieee802154_phy_supported_channels *phy_supported_channels,
        struct ieee802154_attr_value *value)
{
        switch (attr) {
        case IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_PAGES:
                value->phy_supported_channel_pages = phy_supported_channel_page;
                return 0;

        case IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES:
                value->phy_supported_channels = phy_supported_channels;
                return 0;

        default:
                return -ENOENT;
        }
}

struct ieee802154_radio_api {
        struct net_if_api iface_api;

        enum ieee802154_hw_caps (*get_capabilities)(const struct device *dev);

        int (*cca)(const struct device *dev);

        int (*set_channel)(const struct device *dev, uint16_t channel);

        int (*filter)(const struct device *dev,
                      bool set,
                      enum ieee802154_filter_type type,
                      const struct ieee802154_filter *filter);

        int (*set_txpower)(const struct device *dev, int16_t dbm);

        int (*tx)(const struct device *dev, enum ieee802154_tx_mode mode,
                  struct net_pkt *pkt, struct net_buf *frag);

        int (*start)(const struct device *dev);

        int (*stop)(const struct device *dev);

#if defined(CONFIG_IEEE802154_CARRIER_FUNCTIONS)
        int (*continuous_carrier)(const struct device *dev);

        int (*modulated_carrier)(const struct device *dev, const uint8_t *data);
#endif /* CONFIG_IEEE802154_CARRIER_FUNCTIONS */

        int (*configure)(const struct device *dev,
                         enum ieee802154_config_type type,
                         const struct ieee802154_config *config);

        int (*ed_scan)(const struct device *dev,
                       uint16_t duration,
                       energy_scan_done_cb_t done_cb);

        net_time_t (*get_time)(const struct device *dev);

        uint8_t (*get_sch_acc)(const struct device *dev);

        int (*attr_get)(const struct device *dev,
                        enum ieee802154_attr attr,
                        struct ieee802154_attr_value *value);
};

/* Make sure that the network interface API is properly setup inside
 * IEEE 802.15.4 driver API struct (it is the first one).
 */
BUILD_ASSERT(offsetof(struct ieee802154_radio_api, iface_api) == 0);



#define IEEE802154_AR_FLAG_SET (0x20)

static inline bool ieee802154_is_ar_flag_set(struct net_buf *frag)
{
        return (*frag->data & IEEE802154_AR_FLAG_SET);
}



/* TODO: Fix drivers to either unref the packet before they return NET_OK or to
 * return NET_CONTINUE instead. See note below.
 */
extern enum net_verdict ieee802154_handle_ack(struct net_if *iface, struct net_pkt *pkt);

#ifndef CONFIG_IEEE802154_RAW_MODE
extern void ieee802154_init(struct net_if *iface);
#else
#define ieee802154_init(_iface_)
#endif /* CONFIG_IEEE802154_RAW_MODE */


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_IEEE802154_RADIO_H_ */
```

## 10.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation.。

版权（Copyright）：© 2023 F. Grandel, Zephyr Project。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 439 行

物理层能力（PHY Capabilities）。

下列能力描述底层无线电硬件（Radio Hardware，即 PHY／L1）的特性。

### 注释 3：原第 449 行

媒体访问控制卸载能力（MAC Offloading Capabilities），可选。

下列 MAC／L2 特性可选择卸载到专用硬件或私有驱动固件（“硬 MAC”，Hard MAC）。

如果驱动不原生支持这些特性，二层实现（L2 Implementations）必须提供“软 MAC”（Soft MAC）回退实现。

注意：为满足某些 IEEE 802.15.4 协议的时序要求（Timing Requirements），部分卸载能力在实际使用中可能是必需的。例如，在 2.4 GHz 频段，如果没有硬 MAC 支持，CPU 可能无法足够快地发送确认帧（ACKs）以满足规定延迟。

### 注释 4：原第 510 行

注意：更改 `ieee802154_hw_caps` 类型时，也要更新 `IEEE802154_HW_CAPS_BITS_COMMON_COUNT`。

### 注释 5：原第 1318 行

待办（TODO）：当驱动需要支持运行时切换信道页（Channel Page）时，实现 `phyCurrentPage` 的配置。

### 注释 6：原第 1376 行

待办（TODO）：当驱动需要支持运行时切换脉冲重复频率（PRF）时，允许为每次发送调用（TX Call）配置 PRF。

### 注释 7：原第 1798 行

条件编译配置（Configuration）标记：`CONFIG_IEEE802154_CARRIER_FUNCTIONS`。

### 注释 8：原第 1934 行

确保网络接口 API（Network Interface API）已在 IEEE 802.15.4 驱动 API 结构体中正确设置；它是其中第一个成员。

### 注释 9：原第 1972 行

待办（TODO）：修复驱动，使其在返回 `NET_OK` 前释放数据包引用（Unref the Packet），或改为返回 `NET_CONTINUE`。参见下文注释。

### 注释 10：原第 2016 行

条件编译配置（Configuration）标记：`CONFIG_IEEE802154_RAW_MODE`。

### 注释 11：原第 2028 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_IEEE802154_RADIO_H_`。

## 10.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [zephyr/net/net_time.h](https://docs.zephyrproject.org/latest/doxygen/html/net__time_8h.html)
- [zephyr/net/ieee802154.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154_8h.html)
- [zephyr/net/ieee802154_ie.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [ieee802154_phy_channel_page](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gacabc7386bea701373dfb36ab65bd36a9)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_ZERO_OQPSK_2450_BPSK_868_915](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a72b17a977aeb6792f7d2016117f4b2f9)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_ONE_DEPRECATED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a371a12ec5d762b03058fb2532fa04e45)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_TWO_OQPSK_868_915](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a5776e0160927b83f4e4e8d6479aaf804)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_THREE_CSS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a6f71c162be118b0c2edce139753c867e)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_FOUR_HRP_UWB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a68b93381ddc1184ff0ed13456cf4b6a8)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_FIVE_OQPSK_780](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a6ea456573a6ff8aed348a9dc547b2db7)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_SIX_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9ac13dda08becd3d4799d45ef02f774cc1)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_SEVEN_MSK](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a1f33467ec7659ef411b08f7a23663311)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_EIGHT_LRP_UWB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9aa0ab080c8cdac42dbf80622d075854dc)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_NINE_SUN_PREDEFINED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a996b529c9c277d6d653d0e0ffb8b2902)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_TEN_SUN_FSK_GENERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a02a17ea787e99528b2a6a8f5107f2544)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_ELEVEN_OQPSK_2380](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9aad0644244fb5b6cba5a295e246722e94)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_TWELVE_LECIM](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a6d4023088a3607c072acebd3940340c7)
- [IEEE802154_ATTR_PHY_CHANNEL_PAGE_THIRTEEN_RCC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggacabc7386bea701373dfb36ab65bd36a9a56dd4ae42595ef0edb109c729e333b08)
- [ieee802154_phy_channel_range](../network_core_model_reference/P039_ieee802154_phy_channel_range_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [from_channel](../network_core_model_reference/P039_ieee802154_phy_channel_range_结构体.md#aec90e36227a7d9cc1dfc18231341dd03)
- [to_channel](../network_core_model_reference/P039_ieee802154_phy_channel_range_结构体.md#a78af593807753dbfcfce88166f4c1f58)
- [ieee802154_phy_supported_channels](../network_core_model_reference/P040_ieee802154_phy_supported_channels_结构体.md)
- [ranges](../network_core_model_reference/P040_ieee802154_phy_supported_channels_结构体.md#a73ccabf887b567a0ce3ddc5f8a3eeed1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [num_ranges](../network_core_model_reference/P040_ieee802154_phy_supported_channels_结构体.md#a8fb56a7fc6be96035cf4b51891582da9)
- [ieee802154_phy_hrp_uwb_nominal_prf](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga13610aeef06372bc47d84464537fdded)
- [IEEE802154_PHY_HRP_UWB_PRF_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddeda4369c745ed378d8273a1014322f3029a)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_4_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddeda9dc3c58366502aeab04a208937536369)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_16_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedadf9230e6ef62ce66129bfe24f537c88a)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_64_M](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddeda2b24236d3531cab7d21673d065b7c29e)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_64_M_BPRF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedad920ae285cdcc2a4d59f7c23e29dce27)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_128_M_HPRF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedae6c88efd301a449b1a31e8aedf4e30ca)
- [IEEE802154_PHY_HRP_UWB_NOMINAL_256_M_HPRF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga13610aeef06372bc47d84464537fddedacb66442cf2a5e4c539b6b7edf8419be1)
- [ieee802154_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf99cda89c29df3c0088fc57ec09cbcd4)
- [IEEE802154_HW_ENERGY_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a179ad073a5bd34e4e4af587d07ca3f73)
- [IEEE802154_HW_FCS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a0ea21cab335dd9082feb2d08be0eb5fa)
- [IEEE802154_HW_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4afd09f329a708d00f1384a50c59ddde27)
- [IEEE802154_HW_PROMISC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a4adb33f2ca81a24244dead6b379cd916)
- [IEEE802154_HW_CSMA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a2ee53f11e1ed6853e1f5d9dfe7d7bdf7)
- [IEEE802154_HW_TX_RX_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4ab383a932c0ac9deece68f02210089119)
- [IEEE802154_HW_RETRANSMISSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a752472a994bdcbdf9cdf86deb0231849)
- [IEEE802154_HW_RX_TX_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4aec16c4d418117de2d106e84297568b03)
- [IEEE802154_HW_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a435d032f42d509bd78a992de6e4d7b1d)
- [IEEE802154_HW_RXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a68ae68c83a87f0efc25f74edd80c4600)
- [IEEE802154_HW_TX_SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4a7924c3d5bfe6dceeb2e8caa6df7edecb)
- [IEEE802154_RX_ON_WHEN_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4ac1e00966043e5884c4cbd65fb26f0c0b)
- [IEEE802154_HW_SELECTIVE_TXCHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e)
- [ieee802154_filter_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaa1971591e72866d0f3f0d4db2931e25a)
- [IEEE802154_FILTER_TYPE_IEEE_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aa928a93b536c6408b3d77aa329c274fe8)
- [IEEE802154_FILTER_TYPE_SHORT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aa2fa1ac98a3b870fcf6e85e7ec82cfbe9)
- [IEEE802154_FILTER_TYPE_PAN_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aab44cc830999926a5d232aedabef52653)
- [IEEE802154_FILTER_TYPE_SRC_IEEE_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aade18e03611339f5f7ec4fdcdee409c21)
- [IEEE802154_FILTER_TYPE_SRC_SHORT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaa1971591e72866d0f3f0d4db2931e25aac6dbb68674e7594fd4cd69bbe4ea60de)
- [ieee802154_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga3491982b677941442d904ce69fce7c5e)
- [IEEE802154_EVENT_TX_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga3491982b677941442d904ce69fce7c5eaacd61f4466f1ef926adc9e1afe6c1648)
- [IEEE802154_EVENT_RX_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga3491982b677941442d904ce69fce7c5eaef51197ca09befaee8cdfa2cde107273)
- [IEEE802154_EVENT_RX_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga3491982b677941442d904ce69fce7c5eaf7ed46b9d13a232a2ea6b650514eea3d)
- [ieee802154_rx_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga04febbd15f9e6f6540d711ada5a4a1c8)
- [IEEE802154_RX_FAIL_NOT_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8ad584824b4813626d04a85499371b9c32)
- [IEEE802154_RX_FAIL_INVALID_FCS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a103f6683ff71f4f7248ee1a0d09d6be4)
- [IEEE802154_RX_FAIL_ADDR_FILTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a7ff9cfcc5e4dfc2bf7abe1860a39410f)
- [IEEE802154_RX_FAIL_NO_BUFS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a7e180466cd23edf5f030c3fbefadf2d1)
- [IEEE802154_RX_FAIL_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a7bd7daaf3823d86ed48782138b671e57)
- [IEEE802154_RX_FAIL_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga04febbd15f9e6f6540d711ada5a4a1c8a5baa9dd683a717f7fbdfc5ab85935a3b)
- [energy_scan_done_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga8c9ab3cecefe641a25f003eb6d014fc5)
- [device](../device_reference/P002_设备对象结构.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [ieee802154_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga8219b80b8b179fc3a2ffac0dfdfb4e4b)
- [ieee802154_filter](../network_core_model_reference/P017_ieee802154_filter_结构体.md)
- [ieee_addr](../network_core_model_reference/P017_ieee802154_filter_结构体.md#a636ec85ca79b2880de51ed93f6788909)
- [short_addr](../network_core_model_reference/P017_ieee802154_filter_结构体.md#a16a1779ff43accda31bba35b9bdd61c3)
- [pan_id](../network_core_model_reference/P017_ieee802154_filter_结构体.md#a40f77239924af29d40f7595e23475e9b)
- [ieee802154_key](../network_core_model_reference/P032_ieee802154_key_结构体.md)
- [key_value](../network_core_model_reference/P032_ieee802154_key_结构体.md#a01b760f3e622ad0a60888170e5688b9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [key_frame_counter](../network_core_model_reference/P032_ieee802154_key_结构体.md#a357419c2d16a527a2417f4eded566aac)
- [frame_counter_per_key](../network_core_model_reference/P032_ieee802154_key_结构体.md#a5ca5258422db14b99fd37e7126cfc85d)
- [key_id_mode](../network_core_model_reference/P032_ieee802154_key_结构体.md#a732a2a89e74139bd1d8e9b358c0306c7)
- [key_id](../network_core_model_reference/P032_ieee802154_key_结构体.md#ae0a1e354b5718e8135fb6198ea12276a)
- [ieee802154_tx_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gab2bee8752291e082cb277145cef1225d)
- [IEEE802154_TX_MODE_DIRECT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da6904c3c7f53d46c5c8b41dd1a82b2650)
- [IEEE802154_TX_MODE_CCA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da1e23f1ad3f9d0832fd4d67fc00fd8eb5)
- [IEEE802154_TX_MODE_CSMA_CA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da51a0e7cb482447779634062655a1ec47)
- [IEEE802154_TX_MODE_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da9a7b8ba25603b72aecbf7f66abf26508)
- [IEEE802154_TX_MODE_TXTIME_CCA](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e)
- [IEEE802154_TX_MODE_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225daa389aeccad62a0516678564e68fcd595)
- [IEEE802154_TX_MODE_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2)
- [ieee802154_fpb_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gab593bc6640ddea23c951982ca2f4c0bf)
- [IEEE802154_FPB_ADDR_MATCH_THREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab593bc6640ddea23c951982ca2f4c0bfa012874ab4d234bbeb2954756cf2dc9d6)
- [IEEE802154_FPB_ADDR_MATCH_ZIGBEE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab593bc6640ddea23c951982ca2f4c0bfac7c839b7c0649d6151f90ff1d51ae417)
- [ieee802154_config_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga34aecc5996174a812b295a3a4693ad09)
- [IEEE802154_CONFIG_AUTO_ACK_FPB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a38c67aac70d24b31996871fe4686d9ee)
- [IEEE802154_CONFIG_ACK_FPB](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09ab897aea56ea5e9ddf306c5c0d75c2cd7)
- [IEEE802154_CONFIG_PAN_COORDINATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09ab2b6ae3034fb469168ed29704ec045f0)
- [IEEE802154_CONFIG_PROMISCUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a399313ff2d8ebb3a2d72152a9615d8c5)
- [IEEE802154_CONFIG_EVENT_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a8d88a76f71cf8869b3e35e423b18c6f3)
- [IEEE802154_CONFIG_MAC_KEYS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a8bd29c6d6aa67adaf23415eb337904c0)
- [IEEE802154_CONFIG_FRAME_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09aad7d04b7e1c02b2d88fcbb8ab1ac313b)
- [IEEE802154_CONFIG_FRAME_COUNTER_IF_LARGER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09aa34da77f0966ff5a0e8ac73ed68554a8)
- [IEEE802154_CONFIG_RX_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09af4e3dd7588ee06458f2d42f02797b3d6)
- [IEEE802154_CONFIG_CSL_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a9fdbe95e0b7141d9150eaa4a5793c2e7)
- [IEEE802154_CONFIG_EXPECTED_RX_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a1a71ef76d90b6882196e4c6473de6bd8)
- [IEEE802154_CONFIG_ENH_ACK_HEADER_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a840e5f1db9a354e7bcd892ddb4117907)
- [IEEE802154_CONFIG_RX_ON_WHEN_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a9228dbe2583e5be10f64b116e87645e1)
- [IEEE802154_CONFIG_CSMA_CA_BACKOFFS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a2b8dbb8a7de613b8ca81513242958837)
- [IEEE802154_CONFIG_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a61df14aeb348cfc694d539b506dc23ac)
- [IEEE802154_CONFIG_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c)
- [ieee802154_config](../network_core_model_reference/P014_ieee802154_config_结构体.md)
- [enabled](../network_core_model_reference/P014_ieee802154_config_结构体.md#ad9361f9ba1652e46d0be25e0de39afdf)
- [mode](../network_core_model_reference/P014_ieee802154_config_结构体.md#ad139acde94327d4b8ceb76760751521d)
- [auto_ack_fpb](../network_core_model_reference/P014_ieee802154_config_结构体.md#ab27a654a0d53f268199e95dc21e18fd4)
- [addr](../network_core_model_reference/P014_ieee802154_config_结构体.md#a673f5cceb6439bc1c3527c62062151d1)
- [extended](../network_core_model_reference/P014_ieee802154_config_结构体.md#a55823097d62a69d0c92dc70fb4ff1dd5)
- [ack_fpb](../network_core_model_reference/P014_ieee802154_config_结构体.md#a3a5e597e53bfcc9e3bed8bac2edb74d2)
- [pan_coordinator](../network_core_model_reference/P014_ieee802154_config_结构体.md#a078ec577af3d170781ed770c80c54b72)
- [promiscuous](../network_core_model_reference/P014_ieee802154_config_结构体.md#aafb11c4130ff39e5c40dfe5d32c0d4e7)
- [rx_on_when_idle](../network_core_model_reference/P014_ieee802154_config_结构体.md#a8b7d4804cd051d69f3602f35cb4a8630)
- [event_handler](../network_core_model_reference/P014_ieee802154_config_结构体.md#a1558e71a1d5ab74990964ff4deabbdb7)
- [csma_ca_backoffs](../network_core_model_reference/P014_ieee802154_config_结构体.md#afa1d230e1059013a7a99e737da3a0266)
- [mac_keys](../network_core_model_reference/P014_ieee802154_config_结构体.md#a942c0d4fb244c7256530536dc132a727)
- [frame_counter](../network_core_model_reference/P014_ieee802154_config_结构体.md#a272cfd864c7d47c6f06f26871ce07fb6)
- [net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)
- [start](../network_core_model_reference/P014_ieee802154_config_结构体.md#a86b72101b0b21622f3cc8a2b3877e356)
- [duration](../network_core_model_reference/P014_ieee802154_config_结构体.md#ab36833b4311b03f08f67290f4edd8e41)
- [channel](../network_core_model_reference/P014_ieee802154_config_结构体.md#a8f7efaa743e070479632d139f0fc57c0)
- [rx_slot](../network_core_model_reference/P014_ieee802154_config_结构体.md#aadc2714bf31484cce071e9ef7b9a4007)
- [csl_period](../network_core_model_reference/P014_ieee802154_config_结构体.md#a5106a759148ec20c6c6c83a2581c9e88)
- [expected_rx_time](../network_core_model_reference/P014_ieee802154_config_结构体.md#a8124aed4a4af36c0e21fd8f1b1c97e3e)
- [header_ie](../network_core_model_reference/P014_ieee802154_config_结构体.md#a5343dec0de835943c0bef2c2d603a91d)
- [ext_addr](../network_core_model_reference/P014_ieee802154_config_结构体.md#a03d6ec1a371312961f3a1ee42e113bbf)
- [short_addr](../network_core_model_reference/P014_ieee802154_config_结构体.md#aa27066dd9e54dab6795332b7413670f5)
- [purge_ie](../network_core_model_reference/P014_ieee802154_config_结构体.md#a8971a91be8748bd45027fcb730b99639)
- [ack_ie](../network_core_model_reference/P014_ieee802154_config_结构体.md#a39c06e32cb4a74b4d8a9864f714e8c93)
- [ieee802154_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf4deddd3f23ebfd65fa47c5d62634430)
- [IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_PAGES](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a)
- [IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d)
- [IEEE802154_ATTR_PHY_HRP_UWB_SUPPORTED_PRFS](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430ad90b4a118866c4942ef6f6a8ae56eb3f)
- [IEEE802154_ATTR_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430aa0830214987de7a89297777c0d1004de)
- [IEEE802154_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511)
- [ieee802154_attr_value](../network_core_model_reference/P005_ieee802154_attr_value_结构体.md)
- [phy_supported_channel_pages](../network_core_model_reference/P005_ieee802154_attr_value_结构体.md#a75913597f93de1a80f96bb9dc32d38df)
- [phy_supported_channels](../network_core_model_reference/P005_ieee802154_attr_value_结构体.md#a840d2f3a2502f87806ef79c6926f73f0)
- [phy_hrp_uwb_supported_nominal_prfs](../network_core_model_reference/P005_ieee802154_attr_value_结构体.md#af157805fb8acffb634cba4b37472bdb3)
- [ieee802154_attr_get_channel_page_and_range](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf69d2b65aa46ec4483c6bab419413ba5)
- [ENOENT](../error_reference/P003_系统错误号公共接口.md#ga03e689f378f643d16ea7537918528a48)
- [ieee802154_radio_api](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md)
- [iface_api](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#aa955462d8c6950dc4b5935973f4575d8)
- [get_capabilities](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a09a4b5df81822845f718952c6029442c)
- [cca](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a2cbbd0e64fae28f748bb3e4d654a92bf)
- [set_channel](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a9ad27a2ff0a839dc5b9a4e6317cc59b1)
- [filter](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#aa9502e0e014a8d05ffe235567e8c98f3)
- [set_txpower](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#aeeab6dfcde08af23357ea40f8af68f66)
- [tx](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a70139acec22642c1fc09f2323c383fe6)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [start](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a0e4d57dc3a53299ddedf2140e172103d)
- [stop](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a75cfcfe2b9e69c2e4af53f00c8294b36)
- [configure](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a9acaf4810bd5d3b026cc381bff301071)
- [ed_scan](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a01fc17f85f2be33877a9347f59a84c54)
- [get_time](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a829a0d59fdcda5b6cb029ef1334a6b8b)
- [get_sch_acc](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#ae4a3ef40a5b8031c868d72ead163c97d)
- [attr_get](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a0b3e0ed1385dd428c861e08c79849ef4)
- [ieee802154_is_ar_flag_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaf5d7bdde2a9774f9d90604a6e203bb07)
- [data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [ieee802154_handle_ack](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga68e1f89571ccbefef61a5496577337fc)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [ieee802154_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gad2a4cb5df84ffe20b83fc54dc9bcfc91)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [ieee802154.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154_8h.html)
- [ieee802154_ie.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [net_time.h](https://docs.zephyrproject.org/latest/doxygen/html/net__time_8h.html)
- [ieee802154_attr_value::phy_supported_channel_pages](../network_core_model_reference/P005_ieee802154_attr_value_结构体.md#a75913597f93de1a80f96bb9dc32d38df)
- [ieee802154_attr_value::phy_supported_channels](../network_core_model_reference/P005_ieee802154_attr_value_结构体.md#a840d2f3a2502f87806ef79c6926f73f0)
- [ieee802154_attr_value::phy_hrp_uwb_supported_nominal_prfs](../network_core_model_reference/P005_ieee802154_attr_value_结构体.md#af157805fb8acffb634cba4b37472bdb3)
- [ieee802154_config::ext_addr](../network_core_model_reference/P014_ieee802154_config_结构体.md#a03d6ec1a371312961f3a1ee42e113bbf)
- [ieee802154_config::pan_coordinator](../network_core_model_reference/P014_ieee802154_config_结构体.md#a078ec577af3d170781ed770c80c54b72)
- [ieee802154_config::event_handler](../network_core_model_reference/P014_ieee802154_config_结构体.md#a1558e71a1d5ab74990964ff4deabbdb7)
- [ieee802154_config::frame_counter](../network_core_model_reference/P014_ieee802154_config_结构体.md#a272cfd864c7d47c6f06f26871ce07fb6)
- [ieee802154_config::ack_ie](../network_core_model_reference/P014_ieee802154_config_结构体.md#a39c06e32cb4a74b4d8a9864f714e8c93)
- [ieee802154_config::ack_fpb](../network_core_model_reference/P014_ieee802154_config_结构体.md#a3a5e597e53bfcc9e3bed8bac2edb74d2)
- [ieee802154_config::csl_period](../network_core_model_reference/P014_ieee802154_config_结构体.md#a5106a759148ec20c6c6c83a2581c9e88)
- [ieee802154_config::header_ie](../network_core_model_reference/P014_ieee802154_config_结构体.md#a5343dec0de835943c0bef2c2d603a91d)
- [ieee802154_config::extended](../network_core_model_reference/P014_ieee802154_config_结构体.md#a55823097d62a69d0c92dc70fb4ff1dd5)
- [ieee802154_config::addr](../network_core_model_reference/P014_ieee802154_config_结构体.md#a673f5cceb6439bc1c3527c62062151d1)
- [ieee802154_config::expected_rx_time](../network_core_model_reference/P014_ieee802154_config_结构体.md#a8124aed4a4af36c0e21fd8f1b1c97e3e)
- [ieee802154_config::start](../network_core_model_reference/P014_ieee802154_config_结构体.md#a86b72101b0b21622f3cc8a2b3877e356)
- [ieee802154_config::purge_ie](../network_core_model_reference/P014_ieee802154_config_结构体.md#a8971a91be8748bd45027fcb730b99639)
- [ieee802154_config::rx_on_when_idle](../network_core_model_reference/P014_ieee802154_config_结构体.md#a8b7d4804cd051d69f3602f35cb4a8630)
- [ieee802154_config::channel](../network_core_model_reference/P014_ieee802154_config_结构体.md#a8f7efaa743e070479632d139f0fc57c0)
- [ieee802154_config::mac_keys](../network_core_model_reference/P014_ieee802154_config_结构体.md#a942c0d4fb244c7256530536dc132a727)
- [ieee802154_config::short_addr](../network_core_model_reference/P014_ieee802154_config_结构体.md#aa27066dd9e54dab6795332b7413670f5)
- [ieee802154_config::rx_slot](../network_core_model_reference/P014_ieee802154_config_结构体.md#aadc2714bf31484cce071e9ef7b9a4007)
- [ieee802154_config::promiscuous](../network_core_model_reference/P014_ieee802154_config_结构体.md#aafb11c4130ff39e5c40dfe5d32c0d4e7)
- [ieee802154_config::auto_ack_fpb](../network_core_model_reference/P014_ieee802154_config_结构体.md#ab27a654a0d53f268199e95dc21e18fd4)
- [ieee802154_config::duration](../network_core_model_reference/P014_ieee802154_config_结构体.md#ab36833b4311b03f08f67290f4edd8e41)
- [ieee802154_config::mode](../network_core_model_reference/P014_ieee802154_config_结构体.md#ad139acde94327d4b8ceb76760751521d)
- [ieee802154_config::enabled](../network_core_model_reference/P014_ieee802154_config_结构体.md#ad9361f9ba1652e46d0be25e0de39afdf)
- [ieee802154_config::csma_ca_backoffs](../network_core_model_reference/P014_ieee802154_config_结构体.md#afa1d230e1059013a7a99e737da3a0266)
- [ieee802154_filter::short_addr](../network_core_model_reference/P017_ieee802154_filter_结构体.md#a16a1779ff43accda31bba35b9bdd61c3)
- [ieee802154_filter::pan_id](../network_core_model_reference/P017_ieee802154_filter_结构体.md#a40f77239924af29d40f7595e23475e9b)
- [ieee802154_filter::ieee_addr](../network_core_model_reference/P017_ieee802154_filter_结构体.md#a636ec85ca79b2880de51ed93f6788909)
- [ieee802154_key::key_value](../network_core_model_reference/P032_ieee802154_key_结构体.md#a01b760f3e622ad0a60888170e5688b9d)
- [ieee802154_key::key_frame_counter](../network_core_model_reference/P032_ieee802154_key_结构体.md#a357419c2d16a527a2417f4eded566aac)
- [ieee802154_key::frame_counter_per_key](../network_core_model_reference/P032_ieee802154_key_结构体.md#a5ca5258422db14b99fd37e7126cfc85d)
- [ieee802154_key::key_id_mode](../network_core_model_reference/P032_ieee802154_key_结构体.md#a732a2a89e74139bd1d8e9b358c0306c7)
- [ieee802154_key::key_id](../network_core_model_reference/P032_ieee802154_key_结构体.md#ae0a1e354b5718e8135fb6198ea12276a)
- [ieee802154_phy_channel_range::to_channel](../network_core_model_reference/P039_ieee802154_phy_channel_range_结构体.md#a78af593807753dbfcfce88166f4c1f58)
- [ieee802154_phy_channel_range::from_channel](../network_core_model_reference/P039_ieee802154_phy_channel_range_结构体.md#aec90e36227a7d9cc1dfc18231341dd03)
- [ieee802154_phy_supported_channels::ranges](../network_core_model_reference/P040_ieee802154_phy_supported_channels_结构体.md#a73ccabf887b567a0ce3ddc5f8a3eeed1)
- [ieee802154_phy_supported_channels::num_ranges](../network_core_model_reference/P040_ieee802154_phy_supported_channels_结构体.md#a8fb56a7fc6be96035cf4b51891582da9)
- [ieee802154_radio_api::ed_scan](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a01fc17f85f2be33877a9347f59a84c54)
- [ieee802154_radio_api::get_capabilities](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a09a4b5df81822845f718952c6029442c)
- [ieee802154_radio_api::attr_get](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a0b3e0ed1385dd428c861e08c79849ef4)
- [ieee802154_radio_api::start](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a0e4d57dc3a53299ddedf2140e172103d)
- [ieee802154_radio_api::cca](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a2cbbd0e64fae28f748bb3e4d654a92bf)
- [ieee802154_radio_api::tx](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a70139acec22642c1fc09f2323c383fe6)
- [ieee802154_radio_api::stop](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a75cfcfe2b9e69c2e4af53f00c8294b36)
- [ieee802154_radio_api::get_time](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a829a0d59fdcda5b6cb029ef1334a6b8b)
- [ieee802154_radio_api::configure](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a9acaf4810bd5d3b026cc381bff301071)
- [ieee802154_radio_api::set_channel](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#a9ad27a2ff0a839dc5b9a4e6317cc59b1)
- [ieee802154_radio_api::filter](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#aa9502e0e014a8d05ffe235567e8c98f3)
- [ieee802154_radio_api::iface_api](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#aa955462d8c6950dc4b5935973f4575d8)
- [ieee802154_radio_api::get_sch_acc](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#ae4a3ef40a5b8031c868d72ead163c97d)
- [ieee802154_radio_api::set_txpower](../network_core_model_reference/P041_ieee802154_radio_api_结构体.md#aeeab6dfcde08af23357ea40f8af68f66)
- [net_buf::data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P009_ieee802154_ie.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P011_img_mgmt.h_源码浏览.md)
