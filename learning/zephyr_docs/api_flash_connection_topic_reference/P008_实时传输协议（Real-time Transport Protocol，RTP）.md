---
id: learning.zephyr-docs.api-flash-connection-topic-reference.page-8
title: 实时传输协议（Real-time Transport Protocol，RTP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_实时传输协议（Real-time Transport Protocol，RTP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

接口版本：0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_rtp_5Fheader_5Fextension"></a>

```c
struct rtp_header_extension
```

相关声明：[rtp_header_extension](../network_application_model_reference/P082_rtp_header_extension_结构体.md)。

RFC 3550第5.3.1节定义的实时传输协议（RTP）头部扩展。

<a id="r_rtp_5Fheader"></a>

```c
struct rtp_header
```

相关声明：[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

RFC 3550第5.1节定义的实时传输协议（RTP）固定头部。

<a id="r_rtp_5Fpacket"></a>

```c
struct rtp_packet
```

相关声明：[rtp_packet](../network_application_model_reference/P083_rtp_packet_结构体.md)。

头部与载荷已分离的解码后RTP数据包（Packet）。

<a id="r_rtp_5Fsession_5Fcontext"></a>

```c
struct rtp_session_context
```

相关声明：[rtp_session_context](../network_application_model_reference/P085_rtp_session_context_结构体.md)。

实时传输协议（RTP）的会话配置上下文。

<a id="r_rtp_5Ftransport"></a>

```c
struct rtp_transport
```

相关声明：[rtp_transport](../network_application_model_reference/P086_rtp_transport_结构体.md)。

嵌入rtp_session的内部传输状态（Internal Transport State）。

<a id="r_rtp_5Fsession"></a>

```c
struct rtp_session
```

相关声明：[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)。

实时传输协议（RTP）的会话状态。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.2\_宏定义（Macros）

<a id="r_ga45dc32aa4b3075cfa01349a743c52d54"></a>

```c
#define RTP_VERSION 2
```

相关声明：[RTP_VERSION](#ga45dc32aa4b3075cfa01349a743c52d54)。

RFC 3550 定义的实时传输协议（RTP）版本 2。

<a id="r_gabc3a2eac823a06f7b61fcbfaca6db5c2"></a>

```c
#define RTP_MIN_HEADER_LEN 12
```

相关声明：[RTP_MIN_HEADER_LEN](#gabc3a2eac823a06f7b61fcbfaca6db5c2)。

RTP 头部最小长度（Minimum Header Length），单位为字节，不包含任何贡献源（CSRC）列表或扩展。

<a id="r_gae8984fbbdd41c1440e58b27fe0ef916d"></a>

```c
#define RTP_PAYLOAD_TYPE_MAX 127
```

相关声明：[RTP_PAYLOAD_TYPE_MAX](#gae8984fbbdd41c1440e58b27fe0ef916d)。

RTP 数据包中负载类型（Payload Type）的最大值。

<a id="r_ga01b0bbc8b9131cc7ed8fef358b9b434b"></a>

```c
#define RTP_MARKER 1
```

相关声明：[RTP_MARKER](#ga01b0bbc8b9131cc7ed8fef358b9b434b)。

供 rtp_session_send 的 marker 参数使用的便捷值，用于设置 RTP 标记位（Marker Bit）。

<a id="r_ga95560c5687aa035c0d0a8f2cf0b9cb74"></a>

```c
#define RTP_HDR_V_MASK GENMASK(7, 6)
```

相关声明：[RTP_HDR_V_MASK](#ga95560c5687aa035c0d0a8f2cf0b9cb74)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

rtp_header::vpxcc 中版本字段（Version，V）的掩码。

<a id="r_ga85cc09256304d0ee0ae3a578610b63ca"></a>

```c
#define RTP_HDR_P_MASK BIT(5)
```

相关声明：[RTP_HDR_P_MASK](#ga85cc09256304d0ee0ae3a578610b63ca)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

rtp_header::vpxcc 中填充标志（Padding，P）的掩码。

<a id="r_ga7aea179489f9d2436925eadb922c3ed5"></a>

```c
#define RTP_HDR_X_MASK BIT(4)
```

相关声明：[RTP_HDR_X_MASK](#ga7aea179489f9d2436925eadb922c3ed5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

rtp_header::vpxcc 中扩展标志（Extension，X）的掩码。

<a id="r_gaad8d19269d142a82868052669fc73a40"></a>

```c
#define RTP_HDR_CC_MASK GENMASK(3, 0)
```

相关声明：[RTP_HDR_CC_MASK](#gaad8d19269d142a82868052669fc73a40)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

rtp_header::vpxcc 中贡献源计数字段（CSRC Count，CC）的掩码。

<a id="r_gac4e487b090ef9194accbab5a8370bab4"></a>

```c
#define RTP_HDR_M_MASK BIT(7)
```

相关声明：[RTP_HDR_M_MASK](#gac4e487b090ef9194accbab5a8370bab4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

rtp_header::mpt 中标记位（Marker，M）的掩码。

<a id="r_ga81d02bb212d040c0087669c0c264a1b3"></a>

```c
#define RTP_HDR_PT_MASK GENMASK(6, 0)
```

相关声明：[RTP_HDR_PT_MASK](#ga81d02bb212d040c0087669c0c264a1b3)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

rtp_header::mpt 中负载类型字段（Payload Type，PT）的掩码。

<a id="r_gab1df8386398cd1f4dd5ec5c470439bce"></a>

```c
#define RTP_MAX_CSRC_COUNT CONFIG_RTP_MAX_CSRC_COUNT
```

相关声明：[RTP_MAX_CSRC_COUNT](#gab1df8386398cd1f4dd5ec5c470439bce)。

能够存储的贡献源（CSRC）的最大数量。

<a id="r_ga71c2946f19f3350591f81ae5856c917a"></a>

```c
#define RTP_SESSION_DEFINE(_name, _local_port)
```

相关声明：[RTP_SESSION_DEFINE](#ga71c2946f19f3350591f81ae5856c917a)。

定义 RTP 会话（Session）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.3\_类型定义（Typedefs）

<a id="r_ga8b36233d74d14bda763cfa7188b10d89"></a>

```c
typedef void(* rtp_rx_cb_t) (struct rtp_session *session, struct rtp_packet *packet, void *user_data)
```

相关声明：[rtp_rx_cb_t](#ga8b36233d74d14bda763cfa7188b10d89)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[rtp_packet](../network_application_model_reference/P083_rtp_packet_结构体.md)。

RTP 数据包接收回调类型（Packet Receive Callback Type）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.4\_枚举（Enumerations）

<a id="r_gad5c5d9a7c65f6a7ee02d640653cd9bd5"></a>

```c
enum rtp_role { RTP_ROLE_SINK , RTP_ROLE_SOURCE , RTP_ROLE_BOTH }
```

相关声明：[rtp_role](#gad5c5d9a7c65f6a7ee02d640653cd9bd5)、[RTP_ROLE_SINK](#ggad5c5d9a7c65f6a7ee02d640653cd9bd5ad0aacb43fde7fb0932dac083e82c2a76)、[RTP_ROLE_SOURCE](#ggad5c5d9a7c65f6a7ee02d640653cd9bd5a7ad4596947e09538ff21b529390140d6)、[RTP_ROLE_BOTH](#ggad5c5d9a7c65f6a7ee02d640653cd9bd5a296defa58c2c0f8348ff72133a426d00)。

RTP 会话角色（Session Role）。

<a id="r_ga15d59475e540b1ddd310005700f52701"></a>

```c
enum rtp_transport_type { RTP_TRANSPORT_NUM }
```

相关声明：[rtp_transport_type](#ga15d59475e540b1ddd310005700f52701)、[RTP_TRANSPORT_NUM](#gga15d59475e540b1ddd310005700f52701a850aaf89c815c0f69fd5dab361b4fe43)。

RTP 会话所用的传输后端（Transport Backend）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.5\_函数（Functions）

<a id="r_ga22597830166e0ad8a41edd743ccf5649"></a>

```c
int rtp_init_header_extension (struct rtp_header_extension *hdr_x, uint16_t definition, uint8_t *data, size_t len)
```

相关声明：[rtp_init_header_extension](#ga22597830166e0ad8a41edd743ccf5649)、[rtp_header_extension](../network_application_model_reference/P082_rtp_header_extension_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化 RTP 头部扩展（Header Extension）。

<a id="r_ga7dc5320de0686db3acc8ea9e75ac2bfc"></a>

```c
int rtp_session_init (struct rtp_session *session, struct net_if *iface, struct net_sockaddr *sock_addr, enum rtp_role role, uint8_t payload_type, rtp_rx_cb_t callback, void *user_data, enum rtp_transport_type transport_type)
```

相关声明：[rtp_session_init](#ga7dc5320de0686db3acc8ea9e75ac2bfc)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[rtp_role](#gad5c5d9a7c65f6a7ee02d640653cd9bd5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_rx_cb_t](#ga8b36233d74d14bda763cfa7188b10d89)、[rtp_transport_type](#ga15d59475e540b1ddd310005700f52701)。

初始化 RTP 会话（Session）。

<a id="r_ga77afc3360c202c59b6b34bf8d5f9c872"></a>

```c
static int rtp_session_init_rx (struct rtp_session *session, struct net_if *iface, struct net_sockaddr *sock_addr, rtp_rx_cb_t callback, void *user_data, enum rtp_transport_type transport_type)
```

相关声明：[rtp_session_init_rx](#ga77afc3360c202c59b6b34bf8d5f9c872)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[rtp_rx_cb_t](#ga8b36233d74d14bda763cfa7188b10d89)、[rtp_transport_type](#ga15d59475e540b1ddd310005700f52701)。

初始化仅接收的 RTP 会话（Receive-only Session）。

<a id="r_gab926a5adae98b8b4e142ce834f7e1769"></a>

```c
static int rtp_session_init_tx (struct rtp_session *session, struct net_if *iface, struct net_sockaddr *sock_addr, uint8_t payload_type, enum rtp_transport_type transport_type)
```

相关声明：[rtp_session_init_tx](#gab926a5adae98b8b4e142ce834f7e1769)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_transport_type](#ga15d59475e540b1ddd310005700f52701)。

初始化仅发送的 RTP 会话（Transmit-only Session）。

<a id="r_ga5d7875fd2dda60e9bf827146b3ec6ad0"></a>

```c
int rtp_session_start (struct rtp_session *session)
```

相关声明：[rtp_session_start](#ga5d7875fd2dda60e9bf827146b3ec6ad0)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)。

启动 RTP 会话（Session）。

<a id="r_ga98688e1d781e8eb6285153429056b7bb"></a>

```c
int rtp_session_stop (struct rtp_session *session)
```

相关声明：[rtp_session_stop](#ga98688e1d781e8eb6285153429056b7bb)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)。

停止 RTP 会话（Session）。

<a id="r_ga64f90b3a7f8c78a16f975bff108ba86e"></a>

```c
int rtp_session_add_csrc (struct rtp_session *session, uint32_t csrc)
```

相关声明：[rtp_session_add_csrc](#ga64f90b3a7f8c78a16f975bff108ba86e)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向会话添加贡献源（Contributing Source，CSRC）。

<a id="r_ga7f815441c6bd7084da07ad73d159e1d0"></a>

```c
int rtp_session_remove_csrc (struct rtp_session *session, uint32_t csrc)
```

相关声明：[rtp_session_remove_csrc](#ga7f815441c6bd7084da07ad73d159e1d0)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从会话移除贡献源（Contributing Source，CSRC）。

<a id="r_ga02216271230f855d94b44b78f4757b5e"></a>

```c
int rtp_session_send (struct rtp_session *session, void *data, size_t len, uint32_t delta_ts, uint8_t padding, uint8_t marker, struct rtp_header_extension *hdr_x, uint32_t *timestamp)
```

相关声明：[rtp_session_send](#ga02216271230f855d94b44b78f4757b5e)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_extension](../network_application_model_reference/P082_rtp_header_extension_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送 RTP 数据包，可选用头部扩展（Header Extension）和填充（Padding）。

<a id="r_ga6b47f65a67c20174c8f18197f78ea704"></a>

```c
static int rtp_session_send_simple (struct rtp_session *session, void *data, size_t len, uint32_t delta_ts)
```

相关声明：[rtp_session_send_simple](#ga6b47f65a67c20174c8f18197f78ea704)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送不含头部扩展（Header Extension）、填充（Padding）或标记（Marker）的 RTP 数据包。

<a id="r_gab132b3ceb7e7431b537dab3144351143"></a>

```c
static uint8_t rtp_header_get_v (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_v](#gab132b3ceb7e7431b537dab3144351143)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取 RTP 版本字段（Version，V）。

<a id="r_gaa488e6291ed45498d38597cbc7a63fab"></a>

```c
static uint8_t rtp_header_get_p (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_p](#gaa488e6291ed45498d38597cbc7a63fab)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取填充标志（Padding，P）。

<a id="r_gaa0e466fdc7416ded15259e514866e84b"></a>

```c
static uint8_t rtp_header_get_x (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_x](#gaa0e466fdc7416ded15259e514866e84b)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取扩展标志（Extension，X）。

<a id="r_ga80f1fa1792c888a1f02a5ec56d7e0429"></a>

```c
static uint8_t rtp_header_get_cc (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_cc](#ga80f1fa1792c888a1f02a5ec56d7e0429)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取贡献源计数字段（CSRC Count，CC）。

<a id="r_ga42d0c8ff84d8a5f16f66bc6caa4a55dc"></a>

```c
static uint8_t rtp_header_get_m (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_m](#ga42d0c8ff84d8a5f16f66bc6caa4a55dc)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取标记位（Marker，M）。

<a id="r_ga35eebe350579f0f8790cb94859955eb8"></a>

```c
static uint8_t rtp_header_get_pt (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_pt](#ga35eebe350579f0f8790cb94859955eb8)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取负载类型字段（Payload Type，PT）。

<a id="r_gaeb4d116a464674e0280efd5f2db67f69"></a>

```c
static void rtp_header_set_v (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_v](#gaeb4d116a464674e0280efd5f2db67f69)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 RTP 版本字段（Version，V）。

<a id="r_gab7925fd9990efef208bbd1562cf46fbf"></a>

```c
static void rtp_header_set_p (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_p](#gab7925fd9990efef208bbd1562cf46fbf)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置填充标志（Padding，P）。

<a id="r_ga51107e583ef87b9d312dc524a1e1a9c8"></a>

```c
static void rtp_header_set_x (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_x](#ga51107e583ef87b9d312dc524a1e1a9c8)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置扩展标志（Extension，X）。

<a id="r_ga41080f91afac5e6f78f38d4d4e739917"></a>

```c
static void rtp_header_set_cc (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_cc](#ga41080f91afac5e6f78f38d4d4e739917)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置贡献源计数字段（CSRC Count，CC）。

<a id="r_ga45003b240b30719982ab8862a47f6681"></a>

```c
static void rtp_header_set_m (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_m](#ga45003b240b30719982ab8862a47f6681)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置标记位（Marker，M）。

<a id="r_ga12f93f7d82054a193d42934f5f62b867"></a>

```c
static void rtp_header_set_pt (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_pt](#ga12f93f7d82054a193d42934f5f62b867)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置负载类型字段（Payload Type，PT）。

## 8.6\_详细说明（Detailed Documentation）

<a id="gaad8d19269d142a82868052669fc73a40"></a>

### `RTP_HDR_CC_MASK`

```c
#define RTP_HDR_CC_MASK GENMASK(3, 0)
```

```c
#include <zephyr/net/rtp.h>
```

rtp_header::vpxcc 中贡献源计数字段（CSRC Count，CC）的掩码。

<a id="gac4e487b090ef9194accbab5a8370bab4"></a>

### `RTP_HDR_M_MASK`

```c
#define RTP_HDR_M_MASK BIT(7)
```

```c
#include <zephyr/net/rtp.h>
```

rtp_header::mpt 中标记位（Marker，M）的掩码。

<a id="ga85cc09256304d0ee0ae3a578610b63ca"></a>

### `RTP_HDR_P_MASK`

```c
#define RTP_HDR_P_MASK BIT(5)
```

```c
#include <zephyr/net/rtp.h>
```

rtp_header::vpxcc 中填充标志（Padding，P）的掩码。

<a id="ga81d02bb212d040c0087669c0c264a1b3"></a>

### `RTP_HDR_PT_MASK`

```c
#define RTP_HDR_PT_MASK GENMASK(6, 0)
```

```c
#include <zephyr/net/rtp.h>
```

rtp_header::mpt 中负载类型字段（Payload Type，PT）的掩码。

<a id="ga95560c5687aa035c0d0a8f2cf0b9cb74"></a>

### `RTP_HDR_V_MASK`

```c
#define RTP_HDR_V_MASK GENMASK(7, 6)
```

```c
#include <zephyr/net/rtp.h>
```

rtp_header::vpxcc 中版本字段（Version，V）的掩码。

<a id="ga7aea179489f9d2436925eadb922c3ed5"></a>

### `RTP_HDR_X_MASK`

```c
#define RTP_HDR_X_MASK BIT(4)
```

```c
#include <zephyr/net/rtp.h>
```

rtp_header::vpxcc 中扩展标志（Extension，X）的掩码。

<a id="ga01b0bbc8b9131cc7ed8fef358b9b434b"></a>

### `RTP_MARKER`

```c
#define RTP_MARKER 1
```

```c
#include <zephyr/net/rtp.h>
```

供 rtp_session_send 的 marker 参数使用的便捷值，用于设置 RTP 标记位（Marker Bit）。

传入 0 可清除该位（Bit）。

<a id="gab1df8386398cd1f4dd5ec5c470439bce"></a>

### `RTP_MAX_CSRC_COUNT`

```c
#define RTP_MAX_CSRC_COUNT CONFIG_RTP_MAX_CSRC_COUNT
```

```c
#include <zephyr/net/rtp.h>
```

能够存储的贡献源（CSRC）的最大数量。

<a id="gabc3a2eac823a06f7b61fcbfaca6db5c2"></a>

### `RTP_MIN_HEADER_LEN`

```c
#define RTP_MIN_HEADER_LEN 12
```

```c
#include <zephyr/net/rtp.h>
```

RTP 头部最小长度（Minimum Header Length），单位为字节，不包含任何贡献源（CSRC）列表或扩展。

<a id="gae8984fbbdd41c1440e58b27fe0ef916d"></a>

### `RTP_PAYLOAD_TYPE_MAX`

```c
#define RTP_PAYLOAD_TYPE_MAX 127
```

```c
#include <zephyr/net/rtp.h>
```

RTP 数据包中负载类型（Payload Type）的最大值。

<a id="ga71c2946f19f3350591f81ae5856c917a"></a>

### `RTP_SESSION_DEFINE`

```c
#define RTP_SESSION_DEFINE ( _name, _local_port )
```

```c
#include <zephyr/net/rtp.h>
```

展开值（Value）：

```c
struct rtp_session _name = {.local_port = _local_port, RTP_SESSION_NAME(_name)}
```

定义 RTP 会话（Session）。

声明一个 `rtp_session` 变量，并进行零初始化（Zero-initialization）。使用 `rtp_session_start` 启动会话之前，应先调用 `rtp_session_init` 配置会话。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 要定义的 `rtp_session` 变量名称。 |
| `_local_port` | 发送数据包时使用的本地 UDP 端口（Local UDP Port）。设为 0 可让协议栈自动选择端口，参见 `CONFIG_RTP_LOCAL_PORT_BASE`。仅用于 `RTP_TRANSPORT_NET_PKT`。 |

<a id="ga45dc32aa4b3075cfa01349a743c52d54"></a>

### `RTP_VERSION`

```c
#define RTP_VERSION 2
```

```c
#include <zephyr/net/rtp.h>
```

RFC 3550 定义的实时传输协议（RTP）版本 2。

<a id="ga8b36233d74d14bda763cfa7188b10d89"></a>

### `rtp_rx_cb_t`

```c
typedef void(* rtp_rx_cb_t) (struct rtp_session *session, struct rtp_packet *packet, void *user_data)
```

```c
#include <zephyr/net/rtp.h>
```

RTP 数据包接收回调类型（Packet Receive Callback Type）。

RTP 数据包到达时，在网络接收上下文（Network Receive Context）中调用。回调应保持简短且非阻塞（Non-blocking）。数据包有效载荷指针（Payload Pointer）仅在回调执行期间有效。

另一线程停止会话接收路径时，回调仍可能与停止操作并发执行，或紧随其后执行。停止会话并不保证不存在正在执行或即将分派的回调。实现必须能容忍在自身认为会话已停止之后仍收到回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `session` | 指向接收到数据包的 RTP 会话（RTP Session）的指针。 |
| `packet` | 指向收到的 RTP 数据包（RTP Packet）的指针。 |
| `user_data` | 会话初始化时提供的不透明用户数据（Opaque User Data）。 |

<a id="gad5c5d9a7c65f6a7ee02d640653cd9bd5"></a>

### `rtp_role`

```c
enum rtp_role
```

```c
#include <zephyr/net/rtp.h>
```

RTP 会话角色（Session Role）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `RTP_ROLE_SINK` | 会话（Session）仅接收数据包。 |
| `RTP_ROLE_SOURCE` | 会话（Session）仅发送数据包。 |
| `RTP_ROLE_BOTH` | 会话（Session）既发送也接收数据包。 |

<a id="ga15d59475e540b1ddd310005700f52701"></a>

### `rtp_transport_type`

```c
enum rtp_transport_type
```

```c
#include <zephyr/net/rtp.h>
```

RTP 会话所用的传输后端（Transport Backend）。

传给 `rtp_session_init`。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `RTP_TRANSPORT_NUM` | 不得用作传输类型（Transport Type）。用于标记可能的传输类型最大数量（Maximum Transport Types）。 |

<a id="ga80f1fa1792c888a1f02a5ec56d7e0429"></a>

### `rtp_header_get_cc()`

```c
uint8_t rtp_header_get_cc ( const struct rtp_header * h)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

获取贡献源计数字段（CSRC Count，CC）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要读取的 RTP 头部（RTP Header）。 |

**返回（Returns）**：返回值（Returns）：贡献源计数字段值（CSRC Count Field Value）。

<a id="ga42d0c8ff84d8a5f16f66bc6caa4a55dc"></a>

### `rtp_header_get_m()`

```c
uint8_t rtp_header_get_m ( const struct rtp_header * h)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

获取标记位（Marker，M）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要读取的 RTP 头部（RTP Header）。 |

**返回（Returns）**：返回值（Returns）：标记位值（Marker Bit Value）。

<a id="gaa488e6291ed45498d38597cbc7a63fab"></a>

### `rtp_header_get_p()`

```c
uint8_t rtp_header_get_p ( const struct rtp_header * h)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

获取填充标志（Padding，P）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要读取的 RTP 头部（RTP Header）。 |

**返回（Returns）**：返回值（Returns）：填充标志值（Padding Flag Value）。

<a id="ga35eebe350579f0f8790cb94859955eb8"></a>

### `rtp_header_get_pt()`

```c
uint8_t rtp_header_get_pt ( const struct rtp_header * h)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

获取负载类型字段（Payload Type，PT）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要读取的 RTP 头部（RTP Header）。 |

**返回（Returns）**：返回值（Returns）：有效载荷类型字段值（Payload Type Field Value）。

<a id="gab132b3ceb7e7431b537dab3144351143"></a>

### `rtp_header_get_v()`

```c
uint8_t rtp_header_get_v ( const struct rtp_header * h)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

获取 RTP 版本字段（Version，V）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要读取的 RTP 头部（RTP Header）。 |

**返回（Returns）**：返回值（Returns）：版本字段值（Version Field Value）。

<a id="gaa0e466fdc7416ded15259e514866e84b"></a>

### `rtp_header_get_x()`

```c
uint8_t rtp_header_get_x ( const struct rtp_header * h)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

获取扩展标志（Extension，X）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要读取的 RTP 头部（RTP Header）。 |

**返回（Returns）**：返回值（Returns）：扩展标志值（Extension Flag Value）。

<a id="ga41080f91afac5e6f78f38d4d4e739917"></a>

### `rtp_header_set_cc()`

```c
void rtp_header_set_cc ( struct rtp_header * h, uint8_t value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

设置贡献源计数字段（CSRC Count，CC）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要修改的 RTP 头部（RTP Header）。 |
| `value` | 贡献源计数字段值（CSRC Count Field Value）。 |

<a id="ga45003b240b30719982ab8862a47f6681"></a>

### `rtp_header_set_m()`

```c
void rtp_header_set_m ( struct rtp_header * h, uint8_t value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

设置标记位（Marker，M）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要修改的 RTP 头部（RTP Header）。 |
| `value` | 标记位值（Marker Bit Value）。 |

<a id="gab7925fd9990efef208bbd1562cf46fbf"></a>

### `rtp_header_set_p()`

```c
void rtp_header_set_p ( struct rtp_header * h, uint8_t value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

设置填充标志（Padding，P）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要修改的 RTP 头部（RTP Header）。 |
| `value` | 填充标志值（Padding Flag Value）。 |

<a id="ga12f93f7d82054a193d42934f5f62b867"></a>

### `rtp_header_set_pt()`

```c
void rtp_header_set_pt ( struct rtp_header * h, uint8_t value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

设置负载类型字段（Payload Type，PT）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要修改的 RTP 头部（RTP Header）。 |
| `value` | 有效载荷类型字段值（Payload Type Field Value）。 |

<a id="gaeb4d116a464674e0280efd5f2db67f69"></a>

### `rtp_header_set_v()`

```c
void rtp_header_set_v ( struct rtp_header * h, uint8_t value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

设置 RTP 版本字段（Version，V）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要修改的 RTP 头部（RTP Header）。 |
| `value` | 版本字段值（Version Field Value）。 |

<a id="ga51107e583ef87b9d312dc524a1e1a9c8"></a>

### `rtp_header_set_x()`

```c
void rtp_header_set_x ( struct rtp_header * h, uint8_t value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

设置扩展标志（Extension，X）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h` | 要修改的 RTP 头部（RTP Header）。 |
| `value` | 扩展标志值（Extension Flag Value）。 |

<a id="ga22597830166e0ad8a41edd743ccf5649"></a>

### `rtp_init_header_extension()`

```c
int rtp_init_header_extension ( struct rtp_header_extension * hdr_x, uint16_t definition, uint8_t * data, size_t len )
```

```c
#include <zephyr/net/rtp.h>
```

初始化 RTP 头部扩展（Header Extension）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hdr_x` | 指向待初始化头部扩展结构体（Header Extension Struct）的指针。 |
| `definition` | 由配置文件定义的扩展头标识符（Extension Header Identifier）。 |
| `data` | 指向扩展数据（Extension Data）的指针。 |
| `len` | 数据长度（Data Length），以字节为单位；必须按 32 位字边界对齐（32-bit Word Boundary）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 失败时的 `errno` 值。 |

<a id="ga64f90b3a7f8c78a16f975bff108ba86e"></a>

### `rtp_session_add_csrc()`

```c
int rtp_session_add_csrc ( struct rtp_session * session, uint32_t csrc )
```

```c
#include <zephyr/net/rtp.h>
```

向会话添加贡献源（Contributing Source，CSRC）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `session` | 指向 RTP 会话（RTP Session）的指针。 |
| `csrc` | 要添加的贡献源标识符（CSRC Identifier）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 失败时的 `errno` 值。 |

<a id="ga7dc5320de0686db3acc8ea9e75ac2bfc"></a>

### `rtp_session_init()`

```c
int rtp_session_init ( struct rtp_session * session, struct net_if * iface, struct net_sockaddr * sock_addr, enum rtp_role role, uint8_t payload_type, rtp_rx_cb_t callback, void * user_data, enum rtp_transport_type transport_type )
```

```c
#include <zephyr/net/rtp.h>
```

初始化 RTP 会话（Session）。

根据 `role`，将会话配置为发送（Transmit）、接收（Receive）或同时收发。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `session` | 指向待初始化 RTP 会话（RTP Session）的指针。 |
| `iface` | 要使用的网络接口（Network Interface）。 |
| `sock_addr` | 会话地址和端口（Session Address and Port），即组播组（Multicast Group）或单播对端（Unicast Peer）。应用应注意，单播接收端（Unicast Sink）会接受来自任意发送方的 RTP 数据包。 |
| `role` | 会话充当接收端（Sink）、源端（Source），还是同时充当两者。 |
| `payload_type` | 发送时使用的 RTP 有效载荷类型字段值（Payload Type Field Value）；`role` 为 `RTP_ROLE_SINK` 时忽略。 |
| `callback` | 收到数据包时调用的回调（Callback）；`role` 为 `RTP_ROLE_SINK` 或 `RTP_ROLE_BOTH` 时必需。 |
| `user_data` | 转发给回调的不透明用户数据（Opaque User Data）。 |
| `transport_type` | 要使用的传输后端（Transport Backend），参见 `rtp_transport_type`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 失败时的 `errno` 值。 |

<a id="ga77afc3360c202c59b6b34bf8d5f9c872"></a>

### `rtp_session_init_rx()`

```c
int rtp_session_init_rx ( struct rtp_session * session, struct net_if * iface, struct net_sockaddr * sock_addr, rtp_rx_cb_t callback, void * user_data, enum rtp_transport_type transport_type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

初始化仅接收的 RTP 会话（Receive-only Session）。

对 `rtp_session_init` 的便捷封装，将会话配置为仅接收（Receive Only）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `session` | 指向待初始化 RTP 会话（RTP Session）的指针。 |
| `iface` | 要使用的网络接口（Network Interface）。 |
| `sock_addr` | 要监听的会话地址和端口（Session Address and Port）。 |
| `callback` | 收到数据包时调用的回调（Callback）。 |
| `user_data` | 转发给回调的不透明用户数据（Opaque User Data）。 |
| `transport_type` | 要使用的传输后端（Transport Backend），参见 `rtp_transport_type`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 失败时的 `errno` 值。 |

<a id="gab926a5adae98b8b4e142ce834f7e1769"></a>

### `rtp_session_init_tx()`

```c
int rtp_session_init_tx ( struct rtp_session * session, struct net_if * iface, struct net_sockaddr * sock_addr, uint8_t payload_type, enum rtp_transport_type transport_type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

初始化仅发送的 RTP 会话（Transmit-only Session）。

对 `rtp_session_init` 的便捷封装，将会话配置为仅发送（Transmit Only）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `session` | 指向待初始化 RTP 会话（RTP Session）的指针。 |
| `iface` | 要使用的网络接口（Network Interface）。 |
| `sock_addr` | 发送数据包的目标会话地址和端口（Session Address and Port）。 |
| `payload_type` | RTP 有效载荷类型字段值（Payload Type Field Value）。 |
| `transport_type` | 要使用的传输后端（Transport Backend），参见 `rtp_transport_type`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 失败时的 `errno` 值。 |

<a id="ga7f815441c6bd7084da07ad73d159e1d0"></a>

### `rtp_session_remove_csrc()`

```c
int rtp_session_remove_csrc ( struct rtp_session * session, uint32_t csrc )
```

```c
#include <zephyr/net/rtp.h>
```

从会话移除贡献源（Contributing Source，CSRC）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `session` | 指向 RTP 会话（RTP Session）的指针。 |
| `csrc` | 要移除的贡献源标识符（CSRC Identifier）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 失败时的 `errno` 值。 |

<a id="ga02216271230f855d94b44b78f4757b5e"></a>

### `rtp_session_send()`

```c
int rtp_session_send ( struct rtp_session * session, void * data, size_t len, uint32_t delta_ts, uint8_t padding, uint8_t marker, struct rtp_header_extension * hdr_x, uint32_t * timestamp )
```

```c
#include <zephyr/net/rtp.h>
```

发送 RTP 数据包，可选用头部扩展（Header Extension）和填充（Padding）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` session` | 指向 RTP 会话（RTP Session）的指针。 |
| ` data` | 指向待发送有效载荷数据（Payload Data）的指针。 |
| ` len` | 数据长度，单位为字节。 |
| ` delta_ts` | 要应用的时间戳增量（Timestamp Increment）；对于音频，通常为有效载荷覆盖的采样周期数（Number of Sample Periods）。 |
| ` padding` | 要追加的填充字节数（Number of Padding Bytes），范围为 0–255；传入 0 表示不填充。 |
| ` marker` | 标记位值（Marker Bit Value）；使用 `RTP_MARKER` 置位，使用 0 清除。 |
| ` hdr_x` | 指向头部扩展（Header Extension）的指针；为 `NULL` 时不使用扩展。 |
| `[out] timestamp` | 用于存储数据包所用 RTP 时间戳（RTP Timestamp）的指针。如果调用者不关心该时间戳，可为 `NULL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 失败时的 `errno` 值。 |

<a id="ga6b47f65a67c20174c8f18197f78ea704"></a>

### `rtp_session_send_simple()`

```c
int rtp_session_send_simple ( struct rtp_session * session, void * data, size_t len, uint32_t delta_ts )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/rtp.h>
```

发送不含头部扩展（Header Extension）、填充（Padding）或标记（Marker）的 RTP 数据包。

对 `rtp_session_send` 的便捷封装（Convenience Wrapper）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `session` | 指向 RTP 会话（RTP Session）的指针。 |
| `data` | 指向待发送有效载荷数据（Payload Data）的指针。 |
| `len` | 数据长度，单位为字节。 |
| `delta_ts` | 要应用的时间戳增量（Timestamp Increment）；对于音频，通常为有效载荷覆盖的采样周期数（Number of Sample Periods）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 失败时的 `errno` 值。 |

<a id="ga5d7875fd2dda60e9bf827146b3ec6ad0"></a>

### `rtp_session_start()`

```c
int rtp_session_start ( struct rtp_session * session)
```

```c
#include <zephyr/net/rtp.h>
```

启动 RTP 会话（Session）。

打开网络连接（Network Connections）并开始处理数据包。调用本函数之前，必须已通过 `rtp_session_init` 配置会话。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `session` | 指向 RTP 会话（RTP Session）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 失败时的 `errno` 值。 |

<a id="ga98688e1d781e8eb6285153429056b7bb"></a>

### `rtp_session_stop()`

```c
int rtp_session_stop ( struct rtp_session * session)
```

```c
#include <zephyr/net/rtp.h>
```

停止 RTP 会话（Session）。

关闭网络连接（Network Connections）并停止处理数据包。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `session` | 指向 RTP 会话（RTP Session）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negative` | 失败时的 `errno` 值。 |


## 8.7\_原页交叉引用（Cross References）

- [rtp_header_extension](../network_application_model_reference/P082_rtp_header_extension_结构体.md)
- [RFC 3550, section-5.3.1](https://datatracker.ietf.org/doc/html/rfc3550#section-5.3.1)
- [rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)
- [RFC 3550, section-5.1](https://datatracker.ietf.org/doc/html/rfc3550#section-5.1)
- [rtp_packet](../network_application_model_reference/P083_rtp_packet_结构体.md)
- [rtp_session_context](../network_application_model_reference/P085_rtp_session_context_结构体.md)
- [rtp_transport](../network_application_model_reference/P086_rtp_transport_结构体.md)
- [rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)
- [RFC 3550](https://datatracker.ietf.org/doc/html/rfc3550)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [rtp_header::vpxcc](../network_application_model_reference/P081_rtp_header_结构体.md#ad7ee2dd76dd05924c45b766c993f8dcb)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [rtp_header::mpt](../network_application_model_reference/P081_rtp_header_结构体.md#a2608e48cddd0b18bafc279517cb98e5a)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/net/rtp.h](../api_file_flash_test_reference/P012_zephyr__net__rtp.h_文件参考.md)
- [CONFIG_RTP_LOCAL_PORT_BASE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP_LOCAL_PORT_BASE)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructrtp__session_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggad5c5d9a7c65f6a7ee02d640653cd9bd5ad0aacb43fde7fb0932dac083e82c2a76"></a>
<a id="ggad5c5d9a7c65f6a7ee02d640653cd9bd5a7ad4596947e09538ff21b529390140d6"></a>
<a id="ggad5c5d9a7c65f6a7ee02d640653cd9bd5a296defa58c2c0f8348ff72133a426d00"></a>
<a id="gga15d59475e540b1ddd310005700f52701a850aaf89c815c0f69fd5dab361b4fe43"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_调制解调器命令会话（Modem Chat）.md) · [返回大纲](大纲.md) · [下一章](P009_安全Shell（SSH）客户端_服务器的通用API。.md)
