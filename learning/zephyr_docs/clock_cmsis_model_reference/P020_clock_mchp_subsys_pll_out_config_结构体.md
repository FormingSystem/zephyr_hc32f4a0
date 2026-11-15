---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-20
title: clock_mchp_subsys_pll_out_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__pll__out__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_clock\_mchp\_subsys\_pll\_out\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__pll__out__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

PLL 输出配置结构体（PLL Output Configuration Structure）。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h>
```

<a id="details"></a>

PLL 输出配置结构体（PLL Output Configuration Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_a3483433887d306cc9f2acff66654cd32"></a>

```c
uint8_t output_division_factor
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[output_division_factor](#a3483433887d306cc9f2acff66654cd32)。

确定 PLL 的 VCO 频率输出的分频因子，范围为 `1 ≤ POSTDIV ≤ 63`。

## 20.2\_详细说明（Detailed Documentation）

<a id="a3483433887d306cc9f2acff66654cd32"></a>

### `output_division_factor`

```c
uint8_t clock_mchp_subsys_pll_out_config::output_division_factor
```

确定 PLL 的 VCO 频率输出的分频因子，范围为 `1 ≤ POSTDIV ≤ 63`。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_clock_mchp_subsys_pll_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_clock_mchp_subsys_rtc_config_结构体.md)
