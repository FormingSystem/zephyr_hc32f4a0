---
id: learning.zephyr-docs.usb.api-156
title: 旧版USB功能配置结构
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__cfg__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第156章\_旧版USB功能配置结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__cfg__data.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 156.1\_阅读说明与来源

译注：本页说明旧版USB设备栈核心层（USB Device Core Layer）接口。它位于usb_dc控制器接口之上；原文的弃用标记、宏展开与全部声明均保留。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 设备配置（Device Configuration）。

```c
#include <zephyr/usb/usb_device.h>
```

USB 设备配置（Device Configuration）。

应用以给定参数实例化此结构，并通过 usb_set_config 函数加入配置。调用该函数后再修改此结构会导致未定义行为（Undefined Behavior）；只有调用 usb_deconfig 之后才可以更新此结构。

## 156.2\_数据成员（Data Fields）

<a id="r_a842d4d8a08dd619dd8ee5ccf62ae1e2a"></a>

```c
const uint8_t * usb_device_description
```

USB 设备描述，参见 [原文所引设备描述符说明](http://www.beyondlogic.org/usbnutshell/usb5.shtml#DeviceDescriptors)。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usb_device_description](P156_旧版USB功能配置结构.md#a842d4d8a08dd619dd8ee5ccf62ae1e2a)。

<a id="r_ade7cc5e164a82a86d7c57d7a2a4ef306"></a>

```c
void * interface_descriptor
```

指向接口描述符。

相关声明：[interface_descriptor](P156_旧版USB功能配置结构.md#ade7cc5e164a82a86d7c57d7a2a4ef306)。

<a id="r_a3ea73c7ea8759d3637852ff2d02ee96b"></a>

```c
usb_interface_config interface_config
```

用于接口运行时配置（Runtime Configuration）的函数。

相关声明：[usb_interface_config](P155_旧版USB设备栈核心API.md#ga3439af9464471b3acdc21f4359efb53a)、[interface_config](P156_旧版USB功能配置结构.md#a3ea73c7ea8759d3637852ff2d02ee96b)。

<a id="r_aaf33be8983eb59105beb2d6e551ff195"></a>

```c
void(* cb_usb_status )(struct usb_cfg_data *cfg, enum usb_dc_status_code cb_status, const uint8_t *param)
```

用于接收 USB 连接状态变化通知的回调。

相关声明：[cb_usb_status](P156_旧版USB功能配置结构.md#aaf33be8983eb59105beb2d6e551ff195)、[usb_cfg_data](P156_旧版USB功能配置结构.md)、[usb_dc_status_code](P152_旧版USB控制器驱动API.md#gac09e3e0af1a2b41a5bfbad91f900baf7)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_a84b41f3ddabab946ed165c03e3812e10"></a>

```c
struct usb_interface_cfg_data interface
```

USB 接口（类）的处理函数及存储空间。

相关声明：[usb_interface_cfg_data](P159_旧版USB接口请求配置.md)、[interface](P156_旧版USB功能配置结构.md#a84b41f3ddabab946ed165c03e3812e10)。

<a id="r_a5e58af56af22ecdf0e2222afc408a33b"></a>

```c
uint8_t num_endpoints
```

设备配置中各端点的数量。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_endpoints](P156_旧版USB功能配置结构.md#a5e58af56af22ecdf0e2222afc408a33b)。

<a id="r_adbd7a747db040b54d047c48bed2f50c3"></a>

```c
struct usb_ep_cfg_data * endpoint
```

指向端点结构数组，长度等于与设备描述关联的端点数量，不包括控制端点。

相关声明：[usb_ep_cfg_data](P157_旧版USB端点回调配置.md)、[endpoint](P156_旧版USB功能配置结构.md#adbd7a747db040b54d047c48bed2f50c3)。

## 156.3\_详细说明（Detailed Documentation）

<a id="aaf33be8983eb59105beb2d6e551ff195"></a>

### 156.3.1\_`cb_usb_status`

```c
void(* usb_cfg_data::cb_usb_status) (struct usb_cfg_data *cfg, enum usb_dc_status_code cb_status, const uint8_t *param)
```

用于接收 USB 连接状态变化通知的回调。

<a id="adbd7a747db040b54d047c48bed2f50c3"></a>

### 156.3.2\_`endpoint`

```c
struct usb_ep_cfg_data* usb_cfg_data::endpoint
```

指向端点结构数组，长度等于与设备描述关联的端点数量，不包括控制端点。

> 译注（源码核对）：这里的数组元素是端点地址与回调配置usb_ep_cfg_data，不是控制器层包含ep_mps及ep_type的usb_dc_ep_cfg_data；两者用途和结构布局不同。

<a id="a84b41f3ddabab946ed165c03e3812e10"></a>

### 156.3.3\_`interface`

```c
struct usb_interface_cfg_data usb_cfg_data::interface
```

USB 接口（类）的处理函数及存储空间。

> 译注（源码核对）：原结构说明提到通过usb_set_config加入配置；当前usb_set_config参数实际是描述符字节表指针，usb_cfg_data对象则由USBD_DEFINE_CFG_DATA放入可遍历链接段。不能把usb_cfg_data指针强制转换后作为描述符表传入。

<a id="a3ea73c7ea8759d3637852ff2d02ee96b"></a>

### 156.3.4\_`interface_config`

```c
usb_interface_config usb_cfg_data::interface_config
```

用于接口运行时配置（Runtime Configuration）的函数。

<a id="ade7cc5e164a82a86d7c57d7a2a4ef306"></a>

### 156.3.5\_`interface_descriptor`

```c
void* usb_cfg_data::interface_descriptor
```

指向接口描述符。

<a id="a5e58af56af22ecdf0e2222afc408a33b"></a>

### 156.3.6\_`num_endpoints`

```c
uint8_t usb_cfg_data::num_endpoints
```

设备配置中各端点的数量。

<a id="a842d4d8a08dd619dd8ee5ccf62ae1e2a"></a>

### 156.3.7\_`usb_device_description`

```c
const uint8_t* usb_cfg_data::usb_device_description
```

USB 设备描述，参见 [原文所引设备描述符说明](http://www.beyondlogic.org/usbnutshell/usb5.shtml#DeviceDescriptors)。

## 156.4\_源码跟踪与使用边界

译注依据保存的[官方usb_device头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_device.h)、[旧版设备栈核心](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_device.c)、[传输实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_transfer.c)与[BOS管理实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/bos.c)，摘要见[来源记录](../SOURCES.md)。本仓库[公共头文件](../../../include/zephyr/usb/usb_device.h)与[传输实现](../../../subsys/usb/device/usb_transfer.c)可用于相对路径源码跟踪，版本可能与网页不同。对应控制器接口见[usb_dc参考](P152_旧版USB控制器驱动API.md)；本批没有构建、烧录或执行USB传输测试。

## 156.5\_原始版权与许可

本页声明与宏源自采用BSD-3-Clause许可的usb_device.h；译文集通用许可不覆盖该独立许可。以下逐字保留原始署名、再分发条件与免责声明，代码标识及作者联系方式不改写。

```c
/* SPDX-License-Identifier: BSD-3-Clause */

/*
 *  LPCUSB, an USB device driver for LPC microcontrollers
 *  Copyright (C) 2006 Bertrik Sikken (bertrik@sikken.nl)
 *  Copyright (c) 2016 Intel Corporation
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions are met:
 *
 *  1. Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *  2. Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *  3. The name of the author may not be used to endorse or promote products
 *     derived from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 *  IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 *  OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 *  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 *  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 *  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 *  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 *  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P155_旧版USB设备栈核心API.md) · [返回大纲](大纲.md) · [下一章](P157_旧版USB端点回调配置.md)
