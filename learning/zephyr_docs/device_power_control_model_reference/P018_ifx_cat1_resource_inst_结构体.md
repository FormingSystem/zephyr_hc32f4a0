---
id: learning.zephyr-docs.device-power-control-model-reference.page-18
title: ifx_cat1_resource_inst_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structifx__cat1__resource__inst.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_ifx\_cat1\_resource\_inst\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structifx__cat1__resource__inst.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CAT1资源实例描述符（Resource Instance Descriptor）。

```c
#include <zephyr/drivers/clock_control/clock_control_ifx_cat1.h>
```

<a id="details"></a>

CAT1资源实例描述符（Resource Instance Descriptor）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_a711df9cb83f6d7545b939fd56a7e10e7"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a711df9cb83f6d7545b939fd56a7e10e7)。

资源模块类型（Resource block type）。

<a id="r_a50f1d0589e90b071ddc451efcbb56892"></a>

```c
uint8_t block_num
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[block_num](#a50f1d0589e90b071ddc451efcbb56892)。

资源模块索引。

<a id="r_ad71f2ec8d25fa0792e287b1e0a58ca3f"></a>

```c
uint8_t channel_num
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_num](#ad71f2ec8d25fa0792e287b1e0a58ca3f)。

如果资源类型为每个模块实例定义了多个通道，则表示通道编号。

## 18.2\_详细说明（Detailed Documentation）

<a id="a50f1d0589e90b071ddc451efcbb56892"></a>

### `block_num`

```c
uint8_t ifx_cat1_resource_inst::block_num
```

资源模块索引。

<a id="ad71f2ec8d25fa0792e287b1e0a58ca3f"></a>

### `channel_num`

```c
uint8_t ifx_cat1_resource_inst::channel_num
```

如果资源类型为每个模块实例定义了多个通道，则表示通道编号。

否则为 `0`。

<a id="a711df9cb83f6d7545b939fd56a7e10e7"></a>

### `type`

```c
uint8_t ifx_cat1_resource_inst::type
```

资源模块类型（Resource block type）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_ifx_cat1.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_ifx_cat1.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx__cat1_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_ifx_cat1_clock_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_ifx_clk_结构体.md)
