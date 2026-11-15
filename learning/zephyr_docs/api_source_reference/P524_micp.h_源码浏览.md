---
id: learning.zephyr-docs.api-source-reference.page-524
title: micp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/micp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第524章\_micp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/micp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/micp_8h.html)。

## 524.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="foldopen00178"></a>
<a id="l00178"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="aaics_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__micp_html_ga0541a36655024d9eadcff2d3e0c877f6"></a>
<a id="agroup__bt__micp_html_ga148ffcd0672adff9ccfaf35c522897c4"></a>
<a id="agroup__bt__micp_html_ga19ec08afa7784b80fce039fe84a4e33c"></a>
<a id="agroup__bt__micp_html_ga21e04942da32b15e75a0b0de3fb84167"></a>
<a id="agroup__bt__micp_html_ga26187007ebf35ba2a5c57a076a3a7212"></a>
<a id="agroup__bt__micp_html_ga263bf5cf51e4ef8d7e6986f0d8358da3"></a>
<a id="agroup__bt__micp_html_ga2d50f432703233c0f03cb139b6119faa"></a>
<a id="agroup__bt__micp_html_ga46cc0362c55cd9bdaf331de834a5fef5"></a>
<a id="agroup__bt__micp_html_ga47f971c9c259e43504d586a55cf22c4e"></a>
<a id="agroup__bt__micp_html_ga4b564e6b315a3861f1c3ba6098eabfe1"></a>
<a id="agroup__bt__micp_html_ga5148e78053a3052d27677a1fa24e3847"></a>
<a id="agroup__bt__micp_html_ga525c5d694f7d510d33f088e848733af6"></a>
<a id="agroup__bt__micp_html_ga5dee6c7a1115bffbea39ba0575f369fc"></a>
<a id="agroup__bt__micp_html_ga6248c90bb94cd138c5bf9c68cffda4fe"></a>
<a id="agroup__bt__micp_html_ga863030e1b836c01a1be964bce0c72025"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__aics__cb_html"></a>
<a id="astructbt__aics__register__param_html"></a>
<a id="astructbt__aics_html"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__micp__included_html"></a>
<a id="astructbt__micp__included_html_a2afddd15bd726039682151038b2415d1"></a>
<a id="astructbt__micp__included_html_a32cff1b68d96319958eeba66f249cd67"></a>
<a id="astructbt__micp__mic__ctlr__cb_html"></a>
<a id="astructbt__micp__mic__ctlr__cb_html_a03afd3a79838c15be9262f441a3d338b"></a>
<a id="astructbt__micp__mic__ctlr__cb_html_a21786359322dbd6f814929293a69482f"></a>
<a id="astructbt__micp__mic__ctlr__cb_html_a2359b88344bf36c3a491b0126dac006b"></a>
<a id="astructbt__micp__mic__ctlr__cb_html_a6bd92f744f203736ec04d17a632b16c1"></a>
<a id="astructbt__micp__mic__ctlr__cb_html_ae15fb539599feab59041e30a121021f0"></a>
<a id="astructbt__micp__mic__ctlr_html"></a>
<a id="astructbt__micp__mic__dev__cb_html"></a>
<a id="astructbt__micp__mic__dev__cb_html_ad674b130546ceabbb90e6004121ccd98"></a>
<a id="astructbt__micp__mic__dev__register__param_html"></a>
<a id="astructbt__micp__mic__dev__register__param_html_a8153e3e59f830a3746d3545b9262ae50"></a>
<a id="astructbt__micp__mic__dev__register__param_html_adbb6cf96e7f1d3e48b88cd3fbc5fd71a"></a>

