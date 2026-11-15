---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-95
title: bt_ias_client_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ias__client__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第95章\_bt\_ias\_client\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ias__client__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/services/ias.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 95.1\_数据成员（Data Fields）

<a id="r_a325ad34a67f9d9948740eb87862945b7"></a>

```c
void(* discover )(struct bt_conn *conn, int err)
```

相关声明：[discover](#a325ad34a67f9d9948740eb87862945b7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

`bt_ias_discover` 的回调函数。

## 95.2\_详细说明（Detailed Documentation）

<a id="a325ad34a67f9d9948740eb87862945b7"></a>

### `discover`

```c
void(* bt_ias_client_cb::discover) (struct bt_conn *conn, int err)
```

`bt_ias_discover` 的回调函数。

发现过程（Discovery procedure）完成时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `err` | 成功时为 `0`，否则为属性协议错误（ATT error）或负的错误编号（errno）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ias.h`

## 95.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ias.h](https://docs.zephyrproject.org/latest/doxygen/html/ias_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P094_bt_ias_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P096_bt_l2cap_br_chan_结构体.md)
