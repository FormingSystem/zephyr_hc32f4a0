---
id: learning.zephyr-docs.api-file-modem-network-reference.page-3
title: zephyr__net__net_if.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_net\_\_net\_if.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络接口（Network Interface）的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/net_core.h>
#include <zephyr/net/hostname.h>
#include <zephyr/net/net_linkaddr.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_l2.h>
#include <zephyr/net/net_stats.h>
#include <zephyr/net/net_timeout.h>
#include <zephyr/net/prometheus/collector.h>
#include <zephyr/syscalls/net_if.h>
```

查看此文件的源码。

网络接口（Network Interface）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_net_5Fif_5Faddr"></a>

```c
struct net_if_addr
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)。

网络接口的单播IP地址（Unicast IP Addresses）。

<a id="r_net_5Fif_5Fmcast_5Faddr"></a>

```c
struct net_if_mcast_addr
```

相关声明：[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

网络接口的组播IP地址（Multicast IP Addresses）。

<a id="r_net_5Fif_5Fipv6_5Fprefix"></a>

```c
struct net_if_ipv6_prefix
```

相关声明：[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)。

网络接口的IPv6前缀（Prefixes）。

<a id="r_net_5Fif_5Frouter"></a>

```c
struct net_if_router
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)。

系统中路由器（Routers）的信息。

<a id="r_net_5Fif_5Fipv6"></a>

```c
struct net_if_ipv6
```

相关声明：[net_if_ipv6](../network_core_model_reference/P086_net_if_ipv6_结构体.md)。

IPv6配置（Configuration）。

<a id="r_net_5Fif_5Faddr_5Fipv4"></a>

```c
struct net_if_addr_ipv4
```

相关声明：[net_if_addr_ipv4](../network_core_model_reference/P081_net_if_addr_ipv4_结构体.md)。

网络接口的单播IPv4地址及网络掩码（Netmask）。

<a id="r_net_5Fif_5Fipv4"></a>

```c
struct net_if_ipv4
```

相关声明：[net_if_ipv4](../network_core_model_reference/P085_net_if_ipv4_结构体.md)。

IPv4配置（Configuration）。

<a id="r_net_5Fif_5Fip"></a>

```c
struct net_if_ip
```

相关声明：[net_if_ip](../network_core_model_reference/P084_net_if_ip_结构体.md)。

网络接口的IP地址配置（IP Address Configuration）。

<a id="r_net_5Fif_5Fconfig"></a>

```c
struct net_if_config
```

相关声明：[net_if_config](../network_core_model_reference/P082_net_if_config_结构体.md)。

网络接口的IP及其他配置相关数据（Configuration Related Data）。

<a id="r_net_5Ftraffic_5Fclass"></a>

```c
struct net_traffic_class
```

相关声明：[net_traffic_class](../network_core_model_reference/P154_net_traffic_class_结构体.md)。

网络流量类别（Network Traffic Class）。

<a id="r_net_5Fif_5Fdev"></a>

```c
struct net_if_dev
```

相关声明：[net_if_dev](../network_core_model_reference/P083_net_if_dev_结构体.md)。

网络接口设备（Network Interface Device）结构。

<a id="r_net_5Fif"></a>

```c
struct net_if
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

网络接口（Network Interface）结构。

<a id="r_net_5Fif_5Fmcast_5Fmonitor"></a>

```c
struct net_if_mcast_monitor
```

相关声明：[net_if_mcast_monitor](../network_core_model_reference/P090_net_if_mcast_monitor_结构体.md)。

组播监测处理程序（Multicast Monitor Handler）的结构。

<a id="r_net_5Fif_5Flink_5Fcb"></a>

```c
struct net_if_link_cb
```

相关声明：[net_if_link_cb](../network_core_model_reference/P088_net_if_link_cb_结构体.md)。

链路回调处理程序（Link Callback Handler）的结构。

<a id="r_net_5Fif_5Ftimestamp_5Fcb"></a>

```c
struct net_if_timestamp_cb
```

相关声明：[net_if_timestamp_cb](../network_core_model_reference/P092_net_if_timestamp_cb_结构体.md)。

时间戳回调处理程序（Timestamp Callback Handler）的结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga2b824eff0adada3eb7ff626a8d7c3538"></a>

```c
#define NET_IF_IPV6_DAD_NONCE_LEN 6U
```

相关声明：[NET_IF_IPV6_DAD_NONCE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2b824eff0adada3eb7ff626a8d7c3538)。

RFC 7527 第 4 节定义的增强型重复地址检测（Enhanced DAD）的随机数（Nonce）载荷长度，单位为字节。

<a id="r_ga021e9877ee9532a899a298d6a2c7aeb2"></a>

```c
#define NET_IPV6_MAX_REACHABLE_TIME 3600000U
```

相关声明：[NET_IPV6_MAX_REACHABLE_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga021e9877ee9532a899a298d6a2c7aeb2)。

IPv6 基础可达时间（Base Reachable Time）的最大值，单位为毫秒。

<a id="r_gae0fdb0b909e06ba7831e53700c32b84f"></a>

```c
#define NET_IF_DECLARE(dev_id, inst)
```

相关声明：[NET_IF_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae0fdb0b909e06ba7831e53700c32b84f)。

网络接口（Network Interface）的前向声明（Forward Declaration）。

<a id="r_ga65e4d856b53096bf784a4d5a495ca507"></a>

```c
#define NET_IF_DT_DECLARE(node_id, instance)
```

相关声明：[NET_IF_DT_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga65e4d856b53096bf784a4d5a495ca507)。

网络接口（Network Interface）的前向声明（Forward Declaration）。

<a id="r_ga421f0b8be2317c0865c50ca588f73509"></a>

```c
#define NET_IF_DT_INST_DECLARE(inst, ...)
```

相关声明：[NET_IF_DT_INST_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga421f0b8be2317c0865c50ca588f73509)。

网络接口（Network Interface）的前向声明（Forward Declaration）。

<a id="r_gadd040e5cc26a96c3f66f37539178c3b6"></a>

```c
#define NET_IF_DT_GET(node_id, instance)
```

相关声明：[NET_IF_DT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadd040e5cc26a96c3f66f37539178c3b6)。

获取通过 `NET_DEVICE_DT_DEFINE` 或 `NET_DEVICE_DT_ADD_IFACE` 创建的网络接口（Network Interface）。

<a id="r_ga48a80b52d8b5a16856c86041fc6492e6"></a>

```c
#define NET_IF_DT_INST_GET(inst, ...)
```

相关声明：[NET_IF_DT_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga48a80b52d8b5a16856c86041fc6492e6)。

获取通过 `NET_DEVICE_DT_DEFINE` 或 `NET_DEVICE_DT_ADD_IFACE` 创建的网络接口（Network Interface）。

<a id="r_ga02971562c42494e2a5f71e1f8587e709"></a>

```c
#define NET_DEVICE_INIT(dev_id, name, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu)
```

相关声明：[NET_DEVICE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga02971562c42494e2a5f71e1f8587e709)。

创建网络接口（Network Interface），并将其绑定到网络设备（Network Device）。

<a id="r_gad8e37fc7a32339312dcfa614255988e8"></a>

```c
#define NET_DEVICE_DT_ADD_IFACE(node_id, l2, l2_ctx_type, mtu, instance)
```

相关声明：[NET_DEVICE_DT_ADD_IFACE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad8e37fc7a32339312dcfa614255988e8)。

向通过 `NET_DEVICE_DT_DEFINE` 创建的网络设备（Network Device）添加第二个或更多网络接口（Network Interfaces）。

<a id="r_ga00fe86342a77e32fe440e1bd97c51d51"></a>

```c
#define NET_DEVICE_DT_INST_ADD_IFACE(inst, ...)
```

相关声明：[NET_DEVICE_DT_INST_ADD_IFACE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga00fe86342a77e32fe440e1bd97c51d51)。

类似于 `NET_DEVICE_DT_ADD_IFACE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

<a id="r_gab1f762b01ae7bc37cd4a25724c123dda"></a>

```c
#define NET_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu)
```

相关声明：[NET_DEVICE_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab1f762b01ae7bc37cd4a25724c123dda)。

类似于 `NET_DEVICE_INIT`，但从设备树节点（Devicetree Node）获取元数据（Metadata）。

<a id="r_ga7edd8bc59444d92cad0371c36f9949b7"></a>

```c
#define NET_DEVICE_DT_INST_DEFINE(inst, ...)
```

相关声明：[NET_DEVICE_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga7edd8bc59444d92cad0371c36f9949b7)。

类似于 `NET_DEVICE_DT_DEFINE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

<a id="r_gacc7edecdd9de9920cc155977d8fec2a2"></a>

```c
#define NET_DEVICE_INIT_INSTANCE(dev_id, name, instance, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu)
```

相关声明：[NET_DEVICE_INIT_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gacc7edecdd9de9920cc155977d8fec2a2)。

创建多个网络接口（Network Interfaces），并将它们绑定到网络设备（Network Device）。

<a id="r_ga50702b043a0791e59e7d5679dda1d9e8"></a>

```c
#define NET_DEVICE_DT_DEFINE_INSTANCE(node_id, instance, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu)
```

相关声明：[NET_DEVICE_DT_DEFINE_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga50702b043a0791e59e7d5679dda1d9e8)。

类似于 `NET_DEVICE_OFFLOAD_INIT`，但从设备树（Devicetree）获取元数据（Metadata）。

<a id="r_gabe4b8589996a53cbc50b76c8ea15aa0c"></a>

```c
#define NET_DEVICE_DT_INST_DEFINE_INSTANCE(inst, ...)
```

相关声明：[NET_DEVICE_DT_INST_DEFINE_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gabe4b8589996a53cbc50b76c8ea15aa0c)。

类似于 `NET_DEVICE_DT_DEFINE_INSTANCE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

<a id="r_ga255672607b7958db3f464d2a57a7e635"></a>

```c
#define NET_DEVICE_OFFLOAD_INIT(dev_id, name, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[NET_DEVICE_OFFLOAD_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga255672607b7958db3f464d2a57a7e635)。

创建卸载型网络接口（Offloaded Network Interface），并将其绑定到网络设备（Network Device）。

<a id="r_gab2b287025e194dec1fab24e44d95362f"></a>

```c
#define NET_DEVICE_DT_OFFLOAD_DEFINE(node_id, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[NET_DEVICE_DT_OFFLOAD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab2b287025e194dec1fab24e44d95362f)。

类似于 `NET_DEVICE_OFFLOAD_INIT`，但从设备树节点（Devicetree Node）获取元数据（Metadata）。

<a id="r_ga1cab6943a28e3d3754e36623834b93fd"></a>

```c
#define NET_DEVICE_DT_INST_OFFLOAD_DEFINE(inst, ...)
```

相关声明：[NET_DEVICE_DT_INST_OFFLOAD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1cab6943a28e3d3754e36623834b93fd)。

类似于 `NET_DEVICE_DT_OFFLOAD_DEFINE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

<a id="r_ga6c081875a6f5a848b3ad2fd220c63c3c"></a>

```c
#define NET_IFACE_COUNT(_dst)
```

相关声明：[NET_IFACE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6c081875a6f5a848b3ad2fd220c63c3c)。

统计网络接口（Network Interfaces）的数量。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_gaef3dfe26195514aac625e9f22e399759"></a>

```c
typedef int(* net_socket_create_t) (int, int, int)
```

相关声明：[net_socket_create_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaef3dfe26195514aac625e9f22e399759)。

用于创建卸载套接字（Offloaded Socket）的函数原型（Function Prototype）。

<a id="r_gab58d8561a4f21899e2db34043d346516"></a>

```c
typedef void(* net_if_ip_addr_cb_t) (struct net_if *iface, struct net_if_addr *addr, void *user_data)
```

相关声明：[net_if_ip_addr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab58d8561a4f21899e2db34043d346516)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)。

遍历网络接口 IP 地址（Network Interface IP Addresses）时使用的回调。

<a id="r_ga726eed76563c223de8f611e2544febe9"></a>

```c
typedef void(* net_if_ip_maddr_cb_t) (struct net_if *iface, struct net_if_mcast_addr *maddr, void *user_data)
```

