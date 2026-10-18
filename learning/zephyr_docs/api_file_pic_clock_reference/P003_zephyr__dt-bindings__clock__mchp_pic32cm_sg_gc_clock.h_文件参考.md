---
id: learning.zephyr-docs.api-file-pic-clock-reference.page-3
title: zephyr__dt-bindings__clock__mchp_pic32cm_sg_gc_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__sg__gc__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_dt-bindings\_\_clock\_\_mchp\_pic32cm\_sg\_gc\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cm__sg__gc__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

列出pic32cm_sg_gc系列的时钟子系统ID（Clock Subsystem IDs）。

查看此文件的源码。

<a id="details"></a>

列出 `pic32cm_sg_gc` 系列的时钟子系统标识符（Clock Subsystem IDs）。这些标识符用于设备树节点（Devicetree Nodes），也用作时钟 API 的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_a0ebea68f214a63653aa0eaab0cf9c419"></a>

```c
#define MCHP_CLOCK_DERIVE_ID(type, mclkmaskreg, mclkmaskbit, gclkperiph, inst)
```

相关声明：[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

生成一个 32 位时钟子系统标识符（Clock Subsystem Identifier）。

<a id="define-members-0"></a>

### XOSC_TYPE 时钟标识符（Clock IDs）

<a id="r_a201012bb3a82a346aa0a98a5de91f320"></a>

```c
#define CLOCK_MCHP_XOSC_ID MCHP_CLOCK_DERIVE_ID(0, 0x3f, 0x3f, 0x3f, 0)
```

相关声明：[CLOCK_MCHP_XOSC_ID](#a201012bb3a82a346aa0a98a5de91f320)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

外部振荡器（External Oscillator，XOSC）的时钟标识符（Clock ID）。

<a id="r_a301af797e998ab83173d2a2e66a1ea38"></a>

```c
#define CLOCK_MCHP_XOSC_ID_MAX (0)
```

相关声明：[CLOCK_MCHP_XOSC_ID_MAX](#a301af797e998ab83173d2a2e66a1ea38)。

XOSC 时钟标识符（Clock IDs）的最大索引。

<a id="define-members-1"></a>

### DFLL48M_TYPE 时钟标识符（Clock IDs）

<a id="r_a42e64149c30379ebe4bd72a501d08f23"></a>

```c
#define CLOCK_MCHP_DFLL48M_ID MCHP_CLOCK_DERIVE_ID(1, 0x3f, 0x3f, 0, 0)
```

相关声明：[CLOCK_MCHP_DFLL48M_ID](#a42e64149c30379ebe4bd72a501d08f23)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

48 MHz 数字锁频环（Digital Frequency Locked Loop，DFLL48M）的时钟标识符（Clock ID）。

<a id="r_a16b646af4fc7f989c4c7cc781a82e1b7"></a>

```c
#define CLOCK_MCHP_DFLL48M_ID_MAX (0)
```

相关声明：[CLOCK_MCHP_DFLL48M_ID_MAX](#a16b646af4fc7f989c4c7cc781a82e1b7)。

DFLL48M 时钟标识符（Clock IDs）的最大索引。

<a id="define-members-2"></a>

### DPLL_TYPE 时钟标识符（Clock IDs）

<a id="r_a621a8f4faee2aa6d0d4d8af8609da0e9"></a>

```c
#define CLOCK_MCHP_DPLL_ID_DPLL0 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 1, 0)
```

相关声明：[CLOCK_MCHP_DPLL_ID_DPLL0](#a621a8f4faee2aa6d0d4d8af8609da0e9)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`DPLL0` 时钟标识符（Clock ID）。

<a id="r_a535adb887a7c5c21a1a88f0bf450e5ed"></a>

```c
#define CLOCK_MCHP_DPLL_ID_MAX (0)
```

相关声明：[CLOCK_MCHP_DPLL_ID_MAX](#a535adb887a7c5c21a1a88f0bf450e5ed)。

数字锁相环（DPLL）时钟标识符（Clock IDs）的最大索引。

<a id="define-members-3"></a>

### DPLL_OUT_TYPE 时钟标识符（Clock IDs）

<a id="r_a8e4b88e32515b2771e162e4be9cd6c27"></a>

```c
#define CLOCK_MCHP_DPLL0_ID_OUT0 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 0)
```

相关声明：[CLOCK_MCHP_DPLL0_ID_OUT0](#a8e4b88e32515b2771e162e4be9cd6c27)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`DPLL0` 输出（Output）0 的时钟标识符（Clock ID）。

<a id="r_af45f7265ef4e6481f60d436d672b9164"></a>

```c
#define CLOCK_MCHP_DPLL0_ID_OUT1 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 1)
```

相关声明：[CLOCK_MCHP_DPLL0_ID_OUT1](#af45f7265ef4e6481f60d436d672b9164)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`DPLL0` 输出（Output）1 的时钟标识符（Clock ID）。

<a id="r_a9927eaa7ed4808661de94201f1c22b84"></a>

```c
#define CLOCK_MCHP_DPLL0_ID_OUT2 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 2)
```

相关声明：[CLOCK_MCHP_DPLL0_ID_OUT2](#a9927eaa7ed4808661de94201f1c22b84)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`DPLL0` 输出（Output）2 的时钟标识符（Clock ID）。

<a id="r_a13f41de316cb8d3f41b75b0934d2c1c4"></a>

```c
#define CLOCK_MCHP_DPLL0_ID_OUT3 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 3)
```

相关声明：[CLOCK_MCHP_DPLL0_ID_OUT3](#a13f41de316cb8d3f41b75b0934d2c1c4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`DPLL0` 输出（Output）3 的时钟标识符（Clock ID）。

<a id="r_a3625ecaf031e005197b61a72e82a8f38"></a>

```c
#define CLOCK_MCHP_DPLL0_ID_OUT4 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 4)
```

相关声明：[CLOCK_MCHP_DPLL0_ID_OUT4](#a3625ecaf031e005197b61a72e82a8f38)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`DPLL0` 输出（Output）4 的时钟标识符（Clock ID）。

<a id="r_a1d020421206c10005772bc3912989fa6"></a>

```c
#define CLOCK_MCHP_DPLL_OUT_ID_MAX (4)
```

相关声明：[CLOCK_MCHP_DPLL_OUT_ID_MAX](#a1d020421206c10005772bc3912989fa6)。

DPLL 输出时钟标识符（Output Clock IDs）的最大索引。

<a id="define-members-4"></a>

### RTC_TYPE 时钟标识符（Clock IDs）

<a id="r_aed47d2a2eccaea5ed5f5e99fa41afbbb"></a>

```c
#define CLOCK_MCHP_RTC_ID MCHP_CLOCK_DERIVE_ID(4, 0x3f, 0x3f, 0x3f, 0)
```

相关声明：[CLOCK_MCHP_RTC_ID](#aed47d2a2eccaea5ed5f5e99fa41afbbb)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

实时时钟计数器（Real-Time Counter，RTC）的时钟标识符（Clock ID）。

<a id="r_aa6dc48a4e2e1047734e02f8c060e9369"></a>

```c
#define CLOCK_MCHP_RTC_ID_MAX (0)
```

相关声明：[CLOCK_MCHP_RTC_ID_MAX](#aa6dc48a4e2e1047734e02f8c060e9369)。

RTC 时钟标识符（Clock IDs）的最大索引。

<a id="define-members-5"></a>

### XOSC32K_TYPE 时钟标识符（Clock IDs）

<a id="r_a3262be48f6349821c62498b0521226ff"></a>

```c
#define CLOCK_MCHP_XOSC32K_ID MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 0)
```

相关声明：[CLOCK_MCHP_XOSC32K_ID](#a3262be48f6349821c62498b0521226ff)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

32 kHz 外部振荡器（External Oscillator，XOSC32K）的时钟标识符（Clock ID）。

<a id="r_a09e1e2095d902fe6c82d7992a2eac5da"></a>

```c
#define CLOCK_MCHP_XOSC32K_ID_MAX (0)
```

相关声明：[CLOCK_MCHP_XOSC32K_ID_MAX](#a09e1e2095d902fe6c82d7992a2eac5da)。

XOSC32K 时钟标识符（Clock IDs）的最大索引。

<a id="define-members-6"></a>

### GCLKGEN_TYPE 时钟标识符（Clock IDs）

<a id="r_adc730b78bbb79a2de524288fb8f2a90f"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN0 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 0)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN0](#adc730b78bbb79a2de524288fb8f2a90f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）0 的标识符（ID）。

<a id="r_a7d1c402859c4f053d487b78002f0b16d"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN1 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 1)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN1](#a7d1c402859c4f053d487b78002f0b16d)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）1 的标识符（ID）。

<a id="r_a2dda06b2509f1d33896bf82927da6f84"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN2 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 2)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN2](#a2dda06b2509f1d33896bf82927da6f84)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）2 的标识符（ID）。

<a id="r_ac6c91333d8e736f9c25c765f05f4be66"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN3 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 3)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN3](#ac6c91333d8e736f9c25c765f05f4be66)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）3 的标识符（ID）。

<a id="r_a6bd03b027dab2c82624de849d355e3c7"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN4 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 4)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN4](#a6bd03b027dab2c82624de849d355e3c7)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）4 的标识符（ID）。

<a id="r_ae018b90957ec659f5225363264173348"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN5 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 5)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN5](#ae018b90957ec659f5225363264173348)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）5 的标识符（ID）。

<a id="r_a648ca2df6a086f43bbd79c76726b8acf"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN6 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 6)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN6](#a648ca2df6a086f43bbd79c76726b8acf)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）6 的标识符（ID）。

<a id="r_adcfc04767ae03fef19c1fa01adf73c60"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN7 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 7)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN7](#adcfc04767ae03fef19c1fa01adf73c60)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）7 的标识符（ID）。

<a id="r_a0e06ddf395b54a0c7b9b2d3f284e8449"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN8 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 8)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN8](#a0e06ddf395b54a0c7b9b2d3f284e8449)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）8 的标识符（ID）。

<a id="r_a3da646cdf217d24807332b782c2056c9"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN9 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 9)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN9](#a3da646cdf217d24807332b782c2056c9)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）9 的标识符（ID）。

<a id="r_ab9a58178e0fd1faa6804f35709ac4e94"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN10 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 10)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN10](#ab9a58178e0fd1faa6804f35709ac4e94)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）10 的标识符（ID）。

<a id="r_a8fad76e8d57aa754d1237f4fae8be6ed"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN11 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 11)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN11](#a8fad76e8d57aa754d1237f4fae8be6ed)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）11 的标识符（ID）。

<a id="r_a67296972320d7cb9295cd67c9cf25c54"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_MAX (11)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_MAX](#a67296972320d7cb9295cd67c9cf25c54)。

通用时钟发生器标识符（Generic Clock Generator IDs）的最大索引。

<a id="define-members-7"></a>

### GCLKPERIPH_TYPE 时钟标识符（Clock IDs）

<a id="r_a9447de6351b7f09b6a30d8df8e586d85"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 2, 0)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR0](#a9447de6351b7f09b6a30d8df8e586d85)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：频率计测量 0（Frequency Meter Measure 0）。

<a id="r_ac6fc7ade933679db0f47c23fb27c6988"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 3, 1)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR1](#ac6fc7ade933679db0f47c23fb27c6988)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：频率计测量 1（Frequency Meter Measure 1）。

<a id="r_a0da9e951ad59ea7ffa1b3a0586203202"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 4, 2)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF](#a0da9e951ad59ea7ffa1b3a0586203202)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：频率计参考（Frequency Meter Reference）。

<a id="r_aeaeb9a032e3fa5a00199ef27c2a5ec30"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EIC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 5, 3)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EIC](#aeaeb9a032e3fa5a00199ef27c2a5ec30)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：外部中断控制器 (EIC)（External Interrupt Controller (EIC)）。

<a id="r_ae251d4719eb378734e3cb01c9f5828d8"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 6, 4)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CAN0](#ae251d4719eb378734e3cb01c9f5828d8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CAN0（CAN0）。

<a id="r_a2e77a06b25293f4152b0f2399ab32982"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 7, 5)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CAN1](#a2e77a06b25293f4152b0f2399ab32982)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CAN1（CAN1）。

<a id="r_a31aa9472c7182d16249ba7950b452c14"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 8, 6)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0](#a31aa9472c7182d16249ba7950b452c14)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 0（Event System Channel 0）。

<a id="r_a370930d5d12099ec34871a27cee5c8e2"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 9, 7)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1](#a370930d5d12099ec34871a27cee5c8e2)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 1（Event System Channel 1）。

<a id="r_a6966d71c9da4ce1803c48dc088818401"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 10, 8)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2](#a6966d71c9da4ce1803c48dc088818401)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 2（Event System Channel 2）。

<a id="r_a5d98273862a2323e050874755da0c840"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 11, 9)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3](#a5d98273862a2323e050874755da0c840)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 3（Event System Channel 3）。

<a id="r_a24855b6b55dc3eb9efba6476d6d930e8"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 12, 10)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4](#a24855b6b55dc3eb9efba6476d6d930e8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 4（Event System Channel 4）。

<a id="r_a6bb92b5d57c58e6b1ab083504bbb3756"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 13, 11)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5](#a6bb92b5d57c58e6b1ab083504bbb3756)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 5（Event System Channel 5）。

<a id="r_ae2404c8e3bce6bd9b01903a9ad942d35"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 14, 12)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6](#ae2404c8e3bce6bd9b01903a9ad942d35)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 6（Event System Channel 6）。

<a id="r_a852a5424cc73a5e75fcd7b151e7dd767"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 15, 13)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7](#a852a5424cc73a5e75fcd7b151e7dd767)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 7（Event System Channel 7）。

<a id="r_a9ff8a7f89700d95e431e6d0c12869b56"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 16, 14)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8](#a9ff8a7f89700d95e431e6d0c12869b56)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 8（Event System Channel 8）。

<a id="r_ad7112111ef68955636866ec0adb0e71e"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 17, 15)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9](#ad7112111ef68955636866ec0adb0e71e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 9（Event System Channel 9）。

<a id="r_aeb43cfd70588d9f660e8965516480191"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 16)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10](#aeb43cfd70588d9f660e8965516480191)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 10（Event System Channel 10）。

<a id="r_a93e2a650425a0bb9014c56d848c039bb"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 17)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11](#a93e2a650425a0bb9014c56d848c039bb)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 11（Event System Channel 11）。

<a id="r_a2bb7a4f72e45c2fb5f449b6b3f1b4520"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 18)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW](#a2bb7a4f72e45c2fb5f449b6b3f1b4520)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM0 慢速 时钟（SERCOM0 Slow clock）。

<a id="r_a726fe192480ed57fbdc3e77cc1133c89"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 19)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW](#a726fe192480ed57fbdc3e77cc1133c89)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM1 慢速 时钟（SERCOM1 Slow clock）。

<a id="r_a99d3f0a1c9e10f405c761ae6f3bf2744"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 20)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW](#a99d3f0a1c9e10f405c761ae6f3bf2744)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM2 慢速 时钟（SERCOM2 Slow clock）。

<a id="r_a08fb53b9b65e5743900bd6a4179925d3"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 21)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW](#a08fb53b9b65e5743900bd6a4179925d3)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM3 慢速 时钟（SERCOM3 Slow clock）。

<a id="r_a88f1128166176ebfc0a41dd496186300"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 21, 22)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE](#a88f1128166176ebfc0a41dd496186300)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM0 核心 时钟（SERCOM0 Core clock）。

<a id="r_ab3ef99c62a821f4e5fe1f800de6561c2"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 22, 23)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE](#ab3ef99c62a821f4e5fe1f800de6561c2)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM1 核心 时钟（SERCOM1 Core clock）。

<a id="r_ab0668a32e7385c8629b26cd396e6beaa"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 24)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE](#ab0668a32e7385c8629b26cd396e6beaa)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM2 核心 时钟（SERCOM2 Core clock）。

<a id="r_a155a02aa8799940dd0c59efac25e5bbc"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 25)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE](#a155a02aa8799940dd0c59efac25e5bbc)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM3 核心 时钟（SERCOM3 Core clock）。

<a id="r_af3614ec46e49df22dc37768df6e9c12b"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 26)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC0](#af3614ec46e49df22dc37768df6e9c12b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC0（TCC0）。

<a id="r_a253908d056c2ac97302065d9c0eb1cc4"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 27)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC1](#a253908d056c2ac97302065d9c0eb1cc4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC1（TCC1）。

<a id="r_ae4ebf71771a1435faa34293290ed06f0"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 26, 28)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC2](#ae4ebf71771a1435faa34293290ed06f0)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC2（TCC2）。

<a id="r_a363610cff7033e1bb7036d3b4ed21a0c"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 27, 29)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC3](#a363610cff7033e1bb7036d3b4ed21a0c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC3（TCC3）。

<a id="r_a77eb95730d000556c3b32a7bcf152913"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 28, 30)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE](#a77eb95730d000556c3b32a7bcf152913)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM4 核心 时钟（SERCOM4 Core clock）。

<a id="r_a4b1126fa67b001d9d086874d8536fb48"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 29, 31)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE](#a4b1126fa67b001d9d086874d8536fb48)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM5 核心 时钟（SERCOM5 Core clock）。

<a id="r_a341713f50727d73e4275cc093061487e"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 30, 32)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC4](#a341713f50727d73e4275cc093061487e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC4（TCC4）。

<a id="r_a1cb0b9600a335a01ff00c7eaa64a1229"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 31, 33)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC5](#a1cb0b9600a335a01ff00c7eaa64a1229)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC5（TCC5）。

<a id="r_a14a655c0aead0534f6915a1994a6ed1d"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 32, 34)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC6](#a14a655c0aead0534f6915a1994a6ed1d)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC6（TCC6）。

<a id="r_a845a53053a861de67ebfa150bff389ff"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 33, 35)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_ADC](#a845a53053a861de67ebfa150bff389ff)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：ADC（ADC）。

<a id="r_a8558308cb89c99326b165a7b12b14ff1"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_AC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 34, 36)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_AC](#a8558308cb89c99326b165a7b12b14ff1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：AC (模拟比较器)（AC (Analog Comparator)）。

<a id="r_a65c9bc79d0b5edd7dcc8a6178a600127"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_PTC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 35, 37)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_PTC](#a65c9bc79d0b5edd7dcc8a6178a600127)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：PTC (外设触摸控制器)（PTC (Peripheral Touch Controller)）。

<a id="r_ad49c597f4341f2f56e285e02b05e9563"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CCL0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 36, 38)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CCL0](#ad49c597f4341f2f56e285e02b05e9563)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CCL0（CCL0）。

<a id="r_abd2528ca834d9db6b7bc50e2005f0ed4"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CCL1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 37, 39)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CCL1](#abd2528ca834d9db6b7bc50e2005f0ed4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CCL1（CCL1）。

<a id="r_a566c7babd5641f337fc00adb20367833"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_USB MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 38, 40)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_USB](#a566c7babd5641f337fc00adb20367833)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：USB（USB）。

<a id="r_a9fb0644f504a830a4e324f792815ae98"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_MAX (40)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_MAX](#a9fb0644f504a830a4e324f792815ae98)。

GCLK 外设标识符（Peripheral IDs）的最大索引。

<a id="define-members-8"></a>

### MCLKDOMAIN_TYPE 时钟标识符（Clock IDs）

<a id="r_ac40643badee3512255e142465f0f31b4"></a>

```c
#define CLOCK_MCHP_MCLKDOMAIN_ID_CPU MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 0)
```

相关声明：[CLOCK_MCHP_MCLKDOMAIN_ID_CPU](#ac40643badee3512255e142465f0f31b4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

主时钟域标识符（Main Clock Domain ID）：CPU。

<a id="r_adec6556749cbc3c25b049fd700c36e94"></a>

```c
#define CLOCK_MCHP_MCLKDOMAIN_MAX (0)
```

相关声明：[CLOCK_MCHP_MCLKDOMAIN_MAX](#adec6556749cbc3c25b049fd700c36e94)。

主时钟域标识符（Main Clock Domain IDs）的最大索引。

<a id="define-members-9"></a>

### MCLKPERIPH_TYPE 时钟标识符（Clock IDs）

<a id="r_a5f1c9309e3eb0586eb1f765536b4346e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 0, 0x3f, 0)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB](#a5f1c9309e3eb0586eb1f765536b4346e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DSU (AHB)（DSU (AHB)）。

<a id="r_af85028f923174b11e44d1fc9043c5c75"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 1, 0x3f, 1)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB](#af85028f923174b11e44d1fc9043c5c75)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FCR (AHB)（FCR (AHB)）。

<a id="r_a55391bcfa4db8dfdf6d7fbfbfbc9626f"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 2, 0x3f, 2)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB](#a55391bcfa4db8dfdf6d7fbfbfbc9626f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FCW (AHB)（FCW (AHB)）。

<a id="r_a4f661f6845c462308dbd9dc635eb0216"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PM MCHP_CLOCK_DERIVE_ID(9, 0, 3, 0x3f, 3)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PM](#a4f661f6845c462308dbd9dc635eb0216)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PM（PM）。

<a id="r_a5ae4a436c06ce604b358096d14213da8"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SUPC MCHP_CLOCK_DERIVE_ID(9, 0, 4, 0x3f, 4)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SUPC](#a5ae4a436c06ce604b358096d14213da8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SUPC（SUPC）。

<a id="r_abf5fe57afad6b6d3f88cf4165406c468"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RSTC MCHP_CLOCK_DERIVE_ID(9, 0, 5, 0x3f, 5)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_RSTC](#abf5fe57afad6b6d3f88cf4165406c468)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：RSTC（RSTC）。

<a id="r_af4fe59e6405058b34f7205f58631c38e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL MCHP_CLOCK_DERIVE_ID(9, 0, 6, 0x3f, 6)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL](#af4fe59e6405058b34f7205f58631c38e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：OSCCTRL（OSCCTRL）。

<a id="r_a721267129ed0b4edf349298f972ae3af"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL MCHP_CLOCK_DERIVE_ID(9, 0, 7, 0x3f, 7)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL](#a721267129ed0b4edf349298f972ae3af)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：OSC32KCTRL（OSC32KCTRL）。

<a id="r_a37509ecf92c06e1f063a8c78c8fa0fe7"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FREQM MCHP_CLOCK_DERIVE_ID(9, 0, 10, 0x3f, 8)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FREQM](#a37509ecf92c06e1f063a8c78c8fa0fe7)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FREQM（FREQM）。

<a id="r_a75aeee838d3138dcf67732e62cd3d879"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_WDT MCHP_CLOCK_DERIVE_ID(9, 0, 11, 0x3f, 9)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_WDT](#a75aeee838d3138dcf67732e62cd3d879)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：WDT（WDT）。

<a id="r_ab7ce87ea60b62f5a3d77297cd1d7d713"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RTC MCHP_CLOCK_DERIVE_ID(9, 0, 12, 0x3f, 10)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_RTC](#ab7ce87ea60b62f5a3d77297cd1d7d713)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：RTC（RTC）。

<a id="r_afb137dc52e627ab615dea380c58a44da"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EIC MCHP_CLOCK_DERIVE_ID(9, 0, 13, 0x3f, 11)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_EIC](#afb137dc52e627ab615dea380c58a44da)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：EIC（EIC）。

<a id="r_a574e9bee5faec84626fa1e9ef679e71a"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB MCHP_CLOCK_DERIVE_ID(9, 0, 14, 0x3f, 12)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB](#a574e9bee5faec84626fa1e9ef679e71a)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PAC (APB)（PAC (APB)）。

<a id="r_a9d398dd236236c3fa38dd3f4d3e79c10"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TRAM MCHP_CLOCK_DERIVE_ID(9, 0, 15, 0x3f, 13)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TRAM](#a9d398dd236236c3fa38dd3f4d3e79c10)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TRAM（TRAM）。

<a id="r_a62ee930ec74fb592e2e1ead390e5670a"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC_APB MCHP_CLOCK_DERIVE_ID(9, 0, 21, 0x3f, 14)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC_APB](#a62ee930ec74fb592e2e1ead390e5670a)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：MCRAMC_APB（MCRAMC_APB）。

<a id="r_ac150a2e0461227827858435745496711"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 22, 0x3f, 15)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC_AHB](#ac150a2e0461227827858435745496711)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：MCRAMC_AHB（MCRAMC_AHB）。

<a id="r_a4188938454ae1ed53076aaf4def7f39e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN0 MCHP_CLOCK_DERIVE_ID(9, 0, 23, 0x3f, 16)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CAN0](#a4188938454ae1ed53076aaf4def7f39e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CAN0（CAN0）。

<a id="r_af9fc7781311291889227f80a8af51a76"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN1 MCHP_CLOCK_DERIVE_ID(9, 0, 24, 0x3f, 17)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CAN1](#af9fc7781311291889227f80a8af51a76)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CAN1（CAN1）。

<a id="r_a99453d72ee3d6a66ad85d009f6c3d9bd"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB0_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 25, 0x3f, 18)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_H2PB0_AHB](#a99453d72ee3d6a66ad85d009f6c3d9bd)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：H2PB0 (AHB)（H2PB0 (AHB)）。

<a id="r_a53cd4e5390a70155b5062e52642c6d63"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB0_APB MCHP_CLOCK_DERIVE_ID(9, 0, 26, 0x3f, 19)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_H2PB0_APB](#a53cd4e5390a70155b5062e52642c6d63)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：H2PB0 (APB)（H2PB0 (APB)）。

<a id="r_acadb93a9913d4622db5b6e0b7d375ef1"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB MCHP_CLOCK_DERIVE_ID(9, 0, 27, 0x3f, 20)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB](#acadb93a9913d4622db5b6e0b7d375ef1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PORT (APB)（PORT (APB)）。

<a id="r_a1ea38f3f64ebc1ec538530a23920f45d"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 28, 0x3f, 21)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DMAC_AHB](#a1ea38f3f64ebc1ec538530a23920f45d)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DMAC (AHB)（DMAC (AHB)）。

<a id="r_ae0a16f13ccf85d54ebc961054850376c"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_APB MCHP_CLOCK_DERIVE_ID(9, 0, 29, 0x3f, 22)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DMAC_APB](#ae0a16f13ccf85d54ebc961054850376c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DMAC (APB)（DMAC (APB)）。

<a id="r_a9f2830ece9477f6092119a42fec6b434"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HMATRIX2_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 30, 0x3f, 23)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_HMATRIX2_AHB](#a9f2830ece9477f6092119a42fec6b434)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：HMATRIX2 (AHB)（HMATRIX2 (AHB)）。

<a id="r_a1857f3b332085910127c68b7ecb6bc8b"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HMATRIX2_APB MCHP_CLOCK_DERIVE_ID(9, 0, 31, 0x3f, 24)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_HMATRIX2_APB](#a1857f3b332085910127c68b7ecb6bc8b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：HMATRIX2 (APB)（HMATRIX2 (APB)）。

<a id="r_a574a3cc55f7a8bf32a82232e293a29bc"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BROMC_AHB MCHP_CLOCK_DERIVE_ID(9, 1, 0, 0x3f, 25)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_BROMC_AHB](#a574a3cc55f7a8bf32a82232e293a29bc)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：BROMC (AHB)（BROMC (AHB)）。

<a id="r_a8bad753f6086aaa0288d62dc773fb2d1"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BROMC_APB MCHP_CLOCK_DERIVE_ID(9, 1, 1, 0x3f, 26)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_BROMC_APB](#a8bad753f6086aaa0288d62dc773fb2d1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：BROMC (APB)（BROMC (APB)）。

<a id="r_a0154852bd2224c7a6707bc78b6f6ed3b"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_IDAU MCHP_CLOCK_DERIVE_ID(9, 1, 2, 0x3f, 27)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_IDAU](#a0154852bd2224c7a6707bc78b6f6ed3b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：IDAU（IDAU）。

<a id="r_a1f3f4077f0f5be1dd872c8a18052317e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EVSYS MCHP_CLOCK_DERIVE_ID(9, 1, 3, 0x3f, 28)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_EVSYS](#a1f3f4077f0f5be1dd872c8a18052317e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：EVSYS（EVSYS）。

<a id="r_aaca27bd670359e191ee3ded852b86e9b"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0 MCHP_CLOCK_DERIVE_ID(9, 1, 4, 0x3f, 29)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0](#aaca27bd670359e191ee3ded852b86e9b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM0（SERCOM0）。

<a id="r_ad61fa9b33a8ea563a180c95213ad1d9b"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1 MCHP_CLOCK_DERIVE_ID(9, 1, 5, 0x3f, 30)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1](#ad61fa9b33a8ea563a180c95213ad1d9b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM1（SERCOM1）。

<a id="r_a75fb3dc587c912a5a961dfcd61066e09"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2 MCHP_CLOCK_DERIVE_ID(9, 1, 6, 0x3f, 31)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2](#a75fb3dc587c912a5a961dfcd61066e09)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM2（SERCOM2）。

<a id="r_a893c130bcc447db2b076b694614be658"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3 MCHP_CLOCK_DERIVE_ID(9, 1, 7, 0x3f, 32)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3](#a893c130bcc447db2b076b694614be658)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM3（SERCOM3）。

<a id="r_ad3a8bd23b104522ca890997304fc21d4"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC0 MCHP_CLOCK_DERIVE_ID(9, 1, 8, 0x3f, 33)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC0](#ad3a8bd23b104522ca890997304fc21d4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC0（TCC0）。

<a id="r_ad60be2a1615dfd0de08bb0960e4e4526"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC1 MCHP_CLOCK_DERIVE_ID(9, 1, 9, 0x3f, 34)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC1](#ad60be2a1615dfd0de08bb0960e4e4526)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC1（TCC1）。

<a id="r_a7f0be35a75e900699a10445d7a8463ca"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC2 MCHP_CLOCK_DERIVE_ID(9, 1, 10, 0x3f, 35)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC2](#a7f0be35a75e900699a10445d7a8463ca)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC2（TCC2）。

<a id="r_a1c25975110ff6f0a977adb760c3eef7e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC3 MCHP_CLOCK_DERIVE_ID(9, 1, 11, 0x3f, 36)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC3](#a1c25975110ff6f0a977adb760c3eef7e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC3（TCC3）。

<a id="r_ab86030aa3e1e599bbc46211ca4044488"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4 MCHP_CLOCK_DERIVE_ID(9, 1, 12, 0x3f, 37)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4](#ab86030aa3e1e599bbc46211ca4044488)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM4（SERCOM4）。

<a id="r_ae99c49a5fc48f51bc151d03d8f383cc6"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5 MCHP_CLOCK_DERIVE_ID(9, 1, 13, 0x3f, 38)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5](#ae99c49a5fc48f51bc151d03d8f383cc6)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM5（SERCOM5）。

<a id="r_af79ecdecbec732ce71599f0311d57580"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC4 MCHP_CLOCK_DERIVE_ID(9, 1, 14, 0x3f, 39)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC4](#af79ecdecbec732ce71599f0311d57580)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC4（TCC4）。

<a id="r_ab84c014f1edb2bc7e374a3f82c2ef71d"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC5 MCHP_CLOCK_DERIVE_ID(9, 1, 15, 0x3f, 40)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC5](#ab84c014f1edb2bc7e374a3f82c2ef71d)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC5（TCC5）。

<a id="r_ae95d523e3ad45348066f68fb19622aba"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC6 MCHP_CLOCK_DERIVE_ID(9, 1, 16, 0x3f, 41)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC6](#ae95d523e3ad45348066f68fb19622aba)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC6（TCC6）。

<a id="r_a5d8481769aaec20ff21d47d3ac1347e3"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_ADC MCHP_CLOCK_DERIVE_ID(9, 1, 17, 0x3f, 42)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_ADC](#a5d8481769aaec20ff21d47d3ac1347e3)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：ADC（ADC）。

<a id="r_a15b5103e5212ada5ae5da15831345e2a"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_AC MCHP_CLOCK_DERIVE_ID(9, 1, 18, 0x3f, 43)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_AC](#a15b5103e5212ada5ae5da15831345e2a)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：AC（AC）。

<a id="r_a839339c5809445addd8326f7f3988c96"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PTC MCHP_CLOCK_DERIVE_ID(9, 1, 19, 0x3f, 44)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PTC](#a839339c5809445addd8326f7f3988c96)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PTC（PTC）。

<a id="r_af7b9a675b06b90d460e54af43fb54f62"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CCL0 MCHP_CLOCK_DERIVE_ID(9, 1, 20, 0x3f, 45)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CCL0](#af7b9a675b06b90d460e54af43fb54f62)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CCL0（CCL0）。

<a id="r_a72406d795f45e47145cb9148799de080"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CCL1 MCHP_CLOCK_DERIVE_ID(9, 1, 21, 0x3f, 46)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CCL1](#a72406d795f45e47145cb9148799de080)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CCL1（CCL1）。

<a id="r_aed4f4cc3736914dd59e481ad37710868"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_USB_AHB MCHP_CLOCK_DERIVE_ID(9, 1, 22, 0x3f, 47)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_USB_AHB](#aed4f4cc3736914dd59e481ad37710868)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：USB_AHB（USB_AHB）。

<a id="r_aae27b56b768f9c68bfb39f8a6ea3bd34"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_USB_APB MCHP_CLOCK_DERIVE_ID(9, 1, 23, 0x3f, 48)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_USB_APB](#aae27b56b768f9c68bfb39f8a6ea3bd34)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：USB_APB（USB_APB）。

<a id="r_aa1a035c7f4ff1b0a1f9ef7157f38a6b5"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_AT MCHP_CLOCK_DERIVE_ID(9, 1, 24, 0x3f, 49)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_AT](#aa1a035c7f4ff1b0a1f9ef7157f38a6b5)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：AT（AT）。

<a id="r_a60942f65bae6aaea4ca522e428129485"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB1_AHB MCHP_CLOCK_DERIVE_ID(9, 1, 25, 0x3f, 50)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_H2PB1_AHB](#a60942f65bae6aaea4ca522e428129485)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：H2PB1_AHB（H2PB1_AHB）。

<a id="r_ac7212a639e29b519b89824b69f1f794c"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB1_APB MCHP_CLOCK_DERIVE_ID(9, 1, 26, 0x3f, 51)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_H2PB1_APB](#ac7212a639e29b519b89824b69f1f794c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：H2PB1_APB（H2PB1_APB）。

<a id="r_ae3634155142a10632b80dd498221e215"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB2_AHB MCHP_CLOCK_DERIVE_ID(9, 1, 27, 0x3f, 52)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_H2PB2_AHB](#ae3634155142a10632b80dd498221e215)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：H2PB2_AHB（H2PB2_AHB）。

<a id="r_a0796bf3dd83dd952a5d2c871363946dc"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB2_APB MCHP_CLOCK_DERIVE_ID(9, 1, 28, 0x3f, 53)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_H2PB2_APB](#a0796bf3dd83dd952a5d2c871363946dc)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：H2PB2_APB（H2PB2_APB）。

<a id="r_a7d9495c1ea1942c4d2fc069a29e23d6a"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HSM MCHP_CLOCK_DERIVE_ID(9, 1, 30, 0x3f, 54)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_HSM](#a7d9495c1ea1942c4d2fc069a29e23d6a)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：HSM（HSM）。

<a id="r_a28446fa9da2b5261abbd15da2368fcf1"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PUF MCHP_CLOCK_DERIVE_ID(9, 1, 31, 0x3f, 55)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PUF](#a28446fa9da2b5261abbd15da2368fcf1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PUF（PUF）。

<a id="r_a5884aa8fb4b6841cf3b36f8df64136d1"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MAX (55)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_MAX](#a5884aa8fb4b6841cf3b36f8df64136d1)。

MCLK 外设标识符（Peripheral IDs）的最大索引。

## 3.2\_详细说明（Detailed Documentation）

<a id="a42e64149c30379ebe4bd72a501d08f23"></a>

### `CLOCK_MCHP_DFLL48M_ID`

```c
#define CLOCK_MCHP_DFLL48M_ID MCHP_CLOCK_DERIVE_ID(1, 0x3f, 0x3f, 0, 0)
```

48 MHz 数字锁频环（Digital Frequency Locked Loop，DFLL48M）的时钟标识符（Clock ID）。

<a id="a16b646af4fc7f989c4c7cc781a82e1b7"></a>

### `CLOCK_MCHP_DFLL48M_ID_MAX`

```c
#define CLOCK_MCHP_DFLL48M_ID_MAX (0)
```

DFLL48M 时钟标识符（Clock IDs）的最大索引。

<a id="a8e4b88e32515b2771e162e4be9cd6c27"></a>

### `CLOCK_MCHP_DPLL0_ID_OUT0`

```c
#define CLOCK_MCHP_DPLL0_ID_OUT0 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 0)
```

`DPLL0` 输出（Output）0 的时钟标识符（Clock ID）。

<a id="af45f7265ef4e6481f60d436d672b9164"></a>

### `CLOCK_MCHP_DPLL0_ID_OUT1`

```c
#define CLOCK_MCHP_DPLL0_ID_OUT1 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 1)
```

`DPLL0` 输出（Output）1 的时钟标识符（Clock ID）。

<a id="a9927eaa7ed4808661de94201f1c22b84"></a>

### `CLOCK_MCHP_DPLL0_ID_OUT2`

```c
#define CLOCK_MCHP_DPLL0_ID_OUT2 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 2)
```

`DPLL0` 输出（Output）2 的时钟标识符（Clock ID）。

<a id="a13f41de316cb8d3f41b75b0934d2c1c4"></a>

### `CLOCK_MCHP_DPLL0_ID_OUT3`

```c
#define CLOCK_MCHP_DPLL0_ID_OUT3 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 3)
```

`DPLL0` 输出（Output）3 的时钟标识符（Clock ID）。

<a id="a3625ecaf031e005197b61a72e82a8f38"></a>

### `CLOCK_MCHP_DPLL0_ID_OUT4`

```c
#define CLOCK_MCHP_DPLL0_ID_OUT4 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 4)
```

`DPLL0` 输出（Output）4 的时钟标识符（Clock ID）。

<a id="a621a8f4faee2aa6d0d4d8af8609da0e9"></a>

### `CLOCK_MCHP_DPLL_ID_DPLL0`

```c
#define CLOCK_MCHP_DPLL_ID_DPLL0 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 1, 0)
```

`DPLL0` 时钟标识符（Clock ID）。

<a id="a535adb887a7c5c21a1a88f0bf450e5ed"></a>

### `CLOCK_MCHP_DPLL_ID_MAX`

```c
#define CLOCK_MCHP_DPLL_ID_MAX (0)
```

数字锁相环（DPLL）时钟标识符（Clock IDs）的最大索引。

<a id="a1d020421206c10005772bc3912989fa6"></a>

### `CLOCK_MCHP_DPLL_OUT_ID_MAX`

```c
#define CLOCK_MCHP_DPLL_OUT_ID_MAX (4)
```

DPLL 输出时钟标识符（Output Clock IDs）的最大索引。

<a id="adc730b78bbb79a2de524288fb8f2a90f"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN0`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN0 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 0)
```

通用时钟发生器（Generic Clock Generator）0 的标识符（ID）。

<a id="a7d1c402859c4f053d487b78002f0b16d"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN1`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN1 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 1)
```

通用时钟发生器（Generic Clock Generator）1 的标识符（ID）。

<a id="ab9a58178e0fd1faa6804f35709ac4e94"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN10`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN10 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 10)
```

通用时钟发生器（Generic Clock Generator）10 的标识符（ID）。

<a id="a8fad76e8d57aa754d1237f4fae8be6ed"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN11`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN11 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 11)
```

通用时钟发生器（Generic Clock Generator）11 的标识符（ID）。

<a id="a2dda06b2509f1d33896bf82927da6f84"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN2`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN2 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 2)
```

通用时钟发生器（Generic Clock Generator）2 的标识符（ID）。

<a id="ac6c91333d8e736f9c25c765f05f4be66"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN3`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN3 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 3)
```

通用时钟发生器（Generic Clock Generator）3 的标识符（ID）。

<a id="a6bd03b027dab2c82624de849d355e3c7"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN4`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN4 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 4)
```

通用时钟发生器（Generic Clock Generator）4 的标识符（ID）。

<a id="ae018b90957ec659f5225363264173348"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN5`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN5 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 5)
```

通用时钟发生器（Generic Clock Generator）5 的标识符（ID）。

<a id="a648ca2df6a086f43bbd79c76726b8acf"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN6`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN6 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 6)
```

通用时钟发生器（Generic Clock Generator）6 的标识符（ID）。

<a id="adcfc04767ae03fef19c1fa01adf73c60"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN7`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN7 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 7)
```

通用时钟发生器（Generic Clock Generator）7 的标识符（ID）。

<a id="a0e06ddf395b54a0c7b9b2d3f284e8449"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN8`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN8 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 8)
```

通用时钟发生器（Generic Clock Generator）8 的标识符（ID）。

<a id="a3da646cdf217d24807332b782c2056c9"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN9`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN9 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 9)
```

通用时钟发生器（Generic Clock Generator）9 的标识符（ID）。

<a id="a67296972320d7cb9295cd67c9cf25c54"></a>

### `CLOCK_MCHP_GCLKGEN_ID_MAX`

```c
#define CLOCK_MCHP_GCLKGEN_ID_MAX (11)
```

通用时钟发生器标识符（Generic Clock Generator IDs）的最大索引。

<a id="a8558308cb89c99326b165a7b12b14ff1"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_AC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_AC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 34, 36)
```

GCLK 外设标识符（Peripheral ID）：AC (模拟比较器)（AC (Analog Comparator)）。

<a id="a845a53053a861de67ebfa150bff389ff"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_ADC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 33, 35)
```

