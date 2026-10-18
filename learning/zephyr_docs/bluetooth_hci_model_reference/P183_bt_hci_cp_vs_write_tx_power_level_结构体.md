---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-183
title: bt_hci_cp_vs_write_tx_power_level_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__vs__write__tx__power__level.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第183章\_bt\_hci\_cp\_vs\_write\_tx\_power\_level\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__vs__write__tx__power__level.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 183.1\_数据成员（Data Fields）

<a id="r_a27e1b402a9a1a8850f551a18651e914e"></a>

```c
uint8_t handle_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle_type](#a27e1b402a9a1a8850f551a18651e914e)。

<a id="r_adff511831f183e031d9c61781d337b9d"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#adff511831f183e031d9c61781d337b9d)。

<a id="r_abd7f6c92c1463ec35cfd552ffce50b53"></a>

```c
int8_t tx_power_level
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power_level](#abd7f6c92c1463ec35cfd552ffce50b53)。

## 183.2\_详细说明（Detailed Documentation）

<a id="adff511831f183e031d9c61781d337b9d"></a>

### `handle`

```c
uint16_t bt_hci_cp_vs_write_tx_power_level::handle
```

<a id="a27e1b402a9a1a8850f551a18651e914e"></a>

### `handle_type`

```c
uint8_t bt_hci_cp_vs_write_tx_power_level::handle_type
```

<a id="abd7f6c92c1463ec35cfd552ffce50b53"></a>

### `tx_power_level`

```c
int8_t bt_hci_cp_vs_write_tx_power_level::tx_power_level
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 183.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P182_bt_hci_cp_vs_write_bd_addr_结构体.md) · [返回大纲](大纲.md) · [下一章](P184_bt_hci_cp_write_auth_payload_timeout_结构体.md)
