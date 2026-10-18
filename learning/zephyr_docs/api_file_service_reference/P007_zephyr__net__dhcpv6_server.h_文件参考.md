---
id: learning.zephyr-docs.api-file-service-reference.page-7
title: zephyr__net__dhcpv6_server.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6__server_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_net\_\_dhcpv6\_server.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6__server_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DHCPv6服务器（Server），支持RFC 8415规定的前缀委派（Prefix Delegation）。

<a id="details"></a>

```c
#include <zephyr/net/net_ip.h>
```

查看此文件的源码。

DHCPv6服务器（Server），支持RFC 8415规定的前缀委派（Prefix Delegation）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_net_5Fdhcpv6_5Fserver_5Fparams"></a>

```c
struct net_dhcpv6_server_params
```

相关声明：[net_dhcpv6_server_params](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md)。

DHCPv6服务器（Server）的配置参数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.2\_类型定义（Typedefs）

<a id="r_ga86f2ef89515d47d8ba4fe9b45da1eca9"></a>

```c
typedef void(* net_dhcpv6_server_lease_cb_t) (struct net_if *iface, struct net_dhcpv6_server_lease *lease, void *user_data)
```

相关声明：[net_dhcpv6_server_lease_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#ga86f2ef89515d47d8ba4fe9b45da1eca9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

遍历 DHCPv6 服务器租约（Server Leases）时使用的回调（Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_ga5fdf013a85ca7701ad92c8f50c1b0ed0"></a>

```c
int net_dhcpv6_server_start (struct net_if *iface, struct net_dhcpv6_server_params *params)
```

相关声明：[net_dhcpv6_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#ga5fdf013a85ca7701ad92c8f50c1b0ed0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_dhcpv6_server_params](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md)。

在给定接口（Interface）上启动 DHCPv6 服务器（Server）。

<a id="r_gae090b9103bc0110eca408d3a3989c574"></a>

```c
int net_dhcpv6_server_stop (struct net_if *iface)
```

相关声明：[net_dhcpv6_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#gae090b9103bc0110eca408d3a3989c574)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

停止给定接口（Interface）上的 DHCPv6 服务器（Server）。

<a id="r_gaaedb437385fa27b8454bfc670ff9aa71"></a>

```c
int net_dhcpv6_server_foreach_lease (struct net_if *iface, net_dhcpv6_server_lease_cb_t cb, void *user_data)
```

相关声明：[net_dhcpv6_server_foreach_lease](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#gaaedb437385fa27b8454bfc670ff9aa71)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_dhcpv6_server_lease_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#ga86f2ef89515d47d8ba4fe9b45da1eca9)。

遍历所有 DHCPv6 服务器租约（Server Leases），并为每个租约调用 `cb`。


## 7.4\_原页交叉引用（Cross References）

- [RFC 8415](https://datatracker.ietf.org/doc/html/rfc8415)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P131_dhcpv6_server.h_源码浏览.md)
- [net_dhcpv6_server_params](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md)
- [net_dhcpv6_server_lease_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#ga86f2ef89515d47d8ba4fe9b45da1eca9)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_dhcpv6_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#ga5fdf013a85ca7701ad92c8f50c1b0ed0)
- [net_dhcpv6_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#gae090b9103bc0110eca408d3a3989c574)
- [net_dhcpv6_server_foreach_lease](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#gaaedb437385fa27b8454bfc670ff9aa71)

<a id="header-details"></a>

---

[上一章](P006_zephyr__bluetooth__mesh__dfu.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__dt-bindings__mipi_dsi__mipi_dsi.h_文件参考.md)
