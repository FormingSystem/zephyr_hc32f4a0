---
id: learning.zephyr-docs.api-platform-topic-reference.page-68
title: 网络统计库（Network Statistics Library）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_网络统计库（Network Statistics Library）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络统计库（Network statistics library）

<a id="details"></a>

网络统计库（Network Statistics Library）。

自 1.5 版提供（Since 1.5）；接口版本（Version）0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 68.1\_数据结构（Data Structures）

<a id="r_net_5Fstats_5Fbytes"></a>

```c
struct net_stats_bytes
```

相关声明：[net_stats_bytes](../network_core_model_reference/P126_net_stats_bytes_结构体.md)。

发送与接收的字节数（Bytes Sent and Received）。

<a id="r_net_5Fstats_5Fpkts"></a>

```c
struct net_stats_pkts
```

相关声明：[net_stats_pkts](../network_core_model_reference/P142_net_stats_pkts_结构体.md)。

发送与接收的网络数据包数量（Network Packets Sent and Received）。

<a id="r_net_5Fstats_5Fip"></a>

```c
struct net_stats_ip
```

相关声明：[net_stats_ip](../network_core_model_reference/P134_net_stats_ip_结构体.md)。

IP层（IP Layer）统计信息。

<a id="r_net_5Fstats_5Fip_5Ferrors"></a>

```c
struct net_stats_ip_errors
```

相关声明：[net_stats_ip_errors](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md)。

IP层错误（Error）统计信息。

<a id="r_net_5Fstats_5Ficmp"></a>

```c
struct net_stats_icmp
```

相关声明：[net_stats_icmp](../network_core_model_reference/P133_net_stats_icmp_结构体.md)。

互联网控制消息协议（ICMP）统计信息。

<a id="r_net_5Fstats_5Ftcp"></a>

```c
struct net_stats_tcp
```

相关声明：[net_stats_tcp](../network_core_model_reference/P149_net_stats_tcp_结构体.md)。

TCP统计信息（Statistics）。

<a id="r_net_5Fstats_5Fudp"></a>

```c
struct net_stats_udp
```

相关声明：[net_stats_udp](../network_core_model_reference/P151_net_stats_udp_结构体.md)。

UDP统计信息（Statistics）。

<a id="r_net_5Fstats_5Fraw"></a>

```c
struct net_stats_raw
```

相关声明：[net_stats_raw](../network_core_model_reference/P145_net_stats_raw_结构体.md)。

原始数据包套接字（Raw Packet Socket）统计信息。

<a id="r_net_5Fstats_5Fipv6_5Fnd"></a>

```c
struct net_stats_ipv6_nd
```

相关声明：[net_stats_ipv6_nd](../network_core_model_reference/P139_net_stats_ipv6_nd_结构体.md)。

IPv6邻居发现（Neighbor Discovery）统计信息。

<a id="r_net_5Fstats_5Fipv6_5Fpmtu"></a>

```c
struct net_stats_ipv6_pmtu
```

相关声明：[net_stats_ipv6_pmtu](../network_core_model_reference/P140_net_stats_ipv6_pmtu_结构体.md)。

IPv6路径MTU发现（Path MTU Discovery）统计信息。

<a id="r_net_5Fstats_5Fipv4_5Fpmtu"></a>

```c
struct net_stats_ipv4_pmtu
```

相关声明：[net_stats_ipv4_pmtu](../network_core_model_reference/P137_net_stats_ipv4_pmtu_结构体.md)。

IPv4路径MTU发现（Path MTU Discovery）统计信息。

<a id="r_net_5Fstats_5Fipv6_5Fmld"></a>

```c
struct net_stats_ipv6_mld
```

相关声明：[net_stats_ipv6_mld](../network_core_model_reference/P138_net_stats_ipv6_mld_结构体.md)。

IPv6组播监听守护进程（Multicast Listener Daemon）统计信息。

<a id="r_net_5Fstats_5Fipv4_5Figmp"></a>

```c
struct net_stats_ipv4_igmp
```

相关声明：[net_stats_ipv4_igmp](../network_core_model_reference/P136_net_stats_ipv4_igmp_结构体.md)。

IPv4 IGMP守护进程（Daemon）统计信息。

<a id="r_net_5Fstats_5Fdns"></a>

```c
struct net_stats_dns
```

