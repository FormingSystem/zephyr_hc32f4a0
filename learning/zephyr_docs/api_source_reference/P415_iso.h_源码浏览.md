---
id: learning.zephyr-docs.api-source-reference.page-415
title: iso.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第415章\_iso.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h.html)。

## 415.1\_原始可见代码（Source Code）

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
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
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
<a id="l00167"></a>
<a id="l00168"></a>
<a id="foldopen00174"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="foldopen00196"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="foldopen00205"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="foldopen00219"></a>
<a id="l00219"></a>
<a id="l00225"></a>
<a id="l00231"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="foldopen00261"></a>
<a id="l00261"></a>
<a id="l00269"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="foldopen00293"></a>
<a id="l00293"></a>
<a id="l00300"></a>
<a id="l00306"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="foldopen00352"></a>
<a id="l00352"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="foldopen00368"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="foldopen00386"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="foldopen00485"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="foldopen00500"></a>
<a id="l00500"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="foldopen00589"></a>
<a id="l00589"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="foldopen00648"></a>
<a id="l00648"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00674"></a>
<a id="l00675"></a>
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
<a id="l00691"></a>
<a id="foldopen00703"></a>
<a id="l00703"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="foldopen00791"></a>
<a id="l00791"></a>
<a id="l00793"></a>
<a id="l00794"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="foldopen00811"></a>
<a id="l00811"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00846"></a>
<a id="l00847"></a>
<a id="l00857"></a>
<a id="l00858"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="l00987"></a>
<a id="l00988"></a>
<a id="l01011"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="l01035"></a>
<a id="l01036"></a>
<a id="l01037"></a>
<a id="l01076"></a>
<a id="l01077"></a>
<a id="foldopen01079"></a>
<a id="l01079"></a>
<a id="l01081"></a>
<a id="l01082"></a>
<a id="l01084"></a>
<a id="l01085"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01093"></a>
<a id="l01094"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01105"></a>
<a id="l01106"></a>
<a id="l01107"></a>
<a id="foldopen01109"></a>
<a id="l01109"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01114"></a>
<a id="l01115"></a>
<a id="l01117"></a>
<a id="l01118"></a>
<a id="l01120"></a>
<a id="l01121"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01131"></a>
<a id="l01132"></a>
<a id="l01134"></a>
<a id="l01135"></a>
<a id="l01136"></a>
<a id="foldopen01138"></a>
<a id="l01138"></a>
<a id="l01140"></a>
<a id="l01141"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01146"></a>
<a id="l01147"></a>
<a id="l01149"></a>
<a id="l01150"></a>
<a id="l01152"></a>
<a id="l01153"></a>
<a id="l01155"></a>
<a id="l01156"></a>
<a id="l01158"></a>
<a id="l01159"></a>
<a id="l01161"></a>
<a id="l01162"></a>
<a id="l01164"></a>
<a id="l01165"></a>
<a id="l01166"></a>
<a id="foldopen01168"></a>
<a id="l01168"></a>
<a id="l01170"></a>
<a id="l01171"></a>
<a id="l01173"></a>
<a id="l01174"></a>
<a id="l01176"></a>
<a id="l01177"></a>
<a id="l01179"></a>
<a id="l01180"></a>
<a id="l01182"></a>
<a id="l01183"></a>
<a id="l01185"></a>
<a id="l01186"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="foldopen01192"></a>
<a id="l01192"></a>
<a id="l01194"></a>
<a id="l01195"></a>
<a id="l01197"></a>
<a id="l01198"></a>
<a id="l01200"></a>
<a id="l01201"></a>
<a id="l01208"></a>
<a id="l01209"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01228"></a>
<a id="l01229"></a>
<a id="l01230"></a>
<a id="l01237"></a>
<a id="l01238"></a>
<a id="l01239"></a>
<a id="l01246"></a>
<a id="l01247"></a>
<a id="l01248"></a>
<a id="l01249"></a>
<a id="l01250"></a>
<a id="l01259"></a>
<a id="l01260"></a>
<a id="l01276"></a>
<a id="l01277"></a>
<a id="foldopen01283"></a>
<a id="l01283"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="l01297"></a>
<a id="l01298"></a>
<a id="l01300"></a>
<a id="l01301"></a>
<a id="l01302"></a>
<a id="l01312"></a>
<a id="l01313"></a>
<a id="l01325"></a>
<a id="l01326"></a>
<a id="l01327"></a>
<a id="l01338"></a>
<a id="l01339"></a>
<a id="l01349"></a>
<a id="l01350"></a>
<a id="l01351"></a>
<a id="l01358"></a>
<a id="l01359"></a>
<a id="l01360"></a>
<a id="l01361"></a>
<a id="l01362"></a>
<a id="l01363"></a>
<a id="l01367"></a>
<a id="l01368"></a>
<a id="aaddr_8h_html"></a>
<a id="aatomic_8h_html"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="abuf_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__iso_html_ga0dbb89a133011a833be7d18161471c6a"></a>
<a id="agroup__bt__iso_html_ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6"></a>
<a id="agroup__bt__iso_html_ga4d4c9b8d6d83abcc8d3b337101922800"></a>
<a id="agroup__bt__iso_html_ga53be464e005392676830feeddd8cdc22"></a>
<a id="agroup__bt__iso_html_ga5551cab9896764eec39b8e6102e561e5"></a>
<a id="agroup__bt__iso_html_ga75e58ed5bfa48f84000f1ce974d649c6"></a>
<a id="agroup__bt__iso_html_ga790cfeb8516020f317802e019dca4754"></a>
<a id="agroup__bt__iso_html_ga8a01a56e4a4555ed65a67065facfca76"></a>
<a id="agroup__bt__iso_html_ga94c5c788b099284219e5a303b4b8ea69"></a>
<a id="agroup__bt__iso_html_ga98953a261f3699b62cd19ab4977e0b4c"></a>
<a id="agroup__bt__iso_html_ga98f557c183a82066b81f0265c225bebe"></a>
<a id="agroup__bt__iso_html_gaa3407502145a77e08993220f7ce51b4a"></a>
<a id="agroup__bt__iso_html_gaa3942147fdeebc36039cc35c4e984411"></a>
<a id="agroup__bt__iso_html_gaa74c762451cfb5d04ffcd8d396a75447"></a>
<a id="agroup__bt__iso_html_gab75b817770e3b685920587afde39d6cd"></a>
<a id="agroup__bt__iso_html_gab9c06a86bf5cc023f5f9bd16c5d3265b"></a>
<a id="agroup__bt__iso_html_gac9937316382d257493c7d0359f1341f5"></a>
<a id="agroup__bt__iso_html_gad4b6a7286593ff099117113b6ca996f8"></a>
<a id="agroup__bt__iso_html_gaea03fc251206f18de320506064c1631f"></a>
<a id="agroup__bt__iso_html_gaf2925460cc22cc4220dc376bcbee6201"></a>
<a id="agroup__bt__iso_html_gafcbd720c67c6a6e5f1cae1395e1e06f0"></a>
<a id="agroup__bt__iso_html_gaff0e52777b2140519c63b54b9618bca8"></a>
<a id="agroup__bt__iso_html_gga2c62af103a71aa8f5f8aa103b1245866a143de2c153179b3c40aca51c016e6382"></a>
<a id="agroup__bt__iso_html_gga2c62af103a71aa8f5f8aa103b1245866a5e87d48b6e96275744590194b75396ff"></a>
<a id="agroup__bt__iso_html_gga2c62af103a71aa8f5f8aa103b1245866a5f0aa6e3150819821f800dd7376e2218"></a>
<a id="agroup__bt__iso_html_gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23"></a>
<a id="agroup__bt__iso_html_ggaf2925460cc22cc4220dc376bcbee6201a4cb48a0a2a2ac37bbab5eded1bc3fd22"></a>
<a id="agroup__bt__iso_html_ggaf2925460cc22cc4220dc376bcbee6201acfa2a00a1c203418768ce789cd0cec7d"></a>
<a id="agroup__bt__iso_html_ggaf2925460cc22cc4220dc376bcbee6201aebc34f9c32f1cd5e3197c7edaf657340"></a>
<a id="agroup__bt__iso_html_ggaf2925460cc22cc4220dc376bcbee6201af392f8825090c7beb304efc860a1911d"></a>
<a id="agroup__bt__iso_html_ggafcbd720c67c6a6e5f1cae1395e1e06f0a46a0148a474b297d38d67fb18bdb410a"></a>
<a id="agroup__bt__iso_html_ggafcbd720c67c6a6e5f1cae1395e1e06f0a58579ee03e3769501536826248758f17"></a>
<a id="agroup__bt__iso_html_ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b"></a>
<a id="agroup__bt__iso_html_ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2"></a>
<a id="agroup__bt__iso_html_ggafcbd720c67c6a6e5f1cae1395e1e06f0aa8b51a9ebacbaaac90956d7a9a816edb"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="ahci_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__addr__le__t_html"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__iso__accept__info_html"></a>
<a id="astructbt__iso__accept__info_html_a4225ccc90f1e17e26ce61fe398f506d1"></a>
<a id="astructbt__iso__accept__info_html_a688809132997c37a6fe2529498a4ee0e"></a>
<a id="astructbt__iso__accept__info_html_a88002043a67c89c8d518ebdf92cf8847"></a>
<a id="astructbt__iso__big__cb_html"></a>
<a id="astructbt__iso__big__cb_html_a43d6ee745f7852460f843ced33c777c2"></a>
<a id="astructbt__iso__big__cb_html_ac84e00545dbb330311482eb5abd4a78b"></a>
<a id="astructbt__iso__big__create__param_html"></a>
<a id="astructbt__iso__big__create__param_html_a1288fa2a8f6bb3e2ab26729e245277e1"></a>
<a id="astructbt__iso__big__create__param_html_a63cd16824e9d09e29d3c7e135b08d932"></a>
<a id="astructbt__iso__big__create__param_html_a7548bbb75f240a70435cb86a48846d0a"></a>
<a id="astructbt__iso__big__create__param_html_a7aaef1f7a78ae1088886a78739fd6849"></a>
<a id="astructbt__iso__big__create__param_html_a8ae9c225798e9f5b72fe0b8c3b6f2cf0"></a>
<a id="astructbt__iso__big__create__param_html_aab0e9f66cb10643e72d6382718ed4c0d"></a>
<a id="astructbt__iso__big__create__param_html_ab847021da2e604036cecf90483e12132"></a>
<a id="astructbt__iso__big__create__param_html_ad478d7b36fb34b8e57a25ae0029e4c51"></a>
<a id="astructbt__iso__big__create__param_html_ad931ff1f19f92c29c40d934346498e79"></a>
<a id="astructbt__iso__big__create__param_html_ae7a68301c2a0ea7a81812581f3ab1e61"></a>
<a id="astructbt__iso__big__create__param_html_affce506bd271d9b0e497160c163c5798"></a>
<a id="astructbt__iso__big__sync__param_html"></a>
<a id="astructbt__iso__big__sync__param_html_a14b03509daf760edbead86659f733136"></a>
<a id="astructbt__iso__big__sync__param_html_a16b332b4a0f373cb21e5da6e6e383b9e"></a>
<a id="astructbt__iso__big__sync__param_html_a8e344870fc0e380e6588eb90c7ef72f9"></a>
<a id="astructbt__iso__big__sync__param_html_a8e5cffe8960477e7f64707d7dd4191f6"></a>
<a id="astructbt__iso__big__sync__param_html_a96cd109e9f5820531635d48e88b4bff8"></a>
<a id="astructbt__iso__big__sync__param_html_ac47bfe3ee0c46f5d55d38f24835ac48d"></a>
<a id="astructbt__iso__big__sync__param_html_ac56d7206c3434837a52059716355adad"></a>
<a id="astructbt__iso__big_html"></a>
<a id="astructbt__iso__biginfo_html"></a>
<a id="astructbt__iso__biginfo_html_a1084c209d122d2d13244b77659ce28dd"></a>
<a id="astructbt__iso__biginfo_html_a10eb24596a4353da3feb0d30fed35ae7"></a>
<a id="astructbt__iso__biginfo_html_a24eb83f7b54e9f949cc07e9955b4a8b8"></a>
<a id="astructbt__iso__biginfo_html_a2cbaf6a89e8aaf62c7048e04523e57d4"></a>
<a id="astructbt__iso__biginfo_html_a4a6d6cdea56a69a0b3b3fd021489750d"></a>
<a id="astructbt__iso__biginfo_html_a4efb91dc2f249e41c65cd0dcbfe45bad"></a>
<a id="astructbt__iso__biginfo_html_a78e0a53f920980081d7b0702b02cf386"></a>
<a id="astructbt__iso__biginfo_html_a7d54ecb896c0d6bc590311d5d5a3ac7b"></a>
<a id="astructbt__iso__biginfo_html_a8458f6d6ebe936212d928caca61b13bd"></a>
<a id="astructbt__iso__biginfo_html_a9fddcb74f3de7eb857583a0179427f84"></a>
<a id="astructbt__iso__biginfo_html_aa7dbfd342eecf8ffc2fce9d3fa7209ea"></a>
<a id="astructbt__iso__biginfo_html_ad114dd97500d12242da77e8522133953"></a>
<a id="astructbt__iso__biginfo_html_af356aa29aa82c8deb63a9f47e54070a1"></a>
<a id="astructbt__iso__biginfo_html_afe96caf570314731f6c543b40d7def9a"></a>
<a id="astructbt__iso__broadcaster__info_html"></a>
<a id="astructbt__iso__broadcaster__info_html_a1defaab3c9fbbe1c91f076ece50ad7b0"></a>
<a id="astructbt__iso__broadcaster__info_html_a3d4e44a1da54e5ca0f2002ca3f6e7a13"></a>
<a id="astructbt__iso__broadcaster__info_html_a577370ab24ebd4d80db4d8ffdb918483"></a>
<a id="astructbt__iso__broadcaster__info_html_a71388f9b64510ab91c3147f05f775aeb"></a>
<a id="astructbt__iso__broadcaster__info_html_a9f93161fb7f81d5eb3a55f955be1b85d"></a>
<a id="astructbt__iso__broadcaster__info_html_aa57b6e08cf4d3d154762c8c43de0f2cf"></a>
<a id="astructbt__iso__broadcaster__info_html_aae07a2b0b2a56a5abb290f9345127c4f"></a>
<a id="astructbt__iso__broadcaster__info_html_ab3cb80e6b362e093e6924ab11b8737e9"></a>
<a id="astructbt__iso__broadcaster__info_html_ac1feade59bbad1e08418e1808619f775"></a>
<a id="astructbt__iso__chan__io__qos_html"></a>
<a id="astructbt__iso__chan__io__qos_html_a2180a4f82e4cdf5288b7f67701a16ad6"></a>
<a id="astructbt__iso__chan__io__qos_html_a5106bfd09f6be52604e7c7f0e3390684"></a>
<a id="astructbt__iso__chan__io__qos_html_ac64a3ce7282ac8bc5b5420a46417b22c"></a>
<a id="astructbt__iso__chan__io__qos_html_ae52611dc326b6777620ff7aa43f566e9"></a>
<a id="astructbt__iso__chan__io__qos_html_ae9e7678a63030353eea65152d89464cd"></a>
<a id="astructbt__iso__chan__ops_html"></a>
<a id="astructbt__iso__chan__ops_html_a048954070628229b8aacd373de1fb236"></a>
<a id="astructbt__iso__chan__ops_html_a2069849352019362e5dc7d68f835f359"></a>
<a id="astructbt__iso__chan__ops_html_a6b0e51770158da7b728e1084a8e44504"></a>
<a id="astructbt__iso__chan__ops_html_a6d5d9423fff83f8f337f97b3fc018f39"></a>
<a id="astructbt__iso__chan__ops_html_a750ac5c12155602a32b1f02bb2dc8fba"></a>
<a id="astructbt__iso__chan__path_html"></a>
<a id="astructbt__iso__chan__path_html_a0da75c4911a197fed7fd7f17c76dddae"></a>
<a id="astructbt__iso__chan__path_html_a519c884281207d1165a61ccfb7fbcdf4"></a>
<a id="astructbt__iso__chan__path_html_a5e4fb798376489a38a87e4052ff85550"></a>
<a id="astructbt__iso__chan__path_html_a95db7917f7b9e90a33f494233c3266eb"></a>
<a id="astructbt__iso__chan__path_html_ac370bfca109153db02a747120c227104"></a>
<a id="astructbt__iso__chan__path_html_adaed07de7e09263e3e941817eeb44258"></a>
<a id="astructbt__iso__chan__path_html_aebc12293ba0b10a87f1852e2a3e53a23"></a>
<a id="astructbt__iso__chan__qos_html"></a>
<a id="astructbt__iso__chan__qos_html_a47a99a6ccfa5f1e0c9fb859e66d2e9e3"></a>
<a id="astructbt__iso__chan__qos_html_a4c6bfa577f8cbd724ed2561850fd6255"></a>
<a id="astructbt__iso__chan__qos_html_ac231434d1798f431c4fbac5a759784a5"></a>
<a id="astructbt__iso__chan_html"></a>
<a id="astructbt__iso__chan_html_a214fe133602ac8dcfaaec7f372e12da8"></a>
<a id="astructbt__iso__chan_html_a2b0fc7180d1983ee4a415c5331bed93d"></a>
<a id="astructbt__iso__chan_html_a7fd728385a3aec11be8883bdee8aedea"></a>
<a id="astructbt__iso__chan_html_aba7bf6dcad93b121c46daa6ad473a51c"></a>
<a id="astructbt__iso__chan_html_abe94fca71506bd590d9ef4465258914d"></a>
<a id="astructbt__iso__cig__param_html"></a>
<a id="astructbt__iso__cig__param_html_a36d2eaa4fd3e08988d4c49ca0902a882"></a>
<a id="astructbt__iso__cig__param_html_a3908eadf3080731cb891e803162d321c"></a>
<a id="astructbt__iso__cig__param_html_a4a09f9f6e7a8db17c3037c9f1761b18a"></a>
<a id="astructbt__iso__cig__param_html_a69c12b704b9897d88b71bc96bd2d3024"></a>
<a id="astructbt__iso__cig__param_html_a83fdc5374f341a421e1394b08297cdff"></a>
<a id="astructbt__iso__cig__param_html_a841dee850f3161bd8e904376792c8ad7"></a>
<a id="astructbt__iso__cig__param_html_a85641a8f01d63b4221c013815c055526"></a>
<a id="astructbt__iso__cig__param_html_aadc3762f3fec3127014378fe58c5b684"></a>
<a id="astructbt__iso__cig__param_html_ab222cdb0af475180dd715b4f5658dc65"></a>
<a id="astructbt__iso__cig__param_html_ad1725e09a397e83d1cc88ebd3a60ed93"></a>
<a id="astructbt__iso__cig__param_html_ad7349213bab902a68c726da51fac2306"></a>
<a id="astructbt__iso__cig__param_html_aeffe10e87d81285196e931dcad2882ba"></a>
<a id="astructbt__iso__cig_html"></a>
<a id="astructbt__iso__connect__param_html"></a>
<a id="astructbt__iso__connect__param_html_aba2f3838e03a1e31699a4623ba93d372"></a>
<a id="astructbt__iso__connect__param_html_ad004956584d2d065d8c0c52959f350d5"></a>
<a id="astructbt__iso__info_html"></a>
<a id="astructbt__iso__info_html_a02554d9114dc3e34305a8e986d906cbe"></a>
<a id="astructbt__iso__info_html_a423474bd89ecdc614e6dfb8ea84db27e"></a>
<a id="astructbt__iso__info_html_a4ead7e3c5ab496b6cfc2becfaddb3746"></a>
<a id="astructbt__iso__info_html_a53c6c8eee63cd674d54dc1d40aa33a43"></a>
<a id="astructbt__iso__info_html_a94e8132738697efa39857612399385b8"></a>
<a id="astructbt__iso__info_html_a9e00edb4e09bae39a37956011ccca353"></a>
<a id="astructbt__iso__info_html_ac1edf09109a5e40a4f675281a7d9e300"></a>
<a id="astructbt__iso__info_html_af01766b8eed556ca165222d19ff05838"></a>
<a id="astructbt__iso__recv__info_html"></a>
<a id="astructbt__iso__recv__info_html_a0a7842fcb3251ed89b99fde43ba235a5"></a>
<a id="astructbt__iso__recv__info_html_a4bf778ae9be39eb4a740c2eb9670d98a"></a>
<a id="astructbt__iso__recv__info_html_a7c5b950df0359bb561140d0c2726fae6"></a>
<a id="astructbt__iso__server_html"></a>
<a id="astructbt__iso__server_html_ae67a000ae524cba53b6bda503568ba38"></a>
<a id="astructbt__iso__sync__receiver__info_html"></a>
<a id="astructbt__iso__sync__receiver__info_html_a24bad4231eb214a2c95b1da9ba59c284"></a>
<a id="astructbt__iso__sync__receiver__info_html_a40ff5a4d691a75802f211a63b1e12303"></a>
<a id="astructbt__iso__sync__receiver__info_html_a55e2d87a45234bce1d54a7330164cd0d"></a>
<a id="astructbt__iso__sync__receiver__info_html_a6185a7ac123be930650da6dc84c0c1e0"></a>
<a id="astructbt__iso__sync__receiver__info_html_a80ac6e529491156109955219569fdec6"></a>
<a id="astructbt__iso__sync__receiver__info_html_a8be50f8c6d76515ac290407959eaf0e1"></a>
<a id="astructbt__iso__sync__receiver__info_html_af2857439c483fdd455c7ccaf66f5fb35"></a>
<a id="astructbt__iso__tx__info_html"></a>
<a id="astructbt__iso__tx__info_html_a0cff6aa2893fdc11160e4327afebed13"></a>
<a id="astructbt__iso__tx__info_html_a2791edea2f4f4459acc24c8dbaa33ded"></a>
<a id="astructbt__iso__tx__info_html_ac8a6a4c073e4df1553d32339a6e4b051"></a>
<a id="astructbt__iso__unicast__info_html"></a>
<a id="astructbt__iso__unicast__info_html_a029c450e2324bbc6ee8fda6d1d10deef"></a>
<a id="astructbt__iso__unicast__info_html_a03b084fefcab049efbe1a609a59d9c54"></a>
<a id="astructbt__iso__unicast__info_html_a196ff16e4e959fa656d4af265e686f09"></a>
<a id="astructbt__iso__unicast__info_html_a4d53dc6adc8d5519cf74982aa5031e74"></a>
<a id="astructbt__iso__unicast__info_html_a4fc402b934ae8aa65493df01c88cae34"></a>
<a id="astructbt__iso__unicast__info_html_abc61e1d8edcb099a02054db8ec94ba22"></a>
<a id="astructbt__iso__unicast__info_html_acbc8c068907eba204d369cf76f4f112d"></a>
<a id="astructbt__iso__unicast__tx__info_html"></a>
<a id="astructbt__iso__unicast__tx__info_html_a14548ee24fad8a26287aa0daba451a47"></a>
<a id="astructbt__iso__unicast__tx__info_html_a3134e0bdb663ad7184e23531504233a5"></a>
<a id="astructbt__iso__unicast__tx__info_html_a7bed74a67bb73f6919d2817d82bcf996"></a>
<a id="astructbt__iso__unicast__tx__info_html_aaf1f623eac2f84ca06082776179b71c5"></a>
<a id="astructbt__iso__unicast__tx__info_html_ab4ea9d5bb535d29ae9406e948d8707a9"></a>
<a id="astructbt__iso__unicast__tx__info_html_adc91f9c200199400a84322a58d28a933"></a>
<a id="astructbt__iso__unicast__tx__info_html_afe7dce9255613e5e2939d3719c720822"></a>
<a id="astructbt__le__ext__adv_html"></a>
<a id="astructbt__le__per__adv__sync_html"></a>
<a id="astructnet__buf_html"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2020 Intel Corporation
 * Copyright (c) 2021-2025 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_ISO_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_ISO_H_


