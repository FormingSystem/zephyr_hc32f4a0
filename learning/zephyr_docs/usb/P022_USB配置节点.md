---
id: learning.zephyr-docs.usb.api-22
title: USB配置节点
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__config__node.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_USB配置节点

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__config__node.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 22.1\_阅读说明与来源

译注：本页是[USB设备核心API](P015_USB设备核心API.md)的数据结构参考，说明描述符、配置、上下文与类实例的成员。字段声明和原注释按官方页面保留；内部类型或回调约定的补充明确标为源码译注。

[本册大纲](大纲.md)提供本组第18至28章的全部字段参考。

设备配置节点（Configuration Node）。

```c
#include <zephyr/usb/usbd.h>
```

设备配置节点（Configuration Node）。

配置节点用于管理设备配置，至少需要一个配置。节点没有索引，而是使用描述符的 `bConfigurationValue` 标识配置。

## 22.2\_数据成员（Data Fields）

<a id="r_a003a8d9132b319f54583263c4da1e060"></a>

```c
sys_snode_t node
```

单向链表（slist）节点结构。

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](P022_USB配置节点.md#a003a8d9132b319f54583263c4da1e060)。

<a id="r_a55081d79ab3e6b41a091b3f65d7d2d87"></a>

```c
void * desc
```

指向配置描述符的指针。

相关声明：[desc](P022_USB配置节点.md#a55081d79ab3e6b41a091b3f65d7d2d87)。

<a id="r_a19203885a9698861f849bd0fd57cb37f"></a>

```c
struct usbd_desc_node * str_desc_nd
```

指向字符串描述符节点的可选指针。

相关声明：[usbd_desc_node](P021_USB描述符节点.md)、[str_desc_nd](P022_USB配置节点.md#a19203885a9698861f849bd0fd57cb37f)。

<a id="r_a00493162af2344d3d39f834b4834ef78"></a>

```c
sys_slist_t class_list
```

已注册类（功能）的列表。

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[class_list](P022_USB配置节点.md#a00493162af2344d3d39f834b4834ef78)。

## 22.3\_详细说明（Detailed Documentation）

<a id="a00493162af2344d3d39f834b4834ef78"></a>

### `class_list`

```c
sys_slist_t usbd_config_node::class_list
```

已注册类（功能）的列表。

<a id="a55081d79ab3e6b41a091b3f65d7d2d87"></a>

### `desc`

```c
void* usbd_config_node::desc
```

指向配置描述符的指针。

> 译注（源码核对）：原型使用 void * 保存配置描述符地址。节点的配置身份来自该描述符中的 bConfigurationValue，不能把它当作从零开始的数组下标；配置字符串节点 str_desc_nd 则是可选的。

<a id="a003a8d9132b319f54583263c4da1e060"></a>

### `node`

```c
sys_snode_t usbd_config_node::node
```

单向链表（slist）节点结构。

<a id="a19203885a9698861f849bd0fd57cb37f"></a>

### `str_desc_nd`

```c
struct usbd_desc_node* usbd_config_node::str_desc_nd
```

指向字符串描述符节点的可选指针。

## 22.4\_相关源码与使用边界

本页结构定义来自 `zephyr/usb/usbd.h`；本仓库的[对应头文件](../../../include/zephyr/usb/usbd.h)、[类回调包装接口](../../../subsys/usb/device_next/usbd_class_api.h)、[第9章控制请求处理](../../../subsys/usb/device_next/usbd_ch9.c)及[初始化实现](../../../subsys/usb/device_next/usbd_init.c)可用于源码跟踪，版本可能与官网 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[回调接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class_api.h)、[控制请求实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)、[描述符管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_desc.c)和[初始化实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_init.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P021_USB描述符节点.md) · [返回大纲](大纲.md) · [下一章](P023_USB第9章运行时数据.md)
