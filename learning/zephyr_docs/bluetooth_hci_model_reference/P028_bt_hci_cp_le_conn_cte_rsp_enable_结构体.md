---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-28
title: bt_hci_cp_le_conn_cte_rsp_enable_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__conn__cte__rsp__enable.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_bt\_hci\_cp\_le\_conn\_cte\_rsp\_enable\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__conn__cte__rsp__enable.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_a9d78072143513020620e02a744d4fa9b"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a9d78072143513020620e02a744d4fa9b)。

<a id="r_ae5eaaae211732d772ea53f3936ab32d2"></a>

```c
uint8_t enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[enable](#ae5eaaae211732d772ea53f3936ab32d2)。

## 28.2\_详细说明（Detailed Documentation）

<a id="ae5eaaae211732d772ea53f3936ab32d2"></a>

### `enable`

```c
uint8_t bt_hci_cp_le_conn_cte_rsp_enable::enable
```

<a id="a9d78072143513020620e02a744d4fa9b"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_conn_cte_rsp_enable::handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_bt_hci_cp_le_conn_param_req_neg_reply_结构体.md)
