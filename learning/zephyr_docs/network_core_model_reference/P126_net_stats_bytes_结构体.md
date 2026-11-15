---
id: learning.zephyr-docs.network-core-model-reference.page-126
title: net_stats_bytes_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__bytes.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第126章\_net\_stats\_bytes\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__bytes.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

发送与接收的字节数（Bytes Sent and Received）。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

发送与接收的字节数（Bytes Sent and Received）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 126.1\_数据成员（Data Fields）

<a id="r_a360bdbf177d60b0677beec2037f34cb0"></a>

```c
uint64_t sent
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[sent](#a360bdbf177d60b0677beec2037f34cb0)。

已发送的字节数（Bytes sent）。

<a id="r_a9f87e32d63bc4239ef7db03feedd495e"></a>

```c
uint64_t received
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[received](#a9f87e32d63bc4239ef7db03feedd495e)。

已接收的字节数（Bytes received）。

## 126.2\_详细说明（Detailed Documentation）

<a id="a9f87e32d63bc4239ef7db03feedd495e"></a>

### `received`

```c
uint64_t net_stats_bytes::received
```

已接收的字节数（Bytes received）。

<a id="a360bdbf177d60b0677beec2037f34cb0"></a>

### `sent`

```c
uint64_t net_stats_bytes::sent
```

已发送的字节数（Bytes sent）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 126.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P125_net_stats_结构体.md) · [返回大纲](大纲.md) · [下一章](P127_net_stats_dns_结构体.md)
