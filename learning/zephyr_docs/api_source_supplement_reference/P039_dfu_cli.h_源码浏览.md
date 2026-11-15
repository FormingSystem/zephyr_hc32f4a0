---
id: learning.zephyr-docs.api-source-supplement-reference.page-39
title: dfu_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_dfu\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h.html)。

## 39.1\_原始可见代码（Source Code）

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
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="foldopen00184"></a>
<a id="l00184"></a>
<a id="l00186"></a>
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
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="foldopen00215"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="foldopen00223"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="aaccess_8h_html"></a>
<a id="ablob__cli_8h_html"></a>
<a id="adfu_8h_html"></a>
<a id="agroup__bt__mesh__blob_html_gae0cb28c0e50d02f6e003062457053618"></a>
<a id="agroup__bt__mesh__dfu__cli_html_ga0011fb5c03e6e8c2babfb677d528033b"></a>
<a id="agroup__bt__mesh__dfu__cli_html_ga073c5bc227040f1f33e7b3f2fe69a309"></a>
<a id="agroup__bt__mesh__dfu__cli_html_ga20764694315adb4f846dcff20f377417"></a>
<a id="agroup__bt__mesh__dfu__cli_html_ga20b3e7d3d3640149a20d698a6aa7dca5"></a>
<a id="agroup__bt__mesh__dfu__cli_html_ga2904ba992a00ee9fba6704c1efc8f074"></a>
<a id="agroup__bt__mesh__dfu__cli_html_ga2967b89e8fc3b848b70e493f6e821761"></a>
<a id="agroup__bt__mesh__dfu__cli_html_ga3dd10bd1e8673973fd6db98d3ebda354"></a>
<a id="agroup__bt__mesh__dfu__cli_html_ga4c33f9457d4f367760a51a771dfd2671"></a>
<a id="agroup__bt__mesh__dfu__cli_html_ga4c7353f45a6e33884844fd9d2f443750"></a>
<a id="agroup__bt__mesh__dfu__cli_html_ga603adf5b40b6e382c9035c9f2bad99a9"></a>
<a id="agroup__bt__mesh__dfu__cli_html_gaa1ed22da058839c9f3234ce2e41eda32"></a>
<a id="agroup__bt__mesh__dfu__cli_html_gab754da11705a2d6a24ec828aa7862579"></a>
<a id="agroup__bt__mesh__dfu__cli_html_gad6308700322d96676635bcf0b70c74f7"></a>
<a id="agroup__bt__mesh__dfu__cli_html_gaf76f0cdb5c6b0df12ddb495c718c3c93"></a>
<a id="agroup__bt__mesh__dfu_html_ga82475cb72f2ea8b60e70d6987eca2ff6"></a>
<a id="agroup__bt__mesh__dfu_html_ga99919dcee1e41bc74bd59e33bec2ded2"></a>
<a id="agroup__bt__mesh__dfu_html_ga9e627a3c15de782faa11ef6c4ec5e05d"></a>
<a id="agroup__bt__mesh__dfu_html_gae7d7ef4ed1e65e5f8e1641a9c00bb7e8"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__blob__cli__cb_html"></a>
<a id="astructbt__mesh__blob__cli__inputs_html"></a>
<a id="astructbt__mesh__blob__cli_html"></a>
<a id="astructbt__mesh__blob__io_html"></a>
<a id="astructbt__mesh__blob__target_html"></a>
<a id="astructbt__mesh__blob__xfer_html"></a>
<a id="astructbt__mesh__dfu__cli__cb_html"></a>
<a id="astructbt__mesh__dfu__cli__cb_html_a32b20280b2196437bad6d85edc017c63"></a>
<a id="astructbt__mesh__dfu__cli__cb_html_a6f580db9629d81f72c79d00a5aea2de4"></a>
<a id="astructbt__mesh__dfu__cli__cb_html_aa3c8985490a6b2bd6fcd81dff0132060"></a>
<a id="astructbt__mesh__dfu__cli__cb_html_ab4d00147b1e525f392d09d5545de2465"></a>
<a id="astructbt__mesh__dfu__cli__cb_html_ad2abfdf93f23cecd30e12241bb064a7f"></a>
<a id="astructbt__mesh__dfu__cli__xfer__blob__params_html"></a>
<a id="astructbt__mesh__dfu__cli__xfer__blob__params_html_a1015b239306bd5eb1c9648b5c1d59481"></a>
<a id="astructbt__mesh__dfu__cli__xfer__blob__params_html_a45452ae73f585ffba5c76291d41dd1ed"></a>
<a id="astructbt__mesh__dfu__cli__xfer_html"></a>
<a id="astructbt__mesh__dfu__cli__xfer_html_a2c4feacc090dace0986e533257f9b291"></a>
<a id="astructbt__mesh__dfu__cli__xfer_html_a3c25a54eb4e557d749a9fb1ba66aecb4"></a>
<a id="astructbt__mesh__dfu__cli__xfer_html_a6608f683fd94e12f7c3ef5f3de7ec248"></a>
<a id="astructbt__mesh__dfu__cli__xfer_html_adece8c0e0cec2262a7066b27636fc46e"></a>
<a id="astructbt__mesh__dfu__cli_html"></a>
<a id="astructbt__mesh__dfu__cli_html_a18d31020aba939826aa34060a4a28121"></a>
<a id="astructbt__mesh__dfu__cli_html_a29a8240e5d47abaabf9d356bcdcba48d"></a>
<a id="astructbt__mesh__dfu__cli_html_a3e5d177198a4c57ccd98a53c20490c89"></a>
<a id="astructbt__mesh__dfu__cli_html_a40b6dfe0c3dc545afc30cd18c5b498b2"></a>
<a id="astructbt__mesh__dfu__cli_html_a463a5c12df5ba3041c46c5c008d473da"></a>
<a id="astructbt__mesh__dfu__cli_html_a67450510328c50e52fa97c80903508cd"></a>
<a id="astructbt__mesh__dfu__cli_html_a8f5d37bda72f1a112428958404ddce63"></a>
<a id="astructbt__mesh__dfu__cli_html_a9396bb9e1245ab2613e3f7dfd753e793"></a>
<a id="astructbt__mesh__dfu__cli_html_a945b5c9f70086ca57d3ee77704ece6fd"></a>
<a id="astructbt__mesh__dfu__cli_html_a94924c2ad2654a14b23a07ea0351ec1b"></a>
<a id="astructbt__mesh__dfu__cli_html_a9531713e4659188de31015b66dfc38bc"></a>
<a id="astructbt__mesh__dfu__cli_html_a9a8676e704a0346e1030f93d7ab6213c"></a>
<a id="astructbt__mesh__dfu__cli_html_aa6f7be1a8dcd76f519e934654f96c909"></a>
<a id="astructbt__mesh__dfu__cli_html_ab882e681b4bfc66374503c83237f57dd"></a>
<a id="astructbt__mesh__dfu__cli_html_ad6cc63e09b15d8471fde2192977be2ed"></a>
<a id="astructbt__mesh__dfu__cli_html_aeaf4f0114a6a47ec6d866ce7b6714d47"></a>
<a id="astructbt__mesh__dfu__cli_html_af7ec498fa49b8e5cc0a3d67ad8dedee5"></a>
<a id="astructbt__mesh__dfu__img_html"></a>
<a id="astructbt__mesh__dfu__metadata__status_html"></a>
<a id="astructbt__mesh__dfu__metadata__status_html_a1d41b76b66acadc20f7f9ec1f4bc8b9b"></a>
<a id="astructbt__mesh__dfu__metadata__status_html_a299723f7176938b2900cfdae4550965c"></a>
<a id="astructbt__mesh__dfu__metadata__status_html_ae7ad71649f295142e48863b6d884b966"></a>
<a id="astructbt__mesh__dfu__slot_html"></a>
<a id="astructbt__mesh__dfu__target__status_html"></a>
<a id="astructbt__mesh__dfu__target__status_html_a13505201dbafeff54c0b35b445fd4f85"></a>
<a id="astructbt__mesh__dfu__target__status_html_a25b2198ad4970d50707ff7994c9d1415"></a>
<a id="astructbt__mesh__dfu__target__status_html_a2848ad866fbd437164b73a7504b75518"></a>
<a id="astructbt__mesh__dfu__target__status_html_ab2e77b63918bb9a735a4ab20a4ca9333"></a>
<a id="astructbt__mesh__dfu__target__status_html_aedbbfc07a68e60236901a3c79377fe65"></a>
<a id="astructbt__mesh__dfu__target__status_html_aedbd5c0a04460656d0a78eb49fd047b2"></a>
<a id="astructbt__mesh__dfu__target__status_html_aef5cbadbdd7b4b006dc304cd94c1bca4"></a>
<a id="astructbt__mesh__dfu__target_html"></a>
<a id="astructbt__mesh__dfu__target_html_a3d18d0ae1d0902cf84402b090a9aaa99"></a>
<a id="astructbt__mesh__dfu__target_html_a43730ff708da06fe31e801adf7a79c0e"></a>
<a id="astructbt__mesh__dfu__target_html_a4ad51f9dc3fdb39afeef55e4cd22b968"></a>
<a id="astructbt__mesh__dfu__target_html_a96393388212d4bffd8fb00c82e58d364"></a>
<a id="astructbt__mesh__dfu__target_html_a986a58915c0b0ab509ddbbbe475976d2"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ctx_html"></a>
<a id="astructk__sem_html"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_CLI_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_CLI_H__

