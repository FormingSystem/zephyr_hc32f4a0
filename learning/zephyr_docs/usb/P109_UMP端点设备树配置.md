---
id: learning.zephyr-docs.usb.api-109
title: UMP端点设备树配置
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structump__endpoint__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第109章\_UMP端点设备树配置

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structump__endpoint__dt__spec.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 109.1\_阅读说明与来源

译注：本页说明UMP流响应器、配置对象或其实现依据。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

> 译注（路径修正）：原网页把文档构建服务器的绝对目录写入头文件包含展示。本译文统一使用 `#include "ump_stream_responder.h"`；文件位于官方源码树的 `lib/midi2/`。启用 `CONFIG_MIDI2_UMP_STREAM_RESPONDER` 后，该目录由对应CMake文件加入包含搜索路径。

UMP 端点配置描述（Endpoint Specification）。

```c
#include "ump_stream_responder.h"
```

UMP 端点配置描述（Endpoint Specification）。

## 109.2\_数据成员（Data Fields）

<a id="r_afdb120b1f342c1e078ef30ccabcfd0a0"></a>

```c
const char * name
```

此端点的名称；未命名时为 NULL。

相关声明：[name](P109_UMP端点设备树配置.md#afdb120b1f342c1e078ef30ccabcfd0a0)。

<a id="r_ab7ca8d380d52b184db8bddcc59516f7e"></a>

```c
size_t n_blocks
```

此端点中的功能块数量。

相关声明：[n_blocks](P109_UMP端点设备树配置.md#ab7ca8d380d52b184db8bddcc59516f7e)。

<a id="r_ae446e4a4778b2c89de2120d935068c03"></a>

```c
struct ump_block_dt_spec blocks []
```

此端点中的功能块。

相关声明：[ump_block_dt_spec](P114_UMP功能块设备树配置.md)、[blocks](P109_UMP端点设备树配置.md#ae446e4a4778b2c89de2120d935068c03)。

## 109.3\_详细说明（Detailed Documentation）

<a id="ae446e4a4778b2c89de2120d935068c03"></a>

### 109.3.1\_`blocks`

```c
struct ump_block_dt_spec ump_endpoint_dt_spec::blocks[]
```

此端点中的功能块。

> 译注（源码核对）：这是柔性数组成员（Flexible Array Member），不是指向独立数组的指针；手工分配此对象时须为n_blocks个元素预留实际存储。官方宏以初始化器生成相应静态描述。

<a id="ab7ca8d380d52b184db8bddcc59516f7e"></a>

### 109.3.2\_`n\_blocks`

```c
size_t ump_endpoint_dt_spec::n_blocks
```

此端点中的功能块数量。

<a id="afdb120b1f342c1e078ef30ccabcfd0a0"></a>

### 109.3.3\_`name`

```c
const char* ump_endpoint_dt_spec::name
```

此端点的名称；未命名时为 NULL。

> 译注（源码核对）：名称指针可以为NULL。当前发现响应器只在名称非NULL且过滤位请求名称时进入发送；空字符串会产生0个字符串数据包。

结构定义源文件：`lib/midi2/ump_stream_responder.h`。原网页附带的构建目录前缀已移除。

## 109.4\_源码跟踪与使用边界

译注依据保存的[官方响应器头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.h)、[实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.c)、[CMake入口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/CMakeLists.txt)和[Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/Kconfig)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../lib/midi2/ump_stream_responder.h)与[实现](../../../lib/midi2/ump_stream_responder.c)可用于源码跟踪，版本可能与网页不同；本批未构建或执行MIDI硬件验证。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P108_UMP流响应器API.md) · [返回大纲](大纲.md) · [下一章](P110_UMP流响应器配置.md)
