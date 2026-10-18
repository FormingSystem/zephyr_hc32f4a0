---
id: learning.zephyr-docs.api-source-configuration-reference.page-16
title: dfu_srv.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfu__srv_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_dfu\_srv.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dfu__srv_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dfu__srv_8h.html)。

## 16.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="foldopen00036"></a>
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
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="foldopen00176"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="aaccess_8h_html"></a>
<a id="ablob__srv_8h_html"></a>
<a id="adfu_8h_html"></a>
<a id="agroup__bt__mesh__dfu__srv_html_ga45aef92fe1de4c45ccb5369c1f5222ee"></a>
<a id="agroup__bt__mesh__dfu__srv_html_ga64eeb5bfe9bac8c1120c5e0aa9ce02ac"></a>
<a id="agroup__bt__mesh__dfu__srv_html_ga77142a1f3cfe2ff1d53332114f977b38"></a>
<a id="agroup__bt__mesh__dfu__srv_html_ga94107fb1ca9207fc6918eae1fb1b3755"></a>
<a id="agroup__bt__mesh__dfu__srv_html_ga9f125ace97a40f060e0d8c59fd49f514"></a>
<a id="agroup__bt__mesh__dfu__srv_html_gaf5a00dd89faf52cd7797c54c572e1211"></a>
<a id="agroup__bt__mesh__dfu_html_gae7d7ef4ed1e65e5f8e1641a9c00bb7e8"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__blob__io_html"></a>
<a id="astructbt__mesh__blob__srv__cb_html"></a>
<a id="astructbt__mesh__blob__srv_html"></a>
<a id="astructbt__mesh__dfu__img_html"></a>
<a id="astructbt__mesh__dfu__srv__cb_html"></a>
<a id="astructbt__mesh__dfu__srv__cb_html_a3fec449cebe43dd2d8e6ecf3c148234d"></a>
<a id="astructbt__mesh__dfu__srv__cb_html_a822ed15f15286ad4c5ce69009349f6cf"></a>
<a id="astructbt__mesh__dfu__srv__cb_html_adaefef5067cf3ea273f1db95ca536254"></a>
<a id="astructbt__mesh__dfu__srv__cb_html_afbde918804e66160ffa176c206540027"></a>
<a id="astructbt__mesh__dfu__srv__cb_html_afe4b6ca9f56938695addba6ecc18bb4b"></a>
<a id="astructbt__mesh__dfu__srv_html"></a>
<a id="astructbt__mesh__dfu__srv_html_a23fad6646192b4bdaf80e5bfa3cdf928"></a>
<a id="astructbt__mesh__dfu__srv_html_a75fa0d64310958904435f0b08ae9e5a4"></a>
<a id="astructbt__mesh__dfu__srv_html_ab372c28be95c833146f10236d9e3ecfe"></a>
<a id="astructbt__mesh__dfu__srv_html_ab3cdb7ca3928bccebfcf59fab7f76e51"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructnet__buf__simple_html"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_SRV_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_SRV_H__

#include <zephyr/bluetooth/mesh/dfu.h>
#include <zephyr/bluetooth/mesh/blob_srv.h>
#include <zephyr/bluetooth/mesh/access.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_dfu_srv;

#define BT_MESH_DFU_SRV_INIT(_handlers, _imgs, _img_count)                     \
        {                                                                      \
                .blob = { .cb = &_bt_mesh_dfu_srv_blob_cb }, .cb = _handlers,  \
                .imgs = _imgs, .img_count = _img_count,                        \
        }

#define BT_MESH_MODEL_DFU_SRV(_srv)                                            \
        BT_MESH_MODEL_BLOB_SRV(&(_srv)->blob),                                  \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_DFU_SRV, _bt_mesh_dfu_srv_op, NULL,  \
                         _srv, &_bt_mesh_dfu_srv_cb)

struct bt_mesh_dfu_srv_cb {
        int (*check)(struct bt_mesh_dfu_srv *srv,
                     const struct bt_mesh_dfu_img *img,
                     struct net_buf_simple *metadata,
                     enum bt_mesh_dfu_effect *effect);

        int (*start)(struct bt_mesh_dfu_srv *srv,
                     const struct bt_mesh_dfu_img *img,
                     struct net_buf_simple *metadata,
                     const struct bt_mesh_blob_io **io);

        void (*end)(struct bt_mesh_dfu_srv *srv,
                    const struct bt_mesh_dfu_img *img, bool success);

        int (*recover)(struct bt_mesh_dfu_srv *srv,
                       const struct bt_mesh_dfu_img *img,
                       const struct bt_mesh_blob_io **io);

        int (*apply)(struct bt_mesh_dfu_srv *srv,
                     const struct bt_mesh_dfu_img *img);
};

