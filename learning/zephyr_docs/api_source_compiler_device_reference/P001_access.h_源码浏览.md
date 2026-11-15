---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-1
title: access.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_access.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)。

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
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
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
<a id="l00039"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00069"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00083"></a>
<a id="l00087"></a>
<a id="l00091"></a>
<a id="l00095"></a>
<a id="l00099"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="foldopen00132"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="foldopen00163"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="foldopen00182"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="foldopen00230"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="foldopen00258"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="foldopen00290"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="foldopen00317"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="foldopen00354"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="foldopen00372"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="foldopen00410"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="foldopen00424"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="foldopen00439"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="foldopen00483"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="foldopen00530"></a>
<a id="l00530"></a>
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
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="foldopen00592"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="foldopen00604"></a>
<a id="l00604"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="foldopen00623"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="foldopen00635"></a>
<a id="l00635"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00691"></a>
<a id="l00692"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="foldopen00705"></a>
<a id="l00705"></a>
<a id="l00707"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="foldopen00713"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00716"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="foldopen00722"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00761"></a>
<a id="l00762"></a>
<a id="foldopen00764"></a>
<a id="l00764"></a>
<a id="l00771"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="foldopen00826"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="foldopen00868"></a>
<a id="l00868"></a>
<a id="l00869"></a>
<a id="l00870"></a>
<a id="l00871"></a>
<a id="l00872"></a>
<a id="l00884"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00948"></a>
<a id="l00949"></a>
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00965"></a>
<a id="l00966"></a>
<a id="l00974"></a>
<a id="l00975"></a>
<a id="foldopen00977"></a>
<a id="l00977"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="l00984"></a>
<a id="l00985"></a>
<a id="foldopen00987"></a>
<a id="l00987"></a>
<a id="l00989"></a>
<a id="l00991"></a>
<a id="l00993"></a>
<a id="l00995"></a>
<a id="l00997"></a>
<a id="l00998"></a>
<a id="l01000"></a>
<a id="l01002"></a>
<a id="l01004"></a>
<a id="l01006"></a>
<a id="l01007"></a>
<a id="l01008"></a>
<a id="foldopen01010"></a>
<a id="l01010"></a>
<a id="l01012"></a>
<a id="l01014"></a>
<a id="l01015"></a>
<a id="l01016"></a>
<a id="l01029"></a>
<a id="l01030"></a>
<a id="l01031"></a>
<a id="l01032"></a>
<a id="l01033"></a>
<a id="l01034"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="aassigned__numbers_8h_html"></a>
<a id="agroup__bt__mesh__access_html_ga03ce9f6f9ccf734ea72beede09288923"></a>
<a id="agroup__bt__mesh__access_html_ga06644f8a5fa43351328d3f3403dbad03"></a>
<a id="agroup__bt__mesh__access_html_ga10603a5846210a397f306b227ce10c2e"></a>
<a id="agroup__bt__mesh__access_html_ga13986422dda5edce4f5fb1ce387093e3"></a>
<a id="agroup__bt__mesh__access_html_ga1b961d45f8b7c231c698ca229115e434"></a>
<a id="agroup__bt__mesh__access_html_ga26ac86bdd32d27e0091735d98670687a"></a>
<a id="agroup__bt__mesh__access_html_ga762896dd2e806b5be061b220d53ce4db"></a>
<a id="agroup__bt__mesh__access_html_ga7cac052ef76f4b37a95343329b078e77"></a>
<a id="agroup__bt__mesh__access_html_ga8445c550a47dba16e3fa6fea36d6d9fc"></a>
<a id="agroup__bt__mesh__access_html_ga8575f680e77d86d6c85cac27985b9f3c"></a>
<a id="agroup__bt__mesh__access_html_ga8edba04af103fb11994d4d3e558ec4fb"></a>
<a id="agroup__bt__mesh__access_html_gaa8694fdab3f514d8051dad1cc7362ac9"></a>
<a id="agroup__bt__mesh__access_html_gadfb473db4b23902a192e12d322ff1fd2"></a>
<a id="agroup__bt__mesh__access_html_gadff0895c5c34928d778fa615512b3d85"></a>
<a id="agroup__bt__mesh__access_html_gaf0510f9511d72f1d4fd07f865753a50a"></a>
<a id="agroup__bt__mesh__access_html_gaf6356f715c8968151b8d539f2dd1880c"></a>
<a id="agroup__settings_html_ga51cdac276c1fb8cd27fc3eec42749a04"></a>
<a id="ainclude_2zephyr_2settings_2settings_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="amsg_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__comp2__record_html"></a>
<a id="astructbt__mesh__comp2__record_html_a19ce94025c1c8079ca2789bbcd09b00e"></a>
<a id="astructbt__mesh__comp2__record_html_a26370a5dc68af03424c0f2f4fecd0181"></a>
<a id="astructbt__mesh__comp2__record_html_a4970a0757c34ab97697c69728b564df6"></a>
<a id="astructbt__mesh__comp2__record_html_a5f25c33170c77375f6492ad3cc0feaac"></a>
<a id="astructbt__mesh__comp2__record_html_a6f81d99a62252cd26d87ca4fb289bdf9"></a>
<a id="astructbt__mesh__comp2__record_html_abdc488e846233fa05f0fc48f4081576e"></a>
<a id="astructbt__mesh__comp2__record_html_ac3cabce01490191f145234f386b9b119"></a>
<a id="astructbt__mesh__comp2__record_html_acd5f5770a6606ad00fa0815e4866ec4e"></a>
<a id="astructbt__mesh__comp2__record_html_ad13066e9d6d32e8e2eab64881249eb7e"></a>
<a id="astructbt__mesh__comp2_html"></a>
<a id="astructbt__mesh__comp2_html_a9f3425cd64cc487e9a49b85bb0f2159b"></a>
<a id="astructbt__mesh__comp2_html_adf022ca0738626832d566fd6a5a1d889"></a>
<a id="astructbt__mesh__comp_html"></a>
<a id="astructbt__mesh__comp_html_a54031f4c3683a7209e8f7441c5875788"></a>
<a id="astructbt__mesh__comp_html_a648f695898305ef9e6f4f9db42dd8cf9"></a>
<a id="astructbt__mesh__comp_html_a7e4351e81e4e04bb9681e76d384f2fa5"></a>
<a id="astructbt__mesh__comp_html_ad3da0629db1cb423260aa202cab7f062"></a>
<a id="astructbt__mesh__comp_html_aff69499c7ac2c1ba643c946c75aa21ce"></a>
<a id="astructbt__mesh__elem_1_1bt__mesh__elem__rt__ctx_html"></a>
<a id="astructbt__mesh__elem_1_1bt__mesh__elem__rt__ctx_html_a659279b38f1f3e015ebc648901577038"></a>
<a id="astructbt__mesh__elem_html"></a>
<a id="astructbt__mesh__elem_html_a2090fa7827eb6a7b8bd1adfb831439cb"></a>
<a id="astructbt__mesh__elem_html_a57fefe57d9425d6666495d1f72a3f132"></a>
<a id="astructbt__mesh__elem_html_a5f4c8ded34cf56c7f60189584e8e5b46"></a>
<a id="astructbt__mesh__elem_html_a648273e844ff9fa71578372e764ca8cf"></a>
<a id="astructbt__mesh__elem_html_a81d4fc1c41e2944bf7f6e71b00e19a0f"></a>
<a id="astructbt__mesh__elem_html_aea56fd98c9aecfb9de3772ad3f14b25e"></a>
<a id="astructbt__mesh__mod__id__vnd_html"></a>
<a id="astructbt__mesh__mod__id__vnd_html_a187a919337c92f54eaba6f932c7a3670"></a>
<a id="astructbt__mesh__mod__id__vnd_html_a1a299852544a5e6fa3c34ac5ffd883d8"></a>
<a id="astructbt__mesh__model_1_1bt__mesh__model__rt__ctx_html"></a>
<a id="astructbt__mesh__model_1_1bt__mesh__model__rt__ctx_html_a434ae02cff38c614ef340a3c17f30e9b"></a>
<a id="astructbt__mesh__model_1_1bt__mesh__model__rt__ctx_html_a718d3be40e7be83a196634054d18d568"></a>
<a id="astructbt__mesh__model_1_1bt__mesh__model__rt__ctx_html_a79351fd25ad2ebd1f08ef1748d21dabd"></a>
<a id="astructbt__mesh__model_1_1bt__mesh__model__rt__ctx_html_ab584da43197ad7afe8c9ae807ce69f7e"></a>
<a id="astructbt__mesh__model_1_1bt__mesh__model__rt__ctx_html_aca9b558516b929a0b88d8171027e7c71"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__cb_html_a1688a2c6d7b3b17ba49a0975b6f4f68e"></a>
<a id="astructbt__mesh__model__cb_html_a21fc24829c6933a035b0f0be1a1f58e5"></a>
<a id="astructbt__mesh__model__cb_html_a3a7ad466120085c55bcffacb15c78518"></a>
<a id="astructbt__mesh__model__cb_html_a8333420fb9d1d98799ae03ba3b23bfe4"></a>
<a id="astructbt__mesh__model__cb_html_ae28f875dffc7f5f2ce99abe590369f43"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model__op_html_a09c18a889e08bc708b9dc623f8177e39"></a>
<a id="astructbt__mesh__model__op_html_a25445fe2e937a321942c312bd675e486"></a>
<a id="astructbt__mesh__model__op_html_a4a5de7a12f2f8743048aafc81af0cece"></a>
<a id="astructbt__mesh__model__pub_html"></a>
<a id="astructbt__mesh__model__pub_html_a0354344e08e633dc4d6c0b4e7b169080"></a>
<a id="astructbt__mesh__model__pub_html_a0ad1809fe74930c9b36b32516a8d146f"></a>
<a id="astructbt__mesh__model__pub_html_a16c13e46c012ab836acd02b8fe5f05e3"></a>
<a id="astructbt__mesh__model__pub_html_a23a865dbd2dce5c1af074097864611e9"></a>
<a id="astructbt__mesh__model__pub_html_a3617adb0c1192419bdac2ad0f37199ac"></a>
<a id="astructbt__mesh__model__pub_html_a3d93d44ff85243dc94e7b4d36cde5b97"></a>
<a id="astructbt__mesh__model__pub_html_a408c9185168b962f7e7314f9a429fe8c"></a>
<a id="astructbt__mesh__model__pub_html_a4e211c851bf91a9b43f035d435e9c93c"></a>
<a id="astructbt__mesh__model__pub_html_a4f2ce8727ffb44f564d1dc0615ebcadf"></a>
<a id="astructbt__mesh__model__pub_html_a5f5639c01d3704ec3d527c418d35f827"></a>
<a id="astructbt__mesh__model__pub_html_a820b713aaa1e0c33a4a59c80f805e854"></a>
<a id="astructbt__mesh__model__pub_html_aa5026299082b3013740c7e36c01f91f5"></a>
<a id="astructbt__mesh__model__pub_html_ab6e00714ea899eb32873d10b0908d278"></a>
<a id="astructbt__mesh__model__pub_html_ab704aedcfd06d374615ef18c6ecc84a9"></a>
<a id="astructbt__mesh__model__pub_html_abdbdc3bbc5d4ac5a5d606b55bb2d50ee"></a>
<a id="astructbt__mesh__model__pub_html_abea9c2085c9d2e1e2fc71f03dd323ee7"></a>
<a id="astructbt__mesh__model__pub_html_ae550510e9ca45f8c9fd9802e4e7e0f3d"></a>
<a id="astructbt__mesh__model__pub_html_af3771432d13805710e94f013332e8214"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__model_html_a274c811c22b764908599127b128ce584"></a>
<a id="astructbt__mesh__model_html_a3372deccde1a5ab26d9204c97339596e"></a>
<a id="astructbt__mesh__model_html_a3980e6f8100151cb3339792821fa7858"></a>
<a id="astructbt__mesh__model_html_a460ab46730afa4f74e4066f787864b0b"></a>
<a id="astructbt__mesh__model_html_a4acc656c737cf79161414984312100b6"></a>
<a id="astructbt__mesh__model_html_a63595a0559ca70ca76c996f0b71c7983"></a>
<a id="astructbt__mesh__model_html_a67a91d64051e055b79f5d9166ab12660"></a>
<a id="astructbt__mesh__model_html_a79b8fd44ced901c3478f0e04d7dadfcd"></a>
<a id="astructbt__mesh__model_html_a848ccf09f7b75ff8a48acb6c8088cf2a"></a>
<a id="astructbt__mesh__model_html_adf3e3f0dab9838cc76361949b237bb9e"></a>
<a id="astructbt__mesh__model_html_af4a1b5e837b3a1266c7f61ee21020c0b"></a>
<a id="astructbt__mesh__model_html_af5b948709773e5388c30d457ec2a9559"></a>
<a id="astructbt__mesh__models__metadata__entry_html"></a>
<a id="astructbt__mesh__models__metadata__entry_html_a39959b1f46e1b21eb78dbe3293f29149"></a>
<a id="astructbt__mesh__models__metadata__entry_html_adb5aaf010cae636c0b60a88f38d36fac"></a>
<a id="astructbt__mesh__models__metadata__entry_html_ae343d6ca709e1aceafc25d64cdf3916d"></a>
<a id="astructbt__mesh__msg__ctx_html"></a>
<a id="astructbt__mesh__send__cb_html"></a>
<a id="astructbt__mesh__send__cb_html_a2f84ef4cb2d28729cd98b844a3d25f55"></a>
<a id="astructbt__mesh__send__cb_html_aa169dbec8c96fd41a35616c009604685"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="asys_2util_8h_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_ACCESS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_ACCESS_H_

