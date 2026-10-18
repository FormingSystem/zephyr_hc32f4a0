---
id: learning.zephyr-docs.networking.page-39
title: SNTP服务器示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/sntp_server/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_SNTP服务器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/sntp_server/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 39.1\_概览（Overview）

本示例实现简单的 SNTP 服务器，源码见官方 [`samples/net/sockets/sntp_server`](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/sockets/sntp_server)。

启动时，示例查询 [`CONFIG_NET_SAMPLE_SNTP_UPSTREAM_ADDRESS`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/sntp_server/Kconfig) 配置的上游 SNTP 服务器，用响应设置系统时钟。随后，在所有已启用的地址族上通过默认 UDP `123` 端口向客户端提供时间。

上游服务器没有默认地址，应按实际网络设置，例如 `pool.ntp.org`。没有配置时，示例仍启动服务器，但会告知客户端时钟未同步，返回的时间戳不能使用。

可以使用 `ntpdig`、`sntp` 等 SNTP 客户端查询它。平台必须具备网络支持，可能还需调整配置。

> 源码跟踪译注：该上游地址是本示例的配置选项，定义见[官方示例 Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/sntp_server/Kconfig)，默认空字符串。它不是所有 Zephyr 应用自动共享的全局时间服务器设置；本仓库缺少的新版示例文件使用官方来源链接，不伪造本地文件入口。

## 39.2\_构建与运行（Building and Running）

主机侧进一步说明见 [net-tools](https://github.com/zephyrproject-rtos/net-tools) 项目。原文说明可按[QEMU 联网指南](P009_QEMU联网概览.md#networking-with-qemu)在 QEMU 或 `native_sim` 上构建运行，本页没有另外列出命令。

通过 [Wi-Fi 配置片段（Snippet）](../snippets/P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)可启用 IPv4 Wi-Fi 支持。

## 39.3\_相关接口

- [BSD 套接字兼容 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)。
- [SNTP API](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html)。
- [SNTP 服务器 API](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp__server.html)。


<a id="sntp-server"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="wi-fi"></a>
<a id="see-also"></a>

[上一章](P038_SNTP客户端示例.md) · [返回大纲](大纲.md) · [下一章](P040_BSD套接字.md)
