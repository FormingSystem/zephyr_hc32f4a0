---
id: learning.zephyr-docs.device-power-control-model-reference.page-70
title: pulse_symbol_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpulse__symbol.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_pulse\_symbol\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpulse__symbol.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

脉冲流（Pulse Stream）的一个符号。

```c
#include <zephyr/drivers/pulse_io.h>
```

<a id="details"></a>

脉冲流中的一个符号（Symbol）。`duration` 以所配置 `resolution_hz` 对应的节拍数表示。注意：此位域布局是 RAM 中的 API 约定，不是线路传输格式，也不是 DMA 格式。通过 DMA 向硬件提供数据的后端必须转换为自身的紧凑表示，不能直接传输此结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

<a id="r_aa164a0e6915c09bf376739ea724bf3e5"></a>

```c
uint32_t duration: 31
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[duration](#aa164a0e6915c09bf376739ea724bf3e5)。

持续时间，以所配置分辨率的节拍数表示。

<a id="r_abcebf0eaf2ca01ab0144b23153b024fc"></a>

```c
uint32_t level: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[level](#abcebf0eaf2ca01ab0144b23153b024fc)。

此持续时间内的线路电平，取 `0` 或 `1`。

## 70.2\_详细说明（Detailed Documentation）

<a id="aa164a0e6915c09bf376739ea724bf3e5"></a>

### `duration`

```c
uint32_t pulse_symbol::duration
```

持续时间，以所配置分辨率的节拍数表示。

<a id="abcebf0eaf2ca01ab0144b23153b024fc"></a>

### `level`

```c
uint32_t pulse_symbol::level
```

此持续时间内的线路电平，取 `0` 或 `1`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pulse_io.h`

## 70.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pulse_io.h](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_pulse_io_tx_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_rcar_cpg_clk_结构体.md)
