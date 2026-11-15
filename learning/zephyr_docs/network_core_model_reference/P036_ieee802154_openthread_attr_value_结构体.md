---
id: learning.zephyr-docs.network-core-model-reference.page-36
title: ieee802154_openthread_attr_value_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__openthread__attr__value.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_ieee802154\_openthread\_attr\_value\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__openthread__attr__value.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ieee802154驱动中OpenThread专用的属性值数据。

```c
#include <zephyr/net/ieee802154_radio_openthread.h>
```

<a id="details"></a>

ieee802154驱动中OpenThread专用的属性值数据（Attribute Value Data）。此类型扩展ieee802154_attr_value。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a384442fee79330fd778f4c5891c41e0a"></a>

```c
struct ieee802154_attr_value common
```

相关声明：[ieee802154_attr_value](P005_ieee802154_attr_value_结构体.md)、[common](#a794c867bf25cd23b9b1797d995696c8a)。

通用属性值（Common Attribute Value）。

<a id="r_af2394207e27a551104ed45068a67b9e6"></a>

```c
uint16_t t_recca
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_recca](#a84f1a03b847ff2050f38a59573a00cd8)。

IEEE802154_OPENTHREAD_ATTR_T_RECCA的属性值。

<a id="r_a826a4ee8681e6c08cc16bd06feef8869"></a>

```c
uint16_t t_ccatx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ccatx](#a423bc2cc48ceead6a6febd7f78504843)。

IEEE802154_OPENTHREAD_ATTR_T_CCATX的属性值。

<a id="r_ab5416f1746e6758118f41db80a5a6392"></a>

```c
};
```

## 36.2\_详细说明（Detailed Documentation）

<a id="ab5416f1746e6758118f41db80a5a6392"></a>

### `[union]`

```c
union { ... } ieee802154_openthread_attr_value
```

<a id="a794c867bf25cd23b9b1797d995696c8a"></a>

### `common`

```c
struct ieee802154_attr_value ieee802154_openthread_attr_value::common
```

通用属性值（Common Attribute Value）。

<a id="a423bc2cc48ceead6a6febd7f78504843"></a>

### `t_ccatx`

```c
uint16_t ieee802154_openthread_attr_value::t_ccatx
```

IEEE802154_OPENTHREAD_ATTR_T_CCATX的属性值。

<a id="a84f1a03b847ff2050f38a59573a00cd8"></a>

### `t_recca`

```c
uint16_t ieee802154_openthread_attr_value::t_recca
```

IEEE802154_OPENTHREAD_ATTR_T_RECCA的属性值。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_radio_openthread.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_radio_openthread.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h_source.html)
- [ieee802154_attr_value](P005_ieee802154_attr_value_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [IEEE802154_OPENTHREAD_ATTR_T_RECCA](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5)
- [IEEE802154_OPENTHREAD_ATTR_T_CCATX](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b)
- [ieee802154_openthread_attr_value](P036_ieee802154_openthread_attr_value_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_ieee802154_mpdu_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_ieee802154_openthread_config_结构体.md)
