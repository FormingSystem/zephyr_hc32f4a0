---
id: learning.zephyr-docs.usb.api-162
title: USB类专用描述符头
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__cs__desc__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第162章\_USB类专用描述符头

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__cs__desc__header.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 162.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

USB 类专用描述符头（Class-specific Descriptor Header）。

```c
#include <zephyr/usb/usb_ch9.h>
```

USB 类专用描述符头（Class-specific Descriptor Header）。

## 162.2\_数据成员（Data Fields）

<a id="r_afef6d42038db5d9f77cda20c8483eca9"></a>

```c
uint8_t bLength
```

描述符的长度，以字节为单位。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P162_USB类专用描述符头.md#afef6d42038db5d9f77cda20c8483eca9)。

<a id="r_a0b8a1a5f7983646e4d1bb295613bfa46"></a>

```c
uint8_t bDescriptorType
```

描述符的类型。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P162_USB类专用描述符头.md#a0b8a1a5f7983646e4d1bb295613bfa46)。

<a id="r_a63d151c4de5bf4f5ad88885cceb14441"></a>

```c
uint8_t bDescriptorSubtype
```

类专用描述符类型（Class-specific Descriptor Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorSubtype](P162_USB类专用描述符头.md#a63d151c4de5bf4f5ad88885cceb14441)。

## 162.3\_详细说明（Detailed Documentation）

<a id="a63d151c4de5bf4f5ad88885cceb14441"></a>

### 162.3.1\_`bDescriptorSubtype`

```c
uint8_t usb_cs_desc_header::bDescriptorSubtype
```

类专用描述符类型（Class-specific Descriptor Type）。

<a id="a0b8a1a5f7983646e4d1bb295613bfa46"></a>

### 162.3.2\_`bDescriptorType`

```c
uint8_t usb_cs_desc_header::bDescriptorType
```

描述符的类型。

<a id="afef6d42038db5d9f77cda20c8483eca9"></a>

### 162.3.3\_`bLength`

```c
uint8_t usb_cs_desc_header::bLength
```

描述符的长度，以字节为单位。

## 162.4\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P161_USB通用描述符头.md) · [返回大纲](大纲.md) · [下一章](P163_USB设备描述符.md)
