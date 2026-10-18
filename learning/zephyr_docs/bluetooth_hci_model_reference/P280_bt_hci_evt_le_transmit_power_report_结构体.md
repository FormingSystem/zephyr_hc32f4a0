---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-280
title: bt_hci_evt_le_transmit_power_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__transmit__power__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第280章\_bt\_hci\_evt\_le\_transmit\_power\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__transmit__power__report.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 280.1\_数据成员（Data Fields）

<a id="r_af1629e59dd651e1616b89f4958f47c92"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#af1629e59dd651e1616b89f4958f47c92)。

<a id="r_a4feadb14800c1b51a9cc523c1d6a9063"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a4feadb14800c1b51a9cc523c1d6a9063)。

<a id="r_a341cc0c5cc1ea969e2024b67056a5439"></a>

```c
uint8_t reason
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason](#a341cc0c5cc1ea969e2024b67056a5439)。

<a id="r_ad6130863713cf31a1cbe33de9fb5428f"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#ad6130863713cf31a1cbe33de9fb5428f)。

<a id="r_aa0df9c50a555fa40ed25a14f7b6a5e77"></a>

```c
int8_t tx_power_level
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power_level](#aa0df9c50a555fa40ed25a14f7b6a5e77)。

<a id="r_a2dc33da8f36cceda362d0c87098b02d6"></a>

```c
uint8_t tx_power_level_flag
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_power_level_flag](#a2dc33da8f36cceda362d0c87098b02d6)。

<a id="r_ac42d60325235f517728ff44385361db2"></a>

```c
int8_t delta
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[delta](#ac42d60325235f517728ff44385361db2)。

## 280.2\_详细说明（Detailed Documentation）

<a id="ac42d60325235f517728ff44385361db2"></a>

### `delta`

```c
int8_t bt_hci_evt_le_transmit_power_report::delta
```

<a id="a4feadb14800c1b51a9cc523c1d6a9063"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_transmit_power_report::handle
```

<a id="ad6130863713cf31a1cbe33de9fb5428f"></a>

### `phy`

```c
uint8_t bt_hci_evt_le_transmit_power_report::phy
```

<a id="a341cc0c5cc1ea969e2024b67056a5439"></a>

### `reason`

```c
uint8_t bt_hci_evt_le_transmit_power_report::reason
```

<a id="af1629e59dd651e1616b89f4958f47c92"></a>

### `status`

```c
uint8_t bt_hci_evt_le_transmit_power_report::status
```

<a id="aa0df9c50a555fa40ed25a14f7b6a5e77"></a>

### `tx_power_level`

```c
int8_t bt_hci_evt_le_transmit_power_report::tx_power_level
```

<a id="a2dc33da8f36cceda362d0c87098b02d6"></a>

### `tx_power_level_flag`

```c
uint8_t bt_hci_evt_le_transmit_power_report::tx_power_level_flag
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 280.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P279_bt_hci_evt_le_subrate_change_结构体.md) · [返回大纲](大纲.md) · [下一章](P281_bt_hci_evt_link_key_notify_结构体.md)
