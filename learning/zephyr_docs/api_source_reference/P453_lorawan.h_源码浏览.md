---
id: learning.zephyr-docs.api-source-reference.page-453
title: lorawan.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第453章\_lorawan.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h.html)。

## 453.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="foldopen00158"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="foldopen00178"></a>
<a id="l00178"></a>
<a id="l00186"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__lorawan__api_html_ga0635d19612db9009775eae8e527d4897"></a>
<a id="agroup__lorawan__api_html_ga12afde687fb1081bc669f844e6ab7c92"></a>
<a id="agroup__lorawan__api_html_ga14f9cb6a11c585f9ac4e9986735a82c3"></a>
<a id="agroup__lorawan__api_html_ga17a7a2e1dbfa19b9f7e18a81be5514dd"></a>
<a id="agroup__lorawan__api_html_ga1f87b0b04bb5e75623d63d82f6069207"></a>
<a id="agroup__lorawan__api_html_ga23758c3225e3ebf62bbe91b7589b67d7"></a>
<a id="agroup__lorawan__api_html_ga243c3200693ae9c81dea238068afc7dd"></a>
<a id="agroup__lorawan__api_html_ga276e66fb8ce88f853d1987686e31fc86"></a>
<a id="agroup__lorawan__api_html_ga2bf50442214ecdc717f1a24dc058a338"></a>
<a id="agroup__lorawan__api_html_ga432929bd5911e04e57ef178b65e1beaa"></a>
<a id="agroup__lorawan__api_html_ga505e8d27bc7bc029feb93bbe4982d329"></a>
<a id="agroup__lorawan__api_html_ga55b5a10df7235d51a65b40032e5f6907"></a>
<a id="agroup__lorawan__api_html_ga5b2c7543c45801c9d0d7f46546771f17"></a>
<a id="agroup__lorawan__api_html_ga5d78efba3f8e62ccd6317aed8af4bc54"></a>
<a id="agroup__lorawan__api_html_ga640d93930e09327ee87563597f919725"></a>
<a id="agroup__lorawan__api_html_ga6d1b45c5543473ff4fbcef473a8e0e35"></a>
<a id="agroup__lorawan__api_html_ga7b620841f521b9addc8d1ee823ee45fd"></a>
<a id="agroup__lorawan__api_html_ga87a8d911f1c825bcf8c77ada568f3ed4"></a>
<a id="agroup__lorawan__api_html_ga88b65799c3f1d98fbce80927218c0837"></a>
<a id="agroup__lorawan__api_html_ga88c22a7e83437688039c05f9c7c1e7d4"></a>
<a id="agroup__lorawan__api_html_ga94e3c282537618efae65e8ada1f88e81"></a>
<a id="agroup__lorawan__api_html_ga9771704a8bcab778dd30653a0fbdeb2f"></a>
<a id="agroup__lorawan__api_html_ga980f1650e9cceba19da453d4937273cb"></a>
<a id="agroup__lorawan__api_html_gaaa70ba5aa545b59233bc906948a4030d"></a>
<a id="agroup__lorawan__api_html_gaaf60e8b09d6f8d3a89aa2089c137fd3f"></a>
<a id="agroup__lorawan__api_html_gab28a9f22482069b2246892e4ee31660d"></a>
<a id="agroup__lorawan__api_html_gab62274848abe7cd0f23fadefd185028b"></a>
<a id="agroup__lorawan__api_html_gab91f31477cd44e10692ca9d56d137ae2"></a>
<a id="agroup__lorawan__api_html_gab9768bad8d0c18410f6b8e946e89cbbe"></a>
<a id="agroup__lorawan__api_html_gacb8efaa0761f8761146a0e913dcb627d"></a>
<a id="agroup__lorawan__api_html_gade697fcc14a384420afc8817f72af410"></a>
<a id="agroup__lorawan__api_html_gaed19bb9c528f8f21104201fd0816e3a9"></a>
<a id="agroup__lorawan__api_html_gaf9fad3b2bb93ab43751098f4b8dd31f9"></a>
<a id="agroup__lorawan__api_html_gga0635d19612db9009775eae8e527d4897a054ebab376354c8a9e6a5f4e9f6f78ee"></a>
<a id="agroup__lorawan__api_html_gga0635d19612db9009775eae8e527d4897a1bc4cacfd02a630226f629ed61f4e1ca"></a>
<a id="agroup__lorawan__api_html_gga0635d19612db9009775eae8e527d4897a2bdaecd6f1f853cd370ba89b465a9ee1"></a>
<a id="agroup__lorawan__api_html_gga0635d19612db9009775eae8e527d4897a3b7968012bf2c8fa7adef454fc33124a"></a>
<a id="agroup__lorawan__api_html_gga0635d19612db9009775eae8e527d4897a3bc215c41b7fb5652c6729756b8f979a"></a>
<a id="agroup__lorawan__api_html_gga0635d19612db9009775eae8e527d4897a577c304c4c1998916203e9ec7ae6e1be"></a>
<a id="agroup__lorawan__api_html_gga0635d19612db9009775eae8e527d4897a7443e6adbaaf4f7cb2037d8f3e42d86a"></a>
<a id="agroup__lorawan__api_html_gga0635d19612db9009775eae8e527d4897a8f2f25b3ab1167f69aa594a034b27180"></a>
<a id="agroup__lorawan__api_html_gga0635d19612db9009775eae8e527d4897a9564d246e39448f478412861a3a87b7e"></a>
<a id="agroup__lorawan__api_html_gga0635d19612db9009775eae8e527d4897aaa05e08a24aded2ada511fd2d1f4cebd"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a080b31031f5a2b54d84ed49b133b0a86"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a08f879f1054ca54e488180b07d7ff952"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a0a18193e15d268d262d58897d39993b3"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a0df057cf1505ba94876deaeddd515548"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a18bfd63ae262f992d9d12f8d56cc217e"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a1ad3be15c2e60d0bb2f3c12faf279efa"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a2a631e746ffc5c4378e39b7a90dd44e2"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a4738baf87e0cb2e64d9c525e40dd6e0a"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a4ac565dbaae0c6ad4e62dc34ca0c013a"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a4b60b8eb52c07b40cbaaf94a4c56e1f6"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a6f6cd4ecd247f67cad08ede84649a939"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86a941f8a603aeb54560be7125a55c74159"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86aac8afba95d7187f0829aae7abda894d5"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86acc624ccf8a9585889c3685217f56099f"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86ade4655b32ca976c317fa9f44ac8b148a"></a>
<a id="agroup__lorawan__api_html_gga276e66fb8ce88f853d1987686e31fc86afbc8d04236410a6107cccfd71ba4bace"></a>
<a id="agroup__lorawan__api_html_gga2bf50442214ecdc717f1a24dc058a338a13bb2a28232081844e36308977ec6701"></a>
<a id="agroup__lorawan__api_html_gga2bf50442214ecdc717f1a24dc058a338a5f262e334bc46278bec491cd022b612a"></a>
<a id="agroup__lorawan__api_html_gga5d78efba3f8e62ccd6317aed8af4bc54a40ee76ac8d0b40d06903fc06a7ef1989"></a>
<a id="agroup__lorawan__api_html_gga5d78efba3f8e62ccd6317aed8af4bc54a9855d8332363a554db9dde446cc409b7"></a>
<a id="agroup__lorawan__api_html_gga88b65799c3f1d98fbce80927218c0837a538e56348e6d5b506e661e3af18aee6c"></a>
<a id="agroup__lorawan__api_html_gga88b65799c3f1d98fbce80927218c0837a79a9c205ac583051b2e072389491c7cb"></a>
<a id="agroup__lorawan__api_html_gga88b65799c3f1d98fbce80927218c0837ad158a1985688bbe54b20a8a808774547"></a>
<a id="agroup__lorawan__api_html_ggab28a9f22482069b2246892e4ee31660da01aee480c4308ac7abb6bf909478cce2"></a>
<a id="agroup__lorawan__api_html_ggab28a9f22482069b2246892e4ee31660dad272f787e193c2397e1b670ced4ba1b8"></a>
<a id="agroup__lorawan__api_html_ggacb8efaa0761f8761146a0e913dcb627da2744fe63701f5a5f23706b6f37672c70"></a>
<a id="agroup__lorawan__api_html_ggacb8efaa0761f8761146a0e913dcb627da404530e5008260260131de051283f7ba"></a>
<a id="agroup__lorawan__api_html_ggacb8efaa0761f8761146a0e913dcb627da52d67181588c94d2a423040b4b5a1de4"></a>
<a id="agroup__lorawan__api_html_ggacb8efaa0761f8761146a0e913dcb627da6a1ba05859d575a28095437436c8e6a6"></a>
<a id="agroup__lorawan__api_html_ggacb8efaa0761f8761146a0e913dcb627da70e25dd006efc115617631f64cc34c88"></a>
<a id="agroup__lorawan__api_html_ggacb8efaa0761f8761146a0e913dcb627da9113b34d94da40149442f432fd97e86c"></a>
<a id="agroup__lorawan__api_html_ggacb8efaa0761f8761146a0e913dcb627dabcb9529d8f449bcb85a893fdd20f9180"></a>
<a id="agroup__lorawan__api_html_ggacb8efaa0761f8761146a0e913dcb627dad30a636d45def6889e2b5cbf60f28c0e"></a>
<a id="agroup__lorawan__api_html_ggacb8efaa0761f8761146a0e913dcb627dadb106a189c4c647e5e3af89cc753e0d8"></a>
<a id="agroup__lorawan__api_html_ggacb8efaa0761f8761146a0e913dcb627dafae64ea9dd2c2ee7e897fc0f94484da5"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructlorawan__downlink__cb_html"></a>
<a id="astructlorawan__downlink__cb_html_a0479e13faf06b99cf9023ebed8022131"></a>
<a id="astructlorawan__downlink__cb_html_ad54df4a4ab38003d59f82b19fb16f5fd"></a>
<a id="astructlorawan__downlink__cb_html_ae4f5e74bd927c650eba0d9b2f3978d8f"></a>
<a id="astructlorawan__join__abp_html"></a>
<a id="astructlorawan__join__abp_html_a7a409fa2f3761c49085818768a62d216"></a>
<a id="astructlorawan__join__abp_html_a8019bead1dfdda7a0b05f35f128edca5"></a>
<a id="astructlorawan__join__abp_html_aa389fec6799b12e750d57aaf0b34e6b0"></a>
<a id="astructlorawan__join__abp_html_ad132826d04b66f145865f9a30ff03fff"></a>
<a id="astructlorawan__join__config_html"></a>
<a id="astructlorawan__join__config_html_a0b44703df9ebe466ccf1d7744138daee"></a>
<a id="astructlorawan__join__config_html_a7e2db9310308b59f652d72a3d7b3f7ff"></a>
<a id="astructlorawan__join__config_html_a9dbe39641f878e4c997a16711fdb5585"></a>
<a id="astructlorawan__join__config_html_af5c973ed774255858b2219f737a3fe0a"></a>
<a id="astructlorawan__join__otaa_html"></a>
<a id="astructlorawan__join__otaa_html_a28dd704e28d0bed909c3e85e516c85ea"></a>
<a id="astructlorawan__join__otaa_html_aacf3523f615f08fac1993e0bdc354072"></a>
<a id="astructlorawan__join__otaa_html_ab83167af58040f95072a95fbaed1ff5d"></a>
<a id="astructlorawan__join__otaa_html_af1a96b4fa17ee70ee0e8ba078b02a6bc"></a>

