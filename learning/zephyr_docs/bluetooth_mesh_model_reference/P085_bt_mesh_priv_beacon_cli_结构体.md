---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-85
title: bt_mesh_priv_beacon_cli_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__priv__beacon__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_bt\_mesh\_priv\_beacon\_cli\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__priv__beacon__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Mesh私有信标客户端（Private Beacon Client）模型。

```c
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
```

<a id="details"></a>

Mesh私有信标客户端（Private Beacon Client）模型。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 85.1\_数据成员（Data Fields）

<a id="r_a506b13407e466908d8a8684386bf3927"></a>

```c
const struct bt_mesh_model * model
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[model](#a506b13407e466908d8a8684386bf3927)。

<a id="r_aa4105b00e2a3ad9027b888f0ebbea23e"></a>

```c
struct bt_mesh_msg_ack_ctx ack_ctx
```

相关声明：[bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)、[ack_ctx](#aa4105b00e2a3ad9027b888f0ebbea23e)。

<a id="r_ab281b9ac10c54068372f90bccfe07feb"></a>

```c
const struct bt_mesh_priv_beacon_cli_cb * cb
```

相关声明：[bt_mesh_priv_beacon_cli_cb](P086_bt_mesh_priv_beacon_cli_cb_结构体.md)、[cb](#ab281b9ac10c54068372f90bccfe07feb)。

私有信标客户端状态消息（Private Beacon Client Status）的可选回调。

## 85.2\_详细说明（Detailed Documentation）

<a id="aa4105b00e2a3ad9027b888f0ebbea23e"></a>

### `ack_ctx`

```c
struct bt_mesh_msg_ack_ctx bt_mesh_priv_beacon_cli::ack_ctx
```

<a id="ab281b9ac10c54068372f90bccfe07feb"></a>

### `cb`

```c
const struct bt_mesh_priv_beacon_cli_cb* bt_mesh_priv_beacon_cli::cb
```

私有信标客户端状态消息（Private Beacon Client Status）的可选回调。

<a id="a506b13407e466908d8a8684386bf3927"></a>

### `model`

```c
const struct bt_mesh_model* bt_mesh_priv_beacon_cli::model
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/priv_beacon_cli.h`

## 85.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/priv_beacon_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)
- [bt_mesh_priv_beacon_cli_cb](P086_bt_mesh_priv_beacon_cli_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P084_bt_mesh_priv_beacon_结构体.md) · [返回大纲](大纲.md) · [下一章](P086_bt_mesh_priv_beacon_cli_cb_结构体.md)
