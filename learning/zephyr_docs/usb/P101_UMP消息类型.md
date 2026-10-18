---
id: learning.zephyr-docs.usb.api-101
title: UMP消息类型
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__mt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第101章\_UMP消息类型

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__mt.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 101.1\_阅读说明与来源

译注：本页说明MIDI通用数据包的消息类型、命令或流消息字段。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 2.1.4 节：消息类型（Message Type，MT）分配。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

## 101.2\_宏定义（Macros）

<a id="r_ga6b9f0ce12bbdcb92fb4003ba9d5ed3e3"></a>

```c
#define UMP_MT_UTILITY 0x00
```

实用消息（Utility Messages）。

相关声明：[UMP_MT_UTILITY](P101_UMP消息类型.md#ga6b9f0ce12bbdcb92fb4003ba9d5ed3e3)。

<a id="r_gab8f194f60f1b5de7f050009275e44412"></a>

```c
#define UMP_MT_SYS_RT_COMMON 0x01
```

系统实时消息（System Real Time Messages）和系统公共消息（System Common Messages），不含系统专用消息（System Exclusive，SysEx）。

相关声明：[UMP_MT_SYS_RT_COMMON](P101_UMP消息类型.md#gab8f194f60f1b5de7f050009275e44412)。

<a id="r_gae086e5899933e436715ed2321607ef36"></a>

```c
#define UMP_MT_MIDI1_CHANNEL_VOICE 0x02
```

MIDI 1.0 通道语音消息（Channel Voice Messages）。

相关声明：[UMP_MT_MIDI1_CHANNEL_VOICE](P101_UMP消息类型.md#gae086e5899933e436715ed2321607ef36)。

<a id="r_ga235bf38958774c9ccc8864b98cff7ff9"></a>

```c
#define UMP_MT_DATA_64 0x03
```

64 位数据消息（Data Messages），包含系统专用消息（System Exclusive）。

相关声明：[UMP_MT_DATA_64](P101_UMP消息类型.md#ga235bf38958774c9ccc8864b98cff7ff9)。

<a id="r_ga9f2ac215138eb6e958df9558547f805a"></a>

```c
#define UMP_MT_MIDI2_CHANNEL_VOICE 0x04
```

MIDI 2.0 通道语音消息（Channel Voice Messages）。

相关声明：[UMP_MT_MIDI2_CHANNEL_VOICE](P101_UMP消息类型.md#ga9f2ac215138eb6e958df9558547f805a)。

<a id="r_gabe19506f8d84dbc84a46114768853d5b"></a>

```c
#define UMP_MT_DATA_128 0x05
```

128 位数据消息（Data Messages）。

相关声明：[UMP_MT_DATA_128](P101_UMP消息类型.md#gabe19506f8d84dbc84a46114768853d5b)。

<a id="r_ga916fba3c7a01dfff98f94c700a585fd5"></a>

```c
#define UMP_MT_FLEX_DATA 0x0d
```

灵活数据消息（Flex Data Messages）。

相关声明：[UMP_MT_FLEX_DATA](P101_UMP消息类型.md#ga916fba3c7a01dfff98f94c700a585fd5)。

<a id="r_gae14fb523ae456ca3e49a86de7d197e55"></a>

```c
#define UMP_MT_UMP_STREAM 0x0f
```

UMP 流消息（UMP Stream Message）。

相关声明：[UMP_MT_UMP_STREAM](P101_UMP消息类型.md#gae14fb523ae456ca3e49a86de7d197e55)。

## 101.3\_详细说明（Detailed Documentation）

<a id="gabe19506f8d84dbc84a46114768853d5b"></a>

### 101.3.1\_`UMP\_MT\_DATA\_128`

```c
#define UMP_MT_DATA_128 0x05
```

```c
#include <zephyr/audio/midi.h>
```

128 位数据消息（Data Messages）。

<a id="ga235bf38958774c9ccc8864b98cff7ff9"></a>

### 101.3.2\_`UMP\_MT\_DATA\_64`

```c
#define UMP_MT_DATA_64 0x03
```

```c
#include <zephyr/audio/midi.h>
```

64 位数据消息（Data Messages），包含系统专用消息（System Exclusive）。

<a id="ga916fba3c7a01dfff98f94c700a585fd5"></a>

### 101.3.3\_`UMP\_MT\_FLEX\_DATA`

```c
#define UMP_MT_FLEX_DATA 0x0d
```

```c
#include <zephyr/audio/midi.h>
```

灵活数据消息（Flex Data Messages）。

<a id="gae086e5899933e436715ed2321607ef36"></a>

### 101.3.4\_`UMP\_MT\_MIDI1\_CHANNEL\_VOICE`

```c
#define UMP_MT_MIDI1_CHANNEL_VOICE 0x02
```

```c
#include <zephyr/audio/midi.h>
```

MIDI 1.0 通道语音消息（Channel Voice Messages）。

<a id="ga9f2ac215138eb6e958df9558547f805a"></a>

### 101.3.5\_`UMP\_MT\_MIDI2\_CHANNEL\_VOICE`

```c
#define UMP_MT_MIDI2_CHANNEL_VOICE 0x04
```

```c
#include <zephyr/audio/midi.h>
```

MIDI 2.0 通道语音消息（Channel Voice Messages）。

<a id="gab8f194f60f1b5de7f050009275e44412"></a>

### 101.3.6\_`UMP\_MT\_SYS\_RT\_COMMON`

```c
#define UMP_MT_SYS_RT_COMMON 0x01
```

```c
#include <zephyr/audio/midi.h>
```

系统实时消息（System Real Time Messages）和系统公共消息（System Common Messages），不含系统专用消息（System Exclusive，SysEx）。

<a id="gae14fb523ae456ca3e49a86de7d197e55"></a>

### 101.3.7\_`UMP\_MT\_UMP\_STREAM`

```c
#define UMP_MT_UMP_STREAM 0x0f
```

```c
#include <zephyr/audio/midi.h>
```

UMP 流消息（UMP Stream Message）。

**参阅（See Also）**：参阅 UMP 流专用字段（UMP Stream Specific Fields）。

相关声明：[UMP Stream specific fields](P103_UMP流消息字段.md)。

> 译注（源码核对）：这是整个UMP的消息类型0x0f，取自首字最高4位；流消息内部另有格式和10位状态字段，不能把消息类型值与流状态值互换。

<a id="ga6b9f0ce12bbdcb92fb4003ba9d5ed3e3"></a>

### 101.3.8\_`UMP\_MT\_UTILITY`

```c
#define UMP_MT_UTILITY 0x00
```

```c
#include <zephyr/audio/midi.h>
```

实用消息（Utility Messages）。

## 101.4\_源码跟踪与使用边界

译注依据保存的[官方MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[对应头文件](../../../include/zephyr/audio/midi.h)可用于源码跟踪，版本可能与网页不同；原注释存在疑点时，在相应条目旁给出核对依据。本批未执行固件构建或MIDI硬件测试。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

[上一章](P100_MIDI命令常量.md) · [返回大纲](大纲.md) · [下一章](P102_MIDI系统消息状态.md)
