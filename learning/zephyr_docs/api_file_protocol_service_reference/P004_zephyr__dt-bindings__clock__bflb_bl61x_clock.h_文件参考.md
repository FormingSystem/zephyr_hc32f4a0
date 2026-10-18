---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-4
title: zephyr__dt-bindings__clock__bflb_bl61x_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl61x__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_dt-bindings\_\_clock\_\_bflb\_bl61x\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl61x__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

要安全运行，必须设置BCLK分频器（Divider），使BCLK不超过80 MHz。不过，已有观察表明硬件能够容忍最高130 MHz的BCLK。

<a id="details"></a>

```c
#include "bflb_clock_common.h"
```

查看此文件的源码。

为安全运行，**必须**设置 BCLK 分频器（Divider），使 BCLK 不超过 80 MHz；不过原文观察到最高 130 MHz 也曾能够运行。驱动可以从时钟源（通常为 BCLK）构造可用时钟，因此外设无需额外设置。这种超频会使大多数复杂外设（Wi-Fi），以及可作为外设总线主设备（Bus Master）的外设（DMA 和使用 DMA 的驱动）无法正常工作。必须调整闪存输入时钟（Flash Input Clock）以适配新的时钟设置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="r_a1a241ee58604bb423bf4373cf17308ba"></a>

```c
#define BL61X_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

相关声明：[BL61X_CLKID_CLK_ROOT](#a1a241ee58604bb423bf4373cf17308ba)、[BFLB_CLKID_CLK_ROOT](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#af2d6e2a7c386b50358a9cf50fc8808b3)。

根时钟（Root Clock）。

<a id="r_aa6cfeee5f7e71c8f2148899c58a35795"></a>

```c
#define BL61X_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

