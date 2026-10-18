---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-368
title: bt_hci_rp_le_read_num_adv_sets_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__num__adv__sets.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第368章\_bt\_hci\_rp\_le\_read\_num\_adv\_sets\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__num__adv__sets.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 368.1\_数据成员（Data Fields）

<a id="r_a590934059fb851a14b2eec66f32a5334"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a590934059fb851a14b2eec66f32a5334)。

<a id="r_a7dd26bda7a8ab75fed2af19bb5af34fc"></a>

```c
uint8_t num_sets
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_sets](#a7dd26bda7a8ab75fed2af19bb5af34fc)。

## 368.2\_详细说明（Detailed Documentation）

<a id="a7dd26bda7a8ab75fed2af19bb5af34fc"></a>

### `num_sets`

```c
uint8_t bt_hci_rp_le_read_num_adv_sets::num_sets
```

<a id="a590934059fb851a14b2eec66f32a5334"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_num_adv_sets::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 368.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P367_bt_hci_rp_le_read_max_data_len_结构体.md) · [返回大纲](大纲.md) · [下一章](P369_bt_hci_rp_le_read_peer_rpa_结构体.md)
