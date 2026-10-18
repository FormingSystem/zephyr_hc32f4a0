---
id: learning.zephyr-docs.api-source-reference.page-126
title: dfu.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第126章\_dfu.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h.html)。

## 126.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
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
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="foldopen00114"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="foldopen00146"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00158"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="ablob_8h_html"></a>
<a id="agroup__bt__mesh__dfu_html_ga82475cb72f2ea8b60e70d6987eca2ff6"></a>
<a id="agroup__bt__mesh__dfu_html_ga8f2afd35a2215f51cd08debe6e1c8ae4"></a>
<a id="agroup__bt__mesh__dfu_html_ga99919dcee1e41bc74bd59e33bec2ded2"></a>
<a id="agroup__bt__mesh__dfu_html_ga9e627a3c15de782faa11ef6c4ec5e05d"></a>
<a id="agroup__bt__mesh__dfu_html_gacd0f7b01837809a0a92d27f248a9fdd3"></a>
<a id="agroup__bt__mesh__dfu_html_gae7d7ef4ed1e65e5f8e1641a9c00bb7e8"></a>
<a id="agroup__bt__mesh__dfu_html_gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba"></a>
<a id="agroup__bt__mesh__dfu_html_gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be"></a>
<a id="agroup__bt__mesh__dfu_html_gga99919dcee1e41bc74bd59e33bec2ded2a36ff3279f4e7683310015b80710e11ad"></a>
<a id="agroup__bt__mesh__dfu_html_gga99919dcee1e41bc74bd59e33bec2ded2a7be52104081ed2b8880aa4175351d4b7"></a>
<a id="agroup__bt__mesh__dfu_html_gga99919dcee1e41bc74bd59e33bec2ded2a98de12815a145378849c71d4a4c3bc65"></a>
<a id="agroup__bt__mesh__dfu_html_gga99919dcee1e41bc74bd59e33bec2ded2a9de660580a58dea6ba6e97ea0d371156"></a>
<a id="agroup__bt__mesh__dfu_html_gga99919dcee1e41bc74bd59e33bec2ded2ab0e56b13787d57d1db20c04f197b0771"></a>
<a id="agroup__bt__mesh__dfu_html_gga99919dcee1e41bc74bd59e33bec2ded2ab36713294a0e68d8b1615374d2a65266"></a>
<a id="agroup__bt__mesh__dfu_html_gga99919dcee1e41bc74bd59e33bec2ded2ab51ff97ee07154b6e94f7886bf99ffca"></a>
<a id="agroup__bt__mesh__dfu_html_gga99919dcee1e41bc74bd59e33bec2ded2abf0e855c2393a272887df9f45e9475e8"></a>
<a id="agroup__bt__mesh__dfu_html_gga99919dcee1e41bc74bd59e33bec2ded2ad8fdc7da5216a666999a5918f4632c7f"></a>
<a id="agroup__bt__mesh__dfu_html_gga99919dcee1e41bc74bd59e33bec2ded2ade806d4326588400748caef1a0bb587e"></a>
<a id="agroup__bt__mesh__dfu_html_gga99919dcee1e41bc74bd59e33bec2ded2af9515160965c55602e623498e01bbc51"></a>
<a id="agroup__bt__mesh__dfu_html_gga9e627a3c15de782faa11ef6c4ec5e05da1f23483a915866abeeefddb0ff126047"></a>
<a id="agroup__bt__mesh__dfu_html_gga9e627a3c15de782faa11ef6c4ec5e05da2eb1e712cc20311cc303eeed7d94701c"></a>
<a id="agroup__bt__mesh__dfu_html_gga9e627a3c15de782faa11ef6c4ec5e05da3e95581f4bd3981b86c037df8e38f806"></a>
<a id="agroup__bt__mesh__dfu_html_gga9e627a3c15de782faa11ef6c4ec5e05da4b5aeee1bfc7e4d855205c7d623ad33a"></a>
<a id="agroup__bt__mesh__dfu_html_gga9e627a3c15de782faa11ef6c4ec5e05da59c78171ab24cffdd2453dff1f377934"></a>
<a id="agroup__bt__mesh__dfu_html_gga9e627a3c15de782faa11ef6c4ec5e05da8021a64fb42385544cb8f8ef7b2bca27"></a>
<a id="agroup__bt__mesh__dfu_html_gga9e627a3c15de782faa11ef6c4ec5e05da8e1990cba0513aa0ad0a95625e949e25"></a>
<a id="agroup__bt__mesh__dfu_html_gga9e627a3c15de782faa11ef6c4ec5e05da9829bf8e37e6eeec483752ebb73325ad"></a>
<a id="agroup__bt__mesh__dfu_html_ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a049447eb32bcc0b1b18d5ae908de30b8"></a>
<a id="agroup__bt__mesh__dfu_html_ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211"></a>
<a id="agroup__bt__mesh__dfu_html_ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a399d11f493d538d6d11a6aee927015dc"></a>
<a id="agroup__bt__mesh__dfu_html_ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8af8fba9033b663ce141c099b48128b22e"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__mesh__dfu__img_html"></a>
<a id="astructbt__mesh__dfu__img_html_a578b2932efb07a3e4eb80043902cc7a0"></a>
<a id="astructbt__mesh__dfu__img_html_a97e17c59a0528462d554d6bbe78858da"></a>
<a id="astructbt__mesh__dfu__img_html_aa4d91e47dd4c20939d8ef8ada0b86f83"></a>
<a id="astructbt__mesh__dfu__slot_html"></a>
<a id="astructbt__mesh__dfu__slot_html_a3f6258793af506b639dd384562fc4a20"></a>
<a id="astructbt__mesh__dfu__slot_html_a47ab534d52e931155dfc7cf4e2444999"></a>
<a id="astructbt__mesh__dfu__slot_html_a9ab5db428c7d57803d6bbc5f26f9c7bb"></a>
<a id="astructbt__mesh__dfu__slot_html_aa554bde6cdffa419ada8ea7410118947"></a>
<a id="astructbt__mesh__dfu__slot_html_af3e056bf835365afda82f3ec8342d926"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_H__

