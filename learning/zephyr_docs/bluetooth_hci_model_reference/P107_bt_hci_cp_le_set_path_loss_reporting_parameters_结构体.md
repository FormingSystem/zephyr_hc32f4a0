---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-107
title: bt_hci_cp_le_set_path_loss_reporting_parameters_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__path__loss__reporting__parameters.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第107章\_bt\_hci\_cp\_le\_set\_path\_loss\_reporting\_parameters\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__path__loss__reporting__parameters.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 107.1\_数据成员（Data Fields）

<a id="r_a2dec83b0269835538cf4bc5553483f19"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a2dec83b0269835538cf4bc5553483f19)。

<a id="r_ac8b7b832ba241c0448c80be22249b3ca"></a>

```c
uint8_t high_threshold
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[high_threshold](#ac8b7b832ba241c0448c80be22249b3ca)。

<a id="r_ab5de762b7b82c8f453dafe1ea9bbf46d"></a>

```c
uint8_t high_hysteresis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[high_hysteresis](#ab5de762b7b82c8f453dafe1ea9bbf46d)。

<a id="r_a79a53ca3a481e013a5ee892d779e7bfd"></a>

```c
uint8_t low_threshold
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[low_threshold](#a79a53ca3a481e013a5ee892d779e7bfd)。

<a id="r_a28f79bd4ccec4ed108e20a0080ec842d"></a>

```c
uint8_t low_hysteresis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[low_hysteresis](#a28f79bd4ccec4ed108e20a0080ec842d)。

<a id="r_a2289e8198eea1686030ffd3e225c8e7d"></a>

```c
uint16_t min_time_spent
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_time_spent](#a2289e8198eea1686030ffd3e225c8e7d)。

## 107.2\_详细说明（Detailed Documentation）

<a id="a2dec83b0269835538cf4bc5553483f19"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_set_path_loss_reporting_parameters::handle
```

<a id="ab5de762b7b82c8f453dafe1ea9bbf46d"></a>

### `high_hysteresis`

```c
uint8_t bt_hci_cp_le_set_path_loss_reporting_parameters::high_hysteresis
```

<a id="ac8b7b832ba241c0448c80be22249b3ca"></a>

### `high_threshold`

```c
uint8_t bt_hci_cp_le_set_path_loss_reporting_parameters::high_threshold
```

<a id="a28f79bd4ccec4ed108e20a0080ec842d"></a>

### `low_hysteresis`

```c
uint8_t bt_hci_cp_le_set_path_loss_reporting_parameters::low_hysteresis
```

<a id="a79a53ca3a481e013a5ee892d779e7bfd"></a>

### `low_threshold`

```c
uint8_t bt_hci_cp_le_set_path_loss_reporting_parameters::low_threshold
```

<a id="a2289e8198eea1686030ffd3e225c8e7d"></a>

### `min_time_spent`

```c
uint16_t bt_hci_cp_le_set_path_loss_reporting_parameters::min_time_spent
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 107.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P106_bt_hci_cp_le_set_path_loss_reporting_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P108_bt_hci_cp_le_set_pawr_response_data_结构体.md)
