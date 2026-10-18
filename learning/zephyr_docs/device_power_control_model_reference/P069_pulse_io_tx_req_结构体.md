---
id: learning.zephyr-docs.device-power-control-model-reference.page-69
title: pulse_io_tx_req_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__tx__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_pulse\_io\_tx\_req\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__tx__req.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

发送提交描述符（TX Submission Descriptor）。

```c
#include <zephyr/drivers/pulse_io.h>
```

<a id="details"></a>

发送提交描述符（TX submission descriptor）。仅使用 `symbols` 或 `cells` 其中之一，由通道配置的 `pulse_io_mode` 决定。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_affd286c15d5fcc44c706fc3c9e6c23be"></a>

```c
const struct pulse_symbol * symbols
```

相关声明：[pulse_symbol](P070_pulse_symbol_结构体.md)、[symbols](#a33af6b148afa43e93d1b8826d78198d7)。

SYMBOL 模式的源缓冲区。

<a id="r_ab0e686f82e37f759e2946f2ec6ae8ae3"></a>

```c
const struct pulse_cell * cells
```

相关声明：[pulse_cell](P061_pulse_cell_结构体.md)、[cells](#a21426e72b2eaab937e86d50e46177505)。

CELL 模式的源缓冲区。

<a id="r_a1240ebcd4760932cf32905144f08809b"></a>

```c
};
```

源缓冲区，按配置的模式解释。

<a id="r_a39ecb966484761d419c10cd41ae15512"></a>

```c
size_t count
```

相关声明：[count](#a39ecb966484761d419c10cd41ae15512)。

源缓冲区中的条目数。

<a id="r_a39ba9d615f8b40f117bd3efc97bdacd7"></a>

```c
uint32_t loop_count
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[loop_count](#a39ba9d615f8b40f117bd3efc97bdacd7)。

`0`：单次发送；`1..tx_loop_max`：有限次数循环；`UINT32_MAX`：无限循环。

## 69.2\_详细说明（Detailed Documentation）

<a id="a1240ebcd4760932cf32905144f08809b"></a>

### `[union]`

```c
union { ... } pulse_io_tx_req
```

源缓冲区，按配置的模式解释。

<a id="a21426e72b2eaab937e86d50e46177505"></a>

### `cells`

```c
const struct pulse_cell* pulse_io_tx_req::cells
```

CELL 模式的源缓冲区。

<a id="a39ecb966484761d419c10cd41ae15512"></a>

### `count`

```c
size_t pulse_io_tx_req::count
```

源缓冲区中的条目数。

<a id="a39ba9d615f8b40f117bd3efc97bdacd7"></a>

### `loop_count`

```c
uint32_t pulse_io_tx_req::loop_count
```

`0`：单次发送；`1..tx_loop_max`：有限次数循环；`UINT32_MAX`：无限循环。

<a id="a33af6b148afa43e93d1b8826d78198d7"></a>

### `symbols`

```c
const struct pulse_symbol* pulse_io_tx_req::symbols
```

SYMBOL 模式的源缓冲区。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pulse_io.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pulse_io.h](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html)
- [pulse_symbol](P070_pulse_symbol_结构体.md)
- [pulse_cell](P061_pulse_cell_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pulse_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga8a69608ee00587642aca6e0d69878b07)
- [pulse_io_tx_req](P069_pulse_io_tx_req_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_pulse_io_rx_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_pulse_symbol_结构体.md)
