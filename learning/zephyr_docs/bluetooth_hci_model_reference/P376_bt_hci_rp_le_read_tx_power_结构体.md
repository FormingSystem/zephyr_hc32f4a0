---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-376
title: bt_hci_rp_le_read_tx_power_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__tx__power.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第376章\_bt\_hci\_rp\_le\_read\_tx\_power\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__tx__power.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 376.1\_数据成员（Data Fields）

<a id="r_a805629b92c65e006082d819f578ed555"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a805629b92c65e006082d819f578ed555)。

<a id="r_a6d4ab95efda5cfc97ae11d83787da8d7"></a>

```c
int8_t min_tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[min_tx_power](#a6d4ab95efda5cfc97ae11d83787da8d7)。

<a id="r_a1d794f1f7ea77eceac7dae2546eab047"></a>

```c
int8_t max_tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[max_tx_power](#a1d794f1f7ea77eceac7dae2546eab047)。

## 376.2\_详细说明（Detailed Documentation）

<a id="a1d794f1f7ea77eceac7dae2546eab047"></a>

### `max_tx_power`

```c
int8_t bt_hci_rp_le_read_tx_power::max_tx_power
```

<a id="a6d4ab95efda5cfc97ae11d83787da8d7"></a>

### `min_tx_power`

```c
int8_t bt_hci_rp_le_read_tx_power::min_tx_power
```

<a id="a805629b92c65e006082d819f578ed555"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_tx_power::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 376.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P375_bt_hci_rp_le_read_test_counters_结构体.md) · [返回大纲](大纲.md) · [下一章](P377_bt_hci_rp_le_read_tx_power_level_结构体.md)
