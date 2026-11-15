---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-6
title: zephyr__net__capture.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/capture_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_net\_\_capture.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/capture_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络数据包捕获（Network Packet Capture）的定义。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/device.h>
```

查看此文件的源码。

网络数据包捕获定义（Network Packet Capture Definitions），用于捕获网络数据包。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_net_5Fcapture_5Fcooked"></a>

```c
struct net_capture_cooked
```

相关声明：[net_capture_cooked](../network_core_model_reference/P050_net_capture_cooked_结构体.md)。

处理后模式捕获（Cooked Mode Capture）的上下文信息。

<a id="r_net_5Fcapture_5Finfo"></a>

```c
struct net_capture_info
```

相关声明：[net_capture_info](../network_core_model_reference/P051_net_capture_info_结构体.md)。

网络数据包捕获（Network Packet Capture）的设备信息。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_gad67ec9d34a7e4f85a4f507b30981fad8"></a>

```c
#define NET_CAPTURE_LL_ADDRLEN 8
```

相关声明：[NET_CAPTURE_LL_ADDRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gad67ec9d34a7e4f85a4f507b30981fad8)。

链路层地址（Link-layer Address）的最大长度。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_gaec06d9e76514c8fd2d7bc4e738fa8e5c"></a>

```c
typedef void(* net_capture_cb_t) (struct net_capture_info *info, void *user_data)
```

相关声明：[net_capture_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gaec06d9e76514c8fd2d7bc4e738fa8e5c)、[net_capture_info](../network_core_model_reference/P051_net_capture_info_结构体.md)。

遍历捕获设备（Capture Devices）时使用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_ga8b6c9d07ae0e1ee906129cb2f0b411ec"></a>

```c
enum net_capture_packet_type { NET_CAPTURE_HOST , NET_CAPTURE_BROADCAST , NET_CAPTURE_MULTICAST , NET_CAPTURE_OTHERHOST , NET_CAPTURE_OUTGOING }
```

相关声明：[net_capture_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga8b6c9d07ae0e1ee906129cb2f0b411ec)、[NET_CAPTURE_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411ecac19ae62e8505d342c1c2351e61a64ce5)、[NET_CAPTURE_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411eca9d0c1f31a408bc6b56b106e356f0be88)、[NET_CAPTURE_MULTICAST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411eca29604d550ee5aaf22808e7fa9c93526d)、[NET_CAPTURE_OTHERHOST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411ecae4772d47a9130a69f0477d4e8ed64264)、[NET_CAPTURE_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411ecaf12e4a87c90d5fa6ced21051dac65631)。

所捕获数据的类型与方向（Type and Direction）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_gab280c0c6cc607bdb07211a9450eae262"></a>

```c
int net_capture_setup (const char *remote_addr, const char *my_local_addr, const char *peer_addr, const struct device **dev)
```

相关声明：[net_capture_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gab280c0c6cc607bdb07211a9450eae262)、[device](../device_reference/P002_设备对象结构.md)。

设置网络数据包捕获支持（Network Packet Capturing Support）。

<a id="r_ga7a56719068938c34c9c6149296074d01"></a>

```c
static int net_capture_cleanup (const struct device *dev)
```

相关声明：[net_capture_cleanup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga7a56719068938c34c9c6149296074d01)、[device](../device_reference/P002_设备对象结构.md)。

清理网络数据包捕获支持（Network Packet Capturing Support）。

<a id="r_gaf449c308080dc126e2e7c03b38d2a0aa"></a>

```c
static int net_capture_enable (const struct device *dev, struct net_if *iface)
```

相关声明：[net_capture_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gaf449c308080dc126e2e7c03b38d2a0aa)、[device](../device_reference/P002_设备对象结构.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启用网络数据包捕获支持（Network Packet Capturing Support）。

<a id="r_ga651987b8b1e713865cff01412934f3cc"></a>

```c
static bool net_capture_is_enabled (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_capture_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga651987b8b1e713865cff01412934f3cc)、[device](../device_reference/P002_设备对象结构.md)。

网络数据包捕获（Network Packet Capture）是否已启用。

