---
id: learning.zephyr-docs.api-source-reference.page-492
title: mchp_clock_pic32cm_jh.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第492章\_mchp\_clock\_pic32cm\_jh.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h.html)。

## 492.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00038"></a>
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
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
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
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="foldopen00147"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
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
<a id="l00161"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="foldopen00175"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ga4303aa06f4b9a93874f2d26406e788e3"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gaca271f1fae614cbd8c12fed31bcb64ea"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga073dab68c78edce3985eb201a039a989a198b4b6273b991b0795e574036b3e177"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga073dab68c78edce3985eb201a039a989a26b8d25a8d166e0b8e79c77312897145"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga073dab68c78edce3985eb201a039a989a7ae946790cdbcec68bb8f7e8b35cd9fe"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga2b83aa5b88c064d44d3a0ef7661a15cfa9095a4473e6e218ea0d2715695ecb2ff"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga2b83aa5b88c064d44d3a0ef7661a15cfaa377b029b64d15627a7bee121ffc6050"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga2b83aa5b88c064d44d3a0ef7661a15cfad5e72f091a71486e117cdea5b8381dff"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga2b83aa5b88c064d44d3a0ef7661a15cfafaa5cfa19e470035ad1cec308aa63f7b"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3a06c5e0bcabf7b54347f7e2c4cb54f2e1"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3a1d3ab3603b8569a32492a33a7343b51b"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3a4980f4845c33d559860cb4a2c8cbe8ab"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3a5341cf2520f14d53305b552e29d336af"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3a68d97439120b74cfb174d6d9f7254c57"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3a8dceb2229cb86ce500350fcb3f795a38"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3a97968c136ce06b10ff5b78fdeec82c6b"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3aa6e359c000dc41599beaf5937d7b91b1"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3ac2e281fba8772d11634fa74f1559e6ae"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3ac5a35357502c5bf9ca76f5a935efbcb1"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3ac808175c0850ab5634c87fc49a2cde89"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3adb65fbb10b4703d719fe61dd044da5e9"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3ae15895137cfed2a01dc07fd073c7f4f0"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3af1947f866264e2b7eca4a0dbba0223cd"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3af8fcf13844de18b99b21de542e31f2d9"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga4303aa06f4b9a93874f2d26406e788e3afce32516f8303f06461a7edb1512cb4b"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaa1d753cfcae1b5d0249908d1567257cbc"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaa2b4dbfa6f3b2985c25df5457babcfc19"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaa2e3099c6db41c26e126ea236ae1f4917"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaa49e87978ba1e4471c0dc76705950f7d7"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaa5049effd0b7a893f2e278b857010e24f"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaa5bb7c103fe4f9548da6f6ff38b8e4fe6"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaa8f6301943a69f328ac49e0b302c6e1e1"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaa9e1c784e19edd414b2c51196fb0ea630"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaab1e1b66c6b826cbc9077fb579c73466b"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaabdb11235f190deb557d9e19d4c24618c"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaad1027fef245b5a24b80e383981d40913"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_ggaca271f1fae614cbd8c12fed31bcb64eaad463d37743aa9dce5a24ea0b9f2f6f83"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_ga073dab68c78edce3985eb201a039a989"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_ga2b83aa5b88c064d44d3a0ef7661a15cf"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_ga5835567db8d16c4eeb7a03b843ac6254"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_gaab34442b0d6c171691ae299675542777"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_gaca271f1fae614cbd8c12fed31bcb64ea"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a002e232f09f2da92b359ecd1543465d0"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a2b83aa5b88c064d44d3a0ef7661a15cf"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a2b83aa5b88c064d44d3a0ef7661a15cfae738ec040a54d0b171192d122abdd332"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a5835567db8d16c4eeb7a03b843ac6254"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a5835567db8d16c4eeb7a03b843ac6254a688a2dbe64b6a818ab84f26cc983b3f0"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a5835567db8d16c4eeb7a03b843ac6254a9f893cbec63df56227f17098ddf70074"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a5835567db8d16c4eeb7a03b843ac6254ab071663992b6be65b6f77442239d3157"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a5835567db8d16c4eeb7a03b843ac6254ac52aba85d20e21bd3135cc46e467dbfc"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a5835567db8d16c4eeb7a03b843ac6254ace4fa9213f609c27198c75f17b0f7beb"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a5835567db8d16c4eeb7a03b843ac6254ad251e58f232eaa9d45cce47e600b506f"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a5835567db8d16c4eeb7a03b843ac6254ae11a4d93aaafcfaeed5a7cc6e0a1de89"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a5835567db8d16c4eeb7a03b843ac6254aefa35c60f9274b62c0b829c1c24a571b"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a9b6955116dae7fa53c8dad373a1ef9c9"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a20bf106031eb19f25b8e3b1250033088"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a69bd2c6d8f016e8ecdfd07fba7268dcc"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a71ead69f87ccd57496b0467a6264d411"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a9cbc78f597c2930b36280c59164e12ae"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777aff9b0bedc5de2cfe3259df2910ab55f9"></a>
<a id="amchp__pic32cm__jh__clock_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructclock__mchp__subsys__fdpll__config_html"></a>
<a id="astructclock__mchp__subsys__fdpll__config_html_a1ae355aede60d06e8ae395517ba5f7cd"></a>
<a id="astructclock__mchp__subsys__fdpll__config_html_a24bc48331e32436c8f6c2cf3c76e7ed5"></a>
<a id="astructclock__mchp__subsys__fdpll__config_html_a763e54cbab07657be8eff1b8ca45f65e"></a>
<a id="astructclock__mchp__subsys__fdpll__config_html_a8057b8d7233e11008eb81f798083ad6a"></a>
<a id="astructclock__mchp__subsys__fdpll__config_html_aa081dea6b720e1bf79c4eb1ba139c664"></a>
<a id="astructclock__mchp__subsys__fdpll__config_html_aa3e53c57298528f9033e08cc238f6891"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html_a59f3f908c254d4299164b5fea5885514"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html_aeb553aa051490aefb8d38cc9ce7e8166"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html_af803dcb746c1438f6e08ac30042d3651"></a>
<a id="astructclock__mchp__subsys__gclkperiph__config_html"></a>
<a id="astructclock__mchp__subsys__gclkperiph__config_html_a1727b4df3eb0dcff7365909002cef636"></a>
<a id="astructclock__mchp__subsys__mclkcpu__config_html"></a>
<a id="astructclock__mchp__subsys__mclkcpu__config_html_a380cc94c6ed19143a29f2590af21f672"></a>
<a id="astructclock__mchp__subsys__osc32k__config_html"></a>
<a id="astructclock__mchp__subsys__osc32k__config_html_a8343157fa2c56424b9fc9768237e1922"></a>
<a id="astructclock__mchp__subsys__osc32k__config_html_ace2f42ea255ec213ed207b18538a2a2d"></a>
<a id="astructclock__mchp__subsys__osc48m__config_html"></a>
<a id="astructclock__mchp__subsys__osc48m__config_html_a191da6844eba2d9c20d4b21bedf825da"></a>
<a id="astructclock__mchp__subsys__osc48m__config_html_aa2e9756157bdb1d71ff586c7baa5d856"></a>
<a id="astructclock__mchp__subsys__osc48m__config_html_ad5ee1cd0de32cff6c1e3726e56b33efc"></a>
<a id="astructclock__mchp__subsys__rtc__config_html"></a>
<a id="astructclock__mchp__subsys__rtc__config_html_af6a74f1140ddab14f3e8f4642284f443"></a>
<a id="astructclock__mchp__subsys__xosc32k__config_html"></a>
<a id="astructclock__mchp__subsys__xosc32k__config_html_a44925c2cea8adc89c1d5910156b4f105"></a>
<a id="astructclock__mchp__subsys__xosc32k__config_html_afb7ecdb2ad0168376649c5acb0c5c765"></a>
<a id="astructclock__mchp__subsys__xosc__config_html"></a>
<a id="astructclock__mchp__subsys__xosc__config_html_a298c2524a043091ab6f591759d03c72b"></a>
<a id="astructclock__mchp__subsys__xosc__config_html_a51e27943063374fa67b03509d8d8b962"></a>

