---
id: learning.zephyr-docs.api-source-reference.page-77
title: brg_cfg_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_brg\_cfg\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__cli_8h.html)。

## 77.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00316"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="abrg__cfg_8h_html"></a>
<a id="agroup__bt__mesh__brg__cfg__cli_html_ga04bb227d14d4f478e4f32a8ca87d2c38"></a>
<a id="agroup__bt__mesh__brg__cfg__cli_html_ga252994dd3119387703af45c0932ef253"></a>
<a id="agroup__bt__mesh__brg__cfg__cli_html_ga6643d4d043af4b0cb30470a5c9a46f38"></a>
<a id="agroup__bt__mesh__brg__cfg__cli_html_ga6a4507190e425013a9d21ea0a1be1b5c"></a>
<a id="agroup__bt__mesh__brg__cfg__cli_html_ga8f055e8ee384e8ea4887a56720959b26"></a>
<a id="agroup__bt__mesh__brg__cfg__cli_html_ga99951987bd6787e3e1348d8e51e64fe5"></a>
<a id="agroup__bt__mesh__brg__cfg__cli_html_gabdb919dcf177b8d5c8a28b057469bf18"></a>
<a id="agroup__bt__mesh__brg__cfg__cli_html_gacd3811be7b87d2d9187aed6c50945b85"></a>
<a id="agroup__bt__mesh__brg__cfg__cli_html_gad30102a29983545ec79f178b1390ce74"></a>
<a id="agroup__bt__mesh__brg__cfg_html_ga7bddcbe2b1196df6a1c80d8c213866f9"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__brg__cfg__cli__cb_html"></a>
<a id="astructbt__mesh__brg__cfg__cli__cb_html_a3817e30dd90b161a7442604207ed0ba8"></a>
<a id="astructbt__mesh__brg__cfg__cli__cb_html_a608b74d78f2f4bb06130f40071ac93af"></a>
<a id="astructbt__mesh__brg__cfg__cli__cb_html_a947e2169ed2cb0964c082bd82c1b0943"></a>
<a id="astructbt__mesh__brg__cfg__cli__cb_html_ac045febf91cc95982985e6de094e403b"></a>
<a id="astructbt__mesh__brg__cfg__cli__cb_html_afe8e0a5ed681630e826ff0aa3889cd88"></a>
<a id="astructbt__mesh__brg__cfg__cli_html"></a>
<a id="astructbt__mesh__brg__cfg__cli_html_a5a7b181b3d026de617085efc0c671474"></a>
<a id="astructbt__mesh__brg__cfg__cli_html_a6cbc5bb1a79c9951b4cd2f16e06d1beb"></a>
<a id="astructbt__mesh__brg__cfg__cli_html_ac0f982fa211bb6660a3159f7e796abb7"></a>
<a id="astructbt__mesh__brg__cfg__filter__netkey_html"></a>
<a id="astructbt__mesh__brg__cfg__subnets__list_html"></a>
<a id="astructbt__mesh__brg__cfg__table__entry_html"></a>
<a id="astructbt__mesh__brg__cfg__table__list_html"></a>
<a id="astructbt__mesh__brg__cfg__table__status_html"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ack__ctx_html"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_CLI_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_CLI_H__

#include <zephyr/bluetooth/mesh/brg_cfg.h>

#ifdef __cplusplus
extern "C" {
#endif


struct bt_mesh_brg_cfg_cli;

#define BT_MESH_MODEL_BRG_CFG_CLI(_cli)                                                            \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_BRG_CFG_CLI, _bt_mesh_brg_cfg_cli_op, NULL, _cli,        \
                         &_bt_mesh_brg_cfg_cli_cb)

struct bt_mesh_brg_cfg_cli_cb {
        void (*bridge_status)(struct bt_mesh_brg_cfg_cli *cli, uint16_t addr,
                              enum bt_mesh_brg_cfg_state status);

        void (*table_size_status)(struct bt_mesh_brg_cfg_cli *cli, uint16_t addr, uint16_t size);

        void (*table_status)(struct bt_mesh_brg_cfg_cli *cli, uint16_t addr,
                             struct bt_mesh_brg_cfg_table_status *rsp);

        void (*subnets_list)(struct bt_mesh_brg_cfg_cli *cli, uint16_t addr,
                             struct bt_mesh_brg_cfg_subnets_list *rsp);

        void (*table_list)(struct bt_mesh_brg_cfg_cli *cli, uint16_t addr,
                           struct bt_mesh_brg_cfg_table_list *rsp);
};

struct bt_mesh_brg_cfg_cli {
        const struct bt_mesh_model *model;

        const struct bt_mesh_brg_cfg_cli_cb *cb;

        /* Internal parameters for tracking message responses. */
        struct bt_mesh_msg_ack_ctx ack_ctx;
};

int bt_mesh_brg_cfg_cli_get(uint16_t net_idx, uint16_t addr, enum bt_mesh_brg_cfg_state *status);

int bt_mesh_brg_cfg_cli_set(uint16_t net_idx, uint16_t addr, enum bt_mesh_brg_cfg_state val,
                            enum bt_mesh_brg_cfg_state *status);

int bt_mesh_brg_cfg_cli_table_size_get(uint16_t net_idx, uint16_t addr, uint16_t *size);

int bt_mesh_brg_cfg_cli_table_add(uint16_t net_idx, uint16_t addr,
                                  struct bt_mesh_brg_cfg_table_entry *entry,
                                  struct bt_mesh_brg_cfg_table_status *rsp);

