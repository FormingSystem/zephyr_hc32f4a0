---
id: learning.zephyr-docs.api-file-gap-modem-reference.page-2
title: zephyr__bluetooth__gap.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_bluetooth\_\_gap.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gap_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙通用接入配置文件（Generic Access Profile）的定义和分配编号。

<a id="details"></a>

```c
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/byteorder.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

蓝牙通用接入配置文件（Generic Access Profile）的定义和分配编号。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga39ab5040c9471631486da7dbebd9c36f"></a>

```c
#define BT_GAP_ADV_MAX_ADV_DATA_LEN 31
```

相关声明：[BT_GAP_ADV_MAX_ADV_DATA_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga39ab5040c9471631486da7dbebd9c36f)。

最大广播数据长度（Maximum advertising data length）。

<a id="r_ga53af114e4925482739dc50dc84c2f641"></a>

```c
#define BT_GAP_ADV_MAX_EXT_ADV_DATA_LEN 1650
```

相关声明：[BT_GAP_ADV_MAX_EXT_ADV_DATA_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga53af114e4925482739dc50dc84c2f641)。

扩展广播数据（Extended Advertising Data）的最大长度。

<a id="r_ga61ccce819d75313cb2ee58309ed4b275"></a>

```c
#define BT_GAP_TX_POWER_INVALID 0x7f
```

相关声明：[BT_GAP_TX_POWER_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga61ccce819d75313cb2ee58309ed4b275)。

哨兵值（Sentinel Value），表示以 dBm 为单位的发射功率（TX Power）不可用或未知。

<a id="r_ga64b5c5e429dadf1e875984f69cd399dc"></a>

```c
#define BT_GAP_RSSI_INVALID 0x7f
```

相关声明：[BT_GAP_RSSI_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga64b5c5e429dadf1e875984f69cd399dc)。

哨兵值（Sentinel Value），表示以 dBm 为单位的接收信号强度指示（RSSI）不可用或未知。

<a id="r_ga103af3e3142473be8897cd2647dca915"></a>

```c
#define BT_GAP_SID_INVALID 0xff
```

相关声明：[BT_GAP_SID_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga103af3e3142473be8897cd2647dca915)。

哨兵值（Sentinel Value），表示广播集标识符（Advertising Set Identifier）无效或未知。

<a id="r_ga9d6b2af6b96eab6356ded93c54301ef6"></a>

```c
#define BT_GAP_NO_TIMEOUT 0x0000
```

相关声明：[BT_GAP_NO_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga9d6b2af6b96eab6356ded93c54301ef6)。

哨兵值（Sentinel Value），表示未设置超时（Timeout）。

<a id="r_gabe483d4dd601b11ac3eea570c962b1ec"></a>

```c
#define BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT 128
```

相关声明：[BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gabe483d4dd601b11ac3eea570c962b1ec)。

<a id="r_ga90cfab7c375a8af6f9224a5635cbd023"></a>

```c
#define BT_GAP_DATA_LEN_DEFAULT 0x001b /* 27 bytes */
```

相关声明：[BT_GAP_DATA_LEN_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga90cfab7c375a8af6f9224a5635cbd023)。

默认数据长度（Default Data Length）。

<a id="r_gacf5f35866d4677bd45c6e567886cabb9"></a>

```c
#define BT_GAP_DATA_LEN_MAX 0x00fb /* 251 bytes */
```

相关声明：[BT_GAP_DATA_LEN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gacf5f35866d4677bd45c6e567886cabb9)。

最大数据长度（Maximum Data Length）。

<a id="r_ga245249c0b6f8ccc419f2132f76362908"></a>

```c
#define BT_GAP_DATA_TIME_DEFAULT 0x0148 /* 328 us */
```

相关声明：[BT_GAP_DATA_TIME_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga245249c0b6f8ccc419f2132f76362908)。

默认数据时间（Default Data Time）。

<a id="r_ga379b5d8d7f243abbc584c288cd01815f"></a>

```c
#define BT_GAP_DATA_TIME_MAX 0x4290 /* 17040 us */
```

相关声明：[BT_GAP_DATA_TIME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga379b5d8d7f243abbc584c288cd01815f)。

最大数据时间（Maximum Data Time）。

<a id="r_gacf05b7660d2ae85f64e2a220abf8e57d"></a>

```c
#define BT_GAP_SID_MIN 0x00
```

相关声明：[BT_GAP_SID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gacf05b7660d2ae85f64e2a220abf8e57d)。

最小广播集数量（Minimum Advertising Set Number）。

<a id="r_gafa6f803fe3ada07030fb1f2f725940c4"></a>

```c
#define BT_GAP_SID_MAX 0x0F
```

相关声明：[BT_GAP_SID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gafa6f803fe3ada07030fb1f2f725940c4)。

最大广播集数量（Maximum Advertising Set Number）。

<a id="r_gaf92b229c47309a7a5e99047f28b860e7"></a>

```c
#define BT_GAP_PER_ADV_MAX_SKIP 0x01F3
```

相关声明：[BT_GAP_PER_ADV_MAX_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaf92b229c47309a7a5e99047f28b860e7)。

成功接收后可跳过的连续周期广播事件（Periodic Advertisement Events）的最大数量。

<a id="r_ga17d8ae7e98f6a1dfead4f8ecb75f9645"></a>

```c
#define BT_GAP_PER_ADV_MIN_TIMEOUT 0x000A /* 100 ms */
```

相关声明：[BT_GAP_PER_ADV_MIN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga17d8ae7e98f6a1dfead4f8ecb75f9645)。

最小周期广播超时（Periodic Advertising Timeout），单位为 `N * 10 ms`。

<a id="r_gad6674199f615fa6ecaeb1fe9d099e04c"></a>

```c
#define BT_GAP_PER_ADV_MAX_TIMEOUT 0x4000 /* 163.84 s */
```

相关声明：[BT_GAP_PER_ADV_MAX_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gad6674199f615fa6ecaeb1fe9d099e04c)。

最大周期广播超时（Periodic Advertising Timeout），单位为 `N * 10 ms`。

<a id="r_ga07e21fdeb8a0a0b967690898bef2f7aa"></a>

```c
#define BT_GAP_PER_ADV_MIN_INTERVAL 0x0006 /* 7.5 ms */
```

相关声明：[BT_GAP_PER_ADV_MIN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga07e21fdeb8a0a0b967690898bef2f7aa)。

最小周期广播间隔（Minimum Periodic Advertising Interval），为 N × 1.25 毫秒。

<a id="r_ga80bf3f1fb6f34a2c4363687149c365bd"></a>

```c
#define BT_GAP_PER_ADV_MAX_INTERVAL 0xFFFF /* 81.91875 s */
```

相关声明：[BT_GAP_PER_ADV_MAX_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga80bf3f1fb6f34a2c4363687149c365bd)。

最大周期广播间隔（Maximum Periodic Advertising Interval），为 N × 1.25 毫秒。

<a id="r_ga6e10b5311c785ad7eea10743987c0f27"></a>

```c
#define BT_GAP_ADV_INTERVAL_TO_US(_interval)
```

相关声明：[BT_GAP_ADV_INTERVAL_TO_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga6e10b5311c785ad7eea10743987c0f27)。

将广播间隔（Advertising Interval，`N * 0.625 ms`）转换为微秒。

<a id="r_ga7261e64328e433d333d88d3a4cad21de"></a>

```c
#define BT_GAP_ADV_INTERVAL_TO_MS(_interval)
```

相关声明：[BT_GAP_ADV_INTERVAL_TO_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga7261e64328e433d333d88d3a4cad21de)。

将广播间隔（Advertising Interval，`N * 0.625 ms`）转换为毫秒。

<a id="r_ga4feca4664259c43121c2ff481d9ee611"></a>

```c
#define BT_GAP_ISO_INTERVAL_TO_US(_interval)
```

相关声明：[BT_GAP_ISO_INTERVAL_TO_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga4feca4664259c43121c2ff481d9ee611)。

将等时间隔（Isochronous Interval，`N * 1.25 ms`）转换为微秒。

<a id="r_ga46c1e49ca3285ed9fc1b4ac593a25cd3"></a>

```c
#define BT_GAP_ISO_INTERVAL_TO_MS(_interval)
```

相关声明：[BT_GAP_ISO_INTERVAL_TO_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga46c1e49ca3285ed9fc1b4ac593a25cd3)。

将等时间隔（Isochronous Interval，`N * 1.25 ms`）转换为毫秒。

<a id="r_ga63587ef565ccde477b9c6f03faf778a5"></a>

```c
#define BT_GAP_PER_ADV_INTERVAL_TO_US(_interval)
```

相关声明：[BT_GAP_PER_ADV_INTERVAL_TO_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga63587ef565ccde477b9c6f03faf778a5)。

将周期广播间隔（Periodic Advertising Interval，`N * 1.25 ms`）转换为微秒（原文末尾有一个 `*`）。

<a id="r_gac240015012694df3557679d99da6c1a9"></a>

```c
#define BT_GAP_PER_ADV_INTERVAL_TO_MS(_interval)
```

相关声明：[BT_GAP_PER_ADV_INTERVAL_TO_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gac240015012694df3557679d99da6c1a9)。

将周期广播间隔（Periodic Advertising Interval，`N * 1.25 ms`）转换为毫秒。

<a id="r_gac79626389f62bb7b3e5b5f6d3a5eaf2b"></a>

```c
#define BT_GAP_US_TO_ADV_INTERVAL(_interval)
```

相关声明：[BT_GAP_US_TO_ADV_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gac79626389f62bb7b3e5b5f6d3a5eaf2b)。

将微秒转换为广播间隔（Advertising Interval）单位，每单位为 0.625 ms。

<a id="r_gaef9c34f229f1b8b06d3e6cd44a1014ef"></a>

```c
#define BT_GAP_MS_TO_ADV_INTERVAL(_interval)
```

相关声明：[BT_GAP_MS_TO_ADV_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaef9c34f229f1b8b06d3e6cd44a1014ef)。

将毫秒转换为广播间隔（Advertising Interval）单位，每单位为 0.625 ms。

<a id="r_ga5a9da01507b4356c2ad6f8309257f2ce"></a>

```c
#define BT_GAP_US_TO_PER_ADV_INTERVAL(_interval)
```

相关声明：[BT_GAP_US_TO_PER_ADV_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga5a9da01507b4356c2ad6f8309257f2ce)。

将微秒转换为周期广播间隔（Periodic Advertising Interval）单位，每单位为 1.25 ms。

<a id="r_ga15ec0bc7c9bab797d6c5595269a33ea4"></a>

```c
#define BT_GAP_MS_TO_PER_ADV_INTERVAL(_interval)
```

相关声明：[BT_GAP_MS_TO_PER_ADV_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga15ec0bc7c9bab797d6c5595269a33ea4)。

将毫秒转换为周期广播间隔（Periodic Advertising Interval）单位，每单位为 1.25 ms。

<a id="r_ga242a6a4e3dd138073c01bc600c9642eb"></a>

```c
#define BT_GAP_MS_TO_PER_ADV_SYNC_TIMEOUT(_timeout)
```

相关声明：[BT_GAP_MS_TO_PER_ADV_SYNC_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga242a6a4e3dd138073c01bc600c9642eb)。

将毫秒转换为周期广播同步超时（Periodic Advertising Sync Timeout）单位，每单位为 10 ms。

<a id="r_gaf33284a372b21e24c53deb5e3a6a91aa"></a>

```c
#define BT_GAP_US_TO_PER_ADV_SYNC_TIMEOUT(_timeout)
```

相关声明：[BT_GAP_US_TO_PER_ADV_SYNC_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaf33284a372b21e24c53deb5e3a6a91aa)。

将微秒转换为周期广播同步超时（Periodic Advertising Sync Timeout）单位，每单位为 10 ms。

<a id="r_gab65e489c4a799774f6511c6ce5b65ea2"></a>

```c
#define BT_GAP_US_TO_SCAN_INTERVAL(_interval)
```

相关声明：[BT_GAP_US_TO_SCAN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gab65e489c4a799774f6511c6ce5b65ea2)。

将微秒转换为扫描间隔（Scan Interval）单位，每单位为 0.625 ms。

<a id="r_gad18c4a9774014081833905fc9e03fb15"></a>

```c
#define BT_GAP_MS_TO_SCAN_INTERVAL(_interval)
```

相关声明：[BT_GAP_MS_TO_SCAN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gad18c4a9774014081833905fc9e03fb15)。

将毫秒转换为扫描间隔（Scan Interval）单位，每单位为 0.625 ms。

<a id="r_gaac5d0ec82d9730b793960c0470ac6342"></a>

```c
#define BT_GAP_US_TO_SCAN_WINDOW(_window)
```

相关声明：[BT_GAP_US_TO_SCAN_WINDOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaac5d0ec82d9730b793960c0470ac6342)。

将微秒转换为扫描窗口（Scan Window）单位，每单位为 0.625 ms。

<a id="r_ga5204f7e42b4e33eb8ae4ae71b82a4c88"></a>

```c
#define BT_GAP_MS_TO_SCAN_WINDOW(_window)
```

相关声明：[BT_GAP_MS_TO_SCAN_WINDOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga5204f7e42b4e33eb8ae4ae71b82a4c88)。

将毫秒转换为扫描窗口（Scan Window）单位，每单位为 0.625 ms。

<a id="r_gab12ba919a5a389b4c342d142d3a9ce6e"></a>

```c
#define BT_GAP_US_TO_CONN_INTERVAL(_interval)
```

相关声明：[BT_GAP_US_TO_CONN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gab12ba919a5a389b4c342d142d3a9ce6e)。

将微秒转换为连接间隔（Connection Interval）单位，每单位为 1.25 ms。

<a id="r_ga75985e2c444da7b2426cc746c9781c8c"></a>

```c
#define BT_GAP_MS_TO_CONN_INTERVAL(_interval)
```

相关声明：[BT_GAP_MS_TO_CONN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga75985e2c444da7b2426cc746c9781c8c)。

将毫秒转换为连接间隔（Connection Interval）单位，每单位为 1.25 ms。

<a id="r_ga24f79cacceeea262987f3cdaf2ef6bc3"></a>

```c
#define BT_GAP_MS_TO_CONN_TIMEOUT(_timeout)
```

相关声明：[BT_GAP_MS_TO_CONN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga24f79cacceeea262987f3cdaf2ef6bc3)。

将毫秒转换为连接监督超时（Connection Supervision Timeout）单位，每单位为 10 ms。

<a id="r_ga317a60f9edb371fef180130282805539"></a>

```c
#define BT_GAP_US_TO_CONN_TIMEOUT(_timeout)
```

相关声明：[BT_GAP_US_TO_CONN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga317a60f9edb371fef180130282805539)。

将微秒转换为连接监督超时（Connection Supervision Timeout）单位，每单位为 10 ms。

<a id="r_ga8905e22b1864021b77367c228b8bff48"></a>

```c
#define BT_GAP_US_TO_CONN_EVENT_LEN(_event_len)
```

相关声明：[BT_GAP_US_TO_CONN_EVENT_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga8905e22b1864021b77367c228b8bff48)。

将毫秒转换为连接事件长度（Connection Event Length）单位，原文给出的单位值为 0.625。

<a id="r_gaa3703cccd343dbb6418fdeb47a718eb5"></a>

```c
#define BT_GAP_MS_TO_CONN_EVENT_LEN(_event_len)
```

相关声明：[BT_GAP_MS_TO_CONN_EVENT_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaa3703cccd343dbb6418fdeb47a718eb5)。

将毫秒转换为连接事件长度（Connection Event Length）单位，原文给出的单位值为 0.625。

<a id="r_ga799f6cb9dd02b9995ed76fbe97be3eb3"></a>

```c
#define BT_LE_SUPP_FEAT_40_ENCODE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_40_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga799f6cb9dd02b9995ed76fbe97be3eb3)。

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 40 位，以小端序（Little-Endian）编码为数组值。

