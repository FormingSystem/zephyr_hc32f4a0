---
id: learning.zephyr-docs.usb.api-171
title: USB端点属性位域
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__ep__desc__bmattr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2020 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第171章\_USB端点属性位域

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__ep__desc__bmattr.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 171.1\_阅读说明与来源

译注：本页属于 USB 第 9 章（Chapter 9）控制请求与描述符参考。这些结构把设备、配置、接口和端点的协议字段表示为 C 声明，便于对照枚举过程及设备栈实现。原字段说明完整保留，补充的源码解释明确标为译注；[本册大纲](大纲.md)提供相关接口和示例。

端点属性位域（Endpoint Attribute Bit Fields）。

```c
#include <zephyr/usb/usb_ch9.h>
```

端点属性位域（Endpoint Attribute Bit Fields）。

参见规范中的表 9-13。

## 171.2\_数据成员（Data Fields）

<a id="r_aad0fafee643f870dc6b9e04b805be4c1"></a>

```c
uint8_t reserved: 2
```

保留位（Reserved Bits）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved](P171_USB端点属性位域.md#aad0fafee643f870dc6b9e04b805be4c1)。

<a id="r_ace1957268116f35f93fc67e7ed2f827b"></a>

```c
uint8_t usage: 2
```

用途类型（Usage Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usage](P171_USB端点属性位域.md#ace1957268116f35f93fc67e7ed2f827b)。

<a id="r_a20a1a476ad08ab95f6118627abd72375"></a>

```c
uint8_t synch: 2
```

同步类型（Synchronization Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[synch](P171_USB端点属性位域.md#a20a1a476ad08ab95f6118627abd72375)。

<a id="r_a00c87e3fc2a32a759f7627c363f533a8"></a>

```c
uint8_t transfer: 2
```

传输类型（Transfer Type）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transfer](P171_USB端点属性位域.md#a00c87e3fc2a32a759f7627c363f533a8)。

## 171.3\_详细说明（Detailed Documentation）

<a id="aad0fafee643f870dc6b9e04b805be4c1"></a>

### 171.3.1\_`reserved`

```c
uint8_t usb_ep_desc_bmattr::reserved
```

保留位（Reserved Bits）。

<a id="a20a1a476ad08ab95f6118627abd72375"></a>

### 171.3.2\_`synch`

```c
uint8_t usb_ep_desc_bmattr::synch
```

同步类型（Synchronization Type）。

<a id="a00c87e3fc2a32a759f7627c363f533a8"></a>

### 171.3.3\_`transfer`

```c
uint8_t usb_ep_desc_bmattr::transfer
```

传输类型（Transfer Type）。

> 译注（源码核对）：源码将 `transfer`、`synch`、`usage`、`reserved` 各定义为 2 位。`CONFIG_LITTLE_ENDIAN` 分支调整字段声明顺序；这些是同一个端点属性字节的位域，不能当成四个独立字节。

<a id="ace1957268116f35f93fc67e7ed2f827b"></a>

### 171.3.4\_`usage`

```c
uint8_t usb_ep_desc_bmattr::usage
```

用途类型（Usage Type）。

## 171.4\_源码跟踪与使用边界

译注依据保存的[官方 USB 第 9 章头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_ch9.h)与[新版设备栈标准请求处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)，原始头文件署名为 Copyright (c) 2020 PHYTEC Messtechnik GmbH，许可证为 `Apache-2.0`。文件摘要见[来源记录](../SOURCES.md)。本仓库的[同名头文件](../../../include/zephyr/usb/usb_ch9.h)和[请求处理源码](../../../subsys/usb/device_next/usbd_ch9.c)供相对路径跟踪，版本可能与官网不同。轮询间隔换算还核对保存的[官方整数 log2 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/math/ilog2.h)。标准字段的具体编码仍应结合原页所引用的规范及目标速率理解；本页不以字段名称替代协议约束。本批未构建固件或连接设备进行枚举测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P170_USB请求类型位域.md) · [返回大纲](大纲.md) · [下一章](P172_USB标准请求与描述符常量.md)
