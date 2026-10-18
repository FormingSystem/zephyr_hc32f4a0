---
id: learning.zephyr-docs.usb.api-182
title: CDC网络控制模型描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcdc__ncm__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- Copyright (c) 2025 - 2026 NXP -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第182章\_CDC网络控制模型描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcdc__ncm__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 182.1\_阅读说明与来源

译注：本组说明 USB 通信设备类（Communications Device Class，CDC）的协议常量和数据结构。抽象控制模型（Abstract Control Model，ACM）用于相关串行通信功能；以太网控制模型（Ethernet Control Model，ECM）与网络控制模型（Network Control Model，NCM）用于网络功能。原文只列声明的字段按原样保留，源码补充明确标为译注；[本册大纲](大纲.md)列出相关驱动说明和示例。

以太网网络控制模型描述符（Ethernet Network Control Model，NCM Descriptor）。

```c
#include <zephyr/usb/class/usb_cdc.h>
```

以太网网络控制模型描述符（Ethernet Network Control Model，NCM Descriptor）。

## 182.2\_数据成员（Data Fields）

<a id="r_a932a73d95abf90a0ba7f0de3e1760375"></a>

```c
uint8_t bFunctionLength
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bFunctionLength](P182_CDC网络控制模型描述符.md#a932a73d95abf90a0ba7f0de3e1760375)。

<a id="r_a9dea58db91413ebcff65151e006a3b2c"></a>

```c
uint8_t bDescriptorType
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P182_CDC网络控制模型描述符.md#a9dea58db91413ebcff65151e006a3b2c)。

<a id="r_a9fb11a778a65e5e8538619467cd6c6d6"></a>

```c
uint8_t bDescriptorSubtype
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorSubtype](P182_CDC网络控制模型描述符.md#a9fb11a778a65e5e8538619467cd6c6d6)。

<a id="r_aa9b5bd71a73783e4a3c85a1d39f9def3"></a>

```c
uint16_t bcdNcmVersion
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bcdNcmVersion](P182_CDC网络控制模型描述符.md#aa9b5bd71a73783e4a3c85a1d39f9def3)。

<a id="r_a8a88e3d7d2b36876a38fa8025118f069"></a>

```c
uint8_t bmNetworkCapabilities
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bmNetworkCapabilities](P182_CDC网络控制模型描述符.md#a8a88e3d7d2b36876a38fa8025118f069)。

## 182.3\_详细说明（Detailed Documentation）

<a id="aa9b5bd71a73783e4a3c85a1d39f9def3"></a>

### 182.3.1\_`bcdNcmVersion`

```c
uint16_t cdc_ncm_descriptor::bcdNcmVersion
```

> 译注（源码核对）：当前 NCM 模板使用 `sys_cpu_to_le16(0x100)` 初始化版本字段，与 CDC 通用头部的 bcdCDC 分别保存。

<a id="a9fb11a778a65e5e8538619467cd6c6d6"></a>

### 182.3.2\_`bDescriptorSubtype`

```c
uint8_t cdc_ncm_descriptor::bDescriptorSubtype
```

<a id="a9dea58db91413ebcff65151e006a3b2c"></a>

### 182.3.3\_`bDescriptorType`

```c
uint8_t cdc_ncm_descriptor::bDescriptorType
```

<a id="a932a73d95abf90a0ba7f0de3e1760375"></a>

### 182.3.4\_`bFunctionLength`

```c
uint8_t cdc_ncm_descriptor::bFunctionLength
```

<a id="a8a88e3d7d2b36876a38fa8025118f069"></a>

### 182.3.5\_`bmNetworkCapabilities`

```c
uint8_t cdc_ncm_descriptor::bmNetworkCapabilities
```

> 译注（源码核对）：网络能力位图（Network Capabilities Bitmap）说明相应功能支持的请求。当前 NCM 模板只设置 USB_CDC_NCM_NCAP_ETH_FILTER；头文件定义六个能力位，不表示默认把六项能力全部打开。

## 182.4\_源码跟踪与使用边界

译注依据保存的[官方 CDC 公共头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_cdc.h)、[ACM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ecm.c)和[NCM 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_cdc_ncm.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[公共头文件](../../../include/zephyr/usb/class/usb_cdc.h)、[ACM 源码](../../../subsys/usb/device_next/class/usbd_cdc_acm.c)、[ECM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ecm.c)及[NCM 源码](../../../subsys/usb/device_next/class/usbd_cdc_ncm.c)供相对路径跟踪，版本可能与官网不同。本批未构建固件、连接串口或执行 USB 网络通信测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P181_CDC以太网功能描述符.md) · [返回大纲](大纲.md) · [下一章](P183_CDC公共头文件源码.md)
