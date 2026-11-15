---
id: learning.zephyr-docs.usb.api-149
title: USB微软操作系统能力
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__bos__capability__msos.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第149章\_USB微软操作系统能力

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__bos__capability__msos.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 149.1\_阅读说明与来源

译注：本页说明USB二进制设备对象存储（Binary Device Object Store，BOS）及其能力描述符。通用结构由新旧USB设备栈相关代码引用，不因旧版管理入口弃用而自动成为同一套弃用接口。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

平台能力描述符中的 Microsoft OS 2.0 描述符专用部分。

```c
#include <zephyr/usb/bos.h>
```

平台能力描述符中的 Microsoft OS 2.0 描述符专用部分。

定义 Microsoft OS 2.0 描述符集（Descriptor Set），用于向 Windows 主机描述设备能力。

## 149.2\_数据成员（Data Fields）

<a id="r_a5e10aed83d93d2ddc1278245aab9cb0a"></a>

```c
uint32_t dwWindowsVersion
```

支持的 Windows 版本，例如 0x0A000000UL 表示 Windows 10。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dwWindowsVersion](P149_USB微软操作系统能力.md#a5e10aed83d93d2ddc1278245aab9cb0a)。

<a id="r_adbf37ee9a5d7479d59cd1a44ab8d8ca5"></a>

```c
uint16_t wMSOSDescriptorSetTotalLength
```

MS OS 2.0 描述符集的总长度。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wMSOSDescriptorSetTotalLength](P149_USB微软操作系统能力.md#adbf37ee9a5d7479d59cd1a44ab8d8ca5)。

<a id="r_a4da7539d3bc58fe1da48e3d4d8c965e2"></a>

```c
uint8_t bMS_VendorCode
```

用于获取 MS OS 2.0 描述符集的厂商专用请求代码（Vendor-Specific Request Code）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bMS_VendorCode](P149_USB微软操作系统能力.md#a4da7539d3bc58fe1da48e3d4d8c965e2)。

<a id="r_a0945c68d9e7911add0c0586b000c90d3"></a>

```c
uint8_t bAltEnumCode
```

替代枚举代码（Alternate Enumeration Code），不使用时为 0。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bAltEnumCode](P149_USB微软操作系统能力.md#a0945c68d9e7911add0c0586b000c90d3)。

## 149.3\_详细说明（Detailed Documentation）

<a id="a0945c68d9e7911add0c0586b000c90d3"></a>

### 149.3.1\_`bAltEnumCode`

```c
uint8_t usb_bos_capability_msos::bAltEnumCode
```

替代枚举代码（Alternate Enumeration Code），不使用时为 0。

<a id="a4da7539d3bc58fe1da48e3d4d8c965e2"></a>

### 149.3.2\_`bMS_VendorCode`

```c
uint8_t usb_bos_capability_msos::bMS_VendorCode
```

用于获取 MS OS 2.0 描述符集的厂商专用请求代码（Vendor-Specific Request Code）。

> 译注（源码核对）：这是控制请求中的厂商请求代码，不是USB设备描述符的厂商标识VID。示例同时使用该代码定义BOS相关厂商请求处理，声明的代码应与处理路径一致。

<a id="a5e10aed83d93d2ddc1278245aab9cb0a"></a>

### 149.3.3\_`dwWindowsVersion`

```c
uint32_t usb_bos_capability_msos::dwWindowsVersion
```

支持的 Windows 版本，例如 0x0A000000UL 表示 Windows 10。

<a id="adbf37ee9a5d7479d59cd1a44ab8d8ca5"></a>

### 149.3.4\_`wMSOSDescriptorSetTotalLength`

```c
uint16_t usb_bos_capability_msos::wMSOSDescriptorSetTotalLength
```

MS OS 2.0 描述符集的总长度。

> 译注（源码核对）：官方示例取sizeof(msosv2_desc)并以sys_cpu_to_le16()编码，表示另外获取的整个MS OS 2.0描述符集长度，不是当前8字节专用字段结构的大小，也不是28字节平台能力描述符的大小。

## 149.4\_源码跟踪与使用边界

译注依据保存的[官方BOS头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/bos.h)、[WebUSB能力与请求示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/webusb.h)及[Microsoft OS能力示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/msosv2.h)，摘要见[来源记录](../SOURCES.md)。WebUSB的URL索引与平台能力字段另核对[WebUSB规范](https://usb.spec.whatwg.org/#webusb-platform-capability-descriptor)。本仓库[通用头文件](../../../include/zephyr/usb/bos.h)与[WebUSB示例](../../../samples/subsys/usb/webusb/src/main.c)可用于相对路径源码跟踪，版本可能与网页不同。相关应用见[WebUSB示例译文](P069_WebUSB示例.md)；本批未构建固件、枚举设备或进行USB通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P148_USB链路电源管理能力.md) · [返回大纲](大纲.md) · [下一章](P150_USB网页访问能力.md)
