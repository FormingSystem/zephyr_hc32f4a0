---
id: learning.zephyr-docs.usb.api-17
title: USB设备消息结构
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__msg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_USB设备消息结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__msg.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 17.1\_阅读说明与来源

译注：配合[USB设备支持](P002_USB设备支持.md)与[设备栈API说明](P014_USB设备栈API说明.md)阅读。这里翻译新版设备栈核心接口、通知消息及其数据结构；旧版 usb_enable() 接口另见旧版指南。函数参数、返回值和原始宏定义按保存的官方页面保留，源码差异明确标为译注。

本组：[USB设备核心API](P015_USB设备核心API.md) · [USB设备消息API](P016_USB设备消息API.md) · [USB设备消息结构](P017_USB设备消息结构.md)。

USB 设备消息（Message）。

```c
#include <zephyr/usb/usbd_msg.h>
```

USB 设备消息（Message）。

## 17.2\_数据成员（Data Fields）

<a id="r_a37b6c815edc24c8aed291fac7c765abe"></a>

```c
enum usbd_msg_type type
```

消息类型。

相关声明：[usbd_msg_type](P016_USB设备消息API.md#gaa9163408c0006825575a919322f25f56)、[type](P017_USB设备消息结构.md#a37b6c815edc24c8aed291fac7c765abe)。

```c
union {
```



<a id="r_a83e035c662ba3405055746da57dd11a3"></a>

```c
int status
```



相关声明：[status](P017_USB设备消息结构.md#ad3cc8990c42917871981f2f810a2d7e7)。

<a id="r_a5f39d88fe359712fc4974ae85d09fe0c"></a>

```c
const struct device * dev
```



相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](P017_USB设备消息结构.md#ab75e8dfe889902f536367c0ef15410f8)。

<a id="r_acd43f383745512c420f108eef37e64bf"></a>

```c
};
```

消息状态、值或数据。

## 17.3\_详细说明（Detailed Documentation）

<a id="acd43f383745512c420f108eef37e64bf"></a>

### `[union]`

```c
union { ... } usbd_msg
```

消息状态、值或数据。

> 译注（源码核对）：status 和 dev 共用联合体（Union）存储空间，不是两份同时有效的载荷。应先按 type 确定消息含义，再读取对应成员；发布 simple 消息时填写 status，发布 device 消息时填写 dev。

<a id="ab75e8dfe889902f536367c0ef15410f8"></a>

### `dev`

```c
const struct device* usbd_msg::dev
```

<a id="ad3cc8990c42917871981f2f810a2d7e7"></a>

### `status`

```c
int usbd_msg::status
```

<a id="a37b6c815edc24c8aed291fac7c765abe"></a>

### `type`

```c
enum usbd_msg_type usbd_msg::type
```

消息类型。

## 17.4\_相关源码与使用边界

本仓库的[核心头文件](../../../include/zephyr/usb/usbd.h)、[消息头文件](../../../include/zephyr/usb/usbd_msg.h)、[类注册实现](../../../subsys/usb/device_next/usbd_class.c)、[设备生命周期实现](../../../subsys/usb/device_next/usbd_device.c)与[消息投递实现](../../../subsys/usb/device_next/usbd_msg.c)可用于源码跟踪，版本可能与官网 latest 不同。译注核对依据为保存的[官方核心头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[消息定义](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd_msg.h)、[类实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class.c)、[设备实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_device.c)、[配置实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_config.c)与[消息实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_msg.c)，摘要见[来源记录](../SOURCES.md)。本批没有构建或运行USB固件，也未进行实板验证。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P016_USB设备消息API.md) · [返回大纲](大纲.md) · [下一章](P018_USB字符串描述符数据.md)
