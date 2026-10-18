---
id: learning.zephyr-docs.api-file-storage-event-reference.page-15
title: zephyr__net__net_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_net\_\_net\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理（Network Management）API的公共头文件。

<a id="details"></a>

```c
#include <zephyr/sys/__assert.h>
#include <zephyr/net/net_core.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/net_event.h>
```

查看此文件的源码。

网络管理（Network Management）API的公共头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_net_5Fmgmt_5Fevent_5Fcallback"></a>

```c
struct net_mgmt_event_callback
```

相关声明：[net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)。

网络管理事件回调（Network Management Event Callback）结构；用于向网络管理事件部分注册回调，使该结构的所有者能够根据给定事件掩码接收网络事件通知。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ga40e0f9fc86812ad9f6fe174b4c3804e6"></a>

```c
#define net_mgmt(_mgmt_request, _iface, _data, _len)
```

相关声明：[net_mgmt](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga40e0f9fc86812ad9f6fe174b4c3804e6)。

生成网络管理事件（Network Management Event）。

<a id="r_ga08bde8717fd8e12a338c517b22b87776"></a>

```c
#define NET_MGMT_DEFINE_REQUEST_HANDLER(_mgmt_request)
```

相关声明：[NET_MGMT_DEFINE_REQUEST_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga08bde8717fd8e12a338c517b22b87776)。

为给定网络事件（Network Event）声明请求处理函数（Request Handler）。

<a id="r_gab67d09d1e65b806ec1957451cbf60501"></a>

```c
#define NET_MGMT_REGISTER_REQUEST_HANDLER(_mgmt_request, _func)
```

相关声明：[NET_MGMT_REGISTER_REQUEST_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gab67d09d1e65b806ec1957451cbf60501)。

为给定网络事件（Network Event）创建请求处理函数（Request Handler）。

<a id="r_ga3a6ca8a72ab12afd4f9b0461253eaa12"></a>

```c
#define NET_MGMT_REGISTER_EVENT_HANDLER(_name, _event_mask, _func, _user_data)
```

相关声明：[NET_MGMT_REGISTER_EVENT_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga3a6ca8a72ab12afd4f9b0461253eaa12)。

定义静态网络事件处理程序（Static Network Event Handler）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.3\_类型定义（Typedefs）

<a id="r_ga78b9302193bd0c5cc35d81d298a5eb6b"></a>

```c
typedef int(* net_mgmt_request_handler_t) (uint64_t mgmt_request, struct net_if *iface, void *data, size_t len)
```

相关声明：[net_mgmt_request_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga78b9302193bd0c5cc35d81d298a5eb6b)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

所有网络管理（Net MGMT）请求处理程序必须遵循的函数签名（Signature）。

<a id="r_ga2e83a5a769ac52c846f255e23aea84d2"></a>

```c
typedef void(* net_mgmt_event_handler_t) (struct net_mgmt_event_callback *cb, uint64_t mgmt_event, struct net_if *iface)
```

