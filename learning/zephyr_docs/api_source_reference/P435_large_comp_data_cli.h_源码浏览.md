---
id: learning.zephyr-docs.api-source-reference.page-435
title: large_comp_data_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第435章\_large\_comp\_data\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__cli_8h.html)。

## 435.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="agroup__bt__mesh__large__comp__data__cli_html_ga4073eb48c43460804705d80ac0919864"></a>
<a id="agroup__bt__mesh__large__comp__data__cli_html_gaf505ee14246746fc245a34328443d1c6"></a>
<a id="amesh_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__large__comp__data__cli__cb_html"></a>
<a id="astructbt__mesh__large__comp__data__cli__cb_html_ab0e17df5eb165a44d70542b8edd36ab9"></a>
<a id="astructbt__mesh__large__comp__data__cli__cb_html_ade54d137534ffb2274e366140f6cbd3c"></a>
<a id="astructbt__mesh__large__comp__data__cli_html"></a>
<a id="astructbt__mesh__large__comp__data__cli_html_a39d9086c8d9803f939c6103e613699b1"></a>
<a id="astructbt__mesh__large__comp__data__cli_html_a4401ff19edfe69c018dd0dbb6f81dc0d"></a>
<a id="astructbt__mesh__large__comp__data__cli_html_afec070cb549d56b3900c4df1e14656ed"></a>
<a id="astructbt__mesh__large__comp__data__rsp_html"></a>
<a id="astructbt__mesh__large__comp__data__rsp_html_a02d92a210b5b7a26b1df4f5076ed99d8"></a>
<a id="astructbt__mesh__large__comp__data__rsp_html_a8bba19b3687a67442e91873c228be361"></a>
<a id="astructbt__mesh__large__comp__data__rsp_html_aaab8add82c9f24d68af0ddd279164882"></a>
<a id="astructbt__mesh__large__comp__data__rsp_html_ad3d781276eaf84fd1a8a4d031c005deb"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ack__ctx_html"></a>
<a id="astructnet__buf__simple_html"></a>

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_LARGE_COMP_DATA_CLI_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_LARGE_COMP_DATA_CLI_H_

#include <zephyr/bluetooth/mesh.h>

#ifdef __cplusplus
extern "C" {
#endif


struct bt_mesh_large_comp_data_cli;

struct bt_mesh_large_comp_data_rsp {
        uint8_t page;
        uint16_t offset;
        uint16_t total_size;
        struct net_buf_simple *data;
};

struct bt_mesh_large_comp_data_cli_cb {
        void (*large_comp_data_status)(struct bt_mesh_large_comp_data_cli *cli, uint16_t addr,
                                       struct bt_mesh_large_comp_data_rsp *rsp);

        void (*models_metadata_status)(struct bt_mesh_large_comp_data_cli *cli, uint16_t addr,
                                       struct bt_mesh_large_comp_data_rsp *rsp);
};

struct bt_mesh_large_comp_data_cli {
        const struct bt_mesh_model *model;

        struct bt_mesh_msg_ack_ctx ack_ctx;

        const struct bt_mesh_large_comp_data_cli_cb *cb;
};

#define BT_MESH_MODEL_LARGE_COMP_DATA_CLI(cli_data)                                                \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_LARGE_COMP_DATA_CLI,                                     \
                         _bt_mesh_large_comp_data_cli_op, NULL, cli_data,                          \
                         &_bt_mesh_large_comp_data_cli_cb)

int bt_mesh_large_comp_data_get(uint16_t net_idx, uint16_t addr, uint8_t page,
                                size_t offset, struct bt_mesh_large_comp_data_rsp *rsp);

int bt_mesh_models_metadata_get(uint16_t net_idx, uint16_t addr, uint8_t page,
                                size_t offset, struct bt_mesh_large_comp_data_rsp *rsp);

