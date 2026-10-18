---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-60
title: bt_gatt_include_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__include.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_bt\_gatt\_include\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__include.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含服务（Include）属性值。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

包含属性值（Include Attribute Value）。此结构表示 GATT 服务器中的被包含服务属性（Included service attribute）。被包含服务是从另一个服务内部引用的服务，可用于复用公共服务定义。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_afa028e8daae00e3b1bc0b866c4335af3"></a>

```c
const struct bt_uuid * uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#afa028e8daae00e3b1bc0b866c4335af3)。

服务通用唯一标识符（Service UUID）。

<a id="r_ac7f6c1a8018f483dce14f0fe21031232"></a>

```c
uint16_t start_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[start_handle](#ac7f6c1a8018f483dce14f0fe21031232)。

被包含服务内第一个属性的句柄（First attribute handle）。

<a id="r_a54d20cebfd6ba62b692c363acdc25d61"></a>

```c
uint16_t end_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[end_handle](#a54d20cebfd6ba62b692c363acdc25d61)。

被包含服务内最后一个属性的句柄（Last attribute handle）。

## 60.2\_详细说明（Detailed Documentation）

<a id="a54d20cebfd6ba62b692c363acdc25d61"></a>

### `end_handle`

```c
uint16_t bt_gatt_include::end_handle
```

被包含服务内最后一个属性的句柄（Last attribute handle）。

<a id="ac7f6c1a8018f483dce14f0fe21031232"></a>

### `start_handle`

```c
uint16_t bt_gatt_include::start_handle
```

被包含服务内第一个属性的句柄（First attribute handle）。

<a id="afa028e8daae00e3b1bc0b866c4335af3"></a>

### `uuid`

```c
const struct bt_uuid* bt_gatt_include::uuid
```

服务通用唯一标识符（Service UUID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_bt_gatt_exchange_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_bt_gatt_indicate_params_结构体.md)
