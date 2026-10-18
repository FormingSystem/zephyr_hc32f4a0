---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-45
title: bt_hci_cp_le_generate_dhkey_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__generate__dhkey.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_bt\_hci\_cp\_le\_generate\_dhkey\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__generate__dhkey.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_a0f67195504d877a1d11b7dfb77d09fcc"></a>

```c
uint8_t key [64]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key](#a0f67195504d877a1d11b7dfb77d09fcc)。

## 45.2\_详细说明（Detailed Documentation）

<a id="a0f67195504d877a1d11b7dfb77d09fcc"></a>

### `key`

```c
uint8_t bt_hci_cp_le_generate_dhkey::key[64]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 45.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_bt_hci_cp_le_frame_space_update_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_bt_hci_cp_le_generate_dhkey_v2_结构体.md)
