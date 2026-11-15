---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-10
title: bt_a2dp_stream_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__stream__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_bt\_a2dp\_stream\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__stream__ops.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

与流端点相关的操作。

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

<a id="details"></a>

与流端点相关的操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a146f907aa60ae130b3248da7475db0cb"></a>

```c
void(* configured )(struct bt_a2dp_stream *stream)
```

相关声明：[configured](#a146f907aa60ae130b3248da7475db0cb)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)。

流配置完成回调（Stream Configured Callback）。

<a id="r_a88d7a0598a5af6740747eb575b8b57df"></a>

```c
void(* established )(struct bt_a2dp_stream *stream)
```

相关声明：[established](#a88d7a0598a5af6740747eb575b8b57df)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)。

流建立回调（Stream Establishment Callback）。

<a id="r_acaa2c8b7e59a0b0bb652c9801110234b"></a>

```c
void(* released )(struct bt_a2dp_stream *stream)
```

相关声明：[released](#acaa2c8b7e59a0b0bb652c9801110234b)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)。

流释放回调（Stream Release Callback）。

<a id="r_a292e604e7db2faca1915533eab76830e"></a>

```c
void(* started )(struct bt_a2dp_stream *stream)
```

相关声明：[started](#a292e604e7db2faca1915533eab76830e)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)。

流启动回调（Stream Start Callback）。

<a id="r_af839ecbcb131cb68165c516c2e049fe5"></a>

```c
void(* suspended )(struct bt_a2dp_stream *stream)
```

相关声明：[suspended](#af839ecbcb131cb68165c516c2e049fe5)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)。

流暂停回调（Stream Suspend Callback）。

<a id="r_ac3e34e9abca72313873b9944501407bb"></a>

```c
void(* recv )(struct bt_a2dp_stream *stream, struct net_buf *buf, uint16_t seq_num, uint32_t ts)
```

相关声明：[recv](#ac3e34e9abca72313873b9944501407bb)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

媒体流数据，仅用于接收端（Sink）。

<a id="r_af7e532cff599eab0515aeef228eeb549"></a>

```c
void(* sent )(struct bt_a2dp_stream *stream)
```

相关声明：[sent](#af7e532cff599eab0515aeef228eeb549)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)。

流音频的主机控制器接口（HCI）发送回调。

<a id="r_aacd43a628ff2ad2f23c13c113bb4e223"></a>

```c
void(* delay_report )(struct bt_a2dp_stream *stream, uint16_t value)
```

相关声明：[delay_report](#aacd43a628ff2ad2f23c13c113bb4e223)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

已收到延迟报告值。

## 10.2\_详细说明（Detailed Documentation）

<a id="a146f907aa60ae130b3248da7475db0cb"></a>

### `configured`

```c
void(* bt_a2dp_stream_ops::configured) (struct bt_a2dp_stream *stream)
```

流配置完成回调（Stream Configured Callback）。

每当音频流完成配置或重新配置时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 已完成配置的流对象。 |

<a id="aacd43a628ff2ad2f23c13c113bb4e223"></a>

### `delay_report`

```c
void(* bt_a2dp_stream_ops::delay_report) (struct bt_a2dp_stream *stream, uint16_t value)
```

已收到延迟报告值。

当延迟报告得到接受响应时调用此回调，即未设置 `delay_report_req`，或者 `delay_report_req` 返回成功时。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `value` | 延迟报告值，单位为 1/10 毫秒。 |

<a id="a88d7a0598a5af6740747eb575b8b57df"></a>

### `established`

```c
void(* bt_a2dp_stream_ops::established) (struct bt_a2dp_stream *stream)
```

流建立回调（Stream Establishment Callback）。

每当音频流建立完成时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 已建立的流对象。 |

<a id="ac3e34e9abca72313873b9944501407bb"></a>

### `recv`

```c
void(* bt_a2dp_stream_ops::recv) (struct bt_a2dp_stream *stream, struct net_buf *buf, uint16_t seq_num, uint32_t ts)
```

媒体流数据，仅用于接收端（Sink）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象。 |
| `buf` | 数据缓冲区（Data Buffer）。 |
| `seq_num` | 序列号（Sequence Number）。 |
| `ts` | 时间戳（Timestamp）。 |

<a id="acaa2c8b7e59a0b0bb652c9801110234b"></a>

### `released`

```c
void(* bt_a2dp_stream_ops::released) (struct bt_a2dp_stream *stream)
```

流释放回调（Stream Release Callback）。

释放过程（`bt_a2dp_stream_release`、`release_req`、`release_rsp` 以及断开 L2CAP 媒体通道）、中止过程（`bt_a2dp_stream_abort`、`abort_req`、`abort_rsp` 以及断开 L2CAP 媒体通道）和错误处理过程（例如 L2CAP 通道意外断开）都会导致流释放。每当音频流释放时调用此回调。释放后，该流失效，不能再用于控制。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 已释放的流对象。 |

<a id="af7e532cff599eab0515aeef228eeb549"></a>

### `sent`

```c
void(* bt_a2dp_stream_ops::sent) (struct bt_a2dp_stream *stream)
```

流音频的主机控制器接口（HCI）发送回调。

控制器将服务数据单元（Service Data Unit，SDU）标记为完成后调用此回调。控制器何时进行标记取决于其实现，可能在 SDU 入发送队列之后，也可能在通过空口发出或被清除之后。

仅当等时（ISO）数据路径为 HCI 时使用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |

<a id="a292e604e7db2faca1915533eab76830e"></a>

### `started`

```c
void(* bt_a2dp_stream_ops::started) (struct bt_a2dp_stream *stream)
```

流启动回调（Stream Start Callback）。

每当音频流启动时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 已启动的流对象。 |

<a id="af839ecbcb131cb68165c516c2e049fe5"></a>

### `suspended`

```c
void(* bt_a2dp_stream_ops::suspended) (struct bt_a2dp_stream *stream)
```

流暂停回调（Stream Suspend Callback）。

每当音频流暂停时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 已暂停的流对象。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/a2dp.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/a2dp.h](https://docs.zephyrproject.org/latest/doxygen/html/a2dp_8h_source.html)
- [bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)
- [net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_bt_a2dp_stream_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_bt_addr_le_t_结构体.md)
