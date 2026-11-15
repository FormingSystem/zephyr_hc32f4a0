---
id: learning.zephyr-docs.api-source-supplement-reference.page-91
title: img_mgmt_callbacks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第91章\_img\_mgmt\_callbacks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h.html)。

## 91.1\_原始可见代码（Source Code）

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
<a id="l00036"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00087"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="foldopen00100"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="foldopen00140"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="agroup__mcumgr__callback__api__img__mgmt_html_ga3fa2c42bade08cca1122e32f6315f107"></a>
<a id="agroup__mcumgr__callback__api__img__mgmt_html_gga3fa2c42bade08cca1122e32f6315f107a0ba2354ef268ed22c51df7e5708c50bf"></a>
<a id="agroup__mcumgr__callback__api__img__mgmt_html_gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c"></a>
<a id="agroup__mcumgr__callback__api__img__mgmt_html_gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4"></a>
<a id="agroup__mcumgr__callback__api__img__mgmt_html_gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb"></a>
<a id="agroup__mcumgr__callback__api__img__mgmt_html_gga3fa2c42bade08cca1122e32f6315f107a4204cb29c7308f103644162839abcb88"></a>
<a id="agroup__mcumgr__callback__api__img__mgmt_html_gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7"></a>
<a id="agroup__mcumgr__callback__api__img__mgmt_html_gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0"></a>
<a id="agroup__mcumgr__callback__api__img__mgmt_html_gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3"></a>
<a id="agroup__mcumgr__callback__api__img__mgmt_html_gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8"></a>
<a id="agroup__mcumgr__callback__api__img__mgmt_html_gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf"></a>
<a id="agroup__mcumgr__callback__api_html_gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructflash__area_html"></a>
<a id="astructimg__mgmt__image__confirmed_html"></a>
<a id="astructimg__mgmt__image__confirmed_html_a2cd305cbe1446fd26b97a25cacad0e5c"></a>
<a id="astructimg__mgmt__slot__info__image_html"></a>
<a id="astructimg__mgmt__slot__info__image_html_a2456d0f9cc29a5cb56d5e8fb45f149d7"></a>
<a id="astructimg__mgmt__slot__info__image_html_af19f99ee4e86a586177b014c364be94c"></a>
<a id="astructimg__mgmt__slot__info__slot_html"></a>
<a id="astructimg__mgmt__slot__info__slot_html_a316d66379317f7a13be21cd242cdddda"></a>
<a id="astructimg__mgmt__slot__info__slot_html_a4fbfd8fb9135cc3fa2cc65f71ca2199e"></a>
<a id="astructimg__mgmt__slot__info__slot_html_a53ef029264545a7caca289d61e7983a1"></a>
<a id="astructimg__mgmt__slot__info__slot_html_ab809efd89381e763f73a45b5c5e807d7"></a>
<a id="astructimg__mgmt__state__slot__encode_html"></a>
<a id="astructimg__mgmt__state__slot__encode_html_a5c2486f75743eb44133819b5f35d97cb"></a>
<a id="astructimg__mgmt__state__slot__encode_html_a62157cb9a3288806f4ec11e5c2ef20ac"></a>
<a id="astructimg__mgmt__state__slot__encode_html_a9279018722b20380da6e48046787d220"></a>
<a id="astructimg__mgmt__state__slot__encode_html_a9e53ce9a8a88b76e035b02cd2289fb07"></a>
<a id="astructimg__mgmt__state__slot__encode_html_aa4bf77897519408786c1ee28029342dd"></a>
<a id="astructimg__mgmt__state__slot__encode_html_ad669d8c2062f90d008f715dee206c687"></a>
<a id="astructimg__mgmt__upload__action_html"></a>
<a id="astructimg__mgmt__upload__check_html"></a>
<a id="astructimg__mgmt__upload__check_html_ab8a3e937302b1def309508eace664793"></a>
<a id="astructimg__mgmt__upload__check_html_aea96e650e2701e6064638dd4c384df55"></a>
<a id="astructimg__mgmt__upload__req_html"></a>

```c
/*
 * Copyright (c) 2022 Laird Connectivity
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_CALLBACKS_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_CALLBACKS_H_


#include <stdbool.h>
#include <stdint.h>
#include <zcbor_common.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Dummy definitions, include zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h for actual definitions */
struct img_mgmt_upload_action;
struct img_mgmt_upload_req;


enum img_mgmt_group_events {
        MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK                  = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 0),

        MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED                = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 1),

        MGMT_EVT_OP_IMG_MGMT_DFU_STARTED                = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 2),

        MGMT_EVT_OP_IMG_MGMT_DFU_PENDING                = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 3),

        MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED              = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 4),

        MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK_WRITE_COMPLETE   = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 5),

        MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE           = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 6),

        MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE            = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 7),

        MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_SLOT             = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_IMG, 8),

        MGMT_EVT_OP_IMG_MGMT_ALL                        = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_IMG),
};

struct img_mgmt_upload_check {
        struct img_mgmt_upload_action *action;

        struct img_mgmt_upload_req *req;
};

struct img_mgmt_image_confirmed {
        const uint8_t image;
};

struct img_mgmt_state_slot_encode {
        bool *ok;
        zcbor_state_t *zse;
        const uint32_t slot;
        const char *version;
        const uint8_t *hash;
        const int flags;
};

struct img_mgmt_slot_info_image {
        const uint8_t image;

        zcbor_state_t *zse;
};

struct img_mgmt_slot_info_slot {
        const uint8_t image;

        const uint8_t slot;

        const struct flash_area *fa;

        zcbor_state_t *zse;
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_CALLBACKS_H_ */
```

