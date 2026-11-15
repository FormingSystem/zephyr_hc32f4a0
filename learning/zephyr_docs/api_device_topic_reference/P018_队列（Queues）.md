---
id: learning.zephyr-docs.api-device-topic-reference.page-18
title: 队列（Queues）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_队列（Queues）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

管线层面的线程化元素。

<a id="details"></a>

管线层面的线程化元素。

<a id="header-files"></a>
<a id="files"></a>

## 18.1\_文件（Files）

<a id="r_mpipe_5Fqueue_2Eh"></a>

```c
file mpipe_queue.h
```

相关声明：[mpipe_queue.h](../api_file_service_reference/P026_zephyr__mpipe__base__mpipe_queue.h_文件参考.md)。

用于流水线级线程化（Pipeline-Level Threading）的队列元素。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fqueue"></a>

```c
struct mpipe_queue
```

相关声明：[mpipe_queue](../audio_video_model_reference/P028_mpipe_queue_结构体.md)。

队列元素（Queue Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 18.3\_枚举（Enumerations）

<a id="r_gae0389e724fcbb0a41198c2902aa5ead7"></a>

```c
enum { MPIPE_PROP_BASE_QUEUE_SIZE = MPIPE_PROP_TRANSFORM_LAST , MPIPE_PROP_BASE_QUEUE_THREAD_PRIORITY , MPIPE_PROP_BASE_QUEUE_LEAK }
```

相关声明：[MPIPE_PROP_BASE_QUEUE_SIZE](#ggae0389e724fcbb0a41198c2902aa5ead7a72375bea91fdf95aeb286bae43415f1c)、[MPIPE_PROP_BASE_QUEUE_THREAD_PRIORITY](#ggae0389e724fcbb0a41198c2902aa5ead7ad9b653b67bd3bda3b56276d918943db6)、[MPIPE_PROP_BASE_QUEUE_LEAK](#ggae0389e724fcbb0a41198c2902aa5ead7a17fb9e12018fca8d667b5771dda465f7)。

队列属性标识（Queue Property Identifiers）。

<a id="r_ga627fd88220a8b0b06c46aa18fe7d8a84"></a>

```c
enum mpipe_base_queue_leak { MPIPE_BASE_QUEUE_LEAK_NONE = 0 , MPIPE_BASE_QUEUE_LEAK_OLDEST , MPIPE_BASE_QUEUE_LEAK_NEWEST }
```

相关声明：[mpipe_base_queue_leak](#ga627fd88220a8b0b06c46aa18fe7d8a84)、[MPIPE_BASE_QUEUE_LEAK_NONE](#gga627fd88220a8b0b06c46aa18fe7d8a84a473301fa176adda9141acdcedc7b70de)、[MPIPE_BASE_QUEUE_LEAK_OLDEST](#gga627fd88220a8b0b06c46aa18fe7d8a84a50ac5619e65c3ec7d29ec0abd9bf5cb6)、[MPIPE_BASE_QUEUE_LEAK_NEWEST](#gga627fd88220a8b0b06c46aa18fe7d8a84aff5e4f0a9919568a53d442b45d274ecf)。

队列已满（Full Queue）时对新缓冲区（New Buffer）的处理方式。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.4\_函数（Functions）

<a id="r_ga6cade533253c3f6d31aaede6bfe5e152"></a>

```c
int mpipe_queue_init (struct mpipe_queue *queue, uint8_t id)
```

相关声明：[mpipe_queue_init](#ga6cade533253c3f6d31aaede6bfe5e152)、[mpipe_queue](../audio_video_model_reference/P028_mpipe_queue_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化队列元素（Queue Element）。

## 18.5\_详细说明（Detailed Documentation）

<a id="gae0389e724fcbb0a41198c2902aa5ead7"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/mpipe/base/mpipe_queue.h>
```

队列属性标识（Queue Property Identifiers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PROP_BASE_QUEUE_SIZE` | 队列能够容纳的缓冲区数量。 |
| `MPIPE_PROP_BASE_QUEUE_THREAD_PRIORITY` | 队列线程的调度优先级（scheduling priority）。 |
| `MPIPE_PROP_BASE_QUEUE_LEAK` | 队列已满时如何处理新缓冲区，取值为 `mpipe_base_queue_leak`。 |

<a id="ga627fd88220a8b0b06c46aa18fe7d8a84"></a>

### `mpipe_base_queue_leak`

```c
enum mpipe_base_queue_leak
```

```c
#include <zephyr/mpipe/base/mpipe_queue.h>
```

队列已满（Full Queue）时对新缓冲区（New Buffer）的处理方式。

队列首先是一个不丢失数据的线程边界（thread boundary），因此默认情况下，队列满时会阻塞生产者，直到消费者释放一个槽位。实时源（live source）向较慢的分支供给数据时，可能更希望丢弃数据：丢弃策略（leak policy）限制的是延迟，而非阻塞生产者。流结束（end of stream）事件绝不会被丢弃。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_BASE_QUEUE_LEAK_NONE` | 阻塞生产者，直到有空闲槽位。 |
| `MPIPE_BASE_QUEUE_LEAK_OLDEST` | 丢弃队列中最早的缓冲区，使消费者始终获取最新数据。 |
| `MPIPE_BASE_QUEUE_LEAK_NEWEST` | 丢弃新到达的缓冲区，使队列中已有缓冲区按顺序交付。 |

<a id="ga6cade533253c3f6d31aaede6bfe5e152"></a>

### `mpipe_queue_init()`

```c
int mpipe_queue_init ( struct mpipe_queue * queue, uint8_t id )
```

```c
#include <zephyr/mpipe/base/mpipe_queue.h>
```

初始化队列元素（Queue Element）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `queue` | 指向待初始化元素（Element）的指针（Pointer）。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。


## 18.6\_原页交叉引用（Cross References）

- [mpipe_queue.h](../api_file_service_reference/P026_zephyr__mpipe__base__mpipe_queue.h_文件参考.md)
- [mpipe_queue](../audio_video_model_reference/P028_mpipe_queue_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae0389e724fcbb0a41198c2902aa5ead7a72375bea91fdf95aeb286bae43415f1c"></a>
<a id="ggae0389e724fcbb0a41198c2902aa5ead7ad9b653b67bd3bda3b56276d918943db6"></a>
<a id="ggae0389e724fcbb0a41198c2902aa5ead7a17fb9e12018fca8d667b5771dda465f7"></a>
<a id="gga627fd88220a8b0b06c46aa18fe7d8a84a473301fa176adda9141acdcedc7b70de"></a>
<a id="gga627fd88220a8b0b06c46aa18fe7d8a84a50ac5619e65c3ec7d29ec0abd9bf5cb6"></a>
<a id="gga627fd88220a8b0b06c46aa18fe7d8a84aff5e4f0a9919568a53d442b45d274ecf"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P017_内存管理（Memory Management）.md) · [返回大纲](大纲.md) · [下一章](P019_接收端（Sinks）.md)
