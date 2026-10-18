---
id: learning.zephyr-docs.network-core-model-reference.page-47
title: net_buf_pool_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__pool.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_net\_buf\_pool\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__pool.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络缓冲池（Network Buffer Pool）的表示。

```c
#include <zephyr/net_buf.h>
```

<a id="details"></a>

网络缓冲池（Network Buffer Pool）的表示。此结构用于表示一组网络缓冲区构成的池。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_a97e5b2e51238e859f93882a8008ba305"></a>

```c
struct k_lifo free
```

相关声明：[k_lifo](../queue_reference/P006_内核LIFO结构.md)、[free](#a97e5b2e51238e859f93882a8008ba305)。

缓冲区空闲时放入的后进先出队列（LIFO）。

<a id="r_ae92fc3f3f51be63ccdeee9614d21cc34"></a>

```c
struct k_spinlock lock
```

相关声明：[k_spinlock](../kernel/P066_自旋锁结构参考.md)、[lock](#ae92fc3f3f51be63ccdeee9614d21cc34)。

用于防止并发访问或修改（Concurrent Access / Modifications）。

<a id="r_a55b57f4f573c7e752c3ccf2f92f25626"></a>

```c
const uint16_t buf_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[buf_count](#a55b57f4f573c7e752c3ccf2f92f25626)。

池中的缓冲区数量。

<a id="r_a3fdf83b4c0b5acefbb761da285791ad2"></a>

```c
uint16_t uninit_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uninit_count](#a3fdf83b4c0b5acefbb761da285791ad2)。

尚未初始化的缓冲区数量。

<a id="r_a4718ecec19d7e2ccaf04b6ff61120975"></a>

```c
uint8_t user_data_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[user_data_size](#a4718ecec19d7e2ccaf04b6ff61120975)。

分配给此池的用户数据（User Data）大小。

<a id="r_a2a9141d7cd20cd98818a92dc5bc99f56"></a>

```c
void(*const destroy )(struct net_buf *buf)
```

相关声明：[destroy](#a2a9141d7cd20cd98818a92dc5bc99f56)、[net_buf](P046_net_buf_结构体.md)。

缓冲区释放时可选的销毁回调（Destroy Callback）。

<a id="r_a617bd8f77e55481d97183da8c0c62cc5"></a>

```c
const struct net_buf_data_alloc * alloc
```

相关声明：[alloc](#a617bd8f77e55481d97183da8c0c62cc5)。

数据分配处理程序（Data Allocation Handlers）。

## 47.2\_详细说明（Detailed Documentation）

<a id="a617bd8f77e55481d97183da8c0c62cc5"></a>

### `alloc`

```c
const struct net_buf_data_alloc* net_buf_pool::alloc
```

数据分配处理程序（Data Allocation Handlers）。

<a id="a55b57f4f573c7e752c3ccf2f92f25626"></a>

### `buf_count`

```c
const uint16_t net_buf_pool::buf_count
```

池中的缓冲区数量。

<a id="a2a9141d7cd20cd98818a92dc5bc99f56"></a>

### `destroy`

```c
void(*const net_buf_pool::destroy) (struct net_buf *buf)
```

缓冲区释放时可选的销毁回调（Destroy Callback）。

<a id="a97e5b2e51238e859f93882a8008ba305"></a>

### `free`

```c
struct k_lifo net_buf_pool::free
```

缓冲区空闲时放入的后进先出队列（LIFO）。

<a id="ae92fc3f3f51be63ccdeee9614d21cc34"></a>

### `lock`

```c
struct k_spinlock net_buf_pool::lock
```

用于防止并发访问或修改（Concurrent Access / Modifications）。

<a id="a3fdf83b4c0b5acefbb761da285791ad2"></a>

### `uninit_count`

```c
uint16_t net_buf_pool::uninit_count
```

尚未初始化的缓冲区数量。

<a id="a4718ecec19d7e2ccaf04b6ff61120975"></a>

### `user_data_size`

```c
uint8_t net_buf_pool::user_data_size
```

分配给此池的用户数据（User Data）大小。

本数据类型文档由以下文件生成：

- `zephyr/net_buf.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)
- [k_lifo](../queue_reference/P006_内核LIFO结构.md)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](P046_net_buf_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_net_buf_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_net_buf_simple_结构体.md)