<a id="r_ga7aa92098e33840ff02cb8c0435637094"></a>

```c
#define BT_LE_SUPP_FEAT_32_ENCODE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_32_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga7aa92098e33840ff02cb8c0435637094)。

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 4 字节，以小端序（Little-Endian）编码为长度为 4 字节的数组。

<a id="r_gab8739c92f8d50b796539a21027c3b6eb"></a>

```c
#define BT_LE_SUPP_FEAT_24_ENCODE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_24_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gab8739c92f8d50b796539a21027c3b6eb)。

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 3 字节，以小端序（Little-Endian）编码为长度为 3 字节的数组。

<a id="r_ga3c29ad99d6a6e020148590381ab08b17"></a>

```c
#define BT_LE_SUPP_FEAT_16_ENCODE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_16_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga3c29ad99d6a6e020148590381ab08b17)。

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低 2 字节，以小端序（Little-Endian）编码为长度为 2 字节的数组。

<a id="r_ga8fac302925ac3ef8982630e6a0ec13af"></a>

```c
#define BT_LE_SUPP_FEAT_8_ENCODE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_8_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga8fac302925ac3ef8982630e6a0ec13af)。

将 64 位低功耗蓝牙支持特性（LE Supported Features）的最低字节编码为长度为 1 字节的数组。

