---
id: learning.zephyr-docs.api-source-device-reference.page-53
title: usbd.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_usbd.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbd_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usbd_8h.html)。

## 53.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00077"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="foldopen00158"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="foldopen00195"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="foldopen00215"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="foldopen00225"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="foldopen00243"></a>
<a id="l00243"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="foldopen00255"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="foldopen00294"></a>
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
<a id="l00325"></a>
<a id="l00326"></a>
<a id="foldopen00330"></a>
<a id="l00330"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="foldopen00345"></a>
<a id="l00345"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="foldopen00396"></a>
<a id="l00396"></a>
<a id="l00398"></a>
<a id="l00400"></a>
<a id="l00402"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00417"></a>
<a id="l00419"></a>
<a id="l00421"></a>
<a id="l00425"></a>
<a id="l00429"></a>
<a id="l00431"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00437"></a>
<a id="foldopen00448"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="foldopen00463"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="foldopen00488"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
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
<a id="foldopen00552"></a>
<a id="l00552"></a>
<a id="l00553"></a>
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
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="foldopen00583"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="foldopen00606"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="foldopen00629"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="foldopen00643"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="foldopen00659"></a>
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
<a id="foldopen00679"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="foldopen00694"></a>
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
<a id="foldopen00716"></a>
<a id="l00716"></a>
<a id="l00717"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="foldopen00744"></a>
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
<a id="foldopen00769"></a>
<a id="l00769"></a>
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
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="foldopen00792"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00797"></a>
<a id="foldopen00802"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00872"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00968"></a>
<a id="l00969"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00990"></a>
<a id="l00991"></a>
<a id="l01001"></a>
<a id="l01002"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="l01021"></a>
<a id="l01022"></a>
<a id="l01031"></a>
<a id="l01032"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01057"></a>
<a id="l01058"></a>
<a id="l01059"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="l01083"></a>
<a id="l01084"></a>
<a id="l01085"></a>
<a id="l01094"></a>
<a id="l01095"></a>
<a id="l01106"></a>
<a id="l01107"></a>
<a id="l01115"></a>
<a id="l01116"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="l01144"></a>
<a id="l01145"></a>
<a id="l01153"></a>
<a id="l01154"></a>
<a id="l01164"></a>
<a id="l01165"></a>
<a id="l01166"></a>
<a id="l01175"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="l01186"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01197"></a>
<a id="l01198"></a>
<a id="l01199"></a>
<a id="l01211"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01215"></a>
<a id="l01226"></a>
<a id="l01227"></a>
<a id="l01228"></a>
<a id="l01229"></a>
<a id="l01240"></a>
<a id="l01241"></a>
<a id="l01242"></a>
<a id="l01243"></a>
<a id="l01254"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01270"></a>
<a id="l01271"></a>
<a id="l01283"></a>
<a id="l01284"></a>
<a id="l01285"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="l01291"></a>
<a id="l01292"></a>
<a id="l01293"></a>
<a id="l01294"></a>
<a id="abos_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__doubly-linked-list__apis_html_ga57fdb936802a617d16c00ab08cd2ad98"></a>
<a id="agroup__doubly-linked-list__apis_html_gaa03f9557215b486fee1039dd4c07e683"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__usbd__api_html_ga03729a4e9add3a55a7c3c2c8666a53a7"></a>
<a id="agroup__usbd__api_html_ga06541b17f5afc917cc5154bd4d816ec3"></a>
<a id="agroup__usbd__api_html_ga06aa9f954b6765e07494753bb4fa42d4"></a>
<a id="agroup__usbd__api_html_ga1534058a609794e1d080aed98fcf5823"></a>
<a id="agroup__usbd__api_html_ga176f42b2dd221c0de28ad9122a7d2693"></a>
<a id="agroup__usbd__api_html_ga1a40fc13129e9218ca63ab3ca70d8d68"></a>
<a id="agroup__usbd__api_html_ga1ae7a7a04f4ec1206d352d5c6401c51b"></a>
<a id="agroup__usbd__api_html_ga1ce934ca354853ec9c7c295cca2d0e3d"></a>
<a id="agroup__usbd__api_html_ga2996b5f6df459c8a179fc6c22f944063"></a>
<a id="agroup__usbd__api_html_ga2b803f8ac10d9375a74949cd2c2f3136"></a>
<a id="agroup__usbd__api_html_ga2cd074cefff922b0816de37935d9646e"></a>
<a id="agroup__usbd__api_html_ga2e511d0341b4e1bd57fb4420512eeeb5"></a>
<a id="agroup__usbd__api_html_ga2ebe08b8bf5ff3b64c4df1fcb346cf38"></a>
<a id="agroup__usbd__api_html_ga2f2da3d634530f08cd59d408c811ad71"></a>
<a id="agroup__usbd__api_html_ga3146ee636b84c6d319365716f5741363"></a>
<a id="agroup__usbd__api_html_ga33d0cef23d4b6c62b79b41559427b584"></a>
<a id="agroup__usbd__api_html_ga34086553e74795ffdc000349e61a3c8b"></a>
<a id="agroup__usbd__api_html_ga37585e0124a4d0d8cf6e65f13325eaf0"></a>
<a id="agroup__usbd__api_html_ga44719fc03a50c70d75ce65e1d2f77a04"></a>
<a id="agroup__usbd__api_html_ga4a837040e9d02c5773d69a6cf6c35960"></a>
<a id="agroup__usbd__api_html_ga59fc1ea6d943d26b0207bb6060e18f08"></a>
<a id="agroup__usbd__api_html_ga5ea40d893980e24294e82d22855b407c"></a>
<a id="agroup__usbd__api_html_ga5f4b69609f9a8f00a9e0fea4dffce1c4"></a>
<a id="agroup__usbd__api_html_ga5f7a5af958f7de8893e04ff2b7748c7e"></a>
<a id="agroup__usbd__api_html_ga6c671d49c811b0af6b809f5940cd6d70"></a>
<a id="agroup__usbd__api_html_ga78e5f07af641f9610cc32255efe1680f"></a>
<a id="agroup__usbd__api_html_ga83a58b50bec680513eabd3bb7075b511"></a>
<a id="agroup__usbd__api_html_ga8aa454c24495f2a462eae53b78c488dc"></a>
<a id="agroup__usbd__api_html_ga8b0fff68bc6ce9d8ec4a7dfd59f0eade"></a>
<a id="agroup__usbd__api_html_ga9056e1f01b64ddd26db6a5ee45439e22"></a>
<a id="agroup__usbd__api_html_ga94cb8465b7bf85457f29e84b5b8ddfe9"></a>
<a id="agroup__usbd__api_html_ga95fb708d8a54eaa3ce0acc4e65519bbc"></a>
<a id="agroup__usbd__api_html_ga967d507d82d912119a732fd230bd561e"></a>
<a id="agroup__usbd__api_html_gaaa21e9f33175b7d2434e54e1b3d2799b"></a>
<a id="agroup__usbd__api_html_gaab7c4692a30b58aa76b03b9e50460856"></a>
<a id="agroup__usbd__api_html_gaabf8333a7aefc4428f38e79a7264e383"></a>
<a id="agroup__usbd__api_html_gaaebba63d8a8b78a1f06c1a5a476cd306"></a>
<a id="agroup__usbd__api_html_gab023ab276eb68c644895483344d33948"></a>
<a id="agroup__usbd__api_html_gab4a0d05a8f183f7479ad33ee29e8a611"></a>
<a id="agroup__usbd__api_html_gacb704bd4f396887c859932b2ab6b4991"></a>
<a id="agroup__usbd__api_html_gaf8aadd499f7e0438acac4a7f36645d49"></a>
<a id="agroup__usbd__api_html_gaf97c68e75420bd5a1085c047577fd5a7"></a>
<a id="agroup__usbd__api_html_gafda88e8a71c52addbe76ebeb874a8af5"></a>
<a id="agroup__usbd__api_html_gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a"></a>
<a id="agroup__usbd__api_html_gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7"></a>
<a id="agroup__usbd__api_html_gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266"></a>
<a id="agroup__usbd__api_html_gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509"></a>
<a id="agroup__usbd__api_html_gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048"></a>
<a id="agroup__usbd__api_html_gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d"></a>
<a id="alog_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructk__spinlock_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_a1522d81a002804223e25300a6961f527"></a>
<a id="astructusb__setup__packet_html"></a>
<a id="astructusbd__bos__desc__data_html"></a>
<a id="astructusbd__bos__desc__data_html_a084578c905400488e5ce73c71f8aaf00"></a>
<a id="astructusbd__bos__desc__data_html_a2d8570c88670c4fbf2d79bb989da01d9"></a>
<a id="astructusbd__cctx__vendor__req_html"></a>
<a id="astructusbd__cctx__vendor__req_html_a2ddf3ce0c1c0a6d788b7ef30cf8d67ea"></a>
<a id="astructusbd__cctx__vendor__req_html_a3b5e99bff9dbfa023a4e6a5b4a69abd0"></a>
<a id="astructusbd__ch9__data_html"></a>
<a id="astructusbd__ch9__data_html_a1f759fb0d758e50c4589b6b6b1fd2a24"></a>
<a id="astructusbd__ch9__data_html_a504360b7cb11240a2fda68344f2e3b62"></a>
<a id="astructusbd__ch9__data_html_a6ab6f611fd1eff8d6fde0617c587fefb"></a>
<a id="astructusbd__ch9__data_html_a70d1a1be0aab6167ca4f4580b9c65eff"></a>
<a id="astructusbd__ch9__data_html_a85f96c69cede5b51c1f9739a4ae67f4d"></a>
<a id="astructusbd__ch9__data_html_a8f831eca1974b8411072f8102c444d45"></a>
<a id="astructusbd__class__api_html"></a>
<a id="astructusbd__class__api_html_a09475f1b29f482e548b6bc168dcd19e7"></a>
<a id="astructusbd__class__api_html_a11d09e35f9d4c4d6b18e12bf4ea241b0"></a>
<a id="astructusbd__class__api_html_a488b102936b5cd3e4095578119b71510"></a>
<a id="astructusbd__class__api_html_a598afe76b5c2f9e75a049fe785393e04"></a>
<a id="astructusbd__class__api_html_a5ca5bc6d3f5220bd3658d9398e09016e"></a>
<a id="astructusbd__class__api_html_a70425718fd34534fd976240340b4496d"></a>
<a id="astructusbd__class__api_html_a7d749f007d70e30f76aa121067b7a5c6"></a>
<a id="astructusbd__class__api_html_ab37dd5f2bf4029f149e69046702626a1"></a>
<a id="astructusbd__class__api_html_ab42f61db338471f0c5260576680409e9"></a>
<a id="astructusbd__class__api_html_ae6f3a658e5768f5d6672cd0e5f2d24a5"></a>
<a id="astructusbd__class__api_html_afd43bfa4aab664c50648aa59a0c713de"></a>
<a id="astructusbd__class__data_html"></a>
<a id="astructusbd__class__data_html_a10bb5b9af6098fbbc86fd00ef54e84e1"></a>
<a id="astructusbd__class__data_html_a111a803092fd389a500fb99bfc71b29a"></a>
<a id="astructusbd__class__data_html_a32db83ecf80e1ac9e4d5deda54581deb"></a>
<a id="astructusbd__class__data_html_a9109af3e25c499d4ef1f0746bf6a20cc"></a>
<a id="astructusbd__class__data_html_ad251371b0e401fb2bffd6aaa1ff49063"></a>
<a id="astructusbd__config__node_html"></a>
<a id="astructusbd__config__node_html_a003a8d9132b319f54583263c4da1e060"></a>
<a id="astructusbd__config__node_html_a00493162af2344d3d39f834b4834ef78"></a>
<a id="astructusbd__config__node_html_a19203885a9698861f849bd0fd57cb37f"></a>
<a id="astructusbd__config__node_html_a55081d79ab3e6b41a091b3f65d7d2d87"></a>
<a id="astructusbd__context_html"></a>
<a id="astructusbd__context_html_a193420cc196f115cbd6947b10d542ee5"></a>
<a id="astructusbd__context_html_a250e2f82c7239ce81b104b6ef3c16857"></a>
<a id="astructusbd__context_html_a300ab0384b3d4e7f3d7d188a27a78be3"></a>
<a id="astructusbd__context_html_a3acad44126b6c3d56823ef7408332087"></a>
<a id="astructusbd__context_html_a4a6bd413d06328ffa5db089e35157376"></a>
<a id="astructusbd__context_html_a4fb1545ec02e7d38766cee9940edc1eb"></a>
<a id="astructusbd__context_html_a52c2cc6118b46fbcbc7a495df61f6b6c"></a>
<a id="astructusbd__context_html_a6b463c6c01230bc68c50ba5bb5550e99"></a>
<a id="astructusbd__context_html_a7a884c982011034fd02a41d7cb450509"></a>
<a id="astructusbd__context_html_a8c7d153a73859dd8ba25265f059f7495"></a>
<a id="astructusbd__context_html_a8ff2a4303b73db67eeabdd999736b3a6"></a>
<a id="astructusbd__context_html_ade73c224b256007bf2d68bd1205ceb6e"></a>
<a id="astructusbd__context_html_adf8dd86f2784cc69ce6da314adc00b72"></a>
<a id="astructusbd__context_html_ae65f5ae6e67b1e9e302a1d45d59751c3"></a>
<a id="astructusbd__context_html_aec2fa8e53ddaa2e282e381218171d7bd"></a>
<a id="astructusbd__desc__node_html"></a>
<a id="astructusbd__desc__node_html_a786e2911b5ec7d6c908c148be4d27f5f"></a>
<a id="astructusbd__desc__node_html_a9f1941cd036c01387d8ad9a4aceb595a"></a>
<a id="astructusbd__desc__node_html_ac437b472e012e8fdec049f28e9f88944"></a>
<a id="astructusbd__desc__node_html_ad71ef74fd7fe43a8117704553a3be01c"></a>
<a id="astructusbd__desc__node_html_ae34fee200f7fd78355addafe79789cb4"></a>
<a id="astructusbd__desc__node_html_afd65079b8b969fa4101a3f9f662c7b6b"></a>
<a id="astructusbd__msg_html"></a>
<a id="astructusbd__status_html"></a>
<a id="astructusbd__status_html_a113085892967cf7c9cb70131b320d61a"></a>
<a id="astructusbd__status_html_a2382fcb655fe51e0bcf83f85aa182ba3"></a>
<a id="astructusbd__status_html_a295009d25826732ba9eebd7735d93d23"></a>
<a id="astructusbd__status_html_a78de12245d08ecc71e09d5519fe0e857"></a>
<a id="astructusbd__status_html_ae4107cb4f379cce8c0472a98483705b8"></a>
<a id="astructusbd__status_html_afb67cfda187e40229f842c93aa09f0ba"></a>
<a id="astructusbd__str__desc__data_html"></a>
<a id="astructusbd__str__desc__data_html_a0654953d15160cc19cad86a407f655cb"></a>
<a id="astructusbd__str__desc__data_html_a2e6dfc9cbbd44457113899db988a84ca"></a>
<a id="astructusbd__str__desc__data_html_a40459d114a339841e1f9c14b0d036fe8"></a>
<a id="astructusbd__str__desc__data_html_ad4d7c291f95973d20ff522b8a5ef65a0"></a>
<a id="astructusbd__vreq__node_html"></a>
<a id="astructusbd__vreq__node_html_a3c68346e2f871b22fb6c3b282ddfdccb"></a>
<a id="astructusbd__vreq__node_html_a91fe4c5cf5ccad89e81380a332a8f955"></a>
<a id="astructusbd__vreq__node_html_ae69e3dd3b4cdc7deb1ccdd9d9ebe4ec3"></a>
<a id="asys_2byteorder_8h_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="ausb__buf_8h_html"></a>
<a id="ausb__ch9_8h_html"></a>
<a id="ausbd__msg_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USBD_H_
#define ZEPHYR_INCLUDE_USBD_H_

