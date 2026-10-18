---
id: learning.zephyr-docs.usb.api-15
title: USB设备核心API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_USB设备核心API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usbd__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 15.1\_阅读说明与来源

译注：配合[USB设备支持](P002_USB设备支持.md)与[设备栈API说明](P014_USB设备栈API说明.md)阅读。这里翻译新版设备栈核心接口、通知消息及其数据结构；旧版 usb_enable() 接口另见旧版指南。函数参数、返回值和原始宏定义按保存的官方页面保留，源码差异明确标为译注。

本组：[USB设备核心API](P015_USB设备核心API.md) · [USB设备消息API](P016_USB设备消息API.md) · [USB设备消息结构](P017_USB设备消息结构.md)。

新版 USB 设备栈核心 API（Core API）。

新版 USB 设备栈核心 API。自 Zephyr 3.3 引入；接口版本为 0.2.0。

## 15.2\_数据结构（Data Structures）

<a id="r_usbd_5Fstr_5Fdesc_5Fdata"></a>

```c
struct usbd_str_desc_data
```

内部使用，用于保持描述符（Descriptor）的顺序。

相关声明：[usbd_str_desc_data](P018_USB字符串描述符数据.md)。

<a id="r_usbd_5Fvreq_5Fnode"></a>

```c
struct usbd_vreq_node
```

USBD 厂商请求节点（Vendor Request Node）。

相关声明：[usbd_vreq_node](P019_USB厂商请求节点.md)。

<a id="r_usbd_5Fbos_5Fdesc_5Fdata"></a>

```c
struct usbd_bos_desc_data
```

USBD 二进制设备对象存储（Binary Device Object Store，BOS）的设备能力描述符数据。

相关声明：[usbd_bos_desc_data](P020_USBBOS能力描述符数据.md)。

<a id="r_usbd_5Fdesc_5Fnode"></a>

```c
struct usbd_desc_node
```

描述符节点。

相关声明：[usbd_desc_node](P021_USB描述符节点.md)。

<a id="r_usbd_5Fconfig_5Fnode"></a>

```c
struct usbd_config_node
```

设备配置节点（Configuration Node）。

相关声明：[usbd_config_node](P022_USB配置节点.md)。

<a id="r_usbd_5Fch9_5Fdata"></a>

```c
struct usbd_ch9_data
```

USB 设备支持中间层的运行时数据。

相关声明：[usbd_ch9_data](P023_USB第9章运行时数据.md)。

<a id="r_usbd_5Fstatus"></a>

```c
struct usbd_status
```

USB 设备支持状态。

相关声明：[usbd_status](P024_USB设备状态结构.md)。

<a id="r_usbd_5Fcontext"></a>

```c
struct usbd_context
```

USB 设备支持的运行时上下文（Runtime Context）。

相关声明：[usbd_context](P025_USB设备上下文结构.md)。

<a id="r_usbd_5Fcctx_5Fvendor_5Freq"></a>

```c
struct usbd_cctx_vendor_req
```

厂商请求表。

相关声明：[usbd_cctx_vendor_req](P026_USB类厂商请求表.md)。

<a id="r_usbd_5Fclass_5Fapi"></a>

```c
struct usbd_class_api
```

USB 设备支持的类实例（Class Instance）API。

相关声明：[usbd_class_api](P027_USB类回调接口.md)。

<a id="r_usbd_5Fclass_5Fdata"></a>

```c
struct usbd_class_data
```

USB 设备支持的类数据。

相关声明：[usbd_class_data](P028_USB类数据结构.md)。

## 15.3\_宏定义（Macros）

<a id="r_ga3f675bab13e089ab9576b29a6bb52364"></a>

```c
#define USBD_SUPPORTS_HIGH_SPEED IS_EQ(CONFIG_USBD_MAX_SPEED, 1)
```