#include <zephyr/sys/util.h>
#include <zephyr/settings/settings.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/mesh/msg.h>


/* Internal macros used to initialize array members */
#define BT_MESH_KEY_UNUSED_ELT_(IDX, _) BT_MESH_KEY_UNUSED
#define BT_MESH_ADDR_UNASSIGNED_ELT_(IDX, _) BT_MESH_ADDR_UNASSIGNED
#define BT_MESH_UUID_UNASSIGNED_ELT_(IDX, _) NULL
#define BT_MESH_MODEL_KEYS_UNUSED(_keys)                        \
        { LISTIFY(_keys, BT_MESH_KEY_UNUSED_ELT_, (,)) }
#define BT_MESH_MODEL_GROUPS_UNASSIGNED(_grps)                  \
        { LISTIFY(_grps, BT_MESH_ADDR_UNASSIGNED_ELT_, (,)) }
#if CONFIG_BT_MESH_LABEL_COUNT > 0
#define BT_MESH_MODEL_UUIDS_UNASSIGNED()                        \
        .uuids = (const uint8_t *[]){ LISTIFY(CONFIG_BT_MESH_LABEL_COUNT, \
                                     BT_MESH_UUID_UNASSIGNED_ELT_, (,)) },
#else
#define BT_MESH_MODEL_UUIDS_UNASSIGNED()
#endif


