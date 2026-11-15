---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-305
title: bt_hci_evt_vs_scan_req_rx_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__vs__scan__req__rx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第305章\_bt\_hci\_evt\_vs\_scan\_req\_rx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__vs__scan__req__rx.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 305.1\_数据成员（Data Fields）

<a id="r_a56613220a50bc50a771f432b7e617d5b"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a56613220a50bc50a771f432b7e617d5b)。

<a id="r_acbfa7ec0a3ab1f94f53598a9d8242aba"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#acbfa7ec0a3ab1f94f53598a9d8242aba)。

## 305.2\_详细说明（Detailed Documentation）

<a id="a56613220a50bc50a771f432b7e617d5b"></a>

### `addr`

```c
bt_addr_le_t bt_hci_evt_vs_scan_req_rx::addr
```

<a id="acbfa7ec0a3ab1f94f53598a9d8242aba"></a>

### `rssi`

```c
int8_t bt_hci_evt_vs_scan_req_rx::rssi
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 305.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P306_bt_hci_evt_vs_trace_info_结构体.md)
