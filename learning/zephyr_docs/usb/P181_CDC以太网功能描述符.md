---
id: learning.zephyr-docs.usb.api-181
title: CDC以太网功能描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcdc__ecm__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- Copyright (c) 2025 - 2026 NXP -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第181章\_CDC以太网功能描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcdc__ecm__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 181.1\_阅读说明与来源

译注：本组说明 USB 通信设备类（Communications Device Class，CDC）的协议常量和数据结构。抽象控制模型（Abstract Control Model，ACM）用于相关串行通信功能；以太网控制模型（Ethernet Control Model，ECM）与网络控制模型（Network Control Model，NCM）用于网络功能。原文只列声明的字段按原样保留，源码补充明确标为译注；[本册大纲](大纲.md)列出相关驱动说明和示例。

以太网网络功能描述符（Ethernet Networking Functional Descriptor）。

```c
#include <zephyr/usb/class/usb_cdc.h>
```

以太网网络功能描述符（Ethernet Networking Functional Descriptor）。

## 181.2\_数据成员（Data Fields）

<a id="r_aa5cfb3a02e9818cf3faaff1dbb9dd487"></a>

```c
uint8_t bFunctionLength
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bFunctionLength](P181_CDC以太网功能描述符.md#aa5cfb3a02e9818cf3faaff1dbb9dd487)。

<a id="r_ae000bdad185ca5af3674274ea3fa45d6"></a>

```c
uint8_t bDescriptorType
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P181_CDC以太网功能描述符.md#ae000bdad185ca5af3674274ea3fa45d6)。

<a id="r_aaf95074ec751f227a33317325567c890"></a>

```c
uint8_t bDescriptorSubtype
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorSubtype](P181_CDC以太网功能描述符.md#aaf95074ec751f227a33317325567c890)。

<a id="r_ad43f97e428ef743d4655a1e91b91478d"></a>

```c
uint8_t iMACAddress
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iMACAddress](P181_CDC以太网功能描述符.md#ad43f97e428ef743d4655a1e91b91478d)。

<a id="r_a3a7b901bef04212b217a69d055e37e66"></a>

```c
uint32_t bmEthernetStatistics
```



相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bmEthernetStatistics](P181_CDC以太网功能描述符.md#a3a7b901bef04212b217a69d055e37e66)。

<a id="r_afdf7f4478515917b1ed653118e7a8540"></a>

```c
uint16_t wMaxSegmentSize
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wMaxSegmentSize](P181_CDC以太网功能描述符.md#afdf7f4478515917b1ed653118e7a8540)。

<a id="r_a196fcac7b1c9bf0f2b42a6d4ccb48de6"></a>

```c
uint16_t wNumberMCFilters
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wNumberMCFilters](P181_CDC以太网功能描述符.md#a196fcac7b1c9bf0f2b42a6d4ccb48de6)。

<a id="r_aed687a9629eb3c793af9260db407a136"></a>

```c
uint8_t bNumberPowerFilters
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bNumberPowerFilters](P181_CDC以太网功能描述符.md#aed687a9629eb3c793af9260db407a136)。

## 181.3\_详细说明（Detailed Documentation）

<a id="aaf95074ec751f227a33317325567c890"></a>

### 181.3.1\_`bDescriptorSubtype`

```c
uint8_t cdc_ecm_descriptor::bDescriptorSubtype
```

<a id="ae000bdad185ca5af3674274ea3fa45d6"></a>

### 181.3.2\_`bDescriptorType`

```c
uint8_t cdc_ecm_descriptor::bDescriptorType
```

<a id="aa5cfb3a02e9818cf3faaff1dbb9dd487"></a>

### 181.3.3\_`bFunctionLength`

```c
uint8_t cdc_ecm_descriptor::bFunctionLength
```

<a id="a3a7b901bef04212b217a69d055e37e66"></a>

### 181.3.4\_`bmEthernetStatistics`

```c
uint32_t cdc_ecm_descriptor::bmEthernetStatistics
```

> 译注（源码核对）：这是描述符中的统计能力字段。公共头文件同时提供统计请求的选择器代码；存在某个选择器宏并不自动表示设备实现了该项统计。当前 ECM 与 NCM 描述符模板均把该能力字段初始化为 0。

<a id="aed687a9629eb3c793af9260db407a136"></a>

### 181.3.5\_`bNumberPowerFilters`

```c
uint8_t cdc_ecm_descriptor::bNumberPowerFilters
```

<a id="ad43f97e428ef743d4655a1e91b91478d"></a>

### 181.3.6\_`iMACAddress`

```c
uint8_t cdc_ecm_descriptor::iMACAddress
```

> 译注（源码核对）：这是 MAC 地址字符串描述符的索引（String Descriptor Index），不是直接存放六个地址字节的数组。当前 ECM 初始化添加对应字符串描述符后，用 usbd_str_desc_get_idx() 取得索引填入。

<a id="afdf7f4478515917b1ed653118e7a8540"></a>

### 181.3.7\_`wMaxSegmentSize`

```c
uint16_t cdc_ecm_descriptor::wMaxSegmentSize
```

> 译注（源码核对）：当前 ECM/NCM 模板使用 `sys_cpu_to_le16(NET_ETH_MAX_FRAME_SIZE)` 初始化此字段。它描述以太网帧相关的最大段大小，不是 USB 端点的 `wMaxPacketSize`。

<a id="a196fcac7b1c9bf0f2b42a6d4ccb48de6"></a>

### 181.3.8\_`wNumberMCFilters`

```c
uint16_t cdc_ecm_descriptor::wNumberMCFilters
```

## 181.4\_源码跟踪与使用边界

译注依据保存的[官方 CDC 公共头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_cdc.h)、[ACM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ecm.c)和[NCM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ncm.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[公共头文件](../../../include/zephyr/usb/class/usb_cdc.h)、[ACM 源码](../../../subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ecm.c)及[NCM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ncm.c)供相对路径跟踪，版本可能与官网不同。本批未构建固件、连接串口或执行 USB 网络通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P180_CDC串行状态通知.md) · [返回大纲](大纲.md) · [下一章](P182_CDC网络控制模型描述符.md)
