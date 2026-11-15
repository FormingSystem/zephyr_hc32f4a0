---
id: learning.zephyr-docs.api-source-reference.page-898
title: usbd_uvc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__uvc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第898章\_usbd\_uvc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbd__uvc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../usb/P123_USB视频头文件接口.md)。

## 898.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00027"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2video_8h_html"></a>
<a id="agroup__usbd__uvc_html_ga9c84595e78a2294f1470056199c074ae"></a>
<a id="agroup__usbd__uvc_html_gacdfc08f59e0032e68b838f5893edbda1"></a>
<a id="agroup__usbd__uvc_html_gad6415b544866cfa15efac2a53c760f2a"></a>
<a id="agroup__usbd__uvc_html_gaec4b7ac54a524724bb29751fd1cafafe"></a>
<a id="astructdevice_html"></a>
<a id="astructvideo__format_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) tinyVision.ai Inc.
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USB_CLASS_USBD_UVC_H
#define ZEPHYR_INCLUDE_USB_CLASS_USBD_UVC_H

#include <zephyr/device.h>
#include <zephyr/drivers/video.h>


void uvc_device_init(const struct device *uvc_dev, const struct device *video_dev);

int uvc_device_add_format(const struct device *const uvc_dev, const struct video_format *const fmt);

int uvc_device_enable(const struct device *const uvc_dev);

int uvc_device_shutdown(const struct device *const uvc_dev);


#endif /* ZEPHYR_INCLUDE_USB_CLASS_USBD_UVC_H */
```

## 898.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) tinyVision.ai Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 88 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_CLASS_USBD_UVC_H`。

## 898.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../usb/P123_USB视频头文件接口.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/video.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h.html)
- [uvc_device_init](../usb/P122_USB视频设备API.md#ga9c84595e78a2294f1470056199c074ae)
- [device](../device_reference/P002_设备对象结构.md)
- [uvc_device_add_format](../usb/P122_USB视频设备API.md#gacdfc08f59e0032e68b838f5893edbda1)
- [video_format](../audio_video_model_reference/P059_video_format_结构体.md)
- [uvc_device_enable](../usb/P122_USB视频设备API.md#gaec4b7ac54a524724bb29751fd1cafafe)
- [uvc_device_shutdown](../usb/P122_USB视频设备API.md#gad6415b544866cfa15efac2a53c760f2a)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [video.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h.html)

---

[上一章](P897_usbd_uac2.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P899_user_pipe.h_源码浏览.md)
