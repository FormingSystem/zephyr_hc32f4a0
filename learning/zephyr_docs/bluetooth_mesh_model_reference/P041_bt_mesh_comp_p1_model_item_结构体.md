---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-41
title: bt_mesh_comp_p1_model_item_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p1__model__item.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_bt\_mesh\_comp\_p1\_model\_item\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p1__model__item.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

组成数据（Composition Data）第1页的模型项表示。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

组成数据（Composition Data）第1页的模型项表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_aee352e8563133dddbb37c1f31dfe7c09"></a>

```c
bool cor_present
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[cor_present](#aee352e8563133dddbb37c1f31dfe7c09)。

`Corresponding_Group_ID` 字段指示符（Field indicator）。

<a id="r_af2f213813440cb4a87884e3625a704e7"></a>

```c
bool format
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[format](#af2f213813440cb4a87884e3625a704e7)。

决定扩展模型项（Extended Model Item）的格式。

<a id="r_ae019a211eafeb20f323ad97328d938f7"></a>

```c
uint8_t ext_item_cnt: 6
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ext_item_cnt](#ae019a211eafeb20f323ad97328d938f7)。

扩展模型项集合（Extended Model Items）中的条目数量。

<a id="r_a95baa1acf3a82e8559ce4a47b7e03be8"></a>

```c
uint8_t cor_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cor_id](#a95baa1acf3a82e8559ce4a47b7e03be8)。

包含扩展模型项（Extended Model Items）的缓冲区。

## 41.2\_详细说明（Detailed Documentation）

<a id="a95baa1acf3a82e8559ce4a47b7e03be8"></a>

### `cor_id`

```c
uint8_t bt_mesh_comp_p1_model_item::cor_id
```

包含扩展模型项（Extended Model Items）的缓冲区。

若 `cor_present` 设为 `1`，则以 `Corresponding_Group_ID` 开始。

<a id="aee352e8563133dddbb37c1f31dfe7c09"></a>

### `cor_present`

```c
bool bt_mesh_comp_p1_model_item::cor_present
```

`Corresponding_Group_ID` 字段指示符（Field indicator）。

<a id="ae019a211eafeb20f323ad97328d938f7"></a>

### `ext_item_cnt`

```c
uint8_t bt_mesh_comp_p1_model_item::ext_item_cnt
```

扩展模型项集合（Extended Model Items）中的条目数量。

<a id="af2f213813440cb4a87884e3625a704e7"></a>

### `format`

```c
bool bt_mesh_comp_p1_model_item::format
```

决定扩展模型项（Extended Model Item）的格式。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_bt_mesh_comp_p1_item_short_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_bt_mesh_comp_p2_record_结构体.md)
