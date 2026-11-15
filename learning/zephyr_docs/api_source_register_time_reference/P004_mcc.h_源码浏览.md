---
id: learning.zephyr-docs.api-source-register-time-reference.page-4
title: mcc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_mcc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mcc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mcc_8h.html)。

## 4.1\_原始可见代码（Source Code）

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
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="foldopen00513"></a>
<a id="l00513"></a>
<a id="l00515"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00558"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00564"></a>
<a id="l00566"></a>
<a id="l00568"></a>
<a id="l00570"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00590"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00602"></a>
<a id="l00604"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00614"></a>
<a id="l00616"></a>
<a id="l00618"></a>
<a id="l00620"></a>
<a id="l00622"></a>
<a id="l00624"></a>
<a id="l00626"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00712"></a>
<a id="l00713"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00868"></a>
<a id="l00869"></a>
<a id="l00880"></a>
<a id="l00881"></a>
<a id="l00889"></a>
<a id="l00890"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="l00946"></a>
<a id="l00947"></a>
<a id="l00955"></a>
<a id="l00956"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="l00973"></a>
<a id="l00974"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="l00997"></a>
<a id="l01001"></a>
<a id="l01002"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__mcc_html_ga05295649385c3a337401765627d09553"></a>
<a id="agroup__bt__mcc_html_ga077a134ff1404fb76aa756a5531fd1d7"></a>
<a id="agroup__bt__mcc_html_ga0b309ae7ce23834f303c39017ffa4e50"></a>
<a id="agroup__bt__mcc_html_ga0e69de33c37957a2b5473df7d3c3f389"></a>
<a id="agroup__bt__mcc_html_ga1167f5e2ef4a7e78469aefc0cef18bff"></a>
<a id="agroup__bt__mcc_html_ga11e4c02ba0b1fbc197aaf071b82a1eed"></a>
<a id="agroup__bt__mcc_html_ga128883c867b10e57d3f2f26a708b7263"></a>
<a id="agroup__bt__mcc_html_ga1322f2ddbb587c70fd23a7ccfc1fc779"></a>
<a id="agroup__bt__mcc_html_ga1382e5b6000896dc94f6489909301719"></a>
<a id="agroup__bt__mcc_html_ga13bedbb573bc5575ab75fc3ae65c1870"></a>
<a id="agroup__bt__mcc_html_ga1a12fb89adf29c83bca02f701213c6d7"></a>
<a id="agroup__bt__mcc_html_ga1c4c842879cd8b209080a59d3ba125f8"></a>
<a id="agroup__bt__mcc_html_ga1fbf0b4fd624626127774d2662083875"></a>
<a id="agroup__bt__mcc_html_ga200a827f4bf5d65570ddabd028269f77"></a>
<a id="agroup__bt__mcc_html_ga28ac116604248643b0b203b4a314b7b1"></a>
<a id="agroup__bt__mcc_html_ga2f3099d097b28ab9c4abf81e19474def"></a>
<a id="agroup__bt__mcc_html_ga3089e6165e8491325f7205279bb5bb83"></a>
<a id="agroup__bt__mcc_html_ga324161056e03195820bbd7cc77ff287d"></a>
<a id="agroup__bt__mcc_html_ga366fdfaa23cef9f1c3ba7ddd36a67658"></a>
<a id="agroup__bt__mcc_html_ga38733456db6bc6558a511e104577c9c9"></a>
<a id="agroup__bt__mcc_html_ga3ccd5961cc4c8d82fa988d300e12e1ae"></a>
<a id="agroup__bt__mcc_html_ga3f4a538bcf436e4e80b73ed6e077dfa0"></a>
<a id="agroup__bt__mcc_html_ga471d0491b70e5472e16c3035507761cc"></a>
<a id="agroup__bt__mcc_html_ga48dd365aa637336b9899db4b6986a5e4"></a>
<a id="agroup__bt__mcc_html_ga4b1ebe682ad134795f8a1b494244f8b6"></a>
<a id="agroup__bt__mcc_html_ga4cb0a95e91d3ec00ede64663a2b932f0"></a>
<a id="agroup__bt__mcc_html_ga50a45f043bd2ae1741a120e02e9dc2f5"></a>
<a id="agroup__bt__mcc_html_ga50da90a5c351c99494208b44096a61c8"></a>
<a id="agroup__bt__mcc_html_ga5a39822a21a6f2aa7a6548c57979a926"></a>
<a id="agroup__bt__mcc_html_ga5b3a8fb8e8251cf005b34e47619ae7b9"></a>
<a id="agroup__bt__mcc_html_ga5f21a1eed4bfe4dfbca40949af895723"></a>
<a id="agroup__bt__mcc_html_ga611c9edebff5b4347ad1241ffd19f49e"></a>
<a id="agroup__bt__mcc_html_ga67611a3068284b0c7fbb3ef07dfe7688"></a>
<a id="agroup__bt__mcc_html_ga692160554947f92e8c81912c5e597086"></a>
<a id="agroup__bt__mcc_html_ga6927860f1803aeade4994610da32d402"></a>
<a id="agroup__bt__mcc_html_ga6f5383be3f344c25361786d903640909"></a>
<a id="agroup__bt__mcc_html_ga724ce71fc88f1ca4bcf209c92c177f36"></a>
<a id="agroup__bt__mcc_html_ga77cbf810c35d1a17efce1fae6a941963"></a>
<a id="agroup__bt__mcc_html_ga7cdb524ff9c34f24c1740adb9eca072c"></a>
<a id="agroup__bt__mcc_html_ga7dfa14489a4cea4b00053c9aa75cf373"></a>
<a id="agroup__bt__mcc_html_ga8374ac230c5fe6b5a1bb7fa873fdeb49"></a>
<a id="agroup__bt__mcc_html_ga83d6614d4a0808782b1b4df115b872d2"></a>
<a id="agroup__bt__mcc_html_ga8bbb0d28f7dcf23a30a8ca56d647ac2c"></a>
<a id="agroup__bt__mcc_html_ga8cb43a6947df48113b082d8cc8ccf25c"></a>
<a id="agroup__bt__mcc_html_ga920f25e04e1be4ad5f7e220c2e9102b5"></a>
<a id="agroup__bt__mcc_html_ga9489c34b6006df8bd26e626030cab71f"></a>
<a id="agroup__bt__mcc_html_ga94de08bb0a1e1324600e4957b648e92b"></a>
<a id="agroup__bt__mcc_html_ga9805222315ca6e6df0720233055af10c"></a>
<a id="agroup__bt__mcc_html_ga98814a516a027bdaa3250e93d55309fd"></a>
<a id="agroup__bt__mcc_html_gaa1f9ead03b4cccaff1e3390b8052b0f3"></a>
<a id="agroup__bt__mcc_html_gaa243806f65c4a37d41f25bcc4f1839fc"></a>
<a id="agroup__bt__mcc_html_gaa566a4c42f0ab0ab6feddf4e25845609"></a>
<a id="agroup__bt__mcc_html_gaa943b61848ee43e91d473f6fdd0a604f"></a>
<a id="agroup__bt__mcc_html_gaaddc4abe38f6ca811967ae6a10d8f8f0"></a>
<a id="agroup__bt__mcc_html_gab168a4c86de444dd066802c4a5fe41c3"></a>
<a id="agroup__bt__mcc_html_gab268faeca207e115ee1be0843ab8c342"></a>
<a id="agroup__bt__mcc_html_gab37df36e15132b9235d1093f5aa403cc"></a>
<a id="agroup__bt__mcc_html_gaba527d8f0307ab11150a5434231c0e7e"></a>
<a id="agroup__bt__mcc_html_gac1b440cfa54dd4b6e23bb47bf885f88d"></a>
<a id="agroup__bt__mcc_html_gac22e840b65895aa018ab1b4535a87672"></a>
<a id="agroup__bt__mcc_html_gac45a2aff295535f70ac4a070e970b7a0"></a>
<a id="agroup__bt__mcc_html_gac4b09a77df52d2681e7652591ca32bf8"></a>
<a id="agroup__bt__mcc_html_gaca904bacb552792ffd85c6a640f0ba48"></a>
<a id="agroup__bt__mcc_html_gad324366d33bef6b1ed1c8fc881bf44cf"></a>
<a id="agroup__bt__mcc_html_gadb607997fdcb3e57bbfc90790de4b927"></a>
<a id="agroup__bt__mcc_html_gadf687cb26a6d00bca73e273da583df88"></a>
<a id="agroup__bt__mcc_html_gae001cb2d701457ce083aa8a0fd5ec518"></a>
<a id="agroup__bt__mcc_html_gae3f385811f852d584595c6e531556aed"></a>
<a id="agroup__bt__mcc_html_gae4c2d1a5c41df1c3535418cc23d48f8e"></a>
<a id="agroup__bt__mcc_html_gaf0d619b493a8fb4c00278a0a85bb2529"></a>
<a id="agroup__bt__mcc_html_gaf143098f5dfcfba01df3d6f06472779e"></a>
<a id="agroup__bt__mcc_html_gaf186e6adefa296de4146502665d738b3"></a>
<a id="agroup__bt__mcc_html_gaf61f6fcf3f96ccb6f5a72ffaad27dec4"></a>
<a id="agroup__bt__mcc_html_gafb0869e0ef5332d39070081efdacf17c"></a>
<a id="agroup__bt__mcc_html_gafeebcbb0c77d5d4acbe151fd9888d084"></a>
<a id="agroup__bt__mcc_html_gaff887eda3b84cad1052549f23c8dcfbe"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="amedia__proxy_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__mcc__cb_html"></a>
<a id="astructbt__mcc__cb_html_a00a0ba5ed665ef7fc2ca861d985ccd64"></a>
<a id="astructbt__mcc__cb_html_a00acb676c73ebbad2b0180b3e8373150"></a>
<a id="astructbt__mcc__cb_html_a054e0cfb27c01f43d499a2c44788cb73"></a>
<a id="astructbt__mcc__cb_html_a0e7757b6f911456feaca931cd33f117f"></a>
<a id="astructbt__mcc__cb_html_a17ebc9dbddd714d99b599b2a683ab771"></a>
<a id="astructbt__mcc__cb_html_a1c7277f390f6b478090611be9e82a4f8"></a>
<a id="astructbt__mcc__cb_html_a2c1b570ce8d83c3f20eb99807263a5cd"></a>
<a id="astructbt__mcc__cb_html_a2f48a0e0b891131347b0ddc2cb5a8ba7"></a>
<a id="astructbt__mcc__cb_html_a3538beef41edd96b8557b43c1266078b"></a>
<a id="astructbt__mcc__cb_html_a38e4682608c7d7ff6c44431a6bdab3af"></a>
<a id="astructbt__mcc__cb_html_a3975e296b67eb244bf92254e9776ea3c"></a>
<a id="astructbt__mcc__cb_html_a46bd2c23d92d8362cdf9ad4862b78407"></a>
<a id="astructbt__mcc__cb_html_a47f8d92b18b0e4ffb3aacde05e7cb410"></a>
<a id="astructbt__mcc__cb_html_a4f2ea54d6c60beb28feab7b6453aec7c"></a>
<a id="astructbt__mcc__cb_html_a52724924ab19f59cc936344ebe13d437"></a>
<a id="astructbt__mcc__cb_html_a540797123f8968b49a6e98b30ea534c8"></a>
<a id="astructbt__mcc__cb_html_a5f87b5d07241b4124911be0cd6c43b37"></a>
<a id="astructbt__mcc__cb_html_a75c8e63baf45a119e9007f246362ab8d"></a>
<a id="astructbt__mcc__cb_html_a810ceaee44fcbdec90a1ee227b6974df"></a>
<a id="astructbt__mcc__cb_html_a835f60ad32edc4311a624e779972f0d5"></a>
<a id="astructbt__mcc__cb_html_a85268d9ce708aef01aa528aaedf0f7e0"></a>
<a id="astructbt__mcc__cb_html_a872d0322ba3889f1f7d32e8966b53624"></a>
<a id="astructbt__mcc__cb_html_a87583247634728d3d9af7eb411d088a7"></a>
<a id="astructbt__mcc__cb_html_a8c7b5954e286d074a94a39bee266082c"></a>
<a id="astructbt__mcc__cb_html_a90e62e90752087da36122a65f6c9ed4e"></a>
<a id="astructbt__mcc__cb_html_a929d7b8fc925961048d5ff5e70a5126e"></a>
<a id="astructbt__mcc__cb_html_a9f7f3424aa230a8752f40a40b82b0b66"></a>
<a id="astructbt__mcc__cb_html_aaa2bdfb99e5cd7c2a0d0c800533e8491"></a>
<a id="astructbt__mcc__cb_html_abb7769b73564a22645bfe6b11f239637"></a>
<a id="astructbt__mcc__cb_html_ac0e382f1117f983e7a2178fde274d460"></a>
<a id="astructbt__mcc__cb_html_ac9e182bbdd9671c5caee5bcd42198d90"></a>
<a id="astructbt__mcc__cb_html_ad13669e60992a1a407534f387efd1da8"></a>
<a id="astructbt__mcc__cb_html_ad1636e717ef5039586b7a1462041e888"></a>
<a id="astructbt__mcc__cb_html_ad7ddcae67bf71030ac2d8438ac2e863f"></a>
<a id="astructbt__mcc__cb_html_ad8d3eff0cc183797280c9f668a840add"></a>
<a id="astructbt__mcc__cb_html_ae4d0e2e4df695352e8d2ed76db1f420e"></a>
<a id="astructbt__mcc__cb_html_aeea1ef17b3b1e24c965d71f210952079"></a>
<a id="astructbt__mcc__cb_html_af1c9664a2459550af0a6ed611fd17263"></a>
<a id="astructbt__mcc__cb_html_affa57da8f325dce8298d097af38d0d62"></a>
<a id="astructbt__ots__client_html"></a>
<a id="astructmpl__cmd__ntf_html"></a>
<a id="astructmpl__cmd_html"></a>
<a id="astructmpl__search_html"></a>
<a id="astructmpl__search_html_a836bebfaadb56672a7e76c0ac2e450a9"></a>
<a id="astructnet__buf__simple_html"></a>

