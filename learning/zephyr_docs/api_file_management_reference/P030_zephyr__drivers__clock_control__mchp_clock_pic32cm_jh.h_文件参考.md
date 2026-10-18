---
id: learning.zephyr-docs.api-file-management-reference.page-30
title: zephyr__drivers__clock_control__mchp_clock_pic32cm_jh.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_zephyr\_\_drivers\_\_clock\_control\_\_mchp\_clock\_pic32cm\_jh.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip PIC32CM JH系列的时钟控制（Clock Control）头文件。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/clock/mchp_pic32cm_jh_clock.h>
```

查看此文件的源码。

Microchip PIC32CM JH 系列的时钟控制头文件（clock control header）。本文件提供 PIC32CM JH 系列的时钟驱动接口定义及结构体。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 30.1\_数据结构（Data Structures）

<a id="r_clock_5Fmchp_5Fsubsys_5Fxosc_5Fconfig"></a>

```c
struct clock_mchp_subsys_xosc_config
```

相关声明：[clock_mchp_subsys_xosc_config](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md)。

外部晶体振荡器（External Crystal Oscillator）配置结构体。

<a id="r_clock_5Fmchp_5Fsubsys_5Fosc48m_5Fconfig"></a>

```c
struct clock_mchp_subsys_osc48m_config
```

相关声明：[clock_mchp_subsys_osc48m_config](../clock_cmsis_model_reference/P017_clock_mchp_subsys_osc48m_config_结构体.md)。

内部 48 MHz 振荡器（OSC48M）配置。

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

<a id="r_clock_5Fmchp_5Fsubsys_5Fosc32k_5Fconfig"></a>

```c
struct clock_mchp_subsys_osc32k_config
```

相关声明：[clock_mchp_subsys_osc32k_config](../clock_cmsis_model_reference/P016_clock_mchp_subsys_osc32k_config_结构体.md)。

32 kHz 内部振荡器（OSC32K）配置。

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

## 30.2\_类型定义（Typedefs）

<a id="r_ga9b6955116dae7fa53c8dad373a1ef9c9"></a>

```c
typedef uint32_t * clock_mchp_rate_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[clock_mchp_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga9b6955116dae7fa53c8dad373a1ef9c9)。

时钟频率数据类型（clock rate datatype）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 30.3\_枚举（Enumerations）

<a id="r_ga4303aa06f4b9a93874f2d26406e788e3"></a>

```c
enum clock_mchp_osc48m_divider_freq { CLOCK_MCHP_DIVIDER_48_MHZ , CLOCK_MCHP_DIVIDER_24_MHZ , CLOCK_MCHP_DIVIDER_16_MHZ , CLOCK_MCHP_DIVIDER_12_MHZ , CLOCK_MCHP_DIVIDER_9_6_MHZ , CLOCK_MCHP_DIVIDER_8_MHZ , CLOCK_MCHP_DIVIDER_6_86_MHZ , CLOCK_MCHP_DIVIDER_6_MHZ , CLOCK_MCHP_DIVIDER_5_33_MHZ , CLOCK_MCHP_DIVIDER_4_8_MHZ , CLOCK_MCHP_DIVIDER_4_36_MHZ , CLOCK_MCHP_DIVIDER_4_MHZ , CLOCK_MCHP_DIVIDER_3_69_MHZ , CLOCK_MCHP_DIVIDER_3_43_MHZ , CLOCK_MCHP_DIVIDER_3_2_MHZ , CLOCK_MCHP_DIVIDER_3_MHZ }
```

