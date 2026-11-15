---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-146
title: bt_hci_cp_mesh_set_scanning_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__mesh__set__scanning.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第146章\_bt\_hci\_cp\_mesh\_set\_scanning\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__mesh__set__scanning.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 146.1\_数据成员（Data Fields）

<a id="r_aed23ad3e51e459bbc86945576a8113ef"></a>

```c
uint8_t enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[enable](#aed23ad3e51e459bbc86945576a8113ef)。

<a id="r_a2b27e80def9b437c16de186d5371e140"></a>

```c
uint8_t ch_map
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch_map](#a2b27e80def9b437c16de186d5371e140)。

<a id="r_ac7cf268f484a575268fc6aa0f1b44cce"></a>

```c
uint8_t scan_filter
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scan_filter](#ac7cf268f484a575268fc6aa0f1b44cce)。

## 146.2\_详细说明（Detailed Documentation）

<a id="a2b27e80def9b437c16de186d5371e140"></a>

### `ch_map`

```c
uint8_t bt_hci_cp_mesh_set_scanning::ch_map
```

<a id="aed23ad3e51e459bbc86945576a8113ef"></a>

### `enable`

```c
uint8_t bt_hci_cp_mesh_set_scanning::enable
```

<a id="ac7cf268f484a575268fc6aa0f1b44cce"></a>

### `scan_filter`

```c
uint8_t bt_hci_cp_mesh_set_scanning::scan_filter
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 146.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P145_bt_hci_cp_mesh_set_scan_filter_结构体.md) · [返回大纲](大纲.md) · [下一章](P147_bt_hci_cp_pin_code_neg_reply_结构体.md)
