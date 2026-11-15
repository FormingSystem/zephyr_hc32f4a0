---
id: learning.zephyr-docs.api-audio-metrics-topic-reference.page-5
title: 网络管理（Network Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_网络管理（Network Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络管理（Network Management）

<a id="details"></a>

网络管理（Network Management）。自（Since）1.7 起提供，版本（Version）2.0.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

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

<a id="r_net_5Fmgmt_5Fevent_5Fcallback"></a>

```c
struct net_mgmt_event_callback
```

相关声明：[net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)。

网络管理事件回调（Network Management Event Callback）结构；用于向网络管理事件部分注册回调，使该结构的所有者能够根据给定事件掩码接收网络事件通知。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_gac43a928bce3feb217b37ff7eb205e71b"></a>

```c
#define NET_EVENT_IF_DOWN (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_DOWN)
```

相关声明：[NET_EVENT_IF_DOWN](#gac43a928bce3feb217b37ff7eb205e71b)。

网络接口转为停用（Down）状态时发出的事件。

<a id="r_gaddc84a60607bb27048397e29eb9107f5"></a>

```c
#define NET_EVENT_IF_UP (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_UP)
```

相关声明：[NET_EVENT_IF_UP](#gaddc84a60607bb27048397e29eb9107f5)。

网络接口转为启用（Up）状态时发出的事件。

<a id="r_gacb6ac7a4579be883abc9aa638299b0cd"></a>

```c
#define NET_EVENT_IF_ADMIN_DOWN (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_ADMIN_DOWN)
```

相关声明：[NET_EVENT_IF_ADMIN_DOWN](#gacb6ac7a4579be883abc9aa638299b0cd)。

手动停用（Down）网络接口时发出的事件。

<a id="r_ga94a52eb94cc2189919ade9c8c8f239bd"></a>

```c
#define NET_EVENT_IF_ADMIN_UP (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_ADMIN_UP)
```

相关声明：[NET_EVENT_IF_ADMIN_UP](#ga94a52eb94cc2189919ade9c8c8f239bd)。

手动启用（Up）网络接口时发出的事件。

<a id="r_gabfb799347776323486fb0d4563e31b3b"></a>

```c
#define NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD (NET_EVENT_PACKET_BASE | NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_ADD)
```

相关声明：[NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD](#gabfb799347776323486fb0d4563e31b3b)。

添加分组套接字（Packet Socket）的组播组成员资格（Multicast Group Membership）时发出的事件。

<a id="r_gaec5574f6308a89db36c2793bce6d5dcb"></a>

```c
#define NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP (NET_EVENT_PACKET_BASE | NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_DROP)
```

相关声明：[NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP](#gaec5574f6308a89db36c2793bce6d5dcb)。

移除分组套接字（Packet Socket）的组播组成员资格（Multicast Group Membership）时发出的事件。

<a id="r_ga20125c6148169a91fbebab1ebba17be3"></a>

```c
#define NET_EVENT_IPV6_ADDR_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_ADD)
```

相关声明：[NET_EVENT_IPV6_ADDR_ADD](#ga20125c6148169a91fbebab1ebba17be3)。

向系统添加 IPv6 地址（Address）时发出的事件。

<a id="r_ga61f243efbc25928815ec78305b4f000e"></a>

```c
#define NET_EVENT_IPV6_ADDR_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_DEL)
```

相关声明：[NET_EVENT_IPV6_ADDR_DEL](#ga61f243efbc25928815ec78305b4f000e)。

从系统移除 IPv6 地址（Address）时发出的事件。

<a id="r_gadda9dccf913a4dcb4d12b2b1fe5d403c"></a>

```c
#define NET_EVENT_IPV6_MADDR_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MADDR_ADD)
```

相关声明：[NET_EVENT_IPV6_MADDR_ADD](#gadda9dccf913a4dcb4d12b2b1fe5d403c)。

向系统添加 IPv6 组播地址（Multicast Address）时发出的事件。

<a id="r_ga035db32f66effd2407e0cca4b1fd9ea3"></a>

```c
#define NET_EVENT_IPV6_MADDR_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MADDR_DEL)
```

相关声明：[NET_EVENT_IPV6_MADDR_DEL](#ga035db32f66effd2407e0cca4b1fd9ea3)。

从系统移除 IPv6 组播地址（Multicast Address）时发出的事件。

<a id="r_ga392414b95838bca1e55e4342870a8333"></a>

```c
#define NET_EVENT_IPV6_PREFIX_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PREFIX_ADD)
```

相关声明：[NET_EVENT_IPV6_PREFIX_ADD](#ga392414b95838bca1e55e4342870a8333)。

向系统添加 IPv6 前缀（Prefix）时发出的事件。

<a id="r_gab06f93335938a635966e85a18b5b0cf6"></a>

```c
#define NET_EVENT_IPV6_PREFIX_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PREFIX_DEL)
```

相关声明：[NET_EVENT_IPV6_PREFIX_DEL](#gab06f93335938a635966e85a18b5b0cf6)。

从系统移除 IPv6 前缀（Prefix）时发出的事件。

<a id="r_ga287d37bae2d74e0c85de59c5e23d409a"></a>

```c
#define NET_EVENT_IPV6_MCAST_JOIN (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MCAST_JOIN)
```

相关声明：[NET_EVENT_IPV6_MCAST_JOIN](#ga287d37bae2d74e0c85de59c5e23d409a)。

加入 IPv6 组播组（Multicast Group）时发出的事件。

<a id="r_ga862d1b2ce9b65c0806ef77909364a58d"></a>

```c
#define NET_EVENT_IPV6_MCAST_LEAVE (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MCAST_LEAVE)
```

相关声明：[NET_EVENT_IPV6_MCAST_LEAVE](#ga862d1b2ce9b65c0806ef77909364a58d)。

离开 IPv6 组播组（Multicast Group）时发出的事件。

<a id="r_gaae932293528aa40127a906c3dbd45e31"></a>

```c
#define NET_EVENT_IPV6_ROUTER_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTER_ADD)
```

相关声明：[NET_EVENT_IPV6_ROUTER_ADD](#gaae932293528aa40127a906c3dbd45e31)。

向系统添加 IPv6 路由器（Router）时发出的事件。

<a id="r_ga8d4b7798981aaaf3aea2b793739143b7"></a>

```c
#define NET_EVENT_IPV6_ROUTER_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTER_DEL)
```

相关声明：[NET_EVENT_IPV6_ROUTER_DEL](#ga8d4b7798981aaaf3aea2b793739143b7)。

从系统移除 IPv6 路由器（Router）时发出的事件。

<a id="r_gad19b5e742ded9b3ed673d8f7985100fd"></a>

```c
#define NET_EVENT_IPV6_ROUTE_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTE_ADD)
```

相关声明：[NET_EVENT_IPV6_ROUTE_ADD](#gad19b5e742ded9b3ed673d8f7985100fd)。

向系统添加 IPv6 路由（Route）时发出的事件。

<a id="r_gae6f68ec69032ac049f072d6ed164987c"></a>

```c
#define NET_EVENT_IPV6_ROUTE_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTE_DEL)
```

相关声明：[NET_EVENT_IPV6_ROUTE_DEL](#gae6f68ec69032ac049f072d6ed164987c)。

从系统移除 IPv6 路由（Route）时发出的事件。

<a id="r_ga8711b4b1e88c897196b982e4d56968f1"></a>

```c
#define NET_EVENT_IPV6_DAD_SUCCEED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DAD_SUCCEED)
```

相关声明：[NET_EVENT_IPV6_DAD_SUCCEED](#ga8711b4b1e88c897196b982e4d56968f1)。

IPv6 重复地址检测（Duplicate Address Detection）成功时发出的事件。

<a id="r_ga0d5013ea3a6fa3bddd5cb182dd616151"></a>

```c
#define NET_EVENT_IPV6_DAD_FAILED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DAD_FAILED)
```

相关声明：[NET_EVENT_IPV6_DAD_FAILED](#ga0d5013ea3a6fa3bddd5cb182dd616151)。

IPv6 重复地址检测（Duplicate Address Detection）失败时发出的事件。

<a id="r_ga96fe7da048fe4d59435b7337626d4af7"></a>

```c
#define NET_EVENT_IPV6_NBR_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_NBR_ADD)
```

相关声明：[NET_EVENT_IPV6_NBR_ADD](#ga96fe7da048fe4d59435b7337626d4af7)。

向系统添加 IPv6 邻居（Neighbor）时发出的事件。

<a id="r_ga5be1cdfeb1b8da485b1042a7b2dc14e4"></a>

```c
#define NET_EVENT_IPV6_NBR_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_NBR_DEL)
```

相关声明：[NET_EVENT_IPV6_NBR_DEL](#ga5be1cdfeb1b8da485b1042a7b2dc14e4)。

从系统移除 IPv6 邻居（Neighbor）时发出的事件。

<a id="r_gaa07a5e8779ec24e5ab883970bcec6c5e"></a>

```c
#define NET_EVENT_IPV6_DHCP_START (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_START)
```

相关声明：[NET_EVENT_IPV6_DHCP_START](#gaa07a5e8779ec24e5ab883970bcec6c5e)。

IPv6 DHCP 客户端（Client）启动时发出的事件。

<a id="r_gaff89dbc7562a85e9ff073b507bdf06e3"></a>

```c
#define NET_EVENT_IPV6_DHCP_BOUND (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_BOUND)
```

相关声明：[NET_EVENT_IPV6_DHCP_BOUND](#gaff89dbc7562a85e9ff073b507bdf06e3)。

IPv6 DHCP 客户端地址绑定（Bound）时发出的事件。

<a id="r_gaab05d5a65ef5f9ed147e32ce380f7de4"></a>

```c
#define NET_EVENT_IPV6_DHCP_STOP (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_STOP)
```

相关声明：[NET_EVENT_IPV6_DHCP_STOP](#gaab05d5a65ef5f9ed147e32ce380f7de4)。

IPv6 DHCP 客户端（Client）停止时发出的事件。

<a id="r_ga6cc42e3ca8197e46809de6082602ab98"></a>

```c
#define NET_EVENT_IPV6_ADDR_DEPRECATED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_DEPRECATED)
```

相关声明：[NET_EVENT_IPV6_ADDR_DEPRECATED](#ga6cc42e3ca8197e46809de6082602ab98)。

IPv6 地址已弃用（Deprecated）。

<a id="r_ga95f7a737a39fb655d3577405e70e04ba"></a>

```c
#define NET_EVENT_IPV6_PE_ENABLED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_ENABLED)
```

相关声明：[NET_EVENT_IPV6_PE_ENABLED](#ga95f7a737a39fb655d3577405e70e04ba)。

IPv6 隐私扩展（Privacy Extension）已启用。

<a id="r_gaba20579e42c4cebc8c3ac9a40ff384f3"></a>

```c
#define NET_EVENT_IPV6_PE_DISABLED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_DISABLED)
```

相关声明：[NET_EVENT_IPV6_PE_DISABLED](#gaba20579e42c4cebc8c3ac9a40ff384f3)。

IPv6 隐私扩展（Privacy Extension）已禁用。

<a id="r_ga19d671971cf07e76580db8098ab32971"></a>

```c
#define NET_EVENT_IPV6_PE_FILTER_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_FILTER_ADD)
```

相关声明：[NET_EVENT_IPV6_PE_FILTER_ADD](#ga19d671971cf07e76580db8098ab32971)。

已添加 IPv6 隐私扩展过滤器（Privacy Extension Filter）。

<a id="r_gaf2f1c4b8dc5b9b07985265cee6a90f70"></a>

```c
#define NET_EVENT_IPV6_PE_FILTER_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_FILTER_DEL)
```

相关声明：[NET_EVENT_IPV6_PE_FILTER_DEL](#gaf2f1c4b8dc5b9b07985265cee6a90f70)。

已移除 IPv6 隐私扩展过滤器（Privacy Extension Filter）。

<a id="r_gae0e1924aa8c8f6dc47582883528df185"></a>

```c
#define NET_EVENT_IPV6_PMTU_CHANGED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PMTU_CHANGED)
```

相关声明：[NET_EVENT_IPV6_PMTU_CHANGED](#gae0e1924aa8c8f6dc47582883528df185)。

IPv6 路径最大传输单元（Path MTU）已改变。

<a id="r_gad422365df617ce1473412908738048f0"></a>

```c
#define NET_EVENT_IPV4_ADDR_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ADDR_ADD)
```

相关声明：[NET_EVENT_IPV4_ADDR_ADD](#gad422365df617ce1473412908738048f0)。

向系统添加 IPv4 地址（Address）时发出的事件。

<a id="r_ga0d78644f799d1d8f5c18ec9860582817"></a>

```c
#define NET_EVENT_IPV4_ADDR_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ADDR_DEL)
```

相关声明：[NET_EVENT_IPV4_ADDR_DEL](#ga0d78644f799d1d8f5c18ec9860582817)。

从系统移除 IPv4 地址（Address）时发出的事件。

<a id="r_ga854e897d09eecccc83d04d86fbba5b64"></a>

```c
#define NET_EVENT_IPV4_MADDR_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MADDR_ADD)
```

相关声明：[NET_EVENT_IPV4_MADDR_ADD](#ga854e897d09eecccc83d04d86fbba5b64)。

向系统添加 IPv4 组播地址（Multicast Address）时发出的事件。

<a id="r_ga303824277664ee64674b7c93ff865bb4"></a>

```c
#define NET_EVENT_IPV4_MADDR_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MADDR_DEL)
```

相关声明：[NET_EVENT_IPV4_MADDR_DEL](#ga303824277664ee64674b7c93ff865bb4)。

从系统移除 IPv4 组播地址（Multicast Address）时发出的事件。

<a id="r_ga740c97a7e94181ad734888bbe7b0a3d0"></a>

```c
#define NET_EVENT_IPV4_ROUTER_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTER_ADD)
```

相关声明：[NET_EVENT_IPV4_ROUTER_ADD](#ga740c97a7e94181ad734888bbe7b0a3d0)。

向系统添加 IPv4 路由器（Router）时发出的事件。

<a id="r_gae45a3b6a5f4b72edc51e06a22b88239a"></a>

```c
#define NET_EVENT_IPV4_ROUTER_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTER_DEL)
```

相关声明：[NET_EVENT_IPV4_ROUTER_DEL](#gae45a3b6a5f4b72edc51e06a22b88239a)。

从系统移除 IPv4 路由器（Router）时发出的事件。

<a id="r_ga766d04b6b789c1c966c2e2149a3e1229"></a>

```c
#define NET_EVENT_IPV4_ROUTE_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTE_ADD)
```

相关声明：[NET_EVENT_IPV4_ROUTE_ADD](#ga766d04b6b789c1c966c2e2149a3e1229)。

向系统添加 IPv4 路由（Route）时发出的事件。

<a id="r_ga1d7b96d88f846eb58db7867ffc96c2ea"></a>

```c
#define NET_EVENT_IPV4_ROUTE_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTE_DEL)
```

相关声明：[NET_EVENT_IPV4_ROUTE_DEL](#ga1d7b96d88f846eb58db7867ffc96c2ea)。

从系统移除 IPv4 路由（Route）时发出的事件。

<a id="r_ga2d3a9351c226b1542d1b2f469b77233a"></a>

```c
#define NET_EVENT_IPV4_DHCP_START (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_START)
```

相关声明：[NET_EVENT_IPV4_DHCP_START](#ga2d3a9351c226b1542d1b2f469b77233a)。

IPv4 DHCP 客户端（Client）启动时发出的事件。

<a id="r_ga7461ef85f4f8433851cb7583468c00cb"></a>

```c
#define NET_EVENT_IPV4_DHCP_BOUND (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_BOUND)
```

相关声明：[NET_EVENT_IPV4_DHCP_BOUND](#ga7461ef85f4f8433851cb7583468c00cb)。

IPv4 DHCP 客户端地址绑定（Bound）时发出的事件。

<a id="r_gabc06b6010780ab2d1e4f88227965b4e7"></a>

```c
#define NET_EVENT_IPV4_DHCP_STOP (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_STOP)
```

相关声明：[NET_EVENT_IPV4_DHCP_STOP](#gabc06b6010780ab2d1e4f88227965b4e7)。

IPv4 DHCP 客户端（Client）停止时发出的事件。

<a id="r_ga17ad57d81f3046555f94f75dc6d31ec1"></a>

```c
#define NET_EVENT_IPV4_MCAST_JOIN (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MCAST_JOIN)
```

相关声明：[NET_EVENT_IPV4_MCAST_JOIN](#ga17ad57d81f3046555f94f75dc6d31ec1)。

加入 IPv4 组播组（Multicast Group）时发出的事件。

<a id="r_ga3cbb8a9dfec8435b93d908171ab944c9"></a>

```c
#define NET_EVENT_IPV4_MCAST_LEAVE (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MCAST_LEAVE)
```

相关声明：[NET_EVENT_IPV4_MCAST_LEAVE](#ga3cbb8a9dfec8435b93d908171ab944c9)。

离开 IPv4 组播组（Multicast Group）时发出的事件。

<a id="r_ga5293377de1fdc79e7564f4e5104a07c2"></a>

```c
#define NET_EVENT_IPV4_ACD_SUCCEED (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_SUCCEED)
```

相关声明：[NET_EVENT_IPV4_ACD_SUCCEED](#ga5293377de1fdc79e7564f4e5104a07c2)。

IPv4 地址冲突检测（Address Conflict Detection）成功时发出的事件。

<a id="r_ga3de741f5732473a1f49d9d0b93183549"></a>

```c
#define NET_EVENT_IPV4_ACD_FAILED (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_FAILED)
```

相关声明：[NET_EVENT_IPV4_ACD_FAILED](#ga3de741f5732473a1f49d9d0b93183549)。

IPv4 地址冲突检测（Address Conflict Detection）失败时发出的事件。

<a id="r_ga9af1f8f4ba965e6d6e82a190ab4748a1"></a>

```c
#define NET_EVENT_IPV4_ACD_CONFLICT (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_CONFLICT)
```

相关声明：[NET_EVENT_IPV4_ACD_CONFLICT](#ga9af1f8f4ba965e6d6e82a190ab4748a1)。

IPv4 地址已被确认可安全使用后，又检测到地址冲突（Address Conflict）时发出的事件。

<a id="r_ga24766ef249022c198299d38e95f400b9"></a>

```c
#define NET_EVENT_IPV4_PMTU_CHANGED (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_PMTU_CHANGED)
```

相关声明：[NET_EVENT_IPV4_PMTU_CHANGED](#ga24766ef249022c198299d38e95f400b9)。

IPv4 路径最大传输单元（Path MTU）已改变。

<a id="r_gacbd2b10cc345359c07de4a62eb172a09"></a>

```c
#define NET_EVENT_L4_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CONNECTED)
```

相关声明：[NET_EVENT_L4_CONNECTED](#gacbd2b10cc345359c07de4a62eb172a09)。

系统被视为已连接（Connected）时发出的事件。

<a id="r_gacd9e0b5e2f540794b20f11b070ffbd65"></a>

```c
#define NET_EVENT_L4_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DISCONNECTED)
```

相关声明：[NET_EVENT_L4_DISCONNECTED](#gacd9e0b5e2f540794b20f11b070ffbd65)。

系统不再处于已连接（Connected）状态时发出的事件。

<a id="r_ga532fdc2f199e047a5d17e325cee12cf1"></a>

```c
#define NET_EVENT_L4_IPV4_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV4_CONNECTED)
```

相关声明：[NET_EVENT_L4_IPV4_CONNECTED](#ga532fdc2f199e047a5d17e325cee12cf1)。

IPv4 网络连通性（Network Connectivity）可用时触发的事件。

<a id="r_gaa92cc806d93446d548a05edb8e0074c2"></a>

```c
#define NET_EVENT_L4_IPV4_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV4_DISCONNECTED)
```

相关声明：[NET_EVENT_L4_IPV4_DISCONNECTED](#gaa92cc806d93446d548a05edb8e0074c2)。

IPv4 网络连通性（Network Connectivity）丢失时发出的事件。

<a id="r_gaf6bb88ed90df5aacb40e42fcc5bfbcf5"></a>

```c
#define NET_EVENT_L4_IPV6_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV6_CONNECTED)
```

相关声明：[NET_EVENT_L4_IPV6_CONNECTED](#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)。

IPv6 网络连通性（Network Connectivity）可用时发出的事件。

<a id="r_gac81abeab44fbf2b6f29d4e11a1e1bd17"></a>

```c
#define NET_EVENT_L4_IPV6_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV6_DISCONNECTED)
```

相关声明：[NET_EVENT_L4_IPV6_DISCONNECTED](#gac81abeab44fbf2b6f29d4e11a1e1bd17)。

IPv6 网络连通性（Network Connectivity）丢失时发出的事件。

<a id="r_ga5735d13f24c974ad6d4038c93edf05e0"></a>

```c
#define NET_EVENT_DNS_SERVER_ADD (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVER_ADD)
```

相关声明：[NET_EVENT_DNS_SERVER_ADD](#ga5735d13f24c974ad6d4038c93edf05e0)。

向系统添加 DNS 服务器（DNS Server）时发出的事件。

<a id="r_ga9d406772e5d1ad2952b2a2e0fed05c73"></a>

```c
#define NET_EVENT_DNS_SERVER_DEL (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVER_DEL)
```

相关声明：[NET_EVENT_DNS_SERVER_DEL](#ga9d406772e5d1ad2952b2a2e0fed05c73)。

从系统移除 DNS 服务器（DNS Server）时发出的事件。

<a id="r_gac654c28128762a3160ce5f5717f053c5"></a>

```c
#define NET_EVENT_DNS_SERVERS_RECONFIGURED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVERS_RECONFIGURED)
```

相关声明：[NET_EVENT_DNS_SERVERS_RECONFIGURED](#gac654c28128762a3160ce5f5717f053c5)。

刷新 DNS 服务器配置（DNS Server Configuration）时发出的事件。

<a id="r_gac5a7458d89e4a95564999dca3c1b9f1e"></a>

```c
#define NET_EVENT_HOSTNAME_CHANGED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_HOSTNAME_CHANGED)
```

相关声明：[NET_EVENT_HOSTNAME_CHANGED](#gac5a7458d89e4a95564999dca3c1b9f1e)。

系统主机名（Hostname）改变时发出的事件。

<a id="r_gaa89b82a1890c55775f8c3c24e11f40e2"></a>

```c
#define NET_EVENT_CAPTURE_STARTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CAPTURE_STARTED)
```

相关声明：[NET_EVENT_CAPTURE_STARTED](#gaa89b82a1890c55775f8c3c24e11f40e2)。

网络数据包捕获（Network Packet Capture）已启动。

<a id="r_gaa2b655aedd597636790409539b1f86cd"></a>

```c
#define NET_EVENT_CAPTURE_STOPPED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CAPTURE_STOPPED)
```

相关声明：[NET_EVENT_CAPTURE_STOPPED](#gaa2b655aedd597636790409539b1f86cd)。

网络数据包捕获（Network Packet Capture）已停止。

<a id="r_ga8084de14ebd35b4d32075642e952ca4d"></a>

```c
#define NET_EVENT_VPN_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_CONNECTED)
```

相关声明：[NET_EVENT_VPN_CONNECTED](#ga8084de14ebd35b4d32075642e952ca4d)。

VPN 网络连通性（Network Connectivity）可用时发出的事件。

<a id="r_ga74e837120225c10f0ccfa38696051cb8"></a>

```c
#define NET_EVENT_VPN_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_DISCONNECTED)
```

相关声明：[NET_EVENT_VPN_DISCONNECTED](#ga74e837120225c10f0ccfa38696051cb8)。

VPN 网络连通性（Network Connectivity）丢失时发出的事件。

<a id="r_gace9ee5cff7234717a9f183b89dcd28a3"></a>

```c
#define NET_EVENT_VPN_PEER_ADD (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_PEER_ADD)
```

相关声明：[NET_EVENT_VPN_PEER_ADD](#gace9ee5cff7234717a9f183b89dcd28a3)。

向系统添加 VPN 对等端（Peer）时发出的事件。

<a id="r_ga03f4fcb1977379401e2b6ea83ad37883"></a>

```c
#define NET_EVENT_VPN_PEER_DEL (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_PEER_DEL)
```

相关声明：[NET_EVENT_VPN_PEER_DEL](#ga03f4fcb1977379401e2b6ea83ad37883)。

从系统移除 VPN 对等端（Peer）时发出的事件。

<a id="r_ga13635b6d7a152faa81d09b6285aeedf9"></a>

```c
#define NET_EVENT_L4_IF_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IF_CONNECTED)
```

相关声明：[NET_EVENT_L4_IF_CONNECTED](#ga13635b6d7a152faa81d09b6285aeedf9)。

接口被视为已连接（Connected）时发出的事件。

<a id="r_ga25300c6b7a8e38f058555493edaefe04"></a>

```c
#define NET_EVENT_L4_IF_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IF_DISCONNECTED)
```

相关声明：[NET_EVENT_L4_IF_DISCONNECTED](#ga25300c6b7a8e38f058555493edaefe04)。

接口不被视为已连接（Connected）时发出的事件。

<a id="r_ga40e0f9fc86812ad9f6fe174b4c3804e6"></a>

```c
#define net_mgmt(_mgmt_request, _iface, _data, _len)
```

相关声明：[net_mgmt](#ga40e0f9fc86812ad9f6fe174b4c3804e6)。

生成网络管理事件（Network Management Event）。

<a id="r_ga08bde8717fd8e12a338c517b22b87776"></a>

```c
#define NET_MGMT_DEFINE_REQUEST_HANDLER(_mgmt_request)
```

相关声明：[NET_MGMT_DEFINE_REQUEST_HANDLER](#ga08bde8717fd8e12a338c517b22b87776)。

为给定网络事件（Network Event）声明请求处理函数（Request Handler）。

<a id="r_gab67d09d1e65b806ec1957451cbf60501"></a>

```c
#define NET_MGMT_REGISTER_REQUEST_HANDLER(_mgmt_request, _func)
```

相关声明：[NET_MGMT_REGISTER_REQUEST_HANDLER](#gab67d09d1e65b806ec1957451cbf60501)。

为给定网络事件（Network Event）创建请求处理函数（Request Handler）。

<a id="r_ga3a6ca8a72ab12afd4f9b0461253eaa12"></a>

```c
#define NET_MGMT_REGISTER_EVENT_HANDLER(_name, _event_mask, _func, _user_data)
```

相关声明：[NET_MGMT_REGISTER_EVENT_HANDLER](#ga3a6ca8a72ab12afd4f9b0461253eaa12)。

定义静态网络事件处理程序（Static Network Event Handler）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_ga78b9302193bd0c5cc35d81d298a5eb6b"></a>

```c
typedef int(* net_mgmt_request_handler_t) (uint64_t mgmt_request, struct net_if *iface, void *data, size_t len)
```

相关声明：[net_mgmt_request_handler_t](#ga78b9302193bd0c5cc35d81d298a5eb6b)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

所有网络管理（Net MGMT）请求处理程序必须遵循的函数签名（Signature）。

<a id="r_ga2e83a5a769ac52c846f255e23aea84d2"></a>

```c
typedef void(* net_mgmt_event_handler_t) (struct net_mgmt_event_callback *cb, uint64_t mgmt_event, struct net_if *iface)
```

相关声明：[net_mgmt_event_handler_t](#ga2e83a5a769ac52c846f255e23aea84d2)、[net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

定义用户回调处理函数签名（Callback Handler Function Signature）。

<a id="r_gaf3773f8e945c4ec05b2fab46cd8b1881"></a>

```c
typedef void(* net_mgmt_event_static_handler_t) (uint64_t mgmt_event, struct net_if *iface, void *info, size_t info_length, void *user_data)
```

相关声明：[net_mgmt_event_static_handler_t](#gaf3773f8e945c4ec05b2fab46cd8b1881)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

定义用户回调处理函数签名（Callback Handler Function Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.4\_枚举（Enumerations）

<a id="r_ga5e6911455b9ab9f4c82780001459461a"></a>

```c
enum net_mgmt_layer_code { NET_MGMT_LAYER_CODE_UNKNOWN = 0x00 , NET_MGMT_LAYER_CODE_IFACE = 0x01 , NET_MGMT_LAYER_CODE_CONN = 0x02 , NET_MGMT_LAYER_CODE_IPV4 = 0x03 , NET_MGMT_LAYER_CODE_IPV6 = 0x04 , NET_MGMT_LAYER_CODE_L4 = 0x05 , NET_MGMT_LAYER_CODE_COAP = 0x06 , NET_MGMT_LAYER_CODE_STATS = 0x07 , NET_MGMT_LAYER_CODE_HOSTAP = 0x08 , NET_MGMT_LAYER_CODE_ETHERNET = 0x09 , NET_MGMT_LAYER_CODE_IEEE802514 = 0x0A , NET_MGMT_LAYER_CODE_PPP = 0x0B , NET_MGMT_LAYER_CODE_VIRTUAL = 0x0C , NET_MGMT_LAYER_CODE_WIFI = 0x0D , NET_MGMT_LAYER_CODE_PACKET = 0x0E , NET_MGMT_LAYER_CODE_USER3 = 0x7C , NET_MGMT_LAYER_CODE_USER2 = 0x7D , NET_MGMT_LAYER_CODE_USER1 = 0x7E , NET_MGMT_LAYER_CODE_RESERVED = 0x7F }
```

相关声明：[net_mgmt_layer_code](#ga5e6911455b9ab9f4c82780001459461a)、[NET_MGMT_LAYER_CODE_UNKNOWN](#gga5e6911455b9ab9f4c82780001459461aa3206e13330183c74d20e89407e11c7cd)、[NET_MGMT_LAYER_CODE_IFACE](#gga5e6911455b9ab9f4c82780001459461aa2e23e545f7d78775adb5271f7bf42518)、[NET_MGMT_LAYER_CODE_CONN](#gga5e6911455b9ab9f4c82780001459461aabf1c9ef98fb7237ba1591108c67bf1d7)、[NET_MGMT_LAYER_CODE_IPV4](#gga5e6911455b9ab9f4c82780001459461aa25c33c6faa9d22f4ac5b70049bb4bbd2)、[NET_MGMT_LAYER_CODE_IPV6](#gga5e6911455b9ab9f4c82780001459461aa8f1f092ecdfcf341458e7389cee3ace8)、[NET_MGMT_LAYER_CODE_L4](#gga5e6911455b9ab9f4c82780001459461aab60d69e5ee62cb0212b1e424d7847b4e)、[NET_MGMT_LAYER_CODE_COAP](#gga5e6911455b9ab9f4c82780001459461aa5701861bfb5fae92e8c7b08ea02f61a7)、[NET_MGMT_LAYER_CODE_STATS](#gga5e6911455b9ab9f4c82780001459461aa3ab69a93464d5fa0d5be9ac9f3757cb6)、[NET_MGMT_LAYER_CODE_HOSTAP](#gga5e6911455b9ab9f4c82780001459461aa06935e2c46523b1a3f414f4c981992fc)、[NET_MGMT_LAYER_CODE_ETHERNET](#gga5e6911455b9ab9f4c82780001459461aafd0569a3f3cde9e892751a84b74836b4)、[NET_MGMT_LAYER_CODE_IEEE802514](#gga5e6911455b9ab9f4c82780001459461aa4893c212a3026909dcb8663abbdf2b2b)、[NET_MGMT_LAYER_CODE_PPP](#gga5e6911455b9ab9f4c82780001459461aa52b23f5afbf235bef6bc2aeea69271c1)、[NET_MGMT_LAYER_CODE_VIRTUAL](#gga5e6911455b9ab9f4c82780001459461aac767c8da93a6d0f5a53e64cbfdf94fca)、[NET_MGMT_LAYER_CODE_WIFI](#gga5e6911455b9ab9f4c82780001459461aa7f2f4d110d3003974bd0da0154c2d789)、[NET_MGMT_LAYER_CODE_PACKET](#gga5e6911455b9ab9f4c82780001459461aa997785b24761b410a1d33788c46f90b1)、[NET_MGMT_LAYER_CODE_USER3](#gga5e6911455b9ab9f4c82780001459461aa4e57a620f5778d346984398c0e786977)、[NET_MGMT_LAYER_CODE_USER2](#gga5e6911455b9ab9f4c82780001459461aaa335a8c82c6d7614337e3501a69aa1d4)、[NET_MGMT_LAYER_CODE_USER1](#gga5e6911455b9ab9f4c82780001459461aa10876d890aac72553ab69c0964bef48a)、[NET_MGMT_LAYER_CODE_RESERVED](#gga5e6911455b9ab9f4c82780001459461aaef64c0749996046b313ebf366b3eab75)。

集中定义层级代码（Layer Codes），为 7 位值。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.5\_函数（Functions）

<a id="r_ga4e42b6d16b863ca374d032682e8c11fb"></a>

```c
static void net_mgmt_init_event_callback (struct net_mgmt_event_callback *cb, net_mgmt_event_handler_t handler, uint64_t mgmt_event_mask)
```

相关声明：[net_mgmt_init_event_callback](#ga4e42b6d16b863ca374d032682e8c11fb)、[net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)、[net_mgmt_event_handler_t](#ga2e83a5a769ac52c846f255e23aea84d2)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

正确初始化 `struct net_mgmt_event_callback` 的辅助接口（Helper）。

<a id="r_gae53f5bbc973b0f414107eca75ac0c26f"></a>

```c
void net_mgmt_add_event_callback (struct net_mgmt_event_callback *cb)
```

相关声明：[net_mgmt_add_event_callback](#gae53f5bbc973b0f414107eca75ac0c26f)、[net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)。

添加用户回调（User Callback）。

<a id="r_ga4960bfb01ecd891da72c57f17587f946"></a>

```c
void net_mgmt_del_event_callback (struct net_mgmt_event_callback *cb)
```

相关声明：[net_mgmt_del_event_callback](#ga4960bfb01ecd891da72c57f17587f946)、[net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)。

删除用户回调（User Callback）。

<a id="r_ga6415ec1e2e7f477c8976022ac33b0654"></a>

```c
void net_mgmt_event_notify_with_info (uint64_t mgmt_event, struct net_if *iface, const void *info, size_t length)
```

相关声明：[net_mgmt_event_notify_with_info](#ga6415ec1e2e7f477c8976022ac33b0654)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

供系统通知事件（Event）使用。

<a id="r_gabf710692e596a2d98f37b82da884a82a"></a>

```c
static void net_mgmt_event_notify (uint64_t mgmt_event, struct net_if *iface)
```

相关声明：[net_mgmt_event_notify](#gabf710692e596a2d98f37b82da884a82a)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

供系统通知不带附加信息（Additional Information）的事件使用。

<a id="r_ga7137c77c55ee2609941c88db79e22d1a"></a>

```c
int net_mgmt_event_wait (uint64_t mgmt_event_mask, uint64_t *raised_event, struct net_if **iface, const void **info, size_t *info_length, k_timeout_t timeout)
```

相关声明：[net_mgmt_event_wait](#ga7137c77c55ee2609941c88db79e22d1a)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

用于按事件掩码（Event Mask）同步等待。

<a id="r_ga3ab114106df41144c0fae8e6faad12cb"></a>

```c
int net_mgmt_event_wait_on_iface (struct net_if *iface, uint64_t mgmt_event_mask, uint64_t *raised_event, const void **info, size_t *info_length, k_timeout_t timeout)
```

相关声明：[net_mgmt_event_wait_on_iface](#ga3ab114106df41144c0fae8e6faad12cb)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

用于按事件掩码（Event Mask）同步等待指定接口（Iface）的事件。

<a id="r_gaab4fe2e9ea0657bf91fb1910af6729cc"></a>

```c
void net_mgmt_event_init (void)
```

相关声明：[net_mgmt_event_init](#gaab4fe2e9ea0657bf91fb1910af6729cc)。

供网络协议栈核心（Network Stack Core）初始化网络事件处理（Event Processing）使用。

## 5.6\_详细说明（Detailed Documentation）

<a id="gaa89b82a1890c55775f8c3c24e11f40e2"></a>

### `NET_EVENT_CAPTURE_STARTED`

```c
#define NET_EVENT_CAPTURE_STARTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CAPTURE_STARTED)
```

```c
#include <zephyr/net/net_event.h>
```

网络数据包捕获（Network Packet Capture）已启动。

<a id="gaa2b655aedd597636790409539b1f86cd"></a>

### `NET_EVENT_CAPTURE_STOPPED`

```c
#define NET_EVENT_CAPTURE_STOPPED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CAPTURE_STOPPED)
```

```c
#include <zephyr/net/net_event.h>
```

网络数据包捕获（Network Packet Capture）已停止。

<a id="ga5735d13f24c974ad6d4038c93edf05e0"></a>

### `NET_EVENT_DNS_SERVER_ADD`

```c
#define NET_EVENT_DNS_SERVER_ADD (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVER_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 DNS 服务器（DNS Server）时发出的事件。

<a id="ga9d406772e5d1ad2952b2a2e0fed05c73"></a>

### `NET_EVENT_DNS_SERVER_DEL`

```c
#define NET_EVENT_DNS_SERVER_DEL (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVER_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 DNS 服务器（DNS Server）时发出的事件。

<a id="gac654c28128762a3160ce5f5717f053c5"></a>

### `NET_EVENT_DNS_SERVERS_RECONFIGURED`

```c
#define NET_EVENT_DNS_SERVERS_RECONFIGURED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DNS_SERVERS_RECONFIGURED)
```

```c
#include <zephyr/net/net_event.h>
```

刷新 DNS 服务器配置（DNS Server Configuration）时发出的事件。

每次成功重新配置都会触发，即使新的服务器集合与现有集合相同也不例外。在集合相同的情况下，会有意抑制逐槽位的 ADD／DEL 差量事件，以免在 DHCP Offer 重传及 IPv6 路由器通告（RA）时取消正在进行的查询。如果使用方需要在网络事件之后收到“DNS 配置再次就绪”的信号，应监听此事件，而不是 `NET_EVENT_DNS_SERVER_ADD`。

此事件携带的 `iface` 载荷为 `NULL`，属于系统级事件（System-Level Event）。

<a id="gac5a7458d89e4a95564999dca3c1b9f1e"></a>

### `NET_EVENT_HOSTNAME_CHANGED`

```c
#define NET_EVENT_HOSTNAME_CHANGED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_HOSTNAME_CHANGED)
```

```c
#include <zephyr/net/net_event.h>
```

系统主机名（Hostname）改变时发出的事件。

<a id="gacb6ac7a4579be883abc9aa638299b0cd"></a>

### `NET_EVENT_IF_ADMIN_DOWN`

```c
#define NET_EVENT_IF_ADMIN_DOWN (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_ADMIN_DOWN)
```

```c
#include <zephyr/net/net_event.h>
```

手动停用（Down）网络接口时发出的事件。

<a id="ga94a52eb94cc2189919ade9c8c8f239bd"></a>

### `NET_EVENT_IF_ADMIN_UP`

```c
#define NET_EVENT_IF_ADMIN_UP (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_ADMIN_UP)
```

```c
#include <zephyr/net/net_event.h>
```

手动启用（Up）网络接口时发出的事件。

<a id="gac43a928bce3feb217b37ff7eb205e71b"></a>

### `NET_EVENT_IF_DOWN`

```c
#define NET_EVENT_IF_DOWN (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_DOWN)
```

```c
#include <zephyr/net/net_event.h>
```

网络接口转为停用（Down）状态时发出的事件。

<a id="gaddc84a60607bb27048397e29eb9107f5"></a>

### `NET_EVENT_IF_UP`

```c
#define NET_EVENT_IF_UP (NET_EVENT_IF_BASE | NET_EVENT_IF_CMD_UP)
```

```c
#include <zephyr/net/net_event.h>
```

网络接口转为启用（Up）状态时发出的事件。

<a id="ga9af1f8f4ba965e6d6e82a190ab4748a1"></a>

### `NET_EVENT_IPV4_ACD_CONFLICT`

```c
#define NET_EVENT_IPV4_ACD_CONFLICT (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_CONFLICT)
```

```c
#include <zephyr/net/net_event.h>
```

IPv4 地址已被确认可安全使用后，又检测到地址冲突（Address Conflict）时发出的事件。

在这种情况下如何处理，由应用决定。

<a id="ga3de741f5732473a1f49d9d0b93183549"></a>

### `NET_EVENT_IPV4_ACD_FAILED`

```c
#define NET_EVENT_IPV4_ACD_FAILED (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_FAILED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv4 地址冲突检测（Address Conflict Detection）失败时发出的事件。

<a id="ga5293377de1fdc79e7564f4e5104a07c2"></a>

### `NET_EVENT_IPV4_ACD_SUCCEED`

```c
#define NET_EVENT_IPV4_ACD_SUCCEED (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ACD_SUCCEED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv4 地址冲突检测（Address Conflict Detection）成功时发出的事件。

<a id="gad422365df617ce1473412908738048f0"></a>

### `NET_EVENT_IPV4_ADDR_ADD`

```c
#define NET_EVENT_IPV4_ADDR_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ADDR_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 IPv4 地址（Address）时发出的事件。

<a id="ga0d78644f799d1d8f5c18ec9860582817"></a>

### `NET_EVENT_IPV4_ADDR_DEL`

```c
#define NET_EVENT_IPV4_ADDR_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ADDR_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 IPv4 地址（Address）时发出的事件。

<a id="ga7461ef85f4f8433851cb7583468c00cb"></a>

### `NET_EVENT_IPV4_DHCP_BOUND`

```c
#define NET_EVENT_IPV4_DHCP_BOUND (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_BOUND)
```

```c
#include <zephyr/net/net_event.h>
```

IPv4 DHCP 客户端地址绑定（Bound）时发出的事件。

<a id="ga2d3a9351c226b1542d1b2f469b77233a"></a>

### `NET_EVENT_IPV4_DHCP_START`

```c
#define NET_EVENT_IPV4_DHCP_START (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_START)
```

```c
#include <zephyr/net/net_event.h>
```

IPv4 DHCP 客户端（Client）启动时发出的事件。

<a id="gabc06b6010780ab2d1e4f88227965b4e7"></a>

### `NET_EVENT_IPV4_DHCP_STOP`

```c
#define NET_EVENT_IPV4_DHCP_STOP (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_DHCP_STOP)
```

```c
#include <zephyr/net/net_event.h>
```

IPv4 DHCP 客户端（Client）停止时发出的事件。

<a id="ga854e897d09eecccc83d04d86fbba5b64"></a>

### `NET_EVENT_IPV4_MADDR_ADD`

```c
#define NET_EVENT_IPV4_MADDR_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MADDR_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 IPv4 组播地址（Multicast Address）时发出的事件。

<a id="ga303824277664ee64674b7c93ff865bb4"></a>

### `NET_EVENT_IPV4_MADDR_DEL`

```c
#define NET_EVENT_IPV4_MADDR_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MADDR_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 IPv4 组播地址（Multicast Address）时发出的事件。

<a id="ga17ad57d81f3046555f94f75dc6d31ec1"></a>

### `NET_EVENT_IPV4_MCAST_JOIN`

```c
#define NET_EVENT_IPV4_MCAST_JOIN (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MCAST_JOIN)
```

```c
#include <zephyr/net/net_event.h>
```

加入 IPv4 组播组（Multicast Group）时发出的事件。

<a id="ga3cbb8a9dfec8435b93d908171ab944c9"></a>

### `NET_EVENT_IPV4_MCAST_LEAVE`

```c
#define NET_EVENT_IPV4_MCAST_LEAVE (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_MCAST_LEAVE)
```

```c
#include <zephyr/net/net_event.h>
```

离开 IPv4 组播组（Multicast Group）时发出的事件。

<a id="ga24766ef249022c198299d38e95f400b9"></a>

### `NET_EVENT_IPV4_PMTU_CHANGED`

```c
#define NET_EVENT_IPV4_PMTU_CHANGED (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_PMTU_CHANGED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv4 路径最大传输单元（Path MTU）已改变。

<a id="ga766d04b6b789c1c966c2e2149a3e1229"></a>

### `NET_EVENT_IPV4_ROUTE_ADD`

```c
#define NET_EVENT_IPV4_ROUTE_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTE_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 IPv4 路由（Route）时发出的事件。

<a id="ga1d7b96d88f846eb58db7867ffc96c2ea"></a>

### `NET_EVENT_IPV4_ROUTE_DEL`

```c
#define NET_EVENT_IPV4_ROUTE_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTE_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 IPv4 路由（Route）时发出的事件。

<a id="ga740c97a7e94181ad734888bbe7b0a3d0"></a>

### `NET_EVENT_IPV4_ROUTER_ADD`

```c
#define NET_EVENT_IPV4_ROUTER_ADD (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTER_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 IPv4 路由器（Router）时发出的事件。

<a id="gae45a3b6a5f4b72edc51e06a22b88239a"></a>

### `NET_EVENT_IPV4_ROUTER_DEL`

```c
#define NET_EVENT_IPV4_ROUTER_DEL (NET_EVENT_IPV4_BASE | NET_EVENT_IPV4_CMD_ROUTER_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 IPv4 路由器（Router）时发出的事件。

<a id="ga20125c6148169a91fbebab1ebba17be3"></a>

### `NET_EVENT_IPV6_ADDR_ADD`

```c
#define NET_EVENT_IPV6_ADDR_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 IPv6 地址（Address）时发出的事件。

<a id="ga61f243efbc25928815ec78305b4f000e"></a>

### `NET_EVENT_IPV6_ADDR_DEL`

```c
#define NET_EVENT_IPV6_ADDR_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 IPv6 地址（Address）时发出的事件。

<a id="ga6cc42e3ca8197e46809de6082602ab98"></a>

### `NET_EVENT_IPV6_ADDR_DEPRECATED`

```c
#define NET_EVENT_IPV6_ADDR_DEPRECATED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ADDR_DEPRECATED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv6 地址已弃用（Deprecated）。

<a id="ga0d5013ea3a6fa3bddd5cb182dd616151"></a>

### `NET_EVENT_IPV6_DAD_FAILED`

```c
#define NET_EVENT_IPV6_DAD_FAILED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DAD_FAILED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv6 重复地址检测（Duplicate Address Detection）失败时发出的事件。

<a id="ga8711b4b1e88c897196b982e4d56968f1"></a>

### `NET_EVENT_IPV6_DAD_SUCCEED`

```c
#define NET_EVENT_IPV6_DAD_SUCCEED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DAD_SUCCEED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv6 重复地址检测（Duplicate Address Detection）成功时发出的事件。

<a id="gaff89dbc7562a85e9ff073b507bdf06e3"></a>

### `NET_EVENT_IPV6_DHCP_BOUND`

```c
#define NET_EVENT_IPV6_DHCP_BOUND (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_BOUND)
```

```c
#include <zephyr/net/net_event.h>
```

IPv6 DHCP 客户端地址绑定（Bound）时发出的事件。

<a id="gaa07a5e8779ec24e5ab883970bcec6c5e"></a>

### `NET_EVENT_IPV6_DHCP_START`

```c
#define NET_EVENT_IPV6_DHCP_START (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_START)
```

```c
#include <zephyr/net/net_event.h>
```

IPv6 DHCP 客户端（Client）启动时发出的事件。

<a id="gaab05d5a65ef5f9ed147e32ce380f7de4"></a>

### `NET_EVENT_IPV6_DHCP_STOP`

```c
#define NET_EVENT_IPV6_DHCP_STOP (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_DHCP_STOP)
```

```c
#include <zephyr/net/net_event.h>
```

IPv6 DHCP 客户端（Client）停止时发出的事件。

<a id="gadda9dccf913a4dcb4d12b2b1fe5d403c"></a>

### `NET_EVENT_IPV6_MADDR_ADD`

```c
#define NET_EVENT_IPV6_MADDR_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MADDR_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 IPv6 组播地址（Multicast Address）时发出的事件。

<a id="ga035db32f66effd2407e0cca4b1fd9ea3"></a>

### `NET_EVENT_IPV6_MADDR_DEL`

```c
#define NET_EVENT_IPV6_MADDR_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MADDR_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 IPv6 组播地址（Multicast Address）时发出的事件。

<a id="ga287d37bae2d74e0c85de59c5e23d409a"></a>

### `NET_EVENT_IPV6_MCAST_JOIN`

```c
#define NET_EVENT_IPV6_MCAST_JOIN (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MCAST_JOIN)
```

```c
#include <zephyr/net/net_event.h>
```

加入 IPv6 组播组（Multicast Group）时发出的事件。

<a id="ga862d1b2ce9b65c0806ef77909364a58d"></a>

### `NET_EVENT_IPV6_MCAST_LEAVE`

```c
#define NET_EVENT_IPV6_MCAST_LEAVE (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_MCAST_LEAVE)
```

```c
#include <zephyr/net/net_event.h>
```

离开 IPv6 组播组（Multicast Group）时发出的事件。

<a id="ga96fe7da048fe4d59435b7337626d4af7"></a>

### `NET_EVENT_IPV6_NBR_ADD`

```c
#define NET_EVENT_IPV6_NBR_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_NBR_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 IPv6 邻居（Neighbor）时发出的事件。

<a id="ga5be1cdfeb1b8da485b1042a7b2dc14e4"></a>

### `NET_EVENT_IPV6_NBR_DEL`

```c
#define NET_EVENT_IPV6_NBR_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_NBR_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 IPv6 邻居（Neighbor）时发出的事件。

<a id="gaba20579e42c4cebc8c3ac9a40ff384f3"></a>

### `NET_EVENT_IPV6_PE_DISABLED`

```c
#define NET_EVENT_IPV6_PE_DISABLED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_DISABLED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv6 隐私扩展（Privacy Extension）已禁用。

<a id="ga95f7a737a39fb655d3577405e70e04ba"></a>

### `NET_EVENT_IPV6_PE_ENABLED`

```c
#define NET_EVENT_IPV6_PE_ENABLED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_ENABLED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv6 隐私扩展（Privacy Extension）已启用。

<a id="ga19d671971cf07e76580db8098ab32971"></a>

### `NET_EVENT_IPV6_PE_FILTER_ADD`

```c
#define NET_EVENT_IPV6_PE_FILTER_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_FILTER_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

已添加 IPv6 隐私扩展过滤器（Privacy Extension Filter）。

<a id="gaf2f1c4b8dc5b9b07985265cee6a90f70"></a>

### `NET_EVENT_IPV6_PE_FILTER_DEL`

```c
#define NET_EVENT_IPV6_PE_FILTER_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PE_FILTER_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

已移除 IPv6 隐私扩展过滤器（Privacy Extension Filter）。

<a id="gae0e1924aa8c8f6dc47582883528df185"></a>

### `NET_EVENT_IPV6_PMTU_CHANGED`

```c
#define NET_EVENT_IPV6_PMTU_CHANGED (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PMTU_CHANGED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv6 路径最大传输单元（Path MTU）已改变。

<a id="ga392414b95838bca1e55e4342870a8333"></a>

### `NET_EVENT_IPV6_PREFIX_ADD`

```c
#define NET_EVENT_IPV6_PREFIX_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PREFIX_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 IPv6 前缀（Prefix）时发出的事件。

<a id="gab06f93335938a635966e85a18b5b0cf6"></a>

### `NET_EVENT_IPV6_PREFIX_DEL`

```c
#define NET_EVENT_IPV6_PREFIX_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_PREFIX_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 IPv6 前缀（Prefix）时发出的事件。

<a id="gad19b5e742ded9b3ed673d8f7985100fd"></a>

### `NET_EVENT_IPV6_ROUTE_ADD`

```c
#define NET_EVENT_IPV6_ROUTE_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTE_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 IPv6 路由（Route）时发出的事件。

<a id="gae6f68ec69032ac049f072d6ed164987c"></a>

### `NET_EVENT_IPV6_ROUTE_DEL`

```c
#define NET_EVENT_IPV6_ROUTE_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTE_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 IPv6 路由（Route）时发出的事件。

<a id="gaae932293528aa40127a906c3dbd45e31"></a>

### `NET_EVENT_IPV6_ROUTER_ADD`

```c
#define NET_EVENT_IPV6_ROUTER_ADD (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTER_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 IPv6 路由器（Router）时发出的事件。

<a id="ga8d4b7798981aaaf3aea2b793739143b7"></a>

### `NET_EVENT_IPV6_ROUTER_DEL`

```c
#define NET_EVENT_IPV6_ROUTER_DEL (NET_EVENT_IPV6_BASE | NET_EVENT_IPV6_CMD_ROUTER_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 IPv6 路由器（Router）时发出的事件。

<a id="gacbd2b10cc345359c07de4a62eb172a09"></a>

### `NET_EVENT_L4_CONNECTED`

```c
#define NET_EVENT_L4_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_CONNECTED)
```

```c
#include <zephyr/net/net_event.h>
```

系统被视为已连接（Connected）时发出的事件。

此处的已连接（Connected）指网络接口已启用（Up），且已经为接口分配 IPv4 或 IPv6 地址。

<a id="gacd9e0b5e2f540794b20f11b070ffbd65"></a>

### `NET_EVENT_L4_DISCONNECTED`

```c
#define NET_EVENT_L4_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_DISCONNECTED)
```

```c
#include <zephyr/net/net_event.h>
```

系统不再处于已连接（Connected）状态时发出的事件。

通常意味着网络连通性（Network Connectivity）已丢失，例如网络接口停用（Down），或接口不再拥有 IP 地址等。

<a id="ga13635b6d7a152faa81d09b6285aeedf9"></a>

### `NET_EVENT_L4_IF_CONNECTED`

```c
#define NET_EVENT_L4_IF_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IF_CONNECTED)
```

```c
#include <zephyr/net/net_event.h>
```

接口被视为已连接（Connected）时发出的事件。

<a id="ga25300c6b7a8e38f058555493edaefe04"></a>

### `NET_EVENT_L4_IF_DISCONNECTED`

```c
#define NET_EVENT_L4_IF_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IF_DISCONNECTED)
```

```c
#include <zephyr/net/net_event.h>
```

接口不被视为已连接（Connected）时发出的事件。

<a id="ga532fdc2f199e047a5d17e325cee12cf1"></a>

### `NET_EVENT_L4_IPV4_CONNECTED`

```c
#define NET_EVENT_L4_IPV4_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV4_CONNECTED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv4 网络连通性（Network Connectivity）可用时触发的事件。

<a id="gaa92cc806d93446d548a05edb8e0074c2"></a>

### `NET_EVENT_L4_IPV4_DISCONNECTED`

```c
#define NET_EVENT_L4_IPV4_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV4_DISCONNECTED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv4 网络连通性（Network Connectivity）丢失时发出的事件。

<a id="gaf6bb88ed90df5aacb40e42fcc5bfbcf5"></a>

### `NET_EVENT_L4_IPV6_CONNECTED`

```c
#define NET_EVENT_L4_IPV6_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV6_CONNECTED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv6 网络连通性（Network Connectivity）可用时发出的事件。

<a id="gac81abeab44fbf2b6f29d4e11a1e1bd17"></a>

### `NET_EVENT_L4_IPV6_DISCONNECTED`

```c
#define NET_EVENT_L4_IPV6_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_IPV6_DISCONNECTED)
```

```c
#include <zephyr/net/net_event.h>
```

IPv6 网络连通性（Network Connectivity）丢失时发出的事件。

<a id="gabfb799347776323486fb0d4563e31b3b"></a>

### `NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD`

```c
#define NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD (NET_EVENT_PACKET_BASE | NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

添加分组套接字（Packet Socket）的组播组成员资格（Multicast Group Membership）时发出的事件。

<a id="gaec5574f6308a89db36c2793bce6d5dcb"></a>

### `NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP`

```c
#define NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP (NET_EVENT_PACKET_BASE | NET_EVENT_PACKET_CMD_MCAST_MEMBERSHIP_DROP)
```

```c
#include <zephyr/net/net_event.h>
```

移除分组套接字（Packet Socket）的组播组成员资格（Multicast Group Membership）时发出的事件。

<a id="ga8084de14ebd35b4d32075642e952ca4d"></a>

### `NET_EVENT_VPN_CONNECTED`

```c
#define NET_EVENT_VPN_CONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_CONNECTED)
```

```c
#include <zephyr/net/net_event.h>
```

VPN 网络连通性（Network Connectivity）可用时发出的事件。

<a id="ga74e837120225c10f0ccfa38696051cb8"></a>

### `NET_EVENT_VPN_DISCONNECTED`

```c
#define NET_EVENT_VPN_DISCONNECTED (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_DISCONNECTED)
```

```c
#include <zephyr/net/net_event.h>
```

VPN 网络连通性（Network Connectivity）丢失时发出的事件。

<a id="gace9ee5cff7234717a9f183b89dcd28a3"></a>

### `NET_EVENT_VPN_PEER_ADD`

```c
#define NET_EVENT_VPN_PEER_ADD (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_PEER_ADD)
```

```c
#include <zephyr/net/net_event.h>
```

向系统添加 VPN 对等端（Peer）时发出的事件。

<a id="ga03f4fcb1977379401e2b6ea83ad37883"></a>

### `NET_EVENT_VPN_PEER_DEL`

```c
#define NET_EVENT_VPN_PEER_DEL (NET_EVENT_L4_BASE | NET_EVENT_L4_CMD_VPN_PEER_DEL)
```

```c
#include <zephyr/net/net_event.h>
```

从系统移除 VPN 对等端（Peer）时发出的事件。

<a id="ga40e0f9fc86812ad9f6fe174b4c3804e6"></a>

### `net_mgmt`

```c
#define net_mgmt ( _mgmt_request, _iface, _data, _len )
```

```c
#include <zephyr/net/net_mgmt.h>
```

展开值（Value）：

```c
net_mgmt_##_mgmt_request(_mgmt_request, _iface, _data, _len)
```

生成网络管理事件（Network Management Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_mgmt_request` | 管理事件标识符（Management Event Identifier）。 |
| `_iface` | 网络接口（Network Interface） |
| `_data` | 事件的任何附加数据（Additional Data）。 |
| `_len` | 附加数据的长度。 |

<a id="ga08bde8717fd8e12a338c517b22b87776"></a>

### `NET_MGMT_DEFINE_REQUEST_HANDLER`

```c
#define NET_MGMT_DEFINE_REQUEST_HANDLER ( _mgmt_request)
```

```c
#include <zephyr/net/net_mgmt.h>
```

展开值（Value）：

```c
extern int net_mgmt_##_mgmt_request(uint64_t mgmt_request,      \
                                    struct net_if *iface,       \
                                    void *data, size_t len)
```

为给定网络事件（Network Event）声明请求处理函数（Request Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_mgmt_request` | 管理事件标识符（Management Event Identifier）。 |

<a id="ga3a6ca8a72ab12afd4f9b0461253eaa12"></a>

### `NET_MGMT_REGISTER_EVENT_HANDLER`

```c
#define NET_MGMT_REGISTER_EVENT_HANDLER ( _name, _event_mask, _func, _user_data )
```

```c
#include <zephyr/net/net_mgmt.h>
```

展开值（Value）：

```c
const STRUCT_SECTION_ITERABLE(net_mgmt_event_static_handler, _name) = { \
        .event_mask = _event_mask,                                      \
        .handler = _func,                                               \
        .user_data = (void *)_user_data,                                \
}
```

定义静态网络事件处理程序（Static Network Event Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 事件处理函数（Event Handler）的名称。 |
| `_event_mask` | 网络事件掩码（Event Mask），指定哪些事件到达时应调用传入的处理函数。注意，只有命令部分按掩码处理，可匹配一个或多个命令；层（Layer）和层代码（Layer Code）采用精确匹配。因此，要接收来自多个层的事件，必须为每个要监听的层分别注册一个监听器。 |
| `_func` | 网络事件发出时要调用的函数。 |
| `_user_data` | 调用网络事件处理函数时传入的用户数据（User Data）。 |

<a id="gab67d09d1e65b806ec1957451cbf60501"></a>

### `NET_MGMT_REGISTER_REQUEST_HANDLER`

```c
#define NET_MGMT_REGISTER_REQUEST_HANDLER ( _mgmt_request, _func )
```

```c
#include <zephyr/net/net_mgmt.h>
```

展开值（Value）：

```c
FUNC_ALIAS(_func, net_mgmt_##_mgmt_request, int)
```

为给定网络事件（Network Event）创建请求处理函数（Request Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_mgmt_request` | 管理事件标识符（Management Event Identifier）。 |
| `_func` | 处理此事件的函数。 |

<a id="ga2e83a5a769ac52c846f255e23aea84d2"></a>

### `net_mgmt_event_handler_t`

```c
typedef void(* net_mgmt_event_handler_t) (struct net_mgmt_event_callback *cb, uint64_t mgmt_event, struct net_if *iface)
```

```c
#include <zephyr/net/net_mgmt.h>
```

定义用户回调处理函数签名（Callback Handler Function Signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 拥有此处理函数的原始 `struct net_mgmt_event_callback`。 |
| `mgmt_event` | 正在通知的网络事件（Network Event）。 |
| `iface` | 如果事件属于某个接口，则为指向该接口 `struct net_if` 的指针；否则为 `NULL`。 |

<a id="gaf3773f8e945c4ec05b2fab46cd8b1881"></a>

### `net_mgmt_event_static_handler_t`

```c
typedef void(* net_mgmt_event_static_handler_t) (uint64_t mgmt_event, struct net_if *iface, void *info, size_t info_length, void *user_data)
```

```c
#include <zephyr/net/net_mgmt.h>
```

定义用户回调处理函数签名（Callback Handler Function Signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mgmt_event` | 正在通知的网络事件（Network Event）。 |
| `iface` | 如果事件属于某个接口，则为指向该接口 `struct net_if` 的指针；否则为 `NULL`。 |
| `info` | 指向处理函数能够理解的数据的有效指针；否则为 `NULL`。 |
| `info_length` | `info` 所指内存的长度，单位为字节。 |
| `user_data` | 用户提供给处理函数的数据。 |

<a id="ga78b9302193bd0c5cc35d81d298a5eb6b"></a>

### `net_mgmt_request_handler_t`

```c
typedef int(* net_mgmt_request_handler_t) (uint64_t mgmt_request, struct net_if *iface, void *data, size_t len)
```

```c
#include <zephyr/net/net_mgmt.h>
```

所有网络管理（Net MGMT）请求处理程序必须遵循的函数签名（Signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mgmt_request` | 调用此处理函数时使用的确切请求值（Request Value）。 |
| `iface` | 如果请求关联某个网络接口，则为指向 `struct net_if` 的有效指针；否则为 `NULL`。 |
| `data` | 指向处理函数能够理解的数据的有效指针；否则为 `NULL`。 |
| `len` | `data` 所指内存的长度，单位为字节。 |

<a id="ga5e6911455b9ab9f4c82780001459461a"></a>

### `net_mgmt_layer_code`

```c
enum net_mgmt_layer_code
```

```c
#include <zephyr/net/net_mgmt.h>
```

集中定义层级代码（Layer Codes），为 7 位值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_MGMT_LAYER_CODE_UNKNOWN` | 未知层代码（Unknown Layer Code），请勿使用。 |
| `NET_MGMT_LAYER_CODE_IFACE` | 网络接口层代码（Network Interface Layer Code）。 |
| `NET_MGMT_LAYER_CODE_CONN` | 连通性层代码（Connectivity Layer Code）。 |
| `NET_MGMT_LAYER_CODE_IPV4` | IPv4 层代码（Layer Code）。 |
| `NET_MGMT_LAYER_CODE_IPV6` | IPv6 层代码（Layer Code）。 |
| `NET_MGMT_LAYER_CODE_L4` | 第 4 层代码（L4 Layer Code）。 |
| `NET_MGMT_LAYER_CODE_COAP` | CoAP 层代码（Layer Code）。 |
| `NET_MGMT_LAYER_CODE_STATS` | 统计层代码（Statistics Layer Code）。 |
| `NET_MGMT_LAYER_CODE_HOSTAP` | Hostap（wpa_supplicant）层代码（Layer Code）。 |
| `NET_MGMT_LAYER_CODE_ETHERNET` | 以太网层代码（Ethernet Layer Code）。 |
| `NET_MGMT_LAYER_CODE_IEEE802514` | IEEE 802.15.4 层代码（Layer Code）。 |
| `NET_MGMT_LAYER_CODE_PPP` | PPP 层代码（Layer Code）。 |
| `NET_MGMT_LAYER_CODE_VIRTUAL` | 虚拟网络接口层代码（Virtual Network Interface Layer Code）。 |
| `NET_MGMT_LAYER_CODE_WIFI` | Wi-Fi 层代码（Layer Code）。 |
| `NET_MGMT_LAYER_CODE_PACKET` | 分组层代码（Packet Layer Code，L2）。 |
| `NET_MGMT_LAYER_CODE_USER3` | 用户层代码 3（User Layer Code 3）。 |
| `NET_MGMT_LAYER_CODE_USER2` | 用户层代码 2（User Layer Code 2）。 |
| `NET_MGMT_LAYER_CODE_USER1` | 用户层代码 1（User Layer Code 1）。 |
| `NET_MGMT_LAYER_CODE_RESERVED` | 保留供将来使用的层代码（layer code）。 |

<a id="gae53f5bbc973b0f414107eca75ac0c26f"></a>

### `net_mgmt_add_event_callback()`

```c
void net_mgmt_add_event_callback ( struct net_mgmt_event_callback * cb)
```

```c
#include <zephyr/net/net_mgmt.h>
```

添加用户回调（User Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向要添加的用户回调（Callback）的有效指针。 |

<a id="ga4960bfb01ecd891da72c57f17587f946"></a>

### `net_mgmt_del_event_callback()`

```c
void net_mgmt_del_event_callback ( struct net_mgmt_event_callback * cb)
```

```c
#include <zephyr/net/net_mgmt.h>
```

删除用户回调（User Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向要删除的用户回调（Callback）的有效指针。 |

<a id="gaab4fe2e9ea0657bf91fb1910af6729cc"></a>

### `net_mgmt_event_init()`

```c
void net_mgmt_event_init ( void )
```

```c
#include <zephyr/net/net_mgmt.h>
```

供网络协议栈核心（Network Stack Core）初始化网络事件处理（Event Processing）使用。

<a id="gabf710692e596a2d98f37b82da884a82a"></a>

### `net_mgmt_event_notify()`

```c
void net_mgmt_event_notify ( uint64_t mgmt_event, struct net_if * iface )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_mgmt.h>
```

供系统通知不带附加信息（Additional Information）的事件使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mgmt_event` | 实际要通知的网络事件代码（Network Event Code）。 |
| `iface` | 仅当事件基于某个接口时，为指向 `struct net_if` 的有效指针；否则为 `NULL`。 |

<a id="ga6415ec1e2e7f477c8976022ac33b0654"></a>

### `net_mgmt_event_notify_with_info()`

```c
void net_mgmt_event_notify_with_info ( uint64_t mgmt_event, struct net_if * iface, const void * info, size_t length )
```

```c
#include <zephyr/net/net_mgmt.h>
```

供系统通知事件（Event）使用。

注（Note）：未定义 `CONFIG_NET_MGMT_EVENT_INFO` 时，`info` 和 `length` 被禁用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mgmt_event` | 实际要通知的网络事件代码（Network Event Code）。 |
| `iface` | 仅当事件基于某个接口时，为指向 `struct net_if` 的有效指针；否则为 `NULL`。 |
| `info` | 指向希望随事件一起传递的信息的有效指针；否则为 `NULL`。注意，所指数据的格式由相关事件规定。 |
| `length` | `info` 指针所指数据的大小。 |

<a id="ga7137c77c55ee2609941c88db79e22d1a"></a>

### `net_mgmt_event_wait()`

```c
int net_mgmt_event_wait ( uint64_t mgmt_event_mask, uint64_t * raised_event, struct net_if ** iface, const void ** info, size_t * info_length, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_mgmt.h>
```

用于按事件掩码（Event Mask）同步等待。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mgmt_event_mask` | 要等待的相关事件的掩码（Event Mask）。 |
| `raised_event` | 指向 `uint64_t` 的指针，用于获取掩码中实际触发的是哪个事件。调用者不需要此信息时可为 `NULL`。 |
| `iface` | 指向接口指针存储位置的指针，用于接收事件来源接口。只有按调用者要监听的事件，在事件掩码中相应设置了 `NET_MGMT_IFACE_BIT` 位时才有效。 |
| `info` | 若用户希望获取事件可能附带的信息，则传入有效指针；否则为 `NULL`。 |
| `info_length` | 给出 `info` 内存区域的长度。仅当 `info` 不为 `NULL` 时有效。 |
| `timeout` | 超时时长（Timeout Delay）。可使用 `K_FOREVER` 无限等待。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，否则为负错误码。若因超时而非实际事件返回，则明确返回 `-ETIMEDOUT`。

<a id="ga3ab114106df41144c0fae8e6faad12cb"></a>

### `net_mgmt_event_wait_on_iface()`

```c
int net_mgmt_event_wait_on_iface ( struct net_if * iface, uint64_t mgmt_event_mask, uint64_t * raised_event, const void ** info, size_t * info_length, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_mgmt.h>
```

用于按事件掩码（Event Mask）同步等待指定接口（Iface）的事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向要监听其事件的有效网络接口的指针。 |
| `mgmt_event_mask` | 要等待的相关事件掩码（Event Mask）。监听的事件应为接口相关事件，因此必须设置 `NET_MGMT_IFACE_BIT` 位。 |
| `raised_event` | 指向 `uint64_t` 的指针，用于获取掩码中实际触发的是哪个事件。调用者不需要此信息时可为 `NULL`。 |
| `info` | 若用户希望获取事件可能附带的信息，则传入有效指针；否则为 `NULL`。 |
| `info_length` | 给出 `info` 内存区域的长度。仅当 `info` 不为 `NULL` 时有效。 |
| `timeout` | 超时时长（Timeout Delay）。可使用 `K_FOREVER` 无限等待。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，否则为负错误码。若因超时而非实际事件返回，则明确返回 `-ETIMEDOUT`。

<a id="ga4e42b6d16b863ca374d032682e8c11fb"></a>

### `net_mgmt_init_event_callback()`

```c
void net_mgmt_init_event_callback ( struct net_mgmt_event_callback * cb, net_mgmt_event_handler_t handler, uint64_t mgmt_event_mask )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_mgmt.h>
```

正确初始化 `struct net_mgmt_event_callback` 的辅助接口（Helper）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 有效的应用回调结构体指针。 |
| `handler` | 有效的处理函数指针（Handler Function Pointer）。 |
| `mgmt_event_mask` | 处理函数所关注的事件掩码（Event Mask）。 |


## 5.7\_原页交叉引用（Cross References）

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
- [net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [zephyr/net/net_event.h](../api_file_gap_modem_reference/P004_zephyr__net__net_event.h_文件参考.md)
- [zephyr/net/net_mgmt.h](../api_file_storage_event_reference/P015_zephyr__net__net_mgmt.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructnet__if_html"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa3206e13330183c74d20e89407e11c7cd"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa2e23e545f7d78775adb5271f7bf42518"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aabf1c9ef98fb7237ba1591108c67bf1d7"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa25c33c6faa9d22f4ac5b70049bb4bbd2"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa8f1f092ecdfcf341458e7389cee3ace8"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aab60d69e5ee62cb0212b1e424d7847b4e"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa5701861bfb5fae92e8c7b08ea02f61a7"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa3ab69a93464d5fa0d5be9ac9f3757cb6"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa06935e2c46523b1a3f414f4c981992fc"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aafd0569a3f3cde9e892751a84b74836b4"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa4893c212a3026909dcb8663abbdf2b2b"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa52b23f5afbf235bef6bc2aeea69271c1"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aac767c8da93a6d0f5a53e64cbfdf94fca"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa7f2f4d110d3003974bd0da0154c2d789"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa997785b24761b410a1d33788c46f90b1"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa4e57a620f5778d346984398c0e786977"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aaa335a8c82c6d7614337e3501a69aa1d4"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aa10876d890aac72553ab69c0964bef48a"></a>
<a id="gga5e6911455b9ab9f4c82780001459461aaef64c0749996046b313ebf366b3eab75"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_集成电路间音频总线（I2S）.md) · [返回大纲](大纲.md) · [下一章](P006_Prometheus API API主题.md)
