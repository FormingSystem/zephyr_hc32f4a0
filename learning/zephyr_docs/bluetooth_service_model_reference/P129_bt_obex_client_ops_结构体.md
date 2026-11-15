---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-129
title: bt_obex_client_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__client__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第129章\_bt\_obex\_client\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__client__ops.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象交换协议（OBEX）的客户端操作结构。

```c
#include <zephyr/bluetooth/classic/obex.h>
```

<a id="details"></a>

OBEX 客户端操作结构体。此对象必须在 OBEX 客户端的整个生命周期内保持有效且不变。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 129.1\_数据成员（Data Fields）

<a id="r_ac47ffc1353bef9d4d3725e05b75461f2"></a>

```c
void(* connect )(struct bt_obex_client *client, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#ac47ffc1353bef9d4d3725e05b75461f2)、[bt_obex_client](P128_bt_obex_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

对象交换协议（Object Exchange，OBEX）连接响应回调。

<a id="r_a1e7227232515d875123e6f8ed2bfd993"></a>

```c
void(* disconnect )(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[disconnect](#a1e7227232515d875123e6f8ed2bfd993)、[bt_obex_client](P128_bt_obex_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 断开连接响应回调。

<a id="r_a6a5cb209c9fb53786ee51ac4080d7bbc"></a>

```c
void(* put )(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[put](#a6a5cb209c9fb53786ee51ac4080d7bbc)、[bt_obex_client](P128_bt_obex_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 放置（put）响应回调。

<a id="r_ae63892d7c4ec6850de4137b466e0fa94"></a>

```c
void(* get )(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get](#ae63892d7c4ec6850de4137b466e0fa94)、[bt_obex_client](P128_bt_obex_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 获取（get）响应回调。

<a id="r_a28ee9ffbbd94c961ef28216ec958d604"></a>

```c
void(* abort )(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[abort](#a28ee9ffbbd94c961ef28216ec958d604)、[bt_obex_client](P128_bt_obex_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 中止响应回调。

<a id="r_a250940fb4d5b0a2e782645ba7307fd70"></a>

```c
void(* setpath )(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[setpath](#a250940fb4d5b0a2e782645ba7307fd70)、[bt_obex_client](P128_bt_obex_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 设置路径（SetPath）响应回调。

<a id="r_a1a09c04578beca66cac473fe125747cd"></a>

```c
void(* action )(struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[action](#a1a09c04578beca66cac473fe125747cd)、[bt_obex_client](P128_bt_obex_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

OBEX 动作（action）响应回调。

## 129.2\_详细说明（Detailed Documentation）

<a id="a28ee9ffbbd94c961ef28216ec958d604"></a>

### `abort`

```c
void(* bt_obex_client_ops::abort) (struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

OBEX 中止响应回调。

如果提供了此回调，每当收到 OBEX 中止（abort）响应时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 可选响应头。 |

<a id="a1a09c04578beca66cac473fe125747cd"></a>

### `action`

```c
void(* bt_obex_client_ops::action) (struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

OBEX 动作（action）响应回调。

如果提供了此回调，每当收到 OBEX 动作（action）响应时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 可选响应头。 |

<a id="ac47ffc1353bef9d4d3725e05b75461f2"></a>

### `connect`

```c
void(* bt_obex_client_ops::connect) (struct bt_obex_client *client, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

对象交换协议（Object Exchange，OBEX）连接响应回调。

如果提供了此回调，每当收到 OBEX 连接（connect）响应时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象。 |
| `rsp_code` | 响应码（Response Code）。 |
| `version` | OBEX 版本号。 |
| `mopl` | OBEX 数据包的最大长度。 |
| `buf` | 头部序列（Sequence of headers）。 |

<a id="a1e7227232515d875123e6f8ed2bfd993"></a>

### `disconnect`

```c
void(* bt_obex_client_ops::disconnect) (struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

OBEX 断开连接响应回调。

如果提供了此回调，每当收到 OBEX 断开连接（disconnect）响应时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 头部序列（Sequence of headers）。 |

<a id="ae63892d7c4ec6850de4137b466e0fa94"></a>

### `get`

```c
void(* bt_obex_client_ops::get) (struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

OBEX 获取（get）响应回调。

如果提供了此回调，每当收到 OBEX 获取（get）响应时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 可选响应头。 |

<a id="a6a5cb209c9fb53786ee51ac4080d7bbc"></a>

### `put`

```c
void(* bt_obex_client_ops::put) (struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

OBEX 放置（put）响应回调。

如果提供了此回调，每当收到 OBEX 放置（put）响应时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 可选响应头。 |

<a id="a250940fb4d5b0a2e782645ba7307fd70"></a>

### `setpath`

```c
void(* bt_obex_client_ops::setpath) (struct bt_obex_client *client, uint8_t rsp_code, struct net_buf *buf)
```

OBEX 设置路径（SetPath）响应回调。

如果提供了此回调，每当收到 OBEX 设置路径（SetPath）响应时都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | OBEX 客户端对象。 |
| `rsp_code` | 响应码（Response Code）。 |
| `buf` | 可选响应头。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/obex.h`

## 129.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/obex.h](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h_source.html)
- [bt_obex_client](P128_bt_obex_client_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P128_bt_obex_client_结构体.md) · [返回大纲](大纲.md) · [下一章](P130_bt_obex_hdr_结构体.md)
