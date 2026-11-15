---
id: learning.zephyr-docs.api-source-reference.page-306
title: has.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/has_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第306章\_has.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/has_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/has_8h.html)。

## 306.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
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
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00071"></a>
<a id="l00076"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="foldopen00314"></a>
<a id="l00314"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="foldopen00344"></a>
<a id="l00344"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="foldopen00487"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="agroup__bt__has_html_ga0bf932a9a1977e4d1926c11242c7b70d"></a>
<a id="agroup__bt__has_html_ga2c0fe62baa63b72703d6f553f1de072b"></a>
<a id="agroup__bt__has_html_ga39f9ac2f94b1febe8e834ae54e110e90"></a>
<a id="agroup__bt__has_html_ga3a564b18ce6cbc7a5af970474ddf25a2"></a>
<a id="agroup__bt__has_html_ga462679b8b5c91762c6d1daf03c5675d0"></a>
<a id="agroup__bt__has_html_ga4a228ee29a26346867a6427f81816336"></a>
<a id="agroup__bt__has_html_ga50d470390967317cb84b17fd450546a4"></a>
<a id="agroup__bt__has_html_ga54ef9918e4fb458b7416ffb94acca808"></a>
<a id="agroup__bt__has_html_ga66943cb5275ca660f2eab11e37708d81"></a>
<a id="agroup__bt__has_html_ga6f06adc529a500fcfcfea2ae89ea60d5"></a>
<a id="agroup__bt__has_html_ga715cfe5bd08fbd4557ee6052b38f27de"></a>
<a id="agroup__bt__has_html_ga7b8913a9f9bc4d5c066582780adcf274"></a>
<a id="agroup__bt__has_html_ga7e37a89b1bf0a732045276cf6b922956"></a>
<a id="agroup__bt__has_html_ga8303b5fb2558a35bb2cb06cd5788e636"></a>
<a id="agroup__bt__has_html_ga9bc61dfc710070fb136120944c0776b9"></a>
<a id="agroup__bt__has_html_gaa9572a32f912c8fe529b510aa23f4540"></a>
<a id="agroup__bt__has_html_gabe523e1aefc789ad0031e3c0efb27379"></a>
<a id="agroup__bt__has_html_gac39ca2d72273bd591618d186b48c20b0"></a>
<a id="agroup__bt__has_html_gacaa997913949b6ea98c5c6233fefdc52"></a>
<a id="agroup__bt__has_html_gadf0a488721910633fa2b54b2c7645bd9"></a>
<a id="agroup__bt__has_html_gae1787671fac3b7873c5994adc7d19b20"></a>
<a id="agroup__bt__has_html_gaf3765300072b0a6d1ee45699e710d4da"></a>
<a id="agroup__bt__has_html_gaf83c83d9f2c9575e48455b975c4266ce"></a>
<a id="agroup__bt__has_html_gga50d470390967317cb84b17fd450546a4a885520fe7fa533b6ea79db7ebeeed258"></a>
<a id="agroup__bt__has_html_gga7b8913a9f9bc4d5c066582780adcf274a70645a9bfc628425b93b0aa6ce539173"></a>
<a id="agroup__bt__has_html_gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59"></a>
<a id="agroup__bt__has_html_gga7b8913a9f9bc4d5c066582780adcf274ad479ec0e277e2e894d0056965b484e09"></a>
<a id="agroup__bt__has_html_ggaa9572a32f912c8fe529b510aa23f4540a4b711ff711e81a22b7e80f7dc8a4aae8"></a>
<a id="agroup__bt__has_html_ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c"></a>
<a id="agroup__bt__has_html_ggaa9572a32f912c8fe529b510aa23f4540af9e7c56173aeeb593f9e12a0e3366a0b"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__has__client__cb_html"></a>
<a id="astructbt__has__client__cb_html_a1c28e7b5542100ce93727ac097cc6dee"></a>
<a id="astructbt__has__client__cb_html_a4217754818ad047f287aceda8326bf99"></a>
<a id="astructbt__has__client__cb_html_a50759c76add5f4f76e23e742ae3ebe1b"></a>
<a id="astructbt__has__client__cb_html_a903397650915f3335dd2b8cd4f51d293"></a>
<a id="astructbt__has__client__cb_html_aa54cf5f268e542947ffb30531b7702ba"></a>
<a id="astructbt__has__client__cb_html_acf35d62cce0c2181e2eefd8c43e3b568"></a>
<a id="astructbt__has__features__param_html"></a>
<a id="astructbt__has__features__param_html_a5ff95f2633bf577fc0f4c3d714d53bb1"></a>
<a id="astructbt__has__features__param_html_abcaf8630309bcae1a8184095c1eca656"></a>
<a id="astructbt__has__features__param_html_ada946ee62547349bc01054db5cafa279"></a>
<a id="astructbt__has__preset__ops_html"></a>
<a id="astructbt__has__preset__ops_html_a7f0069639eb3b1f8b0d290a752b68770"></a>
<a id="astructbt__has__preset__ops_html_aec9d0f01c03f02f0a6f124527b72235e"></a>
<a id="astructbt__has__preset__record_html"></a>
<a id="astructbt__has__preset__record_html_a68484827708a19a75f2cdf922f01e677"></a>
<a id="astructbt__has__preset__record_html_ac064f0ae2841627930fb3ca0370ef5ec"></a>
<a id="astructbt__has__preset__record_html_ad3fc652d24a8b625b97abb02f0fb66bb"></a>
<a id="astructbt__has__preset__register__param_html"></a>
<a id="astructbt__has__preset__register__param_html_a35b8d2e9a01198cc34350595c786f1ae"></a>
<a id="astructbt__has__preset__register__param_html_a6e480fb6337d363353ca7ba6f716cd71"></a>
<a id="astructbt__has__preset__register__param_html_a8273bbec14040a7dd67aeac14188b86b"></a>
<a id="astructbt__has__preset__register__param_html_a9a3ade943b4f7569577c092df3ec467c"></a>
<a id="astructbt__has_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2022 Codecoup
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_HAS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_HAS_H_


