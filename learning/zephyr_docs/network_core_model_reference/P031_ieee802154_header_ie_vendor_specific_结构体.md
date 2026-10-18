---
id: learning.zephyr-docs.network-core-model-reference.page-31
title: ieee802154_header_ie_vendor_specific_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__vendor__specific.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_ieee802154\_header\_ie\_vendor\_specific\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__header__ie__vendor__specific.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

厂商专用头部信息元素（Vendor Specific Header IE），见第7.4.2.3节。

```c
#include <zephyr/net/ieee802154_ie.h>
```

<a id="details"></a>

厂商专用头部信息元素（Vendor Specific Header IE），见第7.4.2.3节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_a52d5ef47cbf674438bdc59aff40d0cbe"></a>

```c
uint8_t vendor_oui [IEEE802154_VENDOR_SPECIFIC_IE_OUI_LEN]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[vendor_oui](#a52d5ef47cbf674438bdc59aff40d0cbe)。

厂商的组织唯一标识符（OUI）。

<a id="r_a7227c96e07f5cd26353d10710d5a8db1"></a>

```c
uint8_t * vendor_specific_info
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[vendor_specific_info](#a7227c96e07f5cd26353d10710d5a8db1)。

厂商专用信息（Vendor Specific Information）。

## 31.2\_详细说明（Detailed Documentation）

<a id="a52d5ef47cbf674438bdc59aff40d0cbe"></a>

### `vendor_oui`

```c
uint8_t ieee802154_header_ie_vendor_specific::vendor_oui[IEEE802154_VENDOR_SPECIFIC_IE_OUI_LEN]
```

厂商的组织唯一标识符（OUI）。

<a id="a7227c96e07f5cd26353d10710d5a8db1"></a>

### `vendor_specific_info`

```c
uint8_t* ieee802154_header_ie_vendor_specific::vendor_specific_info
```

厂商专用信息（Vendor Specific Information）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_ie.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_ie.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_ieee802154_header_ie_time_correction_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_ieee802154_key_结构体.md)
