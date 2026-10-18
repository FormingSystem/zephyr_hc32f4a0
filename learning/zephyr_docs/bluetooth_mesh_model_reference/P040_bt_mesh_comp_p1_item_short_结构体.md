---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-40
title: bt_mesh_comp_p1_item_short_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p1__item__short.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_bt\_mesh\_comp\_p1\_item\_short\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p1__item__short.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

短格式表示的扩展模型项（Extended Model Item）。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

短格式表示的扩展模型项（Extended Model Item）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_a1fb6c8134a2c02e3b83dfea12ab39410"></a>

```c
uint8_t elem_offset: 3
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[elem_offset](#a1fb6c8134a2c02e3b83dfea12ab39410)。

元素地址修饰值（Element address modifier）。

<a id="r_a7e2152fe608c52cbc0700a43a5653132"></a>

```c
uint8_t mod_item_idx: 5
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mod_item_idx](#a7e2152fe608c52cbc0700a43a5653132)。

模型索引（Model Index）。

## 40.2\_详细说明（Detailed Documentation）

<a id="a1fb6c8134a2c02e3b83dfea12ab39410"></a>

### `elem_offset`

```c
uint8_t bt_mesh_comp_p1_item_short::elem_offset
```

元素地址修饰值（Element address modifier）。

<a id="a7e2152fe608c52cbc0700a43a5653132"></a>

### `mod_item_idx`

```c
uint8_t bt_mesh_comp_p1_item_short::mod_item_idx
```

模型索引（Model Index）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_bt_mesh_comp_p1_item_long_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_bt_mesh_comp_p1_model_item_结构体.md)
