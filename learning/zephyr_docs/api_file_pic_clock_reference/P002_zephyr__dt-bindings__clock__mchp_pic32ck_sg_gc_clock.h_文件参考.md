---
id: learning.zephyr-docs.api-file-pic-clock-reference.page-2
title: zephyr__dt-bindings__clock__mchp_pic32ck_sg_gc_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32ck__sg__gc__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_dt-bindings\_\_clock\_\_mchp\_pic32ck\_sg\_gc\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32ck__sg__gc__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

列出pic32ck_sg_gc系列的时钟子系统ID（Clock Subsystem IDs）。

查看此文件的源码。

<a id="details"></a>

列出 `pic32ck_sg_gc` 系列的时钟子系统标识符（Clock Subsystem IDs）。这些标识符用于设备树节点（Devicetree Nodes），也用作时钟 API 的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

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

### PLL_TYPE 时钟标识符（Clock IDs）

<a id="r_acd48cc8da0678862a2d8e0af37799e1e"></a>

```c
#define CLOCK_MCHP_PLL_ID_PLL0 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 0, 0)
```

相关声明：[CLOCK_MCHP_PLL_ID_PLL0](#acd48cc8da0678862a2d8e0af37799e1e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`PLL0` 时钟标识符（Clock ID）。

<a id="r_a5ef027c132316e0aa9fe06cc2e0f3b63"></a>

```c
#define CLOCK_MCHP_PLL_ID_MAX (0)
```

相关声明：[CLOCK_MCHP_PLL_ID_MAX](#a5ef027c132316e0aa9fe06cc2e0f3b63)。

锁相环（PLL）时钟标识符（Clock IDs）的最大索引。

<a id="define-members-3"></a>

### PLL_OUT_TYPE 时钟标识符（Clock IDs）

<a id="r_a12ddd4213583b011cf2ec8e5802ac3f2"></a>

```c
#define CLOCK_MCHP_PLL0_ID_OUT0 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 0)
```

相关声明：[CLOCK_MCHP_PLL0_ID_OUT0](#a12ddd4213583b011cf2ec8e5802ac3f2)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`PLL0` 输出（Output）0 的时钟标识符（Clock ID）。

<a id="r_a24937208d2f707d32917b2293fe9e9e3"></a>

```c
#define CLOCK_MCHP_PLL0_ID_OUT1 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 1)
```

相关声明：[CLOCK_MCHP_PLL0_ID_OUT1](#a24937208d2f707d32917b2293fe9e9e3)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`PLL0` 输出（Output）1 的时钟标识符（Clock ID）。

<a id="r_a9d67b9354cc244fc98303556530d711f"></a>

```c
#define CLOCK_MCHP_PLL0_ID_OUT2 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 2)
```

相关声明：[CLOCK_MCHP_PLL0_ID_OUT2](#a9d67b9354cc244fc98303556530d711f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`PLL0` 输出（Output）2 的时钟标识符（Clock ID）。

<a id="r_aaba7d7ef85c02109d97d6c1098f84bc8"></a>

```c
#define CLOCK_MCHP_PLL0_ID_OUT3 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 3)
```

相关声明：[CLOCK_MCHP_PLL0_ID_OUT3](#aaba7d7ef85c02109d97d6c1098f84bc8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`PLL0` 输出（Output）3 的时钟标识符（Clock ID）。

<a id="r_a8c05b54dae36aa1f2c04a5dd05d12531"></a>

```c
#define CLOCK_MCHP_PLL0_ID_OUT4 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 4)
```

相关声明：[CLOCK_MCHP_PLL0_ID_OUT4](#a8c05b54dae36aa1f2c04a5dd05d12531)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`PLL0` 输出（Output）4 的时钟标识符（Clock ID）。

<a id="r_aa71217a134f7ad7b2ec49463fcf739f1"></a>

```c
#define CLOCK_MCHP_PLL0_ID_OUT5 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 5)
```

相关声明：[CLOCK_MCHP_PLL0_ID_OUT5](#aa71217a134f7ad7b2ec49463fcf739f1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`PLL0` 输出（Output）5 的时钟标识符（Clock ID）。

<a id="r_a1566da9a6867acb8da4a3e4cf7e7ab5d"></a>

```c
#define CLOCK_MCHP_PLL0_OUT_ID_MAX (5)
```

相关声明：[CLOCK_MCHP_PLL0_OUT_ID_MAX](#a1566da9a6867acb8da4a3e4cf7e7ab5d)。

PLL0 输出时钟标识符（Output Clock IDs）的最大索引。

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

<a id="r_a31aa9472c7182d16249ba7950b452c14"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 6, 4)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0](#a31aa9472c7182d16249ba7950b452c14)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 0（Event System Channel 0）。

<a id="r_a370930d5d12099ec34871a27cee5c8e2"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 7, 5)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1](#a370930d5d12099ec34871a27cee5c8e2)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 1（Event System Channel 1）。

<a id="r_a6966d71c9da4ce1803c48dc088818401"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 8, 6)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2](#a6966d71c9da4ce1803c48dc088818401)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 2（Event System Channel 2）。

<a id="r_a5d98273862a2323e050874755da0c840"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 9, 7)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3](#a5d98273862a2323e050874755da0c840)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 3（Event System Channel 3）。

<a id="r_a24855b6b55dc3eb9efba6476d6d930e8"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 10, 8)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4](#a24855b6b55dc3eb9efba6476d6d930e8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 4（Event System Channel 4）。

<a id="r_a6bb92b5d57c58e6b1ab083504bbb3756"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 11, 9)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5](#a6bb92b5d57c58e6b1ab083504bbb3756)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 5（Event System Channel 5）。

<a id="r_ae2404c8e3bce6bd9b01903a9ad942d35"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 12, 10)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6](#ae2404c8e3bce6bd9b01903a9ad942d35)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 6（Event System Channel 6）。

<a id="r_a852a5424cc73a5e75fcd7b151e7dd767"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 13, 11)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7](#a852a5424cc73a5e75fcd7b151e7dd767)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 7（Event System Channel 7）。

<a id="r_a9ff8a7f89700d95e431e6d0c12869b56"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 14, 12)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8](#a9ff8a7f89700d95e431e6d0c12869b56)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 8（Event System Channel 8）。

<a id="r_ad7112111ef68955636866ec0adb0e71e"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 15, 13)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9](#ad7112111ef68955636866ec0adb0e71e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 9（Event System Channel 9）。

<a id="r_aeb43cfd70588d9f660e8965516480191"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 16, 14)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10](#aeb43cfd70588d9f660e8965516480191)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 10（Event System Channel 10）。

<a id="r_a93e2a650425a0bb9014c56d848c039bb"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 17, 15)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11](#a93e2a650425a0bb9014c56d848c039bb)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 11（Event System Channel 11）。

<a id="r_af5855721c29be7a03686059ae3ca7f5e"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 16)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SDMMC0_SLOW](#af5855721c29be7a03686059ae3ca7f5e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SDMMC0 慢速 时钟（SDMMC0 Slow Clock）。

<a id="r_a1f495a4359379169060d5e1ac071aa1c"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 17)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SDMMC1_SLOW](#a1f495a4359379169060d5e1ac071aa1c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SDMMC1 慢速 时钟（SDMMC1 Slow Clock）。

<a id="r_a2bb7a4f72e45c2fb5f449b6b3f1b4520"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 18)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW](#a2bb7a4f72e45c2fb5f449b6b3f1b4520)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM0 慢速 时钟（SERCOM0 Slow Clock）。

<a id="r_a726fe192480ed57fbdc3e77cc1133c89"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 19)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW](#a726fe192480ed57fbdc3e77cc1133c89)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM1 慢速 时钟（SERCOM1 Slow Clock）。

<a id="r_accbd9b23f933a8bae611a00019c5eb50"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 20)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_SLOW](#accbd9b23f933a8bae611a00019c5eb50)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM4 慢速 时钟（SERCOM4 Slow Clock）。

<a id="r_a99d3f0a1c9e10f405c761ae6f3bf2744"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 21)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW](#a99d3f0a1c9e10f405c761ae6f3bf2744)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM2 慢速 时钟（SERCOM2 Slow Clock）。

<a id="r_a08fb53b9b65e5743900bd6a4179925d3"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 22)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW](#a08fb53b9b65e5743900bd6a4179925d3)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM3 慢速 时钟（SERCOM3 Slow Clock）。

<a id="r_a680eff3630a7446292705a3c29098510"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 23)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_SLOW](#a680eff3630a7446292705a3c29098510)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM5 慢速 时钟（SERCOM5 Slow Clock）。

<a id="r_a8aaeb571901ab3b932c93aea8f67f39a"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 24)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_SLOW](#a8aaeb571901ab3b932c93aea8f67f39a)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM6 慢速 时钟（SERCOM6 Slow Clock）。

<a id="r_a277cd1054793077c5c67551bf4a38df5"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 25)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_SLOW](#a277cd1054793077c5c67551bf4a38df5)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM7 慢速 时钟（SERCOM7 Slow Clock）。

<a id="r_a88f1128166176ebfc0a41dd496186300"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 26)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE](#a88f1128166176ebfc0a41dd496186300)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM0 核心 时钟（SERCOM0 Core Clock）。

<a id="r_ab3ef99c62a821f4e5fe1f800de6561c2"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 27)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE](#ab3ef99c62a821f4e5fe1f800de6561c2)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM1 核心 时钟（SERCOM1 Core Clock）。

<a id="r_ab0668a32e7385c8629b26cd396e6beaa"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 21, 28)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE](#ab0668a32e7385c8629b26cd396e6beaa)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM2 核心 时钟（SERCOM2 Core Clock）。

<a id="r_a155a02aa8799940dd0c59efac25e5bbc"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 22, 29)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE](#a155a02aa8799940dd0c59efac25e5bbc)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM3 核心 时钟（SERCOM3 Core Clock）。

<a id="r_af3614ec46e49df22dc37768df6e9c12b"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 30)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC0](#af3614ec46e49df22dc37768df6e9c12b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC0（TCC0）。

<a id="r_a253908d056c2ac97302065d9c0eb1cc4"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 31)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC1](#a253908d056c2ac97302065d9c0eb1cc4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC1（TCC1）。

<a id="r_ae4ebf71771a1435faa34293290ed06f0"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 32)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC2](#ae4ebf71771a1435faa34293290ed06f0)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC2（TCC2）。

<a id="r_a363610cff7033e1bb7036d3b4ed21a0c"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 33)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC3](#a363610cff7033e1bb7036d3b4ed21a0c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC3（TCC3）。

<a id="r_a77eb95730d000556c3b32a7bcf152913"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 34)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE](#a77eb95730d000556c3b32a7bcf152913)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM4 核心 时钟（SERCOM4 Core Clock）。

<a id="r_a4b1126fa67b001d9d086874d8536fb48"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 26, 35)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE](#a4b1126fa67b001d9d086874d8536fb48)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM5 核心 时钟（SERCOM5 Core Clock）。

<a id="r_a8b7161f3cedb7e5e39cc5d98498e262c"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 27, 36)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE](#a8b7161f3cedb7e5e39cc5d98498e262c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM6 核心 时钟（SERCOM6 Core Clock）。

<a id="r_a12909dbedec1469b89c431395b9fb6eb"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 28, 37)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE](#a12909dbedec1469b89c431395b9fb6eb)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM7 核心 时钟（SERCOM7 Core Clock）。

<a id="r_a341713f50727d73e4275cc093061487e"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 29, 38)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC4](#a341713f50727d73e4275cc093061487e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC4（TCC4）。

<a id="r_a1cb0b9600a335a01ff00c7eaa64a1229"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 30, 39)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC5](#a1cb0b9600a335a01ff00c7eaa64a1229)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC5（TCC5）。

<a id="r_a14a655c0aead0534f6915a1994a6ed1d"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 31, 40)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC6](#a14a655c0aead0534f6915a1994a6ed1d)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC6（TCC6）。

<a id="r_a89967af8e20803cdb7e41890c4a4a143"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC7 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 32, 41)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC7](#a89967af8e20803cdb7e41890c4a4a143)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC7（TCC7）。

<a id="r_a845a53053a861de67ebfa150bff389ff"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 33, 42)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_ADC](#a845a53053a861de67ebfa150bff389ff)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：ADC（ADC）。

<a id="r_a8558308cb89c99326b165a7b12b14ff1"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_AC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 34, 43)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_AC](#a8558308cb89c99326b165a7b12b14ff1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：AC（AC）。

<a id="r_a65c9bc79d0b5edd7dcc8a6178a600127"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_PTC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 35, 44)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_PTC](#a65c9bc79d0b5edd7dcc8a6178a600127)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：PTC（PTC）。

<a id="r_a0730543904f07b779d0a4ecea9bb8b3e"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SPI_IXS MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 36, 45)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SPI_IXS](#a0730543904f07b779d0a4ecea9bb8b3e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SPI_IXS（SPI_IXS）。

<a id="r_a9f9af8bd8013d7536389a108851b0925"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CCL MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 37, 46)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CCL](#a9f9af8bd8013d7536389a108851b0925)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CCL（CCL）。

<a id="r_abf9396d20ea2356d9963326cab64df02"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_PDEC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 38, 47)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_PDEC](#abf9396d20ea2356d9963326cab64df02)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：PDEC（PDEC）。

<a id="r_ae251d4719eb378734e3cb01c9f5828d8"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 39, 48)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CAN0](#ae251d4719eb378734e3cb01c9f5828d8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CAN0（CAN0）。

<a id="r_a2e77a06b25293f4152b0f2399ab32982"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 40, 49)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CAN1](#a2e77a06b25293f4152b0f2399ab32982)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CAN1（CAN1）。

<a id="r_a43d835c163dac2527c083c001fffd9aa"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_ETH_TX MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 41, 50)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_ETH_TX](#a43d835c163dac2527c083c001fffd9aa)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：ETH_TX（ETH_TX）。

<a id="r_aa72adfa1befae033f3111e544978a621"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_ETH_TSU MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 42, 51)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_ETH_TSU](#aa72adfa1befae033f3111e544978a621)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：ETH_TSU（ETH_TSU）。

<a id="r_a1e5c49e89ef93f44610556597c2be205"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SQI MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 43, 52)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SQI](#a1e5c49e89ef93f44610556597c2be205)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SQI（SQI）。

<a id="r_a40318aa3aa6c1098d0432d2abfa46f0c"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 44, 53)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SDMMC0](#a40318aa3aa6c1098d0432d2abfa46f0c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SDMMC0（SDMMC0）。

<a id="r_a6c822629f1075df52bc4ba09021a9788"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 45, 54)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SDMMC1](#a6c822629f1075df52bc4ba09021a9788)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SDMMC1（SDMMC1）。

<a id="r_a566c7babd5641f337fc00adb20367833"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_USB MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 46, 55)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_USB](#a566c7babd5641f337fc00adb20367833)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：USB（USB）。

<a id="r_a5f974f3ec705d29f83a0c41aeeff0169"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CPU0_TRACE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 47, 56)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CPU0_TRACE](#a5f974f3ec705d29f83a0c41aeeff0169)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CPU0_TRACE（CPU0_TRACE）。

<a id="r_a9fb0644f504a830a4e324f792815ae98"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_MAX (56)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_MAX](#a9fb0644f504a830a4e324f792815ae98)。

GCLK 外设标识符（Peripheral IDs）的最大索引。

<a id="define-members-8"></a>

### MCLKDOMAIN_TYPE 时钟标识符（Clock IDs）

<a id="r_a6de8b0b73f5ad847d3b4a1c2898ba534"></a>

```c
#define CLOCK_MCHP_MCLKCPU_ID MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 0)
```

相关声明：[CLOCK_MCHP_MCLKCPU_ID](#a6de8b0b73f5ad847d3b4a1c2898ba534)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

主时钟域标识符（Main Clock Domain ID）：CPU。

<a id="r_ad164589a2abc31000c96bd45a7eac9ba"></a>

```c
#define CLOCK_MCHP_MCLKCPU_MAX (0)
```

相关声明：[CLOCK_MCHP_MCLKCPU_MAX](#ad164589a2abc31000c96bd45a7eac9ba)。

主时钟域标识符（Main Clock Domain IDs）的最大索引。

<a id="define-members-9"></a>

### MCLKPERIPH_TYPE 时钟标识符（Clock IDs）

<a id="r_a5f1c9309e3eb0586eb1f765536b4346e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 3, 0x3f, 0)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB](#a5f1c9309e3eb0586eb1f765536b4346e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DSU (AHB)（DSU (AHB)）。

<a id="r_af85028f923174b11e44d1fc9043c5c75"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 4, 0x3f, 1)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB](#af85028f923174b11e44d1fc9043c5c75)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FCR (AHB)（FCR (AHB)）。

<a id="r_a55391bcfa4db8dfdf6d7fbfbfbc9626f"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 5, 0x3f, 2)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB](#a55391bcfa4db8dfdf6d7fbfbfbc9626f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FCW (AHB)（FCW (AHB)）。

<a id="r_ad63bf9ad8a02a102f6cc0b4ebcecd8ae"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 6, 0x3f, 3)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PAC_AHB](#ad63bf9ad8a02a102f6cc0b4ebcecd8ae)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PAC (AHB)（PAC (AHB)）。

<a id="r_a98a4fedf80bb2756cf890d8c33dc98cf"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA0_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 8, 0x3f, 4)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DMA0_AHB](#a98a4fedf80bb2756cf890d8c33dc98cf)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DMA0 (AHB)（DMA0 (AHB)）。

<a id="r_aefad014e192ff33d0a75ed69d3e99997"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA1_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 9, 0x3f, 5)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DMA1_AHB](#aefad014e192ff33d0a75ed69d3e99997)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DMA1 (AHB)（DMA1 (AHB)）。

<a id="r_a362ebd80cf078c91d39f7e37078445a9"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PRM_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 12, 0x3f, 6)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PRM_AHB](#a362ebd80cf078c91d39f7e37078445a9)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PRM (AHB)（PRM (AHB)）。

<a id="r_a020e0dd01728bbb323fd174eccb1509f"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN0_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 13, 0x3f, 7)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CAN0_AHB](#a020e0dd01728bbb323fd174eccb1509f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CAN0 (AHB)（CAN0 (AHB)）。

<a id="r_a82eab8ef6506c116079b31528651ac8e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN1_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 14, 0x3f, 8)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CAN1_AHB](#a82eab8ef6506c116079b31528651ac8e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CAN1 (AHB)（CAN1 (AHB)）。

<a id="r_aa4f92ad099bb80accb050b39876688c3"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_ETH_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 15, 0x3f, 9)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_ETH_AHB](#aa4f92ad099bb80accb050b39876688c3)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：ETH (AHB)（ETH (AHB)）。

<a id="r_a29100f869118c250054725cdf72d58f8"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SQI_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 16, 0x3f, 10)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SQI_AHB](#a29100f869118c250054725cdf72d58f8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SQI (AHB)（SQI (AHB)）。

<a id="r_a4cd460b34dac65adf8e9c19fc7072149"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDMMC0_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 17, 0x3f, 11)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SDMMC0_AHB](#a4cd460b34dac65adf8e9c19fc7072149)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SDMMC0 (AHB)（SDMMC0 (AHB)）。

<a id="r_a0ff819df13afc3af15b8e593f9a027c4"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDMMC1_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 18, 0x3f, 12)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SDMMC1_AHB](#a0ff819df13afc3af15b8e593f9a027c4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SDMMC1 (AHB)（SDMMC1 (AHB)）。

<a id="r_a03f03076ce38c08aff0158f36e552bdb"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_USBFS_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 19, 0x3f, 13)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_USBFS_AHB](#a03f03076ce38c08aff0158f36e552bdb)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：USBFS (AHB)（USBFS (AHB)）。

<a id="r_a311c2b3b6b7c998cd03a0ad4caaf9b68"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_USBHS_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 20, 0x3f, 14)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_USBHS_AHB](#a311c2b3b6b7c998cd03a0ad4caaf9b68)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：USBHS (AHB)（USBHS (AHB)）。

<a id="r_ada6c6291b51b7fe41ee0925e31628ff9"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 21, 0x3f, 15)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_EBI_AHB](#ada6c6291b51b7fe41ee0925e31628ff9)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：EBI (AHB)（EBI (AHB)）。

<a id="r_a37acd5942b619f4410efdebad1a29651"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HSM_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 22, 0x3f, 16)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_HSM_AHB](#a37acd5942b619f4410efdebad1a29651)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：HSM (AHB)（HSM (AHB)）。

<a id="r_a25521d18a70eacc1ad5cc347feb0765e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_APB MCHP_CLOCK_DERIVE_ID(9, 1, 0, 0x3f, 17)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DSU_APB](#a25521d18a70eacc1ad5cc347feb0765e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DSU (APB)（DSU (APB)）。

<a id="r_a8427e8e5faebe7f66dbfe1554d024c6e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_APB MCHP_CLOCK_DERIVE_ID(9, 1, 1, 0x3f, 18)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FCR_APB](#a8427e8e5faebe7f66dbfe1554d024c6e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FCR (APB)（FCR (APB)）。

<a id="r_a979b800be2dabf8c744fef8295cf1bcc"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_APB MCHP_CLOCK_DERIVE_ID(9, 1, 2, 0x3f, 19)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FCW_APB](#a979b800be2dabf8c744fef8295cf1bcc)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FCW (APB)（FCW (APB)）。

<a id="r_acd7a900e83eb1f4440f1a3bb19b64c87"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RSTC_APB MCHP_CLOCK_DERIVE_ID(9, 1, 5, 0x3f, 20)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_RSTC_APB](#acd7a900e83eb1f4440f1a3bb19b64c87)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：RSTC (APB)（RSTC (APB)）。

<a id="r_af1c5abfaa99c29512de8ad86d50436fa"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL_APB MCHP_CLOCK_DERIVE_ID(9, 1, 6, 0x3f, 21)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL_APB](#af1c5abfaa99c29512de8ad86d50436fa)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：OSCCTRL (APB)（OSCCTRL (APB)）。

<a id="r_a1d56390d443e73b0a3ff50b5375d053d"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL_APB MCHP_CLOCK_DERIVE_ID(9, 1, 7, 0x3f, 22)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL_APB](#a1d56390d443e73b0a3ff50b5375d053d)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：OSC32KCTRL (APB)（OSC32KCTRL (APB)）。

<a id="r_a7683dd70a6fd67b23950255a318a92c5"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FREQM_APB MCHP_CLOCK_DERIVE_ID(9, 1, 10, 0x3f, 23)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FREQM_APB](#a7683dd70a6fd67b23950255a318a92c5)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FREQM (APB)（FREQM (APB)）。

<a id="r_aea2b6485e25c10b439400ce5104a7be6"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_WDT_APB MCHP_CLOCK_DERIVE_ID(9, 1, 11, 0x3f, 24)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_WDT_APB](#aea2b6485e25c10b439400ce5104a7be6)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：WDT (APB)（WDT (APB)）。

<a id="r_ad712b633caa2592437efda6d5fa9fddf"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RTC_APB MCHP_CLOCK_DERIVE_ID(9, 1, 12, 0x3f, 25)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_RTC_APB](#ad712b633caa2592437efda6d5fa9fddf)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：RTC (APB)（RTC (APB)）。

<a id="r_a96f372b19d6097849c37795933d0822f"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EIC_APB MCHP_CLOCK_DERIVE_ID(9, 1, 13, 0x3f, 26)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_EIC_APB](#a96f372b19d6097849c37795933d0822f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：EIC (APB)（EIC (APB)）。

<a id="r_a574e9bee5faec84626fa1e9ef679e71a"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB MCHP_CLOCK_DERIVE_ID(9, 1, 14, 0x3f, 27)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB](#a574e9bee5faec84626fa1e9ef679e71a)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PAC (APB)（PAC (APB)）。

<a id="r_a24b1be03ee41ef4d3e4ba72694d863b5"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TRAM_APB MCHP_CLOCK_DERIVE_ID(9, 1, 15, 0x3f, 28)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TRAM_APB](#a24b1be03ee41ef4d3e4ba72694d863b5)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TRAM (APB)（TRAM (APB)）。

<a id="r_a0d19557ec776183aa0734c97d38cdbc6"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MBISTINTF_APB MCHP_CLOCK_DERIVE_ID(9, 1, 18, 0x3f, 29)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_MBISTINTF_APB](#a0d19557ec776183aa0734c97d38cdbc6)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：MBISTINTF (APB)（MBISTINTF (APB)）。

<a id="r_ac8d026bae71eb4c033b8fd93b2e0fa2c"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TDM_APB MCHP_CLOCK_DERIVE_ID(9, 1, 19, 0x3f, 30)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TDM_APB](#ac8d026bae71eb4c033b8fd93b2e0fa2c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TDM (APB)（TDM (APB)）。

<a id="r_acadb93a9913d4622db5b6e0b7d375ef1"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB MCHP_CLOCK_DERIVE_ID(9, 2, 0, 0x3f, 31)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB](#acadb93a9913d4622db5b6e0b7d375ef1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PORT (APB)（PORT (APB)）。

<a id="r_a003cccbd09694978168d83d06b25995f"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA0_APB MCHP_CLOCK_DERIVE_ID(9, 2, 1, 0x3f, 32)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DMA0_APB](#a003cccbd09694978168d83d06b25995f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DMA0 (APB)（DMA0 (APB)）。

<a id="r_aea8d908b0ffd05877a425b9b5085b6c8"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA1_APB MCHP_CLOCK_DERIVE_ID(9, 2, 2, 0x3f, 33)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DMA1_APB](#aea8d908b0ffd05877a425b9b5085b6c8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DMA1 (APB)（DMA1 (APB)）。

<a id="r_a06eb4d6cb2bec066a15857648c259223"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PRM_APB MCHP_CLOCK_DERIVE_ID(9, 2, 4, 0x3f, 34)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PRM_APB](#a06eb4d6cb2bec066a15857648c259223)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PRM (APB)（PRM (APB)）。

<a id="r_ae43a1ae1b9502fa64d0f2d679937a759"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_IDAU_APB MCHP_CLOCK_DERIVE_ID(9, 2, 5, 0x3f, 35)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_IDAU_APB](#ae43a1ae1b9502fa64d0f2d679937a759)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：IDAU (APB)（IDAU (APB)）。

<a id="r_a0beb2098f964c3ca55a9dca232e2f280"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EVSYS_APB MCHP_CLOCK_DERIVE_ID(9, 2, 6, 0x3f, 36)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_EVSYS_APB](#a0beb2098f964c3ca55a9dca232e2f280)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：EVSYS (APB)（EVSYS (APB)）。

<a id="r_a47f3b5aa5a51664bb754a6bd409110a4"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0_APB MCHP_CLOCK_DERIVE_ID(9, 2, 7, 0x3f, 37)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0_APB](#a47f3b5aa5a51664bb754a6bd409110a4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM0 (APB)（SERCOM0 (APB)）。

<a id="r_af797c727eb17090ccefc52a22c5f5b51"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1_APB MCHP_CLOCK_DERIVE_ID(9, 2, 8, 0x3f, 38)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1_APB](#af797c727eb17090ccefc52a22c5f5b51)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM1 (APB)（SERCOM1 (APB)）。

<a id="r_ad809db56498079a4d2b01e393af7bd04"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2_APB MCHP_CLOCK_DERIVE_ID(9, 2, 9, 0x3f, 39)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2_APB](#ad809db56498079a4d2b01e393af7bd04)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM2 (APB)（SERCOM2 (APB)）。

<a id="r_aff58338e2aa80841b910bebca63ca132"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3_APB MCHP_CLOCK_DERIVE_ID(9, 2, 10, 0x3f, 40)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3_APB](#aff58338e2aa80841b910bebca63ca132)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM3 (APB)（SERCOM3 (APB)）。

<a id="r_a09ddda66170546df3264fa6630c21ad9"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC0_APB MCHP_CLOCK_DERIVE_ID(9, 2, 11, 0x3f, 41)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC0_APB](#a09ddda66170546df3264fa6630c21ad9)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC0 (APB)（TCC0 (APB)）。

<a id="r_a426ad19aeeb116ceed471a6ffbe27ba6"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC1_APB MCHP_CLOCK_DERIVE_ID(9, 2, 12, 0x3f, 42)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC1_APB](#a426ad19aeeb116ceed471a6ffbe27ba6)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC1 (APB)（TCC1 (APB)）。

<a id="r_a0c54ce51de3b7012abcfe6822cd81a58"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC2_APB MCHP_CLOCK_DERIVE_ID(9, 2, 13, 0x3f, 43)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC2_APB](#a0c54ce51de3b7012abcfe6822cd81a58)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC2 (APB)（TCC2 (APB)）。

<a id="r_a1e301cdd4b8a60bff8b52eff03dcd6e6"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC3_APB MCHP_CLOCK_DERIVE_ID(9, 2, 14, 0x3f, 44)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC3_APB](#a1e301cdd4b8a60bff8b52eff03dcd6e6)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC3 (APB)（TCC3 (APB)）。

<a id="r_a75c42c1ce5bd4831739973617e5fedd4"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4_APB MCHP_CLOCK_DERIVE_ID(9, 3, 0, 0x3f, 45)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4_APB](#a75c42c1ce5bd4831739973617e5fedd4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM4 (APB)（SERCOM4 (APB)）。

<a id="r_ac3f06e5a5b8a2d43465ff0ce073427e0"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5_APB MCHP_CLOCK_DERIVE_ID(9, 3, 1, 0x3f, 46)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5_APB](#ac3f06e5a5b8a2d43465ff0ce073427e0)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM5 (APB)（SERCOM5 (APB)）。

<a id="r_a22d35327a659f86f3bbd1b86dfbd0bdc"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM6_APB MCHP_CLOCK_DERIVE_ID(9, 3, 2, 0x3f, 47)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM6_APB](#a22d35327a659f86f3bbd1b86dfbd0bdc)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM6 (APB)（SERCOM6 (APB)）。

<a id="r_a476d7f837f1d5c092b9375864e895e7b"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM7_APB MCHP_CLOCK_DERIVE_ID(9, 3, 3, 0x3f, 48)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM7_APB](#a476d7f837f1d5c092b9375864e895e7b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM7 (APB)（SERCOM7 (APB)）。

<a id="r_a07f028c49e5174a320eba2f326c013b7"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC4_APB MCHP_CLOCK_DERIVE_ID(9, 3, 4, 0x3f, 49)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC4_APB](#a07f028c49e5174a320eba2f326c013b7)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC4 (APB)（TCC4 (APB)）。

<a id="r_ac08c3fbc66ec7948bb78a7bbea684467"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC5_APB MCHP_CLOCK_DERIVE_ID(9, 3, 5, 0x3f, 50)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC5_APB](#ac08c3fbc66ec7948bb78a7bbea684467)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC5 (APB)（TCC5 (APB)）。

<a id="r_aabe0b18cb49f214748847d1fd6c9b0d4"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC6_APB MCHP_CLOCK_DERIVE_ID(9, 3, 6, 0x3f, 51)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC6_APB](#aabe0b18cb49f214748847d1fd6c9b0d4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC6 (APB)（TCC6 (APB)）。

<a id="r_ab3e026a71c9ecbf0b7508e2d58d51485"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC7_APB MCHP_CLOCK_DERIVE_ID(9, 3, 7, 0x3f, 52)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC7_APB](#ab3e026a71c9ecbf0b7508e2d58d51485)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC7 (APB)（TCC7 (APB)）。

<a id="r_a09bd059dfc0f111ccf5f1f3149363ed6"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_ADC_APB MCHP_CLOCK_DERIVE_ID(9, 3, 8, 0x3f, 53)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_ADC_APB](#a09bd059dfc0f111ccf5f1f3149363ed6)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：ADC (APB)（ADC (APB)）。

<a id="r_affe3569727db011f6a21143af7b9e2a7"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_AC_APB MCHP_CLOCK_DERIVE_ID(9, 3, 9, 0x3f, 54)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_AC_APB](#affe3569727db011f6a21143af7b9e2a7)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：AC (APB)（AC (APB)）。

<a id="r_a31de65a5228c7021bef57eb9edef0ee8"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PTC_APB MCHP_CLOCK_DERIVE_ID(9, 3, 10, 0x3f, 55)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PTC_APB](#a31de65a5228c7021bef57eb9edef0ee8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PTC (APB)（PTC (APB)）。

<a id="r_a2c6f9bd6f15c1c2518c578d192e9917c"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_I2S_APB MCHP_CLOCK_DERIVE_ID(9, 3, 11, 0x3f, 56)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_I2S_APB](#a2c6f9bd6f15c1c2518c578d192e9917c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：I2S (APB)（I2S (APB)）。

<a id="r_aa7f5424b104ff218e0abc29c45709ef5"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PCC_APB MCHP_CLOCK_DERIVE_ID(9, 3, 12, 0x3f, 57)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PCC_APB](#aa7f5424b104ff218e0abc29c45709ef5)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PCC (APB)（PCC (APB)）。

<a id="r_a4f466eeed8fa57339509207c77fd6cf0"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CCL_APB MCHP_CLOCK_DERIVE_ID(9, 3, 13, 0x3f, 58)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CCL_APB](#a4f466eeed8fa57339509207c77fd6cf0)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CCL (APB)（CCL (APB)）。

<a id="r_ac97b177e0b4050c248416cbb09dc6693"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PDEC_APB MCHP_CLOCK_DERIVE_ID(9, 3, 14, 0x3f, 59)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PDEC_APB](#ac97b177e0b4050c248416cbb09dc6693)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PDEC (APB)（PDEC (APB)）。

<a id="r_aa6e14d78643d022467b3385bf930f349"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_ETH_APB MCHP_CLOCK_DERIVE_ID(9, 3, 15, 0x3f, 60)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_ETH_APB](#aa6e14d78643d022467b3385bf930f349)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：ETH (APB)（ETH (APB)）。

<a id="r_a1f0b24f209cc2aeba54f770d9ad6f045"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TRNG_APB MCHP_CLOCK_DERIVE_ID(9, 3, 16, 0x3f, 61)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TRNG_APB](#a1f0b24f209cc2aeba54f770d9ad6f045)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TRNG (APB)（TRNG (APB)）。

<a id="r_aae27b56b768f9c68bfb39f8a6ea3bd34"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_USB_APB MCHP_CLOCK_DERIVE_ID(9, 3, 17, 0x3f, 62)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_USB_APB](#aae27b56b768f9c68bfb39f8a6ea3bd34)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：USB (APB)（USB (APB)）。

<a id="r_a9fb89fb266e6bee7606a1de146a33d4f"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_APB MCHP_CLOCK_DERIVE_ID(9, 3, 18, 0x3f, 63)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_EBI_APB](#a9fb89fb266e6bee7606a1de146a33d4f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：EBI (APB)（EBI (APB)）。

<a id="r_a0819cfd2cae3f24367c9fda31718c240"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BSDAP_AHB MCHP_CLOCK_DERIVE_ID(9, 3, 19, 0x3f, 64)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_BSDAP_AHB](#a0819cfd2cae3f24367c9fda31718c240)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：BSDAP (AHB)（BSDAP (AHB)）。

<a id="r_a5884aa8fb4b6841cf3b36f8df64136d1"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MAX (64)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_MAX](#a5884aa8fb4b6841cf3b36f8df64136d1)。

MCLK 外设标识符（Peripheral IDs）的最大索引。

## 2.2\_详细说明（Detailed Documentation）

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
#define CLOCK_MCHP_GCLKPERIPH_ID_AC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 34, 43)
```

GCLK 外设标识符（Peripheral ID）：AC（AC）。

<a id="a845a53053a861de67ebfa150bff389ff"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_ADC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 33, 42)
```

GCLK 外设标识符（Peripheral ID）：ADC（ADC）。

<a id="ae251d4719eb378734e3cb01c9f5828d8"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CAN0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 39, 48)
```

GCLK 外设标识符（Peripheral ID）：CAN0（CAN0）。

<a id="a2e77a06b25293f4152b0f2399ab32982"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CAN1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 40, 49)
```

