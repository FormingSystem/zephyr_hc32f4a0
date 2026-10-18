---
id: learning.zephyr-docs.api-source-reference.page-914
title: vocs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/vocs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第914章\_vocs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/vocs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/vocs_8h.html)。

## 914.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
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
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00103"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="foldopen00224"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00238"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__vocs_html_ga02b036f060eee947c8924bbea846bc29"></a>
<a id="agroup__bt__vocs_html_ga2630344190f12f911bb2b01c4b95ded6"></a>
<a id="agroup__bt__vocs_html_ga28ea337e439b5872abab8f5b98719da4"></a>
<a id="agroup__bt__vocs_html_ga45efa872e07ac8051379caf5aa8d0133"></a>
<a id="agroup__bt__vocs_html_ga6182120b1bece7f5851bb6295c81b562"></a>
<a id="agroup__bt__vocs_html_ga6c835234a5530bae3bb0f5bd03a0bdd7"></a>
<a id="agroup__bt__vocs_html_ga84983707e04eae75f18017072b647115"></a>
<a id="agroup__bt__vocs_html_ga90ba394e6be138d6052b95d73ab2f409"></a>
<a id="agroup__bt__vocs_html_ga9f7ff4c0521686ded011758ddd8ea95e"></a>
<a id="agroup__bt__vocs_html_gaa329fd8931add8fd4f6c59b48c91ef75"></a>
<a id="agroup__bt__vocs_html_gaa351c3ab631b16272e27cbb837d9e49c"></a>
<a id="agroup__bt__vocs_html_gaac1c1292cae4c5845a376d2f4db3d661"></a>
<a id="agroup__bt__vocs_html_gaace802556eca3d634a13dd8f2bf3c544"></a>
<a id="agroup__bt__vocs_html_gac011ddd93bb3240148a789f1ee9ef7da"></a>
<a id="agroup__bt__vocs_html_gac17cb7101233605834ec6b66d7417f91"></a>
<a id="agroup__bt__vocs_html_gad50fd539190b5c64b5262d3830699365"></a>
<a id="agroup__bt__vocs_html_gadde50c3eb90ea7b7aa9b9c4b3672710f"></a>
<a id="agroup__bt__vocs_html_gaf210fd531117b9a22a52746266c72c08"></a>
<a id="agroup__bt__vocs_html_gafcf7ecea73c8c199b38c7291ce4a648f"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__vocs__cb_html"></a>
<a id="astructbt__vocs__cb_html_a1b5a3359602ceea1a45ebe7aa79e6b3a"></a>
<a id="astructbt__vocs__cb_html_a2ff42997b87d2a910325d4b04e67f4c5"></a>
<a id="astructbt__vocs__cb_html_a50d1d429089456267b06d4450712b897"></a>
<a id="astructbt__vocs__cb_html_ac508b1e6dda00c607aa1cbe52423ec52"></a>
<a id="astructbt__vocs__cb_html_ae633c1f6cd8aa03d89287e783179460e"></a>
<a id="astructbt__vocs__discover__param_html"></a>
<a id="astructbt__vocs__discover__param_html_a3811da3035bb1f0ff5d290eb60fb2fda"></a>
<a id="astructbt__vocs__discover__param_html_aca830a50436def0f422d05eba34273ed"></a>
<a id="astructbt__vocs__register__param_html"></a>
<a id="astructbt__vocs__register__param_html_a0572c60319c8984e2437e596584c46f5"></a>
<a id="astructbt__vocs__register__param_html_a1f6baed09dc35b974d06f1426b671e05"></a>
<a id="astructbt__vocs__register__param_html_a306ad3c712bb5a5109f3afb4912d590b"></a>
<a id="astructbt__vocs__register__param_html_a6919f965abfa1fec39a3c8e0f29c04f3"></a>
<a id="astructbt__vocs__register__param_html_aace5987e890c8b4dbf3e01fa5c2a4432"></a>
<a id="astructbt__vocs__register__param_html_ac1c2475cd390f5acf840f92ea45c6d31"></a>
<a id="astructbt__vocs_html"></a>