相关声明：[net_mgmt_event_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga2e83a5a769ac52c846f255e23aea84d2)、[net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

定义用户回调处理函数签名（Callback Handler Function Signature）。

<a id="r_gaf3773f8e945c4ec05b2fab46cd8b1881"></a>

```c
typedef void(* net_mgmt_event_static_handler_t) (uint64_t mgmt_event, struct net_if *iface, void *info, size_t info_length, void *user_data)
```

相关声明：[net_mgmt_event_static_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaf3773f8e945c4ec05b2fab46cd8b1881)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

定义用户回调处理函数签名（Callback Handler Function Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.4\_枚举（Enumerations）

<a id="r_ga5e6911455b9ab9f4c82780001459461a"></a>

```c
enum net_mgmt_layer_code { NET_MGMT_LAYER_CODE_UNKNOWN = 0x00 , NET_MGMT_LAYER_CODE_IFACE = 0x01 , NET_MGMT_LAYER_CODE_CONN = 0x02 , NET_MGMT_LAYER_CODE_IPV4 = 0x03 , NET_MGMT_LAYER_CODE_IPV6 = 0x04 , NET_MGMT_LAYER_CODE_L4 = 0x05 , NET_MGMT_LAYER_CODE_COAP = 0x06 , NET_MGMT_LAYER_CODE_STATS = 0x07 , NET_MGMT_LAYER_CODE_HOSTAP = 0x08 , NET_MGMT_LAYER_CODE_ETHERNET = 0x09 , NET_MGMT_LAYER_CODE_IEEE802514 = 0x0A , NET_MGMT_LAYER_CODE_PPP = 0x0B , NET_MGMT_LAYER_CODE_VIRTUAL = 0x0C , NET_MGMT_LAYER_CODE_WIFI = 0x0D , NET_MGMT_LAYER_CODE_PACKET = 0x0E , NET_MGMT_LAYER_CODE_USER3 = 0x7C , NET_MGMT_LAYER_CODE_USER2 = 0x7D , NET_MGMT_LAYER_CODE_USER1 = 0x7E , NET_MGMT_LAYER_CODE_RESERVED = 0x7F }
```

相关声明：[net_mgmt_layer_code](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga5e6911455b9ab9f4c82780001459461a)、[NET_MGMT_LAYER_CODE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa3206e13330183c74d20e89407e11c7cd)、[NET_MGMT_LAYER_CODE_IFACE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa2e23e545f7d78775adb5271f7bf42518)、[NET_MGMT_LAYER_CODE_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aabf1c9ef98fb7237ba1591108c67bf1d7)、[NET_MGMT_LAYER_CODE_IPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa25c33c6faa9d22f4ac5b70049bb4bbd2)、[NET_MGMT_LAYER_CODE_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa8f1f092ecdfcf341458e7389cee3ace8)、[NET_MGMT_LAYER_CODE_L4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aab60d69e5ee62cb0212b1e424d7847b4e)、[NET_MGMT_LAYER_CODE_COAP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa5701861bfb5fae92e8c7b08ea02f61a7)、[NET_MGMT_LAYER_CODE_STATS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa3ab69a93464d5fa0d5be9ac9f3757cb6)、[NET_MGMT_LAYER_CODE_HOSTAP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa06935e2c46523b1a3f414f4c981992fc)、[NET_MGMT_LAYER_CODE_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aafd0569a3f3cde9e892751a84b74836b4)、[NET_MGMT_LAYER_CODE_IEEE802514](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa4893c212a3026909dcb8663abbdf2b2b)、[NET_MGMT_LAYER_CODE_PPP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa52b23f5afbf235bef6bc2aeea69271c1)、[NET_MGMT_LAYER_CODE_VIRTUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aac767c8da93a6d0f5a53e64cbfdf94fca)、[NET_MGMT_LAYER_CODE_WIFI](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa7f2f4d110d3003974bd0da0154c2d789)、[NET_MGMT_LAYER_CODE_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa997785b24761b410a1d33788c46f90b1)、[NET_MGMT_LAYER_CODE_USER3](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa4e57a620f5778d346984398c0e786977)、[NET_MGMT_LAYER_CODE_USER2](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aaa335a8c82c6d7614337e3501a69aa1d4)、[NET_MGMT_LAYER_CODE_USER1](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa10876d890aac72553ab69c0964bef48a)、[NET_MGMT_LAYER_CODE_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aaef64c0749996046b313ebf366b3eab75)。

集中定义层级代码（Layer Codes），为 7 位值。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.5\_函数（Functions）

<a id="r_ga4e42b6d16b863ca374d032682e8c11fb"></a>

```c
static void net_mgmt_init_event_callback (struct net_mgmt_event_callback *cb, net_mgmt_event_handler_t handler, uint64_t mgmt_event_mask)
```

相关声明：[net_mgmt_init_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga4e42b6d16b863ca374d032682e8c11fb)、[net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)、[net_mgmt_event_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga2e83a5a769ac52c846f255e23aea84d2)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

正确初始化 `struct net_mgmt_event_callback` 的辅助接口（Helper）。

<a id="r_gae53f5bbc973b0f414107eca75ac0c26f"></a>

```c
void net_mgmt_add_event_callback (struct net_mgmt_event_callback *cb)
```

相关声明：[net_mgmt_add_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gae53f5bbc973b0f414107eca75ac0c26f)、[net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)。

添加用户回调（User Callback）。

<a id="r_ga4960bfb01ecd891da72c57f17587f946"></a>

```c
void net_mgmt_del_event_callback (struct net_mgmt_event_callback *cb)
```

相关声明：[net_mgmt_del_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga4960bfb01ecd891da72c57f17587f946)、[net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)。

删除用户回调（User Callback）。

<a id="r_ga6415ec1e2e7f477c8976022ac33b0654"></a>

```c
void net_mgmt_event_notify_with_info (uint64_t mgmt_event, struct net_if *iface, const void *info, size_t length)
```

相关声明：[net_mgmt_event_notify_with_info](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga6415ec1e2e7f477c8976022ac33b0654)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

供系统通知事件（Event）使用。

<a id="r_gabf710692e596a2d98f37b82da884a82a"></a>

```c
static void net_mgmt_event_notify (uint64_t mgmt_event, struct net_if *iface)
```

相关声明：[net_mgmt_event_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gabf710692e596a2d98f37b82da884a82a)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

供系统通知不带附加信息（Additional Information）的事件使用。

<a id="r_ga7137c77c55ee2609941c88db79e22d1a"></a>

```c
int net_mgmt_event_wait (uint64_t mgmt_event_mask, uint64_t *raised_event, struct net_if **iface, const void **info, size_t *info_length, k_timeout_t timeout)
```

相关声明：[net_mgmt_event_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga7137c77c55ee2609941c88db79e22d1a)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

用于按事件掩码（Event Mask）同步等待。

<a id="r_ga3ab114106df41144c0fae8e6faad12cb"></a>

```c
int net_mgmt_event_wait_on_iface (struct net_if *iface, uint64_t mgmt_event_mask, uint64_t *raised_event, const void **info, size_t *info_length, k_timeout_t timeout)
```

相关声明：[net_mgmt_event_wait_on_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga3ab114106df41144c0fae8e6faad12cb)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

用于按事件掩码（Event Mask）同步等待指定接口（Iface）的事件。

<a id="r_gaab4fe2e9ea0657bf91fb1910af6729cc"></a>

```c
void net_mgmt_event_init (void)
```

相关声明：[net_mgmt_event_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaab4fe2e9ea0657bf91fb1910af6729cc)。

供网络协议栈核心（Network Stack Core）初始化网络事件处理（Event Processing）使用。


## 15.6\_原页交叉引用（Cross References）

- [zephyr/net/net_core.h](../api_source_system_reference/P023_net_core.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/net_event.h](../api_source_system_reference/P024_net_event.h_源码浏览.md)
- [查看此文件的源码。](../api_source_timing_sensor_reference/P009_net_mgmt.h_源码浏览.md)
- [net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)
- [net_mgmt](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga40e0f9fc86812ad9f6fe174b4c3804e6)
- [NET_MGMT_DEFINE_REQUEST_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga08bde8717fd8e12a338c517b22b87776)
- [NET_MGMT_REGISTER_REQUEST_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gab67d09d1e65b806ec1957451cbf60501)
- [NET_MGMT_REGISTER_EVENT_HANDLER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga3a6ca8a72ab12afd4f9b0461253eaa12)
- [net_mgmt_request_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga78b9302193bd0c5cc35d81d298a5eb6b)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_mgmt_event_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga2e83a5a769ac52c846f255e23aea84d2)
- [net_mgmt_event_static_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaf3773f8e945c4ec05b2fab46cd8b1881)
- [net_mgmt_layer_code](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga5e6911455b9ab9f4c82780001459461a)
- [NET_MGMT_LAYER_CODE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa3206e13330183c74d20e89407e11c7cd)
- [NET_MGMT_LAYER_CODE_IFACE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa2e23e545f7d78775adb5271f7bf42518)
- [NET_MGMT_LAYER_CODE_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aabf1c9ef98fb7237ba1591108c67bf1d7)
- [NET_MGMT_LAYER_CODE_IPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa25c33c6faa9d22f4ac5b70049bb4bbd2)
- [NET_MGMT_LAYER_CODE_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa8f1f092ecdfcf341458e7389cee3ace8)
- [NET_MGMT_LAYER_CODE_L4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aab60d69e5ee62cb0212b1e424d7847b4e)
- [NET_MGMT_LAYER_CODE_COAP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa5701861bfb5fae92e8c7b08ea02f61a7)
- [NET_MGMT_LAYER_CODE_STATS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa3ab69a93464d5fa0d5be9ac9f3757cb6)
- [NET_MGMT_LAYER_CODE_HOSTAP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa06935e2c46523b1a3f414f4c981992fc)
- [NET_MGMT_LAYER_CODE_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aafd0569a3f3cde9e892751a84b74836b4)
- [NET_MGMT_LAYER_CODE_IEEE802514](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa4893c212a3026909dcb8663abbdf2b2b)
- [NET_MGMT_LAYER_CODE_PPP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa52b23f5afbf235bef6bc2aeea69271c1)
- [NET_MGMT_LAYER_CODE_VIRTUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aac767c8da93a6d0f5a53e64cbfdf94fca)
- [NET_MGMT_LAYER_CODE_WIFI](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa7f2f4d110d3003974bd0da0154c2d789)
- [NET_MGMT_LAYER_CODE_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa997785b24761b410a1d33788c46f90b1)
- [NET_MGMT_LAYER_CODE_USER3](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa4e57a620f5778d346984398c0e786977)
- [NET_MGMT_LAYER_CODE_USER2](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aaa335a8c82c6d7614337e3501a69aa1d4)
- [NET_MGMT_LAYER_CODE_USER1](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa10876d890aac72553ab69c0964bef48a)
- [NET_MGMT_LAYER_CODE_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aaef64c0749996046b313ebf366b3eab75)
- [net_mgmt_init_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga4e42b6d16b863ca374d032682e8c11fb)
- [net_mgmt_add_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gae53f5bbc973b0f414107eca75ac0c26f)
- [net_mgmt_del_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga4960bfb01ecd891da72c57f17587f946)
- [net_mgmt_event_notify_with_info](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga6415ec1e2e7f477c8976022ac33b0654)
- [net_mgmt_event_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gabf710692e596a2d98f37b82da884a82a)
- [net_mgmt_event_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga7137c77c55ee2609941c88db79e22d1a)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_mgmt_event_wait_on_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga3ab114106df41144c0fae8e6faad12cb)
- [net_mgmt_event_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaab4fe2e9ea0657bf91fb1910af6729cc)

<a id="header-details"></a>

---

[上一章](P014_zephyr__net__mdns_responder.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__drivers__misc__flexram__nxp_flexram.h_文件参考.md)
