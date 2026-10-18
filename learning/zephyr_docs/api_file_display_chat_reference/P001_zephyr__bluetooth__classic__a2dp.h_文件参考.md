---
id: learning.zephyr-docs.api-file-display-chat-reference.page-1
title: zephyr__bluetooth__classic__a2dp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/a2dp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_classic\_\_a2dp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/a2dp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

高级音频分发配置文件（Advanced Audio Distribution Profile）的头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/l2cap.h>
#include <zephyr/bluetooth/classic/avdtp.h>
```

查看此文件的源码。

高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）头文件。高级音频分发配置文件（A2DP）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Fa2dp_5Fcodec_5Fie"></a>

```c
struct bt_a2dp_codec_ie
```

相关声明：[bt_a2dp_codec_ie](../bluetooth_classic_model_reference/P004_bt_a2dp_codec_ie_结构体.md)。

端点的编解码器信息元素（Codec Information Elements）。

<a id="r_bt_5Fa2dp_5Fcodec_5Fcfg"></a>

```c
struct bt_a2dp_codec_cfg
```

相关声明：[bt_a2dp_codec_cfg](../bluetooth_classic_model_reference/P003_bt_a2dp_codec_cfg_结构体.md)。

端点配置（Endpoint Configuration）。

<a id="r_bt_5Fa2dp_5Fep"></a>

```c
struct bt_a2dp_ep
```

相关声明：[bt_a2dp_ep](../bluetooth_classic_model_reference/P007_bt_a2dp_ep_结构体.md)。

流端点（Stream End Point）。

<a id="r_bt_5Fa2dp_5Fep_5Finfo"></a>

```c
struct bt_a2dp_ep_info
```

相关声明：[bt_a2dp_ep_info](../bluetooth_classic_model_reference/P008_bt_a2dp_ep_info_结构体.md)。

<a id="r_bt_5Fa2dp_5Fdiscover_5Fparam"></a>

```c
struct bt_a2dp_discover_param
```

相关声明：[bt_a2dp_discover_param](../bluetooth_classic_model_reference/P006_bt_a2dp_discover_param_结构体.md)。

<a id="r_bt_5Fa2dp_5Fcb"></a>

```c
struct bt_a2dp_cb
```

相关声明：[bt_a2dp_cb](../bluetooth_classic_model_reference/P002_bt_a2dp_cb_结构体.md)。

正在连接时的回调（Connecting Callback）。

<a id="r_bt_5Fa2dp_5Fstream"></a>

```c
struct bt_a2dp_stream
```

相关声明：[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

A2DP 流（Stream）。

<a id="r_bt_5Fa2dp_5Fstream_5Fops"></a>

```c
struct bt_a2dp_stream_ops
```

相关声明：[bt_a2dp_stream_ops](../bluetooth_classic_model_reference/P010_bt_a2dp_stream_ops_结构体.md)。

与流端点相关的操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_gaf83aa927ac312cfc8577056afffeae56"></a>

```c
#define BT_A2DP_SBC_IE_LENGTH (4U)
```

相关声明：[BT_A2DP_SBC_IE_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gaf83aa927ac312cfc8577056afffeae56)。

SBC 信息元素（IE）长度。

<a id="r_ga313fec2276421be6f29c0309e67755eb"></a>

```c
#define BT_A2DP_MPEG_1_2_IE_LENGTH (4U)
```

相关声明：[BT_A2DP_MPEG_1_2_IE_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga313fec2276421be6f29c0309e67755eb)。

MPEG1、2 信息元素（IE）长度。

<a id="r_ga73ae4b6e2913b3772b32c520bf84de8c"></a>

```c
#define BT_A2DP_MPEG_2_4_IE_LENGTH (6U)
```

相关声明：[BT_A2DP_MPEG_2_4_IE_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga73ae4b6e2913b3772b32c520bf84de8c)。

MPEG2、4 信息元素（IE）长度。

<a id="r_ga3a2b2021adcd90c8c5adbbeb1441826d"></a>

```c
#define BT_A2DP_EP_INIT(_role, _codec, _capability, _delay_report)
```

相关声明：[BT_A2DP_EP_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga3a2b2021adcd90c8c5adbbeb1441826d)。

定义音频端点（Audio Endpoint）。

<a id="r_ga3c0b5c4dbbea7bc3999a81e2bc579a46"></a>

```c
#define BT_A2DP_SINK_EP_INIT(_codec, _capability, _delay_report)
```

相关声明：[BT_A2DP_SINK_EP_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga3c0b5c4dbbea7bc3999a81e2bc579a46)。

定义音频接收端点（Audio Sink Endpoint）。

<a id="r_gab6dc5275f5c5057e2337acc4e31dc2fa"></a>

```c
#define BT_A2DP_SOURCE_EP_INIT(_codec, _capability, _delay_report)
```

相关声明：[BT_A2DP_SOURCE_EP_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gab6dc5275f5c5057e2337acc4e31dc2fa)。

定义音频源端点（Audio Source Endpoint）。

<a id="r_ga0c6adc3461d7e4754bd595da457870c0"></a>

```c
#define BT_A2DP_SBC_SINK_EP(_name, _freq, _ch_mode, _blk_len, _subband, _alloc_mthd, _min_bitpool, _max_bitpool, _delay_report)
```

相关声明：[BT_A2DP_SBC_SINK_EP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga0c6adc3461d7e4754bd595da457870c0)。

定义可用作 bt_a2dp_register_ep 参数的 SBC 接收端点（Sink Endpoint）。

<a id="r_ga47dc400bc57140a40975ec1570d79582"></a>

```c
#define BT_A2DP_SBC_SOURCE_EP(_name, _freq, _ch_mode, _blk_len, _subband, _alloc_mthd, _min_bitpool, _max_bitpool, _delay_report)
```

相关声明：[BT_A2DP_SBC_SOURCE_EP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga47dc400bc57140a40975ec1570d79582)。

定义可用作 bt_a2dp_register_ep 参数的 SBC 源端点（Source Endpoint）。

<a id="r_ga76fb351efe2730311baae1ad6cddbcb1"></a>

```c
#define BT_A2DP_SBC_SINK_EP_DEFAULT(_name)
```

相关声明：[BT_A2DP_SBC_SINK_EP_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga76fb351efe2730311baae1ad6cddbcb1)。

定义可用作 bt_a2dp_register_ep 参数的默认 SBC 接收端点（Default Sink Endpoint）。

<a id="r_ga6830ae27e85471935ae604b18cf779e2"></a>

```c
#define BT_A2DP_SBC_SOURCE_EP_DEFAULT(_name)
```

相关声明：[BT_A2DP_SBC_SOURCE_EP_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga6830ae27e85471935ae604b18cf779e2)。

定义可用作 bt_a2dp_register_ep 参数的默认 SBC 源端点（Default Source Endpoint）。

<a id="r_gac879cbea5f0bbecfc0ec948d6e46c073"></a>

```c
#define BT_A2DP_SBC_EP_CFG(_name, _freq_cfg, _ch_mode_cfg, _blk_len_cfg, _subband_cfg, _alloc_mthd_cfg, _min_bitpool_cfg, _max_bitpool_cfg)
```

相关声明：[BT_A2DP_SBC_EP_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gac879cbea5f0bbecfc0ec948d6e46c073)。

定义 SBC 默认配置（Default Configuration）。

<a id="r_gabbfd3bc3fa080517ef4395b30fd697f7"></a>

```c
#define BT_A2DP_SBC_EP_CFG_DEFAULT(_name, _freq_cfg)
```

相关声明：[BT_A2DP_SBC_EP_CFG_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gabbfd3bc3fa080517ef4395b30fd697f7)。

定义 SBC 默认配置（Default Configuration）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_gae054d7f9fa92e45c7d40ec0e1d8730ed"></a>

```c
typedef uint8_t(* bt_a2dp_discover_ep_cb) (struct bt_a2dp *a2dp, struct bt_a2dp_ep_info *info, struct bt_a2dp_ep **ep)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_a2dp_discover_ep_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gae054d7f9fa92e45c7d40ec0e1d8730ed)、[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)、[bt_a2dp_ep_info](../bluetooth_classic_model_reference/P008_bt_a2dp_ep_info_结构体.md)、[bt_a2dp_ep](../bluetooth_classic_model_reference/P007_bt_a2dp_ep_结构体.md)。

