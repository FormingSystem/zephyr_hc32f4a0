---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-16
title: gap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_gap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html)。

## 16.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00028"></a>
<a id="l00033"></a>
<a id="l00037"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00088"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00102"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00126"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="foldopen00236"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="foldopen00257"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="foldopen00299"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="foldopen00322"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="foldopen00365"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="foldopen00406"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="foldopen00410"></a>
<a id="l00410"></a>
<a id="l00412"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="foldopen00422"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="foldopen00536"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="foldopen00547"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="aassigned__numbers_8h_html"></a>
<a id="abluetooth_2byteorder_8h_html"></a>
<a id="agroup__bt__gap__defines_html_ga07833ed1f79708d5f6a5d0c2e01d4dca"></a>
<a id="agroup__bt__gap__defines_html_ga3cd6d431193b05414020ca5686f4c0e4"></a>
<a id="agroup__bt__gap__defines_html_ga691d9793fd21c41b2c192d65cc2bf6c4"></a>
<a id="agroup__bt__gap__defines_html_ga8ac9dd875bc7480929b5166193c621d0"></a>
<a id="agroup__bt__gap__defines_html_gab7418dd67b5c7fb9b0f9cfd5a55fe272"></a>
<a id="agroup__bt__gap__defines_html_gga07833ed1f79708d5f6a5d0c2e01d4dcaa05b182a44fea67f52015cbfb4d775be8"></a>
<a id="agroup__bt__gap__defines_html_gga07833ed1f79708d5f6a5d0c2e01d4dcaa09292ffe2f0b76b8761fcaad6fbf9ba8"></a>
<a id="agroup__bt__gap__defines_html_gga07833ed1f79708d5f6a5d0c2e01d4dcaa5387de0177d3a9da9fd0c44ca30c7018"></a>
<a id="agroup__bt__gap__defines_html_gga07833ed1f79708d5f6a5d0c2e01d4dcaabb587b376bd6511881d6b70ceaa2af56"></a>
<a id="agroup__bt__gap__defines_html_gga07833ed1f79708d5f6a5d0c2e01d4dcaae48316c135886d9f6d20f7bdba0858c1"></a>
<a id="agroup__bt__gap__defines_html_gga07833ed1f79708d5f6a5d0c2e01d4dcaaf4d48e46c1da164e876e4ded28470c82"></a>
<a id="agroup__bt__gap__defines_html_gga3cd6d431193b05414020ca5686f4c0e4a164fe8b7df50d8e393373153a1f70d1d"></a>
<a id="agroup__bt__gap__defines_html_gga3cd6d431193b05414020ca5686f4c0e4a5fa53f708753d67bd6ec4f54b164b005"></a>
<a id="agroup__bt__gap__defines_html_gga3cd6d431193b05414020ca5686f4c0e4a7f41d38c1a2125bd7c4d1765c8fbee73"></a>
<a id="agroup__bt__gap__defines_html_gga3cd6d431193b05414020ca5686f4c0e4a96900858c146259fc41af27b4cb62247"></a>
<a id="agroup__bt__gap__defines_html_gga3cd6d431193b05414020ca5686f4c0e4a999a15d6ed8c860af7323af1b4d86fe9"></a>
<a id="agroup__bt__gap__defines_html_gga3cd6d431193b05414020ca5686f4c0e4aa4011892d3409238f668c87626587bfd"></a>
<a id="agroup__bt__gap__defines_html_gga3cd6d431193b05414020ca5686f4c0e4ab19b506bc13aad6af3dba925153f4e7d"></a>
<a id="agroup__bt__gap__defines_html_gga3cd6d431193b05414020ca5686f4c0e4ab8fd607ccdc30216fd90d4c6f568b9f6"></a>
<a id="agroup__bt__gap__defines_html_gga3cd6d431193b05414020ca5686f4c0e4ace5a2d3f9fcb1a8913203ee6f437b910"></a>
<a id="agroup__bt__gap__defines_html_gga691d9793fd21c41b2c192d65cc2bf6c4a23fc74a635a05d082b0033b3f152592b"></a>
<a id="agroup__bt__gap__defines_html_gga691d9793fd21c41b2c192d65cc2bf6c4a47ca63851d4380aad42a0a37a17f020d"></a>
<a id="agroup__bt__gap__defines_html_gga691d9793fd21c41b2c192d65cc2bf6c4a53eff400720a20fe1a91da4834bad752"></a>
<a id="agroup__bt__gap__defines_html_gga691d9793fd21c41b2c192d65cc2bf6c4a662049cc8293959194bcb481e1dd50a8"></a>
<a id="agroup__bt__gap__defines_html_gga691d9793fd21c41b2c192d65cc2bf6c4a97d042e48448fdf6a9e35e5d38cb14c3"></a>
<a id="agroup__bt__gap__defines_html_gga691d9793fd21c41b2c192d65cc2bf6c4aaf7e1b40f6464a603e5116db269cacab"></a>
<a id="agroup__bt__gap__defines_html_gga8ac9dd875bc7480929b5166193c621d0a4595d3a3ea30bd4cd51ba4f1c4ab7de9"></a>
<a id="agroup__bt__gap__defines_html_gga8ac9dd875bc7480929b5166193c621d0a55258ac9a7b355db87aeec5d443718f7"></a>
<a id="agroup__bt__gap__defines_html_gga8ac9dd875bc7480929b5166193c621d0a6c5ea1b8392783568b568c74f9f17571"></a>
<a id="agroup__bt__gap__defines_html_gga8ac9dd875bc7480929b5166193c621d0aeda2301e9eb191e742375e54bb765684"></a>
<a id="agroup__bt__gap__defines_html_gga8ac9dd875bc7480929b5166193c621d0af843db0752f3360ccb1a02c456ca9e5e"></a>
<a id="agroup__bt__gap__defines_html_ggab7418dd67b5c7fb9b0f9cfd5a55fe272a2385af24a5a82f4d799674443b92e966"></a>
<a id="agroup__bt__gap__defines_html_ggab7418dd67b5c7fb9b0f9cfd5a55fe272a8a82746ee64ffbcc62e79fdd8e0e30a0"></a>
<a id="agroup__bt__gap__defines_html_ggab7418dd67b5c7fb9b0f9cfd5a55fe272aa8587383f9ea245e8c279fdd63417a19"></a>
<a id="agroup__bt__gap__defines_html_ggab7418dd67b5c7fb9b0f9cfd5a55fe272aec9324d8e0997e1ace59895e168087e8"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2019 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_GAP_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_GAP_H_

