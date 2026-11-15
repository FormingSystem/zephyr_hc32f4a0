---
id: learning.zephyr-docs.network-core-model-reference.page-81
title: net_if_addr_ipv4_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__addr__ipv4.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_net\_if\_addr\_ipv4\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__addr__ipv4.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络接口的单播IPv4地址及网络掩码（Netmask）。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

网络接口单播 IPv4 地址及网络掩码（Network Interface unicast IPv4 address and netmask）。保存单播 IPv4 地址及其对应的网络掩码。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 81.1\_数据成员（Data Fields）

<a id="r_a9d8924e263cc7401569c934533a04b48"></a>

```c
struct net_if_addr ipv4
```

相关声明：[net_if_addr](P080_net_if_addr_结构体.md)、[ipv4](#a9d8924e263cc7401569c934533a04b48)。

IPv4地址（Address）。

<a id="r_a6fac9f57d9689f9925938940db8748b7"></a>

```c
struct net_in_addr netmask
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[netmask](#a6fac9f57d9689f9925938940db8748b7)。

网络掩码（Netmask）。

## 81.2\_详细说明（Detailed Documentation）

<a id="a9d8924e263cc7401569c934533a04b48"></a>

### `ipv4`

```c
struct net_if_addr net_if_addr_ipv4::ipv4
```

IPv4地址（Address）。

<a id="a6fac9f57d9689f9925938940db8748b7"></a>

### `netmask`

```c
struct net_in_addr net_if_addr_ipv4::netmask
```

网络掩码（Netmask）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 81.3\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [net_if_addr](P080_net_if_addr_结构体.md)
- [net_in_addr](P096_net_in_addr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P080_net_if_addr_结构体.md) · [返回大纲](大纲.md) · [下一章](P082_net_if_config_结构体.md)
