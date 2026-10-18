---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-21
title: bt_cap_commander_broadcast_reception_stop_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__broadcast__reception__stop__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_bt\_cap\_commander\_broadcast\_reception\_stop\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__broadcast__reception__stop__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

停止广播接收的参数。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

停止广播接收的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_a35bc972b00c10b90544da19c659fc460"></a>

```c
enum bt_cap_set_type type
```

相关声明：[bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)、[type](#a35bc972b00c10b90544da19c659fc460)。

集合类型（Set type）。

<a id="r_a36ce7cd132cd41a55872985433c2934d"></a>

```c
struct bt_cap_commander_broadcast_reception_stop_member_param * param
```

相关声明：[bt_cap_commander_broadcast_reception_stop_member_param](P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md)、[param](#a36ce7cd132cd41a55872985433c2934d)。

用于此过程的设备集合（Set of devices）。

<a id="r_add81cdf1e3bad07b43602c8ce7c47593"></a>

```c
size_t count
```

相关声明：[count](#add81cdf1e3bad07b43602c8ce7c47593)。

`param` 中的参数数量（Number of parameters）。

## 21.2\_详细说明（Detailed Documentation）

<a id="add81cdf1e3bad07b43602c8ce7c47593"></a>

### `count`

```c
size_t bt_cap_commander_broadcast_reception_stop_param::count
```

`param` 中的参数数量（Number of parameters）。

<a id="a36ce7cd132cd41a55872985433c2934d"></a>

### `param`

```c
struct bt_cap_commander_broadcast_reception_stop_member_param* bt_cap_commander_broadcast_reception_stop_param::param
```

用于此过程的设备集合（Set of devices）。

<a id="a35bc972b00c10b90544da19c659fc460"></a>

### `type`

```c
enum bt_cap_set_type bt_cap_commander_broadcast_reception_stop_param::type
```

集合类型（Set type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [bt_cap_commander_broadcast_reception_stop_member_param](P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_bt_cap_commander_cb_结构体.md)
