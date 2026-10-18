---
id: learning.zephyr-docs.usb.api-98
title: 通用MIDI数据包定义
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第98章\_通用MIDI数据包定义

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 98.1\_阅读说明与来源

译注：本页说明MIDI通用数据包的容器与字段操作宏。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

通用 MIDI 数据包（Universal MIDI Packet，UMP）定义。

通用 MIDI 数据包（Universal MIDI Packet，UMP）定义。

引入版本（Since）：4.1。

接口版本（Version）：0.1.0。

## 98.2\_主题（Topics）

<a id="r_midi_5Fump_5Fcmd"></a>

MIDI命令（MIDI commands）。



相关声明：[MIDI commands](P100_MIDI命令常量.md)。

<a id="r_midi_5Fump_5Fmt"></a>

消息类型（Message types）。



相关声明：[Message types](P101_UMP消息类型.md)。

<a id="r_midi_5Fump_5Fsys"></a>

系统公共消息与系统实时消息状态（System common and System Real Time message status）。



相关声明：[System common and System Real Time message status](P102_MIDI系统消息状态.md)。

<a id="r_ump_5Fstream_5Fresponder"></a>

UMP流响应器（UMP Stream Responder）。

响应 UMP 流消息中的端点发现（Endpoint Discovery）或功能块发现（Function Block Discovery）。

相关声明：[UMP Stream Responder](P108_UMP流响应器API.md)。

<a id="r_midi_5Fump_5Fstream"></a>

UMP流专用字段（UMP Stream specific fields）。



相关声明：[UMP Stream specific fields](P103_UMP流消息字段.md)。

<a id="r_ump112"></a>

通用MIDI数据包格式与MIDI 2.0协议（Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol）。



相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

## 98.3\_文件（Files）

<a id="r_midi_2Eh"></a>

```c
file midi.h
```

MIDI 2.0 通用 MIDI 数据包（UMP）定义的头文件。

