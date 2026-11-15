---
id: learning.zephyr-docs.api-source-reference.page-132
title: direction.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/direction_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第132章\_direction.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html)。

## 132.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
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
<a id="l00014"></a>
<a id="foldopen00016"></a>
<a id="l00016"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00026"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00051"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="foldopen00159"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="foldopen00168"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="foldopen00198"></a>
<a id="l00198"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="foldopen00210"></a>
<a id="l00210"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="adirection_8h_html_a248cd22ad9afe050e3d535f7124112d9"></a>
<a id="adirection_8h_html_a26c40ea36de60266f029763551cd9d4e"></a>
<a id="adirection_8h_html_a53df7da4b178b4a6e4dd68e9266c0771"></a>
<a id="adirection_8h_html_a53df7da4b178b4a6e4dd68e9266c0771a25db2bd4a02678b2ea026ec47b6c2b1b"></a>
<a id="adirection_8h_html_a53df7da4b178b4a6e4dd68e9266c0771a82ee06924dbf1fd3f9c68891b1ccdef4"></a>
<a id="adirection_8h_html_a546598ce9a81161ad1ba098a7b1a8df4"></a>
<a id="adirection_8h_html_a546598ce9a81161ad1ba098a7b1a8df4a68c89c394d7a1d92560a1e51fa1b069a"></a>
<a id="adirection_8h_html_a546598ce9a81161ad1ba098a7b1a8df4ad59a9caab9aeced1f95dd1fe8778fe38"></a>
<a id="adirection_8h_html_a5e4a5168020d488561646beac48916f5"></a>
<a id="adirection_8h_html_a64bf01dee8bc4bbc62e0dbc356726a05"></a>
<a id="adirection_8h_html_a64bf01dee8bc4bbc62e0dbc356726a05a1f24630a9b6afc19e1f671a4b5906dd1"></a>
<a id="adirection_8h_html_a64bf01dee8bc4bbc62e0dbc356726a05a331e4cc8da9f583ad18422cd260018da"></a>
<a id="adirection_8h_html_a64bf01dee8bc4bbc62e0dbc356726a05a3e1c5452412a00c994ad005858e03ac7"></a>
<a id="adirection_8h_html_a64bf01dee8bc4bbc62e0dbc356726a05a6c91466a8e8dfe73665749b263b26207"></a>
<a id="adirection_8h_html_a64bf01dee8bc4bbc62e0dbc356726a05aeeb9304adba4363faaa8e3d299abfdb8"></a>
<a id="adirection_8h_html_a84fee1f1ac25af73bb7a8f91ed912c67"></a>
<a id="adirection_8h_html_a856cfbe26fba92c80f4cf6012a0bbafe"></a>
<a id="adirection_8h_html_a861696041baa770ef3968789afd4cbac"></a>
<a id="adirection_8h_html_a92d0b485a83a7395b3613b144b6e749f"></a>
<a id="adirection_8h_html_a953634e6a88617a8729541d6b5bd0dd6"></a>
<a id="adirection_8h_html_a953634e6a88617a8729541d6b5bd0dd6a53596e4aa9a96006cee3c899150d7a0e"></a>
<a id="adirection_8h_html_a953634e6a88617a8729541d6b5bd0dd6a7f3f42ede92bafd169620bebddc75512"></a>
<a id="adirection_8h_html_a953634e6a88617a8729541d6b5bd0dd6acd6f87bd43540cc1b44e5e023a4d0519"></a>
<a id="adirection_8h_html_aa0eba41c1a810c9592e0097ee4fe7329"></a>
<a id="adirection_8h_html_ab03ec552192056eb8ddb9aae49029265"></a>
<a id="adirection_8h_html_ab9acadbaf03dd976a2ee185574effb4c"></a>
<a id="adirection_8h_html_ab9acadbaf03dd976a2ee185574effb4ca10328e978a6641f5f787f4f4e9b50d6c"></a>
<a id="adirection_8h_html_ab9acadbaf03dd976a2ee185574effb4ca70ea13abb5e1626304f8ef4e22564a8b"></a>
<a id="adirection_8h_html_ab9acadbaf03dd976a2ee185574effb4cacdc558d9892228b4403cb782ed2260f9"></a>
<a id="adirection_8h_html_ab9acadbaf03dd976a2ee185574effb4cadf830cbbe3043423eff237b983bf1c92"></a>
<a id="adirection_8h_html_ac2064484bb3c4ea6ae5eb684f3ace008"></a>
<a id="adirection_8h_html_ade1a048c3fdf11e979fa9a74f33bc375"></a>
<a id="adirection_8h_html_ae98248377f111deb6aa0565db1d3f690"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__df__adv__cte__tx__param_html"></a>
<a id="astructbt__df__adv__cte__tx__param_html_a288d635221a752b231033803acddd261"></a>
<a id="astructbt__df__adv__cte__tx__param_html_a2ab62db4279338e05cd9e5c222c3aab2"></a>
<a id="astructbt__df__adv__cte__tx__param_html_a4af32abbb603d1b7a533771a23d6e9ee"></a>
<a id="astructbt__df__adv__cte__tx__param_html_ac1f251cb2205ce345dc3815b53f13918"></a>
<a id="astructbt__df__adv__cte__tx__param_html_ac974c5bb804912f5940b2ede5f6394a1"></a>
<a id="astructbt__df__conn__cte__req__params_html"></a>
<a id="astructbt__df__conn__cte__req__params_html_a71340a450e573612a271467c51110166"></a>
<a id="astructbt__df__conn__cte__req__params_html_ab8148905943e0d87a37740ab891b9ef7"></a>
<a id="astructbt__df__conn__cte__req__params_html_ae8232614ec9201e4572675d793b2292a"></a>
<a id="astructbt__df__conn__cte__rx__param_html"></a>
<a id="astructbt__df__conn__cte__rx__param_html_a3401f31865ced48d89c2b4560bcd4512"></a>
<a id="astructbt__df__conn__cte__rx__param_html_a35c2aac4512e2ffce19346c9bf51f033"></a>
<a id="astructbt__df__conn__cte__rx__param_html_aee2ed2d86e2740e166434ede099b1250"></a>
<a id="astructbt__df__conn__cte__rx__param_html_afe2dae75b7138b374f991c58f8143c9d"></a>
<a id="astructbt__df__conn__cte__tx__param_html"></a>
<a id="astructbt__df__conn__cte__tx__param_html_a9df1dac6180e77a4c7abc80890346c4a"></a>
<a id="astructbt__df__conn__cte__tx__param_html_ad49bc64170e8ee4741aa01393284e7de"></a>
<a id="astructbt__df__conn__cte__tx__param_html_af78df8115d2fac5b8f6132b48a56bc1c"></a>
<a id="astructbt__df__conn__iq__samples__report_html"></a>
<a id="astructbt__df__conn__iq__samples__report_html_a1e7901b81c8618e4515cd22a681b4d43"></a>
<a id="astructbt__df__conn__iq__samples__report_html_a4d467a7ac76dc9ed6331c10172895097"></a>
<a id="astructbt__df__conn__iq__samples__report_html_a55e1d7d31557f0e1f59ad91834460b78"></a>
<a id="astructbt__df__conn__iq__samples__report_html_a578132e4a88e739451cf80eba7345094"></a>
<a id="astructbt__df__conn__iq__samples__report_html_a60500e954e2694a209c2d103887b2685"></a>
<a id="astructbt__df__conn__iq__samples__report_html_a7c5147b426bb87f9d11c8bdffb91ff02"></a>
<a id="astructbt__df__conn__iq__samples__report_html_a9374ecd1437f532dec863c527d22348d"></a>
<a id="astructbt__df__conn__iq__samples__report_html_aa9b177817075e3781256ec2c7d5ac0ce"></a>
<a id="astructbt__df__conn__iq__samples__report_html_aac825fbdecd6a5a82da0097a8694fb65"></a>
<a id="astructbt__df__conn__iq__samples__report_html_ab6e31e979bba969a18804cf8c9b88f03"></a>
<a id="astructbt__df__conn__iq__samples__report_html_ac14e792a3ce2f3297ddab49e801ba640"></a>
<a id="astructbt__df__conn__iq__samples__report_html_ac7f3993bd20bd44354f15f098e423c33"></a>
<a id="astructbt__df__conn__iq__samples__report_html_afdc456a8af5a31ee62c489534af3ecdb"></a>
<a id="astructbt__df__per__adv__sync__cte__rx__param_html"></a>
<a id="astructbt__df__per__adv__sync__cte__rx__param_html_a1740d3f41dddd755fc1e04216c8070e5"></a>
<a id="astructbt__df__per__adv__sync__cte__rx__param_html_abff68c9f2e42e3fe6e8b155f5390f219"></a>
<a id="astructbt__df__per__adv__sync__cte__rx__param_html_ac64232b5e9b2c6acfadfca1c95fd1021"></a>
<a id="astructbt__df__per__adv__sync__cte__rx__param_html_ac83de1a86fef076d6c8fc6bccbe49a64"></a>
<a id="astructbt__df__per__adv__sync__cte__rx__param_html_ae358cbd7b1dd59a7d0a931c8a5fbd94d"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html_a0b07042bad2a28065b8ea4def73c91d3"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html_a1a9c763fa7dd445b5dea8c2bb7b82bc0"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html_a48793aad0f603d1763f06453e837a9d9"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html_a4d1da7208e043f5ae015612cee16ee25"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html_a64c2936dc8180fc34651b18199241a9b"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html_a6fea28c1d3b00f1fd7bcb7264f4c3fc9"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html_a88d950cdaa4f08a0fa3eb26f1fed7982"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html_aa81e74769290f427b60398eb976b4a2a"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html_ab256dc21c5d707a9195967caaa13e3e0"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html_ad4d213aa20a0c2fe329606ed789436fd"></a>
<a id="astructbt__df__per__adv__sync__iq__samples__report_html_ae0a28844a5588af05bbde046f6355ddf"></a>
<a id="astructbt__hci__le__iq__sample16_html"></a>
<a id="astructbt__hci__le__iq__sample_html"></a>
<a id="astructbt__le__ext__adv_html"></a>
<a id="astructbt__le__per__adv__sync_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_DIRECTION_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_DIRECTION_H_

