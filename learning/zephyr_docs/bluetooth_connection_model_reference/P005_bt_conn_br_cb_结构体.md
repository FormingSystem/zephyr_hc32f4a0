---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-5
title: bt_conn_br_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__br__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_bt\_conn\_br\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__br__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BR/EDR 专用连接回调。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

BR/EDR 专用连接回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_aa278e529ac45aab63586b2566e857057"></a>

```c
void(* mode_changed )(struct bt_conn *conn, uint8_t mode, uint16_t interval)
```

相关声明：[mode_changed](#aa278e529ac45aab63586b2566e857057)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

基本速率／增强数据率连接模式（BR/EDR connection mode）发生变化。

<a id="r_a37af27d6d6d0e767dd439f24ff999c28"></a>

```c
void(* role_changed )(struct bt_conn *conn, uint8_t status)
```

相关声明：[role_changed](#a37af27d6d6d0e767dd439f24ff999c28)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

基本速率／增强数据率连接角色（BR/EDR connection role）发生变化。

<a id="r_a93be2950207ea20c02b66647f5335273"></a>

```c
void(* packet_type_changed )(struct bt_conn *conn, uint8_t status, uint16_t packet_type)
```

相关声明：[packet_type_changed](#a93be2950207ea20c02b66647f5335273)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

基本速率／增强数据率连接（BR/EDR）的数据包类型发生变化。

## 5.2\_详细说明（Detailed Documentation）

<a id="aa278e529ac45aab63586b2566e857057"></a>

### `mode_changed`

```c
void(* bt_conn_br_cb::mode_changed) (struct bt_conn *conn, uint8_t mode, uint16_t interval)
```

基本速率／增强数据率连接模式（BR/EDR connection mode）发生变化。

此回调通知应用，嗅探模式（Sniff mode）已变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `mode` | 活动／嗅探模式（Active/Sniff mode）。 |
| `interval` | 嗅探间隔（Sniff interval）。 |

<a id="a93be2950207ea20c02b66647f5335273"></a>

### `packet_type_changed`

```c
void(* bt_conn_br_cb::packet_type_changed) (struct bt_conn *conn, uint8_t status, uint16_t packet_type)
```

基本速率／增强数据率连接（BR/EDR）的数据包类型发生变化。

此回调通知应用，连接数据包类型变更过程（Connection packet type change procedure）已完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `status` | 事件的主机控制器接口状态（HCI status）。 |
| `packet_type` | 新的数据包类型位掩码（Packet type bitmask）。 |

<a id="a37af27d6d6d0e767dd439f24ff999c28"></a>

### `role_changed`

```c
void(* bt_conn_br_cb::role_changed) (struct bt_conn *conn, uint8_t status)
```

基本速率／增强数据率连接角色（BR/EDR connection role）发生变化。

此回调通知应用，基本速率／增强数据率角色切换过程（BR/EDR role switch procedure）已完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `status` | 角色变更事件的主机控制器接口状态（HCI status）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [bt_conn](P002_bt_conn_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_bt_conn_auth_info_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_bt_conn_br_info_结构体.md)
