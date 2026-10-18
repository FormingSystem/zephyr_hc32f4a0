---
id: learning.zephyr-docs.networking.api-193
title: OCPP头文件源码
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ocpp_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第193章\_OCPP头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ocpp_8h_source.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 193.1\_阅读说明与来源

译注：先读[OCPP 充电桩协议指南](P179_OCPP充电桩协议.md)和[充电桩示例](P182_OCPP充电桩示例.md)，理解充电桩（Charge Point，CP）、中央系统（Central System，CS）、连接器（Connector）、会话（Session）与交易（Transaction）的关系，再按符号查询。

本组：[OCPP完整API参考](P191_OCPP完整API参考.md) · [OCPP头文件参考](P192_OCPP头文件参考.md) · [OCPP头文件源码](P193_OCPP头文件源码.md) · [OCPP充电桩信息结构](P194_OCPP充电桩信息结构.md) · [OCPP中央系统信息结构](P195_OCPP中央系统信息结构.md) · [OCPP的TLS凭据结构](P196_OCPP的TLS凭据结构.md) · [OCPP回调输入输出联合体](P197_OCPP回调输入输出联合体.md)。

下方保留官方 Doxygen 源码浏览页展示的全部代码、标识符和版权／许可注释。仅移除网页行号，将展示用不换行空格还原为空格，并清除行尾空白。原页面已省略用于生成 API 文档的部分注释，行号原本存在跳跃；本展示不能替代完整原始头文件。接口、参数和结构体注释均在本组参考页翻译。

