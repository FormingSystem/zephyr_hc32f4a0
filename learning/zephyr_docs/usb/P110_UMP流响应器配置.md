---
id: learning.zephyr-docs.usb.api-110
title: UMP流响应器配置
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structump__stream__responder__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第110章\_UMP流响应器配置

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structump__stream__responder__cfg.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 110.1\_阅读说明与来源

译注：本页说明UMP流响应器、配置对象或其实现依据。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

> 译注（路径修正）：原网页把文档构建服务器的绝对目录写入头文件包含展示。本译文统一使用 `#include "ump_stream_responder.h"`；文件位于官方源码树的 `lib/midi2/`。启用 `CONFIG_MIDI2_UMP_STREAM_RESPONDER` 后，该目录由对应CMake文件加入包含搜索路径。

UMP 流响应器（UMP Stream Responder）的配置。

```c
#include "ump_stream_responder.h"
```

UMP 流响应器（UMP Stream Responder）的配置。

## 110.2\_数据成员（Data Fields）

<a id="r_a9107c4a2926092a52ea4616f505013ec"></a>

```c
const void * dev
```

用于发送回复数据包的设备。

相关声明：[dev](P110_UMP流响应器配置.md#a9107c4a2926092a52ea4616f505013ec)。

<a id="r_aa1f59013c817617d0ed3cf4b34d92fb6"></a>

```c
ump_send_func send
```

发送回复数据包时调用的函数。

相关声明：[ump_send_func](P108_UMP流响应器API.md#ga2eb945a1c7ab32ffe8a88cb8389ecee2)、[send](P110_UMP流响应器配置.md#aa1f59013c817617d0ed3cf4b34d92fb6)。

<a id="r_afb02b5ac03c76a9d4af2513a99c11903"></a>

```c
const struct ump_endpoint_dt_spec * ep_spec
```

UMP 端点配置描述。

相关声明：[ump_endpoint_dt_spec](P109_UMP端点设备树配置.md)、[ep_spec](P110_UMP流响应器配置.md#afb02b5ac03c76a9d4af2513a99c11903)。

## 110.3\_详细说明（Detailed Documentation）

<a id="a9107c4a2926092a52ea4616f505013ec"></a>

### 110.3.1\_`dev`

```c
const void* ump_stream_responder_cfg::dev
```

用于发送回复数据包的设备。

<a id="afb02b5ac03c76a9d4af2513a99c11903"></a>

### 110.3.2\_`ep\_spec`

```c
const struct ump_endpoint_dt_spec* ump_stream_responder_cfg::ep_spec
```

UMP 端点配置描述。

> 译注（源码核对）：保存配置指针，不复制端点、名称及功能块数组，引用对象必须在响应期间保持有效。

<a id="aa1f59013c817617d0ed3cf4b34d92fb6"></a>

### 110.3.3\_`send`

```c
ump_send_func ump_stream_responder_cfg::send
```

发送回复数据包时调用的函数。

> 译注（源码核对）：该回调返回void，响应器按调用次数计数；不能由响应器返回的正数推断USB发送队列未满或主机已经接收。

结构定义源文件：`lib/midi2/ump_stream_responder.h`。原网页附带的构建目录前缀已移除。

## 110.4\_源码跟踪与使用边界

译注依据保存的[官方响应器头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.h)、[实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/ump_stream_responder.c)、[CMake入口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/CMakeLists.txt)和[Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/lib/midi2/Kconfig)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../lib/midi2/ump_stream_responder.h)与[实现](../../../lib/midi2/ump_stream_responder.c)可用于源码跟踪，版本可能与网页不同；本批未构建或执行MIDI硬件验证。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P109_UMP端点设备树配置.md) · [返回大纲](大纲.md) · [下一章](P111_UMP流响应器头文件接口.md)