#include <zephyr/device.h>
#include <zephyr/usb/bos.h>
#include <zephyr/usb/usb_ch9.h>
#include <zephyr/usb/usbd_msg.h>
#include <zephyr/drivers/usb/usb_buf.h>
#include <zephyr/sys/byteorder.h>
#include <zephyr/sys/slist.h>
#include <zephyr/logging/log.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif


/* 1 if USB device stack is compiled with High-Speed support */
#define USBD_SUPPORTS_HIGH_SPEED IS_EQ(CONFIG_USBD_MAX_SPEED, 1)

/* Maximum bulk max packet size the stack supports */
#define USBD_MAX_BULK_MPS COND_CODE_1(USBD_SUPPORTS_HIGH_SPEED, (512), (64))

/*
 * The length of the string descriptor (bLength) is calculated from the
 * size of the two octets bLength and bDescriptorType plus the
 * length of the UTF16LE string:
 *
 *   bLength = 2 + bString_length
 *   bLength = 2 + sizeof(initializer_string) * 2 - 2
 *   bLength = sizeof(initializer_string) * 2
 * Use this macro to determine the bLength of the string descriptor.
 */
#define USB_STRING_DESCRIPTOR_LENGTH(s) (sizeof(s) * 2)

struct usbd_context;

enum usbd_str_desc_utype {
        USBD_DUT_STRING_LANG,
        USBD_DUT_STRING_MANUFACTURER,
        USBD_DUT_STRING_PRODUCT,
        USBD_DUT_STRING_SERIAL_NUMBER,
        USBD_DUT_STRING_CONFIG,
        USBD_DUT_STRING_INTERFACE,
};

