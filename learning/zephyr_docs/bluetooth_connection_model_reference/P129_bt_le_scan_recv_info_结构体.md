---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-129
title: bt_le_scan_recv_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__scan__recv__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第129章\_bt\_le\_scan\_recv\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__scan__recv__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗蓝牙（LE）广播包与扫描响应包的信息。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

低功耗蓝牙（LE）广播包与扫描响应包的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 129.1\_数据成员（Data Fields）

<a id="r_a907fb7ec3c78d68da5015a8c3afc3084"></a>

```c
const bt_addr_le_t * addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a907fb7ec3c78d68da5015a8c3afc3084)。

广播器的低功耗地址及类型（Advertiser LE address and type）。

<a id="r_a4df8d4e1fdd7514d170744856ebe7015"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a4df8d4e1fdd7514d170744856ebe7015)。

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

<a id="r_a88f677733147245ccbf861c7fc5e0f11"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#a88f677733147245ccbf861c7fc5e0f11)。

广播器信号强度（Advertiser signal strength），单位为 dBm。

<a id="r_a2addeba6d2ec8e55dc5379adf6519148"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a2addeba6d2ec8e55dc5379adf6519148)。

广播器发射功率（Transmit power），单位为 dBm。

<a id="r_adccb2ce5c6d228bd7f8f050088629524"></a>

```c
uint8_t adv_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_type](#adccb2ce5c6d228bd7f8f050088629524)。

广播数据包类型（Advertising packet type）。

<a id="r_af29ddfb59e286af9ca465cbd5a91bf2d"></a>

```c
uint16_t adv_props
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[adv_props](#af29ddfb59e286af9ca465cbd5a91bf2d)。

广播数据包属性位域（Advertising packet properties bitfield）。

<a id="r_a1060c5937708ff81a64f068e02fc7826"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a1060c5937708ff81a64f068e02fc7826)。

周期广播间隔（Periodic advertising interval），为 N × 1.25 毫秒。

<a id="r_a6189ed8453cb7907f34dc7dfaf1343bd"></a>

```c
uint8_t primary_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[primary_phy](#a6189ed8453cb7907f34dc7dfaf1343bd)。

主广播信道物理层（Primary advertising channel PHY）。

<a id="r_ac797291291dc7ba7ac171ed7f24f0d16"></a>

```c
uint8_t secondary_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[secondary_phy](#ac797291291dc7ba7ac171ed7f24f0d16)。

次广播信道物理层（Secondary advertising channel PHY）。

<a id="r_a8885283f39e3ece5d7ff7d5b5d588696"></a>

```c
const bt_addr_le_t * direct_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[direct_addr](#a8885283f39e3ece5d7ff7d5b5d588696)。

定向广播（Directed advertisement）的目标地址。

## 129.2\_详细说明（Detailed Documentation）

<a id="a907fb7ec3c78d68da5015a8c3afc3084"></a>

### `addr`

```c
const bt_addr_le_t* bt_le_scan_recv_info::addr
```

广播器的低功耗地址及类型（Advertiser LE address and type）。

广播器为匿名广播器（Anonymous advertiser）时，此地址为 `BT_ADDR_LE_ANY`。

<a id="af29ddfb59e286af9ca465cbd5a91bf2d"></a>

### `adv_props`

```c
uint16_t bt_le_scan_recv_info::adv_props
```

广播数据包属性位域（Advertising packet properties bitfield）。

使用 `bt_gap_adv_prop` 的取值。如果该值包含 `BT_GAP_ADV_PROP_SCAN_RESPONSE` 位，则表示这是扫描响应（Scan response）。

<a id="adccb2ce5c6d228bd7f8f050088629524"></a>

### `adv_type`

```c
uint8_t bt_le_scan_recv_info::adv_type
```

广播数据包类型（Advertising packet type）。

使用 `bt_gap_adv_type` 的取值。

若类型为 `BT_GAP_ADV_TYPE_SCAN_RSP`，则表示这是扫描响应（Scan response）。

<a id="a8885283f39e3ece5d7ff7d5b5d588696"></a>

### `direct_addr`

```c
const bt_addr_le_t* bt_le_scan_recv_info::direct_addr
```

定向广播（Directed advertisement）的目标地址。

报告不携带目标地址（Target address）时为 `NULL`。广播是否为定向广播，由 `bt_le_scan_recv_info::adv_props` 中的 `BT_GAP_ADV_PROP_DIRECTED` 指示。

低功耗扩展广播报告（LE Extended Advertising Report）始终携带定向广播的目标地址，无论控制器是否解析了该地址。低功耗广播报告（LE Advertising Report）没有目标地址字段，因此使用传统扫描命令时，对于控制器已解析的定向广播，此项为 `NULL`。

控制器无法解析地址时，地址类型为 `BT_ADDR_LE_UNRESOLVED`。

<a id="a1060c5937708ff81a64f068e02fc7826"></a>

### `interval`

```c
uint16_t bt_le_scan_recv_info::interval
```

周期广播间隔（Periodic advertising interval），为 N × 1.25 毫秒。

为 `0` 时表示没有周期广播（Periodic advertising）。

<a id="a6189ed8453cb7907f34dc7dfaf1343bd"></a>

### `primary_phy`

```c
uint8_t bt_le_scan_recv_info::primary_phy
```

主广播信道物理层（Primary advertising channel PHY）。

<a id="a88f677733147245ccbf861c7fc5e0f11"></a>

### `rssi`

```c
int8_t bt_le_scan_recv_info::rssi
```

广播器信号强度（Advertiser signal strength），单位为 dBm。

范围（Range）：-127 至 +20。值不可用时，可设为 `BT_GAP_RSSI_INVALID`。

<a id="ac797291291dc7ba7ac171ed7f24f0d16"></a>

### `secondary_phy`

```c
uint8_t bt_le_scan_recv_info::secondary_phy
```

次广播信道物理层（Secondary advertising channel PHY）。

<a id="a4df8d4e1fdd7514d170744856ebe7015"></a>

### `sid`

```c
uint8_t bt_le_scan_recv_info::sid
```

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

<a id="a2addeba6d2ec8e55dc5379adf6519148"></a>

### `tx_power`

```c
int8_t bt_le_scan_recv_info::tx_power
```

广播器发射功率（Transmit power），单位为 dBm。

范围（Range）：-127 至 +20。值不可用时，可设为 `BT_GAP_TX_POWER_INVALID`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 129.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_GAP_SID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gacf05b7660d2ae85f64e2a220abf8e57d)
- [BT_GAP_SID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gafa6f803fe3ada07030fb1f2f725940c4)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_ADDR_LE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga17e9efacd50c682b2f709c217e920d48)
- [bt_gap_adv_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga8ac9dd875bc7480929b5166193c621d0)
- [BT_GAP_ADV_PROP_SCAN_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0a55258ac9a7b355db87aeec5d443718f7)
- [bt_gap_adv_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga07833ed1f79708d5f6a5d0c2e01d4dca)
- [BT_GAP_ADV_TYPE_SCAN_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga07833ed1f79708d5f6a5d0c2e01d4dcaa5387de0177d3a9da9fd0c44ca30c7018)
- [BT_GAP_ADV_PROP_DIRECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga8ac9dd875bc7480929b5166193c621d0a4595d3a3ea30bd4cd51ba4f1c4ab7de9)
- [BT_ADDR_LE_UNRESOLVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gad02c40564a140300efda28ecb15674be)
- [BT_GAP_RSSI_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga64b5c5e429dadf1e875984f69cd399dc)
- [BT_GAP_TX_POWER_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga61ccce819d75313cb2ee58309ed4b275)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P128_bt_le_scan_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P130_bt_security_info_结构体.md)
