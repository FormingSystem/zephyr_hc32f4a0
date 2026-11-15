---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-306
title: bt_hci_evt_vs_trace_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__vs__trace__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第306章\_bt\_hci\_evt\_vs\_trace\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__vs__trace__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 306.1\_数据成员（Data Fields）

<a id="r_af563e07c5364df229eb767e545c8aaa2"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#af563e07c5364df229eb767e545c8aaa2)。

<a id="r_ae524df8cc722cda0fa86127a6b8e56da"></a>

```c
uint8_t data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ae524df8cc722cda0fa86127a6b8e56da)。

## 306.2\_详细说明（Detailed Documentation）

<a id="ae524df8cc722cda0fa86127a6b8e56da"></a>

### `data`

```c
uint8_t bt_hci_evt_vs_trace_info::data[0]
```

<a id="af563e07c5364df229eb767e545c8aaa2"></a>

### `type`

```c
uint8_t bt_hci_evt_vs_trace_info::type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 306.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P305_bt_hci_evt_vs_scan_req_rx_结构体.md) · [返回大纲](大纲.md) · [下一章](P307_bt_hci_ext_adv_set_结构体.md)
