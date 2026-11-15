---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-394
title: bt_hci_rp_mesh_advertise_cancel_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__mesh__advertise__cancel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第394章\_bt\_hci\_rp\_mesh\_advertise\_cancel\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__mesh__advertise__cancel.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 394.1\_数据成员（Data Fields）

<a id="r_ac8a13ab9c91a88859803dcf9f80658af"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ac8a13ab9c91a88859803dcf9f80658af)。

<a id="r_abcc6cd11403b34f04ff4e128628d7484"></a>

```c
uint8_t opcode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[opcode](#abcc6cd11403b34f04ff4e128628d7484)。

<a id="r_afd121f3bb6d3453e7ec0bd9b895a3ccb"></a>

```c
uint8_t adv_slot
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_slot](#afd121f3bb6d3453e7ec0bd9b895a3ccb)。

## 394.2\_详细说明（Detailed Documentation）

<a id="afd121f3bb6d3453e7ec0bd9b895a3ccb"></a>

### `adv_slot`

```c
uint8_t bt_hci_rp_mesh_advertise_cancel::adv_slot
```

<a id="abcc6cd11403b34f04ff4e128628d7484"></a>

### `opcode`

```c
uint8_t bt_hci_rp_mesh_advertise_cancel::opcode
```

<a id="ac8a13ab9c91a88859803dcf9f80658af"></a>

### `status`

```c
uint8_t bt_hci_rp_mesh_advertise_cancel::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 394.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P393_bt_hci_rp_mesh_advertise_结构体.md) · [返回大纲](大纲.md) · [下一章](P395_bt_hci_rp_mesh_advertise_timed_结构体.md)
