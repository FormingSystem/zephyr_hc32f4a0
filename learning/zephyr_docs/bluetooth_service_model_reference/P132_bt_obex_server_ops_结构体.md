---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-132
title: bt_obex_server_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__server__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第132章\_bt\_obex\_server\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__server__ops.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象交换协议（OBEX）的服务器操作结构。

```c
#include <zephyr/bluetooth/classic/obex.h>
```

<a id="details"></a>

OBEX 服务器操作结构体。此对象必须在 OBEX 服务器的整个生命周期内保持有效且不变。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 132.1\_数据成员（Data Fields）

<a id="r_a0449e9ab3018796818460f95dd2df13e"></a>

```c
void(* connect )(struct bt_obex_server *server, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#a0449e9ab3018796818460f95dd2df13e)、[bt_obex_server](P131_bt_obex_server_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 连接请求回调。

<a id="r_ab7e99df178911eef8cc8192716a64412"></a>

```c
void(* disconnect )(struct bt_obex_server *server, struct net_buf *buf)
```

相关声明：[disconnect](#ab7e99df178911eef8cc8192716a64412)、[bt_obex_server](P131_bt_obex_server_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 断开连接请求回调。

<a id="r_ae761cd5aa9728448ee97f306ab9332a6"></a>

```c
void(* put )(struct bt_obex_server *server, bool final, struct net_buf *buf)
```

相关声明：[put](#ae761cd5aa9728448ee97f306ab9332a6)、[bt_obex_server](P131_bt_obex_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 放置（put）请求回调。

<a id="r_a7380f0fdb31a7f82f75b65a857037987"></a>

```c
void(* get )(struct bt_obex_server *server, bool final, struct net_buf *buf)
```

相关声明：[get](#a7380f0fdb31a7f82f75b65a857037987)、[bt_obex_server](P131_bt_obex_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 获取（get）请求回调。

<a id="r_a2763317faa8d5a1371e979d6021ca114"></a>

```c
void(* abort )(struct bt_obex_server *server, struct net_buf *buf)
```

相关声明：[abort](#a2763317faa8d5a1371e979d6021ca114)、[bt_obex_server](P131_bt_obex_server_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 中止请求回调。

<a id="r_a90839fcaf2bd369d1d5a8c833003f2be"></a>

```c
void(* setpath )(struct bt_obex_server *server, uint8_t flags, struct net_buf *buf)
```

相关声明：[setpath](#a90839fcaf2bd369d1d5a8c833003f2be)、[bt_obex_server](P131_bt_obex_server_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 设置路径（SetPath）请求回调。

<a id="r_a98b433a269295f3784bce6100aea186a"></a>

```c
void(* action )(struct bt_obex_server *server, bool final, struct net_buf *buf)
```

相关声明：[action](#a98b433a269295f3784bce6100aea186a)、[bt_obex_server](P131_bt_obex_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 动作（action）请求回调。

## 132.2\_详细说明（Detailed Documentation）

<a id="a2763317faa8d5a1371e979d6021ca114"></a>

### `abort`

```c
void(* bt_obex_server_ops::abort) (struct bt_obex_server *server, struct net_buf *buf)
```

OBEX 中止请求回调。

如果提供了此回调，每当收到 OBEX 中止（abort）请求时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象。 |
| `buf` | 可选头部。 |

<a id="a98b433a269295f3784bce6100aea186a"></a>

### `action`

```c
void(* bt_obex_server_ops::action) (struct bt_obex_server *server, bool final, struct net_buf *buf)
```

OBEX 动作（action）请求回调。

如果提供了此回调，每当收到 OBEX 动作（action）请求时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象。 |
| `final` | 最终位（final bit）是否已置位。 |
| `buf` | 头部序列；如果存在动作标识符头（action identifier header），则也包含它。 |

<a id="a0449e9ab3018796818460f95dd2df13e"></a>

### `connect`

```c
void(* bt_obex_server_ops::connect) (struct bt_obex_server *server, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

OBEX 连接请求回调。

如果提供了此回调，每当收到 OBEX 连接（connect）请求时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象。 |
| `version` | OBEX 版本号。 |
| `mopl` | OBEX 数据包的最大长度。 |
| `buf` | 头部序列（Sequence of headers）。 |

<a id="ab7e99df178911eef8cc8192716a64412"></a>

### `disconnect`

```c
void(* bt_obex_server_ops::disconnect) (struct bt_obex_server *server, struct net_buf *buf)
```

OBEX 断开连接请求回调。

如果提供了此回调，每当收到 OBEX 断开连接（disconnect）请求时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象。 |
| `buf` | 头部序列（Sequence of headers）。 |

<a id="a7380f0fdb31a7f82f75b65a857037987"></a>

### `get`

```c
void(* bt_obex_server_ops::get) (struct bt_obex_server *server, bool final, struct net_buf *buf)
```

OBEX 获取（get）请求回调。

如果提供了此回调，每当收到 OBEX 获取（get）请求时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象。 |
| `final` | 最终位（final bit）是否已置位。 |
| `buf` | 头部序列（Sequence of headers）。 |

<a id="ae761cd5aa9728448ee97f306ab9332a6"></a>

### `put`

```c
void(* bt_obex_server_ops::put) (struct bt_obex_server *server, bool final, struct net_buf *buf)
```

OBEX 放置（put）请求回调。

如果提供了此回调，每当收到 OBEX 放置（put）请求时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象。 |
| `final` | 最终位（final bit）是否已置位。 |
| `buf` | 头部序列（Sequence of headers）。 |

<a id="a90839fcaf2bd369d1d5a8c833003f2be"></a>

### `setpath`

```c
void(* bt_obex_server_ops::setpath) (struct bt_obex_server *server, uint8_t flags, struct net_buf *buf)
```

OBEX 设置路径（SetPath）请求回调。

如果提供了此回调，每当收到 OBEX 设置路径（SetPath）请求时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | OBEX 服务器对象。 |
| `flags` | 标志，类型为 `bt_obex_setpath_flags`。 |
| `buf` | 可选头部。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/obex.h`

## 132.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/obex.h](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h_source.html)
- [bt_obex_server](P131_bt_obex_server_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_obex_setpath_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gab5f7e6a6c7503f97a851f48c70162483)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P131_bt_obex_server_结构体.md) · [返回大纲](大纲.md) · [下一章](P133_bt_obex_tlv_结构体.md)
