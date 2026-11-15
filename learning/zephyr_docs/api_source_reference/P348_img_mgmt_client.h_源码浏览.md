---
id: learning.zephyr-docs.api-source-reference.page-348
title: img_mgmt_client.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第348章\_img\_mgmt\_client.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h.html)。

## 348.1\_原始可见代码（Source Code）

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
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="agroup__mcumgr__img__mgmt__client_html_ga1c21618818b5b058e28bdd32360e3838"></a>
<a id="agroup__mcumgr__img__mgmt__client_html_ga27ca742a8fc5fc3a96510d73fa85a7a3"></a>
<a id="agroup__mcumgr__img__mgmt__client_html_ga55fddd1f53765ce25e4285e45714ebc1"></a>
<a id="agroup__mcumgr__img__mgmt__client_html_ga96a605c7a4f46851eced1d538f3134b6"></a>
<a id="agroup__mcumgr__img__mgmt__client_html_ga99dccccacad33c5e7f91043b483a3884"></a>
<a id="agroup__mcumgr__img__mgmt__client_html_gab98286b3baac7330c7f42539d38663cd"></a>
<a id="agroup__mcumgr__img__mgmt__client_html_gad1937b33597ddd012fc7d1fd04cf17f8"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga57a5c429be5a3860981007e9728db181"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga70168b0d707c15658fd09b02c361a64c"></a>
<a id="agroup__mcumgr__mgmt__api_html_gac5d8757a7ca945c77f405764b85ad5c5"></a>
<a id="aimg__mgmt_8h_html"></a>
<a id="ainttypes_8h_html"></a>
<a id="amgmt__defines_8h_html"></a>
<a id="asmp__client_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructimg__gr__upload_html"></a>
<a id="astructimg__gr__upload_html_a093b1897e492545ab5b92d91bde727fb"></a>
<a id="astructimg__gr__upload_html_a457e54010e9980b96bc970f6d43bd127"></a>
<a id="astructimg__gr__upload_html_a71736f17ef73d50d0e61049d356e2ce2"></a>
<a id="astructimg__gr__upload_html_a773dfcf2f4ceccb771020f29f2e44c92"></a>
<a id="astructimg__gr__upload_html_ae5245e6622c991cbd207b3f69f7548f3"></a>
<a id="astructimg__gr__upload_html_af71ec58c3a2c39e1549c41f7692b1319"></a>
<a id="astructimg__mgmt__client_html"></a>
<a id="astructimg__mgmt__client_html_a2a2097f05111d6242d623a68959ecca9"></a>
<a id="astructimg__mgmt__client_html_a36abd266bbd1ea35849423708f9e816d"></a>
<a id="astructimg__mgmt__client_html_a4fb8d168a6faf48c32903b71fc8c8097"></a>
<a id="astructimg__mgmt__client_html_a654c94fafac9cd72465a413de8266005"></a>
<a id="astructimg__mgmt__client_html_a77559218adc5f7873366c56f9a02750e"></a>
<a id="astructmcumgr__image__data_html"></a>
<a id="astructmcumgr__image__data_html_a24f83149d88a3709b4f58bc72ee932be"></a>
<a id="astructmcumgr__image__data_html_a713cff86339e08b2f74b564dca4c521e"></a>
<a id="astructmcumgr__image__data_html_a78c32a6ee0d614bd47352e1d65c773a6"></a>
<a id="astructmcumgr__image__data_html_aa75e38d37c9b12a2ccf32af6a47df814"></a>
<a id="astructmcumgr__image__data_html_ab8e2cb7030c755bfae8fda97972df4c2"></a>
<a id="astructmcumgr__image__data_html_ac394e1e5a0e0425b27926a3405d8bb2d"></a>
<a id="astructmcumgr__image__list__flags_html"></a>
<a id="astructmcumgr__image__list__flags_html_a744597f98d3092de161512d0817bb1a2"></a>
<a id="astructmcumgr__image__list__flags_html_acb12d5ae0c75e9dac48874e542784bd3"></a>
<a id="astructmcumgr__image__list__flags_html_ad3ff9c0acbcf2ebbb5f6820b38705bff"></a>
<a id="astructmcumgr__image__list__flags_html_ade2a01aeeede96070bcdf33ce2d949fb"></a>
<a id="astructmcumgr__image__list__flags_html_af7c7b565ef02ea95c7486949a29164c1"></a>
<a id="astructmcumgr__image__state_html"></a>
<a id="astructmcumgr__image__state_html_a4ec39c59f3cfe789dabf7fc361ff86ac"></a>
<a id="astructmcumgr__image__state_html_af7bd52b3a18ad190e0159c5e928b857e"></a>
<a id="astructmcumgr__image__state_html_afd36103c373d709733ee928326c50343"></a>
<a id="astructmcumgr__image__upload_html"></a>
<a id="astructmcumgr__image__upload_html_a5522d2958df295c72fd00212155c7eee"></a>
<a id="astructmcumgr__image__upload_html_ade29d2b559d9709b7372874e993e267c"></a>
<a id="astructsmp__client__object_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_CLIENT_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_CLIENT_H_

