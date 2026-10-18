---
id: learning.zephyr-docs.api-socket-lora-topic-reference.page-7
title: 以太网支持函数（Ethernet Support Functions）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_以太网支持函数（Ethernet Support Functions）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网支持函数（Ethernet support functions）

<a id="details"></a>

以太网支持函数（Ethernet Support Functions）。起始版本（Since）：1.0。版本（Version）：0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 7.1\_主题（Topics）

<a id="r_dsa_5Ftag"></a>

相关声明：[分布式交换架构标签协议（DSA tag protocol）](../api_platform_topic_reference/P014_分布式交换架构标签协议（DSA tag protocol）.md)。

分布式交换架构（DSA）标签协议（Tag Protocol）的定义。

<a id="r_ethernet_5Fmii"></a>

相关声明：[以太网介质无关接口支持函数（Ethernet MII Support Functions）](../api_media_cellular_topic_reference/P011_以太网介质无关接口支持函数（Ethernet MII Support Functions）.md)。

以太网介质无关接口（Media independent interface，MII）函数。

<a id="r_ethernet_5Fmdio"></a>

相关声明：[IEEE 802.3 管理接口。](../api_iso_dns_lin_topic_reference/P008_IEEE 802.3 管理接口。.md)。

IEEE 802.3管理接口（Management Interface）的定义。

<a id="header-files"></a>
<a id="files"></a>

## 7.2\_文件（Files）

<a id="r_eth_5Fadin2111_2Eh"></a>

```c
file eth_adin2111.h
```

相关声明：[eth_adin2111.h](../api_file_mesh_interrupt_reference/P007_zephyr__drivers__ethernet__eth_adin2111.h_文件参考.md)。

ADIN2111以太网控制器（Ethernet Controller）驱动API的头文件。

<a id="r_eth_5Fnxp_5Fenet_2Eh"></a>

```c
file eth_nxp_enet.h
```

相关声明：[eth_nxp_enet.h](../api_file_reference/P109_zephyr__drivers__ethernet__eth_nxp_enet.h_文件参考.md)。

NXP ENET以太网（Ethernet）驱动内部定义的头文件。

<a id="r_eth_5Fnxp_5Fenet_5Fqos_2Eh"></a>

```c
file eth_nxp_enet_qos.h
```

相关声明：[eth_nxp_enet_qos.h](../api_file_reference/P110_zephyr__drivers__ethernet__eth_nxp_enet_qos.h_文件参考.md)。

NXP ENET QOS以太网（Ethernet）驱动内部定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.3\_数据结构（Data Structures）

<a id="r_net_5Feth_5Faddr"></a>

```c
struct net_eth_addr
```

