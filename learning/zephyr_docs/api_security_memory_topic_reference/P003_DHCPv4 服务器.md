---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-3
title: DHCPv4 服务器
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_DHCPv4 服务器

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DHCPv4 服务器

<a id="details"></a>

DHCPv4 服务器（Server）。**引入版本（Since）：**3.6。**版本（Version）：**0.8.0。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.1\_类型定义（Typedefs）

<a id="r_gabd37fd84bc25525d4f1aec4df8aef8b6"></a>

```c
typedef void(* net_dhcpv4_lease_cb_t) (struct net_if *iface, struct dhcpv4_addr_slot *lease, void *user_data)
```

相关声明：[net_dhcpv4_lease_cb_t](#gabd37fd84bc25525d4f1aec4df8aef8b6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

遍历有效 DHCPv4 地址租约（Address Leases）时使用的回调。

<a id="r_ga4a35c423ca86cb324e983d07f6181691"></a>

```c
typedef int(* net_dhcpv4_server_provider_cb_t) (struct net_if *iface, const struct dhcpv4_client_id *client_id, struct net_in_addr *addr, void *user_data)
```

相关声明：[net_dhcpv4_server_provider_cb_t](#ga4a35c423ca86cb324e983d07f6181691)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

让应用程序为指定客户端标识（Client ID）提供地址的回调。

<a id="r_gac2ff21f144101fb00a87be4ca6f6301e"></a>

```c
typedef bool(* net_dhcpv4_server_address_validator_cb_t) (struct net_if *iface, const struct dhcpv4_client_id *client_id, const struct net_in_addr *addr, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_dhcpv4_server_address_validator_cb_t](#gac2ff21f144101fb00a87be4ca6f6301e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

让应用程序接受或拒绝拟议 DHCP 地址的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.2\_函数（Functions）

<a id="r_ga1a56f6dbb4c900e9d5c25cc9c04acac5"></a>

```c
int net_dhcpv4_server_start (struct net_if *iface, struct net_in_addr *base_addr)
```

相关声明：[net_dhcpv4_server_start](#ga1a56f6dbb4c900e9d5c25cc9c04acac5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

在网络接口（Interface）上启动 DHCPv4 服务器实例。

<a id="r_ga7955e5f3ff357c292a8641c0385f34e4"></a>

```c
int net_dhcpv4_server_stop (struct net_if *iface)
```

相关声明：[net_dhcpv4_server_stop](#ga7955e5f3ff357c292a8641c0385f34e4)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

停止网络接口（Interface）上的 DHCPv4 服务器实例。

<a id="r_ga636b2c71a7d5f00997cba946c31c0c00"></a>

```c
int net_dhcpv4_server_foreach_lease (struct net_if *iface, net_dhcpv4_lease_cb_t cb, void *user_data)
```

相关声明：[net_dhcpv4_server_foreach_lease](#ga636b2c71a7d5f00997cba946c31c0c00)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_dhcpv4_lease_cb_t](#gabd37fd84bc25525d4f1aec4df8aef8b6)。

遍历指定网络接口上的所有 DHCPv4 地址租约（Address Leases），并对每个租约调用回调。

<a id="r_ga1db06c0bf6a5f79334c81472b0a37bb7"></a>

```c
void net_dhcpv4_server_set_provider_cb (net_dhcpv4_server_provider_cb_t cb, void *user_data)
```

相关声明：[net_dhcpv4_server_set_provider_cb](#ga1db06c0bf6a5f79334c81472b0a37bb7)、[net_dhcpv4_server_provider_cb_t](#ga4a35c423ca86cb324e983d07f6181691)。

设置向 DHCP 服务器提供地址的回调。

<a id="r_ga240c9c47957ea66ba88cc2945f295e11"></a>

```c
void net_dhcpv4_server_set_address_validator_cb (net_dhcpv4_server_address_validator_cb_t cb, void *user_data)
```

相关声明：[net_dhcpv4_server_set_address_validator_cb](#ga240c9c47957ea66ba88cc2945f295e11)、[net_dhcpv4_server_address_validator_cb_t](#gac2ff21f144101fb00a87be4ca6f6301e)。

设置为 DHCP 服务器验证新地址的回调。

## 3.3\_详细说明（Detailed Documentation）

<a id="gabd37fd84bc25525d4f1aec4df8aef8b6"></a>

### `net_dhcpv4_lease_cb_t`

```c
typedef void(* net_dhcpv4_lease_cb_t) (struct net_if *iface, struct dhcpv4_addr_slot *lease, void *user_data)
```

```c
#include <zephyr/net/dhcpv4_server.h>
```

遍历有效 DHCPv4 地址租约（Address Leases）时使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（Network Interface）的指针。 |
| `lease` | 指向 DHCPv4 地址租约槽（Address Lease Slot）的指针。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="gac2ff21f144101fb00a87be4ca6f6301e"></a>

### `net_dhcpv4_server_address_validator_cb_t`

```c
typedef bool(* net_dhcpv4_server_address_validator_cb_t) (struct net_if *iface, const struct dhcpv4_client_id *client_id, const struct net_in_addr *addr, void *user_data)
```

```c
#include <zephyr/net/dhcpv4_server.h>
```

让应用程序接受或拒绝拟议 DHCP 地址的回调。

在接受拟分配给客户端的地址之前调用，使应用程序可以拒绝给指定客户端使用该地址。若回调返回 0，`addr` 必须为有效地址，并将分配给客户端；若返回任何非零值，则从地址池（Address Pool）为客户端分配地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（Network Interface）的指针。 |
| `client_id` | 指向请求该地址的客户端的指针。 |
| `addr` | 要分配给客户端的地址（Address）。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="ga4a35c423ca86cb324e983d07f6181691"></a>

### `net_dhcpv4_server_provider_cb_t`

```c
typedef int(* net_dhcpv4_server_provider_cb_t) (struct net_if *iface, const struct dhcpv4_client_id *client_id, struct net_in_addr *addr, void *user_data)
```

```c
#include <zephyr/net/dhcpv4_server.h>
```

让应用程序为指定客户端标识（Client ID）提供地址的回调。

在给客户端分配地址之前调用，使应用程序可以覆盖指定客户端的地址。若回调返回 0，`addr` 必须为有效地址，并将分配给客户端；若返回任何非零值，则从地址池（Address Pool）为客户端分配地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（Network Interface）的指针。 |
| `client_id` | 指向请求地址的客户端的指针。 |
| `addr` | 要分配给客户端的地址（Address）。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="ga636b2c71a7d5f00997cba946c31c0c00"></a>

### `net_dhcpv4_server_foreach_lease()`

```c
int net_dhcpv4_server_foreach_lease ( struct net_if * iface, net_dhcpv4_lease_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/dhcpv4_server.h>
```

遍历指定网络接口上的所有 DHCPv4 地址租约（Address Leases），并对每个租约调用回调。

若不提供网络接口，即接口指针为 `NULL`，则遍历所有运行 DHCPv4 服务器实例的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口的指针，可以为 `NULL`。 |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负错误码。

<a id="ga240c9c47957ea66ba88cc2945f295e11"></a>

### `net_dhcpv4_server_set_address_validator_cb()`

```c
void net_dhcpv4_server_set_address_validator_cb ( net_dhcpv4_server_address_validator_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/dhcpv4_server.h>
```

设置为 DHCP 服务器验证新地址的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="ga1db06c0bf6a5f79334c81472b0a37bb7"></a>

### `net_dhcpv4_server_set_provider_cb()`

```c
void net_dhcpv4_server_set_provider_cb ( net_dhcpv4_server_provider_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/dhcpv4_server.h>
```

设置向 DHCP 服务器提供地址的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="ga1a56f6dbb4c900e9d5c25cc9c04acac5"></a>

### `net_dhcpv4_server_start()`

```c
int net_dhcpv4_server_start ( struct net_if * iface, struct net_in_addr * base_addr )
```

```c
#include <zephyr/net/dhcpv4_server.h>
```

在网络接口（Interface）上启动 DHCPv4 服务器实例。

在指定接口上启动 DHCPv4 服务器。服务器开始监听该接口上的 DHCPv4 Discover／Request 消息，并相应地从配置的地址池（Address Pool）分配 IPv4 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向接口（Interface）的有效指针。 |
| `base_addr` | DHCPv4 地址池中的第一个 IPv4 地址。池中的地址数量通过 Kconfig 选项 `CONFIG_NET_DHCPV4_SERVER_ADDR_COUNT` 静态配置。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负错误码。

<a id="ga7955e5f3ff357c292a8641c0385f34e4"></a>

### `net_dhcpv4_server_stop()`

```c
int net_dhcpv4_server_stop ( struct net_if * iface)
```

```c
#include <zephyr/net/dhcpv4_server.h>
```

停止网络接口（Interface）上的 DHCPv4 服务器实例。

停止指定接口上的 DHCPv4 服务器。此后不再处理该接口上的 DHCPv4 请求，并清除所有地址分配记录（Allocations）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向接口（Interface）的有效指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负错误码。


## 3.4\_原页交叉引用（Cross References）

- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/net/dhcpv4_server.h](../api_file_service_interface_reference/P015_zephyr__net__dhcpv4_server.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_CoAP的受限RESTful环境对象安全（OSCORE）API。.md) · [返回大纲](大纲.md) · [下一章](P004_Intel I_O APIC中断控制器（Interrupt Controller）.md)
