---
id: learning.zephyr-docs.usb.api-151
title: USBBOS公共头文件
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bos_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第151章\_USBBOS公共头文件

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bos_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 151.1\_阅读说明与来源

译注：本页说明USB二进制设备对象存储（Binary Device Object Store，BOS）及其能力描述符。通用结构由新旧USB设备栈相关代码引用，不因旧版管理入口弃用而自动成为同一套弃用接口。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 二进制设备对象存储（Binary Device Object Store，BOS）支持。

```c
#include <stdint.h>
```

USB 二进制设备对象存储（Binary Device Object Store，BOS）支持。

## 151.2\_数据结构（Data Structures）

<a id="r_usb_5Fbos_5Fdescriptor"></a>

```c
struct usb_bos_descriptor
```

根 BOS 描述符（Root BOS Descriptor）。

相关声明：[usb_bos_descriptor](P146_USBBOS描述符.md)。

<a id="r_usb_5Fbos_5Fcapability_5Flpm"></a>

```c
struct usb_bos_capability_lpm
```

BOS USB 2.0 扩展能力描述符（Extension Capability Descriptor）。

相关声明：[usb_bos_capability_lpm](P148_USB链路电源管理能力.md)。

<a id="r_usb_5Fbos_5Fplatform_5Fdescriptor"></a>

```c
struct usb_bos_platform_descriptor
```

BOS 平台能力描述符（Platform Capability Descriptor）。

相关声明：[usb_bos_platform_descriptor](P147_USB平台能力描述符.md)。

<a id="r_usb_5Fbos_5Fcapability_5Fwebusb"></a>

```c
struct usb_bos_capability_webusb
```

平台能力描述符中的 WebUSB 专用部分。

相关声明：[usb_bos_capability_webusb](P150_USB网页访问能力.md)。

<a id="r_usb_5Fbos_5Fcapability_5Fmsos"></a>

```c
struct usb_bos_capability_msos
```

平台能力描述符中的 Microsoft OS 2.0 描述符专用部分。

相关声明：[usb_bos_capability_msos](P149_USB微软操作系统能力.md)。

## 151.3\_枚举（Enumerations）

<a id="r_ga0bddefd6b9373068cd4ff8e6fc47950d"></a>

```c
enum usb_bos_capability_types {
    USB_BOS_CAPABILITY_EXTENSION = 0x02,
    USB_BOS_CAPABILITY_PLATFORM = 0x05
}
```

设备能力类型代码（Device Capability Type Codes）。

相关声明：[usb_bos_capability_types](P145_USBBOS支持API.md#ga0bddefd6b9373068cd4ff8e6fc47950d)、[USB_BOS_CAPABILITY_EXTENSION](P145_USBBOS支持API.md#gga0bddefd6b9373068cd4ff8e6fc47950da2ca67045883d490b849193d4a5a29862)、[USB_BOS_CAPABILITY_PLATFORM](P145_USBBOS支持API.md#gga0bddefd6b9373068cd4ff8e6fc47950da5eb29e64487aa25625305f0b4595394b)。

## 151.4\_源码跟踪与使用边界

译注依据保存的[官方BOS头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/bos.h)、[WebUSB能力与请求示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/webusb.h)及[Microsoft OS能力示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/msosv2.h)，摘要见[来源记录](../SOURCES.md)。WebUSB的URL索引与平台能力字段另核对[WebUSB规范](https://usb.spec.whatwg.org/#webusb-platform-capability-descriptor)。本仓库[通用头文件](../../../include/zephyr/usb/bos.h)与[WebUSB示例](../../../samples/subsys/usb/webusb/src/main.c)可用于相对路径源码跟踪，版本可能与网页不同。相关应用见[WebUSB示例译文](P069_WebUSB示例.md)；本批未构建固件、枚举设备或进行USB通信测试。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="details"></a>
<a id="header-details"></a>

[上一章](P150_USB网页访问能力.md) · [返回大纲](大纲.md) · [下一章](P152_旧版USB控制器驱动API.md)
