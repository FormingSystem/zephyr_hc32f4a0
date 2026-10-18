---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-27
title: bt_mesh_cfg_cli_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cfg__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_bt\_mesh\_cfg\_cli\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cfg__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Mesh配置客户端（Configuration Client）的模型上下文。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

Mesh配置客户端（Configuration Client）的模型上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_a525dd5391c83c525c012940575245cea"></a>

```c
const struct bt_mesh_model * model
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[model](#a525dd5391c83c525c012940575245cea)。

组成数据模型条目指针（Composition data model entry pointer）。

<a id="r_a7160cf5d22fa0b909482bbc76f27b6bd"></a>

```c
const struct bt_mesh_cfg_cli_cb * cb
```

相关声明：[bt_mesh_cfg_cli_cb](P028_bt_mesh_cfg_cli_cb_结构体.md)、[cb](#a7160cf5d22fa0b909482bbc76f27b6bd)。

Mesh 配置客户端状态消息（Mesh Configuration Client Status）的可选回调。

<a id="r_a472bf5015857ab97e1a40ab6cfa70bb1"></a>

```c
struct bt_mesh_msg_ack_ctx ack_ctx
```

相关声明：[bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)、[ack_ctx](#a472bf5015857ab97e1a40ab6cfa70bb1)。

## 27.2\_详细说明（Detailed Documentation）

<a id="a472bf5015857ab97e1a40ab6cfa70bb1"></a>

### `ack_ctx`

```c
struct bt_mesh_msg_ack_ctx bt_mesh_cfg_cli::ack_ctx
```

<a id="a7160cf5d22fa0b909482bbc76f27b6bd"></a>

### `cb`

```c
const struct bt_mesh_cfg_cli_cb* bt_mesh_cfg_cli::cb
```

Mesh 配置客户端状态消息（Mesh Configuration Client Status）的可选回调。

<a id="a525dd5391c83c525c012940575245cea"></a>

### `model`

```c
const struct bt_mesh_model* bt_mesh_cfg_cli::model
```

组成数据模型条目指针（Composition data model entry pointer）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_cfg_cli_cb](P028_bt_mesh_cfg_cli_cb_结构体.md)
- [bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_bt_mesh_cdb_subnet_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_bt_mesh_cfg_cli_cb_结构体.md)
