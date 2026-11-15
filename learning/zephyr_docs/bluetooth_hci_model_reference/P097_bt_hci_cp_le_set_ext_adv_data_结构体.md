---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-97
title: bt_hci_cp_le_set_ext_adv_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__adv__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第97章\_bt\_hci\_cp\_le\_set\_ext\_adv\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__adv__data.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 97.1\_数据成员（Data Fields）

<a id="r_a803bb793eefcc714c6c4034123a2e487"></a>

```c
uint8_t handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle](#a803bb793eefcc714c6c4034123a2e487)。

<a id="r_ac5eaa1834f82024055923d08a3bef6b3"></a>

```c
uint8_t op
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[op](#ac5eaa1834f82024055923d08a3bef6b3)。

<a id="r_af9eef9f59bfec5867ea36bdf33e3a9b1"></a>

```c
uint8_t frag_pref
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[frag_pref](#af9eef9f59bfec5867ea36bdf33e3a9b1)。

<a id="r_aea3055cc7ffbaf4cd14996d885e21ba3"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#aea3055cc7ffbaf4cd14996d885e21ba3)。

<a id="r_a7d7df52500eb53a64b6ba5e62f6cf14f"></a>

```c
uint8_t data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a7d7df52500eb53a64b6ba5e62f6cf14f)。

## 97.2\_详细说明（Detailed Documentation）

<a id="a7d7df52500eb53a64b6ba5e62f6cf14f"></a>

### `data`

```c
uint8_t bt_hci_cp_le_set_ext_adv_data::data[0]
```

<a id="af9eef9f59bfec5867ea36bdf33e3a9b1"></a>

### `frag_pref`

```c
uint8_t bt_hci_cp_le_set_ext_adv_data::frag_pref
```

<a id="a803bb793eefcc714c6c4034123a2e487"></a>

### `handle`

```c
uint8_t bt_hci_cp_le_set_ext_adv_data::handle
```

<a id="aea3055cc7ffbaf4cd14996d885e21ba3"></a>

### `len`

```c
uint8_t bt_hci_cp_le_set_ext_adv_data::len
```

<a id="ac5eaa1834f82024055923d08a3bef6b3"></a>

### `op`

```c
uint8_t bt_hci_cp_le_set_ext_adv_data::op
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 97.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P096_bt_hci_cp_le_set_event_mask_结构体.md) · [返回大纲](大纲.md) · [下一章](P098_bt_hci_cp_le_set_ext_adv_enable_结构体.md)
