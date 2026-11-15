---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-37
title: bt_bap_unicast_group_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_bt\_bap\_unicast\_group\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

保存单播组（Unicast Group）信息的结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

保存单播组（Unicast Group）信息的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_a74730a75337b985b7260297b1ecf8a21"></a>

```c
uint32_t sink_pd
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sink_pd](#a74730a75337b985b7260297b1ecf8a21)。

接收端 ASE 的呈现延迟（Presentation Delay），音频方向为中心设备到外围设备（Central to Peripheral）。

<a id="r_a05ecedc6350f6961d9794f854bf5be37"></a>

```c
uint32_t source_pd
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[source_pd](#a05ecedc6350f6961d9794f854bf5be37)。

发送源 ASE 的呈现延迟，音频方向为外围设备到中心设备（Peripheral to Central）。

<a id="r_aa310b32478893830907878f59a65f876"></a>

```c
uint32_t c_to_p_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[c_to_p_interval](#aa310b32478893830907878f59a65f876)。

中心设备到外围设备的 SDU 间隔，单位为微秒。

<a id="r_a70883292203e5f37f71238f0b659aa31"></a>

```c
uint32_t p_to_c_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[p_to_c_interval](#a70883292203e5f37f71238f0b659aa31)。

外围设备到中心设备的 SDU 间隔，单位为微秒。

<a id="r_a9c12fa3c837c300528dce41c8789e301"></a>

```c
uint16_t c_to_p_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[c_to_p_latency](#a9c12fa3c837c300528dce41c8789e301)。

中心设备到外围设备的最大传输延迟，单位为毫秒。

<a id="r_a25208a4e06afd726c6f6f0714233526a"></a>

```c
uint16_t p_to_c_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[p_to_c_latency](#a25208a4e06afd726c6f6f0714233526a)。

外围设备到中心设备的最大传输延迟，单位为毫秒。

<a id="r_a0cfbd31f735e4d18ac95f2e7d2a31f9a"></a>

```c
enum bt_bap_qos_cfg_framing framing
```

相关声明：[bt_bap_qos_cfg_framing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga37a5f9d7198739eef8bde6764da30de9)、[framing](#a0cfbd31f735e4d18ac95f2e7d2a31f9a)。

组内流的成帧方式（Framing）。

<a id="r_ac701205d557f5cdb27663e2521082681"></a>

```c
uint8_t packing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packing](#ac701205d557f5cdb27663e2521082681)。

组的打包方式（Packing）。

<a id="r_a180fe8c6c0081da2f2cb38b3df0fadaf"></a>

```c
bool has_been_connected
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_been_connected](#a180fe8c6c0081da2f2cb38b3df0fadaf)。

组中是否已有任意一条流完成连接。

<a id="r_a1e49ada1c3a60ac73e29cc32f95a9533"></a>

```c
uint8_t c_to_p_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_to_p_ft](#a1e49ada1c3a60ac73e29cc32f95a9533)。

中心设备到外围设备的清除超时（Flush Timeout），以等时间隔（ISO Interval）的倍数表示。

<a id="r_a15731dd811989ea465f2b2b490502db4"></a>

```c
uint8_t p_to_c_ft
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_to_c_ft](#a15731dd811989ea465f2b2b490502db4)。

外围设备到中心设备的清除超时，以等时间隔的倍数表示。

<a id="r_aee9990d7b3a7e7c8230fb5f4eb7198b8"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#aee9990d7b3a7e7c8230fb5f4eb7198b8)。

等时间隔，单位为 1.25 ms。

## 37.2\_详细说明（Detailed Documentation）

<a id="a1e49ada1c3a60ac73e29cc32f95a9533"></a>

### `c_to_p_ft`

```c
uint8_t bt_bap_unicast_group_info::c_to_p_ft
```

中心设备到外围设备的清除超时（Flush Timeout），以等时间隔（ISO Interval）的倍数表示。

如果组中没有添加接收流，则为 0。

<a id="aa310b32478893830907878f59a65f876"></a>

### `c_to_p_interval`

```c
uint32_t bt_bap_unicast_group_info::c_to_p_interval
```

中心设备到外围设备的 SDU 间隔，单位为微秒。

如果组中没有添加接收流，则为 0。

<a id="a9c12fa3c837c300528dce41c8789e301"></a>

### `c_to_p_latency`

```c
uint16_t bt_bap_unicast_group_info::c_to_p_latency
```

中心设备到外围设备的最大传输延迟，单位为毫秒。

如果组中没有添加接收流，则为 0。

<a id="a0cfbd31f735e4d18ac95f2e7d2a31f9a"></a>

### `framing`

```c
enum bt_bap_qos_cfg_framing bt_bap_unicast_group_info::framing
```

组内流的成帧方式（Framing）。

<a id="a180fe8c6c0081da2f2cb38b3df0fadaf"></a>

### `has_been_connected`

```c
bool bt_bap_unicast_group_info::has_been_connected
```

组中是否已有任意一条流完成连接。

此值为 `true` 时，不能再通过 `bt_bap_unicast_group_reconfig()`、`bt_bap_unicast_group_add_streams()` 等操作修改该组。

<a id="aee9990d7b3a7e7c8230fb5f4eb7198b8"></a>

### `iso_interval`

```c
uint16_t bt_bap_unicast_group_info::iso_interval
```

等时间隔，单位为 1.25 ms。

<a id="a15731dd811989ea465f2b2b490502db4"></a>

### `p_to_c_ft`

```c
uint8_t bt_bap_unicast_group_info::p_to_c_ft
```

外围设备到中心设备的清除超时，以等时间隔的倍数表示。

如果组中没有添加发送流，则为 0。

<a id="a70883292203e5f37f71238f0b659aa31"></a>

### `p_to_c_interval`

```c
uint32_t bt_bap_unicast_group_info::p_to_c_interval
```

外围设备到中心设备的 SDU 间隔，单位为微秒。

如果组中没有添加发送流，则为 0。

<a id="a25208a4e06afd726c6f6f0714233526a"></a>

### `p_to_c_latency`

```c
uint16_t bt_bap_unicast_group_info::p_to_c_latency
```

外围设备到中心设备的最大传输延迟，单位为毫秒。

如果组中没有添加发送流，则为 0。

<a id="ac701205d557f5cdb27663e2521082681"></a>

### `packing`

```c
uint8_t bt_bap_unicast_group_info::packing
```

组的打包方式（Packing）。

`BT_ISO_PACKING_SEQUENTIAL` 或 `BT_ISO_PACKING_INTERLEAVED`。

<a id="a74730a75337b985b7260297b1ecf8a21"></a>

### `sink_pd`

```c
uint32_t bt_bap_unicast_group_info::sink_pd
```

接收端 ASE 的呈现延迟（Presentation Delay），音频方向为中心设备到外围设备（Central to Peripheral）。

如果组中没有添加接收流，则为 `BT_BAP_PD_UNSET`。此值仅反映创建或重新配置组时的本地值，不反映任何远端 ASE 上实际配置的值。

<a id="a05ecedc6350f6961d9794f854bf5be37"></a>

### `source_pd`

```c
uint32_t bt_bap_unicast_group_info::source_pd
```

发送源 ASE 的呈现延迟，音频方向为外围设备到中心设备（Peripheral to Central）。

如果组中没有添加发送流，则为 `BT_BAP_PD_UNSET`。此值仅反映创建或重新配置组时的本地值，不反映任何远端 ASE 上实际配置的值。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_bap_qos_cfg_framing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga37a5f9d7198739eef8bde6764da30de9)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_bap_unicast_group_reconfig()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gacd684504c8127ff4f8d038cc06718e5e)
- [bt_bap_unicast_group_add_streams()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#ga9cc792cd1eaaa79d56f3df0e2341cbf6)
- [BT_ISO_PACKING_SEQUENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga6275e8d805e2366522a78f18ca47ac19)
- [BT_ISO_PACKING_INTERLEAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga35b037fcce858857642b4c54bae8dd79)
- [BT_BAP_PD_UNSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga3fb8ca6b5722cad7027553db40c4a94b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_bt_bap_unicast_group_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_bt_bap_unicast_group_param_结构体.md)
