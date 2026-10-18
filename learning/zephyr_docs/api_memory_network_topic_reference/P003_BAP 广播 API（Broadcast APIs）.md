---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-3
title: BAP 广播 API（Broadcast APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_BAP 广播 API（Broadcast APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BAP 广播 API（Broadcast APIs）

<a id="details"></a>

BAP 广播 API（Broadcast APIs）

<a id="header-groups"></a>
<a id="groups"></a>

## 3.1\_主题（Topics）

<a id="r_bt_5Fbap_5Fbroadcast_5Fsink"></a>

相关声明：[BAP 广播接收端 API（Broadcast Sink APIs）](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md)。

BAP 广播接收端 API（Broadcast Sink APIs）

<a id="r_bt_5Fbap_5Fbroadcast_5Fsource"></a>

相关声明：[BAP 广播源 API（Broadcast Source APIs）](P004_BAP 广播源 API（Broadcast Source APIs）.md)。

BAP 广播源 API（Broadcast Source APIs）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.2\_数据结构（Data Structures）

<a id="r_bt_5Fbap_5Fbase_5Fcodec_5Fid"></a>

```c
struct bt_bap_base_codec_id
```

相关声明：[bt_bap_base_codec_id](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md)。

广播音频源端点（Broadcast Audio Source Endpoint，BASE）的编解码器 ID 结构体。

<a id="r_bt_5Fbap_5Fbase_5Fsubgroup_5Fbis"></a>

```c
struct bt_bap_base_subgroup_bis
```

相关声明：[bt_bap_base_subgroup_bis](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md)。

广播音频源端点（BASE）子组中每个广播等时流（Broadcast Isochronous Stream，BIS）的结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_ga29423a39d76ad16f0586d82a23c07ba7"></a>

```c
const struct bt_bap_base * bt_bap_base_get_base_from_ad (const struct bt_data *ad)
```

