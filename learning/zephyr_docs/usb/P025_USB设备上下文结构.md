---
id: learning.zephyr-docs.usb.api-25
title: USB设备上下文结构
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_USB设备上下文结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__context.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 25.1\_阅读说明与来源

译注：本页是[USB设备核心API](P015_USB设备核心API.md)的数据结构参考，说明描述符、配置、上下文与类实例的成员。字段声明和原注释按官方页面保留；内部类型或回调约定的补充明确标为源码译注。

[本册大纲](大纲.md)提供本组第18至28章的全部字段参考。

USB 设备支持的运行时上下文（Runtime Context）。

```c
#include <zephyr/usb/usbd.h>
```

USB 设备支持的运行时上下文（Runtime Context）。

组织全部描述符、配置和接口的主要结构。必须为它指定一个 USB 设备控制器（USB Device Controller，UDC）设备。

## 25.2\_数据成员（Data Fields）

<a id="r_ade73c224b256007bf2d68bd1205ceb6e"></a>

```c
const char * name
```

USB 设备名称。

相关声明：[name](P025_USB设备上下文结构.md#ade73c224b256007bf2d68bd1205ceb6e)。

<a id="r_a8ff2a4303b73db67eeabdd999736b3a6"></a>

```c
struct k_mutex mutex
```

访问互斥量（Mutex）。

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[mutex](P025_USB设备上下文结构.md#a8ff2a4303b73db67eeabdd999736b3a6)。

<a id="r_a52c2cc6118b46fbcbc7a495df61f6b6c"></a>

```c
const struct device * dev
```

指向 UDC 设备的指针。

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](P025_USB设备上下文结构.md#a52c2cc6118b46fbcbc7a495df61f6b6c)。

<a id="r_a300ab0384b3d4e7f3d7d188a27a78be3"></a>

```c
usbd_msg_cb_t msg_cb
```

接收通知消息的回调。

相关声明：[usbd_msg_cb_t](P015_USB设备核心API.md#ga2cd074cefff922b0816de37935d9646e)、[msg_cb](P025_USB设备上下文结构.md#a300ab0384b3d4e7f3d7d188a27a78be3)。

<a id="r_a7a884c982011034fd02a41d7cb450509"></a>

```c
sys_slist_t ep_events
```

保存端点事件的单向链表（slist）。

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[ep_events](P025_USB设备上下文结构.md#a7a884c982011034fd02a41d7cb450509)。

<a id="r_ae65f5ae6e67b1e9e302a1d45d59751c3"></a>

```c
struct k_spinlock ep_event_lock
```

端点事件列表的自旋锁（Spinlock）。

相关声明：[k_spinlock](../kernel/P066_自旋锁结构参考.md)、[ep_event_lock](P025_USB设备上下文结构.md#ae65f5ae6e67b1e9e302a1d45d59751c3)。

<a id="r_a4fb1545ec02e7d38766cee9940edc1eb"></a>

```c
struct usbd_ch9_data ch9_data
```

中间层运行时数据。

相关声明：[usbd_ch9_data](P023_USB第9章运行时数据.md)、[ch9_data](P025_USB设备上下文结构.md#a4fb1545ec02e7d38766cee9940edc1eb)。

<a id="r_adf8dd86f2784cc69ce6da314adc00b72"></a>

```c
sys_dlist_t descriptors
```

管理字符串、BOS 等描述符的单向链表（slist）。

相关声明：[sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)、[descriptors](P025_USB设备上下文结构.md#adf8dd86f2784cc69ce6da314adc00b72)。

<a id="r_a8c7d153a73859dd8ba25265f059f7495"></a>

```c
sys_slist_t fs_configs
```

管理全速（Full-Speed）设备配置的单向链表（slist）。

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[fs_configs](P025_USB设备上下文结构.md#a8c7d153a73859dd8ba25265f059f7495)。

<a id="r_a4a6bd413d06328ffa5db089e35157376"></a>

```c
sys_slist_t hs_configs
```

管理高速（High-Speed）设备配置的单向链表（slist）。

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[hs_configs](P025_USB设备上下文结构.md#a4a6bd413d06328ffa5db089e35157376)。

<a id="r_a6b463c6c01230bc68c50ba5bb5550e99"></a>

```c
sys_dlist_t vreqs
```

管理接收方为设备的厂商请求的双向链表（dlist）。

相关声明：[sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)、[vreqs](P025_USB设备上下文结构.md#a6b463c6c01230bc68c50ba5bb5550e99)。

<a id="r_a3acad44126b6c3d56823ef7408332087"></a>

```c
struct usbd_status status
```

USB 设备支持的状态。

相关声明：[usbd_status](P024_USB设备状态结构.md)、[status](P025_USB设备上下文结构.md#a3acad44126b6c3d56823ef7408332087)。

<a id="r_a193420cc196f115cbd6947b10d542ee5"></a>

```c
void * fs_desc
```

指向全速设备描述符的指针。

相关声明：[fs_desc](P025_USB设备上下文结构.md#a193420cc196f115cbd6947b10d542ee5)。

<a id="r_a250e2f82c7239ce81b104b6ef3c16857"></a>

```c
void * hs_desc
```

指向高速设备描述符的指针。

相关声明：[hs_desc](P025_USB设备上下文结构.md#a250e2f82c7239ce81b104b6ef3c16857)。

<a id="r_aec2fa8e53ddaa2e282e381218171d7bd"></a>

```c
struct net_buf * setup_buf
```

为控制传输 SETUP 阶段预分配的缓冲区。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[setup_buf](P025_USB设备上下文结构.md#aec2fa8e53ddaa2e282e381218171d7bd)。

## 25.3\_详细说明（Detailed Documentation）

<a id="a4fb1545ec02e7d38766cee9940edc1eb"></a>

### `ch9_data`

```c
struct usbd_ch9_data usbd_context::ch9_data
```

中间层运行时数据。

<a id="adf8dd86f2784cc69ce6da314adc00b72"></a>

### `descriptors`

```c
sys_dlist_t usbd_context::descriptors
```

管理字符串、BOS 等描述符的单向链表（slist）。

> 译注（源码核对）：原注释仍写 slist，实际类型为 sys_dlist_t，属于双向链表。源码初始化和描述符管理也按双向链表处理，不能只按原注释选择操作接口。

<a id="a52c2cc6118b46fbcbc7a495df61f6b6c"></a>

### `dev`

```c
const struct device* usbd_context::dev
```

指向 UDC 设备的指针。

<a id="ae65f5ae6e67b1e9e302a1d45d59751c3"></a>

### `ep_event_lock`

```c
struct k_spinlock usbd_context::ep_event_lock
```

端点事件列表的自旋锁（Spinlock）。

<a id="a7a884c982011034fd02a41d7cb450509"></a>

### `ep_events`

```c
sys_slist_t usbd_context::ep_events
```

保存端点事件的单向链表（slist）。

<a id="a8c7d153a73859dd8ba25265f059f7495"></a>

### `fs_configs`

```c
sys_slist_t usbd_context::fs_configs
```

管理全速（Full-Speed）设备配置的单向链表（slist）。

<a id="a193420cc196f115cbd6947b10d542ee5"></a>

### `fs_desc`

```c
void* usbd_context::fs_desc
```

指向全速设备描述符的指针。

<a id="a4a6bd413d06328ffa5db089e35157376"></a>

### `hs_configs`

```c
sys_slist_t usbd_context::hs_configs
```

管理高速（High-Speed）设备配置的单向链表（slist）。

<a id="a250e2f82c7239ce81b104b6ef3c16857"></a>

### `hs_desc`

```c
void* usbd_context::hs_desc
```

指向高速设备描述符的指针。

<a id="a300ab0384b3d4e7f3d7d188a27a78be3"></a>

### `msg_cb`

```c
usbd_msg_cb_t usbd_context::msg_cb
```

接收通知消息的回调。

> 译注（源码核对）：通过 usbd_msg_register_cb() 注册接收函数；执行上下文、消息载荷与生命周期见[USB设备消息API](P016_USB设备消息API.md)和[消息结构](P017_USB设备消息结构.md)，不要自行改写运行中上下文的回调指针。

<a id="a8ff2a4303b73db67eeabdd999736b3a6"></a>

### `mutex`

```c
struct k_mutex usbd_context::mutex
```

访问互斥量（Mutex）。

<a id="ade73c224b256007bf2d68bd1205ceb6e"></a>

### `name`

```c
const char* usbd_context::name
```

USB 设备名称。

<a id="aec2fa8e53ddaa2e282e381218171d7bd"></a>

### `setup_buf`

```c
struct net_buf* usbd_context::setup_buf
```

为控制传输 SETUP 阶段预分配的缓冲区。

<a id="a3acad44126b6c3d56823ef7408332087"></a>

### `status`

```c
struct usbd_status usbd_context::status
```

USB 设备支持的状态。

<a id="a6b463c6c01230bc68c50ba5bb5550e99"></a>

### `vreqs`

```c
sys_dlist_t usbd_context::vreqs
```

管理接收方为设备的厂商请求的双向链表（dlist）。

## 25.4\_相关源码与使用边界

本页结构定义来自 `zephyr/usb/usbd.h`；本仓库的[对应头文件](../../../include/zephyr/usb/usbd.h)、[类回调包装接口](../../../subsys/usb/device_next/usbd_class_api.h)、[第9章控制请求处理](../../../subsys/usb/device_next/usbd_ch9.c)及[初始化实现](../../../subsys/usb/device_next/usbd_init.c)可用于源码跟踪，版本可能与官网 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[回调接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class_api.h)、[控制请求实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)、[描述符管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_desc.c)和[初始化实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_init.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P024_USB设备状态结构.md) · [返回大纲](大纲.md) · [下一章](P026_USB类厂商请求表.md)
