---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-5
title: bt_ascs_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ascs__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_bt\_ascs\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ascs__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

音频流控制服务（Audio Stream Control Service，ASCS）回调结构体。

```c
#include <zephyr/bluetooth/audio/ascs.h>
```

<a id="details"></a>

音频流控制服务（Audio Stream Control Service，ASCS）回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_aa259b32e5a731a20e23659d88143ec6e"></a>

```c
int(* config )(struct bt_conn *conn, const struct bt_bap_ep *ep, enum bt_audio_dir dir, const struct bt_audio_codec_cfg *codec_cfg, struct bt_bap_stream **stream, struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[config](#aa259b32e5a731a20e23659d88143ec6e)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_bap_ep](P024_bt_bap_ep_结构体.md)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_codec_cfg](P008_bt_audio_codec_cfg_结构体.md)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_qos_cfg_pref](P028_bt_bap_qos_cfg_pref_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

端点配置请求回调（Endpoint Configuration Request Callback）。

<a id="r_a6eb6e4e35f9373cbcceb6e93e29b5ef6"></a>

```c
int(* reconfig )(struct bt_bap_stream *stream, enum bt_audio_dir dir, const struct bt_audio_codec_cfg *codec_cfg, struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[reconfig](#a6eb6e4e35f9373cbcceb6e93e29b5ef6)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_codec_cfg](P008_bt_audio_codec_cfg_结构体.md)、[bt_bap_qos_cfg_pref](P028_bt_bap_qos_cfg_pref_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流重新配置请求回调（Stream Reconfiguration Request Callback）。

<a id="r_a319395d4c1dbbfe31d6f67366edd6125"></a>

```c
int(* qos )(struct bt_bap_stream *stream, const struct bt_bap_qos_cfg *qos, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[qos](#a319395d4c1dbbfe31d6f67366edd6125)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流服务质量（Quality of Service，QoS）请求回调。

<a id="r_adcecb25b3c30808d38109eaa414bbf97"></a>

```c
int(* enable )(struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[enable](#adcecb25b3c30808d38109eaa414bbf97)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流启用请求回调（Stream Enable Request Callback）。

<a id="r_ab303fa3d23738b85d55b6b88a5827f43"></a>

```c
int(* start )(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[start](#ab303fa3d23738b85d55b6b88a5827f43)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流启动请求回调（Stream Start Request Callback）。

<a id="r_af2934cbca5f9700adb01f6035f0c329a"></a>

```c
int(* metadata )(struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[metadata](#af2934cbca5f9700adb01f6035f0c329a)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流元数据更新请求回调（Stream Metadata Update Request Callback）。

<a id="r_a6c10e167b53d555e2762596bc8b28088"></a>

```c
int(* disable )(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[disable](#a6c10e167b53d555e2762596bc8b28088)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流禁用请求回调（Stream Disable Request Callback）。

<a id="r_a99a5b250d4944c218c432df6bce5130d"></a>

```c
int(* stop )(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[stop](#a99a5b250d4944c218c432df6bce5130d)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流停止回调（Stream Stop Callback）。

<a id="r_ab9e8bc649765905b1db1b62e5a2a0f09"></a>

```c
int(* release )(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[release](#ab9e8bc649765905b1db1b62e5a2a0f09)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流释放回调（Stream Release Callback）。

## 5.2\_详细说明（Detailed Documentation）

<a id="aa259b32e5a731a20e23659d88143ec6e"></a>

### `config`

```c
int(* bt_ascs_cb::config) (struct bt_conn *conn, const struct bt_bap_ep *ep, enum bt_audio_dir dir, const struct bt_audio_codec_cfg *codec_cfg, struct bt_bap_stream **stream, struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp)
```

端点配置请求回调（Endpoint Configuration Request Callback）。

每当请求配置端点时调用配置回调（Config Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] conn` | 连接对象（Connection Object）。 |
| `[in] ep` | 正在配置的本地音频端点（Local Audio Endpoint）。 |
| `[in] dir` | 端点方向（Direction）。 |
| `[in] codec_cfg` | 编解码器配置（Codec Configuration）。 |
| `[out] stream` | 指向将为该端点配置的流的指针。 |
| `[out] pref` | 指向需要填入值的 QoS 偏好对象（QoS Preference Object）的指针。无效值会导致编解码器配置请求被拒绝。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a6c10e167b53d555e2762596bc8b28088"></a>

### `disable`

```c
int(* bt_ascs_cb::disable) (struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

流禁用请求回调（Stream Disable Request Callback）。

每当请求禁用音频流时调用禁用回调（Disable Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 正在禁用的流对象。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="adcecb25b3c30808d38109eaa414bbf97"></a>

### `enable`

```c
int(* bt_ascs_cb::enable) (struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len, struct bt_bap_ascs_rsp *rsp)
```

流启用请求回调（Stream Enable Request Callback）。

每当请求启用音频流以传输数据时调用启用回调（Enable Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 正在启用的流对象。 |
| `[in] meta` | 元数据条目（Metadata Entries）。 |
| `[in] meta_len` | 元数据长度。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="af2934cbca5f9700adb01f6035f0c329a"></a>

### `metadata`

```c
int(* bt_ascs_cb::metadata) (struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len, struct bt_bap_ascs_rsp *rsp)
```

流元数据更新请求回调（Stream Metadata Update Request Callback）。

每当请求更新音频流元数据时调用元数据回调（Metadata Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 流对象（Stream Object）。 |
| `[in] meta` | 元数据条目（Metadata Entries）。 |
| `[in] meta_len` | 元数据长度。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a319395d4c1dbbfe31d6f67366edd6125"></a>

### `qos`

```c
int(* bt_ascs_cb::qos) (struct bt_bap_stream *stream, const struct bt_bap_qos_cfg *qos, struct bt_bap_ascs_rsp *rsp)
```

流服务质量（Quality of Service，QoS）请求回调。

每当需要配置音频流服务质量时调用 QoS 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 正在重新配置的流对象。 |
| `[in] qos` | 服务质量配置（Quality of Service Configuration）。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a6eb6e4e35f9373cbcceb6e93e29b5ef6"></a>

### `reconfig`

```c
int(* bt_ascs_cb::reconfig) (struct bt_bap_stream *stream, enum bt_audio_dir dir, const struct bt_audio_codec_cfg *codec_cfg, struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp)
```

流重新配置请求回调（Stream Reconfiguration Request Callback）。

每当需要用不同的编解码器配置重新配置音频流时调用重新配置回调（Reconfig Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 正在重新配置的流对象。 |
| `[in] dir` | 端点方向（Direction）。 |
| `[in] codec_cfg` | 编解码器配置（Codec Configuration）。 |
| `[out] pref` | 指向需要填入值的 QoS 偏好对象（QoS Preference Object）的指针。无效值会导致编解码器配置请求被拒绝。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ab9e8bc649765905b1db1b62e5a2a0f09"></a>

### `release`

```c
int(* bt_ascs_cb::release) (struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

流释放回调（Stream Release Callback）。

每当需要释放新音频流并回收其分配资源时调用释放回调（Release Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 流对象（Stream Object）。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ab303fa3d23738b85d55b6b88a5827f43"></a>

### `start`

```c
int(* bt_ascs_cb::start) (struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

流启动请求回调（Stream Start Request Callback）。

每当请求音频流开始传输时调用启动回调（Start Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 流对象（Stream Object）。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a99a5b250d4944c218c432df6bce5130d"></a>

### `stop`

```c
int(* bt_ascs_cb::stop) (struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

流停止回调（Stream Stop Callback）。

每当请求音频流停止传输时调用停止回调（Stop Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 流对象（Stream Object）。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/ascs.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/ascs.h](https://docs.zephyrproject.org/latest/doxygen/html/ascs_8h_source.html)
- [bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)
- [bt_bap_ep](P024_bt_bap_ep_结构体.md)
- [bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)
- [bt_audio_codec_cfg](P008_bt_audio_codec_cfg_结构体.md)
- [bt_bap_stream](P033_bt_bap_stream_结构体.md)
- [bt_bap_qos_cfg_pref](P028_bt_bap_qos_cfg_pref_结构体.md)
- [bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)
- [bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_bt_aics_register_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_bt_ascs_register_param_结构体.md)
