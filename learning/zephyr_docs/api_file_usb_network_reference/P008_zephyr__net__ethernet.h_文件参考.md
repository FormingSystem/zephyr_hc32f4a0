---
id: learning.zephyr-docs.api-file-usb-network-reference.page-8
title: zephyr__net__ethernet.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_net\_\_ethernet.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网（Ethernet）。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_pkt.h>
#include <zephyr/net/lldp.h>
#include <zephyr/sys/clock.h>
#include <zephyr/sys/util.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/ethernet_vlan.h>
#include <zephyr/net/ptp_time.h>
#include <zephyr/net/virtual.h>
#include <zephyr/random/random.h>
#include <zephyr/syscalls/ethernet.h>
```

查看此文件的源码。

以太网（Ethernet）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

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

## 8.2\_宏定义（Macros）

<a id="r_ga399425f810c00bcf9babec019bc2ff12"></a>

```c
#define NET_ETH_ADDR_LEN 6U
```

相关声明：[NET_ETH_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga399425f810c00bcf9babec019bc2ff12)。

以太网 MAC 地址长度（Ethernet MAC Address Length）。

<a id="r_ga4cc1bb4cfa00b7749838eae3ae11048c"></a>

```c
#define NET_ETH_MINIMAL_FRAME_SIZE 60
```

相关声明：[NET_ETH_MINIMAL_FRAME_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga4cc1bb4cfa00b7749838eae3ae11048c)。

以太网最小帧大小（Minimum Ethernet Frame Size）。

<a id="r_gaa337199b1edc50c9003afa5c3a951d8b"></a>

```c
#define NET_ETH_MTU 1500
```

相关声明：[NET_ETH_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa337199b1edc50c9003afa5c3a951d8b)。

以太网最大传输单元大小（Ethernet MTU Size）。

<a id="r_ga197e02748be8eaf410f7deb57c984642"></a>

```c
#define ETH_NET_DEVICE_INIT(dev_id, name, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[ETH_NET_DEVICE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga197e02748be8eaf410f7deb57c984642)。

创建以太网网络接口（Ethernet Network Interface），并将其绑定到网络设备（Network Device）。

<a id="r_ga3dc27a54b7ae178e8c4daeba4c84aab0"></a>

