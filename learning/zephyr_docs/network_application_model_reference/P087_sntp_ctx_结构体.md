---
id: learning.zephyr-docs.network-application-model-reference.page-87
title: sntp_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsntp__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_sntp\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsntp__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

简单网络时间协议（SNTP）的上下文。

```c
#include <zephyr/net/sntp.h>
```

<a id="details"></a>

简单网络时间协议（SNTP）的上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 87.1\_数据成员（Data Fields）

<a id="r_a58bd69ad86d00183e32ed07a9fbebfdc"></a>

```c
struct sntp_time expected_orig_ts
```

相关声明：[sntp_time](P088_sntp_time_结构体.md)、[expected_orig_ts](#a58bd69ad86d00183e32ed07a9fbebfdc)。

客户端向服务器发送请求时的时间戳（Timestamp）。

## 87.2\_详细说明（Detailed Documentation）

<a id="a58bd69ad86d00183e32ed07a9fbebfdc"></a>

### `expected_orig_ts`

```c
struct sntp_time sntp_ctx::expected_orig_ts
```

客户端向服务器发送请求时的时间戳（Timestamp）。

用于检查服务器应答中的起始时间戳（Originated Timestamp）是否与客户端请求中的时间戳一致。

本数据类型文档由以下文件生成：

- `zephyr/net/sntp.h`

## 87.3\_原页交叉引用（Cross References）

- [zephyr/net/sntp.h](https://docs.zephyrproject.org/latest/doxygen/html/sntp_8h_source.html)
- [sntp_time](P088_sntp_time_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P086_rtp_transport_结构体.md) · [返回大纲](大纲.md) · [下一章](P088_sntp_time_结构体.md)
