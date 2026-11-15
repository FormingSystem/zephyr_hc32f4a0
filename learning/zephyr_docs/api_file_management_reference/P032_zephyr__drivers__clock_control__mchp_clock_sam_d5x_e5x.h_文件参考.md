---
id: learning.zephyr-docs.api-file-management-reference.page-32
title: zephyr__drivers__clock_control__mchp_clock_sam_d5x_e5x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__sam__d5x__e5x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zephyr\_\_drivers\_\_clock\_control\_\_mchp\_clock\_sam\_d5x\_e5x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__sam__d5x__e5x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip SAM D5x/E5x系列的时钟控制（Clock Control）头文件。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/clock/mchp_sam_d5x_e5x_clock.h>
```

查看此文件的源码。

Microchip SAM D5x/E5x 系列的时钟控制头文件（clock control header）。本文件提供 SAM D5x/E5x 系列的时钟驱动接口定义及结构体。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 32.1\_数据结构（Data Structures）

<a id="r_clock_5Fmchp_5Fsubsys_5Fxosc_5Fconfig"></a>

```c
struct clock_mchp_subsys_xosc_config
```

相关声明：[clock_mchp_subsys_xosc_config](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md)。

外部晶体振荡器（External Crystal Oscillator）配置结构体。

<a id="r_clock_5Fmchp_5Fsubsys_5Fdfll_5Fconfig"></a>

```c
struct clock_mchp_subsys_dfll_config
```

相关声明：[clock_mchp_subsys_dfll_config](../clock_cmsis_model_reference/P009_clock_mchp_subsys_dfll_config_结构体.md)。

DFLL 配置。

<a id="r_clock_5Fmchp_5Fsubsys_5Ffdpll_5Fconfig"></a>

```c
struct clock_mchp_subsys_fdpll_config
```

相关声明：[clock_mchp_subsys_fdpll_config](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md)。

分数数字锁相环（Fractional DPLL，FDPLL）配置。

<a id="r_clock_5Fmchp_5Fsubsys_5Frtc_5Fconfig"></a>

```c
struct clock_mchp_subsys_rtc_config
```

相关声明：[clock_mchp_subsys_rtc_config](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md)。

实时时钟（Real-Time Clock，RTC）配置结构体。

<a id="r_clock_5Fmchp_5Fsubsys_5Fxosc32k_5Fconfig"></a>

```c
struct clock_mchp_subsys_xosc32k_config
```

相关声明：[clock_mchp_subsys_xosc32k_config](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md)。

外部 32.768 kHz 晶体振荡器（External Crystal Oscillator）配置结构体。

<a id="r_clock_5Fmchp_5Fsubsys_5Fgclkgen_5Fconfig"></a>

```c
struct clock_mchp_subsys_gclkgen_config
```

相关声明：[clock_mchp_subsys_gclkgen_config](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md)。

通用时钟发生器（GCLK Generator）配置结构体。

<a id="r_clock_5Fmchp_5Fsubsys_5Fgclkperiph_5Fconfig"></a>

```c
struct clock_mchp_subsys_gclkperiph_config
```

相关声明：[clock_mchp_subsys_gclkperiph_config](../clock_cmsis_model_reference/P014_clock_mchp_subsys_gclkperiph_config_结构体.md)。

通用时钟外设（GCLK Peripheral）配置结构体。

<a id="r_clock_5Fmchp_5Fsubsys_5Fmclkcpu_5Fconfig"></a>

```c
struct clock_mchp_subsys_mclkcpu_config
```

相关声明：[clock_mchp_subsys_mclkcpu_config](../clock_cmsis_model_reference/P015_clock_mchp_subsys_mclkcpu_config_结构体.md)。

主时钟（MCLK）配置结构体。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 32.2\_类型定义（Typedefs）

<a id="r_ga9b6955116dae7fa53c8dad373a1ef9c9"></a>

```c
typedef uint32_t * clock_mchp_rate_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[clock_mchp_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga9b6955116dae7fa53c8dad373a1ef9c9)。

