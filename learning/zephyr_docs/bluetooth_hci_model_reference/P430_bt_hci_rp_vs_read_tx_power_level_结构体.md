---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-430
title: bt_hci_rp_vs_read_tx_power_level_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__tx__power__level.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第430章\_bt\_hci\_rp\_vs\_read\_tx\_power\_level\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__tx__power__level.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 430.1\_数据成员（Data Fields）

<a id="r_ae5011313891d5ac4eaf0383e125bf786"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ae5011313891d5ac4eaf0383e125bf786)。

<a id="r_a86f8e314571df0dfbc0995fb14108650"></a>

```c
uint8_t handle_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle_type](#a86f8e314571df0dfbc0995fb14108650)。

<a id="r_ae2755a4ba68c73c5bb97f58400d8b16d"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ae2755a4ba68c73c5bb97f58400d8b16d)。

<a id="r_ae1e1ee5319283a725c1eb1ab3ad13481"></a>

```c
int8_t tx_power_level
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power_level](#ae1e1ee5319283a725c1eb1ab3ad13481)。

## 430.2\_详细说明（Detailed Documentation）

<a id="ae2755a4ba68c73c5bb97f58400d8b16d"></a>

### `handle`

```c
uint16_t bt_hci_rp_vs_read_tx_power_level::handle
```

<a id="a86f8e314571df0dfbc0995fb14108650"></a>

### `handle_type`

```c
uint8_t bt_hci_rp_vs_read_tx_power_level::handle_type
```

<a id="ae5011313891d5ac4eaf0383e125bf786"></a>

### `status`

```c
uint8_t bt_hci_rp_vs_read_tx_power_level::status
```

<a id="ae1e1ee5319283a725c1eb1ab3ad13481"></a>

### `tx_power_level`

```c
int8_t bt_hci_rp_vs_read_tx_power_level::tx_power_level
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 430.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P429_bt_hci_rp_vs_read_supported_features_结构体.md) · [返回大纲](大纲.md) · [下一章](P431_bt_hci_rp_vs_read_usb_transport_mode_结构体.md)
