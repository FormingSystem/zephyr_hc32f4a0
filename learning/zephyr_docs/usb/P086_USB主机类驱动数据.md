---
id: learning.zephyr-docs.usb.api-86
title: USB主机类驱动数据
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbh__class__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_USB主机类驱动数据

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbh__class__data.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 86.1\_阅读说明与来源

译注：本页说明USB主机栈（USB Host Stack）的接口与数据对象。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB主机类实例数据。

```c
#include <zephyr/usb/usbh.h>
```

USB主机类实例数据。

## 86.2\_数据成员（Data Fields）

<a id="r_a5c30d8b884acb177c7351fdca0c3aca6"></a>

```c
const char * name
```

USB主机类实例名称。

相关声明：[name](P086_USB主机类驱动数据.md#a5c30d8b884acb177c7351fdca0c3aca6)。

<a id="r_ab81986dc2d5f95c779999cedfc4d08e2"></a>

```c
struct usb_device * udev
```

指向使用此类的USB设备的指针。

相关声明：[usb_device](P080_USB主机设备对象.md)、[udev](P086_USB主机类驱动数据.md#ab81986dc2d5f95c779999cedfc4d08e2)。

<a id="r_aa4e1255c33954ee65e8855d194564b0e"></a>

```c
uint8_t iface
```

所声明功能的首个接口号。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iface](P086_USB主机类驱动数据.md#aa4e1255c33954ee65e8855d194564b0e)。

<a id="r_a1712aeca7d6d92a27593c9e6d10119d5"></a>

```c
struct usbh_class_api * api
```

指向主机支持类API的指针。

相关声明：[usbh_class_api](P085_USB主机类驱动接口.md)、[api](P086_USB主机类驱动数据.md#a1712aeca7d6d92a27593c9e6d10119d5)。

<a id="r_af5aaa5e6a088eb4b5c06d3fecabbbba2"></a>

```c
void * priv
```

指向私有数据的指针。

相关声明：[priv](P086_USB主机类驱动数据.md#af5aaa5e6a088eb4b5c06d3fecabbbba2)。

## 86.3\_详细说明（Detailed Documentation）

<a id="a1712aeca7d6d92a27593c9e6d10119d5"></a>

### 86.3.1\_`api`

```c
struct usbh_class_api* usbh_class_data::api
```

指向主机支持类API的指针。

<a id="aa4e1255c33954ee65e8855d194564b0e"></a>

### 86.3.2\_`iface`

```c
uint8_t usbh_class_data::iface
```

所声明功能的首个接口号。

> 译注（源码核对）：原注释中“First interface number or claimed function”按功能首接口号理解；当前实现还用USBH_CLASS_IFNUM_DEVICE（0xff）表示整个设备，不能将该值作为普通接口数组下标。

<a id="a5c30d8b884acb177c7351fdca0c3aca6"></a>

### 86.3.3\_`name`

```c
const char* usbh_class_data::name
```

USB主机类实例名称。

<a id="af5aaa5e6a088eb4b5c06d3fecabbbba2"></a>

### 86.3.4\_`priv`

```c
void* usbh_class_data::priv
```

指向私有数据的指针。

<a id="ab81986dc2d5f95c779999cedfc4d08e2"></a>

### 86.3.5\_`udev`

```c
struct usb_device* usbh_class_data::udev
```

指向使用此类的USB设备的指针。

> 译注（源码核对）：实例成功绑定后保存设备指针，移除处理后清空；一个已BOUND的实例会被后续匹配跳过。这个指针不是独立分配或复制出来的设备对象。

## 86.4\_源码跟踪与使用边界

译注依据保存的[官方主机头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbh.h)、[UHC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[生命周期实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_api.c)、[类匹配实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class.c)、[类回调包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class_api.h)、[设备管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_device.c)及[事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[主机头文件](../../../include/zephyr/usb/usbh.h)、[UHC头文件](../../../include/zephyr/drivers/usb/uhc.h)与[主机栈目录](../../../subsys/usb/host)可用于源码跟踪，版本可能与网页不同。本批未构建、运行或操作USB硬件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P085_USB主机类驱动接口.md) · [返回大纲](大纲.md) · [下一章](P087_USB主机类匹配条件.md)
