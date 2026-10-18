---
id: learning.zephyr-docs.network-core-model-reference.page-114
title: net_pkt_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__pkt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第114章\_net\_pkt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__pkt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络数据包（Network Packet）。

```c
#include <zephyr/net/net_pkt.h>
```

<a id="details"></a>

网络数据包（Network packet）。注意，向 `net_pkt` 添加新字段时，也要更新 `net_pkt_clone()` 函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 114.1\_数据成员（Data Fields）

<a id="r_a96e82461f6786814de708049f2bc0b22"></a>

```c
intptr_t fifo
```

相关声明：[intptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0bd5dec00e345e69027427f8621d6a6c)、[fifo](#a96e82461f6786814de708049f2bc0b22)。

接收／发送线程（RX/TX threads）和套接字层（Socket layer）使用此先进先出队列（FIFO）。

<a id="r_add4540bddb5c549a5ae61b99b14b0b54"></a>

```c
struct k_mem_slab * slab
```

相关声明：[slab](#add4540bddb5c549a5ae61b99b14b0b54)。

指向其所属内存块池（Slab）的指针。

```c
union {
```

<a id="r_a88a57bf020625487421267c32af6aab3"></a>

```c
struct net_buf * frags
```

相关声明：[net_buf](P046_net_buf_结构体.md)、[frags](#a1c27e50656b8c2713704d979b902c5d6)。

缓冲区片段（Buffer fragment）。

<a id="r_af1099711dc3b09e169e46020d4050251"></a>

```c
struct net_buf * buffer
```

相关声明：[net_buf](P046_net_buf_结构体.md)、[buffer](#ad319458430aa691b88e24776e843d30b)。

缓冲区片段的别名（Alias to a buffer fragment）。

<a id="r_a76f873778e8c46f508a71d6c3a93f588"></a>

```c
};
```

保存数据包的缓冲区（Buffer holding the packet）。

<a id="r_a52f155a86698a929fa2130b594630d06"></a>

```c
struct net_pkt_cursor cursor
```

相关声明：[cursor](#a52f155a86698a929fa2130b594630d06)。

用于读写的内部缓冲区迭代器（Internal buffer iterator）。

<a id="r_a4b9c3f62209f4d7748070224654360cf"></a>

```c
struct net_context * context
```

相关声明：[net_context](P055_net_context_结构体.md)、[context](#a4b9c3f62209f4d7748070224654360cf)。

网络连接上下文（Network connection context）。

<a id="r_a7590eeacf06469206cb7e7949acfa7b2"></a>

```c
struct net_if * iface
```

相关声明：[net_if](P079_net_if_结构体.md)、[iface](#a7590eeacf06469206cb7e7949acfa7b2)。

网络接口（Network Interface）

## 114.2\_详细说明（Detailed Documentation）

<a id="a76f873778e8c46f508a71d6c3a93f588"></a>

### `[union]`

```c
union { ... } net_pkt
```

保存数据包的缓冲区（Buffer holding the packet）。

<a id="ad319458430aa691b88e24776e843d30b"></a>

### `buffer`

```c
struct net_buf* net_pkt::buffer
```

缓冲区片段的别名（Alias to a buffer fragment）。

<a id="a4b9c3f62209f4d7748070224654360cf"></a>

### `context`

```c
struct net_context* net_pkt::context
```

网络连接上下文（Network connection context）。

<a id="a52f155a86698a929fa2130b594630d06"></a>

### `cursor`

```c
struct net_pkt_cursor net_pkt::cursor
```

用于读写的内部缓冲区迭代器（Internal buffer iterator）。

<a id="a96e82461f6786814de708049f2bc0b22"></a>

### `fifo`

```c
intptr_t net_pkt::fifo
```

接收／发送线程（RX/TX threads）和套接字层（Socket layer）使用此先进先出队列（FIFO）。

通过先进先出队列（FIFO）将 `net_pkt` 排入处理线程（Processing thread）的队列。

<a id="a1c27e50656b8c2713704d979b902c5d6"></a>

### `frags`

```c
struct net_buf* net_pkt::frags
```

缓冲区片段（Buffer fragment）。

<a id="a7590eeacf06469206cb7e7949acfa7b2"></a>

### `iface`

```c
struct net_if* net_pkt::iface
```

网络接口（Network Interface）

<a id="add4540bddb5c549a5ae61b99b14b0b54"></a>

### `slab`

```c
struct k_mem_slab* net_pkt::slab
```

指向其所属内存块池（Slab）的指针。

本数据类型文档由以下文件生成：

- `zephyr/net/net_pkt.h`

## 114.3\_原页交叉引用（Cross References）

- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h_source.html)
- [intptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0bd5dec00e345e69027427f8621d6a6c)
- [net_buf](P046_net_buf_结构体.md)
- [net_context](P055_net_context_结构体.md)
- [net_if](P079_net_if_结构体.md)
- [net_pkt](P114_net_pkt_结构体.md)
- [net_pkt_clone()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html#gaefefe50d0c68fb4997abc7b309740959)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P113_net_packet_mreq_结构体.md) · [返回大纲](大纲.md) · [下一章](P115_net_ptp_extended_time_结构体.md)