<a id="r_ga86266eaf452dfaf82f097992e01397c8"></a>

```c
#define BT_LE_SUPP_FEAT_VALIDATE(w64)
```

相关声明：[BT_LE_SUPP_FEAT_VALIDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga86266eaf452dfaf82f097992e01397c8)。

验证低功耗蓝牙支持特性（LE Supported Features）值是否未使用为未来用途保留的位。

<a id="define-members-0"></a>

### 公司标识符（Company Identifiers，参见 Bluetooth Assigned Numbers）

<a id="r_ga6bbf21c05f24d2c2c710be9bcf05af5f"></a>

```c
#define BT_COMP_ID_LF 0x05f1
```

相关声明：[BT_COMP_ID_LF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga6bbf21c05f24d2c2c710be9bcf05af5f)。

Linux 基金会（The Linux Foundation）。

<a id="define-members-1"></a>

### 已定义的通用访问配置文件定时器（Defined GAP Timers）

依据《蓝牙核心规范》（Bluetooth Core Specification）6.2，第 3 卷 C 部分附录 A。

<a id="r_gae9356673ee78d9abb27891738344513a"></a>

```c
#define BT_GAP_SCAN_FAST_INTERVAL_MIN 0x0030
```

相关声明：[BT_GAP_SCAN_FAST_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gae9356673ee78d9abb27891738344513a)。

