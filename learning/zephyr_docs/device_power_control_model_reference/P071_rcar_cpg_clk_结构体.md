---
id: learning.zephyr-docs.device-power-control-model-reference.page-71
title: rcar_cpg_clk_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrcar__cpg__clk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_rcar\_cpg\_clk\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrcar__cpg__clk.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

R-Car CPG/MSSR时钟子系统选择器（Clock Subsystem Selector）。

```c
#include <zephyr/drivers/clock_control/renesas_cpg_mssr.h>
```

<a id="details"></a>

R-Car CPG/MSSR时钟子系统选择器（Clock Subsystem Selector）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.1\_数据成员（Data Fields）

<a id="r_a126cf65226ac7e3521c724d4c9d7b3a4"></a>

```c
uint32_t domain
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[domain](#a126cf65226ac7e3521c724d4c9d7b3a4)。

时钟域（Clock domain）。

<a id="r_aff97932d122b50e3d7546adfe2fc29f5"></a>

```c
uint32_t module
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[module](#aff97932d122b50e3d7546adfe2fc29f5)。

域内的模块（MSSR）标识符。

<a id="r_a84f173b12e610177932cf58d85659f0e"></a>

```c
uint32_t rate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rate](#a84f173b12e610177932cf58d85659f0e)。

请求的时钟频率，单位为 Hz。

## 71.2\_详细说明（Detailed Documentation）

<a id="a126cf65226ac7e3521c724d4c9d7b3a4"></a>

### `domain`

```c
uint32_t rcar_cpg_clk::domain
```

时钟域（Clock domain）。

<a id="aff97932d122b50e3d7546adfe2fc29f5"></a>

### `module`

```c
uint32_t rcar_cpg_clk::module
```

域内的模块（MSSR）标识符。

<a id="a84f173b12e610177932cf58d85659f0e"></a>

### `rate`

```c
uint32_t rcar_cpg_clk::rate
```

请求的时钟频率，单位为 Hz。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/renesas_cpg_mssr.h`

## 71.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/renesas_cpg_mssr.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2renesas__cpg__mssr_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_pulse_symbol_结构体.md) · [返回大纲](大纲.md) · [下一章](P072_rcar_pin_func_结构体.md)