#include <stdint.h>
#include <stddef.h>

#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/buf.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/hci.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_ISO_CHAN_SEND_RESERVE BT_BUF_ISO_SIZE(0)

#define BT_ISO_SDU_BUF_SIZE(mtu) BT_BUF_ISO_SIZE(mtu)

#define BT_ISO_BIS_INDEX_BIT(x) (BIT((x) - 1))

#define BT_ISO_DATA_PATH_HCI        0x00

#define BT_ISO_SDU_INTERVAL_UNKNOWN 0x000000U
#define BT_ISO_DATA_PATH_VS_ID_MIN  0x01
#define BT_ISO_DATA_PATH_VS_ID_MAX  0xFE
#define BT_ISO_CONTROLLER_DELAY_MIN 0x000000
#define BT_ISO_CONTROLLER_DELAY_MAX 0x3D0900
#define BT_ISO_SDU_INTERVAL_MIN     0x0000FFU
#define BT_ISO_SDU_INTERVAL_MAX     0x0FFFFFU
#define BT_ISO_ISO_INTERVAL_MIN     0x0004U
#define BT_ISO_ISO_INTERVAL_MAX     0x0C80U
#define BT_ISO_LATENCY_MIN          0x0005
#define BT_ISO_LATENCY_MAX          0x0FA0
#define BT_ISO_PACKING_SEQUENTIAL   0x00
#define BT_ISO_PACKING_INTERLEAVED  0x01
#define BT_ISO_FRAMING_UNFRAMED     0x00
#define BT_ISO_FRAMING_FRAMED       0x01
#define BT_ISO_MAX_GROUP_ISO_COUNT  0x1F
#define BT_ISO_MIN_SDU              0x0001
#define BT_ISO_MAX_SDU              0x0FFF
#define BT_ISO_CONNECTED_PDU_MIN    0x0000U
#define BT_ISO_BROADCAST_PDU_MIN    0x0001U
#define BT_ISO_PDU_MAX              0x00FBU
#define BT_ISO_BN_MIN               0x01U
#define BT_ISO_BN_MAX               0x0FU
#define BT_ISO_FT_MIN               0x01U
#define BT_ISO_FT_MAX               0xFFU
#define BT_ISO_NSE_MIN              0x01U
#define BT_ISO_NSE_MAX              0x1FU
#define BT_ISO_SYNC_TIMEOUT_MIN     0x000A
#define BT_ISO_SYNC_TIMEOUT_MAX     0x4000
#define BT_ISO_SYNC_MSE_ANY         0x00
#define BT_ISO_SYNC_MSE_MIN         0x01
#define BT_ISO_SYNC_MSE_MAX         0x1F
#define BT_ISO_CONNECTED_RTN_MIN    0x00
#define BT_ISO_CONNECTED_RTN_MAX    0xFF
#define BT_ISO_BROADCAST_RTN_MIN    0x00
#define BT_ISO_BROADCAST_RTN_MAX    0x1E
#define BT_ISO_BROADCAST_CODE_SIZE  0x10
#define BT_ISO_BIS_INDEX_MIN        0x01
#define BT_ISO_BIS_INDEX_MAX        0x1F
#define BT_ISO_IRC_MIN              0x01U
#define BT_ISO_IRC_MAX              0x0FU
#define BT_ISO_PTO_MIN              0x00U
#define BT_ISO_PTO_MAX              0x0FU
#define BT_ISO_SUBINTERVAL_NONE     0x00000000U
#define BT_ISO_SUBINTERVAL_UNKNOWN  0xFFFFFFFFU
#define BT_ISO_SUBINTERVAL_MIN      0x00000190U
#define BT_ISO_SUBINTERVAL_MAX      0x00009C3FU

