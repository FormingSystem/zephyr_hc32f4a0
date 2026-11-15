---
id: learning.zephyr-docs.network-core-model-reference.page-49
title: net_buf_simple_state_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__simple__state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_net\_buf\_simple\_state\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__simple__state.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

缓冲区的解析状态（Parsing State）。

```c
#include <zephyr/net_buf.h>
```

<a id="details"></a>

缓冲区解析状态（Parsing State）。把解析控制权交给不受自身控制的例程时，用于临时保存缓冲区的解析状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_a4061f8e50e14289b1ec999ef490c8fbf"></a>

```c
uint16_t offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[offset](#a4061f8e50e14289b1ec999ef490c8fbf)。

数据指针相对于存储起点的偏移量（Offset）。

<a id="r_af0e544fe2b018a7ff0b30970e9de8253"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#af0e544fe2b018a7ff0b30970e9de8253)。

数据长度。

## 49.2\_详细说明（Detailed Documentation）

<a id="af0e544fe2b018a7ff0b30970e9de8253"></a>

### `len`

```c
uint16_t net_buf_simple_state::len
```

数据长度。

<a id="a4061f8e50e14289b1ec999ef490c8fbf"></a>

### `offset`

```c
uint16_t net_buf_simple_state::offset
```

数据指针相对于存储起点的偏移量（Offset）。

本数据类型文档由以下文件生成：

- `zephyr/net_buf.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_net_buf_simple_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_net_capture_cooked_结构体.md)
