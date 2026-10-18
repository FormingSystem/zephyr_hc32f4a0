---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-48
title: bt_df_per_adv_sync_iq_samples_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__per__adv__sync__iq__samples__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_bt\_df\_per\_adv\_sync\_iq\_samples\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__per__adv__sync__iq__samples__report.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/direction.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_ad4d213aa20a0c2fe329606ed789436fd"></a>

```c
uint8_t chan_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[chan_idx](#ad4d213aa20a0c2fe329606ed789436fd)。

接收含有被采样恒定音调扩展（CTE）的协议数据单元（PDU）时使用的信道索引（Channel index）。

<a id="r_a48793aad0f603d1763f06453e837a9d9"></a>

```c
int16_t rssi
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rssi](#a48793aad0f603d1763f06453e837a9d9)。

携带恒定音调扩展（CTE）的协议数据单元（PDU）的接收信号强度指示（RSSI），不计 CTE 部分。

<a id="r_a0b07042bad2a28065b8ea4def73c91d3"></a>

```c
uint8_t rssi_ant_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rssi_ant_id](#a0b07042bad2a28065b8ea4def73c91d3)。

用于测量接收信号强度指示（RSSI）的天线标识符（Antenna ID）。

<a id="r_aa81e74769290f427b60398eb976b4a2a"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#aa81e74769290f427b60398eb976b4a2a)。

恒定音调扩展类型（CTE type），参见 `bt_df_cte_type`。

<a id="r_ab256dc21c5d707a9195967caaa13e3e0"></a>

```c
uint8_t slot_durations
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[slot_durations](#ab256dc21c5d707a9195967caaa13e3e0)。

所接收的恒定音调扩展（CTE）类型为到达角（AoA）时的时隙持续时间（Slot duration），参见 `bt_df_antenna_switching_slot`。

<a id="r_a6fea28c1d3b00f1fd7bcb7264f4c3fc9"></a>

```c
uint8_t packet_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_status](#a6fea28c1d3b00f1fd7bcb7264f4c3fc9)。

所接收的携带恒定音调扩展（CTE）的协议数据单元（PDU）的状态，参见 `bt_df_packet_status`。

<a id="r_a1a9c763fa7dd445b5dea8c2bb7b82bc0"></a>

```c
uint16_t per_evt_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[per_evt_counter](#a1a9c763fa7dd445b5dea8c2bb7b82bc0)。

`AUX_SYNC_IND` 协议数据单元（PDU）的 `paEventCounter` 值。

<a id="r_a4d1da7208e043f5ae015612cee16ee25"></a>

```c
uint8_t sample_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sample_count](#a4d1da7208e043f5ae015612cee16ee25)。

报告中的同相／正交样本数量（IQ sample count）。

<a id="r_a88d950cdaa4f08a0fa3eb26f1fed7982"></a>

```c
enum bt_df_iq_sample sample_type
```

相关声明：[bt_df_iq_sample](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a53df7da4b178b4a6e4dd68e9266c0771)、[sample_type](#a88d950cdaa4f08a0fa3eb26f1fed7982)。

报告中提供的同相／正交样本类型（IQ sample type）。

```c
union {
```

<a id="r_a35d5a96aa5f72f2b9592e37aa4b91dfc"></a>

```c
struct bt_hci_le_iq_sample const * sample
```

相关声明：[bt_hci_le_iq_sample](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md)、[sample](#a64c2936dc8180fc34651b18199241a9b)。

<a id="r_af2562aec0427036c28c40764df869901"></a>

```c
struct bt_hci_le_iq_sample16 const * sample16
```

相关声明：[bt_hci_le_iq_sample16](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md)、[sample16](#ae0a28844a5588af05bbde046f6355ddf)。

<a id="r_a16a70bd3a0045227e6de26f86231243b"></a>

```c
};
```

指向同相／正交样本数据（IQ sample data）的指针。

## 48.2\_详细说明（Detailed Documentation）

<a id="a16a70bd3a0045227e6de26f86231243b"></a>

### `[union]`

```c
union { ... } bt_df_per_adv_sync_iq_samples_report
```

指向同相／正交样本数据（IQ sample data）的指针。

<a id="ad4d213aa20a0c2fe329606ed789436fd"></a>

### `chan_idx`

```c
uint8_t bt_df_per_adv_sync_iq_samples_report::chan_idx
```

接收含有被采样恒定音调扩展（CTE）的协议数据单元（PDU）时使用的信道索引（Channel index）。

<a id="aa81e74769290f427b60398eb976b4a2a"></a>

### `cte_type`

```c
uint8_t bt_df_per_adv_sync_iq_samples_report::cte_type
```

恒定音调扩展类型（CTE type），参见 `bt_df_cte_type`。

<a id="a6fea28c1d3b00f1fd7bcb7264f4c3fc9"></a>

### `packet_status`

```c
uint8_t bt_df_per_adv_sync_iq_samples_report::packet_status
```

所接收的携带恒定音调扩展（CTE）的协议数据单元（PDU）的状态，参见 `bt_df_packet_status`。

<a id="a1a9c763fa7dd445b5dea8c2bb7b82bc0"></a>

### `per_evt_counter`

```c
uint16_t bt_df_per_adv_sync_iq_samples_report::per_evt_counter
```

`AUX_SYNC_IND` 协议数据单元（PDU）的 `paEventCounter` 值。

<a id="a48793aad0f603d1763f06453e837a9d9"></a>

### `rssi`

```c
int16_t bt_df_per_adv_sync_iq_samples_report::rssi
```

携带恒定音调扩展（CTE）的协议数据单元（PDU）的接收信号强度指示（RSSI），不计 CTE 部分。

范围（Range）：-1270 至 +200；单位（Units）：0.1 dBm。

<a id="a0b07042bad2a28065b8ea4def73c91d3"></a>

### `rssi_ant_id`

```c
uint8_t bt_df_per_adv_sync_iq_samples_report::rssi_ant_id
```

用于测量接收信号强度指示（RSSI）的天线标识符（Antenna ID）。

<a id="a64c2936dc8180fc34651b18199241a9b"></a>

### `sample`

```c
struct bt_hci_le_iq_sample const* bt_df_per_adv_sync_iq_samples_report::sample
```

<a id="ae0a28844a5588af05bbde046f6355ddf"></a>

### `sample16`

```c
struct bt_hci_le_iq_sample16 const* bt_df_per_adv_sync_iq_samples_report::sample16
```

<a id="a4d1da7208e043f5ae015612cee16ee25"></a>

### `sample_count`

```c
uint8_t bt_df_per_adv_sync_iq_samples_report::sample_count
```

报告中的同相／正交样本数量（IQ sample count）。

<a id="a88d950cdaa4f08a0fa3eb26f1fed7982"></a>

### `sample_type`

```c
enum bt_df_iq_sample bt_df_per_adv_sync_iq_samples_report::sample_type
```

报告中提供的同相／正交样本类型（IQ sample type）。

<a id="ab256dc21c5d707a9195967caaa13e3e0"></a>

### `slot_durations`

```c
uint8_t bt_df_per_adv_sync_iq_samples_report::slot_durations
```

所接收的恒定音调扩展（CTE）类型为到达角（AoA）时的时隙持续时间（Slot duration），参见 `bt_df_antenna_switching_slot`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/direction.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/direction.h](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_df_cte_type](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05)
- [bt_df_antenna_switching_slot](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a546598ce9a81161ad1ba098a7b1a8df4)
- [bt_df_packet_status](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#ab9acadbaf03dd976a2ee185574effb4c)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_df_iq_sample](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a53df7da4b178b4a6e4dd68e9266c0771)
- [bt_hci_le_iq_sample](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md)
- [bt_hci_le_iq_sample16](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md)
- [bt_df_per_adv_sync_iq_samples_report](P048_bt_df_per_adv_sync_iq_samples_report_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_bt_df_per_adv_sync_cte_rx_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_bt_gatt_attr_结构体.md)
