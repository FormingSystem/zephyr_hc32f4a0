---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-11
title: zephyr__dt-bindings__timer__ti-dmtimer.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ti-dmtimer_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_dt-bindings\_\_timer\_\_ti-dmtimer.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ti-dmtimer_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Texas Instruments DM定时器的时钟源定义（Clock Source Definitions）。

查看此文件的源码。

<a id="details"></a>

Texas Instruments DM定时器的时钟源定义（Clock Source Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="define-members-0"></a>

### TI DM 定时器时钟源（Timer Clock Sources）

<a id="r_afce7900ac5feeee33ed976ce5e4983bb"></a>

```c
#define HFOSC0_CLKOUT 0x0
```

相关声明：[HFOSC0_CLKOUT](#afce7900ac5feeee33ed976ce5e4983bb)。

高频振荡器（High-frequency Oscillator）0 的时钟输出。

<a id="r_a7b8c5dabc966bba7e778da70c4fc3289"></a>

```c
#define HFOSC0_CLKOUT_32K 0x1
```

相关声明：[HFOSC0_CLKOUT_32K](#a7b8c5dabc966bba7e778da70c4fc3289)。

高频振荡器（High-frequency Oscillator）0 的 32K 时钟输出。

<a id="r_a4033be16f97416767ec9afa8f9d42782"></a>

```c
#define MAIN_PLL0_HSDIV7_CLKOUT 0x2
```

相关声明：[MAIN_PLL0_HSDIV7_CLKOUT](#a4033be16f97416767ec9afa8f9d42782)。

主 PLL0 HSDIV7 时钟输出（Clock Output）。

<a id="r_aaf219e7998b3a5bef23f8485fb283713"></a>

```c
#define CLK_12M_RC 0x3
```

相关声明：[CLK_12M_RC](#aaf219e7998b3a5bef23f8485fb283713)。

12 MHz RC 时钟（Clock）。

<a id="r_a80b3d824b30a1bfd45fa3ddbc0c48b0e"></a>

```c
#define MCU_EXT_REFCLK0 0x4
```

相关声明：[MCU_EXT_REFCLK0](#a80b3d824b30a1bfd45fa3ddbc0c48b0e)。

MCU 外部参考时钟（External Reference Clock）0。

<a id="r_a5e39a3f7f65c6da9dbf8af1616c24773"></a>

```c
#define EXT_REFCLK1 0x5
```

相关声明：[EXT_REFCLK1](#a5e39a3f7f65c6da9dbf8af1616c24773)。

外部参考时钟（External Reference Clock）1。

<a id="r_adc7b8a2eec3fbd9d178d12aab43e4a53"></a>

```c
#define CPTS_RFT_CLK 0x6
```

相关声明：[CPTS_RFT_CLK](#adc7b8a2eec3fbd9d178d12aab43e4a53)。

CPTS 参考频率测试时钟（Reference Frequency Test Clock）。

<a id="r_add9e53959e721fd72d94aada6fd644a7"></a>

```c
#define CPSW3G_CPTS_RFT_CLK 0x7
```

相关声明：[CPSW3G_CPTS_RFT_CLK](#add9e53959e721fd72d94aada6fd644a7)。

CPSW 三端口千兆交换机（3-port Gigabit Switch）的 CPTS 参考频率测试时钟（Reference Frequency Test Clock）。

<a id="r_a466f310d4134fbd27673282fcf2b58b5"></a>

```c
#define MAIN_PLL1_HSDIV3_CLKOUT 0x8
```

相关声明：[MAIN_PLL1_HSDIV3_CLKOUT](#a466f310d4134fbd27673282fcf2b58b5)。

主 PLL1 HSDIV3 时钟输出（Clock Output）。

<a id="r_abcfda4e73c50f6bc1b4994de288a9e53"></a>

```c
#define MAIN_PLL2_HSDIV6_CLKOUT 0x9
```

相关声明：[MAIN_PLL2_HSDIV6_CLKOUT](#abcfda4e73c50f6bc1b4994de288a9e53)。

主 PLL2 HSDIV6 时钟输出（Clock Output）。

<a id="r_a1fb30cdd7b825d7031dc383df4d05fb3"></a>

```c
#define CPSW3G_CPTS_GENF0 0xA
```

相关声明：[CPSW3G_CPTS_GENF0](#a1fb30cdd7b825d7031dc383df4d05fb3)。

CPSW 三端口千兆交换机（3-port Gigabit Switch）的 CPTS 功能 0 时钟（Function 0 Clock）。

<a id="r_ac0656b301b4bd5b037626f801db30b90"></a>

```c
#define CPSW3G_CPTS_GENF1 0xB
```

相关声明：[CPSW3G_CPTS_GENF1](#ac0656b301b4bd5b037626f801db30b90)。

CPSW 三端口千兆交换机（3-port Gigabit Switch）的 CPTS 功能 1 时钟（Function 1 Clock）。

<a id="r_aff31339c59fe5793e841161f51c15ba8"></a>

```c
#define CPTS_GENF1 0xC
```

相关声明：[CPTS_GENF1](#aff31339c59fe5793e841161f51c15ba8)。

CPTS 功能 1 时钟（Function 1 Clock）。

<a id="r_a347143481536492c2d02f6a7795ba0ad"></a>

```c
#define CPTS_GENF2 0xD
```

相关声明：[CPTS_GENF2](#a347143481536492c2d02f6a7795ba0ad)。

CPTS 功能 2 时钟（Function 2 Clock）。

<a id="r_a0c116cf232af3fd58907dd8509d2ff40"></a>

```c
#define CPTS_GENF3 0xE
```

相关声明：[CPTS_GENF3](#a0c116cf232af3fd58907dd8509d2ff40)。

CPTS 功能 3 时钟（Function 3 Clock）。

<a id="r_a7bbfb810dcaf68733b4f5dc58fb40a00"></a>

```c
#define CPTS_GENF4 0xF
```

相关声明：[CPTS_GENF4](#a7bbfb810dcaf68733b4f5dc58fb40a00)。

CPTS 功能 4 时钟（Function 4 Clock）。

## 11.2\_详细说明（Detailed Documentation）

<a id="aaf219e7998b3a5bef23f8485fb283713"></a>

### `CLK_12M_RC`

```c
#define CLK_12M_RC 0x3
```

12 MHz RC 时钟（Clock）。

<a id="a1fb30cdd7b825d7031dc383df4d05fb3"></a>

### `CPSW3G_CPTS_GENF0`

```c
#define CPSW3G_CPTS_GENF0 0xA
```

CPSW 三端口千兆交换机（3-port Gigabit Switch）的 CPTS 功能 0 时钟（Function 0 Clock）。

<a id="ac0656b301b4bd5b037626f801db30b90"></a>

### `CPSW3G_CPTS_GENF1`

```c
#define CPSW3G_CPTS_GENF1 0xB
```

CPSW 三端口千兆交换机（3-port Gigabit Switch）的 CPTS 功能 1 时钟（Function 1 Clock）。

<a id="add9e53959e721fd72d94aada6fd644a7"></a>

### `CPSW3G_CPTS_RFT_CLK`

```c
#define CPSW3G_CPTS_RFT_CLK 0x7
```

CPSW 三端口千兆交换机（3-port Gigabit Switch）的 CPTS 参考频率测试时钟（Reference Frequency Test Clock）。

<a id="aff31339c59fe5793e841161f51c15ba8"></a>

### `CPTS_GENF1`

```c
#define CPTS_GENF1 0xC
```

CPTS 功能 1 时钟（Function 1 Clock）。

<a id="a347143481536492c2d02f6a7795ba0ad"></a>

### `CPTS_GENF2`

```c
#define CPTS_GENF2 0xD
```

CPTS 功能 2 时钟（Function 2 Clock）。

<a id="a0c116cf232af3fd58907dd8509d2ff40"></a>

### `CPTS_GENF3`

```c
#define CPTS_GENF3 0xE
```

CPTS 功能 3 时钟（Function 3 Clock）。

<a id="a7bbfb810dcaf68733b4f5dc58fb40a00"></a>

### `CPTS_GENF4`

```c
#define CPTS_GENF4 0xF
```

CPTS 功能 4 时钟（Function 4 Clock）。

<a id="adc7b8a2eec3fbd9d178d12aab43e4a53"></a>

### `CPTS_RFT_CLK`

```c
#define CPTS_RFT_CLK 0x6
```

CPTS 参考频率测试时钟（Reference Frequency Test Clock）。

<a id="a5e39a3f7f65c6da9dbf8af1616c24773"></a>

### `EXT_REFCLK1`

```c
#define EXT_REFCLK1 0x5
```

外部参考时钟（External Reference Clock）1。

<a id="afce7900ac5feeee33ed976ce5e4983bb"></a>

### `HFOSC0_CLKOUT`

```c
#define HFOSC0_CLKOUT 0x0
```

高频振荡器（High-frequency Oscillator）0 的时钟输出。

<a id="a7b8c5dabc966bba7e778da70c4fc3289"></a>

### `HFOSC0_CLKOUT_32K`

```c
#define HFOSC0_CLKOUT_32K 0x1
```

高频振荡器（High-frequency Oscillator）0 的 32K 时钟输出。

<a id="a4033be16f97416767ec9afa8f9d42782"></a>

### `MAIN_PLL0_HSDIV7_CLKOUT`

```c
#define MAIN_PLL0_HSDIV7_CLKOUT 0x2
```

主 PLL0 HSDIV7 时钟输出（Clock Output）。

<a id="a466f310d4134fbd27673282fcf2b58b5"></a>

### `MAIN_PLL1_HSDIV3_CLKOUT`

```c
#define MAIN_PLL1_HSDIV3_CLKOUT 0x8
```

主 PLL1 HSDIV3 时钟输出（Clock Output）。

<a id="abcfda4e73c50f6bc1b4994de288a9e53"></a>

### `MAIN_PLL2_HSDIV6_CLKOUT`

```c
#define MAIN_PLL2_HSDIV6_CLKOUT 0x9
```

主 PLL2 HSDIV6 时钟输出（Clock Output）。

<a id="a80b3d824b30a1bfd45fa3ddbc0c48b0e"></a>

### `MCU_EXT_REFCLK0`

```c
#define MCU_EXT_REFCLK0 0x4
```

MCU 外部参考时钟（External Reference Clock）0。


## 11.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P864_ti-dmtimer.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P010_zephyr__drivers__tee.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__sys__winstream.h_文件参考.md)
