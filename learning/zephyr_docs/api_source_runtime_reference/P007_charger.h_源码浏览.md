---
id: learning.zephyr-docs.api-source-runtime-reference.page-7
title: charger.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/charger_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_charger.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/charger_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/charger_8h.html)。

## 7.1\_原始可见代码（Source Code）

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
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00045"></a>
<a id="l00048"></a>
<a id="l00051"></a>
<a id="l00054"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00072"></a>
<a id="l00079"></a>
<a id="l00086"></a>
<a id="l00093"></a>
<a id="l00098"></a>
<a id="l00104"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="foldopen00154"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="foldopen00166"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="foldopen00182"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00199"></a>
<a id="l00204"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="foldopen00217"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="foldopen00252"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="foldopen00264"></a>
<a id="l00264"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="foldopen00291"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00315"></a>
<a id="l00317"></a>
<a id="l00319"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00331"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00341"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="foldopen00370"></a>
<a id="l00370"></a>
<a id="l00372"></a>
<a id="l00374"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__charger__interface__backend_html_ga6556781abf0e81eee431c88cb894a8e6"></a>
<a id="agroup__charger__interface__backend_html_gaf035c2972693a8763fd08b7db8c9c0bd"></a>
<a id="agroup__charger__interface__backend_html_gafb7488129e0a6c086d3ff0ffadb6c82b"></a>
<a id="agroup__charger__interface_html_ga0036e3f5924585457a99a2e444ef5aab"></a>
<a id="agroup__charger__interface_html_ga00e5b61d517c93d7d3c863b14b07b738"></a>
<a id="agroup__charger__interface_html_ga2e7d7f15725db4d502bc3f46476a310d"></a>
<a id="agroup__charger__interface_html_ga3b448c73ef8c4844ccbe7adb1f2458fe"></a>
<a id="agroup__charger__interface_html_ga4a3c46bc0916082d15e665f7665c89d7"></a>
<a id="agroup__charger__interface_html_ga4ce808890de2d01cdb75feddbf275635"></a>
<a id="agroup__charger__interface_html_ga6eb3b4cc76e4f1e34732b7853eb860b7"></a>
<a id="agroup__charger__interface_html_ga7666697bde91b66829113efe151d1cb2"></a>
<a id="agroup__charger__interface_html_ga9325615cdd8985cbb3407257afb387a2"></a>
<a id="agroup__charger__interface_html_gaa7a6c34b4871673151671eae1fac84da"></a>
<a id="agroup__charger__interface_html_gaab33241d3b85ab0770be9b1bd17e4412"></a>
<a id="agroup__charger__interface_html_gab29c2fafc53988555d72974199f25475"></a>
<a id="agroup__charger__interface_html_gace1ea9841574d75d314db078df5a0b3a"></a>
<a id="agroup__charger__interface_html_gad95d2b1aaf18ac3a1c536f2d40317c19"></a>
<a id="agroup__charger__interface_html_gaee833a379a8674621d2fdf9b57d1f803"></a>
<a id="agroup__charger__interface_html_gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885"></a>
<a id="agroup__charger__interface_html_gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b"></a>
<a id="agroup__charger__interface_html_gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8"></a>
<a id="agroup__charger__interface_html_gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf"></a>
<a id="agroup__charger__interface_html_gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658"></a>
<a id="agroup__charger__interface_html_gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e"></a>
<a id="agroup__charger__interface_html_gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5"></a>
<a id="agroup__charger__interface_html_gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a0dd5ee0d22cba6440c3f3583582d405b"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a1c8906c0e4e278b84cab7d126cf95526"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a1e60d770a5d8e47118040ace3c6d8ec0"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a389920359b8866af70b164d68820d4b7"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a3d3e3190b016a9c31ed5c82e2ade0b72"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a5b4a6c4f1f6abb7a568c7c42dca696bf"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a703a0e374053a410ec154eac117f9085"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a70f2c71cd9d4e0f88ee36886094540fe"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a73b9f45dd43347016a4dd6e15cd78cf6"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a81a18d7286bfcf729402db6990ddc306"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a9340eb6fb5b80370148a43366b753d9b"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7ace0a0e6cbc0ccaf166ff0df7e1b275c0"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459"></a>
<a id="agroup__charger__interface_html_ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b"></a>
<a id="agroup__charger__interface_html_ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6"></a>
<a id="agroup__charger__interface_html_ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e"></a>
<a id="agroup__charger__interface_html_ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3"></a>
<a id="agroup__charger__interface_html_ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6"></a>
<a id="agroup__charger__interface_html_ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17"></a>
<a id="agroup__charger__interface_html_ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2"></a>
<a id="agroup__charger__interface_html_ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4"></a>
<a id="agroup__charger__interface_html_ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8"></a>
<a id="agroup__charger__interface_html_ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f"></a>
<a id="agroup__charger__interface_html_ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8"></a>
<a id="agroup__charger__interface_html_ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a3ea490c9b3617d4479bd80ef93cd5602"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructcharger__current__notifier_html"></a>
<a id="astructcharger__current__notifier_html_a22c26477263e5abedb200de36a29d9de"></a>
<a id="astructcharger__current__notifier_html_a4998999ef893d18fa64b86ec4fd9ad94"></a>
<a id="astructcharger__current__notifier_html_acb54706bf47f55e197e799393b9eb87e"></a>
<a id="astructcharger__driver__api_html"></a>
<a id="astructcharger__driver__api_html_a41ea553c8bb6a24915d73a00129ee67d"></a>
<a id="astructcharger__driver__api_html_a7a7942d11841d9ec02ff57f46323a3a3"></a>
<a id="astructcharger__driver__api_html_a945bfc62b0572da09480e97a6a819269"></a>
<a id="astructdevice_html"></a>
<a id="aunioncharger__propval_html"></a>
<a id="aunioncharger__propval_html_a0ad956ab4d0b306f94cce2aa81283a35"></a>
<a id="aunioncharger__propval_html_a0e9c59df061dbe7d221244cd48530a10"></a>
<a id="aunioncharger__propval_html_a1619752e64e8f99d1a488d1fa887ee60"></a>
<a id="aunioncharger__propval_html_a24a97e16505fa336bd3a68743d05936b"></a>
<a id="aunioncharger__propval_html_a541d1bf0b3e32d7aaeb6a2f4f443c5dc"></a>
<a id="aunioncharger__propval_html_a733bae9ce0bf7e902f8af307f94a356c"></a>
<a id="aunioncharger__propval_html_a7b7aa29e279028e502d8662c70fc1747"></a>
<a id="aunioncharger__propval_html_a7f4976d72d4a7d48385ceb9f18c510b5"></a>
<a id="aunioncharger__propval_html_a8589124e6152b70b649788a8b94461ab"></a>
<a id="aunioncharger__propval_html_a89d0c93d68650cefe29e891f4db928f4"></a>
<a id="aunioncharger__propval_html_ab0eec508b90d205a1662fd6c69638764"></a>
<a id="aunioncharger__propval_html_ab9f40a6083ff2361ea4d161226cd77ad"></a>
<a id="aunioncharger__propval_html_abd990f67423424da60856f4b6e8824a3"></a>
<a id="aunioncharger__propval_html_ac1a594de2b1c10d28b6a81dd66f1a6ba"></a>
<a id="aunioncharger__propval_html_ad77547e88ec465d2e37526751008f634"></a>
<a id="aunioncharger__propval_html_ae51670de8fa560f0c7610452db029bc2"></a>
<a id="aunioncharger__propval_html_af256e63ca94f7809da101ad1c33c8e7a"></a>
<a id="aunioncharger__propval_html_af4e383bb797432033050937740ce0ac3"></a>
<a id="aunioncharger__propval_html_afbe7b5fe1e421fb97b37d71ce14dc51a"></a>

