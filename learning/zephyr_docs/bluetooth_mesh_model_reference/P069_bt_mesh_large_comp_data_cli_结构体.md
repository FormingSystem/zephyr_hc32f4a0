---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-69
title: bt_mesh_large_comp_data_cli_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__large__comp__data__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_bt\_mesh\_large\_comp\_data\_cli\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__large__comp__data__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

大型组成数据客户端（Large Composition Data Client）的模型上下文。

```c
#include <zephyr/bluetooth/mesh/large_comp_data_cli.h>
```

<a id="details"></a>

大型组成数据客户端（Large Composition Data Client）的模型上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_a4401ff19edfe69c018dd0dbb6f81dc0d"></a>

```c
const struct bt_mesh_model * model
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[model](#a4401ff19edfe69c018dd0dbb6f81dc0d)。

模型条目指针（Model entry pointer）。

<a id="r_afec070cb549d56b3900c4df1e14656ed"></a>

```c
struct bt_mesh_msg_ack_ctx ack_ctx
```

相关声明：[bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)、[ack_ctx](#afec070cb549d56b3900c4df1e14656ed)。

用于跟踪消息响应的内部参数（Internal parameters）。

<a id="r_a39d9086c8d9803f939c6103e613699b1"></a>

```c
const struct bt_mesh_large_comp_data_cli_cb * cb
```

相关声明：[bt_mesh_large_comp_data_cli_cb](P070_bt_mesh_large_comp_data_cli_cb_结构体.md)、[cb](#a39d9086c8d9803f939c6103e613699b1)。

大型组成数据状态消息（Large Composition Data Status）的可选回调。

## 69.2\_详细说明（Detailed Documentation）

<a id="afec070cb549d56b3900c4df1e14656ed"></a>

### `ack_ctx`

```c
struct bt_mesh_msg_ack_ctx bt_mesh_large_comp_data_cli::ack_ctx
```

用于跟踪消息响应的内部参数（Internal parameters）。

<a id="a39d9086c8d9803f939c6103e613699b1"></a>

### `cb`

```c
const struct bt_mesh_large_comp_data_cli_cb* bt_mesh_large_comp_data_cli::cb
```

大型组成数据状态消息（Large Composition Data Status）的可选回调。

<a id="a4401ff19edfe69c018dd0dbb6f81dc0d"></a>

### `model`

```c
const struct bt_mesh_model* bt_mesh_large_comp_data_cli::model
```

模型条目指针（Model entry pointer）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/large_comp_data_cli.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/large_comp_data_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__cli_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)
- [bt_mesh_large_comp_data_cli_cb](P070_bt_mesh_large_comp_data_cli_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_bt_mesh_key_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_bt_mesh_large_comp_data_cli_cb_结构体.md)
