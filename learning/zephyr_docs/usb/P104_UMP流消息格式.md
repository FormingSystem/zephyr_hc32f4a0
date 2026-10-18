---
id: learning.zephyr-docs.usb.api-104
title: UMP流消息格式
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__stream__format.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第104章\_UMP流消息格式

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__stream__format.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 104.1\_阅读说明与来源

译注：本页说明MIDI通用数据包的消息类型、命令或流消息字段。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.1 节“UMP 流消息”中的格式（Format）部分。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

备注：当 UMP_MT(x)=UMP_MT_UMP_STREAM 时，UMP_STREAM_FORMAT(x) 可以是下列值之一。

相关声明：[UMP_MT(x)](P098_通用MIDI数据包定义.md#gafab438886f69fb74a6e058f9343867aa)、[UMP_STREAM_FORMAT(x)](P103_UMP流消息字段.md#gaa964f1d5ebc6ffe3d360f9f4a303d0c7)。

## 104.2\_宏定义（Macros）

<a id="r_ga1437c75d99f58d138ea1ff04d5012b11"></a>

```c
#define UMP_STREAM_FORMAT_COMPLETE 0x00
```

一个 UMP 中包含完整消息（Complete Message）。

相关声明：[UMP_STREAM_FORMAT_COMPLETE](P104_UMP流消息格式.md#ga1437c75d99f58d138ea1ff04d5012b11)。

<a id="r_ga145b3798cf8ada61a57feb6489aaa3f0"></a>

```c
#define UMP_STREAM_FORMAT_START 0x01
```

跨两个或更多 UMP 的消息的起始部分（Start）。

相关声明：[UMP_STREAM_FORMAT_START](P104_UMP流消息格式.md#ga145b3798cf8ada61a57feb6489aaa3f0)。

<a id="r_ga8e84c4586cd1dcb5b0749669508608fd"></a>

```c
#define UMP_STREAM_FORMAT_CONTINUE 0x02
```

跨三个或更多 UMP 的消息的连续部分（Continue）。

相关声明：[UMP_STREAM_FORMAT_CONTINUE](P104_UMP流消息格式.md#ga8e84c4586cd1dcb5b0749669508608fd)。

<a id="r_gaf975fd5766fbddd0a3f1113c1d5c2fb1"></a>

```c
#define UMP_STREAM_FORMAT_END 0x03
```

跨两个或更多 UMP 的消息的结束部分（End）。

相关声明：[UMP_STREAM_FORMAT_END](P104_UMP流消息格式.md#gaf975fd5766fbddd0a3f1113c1d5c2fb1)。

## 104.3\_详细说明（Detailed Documentation）

<a id="ga1437c75d99f58d138ea1ff04d5012b11"></a>

### 104.3.1\_`UMP\_STREAM\_FORMAT\_COMPLETE`

```c
#define UMP_STREAM_FORMAT_COMPLETE 0x00
```

```c
#include <zephyr/audio/midi.h>
```

一个 UMP 中包含完整消息（Complete Message）。

<a id="ga8e84c4586cd1dcb5b0749669508608fd"></a>

### 104.3.2\_`UMP\_STREAM\_FORMAT\_CONTINUE`

```c
#define UMP_STREAM_FORMAT_CONTINUE 0x02
```

```c
#include <zephyr/audio/midi.h>
```

跨三个或更多 UMP 的消息的连续部分（Continue）。

一条消息可以包含多个 Continue UMP。

> 译注（源码核对）：Continue只描述跨多个UMP的逻辑消息片段；宏常量不会自动拼接片段，接收方仍须按对应消息类型处理起始、连续和结束。

<a id="gaf975fd5766fbddd0a3f1113c1d5c2fb1"></a>

### 104.3.3\_`UMP\_STREAM\_FORMAT\_END`

```c
#define UMP_STREAM_FORMAT_END 0x03
```

```c
#include <zephyr/audio/midi.h>
```

跨两个或更多 UMP 的消息的结束部分（End）。

<a id="ga145b3798cf8ada61a57feb6489aaa3f0"></a>

### 104.3.4\_`UMP\_STREAM\_FORMAT\_START`

```c
#define UMP_STREAM_FORMAT_START 0x01
```

```c
#include <zephyr/audio/midi.h>
```

跨两个或更多 UMP 的消息的起始部分（Start）。

## 104.4\_源码跟踪与使用边界

译注依据保存的[官方MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[对应头文件](../../../include/zephyr/audio/midi.h)可用于源码跟踪，版本可能与网页不同；原注释存在疑点时，在相应条目旁给出核对依据。本批未执行固件构建或MIDI硬件测试。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

[上一章](P103_UMP流消息字段.md) · [返回大纲](大纲.md) · [下一章](P105_UMP流消息状态.md)