GCLK 外设标识符（Peripheral ID）：CAN1（CAN1）。

<a id="a9f9af8bd8013d7536389a108851b0925"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CCL`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CCL MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 37, 46)
```

GCLK 外设标识符（Peripheral ID）：CCL（CCL）。

<a id="a5f974f3ec705d29f83a0c41aeeff0169"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CPU0_TRACE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CPU0_TRACE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 47, 56)
```

GCLK 外设标识符（Peripheral ID）：CPU0_TRACE（CPU0_TRACE）。

<a id="aeaeb9a032e3fa5a00199ef27c2a5ec30"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EIC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EIC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 5, 3)
```

GCLK 外设标识符（Peripheral ID）：外部中断控制器 (EIC)（External Interrupt Controller (EIC)）。

<a id="aa72adfa1befae033f3111e544978a621"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_ETH_TSU`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_ETH_TSU MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 42, 51)
```

GCLK 外设标识符（Peripheral ID）：ETH_TSU（ETH_TSU）。

<a id="a43d835c163dac2527c083c001fffd9aa"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_ETH_TX`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_ETH_TX MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 41, 50)
```

GCLK 外设标识符（Peripheral ID）：ETH_TX（ETH_TX）。

<a id="a31aa9472c7182d16249ba7950b452c14"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 6, 4)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 0（Event System Channel 0）。

