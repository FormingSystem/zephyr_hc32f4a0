---
id: learning.zephyr-docs.api-source-supplement-reference.page-228
title: transport_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/transport__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第228章\_transport\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/transport__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/transport__mgmt_8h.html)。

## 228.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="foldopen00174"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="foldopen00238"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ga20cae62e5a2ff1edd8bd47c09bedb899"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ga2e6e8baabe2f34597bdba27bd8be3f5d"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ga3d0f57cfc30eea8b88a91444abc84587"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ga63d8fff2d408a31503fd7d9900d014f8"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ga6a3fc6b16a8f0a8be70a9c395c240344"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ga9dccb97ec585e3f6fbefb076c0702a0b"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gac35a18a01b5cff74aa117d7a3739e7a1"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gace3b51c7b0e6ca80b70a8602800f540f"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gae10192f3da308db7777aa9e13ec0dd98"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gafd6cc94b25d114564c6aa30bec41c14b"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga20cae62e5a2ff1edd8bd47c09bedb899a4541d5558c4049f81f1436c4fc7f53e3"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga20cae62e5a2ff1edd8bd47c09bedb899a4791f3585507952d1a86aa9eafb5f1af"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga20cae62e5a2ff1edd8bd47c09bedb899a71b75164c2408986e43093e817a15532"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga20cae62e5a2ff1edd8bd47c09bedb899ab3bedc6db7e1da2334c5c7af64fa68e5"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga20cae62e5a2ff1edd8bd47c09bedb899abea44b2b3b70a48bce31d6ae07ff7977"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0ba05be247bbd2ed96809ca856d71d0e88f"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0ba0fde105d8cd7cbf0a8781faa9db8136d"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0ba1e1c7e63d17dca29404f64960a564eea"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0ba2563b4336e20d0b4573b08787682aa03"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0ba33a1996969a80f586aa07b5579825dee"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0ba5e289fe0655882faa108e7171c2d229f"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0ba684cfd90f80df815703e5db5f19cc32b"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0ba6926fbd86577bd23b2caa51cd6715f56"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0ba7833f384ca57c0118790fbf7af281a97"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0ba8654385eede95aa8c1d42be55f442bec"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0ba8ba2d5d9553578df5eea84eac24bb399"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0babcf4a53c480f3e80b5aab929d83d29e8"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0babdb237a6ddbe8d2bfb5103fb2f0c5155"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0babea503e9b932a05eecc1f179ed651bb2"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0bae90d5593819ce610d78723d5f33e4f43"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0baee652c087a1ab0f7188febb1e907db7d"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0baf746faaf0b368fd076190aebde47097a"></a>
<a id="agroup__mcumgr__transport__mgmt_html_gga9dccb97ec585e3f6fbefb076c0702a0baf89cd9308236121019733517eeaea421"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ggafd6cc94b25d114564c6aa30bec41c14ba04662ef967bc6ad42b7606a11aec773f"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ggafd6cc94b25d114564c6aa30bec41c14ba22083e434ea11e01916bb0d58f5a33a3"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ggafd6cc94b25d114564c6aa30bec41c14ba3a451c036732b87208c38d84df384c2c"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ggafd6cc94b25d114564c6aa30bec41c14ba408f083dddd2d42987dd5ea47572f5e0"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ggafd6cc94b25d114564c6aa30bec41c14ba50d0df5f92d46b697e7cc7c8d3a43e93"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ggafd6cc94b25d114564c6aa30bec41c14ba67b28c281b5d0ba9a7a686cf76881a85"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ggafd6cc94b25d114564c6aa30bec41c14ba6cd0a2a1b247e0e2f2683f4063adaee3"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ggafd6cc94b25d114564c6aa30bec41c14ba87735cde975ff404e10ff29cfe76c24c"></a>
<a id="agroup__mcumgr__transport__mgmt_html_ggafd6cc94b25d114564c6aa30bec41c14ba9c46215d029d1d0b030a69fcb1812ad1"></a>
<a id="amgmt_2mcumgr_2transport_2smp_8h_html"></a>
<a id="amgmt__defines_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructsmp__transport__bridge_html"></a>
<a id="astructsmp__transport_html"></a>

