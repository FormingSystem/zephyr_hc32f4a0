---
id: learning.zephyr-docs.api-source-reference.page-125
title: dfd_srv.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfd__srv_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第125章\_dfd\_srv.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dfd__srv_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dfd__srv_8h.html)。

## 125.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00029"></a>
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
<a id="l00042"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="foldopen00211"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="aaccess_8h_html"></a>
<a id="ablob__cli_8h_html"></a>
<a id="ablob__srv_8h_html"></a>
<a id="adfd_8h_html"></a>
<a id="adfu__cli_8h_html"></a>
<a id="agroup__bt__mesh__dfd__srv_html_ga126e2d4df8f58b7de36da46c14b2c804"></a>
<a id="agroup__bt__mesh__dfd_html_ga1cce8331a0876c056b25175df32188fb"></a>
<a id="agroup__bt__mesh__dfd_html_gab6562d62668ebcdb146be35b909c30c2"></a>
<a id="agroup__bt__mesh__dfu_html_gaa0812409217dd069b00d386d8ab17f5c"></a>
<a id="agroup__bt__mesh__dfu_html_gacd0f7b01837809a0a92d27f248a9fdd3"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__blob__cli__inputs_html"></a>
<a id="astructbt__mesh__blob__io_html"></a>
<a id="astructbt__mesh__blob__srv__cb_html"></a>
<a id="astructbt__mesh__blob__srv_html"></a>
<a id="astructbt__mesh__blob__target__pull_html"></a>
<a id="astructbt__mesh__dfd__srv__cb_html"></a>
<a id="astructbt__mesh__dfd__srv__cb_html_a6d6d991b3a5bd5fe69b1648fea94ebe4"></a>
<a id="astructbt__mesh__dfd__srv__cb_html_a73f230a76ea32fb1faee15a5d4adb550"></a>
<a id="astructbt__mesh__dfd__srv__cb_html_a84e14ad78ebe520bad3ad6ee24fbb629"></a>
<a id="astructbt__mesh__dfd__srv__cb_html_ae72a527cae827e0a234af3277384d07f"></a>
<a id="astructbt__mesh__dfd__srv_html"></a>
<a id="astructbt__mesh__dfd__srv_html_a02b5ed65738bf08715bbc6a177c6f1ce"></a>
<a id="astructbt__mesh__dfd__srv_html_a1345da3143b1d3334a55ad8053967bf9"></a>
<a id="astructbt__mesh__dfd__srv_html_a1d022e6e15350cd85999f0b07e34f519"></a>
<a id="astructbt__mesh__dfd__srv_html_a20bce6a528c1ef8433f55e8a4277a0ca"></a>
<a id="astructbt__mesh__dfd__srv_html_a26e4b13a8688f26c3330a2b0948bfc8d"></a>
<a id="astructbt__mesh__dfd__srv_html_a4a7847580637713b305918c77210e3c0"></a>
<a id="astructbt__mesh__dfd__srv_html_a4e28f0e0845d1aeb6ebc03032ecfe813"></a>
<a id="astructbt__mesh__dfd__srv_html_a52b10a938105d0fb22e72e30fc92df5c"></a>
<a id="astructbt__mesh__dfd__srv_html_a67e4997a4367d9547a0ae9ff6c2017d6"></a>
<a id="astructbt__mesh__dfd__srv_html_a691eb383f51fd6e10b615ab8921005de"></a>
<a id="astructbt__mesh__dfd__srv_html_a7edbfa6bedb887a941b7567b9eeac8fd"></a>
<a id="astructbt__mesh__dfd__srv_html_ab538079d9f6b98f0de65583d6bdfe7f0"></a>
<a id="astructbt__mesh__dfd__srv_html_abde92a8837d687ef213836d593bf979d"></a>
<a id="astructbt__mesh__dfd__srv_html_af1ac88ae8d9e1e42ff8a98d3969c359d"></a>
<a id="astructbt__mesh__dfd__srv_html_af61665ebb2f46bd3e6277c6ee95ff68c"></a>
<a id="astructbt__mesh__dfu__cli__cb_html"></a>
<a id="astructbt__mesh__dfu__cli_html"></a>
<a id="astructbt__mesh__dfu__slot_html"></a>
<a id="astructbt__mesh__dfu__target_html"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ctx_html"></a>
<a id="astructflash__area_html"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFD_SRV_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFD_SRV_H__