发现流端点（Stream Endpoint）时调用。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_ga4162a6db1ead67f52f961d660beabb8c"></a>

```c
enum bt_a2dp_err_code { BT_A2DP_INVALID_CODEC_TYPE = 0xC1 , BT_A2DP_NOT_SUPPORTED_CODEC_TYPE = 0xC2 , BT_A2DP_INVALID_SAMPLING_FREQUENCY = 0xC3 , BT_A2DP_NOT_SUPPORTED_SAMPLING_FREQUENCY = 0xC4 , BT_A2DP_INVALID_CHANNEL_MODE = 0xC5 , BT_A2DP_NOT_SUPPORTED_CHANNEL_MODE = 0xC6 , BT_A2DP_INVALID_SUBBANDS = 0xC7 , BT_A2DP_NOT_SUPPORTED_SUBBANDS = 0xC8 , BT_A2DP_INVALID_ALLOCATION_METHOD = 0xC9 , BT_A2DP_NOT_SUPPORTED_ALLOCATION_METHOD = 0xCA , BT_A2DP_INVALID_MINIMUM_BITPOOL_VALUE = 0xCB , BT_A2DP_NOT_SUPPORTED_MINIMUM_BITPOOL_VALUE = 0xCC , BT_A2DP_INVALID_MAXIMUM_BITPOOL_VALUE = 0xCD , BT_A2DP_NOT_SUPPORTED_MAXIMUM_BITPOOL_VALUE = 0xCE , BT_A2DP_INVALID_LAYER = 0xCF , BT_A2DP_NOT_SUPPORTED_LAYER = 0xD0 , BT_A2DP_NOT_SUPPORTED_CRC = 0xD1 , BT_A2DP_NOT_SUPPORTED_MPF = 0xD2 , BT_A2DP_NOT_SUPPORTED_VBR = 0xD3 , BT_A2DP_INVALID_BIT_RATE = 0xD4 , BT_A2DP_NOT_SUPPORTED_BIT_RATE = 0xD5 , BT_A2DP_INVALID_OBJECT_TYPE = 0xD6 , BT_A2DP_NOT_SUPPORTED_OBJECT_TYPE = 0xD7 , BT_A2DP_INVALID_CHANNELS = 0xD8 , BT_A2DP_NOT_SUPPORTED_CHANNELS = 0xD9 , BT_A2DP_INVALID_VERSION = 0xDA , BT_A2DP_NOT_SUPPORTED_VERSION = 0xDB , BT_A2DP_NOT_SUPPORTED_MAXIMUM_SUL = 0xDC , BT_A2DP_INVALID_BLOCK_LENGTH = 0xDD , BT_A2DP_INVALID_CP_TYPE = 0xE0 , BT_A2DP_INVALID_CP_FORMAT = 0xE1 , BT_A2DP_INVALID_CODEC_PARAMETER = 0xE2 , BT_A2DP_NOT_SUPPORTED_CODEC_PARAMETER = 0xE3 , BT_A2DP_INVALID_DRC = 0xE4 , BT_A2DP_NOT_SUPPORTED_DRC = 0xE5 }
```

