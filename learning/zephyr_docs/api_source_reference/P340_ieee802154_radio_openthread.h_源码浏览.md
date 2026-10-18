---
id: learning.zephyr-docs.api-source-reference.page-340
title: ieee802154_radio_openthread.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第340章\_ieee802154\_radio\_openthread.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html)。

## 340.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="foldopen00024"></a>
<a id="l00024"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00100"></a>
<a id="l00100"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="foldopen00146"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="foldopen00176"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="foldopen00200"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="agroup__ieee802154__driver_html_gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c"></a>
<a id="agroup__ieee802154__driver_html_ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2"></a>
<a id="agroup__ieee802154__driver_html_ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511"></a>
<a id="agroup__net__time_html_gaf1da332e3909fca30de991cc2f950e56"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="aieee802154__radio_8h_html"></a>
<a id="aieee802154__radio__openthread_8h_html_a038a7e158a73533b1fd55bb92e5fa64a"></a>
<a id="aieee802154__radio__openthread_8h_html_a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f"></a>
<a id="aieee802154__radio__openthread_8h_html_a15a4b5a53be4b2c867eb9551de7d914a"></a>
<a id="aieee802154__radio__openthread_8h_html_a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b"></a>
<a id="aieee802154__radio__openthread_8h_html_a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5"></a>
<a id="aieee802154__radio__openthread_8h_html_a80bc0d04ae7e2286abe372df49880ac8"></a>
<a id="aieee802154__radio__openthread_8h_html_a80bc0d04ae7e2286abe372df49880ac8a8cd0cafed5d27222aff18e42b1693c7f"></a>
<a id="aieee802154__radio__openthread_8h_html_a80bc0d04ae7e2286abe372df49880ac8a9a1663d68026c5156a0f127ae086adc8"></a>
<a id="aieee802154__radio__openthread_8h_html_a83674b259d4cf5c28827385b27a499e2"></a>
<a id="aieee802154__radio__openthread_8h_html_ab11e7d5ec46577a0259d68349ac19525"></a>
<a id="aieee802154__radio__openthread_8h_html_ab11e7d5ec46577a0259d68349ac19525a2b1436aa0d7fdded8fda38b4ee8f2af7"></a>
<a id="aieee802154__radio__openthread_8h_html_ab11e7d5ec46577a0259d68349ac19525a7ee21cd052527506e860b4a3bc772a04"></a>
<a id="aieee802154__radio__openthread_8h_html_ab11e7d5ec46577a0259d68349ac19525ac06ead66659fa9a736d368a9d255bc95"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructieee802154__attr__value_html"></a>
<a id="astructieee802154__config_html"></a>
<a id="astructieee802154__openthread__attr__value_html"></a>
<a id="astructieee802154__openthread__attr__value_html_a423bc2cc48ceead6a6febd7f78504843"></a>
<a id="astructieee802154__openthread__attr__value_html_a794c867bf25cd23b9b1797d995696c8a"></a>
<a id="astructieee802154__openthread__attr__value_html_a84f1a03b847ff2050f38a59573a00cd8"></a>
<a id="astructieee802154__openthread__config_html"></a>
<a id="astructieee802154__openthread__config_html_a29d3c8793578ba47124e1931077d8c98"></a>
<a id="astructieee802154__openthread__config_html_a774c58d56cf2cb37253051c346e67222"></a>
<a id="astructieee802154__openthread__config_html_ab18500f5926c8fb0bb068aca86b169d4"></a>
<a id="astructieee802154__openthread__config_html_ab4cbfdddf55a95958b9df1c0f9ac70f9"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_IEEE802154_RADIO_OPENTHREAD_H_
#define ZEPHYR_INCLUDE_NET_IEEE802154_RADIO_OPENTHREAD_H_

#include <zephyr/net/ieee802154_radio.h>

#define IEEE802154_OPENTHREAD_HW_CAPS_BITS_START IEEE802154_HW_CAPS_BITS_PRIV_START

enum ieee802154_openthread_hw_caps {
        IEEE802154_OPENTHREAD_HW_MULTIPLE_CCA = BIT(IEEE802154_OPENTHREAD_HW_CAPS_BITS_START),

        IEEE802154_OPENTHREAD_HW_CST = BIT(IEEE802154_OPENTHREAD_HW_CAPS_BITS_START + 1),
};

enum ieee802154_openthread_tx_mode {
        IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA = IEEE802154_TX_MODE_PRIV_START
};

enum ieee802154_openthread_config_type {
        IEEE802154_OPENTHREAD_CONFIG_MAX_EXTRA_CCA_ATTEMPTS  = IEEE802154_CONFIG_PRIV_START,

        IEEE802154_OPENTHREAD_CONFIG_CST_PERIOD,

        IEEE802154_OPENTHREAD_CONFIG_EXPECTED_TX_TIME,
};

#define IEEE802154_OPENTHREAD_THREAD_IE_VENDOR_OUI { 0x9b, 0xb8, 0xea }

#define IEEE802154_OPENTHREAD_VENDOR_OUI_LEN 3

struct ieee802154_openthread_config {
        union {
                struct ieee802154_config common;

                uint8_t max_extra_cca_attempts;

                uint32_t cst_period;

                net_time_t expected_tx_time;
        };
};

enum ieee802154_openthread_attr {

        IEEE802154_OPENTHREAD_ATTR_T_RECCA = IEEE802154_ATTR_PRIV_START,

