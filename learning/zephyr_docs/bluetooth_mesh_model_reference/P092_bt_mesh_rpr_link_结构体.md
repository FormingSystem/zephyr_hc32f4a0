---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-92
title: bt_mesh_rpr_link_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__link.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第92章\_bt\_mesh\_rpr\_link\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__link.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

远程配网链路（Remote Provisioning Link）的状态。

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

<a id="details"></a>

远程配网链路（Remote Provisioning Link）的状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 92.1\_数据成员（Data Fields）

<a id="r_a03387a0134a1364c0c2420064960eb03"></a>

```c
enum bt_mesh_rpr_status status
```

相关声明：[bt_mesh_rpr_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga77d2f7158e7629dc54acafbf65e6af90)、[status](#a03387a0134a1364c0c2420064960eb03)。

链路状态（Link status）。

<a id="r_ade33cee01b4f4d2a3a82ed868895c173"></a>

```c
enum bt_mesh_rpr_link_state state
```

相关声明：[bt_mesh_rpr_link_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga0266611238d10f8e97f2b07156991f43)、[state](#ade33cee01b4f4d2a3a82ed868895c173)。

链路状态（Link State）。

## 92.2\_详细说明（Detailed Documentation）

<a id="ade33cee01b4f4d2a3a82ed868895c173"></a>

### `state`

```c
enum bt_mesh_rpr_link_state bt_mesh_rpr_link::state
```

链路状态（Link State）。

<a id="a03387a0134a1364c0c2420064960eb03"></a>

### `status`

```c
enum bt_mesh_rpr_status bt_mesh_rpr_link::status
```

链路状态（Link status）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/rpr.h`

## 92.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/rpr.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr_8h_source.html)
- [bt_mesh_rpr_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga77d2f7158e7629dc54acafbf65e6af90)
- [bt_mesh_rpr_link_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga0266611238d10f8e97f2b07156991f43)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P091_bt_mesh_rpr_cli_结构体.md) · [返回大纲](大纲.md) · [下一章](P093_bt_mesh_rpr_node_结构体.md)