相关声明：[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

以太网地址（Ethernet Address）。

<a id="r_ethernet_5Fqav_5Fparam"></a>

```c
struct ethernet_qav_param
```

相关声明：[ethernet_qav_param](../network_service_model_reference/P010_ethernet_qav_param_结构体.md)。

以太网Qav的专用参数。

<a id="r_ethernet_5Fqbv_5Fparam"></a>

```c
struct ethernet_qbv_param
```

相关声明：[ethernet_qbv_param](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md)。

以太网Qbv的专用参数。

<a id="r_ethernet_5Fqbu_5Fparam"></a>

```c
struct ethernet_qbu_param
```

相关声明：[ethernet_qbu_param](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md)。

以太网Qbu的专用参数。

<a id="r_ethernet_5Ffilter"></a>

```c
struct ethernet_filter
```

相关声明：[ethernet_filter](../network_service_model_reference/P008_ethernet_filter_结构体.md)。

以太网过滤器（Ethernet Filter）的描述。

<a id="r_net_5Feth_5Fmcast_5Faddr"></a>

```c
struct net_eth_mcast_addr
```

相关声明：[net_eth_mcast_addr](../network_core_model_reference/P061_net_eth_mcast_addr_结构体.md)。

网络接口的第二层组播地址（L2 Multicast Address）。

<a id="r_ethernet_5Ftxtime_5Fparam"></a>

```c
struct ethernet_txtime_param
```

相关声明：[ethernet_txtime_param](../network_service_model_reference/P013_ethernet_txtime_param_结构体.md)。

以太网发送时间（TXTIME）的专用参数。

<a id="r_ethernet_5Fapi"></a>

```c
struct ethernet_api
```

相关声明：[ethernet_api](../network_service_model_reference/P007_ethernet_api_结构体.md)。

以太网第二层（Ethernet L2）的API操作。

<a id="r_ethernet_5Flldp"></a>

```c
struct ethernet_lldp
```

相关声明：[ethernet_lldp](../network_service_model_reference/P009_ethernet_lldp_结构体.md)。

以太网链路层发现协议（LLDP）的专用参数。

<a id="r_net_5Feth_5Fmac_5Fconfig"></a>

```c
struct net_eth_mac_config
```

相关声明：[net_eth_mac_config](../network_core_model_reference/P060_net_eth_mac_config_结构体.md)。

MAC地址配置（Address Configuration）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.4\_宏定义（Macros）

<a id="r_ga399425f810c00bcf9babec019bc2ff12"></a>

```c
#define NET_ETH_ADDR_LEN 6U
```

相关声明：[NET_ETH_ADDR_LEN](#ga399425f810c00bcf9babec019bc2ff12)。

以太网 MAC 地址长度（Ethernet MAC Address Length）。

<a id="r_ga4cc1bb4cfa00b7749838eae3ae11048c"></a>

```c
#define NET_ETH_MINIMAL_FRAME_SIZE 60
```

相关声明：[NET_ETH_MINIMAL_FRAME_SIZE](#ga4cc1bb4cfa00b7749838eae3ae11048c)。

以太网最小帧大小（Minimum Ethernet Frame Size）。

<a id="r_gaa337199b1edc50c9003afa5c3a951d8b"></a>

```c
#define NET_ETH_MTU 1500
```

相关声明：[NET_ETH_MTU](#gaa337199b1edc50c9003afa5c3a951d8b)。

以太网最大传输单元大小（Ethernet MTU Size）。

<a id="r_ga197e02748be8eaf410f7deb57c984642"></a>

```c
#define ETH_NET_DEVICE_INIT(dev_id, name, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[ETH_NET_DEVICE_INIT](#ga197e02748be8eaf410f7deb57c984642)。

创建以太网网络接口（Ethernet Network Interface），并将其绑定到网络设备（Network Device）。

<a id="r_ga3dc27a54b7ae178e8c4daeba4c84aab0"></a>

```c
#define ETH_NET_DEVICE_INIT_INSTANCE(dev_id, name, instance, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[ETH_NET_DEVICE_INIT_INSTANCE](#ga3dc27a54b7ae178e8c4daeba4c84aab0)。

创建多个以太网网络接口（Ethernet Network Interface），并将它们绑定到网络设备（Network Device）。

<a id="r_ga9f67fee695953f24b1e5d9e49041aa99"></a>

```c
#define ETH_NET_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[ETH_NET_DEVICE_DT_DEFINE](#ga9f67fee695953f24b1e5d9e49041aa99)。

与 `ETH_NET_DEVICE_INIT` 类似，但从设备树（Devicetree）获取元数据。

<a id="r_gaecf9f102108836ed9cf7e2cdb3c90579"></a>

```c
#define ETH_NET_DEVICE_DT_INST_DEFINE(inst, ...)
```

相关声明：[ETH_NET_DEVICE_DT_INST_DEFINE](#gaecf9f102108836ed9cf7e2cdb3c90579)。

针对兼容标识符为 `DT_DRV_COMPAT` 的实例，提供与 `ETH_NET_DEVICE_DT_DEFINE` 类似的功能。

<a id="r_gaf6524602e433313c15ea2cef762ff0dc"></a>

```c
#define ETH_NET_L3_REGISTER(name, ptype, handler)
```

相关声明：[ETH_NET_L3_REGISTER](#gaf6524602e433313c15ea2cef762ff0dc)。

以太网 L3 协议注册宏（Ethernet L3 Protocol Register Macro）。

<a id="r_ga59882ff8ad5a11c20c08f296edad367e"></a>

```c
#define NET_ETH_MAC_DT_CONFIG_INIT(node_id)
```

相关声明：[NET_ETH_MAC_DT_CONFIG_INIT](#ga59882ff8ad5a11c20c08f296edad367e)。

为给定设备树节点标识符（DT Node Identifier）初始化以太网 MAC 配置（Ethernet MAC Config）。

<a id="r_gac1bb10b6bcc64911128814b9b9de1926"></a>

```c
#define NET_ETH_MAC_DT_INST_CONFIG_INIT(inst)
```

相关声明：[NET_ETH_MAC_DT_INST_CONFIG_INIT](#gac1bb10b6bcc64911128814b9b9de1926)。

针对兼容标识符为 `DT_DRV_COMPAT` 的实例，提供与 `NET_ETH_MAC_DT_CONFIG_INIT` 类似的功能。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.5\_类型定义（Typedefs）

<a id="r_ga8d28addcef0038c4ba1daa84bc104143"></a>

```c
typedef void(* net_eth_mcast_addr_cb_t) (struct net_if *iface, const struct net_eth_mcast_addr *addr, void *user_data)
```

相关声明：[net_eth_mcast_addr_cb_t](#ga8d28addcef0038c4ba1daa84bc104143)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_mcast_addr](../network_core_model_reference/P061_net_eth_mcast_addr_结构体.md)。

由 `net_eth_mcast_addr_foreach()` 使用的回调（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.6\_枚举（Enumerations）

<a id="r_ga9162ff11d626813fc840df0b67820ac5"></a>

```c
enum ethernet_hw_caps { ETHERNET_HW_TX_CHKSUM_OFFLOAD = BIT(0) , ETHERNET_HW_RX_CHKSUM_OFFLOAD = BIT(1) , ETHERNET_HW_VLAN = BIT(2) , ETHERNET_LINK_10BASE = BIT(3) , ETHERNET_LINK_100BASE = BIT(4) , ETHERNET_LINK_1000BASE = BIT(5) , ETHERNET_LINK_2500BASE = BIT(6) , ETHERNET_LINK_5000BASE = BIT(7) , ETHERNET_QAV = BIT(9) , ETHERNET_PROMISC_MODE = BIT(10) , ETHERNET_PRIORITY_QUEUES = BIT(11) , ETHERNET_HW_FILTERING = BIT(12) , ETHERNET_LLDP = BIT(13) , ETHERNET_HW_VLAN_TAG_STRIP = BIT(14) , ETHERNET_DSA_USER_PORT = BIT(15) , ETHERNET_DSA_CONDUIT_PORT = BIT(16) , ETHERNET_QBV = BIT(17) , ETHERNET_QBU = BIT(18) , ETHERNET_TXTIME = BIT(19) , ETHERNET_TXINJECTION_MODE = BIT(20) }
```

相关声明：[ethernet_hw_caps](#ga9162ff11d626813fc840df0b67820ac5)、[ETHERNET_HW_TX_CHKSUM_OFFLOAD](#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861)、[ETHERNET_HW_RX_CHKSUM_OFFLOAD](#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33)、[ETHERNET_HW_VLAN](#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95)、[ETHERNET_LINK_10BASE](#gga9162ff11d626813fc840df0b67820ac5a4508489dc8a67ef908757a9e2338babb)、[ETHERNET_LINK_100BASE](#gga9162ff11d626813fc840df0b67820ac5a2c59d7d5a1d5eff15976806d237960c1)、[ETHERNET_LINK_1000BASE](#gga9162ff11d626813fc840df0b67820ac5a55e8d0ee975acc9eabf5096d1b926f6b)、[ETHERNET_LINK_2500BASE](#gga9162ff11d626813fc840df0b67820ac5afe48cf59ca4d1db42e768ca272159d55)、[ETHERNET_LINK_5000BASE](#gga9162ff11d626813fc840df0b67820ac5a9ab79aee30b73747fceff86fd3b967f9)、[ETHERNET_QAV](#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42)、[ETHERNET_PROMISC_MODE](#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d)、[ETHERNET_PRIORITY_QUEUES](#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475)、[ETHERNET_HW_FILTERING](#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe)、[ETHERNET_LLDP](#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2)、[ETHERNET_HW_VLAN_TAG_STRIP](#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5)、[ETHERNET_DSA_USER_PORT](#gga9162ff11d626813fc840df0b67820ac5a12991c85e1a7405bd145b3fff8aeecf1)、[ETHERNET_DSA_CONDUIT_PORT](#gga9162ff11d626813fc840df0b67820ac5a2eeaa2befc2d7a38f0318addef88f072)、[ETHERNET_QBV](#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85)、[ETHERNET_QBU](#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08)、[ETHERNET_TXTIME](#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2)、[ETHERNET_TXINJECTION_MODE](#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b)。

以太网硬件能力（Ethernet Hardware Capabilities）。

<a id="r_ga139cc696837611a522b289f2ea7bf6fc"></a>

```c
enum ethernet_if_types { L2_ETH_IF_TYPE_ETHERNET , L2_ETH_IF_TYPE_WIFI }
```

相关声明：[ethernet_if_types](#ga139cc696837611a522b289f2ea7bf6fc)、[L2_ETH_IF_TYPE_ETHERNET](#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530)、[L2_ETH_IF_TYPE_WIFI](#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671)。

以太网二层类型（Ethernet L2 Types）。

<a id="r_gabf86b7f09a9d041eea25357cd7a85ede"></a>

```c
enum ethernet_checksum_support { ETHERNET_CHECKSUM_SUPPORT_NONE = NET_IF_CHECKSUM_NONE_BIT , ETHERNET_CHECKSUM_SUPPORT_IPV4_HEADER = NET_IF_CHECKSUM_IPV4_HEADER_BIT , ETHERNET_CHECKSUM_SUPPORT_IPV4_ICMP = NET_IF_CHECKSUM_IPV4_ICMP_BIT , ETHERNET_CHECKSUM_SUPPORT_IPV6_HEADER = NET_IF_CHECKSUM_IPV6_HEADER_BIT , ETHERNET_CHECKSUM_SUPPORT_IPV6_ICMP = NET_IF_CHECKSUM_IPV6_ICMP_BIT , ETHERNET_CHECKSUM_SUPPORT_TCP = NET_IF_CHECKSUM_TCP_BIT , ETHERNET_CHECKSUM_SUPPORT_UDP = NET_IF_CHECKSUM_UDP_BIT }
```

相关声明：[ethernet_checksum_support](#gabf86b7f09a9d041eea25357cd7a85ede)、[ETHERNET_CHECKSUM_SUPPORT_NONE](#ggabf86b7f09a9d041eea25357cd7a85edea90314c44dca3c123d1a0bd70f108524d)、[ETHERNET_CHECKSUM_SUPPORT_IPV4_HEADER](#ggabf86b7f09a9d041eea25357cd7a85edea6485d2abcd3dae6786022aa286234ed4)、[ETHERNET_CHECKSUM_SUPPORT_IPV4_ICMP](#ggabf86b7f09a9d041eea25357cd7a85edea5671ade139cb0cd28d02e3215337acb9)、[ETHERNET_CHECKSUM_SUPPORT_IPV6_HEADER](#ggabf86b7f09a9d041eea25357cd7a85edea557127c3bc97969fe57fcd8ac55567b5)、[ETHERNET_CHECKSUM_SUPPORT_IPV6_ICMP](#ggabf86b7f09a9d041eea25357cd7a85edeac64b392a0591cfe7aa5564a476fe20be)、[ETHERNET_CHECKSUM_SUPPORT_TCP](#ggabf86b7f09a9d041eea25357cd7a85edea3346f0e3d0b350c7fe663cfe389c1e02)、[ETHERNET_CHECKSUM_SUPPORT_UDP](#ggabf86b7f09a9d041eea25357cd7a85edea03e31130ecef7ac032bceed6f3091af8)。

校验和卸载（Checksum Offloading）支持的协议。

<a id="r_gabfab900bfd7a9078e7ac2fd6aed9ce83"></a>

```c
enum ethernet_stats_type { ETHERNET_STATS_TYPE_COMMON = BIT(0) , ETHERNET_STATS_TYPE_VENDOR = BIT(1) , ETHERNET_STATS_TYPE_ALL = 0xFFFFFFFFU }
```

相关声明：[ethernet_stats_type](#gabfab900bfd7a9078e7ac2fd6aed9ce83)、[ETHERNET_STATS_TYPE_COMMON](#ggabfab900bfd7a9078e7ac2fd6aed9ce83ad41e45f16877f28b44ec23fadb35d355)、[ETHERNET_STATS_TYPE_VENDOR](#ggabfab900bfd7a9078e7ac2fd6aed9ce83a3a094b0237833d4523e04d7b6bb5fbab)、[ETHERNET_STATS_TYPE_ALL](#ggabfab900bfd7a9078e7ac2fd6aed9ce83a6bb1bfaf79f232101bc91ab02f54e4a7)。

以太网统计类型（Ethernet Statistics Type），采用位图（Bitmap）表示。

<a id="r_gac2433b0d82ef25373b2c0f994e248e92"></a>

```c
enum net_eth_mac_type { NET_ETH_MAC_DEFAULT = 0 , NET_ETH_MAC_RANDOM , NET_ETH_MAC_NVMEM , NET_ETH_MAC_STATIC }
```

相关声明：[net_eth_mac_type](#gac2433b0d82ef25373b2c0f994e248e92)、[NET_ETH_MAC_DEFAULT](#ggac2433b0d82ef25373b2c0f994e248e92a8b1eb5edcd9f4953d56c9c10088d6bb5)、[NET_ETH_MAC_RANDOM](#ggac2433b0d82ef25373b2c0f994e248e92a3fad5d3a2578e83da31f3188add46b87)、[NET_ETH_MAC_NVMEM](#ggac2433b0d82ef25373b2c0f994e248e92a730e86dd6e257352afb233fdcc189955)、[NET_ETH_MAC_STATIC](#ggac2433b0d82ef25373b2c0f994e248e92a9e0096f69300cf30c1f78c33074c1bda)。

MAC 地址配置类型（MAC Address Configuration Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.7\_函数（Functions）

<a id="r_ga76a5fe39ce12478c666d87f4aec3d579"></a>

```c
static bool net_eth_is_addr_broadcast (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_broadcast](#ga76a5fe39ce12478c666d87f4aec3d579)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为广播地址（Broadcast Address）。

<a id="r_ga237aab2d07ffa84355981d02a4576ebe"></a>

```c
static bool net_eth_is_addr_all_zeroes (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_all_zeroes](#ga237aab2d07ffa84355981d02a4576ebe)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为全零地址（All-zero Address）。

<a id="r_ga89964de263029223d119f361fbd94bfd"></a>

```c
static bool net_eth_is_addr_unspecified (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_unspecified](#ga89964de263029223d119f361fbd94bfd)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为未指定地址（Unspecified Address）。

<a id="r_ga2755ecb84e9759c24302e33a56a1fc84"></a>

```c
static bool net_eth_is_addr_multicast (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_multicast](#ga2755ecb84e9759c24302e33a56a1fc84)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为组播地址（Multicast Address）。

<a id="r_gae91a64c96e0a480927d92271092a158d"></a>

```c
static bool net_eth_is_addr_unicast (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_unicast](#gae91a64c96e0a480927d92271092a158d)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为单播地址（Unicast Address）。

<a id="r_gaf20472f9d60e5cddffed2919b3091030"></a>

```c
static bool net_eth_is_addr_valid (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_valid](#gaf20472f9d60e5cddffed2919b3091030)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否有效（Valid）。

<a id="r_gaec6fb3c05792bdd30596137686f3251a"></a>

```c
static bool net_eth_is_addr_lldp_multicast (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_lldp_multicast](#gaec6fb3c05792bdd30596137686f3251a)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为 LLDP 组播地址（LLDP Multicast Address）。

<a id="r_gaeddfa5b3ff6e356393114b351f87fe43"></a>

```c
static bool net_eth_is_addr_ptp_multicast (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_ptp_multicast](#gaeddfa5b3ff6e356393114b351f87fe43)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为 PTP 组播地址（PTP Multicast Address）。

<a id="r_gae66b24a847f8e0ad119c6c466331afd6"></a>

```c
const struct net_eth_addr * net_eth_broadcast_addr (void)
```

相关声明：[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)、[net_eth_broadcast_addr](#gae66b24a847f8e0ad119c6c466331afd6)。

返回以太网广播地址（Ethernet Broadcast Address）。

<a id="r_ga26984472437a98b00c31156f75558134"></a>

```c
void net_eth_ipv4_mcast_to_mac_addr (const struct net_in_addr *ipv4_addr, struct net_eth_addr *mac_addr)
```

相关声明：[net_eth_ipv4_mcast_to_mac_addr](#ga26984472437a98b00c31156f75558134)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

将 IPv4 组播地址（Multicast Address）转换为以太网地址（Ethernet Address）。

<a id="r_ga93e498e99c155fc402a26a4429d044a0"></a>

```c
void net_eth_ipv6_mcast_to_mac_addr (const struct net_in6_addr *ipv6_addr, struct net_eth_addr *mac_addr)
```

相关声明：[net_eth_ipv6_mcast_to_mac_addr](#ga93e498e99c155fc402a26a4429d044a0)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

将 IPv6 组播地址（Multicast Address）转换为以太网地址（Ethernet Address）。

<a id="r_ga3e578035be797bbbafafa56dedaa8320"></a>

```c
int net_eth_mcast_addr_add (struct net_if *iface, const struct net_eth_addr *addr)
```

相关声明：[net_eth_mcast_addr_add](#ga3e578035be797bbbafafa56dedaa8320)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

在网络接口上加入一个二层组播组（L2 Multicast Group）。

<a id="r_ga3cd2e9abc38bdd7eb0cb3932d96fd90e"></a>

```c
int net_eth_mcast_addr_rm (struct net_if *iface, const struct net_eth_addr *addr)
```

相关声明：[net_eth_mcast_addr_rm](#ga3cd2e9abc38bdd7eb0cb3932d96fd90e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

在网络接口上离开一个二层组播组（L2 Multicast Group）。

<a id="r_ga80adc03695a8fbb9dbc9dd3adec78c04"></a>

```c
void net_eth_mcast_addr_foreach (struct net_if *iface, net_eth_mcast_addr_cb_t cb, void *user_data)
```

相关声明：[net_eth_mcast_addr_foreach](#ga80adc03695a8fbb9dbc9dd3adec78c04)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_mcast_addr_cb_t](#ga8d28addcef0038c4ba1daa84bc104143)。

遍历网络接口的所有二层组播地址（L2 Multicast Address）。

<a id="r_gab0a3b4584bb6ce1d27b98b063fd3fcbd"></a>

```c
static enum ethernet_hw_caps net_eth_get_hw_capabilities (struct net_if *iface)
```

相关声明：[ethernet_hw_caps](#ga9162ff11d626813fc840df0b67820ac5)、[net_eth_get_hw_capabilities](#gab0a3b4584bb6ce1d27b98b063fd3fcbd)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回以太网设备的硬件能力信息（Hardware Capability Information）。

<a id="r_ga1246be489eb7130100bbaebbb73961c5"></a>

```c
static int net_eth_get_hw_config (struct net_if *iface, enum ethernet_config_type type, struct ethernet_config *config)
```

相关声明：[net_eth_get_hw_config](#ga1246be489eb7130100bbaebbb73961c5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回以太网设备的硬件配置信息（Hardware Configuration Information）。

<a id="r_ga16cbc14e3a0a470bbbd5aeb5e73dc1de"></a>

```c
static int net_eth_vlan_enable (struct net_if *iface, uint16_t tag)
```

相关声明：[net_eth_vlan_enable](#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

为接口添加虚拟局域网标签（VLAN Tag）。

<a id="r_gab71a741cea5f645f4354a1abc9c95a50"></a>

```c
static int net_eth_vlan_disable (struct net_if *iface, uint16_t tag)
```

相关声明：[net_eth_vlan_disable](#gab71a741cea5f645f4354a1abc9c95a50)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从接口移除虚拟局域网标签（VLAN Tag）。

<a id="r_ga6184c43a62e4af9958412f99991358c9"></a>

```c
static uint16_t net_eth_get_vlan_tag (struct net_if *iface)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_eth_get_vlan_tag](#ga6184c43a62e4af9958412f99991358c9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回为网络接口指定的虚拟局域网标签（VLAN Tag）。

<a id="r_gad9d890dcf7f5ee3659bf3bd5949faa4e"></a>

```c
static struct net_if * net_eth_get_vlan_iface (struct net_if *iface, uint16_t tag)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_get_vlan_iface](#gad9d890dcf7f5ee3659bf3bd5949faa4e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

返回与该虚拟局域网标签（VLAN Tag）相关联的网络接口。

<a id="r_ga010a95a0239a800131ac3d43dd54737f"></a>

```c
static struct net_if * net_eth_get_vlan_main (struct net_if *iface)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_get_vlan_main](#ga010a95a0239a800131ac3d43dd54737f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回关联到该虚拟局域网标签（VLAN Tag）的主网络接口（Main Network Interface）。

<a id="r_gac536aa7154c4a8d194ec67efb68e275c"></a>

```c
static bool net_eth_is_vlan_enabled (struct ethernet_context *ctx, struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_vlan_enabled](#gac536aa7154c4a8d194ec67efb68e275c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查是否有 VLAN 接口在此特定以太网网络接口上启用，或者是否支持带优先级标签的帧（Priority Tagged Frame，标签为 0）。

<a id="r_ga78aad58ec66710034cab8891ad638a2c"></a>

```c
static bool net_eth_get_vlan_status (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_get_vlan_status](#ga78aad58ec66710034cab8891ad638a2c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取给定网络接口的 VLAN 状态（VLAN Status），即是否已启用。

<a id="r_ga8ca1eccc88a351241298d358ec28fdf5"></a>

```c
static bool net_eth_is_vlan_interface (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_vlan_interface](#ga8ca1eccc88a351241298d358ec28fdf5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查给定接口是否为 VLAN 接口（VLAN Interface）。

<a id="r_gaa0ef2f94fd18da9c5ea675b46faac8d0"></a>

```c
static int net_eth_mac_load (const struct net_eth_mac_config *cfg, uint8_t *mac_addr)
```

相关声明：[net_eth_mac_load](#gaa0ef2f94fd18da9c5ea675b46faac8d0)、[net_eth_mac_config](../network_core_model_reference/P060_net_eth_mac_config_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从指定类型的 MAC 地址配置结构体（MAC Address Configuration Structure）加载 MAC 地址。

<a id="r_gaa7f447129b5b8392640f849d18e9246b"></a>

```c
void net_eth_carrier_set (struct net_if *iface, bool carrier_up)
```

相关声明：[net_eth_carrier_set](#gaa7f447129b5b8392640f849d18e9246b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

通知以太网二层驱动（Ethernet L2 Driver）已检测到载波（Carrier），或载波已丢失。

<a id="r_ga62b33344256bbe228689e2cb541a0874"></a>

```c
static void net_eth_carrier_on (struct net_if *iface)
```

相关声明：[net_eth_carrier_on](#ga62b33344256bbe228689e2cb541a0874)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

通知以太网二层驱动（Ethernet L2 Driver）已检测到载波（Carrier）。

<a id="r_ga97ef5a8ad9157e2db12e9caf6faef5e7"></a>

```c
static void net_eth_carrier_off (struct net_if *iface)
```

相关声明：[net_eth_carrier_off](#ga97ef5a8ad9157e2db12e9caf6faef5e7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

通知以太网二层驱动（Ethernet L2 Driver）载波（Carrier）已丢失。

<a id="r_ga42a3c6b04ef8827e3443c5aebe5541b9"></a>

```c
int net_eth_promisc_mode (struct net_if *iface, bool enable)
```

相关声明：[net_eth_promisc_mode](#ga42a3c6b04ef8827e3443c5aebe5541b9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

开启或关闭混杂模式（Promiscuous Mode）。

<a id="r_gafbb76d53f9f80628d18d39368a28f984"></a>

```c
int net_eth_txinjection_mode (struct net_if *iface, bool enable)
```

相关声明：[net_eth_txinjection_mode](#gafbb76d53f9f80628d18d39368a28f984)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

开启或关闭发送注入模式（TX-Injection Mode）。

<a id="r_ga920bddac077675d544a21fb5650c945e"></a>

```c
int net_eth_mac_filter (struct net_if *iface, struct net_eth_addr *mac, enum ethernet_filter_type type, bool enable)
```

相关声明：[net_eth_mac_filter](#ga920bddac077675d544a21fb5650c945e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为 MAC 地址 `mac` 设置或取消硬件过滤（HW Filtering）。

<a id="r_ga7225d06fbaa12d4668fa165d9e8f0845"></a>

```c
const struct device * net_eth_get_phy (struct net_if *iface)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[net_eth_get_phy](#ga7225d06fbaa12d4668fa165d9e8f0845)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回与此以太网网络接口关联的物理层设备（PHY Device）。

<a id="r_ga37ff48434c56bbb24422dd805449b6f3"></a>

```c
static const struct device * net_eth_get_ptp_clock (struct net_if *iface)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[net_eth_get_ptp_clock](#ga37ff48434c56bbb24422dd805449b6f3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回与此以太网网络接口关联的精确时间协议时钟（PTP Clock）。

<a id="r_ga84c37db5687c5264bec99976a1108ab6"></a>

```c
const struct device * net_eth_get_ptp_clock_by_index (int index)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[net_eth_get_ptp_clock_by_index](#ga84c37db5687c5264bec99976a1108ab6)。

返回与此以太网网络接口索引关联的精确时间协议时钟（PTP Clock）。

<a id="r_ga6e603f6f74e6d7e988e7119a6df2ab4d"></a>

```c
static bool net_eth_type_is_wifi (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_type_is_wifi](#ga6e603f6f74e6d7e988e7119a6df2ab4d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查以太网二层网络接口（Ethernet L2 Network Interface）能否执行 Wi-Fi 功能。

<a id="r_gae617887d42a288697f2507c5b0907909"></a>

```c
static bool net_eth_type_is_ethernet (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_type_is_ethernet](#gae617887d42a288697f2507c5b0907909)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查以太网二层网络接口（Ethernet L2 Network Interface）是否为有线以太网（Cabled Ethernet）。

<a id="r_gaa64462598843dd9f6e731198498aea31"></a>

```c
static void net_eth_set_if_type_wifi (struct net_if *iface)
```

相关声明：[net_eth_set_if_type_wifi](#gaa64462598843dd9f6e731198498aea31)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将以太网接口类型（Ethernet Interface Type）设置为 Wi-Fi。

## 7.8\_详细说明（Detailed Documentation）

<a id="ga9f67fee695953f24b1e5d9e49041aa99"></a>

### `ETH_NET_DEVICE_DT_DEFINE`

```c
#define ETH_NET_DEVICE_DT_DEFINE ( node_id, init_fn, pm, data, config, prio, api, mtu )
```

```c
#include <zephyr/net/ethernet.h>
```

展开值（Value）：

```c
Z_ETH_NET_DEVICE_INIT(node_id, Z_DEVICE_DT_DEV_ID(node_id),     \
                      DEVICE_DT_NAME(node_id), init_fn, pm,     \
                      data, config, prio, api, mtu)
```

与 `ETH_NET_DEVICE_INIT` 类似，但从设备树（Devicetree）获取元数据。

创建以太网网络接口（Ethernet Network Interface），并将其绑定到网络设备（Network Device）。

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

<a id="gaecf9f102108836ed9cf7e2cdb3c90579"></a>

### `ETH_NET_DEVICE_DT_INST_DEFINE`

```c
#define ETH_NET_DEVICE_DT_INST_DEFINE ( inst, ... )
```

```c
#include <zephyr/net/ethernet.h>
```

展开值（Value）：

```c
ETH_NET_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
```

针对兼容标识符为 `DT_DRV_COMPAT` 的实例，提供与 `ETH_NET_DEVICE_DT_DEFINE` 类似的功能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号（Instance Number）。调用 `ETH_NET_DEVICE_DT_DEFINE` 时，会替换为 `DT_DRV_INST(inst)`。 |
| `...` | `ETH_NET_DEVICE_DT_DEFINE` 所要求的其他参数（Parameters）。 |

<a id="ga197e02748be8eaf410f7deb57c984642"></a>

### `ETH_NET_DEVICE_INIT`

```c
#define ETH_NET_DEVICE_INIT ( dev_id, name, init_fn, pm, data, config, prio, api, mtu )
```

```c
#include <zephyr/net/ethernet.h>
```

展开值（Value）：

```c
Z_ETH_NET_DEVICE_INIT(DT_INVALID_NODE, dev_id, name, init_fn,   \
                      pm, data, config, prio, api, mtu)
```

创建以太网网络接口（Ethernet Network Interface），并将其绑定到网络设备（Network Device）。

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

<a id="ga3dc27a54b7ae178e8c4daeba4c84aab0"></a>

### `ETH_NET_DEVICE_INIT_INSTANCE`

```c
#define ETH_NET_DEVICE_INIT_INSTANCE ( dev_id, name, instance, init_fn, pm, data, config, prio, api, mtu )
```

```c
#include <zephyr/net/ethernet.h>
```

展开值（Value）：

```c
Z_ETH_NET_DEVICE_INIT_INSTANCE(DT_INVALID_NODE, dev_id, name,   \
                               instance, init_fn, pm, data,     \
                               config, prio, api, mtu)
```

创建多个以太网网络接口（Ethernet Network Interface），并将它们绑定到网络设备（Network Device）。

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
| `mtu` | 此网络接口（Network Interface）的最大传输单元（MTU），以字节为单位。 |

<a id="gaf6524602e433313c15ea2cef762ff0dc"></a>

### `ETH_NET_L3_REGISTER`

```c
#define ETH_NET_L3_REGISTER ( name, ptype, handler )
```

```c
#include <zephyr/net/ethernet.h>
```

展开值（Value）：

```c
NET_L3_REGISTER(&NET_L2_GET_NAME(ETHERNET), name, ptype, handler)
```

以太网 L3 协议注册宏（Ethernet L3 Protocol Register Macro）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 网络层（L3）协议名称。 |
| `ptype` | 以太网协议类型（Ethernet Protocol Type）。 |
| `handler` | 此协议类型的处理函数（Handler Function）。 |

<a id="ga399425f810c00bcf9babec019bc2ff12"></a>

### `NET_ETH_ADDR_LEN`

```c
#define NET_ETH_ADDR_LEN 6U
```

```c
#include <zephyr/net/ethernet.h>
```

以太网 MAC 地址长度（Ethernet MAC Address Length）。

<a id="ga59882ff8ad5a11c20c08f296edad367e"></a>

### `NET_ETH_MAC_DT_CONFIG_INIT`

```c
#define NET_ETH_MAC_DT_CONFIG_INIT ( node_id)
```

```c
#include <zephyr/net/ethernet.h>
```

展开值（Value）：

```c
COND_CASE_1(DT_PROP(node_id, zephyr_random_mac_address),                                   \
            (Z_NET_ETH_MAC_DT_CONFIG_INIT_RANDOM(node_id)),                                \
            DT_NVMEM_CELLS_HAS_NAME(node_id, mac_address),                                 \
            (Z_NET_ETH_MAC_DT_CONFIG_INIT_NVMEM(node_id)),                                 \
            DT_NODE_HAS_PROP(node_id, local_mac_address),                                  \
            (Z_NET_ETH_MAC_DT_CONFIG_INIT_STATIC(node_id)),                                \
            (Z_NET_ETH_MAC_DT_CONFIG_INIT_DEFAULT(node_id)))
```

为给定设备树节点标识符（DT Node Identifier）初始化以太网 MAC 配置（Ethernet MAC Config）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 节点标识符。 |

<a id="gac1bb10b6bcc64911128814b9b9de1926"></a>

### `NET_ETH_MAC_DT_INST_CONFIG_INIT`

```c
#define NET_ETH_MAC_DT_INST_CONFIG_INIT ( inst)
```

```c
#include <zephyr/net/ethernet.h>
```

展开值（Value）：

```c
NET_ETH_MAC_DT_CONFIG_INIT(DT_DRV_INST(inst))
```

针对兼容标识符为 `DT_DRV_COMPAT` 的实例，提供与 `NET_ETH_MAC_DT_CONFIG_INIT` 类似的功能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号。 |

**参阅（See Also）**：另请参阅（See Also）：`NET_ETH_MAC_DT_CONFIG_INIT`。

<a id="ga4cc1bb4cfa00b7749838eae3ae11048c"></a>

### `NET_ETH_MINIMAL_FRAME_SIZE`

```c
#define NET_ETH_MINIMAL_FRAME_SIZE 60
```

```c
#include <zephyr/net/ethernet.h>
```

以太网最小帧大小（Minimum Ethernet Frame Size）。

<a id="gaa337199b1edc50c9003afa5c3a951d8b"></a>

### `NET_ETH_MTU`

```c
#define NET_ETH_MTU 1500
```

```c
#include <zephyr/net/ethernet.h>
```

以太网最大传输单元大小（Ethernet MTU Size）。

<a id="ga8d28addcef0038c4ba1daa84bc104143"></a>

### `net_eth_mcast_addr_cb_t`

```c
typedef void(* net_eth_mcast_addr_cb_t) (struct net_if *iface, const struct net_eth_mcast_addr *addr, void *user_data)
```

```c
#include <zephyr/net/ethernet.h>
```

由 `net_eth_mcast_addr_foreach()` 使用的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（Network Interface）的指针。 |
| `addr` | 指向该接口的链路层多播地址（L2 Multicast Address）的指针。 |
| `user_data` | 提供给 `net_eth_mcast_addr_foreach()` 的数据。 |

<a id="gabf86b7f09a9d041eea25357cd7a85ede"></a>

### `ethernet_checksum_support`

```c
enum ethernet_checksum_support
```

```c
#include <zephyr/net/ethernet.h>
```

校验和卸载（Checksum Offloading）支持的协议。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ETHERNET_CHECKSUM_SUPPORT_NONE` | 设备不支持任何网络层／传输层校验和卸载（L3/L4 Checksum Offloading）。 |
| `ETHERNET_CHECKSUM_SUPPORT_IPV4_HEADER` | 设备支持 IPv4 头部校验和卸载（Header Checksum Offloading）。 |
| `ETHERNET_CHECKSUM_SUPPORT_IPV4_ICMP` | 设备支持 ICMPv4 载荷校验和卸载（Payload Checksum Offloading），也隐含支持 IPv4 头部校验和卸载。 |
| `ETHERNET_CHECKSUM_SUPPORT_IPV6_HEADER` | 设备支持 IPv6 头部校验和卸载（Header Checksum Offloading）。 |
| `ETHERNET_CHECKSUM_SUPPORT_IPV6_ICMP` | 设备支持 ICMPv6 载荷校验和卸载（Payload Checksum Offloading），也隐含支持 IPv6 头部校验和卸载。 |
| `ETHERNET_CHECKSUM_SUPPORT_TCP` | 设备对所有支持的 IP 协议都支持 TCP 校验和卸载（Checksum Offloading）。 |
| `ETHERNET_CHECKSUM_SUPPORT_UDP` | 设备对所有支持的 IP 协议都支持 UDP 校验和卸载（Checksum Offloading）。 |

<a id="ga9162ff11d626813fc840df0b67820ac5"></a>

### `ethernet_hw_caps`

```c
enum ethernet_hw_caps
```

```c
#include <zephyr/net/ethernet.h>
```

以太网硬件能力（Ethernet Hardware Capabilities）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ETHERNET_HW_TX_CHKSUM_OFFLOAD` | 支持 IPv4、UDP 和 TCP 的全部发送校验和卸载（TX Checksum Offloading）。 |
| `ETHERNET_HW_RX_CHKSUM_OFFLOAD` | 支持 IPv4、UDP 和 TCP 的全部接收校验和卸载（RX Checksum Offloading）。 |
| `ETHERNET_HW_VLAN` | 支持虚拟局域网（VLAN）。 |
| `ETHERNET_LINK_10BASE` | 支持 10 Mbit/s 链路（Link）。 |
| `ETHERNET_LINK_100BASE` | 支持 100 Mbit/s 链路（Link）。 |
| `ETHERNET_LINK_1000BASE` | 支持 1 Gbit/s 链路（Link）。 |
| `ETHERNET_LINK_2500BASE` | 支持 2.5 Gbit/s 链路（Link）。 |
| `ETHERNET_LINK_5000BASE` | 支持 5 Gbit/s 链路（Link）。 |
| `ETHERNET_QAV` | 支持 IEEE 802.1Qav，即基于信用的整形（Credit-based Shaping）。 |
| `ETHERNET_PROMISC_MODE` | 支持混杂模式（Promiscuous Mode）。 |
| `ETHERNET_PRIORITY_QUEUES` | 提供优先级队列（Priority Queues）。 |
| `ETHERNET_HW_FILTERING` | 支持 MAC 地址过滤（MAC Address Filtering）。 |
| `ETHERNET_LLDP` | 支持链路层发现协议（Link Layer Discovery Protocol）。 |
| `ETHERNET_HW_VLAN_TAG_STRIP` | 虚拟局域网标签剥离（VLAN Tag Stripping）。 |
| `ETHERNET_DSA_USER_PORT` | 分布式交换架构（DSA）交换机用户端口（User Port）。 |
| `ETHERNET_DSA_CONDUIT_PORT` | 分布式交换架构（DSA）交换机连接端口（Conduit Port）。 |
| `ETHERNET_QBV` | 支持 IEEE 802.1Qbv，即调度流量（Scheduled Traffic）。 |
| `ETHERNET_QBU` | 支持 IEEE 802.1Qbu，即帧抢占（Frame Preemption）。 |
| `ETHERNET_TXTIME` | 支持发送时间（TXTIME）。 |
| `ETHERNET_TXINJECTION_MODE` | 支持发送注入（TX-Injection）。 |

<a id="ga139cc696837611a522b289f2ea7bf6fc"></a>

### `ethernet_if_types`

```c
enum ethernet_if_types
```

```c
#include <zephyr/net/ethernet.h>
```

以太网二层类型（Ethernet L2 Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `L2_ETH_IF_TYPE_ETHERNET` | IEEE 802.3 以太网（Ethernet），默认值。 |
| `L2_ETH_IF_TYPE_WIFI` | IEEE 802.11 Wi-Fi。 |

<a id="gabfab900bfd7a9078e7ac2fd6aed9ce83"></a>

### `ethernet_stats_type`

```c
enum ethernet_stats_type
```

```c
#include <zephyr/net/ethernet.h>
```

以太网统计类型（Ethernet Statistics Type），采用位图（Bitmap）表示。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ETHERNET_STATS_TYPE_COMMON` | 仅通用统计（Common Statistics），不包括厂商统计（Vendor Statistics）。 |
| `ETHERNET_STATS_TYPE_VENDOR` | 仅厂商统计（Vendor Statistics）。 |
| `ETHERNET_STATS_TYPE_ALL` | 全部统计（All Statistics）。 |

<a id="gac2433b0d82ef25373b2c0f994e248e92"></a>

### `net_eth_mac_type`

```c
enum net_eth_mac_type
```

```c
#include <zephyr/net/ethernet.h>
```

MAC 地址配置类型（MAC Address Configuration Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_ETH_MAC_DEFAULT` | MAC 地址由驱动程序（Driver）处理，这是向后兼容的情况。 |
| `NET_ETH_MAC_RANDOM` | 初始化（Initialization）期间生成随机 MAC 地址（Random MAC Address）。 |
| `NET_ETH_MAC_NVMEM` | 从非易失存储单元（NVMEM Cell）读取 MAC 地址。注意（Attention）：仅当启用以下 Kconfig 选项时可用：`CONFIG_NVMEM`。 |
| `NET_ETH_MAC_STATIC` | 由设备树（Devicetree）提供静态 MAC 地址（Static MAC Address）。 |

**注意（Attention）**：注意（Attention）：仅在启用Kconfig选项CONFIG_NVMEM时可用。

<a id="gae66b24a847f8e0ad119c6c466331afd6"></a>

### `net_eth_broadcast_addr()`

```c
const struct net_eth_addr * net_eth_broadcast_addr ( void )
```

```c
#include <zephyr/net/ethernet.h>
```

返回以太网广播地址（Ethernet Broadcast Address）。

**返回（Returns）**：返回值（Returns）：以太网广播地址（Ethernet Broadcast Address）。

<a id="ga97ef5a8ad9157e2db12e9caf6faef5e7"></a>

### `net_eth_carrier_off()`

```c
void net_eth_carrier_off ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

通知以太网二层驱动（Ethernet L2 Driver）载波（Carrier）已丢失。

断开网线（Cable）时发生。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

<a id="ga62b33344256bbe228689e2cb541a0874"></a>

### `net_eth_carrier_on()`

```c
void net_eth_carrier_on ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

通知以太网二层驱动（Ethernet L2 Driver）已检测到载波（Carrier）。

连接网线（Cable）时发生。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

<a id="gaa7f447129b5b8392640f849d18e9246b"></a>

### `net_eth_carrier_set()`

```c
void net_eth_carrier_set ( struct net_if * iface, bool carrier_up )
```

```c
#include <zephyr/net/ethernet.h>
```

通知以太网二层驱动（Ethernet L2 Driver）已检测到载波（Carrier），或载波已丢失。

连接或断开网线（Cable）时发生。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `carrier_up` | 检测到载波（Carrier）时为 `true`，载波丢失时为 `false`。 |

<a id="gab0a3b4584bb6ce1d27b98b063fd3fcbd"></a>

### `net_eth_get_hw_capabilities()`

```c
enum ethernet_hw_caps net_eth_get_hw_capabilities ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

返回以太网设备的硬件能力信息（Hardware Capability Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：硬件能力（Hardware Capabilities）。

<a id="ga1246be489eb7130100bbaebbb73961c5"></a>

### `net_eth_get_hw_config()`

```c
int net_eth_get_hw_config ( struct net_if * iface, enum ethernet_config_type type, struct ethernet_config * config )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

返回以太网设备的硬件配置信息（Hardware Configuration Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `type` | 配置类型（Configuration Type）。 |
| `config` | 以太网配置（Ethernet Configuration）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga7225d06fbaa12d4668fa165d9e8f0845"></a>

### `net_eth_get_phy()`

```c
const struct device * net_eth_get_phy ( struct net_if * iface)
```

```c
#include <zephyr/net/ethernet.h>
```

返回与此以太网网络接口关联的物理层设备（PHY Device）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：找到物理层（PHY）设备时返回其指针，否则返回 `NULL`。

<a id="ga37ff48434c56bbb24422dd805449b6f3"></a>

### `net_eth_get_ptp_clock()`

```c
const struct device * net_eth_get_ptp_clock ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

返回与此以太网网络接口关联的精确时间协议时钟（PTP Clock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：找到精确时间协议（PTP）时钟时返回其指针；未找到，或该以太网接口不支持 PTP 时，返回 `NULL`。

<a id="ga84c37db5687c5264bec99976a1108ab6"></a>

### `net_eth_get_ptp_clock_by_index()`

```c
const struct device * net_eth_get_ptp_clock_by_index ( int index)
```

```c
#include <zephyr/net/ethernet.h>
```

返回与此以太网网络接口索引关联的精确时间协议时钟（PTP Clock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 网络接口索引（Network interface index）。 |

**返回（Returns）**：返回值（Returns）：找到精确时间协议（PTP）时钟时返回其指针；未找到，或该以太网接口索引对应的接口不支持 PTP 时，返回 `NULL`。

<a id="gad9d890dcf7f5ee3659bf3bd5949faa4e"></a>

### `net_eth_get_vlan_iface()`

```c
struct net_if * net_eth_get_vlan_iface ( struct net_if * iface, uint16_t tag )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

返回与该虚拟局域网标签（VLAN Tag）相关联的网络接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 主网络接口（Main Network Interface），不是 VLAN 接口。 |
| `tag` | 虚拟局域网标签（VLAN Tag）。 |

**返回（Returns）**：返回值（Returns）：与此标签（Tag）关联的网络接口；不存在此类接口时返回 `NULL`。

<a id="ga010a95a0239a800131ac3d43dd54737f"></a>

### `net_eth_get_vlan_main()`

```c
struct net_if * net_eth_get_vlan_main ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

返回关联到该虚拟局域网标签（VLAN Tag）的主网络接口（Main Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | VLAN 网络接口（Network Interface），用于获取指向以太网链路层上下文（Ethernet L2 Context）的指针。 |

**返回（Returns）**：返回值（Returns）：与此标签（Tag）关联的网络接口；不存在此类接口时返回 `NULL`。

<a id="ga78aad58ec66710034cab8891ad638a2c"></a>

### `net_eth_get_vlan_status()`

```c
bool net_eth_get_vlan_status ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

获取给定网络接口的 VLAN 状态（VLAN Status），即是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：此网络接口启用了 VLAN 时为 `true`，否则为 `false`。

<a id="ga6184c43a62e4af9958412f99991358c9"></a>

### `net_eth_get_vlan_tag()`

```c
uint16_t net_eth_get_vlan_tag ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

返回为网络接口指定的虚拟局域网标签（VLAN Tag）。

注意，`interface` 参数必须是 VLAN 接口，而不是以太网接口（Ethernet Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | VLAN 网络接口（Network Interface）。 |

**返回（Returns）**：返回值（Returns）：此接口的 VLAN 标签（Tag）；如果该接口未配置 VLAN，则返回 `NET_VLAN_TAG_UNSPEC`。

<a id="ga26984472437a98b00c31156f75558134"></a>

### `net_eth_ipv4_mcast_to_mac_addr()`

```c
void net_eth_ipv4_mcast_to_mac_addr ( const struct net_in_addr * ipv4_addr, struct net_eth_addr * mac_addr )
```

```c
#include <zephyr/net/ethernet.h>
```

将 IPv4 组播地址（Multicast Address）转换为以太网地址（Ethernet Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ipv4_addr` | IPv4 多播地址（Multicast Address）。 |
| `mac_addr` | 以太网地址（Ethernet Address）的输出缓冲区。 |

<a id="ga93e498e99c155fc402a26a4429d044a0"></a>

### `net_eth_ipv6_mcast_to_mac_addr()`

```c
void net_eth_ipv6_mcast_to_mac_addr ( const struct net_in6_addr * ipv6_addr, struct net_eth_addr * mac_addr )
```

```c
#include <zephyr/net/ethernet.h>
```

将 IPv6 组播地址（Multicast Address）转换为以太网地址（Ethernet Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ipv6_addr` | IPv6 多播地址（Multicast Address）。 |
| `mac_addr` | 以太网地址（Ethernet Address）的输出缓冲区。 |

<a id="ga237aab2d07ffa84355981d02a4576ebe"></a>

### `net_eth_is_addr_all_zeroes()`

```c
bool net_eth_is_addr_all_zeroes ( struct net_eth_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查以太网 MAC 地址是否为全零地址（All-zero Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向以太网 MAC 地址（Ethernet MAC Address）的有效指针。 |

**返回（Returns）**：返回值（Returns）：地址为全零地址（All Zeroes Address）时为 `true`，否则为 `false`。

<a id="ga76a5fe39ce12478c666d87f4aec3d579"></a>

### `net_eth_is_addr_broadcast()`

```c
bool net_eth_is_addr_broadcast ( struct net_eth_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查以太网 MAC 地址是否为广播地址（Broadcast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向以太网 MAC 地址（Ethernet MAC Address）的有效指针。 |

**返回（Returns）**：返回值（Returns）：地址为广播地址（Broadcast Address）时为 `true`，否则为 `false`。

<a id="gaec6fb3c05792bdd30596137686f3251a"></a>

### `net_eth_is_addr_lldp_multicast()`

```c
bool net_eth_is_addr_lldp_multicast ( struct net_eth_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查以太网 MAC 地址是否为 LLDP 组播地址（LLDP Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向以太网 MAC 地址（Ethernet MAC Address）的有效指针。 |

**返回（Returns）**：返回值（Returns）：地址为 LLDP 多播地址（Multicast Address）时为 `true`，否则为 `false`。

<a id="ga2755ecb84e9759c24302e33a56a1fc84"></a>

### `net_eth_is_addr_multicast()`

```c
bool net_eth_is_addr_multicast ( struct net_eth_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查以太网 MAC 地址是否为组播地址（Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向以太网 MAC 地址（Ethernet MAC Address）的有效指针。 |

**返回（Returns）**：返回值（Returns）：地址为多播地址（Multicast Address）时为 `true`，否则为 `false`。

<a id="gaeddfa5b3ff6e356393114b351f87fe43"></a>

### `net_eth_is_addr_ptp_multicast()`

```c
bool net_eth_is_addr_ptp_multicast ( struct net_eth_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查以太网 MAC 地址是否为 PTP 组播地址（PTP Multicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向以太网 MAC 地址（Ethernet MAC Address）的有效指针。 |

**返回（Returns）**：返回值（Returns）：地址为 PTP 多播地址（Multicast Address）时为 `true`，否则为 `false`。

<a id="gae91a64c96e0a480927d92271092a158d"></a>

### `net_eth_is_addr_unicast()`

```c
bool net_eth_is_addr_unicast ( struct net_eth_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查以太网 MAC 地址是否为单播地址（Unicast Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向以太网 MAC 地址（Ethernet MAC Address）的有效指针。 |

**返回（Returns）**：返回值（Returns）：地址为单播地址（Unicast Address）时为 `true`，否则为 `false`。

<a id="ga89964de263029223d119f361fbd94bfd"></a>

### `net_eth_is_addr_unspecified()`

```c
bool net_eth_is_addr_unspecified ( struct net_eth_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查以太网 MAC 地址是否为未指定地址（Unspecified Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向以太网 MAC 地址（Ethernet MAC Address）的有效指针。 |

**返回（Returns）**：返回值（Returns）：地址为未指定地址（Unspecified Address）时为 `true`，否则为 `false`。

<a id="gaf20472f9d60e5cddffed2919b3091030"></a>

### `net_eth_is_addr_valid()`

```c
bool net_eth_is_addr_valid ( struct net_eth_addr * addr)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查以太网 MAC 地址是否有效（Valid）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 指向以太网 MAC 地址（Ethernet MAC Address）的有效指针。 |

**返回（Returns）**：返回值（Returns）：地址有效（Valid）时为 `true`，否则为 `false`。

<a id="gac536aa7154c4a8d194ec67efb68e275c"></a>

### `net_eth_is_vlan_enabled()`

```c
bool net_eth_is_vlan_enabled ( struct ethernet_context * ctx, struct net_if * iface )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查是否有 VLAN 接口在此特定以太网网络接口上启用，或者是否支持带优先级标签的帧（Priority Tagged Frame，标签为 0）。

注意，`iface` 必须是实际的以太网接口（Ethernet Interface），不能是虚拟 VLAN 接口（Virtual VLAN Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 以太网上下文（Ethernet Context）。 |
| `iface` | 以太网网络接口（Ethernet Network Interface）。 |

**返回（Returns）**：返回值（Returns）：此网络接口存在已启用的 VLAN 时为 `true`，否则为 `false`。

<a id="ga8ca1eccc88a351241298d358ec28fdf5"></a>

### `net_eth_is_vlan_interface()`

```c
bool net_eth_is_vlan_interface ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查给定接口是否为 VLAN 接口（VLAN Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

**返回（Returns）**：返回值（Returns）：此网络接口是 VLAN 接口时为 `true`，否则为 `false`。

<a id="ga920bddac077675d544a21fb5650c945e"></a>

### `net_eth_mac_filter()`

```c
int net_eth_mac_filter ( struct net_if * iface, struct net_eth_addr * mac, enum ethernet_filter_type type, bool enable )
```

```c
#include <zephyr/net/ethernet.h>
```

为 MAC 地址 `mac` 设置或取消硬件过滤（HW Filtering）。

多播目的地址（Multicast Destination Address）由 IP 协议栈和分组套接字（Packet Socket）所加入的组共享，因此仅在首个使用者请求时通知设备监听该地址，最后一个使用者退出时才通知设备停止监听。每次设置（Set）此类地址都必须与一次取消设置（Unset）配对；取消从未设置的地址会失败并返回 `-ENOENT`。源地址（Source Address）和单播目的地址（Unicast Destination Address）则直接原样交给设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `mac` | 指向以太网 MAC 地址（Ethernet MAC Address）的指针。 |
| `type` | 过滤器类型（Filter Type），为源（Source）或目的（Destination）。 |
| `enable` | 设置（Set，`true`）或取消设置（Unset，`false`）。 |

**返回（Returns）**：返回值（Returns）：成功设置或取消设置过滤器（Filter）时为 `0`，否则小于 `0`。

<a id="gaa0ef2f94fd18da9c5ea675b46faac8d0"></a>

### `net_eth_mac_load()`

```c
int net_eth_mac_load ( const struct net_eth_mac_config * cfg, uint8_t * mac_addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

从指定类型的 MAC 地址配置结构体（MAC Address Configuration Structure）加载 MAC 地址。

对于随机生成的 MAC 地址，全局／本地位（U/L）被设为本地管理地址（Locally Administered Address，LAA），单播／多播位（I/G）被清零，使其成为单播地址（Unicast Address）。

以太网 MAC 地址长度（Ethernet MAC Address Length）。译注：原文开头的 `<` 是注释标记残留。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cfg` | MAC 地址配置（MAC Address Configuration）。 |
| `mac_addr` | 用于保存结果 MAC 地址的缓冲区（Buffer），大小必须为 `NET_ETH_ADDR_LEN` 字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODATA` | 未加载 MAC 地址配置数据（MAC Address Configuration Data）。 |
| `<0` | 失败时为负 errno 错误码。 |
| `0` | 成功时。 |

<a id="ga3e578035be797bbbafafa56dedaa8320"></a>

### `net_eth_mcast_addr_add()`

```c
int net_eth_mcast_addr_add ( struct net_if * iface, const struct net_eth_addr * addr )
```

```c
#include <zephyr/net/ethernet.h>
```

在网络接口上加入一个二层组播组（L2 Multicast Group）。

将地址加入接口的多播地址（Multicast Address）集合；如果已经加入该组，则增加该地址的引用计数（Reference Count）。只有首个使用者加入该地址时，才配置设备的接收过滤器（Receive Filter）。没有接收过滤器的设备仍会将该组的数据上传，因此在这种情况下也会加入该组。

当 IP 层或分组套接字（Packet Socket）加入多播组（Multicast Group）时，由以太网链路层（Ethernet L2）自身调用。驱动程序无需调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | 要加入的多播 MAC 地址（Multicast MAC Address）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；接口无法再跟踪一个地址时为 `-ENOMEM`；其他错误返回小于 `0` 的值。

<a id="ga80adc03695a8fbb9dbc9dd3adec78c04"></a>

### `net_eth_mcast_addr_foreach()`

```c
void net_eth_mcast_addr_foreach ( struct net_if * iface, net_eth_mcast_addr_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/ethernet.h>
```

遍历网络接口的所有二层组播地址（L2 Multicast Address）。

收到 `ETHERNET_CONFIG_TYPE_FILTER` 请求时会重新配置整个接收过滤器（Receive Filter）的驱动程序，可以用此函数确定设备应监听哪些地址。回调不得加入或退出组（Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `cb` | 针对每个多播地址（Multicast Address）调用的回调。 |
| `user_data` | 传给回调（Callback）的数据。 |

<a id="ga3cd2e9abc38bdd7eb0cb3932d96fd90e"></a>

### `net_eth_mcast_addr_rm()`

```c
int net_eth_mcast_addr_rm ( struct net_if * iface, const struct net_eth_addr * addr )
```

```c
#include <zephyr/net/ethernet.h>
```

在网络接口上离开一个二层组播组（L2 Multicast Group）。

减少该地址的引用计数（Reference Count）；如果这是最后一个使用者，则将该地址从接口的多播地址（Multicast Address）集合中移除。只有最后一个使用者退出该地址时，才重新配置设备的接收过滤器（Receive Filter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `addr` | 要退出的多播 MAC 地址（Multicast MAC Address）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；此前未加入该组时为 `-ENOENT`；其他错误返回小于 `0` 的值。

<a id="ga42a3c6b04ef8827e3443c5aebe5541b9"></a>

### `net_eth_promisc_mode()`

```c
int net_eth_promisc_mode ( struct net_if * iface, bool enable )
```

```c
#include <zephyr/net/ethernet.h>
```

开启或关闭混杂模式（Promiscuous Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `enable` | 开启（On，`true`）或关闭（Off，`false`）。 |

**返回（Returns）**：返回值（Returns）：成功设置或取消该模式（Mode）时为 `0`，否则小于 `0`。

<a id="gaa64462598843dd9f6e731198498aea31"></a>

### `net_eth_set_if_type_wifi()`

```c
void net_eth_set_if_type_wifi ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

将以太网接口类型（Ethernet Interface Type）设置为 Wi-Fi。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

<a id="gafbb76d53f9f80628d18d39368a28f984"></a>

### `net_eth_txinjection_mode()`

```c
int net_eth_txinjection_mode ( struct net_if * iface, bool enable )
```

```c
#include <zephyr/net/ethernet.h>
```

开启或关闭发送注入模式（TX-Injection Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `enable` | 开启（On，`true`）或关闭（Off，`false`）。 |

**返回（Returns）**：返回值（Returns）：成功设置或取消该模式（Mode）时为 `0`，否则小于 `0`。

<a id="gae617887d42a288697f2507c5b0907909"></a>

### `net_eth_type_is_ethernet()`

```c
bool net_eth_type_is_ethernet ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查以太网二层网络接口（Ethernet L2 Network Interface）是否为有线以太网（Cabled Ethernet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值（Returns）：接口为有线以太网（Cabled Ethernet）时为 `true`，否则为 `false`。

<a id="ga6e603f6f74e6d7e988e7119a6df2ab4d"></a>

### `net_eth_type_is_wifi()`

```c
bool net_eth_type_is_wifi ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

检查以太网二层网络接口（Ethernet L2 Network Interface）能否执行 Wi-Fi 功能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值：接口支持 Wi-Fi 时为 true，否则为 false。

<a id="gab71a741cea5f645f4354a1abc9c95a50"></a>

### `net_eth_vlan_disable()`

```c
int net_eth_vlan_disable ( struct net_if * iface, uint16_t tag )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

从接口移除虚拟局域网标签（VLAN Tag）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface）。 |
| `tag` | 要移除的 VLAN 标签（Tag）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga16cbc14e3a0a470bbbd5aeb5e73dc1de"></a>

### `net_eth_vlan_enable()`

```c
int net_eth_vlan_enable ( struct net_if * iface, uint16_t tag )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet.h>
```

为接口添加虚拟局域网标签（VLAN Tag）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要使用的接口（Interface）。 |
| `tag` | 要添加的 VLAN 标签（Tag）。 |

返回（Returns）：成功时为0，出错时小于0。


## 7.9\_原页交叉引用（Cross References）

- [分布式交换架构标签协议（DSA tag protocol）](../api_platform_topic_reference/P014_分布式交换架构标签协议（DSA tag protocol）.md)
- [以太网介质无关接口支持函数（Ethernet MII Support Functions）](../api_media_cellular_topic_reference/P011_以太网介质无关接口支持函数（Ethernet MII Support Functions）.md)
- [IEEE 802.3 管理接口。](../api_iso_dns_lin_topic_reference/P008_IEEE 802.3 管理接口。.md)
- [eth_adin2111.h](../api_file_mesh_interrupt_reference/P007_zephyr__drivers__ethernet__eth_adin2111.h_文件参考.md)
- [eth_nxp_enet.h](../api_file_reference/P109_zephyr__drivers__ethernet__eth_nxp_enet.h_文件参考.md)
- [eth_nxp_enet_qos.h](../api_file_reference/P110_zephyr__drivers__ethernet__eth_nxp_enet_qos.h_文件参考.md)
- [net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)
- [ethernet_qav_param](../network_service_model_reference/P010_ethernet_qav_param_结构体.md)
- [ethernet_qbv_param](../network_service_model_reference/P012_ethernet_qbv_param_结构体.md)
- [ethernet_qbu_param](../network_service_model_reference/P011_ethernet_qbu_param_结构体.md)
- [ethernet_filter](../network_service_model_reference/P008_ethernet_filter_结构体.md)
- [net_eth_mcast_addr](../network_core_model_reference/P061_net_eth_mcast_addr_结构体.md)
- [ethernet_txtime_param](../network_service_model_reference/P013_ethernet_txtime_param_结构体.md)
- [ethernet_api](../network_service_model_reference/P007_ethernet_api_结构体.md)
- [ethernet_lldp](../network_service_model_reference/P009_ethernet_lldp_结构体.md)
- [net_eth_mac_config](../network_core_model_reference/P060_net_eth_mac_config_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [device](../device_reference/P002_设备对象结构.md)
- [zephyr/net/ethernet.h](../api_file_usb_network_reference/P008_zephyr__net__ethernet.h_文件参考.md)
- [DEVICE_DT_NAME](../device_reference/P001_设备模型公共接口.md#gad864d7a50ee45285dacd68be1e5a49ce)
- [pm_device](../power/P039_通用设备运行时电源结构.md)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DT_INVALID_NODE](../dt_identity_reference/P001_设备树节点标识宏.md#ga710cc4455dd7e738f43f750153163855)
- [COND_CASE_1](../util_reference/P001_通用工具公共接口.md#ga0325a11d188ce0d7f2fddc4b74947478)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [DT_NVMEM_CELLS_HAS_NAME](../storage/P018_NVMEM设备树辅助宏.md#ga75c4f7ef73d6802dec48be9a9a042811)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [CONFIG_NVMEM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_gad864d7a50ee45285dacd68be1e5a49ce"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__ethernet_html_ga9f67fee695953f24b1e5d9e49041aa99"></a>
<a id="agroup__devicetree-generic-id_html_ga710cc4455dd7e738f43f750153163855"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__devicetree-nvmem_html_ga75c4f7ef73d6802dec48be9a9a042811"></a>
<a id="agroup__sys-util_html_ga0325a11d188ce0d7f2fddc4b74947478"></a>
<a id="agroup__ethernet_html_ga59882ff8ad5a11c20c08f296edad367e"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggabf86b7f09a9d041eea25357cd7a85edea90314c44dca3c123d1a0bd70f108524d"></a>
<a id="ggabf86b7f09a9d041eea25357cd7a85edea6485d2abcd3dae6786022aa286234ed4"></a>
<a id="ggabf86b7f09a9d041eea25357cd7a85edea5671ade139cb0cd28d02e3215337acb9"></a>
<a id="ggabf86b7f09a9d041eea25357cd7a85edea557127c3bc97969fe57fcd8ac55567b5"></a>
<a id="ggabf86b7f09a9d041eea25357cd7a85edeac64b392a0591cfe7aa5564a476fe20be"></a>
<a id="ggabf86b7f09a9d041eea25357cd7a85edea3346f0e3d0b350c7fe663cfe389c1e02"></a>
<a id="ggabf86b7f09a9d041eea25357cd7a85edea03e31130ecef7ac032bceed6f3091af8"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a4508489dc8a67ef908757a9e2338babb"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a2c59d7d5a1d5eff15976806d237960c1"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a55e8d0ee975acc9eabf5096d1b926f6b"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5afe48cf59ca4d1db42e768ca272159d55"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a9ab79aee30b73747fceff86fd3b967f9"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a12991c85e1a7405bd145b3fff8aeecf1"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a2eeaa2befc2d7a38f0318addef88f072"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2"></a>
<a id="gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b"></a>
<a id="gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530"></a>
<a id="gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671"></a>
<a id="ggabfab900bfd7a9078e7ac2fd6aed9ce83ad41e45f16877f28b44ec23fadb35d355"></a>
<a id="ggabfab900bfd7a9078e7ac2fd6aed9ce83a3a094b0237833d4523e04d7b6bb5fbab"></a>
<a id="ggabfab900bfd7a9078e7ac2fd6aed9ce83a6bb1bfaf79f232101bc91ab02f54e4a7"></a>
<a id="ggac2433b0d82ef25373b2c0f994e248e92a8b1eb5edcd9f4953d56c9c10088d6bb5"></a>
<a id="ggac2433b0d82ef25373b2c0f994e248e92a3fad5d3a2578e83da31f3188add46b87"></a>
<a id="ggac2433b0d82ef25373b2c0f994e248e92a730e86dd6e257352afb233fdcc189955"></a>
<a id="ggac2433b0d82ef25373b2c0f994e248e92a9e0096f69300cf30c1f78c33074c1bda"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_配置客户端模型（Configuration Client Model）.md) · [返回大纲](大纲.md) · [下一章](P008_FIDO2 API主题.md)
