---
id: learning.zephyr-docs.api-file-network-device-reference.page-36
title: zephyr__net__socketcan.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_zephyr\_\_net\_\_socketcan.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SocketCAN的定义。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
```

查看此文件的源码。

SocketCAN 定义，用于提供 SocketCAN 支持。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 36.1\_数据结构（Data Structures）

<a id="r_socketcan_5Fframe"></a>

```c
struct socketcan_frame
```

相关声明：[socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)。

与Linux SocketCAN兼容的CAN帧（Frame）。

<a id="r_socketcan_5Ffilter"></a>

```c
struct socketcan_filter
```

相关声明：[socketcan_filter](../network_service_model_reference/P056_socketcan_filter_结构体.md)。

与Linux SocketCAN兼容的CAN过滤器（Filter）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 36.2\_宏定义（Macros）

<a id="r_ga73214ba92fc9df9cf1af83b8d41626c5"></a>

```c
#define NET_CAN_RAW 1
```

相关声明：[NET_CAN_RAW](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga73214ba92fc9df9cf1af83b8d41626c5)。

协议族（Protocol Family）`PF_CAN` 中的协议。

<a id="r_ga3ec3e39a63684e78a52cf9160c82c257"></a>

```c
#define SOCKETCAN_MAX_DLEN 8U
```

相关声明：[SOCKETCAN_MAX_DLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga3ec3e39a63684e78a52cf9160c82c257)。

SocketCAN 最大数据长度（Maximum Data Length）。

<a id="r_ga7d1f583cdc56ead407496713f3f22ac8"></a>

```c
#define CAN_MTU (sizeof(struct socketcan_frame))
```

相关声明：[CAN_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga7d1f583cdc56ead407496713f3f22ac8)、[socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)。

CAN 帧的最大传输单元（MTU）。

<a id="r_gace1d124719f8eac5f59788811c4afaf4"></a>

```c
#define CANFD_BRS 0x01
```

相关声明：[CANFD_BRS](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#gace1d124719f8eac5f59788811c4afaf4)。

比特率切换（Bit Rate Switch），即载荷数据使用第二种比特率。

<a id="r_gacfc1bf4466d32189a1708b4351df0794"></a>

```c
#define CANFD_ESI 0x02
```

相关声明：[CANFD_ESI](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#gacfc1bf4466d32189a1708b4351df0794)。

发送节点的错误状态指示位（Error State Indicator）。

<a id="r_ga409cae306f00226ef192320f4f01f51c"></a>

```c
#define CANFD_FDF 0x04
```

相关声明：[CANFD_FDF](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga409cae306f00226ef192320f4f01f51c)。

标记 CAN FD，以支持 `struct canfd_frame` 的双重用途（Dual Use）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 36.3\_类型定义（Typedefs）

<a id="typedef-members-0"></a>

### Linux SocketCAN 兼容性（Compatibility）

以下结构体和函数提供与 Linux SocketCAN 所用 CAN 帧（CAN Frame）及 CAN 过滤器（CAN Filter）格式的兼容性。

<a id="r_ga35a7941726d1e22defd8c3098391ca8e"></a>

```c
typedef uint32_t socketcan_id_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[socketcan_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga35a7941726d1e22defd8c3098391ca8e)。

为兼容 Linux SocketCAN 而提供的 CAN 标识符结构体（Identifier Structure）。


## 36.4\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P041_socketcan.h_源码浏览.md)
- [socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)
- [socketcan_filter](../network_service_model_reference/P056_socketcan_filter_结构体.md)
- [NET_CAN_RAW](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga73214ba92fc9df9cf1af83b8d41626c5)
- [SOCKETCAN_MAX_DLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga3ec3e39a63684e78a52cf9160c82c257)
- [CAN_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga7d1f583cdc56ead407496713f3f22ac8)
- [CANFD_BRS](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#gace1d124719f8eac5f59788811c4afaf4)
- [CANFD_ESI](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#gacfc1bf4466d32189a1708b4351df0794)
- [CANFD_FDF](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga409cae306f00226ef192320f4f01f51c)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [socketcan_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga35a7941726d1e22defd8c3098391ca8e)

<a id="header-details"></a>

---

[上一章](P035_zephyr__net__socket_service.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P037_zephyr__net__socketutils.h_文件参考.md)