        IEEE802154_OPENTHREAD_ATTR_T_CCATX
};

struct ieee802154_openthread_attr_value {
        union {
                struct ieee802154_attr_value common;

                uint16_t t_recca;

                uint16_t t_ccatx;

        };
};

#endif /* ZEPHYR_INCLUDE_NET_IEEE802154_RADIO_OPENTHREAD_H_ */
```

## 340.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 214 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_IEEE802154_RADIO_OPENTHREAD_H_`。

## 340.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html)
- [zephyr/net/ieee802154_radio.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h.html)
- [ieee802154_openthread_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a80bc0d04ae7e2286abe372df49880ac8)
- [IEEE802154_OPENTHREAD_HW_MULTIPLE_CCA](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a80bc0d04ae7e2286abe372df49880ac8a9a1663d68026c5156a0f127ae086adc8)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [IEEE802154_OPENTHREAD_HW_CAPS_BITS_START](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a83674b259d4cf5c28827385b27a499e2)
- [IEEE802154_OPENTHREAD_HW_CST](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a80bc0d04ae7e2286abe372df49880ac8a8cd0cafed5d27222aff18e42b1693c7f)
- [ieee802154_openthread_tx_mode](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a038a7e158a73533b1fd55bb92e5fa64a)
- [IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f)
- [IEEE802154_TX_MODE_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2)
- [ieee802154_openthread_config_type](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#ab11e7d5ec46577a0259d68349ac19525)
- [IEEE802154_OPENTHREAD_CONFIG_MAX_EXTRA_CCA_ATTEMPTS](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#ab11e7d5ec46577a0259d68349ac19525ac06ead66659fa9a736d368a9d255bc95)
- [IEEE802154_CONFIG_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c)
- [IEEE802154_OPENTHREAD_CONFIG_CST_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#ab11e7d5ec46577a0259d68349ac19525a2b1436aa0d7fdded8fda38b4ee8f2af7)
- [IEEE802154_OPENTHREAD_CONFIG_EXPECTED_TX_TIME](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#ab11e7d5ec46577a0259d68349ac19525a7ee21cd052527506e860b4a3bc772a04)
- [ieee802154_openthread_config](../network_core_model_reference/P037_ieee802154_openthread_config_结构体.md)
- [ieee802154_config](../network_core_model_reference/P014_ieee802154_config_结构体.md)
- [common](../network_core_model_reference/P037_ieee802154_openthread_config_结构体.md#ab18500f5926c8fb0bb068aca86b169d4)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [max_extra_cca_attempts](../network_core_model_reference/P037_ieee802154_openthread_config_结构体.md#ab4cbfdddf55a95958b9df1c0f9ac70f9)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [cst_period](../network_core_model_reference/P037_ieee802154_openthread_config_结构体.md#a774c58d56cf2cb37253051c346e67222)
- [net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)
- [expected_tx_time](../network_core_model_reference/P037_ieee802154_openthread_config_结构体.md#a29d3c8793578ba47124e1931077d8c98)
- [ieee802154_openthread_attr](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a15a4b5a53be4b2c867eb9551de7d914a)
- [IEEE802154_OPENTHREAD_ATTR_T_RECCA](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5)
- [IEEE802154_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511)
- [IEEE802154_OPENTHREAD_ATTR_T_CCATX](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b)
- [ieee802154_openthread_attr_value](../network_core_model_reference/P036_ieee802154_openthread_attr_value_结构体.md)
- [ieee802154_attr_value](../network_core_model_reference/P005_ieee802154_attr_value_结构体.md)
- [common](../network_core_model_reference/P036_ieee802154_openthread_attr_value_结构体.md#a794c867bf25cd23b9b1797d995696c8a)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [t_recca](../network_core_model_reference/P036_ieee802154_openthread_attr_value_结构体.md#a84f1a03b847ff2050f38a59573a00cd8)
- [t_ccatx](../network_core_model_reference/P036_ieee802154_openthread_attr_value_结构体.md#a423bc2cc48ceead6a6febd7f78504843)
- [ieee802154_radio.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h.html)
- [ieee802154_openthread_attr_value::t_ccatx](../network_core_model_reference/P036_ieee802154_openthread_attr_value_结构体.md#a423bc2cc48ceead6a6febd7f78504843)
- [ieee802154_openthread_attr_value::common](../network_core_model_reference/P036_ieee802154_openthread_attr_value_结构体.md#a794c867bf25cd23b9b1797d995696c8a)
- [ieee802154_openthread_attr_value::t_recca](../network_core_model_reference/P036_ieee802154_openthread_attr_value_结构体.md#a84f1a03b847ff2050f38a59573a00cd8)
- [ieee802154_openthread_config::expected_tx_time](../network_core_model_reference/P037_ieee802154_openthread_config_结构体.md#a29d3c8793578ba47124e1931077d8c98)
- [ieee802154_openthread_config::cst_period](../network_core_model_reference/P037_ieee802154_openthread_config_结构体.md#a774c58d56cf2cb37253051c346e67222)
- [ieee802154_openthread_config::common](../network_core_model_reference/P037_ieee802154_openthread_config_结构体.md#ab18500f5926c8fb0bb068aca86b169d4)
- [ieee802154_openthread_config::max_extra_cca_attempts](../network_core_model_reference/P037_ieee802154_openthread_config_结构体.md#ab4cbfdddf55a95958b9df1c0f9ac70f9)

---

[上一章](P339_ieee802154_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P341_if.h_源码浏览.md)