#include <inttypes.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h>
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>


#ifdef __cplusplus
extern "C" {
#endif

#define IMG_MGMT_CLIENT_HASH_MAX_LEN 64

struct mcumgr_image_list_flags {
        bool bootable: 1;
        bool pending: 1;
        bool confirmed: 1;
        bool active: 1;
        bool permanent: 1;
};

struct mcumgr_image_data {
        uint32_t slot_num;
        uint32_t img_num;
        char hash[IMG_MGMT_CLIENT_HASH_MAX_LEN];
        size_t hash_len;
        char version[IMG_MGMT_VER_MAX_STR_LEN + 1];
        struct mcumgr_image_list_flags flags;
};

struct mcumgr_image_state {
        enum mcumgr_err_t status;
        int image_list_length;
        struct mcumgr_image_data *image_list;
};

struct mcumgr_image_upload {
        enum mcumgr_err_t status;
        size_t image_upload_offset;
};

struct img_gr_upload {
        char sha256[IMG_MGMT_DATA_SHA_LEN];
        bool hash_initialized;
        size_t image_size;
        size_t offset;
        size_t upload_header_size;
        uint32_t image_num;
};

struct img_mgmt_client {
        struct smp_client_object *smp_client;
        struct img_gr_upload upload;
        int image_list_length;
        struct mcumgr_image_data *image_list;
        int status;
};

void img_mgmt_client_init(struct img_mgmt_client *client, struct smp_client_object *smp_client,
                          int image_list_size, struct mcumgr_image_data *image_list);

int img_mgmt_client_upload_init(struct img_mgmt_client *client, size_t image_size,
                                uint32_t image_num, const char *image_hash);

int img_mgmt_client_upload(struct img_mgmt_client *client, const uint8_t *data, size_t length,
                           struct mcumgr_image_upload *res_buf);

int img_mgmt_client_state_write(struct img_mgmt_client *client, const char *hash, size_t hash_len,
                                bool confirm, struct mcumgr_image_state *res_buf);

int img_mgmt_client_state_read(struct img_mgmt_client *client, struct mcumgr_image_state *res_buf);


int img_mgmt_client_erase(struct img_mgmt_client *client, uint32_t slot);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_CLIENT_H_ */
```

## 348.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 243 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_CLIENT_H_`。

## 348.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h.html)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h.html)
- [zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h.html)
- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt_8h.html)
- [zephyr/mgmt/mcumgr/smp/smp_client.h](https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h.html)
- [mcumgr_image_list_flags](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md)
- [bootable](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md#acb12d5ae0c75e9dac48874e542784bd3)
- [pending](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md#a744597f98d3092de161512d0817bb1a2)
- [confirmed](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md#ad3ff9c0acbcf2ebbb5f6820b38705bff)
- [active](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md#ade2a01aeeede96070bcdf33ce2d949fb)
- [permanent](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md#af7c7b565ef02ea95c7486949a29164c1)
- [mcumgr_image_data](../system_service_model_reference/P061_mcumgr_image_data_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [slot_num](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#a713cff86339e08b2f74b564dca4c521e)
- [img_num](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#ac394e1e5a0e0425b27926a3405d8bb2d)
- [hash](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#a78c32a6ee0d614bd47352e1d65c773a6)
- [IMG_MGMT_CLIENT_HASH_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga96a605c7a4f46851eced1d538f3134b6)
- [hash_len](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#ab8e2cb7030c755bfae8fda97972df4c2)
- [version](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#aa75e38d37c9b12a2ccf32af6a47df814)
- [IMG_MGMT_VER_MAX_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga57a5c429be5a3860981007e9728db181)
- [flags](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#a24f83149d88a3709b4f58bc72ee932be)
- [mcumgr_image_state](../system_service_model_reference/P063_mcumgr_image_state_结构体.md)
- [mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)
- [status](../system_service_model_reference/P063_mcumgr_image_state_结构体.md#a4ec39c59f3cfe789dabf7fc361ff86ac)
- [image_list_length](../system_service_model_reference/P063_mcumgr_image_state_结构体.md#afd36103c373d709733ee928326c50343)
- [image_list](../system_service_model_reference/P063_mcumgr_image_state_结构体.md#af7bd52b3a18ad190e0159c5e928b857e)
- [mcumgr_image_upload](../system_service_model_reference/P064_mcumgr_image_upload_结构体.md)
- [status](../system_service_model_reference/P064_mcumgr_image_upload_结构体.md#a5522d2958df295c72fd00212155c7eee)
- [image_upload_offset](../system_service_model_reference/P064_mcumgr_image_upload_结构体.md#ade29d2b559d9709b7372874e993e267c)
- [img_gr_upload](../system_service_model_reference/P042_img_gr_upload_结构体.md)
- [sha256](../system_service_model_reference/P042_img_gr_upload_结构体.md#a773dfcf2f4ceccb771020f29f2e44c92)
- [IMG_MGMT_DATA_SHA_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga70168b0d707c15658fd09b02c361a64c)
- [hash_initialized](../system_service_model_reference/P042_img_gr_upload_结构体.md#af71ec58c3a2c39e1549c41f7692b1319)
- [image_size](../system_service_model_reference/P042_img_gr_upload_结构体.md#a093b1897e492545ab5b92d91bde727fb)
- [offset](../system_service_model_reference/P042_img_gr_upload_结构体.md#a71736f17ef73d50d0e61049d356e2ce2)
- [upload_header_size](../system_service_model_reference/P042_img_gr_upload_结构体.md#ae5245e6622c991cbd207b3f69f7548f3)
- [image_num](../system_service_model_reference/P042_img_gr_upload_结构体.md#a457e54010e9980b96bc970f6d43bd127)
- [img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [smp_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md#a36abd266bbd1ea35849423708f9e816d)
- [upload](../system_service_model_reference/P043_img_mgmt_client_结构体.md#a77559218adc5f7873366c56f9a02750e)
- [image_list_length](../system_service_model_reference/P043_img_mgmt_client_结构体.md#a2a2097f05111d6242d623a68959ecca9)
- [image_list](../system_service_model_reference/P043_img_mgmt_client_结构体.md#a654c94fafac9cd72465a413de8266005)
- [status](../system_service_model_reference/P043_img_mgmt_client_结构体.md#a4fb8d168a6faf48c32903b71fc8c8097)
- [img_mgmt_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga1c21618818b5b058e28bdd32360e3838)
- [img_mgmt_client_upload_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga99dccccacad33c5e7f91043b483a3884)
- [img_mgmt_client_upload](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga55fddd1f53765ce25e4285e45714ebc1)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [img_mgmt_client_state_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#gab98286b3baac7330c7f42539d38663cd)
- [img_mgmt_client_state_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#gad1937b33597ddd012fc7d1fd04cf17f8)
- [img_mgmt_client_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga27ca742a8fc5fc3a96510d73fa85a7a3)
- [img_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt_8h.html)
- [mgmt_defines.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h.html)
- [smp_client.h](https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h.html)
- [img_gr_upload::image_size](../system_service_model_reference/P042_img_gr_upload_结构体.md#a093b1897e492545ab5b92d91bde727fb)
- [img_gr_upload::image_num](../system_service_model_reference/P042_img_gr_upload_结构体.md#a457e54010e9980b96bc970f6d43bd127)
- [img_gr_upload::offset](../system_service_model_reference/P042_img_gr_upload_结构体.md#a71736f17ef73d50d0e61049d356e2ce2)
- [img_gr_upload::sha256](../system_service_model_reference/P042_img_gr_upload_结构体.md#a773dfcf2f4ceccb771020f29f2e44c92)
- [img_gr_upload::upload_header_size](../system_service_model_reference/P042_img_gr_upload_结构体.md#ae5245e6622c991cbd207b3f69f7548f3)
- [img_gr_upload::hash_initialized](../system_service_model_reference/P042_img_gr_upload_结构体.md#af71ec58c3a2c39e1549c41f7692b1319)
- [img_mgmt_client::image_list_length](../system_service_model_reference/P043_img_mgmt_client_结构体.md#a2a2097f05111d6242d623a68959ecca9)
- [img_mgmt_client::smp_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md#a36abd266bbd1ea35849423708f9e816d)
- [img_mgmt_client::status](../system_service_model_reference/P043_img_mgmt_client_结构体.md#a4fb8d168a6faf48c32903b71fc8c8097)
- [img_mgmt_client::image_list](../system_service_model_reference/P043_img_mgmt_client_结构体.md#a654c94fafac9cd72465a413de8266005)
- [img_mgmt_client::upload](../system_service_model_reference/P043_img_mgmt_client_结构体.md#a77559218adc5f7873366c56f9a02750e)
- [mcumgr_image_data::flags](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#a24f83149d88a3709b4f58bc72ee932be)
- [mcumgr_image_data::slot_num](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#a713cff86339e08b2f74b564dca4c521e)
- [mcumgr_image_data::hash](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#a78c32a6ee0d614bd47352e1d65c773a6)
- [mcumgr_image_data::version](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#aa75e38d37c9b12a2ccf32af6a47df814)
- [mcumgr_image_data::hash_len](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#ab8e2cb7030c755bfae8fda97972df4c2)
- [mcumgr_image_data::img_num](../system_service_model_reference/P061_mcumgr_image_data_结构体.md#ac394e1e5a0e0425b27926a3405d8bb2d)
- [mcumgr_image_list_flags::pending](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md#a744597f98d3092de161512d0817bb1a2)
- [mcumgr_image_list_flags::bootable](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md#acb12d5ae0c75e9dac48874e542784bd3)
- [mcumgr_image_list_flags::confirmed](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md#ad3ff9c0acbcf2ebbb5f6820b38705bff)
- [mcumgr_image_list_flags::active](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md#ade2a01aeeede96070bcdf33ce2d949fb)
- [mcumgr_image_list_flags::permanent](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md#af7c7b565ef02ea95c7486949a29164c1)
- [mcumgr_image_state::status](../system_service_model_reference/P063_mcumgr_image_state_结构体.md#a4ec39c59f3cfe789dabf7fc361ff86ac)
- [mcumgr_image_state::image_list](../system_service_model_reference/P063_mcumgr_image_state_结构体.md#af7bd52b3a18ad190e0159c5e928b857e)
- [mcumgr_image_state::image_list_length](../system_service_model_reference/P063_mcumgr_image_state_结构体.md#afd36103c373d709733ee928326c50343)
- [mcumgr_image_upload::status](../system_service_model_reference/P064_mcumgr_image_upload_结构体.md#a5522d2958df295c72fd00212155c7eee)
- [mcumgr_image_upload::image_upload_offset](../system_service_model_reference/P064_mcumgr_image_upload_结构体.md#ade29d2b559d9709b7372874e993e267c)

---

[上一章](P347_iis3dwb.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P349_imx943_clock.h_源码浏览.md)
