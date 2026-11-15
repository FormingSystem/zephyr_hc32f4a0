---
id: learning.zephyr-docs.api-source-reference.page-495
title: mchp_clock_pic32cz_ca.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第495章\_mchp\_clock\_pic32cz\_ca.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h.html)。

## 495.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
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
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00071"></a>
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
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
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
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="foldopen00185"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga2b83aa5b88c064d44d3a0ef7661a15cfa9095a4473e6e218ea0d2715695ecb2ff"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga2b83aa5b88c064d44d3a0ef7661a15cfafaa5cfa19e470035ad1cec308aa63f7b"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_gaab34442b0d6c171691ae299675542777"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_gad4a3719300474b36067b86dad7611d33"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_gga073dab68c78edce3985eb201a039a989a4868e29d2e440862dd6a8484134871ca"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_gga073dab68c78edce3985eb201a039a989a4f5fc805a8d554b93427e31990e8d3cc"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_gga073dab68c78edce3985eb201a039a989aa5ea75b3e521ddad5e1a4b64b385ff48"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_gga073dab68c78edce3985eb201a039a989aff74c95610d9ea91fac78e3f90866dfb"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_ggaab34442b0d6c171691ae299675542777a24e34e40f92b7cd41fa7d927097d6f25"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_ggaab34442b0d6c171691ae299675542777a6ea9310c7eb41d72c82b4abff78b36f8"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_ggaab34442b0d6c171691ae299675542777aaca57694ee279c5aa0b732bb9c7dcd19"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_ggaab34442b0d6c171691ae299675542777ae33d3555ccda79c69de0fc110937cf23"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_ggad4a3719300474b36067b86dad7611d33a49e9404af4ac43cae2f763398bd684f5"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_ggad4a3719300474b36067b86dad7611d33a60af6e9669ecc5ae48c564d63550bf61"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_ggad4a3719300474b36067b86dad7611d33a621956779e5d9517b1dfaef019e2085f"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_ggad4a3719300474b36067b86dad7611d33ad03e683a424631e0db34c23b3d5611a0"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_ga073dab68c78edce3985eb201a039a989"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_ga2b83aa5b88c064d44d3a0ef7661a15cf"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_ga5835567db8d16c4eeb7a03b843ac6254"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_gaab34442b0d6c171691ae299675542777"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a002e232f09f2da92b359ecd1543465d0"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a647395dd08022519b13e0270f44943d6"></a>
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
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a63f142bb2401a057b9ba7b4a8f60eb60"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a69bd2c6d8f016e8ecdfd07fba7268dcc"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a71ead69f87ccd57496b0467a6264d411"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a905cb4bab8f6bb50f690de6a9e970695"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a96de017372252af6f1bcab2cdb32c2f1"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a9cbc78f597c2930b36280c59164e12ae"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777aff9b0bedc5de2cfe3259df2910ab55f9"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a1ec27a2b726685c4affe367881bd55e0"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a8db1c0dbb5d2fa6fc89208f26d8e18fb"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a97424a08d5ca63e8b0bb59699f199fbf"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989aab491fb5a01623e4248e04f4b6af9e76"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33a1035e2c8184feb507cd47a7046567f6b"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33a183ebd7a615416cee57d7bdb0ce4d29b"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33a34340db86e94450b72eae0d7ca0be283"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33a394cfe9ab4e963417fc0787c160ec847"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33a4917fc8ee80c35ab78df854e2ce81958"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33a5f67b9bf8fd7edbe90c4c22073ddc759"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33a666358ed4b1f3564a7b4ae8a0b54cb06"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33a75742e71b54b1bdefd0716085d47e496"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33a99f7e9bb4cf4b36b79070f514c88ad1d"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33aaf6ebe0c6f7370866388499a7a4037c2"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33abf6ced8f2a3eabadea96bdbf0b172b61"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33ae3f23ab2c7a84a5c43fb8361b1ee1f83"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33af1d913a5d9ad87b788becc822818080b"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33af5906d13a56a0e26da669e15b5454b63"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html_ad4a3719300474b36067b86dad7611d33afedc39675c6b63f46e36ed415ea04b27"></a>
<a id="amchp__pic32cz__ca__clock_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructclock__mchp__subsys__dfll48m__config_html"></a>
<a id="astructclock__mchp__subsys__dfll48m__config_html_a0056a9d73d353a31c5c6303e4f96fa1d"></a>
<a id="astructclock__mchp__subsys__dfll48m__config_html_a5f06274d52ac9a342f62361bb6451cc3"></a>
<a id="astructclock__mchp__subsys__dfll48m__config_html_a8b5dca59c164a9c785fc763ed97dbcbd"></a>
<a id="astructclock__mchp__subsys__dfll48m__config_html_af9b0a365f56ef718b2bb74e460f74df9"></a>
<a id="astructclock__mchp__subsys__dpll__config_html"></a>
<a id="astructclock__mchp__subsys__dpll__config_html_a40cc0b64d8a2feaa59a231f7d8d05bb2"></a>
<a id="astructclock__mchp__subsys__dpll__config_html_a4b54b6abcdc5ddb4c6321affcb0110dc"></a>
<a id="astructclock__mchp__subsys__dpll__config_html_a945f0d0e331b4512cfcea6f298b03fd2"></a>
<a id="astructclock__mchp__subsys__dpll__config_html_ae1009bd26ecd41f2f751e14366eb5701"></a>
<a id="astructclock__mchp__subsys__dpll__out__config_html"></a>
<a id="astructclock__mchp__subsys__dpll__out__config_html_a181501af2102f2fd1e3bf3a0e02af531"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html_a59f3f908c254d4299164b5fea5885514"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html_aeb553aa051490aefb8d38cc9ce7e8166"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html_af803dcb746c1438f6e08ac30042d3651"></a>
<a id="astructclock__mchp__subsys__gclkperiph__config_html"></a>
<a id="astructclock__mchp__subsys__gclkperiph__config_html_a1727b4df3eb0dcff7365909002cef636"></a>
<a id="astructclock__mchp__subsys__mclkcpu__config_html"></a>
<a id="astructclock__mchp__subsys__mclkcpu__config_html_a380cc94c6ed19143a29f2590af21f672"></a>
<a id="astructclock__mchp__subsys__rtc__config_html"></a>
<a id="astructclock__mchp__subsys__rtc__config_html_af6a74f1140ddab14f3e8f4642284f443"></a>
<a id="astructclock__mchp__subsys__xosc32k__config_html"></a>
<a id="astructclock__mchp__subsys__xosc32k__config_html_afb7ecdb2ad0168376649c5acb0c5c765"></a>
<a id="astructclock__mchp__subsys__xosc__config_html"></a>
<a id="astructclock__mchp__subsys__xosc__config_html_a51e27943063374fa67b03509d8d8b962"></a>

