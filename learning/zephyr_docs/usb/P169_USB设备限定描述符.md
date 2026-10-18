---
id: learning.zephyr-docs.usb.api-169
title: USB设备限定描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__device__qualifier__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第169章\_USB设备限定描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__device__qualifier__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 169.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

USB 设备限定描述符（Device Qualifier Descriptor）。

```c
#include <zephyr/usb/usb_ch9.h>
```

USB 设备限定描述符（Device Qualifier Descriptor）。

参见规范中的表 9-9。

## 169.2\_数据成员（Data Fields）

<a id="r_ab1bf7ff669706ee5370f90d72f2a6856"></a>

```c
uint8_t bLength
```

描述符长度（Descriptor Length）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P169_USB设备限定描述符.md#ab1bf7ff669706ee5370f90d72f2a6856)。

<a id="r_a1547d76b3c2f7599d2621e4c73ef485d"></a>

```c
uint8_t bDescriptorType
```

描述符类型（Descriptor Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P169_USB设备限定描述符.md#a1547d76b3c2f7599d2621e4c73ef485d)。

<a id="r_aabe610da20b0b4ccc9aefdabd3396bf1"></a>

```c
uint16_t bcdUSB
```

USB 规范版本号（USB Specification Release Number）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bcdUSB](P169_USB设备限定描述符.md#aabe610da20b0b4ccc9aefdabd3396bf1)。

<a id="r_aeb3cbfe114aa775d5121a5580dafa16e"></a>

```c
uint8_t bDeviceClass
```

设备类（Device Class）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDeviceClass](P169_USB设备限定描述符.md#aeb3cbfe114aa775d5121a5580dafa16e)。

<a id="r_a9335b5c4955f68463484b55eb480a1fb"></a>

```c
uint8_t bDeviceSubClass
```

设备子类（Device Subclass）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDeviceSubClass](P169_USB设备限定描述符.md#a9335b5c4955f68463484b55eb480a1fb)。

<a id="r_a9665e7509c611a4eaa0345d3f96ec707"></a>

```c
uint8_t bDeviceProtocol
```

设备协议（Device Protocol）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDeviceProtocol](P169_USB设备限定描述符.md#a9665e7509c611a4eaa0345d3f96ec707)。

<a id="r_ad065540e5d99fbd241b0712e601f62ee"></a>

```c
uint8_t bMaxPacketSize0
```

端点零的最大包长（Maximum Packet Size for Endpoint Zero）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bMaxPacketSize0](P169_USB设备限定描述符.md#ad065540e5d99fbd241b0712e601f62ee)。

<a id="r_a4022310ac474e11b6813af8c1f5d093f"></a>

```c
uint8_t bNumConfigurations
```

配置数量（Number of Configurations）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bNumConfigurations](P169_USB设备限定描述符.md#a4022310ac474e11b6813af8c1f5d093f)。

<a id="r_aa1557859c9220ae5fda7d32833845444"></a>

```c
uint8_t bReserved
```

保留字段（Reserved Field）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bReserved](P169_USB设备限定描述符.md#aa1557859c9220ae5fda7d32833845444)。

## 169.3\_详细说明（Detailed Documentation）

<a id="aabe610da20b0b4ccc9aefdabd3396bf1"></a>

### 169.3.1\_`bcdUSB`

```c
uint16_t usb_device_qualifier_descriptor::bcdUSB
```

USB 规范版本号（USB Specification Release Number）。

<a id="a1547d76b3c2f7599d2621e4c73ef485d"></a>

### 169.3.2\_`bDescriptorType`

```c
uint8_t usb_device_qualifier_descriptor::bDescriptorType
```

描述符类型（Descriptor Type）。

<a id="aeb3cbfe114aa775d5121a5580dafa16e"></a>

### 169.3.3\_`bDeviceClass`

```c
uint8_t usb_device_qualifier_descriptor::bDeviceClass
```

设备类（Device Class）。

<a id="a9665e7509c611a4eaa0345d3f96ec707"></a>

### 169.3.4\_`bDeviceProtocol`

```c
uint8_t usb_device_qualifier_descriptor::bDeviceProtocol
```

设备协议（Device Protocol）。

<a id="a9335b5c4955f68463484b55eb480a1fb"></a>

### 169.3.5\_`bDeviceSubClass`

```c
uint8_t usb_device_qualifier_descriptor::bDeviceSubClass
```

设备子类（Device Subclass）。

<a id="ab1bf7ff669706ee5370f90d72f2a6856"></a>

### 169.3.6\_`bLength`

```c
uint8_t usb_device_qualifier_descriptor::bLength
```

描述符长度（Descriptor Length）。

<a id="ad065540e5d99fbd241b0712e601f62ee"></a>

### 169.3.7\_`bMaxPacketSize0`

```c
uint8_t usb_device_qualifier_descriptor::bMaxPacketSize0
```

端点零的最大包长（Maximum Packet Size for Endpoint Zero）。

<a id="a4022310ac474e11b6813af8c1f5d093f"></a>

### 169.3.8\_`bNumConfigurations`

```c
uint8_t usb_device_qualifier_descriptor::bNumConfigurations
```

配置数量（Number of Configurations）。

> 译注（源码核对）：`sreq_get_dev_qualifier()` 在当前为全速（Full Speed，FS）时读取高速（High Speed，HS）设备描述符，反向也一样；此处填入的是另一速率所对应的配置数量。

<a id="aa1557859c9220ae5fda7d32833845444"></a>

### 169.3.9\_`bReserved`

```c
uint8_t usb_device_qualifier_descriptor::bReserved
```

保留字段（Reserved Field）。

> 译注（源码核对）：当前 `sreq_get_dev_qualifier()` 将此字段初始化为 `0U`；原始声明保留，不能把保留字段当成自定义配置空间。

## 169.4\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P168_USB字符串描述符.md) · [返回大纲](大纲.md) · [下一章](P170_USB请求类型位域.md)
