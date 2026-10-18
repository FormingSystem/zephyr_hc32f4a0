---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-4
title: 微芯（Microchip）PIC32CZ CA
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_微芯（Microchip）PIC32CZ CA

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_mchp_5Fclock_5Fpic32cz_5Fca_2Eh"></a>

```c
file mchp_clock_pic32cz_ca.h
```

相关声明：[mchp_clock_pic32cz_ca.h](../api_file_management_reference/P031_zephyr__drivers__clock_control__mchp_clock_pic32cz_ca.h_文件参考.md)。

Microchip PIC32CZ CA系列的时钟控制（Clock Control）头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.2\_数据结构（Data Structures）

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

<a id="r_clock_5Fmchp_5Fsubsys_5Fdpll_5Fconfig"></a>

```c
struct clock_mchp_subsys_dpll_config
```

相关声明：[clock_mchp_subsys_dpll_config](../clock_cmsis_model_reference/P010_clock_mchp_subsys_dpll_config_结构体.md)。

数字锁相环（Digital Phase-Locked Loop，DPLL）配置结构体。

<a id="r_clock_5Fmchp_5Fsubsys_5Fdpll_5Fout_5Fconfig"></a>

```c
struct clock_mchp_subsys_dpll_out_config
```

相关声明：[clock_mchp_subsys_dpll_out_config](../clock_cmsis_model_reference/P011_clock_mchp_subsys_dpll_out_config_结构体.md)。

DPLL 输出配置结构体（DPLL Output Configuration Structure）。

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

## 4.3\_类型定义（Typedefs）

<a id="r_ga9b6955116dae7fa53c8dad373a1ef9c9"></a>