<a id="a370930d5d12099ec34871a27cee5c8e2"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 7, 5)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 1（Event System Channel 1）。

<a id="aeb43cfd70588d9f660e8965516480191"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 16, 14)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 10（Event System Channel 10）。

<a id="a93e2a650425a0bb9014c56d848c039bb"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 17, 15)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 11（Event System Channel 11）。

<a id="a6966d71c9da4ce1803c48dc088818401"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 8, 6)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 2（Event System Channel 2）。

<a id="a5d98273862a2323e050874755da0c840"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 9, 7)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 3（Event System Channel 3）。

<a id="a24855b6b55dc3eb9efba6476d6d930e8"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 10, 8)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 4（Event System Channel 4）。

<a id="a6bb92b5d57c58e6b1ab083504bbb3756"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 11, 9)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 5（Event System Channel 5）。

<a id="ae2404c8e3bce6bd9b01903a9ad942d35"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 12, 10)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 6（Event System Channel 6）。

<a id="a852a5424cc73a5e75fcd7b151e7dd767"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 13, 11)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 7（Event System Channel 7）。

<a id="a9ff8a7f89700d95e431e6d0c12869b56"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 14, 12)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 8（Event System Channel 8）。

<a id="ad7112111ef68955636866ec0adb0e71e"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 15, 13)
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
#define CLOCK_MCHP_GCLKPERIPH_ID_MAX (56)
```

GCLK 外设标识符（Peripheral IDs）的最大索引。

<a id="abf9396d20ea2356d9963326cab64df02"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_PDEC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_PDEC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 38, 47)
```