```c


/*
 * Copyright (c) 2020-2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MICP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MICP_H_


#include <stdint.h>

#include <zephyr/bluetooth/audio/aics.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_BT_MICP_MIC_DEV)
#define BT_MICP_MIC_DEV_AICS_CNT CONFIG_BT_MICP_MIC_DEV_AICS_INSTANCE_COUNT
#else
#define BT_MICP_MIC_DEV_AICS_CNT 0U
#endif /* CONFIG_BT_MICP_MIC_DEV */

#define BT_MICP_ERR_MUTE_DISABLED                  0x80U

#define BT_MICP_MUTE_UNMUTED                       0x00U
#define BT_MICP_MUTE_MUTED                         0x01U
#define BT_MICP_MUTE_DISABLED                      0x02U

struct bt_micp_mic_ctlr;

struct bt_micp_mic_dev_register_param {
#if defined(CONFIG_BT_MICP_MIC_DEV_AICS) || defined(__DOXYGEN__)
        struct bt_aics_register_param aics_param[BT_MICP_MIC_DEV_AICS_CNT];
#endif /* CONFIG_BT_MICP_MIC_DEV_AICS */

        struct bt_micp_mic_dev_cb *cb;
};

struct bt_micp_included {
        uint8_t aics_cnt;
        struct bt_aics **aics;
};

int bt_micp_mic_dev_register(struct bt_micp_mic_dev_register_param *param);

int bt_micp_mic_dev_included_get(struct bt_micp_included *included);

struct bt_micp_mic_dev_cb {
        void (*mute)(uint8_t mute);
};

int bt_micp_mic_dev_unmute(void);

int bt_micp_mic_dev_mute(void);

int bt_micp_mic_dev_mute_disable(void);

int bt_micp_mic_dev_mute_get(void);

struct bt_micp_mic_ctlr_cb {
        void (*mute)(struct bt_micp_mic_ctlr *mic_ctlr, int err, uint8_t mute);

        void (*discover)(struct bt_micp_mic_ctlr *mic_ctlr, int err,
                         uint8_t aics_count);

        void (*mute_written)(struct bt_micp_mic_ctlr *mic_ctlr, int err);

        void (*unmute_written)(struct bt_micp_mic_ctlr *mic_ctlr, int err);

#if defined(CONFIG_BT_MICP_MIC_CTLR_AICS) || defined(__DOXYGEN__)
        struct bt_aics_cb               aics_cb;
#endif /* CONFIG_BT_MICP_MIC_CTLR_AICS */

        sys_snode_t _node;
};

int bt_micp_mic_ctlr_included_get(struct bt_micp_mic_ctlr *mic_ctlr,
                                  struct bt_micp_included *included);

int bt_micp_mic_ctlr_conn_get(const struct bt_micp_mic_ctlr *mic_ctlr,
                              struct bt_conn **conn);

struct bt_micp_mic_ctlr *bt_micp_mic_ctlr_get_by_conn(const struct bt_conn *conn);

int bt_micp_mic_ctlr_discover(struct bt_conn *conn,
                              struct bt_micp_mic_ctlr **mic_ctlr);

int bt_micp_mic_ctlr_unmute(struct bt_micp_mic_ctlr *mic_ctlr);

int bt_micp_mic_ctlr_mute(struct bt_micp_mic_ctlr *mic_ctlr);

int bt_micp_mic_ctlr_mute_get(struct bt_micp_mic_ctlr *mic_ctlr);

int bt_micp_mic_ctlr_cb_register(struct bt_micp_mic_ctlr_cb *cb);
#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MICP_H_ */
```

## 524.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2020-2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 45 行

条件编译配置（Configuration）标记：`CONFIG_BT_MICP_MIC_DEV`。

### 注释 3：原第 78 行

条件编译配置（Configuration）标记：`CONFIG_BT_MICP_MIC_DEV_AICS`。

### 注释 4：原第 223 行

条件编译配置（Configuration）标记：`CONFIG_BT_MICP_MIC_CTLR_AICS`。

### 注释 5：原第 336 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MICP_H_`。

