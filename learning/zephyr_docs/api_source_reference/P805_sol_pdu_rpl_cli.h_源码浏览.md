---
id: learning.zephyr-docs.api-source-reference.page-805
title: sol_pdu_rpl_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sol__pdu__rpl__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第805章\_sol\_pdu\_rpl\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sol__pdu__rpl__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sol__pdu__rpl__cli_8h.html)。

## 805.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00027"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="agroup__bt__mesh__sol__pdu__rpl__cli_html_ga68fb70fbfb87e76ef6fdb5ac8a1a9506"></a>
<a id="agroup__bt__mesh__sol__pdu__rpl__cli_html_gadabdbd95f39a498307e3ca9e50acfeb9"></a>
<a id="agroup__bt__mesh__sol__pdu__rpl__cli_html_gae7e8a0e364c6695a467a64cd89627d81"></a>
<a id="amesh_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ack__ctx_html"></a>
<a id="astructbt__mesh__msg__ctx_html"></a>
<a id="astructbt__mesh__sol__pdu__rpl__cli_html"></a>
<a id="astructbt__mesh__sol__pdu__rpl__cli_html_a272ff5ae0930f51c9175d99f5c9066e2"></a>
<a id="astructbt__mesh__sol__pdu__rpl__cli_html_a291134f4b6acc60671307ef3b53c4ac8"></a>
<a id="astructbt__mesh__sol__pdu__rpl__cli_html_a6c734589ee3361bfc071da55521a6dee"></a>

```c
/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_SOL_PDU_RPL_CLI_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_SOL_PDU_RPL_CLI_H_

#include <zephyr/bluetooth/mesh.h>

#ifdef __cplusplus
extern "C" {
#endif


struct bt_mesh_sol_pdu_rpl_cli {
        const struct bt_mesh_model *model;

        /* Internal parameters for tracking message responses. */
        struct bt_mesh_msg_ack_ctx ack_ctx;

        void (*srpl_status)(struct bt_mesh_sol_pdu_rpl_cli *cli, uint16_t addr,
                            uint16_t range_start, uint8_t range_length);
};

#define BT_MESH_MODEL_SOL_PDU_RPL_CLI(cli_data)                             \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_SOL_PDU_RPL_CLI,                  \
                         _bt_mesh_sol_pdu_rpl_cli_op, NULL, cli_data,       \
                         &_bt_mesh_sol_pdu_rpl_cli_cb)

int bt_mesh_sol_pdu_rpl_clear(struct bt_mesh_msg_ctx *ctx, uint16_t range_start,
                              uint8_t range_len, uint16_t *start_rsp, uint8_t *len_rsp);


int bt_mesh_sol_pdu_rpl_clear_unack(struct bt_mesh_msg_ctx *ctx, uint16_t range_start,
                                    uint8_t range_len);

void bt_mesh_sol_pdu_rpl_cli_timeout_set(int32_t timeout);

extern const struct bt_mesh_model_op _bt_mesh_sol_pdu_rpl_cli_op[];
extern const struct bt_mesh_model_cb _bt_mesh_sol_pdu_rpl_cli_cb;


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_SOL_PDU_RPL_CLI_H_ */
```

## 805.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 33 行

用于跟踪消息响应的内部参数（Internal parameters）。

### 注释 3：原第 110 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_SOL_PDU_RPL_CLI_H_`。

## 805.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sol__pdu__rpl__cli_8h.html)
- [zephyr/bluetooth/mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_sol_pdu_rpl_cli](../bluetooth_mesh_model_reference/P100_bt_mesh_sol_pdu_rpl_cli_结构体.md)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [model](../bluetooth_mesh_model_reference/P100_bt_mesh_sol_pdu_rpl_cli_结构体.md#a272ff5ae0930f51c9175d99f5c9066e2)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [ack_ctx](../bluetooth_mesh_model_reference/P100_bt_mesh_sol_pdu_rpl_cli_结构体.md#a291134f4b6acc60671307ef3b53c4ac8)
- [srpl_status](../bluetooth_mesh_model_reference/P100_bt_mesh_sol_pdu_rpl_cli_结构体.md#a6c734589ee3361bfc071da55521a6dee)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_sol_pdu_rpl_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#gae7e8a0e364c6695a467a64cd89627d81)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [bt_mesh_sol_pdu_rpl_clear_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#ga68fb70fbfb87e76ef6fdb5ac8a1a9506)
- [bt_mesh_sol_pdu_rpl_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__cli.html#gadabdbd95f39a498307e3ca9e50acfeb9)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_sol_pdu_rpl_cli::model](../bluetooth_mesh_model_reference/P100_bt_mesh_sol_pdu_rpl_cli_结构体.md#a272ff5ae0930f51c9175d99f5c9066e2)
- [bt_mesh_sol_pdu_rpl_cli::ack_ctx](../bluetooth_mesh_model_reference/P100_bt_mesh_sol_pdu_rpl_cli_结构体.md#a291134f4b6acc60671307ef3b53c4ac8)
- [bt_mesh_sol_pdu_rpl_cli::srpl_status](../bluetooth_mesh_model_reference/P100_bt_mesh_sol_pdu_rpl_cli_结构体.md#a6c734589ee3361bfc071da55521a6dee)

---

[上一章](P804_socketutils.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P806_sol_pdu_rpl_srv.h_源码浏览.md)
