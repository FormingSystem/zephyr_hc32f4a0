---
id: learning.zephyr-docs.api-socket-lora-topic-reference.page-2
title: 高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

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

<a id="r_bt_5Fa2dp"></a>

```c
struct bt_a2dp
```

相关声明：[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)。

高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）结构体。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_gaf83aa927ac312cfc8577056afffeae56"></a>

```c
#define BT_A2DP_SBC_IE_LENGTH (4U)
```

相关声明：[BT_A2DP_SBC_IE_LENGTH](#gaf83aa927ac312cfc8577056afffeae56)。

SBC 信息元素（IE）长度。

<a id="r_ga313fec2276421be6f29c0309e67755eb"></a>

```c
#define BT_A2DP_MPEG_1_2_IE_LENGTH (4U)
```

相关声明：[BT_A2DP_MPEG_1_2_IE_LENGTH](#ga313fec2276421be6f29c0309e67755eb)。

MPEG1、2 信息元素（IE）长度。

<a id="r_ga73ae4b6e2913b3772b32c520bf84de8c"></a>

```c
#define BT_A2DP_MPEG_2_4_IE_LENGTH (6U)
```

相关声明：[BT_A2DP_MPEG_2_4_IE_LENGTH](#ga73ae4b6e2913b3772b32c520bf84de8c)。

MPEG2、4 信息元素（IE）长度。

<a id="r_ga3a2b2021adcd90c8c5adbbeb1441826d"></a>

```c
#define BT_A2DP_EP_INIT(_role, _codec, _capability, _delay_report)
```

相关声明：[BT_A2DP_EP_INIT](#ga3a2b2021adcd90c8c5adbbeb1441826d)。

定义音频端点（Audio Endpoint）。

<a id="r_ga3c0b5c4dbbea7bc3999a81e2bc579a46"></a>

```c
#define BT_A2DP_SINK_EP_INIT(_codec, _capability, _delay_report)
```

相关声明：[BT_A2DP_SINK_EP_INIT](#ga3c0b5c4dbbea7bc3999a81e2bc579a46)。

定义音频接收端点（Audio Sink Endpoint）。

<a id="r_gab6dc5275f5c5057e2337acc4e31dc2fa"></a>

```c
#define BT_A2DP_SOURCE_EP_INIT(_codec, _capability, _delay_report)
```

相关声明：[BT_A2DP_SOURCE_EP_INIT](#gab6dc5275f5c5057e2337acc4e31dc2fa)。

定义音频源端点（Audio Source Endpoint）。

<a id="r_ga0c6adc3461d7e4754bd595da457870c0"></a>

```c
#define BT_A2DP_SBC_SINK_EP(_name, _freq, _ch_mode, _blk_len, _subband, _alloc_mthd, _min_bitpool, _max_bitpool, _delay_report)
```

相关声明：[BT_A2DP_SBC_SINK_EP](#ga0c6adc3461d7e4754bd595da457870c0)。

定义可用作 bt_a2dp_register_ep 参数的 SBC 接收端点（Sink Endpoint）。

<a id="r_ga47dc400bc57140a40975ec1570d79582"></a>

```c
#define BT_A2DP_SBC_SOURCE_EP(_name, _freq, _ch_mode, _blk_len, _subband, _alloc_mthd, _min_bitpool, _max_bitpool, _delay_report)
```

相关声明：[BT_A2DP_SBC_SOURCE_EP](#ga47dc400bc57140a40975ec1570d79582)。

定义可用作 bt_a2dp_register_ep 参数的 SBC 源端点（Source Endpoint）。

<a id="r_ga76fb351efe2730311baae1ad6cddbcb1"></a>

```c
#define BT_A2DP_SBC_SINK_EP_DEFAULT(_name)
```

相关声明：[BT_A2DP_SBC_SINK_EP_DEFAULT](#ga76fb351efe2730311baae1ad6cddbcb1)。

定义可用作 bt_a2dp_register_ep 参数的默认 SBC 接收端点（Default Sink Endpoint）。

<a id="r_ga6830ae27e85471935ae604b18cf779e2"></a>

```c
#define BT_A2DP_SBC_SOURCE_EP_DEFAULT(_name)
```

相关声明：[BT_A2DP_SBC_SOURCE_EP_DEFAULT](#ga6830ae27e85471935ae604b18cf779e2)。

定义可用作 bt_a2dp_register_ep 参数的默认 SBC 源端点（Default Source Endpoint）。

<a id="r_gac879cbea5f0bbecfc0ec948d6e46c073"></a>

```c
#define BT_A2DP_SBC_EP_CFG(_name, _freq_cfg, _ch_mode_cfg, _blk_len_cfg, _subband_cfg, _alloc_mthd_cfg, _min_bitpool_cfg, _max_bitpool_cfg)
```

相关声明：[BT_A2DP_SBC_EP_CFG](#gac879cbea5f0bbecfc0ec948d6e46c073)。

定义 SBC 默认配置（Default Configuration）。

<a id="r_gabbfd3bc3fa080517ef4395b30fd697f7"></a>

```c
#define BT_A2DP_SBC_EP_CFG_DEFAULT(_name, _freq_cfg)
```

相关声明：[BT_A2DP_SBC_EP_CFG_DEFAULT](#gabbfd3bc3fa080517ef4395b30fd697f7)。

定义 SBC 默认配置（Default Configuration）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.3\_类型定义（Typedefs）

<a id="r_gae054d7f9fa92e45c7d40ec0e1d8730ed"></a>

```c
typedef uint8_t(* bt_a2dp_discover_ep_cb) (struct bt_a2dp *a2dp, struct bt_a2dp_ep_info *info, struct bt_a2dp_ep **ep)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_a2dp_discover_ep_cb](#gae054d7f9fa92e45c7d40ec0e1d8730ed)、[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)、[bt_a2dp_ep_info](../bluetooth_classic_model_reference/P008_bt_a2dp_ep_info_结构体.md)、[bt_a2dp_ep](../bluetooth_classic_model_reference/P007_bt_a2dp_ep_结构体.md)。

发现流端点（Stream Endpoint）时调用。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.4\_枚举（Enumerations）

<a id="r_ga4162a6db1ead67f52f961d660beabb8c"></a>

```c
enum bt_a2dp_err_code { BT_A2DP_INVALID_CODEC_TYPE = 0xC1 , BT_A2DP_NOT_SUPPORTED_CODEC_TYPE = 0xC2 , BT_A2DP_INVALID_SAMPLING_FREQUENCY = 0xC3 , BT_A2DP_NOT_SUPPORTED_SAMPLING_FREQUENCY = 0xC4 , BT_A2DP_INVALID_CHANNEL_MODE = 0xC5 , BT_A2DP_NOT_SUPPORTED_CHANNEL_MODE = 0xC6 , BT_A2DP_INVALID_SUBBANDS = 0xC7 , BT_A2DP_NOT_SUPPORTED_SUBBANDS = 0xC8 , BT_A2DP_INVALID_ALLOCATION_METHOD = 0xC9 , BT_A2DP_NOT_SUPPORTED_ALLOCATION_METHOD = 0xCA , BT_A2DP_INVALID_MINIMUM_BITPOOL_VALUE = 0xCB , BT_A2DP_NOT_SUPPORTED_MINIMUM_BITPOOL_VALUE = 0xCC , BT_A2DP_INVALID_MAXIMUM_BITPOOL_VALUE = 0xCD , BT_A2DP_NOT_SUPPORTED_MAXIMUM_BITPOOL_VALUE = 0xCE , BT_A2DP_INVALID_LAYER = 0xCF , BT_A2DP_NOT_SUPPORTED_LAYER = 0xD0 , BT_A2DP_NOT_SUPPORTED_CRC = 0xD1 , BT_A2DP_NOT_SUPPORTED_MPF = 0xD2 , BT_A2DP_NOT_SUPPORTED_VBR = 0xD3 , BT_A2DP_INVALID_BIT_RATE = 0xD4 , BT_A2DP_NOT_SUPPORTED_BIT_RATE = 0xD5 , BT_A2DP_INVALID_OBJECT_TYPE = 0xD6 , BT_A2DP_NOT_SUPPORTED_OBJECT_TYPE = 0xD7 , BT_A2DP_INVALID_CHANNELS = 0xD8 , BT_A2DP_NOT_SUPPORTED_CHANNELS = 0xD9 , BT_A2DP_INVALID_VERSION = 0xDA , BT_A2DP_NOT_SUPPORTED_VERSION = 0xDB , BT_A2DP_NOT_SUPPORTED_MAXIMUM_SUL = 0xDC , BT_A2DP_INVALID_BLOCK_LENGTH = 0xDD , BT_A2DP_INVALID_CP_TYPE = 0xE0 , BT_A2DP_INVALID_CP_FORMAT = 0xE1 , BT_A2DP_INVALID_CODEC_PARAMETER = 0xE2 , BT_A2DP_NOT_SUPPORTED_CODEC_PARAMETER = 0xE3 , BT_A2DP_INVALID_DRC = 0xE4 , BT_A2DP_NOT_SUPPORTED_DRC = 0xE5 }
```

相关声明：[bt_a2dp_err_code](#ga4162a6db1ead67f52f961d660beabb8c)、[BT_A2DP_INVALID_CODEC_TYPE](#gga4162a6db1ead67f52f961d660beabb8ca1718e53b8632688eb1aa9253248e7591)、[BT_A2DP_NOT_SUPPORTED_CODEC_TYPE](#gga4162a6db1ead67f52f961d660beabb8cabda2c831224e1c994b5c67ea9fe7be7f)、[BT_A2DP_INVALID_SAMPLING_FREQUENCY](#gga4162a6db1ead67f52f961d660beabb8ca68471cd1037db6687bc1f60cf500681c)、[BT_A2DP_NOT_SUPPORTED_SAMPLING_FREQUENCY](#gga4162a6db1ead67f52f961d660beabb8ca499c532b0069432802cbe72bc33e5a76)、[BT_A2DP_INVALID_CHANNEL_MODE](#gga4162a6db1ead67f52f961d660beabb8ca6222f61712e16dbd0b56fda692844396)、[BT_A2DP_NOT_SUPPORTED_CHANNEL_MODE](#gga4162a6db1ead67f52f961d660beabb8ca8e62e8df4d9e2a5389ad1620de7af755)、[BT_A2DP_INVALID_SUBBANDS](#gga4162a6db1ead67f52f961d660beabb8ca8e06f678574f38b9538f8c45622cee3f)、[BT_A2DP_NOT_SUPPORTED_SUBBANDS](#gga4162a6db1ead67f52f961d660beabb8ca2a20d81b47a5b3119988c3702ba1e84d)、[BT_A2DP_INVALID_ALLOCATION_METHOD](#gga4162a6db1ead67f52f961d660beabb8caf13a2a05042cb4ee373017fabd92303a)、[BT_A2DP_NOT_SUPPORTED_ALLOCATION_METHOD](#gga4162a6db1ead67f52f961d660beabb8ca81723b89ccf0d40db2a2edacd2cbaca8)、[BT_A2DP_INVALID_MINIMUM_BITPOOL_VALUE](#gga4162a6db1ead67f52f961d660beabb8cad81217701b215d26e65c220c83ed4a02)、[BT_A2DP_NOT_SUPPORTED_MINIMUM_BITPOOL_VALUE](#gga4162a6db1ead67f52f961d660beabb8cacd474a29c941a1b1ad164a63d07763d3)、[BT_A2DP_INVALID_MAXIMUM_BITPOOL_VALUE](#gga4162a6db1ead67f52f961d660beabb8ca71dfaa290af68147e83541e37d59d5cf)、[BT_A2DP_NOT_SUPPORTED_MAXIMUM_BITPOOL_VALUE](#gga4162a6db1ead67f52f961d660beabb8ca9fe3d3aea48e5c5122ce058e8918133f)、[BT_A2DP_INVALID_LAYER](#gga4162a6db1ead67f52f961d660beabb8caf2bd03a778271c6310fb51d3dccccb41)、[BT_A2DP_NOT_SUPPORTED_LAYER](#gga4162a6db1ead67f52f961d660beabb8ca48b381cca4ddd1ccb26037e84b0bea9e)、[BT_A2DP_NOT_SUPPORTED_CRC](#gga4162a6db1ead67f52f961d660beabb8ca4e204c6ea5acfe20be37da6fca38eaec)、[BT_A2DP_NOT_SUPPORTED_MPF](#gga4162a6db1ead67f52f961d660beabb8ca95a7b280dbdb757fab3b8b2077120d8f)、[BT_A2DP_NOT_SUPPORTED_VBR](#gga4162a6db1ead67f52f961d660beabb8ca92d1fb010cc69e27ec988de69c9bbd51)、[BT_A2DP_INVALID_BIT_RATE](#gga4162a6db1ead67f52f961d660beabb8cadb4d2cc815b2c01e6f7e2666305d4476)、[BT_A2DP_NOT_SUPPORTED_BIT_RATE](#gga4162a6db1ead67f52f961d660beabb8caf86c457a7e016f440089469c9f442ad1)、[BT_A2DP_INVALID_OBJECT_TYPE](#gga4162a6db1ead67f52f961d660beabb8ca3896984afb4b5d164503bd53f0d4e429)、[BT_A2DP_NOT_SUPPORTED_OBJECT_TYPE](#gga4162a6db1ead67f52f961d660beabb8ca7b5bafd55d8020029e429b142c572615)、[BT_A2DP_INVALID_CHANNELS](#gga4162a6db1ead67f52f961d660beabb8ca182de8e823efe2f6575a900a567b3483)、[BT_A2DP_NOT_SUPPORTED_CHANNELS](#gga4162a6db1ead67f52f961d660beabb8ca3619a0a5c74de24b7dd8bd79b99ca91a)、[BT_A2DP_INVALID_VERSION](#gga4162a6db1ead67f52f961d660beabb8ca47dbe86cbbd2859243995d1d39c46d8d)、[BT_A2DP_NOT_SUPPORTED_VERSION](#gga4162a6db1ead67f52f961d660beabb8ca1d4c42781c74ebda2b084fe609ac284c)、[BT_A2DP_NOT_SUPPORTED_MAXIMUM_SUL](#gga4162a6db1ead67f52f961d660beabb8cafdf002100cc0d7d1f07cf833ed331f2b)、[BT_A2DP_INVALID_BLOCK_LENGTH](#gga4162a6db1ead67f52f961d660beabb8caebf8a58263b517b79947e9cc8a9678c3)、[BT_A2DP_INVALID_CP_TYPE](#gga4162a6db1ead67f52f961d660beabb8caab4c2af80c9588443a297e120f8ee611)、[BT_A2DP_INVALID_CP_FORMAT](#gga4162a6db1ead67f52f961d660beabb8ca0554b3ef221c98b5cb4580ae049a6e63)、[BT_A2DP_INVALID_CODEC_PARAMETER](#gga4162a6db1ead67f52f961d660beabb8ca9aa4fc1c6f365b686ab4dc3875b93396)、[BT_A2DP_NOT_SUPPORTED_CODEC_PARAMETER](#gga4162a6db1ead67f52f961d660beabb8ca3c801158e7ed2623c2d2930ca91b94a9)、[BT_A2DP_INVALID_DRC](#gga4162a6db1ead67f52f961d660beabb8cafd0982a65fc5657b13f35e0761425d96)、[BT_A2DP_NOT_SUPPORTED_DRC](#gga4162a6db1ead67f52f961d660beabb8ca198bd8a559eca40d9d95f6edf8a703fd)。

A2DP 错误码（Error Code）。

<a id="r_gafdb0a28b03d1e11f0595dd3f0b3cb4d6"></a>

```c
enum bt_a2dp_codec_type { BT_A2DP_SBC = 0x00 , BT_A2DP_MPEG1 = 0x01 , BT_A2DP_MPEG2 = 0x02 , BT_A2DP_MPEGD = 0x03 , BT_A2DP_ATRAC = 0x04 , BT_A2DP_VENDOR = 0xff }
```

相关声明：[bt_a2dp_codec_type](#gafdb0a28b03d1e11f0595dd3f0b3cb4d6)、[BT_A2DP_SBC](#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00)、[BT_A2DP_MPEG1](#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6a1f1840d90c1d5ee28b650978bf012497)、[BT_A2DP_MPEG2](#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6aefe729d388e0a3d8bb7759b986123c88)、[BT_A2DP_MPEGD](#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6ad90f96068afbe94c6338d4906b07341b)、[BT_A2DP_ATRAC](#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6a8b969e35e28d18cf05802e1381995e83)、[BT_A2DP_VENDOR](#ggafdb0a28b03d1e11f0595dd3f0b3cb4d6ad3c292360558ea515a84d570c43c1701)。

编解码器类型（Codec Type）。

<a id="r_ga7830b874f18be8fc1c62cb9fc69d3c7e"></a>

```c
enum { BT_A2DP_DISCOVER_EP_STOP = 0 , BT_A2DP_DISCOVER_EP_CONTINUE }
```

相关声明：[BT_A2DP_DISCOVER_EP_STOP](#gga7830b874f18be8fc1c62cb9fc69d3c7eab55d2d864da292240e19ee251de832f2)、[BT_A2DP_DISCOVER_EP_CONTINUE](#gga7830b874f18be8fc1c62cb9fc69d3c7eae38f6b8bd78c8a975d0f59c74fe9d367)。

辅助枚举（Helper Enum），用作 bt_a2dp_discover_ep_cb 的返回值。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.5\_函数（Functions）

<a id="r_gabc74f6c2a0cf619adbefcf9ffbca1c03"></a>

```c
struct bt_a2dp * bt_a2dp_connect (struct bt_conn *conn)
```

相关声明：[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)、[bt_a2dp_connect](#gabc74f6c2a0cf619adbefcf9ffbca1c03)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

建立 A2DP 连接（Connect）。

<a id="r_gabbf0d012860a233ecc84ed333e0da051"></a>

```c
int bt_a2dp_disconnect (struct bt_a2dp *a2dp)
```

相关声明：[bt_a2dp_disconnect](#gabbf0d012860a233ecc84ed333e0da051)、[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)。

断开 A2DP 的 L2CAP 连接（Disconnect）。

<a id="r_gab1cd7028a41bfdc34ce8cc60aed239de"></a>

```c
int bt_a2dp_register_ep (struct bt_a2dp_ep *ep, uint8_t media_type, uint8_t sep_type)
```

相关声明：[bt_a2dp_register_ep](#gab1cd7028a41bfdc34ce8cc60aed239de)、[bt_a2dp_ep](../bluetooth_classic_model_reference/P007_bt_a2dp_ep_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

端点注册（Endpoint Registration）。

<a id="r_ga4af29d7c162743c00534868ba945b7ec"></a>

```c
int bt_a2dp_register_cb (struct bt_a2dp_cb *cb)
```

相关声明：[bt_a2dp_register_cb](#ga4af29d7c162743c00534868ba945b7ec)、[bt_a2dp_cb](../bluetooth_classic_model_reference/P002_bt_a2dp_cb_结构体.md)。

注册回调（Callback）。

<a id="r_ga09470ceb08b66661d63c951736f34a5d"></a>

```c
struct bt_conn * bt_a2dp_get_conn (struct bt_a2dp *a2dp)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_a2dp_get_conn](#ga09470ceb08b66661d63c951736f34a5d)、[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)。

获取 A2DP 对应的 ACL 连接（ACL Connection）。

<a id="r_ga931234227bc2b9eaed9cd60471ee54db"></a>

```c
int bt_a2dp_discover (struct bt_a2dp *a2dp, struct bt_a2dp_discover_param *param)
```

相关声明：[bt_a2dp_discover](#ga931234227bc2b9eaed9cd60471ee54db)、[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)、[bt_a2dp_discover_param](../bluetooth_classic_model_reference/P006_bt_a2dp_discover_param_结构体.md)。

发现远端端点（Remote Endpoints）。

<a id="r_gab8459d999437daa7a107b1bdf4c5ea46"></a>

```c
void bt_a2dp_stream_cb_register (struct bt_a2dp_stream *stream, struct bt_a2dp_stream_ops *ops)
```

相关声明：[bt_a2dp_stream_cb_register](#gab8459d999437daa7a107b1bdf4c5ea46)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)、[bt_a2dp_stream_ops](../bluetooth_classic_model_reference/P010_bt_a2dp_stream_ops_结构体.md)。

为流（Stream）注册音频回调（Audio Callbacks）。

<a id="r_ga3ff3ca4cd016025f95690e89643f0ff5"></a>

```c
int bt_a2dp_stream_config (struct bt_a2dp *a2dp, struct bt_a2dp_stream *stream, struct bt_a2dp_ep *local_ep, struct bt_a2dp_ep *remote_ep, struct bt_a2dp_codec_cfg *config)
```

相关声明：[bt_a2dp_stream_config](#ga3ff3ca4cd016025f95690e89643f0ff5)、[bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)、[bt_a2dp_ep](../bluetooth_classic_model_reference/P007_bt_a2dp_ep_结构体.md)、[bt_a2dp_ep](../bluetooth_classic_model_reference/P007_bt_a2dp_ep_结构体.md)、[bt_a2dp_codec_cfg](../bluetooth_classic_model_reference/P003_bt_a2dp_codec_cfg_结构体.md)。

配置端点（Configure Endpoint）。

<a id="r_ga68f74181bba610c7fd158558afdcbd86"></a>

```c
int bt_a2dp_stream_get_config (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_get_config](#ga68f74181bba610c7fd158558afdcbd86)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

获取流的配置（Stream Configuration）。

<a id="r_gaf47e0028176494f5353ee00261ffa49a"></a>

```c
int bt_a2dp_stream_establish (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_establish](#gaf47e0028176494f5353ee00261ffa49a)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

建立 A2DP 流（Stream）。

<a id="r_ga194e7ec86715cf9007de30f6492e4f58"></a>

```c
int bt_a2dp_stream_release (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_release](#ga194e7ec86715cf9007de30f6492e4f58)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

释放 A2DP 流（Stream）。

<a id="r_ga368403c64581b761099631280014d877"></a>

```c
int bt_a2dp_stream_start (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_start](#ga368403c64581b761099631280014d877)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

启动 A2DP 流（Stream）。

<a id="r_gaf22030f4edd5401b2d5359bcb0590145"></a>

```c
int bt_a2dp_stream_suspend (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_suspend](#gaf22030f4edd5401b2d5359bcb0590145)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

暂停 A2DP 流（Stream）。

<a id="r_ga70fc5f43265a4c407a847c4205cd7697"></a>

```c
int bt_a2dp_stream_reconfig (struct bt_a2dp_stream *stream, struct bt_a2dp_codec_cfg *config)
```

相关声明：[bt_a2dp_stream_reconfig](#ga70fc5f43265a4c407a847c4205cd7697)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)、[bt_a2dp_codec_cfg](../bluetooth_classic_model_reference/P003_bt_a2dp_codec_cfg_结构体.md)。

重新配置 A2DP 流（Stream）。

<a id="r_ga7999e06ef74be78ec2744bb24ff72912"></a>

```c
int bt_a2dp_stream_abort (struct bt_a2dp_stream *stream)
```

相关声明：[bt_a2dp_stream_abort](#ga7999e06ef74be78ec2744bb24ff72912)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

中止 A2DP 流（Stream）。

<a id="r_gafb67c234c9d5748e54d5e67c7b148353"></a>

```c
uint32_t bt_a2dp_get_mtu (struct bt_a2dp_stream *stream)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bt_a2dp_get_mtu](#gafb67c234c9d5748e54d5e67c7b148353)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)。

获取流的 L2CAP 最大传输单元（MTU）。

<a id="r_gae8591dc8ef0b1c1e2af9ff5fb0cab681"></a>

```c
int bt_a2dp_stream_send (struct bt_a2dp_stream *stream, struct net_buf *buf, uint16_t seq_num, uint32_t ts)
```

相关声明：[bt_a2dp_stream_send](#gae8591dc8ef0b1c1e2af9ff5fb0cab681)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送 A2DP 媒体数据（Media Data）。

<a id="r_ga16da4e0afe99748ded1fc6db3911c85d"></a>

```c
struct net_buf * bt_a2dp_stream_create_pdu (struct net_buf_pool *pool, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_a2dp_stream_create_pdu](#ga16da4e0afe99748ded1fc6db3911c85d)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为 bt_a2dp_stream_send 分配 net_buf。

<a id="r_gaa332aeced3d91fc9178bc9dcc0d10564"></a>

```c
int bt_a2dp_stream_delay_report (struct bt_a2dp_stream *stream, uint16_t delay)
```

相关声明：[bt_a2dp_stream_delay_report](#gaa332aeced3d91fc9178bc9dcc0d10564)、[bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

发送延迟报告（Delay Report）。

## 2.6\_详细说明（Detailed Documentation）

<a id="ga3a2b2021adcd90c8c5adbbeb1441826d"></a>

### `BT_A2DP_EP_INIT`

```c
#define BT_A2DP_EP_INIT ( _role, _codec, _capability, _delay_report )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

展开值（Value）：

```c
{                                                                                          \
        .codec_type = _codec,                                                              \
        .sep = {.sep_info = {.media_type = BT_AVDTP_AUDIO, .tsep = _role}},                \
        .codec_cap = _capability, .stream = NULL,                                          \
        .delay_report = _delay_report,                                                     \
}
```

定义音频端点（Audio Endpoint）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_role` | `BT_AVDTP_SOURCE` 或 `BT_AVDTP_SINK`。 |
| `_codec` | 枚举（Enumeration）`bt_a2dp_codec_id` 的值。 |
| `_capability` | 编解码器能力（Codec Capability）。 |
| `_delay_report` | 延迟报告能力（Delay Report Capability）。 |

<a id="ga313fec2276421be6f29c0309e67755eb"></a>

### `BT_A2DP_MPEG_1_2_IE_LENGTH`

```c
#define BT_A2DP_MPEG_1_2_IE_LENGTH (4U)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

MPEG1、2 信息元素（IE）长度。

<a id="ga73ae4b6e2913b3772b32c520bf84de8c"></a>

### `BT_A2DP_MPEG_2_4_IE_LENGTH`

```c
#define BT_A2DP_MPEG_2_4_IE_LENGTH (6U)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

MPEG2、4 信息元素（IE）长度。

<a id="gac879cbea5f0bbecfc0ec948d6e46c073"></a>

### `BT_A2DP_SBC_EP_CFG`

```c
#define BT_A2DP_SBC_EP_CFG ( _name, _freq_cfg, _ch_mode_cfg, _blk_len_cfg, _subband_cfg, _alloc_mthd_cfg, _min_bitpool_cfg, _max_bitpool_cfg )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

展开值（Value）：

```c
static struct bt_a2dp_codec_ie bt_a2dp_codec_ie##_name = {                                 \
        .len = BT_A2DP_SBC_IE_LENGTH,                                                      \
        .codec_ie = {_freq_cfg | _ch_mode_cfg,                                             \
                     _blk_len_cfg | _subband_cfg | _alloc_mthd_cfg, _min_bitpool_cfg,      \
                     _max_bitpool_cfg},                                                    \
};                                                                                         \
struct bt_a2dp_codec_cfg _name = {                                                         \
        .codec_config = &bt_a2dp_codec_ie##_name,                                          \
}
```

定义 SBC 默认配置（Default Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 唯一的结构体名称后缀（Structure Name Postfix）。 |
| `_freq_cfg` | SBC 编解码器采样频率（Codec Frequency），例如 `A2DP_SBC_SAMP_FREQ_44100`。 |
| `_ch_mode_cfg` | SBC 编解码器通道模式（Codec Channel Mode），例如 `A2DP_SBC_CH_MODE_JOINT`。 |
| `_blk_len_cfg` | SBC 编解码器块长度（Codec Block Length），例如 `A2DP_SBC_BLK_LEN_16`。 |
| `_subband_cfg` | SBC 编解码器子带（Codec Subband），例如 `A2DP_SBC_SUBBAND_8`。 |
| `_alloc_mthd_cfg` | SBC 编解码器分配方法（Codec Allocation Method），例如 `A2DP_SBC_ALLOC_MTHD_LOUDNESS`。 |
| `_min_bitpool_cfg` | SBC 编解码器最小比特池（Minimum Bitpool），例如 `18`。 |
| `_max_bitpool_cfg` | SBC 编解码器最大比特池（Maximum Bitpool），例如 `35`。 |

<a id="gabbfd3bc3fa080517ef4395b30fd697f7"></a>

### `BT_A2DP_SBC_EP_CFG_DEFAULT`

```c
#define BT_A2DP_SBC_EP_CFG_DEFAULT ( _name, _freq_cfg )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

展开值（Value）：

```c
static struct bt_a2dp_codec_ie bt_a2dp_codec_ie##_name = {                                 \
        .len = BT_A2DP_SBC_IE_LENGTH,                                                      \
        .codec_ie = {_freq_cfg | A2DP_SBC_CH_MODE_JOINT,                                   \
                     A2DP_SBC_BLK_LEN_16 | A2DP_SBC_SUBBAND_8 |                            \
                             A2DP_SBC_ALLOC_MTHD_LOUDNESS,                                 \
                     18U, 35U},                                                            \
};                                                                                         \
struct bt_a2dp_codec_cfg _name = {                                                         \
        .codec_config = &bt_a2dp_codec_ie##_name,                                          \
}
```

定义 SBC 默认配置（Default Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 唯一的结构体名称后缀（Structure Name Postfix）。 |
| `_freq_cfg` | 用于配置远端同类型编解码器端点（Remote Same Codec Type Endpoint）的频率（Frequency）。 |

<a id="gaf83aa927ac312cfc8577056afffeae56"></a>

### `BT_A2DP_SBC_IE_LENGTH`

```c
#define BT_A2DP_SBC_IE_LENGTH (4U)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

SBC 信息元素（IE）长度。

<a id="ga0c6adc3461d7e4754bd595da457870c0"></a>

### `BT_A2DP_SBC_SINK_EP`

```c
#define BT_A2DP_SBC_SINK_EP ( _name, _freq, _ch_mode, _blk_len, _subband, _alloc_mthd, _min_bitpool, _max_bitpool, _delay_report )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

展开值（Value）：

```c
static struct bt_a2dp_codec_ie bt_a2dp_ep_cap_ie##_name = {                                \
        .len = BT_A2DP_SBC_IE_LENGTH,                                                      \
        .codec_ie = {_freq | _ch_mode, _blk_len | _subband | _alloc_mthd, _min_bitpool,    \
                     _max_bitpool}};                                                       \
static struct bt_a2dp_ep _name =                                                           \
        BT_A2DP_SINK_EP_INIT(BT_A2DP_SBC, (&bt_a2dp_ep_cap_ie##_name), _delay_report)
```

定义可用作 bt_a2dp_register_ep 参数的 SBC 接收端点（Sink Endpoint）。

高级音频分发配置文件（A2DP）规范强制要求支持 SBC；使用 `BT_A2DP_SBC_SINK_EP_DEFAULT` 可以更方便地注册 SBC 端点（Endpoint）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 唯一的结构体名称后缀（Structure Name Postfix）。 |
| `_freq` | SBC 编解码器采样频率（Codec Frequency），例如 `A2DP_SBC_SAMP_FREQ_44100 \| A2DP_SBC_SAMP_FREQ_48000`。 |
| `_ch_mode` | SBC 编解码器通道模式（Codec Channel Mode），例如 `A2DP_SBC_CH_MODE_MONO \| A2DP_SBC_CH_MODE_STEREO`。 |
| `_blk_len` | SBC 编解码器块长度（Codec Block Length），例如 `A2DP_SBC_BLK_LEN_16`。 |
| `_subband` | SBC 编解码器子带（Codec Subband），例如 `A2DP_SBC_SUBBAND_8`。 |
| `_alloc_mthd` | SBC 编解码器分配方法（Codec Allocation Method），例如 `A2DP_SBC_ALLOC_MTHD_LOUDNESS`。 |
| `_min_bitpool` | SBC 编解码器最小比特池（Minimum Bitpool），例如 `18`。 |
| `_max_bitpool` | SBC 编解码器最大比特池（Maximum Bitpool），例如 `35`。 |
| `_delay_report` | 延迟报告能力（Delay Report Capability）。 |

<a id="ga76fb351efe2730311baae1ad6cddbcb1"></a>

### `BT_A2DP_SBC_SINK_EP_DEFAULT`

```c
#define BT_A2DP_SBC_SINK_EP_DEFAULT ( _name)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

展开值（Value）：

```c
static struct bt_a2dp_codec_ie bt_a2dp_ep_cap_ie##_name = {                                \
        .len = BT_A2DP_SBC_IE_LENGTH,                                                      \
        .codec_ie = {A2DP_SBC_SAMP_FREQ_44100 | A2DP_SBC_SAMP_FREQ_48000 |                 \
                             A2DP_SBC_CH_MODE_MONO | A2DP_SBC_CH_MODE_STEREO |             \
                             A2DP_SBC_CH_MODE_JOINT,                                       \
                     A2DP_SBC_BLK_LEN_16 | A2DP_SBC_SUBBAND_8 |                            \
                             A2DP_SBC_ALLOC_MTHD_LOUDNESS,                                 \
                     18U, 35U}};                                                           \
static struct bt_a2dp_ep _name =                                                           \
        BT_A2DP_SINK_EP_INIT(BT_A2DP_SBC, &bt_a2dp_ep_cap_ie##_name, true)
```

定义可用作 bt_a2dp_register_ep 参数的默认 SBC 接收端点（Default Sink Endpoint）。

高级音频分发配置文件（A2DP）规范强制要求支持 SBC；使用 `BT_A2DP_SBC_SINK_EP_DEFAULT` 可以更方便地注册 SBC 端点（Endpoint）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 端点变量名（Endpoint Variable Name）。 |

<a id="ga47dc400bc57140a40975ec1570d79582"></a>

### `BT_A2DP_SBC_SOURCE_EP`

```c
#define BT_A2DP_SBC_SOURCE_EP ( _name, _freq, _ch_mode, _blk_len, _subband, _alloc_mthd, _min_bitpool, _max_bitpool, _delay_report )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

展开值（Value）：

```c
static struct bt_a2dp_codec_ie bt_a2dp_ep_cap_ie##_name = {                                \
        .len = BT_A2DP_SBC_IE_LENGTH,                                                      \
        .codec_ie = {_freq | _ch_mode, _blk_len | _subband | _alloc_mthd, _min_bitpool,    \
                     _max_bitpool}};                                                       \
static struct bt_a2dp_ep _name =                                                           \
        BT_A2DP_SOURCE_EP_INIT(BT_A2DP_SBC, &bt_a2dp_ep_cap_ie##_name, _delay_report)
```

定义可用作 bt_a2dp_register_ep 参数的 SBC 源端点（Source Endpoint）。

高级音频分发配置文件（A2DP）规范强制要求支持 SBC；使用 `BT_A2DP_SBC_SOURCE_EP_DEFAULT` 可以更方便地注册 SBC 端点（Endpoint）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 端点变量名（Endpoint Variable Name）。 |
| `_freq` | SBC 编解码器采样频率（Codec Frequency），例如 `A2DP_SBC_SAMP_FREQ_44100 \| A2DP_SBC_SAMP_FREQ_48000`。 |
| `_ch_mode` | SBC 编解码器通道模式（Codec Channel Mode），例如 `A2DP_SBC_CH_MODE_MONO \| A2DP_SBC_CH_MODE_STEREO`。 |
| `_blk_len` | SBC 编解码器块长度（Codec Block Length），例如 `A2DP_SBC_BLK_LEN_16`。 |
| `_subband` | SBC 编解码器子带（Codec Subband），例如 `A2DP_SBC_SUBBAND_8`。 |
| `_alloc_mthd` | SBC 编解码器分配方法（Codec Allocation Method），例如 `A2DP_SBC_ALLOC_MTHD_LOUDNESS`。 |
| `_min_bitpool` | SBC 编解码器最小比特池（Minimum Bitpool），例如 `18`。 |
| `_max_bitpool` | SBC 编解码器最大比特池（Maximum Bitpool），例如 `35`。 |
| `_delay_report` | 延迟报告能力（Delay Report Capability）。 |

<a id="ga6830ae27e85471935ae604b18cf779e2"></a>

### `BT_A2DP_SBC_SOURCE_EP_DEFAULT`

```c
#define BT_A2DP_SBC_SOURCE_EP_DEFAULT ( _name)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

展开值（Value）：

```c
static struct bt_a2dp_codec_ie bt_a2dp_ep_cap_ie##_name = {                                \
        .len = BT_A2DP_SBC_IE_LENGTH,                                                      \
        .codec_ie = {A2DP_SBC_SAMP_FREQ_44100 | A2DP_SBC_SAMP_FREQ_48000 |                 \
                             A2DP_SBC_CH_MODE_MONO | A2DP_SBC_CH_MODE_STEREO |             \
                             A2DP_SBC_CH_MODE_JOINT,                                       \
                     A2DP_SBC_BLK_LEN_16 | A2DP_SBC_SUBBAND_8 |                            \
                             A2DP_SBC_ALLOC_MTHD_LOUDNESS,                                 \
                     18U, 35U},                                                            \
};                                                                                         \
static struct bt_a2dp_ep _name =                                                           \
        BT_A2DP_SOURCE_EP_INIT(BT_A2DP_SBC, &bt_a2dp_ep_cap_ie##_name, false)
```

定义可用作 bt_a2dp_register_ep 参数的默认 SBC 源端点（Default Source Endpoint）。

高级音频分发配置文件（A2DP）规范强制要求支持 SBC；使用 `BT_A2DP_SBC_SOURCE_EP_DEFAULT` 可以更方便地注册 SBC 端点（Endpoint）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 端点变量名（Endpoint Variable Name）。 |

<a id="ga3c0b5c4dbbea7bc3999a81e2bc579a46"></a>

### `BT_A2DP_SINK_EP_INIT`

```c
#define BT_A2DP_SINK_EP_INIT ( _codec, _capability, _delay_report )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

展开值（Value）：

```c
BT_A2DP_EP_INIT(BT_AVDTP_SINK, _codec, _capability, _delay_report)
```

定义音频接收端点（Audio Sink Endpoint）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_codec` | 枚举（Enumeration）`bt_a2dp_codec_id` 的值。 |
| `_capability` | 编解码器能力（Codec Capability）。 |
| `_delay_report` | 延迟报告能力（Delay Report Capability）。 |

<a id="gab6dc5275f5c5057e2337acc4e31dc2fa"></a>

### `BT_A2DP_SOURCE_EP_INIT`

```c
#define BT_A2DP_SOURCE_EP_INIT ( _codec, _capability, _delay_report )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

展开值（Value）：

```c
BT_A2DP_EP_INIT(BT_AVDTP_SOURCE, _codec, _capability, _delay_report)
```

定义音频源端点（Audio Source Endpoint）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_codec` | 枚举（Enumeration）`bt_a2dp_codec_id` 的值。 |
| `_capability` | 编解码器能力（Codec Capability）。 |
| `_delay_report` | 延迟报告能力（Delay Report Capability）。 |

<a id="gae054d7f9fa92e45c7d40ec0e1d8730ed"></a>

### `bt_a2dp_discover_ep_cb`

```c
typedef uint8_t(* bt_a2dp_discover_ep_cb) (struct bt_a2dp *a2dp, struct bt_a2dp_ep_info *info, struct bt_a2dp_ep **ep)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

发现流端点（Stream Endpoint）时调用。

用户将此类型的函数提供给 `bt_a2dp_discover_param` 对象。每发现一个有效的流端点（Stream Endpoint）后都会调用它。如果没有更多端点，则向用户传入 `NULL`；否则，用户可从 `info` 参数取得有效的端点信息，并可设置 `ep` 参数，以便回调返回后取得端点。函数返回值允许用户控制是否继续获取后续端点。如果当前已找到的端点满足需求、不想再读取更多端点，应返回 `BT_A2DP_DISCOVER_EP_STOP`。否则，返回值表示允许继续进行后续子调用迭代。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a2dp` | A2DP 连接对象（Connection Object），用于标识与被查询远端之间的 A2DP 连接。 |
| `info` | 指向此次回调所报告端点（Endpoint）信息的对象。 |
| `ep` | 如果用户希望使用此次发现的端点（Endpoint），可以设置此参数的值，以取得可供后续其他 A2DP API 使用的端点。如果 `info` 为 `NULL`，即未找到更多端点，此参数也为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：不再需要继续发现下一个端点时返回 `BT_A2DP_DISCOVER_EP_STOP`。原文随后又称，返回 `BT_A2DP_DISCOVER_EP_STOP` 可允许继续发现。译注：原文在此处前后矛盾，两个分支均写为同一常量；保留原文标识符供对照。

<a id="ga7830b874f18be8fc1c62cb9fc69d3c7e"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

辅助枚举（Helper Enum），用作 bt_a2dp_discover_ep_cb 的返回值。

此值通知调用者继续执行后续待处理操作（Pending Actions），或者停止这些操作。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_A2DP_DISCOVER_EP_STOP` |  |
| `BT_A2DP_DISCOVER_EP_CONTINUE` |  |

<a id="gafdb0a28b03d1e11f0595dd3f0b3cb4d6"></a>

### `bt_a2dp_codec_type`

```c
enum bt_a2dp_codec_type
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

编解码器类型（Codec Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_A2DP_SBC` | SBC 编解码器（Codec）。 |
| `BT_A2DP_MPEG1` | MPEG-1 编解码器（Codec）。 |
| `BT_A2DP_MPEG2` | MPEG-2 编解码器（Codec）。 |
| `BT_A2DP_MPEGD` | MPEG-D 编解码器（Codec）。 |
| `BT_A2DP_ATRAC` | ATRAC 编解码器（Codec）。 |
| `BT_A2DP_VENDOR` | 非 A2DP 编解码器（Non-A2DP Codec）。 |

<a id="ga4162a6db1ead67f52f961d660beabb8c"></a>

### `bt_a2dp_err_code`

```c
enum bt_a2dp_err_code
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

A2DP 错误码（Error Code）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_A2DP_INVALID_CODEC_TYPE` | 媒体编解码器类型（Media Codec Type）无效。 |
| `BT_A2DP_NOT_SUPPORTED_CODEC_TYPE` | 不支持该媒体编解码器类型（Media Codec Type）。 |
| `BT_A2DP_INVALID_SAMPLING_FREQUENCY` | 采样频率（Sampling Frequency）无效，或选择了多个值。 |
| `BT_A2DP_NOT_SUPPORTED_SAMPLING_FREQUENCY` | 不支持该采样频率（Sampling Frequency）。 |
| `BT_A2DP_INVALID_CHANNEL_MODE` | 通道模式（Channel Mode）无效，或选择了多个值。 |
| `BT_A2DP_NOT_SUPPORTED_CHANNEL_MODE` | 不支持该通道模式（Channel Mode）。 |
| `BT_A2DP_INVALID_SUBBANDS` | 未选择子带数量（Number of Subbands），或选择了多个值。 |
| `BT_A2DP_NOT_SUPPORTED_SUBBANDS` | 不支持该子带数量（Number of Subbands）。 |
| `BT_A2DP_INVALID_ALLOCATION_METHOD` | 未选择分配方法（Allocation Method），或选择了多个值。 |
| `BT_A2DP_NOT_SUPPORTED_ALLOCATION_METHOD` | 不支持该分配方法（Allocation Method）。 |
| `BT_A2DP_INVALID_MINIMUM_BITPOOL_VALUE` | 最小比特池值（Minimum Bitpool Value）无效。 |
| `BT_A2DP_NOT_SUPPORTED_MINIMUM_BITPOOL_VALUE` | 不支持该最小比特池值（Minimum Bitpool Value）。 |
| `BT_A2DP_INVALID_MAXIMUM_BITPOOL_VALUE` | 最大比特池值（Maximum Bitpool Value）无效。 |
| `BT_A2DP_NOT_SUPPORTED_MAXIMUM_BITPOOL_VALUE` | 不支持该最大比特池值（Maximum Bitpool Value）。 |
| `BT_A2DP_INVALID_LAYER` | 未选择层（Layer），或选择了多个值。 |
| `BT_A2DP_NOT_SUPPORTED_LAYER` | 不支持该层（Layer）。 |
| `BT_A2DP_NOT_SUPPORTED_CRC` | 不支持循环冗余校验（CRC）。 |
| `BT_A2DP_NOT_SUPPORTED_MPF` | 不支持 MPF-2。 |
| `BT_A2DP_NOT_SUPPORTED_VBR` | 不支持可变比特率（VBR）。 |
| `BT_A2DP_INVALID_BIT_RATE` | 未选择比特率（Bit Rate），或选择了多个值。 |
| `BT_A2DP_NOT_SUPPORTED_BIT_RATE` | 不支持该比特率（Bit Rate）。 |
| `BT_A2DP_INVALID_OBJECT_TYPE` | 满足以下情况之一：1）对象类型（Object Type）无效；2）未选择对象类型，或选择了多个值。 |
| `BT_A2DP_NOT_SUPPORTED_OBJECT_TYPE` | 不支持该对象类型（Object Type）。 |
| `BT_A2DP_INVALID_CHANNELS` | 满足以下情况之一：1）通道（Channels）无效；2）未选择通道，或选择了多个值。 |
| `BT_A2DP_NOT_SUPPORTED_CHANNELS` | 不支持该通道（Channels）。 |
| `BT_A2DP_INVALID_VERSION` | 版本（Version）无效。 |
| `BT_A2DP_NOT_SUPPORTED_VERSION` | 不支持该版本（Version）。 |
| `BT_A2DP_NOT_SUPPORTED_MAXIMUM_SUL` | 接收端（SNK）的解码器（Decoder）无法接受此最大 SUL。 |
| `BT_A2DP_INVALID_BLOCK_LENGTH` | 未选择块长度（Block Length），或选择了多个值。 |
| `BT_A2DP_INVALID_CP_TYPE` | 不支持请求的内容保护类型（CP Type）。 |
| `BT_A2DP_INVALID_CP_FORMAT` | 内容保护服务能力（Content Protection Service Capability）／内容保护方案相关数据（Content Protection Scheme Dependent Data）的格式不正确。 |
| `BT_A2DP_INVALID_CODEC_PARAMETER` | 编解码器参数（Codec Parameter）无效。当所用编解码器没有更具体的错误码（Error Code）时使用。 |
| `BT_A2DP_NOT_SUPPORTED_CODEC_PARAMETER` | 不支持该编解码器参数（Codec Parameter）。当所用编解码器没有更具体的错误码（Error Code）时使用。 |
| `BT_A2DP_INVALID_DRC` | 对象类型（Object Type）与动态范围控制（DRC）的组合无效。 |
| `BT_A2DP_NOT_SUPPORTED_DRC` | 不支持动态范围控制（DRC）。 |

<a id="gabc74f6c2a0cf619adbefcf9ffbca1c03"></a>

### `bt_a2dp_connect()`

```c
struct bt_a2dp * bt_a2dp_connect ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

建立 A2DP 连接（Connect）。

应在执行通用访问配置文件（GAP）过程、取得 `conn` 参数后调用此函数。此 API 用于在设备之间建立 A2DP 连接，但只建立音视频分发传输协议（AVDTP）的 L2CAP 信令连接（Signaling Connection）。连接成功后，会调用通过 `bt_a2dp_register_connect_callback` 注册的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向 `bt_conn` 结构体的指针。 |

**返回（Returns）**：返回值（Returns）：成功时返回指向 `struct bt_a2dp` 的指针，出错时返回 `NULL`。

<a id="gabbf0d012860a233ecc84ed333e0da051"></a>

### `bt_a2dp_disconnect()`

```c
int bt_a2dp_disconnect ( struct bt_a2dp * a2dp)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

断开 A2DP 的 L2CAP 连接（Disconnect）。

此函数关闭 AVDTP 的 L2CAP 信令连接（Signaling Connection）。如果已经建立 AVDTP 的 L2CAP 媒体连接（Media Connection），也会将其关闭。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a2dp` | A2DP 实例（Instance）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="ga931234227bc2b9eaed9cd60471ee54db"></a>

### `bt_a2dp_discover()`

```c
int bt_a2dp_discover ( struct bt_a2dp * a2dp, struct bt_a2dp_discover_param * param )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

发现远端端点（Remote Endpoints）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a2dp` | A2DP 实例（Instance）。 |
| `param` | 发现过程（Discovery）使用的参数。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="ga09470ceb08b66661d63c951736f34a5d"></a>

### `bt_a2dp_get_conn()`

```c
struct bt_conn * bt_a2dp_get_conn ( struct bt_a2dp * a2dp)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

获取 A2DP 对应的 ACL 连接（ACL Connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a2dp` | A2DP 实例（Instance）。 |

**返回（Returns）**：返回值（Returns）：与 A2DP 上下文（Context）关联的连接对象（Connection Object）。调用者会取得该对象的一个新引用；使用完毕后，必须通过 `bt_conn_unref()` 释放该引用。

<a id="gafb67c234c9d5748e54d5e67c7b148353"></a>

### `bt_a2dp_get_mtu()`

```c
uint32_t bt_a2dp_get_mtu ( struct bt_a2dp_stream * stream)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

获取流的 L2CAP 最大传输单元（MTU）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象。 |

**返回（Returns）**：返回值（Returns）：最大传输单元（MTU）的值。

<a id="ga4af29d7c162743c00534868ba945b7ec"></a>

### `bt_a2dp_register_cb()`

```c
int bt_a2dp_register_cb ( struct bt_a2dp_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

注册回调（Callback）。

调用 `bt_a2dp_connect` 或由远端设备执行相应操作时，会调用 `cb` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调函数。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="gab1cd7028a41bfdc34ce8cc60aed239de"></a>

### `bt_a2dp_register_ep()`

```c
int bt_a2dp_register_ep ( struct bt_a2dp_ep * ep, uint8_t media_type, uint8_t sep_type )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

端点注册（Endpoint Registration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ep` | 指向 `bt_a2dp_ep` 结构体的指针。 |
| `media_type` | 端点的媒体类型（Media Type），取值为 `bt_avdtp_media_type`。 |
| `sep_type` | 流端点类型（Stream Endpoint Type），取值为 `bt_avdtp_sep_type`。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="ga7999e06ef74be78ec2744bb24ff72912"></a>

### `bt_a2dp_stream_abort()`

```c
int bt_a2dp_stream_abort ( struct bt_a2dp_stream * stream)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

中止 A2DP 流（Stream）。

此函数发送 `AVDTP_ABORT` 命令。中止（Abort）后，流（Stream）失效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="gab8459d999437daa7a107b1bdf4c5ea46"></a>

### `bt_a2dp_stream_cb_register()`

```c
void bt_a2dp_stream_cb_register ( struct bt_a2dp_stream * stream, struct bt_a2dp_stream_ops * ops )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

为流（Stream）注册音频回调（Audio Callbacks）。

为流（Stream）注册音频回调（Audio Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `ops` | 流操作结构体（Stream Operations Structure）。 |

<a id="ga3ff3ca4cd016025f95690e89643f0ff5"></a>

### `bt_a2dp_stream_config()`

```c
int bt_a2dp_stream_config ( struct bt_a2dp * a2dp, struct bt_a2dp_stream * stream, struct bt_a2dp_ep * local_ep, struct bt_a2dp_ep * remote_ep, struct bt_a2dp_codec_cfg * config )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

配置端点（Configure Endpoint）。

可使用 `bt_a2dp_discover` 查找远端端点（Remote Endpoint）。此函数用于配置由 `bt_a2dp_discover` 发现并选中的端点，发送的命令为 `AVDTP_SET_CONFIGURATION`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a2dp` | A2DP 实例（Instance）。 |
| `stream` | 流对象（Stream Object）。 |
| `local_ep` | 已注册、待配置的端点（Endpoint）。 |
| `remote_ep` | 远端端点（Remote Endpoint）。 |
| `config` | 用于配置端点（Endpoint）的配置（Configuration）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="ga16da4e0afe99748ded1fc6db3911c85d"></a>

### `bt_a2dp_stream_create_pdu()`

```c
struct net_buf * bt_a2dp_stream_create_pdu ( struct net_buf_pool * pool, k_timeout_t timeout )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

为 bt_a2dp_stream_send 分配 net_buf。

此函数从指定缓冲池（Buffer Pool）分配缓冲区，为蓝牙 L2CAP 所需的协议头预留足够的头部空间（Headroom），并填充 AVDTP 头部。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 用于分配的缓冲池（Buffer Pool）。 |
| `timeout` | 获取缓冲区的非负等待时长，或特殊值 K_NO_WAIT、K_FOREVER 之一。 |

**返回（Returns）**：返回值（Returns）：新分配的 `net_buf`。

<a id="gaa332aeced3d91fc9178bc9dcc0d10564"></a>

### `bt_a2dp_stream_delay_report()`

```c
int bt_a2dp_stream_delay_report ( struct bt_a2dp_stream * stream, uint16_t delay )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

发送延迟报告（Delay Report）。

只有 A2DP 接收端（Sink）可以调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象。 |
| `delay` | 数值的单位为十分之一毫秒（1/10 Millisecond）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="gaf47e0028176494f5353ee00261ffa49a"></a>

### `bt_a2dp_stream_establish()`

```c
int bt_a2dp_stream_establish ( struct bt_a2dp_stream * stream)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

建立 A2DP 流（Stream）。

此函数发送 `AVDTP_OPEN` 命令，并创建 L2CAP 通道（Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="ga68f74181bba610c7fd158558afdcbd86"></a>

### `bt_a2dp_stream_get_config()`

```c
int bt_a2dp_stream_get_config ( struct bt_a2dp_stream * stream)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

获取流的配置（Stream Configuration）。

此函数发送 `AVDTP_GET_CONFIGURATION` 命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="ga70fc5f43265a4c407a847c4205cd7697"></a>

### `bt_a2dp_stream_reconfig()`

```c
int bt_a2dp_stream_reconfig ( struct bt_a2dp_stream * stream, struct bt_a2dp_codec_cfg * config )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

重新配置 A2DP 流（Stream）。

此函数发送 `AVDTP_RECONFIGURE` 命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象。 |
| `config` | 用于配置流（Stream）的配置（Configuration）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="ga194e7ec86715cf9007de30f6492e4f58"></a>

### `bt_a2dp_stream_release()`

```c
int bt_a2dp_stream_release ( struct bt_a2dp_stream * stream)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

释放 A2DP 流（Stream）。

此函数发送 `AVDTP_CLOSE` 命令，并释放 L2CAP 通道（Channel）。释放后，流（Stream）失效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="gae8591dc8ef0b1c1e2af9ff5fb0cab681"></a>

### `bt_a2dp_stream_send()`

```c
int bt_a2dp_stream_send ( struct bt_a2dp_stream * stream, struct net_buf * buf, uint16_t seq_num, uint32_t ts )
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

发送 A2DP 媒体数据（Media Data）。

只有 A2DP 发送端（Source）可以调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象。 |
| `buf` | 数据（Data）。 |
| `seq_num` | 序列号（Sequence Number）。 |
| `ts` | 时间戳（Timestamp）。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="ga368403c64581b761099631280014d877"></a>

### `bt_a2dp_stream_start()`

```c
int bt_a2dp_stream_start ( struct bt_a2dp_stream * stream)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

启动 A2DP 流（Stream）。

此函数发送 `AVDTP_START` 命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。

<a id="gaf22030f4edd5401b2d5359bcb0590145"></a>

### `bt_a2dp_stream_suspend()`

```c
int bt_a2dp_stream_suspend ( struct bt_a2dp_stream * stream)
```

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

暂停 A2DP 流（Stream）。

此函数发送 `AVDTP_SUSPEND` 命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象。 |

**返回（Returns）**：返回值（Returns）：成功时返回 `0`，出错时返回错误码（Error Code）。


## 2.7\_原页交叉引用（Cross References）

- [bt_a2dp_codec_ie](../bluetooth_classic_model_reference/P004_bt_a2dp_codec_ie_结构体.md)
- [bt_a2dp_codec_cfg](../bluetooth_classic_model_reference/P003_bt_a2dp_codec_cfg_结构体.md)
- [bt_a2dp_ep](../bluetooth_classic_model_reference/P007_bt_a2dp_ep_结构体.md)
- [bt_a2dp_ep_info](../bluetooth_classic_model_reference/P008_bt_a2dp_ep_info_结构体.md)
- [bt_a2dp_discover_param](../bluetooth_classic_model_reference/P006_bt_a2dp_discover_param_结构体.md)
- [bt_a2dp_cb](../bluetooth_classic_model_reference/P002_bt_a2dp_cb_结构体.md)
- [bt_a2dp_stream](../bluetooth_classic_model_reference/P009_bt_a2dp_stream_结构体.md)
- [bt_a2dp_stream_ops](../bluetooth_classic_model_reference/P010_bt_a2dp_stream_ops_结构体.md)
- [bt_a2dp](../bluetooth_classic_model_reference/P001_bt_a2dp_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [zephyr/bluetooth/classic/a2dp.h](../api_file_display_chat_reference/P001_zephyr__bluetooth__classic__a2dp.h_文件参考.md)
- [BT_AVDTP_AUDIO](../api_file_audio_test_reference/P003_zephyr__bluetooth__classic__avdtp.h_文件参考.md#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58)
- [A2DP_SBC_CH_MODE_JOINT](../api_file_mesh_interrupt_reference/P001_zephyr__bluetooth__classic__a2dp_codec_sbc.h_文件参考.md#afcf64fa599e4d820dccdf40990f5ba39)
- [A2DP_SBC_BLK_LEN_16](../api_file_mesh_interrupt_reference/P001_zephyr__bluetooth__classic__a2dp_codec_sbc.h_文件参考.md#a1cb9425713c325442652fb406557e52a)
- [A2DP_SBC_SUBBAND_8](../api_file_mesh_interrupt_reference/P001_zephyr__bluetooth__classic__a2dp_codec_sbc.h_文件参考.md#a6b4bd1ef891c14c4f863c9623dcb63f7)
- [A2DP_SBC_ALLOC_MTHD_LOUDNESS](../api_file_mesh_interrupt_reference/P001_zephyr__bluetooth__classic__a2dp_codec_sbc.h_文件参考.md#a27d905ddf0fdb3dea4d3c12dd3ca33fe)
- [A2DP_SBC_SAMP_FREQ_44100](../api_file_mesh_interrupt_reference/P001_zephyr__bluetooth__classic__a2dp_codec_sbc.h_文件参考.md#a57d7b85560b36603651fae6c055c32c6)
- [A2DP_SBC_SAMP_FREQ_48000](../api_file_mesh_interrupt_reference/P001_zephyr__bluetooth__classic__a2dp_codec_sbc.h_文件参考.md#a0ebafbef2cddd4b6c7c7990ca77db0f9)
- [A2DP_SBC_CH_MODE_MONO](../api_file_mesh_interrupt_reference/P001_zephyr__bluetooth__classic__a2dp_codec_sbc.h_文件参考.md#aa9b58737fa1561b684a20980ea0b6feb)
- [A2DP_SBC_CH_MODE_STEREO](../api_file_mesh_interrupt_reference/P001_zephyr__bluetooth__classic__a2dp_codec_sbc.h_文件参考.md#a5557b7681eeaeb6f6fc78b3be84fc5cf)
- [BT_AVDTP_SINK](../api_file_audio_test_reference/P003_zephyr__bluetooth__classic__avdtp.h_文件参考.md#a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9)
- [BT_AVDTP_SOURCE](../api_file_audio_test_reference/P003_zephyr__bluetooth__classic__avdtp.h_文件参考.md#a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f)
- [bt_conn_unref()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b18c6b22a9f02be0d7d078b2ce51ff6)
- [bt_avdtp_media_type](../api_file_audio_test_reference/P003_zephyr__bluetooth__classic__avdtp.h_文件参考.md#a6e9f13217ede2687e206b6a8cbd9137f)
- [bt_avdtp_sep_type](../api_file_audio_test_reference/P003_zephyr__bluetooth__classic__avdtp.h_文件参考.md#a28b828df32df5a40e8487dc4dee78757)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aavdtp_8h_html_a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58"></a>
<a id="agroup__bt__a2dp_html_gaf83aa927ac312cfc8577056afffeae56"></a>
<a id="astructbt__a2dp__codec__ie_html"></a>
<a id="aa2dp__codec__sbc_8h_html_a1cb9425713c325442652fb406557e52a"></a>
<a id="aa2dp__codec__sbc_8h_html_a27d905ddf0fdb3dea4d3c12dd3ca33fe"></a>
<a id="aa2dp__codec__sbc_8h_html_a6b4bd1ef891c14c4f863c9623dcb63f7"></a>
<a id="aa2dp__codec__sbc_8h_html_afcf64fa599e4d820dccdf40990f5ba39"></a>
<a id="agroup__bt__a2dp_html_ggafdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00"></a>
<a id="aa2dp__codec__sbc_8h_html_a0ebafbef2cddd4b6c7c7990ca77db0f9"></a>
<a id="aa2dp__codec__sbc_8h_html_a5557b7681eeaeb6f6fc78b3be84fc5cf"></a>
<a id="aa2dp__codec__sbc_8h_html_a57d7b85560b36603651fae6c055c32c6"></a>
<a id="aa2dp__codec__sbc_8h_html_aa9b58737fa1561b684a20980ea0b6feb"></a>
<a id="aavdtp_8h_html_a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9"></a>
<a id="agroup__bt__a2dp_html_ga3a2b2021adcd90c8c5adbbeb1441826d"></a>
<a id="aavdtp_8h_html_a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga7830b874f18be8fc1c62cb9fc69d3c7eab55d2d864da292240e19ee251de832f2"></a>
<a id="gga7830b874f18be8fc1c62cb9fc69d3c7eae38f6b8bd78c8a975d0f59c74fe9d367"></a>
<a id="ggafdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00"></a>
<a id="ggafdb0a28b03d1e11f0595dd3f0b3cb4d6a1f1840d90c1d5ee28b650978bf012497"></a>
<a id="ggafdb0a28b03d1e11f0595dd3f0b3cb4d6aefe729d388e0a3d8bb7759b986123c88"></a>
<a id="ggafdb0a28b03d1e11f0595dd3f0b3cb4d6ad90f96068afbe94c6338d4906b07341b"></a>
<a id="ggafdb0a28b03d1e11f0595dd3f0b3cb4d6a8b969e35e28d18cf05802e1381995e83"></a>
<a id="ggafdb0a28b03d1e11f0595dd3f0b3cb4d6ad3c292360558ea515a84d570c43c1701"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca1718e53b8632688eb1aa9253248e7591"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8cabda2c831224e1c994b5c67ea9fe7be7f"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca68471cd1037db6687bc1f60cf500681c"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca499c532b0069432802cbe72bc33e5a76"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca6222f61712e16dbd0b56fda692844396"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca8e62e8df4d9e2a5389ad1620de7af755"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca8e06f678574f38b9538f8c45622cee3f"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca2a20d81b47a5b3119988c3702ba1e84d"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8caf13a2a05042cb4ee373017fabd92303a"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca81723b89ccf0d40db2a2edacd2cbaca8"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8cad81217701b215d26e65c220c83ed4a02"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8cacd474a29c941a1b1ad164a63d07763d3"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca71dfaa290af68147e83541e37d59d5cf"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca9fe3d3aea48e5c5122ce058e8918133f"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8caf2bd03a778271c6310fb51d3dccccb41"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca48b381cca4ddd1ccb26037e84b0bea9e"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca4e204c6ea5acfe20be37da6fca38eaec"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca95a7b280dbdb757fab3b8b2077120d8f"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca92d1fb010cc69e27ec988de69c9bbd51"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8cadb4d2cc815b2c01e6f7e2666305d4476"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8caf86c457a7e016f440089469c9f442ad1"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca3896984afb4b5d164503bd53f0d4e429"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca7b5bafd55d8020029e429b142c572615"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca182de8e823efe2f6575a900a567b3483"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca3619a0a5c74de24b7dd8bd79b99ca91a"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca47dbe86cbbd2859243995d1d39c46d8d"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca1d4c42781c74ebda2b084fe609ac284c"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8cafdf002100cc0d7d1f07cf833ed331f2b"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8caebf8a58263b517b79947e9cc8a9678c3"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8caab4c2af80c9588443a297e120f8ee611"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca0554b3ef221c98b5cb4580ae049a6e63"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca9aa4fc1c6f365b686ab4dc3875b93396"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca3c801158e7ed2623c2d2930ca91b94a9"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8cafd0982a65fc5657b13f35e0761425d96"></a>
<a id="gga4162a6db1ead67f52f961d660beabb8ca198bd8a559eca40d9d95f6edf8a703fd"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_BSD 套接字兼容 API（BSD Sockets compatible API）.md) · [返回大纲](大纲.md) · [下一章](P003_分配编号（Assigned Numbers）.md)