#include <zephyr/bluetooth/mesh/access.h>
#include <zephyr/bluetooth/mesh/dfd.h>
#include <zephyr/bluetooth/mesh/blob_srv.h>
#include <zephyr/bluetooth/mesh/blob_cli.h>
#include <zephyr/bluetooth/mesh/dfu_cli.h>

#ifdef __cplusplus
extern "C" {
#endif

#ifndef CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX
#define CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX 0
#endif

#ifndef CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE
#define CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE 0
#endif

#ifndef CONFIG_BT_MESH_DFD_SRV_SLOT_SPACE
#define CONFIG_BT_MESH_DFD_SRV_SLOT_SPACE 0
#endif

struct bt_mesh_dfd_srv;

#ifdef CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD
#define BT_MESH_DFD_SRV_OOB_INIT(_cb, _oob_schemes, _oob_schemes_count)        \
        {                                                                      \
                .cb = _cb,                                                     \
                .dfu = BT_MESH_DFU_CLI_INIT(&_bt_mesh_dfd_srv_dfu_cb),         \
                .upload = {                                                    \
                        .blob = { .cb = &_bt_mesh_dfd_srv_blob_cb },           \
                },                                                             \
                .oob_schemes = {                                               \
                        .schemes = _oob_schemes,                               \
                        .count = _oob_schemes_count,                           \
                },                                                             \
        }
#endif /* CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD */

#define BT_MESH_DFD_SRV_INIT(_cb)                                              \
        {                                                                      \
                .cb = _cb,                                                     \
                .dfu = BT_MESH_DFU_CLI_INIT(&_bt_mesh_dfd_srv_dfu_cb),         \
                .upload = {                                                    \
                        .blob = { .cb = &_bt_mesh_dfd_srv_blob_cb },           \
                },                                                             \
        }

#define BT_MESH_MODEL_DFD_SRV(_srv)                                            \
        BT_MESH_MODEL_DFU_CLI(&(_srv)->dfu),                                   \
        BT_MESH_MODEL_BLOB_SRV(&(_srv)->upload.blob),                          \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_DFD_SRV, _bt_mesh_dfd_srv_op, NULL,  \
                         _srv, &_bt_mesh_dfd_srv_cb)

struct bt_mesh_dfd_srv_cb {

        int (*recv)(struct bt_mesh_dfd_srv *srv,
                    const struct bt_mesh_dfu_slot *slot,
                    const struct bt_mesh_blob_io **io);

#ifdef CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD
        int (*start_oob_upload)(struct bt_mesh_dfd_srv *srv,
                                const struct bt_mesh_dfu_slot *slot,
                                const char *uri, uint8_t uri_len,
                                const uint8_t *fwid, uint16_t fwid_len);

        void (*cancel_oob_upload)(struct bt_mesh_dfd_srv *srv,
                                  const struct bt_mesh_dfu_slot *slot);

        uint8_t (*oob_progress_get)(struct bt_mesh_dfd_srv *srv,
                                    const struct bt_mesh_dfu_slot *slot);
#endif /* CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD */

        void (*del)(struct bt_mesh_dfd_srv *srv,
                    const struct bt_mesh_dfu_slot *slot);

        int (*send)(struct bt_mesh_dfd_srv *srv,
                    const struct bt_mesh_dfu_slot *slot,
                    const struct bt_mesh_blob_io **io);

        void (*phase)(struct bt_mesh_dfd_srv *srv, enum bt_mesh_dfd_phase phase);
};

struct bt_mesh_dfd_srv {
        const struct bt_mesh_dfd_srv_cb *cb;
        const struct bt_mesh_model *mod;
        struct bt_mesh_dfu_cli dfu;
        struct bt_mesh_dfu_target targets[CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX];
        struct bt_mesh_blob_target_pull pull_ctxs[CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX];
        const struct bt_mesh_blob_io *io;
        uint16_t target_cnt;
        uint16_t slot_idx;
        bool apply;
        enum bt_mesh_dfd_phase phase;
        struct bt_mesh_blob_cli_inputs inputs;

