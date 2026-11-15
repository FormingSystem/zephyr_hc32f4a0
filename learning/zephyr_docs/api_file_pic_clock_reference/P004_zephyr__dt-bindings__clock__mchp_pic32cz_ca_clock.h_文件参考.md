---
id: learning.zephyr-docs.api-file-pic-clock-reference.page-4
title: zephyr__dt-bindings__clock__mchp_pic32cz_ca_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cz__ca__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_dt-bindings\_\_clock\_\_mchp\_pic32cz\_ca\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__pic32cz__ca__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

列出pic32cz_ca系列的时钟子系统ID（Clock Subsystem IDs）。

查看此文件的源码。

<a id="details"></a>

列出 `pic32cz_ca` 系列的时钟子系统标识符（Clock Subsystem IDs）。这些标识符用于设备树节点（Devicetree Nodes），也用作时钟 API 的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

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

<a id="r_a971daee0119b24a95002e99dc33a8547"></a>

```c
#define CLOCK_MCHP_DPLL_ID_DPLL1 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 2, 1)
```

相关声明：[CLOCK_MCHP_DPLL_ID_DPLL1](#a971daee0119b24a95002e99dc33a8547)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`DPLL1` 时钟标识符（Clock ID）。

<a id="r_a535adb887a7c5c21a1a88f0bf450e5ed"></a>

```c
#define CLOCK_MCHP_DPLL_ID_MAX (1)
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

<a id="r_a1a74c6aba140e901e99ea7a16ddfed43"></a>

```c
#define CLOCK_MCHP_DPLL1_ID_OUT0 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 4)
```

相关声明：[CLOCK_MCHP_DPLL1_ID_OUT0](#a1a74c6aba140e901e99ea7a16ddfed43)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`DPLL1` 输出（Output）0 的时钟标识符（Clock ID）。

<a id="r_a0ebfe2b27af57483626a43b317b8b0c4"></a>

```c
#define CLOCK_MCHP_DPLL1_ID_OUT1 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 5)
```

相关声明：[CLOCK_MCHP_DPLL1_ID_OUT1](#a0ebfe2b27af57483626a43b317b8b0c4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`DPLL1` 输出（Output）1 的时钟标识符（Clock ID）。

<a id="r_ac189dc0b4442d365774ab62e8895046b"></a>

```c
#define CLOCK_MCHP_DPLL1_ID_OUT2 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 6)
```

相关声明：[CLOCK_MCHP_DPLL1_ID_OUT2](#ac189dc0b4442d365774ab62e8895046b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`DPLL1` 输出（Output）2 的时钟标识符（Clock ID）。

<a id="r_a8650089f16b6bcce0a580aab140091ea"></a>

```c
#define CLOCK_MCHP_DPLL1_ID_OUT3 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 7)
```

相关声明：[CLOCK_MCHP_DPLL1_ID_OUT3](#a8650089f16b6bcce0a580aab140091ea)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

`DPLL1` 输出（Output）3 的时钟标识符（Clock ID）。

<a id="r_a1d020421206c10005772bc3912989fa6"></a>

```c
#define CLOCK_MCHP_DPLL_OUT_ID_MAX (7)
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

<a id="r_a3f6397604e3735e9aeadc77ddf03607c"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN12 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 12)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN12](#a3f6397604e3735e9aeadc77ddf03607c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）12 的标识符（ID）。

<a id="r_ac918ff9571138d2c907c16b4878301b0"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN13 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 13)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN13](#ac918ff9571138d2c907c16b4878301b0)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）13 的标识符（ID）。

<a id="r_afef541bf3639fc88967d7f776f08951c"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN14 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 14)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN14](#afef541bf3639fc88967d7f776f08951c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）14 的标识符（ID）。

<a id="r_aa9cd23b9abd14e0e1fb8b996840ccee2"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN15 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 15)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_GEN15](#aa9cd23b9abd14e0e1fb8b996840ccee2)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

通用时钟发生器（Generic Clock Generator）15 的标识符（ID）。

<a id="r_a67296972320d7cb9295cd67c9cf25c54"></a>

```c
#define CLOCK_MCHP_GCLKGEN_ID_MAX (15)
```

相关声明：[CLOCK_MCHP_GCLKGEN_ID_MAX](#a67296972320d7cb9295cd67c9cf25c54)。

通用时钟发生器标识符（Generic Clock Generator IDs）的最大索引。

<a id="define-members-7"></a>

### GCLKPERIPH_TYPE 时钟标识符（Clock IDs）

<a id="r_a8f21248b0662fee58bbeb9752de950d4"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 3, 0)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR](#a8f21248b0662fee58bbeb9752de950d4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：频率计测量（Frequency Meter Measure）。

<a id="r_a0da9e951ad59ea7ffa1b3a0586203202"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 4, 1)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF](#a0da9e951ad59ea7ffa1b3a0586203202)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：频率计参考（Frequency Meter Reference）。

<a id="r_aeaeb9a032e3fa5a00199ef27c2a5ec30"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EIC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 5, 2)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EIC](#aeaeb9a032e3fa5a00199ef27c2a5ec30)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：外部中断控制器 (EIC)（External Interrupt Controller (EIC)）。

<a id="r_a31aa9472c7182d16249ba7950b452c14"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 6, 3)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0](#a31aa9472c7182d16249ba7950b452c14)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 0（Event System Channel 0）。

<a id="r_a370930d5d12099ec34871a27cee5c8e2"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 7, 4)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1](#a370930d5d12099ec34871a27cee5c8e2)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 1（Event System Channel 1）。

<a id="r_a6966d71c9da4ce1803c48dc088818401"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 8, 5)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2](#a6966d71c9da4ce1803c48dc088818401)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 2（Event System Channel 2）。

<a id="r_a5d98273862a2323e050874755da0c840"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 9, 6)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3](#a5d98273862a2323e050874755da0c840)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 3（Event System Channel 3）。

<a id="r_a24855b6b55dc3eb9efba6476d6d930e8"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 10, 7)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4](#a24855b6b55dc3eb9efba6476d6d930e8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 4（Event System Channel 4）。

<a id="r_a6bb92b5d57c58e6b1ab083504bbb3756"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 11, 8)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5](#a6bb92b5d57c58e6b1ab083504bbb3756)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 5（Event System Channel 5）。

<a id="r_ae2404c8e3bce6bd9b01903a9ad942d35"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 12, 9)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6](#ae2404c8e3bce6bd9b01903a9ad942d35)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 6（Event System Channel 6）。

<a id="r_a852a5424cc73a5e75fcd7b151e7dd767"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 13, 10)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7](#a852a5424cc73a5e75fcd7b151e7dd767)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 7（Event System Channel 7）。

<a id="r_a9ff8a7f89700d95e431e6d0c12869b56"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 14, 11)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8](#a9ff8a7f89700d95e431e6d0c12869b56)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 8（Event System Channel 8）。

<a id="r_ad7112111ef68955636866ec0adb0e71e"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 15, 12)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9](#ad7112111ef68955636866ec0adb0e71e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 9（Event System Channel 9）。

<a id="r_aeb43cfd70588d9f660e8965516480191"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 16, 13)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10](#aeb43cfd70588d9f660e8965516480191)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 10（Event System Channel 10）。

<a id="r_a93e2a650425a0bb9014c56d848c039bb"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 17, 14)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11](#a93e2a650425a0bb9014c56d848c039bb)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：事件系统通道 11（Event System Channel 11）。

<a id="r_a2bb7a4f72e45c2fb5f449b6b3f1b4520"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 15)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW](#a2bb7a4f72e45c2fb5f449b6b3f1b4520)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM0 慢速 时钟（SERCOM0 Slow clock）。

<a id="r_a726fe192480ed57fbdc3e77cc1133c89"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 16)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW](#a726fe192480ed57fbdc3e77cc1133c89)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM1 慢速 时钟（SERCOM1 Slow clock）。

<a id="r_accbd9b23f933a8bae611a00019c5eb50"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 17)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_SLOW](#accbd9b23f933a8bae611a00019c5eb50)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM4 慢速 时钟（SERCOM4 Slow clock）。

<a id="r_a99d3f0a1c9e10f405c761ae6f3bf2744"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 18)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW](#a99d3f0a1c9e10f405c761ae6f3bf2744)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM2 慢速 时钟（SERCOM2 Slow clock）。

<a id="r_a08fb53b9b65e5743900bd6a4179925d3"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 19)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW](#a08fb53b9b65e5743900bd6a4179925d3)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM3 慢速 时钟（SERCOM3 Slow clock）。

<a id="r_a680eff3630a7446292705a3c29098510"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 20)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_SLOW](#a680eff3630a7446292705a3c29098510)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM5 慢速 时钟（SERCOM5 Slow clock）。

<a id="r_a8aaeb571901ab3b932c93aea8f67f39a"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 21)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_SLOW](#a8aaeb571901ab3b932c93aea8f67f39a)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM6 慢速 时钟（SERCOM6 Slow clock）。

<a id="r_a277cd1054793077c5c67551bf4a38df5"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 22)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_SLOW](#a277cd1054793077c5c67551bf4a38df5)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM7 慢速 时钟（SERCOM7 Slow clock）。

<a id="r_ad7205a316c6b5a9a9700824d8435f614"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM8_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 23)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM8_SLOW](#ad7205a316c6b5a9a9700824d8435f614)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM8 慢速 时钟（SERCOM8 Slow clock）。

<a id="r_a7820807d16cbd8f23d42c2deb0e7ad18"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM9_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 24)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM9_SLOW](#a7820807d16cbd8f23d42c2deb0e7ad18)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM9 慢速 时钟（SERCOM9 Slow clock）。

<a id="r_a88f1128166176ebfc0a41dd496186300"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 21, 25)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE](#a88f1128166176ebfc0a41dd496186300)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM0 核心 时钟（SERCOM0 Core clock）。

<a id="r_ab3ef99c62a821f4e5fe1f800de6561c2"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 22, 26)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE](#ab3ef99c62a821f4e5fe1f800de6561c2)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM1 核心 时钟（SERCOM1 Core clock）。

<a id="r_ab0668a32e7385c8629b26cd396e6beaa"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 27)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE](#ab0668a32e7385c8629b26cd396e6beaa)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM2 核心 时钟（SERCOM2 Core clock）。

<a id="r_a155a02aa8799940dd0c59efac25e5bbc"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 28)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE](#a155a02aa8799940dd0c59efac25e5bbc)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM3 核心 时钟（SERCOM3 Core clock）。

<a id="r_a77eb95730d000556c3b32a7bcf152913"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 29)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE](#a77eb95730d000556c3b32a7bcf152913)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM4 核心 时钟（SERCOM4 Core clock）。

<a id="r_a4b1126fa67b001d9d086874d8536fb48"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 26, 30)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE](#a4b1126fa67b001d9d086874d8536fb48)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM5 核心 时钟（SERCOM5 Core clock）。

<a id="r_a8b7161f3cedb7e5e39cc5d98498e262c"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 27, 31)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE](#a8b7161f3cedb7e5e39cc5d98498e262c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM6 核心 时钟（SERCOM6 Core clock）。

<a id="r_a12909dbedec1469b89c431395b9fb6eb"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 28, 32)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE](#a12909dbedec1469b89c431395b9fb6eb)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM7 核心 时钟（SERCOM7 Core clock）。

<a id="r_ac7ace4228af8c8eab533d58f8f5ea5d0"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM8_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 29, 33)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM8_CORE](#ac7ace4228af8c8eab533d58f8f5ea5d0)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM8 核心 时钟（SERCOM8 Core clock）。

<a id="r_a4b3497b52195d9237be7c89deb290b0e"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM9_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 30, 34)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SERCOM9_CORE](#a4b3497b52195d9237be7c89deb290b0e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SERCOM9 核心 时钟（SERCOM9 Core clock）。

<a id="r_af3614ec46e49df22dc37768df6e9c12b"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 31, 35)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC0](#af3614ec46e49df22dc37768df6e9c12b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC0（TCC0）。

<a id="r_a253908d056c2ac97302065d9c0eb1cc4"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 32, 36)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC1](#a253908d056c2ac97302065d9c0eb1cc4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC1（TCC1）。

<a id="r_ae4ebf71771a1435faa34293290ed06f0"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 33, 37)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC2](#ae4ebf71771a1435faa34293290ed06f0)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC2（TCC2）。

<a id="r_a14a655c0aead0534f6915a1994a6ed1d"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 37, 38)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC6](#a14a655c0aead0534f6915a1994a6ed1d)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC6（TCC6）。

<a id="r_a89967af8e20803cdb7e41890c4a4a143"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC7 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 38, 39)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC7](#a89967af8e20803cdb7e41890c4a4a143)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC7（TCC7）。

<a id="r_a9aab46e09874a681b735dad66a352baa"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC8 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 39, 40)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC8](#a9aab46e09874a681b735dad66a352baa)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC8（TCC8）。

<a id="r_abf072528495ffa4fc031d11c2a0c5654"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC9 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 40, 41)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_TCC9](#abf072528495ffa4fc031d11c2a0c5654)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：TCC9（TCC9）。

<a id="r_a845a53053a861de67ebfa150bff389ff"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 41, 42)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_ADC](#a845a53053a861de67ebfa150bff389ff)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：ADC（ADC）。

<a id="r_a8558308cb89c99326b165a7b12b14ff1"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_AC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 42, 43)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_AC](#a8558308cb89c99326b165a7b12b14ff1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：AC (模拟比较器)（AC (Analog Comparator)）。

<a id="r_a65c9bc79d0b5edd7dcc8a6178a600127"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_PTC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 43, 44)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_PTC](#a65c9bc79d0b5edd7dcc8a6178a600127)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：PTC (外设触摸控制器)（PTC (Peripheral Touch Controller)）。

<a id="r_a1799a6e482e647dbcdf98c8a65bdfd97"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_I2S0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 44, 45)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_I2S0](#a1799a6e482e647dbcdf98c8a65bdfd97)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：I2S0（I2S0）。

<a id="r_a79c9ae703ad391e68221c61bd17b25bb"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_I2S1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 45, 46)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_I2S1](#a79c9ae703ad391e68221c61bd17b25bb)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：I2S1（I2S1）。

<a id="r_ae251d4719eb378734e3cb01c9f5828d8"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 46, 47)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CAN0](#ae251d4719eb378734e3cb01c9f5828d8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CAN0（CAN0）。

<a id="r_a2e77a06b25293f4152b0f2399ab32982"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 47, 48)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CAN1](#a2e77a06b25293f4152b0f2399ab32982)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CAN1（CAN1）。

<a id="r_a6ff5711e8ebc4ecc25eb94a17a391e44"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 48, 49)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CAN2](#a6ff5711e8ebc4ecc25eb94a17a391e44)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CAN2（CAN2）。

<a id="r_a13af660581f12bdd4de13d9b98af0485"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 49, 50)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CAN3](#a13af660581f12bdd4de13d9b98af0485)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CAN3（CAN3）。

<a id="r_a2ef048cd05f2f3b32e054b48ae6c0fa2"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 50, 51)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CAN4](#a2ef048cd05f2f3b32e054b48ae6c0fa2)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CAN4（CAN4）。

<a id="r_a959753336423094e8db5505bbd405bdf"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 51, 52)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CAN5](#a959753336423094e8db5505bbd405bdf)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CAN5（CAN5）。

<a id="r_a48964f392774fac761a2290d265ecac1"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_GMAC_TX MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 54, 53)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_GMAC_TX](#a48964f392774fac761a2290d265ecac1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：GMAC TX（GMAC TX）。

<a id="r_a7aac132e47cc05e97a07fa47fe8e53d6"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_GMAC_TSU MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 55, 54)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_GMAC_TSU](#a7aac132e47cc05e97a07fa47fe8e53d6)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：GMAC TSU（GMAC TSU）。

<a id="r_a7290dbd41a053370f380d7a5524ef995"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SQI0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 56, 55)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SQI0](#a7290dbd41a053370f380d7a5524ef995)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SQI0（SQI0）。

<a id="r_acbfa372bc7330c35727bd2af6da938d1"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SQI1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 57, 56)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SQI1](#acbfa372bc7330c35727bd2af6da938d1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SQI1（SQI1）。

<a id="r_a49f7260022baa903874ca45c038cb50e"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC0_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 58, 57)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SDHC0_CORE](#a49f7260022baa903874ca45c038cb50e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SDHC0 核心（SDHC0 Core）。

<a id="r_a88e3bdc5decf97eb3c5ce756397ddff1"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 59, 58)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SDHC0_SLOW](#a88e3bdc5decf97eb3c5ce756397ddff1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SDHC0 慢速（SDHC0 Slow）。

<a id="r_aec21c0f16ae1ad3205dd08582677616c"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC1_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 60, 59)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SDHC1_CORE](#aec21c0f16ae1ad3205dd08582677616c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SDHC1 核心（SDHC1 Core）。

<a id="r_a6de1f5509f4cd074f13df6ae62b5183f"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 61, 60)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_SDHC1_SLOW](#a6de1f5509f4cd074f13df6ae62b5183f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：SDHC1 慢速（SDHC1 Slow）。

<a id="r_a075962550c0db084f0fa4fef2746eec3"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_MLB MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 62, 61)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_MLB](#a075962550c0db084f0fa4fef2746eec3)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：MLB（MLB）。

<a id="r_a4ef96507f19b49a2a10002e2603d81bf"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CM7_TRACE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 63, 62)
```

相关声明：[CLOCK_MCHP_GCLKPERIPH_ID_CM7_TRACE](#a4ef96507f19b49a2a10002e2603d81bf)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

GCLK 外设标识符（Peripheral ID）：CM7 跟踪（CM7 Trace）。

<a id="r_a9fb0644f504a830a4e324f792815ae98"></a>

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_MAX (62)
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

<a id="r_ad038d0e6ed7f444a98d1f12a4f7a213c"></a>

```c
#define CLOCK_MCHP_MCLKDOMAIN_ID_PERIPH MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 1)
```

相关声明：[CLOCK_MCHP_MCLKDOMAIN_ID_PERIPH](#ad038d0e6ed7f444a98d1f12a4f7a213c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

主时钟域标识符（Main Clock Domain ID）：外设（Peripheral）。

<a id="r_adec6556749cbc3c25b049fd700c36e94"></a>

```c
#define CLOCK_MCHP_MCLKDOMAIN_MAX (1)
```

相关声明：[CLOCK_MCHP_MCLKDOMAIN_MAX](#adec6556749cbc3c25b049fd700c36e94)。

主时钟域标识符（Main Clock Domain IDs）的最大索引。

<a id="define-members-9"></a>

### MCLKPERIPH_TYPE 时钟标识符（Clock IDs）

（待办（TODO）：确认 AHB/APB。）

<a id="r_a5f1c9309e3eb0586eb1f765536b4346e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 0, 0x3f, 0)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB](#a5f1c9309e3eb0586eb1f765536b4346e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DSU (AHB)（DSU (AHB)）。

<a id="r_a25521d18a70eacc1ad5cc347feb0765e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_APB MCHP_CLOCK_DERIVE_ID(9, 0, 1, 0x3f, 1)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DSU_APB](#a25521d18a70eacc1ad5cc347feb0765e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DSU (APB)（DSU (APB)）。

<a id="r_a55391bcfa4db8dfdf6d7fbfbfbc9626f"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 2, 0x3f, 2)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB](#a55391bcfa4db8dfdf6d7fbfbfbc9626f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FCW (AHB)（FCW (AHB)）。

<a id="r_a979b800be2dabf8c744fef8295cf1bcc"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_APB MCHP_CLOCK_DERIVE_ID(9, 0, 3, 0x3f, 3)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FCW_APB](#a979b800be2dabf8c744fef8295cf1bcc)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FCW (APB)（FCW (APB)）。

<a id="r_af85028f923174b11e44d1fc9043c5c75"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 4, 0x3f, 4)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB](#af85028f923174b11e44d1fc9043c5c75)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FCR (AHB)（FCR (AHB)）。

<a id="r_a8427e8e5faebe7f66dbfe1554d024c6e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_APB MCHP_CLOCK_DERIVE_ID(9, 0, 5, 0x3f, 5)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FCR_APB](#a8427e8e5faebe7f66dbfe1554d024c6e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FCR (APB)（FCR (APB)）。

<a id="r_a4f661f6845c462308dbd9dc635eb0216"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PM MCHP_CLOCK_DERIVE_ID(9, 0, 6, 0x3f, 6)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PM](#a4f661f6845c462308dbd9dc635eb0216)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PM（PM）。

<a id="r_a5ae4a436c06ce604b358096d14213da8"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SUPC MCHP_CLOCK_DERIVE_ID(9, 0, 7, 0x3f, 7)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SUPC](#a5ae4a436c06ce604b358096d14213da8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SUPC（SUPC）。

<a id="r_abf5fe57afad6b6d3f88cf4165406c468"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RSTC MCHP_CLOCK_DERIVE_ID(9, 0, 8, 0x3f, 8)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_RSTC](#abf5fe57afad6b6d3f88cf4165406c468)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：RSTC（RSTC）。

<a id="r_af4fe59e6405058b34f7205f58631c38e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL MCHP_CLOCK_DERIVE_ID(9, 0, 9, 0x3f, 9)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL](#af4fe59e6405058b34f7205f58631c38e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：OSCCTRL（OSCCTRL）。

<a id="r_a721267129ed0b4edf349298f972ae3af"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL MCHP_CLOCK_DERIVE_ID(9, 0, 10, 0x3f, 10)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL](#a721267129ed0b4edf349298f972ae3af)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：OSC32KCTRL（OSC32KCTRL）。

<a id="r_a37509ecf92c06e1f063a8c78c8fa0fe7"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FREQM MCHP_CLOCK_DERIVE_ID(9, 0, 13, 0x3f, 11)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_FREQM](#a37509ecf92c06e1f063a8c78c8fa0fe7)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：FREQM（FREQM）。

<a id="r_a75aeee838d3138dcf67732e62cd3d879"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_WDT MCHP_CLOCK_DERIVE_ID(9, 0, 14, 0x3f, 12)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_WDT](#a75aeee838d3138dcf67732e62cd3d879)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：WDT（WDT）。

<a id="r_ab7ce87ea60b62f5a3d77297cd1d7d713"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RTC MCHP_CLOCK_DERIVE_ID(9, 0, 15, 0x3f, 13)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_RTC](#ab7ce87ea60b62f5a3d77297cd1d7d713)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：RTC（RTC）。

<a id="r_afb137dc52e627ab615dea380c58a44da"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EIC MCHP_CLOCK_DERIVE_ID(9, 0, 16, 0x3f, 14)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_EIC](#afb137dc52e627ab615dea380c58a44da)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：EIC（EIC）。

<a id="r_ad63bf9ad8a02a102f6cc0b4ebcecd8ae"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 17, 0x3f, 15)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PAC_AHB](#ad63bf9ad8a02a102f6cc0b4ebcecd8ae)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PAC (AHB)（PAC (AHB)）。

<a id="r_a574e9bee5faec84626fa1e9ef679e71a"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB MCHP_CLOCK_DERIVE_ID(9, 0, 18, 0x3f, 16)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB](#a574e9bee5faec84626fa1e9ef679e71a)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PAC (APB)（PAC (APB)）。

<a id="r_a1ca73dcf5baf2ccecc4f607d6b3051c5"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DRMTCM MCHP_CLOCK_DERIVE_ID(9, 0, 19, 0x3f, 17)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DRMTCM](#a1ca73dcf5baf2ccecc4f607d6b3051c5)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DRMTCM（DRMTCM）。

<a id="r_a95bb042e234637438789ac12ba64a577"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC MCHP_CLOCK_DERIVE_ID(9, 0, 20, 0x3f, 18)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC](#a95bb042e234637438789ac12ba64a577)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：MCRAMC（MCRAMC）。

<a id="r_a9d398dd236236c3fa38dd3f4d3e79c10"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TRAM MCHP_CLOCK_DERIVE_ID(9, 0, 21, 0x3f, 19)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TRAM](#a9d398dd236236c3fa38dd3f4d3e79c10)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TRAM（TRAM）。

<a id="r_a240a6cdd06427460288028a7cd0a7593"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 22, 0x3f, 20)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PORT_AHB](#a240a6cdd06427460288028a7cd0a7593)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PORT (AHB)（PORT (AHB)）。

<a id="r_acadb93a9913d4622db5b6e0b7d375ef1"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB MCHP_CLOCK_DERIVE_ID(9, 0, 23, 0x3f, 21)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB](#acadb93a9913d4622db5b6e0b7d375ef1)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PORT (APB)（PORT (APB)）。

<a id="r_a1ea38f3f64ebc1ec538530a23920f45d"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 24, 0x3f, 22)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DMAC_AHB](#a1ea38f3f64ebc1ec538530a23920f45d)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DMAC (AHB)（DMAC (AHB)）。

<a id="r_ae0a16f13ccf85d54ebc961054850376c"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_APB MCHP_CLOCK_DERIVE_ID(9, 0, 25, 0x3f, 23)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_DMAC_APB](#ae0a16f13ccf85d54ebc961054850376c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：DMAC (APB)（DMAC (APB)）。

<a id="r_a2533096560d799f417ae82fbede412ba"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BUS_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 26, 0x3f, 24)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_BUS_AHB](#a2533096560d799f417ae82fbede412ba)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：BUS (AHB)（BUS (AHB)）。

<a id="r_a20188b847fdd4434a8e6bf4f11f3fb8e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BUS_APB MCHP_CLOCK_DERIVE_ID(9, 0, 27, 0x3f, 25)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_BUS_APB](#a20188b847fdd4434a8e6bf4f11f3fb8e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：BUS (APB)（BUS (APB)）。

<a id="r_a78b45760ed8d6907b19a42af13c5e950"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BOOT_ROM_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 28, 0x3f, 26)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_BOOT_ROM_AHB](#a78b45760ed8d6907b19a42af13c5e950)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：启动 ROM (AHB)（BOOT ROM (AHB)）。

<a id="r_a1421a1cc99b78e1527211fc83ca90c63"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BOOT_ROM_APB MCHP_CLOCK_DERIVE_ID(9, 0, 29, 0x3f, 27)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_BOOT_ROM_APB](#a1421a1cc99b78e1527211fc83ca90c63)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：启动 ROM (APB)（BOOT ROM (APB)）。

<a id="r_a1f3f4077f0f5be1dd872c8a18052317e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EVSYS MCHP_CLOCK_DERIVE_ID(9, 0, 30, 0x3f, 28)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_EVSYS](#a1f3f4077f0f5be1dd872c8a18052317e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：EVSYS（EVSYS）。

<a id="r_aaca27bd670359e191ee3ded852b86e9b"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0 MCHP_CLOCK_DERIVE_ID(9, 0, 31, 0x3f, 29)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0](#aaca27bd670359e191ee3ded852b86e9b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM0（SERCOM0）。

<a id="r_ad61fa9b33a8ea563a180c95213ad1d9b"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1 MCHP_CLOCK_DERIVE_ID(9, 1, 0, 0x3f, 30)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1](#ad61fa9b33a8ea563a180c95213ad1d9b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM1（SERCOM1）。

<a id="r_a75fb3dc587c912a5a961dfcd61066e09"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2 MCHP_CLOCK_DERIVE_ID(9, 1, 1, 0x3f, 31)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2](#a75fb3dc587c912a5a961dfcd61066e09)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM2（SERCOM2）。

<a id="r_a893c130bcc447db2b076b694614be658"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3 MCHP_CLOCK_DERIVE_ID(9, 1, 2, 0x3f, 32)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3](#a893c130bcc447db2b076b694614be658)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM3（SERCOM3）。

<a id="r_ab86030aa3e1e599bbc46211ca4044488"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4 MCHP_CLOCK_DERIVE_ID(9, 1, 3, 0x3f, 33)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4](#ab86030aa3e1e599bbc46211ca4044488)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM4（SERCOM4）。

<a id="r_ae99c49a5fc48f51bc151d03d8f383cc6"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5 MCHP_CLOCK_DERIVE_ID(9, 1, 4, 0x3f, 34)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5](#ae99c49a5fc48f51bc151d03d8f383cc6)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM5（SERCOM5）。

<a id="r_a46866c2dbf37cfdb1fa0af71e3bbd169"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM6 MCHP_CLOCK_DERIVE_ID(9, 1, 5, 0x3f, 35)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM6](#a46866c2dbf37cfdb1fa0af71e3bbd169)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM6（SERCOM6）。

<a id="r_a2b3d5ae8de4926fa8a9fbc87a68528f8"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM7 MCHP_CLOCK_DERIVE_ID(9, 1, 6, 0x3f, 36)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM7](#a2b3d5ae8de4926fa8a9fbc87a68528f8)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM7（SERCOM7）。

<a id="r_af41538eaf6905f9c2f980270e6df35da"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM8 MCHP_CLOCK_DERIVE_ID(9, 1, 7, 0x3f, 37)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM8](#af41538eaf6905f9c2f980270e6df35da)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM8（SERCOM8）。

<a id="r_a3e7e6e8fb0f503df5461f7bebbca1d79"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM9 MCHP_CLOCK_DERIVE_ID(9, 1, 8, 0x3f, 38)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SERCOM9](#a3e7e6e8fb0f503df5461f7bebbca1d79)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SERCOM9（SERCOM9）。

<a id="r_ad3a8bd23b104522ca890997304fc21d4"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC0 MCHP_CLOCK_DERIVE_ID(9, 1, 9, 0x3f, 39)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC0](#ad3a8bd23b104522ca890997304fc21d4)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC0（TCC0）。

<a id="r_ad60be2a1615dfd0de08bb0960e4e4526"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC1 MCHP_CLOCK_DERIVE_ID(9, 1, 10, 0x3f, 40)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC1](#ad60be2a1615dfd0de08bb0960e4e4526)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC1（TCC1）。

<a id="r_a7f0be35a75e900699a10445d7a8463ca"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC2 MCHP_CLOCK_DERIVE_ID(9, 1, 11, 0x3f, 41)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC2](#a7f0be35a75e900699a10445d7a8463ca)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC2（TCC2）。

<a id="r_a1c25975110ff6f0a977adb760c3eef7e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC3 MCHP_CLOCK_DERIVE_ID(9, 1, 12, 0x3f, 42)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC3](#a1c25975110ff6f0a977adb760c3eef7e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC3（TCC3）。

<a id="r_af79ecdecbec732ce71599f0311d57580"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC4 MCHP_CLOCK_DERIVE_ID(9, 1, 13, 0x3f, 43)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC4](#af79ecdecbec732ce71599f0311d57580)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC4（TCC4）。

<a id="r_ab84c014f1edb2bc7e374a3f82c2ef71d"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC5 MCHP_CLOCK_DERIVE_ID(9, 1, 14, 0x3f, 44)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC5](#ab84c014f1edb2bc7e374a3f82c2ef71d)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC5（TCC5）。

<a id="r_ae95d523e3ad45348066f68fb19622aba"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC6 MCHP_CLOCK_DERIVE_ID(9, 1, 15, 0x3f, 45)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC6](#ae95d523e3ad45348066f68fb19622aba)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC6（TCC6）。

<a id="r_ab7895a6585f7bf5959df95ee97e39622"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC7 MCHP_CLOCK_DERIVE_ID(9, 1, 16, 0x3f, 46)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC7](#ab7895a6585f7bf5959df95ee97e39622)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC7（TCC7）。

<a id="r_a9de3c13d55a896ffc8329f19a2094e7c"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC8 MCHP_CLOCK_DERIVE_ID(9, 1, 17, 0x3f, 47)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC8](#a9de3c13d55a896ffc8329f19a2094e7c)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC8（TCC8）。

<a id="r_a12f51fd17276e9342c02beb92a9c88ae"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC9 MCHP_CLOCK_DERIVE_ID(9, 1, 18, 0x3f, 48)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TCC9](#a12f51fd17276e9342c02beb92a9c88ae)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TCC9（TCC9）。

<a id="r_a5d8481769aaec20ff21d47d3ac1347e3"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_ADC MCHP_CLOCK_DERIVE_ID(9, 1, 19, 0x3f, 49)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_ADC](#a5d8481769aaec20ff21d47d3ac1347e3)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：ADC（ADC）。

<a id="r_a15b5103e5212ada5ae5da15831345e2a"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_AC MCHP_CLOCK_DERIVE_ID(9, 1, 20, 0x3f, 50)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_AC](#a15b5103e5212ada5ae5da15831345e2a)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：AC（AC）。

<a id="r_a839339c5809445addd8326f7f3988c96"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PTC MCHP_CLOCK_DERIVE_ID(9, 1, 21, 0x3f, 51)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_PTC](#a839339c5809445addd8326f7f3988c96)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：PTC（PTC）。

<a id="r_aa57bf37a708a409366d76c9d9f0b6849"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_I2S2 MCHP_CLOCK_DERIVE_ID(9, 1, 22, 0x3f, 52)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_I2S2](#aa57bf37a708a409366d76c9d9f0b6849)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：I2S2（I2S2）。

<a id="r_abb76250a336ee29295463bb757d6f59a"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_I2S1 MCHP_CLOCK_DERIVE_ID(9, 1, 23, 0x3f, 53)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_I2S1](#abb76250a336ee29295463bb757d6f59a)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：I2S1（I2S1）。

<a id="r_a4188938454ae1ed53076aaf4def7f39e"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN0 MCHP_CLOCK_DERIVE_ID(9, 1, 24, 0x3f, 54)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CAN0](#a4188938454ae1ed53076aaf4def7f39e)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CAN0（CAN0）。

<a id="r_af9fc7781311291889227f80a8af51a76"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN1 MCHP_CLOCK_DERIVE_ID(9, 1, 25, 0x3f, 55)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CAN1](#af9fc7781311291889227f80a8af51a76)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CAN1（CAN1）。

<a id="r_a6dfe9acec4b4bbb5e44ce1e887e2d56f"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN2 MCHP_CLOCK_DERIVE_ID(9, 1, 26, 0x3f, 56)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CAN2](#a6dfe9acec4b4bbb5e44ce1e887e2d56f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CAN2（CAN2）。

<a id="r_a74a08154befc4c3999e7f005ad466e66"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN3 MCHP_CLOCK_DERIVE_ID(9, 1, 27, 0x3f, 57)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CAN3](#a74a08154befc4c3999e7f005ad466e66)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CAN3（CAN3）。

<a id="r_ab8de707a2b5b6407eba398fd063ec0d7"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN4 MCHP_CLOCK_DERIVE_ID(9, 1, 28, 0x3f, 58)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CAN4](#ab8de707a2b5b6407eba398fd063ec0d7)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CAN4（CAN4）。

<a id="r_a3aecbd1ed7d3e7aad09e8324c2205199"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN5 MCHP_CLOCK_DERIVE_ID(9, 1, 29, 0x3f, 59)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_CAN5](#a3aecbd1ed7d3e7aad09e8324c2205199)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：CAN5（CAN5）。

<a id="r_a7ffbe23bf748b05798ac2398a9aad36b"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_GMAC_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 0, 0x3f, 60)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_GMAC_AHB](#a7ffbe23bf748b05798ac2398a9aad36b)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：GMAC (AHB)（GMAC (AHB)）。

<a id="r_a50b61fd3981504834eaf772233776e61"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_GMAC_APB MCHP_CLOCK_DERIVE_ID(9, 2, 1, 0x3f, 61)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_GMAC_APB](#a50b61fd3981504834eaf772233776e61)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：GMAC (APB)（GMAC (APB)）。

<a id="r_abebcb8d51eae573392d1ea85764b85c2"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SQI0 MCHP_CLOCK_DERIVE_ID(9, 2, 2, 0x3f, 62)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SQI0](#abebcb8d51eae573392d1ea85764b85c2)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SQI0（SQI0）。

<a id="r_a51d80d65010758763f39935ce960d69d"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SQI1 MCHP_CLOCK_DERIVE_ID(9, 2, 3, 0x3f, 63)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SQI1](#a51d80d65010758763f39935ce960d69d)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SQI1（SQI1）。

<a id="r_a423b4d94bc0590196a107a289fb16290"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TRNG MCHP_CLOCK_DERIVE_ID(9, 2, 4, 0x3f, 64)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_TRNG](#a423b4d94bc0590196a107a289fb16290)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：TRNG（TRNG）。

<a id="r_a60eeb69db3722ef3069d907d628681ba"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC0_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 5, 0x3f, 65)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SDHC0_AHB](#a60eeb69db3722ef3069d907d628681ba)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SDHC0 (AHB)（SDHC0 (AHB)）。

<a id="r_a7f793407401fcbb798e8549f2c9a7386"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC0_APB MCHP_CLOCK_DERIVE_ID(9, 2, 6, 0x3f, 66)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SDHC0_APB](#a7f793407401fcbb798e8549f2c9a7386)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SDHC0 (APB)（SDHC0 (APB)）。

<a id="r_ab92f4a776c3c0106d5b3a9481c970d58"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC1_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 7, 0x3f, 67)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SDHC1_AHB](#ab92f4a776c3c0106d5b3a9481c970d58)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SDHC1 (AHB)（SDHC1 (AHB)）。

<a id="r_a50f90846ae8d8a11701cdfd35296f9d0"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC1_APB MCHP_CLOCK_DERIVE_ID(9, 2, 8, 0x3f, 68)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_SDHC1_APB](#a50f90846ae8d8a11701cdfd35296f9d0)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：SDHC1 (APB)（SDHC1 (APB)）。

<a id="r_adf26d2091a06c660eabb2537163d01cd"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HUSB0 MCHP_CLOCK_DERIVE_ID(9, 2, 9, 0x3f, 69)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_HUSB0](#adf26d2091a06c660eabb2537163d01cd)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：HUSB0（HUSB0）。

<a id="r_ac5023cf90864ca0a9666e6acf77b2fd5"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HUSB1 MCHP_CLOCK_DERIVE_ID(9, 2, 10, 0x3f, 70)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_HUSB1](#ac5023cf90864ca0a9666e6acf77b2fd5)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：HUSB1（HUSB1）。

<a id="r_ada6c6291b51b7fe41ee0925e31628ff9"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 11, 0x3f, 71)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_EBI_AHB](#ada6c6291b51b7fe41ee0925e31628ff9)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：EBI (AHB)（EBI (AHB)）。

<a id="r_a9fb89fb266e6bee7606a1de146a33d4f"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_APB MCHP_CLOCK_DERIVE_ID(9, 2, 12, 0x3f, 72)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_EBI_APB](#a9fb89fb266e6bee7606a1de146a33d4f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：EBI (APB)（EBI (APB)）。

<a id="r_a7d9495c1ea1942c4d2fc069a29e23d6a"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HSM MCHP_CLOCK_DERIVE_ID(9, 2, 13, 0x3f, 73)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_HSM](#a7d9495c1ea1942c4d2fc069a29e23d6a)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：HSM（HSM）。

<a id="r_a3b262781fb6df5602412c4c924566d49"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MLB_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 14, 0x3f, 74)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_MLB_AHB](#a3b262781fb6df5602412c4c924566d49)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：MLB (AHB)（MLB (AHB)）。

<a id="r_a53efff05de34c5a6cd5be089eaa4686f"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MLB_APB MCHP_CLOCK_DERIVE_ID(9, 2, 15, 0x3f, 75)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_MLB_APB](#a53efff05de34c5a6cd5be089eaa4686f)、[MCHP_CLOCK_DERIVE_ID](#a0ebea68f214a63653aa0eaab0cf9c419)。

MCLK 外设标识符（Peripheral ID）：MLB (APB)（MLB (APB)）。

<a id="r_a5884aa8fb4b6841cf3b36f8df64136d1"></a>

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MAX (75)
```

