---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-27
title: bt_hci_cp_le_conn_cte_req_enable_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__conn__cte__req__enable.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_bt\_hci\_cp\_le\_conn\_cte\_req\_enable\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__conn__cte__req__enable.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_af340b3b97f9fb12c24baa38415620b44"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#af340b3b97f9fb12c24baa38415620b44)。

<a id="r_aaf38e3d5664d81ae7ac8d3b1bb03c646"></a>

```c
uint8_t enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[enable](#aaf38e3d5664d81ae7ac8d3b1bb03c646)。

<a id="r_a956a1a8794b75e962d03cdcf81847cfc"></a>

```c
uint16_t cte_request_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cte_request_interval](#a956a1a8794b75e962d03cdcf81847cfc)。

<a id="r_a4d4e41bbe95457ce5e8ad68ffeb85200"></a>

```c
uint8_t requested_cte_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[requested_cte_length](#a4d4e41bbe95457ce5e8ad68ffeb85200)。

<a id="r_a5a7443a86e770de4bf7292d813e966e7"></a>

```c
uint8_t requested_cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[requested_cte_type](#a5a7443a86e770de4bf7292d813e966e7)。

## 27.2\_详细说明（Detailed Documentation）

<a id="a956a1a8794b75e962d03cdcf81847cfc"></a>

### `cte_request_interval`

```c
uint16_t bt_hci_cp_le_conn_cte_req_enable::cte_request_interval
```

<a id="aaf38e3d5664d81ae7ac8d3b1bb03c646"></a>

### `enable`

```c
uint8_t bt_hci_cp_le_conn_cte_req_enable::enable
```

<a id="af340b3b97f9fb12c24baa38415620b44"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_conn_cte_req_enable::handle
```

<a id="a4d4e41bbe95457ce5e8ad68ffeb85200"></a>

### `requested_cte_length`

```c
uint8_t bt_hci_cp_le_conn_cte_req_enable::requested_cte_length
```

<a id="a5a7443a86e770de4bf7292d813e966e7"></a>

### `requested_cte_type`

```c
uint8_t bt_hci_cp_le_conn_cte_req_enable::requested_cte_type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_bt_hci_cp_le_big_terminate_sync_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_bt_hci_cp_le_conn_cte_rsp_enable_结构体.md)
