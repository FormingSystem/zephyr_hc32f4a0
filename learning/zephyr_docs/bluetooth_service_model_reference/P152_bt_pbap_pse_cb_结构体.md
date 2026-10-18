---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-152
title: bt_pbap_pse_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__pbap__pse__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第152章\_bt\_pbap\_pse\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__pbap__pse__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电话簿访问配置文件（PBAP）的电话簿服务器设备（PSE）回调操作结构。

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

<a id="details"></a>

电话簿访问规范（PBAP）的电话簿服务器设备（Phone Book Server Equipment，PSE）回调操作结构体。定义在服务器端处理 PBAP 客户端请求的回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 152.1\_数据成员（Data Fields）

<a id="r_a508df68d361d6bbcac77c07326ad216c"></a>

```c
void(* rfcomm_connected )(struct bt_conn *conn, struct bt_pbap_pse *pbap_pse)
```

相关声明：[rfcomm_connected](#a508df68d361d6bbcac77c07326ad216c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)。

RFCOMM 传输连接建立回调。

<a id="r_a9b79c775e8f4bc1196f0496e1e4042af"></a>

```c
void(* rfcomm_disconnected )(struct bt_pbap_pse *pbap_pse)
```

相关声明：[rfcomm_disconnected](#a9b79c775e8f4bc1196f0496e1e4042af)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)。

RFCOMM 传输连接断开回调。

<a id="r_a99fb49679cf7f737e3d6d431fe529006"></a>

```c
void(* l2cap_connected )(struct bt_conn *conn, struct bt_pbap_pse *pbap_pse)
```

相关声明：[l2cap_connected](#a99fb49679cf7f737e3d6d431fe529006)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)。

L2CAP 传输连接建立回调。

<a id="r_aae32aaaf8d68858542127abcbadbd113"></a>

```c
void(* l2cap_disconnected )(struct bt_pbap_pse *pbap_pse)
```

相关声明：[l2cap_disconnected](#aae32aaaf8d68858542127abcbadbd113)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)。

L2CAP 传输连接断开回调。

<a id="r_ada011b1e352408abfcf67795bf3672e5"></a>

```c
void(* connect )(struct bt_pbap_pse *pbap_pse, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#ada011b1e352408abfcf67795bf3672e5)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PSE 连接（connect）请求回调。

<a id="r_a9ad9db6bff9050ab7253101058356b45"></a>

```c
void(* disconnect )(struct bt_pbap_pse *pbap_pse, struct net_buf *buf)
```

相关声明：[disconnect](#a9ad9db6bff9050ab7253101058356b45)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PSE 断开连接（disconnect）请求回调。

<a id="r_a2fb6ed5d1728989b3356664d1b037dce"></a>

```c
void(* pull_phone_book )(struct bt_pbap_pse *pbap_pse, struct net_buf *buf)
```

相关声明：[pull_phone_book](#a2fb6ed5d1728989b3356664d1b037dce)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PSE 拉取电话簿（pull phone book）请求回调。

<a id="r_a16cb90f530643c371cdb63ad0af24cfa"></a>

```c
void(* pull_vcard_listing )(struct bt_pbap_pse *pbap_pse, struct net_buf *buf)
```

相关声明：[pull_vcard_listing](#a16cb90f530643c371cdb63ad0af24cfa)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PSE 拉取 vCard 列表（pull vCard listing）请求回调。

<a id="r_a1601fff1b1b320de8c20f62a0b3779b4"></a>

```c
void(* pull_vcard_entry )(struct bt_pbap_pse *pbap_pse, struct net_buf *buf)
```

相关声明：[pull_vcard_entry](#a1601fff1b1b320de8c20f62a0b3779b4)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PSE 拉取 vCard 条目（pull vCard entry）请求回调。

<a id="r_a9f524ac72b376c1ce033574d75cdc5a0"></a>

```c
void(* set_phone_book )(struct bt_pbap_pse *pbap_pse, uint8_t flags, struct net_buf *buf)
```

相关声明：[set_phone_book](#a9f524ac72b376c1ce033574d75cdc5a0)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PSE 设置电话簿（set phone book）请求回调。

<a id="r_a7fa67e965c441cf8d6b8a1382c68e7cf"></a>

```c
void(* abort )(struct bt_pbap_pse *pbap_pse, struct net_buf *buf)
```

相关声明：[abort](#a7fa67e965c441cf8d6b8a1382c68e7cf)、[bt_pbap_pse](P151_bt_pbap_pse_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PSE 中止（abort）请求回调。

## 152.2\_详细说明（Detailed Documentation）

<a id="a7fa67e965c441cf8d6b8a1382c68e7cf"></a>

### `abort`

```c
void(* bt_pbap_pse_cb::abort) (struct bt_pbap_pse *pbap_pse, struct net_buf *buf)
```

PBAP PSE 中止（abort）请求回调。

收到 PCE 客户端的中止请求时调用。PSE 应取消当前正在进行的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `buf` | 可选请求头缓冲区。 |

<a id="ada011b1e352408abfcf67795bf3672e5"></a>

### `connect`

```c
void(* bt_pbap_pse_cb::connect) (struct bt_pbap_pse *pbap_pse, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

PBAP PSE 连接（connect）请求回调。

收到 PCE 客户端的 PBAP 连接请求时调用。PSE 应验证请求并准备响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `version` | PCE 请求的 PBAP 版本。 |
| `mopl` | PCE 请求的最大 OBEX 数据包长度。 |
| `buf` | 请求头缓冲区，可能包含目标、身份验证等信息。 |

<a id="a9ad9db6bff9050ab7253101058356b45"></a>

### `disconnect`

```c
void(* bt_pbap_pse_cb::disconnect) (struct bt_pbap_pse *pbap_pse, struct net_buf *buf)
```

PBAP PSE 断开连接（disconnect）请求回调。

收到 PCE 客户端的 PBAP 断开连接请求时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `buf` | 可选请求头缓冲区。 |

<a id="a99fb49679cf7f737e3d6d431fe529006"></a>

### `l2cap_connected`

```c
void(* bt_pbap_pse_cb::l2cap_connected) (struct bt_conn *conn, struct bt_pbap_pse *pbap_pse)
```

L2CAP 传输连接建立回调。

底层 L2CAP 传输连接建立时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接。 |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |

<a id="aae32aaaf8d68858542127abcbadbd113"></a>

### `l2cap_disconnected`

```c
void(* bt_pbap_pse_cb::l2cap_disconnected) (struct bt_pbap_pse *pbap_pse)
```

L2CAP 传输连接断开回调。

底层 L2CAP 传输连接断开时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |

<a id="a2fb6ed5d1728989b3356664d1b037dce"></a>

### `pull_phone_book`

```c
void(* bt_pbap_pse_cb::pull_phone_book) (struct bt_pbap_pse *pbap_pse, struct net_buf *buf)
```

PBAP PSE 拉取电话簿（pull phone book）请求回调。

收到 PCE 客户端的拉取电话簿请求时调用。PSE 应取得所请求的电话簿并发回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `buf` | 请求头缓冲区，包含名称、类型、应用参数等信息。 |

<a id="a1601fff1b1b320de8c20f62a0b3779b4"></a>

### `pull_vcard_entry`

```c
void(* bt_pbap_pse_cb::pull_vcard_entry) (struct bt_pbap_pse *pbap_pse, struct net_buf *buf)
```

PBAP PSE 拉取 vCard 条目（pull vCard entry）请求回调。

收到 PCE 客户端的拉取 vCard 条目请求时调用。PSE 应取得所请求的 vCard 条目并发回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `buf` | 请求头缓冲区，包含名称、类型、应用参数等信息。 |

<a id="a16cb90f530643c371cdb63ad0af24cfa"></a>

### `pull_vcard_listing`

```c
void(* bt_pbap_pse_cb::pull_vcard_listing) (struct bt_pbap_pse *pbap_pse, struct net_buf *buf)
```

PBAP PSE 拉取 vCard 列表（pull vCard listing）请求回调。

收到 PCE 客户端的拉取 vCard 列表请求时调用。PSE 应取得所请求的 vCard 列表并发回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `buf` | 请求头缓冲区，包含名称、类型、应用参数等信息。 |

<a id="a508df68d361d6bbcac77c07326ad216c"></a>

### `rfcomm_connected`

```c
void(* bt_pbap_pse_cb::rfcomm_connected) (struct bt_conn *conn, struct bt_pbap_pse *pbap_pse)
```

RFCOMM 传输连接建立回调。

底层 RFCOMM 传输连接建立时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接。 |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |

<a id="a9b79c775e8f4bc1196f0496e1e4042af"></a>

### `rfcomm_disconnected`

```c
void(* bt_pbap_pse_cb::rfcomm_disconnected) (struct bt_pbap_pse *pbap_pse)
```

RFCOMM 传输连接断开回调。

底层 RFCOMM 传输连接断开时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |

<a id="a9f524ac72b376c1ce033574d75cdc5a0"></a>

### `set_phone_book`

```c
void(* bt_pbap_pse_cb::set_phone_book) (struct bt_pbap_pse *pbap_pse, uint8_t flags, struct net_buf *buf)
```

PBAP PSE 设置电话簿（set phone book）请求回调。

收到 PCE 客户端的设置电话簿请求时调用。PSE 应将当前电话簿设为所请求的电话簿。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `flags` | 导航标志：向上、向下或根目录（up/down/root）。`BT_PBAP_SET_PHONE_BOOK_FLAGS_UP` 表示转到父目录；`BT_PBAP_SET_PHONE_BOOK_FLAGS_DOWN_OR_ROOT` 表示转到子目录或根目录。 |
| `buf` | 可选请求头缓冲区，可能包含文件夹名称。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/pbap.h`

## 152.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/pbap.h](https://docs.zephyrproject.org/latest/doxygen/html/pbap_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_pbap_pse](P151_bt_pbap_pse_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [BT_PBAP_SET_PHONE_BOOK_FLAGS_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9602f26d0e3524e0a5f40a9854432e44)
- [BT_PBAP_SET_PHONE_BOOK_FLAGS_DOWN_OR_ROOT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga66c979baa8aefbfab188d4c9017fac8b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P151_bt_pbap_pse_结构体.md) · [返回大纲](大纲.md) · [下一章](P153_bt_pbap_pse_l2cap_结构体.md)
