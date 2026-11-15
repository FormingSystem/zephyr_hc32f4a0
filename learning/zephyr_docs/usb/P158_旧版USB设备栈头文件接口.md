---
id: learning.zephyr-docs.usb.api-158
title: 旧版USB设备栈头文件接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__device_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第158章\_旧版USB设备栈头文件接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__device_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 158.1\_阅读说明与来源

译注：本页说明旧版USB设备栈核心层（USB Device Core Layer）接口。它位于usb_dc控制器接口之上；原文的弃用标记、宏展开与全部声明均保留。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB 设备核心层 API 与结构。

```c
#include <zephyr/drivers/usb/usb_dc.h>
```

```c
#include <zephyr/usb/usb_ch9.h>
```

```c
#include <zephyr/logging/log.h>
```

```c
#include <zephyr/sys/iterable_sections.h>
```

USB 设备核心层 API 与结构。

此文件包含 USB 设备核心层 API 与结构。

## 158.2\_数据结构（Data Structures）

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

## 158.3\_宏定义（Macros）

<a id="r_a95efe03ee4bbfa4d9b0c3932b8ddfe31"></a>

```c
#define USBD_DEVICE_DESCR_DEFINE(p)
```



相关声明：[USBD_DEVICE_DESCR_DEFINE](P158_旧版USB设备栈头文件接口.md#a95efe03ee4bbfa4d9b0c3932b8ddfe31)。

<a id="r_a9403c2bd43e638b4d5634288dfb6574b"></a>

```c
#define USBD_CLASS_DESCR_DEFINE(p, instance)
```



相关声明：[USBD_CLASS_DESCR_DEFINE](P158_旧版USB设备栈头文件接口.md#a9403c2bd43e638b4d5634288dfb6574b)。

<a id="r_a6ff803fe6831ca99e3e9543dd1d2f37d"></a>

```c
#define USBD_MISC_DESCR_DEFINE(p)
```



相关声明：[USBD_MISC_DESCR_DEFINE](P158_旧版USB设备栈头文件接口.md#a6ff803fe6831ca99e3e9543dd1d2f37d)。

<a id="r_a76a98dcc6ca0284195d61bb928197e38"></a>

```c
#define USBD_USER_DESCR_DEFINE(p)
```



相关声明：[USBD_USER_DESCR_DEFINE](P158_旧版USB设备栈头文件接口.md#a76a98dcc6ca0284195d61bb928197e38)。

<a id="r_acb8451e935bab6c8fe2f7eea97a8ae6f"></a>

```c
#define USBD_STRING_DESCR_DEFINE(p)
```



相关声明：[USBD_STRING_DESCR_DEFINE](P158_旧版USB设备栈头文件接口.md#acb8451e935bab6c8fe2f7eea97a8ae6f)。

<a id="r_a5bc3e0d5484c0c54e5996d99ebedc51b"></a>

```c
#define USBD_STRING_DESCR_USER_DEFINE(p)
```



相关声明：[USBD_STRING_DESCR_USER_DEFINE](P158_旧版USB设备栈头文件接口.md#a5bc3e0d5484c0c54e5996d99ebedc51b)。

<a id="r_a2ad0dd7628d3038c32809e6850baf23f"></a>

```c
#define USBD_TERM_DESCR_DEFINE(p)
```



相关声明：[USBD_TERM_DESCR_DEFINE](P158_旧版USB设备栈头文件接口.md#a2ad0dd7628d3038c32809e6850baf23f)。

<a id="r_a5db8e2eb30dd2afc51dbb9e08fbc07c6"></a>

```c
#define USBD_DEFINE_CFG_DATA(name)
```



相关声明：[USBD_DEFINE_CFG_DATA](P158_旧版USB设备栈头文件接口.md#a5db8e2eb30dd2afc51dbb9e08fbc07c6)。

<a id="r_a3d01cf3cbbd08db3d6cfcfb45062b961"></a>

```c
#define USB_MAX_CTRL_MPS 64 __DEPRECATED_MACRO
```

端点 0 的最大包大小（Maximum Packet Size，MPS）。

相关声明：[USB_MAX_CTRL_MPS](P158_旧版USB设备栈头文件接口.md#a3d01cf3cbbd08db3d6cfcfb45062b961)。

<a id="r_a07bbd07466b47a0c498f26e25932392f"></a>

```c
#define USB_MAX_FS_BULK_MPS 64 __DEPRECATED_MACRO
```

全速（Full Speed）批量端点的最大包大小。

相关声明：[USB_MAX_FS_BULK_MPS](P158_旧版USB设备栈头文件接口.md#a07bbd07466b47a0c498f26e25932392f)。

<a id="r_ae88dc2d0b2a21779d8c353cd63ae3455"></a>

```c
#define USB_MAX_FS_INT_MPS 64 __DEPRECATED_MACRO
```

全速中断端点的最大包大小。

相关声明：[USB_MAX_FS_INT_MPS](P158_旧版USB设备栈头文件接口.md#ae88dc2d0b2a21779d8c353cd63ae3455)。

<a id="r_ae45dfb00deef73b2a142576bf136b062"></a>

```c
#define USB_MAX_FS_ISO_MPS 1023 __DEPRECATED_MACRO
```

全速等时端点的最大包大小。

相关声明：[USB_MAX_FS_ISO_MPS](P158_旧版USB设备栈头文件接口.md#ae45dfb00deef73b2a142576bf136b062)。

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

## 158.4\_类型定义（Typedefs）

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

## 158.5\_函数（Functions）

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

## 158.6\_详细说明（Detailed Documentation）

<a id="a3d01cf3cbbd08db3d6cfcfb45062b961"></a>

### 158.6.1\_`USB_MAX_CTRL_MPS`

```c
#define USB_MAX_CTRL_MPS 64 __DEPRECATED_MACRO
```

端点 0 的最大包大小（Maximum Packet Size，MPS）。

<a id="a07bbd07466b47a0c498f26e25932392f"></a>

### 158.6.2\_`USB_MAX_FS_BULK_MPS`

```c
#define USB_MAX_FS_BULK_MPS 64 __DEPRECATED_MACRO
```

全速（Full Speed）批量端点的最大包大小。

<a id="ae88dc2d0b2a21779d8c353cd63ae3455"></a>

### 158.6.3\_`USB_MAX_FS_INT_MPS`

```c
#define USB_MAX_FS_INT_MPS 64 __DEPRECATED_MACRO
```

全速中断端点的最大包大小。

<a id="ae45dfb00deef73b2a142576bf136b062"></a>

### 158.6.4\_`USB_MAX_FS_ISO_MPS`

```c
#define USB_MAX_FS_ISO_MPS 1023 __DEPRECATED_MACRO
```

全速等时端点的最大包大小。

<a id="a9403c2bd43e638b4d5634288dfb6574b"></a>

### 158.6.5\_`USBD_CLASS_DESCR_DEFINE`

```c
#define USBD_CLASS_DESCR_DEFINE ( p, instance )
```

**宏展开值（Value）**

```c
static __in_section(usb, descriptor_##p.1, instance) __used __aligned(1) __DEPRECATED_MACRO
```

<a id="a5db8e2eb30dd2afc51dbb9e08fbc07c6"></a>

### 158.6.6\_`USBD_DEFINE_CFG_DATA`

```c
#define USBD_DEFINE_CFG_DATA ( name)
```

**宏展开值（Value）**

```c
static STRUCT_SECTION_ITERABLE(usb_cfg_data, name) __DEPRECATED_MACRO
```

> 译注（源码核对）：该宏将静态usb_cfg_data对象放入可遍历的链接段（Iterable Section），供设备栈扫描。它本身不会把整个对象复制到新的运行时缓冲区。

<a id="a95efe03ee4bbfa4d9b0c3932b8ddfe31"></a>

### 158.6.7\_`USBD_DEVICE_DESCR_DEFINE`

```c
#define USBD_DEVICE_DESCR_DEFINE ( p)
```

**宏展开值（Value）**

```c
static __in_section(usb, descriptor_##p, 0) __used __aligned(1) __DEPRECATED_MACRO
```

<a id="a6ff803fe6831ca99e3e9543dd1d2f37d"></a>

### 158.6.8\_`USBD_MISC_DESCR_DEFINE`

```c
#define USBD_MISC_DESCR_DEFINE ( p)
```

**宏展开值（Value）**

```c
static __in_section(usb, descriptor_##p, 2) __used __aligned(1) __DEPRECATED_MACRO
```

<a id="acb8451e935bab6c8fe2f7eea97a8ae6f"></a>

### 158.6.9\_`USBD_STRING_DESCR_DEFINE`

```c
#define USBD_STRING_DESCR_DEFINE ( p)
```

**宏展开值（Value）**

```c
static __in_section(usb, descriptor_##p, 4) __used __aligned(1) __DEPRECATED_MACRO
```

<a id="a5bc3e0d5484c0c54e5996d99ebedc51b"></a>

### 158.6.10\_`USBD_STRING_DESCR_USER_DEFINE`

```c
#define USBD_STRING_DESCR_USER_DEFINE ( p)
```

**宏展开值（Value）**

```c
static __in_section(usb, descriptor_##p, 5) __used __aligned(1) __DEPRECATED_MACRO
```

<a id="a2ad0dd7628d3038c32809e6850baf23f"></a>

### 158.6.11\_`USBD_TERM_DESCR_DEFINE`

```c
#define USBD_TERM_DESCR_DEFINE ( p)
```

**宏展开值（Value）**

```c
static __in_section(usb, descriptor_##p, 6) __used __aligned(1) __DEPRECATED_MACRO
```

<a id="a76a98dcc6ca0284195d61bb928197e38"></a>

### 158.6.12\_`USBD_USER_DESCR_DEFINE`

```c
#define USBD_USER_DESCR_DEFINE ( p)
```

**宏展开值（Value）**

```c
static __in_section(usb, descriptor_##p, 3) __used __aligned(1) __DEPRECATED_MACRO
```

## 158.7\_源码跟踪与使用边界

译注依据保存的[官方usb_device头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usb_device.h)、[旧版设备栈核心](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_device.c)、[传输实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/usb_transfer.c)与[BOS管理实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/bos.c)，摘要见[来源记录](../SOURCES.md)。本仓库[公共头文件](../../../include/zephyr/usb/usb_device.h)与[传输实现](../../../subsys/usb/device/usb_transfer.c)可用于相对路径源码跟踪，版本可能与网页不同。对应控制器接口见[usb_dc参考](P152_旧版USB控制器驱动API.md)；本批没有构建、烧录或执行USB传输测试。

## 158.8\_原始版权与许可

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
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructusb__cfg__data_html"></a>

[上一章](P157_旧版USB端点回调配置.md) · [返回大纲](大纲.md) · [下一章](P159_旧版USB接口请求配置.md)
