---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-317
title: bt_hci_le_cs_step_data_mode_1_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__1.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第317章\_bt\_hci\_le\_cs\_step\_data\_mode\_1\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__1.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

子事件结果步骤数据格式：模式 1。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

子事件结果步骤数据格式：模式 1。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 317.1\_数据成员（Data Fields）

<a id="r_a0cb4198466318a7a15cbbb172c582eeb"></a>

```c
uint8_t packet_quality_bit_errors: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_bit_errors](#a0cb4198466318a7a15cbbb172c582eeb)。

<a id="r_a8383926e95cd9d222b91704b2ca6883e"></a>

```c
uint8_t packet_quality_aa_check: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_aa_check](#a8383926e95cd9d222b91704b2ca6883e)。

<a id="r_a4025cf2b229ada27e258d3d519a7b1dd"></a>

```c
uint8_t packet_nadm
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_nadm](#a4025cf2b229ada27e258d3d519a7b1dd)。

<a id="r_a1b9df39c01ab91ab225c809db5066f70"></a>

```c
uint8_t packet_rssi
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_rssi](#a1b9df39c01ab91ab225c809db5066f70)。

```c
union {
```

<a id="r_a34a39748b4c54342bd4be7a3396fb208"></a>

```c
int16_t toa_tod_initiator
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[toa_tod_initiator](#a1365e601f422b98747f9909d3be56b60)。

<a id="r_a47a79c928dada7c1bdba56c9b3a13422"></a>

```c
int16_t tod_toa_reflector
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[tod_toa_reflector](#ab3425181b2a625fcfbbfd14477d717d1)。

<a id="r_a191091979aedce48549f5ca9a3b6a0f5"></a>

```c
};
```

<a id="r_afc8221a5cab14d3842590e6cac52da4d"></a>

```c
uint8_t packet_antenna
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_antenna](#afc8221a5cab14d3842590e6cac52da4d)。

## 317.2\_详细说明（Detailed Documentation）

<a id="a191091979aedce48549f5ca9a3b6a0f5"></a>

### `[union]`

```c
union { ... } bt_hci_le_cs_step_data_mode_1
```

<a id="afc8221a5cab14d3842590e6cac52da4d"></a>

### `packet_antenna`

```c
uint8_t bt_hci_le_cs_step_data_mode_1::packet_antenna
```

<a id="a4025cf2b229ada27e258d3d519a7b1dd"></a>

### `packet_nadm`

```c
uint8_t bt_hci_le_cs_step_data_mode_1::packet_nadm
```

<a id="a8383926e95cd9d222b91704b2ca6883e"></a>

### `packet_quality_aa_check`

```c
uint8_t bt_hci_le_cs_step_data_mode_1::packet_quality_aa_check
```

<a id="a0cb4198466318a7a15cbbb172c582eeb"></a>

### `packet_quality_bit_errors`

```c
uint8_t bt_hci_le_cs_step_data_mode_1::packet_quality_bit_errors
```

<a id="a1b9df39c01ab91ab225c809db5066f70"></a>

### `packet_rssi`

```c
uint8_t bt_hci_le_cs_step_data_mode_1::packet_rssi
```

<a id="a1365e601f422b98747f9909d3be56b60"></a>

### `toa_tod_initiator`

```c
int16_t bt_hci_le_cs_step_data_mode_1::toa_tod_initiator
```

<a id="ab3425181b2a625fcfbbfd14477d717d1"></a>

### `tod_toa_reflector`

```c
int16_t bt_hci_le_cs_step_data_mode_1::tod_toa_reflector
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 317.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_hci_le_cs_step_data_mode_1](P317_bt_hci_le_cs_step_data_mode_1_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md) · [返回大纲](大纲.md) · [下一章](P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md)
