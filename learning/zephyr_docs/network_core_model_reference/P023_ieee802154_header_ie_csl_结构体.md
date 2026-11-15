---
id: learning.zephyr-docs.network-core-model-reference.page-23
title: ieee802154_header_ie_csl_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__csl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_ieee802154\_header\_ie\_csl\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__csl.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用协调采样监听信息元素（CSL IE），见第7.4.2.3节。

```c
#include <zephyr/net/ieee802154_ie.h>
```

<a id="details"></a>

通用协调采样监听信息元素（CSL IE），见第7.4.2.3节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a73eb4feaf8ef3b122b88abe1fc6b9e08"></a>

```c
struct ieee802154_header_ie_csl_full full
```

相关声明：[ieee802154_header_ie_csl_full](P024_ieee802154_header_ie_csl_full_结构体.md)、[full](#abb040a32c97c219ae0674a30ce3c916b)。

协调采样监听（CSL）的完整信息。

<a id="r_a5b95e6edbd44c4d5650992540155b0a6"></a>

```c
struct ieee802154_header_ie_csl_reduced reduced
```

相关声明：[ieee802154_header_ie_csl_reduced](P025_ieee802154_header_ie_csl_reduced_结构体.md)、[reduced](#a8373e14f7c6cd1dfe8cd214dfa5d0676)。

协调采样监听（CSL）的精简信息。

<a id="r_aa325120993785fd17e1c49b74c2fdc4f"></a>

```c
};
```

## 23.2\_详细说明（Detailed Documentation）

<a id="aa325120993785fd17e1c49b74c2fdc4f"></a>

### `[union]`

```c
union { ... } ieee802154_header_ie_csl
```

<a id="abb040a32c97c219ae0674a30ce3c916b"></a>

### `full`

```c
struct ieee802154_header_ie_csl_full ieee802154_header_ie_csl::full
```

协调采样监听（CSL）的完整信息。

<a id="a8373e14f7c6cd1dfe8cd214dfa5d0676"></a>

### `reduced`

```c
struct ieee802154_header_ie_csl_reduced ieee802154_header_ie_csl::reduced
```

协调采样监听（CSL）的精简信息。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_ie.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_ie.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h_source.html)
- [ieee802154_header_ie_csl_full](P024_ieee802154_header_ie_csl_full_结构体.md)
- [ieee802154_header_ie_csl_reduced](P025_ieee802154_header_ie_csl_reduced_结构体.md)
- [ieee802154_header_ie_csl](P023_ieee802154_header_ie_csl_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_ieee802154_gts_spec_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_ieee802154_header_ie_csl_full_结构体.md)
