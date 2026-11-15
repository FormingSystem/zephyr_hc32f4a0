---
id: learning.zephyr-docs.api-file-flash-test-reference.page-12
title: zephyr__net__rtp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_net\_\_rtp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

实时传输协议（Real-time Transport Protocol，RTP）的API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/logging/log_core.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/socket.h>
#include <zephyr/net/net_context.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

实时传输协议（Real-time Transport Protocol，RTP）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

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

## 12.2\_宏定义（Macros）

<a id="r_ga45dc32aa4b3075cfa01349a743c52d54"></a>

```c
#define RTP_VERSION 2
```

相关声明：[RTP_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga45dc32aa4b3075cfa01349a743c52d54)。

RFC 3550 定义的实时传输协议（RTP）版本 2。

<a id="r_gabc3a2eac823a06f7b61fcbfaca6db5c2"></a>

```c
#define RTP_MIN_HEADER_LEN 12
```

相关声明：[RTP_MIN_HEADER_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gabc3a2eac823a06f7b61fcbfaca6db5c2)。

RTP 头部最小长度（Minimum Header Length），单位为字节，不包含任何贡献源（CSRC）列表或扩展。

<a id="r_gae8984fbbdd41c1440e58b27fe0ef916d"></a>

```c
#define RTP_PAYLOAD_TYPE_MAX 127
```

相关声明：[RTP_PAYLOAD_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gae8984fbbdd41c1440e58b27fe0ef916d)。

RTP 数据包中负载类型（Payload Type）的最大值。

<a id="r_ga01b0bbc8b9131cc7ed8fef358b9b434b"></a>

```c
#define RTP_MARKER 1
```

相关声明：[RTP_MARKER](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga01b0bbc8b9131cc7ed8fef358b9b434b)。

供 rtp_session_send 的 marker 参数使用的便捷值，用于设置 RTP 标记位（Marker Bit）。

<a id="r_ga95560c5687aa035c0d0a8f2cf0b9cb74"></a>

```c
#define RTP_HDR_V_MASK GENMASK(7, 6)
```

相关声明：[RTP_HDR_V_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga95560c5687aa035c0d0a8f2cf0b9cb74)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

rtp_header::vpxcc 中版本字段（Version，V）的掩码。

<a id="r_ga85cc09256304d0ee0ae3a578610b63ca"></a>

```c
#define RTP_HDR_P_MASK BIT(5)
```

相关声明：[RTP_HDR_P_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga85cc09256304d0ee0ae3a578610b63ca)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

rtp_header::vpxcc 中填充标志（Padding，P）的掩码。

<a id="r_ga7aea179489f9d2436925eadb922c3ed5"></a>

```c
#define RTP_HDR_X_MASK BIT(4)
```

