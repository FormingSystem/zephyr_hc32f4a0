---
id: learning.zephyr-docs.serialization.page-3
title: CBOR序列化
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/services/serialization/cbor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_CBOR序列化

原文：[官方页面](https://docs.zephyrproject.org/latest/services/serialization/cbor.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 3.1\_概述

[CBOR](https://cbor.io/) 即简洁二进制对象表示（Concise Binary Object Representation）。其设计目标包括支持极小的代码体积、较小的消息体积，以及无需版本协商（Version Negotiation）的可扩展性。

Zephyr 通过 [zcbor库](https://github.com/zephyrproject-rtos/zcbor)提供 CBOR 支持；该库作为 west 模块（West Module）引入。

## 3.2\_配置（Configuration）

启用 Kconfig 选项 [`CONFIG_ZCBOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZCBOR)，即可启用 CBOR 支持。

## 3.3\_API参考（API Reference）

zcbor 库提供自己的 API 文档；更多信息请查阅该库的文档。

> 译注：原页在这里没有内嵌 zcbor API 正文。本页完整翻译的是 Zephyr 官方页面；外部库文档不因这一引用而计作已译。


<a id="cbor"></a>
<a id="cbor-api"></a>
<a id="configuration"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：JSON序列化](P002_JSON序列化.md) · [本模块主线目录](../reading/serialization.md) · [全部主线](../reading/README.md) · [下一篇：Nanopb协议缓冲区](P004_Nanopb协议缓冲区.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P002_JSON序列化.md) · [返回大纲](大纲.md) · [下一章](P004_Nanopb协议缓冲区.md)

</details>

<!-- reading-navigation:end -->
