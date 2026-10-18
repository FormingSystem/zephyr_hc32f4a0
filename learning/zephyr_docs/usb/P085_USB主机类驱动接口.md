---
id: learning.zephyr-docs.usb.api-85
title: USB主机类驱动接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbh__class__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_USB主机类驱动接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbh__class__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 85.1\_阅读说明与来源

译注：本页说明USB主机栈（USB Host Stack）的接口与数据对象。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB主机类实例API。

```c
#include <zephyr/usb/usbh.h>
```

USB主机类实例API。

## 85.2\_数据成员（Data Fields）

<a id="r_aa589062f79f6ce4773b97be830061631"></a>

```c
int(* init )(struct usbh_class_data *const c_data)
```

主机初始化处理函数，在任何设备连接之前调用。

相关声明：[init](P085_USB主机类驱动接口.md#aa589062f79f6ce4773b97be830061631)、[usbh_class_data](P086_USB主机类驱动数据.md)。

<a id="r_af8c42e60c7110f971d99cb36fb8c50f8"></a>

```c
int(* completion_cb )(struct usbh_class_data *const c_data, struct uhc_transfer *const xfer)
```

请求完成处理函数。

相关声明：[completion_cb](P085_USB主机类驱动接口.md#af8c42e60c7110f971d99cb36fb8c50f8)、[usbh_class_data](P086_USB主机类驱动数据.md)、[uhc_transfer](P077_USB主机传输结构.md)。

<a id="r_ac285cd96fbcdb36e689e71d6343afabd"></a>

```c
int(* probe )(struct usbh_class_data *const c_data, struct usb_device *const udev, const uint8_t iface)
```

设备连接处理函数。

相关声明：[probe](P085_USB主机类驱动接口.md#ac285cd96fbcdb36e689e71d6343afabd)、[usbh_class_data](P086_USB主机类驱动数据.md)、[usb_device](P080_USB主机设备对象.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_affc96d2f5cfc0759d53c939a40ef4b90"></a>

```c
int(* removed )(struct usbh_class_data *const c_data)
```

设备移除处理函数。

相关声明：[removed](P085_USB主机类驱动接口.md#affc96d2f5cfc0759d53c939a40ef4b90)、[usbh_class_data](P086_USB主机类驱动数据.md)。

<a id="r_ac9ba5ead8de356de9852f366a2d2509b"></a>

```c
int(* suspended )(struct usbh_class_data *const c_data)
```

总线挂起处理函数，可选。

相关声明：[suspended](P085_USB主机类驱动接口.md#ac9ba5ead8de356de9852f366a2d2509b)、[usbh_class_data](P086_USB主机类驱动数据.md)。

<a id="r_a9758f521dbcaf4d04469e2e6d1e02792"></a>

```c
int(* resumed )(struct usbh_class_data *const c_data)
```

总线恢复处理函数，可选。

相关声明：[resumed](P085_USB主机类驱动接口.md#a9758f521dbcaf4d04469e2e6d1e02792)、[usbh_class_data](P086_USB主机类驱动数据.md)。

## 85.3\_详细说明（Detailed Documentation）

<a id="af8c42e60c7110f971d99cb36fb8c50f8"></a>

### 85.3.1\_`completion\_cb`

```c
int(* usbh_class_api::completion_cb) (struct usbh_class_data *const c_data, struct uhc_transfer *const xfer)
```

请求完成处理函数。

> 译注（源码核对）：此回调原型接收类数据和完成传输。包装在未提供回调时返回-ENOTSUP；实际传输完成还需通过主机请求回调路径转发，声明一个回调指针不等于所有UHC完成事件都会自动交给该类。缓冲与传输对象的释放责任见UHC传输参考。

<a id="aa589062f79f6ce4773b97be830061631"></a>

### 85.3.2\_`init`

```c
int(* usbh_class_api::init) (struct usbh_class_data *const c_data)
```

主机初始化处理函数，在任何设备连接之前调用。

> 译注（源码核对）：当前类初始化包装在缺少init回调时返回-ENOTSUP；初始化失败的实例被置为ERROR，随后不会作为空闲实例参与匹配。初始化阶段来自主机子系统预初始化，不是外设每次插入。

<a id="ac285cd96fbcdb36e689e71d6343afabd"></a>

### 85.3.3\_`probe`

```c
int(* usbh_class_api::probe) (struct usbh_class_data *const c_data, struct usb_device *const udev, const uint8_t iface)
```

设备连接处理函数。

> 译注（源码核对）：先通过字段过滤才调用此回调。返回非零会继续尝试后续空闲实例，返回0才将实例标记为BOUND并填写c_data->udev及iface。因此在probe中应使用传入的udev和iface，不假定这两个成员已由框架填写。iface可为0xff，表示匹配整个设备；否则是接口号或功能首接口号。

<a id="affc96d2f5cfc0759d53c939a40ef4b90"></a>

### 85.3.4\_`removed`

```c
int(* usbh_class_api::removed) (struct usbh_class_data *const c_data)
```

设备移除处理函数。

> 译注（源码核对）：当前移除流程持有设备互斥锁后调用对应实例的removed。返回0则实例回到IDLE；返回非零则进入ERROR；两种情况都会清空c_data->udev。缺少removed回调的包装返回-ENOTSUP，不等于自动清理成功。

<a id="a9758f521dbcaf4d04469e2e6d1e02792"></a>

### 85.3.5\_`resumed`

```c
int(* usbh_class_api::resumed) (struct usbh_class_data *const c_data)
```

总线恢复处理函数，可选。

> 译注（源码核对）：包装允许缺省此回调并返回0。当前主机核心的UHC_EVT_RESUMED分支仅记录日志；具体分发行为需随所用版本核对。

<a id="ac9ba5ead8de356de9852f366a2d2509b"></a>

### 85.3.6\_`suspended`

```c
int(* usbh_class_api::suspended) (struct usbh_class_data *const c_data)
```

总线挂起处理函数，可选。

> 译注（源码核对）：包装允许缺省此回调并返回0。当前主机核心处理UHC_EVT_SUSPENDED时仅记录日志；不能仅因结构体含此成员就假定该事件一定会分发到所有类实例。

## 85.4\_源码跟踪与使用边界

译注依据保存的[官方主机头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbh.h)、[UHC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[生命周期实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_api.c)、[类匹配实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class.c)、[类回调包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class_api.h)、[设备管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_device.c)及[事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[主机头文件](../../../include/zephyr/usb/usbh.h)、[UHC头文件](../../../include/zephyr/drivers/usb/uhc.h)与[主机栈目录](../../../subsys/usb/host)可用于源码跟踪，版本可能与网页不同。本批未构建、运行或操作USB硬件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P084_USB主机状态.md) · [返回大纲](大纲.md) · [下一章](P086_USB主机类驱动数据.md)
