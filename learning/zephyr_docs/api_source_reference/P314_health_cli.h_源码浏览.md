---
id: learning.zephyr-docs.api-source-reference.page-314
title: health_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/health__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第314章\_health\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/health__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/health__cli_8h.html)。

## 314.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="foldopen00127"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="agroup__bt__mesh__access_html_gaa52a40ef5972c4f34cf5ff5a10e21289"></a>
<a id="agroup__bt__mesh__health__cli_html_ga00cef275cdf90876f1381ffaff04b25c"></a>
<a id="agroup__bt__mesh__health__cli_html_ga1b910d0849ce4c33d6de4bf1ff47ece8"></a>
<a id="agroup__bt__mesh__health__cli_html_ga1e8e25681b9fcbc6584a29336924a78a"></a>
<a id="agroup__bt__mesh__health__cli_html_ga2951f45aaaee75f4c77c4381b1ddd617"></a>
<a id="agroup__bt__mesh__health__cli_html_ga2ef46f0b5059a959d5b06d6e49c4f552"></a>
<a id="agroup__bt__mesh__health__cli_html_ga3a528688e340edf49b4bd62317284834"></a>
<a id="agroup__bt__mesh__health__cli_html_ga536c631d87daaca017af078d49094fc1"></a>
<a id="agroup__bt__mesh__health__cli_html_ga77cc4e97193cca60d79a8076f3761ef5"></a>
<a id="agroup__bt__mesh__health__cli_html_ga8e58519ef78946e88258b335c350d754"></a>
<a id="agroup__bt__mesh__health__cli_html_ga9abc0db22da327d02d23371bba59b46a"></a>
<a id="agroup__bt__mesh__health__cli_html_gad6f322f506b8577c56bb0613f7dcbd93"></a>
<a id="agroup__bt__mesh__health__cli_html_gaf3d54597a74a458df0053bd0599d39e9"></a>
<a id="agroup__bt__mesh__health__cli_html_gafb0a46136f82f1aff4273704f1c47ac4"></a>
<a id="agroup__bt__mesh__msg_html_ga5352d6fa05808722eba8a76e2446eddb"></a>
<a id="amesh_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__health__cli_html"></a>
<a id="astructbt__mesh__health__cli_html_a103d110c6cccd69a9e48619668fc60bc"></a>
<a id="astructbt__mesh__health__cli_html_a395f525d846ef029bf5ff9fdde6e7c61"></a>
<a id="astructbt__mesh__health__cli_html_a4cbf24a2407df9bb80e19c1da1558294"></a>
<a id="astructbt__mesh__health__cli_html_a6246d36f8110f401f55003661ab15c86"></a>
<a id="astructbt__mesh__health__cli_html_a9ae3415b328b25c6206dacdad874c2aa"></a>
<a id="astructbt__mesh__health__cli_html_ac2ef6ae4fd8e14ad854a9f2c5c80fc43"></a>
<a id="astructbt__mesh__health__cli_html_ae1b396cb99a32a96762d4435629b1ba5"></a>
<a id="astructbt__mesh__health__cli_html_ae33ffa14689438b39166f4d90386f329"></a>
<a id="astructbt__mesh__health__cli_html_ae472c161f7da7c1cb646102ca78f262b"></a>
<a id="astructbt__mesh__health__cli_html_ae8d023ac56beb39c0d73a3b9e75f6c96"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model__pub_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ack__ctx_html"></a>
<a id="astructbt__mesh__msg__ctx_html"></a>
<a id="astructnet__buf__simple_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_CLI_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_CLI_H_

#include <zephyr/bluetooth/mesh.h>


#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_health_cli {
        const struct bt_mesh_model *model;

        struct bt_mesh_model_pub pub;

        struct net_buf_simple pub_buf;

        uint8_t pub_data[BT_MESH_MODEL_BUF_LEN(BT_MESH_MODEL_OP_2(0x80, 0x32), 3)];

        void (*period_status)(struct bt_mesh_health_cli *cli, uint16_t addr,
                              uint8_t divisor);

        void (*attention_status)(struct bt_mesh_health_cli *cli, uint16_t addr,
                                 uint8_t attention);

        void (*fault_status)(struct bt_mesh_health_cli *cli, uint16_t addr,
                             uint8_t test_id, uint16_t cid, uint8_t *faults,
                             size_t fault_count);

        void (*current_status)(struct bt_mesh_health_cli *cli, uint16_t addr,
                               uint8_t test_id, uint16_t cid, uint8_t *faults,
                               size_t fault_count);

        int (*update)(struct bt_mesh_health_cli *cli, struct net_buf_simple *pub_buf);

        /* Internal parameters for tracking message responses. */
        struct bt_mesh_msg_ack_ctx ack_ctx;
};

#define BT_MESH_MODEL_HEALTH_CLI(cli_data)                                     \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_HEALTH_CLI, bt_mesh_health_cli_op,   \
                         &(cli_data)->pub, cli_data, &bt_mesh_health_cli_cb)

int bt_mesh_health_cli_fault_get(struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx,
                                 uint16_t cid, uint8_t *test_id, uint8_t *faults,
                                 size_t *fault_count);

int bt_mesh_health_cli_fault_clear(struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx,
                                   uint16_t cid, uint8_t *test_id, uint8_t *faults,
                                   size_t *fault_count);

int bt_mesh_health_cli_fault_clear_unack(struct bt_mesh_health_cli *cli,
                                         struct bt_mesh_msg_ctx *ctx, uint16_t cid);