```c


/*
 * Copyright (c) 2020-2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_VOCS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_VOCS_H_


#include <stdint.h>
#include <stdbool.h>

#include <zephyr/bluetooth/conn.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_VOCS_ERR_INVALID_COUNTER                0x80U
#define BT_VOCS_ERR_OP_NOT_SUPPORTED               0x81U
#define BT_VOCS_ERR_OUT_OF_RANGE                   0x82U

#define BT_VOCS_MIN_OFFSET                         -255
#define BT_VOCS_MAX_OFFSET                         255

struct bt_vocs;

struct bt_vocs_register_param {
        uint32_t location;

        bool location_writable;

        int16_t offset;

        char *output_desc;

        bool desc_writable;

        struct bt_vocs_cb *cb;
};

struct bt_vocs_discover_param {
        uint16_t start_handle;
        uint16_t end_handle;
};

struct bt_vocs *bt_vocs_free_instance_get(void);

void *bt_vocs_svc_decl_get(struct bt_vocs *vocs);

int bt_vocs_client_conn_get(const struct bt_vocs *vocs, struct bt_conn **conn);

int bt_vocs_register(struct bt_vocs *vocs,
                     const struct bt_vocs_register_param *param);

typedef void (*bt_vocs_state_cb)(struct bt_vocs *inst, int err, int16_t offset);

typedef void (*bt_vocs_set_offset_cb)(struct bt_vocs *inst, int err);

typedef void (*bt_vocs_location_cb)(struct bt_vocs *inst, int err,
                                    uint32_t location);

typedef void (*bt_vocs_description_cb)(struct bt_vocs *inst, int err,
                                       char *description);

typedef void (*bt_vocs_discover_cb)(struct bt_vocs *inst, int err);

struct bt_vocs_cb {
        bt_vocs_state_cb                state;
        bt_vocs_location_cb             location;
        bt_vocs_description_cb          description;

#if defined(CONFIG_BT_VOCS_CLIENT) || defined(__DOXYGEN__)
        bt_vocs_discover_cb             discover;
        bt_vocs_set_offset_cb           set_offset;
#endif /* CONFIG_BT_VOCS_CLIENT */
};

int bt_vocs_state_get(struct bt_vocs *inst);

int bt_vocs_state_set(struct bt_vocs *inst, int16_t offset);

int bt_vocs_location_get(struct bt_vocs *inst);

int bt_vocs_location_set(struct bt_vocs *inst, uint32_t location);

int bt_vocs_description_get(struct bt_vocs *inst);

int bt_vocs_description_set(struct bt_vocs *inst, const char *description);

void bt_vocs_client_cb_register(struct bt_vocs *inst, struct bt_vocs_cb *cb);

struct bt_vocs *bt_vocs_client_free_instance_get(void);

int bt_vocs_client_free_instance(struct bt_vocs *inst);

int bt_vocs_discover(struct bt_conn *conn, struct bt_vocs *inst,
                     const struct bt_vocs_discover_param *param);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_VOCS_H_ */
```

## 914.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2020-2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 245 行

条件编译配置（Configuration）标记：`CONFIG_BT_VOCS_CLIENT`。

### 注释 3：原第 360 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_VOCS_H_`。

