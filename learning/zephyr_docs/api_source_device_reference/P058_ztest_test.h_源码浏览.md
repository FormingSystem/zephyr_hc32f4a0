---
id: learning.zephyr-docs.api-source-device-reference.page-58
title: ztest_test.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ztest__test_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_ztest\_test.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ztest__test_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ztest__test_8h.html)。

## 58.1\_原始可见代码（Source Code）

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
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
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
<a id="l00076"></a>
<a id="l00077"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00123"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00143"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00160"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="foldopen00183"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="foldopen00192"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="foldopen00246"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="foldopen00289"></a>
<a id="l00289"></a>
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
<a id="l00309"></a>
<a id="l00310"></a>
<a id="foldopen00315"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="foldopen00328"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00422"></a>
<a id="l00426"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00499"></a>
<a id="l00500"></a>
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
<a id="l00521"></a>
<a id="l00522"></a>
<a id="foldopen00529"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="foldopen00560"></a>
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
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="foldopen00601"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="foldopen00642"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="foldopen00678"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
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
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00728"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00744"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="foldopen00860"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00885"></a>
<a id="l00886"></a>
<a id="foldopen00896"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="foldopen00903"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00916"></a>
<a id="l00917"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00963"></a>
<a id="l00964"></a>
<a id="l00965"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="l00971"></a>
<a id="l00972"></a>
<a id="l00973"></a>
<a id="l00974"></a>
<a id="l00975"></a>
<a id="l00976"></a>
<a id="l00977"></a>
<a id="l00978"></a>
<a id="l00979"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00982"></a>
<a id="l00983"></a>
<a id="aapp__memdomain_8h_html"></a>
<a id="agroup__thread__stack__api_html_gab42c634630b892599bdf797e65563a83"></a>
<a id="agroup__ztest__test_html_ga0063907dd70b9eb817ea472162693ee4"></a>
<a id="agroup__ztest__test_html_ga085d30a04102ebb8c3f2206020723ee0"></a>
<a id="agroup__ztest__test_html_ga0edd9f03977918a4fe4f4ed1e59ef3e1"></a>
<a id="agroup__ztest__test_html_ga0f9eeb8ddae455c1e7cc7a388a7b013c"></a>
<a id="agroup__ztest__test_html_ga17537c79021fbc12e56b72ccec4b99c5"></a>
<a id="agroup__ztest__test_html_ga2090c493018a95112b89c5f83b5d8162"></a>
<a id="agroup__ztest__test_html_ga2c7d0aa85e7f320d582395c5ded90133"></a>
<a id="agroup__ztest__test_html_ga349fda278dff713debfd2a3b94b8b1eb"></a>
<a id="agroup__ztest__test_html_ga3adced2fdda96833e6b1ecbf3d61d446"></a>
<a id="agroup__ztest__test_html_ga5b6ba1f30dfeb11d48a176e8f3a31292"></a>
<a id="agroup__ztest__test_html_ga5dde8913cf45656bca8a48c825a95d59"></a>
<a id="agroup__ztest__test_html_ga7769b894fdac5283ac949ce8fceea0dd"></a>
<a id="agroup__ztest__test_html_ga9d7fcc3e316762a9a729f48e71819db7"></a>
<a id="agroup__ztest__test_html_gaa53486873430dd8fa978745d8a1d0686"></a>
<a id="agroup__ztest__test_html_gaafb3cba3a9637839952b2db2486ab88c"></a>
<a id="agroup__ztest__test_html_gabfd65eebc03c9064dcffdd47fa833961"></a>
<a id="agroup__ztest__test_html_gac2842295307e7286d256bb179be60b02"></a>
<a id="agroup__ztest__test_html_gac6b1f8b820cd682094b7aaeebdaa106e"></a>
<a id="agroup__ztest__test_html_gac7ddc33b5a0d11e2ffa0a564019c5e3d"></a>
<a id="agroup__ztest__test_html_gac8a204832c267fed047e7707b65be74d"></a>
<a id="agroup__ztest__test_html_gacd6eb423f54dce8544f7c3b1618c0374"></a>
<a id="agroup__ztest__test_html_gad5323aa82773dac33cf0930e9524420c"></a>
<a id="agroup__ztest__test_html_gada3b1fcfa71db1bf7787c03ff45256d5"></a>
<a id="agroup__ztest__test_html_gaf4dfaad1b5f1059e87f406979769aa26"></a>
<a id="agroup__ztest__test_html_gga5dde8913cf45656bca8a48c825a95d59a1dc3378deb96d78130b2ecc0cd966bd1"></a>
<a id="agroup__ztest__test_html_gga5dde8913cf45656bca8a48c825a95d59a46c899f020982afc47164237a36a1663"></a>
<a id="agroup__ztest__test_html_gga5dde8913cf45656bca8a48c825a95d59a78c54591383696b200d6a4582619b765"></a>
<a id="agroup__ztest__test_html_gga5dde8913cf45656bca8a48c825a95d59aa5a6af32f1f4bac30640934e1eb3b0bf"></a>
<a id="agroup__ztest__test_html_gga5dde8913cf45656bca8a48c825a95d59aaf847259cdce47813e155c3523e36901"></a>
<a id="agroup__ztest__test_html_gga5dde8913cf45656bca8a48c825a95d59ad5efde89d69e093341de2a6a823e3971"></a>
<a id="agroup__ztest__test_html_ggac2842295307e7286d256bb179be60b02a07327a99dd9daf709d9a28a5ea8316c4"></a>
<a id="agroup__ztest__test_html_ggac2842295307e7286d256bb179be60b02a8dac9ba9321cd8d0a3a61b52cbdb4cfc"></a>
<a id="agroup__ztest__test_html_ggac2842295307e7286d256bb179be60b02a92cec4e702d9d4502e02f76c7071211e"></a>
<a id="agroup__ztest__test_html_ggac2842295307e7286d256bb179be60b02aa29639fb74516d8d112b9dade2422888"></a>
<a id="agroup__ztest__test_html_ggac2842295307e7286d256bb179be60b02ac09ff18a766e298ede6f7746f4704c55"></a>
<a id="agroup__ztest__test_html_ggac2842295307e7286d256bb179be60b02af5927209b63a89467df81ad9de245b5e"></a>
<a id="agroup__ztest__test_html_ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d"></a>
<a id="agroup__ztest__test_html_ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a"></a>
<a id="ainit_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructk__mem__partition_html"></a>
<a id="astructztest__arch__api_html"></a>
<a id="astructztest__arch__api_html_a005bcb042aee46de9088b7527df49f9f"></a>
<a id="astructztest__arch__api_html_a427413d24056eb42d3a5302c28bd4329"></a>
<a id="astructztest__arch__api_html_a8334b1ecc7efc93245fe35c7c1da728a"></a>
<a id="astructztest__expected__result__entry_html"></a>
<a id="astructztest__expected__result__entry_html_a37352688340aa1c49a7967d5b568c9a1"></a>
<a id="astructztest__expected__result__entry_html_a74524b4da8fddbd64d526cfc5df72743"></a>
<a id="astructztest__expected__result__entry_html_a92ada50dadf26e5c59e4e529afffd882"></a>
<a id="astructztest__param__inst_html"></a>
<a id="astructztest__param__inst_html_a41e6fd5db549443d51a6ab85277223d6"></a>
<a id="astructztest__param__inst_html_a53ea28da5d3847eaa6f0cc9b61b32577"></a>
<a id="astructztest__param__inst_html_aa4b24e28c5f82954784bf2784b81fced"></a>
<a id="astructztest__param__inst_html_aae7c3351357b0783258915ba73a7a173"></a>
<a id="astructztest__param__values_html"></a>
<a id="astructztest__param__values_html_a23d230232ece43bb6bdecacc7a7fe3c7"></a>
<a id="astructztest__param__values_html_a4c128cca687f2952d34e75c2e901c8bc"></a>
<a id="astructztest__param__values_html_a7eb7826cc6c2ebdaba59b7c530227b8e"></a>
<a id="astructztest__param__values_html_a7f3210eb76bbf05f4847420cbe56f91e"></a>
<a id="astructztest__param__values_html_a93659e0443d1429a090eed95c776f3f1"></a>
<a id="astructztest__suite__node_html"></a>
<a id="astructztest__suite__node_html_a0a1eeaa1f0b90918e6b87e1d37d84eef"></a>
<a id="astructztest__suite__node_html_a0a30e674f7a071e43e1ff1e190bf2020"></a>
<a id="astructztest__suite__node_html_a1d80587f1e1c841d6c4d43b5fe3c9b4d"></a>
<a id="astructztest__suite__node_html_a46ec271d4a7625b01daac27899d5eae4"></a>
<a id="astructztest__suite__node_html_a55f700029b3f6dbfd1bd9ce7df6808e4"></a>
<a id="astructztest__suite__node_html_a97f7e248b5fe9548010d659816f8d295"></a>
<a id="astructztest__suite__node_html_ac0a66cf7eb644fbc7c161ee61c854385"></a>
<a id="astructztest__suite__stats_html"></a>
<a id="astructztest__suite__stats_html_a04d888a17a39bdf62f1b935968d58b92"></a>
<a id="astructztest__suite__stats_html_a58f7c9379bc9bf18c2184fdcd2bbff8c"></a>
<a id="astructztest__suite__stats_html_a94a4d70901b2d2b57cbaf03b9c6d21a9"></a>
<a id="astructztest__unit__test__stats_html"></a>
<a id="astructztest__unit__test__stats_html_a1f1cc422307e6bd7875e42c7205e47d7"></a>
<a id="astructztest__unit__test__stats_html_a21c2c8a05524e673567c7ee3d809ad25"></a>
<a id="astructztest__unit__test__stats_html_a5370f1797292d3fe575166e161dee43f"></a>
<a id="astructztest__unit__test__stats_html_ac24d475c52c4ea7a0de4e99f2d76d1a1"></a>
<a id="astructztest__unit__test__stats_html_addbacc4315f502b2c69ee5ebf5884ad6"></a>
<a id="astructztest__unit__test_html"></a>
<a id="astructztest__unit__test_html_a1176caba02accac7bd2eb02c715a0d38"></a>
<a id="astructztest__unit__test_html_a3b7014bbb299c4aeb6717806e602f38a"></a>
<a id="astructztest__unit__test_html_a5fe0425dde921834acb2c0e387bcc524"></a>
<a id="astructztest__unit__test_html_a9c151bd9e948788c861503b53c52b24d"></a>
<a id="astructztest__unit__test_html_ac94283459e71728180420d66b3a4a53a"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="aztest__test_8h_html_a846fcbfbda9794cba2dcf1c34bd9be1b"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_TESTSUITE_ZTEST_TEST_H_
#define ZEPHYR_TESTSUITE_ZTEST_TEST_H_

