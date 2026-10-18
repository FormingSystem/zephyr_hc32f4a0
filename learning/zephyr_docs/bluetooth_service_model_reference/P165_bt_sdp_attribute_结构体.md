---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-165
title: bt_sdp_attribute_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attribute.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第165章\_bt\_sdp\_attribute\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attribute.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务发现协议（SDP）的属性值。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

服务发现协议（SDP）的属性值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 165.1\_数据成员（Data Fields）

<a id="r_a1221009053aa7911ea82b3169ea330a1"></a>

```c
uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#a1221009053aa7911ea82b3169ea330a1)。

属性 ID。

<a id="r_a424c2ae038fda8dfd96e2a9cd876f9a1"></a>

```c
struct bt_sdp_data_elem val
```

相关声明：[bt_sdp_data_elem](P169_bt_sdp_data_elem_结构体.md)、[val](#a424c2ae038fda8dfd96e2a9cd876f9a1)。

属性数据（Attribute data）。

## 165.2\_详细说明（Detailed Documentation）

<a id="a1221009053aa7911ea82b3169ea330a1"></a>

### `id`

```c
uint16_t bt_sdp_attribute::id
```

属性 ID。

<a id="a424c2ae038fda8dfd96e2a9cd876f9a1"></a>

### `val`

```c
struct bt_sdp_data_elem bt_sdp_attribute::val
```

属性数据（Attribute data）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 165.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_sdp_data_elem](P169_bt_sdp_data_elem_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P164_bt_sdp_attr_value_url_结构体.md) · [返回大纲](大纲.md) · [下一章](P166_bt_sdp_attribute_id_list_结构体.md)
