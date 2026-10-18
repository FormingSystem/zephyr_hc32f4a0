---
id: learning.zephyr-docs.api-source-reference.page-633
title: op_agg_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/op__agg__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第633章\_op\_agg\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/op__agg__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/op__agg__cli_8h.html)。

## 633.1\_原始可见代码（Source Code）

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
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="agroup__bt__mesh__op__agg__cli_html_ga00b5e695503ba169a1b5ec626413b322"></a>
<a id="agroup__bt__mesh__op__agg__cli_html_ga4269bc6118371e2af0967841b18a02dd"></a>
<a id="agroup__bt__mesh__op__agg__cli_html_ga83e44b062babcf0bdb343455e3eddf5f"></a>
<a id="agroup__bt__mesh__op__agg__cli_html_gab151f44fcb5d3f3f0f1dafaf90f05c18"></a>
<a id="agroup__bt__mesh__op__agg__cli_html_gac1905d778362faf442a9538adca34a8c"></a>
<a id="agroup__bt__mesh__op__agg__cli_html_gadbc347b2dc3d78a4ac71d424f0623b6f"></a>
<a id="agroup__bt__mesh__op__agg__cli_html_gaf70cebae8dbd6eb4ef6402585a90e0d5"></a>
<a id="amesh_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>

```c
/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_OP_AGG_CLI_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_OP_AGG_CLI_H_

#include <zephyr/bluetooth/mesh.h>

#ifdef __cplusplus
extern "C" {
#endif


#define BT_MESH_MODEL_OP_AGG_CLI                                               \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_OP_AGG_CLI, _bt_mesh_op_agg_cli_op,  \
                         NULL, NULL, &_bt_mesh_op_agg_cli_cb)

int bt_mesh_op_agg_cli_seq_start(uint16_t net_idx, uint16_t app_idx, uint16_t dst,
                                 uint16_t elem_addr);

int bt_mesh_op_agg_cli_seq_send(void);

void bt_mesh_op_agg_cli_seq_abort(void);

bool bt_mesh_op_agg_cli_seq_is_started(void);

size_t bt_mesh_op_agg_cli_seq_tailroom(void);

int32_t bt_mesh_op_agg_cli_timeout_get(void);

void bt_mesh_op_agg_cli_timeout_set(int32_t timeout);

extern const struct bt_mesh_model_op _bt_mesh_op_agg_cli_op[];
extern const struct bt_mesh_model_cb _bt_mesh_op_agg_cli_cb;


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_OP_AGG_CLI_H_ */
```

## 633.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 98 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_OP_AGG_CLI_H_`。

## 633.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/op__agg__cli_8h.html)
- [zephyr/bluetooth/mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_op_agg_cli_seq_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gac1905d778362faf442a9538adca34a8c)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_op_agg_cli_seq_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gab151f44fcb5d3f3f0f1dafaf90f05c18)
- [bt_mesh_op_agg_cli_seq_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#ga00b5e695503ba169a1b5ec626413b322)
- [bt_mesh_op_agg_cli_seq_is_started](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gadbc347b2dc3d78a4ac71d424f0623b6f)
- [bt_mesh_op_agg_cli_seq_tailroom](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#ga4269bc6118371e2af0967841b18a02dd)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_op_agg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#ga83e44b062babcf0bdb343455e3eddf5f)
- [bt_mesh_op_agg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__cli.html#gaf70cebae8dbd6eb4ef6402585a90e0d5)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)

---

[上一章](P632_od_priv_proxy_srv.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P634_op_agg_srv.h_源码浏览.md)
