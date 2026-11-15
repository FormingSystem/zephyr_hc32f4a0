---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-2
title: zephyr__dt-bindings__clock__bflb_bl60x_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl60x__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_dt-bindings\_\_clock\_\_bflb\_bl60x\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl60x__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BL60x的性能情况较为复杂：BCLK分频器（Divider）是影响BL60x性能最重要的调节因素，这似乎与向CPU供给数据的硬件设计问题有关。在其他所有BFLB片上系统（SoC）中，BCLK对纯CPU性能大体上并不重要，其中也包括采用相同缓存和CPU方案的BL70x、BL70xL。

<a id="details"></a>

```c
#include "bflb_clock_common.h"
```

查看此文件的源码。

BL60x 的性能调节较复杂：BCLK 分频器（Divider）对性能的影响最大，这似乎与向 CPU 供给数据的硬件设计问题有关；在其他 BFLB SoC 上，包括采用相同缓存和 CPU 方案的 BL70x、BL70xL，BCLK 通常对纯 CPU 性能影响不大。因此应调节分频器，同时牢记 BFLB 建议 BCLK 不超过 96 MHz。原文列出的有效配置如下。

| 配置 | 根时钟（Root） | BCLK | 闪存时钟（Flash CLK） | SoC 电压 | 性能／循环展开后（Unrolled） |
| --- | --- | --- | --- | --- | --- |
| 基准（Base） | 192 MHz，标准 | 96 MHz，Root / 2，标准 | 48 MHz，BCLK / 2；可能因模块或 PCB 而异，原文认为此值稳妥 | 原文未另指定 | 1（351 Cmrks）／1.125（395 Cmrks） |
| 提高电压、循环展开时最佳；非标准用法 | 200 MHz，标准 | 200 MHz，超频（Overclocked） | 66 MHz，BCLK / 3 | 1.25 V，已提高 | 1.52（534 Cmrks）／1.9（666 Cmrks） |
| 不提高电压、循环展开时最佳；非标准用法，最大 BCLK | 150 MHz，来自超频设置但在标准范围内 | 150 MHz，超频 | 75 MHz，BCLK / 2 | 未提高 | 1.14（400 Cmrks）／1.42（500 Cmrks） |
| 提高电压、不展开循环时最佳 | 320 MHz，超频 | 160 MHz，Root / 2，超频 | 80 MHz，BCLK / 2 | 1.25 V，已提高 | 1.67（585 Cmrks）／1.88（660 Cmrks） |
| 不展开循环时最佳 | 240 MHz，超频 | 120 MHz，Root / 2，超频 | 60 MHz，BCLK / 2 | 原文未另指定 | 1.25（440 Cmrks）／1.41（494 Cmrks） |

该 SoC 主 CPU 可以运行在更高频率，但实际意义不大，因为性能受 BCLK 速度限制，而 200 MHz BCLK 已接近可达到的上限。原文记录的最高稳定频率为 1.35 V 下的 360 MHz。采用 `360/180` 相比 `200/200` 配置只提高约 10%–22%，性能为 1.8（660 Cmrks），循环展开后为 2.1（740 Cmrks），而且需要给 SoC 施加可用的最高电压。

此外，受锁相环（PLL）要求限制，低于常用 40 MHz 晶体的参考时钟可能使 PLL 无法锁定。超频时，大多数复杂外设（Wi-Fi）及可作为外设总线主设备（Bus Master）的外设（DMA 和使用 DMA 的驱动）无法正常工作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_aeacd7c41a31cecf69b9a9a78d67736a2"></a>

```c
#define BL60X_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

相关声明：[BL60X_CLKID_CLK_ROOT](#aeacd7c41a31cecf69b9a9a78d67736a2)、[BFLB_CLKID_CLK_ROOT](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#af2d6e2a7c386b50358a9cf50fc8808b3)。

根时钟（Root Clock）。

<a id="r_accf2556fddba4992a60cf336291751cd"></a>

```c
#define BL60X_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

