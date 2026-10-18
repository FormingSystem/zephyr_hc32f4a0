---
id: learning.zephyr-docs.network-application-model-reference.page-84
title: rtp_session_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtp__session.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第84章\_rtp\_session\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtp__session.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

实时传输协议（RTP）的会话状态。

```c
#include <zephyr/net/rtp.h>
```

<a id="details"></a>

RTP会话状态（Session State）。使用前应通过RTP_SESSION_DEFINE声明，并用rtp_session_init配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 84.1\_数据成员（Data Fields）

<a id="r_a2e449943d7d522022f977250513a7ac4"></a>

```c
struct rtp_transport transport
```

相关声明：[rtp_transport](P086_rtp_transport_结构体.md)、[transport](#a2e449943d7d522022f977250513a7ac4)。

传输信息（Transport Info）。

<a id="r_ac859d15cfdcf02e93fcaf02dcb88cecd"></a>

```c
struct rtp_session_context rtp_context
```

相关声明：[rtp_session_context](P085_rtp_session_context_结构体.md)、[rtp_context](#ac859d15cfdcf02e93fcaf02dcb88cecd)。

会话配置上下文（Session Configuration Context）。

<a id="r_aa2fadbf53d01bc8d0959e822a5753285"></a>

```c
struct k_mutex lock
```

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[lock](#aa2fadbf53d01bc8d0959e822a5753285)。

保护会话状态并发访问（Concurrent Access）的互斥锁。

<a id="r_aeb6fc69512410a953be85cea1f43ed41"></a>

```c
uint32_t ssrc
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ssrc](#aeb6fc69512410a953be85cea1f43ed41)。

此会话的同步源标识符（Synchronization Source，SSRC）。

<a id="r_a272c8f29a37438938a4c8e9c4d2d16ca"></a>

```c
uint32_t timestamp
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp](#a272c8f29a37438938a4c8e9c4d2d16ca)。

当前RTP时间戳（Timestamp），随每个已发送数据包推进。

<a id="r_ab5899cb4c93868ca6ecbbf10762d37b1"></a>

```c
uint16_t sequence_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sequence_number](#ab5899cb4c93868ca6ecbbf10762d37b1)。

下一个待发送数据包的序列号（Sequence Number）。

<a id="r_a29f55e109e705fd0b9c08e2aef7c5b80"></a>

```c
uint16_t local_port
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[local_port](#a29f55e109e705fd0b9c08e2aef7c5b80)。

发送时使用的本地UDP端口；0表示自动选择，见CONFIG_RTP_LOCAL_PORT_BASE。

<a id="r_aad318a86f8e90f02597b3e9edff52c65"></a>

```c
uint32_t csrc [CONFIG_RTP_MAX_CSRC_COUNT]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[csrc](#aad318a86f8e90f02597b3e9edff52c65)。

贡献源标识符（Contributing Source，CSRC）的列表。

<a id="r_a60b793a3299cf64e7d319f992e6e9f37"></a>

```c
size_t csrc_len
```

相关声明：[csrc_len](#a60b793a3299cf64e7d319f992e6e9f37)。

csrc中有效条目的数量。

<a id="r_a99b191ad08cd8fe5e20a4d8e1bae7547"></a>

```c
const char * name
```

相关声明：[name](#a99b191ad08cd8fe5e20a4d8e1bae7547)。

调试日志消息中使用的可读会话名称（Session Name）。

## 84.2\_详细说明（Detailed Documentation）

<a id="aad318a86f8e90f02597b3e9edff52c65"></a>

### `csrc`

```c
uint32_t rtp_session::csrc[CONFIG_RTP_MAX_CSRC_COUNT]
```

贡献源标识符（Contributing Source，CSRC）的列表。

<a id="a60b793a3299cf64e7d319f992e6e9f37"></a>

### `csrc_len`

```c
size_t rtp_session::csrc_len
```

csrc中有效条目的数量。

<a id="a29f55e109e705fd0b9c08e2aef7c5b80"></a>

### `local_port`

```c
uint16_t rtp_session::local_port
```

发送时使用的本地UDP端口；0表示自动选择，见CONFIG_RTP_LOCAL_PORT_BASE。

<a id="aa2fadbf53d01bc8d0959e822a5753285"></a>

### `lock`

```c
struct k_mutex rtp_session::lock
```

保护会话状态并发访问（Concurrent Access）的互斥锁。

<a id="a99b191ad08cd8fe5e20a4d8e1bae7547"></a>

### `name`

```c
const char* rtp_session::name
```

调试日志消息中使用的可读会话名称（Session Name）。

<a id="ac859d15cfdcf02e93fcaf02dcb88cecd"></a>

### `rtp_context`

```c
struct rtp_session_context rtp_session::rtp_context
```

会话配置上下文（Session Configuration Context）。

<a id="ab5899cb4c93868ca6ecbbf10762d37b1"></a>

### `sequence_number`

```c
uint16_t rtp_session::sequence_number
```

下一个待发送数据包的序列号（Sequence Number）。

<a id="aeb6fc69512410a953be85cea1f43ed41"></a>

### `ssrc`

```c
uint32_t rtp_session::ssrc
```

此会话的同步源标识符（Synchronization Source，SSRC）。

<a id="a272c8f29a37438938a4c8e9c4d2d16ca"></a>

### `timestamp`

```c
uint32_t rtp_session::timestamp
```

当前RTP时间戳（Timestamp），随每个已发送数据包推进。

<a id="a2e449943d7d522022f977250513a7ac4"></a>

### `transport`

```c
struct rtp_transport rtp_session::transport
```

传输信息（Transport Info）。

本数据类型文档由以下文件生成：

- `zephyr/net/rtp.h`

## 84.3\_原页交叉引用（Cross References）

- [zephyr/net/rtp.h](https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h_source.html)
- [rtp_transport](P086_rtp_transport_结构体.md)
- [rtp_session_context](P085_rtp_session_context_结构体.md)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [CONFIG_RTP_LOCAL_PORT_BASE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP_LOCAL_PORT_BASE)
- [RTP_SESSION_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga71c2946f19f3350591f81ae5856c917a)
- [rtp_session_init](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7dc5320de0686db3acc8ea9e75ac2bfc)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P083_rtp_packet_结构体.md) · [返回大纲](大纲.md) · [下一章](P085_rtp_session_context_结构体.md)
