---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-21
title: bt_mesh_brg_cfg_table_list_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__table__list.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_bt\_mesh\_brg\_cfg\_table\_list\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__table__list.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

桥接表列表（Bridging Table List）的响应。

```c
#include <zephyr/bluetooth/mesh/brg_cfg.h>
```

<a id="details"></a>

桥接表列表（Bridging Table List）的响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_a6ac8abf7a95eda792065171e71f699b2"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a6ac8abf7a95eda792065171e71f699b2)。

请求消息的状态码（Status Code）。

<a id="r_a68cfc1c6514f3b7f6eb0d7ad98a15e96"></a>

```c
uint16_t net_idx1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx1](#a68cfc1c6514f3b7f6eb0d7ad98a15e96)。

第一个子网的网络密钥索引（NetKey Index）。

<a id="r_a091f7458fb6fcd6423c944cc1ebfe0a0"></a>

```c
uint16_t net_idx2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx2](#a091f7458fb6fcd6423c944cc1ebfe0a0)。

第二个子网的网络密钥索引（NetKey Index）。

<a id="r_a7c8ebdfc898826d95ec94b34ec3c0945"></a>

```c
uint16_t start_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[start_idx](#a7c8ebdfc898826d95ec94b34ec3c0945)。

起始偏移量（Start offset），以桥接表状态条目（Bridging table state entries）为单位。

<a id="r_a44ce11d9a2cbda69b605fab6ed68cc56"></a>

```c
struct net_buf_simple * list
```

相关声明：[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[list](#a44ce11d9a2cbda69b605fab6ed68cc56)。

指向已分配缓冲区的指针，用于存储已桥接地址和方向的列表（List of bridged addresses and directions）。

## 21.2\_详细说明（Detailed Documentation）

<a id="a44ce11d9a2cbda69b605fab6ed68cc56"></a>

### `list`

```c
struct net_buf_simple* bt_mesh_brg_cfg_table_list::list
```

指向已分配缓冲区的指针，用于存储已桥接地址和方向的列表（List of bridged addresses and directions）。

<a id="a68cfc1c6514f3b7f6eb0d7ad98a15e96"></a>

### `net_idx1`

```c
uint16_t bt_mesh_brg_cfg_table_list::net_idx1
```

第一个子网的网络密钥索引（NetKey Index）。

<a id="a091f7458fb6fcd6423c944cc1ebfe0a0"></a>

### `net_idx2`

```c
uint16_t bt_mesh_brg_cfg_table_list::net_idx2
```

第二个子网的网络密钥索引（NetKey Index）。

<a id="a7c8ebdfc898826d95ec94b34ec3c0945"></a>

### `start_idx`

```c
uint16_t bt_mesh_brg_cfg_table_list::start_idx
```

起始偏移量（Start offset），以桥接表状态条目（Bridging table state entries）为单位。

<a id="a6ac8abf7a95eda792065171e71f699b2"></a>

### `status`

```c
uint8_t bt_mesh_brg_cfg_table_list::status
```

请求消息的状态码（Status Code）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/brg_cfg.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/brg_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_bt_mesh_brg_cfg_table_entry_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_bt_mesh_brg_cfg_table_status_结构体.md)