相关声明：[net_if_ip_maddr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga726eed76563c223de8f611e2544febe9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

遍历网络接口多播 IP 地址（Network Interface Multicast IP Addresses）时使用的回调。

<a id="r_ga0d64291573740a67eae7ff3fcc0910c5"></a>

```c
typedef void(* net_if_mcast_callback_t) (struct net_if *iface, const struct net_addr *addr, bool is_joined)
```

相关声明：[net_if_mcast_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0d64291573740a67eae7ff3fcc0910c5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

定义回调，在加入或退出 IPv6 或 IPv4 多播地址组（Multicast Address Group）时调用。

<a id="r_ga0f87d5753fcd7cce40ecd161e6c91078"></a>

```c
typedef void(* net_if_link_callback_t) (struct net_if *iface, struct net_linkaddr *dst, int status)
```

相关声明：[net_if_link_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0f87d5753fcd7cce40ecd161e6c91078)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

定义网络数据包（Network Packet）发送之后调用的回调。

<a id="r_gac48ab8e6337e7cf387af9b293f254a80"></a>

```c
typedef void(* net_if_cb_t) (struct net_if *iface, void *user_data)
```

相关声明：[net_if_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gac48ab8e6337e7cf387af9b293f254a80)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

遍历网络接口（Network Interfaces）时使用的回调。

<a id="r_ga656c2ba47d280aa1c47bc2d062debbfa"></a>

```c
typedef void(* net_if_timestamp_callback_t) (struct net_pkt *pkt)
```

相关声明：[net_if_timestamp_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga656c2ba47d280aa1c47bc2d062debbfa)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

定义网络数据包（Network Packet）被打上时间戳（Timestamped）之后调用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.4\_枚举（Enumerations）

<a id="r_gae691e5537917ffce27ad0db82c730371"></a>

```c
enum net_if_flag { NET_IF_UP , NET_IF_POINTOPOINT , NET_IF_PROMISC , NET_IF_NO_AUTO_START , NET_IF_SUSPENDED , NET_IF_FORWARD_MULTICASTS , NET_IF_IPV4 , NET_IF_IPV6 , NET_IF_RUNNING , NET_IF_LOWER_UP , NET_IF_DORMANT , NET_IF_IPV6_NO_ND , NET_IF_IPV6_NO_MLD , NET_IF_NO_TX_LOCK }
```

相关声明：[net_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae691e5537917ffce27ad0db82c730371)、[NET_IF_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840)、[NET_IF_POINTOPOINT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009)、[NET_IF_PROMISC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141)、[NET_IF_NO_AUTO_START](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05)、[NET_IF_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0)、[NET_IF_FORWARD_MULTICASTS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac)、[NET_IF_IPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329)、[NET_IF_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6)、[NET_IF_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a)、[NET_IF_LOWER_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d)、[NET_IF_DORMANT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d)、[NET_IF_IPV6_NO_ND](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7)、[NET_IF_IPV6_NO_MLD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe)、[NET_IF_NO_TX_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9)。

网络接口标志（Network Interface Flags）。

<a id="r_gadfe9d90f24046cd9bd4bbee096e747b9"></a>

```c
enum net_if_oper_state { NET_IF_OPER_UNKNOWN , NET_IF_OPER_NOTPRESENT , NET_IF_OPER_DOWN , NET_IF_OPER_LOWERLAYERDOWN , NET_IF_OPER_TESTING , NET_IF_OPER_DORMANT , NET_IF_OPER_UP }
```

相关声明：[net_if_oper_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadfe9d90f24046cd9bd4bbee096e747b9)、[NET_IF_OPER_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58)、[NET_IF_OPER_NOTPRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32)、[NET_IF_OPER_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367)、[NET_IF_OPER_LOWERLAYERDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4)、[NET_IF_OPER_TESTING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f)、[NET_IF_OPER_DORMANT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d)、[NET_IF_OPER_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)。

网络接口运行状态（Network Interface Operational Status），参见 RFC 2863。

<a id="r_ga8db412ae79c64cafe81a66f5acb2f8e9"></a>

```c
enum net_if_checksum_type { NET_IF_CHECKSUM_IPV4_HEADER = NET_IF_CHECKSUM_IPV4_HEADER_BIT , NET_IF_CHECKSUM_IPV4_TCP , NET_IF_CHECKSUM_IPV4_UDP , NET_IF_CHECKSUM_IPV4_ICMP = NET_IF_CHECKSUM_IPV4_ICMP_BIT , NET_IF_CHECKSUM_IPV6_HEADER = NET_IF_CHECKSUM_IPV6_HEADER_BIT , NET_IF_CHECKSUM_IPV6_TCP , NET_IF_CHECKSUM_IPV6_UDP , NET_IF_CHECKSUM_IPV6_ICMP = NET_IF_CHECKSUM_IPV6_ICMP_BIT }
```

相关声明：[net_if_checksum_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8db412ae79c64cafe81a66f5acb2f8e9)、[NET_IF_CHECKSUM_IPV4_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30)、[NET_IF_CHECKSUM_IPV4_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad)、[NET_IF_CHECKSUM_IPV4_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3)、[NET_IF_CHECKSUM_IPV4_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1)、[NET_IF_CHECKSUM_IPV6_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b)、[NET_IF_CHECKSUM_IPV6_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13)、[NET_IF_CHECKSUM_IPV6_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660)、[NET_IF_CHECKSUM_IPV6_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3)。

要查询接口支持情况的校验和类型（Checksum Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.5\_函数（Functions）

<a id="r_ga52f9fca13e9f836799e0e40f581744d2"></a>

```c
static void net_if_flag_set (struct net_if *iface, enum net_if_flag value)
```

相关声明：[net_if_flag_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga52f9fca13e9f836799e0e40f581744d2)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae691e5537917ffce27ad0db82c730371)。

设置网络接口标志（Network Interface Flags）中的一个值。

<a id="r_ga42e7482191a92007960601f8bb621dca"></a>

```c
static bool net_if_flag_test_and_set (struct net_if *iface, enum net_if_flag value)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_flag_test_and_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga42e7482191a92007960601f8bb621dca)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae691e5537917ffce27ad0db82c730371)。

测试并设置网络接口标志（Network Interface Flags）中的一个值。

<a id="r_gaff751b6a92b0c608ecfc50e8c0587fd3"></a>

```c
static void net_if_flag_clear (struct net_if *iface, enum net_if_flag value)
```

相关声明：[net_if_flag_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaff751b6a92b0c608ecfc50e8c0587fd3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae691e5537917ffce27ad0db82c730371)。

清除网络接口标志（Network Interface Flags）中的一个值。

<a id="r_gab8f371c7f8890cf4728177f6595141d7"></a>

```c
static bool net_if_flag_test_and_clear (struct net_if *iface, enum net_if_flag value)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_flag_test_and_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab8f371c7f8890cf4728177f6595141d7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae691e5537917ffce27ad0db82c730371)。

测试并清除网络接口标志（Network Interface Flags）中的一个值。

<a id="r_gae1f373ddd61c18a81481d8ddcfb12543"></a>

