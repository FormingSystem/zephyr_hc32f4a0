---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-16
title: bt_mesh_brg_cfg_cli_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_bt\_mesh\_brg\_cfg\_cli\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

桥接配置客户端（Bridge Configuration Client）的模型上下文。

```c
#include <zephyr/bluetooth/mesh/brg_cfg_cli.h>
```

<a id="details"></a>

桥接配置客户端（Bridge Configuration Client）的模型上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_a6cbc5bb1a79c9951b4cd2f16e06d1beb"></a>

```c
const struct bt_mesh_model * model
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[model](#a6cbc5bb1a79c9951b4cd2f16e06d1beb)。

桥接配置模型条目指针（Bridge Configuration model entry pointer）。

<a id="r_a5a7b181b3d026de617085efc0c671474"></a>

```c
const struct bt_mesh_brg_cfg_cli_cb * cb
```

相关声明：[bt_mesh_brg_cfg_cli_cb](P017_bt_mesh_brg_cfg_cli_cb_结构体.md)、[cb](#a5a7b181b3d026de617085efc0c671474)。

事件处理回调（Event handler callbacks）。

<a id="r_ac0f982fa211bb6660a3159f7e796abb7"></a>

```c
struct bt_mesh_msg_ack_ctx ack_ctx
```

相关声明：[bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)、[ack_ctx](#ac0f982fa211bb6660a3159f7e796abb7)。

## 16.2\_详细说明（Detailed Documentation）

<a id="ac0f982fa211bb6660a3159f7e796abb7"></a>

### `ack_ctx`

```c
struct bt_mesh_msg_ack_ctx bt_mesh_brg_cfg_cli::ack_ctx
```

<a id="a5a7b181b3d026de617085efc0c671474"></a>

### `cb`

```c
const struct bt_mesh_brg_cfg_cli_cb* bt_mesh_brg_cfg_cli::cb
```

事件处理回调（Event handler callbacks）。

<a id="a6cbc5bb1a79c9951b4cd2f16e06d1beb"></a>

### `model`

```c
const struct bt_mesh_model* bt_mesh_brg_cfg_cli::model
```

桥接配置模型条目指针（Bridge Configuration model entry pointer）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/brg_cfg_cli.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/brg_cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__cli_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_brg_cfg_cli_cb](P017_bt_mesh_brg_cfg_cli_cb_结构体.md)
- [bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_bt_mesh_blob_xfer_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_bt_mesh_brg_cfg_cli_cb_结构体.md)
