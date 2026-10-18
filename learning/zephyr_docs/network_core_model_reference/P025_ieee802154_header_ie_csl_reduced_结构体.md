---
id: learning.zephyr-docs.network-core-model-reference.page-25
title: ieee802154_header_ie_csl_reduced_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__csl__reduced.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_ieee802154\_header\_ie\_csl\_reduced\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__csl__reduced.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

精简的协调采样监听信息元素（CSL IE），见第7.4.2.3节。

```c
#include <zephyr/net/ieee802154_ie.h>
```

<a id="details"></a>

精简的协调采样监听信息元素（CSL IE），见第7.4.2.3节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a6fb0873938f857263280286c7aedda11"></a>

```c
uint16_t csl_phase
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[csl_phase](#a6fb0873938f857263280286c7aedda11)。

协调采样监听（CSL）的相位。

<a id="r_a967fe59ea8da123bf07d9184195d00d3"></a>

```c
uint16_t csl_period
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[csl_period](#a967fe59ea8da123bf07d9184195d00d3)。

协调采样监听（CSL）的周期。

## 25.2\_详细说明（Detailed Documentation）

<a id="a967fe59ea8da123bf07d9184195d00d3"></a>

### `csl_period`

```c
uint16_t ieee802154_header_ie_csl_reduced::csl_period
```

协调采样监听（CSL）的周期。

<a id="a6fb0873938f857263280286c7aedda11"></a>

### `csl_phase`

```c
uint16_t ieee802154_header_ie_csl_reduced::csl_phase
```

协调采样监听（CSL）的相位。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_ie.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_ie.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_ieee802154_header_ie_csl_full_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_ieee802154_header_ie_rendezvous_time_结构体.md)