相关声明：[net_stats_dns](../network_core_model_reference/P127_net_stats_dns_结构体.md)。

DNS统计信息（Statistics）。

<a id="r_net_5Fstats_5Ftx_5Ftime"></a>

```c
struct net_stats_tx_time
```

相关声明：[net_stats_tx_time](../network_core_model_reference/P150_net_stats_tx_time_结构体.md)。

用于计算平均发送时间（TX Time）的网络数据包传输时间。

<a id="r_net_5Fstats_5Frx_5Ftime"></a>

```c
struct net_stats_rx_time
```

相关声明：[net_stats_rx_time](../network_core_model_reference/P146_net_stats_rx_time_结构体.md)。

用于计算平均接收时间（RX Time）的网络数据包接收时间。

<a id="r_net_5Fstats_5Ftc"></a>

```c
struct net_stats_tc
```

相关声明：[net_stats_tc](../network_core_model_reference/P148_net_stats_tc_结构体.md)。

流量类别（Traffic Class）统计信息。

<a id="r_net_5Fstats_5Fpm"></a>

```c
struct net_stats_pm
```

相关声明：[net_stats_pm](../network_core_model_reference/P143_net_stats_pm_结构体.md)。

电源管理（Power Management）统计信息。

<a id="r_net_5Fstats_5Fpkt_5Ffilter"></a>

```c
struct net_stats_pkt_filter
```

相关声明：[net_stats_pkt_filter](../network_core_model_reference/P141_net_stats_pkt_filter_结构体.md)。

网络数据包过滤器（Network Packet Filter）统计信息。

<a id="r_net_5Fstats"></a>

```c
struct net_stats
```

相关声明：[net_stats](../network_core_model_reference/P125_net_stats_结构体.md)。

在一个结构中保存全部网络统计信息（Network Statistics）。

<a id="r_net_5Fstats_5Feth_5Ferrors"></a>

```c
struct net_stats_eth_errors
```

相关声明：[net_stats_eth_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md)。

以太网错误（Error）统计信息。

<a id="r_net_5Fstats_5Feth_5Fflow"></a>

```c
struct net_stats_eth_flow
```

相关声明：[net_stats_eth_flow](../network_core_model_reference/P131_net_stats_eth_flow_结构体.md)。

以太网流量控制（Flow Control）统计信息。

<a id="r_net_5Fstats_5Feth_5Fcsum"></a>

```c
struct net_stats_eth_csum
```

相关声明：[net_stats_eth_csum](../network_core_model_reference/P129_net_stats_eth_csum_结构体.md)。

以太网校验和（Checksum）统计信息。

<a id="r_net_5Fstats_5Feth_5Fhw_5Ftimestamp"></a>

```c
struct net_stats_eth_hw_timestamp
```

相关声明：[net_stats_eth_hw_timestamp](../network_core_model_reference/P132_net_stats_eth_hw_timestamp_结构体.md)。

以太网硬件时间戳（Hardware Timestamp）统计信息。

<a id="r_net_5Fstats_5Feth"></a>

```c
struct net_stats_eth
```

相关声明：[net_stats_eth](../network_core_model_reference/P128_net_stats_eth_结构体.md)。

全部以太网（Ethernet）专用统计信息。

<a id="r_net_5Fstats_5Fppp"></a>

```c
struct net_stats_ppp
```

相关声明：[net_stats_ppp](../network_core_model_reference/P144_net_stats_ppp_结构体.md)。

全部点对点协议（PPP）专用统计信息。

<a id="r_net_5Fstats_5Fsta_5Fmgmt"></a>

```c
struct net_stats_sta_mgmt
```

相关声明：[net_stats_sta_mgmt](../network_core_model_reference/P147_net_stats_sta_mgmt_结构体.md)。

全部Wi-Fi管理（Management）统计信息。

<a id="r_net_5Fstats_5Fwifi"></a>

```c
struct net_stats_wifi
```

相关声明：[net_stats_wifi](../network_core_model_reference/P153_net_stats_wifi_结构体.md)。

全部Wi-Fi专用统计信息（Statistics）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 68.2\_宏定义（Macros）

<a id="r_ga2a1dcb35c366878ef5f675d6bc649223"></a>

```c
#define NET_STATS_GET_METRIC_NAME(_name)
```

