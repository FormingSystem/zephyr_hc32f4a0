---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-98
title: bt_l2cap_br_echo_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__echo__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第98章\_bt\_l2cap\_br\_echo\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__echo__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

回显（ECHO）请求/响应的回调结构。

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

<a id="details"></a>

回显（ECHO）请求/响应回调结构体。此结构体用于跟踪 L2CAP BR 的 ECHO 请求/响应信令包，通过 `bt_l2cap_br_echo_cb_register()` API 注册。如果应用中的不同模块都希望跟踪 ECHO 请求/响应信令包，可以注册此 `bt_l2cap_br_echo_cb` 类型的多个实例。若某个实例不关心某项回调，可将其设为 `NULL`，该实例便不会使用此回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 98.1\_数据成员（Data Fields）

<a id="r_abc56aa16213b05fb9d330e4b0147066b"></a>

```c
void(* req )(struct bt_conn *conn, uint8_t identifier, struct net_buf *buf)
```

相关声明：[req](#abc56aa16213b05fb9d330e4b0147066b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到 ECHO 请求。

<a id="r_aee34c139bbfb03796aa162bf31687d6c"></a>

```c
void(* rsp )(struct bt_conn *conn, struct net_buf *buf)
```

相关声明：[rsp](#aee34c139bbfb03796aa162bf31687d6c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到 ECHO 响应。

## 98.2\_详细说明（Detailed Documentation）

<a id="abc56aa16213b05fb9d330e4b0147066b"></a>

### `req`

```c
void(* bt_l2cap_br_echo_cb::req) (struct bt_conn *conn, uint8_t identifier, struct net_buf *buf)
```

已收到 ECHO 请求。

此回调通知应用已收到 ECHO 请求。应调用 `bt_l2cap_br_echo_rsp()` API 发送 ECHO 响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接对象。 |
| `identifier` | ECHO 请求的标识符。 |
| `buf` | 收到的 ECHO 数据。 |

<a id="aee34c139bbfb03796aa162bf31687d6c"></a>

### `rsp`

```c
void(* bt_l2cap_br_echo_cb::rsp) (struct bt_conn *conn, struct net_buf *buf)
```

已收到 ECHO 响应。

此回调通知应用已收到 ECHO 响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接对象。 |
| `buf` | 收到的 ECHO 数据。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/l2cap_br.h`

## 98.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/l2cap_br.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap__br_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_l2cap_br_echo_cb_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga62c0115185f5026c1a842848dc5336ce)
- [bt_l2cap_br_echo_cb](P098_bt_l2cap_br_echo_cb_结构体.md)
- [bt_l2cap_br_echo_rsp()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga8ebf537cc7e4c0a68a320f9c65c94b05)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P097_bt_l2cap_br_connless_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P099_bt_l2cap_br_endpoint_结构体.md)
