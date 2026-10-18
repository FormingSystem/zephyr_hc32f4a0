---
id: learning.zephyr-docs.usb.api-157
title: 旧版USB端点回调配置
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__ep__cfg__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第157章\_旧版USB端点回调配置

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__ep__cfg__data.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 157.1\_阅读说明与来源

译注：本页说明旧版USB设备栈核心层（USB Device Core Layer）接口。它位于usb_dc控制器接口之上；原文的弃用标记、宏展开与全部声明均保留。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 端点配置（Endpoint Configuration）。

```c
#include <zephyr/usb/usb_device.h>
```

USB 端点配置（Endpoint Configuration）。

此结构包含端点配置。

## 157.2\_数据成员（Data Fields）

<a id="r_a5d03244508b6a58d9d0bfb896c2537d1"></a>

```c
usb_ep_callback ep_cb
```

用于通知应用有接收数据可用或发送已完成的回调；应用代码不需要回调时可为 NULL。

相关声明：[usb_ep_callback](P155_旧版USB设备栈核心API.md#ga9a45db26a9be295640ed122533427725)、[ep_cb](P157_旧版USB端点回调配置.md#a5d03244508b6a58d9d0bfb896c2537d1)。

<a id="r_aa87f676a577a8c1605bb9a8fa04f411c"></a>

```c
uint8_t ep_addr
```

设备配置结构中与端点关联的编号：IN EP = 0x80 | <endpoint number>，OUT EP = 0x00 | <endpoint number>。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ep_addr](P157_旧版USB端点回调配置.md#aa87f676a577a8c1605bb9a8fa04f411c)。

## 157.3\_详细说明（Detailed Documentation）

<a id="aa87f676a577a8c1605bb9a8fa04f411c"></a>

### 157.3.1\_`ep_addr`

```c
uint8_t usb_ep_cfg_data::ep_addr
```

设备配置结构中与端点关联的编号：IN EP = 0x80 | <endpoint number>，OUT EP = 0x00 | <endpoint number>。

<a id="a5d03244508b6a58d9d0bfb896c2537d1"></a>

### 157.3.2\_`ep_cb`

```c
usb_ep_callback usb_ep_cfg_data::ep_cb
```

用于通知应用有接收数据可用或发送已完成的回调；应用代码不需要回调时可为 NULL。

## 157.4\_源码跟踪与使用边界

译注依据保存的[官方usb_device头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_device.h)、[旧版设备栈核心](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_device.c)、[传输实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_transfer.c)与[BOS管理实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/bos.c)，摘要见[来源记录](../SOURCES.md)。本仓库[公共头文件](../../../include/zephyr/usb/usb_device.h)与[传输实现](../../../subsys/usb/device/usb_transfer.c)可用于相对路径源码跟踪，版本可能与网页不同。对应控制器接口见[usb_dc参考](P152_旧版USB控制器驱动API.md)；本批没有构建、烧录或执行USB传输测试。

## 157.5\_原始版权与许可

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

[上一章](P156_旧版USB功能配置结构.md) · [返回大纲](大纲.md) · [下一章](P158_旧版USB设备栈头文件接口.md)
