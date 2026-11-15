---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-31
title: bt_bap_scan_delegator_mod_src_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__scan__delegator__mod__src__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_bt\_bap\_scan\_delegator\_mod\_src\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__scan__delegator__mod__src__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

`bt_bap_scan_delegator_mod_src()` 的参数。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

`bt_bap_scan_delegator_mod_src()` 的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_ae387a2c0613545ae3acd372780f738bb"></a>

```c
uint8_t src_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[src_id](#ae387a2c0613545ae3acd372780f738bb)。

周期性广播同步（Periodic Advertising Sync）。

<a id="r_aecc8b74632dcb2b17b9a358e00c75d31"></a>

```c
enum bt_bap_big_enc_state encrypt_state
```

相关声明：[bt_bap_big_enc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5e0b0f70d247e131fa542fae16826a22)、[encrypt_state](#aecc8b74632dcb2b17b9a358e00c75d31)。

广播等时组（Broadcast Isochronous Group，BIG）的加密状态。

<a id="r_a11b4c6d787bd2c828e565282daf5cf2f"></a>

```c
uint32_t broadcast_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[broadcast_id](#a11b4c6d787bd2c828e565282daf5cf2f)。

24 位广播 ID。

<a id="r_aa8dcd7983005ffd23779db6b6ccfb752"></a>

```c
uint8_t num_subgroups
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subgroups](#aa8dcd7983005ffd23779db6b6ccfb752)。

子组数量。

<a id="r_ab189593d0125cd443331bcb390d5502e"></a>

```c
struct bt_bap_bass_subgroup subgroups [0]
```

相关声明：[bt_bap_bass_subgroup](P013_bt_bap_bass_subgroup_结构体.md)、[subgroups](#ab189593d0125cd443331bcb390d5502e)。

子组专用信息。

## 31.2\_详细说明（Detailed Documentation）

<a id="a11b4c6d787bd2c828e565282daf5cf2f"></a>

### `broadcast_id`

```c
uint32_t bt_bap_scan_delegator_mod_src_param::broadcast_id
```

24 位广播 ID。

<a id="aecc8b74632dcb2b17b9a358e00c75d31"></a>

### `encrypt_state`

```c
enum bt_bap_big_enc_state bt_bap_scan_delegator_mod_src_param::encrypt_state
```

广播等时组（Broadcast Isochronous Group，BIG）的加密状态。

<a id="aa8dcd7983005ffd23779db6b6ccfb752"></a>

### `num_subgroups`

```c
uint8_t bt_bap_scan_delegator_mod_src_param::num_subgroups
```

子组数量。

<a id="ae387a2c0613545ae3acd372780f738bb"></a>

### `src_id`

```c
uint8_t bt_bap_scan_delegator_mod_src_param::src_id
```

周期性广播同步（Periodic Advertising Sync）。

<a id="ab189593d0125cd443331bcb390d5502e"></a>

### `subgroups`

```c
struct bt_bap_bass_subgroup bt_bap_scan_delegator_mod_src_param::subgroups[ 0]
```

子组专用信息。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 31.3\_原页交叉引用（Cross References）

- [bt_bap_scan_delegator_mod_src()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac022f38269742f16ff6887840ef5ba9a)
- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_bap_big_enc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5e0b0f70d247e131fa542fae16826a22)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_bap_bass_subgroup](P013_bt_bap_bass_subgroup_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_bt_bap_scan_delegator_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_bt_bap_scan_delegator_recv_state_结构体.md)