#include <zephyr/bluetooth/mesh/access.h>
#include <zephyr/bluetooth/mesh/blob_cli.h>
#include <zephyr/bluetooth/mesh/dfu.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_dfu_cli;

#define BT_MESH_DFU_CLI_INIT(_handlers)                                        \
        {                                                                      \
                .cb = _handlers,                                               \
                .blob = { .cb = &_bt_mesh_dfu_cli_blob_handlers },             \
        }

#define BT_MESH_MODEL_DFU_CLI(_cli)                                            \
        BT_MESH_MODEL_BLOB_CLI(&(_cli)->blob),                                 \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_DFU_CLI, _bt_mesh_dfu_cli_op, NULL,  \
                         _cli, &_bt_mesh_dfu_cli_cb)

struct bt_mesh_dfu_target {
        struct bt_mesh_blob_target blob;
        uint8_t img_idx;
        uint8_t effect;
        uint8_t status;
        uint8_t phase;
};

struct bt_mesh_dfu_metadata_status {
        uint8_t idx;
        enum bt_mesh_dfu_status status;
        enum bt_mesh_dfu_effect effect;
};

struct bt_mesh_dfu_target_status {
        enum bt_mesh_dfu_status status;
        enum bt_mesh_dfu_phase phase;
        enum bt_mesh_dfu_effect effect;
        uint64_t blob_id;
        uint8_t img_idx;
        uint8_t ttl;

