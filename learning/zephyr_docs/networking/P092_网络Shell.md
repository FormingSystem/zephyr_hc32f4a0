---
id: learning.zephyr-docs.networking.page-92
title: 网络Shell
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/net_shell.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第92章\_网络Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/net_shell.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 92.1\_概述

网络命令行（Network Shell）及其配套Shell提供辅助功能，用于查看网络状态、启用或禁用功能，以及执行ping、域名系统解析（Domain Name System，DNS Resolution）等命令。`net-shell`会占用额外内存，因此原文建议通常不要在生产代码中使用。Shell的详细说明见[通用Shell](https://docs.zephyrproject.org/latest/services/shell/index.html#shell-api)。

默认情况下，用户可以看到已启用和未启用的net-shell命令，以便发现可用命令及启用方式。禁用[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)可以关闭这部分额外帮助。

> 译注：命令出现在帮助列表中，不表示所需协议和功能已经编译进当前固件。下面的配置条件用于区分“可发现”与“可执行”。

## 92.2\_网络Shell命令

以下为官方页面列出的全部net-shell命令。

| 命令（Command） | 说明与可用条件（Description） |
| --- | --- |
| `net allocs` | 输出网络内存分配（Memory Allocation）信息。仅在设置[`CONFIG_NET_DEBUG_NET_PKT_ALLOC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DEBUG_NET_PKT_ALLOC)时可用。 |
| `net arp` | 输出IPv4地址解析协议缓存（Address Resolution Protocol Cache，ARP Cache）信息。在已启用IPv4的网络中设置[`CONFIG_NET_ARP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ARP)后可用。 |
| `net bridge` | 输出以太网桥（Ethernet Bridge）信息并操作网桥。仅在设置[`CONFIG_NET_ETHERNET_BRIDGE_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ETHERNET_BRIDGE_SHELL)时可用。 |
| `net capture` | 监测网络流量（Network Traffic），详见[监测网络流量](P017_监视网络流量.md#network-monitoring)。 |
| `net cm` | 连接管理器（Connection Manager）Shell。仅在设置[`CONFIG_NET_CONNECTION_MANAGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONNECTION_MANAGER)时可用。 |
| `net conn` | 输出网络连接（Network Connection）信息。 |
| `net dhcpv4` | 启用或禁用DHCPv4客户端、服务器支持。设置[`CONFIG_NET_DHCPV4_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4_SERVER)或[`CONFIG_NET_DHCPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4)后可用。 |
| `net dhcpv6` | 启用或禁用DHCPv6客户端支持。仅在设置[`CONFIG_NET_DHCPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV6)时可用。 |
| `net dns` | 显示DNS配置，也可以解析DNS名称。仅在设置[`CONFIG_DNS_RESOLVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_RESOLVER)时可用。 |
| `net events` | 启用网络事件监测（Network Event Monitoring）。仅在设置[`CONFIG_NET_MGMT_EVENT_MONITOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT_MONITOR)时可用。 |
| `net filter` | 查看网络数据包过滤规则（Packet Filter Rules）。仅在设置[`CONFIG_NET_PKT_FILTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_FILTER)时可用。 |
| `net ftp` | 连接FTP服务器以传输文件。仅在设置[`CONFIG_FTP_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FTP_CLIENT)时可用。 |
| `net gptp` | 输出广义精确时间协议（Generalized Precision Time Protocol，gPTP）支持信息。仅在设置[`CONFIG_NET_GPTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP)时可用。 |
| `net http` | 显示HTTP服务器信息，或发送HTTP GET／POST／PUT／DELETE请求。设置[`CONFIG_HTTP_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER)或[`CONFIG_HTTP_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_CLIENT)后可用。 |
| `net iface` | 输出网络接口（Network Interface）信息。 |
| `net ipv4` | 输出IPv4专用信息和配置。仅在设置[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)时可用。 |
| `net ipv6` | 输出IPv6专用信息和配置。仅在设置[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)时可用。 |
| `net mem` | 输出网络内存使用信息。设置[`CONFIG_NET_BUF_POOL_USAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF_POOL_USAGE)后会输出更多信息。 |
| `net nbr` | 输出邻居（Neighbor）信息。仅在设置[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)时可用。 |
| `net ping` | 对网络主机执行ping。 |
| `net pkt` | 输出底层网络数据包信息，用于调试。 |
| `net pmtu` | 输出路径最大传输单元发现（Path MTU Discovery）信息。设置[`CONFIG_NET_IPV6_PMTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_PMTU)或[`CONFIG_NET_IPV4_PMTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_PMTU)后可用。 |
| `net ppp` | 输出点对点协议（Point-to-Point Protocol，PPP）信息。设置[`CONFIG_NET_L2_PPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PPP)和[`CONFIG_NET_PPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PPP)后可用。 |
| `net ptp` | 输出精确时间协议（Precision Time Protocol，PTP）支持信息；`net ptp <port>`显示指定端口的详细视图。仅在设置[`CONFIG_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP)时可用。 |
| `net qbv` | 显示和配置IEEE 802.1Qbv时间感知整形器（Time-Aware Shaper，TAS）信息。仅在设置[`CONFIG_NET_QBV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QBV)时可用。 |
| `net quic` | 显示和配置QUIC传输。仅在设置[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)时可用。 |
| `net resume` | 已启用网络电源管理（Network Power Management）时，恢复网络接口。 |
| `net route` | 显示IPv6或IPv4网络路由（Network Route）。设置[`CONFIG_NET_IPV6_ROUTING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_ROUTING)或[`CONFIG_NET_IPV4_ROUTING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_ROUTING)后可用。 |
| `net sockets` | 显示网络套接字（Socket）信息和统计。设置[`CONFIG_NET_SOCKETS_OBJ_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OBJ_CORE)和[`CONFIG_OBJ_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OBJ_CORE)后可用。 |
| `net ssh` | SSH客户端支持。仅在设置[`CONFIG_SSH_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CLIENT)时可用。 |
| `net sshd` | SSH服务器支持。仅在设置[`CONFIG_SSH_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_SERVER)时可用。 |
| `net ssh_key` | SSH密钥生成、删除、保存和加载。设置[`CONFIG_SSH_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CLIENT)或[`CONFIG_SSH_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_SERVER)后可用。 |
| `net stats` | 显示网络统计（Network Statistics）。 |
| `net suspend` | 已启用网络电源管理时，挂起网络接口。 |
| `net tcp` | 建立TCP连接、发送数据及关闭连接。仅在设置[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)时可用。 |
| `net udp` | 直接从Shell发送UDP数据。仅在设置[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)时可用。 |
| `net virtual` | 显示并操作网络虚拟接口（Virtual Interface）。仅在设置[`CONFIG_NET_L2_VIRTUAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_VIRTUAL)时可用。 |
| `net vlan` | 显示以太网虚拟局域网（Virtual LAN，VLAN）信息。仅在设置[`CONFIG_NET_VLAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN)时可用。 |
| `net websocket` | 输出WebSocket信息。仅在设置[`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)时可用。 |
| `net wg` | 显示WireGuard虚拟专用网络（Virtual Private Network，VPN）信息并建立VPN。仅在设置[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)时可用。 |

## 92.3\_Wi-Fi Shell命令

Wi-Fi Shell提供网络扫描、连接、断开和配置命令。

| 命令 | 说明与可用条件 |
| --- | --- |
| `wifi <cmd>` | 用于Wi-Fi连接、断开、扫描和配置的多种命令；仅在设置[`CONFIG_NET_L2_WIFI_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_SHELL)时可用。 |
| `wifi cred` | 显示、添加和删除Wi-Fi网络凭据（Credentials）；仅在设置[`CONFIG_WIFI_CREDENTIALS_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CREDENTIALS_SHELL)时可用。详见[Wi-Fi凭据库](P164_WiFi凭据库.md#lib-wifi-credentials)。 |

## 92.4\_TLS凭据Shell命令

TLS凭据Shell可在易失性后端（Volatile Backend）或受保护的后端存储（Protected Backend Storage）中列出、添加、删除和读取传输层安全凭据（Transport Layer Security Credentials，TLS Credentials）。下列命令仅在设置[`CONFIG_TLS_CREDENTIALS_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS_SHELL)时可用，详见[TLS凭据Shell](P042_TLS凭据Shell.md#tls-credentials-shell)。

| 命令 | 说明 |
| --- | --- |
| `cred buf` | 将凭据数据放入缓冲区，以便添加。 |
| `cred add` | 添加TLS凭据。 |
| `cred del` | 删除TLS凭据。 |
| `cred get` | 读取TLS凭据内容。 |
| `cred list` | 列出已存储的TLS凭据。 |


<a id="network-shell"></a>
<a id="net-shell"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：SOCKS5代理支持](P079_SOCKS5代理支持.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：网络统计](P093_网络统计.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P091_TFTP错误参数.md) · [返回大纲](大纲.md) · [下一章](P093_网络统计.md)

</details>

<!-- reading-navigation:end -->
