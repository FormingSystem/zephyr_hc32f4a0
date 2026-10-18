---
id: learning.zephyr-docs.network-core-model-reference.page-24
title: ieee802154_header_ie_csl_full_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__csl__full.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_ieee802154\_header\_ie\_csl\_full\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__csl__full.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

完整的协调采样监听信息元素（CSL IE），见第7.4.2.3节。

```c
#include <zephyr/net/ieee802154_ie.h>
```

<a id="details"></a>

完整的协调采样监听信息元素（CSL IE），见第7.4.2.3节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a27089bfc19fbef2e79c5dce1a300a7b6"></a>

```c
uint16_t csl_phase
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[csl_phase](#a27089bfc19fbef2e79c5dce1a300a7b6)。

协调采样监听（CSL）的相位。

<a id="r_a6633583d786b2935e27a9feb8918227d"></a>

```c
uint16_t csl_period
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[csl_period](#a6633583d786b2935e27a9feb8918227d)。

协调采样监听（CSL）的周期。

<a id="r_aec452cd03e9baa50253aaafd2232a011"></a>

```c
uint16_t csl_rendezvous_time
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[csl_rendezvous_time](#aec452cd03e9baa50253aaafd2232a011)。

会合时间（Rendezvous Time）。

## 24.2\_详细说明（Detailed Documentation）

<a id="a6633583d786b2935e27a9feb8918227d"></a>

### `csl_period`

```c
uint16_t ieee802154_header_ie_csl_full::csl_period
```

协调采样监听（CSL）的周期。

<a id="a27089bfc19fbef2e79c5dce1a300a7b6"></a>

### `csl_phase`

```c
uint16_t ieee802154_header_ie_csl_full::csl_phase
```

协调采样监听（CSL）的相位。

<a id="aec452cd03e9baa50253aaafd2232a011"></a>

### `csl_rendezvous_time`

```c
uint16_t ieee802154_header_ie_csl_full::csl_rendezvous_time
```

会合时间（Rendezvous Time）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_ie.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_ie.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_ieee802154_header_ie_csl_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_ieee802154_header_ie_csl_reduced_结构体.md)
