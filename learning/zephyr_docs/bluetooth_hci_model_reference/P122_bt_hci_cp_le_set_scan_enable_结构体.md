---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-122
title: bt_hci_cp_le_set_scan_enable_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__scan__enable.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第122章\_bt\_hci\_cp\_le\_set\_scan\_enable\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__scan__enable.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 122.1\_数据成员（Data Fields）

<a id="r_a5e429a0b11be1493515803a360932b06"></a>

```c
uint8_t enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[enable](#a5e429a0b11be1493515803a360932b06)。

<a id="r_a77b0f05c0e76681ed633bd42b3f21811"></a>

```c
uint8_t filter_dup
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_dup](#a77b0f05c0e76681ed633bd42b3f21811)。

## 122.2\_详细说明（Detailed Documentation）

<a id="a5e429a0b11be1493515803a360932b06"></a>

### `enable`

```c
uint8_t bt_hci_cp_le_set_scan_enable::enable
```

<a id="a77b0f05c0e76681ed633bd42b3f21811"></a>

### `filter_dup`

```c
uint8_t bt_hci_cp_le_set_scan_enable::filter_dup
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 122.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P121_bt_hci_cp_le_set_rpa_timeout_结构体.md) · [返回大纲](大纲.md) · [下一章](P123_bt_hci_cp_le_set_scan_param_结构体.md)
