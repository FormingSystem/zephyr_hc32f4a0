---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-266
title: bt_hci_evt_le_per_adv_response_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__adv__response.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第266章\_bt\_hci\_evt\_le\_per\_adv\_response\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__adv__response.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 266.1\_数据成员（Data Fields）

<a id="r_a74e304822ec7a431802cf8a7539d640e"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a74e304822ec7a431802cf8a7539d640e)。

<a id="r_a1100429baf398067a396a6ba8db6778a"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#a1100429baf398067a396a6ba8db6778a)。

<a id="r_a4197fbae54be038502312efc14b66320"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a4197fbae54be038502312efc14b66320)。

<a id="r_aa5b5467f4edd52fb8de078b0948141f0"></a>

```c
uint8_t response_slot
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot](#aa5b5467f4edd52fb8de078b0948141f0)。

<a id="r_aa524756d2cce0718ecfd66704eaf389d"></a>

```c
uint8_t data_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_status](#aa524756d2cce0718ecfd66704eaf389d)。

<a id="r_af68f0dc92118f78f6f5b0ffbf1854664"></a>

```c
uint8_t data_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_length](#af68f0dc92118f78f6f5b0ffbf1854664)。

<a id="r_ace3b58eba63b55ce5f3038d4a7877ec2"></a>

```c
uint8_t data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ace3b58eba63b55ce5f3038d4a7877ec2)。

## 266.2\_详细说明（Detailed Documentation）

<a id="a4197fbae54be038502312efc14b66320"></a>

### `cte_type`

```c
uint8_t bt_hci_evt_le_per_adv_response::cte_type
```

<a id="ace3b58eba63b55ce5f3038d4a7877ec2"></a>

### `data`

```c
uint8_t bt_hci_evt_le_per_adv_response::data[0]
```

<a id="af68f0dc92118f78f6f5b0ffbf1854664"></a>

### `data_length`

```c
uint8_t bt_hci_evt_le_per_adv_response::data_length
```

<a id="aa524756d2cce0718ecfd66704eaf389d"></a>

### `data_status`

```c
uint8_t bt_hci_evt_le_per_adv_response::data_status
```

<a id="aa5b5467f4edd52fb8de078b0948141f0"></a>

### `response_slot`

```c
uint8_t bt_hci_evt_le_per_adv_response::response_slot
```

<a id="a1100429baf398067a396a6ba8db6778a"></a>

### `rssi`

```c
int8_t bt_hci_evt_le_per_adv_response::rssi
```

<a id="a74e304822ec7a431802cf8a7539d640e"></a>

### `tx_power`

```c
int8_t bt_hci_evt_le_per_adv_response::tx_power
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 266.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P265_bt_hci_evt_le_path_loss_threshold_结构体.md) · [返回大纲](大纲.md) · [下一章](P267_bt_hci_evt_le_per_adv_response_report_结构体.md)
