---
id: learning.zephyr-docs.api-file-service-reference.page-52
title: zephyr__bluetooth__mesh__sol_pdu_rpl_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sol__pdu__rpl__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_zephyr\_\_bluetooth\_\_mesh\_\_sol\_pdu\_rpl\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sol__pdu__rpl__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh请求PDU重放保护列表客户端（Solicitation PDU RPL Client）模型API的头文件。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh.h>
```

查看此文件的源码。

蓝牙Mesh请求PDU重放保护列表客户端（Solicitation PDU RPL Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 52.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fsol_5Fpdu_5Frpl_5Fcli"></a>

```c
struct bt_mesh_sol_pdu_rpl_cli
```

相关声明：[bt_mesh_sol_pdu_rpl_cli](../bluetooth_mesh_model_reference/P100_bt_mesh_sol_pdu_rpl_cli_结构体.md)。

请求PDU重放保护列表客户端（Solicitation PDU RPL Client）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 52.2\_宏定义（Macros）

<a id="r_gac5969e20994b07977484391ac2d7bacb"></a>

```c
#define BT_MESH_MODEL_SOL_PDU_RPL_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_SOL_PDU_RPL_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#gac5969e20994b07977484391ac2d7bacb)。

征询协议数据单元重放保护列表客户端模型（Solicitation PDU RPL Client Model）的组成数据条目（Composition Data Entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 52.3\_函数（Functions）

<a id="r_gae7e8a0e364c6695a467a64cd89627d81"></a>

```c
int bt_mesh_sol_pdu_rpl_clear (struct bt_mesh_msg_ctx *ctx, uint16_t range_start, uint8_t range_len, uint16_t *start_rsp, uint8_t *len_rsp)
```

相关声明：[bt_mesh_sol_pdu_rpl_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#gae7e8a0e364c6695a467a64cd89627d81)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从征询协议数据单元重放保护列表（Solicitation PDU RPL）中移除给定地址范围内的条目（Entries）。

<a id="r_ga68fb70fbfb87e76ef6fdb5ac8a1a9506"></a>

```c
int bt_mesh_sol_pdu_rpl_clear_unack (struct bt_mesh_msg_ctx *ctx, uint16_t range_start, uint8_t range_len)
```

相关声明：[bt_mesh_sol_pdu_rpl_clear_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#ga68fb70fbfb87e76ef6fdb5ac8a1a9506)、[bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从征询协议数据单元重放保护列表（Solicitation PDU RPL）中移除给定地址范围内的条目，采用无确认方式（Unacknowledged）。

<a id="r_gadabdbd95f39a498307e3ca9e50acfeb9"></a>

```c
void bt_mesh_sol_pdu_rpl_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_sol_pdu_rpl_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#gadabdbd95f39a498307e3ca9e50acfeb9)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。


## 52.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh.h](../api_source_reference/P514_mesh.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P805_sol_pdu_rpl_cli.h_源码浏览.md)
- [bt_mesh_sol_pdu_rpl_cli](../bluetooth_mesh_model_reference/P100_bt_mesh_sol_pdu_rpl_cli_结构体.md)
- [BT_MESH_MODEL_SOL_PDU_RPL_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#gac5969e20994b07977484391ac2d7bacb)
- [bt_mesh_sol_pdu_rpl_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#gae7e8a0e364c6695a467a64cd89627d81)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_sol_pdu_rpl_clear_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#ga68fb70fbfb87e76ef6fdb5ac8a1a9506)
- [bt_mesh_sol_pdu_rpl_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#gadabdbd95f39a498307e3ca9e50acfeb9)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)

<a id="header-details"></a>

---

[上一章](P051_zephyr__net__socket_net_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P053_zephyr__bluetooth__mesh__statistic.h_文件参考.md)
