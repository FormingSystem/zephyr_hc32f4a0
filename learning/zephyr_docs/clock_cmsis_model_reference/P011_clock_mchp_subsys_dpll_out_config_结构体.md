---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-11
title: clock_mchp_subsys_dpll_out_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__dpll__out__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_clock\_mchp\_subsys\_dpll\_out\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__dpll__out__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

DPLL 输出配置结构体（DPLL Output Configuration Structure）。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h>
```

<a id="details"></a>

DPLL 输出配置结构体（DPLL Output Configuration Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a181501af2102f2fd1e3bf3a0e02af531"></a>

```c
uint8_t output_division_factor
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[output_division_factor](#a181501af2102f2fd1e3bf3a0e02af531)。

确定 PLL 的 VCO 频率输出的分频因子，范围为 `1 ≤ POSTDIV ≤ 63`。

## 11.2\_详细说明（Detailed Documentation）

<a id="a181501af2102f2fd1e3bf3a0e02af531"></a>

### `output_division_factor`

```c
uint8_t clock_mchp_subsys_dpll_out_config::output_division_factor
```

确定 PLL 的 VCO 频率输出的分频因子，范围为 `1 ≤ POSTDIV ≤ 63`。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mchp_clock_pic32cz_ca.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_clock_mchp_subsys_dpll_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_clock_mchp_subsys_fdpll_config_结构体.md)
