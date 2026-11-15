---
id: learning.zephyr-docs.usb.api-180
title: CDC串行状态通知
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcdc__acm__notification.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- Copyright (c) 2025 - 2026 NXP -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第180章\_CDC串行状态通知

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcdc__acm__notification.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 180.1\_阅读说明与来源

译注：本组说明 USB 通信设备类（Communications Device Class，CDC）的协议常量和数据结构。抽象控制模型（Abstract Control Model，ACM）用于相关串行通信功能；以太网控制模型（Ethernet Control Model，ECM）与网络控制模型（Network Control Model，NCM）用于网络功能。原文只列声明的字段按原样保留，源码补充明确标为译注；[本册大纲](大纲.md)列出相关驱动说明和示例。

串行状态（SerialState）通知使用的数据结构。

```c
#include <zephyr/usb/class/usb_cdc.h>
```

串行状态（SerialState）通知使用的数据结构。

## 180.2\_数据成员（Data Fields）

<a id="r_a57b007a8ec893d660e6ec8a1b25f7dd3"></a>

```c
uint8_t bmRequestType
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bmRequestType](P180_CDC串行状态通知.md#a57b007a8ec893d660e6ec8a1b25f7dd3)。

<a id="r_af24dae76a280c008e40a0d031171235c"></a>

```c
uint8_t bNotificationType
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bNotificationType](P180_CDC串行状态通知.md#af24dae76a280c008e40a0d031171235c)。

<a id="r_a3bf290bc6e851331e93bedf49ae5dbe0"></a>

```c
uint16_t wValue
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wValue](P180_CDC串行状态通知.md#a3bf290bc6e851331e93bedf49ae5dbe0)。

<a id="r_a290717590343376c8f1f9a865cb4b0ae"></a>

```c
uint16_t wIndex
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wIndex](P180_CDC串行状态通知.md#a290717590343376c8f1f9a865cb4b0ae)。

<a id="r_af2f8fbceeaa9a3ad0ae1330b8f82bff2"></a>

```c
uint16_t wLength
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wLength](P180_CDC串行状态通知.md#af2f8fbceeaa9a3ad0ae1330b8f82bff2)。

<a id="r_a5666402ce9fbe5fad5f80592aa6f53ec"></a>

```c
uint16_t data
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[data](P180_CDC串行状态通知.md#a5666402ce9fbe5fad5f80592aa6f53ec)。

## 180.3\_详细说明（Detailed Documentation）

<a id="a57b007a8ec893d660e6ec8a1b25f7dd3"></a>

### 180.3.1\_`bmRequestType`

```c
uint8_t cdc_acm_notification::bmRequestType
```

<a id="af24dae76a280c008e40a0d031171235c"></a>

### 180.3.2\_`bNotificationType`

```c
uint8_t cdc_acm_notification::bNotificationType
```

<a id="a5666402ce9fbe5fad5f80592aa6f53ec"></a>

### 180.3.3\_`data`

```c
uint16_t cdc_acm_notification::data
```

> 译注（源码核对）：`cdc_acm_send_notification()` 将串行状态位图以 `sys_cpu_to_le16(serial_state)` 写入 data，并将 wLength 设为 2 字节。wLength 只描述通知数据部分，不是整个通知结构的长度。

<a id="a290717590343376c8f1f9a865cb4b0ae"></a>

### 180.3.4\_`wIndex`

```c
uint16_t cdc_acm_notification::wIndex
```

> 译注（源码核对）：按所保存的当前实现，cdc_acm_send_notification() 初始化 `wIndex = 0`；此处只记录源码现状，不据此推出所有 CDC 实例的接口编号都固定为 0。

<a id="af2f8fbceeaa9a3ad0ae1330b8f82bff2"></a>

### 180.3.5\_`wLength`

```c
uint16_t cdc_acm_notification::wLength
```

<a id="a3bf290bc6e851331e93bedf49ae5dbe0"></a>

### 180.3.6\_`wValue`

```c
uint16_t cdc_acm_notification::wValue
```

## 180.4\_源码跟踪与使用边界

译注依据保存的[官方 CDC 公共头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_cdc.h)、[ACM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ecm.c)和[NCM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ncm.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[公共头文件](../../../include/zephyr/usb/class/usb_cdc.h)、[ACM 源码](../../../subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ecm.c)及[NCM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ncm.c)供相对路径跟踪，版本可能与官网不同。本批未构建固件、连接串口或执行 USB 网络通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P179_CDC线路编码结构.md) · [返回大纲](大纲.md) · [下一章](P181_CDC以太网功能描述符.md)
