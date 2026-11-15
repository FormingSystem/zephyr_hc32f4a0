---
id: learning.zephyr-docs.networking.page-34
title: SNTP时间同步库
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/sntp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_SNTP时间同步库

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/sntp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 34.1\_概览（Overview）

简单网络时间协议（Simple Network Time Protocol，SNTP）库实现 [RFC 4330](https://datatracker.ietf.org/doc/html/rfc4330.html)，用于在计算机网络中同步时钟。

客户端由 [`CONFIG_SNTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SNTP) 启用，向 SNTP 服务器查询时间。服务器由 [`CONFIG_SNTP_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SNTP_SERVER) 启用，在所有已启用的地址族上监听 UDP `123` 端口并回答查询。

应用负责设置系统时钟，再用 [`sntp_server_clock_source()`](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp__server.html#ga36c5b4a695294c7ad6777fe79d08b798) 告知服务器时间来源。在完成此步骤前，服务器应答中的闰秒指示器（Leap Indicator）设为“时钟未同步”，层级（Stratum）为 `16`，使客户端丢弃该时间戳。

## 34.2\_API 参考与示例

客户端接口见[SNTP API](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html)，服务端接口见[SNTP 服务器 API](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp__server.html)。

- [AWS IoT Core MQTT](P216_AWS物联网MQTT示例.md#aws-iot-mqtt)：连接 AWS IoT Core 并使用 MQTT 发布消息。
- [SNTP 客户端示例](P038_SNTP客户端示例.md#sntp-client)：通过 SNTP 从主机获取当前时间。
- [SNTP 服务器示例](P039_SNTP服务器示例.md#sntp-server)：向网络中的 SNTP 客户端提供当前时间。


<a id="simple-network-time-protocol-library"></a>
<a id="sntp-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：主机名配置](P033_主机名配置.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：BSD套接字](P040_BSD套接字.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P033_主机名配置.md) · [返回大纲](大纲.md) · [下一章](P035_DHCPv4客户端示例.md)

</details>

<!-- reading-navigation:end -->
