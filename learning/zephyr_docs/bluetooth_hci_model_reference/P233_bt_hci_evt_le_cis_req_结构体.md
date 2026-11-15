---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-233
title: bt_hci_evt_le_cis_req_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cis__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第233章\_bt\_hci\_evt\_le\_cis\_req\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cis__req.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 233.1\_数据成员（Data Fields）

<a id="r_af8529013adb87340298a89d4727e6867"></a>

```c
uint16_t acl_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[acl_handle](#af8529013adb87340298a89d4727e6867)。

<a id="r_aeed6f4bf58cdb301d6b784a202722acc"></a>

```c
uint16_t cis_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cis_handle](#aeed6f4bf58cdb301d6b784a202722acc)。

<a id="r_ae0ef0ac224bde55de13df4e5eeaf26be"></a>

```c
uint8_t cig_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cig_id](#ae0ef0ac224bde55de13df4e5eeaf26be)。

<a id="r_abdf99eeb7a30c8238bbabdcd60a4847a"></a>

```c
uint8_t cis_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cis_id](#abdf99eeb7a30c8238bbabdcd60a4847a)。

## 233.2\_详细说明（Detailed Documentation）

<a id="af8529013adb87340298a89d4727e6867"></a>

### `acl_handle`

```c
uint16_t bt_hci_evt_le_cis_req::acl_handle
```

<a id="ae0ef0ac224bde55de13df4e5eeaf26be"></a>

### `cig_id`

```c
uint8_t bt_hci_evt_le_cis_req::cig_id
```

<a id="aeed6f4bf58cdb301d6b784a202722acc"></a>

### `cis_handle`

```c
uint16_t bt_hci_evt_le_cis_req::cis_handle
```

<a id="abdf99eeb7a30c8238bbabdcd60a4847a"></a>

### `cis_id`

```c
uint8_t bt_hci_evt_le_cis_req::cis_id
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 233.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P232_bt_hci_evt_le_cis_established_v2_结构体.md) · [返回大纲](大纲.md) · [下一章](P234_bt_hci_evt_le_conn_complete_结构体.md)
