---
id: learning.zephyr-docs.networking.page-36
title: DHCPv6前缀委派示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/dhcpv6_pd/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_DHCPv6前缀委派示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/dhcpv6_pd/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 36.1\_概览（Overview）

本示例演示 [RFC 8415](https://datatracker.ietf.org/doc/html/rfc8415.html) 的 IPv6 前缀委派（Prefix Delegation），可以构建为两种角色。官方源码见 [`samples/net/dhcpv6_pd`](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/dhcpv6_pd)。

- **请求路由器（Requesting Router，默认）**：DHCPv6 客户端在上游广域网（WAN）接口申请 IPv6 地址（IA_NA）与委派前缀（IA_PD）。每个下游局域网（LAN）接口从前缀中取得独立 `/64`，通过路由器通告（RA）发布，使下游主机通过 SLAAC 自动配置地址。
- **委派路由器／服务器（Delegating Router / Server）**：使用 `overlay-server.conf`，从 `2001:db8:abcd::/64` 地址池分配地址，从 `2001:db8:beef::/48` 前缀池为每个客户端分配一个 `/56`。

两个池故意互不重叠。如果把客户端 WAN 地址所属子网也委派给它，它就会把同一子网重新发布到 LAN，使两个不同链路具有相同前缀。

## 36.2\_网络接口（Network Interfaces）

前缀委派至少需要两个链路，因此请求路由器构建启用两个接口。对 `native_sim` 而言，它们是两个 TAP 接口：

- `zeth0`：上游 WAN，运行 DHCPv6 客户端，示例接口索引为 `1`。
- `zeth1`：下游 LAN，发布委派前缀，示例接口索引为 `2`。

下游链路数量受 [`CONFIG_NET_DHCPV6_MAX_DOWNSTREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV6_MAX_DOWNSTREAM) 限制。要向更多链路委派，还需相应增加 [`CONFIG_NET_IF_MAX_IPV6_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IF_MAX_IPV6_COUNT)，以及示例 `boards/native_sim.overlay` 中 `zephyr,native-tap` 接口的数量。

服务器构建使用单一接口 `zeth`。`overlay-server.overlay` 禁用下游接口，并重命名保留的接口，使此构建附加到 `zeth` 而不是 `zeth0`。

运行前，先使用 [net-tools](https://github.com/zephyrproject-rtos/net-tools) 的 `net-setup.sh` 创建主机侧 TAP 连接，例如一个实例作为服务器、另一个实例作为请求路由器。详细设置见该工具项目的 `README-dhcpv6-pd.md`。

> 译注：本节的 overlay 是官方示例自带文件，路径均相对于 `samples/net/dhcpv6_pd`；[`net-tools`](https://github.com/zephyrproject-rtos/net-tools) 是官方外部工具项目。接口名与接口索引属于运行配置，不绑定仓库的磁盘位置。

## 36.3\_构建与运行（Building and Running）

在具备 `native_sim` 构建环境的 Linux 主机终端，从 Zephyr 源码根目录执行。请求路由器／客户端：

```sh
west build -b native_sim samples/net/dhcpv6_pd
west build -t run
```

委派路由器／服务器：

```sh
west build -b native_sim samples/net/dhcpv6_pd -- \
    -DEXTRA_CONF_FILE=overlay-server.conf \
    -DEXTRA_DTC_OVERLAY_FILE=overlay-server.overlay
west build -t run
```

> 译注：两组原命令都默认使用 `build`。若要同时保留两个角色，分别给各角色的构建和运行命令设置不同的 `-d` 构建目录，避免共用同一配置缓存。先完成主机接口连接再启动应用；本轮未实际创建 TAP 或启动这两个实例。

## 36.4\_配置要求与参考

请求路由器下游发送 RA 需要 [`CONFIG_NET_IPV6_ND_RA_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_ND_RA_TX)；WAN 与 LAN 之间转发流量需要 [`CONFIG_NET_IPV6_FORWARDING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_FORWARDING)。

详细接口见[DHCPv6 API](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html)与[DHCPv6 服务器 API](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html)。


<a id="dhcpv6-pd"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="network-interfaces"></a>
<a id="building-and-running"></a>
<a id="requirements"></a>
<a id="see-also"></a>

[上一章](P035_DHCPv4客户端示例.md) · [返回大纲](大纲.md) · [下一章](P037_DNS解析示例.md)
