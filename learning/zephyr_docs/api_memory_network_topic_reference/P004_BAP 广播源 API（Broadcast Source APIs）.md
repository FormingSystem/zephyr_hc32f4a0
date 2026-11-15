---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-4
title: BAP 广播源 API（Broadcast Source APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_BAP 广播源 API（Broadcast Source APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BAP 广播源 API（Broadcast Source APIs）

<a id="details"></a>

BAP 广播源 API（Broadcast Source APIs）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_bt_5Fbap_5Fbroadcast_5Fsource_5Fcb"></a>

```c
struct bt_bap_broadcast_source_cb
```

相关声明：[bt_bap_broadcast_source_cb](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md)。

保存广播音频源（Broadcast Source）回调的结构体。

<a id="r_bt_5Fbap_5Fbroadcast_5Fsource_5Fstream_5Fparam"></a>

```c
struct bt_bap_broadcast_source_stream_param
```

相关声明：[bt_bap_broadcast_source_stream_param](../bluetooth_le_audio_model_reference/P022_bt_bap_broadcast_source_stream_param_结构体.md)。

广播音频源的流参数。

<a id="r_bt_5Fbap_5Fbroadcast_5Fsource_5Fsubgroup_5Fparam"></a>

```c
struct bt_bap_broadcast_source_subgroup_param
```

相关声明：[bt_bap_broadcast_source_subgroup_param](../bluetooth_le_audio_model_reference/P023_bt_bap_broadcast_source_subgroup_param_结构体.md)。

广播音频源的子组参数（Subgroup Parameters）。

<a id="r_bt_5Fbap_5Fbroadcast_5Fsource_5Fparam"></a>

```c
struct bt_bap_broadcast_source_param
```

相关声明：[bt_bap_broadcast_source_param](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md)。

广播音频源创建参数（Broadcast Source Create Parameters）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.2\_类型定义（Typedefs）

<a id="r_ga173ddb24e554afc1b16305cca69ad923"></a>

```c
typedef bool(* bt_bap_broadcast_source_foreach_stream_func_t) (struct bt_bap_stream *stream, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_broadcast_source_foreach_stream_func_t](#ga173ddb24e554afc1b16305cca69ad923)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

bt_bap_broadcast_source_foreach_stream() 的回调函数（Callback Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_gac75ad00b8f9a1cd7048677a33b17acda"></a>

```c
int bt_bap_broadcast_source_register_cb (struct bt_bap_broadcast_source_cb *cb)
```

相关声明：[bt_bap_broadcast_source_register_cb](#gac75ad00b8f9a1cd7048677a33b17acda)、[bt_bap_broadcast_source_cb](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md)。

注册广播源（Broadcast Sources）的回调。

<a id="r_gacc8d26c42c6b4ae6dc11af84ec4af616"></a>

```c
int bt_bap_broadcast_source_unregister_cb (struct bt_bap_broadcast_source_cb *cb)
```

相关声明：[bt_bap_broadcast_source_unregister_cb](#gacc8d26c42c6b4ae6dc11af84ec4af616)、[bt_bap_broadcast_source_cb](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md)。

注销广播源（Broadcast Sources）的回调。

<a id="r_gacdebfc435eebd47cf9cd05099a5f78e0"></a>

```c
int bt_bap_broadcast_source_create (struct bt_bap_broadcast_source_param *param, struct bt_bap_broadcast_source **source)
```

相关声明：[bt_bap_broadcast_source_create](#gacdebfc435eebd47cf9cd05099a5f78e0)、[bt_bap_broadcast_source_param](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)。

创建音频广播源（Audio Broadcast Source）。

<a id="r_gabecaa9db7be5cb03ed997ba478878d40"></a>

```c
int bt_bap_broadcast_source_reconfig (struct bt_bap_broadcast_source *source, struct bt_bap_broadcast_source_param *param)
```

相关声明：[bt_bap_broadcast_source_reconfig](#gabecaa9db7be5cb03ed997ba478878d40)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)、[bt_bap_broadcast_source_param](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md)。

重新配置音频广播源（Audio Broadcast Source）。

<a id="r_gaff2cfdadbff3ebe1e2efb660dee56f02"></a>

```c
int bt_bap_broadcast_source_update_metadata (struct bt_bap_broadcast_source *source, const uint8_t meta[], size_t meta_len)
```

相关声明：[bt_bap_broadcast_source_update_metadata](#gaff2cfdadbff3ebe1e2efb660dee56f02)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

修改音频广播源的元数据（Metadata）。

<a id="r_gac4640f5207599d51c1a63ff47f3c1d5a"></a>

```c
int bt_bap_broadcast_source_start (struct bt_bap_broadcast_source *source, struct bt_le_ext_adv *adv)
```

相关声明：[bt_bap_broadcast_source_start](#gac4640f5207599d51c1a63ff47f3c1d5a)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

启动音频广播源（Audio Broadcast Source）。

<a id="r_ga36a885581eec5cab8b3f652db19b9aba"></a>

```c
int bt_bap_broadcast_source_stop (struct bt_bap_broadcast_source *source)
```

相关声明：[bt_bap_broadcast_source_stop](#ga36a885581eec5cab8b3f652db19b9aba)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)。

停止音频广播源（Audio Broadcast Source）。

<a id="r_ga12e0a4856115a8eb297fe2d1fc130155"></a>

```c
int bt_bap_broadcast_source_delete (struct bt_bap_broadcast_source *source)
```

相关声明：[bt_bap_broadcast_source_delete](#ga12e0a4856115a8eb297fe2d1fc130155)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)。

删除音频广播源（Audio Broadcast Source）。

<a id="r_gafe07e4c6962858500fcf66415a173be8"></a>

```c
int bt_bap_broadcast_source_get_base (struct bt_bap_broadcast_source *source, struct net_buf_simple *base_buf)
```

相关声明：[bt_bap_broadcast_source_get_base](#gafe07e4c6962858500fcf66415a173be8)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

获取广播源的广播音频流端点（Broadcast Audio Stream Endpoint，BASE）。

<a id="r_ga9d543b9282e0dadca3afe3a97e385b15"></a>

```c
int bt_bap_broadcast_source_foreach_stream (struct bt_bap_broadcast_source *source, bt_bap_broadcast_source_foreach_stream_func_t func, void *user_data)
```

相关声明：[bt_bap_broadcast_source_foreach_stream](#ga9d543b9282e0dadca3afe3a97e385b15)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)、[bt_bap_broadcast_source_foreach_stream_func_t](#ga173ddb24e554afc1b16305cca69ad923)。

遍历广播源中的所有流（Streams）。

## 4.4\_详细说明（Detailed Documentation）

<a id="ga173ddb24e554afc1b16305cca69ad923"></a>

### `bt_bap_broadcast_source_foreach_stream_func_t`

```c
typedef bool(* bt_bap_broadcast_source_foreach_stream_func_t) (struct bt_bap_stream *stream, void *user_data)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

