---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-70
title: bt_mesh_large_comp_data_cli_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__large__comp__data__cli__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_bt\_mesh\_large\_comp\_data\_cli\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__large__comp__data__cli__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

大型组成数据状态（Large Composition Data Status）消息的回调。

```c
#include <zephyr/bluetooth/mesh/large_comp_data_cli.h>
```

<a id="details"></a>

大型组成数据状态（Large Composition Data Status）消息的回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

<a id="r_ab0e17df5eb165a44d70542b8edd36ab9"></a>

```c
void(* large_comp_data_status )(struct bt_mesh_large_comp_data_cli *cli, uint16_t addr, struct bt_mesh_large_comp_data_rsp *rsp)
```

相关声明：[large_comp_data_status](#ab0e17df5eb165a44d70542b8edd36ab9)、[bt_mesh_large_comp_data_cli](P069_bt_mesh_large_comp_data_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_large_comp_data_rsp](P071_bt_mesh_large_comp_data_rsp_结构体.md)。

大型组成数据状态消息（Large Composition Data Status）的可选回调。

<a id="r_ade54d137534ffb2274e366140f6cbd3c"></a>

```c
void(* models_metadata_status )(struct bt_mesh_large_comp_data_cli *cli, uint16_t addr, struct bt_mesh_large_comp_data_rsp *rsp)
```

相关声明：[models_metadata_status](#ade54d137534ffb2274e366140f6cbd3c)、[bt_mesh_large_comp_data_cli](P069_bt_mesh_large_comp_data_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_large_comp_data_rsp](P071_bt_mesh_large_comp_data_rsp_结构体.md)。

模型元数据状态消息（Models Metadata Status）的可选回调。

## 70.2\_详细说明（Detailed Documentation）

<a id="ab0e17df5eb165a44d70542b8edd36ab9"></a>

### `large_comp_data_status`

```c
void(* bt_mesh_large_comp_data_cli_cb::large_comp_data_status) (struct bt_mesh_large_comp_data_cli *cli, uint16_t addr, struct bt_mesh_large_comp_data_rsp *rsp)
```

大型组成数据状态消息（Large Composition Data Status）的可选回调。

处理从大型组成数据服务器（Large Composition Data Server）收到的大型组成数据状态消息（Large Composition Data Status）。

如果退出此回调后仍需要 `rsp` 的内容，用户应对其进行深复制（Deep copy）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 大型组成数据客户端上下文（Large Composition Data Client context）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `rsp` | 从服务器收到的响应（Response）。 |

<a id="ade54d137534ffb2274e366140f6cbd3c"></a>

### `models_metadata_status`

```c
void(* bt_mesh_large_comp_data_cli_cb::models_metadata_status) (struct bt_mesh_large_comp_data_cli *cli, uint16_t addr, struct bt_mesh_large_comp_data_rsp *rsp)
```

模型元数据状态消息（Models Metadata Status）的可选回调。

处理从大型组成数据服务器（Large Composition Data Server）收到的模型元数据状态消息（Models Metadata Status）。

如果退出此回调后仍需要 `rsp` 的内容，用户应对其进行深复制（Deep copy）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 大型组成数据客户端上下文（Large Composition Data Client context）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `rsp` | 从服务器收到的响应（Response）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/large_comp_data_cli.h`

## 70.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/large_comp_data_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__cli_8h_source.html)
- [bt_mesh_large_comp_data_cli](P069_bt_mesh_large_comp_data_cli_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_large_comp_data_rsp](P071_bt_mesh_large_comp_data_rsp_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_bt_mesh_large_comp_data_cli_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_bt_mesh_large_comp_data_rsp_结构体.md)
