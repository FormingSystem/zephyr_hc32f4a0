---
id: learning.zephyr-docs.usb.api-168
title: USB字符串描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__string__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第168章\_USB字符串描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__string__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 168.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

USB Unicode 字符串描述符（String Descriptor），采用 UTF-16 小端编码（UTF-16LE）。

```c
#include <zephyr/usb/usb_ch9.h>
```

USB Unicode 字符串描述符（String Descriptor），采用 UTF-16 小端编码（UTF-16LE）。

参见规范中的表 9-15。

## 168.2\_数据成员（Data Fields）

<a id="r_a93d9bb7c2c44f6f0cae1a871a4a18789"></a>

```c
uint8_t bLength
```

描述符长度（Descriptor Length）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P168_USB字符串描述符.md#a93d9bb7c2c44f6f0cae1a871a4a18789)。

<a id="r_a37d44e07cb6d5b449b03fb70c9677b15"></a>

```c
uint8_t bDescriptorType
```

描述符类型（Descriptor Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P168_USB字符串描述符.md#a37d44e07cb6d5b449b03fb70c9677b15)。

<a id="r_aefde51bb570c2bb2eb172c07d48233f1"></a>

```c
uint16_t bString
```

以 UTF-16LE 编码的字符（UTF-16LE Encoded Character）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bString](P168_USB字符串描述符.md#aefde51bb570c2bb2eb172c07d48233f1)。

## 168.3\_详细说明（Detailed Documentation）

<a id="a37d44e07cb6d5b449b03fb70c9677b15"></a>

### 168.3.1\_`bDescriptorType`

```c
uint8_t usb_string_descriptor::bDescriptorType
```

描述符类型（Descriptor Type）。

<a id="a93d9bb7c2c44f6f0cae1a871a4a18789"></a>

### 168.3.2\_`bLength`

```c
uint8_t usb_string_descriptor::bLength
```

描述符长度（Descriptor Length）。

<a id="aefde51bb570c2bb2eb172c07d48233f1"></a>

### 168.3.3\_`bString`

```c
uint16_t usb_string_descriptor::bString
```

以 UTF-16LE 编码的字符（UTF-16LE Encoded Character）。

> 译注（源码核对）：这里按官方头文件保留单个 `uint16_t bString`，没有改写成数组。当前设备栈用此结构返回语言标识（Language ID，LANGID）描述符；普通字符串由 `string_ascii7_to_utf16le()` 将可打印 ASCII-7 字符逐个写成 UTF-16LE 数据。不能由本结构的一个字段推断所有字符串描述符只能容纳一个字符，也不能推断该转换函数支持任意 Unicode 输入。

## 168.4\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P167_USB接口关联描述符.md) · [返回大纲](大纲.md) · [下一章](P169_USB设备限定描述符.md)
