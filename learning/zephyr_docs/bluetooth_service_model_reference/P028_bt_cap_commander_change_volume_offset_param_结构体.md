---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-28
title: bt_cap_commander_change_volume_offset_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__volume__offset__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_bt\_cap\_commander\_change\_volume\_offset\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__change__volume__offset__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

更改音量偏移（Volume Offset）的参数。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

更改音量偏移（Volume Offset）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_a8c22810a91d3109c3d633156bf16dffd"></a>

```c
enum bt_cap_set_type type
```

相关声明：[bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)、[type](#a8c22810a91d3109c3d633156bf16dffd)。

集合类型（Set type）。

<a id="r_a2610505f60d1a67ffef916dadefe841d"></a>

```c
struct bt_cap_commander_change_volume_offset_member_param * param
```

相关声明：[bt_cap_commander_change_volume_offset_member_param](P027_bt_cap_commander_change_volume_offset_member_param_结构体.md)、[param](#a2610505f60d1a67ffef916dadefe841d)。

用于此过程的设备集合（Set of devices）。

<a id="r_ae3d416680196b0ee753a80d6fccb468b"></a>

```c
size_t count
```

相关声明：[count](#ae3d416680196b0ee753a80d6fccb468b)。

`param` 中的参数数量（Number of parameters）。

## 28.2\_详细说明（Detailed Documentation）

<a id="ae3d416680196b0ee753a80d6fccb468b"></a>

### `count`

```c
size_t bt_cap_commander_change_volume_offset_param::count
```

`param` 中的参数数量（Number of parameters）。

<a id="a2610505f60d1a67ffef916dadefe841d"></a>

### `param`

```c
struct bt_cap_commander_change_volume_offset_member_param* bt_cap_commander_change_volume_offset_param::param
```

用于此过程的设备集合（Set of devices）。

<a id="a8c22810a91d3109c3d633156bf16dffd"></a>

### `type`

```c
enum bt_cap_set_type bt_cap_commander_change_volume_offset_param::type
```

集合类型（Set type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [bt_cap_commander_change_volume_offset_member_param](P027_bt_cap_commander_change_volume_offset_member_param_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_bt_cap_commander_change_volume_offset_member_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_bt_cap_commander_change_volume_param_结构体.md)
