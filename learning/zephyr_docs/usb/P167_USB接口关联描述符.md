---
id: learning.zephyr-docs.usb.api-167
title: USB接口关联描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__association__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第167章\_USB接口关联描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__association__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 167.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

USB 3 规范中定义的 USB 关联描述符（Association Descriptor）。

```c
#include <zephyr/usb/usb_ch9.h>
```

USB 3 规范中定义的 USB 关联描述符（Association Descriptor）。

参见规范中的表 9-16。

## 167.2\_数据成员（Data Fields）

<a id="r_a11b2d1b6a8330dcb237e433db277e487"></a>

```c
uint8_t bLength
```

描述符长度（Descriptor Length）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P167_USB接口关联描述符.md#a11b2d1b6a8330dcb237e433db277e487)。

<a id="r_ac7c1237aafde77115977bd05b1b8b0ff"></a>

```c
uint8_t bDescriptorType
```

描述符类型（Descriptor Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P167_USB接口关联描述符.md#ac7c1237aafde77115977bd05b1b8b0ff)。

<a id="r_aa2ad28cdb50d50627ef16d29bfba5a88"></a>

```c
uint8_t bFirstInterface
```

首个接口的编号（First Interface Number）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bFirstInterface](P167_USB接口关联描述符.md#aa2ad28cdb50d50627ef16d29bfba5a88)。

<a id="r_a7d3aad4fa259c865402a41b75bff3ff9"></a>

```c
uint8_t bInterfaceCount
```

关联接口的数量（Number of Associated Interfaces）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bInterfaceCount](P167_USB接口关联描述符.md#a7d3aad4fa259c865402a41b75bff3ff9)。

<a id="r_a1acdb21ad26400d1785a14c637a2b857"></a>

```c
uint8_t bFunctionClass
```

功能类（Function Class）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bFunctionClass](P167_USB接口关联描述符.md#a1acdb21ad26400d1785a14c637a2b857)。

<a id="r_a30ee67b37bfdbe56a5b58fab1d195dc9"></a>

```c
uint8_t bFunctionSubClass
```

功能子类（Function Subclass）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bFunctionSubClass](P167_USB接口关联描述符.md#a30ee67b37bfdbe56a5b58fab1d195dc9)。

<a id="r_a7205b1693998e6471ac9dbafa446a6a5"></a>

```c
uint8_t bFunctionProtocol
```

功能协议（Function Protocol）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bFunctionProtocol](P167_USB接口关联描述符.md#a7205b1693998e6471ac9dbafa446a6a5)。

<a id="r_a416fd6c3c27bb0453f1b2d201c9619b1"></a>

```c
uint8_t iFunction
```

功能字符串索引（Function String Index）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iFunction](P167_USB接口关联描述符.md#a416fd6c3c27bb0453f1b2d201c9619b1)。

## 167.3\_详细说明（Detailed Documentation）

<a id="ac7c1237aafde77115977bd05b1b8b0ff"></a>

### 167.3.1\_`bDescriptorType`

```c
uint8_t usb_association_descriptor::bDescriptorType
```

描述符类型（Descriptor Type）。

<a id="aa2ad28cdb50d50627ef16d29bfba5a88"></a>

### 167.3.2\_`bFirstInterface`

```c
uint8_t usb_association_descriptor::bFirstInterface
```

首个接口的编号（First Interface Number）。

<a id="a1acdb21ad26400d1785a14c637a2b857"></a>

### 167.3.3\_`bFunctionClass`

```c
uint8_t usb_association_descriptor::bFunctionClass
```

功能类（Function Class）。

<a id="a7205b1693998e6471ac9dbafa446a6a5"></a>

### 167.3.4\_`bFunctionProtocol`

```c
uint8_t usb_association_descriptor::bFunctionProtocol
```

功能协议（Function Protocol）。

<a id="a30ee67b37bfdbe56a5b58fab1d195dc9"></a>

### 167.3.5\_`bFunctionSubClass`

```c
uint8_t usb_association_descriptor::bFunctionSubClass
```

功能子类（Function Subclass）。

<a id="a7d3aad4fa259c865402a41b75bff3ff9"></a>

### 167.3.6\_`bInterfaceCount`

```c
uint8_t usb_association_descriptor::bInterfaceCount
```

关联接口的数量（Number of Associated Interfaces）。

<a id="a11b2d1b6a8330dcb237e433db277e487"></a>

### 167.3.7\_`bLength`

```c
uint8_t usb_association_descriptor::bLength
```

描述符长度（Descriptor Length）。

<a id="a416fd6c3c27bb0453f1b2d201c9619b1"></a>

### 167.3.8\_`iFunction`

```c
uint8_t usb_association_descriptor::iFunction
```

功能字符串索引（Function String Index）。

## 167.4\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P166_USB端点描述符.md) · [返回大纲](大纲.md) · [下一章](P168_USB字符串描述符.md)