建议的快速扫描最小扫描间隔（Minimum Scan Interval）。

<a id="r_ga747caa714962215453a966a323e77cf8"></a>

```c
#define BT_GAP_SCAN_FAST_INTERVAL 0x0060
```

相关声明：[BT_GAP_SCAN_FAST_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga747caa714962215453a966a323e77cf8)。

建议的快速扫描最大扫描间隔（Maximum Scan Interval）。

<a id="r_ga100e1c20813630848a1a80390e8a06a0"></a>

```c
#define BT_GAP_SCAN_FAST_WINDOW 0x0030
```

相关声明：[BT_GAP_SCAN_FAST_WINDOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga100e1c20813630848a1a80390e8a06a0)。

建议的快速扫描窗口（Scan Window）。

<a id="r_ga1acb5143221e9f94af4d5dc3a9eab125"></a>

```c
#define BT_GAP_SCAN_SLOW_INTERVAL_1 0x0800
```

相关声明：[BT_GAP_SCAN_SLOW_INTERVAL_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga1acb5143221e9f94af4d5dc3a9eab125)。

建议的慢速扫描间隔（Scan Interval，模式 1）。

<a id="r_ga29a1a15bfbe035f439c48d1db96db392"></a>

```c
#define BT_GAP_SCAN_SLOW_WINDOW_1 0x0012
```

相关声明：[BT_GAP_SCAN_SLOW_WINDOW_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga29a1a15bfbe035f439c48d1db96db392)。

建议的慢速扫描窗口（Scan Window，模式 1）。

<a id="r_ga38455c10880fddac0a1b4303a642e44d"></a>

```c
#define BT_GAP_SCAN_SLOW_INTERVAL_2 0x1000
```

相关声明：[BT_GAP_SCAN_SLOW_INTERVAL_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga38455c10880fddac0a1b4303a642e44d)。

建议的慢速扫描间隔（Scan Interval，模式 2）。

<a id="r_gaa809fd8143c2805768874195ac24936f"></a>

```c
#define BT_GAP_SCAN_SLOW_WINDOW_2 0x0012
```

相关声明：[BT_GAP_SCAN_SLOW_WINDOW_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaa809fd8143c2805768874195ac24936f)。

建议的慢速扫描窗口（Scan Window，模式 2）。