#define BT_ISO_VALID_BIS_BITFIELD(_bis_bitfield)                                                   \
        ((_bis_bitfield) != 0U && (_bis_bitfield) <= BIT_MASK(BT_ISO_BIS_INDEX_MAX))

enum bt_iso_state {
        BT_ISO_STATE_DISCONNECTED,
        BT_ISO_STATE_CONNECTING,
        BT_ISO_STATE_CONNECTED,
        BT_ISO_STATE_DISCONNECTING,
};


enum bt_iso_chan_type {
        BT_ISO_CHAN_TYPE_NONE,
        BT_ISO_CHAN_TYPE_CENTRAL,
        BT_ISO_CHAN_TYPE_PERIPHERAL,
        BT_ISO_CHAN_TYPE_BROADCASTER,
        BT_ISO_CHAN_TYPE_SYNC_RECEIVER
};

struct bt_iso_chan {
        struct bt_conn                  *iso;
        struct bt_iso_chan_ops          *ops;
        struct bt_iso_chan_qos          *qos;
        enum bt_iso_state               state;
        sys_snode_t node;
};

struct bt_iso_chan_io_qos {
        uint16_t                        sdu;
        uint8_t                         phy;
        uint8_t                         rtn;

#if defined(CONFIG_BT_ISO_TEST_PARAMS) || defined(__DOXYGEN__)
        uint16_t max_pdu;

