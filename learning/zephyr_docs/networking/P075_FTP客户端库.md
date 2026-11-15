---
id: learning.zephyr-docs.networking.page-75
title: FTP客户端库
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/ftp_client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_FTP客户端库

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/ftp_client.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 75.1 概览（Overview）

文件传输协议（File Transfer Protocol，FTP）客户端库可以从 FTP 服务器下载文件，也可以向服务器上传文件。

库通过两个独立回调分别报告控制消息（Control Message）和下载数据：[`ftp_client.ctrl_callback`](P083_FTP客户端上下文.md#a19824800556b11ce885f2ea1864ee906) 处理控制消息，[`ftp_client.data_callback`](P083_FTP客户端上下文.md#a46ff461b642c07682cee9e6a1b4561a8) 处理数据。

[`CONFIG_FTP_CLIENT_KEEPALIVE_TIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FTP_CLIENT_KEEPALIVE_TIME) 非零时，库通过定时机制向服务器自动发送保活消息（KEEPALIVE）；每经过该配置指定的时间间隔发送一次。

> 源码核对译注：官方 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ftp/Kconfig) 将间隔定义为秒，默认 60 秒；设为 0 禁用自动保活，但应用仍可调用 `ftp_keepalive()`。当前[实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ftp/ftp_client.c)实际发送 FTP `NOOP` 命令并等待 `200` 响应；原文的 KEEPALIVE 是功能名称。

## 75.2 协议（Protocols）

该库按照[RFC 959](https://datatracker.ietf.org/doc/html/rfc959.html)实现。

## 75.3 限制（Limitations）

目前只实现最小的一组命令，但可以继续扩展支持。不同 FTP 服务器实现存在差异，因此与特定服务器配合时可能需要定制。

## 75.4 API 与示例（API Reference）

详细接口见[FTP 客户端库 API](P080_FTP完整API参考.md)。[FTP 客户端 Shell 示例](P076_FTP客户端示例.md#ftp-client)展示如何通过 Zephyr Shell 与服务器交互。指南、示例及详细 API 分别跟踪翻译状态；本轮未连接服务器或传输文件。


<a id="ftp-client"></a>
<a id="ftp-client-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="overview"></a>
<a id="protocols"></a>
<a id="index-0"></a>
<a id="limitations"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：LwM2M协议栈](P073_LwM2M协议栈.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：TFTP客户端库](P077_TFTP客户端库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P074_LwM2M客户端示例.md) · [返回大纲](大纲.md) · [下一章](P076_FTP客户端示例.md)

</details>

<!-- reading-navigation:end -->