相关声明：[CLOCK_MCHP_MCLKPERIPH_ID_MAX](#a5884aa8fb4b6841cf3b36f8df64136d1)。

MCLK 外设标识符（Peripheral IDs）的最大索引。

## 4.2\_详细说明（Detailed Documentation）

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

<a id="a1a74c6aba140e901e99ea7a16ddfed43"></a>

### `CLOCK_MCHP_DPLL1_ID_OUT0`

```c
#define CLOCK_MCHP_DPLL1_ID_OUT0 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 4)
```

`DPLL1` 输出（Output）0 的时钟标识符（Clock ID）。

<a id="a0ebfe2b27af57483626a43b317b8b0c4"></a>

### `CLOCK_MCHP_DPLL1_ID_OUT1`

```c
#define CLOCK_MCHP_DPLL1_ID_OUT1 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 5)
```

`DPLL1` 输出（Output）1 的时钟标识符（Clock ID）。

<a id="ac189dc0b4442d365774ab62e8895046b"></a>

### `CLOCK_MCHP_DPLL1_ID_OUT2`

```c
#define CLOCK_MCHP_DPLL1_ID_OUT2 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 6)
```

`DPLL1` 输出（Output）2 的时钟标识符（Clock ID）。

<a id="a8650089f16b6bcce0a580aab140091ea"></a>

### `CLOCK_MCHP_DPLL1_ID_OUT3`

```c
#define CLOCK_MCHP_DPLL1_ID_OUT3 MCHP_CLOCK_DERIVE_ID(3, 0x3f, 0x3f, 0x3f, 7)
```

`DPLL1` 输出（Output）3 的时钟标识符（Clock ID）。

<a id="a621a8f4faee2aa6d0d4d8af8609da0e9"></a>

### `CLOCK_MCHP_DPLL_ID_DPLL0`

```c
#define CLOCK_MCHP_DPLL_ID_DPLL0 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 1, 0)
```

`DPLL0` 时钟标识符（Clock ID）。

<a id="a971daee0119b24a95002e99dc33a8547"></a>

### `CLOCK_MCHP_DPLL_ID_DPLL1`

```c
#define CLOCK_MCHP_DPLL_ID_DPLL1 MCHP_CLOCK_DERIVE_ID(2, 0x3f, 0x3f, 2, 1)
```

`DPLL1` 时钟标识符（Clock ID）。

<a id="a535adb887a7c5c21a1a88f0bf450e5ed"></a>

### `CLOCK_MCHP_DPLL_ID_MAX`

```c
#define CLOCK_MCHP_DPLL_ID_MAX (1)
```

数字锁相环（DPLL）时钟标识符（Clock IDs）的最大索引。

<a id="a1d020421206c10005772bc3912989fa6"></a>

### `CLOCK_MCHP_DPLL_OUT_ID_MAX`

```c
#define CLOCK_MCHP_DPLL_OUT_ID_MAX (7)
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

<a id="a3f6397604e3735e9aeadc77ddf03607c"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN12`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN12 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 12)
```

通用时钟发生器（Generic Clock Generator）12 的标识符（ID）。

<a id="ac918ff9571138d2c907c16b4878301b0"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN13`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN13 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 13)
```

通用时钟发生器（Generic Clock Generator）13 的标识符（ID）。

<a id="afef541bf3639fc88967d7f776f08951c"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN14`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN14 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 14)
```

通用时钟发生器（Generic Clock Generator）14 的标识符（ID）。

<a id="aa9cd23b9abd14e0e1fb8b996840ccee2"></a>

### `CLOCK_MCHP_GCLKGEN_ID_GEN15`

```c
#define CLOCK_MCHP_GCLKGEN_ID_GEN15 MCHP_CLOCK_DERIVE_ID(6, 0x3f, 0x3f, 0x3f, 15)
```

通用时钟发生器（Generic Clock Generator）15 的标识符（ID）。

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
#define CLOCK_MCHP_GCLKGEN_ID_MAX (15)
```

