---
id: learning.zephyr-docs.usb.api-94
title: USBMIDI2设备API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__midi2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_USBMIDI2设备API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__midi2.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 94.1\_阅读说明与来源

译注：本页说明USB MIDI 2.0设备接口与回调。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB MIDI 2.0 类设备 API（USB MIDI 2.0 Class Device API）。

USB MIDI 2.0 类设备 API（USB MIDI 2.0 Class Device API）。

引入版本（Since）：4.1。

接口版本（Version）：0.1.0。

参阅（See Also）：midi20，《通用串行总线MIDI设备类定义》（Universal Serial Bus Device Class Definition for MIDI Devices），文档发行版2.0，2020年5月5日。

## 94.2\_数据结构（Data Structures）

<a id="r_usbd_5Fmidi_5Fops"></a>

```c
struct usbd_midi_ops
```

MIDI2 应用事件处理程序（Application Event Handlers）。

相关声明：[usbd_midi_ops](P095_USBMIDI回调接口.md)。

## 94.3\_函数（Functions）

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

## 94.4\_详细说明（Detailed Documentation）

<a id="gab0e96783f610e881b5c36718e708a7d8"></a>

### 94.4.1\_`usbd\_midi\_send()`

```c
int usbd_midi_send ( const struct device * dev, const struct midi_ump ump )
```

```c
#include <zephyr/usb/class/usbd_midi2.h>
```

向主机发送通用 MIDI 数据包（Universal MIDI Packet，UMP）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | MIDI2 设备。 |
| `[in] ump` | 要发送的数据包，采用通用 MIDI 数据包（UMP）格式。 |

**返回（Returns）**：成功返回 0，所有其他值均应视为错误；主机尚未启用 USB MIDI 2.0 时返回 -EIO，发送缓冲区（TX Buffer）空间不足时返回 -ENOBUFS。

> 译注（源码核对）：UMP按值传入，当前实现根据UMP_NUM_WORDS取得长度，将有效32位字转换为小端序（Little-Endian）后复制进发送环形缓冲区，并提交发送工作项。返回0说明已排队，不是主机接收确认；这里没有UAC2那种外部数据缓冲区的所有权移交。

<a id="gab08255e3bd10aea5c272ca08303b1bf5"></a>

### 94.4.2\_`usbd\_midi\_set\_ops()`

```c
void usbd_midi_set_ops ( const struct device * dev, const struct usbd_midi_ops * ops )
```

```c
#include <zephyr/usb/class/usbd_midi2.h>
```

设置 USB MIDI 设备的应用事件处理程序。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | MIDI2 设备。 |
| `[in] ops` | 事件处理程序。传入 NULL 可重置所有回调（Callbacks）。 |

> 译注（源码核对）：当前实现使用memcpy复制回调表，传入NULL则将保存的回调表清零。这与保存外部回调表指针的其他设备类接口不同；应按本接口实际实现理解对象生命周期。

## 94.5\_源码跟踪与使用边界

译注依据保存的[官方MIDI设备头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_midi2.h)、[类驱动实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_midi2.c)与[通用MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[设备头文件](../../../include/zephyr/usb/class/usbd_midi2.h)、[驱动实现](../../../subsys/usb/device_next/class/usbd_midi2.c)与[通用MIDI头文件](../../../include/zephyr/audio/midi.h)可用于跟踪，版本可能与网页不同。本批未执行固件构建或USB MIDI硬件测试。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P093_USBMIDI2设备API说明.md) · [返回大纲](大纲.md) · [下一章](P095_USBMIDI回调接口.md)
