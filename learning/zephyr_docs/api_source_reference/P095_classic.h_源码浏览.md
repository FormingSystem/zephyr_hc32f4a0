---
id: learning.zephyr-docs.api-source-reference.page-95
title: classic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/classic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第95章\_classic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h.html)。

## 95.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00020"></a>
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
<a id="l00042"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="foldopen00201"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00300"></a>
<a id="foldopen00302"></a>
<a id="l00302"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="foldopen00311"></a>
<a id="l00311"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00338"></a>
<a id="foldopen00339"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00353"></a>
<a id="foldopen00354"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="foldopen00365"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="foldopen00376"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="foldopen00388"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="foldopen00401"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="foldopen00414"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="foldopen00427"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="foldopen00478"></a>
<a id="l00478"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00502"></a>
<a id="l00504"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00511"></a>
<a id="foldopen00519"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="foldopen00529"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="foldopen00624"></a>
<a id="l00624"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="aaddr_8h_html"></a>
<a id="adata_8h_html"></a>
<a id="agroup__bt__gap_html_ga03757f934de6f13f95f02316b098875d"></a>
<a id="agroup__bt__gap_html_ga201f64881ccc13169d072d9cc04948ba"></a>
<a id="agroup__bt__gap_html_ga25ab96ac005237aee739bf32fc1aac94"></a>
<a id="agroup__bt__gap_html_ga2ec860d06c45098624b106b59fbab634"></a>
<a id="agroup__bt__gap_html_ga430de0ad30da7322c5353941f1f6a133"></a>
<a id="agroup__bt__gap_html_ga4c82193c50c616d9319c87ebcffabe66"></a>
<a id="agroup__bt__gap_html_ga567c71b49399fe7e1a5593edbf005e3a"></a>
<a id="agroup__bt__gap_html_ga66c29ea0ccb8b8ff5610c1fc53fe1eb9"></a>
<a id="agroup__bt__gap_html_ga6ca71da8c9eed3d317200aa1f6babc7d"></a>
<a id="agroup__bt__gap_html_ga78c5fc5f71d08b0c800967ee7696fc83"></a>
<a id="agroup__bt__gap_html_ga925f510c862c9a36539f4df1db0009d6"></a>
<a id="agroup__bt__gap_html_ga9760190192dde5c498ec96628468be8d"></a>
<a id="agroup__bt__gap_html_gab28ba977a94f63476f360d358868f8f6"></a>
<a id="agroup__bt__gap_html_gab49521adee2b653dbec04fbf833e22d9"></a>
<a id="agroup__bt__gap_html_gab661e90ad27ce1a280cefc15c5ad040c"></a>
<a id="agroup__bt__gap_html_gabfc34fe6f398d6526acc7c5afde8a689"></a>
<a id="agroup__bt__gap_html_gaccab07100ab64fd805fe1d468bc889ac"></a>
<a id="agroup__bt__gap_html_gad88cf1dec20264f9bdde91571efe8dce"></a>
<a id="agroup__bt__gap_html_gae3376fdd364e9b9d6e304ec589ba00f5"></a>
<a id="agroup__bt__gap_html_gga03757f934de6f13f95f02316b098875da53ce32b8981ffb385d1f680f11d8feb7"></a>
<a id="agroup__bt__gap_html_gga03757f934de6f13f95f02316b098875daac2a0585a4115768dcac602ffe87399d"></a>
<a id="agroup__bt__gap_html_ggabfc34fe6f398d6526acc7c5afde8a689a22574d1fc663afc2595ce8222867ee35"></a>
<a id="agroup__bt__gap_html_ggabfc34fe6f398d6526acc7c5afde8a689ab5ad28e0358b20440da3851278a69e97"></a>
<a id="agroup__bt__gap_html_ggabfc34fe6f398d6526acc7c5afde8a689ac01fd21779b5c5bcd883ab4f678ef26f"></a>
<a id="agroup__bt__gap_html_ggabfc34fe6f398d6526acc7c5afde8a689aee59dd0540295ce4313804ce08c07908"></a>
<a id="agroup__bt__gap_html_ggabfc34fe6f398d6526acc7c5afde8a689af1920d7300473810a412d508dfddf95a"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ahci__types_8h_html"></a>
<a id="ahci__types_8h_html_a08d4bdfc189bccbdb97a51b0089e77a0"></a>
<a id="ahci__types_8h_html_a0efddbffb31b93158b10a3f678f94f4e"></a>
<a id="ahci__types_8h_html_a150ea8f2095d8510bde3ebd65d521c29"></a>
<a id="ahci__types_8h_html_a366f85b3bcb3f578b2572149c69b7fc0"></a>
<a id="ahci__types_8h_html_a9ca37afd4638ef94cdd55302bd4c99b3"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astring_8h_html"></a>
<a id="astructbt__addr__t_html"></a>
<a id="astructbt__br__bond__info_html"></a>
<a id="astructbt__br__bond__info_html_aaa0a6ec8d7010b795a48825df7a8c744"></a>
<a id="astructbt__br__discovery__cb_html"></a>
<a id="astructbt__br__discovery__cb_html_a09c9f7258ea1739bf9330cf5c5bd882d"></a>
<a id="astructbt__br__discovery__cb_html_a3315f86bf3c9dbf339aa2254e0679182"></a>
<a id="astructbt__br__discovery__cb_html_a6ea814cabf9747cc7720ece9be59c8b9"></a>
<a id="astructbt__br__discovery__param_html"></a>
<a id="astructbt__br__discovery__param_html_a3087af0c5a264d50a27395d974f99e1e"></a>
<a id="astructbt__br__discovery__param_html_ac02d03f8cfdf4ad7aee3178e871cc105"></a>
<a id="astructbt__br__discovery__result_html"></a>
<a id="astructbt__br__discovery__result_html_a6bfe9a421257e2460eb9b4381252f9cc"></a>
<a id="astructbt__br__discovery__result_html_a833b05883132a0c20690f71b2c14a62a"></a>
<a id="astructbt__br__discovery__result_html_ad1f6bbfc27796e998ed30e307a251841"></a>
<a id="astructbt__br__discovery__result_html_aec239cbb82436ace39c8928a3baa0cf6"></a>
<a id="astructbt__br__inquiry__scan__param_html"></a>
<a id="astructbt__br__inquiry__scan__param_html_a23c55eeca21406ad038d2ff361405d2b"></a>
<a id="astructbt__br__inquiry__scan__param_html_a6a04891451c372f91b1c670f2a642b15"></a>
<a id="astructbt__br__inquiry__scan__param_html_adc90daed4bfa1bc40a8b179f02eaab46"></a>
<a id="astructbt__br__oob_html"></a>
<a id="astructbt__br__oob_html_a9b9f4c830a4e48736ac6b793d628ee98"></a>
<a id="astructbt__br__page__scan__param_html"></a>
<a id="astructbt__br__page__scan__param_html_a0f0cb7a792d2ec2ff7cc1d7bc6b01dce"></a>
<a id="astructbt__br__page__scan__param_html_a670129c10bc0c57684e00ce7835b1648"></a>
<a id="astructbt__br__page__scan__param_html_aab7cc81841af5461825dfe19a45dab3e"></a>
<a id="astructbt__data_html"></a>
<a id="asys_2util_8h_html"></a>