```c
static bool net_if_flag_is_set (struct net_if *iface, enum net_if_flag value)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_flag_is_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae1f373ddd61c18a81481d8ddcfb12543)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae691e5537917ffce27ad0db82c730371)。

检查网络接口标志（Network Interface Flags）中的一个值是否已设置。

<a id="r_ga1f1bf845e63cce02e2183889cc85d57e"></a>

```c
static enum net_if_oper_state net_if_oper_state_set (struct net_if *iface, enum net_if_oper_state oper_state)
```

相关声明：[net_if_oper_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadfe9d90f24046cd9bd4bbee096e747b9)、[net_if_oper_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1f1bf845e63cce02e2183889cc85d57e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_oper_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadfe9d90f24046cd9bd4bbee096e747b9)。

设置接口的运行状态（Operational State）。

<a id="r_gad9e957a4866b4566296ee39392fde0e4"></a>

```c
static enum net_if_oper_state net_if_oper_state (struct net_if *iface)
```

相关声明：[net_if_oper_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadfe9d90f24046cd9bd4bbee096e747b9)、[net_if_oper_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad9e957a4866b4566296ee39392fde0e4)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取接口的运行状态（Operational State）。

<a id="r_gabae216ba527bdfcd945ef19fb48e56be"></a>

```c
static int net_if_oper_state_change_time (struct net_if *iface, int64_t *change_time)
```

相关声明：[net_if_oper_state_change_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gabae216ba527bdfcd945ef19fb48e56be)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

获取接口运行状态的变化时间（Operational State Change Time）。

<a id="r_ga5d01d7fa6c7511d68933ad4cec032d8a"></a>

```c
enum net_verdict net_if_try_send_data (struct net_if *iface, struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_if_try_send_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5d01d7fa6c7511d68933ad4cec032d8a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

尝试通过网络接口（Net Interface）发送数据包（Packet）。

<a id="r_ga84a58403183b88c64fda59d5d2d903fc"></a>

```c
static enum net_verdict net_if_send_data (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_if_send_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga84a58403183b88c64fda59d5d2d903fc)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

通过网络接口（Net Interface）发送数据包（Packet）。

<a id="r_gafa451f6118529d1d084704d00b2aae20"></a>

```c
static const struct net_l2 * net_if_l2 (struct net_if *iface)
```

相关声明：[net_l2](../network_core_model_reference/P103_net_l2_结构体.md)、[net_if_l2](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gafa451f6118529d1d084704d00b2aae20)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取指向接口链路层（Interface L2）的指针。

<a id="r_ga72ed21ca0cb220199f5a2070137c7fef"></a>

```c
enum net_verdict net_if_recv_data (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_if_recv_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga72ed21ca0cb220199f5a2070137c7fef)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

通过网络接口（Net Interface）输入数据包（Packet）。

<a id="r_ga3cad2d51fc9cc225619585e06e252db0"></a>

```c
static void * net_if_l2_data (struct net_if *iface)
```

相关声明：[net_if_l2_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3cad2d51fc9cc225619585e06e252db0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取指向接口链路层私有数据（Interface L2 Private Data）的指针。

<a id="r_gaeb8c703f273bc07ae9bb7a0d8bfe6f3d"></a>

```c
static const struct device * net_if_get_device (struct net_if *iface)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[net_if_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取网络接口（Network Interface）对应的设备（Device）。

<a id="r_ga3617cd1f712b8a85fdd7f1425254ae5d"></a>

```c
void net_if_try_queue_tx (struct net_if *iface, struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_if_try_queue_tx](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3617cd1f712b8a85fdd7f1425254ae5d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

尝试将数据包（Packet）加入网络接口发送队列（TX Queue）。

<a id="r_ga2ac749d465ef7f0f64f294a30310457e"></a>

```c
static void net_if_queue_tx (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_if_queue_tx](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2ac749d465ef7f0f64f294a30310457e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

将数据包（Packet）加入网络接口发送队列（TX Queue）。

<a id="r_ga6bfa5f84a2127bbad27a0a3b319526a1"></a>

```c
static bool net_if_is_ip_offloaded (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_ip_offloaded](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6bfa5f84a2127bbad27a0a3b319526a1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回 IP 卸载状态（IP Offload Status）。

<a id="r_gaecedc93a6dab2c57fe686718ea4d78af"></a>

```c
bool net_if_is_offloaded (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_offloaded](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaecedc93a6dab2c57fe686718ea4d78af)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回给定网络接口（Network Interface）的卸载状态（Offload Status）。

<a id="r_ga520939e94620ca75475a71f153df6d4a"></a>

```c
static struct net_offload * net_if_offload (struct net_if *iface)
```

相关声明：[net_if_offload](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga520939e94620ca75475a71f153df6d4a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回 IP 卸载插件（IP Offload Plugin）。

<a id="r_gaf2d323c1504125fbfde5da9ada8c5657"></a>

```c
static void net_if_offload_set (struct net_if *iface, struct net_offload *offload)
```

相关声明：[net_if_offload_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf2d323c1504125fbfde5da9ada8c5657)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置 IP 卸载插件（IP Offload Plugin）。

<a id="r_gaf308baf2241fa455b50b439b7fab3f1e"></a>

```c
static bool net_if_is_socket_offloaded (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_socket_offloaded](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf308baf2241fa455b50b439b7fab3f1e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回套接字卸载状态（Socket Offload Status）。

<a id="r_ga9db52875580115c743b1f35cd6c46796"></a>

```c
static void net_if_socket_offload_set (struct net_if *iface, net_socket_create_t socket_offload)
```

相关声明：[net_if_socket_offload_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9db52875580115c743b1f35cd6c46796)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_socket_create_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaef3dfe26195514aac625e9f22e399759)。

设置创建卸载套接字（Offloaded Socket）的函数。

<a id="r_gafb2bbaec96c4759d920b2866c0b3ef3a"></a>

```c
static net_socket_create_t net_if_socket_offload (struct net_if *iface)
```

相关声明：[net_socket_create_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaef3dfe26195514aac625e9f22e399759)、[net_if_socket_offload](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gafb2bbaec96c4759d920b2866c0b3ef3a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回创建卸载套接字（Offloaded Socket）的函数。

<a id="r_ga467186e964bf721e14fed38392f21872"></a>

```c
static struct net_linkaddr * net_if_get_link_addr (struct net_if *iface)
```

相关声明：[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)、[net_if_get_link_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga467186e964bf721e14fed38392f21872)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取网络接口的链路地址（Link Address）。

<a id="r_gae271e0e4dcb031a83d9908e597a45048"></a>

```c
static struct net_if_config * net_if_get_config (struct net_if *iface)
```

相关声明：[net_if_config](../network_core_model_reference/P082_net_if_config_结构体.md)、[net_if_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae271e0e4dcb031a83d9908e597a45048)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回此网络接口（Network Interface）的网络配置（Network Configuration）。

<a id="r_ga9655c010ccbf989e9328271f5dbcc685"></a>

```c
static void net_if_start_dad (struct net_if *iface)
```

相关声明：[net_if_start_dad](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9655c010ccbf989e9328271f5dbcc685)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启动重复地址检测过程（Duplicate Address Detection Procedure）。

<a id="r_gab9bdb7f8a9eeed4d9b70965b8af82cb7"></a>

```c
void net_if_start_rs (struct net_if *iface)
```

相关声明：[net_if_start_rs](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab9bdb7f8a9eeed4d9b70965b8af82cb7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启动邻居发现（Neighbor Discovery），并发送路由器请求消息（Router Solicitation Message）。

<a id="r_gab0195bb2151a1ba722a0b11d81066988"></a>

```c
static void net_if_stop_rs (struct net_if *iface)
```

相关声明：[net_if_stop_rs](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab0195bb2151a1ba722a0b11d81066988)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

停止邻居发现（Neighbor Discovery）。

<a id="r_ga655599b1432463455610cff768997e2b"></a>

```c
static void net_if_nbr_reachability_hint (struct net_if *iface, const struct net_in6_addr *ipv6_addr)
```

相关声明：[net_if_nbr_reachability_hint](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga655599b1432463455610cff768997e2b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

为 IPv6 邻居发现（Neighbor Discovery）提供可达性提示（Reachability Hint）。

<a id="r_gaaa6c3d31d3a40cab6cf9e4f4af959b89"></a>

```c
static void net_if_ipv6_nbr_flush (struct net_if *iface)
```

相关声明：[net_if_ipv6_nbr_flush](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaaa6c3d31d3a40cab6cf9e4f4af959b89)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

清空网络接口的 IPv6 邻居缓存（Neighbor Cache）。

<a id="r_gac6bc061b5b0facc5023da2a835fb9bb3"></a>

```c
static bool net_if_ipv6_nbr_rm (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_nbr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gac6bc061b5b0facc5023da2a835fb9bb3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

从 IPv6 邻居缓存（Neighbor Cache）中移除一个邻居（Neighbor）。

<a id="r_ga3863e011f89dff02c3df3ca4a88680e9"></a>

```c
static int net_if_set_link_addr (struct net_if *iface, const uint8_t *addr, uint8_t len, enum net_link_type type)
```

相关声明：[net_if_set_link_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3863e011f89dff02c3df3ca4a88680e9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_link_type](../api_input_runtime_topic_reference/P015_网络链路地址库（Network Link Address Library）.md#ga1312c2322bc4a4f1c3b76d6466806b24)。

设置网络接口的链路地址（Link Address）。

<a id="r_gacddc98531c5748db5a34f5c3a3e96e86"></a>

```c
static uint16_t net_if_get_mtu (struct net_if *iface)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_if_get_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gacddc98531c5748db5a34f5c3a3e96e86)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取网络接口的最大传输单元（MTU）。

<a id="r_ga76b140c6fc39b94ff4102e08e3a58e81"></a>

```c
static void net_if_set_mtu (struct net_if *iface, uint16_t mtu)
```

相关声明：[net_if_set_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga76b140c6fc39b94ff4102e08e3a58e81)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置网络接口的最大传输单元（MTU）。

<a id="r_gae66f6e7bd31545e6161fcd4600fe5842"></a>

```c
static void net_if_addr_set_lf (struct net_if_addr *ifaddr, bool is_infinite)
```

相关声明：[net_if_addr_set_lf](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae66f6e7bd31545e6161fcd4600fe5842)、[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置网络接口地址的无限有效状态（Infinite Status）。

<a id="r_ga1b058361dc9bcac7d842bb49846a0c79"></a>

```c
struct net_if * net_if_get_by_link_addr (struct net_linkaddr *ll_addr)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_by_link_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1b058361dc9bcac7d842bb49846a0c79)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

根据链路层地址（Link Layer Address）获取接口（Interface）。

<a id="r_gadbb8be32caa896bdcdeee19425134827"></a>

```c
struct net_if * net_if_lookup_by_dev (const struct device *dev)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_lookup_by_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadbb8be32caa896bdcdeee19425134827)、[device](../device_reference/P002_设备对象结构.md)。

根据关联的设备（Device）查找接口（Interface）。

<a id="r_gadc87242eb7205362a308b3c4437bf76d"></a>

```c
void net_if_router_rm (struct net_if_router *router)
```

相关声明：[net_if_router_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadc87242eb7205362a308b3c4437bf76d)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)。

从系统中移除路由器（Router）。

<a id="r_ga0a1f27ec893e1af3c97f130be4616589"></a>

```c
void net_if_set_default (struct net_if *iface)
```

相关声明：[net_if_set_default](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0a1f27ec893e1af3c97f130be4616589)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置默认网络接口（Default Network Interface）。

<a id="r_ga55214771e462cbd4930ffa738813cb87"></a>

```c
struct net_if * net_if_get_default (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_default](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga55214771e462cbd4930ffa738813cb87)。

获取默认网络接口（Default Network Interface）。

<a id="r_ga762337e8b66874a0fbf59bdbeba173f5"></a>

```c
struct net_if * net_if_get_first_by_type (const struct net_l2 *l2)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_first_by_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga762337e8b66874a0fbf59bdbeba173f5)、[net_l2](../network_core_model_reference/P103_net_l2_结构体.md)。

根据类型（Type）获取第一个网络接口（Network Interface）。

<a id="r_ga03d8c6aebb1412382a9eec636c227238"></a>

```c
struct net_if * net_if_get_first_up (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_first_up](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga03d8c6aebb1412382a9eec636c227238)。

获取第一个处于启用状态（Up）的网络接口（Network Interface）。

<a id="r_ga56c9aef19bc9827d9ec96c00e10840fa"></a>

```c
int net_if_config_ipv6_get (struct net_if *iface, struct net_if_ipv6 **ipv6)
```

相关声明：[net_if_config_ipv6_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga56c9aef19bc9827d9ec96c00e10840fa)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv6](../network_core_model_reference/P086_net_if_ipv6_结构体.md)。

分配网络接口的 IPv6 配置（IPv6 Configuration）。

<a id="r_ga8af1400b354c42a64795cdb1a600ddd6"></a>

```c
int net_if_config_ipv6_put (struct net_if *iface)
```

相关声明：[net_if_config_ipv6_put](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8af1400b354c42a64795cdb1a600ddd6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

释放网络接口的 IPv6 配置（IPv6 Configuration）。

<a id="r_ga4314c59af790e537e384e969c58fab9d"></a>

```c
struct net_if_addr * net_if_ipv6_addr_lookup (const struct net_in6_addr *addr, struct net_if **iface)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv6_addr_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga4314c59af790e537e384e969c58fab9d)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查此 IPv6 地址是否属于某个接口（Interface）。

<a id="r_gae2935f8b0ad41879b12a491bc260b236"></a>

```c
struct net_if_addr * net_if_ipv6_addr_lookup_by_iface (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv6_addr_lookup_by_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae2935f8b0ad41879b12a491bc260b236)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查此 IPv6 地址是否属于这个特定接口（Specific Interface）。

<a id="r_gaaba6b0ba57a19c3d24628e8498ef421d"></a>

```c
int net_if_ipv6_addr_lookup_by_index (const struct net_in6_addr *addr)
```

相关声明：[net_if_ipv6_addr_lookup_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaaba6b0ba57a19c3d24628e8498ef421d)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查此 IPv6 地址是否属于某个接口索引（Interface Index）对应的接口。

<a id="r_ga3b651babfb5d1dd9f8d266d2aa1cf1b8"></a>

```c
struct net_if_addr * net_if_ipv6_addr_add (struct net_if *iface, const struct net_in6_addr *addr, enum net_addr_type addr_type, uint32_t vlifetime)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv6_addr_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3b651babfb5d1dd9f8d266d2aa1cf1b8)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_addr_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gafecee2d4a331dc85ad962b81a6303e41)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向接口（Interface）添加 IPv6 地址。

<a id="r_gad68f25bd25b198bc4280d334f71495d3"></a>

```c
bool net_if_ipv6_addr_add_by_index (int index, const struct net_in6_addr *addr, enum net_addr_type addr_type, uint32_t vlifetime)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_addr_add_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad68f25bd25b198bc4280d334f71495d3)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_addr_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gafecee2d4a331dc85ad962b81a6303e41)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过索引（Index）向接口添加 IPv6 地址。

<a id="r_gaef8a6752a201f81636c4ffc1ebba4a25"></a>

```c
void net_if_ipv6_addr_update_lifetime (struct net_if_addr *ifaddr, uint32_t vlifetime)
```

相关声明：[net_if_ipv6_addr_update_lifetime](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaef8a6752a201f81636c4ffc1ebba4a25)、[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更新 IPv6 地址的有效生命周期（Valid Lifetime）。

<a id="r_gad0e9473f494d154c4cd89e3e67a13232"></a>

```c
bool net_if_ipv6_addr_rm (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_addr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad0e9473f494d154c4cd89e3e67a13232)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

从接口（Interface）移除 IPv6 地址。

<a id="r_gadc08ec8c23d2ee138eb3a05cdfe00701"></a>

```c
bool net_if_ipv6_addr_rm_by_index (int index, const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_addr_rm_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadc08ec8c23d2ee138eb3a05cdfe00701)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

通过索引（Index）从接口移除 IPv6 地址。

<a id="r_ga5ac646ad7fda0fa48e78c15b4ca52d50"></a>

```c
void net_if_ipv6_addr_foreach (struct net_if *iface, net_if_ip_addr_cb_t cb, void *user_data)
```

相关声明：[net_if_ipv6_addr_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5ac646ad7fda0fa48e78c15b4ca52d50)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ip_addr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab58d8561a4f21899e2db34043d346516)。

遍历网络接口的全部 IPv6 地址，并对每个正在使用的地址调用回调（Callback）。

<a id="r_ga1608a77ffca421769bae381a12e179ce"></a>

```c
struct net_if_mcast_addr * net_if_ipv6_maddr_add (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)、[net_if_ipv6_maddr_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1608a77ffca421769bae381a12e179ce)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

向接口（Interface）添加 IPv6 多播地址（Multicast Address）。

<a id="r_ga6c80fd9c864cb54902d52adcb5d8d639"></a>

```c
bool net_if_ipv6_maddr_rm (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_maddr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6c80fd9c864cb54902d52adcb5d8d639)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

从接口（Interface）移除 IPv6 多播地址（Multicast Address）。

<a id="r_gab677496fb2e27be2df299a346e9c7132"></a>

```c
void net_if_ipv6_maddr_foreach (struct net_if *iface, net_if_ip_maddr_cb_t cb, void *user_data)
```

相关声明：[net_if_ipv6_maddr_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab677496fb2e27be2df299a346e9c7132)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ip_maddr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga726eed76563c223de8f611e2544febe9)。

遍历网络接口的全部 IPv6 多播地址（Multicast Addresses），并对每个正在使用的地址调用回调。

<a id="r_gad520342d393f523c56a98fa618876b54"></a>

```c
struct net_if_mcast_addr * net_if_ipv6_maddr_lookup (const struct net_in6_addr *addr, struct net_if **iface)
```

相关声明：[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)、[net_if_ipv6_maddr_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad520342d393f523c56a98fa618876b54)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查此 IPv6 多播地址（Multicast Address）是否属于指定接口或某个接口（Interface）。

<a id="r_ga8fdd0665ed76db6055777e395ca60255"></a>

```c
void net_if_mcast_mon_register (struct net_if_mcast_monitor *mon, struct net_if *iface, net_if_mcast_callback_t cb)
```

相关声明：[net_if_mcast_mon_register](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8fdd0665ed76db6055777e395ca60255)、[net_if_mcast_monitor](../network_core_model_reference/P090_net_if_mcast_monitor_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0d64291573740a67eae7ff3fcc0910c5)。

注册多播监视器（Multicast Monitor）。

<a id="r_gad323732fe3d178a5dfdf0900e5cb5683"></a>

```c
void net_if_mcast_mon_unregister (struct net_if_mcast_monitor *mon)
```

相关声明：[net_if_mcast_mon_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad323732fe3d178a5dfdf0900e5cb5683)、[net_if_mcast_monitor](../network_core_model_reference/P090_net_if_mcast_monitor_结构体.md)。

注销多播监视器（Multicast Monitor）。

<a id="r_ga372ef131263269cd65586d87997df745"></a>

```c
void net_if_mcast_monitor (struct net_if *iface, const struct net_addr *addr, bool is_joined)
```

相关声明：[net_if_mcast_monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga372ef131263269cd65586d87997df745)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

调用已注册的多播监视器（Multicast Monitors）。

<a id="r_ga49dbc954015307222f176f4149829b76"></a>

```c
void net_if_ipv6_maddr_join (struct net_if *iface, struct net_if_mcast_addr *addr)
```

相关声明：[net_if_ipv6_maddr_join](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga49dbc954015307222f176f4149829b76)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

将给定多播地址（Multicast Address）标记为已加入（Joined）。

<a id="r_gabe2c16a378a35a22d008bff9142e5449"></a>

```c
static bool net_if_ipv6_maddr_is_joined (struct net_if_mcast_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_maddr_is_joined](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gabe2c16a378a35a22d008bff9142e5449)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

检查是否已加入（Joined）给定多播地址（Multicast Address）。

<a id="r_gad24d5537d52de9781a7a6a55ceedd92b"></a>

```c
void net_if_ipv6_maddr_leave (struct net_if *iface, struct net_if_mcast_addr *addr)
```

相关声明：[net_if_ipv6_maddr_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad24d5537d52de9781a7a6a55ceedd92b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

将给定多播地址（Multicast Address）标记为已退出（Left）。

<a id="r_ga9c10341ab913f0b609c2724354ec587a"></a>

```c
struct net_if_ipv6_prefix * net_if_ipv6_prefix_get (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)、[net_if_ipv6_prefix_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9c10341ab913f0b609c2724354ec587a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

返回与此 IPv6 地址对应的前缀（Prefix）。

<a id="r_ga99b22d24fef63bd1681396410b930008"></a>

```c
struct net_if_ipv6_prefix * net_if_ipv6_prefix_lookup (struct net_if *iface, const struct net_in6_addr *addr, uint8_t len)
```

相关声明：[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)、[net_if_ipv6_prefix_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga99b22d24fef63bd1681396410b930008)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查此 IPv6 前缀（Prefix）是否属于该接口。

<a id="r_ga2616868a6d51cbf1d35c6920e258d412"></a>

```c
struct net_if_ipv6_prefix * net_if_ipv6_prefix_add (struct net_if *iface, const struct net_in6_addr *prefix, uint8_t len, uint32_t lifetime)
```

相关声明：[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)、[net_if_ipv6_prefix_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2616868a6d51cbf1d35c6920e258d412)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向网络接口（Network Interface）添加 IPv6 前缀（Prefix）。

<a id="r_ga4b8668b32a14996c68d10ec989c1abb3"></a>

```c
bool net_if_ipv6_prefix_rm (struct net_if *iface, const struct net_in6_addr *addr, uint8_t len)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_prefix_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga4b8668b32a14996c68d10ec989c1abb3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从接口（Interface）移除 IPv6 前缀（Prefix）。

<a id="r_gaa3c711e814fb6a4e552b4ef723d0baa0"></a>

```c
static void net_if_ipv6_prefix_set_lf (struct net_if_ipv6_prefix *prefix, bool is_infinite)
```

相关声明：[net_if_ipv6_prefix_set_lf](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa3c711e814fb6a4e552b4ef723d0baa0)、[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置前缀（Prefix）的无限有效状态（Infinite Status）。

<a id="r_ga68cffe343c518bad7f7f152e30f7f9ee"></a>

```c
void net_if_ipv6_prefix_set_timer (struct net_if_ipv6_prefix *prefix, uint32_t lifetime)
```

相关声明：[net_if_ipv6_prefix_set_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga68cffe343c518bad7f7f152e30f7f9ee)、[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置前缀生命周期定时器（Prefix Lifetime Timer）。

<a id="r_ga2d68cb6dcfcffd3f87bbfb3dfce791ff"></a>

```c
void net_if_ipv6_prefix_unset_timer (struct net_if_ipv6_prefix *prefix)
```

相关声明：[net_if_ipv6_prefix_unset_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)、[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)。

取消前缀生命周期定时器（Prefix Lifetime Timer）。

<a id="r_ga9ff61003d36ee19af27a9b1b24b22170"></a>

```c
int net_if_ipv6_prefix_set_advertise (struct net_if *iface, const struct net_in6_addr *prefix, uint8_t len, bool advertise)
```

相关声明：[net_if_ipv6_prefix_set_advertise](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9ff61003d36ee19af27a9b1b24b22170)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

标记或取消标记一个 IPv6 前缀（Prefix），决定是否在该接口发送的路由器通告（Router Advertisements）中通告此前缀。

<a id="r_ga1c062890f66b97dbb723339fede121ff"></a>

```c
int net_if_ipv6_router_start (struct net_if *iface)
```

相关声明：[net_if_ipv6_router_start](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1c062890f66b97dbb723339fede121ff)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启用接口的 IPv6 路由器角色（Router Role）。

<a id="r_gaa56d3dbc96301e6fa70ee61b08c29841"></a>

```c
int net_if_ipv6_router_stop (struct net_if *iface)
```

相关声明：[net_if_ipv6_router_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa56d3dbc96301e6fa70ee61b08c29841)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

禁用接口的 IPv6 路由器角色（Router Role）。

<a id="r_ga53cc6d8d43f3b3ef7c275dff69b4de8d"></a>

```c
bool net_if_ipv6_addr_onlink (struct net_if **iface, const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_addr_onlink](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga53cc6d8d43f3b3ef7c275dff69b4de8d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查此 IPv6 地址是否属于本网络接口的子网（Subnet）。

<a id="r_ga17d846ec0cbc1e67fd4a2bc1179b7c45"></a>

```c
static struct net_in6_addr * net_if_router_ipv6 (struct net_if_router *router)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_router_ipv6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga17d846ec0cbc1e67fd4a2bc1179b7c45)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)。

获取给定路由器（Router）的 IPv6 地址。

<a id="r_gac68a72e70b5335773964dbfc0319eee5"></a>

```c
struct net_if_router * net_if_ipv6_router_lookup (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv6_router_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gac68a72e70b5335773964dbfc0319eee5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查该 IPv6 地址是否为系统中已配置路由器（Router）的地址之一。

<a id="r_gabfabdb7afa073b54f67d67320da3983c"></a>

```c
struct net_if_router * net_if_ipv6_router_find_default (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv6_router_find_default](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gabfabdb7afa073b54f67d67320da3983c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

查找用于此 IPv6 地址的默认路由器（Default Router）。

<a id="r_gaadba4957802dc376ef011590c91c6af6"></a>

```c
void net_if_ipv6_router_update_lifetime (struct net_if_router *router, uint16_t lifetime)
```

相关声明：[net_if_ipv6_router_update_lifetime](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaadba4957802dc376ef011590c91c6af6)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

更新路由器（Router）的有效生命周期（Valid Lifetime）。

<a id="r_ga8d80080463bcb9035e06e0ac35090780"></a>

```c
struct net_if_router * net_if_ipv6_router_add (struct net_if *iface, const struct net_in6_addr *addr, bool is_default, uint16_t router_lifetime)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv6_router_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8d80080463bcb9035e06e0ac35090780)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向系统添加 IPv6 路由器（Router）。

<a id="r_ga1d108aa0b54c072e0aa9d0c049f02807"></a>

```c
bool net_if_ipv6_router_rm (struct net_if_router *router)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_router_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1d108aa0b54c072e0aa9d0c049f02807)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)。

从系统移除 IPv6 路由器（Router）。

<a id="r_ga66d0a9a8eef095f6d4d44f35dd67f2b6"></a>

```c
static uint8_t net_if_ipv6_get_hop_limit (struct net_if *iface)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_if_ipv6_get_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga66d0a9a8eef095f6d4d44f35dd67f2b6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv6 跳数限制（Hop Limit）。

<a id="r_ga5bf726bb5c1d232103ec6841e7d0cd8c"></a>

```c
static void net_if_ipv6_set_hop_limit (struct net_if *iface, uint8_t hop_limit)
```

相关声明：[net_if_ipv6_set_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5bf726bb5c1d232103ec6841e7d0cd8c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置给定接口的默认 IPv6 跳数限制（Hop Limit）。

<a id="r_ga56e7086633bcf4537f54c7ca70e6c900"></a>

```c
static uint8_t net_if_ipv6_get_mcast_hop_limit (struct net_if *iface)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_if_ipv6_get_mcast_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga56e7086633bcf4537f54c7ca70e6c900)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv6 多播跳数限制（Multicast Hop Limit）。

