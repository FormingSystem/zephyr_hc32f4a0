---
id: learning.zephyr-docs.api-source-reference.page-493
title: mchp_clock_pic32cm_pl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__pl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第493章\_mchp\_clock\_pic32cm\_pl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__pl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__pl_8h.html)。

## 493.1\_原始可见代码（Source Code）

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
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="agroup__clock__control__mchp__pic32cm__jh_html_gga073dab68c78edce3985eb201a039a989a26b8d25a8d166e0b8e79c77312897145"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_ga6c58f134b572f42ac3cca03856468c3a"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga073dab68c78edce3985eb201a039a989ace885f772c60e22702da938ef3f62b58"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga073dab68c78edce3985eb201a039a989ae064355a616a69896d7043124ee11675"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga6c58f134b572f42ac3cca03856468c3aa24645f855f7fa957422f19cc7ffca738"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga6c58f134b572f42ac3cca03856468c3aa29a78c5f4d28a252320ba789172be128"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga6c58f134b572f42ac3cca03856468c3aa2b42333cebbc90cd81265b1240120307"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga6c58f134b572f42ac3cca03856468c3aa3b829d3a31baec5bd6a59a3786443a10"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga6c58f134b572f42ac3cca03856468c3aa539e4664a82765a25cf5c4f6451138c0"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga6c58f134b572f42ac3cca03856468c3aa573b15fb8ba6477f12fd607eebaac897"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga6c58f134b572f42ac3cca03856468c3aa8c71c932640e2c3290ba139a79c33df0"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga6c58f134b572f42ac3cca03856468c3aa9fb40e8a98b517393f77ca6f0d5b3a24"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga6c58f134b572f42ac3cca03856468c3aac258887a28085108578b907f8e7f2d61"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_gga6c58f134b572f42ac3cca03856468c3aaf60b6260a551e23f020708f381aba34e"></a>
<a id="agroup__clock__control__mchp__pic32cm__pl_html_ggaab34442b0d6c171691ae299675542777aa224432a91de8df07361b1f624a11417"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_a9b6955116dae7fa53c8dad373a1ef9c9"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html_aab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe"></a>
<a id="amchp__pic32cm__pl__clock_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructclock__mchp__subsys__oschf__config_html"></a>
<a id="astructclock__mchp__subsys__oschf__config_html_a4980adab90c8f75a0b72de691a9f3b54"></a>

```c
/*
 * Copyright (c) 2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CM_PL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CM_PL_H_

#include <zephyr/dt-bindings/clock/mchp_pic32cm_pl_clock.h>


struct clock_mchp_subsys_oschf_config {
        bool on_demand_en;
};

enum clock_mchp_freq {
        CLOCK_FREQ_1KHZ = 1024,
        CLOCK_FREQ_32KHZ = 32768,
        CLOCK_FREQ_1MHZ = 1000000,
        CLOCK_FREQ_2MHZ = 2000000,
        CLOCK_FREQ_3MHZ = 3000000,
        CLOCK_FREQ_4MHZ = 4000000,
        CLOCK_FREQ_8MHZ = 8000000,
        CLOCK_FREQ_12MHZ = 12000000,
        CLOCK_FREQ_20MHZ = 20000000,
        CLOCK_FREQ_24MHZ = 24000000,
};

enum clock_mchp_gclk_src_clock {
        CLOCK_MCHP_GCLK_SRC_OSCHF = 0,
        CLOCK_MCHP_GCLK_SRC_OSC32K,
        CLOCK_MCHP_GCLK_SRC_XOSC32K,
        CLOCK_MCHP_GCLK_SRC_GCLKPIN,
        CLOCK_MCHP_GCLK_SRC_GCLKGEN1,
        CLOCK_MCHP_GCLK_SRC_COUNT
};

enum clock_mchp_gclkgen {
        CLOCK_MCHP_GCLKGEN_GEN0,
        CLOCK_MCHP_GCLKGEN_GEN1,
        CLOCK_MCHP_GCLKGEN_GEN2,
        CLOCK_MCHP_GCLKGEN_GEN3,
        CLOCK_MCHP_GCLKGEN_MAX
};

typedef uint32_t *clock_mchp_rate_t;


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CM_PL_H_ */
```

