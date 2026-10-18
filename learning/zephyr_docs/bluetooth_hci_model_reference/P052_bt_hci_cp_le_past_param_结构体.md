---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-52
title: bt_hci_cp_le_past_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__past__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_bt\_hci\_cp\_le\_past\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__past__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_a9c99cdd5ae5de58960677781c2287c4d"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#a9c99cdd5ae5de58960677781c2287c4d)。

<a id="r_aa36345a550dfabeef48b430d1a1b0030"></a>

```c
uint8_t mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode](#aa36345a550dfabeef48b430d1a1b0030)。

<a id="r_a622499d51e917f7828629de2291812e5"></a>

```c
uint16_t skip
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[skip](#a622499d51e917f7828629de2291812e5)。

<a id="r_aec9aa4ffe41c6b6f5cfcbc59eb57efca"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#aec9aa4ffe41c6b6f5cfcbc59eb57efca)。

<a id="r_a47c571ff27a59e0a7cbcb460303ee194"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a47c571ff27a59e0a7cbcb460303ee194)。

## 52.2\_详细说明（Detailed Documentation）

<a id="a9c99cdd5ae5de58960677781c2287c4d"></a>

### `conn_handle`

```c
uint16_t bt_hci_cp_le_past_param::conn_handle
```

<a id="a47c571ff27a59e0a7cbcb460303ee194"></a>

### `cte_type`

```c
uint8_t bt_hci_cp_le_past_param::cte_type
```

<a id="aa36345a550dfabeef48b430d1a1b0030"></a>

### `mode`

```c
uint8_t bt_hci_cp_le_past_param::mode
```

<a id="a622499d51e917f7828629de2291812e5"></a>

### `skip`

```c
uint16_t bt_hci_cp_le_past_param::skip
```

<a id="aec9aa4ffe41c6b6f5cfcbc59eb57efca"></a>

### `timeout`

```c
uint16_t bt_hci_cp_le_past_param::timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_bt_hci_cp_le_ltk_req_reply_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_bt_hci_cp_le_per_adv_create_sync_结构体.md)
