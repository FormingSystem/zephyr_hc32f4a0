---
id: learning.zephyr-docs.usb.api-153
title: 旧版USB端点配置结构
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__dc__ep__cfg__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第153章\_旧版USB端点配置结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__dc__ep__cfg__data.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 153.1\_阅读说明与来源

译注：本页说明旧版USB设备控制器驱动API（usb_dc）。它与新版USB设备控制器（USB Device Controller，UDC）API不同；原文的弃用标记与完整接口声明均保留。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 端点配置（Endpoint Configuration）。

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

USB 端点配置（Endpoint Configuration）。

包含 USB 端点配置的结构。

## 153.2\_数据成员（Data Fields）

<a id="r_aba57a59450c93db5935e2ca08c94aa8b"></a>

```c
uint8_t ep_addr
```

设备配置结构中与端点关联的编号：IN EP = 0x80 | <endpoint number>，OUT EP = 0x00 | <endpoint number>。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ep_addr](P153_旧版USB端点配置结构.md#aba57a59450c93db5935e2ca08c94aa8b)。

<a id="r_a497bc16439e98415f383a680a0c4d008"></a>

```c
uint16_t ep_mps
```

端点最大包大小。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ep_mps](P153_旧版USB端点配置结构.md#a497bc16439e98415f383a680a0c4d008)。

<a id="r_a689682e1df951fd2fd492dda5e03cf08"></a>

```c
enum usb_dc_ep_transfer_type ep_type
```

端点传输类型。

相关声明：[usb_dc_ep_transfer_type](P152_旧版USB控制器驱动API.md#gaca68e4a7c3c0a984d1df23794cfa7d87)、[ep_type](P153_旧版USB端点配置结构.md#a689682e1df951fd2fd492dda5e03cf08)。

## 153.3\_详细说明（Detailed Documentation）

<a id="aba57a59450c93db5935e2ca08c94aa8b"></a>

### 153.3.1\_`ep_addr`

```c
uint8_t usb_dc_ep_cfg_data::ep_addr
```

设备配置结构中与端点关联的编号：IN EP = 0x80 | <endpoint number>，OUT EP = 0x00 | <endpoint number>。

> 译注（源码核对）：端点地址包含方向位。相同端点编号的IN与OUT使用不同地址，不能传入只有编号而缺少方向位的值来表示IN端点。

<a id="a497bc16439e98415f383a680a0c4d008"></a>

### 153.3.2\_`ep_mps`

```c
uint16_t usb_dc_ep_cfg_data::ep_mps
```

端点最大包大小。

> 译注（源码核对）：此值描述单个端点包的容量，不是一次应用缓冲区或整个分段传输的总长度。控制器、传输类型及总线速率共同限制可接受的配置。

<a id="a689682e1df951fd2fd492dda5e03cf08"></a>

### 153.3.3\_`ep_type`

```c
enum usb_dc_ep_transfer_type usb_dc_ep_cfg_data::ep_type
```

端点传输类型。

可以是批量（Bulk）、中断（Interrupt）、控制（Control）或等时（Isochronous）。

## 153.4\_源码跟踪与使用边界

译注依据保存的[官方usb_dc头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/usb_dc.h)、[旧版设备栈核心](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_device.c)及[传输实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_transfer.c)，摘要见[来源记录](../SOURCES.md)。本仓库[控制器头文件](../../../include/zephyr/drivers/usb/usb_dc.h)与[设备栈实现](../../../subsys/usb/device/usb_device.c)可用于相对路径源码跟踪，版本可能与网页不同。新版接口见[UDC说明](P029_USB设备控制器API说明.md)，旧版入口见[usb_dc说明](P128_旧版USB设备控制器API.md)。本批未构建、烧录、执行总线收发或唤醒测试。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P152_旧版USB控制器驱动API.md) · [返回大纲](大纲.md) · [下一章](P154_旧版USB控制器头文件接口.md)
