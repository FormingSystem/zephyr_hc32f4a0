---
id: learning.zephyr-docs.network-core-model-reference.page-99
title: net_ip_mreq_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__ip__mreq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_net\_ip\_mreq\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__ip__mreq.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设置IPv4组播网络接口（Multicast Network Interface）时使用的结构。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

设置IPv4组播网络接口（Multicast Network Interface）时使用的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 99.1\_数据成员（Data Fields）

<a id="r_a1bef08a9e287288095ae7589489bbbb8"></a>

```c
struct net_in_addr imr_multiaddr
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[imr_multiaddr](#a1bef08a9e287288095ae7589489bbbb8)。

IP 多播组地址（IP multicast group address）。

<a id="r_a9c4f5c84afbfd49f20bef330ade6a88a"></a>

```c
struct net_in_addr imr_interface
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[imr_interface](#a9c4f5c84afbfd49f20bef330ade6a88a)。

本地接口的 IP 地址（IP address of local interface）。

## 99.2\_详细说明（Detailed Documentation）

<a id="a9c4f5c84afbfd49f20bef330ade6a88a"></a>

### `imr_interface`

```c
struct net_in_addr net_ip_mreq::imr_interface
```

本地接口的 IP 地址（IP address of local interface）。

<a id="a1bef08a9e287288095ae7589489bbbb8"></a>

### `imr_multiaddr`

```c
struct net_in_addr net_ip_mreq::imr_multiaddr
```

IP 多播组地址（IP multicast group address）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 99.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [net_in_addr](P096_net_in_addr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P098_net_iovec_结构体.md) · [返回大纲](大纲.md) · [下一章](P100_net_ip_mreqn_结构体.md)
