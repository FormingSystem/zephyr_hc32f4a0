---
id: learning.zephyr-docs.network-application-model-reference.page-28
title: http_content_range_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__content__range.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_http\_content\_range\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__content__range.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/net/http/parser.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_af32a14a0b8ae40722278c8839ab9429c"></a>

```c
uint64_t start
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[start](#af32a14a0b8ae40722278c8839ab9429c)。

<a id="r_a4be2d7ae61240cc739ac14971946abfa"></a>

```c
uint64_t end
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[end](#a4be2d7ae61240cc739ac14971946abfa)。

<a id="r_a3c96329567d948ecc2f5be5febf48bf4"></a>

```c
uint64_t total
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[total](#a3c96329567d948ecc2f5be5febf48bf4)。

## 28.2\_详细说明（Detailed Documentation）

<a id="a4be2d7ae61240cc739ac14971946abfa"></a>

### `end`

```c
uint64_t http_content_range::end
```

<a id="af32a14a0b8ae40722278c8839ab9429c"></a>

### `start`

```c
uint64_t http_content_range::start
```

<a id="a3c96329567d948ecc2f5be5febf48bf4"></a>

### `total`

```c
uint64_t http_content_range::total
```

本数据类型文档由以下文件生成：

- `zephyr/net/http/parser.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/net/http/parser.h](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_http_client_internal_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_http_content_type_结构体.md)