```c
/*
 * Copyright (c) 2020 Manivannan Sadhasivam <mani@kernel.org>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_LORAWAN_LORAWAN_H_
#define ZEPHYR_INCLUDE_LORAWAN_LORAWAN_H_


#include <zephyr/device.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

enum lorawan_class {
        LORAWAN_CLASS_A = 0x00,
        LORAWAN_CLASS_B = 0x01,
        LORAWAN_CLASS_C = 0x02,
};

enum lorawan_act_type {
        LORAWAN_ACT_OTAA = 0,
        LORAWAN_ACT_ABP,
};

enum lorawan_channels_mask_size {
        LORAWAN_CHANNELS_MASK_SIZE_AS923 = 1,
        LORAWAN_CHANNELS_MASK_SIZE_AU915 = 6,
        LORAWAN_CHANNELS_MASK_SIZE_CN470 = 6,
        LORAWAN_CHANNELS_MASK_SIZE_CN779 = 1,
        LORAWAN_CHANNELS_MASK_SIZE_EU433 = 1,
        LORAWAN_CHANNELS_MASK_SIZE_EU868 = 1,
        LORAWAN_CHANNELS_MASK_SIZE_KR920 = 1,
        LORAWAN_CHANNELS_MASK_SIZE_IN865 = 1,
        LORAWAN_CHANNELS_MASK_SIZE_US915 = 6,
        LORAWAN_CHANNELS_MASK_SIZE_RU864 = 1,
};

enum lorawan_datarate {
        LORAWAN_DR_0 = 0,
        LORAWAN_DR_1,
        LORAWAN_DR_2,
        LORAWAN_DR_3,
        LORAWAN_DR_4,
        LORAWAN_DR_5,
        LORAWAN_DR_6,
        LORAWAN_DR_7,
        LORAWAN_DR_8,
        LORAWAN_DR_9,
        LORAWAN_DR_10,
        LORAWAN_DR_11,
        LORAWAN_DR_12,
        LORAWAN_DR_13,
        LORAWAN_DR_14,
        LORAWAN_DR_15,
};

enum lorawan_region {
        LORAWAN_REGION_AS923,
        LORAWAN_REGION_AU915,
        LORAWAN_REGION_CN470,
        LORAWAN_REGION_CN779,
        LORAWAN_REGION_EU433,
        LORAWAN_REGION_EU868,
        LORAWAN_REGION_KR920,
        LORAWAN_REGION_IN865,
        LORAWAN_REGION_US915,
        LORAWAN_REGION_RU864,
};

enum lorawan_message_type {
        LORAWAN_MSG_UNCONFIRMED = 0,
        LORAWAN_MSG_CONFIRMED,
};

enum lorawan_dl_flags {
        LORAWAN_DATA_PENDING = BIT(0),
        LORAWAN_TIME_UPDATED = BIT(1),
};

struct lorawan_join_otaa {
        uint8_t *join_eui;
        uint8_t *nwk_key;
        uint8_t *app_key;
        uint16_t dev_nonce;
};

struct lorawan_join_abp {
        uint32_t dev_addr;
        uint8_t *app_skey;
        uint8_t *nwk_skey;
        uint8_t *app_eui;
};

struct lorawan_join_config {
        union {
                struct lorawan_join_otaa otaa;
                struct lorawan_join_abp abp;
        };

        uint8_t *dev_eui;

        enum lorawan_act_type mode;
};

#define LW_RECV_PORT_ANY UINT16_MAX

struct lorawan_downlink_cb {
        uint16_t port;
        void (*cb)(uint8_t port, uint8_t flags, int16_t rssi, int8_t snr, uint8_t len,
                   const uint8_t *data);
        sys_snode_t node;
};

typedef uint8_t (*lorawan_battery_level_cb_t)(void);

typedef void (*lorawan_dr_changed_cb_t)(enum lorawan_datarate dr);

typedef void (*lorawan_link_check_ans_cb_t)(uint8_t demod_margin, uint8_t nb_gateways);

typedef int (*transport_descriptor_cb)(uint32_t descriptor);

void lorawan_register_battery_level_callback(lorawan_battery_level_cb_t cb);

void lorawan_register_downlink_callback(struct lorawan_downlink_cb *cb);

void lorawan_register_dr_changed_callback(lorawan_dr_changed_cb_t cb);

void lorawan_register_link_check_ans_callback(lorawan_link_check_ans_cb_t cb);

int lorawan_join(const struct lorawan_join_config *config);

int lorawan_start(void);

int lorawan_send(uint8_t port, uint8_t *data, uint8_t len, enum lorawan_message_type type);

int lorawan_set_class(enum lorawan_class dev_class);

int lorawan_set_conf_msg_tries(uint8_t tries);

void lorawan_enable_adr(bool enable);

int lorawan_set_channels_mask(uint16_t *channels_mask, size_t channels_mask_size);

int lorawan_set_datarate(enum lorawan_datarate dr);

enum lorawan_datarate lorawan_get_min_datarate(void);

void lorawan_get_payload_sizes(uint8_t *max_next_payload_size,
                               uint8_t *max_payload_size);

int lorawan_set_region(enum lorawan_region region);

int lorawan_request_device_time(bool force_request);

int lorawan_device_time_get(uint32_t *gps_time);

int lorawan_request_link_check(bool force_request);

int lorawan_clock_sync_run(void);

int lorawan_clock_sync_get(uint32_t *gps_time);

void lorawan_frag_transport_register_descriptor_callback(transport_descriptor_cb cb);

int lorawan_frag_transport_run(void (*transport_finished_cb)(void));

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_LORAWAN_LORAWAN_H_ */
```

