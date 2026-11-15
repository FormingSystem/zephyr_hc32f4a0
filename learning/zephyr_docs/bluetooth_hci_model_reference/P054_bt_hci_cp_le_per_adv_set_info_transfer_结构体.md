---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-54
title: bt_hci_cp_le_per_adv_set_info_transfer_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__per__adv__set__info__transfer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_bt\_hci\_cp\_le\_per\_adv\_set\_info\_transfer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__per__adv__set__info__transfer.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_a3b2f0c510ef9b385cb42bf9a194fa574"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#a3b2f0c510ef9b385cb42bf9a194fa574)。

<a id="r_a5f14c3265bffdf3e30a554a3686e9e0c"></a>

```c
uint16_t service_data
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[service_data](#a5f14c3265bffdf3e30a554a3686e9e0c)。

<a id="r_a75b2c0fa1d50ef9d3761ac25f487750b"></a>

```c
uint8_t adv_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_handle](#a75b2c0fa1d50ef9d3761ac25f487750b)。

## 54.2\_详细说明（Detailed Documentation）

<a id="a75b2c0fa1d50ef9d3761ac25f487750b"></a>

### `adv_handle`

```c
uint8_t bt_hci_cp_le_per_adv_set_info_transfer::adv_handle
```

<a id="a3b2f0c510ef9b385cb42bf9a194fa574"></a>

### `conn_handle`

```c
uint16_t bt_hci_cp_le_per_adv_set_info_transfer::conn_handle
```

<a id="a5f14c3265bffdf3e30a554a3686e9e0c"></a>

### `service_data`

```c
uint16_t bt_hci_cp_le_per_adv_set_info_transfer::service_data
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_bt_hci_cp_le_per_adv_create_sync_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_bt_hci_cp_le_per_adv_sync_transfer_结构体.md)
