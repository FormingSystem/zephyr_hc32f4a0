---
id: learning.zephyr-docs.usb.api-100
title: MIDI命令常量
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_MIDI命令常量

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__cmd.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 100.1\_阅读说明与来源

译注：本页说明MIDI通用数据包的消息类型、命令或流消息字段。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》（Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol）第 7.3 节：MIDI 1.0 通道语音消息。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

备注：当 UMP_MT(x)=UMP_MT_MIDI1_CHANNEL_VOICE 或 UMP_MT_MIDI2_CHANNEL_VOICE 时，UMP_MIDI_COMMAND(x) 可以是下列值之一。

相关声明：[UMP_MT(x)](P098_通用MIDI数据包定义.md#gafab438886f69fb74a6e058f9343867aa)、[UMP_MIDI_COMMAND(x)](P098_通用MIDI数据包定义.md#gac3af021e7300ab96e449da048545900f)。

## 100.2\_宏定义（Macros）

<a id="r_ga8300450177c4f1ec7c11ed7d8886f87e"></a>

```c
#define UMP_MIDI_NOTE_OFF 0x8
```

音符关闭（Note Off）；p1 为音符编号（Note Number），p2 为力度（Velocity）。

相关声明：[UMP_MIDI_NOTE_OFF](P100_MIDI命令常量.md#ga8300450177c4f1ec7c11ed7d8886f87e)。

<a id="r_ga85749d1edff030bc0d8b131b9116911e"></a>

```c
#define UMP_MIDI_NOTE_ON 0x9
```

音符开启（Note On）；p1 为音符编号（Note Number），p2 为力度（Velocity）。

相关声明：[UMP_MIDI_NOTE_ON](P100_MIDI命令常量.md#ga85749d1edff030bc0d8b131b9116911e)。

<a id="r_ga7fae224629121ad30f9f38241885452c"></a>

```c
#define UMP_MIDI_AFTERTOUCH 0xa
```

复音触后压力（Polyphonic Aftertouch）；p1 为音符编号，p2 为数据。

相关声明：[UMP_MIDI_AFTERTOUCH](P100_MIDI命令常量.md#ga7fae224629121ad30f9f38241885452c)。

<a id="r_gad4b17d74027a541957c933074d0f2d1e"></a>

```c
#define UMP_MIDI_CONTROL_CHANGE 0xb
```

控制变更（Control Change）；p1 为索引（Index），p2 为数据。

相关声明：[UMP_MIDI_CONTROL_CHANGE](P100_MIDI命令常量.md#gad4b17d74027a541957c933074d0f2d1e)。

<a id="r_gaad34de6aae0e22f5c84ef50e488e2d1a"></a>

```c
#define UMP_MIDI_PROGRAM_CHANGE 0xc
```

控制变更（Control Change）；p1 为音色程序（Program）。

相关声明：[UMP_MIDI_PROGRAM_CHANGE](P100_MIDI命令常量.md#gaad34de6aae0e22f5c84ef50e488e2d1a)。

<a id="r_gaf5708894b80514023949e163f9687fb8"></a>

```c
#define UMP_MIDI_CHAN_AFTERTOUCH 0xd
```

通道触后压力（Channel Aftertouch）；p1 为数据。

相关声明：[UMP_MIDI_CHAN_AFTERTOUCH](P100_MIDI命令常量.md#gaf5708894b80514023949e163f9687fb8)。

<a id="r_gab11535e72a74baa71491264dd2c16192"></a>

```c
#define UMP_MIDI_PITCH_BEND 0xe
```

弯音（Pitch Bend）；p1 为低有效部分（LSB），p2 为高有效部分（MSB）。

相关声明：[UMP_MIDI_PITCH_BEND](P100_MIDI命令常量.md#gab11535e72a74baa71491264dd2c16192)。

## 100.3\_详细说明（Detailed Documentation）

<a id="ga7fae224629121ad30f9f38241885452c"></a>

### 100.3.1\_`UMP\_MIDI\_AFTERTOUCH`

```c
#define UMP_MIDI_AFTERTOUCH 0xa
```

```c
#include <zephyr/audio/midi.h>
```

复音触后压力（Polyphonic Aftertouch）；p1 为音符编号，p2 为数据。

<a id="gaf5708894b80514023949e163f9687fb8"></a>

### 100.3.2\_`UMP\_MIDI\_CHAN\_AFTERTOUCH`

```c
#define UMP_MIDI_CHAN_AFTERTOUCH 0xd
```

```c
#include <zephyr/audio/midi.h>
```

通道触后压力（Channel Aftertouch）；p1 为数据。

<a id="gad4b17d74027a541957c933074d0f2d1e"></a>

### 100.3.3\_`UMP\_MIDI\_CONTROL\_CHANGE`

```c
#define UMP_MIDI_CONTROL_CHANGE 0xb
```

```c
#include <zephyr/audio/midi.h>
```

控制变更（Control Change）；p1 为索引（Index），p2 为数据。

<a id="ga8300450177c4f1ec7c11ed7d8886f87e"></a>

### 100.3.4\_`UMP\_MIDI\_NOTE\_OFF`

```c
#define UMP_MIDI_NOTE_OFF 0x8
```

```c
#include <zephyr/audio/midi.h>
```

音符关闭（Note Off）；p1 为音符编号（Note Number），p2 为力度（Velocity）。

<a id="ga85749d1edff030bc0d8b131b9116911e"></a>

### 100.3.5\_`UMP\_MIDI\_NOTE\_ON`

```c
#define UMP_MIDI_NOTE_ON 0x9
```

```c
#include <zephyr/audio/midi.h>
```

音符开启（Note On）；p1 为音符编号（Note Number），p2 为力度（Velocity）。

<a id="gab11535e72a74baa71491264dd2c16192"></a>

### 100.3.6\_`UMP\_MIDI\_PITCH\_BEND`

```c
#define UMP_MIDI_PITCH_BEND 0xe
```

```c
#include <zephyr/audio/midi.h>
```

弯音（Pitch Bend）；p1 为低有效部分（LSB），p2 为高有效部分（MSB）。

> 译注（源码核对）：这里p1／p2的LSB／MSB指MIDI1弯音值的低7位与高7位，组合为(p2 << 7) | p1；并非两个完整8位参数组成16位值。本页虽然列出可由MIDI1和MIDI2通道消息使用的命令码，p1／p2注释描述的是MIDI1参数布局，不应套用到MIDI2全部负载字段。

<a id="gaad34de6aae0e22f5c84ef50e488e2d1a"></a>

### 100.3.7\_`UMP\_MIDI\_PROGRAM\_CHANGE`

```c
#define UMP_MIDI_PROGRAM_CHANGE 0xc
```

```c
#include <zephyr/audio/midi.h>
```

控制变更（Control Change）；p1 为音色程序（Program）。

> 译注（源码核对）：原注释写作Control Change，按原文译在上方；但宏名及值0xc对应音色程序变更（Program Change），其完整状态字节为0xCn，参数为程序编号。MIDI协会消息表也将0xBn控制变更与0xCn程序变更分列，参见[协会消息表](https://midi.org/summary-of-midi-1-0-messages)。

## 100.4\_源码跟踪与使用边界

译注依据保存的[官方MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[对应头文件](../../../include/zephyr/audio/midi.h)可用于源码跟踪，版本可能与网页不同；原注释存在疑点时，在相应条目旁给出核对依据。本批未执行固件构建或MIDI硬件测试。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

[上一章](P099_通用MIDI数据包结构.md) · [返回大纲](大纲.md) · [下一章](P101_UMP消息类型.md)
