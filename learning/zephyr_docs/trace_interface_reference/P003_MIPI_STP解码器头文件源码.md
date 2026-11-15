---
id: learning.zephyr-docs.trace-interface-reference.page-3
title: MIPI_STP解码器头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mipi__stp__decoder_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_MIPI\_STP解码器头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mipi__stp__decoder_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](../observability/P046_MIPI_STP解码头文件.md)和[公共接口](../observability/P027_MIPI_STP解码接口.md)；访问语义和生命周期见本页译注。

## 3.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00023"></a>
<a id="foldopen00046"></a>
<a id="foldopen00064"></a>
<a id="foldopen00101"></a>
<a id="agroup__mipi__stp__decoder__apis_html_ga0e1be10f234d72e81b48d21bfe8a42f8"></a>
<a id="agroup__mipi__stp__decoder__apis_html_ga4a67705c849793f02c7ae409434b4e79"></a>
<a id="agroup__mipi__stp__decoder__apis_html_ga520104e814b15cce22ec74a4e827a5b9"></a>
<a id="agroup__mipi__stp__decoder__apis_html_ga6e1f4b66b14ab44e549292f97046a50d"></a>
<a id="agroup__mipi__stp__decoder__apis_html_ga8c6fdc2927d954291a12e4c31ad8abe2"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da062e36cbfa898f544fea1e5ddfed205e"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da0aa61c6c20ce10ac93ab5d0903af06e5"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da2007260749b9d89c598a528cc8468ab5"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da2697b0f2083731fb03fd197d2905dd37"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da38ae6c0f7c2f37cdb7068fc6dabb2184"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da43d3753e29c66c1a5c1b9da0b55cd36e"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da4b94577fa87699f6aca63ab9062e42b1"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da63596fdd07425a6a1a5342528ac22100"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da6c85b02588c7c1bb07657b4b316bf360"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da6efb90a9074b3ed4d63be65e4245345a"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da7082b6a478ef3ce82bd97b2aa29bf0ef"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da7be5f983d725712fd258d2368d4689c4"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50da853c25efa06fc63571ac14c5696838b7"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50daa0f541093b78f948a6770f16e362560a"></a>
<a id="agroup__mipi__stp__decoder__apis_html_gga6e1f4b66b14ab44e549292f97046a50daf8b791424b5f0e281c64e2258b19129f"></a>
<a id="akernel_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructmipi__stp__decoder__config_html"></a>
<a id="astructmipi__stp__decoder__config_html_a519473c106e406e453c104790045d404"></a>
<a id="astructmipi__stp__decoder__config_html_abf1a03280ec82f3a2db7aef25c6522ac"></a>
<a id="aunionmipi__stp__decoder__data_html"></a>
<a id="aunionmipi__stp__decoder__data_html_a1cb5f92d1d0976f1ec047e7398e6d95d"></a>
<a id="aunionmipi__stp__decoder__data_html_a3b3cae98d63ceda950e88690da282966"></a>
<a id="aunionmipi__stp__decoder__data_html_a3c7d85bc475b27f570b9059745d7d11f"></a>
<a id="aunionmipi__stp__decoder__data_html_a3dc68ca2196c807965071d754c139655"></a>
<a id="aunionmipi__stp__decoder__data_html_a70db937ada38cb0f97cd45fa78bd9466"></a>
<a id="aunionmipi__stp__decoder__data_html_ace873d9e7d38a5f39338618b4d74cdf4"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Nordic Semiconductor ASA.
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00007"></a>#ifndef ZEPHYR_INCLUDE_DEBUG_MIPI_STP_DECODER_H__
<a id="l00008"></a>#define ZEPHYR_INCLUDE_DEBUG_MIPI_STP_DECODER_H__
<a id="l00009"></a>
<a id="l00010"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00011"></a>
<a id="l00012"></a>#ifdef __cplusplus
<a id="l00013"></a>extern "C" {
<a id="l00014"></a>#endif
<a id="l00015"></a>
<a id="l00021"></a>
<a id="l00023"></a>enum mipi_stp_decoder_ctrl_type {
<a id="l00024"></a>        STP_DATA4 = 1,
<a id="l00025"></a>        STP_DATA8 = 2,
<a id="l00026"></a>        STP_DATA16 = 4,
<a id="l00027"></a>        STP_DATA32 = 8,
<a id="l00028"></a>        STP_DATA64 = 16,
<a id="l00029"></a>        STP_DECODER_NULL = 128,
<a id="l00030"></a>        STP_DECODER_MAJOR,
<a id="l00031"></a>        STP_DECODER_MERROR,
<a id="l00032"></a>        STP_DECODER_CHANNEL,
<a id="l00033"></a>        STP_DECODER_VERSION,
<a id="l00034"></a>        STP_DECODER_FREQ,
<a id="l00035"></a>        STP_DECODER_GERROR,
<a id="l00036"></a>        STP_DECODER_FLAG,
<a id="l00037"></a>        STP_DECODER_ASYNC,
<a id="l00038"></a>        STP_DECODER_NOT_SUPPORTED,
<a id="l00039"></a>};
<a id="l00040"></a>
<a id="l00046"></a>#define STP_DECODER_TYPE2STR(_type) \
<a id="l00047"></a>        _type == STP_DATA4 ? "DATA4" : (\
<a id="l00048"></a>        _type == STP_DATA8 ? "DATA8" : (\
<a id="l00049"></a>        _type == STP_DATA16 ? "DATA16" : (\
<a id="l00050"></a>        _type == STP_DATA32 ? "DATA32" : (\
<a id="l00051"></a>        _type == STP_DATA64 ? "DATA64" : (\
<a id="l00052"></a>        _type == STP_DECODER_NULL ? "NULL" : (\
<a id="l00053"></a>        _type == STP_DECODER_MAJOR ? "MAJOR" : (\
<a id="l00054"></a>        _type == STP_DECODER_MERROR ? "MERROR" : (\
<a id="l00055"></a>        _type == STP_DECODER_CHANNEL ? "CHANNEL" : (\
<a id="l00056"></a>        _type == STP_DECODER_VERSION ? "VERSION" : (\
<a id="l00057"></a>        _type == STP_DECODER_FREQ ? "FREQ" : (\
<a id="l00058"></a>        _type == STP_DECODER_GERROR ? "GERROR" : (\
<a id="l00059"></a>        _type == STP_DECODER_FLAG ? "FLAG" : (\
<a id="l00060"></a>        _type == STP_DECODER_ASYNC ? "ASYNC" : (\
<a id="l00061"></a>        "Unknown"))))))))))))))
<a id="l00062"></a>
<a id="l00064"></a>union mipi_stp_decoder_data {
<a id="l00066"></a>        uint16_t id;
<a id="l00067"></a>
<a id="l00069"></a>        uint64_t freq;
<a id="l00070"></a>
<a id="l00072"></a>        uint32_t ver;
<a id="l00073"></a>
<a id="l00075"></a>        uint32_t err;
<a id="l00076"></a>
<a id="l00078"></a>        uint32_t dummy;
<a id="l00079"></a>
<a id="l00081"></a>        uint64_t data;
<a id="l00082"></a>};
<a id="l00083"></a>
<a id="l00096"></a>typedef bool (*mipi_stp_decoder_cb)(enum mipi_stp_decoder_ctrl_type type,
<a id="l00097"></a>                                    union mipi_stp_decoder_data data,
<a id="l00098"></a>                                    uint64_t *ts, bool marked);
<a id="l00099"></a>
<a id="l00101"></a>struct mipi_stp_decoder_config {
<a id="l00103"></a>        bool start_out_of_sync;
<a id="l00104"></a>
<a id="l00106"></a>        mipi_stp_decoder_cb cb;
<a id="l00107"></a>};
<a id="l00108"></a>
<a id="l00116"></a>int mipi_stp_decoder_init(const struct mipi_stp_decoder_config *config);
<a id="l00117"></a>
<a id="l00128"></a>int mipi_stp_decoder_decode(const uint8_t *data, size_t len);
<a id="l00129"></a>
<a id="l00136"></a>void mipi_stp_decoder_sync_loss(void);
<a id="l00137"></a>
<a id="l00141"></a>
<a id="l00142"></a>#ifdef __cplusplus
<a id="l00143"></a>}
<a id="l00144"></a>#endif
<a id="l00145"></a>
<a id="l00146"></a>#endif /* ZEPHYR_INCLUDE_DEBUG_MIPI_STP_DECODER_H__ */
</code></pre>

