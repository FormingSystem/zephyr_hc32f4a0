---
id: learning.zephyr-docs.network-core-model-reference.page-77
title: net_icmp_offload_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__icmp__offload.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_net\_icmp\_offload\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__icmp__offload.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

互联网控制消息协议（ICMP）的卸载上下文（Offload Context）结构。

```c
#include <zephyr/net/icmp.h>
```

<a id="details"></a>

互联网控制消息协议（ICMP）的卸载上下文（Offload Context）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 77.1\_数据成员（Data Fields）

<a id="r_ae31036c45fac89b321fe2c62c06be0b3"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#ae31036c45fac89b321fe2c62c06be0b3)。

列表节点（List Node）。

<a id="r_aad5c9913e8bf68a7453bc773c5784772"></a>

```c
net_icmp_handler_t handler
```

相关声明：[net_icmp_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga35da387f482e5da0c944bbfa349c3ea2)、[handler](#aad5c9913e8bf68a7453bc773c5784772)。

互联网控制消息协议（ICMP）的响应处理程序。

<a id="r_ae28f8f6a0e15271b1f00b10abecdfc3e"></a>

```c
net_icmp_offload_ping_handler_t ping_handler
```

相关声明：[net_icmp_offload_ping_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gad85b780080117bf3b53c5623f962ea71)、[ping_handler](#ae28f8f6a0e15271b1f00b10abecdfc3e)。

ICMP卸载式ping处理程序（Offloaded Ping Handler）。

<a id="r_aeffe11b4701e58532e44b4cff37be680"></a>

```c
struct net_if * iface
```

相关声明：[net_if](P079_net_if_结构体.md)、[iface](#aeffe11b4701e58532e44b4cff37be680)。

卸载式网络接口（Offloaded Network Interface）。

## 77.2\_详细说明（Detailed Documentation）

<a id="aad5c9913e8bf68a7453bc773c5784772"></a>

### `handler`

```c
net_icmp_handler_t net_icmp_offload::handler
```

互联网控制消息协议（ICMP）的响应处理程序。

目前仅有一个处理程序（Handler），因此同一时刻只能进行一次卸载式ping请求/响应。

<a id="aeffe11b4701e58532e44b4cff37be680"></a>

### `iface`

```c
struct net_if* net_icmp_offload::iface
```

卸载式网络接口（Offloaded Network Interface）。

<a id="ae31036c45fac89b321fe2c62c06be0b3"></a>

### `node`

```c
sys_snode_t net_icmp_offload::node
```

列表节点（List Node）。

<a id="ae28f8f6a0e15271b1f00b10abecdfc3e"></a>

### `ping_handler`

```c
net_icmp_offload_ping_handler_t net_icmp_offload::ping_handler
```

ICMP卸载式ping处理程序（Offloaded Ping Handler）。

本数据类型文档由以下文件生成：

- `zephyr/net/icmp.h`

## 77.3\_原页交叉引用（Cross References）

- [zephyr/net/icmp.h](https://docs.zephyrproject.org/latest/doxygen/html/icmp_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [net_icmp_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga35da387f482e5da0c944bbfa349c3ea2)
- [net_icmp_offload_ping_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gad85b780080117bf3b53c5623f962ea71)
- [net_if](P079_net_if_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P076_net_icmp_ip_hdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P078_net_icmp_ping_params_结构体.md)
