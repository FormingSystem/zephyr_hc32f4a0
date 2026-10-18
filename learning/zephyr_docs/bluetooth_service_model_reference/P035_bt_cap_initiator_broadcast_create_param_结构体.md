---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-35
title: bt_cap_initiator_broadcast_create_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__broadcast__create__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_bt\_cap\_initiator\_broadcast\_create\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__broadcast__create__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_initiator_broadcast_audio_create()` 的参数。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_initiator_broadcast_audio_create()` 的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_aee3e0244b59503311bc445f36977a85b"></a>

```c
size_t subgroup_count
```

相关声明：[subgroup_count](#aee3e0244b59503311bc445f36977a85b)。

`subgroup_params` 中的参数数量。

<a id="r_a2eafc157450237cf311d6144e7431839"></a>

```c
struct bt_cap_initiator_broadcast_subgroup_param * subgroup_params
```

相关声明：[bt_cap_initiator_broadcast_subgroup_param](P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md)、[subgroup_params](#a2eafc157450237cf311d6144e7431839)。

流参数数组（Stream Parameters Array）。

<a id="r_aaa6f2828416b0624b8ca15fb2139413f"></a>

```c
const struct bt_bap_qos_cfg * qos
```

相关声明：[bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)、[qos](#aaa6f2828416b0624b8ca15fb2139413f)。

服务质量配置（Quality of Service Configuration）。

<a id="r_ae81ee3dada58a3354c70401380916cbc"></a>

```c
uint8_t packing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packing](#ae81ee3dada58a3354c70401380916cbc)。

广播音频源的打包模式（Packing Mode）。

<a id="r_a4432bee0e365c189996b9f70c7226542"></a>

```c
bool encryption
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[encryption](#a4432bee0e365c189996b9f70c7226542)。

是否加密各条流。

<a id="r_aa4d6fbd5bd13963004e381b987bbeb4d"></a>

```c
uint8_t broadcast_code [BT_ISO_BROADCAST_CODE_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[broadcast_code](#aa4d6fbd5bd13963004e381b987bbeb4d)、[BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)。

16 个八位组的广播代码（Broadcast code）。

<a id="r_a6f562b7a696472b7784ca2e1ced4997a"></a>

```c
uint8_t irc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[irc](#a6f562b7a696472b7784ca2e1ced4997a)。

即时重复计数（Immediate Repetition Count）。

<a id="r_a01d6ffb369caaf808d4b55b3b1748890"></a>

```c
uint8_t pto
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pto](#a01d6ffb369caaf808d4b55b3b1748890)。

预传输偏移（Pre-transmission Offset）。

<a id="r_a8eedd8f9a896931f75642576ca37c7d5"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#a8eedd8f9a896931f75642576ca37c7d5)。

等时间隔（ISO Interval）。

## 35.2\_详细说明（Detailed Documentation）

<a id="aa4d6fbd5bd13963004e381b987bbeb4d"></a>

### `broadcast_code`

```c
uint8_t bt_cap_initiator_broadcast_create_param::broadcast_code[BT_ISO_BROADCAST_CODE_SIZE]
```

16 个八位组的广播代码（Broadcast code）。

仅当 `encrypt` 为 `true` 时有效。

如果该值是字符串，或者不足 16 个八位字节，则其余八位字节必须为 0。

例如，字符串 `"Broadcast Code"` 必须表示为 `[42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]`。

<a id="a4432bee0e365c189996b9f70c7226542"></a>

### `encryption`

```c
bool bt_cap_initiator_broadcast_create_param::encryption
```

是否加密各条流。

<a id="a6f562b7a696472b7784ca2e1ced4997a"></a>

### `irc`

```c
uint8_t bt_cap_initiator_broadcast_create_param::irc
```

即时重复计数（Immediate Repetition Count）。

给定事件中已调度载荷的传输次数。

取值范围为 `BT_ISO_IRC_MIN` 到 `BT_ISO_IRC_MAX`。

<a id="a8eedd8f9a896931f75642576ca37c7d5"></a>

### `iso_interval`

```c
uint16_t bt_cap_initiator_broadcast_create_param::iso_interval
```

等时间隔（ISO Interval）。

相邻 BIS 锚点（Anchor Points）之间的时间。

取值范围为 `BT_ISO_ISO_INTERVAL_MIN` 到 `BT_ISO_ISO_INTERVAL_MAX`。

<a id="ae81ee3dada58a3354c70401380916cbc"></a>

### `packing`

```c
uint8_t bt_cap_initiator_broadcast_create_param::packing
```

广播音频源的打包模式（Packing Mode）。

`BT_ISO_PACKING_SEQUENTIAL` 或 `BT_ISO_PACKING_INTERLEAVED`。

说明（Note）：这是向控制器提出的建议，控制器可以忽略它。

<a id="a01d6ffb369caaf808d4b55b3b1748890"></a>

### `pto`

```c
uint8_t bt_cap_initiator_broadcast_create_param::pto
```

预传输偏移（Pre-transmission Offset）。

预传输使用的偏移量（Offset）。

取值范围为 `BT_ISO_PTO_MIN` 到 `BT_ISO_PTO_MAX`。

<a id="aaa6f2828416b0624b8ca15fb2139413f"></a>

### `qos`

```c
const struct bt_bap_qos_cfg* bt_cap_initiator_broadcast_create_param::qos
```

服务质量配置（Quality of Service Configuration）。

<a id="aee3e0244b59503311bc445f36977a85b"></a>

### `subgroup_count`

```c
size_t bt_cap_initiator_broadcast_create_param::subgroup_count
```

`subgroup_params` 中的参数数量。

<a id="a2eafc157450237cf311d6144e7431839"></a>

### `subgroup_params`

```c
struct bt_cap_initiator_broadcast_subgroup_param* bt_cap_initiator_broadcast_create_param::subgroup_params
```

流参数数组（Stream Parameters Array）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 35.3\_原页交叉引用（Cross References）

- [bt_cap_initiator_broadcast_audio_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga78697225c6b1291dfc016e20fd605fc4)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_initiator_broadcast_subgroup_param](P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md)
- [bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)
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

[上一章](P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_bt_cap_initiator_broadcast_stream_param_结构体.md)
