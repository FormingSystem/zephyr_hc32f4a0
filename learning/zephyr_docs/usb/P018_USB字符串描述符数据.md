---
id: learning.zephyr-docs.usb.api-18
title: USB字符串描述符数据
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__str__desc__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_USB字符串描述符数据

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__str__desc__data.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 18.1\_阅读说明与来源

译注：本页是[USB设备核心API](P015_USB设备核心API.md)的数据结构参考，说明描述符、配置、上下文与类实例的成员。字段声明和原注释按官方页面保留；内部类型或回调约定的补充明确标为源码译注。

[本册大纲](大纲.md)提供本组第18至28章的全部字段参考。

内部使用，用于保持描述符（Descriptor）的顺序。

```c
#include <zephyr/usb/usbd.h>
```

内部使用，用于保持描述符（Descriptor）的顺序。

USBD 字符串描述符数据。

## 18.2\_数据成员（Data Fields）

<a id="r_a0654953d15160cc19cad86a407f655cb"></a>

```c
uint8_t idx
```

描述符索引，字符串描述符需要此字段。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[idx](P018_USB字符串描述符数据.md#a0654953d15160cc19cad86a407f655cb)。

<a id="r_a2e6dfc9cbbd44457113899db988a84ca"></a>

```c
enum usbd_str_desc_utype utype: 8
```

描述符用途类型，不是 `bDescriptorType`。

相关声明：[utype](P018_USB字符串描述符数据.md#a2e6dfc9cbbd44457113899db988a84ca)。

<a id="r_ad4d7c291f95973d20ff522b8a5ef65a0"></a>

```c
unsigned int ascii7: 1
```

字符串描述符采用 ASCII7 格式。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[ascii7](P018_USB字符串描述符数据.md#ad4d7c291f95973d20ff522b8a5ef65a0)。

<a id="r_a40459d114a339841e1f9c14b0d036fe8"></a>

```c
unsigned int use_hwinfo: 1
```

设备栈通过硬件信息（Hardware Info，HWINFO）API 取得序列号（SerialNumber）。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[use_hwinfo](P018_USB字符串描述符数据.md#a40459d114a339841e1f9c14b0d036fe8)。

## 18.3\_详细说明（Detailed Documentation）

<a id="ad4d7c291f95973d20ff522b8a5ef65a0"></a>

### `ascii7`

```c
unsigned int usbd_str_desc_data::ascii7
```

字符串描述符采用 ASCII7 格式。

<a id="a0654953d15160cc19cad86a407f655cb"></a>

### `idx`

```c
uint8_t usbd_str_desc_data::idx
```

描述符索引，字符串描述符需要此字段。

<a id="a40459d114a339841e1f9c14b0d036fe8"></a>

### `use_hwinfo`

```c
unsigned int usbd_str_desc_data::use_hwinfo
```

设备栈通过硬件信息（Hardware Info，HWINFO）API 取得序列号（SerialNumber）。

<a id="a2e6dfc9cbbd44457113899db988a84ca"></a>

### `utype`

```c
enum usbd_str_desc_utype usbd_str_desc_data::utype
```

描述符用途类型，不是 `bDescriptorType`。

> 译注（源码核对）：当前头文件把 utype 定义为 8 位位域（Bit-field），ascii7 与 use_hwinfo 各占 1 位；网页成员声明未展示位域宽度。本结构的用途类型供栈内部区分字符串用途，与 USB 协议的 bDescriptorType 字段不同。

## 18.4\_相关源码与使用边界

本页结构定义来自 `zephyr/usb/usbd.h`；本仓库的[对应头文件](../../../include/zephyr/usb/usbd.h)、[类回调包装接口](../../../subsys/usb/device_next/usbd_class_api.h)、[第9章控制请求处理](../../../subsys/usb/device_next/usbd_ch9.c)及[初始化实现](../../../subsys/usb/device_next/usbd_init.c)可用于源码跟踪，版本可能与官网 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[回调接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class_api.h)、[控制请求实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)、[描述符管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_desc.c)和[初始化实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_init.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P017_USB设备消息结构.md) · [返回大纲](大纲.md) · [下一章](P019_USB厂商请求节点.md)
