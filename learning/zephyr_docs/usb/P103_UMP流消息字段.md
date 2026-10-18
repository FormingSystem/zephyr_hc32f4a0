---
id: learning.zephyr-docs.usb.api-103
title: UMP流消息字段
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__stream.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第103章\_UMP流消息字段

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__stream.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 103.1\_阅读说明与来源

译注：本页说明MIDI通用数据包的消息类型、命令或流消息字段。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.1 节：UMP 流消息。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

## 103.2\_主题（Topics）

<a id="r_midi_5Fump_5Ffb_5Fdisc"></a>

UMP流功能块发现消息过滤位（UMP Stream Function Block discovery message filter bits）。



相关声明：[UMP Stream Function Block discovery message filter bits](P107_UMP功能块发现过滤位.md)。

<a id="r_midi_5Fump_5Fep_5Fdisc"></a>

UMP流端点发现消息过滤位（UMP Stream endpoint discovery message filter bits）。



相关声明：[UMP Stream endpoint discovery message filter bits](P106_UMP端点发现过滤位.md)。

<a id="r_midi_5Fump_5Fstream_5Fformat"></a>

UMP流格式（UMP Stream format）。



相关声明：[UMP Stream format](P104_UMP流消息格式.md)。

<a id="r_midi_5Fump_5Fstream_5Fstatus"></a>

UMP流状态（UMP Stream status）。



相关声明：[UMP Stream status](P105_UMP流消息状态.md)。

## 103.3\_宏定义（Macros）

<a id="r_gaa964f1d5ebc6ffe3d360f9f4a303d0c7"></a>

```c
#define UMP_STREAM_FORMAT(ump)
```

UMP 流消息的格式（Format）。

相关声明：[UMP_STREAM_FORMAT](P103_UMP流消息字段.md#gaa964f1d5ebc6ffe3d360f9f4a303d0c7)。

<a id="r_ga27ee62e9a2c2f6e23de61d8f5c42c0a8"></a>

```c
#define UMP_STREAM_STATUS(ump)
```

UMP 流消息的状态（Status）字段。

相关声明：[UMP_STREAM_STATUS](P103_UMP流消息字段.md#ga27ee62e9a2c2f6e23de61d8f5c42c0a8)。

<a id="r_gacbefffaacf70b546d5b7055bcefe7f16"></a>

```c
#define UMP_STREAM_EP_DISCOVERY_FILTER(ump)
```

端点发现（Endpoint Discovery）消息的过滤位图（Filter Bitmap）。

相关声明：[UMP_STREAM_EP_DISCOVERY_FILTER](P103_UMP流消息字段.md#gacbefffaacf70b546d5b7055bcefe7f16)。

<a id="r_gac7134040f1026e2c4ee20286100b1312"></a>

```c
#define UMP_STREAM_FB_DISCOVERY_FILTER(ump)
```

功能块发现（Function Block Discovery）消息的过滤位图。

相关声明：[UMP_STREAM_FB_DISCOVERY_FILTER](P103_UMP流消息字段.md#gac7134040f1026e2c4ee20286100b1312)。

<a id="r_ga7a6a56afd9298976899b0b2100b79223"></a>

```c
#define UMP_STREAM_FB_DISCOVERY_NUM(ump)
```

功能块发现消息请求的块编号（Block Number）。

相关声明：[UMP_STREAM_FB_DISCOVERY_NUM](P103_UMP流消息字段.md#ga7a6a56afd9298976899b0b2100b79223)。

## 103.4\_详细说明（Detailed Documentation）

<a id="gacbefffaacf70b546d5b7055bcefe7f16"></a>

### 103.4.1\_`UMP\_STREAM\_EP\_DISCOVERY\_FILTER`

```c
#define UMP_STREAM_EP_DISCOVERY_FILTER ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
((ump).data[1] & 0xFF)
```

端点发现（Endpoint Discovery）消息的过滤位图（Filter Bitmap）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包（Universal MIDI Packet），包含端点发现消息。 |

**参阅（See Also）**：参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.1.1 节“端点发现消息”，以及 UMP 流端点发现消息过滤位。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)、[UMP Stream endpoint discovery message filter bits](P106_UMP端点发现过滤位.md)。

> 译注（源码核对）：读取data[1]的最低8位；功能块发现过滤宏读取的是data[0]的最低8位，两种消息的字段位置不同。调用前须确认UMP消息类型与流状态对应端点发现。

<a id="gac7134040f1026e2c4ee20286100b1312"></a>

### 103.4.2\_`UMP\_STREAM\_FB\_DISCOVERY\_FILTER`

```c
#define UMP_STREAM_FB_DISCOVERY_FILTER ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
((ump).data[0] & 0xFF)
```

功能块发现（Function Block Discovery）消息的过滤位图。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包，包含功能块发现消息。 |

**参阅（See Also）**：参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.1.7 节“功能块发现消息”，以及 UMP 流功能块发现消息过滤位。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)、[UMP Stream Function Block discovery message filter bits](P107_UMP功能块发现过滤位.md)。

> 译注（源码核对）：读取data[0]最低8位。返回的是过滤位图，不是单一枚举值；可按位组合多个已定义的请求位。

<a id="ga7a6a56afd9298976899b0b2100b79223"></a>

### 103.4.3\_`UMP\_STREAM\_FB\_DISCOVERY\_NUM`

```c
#define UMP_STREAM_FB_DISCOVERY_NUM ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
(((ump).data[0] >> 8) & 0xFF)
```

功能块发现消息请求的块编号（Block Number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包，包含功能块发现消息。 |

**参阅（See Also）**：参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.1.7 节：功能块发现消息。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

> 译注（源码核对）：读取data[0]的位15至8，和最低8位的功能块过滤位图区分。宏只做位提取，不验证消息类型，也不查找或创建功能块对象。

<a id="gaa964f1d5ebc6ffe3d360f9f4a303d0c7"></a>

### 103.4.4\_`UMP\_STREAM\_FORMAT`

```c
#define UMP_STREAM_FORMAT ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
(((ump).data[0] >> 26) & 0x03)
```

UMP 流消息的格式（Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包，包含 UMP 流消息。 |

**参阅（See Also）**：参阅 UMP 流格式（UMP Stream Format）。

相关声明：[UMP Stream format](P104_UMP流消息格式.md)。

> 译注（源码核对）：格式取自首字位27至26，共2位。普通组号提取宏使用首字位27至24，因此不能同时把这类UMP流消息解释为带普通Group字段的消息。

<a id="ga27ee62e9a2c2f6e23de61d8f5c42c0a8"></a>

### 103.4.5\_`UMP\_STREAM\_STATUS`

```c
#define UMP_STREAM_STATUS ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
(((ump).data[0] >> 16) & 0x3FF)
```

UMP 流消息的状态（Status）字段。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包，包含 UMP 流消息。 |

**参阅（See Also）**：参阅 UMP 流状态（UMP Stream Status）。

相关声明：[UMP Stream status](P105_UMP流消息状态.md)。

> 译注（源码核对）：状态取自首字位25至16，共10位；它与MIDI1的8位状态字节是不同字段。常量值相同也不能跨消息类型使用。

## 103.5\_源码跟踪与使用边界

译注依据保存的[官方MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[对应头文件](../../../include/zephyr/audio/midi.h)可用于源码跟踪，版本可能与网页不同；原注释存在疑点时，在相应条目旁给出核对依据。本批未执行固件构建或MIDI硬件测试。

<a id="header-groups"></a>
<a id="groups"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

[上一章](P102_MIDI系统消息状态.md) · [返回大纲](大纲.md) · [下一章](P104_UMP流消息格式.md)