相关声明：[RTP_HDR_X_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7aea179489f9d2436925eadb922c3ed5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

rtp_header::vpxcc 中扩展标志（Extension，X）的掩码。

<a id="r_gaad8d19269d142a82868052669fc73a40"></a>

```c
#define RTP_HDR_CC_MASK GENMASK(3, 0)
```

相关声明：[RTP_HDR_CC_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaad8d19269d142a82868052669fc73a40)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

rtp_header::vpxcc 中贡献源计数字段（CSRC Count，CC）的掩码。

<a id="r_gac4e487b090ef9194accbab5a8370bab4"></a>

```c
#define RTP_HDR_M_MASK BIT(7)
```

相关声明：[RTP_HDR_M_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gac4e487b090ef9194accbab5a8370bab4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

rtp_header::mpt 中标记位（Marker，M）的掩码。

<a id="r_ga81d02bb212d040c0087669c0c264a1b3"></a>

```c
#define RTP_HDR_PT_MASK GENMASK(6, 0)
```

相关声明：[RTP_HDR_PT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga81d02bb212d040c0087669c0c264a1b3)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

rtp_header::mpt 中负载类型字段（Payload Type，PT）的掩码。

<a id="r_gab1df8386398cd1f4dd5ec5c470439bce"></a>

```c
#define RTP_MAX_CSRC_COUNT CONFIG_RTP_MAX_CSRC_COUNT
```

相关声明：[RTP_MAX_CSRC_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab1df8386398cd1f4dd5ec5c470439bce)。

能够存储的贡献源（CSRC）的最大数量。

<a id="r_ga71c2946f19f3350591f81ae5856c917a"></a>

```c
#define RTP_SESSION_DEFINE(_name, _local_port)
```

相关声明：[RTP_SESSION_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga71c2946f19f3350591f81ae5856c917a)。

定义 RTP 会话（Session）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 12.3\_类型定义（Typedefs）

<a id="r_ga8b36233d74d14bda763cfa7188b10d89"></a>

```c
typedef void(* rtp_rx_cb_t) (struct rtp_session *session, struct rtp_packet *packet, void *user_data)
```

相关声明：[rtp_rx_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga8b36233d74d14bda763cfa7188b10d89)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[rtp_packet](../network_application_model_reference/P083_rtp_packet_结构体.md)。

RTP 数据包接收回调类型（Packet Receive Callback Type）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.4\_枚举（Enumerations）

<a id="r_gad5c5d9a7c65f6a7ee02d640653cd9bd5"></a>

```c
enum rtp_role { RTP_ROLE_SINK , RTP_ROLE_SOURCE , RTP_ROLE_BOTH }
```

相关声明：[rtp_role](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gad5c5d9a7c65f6a7ee02d640653cd9bd5)、[RTP_ROLE_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ggad5c5d9a7c65f6a7ee02d640653cd9bd5ad0aacb43fde7fb0932dac083e82c2a76)、[RTP_ROLE_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ggad5c5d9a7c65f6a7ee02d640653cd9bd5a7ad4596947e09538ff21b529390140d6)、[RTP_ROLE_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ggad5c5d9a7c65f6a7ee02d640653cd9bd5a296defa58c2c0f8348ff72133a426d00)。

RTP 会话角色（Session Role）。

<a id="r_ga15d59475e540b1ddd310005700f52701"></a>

```c
enum rtp_transport_type { RTP_TRANSPORT_NUM }
```

相关声明：[rtp_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga15d59475e540b1ddd310005700f52701)、[RTP_TRANSPORT_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gga15d59475e540b1ddd310005700f52701a850aaf89c815c0f69fd5dab361b4fe43)。

RTP 会话所用的传输后端（Transport Backend）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.5\_函数（Functions）

<a id="r_ga22597830166e0ad8a41edd743ccf5649"></a>

```c
int rtp_init_header_extension (struct rtp_header_extension *hdr_x, uint16_t definition, uint8_t *data, size_t len)
```

相关声明：[rtp_init_header_extension](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga22597830166e0ad8a41edd743ccf5649)、[rtp_header_extension](../network_application_model_reference/P082_rtp_header_extension_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化 RTP 头部扩展（Header Extension）。

<a id="r_ga7dc5320de0686db3acc8ea9e75ac2bfc"></a>

```c
int rtp_session_init (struct rtp_session *session, struct net_if *iface, struct net_sockaddr *sock_addr, enum rtp_role role, uint8_t payload_type, rtp_rx_cb_t callback, void *user_data, enum rtp_transport_type transport_type)
```

相关声明：[rtp_session_init](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7dc5320de0686db3acc8ea9e75ac2bfc)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[rtp_role](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gad5c5d9a7c65f6a7ee02d640653cd9bd5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_rx_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga8b36233d74d14bda763cfa7188b10d89)、[rtp_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga15d59475e540b1ddd310005700f52701)。

初始化 RTP 会话（Session）。

<a id="r_ga77afc3360c202c59b6b34bf8d5f9c872"></a>

```c
static int rtp_session_init_rx (struct rtp_session *session, struct net_if *iface, struct net_sockaddr *sock_addr, rtp_rx_cb_t callback, void *user_data, enum rtp_transport_type transport_type)
```

相关声明：[rtp_session_init_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga77afc3360c202c59b6b34bf8d5f9c872)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[rtp_rx_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga8b36233d74d14bda763cfa7188b10d89)、[rtp_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga15d59475e540b1ddd310005700f52701)。

初始化仅接收的 RTP 会话（Receive-only Session）。

<a id="r_gab926a5adae98b8b4e142ce834f7e1769"></a>

```c
static int rtp_session_init_tx (struct rtp_session *session, struct net_if *iface, struct net_sockaddr *sock_addr, uint8_t payload_type, enum rtp_transport_type transport_type)
```

相关声明：[rtp_session_init_tx](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab926a5adae98b8b4e142ce834f7e1769)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga15d59475e540b1ddd310005700f52701)。

初始化仅发送的 RTP 会话（Transmit-only Session）。

<a id="r_ga5d7875fd2dda60e9bf827146b3ec6ad0"></a>

```c
int rtp_session_start (struct rtp_session *session)
```

相关声明：[rtp_session_start](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga5d7875fd2dda60e9bf827146b3ec6ad0)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)。

启动 RTP 会话（Session）。

<a id="r_ga98688e1d781e8eb6285153429056b7bb"></a>

```c
int rtp_session_stop (struct rtp_session *session)
```

相关声明：[rtp_session_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga98688e1d781e8eb6285153429056b7bb)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)。

