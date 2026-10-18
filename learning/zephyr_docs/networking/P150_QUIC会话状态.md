---
id: learning.zephyr-docs.networking.api-150
title: QUIC会话状态
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structquic__session__state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第150章\_QUIC会话状态

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structquic__session__state.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 150.1\_阅读说明与来源

译注：先读[QUIC传输接口指南](P143_QUIC传输接口.md)及[回显示例目录](P144_QUIC示例目录.md)，理解连接套接字、流套接字和 TLS 握手的关系，再按符号查询本组参考。

本组：[完整API参考](P147_QUIC完整API参考.md) · [头文件参考](P148_QUIC头文件参考.md) · [头文件源码](P149_QUIC头文件源码.md) · [会话状态](P150_QUIC会话状态.md) · [会话传输参数](P151_QUIC会话传输参数.md) · [统计数据](P152_QUIC统计数据.md) · [全局统计](P153_QUIC全局统计数据.md)。

可恢复的 QUIC 客户端会话状态（Resumable QUIC Client Session State）。

```c
#include <zephyr/net/quic.h>
```

可恢复的 QUIC 客户端会话状态（Resumable QUIC Client Session State）。在连接套接字上使用 `ZSOCK_QUIC_SO_SESSION_STATE` 选项，通过 `getsockopt()` 导出此结构，通过 `setsockopt()` 导入。

## 150.2\_数据成员（Data Fields）

<a id="r_ace39205048525dca62d52eccdd4d3d8d"></a>

```c
uint16_t version
```

结构格式版本，必须为 `QUIC_SESSION_STATE_VERSION`。

<a id="r_add0f4633826fa0b1ba21269eb16dc541"></a>

```c
uint16_t cipher_suite
```

与可恢复状态关联的 TLS 1.3 密码套件（Cipher Suite）。

<a id="r_ae82a2ea1627494446e68eb374ea649b7"></a>

```c
uint32_t ticket_lifetime
```

来自 `NewSessionTicket` 的票据生存期（Ticket Lifetime），单位秒。

<a id="r_a7144ad5f980931a49c2d3c93547c4f82"></a>

```c
uint32_t ticket_age_add
```

来自 `NewSessionTicket` 的随机 `ticket_age_add` 值。

<a id="r_a3eabe1807a38a5ef29d6ca9f36d206c7"></a>

```c
uint32_t max_early_data_size
```

