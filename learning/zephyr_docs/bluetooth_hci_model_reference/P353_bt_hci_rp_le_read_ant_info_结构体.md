---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-353
title: bt_hci_rp_le_read_ant_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__ant__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第353章\_bt\_hci\_rp\_le\_read\_ant\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__ant__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 353.1\_数据成员（Data Fields）

<a id="r_ae1388d3eee3085af7f2b0b57b2aa7b1e"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ae1388d3eee3085af7f2b0b57b2aa7b1e)。

<a id="r_a2c78d3db239c9e00729d91834eb60f21"></a>

```c
uint8_t switch_sample_rates
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[switch_sample_rates](#a2c78d3db239c9e00729d91834eb60f21)。

<a id="r_a1f79b45751d39ebb9349df93d0ff2e13"></a>

```c
uint8_t num_ant
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_ant](#a1f79b45751d39ebb9349df93d0ff2e13)。

<a id="r_ae75fe0b9f5fe8c88a8e8482eef299348"></a>

```c
uint8_t max_switch_pattern_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_switch_pattern_len](#ae75fe0b9f5fe8c88a8e8482eef299348)。

<a id="r_a625cc8fa8553eafbbb31cbc0b3f303c7"></a>

```c
uint8_t max_cte_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_cte_len](#a625cc8fa8553eafbbb31cbc0b3f303c7)。

## 353.2\_详细说明（Detailed Documentation）

<a id="a625cc8fa8553eafbbb31cbc0b3f303c7"></a>

### `max_cte_len`

```c
uint8_t bt_hci_rp_le_read_ant_info::max_cte_len
```

<a id="ae75fe0b9f5fe8c88a8e8482eef299348"></a>

### `max_switch_pattern_len`

```c
uint8_t bt_hci_rp_le_read_ant_info::max_switch_pattern_len
```

<a id="a1f79b45751d39ebb9349df93d0ff2e13"></a>

### `num_ant`

```c
uint8_t bt_hci_rp_le_read_ant_info::num_ant
```

<a id="ae1388d3eee3085af7f2b0b57b2aa7b1e"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_ant_info::status
```

<a id="a2c78d3db239c9e00729d91834eb60f21"></a>

### `switch_sample_rates`

```c
uint8_t bt_hci_rp_le_read_ant_info::switch_sample_rates
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 353.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P352_bt_hci_rp_le_read_all_local_supported_features_结构体.md) · [返回大纲](大纲.md) · [下一章](P354_bt_hci_rp_le_read_buffer_size_结构体.md)