相关声明：[NET_STATS_GET_METRIC_NAME](#ga2a1dcb35c366878ef5f675d6bc649223)。

<a id="r_gab58d7d437d4fa9836a826ee59e2d081d"></a>

```c
#define NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx)
```

相关声明：[NET_STATS_GET_COLLECTOR_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)。

<a id="r_gab66b3c8d32d2f02add08c332460d5cd6"></a>

```c
#define NET_STATS_GET_VAR(dev_id, sfx, var)
```

相关声明：[NET_STATS_GET_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)。

<a id="r_gabb15df6c3c85b85756ef5d2d51d0afb2"></a>

```c
#define NET_STATS_GET_INSTANCE(dev_id, sfx, _not_used)
```

相关声明：[NET_STATS_GET_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)。

<a id="r_gafc6b5e19cd9407c28cf151820b76a287"></a>

```c
#define NET_STATS_PROMETHEUS_COUNTER_DEFINE(_desc, _labelval, _not_used, _collector, _name, _stat_var_ptr)
```

相关声明：[NET_STATS_PROMETHEUS_COUNTER_DEFINE](#gafc6b5e19cd9407c28cf151820b76a287)。

<a id="r_ga162fa8a0ea4939e5768a0cc64210dd6a"></a>

```c
#define NET_STATS_PROMETHEUS_GAUGE_DEFINE(_desc, _labelval, _not_used, _collector, _name, _stat_var_ptr)
```

相关声明：[NET_STATS_PROMETHEUS_GAUGE_DEFINE](#ga162fa8a0ea4939e5768a0cc64210dd6a)。

<a id="r_gab02b7f2c5c424723aed7a6aedd1181f9"></a>

```c
#define NET_STATS_PROMETHEUS_SUMMARY_DEFINE(_desc, _labelval, _not_used, _collector, _name, _stat_var_ptr)
```

相关声明：[NET_STATS_PROMETHEUS_SUMMARY_DEFINE](#gab02b7f2c5c424723aed7a6aedd1181f9)。

<a id="r_gae82639c2bed1c646cda66b49ae2f6de9"></a>

```c
#define NET_STATS_PROMETHEUS_HISTOGRAM_DEFINE(_desc, _labelval, _not_used, _collector, _name, _stat_var_ptr)
```

相关声明：[NET_STATS_PROMETHEUS_HISTOGRAM_DEFINE](#gae82639c2bed1c646cda66b49ae2f6de9)。

<a id="r_gaef8debd9597dae9e8ec2ef91d6e645cc"></a>

```c
#define NET_STATS_PROMETHEUS_IPV6(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IPV6](#gaef8debd9597dae9e8ec2ef91d6e645cc)。

<a id="r_gafa2e6de020b887512a3cebe75253fb18"></a>

```c
#define NET_STATS_PROMETHEUS_IPV4(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IPV4](#gafa2e6de020b887512a3cebe75253fb18)。

<a id="r_ga96beec38aeb91a9d95b4e1e415c0d229"></a>

```c
#define NET_STATS_PROMETHEUS_ICMP(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_ICMP](#ga96beec38aeb91a9d95b4e1e415c0d229)。

<a id="r_ga2d400caf2103d6718bc2871abba3eddb"></a>

```c
#define NET_STATS_PROMETHEUS_UDP(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_UDP](#ga2d400caf2103d6718bc2871abba3eddb)。

<a id="r_ga1b581725d1a8652a0b40e71ac2e99261"></a>

```c
#define NET_STATS_PROMETHEUS_TCP(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_TCP](#ga1b581725d1a8652a0b40e71ac2e99261)。

<a id="r_ga1cc29c5da3740b2623fd625f9f360c6d"></a>

```c
#define NET_STATS_PROMETHEUS_IPV6_ND(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IPV6_ND](#ga1cc29c5da3740b2623fd625f9f360c6d)。

<a id="r_ga2593a73001deea960ccfb80cf71489d4"></a>

```c
#define NET_STATS_PROMETHEUS_IPV6_PMTU(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IPV6_PMTU](#ga2593a73001deea960ccfb80cf71489d4)。

<a id="r_gaaa0bc9dd9f53da03492d10c399db8eab"></a>

```c
#define NET_STATS_PROMETHEUS_IPV4_PMTU(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IPV4_PMTU](#gaaa0bc9dd9f53da03492d10c399db8eab)。

<a id="r_ga5c4827a519269cc00323dfe57921117b"></a>

```c
#define NET_STATS_PROMETHEUS_MLD(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_MLD](#ga5c4827a519269cc00323dfe57921117b)。

<a id="r_ga8782a593de8ae207e57abfcc9477e256"></a>

```c
#define NET_STATS_PROMETHEUS_IGMP(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IGMP](#ga8782a593de8ae207e57abfcc9477e256)。

<a id="r_gaef54299a895568956cbae9960c7bf844"></a>

```c
#define NET_STATS_PROMETHEUS_DNS(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_DNS](#gaef54299a895568956cbae9960c7bf844)。

<a id="r_gaf0c1ee536e8a816c537b6cf7344353f4"></a>

```c
#define NET_STATS_PROMETHEUS_TX_TIME(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_TX_TIME](#gaf0c1ee536e8a816c537b6cf7344353f4)。

<a id="r_ga2b9c4b3dc4cd1cd2b79801e7a4b58849"></a>

```c
#define NET_STATS_PROMETHEUS_RX_TIME(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_RX_TIME](#ga2b9c4b3dc4cd1cd2b79801e7a4b58849)。

<a id="r_ga3c3413463adef85973626716e19e05d6"></a>

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER_IPV4(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_PKT_FILTER_IPV4](#ga3c3413463adef85973626716e19e05d6)。

<a id="r_ga94763ab89bb97f832f43e4d09d34edd7"></a>

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER_IPV6(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_PKT_FILTER_IPV6](#ga94763ab89bb97f832f43e4d09d34edd7)。

<a id="r_gac53b62a898db85f469eed307b3852247"></a>

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER_LOCAL(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_PKT_FILTER_LOCAL](#gac53b62a898db85f469eed307b3852247)。

<a id="r_ga347ee5863fd3501b5e3f7f04c8457bda"></a>

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_PKT_FILTER](#ga347ee5863fd3501b5e3f7f04c8457bda)。

<a id="r_gac79e6cd416c92f9d26843900a084b375"></a>

```c
#define NET_STATS_PROMETHEUS(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS](#gac79e6cd416c92f9d26843900a084b375)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 68.3\_类型定义（Typedefs）

<a id="r_ga05ec15873e79256c287f21b6b6fcd752"></a>

```c
typedef uint32_t net_stats_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_stats_t](#ga05ec15873e79256c287f21b6b6fcd752)。

网络统计计数器（Network Statistics Counter）。

## 68.4\_详细说明（Detailed Documentation）

<a id="gab58d7d437d4fa9836a826ee59e2d081d"></a>

### `NET_STATS_GET_COLLECTOR_NAME`

```c
#define NET_STATS_GET_COLLECTOR_NAME ( dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
net_stats_##dev_id##_##sfx##_collector
```

<a id="gabb15df6c3c85b85756ef5d2d51d0afb2"></a>

### `NET_STATS_GET_INSTANCE`

```c
#define NET_STATS_GET_INSTANCE ( dev_id, sfx, _not_used )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
STRINGIFY(_##dev_id##_##sfx)
```

<a id="ga2a1dcb35c366878ef5f675d6bc649223"></a>

### `NET_STATS_GET_METRIC_NAME`

```c
#define NET_STATS_GET_METRIC_NAME ( _name)
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
_name
```

<a id="gab66b3c8d32d2f02add08c332460d5cd6"></a>

### `NET_STATS_GET_VAR`

```c
#define NET_STATS_GET_VAR ( dev_id, sfx, var )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
zephyr_net_##dev_id##_##sfx##_##var
```

<a id="gac79e6cd416c92f9d26843900a084b375"></a>

### `NET_STATS_PROMETHEUS`

```c
#define NET_STATS_PROMETHEUS ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "Processing error",                                     \
        NET_STATS_GET_INSTANCE(dev_id, sfx, process_error),     \
        "error_count",                                          \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, processing_error),       \
        &(iface)->stats.processing_error);                      \
IF_ENABLED(CONFIG_NET_STATISTICS_PKT_FILTER,                    \
           (NET_STATS_PROMETHEUS_PKT_FILTER(iface, dev_id, sfx))) \
/* IP layer error statistics */                                 \
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "IP proto error",                                       \
        NET_STATS_GET_INSTANCE(dev_id, sfx, ip_proto_error),    \
        "error_count",                                          \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, ip_errors_protoerr),     \
        &(iface)->stats.ip_errors.protoerr);                    \
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "IP version/header len error",                          \
        NET_STATS_GET_INSTANCE(dev_id, sfx, ip_vhl_error),      \
        "error_count",                                          \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, ip_errors_vhlerr),       \
        &(iface)->stats.ip_errors.vhlerr);                      \
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "IP header len error (high byte)",                      \
        NET_STATS_GET_INSTANCE(dev_id, sfx, ip_hblen_error),    \
        "error_count",                                          \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, ip_errors_hblenerr),     \
        &(iface)->stats.ip_errors.hblenerr);                    \
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "IP header len error (low byte)",                       \
        NET_STATS_GET_INSTANCE(dev_id, sfx, ip_lblen_error),    \
        "error_count",                                          \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, ip_errors_lblenerr),     \
        &(iface)->stats.ip_errors.lblenerr);                    \
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "IP fragment error",                                    \
        NET_STATS_GET_INSTANCE(dev_id, sfx, ip_frag_error),     \
        "error_count",                                          \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, ip_errors_fragerr),      \
        &(iface)->stats.ip_errors.fragerr);                     \
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "IP checksum error",                                    \
        NET_STATS_GET_INSTANCE(dev_id, sfx, ip_chk_error),      \
        "error_count",                                          \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, ip_errors_chkerr),       \
        &(iface)->stats.ip_errors.chkerr);                      \