#include <stdint.h>

#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/sys/util_macro.h>

enum bt_df_cte_type {
        BT_DF_CTE_TYPE_NONE = 0,
        BT_DF_CTE_TYPE_AOA = BIT(0),
        BT_DF_CTE_TYPE_AOD_1US = BIT(1),
        BT_DF_CTE_TYPE_AOD_2US = BIT(2),
        BT_DF_CTE_TYPE_ALL = (BT_DF_CTE_TYPE_AOA | BT_DF_CTE_TYPE_AOD_1US | BT_DF_CTE_TYPE_AOD_2US)
};

enum bt_df_antenna_switching_slot {
        BT_DF_ANTENNA_SWITCHING_SLOT_1US = 0x1,
        BT_DF_ANTENNA_SWITCHING_SLOT_2US = 0x2
};

enum bt_df_packet_status {
        BT_DF_CTE_CRC_OK = 0x0,
        BT_DF_CTE_CRC_ERR_CTE_BASED_TIME = 0x1,
        BT_DF_CTE_CRC_ERR_CTE_BASED_OTHER = 0x2,
        BT_DF_CTE_INSUFFICIENT_RESOURCES = 0xFF
};

struct bt_df_adv_cte_tx_param {
        uint8_t  cte_len;
        uint8_t  cte_type;
        uint8_t  cte_count;
        uint8_t  num_ant_ids;
        uint8_t  *ant_ids;
};

