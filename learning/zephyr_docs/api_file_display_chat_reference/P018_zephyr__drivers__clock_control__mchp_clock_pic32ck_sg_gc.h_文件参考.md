---
id: learning.zephyr-docs.api-file-display-chat-reference.page-18
title: zephyr__drivers__clock_control__mchp_clock_pic32ck_sg_gc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_drivers\_\_clock\_control\_\_mchp\_clock\_pic32ck\_sg\_gc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip pic32ck_sg_gc系列的时钟控制（Clock Control）头文件。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/clock/mchp_pic32ck_sg_gc_clock.h>
```

查看此文件的源码。

Microchip pic32ck_sg_gc 系列时钟控制头文件（Clock Control Header File）。本文件提供 pic32ck_sg_gc 系列的时钟驱动接口定义（Clock Driver Interface Definitions）及结构体。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

<a id="r_clock_5Fmchp_5Fsubsys_5Fxosc_5Fconfig"></a>

```c
struct clock_mchp_subsys_xosc_config
```

相关声明：[clock_mchp_subsys_xosc_config](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md)。

外部晶体振荡器（External Crystal Oscillator）配置结构体。

<a id="r_clock_5Fmchp_5Fsubsys_5Fdfll48m_5Fconfig"></a>

```c
struct clock_mchp_subsys_dfll48m_config
```

相关声明：[clock_mchp_subsys_dfll48m_config](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md)。

48 MHz 数字锁频环（Digital Frequency-Locked Loop，DFLL）配置结构体。

<a id="r_clock_5Fmchp_5Fsubsys_5Fpll_5Fconfig"></a>

```c
struct clock_mchp_subsys_pll_config
```

相关声明：[clock_mchp_subsys_pll_config](../clock_cmsis_model_reference/P019_clock_mchp_subsys_pll_config_结构体.md)。

锁相环（Phase-Locked Loop，PLL）配置结构体。

<a id="r_clock_5Fmchp_5Fsubsys_5Fpll_5Fout_5Fconfig"></a>

```c
struct clock_mchp_subsys_pll_out_config
```

相关声明：[clock_mchp_subsys_pll_out_config](../clock_cmsis_model_reference/P020_clock_mchp_subsys_pll_out_config_结构体.md)。

PLL 输出配置结构体（PLL Output Configuration Structure）。

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

## 18.2\_类型定义（Typedefs）

<a id="r_a9b6955116dae7fa53c8dad373a1ef9c9"></a>

```c
typedef uint32_t * clock_mchp_rate_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[clock_mchp_rate_t](#a9b6955116dae7fa53c8dad373a1ef9c9)。

时钟频率数据类型（clock rate datatype）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 18.3\_枚举（Enumerations）

<a id="r_aab34442b0d6c171691ae299675542777"></a>

```c
enum clock_mchp_gclkgen { CLOCK_MCHP_GCLKGEN_GEN0 , CLOCK_MCHP_GCLKGEN_GEN1 , CLOCK_MCHP_GCLKGEN_GEN2 , CLOCK_MCHP_GCLKGEN_GEN3 , CLOCK_MCHP_GCLKGEN_GEN4 , CLOCK_MCHP_GCLKGEN_GEN5 , CLOCK_MCHP_GCLKGEN_GEN6 , CLOCK_MCHP_GCLKGEN_GEN7 , CLOCK_MCHP_GCLKGEN_GEN8 , CLOCK_MCHP_GCLKGEN_GEN9 , CLOCK_MCHP_GCLKGEN_GEN10 , CLOCK_MCHP_GCLKGEN_GEN11 }
```

相关声明：[clock_mchp_gclkgen](#aab34442b0d6c171691ae299675542777)、[CLOCK_MCHP_GCLKGEN_GEN0](#aab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f)、[CLOCK_MCHP_GCLKGEN_GEN1](#aab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424)、[CLOCK_MCHP_GCLKGEN_GEN2](#aab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe)、[CLOCK_MCHP_GCLKGEN_GEN3](#aab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08)、[CLOCK_MCHP_GCLKGEN_GEN4](#aab34442b0d6c171691ae299675542777a69bd2c6d8f016e8ecdfd07fba7268dcc)、[CLOCK_MCHP_GCLKGEN_GEN5](#aab34442b0d6c171691ae299675542777a20bf106031eb19f25b8e3b1250033088)、[CLOCK_MCHP_GCLKGEN_GEN6](#aab34442b0d6c171691ae299675542777a9cbc78f597c2930b36280c59164e12ae)、[CLOCK_MCHP_GCLKGEN_GEN7](#aab34442b0d6c171691ae299675542777a71ead69f87ccd57496b0467a6264d411)、[CLOCK_MCHP_GCLKGEN_GEN8](#aab34442b0d6c171691ae299675542777aff9b0bedc5de2cfe3259df2910ab55f9)、[CLOCK_MCHP_GCLKGEN_GEN9](#aab34442b0d6c171691ae299675542777a96de017372252af6f1bcab2cdb32c2f1)、[CLOCK_MCHP_GCLKGEN_GEN10](#aab34442b0d6c171691ae299675542777a63f142bb2401a057b9ba7b4a8f60eb60)、[CLOCK_MCHP_GCLKGEN_GEN11](#aab34442b0d6c171691ae299675542777a905cb4bab8f6bb50f690de6a9e970695)。

通用时钟（GCLK）发生器编号。

<a id="r_a1f0a363c4b5d2260d614bc0b2e19555e"></a>

```c
enum clock_mchp_pll_src_clock { CLOCK_MCHP_PLL_SRC_GCLK0 , CLOCK_MCHP_PLL_SRC_GCLK1 , CLOCK_MCHP_PLL_SRC_GCLK2 , CLOCK_MCHP_PLL_SRC_GCLK3 , CLOCK_MCHP_PLL_SRC_GCLK4 , CLOCK_MCHP_PLL_SRC_GCLK5 , CLOCK_MCHP_PLL_SRC_GCLK6 , CLOCK_MCHP_PLL_SRC_GCLK7 , CLOCK_MCHP_PLL_SRC_GCLK8 , CLOCK_MCHP_PLL_SRC_GCLK9 , CLOCK_MCHP_PLL_SRC_GCLK10 , CLOCK_MCHP_PLL_SRC_GCLK11 , CLOCK_MCHP_PLL_SRC_XOSC , CLOCK_MCHP_PLL_SRC_DFLL48M , CLOCK_MCHP_PLL_SRC_MAX = CLOCK_MCHP_PLL_SRC_DFLL48M }
```

相关声明：[clock_mchp_pll_src_clock](#a1f0a363c4b5d2260d614bc0b2e19555e)、[CLOCK_MCHP_PLL_SRC_GCLK0](#a1f0a363c4b5d2260d614bc0b2e19555eaef24a9e72fe2d4f1518d04b081bfb344)、[CLOCK_MCHP_PLL_SRC_GCLK1](#a1f0a363c4b5d2260d614bc0b2e19555eae6ea73001396449cab6b5ae14adce995)、[CLOCK_MCHP_PLL_SRC_GCLK2](#a1f0a363c4b5d2260d614bc0b2e19555eac158d3d2881be2f4599a3fa17e10c7e4)、[CLOCK_MCHP_PLL_SRC_GCLK3](#a1f0a363c4b5d2260d614bc0b2e19555eab27d86592af60943287f2eed0079a538)、[CLOCK_MCHP_PLL_SRC_GCLK4](#a1f0a363c4b5d2260d614bc0b2e19555ea24133131a7e379620f4cccc8c272d3d2)、[CLOCK_MCHP_PLL_SRC_GCLK5](#a1f0a363c4b5d2260d614bc0b2e19555ea7f589a8c783ca935e3a3bec4e00fe78a)、[CLOCK_MCHP_PLL_SRC_GCLK6](#a1f0a363c4b5d2260d614bc0b2e19555ea47742caeb6c36cfbab2ea52b76375843)、[CLOCK_MCHP_PLL_SRC_GCLK7](#a1f0a363c4b5d2260d614bc0b2e19555ead09414b3eb59c8c3192b06be62ceb0e5)、[CLOCK_MCHP_PLL_SRC_GCLK8](#a1f0a363c4b5d2260d614bc0b2e19555ea8738be13a05d1f2e738b32c41446d7b9)、[CLOCK_MCHP_PLL_SRC_GCLK9](#a1f0a363c4b5d2260d614bc0b2e19555eae253d07c8f5363965d92dbd067d634be)、[CLOCK_MCHP_PLL_SRC_GCLK10](#a1f0a363c4b5d2260d614bc0b2e19555ea8b04fdb20116b7fe6e1c0f76c628db77)、[CLOCK_MCHP_PLL_SRC_GCLK11](#a1f0a363c4b5d2260d614bc0b2e19555eacbcf8ac169420753c80c1b12ad10e517)、[CLOCK_MCHP_PLL_SRC_XOSC](#a1f0a363c4b5d2260d614bc0b2e19555eaf7bd65f6bc9f42452f59f60623d50881)、[CLOCK_MCHP_PLL_SRC_DFLL48M](#a1f0a363c4b5d2260d614bc0b2e19555ea855942173475ae101281766a4fda2e5f)、[CLOCK_MCHP_PLL_SRC_MAX](#a1f0a363c4b5d2260d614bc0b2e19555ea097b57f49a9ed54a8e68a88c45af8540)。

锁相环源时钟（PLL Source Clocks）。

<a id="r_a2b83aa5b88c064d44d3a0ef7661a15cf"></a>

```c
enum clock_mchp_rtc_src_clock { CLOCK_MCHP_RTC_SRC_OSCULP1K = OSC32KCTRL_CLKSELCTRL_RTCSEL_ULP1K_Val , CLOCK_MCHP_RTC_SRC_OSCULP32K = OSC32KCTRL_CLKSELCTRL_RTCSEL_ULP32K_Val , CLOCK_MCHP_RTC_SRC_XOSC1K = OSC32KCTRL_CLKSELCTRL_RTCSEL_XOSC1K_Val , CLOCK_MCHP_RTC_SRC_XOSC32K = OSC32KCTRL_CLKSELCTRL_RTCSEL_XOSC32K_Val }
```

相关声明：[clock_mchp_rtc_src_clock](#a2b83aa5b88c064d44d3a0ef7661a15cf)、[CLOCK_MCHP_RTC_SRC_OSCULP1K](#a2b83aa5b88c064d44d3a0ef7661a15cfa3523c19ffb12654b4d1e663d6ef096ec)、[CLOCK_MCHP_RTC_SRC_OSCULP32K](#a2b83aa5b88c064d44d3a0ef7661a15cfa4eeb4b4c5f682aa3c2c09fb7a321a68d)、[CLOCK_MCHP_RTC_SRC_XOSC1K](#a2b83aa5b88c064d44d3a0ef7661a15cfae738ec040a54d0b171192d122abdd332)、[CLOCK_MCHP_RTC_SRC_XOSC32K](#a2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296)。

实时时钟（RTC）的源时钟（source clocks）。

<a id="r_a073dab68c78edce3985eb201a039a989"></a>

```c
enum clock_mchp_gclk_src_clock { CLOCK_MCHP_GCLK_SRC_XOSC , CLOCK_MCHP_GCLK_SRC_GCLKPIN , CLOCK_MCHP_GCLK_SRC_GCLKGEN1 , CLOCK_MCHP_GCLK_SRC_OSCULP32K , CLOCK_MCHP_GCLK_SRC_XOSC32K , CLOCK_MCHP_GCLK_SRC_DFLL48M , CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT0 , CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT1 , CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT2 , CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT3 , CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT4 , CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT5 , CLOCK_MCHP_GCLK_SRC_MAX = CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT5 }
```

相关声明：[clock_mchp_gclk_src_clock](#a073dab68c78edce3985eb201a039a989)、[CLOCK_MCHP_GCLK_SRC_XOSC](#a073dab68c78edce3985eb201a039a989a002e232f09f2da92b359ecd1543465d0)、[CLOCK_MCHP_GCLK_SRC_GCLKPIN](#a073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef)、[CLOCK_MCHP_GCLK_SRC_GCLKGEN1](#a073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9)、[CLOCK_MCHP_GCLK_SRC_OSCULP32K](#a073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6)、[CLOCK_MCHP_GCLK_SRC_XOSC32K](#a073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380)、[CLOCK_MCHP_GCLK_SRC_DFLL48M](#a073dab68c78edce3985eb201a039a989a647395dd08022519b13e0270f44943d6)、[CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT0](#a073dab68c78edce3985eb201a039a989ad3453cbd92dca5da39da54a267e955b5)、[CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT1](#a073dab68c78edce3985eb201a039a989a0242a7512bbb16e7d97113c66c26ea73)、[CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT2](#a073dab68c78edce3985eb201a039a989aeb2a16ab5ddfe55eab48831761c83aca)、[CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT3](#a073dab68c78edce3985eb201a039a989a956353351be40288ebbc3c7c5d3480c9)、[CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT4](#a073dab68c78edce3985eb201a039a989aa906d7b53c240c7b358a33069e26bad0)、[CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT5](#a073dab68c78edce3985eb201a039a989a9493982be1abdb53d65963d19fc17ab8)、[CLOCK_MCHP_GCLK_SRC_MAX](#a073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768)。

GCLK 发生器的源时钟（source clocks）。

<a id="r_a5835567db8d16c4eeb7a03b843ac6254"></a>

```c
enum clock_mchp_mclk_cpu_div { CLOCK_MCHP_MCLK_CPU_DIV_1 = 1 , CLOCK_MCHP_MCLK_CPU_DIV_2 = 2 , CLOCK_MCHP_MCLK_CPU_DIV_4 = 4 , CLOCK_MCHP_MCLK_CPU_DIV_8 = 8 , CLOCK_MCHP_MCLK_CPU_DIV_16 = 16 , CLOCK_MCHP_MCLK_CPU_DIV_32 = 32 , CLOCK_MCHP_MCLK_CPU_DIV_64 = 64 , CLOCK_MCHP_MCLK_CPU_DIV_128 = 128 }
```

相关声明：[clock_mchp_mclk_cpu_div](#a5835567db8d16c4eeb7a03b843ac6254)、[CLOCK_MCHP_MCLK_CPU_DIV_1](#a5835567db8d16c4eeb7a03b843ac6254a9f893cbec63df56227f17098ddf70074)、[CLOCK_MCHP_MCLK_CPU_DIV_2](#a5835567db8d16c4eeb7a03b843ac6254ac52aba85d20e21bd3135cc46e467dbfc)、[CLOCK_MCHP_MCLK_CPU_DIV_4](#a5835567db8d16c4eeb7a03b843ac6254ad251e58f232eaa9d45cce47e600b506f)、[CLOCK_MCHP_MCLK_CPU_DIV_8](#a5835567db8d16c4eeb7a03b843ac6254ace4fa9213f609c27198c75f17b0f7beb)、[CLOCK_MCHP_MCLK_CPU_DIV_16](#a5835567db8d16c4eeb7a03b843ac6254ae11a4d93aaafcfaeed5a7cc6e0a1de89)、[CLOCK_MCHP_MCLK_CPU_DIV_32](#a5835567db8d16c4eeb7a03b843ac6254ab071663992b6be65b6f77442239d3157)、[CLOCK_MCHP_MCLK_CPU_DIV_64](#a5835567db8d16c4eeb7a03b843ac6254a688a2dbe64b6a818ab84f26cc983b3f0)、[CLOCK_MCHP_MCLK_CPU_DIV_128](#a5835567db8d16c4eeb7a03b843ac6254aefa35c60f9274b62c0b829c1c24a571b)。

CPU 的 MCLK 预分频器（Prescaler）分频比。

## 18.4\_详细说明（Detailed Documentation）

<a id="a9b6955116dae7fa53c8dad373a1ef9c9"></a>

### `clock_mchp_rate_t`

```c
typedef uint32_t* clock_mchp_rate_t
```

时钟频率数据类型（clock rate datatype）。

用于设置时钟速率（Clock Rate）。

<a id="a073dab68c78edce3985eb201a039a989"></a>

### `clock_mchp_gclk_src_clock`

```c
enum clock_mchp_gclk_src_clock
```

GCLK 发生器的源时钟（source clocks）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_MCHP_GCLK_SRC_XOSC` | 外部晶体振荡器（External Crystal Oscillator，XOSC）。 |
| `CLOCK_MCHP_GCLK_SRC_GCLKPIN` | 来自 Gclk I/O 引脚的外部时钟输入（External Clock Input）。 |
| `CLOCK_MCHP_GCLK_SRC_GCLKGEN1` | 通用时钟发生器 1（Generic Clock Generator 1）的输出。 |
| `CLOCK_MCHP_GCLK_SRC_OSCULP32K` | 内部超低功耗（Ultra-low-power）32 kHz 振荡器。 |
| `CLOCK_MCHP_GCLK_SRC_XOSC32K` | 外部 32.768 kHz 晶体振荡器（Crystal Oscillator）。 |
| `CLOCK_MCHP_GCLK_SRC_DFLL48M` | 内部 48 MHz 数字锁频环（DFLL）时钟。 |
| `CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT0` | PLL0 输出时钟（Output Clock）0。 |
| `CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT1` | PLL0 输出时钟（Output Clock）1。 |
| `CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT2` | PLL0 输出时钟（Output Clock）2。 |
| `CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT3` | PLL0 输出时钟（Output Clock）3。 |
| `CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT4` | PLL0 输出时钟（Output Clock）4。 |
| `CLOCK_MCHP_GCLK_SRC_PLL0_CLKOUT5` | PLL0 输出时钟（Output Clock）5。 |
| `CLOCK_MCHP_GCLK_SRC_MAX` | 最大的有效 Gclk 时钟源（Gclk Source）值。 |

<a id="aab34442b0d6c171691ae299675542777"></a>

### `clock_mchp_gclkgen`

```c
enum clock_mchp_gclkgen
```

通用时钟（GCLK）发生器编号。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_MCHP_GCLKGEN_GEN0` | 通用时钟发生器（Gclk Generator）0。 |
| `CLOCK_MCHP_GCLKGEN_GEN1` | 通用时钟发生器（Gclk Generator）1。 |
| `CLOCK_MCHP_GCLKGEN_GEN2` | 通用时钟发生器（Gclk Generator）2。 |
| `CLOCK_MCHP_GCLKGEN_GEN3` | 通用时钟发生器（Gclk Generator）3。 |
| `CLOCK_MCHP_GCLKGEN_GEN4` | 通用时钟发生器（Gclk Generator）4。 |
| `CLOCK_MCHP_GCLKGEN_GEN5` | 通用时钟发生器（Gclk Generator）5。 |
| `CLOCK_MCHP_GCLKGEN_GEN6` | 通用时钟发生器（Gclk Generator）6。 |
| `CLOCK_MCHP_GCLKGEN_GEN7` | 通用时钟发生器（Gclk Generator）7。 |
| `CLOCK_MCHP_GCLKGEN_GEN8` | 通用时钟发生器（Gclk Generator）8。 |
| `CLOCK_MCHP_GCLKGEN_GEN9` | 通用时钟发生器（Gclk Generator）9。 |
| `CLOCK_MCHP_GCLKGEN_GEN10` | 通用时钟发生器（Gclk Generator）10。 |
| `CLOCK_MCHP_GCLKGEN_GEN11` | 通用时钟发生器（Gclk Generator）11。 |

<a id="a5835567db8d16c4eeb7a03b843ac6254"></a>

### `clock_mchp_mclk_cpu_div`

```c
enum clock_mchp_mclk_cpu_div
```

CPU 的 MCLK 预分频器（Prescaler）分频比。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_MCHP_MCLK_CPU_DIV_1` | 1 分频（Divide by 1），即不分频。 |
| `CLOCK_MCHP_MCLK_CPU_DIV_2` | 2 分频（Divide by 2）。 |
| `CLOCK_MCHP_MCLK_CPU_DIV_4` | 4 分频（Divide by 4）。 |
| `CLOCK_MCHP_MCLK_CPU_DIV_8` | 8 分频（Divide by 8）。 |
| `CLOCK_MCHP_MCLK_CPU_DIV_16` | 16 分频（Divide by 16）。 |
| `CLOCK_MCHP_MCLK_CPU_DIV_32` | 32 分频（Divide by 32）。 |
| `CLOCK_MCHP_MCLK_CPU_DIV_64` | 64 分频（Divide by 64）。 |
| `CLOCK_MCHP_MCLK_CPU_DIV_128` | 128 分频（Divide by 128）。 |

<a id="a1f0a363c4b5d2260d614bc0b2e19555e"></a>

### `clock_mchp_pll_src_clock`

```c
enum clock_mchp_pll_src_clock
```

锁相环源时钟（PLL Source Clocks）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_MCHP_PLL_SRC_GCLK0` | 通用时钟发生器（Gclk Generator）0。 |
| `CLOCK_MCHP_PLL_SRC_GCLK1` | 通用时钟发生器（Gclk Generator）1。 |
| `CLOCK_MCHP_PLL_SRC_GCLK2` | 通用时钟发生器（Gclk Generator）2。 |
| `CLOCK_MCHP_PLL_SRC_GCLK3` | 通用时钟发生器（Gclk Generator）3。 |
| `CLOCK_MCHP_PLL_SRC_GCLK4` | 通用时钟发生器（Gclk Generator）4。 |
| `CLOCK_MCHP_PLL_SRC_GCLK5` | 通用时钟发生器（Gclk Generator）5。 |
| `CLOCK_MCHP_PLL_SRC_GCLK6` | 通用时钟发生器（Gclk Generator）6。 |
| `CLOCK_MCHP_PLL_SRC_GCLK7` | 通用时钟发生器（Gclk Generator）7。 |
| `CLOCK_MCHP_PLL_SRC_GCLK8` | 通用时钟发生器（Gclk Generator）8。 |
| `CLOCK_MCHP_PLL_SRC_GCLK9` | 通用时钟发生器（Gclk Generator）9。 |
| `CLOCK_MCHP_PLL_SRC_GCLK10` | 通用时钟发生器（Gclk Generator）10。 |
| `CLOCK_MCHP_PLL_SRC_GCLK11` | 通用时钟发生器（Gclk Generator）11。 |
| `CLOCK_MCHP_PLL_SRC_XOSC` | 外部晶体振荡器（External Crystal Oscillator，XOSC）。 |
| `CLOCK_MCHP_PLL_SRC_DFLL48M` | 内部 48 MHz 数字锁频环（DFLL）时钟。 |
| `CLOCK_MCHP_PLL_SRC_MAX` | 最大的有效锁相环源时钟（PLL Source Clock）值。 |

<a id="a2b83aa5b88c064d44d3a0ef7661a15cf"></a>

### `clock_mchp_rtc_src_clock`

```c
enum clock_mchp_rtc_src_clock
```

实时时钟（RTC）的源时钟（source clocks）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_MCHP_RTC_SRC_OSCULP1K` | 内部超低功耗（Ultra-low-power）1 kHz 振荡器。 |
| `CLOCK_MCHP_RTC_SRC_OSCULP32K` | 内部超低功耗（Ultra-low-power）32 kHz 振荡器。 |
| `CLOCK_MCHP_RTC_SRC_XOSC1K` | 分频至 1 kHz 的外部晶体振荡器（External Crystal Oscillator）。 |
| `CLOCK_MCHP_RTC_SRC_XOSC32K` | 外部 32.768 kHz 晶体振荡器（Crystal Oscillator）。 |


## 18.5\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/clock/mchp_pic32ck_sg_gc_clock.h](../api_source_reference/P501_mchp_pic32ck_sg_gc_clock.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P491_mchp_clock_pic32ck_sg_gc.h_源码浏览.md)
- [clock_mchp_subsys_xosc_config](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md)
- [clock_mchp_subsys_dfll48m_config](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md)
- [clock_mchp_subsys_pll_config](../clock_cmsis_model_reference/P019_clock_mchp_subsys_pll_config_结构体.md)
- [clock_mchp_subsys_pll_out_config](../clock_cmsis_model_reference/P020_clock_mchp_subsys_pll_out_config_结构体.md)
- [clock_mchp_subsys_rtc_config](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md)
- [clock_mchp_subsys_xosc32k_config](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md)
- [clock_mchp_subsys_gclkgen_config](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md)
- [clock_mchp_subsys_gclkperiph_config](../clock_cmsis_model_reference/P014_clock_mchp_subsys_gclkperiph_config_结构体.md)
- [clock_mchp_subsys_mclkcpu_config](../clock_cmsis_model_reference/P015_clock_mchp_subsys_mclkcpu_config_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a073dab68c78edce3985eb201a039a989a002e232f09f2da92b359ecd1543465d0"></a>
<a id="a073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef"></a>
<a id="a073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9"></a>
<a id="a073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6"></a>
<a id="a073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380"></a>
<a id="a073dab68c78edce3985eb201a039a989a647395dd08022519b13e0270f44943d6"></a>
<a id="a073dab68c78edce3985eb201a039a989ad3453cbd92dca5da39da54a267e955b5"></a>
<a id="a073dab68c78edce3985eb201a039a989a0242a7512bbb16e7d97113c66c26ea73"></a>
<a id="a073dab68c78edce3985eb201a039a989aeb2a16ab5ddfe55eab48831761c83aca"></a>
<a id="a073dab68c78edce3985eb201a039a989a956353351be40288ebbc3c7c5d3480c9"></a>
<a id="a073dab68c78edce3985eb201a039a989aa906d7b53c240c7b358a33069e26bad0"></a>
<a id="a073dab68c78edce3985eb201a039a989a9493982be1abdb53d65963d19fc17ab8"></a>
<a id="a073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768"></a>
<a id="aab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f"></a>
<a id="aab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424"></a>
<a id="aab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe"></a>
<a id="aab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08"></a>
<a id="aab34442b0d6c171691ae299675542777a69bd2c6d8f016e8ecdfd07fba7268dcc"></a>
<a id="aab34442b0d6c171691ae299675542777a20bf106031eb19f25b8e3b1250033088"></a>
<a id="aab34442b0d6c171691ae299675542777a9cbc78f597c2930b36280c59164e12ae"></a>
<a id="aab34442b0d6c171691ae299675542777a71ead69f87ccd57496b0467a6264d411"></a>
<a id="aab34442b0d6c171691ae299675542777aff9b0bedc5de2cfe3259df2910ab55f9"></a>
<a id="aab34442b0d6c171691ae299675542777a96de017372252af6f1bcab2cdb32c2f1"></a>
<a id="aab34442b0d6c171691ae299675542777a63f142bb2401a057b9ba7b4a8f60eb60"></a>
<a id="aab34442b0d6c171691ae299675542777a905cb4bab8f6bb50f690de6a9e970695"></a>
<a id="a5835567db8d16c4eeb7a03b843ac6254a9f893cbec63df56227f17098ddf70074"></a>
<a id="a5835567db8d16c4eeb7a03b843ac6254ac52aba85d20e21bd3135cc46e467dbfc"></a>
<a id="a5835567db8d16c4eeb7a03b843ac6254ad251e58f232eaa9d45cce47e600b506f"></a>
<a id="a5835567db8d16c4eeb7a03b843ac6254ace4fa9213f609c27198c75f17b0f7beb"></a>
<a id="a5835567db8d16c4eeb7a03b843ac6254ae11a4d93aaafcfaeed5a7cc6e0a1de89"></a>
<a id="a5835567db8d16c4eeb7a03b843ac6254ab071663992b6be65b6f77442239d3157"></a>
<a id="a5835567db8d16c4eeb7a03b843ac6254a688a2dbe64b6a818ab84f26cc983b3f0"></a>
<a id="a5835567db8d16c4eeb7a03b843ac6254aefa35c60f9274b62c0b829c1c24a571b"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555eaef24a9e72fe2d4f1518d04b081bfb344"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555eae6ea73001396449cab6b5ae14adce995"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555eac158d3d2881be2f4599a3fa17e10c7e4"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555eab27d86592af60943287f2eed0079a538"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555ea24133131a7e379620f4cccc8c272d3d2"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555ea7f589a8c783ca935e3a3bec4e00fe78a"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555ea47742caeb6c36cfbab2ea52b76375843"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555ead09414b3eb59c8c3192b06be62ceb0e5"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555ea8738be13a05d1f2e738b32c41446d7b9"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555eae253d07c8f5363965d92dbd067d634be"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555ea8b04fdb20116b7fe6e1c0f76c628db77"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555eacbcf8ac169420753c80c1b12ad10e517"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555eaf7bd65f6bc9f42452f59f60623d50881"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555ea855942173475ae101281766a4fda2e5f"></a>
<a id="a1f0a363c4b5d2260d614bc0b2e19555ea097b57f49a9ed54a8e68a88c45af8540"></a>
<a id="a2b83aa5b88c064d44d3a0ef7661a15cfa3523c19ffb12654b4d1e663d6ef096ec"></a>
<a id="a2b83aa5b88c064d44d3a0ef7661a15cfa4eeb4b4c5f682aa3c2c09fb7a321a68d"></a>
<a id="a2b83aa5b88c064d44d3a0ef7661a15cfae738ec040a54d0b171192d122abdd332"></a>
<a id="a2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296"></a>

---

[上一章](P017_zephyr__lorawan__lorawan.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__clock_control__mchp_clock_pic32cm_sg_gc.h_文件参考.md)
