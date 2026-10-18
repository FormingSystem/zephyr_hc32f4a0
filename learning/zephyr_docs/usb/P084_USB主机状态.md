---
id: learning.zephyr-docs.usb.api-84
title: USB主机状态
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbh__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第84章\_USB主机状态

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbh__status.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 84.1\_阅读说明与来源

译注：本页说明USB主机栈（USB Host Stack）的接口与数据对象。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB主机支持状态。

```c
#include <zephyr/usb/usbh.h>
```

USB主机支持状态。

## 84.2\_数据成员（Data Fields）

<a id="r_a89bdc78fa77ab48deecc3670029e8354"></a>

```c
unsigned int initialized: 1
```

USB主机支持已初始化。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[initialized](P084_USB主机状态.md#a89bdc78fa77ab48deecc3670029e8354)。

<a id="r_a456a7050403bb854b4e3a3225bec94b2"></a>

```c
unsigned int enabled: 1
```

USB主机支持已启用。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[enabled](P084_USB主机状态.md#a456a7050403bb854b4e3a3225bec94b2)。

## 84.3\_详细说明（Detailed Documentation）

<a id="a456a7050403bb854b4e3a3225bec94b2"></a>

### 84.3.1\_`enabled`

```c
unsigned int usbh_status::enabled
```

USB主机支持已启用。

> 译注（源码核对）：当前启用判断来自uhc_is_enabled()，公开实现未将结果同步写入这个位域。需要判断驱动状态时遵循相关API约定。

<a id="a89bdc78fa77ab48deecc3670029e8354"></a>

### 84.3.2\_`initialized`

```c
unsigned int usbh_status::initialized
```

USB主机支持已初始化。

> 译注（源码核对）：当前usbh_api.c的初始化判断来自uhc_is_initialized()；这些状态位的声明不等于生命周期实现已对它们维护一致的镜像。

## 84.4\_源码跟踪与使用边界

译注依据保存的[官方主机头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbh.h)、[UHC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[生命周期实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_api.c)、[类匹配实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class.c)、[类回调包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class_api.h)、[设备管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_device.c)及[事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[主机头文件](../../../include/zephyr/usb/usbh.h)、[UHC头文件](../../../include/zephyr/drivers/usb/uhc.h)与[主机栈目录](../../../subsys/usb/host)可用于源码跟踪，版本可能与网页不同。本批未构建、运行或操作USB硬件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P083_USB主机上下文.md) · [返回大纲](大纲.md) · [下一章](P085_USB主机类驱动接口.md)
