---
id: learning.zephyr-docs.api-source-reference.page-817
title: statistic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/statistic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第817章\_statistic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/statistic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/statistic_8h.html)。

## 817.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="agroup__bt__mesh__stat_html_ga240344c421ff810578b9d0e06a11fe56"></a>
<a id="agroup__bt__mesh__stat_html_ga8c1e9de2f323111ee95d0903b5ecb2fd"></a>
<a id="agroup__bt__mesh__stat_html_gabe8c893466f24e9b75fe51ae5ea65132"></a>
<a id="agroup__bt__mesh__stat_html_gaf4ca44edb393329569052707aa9a8f18"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructbt__mesh__lpn__timing_html"></a>
<a id="astructbt__mesh__lpn__timing_html_a2c9f8faef395768c1b6e69fcc45c01bf"></a>
<a id="astructbt__mesh__lpn__timing_html_a3d2f6b4b247fadceef5412be13288d9b"></a>
<a id="astructbt__mesh__lpn__timing_html_a414f154e693065c7c40df6bfeb533eab"></a>
<a id="astructbt__mesh__lpn__timing_html_a47584e8ba286e85a5a333946abf6b18c"></a>
<a id="astructbt__mesh__lpn__timing_html_a7908bb6fa9f12aa437e397f8c1b4ecaf"></a>
<a id="astructbt__mesh__lpn__timing_html_a94adbcabda24c6ee0f6fa71bedd23ce0"></a>
<a id="astructbt__mesh__lpn__timing_html_aa2c0aac2b1be70b6bb0b9311213a2482"></a>
<a id="astructbt__mesh__lpn__timing_html_abb4bb74a205cb33573d0fbb078701b62"></a>
<a id="astructbt__mesh__lpn__timing_html_ac115c2cf035c722f8b6f969f700c1f81"></a>
<a id="astructbt__mesh__statistic_html"></a>
<a id="astructbt__mesh__statistic_html_a0f60214d1f2480bc0025415064dd79e8"></a>
<a id="astructbt__mesh__statistic_html_a139484340d2bd3fae763b23e91648e0e"></a>
<a id="astructbt__mesh__statistic_html_a1979c5798d7d015bf4cf0c30716d3e4f"></a>
<a id="astructbt__mesh__statistic_html_a2c47d080eac1050422d36402a9771fa6"></a>
<a id="astructbt__mesh__statistic_html_a448c73e05fd8055baaa64532275d9c69"></a>
<a id="astructbt__mesh__statistic_html_a5c8d77c2d32964f0a54420aafff9a4e1"></a>
<a id="astructbt__mesh__statistic_html_a9da26f6d5ad7b91b69b95e4d4a70bf71"></a>
<a id="astructbt__mesh__statistic_html_aa4d83bb57f86723899bc2fe25342423d"></a>
<a id="astructbt__mesh__statistic_html_aa86617d0c3cfa7e2ed7e10e4c3ac8b5c"></a>
<a id="astructbt__mesh__statistic_html_af7c764c6b702957180d8b74193207a0e"></a>

```c


/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_STATISTIC_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_STATISTIC_H_

#include <stdint.h>


#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_statistic {
        uint32_t rx_adv;
        uint32_t rx_loopback;
        uint32_t rx_proxy;
        uint32_t rx_uknown;
        uint32_t tx_adv_relay_planned;
        uint32_t tx_adv_relay_succeeded;
        uint32_t tx_local_planned;
        uint32_t tx_local_succeeded;
        uint32_t tx_friend_planned;
        uint32_t tx_friend_succeeded;
};

void bt_mesh_stat_get(struct bt_mesh_statistic *st);

void bt_mesh_stat_reset(void);

struct bt_mesh_lpn_timing {
        uint32_t recv_delay_us;
        uint32_t recv_delay_min_us;
        uint32_t recv_delay_max_us;
        uint32_t recv_win_us;
        uint32_t recv_win_min_us;
        uint32_t recv_win_max_us;
        uint32_t recv_win_expected_us;
        uint32_t cnt;
        uint32_t cnt_failed;
};

int bt_mesh_stat_lpn_timing_get(struct bt_mesh_lpn_timing *timing);

void bt_mesh_stat_lpn_timing_reset(void);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_STATISTIC_H_ */
```

## 817.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 126 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_STATISTIC_H_`。

