---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-396
title: bt_hci_rp_mesh_get_opts_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__mesh__get__opts.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第396章\_bt\_hci\_rp\_mesh\_get\_opts\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__mesh__get__opts.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 396.1\_数据成员（Data Fields）

<a id="r_a6bc6ec02023723b280cb643bd19a6178"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a6bc6ec02023723b280cb643bd19a6178)。

<a id="r_a50276763a447e1942b28ef33401c3a54"></a>

```c
uint8_t opcode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[opcode](#a50276763a447e1942b28ef33401c3a54)。

<a id="r_abcc86aae5c91a0b551d6b7686c807349"></a>

```c
uint8_t revision
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[revision](#abcc86aae5c91a0b551d6b7686c807349)。

<a id="r_a06de566ae223d750a4d367575ca2a8a0"></a>

```c
uint8_t ch_map
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch_map](#a06de566ae223d750a4d367575ca2a8a0)。

<a id="r_aa000cd8242e6122d11dae17c726cf15a"></a>

```c
int8_t min_tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[min_tx_power](#aa000cd8242e6122d11dae17c726cf15a)。

<a id="r_aeb49bfa06dc5b7200392c363ed6d67b0"></a>

```c
int8_t max_tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[max_tx_power](#aeb49bfa06dc5b7200392c363ed6d67b0)。

<a id="r_a9088d94213a80dfe7f3fb78188f24e05"></a>

```c
uint8_t max_scan_filter
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_scan_filter](#a9088d94213a80dfe7f3fb78188f24e05)。

<a id="r_a41b1c570c26ee911bd5f9b005492cb95"></a>

```c
uint8_t max_filter_pattern
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_filter_pattern](#a41b1c570c26ee911bd5f9b005492cb95)。

<a id="r_a1fbb06dca694411d58af86dee7a547fc"></a>

```c
uint8_t max_adv_slot
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_adv_slot](#a1fbb06dca694411d58af86dee7a547fc)。

<a id="r_a5464a608f37c74f1d43e83d8877e405e"></a>

```c
uint8_t max_tx_window
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_tx_window](#a5464a608f37c74f1d43e83d8877e405e)。

<a id="r_af607a95cd367be6950a3185c2df2aca8"></a>

```c
uint8_t evt_prefix_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[evt_prefix_len](#af607a95cd367be6950a3185c2df2aca8)。

<a id="r_af2f158774100ab0ca1537e69b3918eaa"></a>

```c
uint8_t evt_prefix
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[evt_prefix](#af2f158774100ab0ca1537e69b3918eaa)。

## 396.2\_详细说明（Detailed Documentation）

<a id="a06de566ae223d750a4d367575ca2a8a0"></a>

### `ch_map`

```c
uint8_t bt_hci_rp_mesh_get_opts::ch_map
```

<a id="af2f158774100ab0ca1537e69b3918eaa"></a>

### `evt_prefix`

```c
uint8_t bt_hci_rp_mesh_get_opts::evt_prefix
```

<a id="af607a95cd367be6950a3185c2df2aca8"></a>

### `evt_prefix_len`

```c
uint8_t bt_hci_rp_mesh_get_opts::evt_prefix_len
```

<a id="a1fbb06dca694411d58af86dee7a547fc"></a>

### `max_adv_slot`

```c
uint8_t bt_hci_rp_mesh_get_opts::max_adv_slot
```

<a id="a41b1c570c26ee911bd5f9b005492cb95"></a>

### `max_filter_pattern`

```c
uint8_t bt_hci_rp_mesh_get_opts::max_filter_pattern
```

<a id="a9088d94213a80dfe7f3fb78188f24e05"></a>

### `max_scan_filter`

```c
uint8_t bt_hci_rp_mesh_get_opts::max_scan_filter
```

<a id="aeb49bfa06dc5b7200392c363ed6d67b0"></a>

### `max_tx_power`

```c
int8_t bt_hci_rp_mesh_get_opts::max_tx_power
```

<a id="a5464a608f37c74f1d43e83d8877e405e"></a>

### `max_tx_window`

```c
uint8_t bt_hci_rp_mesh_get_opts::max_tx_window
```

<a id="aa000cd8242e6122d11dae17c726cf15a"></a>

### `min_tx_power`

```c
int8_t bt_hci_rp_mesh_get_opts::min_tx_power
```

<a id="a50276763a447e1942b28ef33401c3a54"></a>

### `opcode`

```c
uint8_t bt_hci_rp_mesh_get_opts::opcode
```

<a id="abcc86aae5c91a0b551d6b7686c807349"></a>

### `revision`

```c
uint8_t bt_hci_rp_mesh_get_opts::revision
```

<a id="a6bc6ec02023723b280cb643bd19a6178"></a>

### `status`

```c
uint8_t bt_hci_rp_mesh_get_opts::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 396.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P395_bt_hci_rp_mesh_advertise_timed_结构体.md) · [返回大纲](大纲.md) · [下一章](P397_bt_hci_rp_mesh_set_scan_filter_结构体.md)