通用时钟发生器标识符（Generic Clock Generator IDs）的最大索引。

<a id="a8558308cb89c99326b165a7b12b14ff1"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_AC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_AC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 42, 43)
```

GCLK 外设标识符（Peripheral ID）：AC (模拟比较器)（AC (Analog Comparator)）。

<a id="a845a53053a861de67ebfa150bff389ff"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_ADC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_ADC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 41, 42)
```

GCLK 外设标识符（Peripheral ID）：ADC（ADC）。

<a id="ae251d4719eb378734e3cb01c9f5828d8"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CAN0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 46, 47)
```

GCLK 外设标识符（Peripheral ID）：CAN0（CAN0）。

<a id="a2e77a06b25293f4152b0f2399ab32982"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CAN1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 47, 48)
```

GCLK 外设标识符（Peripheral ID）：CAN1（CAN1）。

<a id="a6ff5711e8ebc4ecc25eb94a17a391e44"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CAN2`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 48, 49)
```

GCLK 外设标识符（Peripheral ID）：CAN2（CAN2）。

<a id="a13af660581f12bdd4de13d9b98af0485"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CAN3`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 49, 50)
```

GCLK 外设标识符（Peripheral ID）：CAN3（CAN3）。

<a id="a2ef048cd05f2f3b32e054b48ae6c0fa2"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CAN4`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 50, 51)
```

