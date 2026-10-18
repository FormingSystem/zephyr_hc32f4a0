---
id: learning.zephyr-docs.api-protocol-topic-reference.page-35
title: 解析器（Parsers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_解析器（Parsers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__parser.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

将无固定结构的字节流切分为帧的元素。

<a id="details"></a>

将无帧结构的字节流切分为帧（frames）的元素。解析器（parser）位于数据流从字节转变为帧的位置：其输入来自文件或套接字，这些输入源无法说明其中承载的格式；其输出则是完整的帧，格式由解析器检查内容后确定。正是这种不对称性使解析器拥有独立的基类，而不是使用变换（transform）基类。它无法将输出反向映射到输入能力（capability），因此不实现跨连接端的能力映射（capability crossing），而只描述自己产生的内容。

由于上游元素不了解格式，从上游到达的格式事件（format event）实际上未声明任何有效格式。解析器在向下游传递之前，将其中的能力替换为自己确定的能力，从而使其成为真正的格式声明。解析器通常还需要比正在传输的数据流多一个缓冲区，用于保存仍在组装的帧。

<a id="header-files"></a>
<a id="files"></a>

## 35.1\_文件（Files）

<a id="r_mpipe_5Fparser_2Eh"></a>

```c
file mpipe_parser.h
```

相关声明：[mpipe_parser.h](../api_file_runtime_reference/P040_zephyr__mpipe__mpipe_parser.h_文件参考.md)。

流解析器基础元素（Stream Parser Base Element）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 35.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fparser"></a>

```c
struct mpipe_parser
```

相关声明：[mpipe_parser](../audio_video_model_reference/P026_mpipe_parser_结构体.md)。

基础解析器元素（Base Parser Element）的结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 35.3\_函数（Functions）

<a id="r_ga17fc0c53e8166bdde12176ee2ac7bdb1"></a>

```c
int mpipe_parser_init (struct mpipe_parser *parser, uint8_t id)
```

相关声明：[mpipe_parser_init](#ga17fc0c53e8166bdde12176ee2ac7bdb1)、[mpipe_parser](../audio_video_model_reference/P026_mpipe_parser_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化解析器元素（Parser Element）。

<a id="r_ga433bfb9df636fa51e737acc3ecc0b69f"></a>

```c
int mpipe_parser_change_state (struct mpipe_element *self, enum mpipe_state_change transition)
```

相关声明：[mpipe_parser_change_state](#ga433bfb9df636fa51e737acc3ecc0b69f)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)。

基础解析器元素（Base Parser Element）的状态切换函数（Change State Function）。

## 35.4\_详细说明（Detailed Documentation）

<a id="ga433bfb9df636fa51e737acc3ecc0b69f"></a>

### `mpipe_parser_change_state()`

```c
int mpipe_parser_change_state ( struct mpipe_element * self, enum mpipe_state_change transition )
```

```c
#include <zephyr/mpipe/mpipe_parser.h>
```

基础解析器元素（Base Parser Element）的状态切换函数（Change State Function）。

在从 `PAUSED` 转换到 `READY` 时，此函数会将已协商的连接端能力（pad caps）重置为 `ANY`，使后续重新协商能够从头开始。重写 `change_state` 的派生解析器必须在调用链中调用此基类函数，才能继承该行为。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向元素（Elements）的指针。 |
| `transition` | 转换状态（transition state），参见 `mpipe_state_change`。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga17fc0c53e8166bdde12176ee2ac7bdb1"></a>

### `mpipe_parser_init()`

```c
int mpipe_parser_init ( struct mpipe_parser * parser, uint8_t id )
```

```c
#include <zephyr/mpipe/mpipe_parser.h>
```

初始化解析器元素（Parser Element）。

初始化基础解析器元素结构体、其接收端（sink）和发送端（source）连接端以及默认回调。具体解析器在自身初始化函数中，首先使用相同的 `id` 调用此函数，然后按需重写相应部分。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `parser` | 指向待初始化解析器（Parsers）的指针。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。


## 35.5\_原页交叉引用（Cross References）

- [mpipe_parser.h](../api_file_runtime_reference/P040_zephyr__mpipe__mpipe_parser.h_文件参考.md)
- [mpipe_parser](../audio_video_model_reference/P026_mpipe_parser_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [元素（Elements）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html)
- [解析器（Parsers）](P035_解析器（Parsers）.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P034_分派（Dispatches）.md) · [返回大纲](大纲.md) · [下一章](P036_分流器（Tee）.md)
