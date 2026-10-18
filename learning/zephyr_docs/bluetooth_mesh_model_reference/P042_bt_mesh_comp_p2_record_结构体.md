---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-42
title: bt_mesh_comp_p2_record_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p2__record.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_bt\_mesh\_comp\_p2\_record\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p2__record.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

组成数据（Composition Data）第2页记录的解析结构。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

组成数据（Composition Data）第2页记录的解析结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_a4d947193b1a0f46c9df1eca298135646"></a>

```c
uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#a4d947193b1a0f46c9df1eca298135646)。

Mesh 规范标识符（Mesh profile ID）。

```c
struct {
```

<a id="r_af297b4ff9f81cf5d40f0993536ff1686"></a>

```c
uint8_t x
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[x](#a5377ce835db8ce408d8dabfd87c858f5)。

主版本（Major version）。

<a id="r_a083d5e91c4e78649f90e413888049149"></a>

```c
uint8_t y
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[y](#a0ceff9becd0eb14ca190c49f56ec0957)。

次版本（Minor version）。

<a id="r_a0756a7cac85f44e1f3a1b78e721ce436"></a>

```c
uint8_t z
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[z](#a90e80906ef6d2b8b932215ad183db2d5)。

Z 版本（Z version）。

<a id="r_aa718c024d6ce339ac8c352319b878c53"></a>

```c
} version
```

相关声明：[version](#aa718c024d6ce339ac8c352319b878c53)。

Mesh 规范版本（Mesh Profile Version）。

<a id="r_ad310f8c8e3a167492a6e698336b7f400"></a>

```c
struct net_buf_simple * elem_buf
```

相关声明：[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[elem_buf](#ad310f8c8e3a167492a6e698336b7f400)。

元素偏移缓冲区（Element offset buffer）。

<a id="r_abd0975a47c848265ad13044dfcd3b78d"></a>

```c
struct net_buf_simple * data_buf
```

相关声明：[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[data_buf](#abd0975a47c848265ad13044dfcd3b78d)。

附加数据缓冲区（Additional data buffer）。

## 42.2\_详细说明（Detailed Documentation）

<a id="abd0975a47c848265ad13044dfcd3b78d"></a>

### `data_buf`

```c
struct net_buf_simple* bt_mesh_comp_p2_record::data_buf
```

附加数据缓冲区（Additional data buffer）。

<a id="ad310f8c8e3a167492a6e698336b7f400"></a>

### `elem_buf`

```c
struct net_buf_simple* bt_mesh_comp_p2_record::elem_buf
```

元素偏移缓冲区（Element offset buffer）。

<a id="a4d947193b1a0f46c9df1eca298135646"></a>

### `id`

```c
uint16_t bt_mesh_comp_p2_record::id
```

Mesh 规范标识符（Mesh profile ID）。

<a id="aa718c024d6ce339ac8c352319b878c53"></a>

### `[struct]`

```c
struct { ... } bt_mesh_comp_p2_record::version
```

Mesh 规范版本（Mesh Profile Version）。

<a id="a5377ce835db8ce408d8dabfd87c858f5"></a>

### `x`

```c
uint8_t bt_mesh_comp_p2_record::x
```

主版本（Major version）。

<a id="a0ceff9becd0eb14ca190c49f56ec0957"></a>

### `y`

```c
uint8_t bt_mesh_comp_p2_record::y
```

次版本（Minor version）。

<a id="a90e80906ef6d2b8b932215ad183db2d5"></a>

### `z`

```c
uint8_t bt_mesh_comp_p2_record::z
```

Z 版本（Z version）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_bt_mesh_comp_p1_model_item_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_bt_mesh_dev_capabilities_结构体.md)
