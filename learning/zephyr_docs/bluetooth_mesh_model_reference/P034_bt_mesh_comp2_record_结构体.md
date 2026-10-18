---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-34
title: bt_mesh_comp2_record_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp2__record.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_bt\_mesh\_comp2\_record\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp2__record.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

组成数据（Composition Data）的第2页记录。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

组成数据（Composition Data）的第2页记录。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_a19ce94025c1c8079ca2789bbcd09b00e"></a>

```c
uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#a19ce94025c1c8079ca2789bbcd09b00e)。

Mesh 规范标识符（Mesh profile ID）。

```c
struct {
```

<a id="r_a74305d42b4dee9f0e707597f98a739fa"></a>

```c
uint8_t x
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[x](#a5f25c33170c77375f6492ad3cc0feaac)。

主版本（Major version）。

<a id="r_a1b98e309bd61f431afc0eadae0f232a6"></a>

```c
uint8_t y
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[y](#a4970a0757c34ab97697c69728b564df6)。

次版本（Minor version）。

<a id="r_a072f4f30d323cbc3dae494f1b4714f75"></a>

```c
uint8_t z
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[z](#ac3cabce01490191f145234f386b9b119)。

Z 版本（Z version）。

<a id="r_a26370a5dc68af03424c0f2f4fecd0181"></a>

```c
} version
```

相关声明：[version](#a26370a5dc68af03424c0f2f4fecd0181)。

Mesh 规范版本（Mesh Profile Version）。

<a id="r_ad13066e9d6d32e8e2eab64881249eb7e"></a>

```c
uint8_t elem_offset_cnt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[elem_offset_cnt](#ad13066e9d6d32e8e2eab64881249eb7e)。

元素偏移数量（Element offset count）。

<a id="r_a6f81d99a62252cd26d87ca4fb289bdf9"></a>

```c
const uint8_t * elem_offset
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[elem_offset](#a6f81d99a62252cd26d87ca4fb289bdf9)。

元素偏移列表（Element offset list）。

<a id="r_abdc488e846233fa05f0fc48f4081576e"></a>

```c
uint16_t data_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[data_len](#abdc488e846233fa05f0fc48f4081576e)。

附加数据长度（Length of additional data）。

<a id="r_acd5f5770a6606ad00fa0815e4866ec4e"></a>

```c
const void * data
```

相关声明：[data](#acd5f5770a6606ad00fa0815e4866ec4e)。

附加数据（Additional data）。

## 34.2\_详细说明（Detailed Documentation）

<a id="acd5f5770a6606ad00fa0815e4866ec4e"></a>

### `data`

```c
const void* bt_mesh_comp2_record::data
```

附加数据（Additional data）。

<a id="abdc488e846233fa05f0fc48f4081576e"></a>

### `data_len`

```c
uint16_t bt_mesh_comp2_record::data_len
```

附加数据长度（Length of additional data）。

<a id="a6f81d99a62252cd26d87ca4fb289bdf9"></a>

### `elem_offset`

```c
const uint8_t* bt_mesh_comp2_record::elem_offset
```

元素偏移列表（Element offset list）。

<a id="ad13066e9d6d32e8e2eab64881249eb7e"></a>

### `elem_offset_cnt`

```c
uint8_t bt_mesh_comp2_record::elem_offset_cnt
```

元素偏移数量（Element offset count）。

<a id="a19ce94025c1c8079ca2789bbcd09b00e"></a>

### `id`

```c
uint16_t bt_mesh_comp2_record::id
```

Mesh 规范标识符（Mesh profile ID）。

<a id="a26370a5dc68af03424c0f2f4fecd0181"></a>

### `[struct]`

```c
struct { ... } bt_mesh_comp2_record::version
```

Mesh 规范版本（Mesh Profile Version）。

<a id="a5f25c33170c77375f6492ad3cc0feaac"></a>

### `x`

```c
uint8_t bt_mesh_comp2_record::x
```

主版本（Major version）。

<a id="a4970a0757c34ab97697c69728b564df6"></a>

### `y`

```c
uint8_t bt_mesh_comp2_record::y
```

次版本（Minor version）。

<a id="ac3cabce01490191f145234f386b9b119"></a>

### `z`

```c
uint8_t bt_mesh_comp2_record::z
```

Z 版本（Z version）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_bt_mesh_comp2_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_bt_mesh_comp_p0_结构体.md)