#define BT_MESH_MODEL_RUNTIME_INIT(_user_data)                  \
        .rt = &(struct bt_mesh_model_rt_ctx){ .user_data = (_user_data) },


#ifdef __cplusplus
extern "C" {
#endif

#define BT_MESH_ADDR_UNASSIGNED    0x0000
#define BT_MESH_ADDR_ALL_NODES     0xffff
#define BT_MESH_ADDR_RELAYS        0xfffe
#define BT_MESH_ADDR_FRIENDS       0xfffd
#define BT_MESH_ADDR_PROXIES       0xfffc
#define BT_MESH_ADDR_DFW_NODES     0xfffb
#define BT_MESH_ADDR_IP_NODES      0xfffa
#define BT_MESH_ADDR_IP_BR_ROUTERS 0xfff9

#define BT_MESH_KEY_UNUSED        0xffff
#define BT_MESH_KEY_ANY           0xffff
#define BT_MESH_KEY_DEV           0xfffe
#define BT_MESH_KEY_DEV_LOCAL     BT_MESH_KEY_DEV
#define BT_MESH_KEY_DEV_REMOTE    0xfffd
#define BT_MESH_KEY_DEV_ANY       0xfffc

#define BT_MESH_ADDR_IS_UNICAST(addr) ((addr) && (addr) < 0x8000)
#define BT_MESH_ADDR_IS_GROUP(addr) ((addr) >= 0xc000 && (addr) < 0xff00)
#define BT_MESH_ADDR_IS_FIXED_GROUP(addr) ((addr) >= 0xff00 && (addr) < 0xffff)
#define BT_MESH_ADDR_IS_VIRTUAL(addr) ((addr) >= 0x8000 && (addr) < 0xc000)
#define BT_MESH_ADDR_IS_RFU(addr) ((addr) >= 0xff00 && (addr) <= 0xfff8)

#define BT_MESH_IS_DEV_KEY(key) (key == BT_MESH_KEY_DEV_LOCAL || \
                                 key == BT_MESH_KEY_DEV_REMOTE)

#define BT_MESH_APP_SEG_SDU_MAX   12

#define BT_MESH_APP_UNSEG_SDU_MAX 15

#if defined(CONFIG_BT_MESH_RX_SEG_MAX)
#define BT_MESH_RX_SEG_MAX CONFIG_BT_MESH_RX_SEG_MAX
#else
#define BT_MESH_RX_SEG_MAX 0
#endif

#if defined(CONFIG_BT_MESH_TX_SEG_MAX)
#define BT_MESH_TX_SEG_MAX CONFIG_BT_MESH_TX_SEG_MAX
#else
#define BT_MESH_TX_SEG_MAX 0
#endif

#define BT_MESH_TX_SDU_MAX        MAX((BT_MESH_TX_SEG_MAX *             \
                                       BT_MESH_APP_SEG_SDU_MAX),        \
                                      BT_MESH_APP_UNSEG_SDU_MAX)

#define BT_MESH_RX_SDU_MAX        MAX((BT_MESH_RX_SEG_MAX *             \
                                       BT_MESH_APP_SEG_SDU_MAX),        \
                                      BT_MESH_APP_UNSEG_SDU_MAX)

#define BT_MESH_ELEM(_loc, _mods, _vnd_mods)                            \
{                                                                       \
        .rt               = &(struct bt_mesh_elem_rt_ctx) { 0 },        \
        .loc              = (_loc),                                     \
        .model_count      = ARRAY_SIZE(_mods),                          \
        .vnd_model_count  = ARRAY_SIZE(_vnd_mods),                      \
        .models           = (_mods),                                    \
        .vnd_models       = (_vnd_mods),                                \
}

struct bt_mesh_elem {
        struct bt_mesh_elem_rt_ctx {
                uint16_t addr;
        } * const rt;

        const uint16_t loc;
        const uint8_t model_count;
        const uint8_t vnd_model_count;

        const struct bt_mesh_model * const models;
        const struct bt_mesh_model * const vnd_models;
};

struct bt_mesh_model_op {
        const uint32_t  opcode;

        const ssize_t len;

        int (*const func)(const struct bt_mesh_model *model,
                          struct bt_mesh_msg_ctx *ctx,
                          struct net_buf_simple *buf);
};

#define BT_MESH_MODEL_OP_1(b0) (b0)
#define BT_MESH_MODEL_OP_2(b0, b1) (((b0) << 8) | (b1))
#define BT_MESH_MODEL_OP_3(b0, cid) ((((b0) << 16) | 0xc00000) | (cid))