<a id="r_gaf56a433679ea9701cf8baa3208f8ccc3"></a>

```c
static void net_if_ipv6_set_mcast_hop_limit (struct net_if *iface, uint8_t hop_limit)
```

相关声明：[net_if_ipv6_set_mcast_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf56a433679ea9701cf8baa3208f8ccc3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置给定接口的默认 IPv6 多播跳数限制（Multicast Hop Limit）。

<a id="r_gab3939d735b660f8f02124df656ceba2c"></a>

```c
static void net_if_ipv6_set_base_reachable_time (struct net_if *iface, uint32_t reachable_time)
```

相关声明：[net_if_ipv6_set_base_reachable_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab3939d735b660f8f02124df656ceba2c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置给定接口的 IPv6 可达时间（Reachable Time）。

<a id="r_ga71eb0b9842db6db6930c3567e94d4bd6"></a>

```c
static uint32_t net_if_ipv6_get_base_reachable_time (struct net_if *iface)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_if_ipv6_get_base_reachable_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga71eb0b9842db6db6930c3567e94d4bd6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取给定接口的 IPv6 基础可达时间（Base Reachable Time）。

<a id="r_ga9dd1f91edbb519a6a079f363c33efacf"></a>

```c
static uint32_t net_if_ipv6_get_reachable_time (struct net_if *iface)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_if_ipv6_get_reachable_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9dd1f91edbb519a6a079f363c33efacf)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv6 可达超时（Reachable Timeout）。

<a id="r_gab1861b5cefa73b4eefbb447cb1438cdc"></a>

```c
uint32_t net_if_ipv6_calc_reachable_time (struct net_if_ipv6 *ipv6)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_if_ipv6_calc_reachable_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab1861b5cefa73b4eefbb447cb1438cdc)、[net_if_ipv6](../network_core_model_reference/P086_net_if_ipv6_结构体.md)。

为 IPv6 可达时间（Reachable Time）计算下一个可达时间值。

<a id="r_ga8328266b870fd200660cb2becaab3de4"></a>

```c
static void net_if_ipv6_set_reachable_time (struct net_if_ipv6 *ipv6)
```

相关声明：[net_if_ipv6_set_reachable_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8328266b870fd200660cb2becaab3de4)、[net_if_ipv6](../network_core_model_reference/P086_net_if_ipv6_结构体.md)。

设置给定接口的 IPv6 可达时间（Reachable Time）。

<a id="r_gad74566e5a34f447d2ac63d2c0e82eeff"></a>

```c
static void net_if_ipv6_set_retrans_timer (struct net_if *iface, uint32_t retrans_timer)
```

相关声明：[net_if_ipv6_set_retrans_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad74566e5a34f447d2ac63d2c0e82eeff)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置给定接口的 IPv6 重传定时器（Retransmit Timer）。

<a id="r_gaddbf5a6ba412e6bdb7e31568fe827bd0"></a>

```c
static uint32_t net_if_ipv6_get_retrans_timer (struct net_if *iface)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_if_ipv6_get_retrans_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaddbf5a6ba412e6bdb7e31568fe827bd0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv6 重传定时器（Retransmit Timer）。

<a id="r_ga5f8fc8725d3050a0e8fb0c3c75791c7c"></a>

```c
static const struct net_in6_addr * net_if_ipv6_select_src_addr (struct net_if *iface, const struct net_in6_addr *dst)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_ipv6_select_src_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5f8fc8725d3050a0e8fb0c3c75791c7c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

获取向目的地发送网络数据时应使用的 IPv6 源地址（Source Address）。

<a id="r_ga55df4f4967efb4840dbee7a4078a237b"></a>

```c
static const struct net_in6_addr * net_if_ipv6_select_src_addr_hint (struct net_if *iface, const struct net_in6_addr *dst, int flags)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_ipv6_select_src_addr_hint](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga55df4f4967efb4840dbee7a4078a237b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

获取向目的地发送网络数据时应使用的 IPv6 源地址（Source Address）。

<a id="r_ga367c74aad10b58074e5e1e517d6be379"></a>

```c
static struct net_if * net_if_ipv6_select_src_iface (const struct net_in6_addr *dst)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv6_select_src_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga367c74aad10b58074e5e1e517d6be379)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

获取向目的地发送 IPv6 网络数据时应使用的网络接口（Network Interface）。

<a id="r_ga8c3fe8f29294c8bb9561d22625cf726c"></a>

```c
static struct net_if * net_if_ipv6_select_src_iface_addr (const struct net_in6_addr *dst, const struct net_in6_addr **src_addr)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv6_select_src_iface_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8c3fe8f29294c8bb9561d22625cf726c)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

获取向目的地发送 IPv6 网络数据时应使用的网络接口（Network Interface）。

<a id="r_ga76ebc895fb5959f7f4a2884024bb4963"></a>

