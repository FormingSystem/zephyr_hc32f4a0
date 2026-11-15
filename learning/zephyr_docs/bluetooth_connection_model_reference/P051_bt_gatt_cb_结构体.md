---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-51
title: bt_gatt_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_bt\_gatt\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 回调结构体。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_a93fe1a626ab59c38ef56f02671f88980"></a>

```c
void(* att_mtu_updated )(struct bt_conn *conn, uint16_t tx, uint16_t rx)
```

相关声明：[att_mtu_updated](#a93fe1a626ab59c38ef56f02671f88980)、[bt_conn](P002_bt_conn_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

连接上的最大属性协议传输单元（ATT MTU）已变化。

## 51.2\_详细说明（Detailed Documentation）

<a id="a93fe1a626ab59c38ef56f02671f88980"></a>

### `att_mtu_updated`

```c
void(* bt_gatt_cb::att_mtu_updated) (struct bt_conn *conn, uint16_t tx, uint16_t rx)
```

连接上的最大属性协议传输单元（ATT MTU）已变化。

此回调通知应用，最大发送或接收 ATT 最大传输单元（TX／RX ATT MTU）已增大。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `tx` | 更新后的发送 ATT 最大传输单元（TX ATT MTU）。 |
| `rx` | 更新后的接收 ATT 最大传输单元（RX ATT MTU）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_conn](P002_bt_conn_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_bt_gatt_authorization_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_bt_gatt_ccc_结构体.md)
