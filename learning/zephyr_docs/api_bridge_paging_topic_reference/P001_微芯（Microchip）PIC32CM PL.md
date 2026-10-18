---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-1
title: 微芯（Microchip）PIC32CM PL
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_微芯（Microchip）PIC32CM PL

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__pl.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_mchp_5Fclock_5Fpic32cm_5Fpl_2Eh"></a>

```c
file mchp_clock_pic32cm_pl.h
```

相关声明：[mchp_clock_pic32cm_pl.h](../api_file_interface_reference/P031_zephyr__drivers__clock_control__mchp_clock_pic32cm_pl.h_文件参考.md)。

Microchip PIC32CM PL系列的时钟控制（Clock Control）头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.2\_数据结构（Data Structures）

<a id="r_clock_5Fmchp_5Fsubsys_5Foschf_5Fconfig"></a>

```c
struct clock_mchp_subsys_oschf_config
```

相关声明：[clock_mchp_subsys_oschf_config](../clock_cmsis_model_reference/P018_clock_mchp_subsys_oschf_config_结构体.md)。

高频振荡器（High-frequency Oscillator，OSCHF）子系统配置。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga9b6955116dae7fa53c8dad373a1ef9c9"></a>

```c
typedef uint32_t * clock_mchp_rate_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[clock_mchp_rate_t](#ga9b6955116dae7fa53c8dad373a1ef9c9)。

时钟频率数据类型（clock rate datatype）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_ga6c58f134b572f42ac3cca03856468c3a"></a>

```c
enum clock_mchp_freq { CLOCK_FREQ_1KHZ = 1024 , CLOCK_FREQ_32KHZ = 32768 , CLOCK_FREQ_1MHZ = 1000000 , CLOCK_FREQ_2MHZ = 2000000 , CLOCK_FREQ_3MHZ = 3000000 , CLOCK_FREQ_4MHZ = 4000000 , CLOCK_FREQ_8MHZ = 8000000 , CLOCK_FREQ_12MHZ = 12000000 , CLOCK_FREQ_20MHZ = 20000000 , CLOCK_FREQ_24MHZ = 24000000 }
```

相关声明：[clock_mchp_freq](#ga6c58f134b572f42ac3cca03856468c3a)、[CLOCK_FREQ_1KHZ](#gga6c58f134b572f42ac3cca03856468c3aa29a78c5f4d28a252320ba789172be128)、[CLOCK_FREQ_32KHZ](#gga6c58f134b572f42ac3cca03856468c3aa539e4664a82765a25cf5c4f6451138c0)、[CLOCK_FREQ_1MHZ](#gga6c58f134b572f42ac3cca03856468c3aa573b15fb8ba6477f12fd607eebaac897)、[CLOCK_FREQ_2MHZ](#gga6c58f134b572f42ac3cca03856468c3aa9fb40e8a98b517393f77ca6f0d5b3a24)、[CLOCK_FREQ_3MHZ](#gga6c58f134b572f42ac3cca03856468c3aaf60b6260a551e23f020708f381aba34e)、[CLOCK_FREQ_4MHZ](#gga6c58f134b572f42ac3cca03856468c3aac258887a28085108578b907f8e7f2d61)、[CLOCK_FREQ_8MHZ](#gga6c58f134b572f42ac3cca03856468c3aa8c71c932640e2c3290ba139a79c33df0)、[CLOCK_FREQ_12MHZ](#gga6c58f134b572f42ac3cca03856468c3aa24645f855f7fa957422f19cc7ffca738)、[CLOCK_FREQ_20MHZ](#gga6c58f134b572f42ac3cca03856468c3aa3b829d3a31baec5bd6a59a3786443a10)、[CLOCK_FREQ_24MHZ](#gga6c58f134b572f42ac3cca03856468c3aa2b42333cebbc90cd81265b1240120307)。

常用时钟频率常量（clock frequency constants），单位为 Hz。

<a id="r_ga073dab68c78edce3985eb201a039a989"></a>

```c
enum clock_mchp_gclk_src_clock { CLOCK_MCHP_GCLK_SRC_OSCHF = 0 , CLOCK_MCHP_GCLK_SRC_OSC32K , CLOCK_MCHP_GCLK_SRC_XOSC32K , CLOCK_MCHP_GCLK_SRC_GCLKPIN , CLOCK_MCHP_GCLK_SRC_GCLKGEN1 , CLOCK_MCHP_GCLK_SRC_COUNT }
```

相关声明：[clock_mchp_gclk_src_clock](#ga073dab68c78edce3985eb201a039a989)、[CLOCK_MCHP_GCLK_SRC_OSCHF](#gga073dab68c78edce3985eb201a039a989ae064355a616a69896d7043124ee11675)、[CLOCK_MCHP_GCLK_SRC_OSC32K](#gga073dab68c78edce3985eb201a039a989a26b8d25a8d166e0b8e79c77312897145)、[CLOCK_MCHP_GCLK_SRC_XOSC32K](#gga073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380)、[CLOCK_MCHP_GCLK_SRC_GCLKPIN](#gga073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef)、[CLOCK_MCHP_GCLK_SRC_GCLKGEN1](#gga073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9)、[CLOCK_MCHP_GCLK_SRC_COUNT](#gga073dab68c78edce3985eb201a039a989ace885f772c60e22702da938ef3f62b58)。

GCLK 发生器的源时钟（source clocks）。

<a id="r_gaab34442b0d6c171691ae299675542777"></a>

```c
enum clock_mchp_gclkgen { CLOCK_MCHP_GCLKGEN_GEN0 , CLOCK_MCHP_GCLKGEN_GEN1 , CLOCK_MCHP_GCLKGEN_GEN2 , CLOCK_MCHP_GCLKGEN_GEN3 , CLOCK_MCHP_GCLKGEN_MAX }
```

相关声明：[clock_mchp_gclkgen](#gaab34442b0d6c171691ae299675542777)、[CLOCK_MCHP_GCLKGEN_GEN0](#ggaab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f)、[CLOCK_MCHP_GCLKGEN_GEN1](#ggaab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424)、[CLOCK_MCHP_GCLKGEN_GEN2](#ggaab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe)、[CLOCK_MCHP_GCLKGEN_GEN3](#ggaab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08)、[CLOCK_MCHP_GCLKGEN_MAX](#ggaab34442b0d6c171691ae299675542777aa224432a91de8df07361b1f624a11417)。

通用时钟（GCLK）发生器编号。

## 1.5\_详细说明（Detailed Documentation）

<a id="ga9b6955116dae7fa53c8dad373a1ef9c9"></a>

### `clock_mchp_rate_t`

```c
typedef uint32_t* clock_mchp_rate_t
```

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_pl.h>
```