GCLK 外设标识符（Peripheral ID）：CAN4（CAN4）。

<a id="a959753336423094e8db5505bbd405bdf"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CAN5`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CAN5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 51, 52)
```

GCLK 外设标识符（Peripheral ID）：CAN5（CAN5）。

<a id="a4ef96507f19b49a2a10002e2603d81bf"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_CM7_TRACE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_CM7_TRACE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 63, 62)
```

GCLK 外设标识符（Peripheral ID）：CM7 跟踪（CM7 Trace）。

<a id="aeaeb9a032e3fa5a00199ef27c2a5ec30"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EIC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EIC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 5, 2)
```

GCLK 外设标识符（Peripheral ID）：外部中断控制器 (EIC)（External Interrupt Controller (EIC)）。

<a id="a31aa9472c7182d16249ba7950b452c14"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 6, 3)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 0（Event System Channel 0）。

<a id="a370930d5d12099ec34871a27cee5c8e2"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 7, 4)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 1（Event System Channel 1）。

<a id="aeb43cfd70588d9f660e8965516480191"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH10 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 16, 13)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 10（Event System Channel 10）。

<a id="a93e2a650425a0bb9014c56d848c039bb"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH11 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 17, 14)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 11（Event System Channel 11）。

<a id="a6966d71c9da4ce1803c48dc088818401"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 8, 5)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 2（Event System Channel 2）。

