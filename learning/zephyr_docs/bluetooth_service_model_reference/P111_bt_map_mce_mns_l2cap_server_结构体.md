---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-111
title: bt_map_mce_mns_l2cap_server_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mce__mns__l2cap__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第111章\_bt\_map\_mce\_mns\_l2cap\_server\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mce__mns__l2cap__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息访问配置文件（MAP）客户端的MNS L2CAP服务器。

```c
#include <zephyr/bluetooth/classic/map.h>
```

<a id="details"></a>

MAP 客户端 MNS 的 L2CAP 服务器。此结构体表示用于 MAP 客户端 MNS 的 L2CAP 服务器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 111.1\_数据成员（Data Fields）

<a id="r_a53b201ac19eaced621ef2c3297e89392"></a>

```c
struct bt_goep_transport_l2cap_server server
```

相关声明：[bt_goep_transport_l2cap_server](P072_bt_goep_transport_l2cap_server_结构体.md)、[server](#a53b201ac19eaced621ef2c3297e89392)。

通用对象交换规范（GOEP）的 L2CAP 传输服务器，即底层传输层。

<a id="r_afb98a55954ef0892f107a5920aa5ad2c"></a>

```c
int(* accept )(struct bt_conn *conn, struct bt_map_mce_mns_l2cap_server *server, struct bt_map_mce_mns **mce_mns)
```

相关声明：[accept](#afb98a55954ef0892f107a5920aa5ad2c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mce_mns_l2cap_server](P111_bt_map_mce_mns_l2cap_server_结构体.md)、[server](#a53b201ac19eaced621ef2c3297e89392)、[bt_map_mce_mns](P109_bt_map_mce_mns_结构体.md)。

接受入站连接的回调。

## 111.2\_详细说明（Detailed Documentation）

<a id="afb98a55954ef0892f107a5920aa5ad2c"></a>

### `accept`

```c
int(* bt_map_mce_mns_l2cap_server::accept) (struct bt_conn *conn, struct bt_map_mce_mns_l2cap_server *server, struct bt_map_mce_mns **mce_mns)
```

接受入站连接的回调。

远端 MSE 尝试连接到 MNS 服务器时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `server` | 接收入站连接的 L2CAP 服务器实例。 |
| `mce_mns` | 用于保存所分配 MNS 实例的输出参数。 |

**返回（Returns）**：返回值：成功时返回 0；返回负值错误码表示拒绝连接。

<a id="a53b201ac19eaced621ef2c3297e89392"></a>

### `server`

```c
struct bt_goep_transport_l2cap_server bt_map_mce_mns_l2cap_server::server
```

通用对象交换规范（GOEP）的 L2CAP 传输服务器，即底层传输层。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/map.h`

## 111.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h_source.html)
- [bt_goep_transport_l2cap_server](P072_bt_goep_transport_l2cap_server_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_map_mce_mns_l2cap_server](P111_bt_map_mce_mns_l2cap_server_结构体.md)
- [bt_map_mce_mns](P109_bt_map_mce_mns_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P110_bt_map_mce_mns_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P112_bt_map_mce_mns_rfcomm_server_结构体.md)
