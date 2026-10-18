---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-161
title: bt_sdp_attr_value_pair_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value__pair.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第161章\_bt\_sdp\_attr\_value\_pair\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value__pair.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务发现协议（SDP）属性值对的结构。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

SDP 属性值对（attribute value pair）结构体。包含已解析的属性值信息，包括 UUID 标识符、实际值及其类型。此结构体将 UUID 与其相应属性值关联起来，完整表示一个已解析的 SDP 属性元素。注意：回调函数返回后，UUID 指针和值指针均失效。UUID 指针或值指针可能为 `NULL`：UUID 为 `NULL` 表示此值不属于任何 UUID；值为 `NULL` 表示此 UUID 没有对应值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 161.1\_数据成员（Data Fields）

<a id="r_a533ee8ab9d9dec24faf52c2dc016bb1d"></a>

```c
struct bt_uuid * uuid
```

相关声明：[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](#a533ee8ab9d9dec24faf52c2dc016bb1d)。

属性的 UUID 标识符。

<a id="r_a505490ce660a6c15b2b59efaa5fb6057"></a>

```c
struct bt_sdp_attr_value * value
```

相关声明：[bt_sdp_attr_value](P159_bt_sdp_attr_value_结构体.md)、[value](#a505490ce660a6c15b2b59efaa5fb6057)。

指向已解析属性值的指针。

## 161.2\_详细说明（Detailed Documentation）

<a id="a533ee8ab9d9dec24faf52c2dc016bb1d"></a>

### `uuid`

```c
struct bt_uuid* bt_sdp_attr_value_pair::uuid
```

属性的 UUID 标识符。

<a id="a505490ce660a6c15b2b59efaa5fb6057"></a>

### `value`

```c
struct bt_sdp_attr_value* bt_sdp_attr_value_pair::value
```

指向已解析属性值的指针。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 161.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [bt_sdp_attr_value](P159_bt_sdp_attr_value_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P160_bt_sdp_attr_value_int_结构体.md) · [返回大纲](大纲.md) · [下一章](P162_bt_sdp_attr_value_text_结构体.md)