```c


/*
 * Copyright (c) 2015-2016 Intel Corporation
 * Copyright 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_CLASSIC_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_CLASSIC_H_


#include <stdbool.h>
#include <string.h>

#include <zephyr/sys/util.h>
#include <zephyr/net_buf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/hci_types.h>

#ifdef __cplusplus
extern "C" {
#endif


struct bt_br_discovery_priv {
        uint16_t clock_offset;
        uint8_t pscan_rep_mode;
        uint8_t resolve_state;
};

#define BT_BR_EIR_SIZE_MAX 240

struct bt_br_discovery_result {
        struct bt_br_discovery_priv _priv;

        bt_addr_t addr;

        int8_t rssi;

        uint8_t cod[3];

        uint8_t eir[BT_BR_EIR_SIZE_MAX];
};

struct bt_br_discovery_param {
        uint8_t length;

        bool limited;
};

int bt_br_discovery_start(const struct bt_br_discovery_param *param,
                          struct bt_br_discovery_result *results, size_t count);

int bt_br_discovery_stop(void);

struct bt_br_discovery_cb {

        void (*recv)(const struct bt_br_discovery_result *result);

        void (*timeout)(const struct bt_br_discovery_result *results,
                                  size_t count);

        sys_snode_t node;
};

void bt_br_discovery_cb_register(struct bt_br_discovery_cb *cb);

void bt_br_discovery_cb_unregister(struct bt_br_discovery_cb *cb);

struct bt_br_oob {
        bt_addr_t addr;
};

int bt_br_oob_get_local(struct bt_br_oob *oob);

int bt_br_set_discoverable(bool enable, bool limited);

enum bt_br_conn_req_rsp {
        BT_BR_CONN_REQ_ACCEPT_CENTRAL      = BT_HCI_ROLE_CENTRAL,
        BT_BR_CONN_REQ_ACCEPT_PERIPHERAL   = BT_HCI_ROLE_PERIPHERAL,
        BT_BR_CONN_REQ_REJECT_NO_RESOURCES = BT_HCI_ERR_INSUFFICIENT_RESOURCES,
        BT_BR_CONN_REQ_REJECT_SECURITY     = BT_HCI_ERR_INSUFFICIENT_SECURITY,
        BT_BR_CONN_REQ_REJECT_ADDR         = BT_HCI_ERR_BD_ADDR_UNACCEPTABLE,
};

typedef enum bt_br_conn_req_rsp (*bt_br_conn_req_func_t)(const bt_addr_t *addr, uint32_t cod);

int bt_br_set_connectable(bool enable, bt_br_conn_req_func_t func);

#define BT_BR_SCAN_INTERVAL_MIN 0x0012
#define BT_BR_SCAN_INTERVAL_MAX 0x1000

#define BT_BR_SCAN_WINDOW_MIN 0x0011
#define BT_BR_SCAN_WINDOW_MAX 0x1000


#define BT_BR_PAGE_SCAN_INTERVAL_R0 0x0800
#define BT_BR_PAGE_SCAN_WINDOW_R0   0x0800

#define BT_BR_PAGE_SCAN_FAST_INTERVAL_R1 0x00a0
#define BT_BR_PAGE_SCAN_FAST_WINDOW_R1   0x0011

#define BT_BR_PAGE_SCAN_MEDIUM_INTERVAL_R1 0x0800
#define BT_BR_PAGE_SCAN_MEDIUM_WINDOW_R1   0x0011

#define BT_BR_PAGE_SCAN_SLOW_INTERVAL_R1 0x0800
#define BT_BR_PAGE_SCAN_SLOW_WINDOW_R1   0x0011

#define BT_BR_PAGE_SCAN_FAST_INTERVAL_R2 0x1000
#define BT_BR_PAGE_SCAN_FAST_WINDOW_R2   0x0011

#define BT_BR_PAGE_SCAN_SLOW_INTERVAL_R2 0x1000
#define BT_BR_PAGE_SCAN_SLOW_WINDOW_R2   0x0011


enum bt_br_scan_type {
        BT_BR_SCAN_TYPE_STANDARD = 0,

        BT_BR_SCAN_TYPE_INTERLACED = 1,
};

struct bt_br_page_scan_param {
        uint16_t interval;

        uint16_t window;

        enum bt_br_scan_type type;
};


#define BT_BR_SCAN_INIT(_interval, _window, _type) \
{ \
        .interval = (_interval), \
        .window = (_window), \
        .type = (_type) \
}


#define BT_BR_PAGE_SCAN_PARAM(_interval, _window, _type) \
        ((const struct bt_br_page_scan_param[]) { \
                BT_BR_SCAN_INIT(_interval, _window, _type) \
        })

#define BT_BR_PAGE_SCAN_PARAM_R0 BT_BR_PAGE_SCAN_PARAM(BT_BR_PAGE_SCAN_INTERVAL_R0, \
                                                       BT_BR_PAGE_SCAN_WINDOW_R0, \
                                                       BT_BR_SCAN_TYPE_STANDARD)

#define BT_BR_PAGE_SCAN_PARAM_FAST_R1 \
        BT_BR_PAGE_SCAN_PARAM(BT_BR_PAGE_SCAN_FAST_INTERVAL_R1, \
        BT_BR_PAGE_SCAN_FAST_WINDOW_R1, \
        BT_BR_SCAN_TYPE_INTERLACED)

#define BT_BR_PAGE_SCAN_PARAM_MEDIUM_R1 \
        BT_BR_PAGE_SCAN_PARAM( \
        BT_BR_PAGE_SCAN_MEDIUM_INTERVAL_R1, \
        BT_BR_PAGE_SCAN_MEDIUM_WINDOW_R1, \
        BT_BR_SCAN_TYPE_INTERLACED)

#define BT_BR_PAGE_SCAN_PARAM_SLOW_R1 \
        BT_BR_PAGE_SCAN_PARAM( \
        BT_BR_PAGE_SCAN_SLOW_INTERVAL_R1, \
        BT_BR_PAGE_SCAN_SLOW_WINDOW_R1, \
        BT_BR_SCAN_TYPE_STANDARD)

#define BT_BR_PAGE_SCAN_PARAM_FAST_R2 \
        BT_BR_PAGE_SCAN_PARAM( \
        BT_BR_PAGE_SCAN_FAST_INTERVAL_R2, \
        BT_BR_PAGE_SCAN_FAST_WINDOW_R2, \
        BT_BR_SCAN_TYPE_INTERLACED)

#define BT_BR_PAGE_SCAN_PARAM_SLOW_R2 \
        BT_BR_PAGE_SCAN_PARAM( \
        BT_BR_PAGE_SCAN_SLOW_INTERVAL_R2, \
        BT_BR_PAGE_SCAN_SLOW_WINDOW_R2, \
        BT_BR_SCAN_TYPE_STANDARD)

int bt_br_page_scan_update_param(const struct bt_br_page_scan_param *param);

struct bt_br_inquiry_scan_param {
        uint16_t interval;

        uint16_t window;

        enum bt_br_scan_type type;
};


#define BT_BR_INQUIRY_SCAN_INTERVAL_DEFAULT 0x1000
#define BT_BR_INQUIRY_SCAN_WINDOW_DEFAULT   0x0012


#define BT_BR_INQUIRY_SCAN_PARAM(_interval, _window, _type)                                        \
        ((const struct bt_br_inquiry_scan_param[]){BT_BR_SCAN_INIT(_interval, _window, _type)})

#define BT_BR_INQUIRY_SCAN_PARAM_DEFAULT                                                           \
        BT_BR_INQUIRY_SCAN_PARAM(BT_BR_INQUIRY_SCAN_INTERVAL_DEFAULT,                              \
                                 BT_BR_INQUIRY_SCAN_WINDOW_DEFAULT, BT_BR_SCAN_TYPE_STANDARD)

int bt_br_inquiry_scan_update_param(const struct bt_br_inquiry_scan_param *param);

int bt_br_set_class_of_device(uint32_t cod);

int bt_br_get_class_of_device(uint32_t *cod);

bool bt_br_bond_exists(const bt_addr_t *addr);

int bt_br_unpair(const bt_addr_t *addr);

struct bt_br_bond_info {
        bt_addr_t addr;
};

void bt_br_foreach_bond(void (*func)(const struct bt_br_bond_info *info, void *user_data),
                        void *user_data);

int bt_br_write_eir(const struct bt_data *eir, size_t eir_count, bool fec_required);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_CLASSIC_H_ */
```

