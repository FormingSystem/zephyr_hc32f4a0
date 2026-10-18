---
id: learning.zephyr-docs.networking.page-140
title: PPP点对点协议
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/ppp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第140章\_PPP点对点协议

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/ppp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

[点对点协议（Point-to-Point Protocol，PPP）](https://en.wikipedia.org/wiki/Point-to-Point_Protocol)是一种数据链路层，即第二层（Layer 2）的通信协议，用于在两个节点之间建立直接连接。PPP 用于多种串行链路，因为 IP 包无法在没有数据链路协议的情况下，独立通过调制解调器线路传输。

在 Zephyr 中，每条 PPP 链路都建模为一个网络接口，这与 Linux 的 PPP 实现方式相似。

必须在编译时设置 [`CONFIG_NET_L2_PPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PPP) 来启用 PPP 支持。原文说明该实现只支持以下协议：

- 链路控制协议（Link Control Protocol，LCP），[RFC 1661](https://datatracker.ietf.org/doc/html/rfc1661.html)。
- 高级数据链路控制（High-level Data Link Control，HDLC），[RFC 1662](https://datatracker.ietf.org/doc/html/rfc1662.html)。
- IP 控制协议（IP Control Protocol，IPCP），[RFC 1332](https://datatracker.ietf.org/doc/html/rfc1332.html)。
- IPv6 控制协议（IPv6 Control Protocol，IPV6CP），[RFC 5072](https://datatracker.ietf.org/doc/html/rfc5072.html)。

> 译注——当前源码差异：上述列表按原页面保留。读取当日的官方 [PPP Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig) 还提供 [`CONFIG_NET_L2_PPP_PAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PPP_PAP)，用于启用密码认证协议（Password Authentication Protocol，PAP）。因此不能把原页面的“只支持”列表视为当前全部可选功能的完整清单。

如需通过蜂窝调制解调器使用 PPP，更多信息见[蜂窝调制解调器示例（Cellular Modem）](P214_蜂窝调制解调器示例.md#cellular-modem)。

## 2. 测试（Testing）

如何让 Zephyr PPP 与 Linux 上运行的 `pppd` 对接测试，详见 [net-tools 的 README](https://github.com/zephyrproject-rtos/net-tools/blob/master/README.md#ppp-connectivity)。


<a id="point-to-point-protocol-ppp-support"></a>
<a id="ppp"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="index-1"></a>
<a id="index-2"></a>
<a id="index-3"></a>
<a id="testing"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：数据报分组层路径MTU发现](P139_数据报分组层路径MTU发现.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：RTP实时传输协议](P141_RTP实时传输协议.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P139_数据报分组层路径MTU发现.md) · [返回大纲](大纲.md) · [下一章](P141_RTP实时传输协议.md)

</details>

<!-- reading-navigation:end -->