<a id="a5d98273862a2323e050874755da0c840"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH3 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 9, 6)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 3（Event System Channel 3）。

<a id="a24855b6b55dc3eb9efba6476d6d930e8"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH4 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 10, 7)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 4（Event System Channel 4）。

<a id="a6bb92b5d57c58e6b1ab083504bbb3756"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH5 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 11, 8)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 5（Event System Channel 5）。

<a id="ae2404c8e3bce6bd9b01903a9ad942d35"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 12, 9)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 6（Event System Channel 6）。

<a id="a852a5424cc73a5e75fcd7b151e7dd767"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH7 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 13, 10)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 7（Event System Channel 7）。

<a id="a9ff8a7f89700d95e431e6d0c12869b56"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH8 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 14, 11)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 8（Event System Channel 8）。

<a id="ad7112111ef68955636866ec0adb0e71e"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_EVSYS_CH9 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 15, 12)
```

GCLK 外设标识符（Peripheral ID）：事件系统通道 9（Event System Channel 9）。

<a id="a8f21248b0662fee58bbeb9752de950d4"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_MSR MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 3, 0)
```

GCLK 外设标识符（Peripheral ID）：频率计测量（Frequency Meter Measure）。

<a id="a0da9e951ad59ea7ffa1b3a0586203202"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_FREQM_REF MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 4, 1)
```

GCLK 外设标识符（Peripheral ID）：频率计参考（Frequency Meter Reference）。

<a id="a7aac132e47cc05e97a07fa47fe8e53d6"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_GMAC_TSU`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_GMAC_TSU MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 55, 54)
```

GCLK 外设标识符（Peripheral ID）：GMAC TSU（GMAC TSU）。

<a id="a48964f392774fac761a2290d265ecac1"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_GMAC_TX`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_GMAC_TX MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 54, 53)
```

GCLK 外设标识符（Peripheral ID）：GMAC TX（GMAC TX）。

<a id="a1799a6e482e647dbcdf98c8a65bdfd97"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_I2S0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_I2S0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 44, 45)
```

GCLK 外设标识符（Peripheral ID）：I2S0（I2S0）。