时钟频率数据类型（clock rate datatype）。

用于设置时钟速率（Clock Rate）。

<a id="ga6c58f134b572f42ac3cca03856468c3a"></a>

### `clock_mchp_freq`

```c
enum clock_mchp_freq
```

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_pl.h>
```

常用时钟频率常量（clock frequency constants），单位为 Hz。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_FREQ_1KHZ` | 标称 1 kHz 的时钟频率（Nominal Clock Frequency），实际为 1024 Hz。 |
| `CLOCK_FREQ_32KHZ` | 32 kHz 时钟频率（Clock Frequency），实际为 32768 Hz。 |
| `CLOCK_FREQ_1MHZ` | 1 MHz 时钟频率（Clock Frequency）。 |
| `CLOCK_FREQ_2MHZ` | 2 MHz 时钟频率（Clock Frequency）。 |
| `CLOCK_FREQ_3MHZ` | 3 MHz 时钟频率（Clock Frequency）。 |
| `CLOCK_FREQ_4MHZ` | 4 MHz 时钟频率（Clock Frequency）。 |
| `CLOCK_FREQ_8MHZ` | 8 MHz 时钟频率（Clock Frequency）。 |
| `CLOCK_FREQ_12MHZ` | 12 MHz 时钟频率（Clock Frequency）。 |
| `CLOCK_FREQ_20MHZ` | 20 MHz 时钟频率（Clock Frequency）。 |
| `CLOCK_FREQ_24MHZ` | 24 MHz 时钟频率（Clock Frequency）。 |

<a id="ga073dab68c78edce3985eb201a039a989"></a>

### `clock_mchp_gclk_src_clock`

```c
enum clock_mchp_gclk_src_clock
```

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_pl.h>
```

GCLK 发生器的源时钟（source clocks）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_MCHP_GCLK_SRC_OSCHF` | 高频内部振荡器（High-frequency Internal Oscillator，OSCHF）。 |
| `CLOCK_MCHP_GCLK_SRC_OSC32K` | 内部 32 kHz 振荡器（Internal Oscillator，OSC32K）。 |
| `CLOCK_MCHP_GCLK_SRC_XOSC32K` | 外部 32 kHz 晶体振荡器（External Crystal Oscillator，XOSC32K）。 |
| `CLOCK_MCHP_GCLK_SRC_GCLKPIN` | GCLK 引脚上的外部时钟输入（External Clock Input，GCLKPIN）。 |
| `CLOCK_MCHP_GCLK_SRC_GCLKGEN1` | 通用时钟发生器 1（Generic Clock Generator 1，GCLKGEN1）的输出。 |
| `CLOCK_MCHP_GCLK_SRC_COUNT` | 可用 GLCK 时钟源数量（Number of GLCK SRC Available）。 |

