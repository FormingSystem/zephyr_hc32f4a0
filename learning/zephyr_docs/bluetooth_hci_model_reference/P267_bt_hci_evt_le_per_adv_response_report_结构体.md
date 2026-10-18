---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-267
title: bt_hci_evt_le_per_adv_response_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__adv__response__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第267章\_bt\_hci\_evt\_le\_per\_adv\_response\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__adv__response__report.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 267.1\_数据成员（Data Fields）

<a id="r_a9d746015a9c2b48c54008319c892b063"></a>

```c
uint8_t adv_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_handle](#a9d746015a9c2b48c54008319c892b063)。

<a id="r_ad4f8f61150f82f4ba420e3c0a1f333c2"></a>

```c
uint8_t subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent](#ad4f8f61150f82f4ba420e3c0a1f333c2)。

<a id="r_a46a5b74321a80697fd700a276be18ed3"></a>

```c
uint8_t tx_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_status](#a46a5b74321a80697fd700a276be18ed3)。

<a id="r_a37f3519eefe33e87d49c7c2ad0f8b40c"></a>

```c
uint8_t num_responses
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_responses](#a37f3519eefe33e87d49c7c2ad0f8b40c)。

<a id="r_a3b1bcca7a7dbc6fcf5709f6152268b87"></a>

```c
struct bt_hci_evt_le_per_adv_response responses [0]
```

相关声明：[bt_hci_evt_le_per_adv_response](P266_bt_hci_evt_le_per_adv_response_结构体.md)、[responses](#a3b1bcca7a7dbc6fcf5709f6152268b87)。

## 267.2\_详细说明（Detailed Documentation）

<a id="a9d746015a9c2b48c54008319c892b063"></a>

### `adv_handle`

```c
uint8_t bt_hci_evt_le_per_adv_response_report::adv_handle
```

<a id="a37f3519eefe33e87d49c7c2ad0f8b40c"></a>

### `num_responses`

```c
uint8_t bt_hci_evt_le_per_adv_response_report::num_responses
```

<a id="a3b1bcca7a7dbc6fcf5709f6152268b87"></a>

### `responses`

```c
struct bt_hci_evt_le_per_adv_response bt_hci_evt_le_per_adv_response_report::responses[0]
```

<a id="ad4f8f61150f82f4ba420e3c0a1f333c2"></a>

### `subevent`

```c
uint8_t bt_hci_evt_le_per_adv_response_report::subevent
```

<a id="a46a5b74321a80697fd700a276be18ed3"></a>

### `tx_status`

```c
uint8_t bt_hci_evt_le_per_adv_response_report::tx_status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 267.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_evt_le_per_adv_response](P266_bt_hci_evt_le_per_adv_response_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P266_bt_hci_evt_le_per_adv_response_结构体.md) · [返回大纲](大纲.md) · [下一章](P268_bt_hci_evt_le_per_adv_subevent_data_request_结构体.md)