GCLK 外设标识符（Peripheral ID）：ADC（ADC）。

<a id="ae251d4719eb378734e3cb01c9f5828d8"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CAN0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 6, 4)
```

GCLK 外设标识符（Peripheral ID）：CAN0（CAN0）。

<a id="a2e77a06b25293f4152b0f2399ab32982"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CAN1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 7, 5)
```

GCLK 外设标识符（Peripheral ID）：CAN1（CAN1）。

<a id="ad49c597f4341f2f56e285e02b05e9563"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CCL0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CCL0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 36, 38)
```

GCLK 外设标识符（Peripheral ID）：CCL0（CCL0）。

<a id="abd2528ca834d9db6b7bc50e2005f0ed4"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CCL1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CCL1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 37, 39)
```

GCLK 外设标识符（Peripheral ID）：CCL1（CCL1）。

<a id="aeaeb9a032e3fa5a00199ef27c2a5ec30"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EIC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EIC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 5, 3)
```

GCLK 外设标识符（Peripheral ID）：外部中断控制器 (EIC)（External Interrupt Controller (EIC)）。

<a id="a31aa9472c7182d16249ba7950b452c14"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 8, 6)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 0（Event System Channel 0）。

<a id="a370930d5d12099ec34871a27cee5c8e2"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 9, 7)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 1（Event System Channel 1）。

<a id="aeb43cfd70588d9f660e8965516480191"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 16)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 10（Event System Channel 10）。

<a id="a93e2a650425a0bb9014c56d848c039bb"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 17)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 11（Event System Channel 11）。

<a id="a6966d71c9da4ce1803c48dc088818401"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 10, 8)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 2（Event System Channel 2）。

<a id="a5d98273862a2323e050874755da0c840"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 11, 9)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 3（Event System Channel 3）。

<a id="a24855b6b55dc3eb9efba6476d6d930e8"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 12, 10)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 4（Event System Channel 4）。

<a id="a6bb92b5d57c58e6b1ab083504bbb3756"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 13, 11)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 5（Event System Channel 5）。

<a id="ae2404c8e3bce6bd9b01903a9ad942d35"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 14, 12)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 6（Event System Channel 6）。

<a id="a852a5424cc73a5e75fcd7b151e7dd767"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 15, 13)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 7（Event System Channel 7）。

<a id="a9ff8a7f89700d95e431e6d0c12869b56"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 16, 14)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 8（Event System Channel 8）。

<a id="ad7112111ef68955636866ec0adb0e71e"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 17, 15)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 9（Event System Channel 9）。

<a id="a9447de6351b7f09b6a30d8df8e586d85"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 2, 0)
```

