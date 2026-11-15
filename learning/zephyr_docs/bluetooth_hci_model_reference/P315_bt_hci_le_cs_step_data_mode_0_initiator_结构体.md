---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-315
title: bt_hci_le_cs_step_data_mode_0_initiator_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__0__initiator.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第315章\_bt\_hci\_le\_cs\_step\_data\_mode\_0\_initiator\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__0__initiator.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

子事件结果步骤数据格式（Subevent Result Step Data Format）：模式 0 发起方（Initiator）。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

子事件结果步骤数据格式（Subevent Result Step Data Format）：模式 0 发起方（Initiator）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 315.1\_数据成员（Data Fields）

<a id="r_a339252cacafd05e85c0fb19776343e17"></a>

```c
uint8_t packet_quality_bit_errors: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_bit_errors](#a339252cacafd05e85c0fb19776343e17)。

<a id="r_a811eb38a04e63b12be9e25291126ccc1"></a>

```c
uint8_t packet_quality_aa_check: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_aa_check](#a811eb38a04e63b12be9e25291126ccc1)。

<a id="r_a11edf6e1c1da5d24aa1136521a249f52"></a>

```c
uint8_t packet_rssi
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_rssi](#a11edf6e1c1da5d24aa1136521a249f52)。

<a id="r_ad9a2193cbe5381d30494dbf6f8d84482"></a>

```c
uint8_t packet_antenna
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_antenna](#ad9a2193cbe5381d30494dbf6f8d84482)。

<a id="r_a48fc1fd87869d4ca2b70c42d5c4e1d75"></a>

```c
uint16_t measured_freq_offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[measured_freq_offset](#a48fc1fd87869d4ca2b70c42d5c4e1d75)。

## 315.2\_详细说明（Detailed Documentation）

<a id="a48fc1fd87869d4ca2b70c42d5c4e1d75"></a>

### `measured_freq_offset`

```c
uint16_t bt_hci_le_cs_step_data_mode_0_initiator::measured_freq_offset
```

<a id="ad9a2193cbe5381d30494dbf6f8d84482"></a>

### `packet_antenna`

```c
uint8_t bt_hci_le_cs_step_data_mode_0_initiator::packet_antenna
```

<a id="a811eb38a04e63b12be9e25291126ccc1"></a>

### `packet_quality_aa_check`

```c
uint8_t bt_hci_le_cs_step_data_mode_0_initiator::packet_quality_aa_check
```

<a id="a339252cacafd05e85c0fb19776343e17"></a>

### `packet_quality_bit_errors`

```c
uint8_t bt_hci_le_cs_step_data_mode_0_initiator::packet_quality_bit_errors
```

<a id="a11edf6e1c1da5d24aa1136521a249f52"></a>

### `packet_rssi`

```c
uint8_t bt_hci_le_cs_step_data_mode_0_initiator::packet_rssi
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 315.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P314_bt_hci_iso_sdu_ts_hdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md)
