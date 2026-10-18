---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-19
title: bt_mesh_brg_cfg_subnets_list_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__subnets__list.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_bt\_mesh\_brg\_cfg\_subnets\_list\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__subnets__list.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已桥接子网列表（Bridged Subnets List）的响应。

```c
#include <zephyr/bluetooth/mesh/brg_cfg.h>
```

<a id="details"></a>

已桥接子网列表（Bridged Subnets List）的响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_aa0ccb8e8b74365dfc7a4e2f5f38c50c6"></a>

```c
struct bt_mesh_brg_cfg_filter_netkey net_idx_filter
```

相关声明：[bt_mesh_brg_cfg_filter_netkey](P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)、[net_idx_filter](#aa0ccb8e8b74365dfc7a4e2f5f38c50c6)。

对网络密钥索引（NetKey Indexes）应用的过滤条件，以及用于过滤的网络密钥索引（NetKey Index）。

<a id="r_a9f4cb39c12130ebba6c9d275a4a6b310"></a>

```c
uint8_t start_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[start_idx](#a9f4cb39c12130ebba6c9d275a4a6b310)。

起始偏移量（Start offset），以桥接项（Bridges）为单位。

<a id="r_a00ebe6255aabcd1cab49f08e4dc7e21b"></a>

```c
struct net_buf_simple * list
```

相关声明：[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[list](#a00ebe6255aabcd1cab49f08e4dc7e21b)。

指向已分配缓冲区的指针，用于存储过滤后的网络密钥索引（NetKey Indexes）。

## 19.2\_详细说明（Detailed Documentation）

<a id="a00ebe6255aabcd1cab49f08e4dc7e21b"></a>

### `list`

```c
struct net_buf_simple* bt_mesh_brg_cfg_subnets_list::list
```

指向已分配缓冲区的指针，用于存储过滤后的网络密钥索引（NetKey Indexes）。

<a id="aa0ccb8e8b74365dfc7a4e2f5f38c50c6"></a>

### `net_idx_filter`

```c
struct bt_mesh_brg_cfg_filter_netkey bt_mesh_brg_cfg_subnets_list::net_idx_filter
```

对网络密钥索引（NetKey Indexes）应用的过滤条件，以及用于过滤的网络密钥索引（NetKey Index）。

<a id="a9f4cb39c12130ebba6c9d275a4a6b310"></a>

### `start_idx`

```c
uint8_t bt_mesh_brg_cfg_subnets_list::start_idx
```

起始偏移量（Start offset），以桥接项（Bridges）为单位。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/brg_cfg.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/brg_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h_source.html)
- [bt_mesh_brg_cfg_filter_netkey](P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_bt_mesh_brg_cfg_filter_netkey_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_bt_mesh_brg_cfg_table_entry_结构体.md)