#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/byteorder.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif


#define BT_COMP_ID_LF           0x05f1

#define BT_GAP_SCAN_FAST_INTERVAL_MIN           0x0030
#define BT_GAP_SCAN_FAST_INTERVAL               0x0060
#define BT_GAP_SCAN_FAST_WINDOW                 0x0030
#define BT_GAP_SCAN_SLOW_INTERVAL_1             0x0800
#define BT_GAP_SCAN_SLOW_WINDOW_1               0x0012
#define BT_GAP_SCAN_SLOW_INTERVAL_2             0x1000
#define BT_GAP_SCAN_SLOW_WINDOW_2               0x0012
#define BT_GAP_ADV_FAST_INT_MIN_1               0x0030
#define BT_GAP_ADV_FAST_INT_MAX_1               0x0060
#define BT_GAP_ADV_FAST_INT_MIN_2               0x00a0
#define BT_GAP_ADV_FAST_INT_MAX_2               0x00f0
#define BT_GAP_ADV_SLOW_INT_MIN                 0x0640
#define BT_GAP_ADV_SLOW_INT_MAX                 0x0780
#define BT_GAP_PER_ADV_FAST_INT_MIN_1           0x0018
#define BT_GAP_PER_ADV_FAST_INT_MAX_1           0x0030
#define BT_GAP_PER_ADV_FAST_INT_MIN_2           0x0050
#define BT_GAP_PER_ADV_FAST_INT_MAX_2           0x0078
#define BT_GAP_PER_ADV_SLOW_INT_MIN             0x0320
#define BT_GAP_PER_ADV_SLOW_INT_MAX             0x03C0
#define BT_GAP_INIT_CONN_INT_MIN                0x0018
#define BT_GAP_INIT_CONN_INT_MAX                0x0028

enum bt_gap_le_phy {
        BT_GAP_LE_PHY_NONE                    = 0,
        BT_GAP_LE_PHY_1M                      = BIT(0),
        BT_GAP_LE_PHY_2M                      = BIT(1),
        BT_GAP_LE_PHY_CODED                   = BIT(2),
        BT_GAP_LE_PHY_CODED_S8                = BIT(3),
        BT_GAP_LE_PHY_CODED_S2                = BIT(4),
};

