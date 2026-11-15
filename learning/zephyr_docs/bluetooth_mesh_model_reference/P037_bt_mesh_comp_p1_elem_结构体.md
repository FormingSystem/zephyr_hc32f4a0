---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-37
title: bt_mesh_comp_p1_elem_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p1__elem.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_bt\_mesh\_comp\_p1\_elem\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p1__elem.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

组成数据（Composition Data）第1页的元素表示。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

组成数据（Composition Data）第1页的元素表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_aa6aa100992502cef0484a127224cf07b"></a>

```c
size_t nsig
```

相关声明：[nsig](#aa6aa100992502cef0484a127224cf07b)。

此元素中的蓝牙技术联盟模型数量（SIG models）。

<a id="r_a25492ac30a362e4490d11169ed98197b"></a>

```c
size_t nvnd
```

相关声明：[nvnd](#a25492ac30a362e4490d11169ed98197b)。

此元素中的厂商模型数量（Vendor models）。

## 37.2\_详细说明（Detailed Documentation）

<a id="aa6aa100992502cef0484a127224cf07b"></a>

### `nsig`

```c
size_t bt_mesh_comp_p1_elem::nsig
```

此元素中的蓝牙技术联盟模型数量（SIG models）。

<a id="a25492ac30a362e4490d11169ed98197b"></a>

### `nvnd`

```c
size_t bt_mesh_comp_p1_elem::nvnd
```

此元素中的厂商模型数量（Vendor models）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_bt_mesh_comp_p0_elem_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_bt_mesh_comp_p1_ext_item_结构体.md)
