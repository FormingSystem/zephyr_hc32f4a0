---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-21
title: bt_bap_broadcast_source_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__source__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_bt\_bap\_broadcast\_source\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__source__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

广播音频源创建参数（Broadcast Source Create Parameters）。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

广播音频源创建参数（Broadcast Source Create Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_a5e155c3b92b4f9de3c9e6efa377097e3"></a>

```c
size_t params_count
```

相关声明：[params_count](#a5e155c3b92b4f9de3c9e6efa377097e3)。

`subgroup_params` 中的参数数量。

<a id="r_a6291842b49a55f6b2767dc95c9e874f3"></a>

```c
struct bt_bap_broadcast_source_subgroup_param * params
```

相关声明：[bt_bap_broadcast_source_subgroup_param](P023_bt_bap_broadcast_source_subgroup_param_结构体.md)、[params](#a6291842b49a55f6b2767dc95c9e874f3)。

流参数数组（Stream Parameters Array）。

<a id="r_a71abc0496153a9b8eab402bfaaf92e72"></a>

```c
const struct bt_bap_qos_cfg * qos
```

相关声明：[bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)、[qos](#a71abc0496153a9b8eab402bfaaf92e72)。

服务质量配置（Quality of Service Configuration）。

<a id="r_a493fa57a80e21a288854b2e3e1df775a"></a>

```c
uint8_t packing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packing](#a493fa57a80e21a288854b2e3e1df775a)。

广播音频源的打包模式（Packing Mode）。

<a id="r_a7552bf9a4ff5441b13669effe23abb8c"></a>

```c
bool encryption
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[encryption](#a7552bf9a4ff5441b13669effe23abb8c)。

是否加密各条流。

<a id="r_a6a05b6448f55cf5f52f90e44d83146dc"></a>

```c
uint8_t broadcast_code [BT_ISO_BROADCAST_CODE_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[broadcast_code](#a6a05b6448f55cf5f52f90e44d83146dc)、[BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)。

广播码（Broadcast Code）。

<a id="r_aab1799ab671500b02c1ab0e023ac43f7"></a>

```c
uint8_t irc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[irc](#aab1799ab671500b02c1ab0e023ac43f7)。

即时重复计数（Immediate Repetition Count）。

<a id="r_a50c29b5a2bcae162c0bbda32102a30cc"></a>

```c
uint8_t pto
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pto](#a50c29b5a2bcae162c0bbda32102a30cc)。

预传输偏移（Pre-transmission Offset）。

<a id="r_a11b03e3d63ca2e116e743d9efde920be"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#a11b03e3d63ca2e116e743d9efde920be)。

等时间隔（ISO Interval）。

## 21.2\_详细说明（Detailed Documentation）

<a id="a6a05b6448f55cf5f52f90e44d83146dc"></a>

### `broadcast_code`

```c
uint8_t bt_bap_broadcast_source_param::broadcast_code[BT_ISO_BROADCAST_CODE_SIZE]
```

广播码（Broadcast Code）。

如果该值是字符串，或者不足 16 个八位字节，则其余八位字节必须为 0。

例如，字符串 `"Broadcast Code"` 必须表示为 `[42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]`。

<a id="a7552bf9a4ff5441b13669effe23abb8c"></a>

### `encryption`

```c
bool bt_bap_broadcast_source_param::encryption
```

是否加密各条流。

<a id="aab1799ab671500b02c1ab0e023ac43f7"></a>

### `irc`

```c
uint8_t bt_bap_broadcast_source_param::irc
```

即时重复计数（Immediate Repetition Count）。

给定事件中已调度载荷的传输次数。

取值范围为 `BT_ISO_IRC_MIN` 到 `BT_ISO_IRC_MAX`。

<a id="a11b03e3d63ca2e116e743d9efde920be"></a>

### `iso_interval`

```c
uint16_t bt_bap_broadcast_source_param::iso_interval
```

等时间隔（ISO Interval）。

相邻 BIS 锚点（Anchor Points）之间的时间。

取值范围为 `BT_ISO_ISO_INTERVAL_MIN` 到 `BT_ISO_ISO_INTERVAL_MAX`。

<a id="a493fa57a80e21a288854b2e3e1df775a"></a>

### `packing`

```c
uint8_t bt_bap_broadcast_source_param::packing
```

广播音频源的打包模式（Packing Mode）。

`BT_ISO_PACKING_SEQUENTIAL` 或 `BT_ISO_PACKING_INTERLEAVED`。

说明（Note）：这是向控制器提出的建议，控制器可以忽略它。

<a id="a6291842b49a55f6b2767dc95c9e874f3"></a>

### `params`

```c
struct bt_bap_broadcast_source_subgroup_param* bt_bap_broadcast_source_param::params
```

流参数数组（Stream Parameters Array）。

<a id="a5e155c3b92b4f9de3c9e6efa377097e3"></a>

### `params_count`

```c
size_t bt_bap_broadcast_source_param::params_count
```

`subgroup_params` 中的参数数量。

<a id="a50c29b5a2bcae162c0bbda32102a30cc"></a>

### `pto`

```c
uint8_t bt_bap_broadcast_source_param::pto
```

预传输偏移（Pre-transmission Offset）。

预传输使用的偏移量（Offset）。

取值范围为 `BT_ISO_PTO_MIN` 到 `BT_ISO_PTO_MAX`。

<a id="a71abc0496153a9b8eab402bfaaf92e72"></a>

### `qos`

```c
const struct bt_bap_qos_cfg* bt_bap_broadcast_source_param::qos
```

服务质量配置（Quality of Service Configuration）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_bap_broadcast_source_subgroup_param](P023_bt_bap_broadcast_source_subgroup_param_结构体.md)
- [bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_ISO_IRC_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga52df7bd114b77872c084e28ca86e0b2e)
- [BT_ISO_IRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0f412f1593bcdcfa2b323b285bd508a4)
- [BT_ISO_ISO_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de)
- [BT_ISO_ISO_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gabc381a7f565061ec91d23b7783521da3)
- [BT_ISO_PACKING_SEQUENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga6275e8d805e2366522a78f18ca47ac19)
- [BT_ISO_PACKING_INTERLEAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga35b037fcce858857642b4c54bae8dd79)
- [BT_ISO_PTO_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3f19aaa432290d67fdf4911d1d044dd8)
- [BT_ISO_PTO_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga27e812e35a1f12329310851eb9c056f2)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_bt_bap_broadcast_source_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_bt_bap_broadcast_source_stream_param_结构体.md)
