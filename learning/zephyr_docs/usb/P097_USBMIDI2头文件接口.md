---
id: learning.zephyr-docs.usb.api-97
title: USBMIDI2头文件接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__midi2_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第97章\_USBMIDI2头文件接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbd__midi2_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 97.1\_阅读说明与来源

译注：本页说明USB MIDI 2.0设备接口与回调。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

```c
#include <zephyr/device.h>
```

```c
#include <zephyr/audio/midi.h>
```

## 97.2\_数据结构（Data Structures）

<a id="r_usbd_5Fmidi_5Fops"></a>

```c
struct usbd_midi_ops
```

MIDI2 应用事件处理程序（Application Event Handlers）。

相关声明：[usbd_midi_ops](P095_USBMIDI回调接口.md)。

## 97.3\_函数（Functions）

<a id="r_gab0e96783f610e881b5c36718e708a7d8"></a>

```c
int usbd_midi_send (const struct device *dev, const struct midi_ump ump)
```

向主机发送通用 MIDI 数据包（Universal MIDI Packet，UMP）。

相关声明：[usbd_midi_send](P094_USBMIDI2设备API.md#gab0e96783f610e881b5c36718e708a7d8)、[device](../device_reference/P002_设备对象结构.md)、[midi_ump](P099_通用MIDI数据包结构.md)。

<a id="r_gab08255e3bd10aea5c272ca08303b1bf5"></a>

```c
void usbd_midi_set_ops (const struct device *dev, const struct usbd_midi_ops *ops)
```

设置 USB MIDI 设备的应用事件处理程序。

相关声明：[usbd_midi_set_ops](P094_USBMIDI2设备API.md#gab08255e3bd10aea5c272ca08303b1bf5)、[device](../device_reference/P002_设备对象结构.md)、[usbd_midi_ops](P095_USBMIDI回调接口.md)。

## 97.4\_源码跟踪与使用边界

译注依据保存的[官方MIDI设备头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_midi2.h)、[类驱动实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_midi2.c)与[通用MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[设备头文件](../../../include/zephyr/usb/class/usbd_midi2.h)、[驱动实现](../../../subsys/usb/device_next/class/usbd_midi2.c)与[通用MIDI头文件](../../../include/zephyr/audio/midi.h)可用于跟踪，版本可能与网页不同。本批未执行固件构建或USB MIDI硬件测试。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>

[上一章](P096_USBMIDI2设备示例.md) · [返回大纲](大纲.md) · [下一章](P098_通用MIDI数据包定义.md)