相关声明：[midi.h](https://docs.zephyrproject.org/latest/doxygen/html/midi_8h.html)。

## 98.4\_数据结构（Data Structures）

<a id="r_midi_5Fump"></a>

```c
struct midi_ump
```

通用 MIDI 数据包容器（Container）。

相关声明：[midi_ump](P099_通用MIDI数据包结构.md)。

## 98.5\_宏定义（Macros）

<a id="r_gafab438886f69fb74a6e058f9343867aa"></a>

```c
#define UMP_MT(ump)
```

通用 MIDI 数据包的消息类型（Message Type，MT）字段。

相关声明：[UMP_MT](P098_通用MIDI数据包定义.md#gafab438886f69fb74a6e058f9343867aa)。

<a id="r_gac718c321652066f1537ead1524137949"></a>

```c
#define UMP_NUM_WORDS_LOOKUP_TABLE
```

UMP 共有 16 种消息类型，每种消息的长度可以是 1 到 4 个 uint32。

相关声明：[UMP_NUM_WORDS_LOOKUP_TABLE](P098_通用MIDI数据包定义.md#gac718c321652066f1537ead1524137949)。

<a id="r_ga31e6cb035180b3afca9980307a07c038"></a>

```c
#define UMP_NUM_WORDS(ump)
```

通用 MIDI 数据包的大小，以 32 位字（32-bit Word）为单位。

相关声明：[UMP_NUM_WORDS](P098_通用MIDI数据包定义.md#ga31e6cb035180b3afca9980307a07c038)。

<a id="r_ga497e212c131b7366878e46f63727cab5"></a>

```c
#define UMP_GROUP(ump)
```

通用 MIDI 数据包的 MIDI 组（Group）字段。

相关声明：[UMP_GROUP](P098_通用MIDI数据包定义.md#ga497e212c131b7366878e46f63727cab5)。

<a id="r_ga407db6234865dd53a0939b9e6ca7455c"></a>

```c
#define UMP_MIDI_STATUS(ump)
```

MIDI 通道语音消息（Channel Voice Message）或系统消息（System Message）的状态字节（Status Byte）。

相关声明：[UMP_MIDI_STATUS](P098_通用MIDI数据包定义.md#ga407db6234865dd53a0939b9e6ca7455c)。

<a id="r_gac3af021e7300ab96e449da048545900f"></a>

```c
#define UMP_MIDI_COMMAND(ump)
```

MIDI 通道语音消息的命令（Command）。

相关声明：[UMP_MIDI_COMMAND](P098_通用MIDI数据包定义.md#gac3af021e7300ab96e449da048545900f)。

<a id="r_ga8ecdaa13831c0cf1abf79da0b343416f"></a>

```c
#define UMP_MIDI_CHANNEL(ump)
```

MIDI 通道语音消息的通道（Channel）。

相关声明：[UMP_MIDI_CHANNEL](P098_通用MIDI数据包定义.md#ga8ecdaa13831c0cf1abf79da0b343416f)。

<a id="r_gac64740902864ecb903f70083f2c638d2"></a>

```c
#define UMP_MIDI1_P1(ump)
```

MIDI1 通道语音消息或系统消息的第一个参数。

相关声明：[UMP_MIDI1_P1](P098_通用MIDI数据包定义.md#gac64740902864ecb903f70083f2c638d2)。

<a id="r_ga1c6c6f8928071d4d77744404e62168b4"></a>

```c
#define UMP_MIDI1_P2(ump)
```

MIDI1 通道语音消息或系统消息的第二个参数。

相关声明：[UMP_MIDI1_P2](P098_通用MIDI数据包定义.md#ga1c6c6f8928071d4d77744404e62168b4)。

<a id="r_gac05c1718b33d08a92bae9b4974ced501"></a>

```c
#define UMP_MIDI1_CHANNEL_VOICE(group, command, channel, p1, p2)
```

使用 MIDI1 通道语音消息初始化一个 UMP。

相关声明：[UMP_MIDI1_CHANNEL_VOICE](P098_通用MIDI数据包定义.md#gac05c1718b33d08a92bae9b4974ced501)、[group](https://docs.zephyrproject.org/latest/doxygen/html/structgroup.html)。

<a id="r_ga06562acb0ec4d618d2e05b94c0a1bc4f"></a>

```c
#define UMP_SYS_RT_COMMON(group, status, p1, p2)
```

使用系统实时消息（System Real Time Message）或系统公共消息（System Common Message）初始化一个 UMP。

相关声明：[UMP_SYS_RT_COMMON](P098_通用MIDI数据包定义.md#ga06562acb0ec4d618d2e05b94c0a1bc4f)、[group](https://docs.zephyrproject.org/latest/doxygen/html/structgroup.html)。

## 98.6\_详细说明（Detailed Documentation）

<a id="ga497e212c131b7366878e46f63727cab5"></a>

### 98.6.1\_`UMP\_GROUP`

```c
#define UMP_GROUP ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
(((ump).data[0] >> 24) & 0xF)
```

通用 MIDI 数据包的 MIDI 组（Group）字段。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包（UMP）。 |

> 译注（源码核对）：该宏机械提取位27至24，只有所解释的消息类型具有组字段时才具备相应语义。尤其不能把UMP Stream消息的同一位置无条件当作普通组号。

<a id="gac05c1718b33d08a92bae9b4974ced501"></a>

### 98.6.2\_`UMP\_MIDI1\_CHANNEL\_VOICE`

```c
#define UMP_MIDI1_CHANNEL_VOICE ( group, command, channel, p1, p2 )
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
(struct midi_ump) {.data = {                             \
        (UMP_MT_MIDI1_CHANNEL_VOICE << 28)               \
        | (((group) & 0x0f) << 24)                       \
        | (((command) & 0x0f) << 20)                     \
        | (((channel) & 0x0f) << 16)                     \
        | (((p1) & 0x7f) << 8)                           \
        | ((p2) & 0x7f)                                  \
}}
```

使用 MIDI1 通道语音消息初始化一个 UMP。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | UMP 组。 |
| `command` | MIDI1 命令。 |
| `channel` | MIDI1 通道编号。 |
| `p1` | 第一个 MIDI1 参数。 |
| `p2` | 第二个 MIDI1 参数。 |

**备注（Remarks）**：对于只接收一个参数的消息，接收方会忽略 p2。

> 译注（源码核对）：宏将group、command和channel分别限制为低4位，p1和p2分别限制为低7位；这是位掩码截取，不是带错误返回的参数校验。command应传命令半字节（例如UMP_MIDI_NOTE_ON），不是包含通道的完整状态字节。

<a id="gac64740902864ecb903f70083f2c638d2"></a>

### 98.6.3\_`UMP\_MIDI1\_P1`

```c
#define UMP_MIDI1_P1 ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
(((ump).data[0] >> 8) & 0x7F)
```

MIDI1 通道语音消息或系统消息的第一个参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包，包含 MIDI1 消息。 |

<a id="ga1c6c6f8928071d4d77744404e62168b4"></a>

### 98.6.4\_`UMP\_MIDI1\_P2`

```c
#define UMP_MIDI1_P2 ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
((ump).data[0] & 0x7F)
```

MIDI1 通道语音消息或系统消息的第二个参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包，包含 MIDI1 消息。 |

<a id="ga8ecdaa13831c0cf1abf79da0b343416f"></a>

### 98.6.5\_`UMP\_MIDI\_CHANNEL`

```c
#define UMP_MIDI_CHANNEL ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
(UMP_MIDI_STATUS(ump) & 0xF)
```

MIDI 通道语音消息的通道（Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包，包含 MIDI 事件。 |

> 译注（源码核对）：该宏返回状态字节低4位的原始通道编号，范围0至15；界面上常见的通道1至16表示法需要由应用自行对应。只对有通道字段的消息使用。

<a id="gac3af021e7300ab96e449da048545900f"></a>

### 98.6.6\_`UMP\_MIDI\_COMMAND`

```c
#define UMP_MIDI_COMMAND ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
(UMP_MIDI_STATUS(ump) >> 4)
```

MIDI 通道语音消息的命令（Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包，包含 MIDI 事件。 |

**参阅（See Also）**：MIDI 命令（MIDI Commands）。

<a id="ga407db6234865dd53a0939b9e6ca7455c"></a>

### 98.6.7\_`UMP\_MIDI\_STATUS`

```c
#define UMP_MIDI_STATUS ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
(((ump).data[0] >> 16) & 0xFF)
```

MIDI 通道语音消息（Channel Voice Message）或系统消息（System Message）的状态字节（Status Byte）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包，包含 MIDI1 事件。 |

**参阅（See Also）**：系统公共消息与系统实时消息的状态（System Common and System Real Time Message Status）。

<a id="gafab438886f69fb74a6e058f9343867aa"></a>

### 98.6.8\_`UMP\_MT`

```c
#define UMP_MT ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
((ump).data[0] >> 28)
```

通用 MIDI 数据包的消息类型（Message Type，MT）字段。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包（UMP）。 |

**参阅（See Also）**：消息类型（Message Types）。

> 译注（源码核对）：该宏直接取第一个32位字的最高4位。提取类型不等于验证了整条消息是否合法，也不证明输入缓冲区包含足够的数据。

<a id="ga31e6cb035180b3afca9980307a07c038"></a>

### 98.6.9\_`UMP\_NUM\_WORDS`

```c
#define UMP_NUM_WORDS ( ump)
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
(1 + ((UMP_NUM_WORDS_LOOKUP_TABLE >> (2 * UMP_MT(ump))) & 3))
```

通用 MIDI 数据包的大小，以 32 位字（32-bit Word）为单位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ump` | 通用 MIDI 数据包（UMP）。 |

**参阅（See Also）**：《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》（Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol）第 2.1.4 节：消息类型（MT）分配。

> 译注（源码核对）：返回单位是32位字，转换为字节需要乘以4。查找表按消息类型决定1至4个字；容器固定有4个元素，不代表每条消息都发送16字节。

<a id="gac718c321652066f1537ead1524137949"></a>

### 98.6.10\_`UMP\_NUM\_WORDS\_LOOKUP\_TABLE`

```c
#define UMP_NUM_WORDS_LOOKUP_TABLE
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
((0U << 0) | (0U << 2) | (0U << 4) | (1U << 6) | \
(1U << 8) | (3U << 10) | (0U << 12) | (0U << 14) | \
(1U << 16) | (1U << 18) | (1U << 20) | (2U << 22) | \
(2U << 24) | (3U << 26) | (3U << 28) | (3U << 30))
```

UMP 共有 16 种消息类型，每种消息的长度可以是 1 到 4 个 uint32。

因此，这里将一个包含 16 个 2 位元素的数组打包到一个 uint32 中，作为查找表（Lookup Table）。

> 译注（源码核对）：每种类型占2位，保存的是长度减1，UMP_NUM_WORDS再加1得到字数。这种映射包括保留类型位置，不能代替消息类型支持性检查。

<a id="ga06562acb0ec4d618d2e05b94c0a1bc4f"></a>

### 98.6.11\_`UMP\_SYS\_RT\_COMMON`

```c
#define UMP_SYS_RT_COMMON ( group, status, p1, p2 )
```

```c
#include <zephyr/audio/midi.h>
```

**宏展开值（Value）**

```c
(struct midi_ump) {.data = {             \
        (UMP_MT_SYS_RT_COMMON << 28)     \
        | (((group) & 0x0f) << 24)       \
        | ((status) << 16)               \
        | (((p1) & 0x7f) << 8)           \
        | ((p2) & 0x7f)                  \
}}
```

使用系统实时消息（System Real Time Message）或系统公共消息（System Common Message）初始化一个 UMP。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | UMP 组。 |
| `status` | 状态字节。 |
| `p1` | 第一个参数。 |
| `p2` | 第二个参数。 |

**备注（Remarks）**：对于只接收一个参数或不接收参数的消息，接收方会分别忽略 p2，或同时忽略 p2 和 p1。

> 译注（源码核对）：group、p1和p2在宏中带掩码，但status直接左移16位，调用者应提供合法的系统状态字节；宏本身不会检查状态是否合法。

## 98.7\_源码跟踪与使用边界

译注依据保存的[官方MIDI设备头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_midi2.h)、[类驱动实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_midi2.c)与[通用MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[设备头文件](../../../include/zephyr/usb/class/usbd_midi2.h)、[驱动实现](../../../subsys/usb/device_next/class/usbd_midi2.c)与[通用MIDI头文件](../../../include/zephyr/audio/midi.h)可用于跟踪，版本可能与网页不同。本批未执行固件构建或USB MIDI硬件测试。

<a id="header-groups"></a>
<a id="groups"></a>
<a id="header-files"></a>
<a id="files"></a>
<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__midi__ump__mt_html_gae086e5899933e436715ed2321607ef36"></a>
<a id="astructgroup_html"></a>
<a id="astructmidi__ump_html"></a>
<a id="agroup__midi__ump_html_ga407db6234865dd53a0939b9e6ca7455c"></a>
<a id="agroup__midi__ump_html_gac718c321652066f1537ead1524137949"></a>
<a id="agroup__midi__ump_html_gafab438886f69fb74a6e058f9343867aa"></a>
<a id="agroup__midi__ump__mt_html_gab8f194f60f1b5de7f050009275e44412"></a>

[上一章](P097_USBMIDI2头文件接口.md) · [返回大纲](大纲.md) · [下一章](P099_通用MIDI数据包结构.md)
