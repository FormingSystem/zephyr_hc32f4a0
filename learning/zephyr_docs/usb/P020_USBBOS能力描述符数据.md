---
id: learning.zephyr-docs.usb.api-20
title: USBBOS能力描述符数据
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__bos__desc__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_USBBOS能力描述符数据

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__bos__desc__data.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 20.1\_阅读说明与来源

译注：本页是[USB设备核心API](P015_USB设备核心API.md)的数据结构参考，说明描述符、配置、上下文与类实例的成员。字段声明和原注释按官方页面保留；内部类型或回调约定的补充明确标为源码译注。

[本册大纲](大纲.md)提供本组第18至28章的全部字段参考。

USBD 二进制设备对象存储（Binary Device Object Store，BOS）的设备能力描述符数据。

```c
#include <zephyr/usb/usbd.h>
```

USBD 二进制设备对象存储（Binary Device Object Store，BOS）的设备能力描述符数据。

## 20.2\_数据成员（Data Fields）

<a id="r_a084578c905400488e5ce73c71f8aaf00"></a>

```c
enum usbd_bos_desc_utype utype: 8
```

描述符用途类型，不是 `bDescriptorType`。

相关声明：[utype](P020_USBBOS能力描述符数据.md#a084578c905400488e5ce73c71f8aaf00)。

```c
union {
```



<a id="r_a456ab66b0c6ec5e8445369e4cd0176e7"></a>

```c
struct usbd_vreq_node *const vreq_nd
```



相关声明：[usbd_vreq_node](P019_USB厂商请求节点.md)、[vreq_nd](P020_USBBOS能力描述符数据.md#a2d8570c88670c4fbf2d79bb989da01d9)。

<a id="r_aca0dd8a22589e6594e88f79c61570c2e"></a>

```c
};
```



## 20.3\_详细说明（Detailed Documentation）

<a id="aca0dd8a22589e6594e88f79c61570c2e"></a>

### `[union]`

```c
union { ... } usbd_bos_desc_data
```

<a id="a084578c905400488e5ce73c71f8aaf00"></a>

### `utype`

```c
enum usbd_bos_desc_utype usbd_bos_desc_data::utype
```

描述符用途类型，不是 `bDescriptorType`。

> 译注（源码核对）：当前头文件将该用途类型定义为 8 位位域；vreq_nd 位于匿名联合体中，用于带厂商请求的 BOS 节点。应按节点用途解释它，而不是将用途枚举当作 USB 描述符类型。

<a id="a2d8570c88670c4fbf2d79bb989da01d9"></a>

### `vreq_nd`

```c
struct usbd_vreq_node* const usbd_bos_desc_data::vreq_nd
```

## 20.4\_相关源码与使用边界

本页结构定义来自 `zephyr/usb/usbd.h`；本仓库的[对应头文件](../../../include/zephyr/usb/usbd.h)、[类回调包装接口](../../../subsys/usb/device_next/usbd_class_api.h)、[第9章控制请求处理](../../../subsys/usb/device_next/usbd_ch9.c)及[初始化实现](../../../subsys/usb/device_next/usbd_init.c)可用于源码跟踪，版本可能与官网 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[回调接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class_api.h)、[控制请求实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)、[描述符管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_desc.c)和[初始化实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_init.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P019_USB厂商请求节点.md) · [返回大纲](大纲.md) · [下一章](P021_USB描述符节点.md)
