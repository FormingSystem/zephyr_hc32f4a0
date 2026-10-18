---
id: learning.zephyr-docs.usb.api-99
title: 通用MIDI数据包结构
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmidi__ump.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_通用MIDI数据包结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmidi__ump.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 99.1\_阅读说明与来源

译注：本页说明MIDI通用数据包的容器与字段操作宏。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

通用 MIDI 数据包容器（Container）。

```c
#include <zephyr/audio/midi.h>
```

通用 MIDI 数据包容器（Container）。

## 99.2\_数据成员（Data Fields）

<a id="r_a9c38cadb8046ba91b080604ac66ea89f"></a>

```c
uint32_t data [4]
```

原始内容，使用 CPU 本机字节序（Native Endianness）。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[data](P099_通用MIDI数据包结构.md#a9c38cadb8046ba91b080604ac66ea89f)。

## 99.3\_详细说明（Detailed Documentation）

<a id="a9c38cadb8046ba91b080604ac66ea89f"></a>

### 99.3.1\_`data`

```c
uint32_t midi_ump::data[4]
```

原始内容，使用 CPU 本机字节序（Native Endianness）。

> 译注（源码核对）：data[4]提供最多128位的容器容量；实际有效字数由消息类型确定。数组元素使用CPU本机字节序，不是已经编码好的USB字节流；USB MIDI驱动发送时逐字转换为小端序，接收时进行反向解析。

## 99.4\_源码跟踪与使用边界

译注依据保存的[官方MIDI设备头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_midi2.h)、[类驱动实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_midi2.c)与[通用MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[设备头文件](../../../include/zephyr/usb/class/usbd_midi2.h)、[驱动实现](../../../subsys/usb/device_next/class/usbd_midi2.c)与[通用MIDI头文件](../../../include/zephyr/audio/midi.h)可用于跟踪，版本可能与网页不同。本批未执行固件构建或USB MIDI硬件测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P098_通用MIDI数据包定义.md) · [返回大纲](大纲.md) · [下一章](P100_MIDI命令常量.md)
