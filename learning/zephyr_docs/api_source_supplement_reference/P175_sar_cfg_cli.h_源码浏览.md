---
id: learning.zephyr-docs.api-source-supplement-reference.page-175
title: sar_cfg_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第175章\_sar\_cfg\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg__cli_8h.html)。

## 175.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="agroup__bt__mesh__sar__cfg__cli_html_ga32e2a580b24a41761911e88413e9664e"></a>
<a id="agroup__bt__mesh__sar__cfg__cli_html_ga444c99254ef2ccdd10dac08a94219d79"></a>
<a id="agroup__bt__mesh__sar__cfg__cli_html_ga57d7c6a973b35f53689cbf8a065a538f"></a>
<a id="agroup__bt__mesh__sar__cfg__cli_html_ga884025b2baf8559950ba6dc83e9ef486"></a>
<a id="agroup__bt__mesh__sar__cfg__cli_html_ga893ef5861708bec12f87b9f9cc64b9fc"></a>
<a id="agroup__bt__mesh__sar__cfg__cli_html_ga998846e5735676dc5f79b387d02630d4"></a>
<a id="amesh_8h_html"></a>
<a id="asar__cfg_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model__pub_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ack__ctx_html"></a>
<a id="astructbt__mesh__sar__cfg__cli_html"></a>
<a id="astructbt__mesh__sar__cfg__cli_html_a16a6f6c0b0ac8ae80abfb48a5f231418"></a>
<a id="astructbt__mesh__sar__cfg__cli_html_a30889368bd4e87efd39b6c456b3510d8"></a>
<a id="astructbt__mesh__sar__cfg__cli_html_a31fdb2608f2cf80ea17dd1f72e634769"></a>
<a id="astructbt__mesh__sar__cfg__cli_html_a94056c2b7bfc1b495b5bf7e6a5fe3066"></a>
<a id="astructbt__mesh__sar__rx_html"></a>
<a id="astructbt__mesh__sar__tx_html"></a>

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_SAR_CFG_CLI_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_SAR_CFG_CLI_H_

#include <zephyr/bluetooth/mesh.h>
#include <zephyr/bluetooth/mesh/sar_cfg.h>


#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_sar_cfg_cli {
        const struct bt_mesh_model *model;

        /* Publication structure instance */
        struct bt_mesh_model_pub pub;

        /* Synchronous message timeout in milliseconds. */
        int32_t timeout;

        /* Internal parameters for tracking message responses. */
        struct bt_mesh_msg_ack_ctx ack_ctx;
};

#define BT_MESH_MODEL_SAR_CFG_CLI(_cli)                                  \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_SAR_CFG_CLI,                         \
                         _bt_mesh_sar_cfg_cli_op, _cli.pub, _cli,                  \
                         &_bt_mesh_sar_cfg_cli_cb)

int bt_mesh_sar_cfg_cli_transmitter_get(uint16_t net_idx, uint16_t addr,
                                        struct bt_mesh_sar_tx *rsp);

int bt_mesh_sar_cfg_cli_transmitter_set(uint16_t net_idx, uint16_t addr,
                                        const struct bt_mesh_sar_tx *set,
                                        struct bt_mesh_sar_tx *rsp);

int bt_mesh_sar_cfg_cli_receiver_get(uint16_t net_idx, uint16_t addr,
                                     struct bt_mesh_sar_rx *rsp);

int bt_mesh_sar_cfg_cli_receiver_set(uint16_t net_idx, uint16_t addr,
                                     const struct bt_mesh_sar_rx *set,
                                     struct bt_mesh_sar_rx *rsp);

int32_t bt_mesh_sar_cfg_cli_timeout_get(void);

void bt_mesh_sar_cfg_cli_timeout_set(int32_t timeout);

extern const struct bt_mesh_model_op _bt_mesh_sar_cfg_cli_op[];
extern const struct bt_mesh_model_cb _bt_mesh_sar_cfg_cli_cb;

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_SAR_CFG_CLI_H_ */

```

## 175.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 32 行

发布结构实例（Publication structure instance）。

### 注释 3：原第 35 行

同步消息超时，单位为毫秒。

### 注释 4：原第 38 行

用于跟踪消息响应的内部参数（Internal parameters）。

### 注释 5：原第 122 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_SAR_CFG_CLI_H_`。

## 175.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg__cli_8h.html)
- [zephyr/bluetooth/mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [zephyr/bluetooth/mesh/sar_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg_8h.html)
- [bt_mesh_sar_cfg_cli](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [model](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md#a94056c2b7bfc1b495b5bf7e6a5fe3066)
- [bt_mesh_model_pub](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md)
- [pub](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md#a16a6f6c0b0ac8ae80abfb48a5f231418)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [timeout](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md#a31fdb2608f2cf80ea17dd1f72e634769)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [ack_ctx](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md#a30889368bd4e87efd39b6c456b3510d8)
- [bt_mesh_sar_cfg_cli_transmitter_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga893ef5861708bec12f87b9f9cc64b9fc)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_sar_tx](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md)
- [bt_mesh_sar_cfg_cli_transmitter_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga32e2a580b24a41761911e88413e9664e)
- [bt_mesh_sar_cfg_cli_receiver_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga444c99254ef2ccdd10dac08a94219d79)
- [bt_mesh_sar_rx](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md)
- [bt_mesh_sar_cfg_cli_receiver_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga884025b2baf8559950ba6dc83e9ef486)
- [bt_mesh_sar_cfg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga998846e5735676dc5f79b387d02630d4)
- [bt_mesh_sar_cfg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga57d7c6a973b35f53689cbf8a065a538f)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [sar_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg_8h.html)
- [bt_mesh_sar_cfg_cli::pub](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md#a16a6f6c0b0ac8ae80abfb48a5f231418)
- [bt_mesh_sar_cfg_cli::ack_ctx](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md#a30889368bd4e87efd39b6c456b3510d8)
- [bt_mesh_sar_cfg_cli::timeout](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md#a31fdb2608f2cf80ea17dd1f72e634769)
- [bt_mesh_sar_cfg_cli::model](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md#a94056c2b7bfc1b495b5bf7e6a5fe3066)

---

[上一章](P174_sar_cfg.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P176_seagate_legend_b1414.h_源码浏览.md)
