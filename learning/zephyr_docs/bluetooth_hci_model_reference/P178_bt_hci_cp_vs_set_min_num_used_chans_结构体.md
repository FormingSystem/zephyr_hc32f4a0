---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-178
title: bt_hci_cp_vs_set_min_num_used_chans_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__vs__set__min__num__used__chans.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第178章\_bt\_hci\_cp\_vs\_set\_min\_num\_used\_chans\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__vs__set__min__num__used__chans.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 178.1\_数据成员（Data Fields）

<a id="r_aae4d29392f389a20f9be86870defc954"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#aae4d29392f389a20f9be86870defc954)。

<a id="r_a8cfa13723348bb43c19ceaa56fad2b1c"></a>

```c
uint8_t phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phys](#a8cfa13723348bb43c19ceaa56fad2b1c)。

<a id="r_a68262baddf6b7d2d42d61ad4c2690567"></a>

```c
uint8_t min_used_chans
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_used_chans](#a68262baddf6b7d2d42d61ad4c2690567)。

## 178.2\_详细说明（Detailed Documentation）

<a id="aae4d29392f389a20f9be86870defc954"></a>

### `handle`

```c
uint16_t bt_hci_cp_vs_set_min_num_used_chans::handle
```

<a id="a68262baddf6b7d2d42d61ad4c2690567"></a>

### `min_used_chans`

```c
uint8_t bt_hci_cp_vs_set_min_num_used_chans::min_used_chans
```

<a id="a8cfa13723348bb43c19ceaa56fad2b1c"></a>

### `phys`

```c
uint8_t bt_hci_cp_vs_set_min_num_used_chans::phys
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 178.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P177_bt_hci_cp_vs_set_event_mask_结构体.md) · [返回大纲](大纲.md) · [下一章](P179_bt_hci_cp_vs_set_scan_req_reports_结构体.md)