GCLK 外设标识符（Peripheral ID）：PDEC（PDEC）。

<a id="a65c9bc79d0b5edd7dcc8a6178a600127"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_PTC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_PTC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 35, 44)
```

GCLK 外设标识符（Peripheral ID）：PTC（PTC）。

<a id="a40318aa3aa6c1098d0432d2abfa46f0c"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SDMMC0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 44, 53)
```

GCLK 外设标识符（Peripheral ID）：SDMMC0（SDMMC0）。

<a id="af5855721c29be7a03686059ae3ca7f5e"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SDMMC0_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 16)
```

GCLK 外设标识符（Peripheral ID）：SDMMC0 慢速 时钟（SDMMC0 Slow Clock）。

<a id="a6c822629f1075df52bc4ba09021a9788"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SDMMC1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 45, 54)
```

GCLK 外设标识符（Peripheral ID）：SDMMC1（SDMMC1）。

<a id="a1f495a4359379169060d5e1ac071aa1c"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SDMMC1_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDMMC1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 17)
```

GCLK 外设标识符（Peripheral ID）：SDMMC1 慢速 时钟（SDMMC1 Slow Clock）。

<a id="a88f1128166176ebfc0a41dd496186300"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 26)
```

GCLK 外设标识符（Peripheral ID）：SERCOM0 核心 时钟（SERCOM0 Core Clock）。

