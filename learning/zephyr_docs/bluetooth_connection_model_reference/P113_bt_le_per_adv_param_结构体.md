---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-113
title: bt_le_per_adv_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第113章\_bt\_le\_per\_adv\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

配置周期广播（Periodic Advertising）的参数。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

周期广播配置参数（Periodic advertising configuration parameters）。用于配置最小和最大广播间隔、选项，以及在支持周期广播响应时使用的子事件设置。间隔以 1.25 毫秒为单位；选项字段（Options）可修改其他广播行为。扩展广播器可以通过此结构设置或更新周期广播参数。部分参数仅在设备支持周期广播响应时适用，该支持由 `CONFIG_BT_PER_ADV_RSP` 配置。注意（Note）：用于 `bt_le_per_adv_set_param` 函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 113.1\_数据成员（Data Fields）

<a id="r_a49da44a3c0e4e866ffccffae5a9a22f7"></a>

```c
uint16_t interval_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_min](#a49da44a3c0e4e866ffccffae5a9a22f7)。

最小周期广播间隔（Minimum Periodic Advertising Interval），为 N × 1.25 毫秒。

<a id="r_a61308cfe72ad23372dfd2a3bd2550726"></a>

```c
uint16_t interval_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_max](#a61308cfe72ad23372dfd2a3bd2550726)。

最大周期广播间隔（Maximum Periodic Advertising Interval），为 N × 1.25 毫秒。

<a id="r_a9b80c2427171920f466601e7e8468814"></a>

```c
uint32_t options
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[options](#a9b80c2427171920f466601e7e8468814)。

周期广播选项位域（Periodic advertising options bit-field），参见 `bt_le_per_adv_opt` 字段。

<a id="r_af8be989979c98a17828819ec43dd0b49"></a>

```c
uint8_t num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subevents](#af8be989979c98a17828819ec43dd0b49)。

子事件数量（Number of Subevents）。

<a id="r_a28655741c63775a274c42ad5057d4a1d"></a>

```c
uint8_t subevent_interval
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_interval](#a28655741c63775a274c42ad5057d4a1d)。

子事件间隔（Subevent interval），为 N × 1.25 毫秒。

<a id="r_a07302e13735f502b8950a92b365ef14a"></a>

```c
uint8_t response_slot_delay
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_delay](#a07302e13735f502b8950a92b365ef14a)。

子事件中的广播数据包与第一个响应时隙（Response slot）之间的时间，为 N × 1.25 毫秒。

<a id="r_a67116b81e8ce968cf411843646801ac4"></a>

```c
uint8_t response_slot_spacing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_spacing](#a67116b81e8ce968cf411843646801ac4)。

响应时隙之间的时间（Response slot spacing），为 N × 0.125 毫秒。

<a id="r_a0a8606c103fd91f3222bae6c9f1204fd"></a>

```c
uint8_t num_response_slots
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_response_slots](#a0a8606c103fd91f3222bae6c9f1204fd)。

子事件响应时隙数量（Subevent response slots）。

## 113.2\_详细说明（Detailed Documentation）

<a id="a61308cfe72ad23372dfd2a3bd2550726"></a>

### `interval_max`

```c
uint16_t bt_le_per_adv_param::interval_max
```

最大周期广播间隔（Maximum Periodic Advertising Interval），为 N × 1.25 毫秒。

必须小于或等于 `BT_GAP_PER_ADV_MAX_INTERVAL`，且大于或等于 `interval_min`。

<a id="a49da44a3c0e4e866ffccffae5a9a22f7"></a>

### `interval_min`

```c
uint16_t bt_le_per_adv_param::interval_min
```

最小周期广播间隔（Minimum Periodic Advertising Interval），为 N × 1.25 毫秒。

必须大于或等于 `BT_GAP_PER_ADV_MIN_INTERVAL`，且小于或等于 `interval_max`。

<a id="a0a8606c103fd91f3222bae6c9f1204fd"></a>

### `num_response_slots`

```c
uint8_t bt_le_per_adv_param::num_response_slots
```

子事件响应时隙数量（Subevent response slots）。

为零时，忽略 `response_slot_delay` 和 `response_slot_spacing`。

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_PER_ADV_RSP` 时可用。

<a id="af8be989979c98a17828819ec43dd0b49"></a>

### `num_subevents`

```c
uint8_t bt_le_per_adv_param::num_subevents
```

子事件数量（Number of Subevents）。

为零时，周期广播器（Periodic advertiser）将作为不接收响应的广播方（Broadcaster）。

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_PER_ADV_RSP` 时可用。

<a id="a9b80c2427171920f466601e7e8468814"></a>

### `options`

```c
uint32_t bt_le_per_adv_param::options
```

周期广播选项位域（Periodic advertising options bit-field），参见 `bt_le_per_adv_opt` 字段。

<a id="a07302e13735f502b8950a92b365ef14a"></a>

### `response_slot_delay`

```c
uint8_t bt_le_per_adv_param::response_slot_delay
```

子事件中的广播数据包与第一个响应时隙（Response slot）之间的时间，为 N × 1.25 毫秒。

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_PER_ADV_RSP` 时可用。

<a id="a67116b81e8ce968cf411843646801ac4"></a>

### `response_slot_spacing`

```c
uint8_t bt_le_per_adv_param::response_slot_spacing
```

响应时隙之间的时间（Response slot spacing），为 N × 0.125 毫秒。

必须在 0.25–31.875 毫秒之间。

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_PER_ADV_RSP` 时可用。

<a id="a28655741c63775a274c42ad5057d4a1d"></a>

### `subevent_interval`

```c
uint8_t bt_le_per_adv_param::subevent_interval
```

子事件间隔（Subevent interval），为 N × 1.25 毫秒。

必须在 7.5–318.75 毫秒之间。

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_PER_ADV_RSP` 时可用。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 113.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_le_per_adv_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae60a45dde6b4d9f4c54a2a6070254f11)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [CONFIG_BT_PER_ADV_RSP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_RSP)
- [bt_le_per_adv_set_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa72029a2759123ec776061d2e80bf3a1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P112_bt_le_per_adv_data_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P114_bt_le_per_adv_response_info_结构体.md)
