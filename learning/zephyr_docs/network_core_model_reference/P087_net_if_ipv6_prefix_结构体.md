---
id: learning.zephyr-docs.network-core-model-reference.page-87
title: net_if_ipv6_prefix_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__ipv6__prefix.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_net\_if\_ipv6\_prefix\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__ipv6__prefix.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络接口的IPv6前缀（Prefixes）。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

网络接口 IPv6 前缀（Network Interface IPv6 prefixes）。保存分配给此网络接口的 IPv6 前缀。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 87.1\_数据成员（Data Fields）

<a id="r_a925a97a49d383bd4ce475f5d09fcb7e3"></a>

```c
struct net_timeout lifetime
```

相关声明：[net_timeout](../time_headers_reference/P011_网络超时结构.md)、[lifetime](#a925a97a49d383bd4ce475f5d09fcb7e3)。

前缀生存期（Prefix lifetime）。

<a id="r_ac8db849f05d2532f88af625410118e0c"></a>

```c
struct net_in6_addr prefix
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[prefix](#ac8db849f05d2532f88af625410118e0c)。

IPv6前缀（Prefix）。

<a id="r_a0e2d1997e2ccfe1e1af5f16e0c74ed92"></a>

```c
struct net_if * iface
```

相关声明：[net_if](P079_net_if_结构体.md)、[iface](#a0e2d1997e2ccfe1e1af5f16e0c74ed92)。

指向使用此前缀的网络接口的反向指针（Backpointer）。

<a id="r_a4d2bc2acbe51256b76cf4d3ced3aac39"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a4d2bc2acbe51256b76cf4d3ced3aac39)。

前缀长度（Prefix length）。

<a id="r_a22090441b27bed06098679bf23b4e1e9"></a>

```c
uint8_t is_infinite: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_infinite](#a22090441b27bed06098679bf23b4e1e9)。

IP 前缀是否永久有效（Valid forever）。

<a id="r_a6a4295256957e5eddf149f1ceff62e3f"></a>

```c
uint8_t is_used: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_used](#a6a4295256957e5eddf149f1ceff62e3f)。

此前缀是否正在使用（In use）。

<a id="r_af9eb1a459f311b36f3581664a2b60f7b"></a>

```c
uint8_t is_advertised: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_advertised](#af9eb1a459f311b36f3581664a2b60f7b)。

是否在路由器通告（Router Advertisements）中通告此前缀。

## 87.2\_详细说明（Detailed Documentation）

<a id="a0e2d1997e2ccfe1e1af5f16e0c74ed92"></a>

### `iface`

```c
struct net_if* net_if_ipv6_prefix::iface
```

指向使用此前缀的网络接口的反向指针（Backpointer）。

<a id="af9eb1a459f311b36f3581664a2b60f7b"></a>

### `is_advertised`

```c
uint8_t net_if_ipv6_prefix::is_advertised
```

是否在路由器通告（Router Advertisements）中通告此前缀。

<a id="a22090441b27bed06098679bf23b4e1e9"></a>

### `is_infinite`

```c
uint8_t net_if_ipv6_prefix::is_infinite
```

IP 前缀是否永久有效（Valid forever）。

<a id="a6a4295256957e5eddf149f1ceff62e3f"></a>

### `is_used`

```c
uint8_t net_if_ipv6_prefix::is_used
```

此前缀是否正在使用（In use）。

<a id="a4d2bc2acbe51256b76cf4d3ced3aac39"></a>

### `len`

```c
uint8_t net_if_ipv6_prefix::len
```

前缀长度（Prefix length）。

<a id="a925a97a49d383bd4ce475f5d09fcb7e3"></a>

### `lifetime`

```c
struct net_timeout net_if_ipv6_prefix::lifetime
```

前缀生存期（Prefix lifetime）。

<a id="ac8db849f05d2532f88af625410118e0c"></a>

### `prefix`

```c
struct net_in6_addr net_if_ipv6_prefix::prefix
```

IPv6前缀（Prefix）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 87.3\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [net_timeout](../time_headers_reference/P011_网络超时结构.md)
- [net_in6_addr](P094_net_in6_addr_结构体.md)
- [net_if](P079_net_if_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P086_net_if_ipv6_结构体.md) · [返回大纲](大纲.md) · [下一章](P088_net_if_link_cb_结构体.md)
