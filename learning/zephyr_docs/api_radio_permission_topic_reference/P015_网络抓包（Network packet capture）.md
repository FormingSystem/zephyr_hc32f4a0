---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-15
title: 网络抓包（Network packet capture）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_网络抓包（Network packet capture）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__capture.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络抓包支持函数。

<a id="details"></a>

网络数据包捕获支持函数（Network Packet Capture Support Functions）。引入版本（Since）：2.6；API 版本（Version）：0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

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

## 15.2\_宏定义（Macros）

<a id="r_gad67ec9d34a7e4f85a4f507b30981fad8"></a>

```c
#define NET_CAPTURE_LL_ADDRLEN 8
```

相关声明：[NET_CAPTURE_LL_ADDRLEN](#gad67ec9d34a7e4f85a4f507b30981fad8)。

链路层地址（Link-layer Address）的最大长度。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.3\_类型定义（Typedefs）

<a id="r_gaec06d9e76514c8fd2d7bc4e738fa8e5c"></a>

```c
typedef void(* net_capture_cb_t) (struct net_capture_info *info, void *user_data)
```

相关声明：[net_capture_cb_t](#gaec06d9e76514c8fd2d7bc4e738fa8e5c)、[net_capture_info](../network_core_model_reference/P051_net_capture_info_结构体.md)。

遍历捕获设备（Capture Devices）时使用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.4\_枚举（Enumerations）

<a id="r_ga8b6c9d07ae0e1ee906129cb2f0b411ec"></a>

```c
enum net_capture_packet_type { NET_CAPTURE_HOST , NET_CAPTURE_BROADCAST , NET_CAPTURE_MULTICAST , NET_CAPTURE_OTHERHOST , NET_CAPTURE_OUTGOING }
```

相关声明：[net_capture_packet_type](#ga8b6c9d07ae0e1ee906129cb2f0b411ec)、[NET_CAPTURE_HOST](#gga8b6c9d07ae0e1ee906129cb2f0b411ecac19ae62e8505d342c1c2351e61a64ce5)、[NET_CAPTURE_BROADCAST](#gga8b6c9d07ae0e1ee906129cb2f0b411eca9d0c1f31a408bc6b56b106e356f0be88)、[NET_CAPTURE_MULTICAST](#gga8b6c9d07ae0e1ee906129cb2f0b411eca29604d550ee5aaf22808e7fa9c93526d)、[NET_CAPTURE_OTHERHOST](#gga8b6c9d07ae0e1ee906129cb2f0b411ecae4772d47a9130a69f0477d4e8ed64264)、[NET_CAPTURE_OUTGOING](#gga8b6c9d07ae0e1ee906129cb2f0b411ecaf12e4a87c90d5fa6ced21051dac65631)。

所捕获数据的类型与方向（Type and Direction）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.5\_函数（Functions）

<a id="r_gab280c0c6cc607bdb07211a9450eae262"></a>

```c
int net_capture_setup (const char *remote_addr, const char *my_local_addr, const char *peer_addr, const struct device **dev)
```

相关声明：[net_capture_setup](#gab280c0c6cc607bdb07211a9450eae262)、[device](../device_reference/P002_设备对象结构.md)。

设置网络数据包捕获支持（Network Packet Capturing Support）。

<a id="r_ga7a56719068938c34c9c6149296074d01"></a>

```c
static int net_capture_cleanup (const struct device *dev)
```

相关声明：[net_capture_cleanup](#ga7a56719068938c34c9c6149296074d01)、[device](../device_reference/P002_设备对象结构.md)。

清理网络数据包捕获支持（Network Packet Capturing Support）。

<a id="r_gaf449c308080dc126e2e7c03b38d2a0aa"></a>

```c
static int net_capture_enable (const struct device *dev, struct net_if *iface)
```

相关声明：[net_capture_enable](#gaf449c308080dc126e2e7c03b38d2a0aa)、[device](../device_reference/P002_设备对象结构.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启用网络数据包捕获支持（Network Packet Capturing Support）。

<a id="r_ga651987b8b1e713865cff01412934f3cc"></a>

```c
static bool net_capture_is_enabled (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_capture_is_enabled](#ga651987b8b1e713865cff01412934f3cc)、[device](../device_reference/P002_设备对象结构.md)。

网络数据包捕获（Network Packet Capture）是否已启用。

<a id="r_ga32c66260fc888dcd38b6a3cffca3b951"></a>

```c
static int net_capture_disable (const struct device *dev)
```

相关声明：[net_capture_disable](#ga32c66260fc888dcd38b6a3cffca3b951)、[device](../device_reference/P002_设备对象结构.md)。

禁用网络数据包捕获支持（Network Packet Capturing Support）。

<a id="r_ga54aba9a796ba312554ef9589b879f204"></a>

```c
static void net_capture_pkt (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_capture_pkt](#ga54aba9a796ba312554ef9589b879f204)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

检查是否需要捕获网络数据包（Network Packet）。

<a id="r_ga9f567c3392745ea24f70f736c8973584"></a>

```c
static int net_capture_cooked_setup (struct net_capture_cooked *ctx, uint16_t hatype, uint16_t halen, uint8_t *addr)
```

相关声明：[net_capture_cooked_setup](#ga9f567c3392745ea24f70f736c8973584)、[net_capture_cooked](../network_core_model_reference/P050_net_capture_cooked_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化加工模式捕获上下文（Cooked Mode Capture Context）。

<a id="r_gab68bfc9510ce093447eba513c8e8d288"></a>

```c
static void net_capture_data (struct net_capture_cooked *ctx, const uint8_t *data, size_t len, enum net_capture_packet_type type, uint16_t ptype)
```

相关声明：[net_capture_data](#gab68bfc9510ce093447eba513c8e8d288)、[net_capture_cooked](../network_core_model_reference/P050_net_capture_cooked_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_capture_packet_type](#ga8b6c9d07ae0e1ee906129cb2f0b411ec)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从没有接口（Interface）的来源捕获任意数据。

<a id="r_gabd019c0856ed170da5b74f153f12768a"></a>

```c
static void net_capture_foreach (net_capture_cb_t cb, void *user_data)
```

相关声明：[net_capture_foreach](#gabd019c0856ed170da5b74f153f12768a)、[net_capture_cb_t](#gaec06d9e76514c8fd2d7bc4e738fa8e5c)。

遍历所有捕获设备（Capture Devices），获取它们的信息。

## 15.6\_详细说明（Detailed Documentation）

<a id="gad67ec9d34a7e4f85a4f507b30981fad8"></a>

### `NET_CAPTURE_LL_ADDRLEN`

```c
#define NET_CAPTURE_LL_ADDRLEN 8
```

```c
#include <zephyr/net/capture.h>
```

链路层地址（Link-layer Address）的最大长度。

<a id="gaec06d9e76514c8fd2d7bc4e738fa8e5c"></a>

### `net_capture_cb_t`

```c
typedef void(* net_capture_cb_t) (struct net_capture_info *info, void *user_data)
```

```c
#include <zephyr/net/capture.h>
```

遍历捕获设备（Capture Devices）时使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `info` | 捕获设备（Capture Device）的信息 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="ga8b6c9d07ae0e1ee906129cb2f0b411ec"></a>

### `net_capture_packet_type`

```c
enum net_capture_packet_type
```

```c
#include <zephyr/net/capture.h>
```

所捕获数据的类型与方向（Type and Direction）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_CAPTURE_HOST` | 数据包由其他方发送给本机。 |
| `NET_CAPTURE_BROADCAST` | 数据包由其他方广播（Broadcast）。 |
| `NET_CAPTURE_MULTICAST` | 数据包由其他方多播（Multicast），而非广播。 |
| `NET_CAPTURE_OTHERHOST` | 数据包由其他方发送给另一方。 |
| `NET_CAPTURE_OUTGOING` | 数据包由本机发送。 |

<a id="ga7a56719068938c34c9c6149296074d01"></a>

### `net_capture_cleanup()`

```c
int net_capture_cleanup ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/capture.h>
```

清理网络数据包捕获支持（Network Packet Capturing Support）。

应在捕获完成、资源可以释放时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 网络捕获设备（Network Capture Device），用户必须通过 net_capture_setup() 分配。 |

**返回（Returns）**：返回值（Returns）：成功返回 0；网络数据包捕获清理失败返回小于 0 的值。

<a id="ga9f567c3392745ea24f70f736c8973584"></a>

### `net_capture_cooked_setup()`

```c
int net_capture_cooked_setup ( struct net_capture_cooked * ctx, uint16_t hatype, uint16_t halen, uint8_t * addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/capture.h>
```

初始化加工模式捕获上下文（Cooked Mode Capture Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 由用户分配的加工模式上下文结构体（Cooked Context Struct）。 |
| `hatype` | 链路层地址类型（Link-Layer Address Type）。 |
| `halen` | 链路层地址长度（Link-layer Address Length），最大为 8 字节 |
| `addr` | 链路层地址（Link-Layer Address）。 |

**返回（Returns）**：返回值（Returns）：成功返回 0；上下文初始化失败返回小于 0 的值。

<a id="gab68bfc9510ce093447eba513c8e8d288"></a>

### `net_capture_data()`

```c
void net_capture_data ( struct net_capture_cooked * ctx, const uint8_t * data, size_t len, enum net_capture_packet_type type, uint16_t ptype )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/capture.h>
```

从没有接口（Interface）的来源捕获任意数据。

没有可供捕获的网络接口时，可以使用此接口，例如 PPP 下方包含 HDLC 帧、CAN 总线数据或蓝牙数据包的底层调制解调器设备。传给此函数的数据应仅包含完整的链路层数据包（Link Layer Packets），以免丢失数据包边界。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 加工模式捕获上下文（Cooked Mode Capture Context）。 |
| `data` | 要捕获的数据。 |
| `len` | 数据长度（Data Length）。 |
| `type` | 数据包方向与类型（Direction and Type），例如是否由本机发送等。 |
| `ptype` | 协议类型 ID（Protocol Type ID），即 ethernet.h 中设置的 ETH_P_* 类型。 |

<a id="ga32c66260fc888dcd38b6a3cffca3b951"></a>

### `net_capture_disable()`

```c
int net_capture_disable ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/capture.h>
```

禁用网络数据包捕获支持（Network Packet Capturing Support）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 网络捕获设备（Network Capture Device） |

**返回（Returns）**：返回值（Returns）：成功返回 0；禁用网络数据包捕获失败返回小于 0 的值。

<a id="gaf449c308080dc126e2e7c03b38d2a0aa"></a>

### `net_capture_enable()`

```c
int net_capture_enable ( const struct device * dev, struct net_if * iface )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/capture.h>
```

启用网络数据包捕获支持（Network Packet Capturing Support）。

创建隧道网络接口（Tunnel Network Interface），将捕获的所有数据包送入其中。捕获的网络数据包被封装到 UDP 数据包中，发送给隧道对端。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 网络捕获设备（Network Capture Device） |
| `iface` | 要开始捕获其数据包的网络接口（Network Interface）。 |

**返回（Returns）**：返回值（Returns）：成功返回 0；启用网络数据包捕获失败返回小于 0 的值。

<a id="gabd019c0856ed170da5b74f153f12768a"></a>

### `net_capture_foreach()`

```c
void net_capture_foreach ( net_capture_cb_t cb, void * user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/capture.h>
```

遍历所有捕获设备（Capture Devices），获取它们的信息。

主要用于在 net-shell 中打印当前活动捕获（Active Captures）的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 针对每个捕获设备调用的回调（Callback） |
| `user_data` | 用户提供的数据（User Supplied Data）。 |

<a id="ga651987b8b1e713865cff01412934f3cc"></a>

### `net_capture_is_enabled()`

```c
bool net_capture_is_enabled ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/capture.h>
```

网络数据包捕获（Network Packet Capture）是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 网络捕获设备（Network Capture Device）；设为 NULL 时使用默认捕获设备。 |

**返回（Returns）**：返回值（Returns）：已启用返回 True；网络捕获已禁用返回 False。

<a id="ga54aba9a796ba312554ef9589b879f204"></a>

### `net_capture_pkt()`

```c
void net_capture_pkt ( struct net_if * iface, struct net_pkt * pkt )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/capture.h>
```

检查是否需要捕获网络数据包（Network Packet）。

对每个正在发送的网络数据包调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 发送该数据包的网络接口（Network Interface） |
| `pkt` | 所发送的网络数据包 |

<a id="gab280c0c6cc607bdb07211a9450eae262"></a>

### `net_capture_setup()`

```c
int net_capture_setup ( const char * remote_addr, const char * my_local_addr, const char * peer_addr, const struct device ** dev )
```

```c
#include <zephyr/net/capture.h>
```

设置网络数据包捕获支持（Network Packet Capturing Support）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `remote_addr` | 此值指定隧道远端／外层端点（Remote/Outer Endpoint）的 IP 地址，可以是 IPv4 或 IPv6 地址。该地址用于选择创建隧道的网络接口。 |
| `my_local_addr` | 隧道本地／内层 IP 地址（Local/Inner IP Address），也可包含用作 UDP 源端口的端口号。 |
| `peer_addr` | 隧道对端／内层 IP 地址（Peer/Inner IP Address），也可包含用作 UDP 目标端口的端口号。 |
| `dev` | 网络捕获设备（Network Capture Device），返回给调用方。 |

**返回（Returns）**：返回值（Returns）：成功返回 0；设置网络数据包捕获失败返回小于 0 的值。


## 15.7\_原页交叉引用（Cross References）

- [net_capture_cooked](../network_core_model_reference/P050_net_capture_cooked_结构体.md)
- [net_capture_info](../network_core_model_reference/P051_net_capture_info_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/net/capture.h](../api_file_protocol_service_reference/P006_zephyr__net__capture.h_文件参考.md)
- [ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8b6c9d07ae0e1ee906129cb2f0b411ecac19ae62e8505d342c1c2351e61a64ce5"></a>
<a id="gga8b6c9d07ae0e1ee906129cb2f0b411eca9d0c1f31a408bc6b56b106e356f0be88"></a>
<a id="gga8b6c9d07ae0e1ee906129cb2f0b411eca29604d550ee5aaf22808e7fa9c93526d"></a>
<a id="gga8b6c9d07ae0e1ee906129cb2f0b411ecae4772d47a9130a69f0477d4e8ed64264"></a>
<a id="gga8b6c9d07ae0e1ee906129cb2f0b411ecaf12e4a87c90d5fa6ced21051dac65631"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_LoRa 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P016_半主机 API（Semihosting APIs）.md)
