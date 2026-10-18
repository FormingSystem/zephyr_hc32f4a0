---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-2
title: bt_a2dp_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_bt\_a2dp\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

正在连接时的回调（Connecting Callback）。

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

<a id="details"></a>

正在连接时的回调（Connecting Callback）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_ab0b6a895c2f050ab0961325b8ce7e862"></a>

```c
void(* connected )(struct bt_a2dp *a2dp, int err)
```

相关声明：[connected](#ab0b6a895c2f050ab0961325b8ce7e862)、[bt_a2dp](P001_bt_a2dp_结构体.md)。

A2DP 连接已建立。

<a id="r_a80401da71ae6dc74d058163624f78518"></a>

```c
void(* disconnected )(struct bt_a2dp *a2dp)
```

相关声明：[disconnected](#a80401da71ae6dc74d058163624f78518)、[bt_a2dp](P001_bt_a2dp_结构体.md)。

A2DP 连接已断开。

<a id="r_aab8f5f53a7b507d55e1d594995739222"></a>

```c
int(* config_req )(struct bt_a2dp *a2dp, struct bt_a2dp_ep *ep, struct bt_a2dp_codec_cfg *codec_cfg, struct bt_a2dp_stream **stream, uint8_t *rsp_err_code)
```

相关声明：[config_req](#aab8f5f53a7b507d55e1d594995739222)、[bt_a2dp](P001_bt_a2dp_结构体.md)、[bt_a2dp_ep](P007_bt_a2dp_ep_结构体.md)、[bt_a2dp_codec_cfg](P003_bt_a2dp_codec_cfg_结构体.md)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

端点配置请求回调（Endpoint Configuration Request Callback）。

<a id="r_aba09a3ccebcd77068028d22036d6b53d"></a>

```c
int(* reconfig_req )(struct bt_a2dp_stream *stream, struct bt_a2dp_codec_cfg *codec_cfg, uint8_t *rsp_err_code)
```

相关声明：[reconfig_req](#aba09a3ccebcd77068028d22036d6b53d)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[bt_a2dp_codec_cfg](P003_bt_a2dp_codec_cfg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

端点配置请求回调（Endpoint Configuration Request Callback）。

<a id="r_a3b2f6c42bcdefe8a2591fc59c2357786"></a>

```c
void(* config_rsp )(struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

相关声明：[config_rsp](#a3b2f6c42bcdefe8a2591fc59c2357786)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`bt_a2dp_stream_config()` 和 `bt_a2dp_stream_reconfig()` 的回调函数。

<a id="r_adc611ad1a28c3da94f261cc94f63698f"></a>

```c
int(* establish_req )(struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

相关声明：[establish_req](#adc611ad1a28c3da94f261cc94f63698f)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

流建立请求回调（Stream Establishment Request Callback）。

<a id="r_af19a1f6bb65c60cb0ec7294e66468ba6"></a>

```c
void(* establish_rsp )(struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

相关声明：[establish_rsp](#af19a1f6bb65c60cb0ec7294e66468ba6)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`bt_a2dp_stream_establish()` 的回调函数。

<a id="r_a90a637e6e81bf5a74c878c3b4b2e63c0"></a>

```c
int(* release_req )(struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

相关声明：[release_req](#a90a637e6e81bf5a74c878c3b4b2e63c0)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

流释放请求回调（Stream Release Request Callback）。

<a id="r_ab4c148eb7be896dec8f6a33217b475e1"></a>

```c
void(* release_rsp )(struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

相关声明：[release_rsp](#ab4c148eb7be896dec8f6a33217b475e1)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`bt_a2dp_stream_release()` 的回调函数。

<a id="r_a1388b0365e46afce78b4f08f25af6858"></a>

```c
int(* start_req )(struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

相关声明：[start_req](#a1388b0365e46afce78b4f08f25af6858)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

流启动请求回调（Stream Start Request Callback）。

<a id="r_a49bae91e1cac18a5da90160214a61725"></a>

```c
void(* start_rsp )(struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

相关声明：[start_rsp](#a49bae91e1cac18a5da90160214a61725)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`bt_a2dp_stream_start()` 的回调函数。

<a id="r_a79d2edefa0e6e979bfcfcffe9391a7c0"></a>

```c
int(* suspend_req )(struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

相关声明：[suspend_req](#a79d2edefa0e6e979bfcfcffe9391a7c0)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

流暂停请求回调（Stream Suspend Request Callback）。

<a id="r_a6064e5d61acb3cdd0f83246ce90e712f"></a>

```c
void(* suspend_rsp )(struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

相关声明：[suspend_rsp](#a6064e5d61acb3cdd0f83246ce90e712f)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`bt_a2dp_stream_suspend()` 的回调函数。

<a id="r_a81fe4d6d5db8ad1cf541b141c0bca18f"></a>

```c
int(* abort_req )(struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

相关声明：[abort_req](#a81fe4d6d5db8ad1cf541b141c0bca18f)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

流中止请求回调（Stream Abort Request Callback）。

<a id="r_af051e057f504b1d9c8da4e4958fba115"></a>

```c
void(* abort_rsp )(struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

相关声明：[abort_rsp](#af051e057f504b1d9c8da4e4958fba115)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`bt_a2dp_stream_abort()` 的回调函数。

<a id="r_a37e54151eda0c763c957ee1b2c4218a8"></a>

```c
int(* get_config_req )(struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

相关声明：[get_config_req](#a37e54151eda0c763c957ee1b2c4218a8)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

流配置获取回调（Stream Get Configuration Callback）。

<a id="r_aebbb8d6e28ec806915e786729810c1d9"></a>

```c
void(* get_config_rsp )(struct bt_a2dp_stream *stream, struct bt_a2dp_codec_cfg *codec_cfg, uint8_t rsp_err_code)
```

相关声明：[get_config_rsp](#aebbb8d6e28ec806915e786729810c1d9)、[bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)、[bt_a2dp_codec_cfg](P003_bt_a2dp_codec_cfg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`bt_a2dp_stream_get_config()` 的回调函数。

## 2.2\_详细说明（Detailed Documentation）

<a id="a81fe4d6d5db8ad1cf541b141c0bca18f"></a>

### `abort_req`

```c
int(* bt_a2dp_cb::abort_req) (struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

流中止请求回调（Stream Abort Request Callback）。

每当收到中止流的请求时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[out] rsp_err_code` | 响应错误时给出错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

返回（Returns）：成功时返回 0，发生错误时返回负值。

<a id="af051e057f504b1d9c8da4e4958fba115"></a>

### `abort_rsp`

```c
void(* bt_a2dp_cb::abort_rsp) (struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

`bt_a2dp_stream_abort()` 的回调函数。

中止操作完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[in] rsp_err_code` | 远端响应的错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

<a id="aab8f5f53a7b507d55e1d594995739222"></a>

### `config_req`

```c
int(* bt_a2dp_cb::config_req) (struct bt_a2dp *a2dp, struct bt_a2dp_ep *ep, struct bt_a2dp_codec_cfg *codec_cfg, struct bt_a2dp_stream **stream, uint8_t *rsp_err_code)
```

端点配置请求回调（Endpoint Configuration Request Callback）。

每当收到配置端点的请求时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` a2dp` | A2DP 连接对象。 |
| `[in] ep` | 正在配置的本地音频端点（Local Audio Endpoint）。 |
| `[in] codec_cfg` | 编解码器配置（Codec Configuration）。 |
| `[out] stream` | 指向将为该端点配置的流的指针。 |
| `[out] rsp_err_code` | 响应错误时给出错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

返回（Returns）：成功时返回 0，发生错误时返回负值。

<a id="a3b2f6c42bcdefe8a2591fc59c2357786"></a>

### `config_rsp`

```c
void(* bt_a2dp_cb::config_rsp) (struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

`bt_a2dp_stream_config()` 和 `bt_a2dp_stream_reconfig()` 的回调函数。

编解码器配置操作完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[in] rsp_err_code` | 远端响应的错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

<a id="ab0b6a895c2f050ab0961325b8ce7e862"></a>

### `connected`

```c
void(* bt_a2dp_cb::connected) (struct bt_a2dp *a2dp, int err)
```

A2DP 连接已建立。

此回调向应用通知 A2DP 连接，即音视频分发传输协议（Audio/Video Distribution Transport Protocol，AVDTP）的逻辑链路控制与适配协议（L2CAP）连接。如果 `err` 参数非零，则表示连接建立失败。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a2dp` | A2DP 连接对象。 |
| `err` | 错误码。 |

<a id="a80401da71ae6dc74d058163624f78518"></a>

### `disconnected`

```c
void(* bt_a2dp_cb::disconnected) (struct bt_a2dp *a2dp)
```

A2DP 连接已断开。

此回调向应用通知 A2DP 连接已经断开。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a2dp` | A2DP 连接对象。 |

<a id="adc611ad1a28c3da94f261cc94f63698f"></a>

### `establish_req`

```c
int(* bt_a2dp_cb::establish_req) (struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

流建立请求回调（Stream Establishment Request Callback）。

每当收到建立流的请求时调用此回调，即发送打开命令（Open Command）并创建流的 L2CAP 通道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[out] rsp_err_code` | 响应错误时给出错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

返回（Returns）：成功时返回 0，发生错误时返回负值。

<a id="af19a1f6bb65c60cb0ec7294e66468ba6"></a>

### `establish_rsp`

```c
void(* bt_a2dp_cb::establish_rsp) (struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

`bt_a2dp_stream_establish()` 的回调函数。

流建立操作完成时调用，即打开命令及流的 L2CAP 通道创建完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[in] rsp_err_code` | 远端响应的错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

<a id="a37e54151eda0c763c957ee1b2c4218a8"></a>

### `get_config_req`

```c
int(* bt_a2dp_cb::get_config_req) (struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

流配置获取回调（Stream Get Configuration Callback）。

每当请求流返回当前已配置的配置时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[out] rsp_err_code` | 响应错误时给出错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

返回（Returns）：成功时返回 0，发生错误时返回负值。

<a id="aebbb8d6e28ec806915e786729810c1d9"></a>

### `get_config_rsp`

```c
void(* bt_a2dp_cb::get_config_rsp) (struct bt_a2dp_stream *stream, struct bt_a2dp_codec_cfg *codec_cfg, uint8_t rsp_err_code)
```

`bt_a2dp_stream_get_config()` 的回调函数。

获取配置操作完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[in] codec_cfg` | 获取到的编解码器配置。 |
| `[in] rsp_err_code` | 远端响应的错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

<a id="aba09a3ccebcd77068028d22036d6b53d"></a>

### `reconfig_req`

```c
int(* bt_a2dp_cb::reconfig_req) (struct bt_a2dp_stream *stream, struct bt_a2dp_codec_cfg *codec_cfg, uint8_t *rsp_err_code)
```

端点配置请求回调（Endpoint Configuration Request Callback）。

每当收到重新配置端点的请求时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[in] codec_cfg` | 编解码器配置（Codec Configuration）。 |
| `[out] rsp_err_code` | 响应错误时给出错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

返回（Returns）：成功时返回 0，发生错误时返回负值。

<a id="a90a637e6e81bf5a74c878c3b4b2e63c0"></a>

### `release_req`

```c
int(* bt_a2dp_cb::release_req) (struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

流释放请求回调（Stream Release Request Callback）。

每当收到释放流的请求时调用此回调，即执行释放命令（Release Command）并释放 L2CAP 通道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[out] rsp_err_code` | 响应错误时给出错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

返回（Returns）：成功时返回 0，发生错误时返回负值。

<a id="ab4c148eb7be896dec8f6a33217b475e1"></a>

### `release_rsp`

```c
void(* bt_a2dp_cb::release_rsp) (struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

`bt_a2dp_stream_release()` 的回调函数。

流释放操作完成时调用，即释放命令及 L2CAP 通道释放完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[in] rsp_err_code` | 远端响应的错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

<a id="a1388b0365e46afce78b4f08f25af6858"></a>

### `start_req`

```c
int(* bt_a2dp_cb::start_req) (struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

流启动请求回调（Stream Start Request Callback）。

每当收到启动流的请求时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[out] rsp_err_code` | 响应错误时给出错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

返回（Returns）：成功时返回 0，发生错误时返回负值。

<a id="a49bae91e1cac18a5da90160214a61725"></a>

### `start_rsp`

```c
void(* bt_a2dp_cb::start_rsp) (struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

`bt_a2dp_stream_start()` 的回调函数。

启动操作完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[in] rsp_err_code` | 远端响应的错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

<a id="a79d2edefa0e6e979bfcfcffe9391a7c0"></a>

### `suspend_req`

```c
int(* bt_a2dp_cb::suspend_req) (struct bt_a2dp_stream *stream, uint8_t *rsp_err_code)
```

流暂停请求回调（Stream Suspend Request Callback）。

每当收到暂停流的请求时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[out] rsp_err_code` | 响应错误时给出错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

返回（Returns）：成功时返回 0，发生错误时返回负值。

<a id="a6064e5d61acb3cdd0f83246ce90e712f"></a>

### `suspend_rsp`

```c
void(* bt_a2dp_cb::suspend_rsp) (struct bt_a2dp_stream *stream, uint8_t rsp_err_code)
```

`bt_a2dp_stream_suspend()` 的回调函数。

暂停操作完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 指向流对象（Stream Object）的指针。 |
| `[in] rsp_err_code` | 远端响应的错误码，类型为 `bt_a2dp_err_code` 或 `bt_avdtp_err_code`。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/a2dp.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/a2dp.h](https://docs.zephyrproject.org/latest/doxygen/html/a2dp_8h_source.html)
- [bt_a2dp](P001_bt_a2dp_结构体.md)
- [bt_a2dp_ep](P007_bt_a2dp_ep_结构体.md)
- [bt_a2dp_codec_cfg](P003_bt_a2dp_codec_cfg_结构体.md)
- [bt_a2dp_stream](P009_bt_a2dp_stream_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_a2dp_stream_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga3ff3ca4cd016025f95690e89643f0ff5)
- [bt_a2dp_stream_reconfig()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga70fc5f43265a4c407a847c4205cd7697)
- [bt_a2dp_stream_establish()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gaf47e0028176494f5353ee00261ffa49a)
- [bt_a2dp_stream_release()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga194e7ec86715cf9007de30f6492e4f58)
- [bt_a2dp_stream_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga368403c64581b761099631280014d877)
- [bt_a2dp_stream_suspend()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#gaf22030f4edd5401b2d5359bcb0590145)
- [bt_a2dp_stream_abort()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga7999e06ef74be78ec2744bb24ff72912)
- [bt_a2dp_stream_get_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga68f74181bba610c7fd158558afdcbd86)
- [bt_a2dp_err_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga4162a6db1ead67f52f961d660beabb8c)
- [bt_avdtp_err_code](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#affc7226c1b7795a3d2f51cb4ffaf6d21)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_bt_a2dp_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_bt_a2dp_codec_cfg_结构体.md)
