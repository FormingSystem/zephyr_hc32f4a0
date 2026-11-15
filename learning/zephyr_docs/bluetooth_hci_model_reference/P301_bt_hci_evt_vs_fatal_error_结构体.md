---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-301
title: bt_hci_evt_vs_fatal_error_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__vs__fatal__error.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第301章\_bt\_hci\_evt\_vs\_fatal\_error\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__vs__fatal__error.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 301.1\_数据成员（Data Fields）

<a id="r_a15e84185f74e84e1f9ccd83dc4fa2798"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a15e84185f74e84e1f9ccd83dc4fa2798)。

<a id="r_aefd553e85eedb6e205da39916c5553aa"></a>

```c
uint8_t data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#aefd553e85eedb6e205da39916c5553aa)。

## 301.2\_详细说明（Detailed Documentation）

<a id="aefd553e85eedb6e205da39916c5553aa"></a>

### `data`

```c
uint8_t bt_hci_evt_vs_fatal_error::data[0]
```

<a id="a15e84185f74e84e1f9ccd83dc4fa2798"></a>

### `type`

```c
uint8_t bt_hci_evt_vs_fatal_error::type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 301.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P300_bt_hci_evt_vs_结构体.md) · [返回大纲](大纲.md) · [下一章](P302_bt_hci_evt_vs_fatal_error_trace_data_结构体.md)
