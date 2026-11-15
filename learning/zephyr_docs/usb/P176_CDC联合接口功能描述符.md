---
id: learning.zephyr-docs.usb.api-176
title: CDC联合接口功能描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcdc__union__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- Copyright (c) 2025 - 2026 NXP -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第176章\_CDC联合接口功能描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcdc__union__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 176.1\_阅读说明与来源

译注：本组说明 USB 通信设备类（Communications Device Class，CDC）的协议常量和数据结构。抽象控制模型（Abstract Control Model，ACM）用于相关串行通信功能；以太网控制模型（Ethernet Control Model，ECM）与网络控制模型（Network Control Model，NCM）用于网络功能。原文只列声明的字段按原样保留，源码补充明确标为译注；[本册大纲](大纲.md)列出相关驱动说明和示例。

联合接口功能描述符（Union Interface Functional Descriptor）。

```c
#include <zephyr/usb/class/usb_cdc.h>
```

联合接口功能描述符（Union Interface Functional Descriptor）。

## 176.2\_数据成员（Data Fields）

<a id="r_a83ee5a04668006397663142232471606"></a>

```c
uint8_t bFunctionLength
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bFunctionLength](P176_CDC联合接口功能描述符.md#a83ee5a04668006397663142232471606)。

<a id="r_a839a6a4a7c4b2618c49649d93b7c6ff9"></a>

```c
uint8_t bDescriptorType
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P176_CDC联合接口功能描述符.md#a839a6a4a7c4b2618c49649d93b7c6ff9)。

<a id="r_a965212d833550c13376b231d5e2ce125"></a>

```c
uint8_t bDescriptorSubtype
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorSubtype](P176_CDC联合接口功能描述符.md#a965212d833550c13376b231d5e2ce125)。

<a id="r_a81bdab223598b27b620de0d9dba7bc80"></a>

```c
uint8_t bControlInterface
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bControlInterface](P176_CDC联合接口功能描述符.md#a81bdab223598b27b620de0d9dba7bc80)。

<a id="r_a5bab5215179ecc0bb0bb6e7b9089abf6"></a>

```c
uint8_t bSubordinateInterface0
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bSubordinateInterface0](P176_CDC联合接口功能描述符.md#a5bab5215179ecc0bb0bb6e7b9089abf6)。

## 176.3\_详细说明（Detailed Documentation）

<a id="a81bdab223598b27b620de0d9dba7bc80"></a>

### 176.3.1\_`bControlInterface`

```c
uint8_t cdc_union_descriptor::bControlInterface
```

> 译注（源码核对）：控制接口（Control Interface）编号与从属接口（Subordinate Interface）编号建立关联。当前 usbd_cdc_acm_init() 按实际分配的接口编号更新 `bControlInterface` 与 `bSubordinateInterface0`，不能把初始化模板中的 0、1 当成所有复合设备的固定编号。

<a id="a965212d833550c13376b231d5e2ce125"></a>

### 176.3.2\_`bDescriptorSubtype`

```c
uint8_t cdc_union_descriptor::bDescriptorSubtype
```

<a id="a839a6a4a7c4b2618c49649d93b7c6ff9"></a>

### 176.3.3\_`bDescriptorType`

```c
uint8_t cdc_union_descriptor::bDescriptorType
```

<a id="a83ee5a04668006397663142232471606"></a>

### 176.3.4\_`bFunctionLength`

```c
uint8_t cdc_union_descriptor::bFunctionLength
```

<a id="a5bab5215179ecc0bb0bb6e7b9089abf6"></a>

### 176.3.5\_`bSubordinateInterface0`

```c
uint8_t cdc_union_descriptor::bSubordinateInterface0
```

> 译注（源码核对）：这里按官方结构保留一个从属接口字段。联合接口功能描述符中的“Union”表示接口之间的关联；这个 C 类型本身是 `struct`，不是 C 语言的 `union`。

## 176.4\_源码跟踪与使用边界

译注依据保存的[官方 CDC 公共头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_cdc.h)、[ACM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ecm.c)和[NCM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ncm.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[公共头文件](../../../include/zephyr/usb/class/usb_cdc.h)、[ACM 源码](../../../subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ecm.c)及[NCM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ncm.c)供相对路径跟踪，版本可能与官网不同。本批未构建固件、连接串口或执行 USB 网络通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P175_CDC头部功能描述符.md) · [返回大纲](大纲.md) · [下一章](P177_CDC呼叫管理功能描述符.md)
