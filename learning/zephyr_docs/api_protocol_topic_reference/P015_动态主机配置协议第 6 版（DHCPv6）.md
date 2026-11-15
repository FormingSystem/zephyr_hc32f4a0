---
id: learning.zephyr-docs.api-protocol-topic-reference.page-15
title: 动态主机配置协议第 6 版（DHCPv6）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_动态主机配置协议第 6 版（DHCPv6）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

动态主机配置协议第 6 版（DHCPv6）

<a id="details"></a>

IPv6 动态主机配置协议（DHCPv6）。自 Zephyr 3.5 起提供；API 版本为 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_net_5Fdhcpv6_5Fparams"></a>

```c
struct net_dhcpv6_params
```

相关声明：[net_dhcpv6_params](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md)。

DHCPv6客户端（Client）的配置参数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.2\_函数（Functions）

<a id="r_gab607a476c947d0335a254304e5dc2a24"></a>

```c
void net_dhcpv6_start (struct net_if *iface, struct net_dhcpv6_params *params)
```

相关声明：[net_dhcpv6_start](#gab607a476c947d0335a254304e5dc2a24)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_dhcpv6_params](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md)。

在接口（Interface，`iface`）上启动 DHCPv6 客户端（Client）。

<a id="r_gaf0b903bdcd0becf06ed6b212c74097a0"></a>

```c
void net_dhcpv6_stop (struct net_if *iface)
```

相关声明：[net_dhcpv6_stop](#gaf0b903bdcd0becf06ed6b212c74097a0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

停止接口（Interface，`iface`）上的 DHCPv6 客户端（Client）。

<a id="r_ga99642b89c14cb17f35b45a03a2286441"></a>

```c
void net_dhcpv6_restart (struct net_if *iface)
```

相关声明：[net_dhcpv6_restart](#ga99642b89c14cb17f35b45a03a2286441)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

重新启动接口（Interface，`iface`）上的 DHCPv6 客户端（Client）。

## 15.3\_详细说明（Detailed Documentation）

<a id="ga99642b89c14cb17f35b45a03a2286441"></a>

### `net_dhcpv6_restart()`

```c
void net_dhcpv6_restart ( struct net_if * iface)
```

```c
#include <zephyr/net/dhcpv6.h>
```

重新启动接口（Interface，`iface`）上的 DHCPv6 客户端（Client）。

在指定接口上重新启动 DHCPv6 客户端。客户端会重新启动状态机（state machine），不执行任何初始延迟。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的有效指针。 |

<a id="gab607a476c947d0335a254304e5dc2a24"></a>

### `net_dhcpv6_start()`

```c
void net_dhcpv6_start ( struct net_if * iface, struct net_dhcpv6_params * params )
```

```c
#include <zephyr/net/dhcpv6.h>
```

在接口（Interface，`iface`）上启动 DHCPv6 客户端（Client）。

在指定接口上启动 DHCPv6 客户端。客户端根据配置开始协商 IPv6 地址和／或前缀（prefix）。协商完成后，会将 IPv6 地址／前缀详细信息添加到该接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的有效指针。 |
| `params` | DHCPv6客户端（Client）的配置参数。 |

<a id="gaf0b903bdcd0becf06ed6b212c74097a0"></a>

### `net_dhcpv6_stop()`

```c
void net_dhcpv6_stop ( struct net_if * iface)
```

```c
#include <zephyr/net/dhcpv6.h>
```

停止接口（Interface，`iface`）上的 DHCPv6 客户端（Client）。

在指定接口上停止 DHCPv6 客户端。客户端会从接口移除从 DHCP 服务器取得的全部配置，并停止与服务器进行后续协商。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的有效指针。 |


## 15.4\_原页交叉引用（Cross References）

- [net_dhcpv6_params](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [zephyr/net/dhcpv6.h](../api_file_runtime_reference/P009_zephyr__net__dhcpv6.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_瑞萨（Renesas）RZ 时钟生成电路（CGC）.md) · [返回大纲](大纲.md) · [下一章](P016_Infineon XMC4xxx中断控制器（Interrupt Controller）.md)
