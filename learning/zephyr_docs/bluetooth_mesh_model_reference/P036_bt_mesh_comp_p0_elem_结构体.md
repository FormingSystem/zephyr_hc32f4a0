---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-36
title: bt_mesh_comp_p0_elem_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p0__elem.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_bt\_mesh\_comp\_p0\_elem\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p0__elem.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

组成数据（Composition Data）第0页的元素表示。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

组成数据（Composition Data）第0页的元素表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_a832cdb0a10d364a048971f59f51e841d"></a>

```c
uint16_t loc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[loc](#a832cdb0a10d364a048971f59f51e841d)。

元素位置（Element location）。

<a id="r_a17f61eab2df28f2031f2fbab28254484"></a>

```c
size_t nsig
```

相关声明：[nsig](#a17f61eab2df28f2031f2fbab28254484)。

此元素中的蓝牙技术联盟模型数量（SIG models）。

<a id="r_a2e1bd3146ebc934e9fab0242a06d5b99"></a>

```c
size_t nvnd
```

相关声明：[nvnd](#a2e1bd3146ebc934e9fab0242a06d5b99)。

此元素中的厂商模型数量（Vendor models）。

## 36.2\_详细说明（Detailed Documentation）

<a id="a832cdb0a10d364a048971f59f51e841d"></a>

### `loc`

```c
uint16_t bt_mesh_comp_p0_elem::loc
```

元素位置（Element location）。

<a id="a17f61eab2df28f2031f2fbab28254484"></a>

### `nsig`

```c
size_t bt_mesh_comp_p0_elem::nsig
```

此元素中的蓝牙技术联盟模型数量（SIG models）。

<a id="a2e1bd3146ebc934e9fab0242a06d5b99"></a>

### `nvnd`

```c
size_t bt_mesh_comp_p0_elem::nvnd
```

此元素中的厂商模型数量（Vendor models）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_bt_mesh_comp_p0_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_bt_mesh_comp_p1_elem_结构体.md)
