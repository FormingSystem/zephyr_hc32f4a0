---
id: learning.zephyr-docs.api-source-configuration-reference.page-14
title: csip.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/csip_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_csip.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h.html)。

## 14.1\_原始可见代码（Source Code）

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
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00105"></a>
<a id="l00105"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="foldopen00139"></a>
<a id="l00139"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="foldopen00275"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="foldopen00361"></a>
<a id="l00361"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="foldopen00394"></a>
<a id="l00394"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="foldopen00403"></a>
<a id="l00403"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="foldopen00519"></a>
<a id="l00519"></a>
<a id="l00521"></a>
<a id="l00523"></a>
<a id="l00525"></a>
<a id="l00527"></a>
<a id="l00529"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00537"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00643"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="aaddr_8h_html"></a>
<a id="aassigned__numbers_8h_html"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="adata_8h_html"></a>
<a id="agap_8h_html"></a>
<a id="agroup__bt__csip_html_ga08c514fda44e5a9b5cfc16be629c2b37"></a>
<a id="agroup__bt__csip_html_ga0f2e0b610a4db975a72c6d9a645964cb"></a>
<a id="agroup__bt__csip_html_ga2ce69e3bf51622fd41389a12d26e2ba9"></a>
<a id="agroup__bt__csip_html_ga2d61e25d131631479e34a2c2edf3ebfa"></a>
<a id="agroup__bt__csip_html_ga33069821c84e9b4c16c9d95d88c23158"></a>
<a id="agroup__bt__csip_html_ga42702049524f7ce24dfb6061120414df"></a>
<a id="agroup__bt__csip_html_ga5391b625fbcfd66ab07e014659dc2e45"></a>
<a id="agroup__bt__csip_html_ga5b0149fec5d38e7003593c227b561506"></a>
<a id="agroup__bt__csip_html_ga6b35d73b102ef7b1db26dbd86aaf6a36"></a>
<a id="agroup__bt__csip_html_ga7e7ea4a92bb76aded86807571a2cbb73"></a>
<a id="agroup__bt__csip_html_ga8c3666d8f20f909dd4fa2010ae02c9a5"></a>
<a id="agroup__bt__csip_html_ga95e2ba4b65ec42eedb26bf5ad181b606"></a>
<a id="agroup__bt__csip_html_ga991ee886c814e0b72fa12ed58ef4a90b"></a>
<a id="agroup__bt__csip_html_ga994431ea69920d9e84f35ca6e1e5f634"></a>
<a id="agroup__bt__csip_html_ga9a897ace4906a5df99cffd6cabc1b3e5"></a>
<a id="agroup__bt__csip_html_ga9ee48e36fb33ee27e689d32f08f071a1"></a>
<a id="agroup__bt__csip_html_gab11184ace9246d4c5ead6bdc98ffa2ac"></a>
<a id="agroup__bt__csip_html_gabc8d9c8d2b2f73f5e18e7fdbce95389c"></a>
<a id="agroup__bt__csip_html_gacd83494562a62fbdbc7282107d4454b4"></a>
<a id="agroup__bt__csip_html_gacdb98c9ae3248064e90352387df7cef2"></a>
<a id="agroup__bt__csip_html_gad80917089bc7e629cc3cb9d7fbf6cf45"></a>
<a id="agroup__bt__csip_html_gae020da1a92d3babf47954c12dbbde56b"></a>
<a id="agroup__bt__csip_html_gaee24f364c90cdcd0b6f49c8b297a34a7"></a>
<a id="agroup__bt__csip_html_gaeee5f0691ba0d63a370ac5dd94cb4d5c"></a>
<a id="agroup__bt__csip_html_gaef51ab05dbe9d8a69674f7020e8f837f"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="akernel_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__addr__le__t_html"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__csip__set__coordinator__cb_html"></a>
<a id="astructbt__csip__set__coordinator__cb_html_a25474d60bcd8ee07ef3691554d9bd7ba"></a>
<a id="astructbt__csip__set__coordinator__cb_html_a5bb08e8ce5759f67d2ff02459efe114d"></a>
<a id="astructbt__csip__set__coordinator__cb_html_a724060375ef6f53fcdbabcc12032a4b0"></a>
<a id="astructbt__csip__set__coordinator__cb_html_ab328cf27c2966d7762d82ffb0d334d68"></a>
<a id="astructbt__csip__set__coordinator__cb_html_acc1efc493dd05f14fdc010240982e0de"></a>
<a id="astructbt__csip__set__coordinator__cb_html_adfa831556d13dbda8f06f69f69f9cac1"></a>
<a id="astructbt__csip__set__coordinator__cb_html_ae8cf52f1ace4ea1d56ec2204c59bb71c"></a>
<a id="astructbt__csip__set__coordinator__csis__inst_html"></a>
<a id="astructbt__csip__set__coordinator__csis__inst_html_a0c407932ad1fb5e36cd19daf28bac96d"></a>
<a id="astructbt__csip__set__coordinator__csis__inst_html_a7e7210dded5a084c5d45f9209895e37f"></a>
<a id="astructbt__csip__set__coordinator__set__info_html"></a>
<a id="astructbt__csip__set__coordinator__set__info_html_a362fd6d8afbde9eb77d4f9a47aecb03c"></a>
<a id="astructbt__csip__set__coordinator__set__info_html_aa5e41081508a13948f4c899d1212e2bf"></a>
<a id="astructbt__csip__set__coordinator__set__info_html_aa85b6a24ea8f020bb1312065e461c4b2"></a>
<a id="astructbt__csip__set__coordinator__set__info_html_ac969998670d04d6dea96ea6f666f3fc9"></a>
<a id="astructbt__csip__set__coordinator__set__member_html"></a>
<a id="astructbt__csip__set__coordinator__set__member_html_ac883b4348d5620b5315eeb4d32ea0260"></a>
<a id="astructbt__csip__set__member__cb_html"></a>
<a id="astructbt__csip__set__member__cb_html_a30b2f68aff4b75ffcc8e9d7e2de2afd9"></a>
<a id="astructbt__csip__set__member__cb_html_a46e18120caf78788f0928ada2c92ca5c"></a>
<a id="astructbt__csip__set__member__register__param_html"></a>
<a id="astructbt__csip__set__member__register__param_html_a1878a8d50ab190920435aaef611b69f1"></a>
<a id="astructbt__csip__set__member__register__param_html_a7b74ebf8608ba0a9c50d83d414ff15b2"></a>
<a id="astructbt__csip__set__member__register__param_html_abc87df6590e3c55a2cd860f86398346d"></a>
<a id="astructbt__csip__set__member__register__param_html_aeba89480776db362a9c9406dc3a9a945"></a>
<a id="astructbt__csip__set__member__register__param_html_af38436c47f52ec285cadb5d23c67ea0a"></a>
<a id="astructbt__csip__set__member__register__param_html_af8814b6e0695001e0a70025f5c2b4e83"></a>
<a id="astructbt__csip__set__member__set__info_html"></a>
<a id="astructbt__csip__set__member__set__info_html_a52ba91f4e3ee911f575160355368aae5"></a>
<a id="astructbt__csip__set__member__set__info_html_a75ca9b78932626f167b186b203611c27"></a>
<a id="astructbt__csip__set__member__set__info_html_a9ca9136177d15d68e4cabab2bce43540"></a>
<a id="astructbt__csip__set__member__set__info_html_aa715eda78908c603ec11a48846018845"></a>
<a id="astructbt__csip__set__member__set__info_html_ae0e082aac881500f2005489d6aa88090"></a>
<a id="astructbt__csip__set__member__set__info_html_afcb0ae1252ca6ac09fbdaaf5c8ae8dfa"></a>
<a id="astructbt__csip__set__member__svc__inst_html"></a>
<a id="astructbt__data_html"></a>
<a id="astructbt__gatt__service_html"></a>

