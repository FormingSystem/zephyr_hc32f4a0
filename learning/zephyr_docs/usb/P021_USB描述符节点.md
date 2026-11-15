---
id: learning.zephyr-docs.usb.api-21
title: USB描述符节点
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__desc__node.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_USB描述符节点

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__desc__node.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 21.1\_阅读说明与来源

译注：本页是[USB设备核心API](P015_USB设备核心API.md)的数据结构参考，说明描述符、配置、上下文与类实例的成员。字段声明和原注释按官方页面保留；内部类型或回调约定的补充明确标为源码译注。

[本册大纲](大纲.md)提供本组第18至28章的全部字段参考。

描述符节点。

```c
#include <zephyr/usb/usbd.h>
```

描述符节点。

描述符节点管理没有直接包含在某个结构中的描述符，例如字符串描述符或 BOS 能力描述符。

## 21.2\_数据成员（Data Fields）

<a id="r_a9f1941cd036c01387d8ad9a4aceb595a"></a>

```c
sys_dnode_t node
```

单向链表（slist）节点结构。

相关声明：[sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)、[node](P021_USB描述符节点.md#a9f1941cd036c01387d8ad9a4aceb595a)。

```c
union {
```



<a id="r_a031443b862144b5c8213dbac7f821e57"></a>

```c
struct usbd_str_desc_data str
```



相关声明：[usbd_str_desc_data](P018_USB字符串描述符数据.md)、[str](P021_USB描述符节点.md#ae34fee200f7fd78355addafe79789cb4)。

<a id="r_aaf57c3ce0c033d15a4ac7d2ca3f8eb08"></a>

```c
struct usbd_bos_desc_data bos
```



相关声明：[usbd_bos_desc_data](P020_USBBOS能力描述符数据.md)、[bos](P021_USB描述符节点.md#afd65079b8b969fa4101a3f9f662c7b6b)。

<a id="r_a080f8481b8a0b5278e132b85667686de"></a>

```c
};
```



<a id="r_ac437b472e012e8fdec049f28e9f88944"></a>

```c
const void *const ptr
```

指向描述符载荷（Payload）的不透明指针（Opaque Pointer）。

相关声明：[ptr](P021_USB描述符节点.md#ac437b472e012e8fdec049f28e9f88944)。

<a id="r_ad71ef74fd7fe43a8117704553a3be01c"></a>

```c
uint8_t bLength
```

描述符大小，单位为字节。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bLength](P021_USB描述符节点.md#ad71ef74fd7fe43a8117704553a3be01c)。

<a id="r_a786e2911b5ec7d6c908c148be4d27f5f"></a>

```c
uint8_t bDescriptorType
```

描述符类型。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](P021_USB描述符节点.md#a786e2911b5ec7d6c908c148be4d27f5f)。

## 21.3\_详细说明（Detailed Documentation）

<a id="a080f8481b8a0b5278e132b85667686de"></a>

### `[union]`

```c
union { ... } usbd_desc_node
```

> 译注（源码核对）：str 与 bos 是同一匿名联合体的两个成员，共用存储空间，不能同时作为两份独立的有效数据使用。根据节点实际描述符类型和用途读取相应成员。

<a id="a786e2911b5ec7d6c908c148be4d27f5f"></a>

### `bDescriptorType`

```c
uint8_t usbd_desc_node::bDescriptorType
```

描述符类型。

<a id="ad71ef74fd7fe43a8117704553a3be01c"></a>

### `bLength`

```c
uint8_t usbd_desc_node::bLength
```

描述符大小，单位为字节。

<a id="afd65079b8b969fa4101a3f9f662c7b6b"></a>

### `bos`

```c
struct usbd_bos_desc_data usbd_desc_node::bos
```

<a id="a9f1941cd036c01387d8ad9a4aceb595a"></a>

### `node`

```c
sys_dnode_t usbd_desc_node::node
```

单向链表（slist）节点结构。

> 译注（源码核对）：原文写 slist，但当前声明为 sys_dnode_t，是双向链表节点。与之配套的 usbd_context.descriptors 也声明为 sys_dlist_t；这里保留原注释并指出类型差异，不据旧文字改用单向链表操作。

<a id="ac437b472e012e8fdec049f28e9f88944"></a>

### `ptr`

```c
const void* const usbd_desc_node::ptr
```

指向描述符载荷（Payload）的不透明指针（Opaque Pointer）。

<a id="ae34fee200f7fd78355addafe79789cb4"></a>

### `str`

```c
struct usbd_str_desc_data usbd_desc_node::str
```

## 21.4\_相关源码与使用边界

本页结构定义来自 `zephyr/usb/usbd.h`；本仓库的[对应头文件](../../../include/zephyr/usb/usbd.h)、[类回调包装接口](../../../subsys/usb/device_next/usbd_class_api.h)、[第9章控制请求处理](../../../subsys/usb/device_next/usbd_ch9.c)及[初始化实现](../../../subsys/usb/device_next/usbd_init.c)可用于源码跟踪，版本可能与官网 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[回调接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class_api.h)、[控制请求实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)、[描述符管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_desc.c)和[初始化实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_init.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P020_USBBOS能力描述符数据.md) · [返回大纲](大纲.md) · [下一章](P022_USB配置节点.md)
