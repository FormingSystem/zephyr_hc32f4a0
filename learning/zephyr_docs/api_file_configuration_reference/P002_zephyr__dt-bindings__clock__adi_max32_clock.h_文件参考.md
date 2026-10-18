---
id: learning.zephyr-docs.api-file-configuration-reference.page-2
title: zephyr__dt-bindings__clock__adi_max32_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_dt-bindings\_\_clock\_\_adi\_max32\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_afe3578f3122163009070220def865b17"></a>

```c
#define ADI_MAX32_CLOCK_BUS0 0
```

相关声明：[ADI_MAX32_CLOCK_BUS0](#afe3578f3122163009070220def865b17)。

外设时钟寄存器（Peripheral Clock Register）。

<a id="r_a5b6d4b5a184d286e2353adc8fec22d94"></a>

```c
#define ADI_MAX32_CLOCK_BUS1 1
```

相关声明：[ADI_MAX32_CLOCK_BUS1](#a5b6d4b5a184d286e2353adc8fec22d94)。

<a id="r_ad6f25e814a9f2d91c4050cfd4db96975"></a>

```c
#define ADI_MAX32_CLOCK_BUS2 2
```

相关声明：[ADI_MAX32_CLOCK_BUS2](#ad6f25e814a9f2d91c4050cfd4db96975)。

<a id="r_ad28575fff49c4cb3c4b8c4180cd387de"></a>

```c
#define ADI_MAX32_PRPH_CLK_SRC_PCLK 0 /* Peripheral clock */
```

相关声明：[ADI_MAX32_PRPH_CLK_SRC_PCLK](#ad28575fff49c4cb3c4b8c4180cd387de)。

UART、看门狗定时器（WDT）等外设接口的时钟源（Clock Source）。

<a id="r_a6bc3da20a61d735c15894c7cb7f6fb88"></a>

```c
#define ADI_MAX32_PRPH_CLK_SRC_EXTCLK 1 /* External clock */
```

相关声明：[ADI_MAX32_PRPH_CLK_SRC_EXTCLK](#a6bc3da20a61d735c15894c7cb7f6fb88)。

<a id="r_a0ec9e4fb6e4522325b7c26b1aa6ff4ae"></a>

```c
#define ADI_MAX32_PRPH_CLK_SRC_IBRO 2 /* Internal Baud Rate Oscillator*/
```

相关声明：[ADI_MAX32_PRPH_CLK_SRC_IBRO](#a0ec9e4fb6e4522325b7c26b1aa6ff4ae)。

<a id="r_af9ad74e5aff66314ef7ea4bcbd58a12f"></a>

```c
#define ADI_MAX32_PRPH_CLK_SRC_ERFO 3 /* External RF Oscillator */
```

相关声明：[ADI_MAX32_PRPH_CLK_SRC_ERFO](#af9ad74e5aff66314ef7ea4bcbd58a12f)。

<a id="r_ae22725273956cf339a7aa1ab99ec9d64"></a>

```c
#define ADI_MAX32_PRPH_CLK_SRC_ERTCO 4 /* External RTC Oscillator */
```

相关声明：[ADI_MAX32_PRPH_CLK_SRC_ERTCO](#ae22725273956cf339a7aa1ab99ec9d64)。

<a id="r_ad6039fb9117f11753b062ce70ab6086c"></a>

```c
#define ADI_MAX32_PRPH_CLK_SRC_INRO 5 /* Internal Nano Ring Oscillator */
```

相关声明：[ADI_MAX32_PRPH_CLK_SRC_INRO](#ad6039fb9117f11753b062ce70ab6086c)。

<a id="r_a7cc83f5e0a532b4f59909167562042f0"></a>

```c
#define ADI_MAX32_PRPH_CLK_SRC_ISO 6 /* Internal Secondary Oscillator */
```

相关声明：[ADI_MAX32_PRPH_CLK_SRC_ISO](#a7cc83f5e0a532b4f59909167562042f0)。

<a id="r_a79b4ec22a2ad744b20511fd72f00b88b"></a>

```c
#define ADI_MAX32_PRPH_CLK_SRC_IBRO_DIV8 7 /* IBRO/8 */
```

相关声明：[ADI_MAX32_PRPH_CLK_SRC_IBRO_DIV8](#a79b4ec22a2ad744b20511fd72f00b88b)。

<a id="r_abf12d2334614747738816c67aa32b4e6"></a>

```c
#define ADI_MAX32_PRPH_CLK_SRC_IPLL 8 /* Internal Phase Lock Loop Oscillator */
```

相关声明：[ADI_MAX32_PRPH_CLK_SRC_IPLL](#abf12d2334614747738816c67aa32b4e6)。

<a id="r_ada66413c52e2d3c1d166569fb9d52a84"></a>

```c
#define ADI_MAX32_PRPH_CLK_SRC_EBO 9 /* External Base Oscillator */
```

相关声明：[ADI_MAX32_PRPH_CLK_SRC_EBO](#ada66413c52e2d3c1d166569fb9d52a84)。

## 2.2\_详细说明（Detailed Documentation）

<a id="afe3578f3122163009070220def865b17"></a>

### `ADI_MAX32_CLOCK_BUS0`

```c
#define ADI_MAX32_CLOCK_BUS0 0
```

外设时钟寄存器（Peripheral Clock Register）。

<a id="a5b6d4b5a184d286e2353adc8fec22d94"></a>

### `ADI_MAX32_CLOCK_BUS1`

```c
#define ADI_MAX32_CLOCK_BUS1 1
```

<a id="ad6f25e814a9f2d91c4050cfd4db96975"></a>

### `ADI_MAX32_CLOCK_BUS2`

```c
#define ADI_MAX32_CLOCK_BUS2 2
```

<a id="ada66413c52e2d3c1d166569fb9d52a84"></a>

### `ADI_MAX32_PRPH_CLK_SRC_EBO`

```c
#define ADI_MAX32_PRPH_CLK_SRC_EBO 9 /* External Base Oscillator */
```

<a id="af9ad74e5aff66314ef7ea4bcbd58a12f"></a>

### `ADI_MAX32_PRPH_CLK_SRC_ERFO`

```c
#define ADI_MAX32_PRPH_CLK_SRC_ERFO 3 /* External RF Oscillator */
```

<a id="ae22725273956cf339a7aa1ab99ec9d64"></a>

### `ADI_MAX32_PRPH_CLK_SRC_ERTCO`

```c
#define ADI_MAX32_PRPH_CLK_SRC_ERTCO 4 /* External RTC Oscillator */
```

<a id="a6bc3da20a61d735c15894c7cb7f6fb88"></a>

### `ADI_MAX32_PRPH_CLK_SRC_EXTCLK`

```c
#define ADI_MAX32_PRPH_CLK_SRC_EXTCLK 1 /* External clock */
```

<a id="a0ec9e4fb6e4522325b7c26b1aa6ff4ae"></a>

### `ADI_MAX32_PRPH_CLK_SRC_IBRO`

```c
#define ADI_MAX32_PRPH_CLK_SRC_IBRO 2 /* Internal Baud Rate Oscillator*/
```

<a id="a79b4ec22a2ad744b20511fd72f00b88b"></a>

### `ADI_MAX32_PRPH_CLK_SRC_IBRO_DIV8`

```c
#define ADI_MAX32_PRPH_CLK_SRC_IBRO_DIV8 7 /* IBRO/8 */
```

<a id="ad6039fb9117f11753b062ce70ab6086c"></a>

### `ADI_MAX32_PRPH_CLK_SRC_INRO`

```c
#define ADI_MAX32_PRPH_CLK_SRC_INRO 5 /* Internal Nano Ring Oscillator */
```

<a id="abf12d2334614747738816c67aa32b4e6"></a>

### `ADI_MAX32_PRPH_CLK_SRC_IPLL`

```c
#define ADI_MAX32_PRPH_CLK_SRC_IPLL 8 /* Internal Phase Lock Loop Oscillator */
```

<a id="a7cc83f5e0a532b4f59909167562042f0"></a>

### `ADI_MAX32_PRPH_CLK_SRC_ISO`

```c
#define ADI_MAX32_PRPH_CLK_SRC_ISO 6 /* Internal Secondary Oscillator */
```

<a id="ad28575fff49c4cb3c4b8c4180cd387de"></a>

### `ADI_MAX32_PRPH_CLK_SRC_PCLK`

```c
#define ADI_MAX32_PRPH_CLK_SRC_PCLK 0 /* Peripheral clock */
```

UART、看门狗定时器（WDT）等外设接口的时钟源（Clock Source）。


## 2.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_zephyr__dt-bindings__gpio__adi-sdp-120.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__dt-bindings__clock__aesc-clock-controller.h_文件参考.md)