```c


/*
 * Copyright (c) 2021-2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CSIP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CSIP_H_


#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/gap.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_CSIP_SET_COORDINATOR_DISCOVER_TIMER_VALUE        K_SECONDS(10)

#if defined(CONFIG_BT_CSIP_SET_COORDINATOR)
#define BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES CONFIG_BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES
#else
#define BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES 0U
#endif /* CONFIG_BT_CSIP_SET_COORDINATOR */

#define BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT        0x00U
#define BT_CSIP_READ_SIRK_REQ_RSP_ACCEPT_ENC    0x01U
#define BT_CSIP_READ_SIRK_REQ_RSP_REJECT        0x02U
#define BT_CSIP_READ_SIRK_REQ_RSP_OOB_ONLY      0x03U

#define BT_CSIP_SIRK_SIZE                       16U

#define BT_CSIP_RSI_SIZE                        6U

/* Coordinate Set Identification Service Error codes */
#define BT_CSIP_ERROR_LOCK_DENIED               0x80U
#define BT_CSIP_ERROR_LOCK_RELEASE_DENIED       0x81U
#define BT_CSIP_ERROR_LOCK_INVAL_VALUE          0x82U
#define BT_CSIP_ERROR_SIRK_OOB_ONLY             0x83U
#define BT_CSIP_ERROR_LOCK_ALREADY_GRANTED      0x84U

#define BT_CSIP_DATA_RSI(_rsi) BT_DATA(BT_DATA_CSIS_RSI, _rsi, BT_CSIP_RSI_SIZE)

struct bt_csip_set_member_svc_inst;

struct bt_csip_set_member_cb {
        void (*lock_changed)(struct bt_conn *conn,
                             struct bt_csip_set_member_svc_inst *svc_inst,
                             bool locked);

        uint8_t (*sirk_read_req)(struct bt_conn *conn,
                                 struct bt_csip_set_member_svc_inst *svc_inst);
};

struct bt_csip_set_member_register_param {
        uint8_t set_size;

        uint8_t sirk[BT_CSIP_SIRK_SIZE];

        bool lockable;

        uint8_t rank;

        struct bt_csip_set_member_cb *cb;

#if CONFIG_BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT > 1 || defined(__DOXYGEN__)
        const struct bt_gatt_service *parent;
#endif /* CONFIG_BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT > 1 */
};

void *bt_csip_set_member_svc_decl_get(const struct bt_csip_set_member_svc_inst *svc_inst);

int bt_csip_set_member_register(const struct bt_csip_set_member_register_param *param,
                                struct bt_csip_set_member_svc_inst **svc_inst);

int bt_csip_set_member_unregister(struct bt_csip_set_member_svc_inst *svc_inst);

int bt_csip_set_member_sirk(struct bt_csip_set_member_svc_inst *svc_inst,
                            const uint8_t sirk[BT_CSIP_SIRK_SIZE]);

int bt_csip_set_member_set_size_and_rank(struct bt_csip_set_member_svc_inst *svc_inst, uint8_t size,
                                         uint8_t rank);

struct bt_csip_set_member_set_info {
        uint8_t sirk[BT_CSIP_SIRK_SIZE];

        uint8_t set_size;

        uint8_t rank;

        bool lockable: 1;

        bool locked: 1;

        bt_addr_le_t lock_client_addr;
};

int bt_csip_set_member_get_info(const struct bt_csip_set_member_svc_inst *svc_inst,
                                struct bt_csip_set_member_set_info *info);

int bt_csip_set_member_generate_rsi(const struct bt_csip_set_member_svc_inst *svc_inst,
                                    uint8_t rsi[BT_CSIP_RSI_SIZE]);

int bt_csip_set_member_lock(struct bt_csip_set_member_svc_inst *svc_inst,
                            bool lock, bool force);

struct bt_csip_set_coordinator_set_info {
        uint8_t sirk[BT_CSIP_SIRK_SIZE];

        uint8_t set_size;

        uint8_t rank;

        bool lockable;
};

struct bt_csip_set_coordinator_csis_inst {
        struct bt_csip_set_coordinator_set_info info;

        void *svc_inst;
};

struct bt_csip_set_coordinator_set_member {
        struct bt_csip_set_coordinator_csis_inst insts[BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES];
};

typedef void (*bt_csip_set_coordinator_discover_cb)(
        struct bt_conn *conn,
        const struct bt_csip_set_coordinator_set_member *member,
        int err, size_t set_count);

int bt_csip_set_coordinator_discover(struct bt_conn *conn);

struct bt_csip_set_coordinator_set_member *
bt_csip_set_coordinator_set_member_by_conn(const struct bt_conn *conn);

typedef void (*bt_csip_set_coordinator_lock_set_cb)(int err);

typedef void (*bt_csip_set_coordinator_lock_changed_cb)(
        struct bt_csip_set_coordinator_csis_inst *inst, bool locked);

typedef void (*bt_csip_set_coordinator_sirk_changed_cb)(
        struct bt_csip_set_coordinator_csis_inst *inst);

typedef void (*bt_csip_set_coordinator_size_changed_cb)(
        struct bt_conn *conn, const struct bt_csip_set_coordinator_csis_inst *inst);

typedef void (*bt_csip_set_coordinator_ordered_access_cb_t)(
        const struct bt_csip_set_coordinator_set_info *set_info,
        int err, bool locked,
        struct bt_csip_set_coordinator_set_member *member);

struct bt_csip_set_coordinator_cb {
        bt_csip_set_coordinator_discover_cb discover;
        bt_csip_set_coordinator_lock_set_cb lock_set;
        bt_csip_set_coordinator_lock_set_cb release_set;
        bt_csip_set_coordinator_lock_changed_cb lock_changed;
        bt_csip_set_coordinator_sirk_changed_cb sirk_changed;
        bt_csip_set_coordinator_size_changed_cb size_changed;
        bt_csip_set_coordinator_ordered_access_cb_t ordered_access;

        sys_snode_t _node;
};

bool bt_csip_set_coordinator_is_set_member(const uint8_t sirk[BT_CSIP_SIRK_SIZE],
                                           struct bt_data *data);

int bt_csip_set_coordinator_register_cb(struct bt_csip_set_coordinator_cb *cb);

typedef bool (*bt_csip_set_coordinator_ordered_access_t)(
        const struct bt_csip_set_coordinator_set_info *set_info,
        struct bt_csip_set_coordinator_set_member *members[],
        size_t count);

int bt_csip_set_coordinator_ordered_access(
        const struct bt_csip_set_coordinator_set_member *members[],
        uint8_t count,
        const struct bt_csip_set_coordinator_set_info *set_info,
        bt_csip_set_coordinator_ordered_access_t cb);

int bt_csip_set_coordinator_lock(const struct bt_csip_set_coordinator_set_member **members,
                                 uint8_t count,
                                 const struct bt_csip_set_coordinator_set_info *set_info);

int bt_csip_set_coordinator_release(const struct bt_csip_set_coordinator_set_member **members,
                                    uint8_t count,
                                    const struct bt_csip_set_coordinator_set_info *set_info);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CSIP_H_ */
```