```c
typedef uint32_t * clock_mchp_rate_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[clock_mchp_rate_t](#ga9b6955116dae7fa53c8dad373a1ef9c9)。

时钟频率数据类型（clock rate datatype）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.4\_枚举（Enumerations）

<a id="r_gaab34442b0d6c171691ae299675542777"></a>

```c
enum clock_mchp_gclkgen { CLOCK_MCHP_GCLKGEN_GEN0 , CLOCK_MCHP_GCLKGEN_GEN1 , CLOCK_MCHP_GCLKGEN_GEN2 , CLOCK_MCHP_GCLKGEN_GEN3 , CLOCK_MCHP_GCLKGEN_GEN4 , CLOCK_MCHP_GCLKGEN_GEN5 , CLOCK_MCHP_GCLKGEN_GEN6 , CLOCK_MCHP_GCLKGEN_GEN7 , CLOCK_MCHP_GCLKGEN_GEN8 , CLOCK_MCHP_GCLKGEN_GEN9 , CLOCK_MCHP_GCLKGEN_GEN10 , CLOCK_MCHP_GCLKGEN_GEN11 , CLOCK_MCHP_GCLKGEN_GEN12 , CLOCK_MCHP_GCLKGEN_GEN13 , CLOCK_MCHP_GCLKGEN_GEN14 , CLOCK_MCHP_GCLKGEN_GEN15 }
```

相关声明：[clock_mchp_gclkgen](#gaab34442b0d6c171691ae299675542777)、[CLOCK_MCHP_GCLKGEN_GEN0](#ggaab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f)、[CLOCK_MCHP_GCLKGEN_GEN1](#ggaab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424)、[CLOCK_MCHP_GCLKGEN_GEN2](#ggaab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe)、[CLOCK_MCHP_GCLKGEN_GEN3](#ggaab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08)、[CLOCK_MCHP_GCLKGEN_GEN4](#ggaab34442b0d6c171691ae299675542777a69bd2c6d8f016e8ecdfd07fba7268dcc)、[CLOCK_MCHP_GCLKGEN_GEN5](#ggaab34442b0d6c171691ae299675542777a20bf106031eb19f25b8e3b1250033088)、[CLOCK_MCHP_GCLKGEN_GEN6](#ggaab34442b0d6c171691ae299675542777a9cbc78f597c2930b36280c59164e12ae)、[CLOCK_MCHP_GCLKGEN_GEN7](#ggaab34442b0d6c171691ae299675542777a71ead69f87ccd57496b0467a6264d411)、[CLOCK_MCHP_GCLKGEN_GEN8](#ggaab34442b0d6c171691ae299675542777aff9b0bedc5de2cfe3259df2910ab55f9)、[CLOCK_MCHP_GCLKGEN_GEN9](#ggaab34442b0d6c171691ae299675542777a96de017372252af6f1bcab2cdb32c2f1)、[CLOCK_MCHP_GCLKGEN_GEN10](#ggaab34442b0d6c171691ae299675542777a63f142bb2401a057b9ba7b4a8f60eb60)、[CLOCK_MCHP_GCLKGEN_GEN11](#ggaab34442b0d6c171691ae299675542777a905cb4bab8f6bb50f690de6a9e970695)、[CLOCK_MCHP_GCLKGEN_GEN12](#ggaab34442b0d6c171691ae299675542777a6ea9310c7eb41d72c82b4abff78b36f8)、[CLOCK_MCHP_GCLKGEN_GEN13](#ggaab34442b0d6c171691ae299675542777aaca57694ee279c5aa0b732bb9c7dcd19)、[CLOCK_MCHP_GCLKGEN_GEN14](#ggaab34442b0d6c171691ae299675542777ae33d3555ccda79c69de0fc110937cf23)、[CLOCK_MCHP_GCLKGEN_GEN15](#ggaab34442b0d6c171691ae299675542777a24e34e40f92b7cd41fa7d927097d6f25)。

通用时钟（GCLK）发生器编号。

<a id="r_gad4a3719300474b36067b86dad7611d33"></a>

```c
enum clock_mchp_dpll_src_clock { CLOCK_MCHP_DPLL_SRC_GCLK0 , CLOCK_MCHP_DPLL_SRC_GCLK1 , CLOCK_MCHP_DPLL_SRC_GCLK2 , CLOCK_MCHP_DPLL_SRC_GCLK3 , CLOCK_MCHP_DPLL_SRC_GCLK4 , CLOCK_MCHP_DPLL_SRC_GCLK5 , CLOCK_MCHP_DPLL_SRC_GCLK6 , CLOCK_MCHP_DPLL_SRC_GCLK7 , CLOCK_MCHP_DPLL_SRC_GCLK8 , CLOCK_MCHP_DPLL_SRC_GCLK9 , CLOCK_MCHP_DPLL_SRC_GCLK10 , CLOCK_MCHP_DPLL_SRC_GCLK11 , CLOCK_MCHP_DPLL_SRC_GCLK12 , CLOCK_MCHP_DPLL_SRC_GCLK13 , CLOCK_MCHP_DPLL_SRC_GCLK14 , CLOCK_MCHP_DPLL_SRC_GCLK15 , CLOCK_MCHP_DPLL_SRC_XOSC , CLOCK_MCHP_DPLL_SRC_DFLL48M , CLOCK_MCHP_DPLL_SRC_MAX }
```

相关声明：[clock_mchp_dpll_src_clock](#gad4a3719300474b36067b86dad7611d33)、[CLOCK_MCHP_DPLL_SRC_GCLK0](#ggad4a3719300474b36067b86dad7611d33ae3f23ab2c7a84a5c43fb8361b1ee1f83)、[CLOCK_MCHP_DPLL_SRC_GCLK1](#ggad4a3719300474b36067b86dad7611d33a75742e71b54b1bdefd0716085d47e496)、[CLOCK_MCHP_DPLL_SRC_GCLK2](#ggad4a3719300474b36067b86dad7611d33af5906d13a56a0e26da669e15b5454b63)、[CLOCK_MCHP_DPLL_SRC_GCLK3](#ggad4a3719300474b36067b86dad7611d33a394cfe9ab4e963417fc0787c160ec847)、[CLOCK_MCHP_DPLL_SRC_GCLK4](#ggad4a3719300474b36067b86dad7611d33afedc39675c6b63f46e36ed415ea04b27)、[CLOCK_MCHP_DPLL_SRC_GCLK5](#ggad4a3719300474b36067b86dad7611d33a34340db86e94450b72eae0d7ca0be283)、[CLOCK_MCHP_DPLL_SRC_GCLK6](#ggad4a3719300474b36067b86dad7611d33a183ebd7a615416cee57d7bdb0ce4d29b)、[CLOCK_MCHP_DPLL_SRC_GCLK7](#ggad4a3719300474b36067b86dad7611d33a4917fc8ee80c35ab78df854e2ce81958)、[CLOCK_MCHP_DPLL_SRC_GCLK8](#ggad4a3719300474b36067b86dad7611d33a5f67b9bf8fd7edbe90c4c22073ddc759)、[CLOCK_MCHP_DPLL_SRC_GCLK9](#ggad4a3719300474b36067b86dad7611d33aaf6ebe0c6f7370866388499a7a4037c2)、[CLOCK_MCHP_DPLL_SRC_GCLK10](#ggad4a3719300474b36067b86dad7611d33a666358ed4b1f3564a7b4ae8a0b54cb06)、[CLOCK_MCHP_DPLL_SRC_GCLK11](#ggad4a3719300474b36067b86dad7611d33abf6ced8f2a3eabadea96bdbf0b172b61)、[CLOCK_MCHP_DPLL_SRC_GCLK12](#ggad4a3719300474b36067b86dad7611d33a621956779e5d9517b1dfaef019e2085f)、[CLOCK_MCHP_DPLL_SRC_GCLK13](#ggad4a3719300474b36067b86dad7611d33a49e9404af4ac43cae2f763398bd684f5)、[CLOCK_MCHP_DPLL_SRC_GCLK14](#ggad4a3719300474b36067b86dad7611d33ad03e683a424631e0db34c23b3d5611a0)、[CLOCK_MCHP_DPLL_SRC_GCLK15](#ggad4a3719300474b36067b86dad7611d33a60af6e9669ecc5ae48c564d63550bf61)、[CLOCK_MCHP_DPLL_SRC_XOSC](#ggad4a3719300474b36067b86dad7611d33a99f7e9bb4cf4b36b79070f514c88ad1d)、[CLOCK_MCHP_DPLL_SRC_DFLL48M](#ggad4a3719300474b36067b86dad7611d33af1d913a5d9ad87b788becc822818080b)、[CLOCK_MCHP_DPLL_SRC_MAX](#ggad4a3719300474b36067b86dad7611d33a1035e2c8184feb507cd47a7046567f6b)。

数字锁相环（DPLL）的源时钟。

<a id="r_ga2b83aa5b88c064d44d3a0ef7661a15cf"></a>

```c
enum clock_mchp_rtc_src_clock { CLOCK_MCHP_RTC_SRC_ULP1K = OSC32KCTRL_CLKSELCTRL_RTCSEL_ULP1K_Val , CLOCK_MCHP_RTC_SRC_ULP32K = OSC32KCTRL_CLKSELCTRL_RTCSEL_ULP32K_Val , CLOCK_MCHP_RTC_SRC_XOSC1K = OSC32KCTRL_CLKSELCTRL_RTCSEL_XOSC1K_Val , CLOCK_MCHP_RTC_SRC_XOSC32K = OSC32KCTRL_CLKSELCTRL_RTCSEL_XOSC32K_Val }
```

相关声明：[clock_mchp_rtc_src_clock](#ga2b83aa5b88c064d44d3a0ef7661a15cf)、[CLOCK_MCHP_RTC_SRC_ULP1K](#gga2b83aa5b88c064d44d3a0ef7661a15cfafaa5cfa19e470035ad1cec308aa63f7b)、[CLOCK_MCHP_RTC_SRC_ULP32K](#gga2b83aa5b88c064d44d3a0ef7661a15cfa9095a4473e6e218ea0d2715695ecb2ff)、[CLOCK_MCHP_RTC_SRC_XOSC1K](#gga2b83aa5b88c064d44d3a0ef7661a15cfae738ec040a54d0b171192d122abdd332)、[CLOCK_MCHP_RTC_SRC_XOSC32K](#gga2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296)。

实时时钟（RTC）的源时钟（source clocks）。

<a id="r_ga073dab68c78edce3985eb201a039a989"></a>

```c
enum clock_mchp_gclk_src_clock { CLOCK_MCHP_GCLK_SRC_XOSC , CLOCK_MCHP_GCLK_SRC_GCLKPIN , CLOCK_MCHP_GCLK_SRC_GCLKGEN1 , CLOCK_MCHP_GCLK_SRC_OSCULP32K , CLOCK_MCHP_GCLK_SRC_XOSC32K , CLOCK_MCHP_GCLK_SRC_DFLL48M , CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT0 , CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT1 , CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT2 , CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT3 , CLOCK_MCHP_GCLK_SRC_DPLL1_FRC_CLKOUT0 , CLOCK_MCHP_GCLK_SRC_DPLL1_FRC_CLKOUT1 , CLOCK_MCHP_GCLK_SRC_DPLL1_CLKOUT2 , CLOCK_MCHP_GCLK_SRC_DPLL1_CLKOUT3 , CLOCK_MCHP_GCLK_SRC_MAX }
```

相关声明：[clock_mchp_gclk_src_clock](#ga073dab68c78edce3985eb201a039a989)、[CLOCK_MCHP_GCLK_SRC_XOSC](#gga073dab68c78edce3985eb201a039a989a002e232f09f2da92b359ecd1543465d0)、[CLOCK_MCHP_GCLK_SRC_GCLKPIN](#gga073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef)、[CLOCK_MCHP_GCLK_SRC_GCLKGEN1](#gga073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9)、[CLOCK_MCHP_GCLK_SRC_OSCULP32K](#gga073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6)、[CLOCK_MCHP_GCLK_SRC_XOSC32K](#gga073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380)、[CLOCK_MCHP_GCLK_SRC_DFLL48M](#gga073dab68c78edce3985eb201a039a989a647395dd08022519b13e0270f44943d6)、[CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT0](#gga073dab68c78edce3985eb201a039a989a97424a08d5ca63e8b0bb59699f199fbf)、[CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT1](#gga073dab68c78edce3985eb201a039a989a8db1c0dbb5d2fa6fc89208f26d8e18fb)、[CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT2](#gga073dab68c78edce3985eb201a039a989aab491fb5a01623e4248e04f4b6af9e76)、[CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT3](#gga073dab68c78edce3985eb201a039a989a1ec27a2b726685c4affe367881bd55e0)、[CLOCK_MCHP_GCLK_SRC_DPLL1_FRC_CLKOUT0](#gga073dab68c78edce3985eb201a039a989a4f5fc805a8d554b93427e31990e8d3cc)、[CLOCK_MCHP_GCLK_SRC_DPLL1_FRC_CLKOUT1](#gga073dab68c78edce3985eb201a039a989aa5ea75b3e521ddad5e1a4b64b385ff48)、[CLOCK_MCHP_GCLK_SRC_DPLL1_CLKOUT2](#gga073dab68c78edce3985eb201a039a989aff74c95610d9ea91fac78e3f90866dfb)、[CLOCK_MCHP_GCLK_SRC_DPLL1_CLKOUT3](#gga073dab68c78edce3985eb201a039a989a4868e29d2e440862dd6a8484134871ca)、[CLOCK_MCHP_GCLK_SRC_MAX](#gga073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768)。

GCLK 发生器的源时钟（source clocks）。

<a id="r_ga5835567db8d16c4eeb7a03b843ac6254"></a>

```c
enum clock_mchp_mclk_cpu_div { CLOCK_MCHP_MCLK_CPU_DIV_1 = 1 , CLOCK_MCHP_MCLK_CPU_DIV_2 = 2 , CLOCK_MCHP_MCLK_CPU_DIV_4 = 4 , CLOCK_MCHP_MCLK_CPU_DIV_8 = 8 , CLOCK_MCHP_MCLK_CPU_DIV_16 = 16 , CLOCK_MCHP_MCLK_CPU_DIV_32 = 32 , CLOCK_MCHP_MCLK_CPU_DIV_64 = 64 , CLOCK_MCHP_MCLK_CPU_DIV_128 = 128 }
```

相关声明：[clock_mchp_mclk_cpu_div](#ga5835567db8d16c4eeb7a03b843ac6254)、[CLOCK_MCHP_MCLK_CPU_DIV_1](#gga5835567db8d16c4eeb7a03b843ac6254a9f893cbec63df56227f17098ddf70074)、[CLOCK_MCHP_MCLK_CPU_DIV_2](#gga5835567db8d16c4eeb7a03b843ac6254ac52aba85d20e21bd3135cc46e467dbfc)、[CLOCK_MCHP_MCLK_CPU_DIV_4](#gga5835567db8d16c4eeb7a03b843ac6254ad251e58f232eaa9d45cce47e600b506f)、[CLOCK_MCHP_MCLK_CPU_DIV_8](#gga5835567db8d16c4eeb7a03b843ac6254ace4fa9213f609c27198c75f17b0f7beb)、[CLOCK_MCHP_MCLK_CPU_DIV_16](#gga5835567db8d16c4eeb7a03b843ac6254ae11a4d93aaafcfaeed5a7cc6e0a1de89)、[CLOCK_MCHP_MCLK_CPU_DIV_32](#gga5835567db8d16c4eeb7a03b843ac6254ab071663992b6be65b6f77442239d3157)、[CLOCK_MCHP_MCLK_CPU_DIV_64](#gga5835567db8d16c4eeb7a03b843ac6254a688a2dbe64b6a818ab84f26cc983b3f0)、[CLOCK_MCHP_MCLK_CPU_DIV_128](#gga5835567db8d16c4eeb7a03b843ac6254aefa35c60f9274b62c0b829c1c24a571b)。

CPU 的 MCLK 预分频器（Prescaler）分频比。

## 4.5\_详细说明（Detailed Documentation）

<a id="ga9b6955116dae7fa53c8dad373a1ef9c9"></a>

### `clock_mchp_rate_t`

```c
typedef uint32_t* clock_mchp_rate_t
```

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h>
```

