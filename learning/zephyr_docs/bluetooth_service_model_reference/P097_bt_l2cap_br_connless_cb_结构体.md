---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-97
title: bt_l2cap_br_connless_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__connless__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第97章\_bt\_l2cap\_br\_connless\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__connless__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

无连接数据信道（Connectionless Data Channel）的回调结构。

```c
#include <zephyr/bluetooth/classic/l2cap_br.h>
```

<a id="details"></a>

无连接数据通道（connectionless data channel）回调结构体。此结构体用于跟踪无连接数据通道帧，通过 `bt_l2cap_br_connless_register()` API 注册。如果应用中的不同模块都希望跟踪无连接数据通道帧，可以注册此 `bt_l2cap_br_connless_cb` 类型的多个实例。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 97.1\_数据成员（Data Fields）

<a id="r_a57be5b79d581d1acb5b5c59091fad5fa"></a>

```c
uint16_t psm
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[psm](#a57be5b79d581d1acb5b5c59091fad5fa)。

注册的协议/服务复用器（PSM）。

<a id="r_ab4deccfa24dd5ea61ac390d0dec0cdbf"></a>

```c
bt_security_t sec_level
```

相关声明：[bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)、[sec_level](#ab4deccfa24dd5ea61ac390d0dec0cdbf)。

所需的最低安全级别（security level）。

<a id="r_a2fd9c68c6689c7748f72925cae1ab343"></a>

```c
void(* recv )(struct bt_conn *conn, uint16_t psm, struct net_buf *buf)
```

相关声明：[recv](#a2fd9c68c6689c7748f72925cae1ab343)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[psm](#a57be5b79d581d1acb5b5c59091fad5fa)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到无连接通道数据。

## 97.2\_详细说明（Detailed Documentation）

<a id="a57be5b79d581d1acb5b5c59091fad5fa"></a>

### `psm`

```c
uint16_t bt_l2cap_br_connless_cb::psm
```

注册的协议/服务复用器（PSM）。

对于基本速率（BR），可能的取值如下：

PSM 字段至少占两个八位字节。所有 PSM 值都必须满足：最高有效八位字节的最低有效位为 0，其他所有八位字节的最低有效位为 1。

0：通知所有无连接数据通道帧。

`0x0001` 至 `0x0eff`：由蓝牙技术联盟（Bluetooth SIG）分配的标准固定值。

<a id="a2fd9c68c6689c7748f72925cae1ab343"></a>

### `recv`

```c
void(* bt_l2cap_br_connless_cb::recv) (struct bt_conn *conn, uint16_t psm, struct net_buf *buf)
```

已收到无连接通道数据。

此回调通知应用已收到无连接通道数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接对象。 |
| `psm` | 协议/服务复用器（Protocol/Service Multiplexer，PSM）。 |
| `buf` | 收到的无连接通道数据。 |

<a id="ab4deccfa24dd5ea61ac390d0dec0cdbf"></a>

### `sec_level`

```c
bt_security_t bt_l2cap_br_connless_cb::sec_level
```

所需的最低安全级别（security level）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/l2cap_br.h`

## 97.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/l2cap_br.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap__br_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_l2cap_br_connless_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gad1b4d59a8849124518bb973233b3f362)
- [bt_l2cap_br_connless_cb](P097_bt_l2cap_br_connless_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P096_bt_l2cap_br_chan_结构体.md) · [返回大纲](大纲.md) · [下一章](P098_bt_l2cap_br_echo_cb_结构体.md)
