---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-3
title: 蓝牙 LC3 编解码器（Bluetooth LC3 codec）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_蓝牙 LC3 编解码器（Bluetooth LC3 codec）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LC3

<a id="details"></a>

低复杂度通信编解码器（LC3）。**引入版本（Since）：**3.0。**版本（Version）：**0.8.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_ga8d679b241585ff5ebff0d97bb22dfda9"></a>

```c
#define BT_AUDIO_CODEC_CAP_LC3_DATA(_freq, _duration, _chan_count, _len_min, _len_max, _max_frames_per_sdu)
```

相关声明：[BT_AUDIO_CODEC_CAP_LC3_DATA](#ga8d679b241585ff5ebff0d97bb22dfda9)。

用于声明低复杂度通信编解码器（LC3）能力（capability）的辅助宏。

<a id="r_ga9b5d5e300a7b41060329dbdd2cd073f6"></a>

```c
#define BT_AUDIO_CODEC_CAP_LC3_META(_prefer_context)
```

相关声明：[BT_AUDIO_CODEC_CAP_LC3_META](#ga9b5d5e300a7b41060329dbdd2cd073f6)。

用于声明 LC3 编解码器元数据（metadata）的辅助宏。

<a id="r_gac474746e7314ebf7ed77b8937191cdc1"></a>

```c
#define BT_AUDIO_CODEC_CAP_LC3(_freq, _duration, _chan_count, _len_min, _len_max, _max_frames_per_sdu, _prefer_context)
```

相关声明：[BT_AUDIO_CODEC_CAP_LC3](#gac474746e7314ebf7ed77b8937191cdc1)。

用于声明 LC3 编解码器（codec）的辅助宏。

<a id="r_ga497ff0aa1d7dcfeea6ec549e5fb155d6"></a>

```c
#define BT_AUDIO_CODEC_CFG_LC3_DATA(_freq, _duration, _loc, _len, _frames_per_sdu)
```

相关声明：[BT_AUDIO_CODEC_CFG_LC3_DATA](#ga497ff0aa1d7dcfeea6ec549e5fb155d6)。

用于声明 LC3 编解码器数据配置（data configuration）的辅助宏。

<a id="r_ga2c00f8bd526305d878624c6f1b8030f8"></a>

```c
#define BT_AUDIO_CODEC_CFG_LC3_META(_stream_context)
```

相关声明：[BT_AUDIO_CODEC_CFG_LC3_META](#ga2c00f8bd526305d878624c6f1b8030f8)。

用于声明 LC3 编解码器元数据配置（metadata configuration）的辅助宏。

<a id="r_ga2c5f1f9e6d80a2eef93f7b08a19ea245"></a>

```c
#define BT_AUDIO_CODEC_LC3_CONFIG(_freq, _duration, _loc, _len, _frames_per_sdu, _stream_context)
```

相关声明：[BT_AUDIO_CODEC_LC3_CONFIG](#ga2c5f1f9e6d80a2eef93f7b08a19ea245)。

用于声明 LC3 编解码器配置的辅助宏。

## 3.2\_详细说明（Detailed Documentation）

<a id="gac474746e7314ebf7ed77b8937191cdc1"></a>

### `BT_AUDIO_CODEC_CAP_LC3`

```c
#define BT_AUDIO_CODEC_CAP_LC3 ( _freq, _duration, _chan_count, _len_min, _len_max, _max_frames_per_sdu, _prefer_context )
```

```c
#include <zephyr/bluetooth/audio/lc3.h>
```

展开值（Value）：

```c
BT_AUDIO_CODEC_CAP(BT_HCI_CODING_FORMAT_LC3, 0x0000, 0x0000,                               \
                   BT_AUDIO_CODEC_CAP_LC3_DATA(_freq, _duration, _chan_count, _len_min,    \
                                               _len_max, _max_frames_per_sdu),             \
                   BT_AUDIO_CODEC_CAP_LC3_META(_prefer_context))
```

用于声明 LC3 编解码器（codec）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_freq` | 支持的采样频率位域（Sampling Frequencies Bitfield），参见 `BT_AUDIO_CODEC_CAP_FREQ_*`。 |
| `_duration` | 支持的帧时长位域（Frame Durations Bitfield），参见 `BT_AUDIO_CODEC_CAP_DURATION_*`。 |
| `_chan_count` | 支持的通道（Channels），参见 `BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT`。 |
| `_len_min` | 每个编解码器帧支持的最少八位字节（Octets）数。 |
| `_len_max` | 每个编解码器帧支持的最多八位字节数。 |
| `_max_frames_per_sdu` | 每个服务数据单元（SDU）支持的最大编解码器帧（Codec Frames）数量。 |
| `_prefer_context` | 首选上下文（Preferred Contexts），即 `bt_audio_context`。 |

<a id="ga8d679b241585ff5ebff0d97bb22dfda9"></a>

### `BT_AUDIO_CODEC_CAP_LC3_DATA`

```c
#define BT_AUDIO_CODEC_CAP_LC3_DATA ( _freq, _duration, _chan_count, _len_min, _len_max, _max_frames_per_sdu )
```

```c
#include <zephyr/bluetooth/audio/lc3.h>
```

展开值（Value）：

```c
{                                                                                          \
        BT_AUDIO_CODEC_DATA(BT_AUDIO_CODEC_CAP_TYPE_FREQ, BT_BYTES_LIST_LE16(_freq)),      \
        BT_AUDIO_CODEC_DATA(BT_AUDIO_CODEC_CAP_TYPE_DURATION, (_duration)),                \
        BT_AUDIO_CODEC_DATA(BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT, (_chan_count)),            \
        BT_AUDIO_CODEC_DATA(BT_AUDIO_CODEC_CAP_TYPE_FRAME_LEN,                             \
                            BT_BYTES_LIST_LE16(_len_min),                                  \
                            BT_BYTES_LIST_LE16(_len_max)),                                 \
        COND_CODE_1(_max_frames_per_sdu, (),                                               \
                    (BT_AUDIO_CODEC_DATA(BT_AUDIO_CODEC_CAP_TYPE_FRAME_COUNT,              \
                                         (_max_frames_per_sdu))))                          \
}
```

用于声明低复杂度通信编解码器（LC3）能力（capability）的辅助宏。

`_max_frames_per_sdu` 为可选项，仅当其值不等于 `1` 时才包含此项。

当 `_max_frames_per_sdu` 为 `1` 时，使用 `COND_CODE_1` 省略对应长度／类型／值（LTV）条目。当标志参数（第一个参数）为 `1` 时，`COND_CODE_1` 求值为第二个参数，

- 并去掉一层括号。如果标志参数不等于 `1`，则求值为第三个参数，为 `max_frames_per_sdu` 值插入一个长度／类型／值（LTV）条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_freq` | 支持的采样频率位域（Sampling Frequencies Bitfield），参见 `BT_AUDIO_CODEC_CAP_FREQ_*`。 |
| `_duration` | 支持的帧时长位域（Frame Durations Bitfield），参见 `BT_AUDIO_CODEC_CAP_DURATION_*`。 |
| `_chan_count` | 支持的通道（Channels），参见 `BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT`。 |
| `_len_min` | 每个编解码器帧支持的最少八位字节（Octets）数。 |
| `_len_max` | 每个编解码器帧支持的最多八位字节数。 |
| `_max_frames_per_sdu` | 每个服务数据单元（SDU）支持的最大编解码器帧（Codec Frames）数量。 |

<a id="ga9b5d5e300a7b41060329dbdd2cd073f6"></a>

### `BT_AUDIO_CODEC_CAP_LC3_META`

```c
#define BT_AUDIO_CODEC_CAP_LC3_META ( _prefer_context)
```

```c
#include <zephyr/bluetooth/audio/lc3.h>
```

展开值（Value）：

```c
{                                                                                          \
        BT_AUDIO_CODEC_DATA(BT_AUDIO_METADATA_TYPE_PREF_CONTEXT,                           \
                            BT_BYTES_LIST_LE16(_prefer_context))                           \
}
```

用于声明 LC3 编解码器元数据（metadata）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_prefer_context` | 首选上下文（Preferred Contexts），即 `bt_audio_context`。 |

<a id="ga497ff0aa1d7dcfeea6ec549e5fb155d6"></a>

### `BT_AUDIO_CODEC_CFG_LC3_DATA`

```c
#define BT_AUDIO_CODEC_CFG_LC3_DATA ( _freq, _duration, _loc, _len, _frames_per_sdu )
```

```c
#include <zephyr/bluetooth/audio/lc3.h>
```

展开值（Value）：

```c
{                                                                                          \
        BT_AUDIO_CODEC_DATA(BT_AUDIO_CODEC_CFG_FREQ, (_freq)),                             \
        BT_AUDIO_CODEC_DATA(BT_AUDIO_CODEC_CFG_DURATION, (_duration)),                     \
        BT_AUDIO_CODEC_DATA(BT_AUDIO_CODEC_CFG_CHAN_ALLOC, BT_BYTES_LIST_LE32(_loc)),      \
        BT_AUDIO_CODEC_DATA(BT_AUDIO_CODEC_CFG_FRAME_LEN, BT_BYTES_LIST_LE16(_len)),       \
        COND_CODE_1(_frames_per_sdu, (),                                                   \
                    (BT_AUDIO_CODEC_DATA(BT_AUDIO_CODEC_CFG_FRAME_BLKS_PER_SDU,            \
                                         (_frames_per_sdu))))                              \
}
```

用于声明 LC3 编解码器数据配置（data configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_freq` | 采样频率（Sampling Frequency），即 `BT_AUDIO_CODEC_CFG_FREQ_*`。 |
| `_duration` | 帧时长（Frame Duration），即 `BT_AUDIO_CODEC_CFG_DURATION_*`。 |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_len` | 每帧的八位组数（Octets per Frame），为 16 位整数。 |
| `_frames_per_sdu` | 每个 SDU 的帧数（Frames per SDU），为 8 位整数。此值为可选项，仅当其不等于 `1` 时才包含此项。 |

<a id="ga2c00f8bd526305d878624c6f1b8030f8"></a>

### `BT_AUDIO_CODEC_CFG_LC3_META`

```c
#define BT_AUDIO_CODEC_CFG_LC3_META ( _stream_context)
```

```c
#include <zephyr/bluetooth/audio/lc3.h>
```

展开值（Value）：

```c
{                                                                                          \
        BT_AUDIO_CODEC_DATA(BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT,                         \
                            BT_BYTES_LIST_LE16(_stream_context))                           \
}
```

用于声明 LC3 编解码器元数据配置（metadata configuration）的辅助宏。

<a id="ga2c5f1f9e6d80a2eef93f7b08a19ea245"></a>

### `BT_AUDIO_CODEC_LC3_CONFIG`

```c
#define BT_AUDIO_CODEC_LC3_CONFIG ( _freq, _duration, _loc, _len, _frames_per_sdu, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/lc3.h>
```

展开值（Value）：

```c
BT_AUDIO_CODEC_CFG(                                                                        \
        BT_HCI_CODING_FORMAT_LC3, 0x0000, 0x0000,                                          \
        BT_AUDIO_CODEC_CFG_LC3_DATA(_freq, _duration, _loc, _len, _frames_per_sdu),        \
        BT_AUDIO_CODEC_CFG_LC3_META(_stream_context))
```

用于声明 LC3 编解码器配置的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_freq` | 采样频率（Sampling Frequency），即 `BT_AUDIO_CODEC_CFG_FREQ_*`。 |
| `_duration` | 帧时长（Frame Duration），即 `BT_AUDIO_CODEC_CFG_DURATION_*`。 |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_len` | 每帧的八位组数（Octets per Frame），为 16 位整数。 |
| `_frames_per_sdu` | 每个 SDU 的帧数（Frames per SDU），为 8 位整数。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |


## 3.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/lc3.h](../api_file_management_reference/P026_zephyr__bluetooth__audio__lc3.h_文件参考.md)
- [BT_AUDIO_CODEC_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga6b99f589f6cdcd9e48a83f729a7a4698)
- [BT_HCI_CODING_FORMAT_LC3](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a1fa62d6f28ef56ebe9c18d5ab86fbf8e)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga8f835266fabd6461216fe13e1b3b3a0f)
- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [BT_AUDIO_CODEC_CAP_TYPE_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b)
- [BT_BYTES_LIST_LE16](../byteorder_reference/P003_蓝牙字节序辅助接口.md#ga83b5828023306b4bbf354ca3d6d6c6f2)
- [BT_AUDIO_CODEC_CAP_TYPE_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510)
- [BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191)
- [BT_AUDIO_CODEC_CAP_TYPE_FRAME_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46)
- [BT_AUDIO_CODEC_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gaddc49e39465798ae4c0cbe345e0b50d7)
- [BT_AUDIO_CODEC_CAP_TYPE_FRAME_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [BT_AUDIO_METADATA_TYPE_PREF_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)
- [BT_AUDIO_CODEC_CFG_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3)
- [BT_AUDIO_CODEC_CFG_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223)
- [BT_AUDIO_CODEC_CFG_CHAN_ALLOC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2)
- [BT_BYTES_LIST_LE32](../byteorder_reference/P003_蓝牙字节序辅助接口.md#ga0bf0275f0eea70eb5ae6002edeb1b812)
- [BT_AUDIO_CODEC_CFG_FRAME_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2)
- [BT_AUDIO_CODEC_CFG_FRAME_BLKS_PER_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)
- [BT_AUDIO_CODEC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gaefed7a013e282c63c9b5cbbdcdc67448)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__audio_html_ga6b99f589f6cdcd9e48a83f729a7a4698"></a>
<a id="agroup__bt__lc3_html_ga8d679b241585ff5ebff0d97bb22dfda9"></a>
<a id="agroup__bt__lc3_html_ga9b5d5e300a7b41060329dbdd2cd073f6"></a>
<a id="ahci__types_8h_html_a1fa62d6f28ef56ebe9c18d5ab86fbf8e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b"></a>
<a id="agroup__bt__audio_html_gaddc49e39465798ae4c0cbe345e0b50d7"></a>
<a id="agroup__bt__byteorder_html_ga83b5828023306b4bbf354ca3d6d6c6f2"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2"></a>
<a id="agroup__bt__byteorder_html_ga0bf0275f0eea70eb5ae6002edeb1b812"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa"></a>
<a id="agroup__bt__audio_html_gaefed7a013e282c63c9b5cbbdcdc67448"></a>
<a id="agroup__bt__lc3_html_ga2c00f8bd526305d878624c6f1b8030f8"></a>
<a id="agroup__bt__lc3_html_ga497ff0aa1d7dcfeea6ec549e5fb155d6"></a>

---

[上一章](P002_通用对象交换规范（Generic Object Exchange Profile，GOEP）.md) · [返回大纲](大纲.md) · [下一章](P004_Core Devices SF32LB API主题.md)
