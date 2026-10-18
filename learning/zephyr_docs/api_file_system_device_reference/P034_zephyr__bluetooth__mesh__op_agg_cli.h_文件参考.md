---
id: learning.zephyr-docs.api-file-system-device-reference.page-34
title: zephyr__bluetooth__mesh__op_agg_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/op__agg__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zephyr\_\_bluetooth\_\_mesh\_\_op\_agg\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/op__agg__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh操作码聚合器客户端（Opcodes Aggregator Client）模型API的头文件。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh.h>
```

查看此文件的源码。

蓝牙Mesh操作码聚合器客户端（Opcodes Aggregator Client）模型API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 34.1\_宏定义（Macros）

<a id="r_ga0a8dec4b4f53d1ec95db1efc4ab22f69"></a>

```c
#define BT_MESH_MODEL_OP_AGG_CLI
```

相关声明：[BT_MESH_MODEL_OP_AGG_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#ga0a8dec4b4f53d1ec95db1efc4ab22f69)。

操作码聚合器客户端（Opcodes Aggregator Client）模型的组成数据条目（composition data entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 34.2\_函数（Functions）

<a id="r_gac1905d778362faf442a9538adca34a8c"></a>

```c
int bt_mesh_op_agg_cli_seq_start (uint16_t net_idx, uint16_t app_idx, uint16_t dst, uint16_t elem_addr)
```

相关声明：[bt_mesh_op_agg_cli_seq_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gac1905d778362faf442a9538adca34a8c)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

配置操作码聚合器（Opcodes Aggregator）上下文。

<a id="r_gab151f44fcb5d3f3f0f1dafaf90f05c18"></a>

```c
int bt_mesh_op_agg_cli_seq_send (void)
```

相关声明：[bt_mesh_op_agg_cli_seq_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gab151f44fcb5d3f3f0f1dafaf90f05c18)。

发送操作码聚合器消息。

<a id="r_ga00b5e695503ba169a1b5ec626413b322"></a>

```c
void bt_mesh_op_agg_cli_seq_abort (void)
```

相关声明：[bt_mesh_op_agg_cli_seq_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#ga00b5e695503ba169a1b5ec626413b322)。

中止操作码聚合器上下文。

<a id="r_gadbc347b2dc3d78a4ac71d424f0623b6f"></a>

```c
bool bt_mesh_op_agg_cli_seq_is_started (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_op_agg_cli_seq_is_started](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gadbc347b2dc3d78a4ac71d424f0623b6f)。

检查操作码聚合器序列（Opcodes Aggregator Sequence）上下文是否已经启动。

<a id="r_ga4269bc6118371e2af0967841b18a02dd"></a>

```c
size_t bt_mesh_op_agg_cli_seq_tailroom (void)
```

相关声明：[bt_mesh_op_agg_cli_seq_tailroom](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#ga4269bc6118371e2af0967841b18a02dd)。

获取操作码聚合器上下文的尾部可用空间（tailroom）。

<a id="r_ga83e44b062babcf0bdb343455e3eddf5f"></a>

```c
int32_t bt_mesh_op_agg_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_op_agg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#ga83e44b062babcf0bdb343455e3eddf5f)。

获取当前传输超时值（transmission timeout）。

<a id="r_gaf70cebae8dbd6eb4ef6402585a90e0d5"></a>

```c
void bt_mesh_op_agg_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_op_agg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gaf70cebae8dbd6eb4ef6402585a90e0d5)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。


## 34.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh.h](../api_source_reference/P514_mesh.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P633_op_agg_cli.h_源码浏览.md)
- [BT_MESH_MODEL_OP_AGG_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#ga0a8dec4b4f53d1ec95db1efc4ab22f69)
- [bt_mesh_op_agg_cli_seq_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gac1905d778362faf442a9538adca34a8c)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_op_agg_cli_seq_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gab151f44fcb5d3f3f0f1dafaf90f05c18)
- [bt_mesh_op_agg_cli_seq_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#ga00b5e695503ba169a1b5ec626413b322)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_op_agg_cli_seq_is_started](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gadbc347b2dc3d78a4ac71d424f0623b6f)
- [bt_mesh_op_agg_cli_seq_tailroom](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#ga4269bc6118371e2af0967841b18a02dd)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_op_agg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#ga83e44b062babcf0bdb343455e3eddf5f)
- [bt_mesh_op_agg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gaf70cebae8dbd6eb4ef6402585a90e0d5)

<a id="header-details"></a>

---

[上一章](P033_zephyr__drivers__misc__nxp_flexio__nxp_flexio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P035_zephyr__dt-bindings__interrupt-controller__openisa-intmux.h_文件参考.md)
