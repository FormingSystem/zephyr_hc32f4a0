---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-288
title: bt_hci_evt_num_completed_packets_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__num__completed__packets.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第288章\_bt\_hci\_evt\_num\_completed\_packets\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__num__completed__packets.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 288.1\_数据成员（Data Fields）

<a id="r_a666ed2c19596a89ab0c77275cbe18d1e"></a>

```c
uint8_t num_handles
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_handles](#a666ed2c19596a89ab0c77275cbe18d1e)。

<a id="r_a94fb176924f7e844704be28851366052"></a>

```c
struct bt_hci_handle_count h [0]
```

相关声明：[bt_hci_handle_count](P310_bt_hci_handle_count_结构体.md)、[h](#a94fb176924f7e844704be28851366052)。

## 288.2\_详细说明（Detailed Documentation）

<a id="a94fb176924f7e844704be28851366052"></a>

### `h`

```c
struct bt_hci_handle_count bt_hci_evt_num_completed_packets::h[0]
```

<a id="a666ed2c19596a89ab0c77275cbe18d1e"></a>

### `num_handles`

```c
uint8_t bt_hci_evt_num_completed_packets::num_handles
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 288.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_handle_count](P310_bt_hci_handle_count_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P287_bt_hci_evt_mode_change_结构体.md) · [返回大纲](大纲.md) · [下一章](P289_bt_hci_evt_pin_code_req_结构体.md)
