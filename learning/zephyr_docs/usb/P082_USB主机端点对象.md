---
id: learning.zephyr-docs.usb.api-82
title: USB主机端点对象
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__host__ep.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_USB主机端点对象

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__host__ep.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 82.1\_阅读说明与来源

译注：本页说明USB主机栈（USB Host Stack）的接口与数据对象。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

```c
#include <zephyr/drivers/usb/uhc.h>
```

## 82.2\_数据成员（Data Fields）

<a id="r_a25e9c4004ab03927476093ed4d167dbd"></a>

```c
struct usb_ep_descriptor * desc
```

指向端点描述符（Endpoint Descriptor）的指针。

相关声明：[usb_ep_descriptor](P166_USB端点描述符.md)、[desc](P082_USB主机端点对象.md#a25e9c4004ab03927476093ed4d167dbd)。

## 82.3\_详细说明（Detailed Documentation）

<a id="a25e9c4004ab03927476093ed4d167dbd"></a>

### 82.3.1\_`desc`

```c
struct usb_ep_descriptor* usb_host_ep::desc
```

指向端点描述符（Endpoint Descriptor）的指针。

> 译注（源码核对）：描述符来自当前设备配置数据；取得指针不增加该配置内存的所有权。配置变化、设备断开或对象释放后，旧指针不可继续使用。

## 82.4\_源码跟踪与使用边界

译注依据保存的[官方主机头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbh.h)、[UHC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[生命周期实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_api.c)、[类匹配实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class.c)、[类回调包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class_api.h)、[设备管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_device.c)及[事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[主机头文件](../../../include/zephyr/usb/usbh.h)、[UHC头文件](../../../include/zephyr/drivers/usb/uhc.h)与[主机栈目录](../../../subsys/usb/host)可用于源码跟踪，版本可能与网页不同。本批未构建、运行或操作USB硬件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P081_USB主机接口对象.md) · [返回大纲](大纲.md) · [下一章](P083_USB主机上下文.md)
