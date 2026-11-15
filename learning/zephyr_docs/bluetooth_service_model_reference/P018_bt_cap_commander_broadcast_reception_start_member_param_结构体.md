---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-18
title: bt_cap_commander_broadcast_reception_start_member_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__broadcast__reception__start__member__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_bt\_cap\_commander\_broadcast\_reception\_start\_member\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__broadcast__reception__start__member__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_commander_broadcast_reception_start_param` 中供 `bt_cap_commander_broadcast_reception_start()` 使用的参数部分。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_commander_broadcast_reception_start_param` 中供 `bt_cap_commander_broadcast_reception_start()` 使用的参数部分。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_abf47aafab0b076da675182308d89bff7"></a>

```c
union bt_cap_set_member member
```

相关声明：[bt_cap_set_member](P188_bt_cap_set_member_联合体.md)、[member](#abf47aafab0b076da675182308d89bff7)。

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="r_a93d6b4c76e730f282d24b2086c10aa3e"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a93d6b4c76e730f282d24b2086c10aa3e)。

广播者（Advertiser）的地址。

<a id="r_acc52738756124db042ea884c82163362"></a>

```c
uint8_t adv_sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_sid](#acc52738756124db042ea884c82163362)。

广播集（Advertising Set）的 SID。

<a id="r_a1ba6b20f822f38dd4a0ce1f8b2f2671c"></a>

```c
uint16_t pa_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pa_interval](#a1ba6b20f822f38dd4a0ce1f8b2f2671c)。

周期性广播间隔，单位为毫秒。

<a id="r_a8e6d5d1004d13069739229a7eec3abc0"></a>

```c
uint32_t broadcast_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[broadcast_id](#a8e6d5d1004d13069739229a7eec3abc0)。

24 位广播 ID。

<a id="r_a2222f8ae46afed4760db56079779532d"></a>

```c
struct bt_bap_bass_subgroup subgroups [BT_BAP_BASS_MAX_SUBGROUPS]
```

相关声明：[bt_bap_bass_subgroup](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md)、[subgroups](#a2222f8ae46afed4760db56079779532d)、[BT_BAP_BASS_MAX_SUBGROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga443c212a736852305715452e7f165a9e)。

指向子组数组的指针。

<a id="r_a184f2623ab759832a3ec9770b14c9c63"></a>

```c
size_t num_subgroups
```

相关声明：[num_subgroups](#a184f2623ab759832a3ec9770b14c9c63)。

子组数量。

## 18.2\_详细说明（Detailed Documentation）

<a id="a93d6b4c76e730f282d24b2086c10aa3e"></a>

### `addr`

```c
bt_addr_le_t bt_cap_commander_broadcast_reception_start_member_param::addr
```

广播者（Advertiser）的地址。

<a id="acc52738756124db042ea884c82163362"></a>

### `adv_sid`

```c
uint8_t bt_cap_commander_broadcast_reception_start_member_param::adv_sid
```

广播集（Advertising Set）的 SID。

<a id="a8e6d5d1004d13069739229a7eec3abc0"></a>

### `broadcast_id`

```c
uint32_t bt_cap_commander_broadcast_reception_start_member_param::broadcast_id
```

24 位广播 ID。

<a id="abf47aafab0b076da675182308d89bff7"></a>

### `member`

```c
union bt_cap_set_member bt_cap_commander_broadcast_reception_start_member_param::member
```

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="a184f2623ab759832a3ec9770b14c9c63"></a>

### `num_subgroups`

```c
size_t bt_cap_commander_broadcast_reception_start_member_param::num_subgroups
```

子组数量。

<a id="a1ba6b20f822f38dd4a0ce1f8b2f2671c"></a>

### `pa_interval`

```c
uint16_t bt_cap_commander_broadcast_reception_start_member_param::pa_interval
```

周期性广播间隔，单位为毫秒。

未知时使用 `BT_BAP_PA_INTERVAL_UNKNOWN`。

<a id="a2222f8ae46afed4760db56079779532d"></a>

### `subgroups`

```c
struct bt_bap_bass_subgroup bt_cap_commander_broadcast_reception_start_member_param::subgroups[BT_BAP_BASS_MAX_SUBGROUPS]
```

指向子组数组的指针。

至少必须在某个子组（Subgroup）的 `bis_sync` 参数中设置一位。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 18.3\_原页交叉引用（Cross References）

- [bt_cap_commander_broadcast_reception_start_param](P019_bt_cap_commander_broadcast_reception_start_param_结构体.md)
- [bt_cap_commander_broadcast_reception_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga25be83bb53c8e2ab76f311eaf4f615b9)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_member](P188_bt_cap_set_member_联合体.md)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_bap_bass_subgroup](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md)
- [BT_BAP_BASS_MAX_SUBGROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga443c212a736852305715452e7f165a9e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_bt_cap_broadcast_source_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_bt_cap_commander_broadcast_reception_start_param_结构体.md)
