---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-134
title: bt_obex_transport_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__transport__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第134章\_bt\_obex\_transport\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__transport__ops.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象交换协议（OBEX）的传输操作结构。

```c
#include <zephyr/bluetooth/classic/obex.h>
```

<a id="details"></a>

OBEX 传输操作结构体。此对象必须在 OBEX 客户端或服务器的整个生命周期内保持有效且不变。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 134.1\_数据成员（Data Fields）

<a id="r_aa01998b13bdedcb0d35164dcf8b5a55e"></a>

```c
struct net_buf *(* alloc_buf )(struct bt_obex *obex, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[alloc_buf](#aa01998b13bdedcb0d35164dcf8b5a55e)、[bt_obex](P127_bt_obex_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

缓冲区分配（allocate buf）回调。

<a id="r_a2c04d635154acfa9f4579596d8ed7d79"></a>

```c
int(* send )(struct bt_obex *obex, struct net_buf *buf)
```

相关声明：[send](#a2c04d635154acfa9f4579596d8ed7d79)、[bt_obex](P127_bt_obex_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

通过传输层发送 OBEX 数据。

<a id="r_a57fc547e578a62e6ebb9da89e0ae423c"></a>

```c
int(* disconnect )(struct bt_obex *obex)
```

相关声明：[disconnect](#a57fc547e578a62e6ebb9da89e0ae423c)、[bt_obex](P127_bt_obex_结构体.md)。

断开传输层连接。

## 134.2\_详细说明（Detailed Documentation）

<a id="aa01998b13bdedcb0d35164dcf8b5a55e"></a>

### `alloc_buf`

```c
struct net_buf *(* bt_obex_transport_ops::alloc_buf) (struct bt_obex *obex, struct net_buf_pool *pool)
```

缓冲区分配（allocate buf）回调。

如果提供了此回调，将调用它分配网络缓冲区（net buffer），以保存待发送的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obex` | OBEX 对象。 |
| `pool` | 应从哪个缓冲池取得缓冲区。 |

**返回（Returns）**：返回值（Returns）：已分配的缓冲区（Allocated buffer）。

<a id="a57fc547e578a62e6ebb9da89e0ae423c"></a>

### `disconnect`

```c
int(* bt_obex_transport_ops::disconnect) (struct bt_obex *obex)
```

断开传输层连接。

如果提供了此回调，将调用它断开传输层连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obex` | OBEX 对象。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a2c04d635154acfa9f4579596d8ed7d79"></a>

### `send`

```c
int(* bt_obex_transport_ops::send) (struct bt_obex *obex, struct net_buf *buf)
```

通过传输层发送 OBEX 数据。

如果提供了此回调，将调用它通过 OBEX 传输层发送数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obex` | OBEX 对象。 |
| `buf` | OBEX 数据包。 |

**返回（Returns）**：返回值：成功时返回 0，错误时返回负值。如果 `buf` 大于 OBEX 的 MOPL，则返回 `-EMSGSIZE`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/obex.h`

## 134.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/obex.h](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h_source.html)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_obex](P127_bt_obex_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P133_bt_obex_tlv_结构体.md) · [返回大纲](大纲.md) · [下一章](P135_bt_ots_结构体.md)
