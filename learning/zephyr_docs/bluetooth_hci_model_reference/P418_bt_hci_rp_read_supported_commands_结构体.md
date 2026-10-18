---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-418
title: bt_hci_rp_read_supported_commands_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__supported__commands.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第418章\_bt\_hci\_rp\_read\_supported\_commands\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__supported__commands.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 418.1\_数据成员（Data Fields）

<a id="r_a3d36d892f83cfcb1d2fc955ec71ff061"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a3d36d892f83cfcb1d2fc955ec71ff061)。

<a id="r_afd0dc4411a4c7692515139392bffedd0"></a>

```c
uint8_t commands [64]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[commands](#afd0dc4411a4c7692515139392bffedd0)。

## 418.2\_详细说明（Detailed Documentation）

<a id="afd0dc4411a4c7692515139392bffedd0"></a>

### `commands`

```c
uint8_t bt_hci_rp_read_supported_commands::commands[64]
```

<a id="a3d36d892f83cfcb1d2fc955ec71ff061"></a>

### `status`

```c
uint8_t bt_hci_rp_read_supported_commands::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 418.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P417_bt_hci_rp_read_rssi_结构体.md) · [返回大纲](大纲.md) · [下一章](P419_bt_hci_rp_read_tx_power_level_结构体.md)
