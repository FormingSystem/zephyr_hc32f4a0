---
id: learning.zephyr-docs.api-source-device-reference.page-9
title: fuel_gauge.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_fuel\_gauge.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h.html)。

## 9.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
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
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00048"></a>
<a id="l00050"></a>
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
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="foldopen00230"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00266"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00301"></a>
<a id="l00303"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00315"></a>
<a id="l00317"></a>
<a id="l00319"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00331"></a>
<a id="l00333"></a>
<a id="l00335"></a>
<a id="l00337"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00351"></a>
<a id="l00353"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="l00373"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="l00385"></a>
<a id="l00387"></a>
<a id="l00392"></a>
<a id="l00394"></a>
<a id="l00399"></a>
<a id="l00401"></a>
<a id="l00406"></a>
<a id="l00408"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="l00420"></a>
<a id="l00422"></a>
<a id="l00427"></a>
<a id="l00429"></a>
<a id="l00434"></a>
<a id="l00436"></a>
<a id="l00441"></a>
<a id="l00443"></a>
<a id="l00445"></a>
<a id="l00447"></a>
<a id="l00449"></a>
<a id="l00451"></a>
<a id="l00453"></a>
<a id="l00455"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="foldopen00467"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="foldopen00472"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="foldopen00477"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00487"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="foldopen00534"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00542"></a>
<a id="l00544"></a>
<a id="l00546"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00554"></a>
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
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
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
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
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
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
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
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00676"></a>
<a id="l00677"></a>
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
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="l00724"></a>
<a id="l00725"></a>
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
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__fuel__gauge__interface__backend_html_ga698c8f84da7d1cbe7db1fc024e2388b7"></a>
<a id="agroup__fuel__gauge__interface__backend_html_gae5908067ab2a8c70c517d3e12eb364c1"></a>
<a id="agroup__fuel__gauge__interface__backend_html_gae87a20a20f4f1fbb74d72afb2bcee4c9"></a>
<a id="agroup__fuel__gauge__interface__backend_html_gaed940ae925236ad2f25cf05d78304568"></a>
<a id="agroup__fuel__gauge__interface__backend_html_gaf8843b8ba9ff3102ac4d6c0fa2cb3f69"></a>
<a id="agroup__fuel__gauge__interface_html_ga08e4dae43d5169da58af32ec419ef9e8"></a>
<a id="agroup__fuel__gauge__interface_html_ga41b8379542b9cbd0b3ee9e1bbe4bc599"></a>
<a id="agroup__fuel__gauge__interface_html_ga44fd24de7d165388a87e6dd74f6547af"></a>
<a id="agroup__fuel__gauge__interface_html_ga633eb1cb8dd64123252634b833b2f806"></a>
<a id="agroup__fuel__gauge__interface_html_ga763a40688dc8fc6a0ba85fdc79178ebc"></a>
<a id="agroup__fuel__gauge__interface_html_ga7e6cb77d2d4dd7a0feb25c92d031614c"></a>
<a id="agroup__fuel__gauge__interface_html_ga824e00f1d607cdfe2598625f154636f1"></a>
<a id="agroup__fuel__gauge__interface_html_ga936be681a82f173b664ae2187bc5a73d"></a>
<a id="agroup__fuel__gauge__interface_html_gab84999beab9a43241992945a3b2d37e1"></a>
<a id="agroup__fuel__gauge__interface_html_gac63f43b6023b9f2183001d6876fe328a"></a>
<a id="agroup__fuel__gauge__interface_html_gac8efb10ccb6f510dc92618e218c1df9b"></a>
<a id="agroup__fuel__gauge__interface_html_gae49908857800bdd010d59895cfad9171"></a>
<a id="agroup__fuel__gauge__interface_html_gaf8a1fed5f6af9c25a12130c481411603"></a>
<a id="agroup__fuel__gauge__interface_html_gaf8c7f6c4f49dd420df6841c43c41d615"></a>
<a id="agroup__fuel__gauge__interface_html_gafe9bdc00d856d4cc787265edb7eb0ed2"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a09809ae39a4c79e1a35095300d838c78"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a0a5d8d32ccf8658f88642f33872d94b8"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a1dc93924386cfd048fb9a1865adb9904"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a2026a7272e1a6c301ea53282f919980b"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a328886a8b2318367bb968e4a6c9eba1f"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a34dbed1768f1787d8269ef30c2478c53"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a3515db092af7dfa2d9a8b879e0b56d1e"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a367b0beb959a116e81de9cd5f2adbe43"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a3c5e7d0ede99656b407f25f114adf24d"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a4b599ee88b5ddbb0bdb8f30c1fe2796a"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a4bcd9bf3d2c9c081d9186d30e39ab32a"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a4c66491e317f6b27b2f3db0cdda89b1b"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a4feeb0b0add43143c8f99299af5859ce"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a53744eaac0496db3619baa3b42f96ce6"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a55cf7fcc30be436fd51d79f9ad675d5c"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a58c1b0a39345a7006a8ee0ad6ce01bb4"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a6d6fa90dd558d14f039b9cd9fcb15b70"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a76ca40b38e4326237c94b4f38dc1680b"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a7ca368502befbe58ac68c1aaa24d32ee"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a84b472b072be9494cf7d5f9027421772"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a8d0ac3331a389394b603a00d0a47498f"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a923809dbcdd526822ffde000137eccee"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171a9b300c9edad178b7563f7d5ea3b88833"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171aa7351ed7cc8ece7cacb97c4308048fb2"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171aa993fbb1a9e04554fff73c7e59cd3783"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171aae228a0e3ab76368fbddeff8dd5d1458"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171abd2a4cc73d651fa54c9dab634198aeae"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171abfc512152bf56f62d1d67660e03dc2e9"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ac0754d083fa22c7f07cfd8846b3bdbd5"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ac1ea4d609b9286807c9c589ed0b731eb"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ac265b9e9137c4dbd424d833c50b2d828"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ac7e9e36e2c622474129cf4f51b1782c6"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ad1a57cfd758250b2e3f4b5c4abeac9e7"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ad4d9f765c0e0e388b71ef1db09034f50"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ae29582cdad457499ad83cee06ca3ff21"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171ae8a61b0db58687634ff57f3c536dfd40"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171aea985dd0c89e41bdd018a2dce143d9b4"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171aeba3b1d8a5239d4afbe8f1d4753583aa"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171aec015967b3aef33ca2728058d6d73b55"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171afa3d404c62c20357d29954c25b8df174"></a>
<a id="agroup__fuel__gauge__interface_html_ggae49908857800bdd010d59895cfad9171afa8f22eecf3cbc2b5b50a69ce974f99c"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a3ea490c9b3617d4479bd80ef93cd5602"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructdevice_html"></a>
<a id="astructfuel__gauge__driver__api_html"></a>
<a id="astructfuel__gauge__driver__api_html_a406816c19022eea26f0fd61fb21d234c"></a>
<a id="astructfuel__gauge__driver__api_html_a74815d3bb721452bfd3e35cd1221b223"></a>
<a id="astructfuel__gauge__driver__api_html_aa9963e6744222271ab45e2eabbf69f87"></a>
<a id="astructfuel__gauge__driver__api_html_ab729a85c69e561f1ca0aca9f8eb22d91"></a>
<a id="astructfuel__gauge__driver__api_html_ad12c13461173177d1c81846a85a3f570"></a>
<a id="astructsbs__gauge__device__chemistry_html"></a>
<a id="astructsbs__gauge__device__chemistry_html_a2a3990be7618165d88790e53ac7b4e72"></a>
<a id="astructsbs__gauge__device__chemistry_html_a340cfddcc1ad7a758f75208b38208df4"></a>
<a id="astructsbs__gauge__device__name_html"></a>
<a id="astructsbs__gauge__device__name_html_a5e599e923ccbdc7eb89ab6f7e1d3a662"></a>
<a id="astructsbs__gauge__device__name_html_a6699e048a1ca5feb2cadb05169bcfa5f"></a>
<a id="astructsbs__gauge__manufacturer__name_html"></a>
<a id="astructsbs__gauge__manufacturer__name_html_a13a5902df94842f7a69a8028b8708ced"></a>
<a id="astructsbs__gauge__manufacturer__name_html_a40af61fe30263b21e9b9c92383562b0d"></a>
<a id="aunionfuel__gauge__prop__val_html"></a>
<a id="aunionfuel__gauge__prop__val_html_a06edf4e066a3b655cdfd4ab732e93b7a"></a>
<a id="aunionfuel__gauge__prop__val_html_a0b6878d02d4d5a3865e8ca8d57951914"></a>
<a id="aunionfuel__gauge__prop__val_html_a0bf74ed2b92b7b0920cf90ef7119aa36"></a>
<a id="aunionfuel__gauge__prop__val_html_a11626713aef0445ad613a5976401d09e"></a>
<a id="aunionfuel__gauge__prop__val_html_a1638b4b54bf57af650832e53f9ce90a4"></a>
<a id="aunionfuel__gauge__prop__val_html_a163ecf351a2a538cac53757ad402dde0"></a>
<a id="aunionfuel__gauge__prop__val_html_a20aa5736b0ac3c5adda10152660de275"></a>
<a id="aunionfuel__gauge__prop__val_html_a21fb17e3d083c0a26f592f38b07b797e"></a>
<a id="aunionfuel__gauge__prop__val_html_a2b044d7e33e98fd0c0cead2a3de61431"></a>
<a id="aunionfuel__gauge__prop__val_html_a2c77e8de7fa40fadfa13dfd4c94df804"></a>
<a id="aunionfuel__gauge__prop__val_html_a33297ff5bf70b510272eddf77ced411e"></a>
<a id="aunionfuel__gauge__prop__val_html_a36528b111568bd1c90859e454610fd9f"></a>
<a id="aunionfuel__gauge__prop__val_html_a3b2dc6e92a6b4158115e76c78061fe16"></a>
<a id="aunionfuel__gauge__prop__val_html_a45b20c5118f7ee408d507b94e6cae1dc"></a>
<a id="aunionfuel__gauge__prop__val_html_a4916bb50489c5f70335da2f11ed9477e"></a>
<a id="aunionfuel__gauge__prop__val_html_a49e894ef1b0f7be9c5a1dba12a8cff41"></a>
<a id="aunionfuel__gauge__prop__val_html_a4ce4046d3284afa7fd2e37d510cf4fd2"></a>
<a id="aunionfuel__gauge__prop__val_html_a52b70375d15ed878d62d1390c3144cd8"></a>
<a id="aunionfuel__gauge__prop__val_html_a600a90fd8d847bd29ffd9d96822abdb8"></a>
<a id="aunionfuel__gauge__prop__val_html_a63ce57eb11373a7e899d6324f4335749"></a>
<a id="aunionfuel__gauge__prop__val_html_a65607bb9ba43022c9c566646d4763aac"></a>
<a id="aunionfuel__gauge__prop__val_html_a6f74626deef4debbd8dfe6c188984d1b"></a>
<a id="aunionfuel__gauge__prop__val_html_a740700d2c6c6db83617d8dfd964e34f7"></a>
<a id="aunionfuel__gauge__prop__val_html_a7c8b6f9ee98e5b97ddc85b7e72cea4a8"></a>
<a id="aunionfuel__gauge__prop__val_html_a7d943c31ad7dd53d16bfded98e70b332"></a>
<a id="aunionfuel__gauge__prop__val_html_a7fc0551e303de56e0eb6bdac1ecaccd0"></a>
<a id="aunionfuel__gauge__prop__val_html_a818ab7faf8f51d4d1a5c5f070d54b997"></a>
<a id="aunionfuel__gauge__prop__val_html_a8743f7e7a05919b5469e39527b697e62"></a>
<a id="aunionfuel__gauge__prop__val_html_a8bc68c65571afb6856e7e1e6cb33a5e4"></a>
<a id="aunionfuel__gauge__prop__val_html_a8d349a8fe357fd30ba4d458dd8260f5a"></a>
<a id="aunionfuel__gauge__prop__val_html_a94893761a1f77a9c0e746c34e5bb6e61"></a>
<a id="aunionfuel__gauge__prop__val_html_a957025a2a9fb7709e2bf478f15fd31a0"></a>
<a id="aunionfuel__gauge__prop__val_html_a9b5015878c9a77d9c8330139f94843b7"></a>
<a id="aunionfuel__gauge__prop__val_html_a9bed3247063f069bb92b2902cc5ff468"></a>
<a id="aunionfuel__gauge__prop__val_html_a9dd892b613881fda89635046b3ef7942"></a>
<a id="aunionfuel__gauge__prop__val_html_a9e12460af8ae1a0ba0d1838e977e7a59"></a>
<a id="aunionfuel__gauge__prop__val_html_a9f4653e270e93280bd6bed6022c135b0"></a>
<a id="aunionfuel__gauge__prop__val_html_aa0e46c727bb31acb5d41ce4bc6d5b106"></a>
<a id="aunionfuel__gauge__prop__val_html_aa29f7163a1637b6aa8cd6a15dc99d55b"></a>
<a id="aunionfuel__gauge__prop__val_html_aa52341a118d1445ee762ba1563406441"></a>
<a id="aunionfuel__gauge__prop__val_html_aa5529fea5cfe765be9b66f5fad96ab2f"></a>
<a id="aunionfuel__gauge__prop__val_html_aa901ef363509234577d73958984862a4"></a>
<a id="aunionfuel__gauge__prop__val_html_aaa55eae9e98203e5f1847d6162d1d28e"></a>
<a id="aunionfuel__gauge__prop__val_html_aaee1a60dac0770780bd45c1549fbf819"></a>
<a id="aunionfuel__gauge__prop__val_html_ab19f11342d10502937595b535db09c7a"></a>
<a id="aunionfuel__gauge__prop__val_html_ab43ccbb0a1443e64d26e498d31d1a240"></a>
<a id="aunionfuel__gauge__prop__val_html_ab4aafbc07557b2c15396b8bfc66d7e9b"></a>
<a id="aunionfuel__gauge__prop__val_html_ab553a7b8b86225bd6c13c7f0c0a5e658"></a>
<a id="aunionfuel__gauge__prop__val_html_ab969822a9d1bc32345d02805c6f9b204"></a>
<a id="aunionfuel__gauge__prop__val_html_abec5cadefa09e088620a9598dec9c473"></a>
<a id="aunionfuel__gauge__prop__val_html_ac27ae67a315a7204cea6e88962758587"></a>
<a id="aunionfuel__gauge__prop__val_html_ac651ea27014b7e61fdf5e847d70a188c"></a>
<a id="aunionfuel__gauge__prop__val_html_ac8a4263fede43ebcd28cff1c66e413b1"></a>
<a id="aunionfuel__gauge__prop__val_html_ac8e8e74c2b1f2e0c1f4e65eecf5a745a"></a>
<a id="aunionfuel__gauge__prop__val_html_acf5b8f9b1ff3b3c5b5547d4920dbd7f2"></a>
<a id="aunionfuel__gauge__prop__val_html_ad600545303f0fa6e2853396e83d87fdd"></a>
<a id="aunionfuel__gauge__prop__val_html_ad8d424fbbe3124cde5e82b74957a4885"></a>
<a id="aunionfuel__gauge__prop__val_html_ad96f07db337c038466dd17401c076d38"></a>
<a id="aunionfuel__gauge__prop__val_html_adab6e7b86aea46fdb9f5bc99ae87e431"></a>
<a id="aunionfuel__gauge__prop__val_html_adbfa0be8653107875e91edd5db40265d"></a>
<a id="aunionfuel__gauge__prop__val_html_adeb93ed2120e808aac815dcbdf69067f"></a>
<a id="aunionfuel__gauge__prop__val_html_adecf57aa90e2b5d483cfd889ec512400"></a>
<a id="aunionfuel__gauge__prop__val_html_ae1d5c18887cb8dab5ad070801992be1a"></a>
<a id="aunionfuel__gauge__prop__val_html_ae40e0074599fa69ea5b9e9012c14452b"></a>
<a id="aunionfuel__gauge__prop__val_html_ae716bdf1346dc7767d98526db6083008"></a>
<a id="aunionfuel__gauge__prop__val_html_aec778f250686b960c7328c27b48d5a17"></a>
<a id="aunionfuel__gauge__prop__val_html_aee04c49d39652837420039fb968ecea5"></a>
<a id="aunionfuel__gauge__prop__val_html_aeeeddb48f22b54f90c603d58e9ffa9a5"></a>
<a id="aunionfuel__gauge__prop__val_html_aef3ced90ca261ec7501778a41f12963d"></a>
<a id="aunionfuel__gauge__prop__val_html_af40db6b3dba16b20097d0767e51a07c5"></a>
<a id="aunionfuel__gauge__prop__val_html_af421dee221486f53d71d0fb8e6c4df1c"></a>
<a id="aunionfuel__gauge__prop__val_html_aff81db28e93cb70ebea6793e4493915f"></a>

