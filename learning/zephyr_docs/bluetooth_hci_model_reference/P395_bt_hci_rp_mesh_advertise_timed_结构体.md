---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-395
title: bt_hci_rp_mesh_advertise_timed_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__mesh__advertise__timed.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第395章\_bt\_hci\_rp\_mesh\_advertise\_timed\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__mesh__advertise__timed.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 395.1\_数据成员（Data Fields）

<a id="r_a84554f3b501a48373e9f58875e6a46be"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a84554f3b501a48373e9f58875e6a46be)。

<a id="r_a15527bfd94e49f654b15fc188aa7c83a"></a>

```c
uint8_t opcode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[opcode](#a15527bfd94e49f654b15fc188aa7c83a)。

<a id="r_a17b39cd87b8392ef1ac7d721a55f6fab"></a>

```c
uint8_t adv_slot
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_slot](#a17b39cd87b8392ef1ac7d721a55f6fab)。

## 395.2\_详细说明（Detailed Documentation）

<a id="a17b39cd87b8392ef1ac7d721a55f6fab"></a>

### `adv_slot`

```c
uint8_t bt_hci_rp_mesh_advertise_timed::adv_slot
```

<a id="a15527bfd94e49f654b15fc188aa7c83a"></a>

### `opcode`

```c
uint8_t bt_hci_rp_mesh_advertise_timed::opcode
```

<a id="a84554f3b501a48373e9f58875e6a46be"></a>

### `status`

```c
uint8_t bt_hci_rp_mesh_advertise_timed::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 395.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P394_bt_hci_rp_mesh_advertise_cancel_结构体.md) · [返回大纲](大纲.md) · [下一章](P396_bt_hci_rp_mesh_get_opts_结构体.md)
