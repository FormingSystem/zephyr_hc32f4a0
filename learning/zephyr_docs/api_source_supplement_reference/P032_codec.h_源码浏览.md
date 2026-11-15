---
id: learning.zephyr-docs.api-source-supplement-reference.page-32
title: codec.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/codec_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_codec.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/codec_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/codec_8h.html)。

## 32.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00043"></a>
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
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="foldopen00158"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="foldopen00167"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="foldopen00191"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="foldopen00199"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="foldopen00208"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00259"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="foldopen00355"></a>
<a id="l00355"></a>
<a id="l00359"></a>
<a id="l00363"></a>
<a id="l00367"></a>
<a id="l00371"></a>
<a id="l00375"></a>
<a id="l00379"></a>
<a id="l00383"></a>
<a id="l00387"></a>
<a id="l00391"></a>
<a id="l00395"></a>
<a id="l00399"></a>
<a id="l00403"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00413"></a>
<a id="foldopen00425"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="foldopen00439"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="foldopen00453"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="foldopen00472"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="foldopen00491"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="foldopen00508"></a>
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
<a id="foldopen00533"></a>
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
<a id="foldopen00558"></a>
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
<a id="foldopen00605"></a>
<a id="l00605"></a>
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
<a id="foldopen00626"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="foldopen00651"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="foldopen00682"></a>
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
<a id="l00704"></a>
<a id="l00705"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__audio__codec__interface__backend_html_ga00729fd4ff9c7bb25ab0a44691b15fcd"></a>
<a id="agroup__audio__codec__interface__backend_html_ga0bba1b85f9f55389c5e52e8589947cc3"></a>
<a id="agroup__audio__codec__interface__backend_html_ga16647c5337af251140a9fa70e78b4d34"></a>
<a id="agroup__audio__codec__interface__backend_html_ga1aa7dff0874ce441560a567a1a6d2389"></a>
<a id="agroup__audio__codec__interface__backend_html_ga3998c4fade7829c14a8044c6efc3166c"></a>
<a id="agroup__audio__codec__interface__backend_html_ga4a283340b9ab266c8db97033b6e64865"></a>
<a id="agroup__audio__codec__interface__backend_html_ga6db1b3cf16e013ad5d59eef50acb4b78"></a>
<a id="agroup__audio__codec__interface__backend_html_ga751115a5ab2d9ca3f3362c76684743c0"></a>
<a id="agroup__audio__codec__interface__backend_html_gab05f39f6aedd5ddaef911eeb0e8923cd"></a>
<a id="agroup__audio__codec__interface__backend_html_gabe3ce7aa1275f171856157716796ee94"></a>
<a id="agroup__audio__codec__interface__backend_html_gabe62bf451dd9cb4bfa68e6a016415668"></a>
<a id="agroup__audio__codec__interface__backend_html_gac37a03bca2c70f7608a41910df70d4e2"></a>
<a id="agroup__audio__codec__interface__backend_html_gaf15768e53d0d5cec90f8489302c19227"></a>
<a id="agroup__audio__codec__interface_html_ga0c3344ea62fe994203315a0a7c20616c"></a>
<a id="agroup__audio__codec__interface_html_ga13ecf277fdf4cfaaa424402587a1a7ad"></a>
<a id="agroup__audio__codec__interface_html_ga147094be4c7c5d62df695673d293f12d"></a>
<a id="agroup__audio__codec__interface_html_ga186e9c63c792072280558b953ced1cf7"></a>
<a id="agroup__audio__codec__interface_html_ga1898dae0fac2e2bf34596453037bff7e"></a>
<a id="agroup__audio__codec__interface_html_ga2923c9aca9b8656ba3e3741d5860279a"></a>
<a id="agroup__audio__codec__interface_html_ga3b21ded95eb16d2c5f9f8da3c580a411"></a>
<a id="agroup__audio__codec__interface_html_ga3fa574a02bc12c578ea306202a222d32"></a>
<a id="agroup__audio__codec__interface_html_ga445f95326d5bcf51c355dfc128f1e862"></a>
<a id="agroup__audio__codec__interface_html_ga5365e64b28a7fd33d359eb020cd7f366"></a>
<a id="agroup__audio__codec__interface_html_ga5411b79fa217b0f9c63dc6890323804c"></a>
<a id="agroup__audio__codec__interface_html_ga550f86c43f7d96a1d826330d9da2d1af"></a>
<a id="agroup__audio__codec__interface_html_ga56e51f3a24b7fef4ce4fcb212b5807d9"></a>
<a id="agroup__audio__codec__interface_html_ga5e64f3537a4b0345f82e3e73992ee46a"></a>
<a id="agroup__audio__codec__interface_html_ga6d28af0279eb8e4b693ea35f5235f189"></a>
<a id="agroup__audio__codec__interface_html_ga6faba1d52c8d93e5ab5ec9954bf52f4a"></a>
<a id="agroup__audio__codec__interface_html_ga8fd2079e6128c8a6da59c2dee58101ca"></a>
<a id="agroup__audio__codec__interface_html_ga90f86f013dd46bad33bc95b2a7c8e1c9"></a>
<a id="agroup__audio__codec__interface_html_ga92dc9ce48ff0785dbf002f52afcef254"></a>
<a id="agroup__audio__codec__interface_html_ga966cf980ce24855830e24b5de4d884d6"></a>
<a id="agroup__audio__codec__interface_html_gab6b430783bba55d30a2b99b4bf25a040"></a>
<a id="agroup__audio__codec__interface_html_gad3a2ec4622f9a7b0eb1b4d0a463e20d5"></a>
<a id="agroup__audio__codec__interface_html_gadaa36aabb932903c725007c2005a7304"></a>
<a id="agroup__audio__codec__interface_html_gadd16956b1160388a17c23d6cc84218b3"></a>
<a id="agroup__audio__codec__interface_html_gga147094be4c7c5d62df695673d293f12da0376329aa4700f6b6aed798a13cb1efe"></a>
<a id="agroup__audio__codec__interface_html_gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac"></a>
<a id="agroup__audio__codec__interface_html_gga147094be4c7c5d62df695673d293f12da3cac1ab007667ecc477f493cb74ca504"></a>
<a id="agroup__audio__codec__interface_html_gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c"></a>
<a id="agroup__audio__codec__interface_html_gga147094be4c7c5d62df695673d293f12da94fdc805aec7c34da2de990d1b1bef6e"></a>
<a id="agroup__audio__codec__interface_html_gga147094be4c7c5d62df695673d293f12daa578a69e94a460428e0d09f29cbf9ade"></a>
<a id="agroup__audio__codec__interface_html_gga147094be4c7c5d62df695673d293f12dad32b311e083c62d10b20a4028295d192"></a>
<a id="agroup__audio__codec__interface_html_gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e"></a>
<a id="agroup__audio__codec__interface_html_gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f"></a>
<a id="agroup__audio__codec__interface_html_gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638"></a>
<a id="agroup__audio__codec__interface_html_gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa"></a>
<a id="agroup__audio__codec__interface_html_gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba"></a>
<a id="agroup__audio__codec__interface_html_gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6"></a>
<a id="agroup__audio__codec__interface_html_gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f"></a>
<a id="agroup__audio__codec__interface_html_gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35"></a>
<a id="agroup__audio__codec__interface_html_gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1"></a>
<a id="agroup__audio__codec__interface_html_gga3b21ded95eb16d2c5f9f8da3c580a411a31ebeb6337049a1ccea29ede230ad28a"></a>
<a id="agroup__audio__codec__interface_html_gga3b21ded95eb16d2c5f9f8da3c580a411a68af44d32f8c5e46a962fe0fc0fe0323"></a>
<a id="agroup__audio__codec__interface_html_gga3b21ded95eb16d2c5f9f8da3c580a411a726898c5bfe3cbb217e3bca2fd1cdf7e"></a>
<a id="agroup__audio__codec__interface_html_gga3b21ded95eb16d2c5f9f8da3c580a411aa105c5914186aa9fbbd81af4e754ff0d"></a>
<a id="agroup__audio__codec__interface_html_gga5411b79fa217b0f9c63dc6890323804ca0608dca9fec8160429d17d1d7dac0026"></a>
<a id="agroup__audio__codec__interface_html_gga5411b79fa217b0f9c63dc6890323804ca22cc7ebf7a5c7732fd507835c32aa642"></a>
<a id="agroup__audio__codec__interface_html_gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8"></a>
<a id="agroup__audio__codec__interface_html_gga5411b79fa217b0f9c63dc6890323804ca9b4548cfe663072a98db20ea0da377c1"></a>
<a id="agroup__audio__codec__interface_html_gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb"></a>
<a id="agroup__audio__codec__interface_html_gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90"></a>
<a id="agroup__audio__codec__interface_html_gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9"></a>
<a id="agroup__audio__codec__interface_html_gga8fd2079e6128c8a6da59c2dee58101caa534b2e8dfa910c18b0617c236fa18c4d"></a>
<a id="agroup__audio__codec__interface_html_gga8fd2079e6128c8a6da59c2dee58101caa77fab8d698408449f11d0974bfebaa0b"></a>
<a id="agroup__audio__codec__interface_html_gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8"></a>
<a id="agroup__audio__codec__interface_html_gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913"></a>
<a id="agroup__audio__codec__interface_html_gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad"></a>
<a id="agroup__audio__codec__interface_html_gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811"></a>
<a id="agroup__audio__codec__interface_html_gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3"></a>
<a id="agroup__audio__codec__interface_html_gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a1a35205e5a757748b3cf2f2048956cfe"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a3ad5430c80ae5a55ecbaf9246bd3ae93"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a5370ff516a32a36a9f643d5906461817"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a7b8d80478453df358cbdb7064f7a656d"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04"></a>
<a id="agroup__audio__codec__interface_html_gga966cf980ce24855830e24b5de4d884d6affc38ea2d76af83e6b06a1471dd68cfa"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ai2s_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_ac58f2c111cc9989c86db2a7dc4fd84ca"></a>
<a id="astructaudio__codec__cfg_html"></a>
<a id="astructaudio__codec__cfg_html_a121ca221241b0e2e90d9657a2462cd3c"></a>
<a id="astructaudio__codec__cfg_html_a896521cdcacafeb3c5b42a439415c5bb"></a>
<a id="astructaudio__codec__cfg_html_aa42aa9a75adec5929c54910abdc5311c"></a>
<a id="astructaudio__codec__cfg_html_ab1527545f55b33f9e2ce97f21c79e3b4"></a>
<a id="astructaudio__codec__driver__api_html"></a>
<a id="astructaudio__codec__driver__api_html_a0ebb20a30df3394d42fbb9ae32517ef6"></a>
<a id="astructaudio__codec__driver__api_html_a143fbe63391cda0df3aeca55b9c330ea"></a>
<a id="astructaudio__codec__driver__api_html_a3386afc7e2fde592f01a391d505ffb5e"></a>
<a id="astructaudio__codec__driver__api_html_a625f2e250aef2f41a5cda5d7b81beffb"></a>
<a id="astructaudio__codec__driver__api_html_a672995be9d89a29f6aec7cebf3bfabc1"></a>
<a id="astructaudio__codec__driver__api_html_a9a5b3a4226577ec67897ba4e583aef6f"></a>
<a id="astructaudio__codec__driver__api_html_a9d356cc86c169ac7e243206ce753bb1f"></a>
<a id="astructaudio__codec__driver__api_html_aa3e4d23108d78cc35dd9048ae9f12165"></a>
<a id="astructaudio__codec__driver__api_html_ab85f34fb83f1907da6315fd1aba0df47"></a>
<a id="astructaudio__codec__driver__api_html_aba472f73fcf6c77ac656c51cf80b805d"></a>
<a id="astructaudio__codec__driver__api_html_ac1b78c930b2c32679fb0033f3b4d3c5b"></a>
<a id="astructaudio__codec__driver__api_html_ad9b39565a3bd7adf77c123e2ba50efdb"></a>
<a id="astructaudio__codec__driver__api_html_adabd13d638d2e18ad1ccf02437d62dad"></a>
<a id="astructaudio__codec__eq__cfg_html"></a>
<a id="astructaudio__codec__eq__cfg_html_a0b4e1272b8453fb08b2b223ad44e6faf"></a>
<a id="astructaudio__codec__eq__cfg_html_a80c1956a8c31214201a7ceb0229dd62b"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructi2s__config_html"></a>
<a id="astructpcm__config_html"></a>
<a id="astructpcm__config_html_a2e6b978dd1795d400076bd7ba0812f02"></a>
<a id="astructpcm__config_html_a9c9d58e429f9f9198d22a8437c8373e3"></a>
<a id="astructpcm__config_html_aacad2be27111d146ad046ad048672f72"></a>
<a id="astructpcm__config_html_ab1f1dd56e25317c3caaeb6206f07a211"></a>
<a id="astructpcm__config_html_ad0ad9c1e8c8af0016415f98a7fa0d69e"></a>
<a id="aunionaudio__dai__cfg__t_html"></a>
<a id="aunionaudio__dai__cfg__t_html_a18514b2f3b9622ddb24a58d3701d090d"></a>
<a id="aunionaudio__dai__cfg__t_html_a859ece50501a1c060e20e80f3dc05b95"></a>
<a id="aunionaudio__property__value__t_html"></a>
<a id="aunionaudio__property__value__t_html_a23e0d9031006d64dfb31d87e4f061dc8"></a>
<a id="aunionaudio__property__value__t_html_a70b92e6c426f39e93b7db913e55cd49b"></a>
<a id="aunionaudio__property__value__t_html_aafcfb98016ab4306b4fd6cb54f0c22e0"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_AUDIO_CODEC_H_
#define ZEPHYR_INCLUDE_AUDIO_CODEC_H_