#include <stdint.h>
#include <stdbool.h>

#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_HAS_PRESET_INDEX_NONE 0x00U
#define BT_HAS_PRESET_INDEX_FIRST 0x01U
#define BT_HAS_PRESET_INDEX_LAST 0xFFU

#define BT_HAS_PRESET_NAME_MIN 1U
#define BT_HAS_PRESET_NAME_MAX 40U

struct bt_has;

enum bt_has_hearing_aid_type {
        BT_HAS_HEARING_AID_TYPE_BINAURAL = 0x00,
        BT_HAS_HEARING_AID_TYPE_MONAURAL = 0x01,
        BT_HAS_HEARING_AID_TYPE_BANDED = 0x02,
};

enum bt_has_properties {
        BT_HAS_PROP_NONE = 0,

        BT_HAS_PROP_WRITABLE = BIT(0U),

        BT_HAS_PROP_AVAILABLE = BIT(1U),
};

enum bt_has_capabilities {
        BT_HAS_PRESET_SUPPORT = BIT(0U),
};

struct bt_has_features_param {
        enum bt_has_hearing_aid_type type;

        bool preset_sync_support;

        bool independent_presets;
};

struct bt_has_preset_record {
        uint8_t index;

        enum bt_has_properties properties;

        const char *name;
};

struct bt_has_client_cb {
        void (*discover)(struct bt_conn *conn, int err, struct bt_has *has,
                         enum bt_has_hearing_aid_type type, enum bt_has_capabilities caps);

        void (*preset_switch)(struct bt_has *has, int err, uint8_t index);

        void (*preset_read_rsp)(struct bt_has *has, int err,
                                const struct bt_has_preset_record *record, bool is_last);

        void (*preset_update)(struct bt_has *has, uint8_t index_prev,
                              const struct bt_has_preset_record *record, bool is_last);

        void (*preset_deleted)(struct bt_has *has, uint8_t index, bool is_last);

        void (*preset_availability)(struct bt_has *has, uint8_t index, bool available,
                                    bool is_last);
};

int bt_has_client_cb_register(const struct bt_has_client_cb *cb);

int bt_has_client_discover(struct bt_conn *conn);

int bt_has_client_conn_get(const struct bt_has *has, struct bt_conn **conn);

int bt_has_client_presets_read(struct bt_has *has, uint8_t index, uint8_t max_count);

int bt_has_client_preset_set(struct bt_has *has, uint8_t index, bool sync);

int bt_has_client_preset_next(struct bt_has *has, bool sync);

int bt_has_client_preset_prev(struct bt_has *has, bool sync);

struct bt_has_preset_ops {
        int (*select)(uint8_t index, bool sync);

        void (*name_changed)(uint8_t index, const char *name);
};