## 193.2\_原始源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00068"></a>
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
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="foldopen00146"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="foldopen00154"></a>
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
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="agroup__ip__4__6_html_ga8b4cfadf1b284e52d6905ca88657b48a"></a>
<a id="agroup__ocpp__api_html_ga0cf7081249c509eb467df6147b0e6110"></a>
<a id="agroup__ocpp__api_html_ga306ab09a7e1ce5eb37a25a6933fd8228"></a>
<a id="agroup__ocpp__api_html_ga4b2b8885d144627d43e724a3889ee1cb"></a>
<a id="agroup__ocpp__api_html_ga59e708015c120bba1414ff8331080e20"></a>
<a id="agroup__ocpp__api_html_ga626b8c34f21c59cebdd844218a26f809"></a>
<a id="agroup__ocpp__api_html_ga6cbb071143791698356c7d5787151947"></a>
<a id="agroup__ocpp__api_html_ga7bce1312f3e08bb9862b9162a231c9c4"></a>
<a id="agroup__ocpp__api_html_ga94824d57e36cc817619523aaded8ece1"></a>
<a id="agroup__ocpp__api_html_ga96b1352538137fc49587f4aad069fa66"></a>
<a id="agroup__ocpp__api_html_gaad737e5b91eba7a972da88097f8894e9"></a>
<a id="agroup__ocpp__api_html_gad6b888a526a57532feb21dcf8a6bd071"></a>
<a id="agroup__ocpp__api_html_gafc9982ab1d88e9af2ebe647c671876c6"></a>
<a id="agroup__ocpp__api_html_gga4b2b8885d144627d43e724a3889ee1cba1345c54c53dd0088aa5de6763dd15cc2"></a>
<a id="agroup__ocpp__api_html_gga4b2b8885d144627d43e724a3889ee1cba15b29195fc077bd2cf58a1fda047a5c3"></a>
<a id="agroup__ocpp__api_html_gga4b2b8885d144627d43e724a3889ee1cba23198c5ad01a58694a5f42593f97d026"></a>
<a id="agroup__ocpp__api_html_gga4b2b8885d144627d43e724a3889ee1cbac4064ac7c1f2ed004965e9441d19b88d"></a>
<a id="agroup__ocpp__api_html_gga4b2b8885d144627d43e724a3889ee1cbae90129c78fda6c9f21aaadba45a11959"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a01fb33e7bc399d4b685d396720b698c1"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a06e0a29177bc5b0d920de921e10b7186"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a224d2d25d57886c8200fd0a447e5faae"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a35a9bb9bf371166906479455c1c9178a"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a36bb5a1d957b77c8b6d65042f2c589ac"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a40a3b80da74a8645f6bb50be64b23ace"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a4fa1401134fe057b051a7131049e8e44"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a5b720f10cb8518951c8dc7f209e22490"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a66ccc789070a28f21fd8e4521b967d83"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a6aaf34eb8cd7a9c538f70f7c2909e9b0"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a91b3027a78c2bb5069ac655b614f3e6e"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809a933787dfcec73082ebd4c0144fdd0cd9"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809ab379992411707f5eec45287163d288fc"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809accddeeb3811744536e7f280610c748a0"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809ace0bd2c98033300135471c5f1fea1c06"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809ae9e74f6c45265912220d9a3758a2df0c"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809aeb80f2a3820318120d9ae62f11bbb15d"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809aed5d3d42b3927cab608c4dc3a16e3724"></a>
<a id="agroup__ocpp__api_html_gga626b8c34f21c59cebdd844218a26f809affb62430884b2c8976fdd2c21fc383eb"></a>
<a id="agroup__ocpp__api_html_gga96b1352538137fc49587f4aad069fa66a08926167e33944dac03db3bb07d45a00"></a>
<a id="agroup__ocpp__api_html_gga96b1352538137fc49587f4aad069fa66a3570d5e28bc4efc360da47d0f31787b8"></a>
<a id="agroup__ocpp__api_html_gga96b1352538137fc49587f4aad069fa66a502f9e4a4ef623f5e669747fcf22b6fd"></a>
<a id="agroup__ocpp__api_html_gga96b1352538137fc49587f4aad069fa66a93ad1eb3396e70cfc25c76393175c0ab"></a>
<a id="agroup__tls__credentials_html_gaadfe9694309e473f7be74ed98dfb36d3"></a>
<a id="akernel_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdio_8h_html"></a>
<a id="astructocpp__cp__info_html"></a>
<a id="astructocpp__cp__info_html_a22553b2e207558ea51915cc45f4a385c"></a>
<a id="astructocpp__cp__info_html_a273f5ed3ef61465bda6c54033be994bd"></a>
<a id="astructocpp__cp__info_html_a28f4cc142ecd584a4d2477092f7f1c3f"></a>
<a id="astructocpp__cp__info_html_a38e5219ba817bb7cfcf9ab7582b594f2"></a>
<a id="astructocpp__cp__info_html_a52ad8e1e7509f56e13c9f45b821e354c"></a>
<a id="astructocpp__cp__info_html_a5b6dcc9c966a09f15e38ac927237f2e1"></a>
<a id="astructocpp__cp__info_html_a7876ac178c93df2065fe95bae76c274d"></a>
<a id="astructocpp__cp__info_html_a7c043b50beb91d98f546b809867e8405"></a>
<a id="astructocpp__cp__info_html_ae7cae41736a48a01377c5e230adef80c"></a>
<a id="astructocpp__cp__info_html_af2cdde4d27e0223644456842240723e2"></a>
<a id="astructocpp__cs__info_html"></a>
<a id="astructocpp__cs__info_html_a1f4773ddd7d806ed78c737c8e816bfe6"></a>
<a id="astructocpp__cs__info_html_a99e0021bf753cee1adbc26bb77d44423"></a>
<a id="astructocpp__cs__info_html_ac141083d4bfc61dcb6333527c5c4492b"></a>
<a id="astructocpp__cs__info_html_ae08b92eb19e5db6c5a4ee288fd432ac5"></a>
<a id="astructocpp__tls__credentials_html"></a>
<a id="astructocpp__tls__credentials_html_a38877cf5cdbfb9d86a0932a231ac4ac0"></a>
<a id="astructocpp__tls__credentials_html_a489357da079435f78a5fbcc96c7d4eb3"></a>
<a id="astructocpp__tls__credentials_html_a7a8e98e378561654968250b157ef2bf7"></a>
<a id="astructocpp__tls__credentials_html_aa86c71d47996475aed2dc064f8278a2d"></a>
<a id="atls__credentials_8h_html"></a>
<a id="aunionocpp__io__value_html"></a>
<a id="aunionocpp__io__value_html_a2681a91a384efba554996e5090b31887"></a>
<a id="aunionocpp__io__value_html_a2ba720a5a05f4055a2fd2df55db729a9"></a>
<a id="aunionocpp__io__value_html_aae16117ce8458ee8ed2ae394452a2571"></a>
<a id="aunionocpp__io__value_html_aaf7363d38b1caecf7767c499a9cc5019"></a>
<a id="aunionocpp__io__value_html_acda3059ed054204148b9b5f7d320e958"></a>
<a id="aunionocpp__io__value_html_ae58818d242c3703f79adf32550608100"></a>
<a id="aunionocpp__io__value_html_ae6005468ff90f70b97677ab189b36823"></a>
<a id="aunionocpp__io__value_html_ae7d64324b4475b1c5ec15633c1a0aa4c"></a>

