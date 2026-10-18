---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-17
title: hfp_hf.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hfp__hf_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_hfp\_hf.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hfp__hf_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hfp__hf_8h.html)。

## 17.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
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
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00124"></a>
<a id="l00135"></a>
<a id="l00144"></a>
<a id="l00153"></a>
<a id="l00161"></a>
<a id="l00170"></a>
<a id="l00178"></a>
<a id="l00187"></a>
<a id="l00195"></a>
<a id="l00203"></a>
<a id="l00211"></a>
<a id="l00219"></a>
<a id="l00226"></a>
<a id="l00233"></a>
<a id="l00241"></a>
<a id="l00249"></a>
<a id="l00257"></a>
<a id="l00265"></a>
<a id="l00273"></a>
<a id="l00286"></a>
<a id="l00298"></a>
<a id="l00310"></a>
<a id="l00321"></a>
<a id="l00337"></a>
<a id="l00360"></a>
<a id="l00371"></a>
<a id="l00386"></a>
<a id="l00400"></a>
<a id="l00417"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00740"></a>
<a id="l00741"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00876"></a>
<a id="l00877"></a>
<a id="l00888"></a>
<a id="l00889"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00956"></a>
<a id="l00957"></a>
<a id="l00966"></a>
<a id="l00967"></a>
<a id="l00980"></a>
<a id="l00981"></a>
<a id="l00990"></a>
<a id="l00991"></a>
<a id="l00992"></a>
<a id="foldopen00993"></a>
<a id="l00993"></a>
<a id="l00994"></a>
<a id="l00995"></a>
<a id="l00996"></a>
<a id="l00997"></a>
<a id="l00998"></a>
<a id="l00999"></a>
<a id="l01000"></a>
<a id="l01001"></a>
<a id="l01002"></a>
<a id="l01019"></a>
<a id="l01020"></a>
<a id="l01032"></a>
<a id="l01033"></a>
<a id="l01045"></a>
<a id="l01046"></a>
<a id="l01057"></a>
<a id="l01058"></a>
<a id="l01059"></a>
<a id="l01060"></a>
<a id="l01061"></a>
<a id="l01062"></a>
<a id="l01066"></a>
<a id="l01067"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="agroup__bt__hfp_html_ga04d9fe3524c9522e98830507886bdfc6"></a>
<a id="agroup__bt__hfp_html_ga0602cee7a90ca4afe90b65d748024472"></a>
<a id="agroup__bt__hfp_html_ga06e7e93578601693fa377a240e0d18a7"></a>
<a id="agroup__bt__hfp_html_ga0c1c35b3117f78f43a6300d4ff7dd18b"></a>
<a id="agroup__bt__hfp_html_ga1ad888c3b967d3f9b2e5ccee303b9ad7"></a>
<a id="agroup__bt__hfp_html_ga2b48a0938e65899417b2f3ab1fa4c548"></a>
<a id="agroup__bt__hfp_html_ga2e4a7c05a3ba9a32eab50b9904f7f161"></a>
<a id="agroup__bt__hfp_html_ga2f0e6012503a9b59b03a0fb508d12f88"></a>
<a id="agroup__bt__hfp_html_ga302e9ed397b056edef518470c6ea1d62"></a>
<a id="agroup__bt__hfp_html_ga34649dbecca2513c0b5bcd0e109b2551"></a>
<a id="agroup__bt__hfp_html_ga36be4ff5fd805c4413ba90b1f62b9143"></a>
<a id="agroup__bt__hfp_html_ga38619377f146492993ee9a92a487af50"></a>
<a id="agroup__bt__hfp_html_ga3afb0d82551708975dbeb9c903c3d1fb"></a>
<a id="agroup__bt__hfp_html_ga3f6b43bf53fa04a6e71e883dc38f988b"></a>
<a id="agroup__bt__hfp_html_ga40de46a6651eb85aa6d04ad66f528803"></a>
<a id="agroup__bt__hfp_html_ga540bf6ec23c632b3f736e6302ef32ebd"></a>
<a id="agroup__bt__hfp_html_ga5bad80355fd7903abcee84437d399829"></a>
<a id="agroup__bt__hfp_html_ga64ac1971dc7b1dacf6685bdc0c71e34c"></a>
<a id="agroup__bt__hfp_html_ga6a3a6bc61a3a74f5a4a48d7e39bd74a0"></a>
<a id="agroup__bt__hfp_html_ga6c2ba70d70c8f9d6d569662086985c85"></a>
<a id="agroup__bt__hfp_html_ga70e086f6a02cb116317a8e80f76abf6d"></a>
<a id="agroup__bt__hfp_html_ga7389e5723e01b661b5e9c9d2114918b8"></a>
<a id="agroup__bt__hfp_html_ga7f37a9c009b4e55b7060d635c5b0c67b"></a>
<a id="agroup__bt__hfp_html_ga810c80de5baf92feb23650374b60bcee"></a>
<a id="agroup__bt__hfp_html_ga862b201be555821e932f6df5599eaa57"></a>
<a id="agroup__bt__hfp_html_ga91637662881dd655f8fc8ed6e6f8b973"></a>
<a id="agroup__bt__hfp_html_ga91fc2204f50df07567f87a2b7a18e69f"></a>
<a id="agroup__bt__hfp_html_ga92d89b0b37186688e86091a7a8015245"></a>
<a id="agroup__bt__hfp_html_ga9611012a35df66fac324b99b16e5d958"></a>
<a id="agroup__bt__hfp_html_gaaa9fbdceec140f274fc88c063a4cd4b8"></a>
<a id="agroup__bt__hfp_html_gab6710ce433812c3bf785b787008c36be"></a>
<a id="agroup__bt__hfp_html_gab743d3e14fa13b71ddaf26d46cf41fb3"></a>
<a id="agroup__bt__hfp_html_gabacb666eb0f43db8614413a4ae0ce60a"></a>
<a id="agroup__bt__hfp_html_gabbce5fbf0dec27e1c5a4da144fbfc9c1"></a>
<a id="agroup__bt__hfp_html_gac3c038818cda3645eaadc5374d18c3ee"></a>
<a id="agroup__bt__hfp_html_gac4e3d88b80b69840d52050dcd72c9ab3"></a>
<a id="agroup__bt__hfp_html_gac57d7188e3f8b6e1e28d2a55c2567dbf"></a>
<a id="agroup__bt__hfp_html_gad29bf40953faf638cc08acf919eb8f4f"></a>
<a id="agroup__bt__hfp_html_gad5dab4dcb66d52a80e0689a86de5fec3"></a>
<a id="agroup__bt__hfp_html_gaeed952ce163ef2466ece04af24b76a28"></a>
<a id="agroup__bt__hfp_html_gaf5e7ef119731c0dc35bec61fb7c34774"></a>
<a id="agroup__bt__hfp_html_gga38619377f146492993ee9a92a487af50a5a35798fc921e975775c496ac49193c9"></a>
<a id="agroup__bt__hfp_html_gga38619377f146492993ee9a92a487af50a646f51233cf8906d377bf0d6860f3bb0"></a>
<a id="agroup__bt__hfp_html_gga38619377f146492993ee9a92a487af50ac2233c577a6d8b8871b8e31969616f66"></a>
<a id="agroup__bt__hfp_html_gga6c2ba70d70c8f9d6d569662086985c85aa631c2cc079db31712ac2ec7ac3dee3f"></a>
<a id="agroup__bt__hfp_html_gga6c2ba70d70c8f9d6d569662086985c85adf30d13bccb711d32a3c75e5c1d47d97"></a>
<a id="agroup__bt__hfp_html_gga810c80de5baf92feb23650374b60bceea1ea1ba685375baaabab22ad1c01ca6af"></a>
<a id="agroup__bt__hfp_html_gga810c80de5baf92feb23650374b60bceea7377bf80fd685178d0d8b39189b2122a"></a>
<a id="agroup__bt__hfp_html_gga810c80de5baf92feb23650374b60bceea8f8fc15f39de43b1ed202e16cd198104"></a>
<a id="agroup__bt__hfp_html_gga810c80de5baf92feb23650374b60bceea974da5247c5d332b11c42e93c9cbd831"></a>
<a id="agroup__bt__hfp_html_gga810c80de5baf92feb23650374b60bceea9ff342787f8a6f7b9a5c0db1afa1bfb9"></a>
<a id="agroup__bt__hfp_html_gga810c80de5baf92feb23650374b60bceeab4db9c2eb21b5eb79517c0a761bc7dfa"></a>
<a id="agroup__bt__hfp_html_gga810c80de5baf92feb23650374b60bceeabfa959b76eab9fc14ae941e3c1cd45ff"></a>
<a id="agroup__bt__hfp_html_gga862b201be555821e932f6df5599eaa57a1444cacc3f0307e7b53a0375807668c5"></a>
<a id="agroup__bt__hfp_html_gga862b201be555821e932f6df5599eaa57a24ceb35eba4e18dbde198b77a7db98de"></a>
<a id="agroup__bt__hfp_html_gga862b201be555821e932f6df5599eaa57a3f9c27a235db99073918a904d6902eae"></a>
<a id="agroup__bt__hfp_html_gga862b201be555821e932f6df5599eaa57ac5055465440ffe897930cbfdabb7c3d0"></a>
<a id="agroup__bt__hfp_html_gga862b201be555821e932f6df5599eaa57ad0cfee8ab087438502689d12cafa39cf"></a>
<a id="agroup__bt__hfp_html_gga862b201be555821e932f6df5599eaa57ad8620b141e11f48b46b9cd5ef1842fe6"></a>
<a id="agroup__bt__hfp_html_gga862b201be555821e932f6df5599eaa57adb3fae0b3684e8d035e195a91d24deb8"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__hfp__hf__call_html"></a>
<a id="astructbt__hfp__hf__cb_html"></a>
<a id="astructbt__hfp__hf__cb_html_a07da1a6c86031c42749972d5d9fb7677"></a>
<a id="astructbt__hfp__hf__cb_html_a080d9149f6d0beccbcf6562e3129383a"></a>
<a id="astructbt__hfp__hf__cb_html_a0f2da8d9169658c03d2dabe2c8b1cf6f"></a>
<a id="astructbt__hfp__hf__cb_html_a13b35eb32e4f579d853657a2ea89af42"></a>
<a id="astructbt__hfp__hf__cb_html_a17faaab9a9af5dc53018fc2f94855bea"></a>
<a id="astructbt__hfp__hf__cb_html_a2712d3a5d68bdf2de6dc27f938590c0a"></a>
<a id="astructbt__hfp__hf__cb_html_a298a6d3315535331ffb779899db9f973"></a>
<a id="astructbt__hfp__hf__cb_html_a385cbe2c3a9c402a09b873a3ce753d8b"></a>
<a id="astructbt__hfp__hf__cb_html_a44ae68eb055f23c30dd761fd6eb1c6cd"></a>
<a id="astructbt__hfp__hf__cb_html_a4586240506c876c9f58cf60a091b4044"></a>
<a id="astructbt__hfp__hf__cb_html_a46677dbfe7e73dcdc3b6cacb0aa9fa58"></a>
<a id="astructbt__hfp__hf__cb_html_a4977076381a5c4daf620aa6c6ab558d3"></a>
<a id="astructbt__hfp__hf__cb_html_a5083ff06bbe2ed2611a7c67339a82588"></a>
<a id="astructbt__hfp__hf__cb_html_a512de9839559def9c2110a310f21ca03"></a>
<a id="astructbt__hfp__hf__cb_html_a597d2e9b20ffc2dfedd53aea2969727e"></a>
<a id="astructbt__hfp__hf__cb_html_a68c09fe6aac4ff7f3b24e6a550e75d1e"></a>
<a id="astructbt__hfp__hf__cb_html_a691ec076d6fba14636b873cf75262e81"></a>
<a id="astructbt__hfp__hf__cb_html_a6ea6f5a866d7e4da5e3fe894d700f6b6"></a>
<a id="astructbt__hfp__hf__cb_html_a71f0f50a83defe014b3b364dcc16ad9d"></a>
<a id="astructbt__hfp__hf__cb_html_a80e98b5dd212158c255215b8a304d67c"></a>
<a id="astructbt__hfp__hf__cb_html_a8483c3a3ba8b0e5131bec6fce5dbc36d"></a>
<a id="astructbt__hfp__hf__cb_html_a9f248f9c7e3830c6941225bd4d2363d3"></a>
<a id="astructbt__hfp__hf__cb_html_ac049a95f473eb2e31ed4bba665861429"></a>
<a id="astructbt__hfp__hf__cb_html_ac1e9fb5d0446d498b6cf3705a05633e2"></a>
<a id="astructbt__hfp__hf__cb_html_acc1ff77f98329986c2120b0c9c4f565a"></a>
<a id="astructbt__hfp__hf__cb_html_ace8989f64fea9301d6f48e5252ceb2de"></a>
<a id="astructbt__hfp__hf__cb_html_ada56afdf999f5270f84fcf412916e550"></a>
<a id="astructbt__hfp__hf__cb_html_add68ca4e00f7a5dbc28282ee29bea087"></a>
<a id="astructbt__hfp__hf__cb_html_ae5682d96bdf18b148fac7ce1d9cbdb75"></a>
<a id="astructbt__hfp__hf__cb_html_af6fe24140f5a5a1aea2eff7b1e534cfd"></a>
<a id="astructbt__hfp__hf__cb_html_afdf28b8d8f9598ee2f6fa826aba4fbba"></a>
<a id="astructbt__hfp__hf__current__call_html"></a>
<a id="astructbt__hfp__hf__current__call_html_a69968974df79327c5dabd58f1804df2e"></a>
<a id="astructbt__hfp__hf__current__call_html_a6cefa6a215650f8380a54cda44ce5f19"></a>
<a id="astructbt__hfp__hf__current__call_html_a8c2b49def7926a992e84c175eca3aa2e"></a>
<a id="astructbt__hfp__hf__current__call_html_a9f72915247e66423303a77e6d5382d47"></a>
<a id="astructbt__hfp__hf__current__call_html_aa25db76c59d82c16c0a1db1f509104f8"></a>
<a id="astructbt__hfp__hf__current__call_html_ac384ffbde33c521f305f1283520e0c66"></a>
<a id="astructbt__hfp__hf__current__call_html_ae4f1cd6e24e2ef79a009bba9b30c53ee"></a>
<a id="astructbt__hfp__hf_html"></a>