#include <sys/types.h>

#include <zephyr/kernel.h>
#include <zephyr/bluetooth/mesh/blob.h>

#ifdef __cplusplus
extern "C" {
#endif


#ifndef CONFIG_BT_MESH_DFU_FWID_MAXLEN
#define CONFIG_BT_MESH_DFU_FWID_MAXLEN 0
#endif

#ifndef CONFIG_BT_MESH_DFU_METADATA_MAXLEN
#define CONFIG_BT_MESH_DFU_METADATA_MAXLEN 0
#endif

#ifndef CONFIG_BT_MESH_DFU_URI_MAXLEN
#define CONFIG_BT_MESH_DFU_URI_MAXLEN 0
#endif

#ifndef CONFIG_BT_MESH_DFU_SLOT_CNT
#define CONFIG_BT_MESH_DFU_SLOT_CNT 0
#endif

enum bt_mesh_dfu_phase {
        BT_MESH_DFU_PHASE_IDLE,

        BT_MESH_DFU_PHASE_TRANSFER_ERR,

        BT_MESH_DFU_PHASE_TRANSFER_ACTIVE,

        BT_MESH_DFU_PHASE_VERIFY,

        BT_MESH_DFU_PHASE_VERIFY_OK,

        BT_MESH_DFU_PHASE_VERIFY_FAIL,

        BT_MESH_DFU_PHASE_APPLYING,

        BT_MESH_DFU_PHASE_TRANSFER_CANCELED,

        BT_MESH_DFU_PHASE_APPLY_SUCCESS,

        BT_MESH_DFU_PHASE_APPLY_FAIL,

        BT_MESH_DFU_PHASE_UNKNOWN,
};


enum bt_mesh_dfu_status {
        BT_MESH_DFU_SUCCESS,

        BT_MESH_DFU_ERR_RESOURCES,

        BT_MESH_DFU_ERR_WRONG_PHASE,

        BT_MESH_DFU_ERR_INTERNAL,

        BT_MESH_DFU_ERR_FW_IDX,

        BT_MESH_DFU_ERR_METADATA,

        BT_MESH_DFU_ERR_TEMPORARILY_UNAVAILABLE,

        BT_MESH_DFU_ERR_BLOB_XFER_BUSY,
};

enum bt_mesh_dfu_effect {
        BT_MESH_DFU_EFFECT_NONE,

        BT_MESH_DFU_EFFECT_COMP_CHANGE_NO_RPR,

        BT_MESH_DFU_EFFECT_COMP_CHANGE,

        BT_MESH_DFU_EFFECT_UNPROV,
};

enum bt_mesh_dfu_iter {
        BT_MESH_DFU_ITER_STOP,

        BT_MESH_DFU_ITER_CONTINUE,
};

struct bt_mesh_dfu_img {
        const void *fwid;

        size_t fwid_len;

        const char *uri;
};

struct bt_mesh_dfu_slot {
        size_t size;
        size_t fwid_len;
        size_t metadata_len;
        uint8_t fwid[CONFIG_BT_MESH_DFU_FWID_MAXLEN];
        uint8_t metadata[CONFIG_BT_MESH_DFU_METADATA_MAXLEN];
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_H__ */
```

## 126.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 177 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_DFU_H__`。

## 126.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/bluetooth/mesh/blob.h](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h.html)
- [bt_mesh_dfu_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga99919dcee1e41bc74bd59e33bec2ded2)
- [BT_MESH_DFU_PHASE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a9de660580a58dea6ba6e97ea0d371156)
- [BT_MESH_DFU_PHASE_TRANSFER_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ab0e56b13787d57d1db20c04f197b0771)
- [BT_MESH_DFU_PHASE_TRANSFER_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a36ff3279f4e7683310015b80710e11ad)
- [BT_MESH_DFU_PHASE_VERIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a98de12815a145378849c71d4a4c3bc65)
- [BT_MESH_DFU_PHASE_VERIFY_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2abf0e855c2393a272887df9f45e9475e8)
- [BT_MESH_DFU_PHASE_VERIFY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ade806d4326588400748caef1a0bb587e)
- [BT_MESH_DFU_PHASE_APPLYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ad8fdc7da5216a666999a5918f4632c7f)
- [BT_MESH_DFU_PHASE_TRANSFER_CANCELED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2af9515160965c55602e623498e01bbc51)
- [BT_MESH_DFU_PHASE_APPLY_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ab51ff97ee07154b6e94f7886bf99ffca)
- [BT_MESH_DFU_PHASE_APPLY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2ab36713294a0e68d8b1615374d2a65266)
- [BT_MESH_DFU_PHASE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga99919dcee1e41bc74bd59e33bec2ded2a7be52104081ed2b8880aa4175351d4b7)
- [bt_mesh_dfu_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga9e627a3c15de782faa11ef6c4ec5e05d)
- [BT_MESH_DFU_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da9829bf8e37e6eeec483752ebb73325ad)
- [BT_MESH_DFU_ERR_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da8021a64fb42385544cb8f8ef7b2bca27)
- [BT_MESH_DFU_ERR_WRONG_PHASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da1f23483a915866abeeefddb0ff126047)
- [BT_MESH_DFU_ERR_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da3e95581f4bd3981b86c037df8e38f806)
- [BT_MESH_DFU_ERR_FW_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da2eb1e712cc20311cc303eeed7d94701c)
- [BT_MESH_DFU_ERR_METADATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da59c78171ab24cffdd2453dff1f377934)
- [BT_MESH_DFU_ERR_TEMPORARILY_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da4b5aeee1bfc7e4d855205c7d623ad33a)
- [BT_MESH_DFU_ERR_BLOB_XFER_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga9e627a3c15de782faa11ef6c4ec5e05da8e1990cba0513aa0ad0a95625e949e25)
- [bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)
- [BT_MESH_DFU_EFFECT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8af8fba9033b663ce141c099b48128b22e)
- [BT_MESH_DFU_EFFECT_COMP_CHANGE_NO_RPR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a399d11f493d538d6d11a6aee927015dc)
- [BT_MESH_DFU_EFFECT_COMP_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a049447eb32bcc0b1b18d5ae908de30b8)
- [BT_MESH_DFU_EFFECT_UNPROV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211)
- [bt_mesh_dfu_iter](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga82475cb72f2ea8b60e70d6987eca2ff6)
- [BT_MESH_DFU_ITER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be)
- [BT_MESH_DFU_ITER_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba)
- [bt_mesh_dfu_img](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md)
- [fwid](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md#aa4d91e47dd4c20939d8ef8ada0b86f83)
- [fwid_len](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md#a97e17c59a0528462d554d6bbe78858da)
- [uri](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md#a578b2932efb07a3e4eb80043902cc7a0)
- [bt_mesh_dfu_slot](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md)
- [size](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md#a3f6258793af506b639dd384562fc4a20)
- [fwid_len](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md#a47ab534d52e931155dfc7cf4e2444999)
- [metadata_len](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md#af3e056bf835365afda82f3ec8342d926)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [fwid](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md#a9ab5db428c7d57803d6bbc5f26f9c7bb)
- [CONFIG_BT_MESH_DFU_FWID_MAXLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gacd0f7b01837809a0a92d27f248a9fdd3)
- [metadata](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md#aa554bde6cdffa419ada8ea7410118947)
- [CONFIG_BT_MESH_DFU_METADATA_MAXLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga8f2afd35a2215f51cd08debe6e1c8ae4)
- [blob.h](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [bt_mesh_dfu_img::uri](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md#a578b2932efb07a3e4eb80043902cc7a0)
- [bt_mesh_dfu_img::fwid_len](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md#a97e17c59a0528462d554d6bbe78858da)
- [bt_mesh_dfu_img::fwid](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md#aa4d91e47dd4c20939d8ef8ada0b86f83)
- [bt_mesh_dfu_slot::size](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md#a3f6258793af506b639dd384562fc4a20)
- [bt_mesh_dfu_slot::fwid_len](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md#a47ab534d52e931155dfc7cf4e2444999)
- [bt_mesh_dfu_slot::fwid](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md#a9ab5db428c7d57803d6bbc5f26f9c7bb)
- [bt_mesh_dfu_slot::metadata](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md#aa554bde6cdffa419ada8ea7410118947)
- [bt_mesh_dfu_slot::metadata_len](../bluetooth_mesh_model_reference/P054_bt_mesh_dfu_slot_结构体.md#af3e056bf835365afda82f3ec8342d926)

---

[上一章](P125_dfd_srv.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P127_dfu_metadata.h_源码浏览.md)