```c
/*
 * Copyright (c) 2024 Linumiz
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_OCPP_H_
#define ZEPHYR_INCLUDE_NET_OCPP_H_

#include <stdio.h>
#include <zephyr/kernel.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/tls_credentials.h>

#ifdef __cplusplus
extern "C" {
#endif

#define CISTR50 50

enum ocpp_auth_status {
        OCPP_AUTH_INVALID,
        OCPP_AUTH_ACCEPTED,
        OCPP_AUTH_BLOCKED,
        OCPP_AUTH_EXPIRED,
        OCPP_AUTH_CONCURRENT_TX
};

enum ocpp_notify_reason {
        OCPP_USR_GET_METER_VALUE,

        OCPP_USR_START_CHARGING,

        OCPP_USR_STOP_CHARGING,

        OCPP_USR_UNLOCK_CONNECTOR,
};

enum ocpp_meter_measurand {
        OCPP_OMM_CURRENT_FROM_EV,
        OCPP_OMM_CURRENT_TO_EV,
        OCPP_OMM_CURRENT_MAX_OFFERED_TO_EV,
        OCPP_OMM_ACTIVE_ENERGY_FROM_EV,
        OCPP_OMM_ACTIVE_ENERGY_TO_EV,
        OCPP_OMM_REACTIVE_ENERGY_FROM_EV,
        OCPP_OMM_REACTIVE_ENERGY_TO_EV,
        OCPP_OMM_ACTIVE_POWER_FROM_EV,
        OCPP_OMM_ACTIVE_POWER_TO_EV,
        OCPP_OMM_REACTIVE_POWER_FROM_EV,
        OCPP_OMM_REACTIVE_POWER_TO_EV,
        OCPP_OMM_POWERLINE_FREQ,
        OCPP_OMM_POWER_FACTOR,
        OCPP_OMM_POWER_MAX_OFFERED_TO_EV,
        OCPP_OMM_FAN_SPEED,
        OCPP_OMM_CHARGING_PERCENT,
        OCPP_OMM_TEMPERATURE,
        OCPP_OMM_VOLTAGE_AC_RMS,

        OCPP_OMM_END
};

union ocpp_io_value {

        struct {
                int id_con;

                enum ocpp_meter_measurand mes;

                char val[CISTR50];
        } meter_val;

        struct {
                char idtag[CISTR50];

                int id_con;
        } start_charge;

        struct {
                int id_con;
        } stop_charge;

        struct {
                int id_con;
        } unlock_con;
};

struct ocpp_cp_info {
        char *model;
        char *vendor;

        int num_of_con;

        char *sl_no;
        char *box_sl_no;
        char *fw_ver;
        char *iccid;
        char *imsi;
        char *meter_sl_no;
        char *meter_type;
};

struct ocpp_tls_credentials {
        const sec_tag_t *sec_tag_list;
        char *tls_hostname;
        size_t sec_tag_list_size;
        size_t tls_hostname_size;
};

struct ocpp_cs_info {
        char *cs_ip;
        char *ws_url;
        int port;
        net_sa_family_t sa_family;
#if defined(CONFIG_NET_SOCKETS_SOCKOPT_TLS)
        struct ocpp_tls_credentials creds;
#endif
};

typedef void *ocpp_session_handle_t;

typedef int (*ocpp_user_notify_callback_t)(enum ocpp_notify_reason reason,
                                           union ocpp_io_value *io,
                                           void *user_data);

int ocpp_init(struct ocpp_cp_info *cpi,
              struct ocpp_cs_info *csi,
              ocpp_user_notify_callback_t cb,
              void *user_data);

int ocpp_session_open(ocpp_session_handle_t *hndl);

void ocpp_session_close(ocpp_session_handle_t hndl);

int ocpp_authorize(ocpp_session_handle_t hndl,
                   char *idtag,
                   enum ocpp_auth_status *status,
                   uint32_t timeout_ms);

int ocpp_start_transaction(ocpp_session_handle_t hndl,
                           int meter_val,
                           uint8_t conn_id,
                           uint32_t timeout_ms);

int ocpp_stop_transaction(ocpp_session_handle_t hndl,
                          int meter_val,
                          uint32_t timeout_ms);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_OCPP_H_ */
```

## 193.3\_源码注释译文

版权：2024 年 Linumiz；许可证标识为 `Apache-2.0`。法律署名保持原样。`ZEPHYR_INCLUDE_NET_OCPP_H_` 用于头文件包含保护（Header Include Guard）；`extern "C"` 为 C++ 调用方提供 C 链接约定。

## 193.4\_相关源码与使用边界

声明来自 `<zephyr/net/ocpp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/ocpp.h)可用于源码追踪，版本可能与官网 `latest` 不同。源码核对依据为本批保存的[官方协议实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/ocpp.c)、[官方请求实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/core.c)及[官方示例](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/src/main.c)，摘要见[来源记录](../SOURCES.md)。

[上一章](P192_OCPP头文件参考.md) · [返回大纲](大纲.md) · [下一章](P194_OCPP充电桩信息结构.md)