## 3.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2024 Nordic Semiconductor ASA.；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_DEBUG_MIPI_STP_DECODER_H__头文件包含保护结束。

## 3.3\_原页符号提示（Symbol Descriptions）

### `mipi_stp_decoder_sync_loss`

```c
void mipi_stp_decoder_sync_loss(void)
```

通知同步丢失（Synchronization Loss）。

符号定位：[mipi_stp_decoder_sync_loss](../observability/P027_MIPI_STP解码接口.md#ga0e1be10f234d72e81b48d21bfe8a42f8)。

### `mipi_stp_decoder_init`

```c
int mipi_stp_decoder_init(const struct mipi_stp_decoder_config *config)
```

初始化解码器（Decoder）。

符号定位：[mipi_stp_decoder_init](../observability/P027_MIPI_STP解码接口.md#ga4a67705c849793f02c7ae409434b4e79)。

### `mipi_stp_decoder_decode`

```c
int mipi_stp_decoder_decode(const uint8_t *data, size_t len)
```

解码STPv2数据流（Stream）。

符号定位：[mipi_stp_decoder_decode](../observability/P027_MIPI_STP解码接口.md#ga520104e814b15cce22ec74a4e827a5b9)。

### `mipi_stp_decoder_ctrl_type`

```c
mipi_stp_decoder_ctrl_type
```

STPv2操作码（Opcodes）。

定义位置（Definition）：mipi_stp_decoder.h:23。

符号定位：[mipi_stp_decoder_ctrl_type](../observability/P027_MIPI_STP解码接口.md#ga6e1f4b66b14ab44e549292f97046a50d)。

### `mipi_stp_decoder_cb`

```c
bool(* mipi_stp_decoder_cb)(enum mipi_stp_decoder_ctrl_type type, union mipi_stp_decoder_data data, uint64_t *ts, bool marked)
```

回调函数签名（Callback Signature）。

定义位置（Definition）：mipi_stp_decoder.h:96。

符号定位：[mipi_stp_decoder_cb](../observability/P027_MIPI_STP解码接口.md#ga8c6fdc2927d954291a12e4c31ad8abe2)。

### `STP_DECODER_NULL`

```c
@ STP_DECODER_NULL
```

定义位置（Definition）：mipi_stp_decoder.h:29。

符号定位：[STP_DECODER_NULL](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da062e36cbfa898f544fea1e5ddfed205e)。

### `STP_DATA4`

```c
@ STP_DATA4
```

定义位置（Definition）：mipi_stp_decoder.h:24。

符号定位：[STP_DATA4](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da0aa61c6c20ce10ac93ab5d0903af06e5)。

### `STP_DECODER_FLAG`

```c
@ STP_DECODER_FLAG
```

定义位置（Definition）：mipi_stp_decoder.h:36。

符号定位：[STP_DECODER_FLAG](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da2007260749b9d89c598a528cc8468ab5)。

### `STP_DECODER_FREQ`

```c
@ STP_DECODER_FREQ
```

定义位置（Definition）：mipi_stp_decoder.h:34。

符号定位：[STP_DECODER_FREQ](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da2697b0f2083731fb03fd197d2905dd37)。

### `STP_DATA16`

```c
@ STP_DATA16
```

定义位置（Definition）：mipi_stp_decoder.h:26。

符号定位：[STP_DATA16](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da38ae6c0f7c2f37cdb7068fc6dabb2184)。

### `STP_DATA32`

```c
@ STP_DATA32
```

定义位置（Definition）：mipi_stp_decoder.h:27。

符号定位：[STP_DATA32](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da43d3753e29c66c1a5c1b9da0b55cd36e)。

### `STP_DECODER_MAJOR`

```c
@ STP_DECODER_MAJOR
```

定义位置（Definition）：mipi_stp_decoder.h:30。

符号定位：[STP_DECODER_MAJOR](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da4b94577fa87699f6aca63ab9062e42b1)。

### `STP_DATA8`

```c
@ STP_DATA8
```

定义位置（Definition）：mipi_stp_decoder.h:25。

符号定位：[STP_DATA8](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da63596fdd07425a6a1a5342528ac22100)。

### `STP_DECODER_CHANNEL`

```c
@ STP_DECODER_CHANNEL
```

定义位置（Definition）：mipi_stp_decoder.h:32。

符号定位：[STP_DECODER_CHANNEL](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da6c85b02588c7c1bb07657b4b316bf360)。

### `STP_DATA64`

```c
@ STP_DATA64
```

定义位置（Definition）：mipi_stp_decoder.h:28。

符号定位：[STP_DATA64](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da6efb90a9074b3ed4d63be65e4245345a)。

### `STP_DECODER_ASYNC`

```c
@ STP_DECODER_ASYNC
```

定义位置（Definition）：mipi_stp_decoder.h:37。

符号定位：[STP_DECODER_ASYNC](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da7082b6a478ef3ce82bd97b2aa29bf0ef)。

### `STP_DECODER_NOT_SUPPORTED`

```c
@ STP_DECODER_NOT_SUPPORTED
```

定义位置（Definition）：mipi_stp_decoder.h:38。

符号定位：[STP_DECODER_NOT_SUPPORTED](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da7be5f983d725712fd258d2368d4689c4)。

### `STP_DECODER_GERROR`

```c
@ STP_DECODER_GERROR
```

定义位置（Definition）：mipi_stp_decoder.h:35。

符号定位：[STP_DECODER_GERROR](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da853c25efa06fc63571ac14c5696838b7)。

### `STP_DECODER_MERROR`

```c
@ STP_DECODER_MERROR
```

定义位置（Definition）：mipi_stp_decoder.h:31。

符号定位：[STP_DECODER_MERROR](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50daa0f541093b78f948a6770f16e362560a)。

### `STP_DECODER_VERSION`

```c
@ STP_DECODER_VERSION
```

定义位置（Definition）：mipi_stp_decoder.h:33。

符号定位：[STP_DECODER_VERSION](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50daf8b791424b5f0e281c64e2258b19129f)。

### `kernel.h`

公共内核 API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `bool`

```c
#define bool
```

定义位置（Definition）：stdbool.h:13。

符号定位：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint64_t`

```c
__UINT64_TYPE__ uint64_t
```

定义位置（Definition）：stdint.h:91。

符号定位：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `mipi_stp_decoder_config`

解码器配置（Decoder Configuration）。

定义位置（Definition）：mipi_stp_decoder.h:101。

符号定位：[mipi_stp_decoder_config](../observability/P028_MIPI_STP解码配置.md)。

### `mipi_stp_decoder_config::cb`

```c
mipi_stp_decoder_cb cb
```

回调（Callback）。

定义位置（Definition）：mipi_stp_decoder.h:106。

符号定位：[mipi_stp_decoder_config::cb](../observability/P028_MIPI_STP解码配置.md#a519473c106e406e453c104790045d404)。

### `mipi_stp_decoder_config::start_out_of_sync`

```c
bool start_out_of_sync
```

表示解码器从失同步状态（Out-of-sync State）启动。

定义位置（Definition）：mipi_stp_decoder.h:103。

符号定位：[mipi_stp_decoder_config::start_out_of_sync](../observability/P028_MIPI_STP解码配置.md#abf1a03280ec82f3a2db7aef25c6522ac)。

### `mipi_stp_decoder_data`

保存与给定STP操作码关联数据的联合体（Union）。

定义位置（Definition）：mipi_stp_decoder.h:64。

符号定位：[mipi_stp_decoder_data](../observability/P029_MIPI_STP解码数据.md)。

### `mipi_stp_decoder_data::data`

```c
uint64_t data
```

数据（Data）。

定义位置（Definition）：mipi_stp_decoder.h:81。

符号定位：[mipi_stp_decoder_data::data](../observability/P029_MIPI_STP解码数据.md#a1cb5f92d1d0976f1ec047e7398e6d95d)。

### `mipi_stp_decoder_data::freq`

```c
uint64_t freq
```

频率（Frequency）。

定义位置（Definition）：mipi_stp_decoder.h:69。

符号定位：[mipi_stp_decoder_data::freq](../observability/P029_MIPI_STP解码数据.md#a3b3cae98d63ceda950e88690da282966)。

### `mipi_stp_decoder_data::id`

```c
uint16_t id
```

标识符（ID），用于Major和通道（Channel）。

定义位置（Definition）：mipi_stp_decoder.h:66。

符号定位：[mipi_stp_decoder_data::id](../observability/P029_MIPI_STP解码数据.md#a3c7d85bc475b27f570b9059745d7d11f)。

### `mipi_stp_decoder_data::ver`

```c
uint32_t ver
```

版本（Version）。

定义位置（Definition）：mipi_stp_decoder.h:72。

符号定位：[mipi_stp_decoder_data::ver](../observability/P029_MIPI_STP解码数据.md#a3dc68ca2196c807965071d754c139655)。

### `mipi_stp_decoder_data::dummy`

```c
uint32_t dummy
```

占位项（Dummy）。

定义位置（Definition）：mipi_stp_decoder.h:78。

符号定位：[mipi_stp_decoder_data::dummy](../observability/P029_MIPI_STP解码数据.md#a70db937ada38cb0f97cd45fa78bd9466)。

### `mipi_stp_decoder_data::err`

```c
uint32_t err
```

错误码（Error Code）。

定义位置（Definition）：mipi_stp_decoder.h:75。

符号定位：[mipi_stp_decoder_data::err](../observability/P029_MIPI_STP解码数据.md#ace873d9e7d38a5f39338618b4d74cdf4)。

## 3.4\_源码跟踪译注

> 译注——此头文件描述MIPI系统跟踪协议第2版（MIPI System Trace Protocol v2，STPv2）的流解码接口。操作码（Opcode）、数据联合体和回调声明保持原样；宏生成的DATA4、MAJOR等字符串属于程序输出，不用中文替换。

> 译注——STP_DATA4、STP_DATA8、STP_DATA16、STP_DATA32、STP_DATA64的枚举值依次为1、2、4、8、16；不能把枚举整数直接当作数据位宽。类型名中的数字才标识相应数据位数。

> 译注——官方回调约定在中断锁定（Interrupts Locked）状态调用。返回false表示数据指示失去同步，解码状态机将转入重新同步；时间戳指针为NULL时表示本元素没有时间戳。调用方处理应遵守这个上下文和参数有效期约定。

> 译注——当前实现使用文件级状态变量，并非每次decode都从头解析。分段输入会保留尚未完成的操作码、数据和时间戳状态；不能把同一实例当成多个互不相关数据流的并行解码器。

> 译注——失同步通知（Synchronization Loss）使解码器寻找ASYNC标记，在找到前丢弃数据。原始接口声明成功和失败返回值，而当前decode末尾返回0；返回0不能单独证明流中没有失同步或全部日志都已经恢复。

头文件定位：[include/zephyr/debug/mipi_stp_decoder.h](../../../include/zephyr/debug/mipi_stp_decoder.h)，关联实现／接口：[subsys/debug/mipi_stp_decoder.c](../../../subsys/debug/mipi_stp_decoder.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/debug/mipi_stp_decoder.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/mipi_stp_decoder.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](../observability/P046_MIPI_STP解码头文件.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mipi_stp_decoder_ctrl_type](../observability/P027_MIPI_STP解码接口.md#ga6e1f4b66b14ab44e549292f97046a50d)
- [STP_DATA4](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da0aa61c6c20ce10ac93ab5d0903af06e5)
- [STP_DATA8](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da63596fdd07425a6a1a5342528ac22100)
- [STP_DATA16](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da38ae6c0f7c2f37cdb7068fc6dabb2184)
- [STP_DATA32](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da43d3753e29c66c1a5c1b9da0b55cd36e)
- [STP_DATA64](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da6efb90a9074b3ed4d63be65e4245345a)
- [STP_DECODER_NULL](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da062e36cbfa898f544fea1e5ddfed205e)
- [STP_DECODER_MAJOR](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da4b94577fa87699f6aca63ab9062e42b1)
- [STP_DECODER_MERROR](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50daa0f541093b78f948a6770f16e362560a)
- [STP_DECODER_CHANNEL](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da6c85b02588c7c1bb07657b4b316bf360)
- [STP_DECODER_VERSION](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50daf8b791424b5f0e281c64e2258b19129f)
- [STP_DECODER_FREQ](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da2697b0f2083731fb03fd197d2905dd37)
- [STP_DECODER_GERROR](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da853c25efa06fc63571ac14c5696838b7)
- [STP_DECODER_FLAG](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da2007260749b9d89c598a528cc8468ab5)
- [STP_DECODER_ASYNC](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da7082b6a478ef3ce82bd97b2aa29bf0ef)
- [STP_DECODER_NOT_SUPPORTED](../observability/P027_MIPI_STP解码接口.md#gga6e1f4b66b14ab44e549292f97046a50da7be5f983d725712fd258d2368d4689c4)
- [mipi_stp_decoder_data](../observability/P029_MIPI_STP解码数据.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [id](../observability/P029_MIPI_STP解码数据.md#a3c7d85bc475b27f570b9059745d7d11f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [freq](../observability/P029_MIPI_STP解码数据.md#a3b3cae98d63ceda950e88690da282966)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [ver](../observability/P029_MIPI_STP解码数据.md#a3dc68ca2196c807965071d754c139655)
- [err](../observability/P029_MIPI_STP解码数据.md#ace873d9e7d38a5f39338618b4d74cdf4)
- [dummy](../observability/P029_MIPI_STP解码数据.md#a70db937ada38cb0f97cd45fa78bd9466)
- [data](../observability/P029_MIPI_STP解码数据.md#a1cb5f92d1d0976f1ec047e7398e6d95d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mipi_stp_decoder_cb](../observability/P027_MIPI_STP解码接口.md#ga8c6fdc2927d954291a12e4c31ad8abe2)
- [mipi_stp_decoder_config](../observability/P028_MIPI_STP解码配置.md)
- [start_out_of_sync](../observability/P028_MIPI_STP解码配置.md#abf1a03280ec82f3a2db7aef25c6522ac)
- [cb](../observability/P028_MIPI_STP解码配置.md#a519473c106e406e453c104790045d404)
- [mipi_stp_decoder_init](../observability/P027_MIPI_STP解码接口.md#ga4a67705c849793f02c7ae409434b4e79)
- [mipi_stp_decoder_decode](../observability/P027_MIPI_STP解码接口.md#ga520104e814b15cce22ec74a4e827a5b9)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mipi_stp_decoder_sync_loss](../observability/P027_MIPI_STP解码接口.md#ga0e1be10f234d72e81b48d21bfe8a42f8)

---

[上一章](P002_STMESP底层接口.md) · [返回大纲](大纲.md)