#include <errno.h>
#include <zephyr/drivers/i2s.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
        AUDIO_PCM_RATE_8K = 8000,
        AUDIO_PCM_RATE_11P025K = 11025,
        AUDIO_PCM_RATE_16K = 16000,
        AUDIO_PCM_RATE_22P05K = 22050,
        AUDIO_PCM_RATE_24K = 24000,
        AUDIO_PCM_RATE_32K = 32000,
        AUDIO_PCM_RATE_44P1K = 44100,
        AUDIO_PCM_RATE_48K = 48000,
        AUDIO_PCM_RATE_96K = 96000,
        AUDIO_PCM_RATE_192K = 192000,
} audio_pcm_rate_t;

typedef enum {
        AUDIO_PCM_WIDTH_16_BITS = 16,
        AUDIO_PCM_WIDTH_20_BITS = 20,
        AUDIO_PCM_WIDTH_24_BITS = 24,
        AUDIO_PCM_WIDTH_32_BITS = 32,
} audio_pcm_width_t;

typedef enum {
        AUDIO_DAI_TYPE_I2S,
        AUDIO_DAI_TYPE_LEFT_JUSTIFIED,
        AUDIO_DAI_TYPE_RIGHT_JUSTIFIED,
        AUDIO_DAI_TYPE_PCMA,
        AUDIO_DAI_TYPE_PCMB,
        AUDIO_DAI_TYPE_PCM,
        AUDIO_DAI_TYPE_INVALID,
} audio_dai_type_t;