<a id="a2bb7a4f72e45c2fb5f449b6b3f1b4520"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 18)
```

GCLK 外设标识符（Peripheral ID）：SERCOM0 慢速 时钟（SERCOM0 Slow Clock）。

<a id="ab3ef99c62a821f4e5fe1f800de6561c2"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 27)
```

GCLK 外设标识符（Peripheral ID）：SERCOM1 核心 时钟（SERCOM1 Core Clock）。

<a id="a726fe192480ed57fbdc3e77cc1133c89"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 19)
```

GCLK 外设标识符（Peripheral ID）：SERCOM1 慢速 时钟（SERCOM1 Slow Clock）。

<a id="ab0668a32e7385c8629b26cd396e6beaa"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 21, 28)
```

GCLK 外设标识符（Peripheral ID）：SERCOM2 核心 时钟（SERCOM2 Core Clock）。

<a id="a99d3f0a1c9e10f405c761ae6f3bf2744"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 21)
```

GCLK 外设标识符（Peripheral ID）：SERCOM2 慢速 时钟（SERCOM2 Slow Clock）。

<a id="a155a02aa8799940dd0c59efac25e5bbc"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 22, 29)
```

GCLK 外设标识符（Peripheral ID）：SERCOM3 核心 时钟（SERCOM3 Core Clock）。

<a id="a08fb53b9b65e5743900bd6a4179925d3"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 22)
```

GCLK 外设标识符（Peripheral ID）：SERCOM3 慢速 时钟（SERCOM3 Slow Clock）。

<a id="a77eb95730d000556c3b32a7bcf152913"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 34)
```

GCLK 外设标识符（Peripheral ID）：SERCOM4 核心 时钟（SERCOM4 Core Clock）。

<a id="accbd9b23f933a8bae611a00019c5eb50"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 20)
```

GCLK 外设标识符（Peripheral ID）：SERCOM4 慢速 时钟（SERCOM4 Slow Clock）。

<a id="a4b1126fa67b001d9d086874d8536fb48"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 26, 35)
```

GCLK 外设标识符（Peripheral ID）：SERCOM5 核心 时钟（SERCOM5 Core Clock）。

<a id="a680eff3630a7446292705a3c29098510"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 23)
```

GCLK 外设标识符（Peripheral ID）：SERCOM5 慢速 时钟（SERCOM5 Slow Clock）。

<a id="a8b7161f3cedb7e5e39cc5d98498e262c"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 27, 36)
```

