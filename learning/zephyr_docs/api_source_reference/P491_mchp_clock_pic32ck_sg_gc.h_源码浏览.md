---
id: learning.zephyr-docs.api-source-reference.page-491
title: mchp_clock_pic32ck_sg_gc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第491章\_mchp\_clock\_pic32ck\_sg\_gc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html)。

## 491.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="foldopen00021"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00027"></a>
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
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
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
<a id="l00078"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00121"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="foldopen00127"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="foldopen00159"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="foldopen00165"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="foldopen00180"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="agroup__clock__control__mchp__pic32cz__ca_html_gaab34442b0d6c171691ae299675542777"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_ga073dab68c78edce3985eb201a039a989"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_ga2b83aa5b88c064d44d3a0ef7661a15cf"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_ga5835567db8d16c4eeb7a03b843ac6254"></a>
<a id="agroup__clock__control__mchp__sam__d5x__e5x_html_gaab34442b0d6c171691ae299675542777"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a002e232f09f2da92b359ecd1543465d0"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a0242a7512bbb16e7d97113c66c26ea73"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a647395dd08022519b13e0270f44943d6"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a9493982be1abdb53d65963d19fc17ab8"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a956353351be40288ebbc3c7c5d3480c9"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989aa906d7b53c240c7b358a33069e26bad0"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989ad3453cbd92dca5da39da54a267e955b5"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989aeb2a16ab5ddfe55eab48831761c83aca"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555e"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555ea097b57f49a9ed54a8e68a88c45af8540"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555ea24133131a7e379620f4cccc8c272d3d2"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555ea47742caeb6c36cfbab2ea52b76375843"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555ea7f589a8c783ca935e3a3bec4e00fe78a"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555ea855942173475ae101281766a4fda2e5f"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555ea8738be13a05d1f2e738b32c41446d7b9"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555ea8b04fdb20116b7fe6e1c0f76c628db77"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555eab27d86592af60943287f2eed0079a538"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555eac158d3d2881be2f4599a3fa17e10c7e4"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555eacbcf8ac169420753c80c1b12ad10e517"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555ead09414b3eb59c8c3192b06be62ceb0e5"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555eae253d07c8f5363965d92dbd067d634be"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555eae6ea73001396449cab6b5ae14adce995"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555eaef24a9e72fe2d4f1518d04b081bfb344"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a1f0a363c4b5d2260d614bc0b2e19555eaf7bd65f6bc9f42452f59f60623d50881"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a2b83aa5b88c064d44d3a0ef7661a15cf"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a2b83aa5b88c064d44d3a0ef7661a15cfa3523c19ffb12654b4d1e663d6ef096ec"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a2b83aa5b88c064d44d3a0ef7661a15cfa4eeb4b4c5f682aa3c2c09fb7a321a68d"></a>
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
<a id="amchp__pic32ck__sg__gc__clock_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructclock__mchp__subsys__dfll48m__config_html"></a>
<a id="astructclock__mchp__subsys__dfll48m__config_html_a0056a9d73d353a31c5c6303e4f96fa1d"></a>
<a id="astructclock__mchp__subsys__dfll48m__config_html_a5f06274d52ac9a342f62361bb6451cc3"></a>
<a id="astructclock__mchp__subsys__dfll48m__config_html_a8b5dca59c164a9c785fc763ed97dbcbd"></a>
<a id="astructclock__mchp__subsys__dfll48m__config_html_af9b0a365f56ef718b2bb74e460f74df9"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html_a59f3f908c254d4299164b5fea5885514"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html_aeb553aa051490aefb8d38cc9ce7e8166"></a>
<a id="astructclock__mchp__subsys__gclkgen__config_html_af803dcb746c1438f6e08ac30042d3651"></a>
<a id="astructclock__mchp__subsys__gclkperiph__config_html"></a>
<a id="astructclock__mchp__subsys__gclkperiph__config_html_a1727b4df3eb0dcff7365909002cef636"></a>
<a id="astructclock__mchp__subsys__mclkcpu__config_html"></a>
<a id="astructclock__mchp__subsys__mclkcpu__config_html_a380cc94c6ed19143a29f2590af21f672"></a>
<a id="astructclock__mchp__subsys__pll__config_html"></a>
<a id="astructclock__mchp__subsys__pll__config_html_a1d40f6f5bc7610d5db8d7fc7c16ccd54"></a>
<a id="astructclock__mchp__subsys__pll__config_html_a67f3c481143ff8f860ae7f2fabf16867"></a>
<a id="astructclock__mchp__subsys__pll__config_html_ae4de7160ef688c54e4d7741b695353eb"></a>
<a id="astructclock__mchp__subsys__pll__config_html_af96f2f4bdf60d50f3942c3cc55703ad6"></a>
<a id="astructclock__mchp__subsys__pll__out__config_html"></a>
<a id="astructclock__mchp__subsys__pll__out__config_html_a3483433887d306cc9f2acff66654cd32"></a>
<a id="astructclock__mchp__subsys__rtc__config_html"></a>
<a id="astructclock__mchp__subsys__rtc__config_html_af6a74f1140ddab14f3e8f4642284f443"></a>
<a id="astructclock__mchp__subsys__xosc32k__config_html"></a>
<a id="astructclock__mchp__subsys__xosc32k__config_html_afb7ecdb2ad0168376649c5acb0c5c765"></a>
<a id="astructclock__mchp__subsys__xosc__config_html"></a>
<a id="astructclock__mchp__subsys__xosc__config_html_a51e27943063374fa67b03509d8d8b962"></a>

