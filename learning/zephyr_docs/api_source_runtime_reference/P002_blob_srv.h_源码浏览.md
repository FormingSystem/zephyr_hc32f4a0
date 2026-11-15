---
id: learning.zephyr-docs.api-source-runtime-reference.page-2
title: blob_srv.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_blob\_srv.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h.html)。

## 2.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="foldopen00148"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="aaccess_8h_html"></a>
<a id="ablob_8h_html"></a>
<a id="agroup__atomic__apis_html_ga249c575db9764486197709b327f7370e"></a>
<a id="agroup__bt__mesh__blob__srv_html_ga5d35f13eeb6f7a1fb252e8fb905e9cb3"></a>
<a id="agroup__bt__mesh__blob__srv_html_ga674b59ff721575539818ef74e8d1b91c"></a>
<a id="agroup__bt__mesh__blob__srv_html_gaa7a253c9a577eaa1307bc0e6b93a3d66"></a>
<a id="agroup__bt__mesh__blob__srv_html_gaae3dfbf15f33739bc0a42c924de99cba"></a>
<a id="agroup__bt__mesh__blob__srv_html_gae8739e96f2157f588072e91b51891835"></a>
<a id="agroup__bt__mesh__blob_html_ga26ed2c64bae03758a8a53b28052d0f81"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__blob__block_html"></a>
<a id="astructbt__mesh__blob__io_html"></a>
<a id="astructbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state_html"></a>
<a id="astructbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state_html_a08358fb301e775ed23c0d062676fbf22"></a>
<a id="astructbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state_html_a0c87b3052680c675303747e805c2990e"></a>
<a id="astructbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state_html_a0f5d7d310be154f85ee96ccceb12e971"></a>
<a id="astructbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state_html_a6273d55eda23f868d51382c56bc41e27"></a>
<a id="astructbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state_html_a79b0521bbd2473c6b414a24c5a7bf98a"></a>
<a id="astructbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state_html_aadd08825d36f3ae1e4fe3a7845903f41"></a>
<a id="astructbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state_html_ac5d12eef4c5723af0e19296d75f1c820"></a>
<a id="astructbt__mesh__blob__srv__cb_html"></a>
<a id="astructbt__mesh__blob__srv__cb_html_a94b56462c5fd95535a5f1e0ba2ddf99a"></a>
<a id="astructbt__mesh__blob__srv__cb_html_a99a054d410f0a82101b15309a8f4ec33"></a>
<a id="astructbt__mesh__blob__srv__cb_html_aad5ab6e396f049a3b8a239e9f0d1c063"></a>
<a id="astructbt__mesh__blob__srv__cb_html_ae032ff1d52f46f1716451dc5ff138d0f"></a>
<a id="astructbt__mesh__blob__srv__cb_html_af7b6f557f38c15a174a2a75d1210dab3"></a>
<a id="astructbt__mesh__blob__srv_html"></a>
<a id="astructbt__mesh__blob__srv_html_a1066d309b56748223183d39e8fc7fd82"></a>
<a id="astructbt__mesh__blob__srv_html_a23d12a803a2414aa1460ea9a862cc78b"></a>
<a id="astructbt__mesh__blob__srv_html_a65d08187dce1ed86cbfbb4f977cd32df"></a>
<a id="astructbt__mesh__blob__srv_html_a75b8ecd846fcf96708d31fb5efb0bea1"></a>
<a id="astructbt__mesh__blob__srv_html_a82a5c7fc2ad37e531ec10bada27bf10a"></a>
<a id="astructbt__mesh__blob__srv_html_a8d6a01849e95c4a26d3270f4320c214f"></a>
<a id="astructbt__mesh__blob__srv_html_aa3ac872db59f2f1cd67d25e97020d484"></a>
<a id="astructbt__mesh__blob__srv_html_aad6ef41a187cc5489d6a8d5f4a5b3003"></a>
<a id="astructbt__mesh__blob__srv_html_afec2237da95cc7ffbbdeb99d8ffb12b6"></a>
<a id="astructbt__mesh__blob__xfer_html"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ctx_html"></a>
<a id="astructk__work__delayable_html"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_SRV_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_SRV_H_

#include <zephyr/bluetooth/mesh/access.h>
#include <zephyr/bluetooth/mesh/blob.h>

