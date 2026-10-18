---
id: learning.zephyr-docs.usb.api-74
title: USB主机控制器数据
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuhc__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_USB主机控制器数据

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structuhc__data.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 74.1\_阅读说明与来源

译注：本页说明USB主机控制器（USB Host Controller，UHC）的公开声明。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

UHC驱动公共数据结构。

```c
#include <zephyr/drivers/usb/uhc.h>
```

UHC驱动公共数据结构。

每个UHC控制器驱动都必须提供此结构，并将其用作设备的私有数据（device->data）。

## 74.2\_数据成员（Data Fields）

<a id="r_ac2a48d1d6692931807e8985799c5bdb0"></a>

```c
struct uhc_device_caps caps
```

控制器能力。

相关声明：[uhc_device_caps](P075_USB主机控制器能力.md)、[caps](P074_USB主机控制器数据.md#ac2a48d1d6692931807e8985799c5bdb0)。

<a id="r_a08772cdd5b42bd11ca4a06a75df846e9"></a>

```c
struct k_mutex mutex
```

访问驱动的互斥锁（Mutex）。

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[mutex](P074_USB主机控制器数据.md#a08772cdd5b42bd11ca4a06a75df846e9)。

<a id="r_a32eec449ffbe5e6c262c907e6e6b475a"></a>

```c
sys_dlist_t ctrl_xfers
```

控制传输双向链表（Doubly Linked List，dlist）

相关声明：[sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)、[ctrl_xfers](P074_USB主机控制器数据.md#a32eec449ffbe5e6c262c907e6e6b475a)。

<a id="r_ac6214566324740c34a8bba42515d1d32"></a>

```c
sys_dlist_t bulk_xfers
```

批量传输（Bulk Transfer）双向链表

相关声明：[sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)、[bulk_xfers](P074_USB主机控制器数据.md#ac6214566324740c34a8bba42515d1d32)。

<a id="r_afd1a0828a0ca3e397dba09fe38fd8050"></a>

```c
uhc_event_cb_t event_cb
```

将UHC事件提交给上层的回调。

相关声明：[uhc_event_cb_t](P073_USB主机控制器API.md#ga3cda056094ceef79dd62ad9c6852daf9)、[event_cb](P074_USB主机控制器数据.md#afd1a0828a0ca3e397dba09fe38fd8050)。

<a id="r_a9f4904633f530748c8e3b2ac3ad0563f"></a>

```c
const void * event_ctx
```

用于保存上层上下文的不透明指针。

相关声明：[event_ctx](P074_USB主机控制器数据.md#a9f4904633f530748c8e3b2ac3ad0563f)。

<a id="r_a10852f2523cc733541cc9ea51706559f"></a>

```c
atomic_t status
```

USB主机控制器状态。

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[status](P074_USB主机控制器数据.md#a10852f2523cc733541cc9ea51706559f)。

<a id="r_a294120f6cf8563cb9564c51fcf56d883"></a>

```c
void * priv
```

驱动私有数据。

相关声明：[priv](P074_USB主机控制器数据.md#a294120f6cf8563cb9564c51fcf56d883)。

## 74.3\_详细说明（Detailed Documentation）

<a id="ac6214566324740c34a8bba42515d1d32"></a>

### 74.3.1\_`bulk\_xfers`

```c
sys_dlist_t uhc_data::bulk_xfers
```

批量传输（Bulk Transfer）双向链表

<a id="ac2a48d1d6692931807e8985799c5bdb0"></a>

### 74.3.2\_`caps`

```c
struct uhc_device_caps uhc_data::caps
```

控制器能力。

<a id="a32eec449ffbe5e6c262c907e6e6b475a"></a>

### 74.3.3\_`ctrl\_xfers`

```c
sys_dlist_t uhc_data::ctrl_xfers
```

控制传输双向链表（Doubly Linked List，dlist）

> 译注（源码核对）：原字段说明将控制和批量传输分列为两个链表，但当前公共uhc_xfer_append()将对象放入ctrl_xfers；取下一项时优先该链表，再检查bulk_xfers。具体驱动可能自行管理队列，不能据字段名推定调度策略。

<a id="afd1a0828a0ca3e397dba09fe38fd8050"></a>

### 74.3.4\_`event\_cb`

```c
uhc_event_cb_t uhc_data::event_cb
```

将UHC事件提交给上层的回调。

<a id="a9f4904633f530748c8e3b2ac3ad0563f"></a>

### 74.3.5\_`event\_ctx`

```c
const void* uhc_data::event_ctx
```

用于保存上层上下文的不透明指针。

<a id="a08772cdd5b42bd11ca4a06a75df846e9"></a>

### 74.3.6\_`mutex`

```c
struct k_mutex uhc_data::mutex
```

访问驱动的互斥锁（Mutex）。

<a id="a294120f6cf8563cb9564c51fcf56d883"></a>

### 74.3.7\_`priv`

```c
void* uhc_data::priv
```

驱动私有数据。

<a id="a10852f2523cc733541cc9ea51706559f"></a>

### 74.3.8\_`status`

```c
atomic_t uhc_data::status
```

USB主机控制器状态。

## 74.4\_源码跟踪与使用边界

译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/uhc/uhc_common.c)、[虚拟控制器](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/uhc/uhc_virtual.c)和[主机栈事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../include/zephyr/drivers/usb/uhc.h)、[公共实现](../../../drivers/usb/uhc/uhc_common.c)与[主机栈](../../../subsys/usb/host/usbh_core.c)可用于跟踪，版本可能与网页不同。此API仍为实验性接口，本批未编译或运行USB主机固件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P073_USB主机控制器API.md) · [返回大纲](大纲.md) · [下一章](P075_USB主机控制器能力.md)
