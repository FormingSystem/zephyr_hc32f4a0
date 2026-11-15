---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-433
title: bt_hci_rp_vs_write_tx_power_level_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__write__tx__power__level.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第433章\_bt\_hci\_rp\_vs\_write\_tx\_power\_level\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__write__tx__power__level.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 433.1\_数据成员（Data Fields）

<a id="r_a2d462d79165a3fbc98a3a24c6d6ad8fa"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a2d462d79165a3fbc98a3a24c6d6ad8fa)。

<a id="r_a0ba154d288f23fb5d859d620a9205a68"></a>

```c
uint8_t handle_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle_type](#a0ba154d288f23fb5d859d620a9205a68)。

<a id="r_ac7c2eb75ec96f79d67c0a7b3ce851e14"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ac7c2eb75ec96f79d67c0a7b3ce851e14)。

<a id="r_a6a8c6103c609f2c05cfb46476e23d58e"></a>

```c
int8_t selected_tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[selected_tx_power](#a6a8c6103c609f2c05cfb46476e23d58e)。

## 433.2\_详细说明（Detailed Documentation）

<a id="ac7c2eb75ec96f79d67c0a7b3ce851e14"></a>

### `handle`

```c
uint16_t bt_hci_rp_vs_write_tx_power_level::handle
```

<a id="a0ba154d288f23fb5d859d620a9205a68"></a>

### `handle_type`

```c
uint8_t bt_hci_rp_vs_write_tx_power_level::handle_type
```

<a id="a6a8c6103c609f2c05cfb46476e23d58e"></a>

### `selected_tx_power`

```c
int8_t bt_hci_rp_vs_write_tx_power_level::selected_tx_power
```

<a id="a2d462d79165a3fbc98a3a24c6d6ad8fa"></a>

### `status`

```c
uint8_t bt_hci_rp_vs_write_tx_power_level::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 433.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P432_bt_hci_rp_vs_read_version_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P434_bt_hci_rp_write_auth_payload_timeout_结构体.md)
