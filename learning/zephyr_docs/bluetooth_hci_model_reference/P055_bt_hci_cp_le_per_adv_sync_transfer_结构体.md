---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-55
title: bt_hci_cp_le_per_adv_sync_transfer_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__per__adv__sync__transfer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_bt\_hci\_cp\_le\_per\_adv\_sync\_transfer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__per__adv__sync__transfer.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_a991f77d6f2f0c301fe3322050b2d359f"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#a991f77d6f2f0c301fe3322050b2d359f)。

<a id="r_a1327de0f9b2ebd1eaa97b51850087460"></a>

```c
uint16_t service_data
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[service_data](#a1327de0f9b2ebd1eaa97b51850087460)。

<a id="r_a38537b7f01a93f7a3e8cfcb92098a172"></a>

```c
uint16_t sync_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_handle](#a38537b7f01a93f7a3e8cfcb92098a172)。

## 55.2\_详细说明（Detailed Documentation）

<a id="a991f77d6f2f0c301fe3322050b2d359f"></a>

### `conn_handle`

```c
uint16_t bt_hci_cp_le_per_adv_sync_transfer::conn_handle
```

<a id="a1327de0f9b2ebd1eaa97b51850087460"></a>

### `service_data`

```c
uint16_t bt_hci_cp_le_per_adv_sync_transfer::service_data
```

<a id="a38537b7f01a93f7a3e8cfcb92098a172"></a>

### `sync_handle`

```c
uint16_t bt_hci_cp_le_per_adv_sync_transfer::sync_handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_bt_hci_cp_le_per_adv_set_info_transfer_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_bt_hci_cp_le_per_adv_terminate_sync_结构体.md)