#define BT_MESH_LEN_EXACT(len) (-len)
#define BT_MESH_LEN_MIN(len) (len)

#define BT_MESH_MODEL_OP_END { 0, 0, NULL }

#if !defined(__cplusplus) || defined(__DOXYGEN__)
#define BT_MESH_MODEL_NO_OPS ((struct bt_mesh_model_op []) \
                              { BT_MESH_MODEL_OP_END })

#define BT_MESH_MODEL_NONE ((const struct bt_mesh_model []){})

#define BT_MESH_MODEL_CNT_CB(_id, _op, _pub, _user_data, _keys, _grps, _cb)     \
{                                                                               \
        .id = (_id),                                                            \
        BT_MESH_MODEL_RUNTIME_INIT(_user_data)                                  \
        .pub = _pub,                                                            \
        .keys = (uint16_t []) BT_MESH_MODEL_KEYS_UNUSED(_keys),                 \
        .keys_cnt = _keys,                                                      \
        .groups = (uint16_t []) BT_MESH_MODEL_GROUPS_UNASSIGNED(_grps),         \
        .groups_cnt = _grps,                                                    \
        BT_MESH_MODEL_UUIDS_UNASSIGNED()                                        \
        .op = _op,                                                              \
        .cb = _cb,                                                              \
}

#define BT_MESH_MODEL_CNT_VND_CB(_company, _id, _op, _pub, _user_data, _keys, _grps, _cb)       \
{                                                                                               \
        .vnd.company = (_company),                                                              \
        .vnd.id = (_id),                                                                        \
        BT_MESH_MODEL_RUNTIME_INIT(_user_data)                                                  \
        .op = _op,                                                                              \
        .pub = _pub,                                                                            \
        .keys = (uint16_t []) BT_MESH_MODEL_KEYS_UNUSED(_keys),                                 \
        .keys_cnt = _keys,                                                                      \
        .groups = (uint16_t []) BT_MESH_MODEL_GROUPS_UNASSIGNED(_grps),                         \
        .groups_cnt = _grps,                                                                    \
        BT_MESH_MODEL_UUIDS_UNASSIGNED()                                                        \
        .cb = _cb,                                                                              \
}

#define BT_MESH_MODEL_CB(_id, _op, _pub, _user_data, _cb)       \
        BT_MESH_MODEL_CNT_CB(_id, _op, _pub, _user_data,        \
                             CONFIG_BT_MESH_MODEL_KEY_COUNT,    \
                             CONFIG_BT_MESH_MODEL_GROUP_COUNT, _cb)


#if defined(CONFIG_BT_MESH_LARGE_COMP_DATA_SRV)
#define BT_MESH_MODEL_METADATA_CB(_id, _op, _pub, _user_data, _cb, _metadata)                    \
{                                                                            \
        .id = (_id),                                                         \
        BT_MESH_MODEL_RUNTIME_INIT(_user_data)                               \
        .pub = _pub,                                                         \
        .keys = (uint16_t []) BT_MESH_MODEL_KEYS_UNUSED(CONFIG_BT_MESH_MODEL_KEY_COUNT), \
        .keys_cnt = CONFIG_BT_MESH_MODEL_KEY_COUNT,                          \
        .groups = (uint16_t []) BT_MESH_MODEL_GROUPS_UNASSIGNED(CONFIG_BT_MESH_MODEL_GROUP_COUNT), \
        .groups_cnt = CONFIG_BT_MESH_MODEL_GROUP_COUNT,                      \
        BT_MESH_MODEL_UUIDS_UNASSIGNED()                                     \
        .op = _op,                                                           \
        .cb = _cb,                                                           \
        .metadata = _metadata,                                               \
}
#else
#define BT_MESH_MODEL_METADATA_CB(_id, _op, _pub, _user_data, _cb, _metadata)  \
        BT_MESH_MODEL_CB(_id, _op, _pub, _user_data, _cb)
#endif

#define BT_MESH_MODEL_VND_CB(_company, _id, _op, _pub, _user_data, _cb) \
        BT_MESH_MODEL_CNT_VND_CB(_company, _id, _op, _pub, _user_data,  \
                                 CONFIG_BT_MESH_MODEL_KEY_COUNT,        \
                                 CONFIG_BT_MESH_MODEL_GROUP_COUNT, _cb)

#if defined(CONFIG_BT_MESH_LARGE_COMP_DATA_SRV)
#define BT_MESH_MODEL_VND_METADATA_CB(_company, _id, _op, _pub, _user_data, _cb, _metadata)      \
{                                                                            \
        .vnd.company = (_company),                                           \
        .vnd.id = (_id),                                                     \
        BT_MESH_MODEL_RUNTIME_INIT(_user_data)                               \
        .op = _op,                                                           \
        .pub = _pub,                                                         \
        .keys = (uint16_t []) BT_MESH_MODEL_KEYS_UNUSED(CONFIG_BT_MESH_MODEL_KEY_COUNT), \
        .keys_cnt = CONFIG_BT_MESH_MODEL_KEY_COUNT,                          \
        .groups = (uint16_t []) BT_MESH_MODEL_GROUPS_UNASSIGNED(CONFIG_BT_MESH_MODEL_GROUP_COUNT), \
        .groups_cnt = CONFIG_BT_MESH_MODEL_GROUP_COUNT,                      \
        BT_MESH_MODEL_UUIDS_UNASSIGNED()                                     \
        .cb = _cb,                                                           \
        .metadata = _metadata,                                               \
}
#else
#define BT_MESH_MODEL_VND_METADATA_CB(_company, _id, _op, _pub, _user_data, _cb, _metadata)      \
        BT_MESH_MODEL_VND_CB(_company, _id, _op, _pub, _user_data, _cb)
#endif
#define BT_MESH_MODEL(_id, _op, _pub, _user_data)                              \
        BT_MESH_MODEL_CB(_id, _op, _pub, _user_data, NULL)

#define BT_MESH_MODEL_VND(_company, _id, _op, _pub, _user_data)                \
        BT_MESH_MODEL_VND_CB(_company, _id, _op, _pub, _user_data, NULL)
#endif /* !defined(__cplusplus) || defined(__DOXYGEN__) */

#define BT_MESH_TRANSMIT(count, int_ms) ((uint8_t)((count) | (((int_ms / 10) - 1) << 3)))

#define BT_MESH_TRANSMIT_COUNT(transmit) (((transmit) & (uint8_t)BIT_MASK(3)))

