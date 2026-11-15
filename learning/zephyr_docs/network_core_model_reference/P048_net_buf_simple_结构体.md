---
id: learning.zephyr-docs.network-core-model-reference.page-48
title: net_buf_simple_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__simple.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_net\_buf\_simple\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__simple.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

简单网络缓冲区（Simple Network Buffer）的表示。

```c
#include <zephyr/net_buf.h>
```

<a id="details"></a>

简单网络缓冲区（Simple Network Buffer）的表示。这是net_buf对象的简化版本，实际上net_buf内部也使用net_buf_simple。它不提供引用计数、用户数据、动态分配，也通常不能通过FIFO等内核对象传递。主要用于不需要普通net_buf元数据、且这些元数据开销过大的场景，例如仅需在栈上分配缓冲区，或缓冲区访问及生命周期（Lifetime）受到良好控制与约束时。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_ad232efff435f425d30ac78f5abf2d8b1"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ad232efff435f425d30ac78f5abf2d8b1)。

指向缓冲区数据起点的指针。

<a id="r_ae8707c50d70c26b53281b40eb1720cf3"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#ae8707c50d70c26b53281b40eb1720cf3)。

数据指针（Data Pointer）之后的数据长度。

<a id="r_ae6dc4aa029a67d3911293618eb30caa6"></a>

```c
uint16_t size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[size](#ae6dc4aa029a67d3911293618eb30caa6)。

net_buf_simple::__buf可以存储的数据量。

## 48.2\_详细说明（Detailed Documentation）

<a id="ad232efff435f425d30ac78f5abf2d8b1"></a>

### `data`

```c
uint8_t* net_buf_simple::data
```

指向缓冲区数据起点的指针。

<a id="ae8707c50d70c26b53281b40eb1720cf3"></a>

### `len`

```c
uint16_t net_buf_simple::len
```

数据指针（Data Pointer）之后的数据长度。

还能容纳更多数据的空间应通过net_buf_simple_tailroom()取得，而不是net_buf_simple::size减去net_buf_simple::len，因为net_buf_simple::size也计入了头部预留空间（Headroom）。

<a id="ae6dc4aa029a67d3911293618eb30caa6"></a>

### `size`

```c
uint16_t net_buf_simple::size
```

net_buf_simple::__buf可以存储的数据量。

本数据类型文档由以下文件生成：

- `zephyr/net_buf.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](P046_net_buf_结构体.md)
- [net_buf_simple](P048_net_buf_simple_结构体.md)
- [net_buf_simple_tailroom()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga73e2c42fc23e857a46553084b747c996)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_net_buf_pool_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_net_buf_simple_state_结构体.md)
