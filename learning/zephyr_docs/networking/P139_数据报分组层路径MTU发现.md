---
id: learning.zephyr-docs.networking.page-139
title: 数据报分组层路径MTU发现
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/dplpmtud.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第139章\_数据报分组层路径MTU发现

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/dplpmtud.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

Zephyr 基于 [RFC 8899](https://datatracker.ietf.org/doc/html/rfc8899.html) 提供通用的数据报分组层路径最大传输单元发现（Datagram Packetization Layer Path MTU Discovery，DPLPMTUD）实现。它面向 QUIC、基于 UDP 的 CoAP 和自定义协议等 UDP 传输，用于确定数据报载荷可以有多大，而不依赖本地 IP 分片（IP Fragmentation）。

子系统分工如下。

### 1.1 通用协议栈（Generic Stack）

实现位于 `subsys/net/ip/dplpmtud.c`，负责：

- 为每个目的地维护搜索状态：已验证的分组层路径 MTU（PLPMTU）、探测大小、重试次数和上下界。
- 在基础 PLPMTU，即 `1200` 字节，与路径上限之间进行二分搜索（Binary Search）。
- 与已有的路径 MTU（PMTU）目的地缓存集成：接收 ICMP“包过大”（Packet Too Big，PTB）信息，并输出经过验证的大小。
- 当 PMTU 缓存报告低于基础 PLPMTU 的 MTU 时，处理路径黑洞（Black Hole）。

### 1.2 使用该接口的传输协议（Transport Consumer）

传输协议负责：

- 按 [`net_dplpmtud_get_path_probe_size()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gaa36c73f87f48f1ce43d1ab96aa7328e5) 返回的大小构造探测数据报。
- 发送探测时启用禁止分片（Don't Fragment）；参见[IPv4／IPv6 套接字选项](P040_BSD套接字.md#ip-socket-options)以及 [`ZSOCK_IP_DONTFRAG`](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv4__socket__options.html#ga3c8f7f8895a3daae11dcd439eb2499a3)、[`ZSOCK_IPV6_DONTFRAG`](https://docs.zephyrproject.org/latest/doxygen/html/group__ipv6__socket__options.html#ga44b16e54bc2922153e9a07d628cf1cba)。
- 把传输层确认（ACK）或丢失结果映射到 [`net_dplpmtud_on_path_probe_acked()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga4be5d1abe82e1bf2591d1804eacb401e)、[`net_dplpmtud_on_path_probe_lost()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga8cb73dde5eff26e8fc6e8af967e7877f)。

[QUIC](P143_QUIC传输接口.md#quic-dplpmtud) 是 Zephyr 源码树内第一个使用者。其他传输协议可使用同一 API，无需重复实现 RFC 8899 状态机。

## 2. 配置（Configuration）

分别按地址族启用 DPLPMTUD：

| 地址族 | 配置项 |
| --- | --- |
| IPv4 | [`CONFIG_NET_IPV4_PMTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_PMTU) 和 [`CONFIG_NET_IPV4_PMTU_DPLPMTUD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_PMTU_DPLPMTUD) |
| IPv6 | [`CONFIG_NET_IPV6_PMTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_PMTU) 和 [`CONFIG_NET_IPV6_PMTU_DPLPMTUD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_PMTU_DPLPMTUD) |

两个地址族都需要 [`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)。启用任意一个地址族的选项时，公共选项 [`CONFIG_NET_PMTU_DPLPMTUD`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig) 会被选中。

通过 [`CONFIG_NET_IPV4_PMTU_PTB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_PMTU_PTB) 和 [`CONFIG_NET_IPV6_PMTU_PTB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_PMTU_PTB)，仍可以使用基于 ICMP“包过大”消息的 PMTU 缩减。DPLPMTUD 通过在路径允许时主动探测更大的数据报，补充 PTB 机制。

可同时跟踪的路径数量分别对应 [`CONFIG_NET_IPV4_PMTU_DESTINATION_CACHE_ENTRIES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_PMTU_DESTINATION_CACHE_ENTRIES) 和 [`CONFIG_NET_IPV6_PMTU_DESTINATION_CACHE_ENTRIES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_PMTU_DESTINATION_CACHE_ENTRIES)。

## 3. 使用模型（Usage Model）

为每个远程目的地初始化一个 [`net_dplpmtud_path`](https://docs.zephyrproject.org/latest/doxygen/html/structnet__dplpmtud__path.html)，也可以在连接整个生命周期内复用该句柄：

```c
struct net_dplpmtud_path path;
uint16_t max_plpmtu = 1452U; /* transport / peer limit, or 0 if uncapped */
int mtu;
int probe;
int ret;

ret = net_dplpmtud_init_path(&path, &remote_addr, max_plpmtu);
if (ret < 0) {
    /* handle error */
}

mtu = net_dplpmtud_get_path_mtu(&path);
if (mtu < 0) {
    mtu = NET_DPLPMTUD_BASE_PLPMTU;
}

/* Application data must fit in @a mtu bytes (transport framing excluded). */
```

> 译注——代码注释对照：`1452U` 是传输协议或对端给出的上限，`0` 表示不额外限制；初始化失败的位置需要调用者实现错误处理。原末尾注释要求应用数据适配 `mtu` 字节，并提到传输封装。当前官方 [`dplpmtud.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/dplpmtud.c) 明确把 PLPMTU 作为 UDP 载荷大小，在 PMTU 缓存边界加减 IP 和 UDP 头。因此 QUIC、CoAP 等位于 UDP 载荷内的协议头仍会占用这个上限，应用正文还需为它们预留空间，不能把 `mtu` 全部用作纯应用数据后再额外添加封装。

探测生命周期（Probe Lifecycle）如下：

1. 调用 [`net_dplpmtud_get_path_probe_size()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#gaa36c73f87f48f1ce43d1ab96aa7328e5)。返回 `0` 表示不需要探测。路径必须已经初始化，读取接口不会创建缓存条目。
2. 若 [`net_dplpmtud_path_probe_in_flight()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga86037b3a53ee6fc5cb9c9d57a8e3a69c) 为假，构造对应大小的数据报，并设置禁止分片；可使用套接字选项，或 [`zsock_sendmsg()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gad3274fe71d43caf8c4d92fffb589375e) 中的逐数据报控制消息。原文在这一步也使用了“构造并发送”的措辞，实际发送时序见下一步及译注。
3. 先调用 [`net_dplpmtud_on_path_probe_sent()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga5db1cdda7708b3186670a9c176fa1384)，在通用状态机中登记本次探测，再实际发送探测数据报。
4. 发送失败时，调用 [`net_dplpmtud_on_path_probe_lost()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga8cb73dde5eff26e8fc6e8af967e7877f)，使核心与传输协议的状态保持一致。
5. 获得传输确认结果后，调用 [`net_dplpmtud_on_path_probe_acked()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga4be5d1abe82e1bf2591d1804eacb401e) 或 [`net_dplpmtud_on_path_probe_lost()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga8cb73dde5eff26e8fc6e8af967e7877f)。

> 译注——先登记再发送：官方 [`dplpmtud.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/dplpmtud.h) 明确要求在实际发送之前调用 `net_dplpmtud_on_path_probe_sent()`。应先检查探测大小为正，再构造、登记、发送；返回负错误码时不能把它转换为无符号包大小。登记接口也可能失败，需要处理后再决定是否发送，避免状态机与已发报文不一致。

当传输协议获知新上限时，例如 QUIC 的 `max_udp_payload_size` 传输参数，应调用 [`net_dplpmtud_set_path_max_plpmtu()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga7d1720efbd54fe04bdbfae5ffd53f4f1) 更新。

如果传输协议独立于 ICMP 检测到黑洞，应调用 [`net_dplpmtud_note_path_blackhole()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html#ga9ac65913e3237c9b66c1c0ab5a4ced56)。低于基础 PLPMTU 的 PTB 更新会通过 PMTU 缓存自动应用。

## 4. API 参考（API Reference）

[数据报 PLPMTUD API](https://docs.zephyrproject.org/latest/doxygen/html/group__net__dplpmtud.html)。


<a id="datagram-plpmtud-api"></a>
<a id="net-dplpmtud"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="configuration"></a>
<a id="usage-model"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Trickle定时器库](P138_Trickle定时器库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：PPP点对点协议](P140_PPP点对点协议.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P138_Trickle定时器库.md) · [返回大纲](大纲.md) · [下一章](P140_PPP点对点协议.md)

</details>

<!-- reading-navigation:end -->
