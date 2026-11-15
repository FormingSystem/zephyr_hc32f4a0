---
id: learning.zephyr-docs.network-core-model-reference.page-39
title: ieee802154_phy_channel_range_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__phy__channel__range.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_ieee802154\_phy\_channel\_range\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__phy__channel__range.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示一个受支持的信道范围（Channel Range），见ieee802154_phy_supported_channels。

```c
#include <zephyr/net/ieee802154_radio.h>
```

<a id="details"></a>

表示一个受支持的信道范围（Channel Range），见ieee802154_phy_supported_channels。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_aec90e36227a7d9cc1dfc18231341dd03"></a>

```c
uint16_t from_channel
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[from_channel](#aec90e36227a7d9cc1dfc18231341dd03)。

信道范围（Channel Range）的起点。

<a id="r_a78af593807753dbfcfce88166f4c1f58"></a>

```c
uint16_t to_channel
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[to_channel](#a78af593807753dbfcfce88166f4c1f58)。

信道范围（Channel Range）的终点。

## 39.2\_详细说明（Detailed Documentation）

<a id="aec90e36227a7d9cc1dfc18231341dd03"></a>

### `from_channel`

```c
uint16_t ieee802154_phy_channel_range::from_channel
```

信道范围（Channel Range）的起点。

<a id="a78af593807753dbfcfce88166f4c1f58"></a>

### `to_channel`

```c
uint16_t ieee802154_phy_channel_range::to_channel
```

信道范围（Channel Range）的终点。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_radio.h`

## 39.3\_原页交叉引用（Cross References）

- [ieee802154_phy_supported_channels](P040_ieee802154_phy_supported_channels_结构体.md)
- [zephyr/net/ieee802154_radio.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_ieee802154_pas_spec_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_ieee802154_phy_supported_channels_结构体.md)
