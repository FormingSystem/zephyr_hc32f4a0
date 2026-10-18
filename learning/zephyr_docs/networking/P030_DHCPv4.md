---
id: learning.zephyr-docs.networking.page-30
title: DHCPv4
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/dhcpv4.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_DHCPv4

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/dhcpv4.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 30.1\_概览（Overview）

动态主机配置协议（Dynamic Host Configuration Protocol，DHCP）是 IPv4 网络中的网络管理协议。DHCPv4 服务器为网络设备动态分配 IPv4 地址及其他网络参数，使设备能够与其他 IP 网络通信。

协议工作过程的进一步概述见原文引用的[DHCP 百科条目](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol)。Zephyr 同时支持 DHCPv4 客户端（Client）与服务器（Server）功能。

## 30.2\_用法与接口参考

[DHCPv4 客户端示例](P035_DHCPv4客户端示例.md#dhcpv4-client)演示启动客户端并从服务器取得 IPv4 地址。详细 API 见[DHCPv4 接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html)。


<a id="dhcpv4"></a>
<a id="dhcpv4-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="overview"></a>
<a id="sample-usage"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：网络分组捕获](P029_网络分组捕获.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：DHCPv6](P031_DHCPv6.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P029_网络分组捕获.md) · [返回大纲](大纲.md) · [下一章](P031_DHCPv6.md)

</details>

<!-- reading-navigation:end -->