```c
struct net_in6_addr * net_if_ipv6_get_ll (struct net_if *iface, enum net_addr_state addr_state)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_ipv6_get_ll](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga76ebc895fb5959f7f4a2884024bb4963)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_addr_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga32e58fc83532ef57eeb6ff952f17288d)。

获取处于给定状态的 IPv6 链路本地地址（Link Local Address）。

<a id="r_ga89ea06beb89db41d064b23186c92a567"></a>

```c
struct net_in6_addr * net_if_ipv6_get_ll_addr (enum net_addr_state state, struct net_if **iface)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_ipv6_get_ll_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga89ea06beb89db41d064b23186c92a567)、[net_addr_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga32e58fc83532ef57eeb6ff952f17288d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

从第一个具有匹配给定状态的链路本地地址（Link Local Address）的接口中，返回该链路本地 IPv6 地址。

<a id="r_ga8f37df9b421963d33a0838fe1fedde2a"></a>

```c
void net_if_ipv6_dad_failed (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_ipv6_dad_failed](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8f37df9b421963d33a0838fe1fedde2a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

如果发现本机 IPv6 地址已被使用，则停止 IPv6 重复地址检测（Duplicate Address Detection，DAD）过程。

<a id="r_gaf466f15f578d0ab287d8d3a258a64bb3"></a>

```c
struct net_in6_addr * net_if_ipv6_get_global_addr (enum net_addr_state state, struct net_if **iface)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_ipv6_get_global_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf466f15f578d0ab287d8d3a258a64bb3)、[net_addr_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga32e58fc83532ef57eeb6ff952f17288d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

从第一个具有匹配给定状态的全局 IPv6 地址（Global IPv6 Address）的接口中，返回该全局地址。

<a id="r_ga3390e248249b28f2c80e2ca0bc79d236"></a>

```c
int net_if_config_ipv4_get (struct net_if *iface, struct net_if_ipv4 **ipv4)
```

相关声明：[net_if_config_ipv4_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3390e248249b28f2c80e2ca0bc79d236)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv4](../network_core_model_reference/P085_net_if_ipv4_结构体.md)。

分配网络接口的 IPv4 配置（IPv4 Configuration）。

<a id="r_ga88c13a45617480a665c7f9f589ec8e10"></a>

```c
int net_if_config_ipv4_put (struct net_if *iface)
```

相关声明：[net_if_config_ipv4_put](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga88c13a45617480a665c7f9f589ec8e10)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

释放网络接口的 IPv4 配置（IPv4 Configuration）。

<a id="r_ga7e1fd28dbcf1164d056296b4df782e64"></a>

```c
uint8_t net_if_ipv4_get_ttl (struct net_if *iface)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_if_ipv4_get_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga7e1fd28dbcf1164d056296b4df782e64)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv4 生存时间（Time-to-live）值。

<a id="r_ga5544374d7ebea26a239d561083f0203d"></a>

```c
void net_if_ipv4_set_ttl (struct net_if *iface, uint8_t ttl)
```

相关声明：[net_if_ipv4_set_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5544374d7ebea26a239d561083f0203d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置给定接口的 IPv4 生存时间（Time-to-live）值。

<a id="r_ga71acb65b1988aab8cca9c9604c86231e"></a>

```c
uint8_t net_if_ipv4_get_mcast_ttl (struct net_if *iface)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_if_ipv4_get_mcast_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga71acb65b1988aab8cca9c9604c86231e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv4 多播生存时间（Multicast Time-to-live）值。

<a id="r_ga9452fef4f1309fb1a53a6a8b4f222377"></a>

```c
void net_if_ipv4_set_mcast_ttl (struct net_if *iface, uint8_t ttl)
```

相关声明：[net_if_ipv4_set_mcast_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9452fef4f1309fb1a53a6a8b4f222377)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置给定接口的 IPv4 多播生存时间（Multicast Time-to-live）值。

<a id="r_ga0f324d39cf60e7babb5a1c4a364a8e86"></a>

```c
bool net_if_ipv4_addr_onlink (struct net_if **iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_addr_onlink](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0f324d39cf60e7babb5a1c4a364a8e86)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查此 IPv4 地址是否属于本网络接口的子网（Subnet）。

<a id="r_ga53fb4ce0130fc8d665ddfd466d2a5eb8"></a>

```c
struct net_if_addr * net_if_ipv4_addr_lookup (const struct net_in_addr *addr, struct net_if **iface)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv4_addr_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga53fb4ce0130fc8d665ddfd466d2a5eb8)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查此 IPv4 地址是否属于某个接口（Interface）。

<a id="r_ga496a33ce937652ff60e437f73590dcd8"></a>

```c
struct net_if_addr * net_if_ipv4_addr_lookup_by_iface (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv4_addr_lookup_by_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga496a33ce937652ff60e437f73590dcd8)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查此 IPv4 地址是否属于这个特定接口（Specific Interface）。

<a id="r_ga8164e6a01a311dcaa593039c90b5d7cb"></a>

```c
struct net_if_addr * net_if_ipv4_addr_add (struct net_if *iface, const struct net_in_addr *addr, enum net_addr_type addr_type, uint32_t vlifetime)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv4_addr_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8164e6a01a311dcaa593039c90b5d7cb)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_addr_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gafecee2d4a331dc85ad962b81a6303e41)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向接口（Interface）添加 IPv4 地址。

<a id="r_ga28c3dc1bd0f85710ab3fc8c012183742"></a>

```c
bool net_if_ipv4_addr_rm (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_addr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga28c3dc1bd0f85710ab3fc8c012183742)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

从接口（Interface）移除 IPv4 地址。

<a id="r_gae756e33c22b265b0218345cabfc85227"></a>

```c
int net_if_ipv4_addr_lookup_by_index (const struct net_in_addr *addr)
```

相关声明：[net_if_ipv4_addr_lookup_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae756e33c22b265b0218345cabfc85227)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查此 IPv4 地址是否属于某个接口索引（Interface Index）对应的接口。

<a id="r_ga336c5ec3a6af5b03fafc5796c16de396"></a>

```c
bool net_if_ipv4_addr_add_by_index (int index, const struct net_in_addr *addr, enum net_addr_type addr_type, uint32_t vlifetime)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_addr_add_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga336c5ec3a6af5b03fafc5796c16de396)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_addr_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gafecee2d4a331dc85ad962b81a6303e41)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过网络接口索引（Network Interface Index）向接口添加 IPv4 地址。

<a id="r_ga1b27ab5977aa53ce7f01195c76c23b13"></a>

```c
bool net_if_ipv4_addr_rm_by_index (int index, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_addr_rm_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1b27ab5977aa53ce7f01195c76c23b13)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

通过接口索引（Interface Index）从接口移除 IPv4 地址。

<a id="r_gaae71be476e27c178ebb21b0f183c2825"></a>

```c
void net_if_ipv4_addr_foreach (struct net_if *iface, net_if_ip_addr_cb_t cb, void *user_data)
```

相关声明：[net_if_ipv4_addr_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaae71be476e27c178ebb21b0f183c2825)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ip_addr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab58d8561a4f21899e2db34043d346516)。

遍历网络接口的全部 IPv4 地址，并对每个正在使用的地址调用回调（Callback）。

<a id="r_ga720bf6b3a90f747dd345c56d3afc0c13"></a>

```c
struct net_if_mcast_addr * net_if_ipv4_maddr_add (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)、[net_if_ipv4_maddr_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga720bf6b3a90f747dd345c56d3afc0c13)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

向接口（Interface）添加 IPv4 多播地址（Multicast Address）。

<a id="r_gaa5f133b3999b2d3342707b4a5357d16b"></a>

```c
bool net_if_ipv4_maddr_rm (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_maddr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa5f133b3999b2d3342707b4a5357d16b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

从接口（Interface）移除 IPv4 多播地址（Multicast Address）。

<a id="r_gae82f53c670f602e9c37b65abb6dfaec7"></a>

```c
void net_if_ipv4_maddr_foreach (struct net_if *iface, net_if_ip_maddr_cb_t cb, void *user_data)
```

相关声明：[net_if_ipv4_maddr_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae82f53c670f602e9c37b65abb6dfaec7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ip_maddr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga726eed76563c223de8f611e2544febe9)。

遍历网络接口的全部 IPv4 多播地址（Multicast Addresses），并对每个正在使用的地址调用回调。

<a id="r_gab6c07d40074298e0e49ed0a8c6a230c1"></a>

```c
struct net_if_mcast_addr * net_if_ipv4_maddr_lookup (const struct net_in_addr *addr, struct net_if **iface)
```

相关声明：[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)、[net_if_ipv4_maddr_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab6c07d40074298e0e49ed0a8c6a230c1)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查此 IPv4 多播地址（Multicast Address）是否属于指定接口或某个接口（Interface）。

<a id="r_gae275a5e75817aa178d36f422573ad76a"></a>

```c
void net_if_ipv4_maddr_join (struct net_if *iface, struct net_if_mcast_addr *addr)
```

相关声明：[net_if_ipv4_maddr_join](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae275a5e75817aa178d36f422573ad76a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

将给定多播地址（Multicast Address）标记为已加入（Joined）。

<a id="r_gaa30769fc8016f1a7496b3ede277d8d8a"></a>

```c
static bool net_if_ipv4_maddr_is_joined (struct net_if_mcast_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_maddr_is_joined](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa30769fc8016f1a7496b3ede277d8d8a)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

检查是否已加入（Joined）给定多播地址（Multicast Address）。

<a id="r_ga1408fe384736d20f36c035c10007113c"></a>

```c
void net_if_ipv4_maddr_leave (struct net_if *iface, struct net_if_mcast_addr *addr)
```

相关声明：[net_if_ipv4_maddr_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1408fe384736d20f36c035c10007113c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

将给定多播地址（Multicast Address）标记为已退出（Left）。

<a id="r_ga7f8e34c1001e89d759d3a1e6a5538647"></a>

```c
static void net_if_ipv4_nbr_flush (struct net_if *iface)
```

相关声明：[net_if_ipv4_nbr_flush](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga7f8e34c1001e89d759d3a1e6a5538647)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

清空网络接口的 IPv4 邻居缓存（Neighbor Cache）。

<a id="r_ga5e676ccb2b0cf22410e595d61d8363ce"></a>

```c
static bool net_if_ipv4_nbr_rm (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_nbr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5e676ccb2b0cf22410e595d61d8363ce)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

从 IPv4 邻居缓存（Neighbor Cache）中移除一个邻居（Neighbor）。

<a id="r_ga4ce8f0f7d00b66b905ee9cf1a8b398c6"></a>

```c
static struct net_in_addr * net_if_router_ipv4 (struct net_if_router *router)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_router_ipv4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga4ce8f0f7d00b66b905ee9cf1a8b398c6)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)。

获取给定路由器（Router）的 IPv4 地址。

<a id="r_ga4a290f9bbd65c041e8722b92fe675b77"></a>

```c
struct net_if_router * net_if_ipv4_router_lookup (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv4_router_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga4a290f9bbd65c041e8722b92fe675b77)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查该 IPv4 地址是否为系统中已配置路由器（Router）的地址之一。

<a id="r_gaffdb60ab8db5de97fc5b568a5be1ee8e"></a>

```c
struct net_if_router * net_if_ipv4_router_find_default (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv4_router_find_default](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaffdb60ab8db5de97fc5b568a5be1ee8e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

查找用于此 IPv4 地址的默认路由器（Default Router）。

<a id="r_ga074030e3dd930630e519a1f26b662be6"></a>

```c
struct net_if_router * net_if_ipv4_router_add (struct net_if *iface, const struct net_in_addr *addr, bool is_default, uint16_t router_lifetime)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv4_router_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga074030e3dd930630e519a1f26b662be6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向系统添加 IPv4 路由器（Router）。

<a id="r_ga6be14f5307bc63ce87ff0a3fad7c7f4d"></a>

```c
bool net_if_ipv4_router_rm (struct net_if_router *router)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_router_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6be14f5307bc63ce87ff0a3fad7c7f4d)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)。

从系统移除 IPv4 路由器（Router）。

<a id="r_gadd50b3a60e8ede04e482b9df8953695d"></a>

```c
int net_if_ipv4_route_add (struct net_if *iface, const struct net_in_addr *addr, uint8_t mask_len, const struct net_in_addr *nexthop, uint32_t lifetime)
```

