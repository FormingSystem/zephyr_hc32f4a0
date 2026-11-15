---
id: learning.zephyr-docs.api-source-reference.page-894
title: usbd_midi2.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__midi2_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第894章\_usbd\_midi2.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbd__midi2_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../usb/P097_USBMIDI2头文件接口.md)。

## 894.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__usbd__midi2_html_gab08255e3bd10aea5c272ca08303b1bf5"></a>
<a id="agroup__usbd__midi2_html_gab0e96783f610e881b5c36718e708a7d8"></a>
<a id="amidi_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_ab6d65f3402e67afb9810a8356b915071"></a>
<a id="astructmidi__ump_html"></a>
<a id="astructusbd__midi__ops_html"></a>
<a id="astructusbd__midi__ops_html_a1b0d3b3f7fe7833f2d71abc568029fbf"></a>
<a id="astructusbd__midi__ops_html_a2cfa4187ff4f1b0bc602b92cfc3cba1d"></a>

```c
/*
 * Copyright (c) 2024 Titouan Christophe
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_USB_CLASS_USBD_MIDI_H_
#define ZEPHYR_INCLUDE_USB_CLASS_USBD_MIDI_H_

#ifdef __cplusplus
extern "C" {
#endif


#include <zephyr/device.h>
#include <zephyr/audio/midi.h>

struct usbd_midi_ops {
        void (*rx_packet_cb)(const struct device *dev, const struct midi_ump ump);

        void (*ready_cb)(const struct device *dev, const bool ready);
};

int usbd_midi_send(const struct device *dev, const struct midi_ump ump);

void usbd_midi_set_ops(const struct device *dev, const struct usbd_midi_ops *ops);


#ifdef __cplusplus
}
#endif

#endif
```

## 894.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Titouan Christophe。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 894.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../usb/P097_USBMIDI2头文件接口.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/audio/midi.h](https://docs.zephyrproject.org/latest/doxygen/html/midi_8h.html)
- [usbd_midi_ops](../usb/P095_USBMIDI回调接口.md)
- [rx_packet_cb](../usb/P095_USBMIDI回调接口.md#a2cfa4187ff4f1b0bc602b92cfc3cba1d)
- [device](../device_reference/P002_设备对象结构.md)
- [midi_ump](../usb/P099_通用MIDI数据包结构.md)
- [ready_cb](../usb/P095_USBMIDI回调接口.md#a1b0d3b3f7fe7833f2d71abc568029fbf)
- [usbd_midi_send](../usb/P094_USBMIDI2设备API.md#gab0e96783f610e881b5c36718e708a7d8)
- [usbd_midi_set_ops](../usb/P094_USBMIDI2设备API.md#gab08255e3bd10aea5c272ca08303b1bf5)
- [ops](../device_reference/P002_设备对象结构.md#ab6d65f3402e67afb9810a8356b915071)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [midi.h](https://docs.zephyrproject.org/latest/doxygen/html/midi_8h.html)
- [device::ops](../device_reference/P002_设备对象结构.md#ab6d65f3402e67afb9810a8356b915071)
- [usbd_midi_ops::ready_cb](../usb/P095_USBMIDI回调接口.md#a1b0d3b3f7fe7833f2d71abc568029fbf)
- [usbd_midi_ops::rx_packet_cb](../usb/P095_USBMIDI回调接口.md#a2cfa4187ff4f1b0bc602b92cfc3cba1d)

---

[上一章](P893_usbc_vbus.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P895_usbd_msc.h_源码浏览.md)