        uint8_t burst_number;
#endif /* CONFIG_BT_ISO_TEST_PARAMS */
};

struct bt_iso_chan_qos {
        struct bt_iso_chan_io_qos       *rx;
        struct bt_iso_chan_io_qos       *tx;

#if defined(CONFIG_BT_ISO_TEST_PARAMS) || defined(__DOXYGEN__)
        uint8_t num_subevents;
#endif /* CONFIG_BT_ISO_TEST_PARAMS */
};

struct bt_iso_chan_path {
        uint8_t pid;
        uint8_t format;
        uint16_t cid;
        uint16_t vid;
        uint32_t delay;
        uint8_t cc_len;
        const uint8_t *cc;
};

enum {
        BT_ISO_FLAGS_VALID = BIT(0),

        BT_ISO_FLAGS_ERROR = BIT(1),

        BT_ISO_FLAGS_LOST = BIT(2),

        BT_ISO_FLAGS_TS = BIT(3)
};

struct bt_iso_recv_info {
        uint32_t ts;

        uint16_t seq_num;

        uint8_t flags;
};

struct bt_iso_tx_info {
        uint32_t ts;

        uint32_t offset;

        uint16_t seq_num;
};

struct bt_iso_cig;

struct bt_iso_cig_param {
        struct bt_iso_chan **cis_channels;

        uint8_t num_cis;

        uint32_t c_to_p_interval;

        uint32_t p_to_c_interval;

        uint16_t c_to_p_latency;

        uint16_t p_to_c_latency;

        uint8_t sca;

        uint8_t packing;

        uint8_t framing;

#if defined(CONFIG_BT_ISO_TEST_PARAMS) || defined(__DOXYGEN__)
        uint8_t c_to_p_ft;

        uint8_t p_to_c_ft;

        uint16_t iso_interval;
#endif /* CONFIG_BT_ISO_TEST_PARAMS */
};

struct bt_iso_connect_param {
        struct bt_iso_chan *iso_chan;

        struct bt_conn *acl;
};

struct bt_iso_big;

struct bt_iso_big_create_param {
        struct bt_iso_chan **bis_channels;

        uint8_t num_bis;

        uint32_t interval;

        uint16_t latency;

        uint8_t packing;

        uint8_t framing;

        bool encryption;

        uint8_t bcode[BT_ISO_BROADCAST_CODE_SIZE];

#if defined(CONFIG_BT_ISO_TEST_PARAMS) || defined(__DOXYGEN__)
        uint8_t irc;

        uint8_t pto;

        uint16_t iso_interval;
#endif /* CONFIG_BT_ISO_TEST_PARAMS */
};

struct bt_iso_big_sync_param {
        struct bt_iso_chan **bis_channels;

        uint8_t num_bis;

        uint32_t bis_bitfield;

        uint32_t mse;

        uint16_t sync_timeout;

        bool  encryption;

        uint8_t bcode[BT_ISO_BROADCAST_CODE_SIZE];
};

struct bt_iso_biginfo {
        const bt_addr_le_t *addr;

        uint8_t sid;

        uint8_t  num_bis;

        uint8_t  sub_evt_count;

        uint16_t iso_interval;

        uint8_t  burst_number;

        uint8_t  offset;

        uint8_t  rep_count;

        uint16_t max_pdu;

        uint32_t sdu_interval;

        uint16_t max_sdu;

        uint8_t  phy;

        uint8_t  framing;

        bool  encryption;
};

struct bt_iso_chan_ops {
        void (*connected)(struct bt_iso_chan *chan);

        void (*disconnected)(struct bt_iso_chan *chan, uint8_t reason);

        struct net_buf *(*alloc_buf)(struct bt_iso_chan *chan);

        void (*recv)(struct bt_iso_chan *chan, const struct bt_iso_recv_info *info,
                     struct net_buf *buf);

        void (*sent)(struct bt_iso_chan *chan);

        void (*send_failed)(struct bt_iso_chan *chan, int err);
};

struct bt_iso_accept_info {
        struct bt_conn *acl;

        uint8_t cig_id;

        uint8_t cis_id;
};

struct bt_iso_server {
        int (*accept)(const struct bt_iso_accept_info *info, struct bt_iso_chan **chan);
};

struct bt_iso_chan *bt_iso_get_chan_by_conn(const struct bt_conn *iso);

int bt_iso_server_register(struct bt_iso_server *server);

int bt_iso_server_unregister(struct bt_iso_server *server);

int bt_iso_cig_create(const struct bt_iso_cig_param *param, struct bt_iso_cig **out_cig);

