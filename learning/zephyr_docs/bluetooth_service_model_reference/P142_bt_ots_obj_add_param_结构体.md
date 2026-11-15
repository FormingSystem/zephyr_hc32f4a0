---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-142
title: bt_ots_obj_add_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__obj__add__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第142章\_bt\_ots\_obj\_add\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__obj__add__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象传输服务（OTS）添加对象的描述符。

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="details"></a>

对象传输服务（OTS）添加对象的描述符。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 142.1\_数据成员（Data Fields）

<a id="r_a721734439b43e40324c3a548b5a4eb34"></a>

```c
uint32_t size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[size](#a721734439b43e40324c3a548b5a4eb34)。

待分配的对象大小。

<a id="r_afdbaf218850d4bf3f40f7a9e8d7b0595"></a>

```c
struct bt_ots_obj_type type
```

相关声明：[bt_ots_obj_type](P146_bt_ots_obj_type_结构体.md)、[type](#afdbaf218850d4bf3f40f7a9e8d7b0595)。

对象类型（Object type）。

## 142.2\_详细说明（Detailed Documentation）

<a id="a721734439b43e40324c3a548b5a4eb34"></a>

### `size`

```c
uint32_t bt_ots_obj_add_param::size
```

待分配的对象大小。

<a id="afdbaf218850d4bf3f40f7a9e8d7b0595"></a>

### `type`

```c
struct bt_ots_obj_type bt_ots_obj_add_param::type
```

对象类型（Object type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ots.h`

## 142.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ots.h](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_ots_obj_type](P146_bt_ots_obj_type_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P141_bt_ots_init_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P143_bt_ots_obj_created_desc_结构体.md)
