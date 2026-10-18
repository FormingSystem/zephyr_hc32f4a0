---
id: learning.zephyr-docs.networking.page-141
title: RTP实时传输协议
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/rtp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第141章\_RTP实时传输协议

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/rtp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

实时传输协议（Real-time Transport Protocol，RTP，[RFC 3550](https://datatracker.ietf.org/doc/html/rfc3550.html)）通过 UDP 承载音频等媒体流。Zephyr 通过 [`CONFIG_RTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP) 启用 RTP 数据平面（Data Plane），包含会话管理、包的序列化／反序列化和两个传输后端。实时传输控制协议（RTCP）尚未实现。

应用使用 [`RTP_SESSION_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga71c2946f19f3350591f81ae5856c917a) 声明会话，通过 [`rtp_session_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7dc5320de0686db3acc8ea9e75ac2bfc) 将其配置为发送源（Source）、接收端（Sink）或同时收发，再用 [`rtp_session_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga5d7875fd2dda60e9bf827146b3ec6ad0) 启动。载荷由 [`rtp_session_send()`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga02216271230f855d94b44b78f4757b5e) 发送，接收包通过网络接收上下文调用的回调交给应用。

可选传输方式：

- 套接字（Socket），[`CONFIG_RTP_TRANSPORT_SOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP_TRANSPORT_SOCKET)：使用 BSD 套接字和后台套接字服务轮询，这是默认方式。
- 网络数据包（`net_pkt`），[`CONFIG_RTP_TRANSPORT_NET_PKT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP_TRANSPORT_NET_PKT)：直接构造 `net_pkt` 缓冲区，绕过套接字层，尽量减少开销。

原文注记：RTP 支持仍属实验性（Experimental），API 和 Kconfig 选项可能变化。

> 译注——回调生命周期：官方 [`rtp.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/rtp.h) 要求接收回调保持简短、不阻塞；载荷指针只在本次回调期间有效，需要延后处理时应由应用复制所需数据。其他线程停止会话接收路径时，仍可能有并发或即将派发的回调；不能将“已停止”直接当作再无回调的保证。

## 2. 示例（Samples）

[RTP 示例](P142_RTP发送示例.md#net-rtp)：通过 UDP 组播发送或接收 RTP 音频流。

## 3. API 参考（API Reference）

[RTP 实时传输协议 API](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html)。


<a id="rtp"></a>
<a id="rtp-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="samples"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：PPP点对点协议](P140_PPP点对点协议.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：QUIC传输接口](P143_QUIC传输接口.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P140_PPP点对点协议.md) · [返回大纲](大纲.md) · [下一章](P142_RTP发送示例.md)

</details>

<!-- reading-navigation:end -->
