---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-377
title: bt_hci_rp_le_read_tx_power_level_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__tx__power__level.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第377章\_bt\_hci\_rp\_le\_read\_tx\_power\_level\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__tx__power__level.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 377.1\_数据成员（Data Fields）

<a id="r_a4c83db208bfcb7c9fd2211d192a26d90"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a4c83db208bfcb7c9fd2211d192a26d90)。

<a id="r_aec00dfb34abce2d95af183b74f63d1f3"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#aec00dfb34abce2d95af183b74f63d1f3)。

<a id="r_ae65a43aad74b1081e88afdb533cbe813"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#ae65a43aad74b1081e88afdb533cbe813)。

<a id="r_ad14f660eb67f1014d1a62b0e5a113969"></a>

```c
int8_t current_tx_power_level
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[current_tx_power_level](#ad14f660eb67f1014d1a62b0e5a113969)。

<a id="r_a5f9c59660f7c5842712a4ad9ae1d9527"></a>

```c
int8_t max_tx_power_level
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[max_tx_power_level](#a5f9c59660f7c5842712a4ad9ae1d9527)。

## 377.2\_详细说明（Detailed Documentation）

<a id="ad14f660eb67f1014d1a62b0e5a113969"></a>

### `current_tx_power_level`

```c
int8_t bt_hci_rp_le_read_tx_power_level::current_tx_power_level
```

<a id="aec00dfb34abce2d95af183b74f63d1f3"></a>

### `handle`

```c
uint16_t bt_hci_rp_le_read_tx_power_level::handle
```

<a id="a5f9c59660f7c5842712a4ad9ae1d9527"></a>

### `max_tx_power_level`

```c
int8_t bt_hci_rp_le_read_tx_power_level::max_tx_power_level
```

<a id="ae65a43aad74b1081e88afdb533cbe813"></a>

### `phy`

```c
uint8_t bt_hci_rp_le_read_tx_power_level::phy
```

<a id="a4c83db208bfcb7c9fd2211d192a26d90"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_tx_power_level::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 377.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P376_bt_hci_rp_le_read_tx_power_结构体.md) · [返回大纲](大纲.md) · [下一章](P378_bt_hci_rp_le_reject_cis_结构体.md)