相关声明：[net_if_ipv4_route_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadd50b3a60e8ede04e482b9df8953695d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向系统路由表（Routing Table）添加 IPv4 路由（Route）。

<a id="r_ga919149bde5d0f1319ba60a9b8de1a1bc"></a>

```c
bool net_if_ipv4_addr_mask_cmp (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_addr_mask_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga919149bde5d0f1319ba60a9b8de1a1bc)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查给定 IPv4 地址是否属于本地子网（Local Subnet）。

<a id="r_ga45774258112186b5989b974df934dff1"></a>

```c
bool net_if_ipv4_is_addr_bcast (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_is_addr_bcast](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga45774258112186b5989b974df934dff1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查给定的 IPv4 地址是否为广播地址（Broadcast Address）。

<a id="r_ga1e66458147628585dd5dd613a68a87a3"></a>

```c
static struct net_if * net_if_ipv4_select_src_iface (const struct net_in_addr *dst)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv4_select_src_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1e66458147628585dd5dd613a68a87a3)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

获取向目的地发送 IPv4 网络数据时应使用的网络接口（Network Interface）。

<a id="r_ga29b73b4d2d18edc06b36f5e5dbcbd441"></a>

```c
static struct net_if * net_if_ipv4_select_src_iface_addr (const struct net_in_addr *dst, const struct net_in_addr **src_addr)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv4_select_src_iface_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga29b73b4d2d18edc06b36f5e5dbcbd441)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

获取向目的地发送 IPv4 网络数据时应使用的网络接口（Network Interface）。

<a id="r_gae7ee369901b43a3bd071dacd3a51049a"></a>

```c
static const struct net_in_addr * net_if_ipv4_select_src_addr (struct net_if *iface, const struct net_in_addr *dst)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_ipv4_select_src_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae7ee369901b43a3bd071dacd3a51049a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

获取向目的地发送网络数据时应使用的 IPv4 源地址（Source Address）。

<a id="r_ga6ea398dd6a15e74423fdd55b6a8976f5"></a>

```c
struct net_in_addr * net_if_ipv4_get_ll (struct net_if *iface, enum net_addr_state addr_state)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_ipv4_get_ll](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6ea398dd6a15e74423fdd55b6a8976f5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_addr_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga32e58fc83532ef57eeb6ff952f17288d)。

获取处于给定状态的 IPv4 链路本地地址（Link Local Address）。

<a id="r_ga7648ccab37ffa991f757e6c6a985eec1"></a>

```c
struct net_in_addr * net_if_ipv4_get_global_addr (struct net_if *iface, enum net_addr_state addr_state)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_ipv4_get_global_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga7648ccab37ffa991f757e6c6a985eec1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_addr_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga32e58fc83532ef57eeb6ff952f17288d)。

获取处于给定状态的 IPv4 全局地址（Global Address）。

<a id="r_gaafc473b7c3f3e32f1ba93dd1f7190fe5"></a>

```c
struct net_in_addr net_if_ipv4_get_netmask_by_addr (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_ipv4_get_netmask_by_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaafc473b7c3f3e32f1ba93dd1f7190fe5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

获取与接口某个地址关联的 IPv4 网络掩码（Netmask）。

<a id="r_gaa5087a91a20e4283b4fa9a09add6aaa0"></a>

```c
bool net_if_ipv4_set_netmask_by_addr_by_index (int index, const struct net_in_addr *addr, const struct net_in_addr *netmask)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_set_netmask_by_addr_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa5087a91a20e4283b4fa9a09add6aaa0)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

根据接口索引（Interface Index），为给定地址设置 IPv4 网络掩码（Netmask）。

<a id="r_gaa42af45521841ae8265396c89966a2db"></a>

```c
bool net_if_ipv4_set_netmask_by_addr (struct net_if *iface, const struct net_in_addr *addr, const struct net_in_addr *netmask)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_set_netmask_by_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa42af45521841ae8265396c89966a2db)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

根据接口索引（Interface Index），为给定地址设置 IPv4 网络掩码（Netmask）。

<a id="r_ga12eee59d98d9891f88ed75fbeb5f4d19"></a>

```c
struct net_in_addr net_if_ipv4_get_gw (struct net_if *iface)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_ipv4_get_gw](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga12eee59d98d9891f88ed75fbeb5f4d19)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取接口的 IPv4 网关（Gateway）。

<a id="r_ga0826491553b11c764277cde76490eb02"></a>

```c
void net_if_ipv4_set_gw (struct net_if *iface, const struct net_in_addr *gw)
```

相关声明：[net_if_ipv4_set_gw](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0826491553b11c764277cde76490eb02)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

设置接口的 IPv4 网关（Gateway）。

<a id="r_ga8810a82cf2b6e3f44541c47c635e39de"></a>

```c
bool net_if_ipv4_set_gw_by_index (int index, const struct net_in_addr *gw)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_set_gw_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8810a82cf2b6e3f44541c47c635e39de)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

根据接口索引（Interface Index）设置 IPv4 网关（Gateway）。

<a id="r_gab3c666bf6a0677c25e90082fed88f7a5"></a>

```c
struct net_if * net_if_select_src_iface (const struct net_sockaddr *dst)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_select_src_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab3c666bf6a0677c25e90082fed88f7a5)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

获取向目的地发送 IPv6 或 IPv4 网络数据时应使用的网络接口（Network Interface）。

<a id="r_gaa81b7d9ed8dc05da3391265dbc89b665"></a>

```c
void net_if_register_link_cb (struct net_if_link_cb *link, net_if_link_callback_t cb)
```

相关声明：[net_if_register_link_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa81b7d9ed8dc05da3391265dbc89b665)、[net_if_link_cb](../network_core_model_reference/P088_net_if_link_cb_结构体.md)、[net_if_link_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0f87d5753fcd7cce40ecd161e6c91078)。

注册链路回调（Link Callback）。

<a id="r_ga6ba64fac6e8d846ae7be5990f49a8293"></a>

```c
void net_if_unregister_link_cb (struct net_if_link_cb *link)
```

相关声明：[net_if_unregister_link_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6ba64fac6e8d846ae7be5990f49a8293)、[net_if_link_cb](../network_core_model_reference/P088_net_if_link_cb_结构体.md)。

注销链路回调（Link Callback）。

<a id="r_gaaa64aa4391a85760bb2daf600ac4d898"></a>

```c
void net_if_call_link_cb (struct net_if *iface, struct net_linkaddr *lladdr, int status)
```

相关声明：[net_if_call_link_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaaa64aa4391a85760bb2daf600ac4d898)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

调用链路回调函数（Link Callback Function）。

<a id="r_gac040bd7860e5cd6424709fbf98dd4a99"></a>

```c
static bool net_if_need_calc_rx_checksum (struct net_if *iface, enum net_if_checksum_type chksum_type)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_need_calc_rx_checksum](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gac040bd7860e5cd6424709fbf98dd4a99)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_checksum_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8db412ae79c64cafe81a66f5acb2f8e9)。

检查是否可以省略接收网络数据包的校验和计算（Checksum Calculation）。

<a id="r_ga0db8854bb77133b19c5b0852b43119bb"></a>

```c
static bool net_if_need_calc_tx_checksum (struct net_if *iface, enum net_if_checksum_type chksum_type)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_need_calc_tx_checksum](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0db8854bb77133b19c5b0852b43119bb)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_checksum_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8db412ae79c64cafe81a66f5acb2f8e9)。

检查发送网络数据包时是否可以省略校验和计算（Checksum Calculation）。

<a id="r_ga72708cdb7f133fe5d7edf819756c3516"></a>

```c
struct net_if * net_if_get_by_index (int index)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga72708cdb7f133fe5d7edf819756c3516)。

根据索引（Index）获取接口（Interface）。

<a id="r_ga02445f6c61f0d29f56ac0ef59e025630"></a>

```c
int net_if_get_by_iface (struct net_if *iface)
```

相关声明：[net_if_get_by_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga02445f6c61f0d29f56ac0ef59e025630)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

根据指针（Pointer）获取接口索引（Interface Index）。

<a id="r_ga96b198fd9df4a985b0dde84dd7152815"></a>

```c
void net_if_foreach (net_if_cb_t cb, void *user_data)
```

相关声明：[net_if_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga96b198fd9df4a985b0dde84dd7152815)、[net_if_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gac48ab8e6337e7cf387af9b293f254a80)。

遍历全部网络接口（Network Interfaces），并为每个接口调用回调。

<a id="r_ga02644cc623fc7a8878c17d54984e4210"></a>

```c
int net_if_up (struct net_if *iface)
```

相关声明：[net_if_up](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga02644cc623fc7a8878c17d54984e4210)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启用接口（Bring Interface Up）。

<a id="r_ga7e9b368d4abf9da5656140df70cfa334"></a>

```c
static bool net_if_is_up (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_up](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga7e9b368d4abf9da5656140df70cfa334)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查接口是否已启用且正在运行（Up and Running）。

<a id="r_ga2187650062d6139b9f4b81745a206803"></a>

```c
int net_if_down (struct net_if *iface)
```

相关声明：[net_if_down](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2187650062d6139b9f4b81745a206803)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

停用接口（Bring Interface Down）。

<a id="r_ga099a484a654ad9af35d3212fc2c995b2"></a>

```c
static bool net_if_is_admin_up (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_admin_up](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga099a484a654ad9af35d3212fc2c995b2)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查接口是否已由管理员启用（Brought Up by the Administrator）。

<a id="r_ga35e5db3a631ac9039f14d86e59fc0dcc"></a>

```c
void net_if_carrier_on (struct net_if *iface)
```

相关声明：[net_if_carrier_on](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga35e5db3a631ac9039f14d86e59fc0dcc)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

底层网络设备已检测到载波（Carrier），即网线已连接。

<a id="r_ga6839941422a88c1f707ab70ea34df323"></a>

```c
void net_if_carrier_off (struct net_if *iface)
```

相关声明：[net_if_carrier_off](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6839941422a88c1f707ab70ea34df323)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

底层网络设备已失去载波（Carrier），即网线已断开。

<a id="r_ga095554237016e563d76cfd602d1dae77"></a>

```c
static bool net_if_is_carrier_ok (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_carrier_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga095554237016e563d76cfd602d1dae77)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查网络设备是否存在载波（Carrier）。

<a id="r_ga89a3374d4bb116460a7b7c50a750b593"></a>

```c
void net_if_dormant_on (struct net_if *iface)
```

相关声明：[net_if_dormant_on](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga89a3374d4bb116460a7b7c50a750b593)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将接口标记为休眠（Dormant）。

<a id="r_ga1c31fac887d944ac0a16aad70e889496"></a>

```c
void net_if_dormant_off (struct net_if *iface)
```

相关声明：[net_if_dormant_off](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1c31fac887d944ac0a16aad70e889496)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将接口标记为非休眠（Not Dormant）。

<a id="r_ga6e2e6102271c37acaa59c54e2aa6b413"></a>

```c
static bool net_if_is_dormant (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_dormant](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6e2e6102271c37acaa59c54e2aa6b413)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查接口是否处于休眠状态（Dormant）。

<a id="r_ga198accbfeaeb049eba9ffa2fac82c747"></a>

```c
void net_if_register_timestamp_cb (struct net_if_timestamp_cb *handle, struct net_pkt *pkt, struct net_if *iface, net_if_timestamp_callback_t cb)
```

相关声明：[net_if_register_timestamp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga198accbfeaeb049eba9ffa2fac82c747)、[net_if_timestamp_cb](../network_core_model_reference/P092_net_if_timestamp_cb_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_timestamp_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga656c2ba47d280aa1c47bc2d062debbfa)。

注册时间戳回调（Timestamp Callback）。

<a id="r_gaa5b88649296a278860ca36f14369834f"></a>

```c
void net_if_unregister_timestamp_cb (struct net_if_timestamp_cb *handle)
```

相关声明：[net_if_unregister_timestamp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa5b88649296a278860ca36f14369834f)、[net_if_timestamp_cb](../network_core_model_reference/P092_net_if_timestamp_cb_结构体.md)。

注销时间戳回调（Timestamp Callback）。

<a id="r_gada944cae018ee13d5478402a850e89e2"></a>

```c
void net_if_call_timestamp_cb (struct net_pkt *pkt)
```

相关声明：[net_if_call_timestamp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gada944cae018ee13d5478402a850e89e2)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

调用时间戳回调函数（Timestamp Callback Function）。

<a id="r_ga139ca2bcb45e9ab45b309c5004bb11c7"></a>

```c
void net_if_add_tx_timestamp (struct net_pkt *pkt)
```

相关声明：[net_if_add_tx_timestamp](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga139ca2bcb45e9ab45b309c5004bb11c7)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

<a id="r_gaf9f81f3b9697ca47f7674d85f37a8d80"></a>

```c
static int net_if_set_promisc (struct net_if *iface)
```

相关声明：[net_if_set_promisc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf9f81f3b9697ca47f7674d85f37a8d80)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将网络接口设为混杂模式（Promiscuous Mode）。

<a id="r_ga9c8212c087883510050ac6a39ef0a7bf"></a>

```c
static void net_if_unset_promisc (struct net_if *iface)
```

相关声明：[net_if_unset_promisc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9c8212c087883510050ac6a39ef0a7bf)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将网络接口设为正常模式（Normal Mode）。

<a id="r_ga9f1a6eab849517734ec422deb0ba71f5"></a>

```c
static bool net_if_is_promisc (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_promisc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9f1a6eab849517734ec422deb0ba71f5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查是否设置了混杂模式（Promiscuous Mode）。

<a id="r_ga3cddda628eca248246f9aa3b81938f95"></a>

```c
static bool net_if_are_pending_tx_packets (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_are_pending_tx_packets](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3cddda628eca248246f9aa3b81938f95)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查给定网络接口是否有待发送的网络数据（Pending TX Network Data）。

<a id="r_ga703d9e3c128a3a3f0e452d789a4b7bf6"></a>

