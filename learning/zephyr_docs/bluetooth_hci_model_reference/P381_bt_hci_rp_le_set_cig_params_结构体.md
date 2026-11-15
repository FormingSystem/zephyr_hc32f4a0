---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-381
title: bt_hci_rp_le_set_cig_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__set__cig__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第381章\_bt\_hci\_rp\_le\_set\_cig\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__set__cig__params.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 381.1\_数据成员（Data Fields）

<a id="r_a8426a2b9927bee05fb9a46b4b261c743"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a8426a2b9927bee05fb9a46b4b261c743)。

<a id="r_a951dc88e0cde4e1f0274684498741eac"></a>

```c
uint8_t cig_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cig_id](#a951dc88e0cde4e1f0274684498741eac)。

<a id="r_a8aff643e0ae41455eb9391cfdb45ebda"></a>

```c
uint8_t num_handles
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_handles](#a8aff643e0ae41455eb9391cfdb45ebda)。

<a id="r_a2e95c6217d11169a8a611ea95dce70b6"></a>

```c
uint16_t handle [0]
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a2e95c6217d11169a8a611ea95dce70b6)。

## 381.2\_详细说明（Detailed Documentation）

<a id="a951dc88e0cde4e1f0274684498741eac"></a>

### `cig_id`

```c
uint8_t bt_hci_rp_le_set_cig_params::cig_id
```

<a id="a2e95c6217d11169a8a611ea95dce70b6"></a>

### `handle`

```c
uint16_t bt_hci_rp_le_set_cig_params::handle[0]
```

<a id="a8aff643e0ae41455eb9391cfdb45ebda"></a>

### `num_handles`

```c
uint8_t bt_hci_rp_le_set_cig_params::num_handles
```

<a id="a8426a2b9927bee05fb9a46b4b261c743"></a>

### `status`

```c
uint8_t bt_hci_rp_le_set_cig_params::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 381.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P380_bt_hci_rp_le_remove_iso_path_结构体.md) · [返回大纲](大纲.md) · [下一章](P382_bt_hci_rp_le_set_cig_params_test_结构体.md)