/* General network statistics */                                \
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "Bytes received",                                       \
        NET_STATS_GET_INSTANCE(dev_id, sfx, bytes_recv),        \
        "byte_count",                                           \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, bytes_recv),             \
        &(iface)->stats.bytes.received);                        \
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "Bytes sent",                                           \
        NET_STATS_GET_INSTANCE(dev_id, sfx, bytes_sent),        \
        "byte_count",                                           \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, bytes_sent),             \
        &(iface)->stats.bytes.sent);                            \
NET_STATS_PROMETHEUS_IPV6(iface, dev_id, sfx);                  \
NET_STATS_PROMETHEUS_IPV4(iface, dev_id, sfx);                  \
NET_STATS_PROMETHEUS_ICMP(iface, dev_id, sfx);                  \
NET_STATS_PROMETHEUS_UDP(iface, dev_id, sfx);                   \
NET_STATS_PROMETHEUS_RAW(iface, dev_id, sfx);                   \
NET_STATS_PROMETHEUS_TCP(iface, dev_id, sfx);                   \
NET_STATS_PROMETHEUS_IPV6_ND(iface, dev_id, sfx);               \
NET_STATS_PROMETHEUS_IPV6_PMTU(iface, dev_id, sfx);             \
NET_STATS_PROMETHEUS_IPV4_PMTU(iface, dev_id, sfx);             \
NET_STATS_PROMETHEUS_MLD(iface, dev_id, sfx);                   \
NET_STATS_PROMETHEUS_IGMP(iface, dev_id, sfx);                  \
NET_STATS_PROMETHEUS_DNS(iface, dev_id, sfx);                   \
NET_STATS_PROMETHEUS_TX_TIME(iface, dev_id, sfx);               \
NET_STATS_PROMETHEUS_RX_TIME(iface, dev_id, sfx)
```

<a id="gafc6b5e19cd9407c28cf151820b76a287"></a>

### `NET_STATS_PROMETHEUS_COUNTER_DEFINE`

```c
#define NET_STATS_PROMETHEUS_COUNTER_DEFINE ( _desc, _labelval, _not_used, _collector, _name, _stat_var_ptr )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
static PROMETHEUS_COUNTER_DEFINE(                                       \
        NET_STATS_GET_METRIC_NAME(_name),                               \
        _desc, ({ .key = "nic", .value = &_labelval[1] }),              \
        &(_collector), _stat_var_ptr)
