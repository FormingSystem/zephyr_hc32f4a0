---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-153
title: bt_pbap_pse_l2cap_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__pbap__pse__l2cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第153章\_bt\_pbap\_pse\_l2cap\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__pbap__pse__l2cap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电话簿访问配置文件（PBAP）的PSE L2CAP服务器结构。

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

<a id="details"></a>

PBAP PSE L2CAP 服务器结构体，用于管理通过 L2CAP 传输运行的 PBAP 服务器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 153.1\_数据成员（Data Fields）

<a id="r_ae6342b794786c14db63503a9d0ce2e48"></a>

```c
struct bt_goep_transport_l2cap_server server
```

相关声明：[bt_goep_transport_l2cap_server](P072_bt_goep_transport_l2cap_server_结构体.md)、[server](#ae6342b794786c14db63503a9d0ce2e48)。

底层通用对象交换规范逻辑链路控制与适配协议服务器（GOEP L2CAP server）。

<a id="r_a34e91052e02e8d9e043093cffd207157"></a>

```c
int(* accept )(struct bt_conn *conn, struct bt_pbap_pse_l2cap *pbap_pse_l2cap, struct bt_pbap_pse **pbap_pse)
```

相关声明：[accept](#a34e91052e02e8d9e043093cffd207157)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_pbap_pse_l2cap](P153_bt_pbap_pse_l2cap_结构体.md)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)。

接受连接回调（Accept connection callback）。

## 153.2\_详细说明（Detailed Documentation）

<a id="a34e91052e02e8d9e043093cffd207157"></a>

### `accept`

```c
int(* bt_pbap_pse_l2cap::accept) (struct bt_conn *conn, struct bt_pbap_pse_l2cap *pbap_pse_l2cap, struct bt_pbap_pse **pbap_pse)
```

接受连接回调（Accept connection callback）。

接受新的 L2CAP 连接时调用。应用应分配并初始化 PBAP PSE 实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接。 |
| `pbap_pse_l2cap` | PBAP PSE L2CAP 服务器实例，类型为 `bt_pbap_pse_l2cap`。 |
| `pbap_pse` | 用于保存已创建 PBAP PSE 实例的指针，实例类型为 `bt_pbap_pse`。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ae6342b794786c14db63503a9d0ce2e48"></a>

### `server`

```c
struct bt_goep_transport_l2cap_server bt_pbap_pse_l2cap::server
```

底层通用对象交换规范逻辑链路控制与适配协议服务器（GOEP L2CAP server）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/pbap.h`

## 153.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/pbap.h](https://docs.zephyrproject.org/latest/doxygen/html/pbap_8h_source.html)
- [bt_goep_transport_l2cap_server](P072_bt_goep_transport_l2cap_server_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_pbap_pse_l2cap](P153_bt_pbap_pse_l2cap_结构体.md)
- [bt_pbap_pse](P151_bt_pbap_pse_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P152_bt_pbap_pse_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P154_bt_pbap_pse_rfcomm_结构体.md)