enum usbd_bos_desc_utype {
        USBD_DUT_BOS_NONE,
        USBD_DUT_BOS_VREQ,
};

struct usbd_str_desc_data {
        uint8_t idx;
        enum usbd_str_desc_utype utype : 8;
        unsigned int ascii7 : 1;
        unsigned int use_hwinfo : 1;
};

struct usbd_vreq_node {
        sys_dnode_t node;
        const uint8_t code;
        struct net_buf *(*to_host)(const struct usbd_context *const ctx,
                                   const struct usb_setup_packet *const setup);
        int (*to_dev)(const struct usbd_context *const ctx,
                      const struct usb_setup_packet *const setup,
                      const struct net_buf *const buf);
};

struct usbd_bos_desc_data {
        enum usbd_bos_desc_utype utype : 8;
        union {
                struct usbd_vreq_node *const vreq_nd;
        };
};

struct usbd_desc_node {
        sys_dnode_t node;
        union {
                struct usbd_str_desc_data str;
                struct usbd_bos_desc_data bos;
        };
        const void *const ptr;
        uint8_t bLength;
        uint8_t bDescriptorType;
};

struct usbd_config_node {
        sys_snode_t node;
        void *desc;
        struct usbd_desc_node *str_desc_nd;
        sys_slist_t class_list;
};

/* TODO: Kconfig option USBD_NUMOF_INTERFACES_MAX? */
#define USBD_NUMOF_INTERFACES_MAX       16U

enum usbd_ch9_state {
        USBD_STATE_DEFAULT = 0,
        USBD_STATE_ADDRESS,
        USBD_STATE_CONFIGURED,
};


struct usbd_ch9_data {
        struct usb_setup_packet setup;
        enum usbd_ch9_state state;
        uint32_t ep_halt;
        uint8_t configuration;
        bool post_status;
        uint8_t alternate[USBD_NUMOF_INTERFACES_MAX];
};

enum usbd_speed {
        USBD_SPEED_FS,
        USBD_SPEED_HS,
        USBD_SPEED_SS,
};

struct usbd_status {
        unsigned int initialized : 1;
        unsigned int enabled : 1;
        unsigned int suspended : 1;
        unsigned int rwup : 1;
        unsigned int self_powered : 1;
        enum usbd_speed speed : 2;
};

typedef void (*usbd_msg_cb_t)(struct usbd_context *const ctx,
                              const struct usbd_msg *const msg);

struct usbd_context {
        const char *name;
        struct k_mutex mutex;
        const struct device *dev;
        usbd_msg_cb_t msg_cb;
        sys_slist_t ep_events;
        struct k_spinlock ep_event_lock;
        struct usbd_ch9_data ch9_data;
        sys_dlist_t descriptors;
        sys_slist_t fs_configs;
        sys_slist_t hs_configs;
        sys_dlist_t vreqs;
        struct usbd_status status;
        void *fs_desc;
        void *hs_desc;
        struct net_buf *setup_buf;
};

struct usbd_cctx_vendor_req {
        const uint8_t *reqs;
        uint8_t len;
};

#define USBD_CCTX_REGISTERED            0

struct usbd_class_data;

struct usbd_class_api {
        void (*feature_halt)(struct usbd_class_data *const c_data,
                             uint8_t ep, bool halted);

        void (*update)(struct usbd_class_data *const c_data,
                       uint8_t iface, uint8_t alternate);

        int (*control_to_dev)(struct usbd_class_data *const c_data,
                              const struct usb_setup_packet *const setup,
                              const struct net_buf *const buf);

        struct net_buf *(*control_to_host)(struct usbd_class_data *const c_data,
                                           const struct usb_setup_packet *const setup);

        int (*request)(struct usbd_class_data *const c_data,
                       struct net_buf *buf, int err);

        void (*suspended)(struct usbd_class_data *const c_data);

        void (*resumed)(struct usbd_class_data *const c_data);

        void (*sof)(struct usbd_class_data *const c_data);

        void (*enable)(struct usbd_class_data *const c_data);

        void (*disable)(struct usbd_class_data *const c_data);

        int (*init)(struct usbd_class_data *const c_data);

        void (*shutdown)(struct usbd_class_data *const c_data);

        const void *(*get_desc)(struct usbd_class_data *const c_data,
                                const enum usbd_speed speed);
};

struct usbd_class_data {
        const char *name;
        struct usbd_context *uds_ctx;
        const struct usbd_class_api *api;
        const struct usbd_cctx_vendor_req *v_reqs;
        void *priv;
};

struct usbd_class_node {
        sys_snode_t node;
        struct usbd_class_data *const c_data;
        uint32_t ep_assigned;
        uint32_t ep_active;
        uint32_t iface_bm;
        atomic_t state;
};


static inline struct usbd_context *usbd_class_get_ctx(const struct usbd_class_data *const c_data)
{
        return c_data->uds_ctx;
}

static inline void *usbd_class_get_private(const struct usbd_class_data *const c_data)
{
        return c_data->priv;
}

