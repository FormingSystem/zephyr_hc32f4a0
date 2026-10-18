---
id: learning.zephyr-docs.usb.api-165
title: USB接口描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__if__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第165章\_USB接口描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__if__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 165.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

USB 标准接口描述符（Standard Interface Descriptor）。

```c
#include <zephyr/usb/usb_ch9.h>
```

USB 标准接口描述符（Standard Interface Descriptor）。

参见规范中的表 9-12。

## 165.2\_数据成员（Data Fields）

<a id="r_af2e39b46da3fc3bc52cd9a4b38a3c897"></a>

```c
uint8_t bLength
```

描述符长度（Descriptor Length）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P165_USB接口描述符.md#af2e39b46da3fc3bc52cd9a4b38a3c897)。

<a id="r_aed00a5334643e15dca23b72ec9d0bc32"></a>

```c
uint8_t bDescriptorType
```

描述符类型（Descriptor Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P165_USB接口描述符.md#aed00a5334643e15dca23b72ec9d0bc32)。

<a id="r_af3227603f9169d7edc173318d3da298c"></a>

```c
uint8_t bInterfaceNumber
```

接口编号（Interface Number）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bInterfaceNumber](P165_USB接口描述符.md#af3227603f9169d7edc173318d3da298c)。

<a id="r_a170fa703535138cdb1032b149707aae1"></a>

```c
uint8_t bAlternateSetting
```

备用设置值（Alternate Setting Value）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bAlternateSetting](P165_USB接口描述符.md#a170fa703535138cdb1032b149707aae1)。

<a id="r_a9c67427276ada4d9370eba1bd50d6e3f"></a>

```c
uint8_t bNumEndpoints
```

端点数量（Number of Endpoints）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bNumEndpoints](P165_USB接口描述符.md#a9c67427276ada4d9370eba1bd50d6e3f)。

<a id="r_acd9c54c2ff9e2b92c61b0313d6403bac"></a>

```c
uint8_t bInterfaceClass
```

接口类（Interface Class）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bInterfaceClass](P165_USB接口描述符.md#acd9c54c2ff9e2b92c61b0313d6403bac)。

<a id="r_a3288bd3444a757496b7ec45a33d3c0c8"></a>

```c
uint8_t bInterfaceSubClass
```

接口子类（Interface Subclass）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bInterfaceSubClass](P165_USB接口描述符.md#a3288bd3444a757496b7ec45a33d3c0c8)。

<a id="r_a85e85e0adac6a61d9ed2faeb2051cf71"></a>

```c
uint8_t bInterfaceProtocol
```

接口协议（Interface Protocol）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bInterfaceProtocol](P165_USB接口描述符.md#a85e85e0adac6a61d9ed2faeb2051cf71)。

<a id="r_ae189cb0fd93f2b7720908932aa0b983e"></a>

```c
uint8_t iInterface
```

接口字符串索引（Interface String Index）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iInterface](P165_USB接口描述符.md#ae189cb0fd93f2b7720908932aa0b983e)。

## 165.3\_详细说明（Detailed Documentation）

<a id="a170fa703535138cdb1032b149707aae1"></a>

### 165.3.1\_`bAlternateSetting`

```c
uint8_t usb_if_descriptor::bAlternateSetting
```

备用设置值（Alternate Setting Value）。

> 译注（源码核对）：备用设置与接口编号分别表示两个选择维度。`sreq_set_interface()` 将请求的 `wIndex` 作为接口编号、`wValue` 作为备用设置传给 `usbd_interface_set()`；切换备用设置不会改变请求所指的接口编号。

<a id="aed00a5334643e15dca23b72ec9d0bc32"></a>

### 165.3.2\_`bDescriptorType`

```c
uint8_t usb_if_descriptor::bDescriptorType
```

描述符类型（Descriptor Type）。

<a id="acd9c54c2ff9e2b92c61b0313d6403bac"></a>

### 165.3.3\_`bInterfaceClass`

```c
uint8_t usb_if_descriptor::bInterfaceClass
```

接口类（Interface Class）。

<a id="af3227603f9169d7edc173318d3da298c"></a>

### 165.3.4\_`bInterfaceNumber`

```c
uint8_t usb_if_descriptor::bInterfaceNumber
```

接口编号（Interface Number）。

<a id="a85e85e0adac6a61d9ed2faeb2051cf71"></a>

### 165.3.5\_`bInterfaceProtocol`

```c
uint8_t usb_if_descriptor::bInterfaceProtocol
```

接口协议（Interface Protocol）。

<a id="a3288bd3444a757496b7ec45a33d3c0c8"></a>

### 165.3.6\_`bInterfaceSubClass`

```c
uint8_t usb_if_descriptor::bInterfaceSubClass
```

接口子类（Interface Subclass）。

<a id="af2e39b46da3fc3bc52cd9a4b38a3c897"></a>

### 165.3.7\_`bLength`

```c
uint8_t usb_if_descriptor::bLength
```

描述符长度（Descriptor Length）。

<a id="a9c67427276ada4d9370eba1bd50d6e3f"></a>

### 165.3.8\_`bNumEndpoints`

```c
uint8_t usb_if_descriptor::bNumEndpoints
```

端点数量（Number of Endpoints）。

<a id="ae189cb0fd93f2b7720908932aa0b983e"></a>

### 165.3.9\_`iInterface`

```c
uint8_t usb_if_descriptor::iInterface
```

接口字符串索引（Interface String Index）。

## 165.4\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P164_USB配置描述符.md) · [返回大纲](大纲.md) · [下一章](P166_USB端点描述符.md)
