---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-268
title: bt_hci_evt_le_per_adv_subevent_data_request_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__adv__subevent__data__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第268章\_bt\_hci\_evt\_le\_per\_adv\_subevent\_data\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__adv__subevent__data__request.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 268.1\_数据成员（Data Fields）

<a id="r_ae6f6ef17edabfd210a7e6597087ff512"></a>

```c
uint8_t adv_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_handle](#ae6f6ef17edabfd210a7e6597087ff512)。

<a id="r_a8f7fd9b149aa52422cb3eb874b91943d"></a>

```c
uint8_t subevent_start
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_start](#a8f7fd9b149aa52422cb3eb874b91943d)。

<a id="r_a45cdb248b80602a7f14f24e0324e6f97"></a>

```c
uint8_t subevent_data_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_data_count](#a45cdb248b80602a7f14f24e0324e6f97)。

## 268.2\_详细说明（Detailed Documentation）

<a id="ae6f6ef17edabfd210a7e6597087ff512"></a>

### `adv_handle`

```c
uint8_t bt_hci_evt_le_per_adv_subevent_data_request::adv_handle
```

<a id="a45cdb248b80602a7f14f24e0324e6f97"></a>

### `subevent_data_count`

```c
uint8_t bt_hci_evt_le_per_adv_subevent_data_request::subevent_data_count
```

<a id="a8f7fd9b149aa52422cb3eb874b91943d"></a>

### `subevent_start`

```c
uint8_t bt_hci_evt_le_per_adv_subevent_data_request::subevent_start
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 268.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P267_bt_hci_evt_le_per_adv_response_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P269_bt_hci_evt_le_per_adv_sync_established_结构体.md)