typedef enum {
        AUDIO_PROPERTY_OUTPUT_VOLUME,
        AUDIO_PROPERTY_OUTPUT_MUTE,
        AUDIO_PROPERTY_INPUT_VOLUME,
        AUDIO_PROPERTY_INPUT_MUTE,
        AUDIO_PROPERTY_EQ_GAIN
} audio_property_t;

typedef enum {
        AUDIO_CHANNEL_FRONT_LEFT,
        AUDIO_CHANNEL_FRONT_RIGHT,
        AUDIO_CHANNEL_LFE,
        AUDIO_CHANNEL_FRONT_CENTER,
        AUDIO_CHANNEL_REAR_LEFT,
        AUDIO_CHANNEL_REAR_RIGHT,
        AUDIO_CHANNEL_REAR_CENTER,
        AUDIO_CHANNEL_SIDE_LEFT,
        AUDIO_CHANNEL_SIDE_RIGHT,
        AUDIO_CHANNEL_HEADPHONE_LEFT,
        AUDIO_CHANNEL_HEADPHONE_RIGHT,
        AUDIO_CHANNEL_ALL,

        AUDIO_CHANNEL_COMMON_COUNT,

        AUDIO_CHANNEL_PRIV_START = AUDIO_CHANNEL_COMMON_COUNT,

        AUDIO_CHANNEL_MAX = INT16_MAX
} audio_channel_t;

