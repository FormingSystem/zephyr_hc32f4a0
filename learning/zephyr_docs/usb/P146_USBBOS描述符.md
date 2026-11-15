---
id: learning.zephyr-docs.usb.api-146
title: USBBOS描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__bos__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第146章\_USBBOS描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__bos__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 146.1\_阅读说明与来源

译注：本页说明USB二进制设备对象存储（Binary Device Object Store，BOS）及其能力描述符。通用结构由新旧USB设备栈相关代码引用，不因旧版管理入口弃用而自动成为同一套弃用接口。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

根 BOS 描述符（Root BOS Descriptor）。

```c
#include <zephyr/usb/bos.h>
```

根 BOS 描述符（Root BOS Descriptor）。

## 146.2\_数据成员（Data Fields）

<a id="r_aa3a661440a4b6d6a2ecf27da740c4121"></a>

```c
uint8_t bLength
```

此描述符的大小，以字节为单位（5）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P146_USBBOS描述符.md#aa3a661440a4b6d6a2ecf27da740c4121)。

<a id="r_afd74417a44821690051d50cd5ffdd581"></a>

```c
uint8_t bDescriptorType
```

描述符类型（Descriptor Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P146_USBBOS描述符.md#afd74417a44821690051d50cd5ffdd581)。

<a id="r_ab45b26a3249589469a53b2cfb99ddd1d"></a>

```c
uint16_t wTotalLength
```

此描述符与全部关联设备能力描述符的总长度。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wTotalLength](P146_USBBOS描述符.md#ab45b26a3249589469a53b2cfb99ddd1d)。

<a id="r_a2c0e68a49d6904d32413f3b3598bb926"></a>

```c
uint8_t bNumDeviceCaps
```

后续设备能力描述符的数量。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bNumDeviceCaps](P146_USBBOS描述符.md#a2c0e68a49d6904d32413f3b3598bb926)。

## 146.3\_详细说明（Detailed Documentation）

<a id="afd74417a44821690051d50cd5ffdd581"></a>

### 146.3.1\_`bDescriptorType`

```c
uint8_t usb_bos_descriptor::bDescriptorType
```

描述符类型（Descriptor Type）。

必须设置为 USB_DESC_BOS。

<a id="aa3a661440a4b6d6a2ecf27da740c4121"></a>

### 146.3.2\_`bLength`

```c
uint8_t usb_bos_descriptor::bLength
```

此描述符的大小，以字节为单位（5）。

> 译注（源码核对）：5字节是根BOS描述符本身的长度；完整BOS数据集合还包含后续能力描述符，不能把此值当成全部响应长度。

<a id="a2c0e68a49d6904d32413f3b3598bb926"></a>

### 146.3.3\_`bNumDeviceCaps`

```c
uint8_t usb_bos_descriptor::bNumDeviceCaps
```

后续设备能力描述符的数量。

> 译注（源码核对）：统计的是紧随根描述符的设备能力描述符数量，不是每个能力描述符内部成员、接口或端点的数量。WebUSB与Microsoft OS能力在示例中各组成一项平台能力描述符。

<a id="ab45b26a3249589469a53b2cfb99ddd1d"></a>

### 146.3.4\_`wTotalLength`

```c
uint16_t usb_bos_descriptor::wTotalLength
```

此描述符与全部关联设备能力描述符的总长度。

## 146.4\_源码跟踪与使用边界

译注依据保存的[官方BOS头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/bos.h)、[WebUSB能力与请求示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/webusb.h)及[Microsoft OS能力示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/msosv2.h)，摘要见[来源记录](../SOURCES.md)。WebUSB的URL索引与平台能力字段另核对[WebUSB规范](https://usb.spec.whatwg.org/#webusb-platform-capability-descriptor)。本仓库[通用头文件](../../../include/zephyr/usb/bos.h)与[WebUSB示例](../../../samples/subsys/usb/webusb/src/main.c)可用于相对路径源码跟踪，版本可能与网页不同。相关应用见[WebUSB示例译文](P069_WebUSB示例.md)；本批未构建固件、枚举设备或进行USB通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P145_USBBOS支持API.md) · [返回大纲](大纲.md) · [下一章](P147_USB平台能力描述符.md)
