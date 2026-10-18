---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-4
title: 助听接入服务（Hearing Access Service，HAS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_助听接入服务（Hearing Access Service，HAS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

助听接入服务（Hearing Access Service，HAS）

<a id="details"></a>

助听接入服务（Hearing Access Service，HAS）。自 3.1 起提供（Since 3.1），版本（Version）0.8.0。此服务用于标识助听器（Hearing Aid），并可选择性地控制助听器预设（Presets）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_bt_5Fhas_5Ffeatures_5Fparam"></a>

```c
struct bt_has_features_param
```

相关声明：[bt_has_features_param](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md)。

用于注册助听接入服务（Hearing Access Service）实例特性的结构。

<a id="r_bt_5Fhas_5Fpreset_5Frecord"></a>

```c
struct bt_has_preset_record
```

相关声明：[bt_has_preset_record](../bluetooth_service_model_reference/P081_bt_has_preset_record_结构体.md)。

预设记录（Preset Record）定义。

<a id="r_bt_5Fhas_5Fclient_5Fcb"></a>

```c
struct bt_has_client_cb
```

相关声明：[bt_has_client_cb](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md)。

助听接入服务客户端（Hearing Access Service Client）的回调结构。

<a id="r_bt_5Fhas_5Fpreset_5Fops"></a>

```c
struct bt_has_preset_ops
```

相关声明：[bt_has_preset_ops](../bluetooth_service_model_reference/P080_bt_has_preset_ops_结构体.md)。

预设操作（Preset Operations）结构。

<a id="r_bt_5Fhas_5Fpreset_5Fregister_5Fparam"></a>

```c
struct bt_has_preset_register_param
```

相关声明：[bt_has_preset_register_param](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md)。

预设（Preset）的注册结构。

<a id="r_bt_5Fhas"></a>

```c
struct bt_has
```

相关声明：[bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)。

不透明的助听接入服务（Hearing Access Service）对象。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_gacbc29958c09b26a81e02893cd5914074"></a>

```c
#define BT_HAS_PRESET_NAME_MIN 1U
```

