---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-34
title: bt_bap_stream_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__stream__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_bt\_bap\_stream\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__stream__ops.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

流操作（Stream Operation）。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

流操作（Stream Operation）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_afa90da66b69835c9df73068aa6373778"></a>

```c
void(* codec_configured )(struct bt_bap_stream *stream, const struct bt_bap_qos_cfg_pref *pref)
```

相关声明：[codec_configured](#afa90da66b69835c9df73068aa6373778)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_bap_qos_cfg_pref](P028_bt_bap_qos_cfg_pref_结构体.md)。

流编解码器配置完成回调（Stream Codec Configured Callback）。

<a id="r_a23616f17ef90a03db2f78df180887897"></a>

```c
void(* qos_configured )(struct bt_bap_stream *stream)
```

相关声明：[qos_configured](#a23616f17ef90a03db2f78df180887897)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)。

流 QoS 配置完成回调。

<a id="r_a1c67137b439a87647994530710d9e075"></a>

```c
void(* enabled )(struct bt_bap_stream *stream)
```

相关声明：[enabled](#a1c67137b439a87647994530710d9e075)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)。

流启用完成回调（Stream Enabled Callback）。

<a id="r_a553777c6b6bdda3e0e8c03f3915404cd"></a>

```c
void(* metadata_updated )(struct bt_bap_stream *stream)
```

相关声明：[metadata_updated](#a553777c6b6bdda3e0e8c03f3915404cd)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)。

流元数据更新完成回调。

<a id="r_a3fc784b8a2a7c1a5b19dece3619c130e"></a>

```c
void(* disabled )(struct bt_bap_stream *stream)
```

相关声明：[disabled](#a3fc784b8a2a7c1a5b19dece3619c130e)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)。

流禁用完成回调（Stream Disabled Callback）。

<a id="r_a37876562731d7dbbcd5f5613621b78ca"></a>

```c
void(* released )(struct bt_bap_stream *stream)
```

相关声明：[released](#a37876562731d7dbbcd5f5613621b78ca)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)。

流释放完成回调（Stream Released Callback）。

<a id="r_a7f595e37d40b94510bf09c1f82b479f3"></a>

```c
void(* started )(struct bt_bap_stream *stream)
```

相关声明：[started](#a7f595e37d40b94510bf09c1f82b479f3)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)。

流启动完成回调（Stream Started Callback）。

<a id="r_ab50ea295069a2cd1ab6f4353052262f5"></a>

```c
void(* stopped )(struct bt_bap_stream *stream, uint8_t reason)
```

相关声明：[stopped](#ab50ea295069a2cd1ab6f4353052262f5)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

流停止完成回调（Stream Stopped Callback）。

<a id="r_a09f31dc30de9c880758ec4a1468e59f0"></a>

```c
void(* recv )(struct bt_bap_stream *stream, const struct bt_iso_recv_info *info, struct net_buf *buf)
```

相关声明：[recv](#a09f31dc30de9c880758ec4a1468e59f0)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[bt_iso_recv_info](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__recv__info.html)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

流音频的 HCI 接收回调。

<a id="r_a33b07c51394dea6d632f42aec89a1510"></a>

```c
void(* sent )(struct bt_bap_stream *stream)
```

相关声明：[sent](#a33b07c51394dea6d632f42aec89a1510)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)。

流音频的主机控制器接口（HCI）发送回调。

<a id="r_a533d5ea96aa67b9b74b19c55afd43df1"></a>

```c
void(* connected )(struct bt_bap_stream *stream)
```

相关声明：[connected](#a533d5ea96aa67b9b74b19c55afd43df1)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)。

等时通道连接完成回调（Isochronous Channel Connected Callback）。

<a id="r_a953c7174297f1a27ceed012dced53c5a"></a>

```c
void(* disconnected )(struct bt_bap_stream *stream, uint8_t reason)
```

相关声明：[disconnected](#a953c7174297f1a27ceed012dced53c5a)、[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

等时通道断开连接回调。

## 34.2\_详细说明（Detailed Documentation）

<a id="afa90da66b69835c9df73068aa6373778"></a>

### `codec_configured`

```c
void(* bt_bap_stream_ops::codec_configured) (struct bt_bap_stream *stream, const struct bt_bap_qos_cfg_pref *pref)
```

流编解码器配置完成回调（Stream Codec Configured Callback）。

每当音频流完成编解码器配置时调用编解码器配置完成回调（Codec Configured Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 已完成配置的流对象。 |
| `pref` | 远端 QoS 偏好（Remote QoS Preferences）。 |

<a id="a533d5ea96aa67b9b74b19c55afd43df1"></a>

### `connected`

```c
void(* bt_bap_stream_ops::connected) (struct bt_bap_stream *stream)
```

等时通道连接完成回调（Isochronous Channel Connected Callback）。

如果提供此回调，则每当该流的等时通道连接完成时调用它。这不表示流已可用；流是否可用由 `bt_bap_stream_ops::started` 回调指示。

如果此流与另一条流共享等时通道，则即使此流尚未进入已启动（Started）状态，此回调仍可能被调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |

<a id="a3fc784b8a2a7c1a5b19dece3619c130e"></a>

### `disabled`

```c
void(* bt_bap_stream_ops::disabled) (struct bt_bap_stream *stream)
```

流禁用完成回调（Stream Disabled Callback）。

每当音频流已禁用时调用禁用完成回调（Disabled Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 已禁用的流对象。 |

<a id="a953c7174297f1a27ceed012dced53c5a"></a>

### `disconnected`

```c
void(* bt_bap_stream_ops::disconnected) (struct bt_bap_stream *stream, uint8_t reason)
```

等时通道断开连接回调。

如果提供此回调，则每当等时通道断开时调用它，包括连接被拒绝的情况。

如果此流与另一条流共享等时通道，则即使此流正在离开流传输（Streaming）状态，此回调也可能不被调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `reason` | 表示断开原因的 `BT_HCI_ERR_*` 值。 |

<a id="a1c67137b439a87647994530710d9e075"></a>

### `enabled`

```c
void(* bt_bap_stream_ops::enabled) (struct bt_bap_stream *stream)
```

流启用完成回调（Stream Enabled Callback）。

每当音频流已启用时调用启用完成回调（Enabled Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 已启用的流对象。 |

<a id="a553777c6b6bdda3e0e8c03f3915404cd"></a>

### `metadata_updated`

```c
void(* bt_bap_stream_ops::metadata_updated) (struct bt_bap_stream *stream)
```

流元数据更新完成回调。

每当音频流元数据已更新时调用元数据更新完成回调（Metadata Updated Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 元数据已更新的流对象。 |

<a id="a23616f17ef90a03db2f78df180887897"></a>

### `qos_configured`

```c
void(* bt_bap_stream_ops::qos_configured) (struct bt_bap_stream *stream)
```

流 QoS 配置完成回调。

每当音频流服务质量已设置或更新时调用 QoS 配置完成回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | QoS 已更新的流对象。 |

<a id="a09f31dc30de9c880758ec4a1468e59f0"></a>

### `recv`

```c
void(* bt_bap_stream_ops::recv) (struct bt_bap_stream *stream, const struct bt_iso_recv_info *info, struct net_buf *buf)
```

流音频的 HCI 接收回调。

仅当等时（ISO）数据路径为 HCI 时使用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `info` | 指向缓冲区元数据的指针，其生命周期与 `net_buf` 的生命周期关联。序列号和时间戳等元数据可以由蓝牙控制器提供。 |
| `buf` | 包含传入音频数据的缓冲区。 |

<a id="a37876562731d7dbbcd5f5613621b78ca"></a>

### `released`

```c
void(* bt_bap_stream_ops::released) (struct bt_bap_stream *stream)
```

流释放完成回调（Stream Released Callback）。

每当音频流已释放并可回收其分配资源时调用释放完成回调（Released Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 已释放的流对象。 |

<a id="a33b07c51394dea6d632f42aec89a1510"></a>

### `sent`

```c
void(* bt_bap_stream_ops::sent) (struct bt_bap_stream *stream)
```

流音频的主机控制器接口（HCI）发送回调。

控制器将服务数据单元（Service Data Unit，SDU）标记为完成后调用此回调。控制器何时进行标记取决于其实现，可能在 SDU 入发送队列之后，也可能在通过空口发出或被清除之后。

仅当等时（ISO）数据路径为 HCI 时使用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |

<a id="a7f595e37d40b94510bf09c1f82b479f3"></a>

### `started`

```c
void(* bt_bap_stream_ops::started) (struct bt_bap_stream *stream)
```

流启动完成回调（Stream Started Callback）。

每当音频流已启动并可用于流传输时调用启动完成回调（Started Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 已启动的流对象。 |

<a id="ab50ea295069a2cd1ab6f4353052262f5"></a>

### `stopped`

```c
void(* bt_bap_stream_ops::stopped) (struct bt_bap_stream *stream, uint8_t reason)
```

流停止完成回调（Stream Stopped Callback）。

每当音频流已停止时调用停止完成回调（Stopped Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 已停止的流对象。 |
| `reason` | 表示断开原因的 `BT_HCI_ERR_*` 值。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_bap_stream](P033_bt_bap_stream_结构体.md)
- [bt_bap_qos_cfg_pref](P028_bt_bap_qos_cfg_pref_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_iso_recv_info](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__recv__info.html)
- [net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_bt_bap_stream_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_bt_bap_unicast_client_cb_结构体.md)