struct bt_has_preset_register_param {
        uint8_t index;

        enum bt_has_properties properties;

        const char *name;

        const struct bt_has_preset_ops *ops;
};

int bt_has_register(const struct bt_has_features_param *features);

int bt_has_preset_register(const struct bt_has_preset_register_param *param);

int bt_has_preset_unregister(uint8_t index);

int bt_has_preset_available(uint8_t index);

int bt_has_preset_unavailable(uint8_t index);

typedef bool (*bt_has_preset_func_t)(uint8_t index, enum bt_has_properties properties,
                                     const char *name, void *user_data);

int bt_has_preset_foreach(uint8_t index, bt_has_preset_func_t func, void *user_data);

int bt_has_preset_active_set(uint8_t index);

uint8_t bt_has_preset_active_get(void);

static inline int bt_has_preset_active_clear(void)
{
        return bt_has_preset_active_set(BT_HAS_PRESET_INDEX_NONE);
}

int bt_has_preset_name_change(uint8_t index, const char *name);

int bt_has_features_set(const struct bt_has_features_param *features);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_HAS_H_ */
```

## 306.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2022 Codecoup。

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 523 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_HAS_H_`。

## 306.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/has_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)
- [bt_has_hearing_aid_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaa9572a32f912c8fe529b510aa23f4540)
- [BT_HAS_HEARING_AID_TYPE_BINAURAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c)
- [BT_HAS_HEARING_AID_TYPE_MONAURAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ggaa9572a32f912c8fe529b510aa23f4540a4b711ff711e81a22b7e80f7dc8a4aae8)
- [BT_HAS_HEARING_AID_TYPE_BANDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ggaa9572a32f912c8fe529b510aa23f4540af9e7c56173aeeb593f9e12a0e3366a0b)
- [bt_has_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga7b8913a9f9bc4d5c066582780adcf274)
- [BT_HAS_PROP_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga7b8913a9f9bc4d5c066582780adcf274a70645a9bfc628425b93b0aa6ce539173)
- [BT_HAS_PROP_WRITABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga7b8913a9f9bc4d5c066582780adcf274ad479ec0e277e2e894d0056965b484e09)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_HAS_PROP_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59)
- [bt_has_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga50d470390967317cb84b17fd450546a4)
- [BT_HAS_PRESET_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga50d470390967317cb84b17fd450546a4a885520fe7fa533b6ea79db7ebeeed258)
- [bt_has_features_param](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md)
- [type](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md#abcaf8630309bcae1a8184095c1eca656)
- [preset_sync_support](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md#ada946ee62547349bc01054db5cafa279)
- [independent_presets](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md#a5ff95f2633bf577fc0f4c3d714d53bb1)
- [bt_has_preset_record](../bluetooth_service_model_reference/P081_bt_has_preset_record_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [index](../bluetooth_service_model_reference/P081_bt_has_preset_record_结构体.md#a68484827708a19a75f2cdf922f01e677)
- [properties](../bluetooth_service_model_reference/P081_bt_has_preset_record_结构体.md#ad3fc652d24a8b625b97abb02f0fb66bb)
- [name](../bluetooth_service_model_reference/P081_bt_has_preset_record_结构体.md#ac064f0ae2841627930fb3ca0370ef5ec)
- [bt_has_client_cb](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md)
- [discover](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#acf35d62cce0c2181e2eefd8c43e3b568)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [preset_switch](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#a4217754818ad047f287aceda8326bf99)
- [preset_read_rsp](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#a50759c76add5f4f76e23e742ae3ebe1b)
- [preset_update](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#aa54cf5f268e542947ffb30531b7702ba)
- [preset_deleted](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#a1c28e7b5542100ce93727ac097cc6dee)
- [preset_availability](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#a903397650915f3335dd2b8cd4f51d293)
- [bt_has_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga9bc61dfc710070fb136120944c0776b9)
- [bt_has_client_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaf3765300072b0a6d1ee45699e710d4da)
- [bt_has_client_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga8303b5fb2558a35bb2cb06cd5788e636)
- [bt_has_client_presets_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga54ef9918e4fb458b7416ffb94acca808)
- [bt_has_client_preset_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga4a228ee29a26346867a6427f81816336)
- [bt_has_client_preset_next](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga66943cb5275ca660f2eab11e37708d81)
- [bt_has_client_preset_prev](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga3a564b18ce6cbc7a5af970474ddf25a2)
- [bt_has_preset_ops](../bluetooth_service_model_reference/P080_bt_has_preset_ops_结构体.md)
- [select](../bluetooth_service_model_reference/P080_bt_has_preset_ops_结构体.md#aec9d0f01c03f02f0a6f124527b72235e)
- [name_changed](../bluetooth_service_model_reference/P080_bt_has_preset_ops_结构体.md#a7f0069639eb3b1f8b0d290a752b68770)
- [bt_has_preset_register_param](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md)
- [index](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md#a9a3ade943b4f7569577c092df3ec467c)
- [properties](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md#a8273bbec14040a7dd67aeac14188b86b)
- [name](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md#a35b8d2e9a01198cc34350595c786f1ae)
- [ops](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md#a6e480fb6337d363353ca7ba6f716cd71)
- [bt_has_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gac39ca2d72273bd591618d186b48c20b0)
- [bt_has_preset_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gadf0a488721910633fa2b54b2c7645bd9)
- [bt_has_preset_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga39f9ac2f94b1febe8e834ae54e110e90)
- [bt_has_preset_available](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gacaa997913949b6ea98c5c6233fefdc52)
- [bt_has_preset_unavailable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gabe523e1aefc789ad0031e3c0efb27379)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_has_preset_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaf83c83d9f2c9575e48455b975c4266ce)
- [bt_has_preset_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga0bf932a9a1977e4d1926c11242c7b70d)
- [bt_has_preset_active_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga2c0fe62baa63b72703d6f553f1de072b)
- [bt_has_preset_active_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gae1787671fac3b7873c5994adc7d19b20)
- [bt_has_preset_active_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga715cfe5bd08fbd4557ee6052b38f27de)
- [BT_HAS_PRESET_INDEX_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga462679b8b5c91762c6d1daf03c5675d0)
- [bt_has_preset_name_change](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga6f06adc529a500fcfcfea2ae89ea60d5)
- [bt_has_features_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga7e37a89b1bf0a732045276cf6b922956)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [bt_has_client_cb::preset_deleted](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#a1c28e7b5542100ce93727ac097cc6dee)
- [bt_has_client_cb::preset_switch](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#a4217754818ad047f287aceda8326bf99)
- [bt_has_client_cb::preset_read_rsp](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#a50759c76add5f4f76e23e742ae3ebe1b)
- [bt_has_client_cb::preset_availability](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#a903397650915f3335dd2b8cd4f51d293)
- [bt_has_client_cb::preset_update](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#aa54cf5f268e542947ffb30531b7702ba)
- [bt_has_client_cb::discover](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#acf35d62cce0c2181e2eefd8c43e3b568)
- [bt_has_features_param::independent_presets](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md#a5ff95f2633bf577fc0f4c3d714d53bb1)
- [bt_has_features_param::type](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md#abcaf8630309bcae1a8184095c1eca656)
- [bt_has_features_param::preset_sync_support](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md#ada946ee62547349bc01054db5cafa279)
- [bt_has_preset_ops::name_changed](../bluetooth_service_model_reference/P080_bt_has_preset_ops_结构体.md#a7f0069639eb3b1f8b0d290a752b68770)
- [bt_has_preset_ops::select](../bluetooth_service_model_reference/P080_bt_has_preset_ops_结构体.md#aec9d0f01c03f02f0a6f124527b72235e)
- [bt_has_preset_record::index](../bluetooth_service_model_reference/P081_bt_has_preset_record_结构体.md#a68484827708a19a75f2cdf922f01e677)
- [bt_has_preset_record::name](../bluetooth_service_model_reference/P081_bt_has_preset_record_结构体.md#ac064f0ae2841627930fb3ca0370ef5ec)
- [bt_has_preset_record::properties](../bluetooth_service_model_reference/P081_bt_has_preset_record_结构体.md#ad3fc652d24a8b625b97abb02f0fb66bb)
- [bt_has_preset_register_param::name](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md#a35b8d2e9a01198cc34350595c786f1ae)
- [bt_has_preset_register_param::ops](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md#a6e480fb6337d363353ca7ba6f716cd71)
- [bt_has_preset_register_param::properties](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md#a8273bbec14040a7dd67aeac14188b86b)
- [bt_has_preset_register_param::index](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md#a9a3ade943b4f7569577c092df3ec467c)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P305_h4.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P307_hawkbit.h_源码浏览.md)
