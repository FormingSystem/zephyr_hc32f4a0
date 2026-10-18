---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-285
title: bt_hci_evt_mesh_scan_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__mesh__scan__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第285章\_bt\_hci\_evt\_mesh\_scan\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__mesh__scan__report.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 285.1\_数据成员（Data Fields）

<a id="r_a20d5ffe0df68bee1205a5ee1a5abd6b2"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a20d5ffe0df68bee1205a5ee1a5abd6b2)。

<a id="r_a3d283dd74c33b01fffb42bd4560c6e47"></a>

```c
uint8_t chan
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[chan](#a3d283dd74c33b01fffb42bd4560c6e47)。

<a id="r_af8fb2e61dfe3a3860bf68af0ee8626e6"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#af8fb2e61dfe3a3860bf68af0ee8626e6)。

<a id="r_aa62526739d11d0fa2614e0822f3d70a7"></a>

```c
uint32_t instant
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[instant](#aa62526739d11d0fa2614e0822f3d70a7)。

<a id="r_a281d2c97835fb2f42c6fb322a26d8899"></a>

```c
uint8_t data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_len](#a281d2c97835fb2f42c6fb322a26d8899)。

<a id="r_a573ad980305fb7c10b731a1867c97d1b"></a>

```c
uint8_t data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a573ad980305fb7c10b731a1867c97d1b)。

## 285.2\_详细说明（Detailed Documentation）

<a id="a20d5ffe0df68bee1205a5ee1a5abd6b2"></a>

### `addr`

```c
bt_addr_le_t bt_hci_evt_mesh_scan_report::addr
```

<a id="a3d283dd74c33b01fffb42bd4560c6e47"></a>

### `chan`

```c
uint8_t bt_hci_evt_mesh_scan_report::chan
```

<a id="a573ad980305fb7c10b731a1867c97d1b"></a>

### `data`

```c
uint8_t bt_hci_evt_mesh_scan_report::data[0]
```

<a id="a281d2c97835fb2f42c6fb322a26d8899"></a>

### `data_len`

```c
uint8_t bt_hci_evt_mesh_scan_report::data_len
```

<a id="aa62526739d11d0fa2614e0822f3d70a7"></a>

### `instant`

```c
uint32_t bt_hci_evt_mesh_scan_report::instant
```

<a id="af8fb2e61dfe3a3860bf68af0ee8626e6"></a>

### `rssi`

```c
int8_t bt_hci_evt_mesh_scan_report::rssi
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 285.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P284_bt_hci_evt_mesh_adv_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P286_bt_hci_evt_mesh_scanning_report_结构体.md)