<a id="gaab34442b0d6c171691ae299675542777"></a>

### `clock_mchp_gclkgen`

```c
enum clock_mchp_gclkgen
```

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_pl.h>
```

通用时钟（GCLK）发生器编号。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_MCHP_GCLKGEN_GEN0` | 通用时钟发生器（Generic Clock Generator）0。 |
| `CLOCK_MCHP_GCLKGEN_GEN1` | 通用时钟发生器（Generic Clock Generator）1。 |
| `CLOCK_MCHP_GCLKGEN_GEN2` | 通用时钟发生器（Generic Clock Generator）2。 |
| `CLOCK_MCHP_GCLKGEN_GEN3` | 通用时钟发生器（Generic Clock Generator）3。 |
| `CLOCK_MCHP_GCLKGEN_MAX` | 支持的通用时钟（GCLK）发生器数量，作为哨兵值／最大值（Sentinel/Max）。 |


## 1.6\_原页交叉引用（Cross References）

- [mchp_clock_pic32cm_pl.h](../api_file_interface_reference/P031_zephyr__drivers__clock_control__mchp_clock_pic32cm_pl.h_文件参考.md)
- [clock_mchp_subsys_oschf_config](../clock_cmsis_model_reference/P018_clock_mchp_subsys_oschf_config_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [clock_mchp_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a9b6955116dae7fa53c8dad373a1ef9c9)
- [clock_mchp_gclk_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a073dab68c78edce3985eb201a039a989)
- [clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#aab34442b0d6c171691ae299675542777)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga6c58f134b572f42ac3cca03856468c3aa29a78c5f4d28a252320ba789172be128"></a>
<a id="gga6c58f134b572f42ac3cca03856468c3aa539e4664a82765a25cf5c4f6451138c0"></a>
<a id="gga6c58f134b572f42ac3cca03856468c3aa573b15fb8ba6477f12fd607eebaac897"></a>
<a id="gga6c58f134b572f42ac3cca03856468c3aa9fb40e8a98b517393f77ca6f0d5b3a24"></a>
<a id="gga6c58f134b572f42ac3cca03856468c3aaf60b6260a551e23f020708f381aba34e"></a>
<a id="gga6c58f134b572f42ac3cca03856468c3aac258887a28085108578b907f8e7f2d61"></a>
<a id="gga6c58f134b572f42ac3cca03856468c3aa8c71c932640e2c3290ba139a79c33df0"></a>
<a id="gga6c58f134b572f42ac3cca03856468c3aa24645f855f7fa957422f19cc7ffca738"></a>
<a id="gga6c58f134b572f42ac3cca03856468c3aa3b829d3a31baec5bd6a59a3786443a10"></a>
<a id="gga6c58f134b572f42ac3cca03856468c3aa2b42333cebbc90cd81265b1240120307"></a>
<a id="gga073dab68c78edce3985eb201a039a989ae064355a616a69896d7043124ee11675"></a>
<a id="gga073dab68c78edce3985eb201a039a989a26b8d25a8d166e0b8e79c77312897145"></a>
<a id="gga073dab68c78edce3985eb201a039a989ab1561a7b07902303b17fa4bcde6b1380"></a>
<a id="gga073dab68c78edce3985eb201a039a989a5200c03ecb0051be129eefc9478ddfef"></a>
<a id="gga073dab68c78edce3985eb201a039a989a7b1da4c8c7008aced22b9dde430a7ed9"></a>
<a id="gga073dab68c78edce3985eb201a039a989ace885f772c60e22702da938ef3f62b58"></a>
<a id="ggaab34442b0d6c171691ae299675542777a048e0d6bf0287b29a7c745d8fddab11f"></a>
<a id="ggaab34442b0d6c171691ae299675542777a76ee6dd502fb7e6cbf04dd1608001424"></a>
<a id="ggaab34442b0d6c171691ae299675542777aea66b804019bdf558d09d3a56c797afe"></a>
<a id="ggaab34442b0d6c171691ae299675542777a535554f05f5a0a569a888221cd5b3f08"></a>
<a id="ggaab34442b0d6c171691ae299675542777aa224432a91de8df07361b1f624a11417"></a>

---

[返回大纲](大纲.md) · [下一章](P002_以太网桥接 API（Ethernet Bridging API）.md)
