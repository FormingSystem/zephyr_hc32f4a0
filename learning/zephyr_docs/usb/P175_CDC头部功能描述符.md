---
id: learning.zephyr-docs.usb.api-175
title: CDC头部功能描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcdc__header__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- Copyright (c) 2025 - 2026 NXP -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第175章\_CDC头部功能描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcdc__header__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 175.1\_阅读说明与来源

译注：本组说明 USB 通信设备类（Communications Device Class，CDC）的协议常量和数据结构。抽象控制模型（Abstract Control Model，ACM）用于相关串行通信功能；以太网控制模型（Ethernet Control Model，ECM）与网络控制模型（Network Control Model，NCM）用于网络功能。原文只列声明的字段按原样保留，源码补充明确标为译注；[本册大纲](大纲.md)列出相关驱动说明和示例。

头部功能描述符（Header Functional Descriptor）。

```c
#include <zephyr/usb/class/usb_cdc.h>
```

头部功能描述符（Header Functional Descriptor）。

## 175.2\_数据成员（Data Fields）

<a id="r_ac4ad6939d5a075ff2fe6d7505cba630b"></a>

```c
uint8_t bFunctionLength
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bFunctionLength](P175_CDC头部功能描述符.md#ac4ad6939d5a075ff2fe6d7505cba630b)。

<a id="r_a3b8cc0d8b9d56db158f3b027b2cd6f6a"></a>

```c
uint8_t bDescriptorType
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P175_CDC头部功能描述符.md#a3b8cc0d8b9d56db158f3b027b2cd6f6a)。

<a id="r_a49bf7e700891057f30cd3be77dec0752"></a>

```c
uint8_t bDescriptorSubtype
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorSubtype](P175_CDC头部功能描述符.md#a49bf7e700891057f30cd3be77dec0752)。

<a id="r_ab66b3b87594a4510f11ba9ee950f230c"></a>

```c
uint16_t bcdCDC
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bcdCDC](P175_CDC头部功能描述符.md#ab66b3b87594a4510f11ba9ee950f230c)。

## 175.3\_详细说明（Detailed Documentation）

<a id="ab66b3b87594a4510f11ba9ee950f230c"></a>

### 175.3.1\_`bcdCDC`

```c
uint16_t cdc_header_descriptor::bcdCDC
```

> 译注（源码核对）：此字段记录 CDC 规范版本，和设备描述符中的 `bcdUSB`、`bcdDevice` 属于不同对象。当前 ACM 实现用 `sys_cpu_to_le16()` 初始化此字段；协议中的多字节字段需要按指定字节序编码。

<a id="a49bf7e700891057f30cd3be77dec0752"></a>

### 175.3.2\_`bDescriptorSubtype`

```c
uint8_t cdc_header_descriptor::bDescriptorSubtype
```

<a id="a3b8cc0d8b9d56db158f3b027b2cd6f6a"></a>

### 175.3.3\_`bDescriptorType`

```c
uint8_t cdc_header_descriptor::bDescriptorType
```

<a id="ac4ad6939d5a075ff2fe6d7505cba630b"></a>

### 175.3.4\_`bFunctionLength`

```c
uint8_t cdc_header_descriptor::bFunctionLength
```

> 译注（源码核对）：头部功能描述符由长度、描述符类型、描述符子类型和 CDC 版本四个字段组成；源码用 `__packed` 标记布局。当前实现以 `sizeof(struct cdc_header_descriptor)` 填写长度，不是整组 CDC 接口描述符的总长度。

## 175.4\_源码跟踪与使用边界

译注依据保存的[官方 CDC 公共头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_cdc.h)、[ACM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ecm.c)和[NCM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ncm.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[公共头文件](../../../include/zephyr/usb/class/usb_cdc.h)、[ACM 源码](../../../subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ecm.c)及[NCM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ncm.c)供相对路径跟踪，版本可能与官网不同。本批未构建固件、连接串口或执行 USB 网络通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P174_CDC公共头文件与常量.md) · [返回大纲](大纲.md) · [下一章](P176_CDC联合接口功能描述符.md)
