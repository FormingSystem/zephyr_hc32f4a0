---
id: learning.zephyr-docs.api-source-reference.page-530
title: mii.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mii_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第530章\_mii.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mii_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mii_8h.html)。

## 530.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00027"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
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
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="foldopen00244"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2016 Piotr Mienkowski
 * Copyright 2022 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_MII_H_
#define ZEPHYR_INCLUDE_NET_MII_H_

#include <zephyr/sys/util_macro.h>


#define MII_BMCR       0x0
#define MII_BMSR       0x1
#define MII_PHYID1R    0x2
#define MII_PHYID2R    0x3
#define MII_ANAR       0x4
#define MII_ANLPAR     0x5
#define MII_ANER       0x6
#define MII_ANNPTR     0x7
#define MII_ANLPRNPR   0x8
#define MII_1KTCR      0x9
#define MII_1KSTSR     0xa
#define MII_MMD_ACR    0xd
#define MII_MMD_AADR   0xe
#define MII_ESTAT      0xf

#define MII_BMCR_RESET_BIT           15
#define MII_BMCR_LOOPBACK_BIT        14
#define MII_BMCR_SPEED_LSB_BIT       13
#define MII_BMCR_AUTONEG_ENABLE_BIT  12
#define MII_BMCR_POWER_DOWN_BIT      11
#define MII_BMCR_ISOLATE_BIT         10
#define MII_BMCR_AUTONEG_RESTART_BIT 9
#define MII_BMCR_DUPLEX_MODE_BIT     8
#define MII_BMCR_SPEED_MSB_BIT       6
#define MII_BMCR_RESET               BIT(MII_BMCR_RESET_BIT)
#define MII_BMCR_LOOPBACK            BIT(MII_BMCR_LOOPBACK_BIT)
#define MII_BMCR_SPEED_LSB           BIT(MII_BMCR_SPEED_LSB_BIT)
#define MII_BMCR_AUTONEG_ENABLE      BIT(MII_BMCR_AUTONEG_ENABLE_BIT)
#define MII_BMCR_POWER_DOWN          BIT(MII_BMCR_POWER_DOWN_BIT)
#define MII_BMCR_ISOLATE             BIT(MII_BMCR_ISOLATE_BIT)
#define MII_BMCR_AUTONEG_RESTART     BIT(MII_BMCR_AUTONEG_RESTART_BIT)
#define MII_BMCR_DUPLEX_MODE         BIT(MII_BMCR_DUPLEX_MODE_BIT)
#define MII_BMCR_SPEED_MSB           BIT(MII_BMCR_SPEED_MSB_BIT)
#define MII_BMCR_SPEED_MASK          (MII_BMCR_SPEED_MSB | MII_BMCR_SPEED_LSB)
#define MII_BMCR_SPEED_10            0
#define MII_BMCR_SPEED_100           BIT(MII_BMCR_SPEED_LSB_BIT)
#define MII_BMCR_SPEED_1000          BIT(MII_BMCR_SPEED_MSB_BIT)

#define MII_BMSR_100BASE_T4_BIT       15
#define MII_BMSR_100BASE_X_FULL_BIT   14
#define MII_BMSR_100BASE_X_HALF_BIT   13
#define MII_BMSR_10_FULL_BIT          12
#define MII_BMSR_10_HALF_BIT          11
#define MII_BMSR_100BASE_T2_FULL_BIT  10
#define MII_BMSR_100BASE_T2_HALF_BIT  9
#define MII_BMSR_EXTEND_STATUS_BIT    8
#define MII_BMSR_MF_PREAMB_SUPPR_BIT  6
#define MII_BMSR_AUTONEG_COMPLETE_BIT 5
#define MII_BMSR_REMOTE_FAULT_BIT     4
#define MII_BMSR_AUTONEG_ABILITY_BIT  3
#define MII_BMSR_LINK_STATUS_BIT      2
#define MII_BMSR_JABBER_DETECT_BIT    1
#define MII_BMSR_EXTEND_CAPAB_BIT     0
#define MII_BMSR_100BASE_T4           BIT(MII_BMSR_100BASE_T4_BIT)
#define MII_BMSR_100BASE_X_FULL       BIT(MII_BMSR_100BASE_X_FULL_BIT)
#define MII_BMSR_100BASE_X_HALF       BIT(MII_BMSR_100BASE_X_HALF_BIT)
#define MII_BMSR_10_FULL              BIT(MII_BMSR_10_FULL_BIT)
#define MII_BMSR_10_HALF              BIT(MII_BMSR_10_HALF_BIT)
#define MII_BMSR_100BASE_T2_FULL      BIT(MII_BMSR_100BASE_T2_FULL_BIT)
#define MII_BMSR_100BASE_T2_HALF      BIT(MII_BMSR_100BASE_T2_HALF_BIT)
#define MII_BMSR_EXTEND_STATUS        BIT(MII_BMSR_EXTEND_STATUS_BIT)
#define MII_BMSR_MF_PREAMB_SUPPR      BIT(MII_BMSR_MF_PREAMB_SUPPR_BIT)
#define MII_BMSR_AUTONEG_COMPLETE     BIT(MII_BMSR_AUTONEG_COMPLETE_BIT)
#define MII_BMSR_REMOTE_FAULT         BIT(MII_BMSR_REMOTE_FAULT_BIT)
#define MII_BMSR_AUTONEG_ABILITY      BIT(MII_BMSR_AUTONEG_ABILITY_BIT)
#define MII_BMSR_LINK_STATUS          BIT(MII_BMSR_LINK_STATUS_BIT)
#define MII_BMSR_JABBER_DETECT        BIT(MII_BMSR_JABBER_DETECT_BIT)
#define MII_BMSR_EXTEND_CAPAB         BIT(MII_BMSR_EXTEND_CAPAB_BIT)

