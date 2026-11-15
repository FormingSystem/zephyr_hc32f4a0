---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-2
title: 定义与分配编号（Defines and Assigned Numbers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_定义与分配编号（Defines and Assigned Numbers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙通用接入配置文件（Generic Access Profile）的定义和分配编号。

<a id="details"></a>

蓝牙通用接入配置文件（Generic Access Profile）的定义和分配编号。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga39ab5040c9471631486da7dbebd9c36f"></a>

```c
#define BT_GAP_ADV_MAX_ADV_DATA_LEN 31
```

相关声明：[BT_GAP_ADV_MAX_ADV_DATA_LEN](#ga39ab5040c9471631486da7dbebd9c36f)。

最大广播数据长度（Maximum advertising data length）。

<a id="r_ga53af114e4925482739dc50dc84c2f641"></a>

```c
#define BT_GAP_ADV_MAX_EXT_ADV_DATA_LEN 1650
```

相关声明：[BT_GAP_ADV_MAX_EXT_ADV_DATA_LEN](#ga53af114e4925482739dc50dc84c2f641)。

扩展广播数据（Extended Advertising Data）的最大长度。

<a id="r_ga61ccce819d75313cb2ee58309ed4b275"></a>

```c
#define BT_GAP_TX_POWER_INVALID 0x7f
```

相关声明：[BT_GAP_TX_POWER_INVALID](#ga61ccce819d75313cb2ee58309ed4b275)。

哨兵值（Sentinel Value），表示以 dBm 为单位的发射功率（TX Power）不可用或未知。

<a id="r_ga64b5c5e429dadf1e875984f69cd399dc"></a>

```c
#define BT_GAP_RSSI_INVALID 0x7f
```

相关声明：[BT_GAP_RSSI_INVALID](#ga64b5c5e429dadf1e875984f69cd399dc)。

哨兵值（Sentinel Value），表示以 dBm 为单位的接收信号强度指示（RSSI）不可用或未知。

<a id="r_ga103af3e3142473be8897cd2647dca915"></a>

```c
#define BT_GAP_SID_INVALID 0xff
```

相关声明：[BT_GAP_SID_INVALID](#ga103af3e3142473be8897cd2647dca915)。

哨兵值（Sentinel Value），表示广播集标识符（Advertising Set Identifier）无效或未知。

<a id="r_ga9d6b2af6b96eab6356ded93c54301ef6"></a>

```c
#define BT_GAP_NO_TIMEOUT 0x0000
```

相关声明：[BT_GAP_NO_TIMEOUT](#ga9d6b2af6b96eab6356ded93c54301ef6)。

哨兵值（Sentinel Value），表示未设置超时（Timeout）。

<a id="r_gabe483d4dd601b11ac3eea570c962b1ec"></a>

```c
#define BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT 128
```

相关声明：[BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT](#gabe483d4dd601b11ac3eea570c962b1ec)。

<a id="r_ga90cfab7c375a8af6f9224a5635cbd023"></a>

```c
#define BT_GAP_DATA_LEN_DEFAULT 0x001b /* 27 bytes */
```

相关声明：[BT_GAP_DATA_LEN_DEFAULT](#ga90cfab7c375a8af6f9224a5635cbd023)。

默认数据长度（Default Data Length）。

<a id="r_gacf5f35866d4677bd45c6e567886cabb9"></a>

```c
#define BT_GAP_DATA_LEN_MAX 0x00fb /* 251 bytes */
```

相关声明：[BT_GAP_DATA_LEN_MAX](#gacf5f35866d4677bd45c6e567886cabb9)。

最大数据长度（Maximum Data Length）。

<a id="r_ga245249c0b6f8ccc419f2132f76362908"></a>

```c
#define BT_GAP_DATA_TIME_DEFAULT 0x0148 /* 328 us */
```

相关声明：[BT_GAP_DATA_TIME_DEFAULT](#ga245249c0b6f8ccc419f2132f76362908)。

默认数据时间（Default Data Time）。

<a id="r_ga379b5d8d7f243abbc584c288cd01815f"></a>

```c
#define BT_GAP_DATA_TIME_MAX 0x4290 /* 17040 us */
```

相关声明：[BT_GAP_DATA_TIME_MAX](#ga379b5d8d7f243abbc584c288cd01815f)。

最大数据时间（Maximum Data Time）。

<a id="r_gacf05b7660d2ae85f64e2a220abf8e57d"></a>

```c
#define BT_GAP_SID_MIN 0x00
```

相关声明：[BT_GAP_SID_MIN](#gacf05b7660d2ae85f64e2a220abf8e57d)。

最小广播集数量（Minimum Advertising Set Number）。

<a id="r_gafa6f803fe3ada07030fb1f2f725940c4"></a>

```c
#define BT_GAP_SID_MAX 0x0F
```

相关声明：[BT_GAP_SID_MAX](#gafa6f803fe3ada07030fb1f2f725940c4)。

最大广播集数量（Maximum Advertising Set Number）。

<a id="r_gaf92b229c47309a7a5e99047f28b860e7"></a>

```c
#define BT_GAP_PER_ADV_MAX_SKIP 0x01F3
```

相关声明：[BT_GAP_PER_ADV_MAX_SKIP](#gaf92b229c47309a7a5e99047f28b860e7)。

成功接收后可跳过的连续周期广播事件（Periodic Advertisement Events）的最大数量。

<a id="r_ga17d8ae7e98f6a1dfead4f8ecb75f9645"></a>

```c
#define BT_GAP_PER_ADV_MIN_TIMEOUT 0x000A /* 100 ms */
```

相关声明：[BT_GAP_PER_ADV_MIN_TIMEOUT](#ga17d8ae7e98f6a1dfead4f8ecb75f9645)。

最小周期广播超时（Periodic Advertising Timeout），单位为 `N * 10 ms`。

<a id="r_gad6674199f615fa6ecaeb1fe9d099e04c"></a>

```c
#define BT_GAP_PER_ADV_MAX_TIMEOUT 0x4000 /* 163.84 s */
```

相关声明：[BT_GAP_PER_ADV_MAX_TIMEOUT](#gad6674199f615fa6ecaeb1fe9d099e04c)。

最大周期广播超时（Periodic Advertising Timeout），单位为 `N * 10 ms`。

<a id="r_ga07e21fdeb8a0a0b967690898bef2f7aa"></a>

```c
#define BT_GAP_PER_ADV_MIN_INTERVAL 0x0006 /* 7.5 ms */
```

相关声明：[BT_GAP_PER_ADV_MIN_INTERVAL](#ga07e21fdeb8a0a0b967690898bef2f7aa)。

最小周期广播间隔（Minimum Periodic Advertising Interval），为 N × 1.25 毫秒。

<a id="r_ga80bf3f1fb6f34a2c4363687149c365bd"></a>

```c
#define BT_GAP_PER_ADV_MAX_INTERVAL 0xFFFF /* 81.91875 s */
```

相关声明：[BT_GAP_PER_ADV_MAX_INTERVAL](#ga80bf3f1fb6f34a2c4363687149c365bd)。

最大周期广播间隔（Maximum Periodic Advertising Interval），为 N × 1.25 毫秒。

<a id="r_ga6e10b5311c785ad7eea10743987c0f27"></a>

```c
#define BT_GAP_ADV_INTERVAL_TO_US(_interval)
```

相关声明：[BT_GAP_ADV_INTERVAL_TO_US](#ga6e10b5311c785ad7eea10743987c0f27)。

将广播间隔（Advertising Interval，`N * 0.625 ms`）转换为微秒。

<a id="r_ga7261e64328e433d333d88d3a4cad21de"></a>

```c
#define BT_GAP_ADV_INTERVAL_TO_MS(_interval)
```

相关声明：[BT_GAP_ADV_INTERVAL_TO_MS](#ga7261e64328e433d333d88d3a4cad21de)。

将广播间隔（Advertising Interval，`N * 0.625 ms`）转换为毫秒。

<a id="r_ga4feca4664259c43121c2ff481d9ee611"></a>

```c
#define BT_GAP_ISO_INTERVAL_TO_US(_interval)
```

相关声明：[BT_GAP_ISO_INTERVAL_TO_US](#ga4feca4664259c43121c2ff481d9ee611)。

将等时间隔（Isochronous Interval，`N * 1.25 ms`）转换为微秒。

<a id="r_ga46c1e49ca3285ed9fc1b4ac593a25cd3"></a>

```c
#define BT_GAP_ISO_INTERVAL_TO_MS(_interval)
```

相关声明：[BT_GAP_ISO_INTERVAL_TO_MS](#ga46c1e49ca3285ed9fc1b4ac593a25cd3)。

将等时间隔（Isochronous Interval，`N * 1.25 ms`）转换为毫秒。

<a id="r_ga63587ef565ccde477b9c6f03faf778a5"></a>

```c
#define BT_GAP_PER_ADV_INTERVAL_TO_US(_interval)
```

相关声明：[BT_GAP_PER_ADV_INTERVAL_TO_US](#ga63587ef565ccde477b9c6f03faf778a5)。

将周期广播间隔（Periodic Advertising Interval，`N * 1.25 ms`）转换为微秒（原文末尾有一个 `*`）。

<a id="r_gac240015012694df3557679d99da6c1a9"></a>

```c
#define BT_GAP_PER_ADV_INTERVAL_TO_MS(_interval)
```

相关声明：[BT_GAP_PER_ADV_INTERVAL_TO_MS](#gac240015012694df3557679d99da6c1a9)。

将周期广播间隔（Periodic Advertising Interval，`N * 1.25 ms`）转换为毫秒。

<a id="r_gac79626389f62bb7b3e5b5f6d3a5eaf2b"></a>

```c
#define BT_GAP_US_TO_ADV_INTERVAL(_interval)
```

相关声明：[BT_GAP_US_TO_ADV_INTERVAL](#gac79626389f62bb7b3e5b5f6d3a5eaf2b)。

将微秒转换为广播间隔（Advertising Interval）单位，每单位为 0.625 ms。

<a id="r_gaef9c34f229f1b8b06d3e6cd44a1014ef"></a>

```c
#define BT_GAP_MS_TO_ADV_INTERVAL(_interval)
```

相关声明：[BT_GAP_MS_TO_ADV_INTERVAL](#gaef9c34f229f1b8b06d3e6cd44a1014ef)。

将毫秒转换为广播间隔（Advertising Interval）单位，每单位为 0.625 ms。

<a id="r_ga5a9da01507b4356c2ad6f8309257f2ce"></a>

```c
#define BT_GAP_US_TO_PER_ADV_INTERVAL(_interval)
```

相关声明：[BT_GAP_US_TO_PER_ADV_INTERVAL](#ga5a9da01507b4356c2ad6f8309257f2ce)。

将微秒转换为周期广播间隔（Periodic Advertising Interval）单位，每单位为 1.25 ms。

<a id="r_ga15ec0bc7c9bab797d6c5595269a33ea4"></a>

```c
#define BT_GAP_MS_TO_PER_ADV_INTERVAL(_interval)
```

相关声明：[BT_GAP_MS_TO_PER_ADV_INTERVAL](#ga15ec0bc7c9bab797d6c5595269a33ea4)。

将毫秒转换为周期广播间隔（Periodic Advertising Interval）单位，每单位为 1.25 ms。

<a id="r_ga242a6a4e3dd138073c01bc600c9642eb"></a>

```c
#define BT_GAP_MS_TO_PER_ADV_SYNC_TIMEOUT(_timeout)
```

相关声明：[BT_GAP_MS_TO_PER_ADV_SYNC_TIMEOUT](#ga242a6a4e3dd138073c01bc600c9642eb)。

将毫秒转换为周期广播同步超时（Periodic Advertising Sync Timeout）单位，每单位为 10 ms。

<a id="r_gaf33284a372b21e24c53deb5e3a6a91aa"></a>

```c
#define BT_GAP_US_TO_PER_ADV_SYNC_TIMEOUT(_timeout)
```

相关声明：[BT_GAP_US_TO_PER_ADV_SYNC_TIMEOUT](#gaf33284a372b21e24c53deb5e3a6a91aa)。

将微秒转换为周期广播同步超时（Periodic Advertising Sync Timeout）单位，每单位为 10 ms。

<a id="r_gab65e489c4a799774f6511c6ce5b65ea2"></a>

```c
#define BT_GAP_US_TO_SCAN_INTERVAL(_interval)
```

相关声明：[BT_GAP_US_TO_SCAN_INTERVAL](#gab65e489c4a799774f6511c6ce5b65ea2)。

将微秒转换为扫描间隔（Scan Interval）单位，每单位为 0.625 ms。

<a id="r_gad18c4a9774014081833905fc9e03fb15"></a>

```c
#define BT_GAP_MS_TO_SCAN_INTERVAL(_interval)
```

相关声明：[BT_GAP_MS_TO_SCAN_INTERVAL](#gad18c4a9774014081833905fc9e03fb15)。

将毫秒转换为扫描间隔（Scan Interval）单位，每单位为 0.625 ms。

<a id="r_gaac5d0ec82d9730b793960c0470ac6342"></a>

```c
#define BT_GAP_US_TO_SCAN_WINDOW(_window)
```

相关声明：[BT_GAP_US_TO_SCAN_WINDOW](#gaac5d0ec82d9730b793960c0470ac6342)。

将微秒转换为扫描窗口（Scan Window）单位，每单位为 0.625 ms。

<a id="r_ga5204f7e42b4e33eb8ae4ae71b82a4c88"></a>

```c
#define BT_GAP_MS_TO_SCAN_WINDOW(_window)
```

相关声明：[BT_GAP_MS_TO_SCAN_WINDOW](#ga5204f7e42b4e33eb8ae4ae71b82a4c88)。

将毫秒转换为扫描窗口（Scan Window）单位，每单位为 0.625 ms。

<a id="r_gab12ba919a5a389b4c342d142d3a9ce6e"></a>

```c
#define BT_GAP_US_TO_CONN_INTERVAL(_interval)
```

相关声明：[BT_GAP_US_TO_CONN_INTERVAL](#gab12ba919a5a389b4c342d142d3a9ce6e)。

将微秒转换为连接间隔（Connection Interval）单位，每单位为 1.25 ms。

<a id="r_ga75985e2c444da7b2426cc746c9781c8c"></a>

```c
#define BT_GAP_MS_TO_CONN_INTERVAL(_interval)
```

相关声明：[BT_GAP_MS_TO_CONN_INTERVAL](#ga75985e2c444da7b2426cc746c9781c8c)。

将毫秒转换为连接间隔（Connection Interval）单位，每单位为 1.25 ms。

<a id="r_ga24f79cacceeea262987f3cdaf2ef6bc3"></a>

```c
#define BT_GAP_MS_TO_CONN_TIMEOUT(_timeout)
```

相关声明：[BT_GAP_MS_TO_CONN_TIMEOUT](#ga24f79cacceeea262987f3cdaf2ef6bc3)。

将毫秒转换为连接监督超时（Connection Supervision Timeout）单位，每单位为 10 ms。

<a id="r_ga317a60f9edb371fef180130282805539"></a>

```c
#define BT_GAP_US_TO_CONN_TIMEOUT(_timeout)
```

相关声明：[BT_GAP_US_TO_CONN_TIMEOUT](#ga317a60f9edb371fef180130282805539)。

将微秒转换为连接监督超时（Connection Supervision Timeout）单位，每单位为 10 ms。

<a id="r_ga8905e22b1864021b77367c228b8bff48"></a>

```c
#define BT_GAP_US_TO_CONN_EVENT_LEN(_event_len)
```

相关声明：[BT_GAP_US_TO_CONN_EVENT_LEN](#ga8905e22b1864021b77367c228b8bff48)。

将毫秒转换为连接事件长度（Connection Event Length）单位，原文给出的单位值为 0.625。

<a id="r_gaa3703cccd343dbb6418fdeb47a718eb5"></a>

```c
#define BT_GAP_MS_TO_CONN_EVENT_LEN(_event_len)
```

相关声明：[BT_GAP_MS_TO_CONN_EVENT_LEN](#gaa3703cccd343dbb6418fdeb47a718eb5)。

将毫秒转换为连接事件长度（Connection Event Length）单位，原文给出的单位值为 0.625。

<a id="r_ga799f6cb9dd02b9995ed76fbe97be3eb3"></a>

```c
#define BT_LE_SUPP_FEAT_40_ENCODE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_40_ENCODE](#ga799f6cb9dd02b9995ed76fbe97be3eb3)。

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 40 位，以小端序（Little-Endian）编码为数组值。

<a id="r_ga7aa92098e33840ff02cb8c0435637094"></a>

```c
#define BT_LE_SUPP_FEAT_32_ENCODE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_32_ENCODE](#ga7aa92098e33840ff02cb8c0435637094)。

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 4 字节，以小端序（Little-Endian）编码为长度为 4 字节的数组。

<a id="r_gab8739c92f8d50b796539a21027c3b6eb"></a>

```c
#define BT_LE_SUPP_FEAT_24_ENCODE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_24_ENCODE](#gab8739c92f8d50b796539a21027c3b6eb)。

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 3 字节，以小端序（Little-Endian）编码为长度为 3 字节的数组。

<a id="r_ga3c29ad99d6a6e020148590381ab08b17"></a>

```c
#define BT_LE_SUPP_FEAT_16_ENCODE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_16_ENCODE](#ga3c29ad99d6a6e020148590381ab08b17)。

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 2 字节，以小端序（Little-Endian）编码为长度为 2 字节的数组。

<a id="r_ga8fac302925ac3ef8982630e6a0ec13af"></a>

```c
#define BT_LE_SUPP_FEAT_8_ENCODE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_8_ENCODE](#ga8fac302925ac3ef8982630e6a0ec13af)。

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低字节编码为长度为 1 字节的数组。

<a id="r_ga86266eaf452dfaf82f097992e01397c8"></a>

```c
#define BT_LE_SUPP_FEAT_VALIDATE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_VALIDATE](#ga86266eaf452dfaf82f097992e01397c8)。

验证低功耗蓝牙支持特性（LE Supported Features）值是否未使用为未来用途保留的位。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.2\_枚举（Enumerations）

<a id="r_ga691d9793fd21c41b2c192d65cc2bf6c4"></a>

```c
enum bt_gap_le_phy { BT_GAP_LE_PHY_NONE = 0 , BT_GAP_LE_PHY_1M = (1UL << (0)) , BT_GAP_LE_PHY_2M = (1UL << (1)) , BT_GAP_LE_PHY_CODED = (1UL << (2)) , BT_GAP_LE_PHY_CODED_S8 = (1UL << (3)) , BT_GAP_LE_PHY_CODED_S2 = (1UL << (4)) }
```

相关声明：[bt_gap_le_phy](#ga691d9793fd21c41b2c192d65cc2bf6c4)、[BT_GAP_LE_PHY_NONE](#gga691d9793fd21c41b2c192d65cc2bf6c4aaf7e1b40f6464a603e5116db269cacab)、[BT_GAP_LE_PHY_1M](#gga691d9793fd21c41b2c192d65cc2bf6c4a53eff400720a20fe1a91da4834bad752)、[BT_GAP_LE_PHY_2M](#gga691d9793fd21c41b2c192d65cc2bf6c4a662049cc8293959194bcb481e1dd50a8)、[BT_GAP_LE_PHY_CODED](#gga691d9793fd21c41b2c192d65cc2bf6c4a97d042e48448fdf6a9e35e5d38cb14c3)、[BT_GAP_LE_PHY_CODED_S8](#gga691d9793fd21c41b2c192d65cc2bf6c4a47ca63851d4380aad42a0a37a17f020d)、[BT_GAP_LE_PHY_CODED_S2](#gga691d9793fd21c41b2c192d65cc2bf6c4a23fc74a635a05d082b0033b3f152592b)。

低功耗蓝牙物理层类型（LE PHY Types）。

<a id="r_ga07833ed1f79708d5f6a5d0c2e01d4dca"></a>

```c
enum bt_gap_adv_type { BT_GAP_ADV_TYPE_ADV_IND = 0x00 , BT_GAP_ADV_TYPE_ADV_DIRECT_IND = 0x01 , BT_GAP_ADV_TYPE_ADV_SCAN_IND = 0x02 , BT_GAP_ADV_TYPE_ADV_NONCONN_IND = 0x03 , BT_GAP_ADV_TYPE_SCAN_RSP = 0x04 , BT_GAP_ADV_TYPE_EXT_ADV = 0x05 }
```

相关声明：[bt_gap_adv_type](#ga07833ed1f79708d5f6a5d0c2e01d4dca)、[BT_GAP_ADV_TYPE_ADV_IND](#gga07833ed1f79708d5f6a5d0c2e01d4dcaaf4d48e46c1da164e876e4ded28470c82)、[BT_GAP_ADV_TYPE_ADV_DIRECT_IND](#gga07833ed1f79708d5f6a5d0c2e01d4dcaa05b182a44fea67f52015cbfb4d775be8)、[BT_GAP_ADV_TYPE_ADV_SCAN_IND](#gga07833ed1f79708d5f6a5d0c2e01d4dcaae48316c135886d9f6d20f7bdba0858c1)、[BT_GAP_ADV_TYPE_ADV_NONCONN_IND](#gga07833ed1f79708d5f6a5d0c2e01d4dcaabb587b376bd6511881d6b70ceaa2af56)、[BT_GAP_ADV_TYPE_SCAN_RSP](#gga07833ed1f79708d5f6a5d0c2e01d4dcaa5387de0177d3a9da9fd0c44ca30c7018)、[BT_GAP_ADV_TYPE_EXT_ADV](#gga07833ed1f79708d5f6a5d0c2e01d4dcaa09292ffe2f0b76b8761fcaad6fbf9ba8)。

广播协议数据单元类型（Advertising PDU Types）。

<a id="r_ga8ac9dd875bc7480929b5166193c621d0"></a>

```c
enum bt_gap_adv_prop { BT_GAP_ADV_PROP_CONNECTABLE = (1UL << (0)) , BT_GAP_ADV_PROP_SCANNABLE = (1UL << (1)) , BT_GAP_ADV_PROP_DIRECTED = (1UL << (2)) , BT_GAP_ADV_PROP_SCAN_RESPONSE = (1UL << (3)) , BT_GAP_ADV_PROP_EXT_ADV = (1UL << (4)) }
```

相关声明：[bt_gap_adv_prop](#ga8ac9dd875bc7480929b5166193c621d0)、[BT_GAP_ADV_PROP_CONNECTABLE](#gga8ac9dd875bc7480929b5166193c621d0af843db0752f3360ccb1a02c456ca9e5e)、[BT_GAP_ADV_PROP_SCANNABLE](#gga8ac9dd875bc7480929b5166193c621d0a6c5ea1b8392783568b568c74f9f17571)、[BT_GAP_ADV_PROP_DIRECTED](#gga8ac9dd875bc7480929b5166193c621d0a4595d3a3ea30bd4cd51ba4f1c4ab7de9)、[BT_GAP_ADV_PROP_SCAN_RESPONSE](#gga8ac9dd875bc7480929b5166193c621d0a55258ac9a7b355db87aeec5d443718f7)、[BT_GAP_ADV_PROP_EXT_ADV](#gga8ac9dd875bc7480929b5166193c621d0aeda2301e9eb191e742375e54bb765684)。

广播协议数据单元属性（Advertising PDU Properties）。

<a id="r_gab7418dd67b5c7fb9b0f9cfd5a55fe272"></a>

```c
enum bt_gap_cte { BT_GAP_CTE_AOA = 0x00 , BT_GAP_CTE_AOD_1US = 0x01 , BT_GAP_CTE_AOD_2US = 0x02 , BT_GAP_CTE_NONE = 0xFF }
```

相关声明：[bt_gap_cte](#gab7418dd67b5c7fb9b0f9cfd5a55fe272)、[BT_GAP_CTE_AOA](#ggab7418dd67b5c7fb9b0f9cfd5a55fe272a8a82746ee64ffbcc62e79fdd8e0e30a0)、[BT_GAP_CTE_AOD_1US](#ggab7418dd67b5c7fb9b0f9cfd5a55fe272aa8587383f9ea245e8c279fdd63417a19)、[BT_GAP_CTE_AOD_2US](#ggab7418dd67b5c7fb9b0f9cfd5a55fe272a2385af24a5a82f4d799674443b92e966)、[BT_GAP_CTE_NONE](#ggab7418dd67b5c7fb9b0f9cfd5a55fe272aec9324d8e0997e1ace59895e168087e8)。

恒定音调扩展类型（Constant Tone Extension Types，CTE Types）。

<a id="r_ga3cd6d431193b05414020ca5686f4c0e4"></a>

```c
enum bt_gap_sca { BT_GAP_SCA_UNKNOWN = 0 , BT_GAP_SCA_251_500 = 0 , BT_GAP_SCA_151_250 = 1 , BT_GAP_SCA_101_150 = 2 , BT_GAP_SCA_76_100 = 3 , BT_GAP_SCA_51_75 = 4 , BT_GAP_SCA_31_50 = 5 , BT_GAP_SCA_21_30 = 6 , BT_GAP_SCA_0_20 = 7 }
```

相关声明：[bt_gap_sca](#ga3cd6d431193b05414020ca5686f4c0e4)、[BT_GAP_SCA_UNKNOWN](#gga3cd6d431193b05414020ca5686f4c0e4ace5a2d3f9fcb1a8913203ee6f437b910)、[BT_GAP_SCA_251_500](#gga3cd6d431193b05414020ca5686f4c0e4a96900858c146259fc41af27b4cb62247)、[BT_GAP_SCA_151_250](#gga3cd6d431193b05414020ca5686f4c0e4ab19b506bc13aad6af3dba925153f4e7d)、[BT_GAP_SCA_101_150](#gga3cd6d431193b05414020ca5686f4c0e4a7f41d38c1a2125bd7c4d1765c8fbee73)、[BT_GAP_SCA_76_100](#gga3cd6d431193b05414020ca5686f4c0e4aa4011892d3409238f668c87626587bfd)、[BT_GAP_SCA_51_75](#gga3cd6d431193b05414020ca5686f4c0e4a999a15d6ed8c860af7323af1b4d86fe9)、[BT_GAP_SCA_31_50](#gga3cd6d431193b05414020ca5686f4c0e4a5fa53f708753d67bd6ec4f54b164b005)、[BT_GAP_SCA_21_30](#gga3cd6d431193b05414020ca5686f4c0e4a164fe8b7df50d8e393373153a1f70d1d)、[BT_GAP_SCA_0_20](#gga3cd6d431193b05414020ca5686f4c0e4ab8fd607ccdc30216fd90d4c6f568b9f6)。

外设睡眠时钟精度（Sleep Clock Accuracy，SCA），单位为百万分之一（Parts per Million，ppm）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 2.3\_公司标识符（Company Identifiers，参见 Bluetooth Assigned Numbers）

<a id="r_ga6bbf21c05f24d2c2c710be9bcf05af5f"></a>

```c
#define BT_COMP_ID_LF 0x05f1
```

相关声明：[BT_COMP_ID_LF](#ga6bbf21c05f24d2c2c710be9bcf05af5f)。

Linux 基金会（The Linux Foundation）。

## 2.4\_已定义的通用访问配置文件定时器（Defined GAP Timers）

依据《蓝牙核心规范》（Bluetooth Core Specification）6.2，第 3 卷 C 部分附录 A。

<a id="r_gae9356673ee78d9abb27891738344513a"></a>

```c
#define BT_GAP_SCAN_FAST_INTERVAL_MIN 0x0030
```

相关声明：[BT_GAP_SCAN_FAST_INTERVAL_MIN](#gae9356673ee78d9abb27891738344513a)。

建议的快速扫描最小扫描间隔（Minimum Scan Interval）。

<a id="r_ga747caa714962215453a966a323e77cf8"></a>

```c
#define BT_GAP_SCAN_FAST_INTERVAL 0x0060
```

相关声明：[BT_GAP_SCAN_FAST_INTERVAL](#ga747caa714962215453a966a323e77cf8)。

建议的快速扫描最大扫描间隔（Maximum Scan Interval）。

<a id="r_ga100e1c20813630848a1a80390e8a06a0"></a>

```c
#define BT_GAP_SCAN_FAST_WINDOW 0x0030
```

相关声明：[BT_GAP_SCAN_FAST_WINDOW](#ga100e1c20813630848a1a80390e8a06a0)。

建议的快速扫描窗口（Scan Window）。

<a id="r_ga1acb5143221e9f94af4d5dc3a9eab125"></a>

```c
#define BT_GAP_SCAN_SLOW_INTERVAL_1 0x0800
```

相关声明：[BT_GAP_SCAN_SLOW_INTERVAL_1](#ga1acb5143221e9f94af4d5dc3a9eab125)。

建议的慢速扫描间隔（Scan Interval，模式 1）。

<a id="r_ga29a1a15bfbe035f439c48d1db96db392"></a>

```c
#define BT_GAP_SCAN_SLOW_WINDOW_1 0x0012
```

相关声明：[BT_GAP_SCAN_SLOW_WINDOW_1](#ga29a1a15bfbe035f439c48d1db96db392)。

建议的慢速扫描窗口（Scan Window，模式 1）。

<a id="r_ga38455c10880fddac0a1b4303a642e44d"></a>

```c
#define BT_GAP_SCAN_SLOW_INTERVAL_2 0x1000
```

相关声明：[BT_GAP_SCAN_SLOW_INTERVAL_2](#ga38455c10880fddac0a1b4303a642e44d)。

建议的慢速扫描间隔（Scan Interval，模式 2）。

<a id="r_gaa809fd8143c2805768874195ac24936f"></a>

```c
#define BT_GAP_SCAN_SLOW_WINDOW_2 0x0012
```

相关声明：[BT_GAP_SCAN_SLOW_WINDOW_2](#gaa809fd8143c2805768874195ac24936f)。

建议的慢速扫描窗口（Scan Window，模式 2）。

<a id="r_ga397a52fe616416665b46a2bc454c2e11"></a>

```c
#define BT_GAP_ADV_FAST_INT_MIN_1 0x0030
```

相关声明：[BT_GAP_ADV_FAST_INT_MIN_1](#ga397a52fe616416665b46a2bc454c2e11)。

建议的快速广播最小广播间隔（Minimum Advertising Interval，模式 1）。

<a id="r_ga13acf16d3d8edd39636bb10df752775a"></a>

```c
#define BT_GAP_ADV_FAST_INT_MAX_1 0x0060
```

相关声明：[BT_GAP_ADV_FAST_INT_MAX_1](#ga13acf16d3d8edd39636bb10df752775a)。

建议的快速广播最大广播间隔（Maximum Advertising Interval，模式 1）。

<a id="r_ga9573e6bcdae3aae9d51c0becbbd7ac60"></a>

```c
#define BT_GAP_ADV_FAST_INT_MIN_2 0x00a0
```

相关声明：[BT_GAP_ADV_FAST_INT_MIN_2](#ga9573e6bcdae3aae9d51c0becbbd7ac60)。

建议的快速广播最小广播间隔（Minimum Advertising Interval，模式 2）。

<a id="r_gaebc3ce60836522d883f664227a3ffcfb"></a>

```c
#define BT_GAP_ADV_FAST_INT_MAX_2 0x00f0
```

相关声明：[BT_GAP_ADV_FAST_INT_MAX_2](#gaebc3ce60836522d883f664227a3ffcfb)。

建议的快速广播最大广播间隔（Maximum Advertising Interval，模式 2）。

<a id="r_ga647f70c07c15f11287b735cbaad2a326"></a>

```c
#define BT_GAP_ADV_SLOW_INT_MIN 0x0640
```

相关声明：[BT_GAP_ADV_SLOW_INT_MIN](#ga647f70c07c15f11287b735cbaad2a326)。

建议的慢速广播最小广播间隔（Minimum Advertising Interval）。

<a id="r_gadecbfb823bbb6ffdd48be02df2f05f87"></a>

```c
#define BT_GAP_ADV_SLOW_INT_MAX 0x0780
```

相关声明：[BT_GAP_ADV_SLOW_INT_MAX](#gadecbfb823bbb6ffdd48be02df2f05f87)。

建议的慢速广播最大广播间隔（Maximum Advertising Interval）。

<a id="r_gafd724ebc809044574283c5547beda824"></a>

```c
#define BT_GAP_PER_ADV_FAST_INT_MIN_1 0x0018
```

相关声明：[BT_GAP_PER_ADV_FAST_INT_MIN_1](#gafd724ebc809044574283c5547beda824)。

建议的快速广播最小周期广播间隔（Minimum Periodic Advertising Interval，模式 1）。

<a id="r_ga849315b0b724af6017b910e78db0cfae"></a>

```c
#define BT_GAP_PER_ADV_FAST_INT_MAX_1 0x0030
```

相关声明：[BT_GAP_PER_ADV_FAST_INT_MAX_1](#ga849315b0b724af6017b910e78db0cfae)。

建议的快速广播最大周期广播间隔（Maximum Periodic Advertising Interval，模式 1）。

<a id="r_ga61eb4d6d65f1dd9c475a6f2f44b27957"></a>

```c
#define BT_GAP_PER_ADV_FAST_INT_MIN_2 0x0050
```

相关声明：[BT_GAP_PER_ADV_FAST_INT_MIN_2](#ga61eb4d6d65f1dd9c475a6f2f44b27957)。

建议的快速广播最小周期广播间隔（Minimum Periodic Advertising Interval，模式 2）。

<a id="r_ga264134294d8378d6e7d2bc52d4e0af1c"></a>

```c
#define BT_GAP_PER_ADV_FAST_INT_MAX_2 0x0078
```

相关声明：[BT_GAP_PER_ADV_FAST_INT_MAX_2](#ga264134294d8378d6e7d2bc52d4e0af1c)。

建议的快速广播最大周期广播间隔（Maximum Periodic Advertising Interval，模式 2）。

<a id="r_gab51898ce46ee9ae468ed7ffc1d117321"></a>

```c
#define BT_GAP_PER_ADV_SLOW_INT_MIN 0x0320
```

相关声明：[BT_GAP_PER_ADV_SLOW_INT_MIN](#gab51898ce46ee9ae468ed7ffc1d117321)。

建议的慢速广播最小周期广播间隔（Minimum Periodic Advertising Interval）。

<a id="r_gaa618da2a7c217527b0d962315caa1c22"></a>

```c
#define BT_GAP_PER_ADV_SLOW_INT_MAX 0x03C0
```

相关声明：[BT_GAP_PER_ADV_SLOW_INT_MAX](#gaa618da2a7c217527b0d962315caa1c22)。

建议的慢速广播最大周期广播间隔（Maximum Periodic Advertising Interval）。

<a id="r_gadaa7f1547c4ea22936087c181d82a552"></a>

```c
#define BT_GAP_INIT_CONN_INT_MIN 0x0018
```

相关声明：[BT_GAP_INIT_CONN_INT_MIN](#gadaa7f1547c4ea22936087c181d82a552)。

建议的最小初始连接间隔（Minimum Initial Connection Interval）。

<a id="r_ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1"></a>

```c
#define BT_GAP_INIT_CONN_INT_MAX 0x0028
```

相关声明：[BT_GAP_INIT_CONN_INT_MAX](#ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1)。

建议的最大初始连接间隔（Maximum Initial Connection Interval）。

## 2.5\_详细说明（Detailed Documentation）

<a id="ga6bbf21c05f24d2c2c710be9bcf05af5f"></a>

### `BT_COMP_ID_LF`

```c
#define BT_COMP_ID_LF 0x05f1
```

```c
#include <zephyr/bluetooth/gap.h>
```

Linux 基金会（The Linux Foundation）。

<a id="ga13acf16d3d8edd39636bb10df752775a"></a>

### `BT_GAP_ADV_FAST_INT_MAX_1`

```c
#define BT_GAP_ADV_FAST_INT_MAX_1 0x0060
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的快速广播最大广播间隔（Maximum Advertising Interval，模式 1）。

60 毫秒（ms）。

<a id="gaebc3ce60836522d883f664227a3ffcfb"></a>

### `BT_GAP_ADV_FAST_INT_MAX_2`

```c
#define BT_GAP_ADV_FAST_INT_MAX_2 0x00f0
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的快速广播最大广播间隔（Maximum Advertising Interval，模式 2）。

150 毫秒（ms）。

<a id="ga397a52fe616416665b46a2bc454c2e11"></a>

### `BT_GAP_ADV_FAST_INT_MIN_1`

```c
#define BT_GAP_ADV_FAST_INT_MIN_1 0x0030
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的快速广播最小广播间隔（Minimum Advertising Interval，模式 1）。

30 ms

<a id="ga9573e6bcdae3aae9d51c0becbbd7ac60"></a>

### `BT_GAP_ADV_FAST_INT_MIN_2`

```c
#define BT_GAP_ADV_FAST_INT_MIN_2 0x00a0
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的快速广播最小广播间隔（Minimum Advertising Interval，模式 2）。

100 毫秒（ms）。

<a id="gabe483d4dd601b11ac3eea570c962b1ec"></a>

### `BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT`

```c
#define BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT 128
```

```c
#include <zephyr/bluetooth/gap.h>
```

<a id="ga7261e64328e433d333d88d3a4cad21de"></a>

### `BT_GAP_ADV_INTERVAL_TO_MS`

```c
#define BT_GAP_ADV_INTERVAL_TO_MS ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(BT_GAP_ADV_INTERVAL_TO_US(_interval) / USEC_PER_MSEC)
```

将广播间隔（Advertising Interval，`N * 0.625 ms`）转换为毫秒。

`_interval` 的取值范围（Value Range）为 BT_LE_ADV_INTERVAL_MIN 到 BT_LE_ADV_INTERVAL_MAX。

**说明（Note）**：注意：间隔无法用整数毫秒表示时，会向下舍入（Round Down）。例如，`BT_GAP_ADV_INTERVAL_TO_MS(0x0021)` 得到 20 ms，而非 20.625 ms。

<a id="ga6e10b5311c785ad7eea10743987c0f27"></a>

### `BT_GAP_ADV_INTERVAL_TO_US`

```c
#define BT_GAP_ADV_INTERVAL_TO_US ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
((uint32_t)((_interval) * 625U))
```

将广播间隔（Advertising Interval，`N * 0.625 ms`）转换为微秒。

`_interval` 的取值范围（Value Range）为 BT_LE_ADV_INTERVAL_MIN 到 BT_LE_ADV_INTERVAL_MAX。

<a id="ga39ab5040c9471631486da7dbebd9c36f"></a>

### `BT_GAP_ADV_MAX_ADV_DATA_LEN`

```c
#define BT_GAP_ADV_MAX_ADV_DATA_LEN 31
```

```c
#include <zephyr/bluetooth/gap.h>
```

最大广播数据长度（Maximum advertising data length）。

<a id="ga53af114e4925482739dc50dc84c2f641"></a>

### `BT_GAP_ADV_MAX_EXT_ADV_DATA_LEN`

```c
#define BT_GAP_ADV_MAX_EXT_ADV_DATA_LEN 1650
```

```c
#include <zephyr/bluetooth/gap.h>
```

扩展广播数据（Extended Advertising Data）的最大长度。

**说明（Note）**：注意：扩展广播者（Extended Advertiser）能够发送的最大广播数据长度由控制器定义。

<a id="gadecbfb823bbb6ffdd48be02df2f05f87"></a>

### `BT_GAP_ADV_SLOW_INT_MAX`

```c
#define BT_GAP_ADV_SLOW_INT_MAX 0x0780
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的慢速广播最大广播间隔（Maximum Advertising Interval）。

1.2 秒（s）。

<a id="ga647f70c07c15f11287b735cbaad2a326"></a>

### `BT_GAP_ADV_SLOW_INT_MIN`

```c
#define BT_GAP_ADV_SLOW_INT_MIN 0x0640
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的慢速广播最小广播间隔（Minimum Advertising Interval）。

1 秒（s）。

<a id="ga90cfab7c375a8af6f9224a5635cbd023"></a>

### `BT_GAP_DATA_LEN_DEFAULT`

```c
#define BT_GAP_DATA_LEN_DEFAULT 0x001b /* 27 bytes */
```

```c
#include <zephyr/bluetooth/gap.h>
```

默认数据长度（Default Data Length）。

<a id="gacf5f35866d4677bd45c6e567886cabb9"></a>

### `BT_GAP_DATA_LEN_MAX`

```c
#define BT_GAP_DATA_LEN_MAX 0x00fb /* 251 bytes */
```

```c
#include <zephyr/bluetooth/gap.h>
```

最大数据长度（Maximum Data Length）。

<a id="ga245249c0b6f8ccc419f2132f76362908"></a>

### `BT_GAP_DATA_TIME_DEFAULT`

```c
#define BT_GAP_DATA_TIME_DEFAULT 0x0148 /* 328 us */
```

```c
#include <zephyr/bluetooth/gap.h>
```

默认数据时间（Default Data Time）。

<a id="ga379b5d8d7f243abbc584c288cd01815f"></a>

### `BT_GAP_DATA_TIME_MAX`

```c
#define BT_GAP_DATA_TIME_MAX 0x4290 /* 17040 us */
```

```c
#include <zephyr/bluetooth/gap.h>
```

最大数据时间（Maximum Data Time）。

<a id="ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1"></a>

### `BT_GAP_INIT_CONN_INT_MAX`

```c
#define BT_GAP_INIT_CONN_INT_MAX 0x0028
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的最大初始连接间隔（Maximum Initial Connection Interval）。

50 毫秒（ms）。

<a id="gadaa7f1547c4ea22936087c181d82a552"></a>

### `BT_GAP_INIT_CONN_INT_MIN`

```c
#define BT_GAP_INIT_CONN_INT_MIN 0x0018
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的最小初始连接间隔（Minimum Initial Connection Interval）。

30 ms

<a id="ga46c1e49ca3285ed9fc1b4ac593a25cd3"></a>

### `BT_GAP_ISO_INTERVAL_TO_MS`

```c
#define BT_GAP_ISO_INTERVAL_TO_MS ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(BT_GAP_ISO_INTERVAL_TO_US(_interval) / USEC_PER_MSEC)
```

将等时间隔（Isochronous Interval，`N * 1.25 ms`）转换为毫秒。

`_interval` 的取值范围（Value Range）为 BT_HCI_ISO_INTERVAL_MIN 到 BT_HCI_ISO_INTERVAL_MAX。

**说明（Note）**：注意：间隔无法用整数毫秒表示时，会向下舍入（Round Down）。例如，`BT_GAP_ISO_INTERVAL_TO_MS(0x0005)` 得到 6 ms，而非 6.25 ms。

<a id="ga4feca4664259c43121c2ff481d9ee611"></a>

### `BT_GAP_ISO_INTERVAL_TO_US`

```c
#define BT_GAP_ISO_INTERVAL_TO_US ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
((uint32_t)((_interval) * 1250U))
```

将等时间隔（Isochronous Interval，`N * 1.25 ms`）转换为微秒。

`_interval` 的取值范围（Value Range）为 BT_HCI_ISO_INTERVAL_MIN 到 BT_HCI_ISO_INTERVAL_MAX。

<a id="gaef9c34f229f1b8b06d3e6cd44a1014ef"></a>

### `BT_GAP_MS_TO_ADV_INTERVAL`

```c
#define BT_GAP_MS_TO_ADV_INTERVAL ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(BT_GAP_US_TO_ADV_INTERVAL((_interval) * USEC_PER_MSEC))
```

将毫秒转换为广播间隔（Advertising Interval）单位，每单位为 0.625 ms。

`_interval` 的取值范围（Value Range）为 20 到 1024。

**说明（Note）**：注意：`_interval` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_MS_TO_ADV_INTERVAL(21)` 得到 20.625 毫秒。

<a id="gaa3703cccd343dbb6418fdeb47a718eb5"></a>

### `BT_GAP_MS_TO_CONN_EVENT_LEN`

```c
#define BT_GAP_MS_TO_CONN_EVENT_LEN ( _event_len)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(BT_GAP_US_TO_CONN_EVENT_LEN((_event_len) * USEC_PER_MSEC))
```

将毫秒转换为连接事件长度（Connection Event Length）单位，原文给出的单位值为 0.625。

`_event_len` 的取值范围（Value Range）为 0 到 40959.375。

**说明（Note）**：注意：`_event_len` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_MS_TO_CONN_EVENT_LEN(21)` 得到 20.625 毫秒。

<a id="ga75985e2c444da7b2426cc746c9781c8c"></a>

### `BT_GAP_MS_TO_CONN_INTERVAL`

```c
#define BT_GAP_MS_TO_CONN_INTERVAL ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(BT_GAP_US_TO_CONN_INTERVAL((_interval) * USEC_PER_MSEC))
```

将毫秒转换为连接间隔（Connection Interval）单位，每单位为 1.25 ms。

`_interval` 的取值范围（Value Range）为 7.5 到 4000。

**说明（Note）**：注意：`_interval` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_MS_TO_CONN_INTERVAL(21)` 得到 20 毫秒。

<a id="ga24f79cacceeea262987f3cdaf2ef6bc3"></a>

### `BT_GAP_MS_TO_CONN_TIMEOUT`

```c
#define BT_GAP_MS_TO_CONN_TIMEOUT ( _timeout)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
((uint16_t)((_timeout) / 10U))
```

将毫秒转换为连接监督超时（Connection Supervision Timeout）单位，每单位为 10 ms。

`_timeout` 的取值范围（Value Range）为 100 到 32000。

**说明（Note）**：注意：`_timeout` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_MS_TO_CONN_TIMEOUT(4005)` 得到 4000 毫秒。

<a id="ga15ec0bc7c9bab797d6c5595269a33ea4"></a>

### `BT_GAP_MS_TO_PER_ADV_INTERVAL`

```c
#define BT_GAP_MS_TO_PER_ADV_INTERVAL ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(BT_GAP_US_TO_PER_ADV_INTERVAL((_interval) * USEC_PER_MSEC))
```

将毫秒转换为周期广播间隔（Periodic Advertising Interval）单位，每单位为 1.25 ms。

`_interval` 的取值范围（Value Range）为 7.5 到 81918.75。

**说明（Note）**：注意：`_interval` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_MS_TO_PER_ADV_INTERVAL(11)` 得到 10 毫秒。

<a id="ga242a6a4e3dd138073c01bc600c9642eb"></a>

### `BT_GAP_MS_TO_PER_ADV_SYNC_TIMEOUT`

```c
#define BT_GAP_MS_TO_PER_ADV_SYNC_TIMEOUT ( _timeout)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
((uint16_t)((_timeout) / 10U))
```

将毫秒转换为周期广播同步超时（Periodic Advertising Sync Timeout）单位，每单位为 10 ms。

`_timeout` 的取值范围（Value Range）为 100 到 163840。

**说明（Note）**：注意：`_timeout` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_MS_TO_PER_ADV_SYNC_TIMEOUT(4005)` 得到 4000 毫秒。

<a id="gad18c4a9774014081833905fc9e03fb15"></a>

### `BT_GAP_MS_TO_SCAN_INTERVAL`

```c
#define BT_GAP_MS_TO_SCAN_INTERVAL ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(BT_GAP_US_TO_SCAN_INTERVAL((_interval) * USEC_PER_MSEC))
```

将毫秒转换为扫描间隔（Scan Interval）单位，每单位为 0.625 ms。

启用 CONFIG_BT_EXT_ADV 时，_interval 的取值范围为 2.5 到 40959.375，否则为 2500 到 10240。（数值保留原文。）

**说明（Note）**：注意：`_interval` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_MS_TO_SCAN_INTERVAL(21)` 得到 20.625 毫秒。

<a id="ga5204f7e42b4e33eb8ae4ae71b82a4c88"></a>

### `BT_GAP_MS_TO_SCAN_WINDOW`

```c
#define BT_GAP_MS_TO_SCAN_WINDOW ( _window)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(BT_GAP_US_TO_SCAN_WINDOW((_window) * USEC_PER_MSEC))
```

将毫秒转换为扫描窗口（Scan Window）单位，每单位为 0.625 ms。

启用 CONFIG_BT_EXT_ADV 时，_window 的取值范围为 2.5 到 40959.375，否则为 2500 到 10240。（数值保留原文。）

**说明（Note）**：注意：`_window` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_MS_TO_SCAN_WINDOW(21)` 得到 20.625 毫秒。

<a id="ga9d6b2af6b96eab6356ded93c54301ef6"></a>

### `BT_GAP_NO_TIMEOUT`

```c
#define BT_GAP_NO_TIMEOUT 0x0000
```

```c
#include <zephyr/bluetooth/gap.h>
```

哨兵值（Sentinel Value），表示未设置超时（Timeout）。

<a id="ga849315b0b724af6017b910e78db0cfae"></a>

### `BT_GAP_PER_ADV_FAST_INT_MAX_1`

```c
#define BT_GAP_PER_ADV_FAST_INT_MAX_1 0x0030
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的快速广播最大周期广播间隔（Maximum Periodic Advertising Interval，模式 1）。

60 毫秒（ms）。

<a id="ga264134294d8378d6e7d2bc52d4e0af1c"></a>

### `BT_GAP_PER_ADV_FAST_INT_MAX_2`

```c
#define BT_GAP_PER_ADV_FAST_INT_MAX_2 0x0078
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的快速广播最大周期广播间隔（Maximum Periodic Advertising Interval，模式 2）。

150 毫秒（ms）。

<a id="gafd724ebc809044574283c5547beda824"></a>

### `BT_GAP_PER_ADV_FAST_INT_MIN_1`

```c
#define BT_GAP_PER_ADV_FAST_INT_MIN_1 0x0018
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的快速广播最小周期广播间隔（Minimum Periodic Advertising Interval，模式 1）。

30 ms

<a id="ga61eb4d6d65f1dd9c475a6f2f44b27957"></a>

### `BT_GAP_PER_ADV_FAST_INT_MIN_2`

```c
#define BT_GAP_PER_ADV_FAST_INT_MIN_2 0x0050
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的快速广播最小周期广播间隔（Minimum Periodic Advertising Interval，模式 2）。

100 毫秒（ms）。

<a id="gac240015012694df3557679d99da6c1a9"></a>

### `BT_GAP_PER_ADV_INTERVAL_TO_MS`

```c
#define BT_GAP_PER_ADV_INTERVAL_TO_MS ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(BT_GAP_PER_ADV_INTERVAL_TO_US(_interval) / USEC_PER_MSEC)
```

将周期广播间隔（Periodic Advertising Interval，`N * 1.25 ms`）转换为毫秒。

**说明（Note）**：注意：间隔无法用整数毫秒表示时，会向下舍入（Round Down）。例如，`BT_GAP_PER_ADV_INTERVAL_TO_MS(0x0009)` 得到 11 ms，而非 11.25 ms。

<a id="ga63587ef565ccde477b9c6f03faf778a5"></a>

### `BT_GAP_PER_ADV_INTERVAL_TO_US`

```c
#define BT_GAP_PER_ADV_INTERVAL_TO_US ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
((uint32_t)((_interval) * 1250U))
```

将周期广播间隔（Periodic Advertising Interval，`N * 1.25 ms`）转换为微秒（原文末尾有一个 `*`）。

`_interval` 的取值范围（Value Range）为 BT_HCI_LE_PER_ADV_INTERVAL_MIN 到 BT_HCI_LE_PER_ADV_INTERVAL_MAX。

<a id="ga80bf3f1fb6f34a2c4363687149c365bd"></a>

### `BT_GAP_PER_ADV_MAX_INTERVAL`

```c
#define BT_GAP_PER_ADV_MAX_INTERVAL 0xFFFF /* 81.91875 s */
```

```c
#include <zephyr/bluetooth/gap.h>
```

最大周期广播间隔（Maximum Periodic Advertising Interval），为 N × 1.25 毫秒。

<a id="gaf92b229c47309a7a5e99047f28b860e7"></a>

### `BT_GAP_PER_ADV_MAX_SKIP`

```c
#define BT_GAP_PER_ADV_MAX_SKIP 0x01F3
```

```c
#include <zephyr/bluetooth/gap.h>
```

成功接收后可跳过的连续周期广播事件（Periodic Advertisement Events）的最大数量。

<a id="gad6674199f615fa6ecaeb1fe9d099e04c"></a>

### `BT_GAP_PER_ADV_MAX_TIMEOUT`

```c
#define BT_GAP_PER_ADV_MAX_TIMEOUT 0x4000 /* 163.84 s */
```

```c
#include <zephyr/bluetooth/gap.h>
```

最大周期广播超时（Periodic Advertising Timeout），单位为 `N * 10 ms`。

<a id="ga07e21fdeb8a0a0b967690898bef2f7aa"></a>

### `BT_GAP_PER_ADV_MIN_INTERVAL`

```c
#define BT_GAP_PER_ADV_MIN_INTERVAL 0x0006 /* 7.5 ms */
```

```c
#include <zephyr/bluetooth/gap.h>
```

最小周期广播间隔（Minimum Periodic Advertising Interval），为 N × 1.25 毫秒。

<a id="ga17d8ae7e98f6a1dfead4f8ecb75f9645"></a>

### `BT_GAP_PER_ADV_MIN_TIMEOUT`

```c
#define BT_GAP_PER_ADV_MIN_TIMEOUT 0x000A /* 100 ms */
```

```c
#include <zephyr/bluetooth/gap.h>
```

最小周期广播超时（Periodic Advertising Timeout），单位为 `N * 10 ms`。

<a id="gaa618da2a7c217527b0d962315caa1c22"></a>

### `BT_GAP_PER_ADV_SLOW_INT_MAX`

```c
#define BT_GAP_PER_ADV_SLOW_INT_MAX 0x03C0
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的慢速广播最大周期广播间隔（Maximum Periodic Advertising Interval）。

1.2 秒（s）。

<a id="gab51898ce46ee9ae468ed7ffc1d117321"></a>

### `BT_GAP_PER_ADV_SLOW_INT_MIN`

```c
#define BT_GAP_PER_ADV_SLOW_INT_MIN 0x0320
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的慢速广播最小周期广播间隔（Minimum Periodic Advertising Interval）。

1 秒（s）。

<a id="ga64b5c5e429dadf1e875984f69cd399dc"></a>

### `BT_GAP_RSSI_INVALID`

```c
#define BT_GAP_RSSI_INVALID 0x7f
```

```c
#include <zephyr/bluetooth/gap.h>
```

哨兵值（Sentinel Value），表示以 dBm 为单位的接收信号强度指示（RSSI）不可用或未知。

<a id="ga747caa714962215453a966a323e77cf8"></a>

### `BT_GAP_SCAN_FAST_INTERVAL`

```c
#define BT_GAP_SCAN_FAST_INTERVAL 0x0060
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的快速扫描最大扫描间隔（Maximum Scan Interval）。

60 毫秒（ms）。

<a id="gae9356673ee78d9abb27891738344513a"></a>

### `BT_GAP_SCAN_FAST_INTERVAL_MIN`

```c
#define BT_GAP_SCAN_FAST_INTERVAL_MIN 0x0030
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的快速扫描最小扫描间隔（Minimum Scan Interval）。

30 ms

<a id="ga100e1c20813630848a1a80390e8a06a0"></a>

### `BT_GAP_SCAN_FAST_WINDOW`

```c
#define BT_GAP_SCAN_FAST_WINDOW 0x0030
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的快速扫描窗口（Scan Window）。

30 ms

<a id="ga1acb5143221e9f94af4d5dc3a9eab125"></a>

### `BT_GAP_SCAN_SLOW_INTERVAL_1`

```c
#define BT_GAP_SCAN_SLOW_INTERVAL_1 0x0800
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的慢速扫描间隔（Scan Interval，模式 1）。

1.28 秒（s）。

<a id="ga38455c10880fddac0a1b4303a642e44d"></a>

### `BT_GAP_SCAN_SLOW_INTERVAL_2`

```c
#define BT_GAP_SCAN_SLOW_INTERVAL_2 0x1000
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的慢速扫描间隔（Scan Interval，模式 2）。

2.56 秒（s）。

<a id="ga29a1a15bfbe035f439c48d1db96db392"></a>

### `BT_GAP_SCAN_SLOW_WINDOW_1`

```c
#define BT_GAP_SCAN_SLOW_WINDOW_1 0x0012
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的慢速扫描窗口（Scan Window，模式 1）。

11.25 毫秒（ms）。

<a id="gaa809fd8143c2805768874195ac24936f"></a>

### `BT_GAP_SCAN_SLOW_WINDOW_2`

```c
#define BT_GAP_SCAN_SLOW_WINDOW_2 0x0012
```

```c
#include <zephyr/bluetooth/gap.h>
```

建议的慢速扫描窗口（Scan Window，模式 2）。

11.25 毫秒（ms）。

<a id="ga103af3e3142473be8897cd2647dca915"></a>

### `BT_GAP_SID_INVALID`

```c
#define BT_GAP_SID_INVALID 0xff
```

```c
#include <zephyr/bluetooth/gap.h>
```

哨兵值（Sentinel Value），表示广播集标识符（Advertising Set Identifier）无效或未知。

<a id="gafa6f803fe3ada07030fb1f2f725940c4"></a>

### `BT_GAP_SID_MAX`

```c
#define BT_GAP_SID_MAX 0x0F
```

```c
#include <zephyr/bluetooth/gap.h>
```

最大广播集数量（Maximum Advertising Set Number）。

<a id="gacf05b7660d2ae85f64e2a220abf8e57d"></a>

### `BT_GAP_SID_MIN`

```c
#define BT_GAP_SID_MIN 0x00
```

```c
#include <zephyr/bluetooth/gap.h>
```

最小广播集数量（Minimum Advertising Set Number）。

<a id="ga61ccce819d75313cb2ee58309ed4b275"></a>

### `BT_GAP_TX_POWER_INVALID`

```c
#define BT_GAP_TX_POWER_INVALID 0x7f
```

```c
#include <zephyr/bluetooth/gap.h>
```

哨兵值（Sentinel Value），表示以 dBm 为单位的发射功率（TX Power）不可用或未知。

<a id="gac79626389f62bb7b3e5b5f6d3a5eaf2b"></a>

### `BT_GAP_US_TO_ADV_INTERVAL`

```c
#define BT_GAP_US_TO_ADV_INTERVAL ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
((uint16_t)((_interval) / 625U))
```

将微秒转换为广播间隔（Advertising Interval）单位，每单位为 0.625 ms。

`_interval` 的取值范围（Value Range）为 20000 到 1024000。

**说明（Note）**：注意：`_interval` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_US_TO_ADV_INTERVAL(21000)` 得到 20625 微秒。

<a id="ga8905e22b1864021b77367c228b8bff48"></a>

### `BT_GAP_US_TO_CONN_EVENT_LEN`

```c
#define BT_GAP_US_TO_CONN_EVENT_LEN ( _event_len)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
((uint16_t)((_event_len) / 625U))
```

将毫秒转换为连接事件长度（Connection Event Length）单位，原文给出的单位值为 0.625。

`_event_len` 的取值范围（Value Range）为 0 到 40959375。

**说明（Note）**：注意：`_event_len` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_US_TO_CONN_EVENT_LEN(21000)` 得到 20625 毫秒。（原文使用 milliseconds；该宏名称为微秒转换，单位疑点予以保留。）

<a id="gab12ba919a5a389b4c342d142d3a9ce6e"></a>

### `BT_GAP_US_TO_CONN_INTERVAL`

```c
#define BT_GAP_US_TO_CONN_INTERVAL ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
((uint16_t)((_interval) / 1250U))
```

将微秒转换为连接间隔（Connection Interval）单位，每单位为 1.25 ms。

`_interval` 的取值范围（Value Range）为 7500 到 4000000。

**说明（Note）**：注意：`_interval` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_US_TO_CONN_INTERVAL(21000)` 得到 20000 微秒。

<a id="ga317a60f9edb371fef180130282805539"></a>

### `BT_GAP_US_TO_CONN_TIMEOUT`

```c
#define BT_GAP_US_TO_CONN_TIMEOUT ( _timeout)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(BT_GAP_MS_TO_CONN_TIMEOUT((_timeout) / USEC_PER_MSEC))
```

将微秒转换为连接监督超时（Connection Supervision Timeout）单位，每单位为 10 ms。

`_timeout` 的取值范围（Value Range）为 100000 到 32000000。

**说明（Note）**：注意：`_timeout` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_MS_TO_CONN_TIMEOUT(4005000)` 得到 4000000 微秒。（原文在微秒示例中使用 BT_GAP_MS_TO_CONN_TIMEOUT，宏名称疑点予以保留。）

<a id="ga5a9da01507b4356c2ad6f8309257f2ce"></a>

### `BT_GAP_US_TO_PER_ADV_INTERVAL`

```c
#define BT_GAP_US_TO_PER_ADV_INTERVAL ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
((uint16_t)((_interval) / 1250U))
```

将微秒转换为周期广播间隔（Periodic Advertising Interval）单位，每单位为 1.25 ms。

`_interval` 的取值范围（Value Range）为 7500 到 81918750。

**说明（Note）**：注意：`_interval` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_US_TO_PER_ADV_INTERVAL(11000)` 得到 10000 微秒。

<a id="gaf33284a372b21e24c53deb5e3a6a91aa"></a>

### `BT_GAP_US_TO_PER_ADV_SYNC_TIMEOUT`

```c
#define BT_GAP_US_TO_PER_ADV_SYNC_TIMEOUT ( _timeout)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(BT_GAP_MS_TO_PER_ADV_SYNC_TIMEOUT((_timeout) / USEC_PER_MSEC))
```

将微秒转换为周期广播同步超时（Periodic Advertising Sync Timeout）单位，每单位为 10 ms。

`_timeout` 的取值范围（Value Range）为 100000 到 163840000。

**说明（Note）**：注意：`_timeout` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_US_TO_PER_ADV_SYNC_TIMEOUT(4005000)` 得到 4000000 微秒。

<a id="gab65e489c4a799774f6511c6ce5b65ea2"></a>

### `BT_GAP_US_TO_SCAN_INTERVAL`

```c
#define BT_GAP_US_TO_SCAN_INTERVAL ( _interval)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
((uint16_t)((_interval) / 625U))
```

将微秒转换为扫描间隔（Scan Interval）单位，每单位为 0.625 ms。

启用 CONFIG_BT_EXT_ADV 时，_interval 的取值范围为 2500 到 40959375，否则为 2500 到 10240000。

**说明（Note）**：注意：`_interval` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_US_TO_SCAN_INTERVAL(21000)` 得到 20625 微秒。

<a id="gaac5d0ec82d9730b793960c0470ac6342"></a>

### `BT_GAP_US_TO_SCAN_WINDOW`

```c
#define BT_GAP_US_TO_SCAN_WINDOW ( _window)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
((uint16_t)((_window) / 625U))
```

将微秒转换为扫描窗口（Scan Window）单位，每单位为 0.625 ms。

启用 CONFIG_BT_EXT_ADV 时，_window 的取值范围为 2500 到 40959375，否则为 2500 到 10240000。

**说明（Note）**：注意：`_window` 不是单位的整数倍时，将向下舍入（Round Down）至最近可表示值。例如，`BT_GAP_US_TO_SCAN_WINDOW(21000)` 得到 20625 微秒。

<a id="ga3c29ad99d6a6e020148590381ab08b17"></a>

### `BT_LE_SUPP_FEAT_16_ENCODE`

```c
#define BT_LE_SUPP_FEAT_16_ENCODE ( w64)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
BT_BYTES_LIST_LE16(w64)
```

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 2 字节，以小端序（Little-Endian）编码为长度为 2 字节的数组。

将 64 位低功耗蓝牙支持特性（LE Supported Features）值编码到广播数据的辅助宏。该宏编码最低的 3 个字节，其他 6 个字节不编码。（原文的 3 与 6 合计超过 64 位对应的 8 字节，此处保留该数量疑点。）

将 0x000000DFF00DF00D 编码到广播数据（Advertising Data）的示例。

原始示例（Example）：

```c
BT_DATA_BYTES(BT_DATA_LE_SUPPORTED_FEATURES, BT_LE_SUPP_FEAT_16_ENCODE(0x000000DFF00DF00D))
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `w64` | 低功耗蓝牙支持特性（LE Supported Features）值，64 位。 |

**返回（Returns）**：返回：表示 LE Supported Features 值的逗号分隔值（Comma Separated Values），可直接用作 BT_DATA_BYTES 的参数。

<a id="gab8739c92f8d50b796539a21027c3b6eb"></a>

### `BT_LE_SUPP_FEAT_24_ENCODE`

```c
#define BT_LE_SUPP_FEAT_24_ENCODE ( w64)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
BT_BYTES_LIST_LE24(w64)
```

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 3 字节，以小端序（Little-Endian）编码为长度为 3 字节的数组。

将 64 位低功耗蓝牙支持特性（LE Supported Features）值编码到广播数据的辅助宏。该宏编码最低的 3 个字节，其他 5 个字节不编码。

将 0x000000DFF00DF00D 编码到广播数据（Advertising Data）的示例。

原始示例（Example）：

```c
BT_DATA_BYTES(BT_DATA_LE_SUPPORTED_FEATURES, BT_LE_SUPP_FEAT_24_ENCODE(0x000000DFF00DF00D))
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `w64` | 低功耗蓝牙支持特性（LE Supported Features）值，64 位。 |

**返回（Returns）**：返回：表示 LE Supported Features 值的逗号分隔值（Comma Separated Values），可直接用作 BT_DATA_BYTES 的参数。

<a id="ga7aa92098e33840ff02cb8c0435637094"></a>

### `BT_LE_SUPP_FEAT_32_ENCODE`

```c
#define BT_LE_SUPP_FEAT_32_ENCODE ( w64)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
BT_BYTES_LIST_LE32(w64)
```

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 4 字节，以小端序（Little-Endian）编码为长度为 4 字节的数组。

将 64 位低功耗蓝牙支持特性（LE Supported Features）值编码到广播数据的辅助宏。该宏编码最低的 4 个字节，其他 4 个字节不编码。

将 0x000000DFF00DF00D 编码到广播数据（Advertising Data）的示例。

原始示例（Example）：

```c
BT_DATA_BYTES(BT_DATA_LE_SUPPORTED_FEATURES, BT_LE_SUPP_FEAT_32_ENCODE(0x000000DFF00DF00D))
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `w64` | 低功耗蓝牙支持特性（LE Supported Features）值，64 位。 |

**返回（Returns）**：返回：表示 LE Supported Features 值的逗号分隔值（Comma Separated Values），可直接用作 BT_DATA_BYTES 的参数。

<a id="ga799f6cb9dd02b9995ed76fbe97be3eb3"></a>

### `BT_LE_SUPP_FEAT_40_ENCODE`

```c
#define BT_LE_SUPP_FEAT_40_ENCODE ( w64)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
BT_BYTES_LIST_LE40(w64)
```

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 40 位，以小端序（Little-Endian）编码为数组值。

将 64 位低功耗蓝牙支持特性（LE Supported Features）值的低 40 位编码到广播数据的辅助宏。编码的位数对应《蓝牙 5.3 核心规范》（BT 5.3 Core Specification）定义的 LE 支持特性数量。

将 0x000000DFF00DF00D 编码到广播数据（Advertising Data）的示例。

原始示例（Example）：

```c
BT_DATA_BYTES(BT_DATA_LE_SUPPORTED_FEATURES, BT_LE_SUPP_FEAT_40_ENCODE(0x000000DFF00DF00D))
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `w64` | 低功耗蓝牙支持特性（LE Supported Features）值，64 位。 |

**返回（Returns）**：返回：表示 LE Supported Features 值的逗号分隔值（Comma Separated Values），可直接用作 BT_DATA_BYTES 的参数。

<a id="ga8fac302925ac3ef8982630e6a0ec13af"></a>

### `BT_LE_SUPP_FEAT_8_ENCODE`

```c
#define BT_LE_SUPP_FEAT_8_ENCODE ( w64)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
(((w64) >> 0) & 0xFF)
```

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低字节编码为长度为 1 字节的数组。

将 64 位低功耗蓝牙支持特性（LE Supported Features）值编码到广播数据的辅助宏。该宏只编码最低的 1 个字节，其他 7 个字节不编码。

将 0x000000DFF00DF00D 编码到广播数据（Advertising Data）的示例。

原始示例（Example）：

```c
BT_DATA_BYTES(BT_DATA_LE_SUPPORTED_FEATURES, BT_LE_SUPP_FEAT_8_ENCODE(0x000000DFF00DF00D))
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `w64` | 低功耗蓝牙支持特性（LE Supported Features）值，64 位。 |

**返回（Returns）**：返回：LE Supported Features 值的最低字节（Least Significant Byte），可直接用作 BT_DATA_BYTES 的参数。

<a id="ga86266eaf452dfaf82f097992e01397c8"></a>

### `BT_LE_SUPP_FEAT_VALIDATE`

```c
#define BT_LE_SUPP_FEAT_VALIDATE ( w64)
```

```c
#include <zephyr/bluetooth/gap.h>
```

展开值（Value）：

```c
BUILD_ASSERT(!((w64) & (~BIT64_MASK(40))), \
             "RFU bit in LE Supported Features are not zeros.")
```

验证低功耗蓝牙支持特性（LE Supported Features）值是否未使用为未来用途保留的位。

检查 w64 的第 40–63 位是否全为 0 的辅助宏。该宏遵循《蓝牙 5.3 核心规范》（BT 5.3 Core Specification），原文说明第 0–40 位已分配取值。值无效时报告构建时错误（Build Time Error）。（原文两处范围在位 40 重叠，此处保留其表述。）

<a id="ga8ac9dd875bc7480929b5166193c621d0"></a>

### `bt_gap_adv_prop`

```c
enum bt_gap_adv_prop
```

```c
#include <zephyr/bluetooth/gap.h>
```

广播协议数据单元属性（Advertising PDU Properties）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GAP_ADV_PROP_CONNECTABLE` | 可连接广播（Connectable Advertising）。 |
| `BT_GAP_ADV_PROP_SCANNABLE` | 可扫描广播（Scannable Advertising）。 |
| `BT_GAP_ADV_PROP_DIRECTED` | 定向广播（Directed Advertising）。 |
| `BT_GAP_ADV_PROP_SCAN_RESPONSE` | 主动扫描器（Active Scanner）请求的额外广播数据。 |
| `BT_GAP_ADV_PROP_EXT_ADV` | 扩展广播（Extended Advertising）。 |

<a id="ga07833ed1f79708d5f6a5d0c2e01d4dca"></a>

### `bt_gap_adv_type`

```c
enum bt_gap_adv_type
```

```c
#include <zephyr/bluetooth/gap.h>
```

广播协议数据单元类型（Advertising PDU Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GAP_ADV_TYPE_ADV_IND` | 可扫描且可连接的广播（Scannable and Connectable Advertising）。 |
| `BT_GAP_ADV_TYPE_ADV_DIRECT_IND` | 定向可连接广播（Directed Connectable Advertising）。 |
| `BT_GAP_ADV_TYPE_ADV_SCAN_IND` | 不可连接但可扫描的广播（Non-connectable and Scannable Advertising）。 |
| `BT_GAP_ADV_TYPE_ADV_NONCONN_IND` | 不可连接且不可扫描的广播（Non-connectable and Non-scannable Advertising）。 |
| `BT_GAP_ADV_TYPE_SCAN_RSP` | 主动扫描器（Active Scanner）请求的额外广播数据。 |
| `BT_GAP_ADV_TYPE_EXT_ADV` | 扩展广播（Extended Advertising），参见广播属性（Advertising Properties）。 |

<a id="gab7418dd67b5c7fb9b0f9cfd5a55fe272"></a>

### `bt_gap_cte`

```c
enum bt_gap_cte
```

```c
#include <zephyr/bluetooth/gap.h>
```

恒定音调扩展类型（Constant Tone Extension Types，CTE Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GAP_CTE_AOA` | 到达角（Angle of Arrival）。 |
| `BT_GAP_CTE_AOD_1US` | 使用 1 微秒时隙的出发角（Angle of Departure）。 |
| `BT_GAP_CTE_AOD_2US` | 使用 2 微秒时隙的出发角（Angle of Departure）。 |
| `BT_GAP_CTE_NONE` | 无扩展（No Extensions）。 |

<a id="ga691d9793fd21c41b2c192d65cc2bf6c4"></a>

### `bt_gap_le_phy`

```c
enum bt_gap_le_phy
```

```c
#include <zephyr/bluetooth/gap.h>
```

低功耗蓝牙物理层类型（LE PHY Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GAP_LE_PHY_NONE` | 未设置物理层（PHY）时使用的便捷宏。 |
| `BT_GAP_LE_PHY_1M` | LE 1M 物理层（LE 1M PHY）。 |
| `BT_GAP_LE_PHY_2M` | LE 2M 物理层（LE 2M PHY）。 |
| `BT_GAP_LE_PHY_CODED` | 低功耗蓝牙编码物理层（LE Coded PHY），未指定编码方案。 |
| `BT_GAP_LE_PHY_CODED_S8` | 低功耗蓝牙 S=8 编码物理层（LE Coded S=8 PHY）。仅在启用 Kconfig BT_EXT_ADV_CODING_SELECTION 时用于广播报告。 |
| `BT_GAP_LE_PHY_CODED_S2` | 低功耗蓝牙 S=2 编码物理层（LE Coded S=2 PHY）。仅在启用 Kconfig BT_EXT_ADV_CODING_SELECTION 时用于广播报告。 |

<a id="ga3cd6d431193b05414020ca5686f4c0e4"></a>

### `bt_gap_sca`

```c
enum bt_gap_sca
```

```c
#include <zephyr/bluetooth/gap.h>
```

外设睡眠时钟精度（Sleep Clock Accuracy，SCA），单位为百万分之一（Parts per Million，ppm）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GAP_SCA_UNKNOWN` | 未知（Unknown）。 |
| `BT_GAP_SCA_251_500` | 251 ppm 到 500 ppm，ppm 表示百万分之一（Parts Per Million）。 |
| `BT_GAP_SCA_151_250` | 151 ppm 到 250 ppm，ppm 表示百万分之一（Parts Per Million）。 |
| `BT_GAP_SCA_101_150` | 101 ppm 到 150 ppm，ppm 表示百万分之一（Parts Per Million）。 |
| `BT_GAP_SCA_76_100` | 76 ppm 到 100 ppm，ppm 表示百万分之一（Parts Per Million）。 |
| `BT_GAP_SCA_51_75` | 51 ppm 到 75 ppm，ppm 表示百万分之一（Parts Per Million）。 |
| `BT_GAP_SCA_31_50` | 31 ppm 到 50 ppm，ppm 表示百万分之一（Parts Per Million）。 |
| `BT_GAP_SCA_21_30` | 21 ppm 到 30 ppm，ppm 表示百万分之一（Parts Per Million）。 |
| `BT_GAP_SCA_0_20` | 0 ppm 到 20 ppm，ppm 表示百万分之一（Parts Per Million）。 |


## 2.6\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gap.h](../api_file_gap_modem_reference/P002_zephyr__bluetooth__gap.h_文件参考.md)
- [USEC_PER_MSEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga2d66311052e2bddf914610fb7345ff27)
- [BT_LE_ADV_INTERVAL_MIN](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#ac89392b0484164812b77360d15d9984b)
- [BT_LE_ADV_INTERVAL_MAX](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a6479fb2c964155cfcdd3cc48c3a45618)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [BT_HCI_ISO_INTERVAL_MIN](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a9d5e85ae1380fa85bae9d7e5e67aa0ae)
- [BT_HCI_ISO_INTERVAL_MAX](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#aaadbec2cc6adc2bb14d7117396023d06)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [CONFIG_BT_EXT_ADV](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_EXT_ADV)
- [BT_HCI_LE_PER_ADV_INTERVAL_MIN](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a04f870ac03c1baca22ab5d984354f3bf)
- [BT_HCI_LE_PER_ADV_INTERVAL_MAX](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a2f2216a88cf77ccac1c9a2f6c5820746)
- [BT_BYTES_LIST_LE16](../byteorder_reference/P003_蓝牙字节序辅助接口.md#ga83b5828023306b4bbf354ca3d6d6c6f2)
- [BT_DATA_BYTES](../api_file_display_management_reference/P005_zephyr__bluetooth__data.h_文件参考.md#a4c51f9b7a3a4e84abb4df3f1f714c6e2)
- [BT_DATA_LE_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga207bc1e5405a4fd3f39863a2cb304ebc)
- [BT_BYTES_LIST_LE24](../byteorder_reference/P003_蓝牙字节序辅助接口.md#ga68d63372c0b7e981d7ae715250c42261)
- [BT_BYTES_LIST_LE32](../byteorder_reference/P003_蓝牙字节序辅助接口.md#ga0bf0275f0eea70eb5ae6002edeb1b812)
- [BT_BYTES_LIST_LE40](../byteorder_reference/P003_蓝牙字节序辅助接口.md#gadd963cf0f7898e5e143b5d2fd79839ef)
- [BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__gap__defines_html_ga6e10b5311c785ad7eea10743987c0f27"></a>
<a id="agroup__clock__apis_html_ga2d66311052e2bddf914610fb7345ff27"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="agroup__bt__gap__defines_html_ga4feca4664259c43121c2ff481d9ee611"></a>
<a id="agroup__bt__gap__defines_html_gac79626389f62bb7b3e5b5f6d3a5eaf2b"></a>
<a id="agroup__bt__gap__defines_html_ga8905e22b1864021b77367c228b8bff48"></a>
<a id="agroup__bt__gap__defines_html_gab12ba919a5a389b4c342d142d3a9ce6e"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="agroup__bt__gap__defines_html_ga5a9da01507b4356c2ad6f8309257f2ce"></a>
<a id="agroup__bt__gap__defines_html_gab65e489c4a799774f6511c6ce5b65ea2"></a>
<a id="agroup__bt__gap__defines_html_gaac5d0ec82d9730b793960c0470ac6342"></a>
<a id="agroup__bt__gap__defines_html_ga63587ef565ccde477b9c6f03faf778a5"></a>
<a id="agroup__bt__gap__defines_html_ga24f79cacceeea262987f3cdaf2ef6bc3"></a>
<a id="agroup__bt__gap__defines_html_ga242a6a4e3dd138073c01bc600c9642eb"></a>
<a id="agroup__bt__byteorder_html_ga83b5828023306b4bbf354ca3d6d6c6f2"></a>
<a id="adata_8h_html_a4c51f9b7a3a4e84abb4df3f1f714c6e2"></a>
<a id="agroup__bt__assigned__numbers__core_html_ga207bc1e5405a4fd3f39863a2cb304ebc"></a>
<a id="agroup__bt__gap__defines_html_ga3c29ad99d6a6e020148590381ab08b17"></a>
<a id="agroup__bt__byteorder_html_ga68d63372c0b7e981d7ae715250c42261"></a>
<a id="agroup__bt__gap__defines_html_gab8739c92f8d50b796539a21027c3b6eb"></a>
<a id="agroup__bt__byteorder_html_ga0bf0275f0eea70eb5ae6002edeb1b812"></a>
<a id="agroup__bt__gap__defines_html_ga7aa92098e33840ff02cb8c0435637094"></a>
<a id="agroup__bt__byteorder_html_gadd963cf0f7898e5e143b5d2fd79839ef"></a>
<a id="agroup__bt__gap__defines_html_ga799f6cb9dd02b9995ed76fbe97be3eb3"></a>
<a id="agroup__bt__gap__defines_html_ga8fac302925ac3ef8982630e6a0ec13af"></a>
<a id="agroup__sys-util_html_ga1a138896caafcb2429a6483ea7412d12"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8ac9dd875bc7480929b5166193c621d0af843db0752f3360ccb1a02c456ca9e5e"></a>
<a id="gga8ac9dd875bc7480929b5166193c621d0a6c5ea1b8392783568b568c74f9f17571"></a>
<a id="gga8ac9dd875bc7480929b5166193c621d0a4595d3a3ea30bd4cd51ba4f1c4ab7de9"></a>
<a id="gga8ac9dd875bc7480929b5166193c621d0a55258ac9a7b355db87aeec5d443718f7"></a>
<a id="gga8ac9dd875bc7480929b5166193c621d0aeda2301e9eb191e742375e54bb765684"></a>
<a id="gga07833ed1f79708d5f6a5d0c2e01d4dcaaf4d48e46c1da164e876e4ded28470c82"></a>
<a id="gga07833ed1f79708d5f6a5d0c2e01d4dcaa05b182a44fea67f52015cbfb4d775be8"></a>
<a id="gga07833ed1f79708d5f6a5d0c2e01d4dcaae48316c135886d9f6d20f7bdba0858c1"></a>
<a id="gga07833ed1f79708d5f6a5d0c2e01d4dcaabb587b376bd6511881d6b70ceaa2af56"></a>
<a id="gga07833ed1f79708d5f6a5d0c2e01d4dcaa5387de0177d3a9da9fd0c44ca30c7018"></a>
<a id="gga07833ed1f79708d5f6a5d0c2e01d4dcaa09292ffe2f0b76b8761fcaad6fbf9ba8"></a>
<a id="ggab7418dd67b5c7fb9b0f9cfd5a55fe272a8a82746ee64ffbcc62e79fdd8e0e30a0"></a>
<a id="ggab7418dd67b5c7fb9b0f9cfd5a55fe272aa8587383f9ea245e8c279fdd63417a19"></a>
<a id="ggab7418dd67b5c7fb9b0f9cfd5a55fe272a2385af24a5a82f4d799674443b92e966"></a>
<a id="ggab7418dd67b5c7fb9b0f9cfd5a55fe272aec9324d8e0997e1ace59895e168087e8"></a>
<a id="gga691d9793fd21c41b2c192d65cc2bf6c4aaf7e1b40f6464a603e5116db269cacab"></a>
<a id="gga691d9793fd21c41b2c192d65cc2bf6c4a53eff400720a20fe1a91da4834bad752"></a>
<a id="gga691d9793fd21c41b2c192d65cc2bf6c4a662049cc8293959194bcb481e1dd50a8"></a>
<a id="gga691d9793fd21c41b2c192d65cc2bf6c4a97d042e48448fdf6a9e35e5d38cb14c3"></a>
<a id="gga691d9793fd21c41b2c192d65cc2bf6c4a47ca63851d4380aad42a0a37a17f020d"></a>
<a id="gga691d9793fd21c41b2c192d65cc2bf6c4a23fc74a635a05d082b0033b3f152592b"></a>
<a id="gga3cd6d431193b05414020ca5686f4c0e4ace5a2d3f9fcb1a8913203ee6f437b910"></a>
<a id="gga3cd6d431193b05414020ca5686f4c0e4a96900858c146259fc41af27b4cb62247"></a>
<a id="gga3cd6d431193b05414020ca5686f4c0e4ab19b506bc13aad6af3dba925153f4e7d"></a>
<a id="gga3cd6d431193b05414020ca5686f4c0e4a7f41d38c1a2125bd7c4d1765c8fbee73"></a>
<a id="gga3cd6d431193b05414020ca5686f4c0e4aa4011892d3409238f668c87626587bfd"></a>
<a id="gga3cd6d431193b05414020ca5686f4c0e4a999a15d6ed8c860af7323af1b4d86fe9"></a>
<a id="gga3cd6d431193b05414020ca5686f4c0e4a5fa53f708753d67bd6ec4f54b164b005"></a>
<a id="gga3cd6d431193b05414020ca5686f4c0e4a164fe8b7df50d8e393373153a1f70d1d"></a>
<a id="gga3cd6d431193b05414020ca5686f4c0e4ab8fd607ccdc30216fd90d4c6f568b9f6"></a>

---

[上一章](P001_音频编解码器接口（Audio Codec Interface）.md) · [返回大纲](大纲.md) · [下一章](P003_通用属性配置文件（Generic Attribute Profile，GATT）.md)
