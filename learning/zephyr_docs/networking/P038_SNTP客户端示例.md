---
id: learning.zephyr-docs.networking.page-38
title: SNTP客户端示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/sntp_client/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_SNTP客户端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/sntp_client/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 38.1\_概览（Overview）

此示例是简单网络时间协议（SNTP）客户端，展示如何取得自 `1970 年 1 月 1 日` 起经过的秒数，即纪元时间（Epoch Time）。官方源码见 [`samples/net/sockets/sntp_client`](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/sockets/sntp_client)。

所选平台需要网络支持，配置可能需要按平台调整；本例还假定主机正在运行 SNTP 服务器。

## 38.2\_构建与运行（Building and Running）

应用运行后，向主机发送 SNTP 请求并等待响应。收到后打印当前纪元秒数和响应状态码，成功状态为 `0`。

主机侧更多设置见 [net-tools](https://github.com/zephyrproject-rtos/net-tools) 项目。可以在 QEMU 或 `native_sim` 上构建运行，原文指向[QEMU 联网指南](P009_QEMU联网概览.md#networking-with-qemu)。

通过 [Wi-Fi 配置片段（Snippet）](../snippets/P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)可启用 IPv4 Wi-Fi 支持。

> 译注：官方本页没有单列构建命令，主要给出运行行为与联网指南入口。查询得到时间不应自动理解为该示例已替应用完成系统时钟设置；本轮未发起时间查询。

## 38.3\_相关接口

- [BSD 套接字兼容 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)。
- [SNTP API](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html)。


<a id="sntp-client"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="wi-fi"></a>
<a id="see-also"></a>

[上一章](P037_DNS解析示例.md) · [返回大纲](大纲.md) · [下一章](P039_SNTP服务器示例.md)
