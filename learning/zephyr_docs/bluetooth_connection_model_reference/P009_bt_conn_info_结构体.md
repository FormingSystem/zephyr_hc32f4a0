---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-9
title: bt_conn_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_bt\_conn\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接信息结构体（Connection Info Structure）。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

连接信息结构体（Connection Info Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a7995e1291be494b5bdf860eceea0cad1"></a>

```c
enum bt_conn_type type
```

相关声明：[bt_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab8dde20ae75b51f1e28dbeed06001f20)、[type](#a7995e1291be494b5bdf860eceea0cad1)。

连接类型（Connection Type）。

<a id="r_a8237b8c1bb9a97a174d04cbe13dca7c7"></a>

```c
uint8_t role
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[role](#a8237b8c1bb9a97a174d04cbe13dca7c7)。

连接角色（Connection Role）。

<a id="r_a3a4e24519b5d3ba547423e53c4d92a5c"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a3a4e24519b5d3ba547423e53c4d92a5c)。

创建此连接时使用的本地身份（Local identity）。

```c
union {
```

<a id="r_aa54b00cdf9be8bc071efb9f407324794"></a>

```c
struct bt_conn_le_info le
```

相关声明：[bt_conn_le_info](P023_bt_conn_le_info_结构体.md)、[le](#a6b536e7732dcf7b77a7bc05116dca548)。

低功耗连接专用信息（LE Connection specific Info）。

<a id="r_a2fd70a49891b65f5c3caa3cbd084257c"></a>

```c
struct bt_conn_br_info br
```

相关声明：[bt_conn_br_info](P006_bt_conn_br_info_结构体.md)、[br](#a799e59d3a85625799a32ac3f0b3d67d1)。

基本速率／增强数据率连接专用信息（BR/EDR Connection specific Info）。

<a id="r_a81db42eee8dfa3a98b6afc2b5f078e84"></a>

```c
struct bt_conn_sco_info sco
```

相关声明：[bt_conn_sco_info](P040_bt_conn_sco_info_结构体.md)、[sco](#ad622c69f262ee53ec94918857250a2a0)。

同步面向连接链路专用信息（SCO Connection specific Info）。

<a id="r_a49fd1bafffd76f6ebc1e593e531ec81c"></a>

```c
};
```

连接类型专用信息（Connection Type specific Info）。

<a id="r_ae566e2382b69ff27314dc1dd632dbdbc"></a>

```c
enum bt_conn_state state
```

相关声明：[bt_conn_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9442c1479db60e2db40a2ea6de565282)、[state](#ae566e2382b69ff27314dc1dd632dbdbc)。

连接状态（Connection state）。

<a id="r_ae4405f1b4f3fe2ff6253453964860931"></a>

```c
struct bt_security_info security
```

相关声明：[bt_security_info](P130_bt_security_info_结构体.md)、[security](#ae4405f1b4f3fe2ff6253453964860931)。

安全专用信息（Security specific info）。

## 9.2\_详细说明（Detailed Documentation）

<a id="a49fd1bafffd76f6ebc1e593e531ec81c"></a>

### `[union]`

```c
union { ... } bt_conn_info
```

连接类型专用信息（Connection Type specific Info）。

<a id="a799e59d3a85625799a32ac3f0b3d67d1"></a>

### `br`

```c
struct bt_conn_br_info bt_conn_info::br
```

基本速率／增强数据率连接专用信息（BR/EDR Connection specific Info）。

<a id="a3a4e24519b5d3ba547423e53c4d92a5c"></a>

### `id`

```c
uint8_t bt_conn_info::id
```

创建此连接时使用的本地身份（Local identity）。

<a id="a6b536e7732dcf7b77a7bc05116dca548"></a>

### `le`

```c
struct bt_conn_le_info bt_conn_info::le
```

低功耗连接专用信息（LE Connection specific Info）。

<a id="a8237b8c1bb9a97a174d04cbe13dca7c7"></a>

### `role`

```c
uint8_t bt_conn_info::role
```

连接角色（Connection Role）。

<a id="ad622c69f262ee53ec94918857250a2a0"></a>

### `sco`

```c
struct bt_conn_sco_info bt_conn_info::sco
```

同步面向连接链路专用信息（SCO Connection specific Info）。

<a id="ae4405f1b4f3fe2ff6253453964860931"></a>

### `security`

```c
struct bt_security_info bt_conn_info::security
```

安全专用信息（Security specific info）。

<a id="ae566e2382b69ff27314dc1dd632dbdbc"></a>

### `state`

```c
enum bt_conn_state bt_conn_info::state
```

连接状态（Connection state）。

<a id="a7995e1291be494b5bdf860eceea0cad1"></a>

### `type`

```c
enum bt_conn_type bt_conn_info::type
```

连接类型（Connection Type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [bt_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab8dde20ae75b51f1e28dbeed06001f20)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn_le_info](P023_bt_conn_le_info_结构体.md)
- [bt_conn_br_info](P006_bt_conn_br_info_结构体.md)
- [bt_conn_sco_info](P040_bt_conn_sco_info_结构体.md)
- [bt_conn_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9442c1479db60e2db40a2ea6de565282)
- [bt_security_info](P130_bt_security_info_结构体.md)
- [bt_conn_info](P009_bt_conn_info_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_bt_conn_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_bt_conn_le_conn_rate_changed_结构体.md)
