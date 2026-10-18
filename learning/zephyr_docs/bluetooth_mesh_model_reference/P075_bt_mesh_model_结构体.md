---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-75
title: bt_mesh_model_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_bt\_mesh\_model\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述Mesh模型（Mesh Model）实例的抽象。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

描述Mesh模型（Mesh Model）实例的抽象。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 75.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fmodel_5Frt_5Fctx"></a>

```c
struct bt_mesh_model_rt_ctx
```

相关声明：[bt_mesh_model_rt_ctx](P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 75.2\_数据成员（Data Fields）

```c
union {
```

<a id="r_ab3edb161e4cc94f197bb32326b0a301a"></a>

```c
const uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#a848ccf09f7b75ff8a48acb6c8088cf2a)。

蓝牙技术联盟模型标识符（SIG model ID）。

<a id="r_a13a17e7c024068ad24d48ddd8c5532b7"></a>

```c
const struct bt_mesh_mod_id_vnd vnd
```

相关声明：[bt_mesh_mod_id_vnd](P074_bt_mesh_mod_id_vnd_结构体.md)、[vnd](#a3372deccde1a5ab26d9204c97339596e)。

厂商模型标识（Vendor Model ID）。

<a id="r_abfe9db5b0639ad7566f966ecdafd7082"></a>

```c
};
```

<a id="r_a3980e6f8100151cb3339792821fa7858"></a>

```c
struct bt_mesh_model::bt_mesh_model_rt_ctx rt
```

相关声明：[bt_mesh_model::bt_mesh_model_rt_ctx](P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md)、[rt](#a3980e6f8100151cb3339792821fa7858)。

<a id="r_af4a1b5e837b3a1266c7f61ee21020c0b"></a>

```c
struct bt_mesh_model_pub *const pub
```

相关声明：[bt_mesh_model_pub](P079_bt_mesh_model_pub_结构体.md)、[pub](#af4a1b5e837b3a1266c7f61ee21020c0b)。

模型发布（Model Publication）。

<a id="r_a63595a0559ca70ca76c996f0b71c7983"></a>

```c
uint16_t *const keys
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[keys](#a63595a0559ca70ca76c996f0b71c7983)。

应用密钥列表（AppKey List）。

<a id="r_a79b8fd44ced901c3478f0e04d7dadfcd"></a>

```c
const uint16_t keys_cnt
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[keys_cnt](#a79b8fd44ced901c3478f0e04d7dadfcd)。

<a id="r_a460ab46730afa4f74e4066f787864b0b"></a>

```c
uint16_t *const groups
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[groups](#a460ab46730afa4f74e4066f787864b0b)。

订阅列表（Subscription List），包含组地址或虚拟地址。

<a id="r_adf3e3f0dab9838cc76361949b237bb9e"></a>

```c
const uint16_t groups_cnt
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[groups_cnt](#adf3e3f0dab9838cc76361949b237bb9e)。

<a id="r_a274c811c22b764908599127b128ce584"></a>

```c
const uint8_t **const uuids
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuids](#a274c811c22b764908599127b128ce584)。

模型所订阅的标签通用唯一标识符列表（Label UUIDs）。

<a id="r_a4acc656c737cf79161414984312100b6"></a>

```c
const struct bt_mesh_model_op *const op
```

相关声明：[bt_mesh_model_op](P078_bt_mesh_model_op_结构体.md)、[op](#a4acc656c737cf79161414984312100b6)。

操作码处理函数列表（Opcode handler list）。

<a id="r_a67a91d64051e055b79f5d9166ab12660"></a>

```c
const struct bt_mesh_model_cb *const cb
```

相关声明：[bt_mesh_model_cb](P077_bt_mesh_model_cb_结构体.md)、[cb](#a67a91d64051e055b79f5d9166ab12660)。

模型回调结构（Model callback structure）。

<a id="r_af5b948709773e5388c30d457ec2a9559"></a>

```c
const struct bt_mesh_models_metadata_entry *const metadata
```

相关声明：[bt_mesh_models_metadata_entry](P080_bt_mesh_models_metadata_entry_结构体.md)、[metadata](#af5b948709773e5388c30d457ec2a9559)。

## 75.3\_详细说明（Detailed Documentation）

<a id="abfe9db5b0639ad7566f966ecdafd7082"></a>

### `[union]`

```c
union { ... } bt_mesh_model
```

<a id="a67a91d64051e055b79f5d9166ab12660"></a>

### `cb`

```c
const struct bt_mesh_model_cb* const bt_mesh_model::cb
```

模型回调结构（Model callback structure）。

<a id="a460ab46730afa4f74e4066f787864b0b"></a>

### `groups`

```c
uint16_t* const bt_mesh_model::groups
```

订阅列表（Subscription List），包含组地址或虚拟地址。

<a id="adf3e3f0dab9838cc76361949b237bb9e"></a>

### `groups_cnt`

```c
const uint16_t bt_mesh_model::groups_cnt
```

<a id="a848ccf09f7b75ff8a48acb6c8088cf2a"></a>

### `id`

```c
const uint16_t bt_mesh_model::id
```

蓝牙技术联盟模型标识符（SIG model ID）。

<a id="a63595a0559ca70ca76c996f0b71c7983"></a>

### `keys`

```c
uint16_t* const bt_mesh_model::keys
```

应用密钥列表（AppKey List）。

<a id="a79b8fd44ced901c3478f0e04d7dadfcd"></a>

### `keys_cnt`

```c
const uint16_t bt_mesh_model::keys_cnt
```

<a id="af5b948709773e5388c30d457ec2a9559"></a>

### `metadata`

```c
const struct bt_mesh_models_metadata_entry* const bt_mesh_model::metadata
```

<a id="a4acc656c737cf79161414984312100b6"></a>

### `op`

```c
const struct bt_mesh_model_op* const bt_mesh_model::op
```

操作码处理函数列表（Opcode handler list）。

<a id="af4a1b5e837b3a1266c7f61ee21020c0b"></a>

### `pub`

```c
struct bt_mesh_model_pub* const bt_mesh_model::pub
```

模型发布（Model Publication）。

<a id="a3980e6f8100151cb3339792821fa7858"></a>

### `rt`

```c
struct bt_mesh_model::bt_mesh_model_rt_ctx bt_mesh_model::rt
```

<a id="a274c811c22b764908599127b128ce584"></a>

### `uuids`

```c
const uint8_t** const bt_mesh_model::uuids
```

模型所订阅的标签通用唯一标识符列表（Label UUIDs）。

<a id="a3372deccde1a5ab26d9204c97339596e"></a>

### `vnd`

```c
const struct bt_mesh_mod_id_vnd bt_mesh_model::vnd
```

厂商模型标识（Vendor Model ID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 75.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [bt_mesh_model_rt_ctx](P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_mod_id_vnd](P074_bt_mesh_mod_id_vnd_结构体.md)
- [bt_mesh_model_pub](P079_bt_mesh_model_pub_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_model_op](P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](P077_bt_mesh_model_cb_结构体.md)
- [bt_mesh_models_metadata_entry](P080_bt_mesh_models_metadata_entry_结构体.md)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P074_bt_mesh_mod_id_vnd_结构体.md) · [返回大纲](大纲.md) · [下一章](P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md)
