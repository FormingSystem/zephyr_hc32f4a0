---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-28
title: bt_bap_qos_cfg_pref_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__qos__cfg__pref.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_bt\_bap\_qos\_cfg\_pref\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__qos__cfg__pref.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

音频流服务质量偏好（Audio Stream Quality of Service Preference）结构体。

```c
#include <zephyr/bluetooth/audio/ascs.h>
```

<a id="details"></a>

音频流服务质量偏好（Audio Stream Quality of Service Preference）结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_a2a2de382f04a50d26d174dcc7c7a12c1"></a>

```c
bool unframed_supported
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[unframed_supported](#a2a2de382f04a50d26d174dcc7c7a12c1)。

是否支持未成帧的 PDU（Unframed PDUs）。

<a id="r_a697a67e623d758b76be342a125a369a6"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a697a67e623d758b76be342a125a369a6)。

首选物理层位域（Preferred PHY Bitfield）。

<a id="r_a286bfb02d35ca148f263f1fa1ca9e061"></a>

```c
uint8_t rtn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtn](#a286bfb02d35ca148f263f1fa1ca9e061)。

首选重传次数（Preferred Retransmission Number）。

<a id="r_ac5871b4f58be038eeda483e8d07b9b53"></a>

```c
uint16_t latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[latency](#ac5871b4f58be038eeda483e8d07b9b53)。

首选传输延迟，单位为毫秒。

<a id="r_a3f643768de9d8b0a7a62e403703e0033"></a>

```c
uint32_t pd_min
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pd_min](#a3f643768de9d8b0a7a62e403703e0033)。

最小呈现延迟，单位为微秒。

<a id="r_a666be60856b5b4688d21d7a36b956c29"></a>

```c
uint32_t pd_max
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pd_max](#a666be60856b5b4688d21d7a36b956c29)。

最大呈现延迟，单位为微秒。

<a id="r_a1df8cd4ed27e9099b8b2a069855010aa"></a>

```c
uint32_t pref_pd_min
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pref_pd_min](#a1df8cd4ed27e9099b8b2a069855010aa)。

首选最小呈现延迟，单位为微秒。

<a id="r_ab6475a80b33a9cea69edeaa3093c9070"></a>

```c
uint32_t pref_pd_max
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pref_pd_max](#ab6475a80b33a9cea69edeaa3093c9070)。

首选最大呈现延迟，单位为微秒。

## 28.2\_详细说明（Detailed Documentation）

<a id="ac5871b4f58be038eeda483e8d07b9b53"></a>

### `latency`

```c
uint16_t bt_bap_qos_cfg_pref::latency
```

首选传输延迟，单位为毫秒。

取值范围为 `BT_ISO_LATENCY_MIN` 到 `BT_ISO_LATENCY_MAX`。

<a id="a666be60856b5b4688d21d7a36b956c29"></a>

### `pd_max`

```c
uint32_t bt_bap_qos_cfg_pref::pd_max
```

最大呈现延迟，单位为微秒。

与其他字段不同，这不是偏好值，而是最大值约束。

取值范围为 `bt_bap_qos_cfg_pref::pd_min` 到 `BT_AUDIO_PD_MAX`。

<a id="a3f643768de9d8b0a7a62e403703e0033"></a>

### `pd_min`

```c
uint32_t bt_bap_qos_cfg_pref::pd_min
```

最小呈现延迟，单位为微秒。

与其他字段不同，这不是偏好值，而是最小值约束。

取值范围为 0 到 `BT_AUDIO_PD_MAX`。

<a id="a697a67e623d758b76be342a125a369a6"></a>

### `phy`

```c
uint8_t bt_bap_qos_cfg_pref::phy
```

首选物理层位域（Preferred PHY Bitfield）。

由 `BT_GAP_LE_PHY_1M`、`BT_GAP_LE_PHY_2M` 和 `BT_GAP_LE_PHY_CODED` 中一个或多个值组成的位域。

<a id="ab6475a80b33a9cea69edeaa3093c9070"></a>

### `pref_pd_max`

```c
uint32_t bt_bap_qos_cfg_pref::pref_pd_max
```

首选最大呈现延迟，单位为微秒。

取值范围为 `bt_bap_qos_cfg_pref::pd_min` 到 `bt_bap_qos_cfg_pref::pd_max`，并且必须大于或等于 `bt_bap_qos_cfg_pref::pref_pd_min`；也可以使用 `BT_AUDIO_PD_PREF_NONE` 表示无偏好。

<a id="a1df8cd4ed27e9099b8b2a069855010aa"></a>

### `pref_pd_min`

```c
uint32_t bt_bap_qos_cfg_pref::pref_pd_min
```

首选最小呈现延迟，单位为微秒。

取值范围为 `bt_bap_qos_cfg_pref::pd_min` 到 `bt_bap_qos_cfg_pref::pd_max`；也可以使用 `BT_AUDIO_PD_PREF_NONE` 表示无偏好。

<a id="a286bfb02d35ca148f263f1fa1ca9e061"></a>

### `rtn`

```c
uint8_t bt_bap_qos_cfg_pref::rtn
```

首选重传次数（Preferred Retransmission Number）。

`BT_AUDIO_RTN_PREF_NONE` 表示无偏好。

<a id="a2a2de382f04a50d26d174dcc7c7a12c1"></a>

### `unframed_supported`

```c
bool bt_bap_qos_cfg_pref::unframed_supported
```

是否支持未成帧的 PDU（Unframed PDUs）。

与其他字段不同，此项不是偏好值，而是表示编解码器是否支持未成帧的等时适配层（ISOAL）PDU。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/ascs.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/ascs.h](https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [BT_ISO_LATENCY_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga77ae350543eb05617c590c0ad9cb0048)
- [BT_ISO_LATENCY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gad5e89d05d8706509d8d9d8dac40e3347)
- [BT_AUDIO_PD_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gaaa0414a4baef5a867fd1c6b1865d2dbc)
- [BT_GAP_LE_PHY_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a53eff400720a20fe1a91da4834bad752)
- [BT_GAP_LE_PHY_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a662049cc8293959194bcb481e1dd50a8)
- [BT_GAP_LE_PHY_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gga691d9793fd21c41b2c192d65cc2bf6c4a97d042e48448fdf6a9e35e5d38cb14c3)
- [BT_AUDIO_PD_PREF_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga663ab7bf74d56f36ee6cc80b369cbc16)
- [BT_AUDIO_RTN_PREF_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga4a5fd440b96f4e4acbb791badef8c255)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_bt_bap_qos_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_bt_bap_scan_delegator_add_src_param_结构体.md)