时钟频率数据类型（clock rate datatype）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 32.3\_枚举（Enumerations）

<a id="r_gaab34442b0d6c171691ae299675542777"></a>

```c
enum clock_mchp_gclkgen { CLOCK_MCHP_GCLKGEN_GEN0 , CLOCK_MCHP_GCLKGEN_GEN1 , CLOCK_MCHP_GCLKGEN_GEN2 , CLOCK_MCHP_GCLKGEN_GEN3 , CLOCK_MCHP_GCLKGEN_GEN4 , CLOCK_MCHP_GCLKGEN_GEN5 , CLOCK_MCHP_GCLKGEN_GEN6 , CLOCK_MCHP_GCLKGEN_GEN7 , CLOCK_MCHP_GCLKGEN_GEN8 , CLOCK_MCHP_GCLKGEN_GEN9 , CLOCK_MCHP_GCLKGEN_GEN10 , CLOCK_MCHP_GCLKGEN_GEN11 }
```

相关声明：[clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaab34442b0d6c171691ae299675542777)、[CLOCK_MCHP_GCLKGEN_GEN0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f)、[CLOCK_MCHP_GCLKGEN_GEN1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424)、[CLOCK_MCHP_GCLKGEN_GEN2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe)、[CLOCK_MCHP_GCLKGEN_GEN3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08)、[CLOCK_MCHP_GCLKGEN_GEN4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a69bd2c6d8f016e8ecdfd07fba7268dcc)、[CLOCK_MCHP_GCLKGEN_GEN5](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a20bf106031eb19f25b8e3b1250033088)、[CLOCK_MCHP_GCLKGEN_GEN6](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a9cbc78f597c2930b36280c59164e12ae)、[CLOCK_MCHP_GCLKGEN_GEN7](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a71ead69f87ccd57496b0467a6264d411)、[CLOCK_MCHP_GCLKGEN_GEN8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777aff9b0bedc5de2cfe3259df2910ab55f9)、[CLOCK_MCHP_GCLKGEN_GEN9](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a96de017372252af6f1bcab2cdb32c2f1)、[CLOCK_MCHP_GCLKGEN_GEN10](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a63f142bb2401a057b9ba7b4a8f60eb60)、[CLOCK_MCHP_GCLKGEN_GEN11](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a905cb4bab8f6bb50f690de6a9e970695)。

通用时钟（GCLK）发生器编号。

<a id="r_gaca271f1fae614cbd8c12fed31bcb64ea"></a>

```c
enum clock_mchp_fdpll_src_clock { CLOCK_MCHP_FDPLL_SRC_GCLK0 , CLOCK_MCHP_FDPLL_SRC_GCLK1 , CLOCK_MCHP_FDPLL_SRC_GCLK2 , CLOCK_MCHP_FDPLL_SRC_GCLK3 , CLOCK_MCHP_FDPLL_SRC_GCLK4 , CLOCK_MCHP_FDPLL_SRC_GCLK5 , CLOCK_MCHP_FDPLL_SRC_GCLK6 , CLOCK_MCHP_FDPLL_SRC_GCLK7 , CLOCK_MCHP_FDPLL_SRC_GCLK8 , CLOCK_MCHP_FDPLL_SRC_GCLK9 , CLOCK_MCHP_FDPLL_SRC_GCLK10 , CLOCK_MCHP_FDPLL_SRC_GCLK11 , CLOCK_MCHP_FDPLL_SRC_XOSC32K , CLOCK_MCHP_FDPLL_SRC_XOSC0 , CLOCK_MCHP_FDPLL_SRC_XOSC1 , CLOCK_MCHP_FDPLL_SRC_MAX = CLOCK_MCHP_FDPLL_SRC_XOSC1 }
```

