---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-73
title: bt_goep_transport_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_bt\_goep\_transport\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport__ops.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GOEP 传输操作（Transport Operations）结构体。

```c
#include <zephyr/bluetooth/classic/goep.h>
```

<a id="details"></a>

通用对象交换规范传输操作结构（GOEP transport operations structure）。对象必须在 GOEP 服务器与客户端的整个生命周期内保持有效且不变。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 73.1\_数据成员（Data Fields）

<a id="r_a46068be01ea341e1b74163bea0003e2e"></a>

```c
void(* connected )(struct bt_conn *conn, struct bt_goep *goep)
```

相关声明：[connected](#a46068be01ea341e1b74163bea0003e2e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_goep](P070_bt_goep_结构体.md)。

通用对象交换规范传输连接回调（GOEP transport connected callback）。

<a id="r_a5f8ce2be1a4c87f4e36d47dcc3aa6f3c"></a>

```c
void(* disconnected )(struct bt_goep *goep)
```

相关声明：[disconnected](#a5f8ce2be1a4c87f4e36d47dcc3aa6f3c)、[bt_goep](P070_bt_goep_结构体.md)。

通用对象交换规范传输断开回调（GOEP transport disconnected callback）。

## 73.2\_详细说明（Detailed Documentation）

<a id="a46068be01ea341e1b74163bea0003e2e"></a>

### `connected`

```c
void(* bt_goep_transport_ops::connected) (struct bt_conn *conn, struct bt_goep *goep)
```

通用对象交换规范传输连接回调（GOEP transport connected callback）。

提供此回调后，每次通用对象交换规范传输连接（GOEP transport connection）完成都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步面向连接链路连接（ACL connection）。 |
| `goep` | 已连接的通用对象交换规范对象（GOEP object）。 |

<a id="a5f8ce2be1a4c87f4e36d47dcc3aa6f3c"></a>

### `disconnected`

```c
void(* bt_goep_transport_ops::disconnected) (struct bt_goep *goep)
```

通用对象交换规范传输断开回调（GOEP transport disconnected callback）。

提供此回调后，每次通用对象交换规范传输（GOEP transport）断开都会调用，包括连接被拒绝的情况。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `goep` | 已断开的通用对象交换规范对象（GOEP object）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/goep.h`

## 73.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_goep](P070_bt_goep_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P072_bt_goep_transport_l2cap_server_结构体.md) · [返回大纲](大纲.md) · [下一章](P074_bt_goep_transport_rfcomm_server_结构体.md)
