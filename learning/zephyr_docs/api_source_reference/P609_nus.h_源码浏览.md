---
id: learning.zephyr-docs.api-source-reference.page-609
title: nus.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nus_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第609章\_nus.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html)。

## 609.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
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
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="foldopen00023"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="foldopen00025"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00107"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="abluetooth_2uuid_8h_html"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainst_8h_html"></a>
<a id="anus_8h_html_a1a28f3d267b34856450f60803eed485f"></a>
<a id="anus_8h_html_a84cb19f07f861963c73614a04c0a375f"></a>
<a id="anus_8h_html_a950188897461f1c1f78ffbabeae1180a"></a>
<a id="anus_8h_html_a997453fc8108f64a95186b130ea68076"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__nus__cb_html"></a>
<a id="astructbt__nus__cb_html_a3fc8fcca9d16f18c506ad13d2356e32c"></a>
<a id="astructbt__nus__cb_html_ab28ef9120ed04be0c7dbdd5c76556864"></a>
<a id="astructbt__nus__cb_html_ad95d3bb5f927c25058c4ec6a89c665a4"></a>
<a id="astructbt__nus__inst_html"></a>

```c
/*
 * Copyright (c) 2024 Croxel, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_NUS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_NUS_H_

#include <zephyr/bluetooth/uuid.h>
#include <zephyr/bluetooth/services/nus/inst.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_UUID_NUS_SRV_VAL \
        BT_UUID_128_ENCODE(0x6e400001, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)
#define BT_UUID_NUS_RX_CHAR_VAL \
        BT_UUID_128_ENCODE(0x6e400002, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)
#define BT_UUID_NUS_TX_CHAR_VAL \
        BT_UUID_128_ENCODE(0x6e400003, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)

#define BT_NUS_INST_DEFINE(_name) \
        Z_INTERNAL_BT_NUS_INST_DEFINE(_name)

struct bt_nus_cb {
        void (*notif_enabled)(bool enabled, void *ctx);

        void (*received)(struct bt_conn *conn, const void *data, uint16_t len, void *ctx);

        void *ctx;

        sys_snode_t _node;
};

int bt_nus_inst_cb_register(struct bt_nus_inst *inst, struct bt_nus_cb *cb, void *ctx);

int bt_nus_inst_send(struct bt_conn *conn,
                     struct bt_nus_inst *inst,
                     const void *data,
                     uint16_t len);

static inline int bt_nus_cb_register(struct bt_nus_cb *cb, void *ctx)
{
        return bt_nus_inst_cb_register(NULL, cb, ctx);
}

static inline int bt_nus_send(struct bt_conn *conn, const void *data, uint16_t len)
{
        return bt_nus_inst_send(conn, NULL, data, len);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_NUS_H_ */
```

## 609.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Croxel, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 135 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_NUS_H_`。

## 609.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html)
- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [zephyr/bluetooth/services/nus/inst.h](https://docs.zephyrproject.org/latest/doxygen/html/inst_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_nus_cb](../bluetooth_service_model_reference/P125_bt_nus_cb_结构体.md)
- [notif_enabled](../bluetooth_service_model_reference/P125_bt_nus_cb_结构体.md#a3fc8fcca9d16f18c506ad13d2356e32c)
- [ctx](../bluetooth_service_model_reference/P125_bt_nus_cb_结构体.md#ab28ef9120ed04be0c7dbdd5c76556864)
- [received](../bluetooth_service_model_reference/P125_bt_nus_cb_结构体.md#ad95d3bb5f927c25058c4ec6a89c665a4)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_nus_inst_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html#a84cb19f07f861963c73614a04c0a375f)
- [bt_nus_inst](../bluetooth_service_model_reference/P126_bt_nus_inst_结构体.md)
- [bt_nus_inst_send](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html#a997453fc8108f64a95186b130ea68076)
- [bt_nus_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html#a1a28f3d267b34856450f60803eed485f)
- [bt_nus_send](https://docs.zephyrproject.org/latest/doxygen/html/nus_8h.html#a950188897461f1c1f78ffbabeae1180a)
- [uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h.html)
- [inst.h](https://docs.zephyrproject.org/latest/doxygen/html/inst_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_nus_cb::notif_enabled](../bluetooth_service_model_reference/P125_bt_nus_cb_结构体.md#a3fc8fcca9d16f18c506ad13d2356e32c)
- [bt_nus_cb::ctx](../bluetooth_service_model_reference/P125_bt_nus_cb_结构体.md#ab28ef9120ed04be0c7dbdd5c76556864)
- [bt_nus_cb::received](../bluetooth_service_model_reference/P125_bt_nus_cb_结构体.md#ad95d3bb5f927c25058c4ec6a89c665a4)

---

[上一章](P608_numicro-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P610_nuvoton-npcx-gpio.h_源码浏览.md)
