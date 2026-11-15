---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-29
title: bt_cap_commander_change_volume_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__volume__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_bt\_cap\_commander\_change\_volume\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__volume__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

更改绝对音量（Absolute Volume）的参数。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

更改绝对音量（Absolute Volume）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_ad98625aa08f54759efd349921d104c88"></a>

```c
enum bt_cap_set_type type
```

相关声明：[bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)、[type](#ad98625aa08f54759efd349921d104c88)。

集合类型（Set type）。

<a id="r_a983656766a28118b018a70fef186f531"></a>

```c
union bt_cap_set_member * members
```

相关声明：[bt_cap_set_member](P188_bt_cap_set_member_联合体.md)、[members](#a983656766a28118b018a70fef186f531)。

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="r_a37198e9118f80e5521f140b6aa1d2640"></a>

```c
size_t count
```

相关声明：[count](#a37198e9118f80e5521f140b6aa1d2640)。

`members` 中的成员数量（Number of members）。

<a id="r_ada17f89c8948246d68818f2e44d5ea49"></a>

```c
uint8_t volume
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[volume](#ada17f89c8948246d68818f2e44d5ea49)。

要设置的绝对音量（Absolute volume）。

## 29.2\_详细说明（Detailed Documentation）

<a id="a37198e9118f80e5521f140b6aa1d2640"></a>

### `count`

```c
size_t bt_cap_commander_change_volume_param::count
```

`members` 中的成员数量（Number of members）。

<a id="a983656766a28118b018a70fef186f531"></a>

### `members`

```c
union bt_cap_set_member* bt_cap_commander_change_volume_param::members
```

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="ad98625aa08f54759efd349921d104c88"></a>

### `type`

```c
enum bt_cap_set_type bt_cap_commander_change_volume_param::type
```

集合类型（Set type）。

<a id="ada17f89c8948246d68818f2e44d5ea49"></a>

### `volume`

```c
uint8_t bt_cap_commander_change_volume_param::volume
```

要设置的绝对音量（Absolute volume）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [bt_cap_set_member](P188_bt_cap_set_member_联合体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_bt_cap_commander_change_volume_offset_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md)
