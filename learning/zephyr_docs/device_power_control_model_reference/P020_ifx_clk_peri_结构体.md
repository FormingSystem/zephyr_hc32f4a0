---
id: learning.zephyr-docs.device-power-control-model-reference.page-20
title: ifx_clk_peri_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structifx__clk__peri.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_ifx\_clk\_peri\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structifx__clk__peri.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Infineon外设时钟说明符（Peripheral Clock Specifier）。

```c
#include <zephyr/drivers/clock_control/clock_control_ifx.h>
```

<a id="details"></a>

Infineon外设时钟说明符（Peripheral Clock Specifier）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_aacbb68c082f9ee6385e0a26436553711"></a>

```c
uint32_t div_ord
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[div_ord](#aacbb68c082f9ee6385e0a26436553711)。

所引用 `peri-div` 分频器节点的依赖序号（Dependency ordinal）。

<a id="r_a5f6b88b1827ed1fc2a20613475bf82c2"></a>

```c
uint8_t rootclk_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rootclk_id](#a5f6b88b1827ed1fc2a20613475bf82c2)。

根时钟 ID（外设时钟 ID / 外设多路复用器 ID）。

## 20.2\_详细说明（Detailed Documentation）

<a id="aacbb68c082f9ee6385e0a26436553711"></a>

### `div_ord`

```c
uint32_t ifx_clk_peri::div_ord
```

所引用 `peri-div` 分频器节点的依赖序号（Dependency ordinal）。

<a id="a5f6b88b1827ed1fc2a20613475bf82c2"></a>

### `rootclk_id`

```c
uint8_t ifx_clk_peri::rootclk_id
```

根时钟 ID（外设时钟 ID / 外设多路复用器 ID）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_ifx.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_ifx.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_ifx_clk_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_it8801_mfd_callback_结构体.md)
