---
id: learning.zephyr-docs.usb.api-107
title: UMP功能块发现过滤位
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__fb__disc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第107章\_UMP功能块发现过滤位

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__fb__disc.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 107.1\_阅读说明与来源

译注：本页说明MIDI通用数据包的消息类型、命令或流消息字段。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.1.7 节图 21：功能块发现过滤位图字段格式。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

备注：当 UMP_MT(x)=UMP_MT_UMP_STREAM 且 UMP_STREAM_STATUS(x)=UMP_STREAM_STATUS_FB_DISCOVERY 时，UMP_STREAM_FB_DISCOVERY_FILTER(x) 可以是下列值按位或（Bitwise OR）的组合。

相关声明：[UMP_MT(x)](P098_通用MIDI数据包定义.md#gafab438886f69fb74a6e058f9343867aa)、[UMP_STREAM_STATUS(x)](P103_UMP流消息字段.md#ga27ee62e9a2c2f6e23de61d8f5c42c0a8)、[UMP_STREAM_FB_DISCOVERY_FILTER(x)](P103_UMP流消息字段.md#gac7134040f1026e2c4ee20286100b1312)。

## 107.2\_宏定义（Macros）

<a id="r_gaf0bc0e4083f74cfea57a0c52f7b5b1f6"></a>

```c
#define UMP_FB_DISC_FILTER_INFO BIT(0)
```

请求功能块信息通知（Function Block Info Notification）。

相关声明：[UMP_FB_DISC_FILTER_INFO](P107_UMP功能块发现过滤位.md#gaf0bc0e4083f74cfea57a0c52f7b5b1f6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga3552456370892c941d2c76f7029e0306"></a>

```c
#define UMP_FB_DISC_FILTER_NAME BIT(1)
```

请求功能块名称通知（Function Block Name Notification）。

相关声明：[UMP_FB_DISC_FILTER_NAME](P107_UMP功能块发现过滤位.md#ga3552456370892c941d2c76f7029e0306)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

## 107.3\_详细说明（Detailed Documentation）

<a id="gaf0bc0e4083f74cfea57a0c52f7b5b1f6"></a>

### 107.3.1\_`UMP\_FB\_DISC\_FILTER\_INFO`

```c
#define UMP_FB_DISC_FILTER_INFO BIT(0)
```

```c
#include <zephyr/audio/midi.h>
```

请求功能块信息通知（Function Block Info Notification）。

> 译注（源码核对）：过滤位和功能块编号分别由两个宏取得；将INFO与NAME按位或可同时请求两种通知，不会因此改变请求中的功能块编号。

<a id="ga3552456370892c941d2c76f7029e0306"></a>

### 107.3.2\_`UMP\_FB\_DISC\_FILTER\_NAME`

```c
#define UMP_FB_DISC_FILTER_NAME BIT(1)
```

```c
#include <zephyr/audio/midi.h>
```

请求功能块名称通知（Function Block Name Notification）。

## 107.4\_源码跟踪与使用边界

译注依据保存的[官方MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[对应头文件](../../../include/zephyr/audio/midi.h)可用于源码跟踪，版本可能与网页不同；原注释存在疑点时，在相应条目旁给出核对依据。本批未执行固件构建或MIDI硬件测试。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

[上一章](P106_UMP端点发现过滤位.md) · [返回大纲](大纲.md) · [下一章](P108_UMP流响应器API.md)
