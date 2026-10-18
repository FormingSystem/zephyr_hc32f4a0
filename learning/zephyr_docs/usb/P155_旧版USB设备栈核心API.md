---
id: learning.zephyr-docs.usb.api-155
title: 旧版USB设备栈核心API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group____usb__device__core__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第155章\_旧版USB设备栈核心API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group____usb__device__core__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 155.1\_阅读说明与来源

译注：本页说明旧版USB设备栈核心层（USB Device Core Layer）接口。它位于usb_dc控制器接口之上；原文的弃用标记、宏展开与全部声明均保留。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 设备核心层（USB Device Core Layer）API。

USB 设备核心层（USB Device Core Layer）API。

引入版本（Since）：1.5。

接口版本（Version）：1.0.0。

## 155.2\_数据结构（Data Structures）

<a id="r_usb_5Fep_5Fcfg_5Fdata"></a>

```c
struct usb_ep_cfg_data
```

USB 端点配置（Endpoint Configuration）。

相关声明：[usb_ep_cfg_data](P157_旧版USB端点回调配置.md)。

<a id="r_usb_5Finterface_5Fcfg_5Fdata"></a>

```c
struct usb_interface_cfg_data
```

USB 接口配置（Interface Configuration）。

相关声明：[usb_interface_cfg_data](P159_旧版USB接口请求配置.md)。

<a id="r_usb_5Fcfg_5Fdata"></a>

```c
struct usb_cfg_data
```

USB 设备配置（Device Configuration）。

相关声明：[usb_cfg_data](P156_旧版USB功能配置结构.md)。

## 155.3\_宏定义（Macros）

<a id="r_gabb531b022f5d2d859227a7b35d593d80"></a>

```c
#define USB_TRANS_READ BIT(0) __DEPRECATED_MACRO /** Read transfer flag */
```



