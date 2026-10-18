---
id: learning.zephyr-docs.api-source-reference.page-672
title: priv_beacon_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第672章\_priv\_beacon\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h.html)。

## 672.1\_原始可见代码（Source Code）

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
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="foldopen00098"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="agroup__bt__mesh__priv__beacon__cli_html_ga2a581e49b8812bd78604fc829bd1d79a"></a>
<a id="agroup__bt__mesh__priv__beacon__cli_html_ga389626a517c1bb9cae31501663725483"></a>
<a id="agroup__bt__mesh__priv__beacon__cli_html_ga76d797a76d8f8fda31feacce840a6f9e"></a>
<a id="agroup__bt__mesh__priv__beacon__cli_html_ga838880ae8391b33d0481fba069ea921b"></a>
<a id="agroup__bt__mesh__priv__beacon__cli_html_ga8a535d31954d8871fed557808b6abc71"></a>
<a id="agroup__bt__mesh__priv__beacon__cli_html_gadd6fc3321cd536771921566bbc650396"></a>
<a id="amesh_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ack__ctx_html"></a>
<a id="astructbt__mesh__priv__beacon__cli__cb_html"></a>
<a id="astructbt__mesh__priv__beacon__cli__cb_html_a825bb5dee44075a8b6d14efc5f68c372"></a>
<a id="astructbt__mesh__priv__beacon__cli__cb_html_aa1206f9a75beb79449e5a1bad8e62f41"></a>
<a id="astructbt__mesh__priv__beacon__cli__cb_html_ab4b58af5af27be22dc395df4b2fd35c4"></a>
<a id="astructbt__mesh__priv__beacon__cli_html"></a>
<a id="astructbt__mesh__priv__beacon__cli_html_a506b13407e466908d8a8684386bf3927"></a>
<a id="astructbt__mesh__priv__beacon__cli_html_aa4105b00e2a3ad9027b888f0ebbea23e"></a>
<a id="astructbt__mesh__priv__beacon__cli_html_ab281b9ac10c54068372f90bccfe07feb"></a>
<a id="astructbt__mesh__priv__beacon_html"></a>
<a id="astructbt__mesh__priv__beacon_html_a1a4972527afde6f9aa5c7726d85ddd45"></a>
<a id="astructbt__mesh__priv__beacon_html_ac38424ed4ebcd69307568763ff2d6ffb"></a>
<a id="astructbt__mesh__priv__node__id_html"></a>
<a id="astructbt__mesh__priv__node__id_html_a49c60fedb24de61a399f3da967f4ac7c"></a>
<a id="astructbt__mesh__priv__node__id_html_a5bd318e61b974a94765e0d28db15994f"></a>
<a id="astructbt__mesh__priv__node__id_html_ab772f79daa361a9199f8445b7bda7e44"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_PRIV_BEACON_CLI_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_PRIV_BEACON_CLI_H__

#include <zephyr/bluetooth/mesh.h>

#ifdef __cplusplus
extern "C" {
#endif


#define BT_MESH_MODEL_PRIV_BEACON_CLI(cli_data)                                \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_PRIV_BEACON_CLI,                     \
                         bt_mesh_priv_beacon_cli_op, NULL, cli_data,           \
                         &bt_mesh_priv_beacon_cli_cb)

struct bt_mesh_priv_beacon_cli;

struct bt_mesh_priv_beacon {
        uint8_t enabled;
        uint8_t rand_interval;
};

struct bt_mesh_priv_node_id {
        uint16_t net_idx;
        uint8_t state;
        uint8_t status;
};

struct bt_mesh_priv_beacon_cli_cb {
        void (*priv_beacon_status)(struct bt_mesh_priv_beacon_cli *cli, uint16_t addr,
                                   struct bt_mesh_priv_beacon *priv_beacon);

        void (*priv_gatt_proxy_status)(struct bt_mesh_priv_beacon_cli *cli, uint16_t addr,
                                       uint8_t gatt_proxy);

        void (*priv_node_id_status)(struct bt_mesh_priv_beacon_cli *cli, uint16_t addr,
                                    struct bt_mesh_priv_node_id *priv_node_id);
};

struct bt_mesh_priv_beacon_cli {
        const struct bt_mesh_model *model;

        /* Internal parameters for tracking message responses. */
        struct bt_mesh_msg_ack_ctx ack_ctx;

        const struct bt_mesh_priv_beacon_cli_cb *cb;
};

int bt_mesh_priv_beacon_cli_set(uint16_t net_idx, uint16_t addr,
                                struct bt_mesh_priv_beacon *val,
                                struct bt_mesh_priv_beacon *rsp);

int bt_mesh_priv_beacon_cli_get(uint16_t net_idx, uint16_t addr,
                                struct bt_mesh_priv_beacon *val);

int bt_mesh_priv_beacon_cli_gatt_proxy_set(uint16_t net_idx, uint16_t addr,
                                           uint8_t val, uint8_t *rsp);

int bt_mesh_priv_beacon_cli_gatt_proxy_get(uint16_t net_idx, uint16_t addr,
                                           uint8_t *val);

int bt_mesh_priv_beacon_cli_node_id_set(uint16_t net_idx, uint16_t addr,
                                        struct bt_mesh_priv_node_id *val,
                                        struct bt_mesh_priv_node_id *rsp);

int bt_mesh_priv_beacon_cli_node_id_get(uint16_t net_idx, uint16_t addr,
                                        uint16_t key_net_idx,
                                        struct bt_mesh_priv_node_id *val);

