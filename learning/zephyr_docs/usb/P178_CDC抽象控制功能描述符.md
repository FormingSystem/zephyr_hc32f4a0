---
id: learning.zephyr-docs.usb.api-178
title: CDC抽象控制功能描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcdc__acm__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- Copyright (c) 2025 - 2026 NXP -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第178章\_CDC抽象控制功能描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcdc__acm__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 178.1\_阅读说明与来源

译注：本组说明 USB 通信设备类（Communications Device Class，CDC）的协议常量和数据结构。抽象控制模型（Abstract Control Model，ACM）用于相关串行通信功能；以太网控制模型（Ethernet Control Model，ECM）与网络控制模型（Network Control Model，NCM）用于网络功能。原文只列声明的字段按原样保留，源码补充明确标为译注；[本册大纲](大纲.md)列出相关驱动说明和示例。

抽象控制管理功能描述符（Abstract Control Management Functional Descriptor）。

```c
#include <zephyr/usb/class/usb_cdc.h>
```

抽象控制管理功能描述符（Abstract Control Management Functional Descriptor）。

## 178.2\_数据成员（Data Fields）

<a id="r_a665260ce8cc55e35c941078987f92366"></a>

```c
uint8_t bFunctionLength
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bFunctionLength](P178_CDC抽象控制功能描述符.md#a665260ce8cc55e35c941078987f92366)。

<a id="r_ab62800772430a82673004fcaac13c071"></a>

```c
uint8_t bDescriptorType
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P178_CDC抽象控制功能描述符.md#ab62800772430a82673004fcaac13c071)。

<a id="r_ae1011a0e1520193be5c1fb0fe442915e"></a>

```c
uint8_t bDescriptorSubtype
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorSubtype](P178_CDC抽象控制功能描述符.md#ae1011a0e1520193be5c1fb0fe442915e)。

<a id="r_a3066a08cbc5f0747d435a13ee4f22d14"></a>

```c
uint8_t bmCapabilities
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bmCapabilities](P178_CDC抽象控制功能描述符.md#a3066a08cbc5f0747d435a13ee4f22d14)。

## 178.3\_详细说明（Detailed Documentation）

<a id="ae1011a0e1520193be5c1fb0fe442915e"></a>

### 178.3.1\_`bDescriptorSubtype`

```c
uint8_t cdc_acm_descriptor::bDescriptorSubtype
```

<a id="ab62800772430a82673004fcaac13c071"></a>

### 178.3.2\_`bDescriptorType`

```c
uint8_t cdc_acm_descriptor::bDescriptorType
```

<a id="a665260ce8cc55e35c941078987f92366"></a>

### 178.3.3\_`bFunctionLength`

```c
uint8_t cdc_acm_descriptor::bFunctionLength
```

<a id="a3066a08cbc5f0747d435a13ee4f22d14"></a>

### 178.3.4\_`bmCapabilities`

```c
uint8_t cdc_acm_descriptor::bmCapabilities
```

> 译注（源码核对）：原页只给出声明，没有逐位说明。当前 ACM 描述符模板填写 `BIT(1)`，但仅凭字段名或这个初始值不能推定支持所有类请求；应同时核对 usbd_cdc_acm_ctd() 的请求处理与规范。

## 178.4\_源码跟踪与使用边界

译注依据保存的[官方 CDC 公共头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_cdc.h)、[ACM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ecm.c)和[NCM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ncm.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[公共头文件](../../../include/zephyr/usb/class/usb_cdc.h)、[ACM 源码](../../../subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ecm.c)及[NCM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ncm.c)供相对路径跟踪，版本可能与官网不同。本批未构建固件、连接串口或执行 USB 网络通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P177_CDC呼叫管理功能描述符.md) · [返回大纲](大纲.md) · [下一章](P179_CDC线路编码结构.md)
