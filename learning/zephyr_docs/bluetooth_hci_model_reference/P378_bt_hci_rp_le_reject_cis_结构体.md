---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-378
title: bt_hci_rp_le_reject_cis_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__reject__cis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第378章\_bt\_hci\_rp\_le\_reject\_cis\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__reject__cis.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 378.1\_数据成员（Data Fields）

<a id="r_af2dc8a839d3e19821ab8ec0d3dc427ec"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#af2dc8a839d3e19821ab8ec0d3dc427ec)。

<a id="r_acd8311e13bdfd7edb2d404d80006f9d4"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#acd8311e13bdfd7edb2d404d80006f9d4)。

## 378.2\_详细说明（Detailed Documentation）

<a id="acd8311e13bdfd7edb2d404d80006f9d4"></a>

### `handle`

```c
uint16_t bt_hci_rp_le_reject_cis::handle
```

<a id="af2dc8a839d3e19821ab8ec0d3dc427ec"></a>

### `status`

```c
uint8_t bt_hci_rp_le_reject_cis::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 378.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P377_bt_hci_rp_le_read_tx_power_level_结构体.md) · [返回大纲](大纲.md) · [下一章](P379_bt_hci_rp_le_remove_cig_结构体.md)
