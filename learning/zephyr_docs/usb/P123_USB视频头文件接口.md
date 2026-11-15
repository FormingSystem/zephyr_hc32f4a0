---
id: learning.zephyr-docs.usb.api-123
title: USB视频头文件接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__uvc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第123章\_USB视频头文件接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbd__uvc_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 123.1\_阅读说明与来源

译注：本页说明USB视频类（USB Video Class，UVC）设备接口。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 视频类（USB Video Class，UVC）公开头文件。

```c
#include <zephyr/device.h>
```

```c
#include <zephyr/drivers/video.h>
```

USB 视频类（USB Video Class，UVC）公开头文件。

## 123.2\_函数（Functions）

<a id="r_ga9c84595e78a2294f1470056199c074ae"></a>

```c
void uvc_device_init (const struct device *uvc_dev, const struct device *video_dev)
```

初始化视频设备类（Video Device Class）。

相关声明：[uvc_device_init](P122_USB视频设备API.md#ga9c84595e78a2294f1470056199c074ae)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gacdfc08f59e0032e68b838f5893edbda1"></a>

```c
int uvc_device_add_format (const struct device *const uvc_dev, const struct video_format *const fmt)
```

添加一种由 UVC 实例向主机呈现的视频格式（Video Format）。

相关声明：[uvc_device_add_format](P122_USB视频设备API.md#gacdfc08f59e0032e68b838f5893edbda1)、[device](../device_reference/P002_设备对象结构.md)、[video_format](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__format.html)。

<a id="r_gaec4b7ac54a524724bb29751fd1cafafe"></a>

```c
int uvc_device_enable (const struct device *const uvc_dev)
```

完成 UVC 设备实例的配置。

相关声明：[uvc_device_enable](P122_USB视频设备API.md#gaec4b7ac54a524724bb29751fd1cafafe)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gad6415b544866cfa15efac2a53c760f2a"></a>

```c
int uvc_device_shutdown (const struct device *const uvc_dev)
```

撤销 UVC 设备实例的配置。

相关声明：[uvc_device_shutdown](P122_USB视频设备API.md#gad6415b544866cfa15efac2a53c760f2a)、[device](../device_reference/P002_设备对象结构.md)。

## 123.3\_源码跟踪与使用边界

译注依据保存的[官方UVC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_uvc.h)、[驱动实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_uvc.c)与[设备示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uvc/src/main.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[UVC头文件](../../../include/zephyr/usb/class/usbd_uvc.h)和[实现](../../../subsys/usb/device_next/class/usbd_uvc.c)可用于跟踪，版本可能与网页不同。本批未构建、采集视频或进行USB硬件测试。

<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>

[上一章](P122_USB视频设备API.md) · [返回大纲](大纲.md) · [下一章](P124_USB视频摄像头示例.md)