```

<a id="gaef54299a895568956cbae9960c7bf844"></a>

### `NET_STATS_PROMETHEUS_DNS`

```c
#define NET_STATS_PROMETHEUS_DNS ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="ga162fa8a0ea4939e5768a0cc64210dd6a"></a>

### `NET_STATS_PROMETHEUS_GAUGE_DEFINE`

```c
#define NET_STATS_PROMETHEUS_GAUGE_DEFINE ( _desc, _labelval, _not_used, _collector, _name, _stat_var_ptr )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
static PROMETHEUS_GAUGE_DEFINE(                                         \
        NET_STATS_GET_METRIC_NAME(_name),                               \
        _desc, ({ .key = "nic", .value = &_labelval[1] }),              \
        &(_collector), _stat_var_ptr)
```

<a id="gae82639c2bed1c646cda66b49ae2f6de9"></a>

### `NET_STATS_PROMETHEUS_HISTOGRAM_DEFINE`

```c
#define NET_STATS_PROMETHEUS_HISTOGRAM_DEFINE ( _desc, _labelval, _not_used, _collector, _name, _stat_var_ptr )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
static PROMETHEUS_HISTOGRAM_DEFINE(                                     \
        NET_STATS_GET_METRIC_NAME(_name),                               \
        _desc, ({ .key = "nic", .value = &_labelval[1] }),              \
        &(_collector), _stat_var_ptr)
```