相关声明：[bt_a2dp_err_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga4162a6db1ead67f52f961d660beabb8c)、[BT_A2DP_INVALID_CODEC_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca1718e53b8632688eb1aa9253248e7591)、[BT_A2DP_NOT_SUPPORTED_CODEC_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cabda2c831224e1c994b5c67ea9fe7be7f)、[BT_A2DP_INVALID_SAMPLING_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca68471cd1037db6687bc1f60cf500681c)、[BT_A2DP_NOT_SUPPORTED_SAMPLING_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca499c532b0069432802cbe72bc33e5a76)、[BT_A2DP_INVALID_CHANNEL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca6222f61712e16dbd0b56fda692844396)、[BT_A2DP_NOT_SUPPORTED_CHANNEL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca8e62e8df4d9e2a5389ad1620de7af755)、[BT_A2DP_INVALID_SUBBANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca8e06f678574f38b9538f8c45622cee3f)、[BT_A2DP_NOT_SUPPORTED_SUBBANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca2a20d81b47a5b3119988c3702ba1e84d)、[BT_A2DP_INVALID_ALLOCATION_METHOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8caf13a2a05042cb4ee373017fabd92303a)、[BT_A2DP_NOT_SUPPORTED_ALLOCATION_METHOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca81723b89ccf0d40db2a2edacd2cbaca8)、[BT_A2DP_INVALID_MINIMUM_BITPOOL_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cad81217701b215d26e65c220c83ed4a02)、[BT_A2DP_NOT_SUPPORTED_MINIMUM_BITPOOL_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cacd474a29c941a1b1ad164a63d07763d3)、[BT_A2DP_INVALID_MAXIMUM_BITPOOL_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca71dfaa290af68147e83541e37d59d5cf)、[BT_A2DP_NOT_SUPPORTED_MAXIMUM_BITPOOL_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca9fe3d3aea48e5c5122ce058e8918133f)、[BT_A2DP_INVALID_LAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8caf2bd03a778271c6310fb51d3dccccb41)、[BT_A2DP_NOT_SUPPORTED_LAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca48b381cca4ddd1ccb26037e84b0bea9e)、[BT_A2DP_NOT_SUPPORTED_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca4e204c6ea5acfe20be37da6fca38eaec)、[BT_A2DP_NOT_SUPPORTED_MPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca95a7b280dbdb757fab3b8b2077120d8f)、[BT_A2DP_NOT_SUPPORTED_VBR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca92d1fb010cc69e27ec988de69c9bbd51)、[BT_A2DP_INVALID_BIT_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cadb4d2cc815b2c01e6f7e2666305d4476)、[BT_A2DP_NOT_SUPPORTED_BIT_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8caf86c457a7e016f440089469c9f442ad1)、[BT_A2DP_INVALID_OBJECT_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca3896984afb4b5d164503bd53f0d4e429)、[BT_A2DP_NOT_SUPPORTED_OBJECT_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca7b5bafd55d8020029e429b142c572615)、[BT_A2DP_INVALID_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca182de8e823efe2f6575a900a567b3483)、[BT_A2DP_NOT_SUPPORTED_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca3619a0a5c74de24b7dd8bd79b99ca91a)、[BT_A2DP_INVALID_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca47dbe86cbbd2859243995d1d39c46d8d)、[BT_A2DP_NOT_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca1d4c42781c74ebda2b084fe609ac284c)、[BT_A2DP_NOT_SUPPORTED_MAXIMUM_SUL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cafdf002100cc0d7d1f07cf833ed331f2b)、[BT_A2DP_INVALID_BLOCK_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8caebf8a58263b517b79947e9cc8a9678c3)、[BT_A2DP_INVALID_CP_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8caab4c2af80c9588443a297e120f8ee611)、[BT_A2DP_INVALID_CP_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca0554b3ef221c98b5cb4580ae049a6e63)、[BT_A2DP_INVALID_CODEC_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca9aa4fc1c6f365b686ab4dc3875b93396)、[BT_A2DP_NOT_SUPPORTED_CODEC_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca3c801158e7ed2623c2d2930ca91b94a9)、[BT_A2DP_INVALID_DRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cafd0982a65fc5657b13f35e0761425d96)、[BT_A2DP_NOT_SUPPORTED_DRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca198bd8a559eca40d9d95f6edf8a703fd)。

