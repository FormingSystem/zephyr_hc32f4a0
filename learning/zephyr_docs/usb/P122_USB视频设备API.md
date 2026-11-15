---
id: learning.zephyr-docs.usb.api-122
title: USB视频设备API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__uvc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第122章\_USB视频设备API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__uvc.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 122.1\_阅读说明与来源

译注：本页说明USB视频类（USB Video Class，UVC）设备接口。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 视频类（USB Video Class，UVC）设备 API。

USB 视频类（USB Video Class，UVC）设备 API。

引入版本（Since）：4.2。

接口版本（Version）：0.1.1。

参阅 uvc：《通用串行总线视频设备类定义》（Universal Serial Bus Device Class Definition for Video Devices），文档发行版 1.5，2012 年 8 月 9 日。

## 122.2\_函数（Functions）

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

## 122.3\_详细说明（Detailed Documentation）

<a id="gacdfc08f59e0032e68b838f5893edbda1"></a>

### 122.3.1\_`uvc\_device\_add\_format()`

```c
int uvc_device_add_format ( const struct device *const uvc_dev, const struct video_format *const fmt )
```

```c
#include <zephyr/usb/class/usbd_uvc.h>
```

添加一种由 UVC 实例向主机呈现的视频格式（Video Format）。

这些信息用于生成 USB 描述符（Descriptors）。可以通过 video_get_format 查询主机选定的具体格式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uvc_dev` | 指向待配置 UVC 设备的指针。 |
| `fmt` | 要添加到此 UVC 实例的视频格式。 |

**注意（Note）**：必须在 uvc_device_enable 之前调用此函数。调用前必须设置 fmt 结构体的 size 字段，例如通过调用 video_set_format()。

**返回（Returns）**：成功返回 0，出错返回负值。

> 译注（源码核对）：当前实现未初始化时返回-EIO；视频源未设置或fmt->size为0时返回-EINVAL；格式描述符容量不足时返回-ENOMEM。示例先在视频源上设置格式以取得size，再提交给UVC；添加描述符不等于已经启动采集或完成主机格式选择。

<a id="gaec4b7ac54a524724bb29751fd1cafafe"></a>

### 122.3.2\_`uvc\_device\_enable()`

```c
int uvc_device_enable ( const struct device *const uvc_dev)
```

```c
#include <zephyr/usb/class/usbd_uvc.h>
```

完成 UVC 设备实例的配置。

准备 UVC 接口，使其可以使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uvc_dev` | 指向待配置 UVC 设备的指针。 |

**注意（Note）**：必须在 usbd_init 之前调用此函数。

**返回（Returns）**：成功返回 0，出错返回负值。

> 译注（源码核对）：该接口完成类描述符与默认探测参数准备，不替代usbd_init／usbd_enable。当前实现未初始化时返回-EIO，随后各阶段还可能返回描述符或默认探测生成错误。它没有把重复调用作为无操作处理，应遵循初始化顺序。

<a id="ga9c84595e78a2294f1470056199c074ae"></a>

### 122.3.3\_`uvc\_device\_init()`

```c
void uvc_device_init ( const struct device * uvc_dev, const struct device * video_dev )
```

```c
#include <zephyr/usb/class/usbd_uvc.h>
```

初始化视频设备类（Video Device Class）。

设置 UVC 实例处理控制请求（Control Requests）时使用的视频设备。

它会查询该视频设备支持的控制项和帧间隔（Frame Intervals），并用这些信息生成向主机呈现的 USB 描述符。此外，对于主机发给此 uvc_dev 实例的每一种受支持 UVC 控制请求，都会向 video_dev 发出对应的视频 API 控制请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uvc_dev` | 指向待配置 UVC 设备的指针。 |
| `video_dev` | 指向控制请求所发往的视频设备的指针。 |

**注意（Note）**：必须在 uvc_device_enable 之前调用此函数。

> 译注（源码核对）：当前实现保存视频设备指针并据其能力构建控制描述符。重复初始化时只记录警告后返回，返回类型void没有错误码。应先准备好video_dev，再初始化UVC、添加格式、完成UVC配置，最后初始化和启用USB设备栈。

<a id="gad6415b544866cfa15efac2a53c760f2a"></a>

### 122.3.4\_`uvc\_device\_shutdown()`

```c
int uvc_device_shutdown ( const struct device *const uvc_dev)
```

```c
#include <zephyr/usb/class/usbd_uvc.h>
```

撤销 UVC 设备实例的配置。

重置 USB 设备类的配置，使其能够再次启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uvc_dev` | 指向待撤销配置 UVC 设备的指针。 |

**返回（Returns）**：成功返回 0，出错返回负值。

> 译注（源码核对）：当前实现撤销已分配描述符并清除INITIALIZED位，返回0。重新配置仍需执行init、添加格式和enable；此函数不是视频源停止、全部视频缓冲区释放或USB控制器停用的组合接口。

## 122.4\_源码跟踪与使用边界

译注依据保存的[官方UVC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_uvc.h)、[驱动实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_uvc.c)与[设备示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uvc/src/main.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[UVC头文件](../../../include/zephyr/usb/class/usbd_uvc.h)和[实现](../../../subsys/usb/device_next/class/usbd_uvc.c)可用于跟踪，版本可能与网页不同。本批未构建、采集视频或进行USB硬件测试。

<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P121_USBMIDI设备绑定.md) · [返回大纲](大纲.md) · [下一章](P123_USB视频头文件接口.md)