时钟频率数据类型（clock rate datatype）。

用于设置时钟速率（Clock Rate）。

<a id="gad4a3719300474b36067b86dad7611d33"></a>

### `clock_mchp_dpll_src_clock`

```c
enum clock_mchp_dpll_src_clock
```

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h>
```

数字锁相环（DPLL）的源时钟。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_MCHP_DPLL_SRC_GCLK0` | 通用时钟发生器（Gclk Generator）0。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK1` | 通用时钟发生器（Gclk Generator）1。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK2` | 通用时钟发生器（Gclk Generator）2。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK3` | 通用时钟发生器（Gclk Generator）3。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK4` | 通用时钟发生器（Gclk Generator）4。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK5` | 通用时钟发生器（Gclk Generator）5。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK6` | 通用时钟发生器（Gclk Generator）6。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK7` | 通用时钟发生器（Gclk Generator）7。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK8` | 通用时钟发生器（Gclk Generator）8。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK9` | 通用时钟发生器（Gclk Generator）9。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK10` | 通用时钟发生器（Gclk Generator）10。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK11` | 通用时钟发生器（Gclk Generator）11。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK12` | 通用时钟发生器（GCLK Generator）12。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK13` | 通用时钟发生器（GCLK Generator）13。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK14` | 通用时钟发生器（GCLK Generator）14。 |
| `CLOCK_MCHP_DPLL_SRC_GCLK15` | 通用时钟发生器（GCLK Generator）15。 |
| `CLOCK_MCHP_DPLL_SRC_XOSC` | 外部晶体振荡器（External Crystal Oscillator，XOSC）。 |
| `CLOCK_MCHP_DPLL_SRC_DFLL48M` | 内部 48 MHz 数字锁频环（DFLL）时钟。 |
| `CLOCK_MCHP_DPLL_SRC_MAX` | 最大的有效 DPLL 源时钟（DPLL Source Clock）值。 |

