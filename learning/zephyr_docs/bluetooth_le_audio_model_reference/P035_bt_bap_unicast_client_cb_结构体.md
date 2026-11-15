---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-35
title: bt_bap_unicast_client_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__client__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_bt\_bap\_unicast\_client\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__client__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

单播客户端（Unicast Client）回调结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

单播客户端（Unicast Client）回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_a64546cd17ac346dcb4bbfad5bd9f9616"></a>

```c
void(* location )(struct bt_conn *conn, enum bt_audio_dir dir, enum bt_audio_location loc)
```

相关声明：[location](#a64546cd17ac346dcb4bbfad5bd9f9616)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)。

远端单播服务器的音频位置（Audio Locations）。

<a id="r_a814a5b22c3f75b7708dac5cfdb55292f"></a>

```c
void(* supported_contexts )(struct bt_conn *conn, enum bt_audio_context snk_ctx, enum bt_audio_context src_ctx)
```

相关声明：[supported_contexts](#a814a5b22c3f75b7708dac5cfdb55292f)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

远端单播服务器支持的音频上下文（Supported Contexts）。

<a id="r_ac49c3b8283552213623608498a7befd2"></a>

```c
void(* available_contexts )(struct bt_conn *conn, enum bt_audio_context snk_ctx, enum bt_audio_context src_ctx)
```

相关声明：[available_contexts](#ac49c3b8283552213623608498a7befd2)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

远端单播服务器可用的音频上下文（Available Contexts）。

<a id="r_ae5c31f2540eb39c5b8272b5ae1e867fd"></a>

```c
void(* config )(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

相关声明：[config](#ae5c31f2540eb39c5b8272b5ae1e867fd)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)、[bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)。

`bt_bap_stream_config()` 和 `bt_bap_stream_reconfig()` 的回调函数。

<a id="r_a23b82e9f4174bcc2130d6f4570990180"></a>

```c
void(* qos )(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

相关声明：[qos](#a23b82e9f4174bcc2130d6f4570990180)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)、[bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)。

`bt_bap_stream_qos()` 的回调函数。

<a id="r_a15dd1277b37dcd96a545bb6d450c2f9d"></a>

```c
void(* enable )(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

相关声明：[enable](#a15dd1277b37dcd96a545bb6d450c2f9d)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)、[bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)。

`bt_bap_stream_enable()` 的回调函数。

<a id="r_a5c2d9ec444699ae5c75736115aab0b71"></a>

```c
void(* start )(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

相关声明：[start](#a5c2d9ec444699ae5c75736115aab0b71)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)、[bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)。

`bt_bap_stream_start()` 的回调函数。

<a id="r_abf8ec1b630220172887e3d3d4c550992"></a>

```c
void(* stop )(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

相关声明：[stop](#abf8ec1b630220172887e3d3d4c550992)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)、[bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)。

`bt_bap_stream_stop()` 的回调函数。

<a id="r_a47f86af7675fcf6ac86fad578437afa9"></a>

```c
void(* disable )(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

相关声明：[disable](#a47f86af7675fcf6ac86fad578437afa9)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)、[bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)。

`bt_bap_stream_disable()` 的回调函数。

<a id="r_a7b5fcba437b1532dbac796a48fee2f6a"></a>

```c
void(* metadata )(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

相关声明：[metadata](#a7b5fcba437b1532dbac796a48fee2f6a)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)、[bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)。

`bt_bap_stream_metadata()` 的回调函数。

<a id="r_a7dc1f2486bdabf37b85d0b347563e314"></a>

```c
void(* release )(struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

相关声明：[release](#a7dc1f2486bdabf37b85d0b347563e314)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)、[bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)。

`bt_bap_stream_release()` 的回调函数。

<a id="r_a3c55f4e23607b1e655b5f520d691bf33"></a>

```c
void(* pac_record )(struct bt_conn *conn, enum bt_audio_dir dir, const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[pac_record](#a3c55f4e23607b1e655b5f520d691bf33)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_codec_cap](P007_bt_audio_codec_cap_结构体.md)。

已发现远端已发布音频能力（Published Audio Capability，PAC）记录。

<a id="r_ae473ecc92b5c02a29742d0ba0c51ef4a"></a>

```c
void(* endpoint )(struct bt_conn *conn, enum bt_audio_dir dir, struct bt_bap_ep *ep)
```

相关声明：[endpoint](#ae473ecc92b5c02a29742d0ba0c51ef4a)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_bap_ep](P024_bt_bap_ep_结构体.md)。

已发现远端音频流端点（Audio Stream Endpoint，ASE）。

<a id="r_a1f2f7476506b6b798c1f26371217956e"></a>

```c
void(* discover )(struct bt_conn *conn, int err, enum bt_audio_dir dir)
```

相关声明：[discover](#a1f2f7476506b6b798c1f26371217956e)、[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)。

BAP 发现回调函数（Discovery Callback）。

## 35.2\_详细说明（Detailed Documentation）

<a id="ac49c3b8283552213623608498a7befd2"></a>

### `available_contexts`

```c
void(* bt_bap_unicast_client_cb::available_contexts) (struct bt_conn *conn, enum bt_audio_context snk_ctx, enum bt_audio_context src_ctx)
```

远端单播服务器可用的音频上下文（Available Contexts）。

每当从服务器读取可用上下文，或以其他方式向客户端通知可用上下文时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端单播服务器的连接。 |
| `snk_ctx` | 接收端（Sink）上下文的位域值。 |
| `src_ctx` | 发送源（Source）上下文的位域值。 |

<a id="ae5c31f2540eb39c5b8272b5ae1e867fd"></a>

### `config`

```c
void(* bt_bap_unicast_client_cb::config) (struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

`bt_bap_stream_config()` 和 `bt_bap_stream_reconfig()` 的回调函数。

服务器上的编解码器配置操作完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 执行该操作的流。 |
| `rsp_code` | 响应码（Response Code）。 |
| `reason` | 原因码（Reason Code）。 |

<a id="a47f86af7675fcf6ac86fad578437afa9"></a>

### `disable`

```c
void(* bt_bap_unicast_client_cb::disable) (struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

`bt_bap_stream_disable()` 的回调函数。

服务器上的禁用操作完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 执行该操作的流。如果没有与服务器发送的 ASE ID 关联的流，则可能为 `NULL`。 |
| `rsp_code` | 响应码（Response Code）。 |
| `reason` | 原因码（Reason Code）。 |

<a id="a1f2f7476506b6b798c1f26371217956e"></a>

### `discover`

```c
void(* bt_bap_unicast_client_cb::discover) (struct bt_conn *conn, int err, enum bt_audio_dir dir)
```

BAP 发现回调函数（Discovery Callback）。

发现过程完成时，将 `ep` 设为 `NULL`，并将 `err` 设为 0。

发现过程完成时，将 `codec` 和 `ep` 都设为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端单播服务器的连接。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `dir` | 发现的远端端点和能力的类型。 |

<a id="a15dd1277b37dcd96a545bb6d450c2f9d"></a>

### `enable`

```c
void(* bt_bap_unicast_client_cb::enable) (struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

`bt_bap_stream_enable()` 的回调函数。

服务器上的启用操作完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 执行该操作的流。如果没有与服务器发送的 ASE ID 关联的流，则可能为 `NULL`。 |
| `rsp_code` | 响应码（Response Code）。 |
| `reason` | 原因码（Reason Code）。 |

<a id="ae473ecc92b5c02a29742d0ba0c51ef4a"></a>

### `endpoint`

```c
void(* bt_bap_unicast_client_cb::endpoint) (struct bt_conn *conn, enum bt_audio_dir dir, struct bt_bap_ep *ep)
```

已发现远端音频流端点（Audio Stream Endpoint，ASE）。

在发现过程中发现 ASE 时调用。

发现过程完成时，将 `codec` 和 `ep` 都设为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端单播服务器的连接。 |
| `dir` | 发现的远端端点和能力的类型。 |
| `ep` | 远端端点（Remote Endpoint）。 |

<a id="a64546cd17ac346dcb4bbfad5bd9f9616"></a>

### `location`

```c
void(* bt_bap_unicast_client_cb::location) (struct bt_conn *conn, enum bt_audio_dir dir, enum bt_audio_location loc)
```

远端单播服务器的音频位置（Audio Locations）。

每当从服务器读取音频位置，或以其他方式向客户端通知音频位置时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端单播服务器的连接。 |
| `dir` | 音频位置的方向。 |
| `loc` | 音频位置的位域值。 |

<a id="a7b5fcba437b1532dbac796a48fee2f6a"></a>

### `metadata`

```c
void(* bt_bap_unicast_client_cb::metadata) (struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

`bt_bap_stream_metadata()` 的回调函数。

服务器上的元数据操作完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 执行该操作的流。如果没有与服务器发送的 ASE ID 关联的流，则可能为 `NULL`。 |
| `rsp_code` | 响应码（Response Code）。 |
| `reason` | 原因码（Reason Code）。 |

<a id="a3c55f4e23607b1e655b5f520d691bf33"></a>

### `pac_record`

```c
void(* bt_bap_unicast_client_cb::pac_record) (struct bt_conn *conn, enum bt_audio_dir dir, const struct bt_audio_codec_cap *codec_cap)
```

已发现远端已发布音频能力（Published Audio Capability，PAC）记录。

在发现过程中发现 PAC 记录时调用。

编解码器对象仅在回调期间有效；如果以后还要使用，接收方必须保存这些值。

发现过程完成时，将 `codec` 和 `ep` 都设为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端单播服务器的连接。 |
| `dir` | 发现的远端端点和能力的类型。 |
| `codec_cap` | 远端能力（Remote Capabilities）。 |

<a id="a23b82e9f4174bcc2130d6f4570990180"></a>

### `qos`

```c
void(* bt_bap_unicast_client_cb::qos) (struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

`bt_bap_stream_qos()` 的回调函数。

服务器上的 QoS 配置操作完成时调用。对于正在配置 QoS 的组中的每条流，都会调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 执行该操作的流。如果没有与服务器发送的 ASE ID 关联的流，则可能为 `NULL`。 |
| `rsp_code` | 响应码（Response Code）。 |
| `reason` | 原因码（Reason Code）。 |

<a id="a7dc1f2486bdabf37b85d0b347563e314"></a>

### `release`

```c
void(* bt_bap_unicast_client_cb::release) (struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

`bt_bap_stream_release()` 的回调函数。

服务器上的释放操作完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 执行该操作的流。如果没有与服务器发送的 ASE ID 关联的流，则可能为 `NULL`。 |
| `rsp_code` | 响应码（Response Code）。 |
| `reason` | 原因码（Reason Code）。 |

<a id="a5c2d9ec444699ae5c75736115aab0b71"></a>

### `start`

```c
void(* bt_bap_unicast_client_cb::start) (struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

`bt_bap_stream_start()` 的回调函数。

服务器上的启动操作完成时调用。仅当传给 `bt_bap_stream_start()` 的流对应 `BT_AUDIO_DIR_SOURCE` 端点时才调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 执行该操作的流。如果没有与服务器发送的 ASE ID 关联的流，则可能为 `NULL`。 |
| `rsp_code` | 响应码（Response Code）。 |
| `reason` | 原因码（Reason Code）。 |

<a id="abf8ec1b630220172887e3d3d4c550992"></a>

### `stop`

```c
void(* bt_bap_unicast_client_cb::stop) (struct bt_bap_stream *stream, enum bt_bap_ascs_rsp_code rsp_code, enum bt_bap_ascs_reason reason)
```

`bt_bap_stream_stop()` 的回调函数。

服务器上的停止操作完成时调用。仅当传给 `bt_bap_stream_stop()` 的流对应 `BT_AUDIO_DIR_SOURCE` 端点时才调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 执行该操作的流。如果没有与服务器发送的 ASE ID 关联的流，则可能为 `NULL`。 |
| `rsp_code` | 响应码（Response Code）。 |
| `reason` | 原因码（Reason Code）。 |

<a id="a814a5b22c3f75b7708dac5cfdb55292f"></a>

### `supported_contexts`

```c
void(* bt_bap_unicast_client_cb::supported_contexts) (struct bt_conn *conn, enum bt_audio_context snk_ctx, enum bt_audio_context src_ctx)
```

远端单播服务器支持的音频上下文（Supported Contexts）。

每当从服务器读取支持的上下文，或以其他方式向客户端通知支持的上下文时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端单播服务器的连接。 |
| `snk_ctx` | 接收端（Sink）上下文的位域值。 |
| `src_ctx` | 发送源（Source）上下文的位域值。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)
- [bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [bt_bap_stream](P033_bt_bap_stream_结构体.md)
- [bt_bap_ascs_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9f7efa749c75edd32dc50503397ab9d1)
- [bt_bap_ascs_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga9ca1630544a336b15af8a8e8934c5a45)
- [bt_bap_stream_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaaecbb590e5d073829d4c150e4fd2d8aa)
- [bt_bap_stream_reconfig()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa7df3f6b906241ad5291295a6ddcf1e4)
- [bt_bap_stream_qos()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac878ed89242cac9a8514e8e4f1da4d9d)
- [bt_bap_stream_enable()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga13a859b31b0310ec22339ec7ed0754f8)
- [bt_bap_stream_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga8f2dc67c35299334d21c7dee7b8664ae)
- [bt_bap_stream_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gada72bcd3951eff2bc6b70c02dcaed98b)
- [bt_bap_stream_disable()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0fd2bb35909fc19e3e9cff068ba9e9aa)
- [bt_bap_stream_metadata()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0afe6c927729697e2f984cefcbc7c0f1)
- [bt_bap_stream_release()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaaf94f1f0dda7ef356c0f9ae79b5c60e4)
- [bt_audio_codec_cap](P007_bt_audio_codec_cap_结构体.md)
- [bt_bap_ep](P024_bt_bap_ep_结构体.md)
- [BT_AUDIO_DIR_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_bt_bap_stream_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_bt_bap_unicast_group_结构体.md)