        struct {
                enum bt_mesh_dfd_upload_phase phase;
                struct bt_mesh_dfu_slot *slot;
                const struct flash_area *area;
                struct bt_mesh_blob_srv blob;
#ifdef CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD
                bool is_oob;
                bool is_pending_oob_check;
                struct {
                        uint8_t uri_len;
                        uint8_t uri[CONFIG_BT_MESH_DFU_URI_MAXLEN];
                        uint16_t current_fwid_len;
                        uint8_t current_fwid[CONFIG_BT_MESH_DFU_FWID_MAXLEN];
                        struct bt_mesh_msg_ctx ctx;
                } oob;
#endif /* CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD */
        } upload;

#ifdef CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD
        struct {
                const uint8_t *schemes;
                const uint8_t count;
        } oob_schemes;
#endif /* CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD */
};

#ifdef CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD
int bt_mesh_dfd_srv_oob_check_complete(struct bt_mesh_dfd_srv *srv,
                                       const struct bt_mesh_dfu_slot *slot, int status,
                                       uint8_t *fwid, size_t fwid_len);

int bt_mesh_dfd_srv_oob_store_complete(struct bt_mesh_dfd_srv *srv,
                                       const struct bt_mesh_dfu_slot *slot, bool success,
                                       size_t size, const uint8_t *metadata, size_t metadata_len);
#endif /* CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD */

extern const struct bt_mesh_model_op _bt_mesh_dfd_srv_op[];
extern const struct bt_mesh_model_cb _bt_mesh_dfd_srv_cb;
extern const struct bt_mesh_dfu_cli_cb _bt_mesh_dfd_srv_dfu_cb;
extern const struct bt_mesh_blob_srv_cb _bt_mesh_dfd_srv_blob_cb;

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFD_SRV_H__ */

```

## 125.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 66 行

条件编译配置（Configuration）标记：`CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD`。

### 注释 3：原第 170 行

条件编译配置（Configuration）标记：`CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD`。

### 注释 4：原第 239 行

条件编译配置（Configuration）标记：`CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD`。

### 注释 5：原第 247 行

条件编译配置（Configuration）标记：`CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD`。

### 注释 6：原第 298 行

条件编译配置（Configuration）标记：`CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD`。

### 注释 7：原第 311 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFD_SRV_H__`。