#define MII_ADVERTISE_NEXT_PAGE_BIT    15
#define MII_ADVERTISE_LPACK_BIT        14
#define MII_ADVERTISE_REMOTE_FAULT_BIT 13
#define MII_ADVERTISE_ASYM_PAUSE_BIT   11
#define MII_ADVERTISE_PAUSE_BIT        10
#define MII_ADVERTISE_100BASE_T4_BIT   9
#define MII_ADVERTISE_100_FULL_BIT     8
#define MII_ADVERTISE_100_HALF_BIT     7
#define MII_ADVERTISE_10_FULL_BIT      6
#define MII_ADVERTISE_10_HALF_BIT      5
#define MII_ADVERTISE_NEXT_PAGE        BIT(MII_ADVERTISE_NEXT_PAGE_BIT)
#define MII_ADVERTISE_LPACK            BIT(MII_ADVERTISE_LPACK_BIT)
#define MII_ADVERTISE_REMOTE_FAULT     BIT(MII_ADVERTISE_REMOTE_FAULT_BIT)
#define MII_ADVERTISE_ASYM_PAUSE       BIT(MII_ADVERTISE_ASYM_PAUSE_BIT)
#define MII_ADVERTISE_PAUSE            BIT(MII_ADVERTISE_PAUSE_BIT)
#define MII_ADVERTISE_100BASE_T4       BIT(MII_ADVERTISE_100BASE_T4_BIT)
#define MII_ADVERTISE_100_FULL         BIT(MII_ADVERTISE_100_FULL_BIT)
#define MII_ADVERTISE_100_HALF         BIT(MII_ADVERTISE_100_HALF_BIT)
#define MII_ADVERTISE_10_FULL          BIT(MII_ADVERTISE_10_FULL_BIT)
#define MII_ADVERTISE_10_HALF          BIT(MII_ADVERTISE_10_HALF_BIT)
#define MII_ADVERTISE_SEL_MASK         (0x1F << 0)
#define MII_ADVERTISE_SEL_IEEE_802_3   0x01

#define MII_ADVERTISE_1000_FULL_BIT 9
#define MII_ADVERTISE_1000_HALF_BIT 8
#define MII_ADVERTISE_1000_FULL     BIT(MII_ADVERTISE_1000_FULL_BIT)
#define MII_ADVERTISE_1000_HALF     BIT(MII_ADVERTISE_1000_HALF_BIT)

#define MII_ADVERTISE_ALL (MII_ADVERTISE_10_HALF | MII_ADVERTISE_10_FULL |\
                           MII_ADVERTISE_100_HALF | MII_ADVERTISE_100_FULL |\
                           MII_ADVERTISE_SEL_IEEE_802_3)

#define MII_ESTAT_1000BASE_X_FULL  BIT(15)
#define MII_ESTAT_1000BASE_X_HALF  BIT(14)
#define MII_ESTAT_1000BASE_T_FULL  BIT(13)
#define MII_ESTAT_1000BASE_T_HALF  BIT(12)

#define MII_MMD_ACR_DEVAD_MASK      (0x1F << 0)
#define MII_MMD_ACR_ADDR            (0x00 << 14)
#define MII_MMD_ACR_DATA_NO_POS_INC (0x01 << 14)
#define MII_MMD_ACR_DATA_RW_POS_INC (0x10 << 14)
#define MII_MMD_ACR_DATA_W_POS_INC  (0x11 << 14)


#endif /* ZEPHYR_INCLUDE_NET_MII_H_ */
```

## 530.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Piotr Mienkowski。

版权（Copyright）：2022 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 282 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_MII_H_`。

## 530.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mii_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P529_midi.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P531_mipi_display.h_源码浏览.md)
