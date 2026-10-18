---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-24
title: bt_mesh_cdb_app_key_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cdb__app__key.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_bt\_mesh\_cdb\_app\_key\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cdb__app__key.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/mesh/cdb.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_afa234a0d5f0fb61513a97afb91986976"></a>

```c
uint16_t net_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx](#afa234a0d5f0fb61513a97afb91986976)。

绑定的网络密钥索引（Network key index）。

<a id="r_a2ef7f5d832b36736d3a1811a407b6fa6"></a>

```c
uint16_t app_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[app_idx](#a2ef7f5d832b36736d3a1811a407b6fa6)。

应用密钥索引（Application key index）。

```c
struct {
```

<a id="r_a695de7415ed5e1d1063cbeddddd45319"></a>

```c
struct bt_mesh_key app_key
```

相关声明：[bt_mesh_key](P068_bt_mesh_key_结构体.md)、[app_key](#a2d685a7dd5e1f4678c34ea72be3fe6a2)。

<a id="r_aa113eaa2a648cdabe21dc2c57b31bf65"></a>

```c
} keys [2]
```

相关声明：[keys](#aa113eaa2a648cdabe21dc2c57b31bf65)。

密钥刷新（Key Refresh）所用的旧密钥与新密钥。

## 24.2\_详细说明（Detailed Documentation）

<a id="a2ef7f5d832b36736d3a1811a407b6fa6"></a>

### `app_idx`

```c
uint16_t bt_mesh_cdb_app_key::app_idx
```

应用密钥索引（Application key index）。

<a id="a2d685a7dd5e1f4678c34ea72be3fe6a2"></a>

### `app_key`

```c
struct bt_mesh_key bt_mesh_cdb_app_key::app_key
```

<a id="aa113eaa2a648cdabe21dc2c57b31bf65"></a>

### `[struct]`

```c
struct { ... } bt_mesh_cdb_app_key::keys[2]
```

密钥刷新（Key Refresh）所用的旧密钥与新密钥。

<a id="afa234a0d5f0fb61513a97afb91986976"></a>

### `net_idx`

```c
uint16_t bt_mesh_cdb_app_key::net_idx
```

绑定的网络密钥索引（Network key index）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cdb.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cdb.h](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_key](P068_bt_mesh_key_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_bt_mesh_cdb_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_bt_mesh_cdb_node_结构体.md)