GCLK 外设标识符（Peripheral ID）：频率计测量 0（Frequency Meter Measure 0）。

<a id="ac6fc7ade933679db0f47c23fb27c6988"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 3, 1)
```

GCLK 外设标识符（Peripheral ID）：频率计测量 1（Frequency Meter Measure 1）。

<a id="a0da9e951ad59ea7ffa1b3a0586203202"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 4, 2)
```

GCLK 外设标识符（Peripheral ID）：频率计参考（Frequency Meter Reference）。

<a id="a9fb0644f504a830a4e324f792815ae98"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_MAX`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_MAX (40)
```

GCLK 外设标识符（Peripheral IDs）的最大索引。

<a id="a65c9bc79d0b5edd7dcc8a6178a600127"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_PTC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_PTC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 35, 37)
```

GCLK 外设标识符（Peripheral ID）：PTC (外设触摸控制器)（PTC (Peripheral Touch Controller)）。

<a id="a88f1128166176ebfc0a41dd496186300"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 21, 22)
```

GCLK 外设标识符（Peripheral ID）：SERCOM0 核心 时钟（SERCOM0 Core clock）。

<a id="a2bb7a4f72e45c2fb5f449b6b3f1b4520"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 18)
```

GCLK 外设标识符（Peripheral ID）：SERCOM0 慢速 时钟（SERCOM0 Slow clock）。

<a id="ab3ef99c62a821f4e5fe1f800de6561c2"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 22, 23)
```

