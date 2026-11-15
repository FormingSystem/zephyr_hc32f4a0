---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-30
title: bt_cap_commander_distribute_broadcast_code_member_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__distribute__broadcast__code__member__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__distribute__broadcast__code__member__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分发广播码（Broadcast Code）的成员参数。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

分发广播码（Broadcast Code）的成员参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_acd5d185c590ea9a64faebd354a3d5d4a"></a>

```c
union bt_cap_set_member member
```

相关声明：[bt_cap_set_member](P188_bt_cap_set_member_联合体.md)、[member](#acd5d185c590ea9a64faebd354a3d5d4a)。

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="r_ad240bb7e1e9ad5c40eb1a031a6fbc2fe"></a>

```c
uint8_t src_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[src_id](#ad240bb7e1e9ad5c40eb1a031a6fbc2fe)。

接收状态的音频源 ID（Source ID）。

## 30.2\_详细说明（Detailed Documentation）

<a id="acd5d185c590ea9a64faebd354a3d5d4a"></a>

### `member`

```c
union bt_cap_set_member bt_cap_commander_distribute_broadcast_code_member_param::member
```

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="ad240bb7e1e9ad5c40eb1a031a6fbc2fe"></a>

### `src_id`

```c
uint8_t bt_cap_commander_distribute_broadcast_code_member_param::src_id
```

接收状态的音频源 ID（Source ID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_member](P188_bt_cap_set_member_联合体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_bt_cap_commander_change_volume_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md)
