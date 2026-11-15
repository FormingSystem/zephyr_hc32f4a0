---
id: learning.zephyr-docs.api-source-supplement-reference.page-108
title: mcs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第108章\_mcs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mcs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mcs_8h.html)。

## 108.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00172"></a>
<a id="l00177"></a>
<a id="l00182"></a>
<a id="l00187"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00243"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00285"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00304"></a>
<a id="l00306"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00312"></a>
<a id="l00314"></a>
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00351"></a>
<a id="l00353"></a>
<a id="l00355"></a>
<a id="l00363"></a>
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="asys_2util_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c

/*
 * Copyright (c) 2019 - 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MCS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MCS_H_


#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_MCS_ERR_LONG_VAL_CHANGED     0x80U

#define BT_MCS_PLAYBACK_SPEED_MIN     -128
#define BT_MCS_PLAYBACK_SPEED_QUARTER -128
#define BT_MCS_PLAYBACK_SPEED_HALF     -64
#define BT_MCS_PLAYBACK_SPEED_UNITY      0
#define BT_MCS_PLAYBACK_SPEED_DOUBLE    64
#define BT_MCS_PLAYBACK_SPEED_MAX      127

#define BT_MCS_SEEKING_SPEED_FACTOR_MAX  64
#define BT_MCS_SEEKING_SPEED_FACTOR_MIN   4
#define BT_MCS_SEEKING_SPEED_FACTOR_ZERO  0

#define BT_MCS_PLAYING_ORDER_SINGLE_ONCE    0x01U
#define BT_MCS_PLAYING_ORDER_SINGLE_REPEAT  0x02U
#define BT_MCS_PLAYING_ORDER_INORDER_ONCE   0x03U
#define BT_MCS_PLAYING_ORDER_INORDER_REPEAT 0x04U
#define BT_MCS_PLAYING_ORDER_OLDEST_ONCE    0x05U
#define BT_MCS_PLAYING_ORDER_OLDEST_REPEAT  0x06U
#define BT_MCS_PLAYING_ORDER_NEWEST_ONCE    0x07U
#define BT_MCS_PLAYING_ORDER_NEWEST_REPEAT  0x08U
#define BT_MCS_PLAYING_ORDER_SHUFFLE_ONCE   0x09U
#define BT_MCS_PLAYING_ORDER_SHUFFLE_REPEAT 0x0AU

#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_ONCE    BIT(0U)
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SINGLE_REPEAT  BIT(1U)
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_ONCE   BIT(2U)
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_INORDER_REPEAT BIT(3U)
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_ONCE    BIT(4U)
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_OLDEST_REPEAT  BIT(5U)
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_ONCE    BIT(6U)
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_NEWEST_REPEAT  BIT(7U)
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_ONCE   BIT(8U)
#define BT_MCS_PLAYING_ORDERS_SUPPORTED_SHUFFLE_REPEAT BIT(9U)

#define BT_MCS_MEDIA_STATE_INACTIVE 0x00U
#define BT_MCS_MEDIA_STATE_PLAYING  0x01U
#define BT_MCS_MEDIA_STATE_PAUSED   0x02U
#define BT_MCS_MEDIA_STATE_SEEKING  0x03U

#define BT_MCS_OPC_PLAY          0x01U
#define BT_MCS_OPC_PAUSE         0x02U
#define BT_MCS_OPC_FAST_REWIND   0x03U
#define BT_MCS_OPC_FAST_FORWARD  0x04U
#define BT_MCS_OPC_STOP          0x05U

#define BT_MCS_OPC_MOVE_RELATIVE 0x10U

#define BT_MCS_OPC_PREV_SEGMENT  0x20U
#define BT_MCS_OPC_NEXT_SEGMENT  0x21U
#define BT_MCS_OPC_FIRST_SEGMENT 0x22U
#define BT_MCS_OPC_LAST_SEGMENT  0x23U
#define BT_MCS_OPC_GOTO_SEGMENT  0x24U

#define BT_MCS_OPC_PREV_TRACK    0x30U
#define BT_MCS_OPC_NEXT_TRACK    0x31U
#define BT_MCS_OPC_FIRST_TRACK   0x32U
#define BT_MCS_OPC_LAST_TRACK    0x33U
#define BT_MCS_OPC_GOTO_TRACK    0x34U

#define BT_MCS_OPC_PREV_GROUP    0x40U
#define BT_MCS_OPC_NEXT_GROUP    0x41U
#define BT_MCS_OPC_FIRST_GROUP   0x42U
#define BT_MCS_OPC_LAST_GROUP    0x43U
#define BT_MCS_OPC_GOTO_GROUP    0x44U

#define BT_MCS_OPCODES_SUPPORTED_LEN 4U

#define BT_MCS_OPC_SUP_PLAY          BIT(0U)
#define BT_MCS_OPC_SUP_PAUSE         BIT(1U)
#define BT_MCS_OPC_SUP_FAST_REWIND   BIT(2U)
#define BT_MCS_OPC_SUP_FAST_FORWARD  BIT(3U)
#define BT_MCS_OPC_SUP_STOP          BIT(4U)

#define BT_MCS_OPC_SUP_MOVE_RELATIVE BIT(5U)

#define BT_MCS_OPC_SUP_PREV_SEGMENT  BIT(6U)
#define BT_MCS_OPC_SUP_NEXT_SEGMENT  BIT(7U)
#define BT_MCS_OPC_SUP_FIRST_SEGMENT BIT(8U)
#define BT_MCS_OPC_SUP_LAST_SEGMENT  BIT(9U)
#define BT_MCS_OPC_SUP_GOTO_SEGMENT  BIT(10U)

#define BT_MCS_OPC_SUP_PREV_TRACK    BIT(11U)
#define BT_MCS_OPC_SUP_NEXT_TRACK    BIT(12U)
#define BT_MCS_OPC_SUP_FIRST_TRACK   BIT(13U)
#define BT_MCS_OPC_SUP_LAST_TRACK    BIT(14U)
#define BT_MCS_OPC_SUP_GOTO_TRACK    BIT(15U)

#define BT_MCS_OPC_SUP_PREV_GROUP    BIT(16U)
#define BT_MCS_OPC_SUP_NEXT_GROUP    BIT(17U)
#define BT_MCS_OPC_SUP_FIRST_GROUP   BIT(18U)
#define BT_MCS_OPC_SUP_LAST_GROUP    BIT(19U)
#define BT_MCS_OPC_SUP_GOTO_GROUP    BIT(20U)

#define BT_MCS_OPC_NTF_SUCCESS             0x01U
#define BT_MCS_OPC_NTF_NOT_SUPPORTED       0x02U
#define BT_MCS_OPC_NTF_PLAYER_INACTIVE     0x03U
#define BT_MCS_OPC_NTF_CANNOT_BE_COMPLETED 0x04U

#define BT_MCS_SEARCH_TYPE_TRACK_NAME    0x01U
#define BT_MCS_SEARCH_TYPE_ARTIST_NAME   0x02U
#define BT_MCS_SEARCH_TYPE_ALBUM_NAME    0x03U
#define BT_MCS_SEARCH_TYPE_GROUP_NAME    0x04U
#define BT_MCS_SEARCH_TYPE_EARLIEST_YEAR 0x05U
#define BT_MCS_SEARCH_TYPE_LATEST_YEAR   0x06U
#define BT_MCS_SEARCH_TYPE_GENRE         0x07U
#define BT_MCS_SEARCH_TYPE_ONLY_TRACKS   0x08U
#define BT_MCS_SEARCH_TYPE_ONLY_GROUPS   0x09U

#define SEARCH_LEN_MIN 2U

#define SEARCH_LEN_MAX 64U

#define SEARCH_SCI_LEN_MIN 1   /* An SCI length can be as little as one byte,
                                * for an SCI that has only the type field.
                                * (The SCI len is the length of type + param.)
                                */

#define SEARCH_PARAM_MAX 62U

#define BT_MCS_SCP_NTF_SUCCESS  0x01U
#define BT_MCS_SCP_NTF_FAILURE  0x02U

#define BT_MCS_GROUP_OBJECT_TRACK_TYPE 0x00U
#define BT_MCS_GROUP_OBJECT_GROUP_TYPE 0x01U

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MCS_H_ */
```

## 108.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2019 - 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 336 行

对于仅包含类型字段（Type field）的 SCI，其长度可以只有一个字节。（SCI 长度是 type 与 param 的总长度。）

### 注释 3：原第 376 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_MCS_H_`。

## 108.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mcs_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P107_mchp_mss_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P109_mdns_responder.h_源码浏览.md)