```c
/*
 * Copyright (c) 2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef INCLUDE_ZEPHYR_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CK_SG_GC_H_
#define INCLUDE_ZEPHYR_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CK_SG_GC_H_

#include <zephyr/dt-bindings/clock/mchp_pic32ck_sg_gc_clock.h>

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
};

struct clock_mchp_subsys_dfll48m_config {
        bool on_demand_en;

        bool closed_loop_en;

        enum clock_mchp_gclkgen src;

        uint16_t multiply_factor;
};

enum clock_mchp_pll_src_clock {
        CLOCK_MCHP_PLL_SRC_GCLK0,
        CLOCK_MCHP_PLL_SRC_GCLK1,
        CLOCK_MCHP_PLL_SRC_GCLK2,
        CLOCK_MCHP_PLL_SRC_GCLK3,
        CLOCK_MCHP_PLL_SRC_GCLK4,
        CLOCK_MCHP_PLL_SRC_GCLK5,
        CLOCK_MCHP_PLL_SRC_GCLK6,
        CLOCK_MCHP_PLL_SRC_GCLK7,
        CLOCK_MCHP_PLL_SRC_GCLK8,
        CLOCK_MCHP_PLL_SRC_GCLK9,
        CLOCK_MCHP_PLL_SRC_GCLK10,
        CLOCK_MCHP_PLL_SRC_GCLK11,
        CLOCK_MCHP_PLL_SRC_XOSC,
        CLOCK_MCHP_PLL_SRC_DFLL48M,

        CLOCK_MCHP_PLL_SRC_MAX = CLOCK_MCHP_PLL_SRC_DFLL48M
};

struct clock_mchp_subsys_pll_config {
        uint16_t feedback_divider_factor;

        uint8_t ref_division_factor;

        bool on_demand_en;

        enum clock_mchp_pll_src_clock src;
};

struct clock_mchp_subsys_pll_out_config {
        uint8_t output_division_factor;
};

enum clock_mchp_rtc_src_clock {
        CLOCK_MCHP_RTC_SRC_OSCULP1K = OSC32KCTRL_CLKSELCTRL_RTCSEL_ULP1K_Val,
        CLOCK_MCHP_RTC_SRC_OSCULP32K = OSC32KCTRL_CLKSELCTRL_RTCSEL_ULP32K_Val,
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
        CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT0,
        CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT1,
        CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT2,
        CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT3,
        CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT4,
        CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT5,

        CLOCK_MCHP_GCLK_SRC_MAX = CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT5
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

#endif /* INCLUDE_ZEPHYR_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CK_SG_GC_H_ */
```

