---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-11
title: bt_mesh_blob_srv_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__srv__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_bt\_mesh\_blob\_srv\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__srv__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BLOB传输服务器（BLOB Transfer Server）模型的事件处理程序。

```c
#include <zephyr/bluetooth/mesh/blob_srv.h>
```

<a id="details"></a>

二进制大对象传输服务器模型（BLOB Transfer Server model）的事件处理函数。所有回调均为可选。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_aad5ab6e396f049a3b8a239e9f0d1c063"></a>

```c
int(* start )(struct bt_mesh_blob_srv *srv, struct bt_mesh_msg_ctx *ctx, struct bt_mesh_blob_xfer *xfer)
```

相关声明：[start](#aad5ab6e396f049a3b8a239e9f0d1c063)、[bt_mesh_blob_srv](P009_bt_mesh_blob_srv_结构体.md)、[bt_mesh_msg_ctx](P082_bt_mesh_msg_ctx_结构体.md)、[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)。

传输开始回调（Transfer start callback）。

<a id="r_af7b6f557f38c15a174a2a75d1210dab3"></a>

```c
void(* end )(struct bt_mesh_blob_srv *srv, uint64_t id, bool success)
```

相关声明：[end](#af7b6f557f38c15a174a2a75d1210dab3)、[bt_mesh_blob_srv](P009_bt_mesh_blob_srv_结构体.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

传输结束回调（Transfer end callback）。

<a id="r_a99a054d410f0a82101b15309a8f4ec33"></a>

```c
void(* suspended )(struct bt_mesh_blob_srv *srv)
```

相关声明：[suspended](#a99a054d410f0a82101b15309a8f4ec33)、[bt_mesh_blob_srv](P009_bt_mesh_blob_srv_结构体.md)。

传输挂起回调（Transfer suspended callback）。

<a id="r_ae032ff1d52f46f1716451dc5ff138d0f"></a>

```c
void(* resume )(struct bt_mesh_blob_srv *srv)
```

相关声明：[resume](#ae032ff1d52f46f1716451dc5ff138d0f)、[bt_mesh_blob_srv](P009_bt_mesh_blob_srv_结构体.md)。

传输恢复回调（Transfer resume callback）。

<a id="r_a94b56462c5fd95535a5f1e0ba2ddf99a"></a>

```c
int(* recover )(struct bt_mesh_blob_srv *srv, struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_io **io)
```

相关声明：[recover](#a94b56462c5fd95535a5f1e0ba2ddf99a)、[bt_mesh_blob_srv](P009_bt_mesh_blob_srv_结构体.md)、[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)、[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)。

传输恢复处理回调（Transfer recovery callback）。

## 11.2\_详细说明（Detailed Documentation）

<a id="af7b6f557f38c15a174a2a75d1210dab3"></a>

### `end`

```c
void(* bt_mesh_blob_srv_cb::end) (struct bt_mesh_blob_srv *srv, uint64_t id, bool success)
```

传输结束回调（Transfer end callback）。

传输结束时调用，无论是取消还是成功完成。此时可以准备新的传输（Transfer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 二进制大对象传输服务器实例（BLOB Transfer Server instance）。 |
| `id` | 被取消传输的二进制大对象标识符（BLOB ID）。 |
| `success` | 传输是否成功（Transfer successful）。 |

**说明（Note）**：注意（Note）：若开始参数无效，传输可能尚未开始就已结束。

<a id="a94b56462c5fd95535a5f1e0ba2ddf99a"></a>

### `recover`

```c
int(* bt_mesh_blob_srv_cb::recover) (struct bt_mesh_blob_srv *srv, struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_io **io)
```

传输恢复处理回调（Transfer recovery callback）。

若设备在传输中途重启，则在蓝牙 Mesh 子系统（Bluetooth Mesh subsystem）启动时调用。

如果未定义此回调，重启后不会恢复传输（Transfer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 二进制大对象传输服务器实例（BLOB Transfer Server instance）。 |
| `xfer` | 要恢复的传输（Transfer to resume）。 |
| `io` | 用于返回二进制大对象流（BLOB stream）的参数。回调必须将其设置为有效的 BLOB 流。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；返回负错误码表示放弃传输。

<a id="ae032ff1d52f46f1716451dc5ff138d0f"></a>

### `resume`

```c
void(* bt_mesh_blob_srv_cb::resume) (struct bt_mesh_blob_srv *srv)
```

传输恢复回调（Transfer resume callback）。

挂起的传输恢复（Resumed）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 二进制大对象传输服务器实例（BLOB Transfer Server instance）。 |

<a id="aad5ab6e396f049a3b8a239e9f0d1c063"></a>

### `start`

```c
int(* bt_mesh_blob_srv_cb::start) (struct bt_mesh_blob_srv *srv, struct bt_mesh_msg_ctx *ctx, struct bt_mesh_blob_xfer *xfer)
```

传输开始回调（Transfer start callback）。

使用预先准备的二进制大对象标识符（BLOB ID）开始传输时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 二进制大对象传输服务器实例（BLOB Transfer Server instance）。 |
| `ctx` | 传入的开始消息的消息上下文（Message context）。整个传输均从同一个源地址发送。 |
| `xfer` | 传输参数（Transfer parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；返回负错误码表示拒绝传输。

<a id="a99a054d410f0a82101b15309a8f4ec33"></a>

### `suspended`

```c
void(* bt_mesh_blob_srv_cb::suspended) (struct bt_mesh_blob_srv *srv)
```

传输挂起回调（Transfer suspended callback）。

服务器（Server）等待传输数据包超时时调用。挂起的传输以后可能从当前块（Block）的起始处恢复。当前块中已接收的所有分片（Chunks）都应丢弃，因为恢复传输时会再次接收它们。

恢复传输时会再次调用 `resumed`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 二进制大对象传输服务器实例（BLOB Transfer Server instance）。 |

**说明（Note）**：注意（Note）：二进制大对象传输服务器（BLOB Transfer Server）在挂起状态不运行定时器，由应用决定是否永久取消传输。若应用不干预，传输将无限期挂起，BLOB 传输服务器也不会接受任何新传输。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob_srv.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h_source.html)
- [bt_mesh_blob_srv](P009_bt_mesh_blob_srv_结构体.md)
- [bt_mesh_msg_ctx](P082_bt_mesh_msg_ctx_结构体.md)
- [bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_bt_mesh_blob_target_结构体.md)
