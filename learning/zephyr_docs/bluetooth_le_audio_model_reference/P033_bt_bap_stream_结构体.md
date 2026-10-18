---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-33
title: bt_bap_stream_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__stream.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_bt\_bap\_stream\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__stream.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

基本音频配置文件（Basic Audio Profile，BAP）流结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

基本音频配置文件（BAP）流结构体。流表示远端端点（Remote Endpoint）与本地能力（Local Capability）构成的一份流配置。说明（Note）：流是单向的，但可以与其他流配对，以使用双向连接等时流（CIS）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_adb95fe7a0b981a46898382ee45fd99df"></a>

```c
struct bt_conn * conn
```

相关声明：[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[conn](#adb95fe7a0b981a46898382ee45fd99df)。

连接引用（Connection Reference）。

<a id="r_af871d28b2cca8e4deba66997badbeca2"></a>

```c
struct bt_bap_ep * ep
```

相关声明：[bt_bap_ep](P024_bt_bap_ep_结构体.md)、[ep](#af871d28b2cca8e4deba66997badbeca2)。

端点引用（Endpoint Reference）。

<a id="r_a286b95d990433995a7ee74b7c3ec2f59"></a>

```c
const struct bt_audio_codec_cfg * codec_cfg
```

相关声明：[bt_audio_codec_cfg](P008_bt_audio_codec_cfg_结构体.md)、[codec_cfg](#a286b95d990433995a7ee74b7c3ec2f59)。

编解码器配置（Codec Configuration）。

<a id="r_a503bd9d7e7f594d090bcbe7fc5e313fc"></a>

```c
const struct bt_bap_qos_cfg * qos
```

相关声明：[bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)、[qos](#a503bd9d7e7f594d090bcbe7fc5e313fc)。

服务质量配置（QoS Configuration）。

<a id="r_a46a1f70c1a1fe4696039be14adf3c9b6"></a>

```c
struct bt_bap_stream_ops * ops
```

相关声明：[bt_bap_stream_ops](P034_bt_bap_stream_ops_结构体.md)、[ops](#a46a1f70c1a1fe4696039be14adf3c9b6)。

音频流操作（Audio Stream Operations）。

<a id="r_afe81620dd215aebe04ddc9e36dc7d2dd"></a>

```c
void * user_data
```

相关声明：[user_data](#afe81620dd215aebe04ddc9e36dc7d2dd)。

流用户数据（Stream User Data）。

<a id="r_a90e49f0d9abeabeff602e5409d8416e4"></a>

```c
struct bt_iso_chan * iso
```

相关声明：[bt_iso_chan](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan.html)、[iso](#a90e49f0d9abeabeff602e5409d8416e4)。

等时通道引用（ISO Channel Reference）。

<a id="r_a17d91a06d581cd4341d035eb76d8e0b2"></a>

```c
void * group
```

相关声明：[group](#a17d91a06d581cd4341d035eb76d8e0b2)。

单播组或广播组，供内部使用。

## 33.2\_详细说明（Detailed Documentation）

<a id="a286b95d990433995a7ee74b7c3ec2f59"></a>

### `codec_cfg`

```c
const struct bt_audio_codec_cfg* bt_bap_stream::codec_cfg
```

编解码器配置（Codec Configuration）。

仅当此流的端点非 `NULL` 时有效。

<a id="adb95fe7a0b981a46898382ee45fd99df"></a>

### `conn`

```c
struct bt_conn* bt_bap_stream::conn
```

连接引用（Connection Reference）。

<a id="af871d28b2cca8e4deba66997badbeca2"></a>

### `ep`

```c
struct bt_bap_ep* bt_bap_stream::ep
```

端点引用（Endpoint Reference）。

<a id="a17d91a06d581cd4341d035eb76d8e0b2"></a>

### `group`

```c
void* bt_bap_stream::group
```

单播组或广播组，供内部使用。

<a id="a90e49f0d9abeabeff602e5409d8416e4"></a>

### `iso`

```c
struct bt_iso_chan* bt_bap_stream::iso
```

等时通道引用（ISO Channel Reference）。

将流添加到组（`bt_bap_unicast_group`、`bt_bap_broadcast_source` 或 `bt_bap_broadcast_sink`）后，此项才会有效。

<a id="a46a1f70c1a1fe4696039be14adf3c9b6"></a>

### `ops`

```c
struct bt_bap_stream_ops* bt_bap_stream::ops
```

音频流操作（Audio Stream Operations）。

<a id="a503bd9d7e7f594d090bcbe7fc5e313fc"></a>

### `qos`

```c
const struct bt_bap_qos_cfg* bt_bap_stream::qos
```

服务质量配置（QoS Configuration）。

仅当此流的端点非 `NULL`，且状态为 `BT_BAP_EP_STATE_QOS_CONFIGURED` 或更高时有效。

<a id="afe81620dd215aebe04ddc9e36dc7d2dd"></a>

### `user_data`

```c
void* bt_bap_stream::user_data
```

流用户数据（Stream User Data）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)
- [bt_bap_ep](P024_bt_bap_ep_结构体.md)
- [bt_audio_codec_cfg](P008_bt_audio_codec_cfg_结构体.md)
- [bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)
- [bt_bap_stream_ops](P034_bt_bap_stream_ops_结构体.md)
- [bt_iso_chan](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan.html)
- [bt_bap_unicast_group](P036_bt_bap_unicast_group_结构体.md)
- [bt_bap_broadcast_source](P019_bt_bap_broadcast_source_结构体.md)
- [bt_bap_broadcast_sink](P017_bt_bap_broadcast_sink_结构体.md)
- [BT_BAP_EP_STATE_QOS_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_bt_bap_scan_delegator_recv_state_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_bt_bap_stream_ops_结构体.md)