```c
/*
 * Copyright 2022 Google LLC
 * Copyright 2023 Microsoft Corporation
 * Copyright (c) 2025 Philipp Steiner
 * Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
 * Copyright (c) 2026 Analog Devices Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FUEL_GAUGE_H_
#define ZEPHYR_INCLUDE_DRIVERS_FUEL_GAUGE_H_


#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

#include <errno.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/device.h>

enum fuel_gauge_prop_type {
        FUEL_GAUGE_AVG_CURRENT_UA = 0,
        FUEL_GAUGE_AVG_CURRENT __deprecated = FUEL_GAUGE_AVG_CURRENT_UA,

        FUEL_GAUGE_CURRENT_UA,
        FUEL_GAUGE_CURRENT __deprecated = FUEL_GAUGE_CURRENT_UA,
        FUEL_GAUGE_CHARGE_CUTOFF,
        FUEL_GAUGE_CYCLE_COUNT,
        FUEL_GAUGE_CONNECT_STATE,
        FUEL_GAUGE_FLAGS,
        FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH,
        FUEL_GAUGE_FULL_CHARGE_CAPACITY __deprecated = FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH,
        FUEL_GAUGE_PRESENT_STATE,
        FUEL_GAUGE_REMAINING_CAPACITY_UAH,
        FUEL_GAUGE_REMAINING_CAPACITY __deprecated = FUEL_GAUGE_REMAINING_CAPACITY_UAH,
        FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS,
        FUEL_GAUGE_RUNTIME_TO_EMPTY __deprecated = FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS,
        FUEL_GAUGE_RUNTIME_TO_FULL_MINS,
        FUEL_GAUGE_RUNTIME_TO_FULL __deprecated = FUEL_GAUGE_RUNTIME_TO_FULL_MINS,
        FUEL_GAUGE_SBS_MFR_ACCESS,
        FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT,
        FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE __deprecated = FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT,
        FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT,
        FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE __deprecated = FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT,
        FUEL_GAUGE_TEMPERATURE_DK,
        FUEL_GAUGE_TEMPERATURE __deprecated = FUEL_GAUGE_TEMPERATURE_DK,
        FUEL_GAUGE_VOLTAGE_UV,
        FUEL_GAUGE_VOLTAGE __deprecated = FUEL_GAUGE_VOLTAGE_UV,
        FUEL_GAUGE_SBS_MODE,
        FUEL_GAUGE_CHARGE_CURRENT_UA,
        FUEL_GAUGE_CHARGE_CURRENT __deprecated = FUEL_GAUGE_CHARGE_CURRENT_UA,
        FUEL_GAUGE_CHARGE_VOLTAGE_UV,
        FUEL_GAUGE_CHARGE_VOLTAGE __deprecated = FUEL_GAUGE_CHARGE_VOLTAGE_UV,
        FUEL_GAUGE_STATUS,
        FUEL_GAUGE_DESIGN_CAPACITY,
        FUEL_GAUGE_DESIGN_VOLTAGE_MV,
        FUEL_GAUGE_DESIGN_VOLTAGE __deprecated = FUEL_GAUGE_DESIGN_VOLTAGE_MV,
        FUEL_GAUGE_SBS_ATRATE,
        FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS,
        FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL __deprecated = FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS,
        FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS,
        FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY __deprecated = FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS,
        FUEL_GAUGE_SBS_ATRATE_OK,
        FUEL_GAUGE_SBS_REMAINING_CAPACITY_ALARM,
        FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS,
        FUEL_GAUGE_SBS_REMAINING_TIME_ALARM __deprecated = FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS,
        FUEL_GAUGE_MANUFACTURER_NAME,
        FUEL_GAUGE_DEVICE_NAME,
        FUEL_GAUGE_DEVICE_CHEMISTRY,
        FUEL_GAUGE_CURRENT_DIRECTION,
        FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT,
        FUEL_GAUGE_STATE_OF_CHARGE_ALARM __deprecated = FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT,
        FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV,
        FUEL_GAUGE_LOW_VOLTAGE_ALARM __deprecated = FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV,
        FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV,
        FUEL_GAUGE_HIGH_VOLTAGE_ALARM __deprecated = FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV,
        FUEL_GAUGE_LOW_CURRENT_ALARM_UA,
        FUEL_GAUGE_LOW_CURRENT_ALARM __deprecated = FUEL_GAUGE_LOW_CURRENT_ALARM_UA,
        FUEL_GAUGE_HIGH_CURRENT_ALARM_UA,
        FUEL_GAUGE_HIGH_CURRENT_ALARM __deprecated = FUEL_GAUGE_HIGH_CURRENT_ALARM_UA,
        FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK,
        FUEL_GAUGE_LOW_TEMPERATURE_ALARM __deprecated = FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK,
        FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK,
        FUEL_GAUGE_HIGH_TEMPERATURE_ALARM __deprecated = FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK,
        FUEL_GAUGE_LOW_GPIO_ALARM_UV,
        FUEL_GAUGE_LOW_GPIO_ALARM __deprecated = FUEL_GAUGE_LOW_GPIO_ALARM_UV,
        FUEL_GAUGE_HIGH_GPIO_ALARM_UV,
        FUEL_GAUGE_HIGH_GPIO_ALARM __deprecated = FUEL_GAUGE_HIGH_GPIO_ALARM_UV,
        FUEL_GAUGE_GPIO_VOLTAGE_UV,
        FUEL_GAUGE_GPIO_VOLTAGE __deprecated = FUEL_GAUGE_GPIO_VOLTAGE_UV,
        FUEL_GAUGE_ADC_MODE,
        FUEL_GAUGE_CC_CONFIG,
        FUEL_GAUGE_STATE_OF_HEALTH,
        FUEL_GAUGE_THERM_VOLTAGE_UV,

        FUEL_GAUGE_COMMON_COUNT,
        FUEL_GAUGE_CUSTOM_BEGIN,

        FUEL_GAUGE_PROP_MAX = UINT16_MAX,
};

typedef uint16_t fuel_gauge_prop_t;

typedef int32_t fuel_gauge_custom_value_int_t;

typedef uint32_t fuel_gauge_custom_value_uint_t;

typedef bool fuel_gauge_custom_value_bool_t;

union fuel_gauge_prop_val {
        /* Fields have the format: */
        /* FUEL_GAUGE_PROPERTY_FIELD */
        /* type property_field; */

        /* Dynamic Battery Info */
        __deprecated int avg_current;
        int32_t avg_current_ua;
        bool cutoff;
        __deprecated int current;
        int32_t current_ua;
        uint32_t cycle_count;
        uint32_t connect_state;
        uint32_t flags;
        __deprecated uint32_t full_charge_capacity;
        uint32_t full_charge_capacity_uah;
        bool present_state;
        __deprecated uint32_t remaining_capacity;
        uint32_t remaining_capacity_uah;
        __deprecated uint32_t runtime_to_empty;
        uint32_t runtime_to_empty_mins;
        __deprecated uint32_t runtime_to_full;
        uint32_t runtime_to_full_mins;
        uint16_t sbs_mfr_access_word;
        __deprecated uint8_t absolute_state_of_charge;
        uint8_t absolute_state_of_charge_pct;
        __deprecated uint8_t relative_state_of_charge;
        uint8_t relative_state_of_charge_pct;
        __deprecated uint16_t temperature;
        uint16_t temperature_dk;
        __deprecated int voltage;
        int32_t voltage_uv;
        uint16_t sbs_mode;
        __deprecated uint32_t chg_current;
        uint32_t chg_current_ua;
        __deprecated uint32_t chg_voltage;
        uint32_t chg_voltage_uv;
        uint16_t fg_status;
        uint16_t design_cap;
        __deprecated uint16_t design_volt;
        uint16_t design_volt_mv;
        int16_t sbs_at_rate;
        __deprecated uint16_t sbs_at_rate_time_to_full;
        uint16_t sbs_at_rate_time_to_full_mins;
        __deprecated uint16_t sbs_at_rate_time_to_empty;
        uint16_t sbs_at_rate_time_to_empty_mins;
        bool sbs_at_rate_ok;
        uint16_t sbs_remaining_capacity_alarm;
        __deprecated uint16_t sbs_remaining_time_alarm;
        uint16_t sbs_remaining_time_alarm_mins;
        uint16_t current_direction;
        __deprecated uint8_t state_of_charge_alarm;
        uint8_t state_of_charge_alarm_pct;
        __deprecated uint32_t low_voltage_alarm;
        uint32_t low_voltage_alarm_uv;
        __deprecated uint32_t high_voltage_alarm;
        uint32_t high_voltage_alarm_uv;
        __deprecated int32_t low_current_alarm;
        int32_t low_current_alarm_ua;
        __deprecated int32_t high_current_alarm;
        int32_t high_current_alarm_ua;
        __deprecated uint16_t low_temperature_alarm;
        uint16_t low_temperature_alarm_dk;
        __deprecated uint16_t high_temperature_alarm;
        uint16_t high_temperature_alarm_dk;
        __deprecated int32_t gpio_voltage;
        int32_t gpio_voltage_uv;
        __deprecated int32_t low_gpio_alarm;
        int32_t low_gpio_alarm_uv;
        __deprecated int32_t high_gpio_alarm;
        int32_t high_gpio_alarm_uv;
        uint8_t adc_mode;
        uint8_t cc_config;
        uint8_t state_of_health;
        uint32_t therm_voltage_uv;
        fuel_gauge_custom_value_int_t custom_int;
        fuel_gauge_custom_value_uint_t custom_uint;
        fuel_gauge_custom_value_bool_t custom_bool;
};

#define SBS_GAUGE_MANUFACTURER_NAME_MAX_SIZE 20
#define SBS_GAUGE_DEVICE_NAME_MAX_SIZE       20
#define SBS_GAUGE_DEVICE_CHEMISTRY_MAX_SIZE  4

struct sbs_gauge_manufacturer_name {
        uint8_t manufacturer_name_length;
        char manufacturer_name[SBS_GAUGE_MANUFACTURER_NAME_MAX_SIZE];
} __packed;

struct sbs_gauge_device_name {
        uint8_t device_name_length;
        char device_name[SBS_GAUGE_DEVICE_NAME_MAX_SIZE];
} __packed;

struct sbs_gauge_device_chemistry {
        uint8_t device_chemistry_length;
        char device_chemistry[SBS_GAUGE_DEVICE_CHEMISTRY_MAX_SIZE];
} __packed;


typedef int (*fuel_gauge_get_property_t)(const struct device *dev, fuel_gauge_prop_t prop,
                                         union fuel_gauge_prop_val *val);

typedef int (*fuel_gauge_set_property_t)(const struct device *dev, fuel_gauge_prop_t prop,
                                         union fuel_gauge_prop_val val);

typedef int (*fuel_gauge_get_buffer_property_t)(const struct device *dev,
                                                fuel_gauge_prop_t prop_type, void *dst,
                                                size_t dst_len);

typedef int (*fuel_gauge_set_buffer_property_t)(const struct device *dev,
                                                fuel_gauge_prop_t prop_type, const void *src,
                                                size_t src_len);

typedef int (*fuel_gauge_battery_cutoff_t)(const struct device *dev);

/* Caching is entirely on the onus of the client */

__subsystem struct fuel_gauge_driver_api {
        /*
         * Note: Historically this API allowed drivers to implement a custom multi-get/set property
         * function, this was added so drivers could potentially optimize batch read with their
         * specific chip. However, it was removed because of no existing concrete case upstream.
         * If this need is demonstrated, we can add this back in as an API field.
         */
        fuel_gauge_get_property_t get_property;
        fuel_gauge_set_property_t set_property;
        fuel_gauge_get_buffer_property_t get_buffer_property;
        fuel_gauge_set_buffer_property_t set_buffer_property;
        fuel_gauge_battery_cutoff_t battery_cutoff;
};


__syscall int fuel_gauge_get_prop(const struct device *dev, fuel_gauge_prop_t prop,
                                  union fuel_gauge_prop_val *val);

static inline int z_impl_fuel_gauge_get_prop(const struct device *dev, fuel_gauge_prop_t prop,
                                             union fuel_gauge_prop_val *val)
{
        const struct fuel_gauge_driver_api *api = DEVICE_API_GET(fuel_gauge, dev);

        if (api->get_property == NULL) {
                return -ENOSYS;
        }

        return api->get_property(dev, prop, val);
}


__syscall int fuel_gauge_get_props(const struct device *dev, const fuel_gauge_prop_t *props,
                                   union fuel_gauge_prop_val *vals, size_t len);
static inline int z_impl_fuel_gauge_get_props(const struct device *dev,
                                              const fuel_gauge_prop_t *props,
                                              union fuel_gauge_prop_val *vals, size_t len)
{
        int ret;

        for (size_t i = 0; i < len; i++) {
                ret = DEVICE_API_GET(fuel_gauge, dev)->get_property(dev, props[i], vals + i);

                if (ret) {
                        return ret;
                }
        }

        return 0;
}

__syscall int fuel_gauge_set_prop(const struct device *dev, fuel_gauge_prop_t prop,
                                  union fuel_gauge_prop_val val);

static inline int z_impl_fuel_gauge_set_prop(const struct device *dev, fuel_gauge_prop_t prop,
                                             union fuel_gauge_prop_val val)
{
        const struct fuel_gauge_driver_api *api = DEVICE_API_GET(fuel_gauge, dev);

        if (api->set_property == NULL) {
                return -ENOSYS;
        }

        return api->set_property(dev, prop, val);
}
__syscall int fuel_gauge_set_props(const struct device *dev, const fuel_gauge_prop_t *props,
                                   const union fuel_gauge_prop_val *vals, size_t len);

static inline int z_impl_fuel_gauge_set_props(const struct device *dev,
                                              const fuel_gauge_prop_t *props,
                                              const union fuel_gauge_prop_val *vals, size_t len)
{
        for (size_t i = 0; i < len; i++) {
                int ret = fuel_gauge_set_prop(dev, props[i], vals[i]);

                if (ret) {
                        return ret;
                }
        }

        return 0;
}


__syscall int fuel_gauge_get_buffer_prop(const struct device *dev, fuel_gauge_prop_t prop_type,
                                         void *dst, size_t dst_len);

static inline int z_impl_fuel_gauge_get_buffer_prop(const struct device *dev,
                                                    fuel_gauge_prop_t prop_type, void *dst,
                                                    size_t dst_len)
{
        const struct fuel_gauge_driver_api *api = DEVICE_API_GET(fuel_gauge, dev);

        if (api->get_buffer_property == NULL) {
                return -ENOSYS;
        }

        return api->get_buffer_property(dev, prop_type, dst, dst_len);
}

__syscall int fuel_gauge_set_buffer_prop(const struct device *dev, fuel_gauge_prop_t prop_type,
                                         const void *src, size_t src_len);

static inline int z_impl_fuel_gauge_set_buffer_prop(const struct device *dev,
                                                    fuel_gauge_prop_t prop_type, const void *src,
                                                    size_t src_len)
{
        const struct fuel_gauge_driver_api *api = DEVICE_API_GET(fuel_gauge, dev);

        if (api->set_buffer_property == NULL) {
                return -ENOSYS;
        }

        return api->set_buffer_property(dev, prop_type, src, src_len);
}

__syscall int fuel_gauge_battery_cutoff(const struct device *dev);

static inline int z_impl_fuel_gauge_battery_cutoff(const struct device *dev)
{
        const struct fuel_gauge_driver_api *api = DEVICE_API_GET(fuel_gauge, dev);

        if (api->battery_cutoff == NULL) {
                return -ENOSYS;
        }

        return api->battery_cutoff(dev);
}


#ifdef __cplusplus
}
#endif /* __cplusplus */

#include <zephyr/syscalls/fuel_gauge.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_FUEL_GAUGE_H_ */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 Google LLC。

版权（Copyright）：2023 Microsoft Corporation。

版权（Copyright）：© 2025 Philipp Steiner。

版权（Copyright）：© Qualcomm Technologies, Inc. and/or its subsidiaries.。

版权（Copyright）：© 2026 Analog Devices Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 31 行

条件编译标记：`__cplusplus`。

### 注释 3：原第 231 行

字段格式如下：

### 注释 4：原第 232 行

电量计属性字段（Fuel Gauge Property Field）：`FUEL_GAUGE_PROPERTY_FIELD`。

### 注释 5：原第 233 行

字段声明格式：`type property_field;`。

### 注释 6：原第 235 行

动态电池信息（Dynamic Battery Info）。

### 注释 7：原第 529 行

缓存（Caching）完全由客户端（Client）负责。

### 注释 8：原第 535 行

注意（Note）：此 API 过去允许驱动实现自定义的多属性获取／设置函数（Custom Multi-Get / Set Property Function），以便驱动可能利用特定芯片优化批量读取（Batch Read）。但由于上游没有实际使用案例，该功能被移除。如果有证据表明确实需要，可以将其作为 API 字段（Field）重新加入。

### 注释 9：原第 753 行

条件编译标记：`__cplusplus`。

### 注释 10：原第 757 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FUEL_GAUGE_H_`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [fuel_gauge_prop_type](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gae49908857800bdd010d59895cfad9171)
- [FUEL_GAUGE_AVG_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a1dc93924386cfd048fb9a1865adb9904)
- [FUEL_GAUGE_AVG_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396)
- [FUEL_GAUGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7ca368502befbe58ac68c1aaa24d32ee)
- [FUEL_GAUGE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354)
- [FUEL_GAUGE_CHARGE_CUTOFF](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f)
- [FUEL_GAUGE_CYCLE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984)
- [FUEL_GAUGE_CONNECT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d)
- [FUEL_GAUGE_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c)
- [FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171afa3d404c62c20357d29954c25b8df174)
- [FUEL_GAUGE_FULL_CHARGE_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9)
- [FUEL_GAUGE_PRESENT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b)
- [FUEL_GAUGE_REMAINING_CAPACITY_UAH](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac265b9e9137c4dbd424d833c50b2d828)
- [FUEL_GAUGE_REMAINING_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4)
- [FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a3515db092af7dfa2d9a8b879e0b56d1e)
- [FUEL_GAUGE_RUNTIME_TO_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd)
- [FUEL_GAUGE_RUNTIME_TO_FULL_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a8d0ac3331a389394b603a00d0a47498f)
- [FUEL_GAUGE_RUNTIME_TO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399)
- [FUEL_GAUGE_SBS_MFR_ACCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd)
- [FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4feeb0b0add43143c8f99299af5859ce)
- [FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee)
- [FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ad4d9f765c0e0e388b71ef1db09034f50)
- [FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b)
- [FUEL_GAUGE_TEMPERATURE_DK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a2026a7272e1a6c301ea53282f919980b)
- [FUEL_GAUGE_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009)
- [FUEL_GAUGE_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171afa8f22eecf3cbc2b5b50a69ce974f99c)
- [FUEL_GAUGE_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71)
- [FUEL_GAUGE_SBS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae)
- [FUEL_GAUGE_CHARGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a76ca40b38e4326237c94b4f38dc1680b)
- [FUEL_GAUGE_CHARGE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e)
- [FUEL_GAUGE_CHARGE_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aec015967b3aef33ca2728058d6d73b55)
- [FUEL_GAUGE_CHARGE_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920)
- [FUEL_GAUGE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40)
- [FUEL_GAUGE_DESIGN_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67)
- [FUEL_GAUGE_DESIGN_VOLTAGE_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac1ea4d609b9286807c9c589ed0b731eb)
- [FUEL_GAUGE_DESIGN_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf)
- [FUEL_GAUGE_SBS_ATRATE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58)
- [FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4c66491e317f6b27b2f3db0cdda89b1b)
- [FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70)
- [FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4b599ee88b5ddbb0bdb8f30c1fe2796a)
- [FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0)
- [FUEL_GAUGE_SBS_ATRATE_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec)
- [FUEL_GAUGE_SBS_REMAINING_CAPACITY_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2)
- [FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a6d6fa90dd558d14f039b9cd9fcb15b70)
- [FUEL_GAUGE_SBS_REMAINING_TIME_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a)
- [FUEL_GAUGE_MANUFACTURER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8)
- [FUEL_GAUGE_DEVICE_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10)
- [FUEL_GAUGE_DEVICE_CHEMISTRY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9)
- [FUEL_GAUGE_CURRENT_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ae29582cdad457499ad83cee06ca3ff21)
- [FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a0a5d8d32ccf8658f88642f33872d94b8)
- [FUEL_GAUGE_STATE_OF_CHARGE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abd2a4cc73d651fa54c9dab634198aeae)
- [FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a84b472b072be9494cf7d5f9027421772)
- [FUEL_GAUGE_LOW_VOLTAGE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ad1a57cfd758250b2e3f4b5c4abeac9e7)
- [FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a367b0beb959a116e81de9cd5f2adbe43)
- [FUEL_GAUGE_HIGH_VOLTAGE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac7e9e36e2c622474129cf4f51b1782c6)
- [FUEL_GAUGE_LOW_CURRENT_ALARM_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a923809dbcdd526822ffde000137eccee)
- [FUEL_GAUGE_LOW_CURRENT_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a58c1b0a39345a7006a8ee0ad6ce01bb4)
- [FUEL_GAUGE_HIGH_CURRENT_ALARM_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a09809ae39a4c79e1a35095300d838c78)
- [FUEL_GAUGE_HIGH_CURRENT_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4bcd9bf3d2c9c081d9186d30e39ab32a)
- [FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a328886a8b2318367bb968e4a6c9eba1f)
- [FUEL_GAUGE_LOW_TEMPERATURE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a55cf7fcc30be436fd51d79f9ad675d5c)
- [FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ae8a61b0db58687634ff57f3c536dfd40)
- [FUEL_GAUGE_HIGH_TEMPERATURE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a3c5e7d0ede99656b407f25f114adf24d)
- [FUEL_GAUGE_LOW_GPIO_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a9b300c9edad178b7563f7d5ea3b88833)
- [FUEL_GAUGE_LOW_GPIO_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abfc512152bf56f62d1d67660e03dc2e9)
- [FUEL_GAUGE_HIGH_GPIO_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a53744eaac0496db3619baa3b42f96ce6)
- [FUEL_GAUGE_HIGH_GPIO_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa993fbb1a9e04554fff73c7e59cd3783)
- [FUEL_GAUGE_GPIO_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa7351ed7cc8ece7cacb97c4308048fb2)
- [FUEL_GAUGE_GPIO_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aea985dd0c89e41bdd018a2dce143d9b4)
- [FUEL_GAUGE_ADC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aeba3b1d8a5239d4afbe8f1d4753583aa)
- [FUEL_GAUGE_CC_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac0754d083fa22c7f07cfd8846b3bdbd5)
- [FUEL_GAUGE_STATE_OF_HEALTH](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a34dbed1768f1787d8269ef30c2478c53)
- [FUEL_GAUGE_THERM_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aae228a0e3ab76368fbddeff8dd5d1458)
- [FUEL_GAUGE_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815)
- [FUEL_GAUGE_CUSTOM_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584)
- [FUEL_GAUGE_PROP_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81)
- [UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [fuel_gauge_custom_value_int_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gaf8c7f6c4f49dd420df6841c43c41d615)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [fuel_gauge_custom_value_uint_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga08e4dae43d5169da58af32ec419ef9e8)
- [fuel_gauge_custom_value_bool_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga44fd24de7d165388a87e6dd74f6547af)
- [fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)
- [avg_current](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ad96f07db337c038466dd17401c076d38)
- [avg_current_ua](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a8d349a8fe357fd30ba4d458dd8260f5a)
- [cutoff](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ac8e8e74c2b1f2e0c1f4e65eecf5a745a)
- [current](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a9bed3247063f069bb92b2902cc5ff468)
- [current_ua](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ac8a4263fede43ebcd28cff1c66e413b1)
- [cycle_count](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ac27ae67a315a7204cea6e88962758587)
- [connect_state](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a9f4653e270e93280bd6bed6022c135b0)
- [flags](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#adeb93ed2120e808aac815dcbdf69067f)
- [full_charge_capacity](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aa29f7163a1637b6aa8cd6a15dc99d55b)
- [full_charge_capacity_uah](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#af421dee221486f53d71d0fb8e6c4df1c)
- [present_state](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a4916bb50489c5f70335da2f11ed9477e)
- [remaining_capacity](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#adecf57aa90e2b5d483cfd889ec512400)
- [remaining_capacity_uah](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ab19f11342d10502937595b535db09c7a)
- [runtime_to_empty](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ae716bdf1346dc7767d98526db6083008)
- [runtime_to_empty_mins](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#af40db6b3dba16b20097d0767e51a07c5)
- [runtime_to_full](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a2c77e8de7fa40fadfa13dfd4c94df804)
- [runtime_to_full_mins](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a600a90fd8d847bd29ffd9d96822abdb8)
- [sbs_mfr_access_word](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a957025a2a9fb7709e2bf478f15fd31a0)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [absolute_state_of_charge](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a33297ff5bf70b510272eddf77ced411e)
- [absolute_state_of_charge_pct](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ae1d5c18887cb8dab5ad070801992be1a)
- [relative_state_of_charge](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a45b20c5118f7ee408d507b94e6cae1dc)
- [relative_state_of_charge_pct](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a94893761a1f77a9c0e746c34e5bb6e61)
- [temperature](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a36528b111568bd1c90859e454610fd9f)
- [temperature_dk](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a7d943c31ad7dd53d16bfded98e70b332)
- [voltage](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#abec5cadefa09e088620a9598dec9c473)
- [voltage_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aa52341a118d1445ee762ba1563406441)
- [sbs_mode](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a7fc0551e303de56e0eb6bdac1ecaccd0)
- [chg_current](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a6f74626deef4debbd8dfe6c188984d1b)
- [chg_current_ua](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a740700d2c6c6db83617d8dfd964e34f7)
- [chg_voltage](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a8743f7e7a05919b5469e39527b697e62)
- [chg_voltage_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ae40e0074599fa69ea5b9e9012c14452b)
- [fg_status](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a65607bb9ba43022c9c566646d4763aac)
- [design_cap](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a20aa5736b0ac3c5adda10152660de275)
- [design_volt](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a11626713aef0445ad613a5976401d09e)
- [design_volt_mv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a06edf4e066a3b655cdfd4ab732e93b7a)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [sbs_at_rate](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aa5529fea5cfe765be9b66f5fad96ab2f)
- [sbs_at_rate_time_to_full](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aeeeddb48f22b54f90c603d58e9ffa9a5)
- [sbs_at_rate_time_to_full_mins](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a8bc68c65571afb6856e7e1e6cb33a5e4)
- [sbs_at_rate_time_to_empty](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a7c8b6f9ee98e5b97ddc85b7e72cea4a8)
- [sbs_at_rate_time_to_empty_mins](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#adbfa0be8653107875e91edd5db40265d)
- [sbs_at_rate_ok](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a9b5015878c9a77d9c8330139f94843b7)
- [sbs_remaining_capacity_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a818ab7faf8f51d4d1a5c5f070d54b997)
- [sbs_remaining_time_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aa0e46c727bb31acb5d41ce4bc6d5b106)
- [sbs_remaining_time_alarm_mins](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a0b6878d02d4d5a3865e8ca8d57951914)
- [current_direction](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a52b70375d15ed878d62d1390c3144cd8)
- [state_of_charge_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aa901ef363509234577d73958984862a4)
- [state_of_charge_alarm_pct](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ab43ccbb0a1443e64d26e498d31d1a240)
- [low_voltage_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aff81db28e93cb70ebea6793e4493915f)
- [low_voltage_alarm_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aee04c49d39652837420039fb968ecea5)
- [high_voltage_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a2b044d7e33e98fd0c0cead2a3de61431)
- [high_voltage_alarm_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#acf5b8f9b1ff3b3c5b5547d4920dbd7f2)
- [low_current_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aaa55eae9e98203e5f1847d6162d1d28e)
- [low_current_alarm_ua](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a49e894ef1b0f7be9c5a1dba12a8cff41)
- [high_current_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ab4aafbc07557b2c15396b8bfc66d7e9b)
- [high_current_alarm_ua](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#adab6e7b86aea46fdb9f5bc99ae87e431)
- [low_temperature_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ad8d424fbbe3124cde5e82b74957a4885)
- [low_temperature_alarm_dk](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a163ecf351a2a538cac53757ad402dde0)
- [high_temperature_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a9dd892b613881fda89635046b3ef7942)
- [high_temperature_alarm_dk](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ac651ea27014b7e61fdf5e847d70a188c)
- [gpio_voltage](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ad600545303f0fa6e2853396e83d87fdd)
- [gpio_voltage_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ab969822a9d1bc32345d02805c6f9b204)
- [low_gpio_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aef3ced90ca261ec7501778a41f12963d)
- [low_gpio_alarm_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a4ce4046d3284afa7fd2e37d510cf4fd2)
- [high_gpio_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a0bf74ed2b92b7b0920cf90ef7119aa36)
- [high_gpio_alarm_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ab553a7b8b86225bd6c13c7f0c0a5e658)
- [adc_mode](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a3b2dc6e92a6b4158115e76c78061fe16)
- [cc_config](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aaee1a60dac0770780bd45c1549fbf819)
- [state_of_health](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a1638b4b54bf57af650832e53f9ce90a4)
- [therm_voltage_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a9e12460af8ae1a0ba0d1838e977e7a59)
- [custom_int](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a63ce57eb11373a7e899d6324f4335749)
- [custom_uint](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a21fb17e3d083c0a26f592f38b07b797e)
- [custom_bool](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aec778f250686b960c7328c27b48d5a17)
- [sbs_gauge_manufacturer_name](../device_power_control_model_reference/P084_sbs_gauge_manufacturer_name_结构体.md)
- [manufacturer_name_length](../device_power_control_model_reference/P084_sbs_gauge_manufacturer_name_结构体.md#a13a5902df94842f7a69a8028b8708ced)
- [manufacturer_name](../device_power_control_model_reference/P084_sbs_gauge_manufacturer_name_结构体.md#a40af61fe30263b21e9b9c92383562b0d)
- [SBS_GAUGE_MANUFACTURER_NAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga824e00f1d607cdfe2598625f154636f1)
- [sbs_gauge_device_name](../device_power_control_model_reference/P083_sbs_gauge_device_name_结构体.md)
- [device_name_length](../device_power_control_model_reference/P083_sbs_gauge_device_name_结构体.md#a5e599e923ccbdc7eb89ab6f7e1d3a662)
- [device_name](../device_power_control_model_reference/P083_sbs_gauge_device_name_结构体.md#a6699e048a1ca5feb2cadb05169bcfa5f)
- [SBS_GAUGE_DEVICE_NAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga41b8379542b9cbd0b3ee9e1bbe4bc599)
- [sbs_gauge_device_chemistry](../device_power_control_model_reference/P082_sbs_gauge_device_chemistry_结构体.md)
- [device_chemistry_length](../device_power_control_model_reference/P082_sbs_gauge_device_chemistry_结构体.md#a340cfddcc1ad7a758f75208b38208df4)
- [device_chemistry](../device_power_control_model_reference/P082_sbs_gauge_device_chemistry_结构体.md#a2a3990be7618165d88790e53ac7b4e72)
- [SBS_GAUGE_DEVICE_CHEMISTRY_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gafe9bdc00d856d4cc787265edb7eb0ed2)
- [fuel_gauge_get_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gaed940ae925236ad2f25cf05d78304568)
- [device](../device_reference/P002_设备对象结构.md)
- [fuel_gauge_set_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gae87a20a20f4f1fbb74d72afb2bcee4c9)
- [fuel_gauge_get_buffer_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)
- [fuel_gauge_set_buffer_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#gae5908067ab2a8c70c517d3e12eb364c1)
- [fuel_gauge_battery_cutoff_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface__backend.html#ga698c8f84da7d1cbe7db1fc024e2388b7)
- [fuel_gauge_driver_api](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md)
- [get_property](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md#ab729a85c69e561f1ca0aca9f8eb22d91)
- [set_property](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md#a74815d3bb721452bfd3e35cd1221b223)
- [get_buffer_property](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md#ad12c13461173177d1c81846a85a3f570)
- [set_buffer_property](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md#aa9963e6744222271ab45e2eabbf69f87)
- [battery_cutoff](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md#a406816c19022eea26f0fd61fb21d234c)
- [fuel_gauge_get_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gab84999beab9a43241992945a3b2d37e1)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [fuel_gauge_get_props](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gaf8a1fed5f6af9c25a12130c481411603)
- [fuel_gauge_set_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga936be681a82f173b664ae2187bc5a73d)
- [fuel_gauge_set_props](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gac8efb10ccb6f510dc92618e218c1df9b)
- [fuel_gauge_get_buffer_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga7e6cb77d2d4dd7a0feb25c92d031614c)
- [fuel_gauge_set_buffer_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gac63f43b6023b9f2183001d6876fe328a)
- [fuel_gauge_battery_cutoff](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga763a40688dc8fc6a0ba85fdc79178ebc)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [fuel_gauge_driver_api::battery_cutoff](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md#a406816c19022eea26f0fd61fb21d234c)
- [fuel_gauge_driver_api::set_property](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md#a74815d3bb721452bfd3e35cd1221b223)
- [fuel_gauge_driver_api::set_buffer_property](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md#aa9963e6744222271ab45e2eabbf69f87)
- [fuel_gauge_driver_api::get_property](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md#ab729a85c69e561f1ca0aca9f8eb22d91)
- [fuel_gauge_driver_api::get_buffer_property](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md#ad12c13461173177d1c81846a85a3f570)
- [sbs_gauge_device_chemistry::device_chemistry](../device_power_control_model_reference/P082_sbs_gauge_device_chemistry_结构体.md#a2a3990be7618165d88790e53ac7b4e72)
- [sbs_gauge_device_chemistry::device_chemistry_length](../device_power_control_model_reference/P082_sbs_gauge_device_chemistry_结构体.md#a340cfddcc1ad7a758f75208b38208df4)
- [sbs_gauge_device_name::device_name_length](../device_power_control_model_reference/P083_sbs_gauge_device_name_结构体.md#a5e599e923ccbdc7eb89ab6f7e1d3a662)
- [sbs_gauge_device_name::device_name](../device_power_control_model_reference/P083_sbs_gauge_device_name_结构体.md#a6699e048a1ca5feb2cadb05169bcfa5f)
- [sbs_gauge_manufacturer_name::manufacturer_name_length](../device_power_control_model_reference/P084_sbs_gauge_manufacturer_name_结构体.md#a13a5902df94842f7a69a8028b8708ced)
- [sbs_gauge_manufacturer_name::manufacturer_name](../device_power_control_model_reference/P084_sbs_gauge_manufacturer_name_结构体.md#a40af61fe30263b21e9b9c92383562b0d)
- [fuel_gauge_prop_val::design_volt_mv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a06edf4e066a3b655cdfd4ab732e93b7a)
- [fuel_gauge_prop_val::sbs_remaining_time_alarm_mins](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a0b6878d02d4d5a3865e8ca8d57951914)
- [fuel_gauge_prop_val::high_gpio_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a0bf74ed2b92b7b0920cf90ef7119aa36)
- [fuel_gauge_prop_val::design_volt](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a11626713aef0445ad613a5976401d09e)
- [fuel_gauge_prop_val::state_of_health](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a1638b4b54bf57af650832e53f9ce90a4)
- [fuel_gauge_prop_val::low_temperature_alarm_dk](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a163ecf351a2a538cac53757ad402dde0)
- [fuel_gauge_prop_val::design_cap](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a20aa5736b0ac3c5adda10152660de275)
- [fuel_gauge_prop_val::custom_uint](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a21fb17e3d083c0a26f592f38b07b797e)
- [fuel_gauge_prop_val::high_voltage_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a2b044d7e33e98fd0c0cead2a3de61431)
- [fuel_gauge_prop_val::runtime_to_full](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a2c77e8de7fa40fadfa13dfd4c94df804)
- [fuel_gauge_prop_val::absolute_state_of_charge](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a33297ff5bf70b510272eddf77ced411e)
- [fuel_gauge_prop_val::temperature](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a36528b111568bd1c90859e454610fd9f)
- [fuel_gauge_prop_val::adc_mode](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a3b2dc6e92a6b4158115e76c78061fe16)
- [fuel_gauge_prop_val::relative_state_of_charge](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a45b20c5118f7ee408d507b94e6cae1dc)
- [fuel_gauge_prop_val::present_state](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a4916bb50489c5f70335da2f11ed9477e)
- [fuel_gauge_prop_val::low_current_alarm_ua](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a49e894ef1b0f7be9c5a1dba12a8cff41)
- [fuel_gauge_prop_val::low_gpio_alarm_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a4ce4046d3284afa7fd2e37d510cf4fd2)
- [fuel_gauge_prop_val::current_direction](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a52b70375d15ed878d62d1390c3144cd8)
- [fuel_gauge_prop_val::runtime_to_full_mins](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a600a90fd8d847bd29ffd9d96822abdb8)
- [fuel_gauge_prop_val::custom_int](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a63ce57eb11373a7e899d6324f4335749)
- [fuel_gauge_prop_val::fg_status](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a65607bb9ba43022c9c566646d4763aac)
- [fuel_gauge_prop_val::chg_current](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a6f74626deef4debbd8dfe6c188984d1b)
- [fuel_gauge_prop_val::chg_current_ua](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a740700d2c6c6db83617d8dfd964e34f7)
- [fuel_gauge_prop_val::sbs_at_rate_time_to_empty](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a7c8b6f9ee98e5b97ddc85b7e72cea4a8)
- [fuel_gauge_prop_val::temperature_dk](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a7d943c31ad7dd53d16bfded98e70b332)
- [fuel_gauge_prop_val::sbs_mode](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a7fc0551e303de56e0eb6bdac1ecaccd0)
- [fuel_gauge_prop_val::sbs_remaining_capacity_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a818ab7faf8f51d4d1a5c5f070d54b997)
- [fuel_gauge_prop_val::chg_voltage](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a8743f7e7a05919b5469e39527b697e62)
- [fuel_gauge_prop_val::sbs_at_rate_time_to_full_mins](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a8bc68c65571afb6856e7e1e6cb33a5e4)
- [fuel_gauge_prop_val::avg_current_ua](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a8d349a8fe357fd30ba4d458dd8260f5a)
- [fuel_gauge_prop_val::relative_state_of_charge_pct](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a94893761a1f77a9c0e746c34e5bb6e61)
- [fuel_gauge_prop_val::sbs_mfr_access_word](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a957025a2a9fb7709e2bf478f15fd31a0)
- [fuel_gauge_prop_val::sbs_at_rate_ok](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a9b5015878c9a77d9c8330139f94843b7)
- [fuel_gauge_prop_val::current](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a9bed3247063f069bb92b2902cc5ff468)
- [fuel_gauge_prop_val::high_temperature_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a9dd892b613881fda89635046b3ef7942)
- [fuel_gauge_prop_val::therm_voltage_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a9e12460af8ae1a0ba0d1838e977e7a59)
- [fuel_gauge_prop_val::connect_state](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#a9f4653e270e93280bd6bed6022c135b0)
- [fuel_gauge_prop_val::sbs_remaining_time_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aa0e46c727bb31acb5d41ce4bc6d5b106)
- [fuel_gauge_prop_val::full_charge_capacity](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aa29f7163a1637b6aa8cd6a15dc99d55b)
- [fuel_gauge_prop_val::voltage_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aa52341a118d1445ee762ba1563406441)
- [fuel_gauge_prop_val::sbs_at_rate](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aa5529fea5cfe765be9b66f5fad96ab2f)
- [fuel_gauge_prop_val::state_of_charge_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aa901ef363509234577d73958984862a4)
- [fuel_gauge_prop_val::low_current_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aaa55eae9e98203e5f1847d6162d1d28e)
- [fuel_gauge_prop_val::cc_config](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aaee1a60dac0770780bd45c1549fbf819)
- [fuel_gauge_prop_val::remaining_capacity_uah](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ab19f11342d10502937595b535db09c7a)
- [fuel_gauge_prop_val::state_of_charge_alarm_pct](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ab43ccbb0a1443e64d26e498d31d1a240)
- [fuel_gauge_prop_val::high_current_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ab4aafbc07557b2c15396b8bfc66d7e9b)
- [fuel_gauge_prop_val::high_gpio_alarm_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ab553a7b8b86225bd6c13c7f0c0a5e658)
- [fuel_gauge_prop_val::gpio_voltage_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ab969822a9d1bc32345d02805c6f9b204)
- [fuel_gauge_prop_val::voltage](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#abec5cadefa09e088620a9598dec9c473)
- [fuel_gauge_prop_val::cycle_count](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ac27ae67a315a7204cea6e88962758587)
- [fuel_gauge_prop_val::high_temperature_alarm_dk](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ac651ea27014b7e61fdf5e847d70a188c)
- [fuel_gauge_prop_val::current_ua](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ac8a4263fede43ebcd28cff1c66e413b1)
- [fuel_gauge_prop_val::cutoff](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ac8e8e74c2b1f2e0c1f4e65eecf5a745a)
- [fuel_gauge_prop_val::high_voltage_alarm_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#acf5b8f9b1ff3b3c5b5547d4920dbd7f2)
- [fuel_gauge_prop_val::gpio_voltage](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ad600545303f0fa6e2853396e83d87fdd)
- [fuel_gauge_prop_val::low_temperature_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ad8d424fbbe3124cde5e82b74957a4885)
- [fuel_gauge_prop_val::avg_current](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ad96f07db337c038466dd17401c076d38)
- [fuel_gauge_prop_val::high_current_alarm_ua](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#adab6e7b86aea46fdb9f5bc99ae87e431)
- [fuel_gauge_prop_val::sbs_at_rate_time_to_empty_mins](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#adbfa0be8653107875e91edd5db40265d)
- [fuel_gauge_prop_val::flags](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#adeb93ed2120e808aac815dcbdf69067f)
- [fuel_gauge_prop_val::remaining_capacity](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#adecf57aa90e2b5d483cfd889ec512400)
- [fuel_gauge_prop_val::absolute_state_of_charge_pct](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ae1d5c18887cb8dab5ad070801992be1a)
- [fuel_gauge_prop_val::chg_voltage_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ae40e0074599fa69ea5b9e9012c14452b)
- [fuel_gauge_prop_val::runtime_to_empty](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#ae716bdf1346dc7767d98526db6083008)
- [fuel_gauge_prop_val::custom_bool](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aec778f250686b960c7328c27b48d5a17)
- [fuel_gauge_prop_val::low_voltage_alarm_uv](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aee04c49d39652837420039fb968ecea5)
- [fuel_gauge_prop_val::sbs_at_rate_time_to_full](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aeeeddb48f22b54f90c603d58e9ffa9a5)
- [fuel_gauge_prop_val::low_gpio_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aef3ced90ca261ec7501778a41f12963d)
- [fuel_gauge_prop_val::runtime_to_empty_mins](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#af40db6b3dba16b20097d0767e51a07c5)
- [fuel_gauge_prop_val::full_charge_capacity_uah](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#af421dee221486f53d71d0fb8e6c4df1c)
- [fuel_gauge_prop_val::low_voltage_alarm](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md#aff81db28e93cb70ebea6793e4493915f)

---

[上一章](P008_esai.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P010_gd32e10x-clocks.h_源码浏览.md)
