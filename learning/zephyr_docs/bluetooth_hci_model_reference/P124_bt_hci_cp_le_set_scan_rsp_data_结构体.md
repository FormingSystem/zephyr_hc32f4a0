---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-124
title: bt_hci_cp_le_set_scan_rsp_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__scan__rsp__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第124章\_bt\_hci\_cp\_le\_set\_scan\_rsp\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__scan__rsp__data.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 124.1\_数据成员（Data Fields）

<a id="r_a0fe51008184419c9560bb5d8f287d8be"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a0fe51008184419c9560bb5d8f287d8be)。

<a id="r_aa719449dc2b85f094081d66398b72c7d"></a>

```c
uint8_t data [31]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#aa719449dc2b85f094081d66398b72c7d)。

## 124.2\_详细说明（Detailed Documentation）

<a id="aa719449dc2b85f094081d66398b72c7d"></a>

### `data`

```c
uint8_t bt_hci_cp_le_set_scan_rsp_data::data[31]
```

<a id="a0fe51008184419c9560bb5d8f287d8be"></a>

### `len`

```c
uint8_t bt_hci_cp_le_set_scan_rsp_data::len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 124.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P123_bt_hci_cp_le_set_scan_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P125_bt_hci_cp_le_set_tx_power_report_enable_结构体.md)
