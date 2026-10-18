---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-250
title: bt_hci_evt_le_cte_req_failed_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cte__req__failed.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第250章\_bt\_hci\_evt\_le\_cte\_req\_failed\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cte__req__failed.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 250.1\_数据成员（Data Fields）

<a id="r_a1433f25dee38014dbd2d061b6d75741a"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a1433f25dee38014dbd2d061b6d75741a)。

<a id="r_aa903954fa411e4ae49a613b4e76219dc"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#aa903954fa411e4ae49a613b4e76219dc)。

## 250.2\_详细说明（Detailed Documentation）

<a id="aa903954fa411e4ae49a613b4e76219dc"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_cte_req_failed::conn_handle
```

<a id="a1433f25dee38014dbd2d061b6d75741a"></a>

### `status`

```c
uint8_t bt_hci_evt_le_cte_req_failed::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 250.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P249_bt_hci_evt_le_cs_test_end_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P251_bt_hci_evt_le_data_len_change_结构体.md)
