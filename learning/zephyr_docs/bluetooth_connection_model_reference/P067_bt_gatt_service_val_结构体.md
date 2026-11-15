---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-67
title: bt_gatt_service_val_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__service__val.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_bt\_gatt\_service\_val\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__service__val.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务（Service）属性值。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

服务属性值（Service Attribute Value）。这是由属性类型（Attribute Type）描述、并通过数据库中的属性句柄（Attribute Handle）索引的数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_a683e01db92400e76aed32b7a81369a55"></a>

```c
const struct bt_uuid * uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#a683e01db92400e76aed32b7a81369a55)。

服务通用唯一标识符（Service UUID）。

<a id="r_a75b6fcf0f9f29ad05ccac0e83bcb31b7"></a>

```c
uint16_t end_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[end_handle](#a75b6fcf0f9f29ad05ccac0e83bcb31b7)。

服务中最后一个属性的句柄（Last Attribute handle）。

## 67.2\_详细说明（Detailed Documentation）

<a id="a75b6fcf0f9f29ad05ccac0e83bcb31b7"></a>

### `end_handle`

```c
uint16_t bt_gatt_service_val::end_handle
```

服务中最后一个属性的句柄（Last Attribute handle）。

<a id="a683e01db92400e76aed32b7a81369a55"></a>

### `uuid`

```c
const struct bt_uuid* bt_gatt_service_val::uuid
```

服务通用唯一标识符（Service UUID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_bt_gatt_service_static_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_bt_gatt_subscribe_params_结构体.md)
