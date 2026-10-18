---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-19
title: bt_cap_commander_broadcast_reception_start_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__broadcast__reception__start__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_bt\_cap\_commander\_broadcast\_reception\_start\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__broadcast__reception__start__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

启动广播接收（Broadcast Reception）的参数。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

启动广播接收（Broadcast Reception）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_ae4c1e6d7b345b8764f695ada56483aa1"></a>

```c
enum bt_cap_set_type type
```

相关声明：[bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)、[type](#ae4c1e6d7b345b8764f695ada56483aa1)。

集合类型（Set type）。

<a id="r_a8bac9170f48f34fd2239da9a6d994041"></a>

```c
struct bt_cap_commander_broadcast_reception_start_member_param * param
```

相关声明：[bt_cap_commander_broadcast_reception_start_member_param](P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md)、[param](#a8bac9170f48f34fd2239da9a6d994041)。

用于此过程的设备集合（Set of devices）。

<a id="r_ab0fe6fe27946a349ac33f11526ca13b7"></a>

```c
size_t count
```

相关声明：[count](#ab0fe6fe27946a349ac33f11526ca13b7)。

`param` 中的参数数量（Number of parameters）。

## 19.2\_详细说明（Detailed Documentation）

<a id="ab0fe6fe27946a349ac33f11526ca13b7"></a>

### `count`

```c
size_t bt_cap_commander_broadcast_reception_start_param::count
```

`param` 中的参数数量（Number of parameters）。

<a id="a8bac9170f48f34fd2239da9a6d994041"></a>

### `param`

```c
struct bt_cap_commander_broadcast_reception_start_member_param* bt_cap_commander_broadcast_reception_start_param::param
```

用于此过程的设备集合（Set of devices）。

<a id="ae4c1e6d7b345b8764f695ada56483aa1"></a>

### `type`

```c
enum bt_cap_set_type bt_cap_commander_broadcast_reception_start_param::type
```

集合类型（Set type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [bt_cap_commander_broadcast_reception_start_member_param](P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md)