相关声明：[clock_mchp_osc48m_divider_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga4303aa06f4b9a93874f2d26406e788e3)、[CLOCK_MCHP_DIVIDER_48_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3ae15895137cfed2a01dc07fd073c7f4f0)、[CLOCK_MCHP_DIVIDER_24_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a5341cf2520f14d53305b552e29d336af)、[CLOCK_MCHP_DIVIDER_16_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3af1947f866264e2b7eca4a0dbba0223cd)、[CLOCK_MCHP_DIVIDER_12_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a97968c136ce06b10ff5b78fdeec82c6b)、[CLOCK_MCHP_DIVIDER_9_6_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3afce32516f8303f06461a7edb1512cb4b)、[CLOCK_MCHP_DIVIDER_8_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3ac2e281fba8772d11634fa74f1559e6ae)、[CLOCK_MCHP_DIVIDER_6_86_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3aa6e359c000dc41599beaf5937d7b91b1)、[CLOCK_MCHP_DIVIDER_6_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a1d3ab3603b8569a32492a33a7343b51b)、[CLOCK_MCHP_DIVIDER_5_33_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a06c5e0bcabf7b54347f7e2c4cb54f2e1)、[CLOCK_MCHP_DIVIDER_4_8_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a68d97439120b74cfb174d6d9f7254c57)、[CLOCK_MCHP_DIVIDER_4_36_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3adb65fbb10b4703d719fe61dd044da5e9)、[CLOCK_MCHP_DIVIDER_4_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3ac5a35357502c5bf9ca76f5a935efbcb1)、[CLOCK_MCHP_DIVIDER_3_69_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a8dceb2229cb86ce500350fcb3f795a38)、[CLOCK_MCHP_DIVIDER_3_43_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3ac808175c0850ab5634c87fc49a2cde89)、[CLOCK_MCHP_DIVIDER_3_2_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3af8fcf13844de18b99b21de542e31f2d9)、[CLOCK_MCHP_DIVIDER_3_MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga4303aa06f4b9a93874f2d26406e788e3a4980f4845c33d559860cb4a2c8cbe8ab)。

通过调整分频比（division ratio），控制 OSC48M 振荡器的频率范围。

<a id="r_gaca271f1fae614cbd8c12fed31bcb64ea"></a>

```c
enum clock_mchp_fdpll_src_clock { CLOCK_MCHP_FDPLL_SRC_GCLK0 , CLOCK_MCHP_FDPLL_SRC_GCLK1 , CLOCK_MCHP_FDPLL_SRC_GCLK2 , CLOCK_MCHP_FDPLL_SRC_GCLK3 , CLOCK_MCHP_FDPLL_SRC_GCLK4 , CLOCK_MCHP_FDPLL_SRC_GCLK5 , CLOCK_MCHP_FDPLL_SRC_GCLK6 , CLOCK_MCHP_FDPLL_SRC_GCLK7 , CLOCK_MCHP_FDPLL_SRC_GCLK8 , CLOCK_MCHP_FDPLL_SRC_XOSC32K , CLOCK_MCHP_FDPLL_SRC_XOSC , CLOCK_MCHP_FDPLL_SRC_MAX = CLOCK_MCHP_FDPLL_SRC_XOSC }
```

相关声明：[clock_mchp_fdpll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gaca271f1fae614cbd8c12fed31bcb64ea)、[CLOCK_MCHP_FDPLL_SRC_GCLK0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa2b4dbfa6f3b2985c25df5457babcfc19)、[CLOCK_MCHP_FDPLL_SRC_GCLK1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaad463d37743aa9dce5a24ea0b9f2f6f83)、[CLOCK_MCHP_FDPLL_SRC_GCLK2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa9e1c784e19edd414b2c51196fb0ea630)、[CLOCK_MCHP_FDPLL_SRC_GCLK3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa49e87978ba1e4471c0dc76705950f7d7)、[CLOCK_MCHP_FDPLL_SRC_GCLK4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa5bb7c103fe4f9548da6f6ff38b8e4fe6)、[CLOCK_MCHP_FDPLL_SRC_GCLK5](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa2e3099c6db41c26e126ea236ae1f4917)、[CLOCK_MCHP_FDPLL_SRC_GCLK6](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaad1027fef245b5a24b80e383981d40913)、[CLOCK_MCHP_FDPLL_SRC_GCLK7](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa1d753cfcae1b5d0249908d1567257cbc)、[CLOCK_MCHP_FDPLL_SRC_GCLK8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaabdb11235f190deb557d9e19d4c24618c)、[CLOCK_MCHP_FDPLL_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa8f6301943a69f328ac49e0b302c6e1e1)、[CLOCK_MCHP_FDPLL_SRC_XOSC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaa5049effd0b7a893f2e278b857010e24f)、[CLOCK_MCHP_FDPLL_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaca271f1fae614cbd8c12fed31bcb64eaab1e1b66c6b826cbc9077fb579c73466b)。

FDPLL 的源时钟（source clocks）。

<a id="r_ga2b83aa5b88c064d44d3a0ef7661a15cf"></a>

