---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-27
title: bt_cap_commander_change_volume_offset_member_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__volume__offset__member__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_bt\_cap\_commander\_change\_volume\_offset\_member\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__volume__offset__member__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_commander_change_volume_offset_param` 中供 `bt_cap_commander_change_volume_offset()` 使用的参数部分。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_commander_change_volume_offset_param` 中供 `bt_cap_commander_change_volume_offset()` 使用的参数部分。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_a8e2e4f07be565ef1067d4955ebef50d4"></a>

```c
union bt_cap_set_member member
```

相关声明：[bt_cap_set_member](P188_bt_cap_set_member_联合体.md)、[member](#a8e2e4f07be565ef1067d4955ebef50d4)。

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="r_a7d9e94cd9eb79f1f7a14c8b9bb84e5a8"></a>

```c
int16_t offset
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[offset](#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8)。

要设置的偏移量（Offset）。

## 27.2\_详细说明（Detailed Documentation）

<a id="a8e2e4f07be565ef1067d4955ebef50d4"></a>

### `member`

```c
union bt_cap_set_member bt_cap_commander_change_volume_offset_member_param::member
```

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="a7d9e94cd9eb79f1f7a14c8b9bb84e5a8"></a>

### `offset`

```c
int16_t bt_cap_commander_change_volume_offset_member_param::offset
```

要设置的偏移量（Offset）。

值必须在 `BT_VOCS_MIN_OFFSET` 与 `BT_VOCS_MAX_OFFSET` 之间。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 27.3\_原页交叉引用（Cross References）

- [bt_cap_commander_change_volume_offset_param](P028_bt_cap_commander_change_volume_offset_param_结构体.md)
- [bt_cap_commander_change_volume_offset()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae2cd451b387659b0a2021a9023d74dfa)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_member](P188_bt_cap_set_member_联合体.md)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [BT_VOCS_MIN_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga64d4e32f9d92a58b3229b3aa2e8fcc4d)
- [BT_VOCS_MAX_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#ga800092562173fd37826b5537feaac3ae)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_bt_cap_commander_change_volume_mute_state_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_bt_cap_commander_change_volume_offset_param_结构体.md)