## 453.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Manivannan Sadhasivam <mani@kernel.org>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 550 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_LORAWAN_LORAWAN_H_`。

## 453.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [lorawan_class](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga88b65799c3f1d98fbce80927218c0837)
- [LORAWAN_CLASS_A](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga88b65799c3f1d98fbce80927218c0837a538e56348e6d5b506e661e3af18aee6c)
- [LORAWAN_CLASS_B](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga88b65799c3f1d98fbce80927218c0837a79a9c205ac583051b2e072389491c7cb)
- [LORAWAN_CLASS_C](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga88b65799c3f1d98fbce80927218c0837ad158a1985688bbe54b20a8a808774547)
- [lorawan_act_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga2bf50442214ecdc717f1a24dc058a338)
- [LORAWAN_ACT_OTAA](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga2bf50442214ecdc717f1a24dc058a338a5f262e334bc46278bec491cd022b612a)
- [LORAWAN_ACT_ABP](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga2bf50442214ecdc717f1a24dc058a338a13bb2a28232081844e36308977ec6701)
- [lorawan_channels_mask_size](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga0635d19612db9009775eae8e527d4897)
- [LORAWAN_CHANNELS_MASK_SIZE_AS923](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a577c304c4c1998916203e9ec7ae6e1be)
- [LORAWAN_CHANNELS_MASK_SIZE_AU915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a1bc4cacfd02a630226f629ed61f4e1ca)
- [LORAWAN_CHANNELS_MASK_SIZE_CN470](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a2bdaecd6f1f853cd370ba89b465a9ee1)
- [LORAWAN_CHANNELS_MASK_SIZE_CN779](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a8f2f25b3ab1167f69aa594a034b27180)
- [LORAWAN_CHANNELS_MASK_SIZE_EU433](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a3b7968012bf2c8fa7adef454fc33124a)
- [LORAWAN_CHANNELS_MASK_SIZE_EU868](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a3bc215c41b7fb5652c6729756b8f979a)
- [LORAWAN_CHANNELS_MASK_SIZE_KR920](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a7443e6adbaaf4f7cb2037d8f3e42d86a)
- [LORAWAN_CHANNELS_MASK_SIZE_IN865](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a9564d246e39448f478412861a3a87b7e)
- [LORAWAN_CHANNELS_MASK_SIZE_US915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a054ebab376354c8a9e6a5f4e9f6f78ee)
- [LORAWAN_CHANNELS_MASK_SIZE_RU864](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897aaa05e08a24aded2ada511fd2d1f4cebd)
- [lorawan_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga276e66fb8ce88f853d1987686e31fc86)
- [LORAWAN_DR_0](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a4b60b8eb52c07b40cbaaf94a4c56e1f6)
- [LORAWAN_DR_1](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86ade4655b32ca976c317fa9f44ac8b148a)
- [LORAWAN_DR_2](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a941f8a603aeb54560be7125a55c74159)
- [LORAWAN_DR_3](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a4ac565dbaae0c6ad4e62dc34ca0c013a)
- [LORAWAN_DR_4](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a6f6cd4ecd247f67cad08ede84649a939)
- [LORAWAN_DR_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a08f879f1054ca54e488180b07d7ff952)
- [LORAWAN_DR_6](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86acc624ccf8a9585889c3685217f56099f)
- [LORAWAN_DR_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86aac8afba95d7187f0829aae7abda894d5)
- [LORAWAN_DR_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a080b31031f5a2b54d84ed49b133b0a86)
- [LORAWAN_DR_9](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86afbc8d04236410a6107cccfd71ba4bace)
- [LORAWAN_DR_10](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a0a18193e15d268d262d58897d39993b3)
- [LORAWAN_DR_11](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a2a631e746ffc5c4378e39b7a90dd44e2)
- [LORAWAN_DR_12](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a0df057cf1505ba94876deaeddd515548)
- [LORAWAN_DR_13](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a18bfd63ae262f992d9d12f8d56cc217e)
- [LORAWAN_DR_14](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a1ad3be15c2e60d0bb2f3c12faf279efa)
- [LORAWAN_DR_15](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a4738baf87e0cb2e64d9c525e40dd6e0a)
- [lorawan_region](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gacb8efaa0761f8761146a0e913dcb627d)
- [LORAWAN_REGION_AS923](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da6a1ba05859d575a28095437436c8e6a6)
- [LORAWAN_REGION_AU915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da2744fe63701f5a5f23706b6f37672c70)
- [LORAWAN_REGION_CN470](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da52d67181588c94d2a423040b4b5a1de4)
- [LORAWAN_REGION_CN779](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dadb106a189c4c647e5e3af89cc753e0d8)
- [LORAWAN_REGION_EU433](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dabcb9529d8f449bcb85a893fdd20f9180)
- [LORAWAN_REGION_EU868](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da404530e5008260260131de051283f7ba)
- [LORAWAN_REGION_KR920](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dafae64ea9dd2c2ee7e897fc0f94484da5)
- [LORAWAN_REGION_IN865](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da9113b34d94da40149442f432fd97e86c)
- [LORAWAN_REGION_US915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da70e25dd006efc115617631f64cc34c88)
- [LORAWAN_REGION_RU864](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dad30a636d45def6889e2b5cbf60f28c0e)
- [lorawan_message_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga5d78efba3f8e62ccd6317aed8af4bc54)
- [LORAWAN_MSG_UNCONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga5d78efba3f8e62ccd6317aed8af4bc54a9855d8332363a554db9dde446cc409b7)
- [LORAWAN_MSG_CONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga5d78efba3f8e62ccd6317aed8af4bc54a40ee76ac8d0b40d06903fc06a7ef1989)
- [lorawan_dl_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab28a9f22482069b2246892e4ee31660d)
- [LORAWAN_DATA_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggab28a9f22482069b2246892e4ee31660da01aee480c4308ac7abb6bf909478cce2)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [LORAWAN_TIME_UPDATED](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggab28a9f22482069b2246892e4ee31660dad272f787e193c2397e1b670ced4ba1b8)
- [lorawan_join_otaa](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [join_eui](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md#aacf3523f615f08fac1993e0bdc354072)
- [nwk_key](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md#af1a96b4fa17ee70ee0e8ba078b02a6bc)
- [app_key](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md#a28dd704e28d0bed909c3e85e516c85ea)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [dev_nonce](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md#ab83167af58040f95072a95fbaed1ff5d)
- [lorawan_join_abp](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [dev_addr](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md#ad132826d04b66f145865f9a30ff03fff)
- [app_skey](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md#a8019bead1dfdda7a0b05f35f128edca5)
- [nwk_skey](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md#aa389fec6799b12e750d57aaf0b34e6b0)
- [app_eui](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md#a7a409fa2f3761c49085818768a62d216)
- [lorawan_join_config](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md)
- [otaa](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md#a7e2db9310308b59f652d72a3d7b3f7ff)
- [abp](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md#a0b44703df9ebe466ccf1d7744138daee)
- [dev_eui](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md#af5c973ed774255858b2219f737a3fe0a)
- [mode](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md#a9dbe39641f878e4c997a16711fdb5585)
- [lorawan_downlink_cb](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md)
- [port](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md#a0479e13faf06b99cf9023ebed8022131)
- [cb](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md#ae4f5e74bd927c650eba0d9b2f3978d8f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md#ad54df4a4ab38003d59f82b19fb16f5fd)
- [lorawan_battery_level_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga17a7a2e1dbfa19b9f7e18a81be5514dd)
- [lorawan_dr_changed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga87a8d911f1c825bcf8c77ada568f3ed4)
- [lorawan_link_check_ans_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaf9fad3b2bb93ab43751098f4b8dd31f9)
- [transport_descriptor_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gade697fcc14a384420afc8817f72af410)
- [lorawan_register_battery_level_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga9771704a8bcab778dd30653a0fbdeb2f)
- [lorawan_register_downlink_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab91f31477cd44e10692ca9d56d137ae2)
- [lorawan_register_dr_changed_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga505e8d27bc7bc029feb93bbe4982d329)
- [lorawan_register_link_check_ans_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga7b620841f521b9addc8d1ee823ee45fd)
- [lorawan_join](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga5b2c7543c45801c9d0d7f46546771f17)
- [lorawan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga640d93930e09327ee87563597f919725)
- [lorawan_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga23758c3225e3ebf62bbe91b7589b67d7)
- [lorawan_set_class](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab9768bad8d0c18410f6b8e946e89cbbe)
- [lorawan_set_conf_msg_tries](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga14f9cb6a11c585f9ac4e9986735a82c3)
- [lorawan_enable_adr](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga432929bd5911e04e57ef178b65e1beaa)
- [lorawan_set_channels_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga243c3200693ae9c81dea238068afc7dd)
- [lorawan_set_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaaa70ba5aa545b59233bc906948a4030d)
- [lorawan_get_min_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga6d1b45c5543473ff4fbcef473a8e0e35)
- [lorawan_get_payload_sizes](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga94e3c282537618efae65e8ada1f88e81)
- [lorawan_set_region](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaaf60e8b09d6f8d3a89aa2089c137fd3f)
- [lorawan_request_device_time](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga980f1650e9cceba19da453d4937273cb)
- [lorawan_device_time_get](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga88c22a7e83437688039c05f9c7c1e7d4)
- [lorawan_request_link_check](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaed19bb9c528f8f21104201fd0816e3a9)
- [lorawan_clock_sync_run](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga1f87b0b04bb5e75623d63d82f6069207)
- [lorawan_clock_sync_get](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga12afde687fb1081bc669f844e6ab7c92)
- [lorawan_frag_transport_register_descriptor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab62274848abe7cd0f23fadefd185028b)
- [lorawan_frag_transport_run](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga55b5a10df7235d51a65b40032e5f6907)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [lorawan_downlink_cb::port](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md#a0479e13faf06b99cf9023ebed8022131)
- [lorawan_downlink_cb::node](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md#ad54df4a4ab38003d59f82b19fb16f5fd)
- [lorawan_downlink_cb::cb](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md#ae4f5e74bd927c650eba0d9b2f3978d8f)
- [lorawan_join_abp::app_eui](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md#a7a409fa2f3761c49085818768a62d216)
- [lorawan_join_abp::app_skey](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md#a8019bead1dfdda7a0b05f35f128edca5)
- [lorawan_join_abp::nwk_skey](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md#aa389fec6799b12e750d57aaf0b34e6b0)
- [lorawan_join_abp::dev_addr](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md#ad132826d04b66f145865f9a30ff03fff)
- [lorawan_join_config::abp](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md#a0b44703df9ebe466ccf1d7744138daee)
- [lorawan_join_config::otaa](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md#a7e2db9310308b59f652d72a3d7b3f7ff)
- [lorawan_join_config::mode](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md#a9dbe39641f878e4c997a16711fdb5585)
- [lorawan_join_config::dev_eui](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md#af5c973ed774255858b2219f737a3fe0a)
- [lorawan_join_otaa::app_key](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md#a28dd704e28d0bed909c3e85e516c85ea)
- [lorawan_join_otaa::join_eui](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md#aacf3523f615f08fac1993e0bdc354072)
- [lorawan_join_otaa::dev_nonce](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md#ab83167af58040f95072a95fbaed1ff5d)
- [lorawan_join_otaa::nwk_key](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md#af1a96b4fa17ee70ee0e8ba078b02a6bc)

---

[上一章](P452_emul.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P454_lpc11u6x_clock.h_源码浏览.md)