GCLK 外设标识符（Peripheral ID）：SERCOM1 核心 时钟（SERCOM1 Core clock）。

<a id="a726fe192480ed57fbdc3e77cc1133c89"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 19)
```

GCLK 外设标识符（Peripheral ID）：SERCOM1 慢速 时钟（SERCOM1 Slow clock）。

<a id="ab0668a32e7385c8629b26cd396e6beaa"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 24)
```

GCLK 外设标识符（Peripheral ID）：SERCOM2 核心 时钟（SERCOM2 Core clock）。

<a id="a99d3f0a1c9e10f405c761ae6f3bf2744"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 20)
```

GCLK 外设标识符（Peripheral ID）：SERCOM2 慢速 时钟（SERCOM2 Slow clock）。

<a id="a155a02aa8799940dd0c59efac25e5bbc"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 25)
```

GCLK 外设标识符（Peripheral ID）：SERCOM3 核心 时钟（SERCOM3 Core clock）。

<a id="a08fb53b9b65e5743900bd6a4179925d3"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 21)
```

GCLK 外设标识符（Peripheral ID）：SERCOM3 慢速 时钟（SERCOM3 Slow clock）。

<a id="a77eb95730d000556c3b32a7bcf152913"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 28, 30)
```

GCLK 外设标识符（Peripheral ID）：SERCOM4 核心 时钟（SERCOM4 Core clock）。