A2DP 错误码（Error Code）。

<a id="r_gafdb0a28b03d1e11f0595dd3f0b3cb4d6"></a>

```c
enum bt_a2dp_codec_type { BT_A2DP_SBC = 0x00 , BT_A2DP_MPEG1 = 0x01 , BT_A2DP_MPEG2 = 0x02 , BT_A2DP_MPEGD = 0x03 , BT_A2DP_ATRAC = 0x04 , BT_A2DP_VENDOR = 0xff }
```

相关声明：[bt_a2dp_codec_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gafdb0a28b03d1e11f0595dd3f0b3cb4d6)、[BT_A2DP_SBC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00)、[BT_A2DP_MPEG1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6a1f1840d90c1d5ee28b650978bf012497)、[BT_A2DP_MPEG2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6aefe729d388e0a3d8bb7759b986123c88)、[BT_A2DP_MPEGD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6ad90f96068afbe94c6338d4906b07341b)、[BT_A2DP_ATRAC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6a8b969e35e28d18cf05802e1381995e83)、[BT_A2DP_VENDOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6ad3c292360558ea515a84d570c43c1701)。

编解码器类型（Codec Type）。

<a id="r_ga7830b874f18be8fc1c62cb9fc69d3c7e"></a>

```c
enum { BT_A2DP_DISCOVER_EP_STOP = 0 , BT_A2DP_DISCOVER_EP_CONTINUE }
```

相关声明：[BT_A2DP_DISCOVER_EP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga7830b874f18be8fc1c62cb9fc69d3c7eab55d2d864da292240e19ee251de832f2)、[BT_A2DP_DISCOVER_EP_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga7830b874f18be8fc1c62cb9fc69d3c7eae38f6b8bd78c8a975d0f59c74fe9d367)。