## 914.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/vocs_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [bt_vocs](../bluetooth_service_model_reference/P184_bt_vocs_结构体.md)
- [bt_vocs_register_param](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [location](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#a0572c60319c8984e2437e596584c46f5)
- [location_writable](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#a6919f965abfa1fec39a3c8e0f29c04f3)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [offset](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#ac1c2475cd390f5acf840f92ea45c6d31)
- [output_desc](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#a1f6baed09dc35b974d06f1426b671e05)
- [desc_writable](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#aace5987e890c8b4dbf3e01fa5c2a4432)
- [bt_vocs_cb](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md)
- [cb](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#a306ad3c712bb5a5109f3afb4912d590b)
- [bt_vocs_discover_param](../bluetooth_service_model_reference/P186_bt_vocs_discover_param_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [start_handle](../bluetooth_service_model_reference/P186_bt_vocs_discover_param_结构体.md#aca830a50436def0f422d05eba34273ed)
- [end_handle](../bluetooth_service_model_reference/P186_bt_vocs_discover_param_结构体.md#a3811da3035bb1f0ff5d290eb60fb2fda)
- [bt_vocs_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gadde50c3eb90ea7b7aa9b9c4b3672710f)
- [bt_vocs_svc_decl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga9f7ff4c0521686ded011758ddd8ea95e)
- [bt_vocs_client_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gafcf7ecea73c8c199b38c7291ce4a648f)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_vocs_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gac011ddd93bb3240148a789f1ee9ef7da)
- [bt_vocs_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaa329fd8931add8fd4f6c59b48c91ef75)
- [bt_vocs_set_offset_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga2630344190f12f911bb2b01c4b95ded6)
- [bt_vocs_location_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga84983707e04eae75f18017072b647115)
- [bt_vocs_description_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaa351c3ab631b16272e27cbb837d9e49c)
- [bt_vocs_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gad50fd539190b5c64b5262d3830699365)
- [state](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#ae633c1f6cd8aa03d89287e783179460e)
- [location](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#a50d1d429089456267b06d4450712b897)
- [description](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#ac508b1e6dda00c607aa1cbe52423ec52)
- [discover](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#a2ff42997b87d2a910325d4b04e67f4c5)
- [set_offset](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#a1b5a3359602ceea1a45ebe7aa79e6b3a)
- [bt_vocs_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga6c835234a5530bae3bb0f5bd03a0bdd7)
- [bt_vocs_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga28ea337e439b5872abab8f5b98719da4)
- [bt_vocs_location_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga90ba394e6be138d6052b95d73ab2f409)
- [bt_vocs_location_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga02b036f060eee947c8924bbea846bc29)
- [bt_vocs_description_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaac1c1292cae4c5845a376d2f4db3d661)
- [bt_vocs_description_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gac17cb7101233605834ec6b66d7417f91)
- [bt_vocs_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaace802556eca3d634a13dd8f2bf3c544)
- [bt_vocs_client_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga6182120b1bece7f5851bb6295c81b562)
- [bt_vocs_client_free_instance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaf210fd531117b9a22a52746266c72c08)
- [bt_vocs_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga45efa872e07ac8051379caf5aa8d0133)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [bt_vocs_cb::set_offset](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#a1b5a3359602ceea1a45ebe7aa79e6b3a)
- [bt_vocs_cb::discover](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#a2ff42997b87d2a910325d4b04e67f4c5)
- [bt_vocs_cb::location](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#a50d1d429089456267b06d4450712b897)
- [bt_vocs_cb::description](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#ac508b1e6dda00c607aa1cbe52423ec52)
- [bt_vocs_cb::state](../bluetooth_service_model_reference/P185_bt_vocs_cb_结构体.md#ae633c1f6cd8aa03d89287e783179460e)
- [bt_vocs_discover_param::end_handle](../bluetooth_service_model_reference/P186_bt_vocs_discover_param_结构体.md#a3811da3035bb1f0ff5d290eb60fb2fda)
- [bt_vocs_discover_param::start_handle](../bluetooth_service_model_reference/P186_bt_vocs_discover_param_结构体.md#aca830a50436def0f422d05eba34273ed)
- [bt_vocs_register_param::location](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#a0572c60319c8984e2437e596584c46f5)
- [bt_vocs_register_param::output_desc](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#a1f6baed09dc35b974d06f1426b671e05)
- [bt_vocs_register_param::cb](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#a306ad3c712bb5a5109f3afb4912d590b)
- [bt_vocs_register_param::location_writable](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#a6919f965abfa1fec39a3c8e0f29c04f3)
- [bt_vocs_register_param::desc_writable](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#aace5987e890c8b4dbf3e01fa5c2a4432)
- [bt_vocs_register_param::offset](../bluetooth_service_model_reference/P187_bt_vocs_register_param_结构体.md#ac1c2475cd390f5acf840f92ea45c6d31)

---

[上一章](P913_vl53l0x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P915_w1_sensor.h_源码浏览.md)