struct bt_mesh_dfu_srv {
        struct bt_mesh_blob_srv blob;
        const struct bt_mesh_dfu_srv_cb *cb;
        const struct bt_mesh_dfu_img *imgs;
        size_t img_count;

        /* Runtime state */
        const struct bt_mesh_model *mod;
        struct {
                /* Effect of transfer, @see bt_mesh_dfu_effect. */
                uint8_t effect;
                /* Current phase, @see bt_mesh_dfu_phase. */
                uint8_t phase;
                uint8_t ttl;
                uint8_t idx;
                uint16_t timeout_base;
                uint16_t meta;
                bool self_update;
        } update;
};

void bt_mesh_dfu_srv_verified(struct bt_mesh_dfu_srv *srv);

void bt_mesh_dfu_srv_rejected(struct bt_mesh_dfu_srv *srv);

void bt_mesh_dfu_srv_cancel(struct bt_mesh_dfu_srv *srv);

void bt_mesh_dfu_srv_applied(struct bt_mesh_dfu_srv *srv);

bool bt_mesh_dfu_srv_is_busy(const struct bt_mesh_dfu_srv *srv);

uint8_t bt_mesh_dfu_srv_progress(const struct bt_mesh_dfu_srv *srv);

extern const struct bt_mesh_model_op _bt_mesh_dfu_srv_op[];
extern const struct bt_mesh_model_cb _bt_mesh_dfu_srv_cb;
extern const struct bt_mesh_blob_srv_cb _bt_mesh_dfu_srv_blob_cb;

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_SRV_H__ */

```

## 16.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 187 行

运行时状态（Runtime state）。

### 注释 3：原第 190 行

传输效果（Effect of transfer），参见 `bt_mesh_dfu_effect`。

### 注释 4：原第 192 行

当前阶段（Current phase），参见 `bt_mesh_dfu_phase`。

### 注释 5：原第 267 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_SRV_H__`。

## 16.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dfu__srv_8h.html)
- [zephyr/bluetooth/mesh/dfu.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h.html)
- [zephyr/bluetooth/mesh/blob_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h.html)
- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)
- [bt_mesh_dfu_srv_cb](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md)
- [check](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md#afbde918804e66160ffa176c206540027)
- [bt_mesh_dfu_img](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)
- [start](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md#adaefef5067cf3ea273f1db95ca536254)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [end](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md#a822ed15f15286ad4c5ce69009349f6cf)
- [recover](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md#a3fec449cebe43dd2d8e6ecf3c148234d)
- [apply](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md#afe4b6ca9f56938695addba6ecc18bb4b)
- [bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)
- [blob](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md#a75fa0d64310958904435f0b08ae9e5a4)
- [cb](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md#a23fad6646192b4bdaf80e5bfa3cdf928)
- [imgs](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md#ab372c28be95c833146f10236d9e3ecfe)
- [img_count](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md#ab3cdb7ca3928bccebfcf59fab7f76e51)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_dfu_srv_verified](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac)
- [bt_mesh_dfu_srv_rejected](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga77142a1f3cfe2ff1d53332114f977b38)
- [bt_mesh_dfu_srv_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#gaf5a00dd89faf52cd7797c54c572e1211)
- [bt_mesh_dfu_srv_applied](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga45aef92fe1de4c45ccb5369c1f5222ee)
- [bt_mesh_dfu_srv_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga94107fb1ca9207fc6918eae1fb1b3755)
- [bt_mesh_dfu_srv_progress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga9f125ace97a40f060e0d8c59fd49f514)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [bt_mesh_blob_srv_cb](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md)
- [access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [blob_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h.html)
- [dfu.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h.html)
- [bt_mesh_dfu_srv_cb::recover](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md#a3fec449cebe43dd2d8e6ecf3c148234d)
- [bt_mesh_dfu_srv_cb::end](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md#a822ed15f15286ad4c5ce69009349f6cf)
- [bt_mesh_dfu_srv_cb::start](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md#adaefef5067cf3ea273f1db95ca536254)
- [bt_mesh_dfu_srv_cb::check](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md#afbde918804e66160ffa176c206540027)
- [bt_mesh_dfu_srv_cb::apply](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md#afe4b6ca9f56938695addba6ecc18bb4b)
- [bt_mesh_dfu_srv::cb](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md#a23fad6646192b4bdaf80e5bfa3cdf928)
- [bt_mesh_dfu_srv::blob](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md#a75fa0d64310958904435f0b08ae9e5a4)
- [bt_mesh_dfu_srv::imgs](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md#ab372c28be95c833146f10236d9e3ecfe)
- [bt_mesh_dfu_srv::img_count](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md#ab3cdb7ca3928bccebfcf59fab7f76e51)

---

[上一章](P015_ctype.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P017_dma_mcux_pxp.h_源码浏览.md)
