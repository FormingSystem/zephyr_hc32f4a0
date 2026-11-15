---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-19
title: clock_mchp_subsys_pll_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__pll__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_clock\_mchp\_subsys\_pll\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__pll__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

锁相环（Phase-Locked Loop，PLL）配置结构体。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h>
```

<a id="details"></a>

锁相环（Phase-Locked Loop，PLL）配置结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a1d40f6f5bc7610d5db8d7fc7c16ccd54"></a>

```c
uint16_t feedback_divider_factor
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[feedback_divider_factor](#a1d40f6f5bc7610d5db8d7fc7c16ccd54)。

PLL 压控振荡器（Voltage-Controlled Oscillator，VCO）输出频率与参考输入频率的比值。

<a id="r_ae4de7160ef688c54e4d7741b695353eb"></a>

```c
uint8_t ref_division_factor
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ref_division_factor](#ae4de7160ef688c54e4d7741b695353eb)。

确定 PLL 输入参考频率的分频因子，范围为 `1 ≤ REFDIV ≤ 63`。

<a id="r_af96f2f4bdf60d50f3942c3cc55703ad6"></a>

```c
bool on_demand_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[on_demand_en](#af96f2f4bdf60d50f3942c3cc55703ad6)。

外设请求将振荡器用作时钟源时，配置振荡器开启。

<a id="r_a67f3c481143ff8f860ae7f2fabf16867"></a>

```c
enum clock_mchp_pll_src_clock src
```

相关声明：[clock_mchp_pll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555e)、[src](#a67f3c481143ff8f860ae7f2fabf16867)。

参考源时钟选择（Reference Source Clock Selection）。

## 19.2\_详细说明（Detailed Documentation）

<a id="a1d40f6f5bc7610d5db8d7fc7c16ccd54"></a>

### `feedback_divider_factor`

```c
uint16_t clock_mchp_subsys_pll_config::feedback_divider_factor
```

PLL 压控振荡器（Voltage-Controlled Oscillator，VCO）输出频率与参考输入频率的比值。

<a id="af96f2f4bdf60d50f3942c3cc55703ad6"></a>

### `on_demand_en`

```c
bool clock_mchp_subsys_pll_config::on_demand_en
```

外设请求将振荡器用作时钟源时，配置振荡器开启。

<a id="ae4de7160ef688c54e4d7741b695353eb"></a>

### `ref_division_factor`

```c
uint8_t clock_mchp_subsys_pll_config::ref_division_factor
```

确定 PLL 输入参考频率的分频因子，范围为 `1 ≤ REFDIV ≤ 63`。

<a id="a67f3c481143ff8f860ae7f2fabf16867"></a>

### `src`

```c
enum clock_mchp_pll_src_clock clock_mchp_subsys_pll_config::src
```

参考源时钟选择（Reference Source Clock Selection）。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [clock_mchp_pll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html#a1f0a363c4b5d2260d614bc0b2e19555e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_clock_mchp_subsys_oschf_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_clock_mchp_subsys_pll_out_config_结构体.md)