来自 `NewSessionTicket` 的早期数据许可：不允许 0-RTT 时为 0，否则为 [RFC 9001](https://datatracker.ietf.org/doc/html/rfc9001.html) 第 4.6.1 节规定的哨兵值 `0xffffffff`；QUIC 的实际早期数据上限由传输参数控制。

<a id="r_aed88babe2f43f163983ae4894b531fb4"></a>

```c
uint64_t issue_time_ms
```

收到票据时的本地单调时间戳（Monotonic Timestamp），单位毫秒。

<a id="r_ac9a0a0146cf97781402e6d49a2b400c9"></a>

```c
uint16_t ticket_len
```

不透明票据标识（Opaque Ticket Identity）的长度。

<a id="r_afbf1dad97be7deb3e8988f440b8f09f3"></a>

```c
uint16_t psk_len
```

派生的会话恢复预共享密钥（Resumption PSK）的长度。

<a id="r_a1ec2b67e34265eb62160a73b05ab724e"></a>

```c
uint8_t ticket [256U]
```

来自 `NewSessionTicket` 的不透明票据标识。

<a id="r_a15df59733196120323fc69c5f3b0306e"></a>

```c
uint8_t psk [48U]
```

用于下一次恢复握手的派生会话恢复 PSK。

<a id="r_a56c6f48a588efb749ffe76d832331c9e"></a>

```c
struct quic_session_transport_params transport_params
```

与票据关联、已保存的对端传输参数。

相关声明：[quic_session_transport_params](P151_QUIC会话传输参数.md)。

## 150.3\_详细说明（Detailed Documentation）

<a id="add0f4633826fa0b1ba21269eb16dc541"></a>

### `cipher_suite`

```c
uint16_t quic_session_state::cipher_suite
```

与可恢复状态关联的 TLS 1.3 密码套件（Cipher Suite）。

<a id="aed88babe2f43f163983ae4894b531fb4"></a>

### `issue_time_ms`

```c
uint64_t quic_session_state::issue_time_ms
```

收到票据时的本地单调时间戳（Monotonic Timestamp），单位毫秒。

<a id="a3eabe1807a38a5ef29d6ca9f36d206c7"></a>

### `max_early_data_size`

```c
uint32_t quic_session_state::max_early_data_size
```

来自 `NewSessionTicket` 的早期数据许可：不允许 0-RTT 时为 0，否则为 [RFC 9001](https://datatracker.ietf.org/doc/html/rfc9001.html) 第 4.6.1 节规定的哨兵值 `0xffffffff`；QUIC 的实际早期数据上限由传输参数控制。

<a id="a15df59733196120323fc69c5f3b0306e"></a>

### `psk`

```c
uint8_t quic_session_state::psk[48U]
```

用于下一次恢复握手的派生会话恢复 PSK。

<a id="afbf1dad97be7deb3e8988f440b8f09f3"></a>

### `psk_len`

```c
uint16_t quic_session_state::psk_len
```

派生的会话恢复预共享密钥（Resumption PSK）的长度。

<a id="a1ec2b67e34265eb62160a73b05ab724e"></a>

### `ticket`

```c
uint8_t quic_session_state::ticket[256U]
```

来自 `NewSessionTicket` 的不透明票据标识。

<a id="a7144ad5f980931a49c2d3c93547c4f82"></a>

### `ticket_age_add`

```c
uint32_t quic_session_state::ticket_age_add
```

来自 `NewSessionTicket` 的随机 `ticket_age_add` 值。

<a id="ac9a0a0146cf97781402e6d49a2b400c9"></a>

### `ticket_len`

```c
uint16_t quic_session_state::ticket_len
```

不透明票据标识（Opaque Ticket Identity）的长度。

<a id="ae82a2ea1627494446e68eb374ea649b7"></a>

### `ticket_lifetime`

```c
uint32_t quic_session_state::ticket_lifetime
```

来自 `NewSessionTicket` 的票据生存期（Ticket Lifetime），单位秒。

<a id="a56c6f48a588efb749ffe76d832331c9e"></a>

### `transport_params`

```c
struct quic_session_transport_params quic_session_state::transport_params
```

与票据关联、已保存的对端传输参数。

<a id="ace39205048525dca62d52eccdd4d3d8d"></a>

### `version`

```c
uint16_t quic_session_state::version
```

结构格式版本，必须为 `QUIC_SESSION_STATE_VERSION`。

## 150.4\_相关源码与使用边界

声明来自 `<zephyr/net/quic.h>`。本仓库的[对应头文件](../../../include/zephyr/net/quic.h)可用于源码追踪，版本可能与官网 `latest` 不同；官方原始头文件及实现的读取摘要见[来源记录](../SOURCES.md)。

> 译注——恢复状态不是任意序列化协议：导出必须等到收到 `NewSessionTicket`，并检查返回结果；仅握手完成还不保证有可恢复票据。`issue_time_ms` 是本地单调时钟，不是 UTC 时间或服务端签发时间。结构含派生 PSK，不能当作普通调试信息公开。不同版本、ABI 或时钟起点之间不能仅凭保存了一份内存字节就假定状态可直接复用；原文只给出本结构和套接字导入／导出接口。0-RTT 的重放与拒绝处理仍由应用按协议承担。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P149_QUIC头文件源码.md) · [返回大纲](大纲.md) · [下一章](P151_QUIC会话传输参数.md)
