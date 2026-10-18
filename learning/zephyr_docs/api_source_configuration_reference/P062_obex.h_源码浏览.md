---
id: learning.zephyr-docs.api-source-configuration-reference.page-62
title: obex.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/obex_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_obex.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h.html)。

## 62.1\_原始可见代码（Source Code）

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
<a id="foldopen00033"></a>
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
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
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
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="foldopen00251"></a>
<a id="l00251"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="foldopen00334"></a>
<a id="l00334"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="foldopen00420"></a>
<a id="l00420"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="foldopen00473"></a>
<a id="l00473"></a>
<a id="l00475"></a>
<a id="l00477"></a>
<a id="l00479"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="foldopen00484"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="foldopen00492"></a>
<a id="l00492"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00507"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00513"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="foldopen00538"></a>
<a id="l00538"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00556"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="foldopen00584"></a>
<a id="l00584"></a>
<a id="l00586"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00592"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00888"></a>
<a id="l00889"></a>
<a id="foldopen00891"></a>
<a id="l00891"></a>
<a id="l00893"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00955"></a>
<a id="l00956"></a>
<a id="foldopen00958"></a>
<a id="l00958"></a>
<a id="l00960"></a>
<a id="l00962"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01061"></a>
<a id="l01062"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01090"></a>
<a id="l01091"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01109"></a>
<a id="l01110"></a>
<a id="l01118"></a>
<a id="l01119"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01138"></a>
<a id="l01139"></a>
<a id="l01148"></a>
<a id="l01149"></a>
<a id="l01158"></a>
<a id="l01159"></a>
<a id="l01168"></a>
<a id="l01169"></a>
<a id="foldopen01185"></a>
<a id="l01185"></a>
<a id="l01186"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="l01191"></a>
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
<a id="l01203"></a>
<a id="l01204"></a>
<a id="l01205"></a>
<a id="l01206"></a>
<a id="l01207"></a>
<a id="l01208"></a>
<a id="l01209"></a>
<a id="l01210"></a>
<a id="l01211"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01214"></a>
<a id="l01215"></a>
<a id="l01216"></a>
<a id="l01217"></a>
<a id="l01218"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01221"></a>
<a id="l01222"></a>
<a id="l01223"></a>
<a id="l01224"></a>
<a id="l01225"></a>
<a id="l01226"></a>
<a id="l01235"></a>
<a id="l01236"></a>
<a id="l01244"></a>
<a id="l01245"></a>
<a id="foldopen01254"></a>
<a id="l01254"></a>
<a id="l01255"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01258"></a>
<a id="l01259"></a>
<a id="l01268"></a>
<a id="l01269"></a>
<a id="l01270"></a>
<a id="l01275"></a>
<a id="l01277"></a>
<a id="l01278"></a>
<a id="l01283"></a>
<a id="l01285"></a>
<a id="l01286"></a>
<a id="l01288"></a>
<a id="l01290"></a>
<a id="l01291"></a>
<a id="l01298"></a>
<a id="l01299"></a>
<a id="l01308"></a>
<a id="l01309"></a>
<a id="l01310"></a>
<a id="l01315"></a>
<a id="l01317"></a>
<a id="l01318"></a>
<a id="l01323"></a>
<a id="l01324"></a>
<a id="l01329"></a>
<a id="l01331"></a>
<a id="l01332"></a>
<a id="l01341"></a>
<a id="l01342"></a>
<a id="l01350"></a>
<a id="l01351"></a>
<a id="l01360"></a>
<a id="l01361"></a>
<a id="l01370"></a>
<a id="l01371"></a>
<a id="l01380"></a>
<a id="l01381"></a>
<a id="l01382"></a>
<a id="l01390"></a>
<a id="l01391"></a>
<a id="l01399"></a>
<a id="l01400"></a>
<a id="l01409"></a>
<a id="l01410"></a>
<a id="l01418"></a>
<a id="l01419"></a>
<a id="l01427"></a>
<a id="l01428"></a>
<a id="l01436"></a>
<a id="l01437"></a>
<a id="foldopen01439"></a>
<a id="l01439"></a>
<a id="l01441"></a>
<a id="l01443"></a>
<a id="l01445"></a>
<a id="l01446"></a>
<a id="l01447"></a>
<a id="l01463"></a>
<a id="l01464"></a>
<a id="l01465"></a>
<a id="l01473"></a>
<a id="l01474"></a>
<a id="l01483"></a>
<a id="l01484"></a>
<a id="l01493"></a>
<a id="l01494"></a>
<a id="l01502"></a>
<a id="l01503"></a>
<a id="l01512"></a>
<a id="l01513"></a>
<a id="l01521"></a>
<a id="l01522"></a>
<a id="l01531"></a>
<a id="l01532"></a>
<a id="l01541"></a>
<a id="l01542"></a>
<a id="l01551"></a>
<a id="l01552"></a>
<a id="l01561"></a>
<a id="l01562"></a>
<a id="l01571"></a>
<a id="l01572"></a>
<a id="l01581"></a>
<a id="l01582"></a>
<a id="l01590"></a>
<a id="l01591"></a>
<a id="l01611"></a>
<a id="l01612"></a>
<a id="l01613"></a>
<a id="l01624"></a>
<a id="l01625"></a>
<a id="l01636"></a>
<a id="l01637"></a>
<a id="l01648"></a>
<a id="l01649"></a>
<a id="l01657"></a>
<a id="l01658"></a>
<a id="l01667"></a>
<a id="l01668"></a>
<a id="l01677"></a>
<a id="l01678"></a>
<a id="l01687"></a>
<a id="l01688"></a>
<a id="l01689"></a>
<a id="l01697"></a>
<a id="l01698"></a>
<a id="l01706"></a>
<a id="l01707"></a>
<a id="l01716"></a>
<a id="l01717"></a>
<a id="l01725"></a>
<a id="l01726"></a>
<a id="l01734"></a>
<a id="l01735"></a>
<a id="l01743"></a>
<a id="l01744"></a>
<a id="l01753"></a>
<a id="l01754"></a>
<a id="l01763"></a>
<a id="l01764"></a>
<a id="l01772"></a>
<a id="l01773"></a>
<a id="l01781"></a>
<a id="l01782"></a>
<a id="l01798"></a>
<a id="l01799"></a>
<a id="l01800"></a>
<a id="l01819"></a>
<a id="l01820"></a>
<a id="l01821"></a>
<a id="l01822"></a>
<a id="l01841"></a>
<a id="l01842"></a>
<a id="l01843"></a>
<a id="l01844"></a>
<a id="l01845"></a>
<a id="l01846"></a>
<a id="l01847"></a>
<a id="l01848"></a>
<a id="l01852"></a>
<a id="l01853"></a>
<a id="abluetooth_2uuid_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__atomic__apis_html_gacad6866fa4c844026cd9f8c3fb60ecd7"></a>
<a id="agroup__bt__obex_html_ga0d27f09e3b8ea5636f0a34cf8729abaf"></a>
<a id="agroup__bt__obex_html_ga107787f08e55bf2740cc14cb5614bdbf"></a>
<a id="agroup__bt__obex_html_ga111cd19449aba6fd0e667551874af0cf"></a>
<a id="agroup__bt__obex_html_ga12730d705667c2717c05a75cdfc07281"></a>
<a id="agroup__bt__obex_html_ga13836db790849b5ec6b52bcb97c84505"></a>
<a id="agroup__bt__obex_html_ga14c619eef70addc01d13841eda2d8f89"></a>
<a id="agroup__bt__obex_html_ga14c8efe9c8a99e2736552d59972e7b23"></a>
<a id="agroup__bt__obex_html_ga170456d806c0ff494b0c1d7fad763051"></a>
<a id="agroup__bt__obex_html_ga18ce5303b138959481666c0b8101f59e"></a>
<a id="agroup__bt__obex_html_ga1d8684307899b1bd3724cb3aa996c53e"></a>
<a id="agroup__bt__obex_html_ga1df3928a40f544ffb98b5eb1ceac62dd"></a>
<a id="agroup__bt__obex_html_ga1e9b6dd9a8816ce87235b6b3d723541c"></a>
<a id="agroup__bt__obex_html_ga21afebccbd592381fb1569feaff98511"></a>
<a id="agroup__bt__obex_html_ga225ac4953da5e56a07865c8ab6ee0591"></a>
<a id="agroup__bt__obex_html_ga23ed862cc6149a71793d02d89fb98cdc"></a>
<a id="agroup__bt__obex_html_ga249e8b35b98f564d57dc1d644228b8f2"></a>
<a id="agroup__bt__obex_html_ga296af3d5a15684e4aa3846cc24203fef"></a>
<a id="agroup__bt__obex_html_ga367337d0f002a046248e92f3578efbb6"></a>
<a id="agroup__bt__obex_html_ga3708c17f9c23fdeb5ceda376787cebbd"></a>
<a id="agroup__bt__obex_html_ga3c893652eb9a5f0bf699d357caf40948"></a>
<a id="agroup__bt__obex_html_ga3d805f241fc507587445b3204070055e"></a>
<a id="agroup__bt__obex_html_ga3e9415fa4595d17676ada6622c9fd475"></a>
<a id="agroup__bt__obex_html_ga4463514cf369beb882fec9ab15904821"></a>
<a id="agroup__bt__obex_html_ga49265f0aec21d8c33f56eb44723dabba"></a>
<a id="agroup__bt__obex_html_ga49d1988eae4165f1cec624812cfe5f36"></a>
<a id="agroup__bt__obex_html_ga4b7c08fd620fdc1ff28a4714c84b6e30"></a>
<a id="agroup__bt__obex_html_ga500dcfab79831c5d640406cff8c54f01"></a>
<a id="agroup__bt__obex_html_ga51baeae9280bb50e34b6608f620498fa"></a>
<a id="agroup__bt__obex_html_ga5433561f0e9bad6da2d94dccca1578de"></a>
<a id="agroup__bt__obex_html_ga5571666538c43d8d71dd17dc58d19f45"></a>
<a id="agroup__bt__obex_html_ga560c8f0cb92b769a0716b2bc163c38e1"></a>
<a id="agroup__bt__obex_html_ga56690794dc07dfa598ae2ac68bc90aa0"></a>
<a id="agroup__bt__obex_html_ga58034dc9ba274030eea5bc3980e2ff95"></a>
<a id="agroup__bt__obex_html_ga5a181f7779df1ed2919ba3a94a630df4"></a>
<a id="agroup__bt__obex_html_ga5ae88dad0e7c97d0f20c7e4ceeeb3ce8"></a>
<a id="agroup__bt__obex_html_ga5c93e9786adfb45a60a911087f859757"></a>
<a id="agroup__bt__obex_html_ga6206007c2c3e50d997ae5a644ceae783"></a>
<a id="agroup__bt__obex_html_ga622610a779a2e050e9a05c7eae945b3e"></a>
<a id="agroup__bt__obex_html_ga6392da7ce8009eb95ab8c8a4d45fcb40"></a>
<a id="agroup__bt__obex_html_ga642bfabb90d6576f92c5b546a592ec17"></a>
<a id="agroup__bt__obex_html_ga6d61b4421ad1e56cc2ae611ec77e561e"></a>
<a id="agroup__bt__obex_html_ga6ee576eecea3947f1832d4859f16e1db"></a>
<a id="agroup__bt__obex_html_ga6f9de12183c445557f952fe2b49e3029"></a>
<a id="agroup__bt__obex_html_ga7473f42bef1409100886f7812a71a1dc"></a>
<a id="agroup__bt__obex_html_ga7501193240498e7a9da0034b2e434ffc"></a>
<a id="agroup__bt__obex_html_ga7cb42acb39c601375ef7c73f6be7e6af"></a>
<a id="agroup__bt__obex_html_ga805f13b12c7ce23057cb983d7159c36b"></a>
<a id="agroup__bt__obex_html_ga81b84c24a976c6c13d33eb23b0b10ae9"></a>
<a id="agroup__bt__obex_html_ga877d67e0a4135cabf8b5fddab4d014c6"></a>
<a id="agroup__bt__obex_html_ga945c0865edef9f34e2cf1e817a3b45c1"></a>
<a id="agroup__bt__obex_html_ga96981ef9187406efbd374fd623a14eaa"></a>
<a id="agroup__bt__obex_html_ga9cd4c8342f67b53a3c3177a51f8887cb"></a>
<a id="agroup__bt__obex_html_ga9e08bf74bfbf001a80f40ee2d1b1ef82"></a>
<a id="agroup__bt__obex_html_gaaa33502f3ae9f97767bd0e5e660f021f"></a>
<a id="agroup__bt__obex_html_gaaa8a9630b0bf5597ca620b864fdafa87"></a>
<a id="agroup__bt__obex_html_gaab47709ef621b63172fa54314bf3eff0"></a>
<a id="agroup__bt__obex_html_gab234af4e944a3e97e3459613078005a1"></a>
<a id="agroup__bt__obex_html_gab3db35da4b3daf626e89223262273fb9"></a>
<a id="agroup__bt__obex_html_gab4b0a3533c7ec044efbee05c852d4f09"></a>
<a id="agroup__bt__obex_html_gab551b01deed2c5a31f9a7a4b99045c9c"></a>
<a id="agroup__bt__obex_html_gab5dfc5988d17ef0b79b84fd4c96dc60a"></a>
<a id="agroup__bt__obex_html_gab5f7e6a6c7503f97a851f48c70162483"></a>
<a id="agroup__bt__obex_html_gaba71a8b3b8adc251a5a87fa60848bb3c"></a>
<a id="agroup__bt__obex_html_gabcfa9b33c0f91fbcf787d58e1f1bba41"></a>
<a id="agroup__bt__obex_html_gabd3ff76e8a39e5944daa944f38a63c5f"></a>
<a id="agroup__bt__obex_html_gabef4622fa48b493f6d6ad5d1ecb65726"></a>
<a id="agroup__bt__obex_html_gac47ddfe8cfe1e595a1821f32415d14eb"></a>
<a id="agroup__bt__obex_html_gac7763a310a553b3ba3c6b8b06951f191"></a>
<a id="agroup__bt__obex_html_gac778e8ff0ac7e74795b107750a4a6719"></a>
<a id="agroup__bt__obex_html_gacbae9ed1d18eaab7934258cbfe4fd62a"></a>
<a id="agroup__bt__obex_html_gacc1673746737e4163165b5f379c8105f"></a>
<a id="agroup__bt__obex_html_gaccecf00dc6209d1701ac0a6985f38257"></a>
<a id="agroup__bt__obex_html_gacee063f6b53b85bad52a519cd1c794c5"></a>
<a id="agroup__bt__obex_html_gacfc897d66e8c14629fa4d94f3782c741"></a>
<a id="agroup__bt__obex_html_gad1b3c22eea0915b962d7ab1e27726fe2"></a>
<a id="agroup__bt__obex_html_gad4a84068ce8c7c37b5189d366b771235"></a>
<a id="agroup__bt__obex_html_gad91f69ba1b6780501722221bc516db4b"></a>
<a id="agroup__bt__obex_html_gad9bae471db418e0a50c1b234e37b5d9d"></a>
<a id="agroup__bt__obex_html_gadc92dff93ef2051ff8b3b277a1bc1f17"></a>
<a id="agroup__bt__obex_html_gadd9f9b4cb50eb51df05c60705223e53b"></a>
<a id="agroup__bt__obex_html_gadf2d0b93618e0e29341bc21dfd44954f"></a>
<a id="agroup__bt__obex_html_gae0865eea3d8db09023cfc77b2118bad5"></a>
<a id="agroup__bt__obex_html_gae178bf14d0495ad1e1aa5f7b4d8e1652"></a>
<a id="agroup__bt__obex_html_gae31398502c9d237d7afd47d70315be3f"></a>
<a id="agroup__bt__obex_html_gaeacfe7cb654bf33e7b387358a19fd3d3"></a>
<a id="agroup__bt__obex_html_gaedc6f39972a5414d085ce17b09ffd121"></a>
<a id="agroup__bt__obex_html_gaf8ff29ef3413492d2ec67fba278c2f82"></a>
<a id="agroup__bt__obex_html_gaf9ffc19ef06a2773d664c0b15b2b8857"></a>
<a id="agroup__bt__obex_html_gafa2e01166c3177fe3aea937632fb52b7"></a>
<a id="agroup__bt__obex_html_gafadd6e44ae19786617b5e60608fa4651"></a>
<a id="agroup__bt__obex_html_gga12730d705667c2717c05a75cdfc07281a711263abb984488b8c7273052fb76ae0"></a>
<a id="agroup__bt__obex_html_gga12730d705667c2717c05a75cdfc07281a7c57548121adf0afe43066070ef4b1fa"></a>
<a id="agroup__bt__obex_html_gga12730d705667c2717c05a75cdfc07281abb151a8123c7e6826a052ab252455aee"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a01e2d13304514242e954d45e74e3fcba"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a0fb867c69fb0c8680170359a41f2a3b1"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a31bec44f1240f21545f917eedd31026e"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a3264aa53da0fd7ec6611b8a20a8745f4"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a3417001aed5d114492dcbe2c29496a1b"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a3d42ab8b6a28f9062a97e2b1a9fa7c16"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a46735e651f7f378a3efb1be1a232e4ca"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a4fad7112257bd771e412eefd0c1e8bcc"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a5929acc483779593b1b5c7b702b17976"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a5b723fde52df0965299d2f79e433c0a2"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a6119d9faab405c63a25791edc9588889"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a65e148b396f75cd55b992df84d5176ff"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a6aad7cbbcbebe670d370919fbdc61c19"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a6dac6844a5db11dbc0e43613a32c13a9"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a8bfeff22eabea432eb5863a974adb745"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948a97c1dfb166ac549576d30cadd156365f"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948aa48d582e278e748574d57818a7f5daf1"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948aa722c75042f0db4fba5c6a90516494b1"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948aaa78dab2eda48ebd5d594024b53bec6b"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948ab28b3ee885c373ca83a745fcd019e2e4"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948ac2899a8dca76bfd88bb94d43a3c8a693"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948adda0f643d1c2ebd20d4c9d5644ef6b2c"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948adf199ff987c26bd8d6301c409fb5f6a4"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948ae075bf9dd7e57c66613ffb3de84f09bb"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948ae5149b2da2cfb3c2e832f51282bc08d6"></a>
<a id="agroup__bt__obex_html_gga3c893652eb9a5f0bf699d357caf40948afe34bec1dba1d1fca717f3ffa7c20628"></a>
<a id="agroup__bt__obex_html_gga622610a779a2e050e9a05c7eae945b3ea15ddd595c7832a8bfd382f87b938723b"></a>
<a id="agroup__bt__obex_html_gga622610a779a2e050e9a05c7eae945b3ea8743efcfd509ba7b156ac91a3c928614"></a>
<a id="agroup__bt__obex_html_gga622610a779a2e050e9a05c7eae945b3ead7138e7373f5562faf13faa8bca424e6"></a>
<a id="agroup__bt__obex_html_gga622610a779a2e050e9a05c7eae945b3eae41568fe4c0d0db81ff60f41be6443a5"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a21783b5d9036d61304a7acb3b03d0913"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a2b91abe9e010465f9514f37477b993e0"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a2d2ff2c6ec42d9e80dc4e841e19d31ee"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a2f88a5bf5bb9690d8db856bf02f305d8"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a32d55bb3c73ecb8cdf5f76c6724c9884"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a3b948c9bdf3bebd2b0e7cf34960c19b2"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a3f510d3b203257a37d2ef005d4517a67"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a3f60fb4d3444570c9a73f43b7c9bdc1f"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a48f773daa7f2dabaadc37142ec32ffd1"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a4b7a12b0e11747d1a470e8f559b55ea8"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a4e8f5c004cf3ef6e9ad1b5be1d106a39"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a5c0692d0e3db45a898426b2751e682a0"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a5fc2aa165ffea0caeb59e05ee951e3dc"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a613e95b96eaba0522070b620b4b90953"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a650312673ccc758b735bcead8f1009ef"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a7e38ca653283f53b62fa4b21f48d998a"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a850bbc0fd1810e3a74f2a057e8358b48"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a881d3098a198dc1eced2150a213d1054"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9a955b065ee2543e0bc31a03d9bd15900b"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9aa34ece6da3fe28ec3747ce8621da7e31"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9aa5252b1eaa5fa7d41052d97af24fd4d7"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9aacc05fd2528e29fbd53eb5ff940f9079"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9ab33e506b470df404119976d5460b6bda"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9ab41b31b5e85dcb2981b3f6e9bbba2dd9"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9aba13d60d30201bdb13f01c1ee2ff7916"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9aba8108ac6b050d3dad845a5e8cb42eaf"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9abf41a7e722e12bd71a93093e36bfc2bf"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9ac0faf667c93a32293fbacca2e1696938"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9ac19ffb8b59a7cb1a3e0c1edfe91dd472"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9ac25903e3a229ac50ecea485eca8c5236"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9ac39d7d6fa1fcb0cc5be0ad25aa2574f9"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9acfbc9161dddf6859dd8e8ac70cf8d446"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9ad65c4246d828770010748b1faa6af71c"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9adc906b909c09a8a1cc421e8f4efc1444"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9add3501ba98c972e0e01a6fa898612bd4"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9aeb2abeaf682a47a46291784c2b24b793"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9aeca60f95428624932314fc8f3b4a1b79"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9af449d3c85fbec550c76e29287a626789"></a>
<a id="agroup__bt__obex_html_gga81b84c24a976c6c13d33eb23b0b10ae9afcf5fc7c81eed4d5b67def413535a46f"></a>
<a id="agroup__bt__obex_html_ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75"></a>
<a id="agroup__bt__obex_html_ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553"></a>
<a id="agroup__net__buf_html_gaecbc6adf16469e3366c88445ea7a553a"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_ga3acffbd305ee72dcd4593c0d8af64a4f"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga6a05c923dad0c1208043e9c20a58c8e5"></a>
<a id="akernel_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astring_8h_html"></a>
<a id="astructbt__obex__client__ops_html"></a>
<a id="astructbt__obex__client__ops_html_a1a09c04578beca66cac473fe125747cd"></a>
<a id="astructbt__obex__client__ops_html_a1e7227232515d875123e6f8ed2bfd993"></a>
<a id="astructbt__obex__client__ops_html_a250940fb4d5b0a2e782645ba7307fd70"></a>
<a id="astructbt__obex__client__ops_html_a28ee9ffbbd94c961ef28216ec958d604"></a>
<a id="astructbt__obex__client__ops_html_a6a5cb209c9fb53786ee51ac4080d7bbc"></a>
<a id="astructbt__obex__client__ops_html_ac47ffc1353bef9d4d3725e05b75461f2"></a>
<a id="astructbt__obex__client__ops_html_ae63892d7c4ec6850de4137b466e0fa94"></a>
<a id="astructbt__obex__client_html"></a>
<a id="astructbt__obex__client_html_a271142fde25a5622e25404e3a1f469ad"></a>
<a id="astructbt__obex__client_html_a4b9a3f84253936e7babbfc0077da994a"></a>
<a id="astructbt__obex__client_html_ac66119d12d329310a666a1b2d7175fce"></a>
<a id="astructbt__obex__client_html_adb6891c7c9682987c12021280e18c8d4"></a>
<a id="astructbt__obex__client_html_add9c1c75137848fbfbaf65b63ed01e3b"></a>
<a id="astructbt__obex__hdr_html"></a>
<a id="astructbt__obex__hdr_html_a039bc4f46929c1f9e6c12012fee1e88b"></a>
<a id="astructbt__obex__hdr_html_aa453f73fd7a159d92b193dc53c10d995"></a>
<a id="astructbt__obex__hdr_html_ad1f539c20ef8f9e8849326b7d8b64101"></a>
<a id="astructbt__obex__server__ops_html"></a>
<a id="astructbt__obex__server__ops_html_a0449e9ab3018796818460f95dd2df13e"></a>
<a id="astructbt__obex__server__ops_html_a2763317faa8d5a1371e979d6021ca114"></a>
<a id="astructbt__obex__server__ops_html_a7380f0fdb31a7f82f75b65a857037987"></a>
<a id="astructbt__obex__server__ops_html_a90839fcaf2bd369d1d5a8c833003f2be"></a>
<a id="astructbt__obex__server__ops_html_a98b433a269295f3784bce6100aea186a"></a>
<a id="astructbt__obex__server__ops_html_ab7e99df178911eef8cc8192716a64412"></a>
<a id="astructbt__obex__server__ops_html_ae761cd5aa9728448ee97f306ab9332a6"></a>
<a id="astructbt__obex__server_html"></a>
<a id="astructbt__obex__server_html_a03527bd1e6f2907658756c08e342c283"></a>
<a id="astructbt__obex__server_html_a3aa4c23ecfea67698b6739b670a77aae"></a>
<a id="astructbt__obex__server_html_a3ea81fb07df98a2dd9b9bfdb0acfdf62"></a>
<a id="astructbt__obex__server_html_ac3acbf06e1dfa787507bba076be85e14"></a>
<a id="astructbt__obex__server_html_ac96bcf45b1753cacb8a797c5f7c29eed"></a>
<a id="astructbt__obex__server_html_aefe5b0dbed43308a4881643b5705f033"></a>
<a id="astructbt__obex__tlv_html"></a>
<a id="astructbt__obex__tlv_html_a18d22dae9d1f069d2403398454fadd45"></a>
<a id="astructbt__obex__tlv_html_abb39dc76c06c3dd89a739f3111d143b5"></a>
<a id="astructbt__obex__tlv_html_addcdfe5b297fe7cd9e1f30eee8ade4d7"></a>
<a id="astructbt__obex__transport__ops_html"></a>
<a id="astructbt__obex__transport__ops_html_a2c04d635154acfa9f4579596d8ed7d79"></a>
<a id="astructbt__obex__transport__ops_html_a57fc547e578a62e6ebb9da89e0ae423c"></a>
<a id="astructbt__obex_html"></a>
<a id="astructbt__obex_html_a9aa32991272416015a9746e7cf8e9027"></a>
<a id="astructbt__obex_html_aa22aa60d3dc3308865508717a4b9c398"></a>
<a id="astructbt__obex_html_ac2bc4ebc3b440c1be71c033b7c051c98"></a>
<a id="astructbt__uuid__128_html"></a>
<a id="astructbt__uuid__16_html"></a>
<a id="astructbt__uuid__32_html"></a>
<a id="astructbt__uuid_html"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_ae75b7ca728fb7440ea483be8bf88bc38"></a>
<a id="astructuuid_html"></a>
<a id="aunionbt__obex__uuid_html"></a>
<a id="aunionbt__obex__uuid_html_a37e133ae223fc603ea719e37aca12e57"></a>
<a id="aunionbt__obex__uuid_html_a70f016148a0f2c7477f7d603f0c70bca"></a>
<a id="aunionbt__obex__uuid_html_ac2f5f7bd61988322a3104a36efddb687"></a>
<a id="aunionbt__obex__uuid_html_aed352f85b180d4544b7f16d6d3394abe"></a>