```c
#define ETH_NET_DEVICE_INIT_INSTANCE(dev_id, name, instance, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[ETH_NET_DEVICE_INIT_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga3dc27a54b7ae178e8c4daeba4c84aab0)。

创建多个以太网网络接口（Ethernet Network Interface），并将它们绑定到网络设备（Network Device）。

<a id="r_ga9f67fee695953f24b1e5d9e49041aa99"></a>

```c
#define ETH_NET_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, prio, api, mtu)
```

相关声明：[ETH_NET_DEVICE_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9f67fee695953f24b1e5d9e49041aa99)。

与 `ETH_NET_DEVICE_INIT` 类似，但从设备树（Devicetree）获取元数据。

<a id="r_gaecf9f102108836ed9cf7e2cdb3c90579"></a>

```c
#define ETH_NET_DEVICE_DT_INST_DEFINE(inst, ...)
```

相关声明：[ETH_NET_DEVICE_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaecf9f102108836ed9cf7e2cdb3c90579)。

针对兼容标识符为 `DT_DRV_COMPAT` 的实例，提供与 `ETH_NET_DEVICE_DT_DEFINE` 类似的功能。

<a id="r_gaf6524602e433313c15ea2cef762ff0dc"></a>

```c
#define ETH_NET_L3_REGISTER(name, ptype, handler)
```

相关声明：[ETH_NET_L3_REGISTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaf6524602e433313c15ea2cef762ff0dc)。

以太网 L3 协议注册宏（Ethernet L3 Protocol Register Macro）。

<a id="r_ga59882ff8ad5a11c20c08f296edad367e"></a>

```c
#define NET_ETH_MAC_DT_CONFIG_INIT(node_id)
```

相关声明：[NET_ETH_MAC_DT_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga59882ff8ad5a11c20c08f296edad367e)。

为给定设备树节点标识符（DT Node Identifier）初始化以太网 MAC 配置（Ethernet MAC Config）。

<a id="r_gac1bb10b6bcc64911128814b9b9de1926"></a>

```c
#define NET_ETH_MAC_DT_INST_CONFIG_INIT(inst)
```

相关声明：[NET_ETH_MAC_DT_INST_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac1bb10b6bcc64911128814b9b9de1926)。

针对兼容标识符为 `DT_DRV_COMPAT` 的实例，提供与 `NET_ETH_MAC_DT_CONFIG_INIT` 类似的功能。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.3\_类型定义（Typedefs）

<a id="r_ga8d28addcef0038c4ba1daa84bc104143"></a>

```c
typedef void(* net_eth_mcast_addr_cb_t) (struct net_if *iface, const struct net_eth_mcast_addr *addr, void *user_data)
```

相关声明：[net_eth_mcast_addr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga8d28addcef0038c4ba1daa84bc104143)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_mcast_addr](../network_core_model_reference/P061_net_eth_mcast_addr_结构体.md)。

由 `net_eth_mcast_addr_foreach()` 使用的回调（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.4\_枚举（Enumerations）

<a id="r_ga9162ff11d626813fc840df0b67820ac5"></a>

```c
enum ethernet_hw_caps { ETHERNET_HW_TX_CHKSUM_OFFLOAD = BIT(0) , ETHERNET_HW_RX_CHKSUM_OFFLOAD = BIT(1) , ETHERNET_HW_VLAN = BIT(2) , ETHERNET_LINK_10BASE = BIT(3) , ETHERNET_LINK_100BASE = BIT(4) , ETHERNET_LINK_1000BASE = BIT(5) , ETHERNET_LINK_2500BASE = BIT(6) , ETHERNET_LINK_5000BASE = BIT(7) , ETHERNET_QAV = BIT(9) , ETHERNET_PROMISC_MODE = BIT(10) , ETHERNET_PRIORITY_QUEUES = BIT(11) , ETHERNET_HW_FILTERING = BIT(12) , ETHERNET_LLDP = BIT(13) , ETHERNET_HW_VLAN_TAG_STRIP = BIT(14) , ETHERNET_DSA_USER_PORT = BIT(15) , ETHERNET_DSA_CONDUIT_PORT = BIT(16) , ETHERNET_QBV = BIT(17) , ETHERNET_QBU = BIT(18) , ETHERNET_TXTIME = BIT(19) , ETHERNET_TXINJECTION_MODE = BIT(20) }
```

相关声明：[ethernet_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9162ff11d626813fc840df0b67820ac5)、[ETHERNET_HW_TX_CHKSUM_OFFLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861)、[ETHERNET_HW_RX_CHKSUM_OFFLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33)、[ETHERNET_HW_VLAN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95)、[ETHERNET_LINK_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a4508489dc8a67ef908757a9e2338babb)、[ETHERNET_LINK_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a2c59d7d5a1d5eff15976806d237960c1)、[ETHERNET_LINK_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a55e8d0ee975acc9eabf5096d1b926f6b)、[ETHERNET_LINK_2500BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5afe48cf59ca4d1db42e768ca272159d55)、[ETHERNET_LINK_5000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a9ab79aee30b73747fceff86fd3b967f9)、[ETHERNET_QAV](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42)、[ETHERNET_PROMISC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d)、[ETHERNET_PRIORITY_QUEUES](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475)、[ETHERNET_HW_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe)、[ETHERNET_LLDP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2)、[ETHERNET_HW_VLAN_TAG_STRIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5)、[ETHERNET_DSA_USER_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a12991c85e1a7405bd145b3fff8aeecf1)、[ETHERNET_DSA_CONDUIT_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a2eeaa2befc2d7a38f0318addef88f072)、[ETHERNET_QBV](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85)、[ETHERNET_QBU](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08)、[ETHERNET_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2)、[ETHERNET_TXINJECTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b)。

以太网硬件能力（Ethernet Hardware Capabilities）。

<a id="r_ga139cc696837611a522b289f2ea7bf6fc"></a>

```c
enum ethernet_if_types { L2_ETH_IF_TYPE_ETHERNET , L2_ETH_IF_TYPE_WIFI }
```

相关声明：[ethernet_if_types](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga139cc696837611a522b289f2ea7bf6fc)、[L2_ETH_IF_TYPE_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530)、[L2_ETH_IF_TYPE_WIFI](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671)。

以太网二层类型（Ethernet L2 Types）。

<a id="r_gabf86b7f09a9d041eea25357cd7a85ede"></a>

```c
enum ethernet_checksum_support { ETHERNET_CHECKSUM_SUPPORT_NONE = NET_IF_CHECKSUM_NONE_BIT , ETHERNET_CHECKSUM_SUPPORT_IPV4_HEADER = NET_IF_CHECKSUM_IPV4_HEADER_BIT , ETHERNET_CHECKSUM_SUPPORT_IPV4_ICMP = NET_IF_CHECKSUM_IPV4_ICMP_BIT , ETHERNET_CHECKSUM_SUPPORT_IPV6_HEADER = NET_IF_CHECKSUM_IPV6_HEADER_BIT , ETHERNET_CHECKSUM_SUPPORT_IPV6_ICMP = NET_IF_CHECKSUM_IPV6_ICMP_BIT , ETHERNET_CHECKSUM_SUPPORT_TCP = NET_IF_CHECKSUM_TCP_BIT , ETHERNET_CHECKSUM_SUPPORT_UDP = NET_IF_CHECKSUM_UDP_BIT }
```

相关声明：[ethernet_checksum_support](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gabf86b7f09a9d041eea25357cd7a85ede)、[ETHERNET_CHECKSUM_SUPPORT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea90314c44dca3c123d1a0bd70f108524d)、[ETHERNET_CHECKSUM_SUPPORT_IPV4_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea6485d2abcd3dae6786022aa286234ed4)、[ETHERNET_CHECKSUM_SUPPORT_IPV4_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea5671ade139cb0cd28d02e3215337acb9)、[ETHERNET_CHECKSUM_SUPPORT_IPV6_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea557127c3bc97969fe57fcd8ac55567b5)、[ETHERNET_CHECKSUM_SUPPORT_IPV6_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edeac64b392a0591cfe7aa5564a476fe20be)、[ETHERNET_CHECKSUM_SUPPORT_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea3346f0e3d0b350c7fe663cfe389c1e02)、[ETHERNET_CHECKSUM_SUPPORT_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea03e31130ecef7ac032bceed6f3091af8)。

校验和卸载（Checksum Offloading）支持的协议。

<a id="r_gabfab900bfd7a9078e7ac2fd6aed9ce83"></a>

```c
enum ethernet_stats_type { ETHERNET_STATS_TYPE_COMMON = BIT(0) , ETHERNET_STATS_TYPE_VENDOR = BIT(1) , ETHERNET_STATS_TYPE_ALL = 0xFFFFFFFFU }
```

相关声明：[ethernet_stats_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gabfab900bfd7a9078e7ac2fd6aed9ce83)、[ETHERNET_STATS_TYPE_COMMON](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabfab900bfd7a9078e7ac2fd6aed9ce83ad41e45f16877f28b44ec23fadb35d355)、[ETHERNET_STATS_TYPE_VENDOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabfab900bfd7a9078e7ac2fd6aed9ce83a3a094b0237833d4523e04d7b6bb5fbab)、[ETHERNET_STATS_TYPE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabfab900bfd7a9078e7ac2fd6aed9ce83a6bb1bfaf79f232101bc91ab02f54e4a7)。

以太网统计类型（Ethernet Statistics Type），采用位图（Bitmap）表示。

<a id="r_gac2433b0d82ef25373b2c0f994e248e92"></a>

```c
enum net_eth_mac_type { NET_ETH_MAC_DEFAULT = 0 , NET_ETH_MAC_RANDOM , NET_ETH_MAC_NVMEM , NET_ETH_MAC_STATIC }
```

相关声明：[net_eth_mac_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac2433b0d82ef25373b2c0f994e248e92)、[NET_ETH_MAC_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a8b1eb5edcd9f4953d56c9c10088d6bb5)、[NET_ETH_MAC_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a3fad5d3a2578e83da31f3188add46b87)、[NET_ETH_MAC_NVMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a730e86dd6e257352afb233fdcc189955)、[NET_ETH_MAC_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a9e0096f69300cf30c1f78c33074c1bda)。

MAC 地址配置类型（MAC Address Configuration Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.5\_函数（Functions）

<a id="r_ga76a5fe39ce12478c666d87f4aec3d579"></a>

```c
static bool net_eth_is_addr_broadcast (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga76a5fe39ce12478c666d87f4aec3d579)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为广播地址（Broadcast Address）。

