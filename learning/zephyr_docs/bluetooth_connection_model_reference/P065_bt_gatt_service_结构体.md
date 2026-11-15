---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-65
title: bt_gatt_service_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__service.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_bt\_gatt\_service\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__service.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 服务（Service）结构体。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 服务结构（GATT Service structure）。用于定义可以在运行时注册和注销的 GATT 服务。有关服务应在何时注册，参见 `bt_gatt_service_register`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_a0281e96ab54519df641f6c489fdc6b5b"></a>

```c
struct bt_gatt_attr * attrs
```

相关声明：[bt_gatt_attr](P049_bt_gatt_attr_结构体.md)、[attrs](#a0281e96ab54519df641f6c489fdc6b5b)。

服务属性（Service Attributes）。

<a id="r_a87d8316a92ae04678d7be0ae76ed86cb"></a>

```c
size_t attr_count
```

相关声明：[attr_count](#a87d8316a92ae04678d7be0ae76ed86cb)。

服务属性数量（Service Attribute count）。

## 65.2\_详细说明（Detailed Documentation）

<a id="a87d8316a92ae04678d7be0ae76ed86cb"></a>

### `attr_count`

```c
size_t bt_gatt_service::attr_count
```

服务属性数量（Service Attribute count）。

<a id="a0281e96ab54519df641f6c489fdc6b5b"></a>

### `attrs`

```c
struct bt_gatt_attr* bt_gatt_service::attrs
```

服务属性（Service Attributes）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_gatt_attr](P049_bt_gatt_attr_结构体.md)
- [bt_gatt_service_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gab4d9cfea04e44445d5dc30ad52842b64)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_bt_gatt_scc_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_bt_gatt_service_static_结构体.md)
