---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-77
title: bt_mesh_model_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_bt\_mesh\_model\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模型（Model）的回调函数。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

模型（Model）的回调函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 77.1\_数据成员（Data Fields）

<a id="r_a21fc24829c6933a035b0f0be1a1f58e5"></a>

```c
int(*const settings_set )(const struct bt_mesh_model *model, const char *name, size_t len_rd, settings_read_cb read_cb, void *cb_arg)
```

相关声明：[settings_set](#a21fc24829c6933a035b0f0be1a1f58e5)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[settings_read_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga51cdac276c1fb8cd27fc3eec42749a04)。

与模型绑定的用户数据的值设置处理函数（Set value handler）。

<a id="r_a8333420fb9d1d98799ae03ba3b23bfe4"></a>

```c
int(*const start )(const struct bt_mesh_model *model)
```

相关声明：[start](#a8333420fb9d1d98799ae03ba3b23bfe4)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)。

Mesh 启动时调用的回调（Callback）。

<a id="r_a1688a2c6d7b3b17ba49a0975b6f4f68e"></a>

```c
int(*const init )(const struct bt_mesh_model *model)
```

相关声明：[init](#a1688a2c6d7b3b17ba49a0975b6f4f68e)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)。

模型初始化回调（Model init callback）。

<a id="r_a3a7ad466120085c55bcffacb15c78518"></a>

```c
void(*const reset )(const struct bt_mesh_model *model)
```

相关声明：[reset](#a3a7ad466120085c55bcffacb15c78518)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)。

模型重置回调（Model reset callback）。

<a id="r_ae28f875dffc7f5f2ce99abe590369f43"></a>

```c
void(*const pending_store )(const struct bt_mesh_model *model)
```

相关声明：[pending_store](#ae28f875dffc7f5f2ce99abe590369f43)、[bt_mesh_model](P075_bt_mesh_model_结构体.md)。

用于存储模型待保存用户数据的回调（Pending model user data callback）。

## 77.2\_详细说明（Detailed Documentation）

<a id="a1688a2c6d7b3b17ba49a0975b6f4f68e"></a>

### `init`

```c
int(*const bt_mesh_model_cb::init) (const struct bt_mesh_model *model)
```

模型初始化回调（Model init callback）。

Mesh 初始化期间，对每个模型实例（Model instance）调用。

如果任何模型初始化回调（Model init callback）返回错误，Mesh 子系统初始化将中止，并将错误返回给 `bt_mesh_init` 的调用者。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 要初始化的模型（Model）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回错误。

<a id="ae28f875dffc7f5f2ce99abe590369f43"></a>

### `pending_store`

```c
void(*const bt_mesh_model_cb::pending_store) (const struct bt_mesh_model *model)
```

用于存储模型待保存用户数据的回调（Pending model user data callback）。

由 `bt_mesh_model_data_store_schedule` 触发。

调用 `bt_mesh_model_data_store` 存储用户数据（User data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 此回调所属的模型（Model）。 |

<a id="a3a7ad466120085c55bcffacb15c78518"></a>

### `reset`

```c
void(*const bt_mesh_model_cb::reset) (const struct bt_mesh_model *model)
```

模型重置回调（Model reset callback）。

Mesh 节点重置（Reset）时调用。重置会删除所有模型数据，模型应清除自身状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 此回调所属的模型（Model）。 |

**说明（Note）**：注意（Note）：如果模型存储了任何持久化数据（Persistent data），必须手动擦除。

<a id="a21fc24829c6933a035b0f0be1a1f58e5"></a>

### `settings_set`

```c
int(*const bt_mesh_model_cb::settings_set) (const struct bt_mesh_model *model, const char *name, size_t len_rd, settings_read_cb read_cb, void *cb_arg)
```

与模型绑定的用户数据的值设置处理函数（Set value handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 要设置其持久化数据（Persistent data）的模型（Model）。 |
| `name` | 设置项的名称／键（Name/key of settings item）。 |
| `len_rd` | 后端（Backend）中所找到数据的大小。 |
| `read_cb` | 用于从后端（Backend）读取数据的函数。 |
| `cb_arg` | 后端（Backend）提供给读取函数的参数。 |

**参阅（See Also）**：另见（See also）：`settings_handler::h_set`。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回错误。

<a id="a8333420fb9d1d98799ae03ba3b23bfe4"></a>

### `start`

```c
int(*const bt_mesh_model_cb::start) (const struct bt_mesh_model *model)
```

Mesh 启动时调用的回调（Callback）。

节点完成配网（Provisioning）后，或所有 Mesh 数据已从持久化存储（Persistent storage）载入后，调用此处理函数。

触发此回调时，Mesh 模型可以开始运行其行为，所有接入层 API（Access APIs）均已可用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `model` | 此回调所属的模型（Model）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回错误。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 77.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [settings_read_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga51cdac276c1fb8cd27fc3eec42749a04)
- [bt_mesh_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga521def6f74467a9bd3f2757c6aabd405)
- [bt_mesh_model_data_store_schedule](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga762896dd2e806b5be061b220d53ce4db)
- [bt_mesh_model_data_store](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gadff0895c5c34928d778fa615512b3d85)
- [settings_handler::h_set](https://docs.zephyrproject.org/latest/doxygen/html/structsettings__handler.html#a70aa25bf3b53898ab22906e9949963a4)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P076_bt_mesh_model__bt_mesh_model_rt_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P078_bt_mesh_model_op_结构体.md)
