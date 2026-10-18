---
id: learning.zephyr-docs.api-source-configuration-reference.page-11
title: cfg.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cfg_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_cfg.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cfg_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cfg_8h.html)。

## 11.1\_原始可见代码（Source Code）

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
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
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
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00313"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00508"></a>
<a id="l00514"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="agroup__bt__mesh__cfg__app_html_ga0110ef750489af49a156a259c5a95c9b"></a>
<a id="agroup__bt__mesh__cfg__app_html_ga42c46a936e589460225a1fa69598a1ac"></a>
<a id="agroup__bt__mesh__cfg__app_html_ga5ae73ef766f0e1c38c0414c0a34e4053"></a>
<a id="agroup__bt__mesh__cfg__app_html_gaa0e80a19c14d47808fc11459bf5ea2eb"></a>
<a id="agroup__bt__mesh__cfg__app_html_gad7a949a0a814f6c9a26816c076d8b92a"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_ga0fd04bff5423a36b013089a4ba351d67"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_ga47236f48940303be27fa6af4797424c2"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_ga555b4a7127869355fdf6040b8d14f999"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_ga59bf9f022665edc0ad03267e4bd16632"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_ga5aa3e7f6b64e1b8b98f9737606d5d1ec"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_ga683d1f9abe82649a774b3d53dcaced8e"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_ga6a6ba6ac1dcbe5f6cfce9bbf38c1851f"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_gad251907892150649f3f1ae6b4112cd84"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_gad48780acaae085350a8b48d033717bfa"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_gaec9d827d5f026b473f3ac88988d3c842"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_gaef15af43e74e3c71590c63c5f1e3ea55"></a>
<a id="agroup__bt__mesh__cfg_html_ga01abb07d27edef40ffff4da968065c1d"></a>
<a id="agroup__bt__mesh__cfg_html_ga037375c99abb492d30378deca183071d"></a>
<a id="agroup__bt__mesh__cfg_html_ga08b336fa1a4a721ac9b10fbb75e4af6b"></a>
<a id="agroup__bt__mesh__cfg_html_ga0a3557a71597885a31cf209c6b83cedb"></a>
<a id="agroup__bt__mesh__cfg_html_ga15de1cdc964628b6f001ef893021ce6e"></a>
<a id="agroup__bt__mesh__cfg_html_ga1afc5ec210bbc6090ada922ddf75e284"></a>
<a id="agroup__bt__mesh__cfg_html_ga256d00139ca40eb99303fef766a3add7"></a>
<a id="agroup__bt__mesh__cfg_html_ga26023b727e1b180263b22d0ade145f81"></a>
<a id="agroup__bt__mesh__cfg_html_ga2c8dc9ee5c3862790efd2a74a1ef6873"></a>
<a id="agroup__bt__mesh__cfg_html_ga346244dcc70afe3a85e85c28c56b4f49"></a>
<a id="agroup__bt__mesh__cfg_html_ga479c14f6b0d4a08ddf5b160fa9267844"></a>
<a id="agroup__bt__mesh__cfg_html_ga74b79bc6a15c35ef399e7d5f7c4d26e6"></a>
<a id="agroup__bt__mesh__cfg_html_ga8457f222211bc812106b2dccc87b1abe"></a>
<a id="agroup__bt__mesh__cfg_html_gaa652e4f1460f62252065ac21854ab3f6"></a>
<a id="agroup__bt__mesh__cfg_html_gaa97f63f5b3167c672fa1a0d8c8fe9ab7"></a>
<a id="agroup__bt__mesh__cfg_html_gaac543b57580f9ac8dff36c0ce1196144"></a>
<a id="agroup__bt__mesh__cfg_html_gaafea57625c9fdba535431cc92dadd162"></a>
<a id="agroup__bt__mesh__cfg_html_gac7b1f1208659c80956e6dab6ac0ebc47"></a>
<a id="agroup__bt__mesh__cfg_html_gad8d6773753b80540b2aaa982c1ec8c03"></a>
<a id="agroup__bt__mesh__cfg_html_gadb41d2f78a490aa81b5640bb7ff5a5ce"></a>
<a id="agroup__bt__mesh__cfg_html_gaf9abf4bcba55d273a7e6e8ee42c521a9"></a>
<a id="agroup__bt__mesh__cfg_html_gafe3d54c1546b03cebbecaf762ae87781"></a>
<a id="agroup__bt__mesh__cfg_html_gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729"></a>
<a id="agroup__bt__mesh__cfg_html_gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0"></a>
<a id="agroup__bt__mesh__cfg_html_gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="aminmax_8h_html_affe776513b24d84b39af8ab0930fef7f"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>