#define USBD_DEVICE_DEFINE(device_name, udc_dev, vid, pid)              \
        static struct usb_device_descriptor                             \
        fs_desc_##device_name = {                                       \
                .bLength = sizeof(struct usb_device_descriptor),        \
                .bDescriptorType = USB_DESC_DEVICE,                     \
                .bcdUSB = sys_cpu_to_le16(USB_SRN_2_0),                 \
                .bDeviceClass = USB_BCC_MISCELLANEOUS,                  \
                .bDeviceSubClass = 2,                                   \
                .bDeviceProtocol = 1,                                   \
                .bMaxPacketSize0 = USB_CONTROL_EP_MPS,                  \
                .idVendor = vid,                                        \
                .idProduct = pid,                                       \
                .bcdDevice = sys_cpu_to_le16(USB_BCD_DRN),              \
                .iManufacturer = 0,                                     \
                .iProduct = 0,                                          \
                .iSerialNumber = 0,                                     \
                .bNumConfigurations = 0,                                \
        };                                                              \
        IF_ENABLED(USBD_SUPPORTS_HIGH_SPEED, (                          \
        static struct usb_device_descriptor                             \
        hs_desc_##device_name = {                                       \
                .bLength = sizeof(struct usb_device_descriptor),        \
                .bDescriptorType = USB_DESC_DEVICE,                     \
                .bcdUSB = sys_cpu_to_le16(USB_SRN_2_0),                 \
                .bDeviceClass = USB_BCC_MISCELLANEOUS,                  \
                .bDeviceSubClass = 2,                                   \
                .bDeviceProtocol = 1,                                   \
                .bMaxPacketSize0 = 64,                                  \
                .idVendor = vid,                                        \
                .idProduct = pid,                                       \
                .bcdDevice = sys_cpu_to_le16(USB_BCD_DRN),              \
                .iManufacturer = 0,                                     \
                .iProduct = 0,                                          \
                .iSerialNumber = 0,                                     \
                .bNumConfigurations = 0,                                \
        };                                                              \
        ))                                                              \
        static STRUCT_SECTION_ITERABLE(usbd_context, device_name) = {   \
                .name = STRINGIFY(device_name),                         \
                .mutex = Z_MUTEX_INITIALIZER(device_name.mutex),        \
                .dev = udc_dev,                                         \
                .fs_desc = &fs_desc_##device_name,                      \
                IF_ENABLED(USBD_SUPPORTS_HIGH_SPEED, (                  \
                .hs_desc = &hs_desc_##device_name,                      \
                ))                                                      \
        }

#define USBD_CONFIGURATION_DEFINE(name, attrib, power, desc_nd)         \
        static struct usb_cfg_descriptor                                \
        cfg_desc_##name = {                                             \
                .bLength = sizeof(struct usb_cfg_descriptor),           \
                .bDescriptorType = USB_DESC_CONFIGURATION,              \
                .wTotalLength = 0,                                      \
                .bNumInterfaces = 0,                                    \
                .bConfigurationValue = 1,                               \
                .iConfiguration = 0,                                    \
                .bmAttributes = USB_SCD_RESERVED | (attrib),            \
                .bMaxPower = (power),                                   \
        };                                                              \
        BUILD_ASSERT((power) < 256, "Too much power");                  \
        static struct usbd_config_node name = {                         \
                .desc = &cfg_desc_##name,                               \
                .str_desc_nd = desc_nd,                                 \
        }

#define USBD_DESC_LANG_DEFINE(name)                                     \
        static const uint16_t langid_##name = sys_cpu_to_le16(0x0409);  \
        static struct usbd_desc_node name = {                           \
                .str = {                                                \
                        .idx = 0,                                       \
                        .utype = USBD_DUT_STRING_LANG,                  \
                },                                                      \
                .ptr = &langid_##name,                                  \
                .bLength = sizeof(struct usb_string_descriptor),        \
                .bDescriptorType = USB_DESC_STRING,                     \
        }

#define USBD_DESC_STRING_DEFINE(d_name, d_string, d_utype)                      \
        static const uint8_t ascii_##d_name[sizeof(d_string)] = d_string;       \
        static struct usbd_desc_node d_name = {                                 \
                .str = {                                                        \
                        .utype = d_utype,                                       \
                        .ascii7 = true,                                         \
                },                                                              \
                .ptr = &ascii_##d_name,                                         \
                .bLength = USB_STRING_DESCRIPTOR_LENGTH(d_string),              \
                .bDescriptorType = USB_DESC_STRING,                             \
        }

#define USBD_DESC_MANUFACTURER_DEFINE(d_name, d_string)                 \
        USBD_DESC_STRING_DEFINE(d_name, d_string, USBD_DUT_STRING_MANUFACTURER)

#define USBD_DESC_PRODUCT_DEFINE(d_name, d_string)                      \
        USBD_DESC_STRING_DEFINE(d_name, d_string, USBD_DUT_STRING_PRODUCT)

#define USBD_DESC_SERIAL_NUMBER_DEFINE(d_name)                                  \
        BUILD_ASSERT(IS_ENABLED(CONFIG_HWINFO), "HWINFO not enabled");          \
        static struct usbd_desc_node d_name = {                                 \
                .str = {                                                        \
                        .utype = USBD_DUT_STRING_SERIAL_NUMBER,                 \
                        .ascii7 = true,                                         \
                        .use_hwinfo = true,                                     \
                },                                                              \
                .bDescriptorType = USB_DESC_STRING,                             \
        }

#define USBD_DESC_CONFIG_DEFINE(d_name, d_string)                       \
        USBD_DESC_STRING_DEFINE(d_name, d_string, USBD_DUT_STRING_CONFIG)

#define USBD_DESC_BOS_DEFINE(name, len, subset)                                 \
        BUILD_ASSERT(IS_ENABLED(CONFIG_USBD_BOS_SUPPORT),                       \
                     "USB device BOS support is disabled");                     \
        static struct usbd_desc_node name = {                                   \
                .bos = {                                                        \
                        .utype = USBD_DUT_BOS_NONE,                             \
                },                                                              \
                .ptr = subset,                                                  \
                .bLength = len,                                                 \
                .bDescriptorType = USB_DESC_BOS,                                \
        }

#define USBD_VREQUEST_DEFINE(name, vcode, vto_host, vto_dev)                    \
        BUILD_ASSERT(IS_ENABLED(CONFIG_USBD_VREQ_SUPPORT),                      \
                     "USB device vendor request support is disabled");          \
        static struct usbd_vreq_node name = {                                   \
                .code = vcode,                                                  \
                .to_host = vto_host,                                            \
                .to_dev = vto_dev,                                              \
        }

