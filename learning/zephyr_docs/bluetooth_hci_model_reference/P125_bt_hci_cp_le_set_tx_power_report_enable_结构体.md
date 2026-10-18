---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-125
title: bt_hci_cp_le_set_tx_power_report_enable_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__tx__power__report__enable.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第125章\_bt\_hci\_cp\_le\_set\_tx\_power\_report\_enable\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__tx__power__report__enable.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 125.1\_数据成员（Data Fields）

<a id="r_a4a37c87f8f6a966a90c5de09096d1356"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a4a37c87f8f6a966a90c5de09096d1356)。

<a id="r_a30580470d1ba516d86c8b157ca415ef3"></a>

```c
uint8_t local_enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[local_enable](#a30580470d1ba516d86c8b157ca415ef3)。

<a id="r_ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e"></a>

```c
uint8_t remote_enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[remote_enable](#ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e)。

## 125.2\_详细说明（Detailed Documentation）

<a id="a4a37c87f8f6a966a90c5de09096d1356"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_set_tx_power_report_enable::handle
```

<a id="a30580470d1ba516d86c8b157ca415ef3"></a>

### `local_enable`

```c
uint8_t bt_hci_cp_le_set_tx_power_report_enable::local_enable
```

<a id="ab4e8fb4fd7a1fbbc8b5736f8a6f65c5e"></a>

### `remote_enable`

```c
uint8_t bt_hci_cp_le_set_tx_power_report_enable::remote_enable
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 125.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P124_bt_hci_cp_le_set_scan_rsp_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P126_bt_hci_cp_le_setup_iso_path_结构体.md)