#ifdef __cplusplus
extern "C" {
#endif


struct bt_mesh_blob_srv;

#if defined(CONFIG_BT_MESH_BLOB_SRV)
#define BT_MESH_BLOB_BLOCKS_MAX                                                \
        (DIV_ROUND_UP(CONFIG_BT_MESH_BLOB_SIZE_MAX,                        \
                          CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MIN))
#else
#define BT_MESH_BLOB_BLOCKS_MAX 1
#endif

#define BT_MESH_MODEL_BLOB_SRV(_srv)                                           \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_BLOB_SRV, _bt_mesh_blob_srv_op,      \
                         NULL, _srv, &_bt_mesh_blob_srv_cb)

struct bt_mesh_blob_srv_cb {
        int (*start)(struct bt_mesh_blob_srv *srv, struct bt_mesh_msg_ctx *ctx,
                     struct bt_mesh_blob_xfer *xfer);

        void (*end)(struct bt_mesh_blob_srv *srv, uint64_t id, bool success);

        void (*suspended)(struct bt_mesh_blob_srv *srv);

        void (*resume)(struct bt_mesh_blob_srv *srv);

        int (*recover)(struct bt_mesh_blob_srv *srv,
                       struct bt_mesh_blob_xfer *xfer,
                       const struct bt_mesh_blob_io **io);
};

struct bt_mesh_blob_srv {
        const struct bt_mesh_blob_srv_cb *cb;

        /* Runtime state: */
        const struct bt_mesh_blob_io *io;
        struct k_work_delayable rx_timeout;
        struct bt_mesh_blob_block block;
        const struct bt_mesh_model *mod;
        enum bt_mesh_blob_xfer_phase phase;

        struct bt_mesh_blob_srv_state {
                struct bt_mesh_blob_xfer xfer;
                uint16_t cli;
                uint16_t app_idx;
                uint16_t timeout_base;
                uint16_t mtu_size;
                uint8_t ttl;

                /* Bitfield of pending blocks. */
                ATOMIC_DEFINE(blocks, BT_MESH_BLOB_BLOCKS_MAX);
        } state;

        /* Pull mode (Pull BLOB Transfer Mode) behavior. */
        struct {
                uint16_t chunk_idx;
                struct k_work_delayable report;
        } pull;
};

int bt_mesh_blob_srv_recv(struct bt_mesh_blob_srv *srv, uint64_t id,
                          const struct bt_mesh_blob_io *io, uint8_t ttl,
                          uint16_t timeout_base);

int bt_mesh_blob_srv_cancel(struct bt_mesh_blob_srv *srv);

bool bt_mesh_blob_srv_is_busy(const struct bt_mesh_blob_srv *srv);

uint8_t bt_mesh_blob_srv_progress(const struct bt_mesh_blob_srv *srv);

extern const struct bt_mesh_model_op _bt_mesh_blob_srv_op[];
extern const struct bt_mesh_model_cb _bt_mesh_blob_srv_cb;


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_SRV_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 141 行

运行时状态（Runtime state）：

### 注释 3：原第 156 行

待处理块（Pending blocks）的位域。

### 注释 4：原第 160 行

拉取模式，即拉取式 BLOB 传输模式（Pull BLOB Transfer Mode）的行为。