## 14.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2021-2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 59 行

条件编译配置（Configuration）标记：`CONFIG_BT_CSIP_SET_COORDINATOR`。

### 注释 3：原第 76 行

协调集标识服务错误码（Coordinate Set Identification Service Error codes）。

### 注释 4：原第 193 行

条件编译表达式：`CONFIG_BT_CSIP_SET_MEMBER_MAX_INSTANCE_COUNT > 1`。

### 注释 5：原第 652 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CSIP_H_`。

## 14.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [zephyr/bluetooth/gap.h](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)
- [bt_csip_set_member_cb](../bluetooth_service_model_reference/P059_bt_csip_set_member_cb_结构体.md)
- [lock_changed](../bluetooth_service_model_reference/P059_bt_csip_set_member_cb_结构体.md#a46e18120caf78788f0928ada2c92ca5c)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sirk_read_req](../bluetooth_service_model_reference/P059_bt_csip_set_member_cb_结构体.md#a30b2f68aff4b75ffcc8e9d7e2de2afd9)
- [bt_csip_set_member_register_param](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md)
- [set_size](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#af8814b6e0695001e0a70025f5c2b4e83)
- [sirk](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#aeba89480776db362a9c9406dc3a9a945)
- [BT_CSIP_SIRK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga33069821c84e9b4c16c9d95d88c23158)
- [lockable](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#abc87df6590e3c55a2cd860f86398346d)
- [rank](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#af38436c47f52ec285cadb5d23c67ea0a)
- [cb](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#a1878a8d50ab190920435aaef611b69f1)
- [bt_gatt_service](../bluetooth_connection_model_reference/P065_bt_gatt_service_结构体.md)
- [parent](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#a7b74ebf8608ba0a9c50d83d414ff15b2)
- [bt_csip_set_member_svc_decl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gabc8d9c8d2b2f73f5e18e7fdbce95389c)
- [bt_csip_set_member_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gab11184ace9246d4c5ead6bdc98ffa2ac)
- [bt_csip_set_member_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga9ee48e36fb33ee27e689d32f08f071a1)
- [bt_csip_set_member_sirk](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga9a897ace4906a5df99cffd6cabc1b3e5)
- [bt_csip_set_member_set_size_and_rank](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaef51ab05dbe9d8a69674f7020e8f837f)
- [bt_csip_set_member_set_info](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md)
- [sirk](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#a9ca9136177d15d68e4cabab2bce43540)
- [set_size](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#afcb0ae1252ca6ac09fbdaaf5c8ae8dfa)
- [rank](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#aa715eda78908c603ec11a48846018845)
- [lockable](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#a52ba91f4e3ee911f575160355368aae5)
- [locked](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#ae0e082aac881500f2005489d6aa88090)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [lock_client_addr](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#a75ca9b78932626f167b186b203611c27)
- [bt_csip_set_member_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gad80917089bc7e629cc3cb9d7fbf6cf45)
- [bt_csip_set_member_generate_rsi](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gae020da1a92d3babf47954c12dbbde56b)
- [BT_CSIP_RSI_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga5b0149fec5d38e7003593c227b561506)
- [bt_csip_set_member_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga95e2ba4b65ec42eedb26bf5ad181b606)
- [bt_csip_set_coordinator_set_info](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md)
- [sirk](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md#aa5e41081508a13948f4c899d1212e2bf)
- [set_size](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md#ac969998670d04d6dea96ea6f666f3fc9)
- [rank](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md#a362fd6d8afbde9eb77d4f9a47aecb03c)
- [lockable](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md#aa85b6a24ea8f020bb1312065e461c4b2)
- [bt_csip_set_coordinator_csis_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md)
- [info](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md#a0c407932ad1fb5e36cd19daf28bac96d)
- [svc_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md#a7e7210dded5a084c5d45f9209895e37f)
- [bt_csip_set_coordinator_set_member](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md)
- [insts](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md#ac883b4348d5620b5315eeb4d32ea0260)
- [BT_CSIP_SET_COORDINATOR_MAX_CSIS_INSTANCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga42702049524f7ce24dfb6061120414df)
- [bt_csip_set_coordinator_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaeee5f0691ba0d63a370ac5dd94cb4d5c)
- [bt_csip_set_coordinator_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga7e7ea4a92bb76aded86807571a2cbb73)
- [bt_csip_set_coordinator_set_member_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga8c3666d8f20f909dd4fa2010ae02c9a5)
- [bt_csip_set_coordinator_lock_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga994431ea69920d9e84f35ca6e1e5f634)
- [bt_csip_set_coordinator_lock_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga991ee886c814e0b72fa12ed58ef4a90b)
- [bt_csip_set_coordinator_sirk_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gacdb98c9ae3248064e90352387df7cef2)
- [bt_csip_set_coordinator_size_changed_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaee24f364c90cdcd0b6f49c8b297a34a7)
- [bt_csip_set_coordinator_ordered_access_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga0f2e0b610a4db975a72c6d9a645964cb)
- [bt_csip_set_coordinator_cb](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md)
- [discover](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#a724060375ef6f53fcdbabcc12032a4b0)
- [lock_set](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#a25474d60bcd8ee07ef3691554d9bd7ba)
- [release_set](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#acc1efc493dd05f14fdc010240982e0de)
- [lock_changed](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#adfa831556d13dbda8f06f69f69f9cac1)
- [sirk_changed](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#a5bb08e8ce5759f67d2ff02459efe114d)
- [size_changed](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#ab328cf27c2966d7762d82ffb0d334d68)
- [ordered_access](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#ae8cf52f1ace4ea1d56ec2204c59bb71c)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_csip_set_coordinator_is_set_member](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga6b35d73b102ef7b1db26dbd86aaf6a36)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [bt_csip_set_coordinator_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga08c514fda44e5a9b5cfc16be629c2b37)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_csip_set_coordinator_ordered_access_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga2ce69e3bf51622fd41389a12d26e2ba9)
- [bt_csip_set_coordinator_ordered_access](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gacd83494562a62fbdbc7282107d4454b4)
- [bt_csip_set_coordinator_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga2d61e25d131631479e34a2c2edf3ebfa)
- [bt_csip_set_coordinator_release](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga5391b625fbcfd66ab07e014659dc2e45)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [gap.h](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_csip_set_coordinator_cb::lock_set](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#a25474d60bcd8ee07ef3691554d9bd7ba)
- [bt_csip_set_coordinator_cb::sirk_changed](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#a5bb08e8ce5759f67d2ff02459efe114d)
- [bt_csip_set_coordinator_cb::discover](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#a724060375ef6f53fcdbabcc12032a4b0)
- [bt_csip_set_coordinator_cb::size_changed](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#ab328cf27c2966d7762d82ffb0d334d68)
- [bt_csip_set_coordinator_cb::release_set](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#acc1efc493dd05f14fdc010240982e0de)
- [bt_csip_set_coordinator_cb::lock_changed](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#adfa831556d13dbda8f06f69f69f9cac1)
- [bt_csip_set_coordinator_cb::ordered_access](../bluetooth_service_model_reference/P055_bt_csip_set_coordinator_cb_结构体.md#ae8cf52f1ace4ea1d56ec2204c59bb71c)
- [bt_csip_set_coordinator_csis_inst::info](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md#a0c407932ad1fb5e36cd19daf28bac96d)
- [bt_csip_set_coordinator_csis_inst::svc_inst](../bluetooth_service_model_reference/P056_bt_csip_set_coordinator_csis_inst_结构体.md#a7e7210dded5a084c5d45f9209895e37f)
- [bt_csip_set_coordinator_set_info::rank](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md#a362fd6d8afbde9eb77d4f9a47aecb03c)
- [bt_csip_set_coordinator_set_info::sirk](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md#aa5e41081508a13948f4c899d1212e2bf)
- [bt_csip_set_coordinator_set_info::lockable](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md#aa85b6a24ea8f020bb1312065e461c4b2)
- [bt_csip_set_coordinator_set_info::set_size](../bluetooth_service_model_reference/P057_bt_csip_set_coordinator_set_info_结构体.md#ac969998670d04d6dea96ea6f666f3fc9)
- [bt_csip_set_coordinator_set_member::insts](../bluetooth_service_model_reference/P058_bt_csip_set_coordinator_set_member_结构体.md#ac883b4348d5620b5315eeb4d32ea0260)
- [bt_csip_set_member_cb::sirk_read_req](../bluetooth_service_model_reference/P059_bt_csip_set_member_cb_结构体.md#a30b2f68aff4b75ffcc8e9d7e2de2afd9)
- [bt_csip_set_member_cb::lock_changed](../bluetooth_service_model_reference/P059_bt_csip_set_member_cb_结构体.md#a46e18120caf78788f0928ada2c92ca5c)
- [bt_csip_set_member_register_param::cb](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#a1878a8d50ab190920435aaef611b69f1)
- [bt_csip_set_member_register_param::parent](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#a7b74ebf8608ba0a9c50d83d414ff15b2)
- [bt_csip_set_member_register_param::lockable](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#abc87df6590e3c55a2cd860f86398346d)
- [bt_csip_set_member_register_param::sirk](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#aeba89480776db362a9c9406dc3a9a945)
- [bt_csip_set_member_register_param::rank](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#af38436c47f52ec285cadb5d23c67ea0a)
- [bt_csip_set_member_register_param::set_size](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md#af8814b6e0695001e0a70025f5c2b4e83)
- [bt_csip_set_member_set_info::lockable](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#a52ba91f4e3ee911f575160355368aae5)
- [bt_csip_set_member_set_info::lock_client_addr](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#a75ca9b78932626f167b186b203611c27)
- [bt_csip_set_member_set_info::sirk](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#a9ca9136177d15d68e4cabab2bce43540)
- [bt_csip_set_member_set_info::rank](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#aa715eda78908c603ec11a48846018845)
- [bt_csip_set_member_set_info::locked](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#ae0e082aac881500f2005489d6aa88090)
- [bt_csip_set_member_set_info::set_size](../bluetooth_service_model_reference/P061_bt_csip_set_member_set_info_结构体.md#afcb0ae1252ca6ac09fbdaaf5c8ae8dfa)

---

[上一章](P013_ch570-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P015_ctype.h_源码浏览.md)
