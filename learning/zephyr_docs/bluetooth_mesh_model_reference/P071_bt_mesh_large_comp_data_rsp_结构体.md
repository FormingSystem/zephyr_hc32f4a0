---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-71
title: bt_mesh_large_comp_data_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__large__comp__data__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_bt\_mesh\_large\_comp\_data\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__large__comp__data__rsp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

大型组成数据（Large Composition Data）的响应。

```c
#include <zephyr/bluetooth/mesh/large_comp_data_cli.h>
```

<a id="details"></a>

大型组成数据（Large Composition Data）的响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.1\_数据成员（Data Fields）

<a id="r_ad3d781276eaf84fd1a8a4d031c005deb"></a>

```c
uint8_t page
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[page](#ad3d781276eaf84fd1a8a4d031c005deb)。

页编号（Page number）。

<a id="r_a8bba19b3687a67442e91873c228be361"></a>

```c
uint16_t offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[offset](#a8bba19b3687a67442e91873c228be361)。

位于该页内的偏移。

<a id="r_aaab8add82c9f24d68af0ddd279164882"></a>

```c
uint16_t total_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[total_size](#aaab8add82c9f24d68af0ddd279164882)。

页面总大小（Total page size）。

<a id="r_a02d92a210b5b7a26b1df4f5076ed99d8"></a>

```c
struct net_buf_simple * data
```

相关声明：[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[data](#a02d92a210b5b7a26b1df4f5076ed99d8)。

指向已分配缓冲区的指针，用于存储接收到的数据（Received data）。

## 71.2\_详细说明（Detailed Documentation）

<a id="a02d92a210b5b7a26b1df4f5076ed99d8"></a>

### `data`

```c
struct net_buf_simple* bt_mesh_large_comp_data_rsp::data
```

指向已分配缓冲区的指针，用于存储接收到的数据（Received data）。

<a id="a8bba19b3687a67442e91873c228be361"></a>

### `offset`

```c
uint16_t bt_mesh_large_comp_data_rsp::offset
```

位于该页内的偏移。

<a id="ad3d781276eaf84fd1a8a4d031c005deb"></a>

### `page`

```c
uint8_t bt_mesh_large_comp_data_rsp::page
```

页编号（Page number）。

<a id="aaab8add82c9f24d68af0ddd279164882"></a>

### `total_size`

```c
uint16_t bt_mesh_large_comp_data_rsp::total_size
```

页面总大小（Total page size）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/large_comp_data_cli.h`

## 71.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/large_comp_data_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__cli_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_bt_mesh_large_comp_data_cli_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P072_bt_mesh_lpn_cb_结构体.md)
