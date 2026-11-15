---
id: learning.zephyr-docs.api-source-reference.page-920
title: wifi_utils.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi__utils_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第920章\_wifi\_utils.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/wifi__utils_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/wifi__utils_8h.html)。

## 920.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00027"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00206"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="agroup__wifi__mgmt_html_ga1e2f0439a322355fa7368ea880c9c15d"></a>
<a id="agroup__wifi__mgmt_html_ga2606742e23f48da5ca1660aeac47888b"></a>
<a id="agroup__wifi__mgmt_html_ga428896bb7947b4fb46bf240b5179c7a3"></a>
<a id="agroup__wifi__mgmt_html_ga471a96d3fb6d610a591508b52d4c05a4"></a>
<a id="agroup__wifi__mgmt_html_ga4c91cd7dff0fd9e5402970f3222dc20d"></a>
<a id="agroup__wifi__mgmt_html_ga6fb496c072323dee6f09bfa44c42685f"></a>
<a id="agroup__wifi__mgmt_html_gaa9f346e3f44ad3441813a39bef559e2a"></a>
<a id="agroup__wifi__mgmt_html_gaba9f3117bcef9da1efc1841d3bd9adfd"></a>
<a id="agroup__wifi__mgmt_html_gae013eee6d6b74126c29d6ca7b2036310"></a>
<a id="agroup__wifi__mgmt_html_gaf1872d0ed2efd3737a36dcc0ab13f18e"></a>
<a id="agroup__wifi__mgmt_html_gaf408ba9f75354d3eca735b4804fdf199"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructwifi__band__channel_html"></a>
<a id="awifi_8h_html"></a>
<a id="awifi__mgmt_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_WIFI_UTILS_H_
#define ZEPHYR_INCLUDE_NET_WIFI_UTILS_H_

#include <zephyr/net/wifi.h>
#include <zephyr/net/wifi_mgmt.h>

#ifdef __cplusplus
extern "C" {
#endif



#define WIFI_UTILS_MAX_BAND_STR_LEN 3

#define WIFI_UTILS_MAX_CHAN_STR_LEN 4

int wifi_utils_parse_scan_bands(char *scan_bands_str, uint8_t *band_map);


int wifi_utils_parse_scan_ssids(char *scan_ssids_str,
                                const char *ssids[],
                                uint8_t num_ssids);


int wifi_utils_parse_scan_chan(char *scan_chan_str,
                               struct wifi_band_channel *chan,
                               uint8_t max_channels);


bool wifi_utils_validate_chan(uint8_t band,
                              uint16_t chan);

bool wifi_utils_validate_chan_2g(uint16_t chan);

bool wifi_utils_validate_chan_5g(uint16_t chan);

bool wifi_utils_validate_chan_6g(uint16_t chan);

enum wifi_frequency_bands wifi_utils_chan_to_band(uint16_t chan);

uint16_t wifi_utils_chan_to_freq(enum wifi_frequency_bands band, uint16_t chan);

uint16_t wifi_utils_freq_to_chan(uint16_t freq);



#ifdef __cplusplus
}
#endif
#endif /* ZEPHYR_INCLUDE_NET_WIFI_UTILS_H_ */
```

## 920.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 214 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_WIFI_UTILS_H_`。

## 920.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/wifi__utils_8h.html)
- [zephyr/net/wifi.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html)
- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h.html)
- [wifi_utils_parse_scan_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4c91cd7dff0fd9e5402970f3222dc20d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [wifi_utils_parse_scan_ssids](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga471a96d3fb6d610a591508b52d4c05a4)
- [wifi_utils_parse_scan_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaba9f3117bcef9da1efc1841d3bd9adfd)
- [wifi_band_channel](../network_core_model_reference/P161_wifi_band_channel_结构体.md)
- [wifi_utils_validate_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf1872d0ed2efd3737a36dcc0ab13f18e)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [wifi_utils_validate_chan_2g](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf408ba9f75354d3eca735b4804fdf199)
- [wifi_utils_validate_chan_5g](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae013eee6d6b74126c29d6ca7b2036310)
- [wifi_utils_validate_chan_6g](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2606742e23f48da5ca1660aeac47888b)
- [wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)
- [wifi_utils_chan_to_band](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6fb496c072323dee6f09bfa44c42685f)
- [wifi_utils_chan_to_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga428896bb7947b4fb46bf240b5179c7a3)
- [wifi_utils_freq_to_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa9f346e3f44ad3441813a39bef559e2a)
- [wifi.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html)
- [wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h.html)

---

[上一章](P919_wifi_nm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P921_wireguard.h_源码浏览.md)
