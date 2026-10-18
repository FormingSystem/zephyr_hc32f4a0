---
id: learning.zephyr-docs.api-file-system-power-reference.page-28
title: zephyr__dt-bindings__clock__mchp_xec_pcr.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__pcr_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_dt-bindings\_\_clock\_\_mchp\_xec\_pcr.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__pcr_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip MEC片上系统（SoC）系列的时钟ID。

查看此文件的源码。

<a id="details"></a>

Microchip MEC片上系统（SoC）系列的时钟ID。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 28.1\_宏定义（Macros）

<a id="r_a648809d3dcf2e2aa84641d1dcaaa333f"></a>

```c
#define MCHP_XEC_PLL_CLK32K_SRC_SIL_OSC 0U
```

相关声明：[MCHP_XEC_PLL_CLK32K_SRC_SIL_OSC](#a648809d3dcf2e2aa84641d1dcaaa333f)。

全开启状态（Full On）下使用的 PLL 32 kHz 时钟源（Clock Source）。

<a id="r_a701353ae9e33d97be76c9ee0273c87fa"></a>

```c
#define MCHP_XEC_PLL_CLK32K_SRC_XTAL 1U
```

相关声明：[MCHP_XEC_PLL_CLK32K_SRC_XTAL](#a701353ae9e33d97be76c9ee0273c87fa)。

<a id="r_aa4c445cdf962557f71765cad287cb215"></a>

```c
#define MCHP_XEC_PLL_CLK32K_SRC_PIN 2U
```

相关声明：[MCHP_XEC_PLL_CLK32K_SRC_PIN](#aa4c445cdf962557f71765cad287cb215)。

<a id="r_ac71939dc0ab9d064ea43fd8fd898257c"></a>

```c
#define MCHP_XEC_PERIPH_CLK32K_SRC_SO_SO 0U
```

相关声明：[MCHP_XEC_PERIPH_CLK32K_SRC_SO_SO](#ac71939dc0ab9d064ea43fd8fd898257c)。

全开启（Full On）及 VBAT 运行状态下使用的外设 32 kHz 时钟源（Clock Source）。

<a id="r_a6bc8a1b96df3f9077e6b00da8ea8af22"></a>

```c
#define MCHP_XEC_PERIPH_CLK32K_SRC_XTAL_XTAL 1U
```

相关声明：[MCHP_XEC_PERIPH_CLK32K_SRC_XTAL_XTAL](#a6bc8a1b96df3f9077e6b00da8ea8af22)。

<a id="r_a569039424af967d8445fa62e28f20229"></a>

```c
#define MCHP_XEC_PERIPH_CLK32K_SRC_PIN_SO 2U
```

相关声明：[MCHP_XEC_PERIPH_CLK32K_SRC_PIN_SO](#a569039424af967d8445fa62e28f20229)。

<a id="r_abdee7a88e189e89bc4c721e2e5222d80"></a>

```c
#define MCHP_XEC_PERIPH_CLK32K_SRC_PIN_XTAL 3U
```

相关声明：[MCHP_XEC_PERIPH_CLK32K_SRC_PIN_XTAL](#abdee7a88e189e89bc4c721e2e5222d80)。

<a id="r_abc3c97c553f70c6925bb07c546ad1694"></a>

```c
#define MCHP_XEC_PCR_CLK_CORE 0
```

相关声明：[MCHP_XEC_PCR_CLK_CORE](#abc3c97c553f70c6925bb07c546ad1694)。

供时钟控制驱动（Clock Control Driver）使用的时钟 ID。

<a id="r_a713a1fd7de2fe9c20e69da59e16c5f28"></a>

```c
#define MCHP_XEC_PCR_CLK_CPU 1
```

相关声明：[MCHP_XEC_PCR_CLK_CPU](#a713a1fd7de2fe9c20e69da59e16c5f28)。

CPU 时钟。

<a id="r_a645c476e2d0506aed4842d077a538a16"></a>

```c
#define MCHP_XEC_PCR_CLK_BUS 2
```

相关声明：[MCHP_XEC_PCR_CLK_BUS](#a645c476e2d0506aed4842d077a538a16)。

高级高性能总线（AHB）时钟。

<a id="r_ac772778bad2aaa564299f884150173f7"></a>

```c
#define MCHP_XEC_PCR_CLK_PERIPH 3
```

相关声明：[MCHP_XEC_PCR_CLK_PERIPH](#ac772778bad2aaa564299f884150173f7)。

普通外设时钟（Clock for Normal Peripherals）。

<a id="r_ad313fc38e1fb56d5a9251a771e8a1119"></a>

```c
#define MCHP_XEC_PCR_CLK_PERIPH_FAST 4
```

相关声明：[MCHP_XEC_PCR_CLK_PERIPH_FAST](#ad313fc38e1fb56d5a9251a771e8a1119)。

快速外设时钟（Clock for Fast Peripherals）。

<a id="r_a504da1d12b02d9cbfe5de72adce02da1"></a>

```c
#define MCHP_XEC_PCR_CLK_PERIPH_SLOW 5
```

相关声明：[MCHP_XEC_PCR_CLK_PERIPH_SLOW](#a504da1d12b02d9cbfe5de72adce02da1)。

外设慢时钟（Peripheral Slow Clock）。

<a id="r_a03823c134c521480edab44781d7bb705"></a>

```c
#define MCHP_XEC_PCR_CLK_XTAL 6
```

相关声明：[MCHP_XEC_PCR_CLK_XTAL](#a03823c134c521480edab44781d7bb705)。

由外部晶体（External Crystal）派生的时钟。

<a id="r_a6aef83f9500639cabe3edc3db484b814"></a>

```c
#define MCHP_XEC_PCR_CLK_I3C 7
```

相关声明：[MCHP_XEC_PCR_CLK_I3C](#a6aef83f9500639cabe3edc3db484b814)。

具有 I3C 的 SoC 上的 I3C 控制器输入时钟（Input Clock）。

<a id="r_ac4bed4c09c83ddf32def98787224ba5d"></a>

```c
#define MCHP_XEC_SCR_ENCODE(idx, bitpos)
```

相关声明：[MCHP_XEC_SCR_ENCODE](#ac4bed4c09c83ddf32def98787224ba5d)。

编码外设的休眠使能／时钟请求／复位使能（Sleep-en/Clock-req/Reset-en）索引和位位置。

## 28.2\_详细说明（Detailed Documentation）

<a id="a645c476e2d0506aed4842d077a538a16"></a>

### `MCHP_XEC_PCR_CLK_BUS`

```c
#define MCHP_XEC_PCR_CLK_BUS 2
```

高级高性能总线（AHB）时钟。

<a id="abc3c97c553f70c6925bb07c546ad1694"></a>

### `MCHP_XEC_PCR_CLK_CORE`

```c
#define MCHP_XEC_PCR_CLK_CORE 0
```

供时钟控制驱动（Clock Control Driver）使用的时钟 ID。

内核时钟（Core Clock）。

<a id="a713a1fd7de2fe9c20e69da59e16c5f28"></a>

### `MCHP_XEC_PCR_CLK_CPU`

```c
#define MCHP_XEC_PCR_CLK_CPU 1
```

CPU 时钟。

<a id="a6aef83f9500639cabe3edc3db484b814"></a>

### `MCHP_XEC_PCR_CLK_I3C`

```c
#define MCHP_XEC_PCR_CLK_I3C 7
```

具有 I3C 的 SoC 上的 I3C 控制器输入时钟（Input Clock）。

<a id="ac772778bad2aaa564299f884150173f7"></a>

### `MCHP_XEC_PCR_CLK_PERIPH`

```c
#define MCHP_XEC_PCR_CLK_PERIPH 3
```

普通外设时钟（Clock for Normal Peripherals）。

<a id="ad313fc38e1fb56d5a9251a771e8a1119"></a>

### `MCHP_XEC_PCR_CLK_PERIPH_FAST`

```c
#define MCHP_XEC_PCR_CLK_PERIPH_FAST 4
```

快速外设时钟（Clock for Fast Peripherals）。

<a id="a504da1d12b02d9cbfe5de72adce02da1"></a>

### `MCHP_XEC_PCR_CLK_PERIPH_SLOW`

```c
#define MCHP_XEC_PCR_CLK_PERIPH_SLOW 5
```

外设慢时钟（Peripheral Slow Clock）。

<a id="a03823c134c521480edab44781d7bb705"></a>

### `MCHP_XEC_PCR_CLK_XTAL`

```c
#define MCHP_XEC_PCR_CLK_XTAL 6
```

由外部晶体（External Crystal）派生的时钟。

<a id="a569039424af967d8445fa62e28f20229"></a>

### `MCHP_XEC_PERIPH_CLK32K_SRC_PIN_SO`

```c
#define MCHP_XEC_PERIPH_CLK32K_SRC_PIN_SO 2U
```

<a id="abdee7a88e189e89bc4c721e2e5222d80"></a>

### `MCHP_XEC_PERIPH_CLK32K_SRC_PIN_XTAL`

```c
#define MCHP_XEC_PERIPH_CLK32K_SRC_PIN_XTAL 3U
```

<a id="ac71939dc0ab9d064ea43fd8fd898257c"></a>

### `MCHP_XEC_PERIPH_CLK32K_SRC_SO_SO`

```c
#define MCHP_XEC_PERIPH_CLK32K_SRC_SO_SO 0U
```

全开启（Full On）及 VBAT 运行状态下使用的外设 32 kHz 时钟源（Clock Source）。

<a id="a6bc8a1b96df3f9077e6b00da8ea8af22"></a>

### `MCHP_XEC_PERIPH_CLK32K_SRC_XTAL_XTAL`

```c
#define MCHP_XEC_PERIPH_CLK32K_SRC_XTAL_XTAL 1U
```

<a id="aa4c445cdf962557f71765cad287cb215"></a>

### `MCHP_XEC_PLL_CLK32K_SRC_PIN`

```c
#define MCHP_XEC_PLL_CLK32K_SRC_PIN 2U
```

<a id="a648809d3dcf2e2aa84641d1dcaaa333f"></a>

### `MCHP_XEC_PLL_CLK32K_SRC_SIL_OSC`

```c
#define MCHP_XEC_PLL_CLK32K_SRC_SIL_OSC 0U
```

全开启状态（Full On）下使用的 PLL 32 kHz 时钟源（Clock Source）。

<a id="a701353ae9e33d97be76c9ee0273c87fa"></a>

### `MCHP_XEC_PLL_CLK32K_SRC_XTAL`

```c
#define MCHP_XEC_PLL_CLK32K_SRC_XTAL 1U
```

<a id="ac4bed4c09c83ddf32def98787224ba5d"></a>

### `MCHP_XEC_SCR_ENCODE`

```c
#define MCHP_XEC_SCR_ENCODE ( idx, bitpos )
```

展开值（Value）：

```c
(((idx) & 0x7) | (((bitpos) & 0x1f) << 3))
```

编码外设的休眠使能／时钟请求／复位使能（Sleep-en/Clock-req/Reset-en）索引和位位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | PCR SCR 寄存器从零开始的索引（Zero-based Index），范围 `0–4`。 |
| `bitpos` | 在 32 位 PCR SCR 寄存器中的位位置（Position）。 |


## 28.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P507_mchp_xec_pcr.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P027_zephyr__dt-bindings__clock__mchp_sam_d5x_e5x_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__net__net_config.h_文件参考.md)