相关声明：[BL60X_CLKID_CLK_RC32M](#accf2556fddba4992a60cf336291751cd)、[BFLB_CLKID_CLK_RC32M](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a48bf5d6a4379c03c7817503d7fe66c8b)。

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="r_a8fe00248514b4c133f8551163c433eee"></a>

```c
#define BL60X_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

相关声明：[BL60X_CLKID_CLK_CRYSTAL](#a8fe00248514b4c133f8551163c433eee)、[BFLB_CLKID_CLK_CRYSTAL](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a059c42552c94b942f53c644207776326)。

使用晶体（Crystal）作为时钟。

<a id="r_aa0eef44026316125a2583b82469c218c"></a>

```c
#define BL60X_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

相关声明：[BL60X_CLKID_CLK_BCLK](#aa0eef44026316125a2583b82469c218c)、[BFLB_CLKID_CLK_BCLK](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a81f8f15faf5025212dbe96417515c358)。

总线时钟（Bus Clock）。

<a id="r_a0c65b2482cae45c4c2e699b1a022aa01"></a>

```c
#define BL60X_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

相关声明：[BL60X_CLKID_CLK_F32K](#a0c65b2482cae45c4c2e699b1a022aa01)、[BFLB_CLKID_CLK_F32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a5b8eca0197f839af7776f5d02c6eab13)。

F32K 时钟（Clock）。

<a id="r_af1ecef26fa6e9beab16f26d2c284d95e"></a>

```c
#define BL60X_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

相关声明：[BL60X_CLKID_CLK_XTAL32K](#af1ecef26fa6e9beab16f26d2c284d95e)、[BFLB_CLKID_CLK_XTAL32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a14b75b51b81786bb7ae26070e5e41e22)。

XTAL32K 时钟（Clock）。

<a id="r_a7d3c203fe2c768fc74c314293c5fcc87"></a>

```c
#define BL60X_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

相关声明：[BL60X_CLKID_CLK_RC32K](#a7d3c203fe2c768fc74c314293c5fcc87)、[BFLB_CLKID_CLK_RC32K](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#ad2b0e7bd97598e50d10ce66d5b52a360)。

RC32K 时钟（Clock）。

<a id="r_a529098e27dfab5df2ef931c90e14b6fe"></a>

```c
#define BL60X_CLKID_CLK_PLL BFLB_CLKID_CLK_PRIVATE
```

相关声明：[BL60X_CLKID_CLK_PLL](#a529098e27dfab5df2ef931c90e14b6fe)、[BFLB_CLKID_CLK_PRIVATE](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)。

锁相环（PLL）时钟，标准根频率（Root Frequency）为 480 MHz。

<a id="r_a1e921217d3e752e98d9cd387515da152"></a>

```c
#define BL60X_PLL_TOP_FREQ (DT_FREQ_M(192))
```

相关声明：[BL60X_PLL_TOP_FREQ](#a1e921217d3e752e98d9cd387515da152)。

PLL 在根时钟处的参考最高频率（Reference Top Frequency），此处为 `PLL root / 2.5`。

<a id="r_ada2ff20beee8e010a9526fb0e67224ef"></a>

```c
#define BL60X_PLL_ID_DIV4 0
```

相关声明：[BL60X_PLL_ID_DIV4](#ada2ff20beee8e010a9526fb0e67224ef)。

ID `0`：`PLL root / 10` 或 `top / 4`。

<a id="r_ad1f1937f0c9577726d41338d3e73feae"></a>

```c
#define BL60X_PLL_ID_DIV5_8 1
```

相关声明：[BL60X_PLL_ID_DIV5_8](#ad1f1937f0c9577726d41338d3e73feae)。

ID `1`：`PLL root / 4` 或 `5 * top / 8`。

<a id="r_a34cb0c086cac84c087186cd7ec8874fd"></a>

```c
#define BL60X_PLL_ID_DIV5_3 2
```

相关声明：[BL60X_PLL_ID_DIV5_3](#a34cb0c086cac84c087186cd7ec8874fd)。

ID `2`：`PLL root / 3` 或 `5 * top / 3`。

<a id="r_ab79e32d2febc2f6d96a98b1cb9d8ae0a"></a>

```c
#define BL60X_PLL_ID_DIV1 3
```

相关声明：[BL60X_PLL_ID_DIV1](#ab79e32d2febc2f6d96a98b1cb9d8ae0a)。

ID `3`：`PLL root / 2.5` 或 `top / 1`。

<a id="r_afd86d10d8a6b7b5f7f30aeb332eab2f2"></a>

```c
#define BL60X_PLL_TOP_FREQ_OC1 (DT_FREQ_M(240))
```

相关声明：[BL60X_PLL_TOP_FREQ_OC1](#afd86d10d8a6b7b5f7f30aeb332eab2f2)。

PLL 超频示例（Overclocked PLL Example）1，可使用标准电压。

<a id="r_a49475f4703dbe82d8e4867e8f0b13c04"></a>

```c
#define BL60X_PLL_TOP_FREQ_OC2 (DT_FREQ_M(320))
```

相关声明：[BL60X_PLL_TOP_FREQ_OC2](#a49475f4703dbe82d8e4867e8f0b13c04)。

PLL 超频示例（Overclocked PLL Example）2，必须提高电压至 1.25 V。

## 2.2\_详细说明（Detailed Documentation）

<a id="aa0eef44026316125a2583b82469c218c"></a>

### `BL60X_CLKID_CLK_BCLK`

```c
#define BL60X_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

总线时钟（Bus Clock）。

<a id="a8fe00248514b4c133f8551163c433eee"></a>

### `BL60X_CLKID_CLK_CRYSTAL`

```c
#define BL60X_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

使用晶体（Crystal）作为时钟。

<a id="a0c65b2482cae45c4c2e699b1a022aa01"></a>

### `BL60X_CLKID_CLK_F32K`

```c
#define BL60X_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

F32K 时钟（Clock）。

<a id="a529098e27dfab5df2ef931c90e14b6fe"></a>

### `BL60X_CLKID_CLK_PLL`

```c
#define BL60X_CLKID_CLK_PLL BFLB_CLKID_CLK_PRIVATE
```

锁相环（PLL）时钟，标准根频率（Root Frequency）为 480 MHz。

<a id="a7d3c203fe2c768fc74c314293c5fcc87"></a>

### `BL60X_CLKID_CLK_RC32K`

```c
#define BL60X_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

RC32K 时钟（Clock）。

<a id="accf2556fddba4992a60cf336291751cd"></a>

### `BL60X_CLKID_CLK_RC32M`

```c
#define BL60X_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="aeacd7c41a31cecf69b9a9a78d67736a2"></a>

### `BL60X_CLKID_CLK_ROOT`

```c
#define BL60X_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

根时钟（Root Clock）。

<a id="af1ecef26fa6e9beab16f26d2c284d95e"></a>

### `BL60X_CLKID_CLK_XTAL32K`

```c
#define BL60X_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

XTAL32K 时钟（Clock）。

<a id="ab79e32d2febc2f6d96a98b1cb9d8ae0a"></a>

### `BL60X_PLL_ID_DIV1`

```c
#define BL60X_PLL_ID_DIV1 3
```

ID `3`：`PLL root / 2.5` 或 `top / 1`。

<a id="ada2ff20beee8e010a9526fb0e67224ef"></a>

### `BL60X_PLL_ID_DIV4`

```c
#define BL60X_PLL_ID_DIV4 0
```

ID `0`：`PLL root / 10` 或 `top / 4`。

<a id="a34cb0c086cac84c087186cd7ec8874fd"></a>

### `BL60X_PLL_ID_DIV5_3`

```c
#define BL60X_PLL_ID_DIV5_3 2
```

ID `2`：`PLL root / 3` 或 `5 * top / 3`。

<a id="ad1f1937f0c9577726d41338d3e73feae"></a>

### `BL60X_PLL_ID_DIV5_8`

```c
#define BL60X_PLL_ID_DIV5_8 1
```

ID `1`：`PLL root / 4` 或 `5 * top / 8`。

<a id="a1e921217d3e752e98d9cd387515da152"></a>

### `BL60X_PLL_TOP_FREQ`

```c
#define BL60X_PLL_TOP_FREQ (DT_FREQ_M(192))
```

PLL 在根时钟处的参考最高频率（Reference Top Frequency），此处为 `PLL root / 2.5`。

<a id="afd86d10d8a6b7b5f7f30aeb332eab2f2"></a>

### `BL60X_PLL_TOP_FREQ_OC1`

```c
#define BL60X_PLL_TOP_FREQ_OC1 (DT_FREQ_M(240))
```

PLL 超频示例（Overclocked PLL Example）1，可使用标准电压。

<a id="a49475f4703dbe82d8e4867e8f0b13c04"></a>

### `BL60X_PLL_TOP_FREQ_OC2`

```c
#define BL60X_PLL_TOP_FREQ_OC2 (DT_FREQ_M(320))
```

PLL 超频示例（Overclocked PLL Example）2，必须提高电压至 1.25 V。


## 2.3\_原页交叉引用（Cross References）

- [bflb_clock_common.h](../api_source_reference/P065_bflb_clock_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P059_bflb_bl60x_clock.h_源码浏览.md)
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

[上一章](P001_zephyr__dt-bindings__sensor__apds9253.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__dt-bindings__clock__bflb_bl616cl_clock.h_文件参考.md)
