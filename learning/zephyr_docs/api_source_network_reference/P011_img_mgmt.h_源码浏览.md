---
id: learning.zephyr-docs.api-source-network-reference.page-11
title: img_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_img\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt_8h.html)。

## 11.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="foldopen00193"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="foldopen00203"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="foldopen00213"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="foldopen00226"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00237"></a>
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
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga0d6bb8877516ca486c318fa12c129138"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga1d239fef127e65b11b71360eadfa1ede"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga3e496199d0ea4aa1b3f51e59bb7473f0"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga42475389b4e31d5f35ea58873527e948"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga5199849b6d8847c6a1260254940db95b"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga60ae88823a561160b1ddc406382e4ac3"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga669286d96816e0e99792f407752c81a5"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga6c9124cc59c99769908cdf83f58e1bf1"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga70168b0d707c15658fd09b02c361a64c"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga7e529fa76ddb3d3bf4a527cb11fa9c89"></a>
<a id="agroup__mcumgr__img__mgmt_html_ga90de2da23bcd650ca59219fdfd4f55a1"></a>
<a id="agroup__mcumgr__img__mgmt_html_gab35c8adf2e5e2c941ecbaf3c03101e55"></a>
<a id="agroup__mcumgr__img__mgmt_html_gab6a92433b859fce18b58e6110fa5f489"></a>
<a id="agroup__mcumgr__img__mgmt_html_gad3dce7b70ce3338588003a021eec1ab6"></a>
<a id="agroup__mcumgr__img__mgmt_html_gae9cfa02e5f171d68287cdb0d7d4c0610"></a>
<a id="agroup__mcumgr__img__mgmt_html_gaed0b945d2f83daf63d850b232a2cfea8"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga1d239fef127e65b11b71360eadfa1edea7cf567b16af18752316fde6444e23a21"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga1d239fef127e65b11b71360eadfa1edeab106874625a50d626e55130e91d37bf2"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga1d239fef127e65b11b71360eadfa1edeaff49286e379bd39781a563c1e52c6c8c"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a0d16138a65766047e4917022068832fa"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a227b2b3be93cf963ce034b9cb817d0ca"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a27502b76efcc09ef01cfbe777a9e8086"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a3220405113525f3d5af068b8bf2a80f6"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a360155fc7e541080a7b80bee6ec9dbb6"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a37ad5efbaacdcb708a65674a4dc83d85"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a3a8d3005c72273ee065c34396d3fd2f7"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a4725027793b17187474089fde35730cb"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a4b2994e51eadae6cb43c3683d6e223b6"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a5606b72a7bf61832b92c77e729e02093"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a598c03b99a2be60cf4847fa2f32c5d10"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a5b4301665ef0c9818fcd3174908e5063"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a5d89dde479611276e6956706ee357c6e"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a6c1c103d76e1f16fda77525ba136e9b2"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a7c0f0cda8165d0acf5fc2a072a5c5cc5"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a7db18fe6cb5913fec882dc515d8bb7a0"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a8253896c206d8f3ba486466555662071"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a857b6ecc22e5f54834638aa604cce6bf"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a869d0aa27c38187fdb73d36397dcef3c"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a8a94dfe1aca340c4337fe92554ede4b0"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a8f1bd00b3e00f070b07269fdddd2c8fe"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a92ab3773cdbd00b42fb59865e958069b"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a967c4f0b3d33d925e28f076c8cc3ed5c"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a9a09d73602a77e112a95fa977e9b0355"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5a9e4c9f1a79f645130ef9a8aa09b8b544"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5ab195578794ddc6cffa5e056ee34350a8"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5ab258cd53a5cc13e2376662690703f54b"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5ab75ac303b054a02e99a0ed9726c988de"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5aced7bb74d51b7dd7ff922cf555722276"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5acfdb28d59643e70db86abfa72c2833b7"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5adf54010236b4e6bb4669cdeeb4a6979f"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5ae2413b0ade3185b91ae085af397adabf"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5ae710879342357f27c9705989f572b82f"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5af1eac867913981a4d8f1f2d64108706e"></a>
<a id="agroup__mcumgr__img__mgmt_html_gga669286d96816e0e99792f407752c81a5af55239776b4b5a5eead0440fb3b884b3"></a>
<a id="ainttypes_8h_html"></a>
<a id="amgmt_2mcumgr_2smp_2smp_8h_html"></a>
<a id="amgmt_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructimg__mgmt__state_html"></a>
<a id="astructimg__mgmt__state_html_a1c357f22c420a310c234c96a9bc7143f"></a>
<a id="astructimg__mgmt__state_html_a40619a325f216e1c27e45fd19ccd6db3"></a>
<a id="astructimg__mgmt__state_html_a4da29c0c4b525463cce3f0d3ffbed633"></a>
<a id="astructimg__mgmt__state_html_a6a3cbeb401f057fb1510e1acbdf7d71c"></a>
<a id="astructimg__mgmt__state_html_a965b6426ea57beac531af3bb9d2f0d0e"></a>
<a id="astructimg__mgmt__upload__action_html"></a>
<a id="astructimg__mgmt__upload__action_html_a4b1d3625ade4e4392094ace41ec4aa01"></a>
<a id="astructimg__mgmt__upload__action_html_a6c9248e3c21325ed99ff8cf765f3ac82"></a>
<a id="astructimg__mgmt__upload__action_html_a7661db4343ebf6f7d040e3e87d3611aa"></a>
<a id="astructimg__mgmt__upload__action_html_aac493000e6989735531492f15edb6108"></a>
<a id="astructimg__mgmt__upload__action_html_abe9c3503c6d58cf3b7ad637cd4fec852"></a>
<a id="astructimg__mgmt__upload__req_html"></a>
<a id="astructimg__mgmt__upload__req_html_a25cdcd55c77cde43af1a9ec9b414cecb"></a>
<a id="astructimg__mgmt__upload__req_html_a439504202c945a1dd74b75c35a1a8017"></a>
<a id="astructimg__mgmt__upload__req_html_ad61f8c732f0b2150bd252e47eb539bb1"></a>
<a id="astructimg__mgmt__upload__req_html_ade363ed09134ff2f3a1fcb20a6305cfa"></a>
<a id="astructimg__mgmt__upload__req_html_ae30c1fc9257f04c88216ba92f8453dac"></a>
<a id="astructimg__mgmt__upload__req_html_ae9c67210faa7dfc55a73f66defc00195"></a>
<a id="astructsmp__streamer_html"></a>