        uint16_t timeout_base;
};

typedef enum bt_mesh_dfu_iter (*bt_mesh_dfu_img_cb_t)(
        struct bt_mesh_dfu_cli *cli, struct bt_mesh_msg_ctx *ctx, uint8_t idx,
        uint8_t total, const struct bt_mesh_dfu_img *img, void *cb_data);

struct bt_mesh_dfu_cli_cb {
        void (*suspended)(struct bt_mesh_dfu_cli *cli);

        void (*ended)(struct bt_mesh_dfu_cli *cli,
                      enum bt_mesh_dfu_status reason);

        void (*applied)(struct bt_mesh_dfu_cli *cli);

        void (*confirmed)(struct bt_mesh_dfu_cli *cli);

        void (*lost_target)(struct bt_mesh_dfu_cli *cli,
                            struct bt_mesh_dfu_target *target);
};

struct bt_mesh_dfu_cli {
        const struct bt_mesh_dfu_cli_cb *cb;
        struct bt_mesh_blob_cli blob;

        /* runtime state */

        uint32_t op;
        const struct bt_mesh_model *mod;

        struct {
                const struct bt_mesh_dfu_slot *slot;
                const struct bt_mesh_blob_io *io;
                struct bt_mesh_blob_xfer blob;
                uint8_t state;
                uint8_t flags;
        } xfer;

