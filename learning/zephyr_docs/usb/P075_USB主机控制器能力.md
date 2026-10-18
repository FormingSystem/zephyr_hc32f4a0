---
id: learning.zephyr-docs.usb.api-75
title: USB主机控制器能力
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuhc__device__caps.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_USB主机控制器能力

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structuhc__device__caps.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 75.1\_阅读说明与来源

译注：本页说明USB主机控制器（USB Host Controller，UHC）的公开声明。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB主机控制器能力。

```c
#include <zephyr/drivers/usb/uhc.h>
```

USB主机控制器能力。

此结构主要供USB主机栈使用。

## 75.2\_数据成员（Data Fields）

<a id="r_ab526337af28d25728780cb48dc43e722"></a>

```c
uint32_t hs: 1
```

支持USB高速的控制器。

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[hs](P075_USB主机控制器能力.md#ab526337af28d25728780cb48dc43e722)。

## 75.3\_详细说明（Detailed Documentation）

<a id="ab526337af28d25728780cb48dc43e722"></a>

### 75.3.1\_`hs`

```c
uint32_t uhc_device_caps::hs
```

支持USB高速的控制器。

> 译注（源码核对）：此位描述控制器的高速能力，不是当前连接设备的协商速率。设备实际速率见usb_device_speed；枚举中存在SuperSpeed值也不证明某个控制器支持它。

## 75.4\_源码跟踪与使用边界

译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/uhc/uhc_common.c)、[虚拟控制器](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/uhc/uhc_virtual.c)和[主机栈事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../include/zephyr/drivers/usb/uhc.h)、[公共实现](../../../drivers/usb/uhc/uhc_common.c)与[主机栈](../../../subsys/usb/host/usbh_core.c)可用于跟踪，版本可能与网页不同。此API仍为实验性接口，本批未编译或运行USB主机固件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P074_USB主机控制器数据.md) · [返回大纲](大纲.md) · [下一章](P076_USB主机控制器事件.md)
