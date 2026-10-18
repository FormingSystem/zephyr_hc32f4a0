---
id: learning.zephyr-docs.usb.api-102
title: MIDI系统消息状态
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__sys.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第102章\_MIDI系统消息状态

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__sys.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 102.1\_阅读说明与来源

译注：本页说明MIDI通用数据包的消息类型、命令或流消息字段。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.6 节：系统公共消息与系统实时消息。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

备注：当 UMP_MT(x)=UMP_MT_SYS_RT_COMMON 时，UMP_MIDI_STATUS(x) 可以是下列值之一。

相关声明：[UMP_MT(x)](P098_通用MIDI数据包定义.md#gafab438886f69fb74a6e058f9343867aa)、[UMP_MIDI_STATUS(x)](P098_通用MIDI数据包定义.md#ga407db6234865dd53a0939b9e6ca7455c)。

## 102.2\_宏定义（Macros）

<a id="r_ga85394094ca6d908b7886adc4caceb671"></a>

```c
#define UMP_SYS_MIDI_TIME_CODE 0xf1
```

MIDI 时间码（MIDI Time Code），无参数。

相关声明：[UMP_SYS_MIDI_TIME_CODE](P102_MIDI系统消息状态.md#ga85394094ca6d908b7886adc4caceb671)。

<a id="r_ga254845a2c32a190b0bfc217025c5ad1d"></a>

```c
#define UMP_SYS_SONG_POSITION 0xf2
```

歌曲位置指针（Song Position Pointer）；p1 为低有效部分（LSB），p2 为高有效部分（MSB）。

相关声明：[UMP_SYS_SONG_POSITION](P102_MIDI系统消息状态.md#ga254845a2c32a190b0bfc217025c5ad1d)。

<a id="r_ga1d27e0f6fffd7ec05f58b56be78d9a8d"></a>

```c
#define UMP_SYS_SONG_SELECT 0xf3
```

歌曲选择（Song Select）；p1 为歌曲编号。

相关声明：[UMP_SYS_SONG_SELECT](P102_MIDI系统消息状态.md#ga1d27e0f6fffd7ec05f58b56be78d9a8d)。

<a id="r_ga4aa12e0cdb101a38b938876ebdcca64b"></a>

```c
#define UMP_SYS_TUNE_REQUEST 0xf6
```

调音请求（Tune Request），无参数。

相关声明：[UMP_SYS_TUNE_REQUEST](P102_MIDI系统消息状态.md#ga4aa12e0cdb101a38b938876ebdcca64b)。

<a id="r_gae064f3f47a9387076f5045e12e6ef7b7"></a>

```c
#define UMP_SYS_TIMING_CLOCK 0xf8
```

定时时钟（Timing Clock），无参数。

相关声明：[UMP_SYS_TIMING_CLOCK](P102_MIDI系统消息状态.md#gae064f3f47a9387076f5045e12e6ef7b7)。

<a id="r_ga368ad3719080979709699feb3d002dff"></a>

```c
#define UMP_SYS_START 0xfa
```

开始（Start），无参数。

相关声明：[UMP_SYS_START](P102_MIDI系统消息状态.md#ga368ad3719080979709699feb3d002dff)。

<a id="r_ga766b54e3caced69c147dbc94eb932595"></a>

```c
#define UMP_SYS_CONTINUE 0xfb
```

继续（Continue），无参数。

相关声明：[UMP_SYS_CONTINUE](P102_MIDI系统消息状态.md#ga766b54e3caced69c147dbc94eb932595)。

<a id="r_ga95542dda8f7f73f738c3ae298ca42f44"></a>

```c
#define UMP_SYS_STOP 0xfc
```

停止（Stop），无参数。

相关声明：[UMP_SYS_STOP](P102_MIDI系统消息状态.md#ga95542dda8f7f73f738c3ae298ca42f44)。

<a id="r_gaeb794e3933a2488eadb5f57ba971f81d"></a>

```c
#define UMP_SYS_ACTIVE_SENSING 0xfe
```

活动感知（Active Sensing），无参数。

相关声明：[UMP_SYS_ACTIVE_SENSING](P102_MIDI系统消息状态.md#gaeb794e3933a2488eadb5f57ba971f81d)。

<a id="r_ga5bd5358ae1847774409216f4e246f6f4"></a>

```c
#define UMP_SYS_RESET 0xff
```

复位（Reset），无参数。

相关声明：[UMP_SYS_RESET](P102_MIDI系统消息状态.md#ga5bd5358ae1847774409216f4e246f6f4)。

## 102.3\_详细说明（Detailed Documentation）

<a id="gaeb794e3933a2488eadb5f57ba971f81d"></a>

### 102.3.1\_`UMP\_SYS\_ACTIVE\_SENSING`

```c
#define UMP_SYS_ACTIVE_SENSING 0xfe
```

```c
#include <zephyr/audio/midi.h>
```

活动感知（Active Sensing），无参数。

<a id="ga766b54e3caced69c147dbc94eb932595"></a>

### 102.3.2\_`UMP\_SYS\_CONTINUE`

```c
#define UMP_SYS_CONTINUE 0xfb
```

```c
#include <zephyr/audio/midi.h>
```

继续（Continue），无参数。

<a id="ga85394094ca6d908b7886adc4caceb671"></a>

### 102.3.3\_`UMP\_SYS\_MIDI\_TIME\_CODE`

```c
#define UMP_SYS_MIDI_TIME_CODE 0xf1
```

```c
#include <zephyr/audio/midi.h>
```

MIDI 时间码（MIDI Time Code），无参数。

> 译注（源码核对）：原注释“无参数”有误。MIDI协会表将0xF1定义为时间码四分之一帧（MIDI Time Code Quarter Frame），其后有一个0nnndddd数据字节；在此处的系统消息构造／提取约定中应提供p1，p2不使用。参见[协会消息表](https://midi.org/summary-of-midi-1-0-messages)。

<a id="ga5bd5358ae1847774409216f4e246f6f4"></a>

### 102.3.4\_`UMP\_SYS\_RESET`

```c
#define UMP_SYS_RESET 0xff
```

```c
#include <zephyr/audio/midi.h>
```

复位（Reset），无参数。

<a id="ga254845a2c32a190b0bfc217025c5ad1d"></a>

### 102.3.5\_`UMP\_SYS\_SONG\_POSITION`

```c
#define UMP_SYS_SONG_POSITION 0xf2
```

```c
#include <zephyr/audio/midi.h>
```

歌曲位置指针（Song Position Pointer）；p1 为低有效部分（LSB），p2 为高有效部分（MSB）。

> 译注（源码核对）：歌曲位置值由两个7位部分组成，即(p2 << 7) | p1；不要把两部分理解成完整低／高8位字节。

<a id="ga1d27e0f6fffd7ec05f58b56be78d9a8d"></a>

### 102.3.6\_`UMP\_SYS\_SONG\_SELECT`

```c
#define UMP_SYS_SONG_SELECT 0xf3
```

```c
#include <zephyr/audio/midi.h>
```

歌曲选择（Song Select）；p1 为歌曲编号。

<a id="ga368ad3719080979709699feb3d002dff"></a>

### 102.3.7\_`UMP\_SYS\_START`

```c
#define UMP_SYS_START 0xfa
```

```c
#include <zephyr/audio/midi.h>
```

开始（Start），无参数。

<a id="ga95542dda8f7f73f738c3ae298ca42f44"></a>

### 102.3.8\_`UMP\_SYS\_STOP`

```c
#define UMP_SYS_STOP 0xfc
```

```c
#include <zephyr/audio/midi.h>
```

停止（Stop），无参数。

<a id="gae064f3f47a9387076f5045e12e6ef7b7"></a>

### 102.3.9\_`UMP\_SYS\_TIMING\_CLOCK`

```c
#define UMP_SYS_TIMING_CLOCK 0xf8
```

```c
#include <zephyr/audio/midi.h>
```

定时时钟（Timing Clock），无参数。

<a id="ga4aa12e0cdb101a38b938876ebdcca64b"></a>

### 102.3.10\_`UMP\_SYS\_TUNE\_REQUEST`

```c
#define UMP_SYS_TUNE_REQUEST 0xf6
```

```c
#include <zephyr/audio/midi.h>
```

调音请求（Tune Request），无参数。

## 102.4\_源码跟踪与使用边界

译注依据保存的[官方MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[对应头文件](../../../include/zephyr/audio/midi.h)可用于源码跟踪，版本可能与网页不同；原注释存在疑点时，在相应条目旁给出核对依据。本批未执行固件构建或MIDI硬件测试。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

[上一章](P101_UMP消息类型.md) · [返回大纲](大纲.md) · [下一章](P103_UMP流消息字段.md)