        struct {
                uint8_t ttl;
                uint8_t type;
                uint8_t img_cnt;
                uint16_t addr;
                struct k_sem sem;
                void *params;
                bt_mesh_dfu_img_cb_t img_cb;
        } req;
};

struct bt_mesh_dfu_cli_xfer_blob_params {
        /* Logarithmic representation of the block size. */
        uint8_t block_size_log;
        uint16_t chunk_size;
};

struct bt_mesh_dfu_cli_xfer {
        uint64_t blob_id;
        const struct bt_mesh_dfu_slot *slot;
        enum bt_mesh_blob_xfer_mode mode;
        const struct bt_mesh_dfu_cli_xfer_blob_params *blob_params;
};

int bt_mesh_dfu_cli_send(struct bt_mesh_dfu_cli *cli,
                         const struct bt_mesh_blob_cli_inputs *inputs,
                         const struct bt_mesh_blob_io *io,
                         const struct bt_mesh_dfu_cli_xfer *xfer);

int bt_mesh_dfu_cli_suspend(struct bt_mesh_dfu_cli *cli);

int bt_mesh_dfu_cli_resume(struct bt_mesh_dfu_cli *cli);

int bt_mesh_dfu_cli_cancel(struct bt_mesh_dfu_cli *cli,
                           struct bt_mesh_msg_ctx *ctx);

int bt_mesh_dfu_cli_apply(struct bt_mesh_dfu_cli *cli);

int bt_mesh_dfu_cli_confirm(struct bt_mesh_dfu_cli *cli);

uint8_t bt_mesh_dfu_cli_progress(struct bt_mesh_dfu_cli *cli);

bool bt_mesh_dfu_cli_is_busy(struct bt_mesh_dfu_cli *cli);

int bt_mesh_dfu_cli_imgs_get(struct bt_mesh_dfu_cli *cli,
                             struct bt_mesh_msg_ctx *ctx,
                             bt_mesh_dfu_img_cb_t cb, void *cb_data,
                             uint8_t max_count);

int bt_mesh_dfu_cli_metadata_check(struct bt_mesh_dfu_cli *cli,
                                   struct bt_mesh_msg_ctx *ctx, uint8_t img_idx,
                                   const struct bt_mesh_dfu_slot *slot,
                                   struct bt_mesh_dfu_metadata_status *rsp);

int bt_mesh_dfu_cli_status_get(struct bt_mesh_dfu_cli *cli,
                               struct bt_mesh_msg_ctx *ctx,
                               struct bt_mesh_dfu_target_status *rsp);

int32_t bt_mesh_dfu_cli_timeout_get(void);

void bt_mesh_dfu_cli_timeout_set(int32_t timeout);

extern const struct bt_mesh_blob_cli_cb _bt_mesh_dfu_cli_blob_handlers;
extern const struct bt_mesh_model_cb _bt_mesh_dfu_cli_cb;
extern const struct bt_mesh_model_op _bt_mesh_dfu_cli_op[];

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_CLI_H__ */

```

## 39.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 190 行

运行时状态（Runtime state）。

### 注释 3：原第 216 行

块大小的对数表示（Logarithmic representation of block size）。

### 注释 4：原第 407 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_CLI_H__`。

