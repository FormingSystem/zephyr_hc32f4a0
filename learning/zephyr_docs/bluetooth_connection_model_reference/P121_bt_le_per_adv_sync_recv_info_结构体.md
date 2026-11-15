---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-121
title: bt_le_per_adv_sync_recv_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__recv__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第121章\_bt\_le\_per\_adv\_sync\_recv\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__recv__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已接收的周期广播报告（Periodic Advertising Report）的信息。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

已接收周期广播报告的信息（Received periodic advertising report information）。此结构保存已接收周期广播事件的相关信息，包括广播器地址、广播集标识符（SID）、发射功率（Transmit power）、接收信号强度指示（RSSI）、恒定音调扩展类型（CTE type），以及依配置而定的附加信息，例如子事件指示的事件计数器和子事件。收到周期广播数据时，通过回调提供这些信息。注意（Note）：用于 `bt_le_per_adv_sync_cb` 结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 121.1\_数据成员（Data Fields）

<a id="r_a5817bd4fba2c93adebcebe007650b6eb"></a>

```c
const bt_addr_le_t * addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a5817bd4fba2c93adebcebe007650b6eb)。

广播器的低功耗地址及类型（Advertiser LE address and type）。

<a id="r_a21b0ca87e46c6897282ebd877e45114e"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a21b0ca87e46c6897282ebd877e45114e)。

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

<a id="r_a65f1a2adb7c3d740cb8262ae7f5a7c3e"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a65f1a2adb7c3d740cb8262ae7f5a7c3e)。

广播的发射功率（TX power），单位为 dBm。

<a id="r_aa17c9d917469f121448ed4e1db485700"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#aa17c9d917469f121448ed4e1db485700)。

广播的接收信号强度指示（RSSI），不计任何恒定音调扩展（CTE），单位为 dBm。

<a id="r_a1591907e3cb1f4565b9d26c18bccc7d2"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a1591907e3cb1f4565b9d26c18bccc7d2)。

广播中的恒定音调扩展（Constant Tone Extension，CTE），参见 `bt_df_cte_type`。

<a id="r_a74f6dc1745a756faca2e323292024730"></a>

```c
uint16_t periodic_event_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[periodic_event_counter](#a74f6dc1745a756faca2e323292024730)。

接收子事件指示（Subevent indication）时的事件计数器值（Event counter）。

<a id="r_a1a9dccd6d7592868b5604ec16a5f1540"></a>

```c
uint8_t subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent](#a1a9dccd6d7592868b5604ec16a5f1540)。

接收子事件指示（Subevent indication）所在的子事件。

## 121.2\_详细说明（Detailed Documentation）

<a id="a5817bd4fba2c93adebcebe007650b6eb"></a>

### `addr`

```c
const bt_addr_le_t* bt_le_per_adv_sync_recv_info::addr
```

广播器的低功耗地址及类型（Advertiser LE address and type）。

<a id="a1591907e3cb1f4565b9d26c18bccc7d2"></a>

### `cte_type`

```c
uint8_t bt_le_per_adv_sync_recv_info::cte_type
```

广播中的恒定音调扩展（Constant Tone Extension，CTE），参见 `bt_df_cte_type`。

<a id="a74f6dc1745a756faca2e323292024730"></a>

### `periodic_event_counter`

```c
uint16_t bt_le_per_adv_sync_recv_info::periodic_event_counter
```

接收子事件指示（Subevent indication）时的事件计数器值（Event counter）。

<a id="aa17c9d917469f121448ed4e1db485700"></a>

### `rssi`

```c
int8_t bt_le_per_adv_sync_recv_info::rssi
```

广播的接收信号强度指示（RSSI），不计任何恒定音调扩展（CTE），单位为 dBm。

范围（Range）：-127 至 +20。值不可用时，可设为 `BT_GAP_RSSI_INVALID`。

<a id="a21b0ca87e46c6897282ebd877e45114e"></a>

### `sid`

```c
uint8_t bt_le_per_adv_sync_recv_info::sid
```

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

<a id="a1a9dccd6d7592868b5604ec16a5f1540"></a>

### `subevent`

```c
uint8_t bt_le_per_adv_sync_recv_info::subevent
```

接收子事件指示（Subevent indication）所在的子事件。

<a id="a65f1a2adb7c3d740cb8262ae7f5a7c3e"></a>

### `tx_power`

```c
int8_t bt_le_per_adv_sync_recv_info::tx_power
```

广播的发射功率（TX power），单位为 dBm。

范围（Range）：-127 至 +20。值不可用时，可设为 `BT_GAP_TX_POWER_INVALID`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 121.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_GAP_SID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gacf05b7660d2ae85f64e2a220abf8e57d)
- [BT_GAP_SID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gafa6f803fe3ada07030fb1f2f725940c4)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [bt_df_cte_type](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_le_per_adv_sync_cb](P118_bt_le_per_adv_sync_cb_结构体.md)
- [BT_GAP_RSSI_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga64b5c5e429dadf1e875984f69cd399dc)
- [BT_GAP_TX_POWER_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga61ccce819d75313cb2ee58309ed4b275)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P120_bt_le_per_adv_sync_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P122_bt_le_per_adv_sync_state_info_结构体.md)