```c
/*
 * Copyright (c) 2018-2021 mcumgr authors
 * Copyright (c) 2022-2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_H_


#include <inttypes.h>
#include <bootutil/image.h>
#include <zcbor_common.h>

#ifdef CONFIG_MCUMGR_GRP_IMG_VERBOSE_ERR
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
#include <zephyr/mgmt/mcumgr/smp/smp.h>
#endif


#ifdef __cplusplus
extern "C" {
#endif

#define IMG_MGMT_DATA_SHA_LEN   32 /* SHA256 */

#define IMG_MGMT_STATE_F_PENDING        0x01
#define IMG_MGMT_STATE_F_CONFIRMED      0x02
#define IMG_MGMT_STATE_F_ACTIVE         0x04
#define IMG_MGMT_STATE_F_PERMANENT      0x08

/* 255.255.65535.4294967295\0 */
#define IMG_MGMT_VER_MAX_STR_LEN        (sizeof("255.255.65535.4294967295"))

#define IMG_MGMT_SWAP_TYPE_NONE    0
#define IMG_MGMT_SWAP_TYPE_TEST    1
#define IMG_MGMT_SWAP_TYPE_PERM    2
#define IMG_MGMT_SWAP_TYPE_REVERT  3
#define IMG_MGMT_SWAP_TYPE_UNKNOWN 255

#define IMG_MGMT_ID_STATE     0
#define IMG_MGMT_ID_UPLOAD    1
#define IMG_MGMT_ID_FILE      2
#define IMG_MGMT_ID_CORELIST  3
#define IMG_MGMT_ID_CORELOAD  4
#define IMG_MGMT_ID_ERASE     5
#define IMG_MGMT_ID_SLOT_INFO 6

enum img_mgmt_err_code_t {
        IMG_MGMT_ERR_OK = 0,

        IMG_MGMT_ERR_UNKNOWN,

        IMG_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL,

        IMG_MGMT_ERR_NO_IMAGE,

        IMG_MGMT_ERR_NO_TLVS,

        IMG_MGMT_ERR_INVALID_TLV,

        IMG_MGMT_ERR_TLV_MULTIPLE_HASHES_FOUND,

        IMG_MGMT_ERR_TLV_INVALID_SIZE,

        IMG_MGMT_ERR_HASH_NOT_FOUND,

        IMG_MGMT_ERR_NO_FREE_SLOT,

        IMG_MGMT_ERR_FLASH_OPEN_FAILED,

        IMG_MGMT_ERR_FLASH_READ_FAILED,

        IMG_MGMT_ERR_FLASH_WRITE_FAILED,

        IMG_MGMT_ERR_FLASH_ERASE_FAILED,

        IMG_MGMT_ERR_INVALID_SLOT,

        IMG_MGMT_ERR_NO_FREE_MEMORY,

        IMG_MGMT_ERR_FLASH_CONTEXT_ALREADY_SET,

        IMG_MGMT_ERR_FLASH_CONTEXT_NOT_SET,

        IMG_MGMT_ERR_FLASH_AREA_DEVICE_NULL,

        IMG_MGMT_ERR_INVALID_PAGE_OFFSET,

        IMG_MGMT_ERR_INVALID_OFFSET,

        IMG_MGMT_ERR_INVALID_LENGTH,

        IMG_MGMT_ERR_INVALID_IMAGE_HEADER,

        IMG_MGMT_ERR_INVALID_IMAGE_HEADER_MAGIC,

        IMG_MGMT_ERR_INVALID_HASH,

        IMG_MGMT_ERR_INVALID_FLASH_ADDRESS,

        IMG_MGMT_ERR_VERSION_GET_FAILED,

        IMG_MGMT_ERR_CURRENT_VERSION_IS_NEWER,

        IMG_MGMT_ERR_IMAGE_ALREADY_PENDING,

        IMG_MGMT_ERR_INVALID_IMAGE_VECTOR_TABLE,

        IMG_MGMT_ERR_INVALID_IMAGE_TOO_LARGE,

        IMG_MGMT_ERR_INVALID_IMAGE_DATA_OVERRUN,

        IMG_MGMT_ERR_IMAGE_CONFIRMATION_DENIED,

        IMG_MGMT_ERR_IMAGE_SETTING_TEST_TO_ACTIVE_DENIED,

        IMG_MGMT_ERR_ACTIVE_SLOT_NOT_KNOWN,
};

enum img_mgmt_id_upload_t {
        IMG_MGMT_ID_UPLOAD_STATUS_START         = 0,
        IMG_MGMT_ID_UPLOAD_STATUS_ONGOING,
        IMG_MGMT_ID_UPLOAD_STATUS_COMPLETE,
};

extern int boot_current_slot;
extern struct img_mgmt_state g_img_mgmt_state;

struct img_mgmt_upload_req {
        uint32_t image; /* 0 by default */
        size_t off;     /* SIZE_MAX if unspecified */
        size_t size;    /* SIZE_MAX if unspecified */
        struct zcbor_string img_data;
        struct zcbor_string data_sha;
        bool upgrade;                   /* Only allow greater version numbers. */
};

struct img_mgmt_state {
        int area_id;
        size_t off;
        size_t size;
        uint8_t data_sha_len;
        uint8_t data_sha[IMG_MGMT_DATA_SHA_LEN];
};

struct img_mgmt_upload_action {
        unsigned long long size;
        int write_bytes;
        int area_id;
        bool proceed;
        bool erase;
#ifdef CONFIG_MCUMGR_GRP_IMG_VERBOSE_ERR
        const char *rc_rsn;
#endif
};

/*
 * @brief Read info of an image at the specified slot number
 *
 * @param image_slot    image slot number
 * @param ver           output buffer for image version
 * @param hash          output buffer for image hash
 * @param flags         output buffer for image flags
 *
 * @return 0 on success, non-zero on failure.
 */
int img_mgmt_read_info(int image_slot, struct image_version *ver, uint8_t *hash, uint32_t *flags);

int img_mgmt_my_version(struct image_version *ver);

int img_mgmt_ver_str(const struct image_version *ver, char *dst);

int img_mgmt_active_slot(int image);

int img_mgmt_active_image(void);

int img_mgmt_slot_in_use(int slot);

int img_mgmt_state_any_pending(void);

uint8_t img_mgmt_state_flags(int query_slot);

int img_mgmt_state_set_pending(int slot, int permanent);

int img_mgmt_state_confirm(void);

int img_mgmt_vercmp(const struct image_version *a, const struct image_version *b);

#if defined(CONFIG_MCUMGR_GRP_IMG_MUTEX)
/*
 * @brief       Will reset the image management state back to default (no ongoing upload),
 *              requires that CONFIG_MCUMGR_GRP_IMG_MUTEX be enabled to allow for mutex
 *              locking of the image management state object.
 */
void img_mgmt_reset_upload(void);
#endif

#ifdef CONFIG_MCUMGR_GRP_IMG_VERBOSE_ERR
#define IMG_MGMT_UPLOAD_ACTION_SET_RC_RSN(action, rsn) ((action)->rc_rsn = (rsn))
#define IMG_MGMT_UPLOAD_ACTION_RC_RSN(action) ((action)->rc_rsn)
int img_mgmt_error_rsp(struct smp_streamer *ctxt, int rc, const char *rsn);
extern const char *img_mgmt_err_str_app_reject;
extern const char *img_mgmt_err_str_hdr_malformed;
extern const char *img_mgmt_err_str_magic_mismatch;
extern const char *img_mgmt_err_str_no_slot;
extern const char *img_mgmt_err_str_flash_open_failed;
extern const char *img_mgmt_err_str_flash_erase_failed;
extern const char *img_mgmt_err_str_flash_write_failed;
extern const char *img_mgmt_err_str_downgrade;
extern const char *img_mgmt_err_str_image_bad_flash_addr;
extern const char *img_mgmt_err_str_image_too_large;
extern const char *img_mgmt_err_str_data_overrun;
#else
#define IMG_MGMT_UPLOAD_ACTION_SET_RC_RSN(action, rsn)
#define IMG_MGMT_UPLOAD_ACTION_RC_RSN(action) NULL
#endif


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_H_ */
```

