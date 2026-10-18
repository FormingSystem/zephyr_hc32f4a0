---
id: learning.zephyr-docs.networking.page-110
title: VLAN虚拟局域网
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/vlan.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第110章\_VLAN虚拟局域网

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/vlan.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

[虚拟局域网（Virtual LAN，VLAN）](https://wikipedia.org/wiki/Virtual_LAN)是在数据链路层（Data Link Layer，即 OSI 第 2 层）划分并隔离的计算机网络。对于以太网，这指的是 [IEEE 802.1Q](https://en.wikipedia.org/wiki/IEEE_802.1Q)。

在 Zephyr 中，每个独立 VLAN 都建模为一个虚拟网络接口（Virtual Network Interface）。系统中有一个对应真实物理以太网端口的以太网接口；每个 VLAN 各创建一个虚拟接口，再连接到这个真实接口。这与 Linux 的 VLAN 实现类似：`eth0` 是真实接口，`vlan0` 是运行在 `eth0` 之上的虚拟接口。

## 2. 启用和配置（Enabling and Configuring）

必须在编译时设置 [`CONFIG_NET_VLAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN) 来启用 VLAN，并通过 [`CONFIG_NET_VLAN_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN_COUNT) 配置系统中接口的数量。原文举例：如果有一个不支持 VLAN 的网络接口，以及两个支持 VLAN 的网络接口，应把 [`CONFIG_NET_VLAN_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN_COUNT) 设为 `3`。

> 译注——官方说明与源码差异：以上保留原页面的计数示例。读取当日的官方 [`subsys/net/l2/ethernet/Kconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig) 把 `NET_VLAN_COUNT` 定义为支持的最大 VLAN 标签数量；值为 `0` 时只支持优先级标签 `0`，不创建 VLAN 虚拟接口。官方 [VLAN 示例配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/vlan/prj.conf) 在一个物理接口上配置两个 VLAN 时使用 `CONFIG_NET_VLAN_COUNT=2`，而 IPv4／IPv6 接口总容量为 `3`。应区分 VLAN 虚拟接口容量与包含物理接口在内的总数；分配实现见 [`vlan.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/vlan.c)。

即使在 `prj.conf` 中启用了 VLAN，应用仍需在运行时激活它。VLAN API 提供 [`net_eth_vlan_enable()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)，应用需要传入网络接口和所需的 VLAN 标签。调用 [`net_eth_vlan_disable()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gab71a741cea5f645f4354a1abc9c95a50) 可以禁用指定接口的 VLAN 标记功能。应用还需要自行配置 VLAN 网络接口，例如设置 IP 地址。

API 用法示例见[VLAN 示例应用](P112_VLAN示例.md#vlan)，其源码位于 [`samples/net/ethernet/vlan`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/vlan)。

网络命令行模块（net-shell）提供 `net vlan add` 和 `net vlan del`，可以为指定接口启用或禁用 VLAN 标签。

以太网 VLAN 的进一步规范说明见 [IEEE 802.1Q 规范](https://ieeexplore.ieee.org/document/6991462/)。

## 3. API 参考（API Reference）

[虚拟局域网定义与辅助函数（Virtual LAN Definitions and Helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html)。

相关代码示例：[虚拟局域网（Virtual LAN）](P112_VLAN示例.md#vlan)，建立两个虚拟局域网，并使用 net-shell 查看网络设置。


<a id="virtual-lan-vlan-support"></a>
<a id="vlan-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="overview"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：链路层地址处理](P109_链路层地址处理.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：混杂模式](P114_混杂模式.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P109_链路层地址处理.md) · [返回大纲](大纲.md) · [下一章](P111_以太网示例目录.md)

</details>

<!-- reading-navigation:end -->
