---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-318
title: bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__1__ss__rtt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第318章\_bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__1__ss__rtt.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

子事件结果步骤数据格式：支持探测序列往返时间（Sounding Sequence RTT）的模式 1。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

子事件结果步骤数据格式：支持探测序列往返时间（Sounding Sequence RTT）的模式 1。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 318.1\_数据成员（Data Fields）

<a id="r_a515fde1d568a19ccf6ebefe9052866a4"></a>

```c
uint8_t packet_quality_bit_errors: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_bit_errors](#a515fde1d568a19ccf6ebefe9052866a4)。

<a id="r_ad8f9ca9dda852b435848b988ad872797"></a>

```c
uint8_t packet_quality_aa_check: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_aa_check](#ad8f9ca9dda852b435848b988ad872797)。

<a id="r_a511b281fb1c16fd7d0eaf731906a4292"></a>

```c
uint8_t packet_nadm
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_nadm](#a511b281fb1c16fd7d0eaf731906a4292)。

<a id="r_a5ec9c30063c09285804973008533e5cb"></a>

```c
uint8_t packet_rssi
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_rssi](#a5ec9c30063c09285804973008533e5cb)。

```c
union {
```

<a id="r_aa462db2eb0dbc3bd31cabf6edca4eaa1"></a>

```c
int16_t toa_tod_initiator
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[toa_tod_initiator](#a77bbcd9451360ad97813f9357e44766e)。

<a id="r_a044984dccf65a03098063d90f8b4d992"></a>

```c
int16_t tod_toa_reflector
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[tod_toa_reflector](#ace3843bc24616950f04150b2f86abad4)。

<a id="r_a799bedf4b1cdd92b38eb926ca7fb1ec5"></a>

```c
};
```

<a id="r_abf20351ab0eaf3a7139a464f1d1a72b0"></a>

```c
uint8_t packet_antenna
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_antenna](#abf20351ab0eaf3a7139a464f1d1a72b0)。

<a id="r_a3f8ba85b776f732ebc1086a4317849a1"></a>

```c
uint8_t packet_pct1 [4]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_pct1](#a3f8ba85b776f732ebc1086a4317849a1)。

<a id="r_a9f969aa6fc134a9e618d07f177d2b7fd"></a>

```c
uint8_t packet_pct2 [4]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_pct2](#a9f969aa6fc134a9e618d07f177d2b7fd)。

## 318.2\_详细说明（Detailed Documentation）

<a id="a799bedf4b1cdd92b38eb926ca7fb1ec5"></a>

### `[union]`

```c
union { ... } bt_hci_le_cs_step_data_mode_1_ss_rtt
```

<a id="abf20351ab0eaf3a7139a464f1d1a72b0"></a>

### `packet_antenna`

```c
uint8_t bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_antenna
```

<a id="a511b281fb1c16fd7d0eaf731906a4292"></a>

### `packet_nadm`

```c
uint8_t bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_nadm
```

<a id="a3f8ba85b776f732ebc1086a4317849a1"></a>

### `packet_pct1`

```c
uint8_t bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_pct1[4]
```

<a id="a9f969aa6fc134a9e618d07f177d2b7fd"></a>

### `packet_pct2`

```c
uint8_t bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_pct2[4]
```

<a id="ad8f9ca9dda852b435848b988ad872797"></a>

### `packet_quality_aa_check`

```c
uint8_t bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_quality_aa_check
```

<a id="a515fde1d568a19ccf6ebefe9052866a4"></a>

### `packet_quality_bit_errors`

```c
uint8_t bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_quality_bit_errors
```

<a id="a5ec9c30063c09285804973008533e5cb"></a>

### `packet_rssi`

```c
uint8_t bt_hci_le_cs_step_data_mode_1_ss_rtt::packet_rssi
```

<a id="a77bbcd9451360ad97813f9357e44766e"></a>

### `toa_tod_initiator`

```c
int16_t bt_hci_le_cs_step_data_mode_1_ss_rtt::toa_tod_initiator
```

<a id="ace3843bc24616950f04150b2f86abad4"></a>

### `tod_toa_reflector`

```c
int16_t bt_hci_le_cs_step_data_mode_1_ss_rtt::tod_toa_reflector
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 318.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt](P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P317_bt_hci_le_cs_step_data_mode_1_结构体.md) · [返回大纲](大纲.md) · [下一章](P319_bt_hci_le_cs_step_data_mode_2_结构体.md)
