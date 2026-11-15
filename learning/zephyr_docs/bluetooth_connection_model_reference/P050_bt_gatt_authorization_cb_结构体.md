---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-50
title: bt_gatt_authorization_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__authorization__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_bt\_gatt\_authorization\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__authorization__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 授权（Authorization）回调结构体。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 授权（Authorization）回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.1\_数据成员（Data Fields）

<a id="r_a7b1bcbe10f12c90ee4e3214e36e9c2a3"></a>

```c
bool(* read_authorize )(struct bt_conn *conn, const struct bt_gatt_attr *attr)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[read_authorize](#a7b1bcbe10f12c90ee4e3214e36e9c2a3)、[bt_conn](P002_bt_conn_结构体.md)、[bt_gatt_attr](P049_bt_gatt_attr_结构体.md)。

授权 GATT 读取操作（Read operation）。

<a id="r_a7c12bd14f87f91e672eaaf92e1aa6e7b"></a>

```c
bool(* write_authorize )(struct bt_conn *conn, const struct bt_gatt_attr *attr)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[write_authorize](#a7c12bd14f87f91e672eaaf92e1aa6e7b)、[bt_conn](P002_bt_conn_结构体.md)、[bt_gatt_attr](P049_bt_gatt_attr_结构体.md)。

授权 GATT 写入操作（Write operation）。

## 50.2\_详细说明（Detailed Documentation）

<a id="a7b1bcbe10f12c90ee4e3214e36e9c2a3"></a>

### `read_authorize`

```c
bool(* bt_gatt_authorization_cb::read_authorize) (struct bt_conn *conn, const struct bt_gatt_attr *attr)
```

授权 GATT 读取操作（Read operation）。

此回调允许应用对正在读取的属性（Attribute）授权 GATT 读取操作（Read operation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 正在读取的属性（Attribute）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 授权该操作并允许执行（Authorize）。 |
| `false` | 拒绝该操作并阻止执行（Reject）。 |

<a id="a7c12bd14f87f91e672eaaf92e1aa6e7b"></a>

### `write_authorize`

```c
bool(* bt_gatt_authorization_cb::write_authorize) (struct bt_conn *conn, const struct bt_gatt_attr *attr)
```

授权 GATT 写入操作（Write operation）。

此回调允许应用对正在写入的属性（Attribute）授权 GATT 写入操作（Write operation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `attr` | 正在写入的属性（Attribute）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 授权该操作并允许执行（Authorize）。 |
| `false` | 拒绝该操作并阻止执行（Reject）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 50.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_conn](P002_bt_conn_结构体.md)
- [bt_gatt_attr](P049_bt_gatt_attr_结构体.md)
- [true](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_bt_gatt_attr_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_bt_gatt_cb_结构体.md)
