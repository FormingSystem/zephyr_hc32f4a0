---
id: learning.zephyr-docs.network-core-model-reference.page-4
title: ieee802154_address_field_plain_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__address__field__plain.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_ieee802154\_address\_field\_plain\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__address__field__plain.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含PAN ID和地址的目的地址或源地址字段（Destination / Source Address）。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

包含PAN ID与地址的目的地址或源地址字段（Destination / Source Address）。见第7.2.2.6节及图7-4。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a8237aa26d9e3d564c349f90c8841cee7"></a>

```c
uint16_t pan_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pan_id](#a8237aa26d9e3d564c349f90c8841cee7)。

此地址字段的个人区域网标识（PAN Identifier）。

<a id="r_aff9f5b6d0392c0ba401cb90d63631214"></a>

```c
struct ieee802154_address addr
```

相关声明：[ieee802154_address](P001_ieee802154_address_结构体.md)、[addr](#aff9f5b6d0392c0ba401cb90d63631214)。

PAN ID之后的短地址（Short Address）或扩展地址（Extended Address）。

## 4.2\_详细说明（Detailed Documentation）

<a id="aff9f5b6d0392c0ba401cb90d63631214"></a>

### `addr`

```c
struct ieee802154_address ieee802154_address_field_plain::addr
```

PAN ID之后的短地址（Short Address）或扩展地址（Extended Address）。

<a id="a8237aa26d9e3d564c349f90c8841cee7"></a>

### `pan_id`

```c
uint16_t ieee802154_address_field_plain::pan_id
```

此地址字段的个人区域网标识（PAN Identifier）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [ieee802154_address](P001_ieee802154_address_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_ieee802154_address_field_comp_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_ieee802154_attr_value_结构体.md)
