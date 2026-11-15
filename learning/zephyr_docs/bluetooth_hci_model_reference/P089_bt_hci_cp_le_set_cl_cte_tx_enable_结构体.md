---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-89
title: bt_hci_cp_le_set_cl_cte_tx_enable_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__cl__cte__tx__enable.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第89章\_bt\_hci\_cp\_le\_set\_cl\_cte\_tx\_enable\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__cl__cte__tx__enable.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 89.1\_数据成员（Data Fields）

<a id="r_a55125c808a888eeecfee9410bcb55859"></a>

```c
uint8_t handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle](#a55125c808a888eeecfee9410bcb55859)。

<a id="r_a3530dae940caefeafb9de4ac761ee080"></a>

```c
uint8_t cte_enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_enable](#a3530dae940caefeafb9de4ac761ee080)。

## 89.2\_详细说明（Detailed Documentation）

<a id="a3530dae940caefeafb9de4ac761ee080"></a>

### `cte_enable`

```c
uint8_t bt_hci_cp_le_set_cl_cte_tx_enable::cte_enable
```

<a id="a55125c808a888eeecfee9410bcb55859"></a>

### `handle`

```c
uint8_t bt_hci_cp_le_set_cl_cte_tx_enable::handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 89.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md) · [返回大纲](大纲.md) · [下一章](P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md)