typedef uint8_t audio_dai_dir_t;
#define AUDIO_DAI_DIR_TX   BIT(0)
#define AUDIO_DAI_DIR_RX   BIT(1)
#define AUDIO_DAI_DIR_TXRX (AUDIO_DAI_DIR_TX | AUDIO_DAI_DIR_RX)

struct pcm_config {
        audio_dai_dir_t dir;
        audio_pcm_width_t pcm_width;
        uint8_t channels;
        size_t block_size;
        audio_pcm_rate_t samplerate;
};

typedef union {
        struct i2s_config i2s;
        struct pcm_config pcm;
                               /* Other DAI types go here */
} audio_dai_cfg_t;

typedef enum {
        AUDIO_ROUTE_BYPASS,
        AUDIO_ROUTE_PLAYBACK,
        AUDIO_ROUTE_PLAYBACK_CAPTURE,
        AUDIO_ROUTE_CAPTURE,
} audio_route_t;

struct audio_codec_cfg {
        uint32_t mclk_freq;
        audio_dai_type_t dai_type;
        audio_dai_cfg_t dai_cfg;
        audio_route_t dai_route;
};

struct audio_codec_eq_cfg {
        uint32_t band;
        int32_t gain;
};

typedef union {
        int vol;
        bool mute;
        struct audio_codec_eq_cfg eq;
} audio_property_value_t;

enum audio_codec_error_type {
        AUDIO_CODEC_ERROR_OVERCURRENT = BIT(0),

        AUDIO_CODEC_ERROR_OVERTEMPERATURE = BIT(1),

        AUDIO_CODEC_ERROR_UNDERVOLTAGE = BIT(2),

        AUDIO_CODEC_ERROR_OVERVOLTAGE = BIT(3),

        AUDIO_CODEC_ERROR_DC = BIT(4),
};

typedef void (*audio_codec_error_callback_t)(const struct device *dev, uint32_t errors);

typedef void (*audio_codec_tx_done_callback_t)(const struct device *dev, void *user_data);

typedef void (*audio_codec_rx_done_callback_t)(const struct device *dev, uint8_t *buf, uint32_t len,
                                               void *user_data);


typedef int (*audio_codec_configure_t)(const struct device *dev, struct audio_codec_cfg *cfg);

typedef void (*audio_codec_start_output_t)(const struct device *dev);

typedef void (*audio_codec_stop_output_t)(const struct device *dev);

typedef int (*audio_codec_set_property_t)(const struct device *dev, audio_property_t property,
                                          audio_channel_t channel, audio_property_value_t val);

typedef int (*audio_codec_apply_properties_t)(const struct device *dev);

typedef int (*audio_codec_clear_errors_t)(const struct device *dev);

typedef int (*audio_codec_register_error_callback_t)(const struct device *dev,
                                                     audio_codec_error_callback_t cb);

typedef int (*audio_codec_route_input_t)(const struct device *dev, audio_channel_t channel,
                                         uint32_t input);

typedef int (*audio_codec_route_output_t)(const struct device *dev, audio_channel_t channel,
                                          uint32_t output);

typedef int (*audio_codec_start_t)(const struct device *dev, audio_dai_dir_t dir);

typedef int (*audio_codec_stop_t)(const struct device *dev, audio_dai_dir_t dir);

typedef int (*audio_codec_write_t)(const struct device *dev, uint8_t *data, size_t data_size);

typedef int (*audio_codec_register_done_callback_t)(
        const struct device *dev, audio_codec_tx_done_callback_t tx_cb, void *tx_cb_user_data,
        audio_codec_rx_done_callback_t rx_cb, void *rx_cb_user_data);

#define audio_codec_api audio_codec_driver_api __DEPRECATED_MACRO

