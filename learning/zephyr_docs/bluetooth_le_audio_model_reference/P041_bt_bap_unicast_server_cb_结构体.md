---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-41
title: bt_bap_unicast_server_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__server__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_bt\_bap\_unicast\_server\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__server__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

单播服务器（Unicast Server）回调结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

单播服务器（Unicast Server）回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_ad179b35a5a5685edb8f0ac1b791d5271"></a>

```c
int(* config )(struct bt_conn *conn, const struct bt_bap_ep *ep, enum bt_audio_dir dir, const struct bt_audio_codec_cfg *codec_cfg, struct bt_bap_stream **stream, struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[config](#ad179b35a5a5685edb8f0ac1b791d5271)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_bap_ep](P024_bt_bap_ep_结构体.md)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_codec_cfg](P008_bt_audio_codec_cfg_结构体.md)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_qos_cfg_pref](P028_bt_bap_qos_cfg_pref_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

端点配置请求回调（Endpoint Configuration Request Callback）。

<a id="r_a7bed12780fdf780227d38b61d76d099b"></a>

```c
int(* reconfig )(struct bt_bap_stream *stream, enum bt_audio_dir dir, const struct bt_audio_codec_cfg *codec_cfg, struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[reconfig](#a7bed12780fdf780227d38b61d76d099b)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_codec_cfg](P008_bt_audio_codec_cfg_结构体.md)、[bt_bap_qos_cfg_pref](P028_bt_bap_qos_cfg_pref_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流重新配置请求回调（Stream Reconfiguration Request Callback）。

<a id="r_a2d50b6c328607fc46d85eaf12633f13d"></a>

```c
int(* qos )(struct bt_bap_stream *stream, const struct bt_bap_qos_cfg *qos, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[qos](#a2d50b6c328607fc46d85eaf12633f13d)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流服务质量（Quality of Service，QoS）请求回调。

<a id="r_a7424079675204fba02339ddc661b77c5"></a>

```c
int(* enable )(struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[enable](#a7424079675204fba02339ddc661b77c5)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流启用请求回调（Stream Enable Request Callback）。

<a id="r_a48fb3021507a708a0847a1ebec6075ba"></a>

```c
int(* start )(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[start](#a48fb3021507a708a0847a1ebec6075ba)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流启动请求回调（Stream Start Request Callback）。

<a id="r_a5fe98295e41c426a12ab4a7875b665c8"></a>

```c
int(* metadata )(struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[metadata](#a5fe98295e41c426a12ab4a7875b665c8)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流元数据更新请求回调（Stream Metadata Update Request Callback）。

<a id="r_a22f1af95f055bce79e3810b9682024cf"></a>

```c
int(* disable )(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[disable](#a22f1af95f055bce79e3810b9682024cf)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流禁用请求回调（Stream Disable Request Callback）。

<a id="r_a932296643929403c11512ff4ee7f7879"></a>

```c
int(* stop )(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[stop](#a932296643929403c11512ff4ee7f7879)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流停止回调（Stream Stop Callback）。

<a id="r_a9f5169f0bcdb3a6560f0767ec117b3c6"></a>

```c
int(* release )(struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

相关声明：[release](#a9f5169f0bcdb3a6560f0767ec117b3c6)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp](P010_bt_bap_ascs_rsp_结构体.md)。

流释放回调（Stream Release Callback）。

## 41.2\_详细说明（Detailed Documentation）

<a id="ad179b35a5a5685edb8f0ac1b791d5271"></a>

### `config`

```c
int(* bt_bap_unicast_server_cb::config) (struct bt_conn *conn, const struct bt_bap_ep *ep, enum bt_audio_dir dir, const struct bt_audio_codec_cfg *codec_cfg, struct bt_bap_stream **stream, struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp)
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

<a id="a22f1af95f055bce79e3810b9682024cf"></a>

### `disable`

```c
int(* bt_bap_unicast_server_cb::disable) (struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

流禁用请求回调（Stream Disable Request Callback）。

每当请求禁用音频流时调用禁用回调（Disable Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 正在禁用的流对象。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a7424079675204fba02339ddc661b77c5"></a>

### `enable`

```c
int(* bt_bap_unicast_server_cb::enable) (struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len, struct bt_bap_ascs_rsp *rsp)
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

<a id="a5fe98295e41c426a12ab4a7875b665c8"></a>

### `metadata`

```c
int(* bt_bap_unicast_server_cb::metadata) (struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len, struct bt_bap_ascs_rsp *rsp)
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

<a id="a2d50b6c328607fc46d85eaf12633f13d"></a>

### `qos`

```c
int(* bt_bap_unicast_server_cb::qos) (struct bt_bap_stream *stream, const struct bt_bap_qos_cfg *qos, struct bt_bap_ascs_rsp *rsp)
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

<a id="a7bed12780fdf780227d38b61d76d099b"></a>

### `reconfig`

```c
int(* bt_bap_unicast_server_cb::reconfig) (struct bt_bap_stream *stream, enum bt_audio_dir dir, const struct bt_audio_codec_cfg *codec_cfg, struct bt_bap_qos_cfg_pref *const pref, struct bt_bap_ascs_rsp *rsp)
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

<a id="a9f5169f0bcdb3a6560f0767ec117b3c6"></a>

### `release`

```c
int(* bt_bap_unicast_server_cb::release) (struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

流释放回调（Stream Release Callback）。

每当需要释放新音频流并回收其分配资源时调用释放回调（Release Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 流对象（Stream Object）。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a48fb3021507a708a0847a1ebec6075ba"></a>

### `start`

```c
int(* bt_bap_unicast_server_cb::start) (struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
```

流启动请求回调（Stream Start Request Callback）。

每当请求音频流开始传输时调用启动回调（Start Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 流对象（Stream Object）。 |
| `[out] rsp` | 音频流端点（Audio Stream Endpoint，ASE）操作响应对象。仅在返回值非零时使用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a932296643929403c11512ff4ee7f7879"></a>

### `stop`

```c
int(* bt_bap_unicast_server_cb::stop) (struct bt_bap_stream *stream, struct bt_bap_ascs_rsp *rsp)
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

- `zephyr/bluetooth/audio/bap.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
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

[上一章](P040_bt_bap_unicast_group_stream_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_bt_bap_unicast_server_register_param_结构体.md)