## 817.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/statistic_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [bt_mesh_statistic](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [rx_adv](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a5c8d77c2d32964f0a54420aafff9a4e1)
- [rx_loopback](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a448c73e05fd8055baaa64532275d9c69)
- [rx_proxy](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#aa86617d0c3cfa7e2ed7e10e4c3ac8b5c)
- [rx_uknown](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#af7c764c6b702957180d8b74193207a0e)
- [tx_adv_relay_planned](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a1979c5798d7d015bf4cf0c30716d3e4f)
- [tx_adv_relay_succeeded](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a139484340d2bd3fae763b23e91648e0e)
- [tx_local_planned](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a2c47d080eac1050422d36402a9771fa6)
- [tx_local_succeeded](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a9da26f6d5ad7b91b69b95e4d4a70bf71)
- [tx_friend_planned](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a0f60214d1f2480bc0025415064dd79e8)
- [tx_friend_succeeded](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#aa4d83bb57f86723899bc2fe25342423d)
- [bt_mesh_stat_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#ga8c1e9de2f323111ee95d0903b5ecb2fd)
- [bt_mesh_stat_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#gabe8c893466f24e9b75fe51ae5ea65132)
- [bt_mesh_lpn_timing](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md)
- [recv_delay_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a7908bb6fa9f12aa437e397f8c1b4ecaf)
- [recv_delay_min_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a47584e8ba286e85a5a333946abf6b18c)
- [recv_delay_max_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a2c9f8faef395768c1b6e69fcc45c01bf)
- [recv_win_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#ac115c2cf035c722f8b6f969f700c1f81)
- [recv_win_min_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a3d2f6b4b247fadceef5412be13288d9b)
- [recv_win_max_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#aa2c0aac2b1be70b6bb0b9311213a2482)
- [recv_win_expected_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a94adbcabda24c6ee0f6fa71bedd23ce0)
- [cnt](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#abb4bb74a205cb33573d0fbb078701b62)
- [cnt_failed](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a414f154e693065c7c40df6bfeb533eab)
- [bt_mesh_stat_lpn_timing_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#ga240344c421ff810578b9d0e06a11fe56)
- [bt_mesh_stat_lpn_timing_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#gaf4ca44edb393329569052707aa9a8f18)
- [bt_mesh_lpn_timing::recv_delay_max_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a2c9f8faef395768c1b6e69fcc45c01bf)
- [bt_mesh_lpn_timing::recv_win_min_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a3d2f6b4b247fadceef5412be13288d9b)
- [bt_mesh_lpn_timing::cnt_failed](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a414f154e693065c7c40df6bfeb533eab)
- [bt_mesh_lpn_timing::recv_delay_min_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a47584e8ba286e85a5a333946abf6b18c)
- [bt_mesh_lpn_timing::recv_delay_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a7908bb6fa9f12aa437e397f8c1b4ecaf)
- [bt_mesh_lpn_timing::recv_win_expected_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#a94adbcabda24c6ee0f6fa71bedd23ce0)
- [bt_mesh_lpn_timing::recv_win_max_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#aa2c0aac2b1be70b6bb0b9311213a2482)
- [bt_mesh_lpn_timing::cnt](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#abb4bb74a205cb33573d0fbb078701b62)
- [bt_mesh_lpn_timing::recv_win_us](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md#ac115c2cf035c722f8b6f969f700c1f81)
- [bt_mesh_statistic::tx_friend_planned](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a0f60214d1f2480bc0025415064dd79e8)
- [bt_mesh_statistic::tx_adv_relay_succeeded](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a139484340d2bd3fae763b23e91648e0e)
- [bt_mesh_statistic::tx_adv_relay_planned](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a1979c5798d7d015bf4cf0c30716d3e4f)
- [bt_mesh_statistic::tx_local_planned](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a2c47d080eac1050422d36402a9771fa6)
- [bt_mesh_statistic::rx_loopback](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a448c73e05fd8055baaa64532275d9c69)
- [bt_mesh_statistic::rx_adv](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a5c8d77c2d32964f0a54420aafff9a4e1)
- [bt_mesh_statistic::tx_local_succeeded](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#a9da26f6d5ad7b91b69b95e4d4a70bf71)
- [bt_mesh_statistic::tx_friend_succeeded](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#aa4d83bb57f86723899bc2fe25342423d)
- [bt_mesh_statistic::rx_proxy](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#aa86617d0c3cfa7e2ed7e10e4c3ac8b5c)
- [bt_mesh_statistic::rx_uknown](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md#af7c764c6b702957180d8b74193207a0e)

---

[上一章](P816_state.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P818_status.h_源码浏览.md)
