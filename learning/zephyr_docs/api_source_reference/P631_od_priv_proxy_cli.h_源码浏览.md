---
id: learning.zephyr-docs.api-source-reference.page-631
title: od_priv_proxy_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/od__priv__proxy__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第631章\_od\_priv\_proxy\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/od__priv__proxy__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/od__priv__proxy__cli_8h.html)。

## 631.1\_原始可见代码（Source Code）

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
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="agroup__bt__mesh__od__priv__proxy__cli_html_ga11357595b2d837f6172a2ec98d1e9973"></a>
<a id="agroup__bt__mesh__od__priv__proxy__cli_html_ga9b239c221f8c74108e2a7e5276122e1f"></a>
<a id="agroup__bt__mesh__od__priv__proxy__cli_html_gad613c78e708f0df5aabda9e16fae6a2c"></a>
<a id="amesh_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ack__ctx_html"></a>
<a id="astructbt__mesh__od__priv__proxy__cli_html"></a>
<a id="astructbt__mesh__od__priv__proxy__cli_html_a8f172612abc904718018a6c2d9002e5e"></a>
<a id="astructbt__mesh__od__priv__proxy__cli_html_aeab540da0e42de4aa3e1550cd933f805"></a>
<a id="astructbt__mesh__od__priv__proxy__cli_html_aebd18bb98ded2e5dc3fca3fe121f3bc6"></a>

```c
/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_OD_PRIV_PROXY_CLI_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_OD_PRIV_PROXY_CLI_H_

#include <zephyr/bluetooth/mesh.h>

#ifdef __cplusplus
extern "C" {
#endif


struct bt_mesh_od_priv_proxy_cli {
        const struct bt_mesh_model *model;

        /* Internal parameters for tracking message responses. */
        struct bt_mesh_msg_ack_ctx ack_ctx;

        void (*od_status)(struct bt_mesh_od_priv_proxy_cli *cli, uint16_t addr, uint8_t state);
};

#define BT_MESH_MODEL_OD_PRIV_PROXY_CLI(cli_data)                                  \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_ON_DEMAND_PROXY_CLI,                     \
                         _bt_mesh_od_priv_proxy_cli_op, NULL, cli_data,            \
                         &_bt_mesh_od_priv_proxy_cli_cb)

int bt_mesh_od_priv_proxy_cli_get(uint16_t net_idx, uint16_t addr, uint8_t *val_rsp);

int bt_mesh_od_priv_proxy_cli_set(uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *val_rsp);

void bt_mesh_od_priv_proxy_cli_timeout_set(int32_t timeout);

extern const struct bt_mesh_model_op _bt_mesh_od_priv_proxy_cli_op[];
extern const struct bt_mesh_model_cb _bt_mesh_od_priv_proxy_cli_cb;


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_OD_PRIV_PROXY_CLI_H_ */
```

## 631.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 33 行

用于跟踪消息响应的内部参数（Internal parameters）。

### 注释 3：原第 108 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_OD_PRIV_PROXY_CLI_H_`。

## 631.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/od__priv__proxy__cli_8h.html)
- [zephyr/bluetooth/mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_od_priv_proxy_cli](../bluetooth_mesh_model_reference/P083_bt_mesh_od_priv_proxy_cli_结构体.md)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [model](../bluetooth_mesh_model_reference/P083_bt_mesh_od_priv_proxy_cli_结构体.md#aeab540da0e42de4aa3e1550cd933f805)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [ack_ctx](../bluetooth_mesh_model_reference/P083_bt_mesh_od_priv_proxy_cli_结构体.md#a8f172612abc904718018a6c2d9002e5e)
- [od_status](../bluetooth_mesh_model_reference/P083_bt_mesh_od_priv_proxy_cli_结构体.md#aebd18bb98ded2e5dc3fca3fe121f3bc6)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_mesh_od_priv_proxy_cli_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#ga11357595b2d837f6172a2ec98d1e9973)
- [bt_mesh_od_priv_proxy_cli_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#ga9b239c221f8c74108e2a7e5276122e1f)
- [bt_mesh_od_priv_proxy_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#gad613c78e708f0df5aabda9e16fae6a2c)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_od_priv_proxy_cli::ack_ctx](../bluetooth_mesh_model_reference/P083_bt_mesh_od_priv_proxy_cli_结构体.md#a8f172612abc904718018a6c2d9002e5e)
- [bt_mesh_od_priv_proxy_cli::model](../bluetooth_mesh_model_reference/P083_bt_mesh_od_priv_proxy_cli_结构体.md#aeab540da0e42de4aa3e1550cd933f805)
- [bt_mesh_od_priv_proxy_cli::od_status](../bluetooth_mesh_model_reference/P083_bt_mesh_od_priv_proxy_cli_结构体.md#aebd18bb98ded2e5dc3fca3fe121f3bc6)

---

[上一章](P630_nxp_vref.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P632_od_priv_proxy_srv.h_源码浏览.md)