```c


/*
 * Copyright (c) 2019 - 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MCC_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MCC_H_


#include <stdint.h>
#include <stdbool.h>

#include <zephyr/bluetooth/conn.h>
#include <zephyr/net_buf.h>
#include <zephyr/bluetooth/audio/media_proxy.h>

#ifdef __cplusplus
extern "C" {
#endif

/**** Callback functions ******************************************************/

typedef void (*bt_mcc_discover_mcs_cb)(struct bt_conn *conn, int err);

typedef void (*bt_mcc_read_player_name_cb)(struct bt_conn *conn, int err, const char *name);

typedef void (*bt_mcc_read_icon_obj_id_cb)(struct bt_conn *conn, int err, uint64_t icon_id);

typedef void (*bt_mcc_read_icon_url_cb)(struct bt_conn *conn, int err, const char *icon_url);

typedef void (*bt_mcc_track_changed_ntf_cb)(struct bt_conn *conn, int err);


typedef void (*bt_mcc_read_track_title_cb)(struct bt_conn *conn, int err, const char *title);

typedef void (*bt_mcc_read_track_duration_cb)(struct bt_conn *conn, int err, int32_t dur);

typedef void (*bt_mcc_read_track_position_cb)(struct bt_conn *conn, int err, int32_t pos);

typedef void (*bt_mcc_set_track_position_cb)(struct bt_conn *conn, int err, int32_t pos);

typedef void (*bt_mcc_read_playback_speed_cb)(struct bt_conn *conn, int err, int8_t speed);

typedef void (*bt_mcc_set_playback_speed_cb)(struct bt_conn *conn, int err, int8_t speed);

typedef void (*bt_mcc_read_seeking_speed_cb)(struct bt_conn *conn, int err, int8_t speed);

typedef void (*bt_mcc_read_segments_obj_id_cb)(struct bt_conn *conn, int err, uint64_t id);

typedef void (*bt_mcc_read_current_track_obj_id_cb)(struct bt_conn *conn, int err, uint64_t id);

typedef void (*bt_mcc_set_current_track_obj_id_cb)(struct bt_conn *conn, int err, uint64_t id);

typedef void (*bt_mcc_read_next_track_obj_id_cb)(struct bt_conn *conn, int err, uint64_t id);

typedef void (*bt_mcc_set_next_track_obj_id_cb)(struct bt_conn *conn, int err, uint64_t id);

typedef void (*bt_mcc_read_parent_group_obj_id_cb)(struct bt_conn *conn, int err, uint64_t id);

typedef void (*bt_mcc_read_current_group_obj_id_cb)(struct bt_conn *conn, int err, uint64_t id);

typedef void (*bt_mcc_set_current_group_obj_id_cb)(struct bt_conn *conn, int err, uint64_t obj_id);

typedef void (*bt_mcc_read_playing_order_cb)(struct bt_conn *conn, int err, uint8_t order);

typedef void (*bt_mcc_set_playing_order_cb)(struct bt_conn *conn, int err, uint8_t order);

typedef void (*bt_mcc_read_playing_orders_supported_cb)(struct bt_conn *conn, int err,
                                                        uint16_t orders);

typedef void (*bt_mcc_read_media_state_cb)(struct bt_conn *conn, int err, uint8_t state);

typedef void (*bt_mcc_send_cmd_cb)(struct bt_conn *conn, int err, const struct mpl_cmd *cmd);

typedef void (*bt_mcc_cmd_ntf_cb)(struct bt_conn *conn, int err, const struct mpl_cmd_ntf *ntf);

typedef void (*bt_mcc_read_opcodes_supported_cb)(struct bt_conn *conn, int err,
                                                 uint32_t opcodes);

typedef void (*bt_mcc_send_search_cb)(struct bt_conn *conn, int err,
                                      const struct mpl_search *search);

typedef void (*bt_mcc_search_ntf_cb)(struct bt_conn *conn, int err,
                                     uint8_t result_code);

typedef void (*bt_mcc_read_search_results_obj_id_cb)(struct bt_conn *conn,
                                                     int err, uint64_t id);

typedef void (*bt_mcc_read_content_control_id_cb)(struct bt_conn *conn,
                                                  int err, uint8_t ccid);

/**** Callback functions for the included Object Transfer service *************/

typedef void (*bt_mcc_otc_obj_selected_cb)(struct bt_conn *conn, int err);

typedef void (*bt_mcc_otc_obj_metadata_cb)(struct bt_conn *conn, int err);

typedef void (*bt_mcc_otc_read_icon_object_cb)(struct bt_conn *conn, int err,
                                               struct net_buf_simple *buf);

typedef void (*bt_mcc_otc_read_track_segments_object_cb)(struct bt_conn *conn, int err,
                                                         struct net_buf_simple *buf);

typedef void (*bt_mcc_otc_read_current_track_object_cb)(struct bt_conn *conn, int err,
                                                        struct net_buf_simple *buf);

typedef void (*bt_mcc_otc_read_next_track_object_cb)(struct bt_conn *conn, int err,
                                                     struct net_buf_simple *buf);

typedef void (*bt_mcc_otc_read_parent_group_object_cb)(struct bt_conn *conn, int err,
                                                       struct net_buf_simple *buf);

typedef void (*bt_mcc_otc_read_current_group_object_cb)(struct bt_conn *conn, int err,
                                                        struct net_buf_simple *buf);


struct bt_mcc_cb {
        bt_mcc_discover_mcs_cb                   discover_mcs;
        bt_mcc_read_player_name_cb               read_player_name;
#if defined(CONFIG_BT_OTS_CLIENT) || defined(__DOXYGEN__)
        bt_mcc_read_icon_obj_id_cb               read_icon_obj_id;
#endif /* CONFIG_BT_OTS_CLIENT */
#if defined(CONFIG_BT_MCC_READ_MEDIA_PLAYER_ICON_URL) || defined(__DOXYGEN__)
        bt_mcc_read_icon_url_cb                  read_icon_url;
#endif /* defined(CONFIG_BT_MCC_READ_MEDIA_PLAYER_ICON_URL) */
        bt_mcc_track_changed_ntf_cb              track_changed_ntf;
#if defined(CONFIG_BT_MCC_READ_TRACK_TITLE) || defined(__DOXYGEN__)
        bt_mcc_read_track_title_cb               read_track_title;
#endif /* defined(CONFIG_BT_MCC_READ_TRACK_TITLE) */
#if defined(CONFIG_BT_MCC_READ_TRACK_DURATION) || defined(__DOXYGEN__)
        bt_mcc_read_track_duration_cb            read_track_duration;
#endif /* defined(CONFIG_BT_MCC_READ_TRACK_DURATION) */
#if defined(CONFIG_BT_MCC_READ_TRACK_POSITION) || defined(__DOXYGEN__)
        bt_mcc_read_track_position_cb            read_track_position;
#endif /* defined(CONFIG_BT_MCC_READ_TRACK_POSITION) */
#if defined(CONFIG_BT_MCC_SET_TRACK_POSITION) || defined(__DOXYGEN__)
        bt_mcc_set_track_position_cb             set_track_position;
#endif /* defined(CONFIG_BT_MCC_SET_TRACK_POSITION) */
#if defined(CONFIG_BT_MCC_READ_PLAYBACK_SPEED) || defined(__DOXYGEN__)
        bt_mcc_read_playback_speed_cb            read_playback_speed;
#endif /* defined (CONFIG_BT_MCC_READ_PLAYBACK_SPEED) */
#if defined(CONFIG_BT_MCC_SET_PLAYBACK_SPEED) || defined(__DOXYGEN__)
        bt_mcc_set_playback_speed_cb             set_playback_speed;
#endif /* defined (CONFIG_BT_MCC_SET_PLAYBACK_SPEED) */
#if defined(CONFIG_BT_MCC_READ_SEEKING_SPEED) || defined(__DOXYGEN__)
        bt_mcc_read_seeking_speed_cb             read_seeking_speed;
#endif /* defined (CONFIG_BT_MCC_READ_SEEKING_SPEED) */
#if defined(CONFIG_BT_OTS_CLIENT) || defined(__DOXYGEN__)
        bt_mcc_read_segments_obj_id_cb           read_segments_obj_id;
        bt_mcc_read_current_track_obj_id_cb      read_current_track_obj_id;
        bt_mcc_set_current_track_obj_id_cb       set_current_track_obj_id;
        bt_mcc_read_next_track_obj_id_cb         read_next_track_obj_id;
        bt_mcc_set_next_track_obj_id_cb          set_next_track_obj_id;
        bt_mcc_read_current_group_obj_id_cb      read_current_group_obj_id;
        bt_mcc_set_current_group_obj_id_cb       set_current_group_obj_id;
        bt_mcc_read_parent_group_obj_id_cb       read_parent_group_obj_id;
#endif /* CONFIG_BT_OTS_CLIENT */
#if defined(CONFIG_BT_MCC_READ_PLAYING_ORDER) || defined(__DOXYGEN__)
        bt_mcc_read_playing_order_cb             read_playing_order;
#endif /* defined(CONFIG_BT_MCC_READ_PLAYING_ORDER) */
#if defined(CONFIG_BT_MCC_SET_PLAYING_ORDER) || defined(__DOXYGEN__)
        bt_mcc_set_playing_order_cb              set_playing_order;
#endif /* defined(CONFIG_BT_MCC_SET_PLAYING_ORDER) */
#if defined(CONFIG_BT_MCC_READ_PLAYING_ORDER_SUPPORTED) || defined(__DOXYGEN__)
        bt_mcc_read_playing_orders_supported_cb  read_playing_orders_supported;
#endif /* defined(CONFIG_BT_MCC_READ_PLAYING_ORDER_SUPPORTED) */
#if defined(CONFIG_BT_MCC_READ_MEDIA_STATE) || defined(__DOXYGEN__)
        bt_mcc_read_media_state_cb               read_media_state;
#endif /* defined(CONFIG_BT_MCC_READ_MEDIA_STATE) */
#if defined(CONFIG_BT_MCC_SET_MEDIA_CONTROL_POINT) || defined(__DOXYGEN__)
        bt_mcc_send_cmd_cb                       send_cmd;
#endif /* defined(CONFIG_BT_MCC_SET_MEDIA_CONTROL_POINT) */
        bt_mcc_cmd_ntf_cb                        cmd_ntf;
#if defined(CONFIG_BT_MCC_READ_MEDIA_CONTROL_POINT_OPCODES_SUPPORTED) || defined(__DOXYGEN__)
        bt_mcc_read_opcodes_supported_cb         read_opcodes_supported;
#endif /* defined(CONFIG_BT_MCC_READ_MEDIA_CONTROL_POINT_OPCODES_SUPPORTED) */
#if defined(CONFIG_BT_OTS_CLIENT) || defined(__DOXYGEN__)
        bt_mcc_send_search_cb                    send_search;
        bt_mcc_search_ntf_cb                     search_ntf;
        bt_mcc_read_search_results_obj_id_cb     read_search_results_obj_id;
#endif /* CONFIG_BT_OTS_CLIENT */
#if defined(CONFIG_BT_MCC_READ_CONTENT_CONTROL_ID) || defined(__DOXYGEN__)
        bt_mcc_read_content_control_id_cb        read_content_control_id;
#endif /* defined(CONFIG_BT_MCC_READ_CONTENT_CONTROL_ID) */
#if defined(CONFIG_BT_OTS_CLIENT) || defined(__DOXYGEN__)
        bt_mcc_otc_obj_selected_cb               otc_obj_selected;
        bt_mcc_otc_obj_metadata_cb               otc_obj_metadata;
        bt_mcc_otc_read_icon_object_cb           otc_icon_object;
        bt_mcc_otc_read_track_segments_object_cb otc_track_segments_object;
        bt_mcc_otc_read_current_track_object_cb  otc_current_track_object;
        bt_mcc_otc_read_next_track_object_cb     otc_next_track_object;
        bt_mcc_otc_read_current_group_object_cb  otc_current_group_object;
        bt_mcc_otc_read_parent_group_object_cb   otc_parent_group_object;
#endif /* CONFIG_BT_OTS_CLIENT */
};

/**** Functions ***************************************************************/

int bt_mcc_init(struct bt_mcc_cb *cb);


int bt_mcc_discover_mcs(struct bt_conn *conn, bool subscribe);

int bt_mcc_read_player_name(struct bt_conn *conn);

int bt_mcc_read_icon_obj_id(struct bt_conn *conn);

int bt_mcc_read_icon_url(struct bt_conn *conn);

int bt_mcc_read_track_title(struct bt_conn *conn);

int bt_mcc_read_track_duration(struct bt_conn *conn);

int bt_mcc_read_track_position(struct bt_conn *conn);

int bt_mcc_set_track_position(struct bt_conn *conn, int32_t pos);

int bt_mcc_read_playback_speed(struct bt_conn *conn);

int bt_mcc_set_playback_speed(struct bt_conn *conn, int8_t speed);

int bt_mcc_read_seeking_speed(struct bt_conn *conn);

int bt_mcc_read_segments_obj_id(struct bt_conn *conn);

int bt_mcc_read_current_track_obj_id(struct bt_conn *conn);

int bt_mcc_set_current_track_obj_id(struct bt_conn *conn, uint64_t id);

int bt_mcc_read_next_track_obj_id(struct bt_conn *conn);

int bt_mcc_set_next_track_obj_id(struct bt_conn *conn, uint64_t id);

int bt_mcc_read_current_group_obj_id(struct bt_conn *conn);

int bt_mcc_set_current_group_obj_id(struct bt_conn *conn, uint64_t id);

int bt_mcc_read_parent_group_obj_id(struct bt_conn *conn);

int bt_mcc_read_playing_order(struct bt_conn *conn);

int bt_mcc_set_playing_order(struct bt_conn *conn, uint8_t order);

int bt_mcc_read_playing_orders_supported(struct bt_conn *conn);

int bt_mcc_read_media_state(struct bt_conn *conn);

int bt_mcc_send_cmd(struct bt_conn *conn, const struct mpl_cmd *cmd);

int bt_mcc_read_opcodes_supported(struct bt_conn *conn);

int bt_mcc_send_search(struct bt_conn *conn, const struct mpl_search *search);

int bt_mcc_read_search_results_obj_id(struct bt_conn *conn);

int bt_mcc_read_content_control_id(struct bt_conn *conn);

int bt_mcc_otc_read_object_metadata(struct bt_conn *conn);

int bt_mcc_otc_read_icon_object(struct bt_conn *conn);

int bt_mcc_otc_read_track_segments_object(struct bt_conn *conn);

int bt_mcc_otc_read_current_track_object(struct bt_conn *conn);

int bt_mcc_otc_read_next_track_object(struct bt_conn *conn);

int bt_mcc_otc_read_current_group_object(struct bt_conn *conn);

int bt_mcc_otc_read_parent_group_object(struct bt_conn *conn);

struct bt_ots_client *bt_mcc_otc_inst(struct bt_conn *conn);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MCC_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2019 - 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 40 行

回调函数（Callback functions）分隔标题。

### 注释 3：原第 403 行

所包含对象传输服务（Object Transfer Service）的回调函数分隔标题。

### 注释 4：原第 521 行

条件编译配置（Configuration）标记：`CONFIG_BT_OTS_CLIENT`。

### 注释 5：原第 525 行

条件表达式：`defined(CONFIG_BT_MCC_READ_MEDIA_PLAYER_ICON_URL)`。

### 注释 6：原第 531 行

条件表达式：`defined(CONFIG_BT_MCC_READ_TRACK_TITLE)`。

### 注释 7：原第 535 行

条件表达式：`defined(CONFIG_BT_MCC_READ_TRACK_DURATION)`。

### 注释 8：原第 539 行

条件表达式：`defined(CONFIG_BT_MCC_READ_TRACK_POSITION)`。

### 注释 9：原第 543 行

条件表达式：`defined(CONFIG_BT_MCC_SET_TRACK_POSITION)`。

### 注释 10：原第 547 行

条件表达式：`defined (CONFIG_BT_MCC_READ_PLAYBACK_SPEED)`。

### 注释 11：原第 551 行

条件表达式：`defined (CONFIG_BT_MCC_SET_PLAYBACK_SPEED)`。

### 注释 12：原第 555 行

条件表达式：`defined (CONFIG_BT_MCC_READ_SEEKING_SPEED)`。

### 注释 13：原第 573 行

条件编译配置（Configuration）标记：`CONFIG_BT_OTS_CLIENT`。

### 注释 14：原第 577 行

条件表达式：`defined(CONFIG_BT_MCC_READ_PLAYING_ORDER)`。

### 注释 15：原第 581 行

条件表达式：`defined(CONFIG_BT_MCC_SET_PLAYING_ORDER)`。

### 注释 16：原第 585 行

条件表达式：`defined(CONFIG_BT_MCC_READ_PLAYING_ORDER_SUPPORTED)`。

### 注释 17：原第 589 行

条件表达式：`defined(CONFIG_BT_MCC_READ_MEDIA_STATE)`。

### 注释 18：原第 593 行

条件表达式：`defined(CONFIG_BT_MCC_SET_MEDIA_CONTROL_POINT)`。

### 注释 19：原第 599 行

条件表达式：`defined(CONFIG_BT_MCC_READ_MEDIA_CONTROL_POINT_OPCODES_SUPPORTED)`。

### 注释 20：原第 607 行

条件编译配置（Configuration）标记：`CONFIG_BT_OTS_CLIENT`。

### 注释 21：原第 611 行

条件表达式：`defined(CONFIG_BT_MCC_READ_CONTENT_CONTROL_ID)`。

### 注释 22：原第 629 行

条件编译配置（Configuration）标记：`CONFIG_BT_OTS_CLIENT`。

### 注释 23：原第 632 行

函数（Functions）分隔标题。

### 注释 24：原第 1002 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MCC_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mcc_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/bluetooth/audio/media_proxy.h](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h.html)
- [bt_mcc_discover_mcs_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab268faeca207e115ee1be0843ab8c342)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_mcc_read_player_name_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa943b61848ee43e91d473f6fdd0a604f)
- [bt_mcc_read_icon_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga471d0491b70e5472e16c3035507761cc)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [bt_mcc_read_icon_url_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaaddc4abe38f6ca811967ae6a10d8f8f0)
- [bt_mcc_track_changed_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga67611a3068284b0c7fbb3ef07dfe7688)
- [bt_mcc_read_track_title_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga6927860f1803aeade4994610da32d402)
- [bt_mcc_read_track_duration_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga7cdb524ff9c34f24c1740adb9eca072c)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bt_mcc_read_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga128883c867b10e57d3f2f26a708b7263)
- [bt_mcc_set_track_position_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1167f5e2ef4a7e78469aefc0cef18bff)
- [bt_mcc_read_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga6f5383be3f344c25361786d903640909)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [bt_mcc_set_playback_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1322f2ddbb587c70fd23a7ccfc1fc779)
- [bt_mcc_read_seeking_speed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga3089e6165e8491325f7205279bb5bb83)
- [bt_mcc_read_segments_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1fbf0b4fd624626127774d2662083875)
- [bt_mcc_read_current_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga28ac116604248643b0b203b4a314b7b1)
- [bt_mcc_set_current_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf0d619b493a8fb4c00278a0a85bb2529)
- [bt_mcc_read_next_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga83d6614d4a0808782b1b4df115b872d2)
- [bt_mcc_set_next_track_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga2f3099d097b28ab9c4abf81e19474def)
- [bt_mcc_read_parent_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga48dd365aa637336b9899db4b6986a5e4)
- [bt_mcc_read_current_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5f21a1eed4bfe4dfbca40949af895723)
- [bt_mcc_set_current_group_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)
- [bt_mcc_read_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gafb0869e0ef5332d39070081efdacf17c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mcc_set_playing_order_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1a12fb89adf29c83bca02f701213c6d7)
- [bt_mcc_read_playing_orders_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac45a2aff295535f70ac4a070e970b7a0)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mcc_read_media_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga200a827f4bf5d65570ddabd028269f77)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_mcc_send_cmd_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gae4c2d1a5c41df1c3535418cc23d48f8e)
- [mpl_cmd](../audio_video_model_reference/P037_mpl_cmd_结构体.md)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [bt_mcc_cmd_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga50da90a5c351c99494208b44096a61c8)
- [mpl_cmd_ntf](../audio_video_model_reference/P038_mpl_cmd_ntf_结构体.md)
- [bt_mcc_read_opcodes_supported_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab37df36e15132b9235d1093f5aa403cc)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_mcc_send_search_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga9489c34b6006df8bd26e626030cab71f)
- [mpl_search](../audio_video_model_reference/P040_mpl_search_结构体.md)
- [search](../audio_video_model_reference/P040_mpl_search_结构体.md#a836bebfaadb56672a7e76c0ac2e450a9)
- [bt_mcc_search_ntf_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gab168a4c86de444dd066802c4a5fe41c3)
- [bt_mcc_read_search_results_obj_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5a39822a21a6f2aa7a6548c57979a926)
- [bt_mcc_read_content_control_id_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gadb607997fdcb3e57bbfc90790de4b927)
- [bt_mcc_otc_obj_selected_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf186e6adefa296de4146502665d738b3)
- [bt_mcc_otc_obj_metadata_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga9805222315ca6e6df0720233055af10c)
- [bt_mcc_otc_read_icon_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga13bedbb573bc5575ab75fc3ae65c1870)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mcc_otc_read_track_segments_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1c4c842879cd8b209080a59d3ba125f8)
- [bt_mcc_otc_read_current_track_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaff887eda3b84cad1052549f23c8dcfbe)
- [bt_mcc_otc_read_next_track_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga920f25e04e1be4ad5f7e220c2e9102b5)
- [bt_mcc_otc_read_parent_group_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaca904bacb552792ffd85c6a640f0ba48)
- [bt_mcc_otc_read_current_group_object_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga0b309ae7ce23834f303c39017ffa4e50)
- [bt_mcc_cb](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md)
- [discover_mcs](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a2f48a0e0b891131347b0ddc2cb5a8ba7)
- [read_player_name](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#aeea1ef17b3b1e24c965d71f210952079)
- [read_icon_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a00acb676c73ebbad2b0180b3e8373150)
- [read_icon_url](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a8c7b5954e286d074a94a39bee266082c)
- [track_changed_ntf](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#abb7769b73564a22645bfe6b11f239637)
- [read_track_title](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a3975e296b67eb244bf92254e9776ea3c)
- [read_track_duration](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a85268d9ce708aef01aa528aaedf0f7e0)
- [read_track_position](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ad1636e717ef5039586b7a1462041e888)
- [set_track_position](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#affa57da8f325dce8298d097af38d0d62)
- [read_playback_speed](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a47f8d92b18b0e4ffb3aacde05e7cb410)
- [set_playback_speed](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a5f87b5d07241b4124911be0cd6c43b37)
- [read_seeking_speed](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a75c8e63baf45a119e9007f246362ab8d)
- [read_segments_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a810ceaee44fcbdec90a1ee227b6974df)
- [read_current_track_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a46bd2c23d92d8362cdf9ad4862b78407)
- [set_current_track_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ac9e182bbdd9671c5caee5bcd42198d90)
- [read_next_track_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a540797123f8968b49a6e98b30ea534c8)
- [set_next_track_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a4f2ea54d6c60beb28feab7b6453aec7c)
- [read_current_group_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a0e7757b6f911456feaca931cd33f117f)
- [set_current_group_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ad8d3eff0cc183797280c9f668a840add)
- [read_parent_group_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a87583247634728d3d9af7eb411d088a7)
- [read_playing_order](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a3538beef41edd96b8557b43c1266078b)
- [set_playing_order](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a00a0ba5ed665ef7fc2ca861d985ccd64)
- [read_playing_orders_supported](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a929d7b8fc925961048d5ff5e70a5126e)
- [read_media_state](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a38e4682608c7d7ff6c44431a6bdab3af)
- [send_cmd](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a90e62e90752087da36122a65f6c9ed4e)
- [cmd_ntf](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a835f60ad32edc4311a624e779972f0d5)
- [read_opcodes_supported](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ad7ddcae67bf71030ac2d8438ac2e863f)
- [send_search](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a1c7277f390f6b478090611be9e82a4f8)
- [search_ntf](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a9f7f3424aa230a8752f40a40b82b0b66)
- [read_search_results_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#aaa2bdfb99e5cd7c2a0d0c800533e8491)
- [read_content_control_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ae4d0e2e4df695352e8d2ed76db1f420e)
- [otc_obj_selected](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a17ebc9dbddd714d99b599b2a683ab771)
- [otc_obj_metadata](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#af1c9664a2459550af0a6ed611fd17263)
- [otc_icon_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a054e0cfb27c01f43d499a2c44788cb73)
- [otc_track_segments_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a2c1b570ce8d83c3f20eb99807263a5cd)
- [otc_current_track_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ad13669e60992a1a407534f387efd1da8)
- [otc_next_track_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a52724924ab19f59cc936344ebe13d437)
- [otc_current_group_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ac0e382f1117f983e7a2178fde274d460)
- [otc_parent_group_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a872d0322ba3889f1f7d32e8966b53624)
- [bt_mcc_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga94de08bb0a1e1324600e4957b648e92b)
- [bt_mcc_discover_mcs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa1f9ead03b4cccaff1e3390b8052b0f3)
- [bt_mcc_read_player_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga724ce71fc88f1ca4bcf209c92c177f36)
- [bt_mcc_read_icon_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga0e69de33c37957a2b5473df7d3c3f389)
- [bt_mcc_read_icon_url](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga38733456db6bc6558a511e104577c9c9)
- [bt_mcc_read_track_title](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga7dfa14489a4cea4b00053c9aa75cf373)
- [bt_mcc_read_track_duration](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga50a45f043bd2ae1741a120e02e9dc2f5)
- [bt_mcc_read_track_position](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf143098f5dfcfba01df3d6f06472779e)
- [bt_mcc_set_track_position](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gad324366d33bef6b1ed1c8fc881bf44cf)
- [bt_mcc_read_playback_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa566a4c42f0ab0ab6feddf4e25845609)
- [bt_mcc_set_playback_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga1382e5b6000896dc94f6489909301719)
- [bt_mcc_read_seeking_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga366fdfaa23cef9f1c3ba7ddd36a67658)
- [bt_mcc_read_segments_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga4cb0a95e91d3ec00ede64663a2b932f0)
- [bt_mcc_read_current_track_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga5b3a8fb8e8251cf005b34e47619ae7b9)
- [bt_mcc_set_current_track_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga8374ac230c5fe6b5a1bb7fa873fdeb49)
- [bt_mcc_read_next_track_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga11e4c02ba0b1fbc197aaf071b82a1eed)
- [bt_mcc_set_next_track_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gafeebcbb0c77d5d4acbe151fd9888d084)
- [bt_mcc_read_current_group_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga8cb43a6947df48113b082d8cc8ccf25c)
- [bt_mcc_set_current_group_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gae3f385811f852d584595c6e531556aed)
- [bt_mcc_read_parent_group_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga3ccd5961cc4c8d82fa988d300e12e1ae)
- [bt_mcc_read_playing_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga077a134ff1404fb76aa756a5531fd1d7)
- [bt_mcc_set_playing_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga05295649385c3a337401765627d09553)
- [bt_mcc_read_playing_orders_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaf61f6fcf3f96ccb6f5a72ffaad27dec4)
- [bt_mcc_read_media_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac1b440cfa54dd4b6e23bb47bf885f88d)
- [bt_mcc_send_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga3f4a538bcf436e4e80b73ed6e077dfa0)
- [bt_mcc_read_opcodes_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga692160554947f92e8c81912c5e597086)
- [bt_mcc_send_search](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga324161056e03195820bbd7cc77ff287d)
- [bt_mcc_read_search_results_obj_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga98814a516a027bdaa3250e93d55309fd)
- [bt_mcc_read_content_control_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga77cbf810c35d1a17efce1fae6a941963)
- [bt_mcc_otc_read_object_metadata](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gadf687cb26a6d00bca73e273da583df88)
- [bt_mcc_otc_read_icon_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaba527d8f0307ab11150a5434231c0e7e)
- [bt_mcc_otc_read_track_segments_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac22e840b65895aa018ab1b4535a87672)
- [bt_mcc_otc_read_current_track_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gac4b09a77df52d2681e7652591ca32bf8)
- [bt_mcc_otc_read_next_track_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga611c9edebff5b4347ad1241ffd19f49e)
- [bt_mcc_otc_read_current_group_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#ga4b1ebe682ad134795f8a1b494244f8b6)
- [bt_mcc_otc_read_parent_group_object](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gae001cb2d701457ce083aa8a0fd5ec518)
- [bt_ots_client](../bluetooth_service_model_reference/P137_bt_ots_client_结构体.md)
- [bt_mcc_otc_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html#gaa243806f65c4a37d41f25bcc4f1839fc)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [media_proxy.h](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_mcc_cb::set_playing_order](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a00a0ba5ed665ef7fc2ca861d985ccd64)
- [bt_mcc_cb::read_icon_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a00acb676c73ebbad2b0180b3e8373150)
- [bt_mcc_cb::otc_icon_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a054e0cfb27c01f43d499a2c44788cb73)
- [bt_mcc_cb::read_current_group_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a0e7757b6f911456feaca931cd33f117f)
- [bt_mcc_cb::otc_obj_selected](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a17ebc9dbddd714d99b599b2a683ab771)
- [bt_mcc_cb::send_search](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a1c7277f390f6b478090611be9e82a4f8)
- [bt_mcc_cb::otc_track_segments_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a2c1b570ce8d83c3f20eb99807263a5cd)
- [bt_mcc_cb::discover_mcs](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a2f48a0e0b891131347b0ddc2cb5a8ba7)
- [bt_mcc_cb::read_playing_order](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a3538beef41edd96b8557b43c1266078b)
- [bt_mcc_cb::read_media_state](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a38e4682608c7d7ff6c44431a6bdab3af)
- [bt_mcc_cb::read_track_title](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a3975e296b67eb244bf92254e9776ea3c)
- [bt_mcc_cb::read_current_track_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a46bd2c23d92d8362cdf9ad4862b78407)
- [bt_mcc_cb::read_playback_speed](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a47f8d92b18b0e4ffb3aacde05e7cb410)
- [bt_mcc_cb::set_next_track_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a4f2ea54d6c60beb28feab7b6453aec7c)
- [bt_mcc_cb::otc_next_track_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a52724924ab19f59cc936344ebe13d437)
- [bt_mcc_cb::read_next_track_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a540797123f8968b49a6e98b30ea534c8)
- [bt_mcc_cb::set_playback_speed](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a5f87b5d07241b4124911be0cd6c43b37)
- [bt_mcc_cb::read_seeking_speed](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a75c8e63baf45a119e9007f246362ab8d)
- [bt_mcc_cb::read_segments_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a810ceaee44fcbdec90a1ee227b6974df)
- [bt_mcc_cb::cmd_ntf](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a835f60ad32edc4311a624e779972f0d5)
- [bt_mcc_cb::read_track_duration](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a85268d9ce708aef01aa528aaedf0f7e0)
- [bt_mcc_cb::otc_parent_group_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a872d0322ba3889f1f7d32e8966b53624)
- [bt_mcc_cb::read_parent_group_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a87583247634728d3d9af7eb411d088a7)
- [bt_mcc_cb::read_icon_url](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a8c7b5954e286d074a94a39bee266082c)
- [bt_mcc_cb::send_cmd](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a90e62e90752087da36122a65f6c9ed4e)
- [bt_mcc_cb::read_playing_orders_supported](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a929d7b8fc925961048d5ff5e70a5126e)
- [bt_mcc_cb::search_ntf](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#a9f7f3424aa230a8752f40a40b82b0b66)
- [bt_mcc_cb::read_search_results_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#aaa2bdfb99e5cd7c2a0d0c800533e8491)
- [bt_mcc_cb::track_changed_ntf](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#abb7769b73564a22645bfe6b11f239637)
- [bt_mcc_cb::otc_current_group_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ac0e382f1117f983e7a2178fde274d460)
- [bt_mcc_cb::set_current_track_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ac9e182bbdd9671c5caee5bcd42198d90)
- [bt_mcc_cb::otc_current_track_object](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ad13669e60992a1a407534f387efd1da8)
- [bt_mcc_cb::read_track_position](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ad1636e717ef5039586b7a1462041e888)
- [bt_mcc_cb::read_opcodes_supported](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ad7ddcae67bf71030ac2d8438ac2e863f)
- [bt_mcc_cb::set_current_group_obj_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ad8d3eff0cc183797280c9f668a840add)
- [bt_mcc_cb::read_content_control_id](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#ae4d0e2e4df695352e8d2ed76db1f420e)
- [bt_mcc_cb::read_player_name](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#aeea1ef17b3b1e24c965d71f210952079)
- [bt_mcc_cb::otc_obj_metadata](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#af1c9664a2459550af0a6ed611fd17263)
- [bt_mcc_cb::set_track_position](../bluetooth_service_model_reference/P119_bt_mcc_cb_结构体.md#affa57da8f325dce8298d097af38d0d62)
- [mpl_search::search](../audio_video_model_reference/P040_mpl_search_结构体.md#a836bebfaadb56672a7e76c0ac2e450a9)

---

[上一章](P003_gpio_cmsdk_ahb.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_msi.h_源码浏览.md)