enum bt_gap_adv_type {
        BT_GAP_ADV_TYPE_ADV_IND               = 0x00,
        BT_GAP_ADV_TYPE_ADV_DIRECT_IND        = 0x01,
        BT_GAP_ADV_TYPE_ADV_SCAN_IND          = 0x02,
        BT_GAP_ADV_TYPE_ADV_NONCONN_IND       = 0x03,
        BT_GAP_ADV_TYPE_SCAN_RSP              = 0x04,
        BT_GAP_ADV_TYPE_EXT_ADV               = 0x05,
};

enum bt_gap_adv_prop {
        BT_GAP_ADV_PROP_CONNECTABLE           = BIT(0),
        BT_GAP_ADV_PROP_SCANNABLE             = BIT(1),
        BT_GAP_ADV_PROP_DIRECTED              = BIT(2),
        BT_GAP_ADV_PROP_SCAN_RESPONSE         = BIT(3),
        BT_GAP_ADV_PROP_EXT_ADV               = BIT(4),
};

#define BT_GAP_ADV_MAX_ADV_DATA_LEN             31
#define BT_GAP_ADV_MAX_EXT_ADV_DATA_LEN         1650

#define BT_GAP_TX_POWER_INVALID                 0x7f
#define BT_GAP_RSSI_INVALID                     0x7f
#define BT_GAP_SID_INVALID                      0xff
#define BT_GAP_NO_TIMEOUT                       0x0000

/* The maximum allowed high duty cycle directed advertising timeout, 1.28
 * seconds in 10 ms unit.
 */
#define BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT  128

#define BT_GAP_DATA_LEN_DEFAULT                 0x001b /* 27 bytes */
#define BT_GAP_DATA_LEN_MAX                     0x00fb /* 251 bytes */

#define BT_GAP_DATA_TIME_DEFAULT                0x0148 /* 328 us */
#define BT_GAP_DATA_TIME_MAX                    0x4290 /* 17040 us */

#define BT_GAP_SID_MIN                          0x00
#define BT_GAP_SID_MAX                          0x0F
#define BT_GAP_PER_ADV_MAX_SKIP                 0x01F3
#define BT_GAP_PER_ADV_MIN_TIMEOUT              0x000A /* 100 ms */
#define BT_GAP_PER_ADV_MAX_TIMEOUT              0x4000 /* 163.84 s */
#define BT_GAP_PER_ADV_MIN_INTERVAL             0x0006 /* 7.5 ms */
#define BT_GAP_PER_ADV_MAX_INTERVAL             0xFFFF /* 81.91875 s */

#define BT_GAP_ADV_INTERVAL_TO_US(_interval) ((uint32_t)((_interval) * 625U))

#define BT_GAP_ADV_INTERVAL_TO_MS(_interval) (BT_GAP_ADV_INTERVAL_TO_US(_interval) / USEC_PER_MSEC)

#define BT_GAP_ISO_INTERVAL_TO_US(_interval) ((uint32_t)((_interval) * 1250U))

#define BT_GAP_ISO_INTERVAL_TO_MS(_interval) (BT_GAP_ISO_INTERVAL_TO_US(_interval) / USEC_PER_MSEC)

#define BT_GAP_PER_ADV_INTERVAL_TO_US(_interval) ((uint32_t)((_interval) * 1250U))

#define BT_GAP_PER_ADV_INTERVAL_TO_MS(_interval)                                                   \
        (BT_GAP_PER_ADV_INTERVAL_TO_US(_interval) / USEC_PER_MSEC)

#define BT_GAP_US_TO_ADV_INTERVAL(_interval) ((uint16_t)((_interval) / 625U))

#define BT_GAP_MS_TO_ADV_INTERVAL(_interval)                                                       \
        (BT_GAP_US_TO_ADV_INTERVAL((_interval) * USEC_PER_MSEC))

#define BT_GAP_US_TO_PER_ADV_INTERVAL(_interval) ((uint16_t)((_interval) / 1250U))

#define BT_GAP_MS_TO_PER_ADV_INTERVAL(_interval)                                                   \
        (BT_GAP_US_TO_PER_ADV_INTERVAL((_interval) * USEC_PER_MSEC))

#define BT_GAP_MS_TO_PER_ADV_SYNC_TIMEOUT(_timeout) ((uint16_t)((_timeout) / 10U))

