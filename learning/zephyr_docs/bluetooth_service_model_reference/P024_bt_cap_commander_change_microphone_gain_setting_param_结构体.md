---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-24
title: bt_cap_commander_change_microphone_gain_setting_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__microphone__gain__setting__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_bt\_cap\_commander\_change\_microphone\_gain\_setting\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__microphone__gain__setting__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

更改麦克风静音状态（Microphone Mute State）的参数。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

更改麦克风静音状态（Microphone Mute State）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_abac0f4da7b8b05067636539b2e9f9673"></a>

```c
enum bt_cap_set_type type
```

相关声明：[bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)、[type](#abac0f4da7b8b05067636539b2e9f9673)。

集合类型（Set type）。

<a id="r_ade5a93aee8bcff628228664c4a8428a8"></a>

```c
struct bt_cap_commander_change_microphone_gain_setting_member_param * param
```

相关声明：[bt_cap_commander_change_microphone_gain_setting_member_param](P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md)、[param](#ade5a93aee8bcff628228664c4a8428a8)。

用于此过程的设备集合（Set of devices）。

<a id="r_ae78e5d4761df00c8c8e2cfcb3e727349"></a>

```c
size_t count
```

相关声明：[count](#ae78e5d4761df00c8c8e2cfcb3e727349)。

`param` 中的参数数量（Number of parameters）。

## 24.2\_详细说明（Detailed Documentation）

<a id="ae78e5d4761df00c8c8e2cfcb3e727349"></a>

### `count`

```c
size_t bt_cap_commander_change_microphone_gain_setting_param::count
```

`param` 中的参数数量（Number of parameters）。

<a id="ade5a93aee8bcff628228664c4a8428a8"></a>

### `param`

```c
struct bt_cap_commander_change_microphone_gain_setting_member_param* bt_cap_commander_change_microphone_gain_setting_param::param
```

用于此过程的设备集合（Set of devices）。

<a id="abac0f4da7b8b05067636539b2e9f9673"></a>

### `type`

```c
enum bt_cap_set_type bt_cap_commander_change_microphone_gain_setting_param::type
```

集合类型（Set type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [bt_cap_commander_change_microphone_gain_setting_member_param](P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md)
