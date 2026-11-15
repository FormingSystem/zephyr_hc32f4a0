---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-22
title: bt_mesh_brg_cfg_table_status_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__table__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_bt\_mesh\_brg\_cfg\_table\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__table__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

桥接表状态（Bridging Table Status）的响应。

```c
#include <zephyr/bluetooth/mesh/brg_cfg.h>
```

<a id="details"></a>

桥接表状态（Bridging Table Status）的响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_a6f1ad52ec00ec819064edf503f74744a"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a6f1ad52ec00ec819064edf503f74744a)。

请求消息的状态码（Status Code）。

<a id="r_ae469e4759604077773b45b8ee1f28c37"></a>

```c
struct bt_mesh_brg_cfg_table_entry entry
```

相关声明：[bt_mesh_brg_cfg_table_entry](P020_bt_mesh_brg_cfg_table_entry_结构体.md)、[entry](#ae469e4759604077773b45b8ee1f28c37)。

请求的桥接表条目（Bridging Table entry）。

## 22.2\_详细说明（Detailed Documentation）

<a id="ae469e4759604077773b45b8ee1f28c37"></a>

### `entry`

```c
struct bt_mesh_brg_cfg_table_entry bt_mesh_brg_cfg_table_status::entry
```

请求的桥接表条目（Bridging Table entry）。

<a id="a6f1ad52ec00ec819064edf503f74744a"></a>

### `status`

```c
uint8_t bt_mesh_brg_cfg_table_status::status
```

请求消息的状态码（Status Code）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/brg_cfg.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/brg_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_brg_cfg_table_entry](P020_bt_mesh_brg_cfg_table_entry_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_bt_mesh_brg_cfg_table_list_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_bt_mesh_cdb_结构体.md)
