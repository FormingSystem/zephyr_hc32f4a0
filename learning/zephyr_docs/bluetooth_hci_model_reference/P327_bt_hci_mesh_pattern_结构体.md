---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-327
title: bt_hci_mesh_pattern_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__mesh__pattern.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第327章\_bt\_hci\_mesh\_pattern\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__mesh__pattern.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 327.1\_数据成员（Data Fields）

<a id="r_a2ab9eac21c74a03416007f5b7d0f5bc4"></a>

```c
uint8_t pattern_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pattern_len](#a2ab9eac21c74a03416007f5b7d0f5bc4)。

<a id="r_a78e52a2890db71c501885f575bc80de4"></a>

```c
uint8_t pattern [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pattern](#a78e52a2890db71c501885f575bc80de4)。

## 327.2\_详细说明（Detailed Documentation）

<a id="a78e52a2890db71c501885f575bc80de4"></a>

### `pattern`

```c
uint8_t bt_hci_mesh_pattern::pattern[0]
```

<a id="a2ab9eac21c74a03416007f5b7d0f5bc4"></a>

### `pattern_len`

```c
uint8_t bt_hci_mesh_pattern::pattern_len
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 327.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P326_bt_hci_lockstep_结构体.md) · [返回大纲](大纲.md) · [下一章](P328_bt_hci_op_inquiry_结构体.md)