```c


/*
 * Copyright (c) 2020 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_CFG_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_CFG_H_

#include <stdbool.h>
#include <stddef.h>

#include <sys/types.h>


#ifdef __cplusplus
extern "C" {
#endif

enum bt_mesh_feat_state {
        BT_MESH_FEATURE_DISABLED,
        BT_MESH_FEATURE_ENABLED,
        BT_MESH_FEATURE_NOT_SUPPORTED,
};

/* Key Refresh Phase */
#define BT_MESH_KR_NORMAL                   0x00
#define BT_MESH_KR_PHASE_1                  0x01
#define BT_MESH_KR_PHASE_2                  0x02
#define BT_MESH_KR_PHASE_3                  0x03

/* Legacy feature defines */
#define BT_MESH_RELAY_DISABLED              BT_MESH_FEATURE_DISABLED
#define BT_MESH_RELAY_ENABLED               BT_MESH_FEATURE_ENABLED
#define BT_MESH_RELAY_NOT_SUPPORTED         BT_MESH_FEATURE_NOT_SUPPORTED

#define BT_MESH_BEACON_DISABLED             BT_MESH_FEATURE_DISABLED
#define BT_MESH_BEACON_ENABLED              BT_MESH_FEATURE_ENABLED

#define BT_MESH_PRIV_BEACON_DISABLED        BT_MESH_FEATURE_DISABLED
#define BT_MESH_PRIV_BEACON_ENABLED         BT_MESH_FEATURE_ENABLED

#define BT_MESH_GATT_PROXY_DISABLED         BT_MESH_FEATURE_DISABLED
#define BT_MESH_GATT_PROXY_ENABLED          BT_MESH_FEATURE_ENABLED
#define BT_MESH_GATT_PROXY_NOT_SUPPORTED    BT_MESH_FEATURE_NOT_SUPPORTED

#define BT_MESH_PRIV_GATT_PROXY_DISABLED      BT_MESH_FEATURE_DISABLED
#define BT_MESH_PRIV_GATT_PROXY_ENABLED       BT_MESH_FEATURE_ENABLED
#define BT_MESH_PRIV_GATT_PROXY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED

#define BT_MESH_FRIEND_DISABLED             BT_MESH_FEATURE_DISABLED
#define BT_MESH_FRIEND_ENABLED              BT_MESH_FEATURE_ENABLED
#define BT_MESH_FRIEND_NOT_SUPPORTED        BT_MESH_FEATURE_NOT_SUPPORTED

#define BT_MESH_NODE_IDENTITY_STOPPED       BT_MESH_FEATURE_DISABLED
#define BT_MESH_NODE_IDENTITY_RUNNING       BT_MESH_FEATURE_ENABLED
#define BT_MESH_NODE_IDENTITY_NOT_SUPPORTED BT_MESH_FEATURE_NOT_SUPPORTED

void bt_mesh_beacon_set(bool beacon);

bool bt_mesh_beacon_enabled(void);

int bt_mesh_priv_beacon_set(enum bt_mesh_feat_state priv_beacon);

enum bt_mesh_feat_state bt_mesh_priv_beacon_get(void);

void bt_mesh_priv_beacon_update_interval_set(uint8_t interval);

uint8_t bt_mesh_priv_beacon_update_interval_get(void);

int bt_mesh_default_ttl_set(uint8_t default_ttl);

uint8_t bt_mesh_default_ttl_get(void);

int bt_mesh_od_priv_proxy_get(void);

int bt_mesh_od_priv_proxy_set(uint8_t on_demand_proxy);

void bt_mesh_net_transmit_set(uint8_t xmit);

uint8_t bt_mesh_net_transmit_get(void);

int bt_mesh_relay_set(enum bt_mesh_feat_state relay, uint8_t xmit);

enum bt_mesh_feat_state bt_mesh_relay_get(void);

uint8_t bt_mesh_relay_retransmit_get(void);

int bt_mesh_gatt_proxy_set(enum bt_mesh_feat_state gatt_proxy);

enum bt_mesh_feat_state bt_mesh_gatt_proxy_get(void);

int bt_mesh_priv_gatt_proxy_set(enum bt_mesh_feat_state priv_gatt_proxy);

enum bt_mesh_feat_state bt_mesh_priv_gatt_proxy_get(void);

int bt_mesh_friend_set(enum bt_mesh_feat_state friendship);

enum bt_mesh_feat_state bt_mesh_friend_get(void);


uint8_t bt_mesh_subnet_add(uint16_t net_idx, const uint8_t key[16]);

uint8_t bt_mesh_subnet_update(uint16_t net_idx, const uint8_t key[16]);

uint8_t bt_mesh_subnet_del(uint16_t net_idx);

bool bt_mesh_subnet_exists(uint16_t net_idx);

uint8_t bt_mesh_subnet_kr_phase_set(uint16_t net_idx, uint8_t *phase);

uint8_t bt_mesh_subnet_kr_phase_get(uint16_t net_idx, uint8_t *phase);

uint8_t bt_mesh_subnet_node_id_set(uint16_t net_idx,
                                   enum bt_mesh_feat_state node_id);

uint8_t bt_mesh_subnet_node_id_get(uint16_t net_idx,
                                   enum bt_mesh_feat_state *node_id);

uint8_t bt_mesh_subnet_priv_node_id_set(uint16_t net_idx,
                                        enum bt_mesh_feat_state priv_node_id);

uint8_t bt_mesh_subnet_priv_node_id_get(uint16_t net_idx,
                                        enum bt_mesh_feat_state *priv_node_id);

ssize_t bt_mesh_subnets_get(uint16_t net_idxs[], size_t max, off_t skip);



uint8_t bt_mesh_app_key_add(uint16_t app_idx, uint16_t net_idx,
                            const uint8_t key[16]);

uint8_t bt_mesh_app_key_update(uint16_t app_idx, uint16_t net_idx,
                               const uint8_t key[16]);

uint8_t bt_mesh_app_key_del(uint16_t app_idx, uint16_t net_idx);

bool bt_mesh_app_key_exists(uint16_t app_idx);

ssize_t bt_mesh_app_keys_get(uint16_t net_idx, uint16_t app_idxs[], size_t max,
                             off_t skip);


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_CFG_H_ */
```