<a id="r_ga397a52fe616416665b46a2bc454c2e11"></a>

```c
#define BT_GAP_ADV_FAST_INT_MIN_1 0x0030
```

相关声明：[BT_GAP_ADV_FAST_INT_MIN_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga397a52fe616416665b46a2bc454c2e11)。

建议的快速广播最小广播间隔（Minimum Advertising Interval，模式 1）。

<a id="r_ga13acf16d3d8edd39636bb10df752775a"></a>

```c
#define BT_GAP_ADV_FAST_INT_MAX_1 0x0060
```

相关声明：[BT_GAP_ADV_FAST_INT_MAX_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga13acf16d3d8edd39636bb10df752775a)。

建议的快速广播最大广播间隔（Maximum Advertising Interval，模式 1）。

<a id="r_ga9573e6bcdae3aae9d51c0becbbd7ac60"></a>

```c
#define BT_GAP_ADV_FAST_INT_MIN_2 0x00a0
```

相关声明：[BT_GAP_ADV_FAST_INT_MIN_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga9573e6bcdae3aae9d51c0becbbd7ac60)。

建议的快速广播最小广播间隔（Minimum Advertising Interval，模式 2）。

<a id="r_gaebc3ce60836522d883f664227a3ffcfb"></a>

```c
#define BT_GAP_ADV_FAST_INT_MAX_2 0x00f0
```

相关声明：[BT_GAP_ADV_FAST_INT_MAX_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaebc3ce60836522d883f664227a3ffcfb)。

建议的快速广播最大广播间隔（Maximum Advertising Interval，模式 2）。

<a id="r_ga647f70c07c15f11287b735cbaad2a326"></a>

```c
#define BT_GAP_ADV_SLOW_INT_MIN 0x0640
```

相关声明：[BT_GAP_ADV_SLOW_INT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga647f70c07c15f11287b735cbaad2a326)。

建议的慢速广播最小广播间隔（Minimum Advertising Interval）。

<a id="r_gadecbfb823bbb6ffdd48be02df2f05f87"></a>

```c
#define BT_GAP_ADV_SLOW_INT_MAX 0x0780
```

相关声明：[BT_GAP_ADV_SLOW_INT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gadecbfb823bbb6ffdd48be02df2f05f87)。

建议的慢速广播最大广播间隔（Maximum Advertising Interval）。

<a id="r_gafd724ebc809044574283c5547beda824"></a>

```c
#define BT_GAP_PER_ADV_FAST_INT_MIN_1 0x0018
```

相关声明：[BT_GAP_PER_ADV_FAST_INT_MIN_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gafd724ebc809044574283c5547beda824)。

建议的快速广播最小周期广播间隔（Minimum Periodic Advertising Interval，模式 1）。

<a id="r_ga849315b0b724af6017b910e78db0cfae"></a>

```c
#define BT_GAP_PER_ADV_FAST_INT_MAX_1 0x0030
```

相关声明：[BT_GAP_PER_ADV_FAST_INT_MAX_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga849315b0b724af6017b910e78db0cfae)。

建议的快速广播最大周期广播间隔（Maximum Periodic Advertising Interval，模式 1）。

<a id="r_ga61eb4d6d65f1dd9c475a6f2f44b27957"></a>

```c
#define BT_GAP_PER_ADV_FAST_INT_MIN_2 0x0050
```

相关声明：[BT_GAP_PER_ADV_FAST_INT_MIN_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga61eb4d6d65f1dd9c475a6f2f44b27957)。

建议的快速广播最小周期广播间隔（Minimum Periodic Advertising Interval，模式 2）。

<a id="r_ga264134294d8378d6e7d2bc52d4e0af1c"></a>

```c
#define BT_GAP_PER_ADV_FAST_INT_MAX_2 0x0078
```

相关声明：[BT_GAP_PER_ADV_FAST_INT_MAX_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga264134294d8378d6e7d2bc52d4e0af1c)。

建议的快速广播最大周期广播间隔（Maximum Periodic Advertising Interval，模式 2）。

<a id="r_gab51898ce46ee9ae468ed7ffc1d117321"></a>

```c
#define BT_GAP_PER_ADV_SLOW_INT_MIN 0x0320
```

相关声明：[BT_GAP_PER_ADV_SLOW_INT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gab51898ce46ee9ae468ed7ffc1d117321)。

建议的慢速广播最小周期广播间隔（Minimum Periodic Advertising Interval）。

<a id="r_gaa618da2a7c217527b0d962315caa1c22"></a>

```c
#define BT_GAP_PER_ADV_SLOW_INT_MAX 0x03C0
```

相关声明：[BT_GAP_PER_ADV_SLOW_INT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaa618da2a7c217527b0d962315caa1c22)。

建议的慢速广播最大周期广播间隔（Maximum Periodic Advertising Interval）。

<a id="r_gadaa7f1547c4ea22936087c181d82a552"></a>

```c
#define BT_GAP_INIT_CONN_INT_MIN 0x0018
```

相关声明：[BT_GAP_INIT_CONN_INT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gadaa7f1547c4ea22936087c181d82a552)。

建议的最小初始连接间隔（Minimum Initial Connection Interval）。

<a id="r_ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1"></a>

```c
#define BT_GAP_INIT_CONN_INT_MAX 0x0028
```