#include <zephyr/app_memory/app_memdomain.h>
#include <zephyr/init.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/util.h>
#include <stdbool.h>



#if defined(CONFIG_USERSPACE)
#define __USERSPACE_FLAGS (K_USER)
#else
#define __USERSPACE_FLAGS (0)
#endif

#ifdef __cplusplus
extern "C" {
#endif

enum ztest_expected_result {
        ZTEST_EXPECTED_RESULT_FAIL = 0,
        ZTEST_EXPECTED_RESULT_SKIP,
};

struct ztest_expected_result_entry {
        const char *test_suite_name;
        const char *test_name;
        enum ztest_expected_result expected_result;
};

extern struct ztest_expected_result_entry _ztest_expected_result_entry_list_start[];
extern struct ztest_expected_result_entry _ztest_expected_result_entry_list_end[];

#define __ZTEST_EXPECT(_suite_name, _test_name, expectation)                                       \
        static const STRUCT_SECTION_ITERABLE(                                                      \
                ztest_expected_result_entry,                                                       \
                UTIL_CAT(UTIL_CAT(z_ztest_expected_result_, _suite_name), _test_name)) = {         \
                        .test_suite_name = STRINGIFY(_suite_name),                                 \
                        .test_name = STRINGIFY(_test_name),                                        \
                        .expected_result = expectation,                                            \
        }

#define ZTEST_EXPECT_FAIL(_suite_name, _test_name)                                                 \
        __ZTEST_EXPECT(_suite_name, _test_name, ZTEST_EXPECTED_RESULT_FAIL)

#define ZTEST_EXPECT_SKIP(_suite_name, _test_name)                                                 \
        __ZTEST_EXPECT(_suite_name, _test_name, ZTEST_EXPECTED_RESULT_SKIP)

struct ztest_unit_test {
        const char *test_suite_name;
        const char *name;
        void (*test)(void *data);
        uint32_t thread_options;

        struct ztest_unit_test_stats *const stats;
};

struct ztest_param_values {
        const void *values;
        size_t count;
        size_t elem_size;
        const char *(*name_cb)(size_t index, const void *value);
        void (*value_at_cb)(size_t index, void *out);
        void (*setup_cb)(void);
};

struct ztest_param_inst {
        const char *test_suite_name;
        const char *test_name;
        const char *instance_name;
        const struct ztest_param_values *values;
};

extern struct ztest_unit_test _ztest_unit_test_list_start[];
extern struct ztest_unit_test _ztest_unit_test_list_end[];
extern struct ztest_param_inst _ztest_param_inst_list_start[];
extern struct ztest_param_inst _ztest_param_inst_list_end[];
#define ZTEST_TEST_COUNT (_ztest_unit_test_list_end - _ztest_unit_test_list_start)
#define ZTEST_PARAM_INST_COUNT (_ztest_param_inst_list_end - _ztest_param_inst_list_start)

struct ztest_suite_stats {
        uint32_t run_count;
        uint32_t skip_count;
        uint32_t fail_count;
};

struct ztest_unit_test_stats {
        uint32_t run_count;
        uint32_t skip_count;
        uint32_t fail_count;
        uint32_t pass_count;
        uint32_t duration_worst_ms;
};

typedef void *(*ztest_suite_setup_t)(void);

typedef void (*ztest_suite_before_t)(void *fixture);

typedef void (*ztest_suite_after_t)(void *fixture);

typedef void (*ztest_suite_teardown_t)(void *fixture);

typedef bool (*ztest_suite_predicate_t)(const void *global_state);

struct ztest_suite_node {
        const char *const name;

        const ztest_suite_setup_t setup;

        const ztest_suite_before_t before;

        const ztest_suite_after_t after;

        const ztest_suite_teardown_t teardown;

        const ztest_suite_predicate_t predicate;

        struct ztest_suite_stats *const stats;
};

extern struct ztest_suite_node _ztest_suite_node_list_start[];
extern struct ztest_suite_node _ztest_suite_node_list_end[];

#define ZTEST_SUITE_COUNT (_ztest_suite_node_list_end - _ztest_suite_node_list_start)

#define ZTEST_SUITE(SUITE_NAME, PREDICATE, setup_fn, before_fn, after_fn, teardown_fn)             \
        struct ztest_suite_stats UTIL_CAT(z_ztest_suite_node_stats_, SUITE_NAME);                  \
        static const STRUCT_SECTION_ITERABLE(ztest_suite_node,                                     \
                                             UTIL_CAT(z_ztest_test_node_, SUITE_NAME)) = {         \
                .name = STRINGIFY(SUITE_NAME),                                                     \
                .setup = (setup_fn),                                                               \
                .before = (before_fn),                                                             \
                .after = (after_fn),                                                               \
                .teardown = (teardown_fn),                                                         \
                .predicate = PREDICATE,                                                            \
                .stats = &UTIL_CAT(z_ztest_suite_node_stats_, SUITE_NAME),             \
        }

void ztest_run_all(const void *state, bool shuffle, int suite_iter, int case_iter);

enum ztest_result {
        ZTEST_RESULT_PENDING,
        ZTEST_RESULT_PASS,
        ZTEST_RESULT_FAIL,
        ZTEST_RESULT_SKIP,
        ZTEST_RESULT_SUITE_SKIP,
        ZTEST_RESULT_SUITE_FAIL,
};

enum ztest_phase {
        TEST_PHASE_SETUP,
        TEST_PHASE_BEFORE,
        TEST_PHASE_TEST,
        TEST_PHASE_AFTER,
        TEST_PHASE_TEARDOWN,
        TEST_PHASE_FRAMEWORK,
};


#ifdef ZTEST_UNITTEST
int z_impl_ztest_run_test_suites(const void *state, bool shuffle,
                                int suite_iter, int case_iter);

static inline int ztest_run_test_suites(const void *state, bool shuffle,
                                int suite_iter, int case_iter)
{
        return z_impl_ztest_run_test_suites(state, shuffle, suite_iter, case_iter);
}

#else
__syscall int ztest_run_test_suites(const void *state, bool shuffle,
                                int suite_iter, int case_iter);
#endif

#ifdef ZTEST_UNITTEST
void z_impl___ztest_set_test_result(enum ztest_result new_result);
static inline void __ztest_set_test_result(enum ztest_result new_result)
{
        z_impl___ztest_set_test_result(new_result);
}

void z_impl___ztest_set_test_phase(enum ztest_phase new_phase);
static inline void __ztest_set_test_phase(enum ztest_phase new_phase)
{
        z_impl___ztest_set_test_phase(new_phase);
}
#else
__syscall void __ztest_set_test_result(enum ztest_result new_result);
__syscall void __ztest_set_test_phase(enum ztest_phase new_phase);
#endif


void ztest_verify_all_test_suites_ran(void);

int z_ztest_run_test_suite(const char *name, bool shuffle, int suite_iter,
                        int case_iter, void *param);

struct ztest_unit_test *z_ztest_get_next_test(const char *suite, struct ztest_unit_test *prev);

/* definitions for use with testing application shared memory   */
#ifdef CONFIG_USERSPACE
#define ZTEST_DMEM K_APP_DMEM(ztest_mem_partition)
#define ZTEST_BMEM K_APP_BMEM(ztest_mem_partition)
#define ZTEST_SECTION K_APP_DMEM_SECTION(ztest_mem_partition)
extern struct k_mem_partition ztest_mem_partition;
#else
#define ZTEST_DMEM
#define ZTEST_BMEM
#define ZTEST_SECTION .data
#endif

void ztest_test_fail(void);

void ztest_test_pass(void);

void ztest_test_skip(void);


void ztest_skip_failed_assumption(void);

const void *ztest_get_current_param(void);

size_t ztest_get_current_param_index(void);

size_t ztest_get_current_param_size(void);

bool ztest_has_current_param(void);

#define ZTEST_GET_PARAM_PTR(type) ((const type *)ztest_get_current_param())

#define ZTEST_GET_PARAM(type) (*ZTEST_GET_PARAM_PTR(type))

#define ZTEST_DEFINE_PARAM_VALUES(name_, type_, ...)                                         \
        static const type_ z_ztest_param_arr_##name_[] = {__VA_ARGS__};                     \
        static const struct ztest_param_values name_ = {                                     \
                .values       = z_ztest_param_arr_##name_,                                   \
                .count        = ARRAY_SIZE(z_ztest_param_arr_##name_),                       \
                .elem_size    = sizeof(type_),                                                \
                .name_cb      = NULL,                                                        \
                .value_at_cb  = NULL,                                                        \
                .setup_cb     = NULL,                                                        \
        }

#define ZTEST_DEFINE_PARAM_VALUES_ARRAY(name_, array_)                                       \
        static const struct ztest_param_values name_ = {                                     \
                .values      = (array_),                                                     \
                .count       = ARRAY_SIZE(array_),                                           \
                .elem_size   = sizeof((array_)[0]),                                          \
                .name_cb     = NULL,                                                         \
                .value_at_cb = NULL,                                                         \
                .setup_cb    = NULL,                                                         \
        }

#define ZTEST_DEFINE_PARAM_RANGE(name_, type_, begin_, end_, step_)                          \
        BUILD_ASSERT((end_) > (begin_), "ZTEST_DEFINE_PARAM_RANGE: end must be > begin"); \
        BUILD_ASSERT((step_) > 0, "ZTEST_DEFINE_PARAM_RANGE: step must be > 0");          \
        BUILD_ASSERT(sizeof(type_) <= 16U,                                                   \
                     "ZTEST_DEFINE_PARAM_RANGE: type too large for scratch buffer");        \
        static void z_ztest_range_value_at_##name_(size_t z_idx_, void *z_out_)             \
        {                                                                                    \
                type_ z_val_ = (type_)(begin_) + (type_)(step_) * (type_)(z_idx_);         \
                *(type_ *)z_out_ = z_val_;                                                   \
        }                                                                                    \
        static const struct ztest_param_values name_ = {                                     \
                .values      = NULL,                                                         \
                .count       = (size_t)(((end_) - (begin_) - 1) / (step_) + 1),             \
                .elem_size   = sizeof(type_),                                                \
                .name_cb     = NULL,                                                         \
                .value_at_cb = z_ztest_range_value_at_##name_,                              \
                .setup_cb    = NULL,                                                         \
        }

#define ZTEST_DEFINE_PARAM_GENERATOR(name_, type_, count_, gen_cb_)                          \
        BUILD_ASSERT(sizeof(type_) <= 16U,                                                   \
                     "ZTEST_DEFINE_PARAM_GENERATOR: type too large for scratch buffer");     \
        static const struct ztest_param_values name_ = {                                     \
                .values      = NULL,                                                         \
                .count       = (count_),                                                     \
                .elem_size   = sizeof(type_),                                                \
                .name_cb     = NULL,                                                         \
                .value_at_cb = (gen_cb_),                                                    \
                .setup_cb    = NULL,                                                         \
        }

#define ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP(name_, type_, count_, setup_cb_, gen_cb_)    \
        BUILD_ASSERT(sizeof(type_) <= 16U,                                                   \
                     "ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP: type too large");             \
        static const struct ztest_param_values name_ = {                                     \
                .values      = NULL,                                                         \
                .count       = (count_),                                                     \
                .elem_size   = sizeof(type_),                                                \
                .name_cb     = NULL,                                                         \
                .value_at_cb = (gen_cb_),                                                    \
                .setup_cb    = (setup_cb_),                                                  \
        }

/* Note: all parameters carry a trailing underscore to avoid name collisions
 * with the struct fields of ztest_param_inst (e.g. a parameter named
 * 'instance_name' would cause the preprocessor to replace the token inside
 * the '.instance_name' designator, producing the invalid '.ints').
 */
#define ZTEST_INSTANTIATE_TEST_SUITE_P(inst_, suite_, fn_, param_values_name_)               \
        static const STRUCT_SECTION_ITERABLE(                                                \
                ztest_param_inst,                                                            \
                UTIL_CAT(UTIL_CAT(z_ztest_param_inst_, suite_),                              \
                         UTIL_CAT(_, UTIL_CAT(fn_, UTIL_CAT(_, inst_))))) = {               \
                .test_suite_name = STRINGIFY(suite_),                                        \
                .test_name       = STRINGIFY(fn_),                                           \
                .instance_name   = STRINGIFY(inst_),                                         \
                .values          = &(param_values_name_),                                    \
        }

#define Z_TEST_P(suite, fn, t_options) \
        struct ztest_unit_test_stats z_ztest_unit_test_stats_##suite##_##fn; \
        static void _##suite##_##fn##_wrapper(void *wrapper_data); \
        /* data carries the suite fixture from setup(); use             */ \
        /* ztest_get_current_param() / ZTEST_GET_PARAM() for the value. */ \
        static void suite##_##fn(void *data); \
        static STRUCT_SECTION_ITERABLE(ztest_unit_test, z_ztest_unit_test__##suite##__##fn) = { \
                .test_suite_name = STRINGIFY(suite), \
                .name = STRINGIFY(fn), \
                .test = (_##suite##_##fn##_wrapper), \
                .thread_options = t_options, \
                .stats = &z_ztest_unit_test_stats_##suite##_##fn \
        }; \
        static void _##suite##_##fn##_wrapper(void *wrapper_data) \
        { \
                 suite##_##fn(wrapper_data); \
        } \
        static inline void suite##_##fn(void *data)


#define ZTEST_P(suite, fn) Z_TEST_P(suite, fn, 0)

#define ZTEST_USER_P(suite, fn) Z_TEST_P(suite, fn, K_USER)

#define Z_TEST(suite, fn, t_options, use_fixture)                                                  \
        struct ztest_unit_test_stats z_ztest_unit_test_stats_##suite##_##fn;                       \
        static void _##suite##_##fn##_wrapper(void *wrapper_data);                                 \
        static void suite##_##fn(                                                                  \
                COND_CODE_1(use_fixture, (struct suite##_fixture *fixture), (void)));              \
        static STRUCT_SECTION_ITERABLE(ztest_unit_test, z_ztest_unit_test__##suite##__##fn) = {    \
                .test_suite_name = STRINGIFY(suite),                                               \
                .name = STRINGIFY(fn),                                                             \
                .test = (_##suite##_##fn##_wrapper),                                               \
                .thread_options = t_options,                                                       \
                .stats = &z_ztest_unit_test_stats_##suite##_##fn                                   \
        };                                                                                         \
        static void _##suite##_##fn##_wrapper(void *wrapper_data)                                  \
        {                                                                                          \
                COND_CODE_1(use_fixture, (suite##_##fn((struct suite##_fixture *)wrapper_data);),  \
                            (ARG_UNUSED(wrapper_data); suite##_##fn();))                           \
        }                                                                                          \
        static inline void suite##_##fn(                                                           \
                COND_CODE_1(use_fixture, (struct suite##_fixture *fixture), (void)))

#define Z_ZTEST(suite, fn, t_options) Z_TEST(suite, fn, t_options, 0)
#define Z_ZTEST_F(suite, fn, t_options) Z_TEST(suite, fn, t_options, 1)

#define Z_TEST_SKIP() do {                                                                         \
        ztest_test_skip();                                                                         \
        return;                                                                                    \
} while (0)

#define Z_TEST_SKIP_IFDEF(config) COND_CODE_1(config, (Z_TEST_SKIP()), ())

#define Z_TEST_SKIP_IFNDEF(config) COND_CODE_1(config, (), (Z_TEST_SKIP()))

#define ZTEST(suite, fn) Z_ZTEST(suite, fn, 0)

#define ZTEST_USER(suite, fn) Z_ZTEST(suite, fn, K_USER)

#define ZTEST_F(suite, fn) Z_ZTEST_F(suite, fn, 0)

#define ZTEST_USER_F(suite, fn) Z_ZTEST_F(suite, fn, K_USER)

typedef void (*ztest_rule_cb)(const struct ztest_unit_test *test, void *data);

struct ztest_test_rule {
        ztest_rule_cb before_each;
        ztest_rule_cb after_each;
};

#define ZTEST_RULE(name, before_each_fn, after_each_fn)                                            \
        static STRUCT_SECTION_ITERABLE(ztest_test_rule, z_ztest_test_rule_##name) = {              \
                .before_each = (before_each_fn),                                                   \
                .after_each = (after_each_fn),                                                     \
        }

extern struct ztest_test_rule _ztest_test_rule_list_start[];
extern struct ztest_test_rule _ztest_test_rule_list_end[];

void ztest_simple_1cpu_before(void *data);

void ztest_simple_1cpu_after(void *data);

#define ztest_run_test_suite(suite, shuffle, suite_iter, case_iter, param) \
        z_ztest_run_test_suite(STRINGIFY(suite), shuffle, suite_iter, case_iter, param)

struct ztest_arch_api {
        void (*run_all)(const void *state, bool shuffle, int suite_iter, int case_iter);
        bool (*should_suite_run)(const void *state, struct ztest_suite_node *suite);
        bool (*should_test_run)(const char *suite, const char *test);
};

extern ZTEST_DMEM const struct ztest_arch_api ztest_api;

void z_ztest_run_all(const void *state, bool shuffle, int suite_iter, int case_iter);

bool z_ztest_should_suite_run(const void *state, struct ztest_suite_node *suite);

bool z_ztest_should_test_run(const char *suite, const char *test);

K_THREAD_STACK_DECLARE(ztest_thread_stack,
                       CONFIG_ZTEST_STACK_SIZE + CONFIG_TEST_EXTRA_STACK_SIZE);


__syscall void z_test_1cpu_start(void);
__syscall void z_test_1cpu_stop(void);

__syscall void sys_clock_tick_set(uint64_t tick);

#ifdef __cplusplus
}
#endif

#ifndef ZTEST_UNITTEST
#include <zephyr/syscalls/ztest_test.h>
#endif

#endif /* ZEPHYR_TESTSUITE_ZTEST_TEST_H_ */
```

## 58.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 417 行

供测试应用程序共享内存（Testing Application Shared Memory）使用的定义。

### 注释 3：原第 673 行

注意（Note）：所有参数名都带有尾部下划线（Trailing Underscore），以避免与 `ztest_param_inst` 的结构体字段（Struct Fields）发生名称冲突。例如，若参数名为 `instance_name`，预处理器（Preprocessor）会替换 `.instance_name` 指定符（Designator）中的同名记号，生成无效的 `.ints`。

### 注释 4：原第 692 行

`data` 携带由 `setup()` 提供的测试套件夹具（Suite Fixture）；获取参数值时使用下文所示接口。

### 注释 5：原第 693 行

使用 `ztest_get_current_param()`／`ZTEST_GET_PARAM()` 获取参数值（Value）。

### 注释 6：原第 983 行

头文件保护宏（Header guard）标记：`ZEPHYR_TESTSUITE_ZTEST_TEST_H_`。

## 58.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ztest__test_8h.html)
- [zephyr/app_memory/app_memdomain.h](../memory_domain_reference/P009_应用内存域头文件参考.md)
- [zephyr/init.h](../device_reference/P009_系统初始化头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [ztest_expected_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaf4dfaad1b5f1059e87f406979769aa26)
- [ZTEST_EXPECTED_RESULT_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d)
- [ZTEST_EXPECTED_RESULT_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a)
- [ztest_expected_result_entry](../hardware/P509_测试预期结果记录.md)
- [test_suite_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__expected__result__entry.html#a37352688340aa1c49a7967d5b568c9a1)
- [test_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__expected__result__entry.html#a92ada50dadf26e5c59e4e529afffd882)
- [expected_result](https://docs.zephyrproject.org/latest/doxygen/html/structztest__expected__result__entry.html#a74524b4da8fddbd64d526cfc5df72743)
- [ztest_unit_test](../hardware/P510_单元测试记录结构.md)
- [test_suite_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test.html#ac94283459e71728180420d66b3a4a53a)
- [name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test.html#a1176caba02accac7bd2eb02c715a0d38)
- [test](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test.html#a5fe0425dde921834acb2c0e387bcc524)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [thread_options](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test.html#a9c151bd9e948788c861503b53c52b24d)
- [ztest_unit_test_stats](../hardware/P514_单元测试统计结构.md)
- [stats](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test.html#a3b7014bbb299c4aeb6717806e602f38a)
- [ztest_param_values](../hardware/P511_测试参数集合结构.md)
- [values](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__values.html#a23d230232ece43bb6bdecacc7a7fe3c7)
- [count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__values.html#a4c128cca687f2952d34e75c2e901c8bc)
- [elem_size](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__values.html#a93659e0443d1429a090eed95c776f3f1)
- [value_at_cb](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__values.html#a7f3210eb76bbf05f4847420cbe56f91e)
- [setup_cb](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__values.html#a7eb7826cc6c2ebdaba59b7c530227b8e)
- [ztest_param_inst](../hardware/P512_参数化测试注册结构.md)
- [test_suite_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__inst.html#a53ea28da5d3847eaa6f0cc9b61b32577)
- [test_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__inst.html#aa4b24e28c5f82954784bf2784b81fced)
- [instance_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__inst.html#a41e6fd5db549443d51a6ab85277223d6)
- [values](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__inst.html#aae7c3351357b0783258915ba73a7a173)
- [ztest_suite_stats](../hardware/P513_测试套件统计结构.md)
- [run_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__stats.html#a94a4d70901b2d2b57cbaf03b9c6d21a9)
- [skip_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__stats.html#a04d888a17a39bdf62f1b935968d58b92)
- [fail_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__stats.html#a58f7c9379bc9bf18c2184fdcd2bbff8c)
- [run_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test__stats.html#a1f1cc422307e6bd7875e42c7205e47d7)
- [skip_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test__stats.html#a5370f1797292d3fe575166e161dee43f)
- [fail_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test__stats.html#addbacc4315f502b2c69ee5ebf5884ad6)
- [pass_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test__stats.html#a21c2c8a05524e673567c7ee3d809ad25)
- [duration_worst_ms](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test__stats.html#ac24d475c52c4ea7a0de4e99f2d76d1a1)
- [ztest_suite_before_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac8a204832c267fed047e7707b65be74d)
- [ztest_suite_after_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0f9eeb8ddae455c1e7cc7a388a7b013c)
- [ztest_suite_teardown_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga7769b894fdac5283ac949ce8fceea0dd)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [ztest_suite_predicate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gad5323aa82773dac33cf0930e9524420c)
- [ztest_suite_node](../hardware/P515_测试套件节点结构.md)
- [name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a55f700029b3f6dbfd1bd9ce7df6808e4)
- [ztest_suite_setup_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0063907dd70b9eb817ea472162693ee4)
- [setup](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a0a30e674f7a071e43e1ff1e190bf2020)
- [before](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a0a1eeaa1f0b90918e6b87e1d37d84eef)
- [after](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a46ec271d4a7625b01daac27899d5eae4)
- [teardown](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a97f7e248b5fe9548010d659816f8d295)
- [predicate](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#ac0a66cf7eb644fbc7c161ee61c854385)
- [stats](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a1d80587f1e1c841d6c4d43b5fe3c9b4d)
- [ztest_run_all](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac6b1f8b820cd682094b7aaeebdaa106e)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [ztest_result](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac2842295307e7286d256bb179be60b02)
- [ZTEST_RESULT_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02a8dac9ba9321cd8d0a3a61b52cbdb4cfc)
- [ZTEST_RESULT_PASS](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02a92cec4e702d9d4502e02f76c7071211e)
- [ZTEST_RESULT_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02aa29639fb74516d8d112b9dade2422888)
- [ZTEST_RESULT_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02a07327a99dd9daf709d9a28a5ea8316c4)
- [ZTEST_RESULT_SUITE_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02af5927209b63a89467df81ad9de245b5e)
- [ZTEST_RESULT_SUITE_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ggac2842295307e7286d256bb179be60b02ac09ff18a766e298ede6f7746f4704c55)
- [ztest_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga5dde8913cf45656bca8a48c825a95d59)
- [TEST_PHASE_SETUP](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59aa5a6af32f1f4bac30640934e1eb3b0bf)
- [TEST_PHASE_BEFORE](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59a78c54591383696b200d6a4582619b765)
- [TEST_PHASE_TEST](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59a1dc3378deb96d78130b2ecc0cd966bd1)
- [TEST_PHASE_AFTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59a46c899f020982afc47164237a36a1663)
- [TEST_PHASE_TEARDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59aaf847259cdce47813e155c3523e36901)
- [TEST_PHASE_FRAMEWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gga5dde8913cf45656bca8a48c825a95d59ad5efde89d69e093341de2a6a823e3971)
- [ztest_run_test_suites](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaafb3cba3a9637839952b2db2486ab88c)
- [ztest_verify_all_test_suites_ran](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga349fda278dff713debfd2a3b94b8b1eb)
- [k_mem_partition](../memory_domain_reference/P005_内存分区结构.md)
- [ztest_mem_partition](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga3adced2fdda96833e6b1ecbf3d61d446)
- [ztest_test_fail](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gacd6eb423f54dce8544f7c3b1618c0374)
- [ztest_test_pass](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga085d30a04102ebb8c3f2206020723ee0)
- [ztest_test_skip](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gada3b1fcfa71db1bf7787c03ff45256d5)
- [ztest_skip_failed_assumption](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga17537c79021fbc12e56b72ccec4b99c5)
- [ztest_get_current_param](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga9d7fcc3e316762a9a729f48e71819db7)
- [ztest_get_current_param_index](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga0edd9f03977918a4fe4f4ed1e59ef3e1)
- [ztest_get_current_param_size](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga5b6ba1f30dfeb11d48a176e8f3a31292)
- [ztest_has_current_param](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gabfd65eebc03c9064dcffdd47fa833961)
- [ztest_rule_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga2090c493018a95112b89c5f83b5d8162)
- [ztest_simple_1cpu_before](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gac7ddc33b5a0d11e2ffa0a564019c5e3d)
- [ztest_simple_1cpu_after](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#gaa53486873430dd8fa978745d8a1d0686)
- [ztest_arch_api](../hardware/P516_测试架构后端接口.md)
- [run_all](https://docs.zephyrproject.org/latest/doxygen/html/structztest__arch__api.html#a005bcb042aee46de9088b7527df49f9f)
- [should_suite_run](https://docs.zephyrproject.org/latest/doxygen/html/structztest__arch__api.html#a427413d24056eb42d3a5302c28bd4329)
- [should_test_run](https://docs.zephyrproject.org/latest/doxygen/html/structztest__arch__api.html#a8334b1ecc7efc93245fe35c7c1da728a)
- [ZTEST_DMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__test.html#ga2c7d0aa85e7f320d582395c5ded90133)
- [K_THREAD_STACK_DECLARE](../thread_stack_reference/P001_线程栈接口.md#gab42c634630b892599bdf797e65563a83)
- [sys_clock_tick_set](https://docs.zephyrproject.org/latest/doxygen/html/ztest__test_8h.html#a846fcbfbda9794cba2dcf1c34bd9be1b)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [app_memdomain.h](../memory_domain_reference/P009_应用内存域头文件参考.md)
- [init.h](../device_reference/P009_系统初始化头文件参考.md)
- [ztest_arch_api::run_all](https://docs.zephyrproject.org/latest/doxygen/html/structztest__arch__api.html#a005bcb042aee46de9088b7527df49f9f)
- [ztest_arch_api::should_suite_run](https://docs.zephyrproject.org/latest/doxygen/html/structztest__arch__api.html#a427413d24056eb42d3a5302c28bd4329)
- [ztest_arch_api::should_test_run](https://docs.zephyrproject.org/latest/doxygen/html/structztest__arch__api.html#a8334b1ecc7efc93245fe35c7c1da728a)
- [ztest_expected_result_entry::test_suite_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__expected__result__entry.html#a37352688340aa1c49a7967d5b568c9a1)
- [ztest_expected_result_entry::expected_result](https://docs.zephyrproject.org/latest/doxygen/html/structztest__expected__result__entry.html#a74524b4da8fddbd64d526cfc5df72743)
- [ztest_expected_result_entry::test_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__expected__result__entry.html#a92ada50dadf26e5c59e4e529afffd882)
- [ztest_param_inst::instance_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__inst.html#a41e6fd5db549443d51a6ab85277223d6)
- [ztest_param_inst::test_suite_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__inst.html#a53ea28da5d3847eaa6f0cc9b61b32577)
- [ztest_param_inst::test_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__inst.html#aa4b24e28c5f82954784bf2784b81fced)
- [ztest_param_inst::values](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__inst.html#aae7c3351357b0783258915ba73a7a173)
- [ztest_param_values::values](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__values.html#a23d230232ece43bb6bdecacc7a7fe3c7)
- [ztest_param_values::count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__values.html#a4c128cca687f2952d34e75c2e901c8bc)
- [ztest_param_values::setup_cb](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__values.html#a7eb7826cc6c2ebdaba59b7c530227b8e)
- [ztest_param_values::value_at_cb](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__values.html#a7f3210eb76bbf05f4847420cbe56f91e)
- [ztest_param_values::elem_size](https://docs.zephyrproject.org/latest/doxygen/html/structztest__param__values.html#a93659e0443d1429a090eed95c776f3f1)
- [ztest_suite_node::before](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a0a1eeaa1f0b90918e6b87e1d37d84eef)
- [ztest_suite_node::setup](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a0a30e674f7a071e43e1ff1e190bf2020)
- [ztest_suite_node::stats](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a1d80587f1e1c841d6c4d43b5fe3c9b4d)
- [ztest_suite_node::after](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a46ec271d4a7625b01daac27899d5eae4)
- [ztest_suite_node::name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a55f700029b3f6dbfd1bd9ce7df6808e4)
- [ztest_suite_node::teardown](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#a97f7e248b5fe9548010d659816f8d295)
- [ztest_suite_node::predicate](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__node.html#ac0a66cf7eb644fbc7c161ee61c854385)
- [ztest_suite_stats::skip_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__stats.html#a04d888a17a39bdf62f1b935968d58b92)
- [ztest_suite_stats::fail_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__stats.html#a58f7c9379bc9bf18c2184fdcd2bbff8c)
- [ztest_suite_stats::run_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__suite__stats.html#a94a4d70901b2d2b57cbaf03b9c6d21a9)
- [ztest_unit_test_stats::run_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test__stats.html#a1f1cc422307e6bd7875e42c7205e47d7)
- [ztest_unit_test_stats::pass_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test__stats.html#a21c2c8a05524e673567c7ee3d809ad25)
- [ztest_unit_test_stats::skip_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test__stats.html#a5370f1797292d3fe575166e161dee43f)
- [ztest_unit_test_stats::duration_worst_ms](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test__stats.html#ac24d475c52c4ea7a0de4e99f2d76d1a1)
- [ztest_unit_test_stats::fail_count](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test__stats.html#addbacc4315f502b2c69ee5ebf5884ad6)
- [ztest_unit_test::name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test.html#a1176caba02accac7bd2eb02c715a0d38)
- [ztest_unit_test::stats](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test.html#a3b7014bbb299c4aeb6717806e602f38a)
- [ztest_unit_test::test](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test.html#a5fe0425dde921834acb2c0e387bcc524)
- [ztest_unit_test::thread_options](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test.html#a9c151bd9e948788c861503b53c52b24d)
- [ztest_unit_test::test_suite_name](https://docs.zephyrproject.org/latest/doxygen/html/structztest__unit__test.html#ac94283459e71728180420d66b3a4a53a)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P057_ztest_assert.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P059_ztress.h_源码浏览.md)