extern const struct bt_mesh_model_op _bt_mesh_large_comp_data_cli_op[];
extern const struct bt_mesh_model_cb _bt_mesh_large_comp_data_cli_cb;


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_LARGE_COMP_DATA_CLI_H_ */
```

## 435.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 159 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_LARGE_COMP_DATA_CLI_H_`。

## 435.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__cli_8h.html)
- [zephyr/bluetooth/mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_large_comp_data_cli](../bluetooth_mesh_model_reference/P069_bt_mesh_large_comp_data_cli_结构体.md)
- [bt_mesh_large_comp_data_rsp](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [page](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md#ad3d781276eaf84fd1a8a4d031c005deb)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [offset](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md#a8bba19b3687a67442e91873c228be361)
- [total_size](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md#aaab8add82c9f24d68af0ddd279164882)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [data](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md#a02d92a210b5b7a26b1df4f5076ed99d8)
- [bt_mesh_large_comp_data_cli_cb](../bluetooth_mesh_model_reference/P070_bt_mesh_large_comp_data_cli_cb_结构体.md)
- [large_comp_data_status](../bluetooth_mesh_model_reference/P070_bt_mesh_large_comp_data_cli_cb_结构体.md#ab0e17df5eb165a44d70542b8edd36ab9)
- [models_metadata_status](../bluetooth_mesh_model_reference/P070_bt_mesh_large_comp_data_cli_cb_结构体.md#ade54d137534ffb2274e366140f6cbd3c)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [model](../bluetooth_mesh_model_reference/P069_bt_mesh_large_comp_data_cli_结构体.md#a4401ff19edfe69c018dd0dbb6f81dc0d)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [ack_ctx](../bluetooth_mesh_model_reference/P069_bt_mesh_large_comp_data_cli_结构体.md#afec070cb549d56b3900c4df1e14656ed)
- [cb](../bluetooth_mesh_model_reference/P069_bt_mesh_large_comp_data_cli_结构体.md#a39d9086c8d9803f939c6103e613699b1)
- [bt_mesh_large_comp_data_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html#gaf505ee14246746fc245a34328443d1c6)
- [bt_mesh_models_metadata_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html#ga4073eb48c43460804705d80ac0919864)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_large_comp_data_cli_cb::large_comp_data_status](../bluetooth_mesh_model_reference/P070_bt_mesh_large_comp_data_cli_cb_结构体.md#ab0e17df5eb165a44d70542b8edd36ab9)
- [bt_mesh_large_comp_data_cli_cb::models_metadata_status](../bluetooth_mesh_model_reference/P070_bt_mesh_large_comp_data_cli_cb_结构体.md#ade54d137534ffb2274e366140f6cbd3c)
- [bt_mesh_large_comp_data_cli::cb](../bluetooth_mesh_model_reference/P069_bt_mesh_large_comp_data_cli_结构体.md#a39d9086c8d9803f939c6103e613699b1)
- [bt_mesh_large_comp_data_cli::model](../bluetooth_mesh_model_reference/P069_bt_mesh_large_comp_data_cli_结构体.md#a4401ff19edfe69c018dd0dbb6f81dc0d)
- [bt_mesh_large_comp_data_cli::ack_ctx](../bluetooth_mesh_model_reference/P069_bt_mesh_large_comp_data_cli_结构体.md#afec070cb549d56b3900c4df1e14656ed)
- [bt_mesh_large_comp_data_rsp::data](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md#a02d92a210b5b7a26b1df4f5076ed99d8)
- [bt_mesh_large_comp_data_rsp::offset](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md#a8bba19b3687a67442e91873c228be361)
- [bt_mesh_large_comp_data_rsp::total_size](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md#aaab8add82c9f24d68af0ddd279164882)
- [bt_mesh_large_comp_data_rsp::page](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md#ad3d781276eaf84fd1a8a4d031c005deb)

---

[上一章](P434_label.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P436_large_comp_data_srv.h_源码浏览.md)