extern const struct bt_mesh_model_op bt_mesh_priv_beacon_cli_op[];
extern const struct bt_mesh_model_cb bt_mesh_priv_beacon_cli_cb;


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_PRIV_BEACON_CLI_H__ */
```

## 672.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 101 行

用于跟踪消息响应的内部参数（Internal parameters）。

### 注释 3：原第 204 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_PRIV_BEACON_CLI_H__`。

## 672.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h.html)
- [zephyr/bluetooth/mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_priv_beacon_cli](../bluetooth_mesh_model_reference/P085_bt_mesh_priv_beacon_cli_结构体.md)
- [bt_mesh_priv_beacon](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [enabled](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md#ac38424ed4ebcd69307568763ff2d6ffb)
- [rand_interval](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md#a1a4972527afde6f9aa5c7726d85ddd45)
- [bt_mesh_priv_node_id](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_idx](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md#ab772f79daa361a9199f8445b7bda7e44)
- [state](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md#a5bd318e61b974a94765e0d28db15994f)
- [status](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md#a49c60fedb24de61a399f3da967f4ac7c)
- [bt_mesh_priv_beacon_cli_cb](../bluetooth_mesh_model_reference/P086_bt_mesh_priv_beacon_cli_cb_结构体.md)
- [priv_beacon_status](../bluetooth_mesh_model_reference/P086_bt_mesh_priv_beacon_cli_cb_结构体.md#ab4b58af5af27be22dc395df4b2fd35c4)
- [priv_gatt_proxy_status](../bluetooth_mesh_model_reference/P086_bt_mesh_priv_beacon_cli_cb_结构体.md#a825bb5dee44075a8b6d14efc5f68c372)
- [priv_node_id_status](../bluetooth_mesh_model_reference/P086_bt_mesh_priv_beacon_cli_cb_结构体.md#aa1206f9a75beb79449e5a1bad8e62f41)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [model](../bluetooth_mesh_model_reference/P085_bt_mesh_priv_beacon_cli_结构体.md#a506b13407e466908d8a8684386bf3927)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [ack_ctx](../bluetooth_mesh_model_reference/P085_bt_mesh_priv_beacon_cli_结构体.md#aa4105b00e2a3ad9027b888f0ebbea23e)
- [cb](../bluetooth_mesh_model_reference/P085_bt_mesh_priv_beacon_cli_结构体.md#ab281b9ac10c54068372f90bccfe07feb)
- [bt_mesh_priv_beacon_cli_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga8a535d31954d8871fed557808b6abc71)
- [bt_mesh_priv_beacon_cli_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga76d797a76d8f8fda31feacce840a6f9e)
- [bt_mesh_priv_beacon_cli_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga389626a517c1bb9cae31501663725483)
- [bt_mesh_priv_beacon_cli_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga838880ae8391b33d0481fba069ea921b)
- [bt_mesh_priv_beacon_cli_node_id_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#ga2a581e49b8812bd78604fc829bd1d79a)
- [bt_mesh_priv_beacon_cli_node_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__cli.html#gadd6fc3321cd536771921566bbc650396)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_priv_beacon_cli_cb::priv_gatt_proxy_status](../bluetooth_mesh_model_reference/P086_bt_mesh_priv_beacon_cli_cb_结构体.md#a825bb5dee44075a8b6d14efc5f68c372)
- [bt_mesh_priv_beacon_cli_cb::priv_node_id_status](../bluetooth_mesh_model_reference/P086_bt_mesh_priv_beacon_cli_cb_结构体.md#aa1206f9a75beb79449e5a1bad8e62f41)
- [bt_mesh_priv_beacon_cli_cb::priv_beacon_status](../bluetooth_mesh_model_reference/P086_bt_mesh_priv_beacon_cli_cb_结构体.md#ab4b58af5af27be22dc395df4b2fd35c4)
- [bt_mesh_priv_beacon_cli::model](../bluetooth_mesh_model_reference/P085_bt_mesh_priv_beacon_cli_结构体.md#a506b13407e466908d8a8684386bf3927)
- [bt_mesh_priv_beacon_cli::ack_ctx](../bluetooth_mesh_model_reference/P085_bt_mesh_priv_beacon_cli_结构体.md#aa4105b00e2a3ad9027b888f0ebbea23e)
- [bt_mesh_priv_beacon_cli::cb](../bluetooth_mesh_model_reference/P085_bt_mesh_priv_beacon_cli_结构体.md#ab281b9ac10c54068372f90bccfe07feb)
- [bt_mesh_priv_beacon::rand_interval](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md#a1a4972527afde6f9aa5c7726d85ddd45)
- [bt_mesh_priv_beacon::enabled](../bluetooth_mesh_model_reference/P084_bt_mesh_priv_beacon_结构体.md#ac38424ed4ebcd69307568763ff2d6ffb)
- [bt_mesh_priv_node_id::status](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md#a49c60fedb24de61a399f3da967f4ac7c)
- [bt_mesh_priv_node_id::state](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md#a5bd318e61b974a94765e0d28db15994f)
- [bt_mesh_priv_node_id::net_idx](../bluetooth_mesh_model_reference/P087_bt_mesh_priv_node_id_结构体.md#ab772f79daa361a9199f8445b7bda7e44)

---

[上一章](P671_printk-hooks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P673_priv_beacon_srv.h_源码浏览.md)
