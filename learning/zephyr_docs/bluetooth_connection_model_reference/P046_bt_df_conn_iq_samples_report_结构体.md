---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-46
title: bt_df_conn_iq_samples_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__conn__iq__samples__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_bt\_df\_conn\_iq\_samples\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__conn__iq__samples__report.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/direction.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_ab6e31e979bba969a18804cf8c9b88f03"></a>

```c
enum bt_df_conn_iq_report_err err
```

相关声明：[bt_df_conn_iq_report_err](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a953634e6a88617a8729541d6b5bd0dd6)、[err](#ab6e31e979bba969a18804cf8c9b88f03)。

报告接收失败原因（Report receive failure reason）。

<a id="r_ac14e792a3ce2f3297ddab49e801ba640"></a>

```c
uint8_t rx_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_phy](#ac14e792a3ce2f3297ddab49e801ba640)。

接收含有被采样恒定音调扩展（CTE）的协议数据单元（PDU）时使用的物理层（PHY）。

<a id="r_a9374ecd1437f532dec863c527d22348d"></a>

```c
uint8_t chan_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[chan_idx](#a9374ecd1437f532dec863c527d22348d)。

接收含有被采样恒定音调扩展（CTE）的协议数据单元（PDU）时使用的信道索引（Channel index）。

<a id="r_aac825fbdecd6a5a82da0097a8694fb65"></a>

```c
int16_t rssi
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rssi](#aac825fbdecd6a5a82da0097a8694fb65)。

携带恒定音调扩展（CTE）的协议数据单元（PDU）的接收信号强度指示（RSSI），不计 CTE 部分。

<a id="r_a7c5147b426bb87f9d11c8bdffb91ff02"></a>

```c
uint8_t rssi_ant_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rssi_ant_id](#a7c5147b426bb87f9d11c8bdffb91ff02)。

用于测量接收信号强度指示（RSSI）的天线标识符（Antenna ID）。

<a id="r_a4d467a7ac76dc9ed6331c10172895097"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a4d467a7ac76dc9ed6331c10172895097)。

恒定音调扩展类型（CTE type），参见 `bt_df_cte_type`。

<a id="r_a578132e4a88e739451cf80eba7345094"></a>

```c
uint8_t slot_durations
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[slot_durations](#a578132e4a88e739451cf80eba7345094)。

所接收的恒定音调扩展（CTE）类型为到达角（AoA）时的时隙持续时间（Slot duration），参见 `bt_df_antenna_switching_slot`。

<a id="r_afdc456a8af5a31ee62c489534af3ecdb"></a>

```c
uint8_t packet_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_status](#afdc456a8af5a31ee62c489534af3ecdb)。

所接收的携带恒定音调扩展（CTE）的协议数据单元（PDU）的状态，参见 `bt_df_packet_status`。

<a id="r_ac7f3993bd20bd44354f15f098e423c33"></a>

```c
uint16_t conn_evt_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_evt_counter](#ac7f3993bd20bd44354f15f098e423c33)。

接收并采样恒定音调扩展（CTE）时的连接事件计数器值（Connection event counter）。

<a id="r_a1e7901b81c8618e4515cd22a681b4d43"></a>

```c
enum bt_df_iq_sample sample_type
```

相关声明：[bt_df_iq_sample](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a53df7da4b178b4a6e4dd68e9266c0771)、[sample_type](#a1e7901b81c8618e4515cd22a681b4d43)。

报告中提供的同相／正交样本类型（IQ sample type）。

<a id="r_a60500e954e2694a209c2d103887b2685"></a>

```c
uint8_t sample_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sample_count](#a60500e954e2694a209c2d103887b2685)。

报告中的同相／正交样本数量（IQ sample count）。

```c
union {
```

<a id="r_a2bd2414ffb95b0b82bf24be8ef0ffc1e"></a>

```c
struct bt_hci_le_iq_sample const * sample
```

相关声明：[bt_hci_le_iq_sample](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md)、[sample](#aa9b177817075e3781256ec2c7d5ac0ce)。

<a id="r_acf9a193cfd8f7ddc6d252077069eccc6"></a>

```c
struct bt_hci_le_iq_sample16 const * sample16
```

相关声明：[bt_hci_le_iq_sample16](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md)、[sample16](#a55e1d7d31557f0e1f59ad91834460b78)。

<a id="r_af3635455cf6b195ba28afd7c1464829a"></a>

```c
};
```

指向同相／正交样本数据（IQ sample data）的指针。

## 46.2\_详细说明（Detailed Documentation）

<a id="af3635455cf6b195ba28afd7c1464829a"></a>

### `[union]`

```c
union { ... } bt_df_conn_iq_samples_report
```

指向同相／正交样本数据（IQ sample data）的指针。

<a id="a9374ecd1437f532dec863c527d22348d"></a>

### `chan_idx`

```c
uint8_t bt_df_conn_iq_samples_report::chan_idx
```

接收含有被采样恒定音调扩展（CTE）的协议数据单元（PDU）时使用的信道索引（Channel index）。

<a id="ac7f3993bd20bd44354f15f098e423c33"></a>

### `conn_evt_counter`

```c
uint16_t bt_df_conn_iq_samples_report::conn_evt_counter
```

接收并采样恒定音调扩展（CTE）时的连接事件计数器值（Connection event counter）。

<a id="a4d467a7ac76dc9ed6331c10172895097"></a>

### `cte_type`

```c
uint8_t bt_df_conn_iq_samples_report::cte_type
```

恒定音调扩展类型（CTE type），参见 `bt_df_cte_type`。

<a id="ab6e31e979bba969a18804cf8c9b88f03"></a>

### `err`

```c
enum bt_df_conn_iq_report_err bt_df_conn_iq_samples_report::err
```

报告接收失败原因（Report receive failure reason）。

<a id="afdc456a8af5a31ee62c489534af3ecdb"></a>

### `packet_status`

```c
uint8_t bt_df_conn_iq_samples_report::packet_status
```

所接收的携带恒定音调扩展（CTE）的协议数据单元（PDU）的状态，参见 `bt_df_packet_status`。

<a id="aac825fbdecd6a5a82da0097a8694fb65"></a>

### `rssi`

```c
int16_t bt_df_conn_iq_samples_report::rssi
```

携带恒定音调扩展（CTE）的协议数据单元（PDU）的接收信号强度指示（RSSI），不计 CTE 部分。

范围（Range）：-1270 至 +200；单位（Units）：0.1 dBm。

<a id="a7c5147b426bb87f9d11c8bdffb91ff02"></a>

### `rssi_ant_id`

```c
uint8_t bt_df_conn_iq_samples_report::rssi_ant_id
```

用于测量接收信号强度指示（RSSI）的天线标识符（Antenna ID）。

<a id="ac14e792a3ce2f3297ddab49e801ba640"></a>

### `rx_phy`

```c
uint8_t bt_df_conn_iq_samples_report::rx_phy
```

接收含有被采样恒定音调扩展（CTE）的协议数据单元（PDU）时使用的物理层（PHY）。

<a id="aa9b177817075e3781256ec2c7d5ac0ce"></a>

### `sample`

```c
struct bt_hci_le_iq_sample const* bt_df_conn_iq_samples_report::sample
```

<a id="a55e1d7d31557f0e1f59ad91834460b78"></a>

### `sample16`

```c
struct bt_hci_le_iq_sample16 const* bt_df_conn_iq_samples_report::sample16
```

<a id="a60500e954e2694a209c2d103887b2685"></a>

### `sample_count`

```c
uint8_t bt_df_conn_iq_samples_report::sample_count
```

报告中的同相／正交样本数量（IQ sample count）。

<a id="a1e7901b81c8618e4515cd22a681b4d43"></a>

### `sample_type`

```c
enum bt_df_iq_sample bt_df_conn_iq_samples_report::sample_type
```

报告中提供的同相／正交样本类型（IQ sample type）。

<a id="a578132e4a88e739451cf80eba7345094"></a>

### `slot_durations`

```c
uint8_t bt_df_conn_iq_samples_report::slot_durations
```

所接收的恒定音调扩展（CTE）类型为到达角（AoA）时的时隙持续时间（Slot duration），参见 `bt_df_antenna_switching_slot`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/direction.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/direction.h](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h_source.html)
- [bt_df_conn_iq_report_err](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a953634e6a88617a8729541d6b5bd0dd6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_df_cte_type](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05)
- [bt_df_antenna_switching_slot](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a546598ce9a81161ad1ba098a7b1a8df4)
- [bt_df_packet_status](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#ab9acadbaf03dd976a2ee185574effb4c)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_df_iq_sample](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a53df7da4b178b4a6e4dd68e9266c0771)
- [bt_hci_le_iq_sample](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md)
- [bt_hci_le_iq_sample16](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md)
- [bt_df_conn_iq_samples_report](P046_bt_df_conn_iq_samples_report_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_bt_df_conn_cte_tx_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_bt_df_per_adv_sync_cte_rx_param_结构体.md)