<a id="a4b1126fa67b001d9d086874d8536fb48"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 29, 31)
```

GCLK 外设标识符（Peripheral ID）：SERCOM5 核心 时钟（SERCOM5 Core clock）。

<a id="af3614ec46e49df22dc37768df6e9c12b"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 26)
```

GCLK 外设标识符（Peripheral ID）：TCC0（TCC0）。

<a id="a253908d056c2ac97302065d9c0eb1cc4"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 27)
```

GCLK 外设标识符（Peripheral ID）：TCC1（TCC1）。

<a id="ae4ebf71771a1435faa34293290ed06f0"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC2`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 26, 28)
```

GCLK 外设标识符（Peripheral ID）：TCC2（TCC2）。

<a id="a363610cff7033e1bb7036d3b4ed21a0c"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC3`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 27, 29)
```

GCLK 外设标识符（Peripheral ID）：TCC3（TCC3）。

<a id="a341713f50727d73e4275cc093061487e"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC4`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 30, 32)
```

GCLK 外设标识符（Peripheral ID）：TCC4（TCC4）。

<a id="a1cb0b9600a335a01ff00c7eaa64a1229"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC5`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 31, 33)
```

GCLK 外设标识符（Peripheral ID）：TCC5（TCC5）。

<a id="a14a655c0aead0534f6915a1994a6ed1d"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC6`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 32, 34)
```

GCLK 外设标识符（Peripheral ID）：TCC6（TCC6）。

<a id="a566c7babd5641f337fc00adb20367833"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_USB`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_USB MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 38, 40)
```

GCLK 外设标识符（Peripheral ID）：USB（USB）。

<a id="ac40643badee3512255e142465f0f31b4"></a>

### `CLOCK_MCHP_MCLKDOMAIN_ID_CPU`

```c
#define CLOCK_MCHP_MCLKDOMAIN_ID_CPU MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 0)
```

主时钟域标识符（Main Clock Domain ID）：CPU。

<a id="adec6556749cbc3c25b049fd700c36e94"></a>

### `CLOCK_MCHP_MCLKDOMAIN_MAX`

```c
#define CLOCK_MCHP_MCLKDOMAIN_MAX (0)
```

主时钟域标识符（Main Clock Domain IDs）的最大索引。

<a id="a15b5103e5212ada5ae5da15831345e2a"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_AC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_AC MCHP_CLOCK_DERIVE_ID(9, 1, 18, 0x3f, 43)
```