相关声明：[bt_bap_base_get_base_from_ad](#ga29423a39d76ad16f0586d82a23c07ba7)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

根据周期广播数据（Periodic Advertising Data）生成指向 BASE 的指针。

<a id="r_ga539f92b71ec34f0551ef6240d83b972e"></a>

```c
int bt_bap_base_get_size (const struct bt_bap_base *base)
```

相关声明：[bt_bap_base_get_size](#ga539f92b71ec34f0551ef6240d83b972e)。

获取 BASE 的大小。

<a id="r_gaf91f45bcf7df2f368c5abeb116b65dd0"></a>

```c
int bt_bap_base_get_pres_delay (const struct bt_bap_base *base)
```

相关声明：[bt_bap_base_get_pres_delay](#gaf91f45bcf7df2f368c5abeb116b65dd0)。

获取 BASE 的呈现延迟值（Presentation Delay）。

<a id="r_gadcae0230168564da1ee8b3c577ce27d7"></a>

```c
int bt_bap_base_get_subgroup_count (const struct bt_bap_base *base)
```

相关声明：[bt_bap_base_get_subgroup_count](#gadcae0230168564da1ee8b3c577ce27d7)。

获取 BASE 的子组数量（Subgroup Count）。

<a id="r_ga6deab5a8b7a16ddf0c3685d4003694e1"></a>

```c
int bt_bap_base_get_bis_indexes (const struct bt_bap_base *base, uint32_t *bis_indexes)
```

相关声明：[bt_bap_base_get_bis_indexes](#ga6deab5a8b7a16ddf0c3685d4003694e1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 BASE 的所有广播等时流索引（BIS Indexes）。

<a id="r_ga5e6e0b758409cbdde93c0f648ef5e5e8"></a>

```c
int bt_bap_base_foreach_subgroup (const struct bt_bap_base *base, bool(*func)(const struct bt_bap_base_subgroup *subgroup, void *user_data), void *user_data)
```

相关声明：[bt_bap_base_foreach_subgroup](#ga5e6e0b758409cbdde93c0f648ef5e5e8)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

遍历 BASE 中的所有子组（Subgroups）。

<a id="r_gae75e05a002dee8336eb066ae8231ea0c"></a>

```c
int bt_bap_base_get_subgroup_codec_id (const struct bt_bap_base_subgroup *subgroup, struct bt_bap_base_codec_id *codec_id)
```

相关声明：[bt_bap_base_get_subgroup_codec_id](#gae75e05a002dee8336eb066ae8231ea0c)、[bt_bap_base_codec_id](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md)。

获取子组的编解码器 ID（Codec ID）。

<a id="r_ga10e2e32dc2802ba55d55c77148331f6a"></a>

```c
int bt_bap_base_get_subgroup_codec_data (const struct bt_bap_base_subgroup *subgroup, uint8_t **data)
```

相关声明：[bt_bap_base_get_subgroup_codec_data](#ga10e2e32dc2802ba55d55c77148331f6a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取子组的编解码器配置数据（Codec Configuration Data）。

<a id="r_gafb9d9544f38c7ad2613fff1679eb1f0c"></a>

```c
int bt_bap_base_get_subgroup_codec_meta (const struct bt_bap_base_subgroup *subgroup, uint8_t **meta)
```

相关声明：[bt_bap_base_get_subgroup_codec_meta](#gafb9d9544f38c7ad2613fff1679eb1f0c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取子组的编解码器元数据（Codec Metadata）。

<a id="r_ga920e3409f1978b803bcf6bc8d05ac8f6"></a>

```c
int bt_bap_base_subgroup_codec_to_codec_cfg (const struct bt_bap_base_subgroup *subgroup, struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_bap_base_subgroup_codec_to_codec_cfg](#ga920e3409f1978b803bcf6bc8d05ac8f6)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

将子组编解码器数据存入编解码器配置解析 API（Codec Config Parsing APIs）使用的对象。

<a id="r_ga051e1f8aa2faf3ba7a973356138fd2d3"></a>

```c
int bt_bap_base_get_subgroup_bis_count (const struct bt_bap_base_subgroup *subgroup)
```

相关声明：[bt_bap_base_get_subgroup_bis_count](#ga051e1f8aa2faf3ba7a973356138fd2d3)。

获取子组的广播等时流数量（BIS Count）。

<a id="r_ga37df3bf1e18d2d8e9388541217b2e366"></a>

```c
int bt_bap_base_subgroup_get_bis_indexes (const struct bt_bap_base_subgroup *subgroup, uint32_t *bis_indexes)
```

相关声明：[bt_bap_base_subgroup_get_bis_indexes](#ga37df3bf1e18d2d8e9388541217b2e366)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取子组的所有广播等时流索引（BIS Indexes）。

<a id="r_ga4f85ee43984cb2f3139b41da7b9b1aee"></a>

```c
int bt_bap_base_subgroup_foreach_bis (const struct bt_bap_base_subgroup *subgroup, bool(*func)(const struct bt_bap_base_subgroup_bis *bis, void *user_data), void *user_data)
```

相关声明：[bt_bap_base_subgroup_foreach_bis](#ga4f85ee43984cb2f3139b41da7b9b1aee)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_base_subgroup_bis](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md)。

遍历子组中的所有广播等时流（BIS）。

<a id="r_gaa5cb191df7807ea87f1fba1871ca8ebe"></a>

```c
int bt_bap_base_subgroup_bis_codec_to_codec_cfg (const struct bt_bap_base_subgroup_bis *bis, struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_bap_base_subgroup_bis_codec_to_codec_cfg](#gaa5cb191df7807ea87f1fba1871ca8ebe)、[bt_bap_base_subgroup_bis](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

将 BIS 编解码器配置数据存入编解码器配置解析 API（Codec Config Parsing APIs）使用的对象。

## 3.4\_详细说明（Detailed Documentation）

<a id="ga5e6e0b758409cbdde93c0f648ef5e5e8"></a>

### `bt_bap_base_foreach_subgroup()`

```c
int bt_bap_base_foreach_subgroup ( const struct bt_bap_base * base, bool(* func )(const struct bt_bap_base_subgroup *subgroup, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

遍历 BASE 中的所有子组（Subgroups）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `base` | BASE 指针 |
| `func` | 回调函数（Callback Function）；返回 true 继续遍历，返回 false 停止。 |
| `user_data` | 传给 func 的用户数据（Userdata） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `-ECANCELED` | func 提前停止子组遍历时。 |
| `0` | 已遍历所有子组时。 |

<a id="ga29423a39d76ad16f0586d82a23c07ba7"></a>

### `bt_bap_base_get_base_from_ad()`

```c
const struct bt_bap_base * bt_bap_base_get_base_from_ad ( const struct bt_data * ad)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

根据周期广播数据（Periodic Advertising Data）生成指向 BASE 的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ad` | 周期广播数据（Periodic Advertising Data） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NULL` | 数据不包含 BASE 时。 |
| `Pointer` | 指向 bt_bap_base 结构体。 |

<a id="ga6deab5a8b7a16ddf0c3685d4003694e1"></a>

### `bt_bap_base_get_bis_indexes()`

```c
int bt_bap_base_get_bis_indexes ( const struct bt_bap_base * base, uint32_t * bis_indexes )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取 BASE 的所有广播等时流索引（BIS Indexes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] base` | BASE 指针 |
| `[out] bis_indexes` | 待填充的 32 位 BIS 索引位字段（Index Bitfield） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `0` | 成功时返回。 |

<a id="gaf91f45bcf7df2f368c5abeb116b65dd0"></a>

### `bt_bap_base_get_pres_delay()`

```c
int bt_bap_base_get_pres_delay ( const struct bt_bap_base * base)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取 BASE 的呈现延迟值（Presentation Delay）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `base` | BASE 指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `The` | 24 位呈现延迟值（Presentation Delay Value） |

<a id="ga539f92b71ec34f0551ef6240d83b972e"></a>

### `bt_bap_base_get_size()`

```c
int bt_bap_base_get_size ( const struct bt_bap_base * base)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取 BASE 的大小。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `base` | BASE 指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `The` | BASE 的大小 |

<a id="ga051e1f8aa2faf3ba7a973356138fd2d3"></a>

### `bt_bap_base_get_subgroup_bis_count()`

```c
int bt_bap_base_get_subgroup_bis_count ( const struct bt_bap_base_subgroup * subgroup)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取子组的广播等时流数量（BIS Count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `subgroup` | 子组指针（Subgroup Pointer） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `The` | 8 位 BIS 数量值（Count Value） |

<a id="ga10e2e32dc2802ba55d55c77148331f6a"></a>

### `bt_bap_base_get_subgroup_codec_data()`

```c
int bt_bap_base_get_subgroup_codec_data ( const struct bt_bap_base_subgroup * subgroup, uint8_t ** data )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取子组的编解码器配置数据（Codec Configuration Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] subgroup` | 子组指针（Subgroup Pointer） |
| `[out] data` | 用于指向结果编解码器配置数据（Codec Configuration Data）的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `0` | 成功时返回。 |

<a id="gae75e05a002dee8336eb066ae8231ea0c"></a>

### `bt_bap_base_get_subgroup_codec_id()`

```c
int bt_bap_base_get_subgroup_codec_id ( const struct bt_bap_base_subgroup * subgroup, struct bt_bap_base_codec_id * codec_id )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取子组的编解码器 ID（Codec ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] subgroup` | 子组指针（Subgroup Pointer） |
| `[out] codec_id` | 指向结果存放结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `0` | 成功时返回。 |

<a id="gafb9d9544f38c7ad2613fff1679eb1f0c"></a>

### `bt_bap_base_get_subgroup_codec_meta()`

```c
int bt_bap_base_get_subgroup_codec_meta ( const struct bt_bap_base_subgroup * subgroup, uint8_t ** meta )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取子组的编解码器元数据（Codec Metadata）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] subgroup` | 子组指针（Subgroup Pointer） |
| `[out] meta` | 用于指向结果编解码器元数据（Codec Metadata）的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |

**返回（Returns）**：返回值（Returns）：成功时返回元数据长度。

<a id="gadcae0230168564da1ee8b3c577ce27d7"></a>

### `bt_bap_base_get_subgroup_count()`

```c
int bt_bap_base_get_subgroup_count ( const struct bt_bap_base * base)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取 BASE 的子组数量（Subgroup Count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `base` | BASE 指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `The` | 8 位子组数量值（Subgroup Count Value） |

<a id="gaa5cb191df7807ea87f1fba1871ca8ebe"></a>

### `bt_bap_base_subgroup_bis_codec_to_codec_cfg()`

```c
int bt_bap_base_subgroup_bis_codec_to_codec_cfg ( const struct bt_bap_base_subgroup_bis * bis, struct bt_audio_codec_cfg * codec_cfg )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

将 BIS 编解码器配置数据存入编解码器配置解析 API（Codec Config Parsing APIs）使用的对象。

此操作仅设置编解码器配置解析 API（Codec Config Parsing APIs）对象的 data 和 data_len，但有助于配合 bt_audio_codec_cfg_* 函数使用 BIS 编解码器配置数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] bis` | BIS 指针 |
| `[out] codec_cfg` | 指向结果存放结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `-ENOMEM` | codec_cfg 无法存放子组编解码器数据时。 |
| `0` | 成功时返回。 |

<a id="ga920e3409f1978b803bcf6bc8d05ac8f6"></a>

### `bt_bap_base_subgroup_codec_to_codec_cfg()`

```c
int bt_bap_base_subgroup_codec_to_codec_cfg ( const struct bt_bap_base_subgroup * subgroup, struct bt_audio_codec_cfg * codec_cfg )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

将子组编解码器数据存入编解码器配置解析 API（Codec Config Parsing APIs）使用的对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] subgroup` | 子组指针（Subgroup Pointer） |
| `[out] codec_cfg` | 指向结果存放结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `-ENOMEM` | codec_cfg 无法存放子组编解码器数据时。 |
| `0` | 成功时返回。 |

<a id="ga4f85ee43984cb2f3139b41da7b9b1aee"></a>

### `bt_bap_base_subgroup_foreach_bis()`

```c
int bt_bap_base_subgroup_foreach_bis ( const struct bt_bap_base_subgroup * subgroup, bool(* func )(const struct bt_bap_base_subgroup_bis *bis, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

遍历子组中的所有广播等时流（BIS）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `subgroup` | 子组指针（Subgroup Pointer） |
| `func` | 回调函数（Callback Function）；返回 true 继续遍历，返回 false 停止。 |
| `user_data` | 传给 func 的用户数据（Userdata） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `-ECANCELED` | func 提前停止子组遍历时。 |
| `0` | 已遍历所有 BIS 时。 |

<a id="ga37df3bf1e18d2d8e9388541217b2e366"></a>

### `bt_bap_base_subgroup_get_bis_indexes()`

```c
int bt_bap_base_subgroup_get_bis_indexes ( const struct bt_bap_base_subgroup * subgroup, uint32_t * bis_indexes )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取子组的所有广播等时流索引（BIS Indexes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] subgroup` | 子组指针（Subgroup Pointer） |
| `[out] bis_indexes` | 待填充的 32 位 BIS 索引位字段（Index Bitfield） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效时。 |
| `0` | 成功时返回。 |


## 3.5\_原页交叉引用（Cross References）

- [BAP 广播接收端 API（Broadcast Sink APIs）](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md)
- [BAP 广播源 API（Broadcast Source APIs）](P004_BAP 广播源 API（Broadcast Source APIs）.md)
- [bt_bap_base_codec_id](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md)
- [bt_bap_base_subgroup_bis](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [编解码器配置解析 API（Codec config parsing APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html)
- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_属性协议（Attribute Protocol，ATT）.md) · [返回大纲](大纲.md) · [下一章](P004_BAP 广播源 API（Broadcast Source APIs）.md)
