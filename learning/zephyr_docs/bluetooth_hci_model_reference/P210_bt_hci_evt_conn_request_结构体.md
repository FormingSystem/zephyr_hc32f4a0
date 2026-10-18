---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-210
title: bt_hci_evt_conn_request_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__conn__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第210章\_bt\_hci\_evt\_conn\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__conn__request.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 210.1\_数据成员（Data Fields）

<a id="r_a03a2ee7ff7754173dff0809e4ebce9e6"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a03a2ee7ff7754173dff0809e4ebce9e6)。

<a id="r_a6059d7c56f45d2fe047a7324db1e820d"></a>

```c
uint8_t dev_class [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dev_class](#a6059d7c56f45d2fe047a7324db1e820d)。

<a id="r_ae11d550701f64717a7d6df5c89b92d0e"></a>

```c
uint8_t link_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[link_type](#ae11d550701f64717a7d6df5c89b92d0e)。

## 210.2\_详细说明（Detailed Documentation）

<a id="a03a2ee7ff7754173dff0809e4ebce9e6"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_evt_conn_request::bdaddr
```

<a id="a6059d7c56f45d2fe047a7324db1e820d"></a>

### `dev_class`

```c
uint8_t bt_hci_evt_conn_request::dev_class[3]
```

<a id="ae11d550701f64717a7d6df5c89b92d0e"></a>

### `link_type`

```c
uint8_t bt_hci_evt_conn_request::link_type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 210.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P209_bt_hci_evt_conn_pkt_type_changed_结构体.md) · [返回大纲](大纲.md) · [下一章](P211_bt_hci_evt_data_buf_overflow_结构体.md)
