---
id: learning.zephyr-docs.network-core-model-reference.page-30
title: ieee802154_header_ie_time_correction_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__time__correction.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_ieee802154\_header\_ie\_time\_correction\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__time__correction.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

时间校正信息元素（Time Correction IE），见第7.4.2.7节。

```c
#include <zephyr/net/ieee802154_ie.h>
```

<a id="details"></a>

时间校正信息元素（Time Correction IE），见第7.4.2.7节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a9ee84948740e66d1ee16786de5f38880"></a>

```c
uint16_t time_sync_info
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[time_sync_info](#a9ee84948740e66d1ee16786de5f38880)。

时间同步信息（Time Synchronization Information）。

## 30.2\_详细说明（Detailed Documentation）

<a id="a9ee84948740e66d1ee16786de5f38880"></a>

### `time_sync_info`

```c
uint16_t ieee802154_header_ie_time_correction::time_sync_info
```

时间同步信息（Time Synchronization Information）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_ie.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_ie.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_ieee802154_header_ie_rit_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_ieee802154_header_ie_vendor_specific_结构体.md)
