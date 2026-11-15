---
id: learning.zephyr-docs.network-core-model-reference.page-38
title: ieee802154_pas_spec_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__pas__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_ieee802154\_pas\_spec\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__pas__spec.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

信标载荷中的待处理地址规范（Pending Address Specification）字段。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

信标载荷的待处理地址规范（Pending Address Specification）字段。见第7.3.1.6节及图7-13。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a607b544fb918ecd26c1448597e00c5f6"></a>

```c
uint8_t reserved_1: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved_1](#a607b544fb918ecd26c1448597e00c5f6)。

保留字段（Reserved），应为0。

<a id="r_a3d6cc7e71589d1ade099a823ec052923"></a>

```c
uint8_t nb_eap: 3
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nb_eap](#a3d6cc7e71589d1ade099a823ec052923)。

待处理扩展地址数量子字段（Number of Extended Addresses Pending Subfield）。

<a id="r_a18c098d3dfb15a1902ff90e63041447a"></a>

```c
uint8_t reserved_2: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved_2](#a18c098d3dfb15a1902ff90e63041447a)。

保留字段（Reserved），应为0。

<a id="r_a0429476706f4cbd91082d200963fc71a"></a>

```c
uint8_t nb_sap: 3
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nb_sap](#a0429476706f4cbd91082d200963fc71a)。

待处理短地址数量子字段（Number of Short Addresses Pending Subfield）。

## 38.2\_详细说明（Detailed Documentation）

<a id="a3d6cc7e71589d1ade099a823ec052923"></a>

### `nb_eap`

```c
uint8_t ieee802154_pas_spec::nb_eap
```

待处理扩展地址数量子字段（Number of Extended Addresses Pending Subfield）。

<a id="a0429476706f4cbd91082d200963fc71a"></a>

### `nb_sap`

```c
uint8_t ieee802154_pas_spec::nb_sap
```

待处理短地址数量子字段（Number of Short Addresses Pending Subfield）。

<a id="a607b544fb918ecd26c1448597e00c5f6"></a>

### `reserved_1`

```c
uint8_t ieee802154_pas_spec::reserved_1
```

保留字段（Reserved），应为0。

<a id="a18c098d3dfb15a1902ff90e63041447a"></a>

### `reserved_2`

```c
uint8_t ieee802154_pas_spec::reserved_2
```

保留字段（Reserved），应为0。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_ieee802154_openthread_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_ieee802154_phy_channel_range_结构体.md)
