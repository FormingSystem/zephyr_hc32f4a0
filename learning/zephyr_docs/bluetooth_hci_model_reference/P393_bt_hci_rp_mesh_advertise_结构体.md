---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-393
title: bt_hci_rp_mesh_advertise_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__mesh__advertise.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第393章\_bt\_hci\_rp\_mesh\_advertise\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__mesh__advertise.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 393.1\_数据成员（Data Fields）

<a id="r_a1514ae798eb501a0fcb02a48d222d62e"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a1514ae798eb501a0fcb02a48d222d62e)。

<a id="r_aa5a8760133b1f1554797f91a9c4cd8e3"></a>

```c
uint8_t opcode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[opcode](#aa5a8760133b1f1554797f91a9c4cd8e3)。

<a id="r_a0b88358de3223b528cdd424db25f05a0"></a>

```c
uint8_t adv_slot
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_slot](#a0b88358de3223b528cdd424db25f05a0)。

## 393.2\_详细说明（Detailed Documentation）

<a id="a0b88358de3223b528cdd424db25f05a0"></a>

### `adv_slot`

```c
uint8_t bt_hci_rp_mesh_advertise::adv_slot
```

<a id="aa5a8760133b1f1554797f91a9c4cd8e3"></a>

### `opcode`

```c
uint8_t bt_hci_rp_mesh_advertise::opcode
```

<a id="a1514ae798eb501a0fcb02a48d222d62e"></a>

### `status`

```c
uint8_t bt_hci_rp_mesh_advertise::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 393.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P392_bt_hci_rp_le_test_end_结构体.md) · [返回大纲](大纲.md) · [下一章](P394_bt_hci_rp_mesh_advertise_cancel_结构体.md)
