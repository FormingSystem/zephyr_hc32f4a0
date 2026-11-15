---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-73
title: bt_iso_big_create_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__big__create__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_bt\_iso\_big\_create\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__big__create__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

广播等时组（Broadcast Isochronous Group，BIG）的创建参数。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

广播等时组（Broadcast Isochronous Group，BIG）的创建参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 73.1\_数据成员（Data Fields）

<a id="r_a7548bbb75f240a70435cb86a48846d0a"></a>

```c
struct bt_iso_chan ** bis_channels
```

相关声明：[bt_iso_chan](P077_bt_iso_chan_结构体.md)、[bis_channels](#a7548bbb75f240a70435cb86a48846d0a)。

广播等时流通道指针数组（BIS channel pointers）。

<a id="r_a8ae9c225798e9f5b72fe0b8c3b6f2cf0"></a>

```c
uint8_t num_bis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_bis](#a8ae9c225798e9f5b72fe0b8c3b6f2cf0)。

`bis_channels` 中的通道数量（Number of channels）。

<a id="r_a7aaef1f7a78ae1088886a78739fd6849"></a>

```c
uint32_t interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[interval](#a7aaef1f7a78ae1088886a78739fd6849)。

通道间隔（Channel interval），单位为微秒。

<a id="r_ab847021da2e604036cecf90483e12132"></a>

```c
uint16_t latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[latency](#ab847021da2e604036cecf90483e12132)。

通道延迟（Channel Latency），单位为毫秒。

<a id="r_ad478d7b36fb34b8e57a25ae0029e4c51"></a>

```c
uint8_t packing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packing](#ad478d7b36fb34b8e57a25ae0029e4c51)。

通道打包模式（Channel packing mode）。

<a id="r_aab0e9f66cb10643e72d6382718ed4c0d"></a>

```c
uint8_t framing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[framing](#aab0e9f66cb10643e72d6382718ed4c0d)。

通道成帧模式（Channel framing mode）。

<a id="r_a1288fa2a8f6bb3e2ab26729e245277e1"></a>

```c
bool encryption
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[encryption](#a1288fa2a8f6bb3e2ab26729e245277e1)。

是否加密各条流。

<a id="r_ae7a68301c2a0ea7a81812581f3ab1e61"></a>

```c
uint8_t bcode [0x10]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bcode](#ae7a68301c2a0ea7a81812581f3ab1e61)。

广播码（Broadcast Code）。

<a id="r_ad931ff1f19f92c29c40d934346498e79"></a>

```c
uint8_t irc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[irc](#ad931ff1f19f92c29c40d934346498e79)。

即时重复计数（Immediate Repetition Count）。

<a id="r_affce506bd271d9b0e497160c163c5798"></a>

```c
uint8_t pto
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pto](#affce506bd271d9b0e497160c163c5798)。

预传输偏移（Pre-transmission Offset）。

<a id="r_a63cd16824e9d09e29d3c7e135b08d932"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#a63cd16824e9d09e29d3c7e135b08d932)。

等时间隔（ISO Interval）。

## 73.2\_详细说明（Detailed Documentation）

<a id="ae7a68301c2a0ea7a81812581f3ab1e61"></a>

### `bcode`

```c
uint8_t bt_iso_big_create_param::bcode[0x10]
```

广播码（Broadcast Code）。

用于派生会话密钥（Session key）的代码；该密钥用于加密和解密广播等时流载荷（BIS payloads）。

如果该值是字符串，或者长度少于 16 个八位组（Octets），其余八位组必须为 `0`。

例如，字符串 `"Broadcast Code"` 必须表示为 `[42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]`。

<a id="a7548bbb75f240a70435cb86a48846d0a"></a>

### `bis_channels`

```c
struct bt_iso_chan** bt_iso_big_create_param::bis_channels
```

广播等时流通道指针数组（BIS channel pointers）。

<a id="a1288fa2a8f6bb3e2ab26729e245277e1"></a>

### `encryption`

```c
bool bt_iso_big_create_param::encryption
```

是否加密各条流。

<a id="aab0e9f66cb10643e72d6382718ed4c0d"></a>

### `framing`

```c
uint8_t bt_iso_big_create_param::framing
```

通道成帧模式（Channel framing mode）。

无帧模式（Unframed）使用 `BT_ISO_FRAMING_UNFRAMED`，成帧模式（Framed）使用 `BT_ISO_FRAMING_FRAMED`。

<a id="a7aaef1f7a78ae1088886a78739fd6849"></a>

### `interval`

```c
uint32_t bt_iso_big_create_param::interval
```

通道间隔（Channel interval），单位为微秒。

取值范围为 `BT_ISO_SDU_INTERVAL_MIN` 到 `BT_ISO_SDU_INTERVAL_MAX`。

<a id="ad931ff1f19f92c29c40d934346498e79"></a>

### `irc`

```c
uint8_t bt_iso_big_create_param::irc
```

即时重复计数（Immediate Repetition Count）。

给定事件中已调度载荷的传输次数。

取值范围为 `BT_ISO_IRC_MIN` 到 `BT_ISO_IRC_MAX`。

<a id="a63cd16824e9d09e29d3c7e135b08d932"></a>

### `iso_interval`

```c
uint16_t bt_iso_big_create_param::iso_interval
```

等时间隔（ISO Interval）。

相邻 BIS 锚点（Anchor Points）之间的时间。

取值范围为 `BT_ISO_ISO_INTERVAL_MIN` 到 `BT_ISO_ISO_INTERVAL_MAX`。

<a id="ab847021da2e604036cecf90483e12132"></a>

### `latency`

```c
uint16_t bt_iso_big_create_param::latency
```

通道延迟（Channel Latency），单位为毫秒。

取值范围为 `BT_ISO_LATENCY_MIN` 到 `BT_ISO_LATENCY_MAX`。

设置任何高级等时参数（Advanced ISO parameters）后，此值均被忽略。

<a id="a8ae9c225798e9f5b72fe0b8c3b6f2cf0"></a>

### `num_bis`

```c
uint8_t bt_iso_big_create_param::num_bis
```

`bis_channels` 中的通道数量（Number of channels）。

单组最大通道数量（Maximum channels per group）为 `BT_ISO_MAX_GROUP_ISO_COUNT`。

<a id="ad478d7b36fb34b8e57a25ae0029e4c51"></a>

### `packing`

```c
uint8_t bt_iso_big_create_param::packing
```

通道打包模式（Channel packing mode）。

`BT_ISO_PACKING_SEQUENTIAL` 或 `BT_ISO_PACKING_INTERLEAVED`。

<a id="affce506bd271d9b0e497160c163c5798"></a>

### `pto`

```c
uint8_t bt_iso_big_create_param::pto
```

预传输偏移（Pre-transmission Offset）。

预传输使用的偏移量（Offset）。

取值范围为 `BT_ISO_PTO_MIN` 到 `BT_ISO_PTO_MAX`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 73.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_iso_chan](P077_bt_iso_chan_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [BT_ISO_FRAMING_UNFRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga696a81180ae25aa686a53b73e352c9d2)
- [BT_ISO_FRAMING_FRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8f9aba389529ad2a3667ca378e99de2b)
- [BT_ISO_SDU_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8122de88b6e5423dca653b1f0a484316)
- [BT_ISO_SDU_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga077eb6d219bba947d363e2cce8e0080c)
- [BT_ISO_IRC_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga52df7bd114b77872c084e28ca86e0b2e)
- [BT_ISO_IRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0f412f1593bcdcfa2b323b285bd508a4)
- [BT_ISO_ISO_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de)
- [BT_ISO_ISO_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gabc381a7f565061ec91d23b7783521da3)
- [BT_ISO_LATENCY_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga77ae350543eb05617c590c0ad9cb0048)
- [BT_ISO_LATENCY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gad5e89d05d8706509d8d9d8dac40e3347)
- [BT_ISO_MAX_GROUP_ISO_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gae9dc30b300e2c309d646e3227e8cc00e)
- [BT_ISO_PACKING_SEQUENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga6275e8d805e2366522a78f18ca47ac19)
- [BT_ISO_PACKING_INTERLEAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga35b037fcce858857642b4c54bae8dd79)
- [BT_ISO_PTO_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3f19aaa432290d67fdf4911d1d044dd8)
- [BT_ISO_PTO_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga27e812e35a1f12329310851eb9c056f2)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P072_bt_iso_big_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P074_bt_iso_big_sync_param_结构体.md)
