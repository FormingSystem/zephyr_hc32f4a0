---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-31
title: bt_cap_commander_distribute_broadcast_code_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__distribute__broadcast__code__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_bt\_cap\_commander\_distribute\_broadcast\_code\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__distribute__broadcast__code__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分发广播码的参数。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

分发广播码的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_a9605ad1590ff0279b46d639d38278933"></a>

```c
enum bt_cap_set_type type
```

相关声明：[bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)、[type](#a9605ad1590ff0279b46d639d38278933)。

集合类型（Set type）。

<a id="r_a03be4b2fac7803de233c8a1024640cc2"></a>

```c
struct bt_cap_commander_distribute_broadcast_code_member_param * param
```

相关声明：[bt_cap_commander_distribute_broadcast_code_member_param](P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md)、[param](#a03be4b2fac7803de233c8a1024640cc2)。

用于此过程的设备集合（Set of devices）。

<a id="r_a86316e3bf53edca67e0743072f0f2ee3"></a>

```c
size_t count
```

相关声明：[count](#a86316e3bf53edca67e0743072f0f2ee3)。

`param` 中的参数数量（Number of parameters）。

<a id="r_ac7d426c975c1e2324f52486abf9298b9"></a>

```c
uint8_t broadcast_code [BT_ISO_BROADCAST_CODE_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[broadcast_code](#ac7d426c975c1e2324f52486abf9298b9)、[BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)。

16 个八位组的广播代码（Broadcast code）。

## 31.2\_详细说明（Detailed Documentation）

<a id="ac7d426c975c1e2324f52486abf9298b9"></a>

### `broadcast_code`

```c
uint8_t bt_cap_commander_distribute_broadcast_code_param::broadcast_code[BT_ISO_BROADCAST_CODE_SIZE]
```

16 个八位组的广播代码（Broadcast code）。

如果该值是字符串，或者不足 16 个八位字节，则其余八位字节必须为 0。

例如，字符串 `"Broadcast Code"` 必须表示为 `[42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]`。

<a id="a86316e3bf53edca67e0743072f0f2ee3"></a>

### `count`

```c
size_t bt_cap_commander_distribute_broadcast_code_param::count
```

`param` 中的参数数量（Number of parameters）。

<a id="a03be4b2fac7803de233c8a1024640cc2"></a>

### `param`

```c
struct bt_cap_commander_distribute_broadcast_code_member_param* bt_cap_commander_distribute_broadcast_code_param::param
```

用于此过程的设备集合（Set of devices）。

<a id="a9605ad1590ff0279b46d639d38278933"></a>

### `type`

```c
enum bt_cap_set_type bt_cap_commander_distribute_broadcast_code_param::type
```

集合类型（Set type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [bt_cap_commander_distribute_broadcast_code_member_param](P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md)