<a id="a79c9ae703ad391e68221c61bd17b25bb"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_I2S1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_I2S1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 45, 46)
```

GCLK 外设标识符（Peripheral ID）：I2S1（I2S1）。

<a id="a9fb0644f504a830a4e324f792815ae98"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_MAX`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_MAX (62)
```

GCLK 外设标识符（Peripheral IDs）的最大索引。

<a id="a075962550c0db084f0fa4fef2746eec3"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_MLB`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_MLB MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 62, 61)
```

GCLK 外设标识符（Peripheral ID）：MLB（MLB）。

<a id="a65c9bc79d0b5edd7dcc8a6178a600127"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_PTC`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_PTC MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 43, 44)
```

GCLK 外设标识符（Peripheral ID）：PTC (外设触摸控制器)（PTC (Peripheral Touch Controller)）。

<a id="a49f7260022baa903874ca45c038cb50e"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SDHC0_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC0_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 58, 57)
```

GCLK 外设标识符（Peripheral ID）：SDHC0 核心（SDHC0 Core）。

<a id="a88e3bdc5decf97eb3c5ce756397ddff1"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SDHC0_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 59, 58)
```

GCLK 外设标识符（Peripheral ID）：SDHC0 慢速（SDHC0 Slow）。

<a id="aec21c0f16ae1ad3205dd08582677616c"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SDHC1_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC1_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 60, 59)
```

GCLK 外设标识符（Peripheral ID）：SDHC1 核心（SDHC1 Core）。

<a id="a6de1f5509f4cd074f13df6ae62b5183f"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SDHC1_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SDHC1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 61, 60)
```

GCLK 外设标识符（Peripheral ID）：SDHC1 慢速（SDHC1 Slow）。

<a id="a88f1128166176ebfc0a41dd496186300"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 21, 25)
```

GCLK 外设标识符（Peripheral ID）：SERCOM0 核心 时钟（SERCOM0 Core clock）。

<a id="a2bb7a4f72e45c2fb5f449b6b3f1b4520"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM0_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 15)
```

GCLK 外设标识符（Peripheral ID）：SERCOM0 慢速 时钟（SERCOM0 Slow clock）。

<a id="ab3ef99c62a821f4e5fe1f800de6561c2"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 22, 26)
```

GCLK 外设标识符（Peripheral ID）：SERCOM1 核心 时钟（SERCOM1 Core clock）。

<a id="a726fe192480ed57fbdc3e77cc1133c89"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM1_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 16)
```

GCLK 外设标识符（Peripheral ID）：SERCOM1 慢速 时钟（SERCOM1 Slow clock）。

<a id="ab0668a32e7385c8629b26cd396e6beaa"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 23, 27)
```

GCLK 外设标识符（Peripheral ID）：SERCOM2 核心 时钟（SERCOM2 Core clock）。

<a id="a99d3f0a1c9e10f405c761ae6f3bf2744"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM2_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 18)
```

GCLK 外设标识符（Peripheral ID）：SERCOM2 慢速 时钟（SERCOM2 Slow clock）。

<a id="a155a02aa8799940dd0c59efac25e5bbc"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 24, 28)
```

GCLK 外设标识符（Peripheral ID）：SERCOM3 核心 时钟（SERCOM3 Core clock）。

<a id="a08fb53b9b65e5743900bd6a4179925d3"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM3_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 19)
```

GCLK 外设标识符（Peripheral ID）：SERCOM3 慢速 时钟（SERCOM3 Slow clock）。

<a id="a77eb95730d000556c3b32a7bcf152913"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 25, 29)
```

GCLK 外设标识符（Peripheral ID）：SERCOM4 核心 时钟（SERCOM4 Core clock）。

<a id="accbd9b23f933a8bae611a00019c5eb50"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM4_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 18, 17)
```

GCLK 外设标识符（Peripheral ID）：SERCOM4 慢速 时钟（SERCOM4 Slow clock）。

<a id="a4b1126fa67b001d9d086874d8536fb48"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 26, 30)
```

GCLK 外设标识符（Peripheral ID）：SERCOM5 核心 时钟（SERCOM5 Core clock）。

<a id="a680eff3630a7446292705a3c29098510"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM5_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 20)
```

GCLK 外设标识符（Peripheral ID）：SERCOM5 慢速 时钟（SERCOM5 Slow clock）。

<a id="a8b7161f3cedb7e5e39cc5d98498e262c"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 27, 31)
```

GCLK 外设标识符（Peripheral ID）：SERCOM6 核心 时钟（SERCOM6 Core clock）。

<a id="a8aaeb571901ab3b932c93aea8f67f39a"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM6_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 19, 21)
```

GCLK 外设标识符（Peripheral ID）：SERCOM6 慢速 时钟（SERCOM6 Slow clock）。

<a id="a12909dbedec1469b89c431395b9fb6eb"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 28, 32)
```

GCLK 外设标识符（Peripheral ID）：SERCOM7 核心 时钟（SERCOM7 Core clock）。

<a id="a277cd1054793077c5c67551bf4a38df5"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM7_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 22)
```

GCLK 外设标识符（Peripheral ID）：SERCOM7 慢速 时钟（SERCOM7 Slow clock）。

<a id="ac7ace4228af8c8eab533d58f8f5ea5d0"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM8_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM8_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 29, 33)
```

GCLK 外设标识符（Peripheral ID）：SERCOM8 核心 时钟（SERCOM8 Core clock）。

<a id="ad7205a316c6b5a9a9700824d8435f614"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM8_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM8_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 23)
```

GCLK 外设标识符（Peripheral ID）：SERCOM8 慢速 时钟（SERCOM8 Slow clock）。

<a id="a4b3497b52195d9237be7c89deb290b0e"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM9_CORE`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM9_CORE MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 30, 34)
```

GCLK 外设标识符（Peripheral ID）：SERCOM9 核心 时钟（SERCOM9 Core clock）。

<a id="a7820807d16cbd8f23d42c2deb0e7ad18"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SERCOM9_SLOW`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SERCOM9_SLOW MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 20, 24)
```

GCLK 外设标识符（Peripheral ID）：SERCOM9 慢速 时钟（SERCOM9 Slow clock）。

<a id="a7290dbd41a053370f380d7a5524ef995"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SQI0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SQI0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 56, 55)
```

GCLK 外设标识符（Peripheral ID）：SQI0（SQI0）。

<a id="acbfa372bc7330c35727bd2af6da938d1"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_SQI1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_SQI1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 57, 56)
```

GCLK 外设标识符（Peripheral ID）：SQI1（SQI1）。

<a id="af3614ec46e49df22dc37768df6e9c12b"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC0`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC0 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 31, 35)
```

GCLK 外设标识符（Peripheral ID）：TCC0（TCC0）。

<a id="a253908d056c2ac97302065d9c0eb1cc4"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC1`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC1 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 32, 36)
```

GCLK 外设标识符（Peripheral ID）：TCC1（TCC1）。

<a id="ae4ebf71771a1435faa34293290ed06f0"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC2`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC2 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 33, 37)
```

GCLK 外设标识符（Peripheral ID）：TCC2（TCC2）。

<a id="a14a655c0aead0534f6915a1994a6ed1d"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC6`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC6 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 37, 38)
```

GCLK 外设标识符（Peripheral ID）：TCC6（TCC6）。

<a id="a89967af8e20803cdb7e41890c4a4a143"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC7`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC7 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 38, 39)
```

GCLK 外设标识符（Peripheral ID）：TCC7（TCC7）。

<a id="a9aab46e09874a681b735dad66a352baa"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC8`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC8 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 39, 40)
```

GCLK 外设标识符（Peripheral ID）：TCC8（TCC8）。

<a id="abf072528495ffa4fc031d11c2a0c5654"></a>

### `CLOCK_MCHP_GCLKPERIPH_ID_TCC9`

```c
#define CLOCK_MCHP_GCLKPERIPH_ID_TCC9 MCHP_CLOCK_DERIVE_ID(7, 0x3f, 0x3f, 40, 41)
```

GCLK 外设标识符（Peripheral ID）：TCC9（TCC9）。

<a id="ac40643badee3512255e142465f0f31b4"></a>

### `CLOCK_MCHP_MCLKDOMAIN_ID_CPU`

```c
#define CLOCK_MCHP_MCLKDOMAIN_ID_CPU MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 0)
```

主时钟域标识符（Main Clock Domain ID）：CPU。

<a id="ad038d0e6ed7f444a98d1f12a4f7a213c"></a>

### `CLOCK_MCHP_MCLKDOMAIN_ID_PERIPH`

```c
#define CLOCK_MCHP_MCLKDOMAIN_ID_PERIPH MCHP_CLOCK_DERIVE_ID(8, 0x3f, 0x3f, 0x3f, 1)
```

主时钟域标识符（Main Clock Domain ID）：外设（Peripheral）。

<a id="adec6556749cbc3c25b049fd700c36e94"></a>

### `CLOCK_MCHP_MCLKDOMAIN_MAX`

```c
#define CLOCK_MCHP_MCLKDOMAIN_MAX (1)
```

主时钟域标识符（Main Clock Domain IDs）的最大索引。

<a id="a15b5103e5212ada5ae5da15831345e2a"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_AC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_AC MCHP_CLOCK_DERIVE_ID(9, 1, 20, 0x3f, 50)
```

MCLK 外设标识符（Peripheral ID）：AC（AC）。

<a id="a5d8481769aaec20ff21d47d3ac1347e3"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_ADC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_ADC MCHP_CLOCK_DERIVE_ID(9, 1, 19, 0x3f, 49)
```

MCLK 外设标识符（Peripheral ID）：ADC（ADC）。

<a id="a78b45760ed8d6907b19a42af13c5e950"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_BOOT_ROM_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BOOT_ROM_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 28, 0x3f, 26)
```

MCLK 外设标识符（Peripheral ID）：启动 ROM (AHB)（BOOT ROM (AHB)）。

<a id="a1421a1cc99b78e1527211fc83ca90c63"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_BOOT_ROM_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BOOT_ROM_APB MCHP_CLOCK_DERIVE_ID(9, 0, 29, 0x3f, 27)
```

MCLK 外设标识符（Peripheral ID）：启动 ROM (APB)（BOOT ROM (APB)）。

<a id="a2533096560d799f417ae82fbede412ba"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_BUS_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BUS_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 26, 0x3f, 24)
```

