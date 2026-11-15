---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-92
title: bt_le_adv_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__adv__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第92章\_bt\_le\_adv\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__adv__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗蓝牙广播（LE Advertising）的参数。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

低功耗蓝牙广播（LE Advertising）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 92.1\_数据成员（Data Fields）

<a id="r_af957bd92b949536af2b2db0db7b2b425"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#af957bd92b949536af2b2db0db7b2b425)。

本地身份句柄（Local identity handle）。

<a id="r_a6e2f0e1b76495afe7fe661e8698d0909"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a6e2f0e1b76495afe7fe661e8698d0909)。

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

<a id="r_a9911e9bfc97ff0c48a6decae3f922e95"></a>

```c
uint8_t secondary_max_skip
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[secondary_max_skip](#a9911e9bfc97ff0c48a6decae3f922e95)。

次广播信道最大跳过次数（Secondary channel maximum skip count）。

<a id="r_a1c09c2bcf9600a644e194ecd3367d200"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a1c09c2bcf9600a644e194ecd3367d200)。

请求的发射功率（TX power），单位为 dBm。

<a id="r_a2a978c60153eb03697769bc72928f4ef"></a>

```c
uint32_t options
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[options](#a2a978c60153eb03697769bc72928f4ef)。

广播选项位域（Advertising options bit-field），参见 `bt_le_adv_opt` 字段。

<a id="r_aca8ff5a4f5d29184535162f007b2d39e"></a>

```c
uint32_t interval_min
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[interval_min](#aca8ff5a4f5d29184535162f007b2d39e)。

最小广播间隔（Minimum Advertising Interval），为 N × 0.625 毫秒。

<a id="r_afeba6973dca99d8ee818fdde0c22cb59"></a>

```c
uint32_t interval_max
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[interval_max](#afeba6973dca99d8ee818fdde0c22cb59)。

最大广播间隔（Maximum Advertising Interval），为 N × 0.625 毫秒。

<a id="r_a4cf31f54f067fffa3c848adc2ffd7119"></a>

```c
const bt_addr_le_t * peer
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer](#a4cf31f54f067fffa3c848adc2ffd7119)。

面向对等设备的定向广播（Directed advertising）。

## 92.2\_详细说明（Detailed Documentation）

<a id="af957bd92b949536af2b2db0db7b2b425"></a>

### `id`

```c
uint8_t bt_le_adv_param::id
```

本地身份句柄（Local identity handle）。

本地蓝牙控制器中的身份地址索引（Identity address index）。

**说明（Note）**：注意（Note）：未启用扩展广播 `CONFIG_BT_EXT_ADV`，或控制器不支持扩展广播时，不能使用两个不同的随机地址同时扫描与广播。

<a id="afeba6973dca99d8ee818fdde0c22cb59"></a>

### `interval_max`

```c
uint32_t bt_le_adv_param::interval_max
```

最大广播间隔（Maximum Advertising Interval），为 N × 0.625 毫秒。

最大广播间隔（Maximum Advertising Interval）必须大于或等于最小广播间隔。建议两者不要相等，以便控制器结合其他活动确定最佳广播间隔。传统广播（Legacy advertising）的范围为 `0x0020`–`0x4000`，参见蓝牙核心规范 6.2 第 4 卷 E 部分第 7.8.5 节；扩展广播（Extended advertising）的范围为 `0x0020`–`0xFFFFFF`，参见同规范第 7.8.53 节。

<a id="aca8ff5a4f5d29184535162f007b2d39e"></a>

### `interval_min`

```c
uint32_t bt_le_adv_param::interval_min
```

最小广播间隔（Minimum Advertising Interval），为 N × 0.625 毫秒。

最小广播间隔（Minimum Advertising Interval）必须小于或等于最大广播间隔。建议两者不要相等，以便控制器结合其他活动确定最佳广播间隔。传统广播（Legacy advertising）的范围为 `0x0020`–`0x4000`，参见蓝牙核心规范 6.2 第 4 卷 E 部分第 7.8.5 节；扩展广播（Extended advertising）的范围为 `0x0020`–`0xFFFFFF`，参见同规范第 7.8.53 节。

<a id="a2a978c60153eb03697769bc72928f4ef"></a>

### `options`

```c
uint32_t bt_le_adv_param::options
```

广播选项位域（Advertising options bit-field），参见 `bt_le_adv_opt` 字段。

<a id="a4cf31f54f067fffa3c848adc2ffd7119"></a>

### `peer`

```c
const bt_addr_le_t* bt_le_adv_param::peer
```

面向对等设备的定向广播（Directed advertising）。

设置此参数后，广播器（Advertiser）将向远端设备发送定向广播（Directed advertising）。

广播类型为高占空比（High duty cycle）；若启用 `BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY` 选项，则为低占空比（Low duty cycle）。使用 `BT_LE_ADV_OPT_EXT_ADV` 时，仅允许低占空比。

对于可连接高占空比广播（Connectable high duty cycle），若超时内未能建立连接，将调用 `connected` 回调，并将状态设为 `BT_HCI_ERR_ADV_TIMEOUT`。

<a id="a9911e9bfc97ff0c48a6decae3f922e95"></a>

### `secondary_max_skip`

```c
uint8_t bt_le_adv_param::secondary_max_skip
```

次广播信道最大跳过次数（Secondary channel maximum skip count）。

广播器在必须于次广播信道（Secondary advertising channel）发送广播数据之前，最多可跳过的广播事件数量。

**说明（Note）**：注意（Note）：要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。

<a id="a6e2f0e1b76495afe7fe661e8698d0909"></a>

### `sid`

```c
uint8_t bt_le_adv_param::sid
```

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

**说明（Note）**：注意（Note）：若 `options` 未设置 `BT_LE_ADV_OPT_EXT_ADV`，则忽略此字段。

<a id="a1c09c2bcf9600a644e194ecd3367d200"></a>

### `tx_power`

```c
int8_t bt_le_adv_param::tx_power
```

请求的发射功率（TX power），单位为 dBm。

仅在 `options` 中设置 `BT_LE_ADV_OPT_TX_POWER` 时使用。有效范围为 `BT_HCI_LE_ADV_TX_POWER_MIN` 至 `BT_HCI_LE_ADV_TX_POWER_MAX`。控制器选择最接近的受支持等级，并通过 `bt_le_ext_adv_info::tx_power` 报告实际值。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 92.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_GAP_SID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gacf05b7660d2ae85f64e2a220abf8e57d)
- [BT_GAP_SID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gafa6f803fe3ada07030fb1f2f725940c4)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_le_adv_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gafbf81dab68b0e484d4742471c722fc28)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [CONFIG_BT_EXT_ADV](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_EXT_ADV)
- [BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872)
- [BT_LE_ADV_OPT_EXT_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab)
- [BT_HCI_ERR_ADV_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#abfa408d8366ff3cae1cd35fffcda30c0)
- [BT_LE_ADV_OPT_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ab9ee87ad3a24312174ae46f904fe9c56)
- [BT_HCI_LE_ADV_TX_POWER_MIN](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#aa4ce6784e6ee46069fd109dc1869e716)
- [BT_HCI_LE_ADV_TX_POWER_MAX](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#aa3bfec7459966cf805afcf5186d53103)
- [bt_le_ext_adv_info::tx_power](P105_bt_le_ext_adv_info_结构体.md#a485e4a8124fddee897fe744836cbfb24)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P091_bt_iso_unicast_tx_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P093_bt_le_conn_param_结构体.md)