#define BT_MESH_TRANSMIT_INT(transmit) ((((transmit) >> 3) + 1) * 10)

#define BT_MESH_PUB_TRANSMIT(count, int_ms) BT_MESH_TRANSMIT(count,           \
                                                             (int_ms) / 5)

#define BT_MESH_PUB_TRANSMIT_COUNT(transmit) BT_MESH_TRANSMIT_COUNT(transmit)

#define BT_MESH_PUB_TRANSMIT_INT(transmit) ((((transmit) >> 3) + 1) * 50)

#define BT_MESH_PUB_MSG_TOTAL(pub) (BT_MESH_PUB_TRANSMIT_COUNT((pub)->retransmit) + 1)

#define BT_MESH_PUB_MSG_NUM(pub) (BT_MESH_PUB_TRANSMIT_COUNT((pub)->retransmit) + 1 - (pub)->count)

struct bt_mesh_model_pub {
        const struct bt_mesh_model *mod;

        uint16_t addr;
        const uint8_t *uuid;
        uint16_t key:12,
                 cred:1,
                 send_rel:1,
                 fast_period:1,
                 retr_update:1;

        uint8_t  ttl;
        uint8_t  retransmit;
        uint8_t  period;
        uint8_t  period_div:4,
                 count:4;

        uint8_t delayable:1;

        uint32_t period_start;

        struct net_buf_simple *msg;

        int (*update)(const struct bt_mesh_model *mod);

        struct k_work_delayable timer;
};