MCLK 外设标识符（Peripheral ID）：AC（AC）。

<a id="a5d8481769aaec20ff21d47d3ac1347e3"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_ADC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_ADC MCHP_CLOCK_DERIVE_ID(9, 1, 17, 0x3f, 42)
```

MCLK 外设标识符（Peripheral ID）：ADC（ADC）。

<a id="aa1a035c7f4ff1b0a1f9ef7157f38a6b5"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_AT`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_AT MCHP_CLOCK_DERIVE_ID(9, 1, 24, 0x3f, 49)
```

MCLK 外设标识符（Peripheral ID）：AT（AT）。

<a id="a574a3cc55f7a8bf32a82232e293a29bc"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_BROMC_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BROMC_AHB MCHP_CLOCK_DERIVE_ID(9, 1, 0, 0x3f, 25)
```

MCLK 外设标识符（Peripheral ID）：BROMC (AHB)（BROMC (AHB)）。

<a id="a8bad753f6086aaa0288d62dc773fb2d1"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_BROMC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BROMC_APB MCHP_CLOCK_DERIVE_ID(9, 1, 1, 0x3f, 26)
```

MCLK 外设标识符（Peripheral ID）：BROMC (APB)（BROMC (APB)）。

<a id="a4188938454ae1ed53076aaf4def7f39e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CAN0`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN0 MCHP_CLOCK_DERIVE_ID(9, 0, 23, 0x3f, 16)
```

MCLK 外设标识符（Peripheral ID）：CAN0（CAN0）。

<a id="af9fc7781311291889227f80a8af51a76"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CAN1`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN1 MCHP_CLOCK_DERIVE_ID(9, 0, 24, 0x3f, 17)
```

MCLK 外设标识符（Peripheral ID）：CAN1（CAN1）。

<a id="af7b9a675b06b90d460e54af43fb54f62"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CCL0`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CCL0 MCHP_CLOCK_DERIVE_ID(9, 1, 20, 0x3f, 45)
```

MCLK 外设标识符（Peripheral ID）：CCL0（CCL0）。

<a id="a72406d795f45e47145cb9148799de080"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CCL1`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CCL1 MCHP_CLOCK_DERIVE_ID(9, 1, 21, 0x3f, 46)
```

MCLK 外设标识符（Peripheral ID）：CCL1（CCL1）。

<a id="a1ea38f3f64ebc1ec538530a23920f45d"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DMAC_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 28, 0x3f, 21)
```

