---
id: learning.zephyr-docs.usb.api-147
title: USB平台能力描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__bos__platform__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第147章\_USB平台能力描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__bos__platform__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 147.1\_阅读说明与来源

译注：本页说明USB二进制设备对象存储（Binary Device Object Store，BOS）及其能力描述符。通用结构由新旧USB设备栈相关代码引用，不因旧版管理入口弃用而自动成为同一套弃用接口。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

BOS 平台能力描述符（Platform Capability Descriptor）。

```c
#include <zephyr/usb/bos.h>
```

BOS 平台能力描述符（Platform Capability Descriptor）。

用于描述由通用唯一标识符（Universally Unique Identifier，UUID）标识的平台专用能力。

## 147.2\_数据成员（Data Fields）

<a id="r_a477ab8e85845e8809ff7f4bd1bcc0f8a"></a>

```c
uint8_t bLength
```

此描述符的大小，以字节为单位（20）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P147_USB平台能力描述符.md#a477ab8e85845e8809ff7f4bd1bcc0f8a)。

<a id="r_a26a748945b0223d369a05ad06a2c6d05"></a>

```c
uint8_t bDescriptorType
```

描述符类型（Descriptor Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P147_USB平台能力描述符.md#a26a748945b0223d369a05ad06a2c6d05)。

<a id="r_a8e8e95a1648e6bba7568c519158de917"></a>

```c
uint8_t bDevCapabilityType
```

设备能力类型（Device Capability Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDevCapabilityType](P147_USB平台能力描述符.md#a8e8e95a1648e6bba7568c519158de917)。

<a id="r_a477719191468cec83d2a92a5d6f1231d"></a>

```c
uint8_t bReserved
```

保留字段，必须为零。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bReserved](P147_USB平台能力描述符.md#a477719191468cec83d2a92a5d6f1231d)。

<a id="r_a09f10af1f29bccdd300be504cd2dda10"></a>

```c
uint8_t PlatformCapabilityUUID [16]
```

平台能力 UUID，16 字节，采用小端序（Little-Endian）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[PlatformCapabilityUUID](P147_USB平台能力描述符.md#a09f10af1f29bccdd300be504cd2dda10)。

## 147.3\_详细说明（Detailed Documentation）

<a id="a26a748945b0223d369a05ad06a2c6d05"></a>

### 147.3.1\_`bDescriptorType`

```c
uint8_t usb_bos_platform_descriptor::bDescriptorType
```

描述符类型（Descriptor Type）。

必须设置为 USB_DESC_DEVICE_CAPABILITY。

<a id="a8e8e95a1648e6bba7568c519158de917"></a>

### 147.3.2\_`bDevCapabilityType`

```c
uint8_t usb_bos_platform_descriptor::bDevCapabilityType
```

设备能力类型（Device Capability Type）。

必须为 USB_BOS_CAPABILITY_PLATFORM。

<a id="a477ab8e85845e8809ff7f4bd1bcc0f8a"></a>

### 147.3.3\_`bLength`

```c
uint8_t usb_bos_platform_descriptor::bLength
```

此描述符的大小，以字节为单位（20）。

> 译注（源码核对）：原文20字节描述通用平台头部本身。实际传输的能力描述符还要附加平台专用数据：官方WebUSB示例用sizeof(usb_bos_platform_descriptor)加sizeof(usb_bos_capability_webusb)，共24字节；Microsoft OS示例对应共28字节。不能将带有扩展数据的bLength仍固定填为20。

<a id="a477719191468cec83d2a92a5d6f1231d"></a>

### 147.3.4\_`bReserved`

```c
uint8_t usb_bos_platform_descriptor::bReserved
```

保留字段，必须为零。

<a id="a09f10af1f29bccdd300be504cd2dda10"></a>

### 147.3.5\_`PlatformCapabilityUUID`

```c
uint8_t usb_bos_platform_descriptor::PlatformCapabilityUUID[16]
```

平台能力 UUID，16 字节，采用小端序（Little-Endian）。

> 译注（源码核对）：应按协议定义的UUID字节布局填写，不能把字符串中的32个十六进制字符当作32字节，也不能把16字节整体任意倒序。官方WebUSB示例将3408b638-09a9-47a0-8bfd-a0768815b665编码为38 B6 08 34 A9 09 A0 47 8B FD A0 76 88 15 B6 65，可对照其分组顺序。

## 147.4\_源码跟踪与使用边界

译注依据保存的[官方BOS头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/bos.h)、[WebUSB能力与请求示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/webusb.h)及[Microsoft OS能力示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/msosv2.h)，摘要见[来源记录](../SOURCES.md)。WebUSB的URL索引与平台能力字段另核对[WebUSB规范](https://usb.spec.whatwg.org/#webusb-platform-capability-descriptor)。本仓库[通用头文件](../../../include/zephyr/usb/bos.h)与[WebUSB示例](../../../samples/subsys/usb/webusb/src/main.c)可用于相对路径源码跟踪，版本可能与网页不同。相关应用见[WebUSB示例译文](P069_WebUSB示例.md)；本批未构建固件、枚举设备或进行USB通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P146_USBBOS描述符.md) · [返回大纲](大纲.md) · [下一章](P148_USB链路电源管理能力.md)
