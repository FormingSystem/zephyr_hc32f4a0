---
id: learning.zephyr-docs.api-sensor-network-buffer-reference.page-2
title: 网络接口抽象层（Network Interface abstraction layer）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_网络接口抽象层（Network Interface abstraction layer）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络接口抽象层（Network Interface abstraction layer）

<a id="details"></a>

网络接口抽象层（Network Interface Abstraction Layer）。引入版本（Since）：1.5。接口版本（Version）：1.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

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

## 2.2\_宏定义（Macros）

<a id="r_ga2b824eff0adada3eb7ff626a8d7c3538"></a>

```c
#define NET_IF_IPV6_DAD_NONCE_LEN 6U
```

相关声明：[NET_IF_IPV6_DAD_NONCE_LEN](#ga2b824eff0adada3eb7ff626a8d7c3538)。

RFC 7527 第 4 节定义的增强型重复地址检测（Enhanced DAD）的随机数（Nonce）载荷长度，单位为字节。

<a id="r_ga021e9877ee9532a899a298d6a2c7aeb2"></a>

```c
#define NET_IPV6_MAX_REACHABLE_TIME 3600000U
```

相关声明：[NET_IPV6_MAX_REACHABLE_TIME](#ga021e9877ee9532a899a298d6a2c7aeb2)。

IPv6 基础可达时间（Base Reachable Time）的最大值，单位为毫秒。

<a id="r_gae0fdb0b909e06ba7831e53700c32b84f"></a>

```c
#define NET_IF_DECLARE(dev_id, inst)
```

相关声明：[NET_IF_DECLARE](#gae0fdb0b909e06ba7831e53700c32b84f)。

网络接口（Network Interface）的前向声明（Forward Declaration）。

<a id="r_ga65e4d856b53096bf784a4d5a495ca507"></a>

```c
#define NET_IF_DT_DECLARE(node_id, instance)
```

相关声明：[NET_IF_DT_DECLARE](#ga65e4d856b53096bf784a4d5a495ca507)。

网络接口（Network Interface）的前向声明（Forward Declaration）。

<a id="r_ga421f0b8be2317c0865c50ca588f73509"></a>

```c
#define NET_IF_DT_INST_DECLARE(inst, ...)
```

相关声明：[NET_IF_DT_INST_DECLARE](#ga421f0b8be2317c0865c50ca588f73509)。

网络接口（Network Interface）的前向声明（Forward Declaration）。

<a id="r_gadd040e5cc26a96c3f66f37539178c3b6"></a>

```c
#define NET_IF_DT_GET(node_id, instance)
```

相关声明：[NET_IF_DT_GET](#gadd040e5cc26a96c3f66f37539178c3b6)。

获取通过 `NET_DEVICE_DT_DEFINE` 或 `NET_DEVICE_DT_ADD_IFACE` 创建的网络接口（Network Interface）。

<a id="r_ga48a80b52d8b5a16856c86041fc6492e6"></a>

```c
#define NET_IF_DT_INST_GET(inst, ...)
```

相关声明：[NET_IF_DT_INST_GET](#ga48a80b52d8b5a16856c86041fc6492e6)。

获取通过 `NET_DEVICE_DT_DEFINE` 或 `NET_DEVICE_DT_ADD_IFACE` 创建的网络接口（Network Interface）。

<a id="r_ga02971562c42494e2a5f71e1f8587e709"></a>

```c
#define NET_DEVICE_INIT(dev_id, name, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu)
```

相关声明：[NET_DEVICE_INIT](#ga02971562c42494e2a5f71e1f8587e709)。

创建网络接口（Network Interface），并将其绑定到网络设备（Network Device）。

<a id="r_gad8e37fc7a32339312dcfa614255988e8"></a>

```c
#define NET_DEVICE_DT_ADD_IFACE(node_id, l2, l2_ctx_type, mtu, instance)
```

相关声明：[NET_DEVICE_DT_ADD_IFACE](#gad8e37fc7a32339312dcfa614255988e8)。

向通过 `NET_DEVICE_DT_DEFINE` 创建的网络设备（Network Device）添加第二个或更多网络接口（Network Interfaces）。

<a id="r_ga00fe86342a77e32fe440e1bd97c51d51"></a>

```c
#define NET_DEVICE_DT_INST_ADD_IFACE(inst, ...)
```

相关声明：[NET_DEVICE_DT_INST_ADD_IFACE](#ga00fe86342a77e32fe440e1bd97c51d51)。

类似于 `NET_DEVICE_DT_ADD_IFACE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

<a id="r_gab1f762b01ae7bc37cd4a25724c123dda"></a>

```c
#define NET_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu)
```

相关声明：[NET_DEVICE_DT_DEFINE](#gab1f762b01ae7bc37cd4a25724c123dda)。

类似于 `NET_DEVICE_INIT`，但从设备树节点（Devicetree Node）获取元数据（Metadata）。

<a id="r_ga7edd8bc59444d92cad0371c36f9949b7"></a>

```c
#define NET_DEVICE_DT_INST_DEFINE(inst, ...)
```

相关声明：[NET_DEVICE_DT_INST_DEFINE](#ga7edd8bc59444d92cad0371c36f9949b7)。

类似于 `NET_DEVICE_DT_DEFINE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

<a id="r_gacc7edecdd9de9920cc155977d8fec2a2"></a>

```c
#define NET_DEVICE_INIT_INSTANCE(dev_id, name, instance, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu)
```

相关声明：[NET_DEVICE_INIT_INSTANCE](#gacc7edecdd9de9920cc155977d8fec2a2)。

创建多个网络接口（Network Interfaces），并将它们绑定到网络设备（Network Device）。

<a id="r_ga50702b043a0791e59e7d5679dda1d9e8"></a>

```c
#define NET_DEVICE_DT_DEFINE_INSTANCE(node_id, instance, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu)
```

相关声明：[NET_DEVICE_DT_DEFINE_INSTANCE](#ga50702b043a0791e59e7d5679dda1d9e8)。

类似于 `NET_DEVICE_OFFLOAD_INIT`，但从设备树（Devicetree）获取元数据（Metadata）。

<a id="r_gabe4b8589996a53cbc50b76c8ea15aa0c"></a>

```c
#define NET_DEVICE_DT_INST_DEFINE_INSTANCE(inst, ...)
```

相关声明：[NET_DEVICE_DT_INST_DEFINE_INSTANCE](#gabe4b8589996a53cbc50b76c8ea15aa0c)。

类似于 `NET_DEVICE_DT_DEFINE_INSTANCE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

<a id="r_ga255672607b7958db3f464d2a57a7e635"></a>

```c
#define NET_DEVICE_OFFLOAD_INIT(dev_id, name, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[NET_DEVICE_OFFLOAD_INIT](#ga255672607b7958db3f464d2a57a7e635)。

创建卸载型网络接口（Offloaded Network Interface），并将其绑定到网络设备（Network Device）。

<a id="r_gab2b287025e194dec1fab24e44d95362f"></a>

```c
#define NET_DEVICE_DT_OFFLOAD_DEFINE(node_id, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[NET_DEVICE_DT_OFFLOAD_DEFINE](#gab2b287025e194dec1fab24e44d95362f)。

类似于 `NET_DEVICE_OFFLOAD_INIT`，但从设备树节点（Devicetree Node）获取元数据（Metadata）。

<a id="r_ga1cab6943a28e3d3754e36623834b93fd"></a>

```c
#define NET_DEVICE_DT_INST_OFFLOAD_DEFINE(inst, ...)
```

相关声明：[NET_DEVICE_DT_INST_OFFLOAD_DEFINE](#ga1cab6943a28e3d3754e36623834b93fd)。

类似于 `NET_DEVICE_DT_OFFLOAD_DEFINE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

<a id="r_ga6c081875a6f5a848b3ad2fd220c63c3c"></a>

```c
#define NET_IFACE_COUNT(_dst)
```

相关声明：[NET_IFACE_COUNT](#ga6c081875a6f5a848b3ad2fd220c63c3c)。

统计网络接口（Network Interfaces）的数量。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.3\_类型定义（Typedefs）

<a id="r_gaef3dfe26195514aac625e9f22e399759"></a>

```c
typedef int(* net_socket_create_t) (int, int, int)
```

相关声明：[net_socket_create_t](#gaef3dfe26195514aac625e9f22e399759)。

用于创建卸载套接字（Offloaded Socket）的函数原型（Function Prototype）。

<a id="r_gab58d8561a4f21899e2db34043d346516"></a>

```c
typedef void(* net_if_ip_addr_cb_t) (struct net_if *iface, struct net_if_addr *addr, void *user_data)
```

相关声明：[net_if_ip_addr_cb_t](#gab58d8561a4f21899e2db34043d346516)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)。

遍历网络接口 IP 地址（Network Interface IP Addresses）时使用的回调。

<a id="r_ga726eed76563c223de8f611e2544febe9"></a>

```c
typedef void(* net_if_ip_maddr_cb_t) (struct net_if *iface, struct net_if_mcast_addr *maddr, void *user_data)
```

相关声明：[net_if_ip_maddr_cb_t](#ga726eed76563c223de8f611e2544febe9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

遍历网络接口多播 IP 地址（Network Interface Multicast IP Addresses）时使用的回调。

<a id="r_ga0d64291573740a67eae7ff3fcc0910c5"></a>

```c
typedef void(* net_if_mcast_callback_t) (struct net_if *iface, const struct net_addr *addr, bool is_joined)
```

相关声明：[net_if_mcast_callback_t](#ga0d64291573740a67eae7ff3fcc0910c5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

定义回调，在加入或退出 IPv6 或 IPv4 多播地址组（Multicast Address Group）时调用。

<a id="r_ga0f87d5753fcd7cce40ecd161e6c91078"></a>

```c
typedef void(* net_if_link_callback_t) (struct net_if *iface, struct net_linkaddr *dst, int status)
```

相关声明：[net_if_link_callback_t](#ga0f87d5753fcd7cce40ecd161e6c91078)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

定义网络数据包（Network Packet）发送之后调用的回调。

<a id="r_gac48ab8e6337e7cf387af9b293f254a80"></a>

```c
typedef void(* net_if_cb_t) (struct net_if *iface, void *user_data)
```

相关声明：[net_if_cb_t](#gac48ab8e6337e7cf387af9b293f254a80)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

遍历网络接口（Network Interfaces）时使用的回调。

<a id="r_ga656c2ba47d280aa1c47bc2d062debbfa"></a>

```c
typedef void(* net_if_timestamp_callback_t) (struct net_pkt *pkt)
```

相关声明：[net_if_timestamp_callback_t](#ga656c2ba47d280aa1c47bc2d062debbfa)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

定义网络数据包（Network Packet）被打上时间戳（Timestamped）之后调用的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.4\_枚举（Enumerations）

<a id="r_gae691e5537917ffce27ad0db82c730371"></a>

```c
enum net_if_flag { NET_IF_UP , NET_IF_POINTOPOINT , NET_IF_PROMISC , NET_IF_NO_AUTO_START , NET_IF_SUSPENDED , NET_IF_FORWARD_MULTICASTS , NET_IF_IPV4 , NET_IF_IPV6 , NET_IF_RUNNING , NET_IF_LOWER_UP , NET_IF_DORMANT , NET_IF_IPV6_NO_ND , NET_IF_IPV6_NO_MLD , NET_IF_NO_TX_LOCK }
```

相关声明：[net_if_flag](#gae691e5537917ffce27ad0db82c730371)、[NET_IF_UP](#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840)、[NET_IF_POINTOPOINT](#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009)、[NET_IF_PROMISC](#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141)、[NET_IF_NO_AUTO_START](#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05)、[NET_IF_SUSPENDED](#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0)、[NET_IF_FORWARD_MULTICASTS](#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac)、[NET_IF_IPV4](#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329)、[NET_IF_IPV6](#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6)、[NET_IF_RUNNING](#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a)、[NET_IF_LOWER_UP](#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d)、[NET_IF_DORMANT](#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d)、[NET_IF_IPV6_NO_ND](#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7)、[NET_IF_IPV6_NO_MLD](#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe)、[NET_IF_NO_TX_LOCK](#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9)。

网络接口标志（Network Interface Flags）。

<a id="r_gadfe9d90f24046cd9bd4bbee096e747b9"></a>

```c
enum net_if_oper_state { NET_IF_OPER_UNKNOWN , NET_IF_OPER_NOTPRESENT , NET_IF_OPER_DOWN , NET_IF_OPER_LOWERLAYERDOWN , NET_IF_OPER_TESTING , NET_IF_OPER_DORMANT , NET_IF_OPER_UP }
```

相关声明：[net_if_oper_state](#gadfe9d90f24046cd9bd4bbee096e747b9)、[NET_IF_OPER_UNKNOWN](#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58)、[NET_IF_OPER_NOTPRESENT](#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32)、[NET_IF_OPER_DOWN](#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367)、[NET_IF_OPER_LOWERLAYERDOWN](#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4)、[NET_IF_OPER_TESTING](#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f)、[NET_IF_OPER_DORMANT](#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d)、[NET_IF_OPER_UP](#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)。

网络接口运行状态（Network Interface Operational Status），参见 RFC 2863。

<a id="r_ga8db412ae79c64cafe81a66f5acb2f8e9"></a>

```c
enum net_if_checksum_type { NET_IF_CHECKSUM_IPV4_HEADER = NET_IF_CHECKSUM_IPV4_HEADER_BIT , NET_IF_CHECKSUM_IPV4_TCP , NET_IF_CHECKSUM_IPV4_UDP , NET_IF_CHECKSUM_IPV4_ICMP = NET_IF_CHECKSUM_IPV4_ICMP_BIT , NET_IF_CHECKSUM_IPV6_HEADER = NET_IF_CHECKSUM_IPV6_HEADER_BIT , NET_IF_CHECKSUM_IPV6_TCP , NET_IF_CHECKSUM_IPV6_UDP , NET_IF_CHECKSUM_IPV6_ICMP = NET_IF_CHECKSUM_IPV6_ICMP_BIT }
```

相关声明：[net_if_checksum_type](#ga8db412ae79c64cafe81a66f5acb2f8e9)、[NET_IF_CHECKSUM_IPV4_HEADER](#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30)、[NET_IF_CHECKSUM_IPV4_TCP](#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad)、[NET_IF_CHECKSUM_IPV4_UDP](#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3)、[NET_IF_CHECKSUM_IPV4_ICMP](#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1)、[NET_IF_CHECKSUM_IPV6_HEADER](#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b)、[NET_IF_CHECKSUM_IPV6_TCP](#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13)、[NET_IF_CHECKSUM_IPV6_UDP](#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660)、[NET_IF_CHECKSUM_IPV6_ICMP](#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3)。

要查询接口支持情况的校验和类型（Checksum Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.5\_函数（Functions）

<a id="r_ga52f9fca13e9f836799e0e40f581744d2"></a>

```c
static void net_if_flag_set (struct net_if *iface, enum net_if_flag value)
```

相关声明：[net_if_flag_set](#ga52f9fca13e9f836799e0e40f581744d2)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_flag](#gae691e5537917ffce27ad0db82c730371)。

设置网络接口标志（Network Interface Flags）中的一个值。

<a id="r_ga42e7482191a92007960601f8bb621dca"></a>

```c
static bool net_if_flag_test_and_set (struct net_if *iface, enum net_if_flag value)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_flag_test_and_set](#ga42e7482191a92007960601f8bb621dca)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_flag](#gae691e5537917ffce27ad0db82c730371)。

测试并设置网络接口标志（Network Interface Flags）中的一个值。

<a id="r_gaff751b6a92b0c608ecfc50e8c0587fd3"></a>

```c
static void net_if_flag_clear (struct net_if *iface, enum net_if_flag value)
```

相关声明：[net_if_flag_clear](#gaff751b6a92b0c608ecfc50e8c0587fd3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_flag](#gae691e5537917ffce27ad0db82c730371)。

清除网络接口标志（Network Interface Flags）中的一个值。

<a id="r_gab8f371c7f8890cf4728177f6595141d7"></a>

```c
static bool net_if_flag_test_and_clear (struct net_if *iface, enum net_if_flag value)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_flag_test_and_clear](#gab8f371c7f8890cf4728177f6595141d7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_flag](#gae691e5537917ffce27ad0db82c730371)。

测试并清除网络接口标志（Network Interface Flags）中的一个值。

<a id="r_gae1f373ddd61c18a81481d8ddcfb12543"></a>

```c
static bool net_if_flag_is_set (struct net_if *iface, enum net_if_flag value)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_flag_is_set](#gae1f373ddd61c18a81481d8ddcfb12543)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_flag](#gae691e5537917ffce27ad0db82c730371)。

检查网络接口标志（Network Interface Flags）中的一个值是否已设置。

<a id="r_ga1f1bf845e63cce02e2183889cc85d57e"></a>

```c
static enum net_if_oper_state net_if_oper_state_set (struct net_if *iface, enum net_if_oper_state oper_state)
```

相关声明：[net_if_oper_state](#gadfe9d90f24046cd9bd4bbee096e747b9)、[net_if_oper_state_set](#ga1f1bf845e63cce02e2183889cc85d57e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_oper_state](#gadfe9d90f24046cd9bd4bbee096e747b9)。

设置接口的运行状态（Operational State）。

<a id="r_gad9e957a4866b4566296ee39392fde0e4"></a>

```c
static enum net_if_oper_state net_if_oper_state (struct net_if *iface)
```

相关声明：[net_if_oper_state](#gadfe9d90f24046cd9bd4bbee096e747b9)、[net_if_oper_state](#gad9e957a4866b4566296ee39392fde0e4)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取接口的运行状态（Operational State）。

<a id="r_gabae216ba527bdfcd945ef19fb48e56be"></a>

```c
static int net_if_oper_state_change_time (struct net_if *iface, int64_t *change_time)
```

相关声明：[net_if_oper_state_change_time](#gabae216ba527bdfcd945ef19fb48e56be)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

获取接口运行状态的变化时间（Operational State Change Time）。

<a id="r_ga5d01d7fa6c7511d68933ad4cec032d8a"></a>

```c
enum net_verdict net_if_try_send_data (struct net_if *iface, struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_if_try_send_data](#ga5d01d7fa6c7511d68933ad4cec032d8a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

尝试通过网络接口（Net Interface）发送数据包（Packet）。

<a id="r_ga84a58403183b88c64fda59d5d2d903fc"></a>

```c
static enum net_verdict net_if_send_data (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_if_send_data](#ga84a58403183b88c64fda59d5d2d903fc)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

通过网络接口（Net Interface）发送数据包（Packet）。

<a id="r_gafa451f6118529d1d084704d00b2aae20"></a>

```c
static const struct net_l2 * net_if_l2 (struct net_if *iface)
```

相关声明：[net_l2](../network_core_model_reference/P103_net_l2_结构体.md)、[net_if_l2](#gafa451f6118529d1d084704d00b2aae20)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取指向接口链路层（Interface L2）的指针。

<a id="r_ga72ed21ca0cb220199f5a2070137c7fef"></a>

```c
enum net_verdict net_if_recv_data (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)、[net_if_recv_data](#ga72ed21ca0cb220199f5a2070137c7fef)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

通过网络接口（Net Interface）输入数据包（Packet）。

<a id="r_ga3cad2d51fc9cc225619585e06e252db0"></a>

```c
static void * net_if_l2_data (struct net_if *iface)
```

相关声明：[net_if_l2_data](#ga3cad2d51fc9cc225619585e06e252db0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取指向接口链路层私有数据（Interface L2 Private Data）的指针。

<a id="r_gaeb8c703f273bc07ae9bb7a0d8bfe6f3d"></a>

```c
static const struct device * net_if_get_device (struct net_if *iface)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[net_if_get_device](#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取网络接口（Network Interface）对应的设备（Device）。

<a id="r_ga3617cd1f712b8a85fdd7f1425254ae5d"></a>

```c
void net_if_try_queue_tx (struct net_if *iface, struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_if_try_queue_tx](#ga3617cd1f712b8a85fdd7f1425254ae5d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

尝试将数据包（Packet）加入网络接口发送队列（TX Queue）。

<a id="r_ga2ac749d465ef7f0f64f294a30310457e"></a>

```c
static void net_if_queue_tx (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_if_queue_tx](#ga2ac749d465ef7f0f64f294a30310457e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

将数据包（Packet）加入网络接口发送队列（TX Queue）。

<a id="r_ga6bfa5f84a2127bbad27a0a3b319526a1"></a>

```c
static bool net_if_is_ip_offloaded (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_ip_offloaded](#ga6bfa5f84a2127bbad27a0a3b319526a1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回 IP 卸载状态（IP Offload Status）。

<a id="r_gaecedc93a6dab2c57fe686718ea4d78af"></a>

```c
bool net_if_is_offloaded (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_offloaded](#gaecedc93a6dab2c57fe686718ea4d78af)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回给定网络接口（Network Interface）的卸载状态（Offload Status）。

<a id="r_ga520939e94620ca75475a71f153df6d4a"></a>

```c
static struct net_offload * net_if_offload (struct net_if *iface)
```

相关声明：[net_if_offload](#ga520939e94620ca75475a71f153df6d4a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回 IP 卸载插件（IP Offload Plugin）。

<a id="r_gaf2d323c1504125fbfde5da9ada8c5657"></a>

```c
static void net_if_offload_set (struct net_if *iface, struct net_offload *offload)
```

相关声明：[net_if_offload_set](#gaf2d323c1504125fbfde5da9ada8c5657)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置 IP 卸载插件（IP Offload Plugin）。

<a id="r_gaf308baf2241fa455b50b439b7fab3f1e"></a>

```c
static bool net_if_is_socket_offloaded (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_socket_offloaded](#gaf308baf2241fa455b50b439b7fab3f1e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回套接字卸载状态（Socket Offload Status）。

<a id="r_ga9db52875580115c743b1f35cd6c46796"></a>

```c
static void net_if_socket_offload_set (struct net_if *iface, net_socket_create_t socket_offload)
```

相关声明：[net_if_socket_offload_set](#ga9db52875580115c743b1f35cd6c46796)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_socket_create_t](#gaef3dfe26195514aac625e9f22e399759)。

设置创建卸载套接字（Offloaded Socket）的函数。

<a id="r_gafb2bbaec96c4759d920b2866c0b3ef3a"></a>

```c
static net_socket_create_t net_if_socket_offload (struct net_if *iface)
```

相关声明：[net_socket_create_t](#gaef3dfe26195514aac625e9f22e399759)、[net_if_socket_offload](#gafb2bbaec96c4759d920b2866c0b3ef3a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回创建卸载套接字（Offloaded Socket）的函数。

<a id="r_ga467186e964bf721e14fed38392f21872"></a>

```c
static struct net_linkaddr * net_if_get_link_addr (struct net_if *iface)
```

相关声明：[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)、[net_if_get_link_addr](#ga467186e964bf721e14fed38392f21872)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取网络接口的链路地址（Link Address）。

<a id="r_gae271e0e4dcb031a83d9908e597a45048"></a>

```c
static struct net_if_config * net_if_get_config (struct net_if *iface)
```

相关声明：[net_if_config](../network_core_model_reference/P082_net_if_config_结构体.md)、[net_if_get_config](#gae271e0e4dcb031a83d9908e597a45048)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回此网络接口（Network Interface）的网络配置（Network Configuration）。

<a id="r_ga9655c010ccbf989e9328271f5dbcc685"></a>

```c
static void net_if_start_dad (struct net_if *iface)
```

相关声明：[net_if_start_dad](#ga9655c010ccbf989e9328271f5dbcc685)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启动重复地址检测过程（Duplicate Address Detection Procedure）。

<a id="r_gab9bdb7f8a9eeed4d9b70965b8af82cb7"></a>

```c
void net_if_start_rs (struct net_if *iface)
```

相关声明：[net_if_start_rs](#gab9bdb7f8a9eeed4d9b70965b8af82cb7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启动邻居发现（Neighbor Discovery），并发送路由器请求消息（Router Solicitation Message）。

<a id="r_gab0195bb2151a1ba722a0b11d81066988"></a>

```c
static void net_if_stop_rs (struct net_if *iface)
```

相关声明：[net_if_stop_rs](#gab0195bb2151a1ba722a0b11d81066988)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

停止邻居发现（Neighbor Discovery）。

<a id="r_ga655599b1432463455610cff768997e2b"></a>

```c
static void net_if_nbr_reachability_hint (struct net_if *iface, const struct net_in6_addr *ipv6_addr)
```

相关声明：[net_if_nbr_reachability_hint](#ga655599b1432463455610cff768997e2b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

为 IPv6 邻居发现（Neighbor Discovery）提供可达性提示（Reachability Hint）。

<a id="r_gaaa6c3d31d3a40cab6cf9e4f4af959b89"></a>

```c
static void net_if_ipv6_nbr_flush (struct net_if *iface)
```

相关声明：[net_if_ipv6_nbr_flush](#gaaa6c3d31d3a40cab6cf9e4f4af959b89)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

清空网络接口的 IPv6 邻居缓存（Neighbor Cache）。

<a id="r_gac6bc061b5b0facc5023da2a835fb9bb3"></a>

```c
static bool net_if_ipv6_nbr_rm (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_nbr_rm](#gac6bc061b5b0facc5023da2a835fb9bb3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

从 IPv6 邻居缓存（Neighbor Cache）中移除一个邻居（Neighbor）。

<a id="r_ga3863e011f89dff02c3df3ca4a88680e9"></a>

```c
static int net_if_set_link_addr (struct net_if *iface, const uint8_t *addr, uint8_t len, enum net_link_type type)
```

相关声明：[net_if_set_link_addr](#ga3863e011f89dff02c3df3ca4a88680e9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_link_type](../api_input_runtime_topic_reference/P015_网络链路地址库（Network Link Address Library）.md#ga1312c2322bc4a4f1c3b76d6466806b24)。

设置网络接口的链路地址（Link Address）。

<a id="r_gacddc98531c5748db5a34f5c3a3e96e86"></a>

```c
static uint16_t net_if_get_mtu (struct net_if *iface)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_if_get_mtu](#gacddc98531c5748db5a34f5c3a3e96e86)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取网络接口的最大传输单元（MTU）。

<a id="r_ga76b140c6fc39b94ff4102e08e3a58e81"></a>

```c
static void net_if_set_mtu (struct net_if *iface, uint16_t mtu)
```

相关声明：[net_if_set_mtu](#ga76b140c6fc39b94ff4102e08e3a58e81)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置网络接口的最大传输单元（MTU）。

<a id="r_gae66f6e7bd31545e6161fcd4600fe5842"></a>

```c
static void net_if_addr_set_lf (struct net_if_addr *ifaddr, bool is_infinite)
```

相关声明：[net_if_addr_set_lf](#gae66f6e7bd31545e6161fcd4600fe5842)、[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置网络接口地址的无限有效状态（Infinite Status）。

<a id="r_ga1b058361dc9bcac7d842bb49846a0c79"></a>

```c
struct net_if * net_if_get_by_link_addr (struct net_linkaddr *ll_addr)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_by_link_addr](#ga1b058361dc9bcac7d842bb49846a0c79)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

根据链路层地址（Link Layer Address）获取接口（Interface）。

<a id="r_gadbb8be32caa896bdcdeee19425134827"></a>

```c
struct net_if * net_if_lookup_by_dev (const struct device *dev)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_lookup_by_dev](#gadbb8be32caa896bdcdeee19425134827)、[device](../device_reference/P002_设备对象结构.md)。

根据关联的设备（Device）查找接口（Interface）。

<a id="r_gadc87242eb7205362a308b3c4437bf76d"></a>

```c
void net_if_router_rm (struct net_if_router *router)
```

相关声明：[net_if_router_rm](#gadc87242eb7205362a308b3c4437bf76d)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)。

从系统中移除路由器（Router）。

<a id="r_ga0a1f27ec893e1af3c97f130be4616589"></a>

```c
void net_if_set_default (struct net_if *iface)
```

相关声明：[net_if_set_default](#ga0a1f27ec893e1af3c97f130be4616589)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置默认网络接口（Default Network Interface）。

<a id="r_ga55214771e462cbd4930ffa738813cb87"></a>

```c
struct net_if * net_if_get_default (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_default](#ga55214771e462cbd4930ffa738813cb87)。

获取默认网络接口（Default Network Interface）。

<a id="r_ga762337e8b66874a0fbf59bdbeba173f5"></a>

```c
struct net_if * net_if_get_first_by_type (const struct net_l2 *l2)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_first_by_type](#ga762337e8b66874a0fbf59bdbeba173f5)、[net_l2](../network_core_model_reference/P103_net_l2_结构体.md)。

根据类型（Type）获取第一个网络接口（Network Interface）。

<a id="r_ga03d8c6aebb1412382a9eec636c227238"></a>

```c
struct net_if * net_if_get_first_up (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_first_up](#ga03d8c6aebb1412382a9eec636c227238)。

获取第一个处于启用状态（Up）的网络接口（Network Interface）。

<a id="r_ga56c9aef19bc9827d9ec96c00e10840fa"></a>

```c
int net_if_config_ipv6_get (struct net_if *iface, struct net_if_ipv6 **ipv6)
```

相关声明：[net_if_config_ipv6_get](#ga56c9aef19bc9827d9ec96c00e10840fa)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv6](../network_core_model_reference/P086_net_if_ipv6_结构体.md)。

分配网络接口的 IPv6 配置（IPv6 Configuration）。

<a id="r_ga8af1400b354c42a64795cdb1a600ddd6"></a>

```c
int net_if_config_ipv6_put (struct net_if *iface)
```

相关声明：[net_if_config_ipv6_put](#ga8af1400b354c42a64795cdb1a600ddd6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

释放网络接口的 IPv6 配置（IPv6 Configuration）。

<a id="r_ga4314c59af790e537e384e969c58fab9d"></a>

```c
struct net_if_addr * net_if_ipv6_addr_lookup (const struct net_in6_addr *addr, struct net_if **iface)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv6_addr_lookup](#ga4314c59af790e537e384e969c58fab9d)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查此 IPv6 地址是否属于某个接口（Interface）。

<a id="r_gae2935f8b0ad41879b12a491bc260b236"></a>

```c
struct net_if_addr * net_if_ipv6_addr_lookup_by_iface (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv6_addr_lookup_by_iface](#gae2935f8b0ad41879b12a491bc260b236)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查此 IPv6 地址是否属于这个特定接口（Specific Interface）。

<a id="r_gaaba6b0ba57a19c3d24628e8498ef421d"></a>

```c
int net_if_ipv6_addr_lookup_by_index (const struct net_in6_addr *addr)
```

相关声明：[net_if_ipv6_addr_lookup_by_index](#gaaba6b0ba57a19c3d24628e8498ef421d)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查此 IPv6 地址是否属于某个接口索引（Interface Index）对应的接口。

<a id="r_ga3b651babfb5d1dd9f8d266d2aa1cf1b8"></a>

```c
struct net_if_addr * net_if_ipv6_addr_add (struct net_if *iface, const struct net_in6_addr *addr, enum net_addr_type addr_type, uint32_t vlifetime)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv6_addr_add](#ga3b651babfb5d1dd9f8d266d2aa1cf1b8)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_addr_type](../api_network_work_driver_reference/P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#gafecee2d4a331dc85ad962b81a6303e41)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向接口（Interface）添加 IPv6 地址。

<a id="r_gad68f25bd25b198bc4280d334f71495d3"></a>

```c
bool net_if_ipv6_addr_add_by_index (int index, const struct net_in6_addr *addr, enum net_addr_type addr_type, uint32_t vlifetime)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_addr_add_by_index](#gad68f25bd25b198bc4280d334f71495d3)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_addr_type](../api_network_work_driver_reference/P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#gafecee2d4a331dc85ad962b81a6303e41)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过索引（Index）向接口添加 IPv6 地址。

<a id="r_gaef8a6752a201f81636c4ffc1ebba4a25"></a>

```c
void net_if_ipv6_addr_update_lifetime (struct net_if_addr *ifaddr, uint32_t vlifetime)
```

相关声明：[net_if_ipv6_addr_update_lifetime](#gaef8a6752a201f81636c4ffc1ebba4a25)、[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更新 IPv6 地址的有效生命周期（Valid Lifetime）。

<a id="r_gad0e9473f494d154c4cd89e3e67a13232"></a>

```c
bool net_if_ipv6_addr_rm (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_addr_rm](#gad0e9473f494d154c4cd89e3e67a13232)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

从接口（Interface）移除 IPv6 地址。

<a id="r_gadc08ec8c23d2ee138eb3a05cdfe00701"></a>

```c
bool net_if_ipv6_addr_rm_by_index (int index, const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_addr_rm_by_index](#gadc08ec8c23d2ee138eb3a05cdfe00701)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

通过索引（Index）从接口移除 IPv6 地址。

<a id="r_ga5ac646ad7fda0fa48e78c15b4ca52d50"></a>

```c
void net_if_ipv6_addr_foreach (struct net_if *iface, net_if_ip_addr_cb_t cb, void *user_data)
```

相关声明：[net_if_ipv6_addr_foreach](#ga5ac646ad7fda0fa48e78c15b4ca52d50)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ip_addr_cb_t](#gab58d8561a4f21899e2db34043d346516)。

遍历网络接口的全部 IPv6 地址，并对每个正在使用的地址调用回调（Callback）。

<a id="r_ga1608a77ffca421769bae381a12e179ce"></a>

```c
struct net_if_mcast_addr * net_if_ipv6_maddr_add (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)、[net_if_ipv6_maddr_add](#ga1608a77ffca421769bae381a12e179ce)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

向接口（Interface）添加 IPv6 多播地址（Multicast Address）。

<a id="r_ga6c80fd9c864cb54902d52adcb5d8d639"></a>

```c
bool net_if_ipv6_maddr_rm (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_maddr_rm](#ga6c80fd9c864cb54902d52adcb5d8d639)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

从接口（Interface）移除 IPv6 多播地址（Multicast Address）。

<a id="r_gab677496fb2e27be2df299a346e9c7132"></a>

```c
void net_if_ipv6_maddr_foreach (struct net_if *iface, net_if_ip_maddr_cb_t cb, void *user_data)
```

相关声明：[net_if_ipv6_maddr_foreach](#gab677496fb2e27be2df299a346e9c7132)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ip_maddr_cb_t](#ga726eed76563c223de8f611e2544febe9)。

遍历网络接口的全部 IPv6 多播地址（Multicast Addresses），并对每个正在使用的地址调用回调。

<a id="r_gad520342d393f523c56a98fa618876b54"></a>

```c
struct net_if_mcast_addr * net_if_ipv6_maddr_lookup (const struct net_in6_addr *addr, struct net_if **iface)
```

相关声明：[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)、[net_if_ipv6_maddr_lookup](#gad520342d393f523c56a98fa618876b54)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查此 IPv6 多播地址（Multicast Address）是否属于指定接口或某个接口（Interface）。

<a id="r_ga8fdd0665ed76db6055777e395ca60255"></a>

```c
void net_if_mcast_mon_register (struct net_if_mcast_monitor *mon, struct net_if *iface, net_if_mcast_callback_t cb)
```

相关声明：[net_if_mcast_mon_register](#ga8fdd0665ed76db6055777e395ca60255)、[net_if_mcast_monitor](../network_core_model_reference/P090_net_if_mcast_monitor_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_callback_t](#ga0d64291573740a67eae7ff3fcc0910c5)。

注册多播监视器（Multicast Monitor）。

<a id="r_gad323732fe3d178a5dfdf0900e5cb5683"></a>

```c
void net_if_mcast_mon_unregister (struct net_if_mcast_monitor *mon)
```

相关声明：[net_if_mcast_mon_unregister](#gad323732fe3d178a5dfdf0900e5cb5683)、[net_if_mcast_monitor](../network_core_model_reference/P090_net_if_mcast_monitor_结构体.md)。

注销多播监视器（Multicast Monitor）。

<a id="r_ga372ef131263269cd65586d87997df745"></a>

```c
void net_if_mcast_monitor (struct net_if *iface, const struct net_addr *addr, bool is_joined)
```

相关声明：[net_if_mcast_monitor](#ga372ef131263269cd65586d87997df745)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

调用已注册的多播监视器（Multicast Monitors）。

<a id="r_ga49dbc954015307222f176f4149829b76"></a>

```c
void net_if_ipv6_maddr_join (struct net_if *iface, struct net_if_mcast_addr *addr)
```

相关声明：[net_if_ipv6_maddr_join](#ga49dbc954015307222f176f4149829b76)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

将给定多播地址（Multicast Address）标记为已加入（Joined）。

<a id="r_gabe2c16a378a35a22d008bff9142e5449"></a>

```c
static bool net_if_ipv6_maddr_is_joined (struct net_if_mcast_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_maddr_is_joined](#gabe2c16a378a35a22d008bff9142e5449)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

检查是否已加入（Joined）给定多播地址（Multicast Address）。

<a id="r_gad24d5537d52de9781a7a6a55ceedd92b"></a>

```c
void net_if_ipv6_maddr_leave (struct net_if *iface, struct net_if_mcast_addr *addr)
```

相关声明：[net_if_ipv6_maddr_leave](#gad24d5537d52de9781a7a6a55ceedd92b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

将给定多播地址（Multicast Address）标记为已退出（Left）。

<a id="r_ga9c10341ab913f0b609c2724354ec587a"></a>

```c
struct net_if_ipv6_prefix * net_if_ipv6_prefix_get (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)、[net_if_ipv6_prefix_get](#ga9c10341ab913f0b609c2724354ec587a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

返回与此 IPv6 地址对应的前缀（Prefix）。

<a id="r_ga99b22d24fef63bd1681396410b930008"></a>

```c
struct net_if_ipv6_prefix * net_if_ipv6_prefix_lookup (struct net_if *iface, const struct net_in6_addr *addr, uint8_t len)
```

相关声明：[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)、[net_if_ipv6_prefix_lookup](#ga99b22d24fef63bd1681396410b930008)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查此 IPv6 前缀（Prefix）是否属于该接口。

<a id="r_ga2616868a6d51cbf1d35c6920e258d412"></a>

```c
struct net_if_ipv6_prefix * net_if_ipv6_prefix_add (struct net_if *iface, const struct net_in6_addr *prefix, uint8_t len, uint32_t lifetime)
```

相关声明：[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)、[net_if_ipv6_prefix_add](#ga2616868a6d51cbf1d35c6920e258d412)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向网络接口（Network Interface）添加 IPv6 前缀（Prefix）。

<a id="r_ga4b8668b32a14996c68d10ec989c1abb3"></a>

```c
bool net_if_ipv6_prefix_rm (struct net_if *iface, const struct net_in6_addr *addr, uint8_t len)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_prefix_rm](#ga4b8668b32a14996c68d10ec989c1abb3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从接口（Interface）移除 IPv6 前缀（Prefix）。

<a id="r_gaa3c711e814fb6a4e552b4ef723d0baa0"></a>

```c
static void net_if_ipv6_prefix_set_lf (struct net_if_ipv6_prefix *prefix, bool is_infinite)
```

相关声明：[net_if_ipv6_prefix_set_lf](#gaa3c711e814fb6a4e552b4ef723d0baa0)、[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置前缀（Prefix）的无限有效状态（Infinite Status）。

<a id="r_ga68cffe343c518bad7f7f152e30f7f9ee"></a>

```c
void net_if_ipv6_prefix_set_timer (struct net_if_ipv6_prefix *prefix, uint32_t lifetime)
```

相关声明：[net_if_ipv6_prefix_set_timer](#ga68cffe343c518bad7f7f152e30f7f9ee)、[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置前缀生命周期定时器（Prefix Lifetime Timer）。

<a id="r_ga2d68cb6dcfcffd3f87bbfb3dfce791ff"></a>

```c
void net_if_ipv6_prefix_unset_timer (struct net_if_ipv6_prefix *prefix)
```

相关声明：[net_if_ipv6_prefix_unset_timer](#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)、[net_if_ipv6_prefix](../network_core_model_reference/P087_net_if_ipv6_prefix_结构体.md)。

取消前缀生命周期定时器（Prefix Lifetime Timer）。

<a id="r_ga9ff61003d36ee19af27a9b1b24b22170"></a>

```c
int net_if_ipv6_prefix_set_advertise (struct net_if *iface, const struct net_in6_addr *prefix, uint8_t len, bool advertise)
```

相关声明：[net_if_ipv6_prefix_set_advertise](#ga9ff61003d36ee19af27a9b1b24b22170)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

标记或取消标记一个 IPv6 前缀（Prefix），决定是否在该接口发送的路由器通告（Router Advertisements）中通告此前缀。

<a id="r_ga1c062890f66b97dbb723339fede121ff"></a>

```c
int net_if_ipv6_router_start (struct net_if *iface)
```

相关声明：[net_if_ipv6_router_start](#ga1c062890f66b97dbb723339fede121ff)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启用接口的 IPv6 路由器角色（Router Role）。

<a id="r_gaa56d3dbc96301e6fa70ee61b08c29841"></a>

```c
int net_if_ipv6_router_stop (struct net_if *iface)
```

相关声明：[net_if_ipv6_router_stop](#gaa56d3dbc96301e6fa70ee61b08c29841)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

禁用接口的 IPv6 路由器角色（Router Role）。

<a id="r_ga53cc6d8d43f3b3ef7c275dff69b4de8d"></a>

```c
bool net_if_ipv6_addr_onlink (struct net_if **iface, const struct net_in6_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_addr_onlink](#ga53cc6d8d43f3b3ef7c275dff69b4de8d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查此 IPv6 地址是否属于本网络接口的子网（Subnet）。

<a id="r_ga17d846ec0cbc1e67fd4a2bc1179b7c45"></a>

```c
static struct net_in6_addr * net_if_router_ipv6 (struct net_if_router *router)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_router_ipv6](#ga17d846ec0cbc1e67fd4a2bc1179b7c45)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)。

获取给定路由器（Router）的 IPv6 地址。

<a id="r_gac68a72e70b5335773964dbfc0319eee5"></a>

```c
struct net_if_router * net_if_ipv6_router_lookup (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv6_router_lookup](#gac68a72e70b5335773964dbfc0319eee5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

检查该 IPv6 地址是否为系统中已配置路由器（Router）的地址之一。

<a id="r_gabfabdb7afa073b54f67d67320da3983c"></a>

```c
struct net_if_router * net_if_ipv6_router_find_default (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv6_router_find_default](#gabfabdb7afa073b54f67d67320da3983c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

查找用于此 IPv6 地址的默认路由器（Default Router）。

<a id="r_gaadba4957802dc376ef011590c91c6af6"></a>

```c
void net_if_ipv6_router_update_lifetime (struct net_if_router *router, uint16_t lifetime)
```

相关声明：[net_if_ipv6_router_update_lifetime](#gaadba4957802dc376ef011590c91c6af6)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

更新路由器（Router）的有效生命周期（Valid Lifetime）。

<a id="r_ga8d80080463bcb9035e06e0ac35090780"></a>

```c
struct net_if_router * net_if_ipv6_router_add (struct net_if *iface, const struct net_in6_addr *addr, bool is_default, uint16_t router_lifetime)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv6_router_add](#ga8d80080463bcb9035e06e0ac35090780)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向系统添加 IPv6 路由器（Router）。

<a id="r_ga1d108aa0b54c072e0aa9d0c049f02807"></a>

```c
bool net_if_ipv6_router_rm (struct net_if_router *router)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv6_router_rm](#ga1d108aa0b54c072e0aa9d0c049f02807)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)。

从系统移除 IPv6 路由器（Router）。

<a id="r_ga66d0a9a8eef095f6d4d44f35dd67f2b6"></a>

```c
static uint8_t net_if_ipv6_get_hop_limit (struct net_if *iface)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_if_ipv6_get_hop_limit](#ga66d0a9a8eef095f6d4d44f35dd67f2b6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv6 跳数限制（Hop Limit）。

<a id="r_ga5bf726bb5c1d232103ec6841e7d0cd8c"></a>

```c
static void net_if_ipv6_set_hop_limit (struct net_if *iface, uint8_t hop_limit)
```

相关声明：[net_if_ipv6_set_hop_limit](#ga5bf726bb5c1d232103ec6841e7d0cd8c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置给定接口的默认 IPv6 跳数限制（Hop Limit）。

<a id="r_ga56e7086633bcf4537f54c7ca70e6c900"></a>

```c
static uint8_t net_if_ipv6_get_mcast_hop_limit (struct net_if *iface)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_if_ipv6_get_mcast_hop_limit](#ga56e7086633bcf4537f54c7ca70e6c900)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv6 多播跳数限制（Multicast Hop Limit）。

<a id="r_gaf56a433679ea9701cf8baa3208f8ccc3"></a>

```c
static void net_if_ipv6_set_mcast_hop_limit (struct net_if *iface, uint8_t hop_limit)
```

相关声明：[net_if_ipv6_set_mcast_hop_limit](#gaf56a433679ea9701cf8baa3208f8ccc3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置给定接口的默认 IPv6 多播跳数限制（Multicast Hop Limit）。

<a id="r_gab3939d735b660f8f02124df656ceba2c"></a>

```c
static void net_if_ipv6_set_base_reachable_time (struct net_if *iface, uint32_t reachable_time)
```

相关声明：[net_if_ipv6_set_base_reachable_time](#gab3939d735b660f8f02124df656ceba2c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置给定接口的 IPv6 可达时间（Reachable Time）。

<a id="r_ga71eb0b9842db6db6930c3567e94d4bd6"></a>

```c
static uint32_t net_if_ipv6_get_base_reachable_time (struct net_if *iface)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_if_ipv6_get_base_reachable_time](#ga71eb0b9842db6db6930c3567e94d4bd6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取给定接口的 IPv6 基础可达时间（Base Reachable Time）。

<a id="r_ga9dd1f91edbb519a6a079f363c33efacf"></a>

```c
static uint32_t net_if_ipv6_get_reachable_time (struct net_if *iface)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_if_ipv6_get_reachable_time](#ga9dd1f91edbb519a6a079f363c33efacf)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv6 可达超时（Reachable Timeout）。

<a id="r_gab1861b5cefa73b4eefbb447cb1438cdc"></a>

```c
uint32_t net_if_ipv6_calc_reachable_time (struct net_if_ipv6 *ipv6)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_if_ipv6_calc_reachable_time](#gab1861b5cefa73b4eefbb447cb1438cdc)、[net_if_ipv6](../network_core_model_reference/P086_net_if_ipv6_结构体.md)。

为 IPv6 可达时间（Reachable Time）计算下一个可达时间值。

<a id="r_ga8328266b870fd200660cb2becaab3de4"></a>

```c
static void net_if_ipv6_set_reachable_time (struct net_if_ipv6 *ipv6)
```

相关声明：[net_if_ipv6_set_reachable_time](#ga8328266b870fd200660cb2becaab3de4)、[net_if_ipv6](../network_core_model_reference/P086_net_if_ipv6_结构体.md)。

设置给定接口的 IPv6 可达时间（Reachable Time）。

<a id="r_gad74566e5a34f447d2ac63d2c0e82eeff"></a>

```c
static void net_if_ipv6_set_retrans_timer (struct net_if *iface, uint32_t retrans_timer)
```

相关声明：[net_if_ipv6_set_retrans_timer](#gad74566e5a34f447d2ac63d2c0e82eeff)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置给定接口的 IPv6 重传定时器（Retransmit Timer）。

<a id="r_gaddbf5a6ba412e6bdb7e31568fe827bd0"></a>

```c
static uint32_t net_if_ipv6_get_retrans_timer (struct net_if *iface)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_if_ipv6_get_retrans_timer](#gaddbf5a6ba412e6bdb7e31568fe827bd0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv6 重传定时器（Retransmit Timer）。

<a id="r_ga5f8fc8725d3050a0e8fb0c3c75791c7c"></a>

```c
static const struct net_in6_addr * net_if_ipv6_select_src_addr (struct net_if *iface, const struct net_in6_addr *dst)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_ipv6_select_src_addr](#ga5f8fc8725d3050a0e8fb0c3c75791c7c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

获取向目的地发送网络数据时应使用的 IPv6 源地址（Source Address）。

<a id="r_ga55df4f4967efb4840dbee7a4078a237b"></a>

```c
static const struct net_in6_addr * net_if_ipv6_select_src_addr_hint (struct net_if *iface, const struct net_in6_addr *dst, int flags)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_ipv6_select_src_addr_hint](#ga55df4f4967efb4840dbee7a4078a237b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

获取向目的地发送网络数据时应使用的 IPv6 源地址（Source Address）。

<a id="r_ga367c74aad10b58074e5e1e517d6be379"></a>

```c
static struct net_if * net_if_ipv6_select_src_iface (const struct net_in6_addr *dst)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv6_select_src_iface](#ga367c74aad10b58074e5e1e517d6be379)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

获取向目的地发送 IPv6 网络数据时应使用的网络接口（Network Interface）。

<a id="r_ga8c3fe8f29294c8bb9561d22625cf726c"></a>

```c
static struct net_if * net_if_ipv6_select_src_iface_addr (const struct net_in6_addr *dst, const struct net_in6_addr **src_addr)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv6_select_src_iface_addr](#ga8c3fe8f29294c8bb9561d22625cf726c)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

获取向目的地发送 IPv6 网络数据时应使用的网络接口（Network Interface）。

<a id="r_ga76ebc895fb5959f7f4a2884024bb4963"></a>

```c
struct net_in6_addr * net_if_ipv6_get_ll (struct net_if *iface, enum net_addr_state addr_state)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_ipv6_get_ll](#ga76ebc895fb5959f7f4a2884024bb4963)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_addr_state](../api_network_work_driver_reference/P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga32e58fc83532ef57eeb6ff952f17288d)。

获取处于给定状态的 IPv6 链路本地地址（Link Local Address）。

<a id="r_ga89ea06beb89db41d064b23186c92a567"></a>

```c
struct net_in6_addr * net_if_ipv6_get_ll_addr (enum net_addr_state state, struct net_if **iface)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_ipv6_get_ll_addr](#ga89ea06beb89db41d064b23186c92a567)、[net_addr_state](../api_network_work_driver_reference/P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga32e58fc83532ef57eeb6ff952f17288d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

从第一个具有匹配给定状态的链路本地地址（Link Local Address）的接口中，返回该链路本地 IPv6 地址。

<a id="r_ga8f37df9b421963d33a0838fe1fedde2a"></a>

```c
void net_if_ipv6_dad_failed (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_if_ipv6_dad_failed](#ga8f37df9b421963d33a0838fe1fedde2a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

如果发现本机 IPv6 地址已被使用，则停止 IPv6 重复地址检测（Duplicate Address Detection，DAD）过程。

<a id="r_gaf466f15f578d0ab287d8d3a258a64bb3"></a>

```c
struct net_in6_addr * net_if_ipv6_get_global_addr (enum net_addr_state state, struct net_if **iface)
```

相关声明：[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_if_ipv6_get_global_addr](#gaf466f15f578d0ab287d8d3a258a64bb3)、[net_addr_state](../api_network_work_driver_reference/P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga32e58fc83532ef57eeb6ff952f17288d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

从第一个具有匹配给定状态的全局 IPv6 地址（Global IPv6 Address）的接口中，返回该全局地址。

<a id="r_ga3390e248249b28f2c80e2ca0bc79d236"></a>

```c
int net_if_config_ipv4_get (struct net_if *iface, struct net_if_ipv4 **ipv4)
```

相关声明：[net_if_config_ipv4_get](#ga3390e248249b28f2c80e2ca0bc79d236)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv4](../network_core_model_reference/P085_net_if_ipv4_结构体.md)。

分配网络接口的 IPv4 配置（IPv4 Configuration）。

<a id="r_ga88c13a45617480a665c7f9f589ec8e10"></a>

```c
int net_if_config_ipv4_put (struct net_if *iface)
```

相关声明：[net_if_config_ipv4_put](#ga88c13a45617480a665c7f9f589ec8e10)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

释放网络接口的 IPv4 配置（IPv4 Configuration）。

<a id="r_ga7e1fd28dbcf1164d056296b4df782e64"></a>

```c
uint8_t net_if_ipv4_get_ttl (struct net_if *iface)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_if_ipv4_get_ttl](#ga7e1fd28dbcf1164d056296b4df782e64)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv4 生存时间（Time-to-live）值。

<a id="r_ga5544374d7ebea26a239d561083f0203d"></a>

```c
void net_if_ipv4_set_ttl (struct net_if *iface, uint8_t ttl)
```

相关声明：[net_if_ipv4_set_ttl](#ga5544374d7ebea26a239d561083f0203d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置给定接口的 IPv4 生存时间（Time-to-live）值。

<a id="r_ga71acb65b1988aab8cca9c9604c86231e"></a>

```c
uint8_t net_if_ipv4_get_mcast_ttl (struct net_if *iface)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_if_ipv4_get_mcast_ttl](#ga71acb65b1988aab8cca9c9604c86231e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取为给定接口指定的 IPv4 多播生存时间（Multicast Time-to-live）值。

<a id="r_ga9452fef4f1309fb1a53a6a8b4f222377"></a>

```c
void net_if_ipv4_set_mcast_ttl (struct net_if *iface, uint8_t ttl)
```

相关声明：[net_if_ipv4_set_mcast_ttl](#ga9452fef4f1309fb1a53a6a8b4f222377)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置给定接口的 IPv4 多播生存时间（Multicast Time-to-live）值。

<a id="r_ga0f324d39cf60e7babb5a1c4a364a8e86"></a>

```c
bool net_if_ipv4_addr_onlink (struct net_if **iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_addr_onlink](#ga0f324d39cf60e7babb5a1c4a364a8e86)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查此 IPv4 地址是否属于本网络接口的子网（Subnet）。

<a id="r_ga53fb4ce0130fc8d665ddfd466d2a5eb8"></a>

```c
struct net_if_addr * net_if_ipv4_addr_lookup (const struct net_in_addr *addr, struct net_if **iface)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv4_addr_lookup](#ga53fb4ce0130fc8d665ddfd466d2a5eb8)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查此 IPv4 地址是否属于某个接口（Interface）。

<a id="r_ga496a33ce937652ff60e437f73590dcd8"></a>

```c
struct net_if_addr * net_if_ipv4_addr_lookup_by_iface (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv4_addr_lookup_by_iface](#ga496a33ce937652ff60e437f73590dcd8)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查此 IPv4 地址是否属于这个特定接口（Specific Interface）。

<a id="r_ga8164e6a01a311dcaa593039c90b5d7cb"></a>

```c
struct net_if_addr * net_if_ipv4_addr_add (struct net_if *iface, const struct net_in_addr *addr, enum net_addr_type addr_type, uint32_t vlifetime)
```

相关声明：[net_if_addr](../network_core_model_reference/P080_net_if_addr_结构体.md)、[net_if_ipv4_addr_add](#ga8164e6a01a311dcaa593039c90b5d7cb)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_addr_type](../api_network_work_driver_reference/P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#gafecee2d4a331dc85ad962b81a6303e41)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向接口（Interface）添加 IPv4 地址。

<a id="r_ga28c3dc1bd0f85710ab3fc8c012183742"></a>

```c
bool net_if_ipv4_addr_rm (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_addr_rm](#ga28c3dc1bd0f85710ab3fc8c012183742)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

从接口（Interface）移除 IPv4 地址。

<a id="r_gae756e33c22b265b0218345cabfc85227"></a>

```c
int net_if_ipv4_addr_lookup_by_index (const struct net_in_addr *addr)
```

相关声明：[net_if_ipv4_addr_lookup_by_index](#gae756e33c22b265b0218345cabfc85227)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查此 IPv4 地址是否属于某个接口索引（Interface Index）对应的接口。

<a id="r_ga336c5ec3a6af5b03fafc5796c16de396"></a>

```c
bool net_if_ipv4_addr_add_by_index (int index, const struct net_in_addr *addr, enum net_addr_type addr_type, uint32_t vlifetime)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_addr_add_by_index](#ga336c5ec3a6af5b03fafc5796c16de396)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_addr_type](../api_network_work_driver_reference/P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#gafecee2d4a331dc85ad962b81a6303e41)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过网络接口索引（Network Interface Index）向接口添加 IPv4 地址。

<a id="r_ga1b27ab5977aa53ce7f01195c76c23b13"></a>

```c
bool net_if_ipv4_addr_rm_by_index (int index, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_addr_rm_by_index](#ga1b27ab5977aa53ce7f01195c76c23b13)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

通过接口索引（Interface Index）从接口移除 IPv4 地址。

<a id="r_gaae71be476e27c178ebb21b0f183c2825"></a>

```c
void net_if_ipv4_addr_foreach (struct net_if *iface, net_if_ip_addr_cb_t cb, void *user_data)
```

相关声明：[net_if_ipv4_addr_foreach](#gaae71be476e27c178ebb21b0f183c2825)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ip_addr_cb_t](#gab58d8561a4f21899e2db34043d346516)。

遍历网络接口的全部 IPv4 地址，并对每个正在使用的地址调用回调（Callback）。

<a id="r_ga720bf6b3a90f747dd345c56d3afc0c13"></a>

```c
struct net_if_mcast_addr * net_if_ipv4_maddr_add (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)、[net_if_ipv4_maddr_add](#ga720bf6b3a90f747dd345c56d3afc0c13)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

向接口（Interface）添加 IPv4 多播地址（Multicast Address）。

<a id="r_gaa5f133b3999b2d3342707b4a5357d16b"></a>

```c
bool net_if_ipv4_maddr_rm (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_maddr_rm](#gaa5f133b3999b2d3342707b4a5357d16b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

从接口（Interface）移除 IPv4 多播地址（Multicast Address）。

<a id="r_gae82f53c670f602e9c37b65abb6dfaec7"></a>

```c
void net_if_ipv4_maddr_foreach (struct net_if *iface, net_if_ip_maddr_cb_t cb, void *user_data)
```

相关声明：[net_if_ipv4_maddr_foreach](#gae82f53c670f602e9c37b65abb6dfaec7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ip_maddr_cb_t](#ga726eed76563c223de8f611e2544febe9)。

遍历网络接口的全部 IPv4 多播地址（Multicast Addresses），并对每个正在使用的地址调用回调。

<a id="r_gab6c07d40074298e0e49ed0a8c6a230c1"></a>

```c
struct net_if_mcast_addr * net_if_ipv4_maddr_lookup (const struct net_in_addr *addr, struct net_if **iface)
```

相关声明：[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)、[net_if_ipv4_maddr_lookup](#gab6c07d40074298e0e49ed0a8c6a230c1)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查此 IPv4 多播地址（Multicast Address）是否属于指定接口或某个接口（Interface）。

<a id="r_gae275a5e75817aa178d36f422573ad76a"></a>

```c
void net_if_ipv4_maddr_join (struct net_if *iface, struct net_if_mcast_addr *addr)
```

相关声明：[net_if_ipv4_maddr_join](#gae275a5e75817aa178d36f422573ad76a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

将给定多播地址（Multicast Address）标记为已加入（Joined）。

<a id="r_gaa30769fc8016f1a7496b3ede277d8d8a"></a>

```c
static bool net_if_ipv4_maddr_is_joined (struct net_if_mcast_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_maddr_is_joined](#gaa30769fc8016f1a7496b3ede277d8d8a)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

检查是否已加入（Joined）给定多播地址（Multicast Address）。

<a id="r_ga1408fe384736d20f36c035c10007113c"></a>

```c
void net_if_ipv4_maddr_leave (struct net_if *iface, struct net_if_mcast_addr *addr)
```

相关声明：[net_if_ipv4_maddr_leave](#ga1408fe384736d20f36c035c10007113c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_mcast_addr](../network_core_model_reference/P089_net_if_mcast_addr_结构体.md)。

将给定多播地址（Multicast Address）标记为已退出（Left）。

<a id="r_ga7f8e34c1001e89d759d3a1e6a5538647"></a>

```c
static void net_if_ipv4_nbr_flush (struct net_if *iface)
```

相关声明：[net_if_ipv4_nbr_flush](#ga7f8e34c1001e89d759d3a1e6a5538647)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

清空网络接口的 IPv4 邻居缓存（Neighbor Cache）。

<a id="r_ga5e676ccb2b0cf22410e595d61d8363ce"></a>

```c
static bool net_if_ipv4_nbr_rm (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_nbr_rm](#ga5e676ccb2b0cf22410e595d61d8363ce)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

从 IPv4 邻居缓存（Neighbor Cache）中移除一个邻居（Neighbor）。

<a id="r_ga4ce8f0f7d00b66b905ee9cf1a8b398c6"></a>

```c
static struct net_in_addr * net_if_router_ipv4 (struct net_if_router *router)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_router_ipv4](#ga4ce8f0f7d00b66b905ee9cf1a8b398c6)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)。

获取给定路由器（Router）的 IPv4 地址。

<a id="r_ga4a290f9bbd65c041e8722b92fe675b77"></a>

```c
struct net_if_router * net_if_ipv4_router_lookup (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv4_router_lookup](#ga4a290f9bbd65c041e8722b92fe675b77)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查该 IPv4 地址是否为系统中已配置路由器（Router）的地址之一。

<a id="r_gaffdb60ab8db5de97fc5b568a5be1ee8e"></a>

```c
struct net_if_router * net_if_ipv4_router_find_default (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv4_router_find_default](#gaffdb60ab8db5de97fc5b568a5be1ee8e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

查找用于此 IPv4 地址的默认路由器（Default Router）。

<a id="r_ga074030e3dd930630e519a1f26b662be6"></a>

```c
struct net_if_router * net_if_ipv4_router_add (struct net_if *iface, const struct net_in_addr *addr, bool is_default, uint16_t router_lifetime)
```

相关声明：[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)、[net_if_ipv4_router_add](#ga074030e3dd930630e519a1f26b662be6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向系统添加 IPv4 路由器（Router）。

<a id="r_ga6be14f5307bc63ce87ff0a3fad7c7f4d"></a>

```c
bool net_if_ipv4_router_rm (struct net_if_router *router)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_router_rm](#ga6be14f5307bc63ce87ff0a3fad7c7f4d)、[net_if_router](../network_core_model_reference/P091_net_if_router_结构体.md)。

从系统移除 IPv4 路由器（Router）。

<a id="r_gadd50b3a60e8ede04e482b9df8953695d"></a>

```c
int net_if_ipv4_route_add (struct net_if *iface, const struct net_in_addr *addr, uint8_t mask_len, const struct net_in_addr *nexthop, uint32_t lifetime)
```

相关声明：[net_if_ipv4_route_add](#gadd50b3a60e8ede04e482b9df8953695d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向系统路由表（Routing Table）添加 IPv4 路由（Route）。

<a id="r_ga919149bde5d0f1319ba60a9b8de1a1bc"></a>

```c
bool net_if_ipv4_addr_mask_cmp (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_addr_mask_cmp](#ga919149bde5d0f1319ba60a9b8de1a1bc)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查给定 IPv4 地址是否属于本地子网（Local Subnet）。

<a id="r_ga45774258112186b5989b974df934dff1"></a>

```c
bool net_if_ipv4_is_addr_bcast (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_is_addr_bcast](#ga45774258112186b5989b974df934dff1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

检查给定的 IPv4 地址是否为广播地址（Broadcast Address）。

<a id="r_ga1e66458147628585dd5dd613a68a87a3"></a>

```c
static struct net_if * net_if_ipv4_select_src_iface (const struct net_in_addr *dst)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv4_select_src_iface](#ga1e66458147628585dd5dd613a68a87a3)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

获取向目的地发送 IPv4 网络数据时应使用的网络接口（Network Interface）。

<a id="r_ga29b73b4d2d18edc06b36f5e5dbcbd441"></a>

```c
static struct net_if * net_if_ipv4_select_src_iface_addr (const struct net_in_addr *dst, const struct net_in_addr **src_addr)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_ipv4_select_src_iface_addr](#ga29b73b4d2d18edc06b36f5e5dbcbd441)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

获取向目的地发送 IPv4 网络数据时应使用的网络接口（Network Interface）。

<a id="r_gae7ee369901b43a3bd071dacd3a51049a"></a>

```c
static const struct net_in_addr * net_if_ipv4_select_src_addr (struct net_if *iface, const struct net_in_addr *dst)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_ipv4_select_src_addr](#gae7ee369901b43a3bd071dacd3a51049a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

获取向目的地发送网络数据时应使用的 IPv4 源地址（Source Address）。

<a id="r_ga6ea398dd6a15e74423fdd55b6a8976f5"></a>

```c
struct net_in_addr * net_if_ipv4_get_ll (struct net_if *iface, enum net_addr_state addr_state)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_ipv4_get_ll](#ga6ea398dd6a15e74423fdd55b6a8976f5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_addr_state](../api_network_work_driver_reference/P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga32e58fc83532ef57eeb6ff952f17288d)。

获取处于给定状态的 IPv4 链路本地地址（Link Local Address）。

<a id="r_ga7648ccab37ffa991f757e6c6a985eec1"></a>

```c
struct net_in_addr * net_if_ipv4_get_global_addr (struct net_if *iface, enum net_addr_state addr_state)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_ipv4_get_global_addr](#ga7648ccab37ffa991f757e6c6a985eec1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_addr_state](../api_network_work_driver_reference/P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga32e58fc83532ef57eeb6ff952f17288d)。

获取处于给定状态的 IPv4 全局地址（Global Address）。

<a id="r_gaafc473b7c3f3e32f1ba93dd1f7190fe5"></a>

```c
struct net_in_addr net_if_ipv4_get_netmask_by_addr (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_ipv4_get_netmask_by_addr](#gaafc473b7c3f3e32f1ba93dd1f7190fe5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

获取与接口某个地址关联的 IPv4 网络掩码（Netmask）。

<a id="r_gaa5087a91a20e4283b4fa9a09add6aaa0"></a>

```c
bool net_if_ipv4_set_netmask_by_addr_by_index (int index, const struct net_in_addr *addr, const struct net_in_addr *netmask)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_set_netmask_by_addr_by_index](#gaa5087a91a20e4283b4fa9a09add6aaa0)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

根据接口索引（Interface Index），为给定地址设置 IPv4 网络掩码（Netmask）。

<a id="r_gaa42af45521841ae8265396c89966a2db"></a>

```c
bool net_if_ipv4_set_netmask_by_addr (struct net_if *iface, const struct net_in_addr *addr, const struct net_in_addr *netmask)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_set_netmask_by_addr](#gaa42af45521841ae8265396c89966a2db)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

根据接口索引（Interface Index），为给定地址设置 IPv4 网络掩码（Netmask）。

<a id="r_ga12eee59d98d9891f88ed75fbeb5f4d19"></a>

```c
struct net_in_addr net_if_ipv4_get_gw (struct net_if *iface)
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_if_ipv4_get_gw](#ga12eee59d98d9891f88ed75fbeb5f4d19)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取接口的 IPv4 网关（Gateway）。

<a id="r_ga0826491553b11c764277cde76490eb02"></a>

```c
void net_if_ipv4_set_gw (struct net_if *iface, const struct net_in_addr *gw)
```

相关声明：[net_if_ipv4_set_gw](#ga0826491553b11c764277cde76490eb02)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

设置接口的 IPv4 网关（Gateway）。

<a id="r_ga8810a82cf2b6e3f44541c47c635e39de"></a>

```c
bool net_if_ipv4_set_gw_by_index (int index, const struct net_in_addr *gw)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_ipv4_set_gw_by_index](#ga8810a82cf2b6e3f44541c47c635e39de)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

根据接口索引（Interface Index）设置 IPv4 网关（Gateway）。

<a id="r_gab3c666bf6a0677c25e90082fed88f7a5"></a>

```c
struct net_if * net_if_select_src_iface (const struct net_sockaddr *dst)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_select_src_iface](#gab3c666bf6a0677c25e90082fed88f7a5)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

获取向目的地发送 IPv6 或 IPv4 网络数据时应使用的网络接口（Network Interface）。

<a id="r_gaa81b7d9ed8dc05da3391265dbc89b665"></a>

```c
void net_if_register_link_cb (struct net_if_link_cb *link, net_if_link_callback_t cb)
```

相关声明：[net_if_register_link_cb](#gaa81b7d9ed8dc05da3391265dbc89b665)、[net_if_link_cb](../network_core_model_reference/P088_net_if_link_cb_结构体.md)、[net_if_link_callback_t](#ga0f87d5753fcd7cce40ecd161e6c91078)。

注册链路回调（Link Callback）。

<a id="r_ga6ba64fac6e8d846ae7be5990f49a8293"></a>

```c
void net_if_unregister_link_cb (struct net_if_link_cb *link)
```

相关声明：[net_if_unregister_link_cb](#ga6ba64fac6e8d846ae7be5990f49a8293)、[net_if_link_cb](../network_core_model_reference/P088_net_if_link_cb_结构体.md)。

注销链路回调（Link Callback）。

<a id="r_gaaa64aa4391a85760bb2daf600ac4d898"></a>

```c
void net_if_call_link_cb (struct net_if *iface, struct net_linkaddr *lladdr, int status)
```

相关声明：[net_if_call_link_cb](#gaaa64aa4391a85760bb2daf600ac4d898)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)。

调用链路回调函数（Link Callback Function）。

<a id="r_gac040bd7860e5cd6424709fbf98dd4a99"></a>

```c
static bool net_if_need_calc_rx_checksum (struct net_if *iface, enum net_if_checksum_type chksum_type)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_need_calc_rx_checksum](#gac040bd7860e5cd6424709fbf98dd4a99)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_checksum_type](#ga8db412ae79c64cafe81a66f5acb2f8e9)。

检查是否可以省略接收网络数据包的校验和计算（Checksum Calculation）。

<a id="r_ga0db8854bb77133b19c5b0852b43119bb"></a>

```c
static bool net_if_need_calc_tx_checksum (struct net_if *iface, enum net_if_checksum_type chksum_type)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_need_calc_tx_checksum](#ga0db8854bb77133b19c5b0852b43119bb)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_checksum_type](#ga8db412ae79c64cafe81a66f5acb2f8e9)。

检查发送网络数据包时是否可以省略校验和计算（Checksum Calculation）。

<a id="r_ga72708cdb7f133fe5d7edf819756c3516"></a>

```c
struct net_if * net_if_get_by_index (int index)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_by_index](#ga72708cdb7f133fe5d7edf819756c3516)。

根据索引（Index）获取接口（Interface）。

<a id="r_ga02445f6c61f0d29f56ac0ef59e025630"></a>

```c
int net_if_get_by_iface (struct net_if *iface)
```

相关声明：[net_if_get_by_iface](#ga02445f6c61f0d29f56ac0ef59e025630)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

根据指针（Pointer）获取接口索引（Interface Index）。

<a id="r_ga96b198fd9df4a985b0dde84dd7152815"></a>

```c
void net_if_foreach (net_if_cb_t cb, void *user_data)
```

相关声明：[net_if_foreach](#ga96b198fd9df4a985b0dde84dd7152815)、[net_if_cb_t](#gac48ab8e6337e7cf387af9b293f254a80)。

遍历全部网络接口（Network Interfaces），并为每个接口调用回调。

<a id="r_ga02644cc623fc7a8878c17d54984e4210"></a>

```c
int net_if_up (struct net_if *iface)
```

相关声明：[net_if_up](#ga02644cc623fc7a8878c17d54984e4210)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启用接口（Bring Interface Up）。

<a id="r_ga7e9b368d4abf9da5656140df70cfa334"></a>

```c
static bool net_if_is_up (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_up](#ga7e9b368d4abf9da5656140df70cfa334)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查接口是否已启用且正在运行（Up and Running）。

<a id="r_ga2187650062d6139b9f4b81745a206803"></a>

```c
int net_if_down (struct net_if *iface)
```

相关声明：[net_if_down](#ga2187650062d6139b9f4b81745a206803)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

停用接口（Bring Interface Down）。

<a id="r_ga099a484a654ad9af35d3212fc2c995b2"></a>

```c
static bool net_if_is_admin_up (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_admin_up](#ga099a484a654ad9af35d3212fc2c995b2)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查接口是否已由管理员启用（Brought Up by the Administrator）。

<a id="r_ga35e5db3a631ac9039f14d86e59fc0dcc"></a>

```c
void net_if_carrier_on (struct net_if *iface)
```

相关声明：[net_if_carrier_on](#ga35e5db3a631ac9039f14d86e59fc0dcc)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

底层网络设备已检测到载波（Carrier），即网线已连接。

<a id="r_ga6839941422a88c1f707ab70ea34df323"></a>

```c
void net_if_carrier_off (struct net_if *iface)
```

相关声明：[net_if_carrier_off](#ga6839941422a88c1f707ab70ea34df323)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

底层网络设备已失去载波（Carrier），即网线已断开。

<a id="r_ga095554237016e563d76cfd602d1dae77"></a>

```c
static bool net_if_is_carrier_ok (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_carrier_ok](#ga095554237016e563d76cfd602d1dae77)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查网络设备是否存在载波（Carrier）。

<a id="r_ga89a3374d4bb116460a7b7c50a750b593"></a>

```c
void net_if_dormant_on (struct net_if *iface)
```

相关声明：[net_if_dormant_on](#ga89a3374d4bb116460a7b7c50a750b593)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将接口标记为休眠（Dormant）。

<a id="r_ga1c31fac887d944ac0a16aad70e889496"></a>

```c
void net_if_dormant_off (struct net_if *iface)
```

相关声明：[net_if_dormant_off](#ga1c31fac887d944ac0a16aad70e889496)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将接口标记为非休眠（Not Dormant）。

<a id="r_ga6e2e6102271c37acaa59c54e2aa6b413"></a>

```c
static bool net_if_is_dormant (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_dormant](#ga6e2e6102271c37acaa59c54e2aa6b413)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查接口是否处于休眠状态（Dormant）。

<a id="r_ga198accbfeaeb049eba9ffa2fac82c747"></a>

```c
void net_if_register_timestamp_cb (struct net_if_timestamp_cb *handle, struct net_pkt *pkt, struct net_if *iface, net_if_timestamp_callback_t cb)
```

相关声明：[net_if_register_timestamp_cb](#ga198accbfeaeb049eba9ffa2fac82c747)、[net_if_timestamp_cb](../network_core_model_reference/P092_net_if_timestamp_cb_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_timestamp_callback_t](#ga656c2ba47d280aa1c47bc2d062debbfa)。

注册时间戳回调（Timestamp Callback）。

<a id="r_gaa5b88649296a278860ca36f14369834f"></a>

```c
void net_if_unregister_timestamp_cb (struct net_if_timestamp_cb *handle)
```

相关声明：[net_if_unregister_timestamp_cb](#gaa5b88649296a278860ca36f14369834f)、[net_if_timestamp_cb](../network_core_model_reference/P092_net_if_timestamp_cb_结构体.md)。

注销时间戳回调（Timestamp Callback）。

<a id="r_gada944cae018ee13d5478402a850e89e2"></a>

```c
void net_if_call_timestamp_cb (struct net_pkt *pkt)
```

相关声明：[net_if_call_timestamp_cb](#gada944cae018ee13d5478402a850e89e2)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

调用时间戳回调函数（Timestamp Callback Function）。

<a id="r_ga139ca2bcb45e9ab45b309c5004bb11c7"></a>

```c
void net_if_add_tx_timestamp (struct net_pkt *pkt)
```

相关声明：[net_if_add_tx_timestamp](#ga139ca2bcb45e9ab45b309c5004bb11c7)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

<a id="r_gaf9f81f3b9697ca47f7674d85f37a8d80"></a>

```c
static int net_if_set_promisc (struct net_if *iface)
```

相关声明：[net_if_set_promisc](#gaf9f81f3b9697ca47f7674d85f37a8d80)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将网络接口设为混杂模式（Promiscuous Mode）。

<a id="r_ga9c8212c087883510050ac6a39ef0a7bf"></a>

```c
static void net_if_unset_promisc (struct net_if *iface)
```

相关声明：[net_if_unset_promisc](#ga9c8212c087883510050ac6a39ef0a7bf)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将网络接口设为正常模式（Normal Mode）。

<a id="r_ga9f1a6eab849517734ec422deb0ba71f5"></a>

```c
static bool net_if_is_promisc (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_promisc](#ga9f1a6eab849517734ec422deb0ba71f5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查是否设置了混杂模式（Promiscuous Mode）。

<a id="r_ga3cddda628eca248246f9aa3b81938f95"></a>

```c
static bool net_if_are_pending_tx_packets (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_are_pending_tx_packets](#ga3cddda628eca248246f9aa3b81938f95)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查给定网络接口是否有待发送的网络数据（Pending TX Network Data）。

<a id="r_ga703d9e3c128a3a3f0e452d789a4b7bf6"></a>

```c
bool net_if_is_ethernet (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_ethernet](#ga703d9e3c128a3a3f0e452d789a4b7bf6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查网络接口是否为有线以太网（Cabled Ethernet）。

<a id="r_ga529067a284cac1187b336080e56129c8"></a>

```c
struct net_if * net_if_get_first_ethernet (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_first_ethernet](#ga529067a284cac1187b336080e56129c8)。

获取第一个有线以太网网络接口（Cabled Ethernet Network Interface）。

<a id="r_gaa458b5f349c55007108b47b99f4954d5"></a>

```c
bool net_if_is_wifi (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_if_is_wifi](#gaa458b5f349c55007108b47b99f4954d5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查网络接口是否支持 Wi-Fi。

<a id="r_ga6e89bbafb6c0acdc6bf51078e2027236"></a>

```c
struct net_if * net_if_get_first_wifi (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_first_wifi](#ga6e89bbafb6c0acdc6bf51078e2027236)。

获取第一个 Wi-Fi 网络接口（Network Interface）。

<a id="r_ga0fc3ba6172956f6847027e0bd3d367de"></a>

```c
struct net_if * net_if_get_wifi_sta (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_wifi_sta](#ga0fc3ba6172956f6847027e0bd3d367de)。

获取 Wi-Fi 网络站点接口（Station Interface）。

<a id="r_gaf830eab616191009d88f58b761694b49"></a>

```c
struct net_if * net_if_get_wifi_sap (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_if_get_wifi_sap](#gaf830eab616191009d88f58b761694b49)。

获取第一个 Wi-Fi 网络软件接入点接口（Soft-AP Interface）。

<a id="r_ga5f653cd73c1ecd548a931eb7fbd170f7"></a>

```c
int net_if_get_name (struct net_if *iface, char *buf, int len)
```

相关声明：[net_if_get_name](#ga5f653cd73c1ecd548a931eb7fbd170f7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取网络接口名称（Network Interface Name）。

<a id="r_ga05dec64966fc39e3deb0679b9585688b"></a>

```c
int net_if_set_name (struct net_if *iface, const char *buf)
```

相关声明：[net_if_set_name](#ga05dec64966fc39e3deb0679b9585688b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置网络接口名称（Network Interface Name）。

<a id="r_ga1774ac036032bb0dc2c662f6f4f66a7f"></a>

```c
int net_if_get_by_name (const char *name)
```

相关声明：[net_if_get_by_name](#ga1774ac036032bb0dc2c662f6f4f66a7f)。

根据名称（Name）获取接口索引（Interface Index）。

## 2.6\_详细说明（Detailed Documentation）

<a id="gad8e37fc7a32339312dcfa614255988e8"></a>

### `NET_DEVICE_DT_ADD_IFACE`

```c
#define NET_DEVICE_DT_ADD_IFACE ( node_id, l2, l2_ctx_type, mtu, instance )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
Z_NET_DEVICE_IF_INIT_INSTANCE(Z_DEVICE_DT_DEV_ID(node_id), instance, l2, l2_ctx_type, mtu)
```

向通过 `NET_DEVICE_DT_DEFINE` 创建的网络设备（Network Device）添加第二个或更多网络接口（Network Interfaces）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符。 |
| `l2` | 此网络接口的网络二层（L2）。 |
| `l2_ctx_type` | 二层上下文数据（L2 Context Data）的类型。 |
| `mtu` | 此网络接口（Network Interface）的最大传输单元（MTU），以字节为单位。 |
| `instance` | 实例标识符（Instance Identifier）；`0` 保留给使用 `NET_DEVICE_DT_DEFINE` 创建的第一个接口，附加接口从 `1` 开始。 |

<a id="gab1f762b01ae7bc37cd4a25724c123dda"></a>

### `NET_DEVICE_DT_DEFINE`

```c
#define NET_DEVICE_DT_DEFINE ( node_id, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
Z_NET_DEVICE_INIT(node_id, Z_DEVICE_DT_DEV_ID(node_id), \
                  DEVICE_DT_NAME(node_id), init_fn, pm, data,   \
                  config, prio, api, l2, l2_ctx_type, mtu)
```

类似于 `NET_DEVICE_INIT`，但从设备树节点（Devicetree Node）获取元数据（Metadata）。

创建网络接口（Network Interface），并将其绑定到网络设备（Network Device）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符。 |
| `init_fn` | 驱动初始化函数（Init Function）的地址。 |
| `pm` | 与设备关联的 `struct pm_device` 引用，可选。 |
| `data` | 指向设备私有数据（Private Data）的指针。 |
| `config` | 包含此驱动实例配置信息（Configuration Information）的结构体地址。 |
| `prio` | 执行配置的初始化层级（Initialization Level）。 |
| `api` | 提供驱动使用的 API 函数结构体（API Function Struct）的初始指针，可以为 `NULL`。 |
| `l2` | 此网络接口的网络二层（L2）。 |
| `l2_ctx_type` | 二层上下文数据（L2 Context Data）的类型。 |
| `mtu` | 此网络接口（Network Interface）的最大传输单元（MTU），以字节为单位。 |

<a id="ga50702b043a0791e59e7d5679dda1d9e8"></a>

### `NET_DEVICE_DT_DEFINE_INSTANCE`

```c
#define NET_DEVICE_DT_DEFINE_INSTANCE ( node_id, instance, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
Z_NET_DEVICE_INIT_INSTANCE(node_id,                             \
                           Z_DEVICE_DT_DEV_ID(node_id),         \
                           DEVICE_DT_NAME(node_id), instance,   \
                           init_fn, pm, data, config, prio,     \
                           api, l2, l2_ctx_type, mtu)
```

类似于 `NET_DEVICE_OFFLOAD_INIT`，但从设备树（Devicetree）获取元数据（Metadata）。

创建多个网络接口（Network Interfaces），并将它们绑定到网络设备。如果网络设备需要多个网络接口实例，使用下方宏，并在每次调用时提供不同的实例后缀，例如 `0, 1, 2, ...` 或 `a, b, c, ...`，选择适合的方式即可。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符。 |
| `instance` | 实例标识符（Instance Identifier）。 |
| `init_fn` | 驱动初始化函数（Init Function）的地址。 |
| `pm` | 与设备关联的 `struct pm_device` 引用，可选。 |
| `data` | 指向设备私有数据（Private Data）的指针。 |
| `config` | 包含此驱动实例配置信息（Configuration Information）的结构体地址。 |
| `prio` | 执行配置的初始化层级（Initialization Level）。 |
| `api` | 提供驱动使用的 API 函数结构体（API Function Struct）的初始指针，可以为 `NULL`。 |
| `l2` | 此网络接口的网络二层（L2）。 |
| `l2_ctx_type` | 二层上下文数据（L2 Context Data）的类型。 |
| `mtu` | 此网络接口（Network Interface）的最大传输单元（MTU），以字节为单位。 |

<a id="ga00fe86342a77e32fe440e1bd97c51d51"></a>

### `NET_DEVICE_DT_INST_ADD_IFACE`

```c
#define NET_DEVICE_DT_INST_ADD_IFACE ( inst, ... )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
NET_DEVICE_DT_ADD_IFACE(DT_DRV_INST(inst), __VA_ARGS__)
```

类似于 `NET_DEVICE_DT_ADD_IFACE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号（Instance Number）。调用 `NET_DEVICE_DT_ADD_IFACE` 时将其替换为 `DT_DRV_INST(inst)`。 |
| `...` | `NET_DEVICE_DT_ADD_IFACE` 所要求的其他参数（Parameters）。 |

<a id="ga7edd8bc59444d92cad0371c36f9949b7"></a>

### `NET_DEVICE_DT_INST_DEFINE`

```c
#define NET_DEVICE_DT_INST_DEFINE ( inst, ... )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
NET_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
```

类似于 `NET_DEVICE_DT_DEFINE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号（Instance Number）。调用 `NET_DEVICE_DT_DEFINE` 时将其替换为 `DT_DRV_INST(inst)`。 |
| `...` | `NET_DEVICE_DT_DEFINE` 所要求的其他参数（Parameters）。 |

<a id="gabe4b8589996a53cbc50b76c8ea15aa0c"></a>

### `NET_DEVICE_DT_INST_DEFINE_INSTANCE`

```c
#define NET_DEVICE_DT_INST_DEFINE_INSTANCE ( inst, ... )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
NET_DEVICE_DT_DEFINE_INSTANCE(DT_DRV_INST(inst), __VA_ARGS__)
```

类似于 `NET_DEVICE_DT_DEFINE_INSTANCE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号（Instance Number）。调用 `NET_DEVICE_DT_DEFINE_INSTANCE` 时将其替换为 `DT_DRV_INST(inst)`。 |
| `...` | `NET_DEVICE_DT_DEFINE_INSTANCE` 所要求的其他参数（Parameters）。 |

<a id="ga1cab6943a28e3d3754e36623834b93fd"></a>

### `NET_DEVICE_DT_INST_OFFLOAD_DEFINE`

```c
#define NET_DEVICE_DT_INST_OFFLOAD_DEFINE ( inst, ... )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
NET_DEVICE_DT_OFFLOAD_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
```

类似于 `NET_DEVICE_DT_OFFLOAD_DEFINE`，但用于与 `DT_DRV_COMPAT` 兼容的一个实例（Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号（Instance Number）。调用 `NET_DEVICE_DT_OFFLOAD_DEFINE` 时将其替换为 `DT_DRV_INST(inst)`。 |
| `...` | `NET_DEVICE_DT_OFFLOAD_DEFINE` 所要求的其他参数（Parameters）。 |

<a id="gab2b287025e194dec1fab24e44d95362f"></a>

### `NET_DEVICE_DT_OFFLOAD_DEFINE`

```c
#define NET_DEVICE_DT_OFFLOAD_DEFINE ( node_id, init_fn, pm, data, config, prio, api, mtu )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
Z_NET_DEVICE_OFFLOAD_INIT(node_id, Z_DEVICE_DT_DEV_ID(node_id), \
                          DEVICE_DT_NAME(node_id), init_fn, pm, \
                          data, config, prio, api, mtu)
```

类似于 `NET_DEVICE_OFFLOAD_INIT`，但从设备树节点（Devicetree Node）获取元数据（Metadata）。

创建卸载型网络接口（Offloaded Network Interface），并将其绑定到网络设备。该接口由设备厂商的硬件抽象层（HAL）或类似实现提供。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符。 |
| `init_fn` | 驱动初始化函数（Init Function）的地址。 |
| `pm` | 与设备关联的 `struct pm_device` 引用，可选。 |
| `data` | 指向设备私有数据（Private Data）的指针。 |
| `config` | 包含此驱动实例配置信息（Configuration Information）的结构体地址。 |
| `prio` | 执行配置的初始化层级（Initialization Level）。 |
| `api` | 提供驱动使用的 API 函数结构体（API Function Struct）的初始指针，可以为 `NULL`。 |
| `mtu` | 此网络接口（Network Interface）的最大传输单元（MTU），以字节为单位。 |

<a id="ga02971562c42494e2a5f71e1f8587e709"></a>

### `NET_DEVICE_INIT`

```c
#define NET_DEVICE_INIT ( dev_id, name, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
Z_NET_DEVICE_INIT(DT_INVALID_NODE, dev_id, name, init_fn, pm,   \
                  data, config, prio, api, l2, l2_ctx_type, mtu)
```

创建网络接口（Network Interface），并将其绑定到网络设备（Network Device）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_id` | 网络设备标识（Network Device ID）。 |
| `name` | 该驱动实例向系统公开的名称（Name）。 |
| `init_fn` | 驱动初始化函数（Init Function）的地址。 |
| `pm` | 与设备关联的 `struct pm_device` 引用，可选。 |
| `data` | 指向设备私有数据（Private Data）的指针。 |
| `config` | 包含此驱动实例配置信息（Configuration Information）的结构体地址。 |
| `prio` | 执行配置的初始化层级（Initialization Level）。 |
| `api` | 提供驱动使用的 API 函数结构体（API Function Struct）的初始指针，可以为 `NULL`。 |
| `l2` | 此网络接口的网络二层（L2）。 |
| `l2_ctx_type` | 二层上下文数据（L2 Context Data）的类型。 |
| `mtu` | 此网络接口（Network Interface）的最大传输单元（MTU），以字节为单位。 |

<a id="gacc7edecdd9de9920cc155977d8fec2a2"></a>

### `NET_DEVICE_INIT_INSTANCE`

```c
#define NET_DEVICE_INIT_INSTANCE ( dev_id, name, instance, init_fn, pm, data, config, prio, api, l2, l2_ctx_type, mtu )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
Z_NET_DEVICE_INIT_INSTANCE(DT_INVALID_NODE, dev_id, name,       \
                           instance, init_fn, pm, data, config, \
                           prio, api, l2, l2_ctx_type, mtu)
```

创建多个网络接口（Network Interfaces），并将它们绑定到网络设备（Network Device）。

如果网络设备（Network Device）需要多个网络接口实例（Network Interface Instance），使用下面的宏，每次提供不同的实例后缀（Instance Suffix），例如 `0, 1, 2, ...` 或 `a, b, c, ...`，选择适合的形式即可。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_id` | 网络设备标识（Network Device ID）。 |
| `name` | 该驱动实例向系统公开的名称（Name）。 |
| `instance` | 实例标识符（Instance Identifier）。 |
| `init_fn` | 驱动初始化函数（Init Function）的地址。 |
| `pm` | 与设备关联的 `struct pm_device` 引用，可选。 |
| `data` | 指向设备私有数据（Private Data）的指针。 |
| `config` | 包含此驱动实例配置信息（Configuration Information）的结构体地址。 |
| `prio` | 执行配置的初始化层级（Initialization Level）。 |
| `api` | 提供驱动使用的 API 函数结构体（API Function Struct）的初始指针，可以为 `NULL`。 |
| `l2` | 此网络接口的网络二层（L2）。 |
| `l2_ctx_type` | 二层上下文数据（L2 Context Data）的类型。 |
| `mtu` | 此网络接口（Network Interface）的最大传输单元（MTU），以字节为单位。 |

<a id="ga255672607b7958db3f464d2a57a7e635"></a>

### `NET_DEVICE_OFFLOAD_INIT`

```c
#define NET_DEVICE_OFFLOAD_INIT ( dev_id, name, init_fn, pm, data, config, prio, api, mtu )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
Z_NET_DEVICE_OFFLOAD_INIT(DT_INVALID_NODE, dev_id, name,        \
                          init_fn, pm, data, config, prio, api, \
                          mtu)
```

创建卸载型网络接口（Offloaded Network Interface），并将其绑定到网络设备（Network Device）。

卸载型网络接口（Offloaded Network Interface）由设备厂商的硬件抽象层（HAL）或类似实现提供。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_id` | 网络设备标识（Network Device ID）。 |
| `name` | 该驱动实例向系统公开的名称（Name）。 |
| `init_fn` | 驱动初始化函数（Init Function）的地址。 |
| `pm` | 与设备关联的 `struct pm_device` 引用，可选。 |
| `data` | 指向设备私有数据（Private Data）的指针。 |
| `config` | 包含此驱动实例配置信息（Configuration Information）的结构体地址。 |
| `prio` | 执行配置的初始化层级（Initialization Level）。 |
| `api` | 提供驱动使用的 API 函数结构体（API Function Struct）的初始指针，可以为 `NULL`。 |
| `mtu` | 此网络接口（Network Interface）的最大传输单元（MTU），以字节为单位。 |

<a id="gae0fdb0b909e06ba7831e53700c32b84f"></a>

### `NET_IF_DECLARE`

```c
#define NET_IF_DECLARE ( dev_id, inst )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
static struct net_if NET_IF_GET_NAME(dev_id, inst)
```

网络接口（Network Interface）的前向声明（Forward Declaration）。

允许在实例化宏（Instantiation Macro）之前使用 `NET_IF_GET`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_id` | 提供给 `NET_IF_INIT` 或 `NET_IF_OFFLOAD_INIT` 的设备标识符（Device ID）。 |
| `inst` | 实例标识符（Instance Identifier）。 |

<a id="ga65e4d856b53096bf784a4d5a495ca507"></a>

### `NET_IF_DT_DECLARE`

```c
#define NET_IF_DT_DECLARE ( node_id, instance )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
NET_IF_DECLARE(Z_DEVICE_DT_DEV_ID(node_id), instance)
```

网络接口（Network Interface）的前向声明（Forward Declaration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备节点标识符（Device Node Identifier）。 |
| `instance` | 实例标识符（Instance Identifier）。 |

<a id="gadd040e5cc26a96c3f66f37539178c3b6"></a>

### `NET_IF_DT_GET`

```c
#define NET_IF_DT_GET ( node_id, instance )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
NET_IF_GET(Z_DEVICE_DT_DEV_ID(node_id), instance)
```

获取通过 `NET_DEVICE_DT_DEFINE` 或 `NET_DEVICE_DT_ADD_IFACE` 创建的网络接口（Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备节点标识符（Device Node Identifier）。 |
| `instance` | 实例标识符（Instance Identifier）。 |

<a id="ga421f0b8be2317c0865c50ca588f73509"></a>

### `NET_IF_DT_INST_DECLARE`

```c
#define NET_IF_DT_INST_DECLARE ( inst, ... )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
NET_IF_DT_DECLARE(DT_DRV_INST(inst), __VA_ARGS__)
```

网络接口（Network Interface）的前向声明（Forward Declaration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号（Instance Number）。调用 `NET_DEVICE_DT_ADD_IFACE` 时将其替换为 `DT_DRV_INST(inst)`。 |
| `...` | `NET_DEVICE_DT_ADD_IFACE` 所要求的其他参数（Parameters）。 |

<a id="ga48a80b52d8b5a16856c86041fc6492e6"></a>

### `NET_IF_DT_INST_GET`

```c
#define NET_IF_DT_INST_GET ( inst, ... )
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
NET_IF_DT_GET(DT_DRV_INST(inst), __VA_ARGS__)
```

获取通过 `NET_DEVICE_DT_DEFINE` 或 `NET_DEVICE_DT_ADD_IFACE` 创建的网络接口（Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号（Instance Number）。调用 `NET_IF_DT_GET` 时将其替换为 `DT_DRV_INST(inst)`。 |
| `...` | `NET_DEVICE_DT_ADD_IFACE` 所要求的其他参数（Parameters）。 |

<a id="ga2b824eff0adada3eb7ff626a8d7c3538"></a>

### `NET_IF_IPV6_DAD_NONCE_LEN`

```c
#define NET_IF_IPV6_DAD_NONCE_LEN 6U
```

```c
#include <zephyr/net/net_if.h>
```

RFC 7527 第 4 节定义的增强型重复地址检测（Enhanced DAD）的随机数（Nonce）载荷长度，单位为字节。

<a id="ga6c081875a6f5a848b3ad2fd220c63c3c"></a>

### `NET_IFACE_COUNT`

```c
#define NET_IFACE_COUNT ( _dst)
```

```c
#include <zephyr/net/net_if.h>
```

展开值（Value）：

```c
do {                                                    \
        extern struct net_if _net_if_list_start[];      \
        extern struct net_if _net_if_list_end[];        \
        *(_dst) = ((uintptr_t)_net_if_list_end -        \
                   (uintptr_t)_net_if_list_start) /     \
                sizeof(struct net_if);                  \
} while (0)
```

统计网络接口（Network Interfaces）的数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] _dst` | 指向用于写入结果的位置。 |

<a id="ga021e9877ee9532a899a298d6a2c7aeb2"></a>

### `NET_IPV6_MAX_REACHABLE_TIME`

```c
#define NET_IPV6_MAX_REACHABLE_TIME 3600000U
```

```c
#include <zephyr/net/net_if.h>
```

IPv6 基础可达时间（Base Reachable Time）的最大值，单位为毫秒。

基础可达时间（Base Reachable Time）的上限，与 RFC 4861 第 6.2.1 节规定的 `AdvReachableTime` 上限一致。传给 `net_if_ipv6_set_base_reachable_time` 的值若超过此上限，会被限制到该上限。这也避免 `net_if_ipv6_calc_reachable_time` 按 RFC 4861 的随机因子缩放该值时溢出。

<a id="gac48ab8e6337e7cf387af9b293f254a80"></a>

### `net_if_cb_t`

```c
typedef void(* net_if_cb_t) (struct net_if *iface, void *user_data)
```

```c
#include <zephyr/net/net_if.h>
```

遍历网络接口（Network Interfaces）时使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向当前网络接口（Network Interface）的指针。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="gab58d8561a4f21899e2db34043d346516"></a>

### `net_if_ip_addr_cb_t`

```c
typedef void(* net_if_ip_addr_cb_t) (struct net_if *iface, struct net_if_addr *addr, void *user_data)
```

```c
#include <zephyr/net/net_if.h>
```

遍历网络接口 IP 地址（Network Interface IP Addresses）时使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向地址所属网络接口（Network Interface）的指针。 |
| `addr` | 指向当前 IP 地址（IP Address）的指针。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="ga726eed76563c223de8f611e2544febe9"></a>

### `net_if_ip_maddr_cb_t`

```c
typedef void(* net_if_ip_maddr_cb_t) (struct net_if *iface, struct net_if_mcast_addr *maddr, void *user_data)
```

```c
#include <zephyr/net/net_if.h>
```

遍历网络接口多播 IP 地址（Network Interface Multicast IP Addresses）时使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向地址所属网络接口（Network Interface）的指针。 |
| `maddr` | 指向当前组播 IP 地址（Multicast IP Address）的指针。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="ga0f87d5753fcd7cce40ecd161e6c91078"></a>

### `net_if_link_callback_t`

```c
typedef void(* net_if_link_callback_t) (struct net_if *iface, struct net_linkaddr *dst, int status)
```

```c
#include <zephyr/net/net_if.h>
```

定义网络数据包（Network Packet）发送之后调用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向 `struct net_if` 的指针，`net_pkt` 已发送到该接口。 |
| `dst` | 网络数据包发送目的地的链路层地址（Link Layer Address）。 |
| `status` | 发送状态（Send Status）：`0` 表示成功，小于 `0` 表示错误。 |

<a id="ga0d64291573740a67eae7ff3fcc0910c5"></a>

### `net_if_mcast_callback_t`

```c
typedef void(* net_if_mcast_callback_t) (struct net_if *iface, const struct net_addr *addr, bool is_joined)
```

```c
#include <zephyr/net/net_if.h>
```

定义回调，在加入或退出 IPv6 或 IPv4 多播地址组（Multicast Address Group）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向 `struct net_if` 的指针，组播地址（Multicast Address）附属于该接口。 |
| `addr` | IP 组播地址（IP Multicast Address）。 |
| `is_joined` | 加入组播组（Multicast Group）时为 `true`，离开时为 `false`。 |

<a id="ga656c2ba47d280aa1c47bc2d062debbfa"></a>

### `net_if_timestamp_callback_t`

```c
typedef void(* net_if_timestamp_callback_t) (struct net_pkt *pkt)
```

```c
#include <zephyr/net/net_if.h>
```

定义网络数据包（Network Packet）被打上时间戳（Timestamped）之后调用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 指向 `struct net_pkt` 的指针，该数据包在发送后已加上时间戳（Timestamp）。 |

<a id="gaef3dfe26195514aac625e9f22e399759"></a>

### `net_socket_create_t`

```c
typedef int(* net_socket_create_t) (int, int, int)
```

```c
#include <zephyr/net/net_if.h>
```

用于创建卸载套接字（Offloaded Socket）的函数原型（Function Prototype）。

函数原型（Prototype）与 `socket()` 兼容。

<a id="ga8db412ae79c64cafe81a66f5acb2f8e9"></a>

### `net_if_checksum_type`

```c
enum net_if_checksum_type
```

```c
#include <zephyr/net/net_if.h>
```

要查询接口支持情况的校验和类型（Checksum Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_IF_CHECKSUM_IPV4_HEADER` | 接口支持 IPv4 首部校验和计算（Header Checksum Calculation）。 |
| `NET_IF_CHECKSUM_IPV4_TCP` | 接口支持 IPv4 中 TCP 载荷的校验和计算（Checksum Calculation）。 |
| `NET_IF_CHECKSUM_IPV4_UDP` | 接口支持 IPv4 中 UDP 载荷的校验和计算（Checksum Calculation）。 |
| `NET_IF_CHECKSUM_IPV4_ICMP` | 接口支持 IPv4 中 ICMP4 载荷的校验和计算（Checksum Calculation）。 |
| `NET_IF_CHECKSUM_IPV6_HEADER` | 接口支持 IPv6 首部校验和计算（Header Checksum Calculation）。译注：这是原文对能力项的表述；IPv6 基本首部本身没有校验和字段。 |
| `NET_IF_CHECKSUM_IPV6_TCP` | 接口支持 IPv6 中 TCP 载荷的校验和计算（Checksum Calculation）。 |
| `NET_IF_CHECKSUM_IPV6_UDP` | 接口支持 IPv6 中 UDP 载荷的校验和计算（Checksum Calculation）。 |
| `NET_IF_CHECKSUM_IPV6_ICMP` | 接口支持 IPv6 中 ICMP6 载荷的校验和计算（Checksum Calculation）。 |

<a id="gae691e5537917ffce27ad0db82c730371"></a>

### `net_if_flag`

```c
enum net_if_flag
```

```c
#include <zephyr/net/net_if.h>
```

网络接口标志（Network Interface Flags）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_IF_UP` | 接口处于管理启用状态（Admin Up）。 |
| `NET_IF_POINTOPOINT` | 接口为点到点接口（Point-to-point）。 |
| `NET_IF_PROMISC` | 接口处于混杂模式（Promiscuous Mode）。 |
| `NET_IF_NO_AUTO_START` | 初始化后不要立即启用接口（Bring Interface Up）。这要求设备驱动或其他组件在需要时手动启用接口。 |
| `NET_IF_SUSPENDED` | 电源管理（Power Management）专用：接口正在挂起。 |
| `NET_IF_FORWARD_MULTICASTS` | 此标志决定是否在本接口上转发其他接口接收到的组播（Multicast）。这会为本接口启用组播路由／转发（Multicast Routing/Forwarding）。 |
| `NET_IF_IPV4` | 接口支持 IPv4。 |
| `NET_IF_IPV6` | 接口支持 IPv6。 |
| `NET_IF_RUNNING` | 接口已启用并运行（Up and Running），可以接收和发送。 |
| `NET_IF_LOWER_UP` | 驱动报告第一层已就绪（L1 Up）。 |
| `NET_IF_DORMANT` | 驱动报告暂未就绪状态（Dormant）。 |
| `NET_IF_IPV6_NO_ND` | 已禁用 IPv6 邻居发现（Neighbor Discovery）。 |
| `NET_IF_IPV6_NO_MLD` | 已禁用 IPv6 组播侦听者发现（Multicast Listener Discovery）。 |
| `NET_IF_NO_TX_LOCK` | 接口的发送数据路径（TX Data Path）已禁用互斥锁加锁。 |

<a id="gadfe9d90f24046cd9bd4bbee096e747b9"></a>

### `net_if_oper_state`

```c
enum net_if_oper_state
```

```c
#include <zephyr/net/net_if.h>
```

网络接口运行状态（Network Interface Operational Status），参见 RFC 2863。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_IF_OPER_UNKNOWN` | 初始值（Initial Value），即未知。 |
| `NET_IF_OPER_NOTPRESENT` | 硬件缺失（Hardware Missing）。 |
| `NET_IF_OPER_DOWN` | 接口未启用（Down）。 |
| `NET_IF_OPER_LOWERLAYERDOWN` | 下层接口未启用（Lower Layer Down）。 |
| `NET_IF_OPER_TESTING` | 训练模式（Training Mode）。 |
| `NET_IF_OPER_DORMANT` | 等待外部操作（Waiting External Action）。 |
| `NET_IF_OPER_UP` | 接口已启用（Up）。 |

<a id="ga139ca2bcb45e9ab45b309c5004bb11c7"></a>

### `net_if_add_tx_timestamp()`

```c
void net_if_add_tx_timestamp ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/net_if.h>
```

<a id="gae66f6e7bd31545e6161fcd4600fe5842"></a>

### `net_if_addr_set_lf()`

```c
void net_if_addr_set_lf ( struct net_if_addr * ifaddr, bool is_infinite )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置网络接口地址的无限有效状态（Infinite Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ifaddr` | 网络接口的 IP 地址（IP Address）。 |
| `is_infinite` | 无限期状态（Infinite Status）。 |

<a id="ga3cddda628eca248246f9aa3b81938f95"></a>

### `net_if_are_pending_tx_packets()`

```c
bool net_if_are_pending_tx_packets ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

检查给定网络接口是否有待发送的网络数据（Pending TX Network Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值（Returns）：此网络接口存在待发送的网络数据包时为 `true`，否则为 `false`。

<a id="gaaa64aa4391a85760bb2daf600ac4d898"></a>

### `net_if_call_link_cb()`

```c
void net_if_call_link_cb ( struct net_if * iface, struct net_linkaddr * lladdr, int status )
```

```c
#include <zephyr/net/net_if.h>
```

调用链路回调函数（Link Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `lladdr` | 目的链路层地址（Destination Link Layer Address）。 |
| `status` | `0` 表示成功，小于 `0` 表示错误（Error）。 |

<a id="gada944cae018ee13d5478402a850e89e2"></a>

### `net_if_call_timestamp_cb()`

```c
void net_if_call_timestamp_cb ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/net_if.h>
```

调用时间戳回调函数（Timestamp Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络缓冲区（Network Buffer）。 |

<a id="ga6839941422a88c1f707ab70ea34df323"></a>

### `net_if_carrier_off()`

```c
void net_if_carrier_off ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

底层网络设备已失去载波（Carrier），即网线已断开。

相应的网络设备驱动或二层（L2）实现应使用此函数，更新其在网络接口上的状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

<a id="ga35e5db3a631ac9039f14d86e59fc0dcc"></a>

### `net_if_carrier_on()`

```c
void net_if_carrier_on ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

底层网络设备已检测到载波（Carrier），即网线已连接。

相应的网络设备驱动或二层（L2）实现应使用此函数，更新其在网络接口上的状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

<a id="ga3390e248249b28f2c80e2ca0bc79d236"></a>

### `net_if_config_ipv4_get()`

```c
int net_if_config_ipv4_get ( struct net_if * iface, struct net_if_ipv4 ** ipv4 )
```

```c
#include <zephyr/net/net_if.h>
```

分配网络接口的 IPv4 配置（IPv4 Configuration）。

此函数分配新的 IPv4 配置（Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface）。 |
| `ipv4` | 将已分配的 IPv4 结构的指针返回给调用方（Caller）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga88c13a45617480a665c7f9f589ec8e10"></a>

### `net_if_config_ipv4_put()`

```c
int net_if_config_ipv4_put ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

释放网络接口的 IPv4 配置（IPv4 Configuration）。

将配置归还到池（Pool），供其他接口复用。首先移除接口仍持有的全部单播地址、组播地址和路由器，再将配置恢复为默认值。地址移除是强制性的，即便地址仍被引用也会执行，因此调用方必须确保这些地址已不再使用。此过程不发送 IGMP 离组消息（Leave Message），所以必须先关闭接口，再调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga56c9aef19bc9827d9ec96c00e10840fa"></a>

### `net_if_config_ipv6_get()`

```c
int net_if_config_ipv6_get ( struct net_if * iface, struct net_if_ipv6 ** ipv6 )
```

```c
#include <zephyr/net/net_if.h>
```

分配网络接口的 IPv6 配置（IPv6 Configuration）。

此函数分配新的 IPv6 配置（Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface）。 |
| `ipv6` | 将已分配的 IPv6 结构的指针返回给调用方（Caller）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga8af1400b354c42a64795cdb1a600ddd6"></a>

### `net_if_config_ipv6_put()`

```c
int net_if_config_ipv6_put ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

释放网络接口的 IPv6 配置（IPv6 Configuration）。

将配置归还到池（Pool），供其他接口复用。首先移除接口仍持有的全部单播地址、组播地址、前缀和路由器，再将配置恢复为默认值。地址移除是强制性的，即便地址仍被引用也会执行，因此调用方必须确保这些地址已不再使用。此过程不发送 MLD 离组消息（Leave Message），所以必须先关闭接口，再调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga1c31fac887d944ac0a16aad70e889496"></a>

### `net_if_dormant_off()`

```c
void net_if_dormant_off ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

将接口标记为非休眠（Not Dormant）。

相应的网络设备驱动或二层（L2）实现应使用此函数，更新其在网络接口上的状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

<a id="ga89a3374d4bb116460a7b7c50a750b593"></a>

### `net_if_dormant_on()`

```c
void net_if_dormant_on ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

将接口标记为休眠（Dormant）。

暂未就绪状态（Dormant）表示接口尚不能传输数据包，正在等待某个事件，例如 Wi-Fi 网络关联（Association）。

相应的网络设备驱动或二层（L2）实现应使用此函数，更新其在网络接口上的状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

<a id="ga2187650062d6139b9f4b81745a206803"></a>

### `net_if_down()`

```c
int net_if_down ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

停用接口（Bring Interface Down）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

返回（Returns）：成功为0。

<a id="gaff751b6a92b0c608ecfc50e8c0587fd3"></a>

### `net_if_flag_clear()`

```c
void net_if_flag_clear ( struct net_if * iface, enum net_if_flag value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

清除网络接口标志（Network Interface Flags）中的一个值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |
| `value` | 标志值（Flag Value）。 |

<a id="gae1f373ddd61c18a81481d8ddcfb12543"></a>

### `net_if_flag_is_set()`

```c
bool net_if_flag_is_set ( struct net_if * iface, enum net_if_flag value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

检查网络接口标志（Network Interface Flags）中的一个值是否已设置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |
| `value` | 标志值（Flag Value）。 |

**返回（Returns）**：返回值（Returns）：该值已设置时为 `true`，否则为 `false`。

<a id="ga52f9fca13e9f836799e0e40f581744d2"></a>

### `net_if_flag_set()`

```c
void net_if_flag_set ( struct net_if * iface, enum net_if_flag value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置网络接口标志（Network Interface Flags）中的一个值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |
| `value` | 标志值（Flag Value）。 |

<a id="gab8f371c7f8890cf4728177f6595141d7"></a>

### `net_if_flag_test_and_clear()`

```c
bool net_if_flag_test_and_clear ( struct net_if * iface, enum net_if_flag value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

测试并清除网络接口标志（Network Interface Flags）中的一个值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |
| `value` | 标志值（Flag Value）。 |

**返回（Returns）**：如果该位已置位，则返回 true；否则返回 false。

<a id="ga42e7482191a92007960601f8bb621dca"></a>

### `net_if_flag_test_and_set()`

```c
bool net_if_flag_test_and_set ( struct net_if * iface, enum net_if_flag value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

测试并设置网络接口标志（Network Interface Flags）中的一个值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |
| `value` | 标志值（Flag Value）。 |

**返回（Returns）**：如果该位已置位，则返回 true；否则返回 false。

<a id="ga96b198fd9df4a985b0dde84dd7152815"></a>

### `net_if_foreach()`

```c
void net_if_foreach ( net_if_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/net_if.h>
```

遍历全部网络接口（Network Interfaces），并为每个接口调用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

<a id="ga02445f6c61f0d29f56ac0ef59e025630"></a>

### `net_if_get_by_iface()`

```c
int net_if_get_by_iface ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

根据指针（Pointer）获取接口索引（Interface Index）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值（Returns）：接口索引（Interface Index）。

<a id="ga72708cdb7f133fe5d7edf819756c3516"></a>

### `net_if_get_by_index()`

```c
struct net_if * net_if_get_by_index ( int index)
```

```c
#include <zephyr/net/net_if.h>
```

根据索引（Index）获取接口（Interface）。

此函数之所以是系统调用（Syscall），仅为了提供对对象的访问，以便分配权限（Permissions）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 接口索引（Interface index）。 |

**返回（Returns）**：返回值（Returns）：接口的指针；未找到时为 `NULL`。

<a id="ga1b058361dc9bcac7d842bb49846a0c79"></a>

### `net_if_get_by_link_addr()`

```c
struct net_if * net_if_get_by_link_addr ( struct net_linkaddr * ll_addr)
```

```c
#include <zephyr/net/net_if.h>
```

根据链路层地址（Link Layer Address）获取接口（Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ll_addr` | 链路层地址（Link Layer Address）。 |

**返回（Returns）**：返回值（Returns）：网络接口；未找到时为 `NULL`。

<a id="ga1774ac036032bb0dc2c662f6f4f66a7f"></a>

### `net_if_get_by_name()`

```c
int net_if_get_by_name ( const char * name)
```

```c
#include <zephyr/net/net_if.h>
```

根据名称（Name）获取接口索引（Interface Index）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 网络接口名称（Network Interface Name）。 |

**返回（Returns）**：返回值（Returns）：接口索引（Interface Index）。

<a id="gae271e0e4dcb031a83d9908e597a45048"></a>

### `net_if_get_config()`

```c
struct net_if_config * net_if_get_config ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

返回此网络接口（Network Interface）的网络配置（Network Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |

**返回（Returns）**：返回值（Returns）：配置（Configuration）的指针。

<a id="ga55214771e462cbd4930ffa738813cb87"></a>

### `net_if_get_default()`

```c
struct net_if * net_if_get_default ( void )
```

```c
#include <zephyr/net/net_if.h>
```

获取默认网络接口（Default Network Interface）。

**返回（Returns）**：返回值（Returns）：默认接口；未配置任何接口时为 `NULL`。

<a id="gaeb8c703f273bc07ae9bb7a0d8bfe6f3d"></a>

### `net_if_get_device()`

```c
const struct device * net_if_get_device ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取网络接口（Network Interface）对应的设备（Device）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |

**返回（Returns）**：返回值（Returns）：设备驱动实例（Device Driver Instance）的指针。

<a id="ga762337e8b66874a0fbf59bdbeba173f5"></a>

### `net_if_get_first_by_type()`

```c
struct net_if * net_if_get_first_by_type ( const struct net_l2 * l2)
```

```c
#include <zephyr/net/net_if.h>
```

根据类型（Type）获取第一个网络接口（Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `l2` | 网络接口的二层类型（Layer 2 Type）。 |

**返回（Returns）**：返回值（Returns）：指定类型的第一个网络接口；未找到此类接口时为 `NULL`。

<a id="ga529067a284cac1187b336080e56129c8"></a>

### `net_if_get_first_ethernet()`

```c
struct net_if * net_if_get_first_ethernet ( void )
```

```c
#include <zephyr/net/net_if.h>
```

获取第一个有线以太网网络接口（Cabled Ethernet Network Interface）。

**返回（Returns）**：返回值（Returns）：网络接口的指针；未找到时为 `NULL`。

<a id="ga03d8c6aebb1412382a9eec636c227238"></a>

### `net_if_get_first_up()`

```c
struct net_if * net_if_get_first_up ( void )
```

```c
#include <zephyr/net/net_if.h>
```

获取第一个处于启用状态（Up）的网络接口（Network Interface）。

**返回（Returns）**：返回值（Returns）：第一个已启用（Up）的网络接口；全部接口均未启用时为 `NULL`。

<a id="ga6e89bbafb6c0acdc6bf51078e2027236"></a>

### `net_if_get_first_wifi()`

```c
struct net_if * net_if_get_first_wifi ( void )
```

```c
#include <zephyr/net/net_if.h>
```

获取第一个 Wi-Fi 网络接口（Network Interface）。

**返回（Returns）**：返回值（Returns）：网络接口的指针；未找到时为 `NULL`。

<a id="ga467186e964bf721e14fed38392f21872"></a>

### `net_if_get_link_addr()`

```c
struct net_linkaddr * net_if_get_link_addr ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取网络接口的链路地址（Link Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |

**返回（Returns）**：返回值（Returns）：网络链路地址（Network Link Address）的指针。

<a id="gacddc98531c5748db5a34f5c3a3e96e86"></a>

### `net_if_get_mtu()`

```c
uint16_t net_if_get_mtu ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取网络接口的最大传输单元（MTU）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |

**返回（Returns）**：返回值（Returns）：最大传输单元（MTU）。

<a id="ga5f653cd73c1ecd548a931eb7fbd170f7"></a>

### `net_if_get_name()`

```c
int net_if_get_name ( struct net_if * iface, char * buf, int len )
```

```c
#include <zephyr/net/net_if.h>
```

获取网络接口名称（Network Interface Name）。

如果未启用接口名称（Interface Name）支持，则返回空字符串。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |
| `buf` | 用户提供的缓冲区（Buffer）。 |
| `len` | 用户提供的缓冲区长度（Buffer Length）。 |

**返回（Returns）**：返回值（Returns）：复制到 `buf` 的接口名称长度；参数无效时为 `-EINVAL`；无法将名称复制到用户缓冲区时为 `-ERANGE`；接口名称支持被禁用时为 `-ENOTSUP`。

<a id="gaf830eab616191009d88f58b761694b49"></a>

### `net_if_get_wifi_sap()`

```c
struct net_if * net_if_get_wifi_sap ( void )
```

```c
#include <zephyr/net/net_if.h>
```

获取第一个 Wi-Fi 网络软件接入点接口（Soft-AP Interface）。

**返回（Returns）**：返回值（Returns）：网络接口的指针；未找到时为 `NULL`。

<a id="ga0fc3ba6172956f6847027e0bd3d367de"></a>

### `net_if_get_wifi_sta()`

```c
struct net_if * net_if_get_wifi_sta ( void )
```

```c
#include <zephyr/net/net_if.h>
```

获取 Wi-Fi 网络站点接口（Station Interface）。

**返回（Returns）**：返回值（Returns）：网络接口的指针；未找到时为 `NULL`。

<a id="ga8164e6a01a311dcaa593039c90b5d7cb"></a>

### `net_if_ipv4_addr_add()`

```c
struct net_if_addr * net_if_ipv4_addr_add ( struct net_if * iface, const struct net_in_addr * addr, enum net_addr_type addr_type, uint32_t vlifetime )
```

```c
#include <zephyr/net/net_if.h>
```

向接口（Interface）添加 IPv4 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv4地址（Address）。 |
| `addr_type` | IPv4 地址类型（Address Type）。 |
| `vlifetime` | 此地址的有效期（Validity Time）。 |

**返回（Returns）**：返回值（Returns）：接口地址的指针；无法添加时为 `NULL`。

<a id="ga336c5ec3a6af5b03fafc5796c16de396"></a>

### `net_if_ipv4_addr_add_by_index()`

```c
bool net_if_ipv4_addr_add_by_index ( int index, const struct net_in_addr * addr, enum net_addr_type addr_type, uint32_t vlifetime )
```

```c
#include <zephyr/net/net_if.h>
```

通过网络接口索引（Network Interface Index）向接口添加 IPv4 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 网络接口索引（Network interface index）。 |
| `addr` | IPv4地址（Address）。 |
| `addr_type` | IPv4 地址类型（Address Type）。 |
| `vlifetime` | 此地址的有效期（Validity Time）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `true`；无法添加地址时为 `false`。

<a id="gaae71be476e27c178ebb21b0f183c2825"></a>

### `net_if_ipv4_addr_foreach()`

```c
void net_if_ipv4_addr_foreach ( struct net_if * iface, net_if_ip_addr_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/net_if.h>
```

遍历网络接口的全部 IPv4 地址，并对每个正在使用的地址调用回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（Network Interface）的指针。 |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

<a id="ga53fb4ce0130fc8d665ddfd466d2a5eb8"></a>

### `net_if_ipv4_addr_lookup()`

```c
struct net_if_addr * net_if_ipv4_addr_lookup ( const struct net_in_addr * addr, struct net_if ** iface )
```

```c
#include <zephyr/net/net_if.h>
```

检查此 IPv4 地址是否属于某个接口（Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv4地址（Address）。 |
| `iface` | 返回接口（Interface）。 |

**返回（Returns）**：返回值（Returns）：接口地址的指针；未找到时为 `NULL`。

<a id="ga496a33ce937652ff60e437f73590dcd8"></a>

### `net_if_ipv4_addr_lookup_by_iface()`

```c
struct net_if_addr * net_if_ipv4_addr_lookup_by_iface ( struct net_if * iface, const struct net_in_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

检查此 IPv4 地址是否属于这个特定接口（Specific Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值（Returns）：接口地址的指针；未找到时为 `NULL`。

<a id="gae756e33c22b265b0218345cabfc85227"></a>

### `net_if_ipv4_addr_lookup_by_index()`

```c
int net_if_ipv4_addr_lookup_by_index ( const struct net_in_addr * addr)
```

```c
#include <zephyr/net/net_if.h>
```

检查此 IPv4 地址是否属于某个接口索引（Interface Index）对应的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值（Returns）：大于 `0` 表示在给定网络接口索引中找到了地址；其他值均表示未找到。

<a id="ga919149bde5d0f1319ba60a9b8de1a1bc"></a>

### `net_if_ipv4_addr_mask_cmp()`

```c
bool net_if_ipv4_addr_mask_cmp ( struct net_if * iface, const struct net_in_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

检查给定 IPv4 地址是否属于本地子网（Local Subnet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface），必须是有效的接口指针。 |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值（Returns）：地址属于本地子网（Local Subnet）时为 `true`，否则为 `false`。

<a id="ga0f324d39cf60e7babb5a1c4a364a8e86"></a>

### `net_if_ipv4_addr_onlink()`

```c
bool net_if_ipv4_addr_onlink ( struct net_if ** iface, const struct net_in_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

检查此 IPv4 地址是否属于本网络接口的子网（Subnet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface），返回给调用方。`iface` 可以为 `NULL`，此时检查全部接口。 |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值（Returns）：地址属于本地子网（Subnet）时为 `true`，否则为 `false`。

<a id="ga28c3dc1bd0f85710ab3fc8c012183742"></a>

### `net_if_ipv4_addr_rm()`

```c
bool net_if_ipv4_addr_rm ( struct net_if * iface, const struct net_in_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

从接口（Interface）移除 IPv4 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值（Returns）：成功移除时为 `true`，否则为 `false`。

<a id="ga1b27ab5977aa53ce7f01195c76c23b13"></a>

### `net_if_ipv4_addr_rm_by_index()`

```c
bool net_if_ipv4_addr_rm_by_index ( int index, const struct net_in_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

通过接口索引（Interface Index）从接口移除 IPv4 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 网络接口索引（Network interface index）。 |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值（Returns）：成功移除时为 `true`，否则为 `false`。

<a id="ga7648ccab37ffa991f757e6c6a985eec1"></a>

### `net_if_ipv4_get_global_addr()`

```c
struct net_in_addr * net_if_ipv4_get_global_addr ( struct net_if * iface, enum net_addr_state addr_state )
```

```c
#include <zephyr/net/net_if.h>
```

获取处于给定状态的 IPv4 全局地址（Global Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface），必须是有效的接口指针。 |
| `addr_state` | IPv4 地址状态（Address State）：首选（Preferred）、暂定（Tentative）、已弃用（Deprecated）。 |

**返回（Returns）**：返回值（Returns）：链路本地 IPv4 地址（Link-local IPv4 Address）的指针；找不到合适地址时为 `NULL`。

<a id="ga12eee59d98d9891f88ed75fbeb5f4d19"></a>

### `net_if_ipv4_get_gw()`

```c
struct net_in_addr net_if_ipv4_get_gw ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

获取接口的 IPv4 网关（Gateway）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface）。 |

**返回（Returns）**：返回值（Returns）：接口上设置的网关（Gateway）；未找到时返回未指定地址（Unspecified Address）。

<a id="ga6ea398dd6a15e74423fdd55b6a8976f5"></a>

### `net_if_ipv4_get_ll()`

```c
struct net_in_addr * net_if_ipv4_get_ll ( struct net_if * iface, enum net_addr_state addr_state )
```

```c
#include <zephyr/net/net_if.h>
```

获取处于给定状态的 IPv4 链路本地地址（Link Local Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface），必须是有效的接口指针。 |
| `addr_state` | IPv4 地址状态（Address State）：首选（Preferred）、暂定（Tentative）、已弃用（Deprecated）。 |

**返回（Returns）**：返回值（Returns）：链路本地 IPv4 地址（Link-local IPv4 Address）的指针；找不到合适地址时为 `NULL`。

<a id="ga71acb65b1988aab8cca9c9604c86231e"></a>

### `net_if_ipv4_get_mcast_ttl()`

```c
uint8_t net_if_ipv4_get_mcast_ttl ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

获取为给定接口指定的 IPv4 多播生存时间（Multicast Time-to-live）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：生存时间（Time-to-live）。

<a id="gaafc473b7c3f3e32f1ba93dd1f7190fe5"></a>

### `net_if_ipv4_get_netmask_by_addr()`

```c
struct net_in_addr net_if_ipv4_get_netmask_by_addr ( struct net_if * iface, const struct net_in_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

获取与接口某个地址关联的 IPv4 网络掩码（Netmask）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface）。 |
| `addr` | 要检查的 IPv4 地址（Address）。 |

**返回（Returns）**：返回值（Returns）：接口上与给定地址关联的子网掩码（Netmask）；未找到时返回未指定地址（Unspecified Address）。

<a id="ga7e1fd28dbcf1164d056296b4df782e64"></a>

### `net_if_ipv4_get_ttl()`

```c
uint8_t net_if_ipv4_get_ttl ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

获取为给定接口指定的 IPv4 生存时间（Time-to-live）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：生存时间（Time-to-live）。

<a id="ga45774258112186b5989b974df934dff1"></a>

### `net_if_ipv4_is_addr_bcast()`

```c
bool net_if_ipv4_is_addr_bcast ( struct net_if * iface, const struct net_in_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

检查给定的 IPv4 地址是否为广播地址（Broadcast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface），必须是有效的接口指针。 |
| `addr` | IPv4 地址，应采用网络字节序（Network Byte Order）。 |

**返回（Returns）**：返回值：地址为广播地址（Broadcast Address）时为 `true`，否则为 `false`。

<a id="ga720bf6b3a90f747dd345c56d3afc0c13"></a>

### `net_if_ipv4_maddr_add()`

```c
struct net_if_mcast_addr * net_if_ipv4_maddr_add ( struct net_if * iface, const struct net_in_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

向接口（Interface）添加 IPv4 多播地址（Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv4 多播地址（Multicast Address）。 |

**返回（Returns）**：返回值（Returns）：接口组播地址的指针；无法添加时为 `NULL`。

<a id="gae82f53c670f602e9c37b65abb6dfaec7"></a>

### `net_if_ipv4_maddr_foreach()`

```c
void net_if_ipv4_maddr_foreach ( struct net_if * iface, net_if_ip_maddr_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/net_if.h>
```

遍历网络接口的全部 IPv4 多播地址（Multicast Addresses），并对每个正在使用的地址调用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（Network Interface）的指针。 |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

<a id="gaa30769fc8016f1a7496b3ede277d8d8a"></a>

### `net_if_ipv4_maddr_is_joined()`

```c
bool net_if_ipv4_maddr_is_joined ( struct net_if_mcast_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

检查是否已加入（Joined）给定多播地址（Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv4 多播地址（Multicast Address）。 |

**返回（Returns）**：返回值（Returns）：已加入该地址对应的组播组时为 `true`，否则为 `false`。

<a id="gae275a5e75817aa178d36f422573ad76a"></a>

### `net_if_ipv4_maddr_join()`

```c
void net_if_ipv4_maddr_join ( struct net_if * iface, struct net_if_mcast_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

将给定多播地址（Multicast Address）标记为已加入（Joined）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 地址所属的网络接口（Network Interface）。 |
| `addr` | IPv4 多播地址（Multicast Address）。 |

<a id="ga1408fe384736d20f36c035c10007113c"></a>

### `net_if_ipv4_maddr_leave()`

```c
void net_if_ipv4_maddr_leave ( struct net_if * iface, struct net_if_mcast_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

将给定多播地址（Multicast Address）标记为已退出（Left）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 地址所属的网络接口（Network Interface）。 |
| `addr` | IPv4 多播地址（Multicast Address）。 |

<a id="gab6c07d40074298e0e49ed0a8c6a230c1"></a>

### `net_if_ipv4_maddr_lookup()`

```c
struct net_if_mcast_addr * net_if_ipv4_maddr_lookup ( const struct net_in_addr * addr, struct net_if ** iface )
```

```c
#include <zephyr/net/net_if.h>
```

检查此 IPv4 多播地址（Multicast Address）是否属于指定接口或某个接口（Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv4地址（Address）。 |
| `iface` | 如果 `*iface` 为 `NULL`，则返回接口指针；否则必须匹配 `*iface` 的值。 |

**返回（Returns）**：返回值（Returns）：接口组播地址的指针；未找到时为 `NULL`。

<a id="gaa5f133b3999b2d3342707b4a5357d16b"></a>

### `net_if_ipv4_maddr_rm()`

```c
bool net_if_ipv4_maddr_rm ( struct net_if * iface, const struct net_in_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

从接口（Interface）移除 IPv4 多播地址（Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv4 多播地址（Multicast Address）。 |

**返回（Returns）**：返回值（Returns）：成功移除时为 `true`，否则为 `false`。

<a id="ga7f8e34c1001e89d759d3a1e6a5538647"></a>

### `net_if_ipv4_nbr_flush()`

```c
void net_if_ipv4_nbr_flush ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

清空网络接口的 IPv4 邻居缓存（Neighbor Cache）。

移除全部动态学习的邻居（Dynamically Learned Neighbors），使这些对端的链路层地址在下次需要时重新解析。静态添加的条目予以保留；要移除静态条目，请使用 `net_if_ipv4_nbr_rm()`。在以太网链路上，此缓存就是 ARP 缓存；不解析 IPv4 地址的链路层没有需要清空的内容。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface）；为 `NULL` 时清空全部接口。 |

<a id="ga5e676ccb2b0cf22410e595d61d8363ce"></a>

### `net_if_ipv4_nbr_rm()`

```c
bool net_if_ipv4_nbr_rm ( struct net_if * iface, const struct net_in_addr * addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

从 IPv4 邻居缓存（Neighbor Cache）中移除一个邻居（Neighbor）。

与 `net_if_ipv4_nbr_flush()` 不同，此函数也移除静态添加的邻居（Static Neighbor），因此可以用它撤销静态条目。等待该地址解析的所有数据包都会被丢弃。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface）；为 `NULL` 时匹配任意接口。 |
| `addr` | 邻居（Neighbor）的 IPv4 地址。 |

**返回（Returns）**：返回值（Returns）：移除了邻居时为 `true`；原本不存在该邻居时为 `false`。

<a id="gadd50b3a60e8ede04e482b9df8953695d"></a>

### `net_if_ipv4_route_add()`

```c
int net_if_ipv4_route_add ( struct net_if * iface, const struct net_in_addr * addr, uint8_t mask_len, const struct net_in_addr * nexthop, uint32_t lifetime )
```

```c
#include <zephyr/net/net_if.h>
```

向系统路由表（Routing Table）添加 IPv4 路由（Route）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 此路由绑定的网络接口（Network Interface）。 |
| `addr` | 路由的目的 IPv4 地址（Destination IPv4 Address）。 |
| `mask_len` | 目的网络掩码长度（Destination Netmask Length）。 |
| `nexthop` | 下一跳（Next Hop）的 IPv4 地址；对于链路直连路由（On-link Route）为 `NULL`。 |
| `lifetime` | 路由生存期（Route Lifetime），单位为秒；`UINT32_MAX` 表示永不过期。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="ga074030e3dd930630e519a1f26b662be6"></a>

### `net_if_ipv4_router_add()`

```c
struct net_if_router * net_if_ipv4_router_add ( struct net_if * iface, const struct net_in_addr * addr, bool is_default, uint16_t router_lifetime )
```

```c
#include <zephyr/net/net_if.h>
```

向系统添加 IPv4 路由器（Router）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv4地址（Address）。 |
| `is_default` | 此路由器是否为默认路由器（Default Router）。 |
| `router_lifetime` | 路由器生存期（Router Lifetime）；`0` 表示永不过期。 |

**返回（Returns）**：返回值（Returns）：路由器信息的指针；无法添加时为 `NULL`。

<a id="gaffdb60ab8db5de97fc5b568a5be1ee8e"></a>

### `net_if_ipv4_router_find_default()`

```c
struct net_if_router * net_if_ipv4_router_find_default ( struct net_if * iface, const struct net_in_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

查找用于此 IPv4 地址的默认路由器（Default Router）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface）。可以为 `NULL`，此时遍历全部网络接口以寻找合适的路由器。 |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值（Returns）：路由器信息的指针；无法找到时为 `NULL`。

<a id="ga4a290f9bbd65c041e8722b92fe675b77"></a>

### `net_if_ipv4_router_lookup()`

```c
struct net_if_router * net_if_ipv4_router_lookup ( struct net_if * iface, const struct net_in_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

检查该 IPv4 地址是否为系统中已配置路由器（Router）的地址之一。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv4地址（Address）。 |

**返回（Returns）**：返回值（Returns）：路由器信息的指针；无法找到时为 `NULL`。

<a id="ga6be14f5307bc63ce87ff0a3fad7c7f4d"></a>

### `net_if_ipv4_router_rm()`

```c
bool net_if_ipv4_router_rm ( struct net_if_router * router)
```

```c
#include <zephyr/net/net_if.h>
```

从系统移除 IPv4 路由器（Router）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `router` | 路由器信息（Router Information）。 |

**返回（Returns）**：返回值（Returns）：成功移除时为 `true`，否则为 `false`。

<a id="gae7ee369901b43a3bd071dacd3a51049a"></a>

### `net_if_ipv4_select_src_addr()`

```c
const struct net_in_addr * net_if_ipv4_select_src_addr ( struct net_if * iface, const struct net_in_addr * dst )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取向目的地发送网络数据时应使用的 IPv4 源地址（Source Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 发送数据包时使用的接口（Interface）。如果接口未知，可以传入 `NULL`。 |
| `dst` | IPv4 目的地址（Destination Address）。 |

**返回（Returns）**：返回值（Returns）：应使用的 IPv4 地址的指针；无法找到 IPv4 地址时为 `NULL`。

<a id="ga1e66458147628585dd5dd613a68a87a3"></a>

### `net_if_ipv4_select_src_iface()`

```c
struct net_if * net_if_ipv4_select_src_iface ( const struct net_in_addr * dst)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取向目的地发送 IPv4 网络数据时应使用的网络接口（Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | IPv4 目的地址（Destination Address）。 |

**返回（Returns）**：返回值（Returns）：应使用的网络接口的指针；无法找到合适接口时为 `NULL`。

<a id="ga29b73b4d2d18edc06b36f5e5dbcbd441"></a>

### `net_if_ipv4_select_src_iface_addr()`

```c
struct net_if * net_if_ipv4_select_src_iface_addr ( const struct net_in_addr * dst, const struct net_in_addr ** src_addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取向目的地发送 IPv4 网络数据时应使用的网络接口（Network Interface）。

同时返回该网络接口的源 IPv4 地址（Source IPv4 Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | IPv4 目的地址（Destination Address）。 |
| `src_addr` | IPv4 源地址（Source Address）。如果不需要源地址，可以设为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：应使用的网络接口的指针；无法找到合适接口时为 `NULL`。

<a id="ga0826491553b11c764277cde76490eb02"></a>

### `net_if_ipv4_set_gw()`

```c
void net_if_ipv4_set_gw ( struct net_if * iface, const struct net_in_addr * gw )
```

```c
#include <zephyr/net/net_if.h>
```

设置接口的 IPv4 网关（Gateway）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface）。 |
| `gw` | 网关（Gateway）的 IPv4 地址。 |

<a id="ga8810a82cf2b6e3f44541c47c635e39de"></a>

### `net_if_ipv4_set_gw_by_index()`

```c
bool net_if_ipv4_set_gw_by_index ( int index, const struct net_in_addr * gw )
```

```c
#include <zephyr/net/net_if.h>
```

根据接口索引（Interface Index）设置 IPv4 网关（Gateway）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 网络接口索引（Network interface index）。 |
| `gw` | 网关（Gateway）的 IPv4 地址。 |

**返回（Returns）**：返回值（Returns）：添加了网关时为 `true`，否则为 `false`。

<a id="ga9452fef4f1309fb1a53a6a8b4f222377"></a>

### `net_if_ipv4_set_mcast_ttl()`

```c
void net_if_ipv4_set_mcast_ttl ( struct net_if * iface, uint8_t ttl )
```

```c
#include <zephyr/net/net_if.h>
```

设置给定接口的 IPv4 多播生存时间（Multicast Time-to-live）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `ttl` | 生存时间值（Time-to-live Value）。 |

<a id="gaa42af45521841ae8265396c89966a2db"></a>

### `net_if_ipv4_set_netmask_by_addr()`

```c
bool net_if_ipv4_set_netmask_by_addr ( struct net_if * iface, const struct net_in_addr * addr, const struct net_in_addr * netmask )
```

```c
#include <zephyr/net/net_if.h>
```

根据接口索引（Interface Index），为给定地址设置 IPv4 网络掩码（Netmask）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | 与此子网掩码（Netmask）关联的 IPv4 地址。 |
| `netmask` | IPv4 子网掩码（Netmask）。 |

**返回（Returns）**：返回值（Returns）：添加了子网掩码时为 `true`，否则为 `false`。

<a id="gaa5087a91a20e4283b4fa9a09add6aaa0"></a>

### `net_if_ipv4_set_netmask_by_addr_by_index()`

```c
bool net_if_ipv4_set_netmask_by_addr_by_index ( int index, const struct net_in_addr * addr, const struct net_in_addr * netmask )
```

```c
#include <zephyr/net/net_if.h>
```

根据接口索引（Interface Index），为给定地址设置 IPv4 网络掩码（Netmask）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 网络接口索引（Network interface index）。 |
| `addr` | 与此子网掩码（Netmask）关联的 IPv4 地址。 |
| `netmask` | IPv4 子网掩码（Netmask）。 |

**返回（Returns）**：返回值（Returns）：添加了子网掩码时为 `true`，否则为 `false`。

<a id="ga5544374d7ebea26a239d561083f0203d"></a>

### `net_if_ipv4_set_ttl()`

```c
void net_if_ipv4_set_ttl ( struct net_if * iface, uint8_t ttl )
```

```c
#include <zephyr/net/net_if.h>
```

设置给定接口的 IPv4 生存时间（Time-to-live）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `ttl` | 生存时间值（Time-to-live Value）。 |

<a id="ga3b651babfb5d1dd9f8d266d2aa1cf1b8"></a>

### `net_if_ipv6_addr_add()`

```c
struct net_if_addr * net_if_ipv6_addr_add ( struct net_if * iface, const struct net_in6_addr * addr, enum net_addr_type addr_type, uint32_t vlifetime )
```

```c
#include <zephyr/net/net_if.h>
```

向接口（Interface）添加 IPv6 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv6地址（Address）。 |
| `addr_type` | IPv6 地址类型（Address Type）。 |
| `vlifetime` | 此地址的有效期（Validity Time）。 |

**返回（Returns）**：返回值（Returns）：接口地址的指针；无法添加时为 `NULL`。

<a id="gad68f25bd25b198bc4280d334f71495d3"></a>

### `net_if_ipv6_addr_add_by_index()`

```c
bool net_if_ipv6_addr_add_by_index ( int index, const struct net_in6_addr * addr, enum net_addr_type addr_type, uint32_t vlifetime )
```

```c
#include <zephyr/net/net_if.h>
```

通过索引（Index）向接口添加 IPv6 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 网络接口索引（Network interface index）。 |
| `addr` | IPv6地址（Address）。 |
| `addr_type` | IPv6 地址类型（Address Type）。 |
| `vlifetime` | 此地址的有效期（Validity Time）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `true`；无法添加地址时为 `false`。

<a id="ga5ac646ad7fda0fa48e78c15b4ca52d50"></a>

### `net_if_ipv6_addr_foreach()`

```c
void net_if_ipv6_addr_foreach ( struct net_if * iface, net_if_ip_addr_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/net_if.h>
```

遍历网络接口的全部 IPv6 地址，并对每个正在使用的地址调用回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（Network Interface）的指针。 |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

<a id="ga4314c59af790e537e384e969c58fab9d"></a>

### `net_if_ipv6_addr_lookup()`

```c
struct net_if_addr * net_if_ipv6_addr_lookup ( const struct net_in6_addr * addr, struct net_if ** iface )
```

```c
#include <zephyr/net/net_if.h>
```

检查此 IPv6 地址是否属于某个接口（Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |
| `iface` | 返回接口指针（Interface Pointer）。 |

**返回（Returns）**：返回值（Returns）：接口地址的指针；未找到时为 `NULL`。

<a id="gae2935f8b0ad41879b12a491bc260b236"></a>

### `net_if_ipv6_addr_lookup_by_iface()`

```c
struct net_if_addr * net_if_ipv6_addr_lookup_by_iface ( struct net_if * iface, const struct net_in6_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

检查此 IPv6 地址是否属于这个特定接口（Specific Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值（Returns）：接口地址的指针；未找到时为 `NULL`。

<a id="gaaba6b0ba57a19c3d24628e8498ef421d"></a>

### `net_if_ipv6_addr_lookup_by_index()`

```c
int net_if_ipv6_addr_lookup_by_index ( const struct net_in6_addr * addr)
```

```c
#include <zephyr/net/net_if.h>
```

检查此 IPv6 地址是否属于某个接口索引（Interface Index）对应的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值（Returns）：大于 `0` 表示在给定网络接口索引中找到了地址；其他值均表示未找到。

<a id="ga53cc6d8d43f3b3ef7c275dff69b4de8d"></a>

### `net_if_ipv6_addr_onlink()`

```c
bool net_if_ipv6_addr_onlink ( struct net_if ** iface, const struct net_in6_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

检查此 IPv6 地址是否属于本网络接口的子网（Subnet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface），返回给调用方。`iface` 可以为 `NULL`，此时检查全部接口。 |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值（Returns）：地址属于本地子网（Subnet）时为 `true`，否则为 `false`。

<a id="gad0e9473f494d154c4cd89e3e67a13232"></a>

### `net_if_ipv6_addr_rm()`

```c
bool net_if_ipv6_addr_rm ( struct net_if * iface, const struct net_in6_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

从接口（Interface）移除 IPv6 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值（Returns）：成功移除时为 `true`，否则为 `false`。

<a id="gadc08ec8c23d2ee138eb3a05cdfe00701"></a>

### `net_if_ipv6_addr_rm_by_index()`

```c
bool net_if_ipv6_addr_rm_by_index ( int index, const struct net_in6_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

通过索引（Index）从接口移除 IPv6 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 网络接口索引（Network interface index）。 |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值（Returns）：成功移除时为 `true`，否则为 `false`。

<a id="gaef8a6752a201f81636c4ffc1ebba4a25"></a>

### `net_if_ipv6_addr_update_lifetime()`

```c
void net_if_ipv6_addr_update_lifetime ( struct net_if_addr * ifaddr, uint32_t vlifetime )
```

```c
#include <zephyr/net/net_if.h>
```

更新 IPv6 地址的有效生命周期（Valid Lifetime）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ifaddr` | 网络 IPv6 地址（Network IPv6 Address）。 |
| `vlifetime` | 此地址的有效期（Validity Time）。 |

<a id="gab1861b5cefa73b4eefbb447cb1438cdc"></a>

### `net_if_ipv6_calc_reachable_time()`

```c
uint32_t net_if_ipv6_calc_reachable_time ( struct net_if_ipv6 * ipv6)
```

```c
#include <zephyr/net/net_if.h>
```

为 IPv6 可达时间（Reachable Time）计算下一个可达时间值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ipv6` | IPv6 地址配置（Address Configuration）。 |

**返回（Returns）**：返回值（Returns）：可达时间（Reachable Time）。

<a id="ga8f37df9b421963d33a0838fe1fedde2a"></a>

### `net_if_ipv6_dad_failed()`

```c
void net_if_ipv6_dad_failed ( struct net_if * iface, const struct net_in6_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

如果发现本机 IPv6 地址已被使用，则停止 IPv6 重复地址检测（Duplicate Address Detection，DAD）过程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 执行重复地址检测（DAD）的接口。 |
| `addr` | 重复地址检测（DAD）失败的 IPv6 地址。 |

<a id="ga71eb0b9842db6db6930c3567e94d4bd6"></a>

### `net_if_ipv6_get_base_reachable_time()`

```c
uint32_t net_if_ipv6_get_base_reachable_time ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取给定接口的 IPv6 基础可达时间（Base Reachable Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：基础可达时间（Base Reachable Time），单位为毫秒。

<a id="gaf466f15f578d0ab287d8d3a258a64bb3"></a>

### `net_if_ipv6_get_global_addr()`

```c
struct net_in6_addr * net_if_ipv6_get_global_addr ( enum net_addr_state state, struct net_if ** iface )
```

```c
#include <zephyr/net/net_if.h>
```

从第一个具有匹配给定状态的全局 IPv6 地址（Global IPv6 Address）的接口中，返回该全局地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `state` | IPv6 地址状态（Address State）：任意（ANY）、暂定（TENTATIVE）、首选（PREFERRED）、已弃用（DEPRECATED）。 |
| `iface` | 调用方可以指定要检查的接口。如果 `iface` 为 `NULL`，则检查全部接口。将定义了该 IPv6 地址的接口的指针返回给调用方。 |

**返回（Returns）**：返回值（Returns）：IPv6 地址的指针；未找到时为 `NULL`。

<a id="ga66d0a9a8eef095f6d4d44f35dd67f2b6"></a>

### `net_if_ipv6_get_hop_limit()`

```c
uint8_t net_if_ipv6_get_hop_limit ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取为给定接口指定的 IPv6 跳数限制（Hop Limit）。

这是默认值（Default Value），用户可以覆盖。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：跳数限制（Hop Limit）。

<a id="ga76ebc895fb5959f7f4a2884024bb4963"></a>

### `net_if_ipv6_get_ll()`

```c
struct net_in6_addr * net_if_ipv6_get_ll ( struct net_if * iface, enum net_addr_state addr_state )
```

```c
#include <zephyr/net/net_if.h>
```

获取处于给定状态的 IPv6 链路本地地址（Link Local Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface），必须是有效的接口指针。 |
| `addr_state` | IPv6 地址状态（Address State）：首选（Preferred）、暂定（Tentative）、已弃用（Deprecated）。 |

**返回（Returns）**：返回值（Returns）：链路本地 IPv6 地址（Link-local IPv6 Address）的指针；无法找到合适地址时为 `NULL`。

<a id="ga89ea06beb89db41d064b23186c92a567"></a>

### `net_if_ipv6_get_ll_addr()`

```c
struct net_in6_addr * net_if_ipv6_get_ll_addr ( enum net_addr_state state, struct net_if ** iface )
```

```c
#include <zephyr/net/net_if.h>
```

从第一个具有匹配给定状态的链路本地地址（Link Local Address）的接口中，返回该链路本地 IPv6 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `state` | IPv6 地址状态（Address State）：任意（ANY）、暂定（TENTATIVE）、首选（PREFERRED）、已弃用（DEPRECATED）。 |
| `iface` | 返回接口指针（Interface Pointer）。 |

**返回（Returns）**：返回值（Returns）：IPv6 地址的指针；未找到时为 `NULL`。

<a id="ga56e7086633bcf4537f54c7ca70e6c900"></a>

### `net_if_ipv6_get_mcast_hop_limit()`

```c
uint8_t net_if_ipv6_get_mcast_hop_limit ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取为给定接口指定的 IPv6 多播跳数限制（Multicast Hop Limit）。

这是默认值（Default Value），用户可以覆盖。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：跳数限制（Hop Limit）。

<a id="ga9dd1f91edbb519a6a079f363c33efacf"></a>

### `net_if_ipv6_get_reachable_time()`

```c
uint32_t net_if_ipv6_get_reachable_time ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取为给定接口指定的 IPv6 可达超时（Reachable Timeout）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：可达超时（Reachable Timeout）。

<a id="gaddbf5a6ba412e6bdb7e31568fe827bd0"></a>

### `net_if_ipv6_get_retrans_timer()`

```c
uint32_t net_if_ipv6_get_retrans_timer ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取为给定接口指定的 IPv6 重传定时器（Retransmit Timer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：重传定时器（Retransmit Timer）。

<a id="ga1608a77ffca421769bae381a12e179ce"></a>

### `net_if_ipv6_maddr_add()`

```c
struct net_if_mcast_addr * net_if_ipv6_maddr_add ( struct net_if * iface, const struct net_in6_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

向接口（Interface）添加 IPv6 多播地址（Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv6 多播地址（Multicast Address）。 |

**返回（Returns）**：返回值（Returns）：接口组播地址的指针；无法添加时为 `NULL`。

<a id="gab677496fb2e27be2df299a346e9c7132"></a>

### `net_if_ipv6_maddr_foreach()`

```c
void net_if_ipv6_maddr_foreach ( struct net_if * iface, net_if_ip_maddr_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/net_if.h>
```

遍历网络接口的全部 IPv6 多播地址（Multicast Addresses），并对每个正在使用的地址调用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（Network Interface）的指针。 |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

<a id="gabe2c16a378a35a22d008bff9142e5449"></a>

### `net_if_ipv6_maddr_is_joined()`

```c
bool net_if_ipv6_maddr_is_joined ( struct net_if_mcast_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

检查是否已加入（Joined）给定多播地址（Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6 多播地址（Multicast Address）。 |

**返回（Returns）**：返回值（Returns）：已加入该地址对应的组播组时为 `true`，否则为 `false`。

<a id="ga49dbc954015307222f176f4149829b76"></a>

### `net_if_ipv6_maddr_join()`

```c
void net_if_ipv6_maddr_join ( struct net_if * iface, struct net_if_mcast_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

将给定多播地址（Multicast Address）标记为已加入（Joined）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 地址所属的网络接口（Network Interface）。 |
| `addr` | IPv6 多播地址（Multicast Address）。 |

<a id="gad24d5537d52de9781a7a6a55ceedd92b"></a>

### `net_if_ipv6_maddr_leave()`

```c
void net_if_ipv6_maddr_leave ( struct net_if * iface, struct net_if_mcast_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

将给定多播地址（Multicast Address）标记为已退出（Left）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 地址所属的网络接口（Network Interface）。 |
| `addr` | IPv6 多播地址（Multicast Address）。 |

<a id="gad520342d393f523c56a98fa618876b54"></a>

### `net_if_ipv6_maddr_lookup()`

```c
struct net_if_mcast_addr * net_if_ipv6_maddr_lookup ( const struct net_in6_addr * addr, struct net_if ** iface )
```

```c
#include <zephyr/net/net_if.h>
```

检查此 IPv6 多播地址（Multicast Address）是否属于指定接口或某个接口（Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | IPv6地址（Address）。 |
| `iface` | 如果 `*iface` 为 `NULL`，则返回接口指针；否则必须匹配 `*iface` 的值。 |

**返回（Returns）**：返回值（Returns）：接口组播地址的指针；未找到时为 `NULL`。

<a id="ga6c80fd9c864cb54902d52adcb5d8d639"></a>

### `net_if_ipv6_maddr_rm()`

```c
bool net_if_ipv6_maddr_rm ( struct net_if * iface, const struct net_in6_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

从接口（Interface）移除 IPv6 多播地址（Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv6 多播地址（Multicast Address）。 |

**返回（Returns）**：返回值（Returns）：成功移除时为 `true`，否则为 `false`。

<a id="gaaa6c3d31d3a40cab6cf9e4f4af959b89"></a>

### `net_if_ipv6_nbr_flush()`

```c
void net_if_ipv6_nbr_flush ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

清空网络接口的 IPv6 邻居缓存（Neighbor Cache）。

移除全部动态学习的邻居（Dynamically Learned Neighbors），使这些对端的链路层地址在下次需要时重新解析。静态添加的条目予以保留；要移除静态条目，请使用 `net_if_ipv6_nbr_rm()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface）；为 `NULL` 时清空全部接口。 |

<a id="gac6bc061b5b0facc5023da2a835fb9bb3"></a>

### `net_if_ipv6_nbr_rm()`

```c
bool net_if_ipv6_nbr_rm ( struct net_if * iface, const struct net_in6_addr * addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

从 IPv6 邻居缓存（Neighbor Cache）中移除一个邻居（Neighbor）。

与 `net_if_ipv6_nbr_flush()` 不同，此函数也移除静态添加的邻居（Static Neighbor），因此可以用它撤销静态条目。等待该地址解析的所有数据包都会被丢弃。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface）；为 `NULL` 时匹配任意接口。 |
| `addr` | 邻居（Neighbor）的 IPv6 地址。 |

**返回（Returns）**：返回值（Returns）：移除了邻居时为 `true`；原本不存在该邻居时为 `false`。

<a id="ga2616868a6d51cbf1d35c6920e258d412"></a>

### `net_if_ipv6_prefix_add()`

```c
struct net_if_ipv6_prefix * net_if_ipv6_prefix_add ( struct net_if * iface, const struct net_in6_addr * prefix, uint8_t len, uint32_t lifetime )
```

```c
#include <zephyr/net/net_if.h>
```

向网络接口（Network Interface）添加 IPv6 前缀（Prefix）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `prefix` | IPv6地址（Address）。 |
| `len` | 前缀长度（Prefix length）。 |
| `lifetime` | 前缀生存期（Prefix Lifetime），单位为秒。 |

**返回（Returns）**：返回值（Returns）：前缀的指针；未能添加前缀时为 `NULL`。

<a id="ga9c10341ab913f0b609c2724354ec587a"></a>

### `net_if_ipv6_prefix_get()`

```c
struct net_if_ipv6_prefix * net_if_ipv6_prefix_get ( struct net_if * iface, const struct net_in6_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

返回与此 IPv6 地址对应的前缀（Prefix）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值（Returns）：前缀的指针；未找到时为 `NULL`。

<a id="ga99b22d24fef63bd1681396410b930008"></a>

### `net_if_ipv6_prefix_lookup()`

```c
struct net_if_ipv6_prefix * net_if_ipv6_prefix_lookup ( struct net_if * iface, const struct net_in6_addr * addr, uint8_t len )
```

```c
#include <zephyr/net/net_if.h>
```

检查此 IPv6 前缀（Prefix）是否属于该接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv6地址（Address）。 |
| `len` | 前缀长度（Prefix length）。 |

**返回（Returns）**：返回值（Returns）：前缀的指针；未找到时为 `NULL`。

<a id="ga4b8668b32a14996c68d10ec989c1abb3"></a>

### `net_if_ipv6_prefix_rm()`

```c
bool net_if_ipv6_prefix_rm ( struct net_if * iface, const struct net_in6_addr * addr, uint8_t len )
```

```c
#include <zephyr/net/net_if.h>
```

从接口（Interface）移除 IPv6 前缀（Prefix）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv6 前缀地址（Prefix Address）。 |
| `len` | 前缀长度（Prefix length）。 |

**返回（Returns）**：返回值（Returns）：成功移除时为 `true`，否则为 `false`。

<a id="ga9ff61003d36ee19af27a9b1b24b22170"></a>

### `net_if_ipv6_prefix_set_advertise()`

```c
int net_if_ipv6_prefix_set_advertise ( struct net_if * iface, const struct net_in6_addr * prefix, uint8_t len, bool advertise )
```

```c
#include <zephyr/net/net_if.h>
```

标记或取消标记一个 IPv6 前缀（Prefix），决定是否在该接口发送的路由器通告（Router Advertisements）中通告此前缀。

必须先通过 `net_if_ipv6_router_start()` 将接口设置为路由器，才能发送通告（Advertisements）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `prefix` | IPv6 前缀地址（Prefix Address）。 |
| `len` | 前缀长度（Prefix length）。 |
| `advertise` | `true` 表示通告前缀（Advertise Prefix），`false` 表示停止通告。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="gaa3c711e814fb6a4e552b4ef723d0baa0"></a>

### `net_if_ipv6_prefix_set_lf()`

```c
void net_if_ipv6_prefix_set_lf ( struct net_if_ipv6_prefix * prefix, bool is_infinite )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置前缀（Prefix）的无限有效状态（Infinite Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prefix` | IPv6地址（Address）。 |
| `is_infinite` | 无限期状态（Infinite Status）。 |

<a id="ga68cffe343c518bad7f7f152e30f7f9ee"></a>

### `net_if_ipv6_prefix_set_timer()`

```c
void net_if_ipv6_prefix_set_timer ( struct net_if_ipv6_prefix * prefix, uint32_t lifetime )
```

```c
#include <zephyr/net/net_if.h>
```

设置前缀生命周期定时器（Prefix Lifetime Timer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prefix` | IPv6地址（Address）。 |
| `lifetime` | 前缀生存期（Prefix Lifetime），单位为秒。 |

<a id="ga2d68cb6dcfcffd3f87bbfb3dfce791ff"></a>

### `net_if_ipv6_prefix_unset_timer()`

```c
void net_if_ipv6_prefix_unset_timer ( struct net_if_ipv6_prefix * prefix)
```

```c
#include <zephyr/net/net_if.h>
```

取消前缀生命周期定时器（Prefix Lifetime Timer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prefix` | IPv6地址（Address）。 |

<a id="ga8d80080463bcb9035e06e0ac35090780"></a>

### `net_if_ipv6_router_add()`

```c
struct net_if_router * net_if_ipv6_router_add ( struct net_if * iface, const struct net_in6_addr * addr, bool is_default, uint16_t router_lifetime )
```

```c
#include <zephyr/net/net_if.h>
```

向系统添加 IPv6 路由器（Router）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv6地址（Address）。 |
| `is_default` | 此路由器是否为默认路由器（Default Router）。 |
| `router_lifetime` | 路由器生存期（Router Lifetime）；`0` 表示永不过期。 |

**返回（Returns）**：返回值（Returns）：路由器信息的指针；无法添加时为 `NULL`。

<a id="gabfabdb7afa073b54f67d67320da3983c"></a>

### `net_if_ipv6_router_find_default()`

```c
struct net_if_router * net_if_ipv6_router_find_default ( struct net_if * iface, const struct net_in6_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

查找用于此 IPv6 地址的默认路由器（Default Router）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface）。可以为 `NULL`，此时遍历全部网络接口以寻找合适的路由器。 |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值（Returns）：路由器信息的指针；无法找到时为 `NULL`。

<a id="gac68a72e70b5335773964dbfc0319eee5"></a>

### `net_if_ipv6_router_lookup()`

```c
struct net_if_router * net_if_ipv6_router_lookup ( struct net_if * iface, const struct net_in6_addr * addr )
```

```c
#include <zephyr/net/net_if.h>
```

检查该 IPv6 地址是否为系统中已配置路由器（Router）的地址之一。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | IPv6地址（Address）。 |

**返回（Returns）**：返回值（Returns）：路由器信息的指针；无法找到时为 `NULL`。

<a id="ga1d108aa0b54c072e0aa9d0c049f02807"></a>

### `net_if_ipv6_router_rm()`

```c
bool net_if_ipv6_router_rm ( struct net_if_router * router)
```

```c
#include <zephyr/net/net_if.h>
```

从系统移除 IPv6 路由器（Router）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `router` | 路由器信息（Router Information）。 |

**返回（Returns）**：返回值（Returns）：成功移除时为 `true`，否则为 `false`。

<a id="ga1c062890f66b97dbb723339fede121ff"></a>

### `net_if_ipv6_router_start()`

```c
int net_if_ipv6_router_start ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

启用接口的 IPv6 路由器角色（Router Role）。

启用后，接口响应收到的路由器请求（Router Solicitation），并定期发送非请求的路由器通告（Unsolicited Router Advertisement）。对于每个标记为需要通告的前缀，通告包含一个前缀信息选项（Prefix Information Option），参见 `net_if_ipv6_prefix_set_advertise()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="gaa56d3dbc96301e6fa70ee61b08c29841"></a>

### `net_if_ipv6_router_stop()`

```c
int net_if_ipv6_router_stop ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

禁用接口的 IPv6 路由器角色（Router Role）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。

<a id="gaadba4957802dc376ef011590c91c6af6"></a>

### `net_if_ipv6_router_update_lifetime()`

```c
void net_if_ipv6_router_update_lifetime ( struct net_if_router * router, uint16_t lifetime )
```

```c
#include <zephyr/net/net_if.h>
```

更新路由器（Router）的有效生命周期（Valid Lifetime）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `router` | 网络 IPv6 地址（Network IPv6 Address）。 |
| `lifetime` | 此路由器的生存期（Lifetime）。 |

<a id="ga5f8fc8725d3050a0e8fb0c3c75791c7c"></a>

### `net_if_ipv6_select_src_addr()`

```c
const struct net_in6_addr * net_if_ipv6_select_src_addr ( struct net_if * iface, const struct net_in6_addr * dst )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取向目的地发送网络数据时应使用的 IPv6 源地址（Source Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 接收数据包时使用的接口（Interface）。如果接口未知，可以传入 `NULL`。 |
| `dst` | IPv6 目的地址（Destination Address）。 |

**返回（Returns）**：返回值（Returns）：应使用的 IPv6 地址的指针；无法找到 IPv6 地址时为 `NULL`。

<a id="ga55df4f4967efb4840dbee7a4078a237b"></a>

### `net_if_ipv6_select_src_addr_hint()`

```c
const struct net_in6_addr * net_if_ipv6_select_src_addr_hint ( struct net_if * iface, const struct net_in6_addr * dst, int flags )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取向目的地发送网络数据时应使用的 IPv6 源地址（Source Address）。

使用为套接字（Socket）设置的提示，选择适当地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 接收数据包时使用的接口（Interface）。如果接口未知，可以传入 `NULL`。 |
| `dst` | IPv6 目的地址（Destination Address）。 |
| `flags` | 来自相关套接字的提示（Hint）。具体取值参见 RFC 5014。 |

**返回（Returns）**：返回值（Returns）：应使用的 IPv6 地址的指针；无法找到 IPv6 地址时为 `NULL`。

<a id="ga367c74aad10b58074e5e1e517d6be379"></a>

### `net_if_ipv6_select_src_iface()`

```c
struct net_if * net_if_ipv6_select_src_iface ( const struct net_in6_addr * dst)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取向目的地发送 IPv6 网络数据时应使用的网络接口（Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | IPv6 目的地址（Destination Address）。 |

**返回（Returns）**：返回值（Returns）：应使用的网络接口的指针；无法找到合适接口时为 `NULL`。

<a id="ga8c3fe8f29294c8bb9561d22625cf726c"></a>

### `net_if_ipv6_select_src_iface_addr()`

```c
struct net_if * net_if_ipv6_select_src_iface_addr ( const struct net_in6_addr * dst, const struct net_in6_addr ** src_addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取向目的地发送 IPv6 网络数据时应使用的网络接口（Network Interface）。

同时返回该网络接口的源 IPv6 地址（Source IPv6 Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | IPv6 目的地址（Destination Address）。 |
| `src_addr` | IPv6 源地址（Source Address）。如果不需要源地址，可以设为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：应使用的网络接口的指针；无法找到合适接口时为 `NULL`。

<a id="gab3939d735b660f8f02124df656ceba2c"></a>

### `net_if_ipv6_set_base_reachable_time()`

```c
void net_if_ipv6_set_base_reachable_time ( struct net_if * iface, uint32_t reachable_time )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置给定接口的 IPv6 可达时间（Reachable Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `reachable_time` | 新的可达时间（Reachable Time）。超过 `NET_IPV6_MAX_REACHABLE_TIME` 的值会被限制到此上限。 |

<a id="ga5bf726bb5c1d232103ec6841e7d0cd8c"></a>

### `net_if_ipv6_set_hop_limit()`

```c
void net_if_ipv6_set_hop_limit ( struct net_if * iface, uint8_t hop_limit )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置给定接口的默认 IPv6 跳数限制（Hop Limit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `hop_limit` | 新的跳数限制（Hop Limit）。 |

<a id="gaf56a433679ea9701cf8baa3208f8ccc3"></a>

### `net_if_ipv6_set_mcast_hop_limit()`

```c
void net_if_ipv6_set_mcast_hop_limit ( struct net_if * iface, uint8_t hop_limit )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置给定接口的默认 IPv6 多播跳数限制（Multicast Hop Limit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `hop_limit` | 新的跳数限制（Hop Limit）。 |

<a id="ga8328266b870fd200660cb2becaab3de4"></a>

### `net_if_ipv6_set_reachable_time()`

```c
void net_if_ipv6_set_reachable_time ( struct net_if_ipv6 * ipv6)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置给定接口的 IPv6 可达时间（Reachable Time）。

这要求已经为接口设置基础可达时间（Base Reachable Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ipv6` | IPv6 地址配置（Address Configuration）。 |

<a id="gad74566e5a34f447d2ac63d2c0e82eeff"></a>

### `net_if_ipv6_set_retrans_timer()`

```c
void net_if_ipv6_set_retrans_timer ( struct net_if * iface, uint32_t retrans_timer )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置给定接口的 IPv6 重传定时器（Retransmit Timer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `retrans_timer` | 新的重传定时器（Retransmit Timer）。 |

<a id="ga099a484a654ad9af35d3212fc2c995b2"></a>

### `net_if_is_admin_up()`

```c
bool net_if_is_admin_up ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

检查接口是否已由管理员启用（Brought Up by the Administrator）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值（Returns）：接口处于管理启用状态（Admin Up）时为 `true`，否则为 `false`。

<a id="ga095554237016e563d76cfd602d1dae77"></a>

### `net_if_is_carrier_ok()`

```c
bool net_if_is_carrier_ok ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

检查网络设备是否存在载波（Carrier）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值（Returns）：存在载波（Carrier）时为 `true`，否则为 `false`。

<a id="ga6e2e6102271c37acaa59c54e2aa6b413"></a>

### `net_if_is_dormant()`

```c
bool net_if_is_dormant ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

检查接口是否处于休眠状态（Dormant）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值（Returns）：接口处于暂未就绪状态（Dormant）时为 `true`，否则为 `false`。

<a id="ga703d9e3c128a3a3f0e452d789a4b7bf6"></a>

### `net_if_is_ethernet()`

```c
bool net_if_is_ethernet ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

检查网络接口是否为有线以太网（Cabled Ethernet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值（Returns）：接口为有线以太网（Cabled Ethernet）时为 `true`，否则为 `false`。

<a id="ga6bfa5f84a2127bbad27a0a3b319526a1"></a>

### `net_if_is_ip_offloaded()`

```c
bool net_if_is_ip_offloaded ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

返回 IP 卸载状态（IP Offload Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：IP 卸载（IP Offloading）处于活动状态时为 `true`，否则为 `false`。

<a id="gaecedc93a6dab2c57fe686718ea4d78af"></a>

### `net_if_is_offloaded()`

```c
bool net_if_is_offloaded ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

返回给定网络接口（Network Interface）的卸载状态（Offload Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：IP 卸载或套接字卸载（Socket Offloading）处于活动状态时为 `true`，否则为 `false`。

<a id="ga9f1a6eab849517734ec422deb0ba71f5"></a>

### `net_if_is_promisc()`

```c
bool net_if_is_promisc ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

检查是否设置了混杂模式（Promiscuous Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值（Returns）：接口处于混杂模式（Promiscuous Mode）时为 `true`，否则为 `false`。

<a id="gaf308baf2241fa455b50b439b7fab3f1e"></a>

### `net_if_is_socket_offloaded()`

```c
bool net_if_is_socket_offloaded ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

返回套接字卸载状态（Socket Offload Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：套接字卸载（Socket Offloading）处于活动状态时为 `true`，否则为 `false`。

<a id="ga7e9b368d4abf9da5656140df70cfa334"></a>

### `net_if_is_up()`

```c
bool net_if_is_up ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

检查接口是否已启用且正在运行（Up and Running）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值（Returns）：接口已启用（Up）时为 `true`，未启用（Down）时为 `false`。

<a id="gaa458b5f349c55007108b47b99f4954d5"></a>

### `net_if_is_wifi()`

```c
bool net_if_is_wifi ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

检查网络接口是否支持 Wi-Fi。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值：接口支持 Wi-Fi 时为 true，否则为 false。

<a id="gafa451f6118529d1d084704d00b2aae20"></a>

### `net_if_l2()`

```c
const struct net_l2 * net_if_l2 ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取指向接口链路层（Interface L2）的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：接口二层（L2）的指针。

<a id="ga3cad2d51fc9cc225619585e06e252db0"></a>

### `net_if_l2_data()`

```c
void * net_if_l2_data ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取指向接口链路层私有数据（Interface L2 Private Data）的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：接口二层数据（L2 Data）的指针。

<a id="gadbb8be32caa896bdcdeee19425134827"></a>

### `net_if_lookup_by_dev()`

```c
struct net_if * net_if_lookup_by_dev ( const struct device * dev)
```

```c
#include <zephyr/net/net_if.h>
```

根据关联的设备（Device）查找接口（Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 有效的 `struct device` 指针，用于与接口建立关联。 |

**返回（Returns）**：返回值（Returns）：成功时为有效的 `struct net_if` 指针，否则为 `NULL`。

<a id="ga8fdd0665ed76db6055777e395ca60255"></a>

### `net_if_mcast_mon_register()`

```c
void net_if_mcast_mon_register ( struct net_if_mcast_monitor * mon, struct net_if * iface, net_if_mcast_callback_t cb )
```

```c
#include <zephyr/net/net_if.h>
```

注册多播监视器（Multicast Monitor）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 监视器句柄（Monitor Handle），即指向监视器存储结构的指针。该结构应由调用方分配，但不必初始化。 |
| `iface` | 网络接口（Network Interface）；为 `NULL` 时表示全部接口。 |
| `cb` | 监视器回调（Monitor Callback）。 |

<a id="gad323732fe3d178a5dfdf0900e5cb5683"></a>

### `net_if_mcast_mon_unregister()`

```c
void net_if_mcast_mon_unregister ( struct net_if_mcast_monitor * mon)
```

```c
#include <zephyr/net/net_if.h>
```

注销多播监视器（Multicast Monitor）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mon` | 监视器句柄（Monitor Handle）。 |

<a id="ga372ef131263269cd65586d87997df745"></a>

### `net_if_mcast_monitor()`

```c
void net_if_mcast_monitor ( struct net_if * iface, const struct net_addr * addr, bool is_joined )
```

```c
#include <zephyr/net/net_if.h>
```

调用已注册的多播监视器（Multicast Monitors）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | 组播地址（Multicast Address）。 |
| `is_joined` | 是否已加入此组播地址对应的组：`true` 表示已加入（Joined），`false` 表示未加入。 |

<a id="ga655599b1432463455610cff768997e2b"></a>

### `net_if_nbr_reachability_hint()`

```c
void net_if_nbr_reachability_hint ( struct net_if * iface, const struct net_in6_addr * ipv6_addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

为 IPv6 邻居发现（Neighbor Discovery）提供可达性提示（Reachability Hint）。

此函数供上层协议向 IPv6 邻居发现（Neighbor Discovery，ND）过程通知与指定邻居之间的活动链路。通过报告近期的“前向进展”（Forward Progress）事件，例如收到 ACK，可按 RFC 4861 第 7.3 节的指导减少不必要的 ND 流量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（Network Interface）的指针。 |
| `ipv6_addr` | 指向邻居节点 IPv6 地址的指针（Pointer）。 |

<a id="gac040bd7860e5cd6424709fbf98dd4a99"></a>

### `net_if_need_calc_rx_checksum()`

```c
bool net_if_need_calc_rx_checksum ( struct net_if * iface, enum net_if_checksum_type chksum_type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

检查是否可以省略接收网络数据包的校验和计算（Checksum Calculation）。

例如，许多以太网设备支持网络数据包卸载（Network Packet Offloading），此时 IP 协议栈无需计算校验和。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `chksum_type` | 需要计算校验和的三层和／或四层协议（L3/L4 Protocol）。 |

**返回（Returns）**：返回值（Returns）：需要计算校验和时为 `true`，否则为 `false`。

<a id="ga0db8854bb77133b19c5b0852b43119bb"></a>

### `net_if_need_calc_tx_checksum()`

```c
bool net_if_need_calc_tx_checksum ( struct net_if * iface, enum net_if_checksum_type chksum_type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

检查发送网络数据包时是否可以省略校验和计算（Checksum Calculation）。

例如，许多以太网设备支持网络数据包卸载（Network Packet Offloading），此时 IP 协议栈无需计算校验和。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `chksum_type` | 需要计算校验和的三层和／或四层协议（L3/L4 Protocol）。 |

**返回（Returns）**：返回值（Returns）：需要计算校验和时为 `true`，否则为 `false`。

<a id="ga520939e94620ca75475a71f153df6d4a"></a>

### `net_if_offload()`

```c
struct net_offload * net_if_offload ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

返回 IP 卸载插件（IP Offload Plugin）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：未定义卸载插件（Offload Plugin）时为 `NULL`，否则为有效指针。

<a id="gaf2d323c1504125fbfde5da9ada8c5657"></a>

### `net_if_offload_set()`

```c
void net_if_offload_set ( struct net_if * iface, struct net_offload * offload )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置 IP 卸载插件（IP Offload Plugin）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `offload` | 要设置的卸载插件（Offload Plugin）。 |

<a id="gad9e957a4866b4566296ee39392fde0e4"></a>

### `net_if_oper_state()`

```c
enum net_if_oper_state net_if_oper_state ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取接口的运行状态（Operational State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值（Returns）：接口的运行状态（Operational State）。

<a id="gabae216ba527bdfcd945ef19fb48e56be"></a>

### `net_if_oper_state_change_time()`

```c
int net_if_oper_state_change_time ( struct net_if * iface, int64_t * change_time )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取接口运行状态的变化时间（Operational State Change Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |
| `change_time` | 用于保存状态变更时间的指针。该时间表示接口运行状态（Operational State）上次改变时，自启动以来经过的毫秒数。如果接口运行状态尚未发生改变，则值为 `0`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；无法获取运行状态变更时间时为 `-EINVAL`，例如 `iface` 或 `change_time` 为 `NULL`。

<a id="ga1f1bf845e63cce02e2183889cc85d57e"></a>

### `net_if_oper_state_set()`

```c
enum net_if_oper_state net_if_oper_state_set ( struct net_if * iface, enum net_if_oper_state oper_state )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置接口的运行状态（Operational State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |
| `oper_state` | 要设置的运行状态（Operational State）。 |

**返回（Returns）**：返回值（Returns）：接口的新运行状态（Operational State）。

<a id="ga2ac749d465ef7f0f64f294a30310457e"></a>

### `net_if_queue_tx()`

```c
void net_if_queue_tx ( struct net_if * iface, struct net_pkt * pkt )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

将数据包（Packet）加入网络接口发送队列（TX Queue）。

等价于使用无限超时（Infinite Timeout）调用 `net_if_try_queue_tx`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |
| `pkt` | 指向要加入队列的网络数据包（Network Packet）的指针。 |

<a id="ga72ed21ca0cb220199f5a2070137c7fef"></a>

### `net_if_recv_data()`

```c
enum net_verdict net_if_recv_data ( struct net_if * iface, struct net_pkt * pkt )
```

```c
#include <zephyr/net/net_if.h>
```

通过网络接口（Net Interface）输入数据包（Packet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |
| `pkt` | 指向要输入的网络数据包（Network Packet）的指针。 |

**返回（Returns）**：返回值（Returns）：对该数据包的处理裁定（Verdict）。

<a id="gaa81b7d9ed8dc05da3391265dbc89b665"></a>

### `net_if_register_link_cb()`

```c
void net_if_register_link_cb ( struct net_if_link_cb * link, net_if_link_callback_t cb )
```

```c
#include <zephyr/net/net_if.h>
```

注册链路回调（Link Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `link` | 调用方指定的回调处理函数（Callback Handler）。 |
| `cb` | 要注册的回调（Callback）。 |

<a id="ga198accbfeaeb049eba9ffa2fac82c747"></a>

### `net_if_register_timestamp_cb()`

```c
void net_if_register_timestamp_cb ( struct net_if_timestamp_cb * handle, struct net_pkt * pkt, struct net_if * iface, net_if_timestamp_callback_t cb )
```

```c
#include <zephyr/net/net_if.h>
```

注册时间戳回调（Timestamp Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 调用方指定的回调处理函数（Callback Handler）。 |
| `pkt` | 为其注册回调的网络数据包（Network Packet）；`NULL` 表示全部数据包。 |
| `iface` | 回调对应的网络接口（Network Interface）；`NULL` 表示全部接口。 |
| `cb` | 要注册的回调（Callback）。 |

<a id="ga4ce8f0f7d00b66b905ee9cf1a8b398c6"></a>

### `net_if_router_ipv4()`

```c
struct net_in_addr * net_if_router_ipv4 ( struct net_if_router * router)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取给定路由器（Router）的 IPv4 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `router` | 网络路由器（Network Router）。 |

**返回（Returns）**：返回值（Returns）：IPv4 地址的指针；不存在时为 `NULL`。

<a id="ga17d846ec0cbc1e67fd4a2bc1179b7c45"></a>

### `net_if_router_ipv6()`

```c
struct net_in6_addr * net_if_router_ipv6 ( struct net_if_router * router)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

获取给定路由器（Router）的 IPv6 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `router` | 网络路由器（Network Router）。 |

**返回（Returns）**：返回值（Returns）：IPv6 地址的指针；不存在时为 `NULL`。

<a id="gadc87242eb7205362a308b3c4437bf76d"></a>

### `net_if_router_rm()`

```c
void net_if_router_rm ( struct net_if_router * router)
```

```c
#include <zephyr/net/net_if.h>
```

从系统中移除路由器（Router）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `router` | 指向现有路由器（Router）的指针。 |

<a id="gab3c666bf6a0677c25e90082fed88f7a5"></a>

### `net_if_select_src_iface()`

```c
struct net_if * net_if_select_src_iface ( const struct net_sockaddr * dst)
```

```c
#include <zephyr/net/net_if.h>
```

获取向目的地发送 IPv6 或 IPv4 网络数据时应使用的网络接口（Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | IPv6 或 IPv4 目的地址（Destination Address）。 |

**返回（Returns）**：返回值（Returns）：应使用的网络接口的指针。注意，如果找不到最佳网络接口，此函数返回默认网络接口（Default Network Interface）。

<a id="ga84a58403183b88c64fda59d5d2d903fc"></a>

### `net_if_send_data()`

```c
enum net_verdict net_if_send_data ( struct net_if * iface, struct net_pkt * pkt )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

通过网络接口（Net Interface）发送数据包（Packet）。

等价于使用无限超时（Infinite Timeout）调用 `net_if_try_send_data`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |
| `pkt` | 指向待发送的网络数据包（Network Packet）的指针。 |

**返回（Returns）**：返回值（Returns）：对该数据包的处理裁定（Verdict）。

<a id="ga0a1f27ec893e1af3c97f130be4616589"></a>

### `net_if_set_default()`

```c
void net_if_set_default ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

设置默认网络接口（Default Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 新的默认接口（Default Interface）；`NULL` 表示恢复使用 Kconfig 所设置的接口。 |

<a id="ga3863e011f89dff02c3df3ca4a88680e9"></a>

### `net_if_set_link_addr()`

```c
int net_if_set_link_addr ( struct net_if * iface, const uint8_t * addr, uint8_t len, enum net_link_type type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置网络接口的链路地址（Link Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |
| `addr` | 指向表示地址的 `uint8_t` 缓冲区的指针（Pointer）。 |
| `len` | 地址缓冲区长度（Address Buffer Length）。 |
| `type` | 此链路地址的网络承载类型（Network Bearer Type）。 |

返回（Returns）：成功为0。

<a id="ga76b140c6fc39b94ff4102e08e3a58e81"></a>

### `net_if_set_mtu()`

```c
void net_if_set_mtu ( struct net_if * iface, uint16_t mtu )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置网络接口的最大传输单元（MTU）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |
| `mtu` | 新的最大传输单元（MTU）；注意，只存储 16 位的 MTU 值。 |

<a id="ga05dec64966fc39e3deb0679b9585688b"></a>

### `net_if_set_name()`

```c
int net_if_set_name ( struct net_if * iface, const char * buf )
```

```c
#include <zephyr/net/net_if.h>
```

设置网络接口名称（Network Interface Name）。

通常无需调用此函数，因为系统会自动为网络接口分配名称（Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |
| `buf` | 用户提供的名称（Name）。 |

**返回（Returns）**：返回值（Returns）：正确设置名称时为 `0`；接口名称支持被禁用时为 `-ENOTSUP`；参数无效时为 `-EINVAL`；名称过长时为 `-ENAMETOOLONG`。

<a id="gaf9f81f3b9697ca47f7674d85f37a8d80"></a>

### `net_if_set_promisc()`

```c
int net_if_set_promisc ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

将网络接口设为混杂模式（Promiscuous Mode）。

注意，并非所有网络技术（Network Technologies）都支持此功能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时小于 `0`。

<a id="gafb2bbaec96c4759d920b2866c0b3ef3a"></a>

### `net_if_socket_offload()`

```c
net_socket_create_t net_if_socket_offload ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

返回创建卸载套接字（Offloaded Socket）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：接口不采用套接字卸载（Socket Offloading）时为 `NULL`，否则为有效指针。

<a id="ga9db52875580115c743b1f35cd6c46796"></a>

### `net_if_socket_offload_set()`

```c
void net_if_socket_offload_set ( struct net_if * iface, net_socket_create_t socket_offload )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

设置创建卸载套接字（Offloaded Socket）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `socket_offload` | 用于创建卸载套接字（Offloaded Socket）的函数。 |

<a id="ga9655c010ccbf989e9328271f5dbcc685"></a>

### `net_if_start_dad()`

```c
void net_if_start_dad ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

启动重复地址检测过程（Duplicate Address Detection Procedure）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |

<a id="gab9bdb7f8a9eeed4d9b70965b8af82cb7"></a>

### `net_if_start_rs()`

```c
void net_if_start_rs ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

启动邻居发现（Neighbor Discovery），并发送路由器请求消息（Router Solicitation Message）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |

<a id="gab0195bb2151a1ba722a0b11d81066988"></a>

### `net_if_stop_rs()`

```c
void net_if_stop_rs ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

停止邻居发现（Neighbor Discovery）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |

<a id="ga3617cd1f712b8a85fdd7f1425254ae5d"></a>

### `net_if_try_queue_tx()`

```c
void net_if_try_queue_tx ( struct net_if * iface, struct net_pkt * pkt, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_if.h>
```

尝试将数据包（Packet）加入网络接口发送队列（TX Queue）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |
| `pkt` | 指向要加入队列的网络数据包（Network Packet）的指针。 |
| `timeout` | 尝试入队的超时时间（Enqueuing Timeout）。 |

<a id="ga5d01d7fa6c7511d68933ad4cec032d8a"></a>

### `net_if_try_send_data()`

```c
enum net_verdict net_if_try_send_data ( struct net_if * iface, struct net_pkt * pkt, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_if.h>
```

尝试通过网络接口（Net Interface）发送数据包（Packet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口结构（Network Interface Structure）的指针。 |
| `pkt` | 指向待发送的网络数据包（Network Packet）的指针。 |
| `timeout` | 尝试发送的超时时间（Send Timeout）。 |

**返回（Returns）**：返回值（Returns）：对该数据包的处理裁定（Verdict）。

<a id="ga6ba64fac6e8d846ae7be5990f49a8293"></a>

### `net_if_unregister_link_cb()`

```c
void net_if_unregister_link_cb ( struct net_if_link_cb * link)
```

```c
#include <zephyr/net/net_if.h>
```

注销链路回调（Link Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `link` | 调用方指定的回调处理函数（Callback Handler）。 |

<a id="gaa5b88649296a278860ca36f14369834f"></a>

### `net_if_unregister_timestamp_cb()`

```c
void net_if_unregister_timestamp_cb ( struct net_if_timestamp_cb * handle)
```

```c
#include <zephyr/net/net_if.h>
```

注销时间戳回调（Timestamp Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 调用方指定的回调处理函数（Callback Handler）。 |

<a id="ga9c8212c087883510050ac6a39ef0a7bf"></a>

### `net_if_unset_promisc()`

```c
void net_if_unset_promisc ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_if.h>
```

将网络接口设为正常模式（Normal Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

<a id="ga02644cc623fc7a8878c17d54984e4210"></a>

### `net_if_up()`

```c
int net_if_up ( struct net_if * iface)
```

```c
#include <zephyr/net/net_if.h>
```

启用接口（Bring Interface Up）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

返回（Returns）：成功为0。


## 2.7\_原页交叉引用（Cross References）

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
- [RFC 7527, section-4](https://datatracker.ietf.org/doc/html/rfc7527#section-4)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_linkaddr](../network_core_model_reference/P105_net_linkaddr_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [RFC 2863](https://datatracker.ietf.org/doc/html/rfc2863)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [net_verdict](../api_vector_pipeline_topic_reference/P024_网络核心库（Network Core Library）.md#ga8e5393f3bdd85491f221324e637c3896)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_l2](../network_core_model_reference/P103_net_l2_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_link_type](../api_input_runtime_topic_reference/P015_网络链路地址库（Network Link Address Library）.md#ga1312c2322bc4a4f1c3b76d6466806b24)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_addr_type](../api_network_work_driver_reference/P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#gafecee2d4a331dc85ad962b81a6303e41)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [net_addr_state](../api_network_work_driver_reference/P002_IPv4_IPv6 原语与辅助工具（Primitives and helpers）.md#ga32e58fc83532ef57eeb6ff952f17288d)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [zephyr/net/net_if.h](../api_file_modem_network_reference/P003_zephyr__net__net_if.h_文件参考.md)
- [DEVICE_DT_NAME](../device_reference/P001_设备模型公共接口.md#gad864d7a50ee45285dacd68be1e5a49ce)
- [pm_device](../power/P039_通用设备运行时电源结构.md)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DT_INVALID_NODE](../dt_identity_reference/P001_设备树节点标识宏.md#ga710cc4455dd7e738f43f750153163855)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [RFC 4861, section-6.2.1](https://datatracker.ietf.org/doc/html/rfc4861#section-6.2.1)
- [RFC 4861](https://datatracker.ietf.org/doc/html/rfc4861)
- [socket()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a4dcc080bfb18d95d173bc205084f8b0a)
- [RFC 5014](https://datatracker.ietf.org/doc/html/rfc5014)
- [RFC 4861, section-7.3](https://datatracker.ietf.org/doc/html/rfc4861#section-7.3)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_gad864d7a50ee45285dacd68be1e5a49ce"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__net__if_html_gad8e37fc7a32339312dcfa614255988e8"></a>
<a id="agroup__net__if_html_gab1f762b01ae7bc37cd4a25724c123dda"></a>
<a id="agroup__net__if_html_ga50702b043a0791e59e7d5679dda1d9e8"></a>
<a id="agroup__net__if_html_gab2b287025e194dec1fab24e44d95362f"></a>
<a id="agroup__devicetree-generic-id_html_ga710cc4455dd7e738f43f750153163855"></a>
<a id="astructnet__if_html"></a>
<a id="agroup__net__if_html_gae0fdb0b909e06ba7831e53700c32b84f"></a>
<a id="agroup__net__if_html_ga65e4d856b53096bf784a4d5a495ca507"></a>
<a id="agroup__net__if_html_gadd040e5cc26a96c3f66f37539178c3b6"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30"></a>
<a id="gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad"></a>
<a id="gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3"></a>
<a id="gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1"></a>
<a id="gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b"></a>
<a id="gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13"></a>
<a id="gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660"></a>
<a id="gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3"></a>
<a id="ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840"></a>
<a id="ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009"></a>
<a id="ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141"></a>
<a id="ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05"></a>
<a id="ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0"></a>
<a id="ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac"></a>
<a id="ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329"></a>
<a id="ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6"></a>
<a id="ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a"></a>
<a id="ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d"></a>
<a id="ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d"></a>
<a id="ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7"></a>
<a id="ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe"></a>
<a id="ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9"></a>
<a id="ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58"></a>
<a id="ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32"></a>
<a id="ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367"></a>
<a id="ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4"></a>
<a id="ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f"></a>
<a id="ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d"></a>
<a id="ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_网络缓冲区库（Network Buffer Library）.md) · [返回大纲](大纲.md) · [下一章](P003_传感器（Sensor）.md)