bt_bap_broadcast_source_foreach_stream() 的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 音频流（Audio Stream） |
| `user_data` | 用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 继续遍历（Continue Iterating）。 |
| `false` | 停止遍历（Stop Iterating）。 |

<a id="gacdebfc435eebd47cf9cd05099a5f78e0"></a>

### `bt_bap_broadcast_source_create()`

```c
int bt_bap_broadcast_source_create ( struct bt_bap_broadcast_source_param * param, struct bt_bap_broadcast_source ** source )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

创建音频广播源（Audio Broadcast Source）。

创建包含一个或多个音频流（Audio Streams）的新音频广播源。

调用后，扫描器即可发现广播源，设备开始广播音频公告（Audio Announcements）。

在调用 bt_bap_broadcast_source_start() 之前，不能发送音频数据，扫描器也看不到音频信息（BIGInfo）；参见 bt_le_per_adv_sync_cb。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] param` | 指向创建广播源所用参数的指针。 |
| `[out] source` | 指向已创建广播源的指针 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga12e0a4856115a8eb297fe2d1fc130155"></a>

### `bt_bap_broadcast_source_delete()`

```c
int bt_bap_broadcast_source_delete ( struct bt_bap_broadcast_source * source)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

删除音频广播源（Audio Broadcast Source）。

删除音频广播源（Audio Broadcast Source）。广播源完全停止广播，此后不可再使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 指向广播源（Broadcast Source）的指针 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga9d543b9282e0dadca3afe3a97e385b15"></a>

### `bt_bap_broadcast_source_foreach_stream()`

```c
int bt_bap_broadcast_source_foreach_stream ( struct bt_bap_broadcast_source * source, bt_bap_broadcast_source_foreach_stream_func_t func, void * user_data )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

遍历广播源中的所有流（Streams）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 广播源（Broadcast Source） |
| `func` | 回调函数。 |
| `user_data` | 发送给回调函数的用户指定数据 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功，即使广播源中没有流也视为成功。 |
| `-ECANCELED` | func 返回 false 并停止遍历。 |
| `-EINVAL` | source 或 func 为 NULL。 |

<a id="gafe07e4c6962858500fcf66415a173be8"></a>

### `bt_bap_broadcast_source_get_base()`

