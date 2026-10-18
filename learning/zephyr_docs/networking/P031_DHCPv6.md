---
id: learning.zephyr-docs.networking.page-31
title: DHCPv6
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/dhcpv6.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_DHCPv6

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/dhcpv6.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 31.1\_概览（Overview）

IPv6 动态主机配置协议（DHCPv6）用于管理 IPv6 网络。服务器为设备动态分配 IPv6 地址及其他网络参数，使设备能够与其他 IP 网络通信。进一步概述见原文引用的[DHCPv6 百科条目](https://en.wikipedia.org/wiki/DHCPv6)。

Zephyr 同时支持 DHCPv6 客户端与服务器，包括 [RFC 8415](https://www.rfc-editor.org/rfc/rfc8415) 规定的 IPv6 前缀委派（Prefix Delegation，IA_PD）。

## 31.2\_前缀委派（Prefix Delegation）

客户端可以充当请求路由器（Requesting Router）：除了请求非临时地址（Non-temporary Address，IA_NA），还可设置 [`net_dhcpv6_params.request_prefix`](https://docs.zephyrproject.org/latest/doxygen/html/structnet__dhcpv6__params.html#afd290d92fcc5ae3bac9a9c7030910e6b) 请求委派前缀。获得的前缀安装到发起请求的接口上。

如果节点还要把该前缀进一步分配给一个或多个下游链路，应在 [`net_dhcpv6_params.downstream_ifaces`](https://docs.zephyrproject.org/latest/doxygen/html/structnet__dhcpv6__params.html#ad66949eb34540dbe8808dc9aea9e6368) 数组中列出下游局域网（LAN）接口索引，并用 [`net_dhcpv6_params.downstream_count`](https://docs.zephyrproject.org/latest/doxygen/html/structnet__dhcpv6__params.html#a2549234454437b4316f863347236ef6c) 指定条目数。

每个下游接口从委派前缀中获得不同的 `/64`，第 N 个接口取得第 N 个 `/64`。随后通过该接口的路由器通告（Router Advertisement，RA）发布，使下游主机使用无状态地址自动配置（Stateless Address Autoconfiguration，SLAAC）生成地址。

数组最多容纳 [`CONFIG_NET_DHCPV6_MAX_DOWNSTREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV6_MAX_DOWNSTREAM) 个条目。若 [`net_dhcpv6_params.downstream_count`](https://docs.zephyrproject.org/latest/doxygen/html/structnet__dhcpv6__params.html#a2549234454437b4316f863347236ef6c) 为 `0`，只在请求接口上安装前缀，不向下游分配。下游通告要求启用 [`CONFIG_NET_IPV6_ND_RA_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_ND_RA_TX)，即 RA 发送／路由器角色；若还要在上下游之间转发流量，则需 [`CONFIG_NET_IPV6_FORWARDING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_FORWARDING)。

委派前缀必须足够短，才能为每个下游接口提供不同的 `/64`。长度为 L 的前缀最多支持 `2^(64 - L)` 个下游链路。因此 `/64` 只能分配给一个链路，长于 `/64` 则完全不能这样分配。无法取得独立 `/64` 的下游接口会被跳过，并产生警告。

启用 [`CONFIG_NET_DHCPV6_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV6_SERVER) 的服务器实现委派路由器（Delegating Router）角色，从配置的池中分配地址与委派前缀。两种角色的完整例子见[DHCPv6 前缀委派示例](P036_DHCPv6前缀委派示例.md#dhcpv6-pd)。

## 31.3\_实现限制（Limitations）

原文列出针对 RFC 8415 与 RFC 4861 的以下简化：

- 设置 [`CONFIG_NET_DHCPV6_SEND_RELEASE_ON_STOP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV6_SEND_RELEASE_ON_STOP) 后，客户端停止时发送的 Release 是尽力而为（Best Effort）的：只发送一次，不按[RFC 8415 第 18.2.7 节](https://datatracker.ietf.org/doc/html/rfc8415.html#section-18.2.7)重传 `REL_MAX_RC` 次。未释放的租约（Lease）在到期后由服务器收回。
- 非请求触发的 RA 使用 [`CONFIG_NET_IPV6_ND_RA_TX_INTERVAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_ND_RA_TX_INTERVAL) 指定的固定间隔，不在 `MinRtrAdvInterval` 与 `MaxRtrAdvInterval` 间随机选择；接口成为路由器时，也不发送初始的 `MAX_INITIAL_RTR_ADVERTISEMENTS` 通告突发。应请求发送的 RA 则按[RFC 4861 第 6.2.6 节](https://datatracker.ietf.org/doc/html/rfc4861.html#section-6.2.6)限速并随机延迟。
- 服务器通过改变池基地址中的单个字节分配地址与前缀，因此池容量受 [`CONFIG_NET_DHCPV6_SERVER_MAX_LEASES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV6_SERVER_MAX_LEASES) 限制，IA_PD 池的前缀长度必须按字节对齐。

## 31.4\_API 参考与相关示例

接口分别见[DHCPv6 API](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html)与[DHCPv6 服务器 API](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html)。[前缀委派示例](P036_DHCPv6前缀委派示例.md#dhcpv6-pd)演示按 RFC 8415 获取并委派 IPv6 前缀。


<a id="dhcpv6"></a>
<a id="dhcpv6-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="overview"></a>
<a id="prefix-delegation"></a>
<a id="limitations"></a>
<a id="index-0"></a>
<a id="index-1"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：DHCPv4](P030_DHCPv4.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：DNS解析](P032_DNS解析.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P030_DHCPv4.md) · [返回大纲](大纲.md) · [下一章](P032_DNS解析.md)

</details>

<!-- reading-navigation:end -->
