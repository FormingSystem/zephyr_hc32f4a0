---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-16
title: bt_bap_broadcast_assistant_mod_src_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__assistant__mod__src__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_bt\_bap\_broadcast\_assistant\_mod\_src\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__assistant__mod__src__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

修改音频源的参数。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

修改音频源的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_a5bc7c0a491872d655296bbb979402a62"></a>

```c
uint8_t src_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[src_id](#a5bc7c0a491872d655296bbb979402a62)。

接收状态的音频源 ID（Source ID）。

<a id="r_a794bb68c8a73edfe3d44dbe9a0bf2830"></a>

```c
bool pa_sync
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[pa_sync](#a794bb68c8a73edfe3d44dbe9a0bf2830)。

是否同步到周期性广播（Periodic Advertisements）。

<a id="r_aebaa104384dcbec7bb952a27f3acc24d"></a>

```c
uint16_t pa_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pa_interval](#aebaa104384dcbec7bb952a27f3acc24d)。

周期性广播间隔（Periodic Advertising Interval）。

<a id="r_a42b12c6d9f5c622433c9c1f0c72726c1"></a>

```c
uint8_t num_subgroups
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subgroups](#a42b12c6d9f5c622433c9c1f0c72726c1)。

子组数量。

<a id="r_a2383ec98b14054e0bc66bb4a0ae7b8b6"></a>

```c
struct bt_bap_bass_subgroup * subgroups
```

相关声明：[bt_bap_bass_subgroup](P013_bt_bap_bass_subgroup_结构体.md)、[subgroups](#a2383ec98b14054e0bc66bb4a0ae7b8b6)。

指向子组数组的指针。

## 16.2\_详细说明（Detailed Documentation）

<a id="a42b12c6d9f5c622433c9c1f0c72726c1"></a>

### `num_subgroups`

```c
uint8_t bt_bap_broadcast_assistant_mod_src_param::num_subgroups
```

子组数量。

<a id="aebaa104384dcbec7bb952a27f3acc24d"></a>

### `pa_interval`

```c
uint16_t bt_bap_broadcast_assistant_mod_src_param::pa_interval
```

周期性广播间隔（Periodic Advertising Interval）。

未知时使用 `BT_BAP_PA_INTERVAL_UNKNOWN`。

<a id="a794bb68c8a73edfe3d44dbe9a0bf2830"></a>

### `pa_sync`

```c
bool bt_bap_broadcast_assistant_mod_src_param::pa_sync
```

是否同步到周期性广播（Periodic Advertisements）。

<a id="a5bc7c0a491872d655296bbb979402a62"></a>

### `src_id`

```c
uint8_t bt_bap_broadcast_assistant_mod_src_param::src_id
```

接收状态的音频源 ID（Source ID）。

<a id="a2383ec98b14054e0bc66bb4a0ae7b8b6"></a>

### `subgroups`

```c
struct bt_bap_bass_subgroup* bt_bap_broadcast_assistant_mod_src_param::subgroups
```

指向子组数组的指针。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_bap_bass_subgroup](P013_bt_bap_bass_subgroup_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_bt_bap_broadcast_assistant_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_bt_bap_broadcast_sink_结构体.md)
