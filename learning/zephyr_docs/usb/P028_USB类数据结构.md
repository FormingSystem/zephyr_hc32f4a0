---
id: learning.zephyr-docs.usb.api-28
title: USB类数据结构
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__class__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_USB类数据结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__class__data.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 28.1\_阅读说明与来源

译注：本页是[USB设备核心API](P015_USB设备核心API.md)的数据结构参考，说明描述符、配置、上下文与类实例的成员。字段声明和原注释按官方页面保留；内部类型或回调约定的补充明确标为源码译注。

[本册大纲](大纲.md)提供本组第18至28章的全部字段参考。

USB 设备支持的类数据。

```c
#include <zephyr/usb/usbd.h>
```

USB 设备支持的类数据。

## 28.2\_数据成员（Data Fields）

<a id="r_ad251371b0e401fb2bffd6aaa1ff49063"></a>

```c
const char * name
```

USB 设备类实例名称。

相关声明：[name](P028_USB类数据结构.md#ad251371b0e401fb2bffd6aaa1ff49063)。

<a id="r_a111a803092fd389a500fb99bfc71b29a"></a>

```c
struct usbd_context * uds_ctx
```

指向 USB 设备栈上下文结构的指针。

相关声明：[usbd_context](P025_USB设备上下文结构.md)、[uds_ctx](P028_USB类数据结构.md#a111a803092fd389a500fb99bfc71b29a)。

<a id="r_a9109af3e25c499d4ef1f0746bf6a20cc"></a>

```c
const struct usbd_class_api * api
```

指向设备支持类 API 的指针。

相关声明：[usbd_class_api](P027_USB类回调接口.md)、[api](P028_USB类数据结构.md#a9109af3e25c499d4ef1f0746bf6a20cc)。

<a id="r_a32db83ecf80e1ac9e4d5deda54581deb"></a>

```c
const struct usbd_cctx_vendor_req * v_reqs
```

支持的厂商请求表，可以为 `NULL`。

相关声明：[usbd_cctx_vendor_req](P026_USB类厂商请求表.md)、[v_reqs](P028_USB类数据结构.md#a32db83ecf80e1ac9e4d5deda54581deb)。

<a id="r_a10bb5b9af6098fbbc86fd00ef54e84e1"></a>

```c
void * priv
```

指向私有数据（Private Data）的指针。

相关声明：[priv](P028_USB类数据结构.md#a10bb5b9af6098fbbc86fd00ef54e84e1)。

## 28.3\_详细说明（Detailed Documentation）

<a id="a9109af3e25c499d4ef1f0746bf6a20cc"></a>

### `api`

```c
const struct usbd_class_api* usbd_class_data::api
```

指向设备支持类 API 的指针。

<a id="ad251371b0e401fb2bffd6aaa1ff49063"></a>

### `name`

```c
const char* usbd_class_data::name
```

USB 设备类实例名称。

<a id="a10bb5b9af6098fbbc86fd00ef54e84e1"></a>

### `priv`

```c
void* usbd_class_data::priv
```

指向私有数据（Private Data）的指针。

<a id="a111a803092fd389a500fb99bfc71b29a"></a>

### `uds_ctx`

```c
struct usbd_context* usbd_class_data::uds_ctx
```

指向 USB 设备栈上下文结构的指针。

> 译注（源码核对）：类实现应调用 usbd_class_get_ctx() 获取设备上下文，按核心API约定避免直接访问此成员；私有数据同样可通过 usbd_class_get_private() 获取。

<a id="a32db83ecf80e1ac9e4d5deda54581deb"></a>

### `v_reqs`

```c
const struct usbd_cctx_vendor_req* usbd_class_data::v_reqs
```

支持的厂商请求表，可以为 `NULL`。

## 28.4\_相关源码与使用边界

本页结构定义来自 `zephyr/usb/usbd.h`；本仓库的[对应头文件](../../../include/zephyr/usb/usbd.h)、[类回调包装接口](../../../subsys/usb/device_next/usbd_class_api.h)、[第9章控制请求处理](../../../subsys/usb/device_next/usbd_ch9.c)及[初始化实现](../../../subsys/usb/device_next/usbd_init.c)可用于源码跟踪，版本可能与官网 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[回调接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class_api.h)、[控制请求实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)、[描述符管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_desc.c)和[初始化实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_init.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P027_USB类回调接口.md) · [返回大纲](大纲.md) · [下一章](P029_USB设备控制器API说明.md)