GCLK 外设标识符（Peripheral ID）：SERCOM6 核心 时钟（SERCOM6 Core Clock）。

<a id="a8aaeb571901ab3b932c93aea8f67f39a"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 24)
```

GCLK 外设标识符（Peripheral ID）：SERCOM6 慢速 时钟（SERCOM6 Slow Clock）。

<a id="a12909dbedec1469b89c431395b9fb6eb"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 28, 37)
```

GCLK 外设标识符（Peripheral ID）：SERCOM7 核心 时钟（SERCOM7 Core Clock）。

<a id="a277cd1054793077c5c67551bf4a38df5"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 25)
```

GCLK 外设标识符（Peripheral ID）：SERCOM7 慢速 时钟（SERCOM7 Slow Clock）。

<a id="a0730543904f07b779d0a4ecea9bb8b3e"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SPI_IXS`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SPI_IXS MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 36, 45)
```

GCLK 外设标识符（Peripheral ID）：SPI_IXS（SPI_IXS）。

<a id="a1e5c49e89ef93f44610556597c2be205"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SQI`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SQI MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 43, 52)
```

GCLK 外设标识符（Peripheral ID）：SQI（SQI）。

<a id="af3614ec46e49df22dc37768df6e9c12b"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 30)
```

GCLK 外设标识符（Peripheral ID）：TCC0（TCC0）。

<a id="a253908d056c2ac97302065d9c0eb1cc4"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 31)
```

GCLK 外设标识符（Peripheral ID）：TCC1（TCC1）。

<a id="ae4ebf71771a1435faa34293290ed06f0"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC2`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 32)
```

GCLK 外设标识符（Peripheral ID）：TCC2（TCC2）。

<a id="a363610cff7033e1bb7036d3b4ed21a0c"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC3`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 33)
```

GCLK 外设标识符（Peripheral ID）：TCC3（TCC3）。

<a id="a341713f50727d73e4275cc093061487e"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC4`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 29, 38)
```

GCLK 外设标识符（Peripheral ID）：TCC4（TCC4）。

<a id="a1cb0b9600a335a01ff00c7eaa64a1229"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC5`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 30, 39)
```

GCLK 外设标识符（Peripheral ID）：TCC5（TCC5）。

<a id="a14a655c0aead0534f6915a1994a6ed1d"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC6`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 31, 40)
```

GCLK 外设标识符（Peripheral ID）：TCC6（TCC6）。

<a id="a89967af8e20803cdb7e41890c4a4a143"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC7`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC7 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 32, 41)
```

GCLK 外设标识符（Peripheral ID）：TCC7（TCC7）。

<a id="a566c7babd5641f337fc00adb20367833"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_USB`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_USB MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 46, 55)
```

GCLK 外设标识符（Peripheral ID）：USB（USB）。

<a id="a6de8b0b73f5ad847d3b4a1c2898ba534"></a>

### `CLOCK_MCHP_MCLKCPU_ID`

```c
#define CLOCK_MCHP_MCLKCPU_ID MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 0)
```

主时钟域标识符（Main Clock Domain ID）：CPU。

<a id="ad164589a2abc31000c96bd45a7eac9ba"></a>

### `CLOCK_MCHP_MCLKCPU_MAX`

```c
#define CLOCK_MCHP_MCLKCPU_MAX (0)
```

主时钟域标识符（Main Clock Domain IDs）的最大索引。

<a id="affe3569727db011f6a21143af7b9e2a7"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_AC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_AC_APB MCHP_CLOCK_DERIVE_ID(9, 3, 9, 0x3f, 54)
```

MCLK 外设标识符（Peripheral ID）：AC (APB)（AC (APB)）。

<a id="a09bd059dfc0f111ccf5f1f3149363ed6"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_ADC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_ADC_APB MCHP_CLOCK_DERIVE_ID(9, 3, 8, 0x3f, 53)
```

MCLK 外设标识符（Peripheral ID）：ADC (APB)（ADC (APB)）。

<a id="a0819cfd2cae3f24367c9fda31718c240"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_BSDAP_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BSDAP_AHB MCHP_CLOCK_DERIVE_ID(9, 3, 19, 0x3f, 64)
```

MCLK 外设标识符（Peripheral ID）：BSDAP (AHB)（BSDAP (AHB)）。

<a id="a020e0dd01728bbb323fd174eccb1509f"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CAN0_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN0_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 13, 0x3f, 7)
```

MCLK 外设标识符（Peripheral ID）：CAN0 (AHB)（CAN0 (AHB)）。

<a id="a82eab8ef6506c116079b31528651ac8e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CAN1_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN1_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 14, 0x3f, 8)
```

MCLK 外设标识符（Peripheral ID）：CAN1 (AHB)（CAN1 (AHB)）。

<a id="a4f466eeed8fa57339509207c77fd6cf0"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CCL_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CCL_APB MCHP_CLOCK_DERIVE_ID(9, 3, 13, 0x3f, 58)
```

MCLK 外设标识符（Peripheral ID）：CCL (APB)（CCL (APB)）。

<a id="a98a4fedf80bb2756cf890d8c33dc98cf"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DMA0_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA0_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 8, 0x3f, 4)
```

MCLK 外设标识符（Peripheral ID）：DMA0 (AHB)（DMA0 (AHB)）。

<a id="a003cccbd09694978168d83d06b25995f"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DMA0_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA0_APB MCHP_CLOCK_DERIVE_ID(9, 2, 1, 0x3f, 32)
```

MCLK 外设标识符（Peripheral ID）：DMA0 (APB)（DMA0 (APB)）。

<a id="aefad014e192ff33d0a75ed69d3e99997"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DMA1_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA1_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 9, 0x3f, 5)
```

MCLK 外设标识符（Peripheral ID）：DMA1 (AHB)（DMA1 (AHB)）。

<a id="aea8d908b0ffd05877a425b9b5085b6c8"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DMA1_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMA1_APB MCHP_CLOCK_DERIVE_ID(9, 2, 2, 0x3f, 33)
```

MCLK 外设标识符（Peripheral ID）：DMA1 (APB)（DMA1 (APB)）。

<a id="a5f1c9309e3eb0586eb1f765536b4346e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 3, 0x3f, 0)
```

MCLK 外设标识符（Peripheral ID）：DSU (AHB)（DSU (AHB)）。

<a id="a25521d18a70eacc1ad5cc347feb0765e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DSU_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_APB MCHP_CLOCK_DERIVE_ID(9, 1, 0, 0x3f, 17)
```

MCLK 外设标识符（Peripheral ID）：DSU (APB)（DSU (APB)）。

<a id="ada6c6291b51b7fe41ee0925e31628ff9"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_EBI_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 21, 0x3f, 15)
```

MCLK 外设标识符（Peripheral ID）：EBI (AHB)（EBI (AHB)）。

<a id="a9fb89fb266e6bee7606a1de146a33d4f"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_EBI_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_APB MCHP_CLOCK_DERIVE_ID(9, 3, 18, 0x3f, 63)
```

MCLK 外设标识符（Peripheral ID）：EBI (APB)（EBI (APB)）。

<a id="a96f372b19d6097849c37795933d0822f"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_EIC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EIC_APB MCHP_CLOCK_DERIVE_ID(9, 1, 13, 0x3f, 26)
```

MCLK 外设标识符（Peripheral ID）：EIC (APB)（EIC (APB)）。

<a id="aa4f92ad099bb80accb050b39876688c3"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_ETH_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_ETH_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 15, 0x3f, 9)
```

MCLK 外设标识符（Peripheral ID）：ETH (AHB)（ETH (AHB)）。

<a id="aa6e14d78643d022467b3385bf930f349"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_ETH_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_ETH_APB MCHP_CLOCK_DERIVE_ID(9, 3, 15, 0x3f, 60)
```

MCLK 外设标识符（Peripheral ID）：ETH (APB)（ETH (APB)）。

<a id="a0beb2098f964c3ca55a9dca232e2f280"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_EVSYS_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EVSYS_APB MCHP_CLOCK_DERIVE_ID(9, 2, 6, 0x3f, 36)
```

MCLK 外设标识符（Peripheral ID）：EVSYS (APB)（EVSYS (APB)）。

<a id="af85028f923174b11e44d1fc9043c5c75"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 4, 0x3f, 1)
```

MCLK 外设标识符（Peripheral ID）：FCR (AHB)（FCR (AHB)）。

<a id="a8427e8e5faebe7f66dbfe1554d024c6e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FCR_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_APB MCHP_CLOCK_DERIVE_ID(9, 1, 1, 0x3f, 18)
```

MCLK 外设标识符（Peripheral ID）：FCR (APB)（FCR (APB)）。

<a id="a55391bcfa4db8dfdf6d7fbfbfbc9626f"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 5, 0x3f, 2)
```