## 95.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015-2016 Intel Corporation。

版权（Copyright）：2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 662 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_CLASSIC_H_`。

## 95.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/bluetooth/data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_br_discovery_result](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [addr](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md#a833b05883132a0c20690f71b2c14a62a)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [rssi](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md#ad1f6bbfc27796e998ed30e307a251841)
- [cod](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md#aec239cbb82436ace39c8928a3baa0cf6)
- [eir](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md#a6bfe9a421257e2460eb9b4381252f9cc)
- [BT_BR_EIR_SIZE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga925f510c862c9a36539f4df1db0009d6)
- [bt_br_discovery_param](../bluetooth_service_model_reference/P012_bt_br_discovery_param_结构体.md)
- [length](../bluetooth_service_model_reference/P012_bt_br_discovery_param_结构体.md#a3087af0c5a264d50a27395d974f99e1e)
- [limited](../bluetooth_service_model_reference/P012_bt_br_discovery_param_结构体.md#ac02d03f8cfdf4ad7aee3178e871cc105)
- [bt_br_discovery_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9760190192dde5c498ec96628468be8d)
- [bt_br_discovery_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga567c71b49399fe7e1a5593edbf005e3a)
- [bt_br_discovery_cb](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md)
- [recv](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md#a3315f86bf3c9dbf339aa2254e0679182)
- [timeout](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md#a09c9f7258ea1739bf9330cf5c5bd882d)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md#a6ea814cabf9747cc7720ece9be59c8b9)
- [bt_br_discovery_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga430de0ad30da7322c5353941f1f6a133)
- [bt_br_discovery_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga25ab96ac005237aee739bf32fc1aac94)
- [bt_br_oob](../bluetooth_service_model_reference/P015_bt_br_oob_结构体.md)
- [addr](../bluetooth_service_model_reference/P015_bt_br_oob_结构体.md#a9b9f4c830a4e48736ac6b793d628ee98)
- [bt_br_oob_get_local](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga2ec860d06c45098624b106b59fbab634)
- [bt_br_set_discoverable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae3376fdd364e9b9d6e304ec589ba00f5)
- [bt_br_conn_req_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabfc34fe6f398d6526acc7c5afde8a689)
- [BT_BR_CONN_REQ_ACCEPT_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689ac01fd21779b5c5bcd883ab4f678ef26f)
- [BT_HCI_ROLE_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a150ea8f2095d8510bde3ebd65d521c29)
- [BT_BR_CONN_REQ_ACCEPT_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689ab5ad28e0358b20440da3851278a69e97)
- [BT_HCI_ROLE_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a9ca37afd4638ef94cdd55302bd4c99b3)
- [BT_BR_CONN_REQ_REJECT_NO_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689af1920d7300473810a412d508dfddf95a)
- [BT_HCI_ERR_INSUFFICIENT_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a0efddbffb31b93158b10a3f678f94f4e)
- [BT_BR_CONN_REQ_REJECT_SECURITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689a22574d1fc663afc2595ce8222867ee35)
- [BT_HCI_ERR_INSUFFICIENT_SECURITY](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a08d4bdfc189bccbdb97a51b0089e77a0)
- [BT_BR_CONN_REQ_REJECT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggabfc34fe6f398d6526acc7c5afde8a689aee59dd0540295ce4313804ce08c07908)
- [BT_HCI_ERR_BD_ADDR_UNACCEPTABLE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a366f85b3bcb3f578b2572149c69b7fc0)
- [bt_br_conn_req_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab661e90ad27ce1a280cefc15c5ad040c)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_br_set_connectable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga66c29ea0ccb8b8ff5610c1fc53fe1eb9)
- [bt_br_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga03757f934de6f13f95f02316b098875d)
- [BT_BR_SCAN_TYPE_STANDARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga03757f934de6f13f95f02316b098875da53ce32b8981ffb385d1f680f11d8feb7)
- [BT_BR_SCAN_TYPE_INTERLACED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga03757f934de6f13f95f02316b098875daac2a0585a4115768dcac602ffe87399d)
- [bt_br_page_scan_param](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md)
- [interval](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md#a670129c10bc0c57684e00ce7835b1648)
- [window](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md#a0f0cb7a792d2ec2ff7cc1d7bc6b01dce)
- [type](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md#aab7cc81841af5461825dfe19a45dab3e)
- [bt_br_page_scan_update_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga78c5fc5f71d08b0c800967ee7696fc83)
- [bt_br_inquiry_scan_param](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md)
- [interval](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md#a6a04891451c372f91b1c670f2a642b15)
- [window](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md#adc90daed4bfa1bc40a8b179f02eaab46)
- [type](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md#a23c55eeca21406ad038d2ff361405d2b)
- [bt_br_inquiry_scan_update_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6ca71da8c9eed3d317200aa1f6babc7d)
- [bt_br_set_class_of_device](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga201f64881ccc13169d072d9cc04948ba)
- [bt_br_get_class_of_device](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab49521adee2b653dbec04fbf833e22d9)
- [bt_br_bond_exists](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad88cf1dec20264f9bdde91571efe8dce)
- [bt_br_unpair](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaccab07100ab64fd805fe1d468bc889ac)
- [bt_br_bond_info](../bluetooth_service_model_reference/P009_bt_br_bond_info_结构体.md)
- [addr](../bluetooth_service_model_reference/P009_bt_br_bond_info_结构体.md#aaa0a6ec8d7010b795a48825df7a8c744)
- [bt_br_foreach_bond](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga4c82193c50c616d9319c87ebcffabe66)
- [bt_br_write_eir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab28ba977a94f63476f360d358868f8f6)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [data.h](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)
- [hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_br_bond_info::addr](../bluetooth_service_model_reference/P009_bt_br_bond_info_结构体.md#aaa0a6ec8d7010b795a48825df7a8c744)
- [bt_br_discovery_cb::timeout](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md#a09c9f7258ea1739bf9330cf5c5bd882d)
- [bt_br_discovery_cb::recv](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md#a3315f86bf3c9dbf339aa2254e0679182)
- [bt_br_discovery_cb::node](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md#a6ea814cabf9747cc7720ece9be59c8b9)
- [bt_br_discovery_param::length](../bluetooth_service_model_reference/P012_bt_br_discovery_param_结构体.md#a3087af0c5a264d50a27395d974f99e1e)
- [bt_br_discovery_param::limited](../bluetooth_service_model_reference/P012_bt_br_discovery_param_结构体.md#ac02d03f8cfdf4ad7aee3178e871cc105)
- [bt_br_discovery_result::eir](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md#a6bfe9a421257e2460eb9b4381252f9cc)
- [bt_br_discovery_result::addr](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md#a833b05883132a0c20690f71b2c14a62a)
- [bt_br_discovery_result::rssi](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md#ad1f6bbfc27796e998ed30e307a251841)
- [bt_br_discovery_result::cod](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md#aec239cbb82436ace39c8928a3baa0cf6)
- [bt_br_inquiry_scan_param::type](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md#a23c55eeca21406ad038d2ff361405d2b)
- [bt_br_inquiry_scan_param::interval](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md#a6a04891451c372f91b1c670f2a642b15)
- [bt_br_inquiry_scan_param::window](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md#adc90daed4bfa1bc40a8b179f02eaab46)
- [bt_br_oob::addr](../bluetooth_service_model_reference/P015_bt_br_oob_结构体.md#a9b9f4c830a4e48736ac6b793d628ee98)
- [bt_br_page_scan_param::window](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md#a0f0cb7a792d2ec2ff7cc1d7bc6b01dce)
- [bt_br_page_scan_param::interval](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md#a670129c10bc0c57684e00ce7835b1648)
- [bt_br_page_scan_param::type](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md#aab7cc81841af5461825dfe19a45dab3e)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P094_ch32v20x_30x-clocks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P096_clk.h_源码浏览.md)
