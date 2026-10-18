---
id: learning.zephyr-docs.network-core-model-reference.page-156
title: net_tuple_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__tuple.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第156章\_net\_tuple\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__tuple.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv6/IPv4网络连接元组（Network Connection Tuple）。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

IPv6/IPv4网络连接元组（Network Connection Tuple）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 156.1\_数据成员（Data Fields）

<a id="r_a8f9a1aab3c3aedeead795ca6624d4d6d"></a>

```c
struct net_addr * remote_addr
```

相关声明：[remote_addr](#a8f9a1aab3c3aedeead795ca6624d4d6d)。

IPv6／IPv4 远端地址（Remote address）。

<a id="r_af7004f8f8d74d49d6771393825612294"></a>

```c
struct net_addr * local_addr
```

相关声明：[local_addr](#af7004f8f8d74d49d6771393825612294)。

IPv6／IPv4 本地地址（Local address）。

<a id="r_ab4c31093a23bc60d8dcf5b784e3fb39a"></a>

```c
uint16_t remote_port
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[remote_port](#ab4c31093a23bc60d8dcf5b784e3fb39a)。

UDP／TCP 远端端口（Remote port）。

<a id="r_a9a1cd0dd55a9e866cb0e910120362b7e"></a>

```c
uint16_t local_port
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[local_port](#a9a1cd0dd55a9e866cb0e910120362b7e)。

UDP／TCP 本地端口（Local port）。

<a id="r_aa9eeba2c8e263afbf6368e04353d6014"></a>

```c
enum net_ip_protocol ip_proto
```

相关声明：[net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)、[ip_proto](#aa9eeba2c8e263afbf6368e04353d6014)。

IP 协议（IP protocol）。

## 156.2\_详细说明（Detailed Documentation）

<a id="aa9eeba2c8e263afbf6368e04353d6014"></a>

### `ip_proto`

```c
enum net_ip_protocol net_tuple::ip_proto
```

IP 协议（IP protocol）。

<a id="af7004f8f8d74d49d6771393825612294"></a>

### `local_addr`

```c
struct net_addr* net_tuple::local_addr
```

IPv6／IPv4 本地地址（Local address）。

<a id="a9a1cd0dd55a9e866cb0e910120362b7e"></a>

### `local_port`

```c
uint16_t net_tuple::local_port
```

UDP／TCP 本地端口（Local port）。

<a id="a8f9a1aab3c3aedeead795ca6624d4d6d"></a>

### `remote_addr`

```c
struct net_addr* net_tuple::remote_addr
```

IPv6／IPv4 远端地址（Remote address）。

<a id="ab4c31093a23bc60d8dcf5b784e3fb39a"></a>

### `remote_port`

```c
uint16_t net_tuple::remote_port
```

UDP／TCP 远端端口（Remote port）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 156.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P155_net_trickle_结构体.md) · [返回大纲](大纲.md) · [下一章](P157_net_wifi_mgmt_offload_结构体.md)
