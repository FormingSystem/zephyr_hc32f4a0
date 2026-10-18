---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-101
title: bt_l2cap_chan_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__chan.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第101章\_bt\_l2cap\_chan\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__chan.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

逻辑链路控制与适配协议（L2CAP）的信道结构。

```c
#include <zephyr/bluetooth/l2cap.h>
```

<a id="details"></a>

逻辑链路控制与适配协议（L2CAP）的信道结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 101.1\_数据成员（Data Fields）

<a id="r_a007a7ef11a00c0dff22cd64961260d3d"></a>

```c
struct bt_conn * conn
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[conn](#a007a7ef11a00c0dff22cd64961260d3d)。

通道连接引用（Channel connection reference）。

<a id="r_a3e370744f17ca4cff200cc0a2ee1a74b"></a>

```c
const struct bt_l2cap_chan_ops * ops
```

相关声明：[bt_l2cap_chan_ops](P102_bt_l2cap_chan_ops_结构体.md)、[ops](#a3e370744f17ca4cff200cc0a2ee1a74b)。

通道操作引用（Channel operations reference）。

<a id="r_a123ae4bb1db6f4b41561b3d4691b1c02"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a123ae4bb1db6f4b41561b3d4691b1c02)。

<a id="r_ac0fbde11b35e0b6b424970e73c945a40"></a>

```c
bt_l2cap_chan_destroy_t destroy
```

相关声明：[bt_l2cap_chan_destroy_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga88baae9c159f3de4ccb34fd0e3cc8c3b)、[destroy](#ac0fbde11b35e0b6b424970e73c945a40)。

<a id="r_a7603e2c212e0522a1ffca2198224a994"></a>

```c
atomic_t status [ATOMIC_BITMAP_SIZE(BT_L2CAP_NUM_STATUS)]
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[status](#a7603e2c212e0522a1ffca2198224a994)、[ATOMIC_BITMAP_SIZE](../atomic_reference/P001_原子操作公共接口.md#gafac28874aaad3bcec72c693186e988cb)、[BT_L2CAP_NUM_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c)。

## 101.2\_详细说明（Detailed Documentation）

<a id="a007a7ef11a00c0dff22cd64961260d3d"></a>

### `conn`

```c
struct bt_conn* bt_l2cap_chan::conn
```

通道连接引用（Channel connection reference）。

<a id="ac0fbde11b35e0b6b424970e73c945a40"></a>

### `destroy`

```c
bt_l2cap_chan_destroy_t bt_l2cap_chan::destroy
```

<a id="a123ae4bb1db6f4b41561b3d4691b1c02"></a>

### `node`

```c
sys_snode_t bt_l2cap_chan::node
```

<a id="a3e370744f17ca4cff200cc0a2ee1a74b"></a>

### `ops`

```c
const struct bt_l2cap_chan_ops* bt_l2cap_chan::ops
```

通道操作引用（Channel operations reference）。

<a id="a7603e2c212e0522a1ffca2198224a994"></a>

### `status`

```c
atomic_t bt_l2cap_chan::status[ATOMIC_BITMAP_SIZE(BT_L2CAP_NUM_STATUS)]
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/l2cap.h`

## 101.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_l2cap_chan_ops](P102_bt_l2cap_chan_ops_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_l2cap_chan_destroy_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga88baae9c159f3de4ccb34fd0e3cc8c3b)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [ATOMIC_BITMAP_SIZE](../atomic_reference/P001_原子操作公共接口.md#gafac28874aaad3bcec72c693186e988cb)
- [BT_L2CAP_NUM_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P100_bt_l2cap_br_window_结构体.md) · [返回大纲](大纲.md) · [下一章](P102_bt_l2cap_chan_ops_结构体.md)