## 91.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Laird Connectivity。

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

虚拟定义（Dummy definitions）；实际定义请包含 `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h`。

### 注释 3：原第 165 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_CALLBACKS_H_`。

## 91.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [img_mgmt_upload_action](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md)
- [img_mgmt_upload_req](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md)
- [img_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#ga3fa2c42bade08cca1122e32f6315f107)
- [MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c)
- [MGMT_EVT_GRP_IMG](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1)
- [MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8)
- [MGMT_EVT_OP_IMG_MGMT_DFU_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf)
- [MGMT_EVT_OP_IMG_MGMT_DFU_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4)
- [MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb)
- [MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK_WRITE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a4204cb29c7308f103644162839abcb88)
- [MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7)
- [MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3)
- [MGMT_EVT_OP_IMG_MGMT_SLOT_INFO_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0)
- [MGMT_EVT_OP_IMG_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a0ba2354ef268ed22c51df7e5708c50bf)
- [img_mgmt_upload_check](../system_service_model_reference/P050_img_mgmt_upload_check_结构体.md)
- [action](../system_service_model_reference/P050_img_mgmt_upload_check_结构体.md#aea96e650e2701e6064638dd4c384df55)
- [req](../system_service_model_reference/P050_img_mgmt_upload_check_结构体.md#ab8a3e937302b1def309508eace664793)
- [img_mgmt_image_confirmed](../system_service_model_reference/P044_img_mgmt_image_confirmed_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [image](../system_service_model_reference/P044_img_mgmt_image_confirmed_结构体.md#a2cd305cbe1446fd26b97a25cacad0e5c)
- [img_mgmt_state_slot_encode](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md)
- [ok](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#a9279018722b20380da6e48046787d220)
- [zse](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#a62157cb9a3288806f4ec11e5c2ef20ac)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [slot](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#ad669d8c2062f90d008f715dee206c687)
- [version](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#aa4bf77897519408786c1ee28029342dd)
- [hash](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#a5c2486f75743eb44133819b5f35d97cb)
- [flags](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#a9e53ce9a8a88b76e035b02cd2289fb07)
- [img_mgmt_slot_info_image](../system_service_model_reference/P045_img_mgmt_slot_info_image_结构体.md)
- [image](../system_service_model_reference/P045_img_mgmt_slot_info_image_结构体.md#a2456d0f9cc29a5cb56d5e8fb45f149d7)
- [zse](../system_service_model_reference/P045_img_mgmt_slot_info_image_结构体.md#af19f99ee4e86a586177b014c364be94c)
- [img_mgmt_slot_info_slot](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md)
- [image](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md#ab809efd89381e763f73a45b5c5e807d7)
- [slot](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md#a4fbfd8fb9135cc3fa2cc65f71ca2199e)
- [flash_area](../system_service_model_reference/P027_flash_area_结构体.md)
- [fa](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md#a53ef029264545a7caca289d61e7983a1)
- [zse](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md#a316d66379317f7a13be21cd242cdddda)
- [img_mgmt_image_confirmed::image](../system_service_model_reference/P044_img_mgmt_image_confirmed_结构体.md#a2cd305cbe1446fd26b97a25cacad0e5c)
- [img_mgmt_slot_info_image::image](../system_service_model_reference/P045_img_mgmt_slot_info_image_结构体.md#a2456d0f9cc29a5cb56d5e8fb45f149d7)
- [img_mgmt_slot_info_image::zse](../system_service_model_reference/P045_img_mgmt_slot_info_image_结构体.md#af19f99ee4e86a586177b014c364be94c)
- [img_mgmt_slot_info_slot::zse](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md#a316d66379317f7a13be21cd242cdddda)
- [img_mgmt_slot_info_slot::slot](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md#a4fbfd8fb9135cc3fa2cc65f71ca2199e)
- [img_mgmt_slot_info_slot::fa](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md#a53ef029264545a7caca289d61e7983a1)
- [img_mgmt_slot_info_slot::image](../system_service_model_reference/P046_img_mgmt_slot_info_slot_结构体.md#ab809efd89381e763f73a45b5c5e807d7)
- [img_mgmt_state_slot_encode::hash](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#a5c2486f75743eb44133819b5f35d97cb)
- [img_mgmt_state_slot_encode::zse](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#a62157cb9a3288806f4ec11e5c2ef20ac)
- [img_mgmt_state_slot_encode::ok](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#a9279018722b20380da6e48046787d220)
- [img_mgmt_state_slot_encode::flags](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#a9e53ce9a8a88b76e035b02cd2289fb07)
- [img_mgmt_state_slot_encode::version](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#aa4bf77897519408786c1ee28029342dd)
- [img_mgmt_state_slot_encode::slot](../system_service_model_reference/P048_img_mgmt_state_slot_encode_结构体.md#ad669d8c2062f90d008f715dee206c687)
- [img_mgmt_upload_check::req](../system_service_model_reference/P050_img_mgmt_upload_check_结构体.md#ab8a3e937302b1def309508eace664793)
- [img_mgmt_upload_check::action](../system_service_model_reference/P050_img_mgmt_upload_check_结构体.md#aea96e650e2701e6064638dd4c384df55)

---

[上一章](P090_ifx_clock_source_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P092_imx_spc.h_源码浏览.md)
