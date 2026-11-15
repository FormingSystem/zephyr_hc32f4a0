---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-33
title: bt_hci_cp_le_create_cis_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__create__cis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_bt\_hci\_cp\_le\_create\_cis\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__create__cis.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_acd348a7d68947af8e7119b2e1a864481"></a>

```c
uint8_t num_cis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_cis](#acd348a7d68947af8e7119b2e1a864481)。

<a id="r_a5a323d09df7813fc9b834cc1d205d101"></a>

```c
struct bt_hci_cis cis [0]
```

相关声明：[bt_hci_cis](P002_bt_hci_cis_结构体.md)、[cis](#a5a323d09df7813fc9b834cc1d205d101)。

## 33.2\_详细说明（Detailed Documentation）

<a id="a5a323d09df7813fc9b834cc1d205d101"></a>

### `cis`

```c
struct bt_hci_cis bt_hci_cp_le_create_cis::cis[0]
```

<a id="acd348a7d68947af8e7119b2e1a864481"></a>

### `num_cis`

```c
uint8_t bt_hci_cp_le_create_cis::num_cis
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_cis](P002_bt_hci_cis_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_bt_hci_cp_le_create_big_test_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_bt_hci_cp_le_create_conn_结构体.md)
