---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-66
title: bt_gatt_service_static_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__service__static.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_bt\_gatt\_service\_static\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__service__static.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

静态 GATT 服务结构体。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

静态 GATT 服务结构（Static GATT Service structure）。允许用户声明静态 GATT 服务，以减少随机存取存储器（RAM）占用。可使用 `BT_GATT_SERVICE_DEFINE` 宏静态定义并注册服务。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_a38f9e02241fe37f68df5dd8782b59e9f"></a>

```c
const struct bt_gatt_attr * attrs
```

相关声明：[bt_gatt_attr](P049_bt_gatt_attr_结构体.md)、[attrs](#a38f9e02241fe37f68df5dd8782b59e9f)。

服务属性（Service Attributes）。

<a id="r_a84c35a391e372396e2ec89eaf0d4d047"></a>

```c
size_t attr_count
```

相关声明：[attr_count](#a84c35a391e372396e2ec89eaf0d4d047)。

服务属性数量（Service Attribute count）。

## 66.2\_详细说明（Detailed Documentation）

<a id="a84c35a391e372396e2ec89eaf0d4d047"></a>

### `attr_count`

```c
size_t bt_gatt_service_static::attr_count
```

服务属性数量（Service Attribute count）。

<a id="a38f9e02241fe37f68df5dd8782b59e9f"></a>

### `attrs`

```c
const struct bt_gatt_attr* bt_gatt_service_static::attrs
```

服务属性（Service Attributes）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_gatt_attr](P049_bt_gatt_attr_结构体.md)
- [BT_GATT_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga04c7887fb67107bd060dd023fd3186d5)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_bt_gatt_service_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_bt_gatt_service_val_结构体.md)
