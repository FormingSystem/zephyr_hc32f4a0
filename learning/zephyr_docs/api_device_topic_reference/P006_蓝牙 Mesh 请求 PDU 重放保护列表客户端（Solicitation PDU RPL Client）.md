---
id: learning.zephyr-docs.api-device-topic-reference.page-6
title: 蓝牙 Mesh 请求 PDU 重放保护列表客户端（Solicitation PDU RPL Client）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_蓝牙 Mesh 请求 PDU 重放保护列表客户端（Solicitation PDU RPL Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_sol_5Fpdu_5Frpl_5Fcli_2Eh"></a>

```c
file sol_pdu_rpl_cli.h
```

相关声明：[sol_pdu_rpl_cli.h](../api_file_service_reference/P052_zephyr__bluetooth__mesh__sol_pdu_rpl_cli.h_文件参考.md)。

蓝牙Mesh请求PDU重放保护列表客户端（Solicitation PDU RPL Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.2\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fsol_5Fpdu_5Frpl_5Fcli"></a>

```c
struct bt_mesh_sol_pdu_rpl_cli
```

相关声明：[bt_mesh_sol_pdu_rpl_cli](../bluetooth_mesh_model_reference/P100_bt_mesh_sol_pdu_rpl_cli_结构体.md)。

请求PDU重放保护列表客户端（Solicitation PDU RPL Client）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.3\_宏定义（Macros）

<a id="r_gac5969e20994b07977484391ac2d7bacb"></a>

```c
#define BT_MESH_MODEL_SOL_PDU_RPL_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_SOL_PDU_RPL_CLI](#gac5969e20994b07977484391ac2d7bacb)。

征询协议数据单元重放保护列表客户端模型（Solicitation PDU RPL Client Model）的组成数据条目（Composition Data Entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.4\_函数（Functions）

<a id="r_gae7e8a0e364c6695a467a64cd89627d81"></a>

```c
int bt_mesh_sol_pdu_rpl_clear (struct bt_mesh_msg_ctx *ctx, uint16_t range_start, uint8_t range_len, uint16_t *start_rsp, uint8_t *len_rsp)
```

相关声明：[bt_mesh_sol_pdu_rpl_clear](#gae7e8a0e364c6695a467a64cd89627d81)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从征询协议数据单元重放保护列表（Solicitation PDU RPL）中移除给定地址范围内的条目（Entries）。

<a id="r_ga68fb70fbfb87e76ef6fdb5ac8a1a9506"></a>

```c
int bt_mesh_sol_pdu_rpl_clear_unack (struct bt_mesh_msg_ctx *ctx, uint16_t range_start, uint8_t range_len)
```

相关声明：[bt_mesh_sol_pdu_rpl_clear_unack](#ga68fb70fbfb87e76ef6fdb5ac8a1a9506)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从征询协议数据单元重放保护列表（Solicitation PDU RPL）中移除给定地址范围内的条目，采用无确认方式（Unacknowledged）。

<a id="r_gadabdbd95f39a498307e3ca9e50acfeb9"></a>

```c
void bt_mesh_sol_pdu_rpl_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_sol_pdu_rpl_cli_timeout_set](#gadabdbd95f39a498307e3ca9e50acfeb9)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。

## 6.5\_详细说明（Detailed Documentation）

<a id="gac5969e20994b07977484391ac2d7bacb"></a>

### `BT_MESH_MODEL_SOL_PDU_RPL_CLI`

```c
#define BT_MESH_MODEL_SOL_PDU_RPL_CLI ( cli_data)
```

```c
#include <zephyr/bluetooth/mesh/sol_pdu_rpl_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_SOL_PDU_RPL_CLI,                  \
                 _bt_mesh_sol_pdu_rpl_cli_op, NULL, cli_data,       \
                 &_bt_mesh_sol_pdu_rpl_cli_cb)
```

征询协议数据单元重放保护列表客户端模型（Solicitation PDU RPL Client Model）的组成数据条目（Composition Data Entry）。

<a id="gae7e8a0e364c6695a467a64cd89627d81"></a>

### `bt_mesh_sol_pdu_rpl_clear()`

```c
int bt_mesh_sol_pdu_rpl_clear ( struct bt_mesh_msg_ctx * ctx, uint16_t range_start, uint8_t range_len, uint16_t * start_rsp, uint8_t * len_rsp )
```

```c
#include <zephyr/bluetooth/mesh/sol_pdu_rpl_cli.h>
```

从征询协议数据单元重放保护列表（Solicitation PDU RPL）中移除给定地址范围内的条目（Entries）。

将 `start_rsp` 或 `len_rsp` 设为 `NULL` 即可异步使用此方法。这样，该方法不会等待响应，而会在发送命令后立即返回。

若要处理异步方法的响应参数，请在 `bt_mesh_sol_pdu_rpl_cli` 结构体中注册 `srpl_status` 回调（callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 该消息的消息上下文（Message context）。 |
| `range_start` | 单播地址范围（Unicast address range）的起始地址。 |
| `range_len` | 单播地址范围的长度。有效值为 `0x00`，以及 `0x02` 至 `0xff`。 |
| `start_rsp` | 范围起始地址的响应缓冲区。 |
| `len_rsp` | 范围长度的响应缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga68fb70fbfb87e76ef6fdb5ac8a1a9506"></a>

### `bt_mesh_sol_pdu_rpl_clear_unack()`

```c
int bt_mesh_sol_pdu_rpl_clear_unack ( struct bt_mesh_msg_ctx * ctx, uint16_t range_start, uint8_t range_len )
```

```c
#include <zephyr/bluetooth/mesh/sol_pdu_rpl_cli.h>
```

从征询协议数据单元重放保护列表（Solicitation PDU RPL）中移除给定地址范围内的条目，采用无确认方式（Unacknowledged）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 该消息的消息上下文（Message context）。 |
| `range_start` | 单播地址范围（Unicast address range）的起始地址。 |
| `range_len` | 单播地址范围的长度。有效值为 `0x00`，以及 `0x02` 至 `0xff`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="gadabdbd95f39a498307e3ca9e50acfeb9"></a>

### `bt_mesh_sol_pdu_rpl_cli_timeout_set()`

```c
void bt_mesh_sol_pdu_rpl_cli_timeout_set ( int32_t timeout)
```

```c
#include <zephyr/bluetooth/mesh/sol_pdu_rpl_cli.h>
```

设置传输超时值（Transmission Timeout Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 新的传输超时（transmission timeout），单位为毫秒。 |


## 6.6\_原页交叉引用（Cross References）

- [sol_pdu_rpl_cli.h](../api_file_service_reference/P052_zephyr__bluetooth__mesh__sol_pdu_rpl_cli.h_文件参考.md)
- [bt_mesh_sol_pdu_rpl_cli](../bluetooth_mesh_model_reference/P100_bt_mesh_sol_pdu_rpl_cli_结构体.md)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_SOL_PDU_RPL_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga6e747dd364bcfaa368e37c5f01afd530)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga6e747dd364bcfaa368e37c5f01afd530"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_蓝牙 Mesh 分段与重组配置客户端模型（SAR Configuration Client Model）.md) · [返回大纲](大纲.md) · [下一章](P007_充电器驱动后端 API（Charger Driver Backend API）.md)
