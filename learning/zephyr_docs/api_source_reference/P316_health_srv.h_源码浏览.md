---
id: learning.zephyr-docs.api-source-reference.page-316
title: health_srv.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/health__srv_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第316章\_health\_srv.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/health__srv_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/health__srv_8h.html)。

## 316.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="foldopen00146"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="foldopen00175"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="foldopen00188"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="foldopen00204"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="abluetooth_2byteorder_8h_html"></a>
<a id="agroup__bt__mesh__health__srv_html_gad04789eb167b61d5ff19827c560ceb6e"></a>
<a id="amesh_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__elem_html"></a>
<a id="astructbt__mesh__health__srv__cb_html"></a>
<a id="astructbt__mesh__health__srv__cb_html_a03ff8869793804dd5943f5d2cd63cc3e"></a>
<a id="astructbt__mesh__health__srv__cb_html_a555711f2892d8e5a96661c6fff03c7f8"></a>
<a id="astructbt__mesh__health__srv__cb_html_ab426938525f8478ab27dc08a2f25273f"></a>
<a id="astructbt__mesh__health__srv__cb_html_abd881db6cf849433808bc6464e109b60"></a>
<a id="astructbt__mesh__health__srv__cb_html_ad9e8a392943d4848190c4513327bc52c"></a>
<a id="astructbt__mesh__health__srv__cb_html_afdc878362b78ccfeb4473bcdfb02b9d1"></a>
<a id="astructbt__mesh__health__srv_html"></a>
<a id="astructbt__mesh__health__srv_html_a4d316010b2737eca7bad3aef6774d52b"></a>
<a id="astructbt__mesh__health__srv_html_a8df7f6c7e434cb717b9b51a3167b5e86"></a>
<a id="astructbt__mesh__health__srv_html_aff95fc381ea8048d4d76668b92126dc6"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructk__work__delayable_html"></a>

```c


/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_SRV_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_SRV_H_


#include <zephyr/bluetooth/mesh.h>
#include <zephyr/bluetooth/byteorder.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_health_srv_cb {
        int (*fault_get_cur)(const struct bt_mesh_model *model, uint8_t *test_id,
                             uint16_t *company_id, uint8_t *faults,
                             uint8_t *fault_count);

        int (*fault_get_reg)(const struct bt_mesh_model *model, uint16_t company_id,
                             uint8_t *test_id, uint8_t *faults,
                             uint8_t *fault_count);

        int (*fault_clear)(const struct bt_mesh_model *model, uint16_t company_id);

        int (*fault_test)(const struct bt_mesh_model *model, uint8_t test_id,
                          uint16_t company_id);

        void (*attn_on)(const struct bt_mesh_model *model);

        void (*attn_off)(const struct bt_mesh_model *model);
};

#define BT_MESH_HEALTH_PUB_DEFINE(_name, _max_faults) \
        BT_MESH_MODEL_PUB_DEFINE(_name, NULL, (1 + 3 + (_max_faults)))

struct bt_mesh_health_srv {
        const struct bt_mesh_model *model;

        const struct bt_mesh_health_srv_cb *cb;

        struct k_work_delayable attn_timer;
};

#define BT_MESH_MODEL_HEALTH_SRV(srv, pub, ...)                        \
        BT_MESH_MODEL_METADATA_CB(BT_MESH_MODEL_ID_HEALTH_SRV,         \
                                  bt_mesh_health_srv_op,               \
                                  pub,                                 \
                                  srv,                                 \
                                  &bt_mesh_health_srv_cb, __VA_ARGS__)

#define BT_MESH_HEALTH_TEST_INFO_METADATA_ID 0x0000

#define BT_MESH_HEALTH_TEST_INFO_METADATA(tests)                               \
        {                                                                      \
                .len = ARRAY_SIZE(tests),                                      \
                .id = BT_MESH_HEALTH_TEST_INFO_METADATA_ID,                    \
                .data = tests,                                                 \
        }

#define BT_MESH_HEALTH_TEST_INFO(cid, tests...)                                \
        BT_BYTES_LIST_LE16(cid), sizeof((uint8_t[]){ tests }), tests

int bt_mesh_health_srv_fault_update(const struct bt_mesh_elem *elem);

extern const struct bt_mesh_model_op bt_mesh_health_srv_op[];
extern const struct bt_mesh_model_cb bt_mesh_health_srv_cb;

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_SRV_H_ */
```

## 316.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 232 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_SRV_H_`。

## 316.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/health__srv_8h.html)
- [zephyr/bluetooth/mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [zephyr/bluetooth/byteorder.h](../byteorder_reference/P004_蓝牙字节序头文件参考.md)
- [bt_mesh_health_srv_cb](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md)
- [fault_get_cur](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#a03ff8869793804dd5943f5d2cd63cc3e)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [fault_get_reg](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#a555711f2892d8e5a96661c6fff03c7f8)
- [fault_clear](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#afdc878362b78ccfeb4473bcdfb02b9d1)
- [fault_test](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#ab426938525f8478ab27dc08a2f25273f)
- [attn_on](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#ad9e8a392943d4848190c4513327bc52c)
- [attn_off](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#abd881db6cf849433808bc6464e109b60)
- [bt_mesh_health_srv](../bluetooth_mesh_model_reference/P066_bt_mesh_health_srv_结构体.md)
- [model](../bluetooth_mesh_model_reference/P066_bt_mesh_health_srv_结构体.md#aff95fc381ea8048d4d76668b92126dc6)
- [cb](../bluetooth_mesh_model_reference/P066_bt_mesh_health_srv_结构体.md#a4d316010b2737eca7bad3aef6774d52b)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [attn_timer](../bluetooth_mesh_model_reference/P066_bt_mesh_health_srv_结构体.md#a8df7f6c7e434cb717b9b51a3167b5e86)
- [bt_mesh_health_srv_fault_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#gad04789eb167b61d5ff19827c560ceb6e)
- [bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [byteorder.h](../byteorder_reference/P004_蓝牙字节序头文件参考.md)
- [mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_health_srv_cb::fault_get_cur](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#a03ff8869793804dd5943f5d2cd63cc3e)
- [bt_mesh_health_srv_cb::fault_get_reg](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#a555711f2892d8e5a96661c6fff03c7f8)
- [bt_mesh_health_srv_cb::fault_test](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#ab426938525f8478ab27dc08a2f25273f)
- [bt_mesh_health_srv_cb::attn_off](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#abd881db6cf849433808bc6464e109b60)
- [bt_mesh_health_srv_cb::attn_on](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#ad9e8a392943d4848190c4513327bc52c)
- [bt_mesh_health_srv_cb::fault_clear](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md#afdc878362b78ccfeb4473bcdfb02b9d1)
- [bt_mesh_health_srv::cb](../bluetooth_mesh_model_reference/P066_bt_mesh_health_srv_结构体.md#a4d316010b2737eca7bad3aef6774d52b)
- [bt_mesh_health_srv::attn_timer](../bluetooth_mesh_model_reference/P066_bt_mesh_health_srv_结构体.md#a8df7f6c7e434cb717b9b51a3167b5e86)
- [bt_mesh_health_srv::model](../bluetooth_mesh_model_reference/P066_bt_mesh_health_srv_结构体.md#aff95fc381ea8048d4d76668b92126dc6)

---

[上一章](P315_health_faults.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P317_heartbeat.h_源码浏览.md)