<a id="r_ga32c66260fc888dcd38b6a3cffca3b951"></a>

```c
static int net_capture_disable (const struct device *dev)
```

相关声明：[net_capture_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga32c66260fc888dcd38b6a3cffca3b951)、[device](../device_reference/P002_设备对象结构.md)。

禁用网络数据包捕获支持（Network Packet Capturing Support）。

<a id="r_ga54aba9a796ba312554ef9589b879f204"></a>

```c
static void net_capture_pkt (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_capture_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga54aba9a796ba312554ef9589b879f204)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

检查是否需要捕获网络数据包（Network Packet）。

<a id="r_ga9f567c3392745ea24f70f736c8973584"></a>

```c
static int net_capture_cooked_setup (struct net_capture_cooked *ctx, uint16_t hatype, uint16_t halen, uint8_t *addr)
```

相关声明：[net_capture_cooked_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga9f567c3392745ea24f70f736c8973584)、[net_capture_cooked](../network_core_model_reference/P050_net_capture_cooked_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化加工模式捕获上下文（Cooked Mode Capture Context）。

<a id="r_gab68bfc9510ce093447eba513c8e8d288"></a>

```c
static void net_capture_data (struct net_capture_cooked *ctx, const uint8_t *data, size_t len, enum net_capture_packet_type type, uint16_t ptype)
```

相关声明：[net_capture_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gab68bfc9510ce093447eba513c8e8d288)、[net_capture_cooked](../network_core_model_reference/P050_net_capture_cooked_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_capture_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga8b6c9d07ae0e1ee906129cb2f0b411ec)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从没有接口（Interface）的来源捕获任意数据。

<a id="r_gabd019c0856ed170da5b74f153f12768a"></a>

```c
static void net_capture_foreach (net_capture_cb_t cb, void *user_data)
```

相关声明：[net_capture_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gabd019c0856ed170da5b74f153f12768a)、[net_capture_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gaec06d9e76514c8fd2d7bc4e738fa8e5c)。

遍历所有捕获设备（Capture Devices），获取它们的信息。


## 6.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P022_capture.h_源码浏览.md)
- [net_capture_cooked](../network_core_model_reference/P050_net_capture_cooked_结构体.md)
- [net_capture_info](../network_core_model_reference/P051_net_capture_info_结构体.md)
- [NET_CAPTURE_LL_ADDRLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gad67ec9d34a7e4f85a4f507b30981fad8)
- [net_capture_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gaec06d9e76514c8fd2d7bc4e738fa8e5c)
- [net_capture_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga8b6c9d07ae0e1ee906129cb2f0b411ec)
- [NET_CAPTURE_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411ecac19ae62e8505d342c1c2351e61a64ce5)
- [NET_CAPTURE_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411eca9d0c1f31a408bc6b56b106e356f0be88)
- [NET_CAPTURE_MULTICAST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411eca29604d550ee5aaf22808e7fa9c93526d)
- [NET_CAPTURE_OTHERHOST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411ecae4772d47a9130a69f0477d4e8ed64264)
- [NET_CAPTURE_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gga8b6c9d07ae0e1ee906129cb2f0b411ecaf12e4a87c90d5fa6ced21051dac65631)
- [net_capture_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gab280c0c6cc607bdb07211a9450eae262)
- [device](../device_reference/P002_设备对象结构.md)
- [net_capture_cleanup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga7a56719068938c34c9c6149296074d01)
- [net_capture_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gaf449c308080dc126e2e7c03b38d2a0aa)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_capture_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga651987b8b1e713865cff01412934f3cc)
- [net_capture_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga32c66260fc888dcd38b6a3cffca3b951)
- [net_capture_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga54aba9a796ba312554ef9589b879f204)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_capture_cooked_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#ga9f567c3392745ea24f70f736c8973584)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_capture_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gab68bfc9510ce093447eba513c8e8d288)
- [net_capture_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html#gabd019c0856ed170da5b74f153f12768a)

<a id="header-details"></a>

---

[上一章](P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__dt-bindings__pinctrl__ch32h41x-pinctrl.h_文件参考.md)
