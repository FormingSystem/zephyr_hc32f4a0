---
id: learning.zephyr-docs.api-device-topic-reference.page-19
title: 接收端（Sinks）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_接收端（Sinks）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__sink.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消耗缓冲区并终结数据流的元素。

<a id="details"></a>

消费缓冲区并结束数据流的接收端元素（Sinks）。接收端只有一个接收连接端（sink pad），没有发送连接端（source pad）：数据在此离开处理图（graph），进入显示屏、文件或编解码器。它是两类协商的简单终点：对能力查询（capability query），返回自己支持且提议范围允许的第一个格式；对缓冲池查询（buffer pool query），提出自身所需条件，因为没有下游可先行询问。

接收端还负责报告流结束。具有多个接收端的处理图会为每个接收端产生一条流结束消息，管线（pipeline）将这些消息合并为应用程序最终看到的一条通知；参见管线（Pipelines）主题。

<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_mpipe_5Fsink_2Eh"></a>

```c
file mpipe_sink.h
```

相关声明：[mpipe_sink.h](../api_file_runtime_reference/P042_zephyr__mpipe__mpipe_sink.h_文件参考.md)。

接收端（Sink）：消耗缓冲区的元素。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 19.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fsink"></a>

```c
struct mpipe_sink
```

相关声明：[mpipe_sink](../audio_video_model_reference/P029_mpipe_sink_结构体.md)。

接收端元素（Sink Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 19.3\_枚举（Enumerations）

<a id="r_ga87a63291ab124bd59e51a57f64446d01"></a>

```c
enum mpipe_prop_sink { MPIPE_PROP_SINK_LAST }
```

相关声明：[mpipe_prop_sink](#ga87a63291ab124bd59e51a57f64446d01)、[MPIPE_PROP_SINK_LAST](#gga87a63291ab124bd59e51a57f64446d01a22461ad516155f1cbd0bf917d98cca6b)。

汇端元素属性（Sink Element Properties）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.4\_函数（Functions）

<a id="r_ga8c19ec865af49f6e320161582b2dd5ae"></a>

```c
int mpipe_sink_init (struct mpipe_sink *sink, uint8_t id)
```

相关声明：[mpipe_sink_init](#ga8c19ec865af49f6e320161582b2dd5ae)、[mpipe_sink](../audio_video_model_reference/P029_mpipe_sink_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化汇端元素（Sink Element）。

<a id="r_ga6461b51403968217a6bc568cbb990250"></a>

```c
int mpipe_sink_change_state (struct mpipe_element *self, enum mpipe_state_change transition)
```

相关声明：[mpipe_sink_change_state](#ga6461b51403968217a6bc568cbb990250)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)。

基础汇端元素（Base Sink Element）的状态切换函数（Change State Function）。

## 19.5\_详细说明（Detailed Documentation）

<a id="ga87a63291ab124bd59e51a57f64446d01"></a>

### `mpipe_prop_sink`

```c
enum mpipe_prop_sink
```

```c
#include <zephyr/mpipe/mpipe_sink.h>
```

汇端元素属性（Sink Element Properties）。

基础接收端（base sink）可配置属性的枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PROP_SINK_LAST` | 最后一个接收端属性的标记，用于验证／迭代。 |

<a id="ga6461b51403968217a6bc568cbb990250"></a>

### `mpipe_sink_change_state()`

```c
int mpipe_sink_change_state ( struct mpipe_element * self, enum mpipe_state_change transition )
```

```c
#include <zephyr/mpipe/mpipe_sink.h>
```

基础汇端元素（Base Sink Element）的状态切换函数（Change State Function）。

在从 `PAUSED` 转换到 `READY` 时，此函数将已协商的连接端能力（pad caps）重置为 `ANY`，使后续重新协商能够从头开始。重写 `change_state` 的派生接收端必须在调用链中调用此基类函数，才能继承该行为。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向元素（Elements）的指针。 |
| `transition` | 转换状态（transition state），参见 `mpipe_state_change`。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga8c19ec865af49f6e320161582b2dd5ae"></a>

### `mpipe_sink_init()`

```c
int mpipe_sink_init ( struct mpipe_sink * sink, uint8_t id )
```

```c
#include <zephyr/mpipe/mpipe_sink.h>
```

初始化汇端元素（Sink Element）。

初始化基础接收端元素结构体，设置接收连接端（sink pad），并配置查询和事件处理的默认回调。具体接收端在自身初始化函数中，首先使用相同的 `id` 调用此函数，然后按需重写相应部分。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sink` | 指向待初始化接收端（Sinks）的指针。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。


## 19.6\_原页交叉引用（Cross References）

- [mpipe_sink.h](../api_file_runtime_reference/P042_zephyr__mpipe__mpipe_sink.h_文件参考.md)
- [mpipe_sink](../audio_video_model_reference/P029_mpipe_sink_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [管线（Pipelines）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pipeline.html)
- [元素（Elements）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html)
- [接收端（Sinks）](P019_接收端（Sinks）.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga87a63291ab124bd59e51a57f64446d01a22461ad516155f1cbd0bf917d98cca6b"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_队列（Queues）.md) · [返回大纲](大纲.md) · [下一章](P020_卸载型网络设备（Offloaded Net Devices）.md)
