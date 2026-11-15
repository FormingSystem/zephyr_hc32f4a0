---
id: learning.zephyr-docs.api-file-configuration-reference.page-59
title: zephyr__net__net_stats.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_zephyr\_\_net\_\_net\_stats.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络统计信息（Network Statistics）。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/net/net_core.h>
#include <zephyr/net/net_mgmt.h>
#include <zephyr/net/prometheus/collector.h>
#include <zephyr/net/prometheus/counter.h>
#include <zephyr/net/prometheus/metric.h>
#include <zephyr/net/prometheus/gauge.h>
#include <zephyr/net/prometheus/histogram.h>
#include <zephyr/net/prometheus/summary.h>
```

查看此文件的源码。

网络统计（Network Statistics）。网络统计数据会占用内存（Memory），因此仅应在调试（Debugging）时启用。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 59.1\_数据结构（Data Structures）

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

## 59.2\_宏定义（Macros）

<a id="r_ga2a1dcb35c366878ef5f675d6bc649223"></a>

```c
#define NET_STATS_GET_METRIC_NAME(_name)
```

相关声明：[NET_STATS_GET_METRIC_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga2a1dcb35c366878ef5f675d6bc649223)。

<a id="r_gab58d7d437d4fa9836a826ee59e2d081d"></a>

```c
#define NET_STATS_GET_COLLECTOR_NAME(dev_id, sfx)
```

相关声明：[NET_STATS_GET_COLLECTOR_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gab58d7d437d4fa9836a826ee59e2d081d)。

<a id="r_gab66b3c8d32d2f02add08c332460d5cd6"></a>

```c
#define NET_STATS_GET_VAR(dev_id, sfx, var)
```

相关声明：[NET_STATS_GET_VAR](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gab66b3c8d32d2f02add08c332460d5cd6)。

<a id="r_gabb15df6c3c85b85756ef5d2d51d0afb2"></a>

```c
#define NET_STATS_GET_INSTANCE(dev_id, sfx, _not_used)
```

相关声明：[NET_STATS_GET_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gabb15df6c3c85b85756ef5d2d51d0afb2)。

<a id="r_gafc6b5e19cd9407c28cf151820b76a287"></a>

```c
#define NET_STATS_PROMETHEUS_COUNTER_DEFINE(_desc, _labelval, _not_used, _collector, _name, _stat_var_ptr)
```

相关声明：[NET_STATS_PROMETHEUS_COUNTER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gafc6b5e19cd9407c28cf151820b76a287)。

<a id="r_ga162fa8a0ea4939e5768a0cc64210dd6a"></a>

```c
#define NET_STATS_PROMETHEUS_GAUGE_DEFINE(_desc, _labelval, _not_used, _collector, _name, _stat_var_ptr)
```

相关声明：[NET_STATS_PROMETHEUS_GAUGE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga162fa8a0ea4939e5768a0cc64210dd6a)。

<a id="r_gab02b7f2c5c424723aed7a6aedd1181f9"></a>

```c
#define NET_STATS_PROMETHEUS_SUMMARY_DEFINE(_desc, _labelval, _not_used, _collector, _name, _stat_var_ptr)
```

相关声明：[NET_STATS_PROMETHEUS_SUMMARY_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gab02b7f2c5c424723aed7a6aedd1181f9)。

<a id="r_gae82639c2bed1c646cda66b49ae2f6de9"></a>

```c
#define NET_STATS_PROMETHEUS_HISTOGRAM_DEFINE(_desc, _labelval, _not_used, _collector, _name, _stat_var_ptr)
```

相关声明：[NET_STATS_PROMETHEUS_HISTOGRAM_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gae82639c2bed1c646cda66b49ae2f6de9)。

<a id="r_gaef8debd9597dae9e8ec2ef91d6e645cc"></a>

```c
#define NET_STATS_PROMETHEUS_IPV6(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gaef8debd9597dae9e8ec2ef91d6e645cc)。

<a id="r_gafa2e6de020b887512a3cebe75253fb18"></a>