<a id="ga96beec38aeb91a9d95b4e1e415c0d229"></a>

### `NET_STATS_PROMETHEUS_ICMP`

```c
#define NET_STATS_PROMETHEUS_ICMP ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="ga8782a593de8ae207e57abfcc9477e256"></a>

### `NET_STATS_PROMETHEUS_IGMP`

```c
#define NET_STATS_PROMETHEUS_IGMP ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="gafa2e6de020b887512a3cebe75253fb18"></a>

### `NET_STATS_PROMETHEUS_IPV4`

```c
#define NET_STATS_PROMETHEUS_IPV4 ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="gaaa0bc9dd9f53da03492d10c399db8eab"></a>

### `NET_STATS_PROMETHEUS_IPV4_PMTU`

```c
#define NET_STATS_PROMETHEUS_IPV4_PMTU ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="gaef8debd9597dae9e8ec2ef91d6e645cc"></a>

### `NET_STATS_PROMETHEUS_IPV6`

```c
#define NET_STATS_PROMETHEUS_IPV6 ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="ga1cc29c5da3740b2623fd625f9f360c6d"></a>

### `NET_STATS_PROMETHEUS_IPV6_ND`

```c
#define NET_STATS_PROMETHEUS_IPV6_ND ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="ga2593a73001deea960ccfb80cf71489d4"></a>

### `NET_STATS_PROMETHEUS_IPV6_PMTU`

```c
#define NET_STATS_PROMETHEUS_IPV6_PMTU ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="ga5c4827a519269cc00323dfe57921117b"></a>

### `NET_STATS_PROMETHEUS_MLD`

```c
#define NET_STATS_PROMETHEUS_MLD ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="ga347ee5863fd3501b5e3f7f04c8457bda"></a>

### `NET_STATS_PROMETHEUS_PKT_FILTER`

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "Packet filter RX drop",                                \
        NET_STATS_GET_INSTANCE(dev_id, sfx, pkt_filter_rx_drop),\
        "packet_count",                                         \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, pkt_filter_rx_drop),     \
        &(iface)->stats.pkt_filter.rx.drop);                    \
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "Packet filter TX drop",                                \
        NET_STATS_GET_INSTANCE(dev_id, sfx, pkt_filter_tx_drop),\
        "packet_count",                                         \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, pkt_filter_tx_drop),     \
        &(iface)->stats.pkt_filter.tx.drop);                    \
IF_ENABLED(CONFIG_NET_PKT_FILTER_IPV4_HOOK,                     \
           (NET_STATS_PROMETHEUS_PKT_FILTER_IPV4(iface, dev_id, sfx))) \
IF_ENABLED(CONFIG_NET_PKT_FILTER_IPV6_HOOK,                     \
           (NET_STATS_PROMETHEUS_PKT_FILTER_IPV6(iface, dev_id, sfx))) \
IF_ENABLED(CONFIG_NET_PKT_FILTER_LOCAL_IN_HOOK,                 \
           (NET_STATS_PROMETHEUS_PKT_FILTER_LOCAL(iface, dev_id, sfx)))
