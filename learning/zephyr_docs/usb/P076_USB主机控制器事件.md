---
id: learning.zephyr-docs.usb.api-76
title: USB主机控制器事件
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuhc__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_USB主机控制器事件

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structuhc__event.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 76.1\_阅读说明与来源

译注：本页说明USB主机控制器（USB Host Controller，UHC）的公开声明。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB主机控制器事件。

```c
#include <zephyr/drivers/usb/uhc.h>
```

USB主机控制器事件。

来自UHC驱动的所有事件使用的公共结构；事件通过消息队列以及上层在控制器初始化（uhc_init）时提供的回调（uhc_event_cb_t）传递到上层。

## 76.2\_数据成员（Data Fields）

<a id="r_acd04587fac14f9a8a91b75642f5b2e82"></a>

```c
sys_snode_t node
```

用于消息队列的单向链表（Singly Linked List，slist）节点

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](P076_USB主机控制器事件.md#acd04587fac14f9a8a91b75642f5b2e82)。

<a id="r_a30fddbbe0f15a16320fba3cb4fd81d84"></a>

```c
enum uhc_event_type type
```

事件类型。

相关声明：[uhc_event_type](P073_USB主机控制器API.md#gabaf69c1e69fe0fb3d912b92daf8754eb)、[type](P076_USB主机控制器事件.md#a30fddbbe0f15a16320fba3cb4fd81d84)。

```c
union {
```



<a id="r_aa2fb3a2e498f69cd470b6c3eba17481e"></a>

```c
int status
```

事件状态值，如有。

相关声明：[status](P076_USB主机控制器事件.md#a5d7e1cc1bcb25e10f009ac3a8acd94b6)。

<a id="r_af420fda4eacf0ddbf4a7a39c3726555d"></a>

```c
struct uhc_transfer * xfer
```

指向请求的指针，仅供UHC_EVT_EP_REQUEST使用。

相关声明：[uhc_transfer](P077_USB主机传输结构.md)、[xfer](P076_USB主机控制器事件.md#a03f3cebee6edfaf620a98c198a70dbd0)。

<a id="r_a2b9e097fbb376dc33de491e103d18e8d"></a>

```c
};
```



<a id="r_a055be3fd47e16bc48498163be3e55d09"></a>

```c
const struct device * dev
```

指向控制器device结构体的指针。

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](P076_USB主机控制器事件.md#a055be3fd47e16bc48498163be3e55d09)。

## 76.3\_详细说明（Detailed Documentation）

<a id="a2b9e097fbb376dc33de491e103d18e8d"></a>

### 76.3.1\_`[union]`

```c
union { ... } uhc_event
```

> 译注（源码核对）：status和xfer共享同一联合体存储；先检查type再读取对应成员，不能同时解释两者。

<a id="a055be3fd47e16bc48498163be3e55d09"></a>

### 76.3.2\_`dev`

```c
const struct device* uhc_event::dev
```

指向控制器device结构体的指针。

<a id="acd04587fac14f9a8a91b75642f5b2e82"></a>

### 76.3.3\_`node`

```c
sys_snode_t uhc_event::node
```

用于消息队列的单向链表（Singly Linked List，slist）节点

> 译注（源码核对）：这是原结构保留的链表节点说明；当前主机栈使用k_msgq按值复制事件，并分别排队总线事件和端点完成事件，不通过这个node串链。

<a id="a5d7e1cc1bcb25e10f009ac3a8acd94b6"></a>

### 76.3.4\_`status`

```c
int uhc_event::status
```

事件状态值，如有。

<a id="a30fddbbe0f15a16320fba3cb4fd81d84"></a>

### 76.3.5\_`type`

```c
enum uhc_event_type uhc_event::type
```

事件类型。

<a id="a03f3cebee6edfaf620a98c198a70dbd0"></a>

### 76.3.6\_`xfer`

```c
struct uhc_transfer* uhc_event::xfer
```

指向请求的指针，仅供UHC_EVT_EP_REQUEST使用。

> 译注（源码核对）：仅用于端点请求事件，完成状态从xfer->err取得，不能读取同一联合体中的event.status。当前公共完成函数先移除队列节点、清除queued并设置err，再发事件并释放队列持有的引用。上层须另按所有权约定保证其事件处理期间对象有效。

## 76.4\_源码跟踪与使用边界

译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/uhc/uhc_common.c)、[虚拟控制器](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/uhc/uhc_virtual.c)和[主机栈事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../include/zephyr/drivers/usb/uhc.h)、[公共实现](../../../drivers/usb/uhc/uhc_common.c)与[主机栈](../../../subsys/usb/host/usbh_core.c)可用于跟踪，版本可能与网页不同。此API仍为实验性接口，本批未编译或运行USB主机固件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P075_USB主机控制器能力.md) · [返回大纲](大纲.md) · [下一章](P077_USB主机传输结构.md)