#define BT_MESH_MODEL_PUB_DEFINE(_name, _update, _msg_len) \
        NET_BUF_SIMPLE_DEFINE_STATIC(bt_mesh_pub_msg_##_name, _msg_len); \
        static struct bt_mesh_model_pub _name = { \
                .msg = &bt_mesh_pub_msg_##_name, \
                .update = _update, \
        }

struct bt_mesh_models_metadata_entry {
        const uint16_t len;

        const uint16_t id;

        const void * const data;
};

#define BT_MESH_MODELS_METADATA_ENTRY(_len, _id, _data)                         \
        {                                                                      \
                .len = (_len), .id = _id, .data = _data,                       \
        }

#define BT_MESH_MODELS_METADATA_NONE NULL

#define BT_MESH_MODELS_METADATA_END { 0, 0, NULL }

struct bt_mesh_model_cb {
        int (*const settings_set)(const struct bt_mesh_model *model,
                                  const char *name, size_t len_rd,
                                  settings_read_cb read_cb, void *cb_arg);

        int (*const start)(const struct bt_mesh_model *model);

        int (*const init)(const struct bt_mesh_model *model);

        void (*const reset)(const struct bt_mesh_model *model);

        void (*const pending_store)(const struct bt_mesh_model *model);
};

struct bt_mesh_mod_id_vnd {
        uint16_t company;
        uint16_t id;
};

struct bt_mesh_model {
        union {
                const uint16_t id;
                const struct bt_mesh_mod_id_vnd vnd;
        };

        /* Model runtime information */
        struct bt_mesh_model_rt_ctx {
                uint8_t  elem_idx;   /* Belongs to Nth element */
                uint8_t  mod_idx;    /* Is the Nth model in the element */
                uint16_t flags;      /* Model flags for internal bookkeeping */

#ifdef CONFIG_BT_MESH_MODEL_EXTENSIONS
                /* Pointer to the next model in a model extension list. */
                const struct bt_mesh_model *next;
#endif
                void *user_data;
        } * const rt;

        struct bt_mesh_model_pub * const pub;

        uint16_t * const keys;
        const uint16_t keys_cnt;

        uint16_t * const groups;
        const uint16_t groups_cnt;

#if (CONFIG_BT_MESH_LABEL_COUNT > 0) || defined(__DOXYGEN__)
        const uint8_t ** const uuids;
#endif

        const struct bt_mesh_model_op * const op;

        const struct bt_mesh_model_cb * const cb;

#if defined(CONFIG_BT_MESH_LARGE_COMP_DATA_SRV) || defined(__DOXYGEN__)
        /* Pointer to the array of model metadata entries. */
        const struct bt_mesh_models_metadata_entry * const metadata;
#endif
};

struct bt_mesh_send_cb {
        void (*start)(uint16_t duration, int err, void *cb_data);
        void (*end)(int err, void *cb_data);
};


#define BT_MESH_TTL_DEFAULT 0xff

#define BT_MESH_TTL_MAX     0x7f

int bt_mesh_model_send(const struct bt_mesh_model *model,
                       struct bt_mesh_msg_ctx *ctx,
                       struct net_buf_simple *msg,
                       const struct bt_mesh_send_cb *cb,
                       void *cb_data);

int bt_mesh_model_publish(const struct bt_mesh_model *model);

static inline bool bt_mesh_model_pub_is_retransmission(const struct bt_mesh_model *model)
{
        return model->pub->count != BT_MESH_PUB_TRANSMIT_COUNT(model->pub->retransmit);
}

const struct bt_mesh_elem *bt_mesh_model_elem(const struct bt_mesh_model *mod);

const struct bt_mesh_model *bt_mesh_model_find(const struct bt_mesh_elem *elem,
                                               uint16_t id);

const struct bt_mesh_model *bt_mesh_model_find_vnd(const struct bt_mesh_elem *elem,
                                                   uint16_t company, uint16_t id);

static inline bool bt_mesh_model_in_primary(const struct bt_mesh_model *mod)
{
        return (mod->rt->elem_idx == 0);
}

int bt_mesh_model_data_store(const struct bt_mesh_model *mod, bool vnd,
                             const char *name, const void *data,
                             size_t data_len);

void bt_mesh_model_data_store_schedule(const struct bt_mesh_model *mod);

int bt_mesh_model_extend(const struct bt_mesh_model *extending_mod,
                         const struct bt_mesh_model *base_mod);


int bt_mesh_model_correspond(const struct bt_mesh_model *corresponding_mod,
                             const struct bt_mesh_model *base_mod);

bool bt_mesh_model_is_extended(const struct bt_mesh_model *model);

int bt_mesh_comp_change_prepare(void);

int bt_mesh_models_metadata_change_prepare(void);

struct bt_mesh_comp {
        uint16_t cid;
        uint16_t pid;
        uint16_t vid;

        size_t elem_count;
        const struct bt_mesh_elem *elem;
};

struct bt_mesh_comp2_record {
        uint16_t id;
        struct {
                uint8_t x;
                uint8_t y;
                uint8_t z;
        } version;
        uint8_t elem_offset_cnt;
        const uint8_t *elem_offset;
        uint16_t data_len;
        const void *data;
};

struct bt_mesh_comp2 {
        size_t record_cnt;
        const struct bt_mesh_comp2_record *record;
};

int bt_mesh_comp2_register(const struct bt_mesh_comp2 *comp2);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_ACCESS_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 22 行

用于初始化数组成员（array members）的内部宏。

### 注释 3：原第 441 行

条件表达式：`!defined(__cplusplus) || defined(__DOXYGEN__)`。

### 注释 4：原第 721 行

模型运行时信息（model runtime information）。

### 注释 5：原第 723 行

属于第 N 个元素（element）。

### 注释 6：原第 724 行

是该元素中的第 N 个模型（model）。

### 注释 7：原第 725 行

用于内部记账管理（bookkeeping）的模型标志。

### 注释 8：原第 728 行

指向模型扩展列表（model extension list）中下一个模型的指针。

### 注释 9：原第 758 行

指向模型元数据条目（model metadata entries）数组的指针。

### 注释 10：原第 1039 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_ACCESS_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/settings/settings.h](../storage/P076_设置子系统头文件.md)
- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [zephyr/bluetooth/mesh/msg.h](https://docs.zephyrproject.org/latest/doxygen/html/msg_8h.html)
- [bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)
- [bt_mesh_elem_rt_ctx](../bluetooth_mesh_model_reference/P060_bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [addr](../bluetooth_mesh_model_reference/P060_bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体.md#a659279b38f1f3e015ebc648901577038)
- [rt](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#a2090fa7827eb6a7b8bd1adfb831439cb)
- [loc](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#a5f4c8ded34cf56c7f60189584e8e5b46)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [model_count](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#a648273e844ff9fa71578372e764ca8cf)
- [vnd_model_count](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#aea56fd98c9aecfb9de3772ad3f14b25e)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [models](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#a57fefe57d9425d6666495d1f72a3f132)
- [vnd_models](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#a81d4fc1c41e2944bf7f6e71b00e19a0f)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [opcode](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md#a09c18a889e08bc708b9dc623f8177e39)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [len](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md#a25445fe2e937a321942c312bd675e486)
- [func](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md#a4a5de7a12f2f8743048aafc81af0cece)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mesh_model_pub](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md)
- [mod](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#aa5026299082b3013740c7e36c01f91f5)
- [addr](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a408c9185168b962f7e7314f9a429fe8c)
- [uuid](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#abea9c2085c9d2e1e2fc71f03dd323ee7)
- [key](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a0ad1809fe74930c9b36b32516a8d146f)
- [cred](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a3617adb0c1192419bdac2ad0f37199ac)
- [send_rel](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#ab704aedcfd06d374615ef18c6ecc84a9)
- [fast_period](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#abdbdc3bbc5d4ac5a5d606b55bb2d50ee)
- [retr_update](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a16c13e46c012ab836acd02b8fe5f05e3)
- [ttl](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a820b713aaa1e0c33a4a59c80f805e854)
- [retransmit](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a3d93d44ff85243dc94e7b4d36cde5b97)
- [period](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#ae550510e9ca45f8c9fd9802e4e7e0f3d)
- [period_div](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a4f2ce8727ffb44f564d1dc0615ebcadf)
- [count](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a4e211c851bf91a9b43f035d435e9c93c)
- [delayable](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a23a865dbd2dce5c1af074097864611e9)
- [period_start](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#ab6e00714ea899eb32873d10b0908d278)
- [msg](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a5f5639c01d3704ec3d527c418d35f827)
- [update](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a0354344e08e633dc4d6c0b4e7b169080)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [timer](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#af3771432d13805710e94f013332e8214)
- [bt_mesh_models_metadata_entry](../bluetooth_mesh_model_reference/P080_bt_mesh_models_metadata_entry_结构体.md)
- [len](../bluetooth_mesh_model_reference/P080_bt_mesh_models_metadata_entry_结构体.md#a39959b1f46e1b21eb78dbe3293f29149)
- [id](../bluetooth_mesh_model_reference/P080_bt_mesh_models_metadata_entry_结构体.md#ae343d6ca709e1aceafc25d64cdf3916d)
- [data](../bluetooth_mesh_model_reference/P080_bt_mesh_models_metadata_entry_结构体.md#adb5aaf010cae636c0b60a88f38d36fac)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [settings_set](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#a21fc24829c6933a035b0f0be1a1f58e5)
- [settings_read_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga51cdac276c1fb8cd27fc3eec42749a04)
- [start](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#a8333420fb9d1d98799ae03ba3b23bfe4)
- [init](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#a1688a2c6d7b3b17ba49a0975b6f4f68e)
- [reset](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#a3a7ad466120085c55bcffacb15c78518)
- [pending_store](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#ae28f875dffc7f5f2ce99abe590369f43)
- [bt_mesh_mod_id_vnd](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md)
- [company](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md#a187a919337c92f54eaba6f932c7a3670)
- [id](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md#a1a299852544a5e6fa3c34ac5ffd883d8)
- [id](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a848ccf09f7b75ff8a48acb6c8088cf2a)
- [vnd](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a3372deccde1a5ab26d9204c97339596e)
- [bt_mesh_model_rt_ctx](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md)
- [elem_idx](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md#aca9b558516b929a0b88d8171027e7c71)
- [mod_idx](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md#a79351fd25ad2ebd1f08ef1748d21dabd)
- [flags](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md#ab584da43197ad7afe8c9ae807ce69f7e)
- [next](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md#a434ae02cff38c614ef340a3c17f30e9b)
- [user_data](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md#a718d3be40e7be83a196634054d18d568)
- [rt](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a3980e6f8100151cb3339792821fa7858)
- [pub](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#af4a1b5e837b3a1266c7f61ee21020c0b)
- [keys](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a63595a0559ca70ca76c996f0b71c7983)
- [keys_cnt](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a79b8fd44ced901c3478f0e04d7dadfcd)
- [groups](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a460ab46730afa4f74e4066f787864b0b)
- [groups_cnt](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#adf3e3f0dab9838cc76361949b237bb9e)
- [uuids](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a274c811c22b764908599127b128ce584)
- [op](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a4acc656c737cf79161414984312100b6)
- [cb](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a67a91d64051e055b79f5d9166ab12660)
- [metadata](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#af5b948709773e5388c30d457ec2a9559)
- [bt_mesh_send_cb](../bluetooth_mesh_model_reference/P099_bt_mesh_send_cb_结构体.md)
- [start](../bluetooth_mesh_model_reference/P099_bt_mesh_send_cb_结构体.md#a2f84ef4cb2d28729cd98b844a3d25f55)
- [end](../bluetooth_mesh_model_reference/P099_bt_mesh_send_cb_结构体.md#aa169dbec8c96fd41a35616c009604685)
- [bt_mesh_model_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga7cac052ef76f4b37a95343329b078e77)
- [bt_mesh_model_publish](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga06644f8a5fa43351328d3f3403dbad03)
- [bt_mesh_model_pub_is_retransmission](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga1b961d45f8b7c231c698ca229115e434)
- [BT_MESH_PUB_TRANSMIT_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga13986422dda5edce4f5fb1ce387093e3)
- [bt_mesh_model_elem](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8edba04af103fb11994d4d3e558ec4fb)
- [bt_mesh_model_find](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf0510f9511d72f1d4fd07f865753a50a)
- [bt_mesh_model_find_vnd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gadfb473db4b23902a192e12d322ff1fd2)
- [bt_mesh_model_in_primary](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa8694fdab3f514d8051dad1cc7362ac9)
- [bt_mesh_model_data_store](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gadff0895c5c34928d778fa615512b3d85)
- [bt_mesh_model_data_store_schedule](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga762896dd2e806b5be061b220d53ce4db)
- [bt_mesh_model_extend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf6356f715c8968151b8d539f2dd1880c)
- [bt_mesh_model_correspond](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga03ce9f6f9ccf734ea72beede09288923)
- [bt_mesh_model_is_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga10603a5846210a397f306b227ce10c2e)
- [bt_mesh_comp_change_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8575f680e77d86d6c85cac27985b9f3c)
- [bt_mesh_models_metadata_change_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga26ac86bdd32d27e0091735d98670687a)
- [bt_mesh_comp](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md)
- [cid](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md#a648f695898305ef9e6f4f9db42dd8cf9)
- [pid](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md#a54031f4c3683a7209e8f7441c5875788)
- [vid](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md#a7e4351e81e4e04bb9681e76d384f2fa5)
- [elem_count](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md#aff69499c7ac2c1ba643c946c75aa21ce)
- [elem](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md#ad3da0629db1cb423260aa202cab7f062)
- [bt_mesh_comp2_record](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md)
- [id](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#a19ce94025c1c8079ca2789bbcd09b00e)
- [x](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#a5f25c33170c77375f6492ad3cc0feaac)
- [y](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#a4970a0757c34ab97697c69728b564df6)
- [z](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#ac3cabce01490191f145234f386b9b119)
- [version](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#a26370a5dc68af03424c0f2f4fecd0181)
- [elem_offset_cnt](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#ad13066e9d6d32e8e2eab64881249eb7e)
- [elem_offset](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#a6f81d99a62252cd26d87ca4fb289bdf9)
- [data_len](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#abdc488e846233fa05f0fc48f4081576e)
- [data](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#acd5f5770a6606ad00fa0815e4866ec4e)
- [bt_mesh_comp2](../bluetooth_mesh_model_reference/P033_bt_mesh_comp2_结构体.md)
- [record_cnt](../bluetooth_mesh_model_reference/P033_bt_mesh_comp2_结构体.md#a9f3425cd64cc487e9a49b85bb0f2159b)
- [record](../bluetooth_mesh_model_reference/P033_bt_mesh_comp2_结构体.md#adf022ca0738626832d566fd6a5a1d889)
- [bt_mesh_comp2_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8445c550a47dba16e3fa6fea36d6d9fc)
- [assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [settings.h](../storage/P076_设置子系统头文件.md)
- [msg.h](https://docs.zephyrproject.org/latest/doxygen/html/msg_8h.html)
- [bt_mesh_comp2_record::id](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#a19ce94025c1c8079ca2789bbcd09b00e)
- [bt_mesh_comp2_record::version](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#a26370a5dc68af03424c0f2f4fecd0181)
- [bt_mesh_comp2_record::y](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#a4970a0757c34ab97697c69728b564df6)
- [bt_mesh_comp2_record::x](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#a5f25c33170c77375f6492ad3cc0feaac)
- [bt_mesh_comp2_record::elem_offset](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#a6f81d99a62252cd26d87ca4fb289bdf9)
- [bt_mesh_comp2_record::data_len](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#abdc488e846233fa05f0fc48f4081576e)
- [bt_mesh_comp2_record::z](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#ac3cabce01490191f145234f386b9b119)
- [bt_mesh_comp2_record::data](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#acd5f5770a6606ad00fa0815e4866ec4e)
- [bt_mesh_comp2_record::elem_offset_cnt](../bluetooth_mesh_model_reference/P034_bt_mesh_comp2_record_结构体.md#ad13066e9d6d32e8e2eab64881249eb7e)
- [bt_mesh_comp2::record_cnt](../bluetooth_mesh_model_reference/P033_bt_mesh_comp2_结构体.md#a9f3425cd64cc487e9a49b85bb0f2159b)
- [bt_mesh_comp2::record](../bluetooth_mesh_model_reference/P033_bt_mesh_comp2_结构体.md#adf022ca0738626832d566fd6a5a1d889)
- [bt_mesh_comp::pid](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md#a54031f4c3683a7209e8f7441c5875788)
- [bt_mesh_comp::cid](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md#a648f695898305ef9e6f4f9db42dd8cf9)
- [bt_mesh_comp::vid](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md#a7e4351e81e4e04bb9681e76d384f2fa5)
- [bt_mesh_comp::elem](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md#ad3da0629db1cb423260aa202cab7f062)
- [bt_mesh_comp::elem_count](../bluetooth_mesh_model_reference/P032_bt_mesh_comp_结构体.md#aff69499c7ac2c1ba643c946c75aa21ce)
- [bt_mesh_elem::bt_mesh_elem_rt_ctx](../bluetooth_mesh_model_reference/P060_bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体.md)
- [bt_mesh_elem::bt_mesh_elem_rt_ctx::addr](../bluetooth_mesh_model_reference/P060_bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体.md#a659279b38f1f3e015ebc648901577038)
- [bt_mesh_elem::rt](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#a2090fa7827eb6a7b8bd1adfb831439cb)
- [bt_mesh_elem::models](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#a57fefe57d9425d6666495d1f72a3f132)
- [bt_mesh_elem::loc](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#a5f4c8ded34cf56c7f60189584e8e5b46)
- [bt_mesh_elem::model_count](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#a648273e844ff9fa71578372e764ca8cf)
- [bt_mesh_elem::vnd_models](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#a81d4fc1c41e2944bf7f6e71b00e19a0f)
- [bt_mesh_elem::vnd_model_count](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md#aea56fd98c9aecfb9de3772ad3f14b25e)
- [bt_mesh_mod_id_vnd::company](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md#a187a919337c92f54eaba6f932c7a3670)
- [bt_mesh_mod_id_vnd::id](../bluetooth_mesh_model_reference/P074_bt_mesh_mod_id_vnd_结构体.md#a1a299852544a5e6fa3c34ac5ffd883d8)
- [bt_mesh_model::bt_mesh_model_rt_ctx](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md)
- [bt_mesh_model::bt_mesh_model_rt_ctx::next](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md#a434ae02cff38c614ef340a3c17f30e9b)
- [bt_mesh_model::bt_mesh_model_rt_ctx::user_data](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md#a718d3be40e7be83a196634054d18d568)
- [bt_mesh_model::bt_mesh_model_rt_ctx::mod_idx](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md#a79351fd25ad2ebd1f08ef1748d21dabd)
- [bt_mesh_model::bt_mesh_model_rt_ctx::flags](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md#ab584da43197ad7afe8c9ae807ce69f7e)
- [bt_mesh_model::bt_mesh_model_rt_ctx::elem_idx](../bluetooth_mesh_model_reference/P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md#aca9b558516b929a0b88d8171027e7c71)
- [bt_mesh_model_cb::init](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#a1688a2c6d7b3b17ba49a0975b6f4f68e)
- [bt_mesh_model_cb::settings_set](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#a21fc24829c6933a035b0f0be1a1f58e5)
- [bt_mesh_model_cb::reset](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#a3a7ad466120085c55bcffacb15c78518)
- [bt_mesh_model_cb::start](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#a8333420fb9d1d98799ae03ba3b23bfe4)
- [bt_mesh_model_cb::pending_store](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md#ae28f875dffc7f5f2ce99abe590369f43)
- [bt_mesh_model_op::opcode](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md#a09c18a889e08bc708b9dc623f8177e39)
- [bt_mesh_model_op::len](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md#a25445fe2e937a321942c312bd675e486)
- [bt_mesh_model_op::func](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md#a4a5de7a12f2f8743048aafc81af0cece)
- [bt_mesh_model_pub::update](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a0354344e08e633dc4d6c0b4e7b169080)
- [bt_mesh_model_pub::key](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a0ad1809fe74930c9b36b32516a8d146f)
- [bt_mesh_model_pub::retr_update](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a16c13e46c012ab836acd02b8fe5f05e3)
- [bt_mesh_model_pub::delayable](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a23a865dbd2dce5c1af074097864611e9)
- [bt_mesh_model_pub::cred](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a3617adb0c1192419bdac2ad0f37199ac)
- [bt_mesh_model_pub::retransmit](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a3d93d44ff85243dc94e7b4d36cde5b97)
- [bt_mesh_model_pub::addr](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a408c9185168b962f7e7314f9a429fe8c)
- [bt_mesh_model_pub::count](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a4e211c851bf91a9b43f035d435e9c93c)
- [bt_mesh_model_pub::period_div](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a4f2ce8727ffb44f564d1dc0615ebcadf)
- [bt_mesh_model_pub::msg](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a5f5639c01d3704ec3d527c418d35f827)
- [bt_mesh_model_pub::ttl](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#a820b713aaa1e0c33a4a59c80f805e854)
- [bt_mesh_model_pub::mod](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#aa5026299082b3013740c7e36c01f91f5)
- [bt_mesh_model_pub::period_start](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#ab6e00714ea899eb32873d10b0908d278)
- [bt_mesh_model_pub::send_rel](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#ab704aedcfd06d374615ef18c6ecc84a9)
- [bt_mesh_model_pub::fast_period](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#abdbdc3bbc5d4ac5a5d606b55bb2d50ee)
- [bt_mesh_model_pub::uuid](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#abea9c2085c9d2e1e2fc71f03dd323ee7)
- [bt_mesh_model_pub::period](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#ae550510e9ca45f8c9fd9802e4e7e0f3d)
- [bt_mesh_model_pub::timer](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md#af3771432d13805710e94f013332e8214)
- [bt_mesh_model::uuids](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a274c811c22b764908599127b128ce584)
- [bt_mesh_model::vnd](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a3372deccde1a5ab26d9204c97339596e)
- [bt_mesh_model::rt](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a3980e6f8100151cb3339792821fa7858)
- [bt_mesh_model::groups](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a460ab46730afa4f74e4066f787864b0b)
- [bt_mesh_model::op](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a4acc656c737cf79161414984312100b6)
- [bt_mesh_model::keys](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a63595a0559ca70ca76c996f0b71c7983)
- [bt_mesh_model::cb](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a67a91d64051e055b79f5d9166ab12660)
- [bt_mesh_model::keys_cnt](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a79b8fd44ced901c3478f0e04d7dadfcd)
- [bt_mesh_model::id](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#a848ccf09f7b75ff8a48acb6c8088cf2a)
- [bt_mesh_model::groups_cnt](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#adf3e3f0dab9838cc76361949b237bb9e)
- [bt_mesh_model::pub](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#af4a1b5e837b3a1266c7f61ee21020c0b)
- [bt_mesh_model::metadata](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md#af5b948709773e5388c30d457ec2a9559)
- [bt_mesh_models_metadata_entry::len](../bluetooth_mesh_model_reference/P080_bt_mesh_models_metadata_entry_结构体.md#a39959b1f46e1b21eb78dbe3293f29149)
- [bt_mesh_models_metadata_entry::data](../bluetooth_mesh_model_reference/P080_bt_mesh_models_metadata_entry_结构体.md#adb5aaf010cae636c0b60a88f38d36fac)
- [bt_mesh_models_metadata_entry::id](../bluetooth_mesh_model_reference/P080_bt_mesh_models_metadata_entry_结构体.md#ae343d6ca709e1aceafc25d64cdf3916d)
- [bt_mesh_send_cb::start](../bluetooth_mesh_model_reference/P099_bt_mesh_send_cb_结构体.md#a2f84ef4cb2d28729cd98b844a3d25f55)
- [bt_mesh_send_cb::end](../bluetooth_mesh_model_reference/P099_bt_mesh_send_cb_结构体.md#aa169dbec8c96fd41a35616c009604685)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[返回大纲](大纲.md) · [下一章](P002_audio.h_源码浏览.md)
