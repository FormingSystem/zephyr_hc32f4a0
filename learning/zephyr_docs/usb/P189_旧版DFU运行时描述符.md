---
id: learning.zephyr-docs.usb.api-189
title: 旧版DFU运行时描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdfu__runtime__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2015,2016 Intel Corporation. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第189章\_旧版DFU运行时描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdfu__runtime__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 189.1\_阅读说明与来源

译注：本组补齐设备固件升级（Device Firmware Upgrade，DFU）的头文件参考、协议状态和功能描述符，分别标明旧版设备栈与新版设备栈。镜像定义宏及回调说明见[设备固件升级 API](P062_USB设备固件升级API.md)和[镜像结构](P063_USB固件升级镜像结构.md)；本页不会仅凭描述符字段推定目标板已具备升级能力。

运行时功能描述符（Run-Time Functional Descriptor）。

```c
#include <zephyr/usb/class/usb_dfu.h>
```

运行时功能描述符（Run-Time Functional Descriptor）。

## 189.2\_数据成员（Data Fields）

<a id="r_a0eeecced453c285febca7a9d867c7241"></a>

```c
uint8_t bLength
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P189_旧版DFU运行时描述符.md#a0eeecced453c285febca7a9d867c7241)。

<a id="r_a5464341cf3c706af93de58c6db5edfb9"></a>

```c
uint8_t bDescriptorType
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P189_旧版DFU运行时描述符.md#a5464341cf3c706af93de58c6db5edfb9)。

<a id="r_aa8d5f353530adf846b14e88c97095a50"></a>

```c
uint8_t bmAttributes
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bmAttributes](P189_旧版DFU运行时描述符.md#aa8d5f353530adf846b14e88c97095a50)。

<a id="r_adaf32d218daf9fc74a6639845355cd9b"></a>

```c
uint16_t wDetachTimeOut
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wDetachTimeOut](P189_旧版DFU运行时描述符.md#adaf32d218daf9fc74a6639845355cd9b)。

<a id="r_a86312a99ed7c89eb027ca3e35b7b32e5"></a>

```c
uint16_t wTransferSize
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wTransferSize](P189_旧版DFU运行时描述符.md#a86312a99ed7c89eb027ca3e35b7b32e5)。

<a id="r_a3dca4dc35930794eaa0ac03522949048"></a>

```c
uint16_t bcdDFUVersion
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bcdDFUVersion](P189_旧版DFU运行时描述符.md#a3dca4dc35930794eaa0ac03522949048)。

## 189.3\_详细说明（Detailed Documentation）

<a id="a3dca4dc35930794eaa0ac03522949048"></a>

### 189.3.1\_`bcdDFUVersion`

```c
uint16_t dfu_runtime_descriptor::bcdDFUVersion
```

<a id="a5464341cf3c706af93de58c6db5edfb9"></a>

### 189.3.2\_`bDescriptorType`

```c
uint8_t dfu_runtime_descriptor::bDescriptorType
```

<a id="a0eeecced453c285febca7a9d867c7241"></a>

### 189.3.3\_`bLength`

```c
uint8_t dfu_runtime_descriptor::bLength
```

> 译注（源码核对）：原始类型名为 dfu_runtime_descriptor，当前旧版实现同时在运行时和 DFU 模式的描述符中使用它。新设备栈使用另一类型 usb_dfu_descriptor；即使字段对应，也不能仅替换类型名就认为完成了整套设备栈迁移。

<a id="aa8d5f353530adf846b14e88c97095a50"></a>

### 189.3.4\_`bmAttributes`

```c
uint8_t dfu_runtime_descriptor::bmAttributes
```

<a id="adaf32d218daf9fc74a6639845355cd9b"></a>

### 189.3.5\_`wDetachTimeOut`

```c
uint16_t dfu_runtime_descriptor::wDetachTimeOut
```

<a id="a86312a99ed7c89eb027ca3e35b7b32e5"></a>

### 189.3.6\_`wTransferSize`

```c
uint16_t dfu_runtime_descriptor::wTransferSize
```

> 译注（源码核对）：旧版代码以 sys_cpu_to_le16(USB_DFU_MAX_XFER_SIZE) 初始化此字段。上传时还把主机请求的长度限制到请求缓冲区大小；不能按主机任意请求长度假定缓冲区总是足够。

## 189.4\_源码跟踪与使用边界

译注依据保存的[旧版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_dfu.h)、[新版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_dfu.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_dfu.c)及[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/dfu/usb_dfu.c)，摘要见[来源记录](../SOURCES.md)。仓库内[旧版头文件](../../../include/zephyr/usb/class/usb_dfu.h)、[新版头文件](../../../include/zephyr/usb/class/usbd_dfu.h)、[新版实现](../../../subsys/usb/device_next/class/usbd_dfu.c)与[旧版实现](../../../subsys/usb/device/class/dfu/usb_dfu.c)用于相对路径跟踪，版本可能与官网不同。

> 译注：本页属于已弃用的旧版 DFU 接口，保留用于阅读和迁移对照；新实现从[新版 DFU API](P062_USB设备固件升级API.md)阅读。

本批未构建固件、执行镜像下载、擦写 Flash 或验证重启后的镜像。

## 189.5\_原始版权与许可

以下保留所依据头文件的原始许可声明。

```c
/* SPDX-License-Identifier: BSD-3-Clause */

/***************************************************************************
 *
 * Copyright (c) 2015,2016 Intel Corporation.
 * Copyright (c) 2017 PHYTEC Messtechnik GmbH
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * * Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 * * Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in
 * the documentation and/or other materials provided with the
 * distribution.
 * * Neither the name of Intel Corporation nor the names of its
 * contributors may be used to endorse or promote products derived
 * from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 ***************************************************************************/
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P188_DFU设备类头文件源码.md) · [返回大纲](大纲.md) · [下一章](P190_蓝牙HCIUSB控制器示例.md)