```c
/*
 * Copyright (c) 2025-2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CZ_CA_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CZ_CA_H_

#include <zephyr/dt-bindings/clock/mchp_pic32cz_ca_clock.h>


struct clock_mchp_subsys_xosc_config {
        bool on_demand_en;
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
        CLOCK_MCHP_GCLKGEN_GEN8,
        CLOCK_MCHP_GCLKGEN_GEN9,
        CLOCK_MCHP_GCLKGEN_GEN10,
        CLOCK_MCHP_GCLKGEN_GEN11,
        CLOCK_MCHP_GCLKGEN_GEN12,
        CLOCK_MCHP_GCLKGEN_GEN13,
        CLOCK_MCHP_GCLKGEN_GEN14,
        CLOCK_MCHP_GCLKGEN_GEN15
};

struct clock_mchp_subsys_dfll48m_config {
        bool on_demand_en;

        bool closed_loop_en;

        enum clock_mchp_gclkgen src;

        uint16_t multiply_factor;
};

enum clock_mchp_dpll_src_clock {
        CLOCK_MCHP_DPLL_SRC_GCLK0,
        CLOCK_MCHP_DPLL_SRC_GCLK1,
        CLOCK_MCHP_DPLL_SRC_GCLK2,
        CLOCK_MCHP_DPLL_SRC_GCLK3,
        CLOCK_MCHP_DPLL_SRC_GCLK4,
        CLOCK_MCHP_DPLL_SRC_GCLK5,
        CLOCK_MCHP_DPLL_SRC_GCLK6,
        CLOCK_MCHP_DPLL_SRC_GCLK7,
        CLOCK_MCHP_DPLL_SRC_GCLK8,
        CLOCK_MCHP_DPLL_SRC_GCLK9,
        CLOCK_MCHP_DPLL_SRC_GCLK10,
        CLOCK_MCHP_DPLL_SRC_GCLK11,
        CLOCK_MCHP_DPLL_SRC_GCLK12,
        CLOCK_MCHP_DPLL_SRC_GCLK13,
        CLOCK_MCHP_DPLL_SRC_GCLK14,
        CLOCK_MCHP_DPLL_SRC_GCLK15,
        CLOCK_MCHP_DPLL_SRC_XOSC,
        CLOCK_MCHP_DPLL_SRC_DFLL48M,

        CLOCK_MCHP_DPLL_SRC_MAX =
                CLOCK_MCHP_DPLL_SRC_DFLL48M
};

struct clock_mchp_subsys_dpll_config {
        uint16_t feedback_divider_factor;

        uint8_t ref_division_factor;

        bool on_demand_en;

        enum clock_mchp_dpll_src_clock src;
};

struct clock_mchp_subsys_dpll_out_config {
        uint8_t output_division_factor;
};

enum clock_mchp_rtc_src_clock {
        CLOCK_MCHP_RTC_SRC_ULP1K = OSC32KCTRL_CLKSELCTRL_RTCSEL_ULP1K_Val,

        CLOCK_MCHP_RTC_SRC_ULP32K = OSC32KCTRL_CLKSELCTRL_RTCSEL_ULP32K_Val,

        CLOCK_MCHP_RTC_SRC_XOSC1K = OSC32KCTRL_CLKSELCTRL_RTCSEL_XOSC1K_Val,

        CLOCK_MCHP_RTC_SRC_XOSC32K = OSC32KCTRL_CLKSELCTRL_RTCSEL_XOSC32K_Val
};

struct clock_mchp_subsys_rtc_config {
        enum clock_mchp_rtc_src_clock src;
};

struct clock_mchp_subsys_xosc32k_config {
        bool on_demand_en;
};

enum clock_mchp_gclk_src_clock {
        CLOCK_MCHP_GCLK_SRC_XOSC,
        CLOCK_MCHP_GCLK_SRC_GCLKPIN,
        CLOCK_MCHP_GCLK_SRC_GCLKGEN1,
        CLOCK_MCHP_GCLK_SRC_OSCULP32K,
        CLOCK_MCHP_GCLK_SRC_XOSC32K,
        CLOCK_MCHP_GCLK_SRC_DFLL48M,
        CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT0,
        CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT1,
        CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT2,
        CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT3,
        CLOCK_MCHP_GCLK_SRC_DPLL1_FRC_CLKOUT0,
        CLOCK_MCHP_GCLK_SRC_DPLL1_FRC_CLKOUT1,
        CLOCK_MCHP_GCLK_SRC_DPLL1_CLKOUT2,
        CLOCK_MCHP_GCLK_SRC_DPLL1_CLKOUT3,

        CLOCK_MCHP_GCLK_SRC_MAX =
                CLOCK_MCHP_GCLK_SRC_DPLL1_CLKOUT3
};

struct clock_mchp_subsys_gclkgen_config {
        uint16_t div_factor;

        bool run_in_standby_en;

        enum clock_mchp_gclk_src_clock src;
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


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CZ_CA_H_ */
```