相关声明：[USBD_SUPPORTS_HIGH_SPEED](P015_USB设备核心API.md#ga3f675bab13e089ab9576b29a6bb52364)、[IS_EQ](../util_reference/P001_通用工具公共接口.md#gaa35a6894bca38a8ffb558c2c22a1eee1)。

<a id="r_gae5b1ba785fb89b129096c255b4084da1"></a>

```c
#define USBD_MAX_BULK_MPS COND_CODE_1(USBD_SUPPORTS_HIGH_SPEED, (512), (64))
```



相关声明：[USBD_MAX_BULK_MPS](P015_USB设备核心API.md#gae5b1ba785fb89b129096c255b4084da1)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)、[USBD_SUPPORTS_HIGH_SPEED](P015_USB设备核心API.md#ga3f675bab13e089ab9576b29a6bb52364)。

<a id="r_gaef85e50556291fa93cbf72b01529b4a8"></a>

```c
#define USB_STRING_DESCRIPTOR_LENGTH(s)
```



相关声明：[USB_STRING_DESCRIPTOR_LENGTH](P015_USB设备核心API.md#gaef85e50556291fa93cbf72b01529b4a8)。

<a id="r_gaf8aadd499f7e0438acac4a7f36645d49"></a>

```c
#define USBD_NUMOF_INTERFACES_MAX 16U
```



相关声明：[USBD_NUMOF_INTERFACES_MAX](P015_USB设备核心API.md#gaf8aadd499f7e0438acac4a7f36645d49)。

<a id="r_ga588b9e156a49d3b0358bee185cdeebee"></a>

```c
#define USBD_CCTX_REGISTERED 0
```

USB 类实例已注册标志。

相关声明：[USBD_CCTX_REGISTERED](P015_USB设备核心API.md#ga588b9e156a49d3b0358bee185cdeebee)。

<a id="r_ga26777805f749f29efa882f9bf391473a"></a>

```c
#define USBD_DEVICE_DEFINE(device_name, udc_dev, vid, pid)
```

定义 USB 设备上下文结构体。

相关声明：[USBD_DEVICE_DEFINE](P015_USB设备核心API.md#ga26777805f749f29efa882f9bf391473a)。

<a id="r_ga2d98fd68eff66f36522688f3de527586"></a>

```c
#define USBD_CONFIGURATION_DEFINE(name, attrib, power, desc_nd)
```

定义 USB 设备配置。

相关声明：[USBD_CONFIGURATION_DEFINE](P015_USB设备核心API.md#ga2d98fd68eff66f36522688f3de527586)。

<a id="r_gaec816a27118bcb289ab4840fcd22888e"></a>

```c
#define USBD_DESC_LANG_DEFINE(name)
```

创建字符串描述符节点及语言字符串描述符。

相关声明：[USBD_DESC_LANG_DEFINE](P015_USB设备核心API.md#gaec816a27118bcb289ab4840fcd22888e)。

<a id="r_gaf800e2040ac30844cab463c13d1fcdf8"></a>

```c
#define USBD_DESC_STRING_DEFINE(d_name, d_string, d_utype)
```

创建字符串描述符。

相关声明：[USBD_DESC_STRING_DEFINE](P015_USB设备核心API.md#gaf800e2040ac30844cab463c13d1fcdf8)。

<a id="r_ga18b1321daf1173a3cb0bc61a0d9beb34"></a>

```c
#define USBD_DESC_MANUFACTURER_DEFINE(d_name, d_string)
```

创建字符串描述符节点及制造商字符串描述符。

相关声明：[USBD_DESC_MANUFACTURER_DEFINE](P015_USB设备核心API.md#ga18b1321daf1173a3cb0bc61a0d9beb34)。

<a id="r_gaa5e43f9eac8f91d3896ea5e19baed031"></a>

```c
#define USBD_DESC_PRODUCT_DEFINE(d_name, d_string)
```

创建字符串描述符节点及产品字符串描述符。

相关声明：[USBD_DESC_PRODUCT_DEFINE](P015_USB设备核心API.md#gaa5e43f9eac8f91d3896ea5e19baed031)。

<a id="r_ga26af7f93205dc78eeb60a3c09aa7b2d3"></a>

```c
#define USBD_DESC_SERIAL_NUMBER_DEFINE(d_name)
```

创建字符串描述符节点及序列号字符串描述符。

相关声明：[USBD_DESC_SERIAL_NUMBER_DEFINE](P015_USB设备核心API.md#ga26af7f93205dc78eeb60a3c09aa7b2d3)。

<a id="r_ga45dc8df18f6fdf72edfd21f35d3046db"></a>

```c
#define USBD_DESC_CONFIG_DEFINE(d_name, d_string)
```

为配置描述符创建字符串描述符节点。

相关声明：[USBD_DESC_CONFIG_DEFINE](P015_USB设备核心API.md#ga45dc8df18f6fdf72edfd21f35d3046db)。

<a id="r_ga620a5aa567dc4de7d5d1ef6b0cd9e937"></a>

```c
#define USBD_DESC_BOS_DEFINE(name, len, subset)
```

定义 BOS 设备能力描述符节点。

相关声明：[USBD_DESC_BOS_DEFINE](P015_USB设备核心API.md#ga620a5aa567dc4de7d5d1ef6b0cd9e937)。

<a id="r_ga0bdfa97d67ee62aa32af5fad2670a8a0"></a>

```c
#define USBD_VREQUEST_DEFINE(name, vcode, vto_host, vto_dev)
```

定义接收方为设备的厂商请求。

相关声明：[USBD_VREQUEST_DEFINE](P015_USB设备核心API.md#ga0bdfa97d67ee62aa32af5fad2670a8a0)。

<a id="r_ga0481d759856a0dc4b937335e8768eedd"></a>

```c
#define USBD_DESC_BOS_VREQ_DEFINE(name, len, subset, vcode, vto_host, vto_dev)
```

定义带有厂商请求的 BOS 设备能力描述符节点。

相关声明：[USBD_DESC_BOS_VREQ_DEFINE](P015_USB设备核心API.md#ga0481d759856a0dc4b937335e8768eedd)。

<a id="r_gaaebebc77106848d8d62016936399776a"></a>

```c
#define USBD_DEFINE_CLASS(class_name, class_api, class_priv, class_v_reqs)
```

定义 USB 设备支持的类数据。

相关声明：[USBD_DEFINE_CLASS](P015_USB设备核心API.md#gaaebebc77106848d8d62016936399776a)。

<a id="r_ga54ca08c74ae715281381d878f828727e"></a>

```c
#define VENDOR_REQ_DEFINE(_reqs, _len)
```

用于声明 `usbd_cctx_vendor_req` 请求表的辅助宏。

相关声明：[VENDOR_REQ_DEFINE](P015_USB设备核心API.md#ga54ca08c74ae715281381d878f828727e)。

<a id="r_ga464933a8332c11d15c92914aa1790e10"></a>

```c
#define USBD_VENDOR_REQ(_reqs...)
```

用于声明所支持厂商请求的辅助宏。

相关声明：[USBD_VENDOR_REQ](P015_USB设备核心API.md#ga464933a8332c11d15c92914aa1790e10)。

## 15.4\_类型定义（Typedefs）

<a id="r_ga2cd074cefff922b0816de37935d9646e"></a>

```c
typedef void(* usbd_msg_cb_t) (struct usbd_context *const ctx, const struct usbd_msg *const msg)
```

用于投递 USB 设备消息的回调类型定义。

相关声明：[usbd_msg_cb_t](P015_USB设备核心API.md#ga2cd074cefff922b0816de37935d9646e)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_msg](P017_USB设备消息结构.md)。

## 15.5\_枚举（Enumerations）

<a id="r_ga95fb708d8a54eaa3ce0acc4e65519bbc"></a>

```c
enum usbd_ch9_state { USBD_STATE_DEFAULT = 0 , USBD_STATE_ADDRESS , USBD_STATE_CONFIGURED }
```

USB 设备支持中间层的运行时状态。

相关声明：[usbd_ch9_state](P015_USB设备核心API.md#ga95fb708d8a54eaa3ce0acc4e65519bbc)、[USBD_STATE_DEFAULT](P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048)、[USBD_STATE_ADDRESS](P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d)、[USBD_STATE_CONFIGURED](P015_USB设备核心API.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509)。

<a id="r_ga2f2da3d634530f08cd59d408c811ad71"></a>

```c
enum usbd_speed { USBD_SPEED_FS , USBD_SPEED_HS , USBD_SPEED_SS }
```

USB 设备速率（Speed）。

相关声明：[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[USBD_SPEED_FS](P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7)、[USBD_SPEED_HS](P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266)、[USBD_SPEED_SS](P015_USB设备核心API.md#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a)。

## 15.6\_函数（Functions）

<a id="r_gaf97c68e75420bd5a1085c047577fd5a7"></a>

```c
static struct usbd_context * usbd_class_get_ctx (const struct usbd_class_data *const c_data)
```

取得注册该类时所属的 USB 设备运行时上下文。

相关声明：[usbd_context](P025_USB设备上下文结构.md)、[usbd_class_get_ctx](P015_USB设备核心API.md#gaf97c68e75420bd5a1085c047577fd5a7)、[usbd_class_data](P028_USB类数据结构.md)。

<a id="r_ga2e511d0341b4e1bd57fb4420512eeeb5"></a>

```c
static void * usbd_class_get_private (const struct usbd_class_data *const c_data)
```

取得类实现的私有数据（Private Data）。

相关声明：[usbd_class_get_private](P015_USB设备核心API.md#ga2e511d0341b4e1bd57fb4420512eeeb5)、[usbd_class_data](P028_USB类数据结构.md)。

<a id="r_ga33d0cef23d4b6c62b79b41559427b584"></a>

```c
int usbd_add_descriptor (struct usbd_context *uds_ctx, struct usbd_desc_node *dn)
```

添加通用 USB 描述符。

相关声明：[usbd_add_descriptor](P015_USB设备核心API.md#ga33d0cef23d4b6c62b79b41559427b584)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_desc_node](P021_USB描述符节点.md)。

<a id="r_gab023ab276eb68c644895483344d33948"></a>

```c
uint8_t usbd_str_desc_get_idx (const struct usbd_desc_node *const desc_nd)
```

从描述符节点取得 USB 字符串描述符索引。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usbd_str_desc_get_idx](P015_USB设备核心API.md#gab023ab276eb68c644895483344d33948)、[usbd_desc_node](P021_USB描述符节点.md)。

<a id="r_ga3146ee636b84c6d319365716f5741363"></a>

```c
void usbd_remove_descriptor (struct usbd_desc_node *const desc_nd)
```

移除 USB 字符串描述符。

相关声明：[usbd_remove_descriptor](P015_USB设备核心API.md#ga3146ee636b84c6d319365716f5741363)、[usbd_desc_node](P021_USB描述符节点.md)。

<a id="r_ga5f4b69609f9a8f00a9e0fea4dffce1c4"></a>

```c
int usbd_add_configuration (struct usbd_context *uds_ctx, const enum usbd_speed speed, struct usbd_config_node *cd)
```

添加 USB 设备配置。

相关声明：[usbd_add_configuration](P015_USB设备核心API.md#ga5f4b69609f9a8f00a9e0fea4dffce1c4)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[usbd_config_node](P022_USB配置节点.md)。

<a id="r_ga4a837040e9d02c5773d69a6cf6c35960"></a>

```c
int usbd_register_class (struct usbd_context *uds_ctx, const char *name, const enum usbd_speed speed, uint8_t cfg)
```

注册一个 USB 类实例。

相关声明：[usbd_register_class](P015_USB设备核心API.md#ga4a837040e9d02c5773d69a6cf6c35960)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga06541b17f5afc917cc5154bd4d816ec3"></a>

```c
int usbd_register_all_classes (struct usbd_context *uds_ctx, const enum usbd_speed speed, uint8_t cfg, const char *const blocklist[])
```

注册所有可用的 USB 类实例。

相关声明：[usbd_register_all_classes](P015_USB设备核心API.md#ga06541b17f5afc917cc5154bd4d816ec3)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga1ae7a7a04f4ec1206d352d5c6401c51b"></a>

```c
int usbd_unregister_class (struct usbd_context *uds_ctx, const char *name, const enum usbd_speed speed, uint8_t cfg)
```

注销一个 USB 类实例。

相关声明：[usbd_unregister_class](P015_USB设备核心API.md#ga1ae7a7a04f4ec1206d352d5c6401c51b)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga2996b5f6df459c8a179fc6c22f944063"></a>

```c
int usbd_unregister_all_classes (struct usbd_context *uds_ctx, const enum usbd_speed speed, uint8_t cfg)
```

注销所有可用的 USB 类实例。

相关声明：[usbd_unregister_all_classes](P015_USB设备核心API.md#ga2996b5f6df459c8a179fc6c22f944063)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga2ebe08b8bf5ff3b64c4df1fcb346cf38"></a>

```c
int usbd_msg_register_cb (struct usbd_context *const uds_ctx, const usbd_msg_cb_t cb)
```

注册 USB 通知消息回调。

相关声明：[usbd_msg_register_cb](P015_USB设备核心API.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_msg_cb_t](P015_USB设备核心API.md#ga2cd074cefff922b0816de37935d9646e)。

<a id="r_ga78e5f07af641f9610cc32255efe1680f"></a>

```c
int usbd_init (struct usbd_context *uds_ctx)
```

初始化 USB 设备。

相关声明：[usbd_init](P015_USB设备核心API.md#ga78e5f07af641f9610cc32255efe1680f)、[usbd_context](P025_USB设备上下文结构.md)。

<a id="r_ga1a40fc13129e9218ca63ab3ca70d8d68"></a>

```c
int usbd_enable (struct usbd_context *uds_ctx)
```

启用 USB 设备支持及已注册的类实例。

相关声明：[usbd_enable](P015_USB设备核心API.md#ga1a40fc13129e9218ca63ab3ca70d8d68)、[usbd_context](P025_USB设备上下文结构.md)。

<a id="r_gaaa21e9f33175b7d2434e54e1b3d2799b"></a>

```c
int usbd_disable (struct usbd_context *uds_ctx)
```

停用 USB 设备支持。

相关声明：[usbd_disable](P015_USB设备核心API.md#gaaa21e9f33175b7d2434e54e1b3d2799b)、[usbd_context](P025_USB设备上下文结构.md)。

<a id="r_ga37585e0124a4d0d8cf6e65f13325eaf0"></a>

```c
int usbd_shutdown (struct usbd_context *const uds_ctx)
```

关闭 USB 设备支持。

相关声明：[usbd_shutdown](P015_USB设备核心API.md#ga37585e0124a4d0d8cf6e65f13325eaf0)、[usbd_context](P025_USB设备上下文结构.md)。

<a id="r_ga176f42b2dd221c0de28ad9122a7d2693"></a>

```c
int usbd_ep_set_halt (struct usbd_context *uds_ctx, uint8_t ep)
```

使端点进入停止（Halt）状态。

相关声明：[usbd_ep_set_halt](P015_USB设备核心API.md#ga176f42b2dd221c0de28ad9122a7d2693)、[usbd_context](P025_USB设备上下文结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga03729a4e9add3a55a7c3c2c8666a53a7"></a>

```c
int usbd_ep_clear_halt (struct usbd_context *uds_ctx, uint8_t ep)
```

清除端点停止状态。

相关声明：[usbd_ep_clear_halt](P015_USB设备核心API.md#ga03729a4e9add3a55a7c3c2c8666a53a7)、[usbd_context](P025_USB设备上下文结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga94cb8465b7bf85457f29e84b5b8ddfe9"></a>

```c
bool usbd_ep_is_halted (struct usbd_context *uds_ctx, uint8_t ep)
```

检查端点是否处于停止状态。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[usbd_ep_is_halted](P015_USB设备核心API.md#ga94cb8465b7bf85457f29e84b5b8ddfe9)、[usbd_context](P025_USB设备上下文结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga6c671d49c811b0af6b809f5940cd6d70"></a>

```c
struct net_buf * usbd_ep_buf_alloc (const struct usbd_class_data *const c_data, const uint8_t ep, const size_t size)
```

为 USB 设备请求分配缓冲区。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[usbd_ep_buf_alloc](P015_USB设备核心API.md#ga6c671d49c811b0af6b809f5940cd6d70)、[usbd_class_data](P028_USB类数据结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga1ce934ca354853ec9c7c295cca2d0e3d"></a>

```c
struct net_buf * usbd_ep_ctrl_data_in_alloc (const struct usbd_context *const uds_ctx, const size_t size)
```

为 USB 控制传输的数据阶段（Data Stage）分配缓冲区。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[usbd_ep_ctrl_data_in_alloc](P015_USB设备核心API.md#ga1ce934ca354853ec9c7c295cca2d0e3d)、[usbd_context](P025_USB设备上下文结构.md)。

<a id="r_ga967d507d82d912119a732fd230bd561e"></a>

```c
int usbd_ep_ctrl_enqueue (struct usbd_context *const uds_ctx, struct net_buf *const buf)
```

将 USB 设备控制请求加入队列。

相关声明：[usbd_ep_ctrl_enqueue](P015_USB设备核心API.md#ga967d507d82d912119a732fd230bd561e)、[usbd_context](P025_USB设备上下文结构.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_gaabf8333a7aefc4428f38e79a7264e383"></a>

```c
int usbd_ep_enqueue (const struct usbd_class_data *const c_data, struct net_buf *const buf)
```

将 USB 设备请求加入队列。

相关声明：[usbd_ep_enqueue](P015_USB设备核心API.md#gaabf8333a7aefc4428f38e79a7264e383)、[usbd_class_data](P028_USB类数据结构.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_ga1534058a609794e1d080aed98fcf5823"></a>

```c
int usbd_ep_dequeue (struct usbd_context *uds_ctx, const uint8_t ep)
```

从端点队列中移除所有 USB 设备控制器请求。

相关声明：[usbd_ep_dequeue](P015_USB设备核心API.md#ga1534058a609794e1d080aed98fcf5823)、[usbd_context](P025_USB设备上下文结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga8aa454c24495f2a462eae53b78c488dc"></a>

```c
int usbd_ep_buf_free (struct usbd_context *uds_ctx, struct net_buf *buf)
```

释放 USB 设备请求缓冲区。

相关声明：[usbd_ep_buf_free](P015_USB设备核心API.md#ga8aa454c24495f2a462eae53b78c488dc)、[usbd_context](P025_USB设备上下文结构.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_ga5f7a5af958f7de8893e04ff2b7748c7e"></a>

```c
bool usbd_is_suspended (struct usbd_context *uds_ctx)
```

检查 USB 设备控制器是否处于挂起（Suspended）状态。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[usbd_is_suspended](P015_USB设备核心API.md#ga5f7a5af958f7de8893e04ff2b7748c7e)、[usbd_context](P025_USB设备上下文结构.md)。

<a id="r_ga34086553e74795ffdc000349e61a3c8b"></a>

```c
int usbd_wakeup_request (struct usbd_context *uds_ctx)
```

发起 USB 远程唤醒（Remote Wakeup，原文标记 TBD，待定）。

相关声明：[usbd_wakeup_request](P015_USB设备核心API.md#ga34086553e74795ffdc000349e61a3c8b)、[usbd_context](P025_USB设备上下文结构.md)。

<a id="r_ga9056e1f01b64ddd26db6a5ee45439e22"></a>

```c
void usbd_self_powered (struct usbd_context *uds_ctx, const bool status)
```

设置 USB 设备的自供电（Self-powered）状态。

相关声明：[usbd_self_powered](P015_USB设备核心API.md#ga9056e1f01b64ddd26db6a5ee45439e22)、[usbd_context](P025_USB设备上下文结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

<a id="r_gab4a0d05a8f183f7479ad33ee29e8a611"></a>

```c
enum usbd_speed usbd_bus_speed (const struct usbd_context *const uds_ctx)
```

取得设备实际速率。

相关声明：[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[usbd_bus_speed](P015_USB设备核心API.md#gab4a0d05a8f183f7479ad33ee29e8a611)、[usbd_context](P025_USB设备上下文结构.md)。

<a id="r_gaab7c4692a30b58aa76b03b9e50460856"></a>

```c
enum usbd_speed usbd_caps_speed (const struct usbd_context *const uds_ctx)
```

取得控制器支持的最高速率。

相关声明：[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[usbd_caps_speed](P015_USB设备核心API.md#gaab7c4692a30b58aa76b03b9e50460856)、[usbd_context](P025_USB设备上下文结构.md)。

<a id="r_gacb704bd4f396887c859932b2ab6b4991"></a>

```c
int usbd_device_set_bcd_usb (struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint16_t bcd)
```

设置 USB 设备描述符的 `bcdUSB` 值。

相关声明：[usbd_device_set_bcd_usb](P015_USB设备核心API.md#gacb704bd4f396887c859932b2ab6b4991)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_ga06aa9f954b6765e07494753bb4fa42d4"></a>

```c
int usbd_device_set_vid (struct usbd_context *const uds_ctx, const uint16_t vid)
```

设置 USB 设备描述符的 `idVendor` 值。

相关声明：[usbd_device_set_vid](P015_USB设备核心API.md#ga06aa9f954b6765e07494753bb4fa42d4)、[usbd_context](P025_USB设备上下文结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_ga44719fc03a50c70d75ce65e1d2f77a04"></a>

```c
int usbd_device_set_pid (struct usbd_context *const uds_ctx, const uint16_t pid)
```

设置 USB 设备描述符的 `idProduct` 值。

相关声明：[usbd_device_set_pid](P015_USB设备核心API.md#ga44719fc03a50c70d75ce65e1d2f77a04)、[usbd_context](P025_USB设备上下文结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_gafda88e8a71c52addbe76ebeb874a8af5"></a>

```c
int usbd_device_set_bcd_device (struct usbd_context *const uds_ctx, const uint16_t bcd)
```

设置 USB 设备描述符的 `bcdDevice` 值。

相关声明：[usbd_device_set_bcd_device](P015_USB设备核心API.md#gafda88e8a71c52addbe76ebeb874a8af5)、[usbd_context](P025_USB设备上下文结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_ga83a58b50bec680513eabd3bb7075b511"></a>

```c
int usbd_device_set_code_triple (struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t base_class, const uint8_t subclass, const uint8_t protocol)
```

设置 USB 设备描述符的类别三元组：基类（Base Class）、子类（SubClass）和协议（Protocol）。

相关声明：[usbd_device_set_code_triple](P015_USB设备核心API.md#ga83a58b50bec680513eabd3bb7075b511)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga2b803f8ac10d9375a74949cd2c2f3136"></a>

```c
int usbd_config_attrib_rwup (struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t cfg, const bool enable)
```

设置 USB 设备配置的远程唤醒属性。

相关声明：[usbd_config_attrib_rwup](P015_USB设备核心API.md#ga2b803f8ac10d9375a74949cd2c2f3136)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

<a id="r_ga8b0fff68bc6ce9d8ec4a7dfd59f0eade"></a>

```c
int usbd_config_attrib_self (struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t cfg, const bool enable)
```

设置 USB 设备配置的自供电属性。

相关声明：[usbd_config_attrib_self](P015_USB设备核心API.md#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

<a id="r_ga59fc1ea6d943d26b0207bb6060e18f08"></a>

```c
int usbd_config_maxpower (struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t cfg, const uint8_t power)
```

设置 USB 设备配置的功耗声明。

相关声明：[usbd_config_maxpower](P015_USB设备核心API.md#ga59fc1ea6d943d26b0207bb6060e18f08)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga5ea40d893980e24294e82d22855b407c"></a>

```c
bool usbd_can_detect_vbus (struct usbd_context *const uds_ctx)
```

检查控制器是否能检测 VBUS 状态变化。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[usbd_can_detect_vbus](P015_USB设备核心API.md#ga5ea40d893980e24294e82d22855b407c)、[usbd_context](P025_USB设备上下文结构.md)。

<a id="r_gaaebba63d8a8b78a1f06c1a5a476cd306"></a>

```c
int usbd_device_register_vreq (struct usbd_context *const uds_ctx, struct usbd_vreq_node *const vreq_nd)
```

注册接收方为设备的 USB 厂商请求。

相关声明：[usbd_device_register_vreq](P015_USB设备核心API.md#gaaebba63d8a8b78a1f06c1a5a476cd306)、[usbd_context](P025_USB设备上下文结构.md)、[usbd_vreq_node](P019_USB厂商请求节点.md)。

## 15.7\_详细说明（Detailed Documentation）

<a id="gaef85e50556291fa93cbf72b01529b4a8"></a>

### `USB_STRING_DESCRIPTOR_LENGTH`

```c
#define USB_STRING_DESCRIPTOR_LENGTH ( s)
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
(sizeof(s) * 2)
```

<a id="ga588b9e156a49d3b0358bee185cdeebee"></a>

### `USBD_CCTX_REGISTERED`

```c
#define USBD_CCTX_REGISTERED 0
```

```c
#include <zephyr/usb/usbd.h>
```

USB 类实例已注册标志。

<a id="ga2d98fd68eff66f36522688f3de527586"></a>

### `USBD_CONFIGURATION_DEFINE`

```c
#define USBD_CONFIGURATION_DEFINE ( name, attrib, power, desc_nd )
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
static struct usb_cfg_descriptor                                \
cfg_desc_##name = {                                             \
        .bLength = sizeof(struct usb_cfg_descriptor),           \
        .bDescriptorType = USB_DESC_CONFIGURATION,              \
        .wTotalLength = 0,                                      \
        .bNumInterfaces = 0,                                    \
        .bConfigurationValue = 1,                               \
        .iConfiguration = 0,                                    \
        .bmAttributes = USB_SCD_RESERVED | (attrib),            \
        .bMaxPower = (power),                                   \
};                                                              \
BUILD_ASSERT((power) < 256, "Too much power");                  \
static struct usbd_config_node name = {                         \
        .desc = &cfg_desc_##name,                               \
        .str_desc_nd = desc_nd,                                 \
}
```

定义 USB 设备配置。

USB 设备的每种受支持速率至少需要一个配置实例。`attrib` 根据该配置下设备应具备的特征，由 `USB_SCD_SELF_POWERED`、`USB_SCD_REMOTE_WAKEUP` 组合而成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 配置名称。 |
| `attrib` | 配置特征，也可用 `usbd_config_attrib_rwup()` 和 `usbd_config_attrib_self()` 更新这些属性。 |
| `power` | `bMaxPower` 值，单位为 2 mA；也可用 `usbd_config_maxpower()` 设置。 |
| `desc_nd` | 用于描述该配置的字符串描述符节点地址，参见 `USBD_DESC_CONFIG_DEFINE()`。字符串描述符可选，此参数可以为 `NULL`。 |

<a id="gaaebebc77106848d8d62016936399776a"></a>

### `USBD_DEFINE_CLASS`

```c
#define USBD_DEFINE_CLASS ( class_name, class_api, class_priv, class_v_reqs )
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
static struct usbd_class_data class_name = {                            \
        .name = STRINGIFY(class_name),                                  \
        .api = class_api,                                               \
        .v_reqs = class_v_reqs,                                         \
        .priv = class_priv,                                             \
};                                                                      \
static STRUCT_SECTION_ITERABLE_ALTERNATE(                               \
        usbd_class_fs, usbd_class_node, class_name##_fs) = {            \
        .c_data = &class_name,                                          \
};                                                                      \
IF_ENABLED(USBD_SUPPORTS_HIGH_SPEED, (                                  \
static STRUCT_SECTION_ITERABLE_ALTERNATE(                               \
        usbd_class_hs, usbd_class_node, class_name##_hs) = {            \
        .c_data = &class_name,                                          \
}                                                                       \
))
```

定义 USB 设备支持的类数据。

此宏定义类（功能）数据，以及协议栈内部使用的相应节点结构。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `class_name` | 类名称。 |
| `class_api` | 指向 `struct usbd_class_api` 的指针。 |
| `class_priv` | 类私有数据。 |
| `class_v_reqs` | 指向 `struct usbd_cctx_vendor_req` 的指针。 |

<a id="ga620a5aa567dc4de7d5d1ef6b0cd9e937"></a>

### `USBD_DESC_BOS_DEFINE`

```c
#define USBD_DESC_BOS_DEFINE ( name, len, subset )
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
BUILD_ASSERT(IS_ENABLED(CONFIG_USBD_BOS_SUPPORT),                       \
             "USB device BOS support is disabled");                     \
static struct usbd_desc_node name = {                                   \
        .bos = {                                                        \
                .utype = USBD_DUT_BOS_NONE,                             \
        },                                                              \
        .ptr = subset,                                                  \
        .bLength = len,                                                 \
        .bDescriptorType = USB_DESC_BOS,                                \
}
```

定义 BOS 设备能力描述符节点。

应用为 USB 2.0 扩展描述符等描述符定义一个 BOS 能力描述符节点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 描述符节点标识符。 |
| `len` | 设备能力描述符长度。 |
| `subset` | 指向设备能力描述符的指针。 |

**注意（Note）**：需要启用 Kconfig 选项 `USBD_BOS_SUPPORT`。

<a id="ga0481d759856a0dc4b937335e8768eedd"></a>

### `USBD_DESC_BOS_VREQ_DEFINE`

```c
#define USBD_DESC_BOS_VREQ_DEFINE ( name, len, subset, vcode, vto_host, vto_dev )
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
BUILD_ASSERT(IS_ENABLED(CONFIG_USBD_BOS_SUPPORT),                       \
             "USB device BOS support is disabled");                     \
USBD_VREQUEST_DEFINE(vreq_nd_##name, vcode, vto_host, vto_dev);         \
static struct usbd_desc_node name = {                                   \
        .bos = {                                                        \
                .utype = USBD_DUT_BOS_VREQ,                             \
                .vreq_nd = &vreq_nd_##name,                             \
        },                                                              \
        .ptr = subset,                                                  \
        .bLength = len,                                                 \
        .bDescriptorType = USB_DESC_BOS,                                \
}
```

定义带有厂商请求的 BOS 设备能力描述符节点。

此宏定义一个带有厂商请求节点的 BOS 描述符，通常为平台能力（Platform Capability）描述符。

USBD_DESC_BOS_VREQ_DEFINE(bos_vreq_webusb, sizeof(bos_cap_webusb), &bos_cap_webusb, SAMPLE_WEBUSB_VENDOR_CODE, webusb_to_host_cb, NULL);

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 描述符节点标识符。 |
| `len` | 设备能力描述符长度。 |
| `subset` | 指向设备能力描述符的指针。 |
| `vcode` | 厂商请求代码。 |
| `vto_host` | 处理设备到主机方向请求的厂商回调。 |
| `vto_dev` | 处理主机到设备方向请求的厂商回调。 |

**注意（Note）**：需要启用 Kconfig 选项 `USBD_VREQ_SUPPORT` 和 `USBD_BOS_SUPPORT`。

<a id="ga45dc8df18f6fdf72edfd21f35d3046db"></a>

### `USBD_DESC_CONFIG_DEFINE`

```c
#define USBD_DESC_CONFIG_DEFINE ( d_name, d_string )
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
USBD_DESC_STRING_DEFINE(d_name, d_string, USBD_DUT_STRING_CONFIG)
```

为配置描述符创建字符串描述符节点。

此宏定义一个描述符节点，其地址可用作 `USBD_CONFIGURATION_DEFINE()` 宏的参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `d_name` | 字符串描述符节点标识符。 |
| `d_string` | 采用 ASCII7 编码的配置说明字符串字面量。 |

<a id="gaec816a27118bcb289ab4840fcd22888e"></a>

### `USBD_DESC_LANG_DEFINE`

```c
#define USBD_DESC_LANG_DEFINE ( name)
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
static const uint16_t langid_##name = sys_cpu_to_le16(0x0409);  \
static struct usbd_desc_node name = {                           \
        .str = {                                                \
                .idx = 0,                                       \
                .utype = USBD_DUT_STRING_LANG,                  \
        },                                                      \
        .ptr = &langid_##name,                                  \
        .bLength = sizeof(struct usb_string_descriptor),        \
        .bDescriptorType = USB_DESC_STRING,                     \
}
```

创建字符串描述符节点及语言字符串描述符。

此宏定义描述符节点及字符串描述符；加入设备上下文后，它会自动用作索引为零的语言字符串描述符。节点与描述符均使用静态存储类说明符（static-storage-class specifier）定义。默认且当前唯一受支持的语言 ID 为 `0x0409`，即英语（美国）。使用字符串描述符时，必须首先将此描述符加入 USB 设备上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 语言字符串描述符节点标识符。 |

<a id="ga18b1321daf1173a3cb0bc61a0d9beb34"></a>

### `USBD_DESC_MANUFACTURER_DEFINE`

```c
#define USBD_DESC_MANUFACTURER_DEFINE ( d_name, d_string )
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
USBD_DESC_STRING_DEFINE(d_name, d_string, USBD_DUT_STRING_MANUFACTURER)
```

创建字符串描述符节点及制造商字符串描述符。

此宏定义描述符节点及字符串描述符；加入设备上下文后，它会自动用作制造商字符串描述符。节点与描述符均使用静态存储类说明符定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `d_name` | 字符串描述符节点标识符。 |
| `d_string` | 采用 ASCII7 编码的制造商字符串字面量。 |

<a id="gaa5e43f9eac8f91d3896ea5e19baed031"></a>

### `USBD_DESC_PRODUCT_DEFINE`

```c
#define USBD_DESC_PRODUCT_DEFINE ( d_name, d_string )
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
USBD_DESC_STRING_DEFINE(d_name, d_string, USBD_DUT_STRING_PRODUCT)
```

创建字符串描述符节点及产品字符串描述符。

此宏定义描述符节点及字符串描述符；加入设备上下文后，它会自动用作产品字符串描述符。节点与描述符均使用静态存储类说明符定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `d_name` | 字符串描述符节点标识符。 |
| `d_string` | 采用 ASCII7 编码的产品字符串字面量。 |

<a id="ga26af7f93205dc78eeb60a3c09aa7b2d3"></a>

### `USBD_DESC_SERIAL_NUMBER_DEFINE`

```c
#define USBD_DESC_SERIAL_NUMBER_DEFINE ( d_name)
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
BUILD_ASSERT(IS_ENABLED(CONFIG_HWINFO), "HWINFO not enabled");          \
static struct usbd_desc_node d_name = {                                 \
        .str = {                                                        \
                .utype = USBD_DUT_STRING_SERIAL_NUMBER,                 \
                .ascii7 = true,                                         \
                .use_hwinfo = true,                                     \
        },                                                              \
        .bDescriptorType = USB_DESC_STRING,                             \
}
```

创建字符串描述符节点及序列号字符串描述符。

此宏定义一个描述符节点；加入设备上下文后，它会自动用作序列号字符串描述符。每当请求这个字符串描述符时，都会通过硬件信息（Hardware Info）获取有效序列号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `d_name` | 字符串描述符节点标识符。 |

**注意（Note）**：必须有可用的 HWINFO 驱动，并启用 Kconfig 选项 `HWINFO`。

<a id="gaf800e2040ac30844cab463c13d1fcdf8"></a>

### `USBD_DESC_STRING_DEFINE`

```c
#define USBD_DESC_STRING_DEFINE ( d_name, d_string, d_utype )
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
static const uint8_t ascii_##d_name[sizeof(d_string)] = d_string;       \
static struct usbd_desc_node d_name = {                                 \
        .str = {                                                        \
                .utype = d_utype,                                       \
                .ascii7 = true,                                         \
        },                                                              \
        .ptr = &ascii_##d_name,                                         \
        .bLength = USB_STRING_DESCRIPTOR_LENGTH(d_string),              \
        .bDescriptorType = USB_DESC_STRING,                             \
}
```

创建字符串描述符。

此宏定义描述符节点及字符串描述符。传入宏的字符串字面量应为 ASCII7 格式，在主机请求时转换为 UTF16LE 格式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `d_name` | 内部字符串描述符节点的标识符名称。 |
| `d_string` | 采用 ASCII7 编码的字符串字面量。 |
| `d_utype` | 字符串描述符的用途类型。 |

<a id="ga26777805f749f29efa882f9bf391473a"></a>

### `USBD_DEVICE_DEFINE`

```c
#define USBD_DEVICE_DEFINE ( device_name, udc_dev, vid, pid )
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
static struct usb_device_descriptor                             \
fs_desc_##device_name = {                                       \
        .bLength = sizeof(struct usb_device_descriptor),        \
        .bDescriptorType = USB_DESC_DEVICE,                     \
        .bcdUSB = sys_cpu_to_le16(USB_SRN_2_0),                 \
        .bDeviceClass = USB_BCC_MISCELLANEOUS,                  \
        .bDeviceSubClass = 2,                                   \
        .bDeviceProtocol = 1,                                   \
        .bMaxPacketSize0 = USB_CONTROL_EP_MPS,                  \
        .idVendor = vid,                                        \
        .idProduct = pid,                                       \
        .bcdDevice = sys_cpu_to_le16(USB_BCD_DRN),              \
        .iManufacturer = 0,                                     \
        .iProduct = 0,                                          \
        .iSerialNumber = 0,                                     \
        .bNumConfigurations = 0,                                \
};                                                              \
IF_ENABLED(USBD_SUPPORTS_HIGH_SPEED, (                          \
static struct usb_device_descriptor                             \
hs_desc_##device_name = {                                       \
        .bLength = sizeof(struct usb_device_descriptor),        \
        .bDescriptorType = USB_DESC_DEVICE,                     \
        .bcdUSB = sys_cpu_to_le16(USB_SRN_2_0),                 \
        .bDeviceClass = USB_BCC_MISCELLANEOUS,                  \
        .bDeviceSubClass = 2,                                   \
        .bDeviceProtocol = 1,                                   \
        .bMaxPacketSize0 = 64,                                  \
        .idVendor = vid,                                        \
        .idProduct = pid,                                       \
        .bcdDevice = sys_cpu_to_le16(USB_BCD_DRN),              \
        .iManufacturer = 0,                                     \
        .iProduct = 0,                                          \
        .iSerialNumber = 0,                                     \
        .bNumConfigurations = 0,                                \
};                                                              \
))                                                              \
static STRUCT_SECTION_ITERABLE(usbd_context, device_name) = {   \
        .name = STRINGIFY(device_name),                         \
        .mutex = Z_MUTEX_INITIALIZER(device_name.mutex),        \
        .dev = udc_dev,                                         \
        .fs_desc = &fs_desc_##device_name,                      \
        IF_ENABLED(USBD_SUPPORTS_HIGH_SPEED, (                  \
        .hs_desc = &hs_desc_##device_name,                      \
        ))                                                      \
}
```

定义 USB 设备上下文结构体。

此宏定义协议栈管理属性和运行时数据所需的 USB 设备结构。`vid`、`pid` 参数也可通过 `usbd_device_set_vid()` 和 `usbd_device_set_pid()` 修改。

使用示例：

```c
USBD_DEVICE_DEFINE(sample_usbd,
                   DEVICE_DT_GET(DT_NODELABEL(zephyr_udc0)),
                   YOUR_VID, YOUR_PID);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `device_name` | USB 设备上下文名称。 |
| `udc_dev` | 指向 USB 设备控制器（USB Device Controller，UDC）设备结构的指针。 |
| `vid` | 厂商标识（Vendor ID，VID）。 |
| `pid` | 产品标识（Product ID，PID）。 |

<a id="gae5b1ba785fb89b129096c255b4084da1"></a>

### `USBD_MAX_BULK_MPS`

```c
#define USBD_MAX_BULK_MPS COND_CODE_1(USBD_SUPPORTS_HIGH_SPEED, (512), (64))
```

```c
#include <zephyr/usb/usbd.h>
```

<a id="gaf8aadd499f7e0438acac4a7f36645d49"></a>

### `USBD_NUMOF_INTERFACES_MAX`

```c
#define USBD_NUMOF_INTERFACES_MAX 16U
```

```c
#include <zephyr/usb/usbd.h>
```

<a id="ga3f675bab13e089ab9576b29a6bb52364"></a>

### `USBD_SUPPORTS_HIGH_SPEED`

```c
#define USBD_SUPPORTS_HIGH_SPEED IS_EQ(CONFIG_USBD_MAX_SPEED, 1)
```

```c
#include <zephyr/usb/usbd.h>
```

<a id="ga464933a8332c11d15c92914aa1790e10"></a>

### `USBD_VENDOR_REQ`

```c
#define USBD_VENDOR_REQ ( _reqs...)
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
VENDOR_REQ_DEFINE(((const uint8_t []) { _reqs }), \
                  sizeof((const uint8_t []) { _reqs }))
```

用于声明所支持厂商请求的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_reqs` | 数量可变的厂商请求。 |

<a id="ga0bdfa97d67ee62aa32af5fad2670a8a0"></a>

### `USBD_VREQUEST_DEFINE`

```c
#define USBD_VREQUEST_DEFINE ( name, vcode, vto_host, vto_dev )
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
BUILD_ASSERT(IS_ENABLED(CONFIG_USBD_VREQ_SUPPORT),                      \
             "USB device vendor request support is disabled");          \
static struct usbd_vreq_node name = {                                   \
        .code = vcode,                                                  \
        .to_host = vto_host,                                            \
        .to_dev = vto_dev,                                              \
}
```

定义接收方为设备的厂商请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 厂商请求标识符。 |
| `vcode` | 厂商请求代码。 |
| `vto_host` | 处理设备到主机方向请求的厂商回调。 |
| `vto_dev` | 处理主机到设备方向请求的厂商回调。 |

**注意（Note）**：需要启用 Kconfig 选项 `USBD_VREQ_SUPPORT`。

<a id="ga54ca08c74ae715281381d878f828727e"></a>

### `VENDOR_REQ_DEFINE`

```c
#define VENDOR_REQ_DEFINE ( _reqs, _len )
```

```c
#include <zephyr/usb/usbd.h>
```

**宏展开值（Value）**

```c
{ \
        .reqs = (const uint8_t *)(_reqs), \
        .len = (_len), \
}
```

用于声明 `usbd_cctx_vendor_req` 请求表的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_reqs` | 指向厂商请求字段的指针。 |
| `_len` | 支持的厂商请求数量。 |

<a id="ga2cd074cefff922b0816de37935d9646e"></a>

### `usbd_msg_cb_t`

```c
typedef void(* usbd_msg_cb_t) (struct usbd_context *const ctx, const struct usbd_msg *const msg)
```

```c
#include <zephyr/usb/usbd.h>
```

用于投递 USB 设备消息的回调类型定义。

启用 Kconfig 选项 `USBD_MSG_DEFERRED_MODE` 时，回调在系统工作队列（System Workqueue）上下文中执行。通知消息存入队列，依次投递给回调。

禁用 Kconfig 选项 `USBD_MSG_DEFERRED_MODE` 时，回调在 USB 设备栈线程上下文中执行。使用者应确保回调不会阻塞或干扰设备栈处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] msg` | 指向 USB 设备消息的指针。 |

> 译注（源码核对）：无论采用哪种模式，消息指针都只应在本次回调期间使用：直接模式传入发布函数的局部对象，延迟模式在回调返回后释放消息块。若需异步继续处理，应复制所需数据。延迟发布在消息内存块分配失败时会丢弃本条消息，不能把排队说明理解为无条件可靠投递。

<a id="ga95fb708d8a54eaa3ce0acc4e65519bbc"></a>

### `usbd_ch9_state`

```c
enum usbd_ch9_state
```

```c
#include <zephyr/usb/usbd.h>
```

USB 设备支持中间层的运行时状态。

这是 USB 设备状态的一个子集，不包含挂起和供电状态，因为单独跟踪它们更合适。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USBD_STATE_DEFAULT` |  |
| `USBD_STATE_ADDRESS` |  |
| `USBD_STATE_CONFIGURED` |  |

<a id="ga2f2da3d634530f08cd59d408c811ad71"></a>

### `usbd_speed`

```c
enum usbd_speed
```

```c
#include <zephyr/usb/usbd.h>
```

USB 设备速率（Speed）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USBD_SPEED_FS` | 设备支持或已连接到全速（Full Speed）总线。 |
| `USBD_SPEED_HS` | 设备支持或已连接到高速（High Speed）总线。 |
| `USBD_SPEED_SS` | 设备支持或已连接到超高速（SuperSpeed）总线。 |

> 译注（源码核对）：枚举包含 SuperSpeed 并不证明当前控制器或协议栈已经支持它。能力应通过控制器和配置核实，不能仅由枚举名称推定。

<a id="ga5f4b69609f9a8f00a9e0fea4dffce1c4"></a>

### `usbd_add_configuration()`

```c
int usbd_add_configuration ( struct usbd_context * uds_ctx, const enum usbd_speed speed, struct usbd_config_node * cd )
```

```c
#include <zephyr/usb/usbd.h>
```

添加 USB 设备配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] speed` | 该配置运行的速率。 |
| `[in] cd` | 指向 USB 配置节点的指针。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="ga33d0cef23d4b6c62b79b41559427b584"></a>

### `usbd_add_descriptor()`

```c
int usbd_add_descriptor ( struct usbd_context * uds_ctx, struct usbd_desc_node * dn )
```

```c
#include <zephyr/usb/usbd.h>
```

添加通用 USB 描述符。

添加字符串或 BOS 设备能力等通用描述符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] dn` | 指向 USB 描述符节点的指针。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="gab4a0d05a8f183f7479ad33ee29e8a611"></a>

### `usbd_bus_speed()`

```c
enum usbd_speed usbd_bus_speed ( const struct usbd_context *const uds_ctx)
```

```c
#include <zephyr/usb/usbd.h>
```

取得设备实际速率。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向设备上下文的指针。 |

**返回（Returns）**：设备实际速率。

<a id="ga5ea40d893980e24294e82d22855b407c"></a>

### `usbd_can_detect_vbus()`

```c
bool usbd_can_detect_vbus ( struct usbd_context *const uds_ctx)
```

```c
#include <zephyr/usb/usbd.h>
```

检查控制器是否能检测 VBUS 状态变化。

通用应用可用它在 `usbd_init()` 后显式处理 VBUS 检测事件。例如，短暂延迟后再调用 `usbd_enable()`，给电源管理集成电路（Power Management Integrated Circuit，PMIC）留出检测总线的时间；也可处理必须等到检测到 VBUS 后才能调用 `usbd_enable()` 的情况。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |

**返回（Returns）**：控制器能检测 VBUS 状态变化时为 `true`，否则为 `false`。

<a id="gaab7c4692a30b58aa76b03b9e50460856"></a>

### `usbd_caps_speed()`

```c
enum usbd_speed usbd_caps_speed ( const struct usbd_context *const uds_ctx)
```

```c
#include <zephyr/usb/usbd.h>
```

取得控制器支持的最高速率。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向设备上下文的指针。 |

**返回（Returns）**：支持的最高速率。

<a id="gaf97c68e75420bd5a1085c047577fd5a7"></a>

### `usbd_class_get_ctx()`

```c
struct usbd_context * usbd_class_get_ctx ( const struct usbd_class_data *const c_data) inlinestatic
```

```c
#include <zephyr/usb/usbd.h>
```

取得注册该类时所属的 USB 设备运行时上下文。

类实现必须使用此函数，不直接访问结构体成员。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] c_data` | 指向 USB 设备类数据的指针。 |

**返回（Returns）**：指向 USB 设备运行时上下文的指针。

<a id="ga2e511d0341b4e1bd57fb4420512eeeb5"></a>

### `usbd_class_get_private()`

```c
void * usbd_class_get_private ( const struct usbd_class_data *const c_data) inlinestatic
```

```c
#include <zephyr/usb/usbd.h>
```

取得类实现的私有数据（Private Data）。

类实现必须使用此函数，不直接访问结构体成员。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] c_data` | 指向 USB 设备类数据的指针。 |

**返回（Returns）**：指向类实现私有数据的指针。

<a id="ga2b803f8ac10d9375a74949cd2c2f3136"></a>

### `usbd_config_attrib_rwup()`

```c
int usbd_config_attrib_rwup ( struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t cfg, const bool enable )
```

```c
#include <zephyr/usb/usbd.h>
```

设置 USB 设备配置的远程唤醒属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] speed` | 配置速率。 |
| `[in] cfg` | 配置编号。 |
| `[in] enable` | 为 `true` 时设置属性，否则清除。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="ga8b0fff68bc6ce9d8ec4a7dfd59f0eade"></a>

### `usbd_config_attrib_self()`

```c
int usbd_config_attrib_self ( struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t cfg, const bool enable )
```

```c
#include <zephyr/usb/usbd.h>
```

设置 USB 设备配置的自供电属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] speed` | 配置速率。 |
| `[in] cfg` | 配置编号。 |
| `[in] enable` | 为 `true` 时设置属性，否则清除。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="ga59fc1ea6d943d26b0207bb6060e18f08"></a>

### `usbd_config_maxpower()`

```c
int usbd_config_maxpower ( struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t cfg, const uint8_t power )
```

```c
#include <zephyr/usb/usbd.h>
```

设置 USB 设备配置的功耗声明。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] speed` | 配置速率。 |
| `[in] cfg` | 配置编号。 |
| `[in] power` | 最大功耗值（`bMaxPower`）。 |

**返回（Returns）**：成功为 0，失败为其他值。

> 译注（源码核对）：当前实现直接把 power 写入描述符 bMaxPower，不进行 mA 到字段值的换算。本文所述全速／高速配置按 2 mA 为单位，例如声明 100 mA 应传 50；这只是描述符中的功耗声明，不是电源调节命令。

<a id="gaaebba63d8a8b78a1f06c1a5a476cd306"></a>

### `usbd_device_register_vreq()`

```c
int usbd_device_register_vreq ( struct usbd_context *const uds_ctx, struct usbd_vreq_node *const vreq_nd )
```

```c
#include <zephyr/usb/usbd.h>
```

注册接收方为设备的 USB 厂商请求。

接收方为设备的厂商请求适用于该设备内的所有配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] vreq_nd` | 指向厂商请求节点的指针。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="gafda88e8a71c52addbe76ebeb874a8af5"></a>

### `usbd_device_set_bcd_device()`

```c
int usbd_device_set_bcd_device ( struct usbd_context *const uds_ctx, const uint16_t bcd )
```

```c
#include <zephyr/usb/usbd.h>
```

设置 USB 设备描述符的 `bcdDevice` 值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] bcd` | `bcdDevice` 值。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="gacb704bd4f396887c859932b2ab6b4991"></a>

### `usbd_device_set_bcd_usb()`

```c
int usbd_device_set_bcd_usb ( struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint16_t bcd )
```

```c
#include <zephyr/usb/usbd.h>
```

设置 USB 设备描述符的 `bcdUSB` 值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] speed` | 需要设置 `bcdUSB` 的速率。 |
| `[in] bcd` | `bcdUSB` 值。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="ga83a58b50bec680513eabd3bb7075b511"></a>

### `usbd_device_set_code_triple()`

```c
int usbd_device_set_code_triple ( struct usbd_context *const uds_ctx, const enum usbd_speed speed, const uint8_t base_class, const uint8_t subclass, const uint8_t protocol )
```

```c
#include <zephyr/usb/usbd.h>
```

设置 USB 设备描述符的类别三元组：基类（Base Class）、子类（SubClass）和协议（Protocol）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] speed` | 需要设置类别三元组的速率。 |
| `[in] base_class` | `bDeviceClass` 值。 |
| `[in] subclass` | `bDeviceSubClass` 值。 |
| `[in] protocol` | `bDeviceProtocol` 值。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="ga44719fc03a50c70d75ce65e1d2f77a04"></a>

### `usbd_device_set_pid()`

```c
int usbd_device_set_pid ( struct usbd_context *const uds_ctx, const uint16_t pid )
```

```c
#include <zephyr/usb/usbd.h>
```

设置 USB 设备描述符的 `idProduct` 值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] pid` | `idProduct` 值。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="ga06aa9f954b6765e07494753bb4fa42d4"></a>

### `usbd_device_set_vid()`

```c
int usbd_device_set_vid ( struct usbd_context *const uds_ctx, const uint16_t vid )
```

```c
#include <zephyr/usb/usbd.h>
```

设置 USB 设备描述符的 `idVendor` 值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] vid` | `idVendor` 值。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="gaaa21e9f33175b7d2434e54e1b3d2799b"></a>

### `usbd_disable()`

```c
int usbd_disable ( struct usbd_context * uds_ctx)
```

```c
#include <zephyr/usb/usbd.h>
```

停用 USB 设备支持。

此函数停用 USB 设备支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |

**返回（Returns）**：成功为 0，失败为其他值。

> 译注（源码核对）：当前实现停用控制器并清除 enabled 标志，但保留 initialized。已经停用时返回 -EALREADY；它与 usbd_shutdown() 的撤销初始化职责不同。

<a id="ga1a40fc13129e9218ca63ab3ca70d8d68"></a>

### `usbd_enable()`

```c
int usbd_enable ( struct usbd_context * uds_ctx)
```

```c
#include <zephyr/usb/usbd.h>
```

启用 USB 设备支持及已注册的类实例。

此函数启用 USB 设备支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="ga6c671d49c811b0af6b809f5940cd6d70"></a>

### `usbd_ep_buf_alloc()`

```c
struct net_buf * usbd_ep_buf_alloc ( const struct usbd_class_data *const c_data, const uint8_t ep, const size_t size )
```

```c
#include <zephyr/usb/usbd.h>
```

为 USB 设备请求分配缓冲区。

从控制器驱动的缓冲池分配一个新缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] c_data` | 指向 USB 设备类数据的指针。 |
| `[in] ep` | 端点地址。 |
| `[in] size` | 请求缓冲区大小。 |

**返回（Returns）**：指向已分配请求的指针；出错时为 `NULL`。

<a id="ga8aa454c24495f2a462eae53b78c488dc"></a>

### `usbd_ep_buf_free()`

```c
int usbd_ep_buf_free ( struct usbd_context * uds_ctx, struct net_buf * buf )
```

```c
#include <zephyr/usb/usbd.h>
```

释放 USB 设备请求缓冲区。

将缓冲区归还请求缓冲池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] buf` | 指向 UDC 请求缓冲区的指针。 |

**返回（Returns）**：成功为 0，其他所有值均应视为错误。

<a id="ga03729a4e9add3a55a7c3c2c8666a53a7"></a>

### `usbd_ep_clear_halt()`

```c
int usbd_ep_clear_halt ( struct usbd_context * uds_ctx, uint8_t ep )
```

```c
#include <zephyr/usb/usbd.h>
```

清除端点停止状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] ep` | 端点地址。 |

**返回（Returns）**：成功为 0，否则返回 `udc_ep_clear_halt()` 的错误。

<a id="ga1ce934ca354853ec9c7c295cca2d0e3d"></a>

### `usbd_ep_ctrl_data_in_alloc()`

```c
struct net_buf * usbd_ep_ctrl_data_in_alloc ( const struct usbd_context *const uds_ctx, const size_t size )
```

```c
#include <zephyr/usb/usbd.h>
```

为 USB 控制传输的数据阶段（Data Stage）分配缓冲区。

从控制器驱动的缓冲池分配一个新缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] size` | 请求缓冲区大小。 |

**返回（Returns）**：指向已分配请求的指针；出错时为 `NULL`。

<a id="ga967d507d82d912119a732fd230bd561e"></a>

### `usbd_ep_ctrl_enqueue()`

```c
int usbd_ep_ctrl_enqueue ( struct usbd_context *const uds_ctx, struct net_buf *const buf )
```

```c
#include <zephyr/usb/usbd.h>
```

将 USB 设备控制请求加入队列。

将控制请求加入队列。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] buf` | 指向 UDC 请求缓冲区的指针。 |

**返回（Returns）**：成功为 0，其他所有值均应视为错误。

<a id="ga1534058a609794e1d080aed98fcf5823"></a>

### `usbd_ep_dequeue()`

```c
int usbd_ep_dequeue ( struct usbd_context * uds_ctx, const uint8_t ep )
```

```c
#include <zephyr/usb/usbd.h>
```

从端点队列中移除所有 USB 设备控制器请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] ep` | 端点地址。 |

**返回（Returns）**：成功为 0，否则返回 `udc_ep_dequeue()` 的错误。

<a id="gaabf8333a7aefc4428f38e79a7264e383"></a>

### `usbd_ep_enqueue()`

```c
int usbd_ep_enqueue ( const struct usbd_class_data *const c_data, struct net_buf *const buf )
```

```c
#include <zephyr/usb/usbd.h>
```

将 USB 设备请求加入队列。

将请求加入队列。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] c_data` | 指向 USB 设备类数据的指针。 |
| `[in] buf` | 指向 UDC 请求缓冲区的指针。 |

**返回（Returns）**：成功为 0，否则返回 `udc_ep_enqueue()` 的错误。

<a id="ga94cb8465b7bf85457f29e84b5b8ddfe9"></a>

### `usbd_ep_is_halted()`

```c
bool usbd_ep_is_halted ( struct usbd_context * uds_ctx, uint8_t ep )
```

```c
#include <zephyr/usb/usbd.h>
```

检查端点是否处于停止状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] ep` | 端点地址。 |

**返回（Returns）**：端点已停止时为 `true`，否则为 `false`。

<a id="ga176f42b2dd221c0de28ad9122a7d2693"></a>

### `usbd_ep_set_halt()`

```c
int usbd_ep_set_halt ( struct usbd_context * uds_ctx, uint8_t ep )
```

```c
#include <zephyr/usb/usbd.h>
```

使端点进入停止（Halt）状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] ep` | 端点地址。 |

**返回（Returns）**：成功为 0，否则返回 `udc_ep_set_halt()` 的错误。

<a id="ga78e5f07af641f9610cc32255efe1680f"></a>

### `usbd_init()`

```c
int usbd_init ( struct usbd_context * uds_ctx)
```

```c
#include <zephyr/usb/usbd.h>
```

初始化 USB 设备。

初始化 USB 设备描述符和配置，并初始化 USB 设备控制器。类实例应在参与运行之前注册。不过，即使没有注册实例，协议栈仍应能初始化；此时主机会对缺少接口提出问题。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="ga5f7a5af958f7de8893e04ff2b7748c7e"></a>

### `usbd_is_suspended()`

```c
bool usbd_is_suspended ( struct usbd_context * uds_ctx)
```

```c
#include <zephyr/usb/usbd.h>
```

检查 USB 设备控制器是否处于挂起（Suspended）状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |

**返回（Returns）**：设备已挂起时为 `true`，否则为 `false`。

<a id="ga2ebe08b8bf5ff3b64c4df1fcb346cf38"></a>

### `usbd_msg_register_cb()`

```c
int usbd_msg_register_cb ( struct usbd_context *const uds_ctx, const usbd_msg_cb_t cb )
```

```c
#include <zephyr/usb/usbd.h>
```

注册 USB 通知消息回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] cb` | 指向消息回调函数的指针。 |

**返回（Returns）**：成功为 0，失败为其他值。

<a id="ga06541b17f5afc917cc5154bd4d816ec3"></a>

### `usbd_register_all_classes()`

```c
int usbd_register_all_classes ( struct usbd_context * uds_ctx, const enum usbd_speed speed, uint8_t cfg, const char *const blocklist[] )
```

```c
#include <zephyr/usb/usbd.h>
```

注册所有可用的 USB 类实例。

注册全部可用实例。与 `usbd_register_class` 类似，但不接受实例名称，而是注册所有可用实例。

有时某个功能不应注册，例如使用 USB DFU 实现时，正常设备运行期间必须排除 DFU 模式功能。为此，设备可传入下方形式的排除列表（Blocklist）作为可选参数；不需要排除列表时，参数应为 `NULL`。

```c
static const char *const blocklist[] = {
        "dfu_dfu",
        NULL,
};
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] speed` | 配置速率。 |
| `[in] cfg` | 配置值（`bConfigurationValue`）。 |
| `[in] blocklist` | 以空指针终止的字符串字面量指针数组，用作排除列表。 |

**注意（Note）**：两种方式不能混用。如果应用对任何设备、配置编号或实例调用 `usbd_register_class`，则 `usbd_register_class` 或此函数会失败。

**返回（Returns）**：成功为 0，失败为其他值。

> 译注（源码核对）：当前实现逐个调用 usbd_register_class()，遇到错误立即返回，没有自动回滚此前已经成功注册的实例。原文禁止混用两种注册方式的提醒应保留；失败不等于没有改变任何实例状态。

<a id="ga4a837040e9d02c5773d69a6cf6c35960"></a>

### `usbd_register_class()`

```c
int usbd_register_class ( struct usbd_context * uds_ctx, const char * name, const enum usbd_speed speed, uint8_t cfg )
```

```c
#include <zephyr/usb/usbd.h>
```

注册一个 USB 类实例。

一个 USB 类实现可以具有一个或多个实例，使用设备驱动 API 识别它们。设备名称以前缀标明类名，例如 CDC ACM 类实例使用 `CDC_ACM`，也可在 Shell 中方便地识别。只有 USB 设备栈处于停用状态时才能注册类实例。已注册实例会在设备栈初始化时初始化，各实例的接口描述符也会根据整个上下文进行调整。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] name` | 类实例名称。 |
| `[in] speed` | 配置速率。 |
| `[in] cfg` | 配置值（`bConfigurationValue`）。 |

**返回（Returns）**：成功为 0，失败为其他值。

> 译注（源码核对）：原文写栈处于“停用”状态；当前 usbd_class.c 实际检查 initialized 标志，已初始化时即返回 -EBUSY。应在 usbd_init() 前注册，单独调用 usbd_disable() 不会清除 initialized，不能据此直接重新注册。

<a id="ga3146ee636b84c6d319365716f5741363"></a>

### `usbd_remove_descriptor()`

```c
void usbd_remove_descriptor ( struct usbd_desc_node *const desc_nd)
```

```c
#include <zephyr/usb/usbd.h>
```

移除 USB 字符串描述符。

从任意链表中移除已链接的 USB 字符串描述符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] desc_nd` | 指向 USB 描述符节点的指针。 |

<a id="ga9056e1f01b64ddd26db6a5ee45439e22"></a>

### `usbd_self_powered()`

```c
void usbd_self_powered ( struct usbd_context * uds_ctx, const bool status )
```

```c
#include <zephyr/usb/usbd.h>
```

设置 USB 设备的自供电（Self-powered）状态。

这个状态用于 Get Status 请求响应中的 Self Powered 字段，表示设备当前是否自供电。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向设备上下文的指针。 |
| `[in] status` | 为 `true` 时设置自供电状态，否则清除。 |

> 译注（源码核对）：此函数更新运行时状态，用于 Get Status 响应；usbd_config_attrib_self() 修改配置描述符中的能力属性，二者不能相互代替。

<a id="ga37585e0124a4d0d8cf6e65f13325eaf0"></a>

### `usbd_shutdown()`

```c
int usbd_shutdown ( struct usbd_context *const uds_ctx)
```

```c
#include <zephyr/usb/usbd.h>
```

关闭 USB 设备支持。

此函数完全关闭 USB 设备支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |

**返回（Returns）**：成功为 0，失败为其他值。

> 译注（源码核对）：当前实现执行核心关闭、清理端点队列、释放预分配资源，并清除 initialized。需要特别注意：虽然原页通用返回说明写失败为其他值，本次读取的实现对内部错误只记录日志，函数最后仍返回 0。不能单凭返回 0 证明内部每一步都无错误。

<a id="gab023ab276eb68c644895483344d33948"></a>

### `usbd_str_desc_get_idx()`

```c
uint8_t usbd_str_desc_get_idx ( const struct usbd_desc_node *const desc_nd)
```

```c
#include <zephyr/usb/usbd.h>
```

从描述符节点取得 USB 字符串描述符索引。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] desc_nd` | 指向 USB 描述符节点的指针。 |

**返回（Returns）**：描述符索引；描述符不属于任何设备时为 0。

<a id="ga2996b5f6df459c8a179fc6c22f944063"></a>

### `usbd_unregister_all_classes()`

```c
int usbd_unregister_all_classes ( struct usbd_context * uds_ctx, const enum usbd_speed speed, uint8_t cfg )
```

```c
#include <zephyr/usb/usbd.h>
```

注销所有可用的 USB 类实例。

注销全部可用实例。与 `usbd_unregister_class` 类似，但不接受实例名称，而是注销所有可用实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] speed` | 配置速率。 |
| `[in] cfg` | 配置值（`bConfigurationValue`）。 |

**返回（Returns）**：成功为 0，失败为其他值。

> 译注（源码核对）：当前实现遍历相应速率的全部类节点，逐个注销，遇到第一个错误就返回；此前成功的注销不会自动撤回。它没有与注册排除列表对应的参数，应结合实际注册集合处理。

<a id="ga1ae7a7a04f4ec1206d352d5c6401c51b"></a>

### `usbd_unregister_class()`

```c
int usbd_unregister_class ( struct usbd_context * uds_ctx, const char * name, const enum usbd_speed speed, uint8_t cfg )
```

```c
#include <zephyr/usb/usbd.h>
```

注销一个 USB 类实例。

USB 类实例会被移除，下次启动协议栈时不再出现。只有设备栈处于停用状态时才能注销实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |
| `[in] name` | 类实例名称。 |
| `[in] speed` | 配置速率。 |
| `[in] cfg` | 配置值（`bConfigurationValue`）。 |

**返回（Returns）**：成功为 0，失败为其他值。

> 译注（源码核对）：当前实现同样检查 initialized，已初始化时返回 -EBUSY；不能把停用通信与撤销初始化混为一谈。原文条件按网页保留，实际生命周期按所用版本处理。

<a id="ga34086553e74795ffdc000349e61a3c8b"></a>

### `usbd_wakeup_request()`

```c
int usbd_wakeup_request ( struct usbd_context * uds_ctx)
```

```c
#include <zephyr/usb/usbd.h>
```

发起 USB 远程唤醒（Remote Wakeup，原文标记 TBD，待定）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uds_ctx` | 指向 USB 设备支持上下文的指针。 |

**返回（Returns）**：成功为 0，失败为其他值。

> 译注（源码核对）：原文仍标 TBD；当前实现已检查控制器远程唤醒能力、主机是否允许唤醒及设备是否挂起。不支持时返回 -ENOTSUP，未获允许或未挂起时返回 -EACCES，满足条件后调用 udc_host_wakeup()。

## 15.8\_相关源码与使用边界

本仓库的[核心头文件](../../../include/zephyr/usb/usbd.h)、[消息头文件](../../../include/zephyr/usb/usbd_msg.h)、[类注册实现](../../../subsys/usb/device_next/usbd_class.c)、[设备生命周期实现](../../../subsys/usb/device_next/usbd_device.c)与[消息投递实现](../../../subsys/usb/device_next/usbd_msg.c)可用于源码跟踪，版本可能与官网 latest 不同。译注核对依据为保存的[官方核心头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[消息定义](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd_msg.h)、[类实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class.c)、[设备实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_device.c)、[配置实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_config.c)与[消息实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_msg.c)，摘要见[来源记录](../SOURCES.md)。本批没有构建或运行USB固件，也未进行实板验证。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructusb__cfg__descriptor_html"></a>
<a id="astructusbd__config__node_html"></a>
<a id="astructusbd__config__node_html_a19203885a9698861f849bd0fd57cb37f"></a>
<a id="ausb__ch9_8h_html_a2a8b7c42705cd1e0fd0aecb0028cb2ba"></a>
<a id="ausb__ch9_8h_html_a7764131f2e59070eb032bd9d68d32620"></a>
<a id="agroup__iterable__section__apis_html_gae08ef16db3e04967fdca69a19ca4c70b"></a>
<a id="agroup__usbd__api_html_ga3f675bab13e089ab9576b29a6bb52364"></a>
<a id="astructusbd__class__data_html"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="astructusbd__desc__node_html"></a>
<a id="ausb__ch9_8h_html_a9f6e306632b56036d4dd7cc2430bcec9"></a>
<a id="agroup__usbd__api_html_gaf800e2040ac30844cab463c13d1fcdf8"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructusb__string__descriptor_html"></a>
<a id="astructusbd__desc__node_html_ad71ef74fd7fe43a8117704553a3be01c"></a>
<a id="asys_2byteorder_8h_html_ae7f653c0bca81809b53d8a91854ca4c9"></a>
<a id="ausb__ch9_8h_html_a6a5678b964f3a9b4ba2f52e9a51bebf5"></a>
<a id="agroup__usbd__api_html_gaef85e50556291fa93cbf72b01529b4a8"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructusb__device__descriptor_html"></a>
<a id="ausb__ch9_8h_html_a14527f51ba0e1634b3b477c80e7ae31f"></a>
<a id="ausb__ch9_8h_html_a2f6e90e87d7a1d53418ce084a293e6fc"></a>
<a id="ausb__ch9_8h_html_a62bf5e94c7c36c9d1d94438d7a12a482"></a>
<a id="ausb__ch9_8h_html_a8c4dd61ae766f50c9398c9753b4156b5"></a>
<a id="ausb__ch9_8h_html_aefeff68c3a236749d1105d94ed9bad68"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-generic-id_html_gab7d23294a6bf7fd44a98b48ec47d8a79"></a>
<a id="agroup__usbd__api_html_ga26777805f749f29efa882f9bf391473a"></a>
<a id="agroup__usbd__api_html_ga54ca08c74ae715281381d878f828727e"></a>
<a id="astructusbd__vreq__node_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048"></a>
<a id="gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d"></a>
<a id="gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509"></a>
<a id="gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7"></a>
<a id="gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266"></a>
<a id="gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P014_USB设备栈API说明.md) · [返回大纲](大纲.md) · [下一章](P016_USB设备消息API.md)
