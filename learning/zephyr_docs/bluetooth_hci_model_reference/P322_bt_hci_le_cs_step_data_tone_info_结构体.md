---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-322
title: bt_hci_le_cs_step_data_tone_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__tone__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第322章\_bt\_hci\_le\_cs\_step\_data\_tone\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__tone__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

模式 2 和模式 3 中每条天线路径的步骤数据格式（Per-antenna Path Step Data Format）。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

模式 2 和模式 3 中每条天线路径的步骤数据格式（Per-antenna Path Step Data Format）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 322.1\_数据成员（Data Fields）

<a id="r_aeb76aeb54cb4e5613496431ec6d0093a"></a>

```c
uint8_t phase_correction_term [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phase_correction_term](#aeb76aeb54cb4e5613496431ec6d0093a)。

<a id="r_a5f2e5e95b97d2be49a8ff1d9376892e8"></a>

```c
uint8_t extension_indicator: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[extension_indicator](#a5f2e5e95b97d2be49a8ff1d9376892e8)。

<a id="r_a4d31c0759c17789cb4b9bdc90a8870ca"></a>

```c
uint8_t quality_indicator: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[quality_indicator](#a4d31c0759c17789cb4b9bdc90a8870ca)。

## 322.2\_详细说明（Detailed Documentation）

<a id="a5f2e5e95b97d2be49a8ff1d9376892e8"></a>

### `extension_indicator`

```c
uint8_t bt_hci_le_cs_step_data_tone_info::extension_indicator
```

<a id="aeb76aeb54cb4e5613496431ec6d0093a"></a>

### `phase_correction_term`

```c
uint8_t bt_hci_le_cs_step_data_tone_info::phase_correction_term[3]
```

<a id="a4d31c0759c17789cb4b9bdc90a8870ca"></a>

### `quality_indicator`

```c
uint8_t bt_hci_le_cs_step_data_tone_info::quality_indicator
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 322.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md) · [返回大纲](大纲.md) · [下一章](P323_bt_hci_le_iq_sample_结构体.md)
