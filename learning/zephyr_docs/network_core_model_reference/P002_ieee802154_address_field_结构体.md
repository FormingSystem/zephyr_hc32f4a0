---
id: learning.zephyr-docs.network-core-model-reference.page-2
title: ieee802154_address_field_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__address__field.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_ieee802154\_address\_field\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__address__field.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以压缩或原始形式表示的目的地址或源地址字段（Destination / Source Address）。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

采用压缩或普通形式的目的地址或源地址字段（Destination / Source Address）。具体使用哪一种形式，由第7.2.2节的帧控制与寻址模式规则确定。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a58dce1fabcdb06a759cefcdb6a00a6a4"></a>

```c
struct ieee802154_address_field_plain plain
```

相关声明：[ieee802154_address_field_plain](P004_ieee802154_address_field_plain_结构体.md)、[plain](#ae06d1451a3006bfe10abc6148ce8ebce)。

个人区域网标识（PAN ID）和地址，采用普通寻址（Plain Addressing）。

<a id="r_a57541b84a7abf3553df137503d093a42"></a>

```c
struct ieee802154_address_field_comp comp
```

相关声明：[ieee802154_address_field_comp](P003_ieee802154_address_field_comp_结构体.md)、[comp](#af3df38a8424bfe75cd8ad9694b31074f)。

仅包含地址，采用PAN ID压缩（PAN ID Compressed）。

<a id="r_a54180bc0ed0c1f4ffcff7143ffcc4776"></a>

```c
};
```

普通或PAN压缩形式的目的地址/源地址字段（Destination / Source Address）。

## 2.2\_详细说明（Detailed Documentation）

<a id="a54180bc0ed0c1f4ffcff7143ffcc4776"></a>

### `[union]`

```c
union { ... } ieee802154_address_field
```

普通或PAN压缩形式的目的地址/源地址字段（Destination / Source Address）。

见第7.2.2.6节。

<a id="af3df38a8424bfe75cd8ad9694b31074f"></a>

### `comp`

```c
struct ieee802154_address_field_comp ieee802154_address_field::comp
```

仅包含地址，采用PAN ID压缩（PAN ID Compressed）。

<a id="ae06d1451a3006bfe10abc6148ce8ebce"></a>

### `plain`

```c
struct ieee802154_address_field_plain ieee802154_address_field::plain
```

个人区域网标识（PAN ID）和地址，采用普通寻址（Plain Addressing）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [ieee802154_address_field_plain](P004_ieee802154_address_field_plain_结构体.md)
- [ieee802154_address_field_comp](P003_ieee802154_address_field_comp_结构体.md)
- [ieee802154_address_field](P002_ieee802154_address_field_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_ieee802154_address_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_ieee802154_address_field_comp_结构体.md)
