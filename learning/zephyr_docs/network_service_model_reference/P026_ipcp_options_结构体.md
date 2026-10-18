---
id: learning.zephyr-docs.network-service-model-reference.page-26
title: ipcp_options_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structipcp__options.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_ipcp\_options\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structipcp__options.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv4控制协议（Control Protocol）的选项。

```c
#include <zephyr/net/ppp.h>
```

<a id="details"></a>

IPv4控制协议（Control Protocol）的选项。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_a703bfd73411418a54e1c769f814f3531"></a>

```c
struct net_in_addr address
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[address](#a703bfd73411418a54e1c769f814f3531)。

IPv4地址（Address）。

<a id="r_a558db348a124a5a5489b5ca3181ba52e"></a>

```c
struct net_in_addr dns1_address
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[dns1_address](#a558db348a124a5a5489b5ca3181ba52e)。

主 DNS 服务器地址。

<a id="r_a3026cdd5c023b9f1d584e12f9c6e362d"></a>

```c
struct net_in_addr dns2_address
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[dns2_address](#a3026cdd5c023b9f1d584e12f9c6e362d)。

备用 DNS 服务器地址。

## 26.2\_详细说明（Detailed Documentation）

<a id="a703bfd73411418a54e1c769f814f3531"></a>

### `address`

```c
struct net_in_addr ipcp_options::address
```

IPv4地址（Address）。

<a id="a558db348a124a5a5489b5ca3181ba52e"></a>

### `dns1_address`

```c
struct net_in_addr ipcp_options::dns1_address
```

主 DNS 服务器地址。

<a id="a3026cdd5c023b9f1d584e12f9c6e362d"></a>

### `dns2_address`

```c
struct net_in_addr ipcp_options::dns2_address
```

备用 DNS 服务器地址。

本数据类型文档由以下文件生成：

- `zephyr/net/ppp.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/net/ppp.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h_source.html)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_igmp_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_ipv6cp_options_结构体.md)