struct bt_df_per_adv_sync_cte_rx_param {
        uint8_t cte_types;
        uint8_t slot_durations;
        uint8_t max_cte_count;
        uint8_t num_ant_ids;
        const uint8_t *ant_ids;
};

enum bt_df_iq_sample {
        BT_DF_IQ_SAMPLE_8_BITS_INT,
        BT_DF_IQ_SAMPLE_16_BITS_INT,
};

struct bt_df_per_adv_sync_iq_samples_report {
        uint8_t chan_idx;
        int16_t rssi;
        uint8_t rssi_ant_id;
        uint8_t cte_type;
        uint8_t slot_durations;
        uint8_t packet_status;
        uint16_t per_evt_counter;
        uint8_t sample_count;
        enum bt_df_iq_sample sample_type;
        union {
                struct bt_hci_le_iq_sample const *sample;
                struct bt_hci_le_iq_sample16 const *sample16;
        };
};

struct bt_df_conn_cte_rx_param {
        uint8_t cte_types;
        uint8_t slot_durations;
        uint8_t num_ant_ids;
        const uint8_t *ant_ids;
};

enum bt_df_conn_iq_report_err {
        BT_DF_IQ_REPORT_ERR_SUCCESS,
        BT_DF_IQ_REPORT_ERR_NO_CTE,
        BT_DF_IQ_REPORT_ERR_PEER_REJECTED,
};

