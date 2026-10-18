---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-158
title: bt_rfcomm_server_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__rfcomm__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第158章\_bt\_rfcomm\_server\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__rfcomm__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 158.1\_数据成员（Data Fields）

<a id="r_a30b22ea64c0fdd7130e8aaa79519e776"></a>

```c
uint8_t channel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](#a30b22ea64c0fdd7130e8aaa79519e776)。

服务器通道（Server Channel）。

<a id="r_ac08708bb8161f787737962f62d3c003f"></a>

```c
int(* accept )(struct bt_conn *conn, struct bt_rfcomm_server *server, struct bt_rfcomm_dlc **dlc)
```

相关声明：[accept](#ac08708bb8161f787737962f62d3c003f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_rfcomm_server](P158_bt_rfcomm_server_结构体.md)、[bt_rfcomm_dlc](P155_bt_rfcomm_dlc_结构体.md)。

服务器接受回调（Server accept callback）。

## 158.2\_详细说明（Detailed Documentation）

<a id="ac08708bb8161f787737962f62d3c003f"></a>

### `accept`

```c
int(* bt_rfcomm_server::accept) (struct bt_conn *conn, struct bt_rfcomm_server *server, struct bt_rfcomm_dlc **dlc)
```

服务器接受回调（Server accept callback）。

每当新的传入连接需要授权（Authorization）时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 请求授权（Authorization）的连接。 |
| `server` | 指向与此回调对应的服务器结构（Server structure）的指针。 |
| `dlc` | 用于接收所分配 DLC 的指针。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a30b22ea64c0fdd7130e8aaa79519e776"></a>

### `channel`

```c
uint8_t bt_rfcomm_server::channel
```

服务器通道（Server Channel）。

可能的取值：0——调用 `bt_rfcomm_server_register()` 时自动分配动态值。

`0x01` 至 `0x1e`：动态分配。应用可在服务器注册前预先设置，但不建议这样做；如果传入 0，则由协议栈自动分配。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/rfcomm.h`

## 158.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/rfcomm.h](https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_rfcomm_server](P158_bt_rfcomm_server_结构体.md)
- [bt_rfcomm_dlc](P155_bt_rfcomm_dlc_结构体.md)
- [bt_rfcomm_server_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gafd0ffcff41e233f74dc2726e889f5401)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P157_bt_rfcomm_rpn_结构体.md) · [返回大纲](大纲.md) · [下一章](P159_bt_sdp_attr_value_结构体.md)