### 注释 5：原第 226 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_SRV_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h.html)
- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [zephyr/bluetooth/mesh/blob.h](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h.html)
- [bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)
- [bt_mesh_blob_srv_cb](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md)
- [start](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md#aad5ab6e396f049a3b8a239e9f0d1c063)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [bt_mesh_blob_xfer](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md)
- [end](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md#af7b6f557f38c15a174a2a75d1210dab3)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [suspended](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md#a99a054d410f0a82101b15309a8f4ec33)
- [resume](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md#ae032ff1d52f46f1716451dc5ff138d0f)
- [recover](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md#a94b56462c5fd95535a5f1e0ba2ddf99a)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [cb](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a65d08187dce1ed86cbfbb4f977cd32df)
- [io](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a23d12a803a2414aa1460ea9a862cc78b)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [rx_timeout](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a82a5c7fc2ad37e531ec10bada27bf10a)
- [bt_mesh_blob_block](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md)
- [block](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a8d6a01849e95c4a26d3270f4320c214f)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [mod](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a1066d309b56748223183d39e8fc7fd82)
- [bt_mesh_blob_xfer_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga26ed2c64bae03758a8a53b28052d0f81)
- [phase](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a75b8ecd846fcf96708d31fb5efb0bea1)
- [bt_mesh_blob_srv_state](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md)
- [xfer](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#ac5d12eef4c5723af0e19296d75f1c820)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [cli](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#a08358fb301e775ed23c0d062676fbf22)
- [app_idx](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#a6273d55eda23f868d51382c56bc41e27)
- [timeout_base](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#a0c87b3052680c675303747e805c2990e)
- [mtu_size](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#aadd08825d36f3ae1e4fe3a7845903f41)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ttl](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#a79b0521bbd2473c6b414a24c5a7bf98a)
- [ATOMIC_DEFINE](../atomic_reference/P001_原子操作公共接口.md#ga249c575db9764486197709b327f7370e)
- [blocks](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#a0f5d7d310be154f85ee96ccceb12e971)
- [BT_MESH_BLOB_BLOCKS_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#gaae3dfbf15f33739bc0a42c924de99cba)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [chunk_idx](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#aa3ac872db59f2f1cd67d25e97020d484)
- [report](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#aad6ef41a187cc5489d6a8d5f4a5b3003)
- [pull](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#afec2237da95cc7ffbbdeb99d8ffb12b6)
- [bt_mesh_blob_srv_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#ga5d35f13eeb6f7a1fb252e8fb905e9cb3)
- [bt_mesh_blob_srv_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#gae8739e96f2157f588072e91b51891835)
- [bt_mesh_blob_srv_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#gaa7a253c9a577eaa1307bc0e6b93a3d66)
- [bt_mesh_blob_srv_progress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#ga674b59ff721575539818ef74e8d1b91c)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [blob.h](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h.html)
- [bt_mesh_blob_srv::bt_mesh_blob_srv_state](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md)
- [bt_mesh_blob_srv::bt_mesh_blob_srv_state::cli](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#a08358fb301e775ed23c0d062676fbf22)
- [bt_mesh_blob_srv::bt_mesh_blob_srv_state::timeout_base](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#a0c87b3052680c675303747e805c2990e)
- [bt_mesh_blob_srv::bt_mesh_blob_srv_state::blocks](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#a0f5d7d310be154f85ee96ccceb12e971)
- [bt_mesh_blob_srv::bt_mesh_blob_srv_state::app_idx](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#a6273d55eda23f868d51382c56bc41e27)
- [bt_mesh_blob_srv::bt_mesh_blob_srv_state::ttl](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#a79b0521bbd2473c6b414a24c5a7bf98a)
- [bt_mesh_blob_srv::bt_mesh_blob_srv_state::mtu_size](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#aadd08825d36f3ae1e4fe3a7845903f41)
- [bt_mesh_blob_srv::bt_mesh_blob_srv_state::xfer](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md#ac5d12eef4c5723af0e19296d75f1c820)
- [bt_mesh_blob_srv_cb::recover](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md#a94b56462c5fd95535a5f1e0ba2ddf99a)
- [bt_mesh_blob_srv_cb::suspended](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md#a99a054d410f0a82101b15309a8f4ec33)
- [bt_mesh_blob_srv_cb::start](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md#aad5ab6e396f049a3b8a239e9f0d1c063)
- [bt_mesh_blob_srv_cb::resume](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md#ae032ff1d52f46f1716451dc5ff138d0f)
- [bt_mesh_blob_srv_cb::end](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md#af7b6f557f38c15a174a2a75d1210dab3)
- [bt_mesh_blob_srv::mod](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a1066d309b56748223183d39e8fc7fd82)
- [bt_mesh_blob_srv::io](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a23d12a803a2414aa1460ea9a862cc78b)
- [bt_mesh_blob_srv::cb](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a65d08187dce1ed86cbfbb4f977cd32df)
- [bt_mesh_blob_srv::phase](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a75b8ecd846fcf96708d31fb5efb0bea1)
- [bt_mesh_blob_srv::rx_timeout](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a82a5c7fc2ad37e531ec10bada27bf10a)
- [bt_mesh_blob_srv::block](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#a8d6a01849e95c4a26d3270f4320c214f)
- [bt_mesh_blob_srv::chunk_idx](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#aa3ac872db59f2f1cd67d25e97020d484)
- [bt_mesh_blob_srv::report](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#aad6ef41a187cc5489d6a8d5f4a5b3003)
- [bt_mesh_blob_srv::pull](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md#afec2237da95cc7ffbbdeb99d8ffb12b6)

---

[上一章](P001_arm-mps2-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_bmp581_user.h_源码浏览.md)
