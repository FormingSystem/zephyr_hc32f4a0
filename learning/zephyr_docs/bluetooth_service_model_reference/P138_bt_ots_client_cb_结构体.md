---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-138
title: bt_ots_client_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__client__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第138章\_bt\_ots\_client\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__client__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象传输服务（OTS）的客户端回调结构。

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="details"></a>

对象传输服务（OTS）的客户端回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 138.1\_数据成员（Data Fields）

<a id="r_ace98d27220e394b0990a8274bbd43026"></a>

```c
void(* obj_selected )(struct bt_ots_client *ots_inst, struct bt_conn *conn, int err)
```

相关声明：[obj_selected](#ace98d27220e394b0990a8274bbd43026)、[bt_ots_client](P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

选择新对象时的回调函数。

<a id="r_ae95f3b85758c04279ada801c001086bc"></a>

```c
int(* obj_data_read )(struct bt_ots_client *ots_inst, struct bt_conn *conn, uint32_t offset, uint32_t len, uint8_t *data_p, bool is_complete)
```

相关声明：[obj_data_read](#ae95f3b85758c04279ada801c001086bc)、[bt_ots_client](P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

处理所选对象数据的回调函数。

<a id="r_ab6c03b98fc5c68aa8c76ada23b7dff1c"></a>

```c
void(* obj_metadata_read )(struct bt_ots_client *ots_inst, struct bt_conn *conn, int err, uint8_t metadata_read)
```

相关声明：[obj_metadata_read](#ab6c03b98fc5c68aa8c76ada23b7dff1c)、[bt_ots_client](P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

处理所选对象元数据（metadata）的回调函数。

<a id="r_a2baaf13c8de4ade034f2b58896225e0d"></a>

```c
void(* obj_data_written )(struct bt_ots_client *ots_inst, struct bt_conn *conn, size_t len)
```

相关声明：[obj_data_written](#a2baaf13c8de4ade034f2b58896225e0d)、[bt_ots_client](P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

处理写入对象数据的回调函数。

<a id="r_ad5537da9ced98a15620a7fb1e77b0218"></a>

```c
void(* obj_checksum_calculated )(struct bt_ots_client *ots_inst, struct bt_conn *conn, int err, uint32_t checksum)
```

相关声明：[obj_checksum_calculated](#ad5537da9ced98a15620a7fb1e77b0218)、[bt_ots_client](P137_bt_ots_client_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

收到校验和指示（checksum indication）时的回调函数。

## 138.2\_详细说明（Detailed Documentation）

<a id="ad5537da9ced98a15620a7fb1e77b0218"></a>

### `obj_checksum_calculated`

```c
void(* bt_ots_client_cb::obj_checksum_calculated) (struct bt_ots_client *ots_inst, struct bt_conn *conn, int err, uint32_t checksum)
```

收到校验和指示（checksum indication）时的回调函数。

当 `oacp_ind_handler` 收到 `BT_GATT_OTS_OACP_PROC_CHECKSUM_CALC` 操作的响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 与对端设备的连接。 |
| `err` | 错误码，类型为 `bt_gatt_ots_oacp_res_code`。 |
| `Checksum` | 错误码为 `BT_GATT_OTS_OACP_RES_SUCCESS` 时提供校验和，否则为 0。 |

<a id="ae95f3b85758c04279ada801c001086bc"></a>

### `obj_data_read`

```c
int(* bt_ots_client_cb::obj_data_read) (struct bt_ots_client *ots_inst, struct bt_conn *conn, uint32_t offset, uint32_t len, uint8_t *data_p, bool is_complete)
```

处理所选对象数据的回调函数。

通过 `bt_ots_client_read_object_data()` 读取所选对象的数据时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 与对端设备的连接。 |
| `offset` | 接收数据的偏移量。 |
| `len` | 接收数据的长度。 |
| `data_p` | 指向接收数据的指针。 |
| `is_complete` | 指示是否已接收到整个对象。 |

**返回（Returns）**：返回值：`int` 类型的 `BT_OTS_STOP` 或 `BT_OTS_CONTINUE`。可使用 `BT_OTS_STOP` 停止读取。

<a id="a2baaf13c8de4ade034f2b58896225e0d"></a>

### `obj_data_written`

```c
void(* bt_ots_client_cb::obj_data_written) (struct bt_ots_client *ots_inst, struct bt_conn *conn, size_t len)
```

处理写入对象数据的回调函数。

通过 `bt_ots_client_write_object_data()` 写入所选对象的数据时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 与对端设备的连接。 |
| `len` | 已写入数据的长度。 |

<a id="ab6c03b98fc5c68aa8c76ada23b7dff1c"></a>

### `obj_metadata_read`

```c
void(* bt_ots_client_cb::obj_metadata_read) (struct bt_ots_client *ots_inst, struct bt_conn *conn, int err, uint8_t metadata_read)
```

处理所选对象元数据（metadata）的回调函数。

通过 `bt_ots_client_read_object_metadata()` 读取所选对象的元数据时调用。并非所有元数据都一定已初始化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 与对端设备的连接。 |
| `err` | 错误值。成功时为 0，失败时为 GATT 错误或 `ERRNO`。 |
| `metadata_read` | 标记已成功读取的元数据的位域（bitfield）。 |

<a id="ace98d27220e394b0990a8274bbd43026"></a>

### `obj_selected`

```c
void(* bt_ots_client_cb::obj_selected) (struct bt_ots_client *ots_inst, struct bt_conn *conn, int err)
```

选择新对象时的回调函数。

选择新对象且当前对象发生变化时调用。`ots_inst` 中的 `cur_object` 此时已被重置，应使用 `bt_ots_client_read_object_metadata()` 重新读取元数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots_inst` | 指向对象传输客户端（OTC）实例的指针。 |
| `conn` | 与对端设备的连接。 |
| `err` | 错误码，类型为 `bt_ots_olcp_res_code`。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ots.h`

## 138.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ots.h](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h_source.html)
- [bt_ots_client](P137_bt_ots_client_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [Checksum](../checksum_reference/P001_校验和主题目录.md)
- [bt_ots_client_read_object_data()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga8ad1c53325c1b77271307507317a5965)
- [bt_ots_client_write_object_data()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga9444b064c616718dae1577b21540fb9a)
- [bt_ots_client_read_object_metadata()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga936f392c880c9d1a73f2bd632e5b63e0)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P137_bt_ots_client_结构体.md) · [返回大纲](大纲.md) · [下一章](P139_bt_ots_date_time_结构体.md)