#define BT_GAP_US_TO_PER_ADV_SYNC_TIMEOUT(_timeout)                                                \
        (BT_GAP_MS_TO_PER_ADV_SYNC_TIMEOUT((_timeout) / USEC_PER_MSEC))

#define BT_GAP_US_TO_SCAN_INTERVAL(_interval) ((uint16_t)((_interval) / 625U))

#define BT_GAP_MS_TO_SCAN_INTERVAL(_interval)                                                      \
        (BT_GAP_US_TO_SCAN_INTERVAL((_interval) * USEC_PER_MSEC))

#define BT_GAP_US_TO_SCAN_WINDOW(_window) ((uint16_t)((_window) / 625U))

#define BT_GAP_MS_TO_SCAN_WINDOW(_window) (BT_GAP_US_TO_SCAN_WINDOW((_window) * USEC_PER_MSEC))

#define BT_GAP_US_TO_CONN_INTERVAL(_interval) ((uint16_t)((_interval) / 1250U))

#define BT_GAP_MS_TO_CONN_INTERVAL(_interval)                                                      \
        (BT_GAP_US_TO_CONN_INTERVAL((_interval) * USEC_PER_MSEC))

#define BT_GAP_MS_TO_CONN_TIMEOUT(_timeout) ((uint16_t)((_timeout) / 10U))

#define BT_GAP_US_TO_CONN_TIMEOUT(_timeout) (BT_GAP_MS_TO_CONN_TIMEOUT((_timeout) / USEC_PER_MSEC))

#define BT_GAP_US_TO_CONN_EVENT_LEN(_event_len) ((uint16_t)((_event_len) / 625U))

#define BT_GAP_MS_TO_CONN_EVENT_LEN(_event_len)                                                    \
        (BT_GAP_US_TO_CONN_EVENT_LEN((_event_len) * USEC_PER_MSEC))

enum bt_gap_cte {
        BT_GAP_CTE_AOA = 0x00,
        BT_GAP_CTE_AOD_1US = 0x01,
        BT_GAP_CTE_AOD_2US = 0x02,
        BT_GAP_CTE_NONE = 0xFF,
};

enum bt_gap_sca {
        BT_GAP_SCA_UNKNOWN = 0,
        BT_GAP_SCA_251_500 = 0,
        BT_GAP_SCA_151_250 = 1,
        BT_GAP_SCA_101_150 = 2,
        BT_GAP_SCA_76_100 = 3,
        BT_GAP_SCA_51_75 = 4,
        BT_GAP_SCA_31_50 = 5,
        BT_GAP_SCA_21_30 = 6,
        BT_GAP_SCA_0_20 = 7,
};

#define BT_LE_SUPP_FEAT_40_ENCODE(w64) BT_BYTES_LIST_LE40(w64)

#define BT_LE_SUPP_FEAT_32_ENCODE(w64) BT_BYTES_LIST_LE32(w64)

#define BT_LE_SUPP_FEAT_24_ENCODE(w64) BT_BYTES_LIST_LE24(w64)

#define BT_LE_SUPP_FEAT_16_ENCODE(w64) BT_BYTES_LIST_LE16(w64)

#define BT_LE_SUPP_FEAT_8_ENCODE(w64) \
        (((w64) >> 0) & 0xFF)

#define BT_LE_SUPP_FEAT_VALIDATE(w64) \
        BUILD_ASSERT(!((w64) & (~BIT64_MASK(40))), \
                     "RFU bit in LE Supported Features are not zeros.")


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_GAP_H_ */
```

## 16.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权所有（Copyright）2019 Nordic Semiconductor ASA。

SPDX-License-Identifier: Apache-2.0。

### 注释 2：原第 157 行

高占空比定向广播（high duty cycle directed advertising）允许的最大超时为 1.28 秒，以 10 ms 为单位表示。

### 注释 3：原第 163 行

27 字节（bytes）。

### 注释 4：原第 165 行

251 字节（bytes）。

### 注释 5：原第 168 行

328 微秒（μs）。

### 注释 6：原第 170 行

17040 微秒（μs）。

### 注释 7：原第 181 行

100 毫秒（ms）。

### 注释 8：原第 183 行

163.84 秒（s）。

### 注释 9：原第 185 行

7.5 毫秒（ms）。

### 注释 10：原第 187 行

81.91875 秒（s）。

### 注释 11：原第 559 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_GAP_H_`。

