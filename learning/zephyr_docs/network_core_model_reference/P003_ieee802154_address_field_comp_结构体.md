---
id: learning.zephyr-docs.network-core-model-reference.page-3
title: ieee802154_address_field_comp_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__address__field__comp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_ieee802154\_address\_field\_comp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__address__field__comp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PAN ID压缩（PAN ID Compression）省略PAN ID时的目的地址或源地址字段。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

PAN ID压缩（PAN ID Compression）省略PAN ID时的目的地址或源地址字段。见第7.2.2.6节；此形式只携带地址。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a3c7f8e5bb1f015e02123669726fbcf6c"></a>

```c
struct ieee802154_address addr
```

相关声明：[ieee802154_address](P001_ieee802154_address_结构体.md)、[addr](#a3c7f8e5bb1f015e02123669726fbcf6c)。

省略PAN ID时的短地址（Short Address）或扩展地址（Extended Address），即压缩形式。

## 3.2\_详细说明（Detailed Documentation）

<a id="a3c7f8e5bb1f015e02123669726fbcf6c"></a>

### `addr`

```c
struct ieee802154_address ieee802154_address_field_comp::addr
```

省略PAN ID时的短地址（Short Address）或扩展地址（Extended Address），即压缩形式。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [ieee802154_address](P001_ieee802154_address_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_ieee802154_address_field_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_ieee802154_address_field_plain_结构体.md)