停止 RTP 会话（Session）。

<a id="r_ga64f90b3a7f8c78a16f975bff108ba86e"></a>

```c
int rtp_session_add_csrc (struct rtp_session *session, uint32_t csrc)
```

相关声明：[rtp_session_add_csrc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga64f90b3a7f8c78a16f975bff108ba86e)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向会话添加贡献源（Contributing Source，CSRC）。

<a id="r_ga7f815441c6bd7084da07ad73d159e1d0"></a>

```c
int rtp_session_remove_csrc (struct rtp_session *session, uint32_t csrc)
```

相关声明：[rtp_session_remove_csrc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7f815441c6bd7084da07ad73d159e1d0)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从会话移除贡献源（Contributing Source，CSRC）。

<a id="r_ga02216271230f855d94b44b78f4757b5e"></a>

```c
int rtp_session_send (struct rtp_session *session, void *data, size_t len, uint32_t delta_ts, uint8_t padding, uint8_t marker, struct rtp_header_extension *hdr_x, uint32_t *timestamp)
```

相关声明：[rtp_session_send](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga02216271230f855d94b44b78f4757b5e)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_extension](../network_application_model_reference/P082_rtp_header_extension_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送 RTP 数据包，可选用头部扩展（Header Extension）和填充（Padding）。

<a id="r_ga6b47f65a67c20174c8f18197f78ea704"></a>

```c
static int rtp_session_send_simple (struct rtp_session *session, void *data, size_t len, uint32_t delta_ts)
```

相关声明：[rtp_session_send_simple](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga6b47f65a67c20174c8f18197f78ea704)、[rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送不含头部扩展（Header Extension）、填充（Padding）或标记（Marker）的 RTP 数据包。

<a id="r_gab132b3ceb7e7431b537dab3144351143"></a>

```c
static uint8_t rtp_header_get_v (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_v](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab132b3ceb7e7431b537dab3144351143)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取 RTP 版本字段（Version，V）。

<a id="r_gaa488e6291ed45498d38597cbc7a63fab"></a>

```c
static uint8_t rtp_header_get_p (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_p](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaa488e6291ed45498d38597cbc7a63fab)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取填充标志（Padding，P）。

<a id="r_gaa0e466fdc7416ded15259e514866e84b"></a>

```c
static uint8_t rtp_header_get_x (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_x](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaa0e466fdc7416ded15259e514866e84b)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取扩展标志（Extension，X）。

<a id="r_ga80f1fa1792c888a1f02a5ec56d7e0429"></a>

```c
static uint8_t rtp_header_get_cc (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga80f1fa1792c888a1f02a5ec56d7e0429)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取贡献源计数字段（CSRC Count，CC）。

<a id="r_ga42d0c8ff84d8a5f16f66bc6caa4a55dc"></a>

```c
static uint8_t rtp_header_get_m (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_m](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga42d0c8ff84d8a5f16f66bc6caa4a55dc)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取标记位（Marker，M）。

<a id="r_ga35eebe350579f0f8790cb94859955eb8"></a>

```c
static uint8_t rtp_header_get_pt (const struct rtp_header *h)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtp_header_get_pt](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga35eebe350579f0f8790cb94859955eb8)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)。

