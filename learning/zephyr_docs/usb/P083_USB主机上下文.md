---
id: learning.zephyr-docs.usb.api-83
title: USB主机上下文
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbh__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第83章\_USB主机上下文

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbh__context.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 83.1\_阅读说明与来源

译注：本页说明USB主机栈（USB Host Stack）的接口与数据对象。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB主机支持的运行时上下文（Runtime Context）。

```c
#include <zephyr/usb/usbh.h>
```

USB主机支持的运行时上下文（Runtime Context）。

## 83.2\_数据成员（Data Fields）

<a id="r_ab0896f1266f674ba1dd62a102962f2b6"></a>

```c
const char * name
```

USB设备名称。

相关声明：[name](P083_USB主机上下文.md#ab0896f1266f674ba1dd62a102962f2b6)。

<a id="r_a3fbaf512dd1f68706684b4adf845ee51"></a>

```c
struct k_mutex mutex
```

访问互斥锁。

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[mutex](P083_USB主机上下文.md#a3fbaf512dd1f68706684b4adf845ee51)。

<a id="r_aefdff404508b92733f66142f1c299e01"></a>

```c
const struct device * dev
```

指向USB主机控制器（USB Host Controller，UHC）device结构的指针。

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](P083_USB主机上下文.md#aefdff404508b92733f66142f1c299e01)。

<a id="r_a21ae15801166839d3fce3ecaf634e0f7"></a>

```c
struct usbh_status status
```

USB主机支持的状态。

相关声明：[usbh_status](P084_USB主机状态.md)、[status](P083_USB主机上下文.md#a21ae15801166839d3fce3ecaf634e0f7)。

<a id="r_a2fc9fa080e8d7eb9f6649f4f11b11f88"></a>

```c
sys_dlist_t udevs
```

USB设备列表。

相关声明：[sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)、[udevs](P083_USB主机上下文.md#a2fc9fa080e8d7eb9f6649f4f11b11f88)。

<a id="r_a043d232f5927e2b26a99b0ac3de8717f"></a>

```c
struct usb_device * root
```

USB根设备。

相关声明：[usb_device](P080_USB主机设备对象.md)、[root](P083_USB主机上下文.md#a043d232f5927e2b26a99b0ac3de8717f)。

<a id="r_ac331b6555c6f1cf668ff92e3d092eedc"></a>

```c
struct sys_bitarray * addr_ba
```

记录已分配设备地址的位数组（Bit Array）。

相关声明：[addr_ba](P083_USB主机上下文.md#ac331b6555c6f1cf668ff92e3d092eedc)。

## 83.3\_详细说明（Detailed Documentation）

<a id="ac331b6555c6f1cf668ff92e3d092eedc"></a>

### 83.3.1\_`addr\_ba`

```c
struct sys_bitarray* usbh_context::addr_ba
```

记录已分配设备地址的位数组（Bit Array）。

> 译注（源码核对）：宏建立128位数组，当前分配循环只使用地址1至127；设备释放时清除对应位。位图容量与同时可连接设备数不同，后者还受设备对象池和控制器能力限制。

<a id="aefdff404508b92733f66142f1c299e01"></a>

### 83.3.2\_`dev`

```c
const struct device* usbh_context::dev
```

指向USB主机控制器（USB Host Controller，UHC）device结构的指针。

<a id="a3fbaf512dd1f68706684b4adf845ee51"></a>

### 83.3.3\_`mutex`

```c
struct k_mutex usbh_context::mutex
```

访问互斥锁。

<a id="ab0896f1266f674ba1dd62a102962f2b6"></a>

### 83.3.4\_`name`

```c
const char* usbh_context::name
```

USB设备名称。

> 译注（源码核对）：原注释称USB设备名称，但USBH_CONTROLLER_DEFINE实际将上下文变量名字符串化写入此字段；它不是所连接外设的iProduct字符串。

<a id="a043d232f5927e2b26a99b0ac3de8717f"></a>

### 83.3.5\_`root`

```c
struct usb_device* usbh_context::root
```

USB根设备。

> 译注（源码核对）：当前连接流程在root为空时把新设备设为根设备，并将其level设为1；此指针表示栈管理的设备对象，不是UHC驱动device对象。

<a id="a21ae15801166839d3fce3ecaf634e0f7"></a>

### 83.3.6\_`status`

```c
struct usbh_status usbh_context::status
```

USB主机支持的状态。

> 译注（源码核对）：当前公开生命周期实现查询UHC的初始化／启用位，并未同步更新这里的两个位域。不要绕过生命周期接口，单凭本字段推断控制器实际状态。

<a id="a2fc9fa080e8d7eb9f6649f4f11b11f88"></a>

### 83.3.7\_`udevs`

```c
sys_dlist_t usbh_context::udevs
```

USB设备列表。

## 83.4\_源码跟踪与使用边界

译注依据保存的[官方主机头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbh.h)、[UHC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[生命周期实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_api.c)、[类匹配实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class.c)、[类回调包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class_api.h)、[设备管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_device.c)及[事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[主机头文件](../../../include/zephyr/usb/usbh.h)、[UHC头文件](../../../include/zephyr/drivers/usb/uhc.h)与[主机栈目录](../../../subsys/usb/host)可用于源码跟踪，版本可能与网页不同。本批未构建、运行或操作USB硬件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P082_USB主机端点对象.md) · [返回大纲](大纲.md) · [下一章](P084_USB主机状态.md)