```c
/* obex.h - IrDA Object Exchange Protocol handling */

/*
 * Copyright 2024-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_OBEX_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_OBEX_H_


#include <zephyr/kernel.h>
#include <string.h>
#include <errno.h>
#include <stdbool.h>

#include <zephyr/bluetooth/uuid.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_OBEX_MIN_MTU 255

enum __packed bt_obex_rsp_code {
        BT_OBEX_RSP_CODE_CONTINUE = 0x90,
        BT_OBEX_RSP_CODE_OK = 0xa0,
        BT_OBEX_RSP_CODE_SUCCESS = 0xa0,
        BT_OBEX_RSP_CODE_CREATED = 0xa1,
        BT_OBEX_RSP_CODE_ACCEPTED = 0xa2,
        BT_OBEX_RSP_CODE_NON_AUTH_INFO = 0xa3,
        BT_OBEX_RSP_CODE_NO_CONTENT = 0xa4,
        BT_OBEX_RSP_CODE_RESET_CONTENT = 0xa5,
        BT_OBEX_RSP_CODE_PARTIAL_CONTENT = 0xa6,
        BT_OBEX_RSP_CODE_MULTI_CHOICES = 0xb0,
        BT_OBEX_RSP_CODE_MOVED_PERM = 0xb1,
        BT_OBEX_RSP_CODE_MOVED_TEMP = 0xb2,
        BT_OBEX_RSP_CODE_SEE_OTHER = 0xb3,
        BT_OBEX_RSP_CODE_NOT_MODIFIED = 0xb4,
        BT_OBEX_RSP_CODE_USE_PROXY = 0xb5,
        BT_OBEX_RSP_CODE_BAD_REQ = 0xc0,
        BT_OBEX_RSP_CODE_UNAUTH = 0xc1,
        BT_OBEX_RSP_CODE_PAY_REQ = 0xc2,
        BT_OBEX_RSP_CODE_FORBIDDEN = 0xc3,
        BT_OBEX_RSP_CODE_NOT_FOUND = 0xc4,
        BT_OBEX_RSP_CODE_NOT_ALLOW = 0xc5,
        BT_OBEX_RSP_CODE_NOT_ACCEPT = 0xc6,
        BT_OBEX_RSP_CODE_PROXY_AUTH_REQ = 0xc7,
        BT_OBEX_RSP_CODE_REQ_TIMEOUT = 0xc8,
        BT_OBEX_RSP_CODE_CONFLICT = 0xc9,
        BT_OBEX_RSP_CODE_GONE = 0xca,
        BT_OBEX_RSP_CODE_LEN_REQ = 0xcb,
        BT_OBEX_RSP_CODE_PRECON_FAIL = 0xcc,
        BT_OBEX_RSP_CODE_ENTITY_TOO_LARGE = 0xcd,
        BT_OBEX_RSP_CODE_URL_TOO_LARGE = 0xce,
        BT_OBEX_RSP_CODE_UNSUPP_MEDIA_TYPE = 0xcf,
        BT_OBEX_RSP_CODE_INTER_ERROR = 0xd0,
        BT_OBEX_RSP_CODE_NOT_IMPL = 0xd1,
        BT_OBEX_RSP_CODE_BAD_GATEWAY = 0xd2,
        BT_OBEX_RSP_CODE_UNAVAIL = 0xd3,
        BT_OBEX_RSP_CODE_GATEWAY_TIMEOUT = 0xd4,
        BT_OBEX_RSP_CODE_VER_UNSUPP = 0xd5,
        BT_OBEX_RSP_CODE_DB_FULL = 0xe0,
        BT_OBEX_RSP_CODE_DB_LOCK = 0xe1,
};

#if defined(CONFIG_BT_OEBX_RSP_CODE_TO_STR)
const char *bt_obex_rsp_code_to_str(enum bt_obex_rsp_code rsp_code);
#else
static inline const char *bt_obex_rsp_code_to_str(enum bt_obex_rsp_code rsp_code)
{
        ARG_UNUSED(rsp_code);

        return "";
}
#endif /* CONFIG_BT_OEBX_RSP_CODE_TO_STR */

enum __packed bt_obex_header_id {
        BT_OBEX_HEADER_ID_COUNT = 0xC0,

        BT_OBEX_HEADER_ID_NAME = 0x01,

        BT_OBEX_HEADER_ID_TYPE = 0x42,

        BT_OBEX_HEADER_ID_LEN = 0xC3,

        BT_OBEX_HEADER_ID_TIME_ISO_8601 = 0x44,

        BT_OBEX_HEADER_ID_TIME = 0xC4,

        BT_OBEX_HEADER_ID_DES = 0x05,

        BT_OBEX_HEADER_ID_TARGET = 0x46,

        BT_OBEX_HEADER_ID_HTTP = 0x47,

        BT_OBEX_HEADER_ID_BODY = 0x48,

        BT_OBEX_HEADER_ID_END_BODY = 0x49,

        BT_OBEX_HEADER_ID_WHO = 0x4A,

        BT_OBEX_HEADER_ID_CONN_ID = 0xCB,

        BT_OBEX_HEADER_ID_APP_PARAM = 0x4C,

        BT_OBEX_HEADER_ID_AUTH_CHALLENGE = 0x4D,

        BT_OBEX_HEADER_ID_AUTH_RSP = 0x4E,

        BT_OBEX_HEADER_ID_CREATE_ID = 0xCF,

        BT_OBEX_HEADER_ID_WAN_UUID = 0x50,

        BT_OBEX_HEADER_ID_OBJECT_CLASS = 0x51,

        BT_OBEX_HEADER_ID_SESSION_PARAM = 0x52,

        BT_OBEX_HEADER_ID_SESSION_SEQ_NUM = 0x93,

        BT_OBEX_HEADER_ID_ACTION_ID = 0x94,

        BT_OBEX_HEADER_ID_DEST_NAME = 0x15,

        BT_OBEX_HEADER_ID_PERM = 0xD6,

        BT_OBEX_HEADER_ID_SRM = 0x97,

        BT_OBEX_HEADER_ID_SRM_PARAM = 0x98,
};

#define BT_OBEX_HDR_LEN 3

#define BT_OBEX_PDU_LEN(mopl) ((mopl) - BT_OBEX_HDR_LEN)

#define BT_OBEX_HDR_LEN_OF_HEADER_BODY 3

#define BT_OBEX_DATA_LEN_OF_HEADER_BODY(len) ((len) - BT_OBEX_HDR_LEN_OF_HEADER_BODY)

#define BT_OBEX_SEND_BUF_RESERVE 7

struct bt_obex;
struct bt_obex_server;
struct bt_obex_client;

struct bt_obex_server_ops {
        void (*connect)(struct bt_obex_server *server, uint8_t version, uint16_t mopl,
                        struct net_buf *buf);

        void (*disconnect)(struct bt_obex_server *server, struct net_buf *buf);

        void (*put)(struct bt_obex_server *server, bool final, struct net_buf *buf);

        void (*get)(struct bt_obex_server *server, bool final, struct net_buf *buf);

        void (*abort)(struct bt_obex_server *server, struct net_buf *buf);

        void (*setpath)(struct bt_obex_server *server, uint8_t flags, struct net_buf *buf);

        void (*action)(struct bt_obex_server *server, bool final, struct net_buf *buf);
};

struct bt_obex_client_ops {
        void (*connect)(struct bt_obex_client *client, uint8_t rsp_code, uint8_t version,
                        uint16_t mopl, struct net_buf *buf);

        void (*disconnect)(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*put)(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*get)(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*abort)(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*setpath)(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf);

        void (*action)(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf);
};

struct bt_obex_transport_ops {
        struct net_buf *(*alloc_buf)(struct bt_obex *obex, struct net_buf_pool *pool);

        int (*send)(struct bt_obex *obex, struct net_buf *buf);

        int (*disconnect)(struct bt_obex *obex);
};

enum __packed bt_obex_state {
        BT_OBEX_DISCONNECTED,
        BT_OBEX_CONNECTING,
        BT_OBEX_CONNECTED,
        BT_OBEX_DISCONNECTING,
};

union bt_obex_uuid {
        struct bt_uuid uuid;
        struct bt_uuid_16 u16;
        struct bt_uuid_32 u32;
        struct bt_uuid_128 u128;
};

struct bt_obex_server {
        struct bt_obex *obex;

        const struct bt_uuid_128 *uuid;

        const struct bt_obex_server_ops *ops;

        struct {
                uint16_t mopl;
        } rx;

        struct {
                uint16_t mopl;
        } tx;

        atomic_t _state;

        atomic_t _opcode;

        atomic_t _flags;

        union bt_obex_uuid _target;

        uint32_t _conn_id;

        sys_snode_t _node;
};

struct bt_obex_client {
        struct bt_obex *obex;

        const struct bt_obex_client_ops *ops;

        struct {
                uint16_t mopl;
        } rx;

        struct {
                uint16_t mopl;
        } tx;

        atomic_t _state;

        atomic_t _opcode;

        atomic_t _pre_opcode;

        atomic_t _flags;

        union bt_obex_uuid _target;

        uint32_t _conn_id;

        sys_snode_t _node;
};

struct bt_obex {
        struct {
                uint16_t mtu;
        } rx;

        struct {
                uint16_t mtu;
        } tx;

        const struct bt_obex_transport_ops *_transport_ops;

        atomic_ptr_t _active_client;

        atomic_ptr_t _last_client;

        atomic_ptr_t _active_server;

        sys_slist_t _clients;

        sys_slist_t _servers;
};

int bt_obex_server_register(struct bt_obex_server *server, const struct bt_uuid_128 *uuid);

int bt_obex_server_unregister(struct bt_obex_server *server);

int bt_obex_connect(struct bt_obex_client *client, uint16_t mopl, struct net_buf *buf);

int bt_obex_connect_rsp(struct bt_obex_server *server, uint8_t rsp_code, uint16_t mopl,
                        struct net_buf *buf);

int bt_obex_disconnect(struct bt_obex_client *client, struct net_buf *buf);

int bt_obex_disconnect_rsp(struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_obex_put(struct bt_obex_client *client, bool final, struct net_buf *buf);

int bt_obex_put_rsp(struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_obex_get(struct bt_obex_client *client, bool final, struct net_buf *buf);

int bt_obex_get_rsp(struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_obex_abort(struct bt_obex_client *client, struct net_buf *buf);

int bt_obex_abort_rsp(struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf);

enum __packed bt_obex_setpath_flags {
        BT_OBEX_SETPATH_FLAG_BACKUP = BIT(0U),
        BT_OBEX_SETPATH_FLAG_NO_CREATE = BIT(1U),
};

int bt_obex_setpath(struct bt_obex_client *client, uint8_t flags, struct net_buf *buf);

int bt_obex_setpath_rsp(struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf);

enum __packed bt_obex_action_id {
        BT_OBEX_ACTION_COPY = 0x00,
        BT_OBEX_ACTION_MOVE_RENAME = 0x01,
        BT_OBEX_ACTION_SET_PERM = 0x02,
};

int bt_obex_action(struct bt_obex_client *client, bool final, struct net_buf *buf);

int bt_obex_action_rsp(struct bt_obex_server *server, uint8_t rsp_code, struct net_buf *buf);

int bt_obex_add_header_count(struct net_buf *buf, uint32_t count);

int bt_obex_add_header_name(struct net_buf *buf, uint16_t len, const uint8_t *name);

int bt_obex_add_header_type(struct net_buf *buf, uint16_t len, const uint8_t *type);

int bt_obex_add_header_len(struct net_buf *buf, uint32_t len);

int bt_obex_add_header_time_iso_8601(struct net_buf *buf, uint16_t len, const uint8_t *t);

int bt_obex_add_header_time(struct net_buf *buf, uint32_t t);

int bt_obex_add_header_description(struct net_buf *buf, uint16_t len, const uint8_t *dec);

int bt_obex_add_header_target(struct net_buf *buf, uint16_t len, const uint8_t *target);

int bt_obex_add_header_http(struct net_buf *buf, uint16_t len, const uint8_t *http);

int bt_obex_add_header_body(struct net_buf *buf, uint16_t len, const uint8_t *body);

int bt_obex_add_header_end_body(struct net_buf *buf, uint16_t len, const uint8_t *body);

static inline int bt_obex_add_header_body_or_end_body(struct net_buf *buf, uint16_t mopl,
                                                      uint16_t len, const uint8_t *body,
                                                      uint16_t *added_len)
{
        uint16_t tx_len;
        int err;

        /*
         * OBEX Version 1.5, section 2.2.9 Body, End-of-Body
         * The `body` could be a NULL, so the `len` of the name could 0.
         * In some cases, the object body data is generated on the fly and the end cannot
         * be anticipated, so it is legal to send a zero length End-of-Body header.
         */
        if ((buf == NULL) || ((len != 0) && (body == NULL)) || (added_len == NULL) ||
            (mopl < BT_OBEX_MIN_MTU)) {
                return -EINVAL;
        }

        tx_len = BT_OBEX_PDU_LEN(mopl);
        if (tx_len <= buf->len) {
                return -ENOMEM;
        }

        *added_len = 0;

        tx_len = MIN((tx_len - buf->len), net_buf_tailroom(buf));
        if (tx_len <= BT_OBEX_HDR_LEN_OF_HEADER_BODY) {
                return 0;
        }

        tx_len = BT_OBEX_DATA_LEN_OF_HEADER_BODY(tx_len);
        if (tx_len >= len) {
                *added_len = len;
                err = bt_obex_add_header_end_body(buf, len, body);
        } else {
                *added_len = tx_len;
                err = bt_obex_add_header_body(buf, tx_len, body);
        }

        return err;
}

int bt_obex_add_header_who(struct net_buf *buf, uint16_t len, const uint8_t *who);

int bt_obex_add_header_conn_id(struct net_buf *buf, uint32_t conn_id);

struct bt_obex_tlv {
        uint8_t type;
        uint8_t data_len;
        const uint8_t *data;
};

int bt_obex_add_header_app_param(struct net_buf *buf, size_t count,
                                 const struct bt_obex_tlv data[]);

#define BT_OBEX_CHALLENGE_TAG_NONCE 0x00
#define BT_OBEX_CHALLENGE_TAG_NONCE_LEN 16

#define BT_OBEX_CHALLENGE_TAG_OPTIONS 0x01
#define BT_OBEX_CHALLENGE_TAG_OPTIONS_LEN 1

#define BT_OBEX_CHALLENGE_TAG_OPTION_REQ_USER_ID BIT(0)
#define BT_OBEX_CHALLENGE_TAG_OPTION_ACCESS_MODE BIT(1)

#define BT_OBEX_CHALLENGE_TAG_REALM 0x02

int bt_obex_add_header_auth_challenge(struct net_buf *buf, size_t count,
                                      const struct bt_obex_tlv data[]);

#define BT_OBEX_RESPONSE_TAG_REQ_DIGEST 0x00
#define BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN 16

#define BT_OBEX_RESPONSE_TAG_USER_ID 0x01

#define BT_OBEX_RESPONSE_TAG_NONCE 0x02
#define BT_OBEX_RESPONSE_TAG_NONCE_LEN 16

int bt_obex_add_header_auth_rsp(struct net_buf *buf, size_t count, const struct bt_obex_tlv data[]);

int bt_obex_add_header_creator_id(struct net_buf *buf, uint32_t creator_id);

int bt_obex_add_header_wan_uuid(struct net_buf *buf, uint16_t len, const uint8_t *uuid);

int bt_obex_add_header_obj_class(struct net_buf *buf, uint16_t len, const uint8_t *obj_class);

int bt_obex_add_header_session_param(struct net_buf *buf, uint16_t len,
                                     const uint8_t *session_param);

int bt_obex_add_header_session_seq_number(struct net_buf *buf, uint32_t session_seq_number);

int bt_obex_add_header_action_id(struct net_buf *buf, uint8_t action_id);

int bt_obex_add_header_dest_name(struct net_buf *buf, uint16_t len, const uint8_t *dest_name);

int bt_obex_add_header_perm(struct net_buf *buf, uint32_t perm);

int bt_obex_add_header_srm(struct net_buf *buf, uint8_t srm);

int bt_obex_add_header_srm_param(struct net_buf *buf, uint8_t srm_param);

struct bt_obex_hdr {
        uint8_t id;
        uint16_t len;
        const uint8_t *data;
};

int bt_obex_header_parse(struct net_buf *buf,
                         bool (*func)(struct bt_obex_hdr *hdr, void *user_data), void *user_data);

int bt_obex_get_header_count(struct net_buf *buf, uint32_t *count);

int bt_obex_get_header_name(struct net_buf *buf, uint16_t *len, const uint8_t **name);

int bt_obex_get_header_type(struct net_buf *buf, uint16_t *len, const uint8_t **type);

int bt_obex_get_header_len(struct net_buf *buf, uint32_t *len);

int bt_obex_get_header_time_iso_8601(struct net_buf *buf, uint16_t *len, const uint8_t **t);

int bt_obex_get_header_time(struct net_buf *buf, uint32_t *t);

int bt_obex_get_header_description(struct net_buf *buf, uint16_t *len, const uint8_t **dec);

int bt_obex_get_header_target(struct net_buf *buf, uint16_t *len, const uint8_t **target);

int bt_obex_get_header_http(struct net_buf *buf, uint16_t *len, const uint8_t **http);

int bt_obex_get_header_body(struct net_buf *buf, uint16_t *len, const uint8_t **body);

int bt_obex_get_header_end_body(struct net_buf *buf, uint16_t *len, const uint8_t **body);

int bt_obex_get_header_who(struct net_buf *buf, uint16_t *len, const uint8_t **who);

int bt_obex_get_header_conn_id(struct net_buf *buf, uint32_t *conn_id);

int bt_obex_tlv_parse(uint16_t len, const uint8_t *data,
                      bool (*func)(struct bt_obex_tlv *tlv, void *user_data), void *user_data);

int bt_obex_get_header_app_param(struct net_buf *buf, uint16_t *len, const uint8_t **app_param);

int bt_obex_get_header_auth_challenge(struct net_buf *buf, uint16_t *len, const uint8_t **auth);

int bt_obex_get_header_auth_rsp(struct net_buf *buf, uint16_t *len, const uint8_t **auth);

int bt_obex_get_header_creator_id(struct net_buf *buf, uint32_t *creator_id);

int bt_obex_get_header_wan_uuid(struct net_buf *buf, uint16_t *len, const uint8_t **uuid);

int bt_obex_get_header_obj_class(struct net_buf *buf, uint16_t *len, const uint8_t **obj_class);

int bt_obex_get_header_session_param(struct net_buf *buf, uint16_t *len,
                                     const uint8_t **session_param);

int bt_obex_get_header_session_seq_number(struct net_buf *buf, uint32_t *session_seq_number);

int bt_obex_get_header_action_id(struct net_buf *buf, uint8_t *action_id);

int bt_obex_get_header_dest_name(struct net_buf *buf, uint16_t *len, const uint8_t **dest_name);

int bt_obex_get_header_perm(struct net_buf *buf, uint32_t *perm);

int bt_obex_get_header_srm(struct net_buf *buf, uint8_t *srm);

int bt_obex_get_header_srm_param(struct net_buf *buf, uint8_t *srm_param);

int bt_obex_make_uuid(union bt_obex_uuid *uuid, const uint8_t *data, uint16_t len);

bool bt_obex_string_is_valid(uint8_t id, uint16_t len, const uint8_t *str);

bool bt_obex_has_header(struct net_buf *buf, uint8_t id);

bool bt_obex_has_app_param(struct net_buf *buf, uint8_t id);

int bt_obex_generate_nonce(const uint8_t *pwd, size_t pwd_len,
                           uint8_t nonce[BT_OBEX_CHALLENGE_TAG_NONCE_LEN]);

int bt_obex_calculate_request_digest(const uint8_t *pwd, size_t pwd_len,
                                     const uint8_t nonce[BT_OBEX_CHALLENGE_TAG_NONCE_LEN],
                                     uint8_t digest[BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN]);

int bt_obex_verify_auth_response(const uint8_t *pwd, size_t pwd_len,
                                 const uint8_t nonce[BT_OBEX_CHALLENGE_TAG_NONCE_LEN],
                                 const uint8_t digest[BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN]);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_OBEX_H_ */
```