```c
#define NET_STATS_PROMETHEUS_IPV4(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gafa2e6de020b887512a3cebe75253fb18)。

<a id="r_ga96beec38aeb91a9d95b4e1e415c0d229"></a>

```c
#define NET_STATS_PROMETHEUS_ICMP(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga96beec38aeb91a9d95b4e1e415c0d229)。

<a id="r_ga2d400caf2103d6718bc2871abba3eddb"></a>

```c
#define NET_STATS_PROMETHEUS_UDP(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga2d400caf2103d6718bc2871abba3eddb)。

<a id="r_ga1b581725d1a8652a0b40e71ac2e99261"></a>

```c
#define NET_STATS_PROMETHEUS_TCP(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga1b581725d1a8652a0b40e71ac2e99261)。

<a id="r_ga1cc29c5da3740b2623fd625f9f360c6d"></a>

```c
#define NET_STATS_PROMETHEUS_IPV6_ND(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IPV6_ND](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga1cc29c5da3740b2623fd625f9f360c6d)。

<a id="r_ga2593a73001deea960ccfb80cf71489d4"></a>

```c
#define NET_STATS_PROMETHEUS_IPV6_PMTU(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IPV6_PMTU](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga2593a73001deea960ccfb80cf71489d4)。

<a id="r_gaaa0bc9dd9f53da03492d10c399db8eab"></a>

```c
#define NET_STATS_PROMETHEUS_IPV4_PMTU(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IPV4_PMTU](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gaaa0bc9dd9f53da03492d10c399db8eab)。

<a id="r_ga5c4827a519269cc00323dfe57921117b"></a>

```c
#define NET_STATS_PROMETHEUS_MLD(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_MLD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga5c4827a519269cc00323dfe57921117b)。

<a id="r_ga8782a593de8ae207e57abfcc9477e256"></a>

```c
#define NET_STATS_PROMETHEUS_IGMP(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_IGMP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga8782a593de8ae207e57abfcc9477e256)。

<a id="r_gaef54299a895568956cbae9960c7bf844"></a>

```c
#define NET_STATS_PROMETHEUS_DNS(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_DNS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gaef54299a895568956cbae9960c7bf844)。

<a id="r_gaf0c1ee536e8a816c537b6cf7344353f4"></a>

```c
#define NET_STATS_PROMETHEUS_TX_TIME(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_TX_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gaf0c1ee536e8a816c537b6cf7344353f4)。

<a id="r_ga2b9c4b3dc4cd1cd2b79801e7a4b58849"></a>

```c
#define NET_STATS_PROMETHEUS_RX_TIME(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_RX_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga2b9c4b3dc4cd1cd2b79801e7a4b58849)。

<a id="r_ga3c3413463adef85973626716e19e05d6"></a>

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER_IPV4(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_PKT_FILTER_IPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga3c3413463adef85973626716e19e05d6)。

<a id="r_ga94763ab89bb97f832f43e4d09d34edd7"></a>

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER_IPV6(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_PKT_FILTER_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga94763ab89bb97f832f43e4d09d34edd7)。

<a id="r_gac53b62a898db85f469eed307b3852247"></a>

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER_LOCAL(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_PKT_FILTER_LOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gac53b62a898db85f469eed307b3852247)。

<a id="r_ga347ee5863fd3501b5e3f7f04c8457bda"></a>

```c
#define NET_STATS_PROMETHEUS_PKT_FILTER(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS_PKT_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga347ee5863fd3501b5e3f7f04c8457bda)。

<a id="r_gac79e6cd416c92f9d26843900a084b375"></a>

```c
#define NET_STATS_PROMETHEUS(iface, dev_id, sfx)
```

相关声明：[NET_STATS_PROMETHEUS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gac79e6cd416c92f9d26843900a084b375)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 59.3\_类型定义（Typedefs）

<a id="r_ga05ec15873e79256c287f21b6b6fcd752"></a>

```c
typedef uint32_t net_stats_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)。

