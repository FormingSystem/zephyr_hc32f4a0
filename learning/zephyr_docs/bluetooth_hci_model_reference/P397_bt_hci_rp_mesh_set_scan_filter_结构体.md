---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-397
title: bt_hci_rp_mesh_set_scan_filter_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__mesh__set__scan__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第397章\_bt\_hci\_rp\_mesh\_set\_scan\_filter\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__mesh__set__scan__filter.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 397.1\_数据成员（Data Fields）

<a id="r_a2c832868fd092e235171a8e963c3eaf9"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a2c832868fd092e235171a8e963c3eaf9)。

<a id="r_a029223e5cfca25fc8b0565211734125e"></a>

```c
uint8_t opcode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[opcode](#a029223e5cfca25fc8b0565211734125e)。

<a id="r_afad78bfd78bb399cdeba73ccd10a66fe"></a>

```c
uint8_t scan_filter
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scan_filter](#afad78bfd78bb399cdeba73ccd10a66fe)。

## 397.2\_详细说明（Detailed Documentation）

<a id="a029223e5cfca25fc8b0565211734125e"></a>

### `opcode`

```c
uint8_t bt_hci_rp_mesh_set_scan_filter::opcode
```

<a id="afad78bfd78bb399cdeba73ccd10a66fe"></a>

### `scan_filter`

```c
uint8_t bt_hci_rp_mesh_set_scan_filter::scan_filter
```

<a id="a2c832868fd092e235171a8e963c3eaf9"></a>

### `status`

```c
uint8_t bt_hci_rp_mesh_set_scan_filter::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 397.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P396_bt_hci_rp_mesh_get_opts_结构体.md) · [返回大纲](大纲.md) · [下一章](P398_bt_hci_rp_mesh_set_scanning_结构体.md)
