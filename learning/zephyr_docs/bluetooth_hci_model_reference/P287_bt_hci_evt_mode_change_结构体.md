---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-287
title: bt_hci_evt_mode_change_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__mode__change.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第287章\_bt\_hci\_evt\_mode\_change\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__mode__change.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 287.1\_数据成员（Data Fields）

<a id="r_abd35ca68cd0c371350ee49d95aa68454"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#abd35ca68cd0c371350ee49d95aa68454)。

<a id="r_af33d9335a8e9253b481c91dbd0716e40"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#af33d9335a8e9253b481c91dbd0716e40)。

<a id="r_a91a9d6e910fd1999003ae41dce8eaa69"></a>

```c
uint8_t mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode](#a91a9d6e910fd1999003ae41dce8eaa69)。

<a id="r_a12092d35d2866f9c04da6e9e9889416e"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a12092d35d2866f9c04da6e9e9889416e)。

## 287.2\_详细说明（Detailed Documentation）

<a id="af33d9335a8e9253b481c91dbd0716e40"></a>

### `handle`

```c
uint16_t bt_hci_evt_mode_change::handle
```

<a id="a12092d35d2866f9c04da6e9e9889416e"></a>

### `interval`

```c
uint16_t bt_hci_evt_mode_change::interval
```

<a id="a91a9d6e910fd1999003ae41dce8eaa69"></a>

### `mode`

```c
uint8_t bt_hci_evt_mode_change::mode
```

<a id="abd35ca68cd0c371350ee49d95aa68454"></a>

### `status`

```c
uint8_t bt_hci_evt_mode_change::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 287.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P286_bt_hci_evt_mesh_scanning_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P288_bt_hci_evt_num_completed_packets_结构体.md)
