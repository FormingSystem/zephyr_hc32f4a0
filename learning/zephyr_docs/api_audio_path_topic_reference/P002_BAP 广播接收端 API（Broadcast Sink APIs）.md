---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-2
title: BAP 广播接收端 API（Broadcast Sink APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_BAP 广播接收端 API（Broadcast Sink APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__sink.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BAP 广播接收端 API（Broadcast Sink APIs）

<a id="details"></a>

BAP 广播接收端 API（Broadcast Sink APIs）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fbap_5Fbroadcast_5Fsink_5Fcb"></a>

```c
struct bt_bap_broadcast_sink_cb
```

相关声明：[bt_bap_broadcast_sink_cb](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md)。

广播音频接收端（Broadcast Audio Sink）回调结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_ga1b83ead634d990e954f233d0208c5a85"></a>

```c
int bt_bap_broadcast_sink_register_cb (struct bt_bap_broadcast_sink_cb *cb)
```

相关声明：[bt_bap_broadcast_sink_register_cb](#ga1b83ead634d990e954f233d0208c5a85)、[bt_bap_broadcast_sink_cb](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md)。

注册广播接收端回调（Broadcast Sink Callbacks）。

<a id="r_ga0637d1957db70ad39e0608ed07e75166"></a>

```c
int bt_bap_broadcast_sink_create (struct bt_le_per_adv_sync *pa_sync, uint32_t broadcast_id, struct bt_bap_broadcast_sink **sink)
```

相关声明：[bt_bap_broadcast_sink_create](#ga0637d1957db70ad39e0608ed07e75166)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)。

从周期广播同步（Periodic Advertising Sync）创建广播接收端（Broadcast Sink）。

<a id="r_gacadebb5ce8aab5f5b8f1ff7e0fa57805"></a>

```c
int bt_bap_broadcast_sink_sync (struct bt_bap_broadcast_sink *sink, uint32_t indexes_bitfield, struct bt_bap_stream *streams[], const uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE])
```

相关声明：[bt_bap_broadcast_sink_sync](#gacadebb5ce8aab5f5b8f1ff7e0fa57805)、[bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)。

同步到广播端的音频（Broadcaster's Audio）。

<a id="r_ga1020b21bfb4195aeb5823197145b1fe9"></a>

```c
int bt_bap_broadcast_sink_stop (struct bt_bap_broadcast_sink *sink)
```

相关声明：[bt_bap_broadcast_sink_stop](#ga1020b21bfb4195aeb5823197145b1fe9)、[bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)。

停止音频广播接收端（Audio Broadcast Sink）。

<a id="r_ga8b9d6cb409a3671654e053475ada3fda"></a>

```c
int bt_bap_broadcast_sink_delete (struct bt_bap_broadcast_sink *sink)
```

相关声明：[bt_bap_broadcast_sink_delete](#ga8b9d6cb409a3671654e053475ada3fda)、[bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)。

释放广播接收端（Broadcast Sink）。

## 2.3\_详细说明（Detailed Documentation）

<a id="ga0637d1957db70ad39e0608ed07e75166"></a>

### `bt_bap_broadcast_sink_create()`

```c
int bt_bap_broadcast_sink_create ( struct bt_le_per_adv_sync * pa_sync, uint32_t broadcast_id, struct bt_bap_broadcast_sink ** sink )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

从周期广播同步（Periodic Advertising Sync）创建广播接收端（Broadcast Sink）。

只有确认该周期广播同步（Periodic Advertising Sync）来自广播源（Broadcast Source）后，才应执行此操作。

需要将创建的广播接收端（Broadcast Sink）传给 `bt_bap_broadcast_sink_sync()`，才能同步到广播音频。

若成功，将调用 `bt_bap_broadcast_sink_cb.pa_synced()`，并传入已创建的广播接收端（Broadcast Sink）对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` pa_sync` | 指向周期广播同步对象（Periodic Advertising Sync Object）的指针。 |
| ` broadcast_id` | 24 位广播 ID。 |
| `[out] sink` | 指向所创建广播接收端（Broadcast Sink）的指针。 |

**返回（Returns）**：返回值：成功返回 0，出错时返回 errno 值。

<a id="ga8b9d6cb409a3671654e053475ada3fda"></a>

### `bt_bap_broadcast_sink_delete()`

```c
int bt_bap_broadcast_sink_delete ( struct bt_bap_broadcast_sink * sink)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

释放广播接收端（Broadcast Sink）。

在 `pa_synced` 回调之后分配了广播接收端（Broadcast Sink），便可使用此函数删除它。若该接收端已同步到任何广播音频流（Broadcast Audio Streams），必须先使用 `bt_bap_stream_stop` 停止这些流。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sink` | 指向要删除的接收端对象（Sink Object）的指针。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga1b83ead634d990e954f233d0208c5a85"></a>

### `bt_bap_broadcast_sink_register_cb()`

```c
int bt_bap_broadcast_sink_register_cb ( struct bt_bap_broadcast_sink_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注册广播接收端回调（Broadcast Sink Callbacks）。

可以注册多个回调结构体（Callback Structs），但每个结构体只能注册一次。多次注册同一回调属于未定义行为（Undefined Behavior），可能破坏协议栈。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 广播接收端回调结构体（Broadcast Sink Callback Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-EALREADY` | `cb` 已注册（Registered）时。 |

<a id="ga1020b21bfb4195aeb5823197145b1fe9"></a>

### `bt_bap_broadcast_sink_stop()`

```c
int bt_bap_broadcast_sink_stop ( struct bt_bap_broadcast_sink * sink)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

停止音频广播接收端（Audio Broadcast Sink）。

停止音频广播接收端（Audio Broadcast Sink）。接收端将停止接收 BIGInfo，音频数据也将无法继续流式传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sink` | 指向广播接收端（Broadcast Sink）的指针。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gacadebb5ce8aab5f5b8f1ff7e0fa57805"></a>

### `bt_bap_broadcast_sink_sync()`

```c
int bt_bap_broadcast_sink_sync ( struct bt_bap_broadcast_sink * sink, uint32_t indexes_bitfield, struct bt_bap_stream * streams[], const uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE] )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

同步到广播端的音频（Broadcaster's Audio）。

例如，字符串 `"Broadcast Code"` 必须表示为 `[42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sink` | 指向 `base_recv` 回调提供的接收端对象（Sink Object）的指针。 |
| `indexes_bitfield` | 要同步的广播等时流（BIS）索引位域。例如，要同步 BIS 索引 1 和 2，该值应为 `BIT(1U) \| BIT(2U)`。 |
| `streams` | 接收端使用的流对象指针（Stream Object Pointers）。若要同步多个 BIS 索引，必须提供多个流。 |
| `broadcast_code` | 16 字节的广播码（Broadcast Code）。广播已加密时必须提供，参见 `bt_bap_broadcast_sink_cb::syncable`。若该值为字符串或不足 16 字节，其余字节必须为 0。 |

**返回（Returns）**：成功返回 0，出错时返回负值。


## 2.4\_原页交叉引用（Cross References）

- [bt_bap_broadcast_sink_cb](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)
- [bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)
- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)
- [BIT(1U)](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [bt_bap_broadcast_sink_cb::syncable](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md#a23390a63acbcf831a177a550d1012047)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_分配编号转字符串 API（Assigned numbers to string API）.md) · [返回大纲](大纲.md) · [下一章](P003_加密广播数据（Encrypted Advertising Data，EAD）.md)
