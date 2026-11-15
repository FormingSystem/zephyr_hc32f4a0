---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-76
title: bt_mesh_model__bt_mesh_model_rt_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model_1_1bt__mesh__model__rt__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_bt\_mesh\_model\_\_bt\_mesh\_model\_rt\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model_1_1bt__mesh__model__rt__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 76.1\_数据成员（Data Fields）

<a id="r_aca9b558516b929a0b88d8171027e7c71"></a>

```c
uint8_t elem_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[elem_idx](#aca9b558516b929a0b88d8171027e7c71)。

<a id="r_a79351fd25ad2ebd1f08ef1748d21dabd"></a>

```c
uint8_t mod_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mod_idx](#a79351fd25ad2ebd1f08ef1748d21dabd)。

<a id="r_ab584da43197ad7afe8c9ae807ce69f7e"></a>

```c
uint16_t flags
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flags](#ab584da43197ad7afe8c9ae807ce69f7e)。

<a id="r_a434ae02cff38c614ef340a3c17f30e9b"></a>

```c
const struct bt_mesh_model * next
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[next](#a434ae02cff38c614ef340a3c17f30e9b)。

<a id="r_a718d3be40e7be83a196634054d18d568"></a>

```c
void * user_data
```

相关声明：[user_data](#a718d3be40e7be83a196634054d18d568)。

模型专用用户数据（Model-specific user data）。

## 76.2\_详细说明（Detailed Documentation）

<a id="aca9b558516b929a0b88d8171027e7c71"></a>

### `elem_idx`

```c
uint8_t bt_mesh_model::bt_mesh_model_rt_ctx::elem_idx
```

<a id="ab584da43197ad7afe8c9ae807ce69f7e"></a>

### `flags`

```c
uint16_t bt_mesh_model::bt_mesh_model_rt_ctx::flags
```

<a id="a79351fd25ad2ebd1f08ef1748d21dabd"></a>

### `mod_idx`

```c
uint8_t bt_mesh_model::bt_mesh_model_rt_ctx::mod_idx
```

<a id="a434ae02cff38c614ef340a3c17f30e9b"></a>

### `next`

```c
const struct bt_mesh_model* bt_mesh_model::bt_mesh_model_rt_ctx::next
```

<a id="a718d3be40e7be83a196634054d18d568"></a>

### `user_data`

```c
void* bt_mesh_model::bt_mesh_model_rt_ctx::user_data
```

模型专用用户数据（Model-specific user data）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 76.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P075_bt_mesh_model_结构体.md) · [返回大纲](大纲.md) · [下一章](P077_bt_mesh_model_cb_结构体.md)
