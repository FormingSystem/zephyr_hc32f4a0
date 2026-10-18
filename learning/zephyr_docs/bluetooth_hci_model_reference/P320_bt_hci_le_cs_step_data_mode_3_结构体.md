---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-320
title: bt_hci_le_cs_step_data_mode_3_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__3.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第320章\_bt\_hci\_le\_cs\_step\_data\_mode\_3\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__3.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

子事件结果步骤数据格式：模式 3。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

子事件结果步骤数据格式：模式 3。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 320.1\_数据成员（Data Fields）

<a id="r_a42b8bdf1fd492be1daded674e3d733d6"></a>

```c
uint8_t packet_quality_bit_errors: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_bit_errors](#a42b8bdf1fd492be1daded674e3d733d6)。

<a id="r_ad4c30784cc2586b5b8dcfa22e7a1f8fb"></a>

```c
uint8_t packet_quality_aa_check: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_aa_check](#ad4c30784cc2586b5b8dcfa22e7a1f8fb)。

<a id="r_a9b7373e7d3faa0cb5553d4f897c94ebc"></a>

```c
uint8_t packet_nadm
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_nadm](#a9b7373e7d3faa0cb5553d4f897c94ebc)。

<a id="r_a60750ac38bf019a0c7a8656ca59fc402"></a>

```c
uint8_t packet_rssi
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_rssi](#a60750ac38bf019a0c7a8656ca59fc402)。

```c
union {
```

<a id="r_ad910ae22fd9faa3358bdfb2b968fc04e"></a>

```c
int16_t toa_tod_initiator
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[toa_tod_initiator](#a183f3ee64a4482c9d3e0f041151fdcf9)。

<a id="r_a5648ec90403c31f403dba6832e937d52"></a>

```c
int16_t tod_toa_reflector
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[tod_toa_reflector](#aa0f1918115a6e550d6fab17529bbb4f2)。

<a id="r_a9ad06cb8bcbae12253a6aead552d2a82"></a>

```c
};
```

<a id="r_ad20e9c1deba67aa5759881b52d13311d"></a>

```c
uint8_t packet_antenna
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_antenna](#ad20e9c1deba67aa5759881b52d13311d)。

<a id="r_a609102fc9d42fe73c09907f54526bd40"></a>

```c
uint8_t antenna_permutation_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[antenna_permutation_index](#a609102fc9d42fe73c09907f54526bd40)。

<a id="r_a9ae78aa83a22f0618491871d55f2f0b9"></a>

```c
struct bt_hci_le_cs_step_data_tone_info tone_info []
```

相关声明：[bt_hci_le_cs_step_data_tone_info](P322_bt_hci_le_cs_step_data_tone_info_结构体.md)、[tone_info](#a9ae78aa83a22f0618491871d55f2f0b9)。

## 320.2\_详细说明（Detailed Documentation）

<a id="a9ad06cb8bcbae12253a6aead552d2a82"></a>

### `[union]`

```c
union { ... } bt_hci_le_cs_step_data_mode_3
```

<a id="a609102fc9d42fe73c09907f54526bd40"></a>

### `antenna_permutation_index`

```c
uint8_t bt_hci_le_cs_step_data_mode_3::antenna_permutation_index
```

<a id="ad20e9c1deba67aa5759881b52d13311d"></a>

### `packet_antenna`

```c
uint8_t bt_hci_le_cs_step_data_mode_3::packet_antenna
```

<a id="a9b7373e7d3faa0cb5553d4f897c94ebc"></a>

### `packet_nadm`

```c
uint8_t bt_hci_le_cs_step_data_mode_3::packet_nadm
```

<a id="ad4c30784cc2586b5b8dcfa22e7a1f8fb"></a>

### `packet_quality_aa_check`

```c
uint8_t bt_hci_le_cs_step_data_mode_3::packet_quality_aa_check
```

<a id="a42b8bdf1fd492be1daded674e3d733d6"></a>

### `packet_quality_bit_errors`

```c
uint8_t bt_hci_le_cs_step_data_mode_3::packet_quality_bit_errors
```

<a id="a60750ac38bf019a0c7a8656ca59fc402"></a>

### `packet_rssi`

```c
uint8_t bt_hci_le_cs_step_data_mode_3::packet_rssi
```

<a id="a183f3ee64a4482c9d3e0f041151fdcf9"></a>

### `toa_tod_initiator`

```c
int16_t bt_hci_le_cs_step_data_mode_3::toa_tod_initiator
```

<a id="aa0f1918115a6e550d6fab17529bbb4f2"></a>

### `tod_toa_reflector`

```c
int16_t bt_hci_le_cs_step_data_mode_3::tod_toa_reflector
```

<a id="a9ae78aa83a22f0618491871d55f2f0b9"></a>

### `tone_info`

```c
struct bt_hci_le_cs_step_data_tone_info bt_hci_le_cs_step_data_mode_3::tone_info[]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 320.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_hci_le_cs_step_data_tone_info](P322_bt_hci_le_cs_step_data_tone_info_结构体.md)
- [bt_hci_le_cs_step_data_mode_3](P320_bt_hci_le_cs_step_data_mode_3_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P319_bt_hci_le_cs_step_data_mode_2_结构体.md) · [返回大纲](大纲.md) · [下一章](P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md)
