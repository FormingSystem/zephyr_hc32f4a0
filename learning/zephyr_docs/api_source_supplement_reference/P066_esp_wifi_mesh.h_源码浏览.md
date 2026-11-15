---
id: learning.zephyr-docs.api-source-supplement-reference.page-66
title: esp_wifi_mesh.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp__wifi__mesh_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_esp\_wifi\_mesh.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp__wifi__mesh_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp__wifi__mesh_8h.html)。

## 66.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00036"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00118"></a>
<a id="l00122"></a>
<a id="l00127"></a>
<a id="l00132"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00143"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="foldopen00254"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="foldopen00275"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="agroup__esp__wifi__mesh_html_ga1839da0700018e749326a870f1de972c"></a>
<a id="agroup__esp__wifi__mesh_html_ga1ac5c3150d24d5f259849ff0193c2523"></a>
<a id="agroup__esp__wifi__mesh_html_ga1b47943d3a51c9a3242d611010471412"></a>
<a id="agroup__esp__wifi__mesh_html_ga274783492b9e005ddfe5c2f6d7b85172"></a>
<a id="agroup__esp__wifi__mesh_html_ga2fbe0fb60b71abd4c070f26a1c7fb837"></a>
<a id="agroup__esp__wifi__mesh_html_ga3ad7865a96ed96c1a48c9f24e74eadd2"></a>
<a id="agroup__esp__wifi__mesh_html_ga56d92972f648a8d741dcc596b5c99919"></a>
<a id="agroup__esp__wifi__mesh_html_ga62b577f30a0fc68e9967284dafb99cf3"></a>
<a id="agroup__esp__wifi__mesh_html_ga64a1e694c72b317434559e8f066d971b"></a>
<a id="agroup__esp__wifi__mesh_html_ga6535544200d1ff000436b5006cbd2724"></a>
<a id="agroup__esp__wifi__mesh_html_ga68e0258134c3452bdd4c68f26d8a82fa"></a>
<a id="agroup__esp__wifi__mesh_html_ga75d2c1ccdc4dc058762f1be00517cd22"></a>
<a id="agroup__esp__wifi__mesh_html_ga7770e2363bf12c941c47ba5e6d69f105"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523a051120f6c8e06e8d8af9ced2b1853d3d"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523a0aecb5ac826e1bbb299277a866560007"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523a4effc55eec1beaae8b9bed0bf6124ce2"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523a63d20c75924c35d145c3f6ed76bd2b39"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523a746c61eaa6a07b1a308e64a3694cb9d3"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523a81544b2e377b5e0119f0c32fe6850a05"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523a818b192870dc294f3c3e7f9d1ab77942"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523ab830022e61381c7f390dd971b91902f8"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523ab99699382f6712fa0e7a79ccd5cb39a1"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523ad22734779b418a2e0dfcf0afae54e716"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523af436f81bddf53ae53129fabebfcc4c32"></a>
<a id="agroup__esp__wifi__mesh_html_gga1ac5c3150d24d5f259849ff0193c2523affe5cded5aa5db5d8233dc8ce8f57bb8"></a>
<a id="agroup__wifi__mgmt_html_gadde31a04fa25ed805115c6b31854cd9c"></a>
<a id="aminmax_8h_html_affe776513b24d84b39af8ab0930fef7f"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructesp__wifi__mesh__addr_html"></a>
<a id="astructesp__wifi__mesh__addr_html_abc17d248b689dd7c2ee2b0ce953fa8ff"></a>
<a id="astructesp__wifi__mesh__config_html"></a>
<a id="astructesp__wifi__mesh__config_html_a25c487b261eda67fb0ade6ef4f6a3319"></a>
<a id="astructesp__wifi__mesh__config_html_a3f479fa2a96bd0141a26b307b21d5299"></a>
<a id="astructesp__wifi__mesh__config_html_a578c704181d4560d6851bba8839b3b42"></a>
<a id="astructesp__wifi__mesh__config_html_a7271c57c8730a069771738d181508724"></a>
<a id="astructesp__wifi__mesh__config_html_a72ef51dca5f383486898cafbbefa4d88"></a>
<a id="astructesp__wifi__mesh__config_html_a794408d0ed1382cc9104e9a19d99560d"></a>
<a id="astructesp__wifi__mesh__config_html_a820b4a655de29d7056c4ce15dbfa184d"></a>
<a id="astructesp__wifi__mesh__config_html_a996b2ac59cff92df84e1a394549bf565"></a>
<a id="astructesp__wifi__mesh__event__info_html"></a>
<a id="astructesp__wifi__mesh__event__info_html_a69fa2fd2f6c244b1c730ecb880165728"></a>
<a id="astructesp__wifi__mesh__event__info_html_a90676505f5e1d0df03bf245cbb16f2c0"></a>
<a id="astructesp__wifi__mesh__event__info_html_af1702d5f2359103b31cc8d8ff7346f6e"></a>
<a id="astructesp__wifi__mesh__event__info_html_af5a036d50b7f2a8b878fdc262a91acd0"></a>
<a id="astructesp__wifi__mesh__status_html"></a>
<a id="astructesp__wifi__mesh__status_html_a3c7f1798e50aab22882586a0b388b135"></a>
<a id="astructesp__wifi__mesh__status_html_a9e7451c7e2ad2780279db9db50f319f1"></a>
<a id="astructesp__wifi__mesh__status_html_ab4962e3da36ca5f7a883a16994058d5a"></a>
<a id="astructesp__wifi__mesh__status_html_ad796be56b81338faa45d47fd60e0cac5"></a>
<a id="astructnet__if_html"></a>
<a id="awifi_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_ESP_WIFI_MESH_H_
#define ZEPHYR_INCLUDE_DRIVERS_ESP_WIFI_MESH_H_

