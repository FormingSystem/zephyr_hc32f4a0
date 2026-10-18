---
id: learning.zephyr-docs.device-power-control-model-reference.page-68
title: pulse_io_rx_req_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__rx__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_pulse\_io\_rx\_req\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__rx__req.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接收提交描述符（RX Submission Descriptor）。

```c
#include <zephyr/drivers/pulse_io.h>
```

<a id="details"></a>

接收提交描述符（RX Submission Descriptor）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a4b2ced7da249c63f08743154e8c9706c"></a>

```c
struct pulse_symbol * symbols
```

相关声明：[pulse_symbol](P070_pulse_symbol_结构体.md)、[symbols](#a5847bb48236f6d665b176daf72cdee6e)。

符号（SYMBOL）模式的目的缓冲区。

<a id="r_aa24d7cd2ddad5a44715d0fe88a82e524"></a>

```c
struct pulse_cell * cells
```

相关声明：[pulse_cell](P061_pulse_cell_结构体.md)、[cells](#a70ae274b716278583e655e2457577f58)。

单元（CELL）模式的目的缓冲区。

<a id="r_ad1ee7773825f87bd06d3826de0890e91"></a>

```c
};
```

目的缓冲区，按配置的模式解释。

<a id="r_a3412f6080ba7eaecaf1d4b532b77451a"></a>

```c
size_t capacity
```

相关声明：[capacity](#a3412f6080ba7eaecaf1d4b532b77451a)。

目的缓冲区容量，以条目数计。

## 68.2\_详细说明（Detailed Documentation）

<a id="ad1ee7773825f87bd06d3826de0890e91"></a>

### `[union]`

```c
union { ... } pulse_io_rx_req
```

目的缓冲区，按配置的模式解释。

<a id="a3412f6080ba7eaecaf1d4b532b77451a"></a>

### `capacity`

```c
size_t pulse_io_rx_req::capacity
```

目的缓冲区容量，以条目数计。

<a id="a70ae274b716278583e655e2457577f58"></a>

### `cells`

```c
struct pulse_cell* pulse_io_rx_req::cells
```

单元（CELL）模式的目的缓冲区。

<a id="a5847bb48236f6d665b176daf72cdee6e"></a>

### `symbols`

```c
struct pulse_symbol* pulse_io_rx_req::symbols
```

符号（SYMBOL）模式的目的缓冲区。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pulse_io.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pulse_io.h](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html)
- [pulse_symbol](P070_pulse_symbol_结构体.md)
- [pulse_cell](P061_pulse_cell_结构体.md)
- [pulse_io_rx_req](P068_pulse_io_rx_req_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_pulse_io_encoder_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_pulse_io_tx_req_结构体.md)
