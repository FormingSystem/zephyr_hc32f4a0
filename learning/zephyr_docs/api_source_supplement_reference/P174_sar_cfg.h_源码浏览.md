---
id: learning.zephyr-docs.api-source-supplement-reference.page-174
title: sar_cfg.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第174章\_sar\_cfg.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg_8h.html)。

## 174.1\_原始可见代码（Source Code）

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
<a id="l00027"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__mesh__sar__rx_html"></a>
<a id="astructbt__mesh__sar__rx_html_a32a790589ddebee397d536b18518558d"></a>
<a id="astructbt__mesh__sar__rx_html_a5517a0f2167340cf59ef6fc72077f010"></a>
<a id="astructbt__mesh__sar__rx_html_a70615d8df27b6f8291291b73abc57c9c"></a>
<a id="astructbt__mesh__sar__rx_html_aac228432bddf7f112ccbcb9e3d05d2ce"></a>
<a id="astructbt__mesh__sar__rx_html_ad277cc6c5d221aab7fd22581bfccd83c"></a>
<a id="astructbt__mesh__sar__tx_html"></a>
<a id="astructbt__mesh__sar__tx_html_a1893bbeb473ebcf99db633e7f979b376"></a>
<a id="astructbt__mesh__sar__tx_html_a40a96d401f44345397bd605d6f25e04a"></a>
<a id="astructbt__mesh__sar__tx_html_a686a6a4a7e6a7c6a532ddb8c8bad76df"></a>
<a id="astructbt__mesh__sar__tx_html_a6fec529b66c04f0828f5d5d716fd9281"></a>
<a id="astructbt__mesh__sar__tx_html_a8e0ad5b5977bd4aad20bd79977a0342d"></a>
<a id="astructbt__mesh__sar__tx_html_aa491eda390c1b9532e968ed566ec23c2"></a>
<a id="astructbt__mesh__sar__tx_html_adaa856b561ac24c07706a04eea157183"></a>

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_SAR_CFG_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_SAR_CFG_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif


struct bt_mesh_sar_tx {
        uint8_t seg_int_step;

        uint8_t unicast_retrans_count;

        uint8_t unicast_retrans_without_prog_count;

        /* SAR Unicast Retransmissions Interval Step state */
        uint8_t unicast_retrans_int_step;

        uint8_t unicast_retrans_int_inc;

        uint8_t multicast_retrans_count;

        uint8_t multicast_retrans_int;
};

struct bt_mesh_sar_rx {
        uint8_t seg_thresh;

        uint8_t ack_delay_inc;

        uint8_t discard_timeout;

        uint8_t rx_seg_int_step;

        uint8_t ack_retrans_count;
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_SAR_CFG_H_ */
```

## 174.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

分段与重组（SAR）的单播重传间隔步长状态（Unicast Retransmissions Interval Step state）。

### 注释 3：原第 76 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_SAR_CFG_H_`。

## 174.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [bt_mesh_sar_tx](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [seg_int_step](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#aa491eda390c1b9532e968ed566ec23c2)
- [unicast_retrans_count](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#adaa856b561ac24c07706a04eea157183)
- [unicast_retrans_without_prog_count](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#a1893bbeb473ebcf99db633e7f979b376)
- [unicast_retrans_int_step](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#a8e0ad5b5977bd4aad20bd79977a0342d)
- [unicast_retrans_int_inc](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#a40a96d401f44345397bd605d6f25e04a)
- [multicast_retrans_count](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#a686a6a4a7e6a7c6a532ddb8c8bad76df)
- [multicast_retrans_int](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#a6fec529b66c04f0828f5d5d716fd9281)
- [bt_mesh_sar_rx](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md)
- [seg_thresh](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md#a32a790589ddebee397d536b18518558d)
- [ack_delay_inc](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md#a5517a0f2167340cf59ef6fc72077f010)
- [discard_timeout](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md#a70615d8df27b6f8291291b73abc57c9c)
- [rx_seg_int_step](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md#ad277cc6c5d221aab7fd22581bfccd83c)
- [ack_retrans_count](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md#aac228432bddf7f112ccbcb9e3d05d2ce)
- [bt_mesh_sar_rx::seg_thresh](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md#a32a790589ddebee397d536b18518558d)
- [bt_mesh_sar_rx::ack_delay_inc](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md#a5517a0f2167340cf59ef6fc72077f010)
- [bt_mesh_sar_rx::discard_timeout](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md#a70615d8df27b6f8291291b73abc57c9c)
- [bt_mesh_sar_rx::ack_retrans_count](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md#aac228432bddf7f112ccbcb9e3d05d2ce)
- [bt_mesh_sar_rx::rx_seg_int_step](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md#ad277cc6c5d221aab7fd22581bfccd83c)
- [bt_mesh_sar_tx::unicast_retrans_without_prog_count](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#a1893bbeb473ebcf99db633e7f979b376)
- [bt_mesh_sar_tx::unicast_retrans_int_inc](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#a40a96d401f44345397bd605d6f25e04a)
- [bt_mesh_sar_tx::multicast_retrans_count](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#a686a6a4a7e6a7c6a532ddb8c8bad76df)
- [bt_mesh_sar_tx::multicast_retrans_int](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#a6fec529b66c04f0828f5d5d716fd9281)
- [bt_mesh_sar_tx::unicast_retrans_int_step](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#a8e0ad5b5977bd4aad20bd79977a0342d)
- [bt_mesh_sar_tx::seg_int_step](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#aa491eda390c1b9532e968ed566ec23c2)
- [bt_mesh_sar_tx::unicast_retrans_count](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md#adaa856b561ac24c07706a04eea157183)

---

[上一章](P173_rx_mtu_pwm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P175_sar_cfg_cli.h_源码浏览.md)