## 493.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 95 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_PIC32CM_PL_H_`。

## 493.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__pl_8h.html)
- [zephyr/dt-bindings/clock/mchp_pic32cm_pl_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__pl__clock_8h.html)
- [clock_mchp_subsys_oschf_config](../clock_cmsis_model_reference/P018_clock_mchp_subsys_oschf_config_结构体.md)
- [on_demand_en](../clock_cmsis_model_reference/P018_clock_mchp_subsys_oschf_config_结构体.md#a4980adab90c8f75a0b72de691a9f3b54)
- [clock_mchp_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#ga6c58f134b572f42ac3cca03856468c3a)
- [CLOCK_FREQ_1KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga6c58f134b572f42ac3cca03856468c3aa29a78c5f4d28a252320ba789172be128)
- [CLOCK_FREQ_32KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga6c58f134b572f42ac3cca03856468c3aa539e4664a82765a25cf5c4f6451138c0)
- [CLOCK_FREQ_1MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga6c58f134b572f42ac3cca03856468c3aa573b15fb8ba6477f12fd607eebaac897)
- [CLOCK_FREQ_2MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga6c58f134b572f42ac3cca03856468c3aa9fb40e8a98b517393f77ca6f0d5b3a24)
- [CLOCK_FREQ_3MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga6c58f134b572f42ac3cca03856468c3aaf60b6260a551e23f020708f381aba34e)
- [CLOCK_FREQ_4MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga6c58f134b572f42ac3cca03856468c3aac258887a28085108578b907f8e7f2d61)
- [CLOCK_FREQ_8MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga6c58f134b572f42ac3cca03856468c3aa8c71c932640e2c3290ba139a79c33df0)
- [CLOCK_FREQ_12MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga6c58f134b572f42ac3cca03856468c3aa24645f855f7fa957422f19cc7ffca738)
- [CLOCK_FREQ_20MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga6c58f134b572f42ac3cca03856468c3aa3b829d3a31baec5bd6a59a3786443a10)
- [CLOCK_FREQ_24MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga6c58f134b572f42ac3cca03856468c3aa2b42333cebbc90cd81265b1240120307)
- [clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989)
- [CLOCK_MCHP_GCLK_SRC_OSCHF](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga073dab68c78edce3985eb201a039a989ae064355a616a69896d7043124ee11675)
- [CLOCK_MCHP_GCLK_SRC_OSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a26b8d25a8d166e0b8e79c77312897145)
- [CLOCK_MCHP_GCLK_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380)
- [CLOCK_MCHP_GCLK_SRC_GCLKPIN](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef)
- [CLOCK_MCHP_GCLK_SRC_GCLKGEN1](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9)
- [CLOCK_MCHP_GCLK_SRC_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#gga073dab68c78edce3985eb201a039a989ace885f772c60e22702da938ef3f62b58)
- [clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777)
- [CLOCK_MCHP_GCLKGEN_GEN0](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f)
- [CLOCK_MCHP_GCLKGEN_GEN1](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424)
- [CLOCK_MCHP_GCLKGEN_GEN2](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe)
- [CLOCK_MCHP_GCLKGEN_GEN3](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08)
- [CLOCK_MCHP_GCLKGEN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html#ggaab34442b0d6c171691ae299675542777aa224432a91de8df07361b1f624a11417)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clock_mchp_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a9b6955116dae7fa53c8dad373a1ef9c9)
- [mchp_pic32cm_pl_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__pl__clock_8h.html)
- [clock_mchp_subsys_oschf_config::on_demand_en](../clock_cmsis_model_reference/P018_clock_mchp_subsys_oschf_config_结构体.md#a4980adab90c8f75a0b72de691a9f3b54)

---

[上一章](P492_mchp_clock_pic32cm_jh.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P494_mchp_clock_pic32cm_sg_gc.h_源码浏览.md)