<a id="r_ga237aab2d07ffa84355981d02a4576ebe"></a>

```c
static bool net_eth_is_addr_all_zeroes (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_all_zeroes](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga237aab2d07ffa84355981d02a4576ebe)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为全零地址（All-zero Address）。

<a id="r_ga89964de263029223d119f361fbd94bfd"></a>

```c
static bool net_eth_is_addr_unspecified (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_unspecified](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga89964de263029223d119f361fbd94bfd)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为未指定地址（Unspecified Address）。

<a id="r_ga2755ecb84e9759c24302e33a56a1fc84"></a>

```c
static bool net_eth_is_addr_multicast (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_multicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga2755ecb84e9759c24302e33a56a1fc84)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为组播地址（Multicast Address）。

<a id="r_gae91a64c96e0a480927d92271092a158d"></a>

```c
static bool net_eth_is_addr_unicast (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_unicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gae91a64c96e0a480927d92271092a158d)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为单播地址（Unicast Address）。

<a id="r_gaf20472f9d60e5cddffed2919b3091030"></a>

```c
static bool net_eth_is_addr_valid (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaf20472f9d60e5cddffed2919b3091030)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否有效（Valid）。

<a id="r_gaec6fb3c05792bdd30596137686f3251a"></a>

```c
static bool net_eth_is_addr_lldp_multicast (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_lldp_multicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaec6fb3c05792bdd30596137686f3251a)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为 LLDP 组播地址（LLDP Multicast Address）。

