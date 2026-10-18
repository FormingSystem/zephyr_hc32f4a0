---
id: learning.zephyr-docs.usb.api-159
title: 旧版USB接口请求配置
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__interface__cfg__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第159章\_旧版USB接口请求配置

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__interface__cfg__data.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 159.1\_阅读说明与来源

译注：本页说明旧版USB设备栈核心层（USB Device Core Layer）接口。它位于usb_dc控制器接口之上；原文的弃用标记、宏展开与全部声明均保留。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 接口配置（Interface Configuration）。

```c
#include <zephyr/usb/usb_device.h>
```

USB 接口配置（Interface Configuration）。

此结构包含 USB 接口配置。

## 159.2\_数据成员（Data Fields）

<a id="r_a144ed5ba67d1adb8dbb1d936ac440272"></a>

```c
usb_request_handler class_handler
```

USB 类专用控制通信（端点 0，EP 0）的处理函数。

相关声明：[usb_request_handler](P155_旧版USB设备栈核心API.md#gaddacbff094a41c885c3041af72fa6804)、[class_handler](P159_旧版USB接口请求配置.md#a144ed5ba67d1adb8dbb1d936ac440272)。

<a id="r_a2d5d65d41cef609173287161797318d2"></a>

```c
usb_request_handler vendor_handler
```

USB 厂商专用命令（Vendor-Specific Command）的处理函数。

相关声明：[usb_request_handler](P155_旧版USB设备栈核心API.md#gaddacbff094a41c885c3041af72fa6804)、[vendor_handler](P159_旧版USB接口请求配置.md#a2d5d65d41cef609173287161797318d2)。

<a id="r_a117a1a88c02048ee43994d3e5a4ce922"></a>

```c
usb_request_handler custom_handler
```

请求交给第 9 章（Chapter 9）请求处理函数之前，自定义请求处理函数有优先处理的机会。

相关声明：[usb_request_handler](P155_旧版USB设备栈核心API.md#gaddacbff094a41c885c3041af72fa6804)、[custom_handler](P159_旧版USB接口请求配置.md#a117a1a88c02048ee43994d3e5a4ce922)。

## 159.3\_详细说明（Detailed Documentation）

<a id="a144ed5ba67d1adb8dbb1d936ac440272"></a>

### 159.3.1\_`class_handler`

```c
usb_request_handler usb_interface_cfg_data::class_handler
```

USB 类专用控制通信（端点 0，EP 0）的处理函数。

<a id="a117a1a88c02048ee43994d3e5a4ce922"></a>

### 159.3.2\_`custom_handler`

```c
usb_request_handler usb_interface_cfg_data::custom_handler
```

请求交给第 9 章（Chapter 9）请求处理函数之前，自定义请求处理函数有优先处理的机会。

成功时返回 0；如果自定义处理函数未处理该请求，需要转由 USB 核心栈处理，则返回 -EINVAL；其他错误码表示自定义处理函数内部发生失败。

> 译注（源码核对）：此处-EINVAL按原接口约定表示交回核心栈继续处理，与其他错误返回的含义不同；实现自定义处理器时不能把所有不认识的请求都统一当成已经处理成功。

<a id="a2d5d65d41cef609173287161797318d2"></a>

### 159.3.3\_`vendor_handler`

```c
usb_request_handler usb_interface_cfg_data::vendor_handler
```

USB 厂商专用命令（Vendor-Specific Command）的处理函数。

## 159.4\_源码跟踪与使用边界

译注依据保存的[官方usb_device头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_device.h)、[旧版设备栈核心](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_device.c)、[传输实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_transfer.c)与[BOS管理实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/bos.c)，摘要见[来源记录](../SOURCES.md)。本仓库[公共头文件](../../../include/zephyr/usb/usb_device.h)与[传输实现](../../../subsys/usb/device/usb_transfer.c)可用于相对路径源码跟踪，版本可能与网页不同。对应控制器接口见[usb_dc参考](P152_旧版USB控制器驱动API.md)；本批没有构建、烧录或执行USB传输测试。

## 159.5\_原始版权与许可

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

[上一章](P158_旧版USB设备栈头文件接口.md) · [返回大纲](大纲.md) · [下一章](P160_USB控制请求包.md)
