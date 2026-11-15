---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-59
title: bt_mesh_elem_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__elem.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_bt\_mesh\_elem\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__elem.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述Mesh元素（Mesh Element）的抽象。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

描述Mesh元素（Mesh Element）的抽象。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 59.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Felem_5Frt_5Fctx"></a>

```c
struct bt_mesh_elem_rt_ctx
```

相关声明：[bt_mesh_elem_rt_ctx](P060_bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体.md)。

Mesh元素（Mesh Element）的运行时信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.2\_数据成员（Data Fields）

<a id="r_a2090fa7827eb6a7b8bd1adfb831439cb"></a>

```c
struct bt_mesh_elem::bt_mesh_elem_rt_ctx rt
```

相关声明：[bt_mesh_elem::bt_mesh_elem_rt_ctx](P060_bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体.md)、[rt](#a2090fa7827eb6a7b8bd1adfb831439cb)。

<a id="r_a5f4c8ded34cf56c7f60189584e8e5b46"></a>

```c
const uint16_t loc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[loc](#a5f4c8ded34cf56c7f60189584e8e5b46)。

位置描述符（Location Descriptor），参见 GATT 蓝牙命名空间描述符（Bluetooth Namespace Descriptors）。

<a id="r_a648273e844ff9fa71578372e764ca8cf"></a>

```c
const uint8_t model_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[model_count](#a648273e844ff9fa71578372e764ca8cf)。

此元素中的蓝牙技术联盟模型数量（SIG models）。

<a id="r_aea56fd98c9aecfb9de3772ad3f14b25e"></a>

```c
const uint8_t vnd_model_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[vnd_model_count](#aea56fd98c9aecfb9de3772ad3f14b25e)。

此元素中的厂商模型数量（Vendor models）。

<a id="r_a57fefe57d9425d6666495d1f72a3f132"></a>

```c
const struct bt_mesh_model *const models
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[models](#a57fefe57d9425d6666495d1f72a3f132)。

此元素中的蓝牙技术联盟模型列表（SIG models）。

<a id="r_a81d4fc1c41e2944bf7f6e71b00e19a0f"></a>

```c
const struct bt_mesh_model *const vnd_models
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[vnd_models](#a81d4fc1c41e2944bf7f6e71b00e19a0f)。

此元素中的厂商模型列表（Vendor models）。

## 59.3\_详细说明（Detailed Documentation）

<a id="a5f4c8ded34cf56c7f60189584e8e5b46"></a>

### `loc`

```c
const uint16_t bt_mesh_elem::loc
```

位置描述符（Location Descriptor），参见 GATT 蓝牙命名空间描述符（Bluetooth Namespace Descriptors）。

<a id="a648273e844ff9fa71578372e764ca8cf"></a>

### `model_count`

```c
const uint8_t bt_mesh_elem::model_count
```

此元素中的蓝牙技术联盟模型数量（SIG models）。

<a id="a57fefe57d9425d6666495d1f72a3f132"></a>

### `models`

```c
const struct bt_mesh_model* const bt_mesh_elem::models
```

此元素中的蓝牙技术联盟模型列表（SIG models）。

<a id="a2090fa7827eb6a7b8bd1adfb831439cb"></a>

### `rt`

```c
struct bt_mesh_elem::bt_mesh_elem_rt_ctx bt_mesh_elem::rt
```

<a id="aea56fd98c9aecfb9de3772ad3f14b25e"></a>

### `vnd_model_count`

```c
const uint8_t bt_mesh_elem::vnd_model_count
```

此元素中的厂商模型数量（Vendor models）。

<a id="a81d4fc1c41e2944bf7f6e71b00e19a0f"></a>

### `vnd_models`

```c
const struct bt_mesh_model* const bt_mesh_elem::vnd_models
```

此元素中的厂商模型列表（Vendor models）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 59.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [bt_mesh_elem_rt_ctx](P060_bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_bt_mesh_dfu_target_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体.md)