MCLK 外设标识符（Peripheral ID）：DMAC (AHB)（DMAC (AHB)）。

<a id="ae0a16f13ccf85d54ebc961054850376c"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DMAC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_APB MCHP_CLOCK_DERIVE_ID(9, 0, 29, 0x3f, 22)
```

MCLK 外设标识符（Peripheral ID）：DMAC (APB)（DMAC (APB)）。

<a id="a5f1c9309e3eb0586eb1f765536b4346e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 0, 0x3f, 0)
```

MCLK 外设标识符（Peripheral ID）：DSU (AHB)（DSU (AHB)）。

<a id="afb137dc52e627ab615dea380c58a44da"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_EIC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EIC MCHP_CLOCK_DERIVE_ID(9, 0, 13, 0x3f, 11)
```

MCLK 外设标识符（Peripheral ID）：EIC（EIC）。

<a id="a1f3f4077f0f5be1dd872c8a18052317e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_EVSYS`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EVSYS MCHP_CLOCK_DERIVE_ID(9, 1, 3, 0x3f, 28)
```

MCLK 外设标识符（Peripheral ID）：EVSYS（EVSYS）。

<a id="af85028f923174b11e44d1fc9043c5c75"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 1, 0x3f, 1)
```

MCLK 外设标识符（Peripheral ID）：FCR (AHB)（FCR (AHB)）。

<a id="a55391bcfa4db8dfdf6d7fbfbfbc9626f"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 2, 0x3f, 2)
```

MCLK 外设标识符（Peripheral ID）：FCW (AHB)（FCW (AHB)）。

<a id="a37509ecf92c06e1f063a8c78c8fa0fe7"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FREQM`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FREQM MCHP_CLOCK_DERIVE_ID(9, 0, 10, 0x3f, 8)
```

MCLK 外设标识符（Peripheral ID）：FREQM（FREQM）。

<a id="a99453d72ee3d6a66ad85d009f6c3d9bd"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_H2PB0_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB0_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 25, 0x3f, 18)
```

MCLK 外设标识符（Peripheral ID）：H2PB0 (AHB)（H2PB0 (AHB)）。

<a id="a53cd4e5390a70155b5062e52642c6d63"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_H2PB0_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB0_APB MCHP_CLOCK_DERIVE_ID(9, 0, 26, 0x3f, 19)
```

MCLK 外设标识符（Peripheral ID）：H2PB0 (APB)（H2PB0 (APB)）。

<a id="a60942f65bae6aaea4ca522e428129485"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_H2PB1_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB1_AHB MCHP_CLOCK_DERIVE_ID(9, 1, 25, 0x3f, 50)
```

MCLK 外设标识符（Peripheral ID）：H2PB1_AHB（H2PB1_AHB）。

<a id="ac7212a639e29b519b89824b69f1f794c"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_H2PB1_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB1_APB MCHP_CLOCK_DERIVE_ID(9, 1, 26, 0x3f, 51)
```

MCLK 外设标识符（Peripheral ID）：H2PB1_APB（H2PB1_APB）。

<a id="ae3634155142a10632b80dd498221e215"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_H2PB2_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB2_AHB MCHP_CLOCK_DERIVE_ID(9, 1, 27, 0x3f, 52)
```

MCLK 外设标识符（Peripheral ID）：H2PB2_AHB（H2PB2_AHB）。

<a id="a0796bf3dd83dd952a5d2c871363946dc"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_H2PB2_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_H2PB2_APB MCHP_CLOCK_DERIVE_ID(9, 1, 28, 0x3f, 53)
```

MCLK 外设标识符（Peripheral ID）：H2PB2_APB（H2PB2_APB）。

<a id="a9f2830ece9477f6092119a42fec6b434"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_HMATRIX2_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HMATRIX2_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 30, 0x3f, 23)
```

MCLK 外设标识符（Peripheral ID）：HMATRIX2 (AHB)（HMATRIX2 (AHB)）。

<a id="a1857f3b332085910127c68b7ecb6bc8b"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_HMATRIX2_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HMATRIX2_APB MCHP_CLOCK_DERIVE_ID(9, 0, 31, 0x3f, 24)
```

MCLK 外设标识符（Peripheral ID）：HMATRIX2 (APB)（HMATRIX2 (APB)）。

<a id="a7d9495c1ea1942c4d2fc069a29e23d6a"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_HSM`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HSM MCHP_CLOCK_DERIVE_ID(9, 1, 30, 0x3f, 54)
```

MCLK 外设标识符（Peripheral ID）：HSM（HSM）。

<a id="a0154852bd2224c7a6707bc78b6f6ed3b"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_IDAU`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_IDAU MCHP_CLOCK_DERIVE_ID(9, 1, 2, 0x3f, 27)
```

MCLK 外设标识符（Peripheral ID）：IDAU（IDAU）。

<a id="a5884aa8fb4b6841cf3b36f8df64136d1"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_MAX`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MAX (55)
```

MCLK 外设标识符（Peripheral IDs）的最大索引。

<a id="ac150a2e0461227827858435745496711"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 22, 0x3f, 15)
```

MCLK 外设标识符（Peripheral ID）：MCRAMC_AHB（MCRAMC_AHB）。

<a id="a62ee930ec74fb592e2e1ead390e5670a"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC_APB MCHP_CLOCK_DERIVE_ID(9, 0, 21, 0x3f, 14)
```

MCLK 外设标识符（Peripheral ID）：MCRAMC_APB（MCRAMC_APB）。

<a id="a721267129ed0b4edf349298f972ae3af"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL MCHP_CLOCK_DERIVE_ID(9, 0, 7, 0x3f, 7)
```

MCLK 外设标识符（Peripheral ID）：OSC32KCTRL（OSC32KCTRL）。

<a id="af4fe59e6405058b34f7205f58631c38e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL MCHP_CLOCK_DERIVE_ID(9, 0, 6, 0x3f, 6)
```

MCLK 外设标识符（Peripheral ID）：OSCCTRL（OSCCTRL）。

<a id="a574e9bee5faec84626fa1e9ef679e71a"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB MCHP_CLOCK_DERIVE_ID(9, 0, 14, 0x3f, 12)
```

MCLK 外设标识符（Peripheral ID）：PAC (APB)（PAC (APB)）。

<a id="a4f661f6845c462308dbd9dc635eb0216"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PM`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PM MCHP_CLOCK_DERIVE_ID(9, 0, 3, 0x3f, 3)
```

MCLK 外设标识符（Peripheral ID）：PM（PM）。

<a id="acadb93a9913d4622db5b6e0b7d375ef1"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB MCHP_CLOCK_DERIVE_ID(9, 0, 27, 0x3f, 20)
```

MCLK 外设标识符（Peripheral ID）：PORT (APB)（PORT (APB)）。

<a id="a839339c5809445addd8326f7f3988c96"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PTC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PTC MCHP_CLOCK_DERIVE_ID(9, 1, 19, 0x3f, 44)
```

MCLK 外设标识符（Peripheral ID）：PTC（PTC）。

<a id="a28446fa9da2b5261abbd15da2368fcf1"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PUF`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PUF MCHP_CLOCK_DERIVE_ID(9, 1, 31, 0x3f, 55)
```

MCLK 外设标识符（Peripheral ID）：PUF（PUF）。

<a id="abf5fe57afad6b6d3f88cf4165406c468"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_RSTC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RSTC MCHP_CLOCK_DERIVE_ID(9, 0, 5, 0x3f, 5)
```

MCLK 外设标识符（Peripheral ID）：RSTC（RSTC）。

<a id="ab7ce87ea60b62f5a3d77297cd1d7d713"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_RTC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RTC MCHP_CLOCK_DERIVE_ID(9, 0, 12, 0x3f, 10)
```

MCLK 外设标识符（Peripheral ID）：RTC（RTC）。

<a id="aaca27bd670359e191ee3ded852b86e9b"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0 MCHP_CLOCK_DERIVE_ID(9, 1, 4, 0x3f, 29)
```

MCLK 外设标识符（Peripheral ID）：SERCOM0（SERCOM0）。

<a id="ad61fa9b33a8ea563a180c95213ad1d9b"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1 MCHP_CLOCK_DERIVE_ID(9, 1, 5, 0x3f, 30)
```

MCLK 外设标识符（Peripheral ID）：SERCOM1（SERCOM1）。

<a id="a75fb3dc587c912a5a961dfcd61066e09"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2 MCHP_CLOCK_DERIVE_ID(9, 1, 6, 0x3f, 31)
```

MCLK 外设标识符（Peripheral ID）：SERCOM2（SERCOM2）。

<a id="a893c130bcc447db2b076b694614be658"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3 MCHP_CLOCK_DERIVE_ID(9, 1, 7, 0x3f, 32)
```