相关声明：[clock_mchp_fdpll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaca271f1fae614cbd8c12fed31bcb64ea)、[CLOCK_MCHP_FDPLL_SRC_GCLK0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa2b4dbfa6f3b2985c25df5457babcfc19)、[CLOCK_MCHP_FDPLL_SRC_GCLK1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaad463d37743aa9dce5a24ea0b9f2f6f83)、[CLOCK_MCHP_FDPLL_SRC_GCLK2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa9e1c784e19edd414b2c51196fb0ea630)、[CLOCK_MCHP_FDPLL_SRC_GCLK3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa49e87978ba1e4471c0dc76705950f7d7)、[CLOCK_MCHP_FDPLL_SRC_GCLK4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa5bb7c103fe4f9548da6f6ff38b8e4fe6)、[CLOCK_MCHP_FDPLL_SRC_GCLK5](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa2e3099c6db41c26e126ea236ae1f4917)、[CLOCK_MCHP_FDPLL_SRC_GCLK6](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaad1027fef245b5a24b80e383981d40913)、[CLOCK_MCHP_FDPLL_SRC_GCLK7](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa1d753cfcae1b5d0249908d1567257cbc)、[CLOCK_MCHP_FDPLL_SRC_GCLK8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaabdb11235f190deb557d9e19d4c24618c)、[CLOCK_MCHP_FDPLL_SRC_GCLK9](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaac3bbb2366b36bd1e9d47c12bd9fabb3e)、[CLOCK_MCHP_FDPLL_SRC_GCLK10](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa4ef8901c275799cfb25c0713947ac05e)、[CLOCK_MCHP_FDPLL_SRC_GCLK11](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa5d6f026a21a52f817f5744936cdc4963)、[CLOCK_MCHP_FDPLL_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa8f6301943a69f328ac49e0b302c6e1e1)、[CLOCK_MCHP_FDPLL_SRC_XOSC0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa2ba17f11b30e983b5710e7f2d8178e62)、[CLOCK_MCHP_FDPLL_SRC_XOSC1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa31d3b1444e97f20b9154f0605033ef50)、[CLOCK_MCHP_FDPLL_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaab1e1b66c6b826cbc9077fb579c73466b)。

FDPLL 的源时钟（source clocks）。

<a id="r_ga2b83aa5b88c064d44d3a0ef7661a15cf"></a>

```c
enum clock_mchp_rtc_src_clock { CLOCK_MCHP_RTC_SRC_ULP1K = OSC32KCTRL_RTCCTRL_RTCSEL_ULP1K , CLOCK_MCHP_RTC_SRC_ULP32K = OSC32KCTRL_RTCCTRL_RTCSEL_ULP32K , CLOCK_MCHP_RTC_SRC_XOSC1K = OSC32KCTRL_RTCCTRL_RTCSEL_XOSC1K , CLOCK_MCHP_RTC_SRC_XOSC32K = OSC32KCTRL_RTCCTRL_RTCSEL_XOSC32K }
```

相关声明：[clock_mchp_rtc_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga2b83aa5b88c064d44d3a0ef7661a15cf)、[CLOCK_MCHP_RTC_SRC_ULP1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga2b83aa5b88c064d44d3a0ef7661a15cfafaa5cfa19e470035ad1cec308aa63f7b)、[CLOCK_MCHP_RTC_SRC_ULP32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga2b83aa5b88c064d44d3a0ef7661a15cfa9095a4473e6e218ea0d2715695ecb2ff)、[CLOCK_MCHP_RTC_SRC_XOSC1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga2b83aa5b88c064d44d3a0ef7661a15cfae738ec040a54d0b171192d122abdd332)、[CLOCK_MCHP_RTC_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296)。

实时时钟（RTC）的源时钟（source clocks）。

<a id="r_ga073dab68c78edce3985eb201a039a989"></a>

