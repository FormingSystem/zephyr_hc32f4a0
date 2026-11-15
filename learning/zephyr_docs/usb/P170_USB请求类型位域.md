---
id: learning.zephyr-docs.usb.api-170
title: USB请求类型位域
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__req__type__field.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第170章\_USB请求类型位域

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__req__type__field.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 170.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

bmRequestType 位域（Bit Field）的表示。

```c
#include <zephyr/usb/usb_ch9.h>
```

bmRequestType 位域（Bit Field）的表示。

## 170.2\_数据成员（Data Fields）

<a id="r_af312d3f2c354d2ed987a25b55b299efd"></a>

```c
uint8_t direction: 1
```

数据传输方向（Data Transfer Direction）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[direction](P170_USB请求类型位域.md#af312d3f2c354d2ed987a25b55b299efd)。

<a id="r_ab3c23439784768b6ddf71b81d58452d0"></a>

```c
uint8_t type: 2
```

请求类型（Request Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](P170_USB请求类型位域.md#ab3c23439784768b6ddf71b81d58452d0)。

<a id="r_aa75b3b73833a9c8163ab9539817d1f31"></a>

```c
uint8_t recipient: 5
```

请求接收方（Request Recipient）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[recipient](P170_USB请求类型位域.md#aa75b3b73833a9c8163ab9539817d1f31)。

## 170.3\_详细说明（Detailed Documentation）

<a id="af312d3f2c354d2ed987a25b55b299efd"></a>

### 170.3.1\_`direction`

```c
uint8_t usb_req_type_field::direction
```

数据传输方向（Data Transfer Direction）。

> 译注（源码核对）：头文件将方向定义为 1 位：0 表示主机到设备，1 表示设备到主机。`recipient` 为 5 位，`type` 为 2 位；Doxygen 的字段摘要省略了位宽，完整声明见本组头文件源码页。

<a id="aa75b3b73833a9c8163ab9539817d1f31"></a>

### 170.3.2\_`recipient`

```c
uint8_t usb_req_type_field::recipient
```

请求接收方（Request Recipient）。

<a id="ab3c23439784768b6ddf71b81d58452d0"></a>

### 170.3.3\_`type`

```c
uint8_t usb_req_type_field::type
```

请求类型（Request Type）。

## 170.4\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。轮询间隔换算还核对保存的[官方整数 log2 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/math/ilog2.h)。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P169_USB设备限定描述符.md) · [返回大纲](大纲.md) · [下一章](P171_USB端点属性位域.md)
