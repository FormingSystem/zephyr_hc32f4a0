---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-96
title: bt_mesh_sar_cfg_cli_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__sar__cfg__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第96章\_bt\_mesh\_sar\_cfg\_cli\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__sar__cfg__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Mesh分段与重组配置客户端（SAR Configuration Client）的模型上下文。

```c
#include <zephyr/bluetooth/mesh/sar_cfg_cli.h>
```

<a id="details"></a>

Mesh分段与重组配置客户端（SAR Configuration Client）的模型上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 96.1\_数据成员（Data Fields）

<a id="r_a94056c2b7bfc1b495b5bf7e6a5fe3066"></a>

```c
const struct bt_mesh_model * model
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[model](#a94056c2b7bfc1b495b5bf7e6a5fe3066)。

接入层模型指针（Access model pointer）。

<a id="r_a16a6f6c0b0ac8ae80abfb48a5f231418"></a>

```c
struct bt_mesh_model_pub pub
```

相关声明：[bt_mesh_model_pub](P079_bt_mesh_model_pub_结构体.md)、[pub](#a16a6f6c0b0ac8ae80abfb48a5f231418)。

<a id="r_a31fdb2608f2cf80ea17dd1f72e634769"></a>

```c
int32_t timeout
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[timeout](#a31fdb2608f2cf80ea17dd1f72e634769)。

<a id="r_a30889368bd4e87efd39b6c456b3510d8"></a>

```c
struct bt_mesh_msg_ack_ctx ack_ctx
```

相关声明：[bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)、[ack_ctx](#a30889368bd4e87efd39b6c456b3510d8)。

## 96.2\_详细说明（Detailed Documentation）

<a id="a30889368bd4e87efd39b6c456b3510d8"></a>

### `ack_ctx`

```c
struct bt_mesh_msg_ack_ctx bt_mesh_sar_cfg_cli::ack_ctx
```

<a id="a94056c2b7bfc1b495b5bf7e6a5fe3066"></a>

### `model`

```c
const struct bt_mesh_model* bt_mesh_sar_cfg_cli::model
```

接入层模型指针（Access model pointer）。

<a id="a16a6f6c0b0ac8ae80abfb48a5f231418"></a>

### `pub`

```c
struct bt_mesh_model_pub bt_mesh_sar_cfg_cli::pub
```

<a id="a31fdb2608f2cf80ea17dd1f72e634769"></a>

### `timeout`

```c
int32_t bt_mesh_sar_cfg_cli::timeout
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/sar_cfg_cli.h`

## 96.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/sar_cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg__cli_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_model_pub](P079_bt_mesh_model_pub_结构体.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P095_bt_mesh_rpr_unprov_结构体.md) · [返回大纲](大纲.md) · [下一章](P097_bt_mesh_sar_rx_结构体.md)