MCLK 外设标识符（Peripheral ID）：BUS (AHB)（BUS (AHB)）。

<a id="a20188b847fdd4434a8e6bf4f11f3fb8e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_BUS_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_BUS_APB MCHP_CLOCK_DERIVE_ID(9, 0, 27, 0x3f, 25)
```

MCLK 外设标识符（Peripheral ID）：BUS (APB)（BUS (APB)）。

<a id="a4188938454ae1ed53076aaf4def7f39e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CAN0`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN0 MCHP_CLOCK_DERIVE_ID(9, 1, 24, 0x3f, 54)
```

MCLK 外设标识符（Peripheral ID）：CAN0（CAN0）。

<a id="af9fc7781311291889227f80a8af51a76"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CAN1`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN1 MCHP_CLOCK_DERIVE_ID(9, 1, 25, 0x3f, 55)
```

MCLK 外设标识符（Peripheral ID）：CAN1（CAN1）。

<a id="a6dfe9acec4b4bbb5e44ce1e887e2d56f"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CAN2`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN2 MCHP_CLOCK_DERIVE_ID(9, 1, 26, 0x3f, 56)
```

MCLK 外设标识符（Peripheral ID）：CAN2（CAN2）。

<a id="a74a08154befc4c3999e7f005ad466e66"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CAN3`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN3 MCHP_CLOCK_DERIVE_ID(9, 1, 27, 0x3f, 57)
```

MCLK 外设标识符（Peripheral ID）：CAN3（CAN3）。

<a id="ab8de707a2b5b6407eba398fd063ec0d7"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CAN4`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN4 MCHP_CLOCK_DERIVE_ID(9, 1, 28, 0x3f, 58)
```

MCLK 外设标识符（Peripheral ID）：CAN4（CAN4）。

<a id="a3aecbd1ed7d3e7aad09e8324c2205199"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_CAN5`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_CAN5 MCHP_CLOCK_DERIVE_ID(9, 1, 29, 0x3f, 59)
```

MCLK 外设标识符（Peripheral ID）：CAN5（CAN5）。

<a id="a1ea38f3f64ebc1ec538530a23920f45d"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DMAC_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 24, 0x3f, 22)
```

MCLK 外设标识符（Peripheral ID）：DMAC (AHB)（DMAC (AHB)）。

<a id="ae0a16f13ccf85d54ebc961054850376c"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DMAC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DMAC_APB MCHP_CLOCK_DERIVE_ID(9, 0, 25, 0x3f, 23)
```

MCLK 外设标识符（Peripheral ID）：DMAC (APB)（DMAC (APB)）。

<a id="a1ca73dcf5baf2ccecc4f607d6b3051c5"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DRMTCM`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DRMTCM MCHP_CLOCK_DERIVE_ID(9, 0, 19, 0x3f, 17)
```

MCLK 外设标识符（Peripheral ID）：DRMTCM（DRMTCM）。

<a id="a5f1c9309e3eb0586eb1f765536b4346e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 0, 0x3f, 0)
```

MCLK 外设标识符（Peripheral ID）：DSU (AHB)（DSU (AHB)）。

<a id="a25521d18a70eacc1ad5cc347feb0765e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_DSU_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_DSU_APB MCHP_CLOCK_DERIVE_ID(9, 0, 1, 0x3f, 1)
```

MCLK 外设标识符（Peripheral ID）：DSU (APB)（DSU (APB)）。

<a id="ada6c6291b51b7fe41ee0925e31628ff9"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_EBI_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 11, 0x3f, 71)
```

MCLK 外设标识符（Peripheral ID）：EBI (AHB)（EBI (AHB)）。

<a id="a9fb89fb266e6bee7606a1de146a33d4f"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_EBI_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EBI_APB MCHP_CLOCK_DERIVE_ID(9, 2, 12, 0x3f, 72)
```

MCLK 外设标识符（Peripheral ID）：EBI (APB)（EBI (APB)）。

<a id="afb137dc52e627ab615dea380c58a44da"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_EIC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EIC MCHP_CLOCK_DERIVE_ID(9, 0, 16, 0x3f, 14)
```

MCLK 外设标识符（Peripheral ID）：EIC（EIC）。

<a id="a1f3f4077f0f5be1dd872c8a18052317e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_EVSYS`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_EVSYS MCHP_CLOCK_DERIVE_ID(9, 0, 30, 0x3f, 28)
```

MCLK 外设标识符（Peripheral ID）：EVSYS（EVSYS）。

<a id="af85028f923174b11e44d1fc9043c5c75"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 4, 0x3f, 4)
```

MCLK 外设标识符（Peripheral ID）：FCR (AHB)（FCR (AHB)）。

<a id="a8427e8e5faebe7f66dbfe1554d024c6e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FCR_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCR_APB MCHP_CLOCK_DERIVE_ID(9, 0, 5, 0x3f, 5)
```

MCLK 外设标识符（Peripheral ID）：FCR (APB)（FCR (APB)）。

<a id="a55391bcfa4db8dfdf6d7fbfbfbc9626f"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 2, 0x3f, 2)
```

MCLK 外设标识符（Peripheral ID）：FCW (AHB)（FCW (AHB)）。

<a id="a979b800be2dabf8c744fef8295cf1bcc"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FCW_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FCW_APB MCHP_CLOCK_DERIVE_ID(9, 0, 3, 0x3f, 3)
```

MCLK 外设标识符（Peripheral ID）：FCW (APB)（FCW (APB)）。

<a id="a37509ecf92c06e1f063a8c78c8fa0fe7"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_FREQM`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_FREQM MCHP_CLOCK_DERIVE_ID(9, 0, 13, 0x3f, 11)
```

MCLK 外设标识符（Peripheral ID）：FREQM（FREQM）。

<a id="a7ffbe23bf748b05798ac2398a9aad36b"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_GMAC_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_GMAC_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 0, 0x3f, 60)
```

MCLK 外设标识符（Peripheral ID）：GMAC (AHB)（GMAC (AHB)）。

<a id="a50b61fd3981504834eaf772233776e61"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_GMAC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_GMAC_APB MCHP_CLOCK_DERIVE_ID(9, 2, 1, 0x3f, 61)
```

MCLK 外设标识符（Peripheral ID）：GMAC (APB)（GMAC (APB)）。

<a id="a7d9495c1ea1942c4d2fc069a29e23d6a"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_HSM`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HSM MCHP_CLOCK_DERIVE_ID(9, 2, 13, 0x3f, 73)
```

MCLK 外设标识符（Peripheral ID）：HSM（HSM）。

<a id="adf26d2091a06c660eabb2537163d01cd"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_HUSB0`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HUSB0 MCHP_CLOCK_DERIVE_ID(9, 2, 9, 0x3f, 69)
```

MCLK 外设标识符（Peripheral ID）：HUSB0（HUSB0）。

<a id="ac5023cf90864ca0a9666e6acf77b2fd5"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_HUSB1`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_HUSB1 MCHP_CLOCK_DERIVE_ID(9, 2, 10, 0x3f, 70)
```

MCLK 外设标识符（Peripheral ID）：HUSB1（HUSB1）。

<a id="abb76250a336ee29295463bb757d6f59a"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_I2S1`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_I2S1 MCHP_CLOCK_DERIVE_ID(9, 1, 23, 0x3f, 53)
```

MCLK 外设标识符（Peripheral ID）：I2S1（I2S1）。

<a id="aa57bf37a708a409366d76c9d9f0b6849"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_I2S2`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_I2S2 MCHP_CLOCK_DERIVE_ID(9, 1, 22, 0x3f, 52)
```

MCLK 外设标识符（Peripheral ID）：I2S2（I2S2）。

<a id="a5884aa8fb4b6841cf3b36f8df64136d1"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_MAX`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MAX (75)
```

MCLK 外设标识符（Peripheral IDs）的最大索引。

<a id="a95bb042e234637438789ac12ba64a577"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MCRAMC MCHP_CLOCK_DERIVE_ID(9, 0, 20, 0x3f, 18)
```

MCLK 外设标识符（Peripheral ID）：MCRAMC（MCRAMC）。

<a id="a3b262781fb6df5602412c4c924566d49"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_MLB_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MLB_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 14, 0x3f, 74)
```

MCLK 外设标识符（Peripheral ID）：MLB (AHB)（MLB (AHB)）。

<a id="a53efff05de34c5a6cd5be089eaa4686f"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_MLB_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_MLB_APB MCHP_CLOCK_DERIVE_ID(9, 2, 15, 0x3f, 75)
```

MCLK 外设标识符（Peripheral ID）：MLB (APB)（MLB (APB)）。

<a id="a721267129ed0b4edf349298f972ae3af"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSC32KCTRL MCHP_CLOCK_DERIVE_ID(9, 0, 10, 0x3f, 10)
```

MCLK 外设标识符（Peripheral ID）：OSC32KCTRL（OSC32KCTRL）。

<a id="af4fe59e6405058b34f7205f58631c38e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_OSCCTRL MCHP_CLOCK_DERIVE_ID(9, 0, 9, 0x3f, 9)
```

MCLK 外设标识符（Peripheral ID）：OSCCTRL（OSCCTRL）。

<a id="ad63bf9ad8a02a102f6cc0b4ebcecd8ae"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PAC_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 17, 0x3f, 15)
```

MCLK 外设标识符（Peripheral ID）：PAC (AHB)（PAC (AHB)）。

<a id="a574e9bee5faec84626fa1e9ef679e71a"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PAC_APB MCHP_CLOCK_DERIVE_ID(9, 0, 18, 0x3f, 16)
```

MCLK 外设标识符（Peripheral ID）：PAC (APB)（PAC (APB)）。

<a id="a4f661f6845c462308dbd9dc635eb0216"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PM`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PM MCHP_CLOCK_DERIVE_ID(9, 0, 6, 0x3f, 6)
```

