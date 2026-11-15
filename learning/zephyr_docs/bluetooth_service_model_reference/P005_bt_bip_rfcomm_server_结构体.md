---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-5
title: bt_bip_rfcomm_server_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__rfcomm__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_bt\_bip\_rfcomm\_server\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__rfcomm__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BIP 的 RFCOMM 服务器结构体。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

<a id="details"></a>

基本成像规范串口仿真协议服务器结构（BIP RFCOMM server structure）。表示使用 RFCOMM 传输的 BIP 服务器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a40ec65e156c02ad06b55aa1fc594ca71"></a>

```c
struct bt_goep_transport_rfcomm_server server
```

相关声明：[bt_goep_transport_rfcomm_server](P074_bt_goep_transport_rfcomm_server_结构体.md)、[server](#a40ec65e156c02ad06b55aa1fc594ca71)。

底层通用对象交换规范串口仿真协议服务器（GOEP RFCOMM server）。

<a id="r_ad7b714b584c18e41feb7385819c50511"></a>

```c
int(* accept )(struct bt_conn *conn, struct bt_bip_rfcomm_server *server, struct bt_bip **bip)
```

相关声明：[accept](#ad7b714b584c18e41feb7385819c50511)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bip_rfcomm_server](P005_bt_bip_rfcomm_server_结构体.md)、[server](#a40ec65e156c02ad06b55aa1fc594ca71)、[bt_bip](P001_bt_bip_结构体.md)。

接受连接回调（Accept connection callback）。

## 5.2\_详细说明（Detailed Documentation）

<a id="ad7b714b584c18e41feb7385819c50511"></a>

### `accept`

```c
int(* bt_bip_rfcomm_server::accept) (struct bt_conn *conn, struct bt_bip_rfcomm_server *server, struct bt_bip **bip)
```

接受连接回调（Accept connection callback）。

接受新的串口仿真协议连接（RFCOMM connection）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接（Bluetooth Connection）。 |
| `server` | 串口仿真协议服务器实例（RFCOMM server instance）。 |
| `bip` | 用于存放新建基本成像规范实例（BIP instance）的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="a40ec65e156c02ad06b55aa1fc594ca71"></a>

### `server`

```c
struct bt_goep_transport_rfcomm_server bt_bip_rfcomm_server::server
```

底层通用对象交换规范串口仿真协议服务器（GOEP RFCOMM server）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/bip.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/bip.h](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h_source.html)
- [bt_goep_transport_rfcomm_server](P074_bt_goep_transport_rfcomm_server_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_bip_rfcomm_server](P005_bt_bip_rfcomm_server_结构体.md)
- [bt_bip](P001_bt_bip_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_bt_bip_l2cap_server_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_bt_bip_server_结构体.md)