int bt_mesh_health_cli_fault_test(struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx,
                                  uint16_t cid, uint8_t test_id, uint8_t *faults,
                                  size_t *fault_count);

int bt_mesh_health_cli_fault_test_unack(struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx,
                                        uint16_t cid, uint8_t test_id);

int bt_mesh_health_cli_period_get(struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx,
                                  uint8_t *divisor);

int bt_mesh_health_cli_period_set(struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx,
                                  uint8_t divisor, uint8_t *updated_divisor);

int bt_mesh_health_cli_period_set_unack(struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx,
                                        uint8_t divisor);

int bt_mesh_health_cli_attention_get(struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx,
                                     uint8_t *attention);

int bt_mesh_health_cli_attention_set(struct bt_mesh_health_cli *cli, struct bt_mesh_msg_ctx *ctx,
                                     uint8_t attention, uint8_t *updated_attention);

int bt_mesh_health_cli_attention_set_unack(struct bt_mesh_health_cli *cli,
                                           struct bt_mesh_msg_ctx *ctx, uint8_t attention);

int32_t bt_mesh_health_cli_timeout_get(void);

void bt_mesh_health_cli_timeout_set(int32_t timeout);

extern const struct bt_mesh_model_op bt_mesh_health_cli_op[];
extern const struct bt_mesh_model_cb bt_mesh_health_cli_cb;

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_CLI_H_ */
```

## 314.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 118 行

用于跟踪消息响应的内部参数（Internal parameters）。

### 注释 3：原第 379 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_CLI_H_`。

## 314.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/health__cli_8h.html)
- [zephyr/bluetooth/mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_health_cli](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [model](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#ae472c161f7da7c1cb646102ca78f262b)
- [bt_mesh_model_pub](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md)
- [pub](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#ae33ffa14689438b39166f4d90386f329)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [pub_buf](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#a9ae3415b328b25c6206dacdad874c2aa)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [pub_data](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#a103d110c6cccd69a9e48619668fc60bc)
- [BT_MESH_MODEL_BUF_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga5352d6fa05808722eba8a76e2446eddb)
- [BT_MESH_MODEL_OP_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa52a40ef5972c4f34cf5ff5a10e21289)
- [period_status](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#a395f525d846ef029bf5ff9fdde6e7c61)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [attention_status](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#ae8d023ac56beb39c0d73a3b9e75f6c96)
- [fault_status](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#a4cbf24a2407df9bb80e19c1da1558294)
- [current_status](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#a6246d36f8110f401f55003661ab15c86)
- [update](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#ae1b396cb99a32a96762d4435629b1ba5)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [ack_ctx](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#ac2ef6ae4fd8e14ad854a9f2c5c80fc43)
- [bt_mesh_health_cli_fault_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga2951f45aaaee75f4c77c4381b1ddd617)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [bt_mesh_health_cli_fault_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga77cc4e97193cca60d79a8076f3761ef5)
- [bt_mesh_health_cli_fault_clear_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#gafb0a46136f82f1aff4273704f1c47ac4)
- [bt_mesh_health_cli_fault_test](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga00cef275cdf90876f1381ffaff04b25c)
- [bt_mesh_health_cli_fault_test_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga8e58519ef78946e88258b335c350d754)
- [bt_mesh_health_cli_period_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga1e8e25681b9fcbc6584a29336924a78a)
- [bt_mesh_health_cli_period_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga2ef46f0b5059a959d5b06d6e49c4f552)
- [bt_mesh_health_cli_period_set_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga536c631d87daaca017af078d49094fc1)
- [bt_mesh_health_cli_attention_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#gad6f322f506b8577c56bb0613f7dcbd93)
- [bt_mesh_health_cli_attention_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga1b910d0849ce4c33d6de4bf1ff47ece8)
- [bt_mesh_health_cli_attention_set_unack](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga3a528688e340edf49b4bd62317284834)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_health_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#ga9abc0db22da327d02d23371bba59b46a)
- [bt_mesh_health_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__cli.html#gaf3d54597a74a458df0053bd0599d39e9)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_health_cli::pub_data](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#a103d110c6cccd69a9e48619668fc60bc)
- [bt_mesh_health_cli::period_status](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#a395f525d846ef029bf5ff9fdde6e7c61)
- [bt_mesh_health_cli::fault_status](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#a4cbf24a2407df9bb80e19c1da1558294)
- [bt_mesh_health_cli::current_status](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#a6246d36f8110f401f55003661ab15c86)
- [bt_mesh_health_cli::pub_buf](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#a9ae3415b328b25c6206dacdad874c2aa)
- [bt_mesh_health_cli::ack_ctx](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#ac2ef6ae4fd8e14ad854a9f2c5c80fc43)
- [bt_mesh_health_cli::update](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#ae1b396cb99a32a96762d4435629b1ba5)
- [bt_mesh_health_cli::pub](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#ae33ffa14689438b39166f4d90386f329)
- [bt_mesh_health_cli::model](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#ae472c161f7da7c1cb646102ca78f262b)
- [bt_mesh_health_cli::attention_status](../bluetooth_mesh_model_reference/P065_bt_mesh_health_cli_结构体.md#ae8d023ac56beb39c0d73a3b9e75f6c96)

---

[上一章](P313_hdr_ddr.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P315_health_faults.h_源码浏览.md)
