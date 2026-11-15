---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-25
title: bt_hci_cp_le_big_create_sync_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__big__create__sync.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_bt\_hci\_cp\_le\_big\_create\_sync\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__big__create__sync.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a6692dae077ce1ce4f31bc94b9d391afd"></a>

```c
uint8_t big_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[big_handle](#a6692dae077ce1ce4f31bc94b9d391afd)。

<a id="r_a70b031f24cdf231e5c168b155517eae0"></a>

```c
uint16_t sync_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_handle](#a70b031f24cdf231e5c168b155517eae0)。

<a id="r_a482edf3326e2dd720b14a03609c1256a"></a>

```c
uint8_t encryption
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[encryption](#a482edf3326e2dd720b14a03609c1256a)。

<a id="r_a053475c3af12e6e37dc4befcf634d68f"></a>

```c
uint8_t bcode [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bcode](#a053475c3af12e6e37dc4befcf634d68f)。

<a id="r_a37050e3eb914ff06495695d44c3fdb50"></a>

```c
uint8_t mse
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mse](#a37050e3eb914ff06495695d44c3fdb50)。

<a id="r_a55e83bc3722ce2dbf943879a80ef2872"></a>

```c
uint16_t sync_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_timeout](#a55e83bc3722ce2dbf943879a80ef2872)。

<a id="r_a7efae2c8dc46d13fb2abca677ac152b0"></a>

```c
uint8_t num_bis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_bis](#a7efae2c8dc46d13fb2abca677ac152b0)。

<a id="r_a6d1050c2a0522be215d82d3874fed4b6"></a>

```c
uint8_t bis [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bis](#a6d1050c2a0522be215d82d3874fed4b6)。

## 25.2\_详细说明（Detailed Documentation）

<a id="a053475c3af12e6e37dc4befcf634d68f"></a>

### `bcode`

```c
uint8_t bt_hci_cp_le_big_create_sync::bcode[16]
```

<a id="a6692dae077ce1ce4f31bc94b9d391afd"></a>

### `big_handle`

```c
uint8_t bt_hci_cp_le_big_create_sync::big_handle
```

<a id="a6d1050c2a0522be215d82d3874fed4b6"></a>

### `bis`

```c
uint8_t bt_hci_cp_le_big_create_sync::bis[0]
```

<a id="a482edf3326e2dd720b14a03609c1256a"></a>

### `encryption`

```c
uint8_t bt_hci_cp_le_big_create_sync::encryption
```

<a id="a37050e3eb914ff06495695d44c3fdb50"></a>

### `mse`

```c
uint8_t bt_hci_cp_le_big_create_sync::mse
```

<a id="a7efae2c8dc46d13fb2abca677ac152b0"></a>

### `num_bis`

```c
uint8_t bt_hci_cp_le_big_create_sync::num_bis
```

<a id="a70b031f24cdf231e5c168b155517eae0"></a>

### `sync_handle`

```c
uint16_t bt_hci_cp_le_big_create_sync::sync_handle
```

<a id="a55e83bc3722ce2dbf943879a80ef2872"></a>

### `sync_timeout`

```c
uint16_t bt_hci_cp_le_big_create_sync::sync_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_bt_hci_cp_le_add_dev_to_rl_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_bt_hci_cp_le_big_terminate_sync_结构体.md)