MCLK 外设标识符（Peripheral ID）：PM（PM）。

<a id="a240a6cdd06427460288028a7cd0a7593"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PORT_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_AHB MCHP_CLOCK_DERIVE_ID(9, 0, 22, 0x3f, 20)
```

MCLK 外设标识符（Peripheral ID）：PORT (AHB)（PORT (AHB)）。

<a id="acadb93a9913d4622db5b6e0b7d375ef1"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PORT_APB MCHP_CLOCK_DERIVE_ID(9, 0, 23, 0x3f, 21)
```

MCLK 外设标识符（Peripheral ID）：PORT (APB)（PORT (APB)）。

<a id="a839339c5809445addd8326f7f3988c96"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_PTC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_PTC MCHP_CLOCK_DERIVE_ID(9, 1, 21, 0x3f, 51)
```

MCLK 外设标识符（Peripheral ID）：PTC（PTC）。

<a id="abf5fe57afad6b6d3f88cf4165406c468"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_RSTC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RSTC MCHP_CLOCK_DERIVE_ID(9, 0, 8, 0x3f, 8)
```

MCLK 外设标识符（Peripheral ID）：RSTC（RSTC）。

<a id="ab7ce87ea60b62f5a3d77297cd1d7d713"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_RTC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_RTC MCHP_CLOCK_DERIVE_ID(9, 0, 15, 0x3f, 13)
```

MCLK 外设标识符（Peripheral ID）：RTC（RTC）。

<a id="a60eeb69db3722ef3069d907d628681ba"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SDHC0_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC0_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 5, 0x3f, 65)
```

MCLK 外设标识符（Peripheral ID）：SDHC0 (AHB)（SDHC0 (AHB)）。

<a id="a7f793407401fcbb798e8549f2c9a7386"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SDHC0_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC0_APB MCHP_CLOCK_DERIVE_ID(9, 2, 6, 0x3f, 66)
```

MCLK 外设标识符（Peripheral ID）：SDHC0 (APB)（SDHC0 (APB)）。

<a id="ab92f4a776c3c0106d5b3a9481c970d58"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SDHC1_AHB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC1_AHB MCHP_CLOCK_DERIVE_ID(9, 2, 7, 0x3f, 67)
```

MCLK 外设标识符（Peripheral ID）：SDHC1 (AHB)（SDHC1 (AHB)）。

<a id="a50f90846ae8d8a11701cdfd35296f9d0"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SDHC1_APB`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SDHC1_APB MCHP_CLOCK_DERIVE_ID(9, 2, 8, 0x3f, 68)
```

MCLK 外设标识符（Peripheral ID）：SDHC1 (APB)（SDHC1 (APB)）。

<a id="aaca27bd670359e191ee3ded852b86e9b"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM0 MCHP_CLOCK_DERIVE_ID(9, 0, 31, 0x3f, 29)
```

MCLK 外设标识符（Peripheral ID）：SERCOM0（SERCOM0）。

<a id="ad61fa9b33a8ea563a180c95213ad1d9b"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM1 MCHP_CLOCK_DERIVE_ID(9, 1, 0, 0x3f, 30)
```

MCLK 外设标识符（Peripheral ID）：SERCOM1（SERCOM1）。

<a id="a75fb3dc587c912a5a961dfcd61066e09"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM2 MCHP_CLOCK_DERIVE_ID(9, 1, 1, 0x3f, 31)
```

MCLK 外设标识符（Peripheral ID）：SERCOM2（SERCOM2）。

<a id="a893c130bcc447db2b076b694614be658"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM3 MCHP_CLOCK_DERIVE_ID(9, 1, 2, 0x3f, 32)
```

MCLK 外设标识符（Peripheral ID）：SERCOM3（SERCOM3）。

<a id="ab86030aa3e1e599bbc46211ca4044488"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM4 MCHP_CLOCK_DERIVE_ID(9, 1, 3, 0x3f, 33)
```

MCLK 外设标识符（Peripheral ID）：SERCOM4（SERCOM4）。

<a id="ae99c49a5fc48f51bc151d03d8f383cc6"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM5 MCHP_CLOCK_DERIVE_ID(9, 1, 4, 0x3f, 34)
```

MCLK 外设标识符（Peripheral ID）：SERCOM5（SERCOM5）。

<a id="a46866c2dbf37cfdb1fa0af71e3bbd169"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM6`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM6 MCHP_CLOCK_DERIVE_ID(9, 1, 5, 0x3f, 35)
```

MCLK 外设标识符（Peripheral ID）：SERCOM6（SERCOM6）。

<a id="a2b3d5ae8de4926fa8a9fbc87a68528f8"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM7`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM7 MCHP_CLOCK_DERIVE_ID(9, 1, 6, 0x3f, 36)
```

MCLK 外设标识符（Peripheral ID）：SERCOM7（SERCOM7）。

<a id="af41538eaf6905f9c2f980270e6df35da"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM8`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM8 MCHP_CLOCK_DERIVE_ID(9, 1, 7, 0x3f, 37)
```

MCLK 外设标识符（Peripheral ID）：SERCOM8（SERCOM8）。

<a id="a3e7e6e8fb0f503df5461f7bebbca1d79"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SERCOM9`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SERCOM9 MCHP_CLOCK_DERIVE_ID(9, 1, 8, 0x3f, 38)
```

MCLK 外设标识符（Peripheral ID）：SERCOM9（SERCOM9）。

<a id="abebcb8d51eae573392d1ea85764b85c2"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SQI0`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SQI0 MCHP_CLOCK_DERIVE_ID(9, 2, 2, 0x3f, 62)
```

MCLK 外设标识符（Peripheral ID）：SQI0（SQI0）。

<a id="a51d80d65010758763f39935ce960d69d"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SQI1`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SQI1 MCHP_CLOCK_DERIVE_ID(9, 2, 3, 0x3f, 63)
```

MCLK 外设标识符（Peripheral ID）：SQI1（SQI1）。

<a id="a5ae4a436c06ce604b358096d14213da8"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_SUPC`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_SUPC MCHP_CLOCK_DERIVE_ID(9, 0, 7, 0x3f, 7)
```

MCLK 外设标识符（Peripheral ID）：SUPC（SUPC）。

<a id="ad3a8bd23b104522ca890997304fc21d4"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC0`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC0 MCHP_CLOCK_DERIVE_ID(9, 1, 9, 0x3f, 39)
```

MCLK 外设标识符（Peripheral ID）：TCC0（TCC0）。

<a id="ad60be2a1615dfd0de08bb0960e4e4526"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC1`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC1 MCHP_CLOCK_DERIVE_ID(9, 1, 10, 0x3f, 40)
```

MCLK 外设标识符（Peripheral ID）：TCC1（TCC1）。

<a id="a7f0be35a75e900699a10445d7a8463ca"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC2`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC2 MCHP_CLOCK_DERIVE_ID(9, 1, 11, 0x3f, 41)
```

MCLK 外设标识符（Peripheral ID）：TCC2（TCC2）。

<a id="a1c25975110ff6f0a977adb760c3eef7e"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC3`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC3 MCHP_CLOCK_DERIVE_ID(9, 1, 12, 0x3f, 42)
```

MCLK 外设标识符（Peripheral ID）：TCC3（TCC3）。

<a id="af79ecdecbec732ce71599f0311d57580"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC4`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC4 MCHP_CLOCK_DERIVE_ID(9, 1, 13, 0x3f, 43)
```

MCLK 外设标识符（Peripheral ID）：TCC4（TCC4）。

<a id="ab84c014f1edb2bc7e374a3f82c2ef71d"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC5`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC5 MCHP_CLOCK_DERIVE_ID(9, 1, 14, 0x3f, 44)
```

MCLK 外设标识符（Peripheral ID）：TCC5（TCC5）。

<a id="ae95d523e3ad45348066f68fb19622aba"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC6`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC6 MCHP_CLOCK_DERIVE_ID(9, 1, 15, 0x3f, 45)
```

MCLK 外设标识符（Peripheral ID）：TCC6（TCC6）。

<a id="ab7895a6585f7bf5959df95ee97e39622"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC7`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC7 MCHP_CLOCK_DERIVE_ID(9, 1, 16, 0x3f, 46)
```

MCLK 外设标识符（Peripheral ID）：TCC7（TCC7）。

<a id="a9de3c13d55a896ffc8329f19a2094e7c"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC8`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC8 MCHP_CLOCK_DERIVE_ID(9, 1, 17, 0x3f, 47)
```

MCLK 外设标识符（Peripheral ID）：TCC8（TCC8）。

<a id="a12f51fd17276e9342c02beb92a9c88ae"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TCC9`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TCC9 MCHP_CLOCK_DERIVE_ID(9, 1, 18, 0x3f, 48)
```

MCLK 外设标识符（Peripheral ID）：TCC9（TCC9）。

<a id="a9d398dd236236c3fa38dd3f4d3e79c10"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TRAM`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TRAM MCHP_CLOCK_DERIVE_ID(9, 0, 21, 0x3f, 19)
```

MCLK 外设标识符（Peripheral ID）：TRAM（TRAM）。

<a id="a423b4d94bc0590196a107a289fb16290"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_TRNG`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_TRNG MCHP_CLOCK_DERIVE_ID(9, 2, 4, 0x3f, 64)
```

MCLK 外设标识符（Peripheral ID）：TRNG（TRNG）。

<a id="a75aeee838d3138dcf67732e62cd3d879"></a>

### `CLOCK_MCHP_MCLKPERIPH_ID_WDT`

```c
#define CLOCK_MCHP_MCLKPERIPH_ID_WDT MCHP_CLOCK_DERIVE_ID(9, 0, 14, 0x3f, 12)
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


## 4.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P503_mchp_pic32cz_ca_clock.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P003_zephyr__dt-bindings__clock__mchp_pic32cm_sg_gc_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__clock__rts5912_clock.h_文件参考.md)