__subsystem struct audio_codec_driver_api {
        audio_codec_configure_t configure;
        audio_codec_start_output_t start_output;
        audio_codec_stop_output_t stop_output;
        audio_codec_set_property_t set_property;
        audio_codec_apply_properties_t apply_properties;
        audio_codec_clear_errors_t clear_errors;
        audio_codec_register_error_callback_t register_error_callback;
        audio_codec_route_input_t route_input;
        audio_codec_route_output_t route_output;
        audio_codec_start_t start;
        audio_codec_stop_t stop;
        audio_codec_write_t write;
        audio_codec_register_done_callback_t register_done_callback;
};


static inline int audio_codec_configure(const struct device *dev, struct audio_codec_cfg *cfg)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        return api->configure(dev, cfg);
}

static inline void audio_codec_start_output(const struct device *dev)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        api->start_output(dev);
}

static inline void audio_codec_stop_output(const struct device *dev)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        api->stop_output(dev);
}

static inline int audio_codec_set_property(const struct device *dev, audio_property_t property,
                                           audio_channel_t channel, audio_property_value_t val)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        return api->set_property(dev, property, channel, val);
}

static inline int audio_codec_apply_properties(const struct device *dev)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        return api->apply_properties(dev);
}

static inline int audio_codec_clear_errors(const struct device *dev)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        if (api->clear_errors == NULL) {
                return -ENOSYS;
        }

        return api->clear_errors(dev);
}

static inline int audio_codec_register_error_callback(const struct device *dev,
                                                      audio_codec_error_callback_t cb)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        if (api->register_error_callback == NULL) {
                return -ENOSYS;
        }

        return api->register_error_callback(dev, cb);
}

static inline int audio_codec_route_input(const struct device *dev, audio_channel_t channel,
                                          uint32_t input)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        if (api->route_input == NULL) {
                return -ENOSYS;
        }

        return api->route_input(dev, channel, input);
}

static inline int audio_codec_route_output(const struct device *dev, audio_channel_t channel,
                                           uint32_t output)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        if (api->route_output == NULL) {
                return -ENOSYS;
        }

        return api->route_output(dev, channel, output);
}

static inline int audio_codec_start(const struct device *dev, audio_dai_dir_t dir)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        if (api->start == NULL) {
                return -ENOSYS;
        }

        return api->start(dev, dir);
}

static inline int audio_codec_stop(const struct device *dev, audio_dai_dir_t dir)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        if (api->stop == NULL) {
                return -ENOSYS;
        }

        return api->stop(dev, dir);
}

static inline int audio_codec_write(const struct device *dev, uint8_t *data, size_t data_size)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        if (api->write == NULL) {
                return -ENOSYS;
        }

        return api->write(dev, data, data_size);
}

