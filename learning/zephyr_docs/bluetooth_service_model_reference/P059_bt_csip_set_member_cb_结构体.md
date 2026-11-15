---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-59
title: bt_csip_set_member_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__member__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_bt\_csip\_set\_member\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__member__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

协调集合标识服务（Coordinated Set Identification Service，CSIS）的回调结构体。

```c
#include <zephyr/bluetooth/audio/csip.h>
```

<a id="details"></a>

协调集合标识服务（Coordinated Set Identification Service，CSIS）的回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_a46e18120caf78788f0928ada2c92ca5c"></a>

```c
void(* lock_changed )(struct bt_conn *conn, struct bt_csip_set_member_svc_inst *svc_inst, bool locked)
```

相关声明：[lock_changed](#a46e18120caf78788f0928ada2c92ca5c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_csip_set_member_svc_inst](P062_bt_csip_set_member_svc_inst_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

服务器上的锁（Lock）发生变化时调用的回调。

<a id="r_a30b2f68aff4b75ffcc8e9d7e2de2afd9"></a>

```c
uint8_t(* sirk_read_req )(struct bt_conn *conn, struct bt_csip_set_member_svc_inst *svc_inst)
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sirk_read_req](#a30b2f68aff4b75ffcc8e9d7e2de2afd9)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_csip_set_member_svc_inst](P062_bt_csip_set_member_svc_inst_结构体.md)。

对等设备发出的读取集合身份解析密钥（SIRK）请求。

## 59.2\_详细说明（Detailed Documentation）

<a id="a46e18120caf78788f0928ada2c92ca5c"></a>

### `lock_changed`

```c
void(* bt_csip_set_member_cb::lock_changed) (struct bt_conn *conn, struct bt_csip_set_member_svc_inst *svc_inst, bool locked)
```

服务器上的锁（Lock）发生变化时调用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向更改锁的客户端连接的指针。如果服务器通过调用 `bt_csip_set_member_lock()` 或超时更改锁，则为 `NULL`。 |
| `svc_inst` | 指向协调集合标识服务（Coordinated Set Identification Service）的指针。 |
| `locked` | 锁（Lock）是被锁定还是释放。 |

<a id="a30b2f68aff4b75ffcc8e9d7e2de2afd9"></a>

### `sirk_read_req`

```c
uint8_t(* bt_csip_set_member_cb::sirk_read_req) (struct bt_conn *conn, struct bt_csip_set_member_svc_inst *svc_inst)
```

对等设备发出的读取集合身份解析密钥（SIRK）请求。

若未设置此回调，所有客户端都可在未加密的情况下读取集合身份解析密钥（SIRK）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 请求读取集合身份解析密钥（SIRK）的客户端连接。 |
| `svc_inst` | 指向协调集合标识服务（Coordinated Set Identification Service）的指针。 |

**返回（Returns）**：返回值（Returns）：一个 `BT_CSIP_READ_SIRK_REQ_RSP_*` 响应码。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/csip.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/csip.h](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_csip_set_member_svc_inst](P062_bt_csip_set_member_svc_inst_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_csip_set_member_lock()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga95e2ba4b65ec42eedb26bf5ad181b606)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_bt_csip_set_coordinator_set_member_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_bt_csip_set_member_register_param_结构体.md)