MCLK 外设标识符（Peripheral ID）：FCW (AHB)（FCW (AHB)）。

<a id="a979b800be2dabf8c744fef8295cf1bcc"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FCW_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_APB MCHP_CLOCK_DERIVE_ID(9, 1, 2, 0x3f, 19)
```

MCLK 外设标识符（Peripheral ID）：FCW (APB)（FCW (APB)）。

<a id="a7683dd70a6fd67b23950255a318a92c5"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FREQM_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FREQM_APB MCHP_CLOCK_DERIVE_ID(9, 1, 10, 0x3f, 23)
```

MCLK 外设标识符（Peripheral ID）：FREQM (APB)（FREQM (APB)）。

<a id="a37acd5942b619f4410efdebad1a29651"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_HSM_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HSM_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 22, 0x3f, 16)
```

MCLK 外设标识符（Peripheral ID）：HSM (AHB)（HSM (AHB)）。

<a id="a2c6f9bd6f15c1c2518c578d192e9917c"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_I2S_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_I2S_APB MCHP_CLOCK_DERIVE_ID(9, 3, 11, 0x3f, 56)
```

MCLK 外设标识符（Peripheral ID）：I2S (APB)（I2S (APB)）。

<a id="ae43a1ae1b9502fa64d0f2d679937a759"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_IDAU_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_IDAU_APB MCHP_CLOCK_DERIVE_ID(9, 2, 5, 0x3f, 35)
```

MCLK 外设标识符（Peripheral ID）：IDAU (APB)（IDAU (APB)）。

<a id="a5884aa8fb4b6841cf3b36f8df64136d1"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_MAX`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MAX (64)
```

MCLK 外设标识符（Peripheral IDs）的最大索引。

<a id="a0d19557ec776183aa0734c97d38cdbc6"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_MBISTINTF_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MBISTINTF_APB MCHP_CLOCK_DERIVE_ID(9, 1, 18, 0x3f, 29)
```

MCLK 外设标识符（Peripheral ID）：MBISTINTF (APB)（MBISTINTF (APB)）。

<a id="a1d56390d443e73b0a3ff50b5375d053d"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL_APB MCHP_CLOCK_DERIVE_ID(9, 1, 7, 0x3f, 22)
```

MCLK 外设标识符（Peripheral ID）：OSC32KCTRL (APB)（OSC32KCTRL (APB)）。

<a id="af1c5abfaa99c29512de8ad86d50436fa"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL_APB MCHP_CLOCK_DERIVE_ID(9, 1, 6, 0x3f, 21)
```

MCLK 外设标识符（Peripheral ID）：OSCCTRL (APB)（OSCCTRL (APB)）。

<a id="ad63bf9ad8a02a102f6cc0b4ebcecd8ae"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PAC_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 6, 0x3f, 3)
```

MCLK 外设标识符（Peripheral ID）：PAC (AHB)（PAC (AHB)）。

<a id="a574e9bee5faec84626fa1e9ef679e71a"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB MCHP_CLOCK_DERIVE_ID(9, 1, 14, 0x3f, 27)
```

MCLK 外设标识符（Peripheral ID）：PAC (APB)（PAC (APB)）。

<a id="aa7f5424b104ff218e0abc29c45709ef5"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PCC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PCC_APB MCHP_CLOCK_DERIVE_ID(9, 3, 12, 0x3f, 57)
```

MCLK 外设标识符（Peripheral ID）：PCC (APB)（PCC (APB)）。

<a id="ac97b177e0b4050c248416cbb09dc6693"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PDEC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PDEC_APB MCHP_CLOCK_DERIVE_ID(9, 3, 14, 0x3f, 59)
```

MCLK 外设标识符（Peripheral ID）：PDEC (APB)（PDEC (APB)）。

<a id="acadb93a9913d4622db5b6e0b7d375ef1"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB MCHP_CLOCK_DERIVE_ID(9, 2, 0, 0x3f, 31)
```

MCLK 外设标识符（Peripheral ID）：PORT (APB)（PORT (APB)）。

<a id="a362ebd80cf078c91d39f7e37078445a9"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PRM_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PRM_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 12, 0x3f, 6)
```

MCLK 外设标识符（Peripheral ID）：PRM (AHB)（PRM (AHB)）。

<a id="a06eb4d6cb2bec066a15857648c259223"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PRM_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PRM_APB MCHP_CLOCK_DERIVE_ID(9, 2, 4, 0x3f, 34)
```

MCLK 外设标识符（Peripheral ID）：PRM (APB)（PRM (APB)）。

<a id="a31de65a5228c7021bef57eb9edef0ee8"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PTC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PTC_APB MCHP_CLOCK_DERIVE_ID(9, 3, 10, 0x3f, 55)
```

MCLK 外设标识符（Peripheral ID）：PTC (APB)（PTC (APB)）。

<a id="acd7a900e83eb1f4440f1a3bb19b64c87"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_RSTC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RSTC_APB MCHP_CLOCK_DERIVE_ID(9, 1, 5, 0x3f, 20)
```

MCLK 外设标识符（Peripheral ID）：RSTC (APB)（RSTC (APB)）。

<a id="ad712b633caa2592437efda6d5fa9fddf"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_RTC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RTC_APB MCHP_CLOCK_DERIVE_ID(9, 1, 12, 0x3f, 25)
```

MCLK 外设标识符（Peripheral ID）：RTC (APB)（RTC (APB)）。

<a id="a4cd460b34dac65adf8e9c19fc7072149"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SDMMC0_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDMMC0_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 17, 0x3f, 11)
```

MCLK 外设标识符（Peripheral ID）：SDMMC0 (AHB)（SDMMC0 (AHB)）。

<a id="a0ff819df13afc3af15b8e593f9a027c4"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SDMMC1_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDMMC1_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 18, 0x3f, 12)
```

MCLK 外设标识符（Peripheral ID）：SDMMC1 (AHB)（SDMMC1 (AHB)）。

<a id="a47f3b5aa5a51664bb754a6bd409110a4"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0_APB MCHP_CLOCK_DERIVE_ID(9, 2, 7, 0x3f, 37)
```

MCLK 外设标识符（Peripheral ID）：SERCOM0 (APB)（SERCOM0 (APB)）。

<a id="af797c727eb17090ccefc52a22c5f5b51"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1_APB MCHP_CLOCK_DERIVE_ID(9, 2, 8, 0x3f, 38)
```

MCLK 外设标识符（Peripheral ID）：SERCOM1 (APB)（SERCOM1 (APB)）。

<a id="ad809db56498079a4d2b01e393af7bd04"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2_APB MCHP_CLOCK_DERIVE_ID(9, 2, 9, 0x3f, 39)
```

MCLK 外设标识符（Peripheral ID）：SERCOM2 (APB)（SERCOM2 (APB)）。

<a id="aff58338e2aa80841b910bebca63ca132"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3_APB MCHP_CLOCK_DERIVE_ID(9, 2, 10, 0x3f, 40)
```

MCLK 外设标识符（Peripheral ID）：SERCOM3 (APB)（SERCOM3 (APB)）。

<a id="a75c42c1ce5bd4831739973617e5fedd4"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4_APB MCHP_CLOCK_DERIVE_ID(9, 3, 0, 0x3f, 45)
```

MCLK 外设标识符（Peripheral ID）：SERCOM4 (APB)（SERCOM4 (APB)）。

<a id="ac3f06e5a5b8a2d43465ff0ce073427e0"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5_APB MCHP_CLOCK_DERIVE_ID(9, 3, 1, 0x3f, 46)
```

MCLK 外设标识符（Peripheral ID）：SERCOM5 (APB)（SERCOM5 (APB)）。

<a id="a22d35327a659f86f3bbd1b86dfbd0bdc"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM6_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM6_APB MCHP_CLOCK_DERIVE_ID(9, 3, 2, 0x3f, 47)
```

MCLK 外设标识符（Peripheral ID）：SERCOM6 (APB)（SERCOM6 (APB)）。

<a id="a476d7f837f1d5c092b9375864e895e7b"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM7_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM7_APB MCHP_CLOCK_DERIVE_ID(9, 3, 3, 0x3f, 48)
```

MCLK 外设标识符（Peripheral ID）：SERCOM7 (APB)（SERCOM7 (APB)）。

<a id="a29100f869118c250054725cdf72d58f8"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SQI_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SQI_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 16, 0x3f, 10)
```

MCLK 外设标识符（Peripheral ID）：SQI (AHB)（SQI (AHB)）。

<a id="a09ddda66170546df3264fa6630c21ad9"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC0_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC0_APB MCHP_CLOCK_DERIVE_ID(9, 2, 11, 0x3f, 41)
```