<a id="r_gaeddfa5b3ff6e356393114b351f87fe43"></a>

```c
static bool net_eth_is_addr_ptp_multicast (struct net_eth_addr *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_addr_ptp_multicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaeddfa5b3ff6e356393114b351f87fe43)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

检查以太网 MAC 地址是否为 PTP 组播地址（PTP Multicast Address）。

<a id="r_gae66b24a847f8e0ad119c6c466331afd6"></a>

```c
const struct net_eth_addr * net_eth_broadcast_addr (void)
```

相关声明：[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)、[net_eth_broadcast_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gae66b24a847f8e0ad119c6c466331afd6)。

返回以太网广播地址（Ethernet Broadcast Address）。

<a id="r_ga26984472437a98b00c31156f75558134"></a>

```c
void net_eth_ipv4_mcast_to_mac_addr (const struct net_in_addr *ipv4_addr, struct net_eth_addr *mac_addr)
```

相关声明：[net_eth_ipv4_mcast_to_mac_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga26984472437a98b00c31156f75558134)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

将 IPv4 组播地址（Multicast Address）转换为以太网地址（Ethernet Address）。

<a id="r_ga93e498e99c155fc402a26a4429d044a0"></a>

```c
void net_eth_ipv6_mcast_to_mac_addr (const struct net_in6_addr *ipv6_addr, struct net_eth_addr *mac_addr)
```

相关声明：[net_eth_ipv6_mcast_to_mac_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga93e498e99c155fc402a26a4429d044a0)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

将 IPv6 组播地址（Multicast Address）转换为以太网地址（Ethernet Address）。

<a id="r_ga3e578035be797bbbafafa56dedaa8320"></a>

```c
int net_eth_mcast_addr_add (struct net_if *iface, const struct net_eth_addr *addr)
```

相关声明：[net_eth_mcast_addr_add](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga3e578035be797bbbafafa56dedaa8320)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

在网络接口上加入一个二层组播组（L2 Multicast Group）。

<a id="r_ga3cd2e9abc38bdd7eb0cb3932d96fd90e"></a>

```c
int net_eth_mcast_addr_rm (struct net_if *iface, const struct net_eth_addr *addr)
```

相关声明：[net_eth_mcast_addr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga3cd2e9abc38bdd7eb0cb3932d96fd90e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)。

在网络接口上离开一个二层组播组（L2 Multicast Group）。

<a id="r_ga80adc03695a8fbb9dbc9dd3adec78c04"></a>

```c
void net_eth_mcast_addr_foreach (struct net_if *iface, net_eth_mcast_addr_cb_t cb, void *user_data)
```

相关声明：[net_eth_mcast_addr_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga80adc03695a8fbb9dbc9dd3adec78c04)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_mcast_addr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga8d28addcef0038c4ba1daa84bc104143)。

遍历网络接口的所有二层组播地址（L2 Multicast Address）。

<a id="r_gab0a3b4584bb6ce1d27b98b063fd3fcbd"></a>

```c
static enum ethernet_hw_caps net_eth_get_hw_capabilities (struct net_if *iface)
```

相关声明：[ethernet_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9162ff11d626813fc840df0b67820ac5)、[net_eth_get_hw_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gab0a3b4584bb6ce1d27b98b063fd3fcbd)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回以太网设备的硬件能力信息（Hardware Capability Information）。

<a id="r_ga1246be489eb7130100bbaebbb73961c5"></a>

```c
static int net_eth_get_hw_config (struct net_if *iface, enum ethernet_config_type type, struct ethernet_config *config)
```

相关声明：[net_eth_get_hw_config](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga1246be489eb7130100bbaebbb73961c5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回以太网设备的硬件配置信息（Hardware Configuration Information）。

<a id="r_ga16cbc14e3a0a470bbbd5aeb5e73dc1de"></a>

```c
static int net_eth_vlan_enable (struct net_if *iface, uint16_t tag)
```

相关声明：[net_eth_vlan_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

为接口添加虚拟局域网标签（VLAN Tag）。

<a id="r_gab71a741cea5f645f4354a1abc9c95a50"></a>

```c
static int net_eth_vlan_disable (struct net_if *iface, uint16_t tag)
```

相关声明：[net_eth_vlan_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gab71a741cea5f645f4354a1abc9c95a50)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从接口移除虚拟局域网标签（VLAN Tag）。

<a id="r_ga6184c43a62e4af9958412f99991358c9"></a>

```c
static uint16_t net_eth_get_vlan_tag (struct net_if *iface)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_eth_get_vlan_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga6184c43a62e4af9958412f99991358c9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回为网络接口指定的虚拟局域网标签（VLAN Tag）。

