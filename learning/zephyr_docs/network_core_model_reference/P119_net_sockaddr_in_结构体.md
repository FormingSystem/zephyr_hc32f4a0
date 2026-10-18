---
id: learning.zephyr-docs.network-core-model-reference.page-119
title: net_sockaddr_in_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr__in.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第119章\_net\_sockaddr\_in\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr__in.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv4的套接字地址结构（Socket Address Struct）。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

IPv4的套接字地址结构（Socket Address Struct）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 119.1\_数据成员（Data Fields）

<a id="r_a5acd06c9decdae8344c05d32b47746b1"></a>

```c
net_sa_family_t sin_family
```

相关声明：[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)、[sin_family](#a5acd06c9decdae8344c05d32b47746b1)。

`NET_AF_INET`。

<a id="r_a099706d7572442b073f9efffe3df7000"></a>

```c
uint16_t sin_port
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sin_port](#a099706d7572442b073f9efffe3df7000)。

端口号（Port number）。

<a id="r_a3cd81a45a4c8bc3ab18247378aeee123"></a>

```c
struct net_in_addr sin_addr
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[sin_addr](#a3cd81a45a4c8bc3ab18247378aeee123)。

IPv4地址（Address）。

## 119.2\_详细说明（Detailed Documentation）

<a id="a3cd81a45a4c8bc3ab18247378aeee123"></a>

### `sin_addr`

```c
struct net_in_addr net_sockaddr_in::sin_addr
```

IPv4地址（Address）。

<a id="a5acd06c9decdae8344c05d32b47746b1"></a>

### `sin_family`

```c
net_sa_family_t net_sockaddr_in::sin_family
```

`NET_AF_INET`。

<a id="a099706d7572442b073f9efffe3df7000"></a>

### `sin_port`

```c
uint16_t net_sockaddr_in::sin_port
```

端口号（Port number）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 119.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_in_addr](P096_net_in_addr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P118_net_sockaddr_can_结构体.md) · [返回大纲](大纲.md) · [下一章](P120_net_sockaddr_in6_结构体.md)
