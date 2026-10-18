---
id: learning.zephyr-docs.usb.api-77
title: USB主机传输结构
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuhc__transfer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_USB主机传输结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structuhc__transfer.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 77.1\_阅读说明与来源

译注：本页说明USB主机控制器（USB Host Controller，UHC）的公开声明。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

UHC端点缓冲区信息。

```c
#include <zephyr/drivers/usb/uhc.h>
```

UHC端点缓冲区信息。

所有UHC请求都必须使用此结构，其中包含请求元数据（Metadata），以及为每个请求存储net_buf结构的先进先出队列（First-In, First-Out，FIFO）。

上层（主机栈）不应直接使用此结构的成员。

## 77.2\_数据成员（Data Fields）

<a id="r_ae1fcb0b866e3d7c5b5ea9dff6221f37d"></a>

```c
sys_dnode_t node
```

双向链表节点

相关声明：[sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)、[node](P077_USB主机传输结构.md#ae1fcb0b866e3d7c5b5ea9dff6221f37d)。

<a id="r_a105b30625208c612b4abe857e208a7f1"></a>

```c
struct sys_ref ref
```

引用计数（Reference Count）。

相关声明：[sys_ref](../sysref_reference/P002_引用计数对象.md)、[ref](P077_USB主机传输结构.md#a105b30625208c612b4abe857e208a7f1)。

<a id="r_ae681c0078b8afedd3b6fba165861e114"></a>

```c
uint8_t setup_pkt [ROUND_UP(8, USB_PRIV_BUFGRANULARITY)]
```

控制传输的建立包（Setup Packet）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[setup_pkt](P077_USB主机传输结构.md#ae681c0078b8afedd3b6fba165861e114)、[ROUND_UP](../util_reference/P001_通用工具公共接口.md#gaada5610108b15d85c65d863b0c646ef3)。

<a id="r_a170385b08171659f05ac7112faf8e587"></a>

```c
struct net_buf * buf
```

传输数据缓冲区。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[buf](P077_USB主机传输结构.md#a170385b08171659f05ac7112faf8e587)。

<a id="r_aaf664844dc9f1871cce3d38516c042ef"></a>

```c
uint8_t ep
```

请求关联的端点。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ep](P077_USB主机传输结构.md#aaf664844dc9f1871cce3d38516c042ef)。

<a id="r_ad4dbc766c6ded0ebfab7e36b19643b15"></a>

```c
uint8_t type
```

端点类型。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](P077_USB主机传输结构.md#ad4dbc766c6ded0ebfab7e36b19643b15)。

<a id="r_a61a6c74cc7c026404ccf42d1164765b8"></a>

```c
uint16_t mps
```

最大包长（Maximum Packet Size，MPS）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mps](P077_USB主机传输结构.md#a61a6c74cc7c026404ccf42d1164765b8)。

<a id="r_af6d6de482f092e4f85679722ad609cbf"></a>

```c
uint16_t interval
```

间隔，仅用于周期性传输（Periodic Transfer）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](P077_USB主机传输结构.md#af6d6de482f092e4f85679722ad609cbf)。

<a id="r_a23e4115c774134ccd143189b0f4f2460"></a>

```c
uint16_t start_frame
```

起始帧，仅用于周期性传输。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[start_frame](P077_USB主机传输结构.md#a23e4115c774134ccd143189b0f4f2460)。

<a id="r_ad2b246c850c3b30f7d2b58fc9a47008b"></a>

```c
unsigned int queued: 1
```

标志，表示请求缓冲区已入队。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[queued](P077_USB主机传输结构.md#ad2b246c850c3b30f7d2b58fc9a47008b)。

<a id="r_a9983482be9724e281e56c978ce27d93f"></a>

```c
unsigned int stage: 2
```

控制阶段状态，由驱动决定是否使用。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[stage](P077_USB主机传输结构.md#a9983482be9724e281e56c978ce27d93f)。

<a id="r_a584f5713acc9c191a5a3f4ff7d77435c"></a>

```c
unsigned int no_status: 1
```

省略控制传输的状态阶段（Status Stage）。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[no_status](P077_USB主机传输结构.md#a584f5713acc9c191a5a3f4ff7d77435c)。

<a id="r_a81a8a80809420787f4c0ab232a24a514"></a>

```c
struct usb_device * udev
```

指向USB设备的指针。

相关声明：[usb_device](P080_USB主机设备对象.md)、[udev](P077_USB主机传输结构.md#a81a8a80809420787f4c0ab232a24a514)。

<a id="r_ad4d80a3f20cdec7dd2237a98054dd287"></a>

```c
void * cb
```

传输完成回调指针，对UHC为不透明对象。

相关声明：[cb](P077_USB主机传输结构.md#ad4d80a3f20cdec7dd2237a98054dd287)。

<a id="r_a0f2d4a735ce224260d100dc756b1900f"></a>

```c
void * priv
```

完成回调的私有数据指针。

相关声明：[priv](P077_USB主机传输结构.md#a0f2d4a735ce224260d100dc756b1900f)。

<a id="r_a11f002f91b1039c226b7c9feb8223e11"></a>

```c
int err
```

传输结果，成功为0，其他值表示错误。

相关声明：[err](P077_USB主机传输结构.md#a11f002f91b1039c226b7c9feb8223e11)。

## 77.3\_详细说明（Detailed Documentation）

<a id="a170385b08171659f05ac7112faf8e587"></a>

### 77.3.1\_`buf`

```c
struct net_buf* uhc_transfer::buf
```

传输数据缓冲区。

> 译注（源码核对）：当前结构只有一个net_buf指针，原概述所称“FIFOs存储net_buf”是遗留表述。不要据此假定存在可直接操作的多缓冲FIFO；缓冲区添加和释放由对应API及调用方所有权约定负责。

<a id="ad4d80a3f20cdec7dd2237a98054dd287"></a>

### 77.3.2\_`cb`

```c
void* uhc_transfer::cb
```

传输完成回调指针，对UHC为不透明对象。

> 译注（源码核对）：UHC层保存不透明指针；当前主机事件线程将其作为usbh_udev_cb_t调用，传入udev和xfer。没有回调时，默认丢弃路径释放缓冲区并减少传输引用。

<a id="aaf664844dc9f1871cce3d38516c042ef"></a>

### 77.3.3\_`ep`

```c
uint8_t uhc_transfer::ep
```

请求关联的端点。

<a id="a11f002f91b1039c226b7c9feb8223e11"></a>

### 77.3.4\_`err`

```c
int uhc_transfer::err
```

传输结果，成功为0，其他值表示错误。

<a id="af6d6de482f092e4f85679722ad609cbf"></a>

### 77.3.5\_`interval`

```c
uint16_t uhc_transfer::interval
```

间隔，仅用于周期性传输（Periodic Transfer）。

> 译注（源码核对）：公共分配函数从端点描述符bInterval取值；这是USB端点的间隔编码，不能未经速率／传输类型解释就统一视为毫秒。

<a id="a61a6c74cc7c026404ccf42d1164765b8"></a>

### 77.3.6\_`mps`

```c
uint16_t uhc_transfer::mps
```

最大包长（Maximum Packet Size，MPS）。

<a id="a584f5713acc9c191a5a3f4ff7d77435c"></a>

### 77.3.7\_`no\_status`

```c
unsigned int uhc_transfer::no_status
```

省略控制传输的状态阶段（Status Stage）。

该标志为可选项，主要用于测试。

> 译注（源码核对）：用于测试时跳过控制传输状态阶段，不是普通控制请求都应设置的完成标志。

<a id="ae1fcb0b866e3d7c5b5ea9dff6221f37d"></a>

### 77.3.8\_`node`

```c
sys_dnode_t uhc_transfer::node
```

双向链表节点

<a id="a0f2d4a735ce224260d100dc756b1900f"></a>

### 77.3.9\_`priv`

```c
void* uhc_transfer::priv
```

完成回调的私有数据指针。

<a id="ad2b246c850c3b30f7d2b58fc9a47008b"></a>

### 77.3.10\_`queued`

```c
unsigned int uhc_transfer::queued
```

标志，表示请求缓冲区已入队。

<a id="a105b30625208c612b4abe857e208a7f1"></a>

### 77.3.11\_`ref`

```c
struct sys_ref uhc_transfer::ref
```

引用计数（Reference Count）。

<a id="ae681c0078b8afedd3b6fba165861e114"></a>

### 77.3.12\_`setup\_pkt`

```c
uint8_t uhc_transfer::setup_pkt[ROUND_UP(8, USB_PRIV_BUFGRANULARITY)]
```

控制传输的建立包（Setup Packet）。

> 译注（源码核对）：官方生成页展示展开后的数组容量；当前头文件用USB_BUF_ROUND_UP(8)并加USB_BUF_ALIGN对齐。USB建立包内容仍为8字节，缓冲区取整与对齐不改变协议长度。

<a id="a9983482be9724e281e56c978ce27d93f"></a>

### 77.3.13\_`stage`

```c
unsigned int uhc_transfer::stage
```

控制阶段状态，由驱动决定是否使用。

<a id="a23e4115c774134ccd143189b0f4f2460"></a>

### 77.3.14\_`start\_frame`

```c
uint16_t uhc_transfer::start_frame
```

起始帧，仅用于周期性传输。

<a id="ad4dbc766c6ded0ebfab7e36b19643b15"></a>

### 77.3.15\_`type`

```c
uint8_t uhc_transfer::type
```

端点类型。

<a id="a81a8a80809420787f4c0ab232a24a514"></a>

### 77.3.16\_`udev`

```c
struct usb_device* uhc_transfer::udev
```

指向USB设备的指针。

## 77.4\_源码跟踪与使用边界

译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/uhc/uhc_common.c)、[虚拟控制器](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/uhc/uhc_virtual.c)和[主机栈事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../include/zephyr/drivers/usb/uhc.h)、[公共实现](../../../drivers/usb/uhc/uhc_common.c)与[主机栈](../../../subsys/usb/host/usbh_core.c)可用于跟踪，版本可能与网页不同。此API仍为实验性接口，本批未编译或运行USB主机固件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P076_USB主机控制器事件.md) · [返回大纲](大纲.md) · [下一章](P078_USB主机栈头文件接口.md)