```c
enum clock_mchp_rtc_src_clock { CLOCK_MCHP_RTC_SRC_ULP1K = OSC32KCTRL_RTCCTRL_RTCSEL_ULP1K , CLOCK_MCHP_RTC_SRC_ULP32K = OSC32KCTRL_RTCCTRL_RTCSEL_ULP32K , CLOCK_MCHP_RTC_SRC_OSC1K = OSC32KCTRL_RTCCTRL_RTCSEL_OSC1K , CLOCK_MCHP_RTC_SRC_OSC32K = OSC32KCTRL_RTCCTRL_RTCSEL_OSC32K , CLOCK_MCHP_RTC_SRC_XOSC1K = OSC32KCTRL_RTCCTRL_RTCSEL_XOSC1K , CLOCK_MCHP_RTC_SRC_XOSC32K = OSC32KCTRL_RTCCTRL_RTCSEL_XOSC32K }
```

相关声明：[clock_mchp_rtc_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga2b83aa5b88c064d44d3a0ef7661a15cf)、[CLOCK_MCHP_RTC_SRC_ULP1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfafaa5cfa19e470035ad1cec308aa63f7b)、[CLOCK_MCHP_RTC_SRC_ULP32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfa9095a4473e6e218ea0d2715695ecb2ff)、[CLOCK_MCHP_RTC_SRC_OSC1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfad5e72f091a71486e117cdea5b8381dff)、[CLOCK_MCHP_RTC_SRC_OSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfaa377b029b64d15627a7bee121ffc6050)、[CLOCK_MCHP_RTC_SRC_XOSC1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfae738ec040a54d0b171192d122abdd332)、[CLOCK_MCHP_RTC_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296)。

实时时钟（RTC）的源时钟（source clocks）。

<a id="r_ga073dab68c78edce3985eb201a039a989"></a>

```c
enum clock_mchp_gclk_src_clock { CLOCK_MCHP_GCLK_SRC_XOSC , CLOCK_MCHP_GCLK_SRC_GCLKPIN , CLOCK_MCHP_GCLK_SRC_GCLKGEN1 , CLOCK_MCHP_GCLK_SRC_OSCULP32K , CLOCK_MCHP_GCLK_SRC_OSC32K , CLOCK_MCHP_GCLK_SRC_XOSC32K , CLOCK_MCHP_GCLK_SRC_OSC48M , CLOCK_MCHP_GCLK_SRC_FDPLL , CLOCK_MCHP_GCLK_SRC_MAX = CLOCK_MCHP_GCLK_SRC_FDPLL }
```

相关声明：[clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga073dab68c78edce3985eb201a039a989)、[CLOCK_MCHP_GCLK_SRC_XOSC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a002e232f09f2da92b359ecd1543465d0)、[CLOCK_MCHP_GCLK_SRC_GCLKPIN](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef)、[CLOCK_MCHP_GCLK_SRC_GCLKGEN1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9)、[CLOCK_MCHP_GCLK_SRC_OSCULP32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6)、[CLOCK_MCHP_GCLK_SRC_OSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a26b8d25a8d166e0b8e79c77312897145)、[CLOCK_MCHP_GCLK_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380)、[CLOCK_MCHP_GCLK_SRC_OSC48M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a198b4b6273b991b0795e574036b3e177)、[CLOCK_MCHP_GCLK_SRC_FDPLL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a7ae946790cdbcec68bb8f7e8b35cd9fe)、[CLOCK_MCHP_GCLK_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768)。

通用时钟（GCLK）发生器的源时钟。

<a id="r_gaab34442b0d6c171691ae299675542777"></a>

```c
enum clock_mchp_gclkgen { CLOCK_MCHP_GCLKGEN_GEN0 , CLOCK_MCHP_GCLKGEN_GEN1 , CLOCK_MCHP_GCLKGEN_GEN2 , CLOCK_MCHP_GCLKGEN_GEN3 , CLOCK_MCHP_GCLKGEN_GEN4 , CLOCK_MCHP_GCLKGEN_GEN5 , CLOCK_MCHP_GCLKGEN_GEN6 , CLOCK_MCHP_GCLKGEN_GEN7 , CLOCK_MCHP_GCLKGEN_GEN8 }
```

