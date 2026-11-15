---
id: learning.zephyr-docs.usb.api-95
title: USBMIDI回调接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__midi__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第95章\_USBMIDI回调接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__midi__ops.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 95.1\_阅读说明与来源

译注：本页说明USB MIDI 2.0设备接口与回调。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

MIDI2 应用事件处理程序（Application Event Handlers）。

```c
#include <zephyr/usb/class/usbd_midi2.h>
```

MIDI2 应用事件处理程序（Application Event Handlers）。

## 95.2\_数据成员（Data Fields）

<a id="r_a2cfa4187ff4f1b0bc602b92cfc3cba1d"></a>

```c
void(* rx_packet_cb )(const struct device *dev, const struct midi_ump ump)
```

接收来自主机的通用 MIDI 数据包时使用的回调类型。

相关声明：[rx_packet_cb](P095_USBMIDI回调接口.md#a2cfa4187ff4f1b0bc602b92cfc3cba1d)、[device](../device_reference/P002_设备对象结构.md)、[midi_ump](P099_通用MIDI数据包结构.md)。

<a id="r_a1b0d3b3f7fe7833f2d71abc568029fbf"></a>

```c
void(* ready_cb )(const struct device *dev, const bool ready)
```

MIDI2 接口运行时状态（Runtime Status）变化的回调类型。

相关声明：[ready_cb](P095_USBMIDI回调接口.md#a1b0d3b3f7fe7833f2d71abc568029fbf)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

## 95.3\_详细说明（Detailed Documentation）

<a id="a1b0d3b3f7fe7833f2d71abc568029fbf"></a>

### 95.3.1\_`ready\_cb`

```c
void(* usbd_midi_ops::ready_cb) (const struct device *dev, const bool ready)
```

MIDI2 接口运行时状态（Runtime Status）变化的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | MIDI2 设备。 |
| `[in] ready` | 主机启用接口时为 true。 |

> 译注（源码核对）：当前实现依据备用设置（Alternate Setting）切换报告MIDI2可用状态；停用或挂起时报告false，恢复或启用且选择MIDI2备用设置时报告true。该状态不是物理连接、应用已读取数据或发送已完成的通知。

<a id="a2cfa4187ff4f1b0bc602b92cfc3cba1d"></a>

### 95.3.2\_`rx\_packet\_cb`

```c
void(* usbd_midi_ops::rx_packet_cb) (const struct device *dev, const struct midi_ump ump)
```

接收来自主机的通用 MIDI 数据包时使用的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 接收该数据包的 MIDI2 设备。 |
| `[in] ump` | 收到的数据包，采用通用 MIDI 数据包（UMP）格式。 |

> 译注（源码核对）：当前驱动按UMP的消息类型确定字数，从USB接收缓冲区解析各个小端32位字，并按值传入完整消息。解析发现数据包不完整时记录错误并停止，不会为残缺的UMP调用此回调；回调不是对原始USB字节缓冲区的所有权移交。

## 95.4\_源码跟踪与使用边界

译注依据保存的[官方MIDI设备头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_midi2.h)、[类驱动实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_midi2.c)与[通用MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[设备头文件](../../../include/zephyr/usb/class/usbd_midi2.h)、[驱动实现](../../../subsys/usb/device_next/class/usbd_midi2.c)与[通用MIDI头文件](../../../include/zephyr/audio/midi.h)可用于跟踪，版本可能与网页不同。本批未执行固件构建或USB MIDI硬件测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P094_USBMIDI2设备API.md) · [返回大纲](大纲.md) · [下一章](P096_USBMIDI2设备示例.md)