```c
int bt_bap_broadcast_source_get_base ( struct bt_bap_broadcast_source * source, struct net_buf_simple * base_buf )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取广播源的广播音频流端点（Broadcast Audio Stream Endpoint，BASE）。

将广播源的 BASE 编码到缓冲区，以用于广播（Advertisement）。BASE 采用小端字节序（Little-endian）编码，必须放入周期广播数据（Periodic Advertising Data）；参见 bt_le_per_adv_set_data()。

结构见基本音频规范（Basic Audio Profile）v1.0.1 表 3.15。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 指向广播源（Broadcast Source）的指针。 |
| `base_buf` | 指向将写入 BASE 的缓冲区的指针。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gabecaa9db7be5cb03ed997ba478878d40"></a>

### `bt_bap_broadcast_source_reconfig()`

```c
int bt_bap_broadcast_source_reconfig ( struct bt_bap_broadcast_source * source, struct bt_bap_broadcast_source_param * param )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

重新配置音频广播源（Audio Broadcast Source）。

使用新的编解码器及服务质量参数（Codec and Quality of Service Parameters）重新配置音频广播源。仅可在广播源停止时执行。

这可能修改广播音频源端点（Broadcast Audio Source Endpoint，BASE），因此随后应调用 bt_bap_broadcast_source_get_base() 获取新的 BASE 信息。

若 param.params_count 小于广播源已创建的子组数量，则仅更新前 param.params_count 个子组。不在 param 范围内的子组中的流保持原样，不会移除；从广播源移除流的唯一方式是重新创建广播源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 指向广播源（Broadcast Source）的指针 |
| `param` | 指向重新配置广播源所用参数的指针。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gac75ad00b8f9a1cd7048677a33b17acda"></a>

### `bt_bap_broadcast_source_register_cb()`

```c
int bt_bap_broadcast_source_register_cb ( struct bt_bap_broadcast_source_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注册广播源（Broadcast Sources）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-EEXIST` | cb 已注册时。 |

<a id="gac4640f5207599d51c1a63ff47f3c1d5a"></a>

### `bt_bap_broadcast_source_start()`

```c
int bt_bap_broadcast_source_start ( struct bt_bap_broadcast_source * source, struct bt_le_ext_adv * adv )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

启动音频广播源（Audio Broadcast Source）。

启动包含一个或多个音频流的音频广播源（Audio Broadcast Source）。广播源开始广播 BIGInfo，随后可以流式发送音频数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 指向广播源（Broadcast Source）的指针 |
| `adv` | 指向已配置周期广播（Periodic Advertising）的扩展广播集（Extended Advertising Set）的指针。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga36a885581eec5cab8b3f652db19b9aba"></a>

### `bt_bap_broadcast_source_stop()`

```c
int bt_bap_broadcast_source_stop ( struct bt_bap_broadcast_source * source)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

停止音频广播源（Audio Broadcast Source）。

停止音频广播源（Audio Broadcast Source）。停止广播 BIGInfo，随后不能再流式发送音频数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 指向广播源（Broadcast Source）的指针 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gacc8d26c42c6b4ae6dc11af84ec4af616"></a>

### `bt_bap_broadcast_source_unregister_cb()`

```c
int bt_bap_broadcast_source_unregister_cb ( struct bt_bap_broadcast_source_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注销广播源（Broadcast Sources）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-ENOENT` | cb 未注册时。 |

<a id="gaff2cfdadbff3ebe1e2efb660dee56f02"></a>

### `bt_bap_broadcast_source_update_metadata()`

```c
int bt_bap_broadcast_source_update_metadata ( struct bt_bap_broadcast_source * source, const uint8_t meta[], size_t meta_len )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

修改音频广播源的元数据（Metadata）。

修改音频广播源元数据（Metadata），仅可在广播源已启动时执行。若在停止状态更新元数据，使用 bt_bap_broadcast_source_reconfig()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 指向广播源（Broadcast Source）的指针。 |
| `meta` | 元数据（Metadata）。 |
| `meta_len` | 元数据长度。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。


## 4.5\_原页交叉引用（Cross References）

- [bt_bap_broadcast_source_cb](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md)
- [bt_bap_broadcast_source_stream_param](../bluetooth_le_audio_model_reference/P022_bt_bap_broadcast_source_stream_param_结构体.md)
- [bt_bap_broadcast_source_subgroup_param](../bluetooth_le_audio_model_reference/P023_bt_bap_broadcast_source_subgroup_param_结构体.md)
- [bt_bap_broadcast_source_param](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)
- [bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [bt_le_per_adv_sync_cb](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md)
- [bt_le_per_adv_set_data()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gafd0e7ccca93a8347a4ca6cca88e77899)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_BAP 广播 API（Broadcast APIs）.md) · [返回大纲](大纲.md) · [下一章](P005_蓝牙主机控制器接口（Bluetooth HCI）.md)
