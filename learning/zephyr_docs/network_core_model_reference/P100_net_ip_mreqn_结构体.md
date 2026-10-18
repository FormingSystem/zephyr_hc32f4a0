---
id: learning.zephyr-docs.network-core-model-reference.page-100
title: net_ip_mreqn_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__ip__mreqn.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_net\_ip\_mreqn\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__ip__mreqn.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

加入或离开IPv4组播组（Multicast Group）时使用的结构。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

加入或离开IPv4组播组（Multicast Group）时使用的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 100.1\_数据成员（Data Fields）

<a id="r_ac0ac21d6427ca1654eefe6fb903c4d99"></a>

```c
struct net_in_addr imr_multiaddr
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[imr_multiaddr](#ac0ac21d6427ca1654eefe6fb903c4d99)。

IP 多播组地址（IP multicast group address）。

<a id="r_abb6dbf4f2aae8fe0e3fc4ec5b6d0fdf8"></a>

```c
struct net_in_addr imr_address
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[imr_address](#abb6dbf4f2aae8fe0e3fc4ec5b6d0fdf8)。

本地接口的 IP 地址（IP address of local interface）。

<a id="r_a3d89352335683bfcda267b47c591ba1f"></a>

```c
int imr_ifindex
```

相关声明：[imr_ifindex](#a3d89352335683bfcda267b47c591ba1f)。

网络接口索引（Network interface index）。

## 100.2\_详细说明（Detailed Documentation）

<a id="abb6dbf4f2aae8fe0e3fc4ec5b6d0fdf8"></a>

### `imr_address`

```c
struct net_in_addr net_ip_mreqn::imr_address
```

本地接口的 IP 地址（IP address of local interface）。

<a id="a3d89352335683bfcda267b47c591ba1f"></a>

### `imr_ifindex`

```c
int net_ip_mreqn::imr_ifindex
```

网络接口索引（Network interface index）。

<a id="ac0ac21d6427ca1654eefe6fb903c4d99"></a>

### `imr_multiaddr`

```c
struct net_in_addr net_ip_mreqn::imr_multiaddr
```

IP 多播组地址（IP multicast group address）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 100.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [net_in_addr](P096_net_in_addr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P099_net_ip_mreq_结构体.md) · [返回大纲](大纲.md) · [下一章](P101_net_iptable_rule_params_结构体.md)
