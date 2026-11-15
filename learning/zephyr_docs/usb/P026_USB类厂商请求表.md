---
id: learning.zephyr-docs.usb.api-26
title: USB类厂商请求表
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__cctx__vendor__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_USB类厂商请求表

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__cctx__vendor__req.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 26.1\_阅读说明与来源

译注：本页是[USB设备核心API](P015_USB设备核心API.md)的数据结构参考，说明描述符、配置、上下文与类实例的成员。字段声明和原注释按官方页面保留；内部类型或回调约定的补充明确标为源码译注。

[本册大纲](大纲.md)提供本组第18至28章的全部字段参考。

厂商请求表（Vendor Requests Table）。

```c
#include <zephyr/usb/usbd.h>
```

厂商请求表（Vendor Requests Table）。

## 26.2\_数据成员（Data Fields）

<a id="r_a2ddf3ce0c1c0a6d788b7ef30cf8d67ea"></a>

```c
const uint8_t * reqs
```

类所支持的厂商请求数组。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reqs](P026_USB类厂商请求表.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea)。

<a id="r_a3b5e99bff9dbfa023a4e6a5b4a69abd0"></a>

```c
uint8_t len
```

数组长度。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](P026_USB类厂商请求表.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0)。

## 26.3\_详细说明（Detailed Documentation）

<a id="a3b5e99bff9dbfa023a4e6a5b4a69abd0"></a>

### `len`

```c
uint8_t usbd_cctx_vendor_req::len
```

数组长度。

<a id="a2ddf3ce0c1c0a6d788b7ef30cf8d67ea"></a>

### `reqs`

```c
const uint8_t* usbd_cctx_vendor_req::reqs
```

类所支持的厂商请求数组。

> 译注（源码核对）：这里保存类支持的请求代码数组，len 是数组元素数量；它不是以 NULL 结尾的字符串列表。类厂商请求表与接收方为 Device 的 usbd_vreq_node 属于不同分派路径。

## 26.4\_相关源码与使用边界

本页结构定义来自 `zephyr/usb/usbd.h`；本仓库的[对应头文件](../../../include/zephyr/usb/usbd.h)、[类回调包装接口](../../../subsys/usb/device_next/usbd_class_api.h)、[第9章控制请求处理](../../../subsys/usb/device_next/usbd_ch9.c)及[初始化实现](../../../subsys/usb/device_next/usbd_init.c)可用于源码跟踪，版本可能与官网 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[回调接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class_api.h)、[控制请求实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)、[描述符管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_desc.c)和[初始化实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_init.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P025_USB设备上下文结构.md) · [返回大纲](大纲.md) · [下一章](P027_USB类回调接口.md)
