---
id: learning.zephyr-docs.network-core-model-reference.page-27
title: ieee802154_header_ie_rendezvous_time_full_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__rendezvous__time__full.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_ieee802154\_header\_ie\_rendezvous\_time\_full\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__rendezvous__time__full.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

完整的会合时间信息元素（Rendezvous Time IE），见第7.4.2.6节；macCslInterval非零。

```c
#include <zephyr/net/ieee802154_ie.h>
```

<a id="details"></a>

完整的会合时间信息元素（Rendezvous Time IE），见第7.4.2.6节；macCslInterval非零。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_a57a0ae2de948d7890ef61e3e245c24cd"></a>

```c
uint16_t rendezvous_time
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rendezvous_time](#a57a0ae2de948d7890ef61e3e245c24cd)。

会合时间（Rendezvous Time）。

<a id="r_a77a83a45e1292ee4dfc99d388ec8b305"></a>

```c
uint16_t wakeup_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wakeup_interval](#a77a83a45e1292ee4dfc99d388ec8b305)。

唤醒间隔（Wakeup Interval）。

## 27.2\_详细说明（Detailed Documentation）

<a id="a57a0ae2de948d7890ef61e3e245c24cd"></a>

### `rendezvous_time`

```c
uint16_t ieee802154_header_ie_rendezvous_time_full::rendezvous_time
```

会合时间（Rendezvous Time）。

<a id="a77a83a45e1292ee4dfc99d388ec8b305"></a>

### `wakeup_interval`

```c
uint16_t ieee802154_header_ie_rendezvous_time_full::wakeup_interval
```

唤醒间隔（Wakeup Interval）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_ie.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_ie.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_ieee802154_header_ie_rendezvous_time_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_ieee802154_header_ie_rendezvous_time_reduced_结构体.md)