辅助枚举（Helper Enum），用作 bt_a2dp_discover_ep_cb 的返回值。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_gabc74f6c2a0cf619adbefcf9ffbca1c03"></a>

```c
struct bt_a2dp * bt_a2dp_connect (struct bt_conn *conn)
```

相关声明：[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)、[bt_a2dp_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gabc74f6c2a0cf619adbefcf9ffbca1c03)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

建立 A2DP 连接（Connect）。

<a id="r_gabbf0d012860a233ecc84ed333e0da051"></a>

```c
int bt_a2dp_disconnect (struct bt_a2dp *a2dp)
```

相关声明：[bt_a2dp_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gabbf0d012860a233ecc84ed333e0da051)、[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)。

断开 A2DP 的 L2CAP 连接（Disconnect）。

<a id="r_gab1cd7028a41bfdc34ce8cc60aed239de"></a>

```c
int bt_a2dp_register_ep (struct bt_a2dp_ep *ep, uint8_t media_type, uint8_t sep_type)
```

相关声明：[bt_a2dp_register_ep](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gab1cd7028a41bfdc34ce8cc60aed239de)、[bt_a2dp_ep](../bluetooth_classic_model_reference/P007_bt_a2dp_ep_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

端点注册（Endpoint Registration）。

<a id="r_ga4af29d7c162743c00534868ba945b7ec"></a>

```c
int bt_a2dp_register_cb (struct bt_a2dp_cb *cb)
```

相关声明：[bt_a2dp_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga4af29d7c162743c00534868ba945b7ec)、[bt_a2dp_cb](../bluetooth_classic_model_reference/P002_bt_a2dp_cb_结构体.md)。

注册回调（Callback）。

<a id="r_ga09470ceb08b66661d63c951736f34a5d"></a>

```c
struct bt_conn * bt_a2dp_get_conn (struct bt_a2dp *a2dp)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_a2dp_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga09470ceb08b66661d63c951736f34a5d)、[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)。

获取 A2DP 对应的 ACL 连接（ACL Connection）。

<a id="r_ga931234227bc2b9eaed9cd60471ee54db"></a>

```c
int bt_a2dp_discover (struct bt_a2dp *a2dp, struct bt_a2dp_discover_param *param)
```

相关声明：[bt_a2dp_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga931234227bc2b9eaed9cd60471ee54db)、[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)、[bt_a2dp_discover_param](../bluetooth_classic_model_reference/P006_bt_a2dp_discover_param_结构体.md)。

发现远端端点（Remote Endpoints）。

<a id="r_gab8459d999437daa7a107b1bdf4c5ea46"></a>

```c
void bt_a2dp_stream_cb_register (struct bt_a2dp_stream *stream, struct bt_a2dp_stream_ops *ops)
```

相关声明：[bt_a2dp_stream_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gab8459d999437daa7a107b1bdf4c5ea46)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)、[bt_a2dp_stream_ops](../bluetooth_classic_model_reference/P010_bt_a2dp_stream_ops_结构体.md)。

为流（Stream）注册音频回调（Audio Callbacks）。

<a id="r_ga3ff3ca4cd016025f95690e89643f0ff5"></a>

```c
int bt_a2dp_stream_config (struct bt_a2dp *a2dp, struct bt_a2dp_stream *stream, struct bt_a2dp_ep *local_ep, struct bt_a2dp_ep *remote_ep, struct bt_a2dp_codec_cfg *config)
```

相关声明：[bt_a2dp_stream_config](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga3ff3ca4cd016025f95690e89643f0ff5)、[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)、[bt_a2dp_ep](../bluetooth_classic_model_reference/P007_bt_a2dp_ep_结构体.md)、[bt_a2dp_ep](../bluetooth_classic_model_reference/P007_bt_a2dp_ep_结构体.md)、[bt_a2dp_codec_cfg](../bluetooth_classic_model_reference/P003_bt_a2dp_codec_cfg_结构体.md)。

配置端点（Configure Endpoint）。

<a id="r_ga68f74181bba610c7fd158558afdcbd86"></a>

```c
int bt_a2dp_stream_get_config (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga68f74181bba610c7fd158558afdcbd86)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

获取流的配置（Stream Configuration）。

<a id="r_gaf47e0028176494f5353ee00261ffa49a"></a>

```c
int bt_a2dp_stream_establish (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_establish](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gaf47e0028176494f5353ee00261ffa49a)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

建立 A2DP 流（Stream）。

<a id="r_ga194e7ec86715cf9007de30f6492e4f58"></a>

```c
int bt_a2dp_stream_release (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_release](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga194e7ec86715cf9007de30f6492e4f58)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

释放 A2DP 流（Stream）。

<a id="r_ga368403c64581b761099631280014d877"></a>

```c
int bt_a2dp_stream_start (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga368403c64581b761099631280014d877)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

启动 A2DP 流（Stream）。

<a id="r_gaf22030f4edd5401b2d5359bcb0590145"></a>

```c
int bt_a2dp_stream_suspend (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gaf22030f4edd5401b2d5359bcb0590145)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

暂停 A2DP 流（Stream）。

<a id="r_ga70fc5f43265a4c407a847c4205cd7697"></a>

```c
int bt_a2dp_stream_reconfig (struct bt_a2dp_stream *stream, struct bt_a2dp_codec_cfg *config)
```

相关声明：[bt_a2dp_stream_reconfig](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga70fc5f43265a4c407a847c4205cd7697)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)、[bt_a2dp_codec_cfg](../bluetooth_classic_model_reference/P003_bt_a2dp_codec_cfg_结构体.md)。