static inline int audio_codec_register_done_callback(const struct device *dev,
                                                     audio_codec_tx_done_callback_t tx_cb,
                                                     void *tx_cb_user_data,
                                                     audio_codec_rx_done_callback_t rx_cb,
                                                     void *rx_cb_user_data)
{
        const struct audio_codec_driver_api *api = DEVICE_API_GET(audio_codec, dev);

        if (api->register_done_callback == NULL) {
                return -ENOSYS;
        }

        return api->register_done_callback(dev, tx_cb, tx_cb_user_data, rx_cb, rx_cb_user_data);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_AUDIO_CODEC_H_ */
```

## 32.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 161 行

其他数字音频接口（DAI）类型放在这里。

### 注释 3：原第 705 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_AUDIO_CODEC_H_`。

## 32.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/codec_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/drivers/i2s.h](https://docs.zephyrproject.org/latest/doxygen/html/i2s_8h.html)
- [AUDIO_PCM_RATE_8K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8)
- [AUDIO_PCM_RATE_11P025K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa534b2e8dfa910c18b0617c236fa18c4d)
- [AUDIO_PCM_RATE_16K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3)
- [AUDIO_PCM_RATE_22P05K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa77fab8d698408449f11d0974bfebaa0b)
- [AUDIO_PCM_RATE_24K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945)
- [AUDIO_PCM_RATE_32K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90)
- [AUDIO_PCM_RATE_44P1K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad)
- [AUDIO_PCM_RATE_48K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913)
- [AUDIO_PCM_RATE_96K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811)
- [AUDIO_PCM_RATE_192K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9)
- [audio_pcm_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga8fd2079e6128c8a6da59c2dee58101ca)
- [AUDIO_PCM_WIDTH_16_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e)
- [AUDIO_PCM_WIDTH_20_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638)
- [AUDIO_PCM_WIDTH_24_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa)
- [AUDIO_PCM_WIDTH_32_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f)
- [audio_pcm_width_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga1898dae0fac2e2bf34596453037bff7e)
- [AUDIO_DAI_TYPE_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac)
- [AUDIO_DAI_TYPE_LEFT_JUSTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da3cac1ab007667ecc477f493cb74ca504)
- [AUDIO_DAI_TYPE_RIGHT_JUSTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da94fdc805aec7c34da2de990d1b1bef6e)
- [AUDIO_DAI_TYPE_PCMA](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da0376329aa4700f6b6aed798a13cb1efe)
- [AUDIO_DAI_TYPE_PCMB](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12daa578a69e94a460428e0d09f29cbf9ade)
- [AUDIO_DAI_TYPE_PCM](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12dad32b311e083c62d10b20a4028295d192)
- [AUDIO_DAI_TYPE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c)
- [audio_dai_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga147094be4c7c5d62df695673d293f12d)
- [AUDIO_PROPERTY_OUTPUT_VOLUME](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8)
- [AUDIO_PROPERTY_OUTPUT_MUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb)
- [AUDIO_PROPERTY_INPUT_VOLUME](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca0608dca9fec8160429d17d1d7dac0026)
- [AUDIO_PROPERTY_INPUT_MUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca9b4548cfe663072a98db20ea0da377c1)
- [AUDIO_PROPERTY_EQ_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca22cc7ebf7a5c7732fd507835c32aa642)
- [audio_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5411b79fa217b0f9c63dc6890323804c)
- [AUDIO_CHANNEL_FRONT_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18)
- [AUDIO_CHANNEL_FRONT_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75)
- [AUDIO_CHANNEL_LFE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6)
- [AUDIO_CHANNEL_FRONT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8)
- [AUDIO_CHANNEL_REAR_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc)
- [AUDIO_CHANNEL_REAR_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9)
- [AUDIO_CHANNEL_REAR_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04)
- [AUDIO_CHANNEL_SIDE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba)
- [AUDIO_CHANNEL_SIDE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec)
- [AUDIO_CHANNEL_HEADPHONE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6affc38ea2d76af83e6b06a1471dd68cfa)
- [AUDIO_CHANNEL_HEADPHONE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a7b8d80478453df358cbdb7064f7a656d)
- [AUDIO_CHANNEL_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878)
- [AUDIO_CHANNEL_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a1a35205e5a757748b3cf2f2048956cfe)
- [AUDIO_CHANNEL_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a3ad5430c80ae5a55ecbaf9246bd3ae93)
- [AUDIO_CHANNEL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a5370ff516a32a36a9f643d5906461817)
- [INT16_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac58f2c111cc9989c86db2a7dc4fd84ca)
- [audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)
- [pcm_config](../audio_video_model_reference/P041_pcm_config_结构体.md)
- [dir](../audio_video_model_reference/P041_pcm_config_结构体.md#a2e6b978dd1795d400076bd7ba0812f02)
- [pcm_width](../audio_video_model_reference/P041_pcm_config_结构体.md#a9c9d58e429f9f9198d22a8437c8373e3)
- [channels](../audio_video_model_reference/P041_pcm_config_结构体.md#ad0ad9c1e8c8af0016415f98a7fa0d69e)
- [block_size](../audio_video_model_reference/P041_pcm_config_结构体.md#aacad2be27111d146ad046ad048672f72)
- [samplerate](../audio_video_model_reference/P041_pcm_config_结构体.md#ab1f1dd56e25317c3caaeb6206f07a211)
- [i2s_config](../audio_video_model_reference/P008_i2s_config_结构体.md)
- [i2s](../audio_video_model_reference/P066_audio_dai_cfg_t_联合体.md#a18514b2f3b9622ddb24a58d3701d090d)
- [pcm](../audio_video_model_reference/P066_audio_dai_cfg_t_联合体.md#a859ece50501a1c060e20e80f3dc05b95)
- [audio_dai_cfg_t](../audio_video_model_reference/P066_audio_dai_cfg_t_联合体.md)
- [AUDIO_ROUTE_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411a68af44d32f8c5e46a962fe0fc0fe0323)
- [AUDIO_ROUTE_PLAYBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411a726898c5bfe3cbb217e3bca2fd1cdf7e)
- [AUDIO_ROUTE_PLAYBACK_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411aa105c5914186aa9fbbd81af4e754ff0d)
- [AUDIO_ROUTE_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411a31ebeb6337049a1ccea29ede230ad28a)
- [audio_route_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga3b21ded95eb16d2c5f9f8da3c580a411)
- [audio_codec_cfg](../driver_model_reference/P016_音频编解码器配置.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mclk_freq](../driver_model_reference/P016_音频编解码器配置.md#a896521cdcacafeb3c5b42a439415c5bb)
- [dai_type](../driver_model_reference/P016_音频编解码器配置.md#a121ca221241b0e2e90d9657a2462cd3c)
- [dai_cfg](../driver_model_reference/P016_音频编解码器配置.md#aa42aa9a75adec5929c54910abdc5311c)
- [dai_route](../driver_model_reference/P016_音频编解码器配置.md#ab1527545f55b33f9e2ce97f21c79e3b4)
- [audio_codec_eq_cfg](../driver_model_reference/P018_音频编解码器均衡配置.md)
- [band](../driver_model_reference/P018_音频编解码器均衡配置.md#a0b4e1272b8453fb08b2b223ad44e6faf)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [gain](../driver_model_reference/P018_音频编解码器均衡配置.md#a80c1956a8c31214201a7ceb0229dd62b)
- [vol](../audio_video_model_reference/P067_audio_property_value_t_联合体.md#aafcfb98016ab4306b4fd6cb54f0c22e0)
- [mute](../audio_video_model_reference/P067_audio_property_value_t_联合体.md#a23e0d9031006d64dfb31d87e4f061dc8)
- [eq](../audio_video_model_reference/P067_audio_property_value_t_联合体.md#a70b92e6c426f39e93b7db913e55cd49b)
- [audio_property_value_t](../audio_video_model_reference/P067_audio_property_value_t_联合体.md)
- [audio_codec_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga2923c9aca9b8656ba3e3741d5860279a)
- [AUDIO_CODEC_ERROR_OVERCURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [AUDIO_CODEC_ERROR_OVERTEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f)
- [AUDIO_CODEC_ERROR_UNDERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba)
- [AUDIO_CODEC_ERROR_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6)
- [AUDIO_CODEC_ERROR_DC](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35)
- [audio_codec_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga13ecf277fdf4cfaaa424402587a1a7ad)
- [device](../device_reference/P002_设备对象结构.md)
- [audio_codec_tx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5365e64b28a7fd33d359eb020cd7f366)
- [audio_codec_rx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga56e51f3a24b7fef4ce4fcb212b5807d9)
- [audio_codec_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#ga751115a5ab2d9ca3f3362c76684743c0)
- [audio_codec_start_output_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#ga0bba1b85f9f55389c5e52e8589947cc3)
- [audio_codec_stop_output_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#gab05f39f6aedd5ddaef911eeb0e8923cd)
- [audio_codec_set_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#ga1aa7dff0874ce441560a567a1a6d2389)
- [audio_codec_apply_properties_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#gabe3ce7aa1275f171856157716796ee94)
- [audio_codec_clear_errors_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#ga3998c4fade7829c14a8044c6efc3166c)
- [audio_codec_register_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#ga6db1b3cf16e013ad5d59eef50acb4b78)
- [audio_codec_route_input_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#ga00729fd4ff9c7bb25ab0a44691b15fcd)
- [audio_codec_route_output_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#ga16647c5337af251140a9fa70e78b4d34)
- [audio_codec_start_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#gaf15768e53d0d5cec90f8489302c19227)
- [audio_codec_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#ga4a283340b9ab266c8db97033b6e64865)
- [audio_codec_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#gabe62bf451dd9cb4bfa68e6a016415668)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [audio_codec_register_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html#gac37a03bca2c70f7608a41910df70d4e2)
- [audio_codec_driver_api](../driver_model_reference/P017_音频编解码器驱动接口.md)
- [configure](../driver_model_reference/P017_音频编解码器驱动接口.md#a143fbe63391cda0df3aeca55b9c330ea)
- [start_output](../driver_model_reference/P017_音频编解码器驱动接口.md#a0ebb20a30df3394d42fbb9ae32517ef6)
- [stop_output](../driver_model_reference/P017_音频编解码器驱动接口.md#aba472f73fcf6c77ac656c51cf80b805d)
- [set_property](../driver_model_reference/P017_音频编解码器驱动接口.md#a3386afc7e2fde592f01a391d505ffb5e)
- [apply_properties](../driver_model_reference/P017_音频编解码器驱动接口.md#a9d356cc86c169ac7e243206ce753bb1f)
- [clear_errors](../driver_model_reference/P017_音频编解码器驱动接口.md#aa3e4d23108d78cc35dd9048ae9f12165)
- [register_error_callback](../driver_model_reference/P017_音频编解码器驱动接口.md#a672995be9d89a29f6aec7cebf3bfabc1)
- [route_input](../driver_model_reference/P017_音频编解码器驱动接口.md#ab85f34fb83f1907da6315fd1aba0df47)
- [route_output](../driver_model_reference/P017_音频编解码器驱动接口.md#ad9b39565a3bd7adf77c123e2ba50efdb)
- [start](../driver_model_reference/P017_音频编解码器驱动接口.md#ac1b78c930b2c32679fb0033f3b4d3c5b)
- [stop](../driver_model_reference/P017_音频编解码器驱动接口.md#a625f2e250aef2f41a5cda5d7b81beffb)
- [write](../driver_model_reference/P017_音频编解码器驱动接口.md#a9a5b3a4226577ec67897ba4e583aef6f)
- [register_done_callback](../driver_model_reference/P017_音频编解码器驱动接口.md#adabd13d638d2e18ad1ccf02437d62dad)
- [audio_codec_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga0c3344ea62fe994203315a0a7c20616c)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [audio_codec_start_output](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga186e9c63c792072280558b953ced1cf7)
- [audio_codec_stop_output](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga6faba1d52c8d93e5ab5ec9954bf52f4a)
- [audio_codec_set_property](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga6d28af0279eb8e4b693ea35f5235f189)
- [audio_codec_apply_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gadd16956b1160388a17c23d6cc84218b3)
- [audio_codec_clear_errors](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga550f86c43f7d96a1d826330d9da2d1af)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [audio_codec_register_error_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga90f86f013dd46bad33bc95b2a7c8e1c9)
- [audio_codec_route_input](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga92dc9ce48ff0785dbf002f52afcef254)
- [audio_codec_route_output](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gadaa36aabb932903c725007c2005a7304)
- [audio_codec_start](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga445f95326d5bcf51c355dfc128f1e862)
- [audio_codec_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga3fa574a02bc12c578ea306202a222d32)
- [audio_codec_write](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gab6b430783bba55d30a2b99b4bf25a040)
- [audio_codec_register_done_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5e64f3537a4b0345f82e3e73992ee46a)
- [i2s.h](https://docs.zephyrproject.org/latest/doxygen/html/i2s_8h.html)
- [audio_codec_cfg::dai_type](../driver_model_reference/P016_音频编解码器配置.md#a121ca221241b0e2e90d9657a2462cd3c)
- [audio_codec_cfg::mclk_freq](../driver_model_reference/P016_音频编解码器配置.md#a896521cdcacafeb3c5b42a439415c5bb)
- [audio_codec_cfg::dai_cfg](../driver_model_reference/P016_音频编解码器配置.md#aa42aa9a75adec5929c54910abdc5311c)
- [audio_codec_cfg::dai_route](../driver_model_reference/P016_音频编解码器配置.md#ab1527545f55b33f9e2ce97f21c79e3b4)
- [audio_codec_driver_api::start_output](../driver_model_reference/P017_音频编解码器驱动接口.md#a0ebb20a30df3394d42fbb9ae32517ef6)
- [audio_codec_driver_api::configure](../driver_model_reference/P017_音频编解码器驱动接口.md#a143fbe63391cda0df3aeca55b9c330ea)
- [audio_codec_driver_api::set_property](../driver_model_reference/P017_音频编解码器驱动接口.md#a3386afc7e2fde592f01a391d505ffb5e)
- [audio_codec_driver_api::stop](../driver_model_reference/P017_音频编解码器驱动接口.md#a625f2e250aef2f41a5cda5d7b81beffb)
- [audio_codec_driver_api::register_error_callback](../driver_model_reference/P017_音频编解码器驱动接口.md#a672995be9d89a29f6aec7cebf3bfabc1)
- [audio_codec_driver_api::write](../driver_model_reference/P017_音频编解码器驱动接口.md#a9a5b3a4226577ec67897ba4e583aef6f)
- [audio_codec_driver_api::apply_properties](../driver_model_reference/P017_音频编解码器驱动接口.md#a9d356cc86c169ac7e243206ce753bb1f)
- [audio_codec_driver_api::clear_errors](../driver_model_reference/P017_音频编解码器驱动接口.md#aa3e4d23108d78cc35dd9048ae9f12165)
- [audio_codec_driver_api::route_input](../driver_model_reference/P017_音频编解码器驱动接口.md#ab85f34fb83f1907da6315fd1aba0df47)
- [audio_codec_driver_api::stop_output](../driver_model_reference/P017_音频编解码器驱动接口.md#aba472f73fcf6c77ac656c51cf80b805d)
- [audio_codec_driver_api::start](../driver_model_reference/P017_音频编解码器驱动接口.md#ac1b78c930b2c32679fb0033f3b4d3c5b)
- [audio_codec_driver_api::route_output](../driver_model_reference/P017_音频编解码器驱动接口.md#ad9b39565a3bd7adf77c123e2ba50efdb)
- [audio_codec_driver_api::register_done_callback](../driver_model_reference/P017_音频编解码器驱动接口.md#adabd13d638d2e18ad1ccf02437d62dad)
- [audio_codec_eq_cfg::band](../driver_model_reference/P018_音频编解码器均衡配置.md#a0b4e1272b8453fb08b2b223ad44e6faf)
- [audio_codec_eq_cfg::gain](../driver_model_reference/P018_音频编解码器均衡配置.md#a80c1956a8c31214201a7ceb0229dd62b)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [pcm_config::dir](../audio_video_model_reference/P041_pcm_config_结构体.md#a2e6b978dd1795d400076bd7ba0812f02)
- [pcm_config::pcm_width](../audio_video_model_reference/P041_pcm_config_结构体.md#a9c9d58e429f9f9198d22a8437c8373e3)
- [pcm_config::block_size](../audio_video_model_reference/P041_pcm_config_结构体.md#aacad2be27111d146ad046ad048672f72)
- [pcm_config::samplerate](../audio_video_model_reference/P041_pcm_config_结构体.md#ab1f1dd56e25317c3caaeb6206f07a211)
- [pcm_config::channels](../audio_video_model_reference/P041_pcm_config_结构体.md#ad0ad9c1e8c8af0016415f98a7fa0d69e)
- [audio_dai_cfg_t::i2s](../audio_video_model_reference/P066_audio_dai_cfg_t_联合体.md#a18514b2f3b9622ddb24a58d3701d090d)
- [audio_dai_cfg_t::pcm](../audio_video_model_reference/P066_audio_dai_cfg_t_联合体.md#a859ece50501a1c060e20e80f3dc05b95)
- [audio_property_value_t::mute](../audio_video_model_reference/P067_audio_property_value_t_联合体.md#a23e0d9031006d64dfb31d87e4f061dc8)
- [audio_property_value_t::eq](../audio_video_model_reference/P067_audio_property_value_t_联合体.md#a70b92e6c426f39e93b7db913e55cd49b)
- [audio_property_value_t::vol](../audio_video_model_reference/P067_audio_property_value_t_联合体.md#aafcfb98016ab4306b4fd6cb54f0c22e0)

---

[上一章](P031_cobs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P033_common-clock.h_源码浏览.md)
