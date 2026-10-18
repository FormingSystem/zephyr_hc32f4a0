---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-379
title: bt_hci_rp_le_remove_cig_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__remove__cig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第379章\_bt\_hci\_rp\_le\_remove\_cig\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__remove__cig.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 379.1\_数据成员（Data Fields）

<a id="r_a1335f26f1dc67ff8e2a1960d1b24b1a0"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a1335f26f1dc67ff8e2a1960d1b24b1a0)。

<a id="r_a82e74fbbce714b035b1e53fd5f1b09b5"></a>

```c
uint8_t cig_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cig_id](#a82e74fbbce714b035b1e53fd5f1b09b5)。

## 379.2\_详细说明（Detailed Documentation）

<a id="a82e74fbbce714b035b1e53fd5f1b09b5"></a>

### `cig_id`

```c
uint8_t bt_hci_rp_le_remove_cig::cig_id
```

<a id="a1335f26f1dc67ff8e2a1960d1b24b1a0"></a>

### `status`

```c
uint8_t bt_hci_rp_le_remove_cig::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 379.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P378_bt_hci_rp_le_reject_cis_结构体.md) · [返回大纲](大纲.md) · [下一章](P380_bt_hci_rp_le_remove_iso_path_结构体.md)