## 491.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 191 行

头文件保护宏（Header guard）标记：`INCLUDE_ZEPHYR_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CK_SG_GC_H_`。

## 491.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html)
- [zephyr/dt-bindings/clock/mchp_pic32ck_sg_gc_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32ck__sg__gc__clock_8h.html)
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
- [clock_mchp_subsys_dfll48m_config](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md)
- [on_demand_en](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a8b5dca59c164a9c785fc763ed97dbcbd)
- [closed_loop_en](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a5f06274d52ac9a342f62361bb6451cc3)
- [clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#gaab34442b0d6c171691ae299675542777)
- [src](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#af9b0a365f56ef718b2bb74e460f74df9)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [multiply_factor](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a0056a9d73d353a31c5c6303e4f96fa1d)
- [clock_mchp_pll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555e)
- [CLOCK_MCHP_PLL_SRC_GCLK0](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555eaef24a9e72fe2d4f1518d04b081bfb344)
- [CLOCK_MCHP_PLL_SRC_GCLK1](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555eae6ea73001396449cab6b5ae14adce995)
- [CLOCK_MCHP_PLL_SRC_GCLK2](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555eac158d3d2881be2f4599a3fa17e10c7e4)
- [CLOCK_MCHP_PLL_SRC_GCLK3](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555eab27d86592af60943287f2eed0079a538)
- [CLOCK_MCHP_PLL_SRC_GCLK4](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555ea24133131a7e379620f4cccc8c272d3d2)
- [CLOCK_MCHP_PLL_SRC_GCLK5](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555ea7f589a8c783ca935e3a3bec4e00fe78a)
- [CLOCK_MCHP_PLL_SRC_GCLK6](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555ea47742caeb6c36cfbab2ea52b76375843)
- [CLOCK_MCHP_PLL_SRC_GCLK7](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555ead09414b3eb59c8c3192b06be62ceb0e5)
- [CLOCK_MCHP_PLL_SRC_GCLK8](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555ea8738be13a05d1f2e738b32c41446d7b9)
- [CLOCK_MCHP_PLL_SRC_GCLK9](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555eae253d07c8f5363965d92dbd067d634be)
- [CLOCK_MCHP_PLL_SRC_GCLK10](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555ea8b04fdb20116b7fe6e1c0f76c628db77)
- [CLOCK_MCHP_PLL_SRC_GCLK11](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555eacbcf8ac169420753c80c1b12ad10e517)
- [CLOCK_MCHP_PLL_SRC_XOSC](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555eaf7bd65f6bc9f42452f59f60623d50881)
- [CLOCK_MCHP_PLL_SRC_DFLL48M](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555ea855942173475ae101281766a4fda2e5f)
- [CLOCK_MCHP_PLL_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555ea097b57f49a9ed54a8e68a88c45af8540)
- [clock_mchp_subsys_pll_config](../clock_cmsis_model_reference/P019_clock_mchp_subsys_pll_config_结构体.md)
- [feedback_divider_factor](../clock_cmsis_model_reference/P019_clock_mchp_subsys_pll_config_结构体.md#a1d40f6f5bc7610d5db8d7fc7c16ccd54)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ref_division_factor](../clock_cmsis_model_reference/P019_clock_mchp_subsys_pll_config_结构体.md#ae4de7160ef688c54e4d7741b695353eb)
- [on_demand_en](../clock_cmsis_model_reference/P019_clock_mchp_subsys_pll_config_结构体.md#af96f2f4bdf60d50f3942c3cc55703ad6)
- [src](../clock_cmsis_model_reference/P019_clock_mchp_subsys_pll_config_结构体.md#a67f3c481143ff8f860ae7f2fabf16867)
- [clock_mchp_subsys_pll_out_config](../clock_cmsis_model_reference/P020_clock_mchp_subsys_pll_out_config_结构体.md)
- [output_division_factor](../clock_cmsis_model_reference/P020_clock_mchp_subsys_pll_out_config_结构体.md#a3483433887d306cc9f2acff66654cd32)
- [clock_mchp_rtc_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a2b83aa5b88c064d44d3a0ef7661a15cf)
- [CLOCK_MCHP_RTC_SRC_OSCULP1K](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a2b83aa5b88c064d44d3a0ef7661a15cfa3523c19ffb12654b4d1e663d6ef096ec)
- [CLOCK_MCHP_RTC_SRC_OSCULP32K](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a2b83aa5b88c064d44d3a0ef7661a15cfa4eeb4b4c5f682aa3c2c09fb7a321a68d)
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
- [CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT0](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989ad3453cbd92dca5da39da54a267e955b5)
- [CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT1](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a0242a7512bbb16e7d97113c66c26ea73)
- [CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT2](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989aeb2a16ab5ddfe55eab48831761c83aca)
- [CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT3](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a956353351be40288ebbc3c7c5d3480c9)
- [CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT4](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989aa906d7b53c240c7b358a33069e26bad0)
- [CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT5](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a9493982be1abdb53d65963d19fc17ab8)
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
- [mchp_pic32ck_sg_gc_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32ck__sg__gc__clock_8h.html)
- [clock_mchp_subsys_dfll48m_config::multiply_factor](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a0056a9d73d353a31c5c6303e4f96fa1d)
- [clock_mchp_subsys_dfll48m_config::closed_loop_en](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a5f06274d52ac9a342f62361bb6451cc3)
- [clock_mchp_subsys_dfll48m_config::on_demand_en](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#a8b5dca59c164a9c785fc763ed97dbcbd)
- [clock_mchp_subsys_dfll48m_config::src](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md#af9b0a365f56ef718b2bb74e460f74df9)
- [clock_mchp_subsys_gclkgen_config::run_in_standby_en](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#a59f3f908c254d4299164b5fea5885514)
- [clock_mchp_subsys_gclkgen_config::src](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#aeb553aa051490aefb8d38cc9ce7e8166)
- [clock_mchp_subsys_gclkgen_config::div_factor](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md#af803dcb746c1438f6e08ac30042d3651)
- [clock_mchp_subsys_gclkperiph_config::src](../clock_cmsis_model_reference/P014_clock_mchp_subsys_gclkperiph_config_结构体.md#a1727b4df3eb0dcff7365909002cef636)
- [clock_mchp_subsys_mclkcpu_config::division_factor](../clock_cmsis_model_reference/P015_clock_mchp_subsys_mclkcpu_config_结构体.md#a380cc94c6ed19143a29f2590af21f672)
- [clock_mchp_subsys_pll_config::feedback_divider_factor](../clock_cmsis_model_reference/P019_clock_mchp_subsys_pll_config_结构体.md#a1d40f6f5bc7610d5db8d7fc7c16ccd54)
- [clock_mchp_subsys_pll_config::src](../clock_cmsis_model_reference/P019_clock_mchp_subsys_pll_config_结构体.md#a67f3c481143ff8f860ae7f2fabf16867)
- [clock_mchp_subsys_pll_config::ref_division_factor](../clock_cmsis_model_reference/P019_clock_mchp_subsys_pll_config_结构体.md#ae4de7160ef688c54e4d7741b695353eb)
- [clock_mchp_subsys_pll_config::on_demand_en](../clock_cmsis_model_reference/P019_clock_mchp_subsys_pll_config_结构体.md#af96f2f4bdf60d50f3942c3cc55703ad6)
- [clock_mchp_subsys_pll_out_config::output_division_factor](../clock_cmsis_model_reference/P020_clock_mchp_subsys_pll_out_config_结构体.md#a3483433887d306cc9f2acff66654cd32)
- [clock_mchp_subsys_rtc_config::src](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md#af6a74f1140ddab14f3e8f4642284f443)
- [clock_mchp_subsys_xosc32k_config::on_demand_en](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md#afb7ecdb2ad0168376649c5acb0c5c765)
- [clock_mchp_subsys_xosc_config::on_demand_en](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md#a51e27943063374fa67b03509d8d8b962)

---

[上一章](P490_mchp-xec-ecia.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P492_mchp_clock_pic32cm_jh.h_源码浏览.md)
