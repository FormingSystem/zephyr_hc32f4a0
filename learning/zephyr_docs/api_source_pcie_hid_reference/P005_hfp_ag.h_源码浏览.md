---
id: learning.zephyr-docs.api-source-pcie-hid-reference.page-5
title: hfp_ag.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hfp__ag_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_hfp\_ag.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hfp__ag_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hfp__ag_8h.html)。

## 5.1\_原始可见代码（Source Code）

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
<a id="foldopen00028"></a>
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
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00084"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00121"></a>
<a id="l00121"></a>
<a id="l00130"></a>
<a id="l00139"></a>
<a id="l00148"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00888"></a>
<a id="l00889"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00923"></a>
<a id="l00924"></a>
<a id="l00925"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="agroup__bt__hfp__ag_html_ga018d8ed8912f9dcef8c5fa37ac2bd889"></a>
<a id="agroup__bt__hfp__ag_html_ga019020ee2ed73c218f7dadf8371bf9a6"></a>
<a id="agroup__bt__hfp__ag_html_ga030c97d703fb45a2055653c51cb1b403"></a>
<a id="agroup__bt__hfp__ag_html_ga0a12a56baa25e2aea101a387fcccb88e"></a>
<a id="agroup__bt__hfp__ag_html_ga0f8b2e463aefbf74b26ac4f27033486c"></a>
<a id="agroup__bt__hfp__ag_html_ga195daffc37f1a3f210ba52dae1a9c4c2"></a>
<a id="agroup__bt__hfp__ag_html_ga20ef1240e0ff72d914405b259cc3164f"></a>
<a id="agroup__bt__hfp__ag_html_ga28682fc5d8cfee9c0adece68bcb94c3f"></a>
<a id="agroup__bt__hfp__ag_html_ga2f2e85a6076930ed87bc0727c75209a9"></a>
<a id="agroup__bt__hfp__ag_html_ga351e1b78b8c19c3971554fabb331e5c6"></a>
<a id="agroup__bt__hfp__ag_html_ga3668f3997afe9ab678f9eb2e6faf324d"></a>
<a id="agroup__bt__hfp__ag_html_ga37640efdcc737bfa0390df889a62f810"></a>
<a id="agroup__bt__hfp__ag_html_ga379ec1c540195549fc59417d8d1ce7e5"></a>
<a id="agroup__bt__hfp__ag_html_ga405fcf8e03bac39bd5b0e7bf2766045f"></a>
<a id="agroup__bt__hfp__ag_html_ga443cd2928686f222d61f06c7477ea793"></a>
<a id="agroup__bt__hfp__ag_html_ga4bbcec3ed5394e965aa7404dc968b94d"></a>
<a id="agroup__bt__hfp__ag_html_ga4da632e9775051df6a5b5010fd3806df"></a>
<a id="agroup__bt__hfp__ag_html_ga4e71364283448c7c5d3306c111aa167d"></a>
<a id="agroup__bt__hfp__ag_html_ga525085c7c75e412ca43ba8b23cbc0c3d"></a>
<a id="agroup__bt__hfp__ag_html_ga53778bd332c95fa4357d254f5ef125a2"></a>
<a id="agroup__bt__hfp__ag_html_ga542a1754a16e32a9b2651f1230aa7066"></a>
<a id="agroup__bt__hfp__ag_html_ga5614bf3f1de11959a0364f458523e06e"></a>
<a id="agroup__bt__hfp__ag_html_ga580328104cf990c6f9e0a64642c16ebd"></a>
<a id="agroup__bt__hfp__ag_html_ga5b602810558268396f0cb64adcb0d014"></a>
<a id="agroup__bt__hfp__ag_html_ga5e249248a52d7c95c9d3f3f852bf2314"></a>
<a id="agroup__bt__hfp__ag_html_ga881ea4d3cc732fb5d804df203dde7746"></a>
<a id="agroup__bt__hfp__ag_html_ga8e9b485f7ea0b9e16d96f578cdc587c3"></a>
<a id="agroup__bt__hfp__ag_html_gaacc2df6144e1a33b13635855fe74f1f1"></a>
<a id="agroup__bt__hfp__ag_html_gaaf066dce38c028254b6c1880bcebaa13"></a>
<a id="agroup__bt__hfp__ag_html_gab288d6e6b45a24b706328da58ca43a3b"></a>
<a id="agroup__bt__hfp__ag_html_gabdad8c764c91e133598584d741ed9d4b"></a>
<a id="agroup__bt__hfp__ag_html_gacb1b361e6b0a441102f7ccd641eb3e6b"></a>
<a id="agroup__bt__hfp__ag_html_gad2220b4a470cb3d537cf09492847568e"></a>
<a id="agroup__bt__hfp__ag_html_gadf0b4aef701cf0986ea9599ad79d451a"></a>
<a id="agroup__bt__hfp__ag_html_gaf838e54046c380931f23a59919ccfa5b"></a>
<a id="agroup__bt__hfp__ag_html_gga019020ee2ed73c218f7dadf8371bf9a6a08a4f52a9ca4fdcaa1c6575b1b378b55"></a>
<a id="agroup__bt__hfp__ag_html_gga019020ee2ed73c218f7dadf8371bf9a6a83ea29c4261577438e481e2b9f0c7d37"></a>
<a id="agroup__bt__hfp__ag_html_gga030c97d703fb45a2055653c51cb1b403a9719aca10a790eb9f62d498bc4bec9d1"></a>
<a id="agroup__bt__hfp__ag_html_gga030c97d703fb45a2055653c51cb1b403afd31a626b024de7e6e68ade0d776b14f"></a>
<a id="agroup__bt__hfp__ag_html_gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234"></a>
<a id="agroup__bt__hfp__ag_html_gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5"></a>
<a id="agroup__bt__hfp__ag_html_gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b"></a>
<a id="agroup__bt__hfp__ag_html_gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493"></a>
<a id="agroup__bt__hfp__ag_html_gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609"></a>
<a id="agroup__bt__hfp__ag_html_gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d"></a>
<a id="agroup__bt__hfp__ag_html_gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863"></a>
<a id="agroup__bt__hfp__ag_html_gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36"></a>
<a id="agroup__bt__hfp__ag_html_ggad2220b4a470cb3d537cf09492847568ea09545d4deadcc910c42b615d21f91963"></a>
<a id="agroup__bt__hfp__ag_html_ggad2220b4a470cb3d537cf09492847568ea2e155da5b54cb32a400de1d44ebc2542"></a>
<a id="agroup__bt__hfp__ag_html_ggad2220b4a470cb3d537cf09492847568ea423017739b17f57e0a8adb7d6b9cffae"></a>
<a id="agroup__bt__hfp__ag_html_ggad2220b4a470cb3d537cf09492847568ea4c387d6e8628fc40e9969c95ff9ea658"></a>
<a id="agroup__bt__hfp__ag_html_ggad2220b4a470cb3d537cf09492847568ea4faad88cf6cb9926f78e7da7065713f8"></a>
<a id="agroup__bt__hfp__ag_html_ggad2220b4a470cb3d537cf09492847568ea5b1a40f632b8d9ce3b02ffacb1a07fb2"></a>
<a id="agroup__bt__hfp__ag_html_ggad2220b4a470cb3d537cf09492847568eac2acf82710d562fd2852139f7e8146e2"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__hfp__ag__call_html"></a>
<a id="astructbt__hfp__ag__cb_html"></a>
<a id="astructbt__hfp__ag__cb_html_a0b8967f487d64556851420b2f4e059fe"></a>
<a id="astructbt__hfp__ag__cb_html_a16c528018a2e9e97320df885c049454f"></a>
<a id="astructbt__hfp__ag__cb_html_a1cf5786c517ecf4bf611a168e312084c"></a>
<a id="astructbt__hfp__ag__cb_html_a2f15172060cc5d225894be5c8311610b"></a>
<a id="astructbt__hfp__ag__cb_html_a38adb040dee9abd794f952322bf3d615"></a>
<a id="astructbt__hfp__ag__cb_html_a390377048e8623889515f2c6b6be0874"></a>
<a id="astructbt__hfp__ag__cb_html_a5b9f1c48e15a74b052678c491a592a5f"></a>
<a id="astructbt__hfp__ag__cb_html_a7da69bf1f5b85130ce2656c4915ba6d8"></a>
<a id="astructbt__hfp__ag__cb_html_a82abcad15f921fb0c99cc705e139aac1"></a>
<a id="astructbt__hfp__ag__cb_html_a8946de63ef24bbbc69e285abe2d141c1"></a>
<a id="astructbt__hfp__ag__cb_html_a95600361e59a516f220a314e920c5858"></a>
<a id="astructbt__hfp__ag__cb_html_a965d39254b75668f968d9a2bb5cffeba"></a>
<a id="astructbt__hfp__ag__cb_html_a976016f32e462daf38cd6d24ba18ff3d"></a>
<a id="astructbt__hfp__ag__cb_html_a98c497e706ed5fcfe6fd308741893e91"></a>
<a id="astructbt__hfp__ag__cb_html_a9d6b978f82de6ded48881a87eb90aebb"></a>
<a id="astructbt__hfp__ag__cb_html_aa0a4ab5aad6557a786ccf2f6861b932c"></a>
<a id="astructbt__hfp__ag__cb_html_aa578544cd1f329a06898efcfa7db2d78"></a>
<a id="astructbt__hfp__ag__cb_html_aaad37582866c420ee41c3f730de16eb4"></a>
<a id="astructbt__hfp__ag__cb_html_aac2b1ff4d80361e0e5eea2481027b4cf"></a>
<a id="astructbt__hfp__ag__cb_html_ab9506172c5b23bf97b5d59ddaddd7282"></a>
<a id="astructbt__hfp__ag__cb_html_abe1b5d71279c2e3292b3b90043d75224"></a>
<a id="astructbt__hfp__ag__cb_html_abe78441b0f01acd72713c7658f4e0274"></a>
<a id="astructbt__hfp__ag__cb_html_ac06c1ddfa5cdc4ecb81a838e32299c8a"></a>
<a id="astructbt__hfp__ag__cb_html_ac3771d39b8f1982514bbb23fc7773468"></a>
<a id="astructbt__hfp__ag__cb_html_ac3c09ffe392e167dd5aae82e740b5050"></a>
<a id="astructbt__hfp__ag__cb_html_ad690d69c9786c69ad85e005e778b316c"></a>
<a id="astructbt__hfp__ag__cb_html_ad9925958c87b164113f607bd680ce2c3"></a>
<a id="astructbt__hfp__ag__cb_html_adf9960da8a3f4c38f7fcd60501522462"></a>
<a id="astructbt__hfp__ag__cb_html_aecc8cdaf372d93f9cb531604f9b82d65"></a>
<a id="astructbt__hfp__ag__cb_html_af335450c5e63139485fa5a131814d650"></a>
<a id="astructbt__hfp__ag__cb_html_af9c53ab021dbbf1017d71895581960c4"></a>
<a id="astructbt__hfp__ag__ongoing__call_html"></a>
<a id="astructbt__hfp__ag__ongoing__call_html_a1e5800a9c0f37539d0505d3223a35e2f"></a>
<a id="astructbt__hfp__ag__ongoing__call_html_a26a77093f5aace7dd2d5693f4cb82189"></a>
<a id="astructbt__hfp__ag__ongoing__call_html_a506610c17544daf8a0238a2c4d285526"></a>
<a id="astructbt__hfp__ag__ongoing__call_html_ac865f464436c3e73561fa8f6fcf09947"></a>
<a id="astructbt__hfp__ag_html"></a>

