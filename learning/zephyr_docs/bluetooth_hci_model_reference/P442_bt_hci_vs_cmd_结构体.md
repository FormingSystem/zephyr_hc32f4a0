---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-442
title: bt_hci_vs_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__vs__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第442章\_bt\_hci\_vs\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__vs__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 442.1\_数据成员（Data Fields）

<a id="r_a640c7523215b676dd8922d95c136cc4b"></a>

```c
uint16_t vendor_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vendor_id](#a640c7523215b676dd8922d95c136cc4b)。

<a id="r_a1ca54af74a178506b954fe8e43a04895"></a>

```c
uint16_t opcode_base
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[opcode_base](#a1ca54af74a178506b954fe8e43a04895)。

## 442.2\_详细说明（Detailed Documentation）

<a id="a1ca54af74a178506b954fe8e43a04895"></a>

### `opcode_base`

```c
uint16_t bt_hci_vs_cmd::opcode_base
```

<a id="a640c7523215b676dd8922d95c136cc4b"></a>

### `vendor_id`

```c
uint16_t bt_hci_vs_cmd::vendor_id
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 442.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P441_bt_hci_std_codecs_v2_结构体.md) · [返回大纲](大纲.md) · [下一章](P443_bt_hci_vs_codec_info_结构体.md)