```c
/*
 * Copyright (c) 2025 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CM_JH_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CM_JH_H_

#include <zephyr/dt-bindings/clock/mchp_pic32cm_jh_clock.h>


struct clock_mchp_subsys_xosc_config {
        bool on_demand_en;

        bool run_in_standby_en;
};

enum clock_mchp_osc48m_divider_freq {
        CLOCK_MCHP_DIVIDER_48_MHZ,
        CLOCK_MCHP_DIVIDER_24_MHZ,
        CLOCK_MCHP_DIVIDER_16_MHZ,
        CLOCK_MCHP_DIVIDER_12_MHZ,
        CLOCK_MCHP_DIVIDER_9_6_MHZ,
        CLOCK_MCHP_DIVIDER_8_MHZ,
        CLOCK_MCHP_DIVIDER_6_86_MHZ,
        CLOCK_MCHP_DIVIDER_6_MHZ,
        CLOCK_MCHP_DIVIDER_5_33_MHZ,
        CLOCK_MCHP_DIVIDER_4_8_MHZ,
        CLOCK_MCHP_DIVIDER_4_36_MHZ,
        CLOCK_MCHP_DIVIDER_4_MHZ,
        CLOCK_MCHP_DIVIDER_3_69_MHZ,
        CLOCK_MCHP_DIVIDER_3_43_MHZ,
        CLOCK_MCHP_DIVIDER_3_2_MHZ,
        CLOCK_MCHP_DIVIDER_3_MHZ
};

struct clock_mchp_subsys_osc48m_config {
        bool on_demand_en;

        bool run_in_standby_en;

        enum clock_mchp_osc48m_divider_freq post_divider_freq;
};

enum clock_mchp_fdpll_src_clock {
        CLOCK_MCHP_FDPLL_SRC_GCLK0,
        CLOCK_MCHP_FDPLL_SRC_GCLK1,
        CLOCK_MCHP_FDPLL_SRC_GCLK2,
        CLOCK_MCHP_FDPLL_SRC_GCLK3,
        CLOCK_MCHP_FDPLL_SRC_GCLK4,
        CLOCK_MCHP_FDPLL_SRC_GCLK5,
        CLOCK_MCHP_FDPLL_SRC_GCLK6,
        CLOCK_MCHP_FDPLL_SRC_GCLK7,
        CLOCK_MCHP_FDPLL_SRC_GCLK8,
        CLOCK_MCHP_FDPLL_SRC_XOSC32K,
        CLOCK_MCHP_FDPLL_SRC_XOSC,

        CLOCK_MCHP_FDPLL_SRC_MAX = CLOCK_MCHP_FDPLL_SRC_XOSC
};

struct clock_mchp_subsys_fdpll_config {
        bool on_demand_en;

        bool run_in_standby_en;

        uint32_t divider_ratio_frac;

        uint32_t divider_ratio_int;

        uint32_t xosc_clock_divider;

        enum clock_mchp_fdpll_src_clock src;
};

enum clock_mchp_rtc_src_clock {
        CLOCK_MCHP_RTC_SRC_ULP1K = OSC32KCTRL_RTCCTRL_RTCSEL_ULP1K,
        CLOCK_MCHP_RTC_SRC_ULP32K = OSC32KCTRL_RTCCTRL_RTCSEL_ULP32K,
        CLOCK_MCHP_RTC_SRC_OSC1K = OSC32KCTRL_RTCCTRL_RTCSEL_OSC1K,
        CLOCK_MCHP_RTC_SRC_OSC32K = OSC32KCTRL_RTCCTRL_RTCSEL_OSC32K,
        CLOCK_MCHP_RTC_SRC_XOSC1K = OSC32KCTRL_RTCCTRL_RTCSEL_XOSC1K,
        CLOCK_MCHP_RTC_SRC_XOSC32K = OSC32KCTRL_RTCCTRL_RTCSEL_XOSC32K
};

struct clock_mchp_subsys_rtc_config {
        enum clock_mchp_rtc_src_clock src;
};

struct clock_mchp_subsys_xosc32k_config {
        bool on_demand_en;

        bool run_in_standby_en;
};

struct clock_mchp_subsys_osc32k_config {
        bool on_demand_en;

        bool run_in_standby_en;
};

enum clock_mchp_gclk_src_clock {
        CLOCK_MCHP_GCLK_SRC_XOSC,
        CLOCK_MCHP_GCLK_SRC_GCLKPIN,
        CLOCK_MCHP_GCLK_SRC_GCLKGEN1,
        CLOCK_MCHP_GCLK_SRC_OSCULP32K,
        CLOCK_MCHP_GCLK_SRC_OSC32K,
        CLOCK_MCHP_GCLK_SRC_XOSC32K,
        CLOCK_MCHP_GCLK_SRC_OSC48M,
        CLOCK_MCHP_GCLK_SRC_FDPLL,

        CLOCK_MCHP_GCLK_SRC_MAX = CLOCK_MCHP_GCLK_SRC_FDPLL
};

struct clock_mchp_subsys_gclkgen_config {
        uint16_t div_factor;

        bool run_in_standby_en;

        enum clock_mchp_gclk_src_clock src;
};

enum clock_mchp_gclkgen {
        CLOCK_MCHP_GCLKGEN_GEN0,
        CLOCK_MCHP_GCLKGEN_GEN1,
        CLOCK_MCHP_GCLKGEN_GEN2,
        CLOCK_MCHP_GCLKGEN_GEN3,
        CLOCK_MCHP_GCLKGEN_GEN4,
        CLOCK_MCHP_GCLKGEN_GEN5,
        CLOCK_MCHP_GCLKGEN_GEN6,
        CLOCK_MCHP_GCLKGEN_GEN7,
        CLOCK_MCHP_GCLKGEN_GEN8
};

struct clock_mchp_subsys_gclkperiph_config {
        enum clock_mchp_gclkgen src;
};

enum clock_mchp_mclk_cpu_div {
        CLOCK_MCHP_MCLK_CPU_DIV_1 = 1,
        CLOCK_MCHP_MCLK_CPU_DIV_2 = 2,
        CLOCK_MCHP_MCLK_CPU_DIV_4 = 4,
        CLOCK_MCHP_MCLK_CPU_DIV_8 = 8,
        CLOCK_MCHP_MCLK_CPU_DIV_16 = 16,
        CLOCK_MCHP_MCLK_CPU_DIV_32 = 32,
        CLOCK_MCHP_MCLK_CPU_DIV_64 = 64,
        CLOCK_MCHP_MCLK_CPU_DIV_128 = 128
};

struct clock_mchp_subsys_mclkcpu_config {
        enum clock_mchp_mclk_cpu_div division_factor;
};

typedef uint32_t *clock_mchp_rate_t;


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CM_JH_H_ */
```

