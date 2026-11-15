---
id: learning.zephyr-docs.network-application-model-reference.page-85
title: rtp_session_context_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtp__session__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_rtp\_session\_context\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtp__session__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

实时传输协议（RTP）的会话配置上下文。

```c
#include <zephyr/net/rtp.h>
```

<a id="details"></a>

实时传输协议（RTP）的会话配置上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 85.1\_数据成员（Data Fields）

<a id="r_ad989ac0403bda54841f06a31877925fa"></a>

```c
struct net_if * iface
```

相关声明：[net_if](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if.html)、[iface](#ad989ac0403bda54841f06a31877925fa)。

会话所用的网络接口（Network Interface）。

<a id="r_a5684adbb6eecd726b154d2b97059fdd4"></a>

```c
struct net_sockaddr_storage sock_addr
```

相关声明：[sock_addr](#a5684adbb6eecd726b154d2b97059fdd4)。

会话地址与端口（Session Address and Port），即组播组地址或单播对端。

<a id="r_a936e1389e182bcc07c7ddb514dfd6745"></a>

```c
enum rtp_role role
```

相关声明：[rtp_role](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gad5c5d9a7c65f6a7ee02d640653cd9bd5)、[role](#a936e1389e182bcc07c7ddb514dfd6745)。

会话角色（Role）：接收端（Sink）、源端（Source）或两者兼具。

<a id="r_ac25e4a61cb0724f7fa87773e6bd84fad"></a>

```c
uint8_t payload_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[payload_type](#ac25e4a61cb0724f7fa87773e6bd84fad)。

发送时使用的RTP载荷类型（Payload Type）字段值。

<a id="r_a1aceba2a7406f2be87186f925b4e8fda"></a>

```c
rtp_rx_cb_t callback
```

相关声明：[rtp_rx_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga8b36233d74d14bda763cfa7188b10d89)、[callback](#a1aceba2a7406f2be87186f925b4e8fda)。

数据包接收时调用的回调（Callback）；角色为RTP_ROLE_SINK或RTP_ROLE_BOTH时必须提供。

<a id="r_a149d649197fd40a9e129a9e3e95b48b2"></a>

```c
void * user_data
```

相关声明：[user_data](#a149d649197fd40a9e129a9e3e95b48b2)。

转发给回调的不透明用户数据（Opaque User Data）。

## 85.2\_详细说明（Detailed Documentation）

<a id="a1aceba2a7406f2be87186f925b4e8fda"></a>

### `callback`

```c
rtp_rx_cb_t rtp_session_context::callback
```

数据包接收时调用的回调（Callback）；角色为RTP_ROLE_SINK或RTP_ROLE_BOTH时必须提供。

<a id="ad989ac0403bda54841f06a31877925fa"></a>

### `iface`

```c
struct net_if* rtp_session_context::iface
```

会话所用的网络接口（Network Interface）。

<a id="ac25e4a61cb0724f7fa87773e6bd84fad"></a>

### `payload_type`

```c
uint8_t rtp_session_context::payload_type
```

发送时使用的RTP载荷类型（Payload Type）字段值。

<a id="a936e1389e182bcc07c7ddb514dfd6745"></a>

### `role`

```c
enum rtp_role rtp_session_context::role
```

会话角色（Role）：接收端（Sink）、源端（Source）或两者兼具。

<a id="a5684adbb6eecd726b154d2b97059fdd4"></a>

### `sock_addr`

```c
struct net_sockaddr_storage rtp_session_context::sock_addr
```

会话地址与端口（Session Address and Port），即组播组地址或单播对端。

<a id="a149d649197fd40a9e129a9e3e95b48b2"></a>

### `user_data`

```c
void* rtp_session_context::user_data
```

转发给回调的不透明用户数据（Opaque User Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/rtp.h`

## 85.3\_原页交叉引用（Cross References）

- [zephyr/net/rtp.h](https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h_source.html)
- [net_if](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if.html)
- [rtp_role](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gad5c5d9a7c65f6a7ee02d640653cd9bd5)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [rtp_rx_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga8b36233d74d14bda763cfa7188b10d89)
- [RTP_ROLE_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ggad5c5d9a7c65f6a7ee02d640653cd9bd5ad0aacb43fde7fb0932dac083e82c2a76)
- [RTP_ROLE_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ggad5c5d9a7c65f6a7ee02d640653cd9bd5a296defa58c2c0f8348ff72133a426d00)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P084_rtp_session_结构体.md) · [返回大纲](大纲.md) · [下一章](P086_rtp_transport_结构体.md)