```c
bool net_if_is_ethernet (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_ethernet](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga703d9e3c128a3a3f0e452d789a4b7bf6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查网络接口是否为有线以太网（Cabled Ethernet）。

<a id="r_ga529067a284cac1187b336080e56129c8"></a>

```c
struct net_if * net_if_get_first_ethernet (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_first_ethernet](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga529067a284cac1187b336080e56129c8)。

获取第一个有线以太网网络接口（Cabled Ethernet Network Interface）。

<a id="r_gaa458b5f349c55007108b47b99f4954d5"></a>

```c
bool net_if_is_wifi (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_wifi](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa458b5f349c55007108b47b99f4954d5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查网络接口是否支持 Wi-Fi。

<a id="r_ga6e89bbafb6c0acdc6bf51078e2027236"></a>

```c
struct net_if * net_if_get_first_wifi (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_first_wifi](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6e89bbafb6c0acdc6bf51078e2027236)。

获取第一个 Wi-Fi 网络接口（Network Interface）。

<a id="r_ga0fc3ba6172956f6847027e0bd3d367de"></a>

```c
struct net_if * net_if_get_wifi_sta (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_wifi_sta](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0fc3ba6172956f6847027e0bd3d367de)。

获取 Wi-Fi 网络站点接口（Station Interface）。

<a id="r_gaf830eab616191009d88f58b761694b49"></a>

```c
struct net_if * net_if_get_wifi_sap (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_wifi_sap](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf830eab616191009d88f58b761694b49)。

获取第一个 Wi-Fi 网络软件接入点接口（Soft-AP Interface）。

<a id="r_ga5f653cd73c1ecd548a931eb7fbd170f7"></a>

```c
int net_if_get_name (struct net_if *iface, char *buf, int len)
```

