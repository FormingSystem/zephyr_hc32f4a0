---
id: learning.zephyr-docs.device-power-control-model-reference.page-19
title: ifx_clk_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structifx__clk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_ifx\_clk\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structifx__clk.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Infineon时钟说明符（Clock Specifier）。

```c
#include <zephyr/drivers/clock_control/clock_control_ifx.h>
```

<a id="details"></a>

Infineon时钟说明符（Clock Specifier）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a244fa8efec2792704d70a0c9a2f061bd"></a>

```c
uint8_t clk
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clk](#a244fa8efec2792704d70a0c9a2f061bd)。

时钟类型。

<a id="r_afb377cb6f9831a5537e4f4e3272a4809"></a>

```c
uint8_t clk_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clk_id](#afb377cb6f9831a5537e4f4e3272a4809)。

时钟 ID。

## 19.2\_详细说明（Detailed Documentation）

<a id="a244fa8efec2792704d70a0c9a2f061bd"></a>

### `clk`

```c
uint8_t ifx_clk::clk
```

时钟类型。

<a id="afb377cb6f9831a5537e4f4e3272a4809"></a>

### `clk_id`

```c
uint8_t ifx_clk::clk_id
```

时钟 ID。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_ifx.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_ifx.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_ifx_cat1_resource_inst_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_ifx_clk_peri_结构体.md)