```c


/*
 * Copyright (c) 2015-2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HFP_HF_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HFP_HF_H_


#include <zephyr/bluetooth/bluetooth.h>

#ifdef __cplusplus
extern "C" {
#endif

/* HFP CODEC IDs */
#define BT_HFP_HF_CODEC_CVSD    0x01
#define BT_HFP_HF_CODEC_MSBC    0x02
#define BT_HFP_HF_CODEC_LC3_SWB 0x03

struct bt_hfp_hf;

struct bt_hfp_hf_call;

enum __packed bt_hfp_hf_call_status {
        BT_HFP_HF_CALL_STATUS_ACTIVE = 0,
        BT_HFP_HF_CALL_STATUS_HELD = 1,
        BT_HFP_HF_CALL_STATUS_DIALING = 2,
        BT_HFP_HF_CALL_STATUS_ALERTING = 3,
        BT_HFP_HF_CALL_STATUS_INCOMING = 4,
        BT_HFP_HF_CALL_STATUS_WAITING = 5,
        BT_HFP_HF_CALL_STATUS_INCOMING_HELD = 6
};

enum __packed bt_hfp_hf_call_dir {
        BT_HFP_HF_CALL_DIR_OUTGOING = 0,
        BT_HFP_HF_CALL_DIR_INCOMING = 1,
};

enum __packed bt_hfp_hf_call_mode {
        BT_HFP_HF_CALL_MODE_VOICE = 0,
        BT_HFP_HF_CALL_MODE_DATA = 1,
        BT_HFP_HF_CALL_MODE_FAX = 2,
};

struct bt_hfp_hf_current_call {
        uint8_t index;
        enum bt_hfp_hf_call_dir dir;
        enum bt_hfp_hf_call_status status;
        enum bt_hfp_hf_call_mode mode;
        bool multiparty;
        const char *number;
        uint8_t type;
};

struct bt_hfp_hf_cb {
        void (*connected)(struct bt_conn *conn, struct bt_hfp_hf *hf);
        void (*disconnected)(struct bt_hfp_hf *hf);
        void (*sco_connected)(struct bt_hfp_hf *hf, struct bt_conn *sco_conn);
        void (*sco_disconnected)(struct bt_conn *sco_conn, uint8_t reason);
        void (*service)(struct bt_hfp_hf *hf, uint32_t value);
        void (*outgoing)(struct bt_hfp_hf *hf, struct bt_hfp_hf_call *call);
        void (*remote_ringing)(struct bt_hfp_hf_call *call);
        void (*incoming)(struct bt_hfp_hf *hf, struct bt_hfp_hf_call *call);
        void (*incoming_held)(struct bt_hfp_hf_call *call);
        void (*accept)(struct bt_hfp_hf_call *call);
        void (*reject)(struct bt_hfp_hf_call *call);
        void (*terminate)(struct bt_hfp_hf_call *call);
        void (*held)(struct bt_hfp_hf_call *call);
        void (*retrieve)(struct bt_hfp_hf_call *call);
        void (*signal)(struct bt_hfp_hf *hf, uint32_t value);
        void (*roam)(struct bt_hfp_hf *hf, uint32_t value);
        void (*battery)(struct bt_hfp_hf *hf, uint32_t value);
        void (*ring_indication)(struct bt_hfp_hf_call *call);
        void (*dialing)(struct bt_hfp_hf *hf, int err);
        void (*clip)(struct bt_hfp_hf_call *call, const char *number, uint8_t type);
        void (*vgm)(struct bt_hfp_hf *hf, uint8_t gain);
        void (*vgs)(struct bt_hfp_hf *hf, uint8_t gain);
        void (*inband_ring)(struct bt_hfp_hf *hf, bool inband);
        void (*operator)(struct bt_hfp_hf *hf, uint8_t mode, uint8_t format, const char *operator);
        void (*codec_negotiate)(struct bt_hfp_hf *hf, uint8_t id);
        void (*ecnr_turn_off)(struct bt_hfp_hf *hf, int err);
        void (*call_waiting)(struct bt_hfp_hf_call *call, const char *number, uint8_t type);
        void (*voice_recognition)(struct bt_hfp_hf *hf, bool activate);
        void (*vre_state)(struct bt_hfp_hf *hf, uint8_t state);
        void (*textual_representation)(struct bt_hfp_hf *hf, char *id, uint8_t type,
                                       uint8_t operation, const char *text);
        void (*request_phone_number)(struct bt_hfp_hf *hf, const char *number);

        void (*subscriber_number)(struct bt_hfp_hf *hf, const char *number, uint8_t type,
                                  uint8_t service);

        void (*query_call)(struct bt_hfp_hf *hf, struct bt_hfp_hf_current_call *call);
};

int bt_hfp_hf_register(struct bt_hfp_hf_cb *cb);

int bt_hfp_hf_connect(struct bt_conn *conn, struct bt_hfp_hf **hf, uint8_t channel);

int bt_hfp_hf_disconnect(struct bt_hfp_hf *hf);

int bt_hfp_hf_cli(struct bt_hfp_hf *hf, bool enable);

int bt_hfp_hf_vgm(struct bt_hfp_hf *hf, uint8_t gain);

int bt_hfp_hf_vgs(struct bt_hfp_hf *hf, uint8_t gain);

int bt_hfp_hf_get_operator(struct bt_hfp_hf *hf);

int bt_hfp_hf_accept(struct bt_hfp_hf_call *call);

int bt_hfp_hf_reject(struct bt_hfp_hf_call *call);

int bt_hfp_hf_terminate(struct bt_hfp_hf_call *call);

int bt_hfp_hf_hold_incoming(struct bt_hfp_hf_call *call);

int bt_hfp_hf_query_respond_hold_status(struct bt_hfp_hf *hf);

int bt_hfp_hf_number_call(struct bt_hfp_hf *hf, const char *number);

int bt_hfp_hf_memory_dial(struct bt_hfp_hf *hf, const char *location);

int bt_hfp_hf_redial(struct bt_hfp_hf *hf);

int bt_hfp_hf_audio_connect(struct bt_hfp_hf *hf);

int bt_hfp_hf_select_codec(struct bt_hfp_hf *hf, uint8_t codec_id);

int bt_hfp_hf_set_codecs(struct bt_hfp_hf *hf, uint8_t codec_ids);

int bt_hfp_hf_turn_off_ecnr(struct bt_hfp_hf *hf);

int bt_hfp_hf_call_waiting_notify(struct bt_hfp_hf *hf, bool enable);

int bt_hfp_hf_release_all_held(struct bt_hfp_hf *hf);

int bt_hfp_hf_set_udub(struct bt_hfp_hf *hf);

int bt_hfp_hf_release_active_accept_other(struct bt_hfp_hf *hf);

int bt_hfp_hf_hold_active_accept_other(struct bt_hfp_hf *hf);

int bt_hfp_hf_join_conversation(struct bt_hfp_hf *hf);

int bt_hfp_hf_explicit_call_transfer(struct bt_hfp_hf *hf);

int bt_hfp_hf_release_specified_call(struct bt_hfp_hf_call *call);

int bt_hfp_hf_private_consultation_mode(struct bt_hfp_hf_call *call);

int bt_hfp_hf_voice_recognition(struct bt_hfp_hf *hf, bool activate);

int bt_hfp_hf_ready_to_accept_audio(struct bt_hfp_hf *hf);

int bt_hfp_hf_request_phone_number(struct bt_hfp_hf *hf);

int bt_hfp_hf_transmit_dtmf_code(struct bt_hfp_hf_call *call, char code);

int bt_hfp_hf_query_subscriber(struct bt_hfp_hf *hf);

/* HFP HF Indicators */
enum hfp_hf_ag_indicators {
        HF_SERVICE_IND = 0, /* AG service indicator */
        HF_CALL_IND,        /* AG call indicator */
        HF_CALL_SETUP_IND,  /* AG call setup indicator */
        HF_CALL_HELD_IND,   /* AG call held indicator */
        HF_SIGNAL_IND,      /* AG signal indicator */
        HF_ROAM_IND,        /* AG roaming indicator */
        HF_BATTERY_IND      /* AG battery indicator */
};

int bt_hfp_hf_indicator_status(struct bt_hfp_hf *hf, uint8_t status);

int bt_hfp_hf_enhanced_safety(struct bt_hfp_hf *hf, bool enable);

int bt_hfp_hf_battery(struct bt_hfp_hf *hf, uint8_t level);

int bt_hfp_hf_query_list_of_current_calls(struct bt_hfp_hf *hf);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HFP_HF_H_ */
```

