---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-20
title: bt_mesh_brg_cfg_table_entry_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__table__entry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_bt\_mesh\_brg\_cfg\_table\_entry\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__table__entry.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

桥接表（Bridging Table）中某个条目对应的桥接表状态条目。

```c
#include <zephyr/bluetooth/mesh/brg_cfg.h>
```

<a id="details"></a>

桥接表（Bridging Table）中某个条目对应的桥接表状态条目。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_a8ce83ebdec5f306382881ceba71918cf"></a>

```c
uint8_t directions
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[directions](#a8ce83ebdec5f306382881ceba71918cf)。

允许的桥接流量方向（Directions for bridged traffic），或表示不允许桥接流量。

<a id="r_acd096d1ddcf598f533c5b2b2a64c22af"></a>

```c
uint16_t net_idx1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx1](#acd096d1ddcf598f533c5b2b2a64c22af)。

第一个子网的网络密钥索引（NetKey Index）。

<a id="r_a672407976b409e44d06875f22f6891d3"></a>

```c
uint16_t net_idx2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx2](#a672407976b409e44d06875f22f6891d3)。

第二个子网的网络密钥索引（NetKey Index）。

<a id="r_aa1150034663bb584779e88a5bed3fc8c"></a>

```c
uint16_t addr1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr1](#aa1150034663bb584779e88a5bed3fc8c)。

第一个子网中的节点地址（Node address）。

<a id="r_a9262e4a78ca69846d3ac7e4f38d17d0d"></a>

```c
uint16_t addr2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr2](#a9262e4a78ca69846d3ac7e4f38d17d0d)。

第二个子网中的节点地址（Node address）。

## 20.2\_详细说明（Detailed Documentation）

<a id="aa1150034663bb584779e88a5bed3fc8c"></a>

### `addr1`

```c
uint16_t bt_mesh_brg_cfg_table_entry::addr1
```

第一个子网中的节点地址（Node address）。

<a id="a9262e4a78ca69846d3ac7e4f38d17d0d"></a>

### `addr2`

```c
uint16_t bt_mesh_brg_cfg_table_entry::addr2
```

第二个子网中的节点地址（Node address）。

<a id="a8ce83ebdec5f306382881ceba71918cf"></a>

### `directions`

```c
uint8_t bt_mesh_brg_cfg_table_entry::directions
```

允许的桥接流量方向（Directions for bridged traffic），或表示不允许桥接流量。

<a id="acd096d1ddcf598f533c5b2b2a64c22af"></a>

### `net_idx1`

```c
uint16_t bt_mesh_brg_cfg_table_entry::net_idx1
```

第一个子网的网络密钥索引（NetKey Index）。

<a id="a672407976b409e44d06875f22f6891d3"></a>

### `net_idx2`

```c
uint16_t bt_mesh_brg_cfg_table_entry::net_idx2
```

第二个子网的网络密钥索引（NetKey Index）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/brg_cfg.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/brg_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_bt_mesh_brg_cfg_subnets_list_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_bt_mesh_brg_cfg_table_list_结构体.md)