相关声明：[clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gaab34442b0d6c171691ae299675542777)、[CLOCK_MCHP_GCLKGEN_GEN0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f)、[CLOCK_MCHP_GCLKGEN_GEN1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424)、[CLOCK_MCHP_GCLKGEN_GEN2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe)、[CLOCK_MCHP_GCLKGEN_GEN3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08)、[CLOCK_MCHP_GCLKGEN_GEN4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a69bd2c6d8f016e8ecdfd07fba7268dcc)、[CLOCK_MCHP_GCLKGEN_GEN5](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a20bf106031eb19f25b8e3b1250033088)、[CLOCK_MCHP_GCLKGEN_GEN6](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a9cbc78f597c2930b36280c59164e12ae)、[CLOCK_MCHP_GCLKGEN_GEN7](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a71ead69f87ccd57496b0467a6264d411)、[CLOCK_MCHP_GCLKGEN_GEN8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777aff9b0bedc5de2cfe3259df2910ab55f9)。

通用时钟（GCLK）发生器编号。

<a id="r_ga5835567db8d16c4eeb7a03b843ac6254"></a>

```c
enum clock_mchp_mclk_cpu_div { CLOCK_MCHP_MCLK_CPU_DIV_1 = 1 , CLOCK_MCHP_MCLK_CPU_DIV_2 = 2 , CLOCK_MCHP_MCLK_CPU_DIV_4 = 4 , CLOCK_MCHP_MCLK_CPU_DIV_8 = 8 , CLOCK_MCHP_MCLK_CPU_DIV_16 = 16 , CLOCK_MCHP_MCLK_CPU_DIV_32 = 32 , CLOCK_MCHP_MCLK_CPU_DIV_64 = 64 , CLOCK_MCHP_MCLK_CPU_DIV_128 = 128 }
```

相关声明：[clock_mchp_mclk_cpu_div](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga5835567db8d16c4eeb7a03b843ac6254)、[CLOCK_MCHP_MCLK_CPU_DIV_1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254a9f893cbec63df56227f17098ddf70074)、[CLOCK_MCHP_MCLK_CPU_DIV_2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254ac52aba85d20e21bd3135cc46e467dbfc)、[CLOCK_MCHP_MCLK_CPU_DIV_4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254ad251e58f232eaa9d45cce47e600b506f)、[CLOCK_MCHP_MCLK_CPU_DIV_8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254ace4fa9213f609c27198c75f17b0f7beb)、[CLOCK_MCHP_MCLK_CPU_DIV_16](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254ae11a4d93aaafcfaeed5a7cc6e0a1de89)、[CLOCK_MCHP_MCLK_CPU_DIV_32](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254ab071663992b6be65b6f77442239d3157)、[CLOCK_MCHP_MCLK_CPU_DIV_64](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254a688a2dbe64b6a818ab84f26cc983b3f0)、[CLOCK_MCHP_MCLK_CPU_DIV_128](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254aefa35c60f9274b62c0b829c1c24a571b)。

CPU 的 MCLK 预分频器分频比。


