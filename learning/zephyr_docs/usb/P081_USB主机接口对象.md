---
id: learning.zephyr-docs.usb.api-81
title: USB主机接口对象
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__host__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_USB主机接口对象

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__host__interface.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 81.1\_阅读说明与来源

译注：本页说明USB主机栈（USB Host Stack）的接口与数据对象。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

```c
#include <zephyr/drivers/usb/uhc.h>
```

## 81.2\_数据成员（Data Fields）

<a id="r_aa0170523367f9e1459a9ba897c0d88bf"></a>

```c
struct usb_desc_header * dhp
```

指向接口描述符（Interface Descriptor）的指针。

相关声明：[usb_desc_header](P161_USB通用描述符头.md)、[dhp](P081_USB主机接口对象.md#aa0170523367f9e1459a9ba897c0d88bf)。

<a id="r_a8241bb80e15d8434802aad81ba0fc810"></a>

```c
struct usb_association_descriptor * iad
```

指向接口关联描述符（Interface Association Descriptor，IAD）的指针，如有。

相关声明：[usb_association_descriptor](P167_USB接口关联描述符.md)、[iad](P081_USB主机接口对象.md#a8241bb80e15d8434802aad81ba0fc810)。

<a id="r_a4405cdfb6aa6fbbcd2ac27148b9ebea6"></a>

```c
uint8_t alternate
```

此接口已选择的备用设置（Alternate Setting）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[alternate](P081_USB主机接口对象.md#a4405cdfb6aa6fbbcd2ac27148b9ebea6)。

## 81.3\_详细说明（Detailed Documentation）

<a id="a4405cdfb6aa6fbbcd2ac27148b9ebea6"></a>

### 81.3.1\_`alternate`

```c
uint8_t usb_host_interface::alternate
```

此接口已选择的备用设置（Alternate Setting）。

> 译注（源码核对）：备用设置与接口号是不同字段。同一接口切换备用设置可能改变可用端点，不能仅修改此缓存值就视为已经向设备提交Set Interface请求。

<a id="aa0170523367f9e1459a9ba897c0d88bf"></a>

### 81.3.2\_`dhp`

```c
struct usb_desc_header* usb_host_interface::dhp
```

指向接口描述符（Interface Descriptor）的指针。

> 译注（源码核对）：使用通用usb_desc_header指针保存接口描述符位置，读取具体字段前仍需按描述符类型解释；其内存生命周期从属于设备当前配置描述符。

<a id="a8241bb80e15d8434802aad81ba0fc810"></a>

### 81.3.3\_`iad`

```c
struct usb_association_descriptor* usb_host_interface::iad
```

指向接口关联描述符（Interface Association Descriptor，IAD）的指针，如有。

> 译注（源码核对）：多接口功能可通过IAD归组；类匹配时从IAD取功能类／子类／协议及bFirstInterface。没有IAD时从接口描述符取接口类代码与bInterfaceNumber。

## 81.4\_源码跟踪与使用边界

译注依据保存的[官方主机头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbh.h)、[UHC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[生命周期实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_api.c)、[类匹配实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class.c)、[类回调包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class_api.h)、[设备管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_device.c)及[事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[主机头文件](../../../include/zephyr/usb/usbh.h)、[UHC头文件](../../../include/zephyr/drivers/usb/uhc.h)与[主机栈目录](../../../subsys/usb/host)可用于源码跟踪，版本可能与网页不同。本批未构建、运行或操作USB硬件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P080_USB主机设备对象.md) · [返回大纲](大纲.md) · [下一章](P082_USB主机端点对象.md)
