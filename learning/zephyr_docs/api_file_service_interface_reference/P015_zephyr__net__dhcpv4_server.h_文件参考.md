---
id: learning.zephyr-docs.api-file-service-interface-reference.page-15
title: zephyr__net__dhcpv4_server.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4__server_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_net\_\_dhcpv4\_server.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv4__server_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DHCPv4服务器（Server）的API。

<a id="details"></a>

```c
#include <zephyr/net/net_ip.h>
#include <zephyr/sys/clock.h>
```

查看此文件的源码。

DHCPv4服务器（Server）的API。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.1\_类型定义（Typedefs）

<a id="r_gabd37fd84bc25525d4f1aec4df8aef8b6"></a>

```c
typedef void(* net_dhcpv4_lease_cb_t) (struct net_if *iface, struct dhcpv4_addr_slot *lease, void *user_data)
```

相关声明：[net_dhcpv4_lease_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#gabd37fd84bc25525d4f1aec4df8aef8b6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

遍历有效 DHCPv4 地址租约（Address Leases）时使用的回调。

<a id="r_ga4a35c423ca86cb324e983d07f6181691"></a>

```c
typedef int(* net_dhcpv4_server_provider_cb_t) (struct net_if *iface, const struct dhcpv4_client_id *client_id, struct net_in_addr *addr, void *user_data)
```

相关声明：[net_dhcpv4_server_provider_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga4a35c423ca86cb324e983d07f6181691)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

让应用程序为指定客户端标识（Client ID）提供地址的回调。

<a id="r_gac2ff21f144101fb00a87be4ca6f6301e"></a>

```c
typedef bool(* net_dhcpv4_server_address_validator_cb_t) (struct net_if *iface, const struct dhcpv4_client_id *client_id, const struct net_in_addr *addr, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_dhcpv4_server_address_validator_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#gac2ff21f144101fb00a87be4ca6f6301e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

让应用程序接受或拒绝拟议 DHCP 地址的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.2\_函数（Functions）

<a id="r_ga1a56f6dbb4c900e9d5c25cc9c04acac5"></a>

```c
int net_dhcpv4_server_start (struct net_if *iface, struct net_in_addr *base_addr)
```

相关声明：[net_dhcpv4_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga1a56f6dbb4c900e9d5c25cc9c04acac5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

在网络接口（Interface）上启动 DHCPv4 服务器实例。

<a id="r_ga7955e5f3ff357c292a8641c0385f34e4"></a>

```c
int net_dhcpv4_server_stop (struct net_if *iface)
```

相关声明：[net_dhcpv4_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga7955e5f3ff357c292a8641c0385f34e4)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

停止网络接口（Interface）上的 DHCPv4 服务器实例。

<a id="r_ga636b2c71a7d5f00997cba946c31c0c00"></a>

```c
int net_dhcpv4_server_foreach_lease (struct net_if *iface, net_dhcpv4_lease_cb_t cb, void *user_data)
```

相关声明：[net_dhcpv4_server_foreach_lease](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga636b2c71a7d5f00997cba946c31c0c00)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_dhcpv4_lease_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#gabd37fd84bc25525d4f1aec4df8aef8b6)。

遍历指定网络接口上的所有 DHCPv4 地址租约（Address Leases），并对每个租约调用回调。

<a id="r_ga1db06c0bf6a5f79334c81472b0a37bb7"></a>

```c
void net_dhcpv4_server_set_provider_cb (net_dhcpv4_server_provider_cb_t cb, void *user_data)
```

相关声明：[net_dhcpv4_server_set_provider_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga1db06c0bf6a5f79334c81472b0a37bb7)、[net_dhcpv4_server_provider_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga4a35c423ca86cb324e983d07f6181691)。

设置向 DHCP 服务器提供地址的回调。

<a id="r_ga240c9c47957ea66ba88cc2945f295e11"></a>

```c
void net_dhcpv4_server_set_address_validator_cb (net_dhcpv4_server_address_validator_cb_t cb, void *user_data)
```

相关声明：[net_dhcpv4_server_set_address_validator_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga240c9c47957ea66ba88cc2945f295e11)、[net_dhcpv4_server_address_validator_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#gac2ff21f144101fb00a87be4ca6f6301e)。

设置为 DHCP 服务器验证新地址的回调。


## 15.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P129_dhcpv4_server.h_源码浏览.md)
- [net_dhcpv4_lease_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#gabd37fd84bc25525d4f1aec4df8aef8b6)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_dhcpv4_server_provider_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga4a35c423ca86cb324e983d07f6181691)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_dhcpv4_server_address_validator_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#gac2ff21f144101fb00a87be4ca6f6301e)
- [net_dhcpv4_server_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga1a56f6dbb4c900e9d5c25cc9c04acac5)
- [net_dhcpv4_server_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga7955e5f3ff357c292a8641c0385f34e4)
- [net_dhcpv4_server_foreach_lease](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga636b2c71a7d5f00997cba946c31c0c00)
- [net_dhcpv4_server_set_provider_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga1db06c0bf6a5f79334c81472b0a37bb7)
- [net_dhcpv4_server_set_address_validator_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga240c9c47957ea66ba88cc2945f295e11)

<a id="header-details"></a>

---

[上一章](P014_zephyr__bluetooth__mesh__dfu_srv.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__dt-bindings__gpio__dvp-20pin-connector.h_文件参考.md)
