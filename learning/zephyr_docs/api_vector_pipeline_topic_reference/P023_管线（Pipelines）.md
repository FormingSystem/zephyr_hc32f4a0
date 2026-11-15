---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-23
title: 管线（Pipelines）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_管线（Pipelines）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

顶层容器，以及实际运行处理图的对象。

<a id="details"></a>

顶层容器（Top-level Bin），也是实际运行处理图（Graph）的对象。流水线（Pipeline）是最外层的 Bins，因此承担内部容器所没有的三项职责。

它拥有运行处理图的线程：状态变化负责创建、暂停、恢复及等待该线程结束（Join）；线程中的循环从源（Source）获取缓冲区，依次通过各元素的处理函数推送，直到接收端（Sink）消费缓冲区。队列元素（Queue Element）可为图中的一部分提供独立线程。

它安排拆卸（Teardown）顺序：在子元素拆除缓冲池前，先丢弃仍在传递中的缓冲区；只有在子元素排空后，才等待线程结束。暂停不等于拆卸，因此排队内容得以保留，恢复时可以无损继续。

它还汇总流结束（End of Stream）事件：具有多个接收端的图会由每个接收端各产生一条流结束消息，只有最后一条才会到达应用程序。

<a id="header-files"></a>
<a id="files"></a>

## 23.1\_文件（Files）

<a id="r_mpipe_5Fpipeline_2Eh"></a>

```c
file mpipe_pipeline.h
```

相关声明：[mpipe_pipeline.h](../api_file_runtime_reference/P041_zephyr__mpipe__mpipe_pipeline.h_文件参考.md)。

流水线（Pipeline）：运行处理图的顶层容器（Bin）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 23.2\_数据结构（Data Structures）

<a id="r_mpipe"></a>

```c
struct mpipe
```

相关声明：[mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)。

流水线（Pipeline）：运行处理图（Graph）的顶层容器（Bin）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 23.3\_枚举（Enumerations）

<a id="r_ga07a22fd0fa0ac67b938fd4a93b16f88d"></a>

```c
enum mpipe_prop_pipeline { MPIPE_PROP_PIPELINE_THREAD_PRIORITY }
```

相关声明：[mpipe_prop_pipeline](#ga07a22fd0fa0ac67b938fd4a93b16f88d)、[MPIPE_PROP_PIPELINE_THREAD_PRIORITY](#gga07a22fd0fa0ac67b938fd4a93b16f88da8f6877c09918e33c18f422d17d657606)。

流水线属性（Pipeline Properties）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.4\_函数（Functions）

<a id="r_ga86fe870690248ee26e9c7894773cc928"></a>

```c
int mpipe_pipeline_init (struct mpipe *pipe, uint8_t id)
```

相关声明：[mpipe_pipeline_init](#ga86fe870690248ee26e9c7894773cc928)、[mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化流水线（Pipeline）。

<a id="r_ga4d4ef57dabea505630b4503ee25ec40a"></a>

```c
int mpipe_push_buffer (struct mpipe_pad *src_pad, struct net_buf *buffer)
```

相关声明：[mpipe_push_buffer](#ga4d4ef57dabea505630b4503ee25ec40a)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从给定的源端垫端（Source Pad）开始，向下游推送缓冲区（Buffer）。

## 23.5\_详细说明（Detailed Documentation）

<a id="ga07a22fd0fa0ac67b938fd4a93b16f88d"></a>

### `mpipe_prop_pipeline`

```c
enum mpipe_prop_pipeline
```

```c
#include <zephyr/mpipe/mpipe_pipeline.h>
```

流水线属性（Pipeline Properties）。

可为流水线（Pipeline）配置的属性枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PROP_PIPELINE_THREAD_PRIORITY` | 创建流水线线程时使用的线程调度优先级（Thread Scheduling Priority），默认值为 `CONFIG_MPIPE_THREAD_DEFAULT_PRIORITY`。 |

<a id="ga86fe870690248ee26e9c7894773cc928"></a>

### `mpipe_pipeline_init()`

```c
int mpipe_pipeline_init ( struct mpipe * pipe, uint8_t id )
```

```c
#include <zephyr/mpipe/mpipe_pipeline.h>
```

初始化流水线（Pipeline）。

初始化流水线结构体，包括基础容器（Base Bin）及其消息通道（Message Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pipe` | 指向待初始化的多媒体流水线（Multimedia Pipeline）的指针。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga4d4ef57dabea505630b4503ee25ec40a"></a>

### `mpipe_push_buffer()`

```c
int mpipe_push_buffer ( struct mpipe_pad * src_pad, struct net_buf * buffer )
```

```c
#include <zephyr/mpipe/mpipe_pipeline.h>
```

从给定的源端垫端（Source Pad）开始，向下游推送缓冲区（Buffer）。

从元素的 `src_pad` 向下游遍历，调用后续各元素的 `process_fn`，直到到达接收端（Sink）、某个 `process_fn` 失败，或输出缓冲区为 `NULL`。

处理函数（Processing Function）拥有交给它的缓冲区，无论成功还是失败都会释放，因此遍历过程不会在处理错误时再次释放。只有在未到达任何处理函数的两种情况下，遍历过程才自行释放缓冲区：源焊盘（Source Pad）没有对端，或对端焊盘处于冲刷（Flushing）状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src_pad` | 开始推送的源焊盘（Source Pad），首先调用其对端的 `process_fn`。 |
| `buffer` | 要推送的缓冲区，其所有权（Ownership）随调用转移。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。


## 23.6\_原页交叉引用（Cross References）

- [mpipe_pipeline.h](../api_file_runtime_reference/P041_zephyr__mpipe__mpipe_pipeline.h_文件参考.md)
- [mpipe](../audio_video_model_reference/P011_mpipe_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [容器（Bins）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html)
- [CONFIG_MPIPE_THREAD_DEFAULT_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_THREAD_DEFAULT_PRIORITY)
- [多媒体管线（Multimedia Pipeline）](../api_platform_topic_reference/P061_多媒体管线（Multimedia Pipeline）.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga07a22fd0fa0ac67b938fd4a93b16f88da8f6877c09918e33c18f422d17d657606"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P022_拓扑转储（Topology dump）.md) · [返回大纲](大纲.md) · [下一章](P024_网络核心库（Network Core Library）.md)