```

<a id="ga3c3413463adef85973626716e19e05d6"></a>

### `NET_STATS_PROMETHEUS_PKT_FILTER_IPV4`

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER_IPV4 ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "Packet filter RX IPv4 drop",                           \
        NET_STATS_GET_INSTANCE(dev_id, sfx, pkt_filter_rx_ipv4_drop), \
        "packet_count",                                         \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, pkt_filter_rx_ipv4_drop),\
        &(iface)->stats.pkt_filter.rx.ipv4_drop);
```

<a id="ga94763ab89bb97f832f43e4d09d34edd7"></a>

### `NET_STATS_PROMETHEUS_PKT_FILTER_IPV6`

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER_IPV6 ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "Packet filter RX IPv6 drop",                           \
        NET_STATS_GET_INSTANCE(dev_id, sfx, pkt_filter_rx_ipv6_drop), \
        "packet_count",                                         \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, pkt_filter_rx_ipv6_drop),\
        &(iface)->stats.pkt_filter.rx.ipv6_drop);
```

<a id="gac53b62a898db85f469eed307b3852247"></a>

### `NET_STATS_PROMETHEUS_PKT_FILTER_LOCAL`

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER_LOCAL ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
NET_STATS_PROMETHEUS_COUNTER_DEFINE(                            \
        "Packet filter RX local drop",                          \
        NET_STATS_GET_INSTANCE(dev_id, sfx, pkt_filter_rx_local_drop), \
        "packet_count",                                         \
        NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx),              \
        NET_STATS_GET_VAR(dev_id, sfx, pkt_filter_rx_local_drop),\
        &(iface)->stats.pkt_filter.rx.local_drop);
```

<a id="ga2b9c4b3dc4cd1cd2b79801e7a4b58849"></a>

### `NET_STATS_PROMETHEUS_RX_TIME`

```c
#define NET_STATS_PROMETHEUS_RX_TIME ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="gab02b7f2c5c424723aed7a6aedd1181f9"></a>

### `NET_STATS_PROMETHEUS_SUMMARY_DEFINE`

```c
#define NET_STATS_PROMETHEUS_SUMMARY_DEFINE ( _desc, _labelval, _not_used, _collector, _name, _stat_var_ptr )
```

```c
#include <zephyr/net/net_stats.h>
```

展开值（Value）：

```c
static PROMETHEUS_SUMMARY_DEFINE(                                       \
        NET_STATS_GET_METRIC_NAME(_name),                               \
        _desc, ({ .key = "nic", .value = &_labelval[1] }),              \
        &(_collector), _stat_var_ptr)
```

<a id="ga1b581725d1a8652a0b40e71ac2e99261"></a>

### `NET_STATS_PROMETHEUS_TCP`

```c
#define NET_STATS_PROMETHEUS_TCP ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="gaf0c1ee536e8a816c537b6cf7344353f4"></a>

### `NET_STATS_PROMETHEUS_TX_TIME`

