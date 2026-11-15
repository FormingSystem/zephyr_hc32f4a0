---
id: learning.zephyr-docs.network-service-model-reference.page-32
title: netmidi2_session_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnetmidi2__session.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_netmidi2\_session\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnetmidi2__session.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络MIDI 2会话（Session），表示与对端的连接。

```c
#include <zephyr/net/midi2.h>
```

<a id="details"></a>

网络MIDI 2会话（Session），表示与对端的连接。

<a id="header-pub-types"></a>
<a id="pub-types"></a>

## 32.1\_公开类型（Public Types）

<a id="r_a5b346997cfada6aa8ebee00de696d297"></a>

```c
enum { NETMIDI2_SESSION_NOT_INITIALIZED = 0 , NETMIDI2_SESSION_IDLE , NETMIDI2_SESSION_PENDING_INVITATION , NETMIDI2_SESSION_AUTH_REQUIRED , NETMIDI2_SESSION_ESTABLISHED , NETMIDI2_SESSION_PENDING_RESET , NETMIDI2_SESSION_PENDING_BYE }
```

相关声明：[NETMIDI2_SESSION_NOT_INITIALIZED](#a5b346997cfada6aa8ebee00de696d297a85a50751609d84c4151a2393865bebcc)、[NETMIDI2_SESSION_IDLE](#a5b346997cfada6aa8ebee00de696d297a978ea2a084813e350383bcfe961ab964)、[NETMIDI2_SESSION_PENDING_INVITATION](#a5b346997cfada6aa8ebee00de696d297a17fd2771abb25775cce6372d1fbddbbc)、[NETMIDI2_SESSION_AUTH_REQUIRED](#a5b346997cfada6aa8ebee00de696d297a5c0dce1e59eb620eb299eb16c79c3124)、[NETMIDI2_SESSION_ESTABLISHED](#a5b346997cfada6aa8ebee00de696d297af88daf6789f7d887f069e5c11d91b18f)、[NETMIDI2_SESSION_PENDING_RESET](#a5b346997cfada6aa8ebee00de696d297a50d0e9bb5d67e0710cfc7c0503404877)、[NETMIDI2_SESSION_PENDING_BYE](#a5b346997cfada6aa8ebee00de696d297ae75b03f14efdd97f0859ff0edb4f7d64)。

此会话的状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.2\_数据成员（Data Fields）

<a id="r_a78750ffb59f4ff366999bc98dde14b3c"></a>

```c
enum netmidi2_session:: { ... } state
```

相关声明：[state](#a78750ffb59f4ff366999bc98dde14b3c)。

此会话的状态。

<a id="r_a6d6d7cc6d97a83125b0422176e1d9a66"></a>

```c
uint16_t tx_ump_seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_ump_seq](#a6d6d7cc6d97a83125b0422176e1d9a66)。

下一个待发送通用 MIDI 数据包（UMP）的序列号。

<a id="r_adb2f4b5f0b4a8728085877b1c73939f4"></a>

```c
uint16_t rx_ump_seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rx_ump_seq](#adb2f4b5f0b4a8728085877b1c73939f4)。

下一个待接收通用 MIDI 数据包（UMP）的序列号。

<a id="r_a7a1d7bd416cc64e254e4a74c766a299c"></a>

```c
struct net_sockaddr_storage addr
```

相关声明：[addr](#a7a1d7bd416cc64e254e4a74c766a299c)。

对端的远程地址。

<a id="r_a6d2043af218d266065b90cc8762306a3"></a>

```c
net_socklen_t addr_len
```

相关声明：[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[addr_len](#a6d2043af218d266065b90cc8762306a3)。

对端远程地址的长度。

<a id="r_aa1e41d310563718ad152c21b88b516fe"></a>

```c
struct netmidi2_ep * ep
```

相关声明：[netmidi2_ep](P031_netmidi2_ep_结构体.md)、[ep](#aa1e41d310563718ad152c21b88b516fe)。

此会话所属的网络 MIDI 2.0（Network MIDI2）端点。

<a id="r_a4c295b22b957f2a2317ab8b7c53a5b4f"></a>

```c
const struct netmidi2_user * user
```

相关声明：[netmidi2_user](P033_netmidi2_user_结构体.md)、[user](#a4c295b22b957f2a2317ab8b7c53a5b4f)。

此会话所属的用户名。

<a id="r_a8fdb57537d7ebefd4abae5443aed0cb6"></a>

```c
char nonce [16]
```

相关声明：[nonce](#a8fdb57537d7ebefd4abae5443aed0cb6)。

用于授权此会话的密码学一次性值（crypto nonce）。

<a id="r_a5db865937e4719ed2ee444c6b1edab6a"></a>

```c
struct net_buf * tx_buf
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[tx_buf](#a5db865937e4719ed2ee444c6b1edab6a)。

此对端的发送缓冲区。

<a id="r_a65c740d870d3d0a33e6d8c9150bf6534"></a>

```c
struct k_work tx_work
```

相关声明：[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[tx_work](#a65c740d870d3d0a33e6d8c9150bf6534)。

此对端的发送工作项（work）。

## 32.3\_详细说明（Detailed Documentation）

<a id="a5b346997cfada6aa8ebee00de696d297"></a>

### `anonymous enum`

```c
anonymous enum
```

此会话的状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NETMIDI2_SESSION_NOT_INITIALIZED` | 此会话未被使用。 |
| `NETMIDI2_SESSION_IDLE` | 设备可能已经知道彼此的存在，例如通过多播 DNS（mDNS），但双方都未发送邀请（Invitation），两个设备尚未处于会话中。 |
| `NETMIDI2_SESSION_PENDING_INVITATION` | 客户端已发送邀请（Invitation），但主机尚未接受，双方也尚未发送或接收 Bye 命令。 |
| `NETMIDI2_SESSION_AUTH_REQUIRED` | 主机已回复“邀请回复：需要身份验证（Invitation Reply: Authentication Required）”或“邀请回复：需要用户身份验证（Invitation Reply: User Authentication Required）”，且尚未超时。此状态不同于空闲（Idle），因为客户端和主机都需要保存一次性值（Nonce）。 |
| `NETMIDI2_SESSION_ESTABLISHED` | 邀请已被接受，可以交换通用 MIDI 数据包（UMP）命令。 |
| `NETMIDI2_SESSION_PENDING_RESET` | 一个设备已发送会话重置（Session Reset）命令，正在等待会话重置回复（Session Reset Reply），且尚未超时。 |
| `NETMIDI2_SESSION_PENDING_BYE` | 一个端点已发送 Bye，正在等待 Bye Reply，且尚未超时。 |

**参阅（See Also）**：另见《用于通用 MIDI 数据包的用户数据报协议（User Datagram Protocol for Universal MIDI Packets）》第 6.1 节“会话状态（Session States）”。

<a id="a7a1d7bd416cc64e254e4a74c766a299c"></a>

### `addr`

```c
struct net_sockaddr_storage netmidi2_session::addr
```

对端的远程地址。

<a id="a6d2043af218d266065b90cc8762306a3"></a>

### `addr_len`

```c
net_socklen_t netmidi2_session::addr_len
```

对端远程地址的长度。

<a id="aa1e41d310563718ad152c21b88b516fe"></a>

### `ep`

```c
struct netmidi2_ep* netmidi2_session::ep
```

此会话所属的网络 MIDI 2.0（Network MIDI2）端点。

<a id="a8fdb57537d7ebefd4abae5443aed0cb6"></a>

### `nonce`

```c
char netmidi2_session::nonce[16]
```

用于授权此会话的密码学一次性值（crypto nonce）。

<a id="adb2f4b5f0b4a8728085877b1c73939f4"></a>

### `rx_ump_seq`

```c
uint16_t netmidi2_session::rx_ump_seq
```

下一个待接收通用 MIDI 数据包（UMP）的序列号。

<a id="a78750ffb59f4ff366999bc98dde14b3c"></a>

### `[]`

```c
enum { ... } netmidi2_session::state
```

此会话的状态。

**参阅（See Also）**：另见《用于通用 MIDI 数据包的用户数据报协议（User Datagram Protocol for Universal MIDI Packets）》第 6.1 节“会话状态（Session States）”。

<a id="a5db865937e4719ed2ee444c6b1edab6a"></a>

### `tx_buf`

```c
struct net_buf* netmidi2_session::tx_buf
```

此对端的发送缓冲区。

<a id="a6d6d7cc6d97a83125b0422176e1d9a66"></a>

### `tx_ump_seq`

```c
uint16_t netmidi2_session::tx_ump_seq
```

下一个待发送通用 MIDI 数据包（UMP）的序列号。

<a id="a65c740d870d3d0a33e6d8c9150bf6534"></a>

### `tx_work`

```c
struct k_work netmidi2_session::tx_work
```

此对端的发送工作项（work）。

<a id="a4c295b22b957f2a2317ab8b7c53a5b4f"></a>

### `user`

```c
const struct netmidi2_user* netmidi2_session::user
```

此会话所属的用户名。

本数据类型文档由以下文件生成：

- `zephyr/net/midi2.h`

## 32.4\_原页交叉引用（Cross References）

- [zephyr/net/midi2.h](https://docs.zephyrproject.org/latest/doxygen/html/midi2_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [netmidi2_ep](P031_netmidi2_ep_结构体.md)
- [netmidi2_user](P033_netmidi2_user_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [用于通用 MIDI 数据包的用户数据报协议（User Datagram Protocol for Universal MIDI Packets）](https://docs.zephyrproject.org/latest/doxygen/html/group__netmidi10.html)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a5b346997cfada6aa8ebee00de696d297a85a50751609d84c4151a2393865bebcc"></a>
<a id="a5b346997cfada6aa8ebee00de696d297a978ea2a084813e350383bcfe961ab964"></a>
<a id="a5b346997cfada6aa8ebee00de696d297a17fd2771abb25775cce6372d1fbddbbc"></a>
<a id="a5b346997cfada6aa8ebee00de696d297a5c0dce1e59eb620eb299eb16c79c3124"></a>
<a id="a5b346997cfada6aa8ebee00de696d297af88daf6789f7d887f069e5c11d91b18f"></a>
<a id="a5b346997cfada6aa8ebee00de696d297a50d0e9bb5d67e0710cfc7c0503404877"></a>
<a id="a5b346997cfada6aa8ebee00de696d297ae75b03f14efdd97f0859ff0edb4f7d64"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_netmidi2_ep_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_netmidi2_user_结构体.md)
