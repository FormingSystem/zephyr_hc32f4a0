---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-32
title: bt_mesh_comp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_bt\_mesh\_comp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

节点组成（Node Composition）。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

节点组成（Node Composition）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_a648f695898305ef9e6f4f9db42dd8cf9"></a>

```c
uint16_t cid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cid](#a648f695898305ef9e6f4f9db42dd8cf9)。

公司标识符（Company ID）。

<a id="r_a54031f4c3683a7209e8f7441c5875788"></a>

```c
uint16_t pid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pid](#a54031f4c3683a7209e8f7441c5875788)。

产品标识符（Product ID）。

<a id="r_a7e4351e81e4e04bb9681e76d384f2fa5"></a>

```c
uint16_t vid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vid](#a7e4351e81e4e04bb9681e76d384f2fa5)。

版本标识符（Version ID）。

<a id="r_aff69499c7ac2c1ba643c946c75aa21ce"></a>

```c
size_t elem_count
```

相关声明：[elem_count](#aff69499c7ac2c1ba643c946c75aa21ce)。

此设备的元素数量（Number of elements）。

<a id="r_ad3da0629db1cb423260aa202cab7f062"></a>

```c
const struct bt_mesh_elem * elem
```

相关声明：[bt_mesh_elem](P059_bt_mesh_elem_结构体.md)、[elem](#ad3da0629db1cb423260aa202cab7f062)。

元素列表（List of elements）。

## 32.2\_详细说明（Detailed Documentation）

<a id="a648f695898305ef9e6f4f9db42dd8cf9"></a>

### `cid`

```c
uint16_t bt_mesh_comp::cid
```

公司标识符（Company ID）。

<a id="ad3da0629db1cb423260aa202cab7f062"></a>

### `elem`

```c
const struct bt_mesh_elem* bt_mesh_comp::elem
```

元素列表（List of elements）。

<a id="aff69499c7ac2c1ba643c946c75aa21ce"></a>

### `elem_count`

```c
size_t bt_mesh_comp::elem_count
```

此设备的元素数量（Number of elements）。

<a id="a54031f4c3683a7209e8f7441c5875788"></a>

### `pid`

```c
uint16_t bt_mesh_comp::pid
```

产品标识符（Product ID）。

<a id="a7e4351e81e4e04bb9681e76d384f2fa5"></a>

### `vid`

```c
uint16_t bt_mesh_comp::vid
```

版本标识符（Version ID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_elem](P059_bt_mesh_elem_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_bt_mesh_cfg_cli_mod_pub_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_bt_mesh_comp2_结构体.md)