<a id="r_gad9d890dcf7f5ee3659bf3bd5949faa4e"></a>

```c
static struct net_if * net_eth_get_vlan_iface (struct net_if *iface, uint16_t tag)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_get_vlan_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gad9d890dcf7f5ee3659bf3bd5949faa4e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

返回与该虚拟局域网标签（VLAN Tag）相关联的网络接口。

<a id="r_ga010a95a0239a800131ac3d43dd54737f"></a>

```c
static struct net_if * net_eth_get_vlan_main (struct net_if *iface)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_get_vlan_main](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga010a95a0239a800131ac3d43dd54737f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回关联到该虚拟局域网标签（VLAN Tag）的主网络接口（Main Network Interface）。

<a id="r_gac536aa7154c4a8d194ec67efb68e275c"></a>

```c
static bool net_eth_is_vlan_enabled (struct ethernet_context *ctx, struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_vlan_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac536aa7154c4a8d194ec67efb68e275c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查是否有 VLAN 接口在此特定以太网网络接口上启用，或者是否支持带优先级标签的帧（Priority Tagged Frame，标签为 0）。

<a id="r_ga78aad58ec66710034cab8891ad638a2c"></a>

```c
static bool net_eth_get_vlan_status (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_get_vlan_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga78aad58ec66710034cab8891ad638a2c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取给定网络接口的 VLAN 状态（VLAN Status），即是否已启用。

<a id="r_ga8ca1eccc88a351241298d358ec28fdf5"></a>

```c
static bool net_eth_is_vlan_interface (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_is_vlan_interface](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga8ca1eccc88a351241298d358ec28fdf5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查给定接口是否为 VLAN 接口（VLAN Interface）。

<a id="r_gaa0ef2f94fd18da9c5ea675b46faac8d0"></a>

```c
static int net_eth_mac_load (const struct net_eth_mac_config *cfg, uint8_t *mac_addr)
```

相关声明：[net_eth_mac_load](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa0ef2f94fd18da9c5ea675b46faac8d0)、[net_eth_mac_config](../network_core_model_reference/P060_net_eth_mac_config_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从指定类型的 MAC 地址配置结构体（MAC Address Configuration Structure）加载 MAC 地址。

<a id="r_gaa7f447129b5b8392640f849d18e9246b"></a>

```c
void net_eth_carrier_set (struct net_if *iface, bool carrier_up)
```

相关声明：[net_eth_carrier_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa7f447129b5b8392640f849d18e9246b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

通知以太网二层驱动（Ethernet L2 Driver）已检测到载波（Carrier），或载波已丢失。

<a id="r_ga62b33344256bbe228689e2cb541a0874"></a>

```c
static void net_eth_carrier_on (struct net_if *iface)
```

相关声明：[net_eth_carrier_on](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga62b33344256bbe228689e2cb541a0874)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

通知以太网二层驱动（Ethernet L2 Driver）已检测到载波（Carrier）。

<a id="r_ga97ef5a8ad9157e2db12e9caf6faef5e7"></a>

```c
static void net_eth_carrier_off (struct net_if *iface)
```

相关声明：[net_eth_carrier_off](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga97ef5a8ad9157e2db12e9caf6faef5e7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

通知以太网二层驱动（Ethernet L2 Driver）载波（Carrier）已丢失。

<a id="r_ga42a3c6b04ef8827e3443c5aebe5541b9"></a>

```c
int net_eth_promisc_mode (struct net_if *iface, bool enable)
```

相关声明：[net_eth_promisc_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga42a3c6b04ef8827e3443c5aebe5541b9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

开启或关闭混杂模式（Promiscuous Mode）。

<a id="r_gafbb76d53f9f80628d18d39368a28f984"></a>

```c
int net_eth_txinjection_mode (struct net_if *iface, bool enable)
```

相关声明：[net_eth_txinjection_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gafbb76d53f9f80628d18d39368a28f984)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

开启或关闭发送注入模式（TX-Injection Mode）。

<a id="r_ga920bddac077675d544a21fb5650c945e"></a>

```c
int net_eth_mac_filter (struct net_if *iface, struct net_eth_addr *mac, enum ethernet_filter_type type, bool enable)
```

相关声明：[net_eth_mac_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga920bddac077675d544a21fb5650c945e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为 MAC 地址 `mac` 设置或取消硬件过滤（HW Filtering）。

<a id="r_ga7225d06fbaa12d4668fa165d9e8f0845"></a>

```c
const struct device * net_eth_get_phy (struct net_if *iface)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[net_eth_get_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga7225d06fbaa12d4668fa165d9e8f0845)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回与此以太网网络接口关联的物理层设备（PHY Device）。

<a id="r_ga37ff48434c56bbb24422dd805449b6f3"></a>

```c
static const struct device * net_eth_get_ptp_clock (struct net_if *iface)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[net_eth_get_ptp_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga37ff48434c56bbb24422dd805449b6f3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

返回与此以太网网络接口关联的精确时间协议时钟（PTP Clock）。

<a id="r_ga84c37db5687c5264bec99976a1108ab6"></a>

```c
const struct device * net_eth_get_ptp_clock_by_index (int index)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[net_eth_get_ptp_clock_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga84c37db5687c5264bec99976a1108ab6)。

返回与此以太网网络接口索引关联的精确时间协议时钟（PTP Clock）。

<a id="r_ga6e603f6f74e6d7e988e7119a6df2ab4d"></a>

```c
static bool net_eth_type_is_wifi (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_type_is_wifi](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga6e603f6f74e6d7e988e7119a6df2ab4d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查以太网二层网络接口（Ethernet L2 Network Interface）能否执行 Wi-Fi 功能。

<a id="r_gae617887d42a288697f2507c5b0907909"></a>

```c
static bool net_eth_type_is_ethernet (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_eth_type_is_ethernet](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gae617887d42a288697f2507c5b0907909)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查以太网二层网络接口（Ethernet L2 Network Interface）是否为有线以太网（Cabled Ethernet）。

<a id="r_gaa64462598843dd9f6e731198498aea31"></a>

```c
static void net_eth_set_if_type_wifi (struct net_if *iface)
```

相关声明：[net_eth_set_if_type_wifi](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa64462598843dd9f6e731198498aea31)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将以太网接口类型（Ethernet Interface Type）设置为 Wi-Fi。


## 8.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/net_pkt.h](../api_source_packet_gnss_reference/P006_net_pkt.h_源码浏览.md)
- [zephyr/net/lldp.h](../api_source_network_reference/P012_lldp.h_源码浏览.md)
- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/ethernet_vlan.h](../api_source_reference/P247_ethernet_vlan.h_源码浏览.md)
- [zephyr/net/ptp_time.h](../api_source_reference/P681_ptp_time.h_源码浏览.md)
- [zephyr/net/virtual.h](../api_source_device_reference/P055_virtual.h_源码浏览.md)
- [zephyr/random/random.h](../data_utilities/P009_随机数头文件源码.md)
- [查看此文件的源码。](../api_source_socket_ethernet_reference/P003_ethernet.h_源码浏览.md)
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
- [NET_ETH_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga399425f810c00bcf9babec019bc2ff12)
- [NET_ETH_MINIMAL_FRAME_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga4cc1bb4cfa00b7749838eae3ae11048c)
- [NET_ETH_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa337199b1edc50c9003afa5c3a951d8b)
- [ETH_NET_DEVICE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga197e02748be8eaf410f7deb57c984642)
- [ETH_NET_DEVICE_INIT_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga3dc27a54b7ae178e8c4daeba4c84aab0)
- [ETH_NET_DEVICE_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9f67fee695953f24b1e5d9e49041aa99)
- [ETH_NET_DEVICE_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaecf9f102108836ed9cf7e2cdb3c90579)
- [ETH_NET_L3_REGISTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaf6524602e433313c15ea2cef762ff0dc)
- [NET_ETH_MAC_DT_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga59882ff8ad5a11c20c08f296edad367e)
- [NET_ETH_MAC_DT_INST_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac1bb10b6bcc64911128814b9b9de1926)
- [net_eth_mcast_addr_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga8d28addcef0038c4ba1daa84bc104143)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_eth_mcast_addr_foreach()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga80adc03695a8fbb9dbc9dd3adec78c04)
- [ethernet_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9162ff11d626813fc840df0b67820ac5)
- [ETHERNET_HW_TX_CHKSUM_OFFLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861)
- [ETHERNET_HW_RX_CHKSUM_OFFLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33)
- [ETHERNET_HW_VLAN](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95)
- [ETHERNET_LINK_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a4508489dc8a67ef908757a9e2338babb)
- [ETHERNET_LINK_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a2c59d7d5a1d5eff15976806d237960c1)
- [ETHERNET_LINK_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a55e8d0ee975acc9eabf5096d1b926f6b)
- [ETHERNET_LINK_2500BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5afe48cf59ca4d1db42e768ca272159d55)
- [ETHERNET_LINK_5000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a9ab79aee30b73747fceff86fd3b967f9)
- [ETHERNET_QAV](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42)
- [ETHERNET_PROMISC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d)
- [ETHERNET_PRIORITY_QUEUES](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475)
- [ETHERNET_HW_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe)
- [ETHERNET_LLDP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2)
- [ETHERNET_HW_VLAN_TAG_STRIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5)
- [ETHERNET_DSA_USER_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a12991c85e1a7405bd145b3fff8aeecf1)
- [ETHERNET_DSA_CONDUIT_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a2eeaa2befc2d7a38f0318addef88f072)
- [ETHERNET_QBV](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85)
- [ETHERNET_QBU](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08)
- [ETHERNET_TXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2)
- [ETHERNET_TXINJECTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b)
- [ethernet_if_types](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga139cc696837611a522b289f2ea7bf6fc)
- [L2_ETH_IF_TYPE_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530)
- [L2_ETH_IF_TYPE_WIFI](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671)
- [ethernet_checksum_support](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gabf86b7f09a9d041eea25357cd7a85ede)
- [ETHERNET_CHECKSUM_SUPPORT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea90314c44dca3c123d1a0bd70f108524d)
- [ETHERNET_CHECKSUM_SUPPORT_IPV4_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea6485d2abcd3dae6786022aa286234ed4)
- [ETHERNET_CHECKSUM_SUPPORT_IPV4_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea5671ade139cb0cd28d02e3215337acb9)
- [ETHERNET_CHECKSUM_SUPPORT_IPV6_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea557127c3bc97969fe57fcd8ac55567b5)
- [ETHERNET_CHECKSUM_SUPPORT_IPV6_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edeac64b392a0591cfe7aa5564a476fe20be)
- [ETHERNET_CHECKSUM_SUPPORT_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea3346f0e3d0b350c7fe663cfe389c1e02)
- [ETHERNET_CHECKSUM_SUPPORT_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabf86b7f09a9d041eea25357cd7a85edea03e31130ecef7ac032bceed6f3091af8)
- [ethernet_stats_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gabfab900bfd7a9078e7ac2fd6aed9ce83)
- [ETHERNET_STATS_TYPE_COMMON](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabfab900bfd7a9078e7ac2fd6aed9ce83ad41e45f16877f28b44ec23fadb35d355)
- [ETHERNET_STATS_TYPE_VENDOR](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabfab900bfd7a9078e7ac2fd6aed9ce83a3a094b0237833d4523e04d7b6bb5fbab)
- [ETHERNET_STATS_TYPE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggabfab900bfd7a9078e7ac2fd6aed9ce83a6bb1bfaf79f232101bc91ab02f54e4a7)
- [net_eth_mac_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac2433b0d82ef25373b2c0f994e248e92)
- [NET_ETH_MAC_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a8b1eb5edcd9f4953d56c9c10088d6bb5)
- [NET_ETH_MAC_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a3fad5d3a2578e83da31f3188add46b87)
- [NET_ETH_MAC_NVMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a730e86dd6e257352afb233fdcc189955)
- [NET_ETH_MAC_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ggac2433b0d82ef25373b2c0f994e248e92a9e0096f69300cf30c1f78c33074c1bda)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_eth_is_addr_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga76a5fe39ce12478c666d87f4aec3d579)
- [net_eth_is_addr_all_zeroes](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga237aab2d07ffa84355981d02a4576ebe)
- [net_eth_is_addr_unspecified](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga89964de263029223d119f361fbd94bfd)
- [net_eth_is_addr_multicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga2755ecb84e9759c24302e33a56a1fc84)
- [net_eth_is_addr_unicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gae91a64c96e0a480927d92271092a158d)
- [net_eth_is_addr_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaf20472f9d60e5cddffed2919b3091030)
- [net_eth_is_addr_lldp_multicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaec6fb3c05792bdd30596137686f3251a)
- [net_eth_is_addr_ptp_multicast](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaeddfa5b3ff6e356393114b351f87fe43)
- [net_eth_broadcast_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gae66b24a847f8e0ad119c6c466331afd6)
- [net_eth_ipv4_mcast_to_mac_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga26984472437a98b00c31156f75558134)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_eth_ipv6_mcast_to_mac_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga93e498e99c155fc402a26a4429d044a0)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [net_eth_mcast_addr_add](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga3e578035be797bbbafafa56dedaa8320)
- [net_eth_mcast_addr_rm](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga3cd2e9abc38bdd7eb0cb3932d96fd90e)
- [net_eth_get_hw_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gab0a3b4584bb6ce1d27b98b063fd3fcbd)
- [net_eth_get_hw_config](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga1246be489eb7130100bbaebbb73961c5)
- [net_eth_vlan_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_eth_vlan_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gab71a741cea5f645f4354a1abc9c95a50)
- [net_eth_get_vlan_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga6184c43a62e4af9958412f99991358c9)
- [net_eth_get_vlan_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gad9d890dcf7f5ee3659bf3bd5949faa4e)
- [net_eth_get_vlan_main](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga010a95a0239a800131ac3d43dd54737f)
- [net_eth_is_vlan_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac536aa7154c4a8d194ec67efb68e275c)
- [net_eth_get_vlan_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga78aad58ec66710034cab8891ad638a2c)
- [net_eth_is_vlan_interface](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga8ca1eccc88a351241298d358ec28fdf5)
- [net_eth_mac_load](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa0ef2f94fd18da9c5ea675b46faac8d0)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_eth_carrier_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa7f447129b5b8392640f849d18e9246b)
- [net_eth_carrier_on](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga62b33344256bbe228689e2cb541a0874)
- [net_eth_carrier_off](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga97ef5a8ad9157e2db12e9caf6faef5e7)
- [net_eth_promisc_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga42a3c6b04ef8827e3443c5aebe5541b9)
- [net_eth_txinjection_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gafbb76d53f9f80628d18d39368a28f984)
- [net_eth_mac_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga920bddac077675d544a21fb5650c945e)
- [device](../device_reference/P002_设备对象结构.md)
- [net_eth_get_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga7225d06fbaa12d4668fa165d9e8f0845)
- [net_eth_get_ptp_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga37ff48434c56bbb24422dd805449b6f3)
- [net_eth_get_ptp_clock_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga84c37db5687c5264bec99976a1108ab6)
- [net_eth_type_is_wifi](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga6e603f6f74e6d7e988e7119a6df2ab4d)
- [net_eth_type_is_ethernet](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gae617887d42a288697f2507c5b0907909)
- [net_eth_set_if_type_wifi](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa64462598843dd9f6e731198498aea31)

<a id="header-details"></a>

---

[上一章](P007_zephyr__dt-bindings__sensor__tmag5273.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__bluetooth__hci.h_文件参考.md)