#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/wifi.h>


enum esp_wifi_mesh_event {
        ESP_WIFI_MESH_EVENT_STARTED,
        ESP_WIFI_MESH_EVENT_STOPPED,
        ESP_WIFI_MESH_EVENT_PARENT_CONNECTED,
        ESP_WIFI_MESH_EVENT_PARENT_DISCONNECTED,
        ESP_WIFI_MESH_EVENT_CHILD_CONNECTED,
        ESP_WIFI_MESH_EVENT_CHILD_DISCONNECTED,
        ESP_WIFI_MESH_EVENT_NO_PARENT_FOUND,
        ESP_WIFI_MESH_EVENT_FIND_NETWORK,
        ESP_WIFI_MESH_EVENT_ROUTING_TABLE_CHANGE,
        ESP_WIFI_MESH_EVENT_LAYER_CHANGE,
        ESP_WIFI_MESH_EVENT_TODS_REACHABLE,
        ESP_WIFI_MESH_EVENT_TODS_UNREACHABLE,
};

struct esp_wifi_mesh_event_info {
        int layer;
        bool is_root;
        int routing_table_size;
        int reason;
};

typedef void (*esp_wifi_mesh_event_cb_t)(enum esp_wifi_mesh_event event,
                                         const struct esp_wifi_mesh_event_info *info);

void esp_wifi_mesh_event_cb_register(esp_wifi_mesh_event_cb_t cb);

struct esp_wifi_mesh_config {
        char ssid[33];
        char password[64];
        char mesh_password[64];
        uint8_t channel;
        uint8_t mesh_id[6];
        enum wifi_security_type authmode;
        uint8_t num_layers;
        uint8_t max_connections;
};

int esp_wifi_mesh_set_config(const struct esp_wifi_mesh_config *config);

void esp_wifi_mesh_get_config(struct esp_wifi_mesh_config *config);

int esp_wifi_mesh_start(void);

#if !defined(CONFIG_WIFI_ESP32_MESH_IP)
int esp_wifi_mesh_send(const uint8_t *data, size_t len);

