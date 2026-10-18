---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-106
title: bt_l2cap_server_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第106章\_bt\_l2cap\_server\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

L2CAP服务器（Server）结构。

```c
#include <zephyr/bluetooth/l2cap.h>
```

<a id="details"></a>

L2CAP服务器（Server）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 106.1\_数据成员（Data Fields）

<a id="r_a07925dda8566ee7518b1809725e1b110"></a>

```c
uint16_t psm
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[psm](#a07925dda8566ee7518b1809725e1b110)。

服务器的协议/服务复用器（PSM）。

<a id="r_a9f082abf679a397264a7b51fa4400852"></a>

```c
bt_security_t sec_level
```

相关声明：[bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)、[sec_level](#a9f082abf679a397264a7b51fa4400852)。

所需的最低安全级别（security level）。

<a id="r_ad31a1908f7dc733f9497164ccabba2af"></a>

```c
int(* accept )(struct bt_conn *conn, struct bt_l2cap_server *server, struct bt_l2cap_chan **chan)
```

相关声明：[accept](#ad31a1908f7dc733f9497164ccabba2af)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_l2cap_server](P106_bt_l2cap_server_结构体.md)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)。

服务器接受回调（Server accept callback）。

<a id="r_a76b478140d6a57038eb389eac91442c0"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a76b478140d6a57038eb389eac91442c0)。

## 106.2\_详细说明（Detailed Documentation）

<a id="ad31a1908f7dc733f9497164ccabba2af"></a>

### `accept`

```c
int(* bt_l2cap_server::accept) (struct bt_conn *conn, struct bt_l2cap_server *server, struct bt_l2cap_chan **chan)
```

服务器接受回调（Server accept callback）。

每当新的入站连接需要授权时，都会调用此回调。如果接受连接，回调应分配一个零初始化的通道对象，并更新通道引用 `chan`，使其指向该对象的通用成员：对于通过 `bt_l2cap_server_register()` 注册的服务器，对象必须是 `bt_l2cap_le_chan` 类型，且 `chan` 必须指向其 `bt_l2cap_le_chan::chan` 成员；对于通过 `bt_l2cap_br_server_register()` 注册的服务器，对象必须是 `bt_l2cap_br_chan` 类型，且 `chan` 必须指向其 `bt_l2cap_br_chan::chan` 成员。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 请求授权（Authorization）的连接。 |
| `server` | 指向与此回调对应的服务器结构（Server structure）的指针。 |
| `chan` | 用于接收所分配通道的指针。 |

**警告（Warning）**：警告：虽然通过 `chan` 传回的引用类型是 `bt_l2cap_chan`，但如上所述，它必须是某个 `bt_l2cap_le_chan` 或 `bt_l2cap_br_chan` 对象的成员。协议栈会使用包含它的对象，因此返回一个独立的 `bt_l2cap_chan` 会导致越界访问。此回调负责将包含该成员的对象清零。

**返回（Returns）**：返回值：成功时返回 0，错误时返回负值。没有空间可用于新通道时返回 `-ENOMEM`；应用未授权连接时返回 `-EACCES`；加密密钥长度过短时返回 `-EPERM`。

<a id="a76b478140d6a57038eb389eac91442c0"></a>

### `node`

```c
sys_snode_t bt_l2cap_server::node
```

<a id="a07925dda8566ee7518b1809725e1b110"></a>

### `psm`

```c
uint16_t bt_l2cap_server::psm
```

服务器的协议/服务复用器（PSM）。

对于低功耗（LE），可能的取值如下：0——调用 `bt_l2cap_server_register()` 时自动分配动态值。

`0x0001` 至 `0x007f`：由蓝牙技术联盟（Bluetooth SIG）分配的标准固定值。

`0x0080` 至 `0x00ff`：动态分配。应用可在服务器注册前预先设置，但不建议这样做；如果应用将值设为 0，则由协议栈自动分配。

对于基本速率（BR），可能的取值如下：

PSM 字段至少占两个八位字节。所有 PSM 值都必须满足：最高有效八位字节的最低有效位为 0，其他所有八位字节的最低有效位为 1。

0：调用 `bt_l2cap_br_server_register()` 时自动分配动态值。

`0x0001` 至 `0x0eff`：由蓝牙技术联盟（Bluetooth SIG）分配的标准固定值。

<a id="a9f082abf679a397264a7b51fa4400852"></a>

### `sec_level`

```c
bt_security_t bt_l2cap_server::sec_level
```

所需的最低安全级别（security level）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/l2cap.h`

## 106.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_l2cap_server](P106_bt_l2cap_server_结构体.md)
- [bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_l2cap_server_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga1a5e8c81c086872d7fb8da5329f982c6)
- [bt_l2cap_le_chan](P104_bt_l2cap_le_chan_结构体.md)
- [bt_l2cap_le_chan::chan](P104_bt_l2cap_le_chan_结构体.md#a980126cabc3824ab623d634d91f7d761)
- [bt_l2cap_br_server_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga5b0ae2abd714f46e6bb2394bce33e613)
- [bt_l2cap_br_chan](P096_bt_l2cap_br_chan_结构体.md)
- [bt_l2cap_br_chan::chan](P096_bt_l2cap_br_chan_结构体.md#a28ed2b2541697390c325c706d4ad8f0b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P105_bt_l2cap_le_endpoint_结构体.md) · [返回大纲](大纲.md) · [下一章](P107_bt_map_mce_mas_结构体.md)