## 39.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h.html)
- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h.html)
- [zephyr/bluetooth/mesh/dfu.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h.html)
- [bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)
- [bt_mesh_dfu_target](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md)
- [bt_mesh_blob_target](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md)
- [blob](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md#a96393388212d4bffd8fb00c82e58d364)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [img_idx](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md#a986a58915c0b0ab509ddbbbe475976d2)
- [effect](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md#a3d18d0ae1d0902cf84402b090a9aaa99)
- [status](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md#a4ad51f9dc3fdb39afeef55e4cd22b968)
- [phase](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md#a43730ff708da06fe31e801adf7a79c0e)
- [bt_mesh_dfu_metadata_status](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md)
- [idx](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md#a1d41b76b66acadc20f7f9ec1f4bc8b9b)
- [bt_mesh_dfu_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga9e627a3c15de782faa11ef6c4ec5e05d)
- [status](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md#ae7ad71649f295142e48863b6d884b966)
- [bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)
- [effect](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md#a299723f7176938b2900cfdae4550965c)
- [bt_mesh_dfu_target_status](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md)
- [status](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#a25b2198ad4970d50707ff7994c9d1415)
- [bt_mesh_dfu_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga99919dcee1e41bc74bd59e33bec2ded2)
- [phase](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#aedbbfc07a68e60236901a3c79377fe65)
- [effect](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#aef5cbadbdd7b4b006dc304cd94c1bca4)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [blob_id](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#a2848ad866fbd437164b73a7504b75518)
- [img_idx](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#aedbd5c0a04460656d0a78eb49fd047b2)
- [ttl](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#ab2e77b63918bb9a735a4ab20a4ca9333)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [timeout_base](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#a13505201dbafeff54c0b35b445fd4f85)
- [bt_mesh_dfu_iter](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga82475cb72f2ea8b60e70d6987eca2ff6)
- [bt_mesh_dfu_img_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga2967b89e8fc3b848b70e493f6e821761)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [bt_mesh_dfu_img](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md)
- [bt_mesh_dfu_cli_cb](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md)
- [suspended](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md#ad2abfdf93f23cecd30e12241bb064a7f)
- [ended](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md#aa3c8985490a6b2bd6fcd81dff0132060)
- [applied](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md#a6f580db9629d81f72c79d00a5aea2de4)
- [confirmed](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md#a32b20280b2196437bad6d85edc017c63)
- [lost_target](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md#ab4d00147b1e525f392d09d5545de2465)
- [cb](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a18d31020aba939826aa34060a4a28121)
- [bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)
- [blob](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a945b5c9f70086ca57d3ee77704ece6fd)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [op](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a94924c2ad2654a14b23a07ea0351ec1b)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [mod](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#ab882e681b4bfc66374503c83237f57dd)
- [bt_mesh_dfu_slot](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md)
- [slot](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a9396bb9e1245ab2613e3f7dfd753e793)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [io](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a29a8240e5d47abaabf9d356bcdcba48d)
- [bt_mesh_blob_xfer](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md)
- [state](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#aeaf4f0114a6a47ec6d866ce7b6714d47)
- [flags](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a3e5d177198a4c57ccd98a53c20490c89)
- [xfer](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a9a8676e704a0346e1030f93d7ab6213c)
- [ttl](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a463a5c12df5ba3041c46c5c008d473da)
- [type](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a40b6dfe0c3dc545afc30cd18c5b498b2)
- [img_cnt](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#aa6f7be1a8dcd76f519e934654f96c909)
- [addr](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a67450510328c50e52fa97c80903508cd)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [sem](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#af7ec498fa49b8e5cc0a3d67ad8dedee5)
- [params](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#ad6cc63e09b15d8471fde2192977be2ed)
- [img_cb](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a9531713e4659188de31015b66dfc38bc)
- [req](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a8f5d37bda72f1a112428958404ddce63)
- [bt_mesh_dfu_cli_xfer_blob_params](../bluetooth_mesh_model_reference/P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md)
- [block_size_log](../bluetooth_mesh_model_reference/P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md#a45452ae73f585ffba5c76291d41dd1ed)
- [chunk_size](../bluetooth_mesh_model_reference/P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md#a1015b239306bd5eb1c9648b5c1d59481)
- [bt_mesh_dfu_cli_xfer](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md)
- [blob_id](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md#adece8c0e0cec2262a7066b27636fc46e)
- [slot](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md#a3c25a54eb4e557d749a9fb1ba66aecb4)
- [bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)
- [mode](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md#a6608f683fd94e12f7c3ef5f3de7ec248)
- [blob_params](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md#a2c4feacc090dace0986e533257f9b291)
- [bt_mesh_dfu_cli_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga20764694315adb4f846dcff20f377417)
- [bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)
- [bt_mesh_dfu_cli_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gaa1ed22da058839c9f3234ce2e41eda32)
- [bt_mesh_dfu_cli_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga0011fb5c03e6e8c2babfb677d528033b)
- [bt_mesh_dfu_cli_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga4c7353f45a6e33884844fd9d2f443750)
- [bt_mesh_dfu_cli_apply](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga2904ba992a00ee9fba6704c1efc8f074)
- [bt_mesh_dfu_cli_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gaf76f0cdb5c6b0df12ddb495c718c3c93)
- [bt_mesh_dfu_cli_progress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga073c5bc227040f1f33e7b3f2fe69a309)
- [bt_mesh_dfu_cli_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gad6308700322d96676635bcf0b70c74f7)
- [bt_mesh_dfu_cli_imgs_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga4c33f9457d4f367760a51a771dfd2671)
- [bt_mesh_dfu_cli_metadata_check](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga20b3e7d3d3640149a20d698a6aa7dca5)
- [bt_mesh_dfu_cli_status_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gab754da11705a2d6a24ec828aa7862579)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_dfu_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga3dd10bd1e8673973fd6db98d3ebda354)
- [bt_mesh_dfu_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga603adf5b40b6e382c9035c9f2bad99a9)
- [bt_mesh_blob_cli_cb](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h.html)
- [dfu.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h.html)
- [bt_mesh_dfu_cli_cb::confirmed](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md#a32b20280b2196437bad6d85edc017c63)
- [bt_mesh_dfu_cli_cb::applied](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md#a6f580db9629d81f72c79d00a5aea2de4)
- [bt_mesh_dfu_cli_cb::ended](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md#aa3c8985490a6b2bd6fcd81dff0132060)
- [bt_mesh_dfu_cli_cb::lost_target](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md#ab4d00147b1e525f392d09d5545de2465)
- [bt_mesh_dfu_cli_cb::suspended](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md#ad2abfdf93f23cecd30e12241bb064a7f)
- [bt_mesh_dfu_cli_xfer_blob_params::chunk_size](../bluetooth_mesh_model_reference/P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md#a1015b239306bd5eb1c9648b5c1d59481)
- [bt_mesh_dfu_cli_xfer_blob_params::block_size_log](../bluetooth_mesh_model_reference/P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md#a45452ae73f585ffba5c76291d41dd1ed)
- [bt_mesh_dfu_cli_xfer::blob_params](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md#a2c4feacc090dace0986e533257f9b291)
- [bt_mesh_dfu_cli_xfer::slot](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md#a3c25a54eb4e557d749a9fb1ba66aecb4)
- [bt_mesh_dfu_cli_xfer::mode](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md#a6608f683fd94e12f7c3ef5f3de7ec248)
- [bt_mesh_dfu_cli_xfer::blob_id](../bluetooth_mesh_model_reference/P048_bt_mesh_dfu_cli_xfer_结构体.md#adece8c0e0cec2262a7066b27636fc46e)
- [bt_mesh_dfu_cli::cb](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a18d31020aba939826aa34060a4a28121)
- [bt_mesh_dfu_cli::io](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a29a8240e5d47abaabf9d356bcdcba48d)
- [bt_mesh_dfu_cli::flags](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a3e5d177198a4c57ccd98a53c20490c89)
- [bt_mesh_dfu_cli::type](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a40b6dfe0c3dc545afc30cd18c5b498b2)
- [bt_mesh_dfu_cli::ttl](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a463a5c12df5ba3041c46c5c008d473da)
- [bt_mesh_dfu_cli::addr](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a67450510328c50e52fa97c80903508cd)
- [bt_mesh_dfu_cli::req](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a8f5d37bda72f1a112428958404ddce63)
- [bt_mesh_dfu_cli::slot](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a9396bb9e1245ab2613e3f7dfd753e793)
- [bt_mesh_dfu_cli::blob](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a945b5c9f70086ca57d3ee77704ece6fd)
- [bt_mesh_dfu_cli::op](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a94924c2ad2654a14b23a07ea0351ec1b)
- [bt_mesh_dfu_cli::img_cb](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a9531713e4659188de31015b66dfc38bc)
- [bt_mesh_dfu_cli::xfer](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#a9a8676e704a0346e1030f93d7ab6213c)
- [bt_mesh_dfu_cli::img_cnt](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#aa6f7be1a8dcd76f519e934654f96c909)
- [bt_mesh_dfu_cli::mod](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#ab882e681b4bfc66374503c83237f57dd)
- [bt_mesh_dfu_cli::params](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#ad6cc63e09b15d8471fde2192977be2ed)
- [bt_mesh_dfu_cli::state](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#aeaf4f0114a6a47ec6d866ce7b6714d47)
- [bt_mesh_dfu_cli::sem](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md#af7ec498fa49b8e5cc0a3d67ad8dedee5)
- [bt_mesh_dfu_metadata_status::idx](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md#a1d41b76b66acadc20f7f9ec1f4bc8b9b)
- [bt_mesh_dfu_metadata_status::effect](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md#a299723f7176938b2900cfdae4550965c)
- [bt_mesh_dfu_metadata_status::status](../bluetooth_mesh_model_reference/P053_bt_mesh_dfu_metadata_status_结构体.md#ae7ad71649f295142e48863b6d884b966)
- [bt_mesh_dfu_target_status::timeout_base](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#a13505201dbafeff54c0b35b445fd4f85)
- [bt_mesh_dfu_target_status::status](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#a25b2198ad4970d50707ff7994c9d1415)
- [bt_mesh_dfu_target_status::blob_id](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#a2848ad866fbd437164b73a7504b75518)
- [bt_mesh_dfu_target_status::ttl](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#ab2e77b63918bb9a735a4ab20a4ca9333)
- [bt_mesh_dfu_target_status::phase](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#aedbbfc07a68e60236901a3c79377fe65)
- [bt_mesh_dfu_target_status::img_idx](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#aedbd5c0a04460656d0a78eb49fd047b2)
- [bt_mesh_dfu_target_status::effect](../bluetooth_mesh_model_reference/P058_bt_mesh_dfu_target_status_结构体.md#aef5cbadbdd7b4b006dc304cd94c1bca4)
- [bt_mesh_dfu_target::effect](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md#a3d18d0ae1d0902cf84402b090a9aaa99)
- [bt_mesh_dfu_target::phase](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md#a43730ff708da06fe31e801adf7a79c0e)
- [bt_mesh_dfu_target::status](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md#a4ad51f9dc3fdb39afeef55e4cd22b968)
- [bt_mesh_dfu_target::blob](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md#a96393388212d4bffd8fb00c82e58d364)
- [bt_mesh_dfu_target::img_idx](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md#a986a58915c0b0ab509ddbbbe475976d2)

---

[上一章](P038_cy8cmbr3xxx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P040_dmic.h_源码浏览.md)