相关声明：[BT_GAP_INIT_CONN_INT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1)。

建议的最大初始连接间隔（Maximum Initial Connection Interval）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.2\_枚举（Enumerations）

<a id="r_ga691d9793fd21c41b2c192d65cc2bf6c4"></a>

```c
enum bt_gap_le_phy { BT_GAP_LE_PHY_NONE = 0 , BT_GAP_LE_PHY_1M = (1UL << (0)) , BT_GAP_LE_PHY_2M = (1UL << (1)) , BT_GAP_LE_PHY_CODED = (1UL << (2)) , BT_GAP_LE_PHY_CODED_S8 = (1UL << (3)) , BT_GAP_LE_PHY_CODED_S2 = (1UL << (4)) }
```

相关声明：[bt_gap_le_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga691d9793fd21c41b2c192d65cc2bf6c4)、[BT_GAP_LE_PHY_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4aaf7e1b40f6464a603e5116db269cacab)、[BT_GAP_LE_PHY_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a53eff400720a20fe1a91da4834bad752)、[BT_GAP_LE_PHY_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a662049cc8293959194bcb481e1dd50a8)、[BT_GAP_LE_PHY_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a97d042e48448fdf6a9e35e5d38cb14c3)、[BT_GAP_LE_PHY_CODED_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a47ca63851d4380aad42a0a37a17f020d)、[BT_GAP_LE_PHY_CODED_S2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a23fc74a635a05d082b0033b3f152592b)。

低功耗蓝牙物理层类型（LE PHY Types）。

<a id="r_ga07833ed1f79708d5f6a5d0c2e01d4dca"></a>

```c
enum bt_gap_adv_type { BT_GAP_ADV_TYPE_ADV_IND = 0x00 , BT_GAP_ADV_TYPE_ADV_DIRECT_IND = 0x01 , BT_GAP_ADV_TYPE_ADV_SCAN_IND = 0x02 , BT_GAP_ADV_TYPE_ADV_NONCONN_IND = 0x03 , BT_GAP_ADV_TYPE_SCAN_RSP = 0x04 , BT_GAP_ADV_TYPE_EXT_ADV = 0x05 }
```

相关声明：[bt_gap_adv_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga07833ed1f79708d5f6a5d0c2e01d4dca)、[BT_GAP_ADV_TYPE_ADV_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaaf4d48e46c1da164e876e4ded28470c82)、[BT_GAP_ADV_TYPE_ADV_DIRECT_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaa05b182a44fea67f52015cbfb4d775be8)、[BT_GAP_ADV_TYPE_ADV_SCAN_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaae48316c135886d9f6d20f7bdba0858c1)、[BT_GAP_ADV_TYPE_ADV_NONCONN_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaabb587b376bd6511881d6b70ceaa2af56)、[BT_GAP_ADV_TYPE_SCAN_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaa5387de0177d3a9da9fd0c44ca30c7018)、[BT_GAP_ADV_TYPE_EXT_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaa09292ffe2f0b76b8761fcaad6fbf9ba8)。

广播协议数据单元类型（Advertising PDU Types）。

<a id="r_ga8ac9dd875bc7480929b5166193c621d0"></a>

```c
enum bt_gap_adv_prop { BT_GAP_ADV_PROP_CONNECTABLE = (1UL << (0)) , BT_GAP_ADV_PROP_SCANNABLE = (1UL << (1)) , BT_GAP_ADV_PROP_DIRECTED = (1UL << (2)) , BT_GAP_ADV_PROP_SCAN_RESPONSE = (1UL << (3)) , BT_GAP_ADV_PROP_EXT_ADV = (1UL << (4)) }
```

相关声明：[bt_gap_adv_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga8ac9dd875bc7480929b5166193c621d0)、[BT_GAP_ADV_PROP_CONNECTABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0af843db0752f3360ccb1a02c456ca9e5e)、[BT_GAP_ADV_PROP_SCANNABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0a6c5ea1b8392783568b568c74f9f17571)、[BT_GAP_ADV_PROP_DIRECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0a4595d3a3ea30bd4cd51ba4f1c4ab7de9)、[BT_GAP_ADV_PROP_SCAN_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0a55258ac9a7b355db87aeec5d443718f7)、[BT_GAP_ADV_PROP_EXT_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0aeda2301e9eb191e742375e54bb765684)。

广播协议数据单元属性（Advertising PDU Properties）。

<a id="r_gab7418dd67b5c7fb9b0f9cfd5a55fe272"></a>

```c
enum bt_gap_cte { BT_GAP_CTE_AOA = 0x00 , BT_GAP_CTE_AOD_1US = 0x01 , BT_GAP_CTE_AOD_2US = 0x02 , BT_GAP_CTE_NONE = 0xFF }
```

相关声明：[bt_gap_cte](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gab7418dd67b5c7fb9b0f9cfd5a55fe272)、[BT_GAP_CTE_AOA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ggab7418dd67b5c7fb9b0f9cfd5a55fe272a8a82746ee64ffbcc62e79fdd8e0e30a0)、[BT_GAP_CTE_AOD_1US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ggab7418dd67b5c7fb9b0f9cfd5a55fe272aa8587383f9ea245e8c279fdd63417a19)、[BT_GAP_CTE_AOD_2US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ggab7418dd67b5c7fb9b0f9cfd5a55fe272a2385af24a5a82f4d799674443b92e966)、[BT_GAP_CTE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ggab7418dd67b5c7fb9b0f9cfd5a55fe272aec9324d8e0997e1ace59895e168087e8)。

