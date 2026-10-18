---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-60
title: bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_bt\_mesh\_elem\_\_bt\_mesh\_elem\_rt\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Mesh元素（Mesh Element）的运行时信息。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

Mesh元素（Mesh Element）的运行时信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_a659279b38f1f3e015ebc648901577038"></a>

```c
uint16_t addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr](#a659279b38f1f3e015ebc648901577038)。

单播地址（Unicast Address）。

## 60.2\_详细说明（Detailed Documentation）

<a id="a659279b38f1f3e015ebc648901577038"></a>

### `addr`

```c
uint16_t bt_mesh_elem::bt_mesh_elem_rt_ctx::addr
```

单播地址（Unicast Address）。

在运行时配网（Provisioning）过程中设置。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_bt_mesh_elem_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_bt_mesh_friend_cb_结构体.md)
