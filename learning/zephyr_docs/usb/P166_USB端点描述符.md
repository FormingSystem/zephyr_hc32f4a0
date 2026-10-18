---
id: learning.zephyr-docs.usb.api-166
title: USB端点描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__ep__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第166章\_USB端点描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__ep__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 166.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

USB 标准端点描述符（Standard Endpoint Descriptor）。

```c
#include <zephyr/usb/usb_ch9.h>
```

USB 标准端点描述符（Standard Endpoint Descriptor）。

参见规范中的表 9-13。

## 166.2\_数据成员（Data Fields）

<a id="r_ae75468872ec37d8c986534cd78fce717"></a>

```c
uint8_t bLength
```

描述符长度（Descriptor Length）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P166_USB端点描述符.md#ae75468872ec37d8c986534cd78fce717)。

<a id="r_a21412242cf380750e2623f50b5c294e6"></a>

```c
uint8_t bDescriptorType
```

描述符类型（Descriptor Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P166_USB端点描述符.md#a21412242cf380750e2623f50b5c294e6)。

<a id="r_a60234a9d35e232957672a5bc5573d541"></a>

```c
uint8_t bEndpointAddress
```

端点地址（Endpoint Address）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bEndpointAddress](P166_USB端点描述符.md#a60234a9d35e232957672a5bc5573d541)。

```c
union {
```



<a id="r_a2f408e548b3f3a9f7a3ed3857ba8add3"></a>

```c
uint8_t bmAttributes
```

原始端点属性（Raw Endpoint Attributes）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bmAttributes](P166_USB端点描述符.md#ada1c690dfdee3427f303c04b5825ccca)。

<a id="r_ae3690d6b517c88068359c4021eb9abbd"></a>

```c
struct usb_ep_desc_bmattr Attributes
```

结构化端点属性（Structured Endpoint Attributes）。

相关声明：[usb_ep_desc_bmattr](P171_USB端点属性位域.md)、[Attributes](P166_USB端点描述符.md#a6be879be0aac0c679c9d50bbaa9e6dda)。

<a id="r_a6adb255db6a848c460b018d13ec0e1e6"></a>

```c
};
```



<a id="r_a802ba531354e1d8a1c361af1d0716d82"></a>

```c
uint16_t wMaxPacketSize
```

最大包长（Maximum Packet Size）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wMaxPacketSize](P166_USB端点描述符.md#a802ba531354e1d8a1c361af1d0716d82)。

<a id="r_a6facefd49d301bbe357e1d420583cf1d"></a>

```c
uint8_t bInterval
```

轮询间隔（Polling Interval）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bInterval](P166_USB端点描述符.md#a6facefd49d301bbe357e1d420583cf1d)。

## 166.3\_详细说明（Detailed Documentation）

<a id="a6adb255db6a848c460b018d13ec0e1e6"></a>

### 166.3.1\_`[union]`

```c
union { ... } usb_ep_descriptor
```

> 译注（源码核对）：`bmAttributes` 和 `Attributes` 共用一个匿名联合体。后者由 `usb_ep_desc_bmattr` 拆分传输类型、同步类型、用途及保留位；摘要中的联合体起止行属于同一声明。

<a id="a6be879be0aac0c679c9d50bbaa9e6dda"></a>

### 166.3.2\_`Attributes`

```c
struct usb_ep_desc_bmattr usb_ep_descriptor::Attributes
```

结构化端点属性（Structured Endpoint Attributes）。

<a id="a21412242cf380750e2623f50b5c294e6"></a>

### 166.3.3\_`bDescriptorType`

```c
uint8_t usb_ep_descriptor::bDescriptorType
```

描述符类型（Descriptor Type）。

<a id="a60234a9d35e232957672a5bc5573d541"></a>

### 166.3.4\_`bEndpointAddress`

```c
uint8_t usb_ep_descriptor::bEndpointAddress
```

端点地址（Endpoint Address）。

<a id="a6facefd49d301bbe357e1d420583cf1d"></a>

### 166.3.5\_`bInterval`

```c
uint8_t usb_ep_descriptor::bInterval
```

轮询间隔（Polling Interval）。

<a id="ae75468872ec37d8c986534cd78fce717"></a>

### 166.3.6\_`bLength`

```c
uint8_t usb_ep_descriptor::bLength
```

描述符长度（Descriptor Length）。

<a id="ada1c690dfdee3427f303c04b5825ccca"></a>

### 166.3.7\_`bmAttributes`

```c
uint8_t usb_ep_descriptor::bmAttributes
```

原始端点属性（Raw Endpoint Attributes）。

<a id="a802ba531354e1d8a1c361af1d0716d82"></a>

### 166.3.8\_`wMaxPacketSize`

```c
uint16_t usb_ep_descriptor::wMaxPacketSize
```

最大包长（Maximum Packet Size）。

## 166.4\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P165_USB接口描述符.md) · [返回大纲](大纲.md) · [下一章](P167_USB接口关联描述符.md)
