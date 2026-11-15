---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-32
title: bt_cap_handover_broadcast_to_unicast_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__handover__broadcast__to__unicast__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_bt\_cap\_handover\_broadcast\_to\_unicast\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__handover__broadcast__to__unicast__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_handover_broadcast_to_unicast()` 的参数（Parameters）。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_handover_broadcast_to_unicast()` 的参数（Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_af0e79651b30c14a6bfd218203236e954"></a>

```c
struct bt_cap_commander_broadcast_reception_stop_param * reception_stop_param
```

相关声明：[bt_cap_commander_broadcast_reception_stop_param](P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md)、[reception_stop_param](#af0e79651b30c14a6bfd218203236e954)。

用于停止接受方广播音频接收的参数（Broadcast audio reception stop parameters）。

<a id="r_a39721b75c4cf2bd626427a63602d4aef"></a>

```c
uint32_t broadcast_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[broadcast_id](#a39721b75c4cf2bd626427a63602d4aef)。

`broadcast_source` 的广播标识符（Broadcast ID）。

<a id="r_aa43bd1c2e14ecb1c652a170893f7d1ab"></a>

```c
uint8_t adv_sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_sid](#aa43bd1c2e14ecb1c652a170893f7d1ab)。

`broadcast_source` 的广播集标识符（Advertising set ID）。

<a id="r_a3f476e4ff18e4ca2b54fa495ec862718"></a>

```c
uint8_t adv_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_type](#a3f476e4ff18e4ca2b54fa495ec862718)。

`broadcast_source` 广播地址的广播类型（Advertising type）。

<a id="r_a7cfe18cca6342c653e30de247d896c84"></a>

```c
struct bt_cap_broadcast_source * broadcast_source
```

相关声明：[bt_cap_broadcast_source](P017_bt_cap_broadcast_source_结构体.md)、[broadcast_source](#a7cfe18cca6342c653e30de247d896c84)。

包含这些流的源广播源（Source broadcast source）。

<a id="r_ac133453b820f16472ee1537ee84b5205"></a>

```c
struct bt_cap_unicast_group_param * unicast_group_param
```

相关声明：[bt_cap_unicast_group_param](P047_bt_cap_unicast_group_param_结构体.md)、[unicast_group_param](#ac133453b820f16472ee1537ee84b5205)。

待创建的单播组参数（Unicast group parameters）。

<a id="r_a1d94cd5237f209fd8617bc10dd953b18"></a>

```c
struct bt_cap_unicast_audio_start_param * unicast_start_param
```

相关声明：[bt_cap_unicast_audio_start_param](P040_bt_cap_unicast_audio_start_param_结构体.md)、[unicast_start_param](#a1d94cd5237f209fd8617bc10dd953b18)。

启动单播音频的参数（Unicast audio start parameters）。

## 32.2\_详细说明（Detailed Documentation）

<a id="aa43bd1c2e14ecb1c652a170893f7d1ab"></a>

### `adv_sid`

```c
uint8_t bt_cap_handover_broadcast_to_unicast_param::adv_sid
```

`broadcast_source` 的广播集标识符（Advertising set ID）。

`reception_stop_param` 非 `NULL` 时忽略此项。

<a id="a3f476e4ff18e4ca2b54fa495ec862718"></a>

### `adv_type`

```c
uint8_t bt_cap_handover_broadcast_to_unicast_param::adv_type
```

`broadcast_source` 广播地址的广播类型（Advertising type）。

`reception_stop_param` 非 `NULL` 时忽略此项。

<a id="a39721b75c4cf2bd626427a63602d4aef"></a>

### `broadcast_id`

```c
uint32_t bt_cap_handover_broadcast_to_unicast_param::broadcast_id
```

`broadcast_source` 的广播标识符（Broadcast ID）。

`reception_stop_param` 非 `NULL` 时忽略此项。

<a id="a7cfe18cca6342c653e30de247d896c84"></a>

### `broadcast_source`

```c
struct bt_cap_broadcast_source* bt_cap_handover_broadcast_to_unicast_param::broadcast_source
```

包含这些流的源广播源（Source broadcast source）。

广播源（Broadcast source）将被停止并删除。

<a id="af0e79651b30c14a6bfd218203236e954"></a>

### `reception_stop_param`

```c
struct bt_cap_commander_broadcast_reception_stop_param* bt_cap_handover_broadcast_to_unicast_param::reception_stop_param
```

用于停止接受方广播音频接收的参数（Broadcast audio reception stop parameters）。

此参数为可选，因为停止广播音频应会自动停止接受方（Acceptors）的广播音频接收。省略此参数时，将依赖通用音频规范接受方（CAP acceptors）在广播等时组（BIG）停止后超时。CAP 接受方的超时在 `BT_ISO_SYNC_TIMEOUT_MIN` 与 `BT_ISO_SYNC_TIMEOUT_MAX` 之间。

<a id="ac133453b820f16472ee1537ee84b5205"></a>

### `unicast_group_param`

```c
struct bt_cap_unicast_group_param* bt_cap_handover_broadcast_to_unicast_param::unicast_group_param
```

待创建的单播组参数（Unicast group parameters）。

<a id="a1d94cd5237f209fd8617bc10dd953b18"></a>

### `unicast_start_param`

```c
struct bt_cap_unicast_audio_start_param* bt_cap_handover_broadcast_to_unicast_param::unicast_start_param
```

启动单播音频的参数（Unicast audio start parameters）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 32.3\_原页交叉引用（Cross References）

- [bt_cap_handover_broadcast_to_unicast()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92ff8b3133b8f5cb3d3029b5d556fe77)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_commander_broadcast_reception_stop_param](P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_cap_broadcast_source](P017_bt_cap_broadcast_source_结构体.md)
- [bt_cap_unicast_group_param](P047_bt_cap_unicast_group_param_结构体.md)
- [bt_cap_unicast_audio_start_param](P040_bt_cap_unicast_audio_start_param_结构体.md)
- [BT_ISO_SYNC_TIMEOUT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa1bd6484a248a6fb5abc31202e5076d4)
- [BT_ISO_SYNC_TIMEOUT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaeb66806b649bf828afbd83d15c9823eb)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_bt_cap_handover_cb_结构体.md)