## 17.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015-2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 26 行

免提配置文件（HFP）的编解码器标识符（CODEC IDs）。

### 注释 3：原第 992 行

HFP 免提单元（HF）指示器（Indicators）。

### 注释 4：原第 994 行

音频网关（AG）服务指示器（service indicator）。

### 注释 5：原第 995 行

AG 通话指示器（call indicator）。

### 注释 6：原第 996 行

AG 通话建立指示器（call setup indicator）。

### 注释 7：原第 997 行

AG 通话保持指示器（call held indicator）。

### 注释 8：原第 998 行

AG 信号指示器（signal indicator）。

### 注释 9：原第 999 行

AG 漫游指示器（roaming indicator）。

### 注释 10：原第 1000 行

AG 电池指示器（battery indicator）。

### 注释 11：原第 1067 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HFP_HF_H_`。

## 17.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hfp__hf_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)
- [bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)
- [bt_hfp_hf_call_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga810c80de5baf92feb23650374b60bcee)
- [BT_HFP_HF_CALL_STATUS_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea1ea1ba685375baaabab22ad1c01ca6af)
- [BT_HFP_HF_CALL_STATUS_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceeab4db9c2eb21b5eb79517c0a761bc7dfa)
- [BT_HFP_HF_CALL_STATUS_DIALING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea9ff342787f8a6f7b9a5c0db1afa1bfb9)
- [BT_HFP_HF_CALL_STATUS_ALERTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea7377bf80fd685178d0d8b39189b2122a)
- [BT_HFP_HF_CALL_STATUS_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea8f8fc15f39de43b1ed202e16cd198104)
- [BT_HFP_HF_CALL_STATUS_WAITING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea974da5247c5d332b11c42e93c9cbd831)
- [BT_HFP_HF_CALL_STATUS_INCOMING_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceeabfa959b76eab9fc14ae941e3c1cd45ff)
- [bt_hfp_hf_call_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga6c2ba70d70c8f9d6d569662086985c85)
- [BT_HFP_HF_CALL_DIR_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga6c2ba70d70c8f9d6d569662086985c85aa631c2cc079db31712ac2ec7ac3dee3f)
- [BT_HFP_HF_CALL_DIR_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga6c2ba70d70c8f9d6d569662086985c85adf30d13bccb711d32a3c75e5c1d47d97)
- [bt_hfp_hf_call_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga38619377f146492993ee9a92a487af50)
- [BT_HFP_HF_CALL_MODE_VOICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga38619377f146492993ee9a92a487af50ac2233c577a6d8b8871b8e31969616f66)
- [BT_HFP_HF_CALL_MODE_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga38619377f146492993ee9a92a487af50a5a35798fc921e975775c496ac49193c9)
- [BT_HFP_HF_CALL_MODE_FAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga38619377f146492993ee9a92a487af50a646f51233cf8906d377bf0d6860f3bb0)
- [bt_hfp_hf_current_call](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [index](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#a9f72915247e66423303a77e6d5382d47)
- [dir](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#a69968974df79327c5dabd58f1804df2e)
- [status](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#a8c2b49def7926a992e84c175eca3aa2e)
- [mode](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#ae4f1cd6e24e2ef79a009bba9b30c53ee)
- [multiparty](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#aa25db76c59d82c16c0a1db1f509104f8)
- [number](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#ac384ffbde33c521f305f1283520e0c66)
- [type](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#a6cefa6a215650f8380a54cda44ce5f19)
- [bt_hfp_hf_cb](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md)
- [connected](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a68c09fe6aac4ff7f3b24e6a550e75d1e)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [disconnected](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#afdf28b8d8f9598ee2f6fa826aba4fbba)
- [sco_connected](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a6ea6f5a866d7e4da5e3fe894d700f6b6)
- [sco_disconnected](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a4586240506c876c9f58cf60a091b4044)
- [service](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a8483c3a3ba8b0e5131bec6fce5dbc36d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [outgoing](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a46677dbfe7e73dcdc3b6cacb0aa9fa58)
- [remote_ringing](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#ace8989f64fea9301d6f48e5252ceb2de)
- [incoming](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a597d2e9b20ffc2dfedd53aea2969727e)
- [incoming_held](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a71f0f50a83defe014b3b364dcc16ad9d)
- [accept](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a44ae68eb055f23c30dd761fd6eb1c6cd)
- [reject](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a9f248f9c7e3830c6941225bd4d2363d3)
- [terminate](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a691ec076d6fba14636b873cf75262e81)
- [held](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#af6fe24140f5a5a1aea2eff7b1e534cfd)
- [retrieve](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a4977076381a5c4daf620aa6c6ab558d3)
- [signal](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#add68ca4e00f7a5dbc28282ee29bea087)
- [roam](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a13b35eb32e4f579d853657a2ea89af42)
- [battery](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a17faaab9a9af5dc53018fc2f94855bea)
- [ring_indication](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a2712d3a5d68bdf2de6dc27f938590c0a)
- [dialing](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a80e98b5dd212158c255215b8a304d67c)
- [clip](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#ac049a95f473eb2e31ed4bba665861429)
- [vgm](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a512de9839559def9c2110a310f21ca03)
- [vgs](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a385cbe2c3a9c402a09b873a3ce753d8b)
- [inband_ring](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#acc1ff77f98329986c2120b0c9c4f565a)
- [ecnr_turn_off](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a0f2da8d9169658c03d2dabe2c8b1cf6f)
- [call_waiting](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a5083ff06bbe2ed2611a7c67339a82588)
- [voice_recognition](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a07da1a6c86031c42749972d5d9fb7677)
- [vre_state](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a298a6d3315535331ffb779899db9f973)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [textual_representation](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#ada56afdf999f5270f84fcf412916e550)
- [request_phone_number](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#ac1e9fb5d0446d498b6cf3705a05633e2)
- [subscriber_number](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#ae5682d96bdf18b148fac7ce1d9cbdb75)
- [query_call](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a080d9149f6d0beccbcf6562e3129383a)
- [bt_hfp_hf_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga2e4a7c05a3ba9a32eab50b9904f7f161)
- [bt_hfp_hf_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga302e9ed397b056edef518470c6ea1d62)
- [bt_hfp_hf_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaf5e7ef119731c0dc35bec61fb7c34774)
- [bt_hfp_hf_cli](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga64ac1971dc7b1dacf6685bdc0c71e34c)
- [bt_hfp_hf_vgm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga0602cee7a90ca4afe90b65d748024472)
- [bt_hfp_hf_vgs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga0c1c35b3117f78f43a6300d4ff7dd18b)
- [bt_hfp_hf_get_operator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaaa9fbdceec140f274fc88c063a4cd4b8)
- [bt_hfp_hf_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga5bad80355fd7903abcee84437d399829)
- [bt_hfp_hf_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gac4e3d88b80b69840d52050dcd72c9ab3)
- [bt_hfp_hf_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gabbce5fbf0dec27e1c5a4da144fbfc9c1)
- [bt_hfp_hf_hold_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga540bf6ec23c632b3f736e6302ef32ebd)
- [bt_hfp_hf_query_respond_hold_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga70e086f6a02cb116317a8e80f76abf6d)
- [bt_hfp_hf_number_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gac57d7188e3f8b6e1e28d2a55c2567dbf)
- [bt_hfp_hf_memory_dial](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gabacb666eb0f43db8614413a4ae0ce60a)
- [bt_hfp_hf_redial](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga9611012a35df66fac324b99b16e5d958)
- [bt_hfp_hf_audio_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gad29bf40953faf638cc08acf919eb8f4f)
- [bt_hfp_hf_select_codec](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga34649dbecca2513c0b5bcd0e109b2551)
- [bt_hfp_hf_set_codecs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga91fc2204f50df07567f87a2b7a18e69f)
- [bt_hfp_hf_turn_off_ecnr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga7f37a9c009b4e55b7060d635c5b0c67b)
- [bt_hfp_hf_call_waiting_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga3afb0d82551708975dbeb9c903c3d1fb)
- [bt_hfp_hf_release_all_held](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga06e7e93578601693fa377a240e0d18a7)
- [bt_hfp_hf_set_udub](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga7389e5723e01b661b5e9c9d2114918b8)
- [bt_hfp_hf_release_active_accept_other](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga36be4ff5fd805c4413ba90b1f62b9143)
- [bt_hfp_hf_hold_active_accept_other](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga40de46a6651eb85aa6d04ad66f528803)
- [bt_hfp_hf_join_conversation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga04d9fe3524c9522e98830507886bdfc6)
- [bt_hfp_hf_explicit_call_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga2b48a0938e65899417b2f3ab1fa4c548)
- [bt_hfp_hf_release_specified_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga1ad888c3b967d3f9b2e5ccee303b9ad7)
- [bt_hfp_hf_private_consultation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gac3c038818cda3645eaadc5374d18c3ee)
- [bt_hfp_hf_voice_recognition](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaeed952ce163ef2466ece04af24b76a28)
- [bt_hfp_hf_ready_to_accept_audio](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga3f6b43bf53fa04a6e71e883dc38f988b)
- [bt_hfp_hf_request_phone_number](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga92d89b0b37186688e86091a7a8015245)
- [bt_hfp_hf_transmit_dtmf_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga6a3a6bc61a3a74f5a4a48d7e39bd74a0)
- [bt_hfp_hf_query_subscriber](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gad5dab4dcb66d52a80e0689a86de5fec3)
- [hfp_hf_ag_indicators](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga862b201be555821e932f6df5599eaa57)
- [HF_SERVICE_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57adb3fae0b3684e8d035e195a91d24deb8)
- [HF_CALL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57ad8620b141e11f48b46b9cd5ef1842fe6)
- [HF_CALL_SETUP_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57a24ceb35eba4e18dbde198b77a7db98de)
- [HF_CALL_HELD_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57ad0cfee8ab087438502689d12cafa39cf)
- [HF_SIGNAL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57ac5055465440ffe897930cbfdabb7c3d0)
- [HF_ROAM_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57a3f9c27a235db99073918a904d6902eae)
- [HF_BATTERY_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57a1444cacc3f0307e7b53a0375807668c5)
- [bt_hfp_hf_indicator_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gab743d3e14fa13b71ddaf26d46cf41fb3)
- [bt_hfp_hf_enhanced_safety](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gab6710ce433812c3bf785b787008c36be)
- [bt_hfp_hf_battery](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga2f0e6012503a9b59b03a0fb508d12f88)
- [bt_hfp_hf_query_list_of_current_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga91637662881dd655f8fc8ed6e6f8b973)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [bt_hfp_hf_cb::voice_recognition](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a07da1a6c86031c42749972d5d9fb7677)
- [bt_hfp_hf_cb::query_call](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a080d9149f6d0beccbcf6562e3129383a)
- [bt_hfp_hf_cb::ecnr_turn_off](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a0f2da8d9169658c03d2dabe2c8b1cf6f)
- [bt_hfp_hf_cb::roam](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a13b35eb32e4f579d853657a2ea89af42)
- [bt_hfp_hf_cb::battery](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a17faaab9a9af5dc53018fc2f94855bea)
- [bt_hfp_hf_cb::ring_indication](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a2712d3a5d68bdf2de6dc27f938590c0a)
- [bt_hfp_hf_cb::vre_state](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a298a6d3315535331ffb779899db9f973)
- [bt_hfp_hf_cb::vgs](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a385cbe2c3a9c402a09b873a3ce753d8b)
- [bt_hfp_hf_cb::accept](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a44ae68eb055f23c30dd761fd6eb1c6cd)
- [bt_hfp_hf_cb::sco_disconnected](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a4586240506c876c9f58cf60a091b4044)
- [bt_hfp_hf_cb::outgoing](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a46677dbfe7e73dcdc3b6cacb0aa9fa58)
- [bt_hfp_hf_cb::retrieve](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a4977076381a5c4daf620aa6c6ab558d3)
- [bt_hfp_hf_cb::call_waiting](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a5083ff06bbe2ed2611a7c67339a82588)
- [bt_hfp_hf_cb::vgm](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a512de9839559def9c2110a310f21ca03)
- [bt_hfp_hf_cb::incoming](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a597d2e9b20ffc2dfedd53aea2969727e)
- [bt_hfp_hf_cb::connected](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a68c09fe6aac4ff7f3b24e6a550e75d1e)
- [bt_hfp_hf_cb::terminate](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a691ec076d6fba14636b873cf75262e81)
- [bt_hfp_hf_cb::sco_connected](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a6ea6f5a866d7e4da5e3fe894d700f6b6)
- [bt_hfp_hf_cb::incoming_held](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a71f0f50a83defe014b3b364dcc16ad9d)
- [bt_hfp_hf_cb::dialing](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a80e98b5dd212158c255215b8a304d67c)
- [bt_hfp_hf_cb::service](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a8483c3a3ba8b0e5131bec6fce5dbc36d)
- [bt_hfp_hf_cb::reject](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#a9f248f9c7e3830c6941225bd4d2363d3)
- [bt_hfp_hf_cb::clip](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#ac049a95f473eb2e31ed4bba665861429)
- [bt_hfp_hf_cb::request_phone_number](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#ac1e9fb5d0446d498b6cf3705a05633e2)
- [bt_hfp_hf_cb::inband_ring](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#acc1ff77f98329986c2120b0c9c4f565a)
- [bt_hfp_hf_cb::remote_ringing](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#ace8989f64fea9301d6f48e5252ceb2de)
- [bt_hfp_hf_cb::textual_representation](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#ada56afdf999f5270f84fcf412916e550)
- [bt_hfp_hf_cb::signal](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#add68ca4e00f7a5dbc28282ee29bea087)
- [bt_hfp_hf_cb::subscriber_number](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#ae5682d96bdf18b148fac7ce1d9cbdb75)
- [bt_hfp_hf_cb::held](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#af6fe24140f5a5a1aea2eff7b1e534cfd)
- [bt_hfp_hf_cb::disconnected](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md#afdf28b8d8f9598ee2f6fa826aba4fbba)
- [bt_hfp_hf_current_call::dir](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#a69968974df79327c5dabd58f1804df2e)
- [bt_hfp_hf_current_call::type](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#a6cefa6a215650f8380a54cda44ce5f19)
- [bt_hfp_hf_current_call::status](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#a8c2b49def7926a992e84c175eca3aa2e)
- [bt_hfp_hf_current_call::index](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#a9f72915247e66423303a77e6d5382d47)
- [bt_hfp_hf_current_call::multiparty](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#aa25db76c59d82c16c0a1db1f509104f8)
- [bt_hfp_hf_current_call::number](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#ac384ffbde33c521f305f1283520e0c66)
- [bt_hfp_hf_current_call::mode](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md#ae4f1cd6e24e2ef79a009bba9b30c53ee)

---

[上一章](P016_gap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P018_kobject_internal.h_源码浏览.md)
