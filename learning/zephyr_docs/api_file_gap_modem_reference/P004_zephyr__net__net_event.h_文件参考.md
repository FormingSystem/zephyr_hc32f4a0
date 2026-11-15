---
id: learning.zephyr-docs.api-file-gap-modem-reference.page-4
title: zephyr__net__net_event.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_net\_\_net\_event.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络事件代码（Network Events Code）的公共头文件。

<a id="details"></a>

```c
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_mgmt.h>
#include <zephyr/net/hostname.h>
```

查看此文件的源码。

网络事件代码（Network Events Code）的公共头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_net_5Fevent_5Fpacket_5Fmcast"></a>

```c
struct net_event_packet_mcast
```

相关声明：[net_event_packet_mcast](../network_core_model_reference/P073_net_event_packet_mcast_结构体.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD、NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP等网络事件的信息。

<a id="r_net_5Fevent_5Fipv6_5Faddr"></a>

```c
struct net_event_ipv6_addr
```

相关声明：[net_event_ipv6_addr](../network_core_model_reference/P066_net_event_ipv6_addr_结构体.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_ADDR_ADD、NET_EVENT_IPV6_ADDR_DEL、NET_EVENT_IPV6_MADDR_ADD、NET_EVENT_IPV6_MADDR_DEL等网络事件的信息。

<a id="r_net_5Fevent_5Fipv6_5Fnbr"></a>

```c
struct net_event_ipv6_nbr
```

相关声明：[net_event_ipv6_nbr](../network_core_model_reference/P067_net_event_ipv6_nbr_结构体.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_NBR_ADD、NET_EVENT_IPV6_NBR_DEL等网络事件的信息。

<a id="r_net_5Fevent_5Fipv6_5Froute"></a>

```c
struct net_event_ipv6_route
```

相关声明：[net_event_ipv6_route](../network_core_model_reference/P071_net_event_ipv6_route_结构体.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_ROUTE_ADD、NET_EVENT_IPV6_ROUTE_DEL等网络事件的信息。

<a id="r_net_5Fevent_5Fipv4_5Froute"></a>

```c
struct net_event_ipv4_route
```

相关声明：[net_event_ipv4_route](../network_core_model_reference/P065_net_event_ipv4_route_结构体.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV4_ROUTE_ADD、NET_EVENT_IPV4_ROUTE_DEL等网络事件的信息。

<a id="r_net_5Fevent_5Fipv6_5Fprefix"></a>

```c
struct net_event_ipv6_prefix
```

相关声明：[net_event_ipv6_prefix](../network_core_model_reference/P070_net_event_ipv6_prefix_结构体.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_PREFIX_ADD、NET_EVENT_IPV6_PREFIX_DEL等网络事件的信息。

<a id="r_net_5Fevent_5Fl4_5Fhostname"></a>

```c
struct net_event_l4_hostname
```

相关声明：[net_event_l4_hostname](../network_core_model_reference/P072_net_event_l4_hostname_结构体.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_HOSTNAME_CHANGED事件的信息。

<a id="r_net_5Fevent_5Fipv6_5Fpe_5Ffilter"></a>

```c
struct net_event_ipv6_pe_filter
```

相关声明：[net_event_ipv6_pe_filter](../network_core_model_reference/P068_net_event_ipv6_pe_filter_结构体.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_PE_FILTER_ADD、NET_EVENT_IPV6_PE_FILTER_DEL等网络事件的信息。

<a id="r_net_5Fevent_5Fipv4_5Fpmtu_5Finfo"></a>

```c
struct net_event_ipv4_pmtu_info
```

相关声明：[net_event_ipv4_pmtu_info](../network_core_model_reference/P064_net_event_ipv4_pmtu_info_结构体.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV4_PMTU_CHANGED网络事件的信息。

<a id="r_net_5Fevent_5Fipv6_5Fpmtu_5Finfo"></a>

```c
struct net_event_ipv6_pmtu_info
```

相关声明：[net_event_ipv6_pmtu_info](../network_core_model_reference/P069_net_event_ipv6_pmtu_info_结构体.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_IPV6_PMTU_CHANGED网络事件的信息。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_gac43a928bce3feb217b37ff7eb205e71b"></a>

```c
#define NET_EVENT_IF_DOWN (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_DOWN)
```

相关声明：[NET_EVENT_IF_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gac43a928bce3feb217b37ff7eb205e71b)。

网络接口转为停用（Down）状态时发出的事件。

<a id="r_gaddc84a60607bb27048397e29eb9107f5"></a>

```c
#define NET_EVENT_IF_UP (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_UP)
```

相关声明：[NET_EVENT_IF_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaddc84a60607bb27048397e29eb9107f5)。

网络接口转为启用（Up）状态时发出的事件。

<a id="r_gacb6ac7a4579be883abc9aa638299b0cd"></a>

```c
#define NET_EVENT_IF_ADMIN_DOWN (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_ADMIN_DOWN)
```

相关声明：[NET_EVENT_IF_ADMIN_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gacb6ac7a4579be883abc9aa638299b0cd)。

手动停用（Down）网络接口时发出的事件。

<a id="r_ga94a52eb94cc2189919ade9c8c8f239bd"></a>

```c
#define NET_EVENT_IF_ADMIN_UP (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_ADMIN_UP)
```

相关声明：[NET_EVENT_IF_ADMIN_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga94a52eb94cc2189919ade9c8c8f239bd)。

手动启用（Up）网络接口时发出的事件。

<a id="r_gabfb799347776323486fb0d4563e31b3b"></a>

```c
#define NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD (NET_EVENT_PACKET_BASE | NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_ADD)
```

相关声明：[NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gabfb799347776323486fb0d4563e31b3b)。

添加分组套接字（Packet Socket）的组播组成员资格（Multicast Group Membership）时发出的事件。

<a id="r_gaec5574f6308a89db36c2793bce6d5dcb"></a>

```c
#define NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP (NET_EVENT_PACKET_BASE | NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_DROP)
```

相关声明：[NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaec5574f6308a89db36c2793bce6d5dcb)。

移除分组套接字（Packet Socket）的组播组成员资格（Multicast Group Membership）时发出的事件。

<a id="r_ga20125c6148169a91fbebab1ebba17be3"></a>

```c
#define NET_EVENT_IPV6_ADDR_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_ADD)
```

相关声明：[NET_EVENT_IPV6_ADDR_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga20125c6148169a91fbebab1ebba17be3)。

向系统添加 IPv6 地址（Address）时发出的事件。

<a id="r_ga61f243efbc25928815ec78305b4f000e"></a>

```c
#define NET_EVENT_IPV6_ADDR_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_DEL)
```

相关声明：[NET_EVENT_IPV6_ADDR_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga61f243efbc25928815ec78305b4f000e)。

从系统移除 IPv6 地址（Address）时发出的事件。

<a id="r_gadda9dccf913a4dcb4d12b2b1fe5d403c"></a>

```c
#define NET_EVENT_IPV6_MADDR_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MADDR_ADD)
```

相关声明：[NET_EVENT_IPV6_MADDR_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gadda9dccf913a4dcb4d12b2b1fe5d403c)。

向系统添加 IPv6 组播地址（Multicast Address）时发出的事件。

<a id="r_ga035db32f66effd2407e0cca4b1fd9ea3"></a>

```c
#define NET_EVENT_IPV6_MADDR_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MADDR_DEL)
```

相关声明：[NET_EVENT_IPV6_MADDR_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga035db32f66effd2407e0cca4b1fd9ea3)。

从系统移除 IPv6 组播地址（Multicast Address）时发出的事件。

<a id="r_ga392414b95838bca1e55e4342870a8333"></a>

```c
#define NET_EVENT_IPV6_PREFIX_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PREFIX_ADD)
```

相关声明：[NET_EVENT_IPV6_PREFIX_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga392414b95838bca1e55e4342870a8333)。

向系统添加 IPv6 前缀（Prefix）时发出的事件。

<a id="r_gab06f93335938a635966e85a18b5b0cf6"></a>

```c
#define NET_EVENT_IPV6_PREFIX_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PREFIX_DEL)
```

相关声明：[NET_EVENT_IPV6_PREFIX_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gab06f93335938a635966e85a18b5b0cf6)。

从系统移除 IPv6 前缀（Prefix）时发出的事件。

<a id="r_ga287d37bae2d74e0c85de59c5e23d409a"></a>

```c
#define NET_EVENT_IPV6_MCAST_JOIN (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MCAST_JOIN)
```

相关声明：[NET_EVENT_IPV6_MCAST_JOIN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga287d37bae2d74e0c85de59c5e23d409a)。

加入 IPv6 组播组（Multicast Group）时发出的事件。

<a id="r_ga862d1b2ce9b65c0806ef77909364a58d"></a>

```c
#define NET_EVENT_IPV6_MCAST_LEAVE (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MCAST_LEAVE)
```

相关声明：[NET_EVENT_IPV6_MCAST_LEAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga862d1b2ce9b65c0806ef77909364a58d)。

离开 IPv6 组播组（Multicast Group）时发出的事件。

<a id="r_gaae932293528aa40127a906c3dbd45e31"></a>

```c
#define NET_EVENT_IPV6_ROUTER_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTER_ADD)
```

相关声明：[NET_EVENT_IPV6_ROUTER_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaae932293528aa40127a906c3dbd45e31)。

向系统添加 IPv6 路由器（Router）时发出的事件。

<a id="r_ga8d4b7798981aaaf3aea2b793739143b7"></a>

```c
#define NET_EVENT_IPV6_ROUTER_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTER_DEL)
```

相关声明：[NET_EVENT_IPV6_ROUTER_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga8d4b7798981aaaf3aea2b793739143b7)。

从系统移除 IPv6 路由器（Router）时发出的事件。

<a id="r_gad19b5e742ded9b3ed673d8f7985100fd"></a>

```c
#define NET_EVENT_IPV6_ROUTE_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTE_ADD)
```

相关声明：[NET_EVENT_IPV6_ROUTE_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gad19b5e742ded9b3ed673d8f7985100fd)。

向系统添加 IPv6 路由（Route）时发出的事件。

<a id="r_gae6f68ec69032ac049f072d6ed164987c"></a>

```c
#define NET_EVENT_IPV6_ROUTE_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTE_DEL)
```

相关声明：[NET_EVENT_IPV6_ROUTE_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gae6f68ec69032ac049f072d6ed164987c)。

从系统移除 IPv6 路由（Route）时发出的事件。

<a id="r_ga8711b4b1e88c897196b982e4d56968f1"></a>

```c
#define NET_EVENT_IPV6_DAD_SUCCEED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DAD_SUCCEED)
```

相关声明：[NET_EVENT_IPV6_DAD_SUCCEED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga8711b4b1e88c897196b982e4d56968f1)。

IPv6 重复地址检测（Duplicate Address Detection）成功时发出的事件。

<a id="r_ga0d5013ea3a6fa3bddd5cb182dd616151"></a>

```c
#define NET_EVENT_IPV6_DAD_FAILED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DAD_FAILED)
```

相关声明：[NET_EVENT_IPV6_DAD_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga0d5013ea3a6fa3bddd5cb182dd616151)。

IPv6 重复地址检测（Duplicate Address Detection）失败时发出的事件。

<a id="r_ga96fe7da048fe4d59435b7337626d4af7"></a>

```c
#define NET_EVENT_IPV6_NBR_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_NBR_ADD)
```

相关声明：[NET_EVENT_IPV6_NBR_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga96fe7da048fe4d59435b7337626d4af7)。

向系统添加 IPv6 邻居（Neighbor）时发出的事件。

<a id="r_ga5be1cdfeb1b8da485b1042a7b2dc14e4"></a>

```c
#define NET_EVENT_IPV6_NBR_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_NBR_DEL)
```

相关声明：[NET_EVENT_IPV6_NBR_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga5be1cdfeb1b8da485b1042a7b2dc14e4)。

从系统移除 IPv6 邻居（Neighbor）时发出的事件。

<a id="r_gaa07a5e8779ec24e5ab883970bcec6c5e"></a>

```c
#define NET_EVENT_IPV6_DHCP_START (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_START)
```

相关声明：[NET_EVENT_IPV6_DHCP_START](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaa07a5e8779ec24e5ab883970bcec6c5e)。

IPv6 DHCP 客户端（Client）启动时发出的事件。

<a id="r_gaff89dbc7562a85e9ff073b507bdf06e3"></a>

```c
#define NET_EVENT_IPV6_DHCP_BOUND (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_BOUND)
```

相关声明：[NET_EVENT_IPV6_DHCP_BOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaff89dbc7562a85e9ff073b507bdf06e3)。

IPv6 DHCP 客户端地址绑定（Bound）时发出的事件。

<a id="r_gaab05d5a65ef5f9ed147e32ce380f7de4"></a>

```c
#define NET_EVENT_IPV6_DHCP_STOP (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_STOP)
```

相关声明：[NET_EVENT_IPV6_DHCP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaab05d5a65ef5f9ed147e32ce380f7de4)。

IPv6 DHCP 客户端（Client）停止时发出的事件。

<a id="r_ga6cc42e3ca8197e46809de6082602ab98"></a>

```c
#define NET_EVENT_IPV6_ADDR_DEPRECATED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_DEPRECATED)
```

相关声明：[NET_EVENT_IPV6_ADDR_DEPRECATED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga6cc42e3ca8197e46809de6082602ab98)。

IPv6 地址已弃用（Deprecated）。

<a id="r_ga95f7a737a39fb655d3577405e70e04ba"></a>

```c
#define NET_EVENT_IPV6_PE_ENABLED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_ENABLED)
```

相关声明：[NET_EVENT_IPV6_PE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga95f7a737a39fb655d3577405e70e04ba)。

IPv6 隐私扩展（Privacy Extension）已启用。

<a id="r_gaba20579e42c4cebc8c3ac9a40ff384f3"></a>

```c
#define NET_EVENT_IPV6_PE_DISABLED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_DISABLED)
```

相关声明：[NET_EVENT_IPV6_PE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaba20579e42c4cebc8c3ac9a40ff384f3)。

IPv6 隐私扩展（Privacy Extension）已禁用。

<a id="r_ga19d671971cf07e76580db8098ab32971"></a>

```c
#define NET_EVENT_IPV6_PE_FILTER_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_FILTER_ADD)
```

相关声明：[NET_EVENT_IPV6_PE_FILTER_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga19d671971cf07e76580db8098ab32971)。

已添加 IPv6 隐私扩展过滤器（Privacy Extension Filter）。

<a id="r_gaf2f1c4b8dc5b9b07985265cee6a90f70"></a>

```c
#define NET_EVENT_IPV6_PE_FILTER_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_FILTER_DEL)
```

相关声明：[NET_EVENT_IPV6_PE_FILTER_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaf2f1c4b8dc5b9b07985265cee6a90f70)。

已移除 IPv6 隐私扩展过滤器（Privacy Extension Filter）。

<a id="r_gae0e1924aa8c8f6dc47582883528df185"></a>

```c
#define NET_EVENT_IPV6_PMTU_CHANGED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PMTU_CHANGED)
```

相关声明：[NET_EVENT_IPV6_PMTU_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gae0e1924aa8c8f6dc47582883528df185)。

IPv6 路径最大传输单元（Path MTU）已改变。

<a id="r_gad422365df617ce1473412908738048f0"></a>

```c
#define NET_EVENT_IPV4_ADDR_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ADDR_ADD)
```

相关声明：[NET_EVENT_IPV4_ADDR_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gad422365df617ce1473412908738048f0)。

向系统添加 IPv4 地址（Address）时发出的事件。

<a id="r_ga0d78644f799d1d8f5c18ec9860582817"></a>

```c
#define NET_EVENT_IPV4_ADDR_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ADDR_DEL)
```

相关声明：[NET_EVENT_IPV4_ADDR_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga0d78644f799d1d8f5c18ec9860582817)。

从系统移除 IPv4 地址（Address）时发出的事件。

<a id="r_ga854e897d09eecccc83d04d86fbba5b64"></a>

```c
#define NET_EVENT_IPV4_MADDR_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MADDR_ADD)
```

相关声明：[NET_EVENT_IPV4_MADDR_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga854e897d09eecccc83d04d86fbba5b64)。

向系统添加 IPv4 组播地址（Multicast Address）时发出的事件。

<a id="r_ga303824277664ee64674b7c93ff865bb4"></a>

```c
#define NET_EVENT_IPV4_MADDR_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MADDR_DEL)
```

相关声明：[NET_EVENT_IPV4_MADDR_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga303824277664ee64674b7c93ff865bb4)。

从系统移除 IPv4 组播地址（Multicast Address）时发出的事件。

<a id="r_ga740c97a7e94181ad734888bbe7b0a3d0"></a>

```c
#define NET_EVENT_IPV4_ROUTER_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTER_ADD)
```

相关声明：[NET_EVENT_IPV4_ROUTER_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga740c97a7e94181ad734888bbe7b0a3d0)。

向系统添加 IPv4 路由器（Router）时发出的事件。

<a id="r_gae45a3b6a5f4b72edc51e06a22b88239a"></a>

```c
#define NET_EVENT_IPV4_ROUTER_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTER_DEL)
```

相关声明：[NET_EVENT_IPV4_ROUTER_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gae45a3b6a5f4b72edc51e06a22b88239a)。

从系统移除 IPv4 路由器（Router）时发出的事件。

<a id="r_ga766d04b6b789c1c966c2e2149a3e1229"></a>

```c
#define NET_EVENT_IPV4_ROUTE_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTE_ADD)
```

相关声明：[NET_EVENT_IPV4_ROUTE_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga766d04b6b789c1c966c2e2149a3e1229)。

向系统添加 IPv4 路由（Route）时发出的事件。

<a id="r_ga1d7b96d88f846eb58db7867ffc96c2ea"></a>

```c
#define NET_EVENT_IPV4_ROUTE_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTE_DEL)
```

相关声明：[NET_EVENT_IPV4_ROUTE_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga1d7b96d88f846eb58db7867ffc96c2ea)。

从系统移除 IPv4 路由（Route）时发出的事件。

<a id="r_ga2d3a9351c226b1542d1b2f469b77233a"></a>

```c
#define NET_EVENT_IPV4_DHCP_START (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_START)
```

相关声明：[NET_EVENT_IPV4_DHCP_START](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga2d3a9351c226b1542d1b2f469b77233a)。

IPv4 DHCP 客户端（Client）启动时发出的事件。

<a id="r_ga7461ef85f4f8433851cb7583468c00cb"></a>

```c
#define NET_EVENT_IPV4_DHCP_BOUND (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_BOUND)
```

相关声明：[NET_EVENT_IPV4_DHCP_BOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga7461ef85f4f8433851cb7583468c00cb)。

IPv4 DHCP 客户端地址绑定（Bound）时发出的事件。

<a id="r_gabc06b6010780ab2d1e4f88227965b4e7"></a>

```c
#define NET_EVENT_IPV4_DHCP_STOP (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_STOP)
```

相关声明：[NET_EVENT_IPV4_DHCP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gabc06b6010780ab2d1e4f88227965b4e7)。

IPv4 DHCP 客户端（Client）停止时发出的事件。

<a id="r_ga17ad57d81f3046555f94f75dc6d31ec1"></a>

```c
#define NET_EVENT_IPV4_MCAST_JOIN (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MCAST_JOIN)
```

相关声明：[NET_EVENT_IPV4_MCAST_JOIN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga17ad57d81f3046555f94f75dc6d31ec1)。

加入 IPv4 组播组（Multicast Group）时发出的事件。

<a id="r_ga3cbb8a9dfec8435b93d908171ab944c9"></a>

```c
#define NET_EVENT_IPV4_MCAST_LEAVE (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MCAST_LEAVE)
```

相关声明：[NET_EVENT_IPV4_MCAST_LEAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga3cbb8a9dfec8435b93d908171ab944c9)。

离开 IPv4 组播组（Multicast Group）时发出的事件。

<a id="r_ga5293377de1fdc79e7564f4e5104a07c2"></a>

```c
#define NET_EVENT_IPV4_ACD_SUCCEED (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_SUCCEED)
```

相关声明：[NET_EVENT_IPV4_ACD_SUCCEED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga5293377de1fdc79e7564f4e5104a07c2)。

IPv4 地址冲突检测（Address Conflict Detection）成功时发出的事件。

<a id="r_ga3de741f5732473a1f49d9d0b93183549"></a>

```c
#define NET_EVENT_IPV4_ACD_FAILED (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_FAILED)
```

相关声明：[NET_EVENT_IPV4_ACD_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga3de741f5732473a1f49d9d0b93183549)。

IPv4 地址冲突检测（Address Conflict Detection）失败时发出的事件。

<a id="r_ga9af1f8f4ba965e6d6e82a190ab4748a1"></a>

```c
#define NET_EVENT_IPV4_ACD_CONFLICT (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_CONFLICT)
```

相关声明：[NET_EVENT_IPV4_ACD_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga9af1f8f4ba965e6d6e82a190ab4748a1)。

IPv4 地址已被确认可安全使用后，又检测到地址冲突（Address Conflict）时发出的事件。

<a id="r_ga24766ef249022c198299d38e95f400b9"></a>

```c
#define NET_EVENT_IPV4_PMTU_CHANGED (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_PMTU_CHANGED)
```

相关声明：[NET_EVENT_IPV4_PMTU_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga24766ef249022c198299d38e95f400b9)。

IPv4 路径最大传输单元（Path MTU）已改变。

<a id="r_gacbd2b10cc345359c07de4a62eb172a09"></a>

```c
#define NET_EVENT_L4_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CONNECTED)
```

相关声明：[NET_EVENT_L4_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gacbd2b10cc345359c07de4a62eb172a09)。

系统被视为已连接（Connected）时发出的事件。

<a id="r_gacd9e0b5e2f540794b20f11b070ffbd65"></a>

```c
#define NET_EVENT_L4_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DISCONNECTED)
```

相关声明：[NET_EVENT_L4_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gacd9e0b5e2f540794b20f11b070ffbd65)。

系统不再处于已连接（Connected）状态时发出的事件。

<a id="r_ga532fdc2f199e047a5d17e325cee12cf1"></a>

```c
#define NET_EVENT_L4_IPV4_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV4_CONNECTED)
```

相关声明：[NET_EVENT_L4_IPV4_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga532fdc2f199e047a5d17e325cee12cf1)。

IPv4 网络连通性（Network Connectivity）可用时触发的事件。

<a id="r_gaa92cc806d93446d548a05edb8e0074c2"></a>

```c
#define NET_EVENT_L4_IPV4_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV4_DISCONNECTED)
```

相关声明：[NET_EVENT_L4_IPV4_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaa92cc806d93446d548a05edb8e0074c2)。

IPv4 网络连通性（Network Connectivity）丢失时发出的事件。

<a id="r_gaf6bb88ed90df5aacb40e42fcc5bfbcf5"></a>

```c
#define NET_EVENT_L4_IPV6_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV6_CONNECTED)
```

相关声明：[NET_EVENT_L4_IPV6_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)。

IPv6 网络连通性（Network Connectivity）可用时发出的事件。

<a id="r_gac81abeab44fbf2b6f29d4e11a1e1bd17"></a>

```c
#define NET_EVENT_L4_IPV6_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV6_DISCONNECTED)
```

相关声明：[NET_EVENT_L4_IPV6_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gac81abeab44fbf2b6f29d4e11a1e1bd17)。

IPv6 网络连通性（Network Connectivity）丢失时发出的事件。

<a id="r_ga5735d13f24c974ad6d4038c93edf05e0"></a>

```c
#define NET_EVENT_DNS_SERVER_ADD (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVER_ADD)
```

相关声明：[NET_EVENT_DNS_SERVER_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga5735d13f24c974ad6d4038c93edf05e0)。

向系统添加 DNS 服务器（DNS Server）时发出的事件。

<a id="r_ga9d406772e5d1ad2952b2a2e0fed05c73"></a>

```c
#define NET_EVENT_DNS_SERVER_DEL (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVER_DEL)
```

相关声明：[NET_EVENT_DNS_SERVER_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga9d406772e5d1ad2952b2a2e0fed05c73)。

从系统移除 DNS 服务器（DNS Server）时发出的事件。

<a id="r_gac654c28128762a3160ce5f5717f053c5"></a>

```c
#define NET_EVENT_DNS_SERVERS_RECONFIGURED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVERS_RECONFIGURED)
```

相关声明：[NET_EVENT_DNS_SERVERS_RECONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gac654c28128762a3160ce5f5717f053c5)。

刷新 DNS 服务器配置（DNS Server Configuration）时发出的事件。

<a id="r_gac5a7458d89e4a95564999dca3c1b9f1e"></a>

```c
#define NET_EVENT_HOSTNAME_CHANGED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_HOSTNAME_CHANGED)
```

相关声明：[NET_EVENT_HOSTNAME_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gac5a7458d89e4a95564999dca3c1b9f1e)。

系统主机名（Hostname）改变时发出的事件。

<a id="r_gaa89b82a1890c55775f8c3c24e11f40e2"></a>

```c
#define NET_EVENT_CAPTURE_STARTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CAPTURE_STARTED)
```

相关声明：[NET_EVENT_CAPTURE_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaa89b82a1890c55775f8c3c24e11f40e2)。

网络数据包捕获（Network Packet Capture）已启动。

<a id="r_gaa2b655aedd597636790409539b1f86cd"></a>

```c
#define NET_EVENT_CAPTURE_STOPPED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CAPTURE_STOPPED)
```

相关声明：[NET_EVENT_CAPTURE_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaa2b655aedd597636790409539b1f86cd)。

网络数据包捕获（Network Packet Capture）已停止。

<a id="r_ga8084de14ebd35b4d32075642e952ca4d"></a>

```c
#define NET_EVENT_VPN_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_CONNECTED)
```

相关声明：[NET_EVENT_VPN_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga8084de14ebd35b4d32075642e952ca4d)。

VPN 网络连通性（Network Connectivity）可用时发出的事件。

<a id="r_ga74e837120225c10f0ccfa38696051cb8"></a>

```c
#define NET_EVENT_VPN_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_DISCONNECTED)
```

相关声明：[NET_EVENT_VPN_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga74e837120225c10f0ccfa38696051cb8)。

VPN 网络连通性（Network Connectivity）丢失时发出的事件。

<a id="r_gace9ee5cff7234717a9f183b89dcd28a3"></a>

```c
#define NET_EVENT_VPN_PEER_ADD (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_PEER_ADD)
```

相关声明：[NET_EVENT_VPN_PEER_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gace9ee5cff7234717a9f183b89dcd28a3)。

向系统添加 VPN 对等端（Peer）时发出的事件。

<a id="r_ga03f4fcb1977379401e2b6ea83ad37883"></a>

```c
#define NET_EVENT_VPN_PEER_DEL (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_PEER_DEL)
```

相关声明：[NET_EVENT_VPN_PEER_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga03f4fcb1977379401e2b6ea83ad37883)。

从系统移除 VPN 对等端（Peer）时发出的事件。

<a id="r_ga13635b6d7a152faa81d09b6285aeedf9"></a>

```c
#define NET_EVENT_L4_IF_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IF_CONNECTED)
```

相关声明：[NET_EVENT_L4_IF_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga13635b6d7a152faa81d09b6285aeedf9)。

接口被视为已连接（Connected）时发出的事件。

<a id="r_ga25300c6b7a8e38f058555493edaefe04"></a>

```c
#define NET_EVENT_L4_IF_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IF_DISCONNECTED)
```

相关声明：[NET_EVENT_L4_IF_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga25300c6b7a8e38f058555493edaefe04)。

接口不被视为已连接（Connected）时发出的事件。


## 4.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/net_mgmt.h](../api_source_timing_sensor_reference/P009_net_mgmt.h_源码浏览.md)
- [zephyr/net/hostname.h](../api_source_reference/P322_hostname.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P024_net_event.h_源码浏览.md)
- [net_event_packet_mcast](../network_core_model_reference/P073_net_event_packet_mcast_结构体.md)
- [net_event_ipv6_addr](../network_core_model_reference/P066_net_event_ipv6_addr_结构体.md)
- [net_event_ipv6_nbr](../network_core_model_reference/P067_net_event_ipv6_nbr_结构体.md)
- [net_event_ipv6_route](../network_core_model_reference/P071_net_event_ipv6_route_结构体.md)
- [net_event_ipv4_route](../network_core_model_reference/P065_net_event_ipv4_route_结构体.md)
- [net_event_ipv6_prefix](../network_core_model_reference/P070_net_event_ipv6_prefix_结构体.md)
- [net_event_l4_hostname](../network_core_model_reference/P072_net_event_l4_hostname_结构体.md)
- [net_event_ipv6_pe_filter](../network_core_model_reference/P068_net_event_ipv6_pe_filter_结构体.md)
- [net_event_ipv4_pmtu_info](../network_core_model_reference/P064_net_event_ipv4_pmtu_info_结构体.md)
- [net_event_ipv6_pmtu_info](../network_core_model_reference/P069_net_event_ipv6_pmtu_info_结构体.md)
- [NET_EVENT_IF_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gac43a928bce3feb217b37ff7eb205e71b)
- [NET_EVENT_IF_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaddc84a60607bb27048397e29eb9107f5)
- [NET_EVENT_IF_ADMIN_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gacb6ac7a4579be883abc9aa638299b0cd)
- [NET_EVENT_IF_ADMIN_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga94a52eb94cc2189919ade9c8c8f239bd)
- [NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gabfb799347776323486fb0d4563e31b3b)
- [NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaec5574f6308a89db36c2793bce6d5dcb)
- [NET_EVENT_IPV6_ADDR_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga20125c6148169a91fbebab1ebba17be3)
- [NET_EVENT_IPV6_ADDR_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga61f243efbc25928815ec78305b4f000e)
- [NET_EVENT_IPV6_MADDR_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gadda9dccf913a4dcb4d12b2b1fe5d403c)
- [NET_EVENT_IPV6_MADDR_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga035db32f66effd2407e0cca4b1fd9ea3)
- [NET_EVENT_IPV6_PREFIX_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga392414b95838bca1e55e4342870a8333)
- [NET_EVENT_IPV6_PREFIX_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gab06f93335938a635966e85a18b5b0cf6)
- [NET_EVENT_IPV6_MCAST_JOIN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga287d37bae2d74e0c85de59c5e23d409a)
- [NET_EVENT_IPV6_MCAST_LEAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga862d1b2ce9b65c0806ef77909364a58d)
- [NET_EVENT_IPV6_ROUTER_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaae932293528aa40127a906c3dbd45e31)
- [NET_EVENT_IPV6_ROUTER_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga8d4b7798981aaaf3aea2b793739143b7)
- [NET_EVENT_IPV6_ROUTE_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gad19b5e742ded9b3ed673d8f7985100fd)
- [NET_EVENT_IPV6_ROUTE_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gae6f68ec69032ac049f072d6ed164987c)
- [NET_EVENT_IPV6_DAD_SUCCEED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga8711b4b1e88c897196b982e4d56968f1)
- [NET_EVENT_IPV6_DAD_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga0d5013ea3a6fa3bddd5cb182dd616151)
- [NET_EVENT_IPV6_NBR_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga96fe7da048fe4d59435b7337626d4af7)
- [NET_EVENT_IPV6_NBR_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga5be1cdfeb1b8da485b1042a7b2dc14e4)
- [NET_EVENT_IPV6_DHCP_START](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaa07a5e8779ec24e5ab883970bcec6c5e)
- [NET_EVENT_IPV6_DHCP_BOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaff89dbc7562a85e9ff073b507bdf06e3)
- [NET_EVENT_IPV6_DHCP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaab05d5a65ef5f9ed147e32ce380f7de4)
- [NET_EVENT_IPV6_ADDR_DEPRECATED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga6cc42e3ca8197e46809de6082602ab98)
- [NET_EVENT_IPV6_PE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga95f7a737a39fb655d3577405e70e04ba)
- [NET_EVENT_IPV6_PE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaba20579e42c4cebc8c3ac9a40ff384f3)
- [NET_EVENT_IPV6_PE_FILTER_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga19d671971cf07e76580db8098ab32971)
- [NET_EVENT_IPV6_PE_FILTER_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaf2f1c4b8dc5b9b07985265cee6a90f70)
- [NET_EVENT_IPV6_PMTU_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gae0e1924aa8c8f6dc47582883528df185)
- [NET_EVENT_IPV4_ADDR_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gad422365df617ce1473412908738048f0)
- [NET_EVENT_IPV4_ADDR_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga0d78644f799d1d8f5c18ec9860582817)
- [NET_EVENT_IPV4_MADDR_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga854e897d09eecccc83d04d86fbba5b64)
- [NET_EVENT_IPV4_MADDR_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga303824277664ee64674b7c93ff865bb4)
- [NET_EVENT_IPV4_ROUTER_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga740c97a7e94181ad734888bbe7b0a3d0)
- [NET_EVENT_IPV4_ROUTER_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gae45a3b6a5f4b72edc51e06a22b88239a)
- [NET_EVENT_IPV4_ROUTE_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga766d04b6b789c1c966c2e2149a3e1229)
- [NET_EVENT_IPV4_ROUTE_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga1d7b96d88f846eb58db7867ffc96c2ea)
- [NET_EVENT_IPV4_DHCP_START](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga2d3a9351c226b1542d1b2f469b77233a)
- [NET_EVENT_IPV4_DHCP_BOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga7461ef85f4f8433851cb7583468c00cb)
- [NET_EVENT_IPV4_DHCP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gabc06b6010780ab2d1e4f88227965b4e7)
- [NET_EVENT_IPV4_MCAST_JOIN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga17ad57d81f3046555f94f75dc6d31ec1)
- [NET_EVENT_IPV4_MCAST_LEAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga3cbb8a9dfec8435b93d908171ab944c9)
- [NET_EVENT_IPV4_ACD_SUCCEED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga5293377de1fdc79e7564f4e5104a07c2)
- [NET_EVENT_IPV4_ACD_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga3de741f5732473a1f49d9d0b93183549)
- [NET_EVENT_IPV4_ACD_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga9af1f8f4ba965e6d6e82a190ab4748a1)
- [NET_EVENT_IPV4_PMTU_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga24766ef249022c198299d38e95f400b9)
- [NET_EVENT_L4_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gacbd2b10cc345359c07de4a62eb172a09)
- [NET_EVENT_L4_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gacd9e0b5e2f540794b20f11b070ffbd65)
- [NET_EVENT_L4_IPV4_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga532fdc2f199e047a5d17e325cee12cf1)
- [NET_EVENT_L4_IPV4_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaa92cc806d93446d548a05edb8e0074c2)
- [NET_EVENT_L4_IPV6_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)
- [NET_EVENT_L4_IPV6_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gac81abeab44fbf2b6f29d4e11a1e1bd17)
- [NET_EVENT_DNS_SERVER_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga5735d13f24c974ad6d4038c93edf05e0)
- [NET_EVENT_DNS_SERVER_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga9d406772e5d1ad2952b2a2e0fed05c73)
- [NET_EVENT_DNS_SERVERS_RECONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gac654c28128762a3160ce5f5717f053c5)
- [NET_EVENT_HOSTNAME_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gac5a7458d89e4a95564999dca3c1b9f1e)
- [NET_EVENT_CAPTURE_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaa89b82a1890c55775f8c3c24e11f40e2)
- [NET_EVENT_CAPTURE_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaa2b655aedd597636790409539b1f86cd)
- [NET_EVENT_VPN_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga8084de14ebd35b4d32075642e952ca4d)
- [NET_EVENT_VPN_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga74e837120225c10f0ccfa38696051cb8)
- [NET_EVENT_VPN_PEER_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gace9ee5cff7234717a9f183b89dcd28a3)
- [NET_EVENT_VPN_PEER_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga03f4fcb1977379401e2b6ea83ad37883)
- [NET_EVENT_L4_IF_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga13635b6d7a152faa81d09b6285aeedf9)
- [NET_EVENT_L4_IF_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga25300c6b7a8e38f058555493edaefe04)

<a id="header-details"></a>

---

[上一章](P003_zephyr__drivers__modem__hl7800.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__posix__posix_signal.h_文件参考.md)
