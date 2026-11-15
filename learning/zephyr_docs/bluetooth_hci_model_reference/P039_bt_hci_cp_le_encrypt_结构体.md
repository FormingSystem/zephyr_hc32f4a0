---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-39
title: bt_hci_cp_le_encrypt_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__encrypt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_bt\_hci\_cp\_le\_encrypt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__encrypt.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_ab64f1bab8ad3a98217db96e6765a7d24"></a>

```c
uint8_t key [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key](#ab64f1bab8ad3a98217db96e6765a7d24)。

<a id="r_ad520b84e6e2a4e62f7fefba248c4cf10"></a>

```c
uint8_t plaintext [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[plaintext](#ad520b84e6e2a4e62f7fefba248c4cf10)。

## 39.2\_详细说明（Detailed Documentation）

<a id="ab64f1bab8ad3a98217db96e6765a7d24"></a>

### `key`

```c
uint8_t bt_hci_cp_le_encrypt::key[16]
```

<a id="ad520b84e6e2a4e62f7fefba248c4cf10"></a>

### `plaintext`

```c
uint8_t bt_hci_cp_le_encrypt::plaintext[16]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_bt_hci_cp_le_default_past_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_bt_hci_cp_le_enh_rx_test_结构体.md)
