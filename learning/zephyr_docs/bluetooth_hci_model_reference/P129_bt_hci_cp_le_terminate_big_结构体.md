---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-129
title: bt_hci_cp_le_terminate_big_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__terminate__big.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第129章\_bt\_hci\_cp\_le\_terminate\_big\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__terminate__big.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 129.1\_数据成员（Data Fields）

<a id="r_acb5fb9451cf890245a85704579b1d1c8"></a>

```c
uint8_t big_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[big_handle](#acb5fb9451cf890245a85704579b1d1c8)。

<a id="r_a958ab6b2f2bb30c825060498e6917a18"></a>

```c
uint8_t reason
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason](#a958ab6b2f2bb30c825060498e6917a18)。

## 129.2\_详细说明（Detailed Documentation）

<a id="acb5fb9451cf890245a85704579b1d1c8"></a>

### `big_handle`

```c
uint8_t bt_hci_cp_le_terminate_big::big_handle
```

<a id="a958ab6b2f2bb30c825060498e6917a18"></a>

### `reason`

```c
uint8_t bt_hci_cp_le_terminate_big::reason
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 129.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P128_bt_hci_cp_le_subrate_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P130_bt_hci_cp_le_tx_test_结构体.md)