int bt_mesh_brg_cfg_cli_table_remove(uint16_t net_idx, uint16_t addr, uint16_t net_idx1,
                                     uint16_t net_idx2, uint16_t addr1, uint16_t addr2,
                                     struct bt_mesh_brg_cfg_table_status *rsp);

int bt_mesh_brg_cfg_cli_subnets_get(uint16_t net_idx, uint16_t addr,
                                    struct bt_mesh_brg_cfg_filter_netkey filter_net_idx,
                                    uint8_t start_idx, struct bt_mesh_brg_cfg_subnets_list *rsp);

int bt_mesh_brg_cfg_cli_table_get(uint16_t net_idx, uint16_t addr, uint16_t net_idx1,
                                  uint16_t net_idx2, uint16_t start_idx,
                                  struct bt_mesh_brg_cfg_table_list *rsp);

int32_t bt_mesh_brg_cfg_cli_timeout_get(void);

void bt_mesh_brg_cfg_cli_timeout_set(int32_t timeout);

extern const struct bt_mesh_model_op _bt_mesh_brg_cfg_cli_op[];
extern const struct bt_mesh_model_cb _bt_mesh_brg_cfg_cli_cb;


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_CLI_H__ */
```

## 77.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 110 行

用于跟踪消息响应的内部参数（Internal parameters）。

### 注释 3：原第 325 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_BRG_CFG_CLI_H__`。

## 77.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__cli_8h.html)
- [zephyr/bluetooth/mesh/brg_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h.html)
- [bt_mesh_brg_cfg_cli](../bluetooth_mesh_model_reference/P016_bt_mesh_brg_cfg_cli_结构体.md)
- [bt_mesh_brg_cfg_cli_cb](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md)
- [bridge_status](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md#ac045febf91cc95982985e6de094e403b)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_brg_cfg_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#ga7bddcbe2b1196df6a1c80d8c213866f9)
- [table_size_status](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md#afe8e0a5ed681630e826ff0aa3889cd88)
- [table_status](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md#a608b74d78f2f4bb06130f40071ac93af)
- [bt_mesh_brg_cfg_table_status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md)
- [subnets_list](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md#a947e2169ed2cb0964c082bd82c1b0943)
- [bt_mesh_brg_cfg_subnets_list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md)
- [table_list](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md#a3817e30dd90b161a7442604207ed0ba8)
- [bt_mesh_brg_cfg_table_list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [model](../bluetooth_mesh_model_reference/P016_bt_mesh_brg_cfg_cli_结构体.md#a6cbc5bb1a79c9951b4cd2f16e06d1beb)
- [cb](../bluetooth_mesh_model_reference/P016_bt_mesh_brg_cfg_cli_结构体.md#a5a7b181b3d026de617085efc0c671474)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [ack_ctx](../bluetooth_mesh_model_reference/P016_bt_mesh_brg_cfg_cli_结构体.md#ac0f982fa211bb6660a3159f7e796abb7)
- [bt_mesh_brg_cfg_cli_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga6a4507190e425013a9d21ea0a1be1b5c)
- [bt_mesh_brg_cfg_cli_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga6643d4d043af4b0cb30470a5c9a46f38)
- [bt_mesh_brg_cfg_cli_table_size_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga99951987bd6787e3e1348d8e51e64fe5)
- [bt_mesh_brg_cfg_cli_table_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga8f055e8ee384e8ea4887a56720959b26)
- [bt_mesh_brg_cfg_table_entry](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md)
- [bt_mesh_brg_cfg_cli_table_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#gabdb919dcf177b8d5c8a28b057469bf18)
- [bt_mesh_brg_cfg_cli_subnets_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga04bb227d14d4f478e4f32a8ca87d2c38)
- [bt_mesh_brg_cfg_filter_netkey](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_brg_cfg_cli_table_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#gacd3811be7b87d2d9187aed6c50945b85)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_brg_cfg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga252994dd3119387703af45c0932ef253)
- [bt_mesh_brg_cfg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#gad30102a29983545ec79f178b1390ce74)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [brg_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h.html)
- [bt_mesh_brg_cfg_cli_cb::table_list](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md#a3817e30dd90b161a7442604207ed0ba8)
- [bt_mesh_brg_cfg_cli_cb::table_status](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md#a608b74d78f2f4bb06130f40071ac93af)
- [bt_mesh_brg_cfg_cli_cb::subnets_list](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md#a947e2169ed2cb0964c082bd82c1b0943)
- [bt_mesh_brg_cfg_cli_cb::bridge_status](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md#ac045febf91cc95982985e6de094e403b)
- [bt_mesh_brg_cfg_cli_cb::table_size_status](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md#afe8e0a5ed681630e826ff0aa3889cd88)
- [bt_mesh_brg_cfg_cli::cb](../bluetooth_mesh_model_reference/P016_bt_mesh_brg_cfg_cli_结构体.md#a5a7b181b3d026de617085efc0c671474)
- [bt_mesh_brg_cfg_cli::model](../bluetooth_mesh_model_reference/P016_bt_mesh_brg_cfg_cli_结构体.md#a6cbc5bb1a79c9951b4cd2f16e06d1beb)
- [bt_mesh_brg_cfg_cli::ack_ctx](../bluetooth_mesh_model_reference/P016_bt_mesh_brg_cfg_cli_结构体.md#ac0f982fa211bb6660a3159f7e796abb7)

---

[上一章](P076_bos.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P078_brg_cfg_srv.h_源码浏览.md)
