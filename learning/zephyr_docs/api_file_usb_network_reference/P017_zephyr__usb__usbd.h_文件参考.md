---
id: learning.zephyr-docs.api-file-usb-network-reference.page-17
title: zephyr__usb__usbd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_usb\_\_usbd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

新USB设备协议栈（Device Stack）的API和结构。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/usb/bos.h>
#include <zephyr/usb/usb_ch9.h>
#include <zephyr/usb/usbd_msg.h>
#include <zephyr/drivers/usb/usb_buf.h>
#include <zephyr/sys/byteorder.h>
#include <zephyr/sys/slist.h>
#include <zephyr/logging/log.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

新版 USB 设备协议栈 API 与结构体（New USB Device Stack APIs and Structures）。本文件包含 USB 设备协议栈的 API 和结构体。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

<a id="r_usbd_5Fstr_5Fdesc_5Fdata"></a>

```c
struct usbd_str_desc_data
```

相关声明：[usbd_str_desc_data](../usb/P018_USB字符串描述符数据.md)。

内部使用，用于保持描述符（Descriptors）的顺序。

<a id="r_usbd_5Fvreq_5Fnode"></a>

```c
struct usbd_vreq_node
```

相关声明：[usbd_vreq_node](../usb/P019_USB厂商请求节点.md)。

USB设备（USBD）的厂商请求节点。

<a id="r_usbd_5Fbos_5Fdesc_5Fdata"></a>

```c
struct usbd_bos_desc_data
```

相关声明：[usbd_bos_desc_data](../usb/P020_USBBOS能力描述符数据.md)。

USB设备（USBD）的BOS设备能力描述符数据。

<a id="r_usbd_5Fdesc_5Fnode"></a>

```c
struct usbd_desc_node
```

相关声明：[usbd_desc_node](../usb/P021_USB描述符节点.md)。

描述符节点（Descriptor Node）。

<a id="r_usbd_5Fconfig_5Fnode"></a>

```c
struct usbd_config_node
```

相关声明：[usbd_config_node](../usb/P022_USB配置节点.md)。

设备配置节点（Device Configuration Node）。

<a id="r_usbd_5Fch9_5Fdata"></a>

```c
struct usbd_ch9_data
```

相关声明：[usbd_ch9_data](../usb/P023_USB第9章运行时数据.md)。

USB设备支持中间层（Middle Layer）的运行时数据。

<a id="r_usbd_5Fstatus"></a>

```c
struct usbd_status
```

相关声明：[usbd_status](../usb/P024_USB设备状态结构.md)。

USB设备支持状态（Support Status）。

<a id="r_usbd_5Fcontext"></a>

```c
struct usbd_context
```

相关声明：[usbd_context](../usb/P025_USB设备上下文结构.md)。

USB设备支持的运行时上下文（Runtime Context）。

<a id="r_usbd_5Fcctx_5Fvendor_5Freq"></a>

```c
struct usbd_cctx_vendor_req
```

相关声明：[usbd_cctx_vendor_req](../usb/P026_USB类厂商请求表.md)。

厂商请求表（Vendor Requests Table）。

<a id="r_usbd_5Fclass_5Fapi"></a>

```c
struct usbd_class_api
```

相关声明：[usbd_class_api](../usb/P027_USB类回调接口.md)。

USB设备支持的类实例（Class Instance）API。

<a id="r_usbd_5Fclass_5Fdata"></a>

```c
struct usbd_class_data
```

相关声明：[usbd_class_data](../usb/P028_USB类数据结构.md)。

USB设备支持的类数据（Class Data）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.2\_宏定义（Macros）

<a id="r_ga3f675bab13e089ab9576b29a6bb52364"></a>

```c
#define USBD_SUPPORTS_HIGH_SPEED IS_EQ(CONFIG_USBD_MAX_SPEED, 1)
```