## 11.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2020 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

密钥刷新阶段（Key Refresh Phase）。

### 注释 3：原第 45 行

旧版特性定义（Legacy feature defines）。

### 注释 4：原第 629 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_CFG_H_`。

## 11.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cfg_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)
- [BT_MESH_FEATURE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)
- [BT_MESH_FEATURE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)
- [BT_MESH_FEATURE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0)
- [bt_mesh_beacon_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga15de1cdc964628b6f001ef893021ce6e)
- [bt_mesh_beacon_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga479c14f6b0d4a08ddf5b160fa9267844)
- [bt_mesh_priv_beacon_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga1afc5ec210bbc6090ada922ddf75e284)
- [bt_mesh_priv_beacon_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga2c8dc9ee5c3862790efd2a74a1ef6873)
- [bt_mesh_priv_beacon_update_interval_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga01abb07d27edef40ffff4da968065c1d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_priv_beacon_update_interval_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gafe3d54c1546b03cebbecaf762ae87781)
- [bt_mesh_default_ttl_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaafea57625c9fdba535431cc92dadd162)
- [bt_mesh_default_ttl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaa97f63f5b3167c672fa1a0d8c8fe9ab7)
- [bt_mesh_od_priv_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga256d00139ca40eb99303fef766a3add7)
- [bt_mesh_od_priv_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga26023b727e1b180263b22d0ade145f81)
- [bt_mesh_net_transmit_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaa652e4f1460f62252065ac21854ab3f6)
- [bt_mesh_net_transmit_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga08b336fa1a4a721ac9b10fbb75e4af6b)
- [bt_mesh_relay_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gad8d6773753b80540b2aaa982c1ec8c03)
- [bt_mesh_relay_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gadb41d2f78a490aa81b5640bb7ff5a5ce)
- [bt_mesh_relay_retransmit_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaf9abf4bcba55d273a7e6e8ee42c521a9)
- [bt_mesh_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gaac543b57580f9ac8dff36c0ce1196144)
- [bt_mesh_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga8457f222211bc812106b2dccc87b1abe)
- [bt_mesh_priv_gatt_proxy_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga346244dcc70afe3a85e85c28c56b4f49)
- [bt_mesh_priv_gatt_proxy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga037375c99abb492d30378deca183071d)
- [bt_mesh_friend_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga74b79bc6a15c35ef399e7d5f7c4d26e6)
- [bt_mesh_friend_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gac7b1f1208659c80956e6dab6ac0ebc47)
- [bt_mesh_subnet_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga6a6ba6ac1dcbe5f6cfce9bbf38c1851f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_subnet_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga47236f48940303be27fa6af4797424c2)
- [bt_mesh_subnet_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gaec9d827d5f026b473f3ac88988d3c842)
- [bt_mesh_subnet_exists](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gad48780acaae085350a8b48d033717bfa)
- [bt_mesh_subnet_kr_phase_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gaef15af43e74e3c71590c63c5f1e3ea55)
- [bt_mesh_subnet_kr_phase_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#gad251907892150649f3f1ae6b4112cd84)
- [bt_mesh_subnet_node_id_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga59bf9f022665edc0ad03267e4bd16632)
- [bt_mesh_subnet_node_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga683d1f9abe82649a774b3d53dcaced8e)
- [bt_mesh_subnet_priv_node_id_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga5aa3e7f6b64e1b8b98f9737606d5d1ec)
- [bt_mesh_subnet_priv_node_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga555b4a7127869355fdf6040b8d14f999)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [bt_mesh_subnets_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html#ga0fd04bff5423a36b013089a4ba351d67)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [bt_mesh_app_key_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__app.html#ga0110ef750489af49a156a259c5a95c9b)
- [bt_mesh_app_key_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__app.html#ga5ae73ef766f0e1c38c0414c0a34e4053)
- [bt_mesh_app_key_del](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__app.html#gaa0e80a19c14d47808fc11459bf5ea2eb)
- [bt_mesh_app_key_exists](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__app.html#ga42c46a936e589460225a1fa69598a1ac)
- [bt_mesh_app_keys_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__app.html#gad7a949a0a814f6c9a26816c076d8b92a)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)

---

[上一章](P010_ccp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P012_ch32h41x-pinctrl.h_源码浏览.md)