struct bt_df_conn_iq_samples_report {
        enum bt_df_conn_iq_report_err err;
        uint8_t rx_phy;
        uint8_t chan_idx;
        int16_t rssi;
        uint8_t rssi_ant_id;
        uint8_t cte_type;
        uint8_t slot_durations;
        uint8_t packet_status;
        uint16_t conn_evt_counter;
        enum bt_df_iq_sample sample_type;
        uint8_t sample_count;
        union {
                struct bt_hci_le_iq_sample const *sample;
                struct bt_hci_le_iq_sample16 const *sample16;
        };
};

struct bt_df_conn_cte_tx_param {
        uint8_t cte_types;
        uint8_t num_ant_ids;
        const uint8_t *ant_ids;
};

struct bt_df_conn_cte_req_params {
        uint16_t interval;
        uint8_t cte_length;
        uint8_t cte_type;
};

int bt_df_set_adv_cte_tx_param(struct bt_le_ext_adv *adv,
                               const struct bt_df_adv_cte_tx_param *params);

int bt_df_adv_cte_tx_enable(struct bt_le_ext_adv *adv);

int bt_df_adv_cte_tx_disable(struct bt_le_ext_adv *adv);

int bt_df_per_adv_sync_cte_rx_enable(struct bt_le_per_adv_sync *sync,
                                     const struct bt_df_per_adv_sync_cte_rx_param *params);

int bt_df_per_adv_sync_cte_rx_disable(struct bt_le_per_adv_sync *sync);

int bt_df_conn_cte_rx_enable(struct bt_conn *conn, const struct bt_df_conn_cte_rx_param *params);

int bt_df_conn_cte_rx_disable(struct bt_conn *conn);

int bt_df_set_conn_cte_tx_param(struct bt_conn *conn, const struct bt_df_conn_cte_tx_param *params);

int bt_df_conn_cte_req_enable(struct bt_conn *conn, const struct bt_df_conn_cte_req_params *params);

int bt_df_conn_cte_req_disable(struct bt_conn *conn);

int bt_df_conn_cte_rsp_enable(struct bt_conn *conn);

int bt_df_conn_cte_rsp_disable(struct bt_conn *conn);

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_DIRECTION_H_ */
```

## 132.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 365 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_DIRECTION_H_`。