相关声明：[USBD_SUPPORTS_HIGH_SPEED](../usb/P015_USB设备核心API.md#ga3f675bab13e089ab9576b29a6bb52364)、[IS_EQ](../util_reference/P001_通用工具公共接口.md#gaa35a6894bca38a8ffb558c2c22a1eee1)。

<a id="r_gae5b1ba785fb89b129096c255b4084da1"></a>

```c
#define USBD_MAX_BULK_MPS COND_CODE_1(USBD_SUPPORTS_HIGH_SPEED, (512), (64))
```

相关声明：[USBD_MAX_BULK_MPS](../usb/P015_USB设备核心API.md#gae5b1ba785fb89b129096c255b4084da1)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)、[USBD_SUPPORTS_HIGH_SPEED](../usb/P015_USB设备核心API.md#ga3f675bab13e089ab9576b29a6bb52364)。

<a id="r_gaef85e50556291fa93cbf72b01529b4a8"></a>

```c
#define USB_STRING_DESCRIPTOR_LENGTH(s)
```

相关声明：[USB_STRING_DESCRIPTOR_LENGTH](../usb/P015_USB设备核心API.md#gaef85e50556291fa93cbf72b01529b4a8)。

<a id="r_gaf8aadd499f7e0438acac4a7f36645d49"></a>

```c
#define USBD_NUMOF_INTERFACES_MAX 16U
```

相关声明：[USBD_NUMOF_INTERFACES_MAX](../usb/P015_USB设备核心API.md#gaf8aadd499f7e0438acac4a7f36645d49)。

<a id="r_ga588b9e156a49d3b0358bee185cdeebee"></a>

```c
#define USBD_CCTX_REGISTERED 0
```

相关声明：[USBD_CCTX_REGISTERED](../usb/P015_USB设备核心API.md#ga588b9e156a49d3b0358bee185cdeebee)。

USB 类实例已注册标志（USB Class Instance Registered Flag）。

<a id="r_ga26777805f749f29efa882f9bf391473a"></a>

```c
#define USBD_DEVICE_DEFINE(device_name, udc_dev, vid, pid)
```

相关声明：[USBD_DEVICE_DEFINE](../usb/P015_USB设备核心API.md#ga26777805f749f29efa882f9bf391473a)。

定义 USB 设备上下文结构体（USB Device Context Structure）。

<a id="r_ga2d98fd68eff66f36522688f3de527586"></a>

```c
#define USBD_CONFIGURATION_DEFINE(name, attrib, power, desc_nd)
```

相关声明：[USBD_CONFIGURATION_DEFINE](../usb/P015_USB设备核心API.md#ga2d98fd68eff66f36522688f3de527586)。

定义 USB 设备配置（USB Device Configuration）。

<a id="r_gaec816a27118bcb289ab4840fcd22888e"></a>

```c
#define USBD_DESC_LANG_DEFINE(name)
```

相关声明：[USBD_DESC_LANG_DEFINE](../usb/P015_USB设备核心API.md#gaec816a27118bcb289ab4840fcd22888e)。

创建字符串描述符节点（String Descriptor Node）和语言字符串描述符（Language String Descriptor）。

<a id="r_gaf800e2040ac30844cab463c13d1fcdf8"></a>

```c
#define USBD_DESC_STRING_DEFINE(d_name, d_string, d_utype)
```

相关声明：[USBD_DESC_STRING_DEFINE](../usb/P015_USB设备核心API.md#gaf800e2040ac30844cab463c13d1fcdf8)。

创建字符串描述符（String Descriptor）。

<a id="r_ga18b1321daf1173a3cb0bc61a0d9beb34"></a>

```c
#define USBD_DESC_MANUFACTURER_DEFINE(d_name, d_string)
```

相关声明：[USBD_DESC_MANUFACTURER_DEFINE](../usb/P015_USB设备核心API.md#ga18b1321daf1173a3cb0bc61a0d9beb34)。

创建字符串描述符节点（String Descriptor Node）和制造商字符串描述符（Manufacturer String Descriptor）。

<a id="r_gaa5e43f9eac8f91d3896ea5e19baed031"></a>

```c
#define USBD_DESC_PRODUCT_DEFINE(d_name, d_string)
```

相关声明：[USBD_DESC_PRODUCT_DEFINE](../usb/P015_USB设备核心API.md#gaa5e43f9eac8f91d3896ea5e19baed031)。

创建字符串描述符节点（String Descriptor Node）和产品字符串描述符（Product String Descriptor）。

<a id="r_ga26af7f93205dc78eeb60a3c09aa7b2d3"></a>

```c
#define USBD_DESC_SERIAL_NUMBER_DEFINE(d_name)
```

相关声明：[USBD_DESC_SERIAL_NUMBER_DEFINE](../usb/P015_USB设备核心API.md#ga26af7f93205dc78eeb60a3c09aa7b2d3)。

创建字符串描述符节点（String Descriptor Node）和序列号字符串描述符（Serial Number String Descriptor）。

<a id="r_ga45dc8df18f6fdf72edfd21f35d3046db"></a>

```c
#define USBD_DESC_CONFIG_DEFINE(d_name, d_string)
```

相关声明：[USBD_DESC_CONFIG_DEFINE](../usb/P015_USB设备核心API.md#ga45dc8df18f6fdf72edfd21f35d3046db)。

为配置描述符（Configuration Descriptor）创建字符串描述符节点（String Descriptor Node）。

<a id="r_ga620a5aa567dc4de7d5d1ef6b0cd9e937"></a>

```c
#define USBD_DESC_BOS_DEFINE(name, len, subset)
```

相关声明：[USBD_DESC_BOS_DEFINE](../usb/P015_USB设备核心API.md#ga620a5aa567dc4de7d5d1ef6b0cd9e937)。

定义 BOS 设备能力描述符节点（BOS Device Capability Descriptor Node）。

<a id="r_ga0bdfa97d67ee62aa32af5fad2670a8a0"></a>

```c
#define USBD_VREQUEST_DEFINE(name, vcode, vto_host, vto_dev)
```

相关声明：[USBD_VREQUEST_DEFINE](../usb/P015_USB设备核心API.md#ga0bdfa97d67ee62aa32af5fad2670a8a0)。

定义接收方为设备（Recipient Device）的厂商请求（Vendor Request）。

<a id="r_ga0481d759856a0dc4b937335e8768eedd"></a>

```c
#define USBD_DESC_BOS_VREQ_DEFINE(name, len, subset, vcode, vto_host, vto_dev)
```

相关声明：[USBD_DESC_BOS_VREQ_DEFINE](../usb/P015_USB设备核心API.md#ga0481d759856a0dc4b937335e8768eedd)。

定义带厂商请求（Vendor Request）的 BOS 设备能力描述符节点（BOS Device Capability Descriptor Node）。

<a id="r_gaaebebc77106848d8d62016936399776a"></a>

```c
#define USBD_DEFINE_CLASS(class_name, class_api, class_priv, class_v_reqs)
```

相关声明：[USBD_DEFINE_CLASS](../usb/P015_USB设备核心API.md#gaaebebc77106848d8d62016936399776a)。

定义 USB 设备支持的类数据（USB Device Support Class Data）。

<a id="r_ga54ca08c74ae715281381d878f828727e"></a>

```c
#define VENDOR_REQ_DEFINE(_reqs, _len)
```

相关声明：[VENDOR_REQ_DEFINE](../usb/P015_USB设备核心API.md#ga54ca08c74ae715281381d878f828727e)。

用于声明 `usbd_cctx_vendor_req` 请求表（Request Table）的辅助宏。

<a id="r_ga464933a8332c11d15c92914aa1790e10"></a>

```c
#define USBD_VENDOR_REQ(_reqs...)
```

相关声明：[USBD_VENDOR_REQ](../usb/P015_USB设备核心API.md#ga464933a8332c11d15c92914aa1790e10)。

用于声明所支持的厂商请求（Vendor Request）的辅助宏。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 17.3\_类型定义（Typedefs）

<a id="r_ga2cd074cefff922b0816de37935d9646e"></a>

```c
typedef void(* usbd_msg_cb_t) (struct usbd_context *const ctx, const struct usbd_msg *const msg)
```

相关声明：[usbd_msg_cb_t](../usb/P015_USB设备核心API.md#ga2cd074cefff922b0816de37935d9646e)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_msg](../usb/P017_USB设备消息结构.md)。

USB 设备消息传递（USB Device Message Delivery）的回调类型定义（Callback Type Definition）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.4\_枚举（Enumerations）

<a id="r_ga95fb708d8a54eaa3ce0acc4e65519bbc"></a>

```c
enum usbd_ch9_state { USBD_STATE_DEFAULT = 0 , USBD_STATE_ADDRESS , USBD_STATE_CONFIGURED }
```

相关声明：[usbd_ch9_state](../usb/P015_USB设备核心API.md#ga95fb708d8a54eaa3ce0acc4e65519bbc)、[USBD_STATE_DEFAULT](../usb/P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048)、[USBD_STATE_ADDRESS](../usb/P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d)、[USBD_STATE_CONFIGURED](../usb/P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509)。

USB 设备支持中间层的运行时状态（Middle Layer Runtime State）。

<a id="r_ga2f2da3d634530f08cd59d408c811ad71"></a>

```c
enum usbd_speed { USBD_SPEED_FS , USBD_SPEED_HS , USBD_SPEED_SS }
```

相关声明：[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[USBD_SPEED_FS](../usb/P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7)、[USBD_SPEED_HS](../usb/P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266)、[USBD_SPEED_SS](../usb/P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a)。

USB 设备速度（USB Device Speed）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.5\_函数（Functions）

<a id="r_gaf97c68e75420bd5a1085c047577fd5a7"></a>

```c
static struct usbd_context * usbd_class_get_ctx (const struct usbd_class_data *const c_data)
```

相关声明：[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_class_get_ctx](../usb/P015_USB设备核心API.md#gaf97c68e75420bd5a1085c047577fd5a7)、[usbd_class_data](../usb/P028_USB类数据结构.md)。

获取该类所注册于的 USB 设备运行时上下文（USB Device Runtime Context）。

<a id="r_ga2e511d0341b4e1bd57fb4420512eeeb5"></a>

```c
static void * usbd_class_get_private (const struct usbd_class_data *const c_data)
```

相关声明：[usbd_class_get_private](../usb/P015_USB设备核心API.md#ga2e511d0341b4e1bd57fb4420512eeeb5)、[usbd_class_data](../usb/P028_USB类数据结构.md)。

获取类实现私有数据（Class Implementation Private Data）。

<a id="r_ga33d0cef23d4b6c62b79b41559427b584"></a>

```c
int usbd_add_descriptor (struct usbd_context *uds_ctx, struct usbd_desc_node *dn)
```

相关声明：[usbd_add_descriptor](../usb/P015_USB设备核心API.md#ga33d0cef23d4b6c62b79b41559427b584)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_desc_node](../usb/P021_USB描述符节点.md)。

添加通用 USB 描述符（Common USB Descriptor）。

<a id="r_gab023ab276eb68c644895483344d33948"></a>

```c
uint8_t usbd_str_desc_get_idx (const struct usbd_desc_node *const desc_nd)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usbd_str_desc_get_idx](../usb/P015_USB设备核心API.md#gab023ab276eb68c644895483344d33948)、[usbd_desc_node](../usb/P021_USB描述符节点.md)。

从描述符节点（Descriptor Node）获取 USB 字符串描述符索引（USB String Descriptor Index）。

<a id="r_ga3146ee636b84c6d319365716f5741363"></a>

```c
void usbd_remove_descriptor (struct usbd_desc_node *const desc_nd)
```

相关声明：[usbd_remove_descriptor](../usb/P015_USB设备核心API.md#ga3146ee636b84c6d319365716f5741363)、[usbd_desc_node](../usb/P021_USB描述符节点.md)。

移除 USB 字符串描述符（USB String Descriptor）。

<a id="r_ga5f4b69609f9a8f00a9e0fea4dffce1c4"></a>

```c
int usbd_add_configuration (struct usbd_context *uds_ctx, const enum usbd_speed speed, struct usbd_config_node *cd)
```

相关声明：[usbd_add_configuration](../usb/P015_USB设备核心API.md#ga5f4b69609f9a8f00a9e0fea4dffce1c4)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[usbd_config_node](../usb/P022_USB配置节点.md)。

添加 USB 设备配置（USB Device Configuration）。

<a id="r_ga4a837040e9d02c5773d69a6cf6c35960"></a>

```c
int usbd_register_class (struct usbd_context *uds_ctx, const char *name, const enum usbd_speed speed, uint8_t cfg)
```

相关声明：[usbd_register_class](../usb/P015_USB设备核心API.md#ga4a837040e9d02c5773d69a6cf6c35960)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

注册 USB 类实例（USB Class Instance）。

<a id="r_ga06541b17f5afc917cc5154bd4d816ec3"></a>

```c
int usbd_register_all_classes (struct usbd_context *uds_ctx, const enum usbd_speed speed, uint8_t cfg, const char *const blocklist[])
```

相关声明：[usbd_register_all_classes](../usb/P015_USB设备核心API.md#ga06541b17f5afc917cc5154bd4d816ec3)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

注册全部可用的 USB 类实例（USB Class Instance）。

<a id="r_ga1ae7a7a04f4ec1206d352d5c6401c51b"></a>

```c
int usbd_unregister_class (struct usbd_context *uds_ctx, const char *name, const enum usbd_speed speed, uint8_t cfg)
```

相关声明：[usbd_unregister_class](../usb/P015_USB设备核心API.md#ga1ae7a7a04f4ec1206d352d5c6401c51b)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

注销 USB 类实例（USB Class Instance）。

<a id="r_ga2996b5f6df459c8a179fc6c22f944063"></a>

```c
int usbd_unregister_all_classes (struct usbd_context *uds_ctx, const enum usbd_speed speed, uint8_t cfg)
```

相关声明：[usbd_unregister_all_classes](../usb/P015_USB设备核心API.md#ga2996b5f6df459c8a179fc6c22f944063)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

注销全部可用的 USB 类实例（USB Class Instance）。

<a id="r_ga2ebe08b8bf5ff3b64c4df1fcb346cf38"></a>

```c
int usbd_msg_register_cb (struct usbd_context *const uds_ctx, const usbd_msg_cb_t cb)
```

相关声明：[usbd_msg_register_cb](../usb/P015_USB设备核心API.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_msg_cb_t](../usb/P015_USB设备核心API.md#ga2cd074cefff922b0816de37935d9646e)。

注册 USB 通知消息回调（USB Notification Message Callback）。

<a id="r_ga78e5f07af641f9610cc32255efe1680f"></a>

```c
int usbd_init (struct usbd_context *uds_ctx)
```

相关声明：[usbd_init](../usb/P015_USB设备核心API.md#ga78e5f07af641f9610cc32255efe1680f)、[usbd_context](../usb/P025_USB设备上下文结构.md)。

初始化 USB 设备（USB Device）。

<a id="r_ga1a40fc13129e9218ca63ab3ca70d8d68"></a>

```c
int usbd_enable (struct usbd_context *uds_ctx)
```

相关声明：[usbd_enable](../usb/P015_USB设备核心API.md#ga1a40fc13129e9218ca63ab3ca70d8d68)、[usbd_context](../usb/P025_USB设备上下文结构.md)。

启用 USB 设备支持（USB Device Support）及已注册的类实例（Class Instance）。

<a id="r_gaaa21e9f33175b7d2434e54e1b3d2799b"></a>

```c
int usbd_disable (struct usbd_context *uds_ctx)
```

相关声明：[usbd_disable](../usb/P015_USB设备核心API.md#gaaa21e9f33175b7d2434e54e1b3d2799b)、[usbd_context](../usb/P025_USB设备上下文结构.md)。

禁用 USB 设备支持（USB Device Support）。

<a id="r_ga37585e0124a4d0d8cf6e65f13325eaf0"></a>

```c
int usbd_shutdown (struct usbd_context *const uds_ctx)
```

相关声明：[usbd_shutdown](../usb/P015_USB设备核心API.md#ga37585e0124a4d0d8cf6e65f13325eaf0)、[usbd_context](../usb/P025_USB设备上下文结构.md)。

关闭 USB 设备支持（USB Device Support）。

<a id="r_ga176f42b2dd221c0de28ad9122a7d2693"></a>

```c
int usbd_ep_set_halt (struct usbd_context *uds_ctx, uint8_t ep)
```

相关声明：[usbd_ep_set_halt](../usb/P015_USB设备核心API.md#ga176f42b2dd221c0de28ad9122a7d2693)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使端点进入停滞状态（Halt Endpoint）。

<a id="r_ga03729a4e9add3a55a7c3c2c8666a53a7"></a>

```c
int usbd_ep_clear_halt (struct usbd_context *uds_ctx, uint8_t ep)
```

相关声明：[usbd_ep_clear_halt](../usb/P015_USB设备核心API.md#ga03729a4e9add3a55a7c3c2c8666a53a7)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

清除端点停滞（Endpoint Halt）。

<a id="r_ga94cb8465b7bf85457f29e84b5b8ddfe9"></a>

```c
bool usbd_ep_is_halted (struct usbd_context *uds_ctx, uint8_t ep)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[usbd_ep_is_halted](../usb/P015_USB设备核心API.md#ga94cb8465b7bf85457f29e84b5b8ddfe9)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查端点是否处于停滞状态（Endpoint Halted）。

<a id="r_ga6c671d49c811b0af6b809f5940cd6d70"></a>

```c
struct net_buf * usbd_ep_buf_alloc (const struct usbd_class_data *const c_data, const uint8_t ep, const size_t size)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[usbd_ep_buf_alloc](../usb/P015_USB设备核心API.md#ga6c671d49c811b0af6b809f5940cd6d70)、[usbd_class_data](../usb/P028_USB类数据结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为 USB 设备请求（USB Device Request）分配缓冲区（Buffer）。

<a id="r_ga1ce934ca354853ec9c7c295cca2d0e3d"></a>

```c
struct net_buf * usbd_ep_ctrl_data_in_alloc (const struct usbd_context *const uds_ctx, const size_t size)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[usbd_ep_ctrl_data_in_alloc](../usb/P015_USB设备核心API.md#ga1ce934ca354853ec9c7c295cca2d0e3d)、[usbd_context](../usb/P025_USB设备上下文结构.md)。

为 USB 控制传输的数据阶段（Control Transfer Data Stage）分配缓冲区。

<a id="r_ga967d507d82d912119a732fd230bd561e"></a>

```c
int usbd_ep_ctrl_enqueue (struct usbd_context *const uds_ctx, struct net_buf *const buf)
```

相关声明：[usbd_ep_ctrl_enqueue](../usb/P015_USB设备核心API.md#ga967d507d82d912119a732fd230bd561e)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将 USB 设备控制请求（USB Device Control Request）加入队列。

<a id="r_gaabf8333a7aefc4428f38e79a7264e383"></a>

```c
int usbd_ep_enqueue (const struct usbd_class_data *const c_data, struct net_buf *const buf)
```

相关声明：[usbd_ep_enqueue](../usb/P015_USB设备核心API.md#gaabf8333a7aefc4428f38e79a7264e383)、[usbd_class_data](../usb/P028_USB类数据结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将 USB 设备请求（USB Device Request）加入队列。

<a id="r_ga1534058a609794e1d080aed98fcf5823"></a>

```c
int usbd_ep_dequeue (struct usbd_context *uds_ctx, const uint8_t ep)
```

相关声明：[usbd_ep_dequeue](../usb/P015_USB设备核心API.md#ga1534058a609794e1d080aed98fcf5823)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从端点队列（Endpoint Queue）移除全部 USB 设备控制器请求（USB Device Controller Request）。

<a id="r_ga8aa454c24495f2a462eae53b78c488dc"></a>

```c
int usbd_ep_buf_free (struct usbd_context *uds_ctx, struct net_buf *buf)
```

相关声明：[usbd_ep_buf_free](../usb/P015_USB设备核心API.md#ga8aa454c24495f2a462eae53b78c488dc)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

释放 USB 设备请求缓冲区（USB Device Request Buffer）。

<a id="r_ga5f7a5af958f7de8893e04ff2b7748c7e"></a>

```c
bool usbd_is_suspended (struct usbd_context *uds_ctx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[usbd_is_suspended](../usb/P015_USB设备核心API.md#ga5f7a5af958f7de8893e04ff2b7748c7e)、[usbd_context](../usb/P025_USB设备上下文结构.md)。

检查 USB 设备控制器是否已挂起（Suspended）。

<a id="r_ga34086553e74795ffdc000349e61a3c8b"></a>

```c
int usbd_wakeup_request (struct usbd_context *uds_ctx)
```

相关声明：[usbd_wakeup_request](../usb/P015_USB设备核心API.md#ga34086553e74795ffdc000349e61a3c8b)、[usbd_context](../usb/P025_USB设备上下文结构.md)。

启动 USB 远程唤醒（USB Remote Wakeup），待定（TBD）。

<a id="r_ga9056e1f01b64ddd26db6a5ee45439e22"></a>

```c
void usbd_self_powered (struct usbd_context *uds_ctx, const bool status)
```

相关声明：[usbd_self_powered](../usb/P015_USB设备核心API.md#ga9056e1f01b64ddd26db6a5ee45439e22)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 USB 设备的自供电状态（Self-powered Status）。

<a id="r_gab4a0d05a8f183f7479ad33ee29e8a611"></a>

```c
enum usbd_speed usbd_bus_speed (const struct usbd_context *const uds_ctx)
```

相关声明：[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[usbd_bus_speed](../usb/P015_USB设备核心API.md#gab4a0d05a8f183f7479ad33ee29e8a611)、[usbd_context](../usb/P025_USB设备上下文结构.md)。

获取设备实际速度（Actual Device Speed）。

<a id="r_gaab7c4692a30b58aa76b03b9e50460856"></a>

```c
enum usbd_speed usbd_caps_speed (const struct usbd_context *const uds_ctx)
```

相关声明：[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[usbd_caps_speed](../usb/P015_USB设备核心API.md#gaab7c4692a30b58aa76b03b9e50460856)、[usbd_context](../usb/P025_USB设备上下文结构.md)。

获取控制器支持的最高速度（Highest Speed）。

<a id="r_gacb704bd4f396887c859932b2ab6b4991"></a>

```c
int usbd_device_set_bcd_usb (struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint16_t bcd)
```

相关声明：[usbd_device_set_bcd_usb](../usb/P015_USB设备核心API.md#gacb704bd4f396887c859932b2ab6b4991)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 USB 设备描述符（USB Device Descriptor）的 `bcdUSB` 值。

<a id="r_ga06aa9f954b6765e07494753bb4fa42d4"></a>

```c
int usbd_device_set_vid (struct usbd_context *const uds_ctx, const uint16_t vid)
```

相关声明：[usbd_device_set_vid](../usb/P015_USB设备核心API.md#ga06aa9f954b6765e07494753bb4fa42d4)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 USB 设备描述符（USB Device Descriptor）的 `idVendor` 值。

<a id="r_ga44719fc03a50c70d75ce65e1d2f77a04"></a>

```c
int usbd_device_set_pid (struct usbd_context *const uds_ctx, const uint16_t pid)
```

相关声明：[usbd_device_set_pid](../usb/P015_USB设备核心API.md#ga44719fc03a50c70d75ce65e1d2f77a04)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 USB 设备描述符（USB Device Descriptor）的 `idProduct` 值。

<a id="r_gafda88e8a71c52addbe76ebeb874a8af5"></a>

```c
int usbd_device_set_bcd_device (struct usbd_context *const uds_ctx, const uint16_t bcd)
```

相关声明：[usbd_device_set_bcd_device](../usb/P015_USB设备核心API.md#gafda88e8a71c52addbe76ebeb874a8af5)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 USB 设备描述符（USB Device Descriptor）的 `bcdDevice` 值。

<a id="r_ga83a58b50bec680513eabd3bb7075b511"></a>

```c
int usbd_device_set_code_triple (struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t base_class, const uint8_t subclass, const uint8_t protocol)
```

相关声明：[usbd_device_set_code_triple](../usb/P015_USB设备核心API.md#ga83a58b50bec680513eabd3bb7075b511)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 USB 设备描述符（USB Device Descriptor）的三个代码：基本类（Base Class）、子类（SubClass）和协议（Protocol）。

<a id="r_ga2b803f8ac10d9375a74949cd2c2f3136"></a>

```c
int usbd_config_attrib_rwup (struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t cfg, const bool enable)
```

相关声明：[usbd_config_attrib_rwup](../usb/P015_USB设备核心API.md#ga2b803f8ac10d9375a74949cd2c2f3136)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 USB 设备配置的远程唤醒属性（Remote Wakeup）。

<a id="r_ga8b0fff68bc6ce9d8ec4a7dfd59f0eade"></a>

```c
int usbd_config_attrib_self (struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t cfg, const bool enable)
```

相关声明：[usbd_config_attrib_self](../usb/P015_USB设备核心API.md#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 USB 设备配置的自供电属性（Self-powered）。

<a id="r_ga59fc1ea6d943d26b0207bb6060e18f08"></a>

```c
int usbd_config_maxpower (struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t cfg, const uint8_t power)
```

相关声明：[usbd_config_maxpower](../usb/P015_USB设备核心API.md#ga59fc1ea6d943d26b0207bb6060e18f08)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 USB 设备配置的功耗（Power Consumption）。

<a id="r_ga5ea40d893980e24294e82d22855b407c"></a>

```c
bool usbd_can_detect_vbus (struct usbd_context *const uds_ctx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[usbd_can_detect_vbus](../usb/P015_USB设备核心API.md#ga5ea40d893980e24294e82d22855b407c)、[usbd_context](../usb/P025_USB设备上下文结构.md)。

检查控制器能否检测 VBUS 状态变化（VBUS State Change）。

<a id="r_gaaebba63d8a8b78a1f06c1a5a476cd306"></a>

```c
int usbd_device_register_vreq (struct usbd_context *const uds_ctx, struct usbd_vreq_node *const vreq_nd)
```

相关声明：[usbd_device_register_vreq](../usb/P015_USB设备核心API.md#gaaebba63d8a8b78a1f06c1a5a476cd306)、[usbd_context](../usb/P025_USB设备上下文结构.md)、[usbd_vreq_node](../usb/P019_USB厂商请求节点.md)。

注册接收方为设备（Recipient Device）的 USB 厂商请求（USB Vendor Request）。


## 17.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/usb/bos.h](../api_source_reference/P076_bos.h_源码浏览.md)
- [zephyr/usb/usb_ch9.h](../usb/P173_USB第9章头文件源码.md)
- [zephyr/usb/usbd_msg.h](../api_source_reference/P896_usbd_msg.h_源码浏览.md)
- [zephyr/drivers/usb/usb_buf.h](../api_source_runtime_reference/P066_usb_buf.h_源码浏览.md)
- [zephyr/sys/byteorder.h](../byteorder_reference/P002_系统字节序头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/logging/log.h](../log_core_reference/P004_日志公共头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_device_reference/P053_usbd.h_源码浏览.md)
- [usbd_str_desc_data](../usb/P018_USB字符串描述符数据.md)
- [usbd_vreq_node](../usb/P019_USB厂商请求节点.md)
- [usbd_bos_desc_data](../usb/P020_USBBOS能力描述符数据.md)
- [usbd_desc_node](../usb/P021_USB描述符节点.md)
- [usbd_config_node](../usb/P022_USB配置节点.md)
- [usbd_ch9_data](../usb/P023_USB第9章运行时数据.md)
- [usbd_status](../usb/P024_USB设备状态结构.md)
- [usbd_context](../usb/P025_USB设备上下文结构.md)
- [usbd_cctx_vendor_req](../usb/P026_USB类厂商请求表.md)
- [usbd_class_api](../usb/P027_USB类回调接口.md)
- [usbd_class_data](../usb/P028_USB类数据结构.md)
- [USBD_SUPPORTS_HIGH_SPEED](../usb/P015_USB设备核心API.md#ga3f675bab13e089ab9576b29a6bb52364)
- [IS_EQ](../util_reference/P001_通用工具公共接口.md#gaa35a6894bca38a8ffb558c2c22a1eee1)
- [USBD_MAX_BULK_MPS](../usb/P015_USB设备核心API.md#gae5b1ba785fb89b129096c255b4084da1)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [USB_STRING_DESCRIPTOR_LENGTH](../usb/P015_USB设备核心API.md#gaef85e50556291fa93cbf72b01529b4a8)
- [USBD_NUMOF_INTERFACES_MAX](../usb/P015_USB设备核心API.md#gaf8aadd499f7e0438acac4a7f36645d49)
- [USBD_CCTX_REGISTERED](../usb/P015_USB设备核心API.md#ga588b9e156a49d3b0358bee185cdeebee)
- [USBD_DEVICE_DEFINE](../usb/P015_USB设备核心API.md#ga26777805f749f29efa882f9bf391473a)
- [USBD_CONFIGURATION_DEFINE](../usb/P015_USB设备核心API.md#ga2d98fd68eff66f36522688f3de527586)
- [USBD_DESC_LANG_DEFINE](../usb/P015_USB设备核心API.md#gaec816a27118bcb289ab4840fcd22888e)
- [USBD_DESC_STRING_DEFINE](../usb/P015_USB设备核心API.md#gaf800e2040ac30844cab463c13d1fcdf8)
- [USBD_DESC_MANUFACTURER_DEFINE](../usb/P015_USB设备核心API.md#ga18b1321daf1173a3cb0bc61a0d9beb34)
- [USBD_DESC_PRODUCT_DEFINE](../usb/P015_USB设备核心API.md#gaa5e43f9eac8f91d3896ea5e19baed031)
- [USBD_DESC_SERIAL_NUMBER_DEFINE](../usb/P015_USB设备核心API.md#ga26af7f93205dc78eeb60a3c09aa7b2d3)
- [USBD_DESC_CONFIG_DEFINE](../usb/P015_USB设备核心API.md#ga45dc8df18f6fdf72edfd21f35d3046db)
- [USBD_DESC_BOS_DEFINE](../usb/P015_USB设备核心API.md#ga620a5aa567dc4de7d5d1ef6b0cd9e937)
- [USBD_VREQUEST_DEFINE](../usb/P015_USB设备核心API.md#ga0bdfa97d67ee62aa32af5fad2670a8a0)
- [USBD_DESC_BOS_VREQ_DEFINE](../usb/P015_USB设备核心API.md#ga0481d759856a0dc4b937335e8768eedd)
- [USBD_DEFINE_CLASS](../usb/P015_USB设备核心API.md#gaaebebc77106848d8d62016936399776a)
- [VENDOR_REQ_DEFINE](../usb/P015_USB设备核心API.md#ga54ca08c74ae715281381d878f828727e)
- [USBD_VENDOR_REQ](../usb/P015_USB设备核心API.md#ga464933a8332c11d15c92914aa1790e10)
- [usbd_msg_cb_t](../usb/P015_USB设备核心API.md#ga2cd074cefff922b0816de37935d9646e)
- [usbd_msg](../usb/P017_USB设备消息结构.md)
- [usbd_ch9_state](../usb/P015_USB设备核心API.md#ga95fb708d8a54eaa3ce0acc4e65519bbc)
- [USBD_STATE_DEFAULT](../usb/P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048)
- [USBD_STATE_ADDRESS](../usb/P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d)
- [USBD_STATE_CONFIGURED](../usb/P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509)
- [usbd_speed](../usb/P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)
- [USBD_SPEED_FS](../usb/P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7)
- [USBD_SPEED_HS](../usb/P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266)
- [USBD_SPEED_SS](../usb/P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a)
- [usbd_class_get_ctx](../usb/P015_USB设备核心API.md#gaf97c68e75420bd5a1085c047577fd5a7)
- [usbd_class_get_private](../usb/P015_USB设备核心API.md#ga2e511d0341b4e1bd57fb4420512eeeb5)
- [usbd_add_descriptor](../usb/P015_USB设备核心API.md#ga33d0cef23d4b6c62b79b41559427b584)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [usbd_str_desc_get_idx](../usb/P015_USB设备核心API.md#gab023ab276eb68c644895483344d33948)
- [usbd_remove_descriptor](../usb/P015_USB设备核心API.md#ga3146ee636b84c6d319365716f5741363)
- [usbd_add_configuration](../usb/P015_USB设备核心API.md#ga5f4b69609f9a8f00a9e0fea4dffce1c4)
- [usbd_register_class](../usb/P015_USB设备核心API.md#ga4a837040e9d02c5773d69a6cf6c35960)
- [usbd_register_all_classes](../usb/P015_USB设备核心API.md#ga06541b17f5afc917cc5154bd4d816ec3)
- [usbd_unregister_class](../usb/P015_USB设备核心API.md#ga1ae7a7a04f4ec1206d352d5c6401c51b)
- [usbd_unregister_all_classes](../usb/P015_USB设备核心API.md#ga2996b5f6df459c8a179fc6c22f944063)
- [usbd_msg_register_cb](../usb/P015_USB设备核心API.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38)
- [usbd_init](../usb/P015_USB设备核心API.md#ga78e5f07af641f9610cc32255efe1680f)
- [usbd_enable](../usb/P015_USB设备核心API.md#ga1a40fc13129e9218ca63ab3ca70d8d68)
- [usbd_disable](../usb/P015_USB设备核心API.md#gaaa21e9f33175b7d2434e54e1b3d2799b)
- [usbd_shutdown](../usb/P015_USB设备核心API.md#ga37585e0124a4d0d8cf6e65f13325eaf0)
- [usbd_ep_set_halt](../usb/P015_USB设备核心API.md#ga176f42b2dd221c0de28ad9122a7d2693)
- [usbd_ep_clear_halt](../usb/P015_USB设备核心API.md#ga03729a4e9add3a55a7c3c2c8666a53a7)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [usbd_ep_is_halted](../usb/P015_USB设备核心API.md#ga94cb8465b7bf85457f29e84b5b8ddfe9)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [usbd_ep_buf_alloc](../usb/P015_USB设备核心API.md#ga6c671d49c811b0af6b809f5940cd6d70)
- [usbd_ep_ctrl_data_in_alloc](../usb/P015_USB设备核心API.md#ga1ce934ca354853ec9c7c295cca2d0e3d)
- [usbd_ep_ctrl_enqueue](../usb/P015_USB设备核心API.md#ga967d507d82d912119a732fd230bd561e)
- [usbd_ep_enqueue](../usb/P015_USB设备核心API.md#gaabf8333a7aefc4428f38e79a7264e383)
- [usbd_ep_dequeue](../usb/P015_USB设备核心API.md#ga1534058a609794e1d080aed98fcf5823)
- [usbd_ep_buf_free](../usb/P015_USB设备核心API.md#ga8aa454c24495f2a462eae53b78c488dc)
- [usbd_is_suspended](../usb/P015_USB设备核心API.md#ga5f7a5af958f7de8893e04ff2b7748c7e)
- [usbd_wakeup_request](../usb/P015_USB设备核心API.md#ga34086553e74795ffdc000349e61a3c8b)
- [usbd_self_powered](../usb/P015_USB设备核心API.md#ga9056e1f01b64ddd26db6a5ee45439e22)
- [usbd_bus_speed](../usb/P015_USB设备核心API.md#gab4a0d05a8f183f7479ad33ee29e8a611)
- [usbd_caps_speed](../usb/P015_USB设备核心API.md#gaab7c4692a30b58aa76b03b9e50460856)
- [usbd_device_set_bcd_usb](../usb/P015_USB设备核心API.md#gacb704bd4f396887c859932b2ab6b4991)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [usbd_device_set_vid](../usb/P015_USB设备核心API.md#ga06aa9f954b6765e07494753bb4fa42d4)
- [usbd_device_set_pid](../usb/P015_USB设备核心API.md#ga44719fc03a50c70d75ce65e1d2f77a04)
- [usbd_device_set_bcd_device](../usb/P015_USB设备核心API.md#gafda88e8a71c52addbe76ebeb874a8af5)
- [usbd_device_set_code_triple](../usb/P015_USB设备核心API.md#ga83a58b50bec680513eabd3bb7075b511)
- [usbd_config_attrib_rwup](../usb/P015_USB设备核心API.md#ga2b803f8ac10d9375a74949cd2c2f3136)
- [usbd_config_attrib_self](../usb/P015_USB设备核心API.md#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade)
- [usbd_config_maxpower](../usb/P015_USB设备核心API.md#ga59fc1ea6d943d26b0207bb6060e18f08)
- [usbd_can_detect_vbus](../usb/P015_USB设备核心API.md#ga5ea40d893980e24294e82d22855b407c)
- [usbd_device_register_vreq](../usb/P015_USB设备核心API.md#gaaebba63d8a8b78a1f06c1a5a476cd306)

<a id="header-details"></a>

---

[上一章](P016_zephyr__drivers__usb_c__usbc_tc.h_文件参考.md) · [返回大纲](大纲.md)