```c
enum clock_mchp_gclk_src_clock { CLOCK_MCHP_GCLK_SRC_XOSC0 , CLOCK_MCHP_GCLK_SRC_XOSC1 , CLOCK_MCHP_GCLK_SRC_GCLKPIN , CLOCK_MCHP_GCLK_SRC_GCLKGEN1 , CLOCK_MCHP_GCLK_SRC_OSCULP32K , CLOCK_MCHP_GCLK_SRC_XOSC32K , CLOCK_MCHP_GCLK_SRC_DFLL , CLOCK_MCHP_GCLK_SRC_FDPLL0 , CLOCK_MCHP_GCLK_SRC_FDPLL1 , CLOCK_MCHP_GCLK_SRC_MAX = CLOCK_MCHP_GCLK_SRC_FDPLL1 }
```

相关声明：[clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga073dab68c78edce3985eb201a039a989)、[CLOCK_MCHP_GCLK_SRC_XOSC0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989a081d24e09b578e1b0d3183c370ad2bf7)、[CLOCK_MCHP_GCLK_SRC_XOSC1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989ae9bfa0dbbbe627f88ea091849e286f4b)、[CLOCK_MCHP_GCLK_SRC_GCLKPIN](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef)、[CLOCK_MCHP_GCLK_SRC_GCLKGEN1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9)、[CLOCK_MCHP_GCLK_SRC_OSCULP32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6)、[CLOCK_MCHP_GCLK_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380)、[CLOCK_MCHP_GCLK_SRC_DFLL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989aa28a89d9e45956d7e9a6b7d568bb6f9a)、[CLOCK_MCHP_GCLK_SRC_FDPLL0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989a2c47a402ae41f2c8b237c470918be6ee)、[CLOCK_MCHP_GCLK_SRC_FDPLL1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989aa296b5ed39a1a34a8e22cd80fb590f46)、[CLOCK_MCHP_GCLK_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768)。

通用时钟（GCLK）发生器的源时钟。

<a id="r_ga5835567db8d16c4eeb7a03b843ac6254"></a>

```c
enum clock_mchp_mclk_cpu_div { CLOCK_MCHP_MCLK_CPU_DIV_1 = 1 , CLOCK_MCHP_MCLK_CPU_DIV_2 = 2 , CLOCK_MCHP_MCLK_CPU_DIV_4 = 4 , CLOCK_MCHP_MCLK_CPU_DIV_8 = 8 , CLOCK_MCHP_MCLK_CPU_DIV_16 = 16 , CLOCK_MCHP_MCLK_CPU_DIV_32 = 32 , CLOCK_MCHP_MCLK_CPU_DIV_64 = 64 , CLOCK_MCHP_MCLK_CPU_DIV_128 = 128 }
```

相关声明：[clock_mchp_mclk_cpu_div](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga5835567db8d16c4eeb7a03b843ac6254)、[CLOCK_MCHP_MCLK_CPU_DIV_1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254a9f893cbec63df56227f17098ddf70074)、[CLOCK_MCHP_MCLK_CPU_DIV_2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254ac52aba85d20e21bd3135cc46e467dbfc)、[CLOCK_MCHP_MCLK_CPU_DIV_4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254ad251e58f232eaa9d45cce47e600b506f)、[CLOCK_MCHP_MCLK_CPU_DIV_8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254ace4fa9213f609c27198c75f17b0f7beb)、[CLOCK_MCHP_MCLK_CPU_DIV_16](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254ae11a4d93aaafcfaeed5a7cc6e0a1de89)、[CLOCK_MCHP_MCLK_CPU_DIV_32](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254ab071663992b6be65b6f77442239d3157)、[CLOCK_MCHP_MCLK_CPU_DIV_64](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254a688a2dbe64b6a818ab84f26cc983b3f0)、[CLOCK_MCHP_MCLK_CPU_DIV_128](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254aefa35c60f9274b62c0b829c1c24a571b)。

CPU 的 MCLK 预分频器分频比。


