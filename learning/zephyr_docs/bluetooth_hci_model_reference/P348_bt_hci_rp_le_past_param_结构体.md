---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-348
title: bt_hci_rp_le_past_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__past__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第348章\_bt\_hci\_rp\_le\_past\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__past__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 348.1\_数据成员（Data Fields）

<a id="r_a9630362b3d885b13869a4c0fe9e97b12"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a9630362b3d885b13869a4c0fe9e97b12)。

<a id="r_ae6b8a5d7e790516de2f91e41fd893111"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#ae6b8a5d7e790516de2f91e41fd893111)。

## 348.2\_详细说明（Detailed Documentation）

<a id="ae6b8a5d7e790516de2f91e41fd893111"></a>

### `conn_handle`

```c
uint16_t bt_hci_rp_le_past_param::conn_handle
```

<a id="a9630362b3d885b13869a4c0fe9e97b12"></a>

### `status`

```c
uint8_t bt_hci_rp_le_past_param::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 348.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P347_bt_hci_rp_le_ltk_req_reply_结构体.md) · [返回大纲](大纲.md) · [下一章](P349_bt_hci_rp_le_per_adv_set_info_transfer_结构体.md)
