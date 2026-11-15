---
id: learning.zephyr-docs.api-file-system-power-reference.page-3
title: zephyr__dt-bindings__clock__bflb_bl70xl_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl70xl__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_dt-bindings\_\_clock\_\_bflb\_bl70xl\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl70xl__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BL70XL片上系统（SoC）系列的时钟ID。

<a id="details"></a>

```c
#include "bflb_clock_common.h"
```

查看此文件的源码。

BL70XL片上系统（SoC）系列的时钟ID。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_a98ab8cde5758ae0b34c9ff16d866cbcb"></a>

```c
#define BL70XL_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

相关声明：[BL70XL_CLKID_CLK_ROOT](#a98ab8cde5758ae0b34c9ff16d866cbcb)、[BFLB_CLKID_CLK_ROOT](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#af2d6e2a7c386b50358a9cf50fc8808b3)。

根时钟（Root Clock）。

<a id="r_a83b3a0e8b4c025dcaec5b2d09213d0cc"></a>

```c
#define BL70XL_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

相关声明：[BL70XL_CLKID_CLK_RC32M](#a83b3a0e8b4c025dcaec5b2d09213d0cc)、[BFLB_CLKID_CLK_RC32M](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a48bf5d6a4379c03c7817503d7fe66c8b)。

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="r_a53b3135ed8e4dd68cd5116a84113ea9e"></a>

```c
#define BL70XL_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

相关声明：[BL70XL_CLKID_CLK_CRYSTAL](#a53b3135ed8e4dd68cd5116a84113ea9e)、[BFLB_CLKID_CLK_CRYSTAL](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a059c42552c94b942f53c644207776326)。

使用晶体（Crystal）作为时钟。

<a id="r_a57175c9e93463b63aefa1341165afb46"></a>

```c
#define BL70XL_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

相关声明：[BL70XL_CLKID_CLK_BCLK](#a57175c9e93463b63aefa1341165afb46)、[BFLB_CLKID_CLK_BCLK](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a81f8f15faf5025212dbe96417515c358)。

总线时钟（Bus Clock）。

<a id="r_a54e28cb1c7d9116dfa38c33bd7645f81"></a>

```c
#define BL70XL_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

相关声明：[BL70XL_CLKID_CLK_F32K](#a54e28cb1c7d9116dfa38c33bd7645f81)、[BFLB_CLKID_CLK_F32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a5b8eca0197f839af7776f5d02c6eab13)。

F32K 时钟（Clock）。

<a id="r_a8f4ab5ad367000e169060a31ad9cedd0"></a>

```c
#define BL70XL_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

相关声明：[BL70XL_CLKID_CLK_XTAL32K](#a8f4ab5ad367000e169060a31ad9cedd0)、[BFLB_CLKID_CLK_XTAL32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a14b75b51b81786bb7ae26070e5e41e22)。

XTAL32K 时钟（Clock）。

<a id="r_a7869f57f95cf86023c2a01a3a8269b0a"></a>

```c
#define BL70XL_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

相关声明：[BL70XL_CLKID_CLK_RC32K](#a7869f57f95cf86023c2a01a3a8269b0a)、[BFLB_CLKID_CLK_RC32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#ad2b0e7bd97598e50d10ce66d5b52a360)。

RC32K 时钟（Clock）。

<a id="r_a291d31ea87d25e5001bb99eb8ca4ea27"></a>

```c
#define BL70XL_CLKID_CLK_DLL BFLB_CLKID_CLK_PRIVATE
```

相关声明：[BL70XL_CLKID_CLK_DLL](#a291d31ea87d25e5001bb99eb8ca4ea27)、[BFLB_CLKID_CLK_PRIVATE](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#acc4f8e38984a2ec63e470b919b6d8aef)。

延迟锁定环（DLL）时钟，DLL 的标准根频率（Root Frequency）为 128 MHz。

<a id="r_a9e90b9aef4b905603248cf3c87f5b401"></a>

```c
#define BL70XL_DLL_25P6MHZ 0
```

相关声明：[BL70XL_DLL_25P6MHZ](#a9e90b9aef4b905603248cf3c87f5b401)。

ID `0`：DLL 输出（Output）25.6 MHz。

<a id="r_af75bd188a8949769ccde8e1928f9e7af"></a>

```c
#define BL70XL_DLL_42P67MHZ 1
```

相关声明：[BL70XL_DLL_42P67MHZ](#af75bd188a8949769ccde8e1928f9e7af)。

ID `1`：DLL 输出（Output）42.67 MHz。

<a id="r_a27aad9ca45c831a969917e3ce56edc0a"></a>

```c
#define BL70XL_DLL_64MHZ 2
```

相关声明：[BL70XL_DLL_64MHZ](#a27aad9ca45c831a969917e3ce56edc0a)。

ID `2`：DLL 输出（Output）64 MHz。

<a id="r_a12e221ba9d42f3315850187c99e2218e"></a>

```c
#define BL70XL_DLL_128MHZ 3
```

相关声明：[BL70XL_DLL_128MHZ](#a12e221ba9d42f3315850187c99e2218e)。

ID `3`：DLL 输出（Output）128 MHz。

## 3.2\_详细说明（Detailed Documentation）

<a id="a57175c9e93463b63aefa1341165afb46"></a>

### `BL70XL_CLKID_CLK_BCLK`

```c
#define BL70XL_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

总线时钟（Bus Clock）。

<a id="a53b3135ed8e4dd68cd5116a84113ea9e"></a>

### `BL70XL_CLKID_CLK_CRYSTAL`

```c
#define BL70XL_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

使用晶体（Crystal）作为时钟。

<a id="a291d31ea87d25e5001bb99eb8ca4ea27"></a>

### `BL70XL_CLKID_CLK_DLL`

```c
#define BL70XL_CLKID_CLK_DLL BFLB_CLKID_CLK_PRIVATE
```

延迟锁定环（DLL）时钟，DLL 的标准根频率（Root Frequency）为 128 MHz。

<a id="a54e28cb1c7d9116dfa38c33bd7645f81"></a>

### `BL70XL_CLKID_CLK_F32K`

```c
#define BL70XL_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

F32K 时钟（Clock）。

<a id="a7869f57f95cf86023c2a01a3a8269b0a"></a>

### `BL70XL_CLKID_CLK_RC32K`

```c
#define BL70XL_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

RC32K 时钟（Clock）。

<a id="a83b3a0e8b4c025dcaec5b2d09213d0cc"></a>

### `BL70XL_CLKID_CLK_RC32M`

```c
#define BL70XL_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="a98ab8cde5758ae0b34c9ff16d866cbcb"></a>

### `BL70XL_CLKID_CLK_ROOT`

```c
#define BL70XL_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

根时钟（Root Clock）。

<a id="a8f4ab5ad367000e169060a31ad9cedd0"></a>

### `BL70XL_CLKID_CLK_XTAL32K`

```c
#define BL70XL_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

XTAL32K 时钟（Clock）。

<a id="a12e221ba9d42f3315850187c99e2218e"></a>

### `BL70XL_DLL_128MHZ`

```c
#define BL70XL_DLL_128MHZ 3
```

ID `3`：DLL 输出（Output）128 MHz。

<a id="a9e90b9aef4b905603248cf3c87f5b401"></a>

### `BL70XL_DLL_25P6MHZ`

```c
#define BL70XL_DLL_25P6MHZ 0
```

ID `0`：DLL 输出（Output）25.6 MHz。

<a id="af75bd188a8949769ccde8e1928f9e7af"></a>

### `BL70XL_DLL_42P67MHZ`

```c
#define BL70XL_DLL_42P67MHZ 1
```

ID `1`：DLL 输出（Output）42.67 MHz。

<a id="a27aad9ca45c831a969917e3ce56edc0a"></a>

### `BL70XL_DLL_64MHZ`

```c
#define BL70XL_DLL_64MHZ 2
```

ID `2`：DLL 输出（Output）64 MHz。


## 3.3\_原页交叉引用（Cross References）

- [bflb_clock_common.h](../api_source_reference/P065_bflb_clock_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P063_bflb_bl70xl_clock.h_源码浏览.md)
- [BFLB_CLKID_CLK_ROOT](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#af2d6e2a7c386b50358a9cf50fc8808b3)
- [BFLB_CLKID_CLK_RC32M](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a48bf5d6a4379c03c7817503d7fe66c8b)
- [BFLB_CLKID_CLK_CRYSTAL](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a059c42552c94b942f53c644207776326)
- [BFLB_CLKID_CLK_BCLK](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a81f8f15faf5025212dbe96417515c358)
- [BFLB_CLKID_CLK_F32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a5b8eca0197f839af7776f5d02c6eab13)
- [BFLB_CLKID_CLK_XTAL32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a14b75b51b81786bb7ae26070e5e41e22)
- [BFLB_CLKID_CLK_RC32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#ad2b0e7bd97598e50d10ce66d5b52a360)
- [BFLB_CLKID_CLK_PRIVATE](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#acc4f8e38984a2ec63e470b919b6d8aef)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P002_zephyr__dt-bindings__clock__bflb_bl70x_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__drivers__charger.h_文件参考.md)
