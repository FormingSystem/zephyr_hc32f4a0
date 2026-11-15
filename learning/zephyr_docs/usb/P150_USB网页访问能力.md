---
id: learning.zephyr-docs.usb.api-150
title: USB网页访问能力
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__bos__capability__webusb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第150章\_USB网页访问能力

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__bos__capability__webusb.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 150.1\_阅读说明与来源

译注：本页说明USB二进制设备对象存储（Binary Device Object Store，BOS）及其能力描述符。通用结构由新旧USB设备栈相关代码引用，不因旧版管理入口弃用而自动成为同一套弃用接口。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

平台能力描述符中的 WebUSB 专用部分。

```c
#include <zephyr/usb/bos.h>
```

平台能力描述符中的 WebUSB 专用部分。

定义 WebUSB 专用字段，用于扩展通用的平台能力描述符。

## 150.2\_数据成员（Data Fields）

<a id="r_a1ebbfa1bdca4ad783000c67419552e54"></a>

```c
uint16_t bcdVersion
```

以二进制编码十进制（Binary-Coded Decimal，BCD）格式表示的 WebUSB 规范版本，例如 0x0100。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bcdVersion](P150_USB网页访问能力.md#a1ebbfa1bdca4ad783000c67419552e54)。

<a id="r_a3ae4aada1ab7b28d9bac6294467e93ff"></a>

```c
uint8_t bVendorCode
```

主机获取 WebUSB 描述符时使用的厂商专用请求代码。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bVendorCode](P150_USB网页访问能力.md#a3ae4aada1ab7b28d9bac6294467e93ff)。

<a id="r_a068861c7ee1abfdb03e52b8269db30b5"></a>

```c
uint8_t iLandingPage
```

着陆页（Landing Page）字符串描述符的索引。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iLandingPage](P150_USB网页访问能力.md#a068861c7ee1abfdb03e52b8269db30b5)。

## 150.3\_详细说明（Detailed Documentation）

<a id="a1ebbfa1bdca4ad783000c67419552e54"></a>

### 150.3.1\_`bcdVersion`

```c
uint16_t usb_bos_capability_webusb::bcdVersion
```

以二进制编码十进制（Binary-Coded Decimal，BCD）格式表示的 WebUSB 规范版本，例如 0x0100。

> 译注（源码核对）：此处版本描述WebUSB协议；它不是USB设备的bcdUSB版本，也不是浏览器版本号。官方示例用sys_cpu_to_le16(0x0100)将该字段转换为USB使用的小端字节序。

<a id="a3ae4aada1ab7b28d9bac6294467e93ff"></a>

### 150.3.2\_`bVendorCode`

```c
uint8_t usb_bos_capability_webusb::bVendorCode
```

主机获取 WebUSB 描述符时使用的厂商专用请求代码。

<a id="a068861c7ee1abfdb03e52b8269db30b5"></a>

### 150.3.3\_`iLandingPage`

```c
uint8_t usb_bos_capability_webusb::iLandingPage
```

着陆页（Landing Page）字符串描述符的索引。

零表示未定义着陆页。

> 译注（源码核对）：上方“字符串描述符”按原注释翻译；WebUSB规范更准确地将此字段定义为URL描述符索引。官方示例通过厂商请求GET_URL取得含协议前缀与UTF-8 URL的描述符，不是通过普通USB字符串描述符请求获取。0仅表示没有着陆页；不能据此推断WebUSB功能整体关闭。

## 150.4\_源码跟踪与使用边界

译注依据保存的[官方BOS头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/bos.h)、[WebUSB能力与请求示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/webusb.h)及[Microsoft OS能力示例](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/msosv2.h)，摘要见[来源记录](../SOURCES.md)。WebUSB的URL索引与平台能力字段另核对[WebUSB规范](https://usb.spec.whatwg.org/#webusb-platform-capability-descriptor)。本仓库[通用头文件](../../../include/zephyr/usb/bos.h)与[WebUSB示例](../../../samples/subsys/usb/webusb/src/main.c)可用于相对路径源码跟踪，版本可能与网页不同。相关应用见[WebUSB示例译文](P069_WebUSB示例.md)；本批未构建固件、枚举设备或进行USB通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P149_USB微软操作系统能力.md) · [返回大纲](大纲.md) · [下一章](P151_USBBOS公共头文件.md)
