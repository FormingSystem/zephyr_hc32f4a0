---
id: learning.zephyr-docs.networking.page-158
title: 网络API目录
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第158章\_网络API目录

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 网络API目录

Zephyr 为应用提供标准 BSD 套接字（BSD Sockets）API，声明位于 [include/zephyr/net/socket.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/socket.h)，详见 [BSD 套接字 API](P040_BSD套接字.md#bsd-sockets-interface)。

除标准接口外，Zephyr 还提供一组自定义网络 API 和库，见下列目录。

> 原文注意：应用不应使用 [include/zephyr/net/net_context.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_context.h) 中的旧式连接 API（Legacy Connectivity API）。

- [网络通用 API（Network APIs）](P159_网络通用API目录.md)
  - [BSD套接字（BSD Sockets）](P040_BSD套接字.md)
  - [套接字服务（Socket Services）](P041_套接字服务.md)
  - [IPv4和IPv6原语与辅助接口（IPv4/IPv6 Primitives and Helpers）](P137_IPv4和IPv6原语与辅助接口.md)
  - [DNS解析（DNS Resolve）](P032_DNS解析.md)
  - [数据报分组层路径MTU发现（Datagram PLPMTUD API）](P139_数据报分组层路径MTU发现.md)
  - [网络管理（Network Management）](P022_网络管理.md)
  - [网络统计（Network Statistics）](P093_网络统计.md)
  - [网络超时（Network Timeout）](P131_网络超时.md)
  - [网络上下文（Networking Context）](P026_网络上下文.md)
  - [混杂模式（Promiscuous Mode）](P114_混杂模式.md)
  - [SNTP时间同步库（Simple Network Time Protocol Library）](P034_SNTP时间同步库.md)
  - [SOCKS5代理支持（SOCKS5 Proxy Support）](P079_SOCKS5代理支持.md)
  - [Trickle定时器库（Trickle Timer Library）](P138_Trickle定时器库.md)
  - [WebSocket客户端（Websocket Client API）](P053_WebSocket客户端.md)
  - [网络分组捕获（Network Packet Capture）](P029_网络分组捕获.md)
- [网络数据包管理入口（Network Packet Management）](P135_网络数据包管理入口.md)
  - [分组管理（Packet Management）](P025_分组管理.md)
- [网络技术（Networking Technologies）](P160_网络技术目录.md)
  - [以太网（Ethernet）](P106_以太网.md)
  - [IEEE 802.15.4](P170_IEEE802154无线网络.md)
  - [Thread 协议（Thread protocol）](P171_Thread协议.md)
  - [PPP点对点协议（Point-to-Point Protocol (PPP) Support）](P140_PPP点对点协议.md)
  - [Wi-Fi 管理（Wi-Fi Management）](P163_WiFi管理接口.md)
  - [Wi-Fi 凭据库（Wi-Fi credentials Library）](P164_WiFi凭据库.md)
- [网络协议（Protocols）](P161_网络协议目录.md)
  - [CoAP协议库（CoAP）](P064_CoAP协议库.md)
  - [CoAP客户端库（CoAP client）](P065_CoAP客户端库.md)
  - [CoAP服务器库（CoAP server）](P066_CoAP服务器库.md)
  - [CoAP_OSCORE对象安全（OSCORE Support (RFC 8613)）](P067_CoAP_OSCORE对象安全.md)
  - [FTP客户端库（FTP client）](P075_FTP客户端库.md)
  - [HTTP客户端库（HTTP Client）](P049_HTTP客户端库.md)
  - [HTTP服务器库（HTTP Server）](P055_HTTP服务器库.md)
  - [LwM2M协议栈（Lightweight M2M (LwM2M)）](P073_LwM2M协议栈.md)
  - [MCP 服务端（MCP Server）](P178_MCP服务器.md)
  - [MQTT客户端库（MQTT）](P059_MQTT客户端库.md)
  - [MQTT_SN客户端库（MQTT-SN）](P062_MQTT_SN客户端库.md)
  - [开放充电点协议（Open Charge Point Protocol (OCPP)）](P179_OCPP充电桩协议.md)
  - [RTP实时传输协议（RTP）](P141_RTP实时传输协议.md)
  - [TFTP客户端库（TFTP）](P077_TFTP客户端库.md)
  - [Latmon网络延迟监测服务（Latmon Network Service）](P094_Latmon网络延迟监测服务.md)
- [QUIC传输接口（QUIC Transport Interface）](P143_QUIC传输接口.md)
  - [概述（Overview）](P143_QUIC传输接口.md#overview)
  - [架构与概念（Architecture & Concepts）](P143_QUIC传输接口.md#architecture-concepts)
  - [应用工作流程（Application Workflow）](P143_QUIC传输接口.md#application-workflow)
  - [TLS 与安全配置（TLS & Security Configuration）](P143_QUIC传输接口.md#tls-security-configuration)
  - [会话恢复与 0-RTT（Session Resumption and 0-RTT）](P143_QUIC传输接口.md#session-resumption-and-0-rtt)
  - [路径 MTU 发现（Path MTU Discovery (DPLPMTUD)）](P143_QUIC传输接口.md#path-mtu-discovery-dplpmtud)
  - [配置选项（Configure Options）](P143_QUIC传输接口.md#configure-options)
  - [内存模型（Memory Model）](P143_QUIC传输接口.md#memory-model)
  - [Kconfig 优化器（Kconfig Optimizer）](P143_QUIC传输接口.md#kconfig-optimizer)
  - [调优指南（Tuning Guidelines）](P143_QUIC传输接口.md#tuning-guidelines)
  - [API 参考（API Reference）](P143_QUIC传输接口.md#api-reference)
- [网络系统管理（Network System Management）](P162_网络系统管理目录.md)
  - [网络配置库（Network Configuration Library）](P021_网络配置库.md)
  - [DHCPv4](P030_DHCPv4.md)
  - [DHCPv6](P031_DHCPv6.md)
  - [主机名配置（Hostname Configuration）](P033_主机名配置.md)
  - [网络核心辅助接口（Network Core Helpers）](P136_网络核心辅助接口.md)
  - [网络接口（Network Interface）](P023_网络接口.md)
  - [二层管理（L2 Layer Management）](P024_二层管理.md)
  - [网络流量卸载（Network Traffic Offloading）](P027_网络流量卸载.md)
  - [链路层地址处理（Link Layer Address Handling）](P109_链路层地址处理.md)
  - [以太网管理（Ethernet Management）](P107_以太网管理.md)
  - [流量分类（Traffic Classification）](P119_流量分类.md)
  - [网络分组过滤（Network Packet Filtering）](P028_网络分组过滤.md)
  - [网络Shell（Network Shell）](P092_网络Shell.md)
  - [TLS凭据Shell（TLS Credentials Shell）](P042_TLS凭据Shell.md)
- [时间敏感网络（Time Sensitive Networking）](P127_时间敏感网络.md)
  - [gPTP通用精确时间协议（generic Precision Time Protocol (gPTP)）](P117_gPTP通用精确时间协议.md)
  - [网络时间表示（Network time representation in the network stack）](P130_网络时间表示.md)
  - [PTP时间格式（Precision Time Protocol (PTP) time format）](P129_PTP时间格式.md)
  - [PTP精确时间协议（Precision Time Protocol (PTP)）](P128_PTP精确时间协议.md)
- [zperf网络流量生成器（zperf: Network Traffic Generator）](P096_zperf网络流量生成器.md)
  - [概述（Overview）](P096_zperf网络流量生成器.md#overview)
  - [示例用法（Sample Usage）](P096_zperf网络流量生成器.md#sample-usage)
  - [iperf3](P096_zperf网络流量生成器.md#iperf3)
  - [会话管理（Session Management）](P096_zperf网络流量生成器.md#session-management)
  - [自定义数据上传（Custom Data Upload）](P096_zperf网络流量生成器.md#custom-data-upload)
  - [原始发送模式（Raw TX Mode）](P096_zperf网络流量生成器.md#raw-tx-mode)

> 译注：以上逐项保留本官方目录页的范围与层级。已有译文使用相对链接，尚未翻译的页面仍指向官方原文；本目录完成不代表链接的子页面已完成。


<a id="networking-apis"></a>
<a id="networking-api"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：运行协议一致性测试](P157_运行协议一致性测试.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：网络通用API目录](P159_网络通用API目录.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P157_运行协议一致性测试.md) · [返回大纲](大纲.md) · [下一章](P159_网络通用API目录.md)

</details>

<!-- reading-navigation:end -->