```c
#define NET_STATS_PROMETHEUS_TX_TIME ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="ga2d400caf2103d6718bc2871abba3eddb"></a>

### `NET_STATS_PROMETHEUS_UDP`

```c
#define NET_STATS_PROMETHEUS_UDP ( iface, dev_id, sfx )
```

```c
#include <zephyr/net/net_stats.h>
```

<a id="ga05ec15873e79256c287f21b6b6fcd752"></a>

### `net_stats_t`

```c
typedef uint32_t net_stats_t
```

```c
#include <zephyr/net/net_stats.h>
```

网络统计计数器（Network Statistics Counter）。


## 68.5\_原页交叉引用（Cross References）

- [net_stats_bytes](../network_core_model_reference/P126_net_stats_bytes_结构体.md)
- [net_stats_pkts](../network_core_model_reference/P142_net_stats_pkts_结构体.md)
- [net_stats_ip](../network_core_model_reference/P134_net_stats_ip_结构体.md)
- [net_stats_ip_errors](../network_core_model_reference/P135_net_stats_ip_errors_结构体.md)
- [net_stats_icmp](../network_core_model_reference/P133_net_stats_icmp_结构体.md)
- [net_stats_tcp](../network_core_model_reference/P149_net_stats_tcp_结构体.md)
- [net_stats_udp](../network_core_model_reference/P151_net_stats_udp_结构体.md)
- [net_stats_raw](../network_core_model_reference/P145_net_stats_raw_结构体.md)
- [net_stats_ipv6_nd](../network_core_model_reference/P139_net_stats_ipv6_nd_结构体.md)
- [net_stats_ipv6_pmtu](../network_core_model_reference/P140_net_stats_ipv6_pmtu_结构体.md)
- [net_stats_ipv4_pmtu](../network_core_model_reference/P137_net_stats_ipv4_pmtu_结构体.md)
- [net_stats_ipv6_mld](../network_core_model_reference/P138_net_stats_ipv6_mld_结构体.md)
- [net_stats_ipv4_igmp](../network_core_model_reference/P136_net_stats_ipv4_igmp_结构体.md)
- [net_stats_dns](../network_core_model_reference/P127_net_stats_dns_结构体.md)
- [net_stats_tx_time](../network_core_model_reference/P150_net_stats_tx_time_结构体.md)
- [net_stats_rx_time](../network_core_model_reference/P146_net_stats_rx_time_结构体.md)
- [net_stats_tc](../network_core_model_reference/P148_net_stats_tc_结构体.md)
- [net_stats_pm](../network_core_model_reference/P143_net_stats_pm_结构体.md)
- [net_stats_pkt_filter](../network_core_model_reference/P141_net_stats_pkt_filter_结构体.md)
- [net_stats](../network_core_model_reference/P125_net_stats_结构体.md)
- [net_stats_eth_errors](../network_core_model_reference/P130_net_stats_eth_errors_结构体.md)
- [net_stats_eth_flow](../network_core_model_reference/P131_net_stats_eth_flow_结构体.md)
- [net_stats_eth_csum](../network_core_model_reference/P129_net_stats_eth_csum_结构体.md)
- [net_stats_eth_hw_timestamp](../network_core_model_reference/P132_net_stats_eth_hw_timestamp_结构体.md)
- [net_stats_eth](../network_core_model_reference/P128_net_stats_eth_结构体.md)
- [net_stats_ppp](../network_core_model_reference/P144_net_stats_ppp_结构体.md)
- [net_stats_sta_mgmt](../network_core_model_reference/P147_net_stats_sta_mgmt_结构体.md)
- [net_stats_wifi](../network_core_model_reference/P153_net_stats_wifi_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/net/net_stats.h](../api_file_configuration_reference/P059_zephyr__net__net_stats.h_文件参考.md)
- [PROMETHEUS_COUNTER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gadbfcfc7904d6388d2c9dc81d4803264c)
- [PROMETHEUS_GAUGE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga362e708722846a3ca9299e8994becd13)
- [PROMETHEUS_HISTOGRAM_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gaf2ddb4e016104faaf543d9a028756a0c)
- [PROMETHEUS_SUMMARY_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gaa3c043be86118ff9e8122136edc89cc4)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__net__stats_html_ga347ee5863fd3501b5e3f7f04c8457bda"></a>
<a id="agroup__net__stats_html_gab58d7d437d4fa9836a826ee59e2d081d"></a>
<a id="agroup__net__stats_html_gab66b3c8d32d2f02add08c332460d5cd6"></a>
<a id="agroup__net__stats_html_gabb15df6c3c85b85756ef5d2d51d0afb2"></a>
<a id="agroup__net__stats_html_gafc6b5e19cd9407c28cf151820b76a287"></a>
<a id="agroup__net__stats_html_ga2a1dcb35c366878ef5f675d6bc649223"></a>
<a id="agroup__prometheus_html_gadbfcfc7904d6388d2c9dc81d4803264c"></a>
<a id="agroup__prometheus_html_ga362e708722846a3ca9299e8994becd13"></a>
<a id="agroup__prometheus_html_gaf2ddb4e016104faaf543d9a028756a0c"></a>
<a id="agroup__net__stats_html_ga3c3413463adef85973626716e19e05d6"></a>
<a id="agroup__net__stats_html_ga94763ab89bb97f832f43e4d09d34edd7"></a>
<a id="agroup__net__stats_html_gac53b62a898db85f469eed307b3852247"></a>
<a id="agroup__prometheus_html_gaa3c043be86118ff9e8122136edc89cc4"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P067_网络卸载接口（Network Offloading Interface）.md) · [返回大纲](大纲.md) · [下一章](P069_用于通用 MIDI 数据包的用户数据报协议（User Datagram Protocol for Universal MIDI Packets）.md)