<a id="ga073dab68c78edce3985eb201a039a989"></a>

### `clock_mchp_gclk_src_clock`

```c
enum clock_mchp_gclk_src_clock
```

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h>
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
| `CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT0` | DPLL0 输出时钟（Output Clock）0。 |
| `CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT1` | DPLL0 输出时钟（Output Clock）1。 |
| `CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT2` | DPLL0 输出时钟（Output Clock）2。 |
| `CLOCK_MCHP_GCLK_SRC_DPLL0_CLKOUT3` | DPLL0 输出时钟（Output Clock）3。 |
| `CLOCK_MCHP_GCLK_SRC_DPLL1_FRC_CLKOUT0` | DPLL1 输出时钟（Output Clock）0。 |
| `CLOCK_MCHP_GCLK_SRC_DPLL1_FRC_CLKOUT1` | DPLL1 输出时钟（Output Clock）1。 |
| `CLOCK_MCHP_GCLK_SRC_DPLL1_CLKOUT2` | DPLL1 输出时钟（Output Clock）2。 |
| `CLOCK_MCHP_GCLK_SRC_DPLL1_CLKOUT3` | DPLL1 输出时钟（Output Clock）3。 |
| `CLOCK_MCHP_GCLK_SRC_MAX` | 最大的有效 Gclk 时钟源（Gclk Source）值。 |

