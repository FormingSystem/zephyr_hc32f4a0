---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-118
title: bt_hci_cp_le_set_privacy_mode_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__privacy__mode.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第118章\_bt\_hci\_cp\_le\_set\_privacy\_mode\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__privacy__mode.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 118.1\_数据成员（Data Fields）

<a id="r_a404cc9f04cd11924445f12eb4471ef2e"></a>

```c
bt_addr_le_t id_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[id_addr](#a404cc9f04cd11924445f12eb4471ef2e)。

<a id="r_a8ca00418b0638bba6ef586d6cbf253a5"></a>

```c
uint8_t mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode](#a8ca00418b0638bba6ef586d6cbf253a5)。

## 118.2\_详细说明（Detailed Documentation）

<a id="a404cc9f04cd11924445f12eb4471ef2e"></a>

### `id_addr`

```c
bt_addr_le_t bt_hci_cp_le_set_privacy_mode::id_addr
```

<a id="a8ca00418b0638bba6ef586d6cbf253a5"></a>

### `mode`

```c
uint8_t bt_hci_cp_le_set_privacy_mode::mode
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 118.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P117_bt_hci_cp_le_set_phy_结构体.md) · [返回大纲](大纲.md) · [下一章](P119_bt_hci_cp_le_set_procedure_parameters_结构体.md)
