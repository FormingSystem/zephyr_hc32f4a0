---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-33
title: bt_mesh_comp2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_bt\_mesh\_comp2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp2.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

节点组成数据（Composition Data）的第2页。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

节点组成数据（Composition Data）的第2页。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_a9f3425cd64cc487e9a49b85bb0f2159b"></a>

```c
size_t record_cnt
```

相关声明：[record_cnt](#a9f3425cd64cc487e9a49b85bb0f2159b)。

设备上的 Mesh 规范记录数量（Mesh Profile records）。

<a id="r_adf022ca0738626832d566fd6a5a1d889"></a>

```c
const struct bt_mesh_comp2_record * record
```

相关声明：[bt_mesh_comp2_record](P034_bt_mesh_comp2_record_结构体.md)、[record](#adf022ca0738626832d566fd6a5a1d889)。

记录列表（List of records）。

## 33.2\_详细说明（Detailed Documentation）

<a id="adf022ca0738626832d566fd6a5a1d889"></a>

### `record`

```c
const struct bt_mesh_comp2_record* bt_mesh_comp2::record
```

记录列表（List of records）。

<a id="a9f3425cd64cc487e9a49b85bb0f2159b"></a>

### `record_cnt`

```c
size_t bt_mesh_comp2::record_cnt
```

设备上的 Mesh 规范记录数量（Mesh Profile records）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [bt_mesh_comp2_record](P034_bt_mesh_comp2_record_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_bt_mesh_comp_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_bt_mesh_comp2_record_结构体.md)
