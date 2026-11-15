---
id: learning.zephyr-docs.network-core-model-reference.page-72
title: net_event_l4_hostname_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__l4__hostname.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_net\_event\_l4\_hostname\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__l4__hostname.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_HOSTNAME_CHANGED事件的信息。

```c
#include <zephyr/net/net_event.h>
```

<a id="details"></a>

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_HOSTNAME_CHANGED事件的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_a8e04c33dfb1c251a0deaa29081283245"></a>

```c
char hostname [NET_HOSTNAME_SIZE]
```

相关声明：[hostname](#a8e04c33dfb1c251a0deaa29081283245)。

新主机名（Hostname）。

## 72.2\_详细说明（Detailed Documentation）

<a id="a8e04c33dfb1c251a0deaa29081283245"></a>

### `hostname`

```c
char net_event_l4_hostname::hostname[NET_HOSTNAME_SIZE]
```

新主机名（Hostname）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_event.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_net_event_ipv6_route_结构体.md) · [返回大纲](大纲.md) · [下一章](P073_net_event_packet_mcast_结构体.md)
