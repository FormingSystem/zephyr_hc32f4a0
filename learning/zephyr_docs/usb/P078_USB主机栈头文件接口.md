---
id: learning.zephyr-docs.usb.api-78
title: USB主机栈头文件接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbh_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_USB主机栈头文件接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbh_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 78.1\_阅读说明与来源

译注：本页说明USB主机栈（USB Host Stack）的接口与数据对象。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

> 译注（原文名称）：usbh.h的文件概述误写为USB设备栈，下面按原文保留；其宏、类型与接口实际属于USB主机栈，详细接口见[USB主机核心API](P079_USB主机核心API.md)。

新版实验性USB设备栈API和数据结构。

```c
#include <stdint.h>
```

```c
#include <zephyr/device.h>
```

```c
#include <zephyr/net_buf.h>
```

```c
#include <zephyr/sys/util.h>
```

```c
#include <zephyr/sys/dlist.h>
```

```c
#include <zephyr/sys/bitarray.h>
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

```c
#include <zephyr/sys/iterable_sections.h>
```

新版实验性USB设备栈API和数据结构。

此文件包含USB设备栈API和数据结构。

## 78.2\_数据结构（Data Structures）

<a id="r_usbh_5Fstatus"></a>

```c
struct usbh_status
```

USB主机支持状态。

相关声明：[usbh_status](P084_USB主机状态.md)。

<a id="r_usbh_5Fcontext"></a>

```c
struct usbh_context
```

USB主机支持的运行时上下文（Runtime Context）。

相关声明：[usbh_context](P083_USB主机上下文.md)。

<a id="r_usbh_5Fclass_5Ffilter"></a>

```c
struct usbh_class_filter
```

与匹配特定类有关的设备信息。

相关声明：[usbh_class_filter](P087_USB主机类匹配条件.md)。

<a id="r_usbh_5Fclass_5Fapi"></a>

```c
struct usbh_class_api
```

USB主机类实例API。

相关声明：[usbh_class_api](P085_USB主机类驱动接口.md)。

<a id="r_usbh_5Fclass_5Fdata"></a>

```c
struct usbh_class_data
```

USB主机类实例数据。

相关声明：[usbh_class_data](P086_USB主机类驱动数据.md)。

## 78.3\_宏定义（Macros）

<a id="r_ga0a8885f9c6e8371ccc02ce191d010010"></a>

```c
#define USBH_CONTROLLER_DEFINE(device_name, uhc_dev)
```



相关声明：[USBH_CONTROLLER_DEFINE](P079_USB主机核心API.md#ga0a8885f9c6e8371ccc02ce191d010010)。

<a id="r_gac517efa196831699a3fc261453dfe16f"></a>

```c
#define USBH_DEFINE_CLASS(class_name, class_api, class_priv, filt)
```

定义USB主机支持的类数据。

相关声明：[USBH_DEFINE_CLASS](P079_USB主机核心API.md#gac517efa196831699a3fc261453dfe16f)。

## 78.4\_函数（Functions）

<a id="r_ga9a0b6b3d13573de570a95985450fa869"></a>

```c
int usbh_init (struct usbh_context *uhs_ctx)
```

初始化USB主机支持。

相关声明：[usbh_init](P079_USB主机核心API.md#ga9a0b6b3d13573de570a95985450fa869)、[usbh_context](P083_USB主机上下文.md)。

<a id="r_ga799fa25976930bb2ec39f351f91321ff"></a>

```c
int usbh_enable (struct usbh_context *uhs_ctx)
```

启用USB主机支持及类实例。

相关声明：[usbh_enable](P079_USB主机核心API.md#ga799fa25976930bb2ec39f351f91321ff)、[usbh_context](P083_USB主机上下文.md)。

<a id="r_ga9f5874fb7d02f323f389b079a677372f"></a>

```c
int usbh_disable (struct usbh_context *uhs_ctx)
```

停用USB主机支持。

相关声明：[usbh_disable](P079_USB主机核心API.md#ga9f5874fb7d02f323f389b079a677372f)、[usbh_context](P083_USB主机上下文.md)。

<a id="r_gafa107bce1b2c0af5618f5cc6345a17e2"></a>

```c
int usbh_shutdown (struct usbh_context *const uhs_ctx)
```

关闭USB主机支持。

相关声明：[usbh_shutdown](P079_USB主机核心API.md#gafa107bce1b2c0af5618f5cc6345a17e2)、[usbh_context](P083_USB主机上下文.md)。

## 78.5\_源码跟踪与使用边界

译注依据保存的[官方主机头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbh.h)、[UHC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[生命周期实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_api.c)、[类匹配实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class.c)、[类回调包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class_api.h)、[设备管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_device.c)及[事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[主机头文件](../../../include/zephyr/usb/usbh.h)、[UHC头文件](../../../include/zephyr/drivers/usb/uhc.h)与[主机栈目录](../../../subsys/usb/host)可用于源码跟踪，版本可能与网页不同。本批未构建、运行或操作USB硬件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>

[上一章](P077_USB主机传输结构.md) · [返回大纲](大纲.md) · [下一章](P079_USB主机核心API.md)