相关声明：[BT_HAS_PRESET_NAME_MIN](#gacbc29958c09b26a81e02893cd5914074)。

预设名称（Preset Name）的最小长度。

<a id="r_gae133807f12d0d7a1ecd1f8dda24c7f09"></a>

```c
#define BT_HAS_PRESET_NAME_MAX 40U
```

相关声明：[BT_HAS_PRESET_NAME_MAX](#gae133807f12d0d7a1ecd1f8dda24c7f09)。

预设名称（Preset Name）的最大长度。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_gaf83c83d9f2c9575e48455b975c4266ce"></a>

```c
typedef bool(* bt_has_preset_func_t) (uint8_t index, enum bt_has_properties properties, const char *name, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_has_preset_func_t](#gaf83c83d9f2c9575e48455b975c4266ce)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_has_properties](#ga7b8913a9f9bc4d5c066582780adcf274)。

预设迭代器回调（Preset Iterator Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.4\_枚举（Enumerations）

<a id="r_gaa9572a32f912c8fe529b510aa23f4540"></a>

```c
enum bt_has_hearing_aid_type { BT_HAS_HEARING_AID_TYPE_BINAURAL = 0x00 , BT_HAS_HEARING_AID_TYPE_MONAURAL = 0x01 , BT_HAS_HEARING_AID_TYPE_BANDED = 0x02 }
```

相关声明：[bt_has_hearing_aid_type](#gaa9572a32f912c8fe529b510aa23f4540)、[BT_HAS_HEARING_AID_TYPE_BINAURAL](#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c)、[BT_HAS_HEARING_AID_TYPE_MONAURAL](#ggaa9572a32f912c8fe529b510aa23f4540a4b711ff711e81a22b7e80f7dc8a4aae8)、[BT_HAS_HEARING_AID_TYPE_BANDED](#ggaa9572a32f912c8fe529b510aa23f4540af9e7c56173aeeb593f9e12a0e3366a0b)。

助听器设备类型（Hearing Aid Device Type）。

<a id="r_ga7b8913a9f9bc4d5c066582780adcf274"></a>

```c
enum bt_has_properties { BT_HAS_PROP_NONE = 0 , BT_HAS_PROP_WRITABLE = (1UL << (0U)) , BT_HAS_PROP_AVAILABLE = (1UL << (1U)) }
```

相关声明：[bt_has_properties](#ga7b8913a9f9bc4d5c066582780adcf274)、[BT_HAS_PROP_NONE](#gga7b8913a9f9bc4d5c066582780adcf274a70645a9bfc628425b93b0aa6ce539173)、[BT_HAS_PROP_WRITABLE](#gga7b8913a9f9bc4d5c066582780adcf274ad479ec0e277e2e894d0056965b484e09)、[BT_HAS_PROP_AVAILABLE](#gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59)。

预设属性值（Preset Properties Values）。

<a id="r_ga50d470390967317cb84b17fd450546a4"></a>

```c
enum bt_has_capabilities { BT_HAS_PRESET_SUPPORT = (1UL << (0U)) }
```

相关声明：[bt_has_capabilities](#ga50d470390967317cb84b17fd450546a4)、[BT_HAS_PRESET_SUPPORT](#gga50d470390967317cb84b17fd450546a4a885520fe7fa533b6ea79db7ebeeed258)。

助听器设备能力（Hearing Aid Device Capabilities）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.5\_函数（Functions）

<a id="r_ga9bc61dfc710070fb136120944c0776b9"></a>

```c
int bt_has_client_cb_register (const struct bt_has_client_cb *cb)
```

相关声明：[bt_has_client_cb_register](#ga9bc61dfc710070fb136120944c0776b9)、[bt_has_client_cb](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md)。

注册听力接入服务（Hearing Access Service）客户端使用的回调。

<a id="r_gaf3765300072b0a6d1ee45699e710d4da"></a>

```c
int bt_has_client_discover (struct bt_conn *conn)
```

相关声明：[bt_has_client_discover](#gaf3765300072b0a6d1ee45699e710d4da)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现远端设备上的听力接入服务（Hearing Access Service）。

<a id="r_ga8303b5fb2558a35bb2cb06cd5788e636"></a>

```c
int bt_has_client_conn_get (const struct bt_has *has, struct bt_conn **conn)
```

相关声明：[bt_has_client_conn_get](#ga8303b5fb2558a35bb2cb06cd5788e636)、[bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取服务对象的蓝牙连接对象（Bluetooth Connection Object）。

<a id="r_ga54ef9918e4fb458b7416ffb94acca808"></a>

```c
int bt_has_client_presets_read (struct bt_has *has, uint8_t index, uint8_t max_count)
```

相关声明：[bt_has_client_presets_read](#ga54ef9918e4fb458b7416ffb94acca808)、[bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取预设记录（Preset Records）。

<a id="r_ga4a228ee29a26346867a6427f81816336"></a>

```c
int bt_has_client_preset_set (struct bt_has *has, uint8_t index, bool sync)
```

相关声明：[bt_has_client_preset_set](#ga4a228ee29a26346867a6427f81816336)、[bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置活动预设（Active Preset）。

<a id="r_ga66943cb5275ca660f2eab11e37708d81"></a>

```c
int bt_has_client_preset_next (struct bt_has *has, bool sync)
```

相关声明：[bt_has_client_preset_next](#ga66943cb5275ca660f2eab11e37708d81)、[bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

激活下一个预设（Preset）。

<a id="r_ga3a564b18ce6cbc7a5af970474ddf25a2"></a>

```c
int bt_has_client_preset_prev (struct bt_has *has, bool sync)
```

相关声明：[bt_has_client_preset_prev](#ga3a564b18ce6cbc7a5af970474ddf25a2)、[bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

激活上一个预设（Preset）。

<a id="r_gac39ca2d72273bd591618d186b48c20b0"></a>

```c
int bt_has_register (const struct bt_has_features_param *features)
```

相关声明：[bt_has_register](#gac39ca2d72273bd591618d186b48c20b0)、[bt_has_features_param](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md)。

注册听力接入服务（Hearing Access Service）实例。

<a id="r_gadf0a488721910633fa2b54b2c7645bd9"></a>

```c
int bt_has_preset_register (const struct bt_has_preset_register_param *param)
```

相关声明：[bt_has_preset_register](#gadf0a488721910633fa2b54b2c7645bd9)、[bt_has_preset_register_param](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md)。

注册预设（Preset）。

<a id="r_ga39f9ac2f94b1febe8e834ae54e110e90"></a>

```c
int bt_has_preset_unregister (uint8_t index)
```

相关声明：[bt_has_preset_unregister](#ga39f9ac2f94b1febe8e834ae54e110e90)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

注销预设（Preset）。

<a id="r_gacaa997913949b6ea98c5c6233fefdc52"></a>

```c
int bt_has_preset_available (uint8_t index)
```

相关声明：[bt_has_preset_available](#gacaa997913949b6ea98c5c6233fefdc52)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将预设（Preset）设为可用。

<a id="r_gabe523e1aefc789ad0031e3c0efb27379"></a>

```c
int bt_has_preset_unavailable (uint8_t index)
```

相关声明：[bt_has_preset_unavailable](#gabe523e1aefc789ad0031e3c0efb27379)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将预设（Preset）设为不可用。

<a id="r_ga0bf932a9a1977e4d1926c11242c7b70d"></a>

```c
int bt_has_preset_foreach (uint8_t index, bt_has_preset_func_t func, void *user_data)
```

相关声明：[bt_has_preset_foreach](#ga0bf932a9a1977e4d1926c11242c7b70d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_has_preset_func_t](#gaf83c83d9f2c9575e48455b975c4266ce)。

预设迭代器（Preset Iterator）。

<a id="r_ga2c0fe62baa63b72703d6f553f1de072b"></a>

```c
int bt_has_preset_active_set (uint8_t index)
```

相关声明：[bt_has_preset_active_set](#ga2c0fe62baa63b72703d6f553f1de072b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置活动预设（Active Preset）。

<a id="r_gae1787671fac3b7873c5994adc7d19b20"></a>

```c
uint8_t bt_has_preset_active_get (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_has_preset_active_get](#gae1787671fac3b7873c5994adc7d19b20)。

获取活动预设（Active Preset）。

<a id="r_ga715cfe5bd08fbd4557ee6052b38f27de"></a>

```c
static int bt_has_preset_active_clear (void)
```

相关声明：[bt_has_preset_active_clear](#ga715cfe5bd08fbd4557ee6052b38f27de)。

清除活动预设（Active Preset）。

<a id="r_ga6f06adc529a500fcfcfea2ae89ea60d5"></a>

```c
int bt_has_preset_name_change (uint8_t index, const char *name)
```

相关声明：[bt_has_preset_name_change](#ga6f06adc529a500fcfcfea2ae89ea60d5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更改预设名称（Preset Name）。

<a id="r_ga7e37a89b1bf0a732045276cf6b922956"></a>

```c
int bt_has_features_set (const struct bt_has_features_param *features)
```

相关声明：[bt_has_features_set](#ga7e37a89b1bf0a732045276cf6b922956)、[bt_has_features_param](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md)。

更改助听器特性（Hearing Aid Features）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 4.6\_预设索引定义（Preset Index Definitions）

<a id="r_ga462679b8b5c91762c6d1daf03c5675d0"></a>

```c
#define BT_HAS_PRESET_INDEX_NONE 0x00U
```

相关声明：[BT_HAS_PRESET_INDEX_NONE](#ga462679b8b5c91762c6d1daf03c5675d0)。

无索引（No Index）。

<a id="r_ga38df8301e78111dc1e6241594a9bf8c3"></a>

```c
#define BT_HAS_PRESET_INDEX_FIRST 0x01U
```

相关声明：[BT_HAS_PRESET_INDEX_FIRST](#ga38df8301e78111dc1e6241594a9bf8c3)。

首个预设索引（Preset Index）。

<a id="r_ga2e1b80739eeb56d8e0b7779c3d488faa"></a>

```c
#define BT_HAS_PRESET_INDEX_LAST 0xFFU
```

相关声明：[BT_HAS_PRESET_INDEX_LAST](#ga2e1b80739eeb56d8e0b7779c3d488faa)。

最后一个预设索引（Preset Index）。

## 4.7\_详细说明（Detailed Documentation）

<a id="ga38df8301e78111dc1e6241594a9bf8c3"></a>

### `BT_HAS_PRESET_INDEX_FIRST`

```c
#define BT_HAS_PRESET_INDEX_FIRST 0x01U
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

首个预设索引（Preset Index）。

<a id="ga2e1b80739eeb56d8e0b7779c3d488faa"></a>

### `BT_HAS_PRESET_INDEX_LAST`

```c
#define BT_HAS_PRESET_INDEX_LAST 0xFFU
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

最后一个预设索引（Preset Index）。

<a id="ga462679b8b5c91762c6d1daf03c5675d0"></a>

### `BT_HAS_PRESET_INDEX_NONE`

```c
#define BT_HAS_PRESET_INDEX_NONE 0x00U
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

无索引（No Index）。

<a id="gae133807f12d0d7a1ecd1f8dda24c7f09"></a>

### `BT_HAS_PRESET_NAME_MAX`

```c
#define BT_HAS_PRESET_NAME_MAX 40U
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

预设名称（Preset Name）的最大长度。

<a id="gacbc29958c09b26a81e02893cd5914074"></a>

### `BT_HAS_PRESET_NAME_MIN`

```c
#define BT_HAS_PRESET_NAME_MIN 1U
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

预设名称（Preset Name）的最小长度。

<a id="gaf83c83d9f2c9575e48455b975c4266ce"></a>

### `bt_has_preset_func_t`

```c
typedef bool(* bt_has_preset_func_t) (uint8_t index, enum bt_has_properties properties, const char *name, void *user_data)
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

预设迭代器回调（Preset Iterator Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 找到的预设索引（Preset Index）。 |
| `properties` | 预设属性（Preset properties）。 |
| `name` | 预设名称（Preset name）。 |
| `user_data` | 所给数据（Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 继续遍历（Continue Iterating）。 |
| `false` | 停止遍历（Stop Iterating）。 |

<a id="ga50d470390967317cb84b17fd450546a4"></a>

### `bt_has_capabilities`

```c
enum bt_has_capabilities
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

助听器设备能力（Hearing Aid Device Capabilities）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_HAS_PRESET_SUPPORT` | 指示支持预设（Presets）。 |

<a id="gaa9572a32f912c8fe529b510aa23f4540"></a>

### `bt_has_hearing_aid_type`

```c
enum bt_has_hearing_aid_type
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

助听器设备类型（Hearing Aid Device Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_HAS_HEARING_AID_TYPE_BINAURAL` | 组成协调集合（Coordinated Set）的两个助听器，分别用于用户的右耳和左耳，通常供双侧听力损失（Bilateral Hearing Loss）的用户使用。 |
| `BT_HAS_HEARING_AID_TYPE_MONAURAL` | 用于左耳或右耳的单个助听器（Single Hearing Aid），通常供单侧听力损失（Unilateral Hearing Loss）的用户使用。 |
| `BT_HAS_HEARING_AID_TYPE_BANDED` | 彼此相连并对外提供单一蓝牙无线接口（Bluetooth Radio Interface）的两个助听器。 |

<a id="ga7b8913a9f9bc4d5c066582780adcf274"></a>

### `bt_has_properties`

```c
enum bt_has_properties
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

预设属性值（Preset Properties Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_HAS_PROP_NONE` | 未设置任何属性（Properties）。 |
| `BT_HAS_PROP_WRITABLE` | 客户端可以写入预设名称（Preset Name）。 |
| `BT_HAS_PROP_AVAILABLE` | 预设可用性（Preset Availability）。 |

<a id="ga9bc61dfc710070fb136120944c0776b9"></a>

### `bt_has_client_cb_register()`

```c
int bt_has_client_cb_register ( const struct bt_has_client_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

注册听力接入服务（Hearing Access Service）客户端使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（callback structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga8303b5fb2558a35bb2cb06cd5788e636"></a>

### `bt_has_client_conn_get()`

```c
int bt_has_client_conn_get ( const struct bt_has * has, struct bt_conn ** conn )
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

获取服务对象的蓝牙连接对象（Bluetooth Connection Object）。

调用者获得连接对象（Connection Object）的一个新引用；使用完该对象后，必须通过 bt_conn_unref() 释放该引用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] has` | 指向听觉接入服务对象（Hearing Access Service object）的指针。 |
| `[out] conn` | 连接对象（Connection Object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaf3765300072b0a6d1ee45699e710d4da"></a>

### `bt_has_client_discover()`

```c
int bt_has_client_discover ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

发现远端设备上的听力接入服务（Hearing Access Service）。

客户端方法，用于在 conn 标识的服务器上查找助听接入服务（Hearing Access Service）。发现过程（Discovery Procedure）完成时，将调用 bt_has_client_cb::discover 回调，向用户提供 HAS 对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga66943cb5275ca660f2eab11e37708d81"></a>

### `bt_has_client_preset_next()`

```c
int bt_has_client_preset_next ( struct bt_has * has, bool sync )
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

激活下一个预设（Preset）。

客户端过程，将下一个可用预设（Preset）设为活动预设。状态通过 bt_has_client_cb::preset_switch 回调返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `has` | 指向听觉接入服务对象（Hearing Access Service object）的指针。 |
| `sync` | 请求在集合中同步活动预设（Active Preset Synchronization）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga3a564b18ce6cbc7a5af970474ddf25a2"></a>

### `bt_has_client_preset_prev()`

```c
int bt_has_client_preset_prev ( struct bt_has * has, bool sync )
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

激活上一个预设（Preset）。

客户端过程，将上一个可用预设（Preset）设为活动预设。状态通过 bt_has_client_cb::preset_switch 回调返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `has` | 指向听觉接入服务对象（Hearing Access Service object）的指针。 |
| `sync` | 请求在集合中同步活动预设（Active Preset Synchronization）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga4a228ee29a26346867a6427f81816336"></a>

### `bt_has_client_preset_set()`

```c
int bt_has_client_preset_set ( struct bt_has * has, uint8_t index, bool sync )
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

设置活动预设（Active Preset）。

客户端过程，将 index 标识的预设（Preset）设为活动预设。状态通过 bt_has_client_cb::preset_switch 回调返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `has` | 指向听觉接入服务对象（Hearing Access Service object）的指针。 |
| `index` | 要激活的预设索引（Preset Index）。 |
| `sync` | 请求在集合中同步活动预设（Active Preset Synchronization）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga54ef9918e4fb458b7416ffb94acca808"></a>

### `bt_has_client_presets_read()`

```c
int bt_has_client_presets_read ( struct bt_has * has, uint8_t index, uint8_t max_count )
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

读取预设记录（Preset Records）。

客户端方法，从给定索引起最多读取 max_count 个预设（Presets）。通过 bt_has_client_cb::preset_read_rsp 回调返回预设记录，每个预设调用一次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `has` | 指向听觉接入服务对象（Hearing Access Service object）的指针。 |
| `index` | 起始索引（Starting Index）。 |
| `max_count` | 最多读取的预设数量（Maximum Number of Presets）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga7e37a89b1bf0a732045276cf6b922956"></a>

### `bt_has_features_set()`

```c
int bt_has_features_set ( const struct bt_has_features_param * features)
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

更改助听器特性（Hearing Aid Features）。

更改助听器特性（Hearing Aid Features）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `features` | 要设置的特性（Features）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga715cfe5bd08fbd4557ee6052b38f27de"></a>

### `bt_has_preset_active_clear()`

```c
int bt_has_preset_active_clear ( void )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/audio/has.h>
```

清除活动预设（Active Preset）。

供服务器停用当前活动预设（Active Preset）使用。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gae1787671fac3b7873c5994adc7d19b20"></a>

### `bt_has_preset_active_get()`

```c
uint8_t bt_has_preset_active_get ( void )
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

获取活动预设（Active Preset）。

用于获取当前活动预设索引（Active Preset Index）的函数。

返回（Returns）：活动预设索引（Active Preset Index）。

<a id="ga2c0fe62baa63b72703d6f553f1de072b"></a>

### `bt_has_preset_active_set()`

```c
int bt_has_preset_active_set ( uint8_t index)
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

设置活动预设（Active Preset）。

用于将 index 标识的预设设为活动预设（Active Preset）的函数。该预设索引将通知给对端设备（Peer Devices）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 预设索引（Preset index）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gacaa997913949b6ea98c5c6233fefdc52"></a>

### `bt_has_preset_available()`

```c
int bt_has_preset_available ( uint8_t index)
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

将预设（Preset）设为可用。

设置 BT_HAS_PROP_AVAILABLE 属性位，将预设可用性（Preset Availability）通知给对端设备。只有可用预设才能被选为活动预设（Active Preset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 已变为可用的预设索引（Preset Index）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga0bf932a9a1977e4d1926c11242c7b70d"></a>

### `bt_has_preset_foreach()`

```c
int bt_has_preset_foreach ( uint8_t index, bt_has_preset_func_t func, void * user_data )
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

预设迭代器（Preset Iterator）。

遍历预设（Presets）；如果给定非零索引，还可按该索引匹配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 预设索引（Preset Index）；传入 BT_HAS_PRESET_INDEX_NONE 可跳过索引匹配。 |
| `func` | 回调函数（Callback function）。 |
| `user_data` | 传给回调（Callback）的数据。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ECANCELED` | 遍历尚未完成便被回调函数（Callback Function）停止。 |
| `-EINVAL` | func 为 NULL。 |

<a id="ga6f06adc529a500fcfcfea2ae89ea60d5"></a>

### `bt_has_preset_name_change()`

```c
int bt_has_preset_name_change ( uint8_t index, const char * name )
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

更改预设名称（Preset Name）。

更改 index 标识的预设名称（Preset Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 要更改名称的预设索引（Preset Index）。 |
| `name` | 要写入的名称（Name）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gadf0a488721910633fa2b54b2c7645bd9"></a>

### `bt_has_preset_register()`

```c
int bt_has_preset_register ( const struct bt_has_preset_register_param * param)
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

注册预设（Preset）。

注册预设（Register Preset），将其加入对外公开的预设记录列表。CONFIG_BT_HAS_PRESET_COUNT 非零时，可链接此符号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 预设注册参数（Preset Registration Parameter）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gabe523e1aefc789ad0031e3c0efb27379"></a>

### `bt_has_preset_unavailable()`

```c
int bt_has_preset_unavailable ( uint8_t index)
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

将预设（Preset）设为不可用。

清除 BT_HAS_PROP_AVAILABLE 属性位，将预设可用性（Preset Availability）通知给对端设备。不可用预设不能被选为活动预设（Active Preset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 已变为不可用的预设索引（Preset Index）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga39f9ac2f94b1febe8e834ae54e110e90"></a>

### `bt_has_preset_unregister()`

```c
int bt_has_preset_unregister ( uint8_t index)
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

注销预设（Preset）。

注销预设（Unregister Preset），将其从预设记录列表移除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 请求注销的预设索引（Preset Index）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gac39ca2d72273bd591618d186b48c20b0"></a>

### `bt_has_register()`

```c
int bt_has_register ( const struct bt_has_features_param * features)
```

```c
#include <zephyr/bluetooth/audio/has.h>
```

注册听力接入服务（Hearing Access Service）实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `features` | 助听接入服务注册参数（Hearing Access Service Register Parameters）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。


## 4.8\_原页交叉引用（Cross References）

- [bt_has_features_param](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md)
- [bt_has_preset_record](../bluetooth_service_model_reference/P081_bt_has_preset_record_结构体.md)
- [bt_has_client_cb](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md)
- [bt_has_preset_ops](../bluetooth_service_model_reference/P080_bt_has_preset_ops_结构体.md)
- [bt_has_preset_register_param](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md)
- [bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/audio/has.h](../api_file_audio_gateway_reference/P017_zephyr__bluetooth__audio__has.h_文件参考.md)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [bt_conn_unref()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b18c6b22a9f02be0d7d078b2ce51ff6)
- [bt_has_client_cb::discover](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#acf35d62cce0c2181e2eefd8c43e3b568)
- [助听接入服务（Hearing Access Service，HAS）](P004_助听接入服务（Hearing Access Service，HAS）.md)
- [bt_has_client_cb::preset_switch](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#a4217754818ad047f287aceda8326bf99)
- [bt_has_client_cb::preset_read_rsp](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md#a50759c76add5f4f76e23e742ae3ebe1b)
- [CONFIG_BT_HAS_PRESET_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HAS_PRESET_COUNT)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga50d470390967317cb84b17fd450546a4a885520fe7fa533b6ea79db7ebeeed258"></a>
<a id="ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c"></a>
<a id="ggaa9572a32f912c8fe529b510aa23f4540a4b711ff711e81a22b7e80f7dc8a4aae8"></a>
<a id="ggaa9572a32f912c8fe529b510aa23f4540af9e7c56173aeeb593f9e12a0e3366a0b"></a>
<a id="gga7b8913a9f9bc4d5c066582780adcf274a70645a9bfc628425b93b0aa6ce539173"></a>
<a id="gga7b8913a9f9bc4d5c066582780adcf274ad479ec0e277e2e894d0056965b484e09"></a>
<a id="gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_CCP 呼叫控制服务器 API.md) · [返回大纲](大纲.md) · [下一章](P005_子网配置（Subnet Configuration）.md)