```c
/*
 * Copyright (c) 2025-2026 Nordic Semiconductor ASA
 * Copyright (c) 2026, Jamie McCrae
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_TRANSPORT_MGMT_TRANSPORT_MGMT_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_TRANSPORT_MGMT_TRANSPORT_MGMT_H_

#include <stdint.h>
#include <stdbool.h>
#include <zephyr/mgmt/mcumgr/transport/smp.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h>


#ifdef __cplusplus
extern "C" {
#endif

enum transport_mgmt_ids {
        TRANSPORT_MGMT_ID_CONNECT,

        TRANSPORT_MGMT_ID_DISCONNECT,

        TRANSPORT_MGMT_ID_STATUS,

        TRANSPORT_MGMT_ID_RESERVED_1,

        TRANSPORT_MGMT_ID_RESERVED_2,

        TRANSPORT_MGMT_ID_RESERVED_3,

        /*
         * The following are purposely at the end to be able to see if they have been excluded
         * when using enum mgmt due to being optional when using a custom derivative group ID
         */

        TRANSPORT_MGMT_ID_LIST,

        TRANSPORT_MGMT_ID_GET_MODES,

        TRANSPORT_MGMT_ID_GET_CONFIG_DETAILS,
};

#define TRANSPORT_MGMT_DIRECTION_INCOMING false

#define TRANSPORT_MGMT_DIRECTION_OUTGOING true

bool transport_mgmt_is_bridged(struct smp_transport *transport, bool direction);

struct smp_transport *transport_mgmt_get_other_transport(struct smp_transport *transport,
                                                         bool direction);

const struct smp_transport_bridge *transport_mgmt_get_bridge(struct smp_transport *transport,
                                                             bool direction);


#if defined(CONFIG_MCUMGR_GRP_TRANSPORT_LOCKING) || defined(__DOXYGEN__)
void transport_mgmt_lock(void);

void transport_mgmt_unlock(void);
#else
#define transport_mgmt_lock() (void)0
#define transport_mgmt_unlock() (void)0
#endif

bool transport_mgmt_is_bridged_internal(struct smp_transport *transport, bool direction);

const struct smp_transport_bridge *transport_mgmt_get_bridge_internal(
                                                        struct smp_transport *transport,
                                                        bool direction);


int transport_mgmt_disconnect_bridge(struct smp_transport_bridge *bridge);

int transport_mgmt_disconnect_transport(struct smp_transport *transport, bool incoming,
                                        bool outgoing);

int transport_mgmt_disconnect_all(void);

enum transport_mgmt_ret_code_t {
        TRANSPORT_MGMT_ERR_OK = 0,

        TRANSPORT_MGMT_ERR_UNKNOWN,

        TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_REQUIRED_FUNCTIONS,

        TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_INFO_FUNCTIONS,

        TRANSPORT_MGMT_ERR_INVALID_TRANSPORT,

        TRANSPORT_MGMT_ERR_INVALID_MODE,

        TRANSPORT_MGMT_ERR_ALL_CONTEXTS_USED,

        TRANSPORT_MGMT_ERR_BOTH_TRANSPORT_AND_ALL_PARAMETERS,

        TRANSPORT_MGMT_ERR_NOT_BRIDGED,

        TRANSPORT_MGMT_ERR_SAME_BRIDGE_DEVICE_DISALLOWED,

        TRANSPORT_MGMT_ERR_TRANSPORT_INGOING_NOT_SUPPORTED,

        TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_NOT_SUPPORTED,

        TRANSPORT_MGMT_ERR_TRANSPORT_INCOMING_TRANSPORT_ALREADY_BRIDGED,

        TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_TRANSPORT_ALREADY_BRIDGED,

        TRANSPORT_MGMT_ERR_CONNECT_MISSING_PARAMETER,

        TRANSPORT_MGMT_ERR_CONNECT_INVALID_PARAMETER,

        TRANSPORT_MGMT_ERR_CONNECT_UNSUPPORTED_PARAMETER,

        TRANSPORT_MGMT_ERR_CONNECT_FAILED,
};

enum transport_mgmt_config_type_t {
        TRANSPORT_MGMT_CONFIG_TYPE_UINT = 0,

        TRANSPORT_MGMT_CONFIG_TYPE_INT,

        TRANSPORT_MGMT_CONFIG_TYPE_BOOL,

        TRANSPORT_MGMT_CONFIG_TYPE_STRING,

        TRANSPORT_MGMT_CONFIG_TYPE_BYTE_STRING,
};

#if defined(CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_FUNCTION) || defined(__DOXYGEN__)
const uint16_t transport_mgmt_group_id(void);
#elif defined(CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE)
#define transport_mgmt_group_id() CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE_GROUP_ID
#else
#define transport_mgmt_group_id() MGMT_GROUP_ID_TRANSPORT
#endif

#ifdef __cplusplus
}
#endif


#endif
```

## 228.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025-2026 Nordic Semiconductor ASA。

版权（Copyright）：© 2026, Jamie McCrae。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 55 行

以下条目特意放在末尾，以便在使用枚举管理（Enum mgmt）时判断它们是否已被排除；原因是在采用自定义派生分组标识符（Custom derivative group ID）时，这些条目是可选的。