## 16.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html)
- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [zephyr/bluetooth/byteorder.h](../byteorder_reference/P004_蓝牙字节序头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_gap_le_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga691d9793fd21c41b2c192d65cc2bf6c4)
- [BT_GAP_LE_PHY_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4aaf7e1b40f6464a603e5116db269cacab)
- [BT_GAP_LE_PHY_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a53eff400720a20fe1a91da4834bad752)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_GAP_LE_PHY_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a662049cc8293959194bcb481e1dd50a8)
- [BT_GAP_LE_PHY_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a97d042e48448fdf6a9e35e5d38cb14c3)
- [BT_GAP_LE_PHY_CODED_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a47ca63851d4380aad42a0a37a17f020d)
- [BT_GAP_LE_PHY_CODED_S2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a23fc74a635a05d082b0033b3f152592b)
- [bt_gap_adv_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga07833ed1f79708d5f6a5d0c2e01d4dca)
- [BT_GAP_ADV_TYPE_ADV_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaaf4d48e46c1da164e876e4ded28470c82)
- [BT_GAP_ADV_TYPE_ADV_DIRECT_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaa05b182a44fea67f52015cbfb4d775be8)
- [BT_GAP_ADV_TYPE_ADV_SCAN_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaae48316c135886d9f6d20f7bdba0858c1)
- [BT_GAP_ADV_TYPE_ADV_NONCONN_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaabb587b376bd6511881d6b70ceaa2af56)
- [BT_GAP_ADV_TYPE_SCAN_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaa5387de0177d3a9da9fd0c44ca30c7018)
- [BT_GAP_ADV_TYPE_EXT_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaa09292ffe2f0b76b8761fcaad6fbf9ba8)
- [bt_gap_adv_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga8ac9dd875bc7480929b5166193c621d0)
- [BT_GAP_ADV_PROP_CONNECTABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0af843db0752f3360ccb1a02c456ca9e5e)
- [BT_GAP_ADV_PROP_SCANNABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0a6c5ea1b8392783568b568c74f9f17571)
- [BT_GAP_ADV_PROP_DIRECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0a4595d3a3ea30bd4cd51ba4f1c4ab7de9)
- [BT_GAP_ADV_PROP_SCAN_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0a55258ac9a7b355db87aeec5d443718f7)
- [BT_GAP_ADV_PROP_EXT_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0aeda2301e9eb191e742375e54bb765684)
- [bt_gap_cte](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gab7418dd67b5c7fb9b0f9cfd5a55fe272)
- [BT_GAP_CTE_AOA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ggab7418dd67b5c7fb9b0f9cfd5a55fe272a8a82746ee64ffbcc62e79fdd8e0e30a0)
- [BT_GAP_CTE_AOD_1US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ggab7418dd67b5c7fb9b0f9cfd5a55fe272aa8587383f9ea245e8c279fdd63417a19)
- [BT_GAP_CTE_AOD_2US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ggab7418dd67b5c7fb9b0f9cfd5a55fe272a2385af24a5a82f4d799674443b92e966)
- [BT_GAP_CTE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ggab7418dd67b5c7fb9b0f9cfd5a55fe272aec9324d8e0997e1ace59895e168087e8)
- [bt_gap_sca](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga3cd6d431193b05414020ca5686f4c0e4)
- [BT_GAP_SCA_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4ace5a2d3f9fcb1a8913203ee6f437b910)
- [BT_GAP_SCA_251_500](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4a96900858c146259fc41af27b4cb62247)
- [BT_GAP_SCA_151_250](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4ab19b506bc13aad6af3dba925153f4e7d)
- [BT_GAP_SCA_101_150](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4a7f41d38c1a2125bd7c4d1765c8fbee73)
- [BT_GAP_SCA_76_100](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4aa4011892d3409238f668c87626587bfd)
- [BT_GAP_SCA_51_75](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4a999a15d6ed8c860af7323af1b4d86fe9)
- [BT_GAP_SCA_31_50](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4a5fa53f708753d67bd6ec4f54b164b005)
- [BT_GAP_SCA_21_30](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4a164fe8b7df50d8e393373153a1f70d1d)
- [BT_GAP_SCA_0_20](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4ab8fd607ccdc30216fd90d4c6f568b9f6)
- [assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [byteorder.h](../byteorder_reference/P004_蓝牙字节序头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P015_fnmatch.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P017_hfp_hf.h_源码浏览.md)
