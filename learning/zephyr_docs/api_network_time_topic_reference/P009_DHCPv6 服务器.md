---
id: learning.zephyr-docs.api-network-time-topic-reference.page-9
title: DHCPv6 服务器
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_DHCPv6 服务器

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DHCPv6 服务器

<a id="details"></a>

IPv6 动态主机配置协议（DHCPv6）服务器。自 Zephyr 4.5 起提供；API 版本为 0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_net_5Fdhcpv6_5Fserver_5Fparams"></a>

```c
struct net_dhcpv6_server_params
```

相关声明：[net_dhcpv6_server_params](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md)。

DHCPv6服务器（Server）的配置参数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.2\_类型定义（Typedefs）

<a id="r_ga86f2ef89515d47d8ba4fe9b45da1eca9"></a>

```c
typedef void(* net_dhcpv6_server_lease_cb_t) (struct net_if *iface, struct net_dhcpv6_server_lease *lease, void *user_data)
```

相关声明：[net_dhcpv6_server_lease_cb_t](#ga86f2ef89515d47d8ba4fe9b45da1eca9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

遍历 DHCPv6 服务器租约（Server Leases）时使用的回调（Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.3\_函数（Functions）

<a id="r_ga5fdf013a85ca7701ad92c8f50c1b0ed0"></a>

```c
int net_dhcpv6_server_start (struct net_if *iface, struct net_dhcpv6_server_params *params)
```

相关声明：[net_dhcpv6_server_start](#ga5fdf013a85ca7701ad92c8f50c1b0ed0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_dhcpv6_server_params](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md)。

在给定接口（Interface）上启动 DHCPv6 服务器（Server）。

<a id="r_gae090b9103bc0110eca408d3a3989c574"></a>

```c
int net_dhcpv6_server_stop (struct net_if *iface)
```

相关声明：[net_dhcpv6_server_stop](#gae090b9103bc0110eca408d3a3989c574)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

停止给定接口（Interface）上的 DHCPv6 服务器（Server）。

<a id="r_gaaedb437385fa27b8454bfc670ff9aa71"></a>

```c
int net_dhcpv6_server_foreach_lease (struct net_if *iface, net_dhcpv6_server_lease_cb_t cb, void *user_data)
```

相关声明：[net_dhcpv6_server_foreach_lease](#gaaedb437385fa27b8454bfc670ff9aa71)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_dhcpv6_server_lease_cb_t](#ga86f2ef89515d47d8ba4fe9b45da1eca9)。

遍历所有 DHCPv6 服务器租约（Server Leases），并为每个租约调用 `cb`。

## 9.4\_详细说明（Detailed Documentation）

<a id="ga86f2ef89515d47d8ba4fe9b45da1eca9"></a>

### `net_dhcpv6_server_lease_cb_t`

```c
typedef void(* net_dhcpv6_server_lease_cb_t) (struct net_if *iface, struct net_dhcpv6_server_lease *lease, void *user_data)
```

```c
#include <zephyr/net/dhcpv6_server.h>
```

遍历 DHCPv6 服务器租约（Server Leases）时使用的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向租约（lease）所属网络接口的指针。 |
| `lease` | 指向 DHCPv6 服务器租约的指针。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="gaaedb437385fa27b8454bfc670ff9aa71"></a>

### `net_dhcpv6_server_foreach_lease()`

```c
int net_dhcpv6_server_foreach_lease ( struct net_if * iface, net_dhcpv6_server_lease_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/dhcpv6_server.h>
```

遍历所有 DHCPv6 服务器租约（Server Leases），并为每个租约调用 `cb`。

`iface` 为 `NULL` 时，遍历所有正在运行的服务器实例的租约；否则仅遍历 `iface` 上运行的服务器的租约。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口的指针，可以为 `NULL`。 |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

**返回（Returns）**：返回值：成功时返回 0；`iface` 上没有运行中的服务器时返回 `-ENOENT`；其他情况返回负 `errno` 值。

<a id="ga5fdf013a85ca7701ad92c8f50c1b0ed0"></a>

### `net_dhcpv6_server_start()`

```c
int net_dhcpv6_server_start ( struct net_if * iface, struct net_dhcpv6_server_params * params )
```

```c
#include <zephyr/net/dhcpv6_server.h>
```

在给定接口（Interface）上启动 DHCPv6 服务器（Server）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的有效指针。 |
| `params` | 服务器配置参数，会被复制。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="gae090b9103bc0110eca408d3a3989c574"></a>

### `net_dhcpv6_server_stop()`

```c
int net_dhcpv6_server_stop ( struct net_if * iface)
```

```c
#include <zephyr/net/dhcpv6_server.h>
```

停止给定接口（Interface）上的 DHCPv6 服务器（Server）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的有效指针。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。


## 9.5\_原页交叉引用（Cross References）

- [net_dhcpv6_server_params](../network_core_model_reference/P057_net_dhcpv6_server_params_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [zephyr/net/dhcpv6_server.h](../api_file_service_reference/P007_zephyr__net__dhcpv6_server.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_调试访问端口链路（DAP Link）.md) · [返回大纲](大纲.md) · [下一章](P010_eSPI SAF 驱动后端 API（Driver Backend API）.md)
