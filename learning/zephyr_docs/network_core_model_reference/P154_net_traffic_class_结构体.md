---
id: learning.zephyr-docs.network-core-model-reference.page-154
title: net_traffic_class_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__traffic__class.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第154章\_net\_traffic\_class\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__traffic__class.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络流量类别（Network Traffic Class）。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

网络流量类别（Network traffic class）。流量类别用于发送或接收按不同优先级分类的数据。因此，可将某些流量标记为高优先级，使其优先发送或接收。每个发送或接收的网络数据包都会经过先进先出队列（FIFO），交给执行传输的线程。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 154.1\_数据成员（Data Fields）

<a id="r_a94511ca12bad1687f5c7ca862c857ded"></a>

```c
struct k_fifo fifo
```

相关声明：[k_fifo](../queue_reference/P004_内核FIFO结构.md)、[fifo](#a94511ca12bad1687f5c7ca862c857ded)。

处理此发送（TX）或接收（RX）数据包的先进先出队列（FIFO）。

<a id="r_a8d0023588fee0a8ff1381bbc80ada143"></a>

```c
struct k_thread handler
```

相关声明：[k_thread](../thread_core_reference/P004_线程对象结构.md)、[handler](#a8d0023588fee0a8ff1381bbc80ada143)。

流量类别处理线程（Traffic class handler thread）。

<a id="r_a2d98bc68d38bdef649d645b8b52516c5"></a>

```c
k_thread_stack_t * stack
```

相关声明：[k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)、[stack](#a2d98bc68d38bdef649d645b8b52516c5)。

此处理程序的栈（Handler stack）。

## 154.2\_详细说明（Detailed Documentation）

<a id="a94511ca12bad1687f5c7ca862c857ded"></a>

### `fifo`

```c
struct k_fifo net_traffic_class::fifo
```

处理此发送（TX）或接收（RX）数据包的先进先出队列（FIFO）。

<a id="a8d0023588fee0a8ff1381bbc80ada143"></a>

### `handler`

```c
struct k_thread net_traffic_class::handler
```

流量类别处理线程（Traffic class handler thread）。

<a id="a2d98bc68d38bdef649d645b8b52516c5"></a>

### `stack`

```c
k_thread_stack_t* net_traffic_class::stack
```

此处理程序的栈（Handler stack）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 154.3\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P153_net_stats_wifi_结构体.md) · [返回大纲](大纲.md) · [下一章](P155_net_trickle_结构体.md)