int esp_wifi_mesh_recv(uint8_t *data, size_t *len, int timeout_ms);
#endif /* !CONFIG_WIFI_ESP32_MESH_IP */

struct esp_wifi_mesh_status {
        int layer;
        bool is_root;
        int routing_table_size;
        bool tods_reachable;
};

void esp_wifi_mesh_get_status(struct esp_wifi_mesh_status *status);

struct esp_wifi_mesh_addr {
        uint8_t addr[6];
};

int esp_wifi_mesh_get_routing_table(struct esp_wifi_mesh_addr *macs, size_t max, size_t *count);

void esp_wifi_mesh_set_tods_reachable(bool reachable);

void esp_wifi_mesh_bind_sta_rx(void);

struct net_if *esp_wifi_mesh_netif_get(void);


#endif /* ZEPHYR_INCLUDE_DRIVERS_ESP_WIFI_MESH_H_ */
```

## 66.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 249 行

条件编译表达式：`!CONFIG_WIFI_ESP32_MESH_IP`。

### 注释 3：原第 329 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_ESP_WIFI_MESH_H_`。

## 66.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp__wifi__mesh_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/wifi.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html)
- [esp_wifi_mesh_event](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga1ac5c3150d24d5f259849ff0193c2523)
- [ESP_WIFI_MESH_EVENT_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a4effc55eec1beaae8b9bed0bf6124ce2)
- [ESP_WIFI_MESH_EVENT_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a746c61eaa6a07b1a308e64a3694cb9d3)
- [ESP_WIFI_MESH_EVENT_PARENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a63d20c75924c35d145c3f6ed76bd2b39)
- [ESP_WIFI_MESH_EVENT_PARENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523af436f81bddf53ae53129fabebfcc4c32)
- [ESP_WIFI_MESH_EVENT_CHILD_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a051120f6c8e06e8d8af9ced2b1853d3d)
- [ESP_WIFI_MESH_EVENT_CHILD_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523ad22734779b418a2e0dfcf0afae54e716)
- [ESP_WIFI_MESH_EVENT_NO_PARENT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a81544b2e377b5e0119f0c32fe6850a05)
- [ESP_WIFI_MESH_EVENT_FIND_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a0aecb5ac826e1bbb299277a866560007)
- [ESP_WIFI_MESH_EVENT_ROUTING_TABLE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a818b192870dc294f3c3e7f9d1ab77942)
- [ESP_WIFI_MESH_EVENT_LAYER_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523affe5cded5aa5db5d8233dc8ce8f57bb8)
- [ESP_WIFI_MESH_EVENT_TODS_REACHABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523ab99699382f6712fa0e7a79ccd5cb39a1)
- [ESP_WIFI_MESH_EVENT_TODS_UNREACHABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523ab830022e61381c7f390dd971b91902f8)
- [esp_wifi_mesh_event_info](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md)
- [layer](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md#a90676505f5e1d0df03bf245cbb16f2c0)
- [is_root](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md#a69fa2fd2f6c244b1c730ecb880165728)
- [routing_table_size](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md#af1702d5f2359103b31cc8d8ff7346f6e)
- [reason](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md#af5a036d50b7f2a8b878fdc262a91acd0)
- [esp_wifi_mesh_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga3ad7865a96ed96c1a48c9f24e74eadd2)
- [esp_wifi_mesh_event_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga6535544200d1ff000436b5006cbd2724)
- [esp_wifi_mesh_config](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md)
- [ssid](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a72ef51dca5f383486898cafbbefa4d88)
- [password](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a25c487b261eda67fb0ade6ef4f6a3319)
- [mesh_password](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a7271c57c8730a069771738d181508724)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [channel](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a578c704181d4560d6851bba8839b3b42)
- [mesh_id](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a3f479fa2a96bd0141a26b307b21d5299)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [authmode](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a794408d0ed1382cc9104e9a19d99560d)
- [num_layers](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a820b4a655de29d7056c4ce15dbfa184d)
- [max_connections](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a996b2ac59cff92df84e1a394549bf565)
- [esp_wifi_mesh_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga7770e2363bf12c941c47ba5e6d69f105)
- [esp_wifi_mesh_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga75d2c1ccdc4dc058762f1be00517cd22)
- [esp_wifi_mesh_start](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga1839da0700018e749326a870f1de972c)
- [esp_wifi_mesh_send](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga68e0258134c3452bdd4c68f26d8a82fa)
- [esp_wifi_mesh_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga1b47943d3a51c9a3242d611010471412)
- [esp_wifi_mesh_status](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md)
- [layer](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md#ad796be56b81338faa45d47fd60e0cac5)
- [is_root](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md#a3c7f1798e50aab22882586a0b388b135)
- [routing_table_size](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md#a9e7451c7e2ad2780279db9db50f319f1)
- [tods_reachable](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md#ab4962e3da36ca5f7a883a16994058d5a)
- [esp_wifi_mesh_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga56d92972f648a8d741dcc596b5c99919)
- [esp_wifi_mesh_addr](../modem_wireless_model_reference/P012_esp_wifi_mesh_addr_结构体.md)
- [addr](../modem_wireless_model_reference/P012_esp_wifi_mesh_addr_结构体.md#abc17d248b689dd7c2ee2b0ce953fa8ff)
- [esp_wifi_mesh_get_routing_table](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga62b577f30a0fc68e9967284dafb99cf3)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [esp_wifi_mesh_set_tods_reachable](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga274783492b9e005ddfe5c2f6d7b85172)
- [esp_wifi_mesh_bind_sta_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga2fbe0fb60b71abd4c070f26a1c7fb837)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [esp_wifi_mesh_netif_get](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga64a1e694c72b317434559e8f066d971b)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [esp_wifi_mesh_addr::addr](../modem_wireless_model_reference/P012_esp_wifi_mesh_addr_结构体.md#abc17d248b689dd7c2ee2b0ce953fa8ff)
- [esp_wifi_mesh_config::password](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a25c487b261eda67fb0ade6ef4f6a3319)
- [esp_wifi_mesh_config::mesh_id](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a3f479fa2a96bd0141a26b307b21d5299)
- [esp_wifi_mesh_config::channel](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a578c704181d4560d6851bba8839b3b42)
- [esp_wifi_mesh_config::mesh_password](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a7271c57c8730a069771738d181508724)
- [esp_wifi_mesh_config::ssid](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a72ef51dca5f383486898cafbbefa4d88)
- [esp_wifi_mesh_config::authmode](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a794408d0ed1382cc9104e9a19d99560d)
- [esp_wifi_mesh_config::num_layers](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a820b4a655de29d7056c4ce15dbfa184d)
- [esp_wifi_mesh_config::max_connections](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md#a996b2ac59cff92df84e1a394549bf565)
- [esp_wifi_mesh_event_info::is_root](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md#a69fa2fd2f6c244b1c730ecb880165728)
- [esp_wifi_mesh_event_info::layer](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md#a90676505f5e1d0df03bf245cbb16f2c0)
- [esp_wifi_mesh_event_info::routing_table_size](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md#af1702d5f2359103b31cc8d8ff7346f6e)
- [esp_wifi_mesh_event_info::reason](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md#af5a036d50b7f2a8b878fdc262a91acd0)
- [esp_wifi_mesh_status::is_root](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md#a3c7f1798e50aab22882586a0b388b135)
- [esp_wifi_mesh_status::routing_table_size](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md#a9e7451c7e2ad2780279db9db50f319f1)
- [esp_wifi_mesh_status::tods_reachable](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md#ab4962e3da36ca5f7a883a16994058d5a)
- [esp_wifi_mesh_status::layer](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md#ad796be56b81338faa45d47fd60e0cac5)
- [wifi.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html)

---

[上一章](P065_esp32s3-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P067_events.h_源码浏览.md)
