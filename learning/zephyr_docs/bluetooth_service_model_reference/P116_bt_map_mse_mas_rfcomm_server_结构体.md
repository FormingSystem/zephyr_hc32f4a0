---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-116
title: bt_map_mse_mas_rfcomm_server_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mse__mas__rfcomm__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第116章\_bt\_map\_mse\_mas\_rfcomm\_server\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mse__mas__rfcomm__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息访问配置文件（MAP）服务器的MAS RFCOMM服务器。

```c
#include <zephyr/bluetooth/classic/map.h>
```

<a id="details"></a>

MAP 服务器 MAS 的 RFCOMM 服务器。此结构体表示用于 MAP 服务器 MAS 的 RFCOMM 服务器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 116.1\_数据成员（Data Fields）

<a id="r_ac3cc9b87f871e4bb2c188244e1c41fe0"></a>

```c
struct bt_goep_transport_rfcomm_server server
```

相关声明：[bt_goep_transport_rfcomm_server](P074_bt_goep_transport_rfcomm_server_结构体.md)、[server](#ac3cc9b87f871e4bb2c188244e1c41fe0)。

通用对象交换规范（GOEP）的 RFCOMM 传输服务器，即底层传输层。

<a id="r_a0890ac5bf7b837818c03af77ac64ff09"></a>

```c
int(* accept )(struct bt_conn *conn, struct bt_map_mse_mas_rfcomm_server *server, struct bt_map_mse_mas **mse_mas)
```

相关声明：[accept](#a0890ac5bf7b837818c03af77ac64ff09)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mse_mas_rfcomm_server](P116_bt_map_mse_mas_rfcomm_server_结构体.md)、[server](#ac3cc9b87f871e4bb2c188244e1c41fe0)、[bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)。

接受入站连接的回调。

## 116.2\_详细说明（Detailed Documentation）

<a id="a0890ac5bf7b837818c03af77ac64ff09"></a>

### `accept`

```c
int(* bt_map_mse_mas_rfcomm_server::accept) (struct bt_conn *conn, struct bt_map_mse_mas_rfcomm_server *server, struct bt_map_mse_mas **mse_mas)
```

接受入站连接的回调。

远端 MCE 尝试连接到 MAS 服务器时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `server` | 接收入站连接的 RFCOMM 服务器实例。 |
| `mse_mas` | 用于保存所分配 MAS 实例的输出参数。 |

**返回（Returns）**：返回值：成功时返回 0；返回负值错误码表示拒绝连接。

<a id="ac3cc9b87f871e4bb2c188244e1c41fe0"></a>

### `server`

```c
struct bt_goep_transport_rfcomm_server bt_map_mse_mas_rfcomm_server::server
```

通用对象交换规范（GOEP）的 RFCOMM 传输服务器，即底层传输层。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/map.h`

## 116.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h_source.html)
- [bt_goep_transport_rfcomm_server](P074_bt_goep_transport_rfcomm_server_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_map_mse_mas_rfcomm_server](P116_bt_map_mse_mas_rfcomm_server_结构体.md)
- [bt_map_mse_mas](P113_bt_map_mse_mas_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P115_bt_map_mse_mas_l2cap_server_结构体.md) · [返回大纲](大纲.md) · [下一章](P117_bt_map_mse_mns_结构体.md)
