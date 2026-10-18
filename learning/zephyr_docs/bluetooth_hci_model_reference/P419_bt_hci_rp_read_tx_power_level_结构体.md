---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-419
title: bt_hci_rp_read_tx_power_level_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__tx__power__level.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第419章\_bt\_hci\_rp\_read\_tx\_power\_level\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__tx__power__level.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 419.1\_数据成员（Data Fields）

<a id="r_af40a8e2e663872e8d9fdde839cc6d1b4"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#af40a8e2e663872e8d9fdde839cc6d1b4)。

<a id="r_ac2bd21e90145102bc483c2b0b3cdd416"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ac2bd21e90145102bc483c2b0b3cdd416)。

<a id="r_a46526b820038bb445a7824a7b4bfc870"></a>

```c
int8_t tx_power_level
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power_level](#a46526b820038bb445a7824a7b4bfc870)。

## 419.2\_详细说明（Detailed Documentation）

<a id="ac2bd21e90145102bc483c2b0b3cdd416"></a>

### `handle`

```c
uint16_t bt_hci_rp_read_tx_power_level::handle
```

<a id="af40a8e2e663872e8d9fdde839cc6d1b4"></a>

### `status`

```c
uint8_t bt_hci_rp_read_tx_power_level::status
```

<a id="a46526b820038bb445a7824a7b4bfc870"></a>

### `tx_power_level`

```c
int8_t bt_hci_rp_read_tx_power_level::tx_power_level
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 419.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P418_bt_hci_rp_read_supported_commands_结构体.md) · [返回大纲](大纲.md) · [下一章](P420_bt_hci_rp_remote_name_cancel_结构体.md)