## 32.4\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/clock/mchp_sam_d5x_e5x_clock.h](../api_source_compiler_device_reference/P016_mchp_sam_d5x_e5x_clock.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P496_mchp_clock_sam_d5x_e5x.h_源码浏览.md)
- [clock_mchp_subsys_xosc_config](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md)
- [clock_mchp_subsys_dfll_config](../clock_cmsis_model_reference/P009_clock_mchp_subsys_dfll_config_结构体.md)
- [clock_mchp_subsys_fdpll_config](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md)
- [clock_mchp_subsys_rtc_config](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md)
- [clock_mchp_subsys_xosc32k_config](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md)
- [clock_mchp_subsys_gclkgen_config](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md)
- [clock_mchp_subsys_gclkperiph_config](../clock_cmsis_model_reference/P014_clock_mchp_subsys_gclkperiph_config_结构体.md)
- [clock_mchp_subsys_mclkcpu_config](../clock_cmsis_model_reference/P015_clock_mchp_subsys_mclkcpu_config_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [clock_mchp_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga9b6955116dae7fa53c8dad373a1ef9c9)
- [clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaab34442b0d6c171691ae299675542777)
- [CLOCK_MCHP_GCLKGEN_GEN0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f)
- [CLOCK_MCHP_GCLKGEN_GEN1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424)
- [CLOCK_MCHP_GCLKGEN_GEN2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe)
- [CLOCK_MCHP_GCLKGEN_GEN3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08)
- [CLOCK_MCHP_GCLKGEN_GEN4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a69bd2c6d8f016e8ecdfd07fba7268dcc)
- [CLOCK_MCHP_GCLKGEN_GEN5](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a20bf106031eb19f25b8e3b1250033088)
- [CLOCK_MCHP_GCLKGEN_GEN6](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a9cbc78f597c2930b36280c59164e12ae)
- [CLOCK_MCHP_GCLKGEN_GEN7](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a71ead69f87ccd57496b0467a6264d411)
- [CLOCK_MCHP_GCLKGEN_GEN8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777aff9b0bedc5de2cfe3259df2910ab55f9)
- [CLOCK_MCHP_GCLKGEN_GEN9](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a96de017372252af6f1bcab2cdb32c2f1)
- [CLOCK_MCHP_GCLKGEN_GEN10](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a63f142bb2401a057b9ba7b4a8f60eb60)
- [CLOCK_MCHP_GCLKGEN_GEN11](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaab34442b0d6c171691ae299675542777a905cb4bab8f6bb50f690de6a9e970695)
- [clock_mchp_fdpll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaca271f1fae614cbd8c12fed31bcb64ea)
- [CLOCK_MCHP_FDPLL_SRC_GCLK0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa2b4dbfa6f3b2985c25df5457babcfc19)
- [CLOCK_MCHP_FDPLL_SRC_GCLK1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaad463d37743aa9dce5a24ea0b9f2f6f83)
- [CLOCK_MCHP_FDPLL_SRC_GCLK2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa9e1c784e19edd414b2c51196fb0ea630)
- [CLOCK_MCHP_FDPLL_SRC_GCLK3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa49e87978ba1e4471c0dc76705950f7d7)
- [CLOCK_MCHP_FDPLL_SRC_GCLK4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa5bb7c103fe4f9548da6f6ff38b8e4fe6)
- [CLOCK_MCHP_FDPLL_SRC_GCLK5](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa2e3099c6db41c26e126ea236ae1f4917)
- [CLOCK_MCHP_FDPLL_SRC_GCLK6](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaad1027fef245b5a24b80e383981d40913)
- [CLOCK_MCHP_FDPLL_SRC_GCLK7](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa1d753cfcae1b5d0249908d1567257cbc)
- [CLOCK_MCHP_FDPLL_SRC_GCLK8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaabdb11235f190deb557d9e19d4c24618c)
- [CLOCK_MCHP_FDPLL_SRC_GCLK9](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaac3bbb2366b36bd1e9d47c12bd9fabb3e)
- [CLOCK_MCHP_FDPLL_SRC_GCLK10](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa4ef8901c275799cfb25c0713947ac05e)
- [CLOCK_MCHP_FDPLL_SRC_GCLK11](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa5d6f026a21a52f817f5744936cdc4963)
- [CLOCK_MCHP_FDPLL_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa8f6301943a69f328ac49e0b302c6e1e1)
- [CLOCK_MCHP_FDPLL_SRC_XOSC0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa2ba17f11b30e983b5710e7f2d8178e62)
- [CLOCK_MCHP_FDPLL_SRC_XOSC1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaa31d3b1444e97f20b9154f0605033ef50)
- [CLOCK_MCHP_FDPLL_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ggaca271f1fae614cbd8c12fed31bcb64eaab1e1b66c6b826cbc9077fb579c73466b)
- [clock_mchp_rtc_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga2b83aa5b88c064d44d3a0ef7661a15cf)
- [CLOCK_MCHP_RTC_SRC_ULP1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga2b83aa5b88c064d44d3a0ef7661a15cfafaa5cfa19e470035ad1cec308aa63f7b)
- [CLOCK_MCHP_RTC_SRC_ULP32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga2b83aa5b88c064d44d3a0ef7661a15cfa9095a4473e6e218ea0d2715695ecb2ff)
- [CLOCK_MCHP_RTC_SRC_XOSC1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga2b83aa5b88c064d44d3a0ef7661a15cfae738ec040a54d0b171192d122abdd332)
- [CLOCK_MCHP_RTC_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296)
- [clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga073dab68c78edce3985eb201a039a989)
- [CLOCK_MCHP_GCLK_SRC_XOSC0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989a081d24e09b578e1b0d3183c370ad2bf7)
- [CLOCK_MCHP_GCLK_SRC_XOSC1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989ae9bfa0dbbbe627f88ea091849e286f4b)
- [CLOCK_MCHP_GCLK_SRC_GCLKPIN](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef)
- [CLOCK_MCHP_GCLK_SRC_GCLKGEN1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9)
- [CLOCK_MCHP_GCLK_SRC_OSCULP32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6)
- [CLOCK_MCHP_GCLK_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380)
- [CLOCK_MCHP_GCLK_SRC_DFLL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989aa28a89d9e45956d7e9a6b7d568bb6f9a)
- [CLOCK_MCHP_GCLK_SRC_FDPLL0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989a2c47a402ae41f2c8b237c470918be6ee)
- [CLOCK_MCHP_GCLK_SRC_FDPLL1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989aa296b5ed39a1a34a8e22cd80fb590f46)
- [CLOCK_MCHP_GCLK_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768)
- [clock_mchp_mclk_cpu_div](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga5835567db8d16c4eeb7a03b843ac6254)
- [CLOCK_MCHP_MCLK_CPU_DIV_1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254a9f893cbec63df56227f17098ddf70074)
- [CLOCK_MCHP_MCLK_CPU_DIV_2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254ac52aba85d20e21bd3135cc46e467dbfc)
- [CLOCK_MCHP_MCLK_CPU_DIV_4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254ad251e58f232eaa9d45cce47e600b506f)
- [CLOCK_MCHP_MCLK_CPU_DIV_8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254ace4fa9213f609c27198c75f17b0f7beb)
- [CLOCK_MCHP_MCLK_CPU_DIV_16](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254ae11a4d93aaafcfaeed5a7cc6e0a1de89)
- [CLOCK_MCHP_MCLK_CPU_DIV_32](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254ab071663992b6be65b6f77442239d3157)
- [CLOCK_MCHP_MCLK_CPU_DIV_64](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254a688a2dbe64b6a818ab84f26cc983b3f0)
- [CLOCK_MCHP_MCLK_CPU_DIV_128](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gga5835567db8d16c4eeb7a03b843ac6254aefa35c60f9274b62c0b829c1c24a571b)

<a id="header-details"></a>

---

[上一章](P031_zephyr__drivers__clock_control__mchp_clock_pic32cz_ca.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P033_zephyr__drivers__mfd__tle9104.h_文件参考.md)