相关声明：[USB_TRANS_READ](P155_旧版USB设备栈核心API.md#gabb531b022f5d2d859227a7b35d593d80)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga163ee39a47b0a3d9fe3697cc4f24e787"></a>

```c
#define USB_TRANS_WRITE BIT(1) __DEPRECATED_MACRO /** Write transfer flag */
```



相关声明：[USB_TRANS_WRITE](P155_旧版USB设备栈核心API.md#ga163ee39a47b0a3d9fe3697cc4f24e787)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga81c618544f27e0dc0e556021b0418c40"></a>

```c
#define USB_TRANS_NO_ZLP BIT(2) __DEPRECATED_MACRO /** No zero-length packet flag */
```



相关声明：[USB_TRANS_NO_ZLP](P155_旧版USB设备栈核心API.md#ga81c618544f27e0dc0e556021b0418c40)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga40975f1b023ea36118137e86e099e649"></a>

```c
#define USB_DEVICE_BOS_DESC_DEFINE_CAP static __in_section(usb, bos_desc_area, 1) __aligned(1) __used __DEPRECATED_MACRO
```

把 BOS 兼容性描述符放入正确内存段的辅助宏。

相关声明：[USB_DEVICE_BOS_DESC_DEFINE_CAP](P155_旧版USB设备栈核心API.md#ga40975f1b023ea36118137e86e099e649)。

## 155.4\_类型定义（Typedefs）

<a id="r_ga9a45db26a9be295640ed122533427725"></a>

```c
typedef void(* usb_ep_callback) (uint8_t ep, enum usb_dc_ep_cb_status_code cb_status)
```

USB 端点状态回调的函数签名。

相关声明：[usb_ep_callback](P155_旧版USB设备栈核心API.md#ga9a45db26a9be295640ed122533427725)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usb_dc_ep_cb_status_code](P152_旧版USB控制器驱动API.md#gaf7f083f61e1406e7d41513113dccd3bd)。

<a id="r_gaddacbff094a41c885c3041af72fa6804"></a>

```c
typedef int(* usb_request_handler) (struct usb_setup_packet *setup, int32_t *transfer_len, uint8_t **payload_data)
```

类专用请求（Class-Specific Request）回调的函数签名。

相关声明：[usb_request_handler](P155_旧版USB设备栈核心API.md#gaddacbff094a41c885c3041af72fa6804)、[usb_setup_packet](P160_USB控制请求包.md)、[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga3439af9464471b3acdc21f4359efb53a"></a>

```c
typedef void(* usb_interface_config) (struct usb_desc_header *head, uint8_t bInterfaceNumber)
```

用于接口运行时配置（Runtime Configuration）的函数。

相关声明：[usb_interface_config](P155_旧版USB设备栈核心API.md#ga3439af9464471b3acdc21f4359efb53a)、[usb_desc_header](P161_USB通用描述符头.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga2e599eb20f647d9bb2369d76a7dc51db"></a>

```c
typedef void(* usb_transfer_callback) (uint8_t ep, int tsize, void *priv)
```

传输完成回调（Transfer Completion Callback）的函数签名。

相关声明：[usb_transfer_callback](P155_旧版USB设备栈核心API.md#ga2e599eb20f647d9bb2369d76a7dc51db)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

## 155.5\_函数（Functions）

<a id="r_ga28783e727e35db1a651309a7f9f5444a"></a>

```c
int usb_set_config (const uint8_t *usb_descriptor)
```

配置 USB 控制器。

相关声明：[usb_set_config](P155_旧版USB设备栈核心API.md#ga28783e727e35db1a651309a7f9f5444a)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga2d485c77055dd975f3170fbaea7f2bdf"></a>

```c
int usb_deconfig (void)
```

撤销 USB 控制器配置。

相关声明：[usb_deconfig](P155_旧版USB设备栈核心API.md#ga2d485c77055dd975f3170fbaea7f2bdf)。

<a id="r_gad1fa5e491d93c2bd1fe7967c12148902"></a>

```c
int usb_enable (usb_dc_status_callback status_cb)
```

启用 USB 子系统及关联硬件。

相关声明：[usb_enable](P155_旧版USB设备栈核心API.md#gad1fa5e491d93c2bd1fe7967c12148902)、[usb_dc_status_callback](P152_旧版USB控制器驱动API.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee)。

<a id="r_ga65723c9469a12c87e5554169396f8e76"></a>

```c
int usb_disable (void)
```

禁用 USB 设备。

相关声明：[usb_disable](P155_旧版USB设备栈核心API.md#ga65723c9469a12c87e5554169396f8e76)。

<a id="r_ga6d4b568f2f3aac4f099c35393fb601b3"></a>

```c
int usb_write (uint8_t ep, const uint8_t *data, uint32_t data_len, uint32_t *bytes_ret)
```

向指定端点写入数据。

相关声明：[usb_write](P155_旧版USB设备栈核心API.md#ga6d4b568f2f3aac4f099c35393fb601b3)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_gab2c21738baa839b483654d1d5baf2981"></a>

```c
int usb_read (uint8_t ep, uint8_t *data, uint32_t max_data_len, uint32_t *ret_bytes)
```

从指定端点读取数据。

相关声明：[usb_read](P155_旧版USB设备栈核心API.md#gab2c21738baa839b483654d1d5baf2981)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_gaaf206afaf32bde1b8d77d04bc6ec091f"></a>

```c
int usb_ep_set_stall (uint8_t ep)
```

为指定端点设置停滞状态（STALL）。

相关声明：[usb_ep_set_stall](P155_旧版USB设备栈核心API.md#gaaf206afaf32bde1b8d77d04bc6ec091f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gae7bc410d0db8a6d2142992153bb1424d"></a>

```c
int usb_ep_clear_stall (uint8_t ep)
```

清除指定端点的停滞状态（STALL）。

相关声明：[usb_ep_clear_stall](P155_旧版USB设备栈核心API.md#gae7bc410d0db8a6d2142992153bb1424d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga4c919f7e993f80150bdde2d7fab254ee"></a>

```c
int usb_ep_read_wait (uint8_t ep, uint8_t *data, uint32_t max_data_len, uint32_t *read_bytes)
```

从指定端点读取数据。

相关声明：[usb_ep_read_wait](P155_旧版USB设备栈核心API.md#ga4c919f7e993f80150bdde2d7fab254ee)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_gaab17b8c523ac211ff308c8dc774ba092"></a>

```c
int usb_ep_read_continue (uint8_t ep)
```

继续从端点读取数据。

相关声明：[usb_ep_read_continue](P155_旧版USB设备栈核心API.md#gaab17b8c523ac211ff308c8dc774ba092)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gae07256f6b4c1df494025a87bb6dbfd51"></a>

```c
void usb_transfer_ep_callback (uint8_t ep, enum usb_dc_ep_cb_status_code status)
```

用于管理传输的端点回调。

相关声明：[usb_transfer_ep_callback](P155_旧版USB设备栈核心API.md#gae07256f6b4c1df494025a87bb6dbfd51)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usb_dc_ep_cb_status_code](P152_旧版USB控制器驱动API.md#gaf7f083f61e1406e7d41513113dccd3bd)。

<a id="r_ga27c3040dca474b5b45e6bea63a500cce"></a>

```c
int usb_transfer (uint8_t ep, uint8_t *data, size_t dlen, unsigned int flags, usb_transfer_callback cb, void *priv)
```

启动一次传输。

相关声明：[usb_transfer](P155_旧版USB设备栈核心API.md#ga27c3040dca474b5b45e6bea63a500cce)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[usb_transfer_callback](P155_旧版USB设备栈核心API.md#ga2e599eb20f647d9bb2369d76a7dc51db)。

<a id="r_ga1060e3a473a7f0bc71763a413e91ab56"></a>

```c
int usb_transfer_sync (uint8_t ep, uint8_t *data, size_t dlen, unsigned int flags)
```

启动传输并阻塞等待完成。

相关声明：[usb_transfer_sync](P155_旧版USB设备栈核心API.md#ga1060e3a473a7f0bc71763a413e91ab56)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_gab399dc4a43a99c927ee7588a57c49211"></a>

```c
void usb_cancel_transfer (uint8_t ep)
```

取消指定端点正在进行的传输。

相关声明：[usb_cancel_transfer](P155_旧版USB设备栈核心API.md#gab399dc4a43a99c927ee7588a57c49211)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga758a63b22c48d2ae9d025adb92ed5925"></a>

```c
void usb_cancel_transfers (void)
```

取消所有正在进行的传输。

相关声明：[usb_cancel_transfers](P155_旧版USB设备栈核心API.md#ga758a63b22c48d2ae9d025adb92ed5925)。

<a id="r_ga6292a473cffc1f8683da902c2a85d653"></a>

```c
bool usb_transfer_is_busy (uint8_t ep)
```

检查端点是否有传输正在进行。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[usb_transfer_is_busy](P155_旧版USB设备栈核心API.md#ga6292a473cffc1f8683da902c2a85d653)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga7d67c8d49b52fb33818d654ca647c1e5"></a>

```c
int usb_wakeup_request (void)
```

启动 USB 远程唤醒（Remote Wakeup）过程。

相关声明：[usb_wakeup_request](P155_旧版USB设备栈核心API.md#ga7d67c8d49b52fb33818d654ca647c1e5)。

<a id="r_ga577018c415eec38ef5038cdb2f45ed2f"></a>

```c
bool usb_get_remote_wakeup_status (void)
```

取得 USB 远程唤醒功能的状态。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[usb_get_remote_wakeup_status](P155_旧版USB设备栈核心API.md#ga577018c415eec38ef5038cdb2f45ed2f)。

<a id="r_ga1bf8ec88cf752e98234d9f8bb57f976a"></a>

```c
void usb_bos_register_cap (void *hdr)
```

注册 BOS 能力描述符（Capability Descriptor）。

相关声明：[usb_bos_register_cap](P155_旧版USB设备栈核心API.md#ga1bf8ec88cf752e98234d9f8bb57f976a)。

## 155.6\_详细说明（Detailed Documentation）

<a id="ga40975f1b023ea36118137e86e099e649"></a>

### 155.6.1\_`USB_DEVICE_BOS_DESC_DEFINE_CAP`

```c
#define USB_DEVICE_BOS_DESC_DEFINE_CAP static __in_section(usb, bos_desc_area, 1) __aligned(1) __used __DEPRECATED_MACRO
```

```c
#include <zephyr/usb/usb_device.h>
```

把 BOS 兼容性描述符放入正确内存段的辅助宏。

> 译注（源码核对）：原说明使用compatibility一词；此处实际用于BOS设备能力描述符。宏把静态对象放入usb/bos_desc_area对应的链接段，并要求1字节对齐；它不是完成设备栈启用或处理厂商请求的宏。

<a id="ga81c618544f27e0dc0e556021b0418c40"></a>

### 155.6.2\_`USB_TRANS_NO_ZLP`

```c
#define USB_TRANS_NO_ZLP BIT(2) __DEPRECATED_MACRO /** No zero-length packet flag */
```

```c
#include <zephyr/usb/usb_device.h>
```

> 译注（源码核对）：原注释No zero-length packet flag译为“不发送零长度包标志”。ZLP即Zero-Length Packet。当前实现发送长度不是端点MPS整数倍时，会自动设置此标志；不要把它误解为USB事务永远不能使用零长度状态包。

<a id="gabb531b022f5d2d859227a7b35d593d80"></a>

### 155.6.3\_`USB_TRANS_READ`

```c
#define USB_TRANS_READ BIT(0) __DEPRECATED_MACRO /** Read transfer flag */
```

```c
#include <zephyr/usb/usb_device.h>
```

> 译注（源码核对）：原注释Read transfer flag译为“读取传输标志”。此值为BIT(0)，用于高层接收传输。

<a id="ga163ee39a47b0a3d9fe3697cc4f24e787"></a>

### 155.6.4\_`USB_TRANS_WRITE`

```c
#define USB_TRANS_WRITE BIT(1) __DEPRECATED_MACRO /** Write transfer flag */
```

```c
#include <zephyr/usb/usb_device.h>
```

> 译注（源码核对）：原注释Write transfer flag译为“写入传输标志”。此值为BIT(1)，用于高层发送传输。

<a id="ga9a45db26a9be295640ed122533427725"></a>

### 155.6.5\_`usb_ep_callback`

```c
typedef void(* usb_ep_callback) (uint8_t ep, enum usb_dc_ep_cb_status_code cb_status)
```

```c
#include <zephyr/usb/usb_device.h>
```

USB 端点状态回调的函数签名。

<a id="ga3439af9464471b3acdc21f4359efb53a"></a>

### 155.6.6\_`usb_interface_config`

```c
typedef void(* usb_interface_config) (struct usb_desc_header *head, uint8_t bInterfaceNumber)
```

```c
#include <zephyr/usb/usb_device.h>
```

用于接口运行时配置（Runtime Configuration）的函数。

<a id="gaddacbff094a41c885c3041af72fa6804"></a>

### 155.6.7\_`usb_request_handler`

```c
typedef int(* usb_request_handler) (struct usb_setup_packet *setup, int32_t *transfer_len, uint8_t **payload_data)
```

```c
#include <zephyr/usb/usb_device.h>
```

类专用请求（Class-Specific Request）回调的函数签名。

此函数处理与设备描述符表中指定接口编号对应的类专用请求。对于主机到设备方向，len 与 payload_data 分别包含已接收数据的长度和指针。对于设备到主机方向的类请求，回调应分别将 len 与 payload_data 设置为待发送缓冲区的数据长度和地址。

> 译注（源码核对）：说明中的len对应函数声明参数transfer_len。请求处理必须区分主机到设备和设备到主机两个方向；后者要同时提供响应长度与数据地址，不能只写一个返回字节数。

<a id="ga2e599eb20f647d9bb2369d76a7dc51db"></a>

### 155.6.8\_`usb_transfer_callback`

```c
typedef void(* usb_transfer_callback) (uint8_t ep, int tsize, void *priv)
```

```c
#include <zephyr/usb/usb_device.h>
```

传输完成回调（Transfer Completion Callback）的函数签名。

> 译注（源码核对）：当前实现传给tsize的是累计传输字节数，内部错误状态没有作为独立回调参数传出。因此不能把tsize当作完整的errno通道，也不能仅凭0字节完成区分取消、未就绪与正常零长度操作。

<a id="ga1bf8ec88cf752e98234d9f8bb57f976a"></a>

### 155.6.9\_`usb_bos_register_cap()`

```c
void usb_bos_register_cap ( void * hdr)
```

```c
#include <zephyr/usb/usb_device.h>
```

注册 BOS 能力描述符（Capability Descriptor）。

应用应在启用 USB 设备栈之前，使用此函数注册 BOS 能力描述符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] hdr` | 指向 BOS 能力描述符。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

<a id="gab399dc4a43a99c927ee7588a57c49211"></a>

### 155.6.10\_`usb_cancel_transfer()`

```c
void usb_cancel_transfer ( uint8_t ep)
```

```c
#include <zephyr/usb/usb_device.h>
```

取消指定端点正在进行的传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

> 译注（源码核对）：当前实现把正在传输的状态改为-ECANCELED并提交USB工作项，函数返回并不等于完成回调已经运行。缓冲区回收须结合实际完成路径，不应在发出取消后无条件立即复用。

<a id="ga758a63b22c48d2ae9d025adb92ed5925"></a>

### 155.6.11\_`usb_cancel_transfers()`

```c
void usb_cancel_transfers ( void )
```

```c
#include <zephyr/usb/usb_device.h>
```

取消所有正在进行的传输。

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

<a id="ga2d485c77055dd975f3170fbaea7f2bdf"></a>

### 155.6.12\_`usb_deconfig()`

```c
int usb_deconfig ( void )
```

```c
#include <zephyr/usb/usb_device.h>
```

撤销 USB 控制器配置。

此函数使 USB 设备回到初始状态。

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：当前实现注销描述符及若干回调并调用usb_dc_reset()，随后直接返回0，没有传播该底层复位的返回值。它与usb_disable()的断开、取消传输和禁用端点流程不同。

<a id="ga65723c9469a12c87e5554169396f8e76"></a>

### 155.6.13\_`usb_disable()`

```c
int usb_disable ( void )
```

```c
#include <zephyr/usb/usb_device.h>
```

禁用 USB 设备。

此函数禁用 USB 设备。成功后，指定 USB 接口在硬件中被门控时钟，不再能够产生中断。

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="gad1fa5e491d93c2bd1fe7967c12148902"></a>

### 155.6.14\_`usb_enable()`

```c
int usb_enable ( usb_dc_status_callback status_cb)
```

```c
#include <zephyr/usb/usb_device.h>
```

启用 USB 子系统及关联硬件。

此函数初始化 USB 核心子系统并启用相应硬件，使其能够在 USB 总线上收发数据及产生中断。

用户必须在调用此函数之前完成类专用初始化和注册，确保相关类处理代码能够正确处理总线上的数据与事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] status_cb` | 用户注册的回调，用于通知 USB 设备控制器状态。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：当前实现用互斥量串行化启用过程；已启用时返回-EALREADY。如果尚未设置描述符，会尝试取得默认描述符并调用usb_set_config()，但类专用准备工作仍必须符合原接口要求。

<a id="gae7bc410d0db8a6d2142992153bb1424d"></a>

### 155.6.15\_`usb_ep_clear_stall()`

```c
int usb_ep_clear_stall ( uint8_t ep)
```

```c
#include <zephyr/usb/usb_device.h>
```

清除指定端点的停滞状态（STALL）。

USB 设备类处理代码调用此函数，清除端点的停滞状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="gaab17b8c523ac211ff308c8dc774ba092"></a>

### 155.6.16\_`usb_ep_read_continue()`

```c
int usb_ep_read_continue ( uint8_t ep)
```

```c
#include <zephyr/usb/usb_device.h>
```

继续从端点读取数据。

清除端点 NAK，使端点能够接收主机发送的更多数据。通常在 usb_ep_read_wait() 之后、消费者准备好接收更多数据时调用，因此这两个调用共同形成流量控制机制（Flow Control）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga4c919f7e993f80150bdde2d7fab254ee"></a>

### 155.6.17\_`usb_ep_read_wait()`

```c
int usb_ep_read_wait ( uint8_t ep, uint8_t * data, uint32_t max_data_len, uint32_t * read_bytes )
```

```c
#include <zephyr/usb/usb_device.h>
```

从指定端点读取数据。

此函数类似 usb_ep_read，但不会清除端点 NAK，使消费者在完成数据处理前不会被更多向上回调淹没。调用者应随后通过 usb_ep_read_continue() 重新启用端点接收。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |
| `[in] data` | 指向用于写入所读数据的缓冲区。 |
| `[in] max_data_len` | 最多读取的数据长度。 |
| `[out] read_bytes` | 已读取的字节数。如果 data 为 NULL 且 max_data_len 为 0，则应返回当前可读取的字节数。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：原说明提到usb_ep_read，本头文件对应的普通读取接口实际名为usb_read()。wait版本保留端点NAK，由usb_ep_read_continue()重新允许接收；这里不是等待直到有数据的同步传输接口。

<a id="gaaf206afaf32bde1b8d77d04bc6ec091f"></a>

### 155.6.18\_`usb_ep_set_stall()`

```c
int usb_ep_set_stall ( uint8_t ep)
```

```c
#include <zephyr/usb/usb_device.h>
```

为指定端点设置停滞状态（STALL）。

USB 设备类处理代码调用此函数，设置端点的停滞状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga577018c415eec38ef5038cdb2f45ed2f"></a>

### 155.6.19\_`usb_get_remote_wakeup_status()`

```c
bool usb_get_remote_wakeup_status ( void )
```

```c
#include <zephyr/usb/usb_device.h>
```

取得 USB 远程唤醒功能的状态。

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：主机已启用远程唤醒时返回 true，否则返回 false。

<a id="gab2c21738baa839b483654d1d5baf2981"></a>

### 155.6.20\_`usb_read()`

```c
int usb_read ( uint8_t ep, uint8_t * data, uint32_t max_data_len, uint32_t * ret_bytes )
```

```c
#include <zephyr/usb/usb_device.h>
```

从指定端点读取数据。

端点收到 OUT 中断后，由端点处理函数调用此函数。应用必须仅通过提供的 usb_ep_callback 函数调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |
| `[in] data` | 指向用于写入所读数据的缓冲区。 |
| `[in] max_data_len` | 最多读取的数据长度。 |
| `[out] ret_bytes` | 已读取的字节数。如果 data 为 NULL 且 max_data_len 为 0，则返回当前可读取的字节数。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

<a id="ga28783e727e35db1a651309a7f9f5444a"></a>

### 155.6.21\_`usb_set_config()`

```c
int usb_set_config ( const uint8_t * usb_descriptor)
```

```c
#include <zephyr/usb/usb_device.h>
```

配置 USB 控制器。

此函数配置 USB 控制器。配置参数必须有效，否则返回错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] usb_descriptor` | USB 描述符表。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：当前实现保存描述符指针并注册请求处理器，直接返回0，未执行原注释暗示的完整参数校验。不能依赖返回0证明描述符内容、长度和生命周期全部有效。

<a id="ga27c3040dca474b5b45e6bea63a500cce"></a>

### 155.6.22\_`usb_transfer()`

```c
int usb_transfer ( uint8_t ep, uint8_t * data, size_t dlen, unsigned int flags, usb_transfer_callback cb, void * priv )
```

```c
#include <zephyr/usb/usb_device.h>
```

启动一次传输。

启动从数据缓冲区发送或向缓冲区接收的 USB 传输。此函数为异步（Asynchronous）接口，可以在中断请求上下文（IRQ Context）执行。传输完成或出错时，提供的回调在线程上下文（Thread Context）执行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |
| `[in] data` | 指向用于写入或读出的数据缓冲区。 |
| `[in] dlen` | 数据缓冲区大小。 |
| `[in] flags` | 传输标志（Transfer Flags），例如 USB_TRANS_READ、USB_TRANS_WRITE 等。 |
| `[in] cb` | 传输完成或失败时调用的函数。 |
| `[in] priv` | 传回传输完成回调的用户数据。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

> 译注（源码核对）：当前实现保存data指针，不复制整个应用缓冲区；缓冲区应保持有效直到完成通知。相同端点不允许同时存在两次传输，可能返回-EBUSY；内部传输槽不足可能返回-ENOMEM。完成回调由USB工作队列在线程上下文执行，ep回调仍需注册usb_transfer_ep_callback。

<a id="gae07256f6b4c1df494025a87bb6dbfd51"></a>

### 155.6.23\_`usb_transfer_ep_callback()`

```c
void usb_transfer_ep_callback ( uint8_t ep, enum usb_dc_ep_cb_status_code status )
```

```c
#include <zephyr/usb/usb_device.h>
```

用于管理传输的端点回调。

USB 类驱动若要使用高层传输函数，需要将此回调注册为 USB 端点回调。

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

<a id="ga6292a473cffc1f8683da902c2a85d653"></a>

### 155.6.24\_`usb_transfer_is_busy()`

```c
bool usb_transfer_is_busy ( uint8_t ep)
```

```c
#include <zephyr/usb/usb_device.h>
```

检查端点是否有传输正在进行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：传输正在进行时返回 true，否则返回 false。

<a id="ga1060e3a473a7f0bc71763a413e91ab56"></a>

### 155.6.25\_`usb_transfer_sync()`

```c
int usb_transfer_sync ( uint8_t ep, uint8_t * data, size_t dlen, unsigned int flags )
```

```c
#include <zephyr/usb/usb_device.h>
```

启动传输并阻塞等待完成。

这是 usb_transfer 的同步（Synchronous）版本，返回前等待传输完成。返回值为零也可能意味着传输被取消，或端点尚未就绪；这是传输机制及 usb_dc API 的设计所致。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |
| `[in] data` | 指向用于写入或读出的数据缓冲区。 |
| `[in] dlen` | 数据缓冲区大小。 |
| `[in] flags` | 传输标志。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回已传输字节数，失败时返回负的 errno 错误码。

> 译注（源码核对）：当前实现以K_FOREVER等待由完成回调释放的信号量，没有超时参数。同步调用需要能等待的线程上下文，不能因异步usb_transfer允许IRQ上下文就把相同前提套用到此函数；还应避免阻塞执行其完成回调所需的USB工作队列。

<a id="ga7d67c8d49b52fb33818d654ca647c1e5"></a>

### 155.6.26\_`usb_wakeup_request()`

```c
int usb_wakeup_request ( void )
```

```c
#include <zephyr/usb/usb_device.h>
```

启动 USB 远程唤醒（Remote Wakeup）过程。

此函数请求远程唤醒。必须在配置中启用该功能，否则始终返回 -ENOTSUP 错误。

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码，例如总线已处于活动状态时。

<a id="ga6d4b568f2f3aac4f099c35393fb601b3"></a>

### 155.6.27\_`usb_write()`

```c
int usb_write ( uint8_t ep, const uint8_t * data, uint32_t data_len, uint32_t * bytes_ret )
```

```c
#include <zephyr/usb/usb_device.h>
```

向指定端点写入数据。

此函数向指定端点写入数据。传输完成后调用提供的 usb_ep_callback。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ep` | 端点地址，应与设备配置表中列出的地址对应。 |
| `[in] data` | 指向待写入数据。 |
| `[in] data_len` | 请求写入的数据长度；发送零长度状态包（Zero-Length Status Packet）时可以为零。 |
| `[out] bytes_ret` | 写入端点 FIFO 的字节数。如果应用预期全部字节都会写入，此指针可以为 NULL。 |

**已弃用（Deprecated）**：请改用[新版USB设备核心API（USBD）](P015_USB设备核心API.md)。

**返回（Returns）**：成功时返回 0，失败时返回负的 errno 错误码。

## 155.7\_源码跟踪与使用边界

译注依据保存的[官方usb_device头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_device.h)、[旧版设备栈核心](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_device.c)、[传输实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_transfer.c)与[BOS管理实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/bos.c)，摘要见[来源记录](../SOURCES.md)。本仓库[公共头文件](../../../include/zephyr/usb/usb_device.h)与[传输实现](../../../subsys/usb/device/usb_transfer.c)可用于相对路径源码跟踪，版本可能与网页不同。对应控制器接口见[usb_dc参考](P152_旧版USB控制器驱动API.md)；本批没有构建、烧录或执行USB传输测试。

## 155.8\_原始版权与许可

本页声明与宏源自采用BSD-3-Clause许可的usb_device.h；译文集通用许可不覆盖该独立许可。以下逐字保留原始署名、再分发条件与免责声明，代码标识及作者联系方式不改写。

```c
/* SPDX-License-Identifier: BSD-3-Clause */

/*
 *  LPCUSB, an USB device driver for LPC microcontrollers
 *  Copyright (C) 2006 Bertrik Sikken (bertrik@sikken.nl)
 *  Copyright (c) 2016 Intel Corporation
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions are met:
 *
 *  1. Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *  2. Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *  3. The name of the author may not be used to endorse or promote products
 *     derived from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 *  IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 *  OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 *  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 *  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 *  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 *  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 *  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
```

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P154_旧版USB控制器头文件接口.md) · [返回大纲](大纲.md) · [下一章](P156_旧版USB功能配置结构.md)
