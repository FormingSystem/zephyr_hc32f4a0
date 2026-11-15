---
id: learning.zephyr-docs.api-network-time-topic-reference.page-3
title: 操作码聚合器客户端模型（Opcodes Aggregator Client model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_操作码聚合器客户端模型（Opcodes Aggregator Client model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_op_5Fagg_5Fcli_2Eh"></a>

```c
file op_agg_cli.h
```

相关声明：[op_agg_cli.h](../api_file_system_device_reference/P034_zephyr__bluetooth__mesh__op_agg_cli.h_文件参考.md)。

蓝牙Mesh操作码聚合器客户端（Opcodes Aggregator Client）模型API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga0a8dec4b4f53d1ec95db1efc4ab22f69"></a>

```c
#define BT_MESH_MODEL_OP_AGG_CLI
```

相关声明：[BT_MESH_MODEL_OP_AGG_CLI](#ga0a8dec4b4f53d1ec95db1efc4ab22f69)。

操作码聚合器客户端（Opcodes Aggregator Client）模型的组成数据条目（composition data entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_gac1905d778362faf442a9538adca34a8c"></a>

```c
int bt_mesh_op_agg_cli_seq_start (uint16_t net_idx, uint16_t app_idx, uint16_t dst, uint16_t elem_addr)
```

相关声明：[bt_mesh_op_agg_cli_seq_start](#gac1905d778362faf442a9538adca34a8c)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

配置操作码聚合器（Opcodes Aggregator）上下文。

<a id="r_gab151f44fcb5d3f3f0f1dafaf90f05c18"></a>

```c
int bt_mesh_op_agg_cli_seq_send (void)
```

相关声明：[bt_mesh_op_agg_cli_seq_send](#gab151f44fcb5d3f3f0f1dafaf90f05c18)。

发送操作码聚合器消息。

<a id="r_ga00b5e695503ba169a1b5ec626413b322"></a>

```c
void bt_mesh_op_agg_cli_seq_abort (void)
```

相关声明：[bt_mesh_op_agg_cli_seq_abort](#ga00b5e695503ba169a1b5ec626413b322)。

中止操作码聚合器上下文。

<a id="r_gadbc347b2dc3d78a4ac71d424f0623b6f"></a>

```c
bool bt_mesh_op_agg_cli_seq_is_started (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_op_agg_cli_seq_is_started](#gadbc347b2dc3d78a4ac71d424f0623b6f)。

检查操作码聚合器序列（Opcodes Aggregator Sequence）上下文是否已经启动。

<a id="r_ga4269bc6118371e2af0967841b18a02dd"></a>

```c
size_t bt_mesh_op_agg_cli_seq_tailroom (void)
```

相关声明：[bt_mesh_op_agg_cli_seq_tailroom](#ga4269bc6118371e2af0967841b18a02dd)。

获取操作码聚合器上下文的尾部可用空间（tailroom）。

<a id="r_ga83e44b062babcf0bdb343455e3eddf5f"></a>

```c
int32_t bt_mesh_op_agg_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_op_agg_cli_timeout_get](#ga83e44b062babcf0bdb343455e3eddf5f)。

获取当前传输超时值（transmission timeout）。

<a id="r_gaf70cebae8dbd6eb4ef6402585a90e0d5"></a>

```c
void bt_mesh_op_agg_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_op_agg_cli_timeout_set](#gaf70cebae8dbd6eb4ef6402585a90e0d5)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。

## 3.4\_详细说明（Detailed Documentation）

<a id="ga0a8dec4b4f53d1ec95db1efc4ab22f69"></a>

### `BT_MESH_MODEL_OP_AGG_CLI`

```c
#define BT_MESH_MODEL_OP_AGG_CLI
```

```c
#include <zephyr/bluetooth/mesh/op_agg_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_OP_AGG_CLI, _bt_mesh_op_agg_cli_op,  \
                 NULL, NULL, &_bt_mesh_op_agg_cli_cb)
```

操作码聚合器客户端（Opcodes Aggregator Client）模型的组成数据条目（composition data entry）。

<a id="ga00b5e695503ba169a1b5ec626413b322"></a>

### `bt_mesh_op_agg_cli_seq_abort()`

```c
void bt_mesh_op_agg_cli_seq_abort ( void )
```

```c
#include <zephyr/bluetooth/mesh/op_agg_cli.h>
```

中止操作码聚合器上下文。

<a id="gadbc347b2dc3d78a4ac71d424f0623b6f"></a>

### `bt_mesh_op_agg_cli_seq_is_started()`

```c
bool bt_mesh_op_agg_cli_seq_is_started ( void )
```

```c
#include <zephyr/bluetooth/mesh/op_agg_cli.h>
```

检查操作码聚合器序列（Opcodes Aggregator Sequence）上下文是否已经启动。

**返回（Returns）**：返回值：已启动时为 true，否则为 false。

<a id="gab151f44fcb5d3f3f0f1dafaf90f05c18"></a>

### `bt_mesh_op_agg_cli_seq_send()`

```c
int bt_mesh_op_agg_cli_seq_send ( void )
```

```c
#include <zephyr/bluetooth/mesh/op_agg_cli.h>
```

发送操作码聚合器消息。

使用先前配置的上下文，向目标节点发送聚合消息（aggregated message）。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gac1905d778362faf442a9538adca34a8c"></a>

### `bt_mesh_op_agg_cli_seq_start()`

```c
int bt_mesh_op_agg_cli_seq_start ( uint16_t net_idx, uint16_t app_idx, uint16_t dst, uint16_t elem_addr )
```

```c
#include <zephyr/bluetooth/mesh/op_agg_cli.h>
```

配置操作码聚合器（Opcodes Aggregator）上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络密钥（NetKey）索引。 |
| `app_idx` | 用于加密的应用密钥（AppKey）索引。 |
| `dst` | 目标操作码聚合器服务器（Opcodes Aggregator Server）地址。 |
| `elem_addr` | 序列消息（sequence message）的目标节点元素地址。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga4269bc6118371e2af0967841b18a02dd"></a>

### `bt_mesh_op_agg_cli_seq_tailroom()`

```c
size_t bt_mesh_op_agg_cli_seq_tailroom ( void )
```

```c
#include <zephyr/bluetooth/mesh/op_agg_cli.h>
```

获取操作码聚合器上下文的尾部可用空间（tailroom）。

**返回（Returns）**：返回值：操作码聚合器服务数据单元（SDU）的剩余尾部空间（tailroom）。

<a id="ga83e44b062babcf0bdb343455e3eddf5f"></a>

### `bt_mesh_op_agg_cli_timeout_get()`

```c
int32_t bt_mesh_op_agg_cli_timeout_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/op_agg_cli.h>
```

获取当前传输超时值（transmission timeout）。

**返回（Returns）**：返回值：配置的传输超时（transmission timeout），单位为毫秒。

<a id="gaf70cebae8dbd6eb4ef6402585a90e0d5"></a>

### `bt_mesh_op_agg_cli_timeout_set()`

```c
void bt_mesh_op_agg_cli_timeout_set ( int32_t timeout)
```

```c
#include <zephyr/bluetooth/mesh/op_agg_cli.h>
```

设置传输超时值（Transmission Timeout Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 新的传输超时。 |


## 3.5\_原页交叉引用（Cross References）

- [op_agg_cli.h](../api_file_system_device_reference/P034_zephyr__bluetooth__mesh__op_agg_cli.h_文件参考.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_OP_AGG_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gabac62a77e7d2d7677af21c33c8629187)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gabac62a77e7d2d7677af21c33c8629187"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_BMM350 API主题.md) · [返回大纲](大纲.md) · [下一章](P004_蓝牙 Mesh 私有信标客户端（Private Beacon Client）.md)
