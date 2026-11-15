---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-26
title: bt_mesh_cdb_subnet_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cdb__subnet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_bt\_mesh\_cdb\_subnet\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cdb__subnet.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/mesh/cdb.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_a1010965e2030e1bef181920fc5f76116"></a>

```c
uint16_t net_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx](#a1010965e2030e1bef181920fc5f76116)。

网络密钥索引（Network key index）。

<a id="r_a07fbd0e52571cd9a16e876243483e98a"></a>

```c
uint8_t kr_phase
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[kr_phase](#a07fbd0e52571cd9a16e876243483e98a)。

密钥刷新阶段（Key Refresh phase）。

```c
struct {
```

<a id="r_ab55f9318dc399b8607b011f2bd26e7b7"></a>

```c
struct bt_mesh_key net_key
```

相关声明：[bt_mesh_key](P068_bt_mesh_key_结构体.md)、[net_key](#a40d47a7705f4d3a9ba9349972d11072a)。

<a id="r_a2f04c34ebbb8ae1e33f6679f94690c9a"></a>

```c
} keys [2]
```

相关声明：[keys](#a2f04c34ebbb8ae1e33f6679f94690c9a)。

密钥刷新（Key Refresh）所用的旧密钥与新密钥。

## 26.2\_详细说明（Detailed Documentation）

<a id="a2f04c34ebbb8ae1e33f6679f94690c9a"></a>

### `[struct]`

```c
struct { ... } bt_mesh_cdb_subnet::keys[2]
```

密钥刷新（Key Refresh）所用的旧密钥与新密钥。

<a id="a07fbd0e52571cd9a16e876243483e98a"></a>

### `kr_phase`

```c
uint8_t bt_mesh_cdb_subnet::kr_phase
```

密钥刷新阶段（Key Refresh phase）。

<a id="a1010965e2030e1bef181920fc5f76116"></a>

### `net_idx`

```c
uint16_t bt_mesh_cdb_subnet::net_idx
```

网络密钥索引（Network key index）。

<a id="a40d47a7705f4d3a9ba9349972d11072a"></a>

### `net_key`

```c
struct bt_mesh_key bt_mesh_cdb_subnet::net_key
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cdb.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cdb.h](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_key](P068_bt_mesh_key_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_bt_mesh_cdb_node_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_bt_mesh_cfg_cli_结构体.md)
