---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-38
title: bt_mesh_comp_p1_ext_item_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p1__ext__item.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_bt\_mesh\_comp\_p1\_ext\_item\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p1__ext__item.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

扩展模型项（Extended Model Item）。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

扩展模型项（Extended Model Item）。

<a id="header-pub-types"></a>
<a id="pub-types"></a>

## 38.1\_公开类型（Public Types）

<a id="r_a05a526a8448e7b8a4766eb038e4c1a39"></a>

```c
enum { SHORT , LONG }
```

相关声明：[SHORT](#a05a526a8448e7b8a4766eb038e4c1a39a23a15546d8722d7a4706ea34c5785658)、[LONG](#a05a526a8448e7b8a4766eb038e4c1a39ae96bb3e960c4d2c356c0070f34740119)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.2\_数据成员（Data Fields）

<a id="r_a43f50f35690e54d3680a6daa989ce1c0"></a>

```c
enum bt_mesh_comp_p1_ext_item:: { ... } type
```

相关声明：[type](#a43f50f35690e54d3680a6daa989ce1c0)。

```c
union {
```

<a id="r_ada88b6ac5ae6942b5bfb3b69bd04a9f5"></a>

```c
struct bt_mesh_comp_p1_item_short short_item
```

相关声明：[bt_mesh_comp_p1_item_short](P040_bt_mesh_comp_p1_item_short_结构体.md)、[short_item](#ae17176001203ee8c282f06e994cee647)。

短格式表示的条目（Item in short representation）。

<a id="r_a082cb7f3662ce0babd865a6cff926855"></a>

```c
struct bt_mesh_comp_p1_item_long long_item
```

相关声明：[bt_mesh_comp_p1_item_long](P039_bt_mesh_comp_p1_item_long_结构体.md)、[long_item](#a3962046fc095348035a193dad60d1149)。

长格式表示的条目（Item in long representation）。

<a id="r_aff092a724a2997ae05b0c4f1d1045c2f"></a>

```c
};
```

## 38.3\_详细说明（Detailed Documentation）

<a id="a05a526a8448e7b8a4766eb038e4c1a39"></a>

### `anonymous enum`

```c
anonymous enum
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SHORT` |  |
| `LONG` |  |

<a id="aff092a724a2997ae05b0c4f1d1045c2f"></a>

### `[union]`

```c
union { ... } bt_mesh_comp_p1_ext_item
```

<a id="a3962046fc095348035a193dad60d1149"></a>

### `long_item`

```c
struct bt_mesh_comp_p1_item_long bt_mesh_comp_p1_ext_item::long_item
```

长格式表示的条目（Item in long representation）。

<a id="ae17176001203ee8c282f06e994cee647"></a>

### `short_item`

```c
struct bt_mesh_comp_p1_item_short bt_mesh_comp_p1_ext_item::short_item
```

短格式表示的条目（Item in short representation）。

<a id="a43f50f35690e54d3680a6daa989ce1c0"></a>

### `[]`

```c
enum { ... } bt_mesh_comp_p1_ext_item::type
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 38.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)
- [bt_mesh_comp_p1_item_short](P040_bt_mesh_comp_p1_item_short_结构体.md)
- [bt_mesh_comp_p1_item_long](P039_bt_mesh_comp_p1_item_long_结构体.md)
- [bt_mesh_comp_p1_ext_item](P038_bt_mesh_comp_p1_ext_item_结构体.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a05a526a8448e7b8a4766eb038e4c1a39a23a15546d8722d7a4706ea34c5785658"></a>
<a id="a05a526a8448e7b8a4766eb038e4c1a39ae96bb3e960c4d2c356c0070f34740119"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_bt_mesh_comp_p1_elem_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_bt_mesh_comp_p1_item_long_结构体.md)
