---
id: learning.zephyr-docs.api-video-event-topic-reference.page-2
title: BAP 单播服务器 API（Unicast Server APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_BAP 单播服务器 API（Unicast Server APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fbap_5Funicast_5Fserver_5Fcb"></a>

```c
struct bt_bap_unicast_server_cb
```

相关声明：[bt_bap_unicast_server_cb](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md)。

单播服务器（Unicast Server）回调结构体。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.2\_类型定义（Typedefs）

<a id="r_gabb2b96d8de285dff7cbade83768d9aff"></a>

```c
typedef bool(* bt_bap_ep_func_t) (struct bt_bap_ep *ep, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_ep_func_t](#gabb2b96d8de285dff7cbade83768d9aff)、[bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)。

为每个端点（Endpoint）调用的回调函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_gab3ea6014854e6290f058c87e866c3191"></a>

```c
int bt_bap_unicast_server_register (const struct bt_bap_unicast_server_register_param *param)
```

相关声明：[bt_bap_unicast_server_register](#gab3ea6014854e6290f058c87e866c3191)、[bt_bap_unicast_server_register_param](../bluetooth_le_audio_model_reference/P042_bt_bap_unicast_server_register_param_结构体.md)。

注册单播服务器（Unicast Server）。

<a id="r_ga6ef3b9e877ffdc04cc48fda6713a0209"></a>

```c
int bt_bap_unicast_server_unregister (void)
```

相关声明：[bt_bap_unicast_server_unregister](#ga6ef3b9e877ffdc04cc48fda6713a0209)。

注销单播服务器（Unicast Server）。

<a id="r_ga7669133936bc13f7ab38817db9ce69c0"></a>

```c
int bt_bap_unicast_server_register_cb (const struct bt_bap_unicast_server_cb *cb)
```

相关声明：[bt_bap_unicast_server_register_cb](#ga7669133936bc13f7ab38817db9ce69c0)、[bt_bap_unicast_server_cb](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md)。

注册单播服务器回调（Unicast Server Callbacks）。

<a id="r_gadf984f12bdeadcfc814dc2fc770cb7bf"></a>

```c
int bt_bap_unicast_server_unregister_cb (const struct bt_bap_unicast_server_cb *cb)
```

相关声明：[bt_bap_unicast_server_unregister_cb](#gadf984f12bdeadcfc814dc2fc770cb7bf)、[bt_bap_unicast_server_cb](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md)。

注销单播服务器回调（Unicast Server Callbacks）。

<a id="r_gafe7640d6269ec95c8af6d7549fac785d"></a>

```c
int bt_bap_unicast_server_foreach_ep (struct bt_conn *conn, bt_bap_ep_func_t func, void *user_data)
```

相关声明：[bt_bap_unicast_server_foreach_ep](#gafe7640d6269ec95c8af6d7549fac785d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_ep_func_t](#gabb2b96d8de285dff7cbade83768d9aff)。

遍历所给连接的全部端点（Endpoints）。

<a id="r_ga98b170c9f371d7d60c3dde9aff3f6d6b"></a>

```c
int bt_bap_unicast_server_config_ase (struct bt_conn *conn, struct bt_bap_stream *stream, const struct bt_audio_codec_cfg *codec_cfg, const struct bt_bap_qos_cfg_pref *qos_pref)
```

相关声明：[bt_bap_unicast_server_config_ase](#ga98b170c9f371d7d60c3dde9aff3f6d6b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_bap_qos_cfg_pref](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md)。

初始化并配置新的音频流端点（ASE）。

## 2.4\_详细说明（Detailed Documentation）

<a id="gabb2b96d8de285dff7cbade83768d9aff"></a>

### `bt_bap_ep_func_t`

```c
typedef bool(* bt_bap_ep_func_t) (struct bt_bap_ep *ep, void *user_data)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