恒定音调扩展类型（Constant Tone Extension Types，CTE Types）。

<a id="r_ga3cd6d431193b05414020ca5686f4c0e4"></a>

```c
enum bt_gap_sca { BT_GAP_SCA_UNKNOWN = 0 , BT_GAP_SCA_251_500 = 0 , BT_GAP_SCA_151_250 = 1 , BT_GAP_SCA_101_150 = 2 , BT_GAP_SCA_76_100 = 3 , BT_GAP_SCA_51_75 = 4 , BT_GAP_SCA_31_50 = 5 , BT_GAP_SCA_21_30 = 6 , BT_GAP_SCA_0_20 = 7 }
```

相关声明：[bt_gap_sca](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga3cd6d431193b05414020ca5686f4c0e4)、[BT_GAP_SCA_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4ace5a2d3f9fcb1a8913203ee6f437b910)、[BT_GAP_SCA_251_500](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4a96900858c146259fc41af27b4cb62247)、[BT_GAP_SCA_151_250](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4ab19b506bc13aad6af3dba925153f4e7d)、[BT_GAP_SCA_101_150](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4a7f41d38c1a2125bd7c4d1765c8fbee73)、[BT_GAP_SCA_76_100](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4aa4011892d3409238f668c87626587bfd)、[BT_GAP_SCA_51_75](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4a999a15d6ed8c860af7323af1b4d86fe9)、[BT_GAP_SCA_31_50](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4a5fa53f708753d67bd6ec4f54b164b005)、[BT_GAP_SCA_21_30](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4a164fe8b7df50d8e393373153a1f70d1d)、[BT_GAP_SCA_0_20](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga3cd6d431193b05414020ca5686f4c0e4ab8fd607ccdc30216fd90d4c6f568b9f6)。

外设睡眠时钟精度（Sleep Clock Accuracy，SCA），单位为百万分之一（Parts per Million，ppm）。