## 228.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/transport__mgmt_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/mgmt/mcumgr/transport/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html)
- [zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h.html)
- [transport_mgmt_ids](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gafd6cc94b25d114564c6aa30bec41c14b)
- [TRANSPORT_MGMT_ID_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba87735cde975ff404e10ff29cfe76c24c)
- [TRANSPORT_MGMT_ID_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba9c46215d029d1d0b030a69fcb1812ad1)
- [TRANSPORT_MGMT_ID_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba6cd0a2a1b247e0e2f2683f4063adaee3)
- [TRANSPORT_MGMT_ID_RESERVED_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba408f083dddd2d42987dd5ea47572f5e0)
- [TRANSPORT_MGMT_ID_RESERVED_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba3a451c036732b87208c38d84df384c2c)
- [TRANSPORT_MGMT_ID_RESERVED_3](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba50d0df5f92d46b697e7cc7c8d3a43e93)
- [TRANSPORT_MGMT_ID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba67b28c281b5d0ba9a7a686cf76881a85)
- [TRANSPORT_MGMT_ID_GET_MODES](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba04662ef967bc6ad42b7606a11aec773f)
- [TRANSPORT_MGMT_ID_GET_CONFIG_DETAILS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba22083e434ea11e01916bb0d58f5a33a3)
- [transport_mgmt_is_bridged](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gace3b51c7b0e6ca80b70a8602800f540f)
- [smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)
- [transport_mgmt_get_other_transport](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga6a3fc6b16a8f0a8be70a9c395c240344)
- [smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)
- [transport_mgmt_get_bridge](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gac35a18a01b5cff74aa117d7a3739e7a1)
- [transport_mgmt_disconnect_bridge](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gae10192f3da308db7777aa9e13ec0dd98)
- [transport_mgmt_disconnect_transport](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga2e6e8baabe2f34597bdba27bd8be3f5d)
- [transport_mgmt_disconnect_all](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga3d0f57cfc30eea8b88a91444abc84587)
- [transport_mgmt_ret_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga9dccb97ec585e3f6fbefb076c0702a0b)
- [TRANSPORT_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba7833f384ca57c0118790fbf7af281a97)
- [TRANSPORT_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba2563b4336e20d0b4573b08787682aa03)
- [TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_REQUIRED_FUNCTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0baee652c087a1ab0f7188febb1e907db7d)
- [TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_INFO_FUNCTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba5e289fe0655882faa108e7171c2d229f)
- [TRANSPORT_MGMT_ERR_INVALID_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba6926fbd86577bd23b2caa51cd6715f56)
- [TRANSPORT_MGMT_ERR_INVALID_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0babdb237a6ddbe8d2bfb5103fb2f0c5155)
- [TRANSPORT_MGMT_ERR_ALL_CONTEXTS_USED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba1e1c7e63d17dca29404f64960a564eea)
- [TRANSPORT_MGMT_ERR_BOTH_TRANSPORT_AND_ALL_PARAMETERS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba8ba2d5d9553578df5eea84eac24bb399)
- [TRANSPORT_MGMT_ERR_NOT_BRIDGED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0babea503e9b932a05eecc1f179ed651bb2)
- [TRANSPORT_MGMT_ERR_SAME_BRIDGE_DEVICE_DISALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0bae90d5593819ce610d78723d5f33e4f43)
- [TRANSPORT_MGMT_ERR_TRANSPORT_INGOING_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0baf89cd9308236121019733517eeaea421)
- [TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0baf746faaf0b368fd076190aebde47097a)
- [TRANSPORT_MGMT_ERR_TRANSPORT_INCOMING_TRANSPORT_ALREADY_BRIDGED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0babcf4a53c480f3e80b5aab929d83d29e8)
- [TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_TRANSPORT_ALREADY_BRIDGED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba0fde105d8cd7cbf0a8781faa9db8136d)
- [TRANSPORT_MGMT_ERR_CONNECT_MISSING_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba684cfd90f80df815703e5db5f19cc32b)
- [TRANSPORT_MGMT_ERR_CONNECT_INVALID_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba33a1996969a80f586aa07b5579825dee)
- [TRANSPORT_MGMT_ERR_CONNECT_UNSUPPORTED_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba05be247bbd2ed96809ca856d71d0e88f)
- [TRANSPORT_MGMT_ERR_CONNECT_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba8654385eede95aa8c1d42be55f442bec)
- [transport_mgmt_config_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga20cae62e5a2ff1edd8bd47c09bedb899)
- [TRANSPORT_MGMT_CONFIG_TYPE_UINT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899a4791f3585507952d1a86aa9eafb5f1af)
- [TRANSPORT_MGMT_CONFIG_TYPE_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899abea44b2b3b70a48bce31d6ae07ff7977)
- [TRANSPORT_MGMT_CONFIG_TYPE_BOOL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899a4541d5558c4049f81f1436c4fc7f53e3)
- [TRANSPORT_MGMT_CONFIG_TYPE_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899ab3bedc6db7e1da2334c5c7af64fa68e5)
- [TRANSPORT_MGMT_CONFIG_TYPE_BYTE_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899a71b75164c2408986e43093e817a15532)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [transport_mgmt_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga63d8fff2d408a31503fd7d9900d014f8)
- [smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html)
- [mgmt_defines.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h.html)

---

[上一章](P227_tm6605.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P229_arch_inlines.h_源码浏览.md)
