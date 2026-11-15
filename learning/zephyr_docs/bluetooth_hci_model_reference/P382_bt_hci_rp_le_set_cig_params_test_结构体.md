---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-382
title: bt_hci_rp_le_set_cig_params_test_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__set__cig__params__test.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第382章\_bt\_hci\_rp\_le\_set\_cig\_params\_test\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__set__cig__params__test.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 382.1\_数据成员（Data Fields）

<a id="r_a932eadb4d750f79b4a7a9c3feb90fdcd"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a932eadb4d750f79b4a7a9c3feb90fdcd)。

<a id="r_a65c11059bc00244e58d2ab8373e3e725"></a>

```c
uint8_t cig_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cig_id](#a65c11059bc00244e58d2ab8373e3e725)。

<a id="r_a10816d0875092c8e6bd4b13b819c43c7"></a>

```c
uint8_t num_handles
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_handles](#a10816d0875092c8e6bd4b13b819c43c7)。

<a id="r_a08b07863ed63ab627401c0c80bc3c7b4"></a>

```c
uint16_t handle [0]
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a08b07863ed63ab627401c0c80bc3c7b4)。

## 382.2\_详细说明（Detailed Documentation）

<a id="a65c11059bc00244e58d2ab8373e3e725"></a>

### `cig_id`

```c
uint8_t bt_hci_rp_le_set_cig_params_test::cig_id
```

<a id="a08b07863ed63ab627401c0c80bc3c7b4"></a>

### `handle`

```c
uint16_t bt_hci_rp_le_set_cig_params_test::handle[0]
```

<a id="a10816d0875092c8e6bd4b13b819c43c7"></a>

### `num_handles`

```c
uint8_t bt_hci_rp_le_set_cig_params_test::num_handles
```

<a id="a932eadb4d750f79b4a7a9c3feb90fdcd"></a>

### `status`

```c
uint8_t bt_hci_rp_le_set_cig_params_test::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 382.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P381_bt_hci_rp_le_set_cig_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P383_bt_hci_rp_le_set_cl_cte_sampling_enable_结构体.md)
