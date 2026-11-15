---
id: learning.zephyr-docs.usb.api-148
title: USB链路电源管理能力
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__bos__capability__lpm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第148章\_USB链路电源管理能力

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__bos__capability__lpm.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 148.1\_阅读说明与来源

译注：本页说明USB二进制设备对象存储（Binary Device Object Store，BOS）及其能力描述符。通用结构由新旧USB设备栈相关代码引用，不因旧版管理入口弃用而自动成为同一套弃用接口。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

BOS USB 2.0 扩展能力描述符（Extension Capability Descriptor）。

```c
#include <zephyr/usb/bos.h>
```

BOS USB 2.0 扩展能力描述符（Extension Capability Descriptor）。

用于表示对 USB 2.0 链路电源管理（Link Power Management，LPM）及相关尽力服务延迟（Best Effort Service Latency，BESL）参数的支持。

## 148.2\_数据成员（Data Fields）

<a id="r_a09ec679e05e7b848800ab63220109bef"></a>

```c
uint8_t bLength
```

此描述符的大小，以字节为单位。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P148_USB链路电源管理能力.md#a09ec679e05e7b848800ab63220109bef)。

<a id="r_a880b1f6efecf7d1e8e9076680c74f9c2"></a>

```c
uint8_t bDescriptorType
```

描述符类型（Descriptor Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P148_USB链路电源管理能力.md#a880b1f6efecf7d1e8e9076680c74f9c2)。

<a id="r_a1ceea07e81970d684a6c1586364a0c90"></a>

```c
uint8_t bDevCapabilityType
```

设备能力类型（Device Capability Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDevCapabilityType](P148_USB链路电源管理能力.md#a1ceea07e81970d684a6c1586364a0c90)。

<a id="r_a8a643af1e99eafdecc006cf714cb0af7"></a>

```c
uint32_t bmAttributes
```

所支持属性的位图（Bitmap）。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bmAttributes](P148_USB链路电源管理能力.md#a8a643af1e99eafdecc006cf714cb0af7)。

## 148.3\_详细说明（Detailed Documentation）

<a id="a880b1f6efecf7d1e8e9076680c74f9c2"></a>

### 148.3.1\_`bDescriptorType`

```c
uint8_t usb_bos_capability_lpm::bDescriptorType
```

描述符类型（Descriptor Type）。

必须设置为 USB_DESC_DEVICE_CAPABILITY。

<a id="a1ceea07e81970d684a6c1586364a0c90"></a>

### 148.3.2\_`bDevCapabilityType`

```c
uint8_t usb_bos_capability_lpm::bDevCapabilityType
```

设备能力类型（Device Capability Type）。

必须为 USB_BOS_CAPABILITY_EXTENSION。

<a id="a09ec679e05e7b848800ab63220109bef"></a>

### 148.3.3\_`bLength`

```c
uint8_t usb_bos_capability_lpm::bLength
```

此描述符的大小，以字节为单位。

<a id="a8a643af1e99eafdecc006cf714cb0af7"></a>

### 148.3.4\_`bmAttributes`

```c
uint32_t usb_bos_capability_lpm::bmAttributes
```

所支持属性的位图（Bitmap）。

> 译注（源码核对）：这里保存USB 2.0扩展能力的属性位图；结构体定义本身没有提供各个位的含义，也不会自动启用控制器的低功耗功能。设置属性仍需与目标控制器及协议实现支持相符。

## 148.4\_源码跟踪与使用边界

译注依据保存的[官方BOS头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/bos.h)、[WebUSB能力与请求示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/webusb.h)及[Microsoft OS能力示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/msosv2.h)，摘要见[来源记录](../SOURCES.md)。WebUSB的URL索引与平台能力字段另核对[WebUSB规范](https://usb.spec.whatwg.org/#webusb-platform-capability-descriptor)。本仓库[通用头文件](../../../include/zephyr/usb/bos.h)与[WebUSB示例](../../../samples/subsys/usb/webusb/src/main.c)可用于相对路径源码跟踪，版本可能与网页不同。相关应用见[WebUSB示例译文](P069_WebUSB示例.md)；本批未构建固件、枚举设备或进行USB通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P147_USB平台能力描述符.md) · [返回大纲](大纲.md) · [下一章](P149_USB微软操作系统能力.md)
