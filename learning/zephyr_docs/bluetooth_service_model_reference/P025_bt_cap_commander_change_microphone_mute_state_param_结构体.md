---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-25
title: bt_cap_commander_change_microphone_mute_state_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__microphone__mute__state__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_bt\_cap\_commander\_change\_microphone\_mute\_state\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__microphone__mute__state__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

更改麦克风静音状态（Microphone Mute State）的参数。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

更改麦克风静音状态（Microphone Mute State）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a9cdb1eda2108fc341a6d7268fac689b0"></a>

```c
enum bt_cap_set_type type
```

相关声明：[bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)、[type](#a9cdb1eda2108fc341a6d7268fac689b0)。

集合类型（Set type）。

<a id="r_a9c989fe2446ee2e055778c063a6b6de1"></a>

```c
union bt_cap_set_member * members
```

相关声明：[bt_cap_set_member](P188_bt_cap_set_member_联合体.md)、[members](#a9c989fe2446ee2e055778c063a6b6de1)。

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="r_a96007101444d3cd61dda067fa072580e"></a>

```c
size_t count
```

相关声明：[count](#a96007101444d3cd61dda067fa072580e)。

`members` 中的成员数量（Number of members）。

<a id="r_a1b6e22c9c41eb24b3961927b45c98af8"></a>

```c
bool mute
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[mute](#a1b6e22c9c41eb24b3961927b45c98af8)。

要设置的麦克风静音状态（Microphone mute state）。

## 25.2\_详细说明（Detailed Documentation）

<a id="a96007101444d3cd61dda067fa072580e"></a>

### `count`

```c
size_t bt_cap_commander_change_microphone_mute_state_param::count
```

`members` 中的成员数量（Number of members）。

<a id="a9c989fe2446ee2e055778c063a6b6de1"></a>

### `members`

```c
union bt_cap_set_member* bt_cap_commander_change_microphone_mute_state_param::members
```

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="a1b6e22c9c41eb24b3961927b45c98af8"></a>

### `mute`

```c
bool bt_cap_commander_change_microphone_mute_state_param::mute
```

要设置的麦克风静音状态（Microphone mute state）。

`true` 表示静音（Mute），`false` 表示取消静音（Unmute）。

<a id="a9cdb1eda2108fc341a6d7268fac689b0"></a>

### `type`

```c
enum bt_cap_set_type bt_cap_commander_change_microphone_mute_state_param::type
```

集合类型（Set type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [bt_cap_set_member](P188_bt_cap_set_member_联合体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_bt_cap_commander_change_volume_mute_state_param_结构体.md)
