---
id: learning.zephyr-docs.usb.api-177
title: CDC呼叫管理功能描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcdc__cm__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- Copyright (c) 2025 - 2026 NXP -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第177章\_CDC呼叫管理功能描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcdc__cm__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 177.1\_阅读说明与来源

译注：本组说明 USB 通信设备类（Communications Device Class，CDC）的协议常量和数据结构。抽象控制模型（Abstract Control Model，ACM）用于相关串行通信功能；以太网控制模型（Ethernet Control Model，ECM）与网络控制模型（Network Control Model，NCM）用于网络功能。原文只列声明的字段按原样保留，源码补充明确标为译注；[本册大纲](大纲.md)列出相关驱动说明和示例。

呼叫管理功能描述符（Call Management Functional Descriptor）。

```c
#include <zephyr/usb/class/usb_cdc.h>
```

呼叫管理功能描述符（Call Management Functional Descriptor）。

## 177.2\_数据成员（Data Fields）

<a id="r_a578a2a39c7c80de58cb7d952f8decd22"></a>

```c
uint8_t bFunctionLength
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bFunctionLength](P177_CDC呼叫管理功能描述符.md#a578a2a39c7c80de58cb7d952f8decd22)。

<a id="r_ad40616645c5b28754300594b43805a1f"></a>

```c
uint8_t bDescriptorType
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P177_CDC呼叫管理功能描述符.md#ad40616645c5b28754300594b43805a1f)。

<a id="r_a908003360bca9ab79f55d80a2fc7aa24"></a>

```c
uint8_t bDescriptorSubtype
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorSubtype](P177_CDC呼叫管理功能描述符.md#a908003360bca9ab79f55d80a2fc7aa24)。

<a id="r_aabbca6f88b936659124aa28264054b6d"></a>

```c
uint8_t bmCapabilities
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bmCapabilities](P177_CDC呼叫管理功能描述符.md#aabbca6f88b936659124aa28264054b6d)。

<a id="r_a0a29f8dfe1dd9758f210b63d7a87bdc6"></a>

```c
uint8_t bDataInterface
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDataInterface](P177_CDC呼叫管理功能描述符.md#a0a29f8dfe1dd9758f210b63d7a87bdc6)。

## 177.3\_详细说明（Detailed Documentation）

<a id="a0a29f8dfe1dd9758f210b63d7a87bdc6"></a>

### 177.3.1\_`bDataInterface`

```c
uint8_t cdc_cm_descriptor::bDataInterface
```

> 译注（源码核对）：当前 ACM 初始化把此字段设置为数据接口的实际 `bInterfaceNumber`；它是接口编号，不是端点地址或端点数量。呼叫管理能力位图 `bmCapabilities` 是同一描述符中的另一个字段。

<a id="a908003360bca9ab79f55d80a2fc7aa24"></a>

### 177.3.2\_`bDescriptorSubtype`

```c
uint8_t cdc_cm_descriptor::bDescriptorSubtype
```

<a id="ad40616645c5b28754300594b43805a1f"></a>

### 177.3.3\_`bDescriptorType`

```c
uint8_t cdc_cm_descriptor::bDescriptorType
```

<a id="a578a2a39c7c80de58cb7d952f8decd22"></a>

### 177.3.4\_`bFunctionLength`

```c
uint8_t cdc_cm_descriptor::bFunctionLength
```

<a id="aabbca6f88b936659124aa28264054b6d"></a>

### 177.3.5\_`bmCapabilities`

```c
uint8_t cdc_cm_descriptor::bmCapabilities
```

## 177.4\_源码跟踪与使用边界

译注依据保存的[官方 CDC 公共头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_cdc.h)、[ACM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ecm.c)和[NCM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ncm.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[公共头文件](../../../include/zephyr/usb/class/usb_cdc.h)、[ACM 源码](../../../subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ecm.c)及[NCM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ncm.c)供相对路径跟踪，版本可能与官网不同。本批未构建固件、连接串口或执行 USB 网络通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P176_CDC联合接口功能描述符.md) · [返回大纲](大纲.md) · [下一章](P178_CDC抽象控制功能描述符.md)
