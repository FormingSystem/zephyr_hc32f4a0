---
id: learning.zephyr-docs.network-core-model-reference.page-55
title: net_context_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_net\_context\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

注意，上下文中不保存实际源IP地址，因为该地址已在网络接口结构（Network Interface Struct）中设置。

```c
#include <zephyr/net/net_context.h>
```

<a id="details"></a>

注意，上下文中不保存实际源IP地址，因为该地址已设置在网络接口结构（Network Interface Struct）中。如果接口中没有这样的源地址，数据包本来也无法发送。这可为每个IPv6上下文节省12字节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_a2c6f6d484e8744ec97aa966d6f0079c7"></a>

```c
void * fifo_reserved
```

相关声明：[fifo_reserved](#a2c6f6d484e8744ec97aa966d6f0079c7)。

结构的第一个成员，用于把上下文放入先进先出队列（FIFO）。

<a id="r_a1679e131dd6626bc210f23938df3fbcb"></a>

```c
void * user_data
```

相关声明：[user_data](#a1679e131dd6626bc210f23938df3fbcb)。

与上下文（Context）关联的用户数据。

<a id="r_a0ae23462dcc7f84c95e0cc69dfeb6d5a"></a>

```c
atomic_t refcount
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[refcount](#a0ae23462dcc7f84c95e0cc69dfeb6d5a)。

引用计数（Reference Count）。

<a id="r_a730e72866e94ed1695010b50c618a281"></a>

```c
struct k_mutex lock
```

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[lock](#a730e72866e94ed1695010b50c618a281)。

用于保护此上下文免遭多方同时访问的内部锁（Internal Lock）。

```c
union {
```

<a id="r_a5755b7ed1e3b9929c9aa36371da67546"></a>

```c
struct net_sockaddr local
```

相关声明：[net_sockaddr](P117_net_sockaddr_结构体.md)、[local](#a899af7c9b63a2da0ec43646f2d40a146)。

本地端点地址（Local Endpoint Address）。

<a id="r_af0f6eb90b0f81b336e13bdb2b8d8ed05"></a>

```c
struct net_sockaddr_storage local_storage
```

相关声明：[local_storage](#a709208a159d6795c5c8a56ff38732609)。

本地端点地址的存储类型别名（Storage-Typed Alias）。

<a id="r_ab394bd4658f64bb5e4f14b17c452d345"></a>

```c
};
```

本地端点地址（Local Endpoint Address）。

```c
union {
```

<a id="r_a598b861c13539854f9828109716ea7fb"></a>

```c
struct net_sockaddr remote
```

相关声明：[net_sockaddr](P117_net_sockaddr_结构体.md)、[remote](#a1511a41860e1b47b5b7652e9b350aaf4)。

远端端点地址（Remote Endpoint Address）。

<a id="r_ab999f879332d10dbad5b3cec45a2ae64"></a>

```c
struct net_sockaddr_storage remote_storage
```

相关声明：[remote_storage](#a8a548b4c545411f6110e42182b0b99b0)。

远端端点地址的存储类型别名（Storage-Typed Alias）。

<a id="r_ac37f9b4170dd54368ff31e0613702bbd"></a>

```c
};
```

远端端点地址（Remote Endpoint Address）。

<a id="r_abd8ff1b4826535df911d2af14b46e312"></a>

```c
struct net_conn_handle * conn_handler
```

相关声明：[conn_handler](#abd8ff1b4826535df911d2af14b46e312)。

连接句柄（Connection Handle）。

<a id="r_af551b252faf29ee6018d4bd783c5f2b4"></a>

```c
net_context_recv_cb_t recv_cb
```

相关声明：[net_context_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafa485a6fae8237dd7e6856f4567b2317)、[recv_cb](#af551b252faf29ee6018d4bd783c5f2b4)。

收到所需数据包时调用的接收回调（Receive Callback）。

<a id="r_a38c83746c8b2fcddf187a20299d6eb3c"></a>

```c
net_context_send_cb_t send_cb
```

相关声明：[net_context_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3caccfe9fa1bc7ce0e4654192a5de93)、[send_cb](#a38c83746c8b2fcddf187a20299d6eb3c)。

数据包成功发送后调用的发送回调（Send Callback）。

<a id="r_abc30f85e6016901b1d6fbb771b07370d"></a>

```c
net_context_connect_cb_t connect_cb
```

相关声明：[net_context_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga120ae8d4ff788ab21b19c11ed1738a71)、[connect_cb](#abc30f85e6016901b1d6fbb771b07370d)。

连接建立后调用的连接回调（Connect Callback）。

<a id="r_adee6e668bfae2749df9b986d0049f10b"></a>

```c
void * tcp
```

相关声明：[tcp](#adee6e668bfae2749df9b986d0049f10b)。

TCP连接信息（Connection Information）。

```c
struct {
```

<a id="r_ae56374afa462895448945327f6c772fa"></a>

```c
} options
```

相关声明：[options](#ae56374afa462895448945327f6c772fa)。

选项值（Option Values）。

<a id="r_abfb04fc163636498f72b29aa12087e19"></a>

```c
uint16_t proto
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[proto](#abfb04fc163636498f72b29aa12087e19)。

协议（Protocol），为UDP、TCP或IEEE 802.3协议值。

<a id="r_a300e382f78b20f220fc1b450784bbd3c"></a>

```c
uint16_t flags
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flags](#a300e382f78b20f220fc1b450784bbd3c)。

上下文标志（Context Flags）。

<a id="r_ad71d151e1e9e35b934949482066f1947"></a>

```c
int8_t iface
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[iface](#ad71d151e1e9e35b934949482066f1947)。

分配给此上下文的网络接口（Network Interface）。

```c
union {
```

```c
struct {
```

<a id="r_a7c0318bc4d93f7e41b1465ff69bed008"></a>

```c
uint8_t ipv6_hop_limit
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ipv6_hop_limit](#af9801980b3f2bb16f5ea2126a6e18cb4)。

IPv6跳数限制（Hop Limit）。

<a id="r_a633b4614f44588b9ae24a83c1158bf18"></a>

```c
uint8_t ipv6_mcast_hop_limit
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ipv6_mcast_hop_limit](#ab6d310ba4253933448584fa40e6ff4b7)。

IPv6组播跳数限制（Multicast Hop Limit）。

<a id="r_a0b769b5dff3197aab96ab1ca41ed6e52"></a>

```c
}
```

```c
struct {
```

<a id="r_aeed48091084ce1d0a1bd3404e140318b"></a>

```c
uint8_t ipv4_ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ipv4_ttl](#a9a9116844b52dc0366f770f3e6c572eb)。

IPv4生存时间（TTL）。

<a id="r_aef717fb9cbce5aa14009714cc199071b"></a>

```c
uint8_t ipv4_mcast_ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ipv4_mcast_ttl](#a329f737a3eaf0a57aa6700c59f3733dd)。

IPv4组播生存时间（Multicast TTL）。

<a id="r_a2fbb0a2d98969f8e8896bb6ac10d1d24"></a>

```c
}
```

<a id="r_ab93391cafb30d91bdcc860ba127a2848"></a>

```c
};
```

通过此上下文发送的数据包所用的IPv6跳数限制（Hop Limit）或IPv4生存时间（TTL）。

## 55.2\_详细说明（Detailed Documentation）

<a id="ab394bd4658f64bb5e4f14b17c452d345"></a>

### `[union]`

```c
union { ... } net_context
```

本地端点地址（Local Endpoint Address）。

注意，这些值采用网络字节序（Network Byte Order）。

<a id="ab93391cafb30d91bdcc860ba127a2848"></a>

### `[union]`

```c
union { ... } net_context
```

通过此上下文发送的数据包所用的IPv6跳数限制（Hop Limit）或IPv4生存时间（TTL）。

<a id="ac37f9b4170dd54368ff31e0613702bbd"></a>

### `[union]`

```c
union { ... } net_context
```

远端端点地址（Remote Endpoint Address）。

注意，这些值采用网络字节序（Network Byte Order）。

<a id="abd8ff1b4826535df911d2af14b46e312"></a>

### `conn_handler`

```c
struct net_conn_handle* net_context::conn_handler
```

连接句柄（Connection Handle）。

<a id="abc30f85e6016901b1d6fbb771b07370d"></a>

### `connect_cb`

```c
net_context_connect_cb_t net_context::connect_cb
```

连接建立后调用的连接回调（Connect Callback）。

<a id="a2c6f6d484e8744ec97aa966d6f0079c7"></a>

### `fifo_reserved`

```c
void* net_context::fifo_reserved
```

结构的第一个成员，用于把上下文放入先进先出队列（FIFO）。

<a id="a300e382f78b20f220fc1b450784bbd3c"></a>

### `flags`

```c
uint16_t net_context::flags
```

上下文标志（Context Flags）。

<a id="ad71d151e1e9e35b934949482066f1947"></a>

### `iface`

```c
int8_t net_context::iface
```

分配给此上下文的网络接口（Network Interface）。

<a id="a329f737a3eaf0a57aa6700c59f3733dd"></a>

### `ipv4_mcast_ttl`

```c
uint8_t net_context::ipv4_mcast_ttl
```

IPv4组播生存时间（Multicast TTL）。

<a id="a9a9116844b52dc0366f770f3e6c572eb"></a>

### `ipv4_ttl`

```c
uint8_t net_context::ipv4_ttl
```

IPv4生存时间（TTL）。

<a id="af9801980b3f2bb16f5ea2126a6e18cb4"></a>

### `ipv6_hop_limit`

```c
uint8_t net_context::ipv6_hop_limit
```

IPv6跳数限制（Hop Limit）。

<a id="ab6d310ba4253933448584fa40e6ff4b7"></a>

### `ipv6_mcast_hop_limit`

```c
uint8_t net_context::ipv6_mcast_hop_limit
```

IPv6组播跳数限制（Multicast Hop Limit）。

<a id="a899af7c9b63a2da0ec43646f2d40a146"></a>

### `local`

```c
struct net_sockaddr net_context::local
```

本地端点地址（Local Endpoint Address）。

<a id="a709208a159d6795c5c8a56ff38732609"></a>

### `local_storage`

```c
struct net_sockaddr_storage net_context::local_storage
```

本地端点地址的存储类型别名（Storage-Typed Alias）。

<a id="a730e72866e94ed1695010b50c618a281"></a>

### `lock`

```c
struct k_mutex net_context::lock
```

用于保护此上下文免遭多方同时访问的内部锁（Internal Lock）。

<a id="ae56374afa462895448945327f6c772fa"></a>

### `[struct]`

```c
struct { ... } net_context::options
```

选项值（Option Values）。

<a id="abfb04fc163636498f72b29aa12087e19"></a>

### `proto`

```c
uint16_t net_context::proto
```

协议（Protocol），为UDP、TCP或IEEE 802.3协议值。

<a id="af551b252faf29ee6018d4bd783c5f2b4"></a>

### `recv_cb`

```c
net_context_recv_cb_t net_context::recv_cb
```

收到所需数据包时调用的接收回调（Receive Callback）。

<a id="a0ae23462dcc7f84c95e0cc69dfeb6d5a"></a>

### `refcount`

```c
atomic_t net_context::refcount
```

引用计数（Reference Count）。

<a id="a1511a41860e1b47b5b7652e9b350aaf4"></a>

### `remote`

```c
struct net_sockaddr net_context::remote
```

远端端点地址（Remote Endpoint Address）。

<a id="a8a548b4c545411f6110e42182b0b99b0"></a>

### `remote_storage`

```c
struct net_sockaddr_storage net_context::remote_storage
```

远端端点地址的存储类型别名（Storage-Typed Alias）。

<a id="a38c83746c8b2fcddf187a20299d6eb3c"></a>

### `send_cb`

```c
net_context_send_cb_t net_context::send_cb
```

数据包成功发送后调用的发送回调（Send Callback）。

<a id="adee6e668bfae2749df9b986d0049f10b"></a>

### `tcp`

```c
void* net_context::tcp
```

TCP连接信息（Connection Information）。

<a id="a1679e131dd6626bc210f23938df3fbcb"></a>

### `user_data`

```c
void* net_context::user_data
```

与上下文（Context）关联的用户数据。

本数据类型文档由以下文件生成：

- `zephyr/net/net_context.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/net/net_context.h](https://docs.zephyrproject.org/latest/doxygen/html/net__context_8h_source.html)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [net_sockaddr](P117_net_sockaddr_结构体.md)
- [net_context_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafa485a6fae8237dd7e6856f4567b2317)
- [net_context_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3caccfe9fa1bc7ce0e4654192a5de93)
- [net_context_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga120ae8d4ff788ab21b19c11ed1738a71)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_context](P055_net_context_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_net_config_ssh_password_auth_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_net_dhcpv6_params_结构体.md)