相关声明：[BL61X_CLKID_CLK_RC32M](#aa6cfeee5f7e71c8f2148899c58a35795)、[BFLB_CLKID_CLK_RC32M](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a48bf5d6a4379c03c7817503d7fe66c8b)。

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="r_ae9726a3046c809d03478a3c791e90a87"></a>

```c
#define BL61X_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

相关声明：[BL61X_CLKID_CLK_CRYSTAL](#ae9726a3046c809d03478a3c791e90a87)、[BFLB_CLKID_CLK_CRYSTAL](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a059c42552c94b942f53c644207776326)。

使用晶体（Crystal）作为时钟。

<a id="r_ab63e17708db5c39feb6ff5f37d57a657"></a>

```c
#define BL61X_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

相关声明：[BL61X_CLKID_CLK_BCLK](#ab63e17708db5c39feb6ff5f37d57a657)、[BFLB_CLKID_CLK_BCLK](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a81f8f15faf5025212dbe96417515c358)。

总线时钟（Bus Clock）。

<a id="r_a35ae1c43b13d2863e4836b42c27a04c0"></a>

```c
#define BL61X_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

相关声明：[BL61X_CLKID_CLK_F32K](#a35ae1c43b13d2863e4836b42c27a04c0)、[BFLB_CLKID_CLK_F32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a5b8eca0197f839af7776f5d02c6eab13)。

F32K 时钟（Clock）。

<a id="r_a65fb3f058de05e70d71e2c6f23c1c075"></a>

```c
#define BL61X_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

相关声明：[BL61X_CLKID_CLK_XTAL32K](#a65fb3f058de05e70d71e2c6f23c1c075)、[BFLB_CLKID_CLK_XTAL32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a14b75b51b81786bb7ae26070e5e41e22)。

XTAL32K 时钟（Clock）。

<a id="r_a7d433973516d9248a874dd101a615f61"></a>

```c
#define BL61X_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

相关声明：[BL61X_CLKID_CLK_RC32K](#a7d433973516d9248a874dd101a615f61)、[BFLB_CLKID_CLK_RC32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#ad2b0e7bd97598e50d10ce66d5b52a360)。

RC32K 时钟（Clock）。

<a id="r_afb2b0b6f03d11bac602bccf5d546e917"></a>

```c
#define BL61X_CLKID_CLK_WIFIPLL BFLB_CLKID_CLK_PRIVATE
```

相关声明：[BL61X_CLKID_CLK_WIFIPLL](#afb2b0b6f03d11bac602bccf5d546e917)、[BFLB_CLKID_CLK_PRIVATE](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)。

WIFIPLL 时钟，标准根频率（Root Frequency）为 960 MHz。

<a id="r_a2d4d992230e14c54b3a01b21e7c4ee4f"></a>

```c
#define BL61X_CLKID_CLK_AUPLL (BFLB_CLKID_CLK_PRIVATE + 1)
```

相关声明：[BL61X_CLKID_CLK_AUPLL](#a2d4d992230e14c54b3a01b21e7c4ee4f)、[BFLB_CLKID_CLK_PRIVATE](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)。

AUPLL 时钟，没有标准根频率（Standard Root Frequency）。

<a id="r_a9e1e6a13724915cabdc2986455652569"></a>

```c
#define BL61X_CLKID_CLK_160M (BFLB_CLKID_CLK_PRIVATE + 2)
```

相关声明：[BL61X_CLKID_CLK_160M](#a9e1e6a13724915cabdc2986455652569)、[BFLB_CLKID_CLK_PRIVATE](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)。

此时钟通过 PLL 的多路选择（Mux）提供 160 MHz。

<a id="r_a5914acdbfebc563770e2b7f7e285f809"></a>

```c
#define BL61X_AUPLL_ID_DIV2 0
```

相关声明：[BL61X_AUPLL_ID_DIV2](#a5914acdbfebc563770e2b7f7e285f809)。

ID `0`：`AUPLL / 2`。

<a id="r_afa96b4978e97da0986b780e3473c38c0"></a>

```c
#define BL61X_AUPLL_ID_DIV1 1
```

相关声明：[BL61X_AUPLL_ID_DIV1](#afa96b4978e97da0986b780e3473c38c0)。

ID `1`：`AUPLL / 1`。

<a id="r_a0d245ba0b5652c7acaef0856d1a81305"></a>

```c
#define BL61X_WIFIPLL_ID_DIV3_4 2
```

相关声明：[BL61X_WIFIPLL_ID_DIV3_4](#a0d245ba0b5652c7acaef0856d1a81305)。

ID `2`：`WIFIPLL root / 4` 或 `3 * top / 4`。

<a id="r_a20552444f0ef5a51213cf64434b25904"></a>

```c
#define BL61X_WIFIPLL_ID_DIV1 3
```

相关声明：[BL61X_WIFIPLL_ID_DIV1](#a20552444f0ef5a51213cf64434b25904)。

ID `3`：`WIFIPLL root / 3` 或 `top / 1`。

<a id="r_a929cd66787946309cf29679bb9c8fc37"></a>

```c
#define BL61X_WIFIPLL_TOP_FREQ (DT_FREQ_M(320))
```

相关声明：[BL61X_WIFIPLL_TOP_FREQ](#a929cd66787946309cf29679bb9c8fc37)。

WIFIPLL 在根时钟处的参考最高频率（Reference Top Frequency），此处为 `WIFIPLL root / 3`。

<a id="r_ada3f959f4141c94e944dc835ab54f42d"></a>

```c
#define BL61X_AUPLL_TOP_FREQ (DT_FREQ_M(320))
```

相关声明：[BL61X_AUPLL_TOP_FREQ](#ada3f959f4141c94e944dc835ab54f42d)。

AUPLL 的参考最高频率（Reference Top Frequency），即压控振荡器（VCO）直接输出，不经过后分频器（Post-divider）。

<a id="r_a43d0343dedc8013793909d554d42cae7"></a>

```c
#define BL61X_TOP_FREQ_OC1 (DT_FREQ_M(480))
```

相关声明：[BL61X_TOP_FREQ_OC1](#a43d0343dedc8013793909d554d42cae7)。

PLL 超频示例（Overclocked PLL Example）1，可使用标准电压。

<a id="r_afa317f83fa4b60405fe291be10f89b34"></a>

```c
#define BL61X_TOP_FREQ_OC2 (DT_FREQ_M(640))
```

相关声明：[BL61X_TOP_FREQ_OC2](#afa317f83fa4b60405fe291be10f89b34)。

PLL 超频示例（Overclocked PLL Example）2，必须提高电压至 1.25 V。

## 4.2\_详细说明（Detailed Documentation）

<a id="afa96b4978e97da0986b780e3473c38c0"></a>

### `BL61X_AUPLL_ID_DIV1`

```c
#define BL61X_AUPLL_ID_DIV1 1
```

ID `1`：`AUPLL / 1`。

<a id="a5914acdbfebc563770e2b7f7e285f809"></a>

### `BL61X_AUPLL_ID_DIV2`

```c
#define BL61X_AUPLL_ID_DIV2 0
```

ID `0`：`AUPLL / 2`。

<a id="ada3f959f4141c94e944dc835ab54f42d"></a>

### `BL61X_AUPLL_TOP_FREQ`

```c
#define BL61X_AUPLL_TOP_FREQ (DT_FREQ_M(320))
```

AUPLL 的参考最高频率（Reference Top Frequency），即压控振荡器（VCO）直接输出，不经过后分频器（Post-divider）。

<a id="a9e1e6a13724915cabdc2986455652569"></a>

### `BL61X_CLKID_CLK_160M`

```c
#define BL61X_CLKID_CLK_160M (BFLB_CLKID_CLK_PRIVATE + 2)
```

此时钟通过 PLL 的多路选择（Mux）提供 160 MHz。

<a id="a2d4d992230e14c54b3a01b21e7c4ee4f"></a>

### `BL61X_CLKID_CLK_AUPLL`

```c
#define BL61X_CLKID_CLK_AUPLL (BFLB_CLKID_CLK_PRIVATE + 1)
```

AUPLL 时钟，没有标准根频率（Standard Root Frequency）。

<a id="ab63e17708db5c39feb6ff5f37d57a657"></a>

### `BL61X_CLKID_CLK_BCLK`

```c
#define BL61X_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

总线时钟（Bus Clock）。

<a id="ae9726a3046c809d03478a3c791e90a87"></a>

### `BL61X_CLKID_CLK_CRYSTAL`

```c
#define BL61X_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

使用晶体（Crystal）作为时钟。

<a id="a35ae1c43b13d2863e4836b42c27a04c0"></a>

### `BL61X_CLKID_CLK_F32K`

```c
#define BL61X_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

F32K 时钟（Clock）。

<a id="a7d433973516d9248a874dd101a615f61"></a>

### `BL61X_CLKID_CLK_RC32K`

```c
#define BL61X_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

RC32K 时钟（Clock）。

<a id="aa6cfeee5f7e71c8f2148899c58a35795"></a>

### `BL61X_CLKID_CLK_RC32M`

```c
#define BL61X_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="a1a241ee58604bb423bf4373cf17308ba"></a>

### `BL61X_CLKID_CLK_ROOT`

```c
#define BL61X_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

根时钟（Root Clock）。

<a id="afb2b0b6f03d11bac602bccf5d546e917"></a>

### `BL61X_CLKID_CLK_WIFIPLL`

```c
#define BL61X_CLKID_CLK_WIFIPLL BFLB_CLKID_CLK_PRIVATE
```

WIFIPLL 时钟，标准根频率（Root Frequency）为 960 MHz。

<a id="a65fb3f058de05e70d71e2c6f23c1c075"></a>

### `BL61X_CLKID_CLK_XTAL32K`

```c
#define BL61X_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

XTAL32K 时钟（Clock）。

<a id="a43d0343dedc8013793909d554d42cae7"></a>

### `BL61X_TOP_FREQ_OC1`

```c
#define BL61X_TOP_FREQ_OC1 (DT_FREQ_M(480))
```

PLL 超频示例（Overclocked PLL Example）1，可使用标准电压。

<a id="afa317f83fa4b60405fe291be10f89b34"></a>

### `BL61X_TOP_FREQ_OC2`

```c
#define BL61X_TOP_FREQ_OC2 (DT_FREQ_M(640))
```

PLL 超频示例（Overclocked PLL Example）2，必须提高电压至 1.25 V。

<a id="a20552444f0ef5a51213cf64434b25904"></a>

### `BL61X_WIFIPLL_ID_DIV1`

```c
#define BL61X_WIFIPLL_ID_DIV1 3
```

ID `3`：`WIFIPLL root / 3` 或 `top / 1`。

<a id="a0d245ba0b5652c7acaef0856d1a81305"></a>

### `BL61X_WIFIPLL_ID_DIV3_4`

```c
#define BL61X_WIFIPLL_ID_DIV3_4 2
```

ID `2`：`WIFIPLL root / 4` 或 `3 * top / 4`。

<a id="a929cd66787946309cf29679bb9c8fc37"></a>

### `BL61X_WIFIPLL_TOP_FREQ`

```c
#define BL61X_WIFIPLL_TOP_FREQ (DT_FREQ_M(320))
```

WIFIPLL 在根时钟处的参考最高频率（Reference Top Frequency），此处为 `WIFIPLL root / 3`。


## 4.3\_原页交叉引用（Cross References）

- [bflb_clock_common.h](../api_source_reference/P065_bflb_clock_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P061_bflb_bl61x_clock.h_源码浏览.md)
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

[上一章](P003_zephyr__dt-bindings__clock__bflb_bl616cl_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md)
