---
id: learning.zephyr-docs.usb.api-114
title: UMP功能块设备树配置
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structump__block__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第114章\_UMP功能块设备树配置

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structump__block__dt__spec.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 114.1\_阅读说明与来源

译注：本页说明UMP流响应器、配置对象或其实现依据。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

> 译注（路径修正）：原网页把文档构建服务器的绝对目录写入头文件包含展示。本译文统一使用 `#include "ump_stream_responder.h"`；文件位于官方源码树的 `lib/midi2/`。启用 `CONFIG_MIDI2_UMP_STREAM_RESPONDER` 后，该目录由对应CMake文件加入包含搜索路径。

UMP 功能块配置描述（Function Block Specification）。

```c
#include "ump_stream_responder.h"
```

UMP 功能块配置描述（Function Block Specification）。

参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 6 节：功能块（Function Blocks）。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

## 114.2\_数据成员（Data Fields）

<a id="r_a081ed3cfda4c5ac6cb9c618acb20aeaf"></a>

```c
const char * name
```

此功能块的名称；未命名时为 NULL。

相关声明：[name](P114_UMP功能块设备树配置.md#a081ed3cfda4c5ac6cb9c618acb20aeaf)。

<a id="r_a43e7308ad22965d32b9ab174b09e9948"></a>

```c
uint8_t first_group
```

此块中第一个 UMP 组（Group）的编号。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[first_group](P114_UMP功能块设备树配置.md#a43e7308ad22965d32b9ab174b09e9948)。

<a id="r_ad090f11096cbd142d12f53374aec5abc"></a>

```c
uint8_t groups_spanned
```

此块跨越的连续 UMP 组的数量。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[groups_spanned](P114_UMP功能块设备树配置.md#ad090f11096cbd142d12f53374aec5abc)。

<a id="r_a3ecdc37b74894cf05909e6a61b74c28f"></a>

```c
bool is_input
```

此功能块是输入时为 true。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_input](P114_UMP功能块设备树配置.md#a3ecdc37b74894cf05909e6a61b74c28f)。

<a id="r_a94d49a45f045e4263c20f8d1af07b562"></a>

```c
bool is_output
```

此功能块是输出时为 true。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_output](P114_UMP功能块设备树配置.md#a94d49a45f045e4263c20f8d1af07b562)。

<a id="r_a09299c0d4979a0d77e951511f89f4783"></a>

```c
bool is_midi1
```

此功能块仅承载 MIDI1 数据时为 true。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_midi1](P114_UMP功能块设备树配置.md#a09299c0d4979a0d77e951511f89f4783)。

<a id="r_aa9238db0496387de9459c1862e239ae5"></a>

```c
bool is_31250bps
```

此功能块通过物理连线接至 MIDI1 串行接口，且该接口以标准 31250 b/s 速率传输数据时为 true。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_31250bps](P114_UMP功能块设备树配置.md#aa9238db0496387de9459c1862e239ae5)。

## 114.3\_详细说明（Detailed Documentation）

<a id="a43e7308ad22965d32b9ab174b09e9948"></a>

### 114.3.1\_`first\_group`

```c
uint8_t ump_block_dt_spec::first_group
```

此块中第一个 UMP 组（Group）的编号。

> 译注（源码核对）：表示此功能块覆盖的第一个UMP组号，不是功能块数组索引。

<a id="ad090f11096cbd142d12f53374aec5abc"></a>

### 114.3.2\_`groups\_spanned`

```c
uint8_t ump_block_dt_spec::groups_spanned
```

此块跨越的连续 UMP 组的数量。

> 译注（源码核对）：表示从first_group起连续覆盖的组数量。结构体只保存数值，手工构造时需保证范围有效，不能把该字段看作最后一个组号。

<a id="aa9238db0496387de9459c1862e239ae5"></a>

### 114.3.3\_`is\_31250bps`

```c
bool ump_block_dt_spec::is_31250bps
```

此功能块通过物理连线接至 MIDI1 串行接口，且该接口以标准 31250 b/s 速率传输数据时为 true。

> 译注（源码核对）：这是功能块物理串行传输特性的元数据，设置为真不会自动配置UART波特率或建立线路。

<a id="a3ecdc37b74894cf05909e6a61b74c28f"></a>

### 114.3.4\_`is\_input`

```c
bool ump_block_dt_spec::is_input
```

此功能块是输入时为 true。

> 译注（源码核对）：宏对非output-only块设置此标志，并在功能块信息通知中给出Receiver提示；双向块可同时设置is_input和is_output。

<a id="a09299c0d4979a0d77e951511f89f4783"></a>

### 114.3.5\_`is\_midi1`

```c
bool ump_block_dt_spec::is_midi1
```

此功能块仅承载 MIDI1 数据时为 true。

<a id="a94d49a45f045e4263c20f8d1af07b562"></a>

### 114.3.6\_`is\_output`

```c
bool ump_block_dt_spec::is_output
```

此功能块是输出时为 true。

> 译注（源码核对）：宏对非input-only块设置此标志，并在通知中给出Sender提示。方向描述功能块，不应直接等同于USB端点地址的方向位。

<a id="a081ed3cfda4c5ac6cb9c618acb20aeaf"></a>

### 114.3.7\_`name`

```c
const char* ump_block_dt_spec::name
```

此功能块的名称；未命名时为 NULL。

结构定义源文件：`lib/midi2/ump_stream_responder.h`。原网页附带的构建目录前缀已移除。

## 114.4\_源码跟踪与使用边界

译注依据保存的[官方响应器头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.h)、[实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.c)、[CMake入口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/CMakeLists.txt)和[Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/Kconfig)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../lib/midi2/ump_stream_responder.h)与[实现](../../../lib/midi2/ump_stream_responder.c)可用于源码跟踪，版本可能与网页不同；本批未构建或执行MIDI硬件验证。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P113_UMP格式与MIDI协议依据.md) · [返回大纲](大纲.md) · [下一章](P115_USB音频设备绑定.md)