为每个端点（Endpoint）调用的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ep` | 包含端点信息（Endpoint Info）的结构体对象。 |
| `user_data` | 传给函数的数据（Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 继续遍历（Continue Iterating）。 |
| `false` | 停止遍历（Stop Iterating）。 |

<a id="ga98b170c9f371d7d60c3dde9aff3f6d6b"></a>

### `bt_bap_unicast_server_config_ase()`

```c
int bt_bap_unicast_server_config_ase ( struct bt_conn * conn, struct bt_bap_stream * stream, const struct bt_audio_codec_cfg * codec_cfg, const struct bt_bap_qos_cfg_pref * qos_pref )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

初始化并配置新的音频流端点（ASE）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `stream` | 要附加到音频流端点（ASE）的已配置流对象（Stream Object）。 |
| `codec_cfg` | 编解码器配置（Codec Configuration）。 |
| `qos_pref` | 音频流服务质量偏好（Audio Stream Quality of Service Preference）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gafe7640d6269ec95c8af6d7549fac785d"></a>

### `bt_bap_unicast_server_foreach_ep()`

```c
int bt_bap_unicast_server_foreach_ep ( struct bt_conn * conn, bt_bap_ep_func_t func, void * user_data )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

遍历所给连接的全部端点（Endpoints）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `func` | 为每个端点（Endpoint）调用的函数。 |
| `user_data` | 传给回调函数（Callback Function）的数据。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ECANCELED` | 遍历尚未完成便被回调函数（Callback Function）停止。 |
| `-EINVAL` | `conn` 或 `func` 为 `NULL`。 |

<a id="gab3ea6014854e6290f058c87e866c3191"></a>

### `bt_bap_unicast_server_register()`

```c
int bt_bap_unicast_server_register ( const struct bt_bap_unicast_server_register_param * param)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注册单播服务器（Unicast Server）。

注册单播服务器（Unicast Server）。任一时刻只能注册一个单播服务器。此操作会在 GATT 数据库中注册音频流控制服务（ASCS）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | ASCS 的注册参数（Registration Parameters）。 |

**返回（Returns）**：返回值：成功返回 0，否则返回负错误码。

<a id="ga7669133936bc13f7ab38817db9ce69c0"></a>

### `bt_bap_unicast_server_register_cb()`

```c
int bt_bap_unicast_server_register_cb ( const struct bt_bap_unicast_server_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注册单播服务器回调（Unicast Server Callbacks）。

只能注册一个回调结构体（Callback Structure），尝试注册多个将导致错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 单播服务器回调结构体（Unicast Server Callback Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga6ef3b9e877ffdc04cc48fda6713a0209"></a>

### `bt_bap_unicast_server_unregister()`

```c
int bt_bap_unicast_server_unregister ( void )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注销单播服务器（Unicast Server）。

注销单播服务器（Unicast Server），这会从 GATT 数据库中注销 ASCS。调用此函数前，必须使用 `bt_bap_unicast_server_unregister_cb()` 注销通过 `bt_bap_unicast_server_register_cb()` 注册的所有回调。

调用此函数会对所有处于非空闲状态（Non-idle State）的音频流端点（ASE）发起释放操作（Release Operation）。

**返回（Returns）**：返回值：成功返回 0，否则返回负错误码。

<a id="gadf984f12bdeadcfc814dc2fc770cb7bf"></a>

### `bt_bap_unicast_server_unregister_cb()`

```c
int bt_bap_unicast_server_unregister_cb ( const struct bt_bap_unicast_server_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注销单播服务器回调（Unicast Server Callbacks）。

只能注销此前通过 `bt_bap_unicast_server_register_cb()` 注册的回调结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 单播服务器回调结构体（Unicast Server Callback Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。


## 2.5\_原页交叉引用（Cross References）

- [bt_bap_unicast_server_cb](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)
- [bt_bap_unicast_server_register_param](../bluetooth_le_audio_model_reference/P042_bt_bap_unicast_server_register_param_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [bt_bap_qos_cfg_pref](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md)
- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_警报通知服务（Alert Notification Service，ANS）.md) · [返回大纲](大纲.md) · [下一章](P003_蓝牙 Mesh 二进制大对象（BLOB）传输客户端模型 API.md)