int bt_iso_cig_reconfigure(struct bt_iso_cig *cig, const struct bt_iso_cig_param *param);

int bt_iso_cig_terminate(struct bt_iso_cig *cig);

int bt_iso_chan_connect(const struct bt_iso_connect_param *param, size_t count);

int bt_iso_chan_disconnect(struct bt_iso_chan *chan);

int bt_iso_chan_send(struct bt_iso_chan *chan, struct net_buf *buf, uint16_t seq_num);

int bt_iso_chan_send_ts(struct bt_iso_chan *chan, struct net_buf *buf, uint16_t seq_num,
                        uint32_t ts);

int bt_iso_setup_data_path(const struct bt_iso_chan *chan, uint8_t dir,
                           const struct bt_iso_chan_path *path);

int bt_iso_remove_data_path(const struct bt_iso_chan *chan, uint8_t dir);

struct bt_iso_unicast_tx_info {
        uint32_t latency;

        uint32_t flush_timeout;

        uint16_t max_pdu;

        uint8_t  phy;

        uint8_t  bn;

        uint16_t max_sdu;

        uint32_t sdu_interval;
};

struct bt_iso_unicast_info {
        uint8_t cig_id;

        uint8_t cis_id;

        uint32_t cig_sync_delay;

        uint32_t cis_sync_delay;

        uint32_t subinterval;

        struct bt_iso_unicast_tx_info central;

        struct bt_iso_unicast_tx_info peripheral;
};

struct bt_iso_broadcaster_info {
        uint8_t big_handle;

        uint8_t bis_number;

        uint32_t sync_delay;

        uint32_t latency;

        uint32_t  pto;

        uint16_t max_pdu;

        uint8_t  phy;

        uint8_t  bn;

        uint8_t  irc;
};

struct bt_iso_sync_receiver_info {
        uint8_t big_handle;

        uint8_t bis_number;

        uint32_t latency;

        uint32_t  pto;

        uint16_t max_pdu;

        uint8_t  bn;

        uint8_t  irc;
};

struct bt_iso_info {
        enum bt_iso_chan_type type;

        uint16_t iso_interval;

        uint8_t  max_subevent;

        bool can_send;

        bool can_recv;

        union {
#if defined(CONFIG_BT_ISO_UNICAST) || defined(__DOXYGEN__)
                struct bt_iso_unicast_info unicast;
#endif /* CONFIG_BT_ISO_UNICAST */
#if defined(CONFIG_BT_ISO_BROADCASTER) || defined(__DOXYGEN__)
                struct bt_iso_broadcaster_info broadcaster;
#endif /* CONFIG_BT_ISO_BROADCASTER */
#if defined(CONFIG_BT_ISO_SYNC_RECEIVER) || defined(__DOXYGEN__)
                struct bt_iso_sync_receiver_info sync_receiver;
#endif /* CONFIG_BT_ISO_SYNC_RECEIVER */
        };
};

int bt_iso_chan_get_info(const struct bt_iso_chan *chan, struct bt_iso_info *info);

int bt_iso_chan_get_tx_sync(const struct bt_iso_chan *chan, struct bt_iso_tx_info *info);

struct bt_iso_big_cb {
        void (*started)(struct bt_iso_big *big);

        void (*stopped)(struct bt_iso_big *big, uint8_t reason);

        sys_snode_t _node;
};

int bt_iso_big_register_cb(struct bt_iso_big_cb *cb);

int bt_iso_big_create(struct bt_le_ext_adv *padv, struct bt_iso_big_create_param *param,
                      struct bt_iso_big **out_big);

int bt_iso_big_terminate(struct bt_iso_big *big);

int bt_iso_big_sync(struct bt_le_per_adv_sync *sync, struct bt_iso_big_sync_param *param,
                    struct bt_iso_big **out_big);

const char *bt_iso_chan_state_str(enum bt_iso_state state);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_ISO_H_ */
```

## 415.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2020 Intel Corporation。

版权（Copyright）：© 2021-2025 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 257 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_TEST_PARAMS`。

### 注释 3：原第 289 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_TEST_PARAMS`。

### 注释 4：原第 481 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_TEST_PARAMS`。

### 注释 5：原第 585 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_TEST_PARAMS`。

### 注释 6：原第 1229 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_UNICAST`。

### 注释 7：原第 1238 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_BROADCASTER`。

### 注释 8：原第 1247 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO_SYNC_RECEIVER`。

### 注释 9：原第 1368 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_ISO_H_`。