## 125.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dfd__srv_8h.html)
- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [zephyr/bluetooth/mesh/dfd.h](https://docs.zephyrproject.org/latest/doxygen/html/dfd_8h.html)
- [zephyr/bluetooth/mesh/blob_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h.html)
- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h.html)
- [zephyr/bluetooth/mesh/dfu_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h.html)
- [bt_mesh_dfd_srv](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md)
- [bt_mesh_dfd_srv_cb](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md)
- [recv](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md#a6d6d991b3a5bd5fe69b1648fea94ebe4)
- [bt_mesh_dfu_slot](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [del](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md#a73f230a76ea32fb1faee15a5d4adb550)
- [send](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md#a84e14ad78ebe520bad3ad6ee24fbb629)
- [phase](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md#ae72a527cae827e0a234af3277384d07f)
- [bt_mesh_dfd_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gab6562d62668ebcdb146be35b909c30c2)
- [cb](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a7edbfa6bedb887a941b7567b9eeac8fd)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [mod](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a20bce6a528c1ef8433f55e8a4277a0ca)
- [bt_mesh_dfu_cli](../bluetooth_mesh_model_reference/P046_bt_mesh_dfu_cli_结构体.md)
- [dfu](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a1d022e6e15350cd85999f0b07e34f519)
- [bt_mesh_dfu_target](../bluetooth_mesh_model_reference/P057_bt_mesh_dfu_target_结构体.md)
- [targets](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#abde92a8837d687ef213836d593bf979d)
- [CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html#ga126e2d4df8f58b7de36da46c14b2c804)
- [bt_mesh_blob_target_pull](../bluetooth_mesh_model_reference/P013_bt_mesh_blob_target_pull_结构体.md)
- [pull_ctxs](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a1345da3143b1d3334a55ad8053967bf9)
- [io](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a691eb383f51fd6e10b615ab8921005de)
- [target_cnt](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a67e4997a4367d9547a0ae9ff6c2017d6)
- [slot_idx](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#af61665ebb2f46bd3e6277c6ee95ff68c)
- [apply](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#af1ac88ae8d9e1e42ff8a98d3969c359d)
- [phase](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a4a7847580637713b305918c77210e3c0)
- [bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)
- [inputs](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a4e28f0e0845d1aeb6ebc03032ecfe813)
- [bt_mesh_dfd_upload_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ga1cce8331a0876c056b25175df32188fb)
- [slot](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a02b5ed65738bf08715bbc6a177c6f1ce)
- [flash_area](../system_service_model_reference/P027_flash_area_结构体.md)
- [area](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a52b10a938105d0fb22e72e30fc92df5c)
- [bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)
- [blob](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#ab538079d9f6b98f0de65583d6bdfe7f0)
- [CONFIG_BT_MESH_DFU_URI_MAXLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gaa0812409217dd069b00d386d8ab17f5c)
- [CONFIG_BT_MESH_DFU_FWID_MAXLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gacd0f7b01837809a0a92d27f248a9fdd3)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [upload](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a26e4b13a8688f26c3330a2b0948bfc8d)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [bt_mesh_dfu_cli_cb](../bluetooth_mesh_model_reference/P047_bt_mesh_dfu_cli_cb_结构体.md)
- [bt_mesh_blob_srv_cb](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md)
- [access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h.html)
- [blob_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h.html)
- [dfd.h](https://docs.zephyrproject.org/latest/doxygen/html/dfd_8h.html)
- [dfu_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h.html)
- [bt_mesh_dfd_srv_cb::recv](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md#a6d6d991b3a5bd5fe69b1648fea94ebe4)
- [bt_mesh_dfd_srv_cb::del](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md#a73f230a76ea32fb1faee15a5d4adb550)
- [bt_mesh_dfd_srv_cb::send](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md#a84e14ad78ebe520bad3ad6ee24fbb629)
- [bt_mesh_dfd_srv_cb::phase](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md#ae72a527cae827e0a234af3277384d07f)
- [bt_mesh_dfd_srv::slot](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a02b5ed65738bf08715bbc6a177c6f1ce)
- [bt_mesh_dfd_srv::pull_ctxs](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a1345da3143b1d3334a55ad8053967bf9)
- [bt_mesh_dfd_srv::dfu](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a1d022e6e15350cd85999f0b07e34f519)
- [bt_mesh_dfd_srv::mod](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a20bce6a528c1ef8433f55e8a4277a0ca)
- [bt_mesh_dfd_srv::upload](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a26e4b13a8688f26c3330a2b0948bfc8d)
- [bt_mesh_dfd_srv::phase](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a4a7847580637713b305918c77210e3c0)
- [bt_mesh_dfd_srv::inputs](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a4e28f0e0845d1aeb6ebc03032ecfe813)
- [bt_mesh_dfd_srv::area](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a52b10a938105d0fb22e72e30fc92df5c)
- [bt_mesh_dfd_srv::target_cnt](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a67e4997a4367d9547a0ae9ff6c2017d6)
- [bt_mesh_dfd_srv::io](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a691eb383f51fd6e10b615ab8921005de)
- [bt_mesh_dfd_srv::cb](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#a7edbfa6bedb887a941b7567b9eeac8fd)
- [bt_mesh_dfd_srv::blob](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#ab538079d9f6b98f0de65583d6bdfe7f0)
- [bt_mesh_dfd_srv::targets](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#abde92a8837d687ef213836d593bf979d)
- [bt_mesh_dfd_srv::apply](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#af1ac88ae8d9e1e42ff8a98d3969c359d)
- [bt_mesh_dfd_srv::slot_idx](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md#af61665ebb2f46bd3e6277c6ee95ff68c)

---

[上一章](P124_dfd.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P126_dfu.h_源码浏览.md)