相关声明：[net_if_get_name](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5f653cd73c1ecd548a931eb7fbd170f7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取网络接口名称（Network Interface Name）。

<a id="r_ga05dec64966fc39e3deb0679b9585688b"></a>

```c
int net_if_set_name (struct net_if *iface, const char *buf)
```

相关声明：[net_if_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga05dec64966fc39e3deb0679b9585688b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置网络接口名称（Network Interface Name）。

<a id="r_ga1774ac036032bb0dc2c662f6f4f66a7f"></a>

```c
int net_if_get_by_name (const char *name)
```

相关声明：[net_if_get_by_name](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1774ac036032bb0dc2c662f6f4f66a7f)。

根据名称（Name）获取接口索引（Interface Index）。


## 3.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/net_core.h](../api_source_system_reference/P023_net_core.h_源码浏览.md)
- [zephyr/net/hostname.h](../api_source_reference/P322_hostname.h_源码浏览.md)
- [zephyr/net/net_linkaddr.h](../api_source_reference/P576_net_linkaddr.h_源码浏览.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/net_l2.h](../api_source_reference/P575_net_l2.h_源码浏览.md)
- [zephyr/net/net_stats.h](../api_source_interrupt_modem_reference/P007_net_stats.h_源码浏览.md)
- [zephyr/net/net_timeout.h](../time_headers_reference/P010_网络超时头文件源码.md)
- [zephyr/net/prometheus/collector.h](../api_source_reference/P109_collector.h_源码浏览.md)
- [查看此文件的源码。](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)
- [net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)
- [net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)
- [net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)
- [net_if_ipv6](../network_core_model_reference/P086_net_if_ipv6_结构体.md)
- [net_if_addr_ipv4](../network_core_model_reference/P081_net_if_addr_ipv4_结构体.md)
- [net_if_ipv4](../network_core_model_reference/P085_net_if_ipv4_结构体.md)
- [net_if_ip](../network_core_model_reference/P084_net_if_ip_结构体.md)
- [net_if_config](../network_core_model_reference/P082_net_if_config_结构体.md)
- [net_traffic_class](../network_core_model_reference/P154_net_traffic_class_结构体.md)
- [net_if_dev](../network_core_model_reference/P083_net_if_dev_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_if_mcast_monitor](../network_core_model_reference/P090_net_if_mcast_monitor_结构体.md)
- [net_if_link_cb](../network_core_model_reference/P088_net_if_link_cb_结构体.md)
- [net_if_timestamp_cb](../network_core_model_reference/P092_net_if_timestamp_cb_结构体.md)
- [NET_IF_IPV6_DAD_NONCE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2b824eff0adada3eb7ff626a8d7c3538)
- [RFC 7527, section-4](https://datatracker.ietf.org/doc/html/rfc7527#section-4)
- [NET_IPV6_MAX_REACHABLE_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga021e9877ee9532a899a298d6a2c7aeb2)
- [NET_IF_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae0fdb0b909e06ba7831e53700c32b84f)
- [NET_IF_DT_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga65e4d856b53096bf784a4d5a495ca507)
- [NET_IF_DT_INST_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga421f0b8be2317c0865c50ca588f73509)
- [NET_IF_DT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadd040e5cc26a96c3f66f37539178c3b6)
- [NET_IF_DT_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga48a80b52d8b5a16856c86041fc6492e6)
- [NET_DEVICE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga02971562c42494e2a5f71e1f8587e709)
- [NET_DEVICE_DT_ADD_IFACE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad8e37fc7a32339312dcfa614255988e8)
- [NET_DEVICE_DT_INST_ADD_IFACE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga00fe86342a77e32fe440e1bd97c51d51)
- [NET_DEVICE_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab1f762b01ae7bc37cd4a25724c123dda)
- [NET_DEVICE_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga7edd8bc59444d92cad0371c36f9949b7)
- [NET_DEVICE_INIT_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gacc7edecdd9de9920cc155977d8fec2a2)
- [NET_DEVICE_DT_DEFINE_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga50702b043a0791e59e7d5679dda1d9e8)
- [NET_DEVICE_DT_INST_DEFINE_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gabe4b8589996a53cbc50b76c8ea15aa0c)
- [NET_DEVICE_OFFLOAD_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga255672607b7958db3f464d2a57a7e635)
- [NET_DEVICE_DT_OFFLOAD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab2b287025e194dec1fab24e44d95362f)
- [NET_DEVICE_DT_INST_OFFLOAD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1cab6943a28e3d3754e36623834b93fd)
- [NET_IFACE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6c081875a6f5a848b3ad2fd220c63c3c)
- [net_socket_create_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaef3dfe26195514aac625e9f22e399759)
- [net_if_ip_addr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab58d8561a4f21899e2db34043d346516)
- [net_if_ip_maddr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga726eed76563c223de8f611e2544febe9)
- [net_if_mcast_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0d64291573740a67eae7ff3fcc0910c5)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_if_link_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0f87d5753fcd7cce40ecd161e6c91078)
- [net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)
- [net_if_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gac48ab8e6337e7cf387af9b293f254a80)
- [net_if_timestamp_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga656c2ba47d280aa1c47bc2d062debbfa)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae691e5537917ffce27ad0db82c730371)
- [NET_IF_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840)
- [NET_IF_POINTOPOINT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009)
- [NET_IF_PROMISC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141)
- [NET_IF_NO_AUTO_START](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05)
- [NET_IF_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0)
- [NET_IF_FORWARD_MULTICASTS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac)
- [NET_IF_IPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329)
- [NET_IF_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6)
- [NET_IF_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a)
- [NET_IF_LOWER_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d)
- [NET_IF_DORMANT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d)
- [NET_IF_IPV6_NO_ND](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7)
- [NET_IF_IPV6_NO_MLD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe)
- [NET_IF_NO_TX_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9)
- [net_if_oper_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadfe9d90f24046cd9bd4bbee096e747b9)
- [NET_IF_OPER_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58)
- [NET_IF_OPER_NOTPRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32)
- [NET_IF_OPER_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367)
- [NET_IF_OPER_LOWERLAYERDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4)
- [NET_IF_OPER_TESTING](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f)
- [NET_IF_OPER_DORMANT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d)
- [NET_IF_OPER_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)
- [RFC 2863](https://datatracker.ietf.org/doc/html/rfc2863)
- [net_if_checksum_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8db412ae79c64cafe81a66f5acb2f8e9)
- [NET_IF_CHECKSUM_IPV4_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30)
- [NET_IF_CHECKSUM_IPV4_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad)
- [NET_IF_CHECKSUM_IPV4_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3)
- [NET_IF_CHECKSUM_IPV4_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1)
- [NET_IF_CHECKSUM_IPV6_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b)
- [NET_IF_CHECKSUM_IPV6_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13)
- [NET_IF_CHECKSUM_IPV6_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660)
- [NET_IF_CHECKSUM_IPV6_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3)
- [net_if_flag_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga52f9fca13e9f836799e0e40f581744d2)
- [net_if_flag_test_and_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga42e7482191a92007960601f8bb621dca)
- [net_if_flag_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaff751b6a92b0c608ecfc50e8c0587fd3)
- [net_if_flag_test_and_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab8f371c7f8890cf4728177f6595141d7)
- [net_if_flag_is_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae1f373ddd61c18a81481d8ddcfb12543)
- [net_if_oper_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1f1bf845e63cce02e2183889cc85d57e)
- [net_if_oper_state](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad9e957a4866b4566296ee39392fde0e4)
- [net_if_oper_state_change_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gabae216ba527bdfcd945ef19fb48e56be)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)
- [net_if_try_send_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5d01d7fa6c7511d68933ad4cec032d8a)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_if_send_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga84a58403183b88c64fda59d5d2d903fc)
- [net_l2](../network_core_model_reference/P103_net_l2_结构体.md)
- [net_if_l2](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gafa451f6118529d1d084704d00b2aae20)
- [net_if_recv_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga72ed21ca0cb220199f5a2070137c7fef)
- [net_if_l2_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3cad2d51fc9cc225619585e06e252db0)
- [device](../device_reference/P002_设备对象结构.md)
- [net_if_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)
- [net_if_try_queue_tx](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3617cd1f712b8a85fdd7f1425254ae5d)
- [net_if_queue_tx](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2ac749d465ef7f0f64f294a30310457e)
- [net_if_is_ip_offloaded](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6bfa5f84a2127bbad27a0a3b319526a1)
- [net_if_is_offloaded](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaecedc93a6dab2c57fe686718ea4d78af)
- [net_if_offload](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga520939e94620ca75475a71f153df6d4a)
- [net_if_offload_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf2d323c1504125fbfde5da9ada8c5657)
- [net_if_is_socket_offloaded](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf308baf2241fa455b50b439b7fab3f1e)
- [net_if_socket_offload_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9db52875580115c743b1f35cd6c46796)
- [net_if_socket_offload](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gafb2bbaec96c4759d920b2866c0b3ef3a)
- [net_if_get_link_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga467186e964bf721e14fed38392f21872)
- [net_if_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae271e0e4dcb031a83d9908e597a45048)
- [net_if_start_dad](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9655c010ccbf989e9328271f5dbcc685)
- [net_if_start_rs](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab9bdb7f8a9eeed4d9b70965b8af82cb7)
- [net_if_stop_rs](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab0195bb2151a1ba722a0b11d81066988)
- [net_if_nbr_reachability_hint](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga655599b1432463455610cff768997e2b)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [net_if_ipv6_nbr_flush](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaaa6c3d31d3a40cab6cf9e4f4af959b89)
- [net_if_ipv6_nbr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gac6bc061b5b0facc5023da2a835fb9bb3)
- [net_if_set_link_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3863e011f89dff02c3df3ca4a88680e9)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_link_type](../api_input_runtime_topic_reference/P015_网络链路地址库（Network Link Address Library）.md#ga1312c2322bc4a4f1c3b76d6466806b24)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_if_get_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gacddc98531c5748db5a34f5c3a3e96e86)
- [net_if_set_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga76b140c6fc39b94ff4102e08e3a58e81)
- [net_if_addr_set_lf](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae66f6e7bd31545e6161fcd4600fe5842)
- [net_if_get_by_link_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1b058361dc9bcac7d842bb49846a0c79)
- [net_if_lookup_by_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadbb8be32caa896bdcdeee19425134827)
- [net_if_router_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadc87242eb7205362a308b3c4437bf76d)
- [net_if_set_default](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0a1f27ec893e1af3c97f130be4616589)
- [net_if_get_default](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga55214771e462cbd4930ffa738813cb87)
- [net_if_get_first_by_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga762337e8b66874a0fbf59bdbeba173f5)
- [net_if_get_first_up](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga03d8c6aebb1412382a9eec636c227238)
- [net_if_config_ipv6_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga56c9aef19bc9827d9ec96c00e10840fa)
- [net_if_config_ipv6_put](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8af1400b354c42a64795cdb1a600ddd6)
- [net_if_ipv6_addr_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga4314c59af790e537e384e969c58fab9d)
- [net_if_ipv6_addr_lookup_by_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae2935f8b0ad41879b12a491bc260b236)
- [net_if_ipv6_addr_lookup_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaaba6b0ba57a19c3d24628e8498ef421d)
- [net_if_ipv6_addr_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3b651babfb5d1dd9f8d266d2aa1cf1b8)
- [net_addr_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gafecee2d4a331dc85ad962b81a6303e41)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [net_if_ipv6_addr_add_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad68f25bd25b198bc4280d334f71495d3)
- [net_if_ipv6_addr_update_lifetime](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaef8a6752a201f81636c4ffc1ebba4a25)
- [net_if_ipv6_addr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad0e9473f494d154c4cd89e3e67a13232)
- [net_if_ipv6_addr_rm_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadc08ec8c23d2ee138eb3a05cdfe00701)
- [net_if_ipv6_addr_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5ac646ad7fda0fa48e78c15b4ca52d50)
- [net_if_ipv6_maddr_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1608a77ffca421769bae381a12e179ce)
- [net_if_ipv6_maddr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6c80fd9c864cb54902d52adcb5d8d639)
- [net_if_ipv6_maddr_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab677496fb2e27be2df299a346e9c7132)
- [net_if_ipv6_maddr_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad520342d393f523c56a98fa618876b54)
- [net_if_mcast_mon_register](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8fdd0665ed76db6055777e395ca60255)
- [net_if_mcast_mon_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad323732fe3d178a5dfdf0900e5cb5683)
- [net_if_mcast_monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga372ef131263269cd65586d87997df745)
- [net_if_ipv6_maddr_join](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga49dbc954015307222f176f4149829b76)
- [net_if_ipv6_maddr_is_joined](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gabe2c16a378a35a22d008bff9142e5449)
- [net_if_ipv6_maddr_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad24d5537d52de9781a7a6a55ceedd92b)
- [net_if_ipv6_prefix_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9c10341ab913f0b609c2724354ec587a)
- [net_if_ipv6_prefix_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga99b22d24fef63bd1681396410b930008)
- [net_if_ipv6_prefix_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2616868a6d51cbf1d35c6920e258d412)
- [net_if_ipv6_prefix_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga4b8668b32a14996c68d10ec989c1abb3)
- [net_if_ipv6_prefix_set_lf](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa3c711e814fb6a4e552b4ef723d0baa0)
- [net_if_ipv6_prefix_set_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga68cffe343c518bad7f7f152e30f7f9ee)
- [net_if_ipv6_prefix_unset_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)
- [net_if_ipv6_prefix_set_advertise](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9ff61003d36ee19af27a9b1b24b22170)
- [net_if_ipv6_router_start](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1c062890f66b97dbb723339fede121ff)
- [net_if_ipv6_router_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa56d3dbc96301e6fa70ee61b08c29841)
- [net_if_ipv6_addr_onlink](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga53cc6d8d43f3b3ef7c275dff69b4de8d)
- [net_if_router_ipv6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga17d846ec0cbc1e67fd4a2bc1179b7c45)
- [net_if_ipv6_router_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gac68a72e70b5335773964dbfc0319eee5)
- [net_if_ipv6_router_find_default](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gabfabdb7afa073b54f67d67320da3983c)
- [net_if_ipv6_router_update_lifetime](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaadba4957802dc376ef011590c91c6af6)
- [net_if_ipv6_router_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8d80080463bcb9035e06e0ac35090780)
- [net_if_ipv6_router_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1d108aa0b54c072e0aa9d0c049f02807)
- [net_if_ipv6_get_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga66d0a9a8eef095f6d4d44f35dd67f2b6)
- [net_if_ipv6_set_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5bf726bb5c1d232103ec6841e7d0cd8c)
- [net_if_ipv6_get_mcast_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga56e7086633bcf4537f54c7ca70e6c900)
- [net_if_ipv6_set_mcast_hop_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf56a433679ea9701cf8baa3208f8ccc3)
- [net_if_ipv6_set_base_reachable_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab3939d735b660f8f02124df656ceba2c)
- [net_if_ipv6_get_base_reachable_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga71eb0b9842db6db6930c3567e94d4bd6)
- [net_if_ipv6_get_reachable_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9dd1f91edbb519a6a079f363c33efacf)
- [net_if_ipv6_calc_reachable_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab1861b5cefa73b4eefbb447cb1438cdc)
- [net_if_ipv6_set_reachable_time](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8328266b870fd200660cb2becaab3de4)
- [net_if_ipv6_set_retrans_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gad74566e5a34f447d2ac63d2c0e82eeff)
- [net_if_ipv6_get_retrans_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaddbf5a6ba412e6bdb7e31568fe827bd0)
- [net_if_ipv6_select_src_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5f8fc8725d3050a0e8fb0c3c75791c7c)
- [net_if_ipv6_select_src_addr_hint](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga55df4f4967efb4840dbee7a4078a237b)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [net_if_ipv6_select_src_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga367c74aad10b58074e5e1e517d6be379)
- [net_if_ipv6_select_src_iface_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8c3fe8f29294c8bb9561d22625cf726c)
- [net_if_ipv6_get_ll](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga76ebc895fb5959f7f4a2884024bb4963)
- [net_addr_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga32e58fc83532ef57eeb6ff952f17288d)
- [net_if_ipv6_get_ll_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga89ea06beb89db41d064b23186c92a567)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [net_if_ipv6_dad_failed](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8f37df9b421963d33a0838fe1fedde2a)
- [net_if_ipv6_get_global_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf466f15f578d0ab287d8d3a258a64bb3)
- [net_if_config_ipv4_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3390e248249b28f2c80e2ca0bc79d236)
- [net_if_config_ipv4_put](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga88c13a45617480a665c7f9f589ec8e10)
- [net_if_ipv4_get_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga7e1fd28dbcf1164d056296b4df782e64)
- [net_if_ipv4_set_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5544374d7ebea26a239d561083f0203d)
- [net_if_ipv4_get_mcast_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga71acb65b1988aab8cca9c9604c86231e)
- [net_if_ipv4_set_mcast_ttl](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9452fef4f1309fb1a53a6a8b4f222377)
- [net_if_ipv4_addr_onlink](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0f324d39cf60e7babb5a1c4a364a8e86)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_if_ipv4_addr_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga53fb4ce0130fc8d665ddfd466d2a5eb8)
- [net_if_ipv4_addr_lookup_by_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga496a33ce937652ff60e437f73590dcd8)
- [net_if_ipv4_addr_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8164e6a01a311dcaa593039c90b5d7cb)
- [net_if_ipv4_addr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga28c3dc1bd0f85710ab3fc8c012183742)
- [net_if_ipv4_addr_lookup_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae756e33c22b265b0218345cabfc85227)
- [net_if_ipv4_addr_add_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga336c5ec3a6af5b03fafc5796c16de396)
- [net_if_ipv4_addr_rm_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1b27ab5977aa53ce7f01195c76c23b13)
- [net_if_ipv4_addr_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaae71be476e27c178ebb21b0f183c2825)
- [net_if_ipv4_maddr_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga720bf6b3a90f747dd345c56d3afc0c13)
- [net_if_ipv4_maddr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa5f133b3999b2d3342707b4a5357d16b)
- [net_if_ipv4_maddr_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae82f53c670f602e9c37b65abb6dfaec7)
- [net_if_ipv4_maddr_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab6c07d40074298e0e49ed0a8c6a230c1)
- [net_if_ipv4_maddr_join](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae275a5e75817aa178d36f422573ad76a)
- [net_if_ipv4_maddr_is_joined](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa30769fc8016f1a7496b3ede277d8d8a)
- [net_if_ipv4_maddr_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1408fe384736d20f36c035c10007113c)
- [net_if_ipv4_nbr_flush](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga7f8e34c1001e89d759d3a1e6a5538647)
- [net_if_ipv4_nbr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5e676ccb2b0cf22410e595d61d8363ce)
- [net_if_router_ipv4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga4ce8f0f7d00b66b905ee9cf1a8b398c6)
- [net_if_ipv4_router_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga4a290f9bbd65c041e8722b92fe675b77)
- [net_if_ipv4_router_find_default](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaffdb60ab8db5de97fc5b568a5be1ee8e)
- [net_if_ipv4_router_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga074030e3dd930630e519a1f26b662be6)
- [net_if_ipv4_router_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6be14f5307bc63ce87ff0a3fad7c7f4d)
- [net_if_ipv4_route_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gadd50b3a60e8ede04e482b9df8953695d)
- [net_if_ipv4_addr_mask_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga919149bde5d0f1319ba60a9b8de1a1bc)
- [net_if_ipv4_is_addr_bcast](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga45774258112186b5989b974df934dff1)
- [net_if_ipv4_select_src_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1e66458147628585dd5dd613a68a87a3)
- [net_if_ipv4_select_src_iface_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga29b73b4d2d18edc06b36f5e5dbcbd441)
- [net_if_ipv4_select_src_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae7ee369901b43a3bd071dacd3a51049a)
- [net_if_ipv4_get_ll](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6ea398dd6a15e74423fdd55b6a8976f5)
- [net_if_ipv4_get_global_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga7648ccab37ffa991f757e6c6a985eec1)
- [net_if_ipv4_get_netmask_by_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaafc473b7c3f3e32f1ba93dd1f7190fe5)
- [net_if_ipv4_set_netmask_by_addr_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa5087a91a20e4283b4fa9a09add6aaa0)
- [net_if_ipv4_set_netmask_by_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa42af45521841ae8265396c89966a2db)
- [net_if_ipv4_get_gw](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga12eee59d98d9891f88ed75fbeb5f4d19)
- [net_if_ipv4_set_gw](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0826491553b11c764277cde76490eb02)
- [net_if_ipv4_set_gw_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga8810a82cf2b6e3f44541c47c635e39de)
- [net_if_select_src_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab3c666bf6a0677c25e90082fed88f7a5)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_if_register_link_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa81b7d9ed8dc05da3391265dbc89b665)
- [net_if_unregister_link_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6ba64fac6e8d846ae7be5990f49a8293)
- [net_if_call_link_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaaa64aa4391a85760bb2daf600ac4d898)
- [net_if_need_calc_rx_checksum](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gac040bd7860e5cd6424709fbf98dd4a99)
- [net_if_need_calc_tx_checksum](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0db8854bb77133b19c5b0852b43119bb)
- [net_if_get_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga72708cdb7f133fe5d7edf819756c3516)
- [net_if_get_by_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga02445f6c61f0d29f56ac0ef59e025630)
- [net_if_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga96b198fd9df4a985b0dde84dd7152815)
- [net_if_up](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga02644cc623fc7a8878c17d54984e4210)
- [net_if_is_up](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga7e9b368d4abf9da5656140df70cfa334)
- [net_if_down](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2187650062d6139b9f4b81745a206803)
- [net_if_is_admin_up](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga099a484a654ad9af35d3212fc2c995b2)
- [net_if_carrier_on](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga35e5db3a631ac9039f14d86e59fc0dcc)
- [net_if_carrier_off](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6839941422a88c1f707ab70ea34df323)
- [net_if_is_carrier_ok](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga095554237016e563d76cfd602d1dae77)
- [net_if_dormant_on](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga89a3374d4bb116460a7b7c50a750b593)
- [net_if_dormant_off](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1c31fac887d944ac0a16aad70e889496)
- [net_if_is_dormant](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6e2e6102271c37acaa59c54e2aa6b413)
- [net_if_register_timestamp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga198accbfeaeb049eba9ffa2fac82c747)
- [net_if_unregister_timestamp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa5b88649296a278860ca36f14369834f)
- [net_if_call_timestamp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gada944cae018ee13d5478402a850e89e2)
- [net_if_add_tx_timestamp](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga139ca2bcb45e9ab45b309c5004bb11c7)
- [net_if_set_promisc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf9f81f3b9697ca47f7674d85f37a8d80)
- [net_if_unset_promisc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9c8212c087883510050ac6a39ef0a7bf)
- [net_if_is_promisc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9f1a6eab849517734ec422deb0ba71f5)
- [net_if_are_pending_tx_packets](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3cddda628eca248246f9aa3b81938f95)
- [net_if_is_ethernet](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga703d9e3c128a3a3f0e452d789a4b7bf6)
- [net_if_get_first_ethernet](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga529067a284cac1187b336080e56129c8)
- [net_if_is_wifi](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa458b5f349c55007108b47b99f4954d5)
- [net_if_get_first_wifi](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga6e89bbafb6c0acdc6bf51078e2027236)
- [net_if_get_wifi_sta](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0fc3ba6172956f6847027e0bd3d367de)
- [net_if_get_wifi_sap](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaf830eab616191009d88f58b761694b49)
- [net_if_get_name](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5f653cd73c1ecd548a931eb7fbd170f7)
- [net_if_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga05dec64966fc39e3deb0679b9585688b)
- [net_if_get_by_name](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1774ac036032bb0dc2c662f6f4f66a7f)

<a id="header-details"></a>

---

[上一章](P002_zephyr__net__lwm2m.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__dt-bindings__dma__renesas_rza2m_dma.h_文件参考.md)
