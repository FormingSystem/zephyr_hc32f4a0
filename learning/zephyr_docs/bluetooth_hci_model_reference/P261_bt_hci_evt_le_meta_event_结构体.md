---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-261
title: bt_hci_evt_le_meta_event_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__meta__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第261章\_bt\_hci\_evt\_le\_meta\_event\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__meta__event.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 261.1\_数据成员（Data Fields）

<a id="r_a536464a525f8d0f9df915be5ee3d33da"></a>

```c
uint8_t subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent](#a536464a525f8d0f9df915be5ee3d33da)。

<a id="r_a5f08a4c81ebab1638d251b3bf7f8bfab"></a>

```c
uint8_t data []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a5f08a4c81ebab1638d251b3bf7f8bfab)。

## 261.2\_详细说明（Detailed Documentation）

<a id="a5f08a4c81ebab1638d251b3bf7f8bfab"></a>

### `data`

```c
uint8_t bt_hci_evt_le_meta_event::data[]
```

<a id="a536464a525f8d0f9df915be5ee3d33da"></a>

### `subevent`

```c
uint8_t bt_hci_evt_le_meta_event::subevent
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 261.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P260_bt_hci_evt_le_ltk_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P262_bt_hci_evt_le_p256_public_key_complete_结构体.md)
