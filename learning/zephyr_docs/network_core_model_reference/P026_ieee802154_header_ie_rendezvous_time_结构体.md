---
id: learning.zephyr-docs.network-core-model-reference.page-26
title: ieee802154_header_ie_rendezvous_time_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__rendezvous__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_ieee802154\_header\_ie\_rendezvous\_time\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__rendezvous__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

会合时间信息元素（Rendezvous Time IE），见第7.4.2.6节。

```c
#include <zephyr/net/ieee802154_ie.h>
```

<a id="details"></a>

会合时间信息元素（Rendezvous Time IE），见第7.4.2.6节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a06026191c9ce99a9bf6669e47a08bf06"></a>

```c
struct ieee802154_header_ie_rendezvous_time_full full
```

相关声明：[ieee802154_header_ie_rendezvous_time_full](P027_ieee802154_header_ie_rendezvous_time_full_结构体.md)、[full](#ad977678922a3cecd1159a9089c5d41b5)。

会合时间（Rendezvous Time）的完整信息。

<a id="r_afaaf6c8b07840fa7099a814c4ed3a82e"></a>

```c
struct ieee802154_header_ie_rendezvous_time_reduced reduced
```

相关声明：[ieee802154_header_ie_rendezvous_time_reduced](P028_ieee802154_header_ie_rendezvous_time_reduced_结构体.md)、[reduced](#a620857d35fb7dd3a56d193c7f056e4b5)。

会合时间（Rendezvous Time）的精简信息。

<a id="r_ac52322722b1ecd41dd43a33aaecc4e08"></a>

```c
};
```

## 26.2\_详细说明（Detailed Documentation）

<a id="ac52322722b1ecd41dd43a33aaecc4e08"></a>

### `[union]`

```c
union { ... } ieee802154_header_ie_rendezvous_time
```

<a id="ad977678922a3cecd1159a9089c5d41b5"></a>

### `full`

```c
struct ieee802154_header_ie_rendezvous_time_full ieee802154_header_ie_rendezvous_time::full
```

会合时间（Rendezvous Time）的完整信息。

<a id="a620857d35fb7dd3a56d193c7f056e4b5"></a>

### `reduced`

```c
struct ieee802154_header_ie_rendezvous_time_reduced ieee802154_header_ie_rendezvous_time::reduced
```

会合时间（Rendezvous Time）的精简信息。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_ie.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_ie.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h_source.html)
- [ieee802154_header_ie_rendezvous_time_full](P027_ieee802154_header_ie_rendezvous_time_full_结构体.md)
- [ieee802154_header_ie_rendezvous_time_reduced](P028_ieee802154_header_ie_rendezvous_time_reduced_结构体.md)
- [ieee802154_header_ie_rendezvous_time](P026_ieee802154_header_ie_rendezvous_time_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_ieee802154_header_ie_csl_reduced_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_ieee802154_header_ie_rendezvous_time_full_结构体.md)