## 11.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018-2021 mcumgr authors。

版权（Copyright）：© 2022-2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 37 行

安全哈希算法 256（SHA256）。

### 注释 3：原第 53 行

版本字符串容量示例（Version String Capacity Example）：`255.255.65535.4294967295\0`，包含结尾的空字符（NUL）。

### 注释 4：原第 204 行

默认值（Default）为 0。

### 注释 5：原第 205 行

未指定时为 `SIZE_MAX`。

### 注释 6：原第 206 行

未指定时为 `SIZE_MAX`。

### 注释 7：原第 209 行

仅允许更大的版本号（Greater Version Numbers）。

### 注释 8：原第 243 行

读取指定槽位编号（Slot Number）处的镜像信息（Image Info）。

- 参数 `image_slot`：镜像槽位编号（Image Slot Number）。
- 参数 `ver`：镜像版本输出缓冲区（Image Version Output Buffer）。
- 参数 `hash`：镜像哈希输出缓冲区（Image Hash Output Buffer）。
- 参数 `flags`：镜像标志输出缓冲区（Image Flags Output Buffer）。

返回（`@return`）：成功时为 0，失败时为非零值。

### 注释 9：原第 369 行

将镜像管理状态（Image Management State）重置为默认状态，即没有正在进行的上传（Ongoing Upload）。需要启用 `CONFIG_MCUMGR_GRP_IMG_MUTEX`，以允许对镜像管理状态对象执行互斥锁定（Mutex Locking）。

