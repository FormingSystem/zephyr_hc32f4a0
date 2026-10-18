---
id: learning.zephyr-docs.usb.api-163
title: USB设备描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__device__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第163章\_USB设备描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__device__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 163.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

USB 标准设备描述符（Standard Device Descriptor）。

```c
#include <zephyr/usb/usb_ch9.h>
```

USB 标准设备描述符（Standard Device Descriptor）。

参见规范中的表 9-8。

## 163.2\_数据成员（Data Fields）

<a id="r_af3f980ad55af3fd6c222a8802996ab63"></a>

```c
uint8_t bLength
```

描述符长度（Descriptor Length）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P163_USB设备描述符.md#af3f980ad55af3fd6c222a8802996ab63)。

<a id="r_ad1ba08da6ad5b6023f1d0d1461daab7d"></a>

```c
uint8_t bDescriptorType
```

描述符类型（Descriptor Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P163_USB设备描述符.md#ad1ba08da6ad5b6023f1d0d1461daab7d)。

<a id="r_aa400edb6c3183d4922411cdaf980b84e"></a>

```c
uint16_t bcdUSB
```

USB 规范版本号（USB Specification Release Number）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bcdUSB](P163_USB设备描述符.md#aa400edb6c3183d4922411cdaf980b84e)。

<a id="r_aa657267e1d9762b7d2ed3eb60a78d9ad"></a>

```c
uint8_t bDeviceClass
```

设备类（Device Class）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDeviceClass](P163_USB设备描述符.md#aa657267e1d9762b7d2ed3eb60a78d9ad)。

<a id="r_aecfbe730bc3eeccc9c4b5fd17f5f3c3c"></a>

```c
uint8_t bDeviceSubClass
```

设备子类（Device Subclass）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDeviceSubClass](P163_USB设备描述符.md#aecfbe730bc3eeccc9c4b5fd17f5f3c3c)。

<a id="r_a56829af76e57a6ea4fc621b52a0664f8"></a>

```c
uint8_t bDeviceProtocol
```

设备协议（Device Protocol）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDeviceProtocol](P163_USB设备描述符.md#a56829af76e57a6ea4fc621b52a0664f8)。

<a id="r_ac7f47eb197506ac5c555bb4f2fe82d32"></a>

```c
uint8_t bMaxPacketSize0
```

端点零的最大包长（Maximum Packet Size for Endpoint Zero）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bMaxPacketSize0](P163_USB设备描述符.md#ac7f47eb197506ac5c555bb4f2fe82d32)。

<a id="r_a043126e48bebbab536540e44428b6b4f"></a>

```c
uint16_t idVendor
```

厂商标识（Vendor ID，VID）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[idVendor](P163_USB设备描述符.md#a043126e48bebbab536540e44428b6b4f)。

<a id="r_a70d5ecc7bad486b8a8840d86aa151579"></a>

```c
uint16_t idProduct
```

产品标识（Product ID，PID）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[idProduct](P163_USB设备描述符.md#a70d5ecc7bad486b8a8840d86aa151579)。

<a id="r_a41416aa4a49999d2f3f0f67bdc5fa7da"></a>

```c
uint16_t bcdDevice
```

设备版本号（Device Release Number）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bcdDevice](P163_USB设备描述符.md#a41416aa4a49999d2f3f0f67bdc5fa7da)。

<a id="r_ad082330020575944b8471459b816cb40"></a>

```c
uint8_t iManufacturer
```

制造商字符串索引（Manufacturer String Index）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iManufacturer](P163_USB设备描述符.md#ad082330020575944b8471459b816cb40)。

<a id="r_acb90b91c59e65adbcc21949cf0f486f7"></a>

```c
uint8_t iProduct
```

产品字符串索引（Product String Index）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iProduct](P163_USB设备描述符.md#acb90b91c59e65adbcc21949cf0f486f7)。

<a id="r_a105d91b68091e61c9b13ea673fb98eaf"></a>

```c
uint8_t iSerialNumber
```

序列号字符串索引（Serial Number String Index）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iSerialNumber](P163_USB设备描述符.md#a105d91b68091e61c9b13ea673fb98eaf)。

<a id="r_a603204b0517e9ece9bc0d8476b2a7cdc"></a>

```c
uint8_t bNumConfigurations
```

配置数量（Number of Configurations）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bNumConfigurations](P163_USB设备描述符.md#a603204b0517e9ece9bc0d8476b2a7cdc)。

## 163.3\_详细说明（Detailed Documentation）

<a id="a41416aa4a49999d2f3f0f67bdc5fa7da"></a>

### 163.3.1\_`bcdDevice`

```c
uint16_t usb_device_descriptor::bcdDevice
```

设备版本号（Device Release Number）。

<a id="aa400edb6c3183d4922411cdaf980b84e"></a>

### 163.3.2\_`bcdUSB`

```c
uint16_t usb_device_descriptor::bcdUSB
```

USB 规范版本号（USB Specification Release Number）。

> 译注（源码核对）：`bcdUSB` 表示 USB 规范版本；`bcdDevice` 表示设备版本。它们在原声明中都是 `uint16_t`，但含义不同。[USB_BCD_DRN 宏](P172_USB标准请求与描述符常量.md)默认用 Zephyr 内核主、次版本生成设备版本编码；这种默认生成方式不会把 `bcdDevice` 变成 USB 规范版本。

<a id="ad1ba08da6ad5b6023f1d0d1461daab7d"></a>

### 163.3.3\_`bDescriptorType`

```c
uint8_t usb_device_descriptor::bDescriptorType
```

描述符类型（Descriptor Type）。

<a id="aa657267e1d9762b7d2ed3eb60a78d9ad"></a>

### 163.3.4\_`bDeviceClass`

```c
uint8_t usb_device_descriptor::bDeviceClass
```

设备类（Device Class）。

<a id="a56829af76e57a6ea4fc621b52a0664f8"></a>

### 163.3.5\_`bDeviceProtocol`

```c
uint8_t usb_device_descriptor::bDeviceProtocol
```

设备协议（Device Protocol）。

<a id="aecfbe730bc3eeccc9c4b5fd17f5f3c3c"></a>

### 163.3.6\_`bDeviceSubClass`

```c
uint8_t usb_device_descriptor::bDeviceSubClass
```

设备子类（Device Subclass）。

<a id="af3f980ad55af3fd6c222a8802996ab63"></a>

### 163.3.7\_`bLength`

```c
uint8_t usb_device_descriptor::bLength
```

描述符长度（Descriptor Length）。

<a id="ac7f47eb197506ac5c555bb4f2fe82d32"></a>

### 163.3.8\_`bMaxPacketSize0`

```c
uint8_t usb_device_descriptor::bMaxPacketSize0
```

端点零的最大包长（Maximum Packet Size for Endpoint Zero）。

<a id="a603204b0517e9ece9bc0d8476b2a7cdc"></a>

### 163.3.9\_`bNumConfigurations`

```c
uint8_t usb_device_descriptor::bNumConfigurations
```

配置数量（Number of Configurations）。

<a id="a70d5ecc7bad486b8a8840d86aa151579"></a>

### 163.3.10\_`idProduct`

```c
uint16_t usb_device_descriptor::idProduct
```

产品标识（Product ID，PID）。

<a id="a043126e48bebbab536540e44428b6b4f"></a>

### 163.3.11\_`idVendor`

```c
uint16_t usb_device_descriptor::idVendor
```

厂商标识（Vendor ID，VID）。

<a id="ad082330020575944b8471459b816cb40"></a>

### 163.3.12\_`iManufacturer`

```c
uint8_t usb_device_descriptor::iManufacturer
```

制造商字符串索引（Manufacturer String Index）。

<a id="acb90b91c59e65adbcc21949cf0f486f7"></a>

### 163.3.13\_`iProduct`

```c
uint8_t usb_device_descriptor::iProduct
```

产品字符串索引（Product String Index）。

<a id="a105d91b68091e61c9b13ea673fb98eaf"></a>

### 163.3.14\_`iSerialNumber`

```c
uint8_t usb_device_descriptor::iSerialNumber
```

序列号字符串索引（Serial Number String Index）。

## 163.4\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P162_USB类专用描述符头.md) · [返回大纲](大纲.md) · [下一章](P164_USB配置描述符.md)