## 62.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`obex.h`：IrDA 对象交换协议（Object Exchange Protocol）的处理。

### 注释 2：原第 3 行

版权（Copyright）：2024-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 131 行

条件编译配置（Configuration）标记：`CONFIG_BT_OEBX_RSP_CODE_TO_STR`。

### 注释 4：原第 1192 行

OBEX 1.5 版第 2.2.9 节“Body、End-of-Body”。`body` 可以为 NULL，因此名称的 `len` 可以为 0。在某些情况下，对象正文数据是在运行中生成的，无法预先知道何时结束，因此允许发送长度为零的正文结束头（End-of-Body header）。

译注：“名称的 len”按原注释（the len of the name）保留。

### 注释 5：原第 1853 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_OBEX_H_`。

## 62.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [bt_obex_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga81b84c24a976c6c13d33eb23b0b10ae9)
- [BT_OBEX_RSP_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a7e38ca653283f53b62fa4b21f48d998a)
- [BT_OBEX_RSP_CODE_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a881d3098a198dc1eced2150a213d1054)
- [BT_OBEX_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9af449d3c85fbec550c76e29287a626789)
- [BT_OBEX_RSP_CODE_CREATED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a955b065ee2543e0bc31a03d9bd15900b)
- [BT_OBEX_RSP_CODE_ACCEPTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aba13d60d30201bdb13f01c1ee2ff7916)
- [BT_OBEX_RSP_CODE_NON_AUTH_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a2f88a5bf5bb9690d8db856bf02f305d8)
- [BT_OBEX_RSP_CODE_NO_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a32d55bb3c73ecb8cdf5f76c6724c9884)
- [BT_OBEX_RSP_CODE_RESET_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a4e8f5c004cf3ef6e9ad1b5be1d106a39)
- [BT_OBEX_RSP_CODE_PARTIAL_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9afcf5fc7c81eed4d5b67def413535a46f)
- [BT_OBEX_RSP_CODE_MULTI_CHOICES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a3b948c9bdf3bebd2b0e7cf34960c19b2)
- [BT_OBEX_RSP_CODE_MOVED_PERM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aa5252b1eaa5fa7d41052d97af24fd4d7)
- [BT_OBEX_RSP_CODE_MOVED_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9abf41a7e722e12bd71a93093e36bfc2bf)
- [BT_OBEX_RSP_CODE_SEE_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac25903e3a229ac50ecea485eca8c5236)
- [BT_OBEX_RSP_CODE_NOT_MODIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ab33e506b470df404119976d5460b6bda)
- [BT_OBEX_RSP_CODE_USE_PROXY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac19ffb8b59a7cb1a3e0c1edfe91dd472)
- [BT_OBEX_RSP_CODE_BAD_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a2d2ff2c6ec42d9e80dc4e841e19d31ee)
- [BT_OBEX_RSP_CODE_UNAUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9acfbc9161dddf6859dd8e8ac70cf8d446)
- [BT_OBEX_RSP_CODE_PAY_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a5fc2aa165ffea0caeb59e05ee951e3dc)
- [BT_OBEX_RSP_CODE_FORBIDDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a4b7a12b0e11747d1a470e8f559b55ea8)
- [BT_OBEX_RSP_CODE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a2b91abe9e010465f9514f37477b993e0)
- [BT_OBEX_RSP_CODE_NOT_ALLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a3f510d3b203257a37d2ef005d4517a67)
- [BT_OBEX_RSP_CODE_NOT_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a48f773daa7f2dabaadc37142ec32ffd1)
- [BT_OBEX_RSP_CODE_PROXY_AUTH_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aeb2abeaf682a47a46291784c2b24b793)
- [BT_OBEX_RSP_CODE_REQ_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a3f60fb4d3444570c9a73f43b7c9bdc1f)
- [BT_OBEX_RSP_CODE_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aeca60f95428624932314fc8f3b4a1b79)
- [BT_OBEX_RSP_CODE_GONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aa34ece6da3fe28ec3747ce8621da7e31)
- [BT_OBEX_RSP_CODE_LEN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac0faf667c93a32293fbacca2e1696938)
- [BT_OBEX_RSP_CODE_PRECON_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aacc05fd2528e29fbd53eb5ff940f9079)
- [BT_OBEX_RSP_CODE_ENTITY_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a21783b5d9036d61304a7acb3b03d0913)
- [BT_OBEX_RSP_CODE_URL_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9adc906b909c09a8a1cc421e8f4efc1444)
- [BT_OBEX_RSP_CODE_UNSUPP_MEDIA_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a650312673ccc758b735bcead8f1009ef)
- [BT_OBEX_RSP_CODE_INTER_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9add3501ba98c972e0e01a6fa898612bd4)
- [BT_OBEX_RSP_CODE_NOT_IMPL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9aba8108ac6b050d3dad845a5e8cb42eaf)
- [BT_OBEX_RSP_CODE_BAD_GATEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ac39d7d6fa1fcb0cc5be0ad25aa2574f9)
- [BT_OBEX_RSP_CODE_UNAVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a613e95b96eaba0522070b620b4b90953)
- [BT_OBEX_RSP_CODE_GATEWAY_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a850bbc0fd1810e3a74f2a057e8358b48)
- [BT_OBEX_RSP_CODE_VER_UNSUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ab41b31b5e85dcb2981b3f6e9bbba2dd9)
- [BT_OBEX_RSP_CODE_DB_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9ad65c4246d828770010748b1faa6af71c)
- [BT_OBEX_RSP_CODE_DB_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga81b84c24a976c6c13d33eb23b0b10ae9a5c0692d0e3db45a898426b2751e682a0)
- [bt_obex_rsp_code_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga7cb42acb39c601375ef7c73f6be7e6af)
- [bt_obex_header_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3c893652eb9a5f0bf699d357caf40948)
- [BT_OBEX_HEADER_ID_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a6119d9faab405c63a25791edc9588889)
- [BT_OBEX_HEADER_ID_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948adf199ff987c26bd8d6301c409fb5f6a4)
- [BT_OBEX_HEADER_ID_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a8bfeff22eabea432eb5863a974adb745)
- [BT_OBEX_HEADER_ID_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ae075bf9dd7e57c66613ffb3de84f09bb)
- [BT_OBEX_HEADER_ID_TIME_ISO_8601](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ac2899a8dca76bfd88bb94d43a3c8a693)
- [BT_OBEX_HEADER_ID_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a4fad7112257bd771e412eefd0c1e8bcc)
- [BT_OBEX_HEADER_ID_DES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a0fb867c69fb0c8680170359a41f2a3b1)
- [BT_OBEX_HEADER_ID_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a5929acc483779593b1b5c7b702b17976)
- [BT_OBEX_HEADER_ID_HTTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a46735e651f7f378a3efb1be1a232e4ca)
- [BT_OBEX_HEADER_ID_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a3264aa53da0fd7ec6611b8a20a8745f4)
- [BT_OBEX_HEADER_ID_END_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948aaa78dab2eda48ebd5d594024b53bec6b)
- [BT_OBEX_HEADER_ID_WHO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ab28b3ee885c373ca83a745fcd019e2e4)
- [BT_OBEX_HEADER_ID_CONN_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a3417001aed5d114492dcbe2c29496a1b)
- [BT_OBEX_HEADER_ID_APP_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a6dac6844a5db11dbc0e43613a32c13a9)
- [BT_OBEX_HEADER_ID_AUTH_CHALLENGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948aa48d582e278e748574d57818a7f5daf1)
- [BT_OBEX_HEADER_ID_AUTH_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a97c1dfb166ac549576d30cadd156365f)
- [BT_OBEX_HEADER_ID_CREATE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a31bec44f1240f21545f917eedd31026e)
- [BT_OBEX_HEADER_ID_WAN_UUID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a65e148b396f75cd55b992df84d5176ff)
- [BT_OBEX_HEADER_ID_OBJECT_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a5b723fde52df0965299d2f79e433c0a2)
- [BT_OBEX_HEADER_ID_SESSION_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948afe34bec1dba1d1fca717f3ffa7c20628)
- [BT_OBEX_HEADER_ID_SESSION_SEQ_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a3d42ab8b6a28f9062a97e2b1a9fa7c16)
- [BT_OBEX_HEADER_ID_ACTION_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a01e2d13304514242e954d45e74e3fcba)
- [BT_OBEX_HEADER_ID_DEST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948ae5149b2da2cfb3c2e832f51282bc08d6)
- [BT_OBEX_HEADER_ID_PERM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948a6aad7cbbcbebe670d370919fbdc61c19)
- [BT_OBEX_HEADER_ID_SRM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948aa722c75042f0db4fba5c6a90516494b1)
- [BT_OBEX_HEADER_ID_SRM_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga3c893652eb9a5f0bf699d357caf40948adda0f643d1c2ebd20d4c9d5644ef6b2c)
- [bt_obex](../bluetooth_service_model_reference/P127_bt_obex_结构体.md)
- [bt_obex_server](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md)
- [bt_obex_client](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md)
- [bt_obex_server_ops](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md)
- [connect](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#a0449e9ab3018796818460f95dd2df13e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [disconnect](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#ab7e99df178911eef8cc8192716a64412)
- [put](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#ae761cd5aa9728448ee97f306ab9332a6)
- [get](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#a7380f0fdb31a7f82f75b65a857037987)
- [abort](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#a2763317faa8d5a1371e979d6021ca114)
- [setpath](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#a90839fcaf2bd369d1d5a8c833003f2be)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [action](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#a98b433a269295f3784bce6100aea186a)
- [bt_obex_client_ops](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md)
- [connect](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#ac47ffc1353bef9d4d3725e05b75461f2)
- [disconnect](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#a1e7227232515d875123e6f8ed2bfd993)
- [put](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#a6a5cb209c9fb53786ee51ac4080d7bbc)
- [get](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#ae63892d7c4ec6850de4137b466e0fa94)
- [abort](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#a28ee9ffbbd94c961ef28216ec958d604)
- [setpath](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#a250940fb4d5b0a2e782645ba7307fd70)
- [action](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#a1a09c04578beca66cac473fe125747cd)
- [bt_obex_transport_ops](../bluetooth_service_model_reference/P134_bt_obex_transport_ops_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [send](../bluetooth_service_model_reference/P134_bt_obex_transport_ops_结构体.md#a2c04d635154acfa9f4579596d8ed7d79)
- [disconnect](../bluetooth_service_model_reference/P134_bt_obex_transport_ops_结构体.md#a57fc547e578a62e6ebb9da89e0ae423c)
- [bt_obex_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga622610a779a2e050e9a05c7eae945b3e)
- [BT_OBEX_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3ead7138e7373f5562faf13faa8bca424e6)
- [BT_OBEX_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3ea8743efcfd509ba7b156ac91a3c928614)
- [BT_OBEX_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3ea15ddd595c7832a8bfd382f87b938723b)
- [BT_OBEX_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga622610a779a2e050e9a05c7eae945b3eae41568fe4c0d0db81ff60f41be6443a5)
- [bt_obex_uuid](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [uuid](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md#a37e133ae223fc603ea719e37aca12e57)
- [bt_uuid_16](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md)
- [u16](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md#a70f016148a0f2c7477f7d603f0c70bca)
- [bt_uuid_32](../bluetooth_connection_model_reference/P134_bt_uuid_32_结构体.md)
- [u32](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md#ac2f5f7bd61988322a3104a36efddb687)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [u128](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md#aed352f85b180d4544b7f16d6d3394abe)
- [obex](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#ac96bcf45b1753cacb8a797c5f7c29eed)
- [uuid](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#ac3acbf06e1dfa787507bba076be85e14)
- [ops](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#aefe5b0dbed43308a4881643b5705f033)
- [mopl](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#a3aa4c23ecfea67698b6739b670a77aae)
- [rx](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#a03527bd1e6f2907658756c08e342c283)
- [tx](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#a3ea81fb07df98a2dd9b9bfdb0acfdf62)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [obex](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#a271142fde25a5622e25404e3a1f469ad)
- [ops](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#a4b9a3f84253936e7babbfc0077da994a)
- [mopl](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#adb6891c7c9682987c12021280e18c8d4)
- [rx](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#add9c1c75137848fbfbaf65b63ed01e3b)
- [tx](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#ac66119d12d329310a666a1b2d7175fce)
- [mtu](../bluetooth_service_model_reference/P127_bt_obex_结构体.md#aa22aa60d3dc3308865508717a4b9c398)
- [rx](../bluetooth_service_model_reference/P127_bt_obex_结构体.md#ac2bc4ebc3b440c1be71c033b7c051c98)
- [tx](../bluetooth_service_model_reference/P127_bt_obex_结构体.md#a9aa32991272416015a9746e7cf8e9027)
- [atomic_ptr_t](../atomic_reference/P001_原子操作公共接口.md#gacad6866fa4c844026cd9f8c3fb60ecd7)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [bt_obex_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga1df3928a40f544ffb98b5eb1ceac62dd)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_obex_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga642bfabb90d6576f92c5b546a592ec17)
- [bt_obex_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga21afebccbd592381fb1569feaff98511)
- [bt_obex_connect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad91f69ba1b6780501722221bc516db4b)
- [bt_obex_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga107787f08e55bf2740cc14cb5614bdbf)
- [bt_obex_disconnect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gac7763a310a553b3ba3c6b8b06951f191)
- [bt_obex_put](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga1d8684307899b1bd3724cb3aa996c53e)
- [bt_obex_put_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab5dfc5988d17ef0b79b84fd4c96dc60a)
- [bt_obex_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gabd3ff76e8a39e5944daa944f38a63c5f)
- [bt_obex_get_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3e9415fa4595d17676ada6622c9fd475)
- [bt_obex_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gafa2e01166c3177fe3aea937632fb52b7)
- [bt_obex_abort_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6f9de12183c445557f952fe2b49e3029)
- [bt_obex_setpath_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab5f7e6a6c7503f97a851f48c70162483)
- [BT_OBEX_SETPATH_FLAG_BACKUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_OBEX_SETPATH_FLAG_NO_CREATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553)
- [bt_obex_setpath](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6d61b4421ad1e56cc2ae611ec77e561e)
- [bt_obex_setpath_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga13836db790849b5ec6b52bcb97c84505)
- [bt_obex_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga12730d705667c2717c05a75cdfc07281)
- [BT_OBEX_ACTION_COPY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga12730d705667c2717c05a75cdfc07281abb151a8123c7e6826a052ab252455aee)
- [BT_OBEX_ACTION_MOVE_RENAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga12730d705667c2717c05a75cdfc07281a7c57548121adf0afe43066070ef4b1fa)
- [BT_OBEX_ACTION_SET_PERM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gga12730d705667c2717c05a75cdfc07281a711263abb984488b8c7273052fb76ae0)
- [bt_obex_action](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab4b0a3533c7ec044efbee05c852d4f09)
- [bt_obex_action_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gae178bf14d0495ad1e1aa5f7b4d8e1652)
- [bt_obex_add_header_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga14c8efe9c8a99e2736552d59972e7b23)
- [bt_obex_add_header_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga9cd4c8342f67b53a3c3177a51f8887cb)
- [bt_obex_add_header_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gadd9f9b4cb50eb51df05c60705223e53b)
- [bt_obex_add_header_len](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga0d27f09e3b8ea5636f0a34cf8729abaf)
- [bt_obex_add_header_time_iso_8601](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga877d67e0a4135cabf8b5fddab4d014c6)
- [bt_obex_add_header_time](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga249e8b35b98f564d57dc1d644228b8f2)
- [bt_obex_add_header_description](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaedc6f39972a5414d085ce17b09ffd121)
- [bt_obex_add_header_target](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gac778e8ff0ac7e74795b107750a4a6719)
- [bt_obex_add_header_http](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6392da7ce8009eb95ab8c8a4d45fcb40)
- [bt_obex_add_header_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad1b3c22eea0915b962d7ab1e27726fe2)
- [bt_obex_add_header_end_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga805f13b12c7ce23057cb983d7159c36b)
- [bt_obex_add_header_body_or_end_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gadf2d0b93618e0e29341bc21dfd44954f)
- [BT_OBEX_MIN_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6206007c2c3e50d997ae5a644ceae783)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [BT_OBEX_PDU_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga500dcfab79831c5d640406cff8c54f01)
- [ENOMEM](../error_reference/P003_系统错误号公共接口.md#ga6a05c923dad0c1208043e9c20a58c8e5)
- [MIN](../util_reference/P001_通用工具公共接口.md#ga3acffbd305ee72dcd4593c0d8af64a4f)
- [len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [net_buf_tailroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaecbc6adf16469e3366c88445ea7a553a)
- [BT_OBEX_HDR_LEN_OF_HEADER_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5571666538c43d8d71dd17dc58d19f45)
- [BT_OBEX_DATA_LEN_OF_HEADER_BODY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab3db35da4b3daf626e89223262273fb9)
- [bt_obex_add_header_who](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga56690794dc07dfa598ae2ac68bc90aa0)
- [bt_obex_add_header_conn_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gadc92dff93ef2051ff8b3b277a1bc1f17)
- [bt_obex_tlv](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md)
- [type](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md#abb39dc76c06c3dd89a739f3111d143b5)
- [data_len](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md#addcdfe5b297fe7cd9e1f30eee8ade4d7)
- [data](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md#a18d22dae9d1f069d2403398454fadd45)
- [bt_obex_add_header_app_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaeacfe7cb654bf33e7b387358a19fd3d3)
- [bt_obex_add_header_auth_challenge](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacfc897d66e8c14629fa4d94f3782c741)
- [bt_obex_add_header_auth_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5433561f0e9bad6da2d94dccca1578de)
- [bt_obex_add_header_creator_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga14c619eef70addc01d13841eda2d8f89)
- [bt_obex_add_header_wan_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga111cd19449aba6fd0e667551874af0cf)
- [bt_obex_add_header_obj_class](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga7473f42bef1409100886f7812a71a1dc)
- [bt_obex_add_header_session_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gac47ddfe8cfe1e595a1821f32415d14eb)
- [bt_obex_add_header_session_seq_number](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad4a84068ce8c7c37b5189d366b771235)
- [bt_obex_add_header_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga58034dc9ba274030eea5bc3980e2ff95)
- [bt_obex_add_header_dest_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga4463514cf369beb882fec9ab15904821)
- [bt_obex_add_header_perm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga4b7c08fd620fdc1ff28a4714c84b6e30)
- [bt_obex_add_header_srm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga23ed862cc6149a71793d02d89fb98cdc)
- [bt_obex_add_header_srm_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaaa8a9630b0bf5597ca620b864fdafa87)
- [bt_obex_hdr](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md)
- [id](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md#aa453f73fd7a159d92b193dc53c10d995)
- [len](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md#a039bc4f46929c1f9e6c12012fee1e88b)
- [data](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md#ad1f539c20ef8f9e8849326b7d8b64101)
- [bt_obex_header_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5c93e9786adfb45a60a911087f859757)
- [bt_obex_get_header_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga1e9b6dd9a8816ce87235b6b3d723541c)
- [bt_obex_get_header_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gabef4622fa48b493f6d6ad5d1ecb65726)
- [bt_obex_get_header_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gabcfa9b33c0f91fbcf787d58e1f1bba41)
- [bt_obex_get_header_len](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga18ce5303b138959481666c0b8101f59e)
- [bt_obex_get_header_time_iso_8601](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacee063f6b53b85bad52a519cd1c794c5)
- [bt_obex_get_header_time](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga367337d0f002a046248e92f3578efbb6)
- [bt_obex_get_header_description](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3d805f241fc507587445b3204070055e)
- [bt_obex_get_header_target](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga49265f0aec21d8c33f56eb44723dabba)
- [bt_obex_get_header_http](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5a181f7779df1ed2919ba3a94a630df4)
- [bt_obex_get_header_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaba71a8b3b8adc251a5a87fa60848bb3c)
- [bt_obex_get_header_end_body](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaf8ff29ef3413492d2ec67fba278c2f82)
- [bt_obex_get_header_who](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab551b01deed2c5a31f9a7a4b99045c9c)
- [bt_obex_get_header_conn_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga225ac4953da5e56a07865c8ab6ee0591)
- [bt_obex_tlv_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaccecf00dc6209d1701ac0a6985f38257)
- [bt_obex_get_header_app_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga96981ef9187406efbd374fd623a14eaa)
- [bt_obex_get_header_auth_challenge](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga6ee576eecea3947f1832d4859f16e1db)
- [bt_obex_get_header_auth_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gad9bae471db418e0a50c1b234e37b5d9d)
- [bt_obex_get_header_creator_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga9e08bf74bfbf001a80f40ee2d1b1ef82)
- [bt_obex_get_header_wan_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaf9ffc19ef06a2773d664c0b15b2b8857)
- [bt_obex_get_header_obj_class](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga49d1988eae4165f1cec624812cfe5f36)
- [bt_obex_get_header_session_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga560c8f0cb92b769a0716b2bc163c38e1)
- [bt_obex_get_header_session_seq_number](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaaa33502f3ae9f97767bd0e5e660f021f)
- [bt_obex_get_header_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacc1673746737e4163165b5f379c8105f)
- [bt_obex_get_header_dest_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga945c0865edef9f34e2cf1e817a3b45c1)
- [bt_obex_get_header_perm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab234af4e944a3e97e3459613078005a1)
- [bt_obex_get_header_srm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gae0865eea3d8db09023cfc77b2118bad5)
- [bt_obex_get_header_srm_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga7501193240498e7a9da0034b2e434ffc)
- [bt_obex_make_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gafadd6e44ae19786617b5e60608fa4651)
- [bt_obex_string_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga170456d806c0ff494b0c1d7fad763051)
- [bt_obex_has_header](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga296af3d5a15684e4aa3846cc24203fef)
- [bt_obex_has_app_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5ae88dad0e7c97d0f20c7e4ceeeb3ce8)
- [bt_obex_generate_nonce](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3708c17f9c23fdeb5ceda376787cebbd)
- [BT_OBEX_CHALLENGE_TAG_NONCE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaab47709ef621b63172fa54314bf3eff0)
- [bt_obex_calculate_request_digest](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga51baeae9280bb50e34b6608f620498fa)
- [BT_OBEX_RESPONSE_TAG_REQ_DIGEST_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacbae9ed1d18eaab7934258cbfe4fd62a)
- [bt_obex_verify_auth_response](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gae31398502c9d237d7afd47d70315be3f)
- [uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [bt_obex_client_ops::action](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#a1a09c04578beca66cac473fe125747cd)
- [bt_obex_client_ops::disconnect](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#a1e7227232515d875123e6f8ed2bfd993)
- [bt_obex_client_ops::setpath](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#a250940fb4d5b0a2e782645ba7307fd70)
- [bt_obex_client_ops::abort](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#a28ee9ffbbd94c961ef28216ec958d604)
- [bt_obex_client_ops::put](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#a6a5cb209c9fb53786ee51ac4080d7bbc)
- [bt_obex_client_ops::connect](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#ac47ffc1353bef9d4d3725e05b75461f2)
- [bt_obex_client_ops::get](../bluetooth_service_model_reference/P129_bt_obex_client_ops_结构体.md#ae63892d7c4ec6850de4137b466e0fa94)
- [bt_obex_client::obex](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#a271142fde25a5622e25404e3a1f469ad)
- [bt_obex_client::ops](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#a4b9a3f84253936e7babbfc0077da994a)
- [bt_obex_client::tx](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#ac66119d12d329310a666a1b2d7175fce)
- [bt_obex_client::mopl](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#adb6891c7c9682987c12021280e18c8d4)
- [bt_obex_client::rx](../bluetooth_service_model_reference/P128_bt_obex_client_结构体.md#add9c1c75137848fbfbaf65b63ed01e3b)
- [bt_obex_hdr::len](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md#a039bc4f46929c1f9e6c12012fee1e88b)
- [bt_obex_hdr::id](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md#aa453f73fd7a159d92b193dc53c10d995)
- [bt_obex_hdr::data](../bluetooth_service_model_reference/P130_bt_obex_hdr_结构体.md#ad1f539c20ef8f9e8849326b7d8b64101)
- [bt_obex_server_ops::connect](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#a0449e9ab3018796818460f95dd2df13e)
- [bt_obex_server_ops::abort](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#a2763317faa8d5a1371e979d6021ca114)
- [bt_obex_server_ops::get](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#a7380f0fdb31a7f82f75b65a857037987)
- [bt_obex_server_ops::setpath](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#a90839fcaf2bd369d1d5a8c833003f2be)
- [bt_obex_server_ops::action](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#a98b433a269295f3784bce6100aea186a)
- [bt_obex_server_ops::disconnect](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#ab7e99df178911eef8cc8192716a64412)
- [bt_obex_server_ops::put](../bluetooth_service_model_reference/P132_bt_obex_server_ops_结构体.md#ae761cd5aa9728448ee97f306ab9332a6)
- [bt_obex_server::rx](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#a03527bd1e6f2907658756c08e342c283)
- [bt_obex_server::mopl](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#a3aa4c23ecfea67698b6739b670a77aae)
- [bt_obex_server::tx](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#a3ea81fb07df98a2dd9b9bfdb0acfdf62)
- [bt_obex_server::uuid](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#ac3acbf06e1dfa787507bba076be85e14)
- [bt_obex_server::obex](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#ac96bcf45b1753cacb8a797c5f7c29eed)
- [bt_obex_server::ops](../bluetooth_service_model_reference/P131_bt_obex_server_结构体.md#aefe5b0dbed43308a4881643b5705f033)
- [bt_obex_tlv::data](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md#a18d22dae9d1f069d2403398454fadd45)
- [bt_obex_tlv::type](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md#abb39dc76c06c3dd89a739f3111d143b5)
- [bt_obex_tlv::data_len](../bluetooth_service_model_reference/P133_bt_obex_tlv_结构体.md#addcdfe5b297fe7cd9e1f30eee8ade4d7)
- [bt_obex_transport_ops::send](../bluetooth_service_model_reference/P134_bt_obex_transport_ops_结构体.md#a2c04d635154acfa9f4579596d8ed7d79)
- [bt_obex_transport_ops::disconnect](../bluetooth_service_model_reference/P134_bt_obex_transport_ops_结构体.md#a57fc547e578a62e6ebb9da89e0ae423c)
- [bt_obex::tx](../bluetooth_service_model_reference/P127_bt_obex_结构体.md#a9aa32991272416015a9746e7cf8e9027)
- [bt_obex::mtu](../bluetooth_service_model_reference/P127_bt_obex_结构体.md#aa22aa60d3dc3308865508717a4b9c398)
- [bt_obex::rx](../bluetooth_service_model_reference/P127_bt_obex_结构体.md#ac2bc4ebc3b440c1be71c033b7c051c98)
- [net_buf::len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [bt_obex_uuid::uuid](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md#a37e133ae223fc603ea719e37aca12e57)
- [bt_obex_uuid::u16](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md#a70f016148a0f2c7477f7d603f0c70bca)
- [bt_obex_uuid::u32](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md#ac2f5f7bd61988322a3104a36efddb687)
- [bt_obex_uuid::u128](../bluetooth_service_model_reference/P189_bt_obex_uuid_联合体.md#aed352f85b180d4544b7f16d6d3394abe)

---

[上一章](P061_npm2100_vbat.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P063_pinctrl-r8a77951.h_源码浏览.md)
