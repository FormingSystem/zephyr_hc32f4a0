---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-3
title: zephyr__dt-bindings__clock__bflb_bl616cl_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl616cl__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_dt-bindings\_\_clock\_\_bflb\_bl616cl\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl616cl__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

要安全运行，必须设置BCLK分频器（Divider），使BCLK不超过80 MHz。不过，已有观察表明硬件能够容忍最高130 MHz的BCLK。

<a id="details"></a>

```c
#include "bflb_clock_common.h"
```

查看此文件的源码。

为安全运行，**必须**设置 BCLK 分频器（Divider），使 BCLK 不超过 80 MHz；不过原文观察到最高 130 MHz 也曾能够运行。驱动可以从时钟源（通常为 BCLK）构造可用时钟，因此外设无需额外设置。这种超频会使大多数复杂外设（Wi-Fi），以及可作为外设总线主设备（Bus Master）的外设（DMA 和使用 DMA 的驱动）无法正常工作。必须调整闪存输入时钟（Flash Input Clock）以适配新的时钟设置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_a9c8a7e73c86301b833bcfa98452abad9"></a>

```c
#define BL616CL_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

相关声明：[BL616CL_CLKID_CLK_ROOT](#a9c8a7e73c86301b833bcfa98452abad9)、[BFLB_CLKID_CLK_ROOT](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#af2d6e2a7c386b50358a9cf50fc8808b3)。

根时钟（Root Clock）。

<a id="r_ae2564e11efc4b63304c47bf86e66a53b"></a>

```c
#define BL616CL_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

