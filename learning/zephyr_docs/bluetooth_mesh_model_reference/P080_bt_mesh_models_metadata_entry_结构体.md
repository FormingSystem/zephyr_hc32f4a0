---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-80
title: bt_mesh_models_metadata_entry_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__models__metadata__entry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_bt\_mesh\_models\_metadata\_entry\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__models__metadata__entry.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模型元数据条目（Models Metadata Entry）的结构。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

模型元数据条目结构（Models Metadata Entry struct）。主要应使用 `BT_MESH_MODELS_METADATA_ENTRY` 宏创建此结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 80.1\_数据成员（Data Fields）

<a id="r_a39959b1f46e1b21eb78dbe3293f29149"></a>

```c
const uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#a39959b1f46e1b21eb78dbe3293f29149)。

元数据长度。

<a id="r_ae343d6ca709e1aceafc25d64cdf3916d"></a>

```c
const uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#ae343d6ca709e1aceafc25d64cdf3916d)。

元数据标识符（Metadata ID）。

<a id="r_adb5aaf010cae636c0b60a88f38d36fac"></a>

```c
const void *const data
```

相关声明：[data](#adb5aaf010cae636c0b60a88f38d36fac)。

指向原始数据（Raw data）的指针。

## 80.2\_详细说明（Detailed Documentation）

<a id="adb5aaf010cae636c0b60a88f38d36fac"></a>

### `data`

```c
const void* const bt_mesh_models_metadata_entry::data
```

指向原始数据（Raw data）的指针。

<a id="ae343d6ca709e1aceafc25d64cdf3916d"></a>

### `id`

```c
const uint16_t bt_mesh_models_metadata_entry::id
```

元数据标识符（Metadata ID）。

<a id="a39959b1f46e1b21eb78dbe3293f29149"></a>

### `len`

```c
const uint16_t bt_mesh_models_metadata_entry::len
```

元数据长度。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 80.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P079_bt_mesh_model_pub_结构体.md) · [返回大纲](大纲.md) · [下一章](P081_bt_mesh_msg_ack_ctx_结构体.md)