```c
/*
 * Copyright 2023 Cirrus Logic, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CHARGER_H_
#define ZEPHYR_INCLUDE_DRIVERS_CHARGER_H_


#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

enum charger_property {
        CHARGER_PROP_ONLINE = 0,
        CHARGER_PROP_PRESENT,
        CHARGER_PROP_STATUS,
        CHARGER_PROP_CHARGE_TYPE,
        CHARGER_PROP_HEALTH,
        CHARGER_PROP_CONSTANT_CHARGE_CURRENT_UA,
        CHARGER_PROP_PRECHARGE_CURRENT_UA,
        CHARGER_PROP_CHARGE_TERM_CURRENT_UA,
        CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_UV,
        CHARGER_PROP_INPUT_REGULATION_CURRENT_UA,
        CHARGER_PROP_INPUT_REGULATION_VOLTAGE_UV,
        CHARGER_PROP_INPUT_CURRENT_NOTIFICATION,
        CHARGER_PROP_DISCHARGE_CURRENT_NOTIFICATION,
        CHARGER_PROP_SYSTEM_VOLTAGE_NOTIFICATION_UV,
        CHARGER_PROP_STATUS_NOTIFICATION,
        CHARGER_PROP_ONLINE_NOTIFICATION,
        CHARGER_PROP_COMMON_COUNT,
        CHARGER_PROP_CUSTOM_BEGIN = CHARGER_PROP_COMMON_COUNT + 1,
        CHARGER_PROP_MAX = UINT16_MAX,
};

typedef uint16_t charger_prop_t;

typedef int32_t charger_custom_value_int_t;

typedef uint32_t charger_custom_value_uint_t;

typedef bool charger_custom_value_bool_t;

enum charger_online {
        CHARGER_ONLINE_OFFLINE = 0,
        CHARGER_ONLINE_FIXED,
        CHARGER_ONLINE_PROGRAMMABLE,
};

enum charger_status {
        CHARGER_STATUS_UNKNOWN = 0,
        CHARGER_STATUS_CHARGING,
        CHARGER_STATUS_DISCHARGING,
        CHARGER_STATUS_NOT_CHARGING,
        CHARGER_STATUS_FULL,
};

enum charger_charge_type {
        CHARGER_CHARGE_TYPE_UNKNOWN = 0,
        CHARGER_CHARGE_TYPE_NONE,
        CHARGER_CHARGE_TYPE_TRICKLE,
        CHARGER_CHARGE_TYPE_FAST,
        CHARGER_CHARGE_TYPE_STANDARD,
        CHARGER_CHARGE_TYPE_ADAPTIVE,
        CHARGER_CHARGE_TYPE_LONGLIFE,
        CHARGER_CHARGE_TYPE_BYPASS,
};

enum charger_health {
        CHARGER_HEALTH_UNKNOWN = 0,
        CHARGER_HEALTH_GOOD,
        CHARGER_HEALTH_OVERHEAT,
        CHARGER_HEALTH_OVERVOLTAGE,
        CHARGER_HEALTH_UNSPEC_FAILURE,
        CHARGER_HEALTH_COLD,
        CHARGER_HEALTH_WATCHDOG_TIMER_EXPIRE,
        CHARGER_HEALTH_SAFETY_TIMER_EXPIRE,
        CHARGER_HEALTH_CALIBRATION_REQUIRED,
        CHARGER_HEALTH_WARM,
        CHARGER_HEALTH_COOL,
        CHARGER_HEALTH_HOT,
        CHARGER_HEALTH_NO_BATTERY,
};

enum charger_notification_severity {
        CHARGER_SEVERITY_PEAK = 0,
        CHARGER_SEVERITY_CRITICAL,
        CHARGER_SEVERITY_WARNING,
};

struct charger_current_notifier {
        uint8_t severity;
        uint32_t current_ua;
        uint32_t duration_us;
};

typedef void (*charger_status_notifier_t)(enum charger_status status);

typedef void (*charger_online_notifier_t)(enum charger_online online);

union charger_propval {
        /* Fields have the format: */
        /* CHARGER_PROPERTY_FIELD */
        /* type property_field; */

        enum charger_online online;
        bool present;
        enum charger_status status;
        enum charger_charge_type charge_type;
        enum charger_health health;
        uint32_t const_charge_current_ua;
        uint32_t precharge_current_ua;
        uint32_t charge_term_current_ua;
        uint32_t const_charge_voltage_uv;
        uint32_t input_current_regulation_current_ua;
        uint32_t input_voltage_regulation_voltage_uv;
        struct charger_current_notifier input_current_notification;
        struct charger_current_notifier discharge_current_notification;
        uint32_t system_voltage_notification;
        charger_status_notifier_t status_notification;
        charger_online_notifier_t online_notification;
        charger_custom_value_int_t custom_int;
        charger_custom_value_uint_t custom_uint;
        charger_custom_value_bool_t custom_bool;
};


typedef int (*charger_get_property_t)(const struct device *dev, const charger_prop_t prop,
                                      union charger_propval *val);

typedef int (*charger_set_property_t)(const struct device *dev, const charger_prop_t prop,
                                      const union charger_propval *val);

typedef int (*charger_charge_enable_t)(const struct device *dev, const bool enable);

__subsystem struct charger_driver_api {
        charger_get_property_t get_property;
        charger_set_property_t set_property;
        charger_charge_enable_t charge_enable;
};


__syscall int charger_get_prop(const struct device *dev, const charger_prop_t prop,
                               union charger_propval *val);

static inline int z_impl_charger_get_prop(const struct device *dev, const charger_prop_t prop,
                                          union charger_propval *val)
{
        return DEVICE_API_GET(charger, dev)->get_property(dev, prop, val);
}

__syscall int charger_set_prop(const struct device *dev, const charger_prop_t prop,
                               const union charger_propval *val);

static inline int z_impl_charger_set_prop(const struct device *dev, const charger_prop_t prop,
                                          const union charger_propval *val)
{
        return DEVICE_API_GET(charger, dev)->set_property(dev, prop, val);
}

__syscall int charger_charge_enable(const struct device *dev, const bool enable);

static inline int z_impl_charger_charge_enable(const struct device *dev, const bool enable)
{
        return DEVICE_API_GET(charger, dev)->charge_enable(dev, enable);
}


#ifdef __cplusplus
}
#endif /* __cplusplus */

#include <zephyr/syscalls/charger.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_CHARGER_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 Cirrus Logic, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 37 行

条件编译标记：`__cplusplus`。

### 注释 3：原第 292 行

字段格式如下：

### 注释 4：原第 293 行

`CHARGER_PROPERTY_FIELD`。

### 注释 5：原第 294 行

字段声明格式：`type property_field;`。

### 注释 6：原第 442 行

条件编译标记：`__cplusplus`。

### 注释 7：原第 446 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CHARGER_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/charger_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [charger_property](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga6eb3b4cc76e4f1e34732b7853eb860b7)
- [CHARGER_PROP_ONLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a1c8906c0e4e278b84cab7d126cf95526)
- [CHARGER_PROP_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a0dd5ee0d22cba6440c3f3583582d405b)
- [CHARGER_PROP_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a73b9f45dd43347016a4dd6e15cd78cf6)
- [CHARGER_PROP_CHARGE_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95)
- [CHARGER_PROP_HEALTH](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654)
- [CHARGER_PROP_CONSTANT_CHARGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a81a18d7286bfcf729402db6990ddc306)
- [CHARGER_PROP_PRECHARGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9)
- [CHARGER_PROP_CHARGE_TERM_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc)
- [CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a5b4a6c4f1f6abb7a568c7c42dca696bf)
- [CHARGER_PROP_INPUT_REGULATION_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a703a0e374053a410ec154eac117f9085)
- [CHARGER_PROP_INPUT_REGULATION_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a1e60d770a5d8e47118040ace3c6d8ec0)
- [CHARGER_PROP_INPUT_CURRENT_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a70f2c71cd9d4e0f88ee36886094540fe)
- [CHARGER_PROP_DISCHARGE_CURRENT_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a3d3e3190b016a9c31ed5c82e2ade0b72)
- [CHARGER_PROP_SYSTEM_VOLTAGE_NOTIFICATION_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7ace0a0e6cbc0ccaf166ff0df7e1b275c0)
- [CHARGER_PROP_STATUS_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a9340eb6fb5b80370148a43366b753d9b)
- [CHARGER_PROP_ONLINE_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a389920359b8866af70b164d68820d4b7)
- [CHARGER_PROP_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732)
- [CHARGER_PROP_CUSTOM_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3)
- [CHARGER_PROP_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e)
- [UINT16_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3ea490c9b3617d4479bd80ef93cd5602)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [charger_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4ce808890de2d01cdb75feddbf275635)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [charger_custom_value_int_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga9325615cdd8985cbb3407257afb387a2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [charger_custom_value_uint_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaa7a6c34b4871673151671eae1fac84da)
- [charger_custom_value_bool_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga3b448c73ef8c4844ccbe7adb1f2458fe)
- [charger_online](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gad95d2b1aaf18ac3a1c536f2d40317c19)
- [CHARGER_ONLINE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3)
- [CHARGER_ONLINE_FIXED](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6)
- [CHARGER_ONLINE_PROGRAMMABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e)
- [charger_status](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga4a3c46bc0916082d15e665f7665c89d7)
- [CHARGER_STATUS_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5)
- [CHARGER_STATUS_CHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad)
- [CHARGER_STATUS_DISCHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e)
- [CHARGER_STATUS_NOT_CHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658)
- [CHARGER_STATUS_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf)
- [charger_charge_type](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaee833a379a8674621d2fdf9b57d1f803)
- [CHARGER_CHARGE_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4)
- [CHARGER_CHARGE_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17)
- [CHARGER_CHARGE_TYPE_TRICKLE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8)
- [CHARGER_CHARGE_TYPE_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711)
- [CHARGER_CHARGE_TYPE_STANDARD](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6)
- [CHARGER_CHARGE_TYPE_ADAPTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2)
- [CHARGER_CHARGE_TYPE_LONGLIFE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f)
- [CHARGER_CHARGE_TYPE_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8)
- [charger_health](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gaab33241d3b85ab0770be9b1bd17e4412)
- [CHARGER_HEALTH_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad)
- [CHARGER_HEALTH_GOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538)
- [CHARGER_HEALTH_OVERHEAT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b)
- [CHARGER_HEALTH_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459)
- [CHARGER_HEALTH_UNSPEC_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa)
- [CHARGER_HEALTH_COLD](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967)
- [CHARGER_HEALTH_WATCHDOG_TIMER_EXPIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce)
- [CHARGER_HEALTH_SAFETY_TIMER_EXPIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82)
- [CHARGER_HEALTH_CALIBRATION_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1)
- [CHARGER_HEALTH_WARM](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f)
- [CHARGER_HEALTH_COOL](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3)
- [CHARGER_HEALTH_HOT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1)
- [CHARGER_HEALTH_NO_BATTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b)
- [charger_notification_severity](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga2e7d7f15725db4d502bc3f46476a310d)
- [CHARGER_SEVERITY_PEAK](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b)
- [CHARGER_SEVERITY_CRITICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8)
- [CHARGER_SEVERITY_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885)
- [charger_current_notifier](../device_power_control_model_reference/P001_charger_current_notifier_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [severity](../device_power_control_model_reference/P001_charger_current_notifier_结构体.md#a22c26477263e5abedb200de36a29d9de)
- [current_ua](../device_power_control_model_reference/P001_charger_current_notifier_结构体.md#acb54706bf47f55e197e799393b9eb87e)
- [duration_us](../device_power_control_model_reference/P001_charger_current_notifier_结构体.md#a4998999ef893d18fa64b86ec4fd9ad94)
- [charger_status_notifier_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga7666697bde91b66829113efe151d1cb2)
- [charger_online_notifier_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gab29c2fafc53988555d72974199f25475)
- [charger_propval](../device_power_control_model_reference/P104_charger_propval_联合体.md)
- [online](../device_power_control_model_reference/P104_charger_propval_联合体.md#a8589124e6152b70b649788a8b94461ab)
- [present](../device_power_control_model_reference/P104_charger_propval_联合体.md#ab0eec508b90d205a1662fd6c69638764)
- [status](../device_power_control_model_reference/P104_charger_propval_联合体.md#a7f4976d72d4a7d48385ceb9f18c510b5)
- [charge_type](../device_power_control_model_reference/P104_charger_propval_联合体.md#ac1a594de2b1c10d28b6a81dd66f1a6ba)
- [health](../device_power_control_model_reference/P104_charger_propval_联合体.md#abd990f67423424da60856f4b6e8824a3)
- [const_charge_current_ua](../device_power_control_model_reference/P104_charger_propval_联合体.md#af4e383bb797432033050937740ce0ac3)
- [precharge_current_ua](../device_power_control_model_reference/P104_charger_propval_联合体.md#a24a97e16505fa336bd3a68743d05936b)
- [charge_term_current_ua](../device_power_control_model_reference/P104_charger_propval_联合体.md#a89d0c93d68650cefe29e891f4db928f4)
- [const_charge_voltage_uv](../device_power_control_model_reference/P104_charger_propval_联合体.md#a733bae9ce0bf7e902f8af307f94a356c)
- [input_current_regulation_current_ua](../device_power_control_model_reference/P104_charger_propval_联合体.md#ae51670de8fa560f0c7610452db029bc2)
- [input_voltage_regulation_voltage_uv](../device_power_control_model_reference/P104_charger_propval_联合体.md#afbe7b5fe1e421fb97b37d71ce14dc51a)
- [input_current_notification](../device_power_control_model_reference/P104_charger_propval_联合体.md#a0ad956ab4d0b306f94cce2aa81283a35)
- [discharge_current_notification](../device_power_control_model_reference/P104_charger_propval_联合体.md#af256e63ca94f7809da101ad1c33c8e7a)
- [system_voltage_notification](../device_power_control_model_reference/P104_charger_propval_联合体.md#a541d1bf0b3e32d7aaeb6a2f4f443c5dc)
- [status_notification](../device_power_control_model_reference/P104_charger_propval_联合体.md#ad77547e88ec465d2e37526751008f634)
- [online_notification](../device_power_control_model_reference/P104_charger_propval_联合体.md#ab9f40a6083ff2361ea4d161226cd77ad)
- [custom_int](../device_power_control_model_reference/P104_charger_propval_联合体.md#a0e9c59df061dbe7d221244cd48530a10)
- [custom_uint](../device_power_control_model_reference/P104_charger_propval_联合体.md#a7b7aa29e279028e502d8662c70fc1747)
- [custom_bool](../device_power_control_model_reference/P104_charger_propval_联合体.md#a1619752e64e8f99d1a488d1fa887ee60)
- [charger_get_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html#gafb7488129e0a6c086d3ff0ffadb6c82b)
- [device](../device_reference/P002_设备对象结构.md)
- [charger_set_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html#ga6556781abf0e81eee431c88cb894a8e6)
- [charger_charge_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html#gaf035c2972693a8763fd08b7db8c9c0bd)
- [charger_driver_api](../device_power_control_model_reference/P002_charger_driver_api_结构体.md)
- [get_property](../device_power_control_model_reference/P002_charger_driver_api_结构体.md#a945bfc62b0572da09480e97a6a819269)
- [set_property](../device_power_control_model_reference/P002_charger_driver_api_结构体.md#a7a7942d11841d9ec02ff57f46323a3a3)
- [charge_enable](../device_power_control_model_reference/P002_charger_driver_api_结构体.md#a41ea553c8bb6a24915d73a00129ee67d)
- [charger_get_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga00e5b61d517c93d7d3c863b14b07b738)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [charger_set_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#ga0036e3f5924585457a99a2e444ef5aab)
- [charger_charge_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gace1ea9841574d75d314db078df5a0b3a)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [charger_current_notifier::severity](../device_power_control_model_reference/P001_charger_current_notifier_结构体.md#a22c26477263e5abedb200de36a29d9de)
- [charger_current_notifier::duration_us](../device_power_control_model_reference/P001_charger_current_notifier_结构体.md#a4998999ef893d18fa64b86ec4fd9ad94)
- [charger_current_notifier::current_ua](../device_power_control_model_reference/P001_charger_current_notifier_结构体.md#acb54706bf47f55e197e799393b9eb87e)
- [charger_driver_api::charge_enable](../device_power_control_model_reference/P002_charger_driver_api_结构体.md#a41ea553c8bb6a24915d73a00129ee67d)
- [charger_driver_api::set_property](../device_power_control_model_reference/P002_charger_driver_api_结构体.md#a7a7942d11841d9ec02ff57f46323a3a3)
- [charger_driver_api::get_property](../device_power_control_model_reference/P002_charger_driver_api_结构体.md#a945bfc62b0572da09480e97a6a819269)
- [charger_propval::input_current_notification](../device_power_control_model_reference/P104_charger_propval_联合体.md#a0ad956ab4d0b306f94cce2aa81283a35)
- [charger_propval::custom_int](../device_power_control_model_reference/P104_charger_propval_联合体.md#a0e9c59df061dbe7d221244cd48530a10)
- [charger_propval::custom_bool](../device_power_control_model_reference/P104_charger_propval_联合体.md#a1619752e64e8f99d1a488d1fa887ee60)
- [charger_propval::precharge_current_ua](../device_power_control_model_reference/P104_charger_propval_联合体.md#a24a97e16505fa336bd3a68743d05936b)
- [charger_propval::system_voltage_notification](../device_power_control_model_reference/P104_charger_propval_联合体.md#a541d1bf0b3e32d7aaeb6a2f4f443c5dc)
- [charger_propval::const_charge_voltage_uv](../device_power_control_model_reference/P104_charger_propval_联合体.md#a733bae9ce0bf7e902f8af307f94a356c)
- [charger_propval::custom_uint](../device_power_control_model_reference/P104_charger_propval_联合体.md#a7b7aa29e279028e502d8662c70fc1747)
- [charger_propval::status](../device_power_control_model_reference/P104_charger_propval_联合体.md#a7f4976d72d4a7d48385ceb9f18c510b5)
- [charger_propval::online](../device_power_control_model_reference/P104_charger_propval_联合体.md#a8589124e6152b70b649788a8b94461ab)
- [charger_propval::charge_term_current_ua](../device_power_control_model_reference/P104_charger_propval_联合体.md#a89d0c93d68650cefe29e891f4db928f4)
- [charger_propval::present](../device_power_control_model_reference/P104_charger_propval_联合体.md#ab0eec508b90d205a1662fd6c69638764)
- [charger_propval::online_notification](../device_power_control_model_reference/P104_charger_propval_联合体.md#ab9f40a6083ff2361ea4d161226cd77ad)
- [charger_propval::health](../device_power_control_model_reference/P104_charger_propval_联合体.md#abd990f67423424da60856f4b6e8824a3)
- [charger_propval::charge_type](../device_power_control_model_reference/P104_charger_propval_联合体.md#ac1a594de2b1c10d28b6a81dd66f1a6ba)
- [charger_propval::status_notification](../device_power_control_model_reference/P104_charger_propval_联合体.md#ad77547e88ec465d2e37526751008f634)
- [charger_propval::input_current_regulation_current_ua](../device_power_control_model_reference/P104_charger_propval_联合体.md#ae51670de8fa560f0c7610452db029bc2)
- [charger_propval::discharge_current_notification](../device_power_control_model_reference/P104_charger_propval_联合体.md#af256e63ca94f7809da101ad1c33c8e7a)
- [charger_propval::const_charge_current_ua](../device_power_control_model_reference/P104_charger_propval_联合体.md#af4e383bb797432033050937740ce0ac3)
- [charger_propval::input_voltage_regulation_voltage_uv](../device_power_control_model_reference/P104_charger_propval_联合体.md#afbe7b5fe1e421fb97b37d71ce14dc51a)

---

[上一章](P006_cfi.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_cleanup.h_源码浏览.md)
