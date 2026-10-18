---
id: learning.zephyr-docs.usb.api-185
title: DFU功能描述符
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__dfu__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2024 Nordic Semiconductor ASA -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第185章\_DFU功能描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__dfu__descriptor.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 185.1\_阅读说明与来源

译注：本组补齐设备固件升级（Device Firmware Upgrade，DFU）的头文件参考、协议状态和功能描述符，分别标明旧版设备栈与新版设备栈。镜像定义宏及回调说明见[设备固件升级 API](P062_USB设备固件升级API.md)和[镜像结构](P063_USB固件升级镜像结构.md)；本页不会仅凭描述符字段推定目标板已具备升级能力。

```c
#include <zephyr/usb/class/usbd_dfu.h>
```

## 185.2\_数据成员（Data Fields）

<a id="r_aaae3ed6f5fc202453e5a295b25c391e0"></a>

```c
uint8_t bLength
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P185_DFU功能描述符.md#aaae3ed6f5fc202453e5a295b25c391e0)。

<a id="r_a545d551fdf9612abab9679ad9092fe21"></a>

```c
uint8_t bDescriptorType
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P185_DFU功能描述符.md#a545d551fdf9612abab9679ad9092fe21)。

<a id="r_a6eda776c2fa8ad9e92da5a9c0771c017"></a>

```c
uint8_t bmAttributes
```



相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bmAttributes](P185_DFU功能描述符.md#a6eda776c2fa8ad9e92da5a9c0771c017)。

<a id="r_ab37985af3ea9985ebe57d04eb7b004b6"></a>

```c
uint16_t wDetachTimeOut
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wDetachTimeOut](P185_DFU功能描述符.md#ab37985af3ea9985ebe57d04eb7b004b6)。

<a id="r_a6f28ae6870039d8ba994a2aed1d6b8b9"></a>

```c
uint16_t wTransferSize
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wTransferSize](P185_DFU功能描述符.md#a6f28ae6870039d8ba994a2aed1d6b8b9)。

<a id="r_ac917f4ae3b4cda852e7e23a1378cc584"></a>

```c
uint16_t bcdDFUVersion
```



相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bcdDFUVersion](P185_DFU功能描述符.md#ac917f4ae3b4cda852e7e23a1378cc584)。

## 185.3\_详细说明（Detailed Documentation）

<a id="ac917f4ae3b4cda852e7e23a1378cc584"></a>

### 185.3.1\_`bcdDFUVersion`

```c
uint16_t usb_dfu_descriptor::bcdDFUVersion
```

> 译注（源码核对）：新版常量 USB_DFU_VERSION 为 0x0110，源码用 sys_cpu_to_le16() 编码到描述符。该字段表示 DFU 规范版本，不是镜像自身的发布版本。

<a id="a545d551fdf9612abab9679ad9092fe21"></a>

### 185.3.2\_`bDescriptorType`

```c
uint8_t usb_dfu_descriptor::bDescriptorType
```

<a id="aaae3ed6f5fc202453e5a295b25c391e0"></a>

### 185.3.3\_`bLength`

```c
uint8_t usb_dfu_descriptor::bLength
```

<a id="a6eda776c2fa8ad9e92da5a9c0771c017"></a>

### 185.3.4\_`bmAttributes`

```c
uint8_t usb_dfu_descriptor::bmAttributes
```

> 译注（源码核对）：新版 dfu_desc 始终设置可下载与设备自行脱离标志；可上传与容忍固件落实阶段（Manifestation）的标志分别由 CONFIG_USBD_DFU_ENABLE_UPLOAD 和 CONFIG_USBD_DFU_MANIFESTATION_TOLERANT 控制。常量存在不表示各能力都已启用。

<a id="ab37985af3ea9985ebe57d04eb7b004b6"></a>

### 185.3.5\_`wDetachTimeOut`

```c
uint16_t usb_dfu_descriptor::wDetachTimeOut
```

> 译注（源码核对）：所保存的新版实现将此字段初始化为 0，旧版描述符则来自 CONFIG_USB_DFU_DETACH_TIMEOUT。结构字段相似并不代表两套设备栈采用完全相同的初始化和切换策略。

<a id="a6f28ae6870039d8ba994a2aed1d6b8b9"></a>

### 185.3.6\_`wTransferSize`

```c
uint16_t usb_dfu_descriptor::wTransferSize
```

> 译注（源码核对）：当前实现用 sys_cpu_to_le16(CONFIG_USBD_DFU_TRANSFER_SIZE) 设置此字段，并将上传请求的 wLength 与它比较；这是 DFU 传输使用的大小限制，不是整个固件镜像的长度，也不能直接替代 USB 端点的最大包长。

## 185.4\_源码跟踪与使用边界

译注依据保存的[旧版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_dfu.h)、[新版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_dfu.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_dfu.c)及[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/dfu/usb_dfu.c)，摘要见[来源记录](../SOURCES.md)。仓库内[旧版头文件](../../../include/zephyr/usb/class/usb_dfu.h)、[新版头文件](../../../include/zephyr/usb/class/usbd_dfu.h)、[新版实现](../../../subsys/usb/device_next/class/usbd_dfu.c)与[旧版实现](../../../subsys/usb/device/class/dfu/usb_dfu.c)用于相对路径跟踪，版本可能与官网不同。

本批未构建固件、执行镜像下载、擦写 Flash 或验证重启后的镜像。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P184_DFU公共常量与状态码.md) · [返回大纲](大纲.md) · [下一章](P186_DFU公共头文件源码.md)
