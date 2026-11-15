---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-8
title: bt_bip_transport_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__transport__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_bt\_bip\_transport\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__transport__ops.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BIP 传输层操作（Transport Layer Operations）。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

<a id="details"></a>

基本成像规范传输层操作（BIP transport layer operations）。用于传输层事件的回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_a80a1596a382b93366e13a857a5edf3ba"></a>

```c
void(* connected )(struct bt_conn *conn, struct bt_bip *bip)
```

相关声明：[connected](#a80a1596a382b93366e13a857a5edf3ba)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bip](P001_bt_bip_结构体.md)。

传输连接回调（Transport connected callback）。

<a id="r_a49f1708ed03ebe8cfb6a2f11b76bda73"></a>

```c
void(* disconnected )(struct bt_bip *bip)
```

相关声明：[disconnected](#a49f1708ed03ebe8cfb6a2f11b76bda73)、[bt_bip](P001_bt_bip_结构体.md)。

传输断开回调（Transport disconnected callback）。

## 8.2\_详细说明（Detailed Documentation）

<a id="a80a1596a382b93366e13a857a5edf3ba"></a>

### `connected`

```c
void(* bt_bip_transport_ops::connected) (struct bt_conn *conn, struct bt_bip *bip)
```

传输连接回调（Transport connected callback）。

底层传输，即 RFCOMM／L2CAP，建立连接时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接（Bluetooth Connection）。 |
| `bip` | 基本成像规范实例（BIP instance）。 |

<a id="a49f1708ed03ebe8cfb6a2f11b76bda73"></a>

### `disconnected`

```c
void(* bt_bip_transport_ops::disconnected) (struct bt_bip *bip)
```

传输断开回调（Transport disconnected callback）。

底层传输断开连接时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/bip.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/bip.h](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_bip](P001_bt_bip_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_bt_bip_server_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_bt_br_bond_info_结构体.md)