获取负载类型字段（Payload Type，PT）。

<a id="r_gaeb4d116a464674e0280efd5f2db67f69"></a>

```c
static void rtp_header_set_v (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_v](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaeb4d116a464674e0280efd5f2db67f69)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 RTP 版本字段（Version，V）。

<a id="r_gab7925fd9990efef208bbd1562cf46fbf"></a>

```c
static void rtp_header_set_p (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_p](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab7925fd9990efef208bbd1562cf46fbf)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置填充标志（Padding，P）。

<a id="r_ga51107e583ef87b9d312dc524a1e1a9c8"></a>

```c
static void rtp_header_set_x (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_x](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga51107e583ef87b9d312dc524a1e1a9c8)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置扩展标志（Extension，X）。

<a id="r_ga41080f91afac5e6f78f38d4d4e739917"></a>

```c
static void rtp_header_set_cc (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga41080f91afac5e6f78f38d4d4e739917)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置贡献源计数字段（CSRC Count，CC）。

<a id="r_ga45003b240b30719982ab8862a47f6681"></a>

```c
static void rtp_header_set_m (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_m](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga45003b240b30719982ab8862a47f6681)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置标记位（Marker，M）。

<a id="r_ga12f93f7d82054a193d42934f5f62b867"></a>

```c
static void rtp_header_set_pt (struct rtp_header *h, uint8_t value)
```

相关声明：[rtp_header_set_pt](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga12f93f7d82054a193d42934f5f62b867)、[rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置负载类型字段（Payload Type，PT）。


## 12.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/logging/log_core.h](../log_internal_reference/P002_日志核心头文件源码.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/socket.h](../api_source_socket_ethernet_reference/P006_socket.h_源码浏览.md)
- [zephyr/net/net_context.h](../api_source_system_reference/P022_net_context.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P736_rtp.h_源码浏览.md)
- [rtp_header_extension](../network_application_model_reference/P082_rtp_header_extension_结构体.md)
- [RFC 3550, section-5.3.1](https://datatracker.ietf.org/doc/html/rfc3550#section-5.3.1)
- [rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)
- [RFC 3550, section-5.1](https://datatracker.ietf.org/doc/html/rfc3550#section-5.1)
- [rtp_packet](../network_application_model_reference/P083_rtp_packet_结构体.md)
- [rtp_session_context](../network_application_model_reference/P085_rtp_session_context_结构体.md)
- [rtp_transport](../network_application_model_reference/P086_rtp_transport_结构体.md)
- [rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)
- [RTP_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga45dc32aa4b3075cfa01349a743c52d54)
- [RFC 3550](https://datatracker.ietf.org/doc/html/rfc3550)
- [RTP_MIN_HEADER_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gabc3a2eac823a06f7b61fcbfaca6db5c2)
- [RTP_PAYLOAD_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gae8984fbbdd41c1440e58b27fe0ef916d)
- [RTP_MARKER](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga01b0bbc8b9131cc7ed8fef358b9b434b)
- [rtp_session_send](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga02216271230f855d94b44b78f4757b5e)
- [RTP_HDR_V_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga95560c5687aa035c0d0a8f2cf0b9cb74)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [rtp_header::vpxcc](../network_application_model_reference/P081_rtp_header_结构体.md#ad7ee2dd76dd05924c45b766c993f8dcb)
- [RTP_HDR_P_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga85cc09256304d0ee0ae3a578610b63ca)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [RTP_HDR_X_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7aea179489f9d2436925eadb922c3ed5)
- [RTP_HDR_CC_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaad8d19269d142a82868052669fc73a40)
- [RTP_HDR_M_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gac4e487b090ef9194accbab5a8370bab4)
- [rtp_header::mpt](../network_application_model_reference/P081_rtp_header_结构体.md#a2608e48cddd0b18bafc279517cb98e5a)
- [RTP_HDR_PT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga81d02bb212d040c0087669c0c264a1b3)
- [RTP_MAX_CSRC_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab1df8386398cd1f4dd5ec5c470439bce)
- [RTP_SESSION_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga71c2946f19f3350591f81ae5856c917a)
- [rtp_rx_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga8b36233d74d14bda763cfa7188b10d89)
- [rtp_role](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gad5c5d9a7c65f6a7ee02d640653cd9bd5)
- [RTP_ROLE_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ggad5c5d9a7c65f6a7ee02d640653cd9bd5ad0aacb43fde7fb0932dac083e82c2a76)
- [RTP_ROLE_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ggad5c5d9a7c65f6a7ee02d640653cd9bd5a7ad4596947e09538ff21b529390140d6)
- [RTP_ROLE_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ggad5c5d9a7c65f6a7ee02d640653cd9bd5a296defa58c2c0f8348ff72133a426d00)
- [rtp_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga15d59475e540b1ddd310005700f52701)
- [RTP_TRANSPORT_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gga15d59475e540b1ddd310005700f52701a850aaf89c815c0f69fd5dab361b4fe43)
- [rtp_init_header_extension](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga22597830166e0ad8a41edd743ccf5649)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [rtp_session_init](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7dc5320de0686db3acc8ea9e75ac2bfc)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [rtp_session_init_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga77afc3360c202c59b6b34bf8d5f9c872)
- [rtp_session_init_tx](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab926a5adae98b8b4e142ce834f7e1769)
- [rtp_session_start](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga5d7875fd2dda60e9bf827146b3ec6ad0)
- [rtp_session_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga98688e1d781e8eb6285153429056b7bb)
- [rtp_session_add_csrc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga64f90b3a7f8c78a16f975bff108ba86e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [rtp_session_remove_csrc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7f815441c6bd7084da07ad73d159e1d0)
- [rtp_session_send_simple](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga6b47f65a67c20174c8f18197f78ea704)
- [rtp_header_get_v](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab132b3ceb7e7431b537dab3144351143)
- [rtp_header_get_p](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaa488e6291ed45498d38597cbc7a63fab)
- [rtp_header_get_x](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaa0e466fdc7416ded15259e514866e84b)
- [rtp_header_get_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga80f1fa1792c888a1f02a5ec56d7e0429)
- [rtp_header_get_m](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga42d0c8ff84d8a5f16f66bc6caa4a55dc)
- [rtp_header_get_pt](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga35eebe350579f0f8790cb94859955eb8)
- [rtp_header_set_v](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaeb4d116a464674e0280efd5f2db67f69)
- [rtp_header_set_p](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab7925fd9990efef208bbd1562cf46fbf)
- [rtp_header_set_x](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga51107e583ef87b9d312dc524a1e1a9c8)
- [rtp_header_set_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga41080f91afac5e6f78f38d4d4e739917)
- [rtp_header_set_m](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga45003b240b30719982ab8862a47f6681)
- [rtp_header_set_pt](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga12f93f7d82054a193d42934f5f62b867)

<a id="header-details"></a>

---

[上一章](P011_zephyr__bluetooth__classic__pbap.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__dt-bindings__clock__silabs__siwx91x-clock.h_文件参考.md)