## 492.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 222 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CM_JH_H_`。

## 492.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h.html)
- [zephyr/dt-bindings/clock/mchp_pic32cm_jh_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__jh__clock_8h.html)
- [clock_mchp_subsys_xosc_config](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md)
- [on_demand_en](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md#a51e27943063374fa67b03509d8d8b962)
- [run_in_standby_en](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md#a298c2524a043091ab6f591759d03c72b)
- [clock_mchp_osc48m_divider_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga4303aa06f4b9a93874f2d26406e788e3)
- [CLOCK_MCHP_DIVIDER_48_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3ae15895137cfed2a01dc07fd073c7f4f0)
- [CLOCK_MCHP_DIVIDER_24_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a5341cf2520f14d53305b552e29d336af)
- [CLOCK_MCHP_DIVIDER_16_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3af1947f866264e2b7eca4a0dbba0223cd)
- [CLOCK_MCHP_DIVIDER_12_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a97968c136ce06b10ff5b78fdeec82c6b)
- [CLOCK_MCHP_DIVIDER_9_6_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3afce32516f8303f06461a7edb1512cb4b)
- [CLOCK_MCHP_DIVIDER_8_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3ac2e281fba8772d11634fa74f1559e6ae)
- [CLOCK_MCHP_DIVIDER_6_86_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3aa6e359c000dc41599beaf5937d7b91b1)
- [CLOCK_MCHP_DIVIDER_6_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a1d3ab3603b8569a32492a33a7343b51b)
- [CLOCK_MCHP_DIVIDER_5_33_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a06c5e0bcabf7b54347f7e2c4cb54f2e1)
- [CLOCK_MCHP_DIVIDER_4_8_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a68d97439120b74cfb174d6d9f7254c57)
- [CLOCK_MCHP_DIVIDER_4_36_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3adb65fbb10b4703d719fe61dd044da5e9)
- [CLOCK_MCHP_DIVIDER_4_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3ac5a35357502c5bf9ca76f5a935efbcb1)
- [CLOCK_MCHP_DIVIDER_3_69_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a8dceb2229cb86ce500350fcb3f795a38)
- [CLOCK_MCHP_DIVIDER_3_43_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3ac808175c0850ab5634c87fc49a2cde89)
- [CLOCK_MCHP_DIVIDER_3_2_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3af8fcf13844de18b99b21de542e31f2d9)
- [CLOCK_MCHP_DIVIDER_3_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a4980f4845c33d559860cb4a2c8cbe8ab)
- [clock_mchp_subsys_osc48m_config](../clock_cmsis_model_reference/P017_clock_mchp_subsys_osc48m_config_结构体.md)
- [on_demand_en](../clock_cmsis_model_reference/P017_clock_mchp_subsys_osc48m_config_结构体.md#a191da6844eba2d9c20d4b21bedf825da)
- [run_in_standby_en](../clock_cmsis_model_reference/P017_clock_mchp_subsys_osc48m_config_结构体.md#ad5ee1cd0de32cff6c1e3726e56b33efc)
- [post_divider_freq](../clock_cmsis_model_reference/P017_clock_mchp_subsys_osc48m_config_结构体.md#aa2e9756157bdb1d71ff586c7baa5d856)
- [clock_mchp_fdpll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gaca271f1fae614cbd8c12fed31bcb64ea)
- [CLOCK_MCHP_FDPLL_SRC_GCLK0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa2b4dbfa6f3b2985c25df5457babcfc19)
- [CLOCK_MCHP_FDPLL_SRC_GCLK1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaad463d37743aa9dce5a24ea0b9f2f6f83)
- [CLOCK_MCHP_FDPLL_SRC_GCLK2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa9e1c784e19edd414b2c51196fb0ea630)
- [CLOCK_MCHP_FDPLL_SRC_GCLK3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa49e87978ba1e4471c0dc76705950f7d7)
- [CLOCK_MCHP_FDPLL_SRC_GCLK4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa5bb7c103fe4f9548da6f6ff38b8e4fe6)
- [CLOCK_MCHP_FDPLL_SRC_GCLK5](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa2e3099c6db41c26e126ea236ae1f4917)
- [CLOCK_MCHP_FDPLL_SRC_GCLK6](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaad1027fef245b5a24b80e383981d40913)
- [CLOCK_MCHP_FDPLL_SRC_GCLK7](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa1d753cfcae1b5d0249908d1567257cbc)
- [CLOCK_MCHP_FDPLL_SRC_GCLK8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaabdb11235f190deb557d9e19d4c24618c)
- [CLOCK_MCHP_FDPLL_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa8f6301943a69f328ac49e0b302c6e1e1)
- [CLOCK_MCHP_FDPLL_SRC_XOSC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa5049effd0b7a893f2e278b857010e24f)
- [CLOCK_MCHP_FDPLL_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaab1e1b66c6b826cbc9077fb579c73466b)
- [clock_mchp_subsys_fdpll_config](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md)
- [on_demand_en](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#a1ae355aede60d06e8ae395517ba5f7cd)
- [run_in_standby_en](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#aa3e53c57298528f9033e08cc238f6891)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [divider_ratio_frac](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#aa081dea6b720e1bf79c4eb1ba139c664)
- [divider_ratio_int](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#a763e54cbab07657be8eff1b8ca45f65e)
- [xosc_clock_divider](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#a24bc48331e32436c8f6c2cf3c76e7ed5)
- [clock_mchp_fdpll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaca271f1fae614cbd8c12fed31bcb64ea)
- [src](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#a8057b8d7233e11008eb81f798083ad6a)
- [clock_mchp_rtc_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a2b83aa5b88c064d44d3a0ef7661a15cf)
- [CLOCK_MCHP_RTC_SRC_ULP1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfafaa5cfa19e470035ad1cec308aa63f7b)
- [CLOCK_MCHP_RTC_SRC_ULP32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfa9095a4473e6e218ea0d2715695ecb2ff)
- [CLOCK_MCHP_RTC_SRC_OSC1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfad5e72f091a71486e117cdea5b8381dff)
- [CLOCK_MCHP_RTC_SRC_OSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfaa377b029b64d15627a7bee121ffc6050)
- [CLOCK_MCHP_RTC_SRC_XOSC1K](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a2b83aa5b88c064d44d3a0ef7661a15cfae738ec040a54d0b171192d122abdd332)
- [CLOCK_MCHP_RTC_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296)
- [clock_mchp_subsys_rtc_config](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md)
- [clock_mchp_rtc_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga2b83aa5b88c064d44d3a0ef7661a15cf)
- [src](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md#af6a74f1140ddab14f3e8f4642284f443)
- [clock_mchp_subsys_xosc32k_config](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md)
- [on_demand_en](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md#afb7ecdb2ad0168376649c5acb0c5c765)
- [run_in_standby_en](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md#a44925c2cea8adc89c1d5910156b4f105)
- [clock_mchp_subsys_osc32k_config](../clock_cmsis_model_reference/P016_clock_mchp_subsys_osc32k_config_结构体.md)
- [on_demand_en](../clock_cmsis_model_reference/P016_clock_mchp_subsys_osc32k_config_结构体.md#ace2f42ea255ec213ed207b18538a2a2d)
- [run_in_standby_en](../clock_cmsis_model_reference/P016_clock_mchp_subsys_osc32k_config_结构体.md#a8343157fa2c56424b9fc9768237e1922)
- [clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989)
- [CLOCK_MCHP_GCLK_SRC_XOSC](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a002e232f09f2da92b359ecd1543465d0)
- [CLOCK_MCHP_GCLK_SRC_GCLKPIN](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef)
- [CLOCK_MCHP_GCLK_SRC_GCLKGEN1](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9)
- [CLOCK_MCHP_GCLK_SRC_OSCULP32K](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6)
- [CLOCK_MCHP_GCLK_SRC_OSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a26b8d25a8d166e0b8e79c77312897145)
- [CLOCK_MCHP_GCLK_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380)
- [CLOCK_MCHP_GCLK_SRC_OSC48M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a198b4b6273b991b0795e574036b3e177)
- [CLOCK_MCHP_GCLK_SRC_FDPLL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a7ae946790cdbcec68bb8f7e8b35cd9fe)
- [CLOCK_MCHP_GCLK_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768)
- [clock_mchp_subsys_gclkgen_config](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [div_factor](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#af803dcb746c1438f6e08ac30042d3651)
- [run_in_standby_en](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#a59f3f908c254d4299164b5fea5885514)
- [clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga073dab68c78edce3985eb201a039a989)
- [src](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#aeb553aa051490aefb8d38cc9ce7e8166)
- [clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777)
- [CLOCK_MCHP_GCLKGEN_GEN0](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f)
- [CLOCK_MCHP_GCLKGEN_GEN1](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424)
- [CLOCK_MCHP_GCLKGEN_GEN2](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe)
- [CLOCK_MCHP_GCLKGEN_GEN3](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08)
- [CLOCK_MCHP_GCLKGEN_GEN4](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a69bd2c6d8f016e8ecdfd07fba7268dcc)
- [CLOCK_MCHP_GCLKGEN_GEN5](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a20bf106031eb19f25b8e3b1250033088)
- [CLOCK_MCHP_GCLKGEN_GEN6](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a9cbc78f597c2930b36280c59164e12ae)
- [CLOCK_MCHP_GCLKGEN_GEN7](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a71ead69f87ccd57496b0467a6264d411)
- [CLOCK_MCHP_GCLKGEN_GEN8](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777aff9b0bedc5de2cfe3259df2910ab55f9)
- [clock_mchp_subsys_gclkperiph_config](../clock_cmsis_model_reference/P014_clock_mchp_subsys_gclkperiph_config_结构体.md)
- [clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaab34442b0d6c171691ae299675542777)
- [src](../clock_cmsis_model_reference/P014_clock_mchp_subsys_gclkperiph_config_结构体.md#a1727b4df3eb0dcff7365909002cef636)
- [clock_mchp_mclk_cpu_div](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a5835567db8d16c4eeb7a03b843ac6254)
- [CLOCK_MCHP_MCLK_CPU_DIV_1](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a5835567db8d16c4eeb7a03b843ac6254a9f893cbec63df56227f17098ddf70074)
- [CLOCK_MCHP_MCLK_CPU_DIV_2](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a5835567db8d16c4eeb7a03b843ac6254ac52aba85d20e21bd3135cc46e467dbfc)
- [CLOCK_MCHP_MCLK_CPU_DIV_4](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a5835567db8d16c4eeb7a03b843ac6254ad251e58f232eaa9d45cce47e600b506f)
- [CLOCK_MCHP_MCLK_CPU_DIV_8](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a5835567db8d16c4eeb7a03b843ac6254ace4fa9213f609c27198c75f17b0f7beb)
- [CLOCK_MCHP_MCLK_CPU_DIV_16](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a5835567db8d16c4eeb7a03b843ac6254ae11a4d93aaafcfaeed5a7cc6e0a1de89)
- [CLOCK_MCHP_MCLK_CPU_DIV_32](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a5835567db8d16c4eeb7a03b843ac6254ab071663992b6be65b6f77442239d3157)
- [CLOCK_MCHP_MCLK_CPU_DIV_64](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a5835567db8d16c4eeb7a03b843ac6254a688a2dbe64b6a818ab84f26cc983b3f0)
- [CLOCK_MCHP_MCLK_CPU_DIV_128](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a5835567db8d16c4eeb7a03b843ac6254aefa35c60f9274b62c0b829c1c24a571b)
- [clock_mchp_subsys_mclkcpu_config](../clock_cmsis_model_reference/P015_clock_mchp_subsys_mclkcpu_config_结构体.md)
- [clock_mchp_mclk_cpu_div](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga5835567db8d16c4eeb7a03b843ac6254)
- [division_factor](../clock_cmsis_model_reference/P015_clock_mchp_subsys_mclkcpu_config_结构体.md#a380cc94c6ed19143a29f2590af21f672)
- [clock_mchp_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a9b6955116dae7fa53c8dad373a1ef9c9)
- [mchp_pic32cm_jh_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__jh__clock_8h.html)
- [clock_mchp_subsys_fdpll_config::on_demand_en](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#a1ae355aede60d06e8ae395517ba5f7cd)
- [clock_mchp_subsys_fdpll_config::xosc_clock_divider](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#a24bc48331e32436c8f6c2cf3c76e7ed5)
- [clock_mchp_subsys_fdpll_config::divider_ratio_int](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#a763e54cbab07657be8eff1b8ca45f65e)
- [clock_mchp_subsys_fdpll_config::src](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#a8057b8d7233e11008eb81f798083ad6a)
- [clock_mchp_subsys_fdpll_config::divider_ratio_frac](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#aa081dea6b720e1bf79c4eb1ba139c664)
- [clock_mchp_subsys_fdpll_config::run_in_standby_en](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md#aa3e53c57298528f9033e08cc238f6891)
- [clock_mchp_subsys_gclkgen_config::run_in_standby_en](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#a59f3f908c254d4299164b5fea5885514)
- [clock_mchp_subsys_gclkgen_config::src](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#aeb553aa051490aefb8d38cc9ce7e8166)
- [clock_mchp_subsys_gclkgen_config::div_factor](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#af803dcb746c1438f6e08ac30042d3651)
- [clock_mchp_subsys_gclkperiph_config::src](../clock_cmsis_model_reference/P014_clock_mchp_subsys_gclkperiph_config_结构体.md#a1727b4df3eb0dcff7365909002cef636)
- [clock_mchp_subsys_mclkcpu_config::division_factor](../clock_cmsis_model_reference/P015_clock_mchp_subsys_mclkcpu_config_结构体.md#a380cc94c6ed19143a29f2590af21f672)
- [clock_mchp_subsys_osc32k_config::run_in_standby_en](../clock_cmsis_model_reference/P016_clock_mchp_subsys_osc32k_config_结构体.md#a8343157fa2c56424b9fc9768237e1922)
- [clock_mchp_subsys_osc32k_config::on_demand_en](../clock_cmsis_model_reference/P016_clock_mchp_subsys_osc32k_config_结构体.md#ace2f42ea255ec213ed207b18538a2a2d)
- [clock_mchp_subsys_osc48m_config::on_demand_en](../clock_cmsis_model_reference/P017_clock_mchp_subsys_osc48m_config_结构体.md#a191da6844eba2d9c20d4b21bedf825da)
- [clock_mchp_subsys_osc48m_config::post_divider_freq](../clock_cmsis_model_reference/P017_clock_mchp_subsys_osc48m_config_结构体.md#aa2e9756157bdb1d71ff586c7baa5d856)
- [clock_mchp_subsys_osc48m_config::run_in_standby_en](../clock_cmsis_model_reference/P017_clock_mchp_subsys_osc48m_config_结构体.md#ad5ee1cd0de32cff6c1e3726e56b33efc)
- [clock_mchp_subsys_rtc_config::src](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md#af6a74f1140ddab14f3e8f4642284f443)
- [clock_mchp_subsys_xosc32k_config::run_in_standby_en](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md#a44925c2cea8adc89c1d5910156b4f105)
- [clock_mchp_subsys_xosc32k_config::on_demand_en](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md#afb7ecdb2ad0168376649c5acb0c5c765)
- [clock_mchp_subsys_xosc_config::run_in_standby_en](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md#a298c2524a043091ab6f591759d03c72b)
- [clock_mchp_subsys_xosc_config::on_demand_en](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md#a51e27943063374fa67b03509d8d8b962)

---

[上一章](P491_mchp_clock_pic32ck_sg_gc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P493_mchp_clock_pic32cm_pl.h_源码浏览.md)