## 2.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/assigned_numbers.h](../api_source_socket_ethernet_reference/P001_assigned_numbers.h_源码浏览.md)
- [zephyr/bluetooth/byteorder.h](../byteorder_reference/P005_蓝牙字节序头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_transport_clock_reference/P016_gap.h_源码浏览.md)
- [BT_GAP_ADV_MAX_ADV_DATA_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga39ab5040c9471631486da7dbebd9c36f)
- [BT_GAP_ADV_MAX_EXT_ADV_DATA_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga53af114e4925482739dc50dc84c2f641)
- [BT_GAP_TX_POWER_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga61ccce819d75313cb2ee58309ed4b275)
- [BT_GAP_RSSI_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga64b5c5e429dadf1e875984f69cd399dc)
- [BT_GAP_SID_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga103af3e3142473be8897cd2647dca915)
- [BT_GAP_NO_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga9d6b2af6b96eab6356ded93c54301ef6)
- [BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gabe483d4dd601b11ac3eea570c962b1ec)
- [BT_GAP_DATA_LEN_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga90cfab7c375a8af6f9224a5635cbd023)
- [BT_GAP_DATA_LEN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gacf5f35866d4677bd45c6e567886cabb9)
- [BT_GAP_DATA_TIME_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga245249c0b6f8ccc419f2132f76362908)
- [BT_GAP_DATA_TIME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga379b5d8d7f243abbc584c288cd01815f)
- [BT_GAP_SID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gacf05b7660d2ae85f64e2a220abf8e57d)
- [BT_GAP_SID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gafa6f803fe3ada07030fb1f2f725940c4)
- [BT_GAP_PER_ADV_MAX_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaf92b229c47309a7a5e99047f28b860e7)
- [BT_GAP_PER_ADV_MIN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga17d8ae7e98f6a1dfead4f8ecb75f9645)
- [BT_GAP_PER_ADV_MAX_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gad6674199f615fa6ecaeb1fe9d099e04c)
- [BT_GAP_PER_ADV_MIN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga07e21fdeb8a0a0b967690898bef2f7aa)
- [BT_GAP_PER_ADV_MAX_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga80bf3f1fb6f34a2c4363687149c365bd)
- [BT_GAP_ADV_INTERVAL_TO_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga6e10b5311c785ad7eea10743987c0f27)
- [BT_GAP_ADV_INTERVAL_TO_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga7261e64328e433d333d88d3a4cad21de)
- [BT_GAP_ISO_INTERVAL_TO_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga4feca4664259c43121c2ff481d9ee611)
- [BT_GAP_ISO_INTERVAL_TO_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga46c1e49ca3285ed9fc1b4ac593a25cd3)
- [BT_GAP_PER_ADV_INTERVAL_TO_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga63587ef565ccde477b9c6f03faf778a5)
- [BT_GAP_PER_ADV_INTERVAL_TO_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gac240015012694df3557679d99da6c1a9)
- [BT_GAP_US_TO_ADV_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gac79626389f62bb7b3e5b5f6d3a5eaf2b)
- [BT_GAP_MS_TO_ADV_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaef9c34f229f1b8b06d3e6cd44a1014ef)
- [BT_GAP_US_TO_PER_ADV_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga5a9da01507b4356c2ad6f8309257f2ce)
- [BT_GAP_MS_TO_PER_ADV_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga15ec0bc7c9bab797d6c5595269a33ea4)
- [BT_GAP_MS_TO_PER_ADV_SYNC_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga242a6a4e3dd138073c01bc600c9642eb)
- [BT_GAP_US_TO_PER_ADV_SYNC_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaf33284a372b21e24c53deb5e3a6a91aa)
- [BT_GAP_US_TO_SCAN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gab65e489c4a799774f6511c6ce5b65ea2)
- [BT_GAP_MS_TO_SCAN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gad18c4a9774014081833905fc9e03fb15)
- [BT_GAP_US_TO_SCAN_WINDOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaac5d0ec82d9730b793960c0470ac6342)
- [BT_GAP_MS_TO_SCAN_WINDOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga5204f7e42b4e33eb8ae4ae71b82a4c88)
- [BT_GAP_US_TO_CONN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gab12ba919a5a389b4c342d142d3a9ce6e)
- [BT_GAP_MS_TO_CONN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga75985e2c444da7b2426cc746c9781c8c)
- [BT_GAP_MS_TO_CONN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga24f79cacceeea262987f3cdaf2ef6bc3)
- [BT_GAP_US_TO_CONN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga317a60f9edb371fef180130282805539)
- [BT_GAP_US_TO_CONN_EVENT_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga8905e22b1864021b77367c228b8bff48)
- [BT_GAP_MS_TO_CONN_EVENT_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaa3703cccd343dbb6418fdeb47a718eb5)
- [BT_LE_SUPP_FEAT_40_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga799f6cb9dd02b9995ed76fbe97be3eb3)
- [BT_LE_SUPP_FEAT_32_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga7aa92098e33840ff02cb8c0435637094)
- [BT_LE_SUPP_FEAT_24_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gab8739c92f8d50b796539a21027c3b6eb)
- [BT_LE_SUPP_FEAT_16_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga3c29ad99d6a6e020148590381ab08b17)
- [BT_LE_SUPP_FEAT_8_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga8fac302925ac3ef8982630e6a0ec13af)
- [BT_LE_SUPP_FEAT_VALIDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga86266eaf452dfaf82f097992e01397c8)
- [BT_COMP_ID_LF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga6bbf21c05f24d2c2c710be9bcf05af5f)
- [BT_GAP_SCAN_FAST_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gae9356673ee78d9abb27891738344513a)
- [BT_GAP_SCAN_FAST_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga747caa714962215453a966a323e77cf8)
- [BT_GAP_SCAN_FAST_WINDOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga100e1c20813630848a1a80390e8a06a0)
- [BT_GAP_SCAN_SLOW_INTERVAL_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga1acb5143221e9f94af4d5dc3a9eab125)
- [BT_GAP_SCAN_SLOW_WINDOW_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga29a1a15bfbe035f439c48d1db96db392)
- [BT_GAP_SCAN_SLOW_INTERVAL_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga38455c10880fddac0a1b4303a642e44d)
- [BT_GAP_SCAN_SLOW_WINDOW_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaa809fd8143c2805768874195ac24936f)
- [BT_GAP_ADV_FAST_INT_MIN_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga397a52fe616416665b46a2bc454c2e11)
- [BT_GAP_ADV_FAST_INT_MAX_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga13acf16d3d8edd39636bb10df752775a)
- [BT_GAP_ADV_FAST_INT_MIN_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga9573e6bcdae3aae9d51c0becbbd7ac60)
- [BT_GAP_ADV_FAST_INT_MAX_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaebc3ce60836522d883f664227a3ffcfb)
- [BT_GAP_ADV_SLOW_INT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga647f70c07c15f11287b735cbaad2a326)
- [BT_GAP_ADV_SLOW_INT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gadecbfb823bbb6ffdd48be02df2f05f87)
- [BT_GAP_PER_ADV_FAST_INT_MIN_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gafd724ebc809044574283c5547beda824)
- [BT_GAP_PER_ADV_FAST_INT_MAX_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga849315b0b724af6017b910e78db0cfae)
- [BT_GAP_PER_ADV_FAST_INT_MIN_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga61eb4d6d65f1dd9c475a6f2f44b27957)
- [BT_GAP_PER_ADV_FAST_INT_MAX_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga264134294d8378d6e7d2bc52d4e0af1c)
- [BT_GAP_PER_ADV_SLOW_INT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gab51898ce46ee9ae468ed7ffc1d117321)
- [BT_GAP_PER_ADV_SLOW_INT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gaa618da2a7c217527b0d962315caa1c22)
- [BT_GAP_INIT_CONN_INT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gadaa7f1547c4ea22936087c181d82a552)
- [BT_GAP_INIT_CONN_INT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1)
- [bt_gap_le_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga691d9793fd21c41b2c192d65cc2bf6c4)
- [BT_GAP_LE_PHY_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4aaf7e1b40f6464a603e5116db269cacab)
- [BT_GAP_LE_PHY_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a53eff400720a20fe1a91da4834bad752)
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

<a id="header-details"></a>

---

[上一章](P001_zephyr__bluetooth__audio__bap_lc3_preset.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__modem__hl7800.h_文件参考.md)