网络统计计数器（Network Statistics Counter）。


## 59.4\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/net/net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h_source.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h_source.html)
- [zephyr/net/prometheus/collector.h](../api_source_reference/P109_collector.h_源码浏览.md)
- [zephyr/net/prometheus/counter.h](../api_source_reference/P574_counter.h_源码浏览.md)
- [zephyr/net/prometheus/metric.h](../api_source_supplement_reference/P112_metric.h_源码浏览.md)
- [zephyr/net/prometheus/gauge.h](../api_source_reference/P283_gauge.h_源码浏览.md)
- [zephyr/net/prometheus/histogram.h](../api_source_reference/P320_histogram.h_源码浏览.md)
- [zephyr/net/prometheus/summary.h](../api_source_reference/P846_summary.h_源码浏览.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
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
- [NET_STATS_GET_METRIC_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga2a1dcb35c366878ef5f675d6bc649223)
- [NET_STATS_GET_COLLECTOR_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gab58d7d437d4fa9836a826ee59e2d081d)
- [NET_STATS_GET_VAR](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gab66b3c8d32d2f02add08c332460d5cd6)
- [NET_STATS_GET_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gabb15df6c3c85b85756ef5d2d51d0afb2)
- [NET_STATS_PROMETHEUS_COUNTER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gafc6b5e19cd9407c28cf151820b76a287)
- [NET_STATS_PROMETHEUS_GAUGE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga162fa8a0ea4939e5768a0cc64210dd6a)
- [NET_STATS_PROMETHEUS_SUMMARY_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gab02b7f2c5c424723aed7a6aedd1181f9)
- [NET_STATS_PROMETHEUS_HISTOGRAM_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gae82639c2bed1c646cda66b49ae2f6de9)
- [NET_STATS_PROMETHEUS_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gaef8debd9597dae9e8ec2ef91d6e645cc)
- [NET_STATS_PROMETHEUS_IPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gafa2e6de020b887512a3cebe75253fb18)
- [NET_STATS_PROMETHEUS_ICMP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga96beec38aeb91a9d95b4e1e415c0d229)
- [NET_STATS_PROMETHEUS_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga2d400caf2103d6718bc2871abba3eddb)
- [NET_STATS_PROMETHEUS_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga1b581725d1a8652a0b40e71ac2e99261)
- [NET_STATS_PROMETHEUS_IPV6_ND](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga1cc29c5da3740b2623fd625f9f360c6d)
- [NET_STATS_PROMETHEUS_IPV6_PMTU](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga2593a73001deea960ccfb80cf71489d4)
- [NET_STATS_PROMETHEUS_IPV4_PMTU](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gaaa0bc9dd9f53da03492d10c399db8eab)
- [NET_STATS_PROMETHEUS_MLD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga5c4827a519269cc00323dfe57921117b)
- [NET_STATS_PROMETHEUS_IGMP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga8782a593de8ae207e57abfcc9477e256)
- [NET_STATS_PROMETHEUS_DNS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gaef54299a895568956cbae9960c7bf844)
- [NET_STATS_PROMETHEUS_TX_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gaf0c1ee536e8a816c537b6cf7344353f4)
- [NET_STATS_PROMETHEUS_RX_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga2b9c4b3dc4cd1cd2b79801e7a4b58849)
- [NET_STATS_PROMETHEUS_PKT_FILTER_IPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga3c3413463adef85973626716e19e05d6)
- [NET_STATS_PROMETHEUS_PKT_FILTER_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga94763ab89bb97f832f43e4d09d34edd7)
- [NET_STATS_PROMETHEUS_PKT_FILTER_LOCAL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gac53b62a898db85f469eed307b3852247)
- [NET_STATS_PROMETHEUS_PKT_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga347ee5863fd3501b5e3f7f04c8457bda)
- [NET_STATS_PROMETHEUS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#gac79e6cd416c92f9d26843900a084b375)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>

---

[上一章](P058_zephyr__data__navigation.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P060_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza2m.h_文件参考.md)