## 132.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_df_cte_type](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05)
- [BT_DF_CTE_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05a1f24630a9b6afc19e1f671a4b5906dd1)
- [BT_DF_CTE_TYPE_AOA](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05a6c91466a8e8dfe73665749b263b26207)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_DF_CTE_TYPE_AOD_1US](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05a331e4cc8da9f583ad18422cd260018da)
- [BT_DF_CTE_TYPE_AOD_2US](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05aeeb9304adba4363faaa8e3d299abfdb8)
- [BT_DF_CTE_TYPE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05a3e1c5452412a00c994ad005858e03ac7)
- [bt_df_antenna_switching_slot](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a546598ce9a81161ad1ba098a7b1a8df4)
- [BT_DF_ANTENNA_SWITCHING_SLOT_1US](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a546598ce9a81161ad1ba098a7b1a8df4a68c89c394d7a1d92560a1e51fa1b069a)
- [BT_DF_ANTENNA_SWITCHING_SLOT_2US](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a546598ce9a81161ad1ba098a7b1a8df4ad59a9caab9aeced1f95dd1fe8778fe38)
- [bt_df_packet_status](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#ab9acadbaf03dd976a2ee185574effb4c)
- [BT_DF_CTE_CRC_OK](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#ab9acadbaf03dd976a2ee185574effb4ca10328e978a6641f5f787f4f4e9b50d6c)
- [BT_DF_CTE_CRC_ERR_CTE_BASED_TIME](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#ab9acadbaf03dd976a2ee185574effb4cadf830cbbe3043423eff237b983bf1c92)
- [BT_DF_CTE_CRC_ERR_CTE_BASED_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#ab9acadbaf03dd976a2ee185574effb4cacdc558d9892228b4403cb782ed2260f9)
- [BT_DF_CTE_INSUFFICIENT_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#ab9acadbaf03dd976a2ee185574effb4ca70ea13abb5e1626304f8ef4e22564a8b)
- [bt_df_adv_cte_tx_param](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cte_len](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md#a2ab62db4279338e05cd9e5c222c3aab2)
- [cte_type](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md#a4af32abbb603d1b7a533771a23d6e9ee)
- [cte_count](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md#a288d635221a752b231033803acddd261)
- [num_ant_ids](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md#ac974c5bb804912f5940b2ede5f6394a1)
- [ant_ids](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md#ac1f251cb2205ce345dc3815b53f13918)
- [bt_df_per_adv_sync_cte_rx_param](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md)
- [cte_types](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md#a1740d3f41dddd755fc1e04216c8070e5)
- [slot_durations](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md#abff68c9f2e42e3fe6e8b155f5390f219)
- [max_cte_count](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md#ac64232b5e9b2c6acfadfca1c95fd1021)
- [num_ant_ids](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md#ae358cbd7b1dd59a7d0a931c8a5fbd94d)
- [ant_ids](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md#ac83de1a86fef076d6c8fc6bccbe49a64)
- [bt_df_iq_sample](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a53df7da4b178b4a6e4dd68e9266c0771)
- [BT_DF_IQ_SAMPLE_8_BITS_INT](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a53df7da4b178b4a6e4dd68e9266c0771a82ee06924dbf1fd3f9c68891b1ccdef4)
- [BT_DF_IQ_SAMPLE_16_BITS_INT](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a53df7da4b178b4a6e4dd68e9266c0771a25db2bd4a02678b2ea026ec47b6c2b1b)
- [bt_df_per_adv_sync_iq_samples_report](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md)
- [chan_idx](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#ad4d213aa20a0c2fe329606ed789436fd)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [rssi](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a48793aad0f603d1763f06453e837a9d9)
- [rssi_ant_id](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a0b07042bad2a28065b8ea4def73c91d3)
- [cte_type](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#aa81e74769290f427b60398eb976b4a2a)
- [slot_durations](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#ab256dc21c5d707a9195967caaa13e3e0)
- [packet_status](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a6fea28c1d3b00f1fd7bcb7264f4c3fc9)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [per_evt_counter](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a1a9c763fa7dd445b5dea8c2bb7b82bc0)
- [sample_count](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a4d1da7208e043f5ae015612cee16ee25)
- [sample_type](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a88d950cdaa4f08a0fa3eb26f1fed7982)
- [bt_hci_le_iq_sample](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md)
- [sample](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a64c2936dc8180fc34651b18199241a9b)
- [bt_hci_le_iq_sample16](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md)
- [sample16](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#ae0a28844a5588af05bbde046f6355ddf)
- [bt_df_conn_cte_rx_param](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md)
- [cte_types](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md#a3401f31865ced48d89c2b4560bcd4512)
- [slot_durations](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md#afe2dae75b7138b374f991c58f8143c9d)
- [num_ant_ids](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md#aee2ed2d86e2740e166434ede099b1250)
- [ant_ids](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md#a35c2aac4512e2ffce19346c9bf51f033)
- [bt_df_conn_iq_report_err](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a953634e6a88617a8729541d6b5bd0dd6)
- [BT_DF_IQ_REPORT_ERR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a953634e6a88617a8729541d6b5bd0dd6acd6f87bd43540cc1b44e5e023a4d0519)
- [BT_DF_IQ_REPORT_ERR_NO_CTE](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a953634e6a88617a8729541d6b5bd0dd6a53596e4aa9a96006cee3c899150d7a0e)
- [BT_DF_IQ_REPORT_ERR_PEER_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a953634e6a88617a8729541d6b5bd0dd6a7f3f42ede92bafd169620bebddc75512)
- [bt_df_conn_iq_samples_report](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md)
- [err](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#ab6e31e979bba969a18804cf8c9b88f03)
- [rx_phy](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#ac14e792a3ce2f3297ddab49e801ba640)
- [chan_idx](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a9374ecd1437f532dec863c527d22348d)
- [rssi](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#aac825fbdecd6a5a82da0097a8694fb65)
- [rssi_ant_id](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a7c5147b426bb87f9d11c8bdffb91ff02)
- [cte_type](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a4d467a7ac76dc9ed6331c10172895097)
- [slot_durations](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a578132e4a88e739451cf80eba7345094)
- [packet_status](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#afdc456a8af5a31ee62c489534af3ecdb)
- [conn_evt_counter](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#ac7f3993bd20bd44354f15f098e423c33)
- [sample_type](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a1e7901b81c8618e4515cd22a681b4d43)
- [sample_count](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a60500e954e2694a209c2d103887b2685)
- [sample](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#aa9b177817075e3781256ec2c7d5ac0ce)
- [sample16](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a55e1d7d31557f0e1f59ad91834460b78)
- [bt_df_conn_cte_tx_param](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md)
- [cte_types](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md#af78df8115d2fac5b8f6132b48a56bc1c)
- [num_ant_ids](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md#ad49bc64170e8ee4741aa01393284e7de)
- [ant_ids](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md#a9df1dac6180e77a4c7abc80890346c4a)
- [bt_df_conn_cte_req_params](../bluetooth_connection_model_reference/P043_bt_df_conn_cte_req_params_结构体.md)
- [interval](../bluetooth_connection_model_reference/P043_bt_df_conn_cte_req_params_结构体.md#ab8148905943e0d87a37740ab891b9ef7)
- [cte_length](../bluetooth_connection_model_reference/P043_bt_df_conn_cte_req_params_结构体.md#a71340a450e573612a271467c51110166)
- [cte_type](../bluetooth_connection_model_reference/P043_bt_df_conn_cte_req_params_结构体.md#ae8232614ec9201e4572675d793b2292a)
- [bt_df_set_adv_cte_tx_param](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#ae98248377f111deb6aa0565db1d3f690)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_df_adv_cte_tx_enable](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#ab03ec552192056eb8ddb9aae49029265)
- [bt_df_adv_cte_tx_disable](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a248cd22ad9afe050e3d535f7124112d9)
- [bt_df_per_adv_sync_cte_rx_enable](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a26c40ea36de60266f029763551cd9d4e)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [bt_df_per_adv_sync_cte_rx_disable](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#ac2064484bb3c4ea6ae5eb684f3ace008)
- [bt_df_conn_cte_rx_enable](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a92d0b485a83a7395b3613b144b6e749f)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_df_conn_cte_rx_disable](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a861696041baa770ef3968789afd4cbac)
- [bt_df_set_conn_cte_tx_param](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#aa0eba41c1a810c9592e0097ee4fe7329)
- [bt_df_conn_cte_req_enable](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a84fee1f1ac25af73bb7a8f91ed912c67)
- [bt_df_conn_cte_req_disable](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#ade1a048c3fdf11e979fa9a74f33bc375)
- [bt_df_conn_cte_rsp_enable](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a5e4a5168020d488561646beac48916f5)
- [bt_df_conn_cte_rsp_disable](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a856cfbe26fba92c80f4cf6012a0bbafe)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [bt_df_adv_cte_tx_param::cte_count](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md#a288d635221a752b231033803acddd261)
- [bt_df_adv_cte_tx_param::cte_len](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md#a2ab62db4279338e05cd9e5c222c3aab2)
- [bt_df_adv_cte_tx_param::cte_type](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md#a4af32abbb603d1b7a533771a23d6e9ee)
- [bt_df_adv_cte_tx_param::ant_ids](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md#ac1f251cb2205ce345dc3815b53f13918)
- [bt_df_adv_cte_tx_param::num_ant_ids](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md#ac974c5bb804912f5940b2ede5f6394a1)
- [bt_df_conn_cte_req_params::cte_length](../bluetooth_connection_model_reference/P043_bt_df_conn_cte_req_params_结构体.md#a71340a450e573612a271467c51110166)
- [bt_df_conn_cte_req_params::interval](../bluetooth_connection_model_reference/P043_bt_df_conn_cte_req_params_结构体.md#ab8148905943e0d87a37740ab891b9ef7)
- [bt_df_conn_cte_req_params::cte_type](../bluetooth_connection_model_reference/P043_bt_df_conn_cte_req_params_结构体.md#ae8232614ec9201e4572675d793b2292a)
- [bt_df_conn_cte_rx_param::cte_types](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md#a3401f31865ced48d89c2b4560bcd4512)
- [bt_df_conn_cte_rx_param::ant_ids](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md#a35c2aac4512e2ffce19346c9bf51f033)
- [bt_df_conn_cte_rx_param::num_ant_ids](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md#aee2ed2d86e2740e166434ede099b1250)
- [bt_df_conn_cte_rx_param::slot_durations](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md#afe2dae75b7138b374f991c58f8143c9d)
- [bt_df_conn_cte_tx_param::ant_ids](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md#a9df1dac6180e77a4c7abc80890346c4a)
- [bt_df_conn_cte_tx_param::num_ant_ids](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md#ad49bc64170e8ee4741aa01393284e7de)
- [bt_df_conn_cte_tx_param::cte_types](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md#af78df8115d2fac5b8f6132b48a56bc1c)
- [bt_df_conn_iq_samples_report::sample_type](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a1e7901b81c8618e4515cd22a681b4d43)
- [bt_df_conn_iq_samples_report::cte_type](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a4d467a7ac76dc9ed6331c10172895097)
- [bt_df_conn_iq_samples_report::sample16](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a55e1d7d31557f0e1f59ad91834460b78)
- [bt_df_conn_iq_samples_report::slot_durations](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a578132e4a88e739451cf80eba7345094)
- [bt_df_conn_iq_samples_report::sample_count](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a60500e954e2694a209c2d103887b2685)
- [bt_df_conn_iq_samples_report::rssi_ant_id](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a7c5147b426bb87f9d11c8bdffb91ff02)
- [bt_df_conn_iq_samples_report::chan_idx](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#a9374ecd1437f532dec863c527d22348d)
- [bt_df_conn_iq_samples_report::sample](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#aa9b177817075e3781256ec2c7d5ac0ce)
- [bt_df_conn_iq_samples_report::rssi](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#aac825fbdecd6a5a82da0097a8694fb65)
- [bt_df_conn_iq_samples_report::err](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#ab6e31e979bba969a18804cf8c9b88f03)
- [bt_df_conn_iq_samples_report::rx_phy](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#ac14e792a3ce2f3297ddab49e801ba640)
- [bt_df_conn_iq_samples_report::conn_evt_counter](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#ac7f3993bd20bd44354f15f098e423c33)
- [bt_df_conn_iq_samples_report::packet_status](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md#afdc456a8af5a31ee62c489534af3ecdb)
- [bt_df_per_adv_sync_cte_rx_param::cte_types](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md#a1740d3f41dddd755fc1e04216c8070e5)
- [bt_df_per_adv_sync_cte_rx_param::slot_durations](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md#abff68c9f2e42e3fe6e8b155f5390f219)
- [bt_df_per_adv_sync_cte_rx_param::max_cte_count](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md#ac64232b5e9b2c6acfadfca1c95fd1021)
- [bt_df_per_adv_sync_cte_rx_param::ant_ids](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md#ac83de1a86fef076d6c8fc6bccbe49a64)
- [bt_df_per_adv_sync_cte_rx_param::num_ant_ids](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md#ae358cbd7b1dd59a7d0a931c8a5fbd94d)
- [bt_df_per_adv_sync_iq_samples_report::rssi_ant_id](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a0b07042bad2a28065b8ea4def73c91d3)
- [bt_df_per_adv_sync_iq_samples_report::per_evt_counter](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a1a9c763fa7dd445b5dea8c2bb7b82bc0)
- [bt_df_per_adv_sync_iq_samples_report::rssi](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a48793aad0f603d1763f06453e837a9d9)
- [bt_df_per_adv_sync_iq_samples_report::sample_count](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a4d1da7208e043f5ae015612cee16ee25)
- [bt_df_per_adv_sync_iq_samples_report::sample](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a64c2936dc8180fc34651b18199241a9b)
- [bt_df_per_adv_sync_iq_samples_report::packet_status](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a6fea28c1d3b00f1fd7bcb7264f4c3fc9)
- [bt_df_per_adv_sync_iq_samples_report::sample_type](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#a88d950cdaa4f08a0fa3eb26f1fed7982)
- [bt_df_per_adv_sync_iq_samples_report::cte_type](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#aa81e74769290f427b60398eb976b4a2a)
- [bt_df_per_adv_sync_iq_samples_report::slot_durations](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#ab256dc21c5d707a9195967caaa13e3e0)
- [bt_df_per_adv_sync_iq_samples_report::chan_idx](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#ad4d213aa20a0c2fe329606ed789436fd)
- [bt_df_per_adv_sync_iq_samples_report::sample16](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md#ae0a28844a5588af05bbde046f6355ddf)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P131_dhcpv6_server.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P133_dirent.h_源码浏览.md)
