---
id: learning.zephyr-docs.api-file-system-power-reference.page-2
title: zephyr__dt-bindings__clock__bflb_bl70x_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl70x__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_dt-bindings\_\_clock\_\_bflb\_bl70x\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl70x__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include "bflb_clock_common.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ac83b9076bd63c17c2f4d73dcaffbb82b"></a>

```c
#define BL70X_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

相关声明：[BL70X_CLKID_CLK_ROOT](#ac83b9076bd63c17c2f4d73dcaffbb82b)、[BFLB_CLKID_CLK_ROOT](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#af2d6e2a7c386b50358a9cf50fc8808b3)。

根时钟（Root Clock）。

<a id="r_a8192491fc6158e5065b2738d34881260"></a>

```c
#define BL70X_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

相关声明：[BL70X_CLKID_CLK_RC32M](#a8192491fc6158e5065b2738d34881260)、[BFLB_CLKID_CLK_RC32M](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a48bf5d6a4379c03c7817503d7fe66c8b)。

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="r_a3e76791c55a7712184f2e9e9674e88b3"></a>

```c
#define BL70X_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

相关声明：[BL70X_CLKID_CLK_CRYSTAL](#a3e76791c55a7712184f2e9e9674e88b3)、[BFLB_CLKID_CLK_CRYSTAL](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a059c42552c94b942f53c644207776326)。

使用晶体（Crystal）作为时钟。

<a id="r_a6015c9507a7a9def674cf4c98eb2654c"></a>

```c
#define BL70X_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

相关声明：[BL70X_CLKID_CLK_BCLK](#a6015c9507a7a9def674cf4c98eb2654c)、[BFLB_CLKID_CLK_BCLK](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a81f8f15faf5025212dbe96417515c358)。

总线时钟（Bus Clock）。

<a id="r_ad5388ce8c7b4cab2aa1784d38ee4e324"></a>

```c
#define BL70X_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

相关声明：[BL70X_CLKID_CLK_F32K](#ad5388ce8c7b4cab2aa1784d38ee4e324)、[BFLB_CLKID_CLK_F32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a5b8eca0197f839af7776f5d02c6eab13)。

F32K 时钟（Clock）。

<a id="r_a6e21eda5f4068542a0a6df1e7c425811"></a>

```c
#define BL70X_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

相关声明：[BL70X_CLKID_CLK_XTAL32K](#a6e21eda5f4068542a0a6df1e7c425811)、[BFLB_CLKID_CLK_XTAL32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a14b75b51b81786bb7ae26070e5e41e22)。

XTAL32K 时钟（Clock）。

<a id="r_a3abbe6ab4ce1c5b05a7eecdb861b9e15"></a>

```c
#define BL70X_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

相关声明：[BL70X_CLKID_CLK_RC32K](#a3abbe6ab4ce1c5b05a7eecdb861b9e15)、[BFLB_CLKID_CLK_RC32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#ad2b0e7bd97598e50d10ce66d5b52a360)。

RC32K 时钟（Clock）。

<a id="r_a1af3c1bff12a71ede0a4d408476c00d0"></a>

```c
#define BL70X_CLKID_CLK_DLL BFLB_CLKID_CLK_PRIVATE
```

相关声明：[BL70X_CLKID_CLK_DLL](#a1af3c1bff12a71ede0a4d408476c00d0)、[BFLB_CLKID_CLK_PRIVATE](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#acc4f8e38984a2ec63e470b919b6d8aef)。

延迟锁定环（DLL）时钟，DLL 的标准根频率（Root Frequency）为 288 MHz。

<a id="r_a8b9d59f8e8b8d4ecede95ca1cb6add32"></a>

```c
#define BL70X_DLL_57MHz 0
```

相关声明：[BL70X_DLL_57MHz](#a8b9d59f8e8b8d4ecede95ca1cb6add32)。

ID `0`：DLL 输出（Output）57 MHz。

<a id="r_ae4deecec3a8a2258dc14048b77eb013f"></a>

```c
#define BL70X_DLL_96MHz 1
```

相关声明：[BL70X_DLL_96MHz](#ae4deecec3a8a2258dc14048b77eb013f)。

ID `1`：DLL 输出（Output）96 MHz。

<a id="r_a4d9415522361115f7c81f0f267e60b1f"></a>

```c
#define BL70X_DLL_144MHz 2
```

相关声明：[BL70X_DLL_144MHz](#a4d9415522361115f7c81f0f267e60b1f)。

ID `2`：DLL 输出（Output）144 MHz。

<a id="r_a5e923dd758f6f82f7b0f4ed28202dd8c"></a>

```c
#define BL70X_DLL_120MHz 3
```

相关声明：[BL70X_DLL_120MHz](#a5e923dd758f6f82f7b0f4ed28202dd8c)。

ID `3`：DLL 输出（Output）120 MHz，无效（Invalid）。

## 2.2\_详细说明（Detailed Documentation）

<a id="a6015c9507a7a9def674cf4c98eb2654c"></a>

### `BL70X_CLKID_CLK_BCLK`

```c
#define BL70X_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

总线时钟（Bus Clock）。

<a id="a3e76791c55a7712184f2e9e9674e88b3"></a>

### `BL70X_CLKID_CLK_CRYSTAL`

```c
#define BL70X_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

使用晶体（Crystal）作为时钟。

<a id="a1af3c1bff12a71ede0a4d408476c00d0"></a>

### `BL70X_CLKID_CLK_DLL`

```c
#define BL70X_CLKID_CLK_DLL BFLB_CLKID_CLK_PRIVATE
```

延迟锁定环（DLL）时钟，DLL 的标准根频率（Root Frequency）为 288 MHz。

<a id="ad5388ce8c7b4cab2aa1784d38ee4e324"></a>

### `BL70X_CLKID_CLK_F32K`

```c
#define BL70X_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

F32K 时钟（Clock）。

<a id="a3abbe6ab4ce1c5b05a7eecdb861b9e15"></a>

### `BL70X_CLKID_CLK_RC32K`

```c
#define BL70X_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

RC32K 时钟（Clock）。

<a id="a8192491fc6158e5065b2738d34881260"></a>

### `BL70X_CLKID_CLK_RC32M`

```c
#define BL70X_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="ac83b9076bd63c17c2f4d73dcaffbb82b"></a>

### `BL70X_CLKID_CLK_ROOT`

```c
#define BL70X_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

根时钟（Root Clock）。

<a id="a6e21eda5f4068542a0a6df1e7c425811"></a>

### `BL70X_CLKID_CLK_XTAL32K`

```c
#define BL70X_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

XTAL32K 时钟（Clock）。

<a id="a5e923dd758f6f82f7b0f4ed28202dd8c"></a>

### `BL70X_DLL_120MHz`

```c
#define BL70X_DLL_120MHz 3
```

ID `3`：DLL 输出（Output）120 MHz，无效（Invalid）。

<a id="a4d9415522361115f7c81f0f267e60b1f"></a>

### `BL70X_DLL_144MHz`

```c
#define BL70X_DLL_144MHz 2
```

ID `2`：DLL 输出（Output）144 MHz。

<a id="a8b9d59f8e8b8d4ecede95ca1cb6add32"></a>

### `BL70X_DLL_57MHz`

```c
#define BL70X_DLL_57MHz 0
```

ID `0`：DLL 输出（Output）57 MHz。

<a id="ae4deecec3a8a2258dc14048b77eb013f"></a>

### `BL70X_DLL_96MHz`

```c
#define BL70X_DLL_96MHz 1
```

ID `1`：DLL 输出（Output）96 MHz。


## 2.3\_原页交叉引用（Cross References）

- [bflb_clock_common.h](../api_source_reference/P065_bflb_clock_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P062_bflb_bl70x_clock.h_源码浏览.md)
- [BFLB_CLKID_CLK_ROOT](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#af2d6e2a7c386b50358a9cf50fc8808b3)
- [BFLB_CLKID_CLK_RC32M](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a48bf5d6a4379c03c7817503d7fe66c8b)
- [BFLB_CLKID_CLK_CRYSTAL](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a059c42552c94b942f53c644207776326)
- [BFLB_CLKID_CLK_BCLK](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a81f8f15faf5025212dbe96417515c358)
- [BFLB_CLKID_CLK_F32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a5b8eca0197f839af7776f5d02c6eab13)
- [BFLB_CLKID_CLK_XTAL32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#a14b75b51b81786bb7ae26070e5e41e22)
- [BFLB_CLKID_CLK_RC32K](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#ad2b0e7bd97598e50d10ce66d5b52a360)
- [BFLB_CLKID_CLK_PRIVATE](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html#acc4f8e38984a2ec63e470b919b6d8aef)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_zephyr__drivers__i3c__addresses.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__dt-bindings__clock__bflb_bl70xl_clock.h_文件参考.md)
