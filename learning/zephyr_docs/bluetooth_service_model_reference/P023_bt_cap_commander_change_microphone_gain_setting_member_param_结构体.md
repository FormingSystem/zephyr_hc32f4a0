---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-23
title: bt_cap_commander_change_microphone_gain_setting_member_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__microphone__gain__setting__member__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__microphone__gain__setting__member__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_commander_change_microphone_gain_setting_param` 中供 `bt_cap_commander_change_microphone_gain_setting()` 使用的参数部分。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_commander_change_microphone_gain_setting_param` 中供 `bt_cap_commander_change_microphone_gain_setting()` 使用的参数部分。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_a5cc34236153e6a737f71cbc77f5f840e"></a>

```c
union bt_cap_set_member member
```

相关声明：[bt_cap_set_member](P188_bt_cap_set_member_联合体.md)、[member](#a5cc34236153e6a737f71cbc77f5f840e)。

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="r_a8fdcc5ec143b5a73c369d6e15d276196"></a>

```c
int8_t gain
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[gain](#a8fdcc5ec143b5a73c369d6e15d276196)。

要设置的麦克风增益（Microphone gain setting）。

## 23.2\_详细说明（Detailed Documentation）

<a id="a8fdcc5ec143b5a73c369d6e15d276196"></a>

### `gain`

```c
int8_t bt_cap_commander_change_microphone_gain_setting_member_param::gain
```

要设置的麦克风增益（Microphone gain setting）。

<a id="a5cc34236153e6a737f71cbc77f5f840e"></a>

### `member`

```c
union bt_cap_set_member bt_cap_commander_change_microphone_gain_setting_member_param::member
```

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 23.3\_原页交叉引用（Cross References）

- [bt_cap_commander_change_microphone_gain_setting_param](P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md)
- [bt_cap_commander_change_microphone_gain_setting()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga958cd5925699624d23479ad2ace6b55b)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_member](P188_bt_cap_set_member_联合体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_bt_cap_commander_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md)
