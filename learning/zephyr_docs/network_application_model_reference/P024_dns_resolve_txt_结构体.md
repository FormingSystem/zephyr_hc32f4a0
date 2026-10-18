---
id: learning.zephyr-docs.network-application-model-reference.page-24
title: dns_resolve_txt_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__txt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_dns\_resolve\_txt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__txt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

文本记录（TXT）的信息。

```c
#include <zephyr/net/dns_resolve.h>
```

<a id="details"></a>

文本记录（TXT）的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a332e2e090d86a7ff1278a5dc825f0843"></a>

```c
size_t textlen
```

相关声明：[textlen](#a332e2e090d86a7ff1278a5dc825f0843)。

text字段的长度。

<a id="r_a70076b35c818d2b67fdf0f38262a59e9"></a>

```c
char text [64+1]
```

相关声明：[text](#a70076b35c818d2b67fdf0f38262a59e9)。

text字段，以NULL结尾。

## 24.2\_详细说明（Detailed Documentation）

<a id="a70076b35c818d2b67fdf0f38262a59e9"></a>

### `text`

```c
char dns_resolve_txt::text[64+1]
```

text字段，以NULL结尾。

<a id="a332e2e090d86a7ff1278a5dc825f0843"></a>

### `textlen`

```c
size_t dns_resolve_txt::textlen
```

text字段的长度。

本数据类型文档由以下文件生成：

- `zephyr/net/dns_resolve.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/net/dns_resolve.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_dns_resolve_srv_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_dns_sd_rec_结构体.md)