## 30.4\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/clock/mchp_pic32cm_jh_clock.h](../api_source_transport_clock_reference/P019_mchp_pic32cm_jh_clock.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P492_mchp_clock_pic32cm_jh.h_源码浏览.md)
- [clock_mchp_subsys_xosc_config](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md)
- [clock_mchp_subsys_osc48m_config](../clock_cmsis_model_reference/P017_clock_mchp_subsys_osc48m_config_结构体.md)
- [clock_mchp_subsys_fdpll_config](../clock_cmsis_model_reference/P012_clock_mchp_subsys_fdpll_config_结构体.md)
- [clock_mchp_subsys_rtc_config](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md)
- [clock_mchp_subsys_xosc32k_config](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md)
- [clock_mchp_subsys_osc32k_config](../clock_cmsis_model_reference/P016_clock_mchp_subsys_osc32k_config_结构体.md)
- [clock_mchp_subsys_gclkgen_config](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md)
- [clock_mchp_subsys_gclkperiph_config](../clock_cmsis_model_reference/P014_clock_mchp_subsys_gclkperiph_config_结构体.md)
- [clock_mchp_subsys_mclkcpu_config](../clock_cmsis_model_reference/P015_clock_mchp_subsys_mclkcpu_config_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [clock_mchp_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga9b6955116dae7fa53c8dad373a1ef9c9)
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
- [clock_mchp_rtc_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga2b83aa5b88c064d44d3a0ef7661a15cf)
- [CLOCK_MCHP_RTC_SRC_ULP1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfafaa5cfa19e470035ad1cec308aa63f7b)
- [CLOCK_MCHP_RTC_SRC_ULP32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfa9095a4473e6e218ea0d2715695ecb2ff)
- [CLOCK_MCHP_RTC_SRC_OSC1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfad5e72f091a71486e117cdea5b8381dff)
- [CLOCK_MCHP_RTC_SRC_OSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfaa377b029b64d15627a7bee121ffc6050)
- [CLOCK_MCHP_RTC_SRC_XOSC1K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfae738ec040a54d0b171192d122abdd332)
- [CLOCK_MCHP_RTC_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296)
- [clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga073dab68c78edce3985eb201a039a989)
- [CLOCK_MCHP_GCLK_SRC_XOSC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a002e232f09f2da92b359ecd1543465d0)
- [CLOCK_MCHP_GCLK_SRC_GCLKPIN](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef)
- [CLOCK_MCHP_GCLK_SRC_GCLKGEN1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9)
- [CLOCK_MCHP_GCLK_SRC_OSCULP32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6)
- [CLOCK_MCHP_GCLK_SRC_OSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a26b8d25a8d166e0b8e79c77312897145)
- [CLOCK_MCHP_GCLK_SRC_XOSC32K](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380)
- [CLOCK_MCHP_GCLK_SRC_OSC48M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a198b4b6273b991b0795e574036b3e177)
- [CLOCK_MCHP_GCLK_SRC_FDPLL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989a7ae946790cdbcec68bb8f7e8b35cd9fe)
- [CLOCK_MCHP_GCLK_SRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768)
- [clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gaab34442b0d6c171691ae299675542777)
- [CLOCK_MCHP_GCLKGEN_GEN0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f)
- [CLOCK_MCHP_GCLKGEN_GEN1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424)
- [CLOCK_MCHP_GCLKGEN_GEN2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe)
- [CLOCK_MCHP_GCLKGEN_GEN3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08)
- [CLOCK_MCHP_GCLKGEN_GEN4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a69bd2c6d8f016e8ecdfd07fba7268dcc)
- [CLOCK_MCHP_GCLKGEN_GEN5](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a20bf106031eb19f25b8e3b1250033088)
- [CLOCK_MCHP_GCLKGEN_GEN6](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a9cbc78f597c2930b36280c59164e12ae)
- [CLOCK_MCHP_GCLKGEN_GEN7](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777a71ead69f87ccd57496b0467a6264d411)
- [CLOCK_MCHP_GCLKGEN_GEN8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ggaab34442b0d6c171691ae299675542777aff9b0bedc5de2cfe3259df2910ab55f9)
- [clock_mchp_mclk_cpu_div](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga5835567db8d16c4eeb7a03b843ac6254)
- [CLOCK_MCHP_MCLK_CPU_DIV_1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254a9f893cbec63df56227f17098ddf70074)
- [CLOCK_MCHP_MCLK_CPU_DIV_2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254ac52aba85d20e21bd3135cc46e467dbfc)
- [CLOCK_MCHP_MCLK_CPU_DIV_4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254ad251e58f232eaa9d45cce47e600b506f)
- [CLOCK_MCHP_MCLK_CPU_DIV_8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254ace4fa9213f609c27198c75f17b0f7beb)
- [CLOCK_MCHP_MCLK_CPU_DIV_16](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254ae11a4d93aaafcfaeed5a7cc6e0a1de89)
- [CLOCK_MCHP_MCLK_CPU_DIV_32](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254ab071663992b6be65b6f77442239d3157)
- [CLOCK_MCHP_MCLK_CPU_DIV_64](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254a688a2dbe64b6a818ab84f26cc983b3f0)
- [CLOCK_MCHP_MCLK_CPU_DIV_128](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#gga5835567db8d16c4eeb7a03b843ac6254aefa35c60f9274b62c0b829c1c24a571b)

<a id="header-details"></a>

---

[上一章](P029_zephyr__dt-bindings__interrupt-controller__mchp-xec-ecia.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P031_zephyr__drivers__clock_control__mchp_clock_pic32cz_ca.h_文件参考.md)
