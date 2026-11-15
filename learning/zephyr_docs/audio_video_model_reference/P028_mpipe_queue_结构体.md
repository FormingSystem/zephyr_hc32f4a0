---
id: learning.zephyr-docs.audio-video-model-reference.page-28
title: mpipe_queue_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__queue.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_mpipe\_queue\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__queue.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

队列元素（Queue Element）的结构。

```c
#include <zephyr/mpipe/base/mpipe_queue.h>
```

<a id="details"></a>

队列元素（Queue Element）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_a7372d2798449c6d49aae12781ae0ac2a"></a>

```c
struct mpipe_transform transform
```

相关声明：[mpipe_transform](P034_mpipe_transform_结构体.md)、[transform](#a7372d2798449c6d49aae12781ae0ac2a)。

基础变换元素（base transform element）。

<a id="r_a64f81e4ac2cb75cdb4d1a45920211daa"></a>

```c
struct mpipe_thread thread
```

相关声明：[mpipe_thread](P033_mpipe_thread_结构体.md)、[thread](#a64f81e4ac2cb75cdb4d1a45920211daa)。

专门执行下游处理的线程。

<a id="r_a36ee4b88ec2fc501f98e72985ea651a8"></a>

```c
struct k_msgq msgq
```

相关声明：[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)、[msgq](#a36ee4b88ec2fc501f98e72985ea651a8)。

缓冲区指针队列。

<a id="r_aa392264ebe9576abecce5ec3c91daaa7"></a>

```c
char msgq_buffer [(CONFIG_MPIPE_BASE_QUEUE_MAX_SIZE+2) *sizeof(void *)]
```

相关声明：[msgq_buffer](#aa392264ebe9576abecce5ec3c91daaa7)。

消息队列的后备存储空间，大小可容纳最大队列以及 EOS 和暂停哨兵（pause sentinel）。

<a id="r_a4f0676f92ac9a2057af2eca5fd577640"></a>

```c
uint8_t size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[size](#a4f0676f92ac9a2057af2eca5fd577640)。

队列可容纳的缓冲区数量，受 `CONFIG_MPIPE_BASE_QUEUE_MAX_SIZE` 限制，并在 `READY -> PAUSED` 时应用。

<a id="r_a9950b600a3803eae60e93b28b4ca3986"></a>

```c
uint8_t leak
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[leak](#a9950b600a3803eae60e93b28b4ca3986)。

队列已满时的丢弃策略（leak policy），类型为 `mpipe_base_queue_leak`。

<a id="r_a3123f736e185d05da78d53c67bec52b7"></a>

```c
atomic_t flushing
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[flushing](#a3123f736e185d05da78d53c67bec52b7)。

在 `PAUSED -> READY` 时置位：处理函数丢弃缓冲区而不再入队，从而使阻塞于 `k_msgq_put()` 的生产者解除阻塞。

## 28.2\_详细说明（Detailed Documentation）

<a id="a3123f736e185d05da78d53c67bec52b7"></a>

### `flushing`

```c
atomic_t mpipe_queue::flushing
```

在 `PAUSED -> READY` 时置位：处理函数丢弃缓冲区而不再入队，从而使阻塞于 `k_msgq_put()` 的生产者解除阻塞。

<a id="a9950b600a3803eae60e93b28b4ca3986"></a>

### `leak`

```c
uint8_t mpipe_queue::leak
```

队列已满时的丢弃策略（leak policy），类型为 `mpipe_base_queue_leak`。

<a id="a36ee4b88ec2fc501f98e72985ea651a8"></a>

### `msgq`

```c
struct k_msgq mpipe_queue::msgq
```

缓冲区指针队列。

采用 `k_msgq` 而非 `k_fifo`，这样同一个缓冲区可以在分流元素（tee）之后，同时等待于多个队列中。

<a id="aa392264ebe9576abecce5ec3c91daaa7"></a>

### `msgq_buffer`

```c
char mpipe_queue::msgq_buffer[(CONFIG_MPIPE_BASE_QUEUE_MAX_SIZE+2) *sizeof(void *)]
```

消息队列的后备存储空间，大小可容纳最大队列以及 EOS 和暂停哨兵（pause sentinel）。

<a id="a4f0676f92ac9a2057af2eca5fd577640"></a>

### `size`

```c
uint8_t mpipe_queue::size
```

队列可容纳的缓冲区数量，受 `CONFIG_MPIPE_BASE_QUEUE_MAX_SIZE` 限制，并在 `READY -> PAUSED` 时应用。

<a id="a64f81e4ac2cb75cdb4d1a45920211daa"></a>

### `thread`

```c
struct mpipe_thread mpipe_queue::thread
```

专门执行下游处理的线程。

<a id="a7372d2798449c6d49aae12781ae0ac2a"></a>

### `transform`

```c
struct mpipe_transform mpipe_queue::transform
```

基础变换元素（base transform element）。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/base/mpipe_queue.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/base/mpipe_queue.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__queue_8h_source.html)
- [mpipe_transform](P034_mpipe_transform_结构体.md)
- [mpipe_thread](P033_mpipe_thread_结构体.md)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [CONFIG_MPIPE_BASE_QUEUE_MAX_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_BASE_QUEUE_MAX_SIZE)
- [mpipe_base_queue_leak](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ga627fd88220a8b0b06c46aa18fe7d8a84)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [k_msgq_put()](../msgstack_reference/P001_消息队列公共接口.md#ga54e96aaaea5462a1f963b7fd5ca82bfe)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_mpipe_player_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_mpipe_sink_结构体.md)