重新配置 A2DP 流（Stream）。

<a id="r_ga7999e06ef74be78ec2744bb24ff72912"></a>

```c
int bt_a2dp_stream_abort (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga7999e06ef74be78ec2744bb24ff72912)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

中止 A2DP 流（Stream）。

<a id="r_gafb67c234c9d5748e54d5e67c7b148353"></a>

```c
uint32_t bt_a2dp_get_mtu (struct bt_a2dp_stream *stream)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bt_a2dp_get_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gafb67c234c9d5748e54d5e67c7b148353)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

获取流的 L2CAP 最大传输单元（MTU）。

<a id="r_gae8591dc8ef0b1c1e2af9ff5fb0cab681"></a>

```c
int bt_a2dp_stream_send (struct bt_a2dp_stream *stream, struct net_buf *buf, uint16_t seq_num, uint32_t ts)
```

相关声明：[bt_a2dp_stream_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gae8591dc8ef0b1c1e2af9ff5fb0cab681)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送 A2DP 媒体数据（Media Data）。

<a id="r_ga16da4e0afe99748ded1fc6db3911c85d"></a>

```c
struct net_buf * bt_a2dp_stream_create_pdu (struct net_buf_pool *pool, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_a2dp_stream_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga16da4e0afe99748ded1fc6db3911c85d)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为 bt_a2dp_stream_send 分配 net_buf。

<a id="r_gaa332aeced3d91fc9178bc9dcc0d10564"></a>

```c
int bt_a2dp_stream_delay_report (struct bt_a2dp_stream *stream, uint16_t delay)
```

相关声明：[bt_a2dp_stream_delay_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gaa332aeced3d91fc9178bc9dcc0d10564)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

发送延迟报告（Delay Report）。


## 1.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/bluetooth/l2cap.h](../api_source_system_reference/P016_l2cap.h_源码浏览.md)
- [zephyr/bluetooth/classic/avdtp.h](../api_source_supplement_reference/P018_avdtp.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P001_a2dp.h_源码浏览.md)
- [bt_a2dp_codec_ie](../bluetooth_classic_model_reference/P004_bt_a2dp_codec_ie_结构体.md)
- [bt_a2dp_codec_cfg](../bluetooth_classic_model_reference/P003_bt_a2dp_codec_cfg_结构体.md)
- [bt_a2dp_ep](../bluetooth_classic_model_reference/P007_bt_a2dp_ep_结构体.md)
- [bt_a2dp_ep_info](../bluetooth_classic_model_reference/P008_bt_a2dp_ep_info_结构体.md)
- [bt_a2dp_discover_param](../bluetooth_classic_model_reference/P006_bt_a2dp_discover_param_结构体.md)
- [bt_a2dp_cb](../bluetooth_classic_model_reference/P002_bt_a2dp_cb_结构体.md)
- [bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)
- [bt_a2dp_stream_ops](../bluetooth_classic_model_reference/P010_bt_a2dp_stream_ops_结构体.md)
- [BT_A2DP_SBC_IE_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gaf83aa927ac312cfc8577056afffeae56)
- [BT_A2DP_MPEG_1_2_IE_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga313fec2276421be6f29c0309e67755eb)
- [BT_A2DP_MPEG_2_4_IE_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga73ae4b6e2913b3772b32c520bf84de8c)
- [BT_A2DP_EP_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga3a2b2021adcd90c8c5adbbeb1441826d)
- [BT_A2DP_SINK_EP_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga3c0b5c4dbbea7bc3999a81e2bc579a46)
- [BT_A2DP_SOURCE_EP_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gab6dc5275f5c5057e2337acc4e31dc2fa)
- [BT_A2DP_SBC_SINK_EP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga0c6adc3461d7e4754bd595da457870c0)
- [BT_A2DP_SBC_SOURCE_EP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga47dc400bc57140a40975ec1570d79582)
- [BT_A2DP_SBC_SINK_EP_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga76fb351efe2730311baae1ad6cddbcb1)
- [BT_A2DP_SBC_SOURCE_EP_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga6830ae27e85471935ae604b18cf779e2)
- [BT_A2DP_SBC_EP_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gac879cbea5f0bbecfc0ec948d6e46c073)
- [BT_A2DP_SBC_EP_CFG_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gabbfd3bc3fa080517ef4395b30fd697f7)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_a2dp_discover_ep_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gae054d7f9fa92e45c7d40ec0e1d8730ed)
- [bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)
- [bt_a2dp_err_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga4162a6db1ead67f52f961d660beabb8c)
- [BT_A2DP_INVALID_CODEC_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca1718e53b8632688eb1aa9253248e7591)
- [BT_A2DP_NOT_SUPPORTED_CODEC_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cabda2c831224e1c994b5c67ea9fe7be7f)
- [BT_A2DP_INVALID_SAMPLING_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca68471cd1037db6687bc1f60cf500681c)
- [BT_A2DP_NOT_SUPPORTED_SAMPLING_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca499c532b0069432802cbe72bc33e5a76)
- [BT_A2DP_INVALID_CHANNEL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca6222f61712e16dbd0b56fda692844396)
- [BT_A2DP_NOT_SUPPORTED_CHANNEL_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca8e62e8df4d9e2a5389ad1620de7af755)
- [BT_A2DP_INVALID_SUBBANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca8e06f678574f38b9538f8c45622cee3f)
- [BT_A2DP_NOT_SUPPORTED_SUBBANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca2a20d81b47a5b3119988c3702ba1e84d)
- [BT_A2DP_INVALID_ALLOCATION_METHOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8caf13a2a05042cb4ee373017fabd92303a)
- [BT_A2DP_NOT_SUPPORTED_ALLOCATION_METHOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca81723b89ccf0d40db2a2edacd2cbaca8)
- [BT_A2DP_INVALID_MINIMUM_BITPOOL_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cad81217701b215d26e65c220c83ed4a02)
- [BT_A2DP_NOT_SUPPORTED_MINIMUM_BITPOOL_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cacd474a29c941a1b1ad164a63d07763d3)
- [BT_A2DP_INVALID_MAXIMUM_BITPOOL_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca71dfaa290af68147e83541e37d59d5cf)
- [BT_A2DP_NOT_SUPPORTED_MAXIMUM_BITPOOL_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca9fe3d3aea48e5c5122ce058e8918133f)
- [BT_A2DP_INVALID_LAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8caf2bd03a778271c6310fb51d3dccccb41)
- [BT_A2DP_NOT_SUPPORTED_LAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca48b381cca4ddd1ccb26037e84b0bea9e)
- [BT_A2DP_NOT_SUPPORTED_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca4e204c6ea5acfe20be37da6fca38eaec)
- [BT_A2DP_NOT_SUPPORTED_MPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca95a7b280dbdb757fab3b8b2077120d8f)
- [BT_A2DP_NOT_SUPPORTED_VBR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca92d1fb010cc69e27ec988de69c9bbd51)
- [BT_A2DP_INVALID_BIT_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cadb4d2cc815b2c01e6f7e2666305d4476)
- [BT_A2DP_NOT_SUPPORTED_BIT_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8caf86c457a7e016f440089469c9f442ad1)
- [BT_A2DP_INVALID_OBJECT_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca3896984afb4b5d164503bd53f0d4e429)
- [BT_A2DP_NOT_SUPPORTED_OBJECT_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca7b5bafd55d8020029e429b142c572615)
- [BT_A2DP_INVALID_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca182de8e823efe2f6575a900a567b3483)
- [BT_A2DP_NOT_SUPPORTED_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca3619a0a5c74de24b7dd8bd79b99ca91a)
- [BT_A2DP_INVALID_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca47dbe86cbbd2859243995d1d39c46d8d)
- [BT_A2DP_NOT_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca1d4c42781c74ebda2b084fe609ac284c)
- [BT_A2DP_NOT_SUPPORTED_MAXIMUM_SUL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cafdf002100cc0d7d1f07cf833ed331f2b)
- [BT_A2DP_INVALID_BLOCK_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8caebf8a58263b517b79947e9cc8a9678c3)
- [BT_A2DP_INVALID_CP_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8caab4c2af80c9588443a297e120f8ee611)
- [BT_A2DP_INVALID_CP_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca0554b3ef221c98b5cb4580ae049a6e63)
- [BT_A2DP_INVALID_CODEC_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca9aa4fc1c6f365b686ab4dc3875b93396)
- [BT_A2DP_NOT_SUPPORTED_CODEC_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca3c801158e7ed2623c2d2930ca91b94a9)
- [BT_A2DP_INVALID_DRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8cafd0982a65fc5657b13f35e0761425d96)
- [BT_A2DP_NOT_SUPPORTED_DRC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga4162a6db1ead67f52f961d660beabb8ca198bd8a559eca40d9d95f6edf8a703fd)
- [bt_a2dp_codec_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gafdb0a28b03d1e11f0595dd3f0b3cb4d6)
- [BT_A2DP_SBC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00)
- [BT_A2DP_MPEG1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6a1f1840d90c1d5ee28b650978bf012497)
- [BT_A2DP_MPEG2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6aefe729d388e0a3d8bb7759b986123c88)
- [BT_A2DP_MPEGD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6ad90f96068afbe94c6338d4906b07341b)
- [BT_A2DP_ATRAC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6a8b969e35e28d18cf05802e1381995e83)
- [BT_A2DP_VENDOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6ad3c292360558ea515a84d570c43c1701)
- [BT_A2DP_DISCOVER_EP_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga7830b874f18be8fc1c62cb9fc69d3c7eab55d2d864da292240e19ee251de832f2)
- [BT_A2DP_DISCOVER_EP_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gga7830b874f18be8fc1c62cb9fc69d3c7eae38f6b8bd78c8a975d0f59c74fe9d367)
- [bt_a2dp_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gabc74f6c2a0cf619adbefcf9ffbca1c03)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_a2dp_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gabbf0d012860a233ecc84ed333e0da051)
- [bt_a2dp_register_ep](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gab1cd7028a41bfdc34ce8cc60aed239de)
- [bt_a2dp_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga4af29d7c162743c00534868ba945b7ec)
- [bt_a2dp_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga09470ceb08b66661d63c951736f34a5d)
- [bt_a2dp_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga931234227bc2b9eaed9cd60471ee54db)
- [bt_a2dp_stream_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gab8459d999437daa7a107b1bdf4c5ea46)
- [bt_a2dp_stream_config](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga3ff3ca4cd016025f95690e89643f0ff5)
- [bt_a2dp_stream_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga68f74181bba610c7fd158558afdcbd86)
- [bt_a2dp_stream_establish](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gaf47e0028176494f5353ee00261ffa49a)
- [bt_a2dp_stream_release](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga194e7ec86715cf9007de30f6492e4f58)
- [bt_a2dp_stream_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga368403c64581b761099631280014d877)
- [bt_a2dp_stream_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gaf22030f4edd5401b2d5359bcb0590145)
- [bt_a2dp_stream_reconfig](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga70fc5f43265a4c407a847c4205cd7697)
- [bt_a2dp_stream_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga7999e06ef74be78ec2744bb24ff72912)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_a2dp_get_mtu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gafb67c234c9d5748e54d5e67c7b148353)
- [bt_a2dp_stream_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gae8591dc8ef0b1c1e2af9ff5fb0cab681)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_a2dp_stream_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga16da4e0afe99748ded1fc6db3911c85d)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [bt_a2dp_stream_delay_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gaa332aeced3d91fc9178bc9dcc0d10564)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__memory-controller__adi-max32-hpb.h_文件参考.md)