## 415.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/bluetooth/buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_iso_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaf2925460cc22cc4220dc376bcbee6201)
- [BT_ISO_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201af392f8825090c7beb304efc860a1911d)
- [BT_ISO_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201a4cb48a0a2a2ac37bbab5eded1bc3fd22)
- [BT_ISO_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201acfa2a00a1c203418768ce789cd0cec7d)
- [BT_ISO_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201aebc34f9c32f1cd5e3197c7edaf657340)
- [bt_iso_chan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gafcbd720c67c6a6e5f1cae1395e1e06f0)
- [BT_ISO_CHAN_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a58579ee03e3769501536826248758f17)
- [BT_ISO_CHAN_TYPE_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a46a0148a474b297d38d67fb18bdb410a)
- [BT_ISO_CHAN_TYPE_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0aa8b51a9ebacbaaac90956d7a9a816edb)
- [BT_ISO_CHAN_TYPE_BROADCASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b)
- [BT_ISO_CHAN_TYPE_SYNC_RECEIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2)
- [bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [iso](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#a7fd728385a3aec11be8883bdee8aedea)
- [bt_iso_chan_ops](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md)
- [ops](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#a214fe133602ac8dcfaaec7f372e12da8)
- [bt_iso_chan_qos](../bluetooth_connection_model_reference/P081_bt_iso_chan_qos_结构体.md)
- [qos](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#abe94fca71506bd590d9ef4465258914d)
- [state](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#a2b0fc7180d1983ee4a415c5331bed93d)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#aba7bf6dcad93b121c46daa6ad473a51c)
- [bt_iso_chan_io_qos](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [sdu](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md#ae52611dc326b6777620ff7aa43f566e9)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [phy](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md#a2180a4f82e4cdf5288b7f67701a16ad6)
- [rtn](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md#a5106bfd09f6be52604e7c7f0e3390684)
- [max_pdu](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md#ae9e7678a63030353eea65152d89464cd)
- [burst_number](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md#ac64a3ce7282ac8bc5b5420a46417b22c)
- [rx](../bluetooth_connection_model_reference/P081_bt_iso_chan_qos_结构体.md#ac231434d1798f431c4fbac5a759784a5)
- [tx](../bluetooth_connection_model_reference/P081_bt_iso_chan_qos_结构体.md#a47a99a6ccfa5f1e0c9fb859e66d2e9e3)
- [num_subevents](../bluetooth_connection_model_reference/P081_bt_iso_chan_qos_结构体.md#a4c6bfa577f8cbd724ed2561850fd6255)
- [bt_iso_chan_path](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md)
- [pid](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#a5e4fb798376489a38a87e4052ff85550)
- [format](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#a519c884281207d1165a61ccfb7fbcdf4)
- [cid](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#a95db7917f7b9e90a33f494233c3266eb)
- [vid](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#aebc12293ba0b10a87f1852e2a3e53a23)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [delay](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#adaed07de7e09263e3e941817eeb44258)
- [cc_len](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#a0da75c4911a197fed7fd7f17c76dddae)
- [cc](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#ac370bfca109153db02a747120c227104)
- [BT_ISO_FLAGS_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a143de2c153179b3c40aca51c016e6382)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_ISO_FLAGS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a5f0aa6e3150819821f800dd7376e2218)
- [BT_ISO_FLAGS_LOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a5e87d48b6e96275744590194b75396ff)
- [BT_ISO_FLAGS_TS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23)
- [bt_iso_recv_info](../bluetooth_connection_model_reference/P086_bt_iso_recv_info_结构体.md)
- [ts](../bluetooth_connection_model_reference/P086_bt_iso_recv_info_结构体.md#a4bf778ae9be39eb4a740c2eb9670d98a)
- [seq_num](../bluetooth_connection_model_reference/P086_bt_iso_recv_info_结构体.md#a7c5b950df0359bb561140d0c2726fae6)
- [flags](../bluetooth_connection_model_reference/P086_bt_iso_recv_info_结构体.md#a0a7842fcb3251ed89b99fde43ba235a5)
- [bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)
- [ts](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md#ac8a6a4c073e4df1553d32339a6e4b051)
- [offset](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md#a0cff6aa2893fdc11160e4327afebed13)
- [seq_num](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md#a2791edea2f4f4459acc24c8dbaa33ded)
- [bt_iso_cig](../bluetooth_connection_model_reference/P082_bt_iso_cig_结构体.md)
- [bt_iso_cig_param](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md)
- [cis_channels](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a841dee850f3161bd8e904376792c8ad7)
- [num_cis](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a69c12b704b9897d88b71bc96bd2d3024)
- [c_to_p_interval](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#ad7349213bab902a68c726da51fac2306)
- [p_to_c_interval](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a36d2eaa4fd3e08988d4c49ca0902a882)
- [c_to_p_latency](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#aeffe10e87d81285196e931dcad2882ba)
- [p_to_c_latency](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#ad1725e09a397e83d1cc88ebd3a60ed93)
- [sca](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a83fdc5374f341a421e1394b08297cdff)
- [packing](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a3908eadf3080731cb891e803162d321c)
- [framing](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a4a09f9f6e7a8db17c3037c9f1761b18a)
- [c_to_p_ft](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#aadc3762f3fec3127014378fe58c5b684)
- [p_to_c_ft](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#ab222cdb0af475180dd715b4f5658dc65)
- [iso_interval](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a85641a8f01d63b4221c013815c055526)
- [bt_iso_connect_param](../bluetooth_connection_model_reference/P084_bt_iso_connect_param_结构体.md)
- [iso_chan](../bluetooth_connection_model_reference/P084_bt_iso_connect_param_结构体.md#ad004956584d2d065d8c0c52959f350d5)
- [acl](../bluetooth_connection_model_reference/P084_bt_iso_connect_param_结构体.md#aba2f3838e03a1e31699a4623ba93d372)
- [bt_iso_big](../bluetooth_connection_model_reference/P071_bt_iso_big_结构体.md)
- [bt_iso_big_create_param](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md)
- [bis_channels](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#a7548bbb75f240a70435cb86a48846d0a)
- [num_bis](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#a8ae9c225798e9f5b72fe0b8c3b6f2cf0)
- [interval](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#a7aaef1f7a78ae1088886a78739fd6849)
- [latency](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#ab847021da2e604036cecf90483e12132)
- [packing](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#ad478d7b36fb34b8e57a25ae0029e4c51)
- [framing](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#aab0e9f66cb10643e72d6382718ed4c0d)
- [encryption](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#a1288fa2a8f6bb3e2ab26729e245277e1)
- [bcode](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#ae7a68301c2a0ea7a81812581f3ab1e61)
- [BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)
- [irc](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#ad931ff1f19f92c29c40d934346498e79)
- [pto](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#affce506bd271d9b0e497160c163c5798)
- [iso_interval](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#a63cd16824e9d09e29d3c7e135b08d932)
- [bt_iso_big_sync_param](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md)
- [bis_channels](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#ac56d7206c3434837a52059716355adad)
- [num_bis](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#a96cd109e9f5820531635d48e88b4bff8)
- [bis_bitfield](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#a14b03509daf760edbead86659f733136)
- [mse](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#a16b332b4a0f373cb21e5da6e6e383b9e)
- [sync_timeout](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#a8e344870fc0e380e6588eb90c7ef72f9)
- [encryption](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#a8e5cffe8960477e7f64707d7dd4191f6)
- [bcode](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#ac47bfe3ee0c46f5d55d38f24835ac48d)
- [bt_iso_biginfo](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [addr](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#aa7dbfd342eecf8ffc2fce9d3fa7209ea)
- [sid](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a78e0a53f920980081d7b0702b02cf386)
- [num_bis](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a10eb24596a4353da3feb0d30fed35ae7)
- [sub_evt_count](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a24eb83f7b54e9f949cc07e9955b4a8b8)
- [iso_interval](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#afe96caf570314731f6c543b40d7def9a)
- [burst_number](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#ad114dd97500d12242da77e8522133953)
- [offset](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a4efb91dc2f249e41c65cd0dcbfe45bad)
- [rep_count](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a8458f6d6ebe936212d928caca61b13bd)
- [max_pdu](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#af356aa29aa82c8deb63a9f47e54070a1)
- [sdu_interval](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a4a6d6cdea56a69a0b3b3fd021489750d)
- [max_sdu](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a9fddcb74f3de7eb857583a0179427f84)
- [phy](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a2cbaf6a89e8aaf62c7048e04523e57d4)
- [framing](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a1084c209d122d2d13244b77659ce28dd)
- [encryption](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a7d54ecb896c0d6bc590311d5d5a3ac7b)
- [connected](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a6b0e51770158da7b728e1084a8e44504)
- [disconnected](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a2069849352019362e5dc7d68f835f359)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [recv](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a6d5d9423fff83f8f337f97b3fc018f39)
- [sent](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a048954070628229b8aacd373de1fb236)
- [send_failed](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a750ac5c12155602a32b1f02bb2dc8fba)
- [bt_iso_accept_info](../bluetooth_connection_model_reference/P070_bt_iso_accept_info_结构体.md)
- [acl](../bluetooth_connection_model_reference/P070_bt_iso_accept_info_结构体.md#a4225ccc90f1e17e26ce61fe398f506d1)
- [cig_id](../bluetooth_connection_model_reference/P070_bt_iso_accept_info_结构体.md#a88002043a67c89c8d518ebdf92cf8847)
- [cis_id](../bluetooth_connection_model_reference/P070_bt_iso_accept_info_结构体.md#a688809132997c37a6fe2529498a4ee0e)
- [bt_iso_server](../bluetooth_connection_model_reference/P087_bt_iso_server_结构体.md)
- [accept](../bluetooth_connection_model_reference/P087_bt_iso_server_结构体.md#ae67a000ae524cba53b6bda503568ba38)
- [bt_iso_get_chan_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa3407502145a77e08993220f7ce51b4a)
- [bt_iso_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaff0e52777b2140519c63b54b9618bca8)
- [bt_iso_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6)
- [bt_iso_cig_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaea03fc251206f18de320506064c1631f)
- [bt_iso_cig_reconfigure](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga98f557c183a82066b81f0265c225bebe)
- [bt_iso_cig_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gad4b6a7286593ff099117113b6ca996f8)
- [bt_iso_chan_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga98953a261f3699b62cd19ab4977e0b4c)
- [bt_iso_chan_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga94c5c788b099284219e5a303b4b8ea69)
- [bt_iso_chan_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0dbb89a133011a833be7d18161471c6a)
- [bt_iso_chan_send_ts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab75b817770e3b685920587afde39d6cd)
- [bt_iso_setup_data_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa74c762451cfb5d04ffcd8d396a75447)
- [bt_iso_remove_data_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga53be464e005392676830feeddd8cdc22)
- [bt_iso_unicast_tx_info](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md)
- [latency](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#a14548ee24fad8a26287aa0daba451a47)
- [flush_timeout](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#aaf1f623eac2f84ca06082776179b71c5)
- [max_pdu](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#afe7dce9255613e5e2939d3719c720822)
- [phy](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#a3134e0bdb663ad7184e23531504233a5)
- [bn](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#ab4ea9d5bb535d29ae9406e948d8707a9)
- [max_sdu](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#a7bed74a67bb73f6919d2817d82bcf996)
- [sdu_interval](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#adc91f9c200199400a84322a58d28a933)
- [bt_iso_unicast_info](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md)
- [cig_id](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#a196ff16e4e959fa656d4af265e686f09)
- [cis_id](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#abc61e1d8edcb099a02054db8ec94ba22)
- [cig_sync_delay](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#a029c450e2324bbc6ee8fda6d1d10deef)
- [cis_sync_delay](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#acbc8c068907eba204d369cf76f4f112d)
- [subinterval](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#a4d53dc6adc8d5519cf74982aa5031e74)
- [central](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#a4fc402b934ae8aa65493df01c88cae34)
- [peripheral](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#a03b084fefcab049efbe1a609a59d9c54)
- [bt_iso_broadcaster_info](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md)
- [big_handle](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#a1defaab3c9fbbe1c91f076ece50ad7b0)
- [bis_number](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#aae07a2b0b2a56a5abb290f9345127c4f)
- [sync_delay](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#a577370ab24ebd4d80db4d8ffdb918483)
- [latency](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#a71388f9b64510ab91c3147f05f775aeb)
- [pto](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#a9f93161fb7f81d5eb3a55f955be1b85d)
- [max_pdu](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#aa57b6e08cf4d3d154762c8c43de0f2cf)
- [phy](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#a3d4e44a1da54e5ca0f2002ca3f6e7a13)
- [bn](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#ab3cb80e6b362e093e6924ab11b8737e9)
- [irc](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#ac1feade59bbad1e08418e1808619f775)
- [bt_iso_sync_receiver_info](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md)
- [big_handle](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#af2857439c483fdd455c7ccaf66f5fb35)
- [bis_number](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a55e2d87a45234bce1d54a7330164cd0d)
- [latency](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a24bad4231eb214a2c95b1da9ba59c284)
- [pto](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a80ac6e529491156109955219569fdec6)
- [max_pdu](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a40ff5a4d691a75802f211a63b1e12303)
- [bn](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a8be50f8c6d76515ac290407959eaf0e1)
- [irc](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a6185a7ac123be930650da6dc84c0c1e0)
- [bt_iso_info](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md)
- [type](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#af01766b8eed556ca165222d19ff05838)
- [iso_interval](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a53c6c8eee63cd674d54dc1d40aa33a43)
- [max_subevent](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a02554d9114dc3e34305a8e986d906cbe)
- [can_send](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a4ead7e3c5ab496b6cfc2becfaddb3746)
- [can_recv](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a9e00edb4e09bae39a37956011ccca353)
- [unicast](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a423474bd89ecdc614e6dfb8ea84db27e)
- [broadcaster](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a94e8132738697efa39857612399385b8)
- [sync_receiver](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#ac1edf09109a5e40a4f675281a7d9e300)
- [bt_iso_chan_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga75e58ed5bfa48f84000f1ce974d649c6)
- [bt_iso_chan_get_tx_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa3942147fdeebc36039cc35c4e984411)
- [bt_iso_big_cb](../bluetooth_connection_model_reference/P072_bt_iso_big_cb_结构体.md)
- [started](../bluetooth_connection_model_reference/P072_bt_iso_big_cb_结构体.md#ac84e00545dbb330311482eb5abd4a78b)
- [stopped](../bluetooth_connection_model_reference/P072_bt_iso_big_cb_结构体.md#a43d6ee745f7852460f843ced33c777c2)
- [bt_iso_big_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8a01a56e4a4555ed65a67065facfca76)
- [bt_iso_big_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gac9937316382d257493c7d0359f1341f5)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_iso_big_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab9c06a86bf5cc023f5f9bd16c5d3265b)
- [bt_iso_big_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga790cfeb8516020f317802e019dca4754)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [bt_iso_chan_state_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4d4c9b8d6d83abcc8d3b337101922800)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_iso_accept_info::acl](../bluetooth_connection_model_reference/P070_bt_iso_accept_info_结构体.md#a4225ccc90f1e17e26ce61fe398f506d1)
- [bt_iso_accept_info::cis_id](../bluetooth_connection_model_reference/P070_bt_iso_accept_info_结构体.md#a688809132997c37a6fe2529498a4ee0e)
- [bt_iso_accept_info::cig_id](../bluetooth_connection_model_reference/P070_bt_iso_accept_info_结构体.md#a88002043a67c89c8d518ebdf92cf8847)
- [bt_iso_big_cb::stopped](../bluetooth_connection_model_reference/P072_bt_iso_big_cb_结构体.md#a43d6ee745f7852460f843ced33c777c2)
- [bt_iso_big_cb::started](../bluetooth_connection_model_reference/P072_bt_iso_big_cb_结构体.md#ac84e00545dbb330311482eb5abd4a78b)
- [bt_iso_big_create_param::encryption](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#a1288fa2a8f6bb3e2ab26729e245277e1)
- [bt_iso_big_create_param::iso_interval](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#a63cd16824e9d09e29d3c7e135b08d932)
- [bt_iso_big_create_param::bis_channels](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#a7548bbb75f240a70435cb86a48846d0a)
- [bt_iso_big_create_param::interval](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#a7aaef1f7a78ae1088886a78739fd6849)
- [bt_iso_big_create_param::num_bis](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#a8ae9c225798e9f5b72fe0b8c3b6f2cf0)
- [bt_iso_big_create_param::framing](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#aab0e9f66cb10643e72d6382718ed4c0d)
- [bt_iso_big_create_param::latency](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#ab847021da2e604036cecf90483e12132)
- [bt_iso_big_create_param::packing](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#ad478d7b36fb34b8e57a25ae0029e4c51)
- [bt_iso_big_create_param::irc](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#ad931ff1f19f92c29c40d934346498e79)
- [bt_iso_big_create_param::bcode](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#ae7a68301c2a0ea7a81812581f3ab1e61)
- [bt_iso_big_create_param::pto](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md#affce506bd271d9b0e497160c163c5798)
- [bt_iso_big_sync_param::bis_bitfield](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#a14b03509daf760edbead86659f733136)
- [bt_iso_big_sync_param::mse](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#a16b332b4a0f373cb21e5da6e6e383b9e)
- [bt_iso_big_sync_param::sync_timeout](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#a8e344870fc0e380e6588eb90c7ef72f9)
- [bt_iso_big_sync_param::encryption](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#a8e5cffe8960477e7f64707d7dd4191f6)
- [bt_iso_big_sync_param::num_bis](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#a96cd109e9f5820531635d48e88b4bff8)
- [bt_iso_big_sync_param::bcode](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#ac47bfe3ee0c46f5d55d38f24835ac48d)
- [bt_iso_big_sync_param::bis_channels](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md#ac56d7206c3434837a52059716355adad)
- [bt_iso_biginfo::framing](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a1084c209d122d2d13244b77659ce28dd)
- [bt_iso_biginfo::num_bis](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a10eb24596a4353da3feb0d30fed35ae7)
- [bt_iso_biginfo::sub_evt_count](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a24eb83f7b54e9f949cc07e9955b4a8b8)
- [bt_iso_biginfo::phy](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a2cbaf6a89e8aaf62c7048e04523e57d4)
- [bt_iso_biginfo::sdu_interval](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a4a6d6cdea56a69a0b3b3fd021489750d)
- [bt_iso_biginfo::offset](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a4efb91dc2f249e41c65cd0dcbfe45bad)
- [bt_iso_biginfo::sid](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a78e0a53f920980081d7b0702b02cf386)
- [bt_iso_biginfo::encryption](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a7d54ecb896c0d6bc590311d5d5a3ac7b)
- [bt_iso_biginfo::rep_count](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a8458f6d6ebe936212d928caca61b13bd)
- [bt_iso_biginfo::max_sdu](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#a9fddcb74f3de7eb857583a0179427f84)
- [bt_iso_biginfo::addr](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#aa7dbfd342eecf8ffc2fce9d3fa7209ea)
- [bt_iso_biginfo::burst_number](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#ad114dd97500d12242da77e8522133953)
- [bt_iso_biginfo::max_pdu](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#af356aa29aa82c8deb63a9f47e54070a1)
- [bt_iso_biginfo::iso_interval](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md#afe96caf570314731f6c543b40d7def9a)
- [bt_iso_broadcaster_info::big_handle](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#a1defaab3c9fbbe1c91f076ece50ad7b0)
- [bt_iso_broadcaster_info::phy](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#a3d4e44a1da54e5ca0f2002ca3f6e7a13)
- [bt_iso_broadcaster_info::sync_delay](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#a577370ab24ebd4d80db4d8ffdb918483)
- [bt_iso_broadcaster_info::latency](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#a71388f9b64510ab91c3147f05f775aeb)
- [bt_iso_broadcaster_info::pto](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#a9f93161fb7f81d5eb3a55f955be1b85d)
- [bt_iso_broadcaster_info::max_pdu](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#aa57b6e08cf4d3d154762c8c43de0f2cf)
- [bt_iso_broadcaster_info::bis_number](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#aae07a2b0b2a56a5abb290f9345127c4f)
- [bt_iso_broadcaster_info::bn](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#ab3cb80e6b362e093e6924ab11b8737e9)
- [bt_iso_broadcaster_info::irc](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md#ac1feade59bbad1e08418e1808619f775)
- [bt_iso_chan_io_qos::phy](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md#a2180a4f82e4cdf5288b7f67701a16ad6)
- [bt_iso_chan_io_qos::rtn](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md#a5106bfd09f6be52604e7c7f0e3390684)
- [bt_iso_chan_io_qos::burst_number](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md#ac64a3ce7282ac8bc5b5420a46417b22c)
- [bt_iso_chan_io_qos::sdu](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md#ae52611dc326b6777620ff7aa43f566e9)
- [bt_iso_chan_io_qos::max_pdu](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md#ae9e7678a63030353eea65152d89464cd)
- [bt_iso_chan_ops::sent](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a048954070628229b8aacd373de1fb236)
- [bt_iso_chan_ops::disconnected](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a2069849352019362e5dc7d68f835f359)
- [bt_iso_chan_ops::connected](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a6b0e51770158da7b728e1084a8e44504)
- [bt_iso_chan_ops::recv](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a6d5d9423fff83f8f337f97b3fc018f39)
- [bt_iso_chan_ops::send_failed](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a750ac5c12155602a32b1f02bb2dc8fba)
- [bt_iso_chan_path::cc_len](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#a0da75c4911a197fed7fd7f17c76dddae)
- [bt_iso_chan_path::format](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#a519c884281207d1165a61ccfb7fbcdf4)
- [bt_iso_chan_path::pid](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#a5e4fb798376489a38a87e4052ff85550)
- [bt_iso_chan_path::cid](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#a95db7917f7b9e90a33f494233c3266eb)
- [bt_iso_chan_path::cc](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#ac370bfca109153db02a747120c227104)
- [bt_iso_chan_path::delay](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#adaed07de7e09263e3e941817eeb44258)
- [bt_iso_chan_path::vid](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md#aebc12293ba0b10a87f1852e2a3e53a23)
- [bt_iso_chan_qos::tx](../bluetooth_connection_model_reference/P081_bt_iso_chan_qos_结构体.md#a47a99a6ccfa5f1e0c9fb859e66d2e9e3)
- [bt_iso_chan_qos::num_subevents](../bluetooth_connection_model_reference/P081_bt_iso_chan_qos_结构体.md#a4c6bfa577f8cbd724ed2561850fd6255)
- [bt_iso_chan_qos::rx](../bluetooth_connection_model_reference/P081_bt_iso_chan_qos_结构体.md#ac231434d1798f431c4fbac5a759784a5)
- [bt_iso_chan::ops](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#a214fe133602ac8dcfaaec7f372e12da8)
- [bt_iso_chan::state](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#a2b0fc7180d1983ee4a415c5331bed93d)
- [bt_iso_chan::iso](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#a7fd728385a3aec11be8883bdee8aedea)
- [bt_iso_chan::node](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#aba7bf6dcad93b121c46daa6ad473a51c)
- [bt_iso_chan::qos](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#abe94fca71506bd590d9ef4465258914d)
- [bt_iso_cig_param::p_to_c_interval](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a36d2eaa4fd3e08988d4c49ca0902a882)
- [bt_iso_cig_param::packing](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a3908eadf3080731cb891e803162d321c)
- [bt_iso_cig_param::framing](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a4a09f9f6e7a8db17c3037c9f1761b18a)
- [bt_iso_cig_param::num_cis](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a69c12b704b9897d88b71bc96bd2d3024)
- [bt_iso_cig_param::sca](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a83fdc5374f341a421e1394b08297cdff)
- [bt_iso_cig_param::cis_channels](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a841dee850f3161bd8e904376792c8ad7)
- [bt_iso_cig_param::iso_interval](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#a85641a8f01d63b4221c013815c055526)
- [bt_iso_cig_param::c_to_p_ft](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#aadc3762f3fec3127014378fe58c5b684)
- [bt_iso_cig_param::p_to_c_ft](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#ab222cdb0af475180dd715b4f5658dc65)
- [bt_iso_cig_param::p_to_c_latency](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#ad1725e09a397e83d1cc88ebd3a60ed93)
- [bt_iso_cig_param::c_to_p_interval](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#ad7349213bab902a68c726da51fac2306)
- [bt_iso_cig_param::c_to_p_latency](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md#aeffe10e87d81285196e931dcad2882ba)
- [bt_iso_connect_param::acl](../bluetooth_connection_model_reference/P084_bt_iso_connect_param_结构体.md#aba2f3838e03a1e31699a4623ba93d372)
- [bt_iso_connect_param::iso_chan](../bluetooth_connection_model_reference/P084_bt_iso_connect_param_结构体.md#ad004956584d2d065d8c0c52959f350d5)
- [bt_iso_info::max_subevent](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a02554d9114dc3e34305a8e986d906cbe)
- [bt_iso_info::unicast](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a423474bd89ecdc614e6dfb8ea84db27e)
- [bt_iso_info::can_send](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a4ead7e3c5ab496b6cfc2becfaddb3746)
- [bt_iso_info::iso_interval](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a53c6c8eee63cd674d54dc1d40aa33a43)
- [bt_iso_info::broadcaster](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a94e8132738697efa39857612399385b8)
- [bt_iso_info::can_recv](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#a9e00edb4e09bae39a37956011ccca353)
- [bt_iso_info::sync_receiver](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#ac1edf09109a5e40a4f675281a7d9e300)
- [bt_iso_info::type](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md#af01766b8eed556ca165222d19ff05838)
- [bt_iso_recv_info::flags](../bluetooth_connection_model_reference/P086_bt_iso_recv_info_结构体.md#a0a7842fcb3251ed89b99fde43ba235a5)
- [bt_iso_recv_info::ts](../bluetooth_connection_model_reference/P086_bt_iso_recv_info_结构体.md#a4bf778ae9be39eb4a740c2eb9670d98a)
- [bt_iso_recv_info::seq_num](../bluetooth_connection_model_reference/P086_bt_iso_recv_info_结构体.md#a7c5b950df0359bb561140d0c2726fae6)
- [bt_iso_server::accept](../bluetooth_connection_model_reference/P087_bt_iso_server_结构体.md#ae67a000ae524cba53b6bda503568ba38)
- [bt_iso_sync_receiver_info::latency](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a24bad4231eb214a2c95b1da9ba59c284)
- [bt_iso_sync_receiver_info::max_pdu](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a40ff5a4d691a75802f211a63b1e12303)
- [bt_iso_sync_receiver_info::bis_number](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a55e2d87a45234bce1d54a7330164cd0d)
- [bt_iso_sync_receiver_info::irc](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a6185a7ac123be930650da6dc84c0c1e0)
- [bt_iso_sync_receiver_info::pto](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a80ac6e529491156109955219569fdec6)
- [bt_iso_sync_receiver_info::bn](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#a8be50f8c6d76515ac290407959eaf0e1)
- [bt_iso_sync_receiver_info::big_handle](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md#af2857439c483fdd455c7ccaf66f5fb35)
- [bt_iso_tx_info::offset](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md#a0cff6aa2893fdc11160e4327afebed13)
- [bt_iso_tx_info::seq_num](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md#a2791edea2f4f4459acc24c8dbaa33ded)
- [bt_iso_tx_info::ts](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md#ac8a6a4c073e4df1553d32339a6e4b051)
- [bt_iso_unicast_info::cig_sync_delay](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#a029c450e2324bbc6ee8fda6d1d10deef)
- [bt_iso_unicast_info::peripheral](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#a03b084fefcab049efbe1a609a59d9c54)
- [bt_iso_unicast_info::cig_id](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#a196ff16e4e959fa656d4af265e686f09)
- [bt_iso_unicast_info::subinterval](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#a4d53dc6adc8d5519cf74982aa5031e74)
- [bt_iso_unicast_info::central](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#a4fc402b934ae8aa65493df01c88cae34)
- [bt_iso_unicast_info::cis_id](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#abc61e1d8edcb099a02054db8ec94ba22)
- [bt_iso_unicast_info::cis_sync_delay](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md#acbc8c068907eba204d369cf76f4f112d)
- [bt_iso_unicast_tx_info::latency](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#a14548ee24fad8a26287aa0daba451a47)
- [bt_iso_unicast_tx_info::phy](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#a3134e0bdb663ad7184e23531504233a5)
- [bt_iso_unicast_tx_info::max_sdu](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#a7bed74a67bb73f6919d2817d82bcf996)
- [bt_iso_unicast_tx_info::flush_timeout](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#aaf1f623eac2f84ca06082776179b71c5)
- [bt_iso_unicast_tx_info::bn](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#ab4ea9d5bb535d29ae9406e948d8707a9)
- [bt_iso_unicast_tx_info::sdu_interval](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#adc91f9c200199400a84322a58d28a933)
- [bt_iso_unicast_tx_info::max_pdu](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md#afe7dce9255613e5e2939d3719c720822)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P414_ism6hg256x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P416_it51xxx-vcmp.h_源码浏览.md)