MCLK 外设标识符（Peripheral ID）：TCC0 (APB)（TCC0 (APB)）。

<a id="a426ad19aeeb116ceed471a6ffbe27ba6"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC1_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC1_APB MCHP_CLOCK_DERIVE_ID(9, 2, 12, 0x3f, 42)
```

MCLK 外设标识符（Peripheral ID）：TCC1 (APB)（TCC1 (APB)）。

<a id="a0c54ce51de3b7012abcfe6822cd81a58"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC2_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC2_APB MCHP_CLOCK_DERIVE_ID(9, 2, 13, 0x3f, 43)
```

MCLK 外设标识符（Peripheral ID）：TCC2 (APB)（TCC2 (APB)）。

<a id="a1e301cdd4b8a60bff8b52eff03dcd6e6"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC3_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC3_APB MCHP_CLOCK_DERIVE_ID(9, 2, 14, 0x3f, 44)
```

MCLK 外设标识符（Peripheral ID）：TCC3 (APB)（TCC3 (APB)）。

<a id="a07f028c49e5174a320eba2f326c013b7"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC4_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC4_APB MCHP_CLOCK_DERIVE_ID(9, 3, 4, 0x3f, 49)
```

MCLK 外设标识符（Peripheral ID）：TCC4 (APB)（TCC4 (APB)）。

<a id="ac08c3fbc66ec7948bb78a7bbea684467"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC5_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC5_APB MCHP_CLOCK_DERIVE_ID(9, 3, 5, 0x3f, 50)
```

MCLK 外设标识符（Peripheral ID）：TCC5 (APB)（TCC5 (APB)）。

<a id="aabe0b18cb49f214748847d1fd6c9b0d4"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC6_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC6_APB MCHP_CLOCK_DERIVE_ID(9, 3, 6, 0x3f, 51)
```

MCLK 外设标识符（Peripheral ID）：TCC6 (APB)（TCC6 (APB)）。

<a id="ab3e026a71c9ecbf0b7508e2d58d51485"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC7_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC7_APB MCHP_CLOCK_DERIVE_ID(9, 3, 7, 0x3f, 52)
```

MCLK 外设标识符（Peripheral ID）：TCC7 (APB)（TCC7 (APB)）。

<a id="ac8d026bae71eb4c033b8fd93b2e0fa2c"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TDM_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TDM_APB MCHP_CLOCK_DERIVE_ID(9, 1, 19, 0x3f, 30)
```

MCLK 外设标识符（Peripheral ID）：TDM (APB)（TDM (APB)）。

<a id="a24b1be03ee41ef4d3e4ba72694d863b5"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TRAM_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TRAM_APB MCHP_CLOCK_DERIVE_ID(9, 1, 15, 0x3f, 28)
```

MCLK 外设标识符（Peripheral ID）：TRAM (APB)（TRAM (APB)）。

<a id="a1f0b24f209cc2aeba54f770d9ad6f045"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TRNG_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TRNG_APB MCHP_CLOCK_DERIVE_ID(9, 3, 16, 0x3f, 61)
```

MCLK 外设标识符（Peripheral ID）：TRNG (APB)（TRNG (APB)）。

<a id="aae27b56b768f9c68bfb39f8a6ea3bd34"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_USB_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_USB_APB MCHP_CLOCK_DERIVE_ID(9, 3, 17, 0x3f, 62)
```

MCLK 外设标识符（Peripheral ID）：USB (APB)（USB (APB)）。

<a id="a03f03076ce38c08aff0158f36e552bdb"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_USBFS_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_USBFS_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 19, 0x3f, 13)
```

MCLK 外设标识符（Peripheral ID）：USBFS (AHB)（USBFS (AHB)）。

<a id="a311c2b3b6b7c998cd03a0ad4caaf9b68"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_USBHS_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_USBHS_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 20, 0x3f, 14)
```

MCLK 外设标识符（Peripheral ID）：USBHS (AHB)（USBHS (AHB)）。

<a id="aea2b6485e25c10b439400ce5104a7be6"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_WDT_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_WDT_APB MCHP_CLOCK_DERIVE_ID(9, 1, 11, 0x3f, 24)
```

MCLK 外设标识符（Peripheral ID）：WDT (APB)（WDT (APB)）。

<a id="a12ddd4213583b011cf2ec8e5802ac3f2"></a>

### `CLOCK_MCHP_PLL0_ID_OUT0`

```c
#define CLOCK_MCHP_PLL0_ID_OUT0 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 0)
```

`PLL0` 输出（Output）0 的时钟标识符（Clock ID）。

<a id="a24937208d2f707d32917b2293fe9e9e3"></a>

### `CLOCK_MCHP_PLL0_ID_OUT1`

```c
#define CLOCK_MCHP_PLL0_ID_OUT1 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 1)
```

`PLL0` 输出（Output）1 的时钟标识符（Clock ID）。

<a id="a9d67b9354cc244fc98303556530d711f"></a>

### `CLOCK_MCHP_PLL0_ID_OUT2`

```c
#define CLOCK_MCHP_PLL0_ID_OUT2 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 2)
```

`PLL0` 输出（Output）2 的时钟标识符（Clock ID）。

<a id="aaba7d7ef85c02109d97d6c1098f84bc8"></a>

### `CLOCK_MCHP_PLL0_ID_OUT3`

```c
#define CLOCK_MCHP_PLL0_ID_OUT3 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 3)
```

`PLL0` 输出（Output）3 的时钟标识符（Clock ID）。

<a id="a8c05b54dae36aa1f2c04a5dd05d12531"></a>

### `CLOCK_MCHP_PLL0_ID_OUT4`

```c
#define CLOCK_MCHP_PLL0_ID_OUT4 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 4)
```

`PLL0` 输出（Output）4 的时钟标识符（Clock ID）。

<a id="aa71217a134f7ad7b2ec49463fcf739f1"></a>

### `CLOCK_MCHP_PLL0_ID_OUT5`

```c
#define CLOCK_MCHP_PLL0_ID_OUT5 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 5)
```

`PLL0` 输出（Output）5 的时钟标识符（Clock ID）。

<a id="a1566da9a6867acb8da4a3e4cf7e7ab5d"></a>

### `CLOCK_MCHP_PLL0_OUT_ID_MAX`

```c
#define CLOCK_MCHP_PLL0_OUT_ID_MAX (5)
```

PLL0 输出时钟标识符（Output Clock IDs）的最大索引。

<a id="a5ef027c132316e0aa9fe06cc2e0f3b63"></a>

### `CLOCK_MCHP_PLL_ID_MAX`

```c
#define CLOCK_MCHP_PLL_ID_MAX (0)
```

锁相环（PLL）时钟标识符（Clock IDs）的最大索引。

<a id="acd48cc8da0678862a2d8e0af37799e1e"></a>

### `CLOCK_MCHP_PLL_ID_PLL0`

```c
#define CLOCK_MCHP_PLL_ID_PLL0 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 0, 0)
```

`PLL0` 时钟标识符（Clock ID）。

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
- 位 26..31（6 位）：`type`，取值为 `SUBSYS_TYPE_XOSC`（0）、`SUBSYS_TYPE_DFLL48M`（1）、`SUBSYS_TYPE_PLL`（2）、`SUBSYS_TYPE_PLL_OUT`（3）、`SUBSYS_TYPE_RTC`（4）、`SUBSYS_TYPE_XOSC32K`（5）、`SUBSYS_TYPE_GCLKGEN`（6）、`SUBSYS_TYPE_GCLKPERIPH`（7）、`SUBSYS_TYPE_MCLKDOMAIN`（8）或 `SUBSYS_TYPE_MCLKPERIPH`（9）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 时钟子系统类型（Clock Subsystem Type）。 |
| `mclkmaskreg` | 从 AHBx 和 APBx 总线（Buses）中选择。 |
| `mclkmaskbit` | 选择连接到 AHBx 或 APBx 总线的模块（Module），范围 `0–31`。 |
| `gclkperiph` | `PCHTRLm` 中的 GCLK 外设通道编号（Peripheral Channel Number）`m`，范围为 `0–63`。 |
| `inst` | 指定时钟类型（Clock Type）的实例编号（Instance Number）。 |

**返回（Returns）**：返回值（Returns）：编码后的时钟子系统标识符（Encoded Clock Subsystem Identifier）。


## 2.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P501_mchp_pic32ck_sg_gc_clock.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_zephyr__dt-bindings__clock__imx952_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__dt-bindings__clock__mchp_pic32cm_sg_gc_clock.h_文件参考.md)
