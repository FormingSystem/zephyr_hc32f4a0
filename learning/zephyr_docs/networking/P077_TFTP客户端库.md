---
id: learning.zephyr-docs.networking.page-77
title: TFTP客户端库
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/tftp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_TFTP客户端库

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/tftp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 77.1 概览

Zephyr 提供简单的 TFTP 客户端库。TFTP 是简单文件传输协议（Trivial File Transfer Protocol），通过 [`CONFIG_TFTP_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFTP_LIB) 启用。

库的具体用法见[TFTP 客户端示例](P078_TFTP客户端示例.md#tftp-client)，它展示如何从服务器获取文件以及向服务器写入文件。

## 77.2 API 参考（API Reference）

详细接口见[TFTP 客户端库 API](P084_TFTP完整API参考.md)。本官方页面仅为库入口，详细 API 与[客户端示例](P078_TFTP客户端示例.md#tftp-client)分别跟踪翻译状态，不因入口完成而计为全部完成。


<a id="tftp"></a>
<a id="tftp-interface"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：FTP客户端库](P075_FTP客户端库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：SOCKS5代理支持](P079_SOCKS5代理支持.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P076_FTP客户端示例.md) · [返回大纲](大纲.md) · [下一章](P078_TFTP客户端示例.md)

</details>

<!-- reading-navigation:end -->