## 524.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/micp_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/audio/aics.h](https://docs.zephyrproject.org/latest/doxygen/html/aics_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_micp_mic_ctlr](../bluetooth_service_model_reference/P121_bt_micp_mic_ctlr_结构体.md)
- [bt_micp_mic_dev_register_param](../bluetooth_service_model_reference/P124_bt_micp_mic_dev_register_param_结构体.md)
- [bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)
- [aics_param](../bluetooth_service_model_reference/P124_bt_micp_mic_dev_register_param_结构体.md#a8153e3e59f830a3746d3545b9262ae50)
- [BT_MICP_MIC_DEV_AICS_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga46cc0362c55cd9bdaf331de834a5fef5)
- [bt_micp_mic_dev_cb](../bluetooth_service_model_reference/P123_bt_micp_mic_dev_cb_结构体.md)
- [cb](../bluetooth_service_model_reference/P124_bt_micp_mic_dev_register_param_结构体.md#adbb6cf96e7f1d3e48b88cd3fbc5fd71a)
- [bt_micp_included](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [aics_cnt](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md#a32cff1b68d96319958eeba66f249cd67)
- [bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)
- [aics](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md#a2afddd15bd726039682151038b2415d1)
- [bt_micp_mic_dev_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga5dee6c7a1115bffbea39ba0575f369fc)
- [bt_micp_mic_dev_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga0541a36655024d9eadcff2d3e0c877f6)
- [mute](../bluetooth_service_model_reference/P123_bt_micp_mic_dev_cb_结构体.md#ad674b130546ceabbb90e6004121ccd98)
- [bt_micp_mic_dev_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga19ec08afa7784b80fce039fe84a4e33c)
- [bt_micp_mic_dev_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga47f971c9c259e43504d586a55cf22c4e)
- [bt_micp_mic_dev_mute_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga525c5d694f7d510d33f088e848733af6)
- [bt_micp_mic_dev_mute_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga263bf5cf51e4ef8d7e6986f0d8358da3)
- [bt_micp_mic_ctlr_cb](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md)
- [mute](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md#a21786359322dbd6f814929293a69482f)
- [discover](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md#a2359b88344bf36c3a491b0126dac006b)
- [mute_written](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md#ae15fb539599feab59041e30a121021f0)
- [unmute_written](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md#a03afd3a79838c15be9262f441a3d338b)
- [bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)
- [aics_cb](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md#a6bd92f744f203736ec04d17a632b16c1)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_micp_mic_ctlr_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga21e04942da32b15e75a0b0de3fb84167)
- [bt_micp_mic_ctlr_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga4b564e6b315a3861f1c3ba6098eabfe1)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_micp_mic_ctlr_get_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga863030e1b836c01a1be964bce0c72025)
- [bt_micp_mic_ctlr_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga26187007ebf35ba2a5c57a076a3a7212)
- [bt_micp_mic_ctlr_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga6248c90bb94cd138c5bf9c68cffda4fe)
- [bt_micp_mic_ctlr_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga2d50f432703233c0f03cb139b6119faa)
- [bt_micp_mic_ctlr_mute_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga5148e78053a3052d27677a1fa24e3847)
- [bt_micp_mic_ctlr_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga148ffcd0672adff9ccfaf35c522897c4)
- [aics.h](https://docs.zephyrproject.org/latest/doxygen/html/aics_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_micp_included::aics](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md#a2afddd15bd726039682151038b2415d1)
- [bt_micp_included::aics_cnt](../bluetooth_service_model_reference/P120_bt_micp_included_结构体.md#a32cff1b68d96319958eeba66f249cd67)
- [bt_micp_mic_ctlr_cb::unmute_written](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md#a03afd3a79838c15be9262f441a3d338b)
- [bt_micp_mic_ctlr_cb::mute](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md#a21786359322dbd6f814929293a69482f)
- [bt_micp_mic_ctlr_cb::discover](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md#a2359b88344bf36c3a491b0126dac006b)
- [bt_micp_mic_ctlr_cb::aics_cb](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md#a6bd92f744f203736ec04d17a632b16c1)
- [bt_micp_mic_ctlr_cb::mute_written](../bluetooth_service_model_reference/P122_bt_micp_mic_ctlr_cb_结构体.md#ae15fb539599feab59041e30a121021f0)
- [bt_micp_mic_dev_cb::mute](../bluetooth_service_model_reference/P123_bt_micp_mic_dev_cb_结构体.md#ad674b130546ceabbb90e6004121ccd98)
- [bt_micp_mic_dev_register_param::aics_param](../bluetooth_service_model_reference/P124_bt_micp_mic_dev_register_param_结构体.md#a8153e3e59f830a3746d3545b9262ae50)
- [bt_micp_mic_dev_register_param::cb](../bluetooth_service_model_reference/P124_bt_micp_mic_dev_register_param_结构体.md#adbb6cf96e7f1d3e48b88cd3fbc5fd71a)

---

[上一章](P523_mhz19b.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P525_microchip-port-g1-gpio.h_源码浏览.md)