```c


/*
 * Copyright (c) 2015-2016 Intel Corporation
 * Copyright 2023-2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HFP_AG_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HFP_AG_H_


#include <zephyr/bluetooth/bluetooth.h>

#ifdef __cplusplus
extern "C" {
#endif

/* HFP AG Indicators */
enum bt_hfp_ag_indicator {
        BT_HFP_AG_SERVICE_IND = 0,    /* Service availability indicator */
        BT_HFP_AG_CALL_IND = 1,       /* call status indicator */
        BT_HFP_AG_CALL_SETUP_IND = 2, /* Call set up status indicator */
        BT_HFP_AG_CALL_HELD_IND = 3,  /* Call hold status indicator */
        BT_HFP_AG_SIGNAL_IND = 4,    /* Signal strength indicator */
        BT_HFP_AG_ROAM_IND = 5,       /* Roaming status indicator */
        BT_HFP_AG_BATTERY_IND = 6,    /* Battery change indicator */
        BT_HFP_AG_IND_MAX             /* Indicator MAX value */
};

/* HFP CODEC */
#define BT_HFP_AG_CODEC_CVSD    0x01
#define BT_HFP_AG_CODEC_MSBC    0x02
#define BT_HFP_AG_CODEC_LC3_SWB 0x03

struct bt_hfp_ag;

struct bt_hfp_ag_call;

typedef int (*bt_hfp_ag_query_subscriber_func_t)(struct bt_hfp_ag *ag, char *number, uint8_t type,
                                                 uint8_t service);

/* HF indicators */
enum hfp_ag_hf_indicators {
        HFP_AG_ENHANCED_SAFETY_IND = 1, /* Enhanced Safety */
        HFP_AG_BATTERY_LEVEL_IND = 2,   /* Remaining level of Battery */
};

/* The status of the call */
enum __packed bt_hfp_ag_call_status {
        BT_HFP_AG_CALL_STATUS_ACTIVE = 0,       /* Call is active */
        BT_HFP_AG_CALL_STATUS_HELD = 1,         /* Call is on hold */
        BT_HFP_AG_CALL_STATUS_DIALING = 2,      /* Outgoing call is being dialed */
        BT_HFP_AG_CALL_STATUS_ALERTING = 3,     /* Outgoing call is being alerted */
        BT_HFP_AG_CALL_STATUS_INCOMING = 4,     /* Incoming call is came */
        BT_HFP_AG_CALL_STATUS_WAITING = 5,      /* Incoming call is waiting */
        BT_HFP_AG_CALL_STATUS_INCOMING_HELD = 6 /* Call held by Response and Hold */
};

/* The direction of the call */
enum __packed bt_hfp_ag_call_dir {
        BT_HFP_AG_CALL_DIR_OUTGOING = 0, /* It is a outgoing call */
        BT_HFP_AG_CALL_DIR_INCOMING = 1, /* It is a incoming call */
};

struct bt_hfp_ag_ongoing_call {
        char number[CONFIG_BT_HFP_AG_PHONE_NUMBER_MAX_LEN + 1];
        uint8_t type;
        enum bt_hfp_ag_call_dir dir;
        enum bt_hfp_ag_call_status status;
};

struct bt_hfp_ag_cb {
        void (*connected)(struct bt_conn *conn, struct bt_hfp_ag *ag);
        void (*disconnected)(struct bt_hfp_ag *ag);
        void (*sco_connected)(struct bt_hfp_ag *ag, struct bt_conn *sco_conn);
        void (*sco_disconnected)(struct bt_conn *sco_conn, uint8_t reason);

        int (*get_indicator_value)(struct bt_hfp_ag *ag, uint8_t *service, uint8_t *strength,
                                   uint8_t *roam, uint8_t *battery);

        int (*get_ongoing_call)(struct bt_hfp_ag *ag);

        int (*memory_dial)(struct bt_hfp_ag *ag, const char *location, char **number);

        int (*number_call)(struct bt_hfp_ag *ag, const char *number);

        int (*redial)(struct bt_hfp_ag *ag, char number[CONFIG_BT_HFP_AG_PHONE_NUMBER_MAX_LEN + 1]);

        void (*outgoing)(struct bt_hfp_ag *ag, struct bt_hfp_ag_call *call, const char *number);

        void (*incoming)(struct bt_hfp_ag *ag, struct bt_hfp_ag_call *call, const char *number);

        void (*incoming_held)(struct bt_hfp_ag_call *call);

        void (*ringing)(struct bt_hfp_ag_call *call, bool in_band);

        void (*accept)(struct bt_hfp_ag_call *call);

        void (*held)(struct bt_hfp_ag_call *call);

        void (*retrieve)(struct bt_hfp_ag_call *call);

        void (*reject)(struct bt_hfp_ag_call *call);

        void (*terminate)(struct bt_hfp_ag_call *call);

        void (*codec)(struct bt_hfp_ag *ag, uint32_t ids);

        void (*codec_negotiate)(struct bt_hfp_ag *ag, int err);

        void (*audio_connect_req)(struct bt_hfp_ag *ag);

        void (*vgm)(struct bt_hfp_ag *ag, uint8_t gain);

        void (*vgs)(struct bt_hfp_ag *ag, uint8_t gain);

        void (*ecnr_turn_off)(struct bt_hfp_ag *ag);

        void (*explicit_call_transfer)(struct bt_hfp_ag *ag);

        void (*voice_recognition)(struct bt_hfp_ag *ag, bool activate);

        void (*ready_to_accept_audio)(struct bt_hfp_ag *ag);

        int (*request_phone_number)(struct bt_hfp_ag *ag, char **number);

        void (*transmit_dtmf_code)(struct bt_hfp_ag *ag, char code);

        int (*subscriber_number)(struct bt_hfp_ag *ag, bt_hfp_ag_query_subscriber_func_t func);

        void (*hf_indicator_value)(struct bt_hfp_ag *ag, enum hfp_ag_hf_indicators indicator,
                                   uint32_t value);
};

int bt_hfp_ag_register(struct bt_hfp_ag_cb *cb);

int bt_hfp_ag_connect(struct bt_conn *conn, struct bt_hfp_ag **ag, uint8_t channel);

int bt_hfp_ag_disconnect(struct bt_hfp_ag *ag);

int bt_hfp_ag_remote_incoming(struct bt_hfp_ag *ag, const char *number);

int bt_hfp_ag_hold_incoming(struct bt_hfp_ag_call *call);

int bt_hfp_ag_reject(struct bt_hfp_ag_call *call);

int bt_hfp_ag_accept(struct bt_hfp_ag_call *call);

int bt_hfp_ag_terminate(struct bt_hfp_ag_call *call);

int bt_hfp_ag_retrieve(struct bt_hfp_ag_call *call);

int bt_hfp_ag_hold(struct bt_hfp_ag_call *call);

int bt_hfp_ag_outgoing(struct bt_hfp_ag *ag, const char *number);

int bt_hfp_ag_remote_ringing(struct bt_hfp_ag_call *call);

int bt_hfp_ag_remote_reject(struct bt_hfp_ag_call *call);

int bt_hfp_ag_remote_accept(struct bt_hfp_ag_call *call);

int bt_hfp_ag_remote_terminate(struct bt_hfp_ag_call *call);

int bt_hfp_ag_explicit_call_transfer(struct bt_hfp_ag *ag);

int bt_hfp_ag_vgm(struct bt_hfp_ag *ag, uint8_t vgm);

int bt_hfp_ag_vgs(struct bt_hfp_ag *ag, uint8_t vgs);

int bt_hfp_ag_set_operator(struct bt_hfp_ag *ag, uint8_t mode, char *name);

int bt_hfp_ag_audio_connect(struct bt_hfp_ag *ag, uint8_t id);

int bt_hfp_ag_inband_ringtone(struct bt_hfp_ag *ag, bool inband);

int bt_hfp_ag_voice_recognition(struct bt_hfp_ag *ag, bool activate);

int bt_hfp_ag_vre_state(struct bt_hfp_ag *ag, uint8_t state);

int bt_hfp_ag_vre_textual_representation(struct bt_hfp_ag *ag, uint8_t state, const char *id,
                                         uint8_t type, uint8_t operation, const char *text);

int bt_hfp_ag_signal_strength(struct bt_hfp_ag *ag, uint8_t strength);

int bt_hfp_ag_roaming_status(struct bt_hfp_ag *ag, uint8_t status);

int bt_hfp_ag_battery_level(struct bt_hfp_ag *ag, uint8_t level);

int bt_hfp_ag_service_availability(struct bt_hfp_ag *ag, bool available);

int bt_hfp_ag_hf_indicator(struct bt_hfp_ag *ag, enum hfp_ag_hf_indicators indicator, bool enable);

int bt_hfp_ag_ongoing_calls(struct bt_hfp_ag *ag, struct bt_hfp_ag_ongoing_call *calls,
                            size_t count);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HFP_AG_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015-2016 Intel Corporation。

版权（Copyright）：2023-2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

免提配置文件（HFP）音频网关（AG）指示项。

### 注释 3：原第 29 行

服务可用性指示项（Service Availability Indicator）。

### 注释 4：原第 30 行

通话状态指示项（Call Status Indicator）。

### 注释 5：原第 31 行

通话建立状态指示项（Call Setup Status Indicator）。

### 注释 6：原第 32 行

通话保持状态指示项（Call Hold Status Indicator）。

### 注释 7：原第 33 行

信号强度指示项（Signal Strength Indicator）。

### 注释 8：原第 34 行

漫游状态指示项（Roaming Status Indicator）。

### 注释 9：原第 35 行

电池变化指示项（Battery Change Indicator）。

### 注释 10：原第 36 行

指示项最大值（Indicator MAX Value）。

### 注释 11：原第 39 行

免提配置文件（HFP）编解码器（CODEC）。

### 注释 12：原第 83 行

免提端（HF）指示项。

### 注释 13：原第 85 行

增强安全（Enhanced Safety）。

### 注释 14：原第 86 行

剩余电池电量（Remaining Battery Level）。

### 注释 15：原第 89 行

通话状态（Call Status）。

### 注释 16：原第 91 行

通话处于活动状态（Active）。

### 注释 17：原第 92 行

通话处于保持状态（On Hold）。

### 注释 18：原第 93 行

去电正在拨号（Dialing）。

### 注释 19：原第 94 行

去电正在提醒对方（Alerting）。

### 注释 20：原第 95 行

来电已到达（Incoming Call）。

### 注释 21：原第 96 行

来电正在等待（Waiting）。

### 注释 22：原第 97 行

通话由响应并保持（Response and Hold）操作保持。

### 注释 23：原第 100 行

通话方向（Call Direction）。

### 注释 24：原第 102 行

这是一通去电（Outgoing Call）。

### 注释 25：原第 103 行

这是一通来电（Incoming Call）。

### 注释 26：原第 934 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HFP_AG_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hfp__ag_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [bt_hfp_ag_indicator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga37640efdcc737bfa0390df889a62f810)
- [BT_HFP_AG_SERVICE_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234)
- [BT_HFP_AG_CALL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d)
- [BT_HFP_AG_CALL_SETUP_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5)
- [BT_HFP_AG_CALL_HELD_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b)
- [BT_HFP_AG_SIGNAL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493)
- [BT_HFP_AG_ROAM_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863)
- [BT_HFP_AG_BATTERY_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609)
- [BT_HFP_AG_IND_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36)
- [bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)
- [bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)
- [bt_hfp_ag_query_subscriber_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga8e9b485f7ea0b9e16d96f578cdc587c3)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [hfp_ag_hf_indicators](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga030c97d703fb45a2055653c51cb1b403)
- [HFP_AG_ENHANCED_SAFETY_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga030c97d703fb45a2055653c51cb1b403afd31a626b024de7e6e68ade0d776b14f)
- [HFP_AG_BATTERY_LEVEL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga030c97d703fb45a2055653c51cb1b403a9719aca10a790eb9f62d498bc4bec9d1)
- [bt_hfp_ag_call_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gad2220b4a470cb3d537cf09492847568e)
- [BT_HFP_AG_CALL_STATUS_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea4c387d6e8628fc40e9969c95ff9ea658)
- [BT_HFP_AG_CALL_STATUS_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568eac2acf82710d562fd2852139f7e8146e2)
- [BT_HFP_AG_CALL_STATUS_DIALING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea09545d4deadcc910c42b615d21f91963)
- [BT_HFP_AG_CALL_STATUS_ALERTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea423017739b17f57e0a8adb7d6b9cffae)
- [BT_HFP_AG_CALL_STATUS_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea4faad88cf6cb9926f78e7da7065713f8)
- [BT_HFP_AG_CALL_STATUS_WAITING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea5b1a40f632b8d9ce3b02ffacb1a07fb2)
- [BT_HFP_AG_CALL_STATUS_INCOMING_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea2e155da5b54cb32a400de1d44ebc2542)
- [bt_hfp_ag_call_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga019020ee2ed73c218f7dadf8371bf9a6)
- [BT_HFP_AG_CALL_DIR_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga019020ee2ed73c218f7dadf8371bf9a6a83ea29c4261577438e481e2b9f0c7d37)
- [BT_HFP_AG_CALL_DIR_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga019020ee2ed73c218f7dadf8371bf9a6a08a4f52a9ca4fdcaa1c6575b1b378b55)
- [bt_hfp_ag_ongoing_call](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md)
- [number](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md#a1e5800a9c0f37539d0505d3223a35e2f)
- [type](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md#a26a77093f5aace7dd2d5693f4cb82189)
- [dir](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md#a506610c17544daf8a0238a2c4d285526)
- [status](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md#ac865f464436c3e73561fa8f6fcf09947)
- [bt_hfp_ag_cb](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md)
- [connected](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ab9506172c5b23bf97b5d59ddaddd7282)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [disconnected](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#af9c53ab021dbbf1017d71895581960c4)
- [sco_connected](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#aac2b1ff4d80361e0e5eea2481027b4cf)
- [sco_disconnected](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a95600361e59a516f220a314e920c5858)
- [get_indicator_value](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a1cf5786c517ecf4bf611a168e312084c)
- [get_ongoing_call](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ac3771d39b8f1982514bbb23fc7773468)
- [memory_dial](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#af335450c5e63139485fa5a131814d650)
- [number_call](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a98c497e706ed5fcfe6fd308741893e91)
- [redial](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#aa578544cd1f329a06898efcfa7db2d78)
- [outgoing](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a8946de63ef24bbbc69e285abe2d141c1)
- [incoming](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#aa0a4ab5aad6557a786ccf2f6861b932c)
- [incoming_held](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a5b9f1c48e15a74b052678c491a592a5f)
- [ringing](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a0b8967f487d64556851420b2f4e059fe)
- [accept](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a7da69bf1f5b85130ce2656c4915ba6d8)
- [held](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#abe78441b0f01acd72713c7658f4e0274)
- [retrieve](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a9d6b978f82de6ded48881a87eb90aebb)
- [reject](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#abe1b5d71279c2e3292b3b90043d75224)
- [terminate](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#adf9960da8a3f4c38f7fcd60501522462)
- [codec](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a2f15172060cc5d225894be5c8311610b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [codec_negotiate](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a82abcad15f921fb0c99cc705e139aac1)
- [audio_connect_req](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a390377048e8623889515f2c6b6be0874)
- [vgm](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#aaad37582866c420ee41c3f730de16eb4)
- [vgs](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a38adb040dee9abd794f952322bf3d615)
- [ecnr_turn_off](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ac3c09ffe392e167dd5aae82e740b5050)
- [explicit_call_transfer](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ac06c1ddfa5cdc4ecb81a838e32299c8a)
- [voice_recognition](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a16c528018a2e9e97320df885c049454f)
- [ready_to_accept_audio](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ad9925958c87b164113f607bd680ce2c3)
- [request_phone_number](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#aecc8cdaf372d93f9cb531604f9b82d65)
- [transmit_dtmf_code](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ad690d69c9786c69ad85e005e778b316c)
- [subscriber_number](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a976016f32e462daf38cd6d24ba18ff3d)
- [hf_indicator_value](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a965d39254b75668f968d9a2bb5cffeba)
- [bt_hfp_ag_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga379ec1c540195549fc59417d8d1ce7e5)
- [bt_hfp_ag_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga5b602810558268396f0cb64adcb0d014)
- [bt_hfp_ag_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gadf0b4aef701cf0986ea9599ad79d451a)
- [bt_hfp_ag_remote_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga443cd2928686f222d61f06c7477ea793)
- [bt_hfp_ag_hold_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gab288d6e6b45a24b706328da58ca43a3b)
- [bt_hfp_ag_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga195daffc37f1a3f210ba52dae1a9c4c2)
- [bt_hfp_ag_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga351e1b78b8c19c3971554fabb331e5c6)
- [bt_hfp_ag_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga2f2e85a6076930ed87bc0727c75209a9)
- [bt_hfp_ag_retrieve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga405fcf8e03bac39bd5b0e7bf2766045f)
- [bt_hfp_ag_hold](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga4bbcec3ed5394e965aa7404dc968b94d)
- [bt_hfp_ag_outgoing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga580328104cf990c6f9e0a64642c16ebd)
- [bt_hfp_ag_remote_ringing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga0a12a56baa25e2aea101a387fcccb88e)
- [bt_hfp_ag_remote_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gacb1b361e6b0a441102f7ccd641eb3e6b)
- [bt_hfp_ag_remote_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga018d8ed8912f9dcef8c5fa37ac2bd889)
- [bt_hfp_ag_remote_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga525085c7c75e412ca43ba8b23cbc0c3d)
- [bt_hfp_ag_explicit_call_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga5e249248a52d7c95c9d3f3f852bf2314)
- [bt_hfp_ag_vgm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga53778bd332c95fa4357d254f5ef125a2)
- [bt_hfp_ag_vgs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gabdad8c764c91e133598584d741ed9d4b)
- [bt_hfp_ag_set_operator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gaaf066dce38c028254b6c1880bcebaa13)
- [bt_hfp_ag_audio_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga542a1754a16e32a9b2651f1230aa7066)
- [bt_hfp_ag_inband_ringtone](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga881ea4d3cc732fb5d804df203dde7746)
- [bt_hfp_ag_voice_recognition](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga28682fc5d8cfee9c0adece68bcb94c3f)
- [bt_hfp_ag_vre_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga3668f3997afe9ab678f9eb2e6faf324d)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_hfp_ag_vre_textual_representation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga4e71364283448c7c5d3306c111aa167d)
- [bt_hfp_ag_signal_strength](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga20ef1240e0ff72d914405b259cc3164f)
- [bt_hfp_ag_roaming_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga0f8b2e463aefbf74b26ac4f27033486c)
- [bt_hfp_ag_battery_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga4da632e9775051df6a5b5010fd3806df)
- [bt_hfp_ag_service_availability](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gaf838e54046c380931f23a59919ccfa5b)
- [bt_hfp_ag_hf_indicator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gaacc2df6144e1a33b13635855fe74f1f1)
- [bt_hfp_ag_ongoing_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga5614bf3f1de11959a0364f458523e06e)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [bt_hfp_ag_cb::ringing](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a0b8967f487d64556851420b2f4e059fe)
- [bt_hfp_ag_cb::voice_recognition](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a16c528018a2e9e97320df885c049454f)
- [bt_hfp_ag_cb::get_indicator_value](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a1cf5786c517ecf4bf611a168e312084c)
- [bt_hfp_ag_cb::codec](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a2f15172060cc5d225894be5c8311610b)
- [bt_hfp_ag_cb::vgs](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a38adb040dee9abd794f952322bf3d615)
- [bt_hfp_ag_cb::audio_connect_req](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a390377048e8623889515f2c6b6be0874)
- [bt_hfp_ag_cb::incoming_held](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a5b9f1c48e15a74b052678c491a592a5f)
- [bt_hfp_ag_cb::accept](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a7da69bf1f5b85130ce2656c4915ba6d8)
- [bt_hfp_ag_cb::codec_negotiate](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a82abcad15f921fb0c99cc705e139aac1)
- [bt_hfp_ag_cb::outgoing](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a8946de63ef24bbbc69e285abe2d141c1)
- [bt_hfp_ag_cb::sco_disconnected](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a95600361e59a516f220a314e920c5858)
- [bt_hfp_ag_cb::hf_indicator_value](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a965d39254b75668f968d9a2bb5cffeba)
- [bt_hfp_ag_cb::subscriber_number](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a976016f32e462daf38cd6d24ba18ff3d)
- [bt_hfp_ag_cb::number_call](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a98c497e706ed5fcfe6fd308741893e91)
- [bt_hfp_ag_cb::retrieve](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#a9d6b978f82de6ded48881a87eb90aebb)
- [bt_hfp_ag_cb::incoming](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#aa0a4ab5aad6557a786ccf2f6861b932c)
- [bt_hfp_ag_cb::redial](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#aa578544cd1f329a06898efcfa7db2d78)
- [bt_hfp_ag_cb::vgm](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#aaad37582866c420ee41c3f730de16eb4)
- [bt_hfp_ag_cb::sco_connected](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#aac2b1ff4d80361e0e5eea2481027b4cf)
- [bt_hfp_ag_cb::connected](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ab9506172c5b23bf97b5d59ddaddd7282)
- [bt_hfp_ag_cb::reject](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#abe1b5d71279c2e3292b3b90043d75224)
- [bt_hfp_ag_cb::held](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#abe78441b0f01acd72713c7658f4e0274)
- [bt_hfp_ag_cb::explicit_call_transfer](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ac06c1ddfa5cdc4ecb81a838e32299c8a)
- [bt_hfp_ag_cb::get_ongoing_call](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ac3771d39b8f1982514bbb23fc7773468)
- [bt_hfp_ag_cb::ecnr_turn_off](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ac3c09ffe392e167dd5aae82e740b5050)
- [bt_hfp_ag_cb::transmit_dtmf_code](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ad690d69c9786c69ad85e005e778b316c)
- [bt_hfp_ag_cb::ready_to_accept_audio](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#ad9925958c87b164113f607bd680ce2c3)
- [bt_hfp_ag_cb::terminate](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#adf9960da8a3f4c38f7fcd60501522462)
- [bt_hfp_ag_cb::request_phone_number](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#aecc8cdaf372d93f9cb531604f9b82d65)
- [bt_hfp_ag_cb::memory_dial](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#af335450c5e63139485fa5a131814d650)
- [bt_hfp_ag_cb::disconnected](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md#af9c53ab021dbbf1017d71895581960c4)
- [bt_hfp_ag_ongoing_call::number](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md#a1e5800a9c0f37539d0505d3223a35e2f)
- [bt_hfp_ag_ongoing_call::type](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md#a26a77093f5aace7dd2d5693f4cb82189)
- [bt_hfp_ag_ongoing_call::dir](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md#a506610c17544daf8a0238a2c4d285526)
- [bt_hfp_ag_ongoing_call::status](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md#ac865f464436c3e73561fa8f6fcf09947)

---

[上一章](P004_esp32p4-gpio-sigmap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_ite-intc.h_源码浏览.md)