### 注释 10：原第 405 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_IMG_MGMT_IMG_MGMT_H_`。

## 11.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt_8h.html)
- [inttypes.h](../api_file_reference/P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md)
- [zephyr/mgmt/mcumgr/mgmt/mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h.html)
- [zephyr/mgmt/mcumgr/smp/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html)
- [img_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga669286d96816e0e99792f407752c81a5)
- [IMG_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a7db18fe6cb5913fec882dc515d8bb7a0)
- [IMG_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a8f1bd00b3e00f070b07269fdddd2c8fe)
- [IMG_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a5b4301665ef0c9818fcd3174908e5063)
- [IMG_MGMT_ERR_NO_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a360155fc7e541080a7b80bee6ec9dbb6)
- [IMG_MGMT_ERR_NO_TLVS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a598c03b99a2be60cf4847fa2f32c5d10)
- [IMG_MGMT_ERR_INVALID_TLV](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a4725027793b17187474089fde35730cb)
- [IMG_MGMT_ERR_TLV_MULTIPLE_HASHES_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5aced7bb74d51b7dd7ff922cf555722276)
- [IMG_MGMT_ERR_TLV_INVALID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a967c4f0b3d33d925e28f076c8cc3ed5c)
- [IMG_MGMT_ERR_HASH_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a5d89dde479611276e6956706ee357c6e)
- [IMG_MGMT_ERR_NO_FREE_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a0d16138a65766047e4917022068832fa)
- [IMG_MGMT_ERR_FLASH_OPEN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a8253896c206d8f3ba486466555662071)
- [IMG_MGMT_ERR_FLASH_READ_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a9a09d73602a77e112a95fa977e9b0355)
- [IMG_MGMT_ERR_FLASH_WRITE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5adf54010236b4e6bb4669cdeeb4a6979f)
- [IMG_MGMT_ERR_FLASH_ERASE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a869d0aa27c38187fdb73d36397dcef3c)
- [IMG_MGMT_ERR_INVALID_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a7c0f0cda8165d0acf5fc2a072a5c5cc5)
- [IMG_MGMT_ERR_NO_FREE_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ab75ac303b054a02e99a0ed9726c988de)
- [IMG_MGMT_ERR_FLASH_CONTEXT_ALREADY_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5af1eac867913981a4d8f1f2d64108706e)
- [IMG_MGMT_ERR_FLASH_CONTEXT_NOT_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a9e4c9f1a79f645130ef9a8aa09b8b544)
- [IMG_MGMT_ERR_FLASH_AREA_DEVICE_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a6c1c103d76e1f16fda77525ba136e9b2)
- [IMG_MGMT_ERR_INVALID_PAGE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a857b6ecc22e5f54834638aa604cce6bf)
- [IMG_MGMT_ERR_INVALID_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a8a94dfe1aca340c4337fe92554ede4b0)
- [IMG_MGMT_ERR_INVALID_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a227b2b3be93cf963ce034b9cb817d0ca)
- [IMG_MGMT_ERR_INVALID_IMAGE_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5acfdb28d59643e70db86abfa72c2833b7)
- [IMG_MGMT_ERR_INVALID_IMAGE_HEADER_MAGIC](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a5606b72a7bf61832b92c77e729e02093)
- [IMG_MGMT_ERR_INVALID_HASH](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a4b2994e51eadae6cb43c3683d6e223b6)
- [IMG_MGMT_ERR_INVALID_FLASH_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a27502b76efcc09ef01cfbe777a9e8086)
- [IMG_MGMT_ERR_VERSION_GET_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ae710879342357f27c9705989f572b82f)
- [IMG_MGMT_ERR_CURRENT_VERSION_IS_NEWER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a37ad5efbaacdcb708a65674a4dc83d85)
- [IMG_MGMT_ERR_IMAGE_ALREADY_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5af55239776b4b5a5eead0440fb3b884b3)
- [IMG_MGMT_ERR_INVALID_IMAGE_VECTOR_TABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a3a8d3005c72273ee065c34396d3fd2f7)
- [IMG_MGMT_ERR_INVALID_IMAGE_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ab258cd53a5cc13e2376662690703f54b)
- [IMG_MGMT_ERR_INVALID_IMAGE_DATA_OVERRUN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a92ab3773cdbd00b42fb59865e958069b)
- [IMG_MGMT_ERR_IMAGE_CONFIRMATION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ae2413b0ade3185b91ae085af397adabf)
- [IMG_MGMT_ERR_IMAGE_SETTING_TEST_TO_ACTIVE_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ab195578794ddc6cffa5e056ee34350a8)
- [IMG_MGMT_ERR_ACTIVE_SLOT_NOT_KNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a3220405113525f3d5af068b8bf2a80f6)
- [img_mgmt_id_upload_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga1d239fef127e65b11b71360eadfa1ede)
- [IMG_MGMT_ID_UPLOAD_STATUS_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga1d239fef127e65b11b71360eadfa1edeaff49286e379bd39781a563c1e52c6c8c)
- [IMG_MGMT_ID_UPLOAD_STATUS_ONGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga1d239fef127e65b11b71360eadfa1edea7cf567b16af18752316fde6444e23a21)
- [IMG_MGMT_ID_UPLOAD_STATUS_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga1d239fef127e65b11b71360eadfa1edeab106874625a50d626e55130e91d37bf2)
- [boot_current_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga0d6bb8877516ca486c318fa12c129138)
- [img_mgmt_state](../system_service_model_reference/P047_img_mgmt_state_结构体.md)
- [g_img_mgmt_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gad3dce7b70ce3338588003a021eec1ab6)
- [img_mgmt_upload_req](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [image](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#ad61f8c732f0b2150bd252e47eb539bb1)
- [off](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#ae9c67210faa7dfc55a73f66defc00195)
- [size](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#a25cdcd55c77cde43af1a9ec9b414cecb)
- [img_data](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#ade363ed09134ff2f3a1fcb20a6305cfa)
- [data_sha](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#ae30c1fc9257f04c88216ba92f8453dac)
- [upgrade](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#a439504202c945a1dd74b75c35a1a8017)
- [area_id](../system_service_model_reference/P047_img_mgmt_state_结构体.md#a4da29c0c4b525463cce3f0d3ffbed633)
- [off](../system_service_model_reference/P047_img_mgmt_state_结构体.md#a965b6426ea57beac531af3bb9d2f0d0e)
- [size](../system_service_model_reference/P047_img_mgmt_state_结构体.md#a40619a325f216e1c27e45fd19ccd6db3)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data_sha_len](../system_service_model_reference/P047_img_mgmt_state_结构体.md#a6a3cbeb401f057fb1510e1acbdf7d71c)
- [data_sha](../system_service_model_reference/P047_img_mgmt_state_结构体.md#a1c357f22c420a310c234c96a9bc7143f)
- [IMG_MGMT_DATA_SHA_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga70168b0d707c15658fd09b02c361a64c)
- [img_mgmt_upload_action](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md)
- [size](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md#a4b1d3625ade4e4392094ace41ec4aa01)
- [write_bytes](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md#aac493000e6989735531492f15edb6108)
- [area_id](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md#a6c9248e3c21325ed99ff8cf765f3ac82)
- [proceed](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md#a7661db4343ebf6f7d040e3e87d3611aa)
- [erase](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md#abe9c3503c6d58cf3b7ad637cd4fec852)
- [img_mgmt_read_info](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga60ae88823a561160b1ddc406382e4ac3)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [img_mgmt_my_version](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gae9cfa02e5f171d68287cdb0d7d4c0610)
- [img_mgmt_ver_str](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga5199849b6d8847c6a1260254940db95b)
- [img_mgmt_active_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gab35c8adf2e5e2c941ecbaf3c03101e55)
- [img_mgmt_active_image](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gab6a92433b859fce18b58e6110fa5f489)
- [img_mgmt_slot_in_use](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga90de2da23bcd650ca59219fdfd4f55a1)
- [img_mgmt_state_any_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga3e496199d0ea4aa1b3f51e59bb7473f0)
- [img_mgmt_state_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga42475389b4e31d5f35ea58873527e948)
- [img_mgmt_state_set_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga7e529fa76ddb3d3bf4a527cb11fa9c89)
- [img_mgmt_state_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gaed0b945d2f83daf63d850b232a2cfea8)
- [img_mgmt_vercmp](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga6c9124cc59c99769908cdf83f58e1bf1)
- [smp_streamer](../system_service_model_reference/P080_smp_streamer_结构体.md)
- [smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html)
- [mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h.html)
- [img_mgmt_state::data_sha](../system_service_model_reference/P047_img_mgmt_state_结构体.md#a1c357f22c420a310c234c96a9bc7143f)
- [img_mgmt_state::size](../system_service_model_reference/P047_img_mgmt_state_结构体.md#a40619a325f216e1c27e45fd19ccd6db3)
- [img_mgmt_state::area_id](../system_service_model_reference/P047_img_mgmt_state_结构体.md#a4da29c0c4b525463cce3f0d3ffbed633)
- [img_mgmt_state::data_sha_len](../system_service_model_reference/P047_img_mgmt_state_结构体.md#a6a3cbeb401f057fb1510e1acbdf7d71c)
- [img_mgmt_state::off](../system_service_model_reference/P047_img_mgmt_state_结构体.md#a965b6426ea57beac531af3bb9d2f0d0e)
- [img_mgmt_upload_action::size](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md#a4b1d3625ade4e4392094ace41ec4aa01)
- [img_mgmt_upload_action::area_id](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md#a6c9248e3c21325ed99ff8cf765f3ac82)
- [img_mgmt_upload_action::proceed](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md#a7661db4343ebf6f7d040e3e87d3611aa)
- [img_mgmt_upload_action::write_bytes](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md#aac493000e6989735531492f15edb6108)
- [img_mgmt_upload_action::erase](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md#abe9c3503c6d58cf3b7ad637cd4fec852)
- [img_mgmt_upload_req::size](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#a25cdcd55c77cde43af1a9ec9b414cecb)
- [img_mgmt_upload_req::upgrade](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#a439504202c945a1dd74b75c35a1a8017)
- [img_mgmt_upload_req::image](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#ad61f8c732f0b2150bd252e47eb539bb1)
- [img_mgmt_upload_req::img_data](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#ade363ed09134ff2f3a1fcb20a6305cfa)
- [img_mgmt_upload_req::data_sha](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#ae30c1fc9257f04c88216ba92f8453dac)
- [img_mgmt_upload_req::off](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md#ae9c67210faa7dfc55a73f66defc00195)

---

[上一章](P010_ieee802154_radio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P012_lldp.h_源码浏览.md)