<a id="gaab34442b0d6c171691ae299675542777"></a>

### `clock_mchp_gclkgen`

```c
enum clock_mchp_gclkgen
```

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h>
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
| `CLOCK_MCHP_GCLKGEN_GEN12` | 通用时钟发生器（GCLK Generator）12。 |
| `CLOCK_MCHP_GCLKGEN_GEN13` | 通用时钟发生器（GCLK Generator）13。 |
| `CLOCK_MCHP_GCLKGEN_GEN14` | 通用时钟发生器（GCLK Generator）14。 |
| `CLOCK_MCHP_GCLKGEN_GEN15` | 通用时钟发生器（GCLK Generator）15。 |

<a id="ga5835567db8d16c4eeb7a03b843ac6254"></a>

### `clock_mchp_mclk_cpu_div`

```c
enum clock_mchp_mclk_cpu_div
```

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h>
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

<a id="ga2b83aa5b88c064d44d3a0ef7661a15cf"></a>

### `clock_mchp_rtc_src_clock`

```c
enum clock_mchp_rtc_src_clock
```

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h>
```

实时时钟（RTC）的源时钟（source clocks）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_MCHP_RTC_SRC_ULP1K` | 内部超低功耗（Ultra-low-power）1 kHz 振荡器。 |
| `CLOCK_MCHP_RTC_SRC_ULP32K` | 内部超低功耗（Ultra-low-power）32 kHz 振荡器。 |
| `CLOCK_MCHP_RTC_SRC_XOSC1K` | 分频至 1 kHz 的外部晶体振荡器（External Crystal Oscillator）。 |
| `CLOCK_MCHP_RTC_SRC_XOSC32K` | 外部 32.768 kHz 晶体振荡器（Crystal Oscillator）。 |


