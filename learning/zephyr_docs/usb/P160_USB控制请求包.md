---
id: learning.zephyr-docs.usb.api-160
title: USB控制请求包
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__setup__packet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第160章\_USB控制请求包

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__setup__packet.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 160.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

USB 设置数据包（Setup Data Packet）。

```c
#include <zephyr/usb/usb_ch9.h>
```

USB 设置数据包（Setup Data Packet）。

参见规范中的表 9-2。

## 160.2\_数据成员（Data Fields）

```c
union {
```



<a id="r_a3474785adc5baa63670e090134dc08d2"></a>

```c
uint8_t bmRequestType
```

原始请求类型值（Raw Request Type Value）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bmRequestType](P160_USB控制请求包.md#a326cfb3e8b11cc2e7cf4738d593cf10a)。

<a id="r_a4af374f7490e430d69cb11c8d2e10d4f"></a>

```c
struct usb_req_type_field RequestType
```

请求类型位域（Request Type Bit Fields）。

相关声明：[usb_req_type_field](P170_USB请求类型位域.md)、[RequestType](P160_USB控制请求包.md#afa3d273ae57c3124b14ab100ac9f9a24)。

<a id="r_aa922c5946a3421318de5ae77f53c464b"></a>

```c
};
```

请求类型联合体（Request Type Union），提供原始值与结构化字段两种访问方式。

<a id="r_aab50ed2f2cdcc1d747f6f224fe9d2018"></a>

```c
uint8_t bRequest
```

请求代码（Request Code）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bRequest](P160_USB控制请求包.md#aab50ed2f2cdcc1d747f6f224fe9d2018)。

<a id="r_a619fbc1b9b6452f4394da713bdbc6a89"></a>

```c
uint16_t wValue
```

请求专用值（Request-specific Value）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wValue](P160_USB控制请求包.md#a619fbc1b9b6452f4394da713bdbc6a89)。

<a id="r_a953c058f0e31481a3d59b404037be009"></a>

```c
uint16_t wIndex
```

请求专用索引（Request-specific Index）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wIndex](P160_USB控制请求包.md#a953c058f0e31481a3d59b404037be009)。

<a id="r_a3421c921569bf3727534652c5f71da96"></a>

```c
uint16_t wLength
```

预期数据长度（Expected Data Length）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wLength](P160_USB控制请求包.md#a3421c921569bf3727534652c5f71da96)。

## 160.3\_详细说明（Detailed Documentation）

<a id="aa922c5946a3421318de5ae77f53c464b"></a>

### 160.3.1\_`[union]`

```c
union { ... } usb_setup_packet
```

请求类型联合体（Request Type Union），提供原始值与结构化字段两种访问方式。

> 译注（源码核对）：`bmRequestType` 与 `RequestType` 是同一匿名联合体（Anonymous Union）的两种视图，共用存储空间。后者由 `usb_req_type_field` 拆分接收方、类型和数据方向；并不是请求包中额外传输的一组字节。

<a id="a326cfb3e8b11cc2e7cf4738d593cf10a"></a>

### 160.3.2\_`bmRequestType`

```c
uint8_t usb_setup_packet::bmRequestType
```

原始请求类型值（Raw Request Type Value）。

<a id="aab50ed2f2cdcc1d747f6f224fe9d2018"></a>

### 160.3.3\_`bRequest`

```c
uint8_t usb_setup_packet::bRequest
```

请求代码（Request Code）。

<a id="afa3d273ae57c3124b14ab100ac9f9a24"></a>

### 160.3.4\_`RequestType`

```c
struct usb_req_type_field usb_setup_packet::RequestType
```

请求类型位域（Request Type Bit Fields）。

<a id="a953c058f0e31481a3d59b404037be009"></a>

### 160.3.5\_`wIndex`

```c
uint16_t usb_setup_packet::wIndex
```

请求专用索引（Request-specific Index）。

<a id="a3421c921569bf3727534652c5f71da96"></a>

### 160.3.6\_`wLength`

```c
uint16_t usb_setup_packet::wLength
```

预期数据长度（Expected Data Length）。

> 译注（源码核对）：这是请求预期的数据阶段长度，不是已经传输的字节数。新版设备栈读取设置包后将 `wValue`、`wIndex`、`wLength` 从小端转换为 CPU 字节序；描述符响应按请求长度截取，`wLength == 0` 的请求进入无数据阶段的处理分支。

<a id="a619fbc1b9b6452f4394da713bdbc6a89"></a>

### 160.3.7\_`wValue`

```c
uint16_t usb_setup_packet::wValue
```

请求专用值（Request-specific Value）。

## 160.4\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P159_旧版USB接口请求配置.md) · [返回大纲](大纲.md) · [下一章](P161_USB通用描述符头.md)
