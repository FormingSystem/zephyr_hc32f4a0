---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-74
title: bt_mesh_mod_id_vnd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__mod__id__vnd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_bt\_mesh\_mod\_id\_vnd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__mod__id__vnd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

厂商模型标识（Vendor Model ID）。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

厂商模型标识（Vendor Model ID）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 74.1\_数据成员（Data Fields）

<a id="r_a187a919337c92f54eaba6f932c7a3670"></a>

```c
uint16_t company
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[company](#a187a919337c92f54eaba6f932c7a3670)。

厂商的公司标识符（Vendor company ID）。

<a id="r_a1a299852544a5e6fa3c34ac5ffd883d8"></a>

```c
uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#a1a299852544a5e6fa3c34ac5ffd883d8)。

模型标识符（Model ID）。

## 74.2\_详细说明（Detailed Documentation）

<a id="a187a919337c92f54eaba6f932c7a3670"></a>

### `company`

```c
uint16_t bt_mesh_mod_id_vnd::company
```

厂商的公司标识符（Vendor company ID）。

<a id="a1a299852544a5e6fa3c34ac5ffd883d8"></a>

### `id`

```c
uint16_t bt_mesh_mod_id_vnd::id
```

模型标识符（Model ID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 74.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P073_bt_mesh_lpn_timing_结构体.md) · [返回大纲](大纲.md) · [下一章](P075_bt_mesh_model_结构体.md)
