---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-229
title: bt_hci_evt_le_biginfo_adv_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__biginfo__adv__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第229章\_bt\_hci\_evt\_le\_biginfo\_adv\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__biginfo__adv__report.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 229.1\_数据成员（Data Fields）

<a id="r_a8be20bfc607e6ce34ea75c53e285b0d5"></a>

```c
uint16_t sync_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_handle](#a8be20bfc607e6ce34ea75c53e285b0d5)。

<a id="r_ae68f803bbc3f06e7190f62be98d2fe66"></a>

```c
uint8_t num_bis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_bis](#ae68f803bbc3f06e7190f62be98d2fe66)。

<a id="r_ae28d5378a7e2ef59fabb62a3a430ccc8"></a>

```c
uint8_t nse
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nse](#ae28d5378a7e2ef59fabb62a3a430ccc8)。

<a id="r_ae92b69ab0bc257d4f50b98e071c6038b"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#ae92b69ab0bc257d4f50b98e071c6038b)。

<a id="r_ada35f690706be1c6ee8f40787bbe53e5"></a>

```c
uint8_t bn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bn](#ada35f690706be1c6ee8f40787bbe53e5)。

<a id="r_af3a871d3de34b90fc2b09b0725caf479"></a>

```c
uint8_t pto
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pto](#af3a871d3de34b90fc2b09b0725caf479)。

<a id="r_a9c1235653245b517a105570c60ddfa09"></a>

```c
uint8_t irc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[irc](#a9c1235653245b517a105570c60ddfa09)。

<a id="r_a12a000c049e85d2b24720d1a362d28df"></a>

```c
uint16_t max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_pdu](#a12a000c049e85d2b24720d1a362d28df)。

<a id="r_a81e236ceb24012bc267f656f20f1f8c4"></a>

```c
uint8_t sdu_interval [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sdu_interval](#a81e236ceb24012bc267f656f20f1f8c4)。

<a id="r_a084c13c4b0c9c8dca0653b56e53a0c74"></a>

```c
uint16_t max_sdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_sdu](#a084c13c4b0c9c8dca0653b56e53a0c74)。

<a id="r_a2301112acf22cf68d6495ff85f0f29bf"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a2301112acf22cf68d6495ff85f0f29bf)。

<a id="r_abe0636beae2f51004193ad5f7c9efeef"></a>

```c
uint8_t framing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[framing](#abe0636beae2f51004193ad5f7c9efeef)。

<a id="r_ae63eaf93f728109b5fb77ca3179ba99c"></a>

```c
uint8_t encryption
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[encryption](#ae63eaf93f728109b5fb77ca3179ba99c)。

## 229.2\_详细说明（Detailed Documentation）

<a id="ada35f690706be1c6ee8f40787bbe53e5"></a>

### `bn`

```c
uint8_t bt_hci_evt_le_biginfo_adv_report::bn
```

<a id="ae63eaf93f728109b5fb77ca3179ba99c"></a>

### `encryption`

```c
uint8_t bt_hci_evt_le_biginfo_adv_report::encryption
```

<a id="abe0636beae2f51004193ad5f7c9efeef"></a>

### `framing`

```c
uint8_t bt_hci_evt_le_biginfo_adv_report::framing
```

<a id="a9c1235653245b517a105570c60ddfa09"></a>

### `irc`

```c
uint8_t bt_hci_evt_le_biginfo_adv_report::irc
```

<a id="ae92b69ab0bc257d4f50b98e071c6038b"></a>

### `iso_interval`

```c
uint16_t bt_hci_evt_le_biginfo_adv_report::iso_interval
```

<a id="a12a000c049e85d2b24720d1a362d28df"></a>

### `max_pdu`

```c
uint16_t bt_hci_evt_le_biginfo_adv_report::max_pdu
```

<a id="a084c13c4b0c9c8dca0653b56e53a0c74"></a>

### `max_sdu`

```c
uint16_t bt_hci_evt_le_biginfo_adv_report::max_sdu
```

<a id="ae28d5378a7e2ef59fabb62a3a430ccc8"></a>

### `nse`

```c
uint8_t bt_hci_evt_le_biginfo_adv_report::nse
```

<a id="ae68f803bbc3f06e7190f62be98d2fe66"></a>

### `num_bis`

```c
uint8_t bt_hci_evt_le_biginfo_adv_report::num_bis
```

<a id="a2301112acf22cf68d6495ff85f0f29bf"></a>

### `phy`

```c
uint8_t bt_hci_evt_le_biginfo_adv_report::phy
```

<a id="af3a871d3de34b90fc2b09b0725caf479"></a>

### `pto`

```c
uint8_t bt_hci_evt_le_biginfo_adv_report::pto
```

<a id="a81e236ceb24012bc267f656f20f1f8c4"></a>

### `sdu_interval`

```c
uint8_t bt_hci_evt_le_biginfo_adv_report::sdu_interval[3]
```

<a id="a8be20bfc607e6ce34ea75c53e285b0d5"></a>

### `sync_handle`

```c
uint16_t bt_hci_evt_le_biginfo_adv_report::sync_handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 229.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P228_bt_hci_evt_le_big_terminate_结构体.md) · [返回大纲](大纲.md) · [下一章](P230_bt_hci_evt_le_chan_sel_algo_结构体.md)
