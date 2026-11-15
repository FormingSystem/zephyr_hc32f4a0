---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-316
title: bt_hci_le_cs_step_data_mode_0_reflector_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__0__reflector.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第316章\_bt\_hci\_le\_cs\_step\_data\_mode\_0\_reflector\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__0__reflector.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

子事件结果步骤数据格式：模式 0 反射方（Reflector）。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

子事件结果步骤数据格式：模式 0 反射方（Reflector）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 316.1\_数据成员（Data Fields）

<a id="r_a16fb71660c4f4afb1c36765fdbd2a96a"></a>

```c
uint8_t packet_quality_bit_errors: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_bit_errors](#a16fb71660c4f4afb1c36765fdbd2a96a)。

<a id="r_a9c34ecf0b79449754da1d1ba925b1ff2"></a>

```c
uint8_t packet_quality_aa_check: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_quality_aa_check](#a9c34ecf0b79449754da1d1ba925b1ff2)。

<a id="r_aa058afab8cba3f5ce572b8e7d29ef34d"></a>

```c
uint8_t packet_rssi
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_rssi](#aa058afab8cba3f5ce572b8e7d29ef34d)。

<a id="r_ad045baeaf6fbb75de002ffedc4b1a831"></a>

```c
uint8_t packet_antenna
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_antenna](#ad045baeaf6fbb75de002ffedc4b1a831)。

## 316.2\_详细说明（Detailed Documentation）

<a id="ad045baeaf6fbb75de002ffedc4b1a831"></a>

### `packet_antenna`

```c
uint8_t bt_hci_le_cs_step_data_mode_0_reflector::packet_antenna
```

<a id="a9c34ecf0b79449754da1d1ba925b1ff2"></a>

### `packet_quality_aa_check`

```c
uint8_t bt_hci_le_cs_step_data_mode_0_reflector::packet_quality_aa_check
```

<a id="a16fb71660c4f4afb1c36765fdbd2a96a"></a>

### `packet_quality_bit_errors`

```c
uint8_t bt_hci_le_cs_step_data_mode_0_reflector::packet_quality_bit_errors
```

<a id="aa058afab8cba3f5ce572b8e7d29ef34d"></a>

### `packet_rssi`

```c
uint8_t bt_hci_le_cs_step_data_mode_0_reflector::packet_rssi
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 316.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md) · [返回大纲](大纲.md) · [下一章](P317_bt_hci_le_cs_step_data_mode_1_结构体.md)
