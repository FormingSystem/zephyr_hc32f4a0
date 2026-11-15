---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-321
title: bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__3__ss__rtt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第321章\_bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__3__ss__rtt.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

子事件结果步骤数据格式：支持探测序列往返时间（Sounding Sequence RTT）的模式 3。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

子事件结果步骤数据格式：支持探测序列往返时间（Sounding Sequence RTT）的模式 3。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 321.1\_数据成员（Data Fields）

<a id="r_af5d8a8559400b45066bdac86fbdac411"></a>

```c
uint8_t packet_quality_bit_errors: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_bit_errors](#af5d8a8559400b45066bdac86fbdac411)。

<a id="r_a657ec3570e3ad6b2ddab87bada231587"></a>

```c
uint8_t packet_quality_aa_check: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_aa_check](#a657ec3570e3ad6b2ddab87bada231587)。

<a id="r_a9d2428083c401d931520addde0af54fd"></a>

```c
uint8_t packet_nadm
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_nadm](#a9d2428083c401d931520addde0af54fd)。

<a id="r_adc4fe32bc6b7515e5bf1055f19f1a2bd"></a>

```c
uint8_t packet_rssi
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_rssi](#adc4fe32bc6b7515e5bf1055f19f1a2bd)。

```c
union {
```

<a id="r_a5ca94d3d04f51f78e2c9627eac007edd"></a>

```c
int16_t toa_tod_initiator
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[toa_tod_initiator](#ae2181a568ed6da32d3f60ba6d271c64f)。

<a id="r_a942490e620cb5ca6c1723eab637f4253"></a>

```c
int16_t tod_toa_reflector
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[tod_toa_reflector](#ada4d52f54f1efa804a812c65edd8f125)。

<a id="r_ac112c9cad8388984ccd6e83ca4457b4e"></a>

```c
};
```

<a id="r_a9ce412ad8b18a9315b858cf1fe2a466a"></a>

```c
uint8_t packet_antenna
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_antenna](#a9ce412ad8b18a9315b858cf1fe2a466a)。

<a id="r_aada8b3ff1bb0d0b9eccb846da173b3f4"></a>

```c
uint8_t packet_pct1 [4]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_pct1](#aada8b3ff1bb0d0b9eccb846da173b3f4)。

<a id="r_afdebbafc06475dde12aaed73d2180f96"></a>

```c
uint8_t packet_pct2 [4]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_pct2](#afdebbafc06475dde12aaed73d2180f96)。

<a id="r_ac4067e27caa12cf9f8c6525bf6a72973"></a>

```c
uint8_t antenna_permutation_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[antenna_permutation_index](#ac4067e27caa12cf9f8c6525bf6a72973)。

<a id="r_aea13fc3e16092dcede9fb46ea719f21c"></a>

```c
struct bt_hci_le_cs_step_data_tone_info tone_info []
```

相关声明：[bt_hci_le_cs_step_data_tone_info](P322_bt_hci_le_cs_step_data_tone_info_结构体.md)、[tone_info](#aea13fc3e16092dcede9fb46ea719f21c)。

## 321.2\_详细说明（Detailed Documentation）

<a id="ac112c9cad8388984ccd6e83ca4457b4e"></a>

### `[union]`

```c
union { ... } bt_hci_le_cs_step_data_mode_3_ss_rtt
```

<a id="ac4067e27caa12cf9f8c6525bf6a72973"></a>

### `antenna_permutation_index`

```c
uint8_t bt_hci_le_cs_step_data_mode_3_ss_rtt::antenna_permutation_index
```

<a id="a9ce412ad8b18a9315b858cf1fe2a466a"></a>

### `packet_antenna`

```c
uint8_t bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_antenna
```

<a id="a9d2428083c401d931520addde0af54fd"></a>

### `packet_nadm`

```c
uint8_t bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_nadm
```

<a id="aada8b3ff1bb0d0b9eccb846da173b3f4"></a>

### `packet_pct1`

```c
uint8_t bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_pct1[4]
```

<a id="afdebbafc06475dde12aaed73d2180f96"></a>

### `packet_pct2`

```c
uint8_t bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_pct2[4]
```

<a id="a657ec3570e3ad6b2ddab87bada231587"></a>

### `packet_quality_aa_check`

```c
uint8_t bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_quality_aa_check
```

<a id="af5d8a8559400b45066bdac86fbdac411"></a>

### `packet_quality_bit_errors`

```c
uint8_t bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_quality_bit_errors
```

<a id="adc4fe32bc6b7515e5bf1055f19f1a2bd"></a>

### `packet_rssi`

```c
uint8_t bt_hci_le_cs_step_data_mode_3_ss_rtt::packet_rssi
```

<a id="ae2181a568ed6da32d3f60ba6d271c64f"></a>

### `toa_tod_initiator`

```c
int16_t bt_hci_le_cs_step_data_mode_3_ss_rtt::toa_tod_initiator
```

<a id="ada4d52f54f1efa804a812c65edd8f125"></a>

### `tod_toa_reflector`

```c
int16_t bt_hci_le_cs_step_data_mode_3_ss_rtt::tod_toa_reflector
```

<a id="aea13fc3e16092dcede9fb46ea719f21c"></a>

### `tone_info`

```c
struct bt_hci_le_cs_step_data_tone_info bt_hci_le_cs_step_data_mode_3_ss_rtt::tone_info[]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 321.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_hci_le_cs_step_data_tone_info](P322_bt_hci_le_cs_step_data_tone_info_结构体.md)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt](P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P320_bt_hci_le_cs_step_data_mode_3_结构体.md) · [返回大纲](大纲.md) · [下一章](P322_bt_hci_le_cs_step_data_tone_info_结构体.md)