MCLK 外设标识符（Peripheral ID）：SERCOM3（SERCOM3）。

<a id="ab86030aa3e1e599bbc46211ca4044488"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4 MCHP_CLOCK_DERIVE_ID(9, 1, 12, 0x3f, 37)
```

MCLK 外设标识符（Peripheral ID）：SERCOM4（SERCOM4）。

<a id="ae99c49a5fc48f51bc151d03d8f383cc6"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5 MCHP_CLOCK_DERIVE_ID(9, 1, 13, 0x3f, 38)
```

MCLK 外设标识符（Peripheral ID）：SERCOM5（SERCOM5）。

<a id="a5ae4a436c06ce604b358096d14213da8"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SUPC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SUPC MCHP_CLOCK_DERIVE_ID(9, 0, 4, 0x3f, 4)
```

MCLK 外设标识符（Peripheral ID）：SUPC（SUPC）。

<a id="ad3a8bd23b104522ca890997304fc21d4"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC0`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC0 MCHP_CLOCK_DERIVE_ID(9, 1, 8, 0x3f, 33)
```

MCLK 外设标识符（Peripheral ID）：TCC0（TCC0）。

<a id="ad60be2a1615dfd0de08bb0960e4e4526"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC1`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC1 MCHP_CLOCK_DERIVE_ID(9, 1, 9, 0x3f, 34)
```

MCLK 外设标识符（Peripheral ID）：TCC1（TCC1）。

<a id="a7f0be35a75e900699a10445d7a8463ca"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC2`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC2 MCHP_CLOCK_DERIVE_ID(9, 1, 10, 0x3f, 35)
```

MCLK 外设标识符（Peripheral ID）：TCC2（TCC2）。

<a id="a1c25975110ff6f0a977adb760c3eef7e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC3`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC3 MCHP_CLOCK_DERIVE_ID(9, 1, 11, 0x3f, 36)
```

MCLK 外设标识符（Peripheral ID）：TCC3（TCC3）。

<a id="af79ecdecbec732ce71599f0311d57580"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC4`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC4 MCHP_CLOCK_DERIVE_ID(9, 1, 14, 0x3f, 39)
```

MCLK 外设标识符（Peripheral ID）：TCC4（TCC4）。

<a id="ab84c014f1edb2bc7e374a3f82c2ef71d"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC5`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC5 MCHP_CLOCK_DERIVE_ID(9, 1, 15, 0x3f, 40)
```

MCLK 外设标识符（Peripheral ID）：TCC5（TCC5）。

<a id="ae95d523e3ad45348066f68fb19622aba"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC6`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC6 MCHP_CLOCK_DERIVE_ID(9, 1, 16, 0x3f, 41)
```

MCLK 外设标识符（Peripheral ID）：TCC6（TCC6）。

<a id="a9d398dd236236c3fa38dd3f4d3e79c10"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TRAM`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TRAM MCHP_CLOCK_DERIVE_ID(9, 0, 15, 0x3f, 13)
```

MCLK 外设标识符（Peripheral ID）：TRAM（TRAM）。

<a id="aed4f4cc3736914dd59e481ad37710868"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_USB_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_USB_AHB MCHP_CLOCK_DERIVE_ID(9, 1, 22, 0x3f, 47)
```

MCLK 外设标识符（Peripheral ID）：USB_AHB（USB_AHB）。

<a id="aae27b56b768f9c68bfb39f8a6ea3bd34"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_USB_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_USB_APB MCHP_CLOCK_DERIVE_ID(9, 1, 23, 0x3f, 48)
```

MCLK 外设标识符（Peripheral ID）：USB_APB（USB_APB）。

<a id="a75aeee838d3138dcf67732e62cd3d879"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_WDT`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_WDT MCHP_CLOCK_DERIVE_ID(9, 0, 11, 0x3f, 9)
```

MCLK 外设标识符（Peripheral ID）：WDT（WDT）。

<a id="aed47d2a2eccaea5ed5f5e99fa41afbbb"></a>

### `CLOCK_MCHP_RTC_ID`

```c
#define CLOCK_MCHP_RTC_ID MCHP_CLOCK_DERIVE_ID(4, 0x3f, 0x3f, 0x3f, 0)
```

实时时钟计数器（Real-Time Counter，RTC）的时钟标识符（Clock ID）。

<a id="aa6dc48a4e2e1047734e02f8c060e9369"></a>

### `CLOCK_MCHP_RTC_ID_MAX`

```c
#define CLOCK_MCHP_RTC_ID_MAX (0)
```

RTC 时钟标识符（Clock IDs）的最大索引。

<a id="a3262be48f6349821c62498b0521226ff"></a>

### `CLOCK_MCHP_XOSC32K_ID`

```c
#define CLOCK_MCHP_XOSC32K_ID MCHP_CLOCK_DERIVE_ID(5, 0x3f, 0x3f, 0x3f, 0)
```

32 kHz 外部振荡器（External Oscillator，XOSC32K）的时钟标识符（Clock ID）。

<a id="a09e1e2095d902fe6c82d7992a2eac5da"></a>

### `CLOCK_MCHP_XOSC32K_ID_MAX`

```c
#define CLOCK_MCHP_XOSC32K_ID_MAX (0)
```

XOSC32K 时钟标识符（Clock IDs）的最大索引。

<a id="a201012bb3a82a346aa0a98a5de91f320"></a>

### `CLOCK_MCHP_XOSC_ID`

```c
#define CLOCK_MCHP_XOSC_ID MCHP_CLOCK_DERIVE_ID(0, 0x3f, 0x3f, 0x3f, 0)
```

外部振荡器（External Oscillator，XOSC）的时钟标识符（Clock ID）。

<a id="a301af797e998ab83173d2a2e66a1ea38"></a>

### `CLOCK_MCHP_XOSC_ID_MAX`

```c
#define CLOCK_MCHP_XOSC_ID_MAX (0)
```

XOSC 时钟标识符（Clock IDs）的最大索引。

<a id="a0ebea68f214a63653aa0eaab0cf9c419"></a>

### `MCHP_CLOCK_DERIVE_ID`

```c
#define MCHP_CLOCK_DERIVE_ID ( type, mclkmaskreg, mclkmaskbit, gclkperiph, inst )
```

展开值（Value）：

```c
(((type) << 26) | ((mclkmaskreg) << 20) | ((mclkmaskbit) << 14) | ((gclkperiph) << 8) |    \
 inst)
```

生成一个 32 位时钟子系统标识符（Clock Subsystem Identifier）。

将时钟子系统类型（Clock Subsystem Type）、MCLK 总线信息（Bus Information）、GCLK 外设通道（Peripheral Channel）和实例编号（Instance Number）编码为一个 32 位标识符。

位字段布局（Bit Field Layout）：

- 位 `00..07`（8 位）：`inst`（实例）。
- 位 `08..13`（6 位）：`gclkperiph`（GCLK 外设），取值 `0–47`。
- 位 `14..19`（6 位）：`mclkmaskbit`（MCLK 掩码位），取值 `0–31`。
- 位 20..25（6 位）：`mclkmaskreg`，取值为 `MCLKMSK0`（0）、`MCLKMSK1`（1）或 `MCLKMSK2`（2）。
- 位 26..31（6 位）：`type`，取值为 `SUBSYS_TYPE_XOSC`（0）、`SUBSYS_TYPE_DFLL48M`（1）、`SUBSYS_TYPE_DPLL`（2）、`SUBSYS_TYPE_DPLL_OUT`（3）、`SUBSYS_TYPE_RTC`（4）、`SUBSYS_TYPE_XOSC32K`（5）、`SUBSYS_TYPE_GCLKGEN`（6）、`SUBSYS_TYPE_GCLKPERIPH`（7）、`SUBSYS_TYPE_MCLKDOMAIN`（8）或 `SUBSYS_TYPE_MCLKPERIPH`（9）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 时钟子系统类型（Clock Subsystem Type）。 |
| `mclkmaskreg` | 从 AHBx 和 APBx 总线（Buses）中选择。 |
| `mclkmaskbit` | 选择连接到 AHBx 或 APBx 总线的模块（Module），范围 `0–31`。 |
| `gclkperiph` | `PCHTRLm` 中的 GCLK 外设通道编号（Peripheral Channel Number）`m`，范围为 `0–63`。 |
| `inst` | 指定时钟类型（Clock Type）的实例编号（Instance Number）。 |

**返回（Returns）**：返回值（Returns）：编码后的时钟子系统标识符（Encoded Clock Subsystem Identifier）。


## 3.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P502_mchp_pic32cm_sg_gc_clock.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P002_zephyr__dt-bindings__clock__mchp_pic32ck_sg_gc_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__dt-bindings__clock__mchp_pic32cz_ca_clock.h_文件参考.md)
