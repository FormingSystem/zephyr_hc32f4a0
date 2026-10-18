---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-18
title: bt_bap_broadcast_sink_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__sink__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_bt\_bap\_broadcast\_sink\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__sink__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

广播音频接收端（Broadcast Audio Sink）回调结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

广播音频接收端（Broadcast Audio Sink）回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_a1adf2124ec9a16c3c68774194febd0fc"></a>

```c
void(* base_recv )(struct bt_bap_broadcast_sink *sink, const struct bt_bap_base *base, size_t base_size)
```

相关声明：[base_recv](#a1adf2124ec9a16c3c68774194febd0fc)、[bt_bap_broadcast_sink](P017_bt_bap_broadcast_sink_结构体.md)。

已收到广播音频源端点（BASE）数据。

<a id="r_a23390a63acbcf831a177a550d1012047"></a>

```c
void(* syncable )(struct bt_bap_broadcast_sink *sink, const struct bt_iso_biginfo *biginfo)
```

相关声明：[syncable](#a23390a63acbcf831a177a550d1012047)、[bt_bap_broadcast_sink](P017_bt_bap_broadcast_sink_结构体.md)、[bt_iso_biginfo](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__biginfo.html)。

广播接收端可同步（Syncable）。

<a id="r_a6af7aa849cebad26cdf382a1c97a681f"></a>

```c
void(* started )(struct bt_bap_broadcast_sink *sink)
```

相关声明：[started](#a6af7aa849cebad26cdf382a1c97a681f)、[bt_bap_broadcast_sink](P017_bt_bap_broadcast_sink_结构体.md)。

广播接收端已启动，可以从其所有流接收音频数据。

<a id="r_a1dd64d7c764ddd6c531bdd5b1890694f"></a>

```c
void(* stopped )(struct bt_bap_broadcast_sink *sink, uint8_t reason)
```

相关声明：[stopped](#a1dd64d7c764ddd6c531bdd5b1890694f)、[bt_bap_broadcast_sink](P017_bt_bap_broadcast_sink_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

广播接收端已停止，其所有流都不会接收音频数据。

## 18.2\_详细说明（Detailed Documentation）

<a id="a1adf2124ec9a16c3c68774194febd0fc"></a>

### `base_recv`

```c
void(* bt_bap_broadcast_sink_cb::base_recv) (struct bt_bap_broadcast_sink *sink, const struct bt_bap_base *base, size_t base_size)
```

已收到广播音频源端点（BASE）数据。

同步到广播者的周期性广播后，从该广播者收到 BASE 时的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sink` | 指向接收端结构体的指针。 |
| `base` | 广播音频源端点（Broadcast Audio Source Endpoint，BASE）。 |
| `base_size` | `base` 的大小。 |

<a id="a6af7aa849cebad26cdf382a1c97a681f"></a>

### `started`

```c
void(* bt_bap_broadcast_sink_cb::started) (struct bt_bap_broadcast_sink *sink)
```

广播接收端已启动，可以从其所有流接收音频数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sink` | 已启动的广播接收端（Broadcast Sink）。 |

<a id="a1dd64d7c764ddd6c531bdd5b1890694f"></a>

### `stopped`

```c
void(* bt_bap_broadcast_sink_cb::stopped) (struct bt_bap_broadcast_sink *sink, uint8_t reason)
```

广播接收端已停止，其所有流都不会接收音频数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sink` | 已停止的广播接收端。 |
| `reason` | 广播接收端停止的原因，参见 `BT_HCI_ERR_*` 值。 |

<a id="a23390a63acbcf831a177a550d1012047"></a>

### `syncable`

```c
void(* bt_bap_broadcast_sink_cb::syncable) (struct bt_bap_broadcast_sink *sink, const struct bt_iso_biginfo *biginfo)
```

广播接收端可同步（Syncable）。

当广播接收端尚未同步到音频，但音频已可同步时调用。可同步状态根据收到的广播等时组信息（BIGInfo）报告推断。

此回调被调用后，即可调用 `bt_bap_broadcast_sink_sync()` 同步到相应音频流。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sink` | 指向接收端结构体的指针。 |
| `biginfo` | BIGInfo 报告。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_bap_broadcast_sink](P017_bt_bap_broadcast_sink_结构体.md)
- [bt_iso_biginfo](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__biginfo.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_bap_broadcast_sink_sync()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html#gacadebb5ce8aab5f5b8f1ff7e0fa57805)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_bt_bap_broadcast_sink_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_bt_bap_broadcast_source_结构体.md)