#define USBD_DESC_BOS_VREQ_DEFINE(name, len, subset, vcode, vto_host, vto_dev)  \
        BUILD_ASSERT(IS_ENABLED(CONFIG_USBD_BOS_SUPPORT),                       \
                     "USB device BOS support is disabled");                     \
        USBD_VREQUEST_DEFINE(vreq_nd_##name, vcode, vto_host, vto_dev);         \
        static struct usbd_desc_node name = {                                   \
                .bos = {                                                        \
                        .utype = USBD_DUT_BOS_VREQ,                             \
                        .vreq_nd = &vreq_nd_##name,                             \
                },                                                              \
                .ptr = subset,                                                  \
                .bLength = len,                                                 \
                .bDescriptorType = USB_DESC_BOS,                                \
        }

#define USBD_DEFINE_CLASS(class_name, class_api, class_priv, class_v_reqs)      \
        static struct usbd_class_data class_name = {                            \
                .name = STRINGIFY(class_name),                                  \
                .api = class_api,                                               \
                .v_reqs = class_v_reqs,                                         \
                .priv = class_priv,                                             \
        };                                                                      \
        static STRUCT_SECTION_ITERABLE_ALTERNATE(                               \
                usbd_class_fs, usbd_class_node, class_name##_fs) = {            \
                .c_data = &class_name,                                          \
        };                                                                      \
        IF_ENABLED(USBD_SUPPORTS_HIGH_SPEED, (                                  \
        static STRUCT_SECTION_ITERABLE_ALTERNATE(                               \
                usbd_class_hs, usbd_class_node, class_name##_hs) = {            \
                .c_data = &class_name,                                          \
        }                                                                       \
        ))

#define VENDOR_REQ_DEFINE(_reqs, _len) \
        { \
                .reqs = (const uint8_t *)(_reqs), \
                .len = (_len), \
        }

#define USBD_VENDOR_REQ(_reqs...) \
        VENDOR_REQ_DEFINE(((const uint8_t []) { _reqs }), \
                          sizeof((const uint8_t []) { _reqs }))


int usbd_add_descriptor(struct usbd_context *uds_ctx,
                        struct usbd_desc_node *dn);

uint8_t usbd_str_desc_get_idx(const struct usbd_desc_node *const desc_nd);

void usbd_remove_descriptor(struct usbd_desc_node *const desc_nd);

int usbd_add_configuration(struct usbd_context *uds_ctx,
                           const enum usbd_speed speed,
                           struct usbd_config_node *cd);

int usbd_register_class(struct usbd_context *uds_ctx,
                        const char *name,
                        const enum usbd_speed speed, uint8_t cfg);

int usbd_register_all_classes(struct usbd_context *uds_ctx,
                              const enum usbd_speed speed, uint8_t cfg,
                              const char *const blocklist[]);

int usbd_unregister_class(struct usbd_context *uds_ctx,
                          const char *name,
                          const enum usbd_speed speed, uint8_t cfg);

int usbd_unregister_all_classes(struct usbd_context *uds_ctx,
                                const enum usbd_speed speed, uint8_t cfg);

int usbd_msg_register_cb(struct usbd_context *const uds_ctx,
                         const usbd_msg_cb_t cb);

int usbd_init(struct usbd_context *uds_ctx);

int usbd_enable(struct usbd_context *uds_ctx);

int usbd_disable(struct usbd_context *uds_ctx);

int usbd_shutdown(struct usbd_context *const uds_ctx);

int usbd_ep_set_halt(struct usbd_context *uds_ctx, uint8_t ep);

int usbd_ep_clear_halt(struct usbd_context *uds_ctx, uint8_t ep);

bool usbd_ep_is_halted(struct usbd_context *uds_ctx, uint8_t ep);

struct net_buf *usbd_ep_buf_alloc(const struct usbd_class_data *const c_data,
                                  const uint8_t ep, const size_t size);

struct net_buf *usbd_ep_ctrl_data_in_alloc(const struct usbd_context *const uds_ctx,
                                           const size_t size);

int usbd_ep_ctrl_enqueue(struct usbd_context *const uds_ctx,
                         struct net_buf *const buf);

int usbd_ep_enqueue(const struct usbd_class_data *const c_data,
                    struct net_buf *const buf);

int usbd_ep_dequeue(struct usbd_context *uds_ctx, const uint8_t ep);

int usbd_ep_buf_free(struct usbd_context *uds_ctx, struct net_buf *buf);

bool usbd_is_suspended(struct usbd_context *uds_ctx);

int usbd_wakeup_request(struct usbd_context *uds_ctx);

void usbd_self_powered(struct usbd_context *uds_ctx, const bool status);

enum usbd_speed usbd_bus_speed(const struct usbd_context *const uds_ctx);

enum usbd_speed usbd_caps_speed(const struct usbd_context *const uds_ctx);

int usbd_device_set_bcd_usb(struct usbd_context *const uds_ctx,
                            const enum usbd_speed speed, const uint16_t bcd);

int usbd_device_set_vid(struct usbd_context *const uds_ctx,
                         const uint16_t vid);

int usbd_device_set_pid(struct usbd_context *const uds_ctx,
                        const uint16_t pid);

int usbd_device_set_bcd_device(struct usbd_context *const uds_ctx,
                               const uint16_t bcd);

int usbd_device_set_code_triple(struct usbd_context *const uds_ctx,
                                const enum usbd_speed speed,
                                const uint8_t base_class,
                                const uint8_t subclass, const uint8_t protocol);

int usbd_config_attrib_rwup(struct usbd_context *const uds_ctx,
                            const enum usbd_speed speed,
                            const uint8_t cfg, const bool enable);

int usbd_config_attrib_self(struct usbd_context *const uds_ctx,
                            const enum usbd_speed speed,
                            const uint8_t cfg, const bool enable);

int usbd_config_maxpower(struct usbd_context *const uds_ctx,
                         const enum usbd_speed speed,
                         const uint8_t cfg, const uint8_t power);

bool usbd_can_detect_vbus(struct usbd_context *const uds_ctx);

int usbd_device_register_vreq(struct usbd_context *const uds_ctx,
                              struct usbd_vreq_node *const vreq_nd);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_USBD_H_ */
```

## 53.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 40 行

USB 设备协议栈（Device Stack）编译时启用了高速支持（High-Speed Support），则为 1。

### 注释 3：原第 43 行

协议栈支持的最大批量传输包大小（Maximum Bulk Max Packet Size）。

### 注释 4：原第 46 行

字符串描述符长度（String Descriptor Length，`bLength`）由 `bLength` 与 `bDescriptorType` 两个八位字节的大小，加上 UTF-16 小端字符串（UTF16LE String）的长度计算得出：

```c
bLength = 2 + bString_length
bLength = 2 + sizeof(initializer_string) * 2 - 2
bLength = sizeof(initializer_string) * 2
```

使用本宏确定字符串描述符的 `bLength`。

### 注释 5：原第 206 行

待办（TODO）：是否增加 Kconfig 选项 `USBD_NUMOF_INTERFACES_MAX`？

### 注释 6：原第 1294 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USBD_H_`。

## 53.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usbd_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/usb/bos.h](../usb/P151_USBBOS公共头文件.md)
- [zephyr/usb/usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)
- [zephyr/usb/usbd_msg.h](../api_file_configuration_reference/P078_zephyr__usb__usbd_msg.h_文件参考.md)
- [zephyr/drivers/usb/usb_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h.html)
- [zephyr/sys/byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/logging/log.h](../log_core_reference/P003_日志公共头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [usbd_context](../usb/P025_USB设备上下文结构.md)
- [usbd_str_desc_data](../usb/P018_USB字符串描述符数据.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [idx](../usb/P018_USB字符串描述符数据.md#a0654953d15160cc19cad86a407f655cb)
- [utype](../usb/P018_USB字符串描述符数据.md#a2e6dfc9cbbd44457113899db988a84ca)
- [ascii7](../usb/P018_USB字符串描述符数据.md#ad4d7c291f95973d20ff522b8a5ef65a0)
- [use_hwinfo](../usb/P018_USB字符串描述符数据.md#a40459d114a339841e1f9c14b0d036fe8)
- [usbd_vreq_node](../usb/P019_USB厂商请求节点.md)
- [sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)
- [node](../usb/P019_USB厂商请求节点.md#a3c68346e2f871b22fb6c3b282ddfdccb)
- [code](../usb/P019_USB厂商请求节点.md#a91fe4c5cf5ccad89e81380a332a8f955)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [usb_setup_packet](../usb/P160_USB控制请求包.md)
- [to_dev](../usb/P019_USB厂商请求节点.md#ae69e3dd3b4cdc7deb1ccdd9d9ebe4ec3)
- [usbd_bos_desc_data](../usb/P020_USBBOS能力描述符数据.md)
- [utype](../usb/P020_USBBOS能力描述符数据.md#a084578c905400488e5ce73c71f8aaf00)
- [vreq_nd](../usb/P020_USBBOS能力描述符数据.md#a2d8570c88670c4fbf2d79bb989da01d9)
- [usbd_desc_node](../usb/P021_USB描述符节点.md)
- [node](../usb/P021_USB描述符节点.md#a9f1941cd036c01387d8ad9a4aceb595a)
- [str](../usb/P021_USB描述符节点.md#ae34fee200f7fd78355addafe79789cb4)
- [bos](../usb/P021_USB描述符节点.md#afd65079b8b969fa4101a3f9f662c7b6b)
- [ptr](../usb/P021_USB描述符节点.md#ac437b472e012e8fdec049f28e9f88944)
- [bLength](../usb/P021_USB描述符节点.md#ad71ef74fd7fe43a8117704553a3be01c)
- [bDescriptorType](../usb/P021_USB描述符节点.md#a786e2911b5ec7d6c908c148be4d27f5f)
- [usbd_config_node](../usb/P022_USB配置节点.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../usb/P022_USB配置节点.md#a003a8d9132b319f54583263c4da1e060)
- [desc](../usb/P022_USB配置节点.md#a55081d79ab3e6b41a091b3f65d7d2d87)
- [str_desc_nd](../usb/P022_USB配置节点.md#a19203885a9698861f849bd0fd57cb37f)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [class_list](../usb/P022_USB配置节点.md#a00493162af2344d3d39f834b4834ef78)
- [usbd_ch9_state](../usb/P015_USB设备核心API.md#ga95fb708d8a54eaa3ce0acc4e65519bbc)
- [USBD_STATE_DEFAULT](../usb/P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048)
- [USBD_STATE_ADDRESS](../usb/P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d)
- [USBD_STATE_CONFIGURED](../usb/P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509)
- [usbd_ch9_data](../usb/P023_USB第9章运行时数据.md)
- [setup](../usb/P023_USB第9章运行时数据.md#a85f96c69cede5b51c1f9739a4ae67f4d)
- [state](../usb/P023_USB第9章运行时数据.md#a70d1a1be0aab6167ca4f4580b9c65eff)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ep_halt](../usb/P023_USB第9章运行时数据.md#a504360b7cb11240a2fda68344f2e3b62)
- [configuration](../usb/P023_USB第9章运行时数据.md#a1f759fb0d758e50c4589b6b6b1fd2a24)
- [post_status](../usb/P023_USB第9章运行时数据.md#a6ab6f611fd1eff8d6fde0617c587fefb)
- [alternate](../usb/P023_USB第9章运行时数据.md#a8f831eca1974b8411072f8102c444d45)
- [USBD_NUMOF_INTERFACES_MAX](../usb/P015_USB设备核心API.md#gaf8aadd499f7e0438acac4a7f36645d49)
- [usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)
- [USBD_SPEED_FS](../usb/P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7)
- [USBD_SPEED_HS](../usb/P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266)
- [USBD_SPEED_SS](../usb/P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a)
- [usbd_status](../usb/P024_USB设备状态结构.md)
- [initialized](../usb/P024_USB设备状态结构.md#a78de12245d08ecc71e09d5519fe0e857)
- [enabled](../usb/P024_USB设备状态结构.md#a2382fcb655fe51e0bcf83f85aa182ba3)
- [suspended](../usb/P024_USB设备状态结构.md#afb67cfda187e40229f842c93aa09f0ba)
- [rwup](../usb/P024_USB设备状态结构.md#a113085892967cf7c9cb70131b320d61a)
- [self_powered](../usb/P024_USB设备状态结构.md#ae4107cb4f379cce8c0472a98483705b8)
- [speed](../usb/P024_USB设备状态结构.md#a295009d25826732ba9eebd7735d93d23)
- [usbd_msg_cb_t](../usb/P015_USB设备核心API.md#ga2cd074cefff922b0816de37935d9646e)
- [usbd_msg](../usb/P017_USB设备消息结构.md)
- [name](../usb/P025_USB设备上下文结构.md#ade73c224b256007bf2d68bd1205ceb6e)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [mutex](../usb/P025_USB设备上下文结构.md#a8ff2a4303b73db67eeabdd999736b3a6)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../usb/P025_USB设备上下文结构.md#a52c2cc6118b46fbcbc7a495df61f6b6c)
- [msg_cb](../usb/P025_USB设备上下文结构.md#a300ab0384b3d4e7f3d7d188a27a78be3)
- [ep_events](../usb/P025_USB设备上下文结构.md#a7a884c982011034fd02a41d7cb450509)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)
- [ep_event_lock](../usb/P025_USB设备上下文结构.md#ae65f5ae6e67b1e9e302a1d45d59751c3)
- [ch9_data](../usb/P025_USB设备上下文结构.md#a4fb1545ec02e7d38766cee9940edc1eb)
- [sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)
- [descriptors](../usb/P025_USB设备上下文结构.md#adf8dd86f2784cc69ce6da314adc00b72)
- [fs_configs](../usb/P025_USB设备上下文结构.md#a8c7d153a73859dd8ba25265f059f7495)
- [hs_configs](../usb/P025_USB设备上下文结构.md#a4a6bd413d06328ffa5db089e35157376)
- [vreqs](../usb/P025_USB设备上下文结构.md#a6b463c6c01230bc68c50ba5bb5550e99)
- [status](../usb/P025_USB设备上下文结构.md#a3acad44126b6c3d56823ef7408332087)
- [fs_desc](../usb/P025_USB设备上下文结构.md#a193420cc196f115cbd6947b10d542ee5)
- [hs_desc](../usb/P025_USB设备上下文结构.md#a250e2f82c7239ce81b104b6ef3c16857)
- [setup_buf](../usb/P025_USB设备上下文结构.md#aec2fa8e53ddaa2e282e381218171d7bd)
- [usbd_cctx_vendor_req](../usb/P026_USB类厂商请求表.md)
- [reqs](../usb/P026_USB类厂商请求表.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea)
- [len](../usb/P026_USB类厂商请求表.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0)
- [usbd_class_data](../usb/P028_USB类数据结构.md)
- [usbd_class_api](../usb/P027_USB类回调接口.md)
- [feature_halt](../usb/P027_USB类回调接口.md#a09475f1b29f482e548b6bc168dcd19e7)
- [update](../usb/P027_USB类回调接口.md#a11d09e35f9d4c4d6b18e12bf4ea241b0)
- [control_to_dev](../usb/P027_USB类回调接口.md#ab37dd5f2bf4029f149e69046702626a1)
- [request](../usb/P027_USB类回调接口.md#a70425718fd34534fd976240340b4496d)
- [suspended](../usb/P027_USB类回调接口.md#a598afe76b5c2f9e75a049fe785393e04)
- [resumed](../usb/P027_USB类回调接口.md#ae6f3a658e5768f5d6672cd0e5f2d24a5)
- [sof](../usb/P027_USB类回调接口.md#a488b102936b5cd3e4095578119b71510)
- [enable](../usb/P027_USB类回调接口.md#ab42f61db338471f0c5260576680409e9)
- [disable](../usb/P027_USB类回调接口.md#afd43bfa4aab664c50648aa59a0c713de)
- [init](../usb/P027_USB类回调接口.md#a7d749f007d70e30f76aa121067b7a5c6)
- [shutdown](../usb/P027_USB类回调接口.md#a5ca5bc6d3f5220bd3658d9398e09016e)
- [name](../usb/P028_USB类数据结构.md#ad251371b0e401fb2bffd6aaa1ff49063)
- [uds_ctx](../usb/P028_USB类数据结构.md#a111a803092fd389a500fb99bfc71b29a)
- [api](../usb/P028_USB类数据结构.md#a9109af3e25c499d4ef1f0746bf6a20cc)
- [v_reqs](../usb/P028_USB类数据结构.md#a32db83ecf80e1ac9e4d5deda54581deb)
- [priv](../usb/P028_USB类数据结构.md#a10bb5b9af6098fbbc86fd00ef54e84e1)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [usbd_class_get_ctx](../usb/P015_USB设备核心API.md#gaf97c68e75420bd5a1085c047577fd5a7)
- [usbd_class_get_private](../usb/P015_USB设备核心API.md#ga2e511d0341b4e1bd57fb4420512eeeb5)
- [usbd_add_descriptor](../usb/P015_USB设备核心API.md#ga33d0cef23d4b6c62b79b41559427b584)
- [usbd_str_desc_get_idx](../usb/P015_USB设备核心API.md#gab023ab276eb68c644895483344d33948)
- [usbd_remove_descriptor](../usb/P015_USB设备核心API.md#ga3146ee636b84c6d319365716f5741363)
- [usbd_add_configuration](../usb/P015_USB设备核心API.md#ga5f4b69609f9a8f00a9e0fea4dffce1c4)
- [usbd_register_class](../usb/P015_USB设备核心API.md#ga4a837040e9d02c5773d69a6cf6c35960)
- [usbd_register_all_classes](../usb/P015_USB设备核心API.md#ga06541b17f5afc917cc5154bd4d816ec3)
- [usbd_unregister_class](../usb/P015_USB设备核心API.md#ga1ae7a7a04f4ec1206d352d5c6401c51b)
- [usbd_unregister_all_classes](../usb/P015_USB设备核心API.md#ga2996b5f6df459c8a179fc6c22f944063)
- [usbd_msg_register_cb](../usb/P015_USB设备核心API.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38)
- [usbd_init](../usb/P015_USB设备核心API.md#ga78e5f07af641f9610cc32255efe1680f)
- [usbd_enable](../usb/P015_USB设备核心API.md#ga1a40fc13129e9218ca63ab3ca70d8d68)
- [usbd_disable](../usb/P015_USB设备核心API.md#gaaa21e9f33175b7d2434e54e1b3d2799b)
- [usbd_shutdown](../usb/P015_USB设备核心API.md#ga37585e0124a4d0d8cf6e65f13325eaf0)
- [usbd_ep_set_halt](../usb/P015_USB设备核心API.md#ga176f42b2dd221c0de28ad9122a7d2693)
- [usbd_ep_clear_halt](../usb/P015_USB设备核心API.md#ga03729a4e9add3a55a7c3c2c8666a53a7)
- [usbd_ep_is_halted](../usb/P015_USB设备核心API.md#ga94cb8465b7bf85457f29e84b5b8ddfe9)
- [usbd_ep_buf_alloc](../usb/P015_USB设备核心API.md#ga6c671d49c811b0af6b809f5940cd6d70)
- [size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [usbd_ep_ctrl_data_in_alloc](../usb/P015_USB设备核心API.md#ga1ce934ca354853ec9c7c295cca2d0e3d)
- [usbd_ep_ctrl_enqueue](../usb/P015_USB设备核心API.md#ga967d507d82d912119a732fd230bd561e)
- [usbd_ep_enqueue](../usb/P015_USB设备核心API.md#gaabf8333a7aefc4428f38e79a7264e383)
- [usbd_ep_dequeue](../usb/P015_USB设备核心API.md#ga1534058a609794e1d080aed98fcf5823)
- [usbd_ep_buf_free](../usb/P015_USB设备核心API.md#ga8aa454c24495f2a462eae53b78c488dc)
- [usbd_is_suspended](../usb/P015_USB设备核心API.md#ga5f7a5af958f7de8893e04ff2b7748c7e)
- [usbd_wakeup_request](../usb/P015_USB设备核心API.md#ga34086553e74795ffdc000349e61a3c8b)
- [usbd_self_powered](../usb/P015_USB设备核心API.md#ga9056e1f01b64ddd26db6a5ee45439e22)
- [usbd_bus_speed](../usb/P015_USB设备核心API.md#gab4a0d05a8f183f7479ad33ee29e8a611)
- [usbd_caps_speed](../usb/P015_USB设备核心API.md#gaab7c4692a30b58aa76b03b9e50460856)
- [usbd_device_set_bcd_usb](../usb/P015_USB设备核心API.md#gacb704bd4f396887c859932b2ab6b4991)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [usbd_device_set_vid](../usb/P015_USB设备核心API.md#ga06aa9f954b6765e07494753bb4fa42d4)
- [usbd_device_set_pid](../usb/P015_USB设备核心API.md#ga44719fc03a50c70d75ce65e1d2f77a04)
- [usbd_device_set_bcd_device](../usb/P015_USB设备核心API.md#gafda88e8a71c52addbe76ebeb874a8af5)
- [usbd_device_set_code_triple](../usb/P015_USB设备核心API.md#ga83a58b50bec680513eabd3bb7075b511)
- [usbd_config_attrib_rwup](../usb/P015_USB设备核心API.md#ga2b803f8ac10d9375a74949cd2c2f3136)
- [usbd_config_attrib_self](../usb/P015_USB设备核心API.md#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade)
- [usbd_config_maxpower](../usb/P015_USB设备核心API.md#ga59fc1ea6d943d26b0207bb6060e18f08)
- [usbd_can_detect_vbus](../usb/P015_USB设备核心API.md#ga5ea40d893980e24294e82d22855b407c)
- [usbd_device_register_vreq](../usb/P015_USB设备核心API.md#gaaebba63d8a8b78a1f06c1a5a476cd306)
- [bos.h](../usb/P151_USBBOS公共头文件.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [log.h](../log_core_reference/P003_日志公共头文件参考.md)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [net_buf::size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [usbd_bos_desc_data::utype](../usb/P020_USBBOS能力描述符数据.md#a084578c905400488e5ce73c71f8aaf00)
- [usbd_bos_desc_data::vreq_nd](../usb/P020_USBBOS能力描述符数据.md#a2d8570c88670c4fbf2d79bb989da01d9)
- [usbd_cctx_vendor_req::reqs](../usb/P026_USB类厂商请求表.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea)
- [usbd_cctx_vendor_req::len](../usb/P026_USB类厂商请求表.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0)
- [usbd_ch9_data::configuration](../usb/P023_USB第9章运行时数据.md#a1f759fb0d758e50c4589b6b6b1fd2a24)
- [usbd_ch9_data::ep_halt](../usb/P023_USB第9章运行时数据.md#a504360b7cb11240a2fda68344f2e3b62)
- [usbd_ch9_data::post_status](../usb/P023_USB第9章运行时数据.md#a6ab6f611fd1eff8d6fde0617c587fefb)
- [usbd_ch9_data::state](../usb/P023_USB第9章运行时数据.md#a70d1a1be0aab6167ca4f4580b9c65eff)
- [usbd_ch9_data::setup](../usb/P023_USB第9章运行时数据.md#a85f96c69cede5b51c1f9739a4ae67f4d)
- [usbd_ch9_data::alternate](../usb/P023_USB第9章运行时数据.md#a8f831eca1974b8411072f8102c444d45)
- [usbd_class_api::feature_halt](../usb/P027_USB类回调接口.md#a09475f1b29f482e548b6bc168dcd19e7)
- [usbd_class_api::update](../usb/P027_USB类回调接口.md#a11d09e35f9d4c4d6b18e12bf4ea241b0)
- [usbd_class_api::sof](../usb/P027_USB类回调接口.md#a488b102936b5cd3e4095578119b71510)
- [usbd_class_api::suspended](../usb/P027_USB类回调接口.md#a598afe76b5c2f9e75a049fe785393e04)
- [usbd_class_api::shutdown](../usb/P027_USB类回调接口.md#a5ca5bc6d3f5220bd3658d9398e09016e)
- [usbd_class_api::request](../usb/P027_USB类回调接口.md#a70425718fd34534fd976240340b4496d)
- [usbd_class_api::init](../usb/P027_USB类回调接口.md#a7d749f007d70e30f76aa121067b7a5c6)
- [usbd_class_api::control_to_dev](../usb/P027_USB类回调接口.md#ab37dd5f2bf4029f149e69046702626a1)
- [usbd_class_api::enable](../usb/P027_USB类回调接口.md#ab42f61db338471f0c5260576680409e9)
- [usbd_class_api::resumed](../usb/P027_USB类回调接口.md#ae6f3a658e5768f5d6672cd0e5f2d24a5)
- [usbd_class_api::disable](../usb/P027_USB类回调接口.md#afd43bfa4aab664c50648aa59a0c713de)
- [usbd_class_data::priv](../usb/P028_USB类数据结构.md#a10bb5b9af6098fbbc86fd00ef54e84e1)
- [usbd_class_data::uds_ctx](../usb/P028_USB类数据结构.md#a111a803092fd389a500fb99bfc71b29a)
- [usbd_class_data::v_reqs](../usb/P028_USB类数据结构.md#a32db83ecf80e1ac9e4d5deda54581deb)
- [usbd_class_data::api](../usb/P028_USB类数据结构.md#a9109af3e25c499d4ef1f0746bf6a20cc)
- [usbd_class_data::name](../usb/P028_USB类数据结构.md#ad251371b0e401fb2bffd6aaa1ff49063)
- [usbd_config_node::node](../usb/P022_USB配置节点.md#a003a8d9132b319f54583263c4da1e060)
- [usbd_config_node::class_list](../usb/P022_USB配置节点.md#a00493162af2344d3d39f834b4834ef78)
- [usbd_config_node::str_desc_nd](../usb/P022_USB配置节点.md#a19203885a9698861f849bd0fd57cb37f)
- [usbd_config_node::desc](../usb/P022_USB配置节点.md#a55081d79ab3e6b41a091b3f65d7d2d87)
- [usbd_context::fs_desc](../usb/P025_USB设备上下文结构.md#a193420cc196f115cbd6947b10d542ee5)
- [usbd_context::hs_desc](../usb/P025_USB设备上下文结构.md#a250e2f82c7239ce81b104b6ef3c16857)
- [usbd_context::msg_cb](../usb/P025_USB设备上下文结构.md#a300ab0384b3d4e7f3d7d188a27a78be3)
- [usbd_context::status](../usb/P025_USB设备上下文结构.md#a3acad44126b6c3d56823ef7408332087)
- [usbd_context::hs_configs](../usb/P025_USB设备上下文结构.md#a4a6bd413d06328ffa5db089e35157376)
- [usbd_context::ch9_data](../usb/P025_USB设备上下文结构.md#a4fb1545ec02e7d38766cee9940edc1eb)
- [usbd_context::dev](../usb/P025_USB设备上下文结构.md#a52c2cc6118b46fbcbc7a495df61f6b6c)
- [usbd_context::vreqs](../usb/P025_USB设备上下文结构.md#a6b463c6c01230bc68c50ba5bb5550e99)
- [usbd_context::ep_events](../usb/P025_USB设备上下文结构.md#a7a884c982011034fd02a41d7cb450509)
- [usbd_context::fs_configs](../usb/P025_USB设备上下文结构.md#a8c7d153a73859dd8ba25265f059f7495)
- [usbd_context::mutex](../usb/P025_USB设备上下文结构.md#a8ff2a4303b73db67eeabdd999736b3a6)
- [usbd_context::name](../usb/P025_USB设备上下文结构.md#ade73c224b256007bf2d68bd1205ceb6e)
- [usbd_context::descriptors](../usb/P025_USB设备上下文结构.md#adf8dd86f2784cc69ce6da314adc00b72)
- [usbd_context::ep_event_lock](../usb/P025_USB设备上下文结构.md#ae65f5ae6e67b1e9e302a1d45d59751c3)
- [usbd_context::setup_buf](../usb/P025_USB设备上下文结构.md#aec2fa8e53ddaa2e282e381218171d7bd)
- [usbd_desc_node::bDescriptorType](../usb/P021_USB描述符节点.md#a786e2911b5ec7d6c908c148be4d27f5f)
- [usbd_desc_node::node](../usb/P021_USB描述符节点.md#a9f1941cd036c01387d8ad9a4aceb595a)
- [usbd_desc_node::ptr](../usb/P021_USB描述符节点.md#ac437b472e012e8fdec049f28e9f88944)
- [usbd_desc_node::bLength](../usb/P021_USB描述符节点.md#ad71ef74fd7fe43a8117704553a3be01c)
- [usbd_desc_node::str](../usb/P021_USB描述符节点.md#ae34fee200f7fd78355addafe79789cb4)
- [usbd_desc_node::bos](../usb/P021_USB描述符节点.md#afd65079b8b969fa4101a3f9f662c7b6b)
- [usbd_status::rwup](../usb/P024_USB设备状态结构.md#a113085892967cf7c9cb70131b320d61a)
- [usbd_status::enabled](../usb/P024_USB设备状态结构.md#a2382fcb655fe51e0bcf83f85aa182ba3)
- [usbd_status::speed](../usb/P024_USB设备状态结构.md#a295009d25826732ba9eebd7735d93d23)
- [usbd_status::initialized](../usb/P024_USB设备状态结构.md#a78de12245d08ecc71e09d5519fe0e857)
- [usbd_status::self_powered](../usb/P024_USB设备状态结构.md#ae4107cb4f379cce8c0472a98483705b8)
- [usbd_status::suspended](../usb/P024_USB设备状态结构.md#afb67cfda187e40229f842c93aa09f0ba)
- [usbd_str_desc_data::idx](../usb/P018_USB字符串描述符数据.md#a0654953d15160cc19cad86a407f655cb)
- [usbd_str_desc_data::utype](../usb/P018_USB字符串描述符数据.md#a2e6dfc9cbbd44457113899db988a84ca)
- [usbd_str_desc_data::use_hwinfo](../usb/P018_USB字符串描述符数据.md#a40459d114a339841e1f9c14b0d036fe8)
- [usbd_str_desc_data::ascii7](../usb/P018_USB字符串描述符数据.md#ad4d7c291f95973d20ff522b8a5ef65a0)
- [usbd_vreq_node::node](../usb/P019_USB厂商请求节点.md#a3c68346e2f871b22fb6c3b282ddfdccb)
- [usbd_vreq_node::code](../usb/P019_USB厂商请求节点.md#a91fe4c5cf5ccad89e81380a332a8f955)
- [usbd_vreq_node::to_dev](../usb/P019_USB厂商请求节点.md#ae69e3dd3b4cdc7deb1ccdd9d9ebe4ec3)
- [byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [usb_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h.html)
- [usb_ch9.h](../usb/P172_USB标准请求与描述符常量.md)
- [usbd_msg.h](../api_file_configuration_reference/P078_zephyr__usb__usbd_msg.h_文件参考.md)

---

[上一章](P052_syslog.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P054_veml7700.h_源码浏览.md)
