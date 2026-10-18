---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-104
title: bt_le_ext_adv_connected_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__connected__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第104章\_bt\_le\_ext\_adv\_connected\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__connected__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

广播连接事件（Advertising Connected Event）的信息。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

广播连接事件信息（Advertising connected event information）。注意（Note）：用于 `bt_le_ext_adv_cb`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 104.1\_数据成员（Data Fields）

<a id="r_a157efa6206b418f768582107c566fde2"></a>

```c
struct bt_conn * conn
```

相关声明：[bt_conn](P002_bt_conn_结构体.md)、[conn](#a157efa6206b418f768582107c566fde2)。

新连接的连接对象（Connection object）。

## 104.2\_详细说明（Detailed Documentation）

<a id="a157efa6206b418f768582107c566fde2"></a>

### `conn`

```c
struct bt_conn* bt_le_ext_adv_connected_info::conn
```

新连接的连接对象（Connection object）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 104.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_conn](P002_bt_conn_结构体.md)
- [bt_le_ext_adv_cb](P103_bt_le_ext_adv_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P103_bt_le_ext_adv_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P105_bt_le_ext_adv_info_结构体.md)