## 4.6\_原页交叉引用（Cross References）

- [mchp_clock_pic32cz_ca.h](../api_file_management_reference/P031_zephyr__drivers__clock_control__mchp_clock_pic32cz_ca.h_文件参考.md)
- [clock_mchp_subsys_xosc_config](../clock_cmsis_model_reference/P023_clock_mchp_subsys_xosc_config_结构体.md)
- [clock_mchp_subsys_dfll48m_config](../clock_cmsis_model_reference/P008_clock_mchp_subsys_dfll48m_config_结构体.md)
- [clock_mchp_subsys_dpll_config](../clock_cmsis_model_reference/P010_clock_mchp_subsys_dpll_config_结构体.md)
- [clock_mchp_subsys_dpll_out_config](../clock_cmsis_model_reference/P011_clock_mchp_subsys_dpll_out_config_结构体.md)
- [clock_mchp_subsys_rtc_config](../clock_cmsis_model_reference/P021_clock_mchp_subsys_rtc_config_结构体.md)
- [clock_mchp_subsys_xosc32k_config](../clock_cmsis_model_reference/P022_clock_mchp_subsys_xosc32k_config_结构体.md)
- [clock_mchp_subsys_gclkgen_config](../clock_cmsis_model_reference/P013_clock_mchp_subsys_gclkgen_config_结构体.md)
- [clock_mchp_subsys_gclkperiph_config](../clock_cmsis_model_reference/P014_clock_mchp_subsys_gclkperiph_config_结构体.md)
- [clock_mchp_subsys_mclkcpu_config](../clock_cmsis_model_reference/P015_clock_mchp_subsys_mclkcpu_config_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [clock_mchp_rate_t](../api_file_display_chat_reference/P018_zephyr__drivers__clock_control__mchp_clock_pic32ck_sg_gc.h_文件参考.md#a9b6955116dae7fa53c8dad373a1ef9c9)
- [clock_mchp_dpll_src_clock](../api_file_display_chat_reference/P019_zephyr__drivers__clock_control__mchp_clock_pic32cm_sg_gc.h_文件参考.md#ad4a3719300474b36067b86dad7611d33)
- [clock_mchp_gclk_src_clock](../api_file_display_chat_reference/P018_zephyr__drivers__clock_control__mchp_clock_pic32ck_sg_gc.h_文件参考.md#a073dab68c78edce3985eb201a039a989)
- [clock_mchp_gclkgen](../api_file_display_chat_reference/P018_zephyr__drivers__clock_control__mchp_clock_pic32ck_sg_gc.h_文件参考.md#aab34442b0d6c171691ae299675542777)
- [clock_mchp_mclk_cpu_div](../api_file_display_chat_reference/P018_zephyr__drivers__clock_control__mchp_clock_pic32ck_sg_gc.h_文件参考.md#a5835567db8d16c4eeb7a03b843ac6254)
- [clock_mchp_rtc_src_clock](../api_file_display_chat_reference/P018_zephyr__drivers__clock_control__mchp_clock_pic32ck_sg_gc.h_文件参考.md#a2b83aa5b88c064d44d3a0ef7661a15cf)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggad4a3719300474b36067b86dad7611d33ae3f23ab2c7a84a5c43fb8361b1ee1f83"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a75742e71b54b1bdefd0716085d47e496"></a>
<a id="ggad4a3719300474b36067b86dad7611d33af5906d13a56a0e26da669e15b5454b63"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a394cfe9ab4e963417fc0787c160ec847"></a>
<a id="ggad4a3719300474b36067b86dad7611d33afedc39675c6b63f46e36ed415ea04b27"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a34340db86e94450b72eae0d7ca0be283"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a183ebd7a615416cee57d7bdb0ce4d29b"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a4917fc8ee80c35ab78df854e2ce81958"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a5f67b9bf8fd7edbe90c4c22073ddc759"></a>
<a id="ggad4a3719300474b36067b86dad7611d33aaf6ebe0c6f7370866388499a7a4037c2"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a666358ed4b1f3564a7b4ae8a0b54cb06"></a>
<a id="ggad4a3719300474b36067b86dad7611d33abf6ced8f2a3eabadea96bdbf0b172b61"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a621956779e5d9517b1dfaef019e2085f"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a49e9404af4ac43cae2f763398bd684f5"></a>
<a id="ggad4a3719300474b36067b86dad7611d33ad03e683a424631e0db34c23b3d5611a0"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a60af6e9669ecc5ae48c564d63550bf61"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a99f7e9bb4cf4b36b79070f514c88ad1d"></a>
<a id="ggad4a3719300474b36067b86dad7611d33af1d913a5d9ad87b788becc822818080b"></a>
<a id="ggad4a3719300474b36067b86dad7611d33a1035e2c8184feb507cd47a7046567f6b"></a>
<a id="gga073dab68c78edce3985eb201a039a989a002e232f09f2da92b359ecd1543465d0"></a>
<a id="gga073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef"></a>
<a id="gga073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9"></a>
<a id="gga073dab68c78edce3985eb201a039a989a4d806ed2c0ab9d01cd429821b5a0c1b6"></a>
<a id="gga073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380"></a>
<a id="gga073dab68c78edce3985eb201a039a989a647395dd08022519b13e0270f44943d6"></a>
<a id="gga073dab68c78edce3985eb201a039a989a97424a08d5ca63e8b0bb59699f199fbf"></a>
<a id="gga073dab68c78edce3985eb201a039a989a8db1c0dbb5d2fa6fc89208f26d8e18fb"></a>
<a id="gga073dab68c78edce3985eb201a039a989aab491fb5a01623e4248e04f4b6af9e76"></a>
<a id="gga073dab68c78edce3985eb201a039a989a1ec27a2b726685c4affe367881bd55e0"></a>
<a id="gga073dab68c78edce3985eb201a039a989a4f5fc805a8d554b93427e31990e8d3cc"></a>
<a id="gga073dab68c78edce3985eb201a039a989aa5ea75b3e521ddad5e1a4b64b385ff48"></a>
<a id="gga073dab68c78edce3985eb201a039a989aff74c95610d9ea91fac78e3f90866dfb"></a>
<a id="gga073dab68c78edce3985eb201a039a989a4868e29d2e440862dd6a8484134871ca"></a>
<a id="gga073dab68c78edce3985eb201a039a989adde1984d3b00701241932ee89e494768"></a>
<a id="ggaab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f"></a>
<a id="ggaab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424"></a>
<a id="ggaab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe"></a>
<a id="ggaab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08"></a>
<a id="ggaab34442b0d6c171691ae299675542777a69bd2c6d8f016e8ecdfd07fba7268dcc"></a>
<a id="ggaab34442b0d6c171691ae299675542777a20bf106031eb19f25b8e3b1250033088"></a>
<a id="ggaab34442b0d6c171691ae299675542777a9cbc78f597c2930b36280c59164e12ae"></a>
<a id="ggaab34442b0d6c171691ae299675542777a71ead69f87ccd57496b0467a6264d411"></a>
<a id="ggaab34442b0d6c171691ae299675542777aff9b0bedc5de2cfe3259df2910ab55f9"></a>
<a id="ggaab34442b0d6c171691ae299675542777a96de017372252af6f1bcab2cdb32c2f1"></a>
<a id="ggaab34442b0d6c171691ae299675542777a63f142bb2401a057b9ba7b4a8f60eb60"></a>
<a id="ggaab34442b0d6c171691ae299675542777a905cb4bab8f6bb50f690de6a9e970695"></a>
<a id="ggaab34442b0d6c171691ae299675542777a6ea9310c7eb41d72c82b4abff78b36f8"></a>
<a id="ggaab34442b0d6c171691ae299675542777aaca57694ee279c5aa0b732bb9c7dcd19"></a>
<a id="ggaab34442b0d6c171691ae299675542777ae33d3555ccda79c69de0fc110937cf23"></a>
<a id="ggaab34442b0d6c171691ae299675542777a24e34e40f92b7cd41fa7d927097d6f25"></a>
<a id="gga5835567db8d16c4eeb7a03b843ac6254a9f893cbec63df56227f17098ddf70074"></a>
<a id="gga5835567db8d16c4eeb7a03b843ac6254ac52aba85d20e21bd3135cc46e467dbfc"></a>
<a id="gga5835567db8d16c4eeb7a03b843ac6254ad251e58f232eaa9d45cce47e600b506f"></a>
<a id="gga5835567db8d16c4eeb7a03b843ac6254ace4fa9213f609c27198c75f17b0f7beb"></a>
<a id="gga5835567db8d16c4eeb7a03b843ac6254ae11a4d93aaafcfaeed5a7cc6e0a1de89"></a>
<a id="gga5835567db8d16c4eeb7a03b843ac6254ab071663992b6be65b6f77442239d3157"></a>
<a id="gga5835567db8d16c4eeb7a03b843ac6254a688a2dbe64b6a818ab84f26cc983b3f0"></a>
<a id="gga5835567db8d16c4eeb7a03b843ac6254aefa35c60f9274b62c0b829c1c24a571b"></a>
<a id="gga2b83aa5b88c064d44d3a0ef7661a15cfafaa5cfa19e470035ad1cec308aa63f7b"></a>
<a id="gga2b83aa5b88c064d44d3a0ef7661a15cfa9095a4473e6e218ea0d2715695ecb2ff"></a>
<a id="gga2b83aa5b88c064d44d3a0ef7661a15cfae738ec040a54d0b171192d122abdd332"></a>
<a id="gga2b83aa5b88c064d44d3a0ef7661a15cfa22b1702bdaa9980876b770b033f12296"></a>

---

[上一章](P003_微芯（Microchip）PIC32CM JH.md) · [返回大纲](大纲.md) · [下一章](P005_微芯（Microchip）SAM D5x_E5x.md)