相关声明：[BL616CL_CLKID_CLK_RC32M](#ae2564e11efc4b63304c47bf86e66a53b)、[BFLB_CLKID_CLK_RC32M](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a48bf5d6a4379c03c7817503d7fe66c8b)。

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="r_a00881bea6bc10a7f7e63660cc015be9c"></a>

```c
#define BL616CL_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

相关声明：[BL616CL_CLKID_CLK_CRYSTAL](#a00881bea6bc10a7f7e63660cc015be9c)、[BFLB_CLKID_CLK_CRYSTAL](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a059c42552c94b942f53c644207776326)。

使用晶体（Crystal）作为时钟。

<a id="r_a5e0cda01c63a9b16fc5c67f814efe7f9"></a>

```c
#define BL616CL_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

相关声明：[BL616CL_CLKID_CLK_BCLK](#a5e0cda01c63a9b16fc5c67f814efe7f9)、[BFLB_CLKID_CLK_BCLK](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a81f8f15faf5025212dbe96417515c358)。

总线时钟（Bus Clock）。

<a id="r_a71c0ef9ace3cbfbfd904e31794310c9e"></a>

```c
#define BL616CL_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

相关声明：[BL616CL_CLKID_CLK_F32K](#a71c0ef9ace3cbfbfd904e31794310c9e)、[BFLB_CLKID_CLK_F32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a5b8eca0197f839af7776f5d02c6eab13)。

F32K 时钟（Clock）。

<a id="r_abc99131ee8c0e93a6f6e93a4a249e065"></a>

```c
#define BL616CL_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

相关声明：[BL616CL_CLKID_CLK_XTAL32K](#abc99131ee8c0e93a6f6e93a4a249e065)、[BFLB_CLKID_CLK_XTAL32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a14b75b51b81786bb7ae26070e5e41e22)。

XTAL32K 时钟（Clock）。

<a id="r_a32d37497cbe23e3f7fab7c638cd8c0eb"></a>

```c
#define BL616CL_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

相关声明：[BL616CL_CLKID_CLK_RC32K](#a32d37497cbe23e3f7fab7c638cd8c0eb)、[BFLB_CLKID_CLK_RC32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#ad2b0e7bd97598e50d10ce66d5b52a360)。

RC32K 时钟（Clock）。

<a id="r_a0c5a186faa137ae4ae77b28ab19da47d"></a>

```c
#define BL616CL_CLKID_CLK_PLL BFLB_CLKID_CLK_PRIVATE
```

相关声明：[BL616CL_CLKID_CLK_PLL](#a0c5a186faa137ae4ae77b28ab19da47d)、[BFLB_CLKID_CLK_PRIVATE](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)。

锁相环（PLL）时钟，此 PLL 的标准根频率（Root Frequency）为 960 MHz。

<a id="r_abec0a670f900fc4fb6b4a8513aa03aee"></a>

```c
#define BL616CL_CLKID_CLK_160M (BFLB_CLKID_CLK_PRIVATE + 1)
```

相关声明：[BL616CL_CLKID_CLK_160M](#abec0a670f900fc4fb6b4a8513aa03aee)、[BFLB_CLKID_CLK_PRIVATE](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)。

此时钟通过 PLL 的多路选择（Mux）提供 160 MHz。

<a id="r_a837cf0c536eaadac3bfcdff026182ab7"></a>

```c
#define BL616CL_PLL_ID_DIV3_10 0
```

相关声明：[BL616CL_PLL_ID_DIV3_10](#a837cf0c536eaadac3bfcdff026182ab7)。

ID `0`：`PLL root / 10` 或 `3 * top / 10`。

<a id="r_abf852eca08e173848652518ea7789989"></a>

```c
#define BL616CL_PLL_ID_DIV3_5 1
```

相关声明：[BL616CL_PLL_ID_DIV3_5](#abf852eca08e173848652518ea7789989)。

ID `1`：`PLL root / 5` 或 `3 * top / 5`。

<a id="r_a00a7c6e8096e86e69a97df8bbe610afd"></a>

```c
#define BL616CL_PLL_ID_DIV3_4 2
```

相关声明：[BL616CL_PLL_ID_DIV3_4](#a00a7c6e8096e86e69a97df8bbe610afd)。

ID `2`：`PLL root / 4` 或 `3 * top / 4`。

<a id="r_af9585bec47b44e36fe71e435d60b947f"></a>

```c
#define BL616CL_PLL_ID_DIV1 3
```

相关声明：[BL616CL_PLL_ID_DIV1](#af9585bec47b44e36fe71e435d60b947f)。

ID `3`：`PLL root / 3` 或 `top / 1`。

<a id="r_a6e6e538dcd8a7c896b2ac013420463a1"></a>

```c
#define BL616CL_PLL_TOP_FREQ (DT_FREQ_M(320))
```

相关声明：[BL616CL_PLL_TOP_FREQ](#a6e6e538dcd8a7c896b2ac013420463a1)。

PLL 在根时钟处的参考最高频率（Reference Top Frequency），此处为 `PLL root / 3`。

## 3.2\_详细说明（Detailed Documentation）

<a id="abec0a670f900fc4fb6b4a8513aa03aee"></a>

### `BL616CL_CLKID_CLK_160M`

```c
#define BL616CL_CLKID_CLK_160M (BFLB_CLKID_CLK_PRIVATE + 1)
```

此时钟通过 PLL 的多路选择（Mux）提供 160 MHz。

<a id="a5e0cda01c63a9b16fc5c67f814efe7f9"></a>

### `BL616CL_CLKID_CLK_BCLK`

```c
#define BL616CL_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

总线时钟（Bus Clock）。

<a id="a00881bea6bc10a7f7e63660cc015be9c"></a>

### `BL616CL_CLKID_CLK_CRYSTAL`

```c
#define BL616CL_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

使用晶体（Crystal）作为时钟。

<a id="a71c0ef9ace3cbfbfd904e31794310c9e"></a>

### `BL616CL_CLKID_CLK_F32K`

```c
#define BL616CL_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

F32K 时钟（Clock）。

<a id="a0c5a186faa137ae4ae77b28ab19da47d"></a>

### `BL616CL_CLKID_CLK_PLL`

```c
#define BL616CL_CLKID_CLK_PLL BFLB_CLKID_CLK_PRIVATE
```

锁相环（PLL）时钟，此 PLL 的标准根频率（Root Frequency）为 960 MHz。

<a id="a32d37497cbe23e3f7fab7c638cd8c0eb"></a>

### `BL616CL_CLKID_CLK_RC32K`

```c
#define BL616CL_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

RC32K 时钟（Clock）。

<a id="ae2564e11efc4b63304c47bf86e66a53b"></a>

### `BL616CL_CLKID_CLK_RC32M`

```c
#define BL616CL_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="a9c8a7e73c86301b833bcfa98452abad9"></a>

### `BL616CL_CLKID_CLK_ROOT`

```c
#define BL616CL_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

根时钟（Root Clock）。

<a id="abc99131ee8c0e93a6f6e93a4a249e065"></a>

### `BL616CL_CLKID_CLK_XTAL32K`

```c
#define BL616CL_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

XTAL32K 时钟（Clock）。

<a id="af9585bec47b44e36fe71e435d60b947f"></a>

### `BL616CL_PLL_ID_DIV1`

```c
#define BL616CL_PLL_ID_DIV1 3
```

ID `3`：`PLL root / 3` 或 `top / 1`。

<a id="a837cf0c536eaadac3bfcdff026182ab7"></a>

### `BL616CL_PLL_ID_DIV3_10`

```c
#define BL616CL_PLL_ID_DIV3_10 0
```

ID `0`：`PLL root / 10` 或 `3 * top / 10`。

<a id="a00a7c6e8096e86e69a97df8bbe610afd"></a>

### `BL616CL_PLL_ID_DIV3_4`

```c
#define BL616CL_PLL_ID_DIV3_4 2
```

ID `2`：`PLL root / 4` 或 `3 * top / 4`。

<a id="abf852eca08e173848652518ea7789989"></a>

### `BL616CL_PLL_ID_DIV3_5`

```c
#define BL616CL_PLL_ID_DIV3_5 1
```

ID `1`：`PLL root / 5` 或 `3 * top / 5`。

<a id="a6e6e538dcd8a7c896b2ac013420463a1"></a>

### `BL616CL_PLL_TOP_FREQ`

```c
#define BL616CL_PLL_TOP_FREQ (DT_FREQ_M(320))
```

PLL 在根时钟处的参考最高频率（Reference Top Frequency），此处为 `PLL root / 3`。


## 3.3\_原页交叉引用（Cross References）

- [bflb_clock_common.h](../api_source_reference/P065_bflb_clock_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P060_bflb_bl616cl_clock.h_源码浏览.md)
- [BFLB_CLKID_CLK_ROOT](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#af2d6e2a7c386b50358a9cf50fc8808b3)
- [BFLB_CLKID_CLK_RC32M](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a48bf5d6a4379c03c7817503d7fe66c8b)
- [BFLB_CLKID_CLK_CRYSTAL](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a059c42552c94b942f53c644207776326)
- [BFLB_CLKID_CLK_BCLK](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a81f8f15faf5025212dbe96417515c358)
- [BFLB_CLKID_CLK_F32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a5b8eca0197f839af7776f5d02c6eab13)
- [BFLB_CLKID_CLK_XTAL32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a14b75b51b81786bb7ae26070e5e41e22)
- [BFLB_CLKID_CLK_RC32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#ad2b0e7bd97598e50d10ce66d5b52a360)
- [BFLB_CLKID_CLK_PRIVATE](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P002_zephyr__dt-bindings__clock__bflb_bl60x_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__dt-bindings__clock__bflb_bl61x_clock.h_文件参考.md)