## 495.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025-2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 213 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CZ_CA_H_`。

## 495.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h.html)
- [zephyr/dt-bindings/clock/mchp_pic32cz_ca_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cz__ca__clock_8h.html)
- [clock_mchp_subsys_xosc_config](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md)
- [on_demand_en](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md#a51e27943063374fa67b03509d8d8b962)
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
- [CLOCK_MCHP_GCLKGEN_GEN9](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a96de017372252af6f1bcab2cdb32c2f1)
- [CLOCK_MCHP_GCLKGEN_GEN10](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a63f142bb2401a057b9ba7b4a8f60eb60)
- [CLOCK_MCHP_GCLKGEN_GEN11](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a905cb4bab8f6bb50f690de6a9e970695)
- [CLOCK_MCHP_GCLKGEN_GEN12](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#ggaab34442b0d6c171691ae299675542777a6ea9310c7eb41d72c82b4abff78b36f8)
- [CLOCK_MCHP_GCLKGEN_GEN13](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#ggaab34442b0d6c171691ae299675542777aaca57694ee279c5aa0b732bb9c7dcd19)
- [CLOCK_MCHP_GCLKGEN_GEN14](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#ggaab34442b0d6c171691ae299675542777ae33d3555ccda79c69de0fc110937cf23)
- [CLOCK_MCHP_GCLKGEN_GEN15](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#ggaab34442b0d6c171691ae299675542777a24e34e40f92b7cd41fa7d927097d6f25)
- [clock_mchp_subsys_dfll48m_config](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md)
- [on_demand_en](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a8b5dca59c164a9c785fc763ed97dbcbd)
- [closed_loop_en](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a5f06274d52ac9a342f62361bb6451cc3)
- [clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#gaab34442b0d6c171691ae299675542777)
- [src](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#af9b0a365f56ef718b2bb74e460f74df9)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [multiply_factor](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a0056a9d73d353a31c5c6303e4f96fa1d)
- [clock_mchp_dpll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33)
- [CLOCK_MCHP_DPLL_SRC_GCLK0](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33ae3f23ab2c7a84a5c43fb8361b1ee1f83)
- [CLOCK_MCHP_DPLL_SRC_GCLK1](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33a75742e71b54b1bdefd0716085d47e496)
- [CLOCK_MCHP_DPLL_SRC_GCLK2](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33af5906d13a56a0e26da669e15b5454b63)
- [CLOCK_MCHP_DPLL_SRC_GCLK3](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33a394cfe9ab4e963417fc0787c160ec847)
- [CLOCK_MCHP_DPLL_SRC_GCLK4](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33afedc39675c6b63f46e36ed415ea04b27)
- [CLOCK_MCHP_DPLL_SRC_GCLK5](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33a34340db86e94450b72eae0d7ca0be283)
- [CLOCK_MCHP_DPLL_SRC_GCLK6](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33a183ebd7a615416cee57d7bdb0ce4d29b)
- [CLOCK_MCHP_DPLL_SRC_GCLK7](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33a4917fc8ee80c35ab78df854e2ce81958)
- [CLOCK_MCHP_DPLL_SRC_GCLK8](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33a5f67b9bf8fd7edbe90c4c22073ddc759)
- [CLOCK_MCHP_DPLL_SRC_GCLK9](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33aaf6ebe0c6f7370866388499a7a4037c2)
- [CLOCK_MCHP_DPLL_SRC_GCLK10](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33a666358ed4b1f3564a7b4ae8a0b54cb06)
- [CLOCK_MCHP_DPLL_SRC_GCLK11](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33abf6ced8f2a3eabadea96bdbf0b172b61)
- [CLOCK_MCHP_DPLL_SRC_GCLK12](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#ggad4a3719300474b36067b86dad7611d33a621956779e5d9517b1dfaef019e2085f)
- [CLOCK_MCHP_DPLL_SRC_GCLK13](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#ggad4a3719300474b36067b86dad7611d33a49e9404af4ac43cae2f763398bd684f5)
- [CLOCK_MCHP_DPLL_SRC_GCLK14](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#ggad4a3719300474b36067b86dad7611d33ad03e683a424631e0db34c23b3d5611a0)
- [CLOCK_MCHP_DPLL_SRC_GCLK15](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#ggad4a3719300474b36067b86dad7611d33a60af6e9669ecc5ae48c564d63550bf61)
- [CLOCK_MCHP_DPLL_SRC_XOSC](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33a99f7e9bb4cf4b36b79070f514c88ad1d)
- [CLOCK_MCHP_DPLL_SRC_DFLL48M](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33af1d913a5d9ad87b788becc822818080b)
- [CLOCK_MCHP_DPLL_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#ad4a3719300474b36067b86dad7611d33a1035e2c8184feb507cd47a7046567f6b)
- [clock_mchp_subsys_dpll_config](../clock_cmsis_model_reference/P010_clock_mchp_subsys_dpll_config_结构体.md)
- [feedback_divider_factor](../clock_cmsis_model_reference/P010_clock_mchp_subsys_dpll_config_结构体.md#a945f0d0e331b4512cfcea6f298b03fd2)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ref_division_factor](../clock_cmsis_model_reference/P010_clock_mchp_subsys_dpll_config_结构体.md#a4b54b6abcdc5ddb4c6321affcb0110dc)
- [on_demand_en](../clock_cmsis_model_reference/P010_clock_mchp_subsys_dpll_config_结构体.md#ae1009bd26ecd41f2f751e14366eb5701)
- [clock_mchp_dpll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#gad4a3719300474b36067b86dad7611d33)
- [src](../clock_cmsis_model_reference/P010_clock_mchp_subsys_dpll_config_结构体.md#a40cc0b64d8a2feaa59a231f7d8d05bb2)
- [clock_mchp_subsys_dpll_out_config](../clock_cmsis_model_reference/P011_clock_mchp_subsys_dpll_out_config_结构体.md)
- [output_division_factor](../clock_cmsis_model_reference/P011_clock_mchp_subsys_dpll_out_config_结构体.md#a181501af2102f2fd1e3bf3a0e02af531)
- [clock_mchp_rtc_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a2b83aa5b88c064d44d3a0ef7661a15cf)
- [CLOCK_MCHP_RTC_SRC_ULP1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfafaa5cfa19e470035ad1cec308aa63f7b)
- [CLOCK_MCHP_RTC_SRC_ULP32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfa9095a4473e6e218ea0d2715695ecb2ff)
- [CLOCK_MCHP_RTC_SRC_XOSC1K](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a2b83aa5b88c064d44d3a0ef7661a15cfae738ec040a54d0b171192d122abdd332)
- [CLOCK_MCHP_RTC_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296)
- [clock_mchp_subsys_rtc_config](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md)
- [clock_mchp_rtc_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga2b83aa5b88c064d44d3a0ef7661a15cf)
- [src](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md#af6a74f1140ddab14f3e8f4642284f443)
- [clock_mchp_subsys_xosc32k_config](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md)
- [on_demand_en](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md#afb7ecdb2ad0168376649c5acb0c5c765)
- [clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989)
- [CLOCK_MCHP_GCLK_SRC_XOSC](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a002e232f09f2da92b359ecd1543465d0)
- [CLOCK_MCHP_GCLK_SRC_GCLKPIN](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef)
- [CLOCK_MCHP_GCLK_SRC_GCLKGEN1](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9)
- [CLOCK_MCHP_GCLK_SRC_OSCULP32K](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6)
- [CLOCK_MCHP_GCLK_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380)
- [CLOCK_MCHP_GCLK_SRC_DFLL48M](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a647395dd08022519b13e0270f44943d6)
- [CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT0](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a97424a08d5ca63e8b0bb59699f199fbf)
- [CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT1](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a8db1c0dbb5d2fa6fc89208f26d8e18fb)
- [CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT2](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989aab491fb5a01623e4248e04f4b6af9e76)
- [CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT3](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a1ec27a2b726685c4affe367881bd55e0)
- [CLOCK_MCHP_GCLK_SRC_DPLL1_FRC_CLKOUT0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#gga073dab68c78edce3985eb201a039a989a4f5fc805a8d554b93427e31990e8d3cc)
- [CLOCK_MCHP_GCLK_SRC_DPLL1_FRC_CLKOUT1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#gga073dab68c78edce3985eb201a039a989aa5ea75b3e521ddad5e1a4b64b385ff48)
- [CLOCK_MCHP_GCLK_SRC_DPLL1_CLKOUT2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#gga073dab68c78edce3985eb201a039a989aff74c95610d9ea91fac78e3f90866dfb)
- [CLOCK_MCHP_GCLK_SRC_DPLL1_CLKOUT3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#gga073dab68c78edce3985eb201a039a989a4868e29d2e440862dd6a8484134871ca)
- [CLOCK_MCHP_GCLK_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768)
- [clock_mchp_subsys_gclkgen_config](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md)
- [div_factor](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#af803dcb746c1438f6e08ac30042d3651)
- [run_in_standby_en](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#a59f3f908c254d4299164b5fea5885514)
- [clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga073dab68c78edce3985eb201a039a989)
- [src](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#aeb553aa051490aefb8d38cc9ce7e8166)
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
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clock_mchp_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a9b6955116dae7fa53c8dad373a1ef9c9)
- [mchp_pic32cz_ca_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cz__ca__clock_8h.html)
- [clock_mchp_subsys_dfll48m_config::multiply_factor](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a0056a9d73d353a31c5c6303e4f96fa1d)
- [clock_mchp_subsys_dfll48m_config::closed_loop_en](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a5f06274d52ac9a342f62361bb6451cc3)
- [clock_mchp_subsys_dfll48m_config::on_demand_en](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a8b5dca59c164a9c785fc763ed97dbcbd)
- [clock_mchp_subsys_dfll48m_config::src](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#af9b0a365f56ef718b2bb74e460f74df9)
- [clock_mchp_subsys_dpll_config::src](../clock_cmsis_model_reference/P010_clock_mchp_subsys_dpll_config_结构体.md#a40cc0b64d8a2feaa59a231f7d8d05bb2)
- [clock_mchp_subsys_dpll_config::ref_division_factor](../clock_cmsis_model_reference/P010_clock_mchp_subsys_dpll_config_结构体.md#a4b54b6abcdc5ddb4c6321affcb0110dc)
- [clock_mchp_subsys_dpll_config::feedback_divider_factor](../clock_cmsis_model_reference/P010_clock_mchp_subsys_dpll_config_结构体.md#a945f0d0e331b4512cfcea6f298b03fd2)
- [clock_mchp_subsys_dpll_config::on_demand_en](../clock_cmsis_model_reference/P010_clock_mchp_subsys_dpll_config_结构体.md#ae1009bd26ecd41f2f751e14366eb5701)
- [clock_mchp_subsys_dpll_out_config::output_division_factor](../clock_cmsis_model_reference/P011_clock_mchp_subsys_dpll_out_config_结构体.md#a181501af2102f2fd1e3bf3a0e02af531)
- [clock_mchp_subsys_gclkgen_config::run_in_standby_en](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#a59f3f908c254d4299164b5fea5885514)
- [clock_mchp_subsys_gclkgen_config::src](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#aeb553aa051490aefb8d38cc9ce7e8166)
- [clock_mchp_subsys_gclkgen_config::div_factor](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#af803dcb746c1438f6e08ac30042d3651)
- [clock_mchp_subsys_gclkperiph_config::src](../clock_cmsis_model_reference/P014_clock_mchp_subsys_gclkperiph_config_结构体.md#a1727b4df3eb0dcff7365909002cef636)
- [clock_mchp_subsys_mclkcpu_config::division_factor](../clock_cmsis_model_reference/P015_clock_mchp_subsys_mclkcpu_config_结构体.md#a380cc94c6ed19143a29f2590af21f672)
- [clock_mchp_subsys_rtc_config::src](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md#af6a74f1140ddab14f3e8f4642284f443)
- [clock_mchp_subsys_xosc32k_config::on_demand_en](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md#afb7ecdb2ad0168376649c5acb0c5c765)
- [clock_mchp_subsys_xosc_config::on_demand_en](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md#a51e27943063374fa67b03509d8d8b962)

---

[上一章](P494_mchp_clock_pic32cm_sg_gc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P496_mchp_clock_sam_d5x_e5x.h_源码浏览.md)
