---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-17
title: zephyr__bluetooth__audio__has.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/has_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_bluetooth\_\_audio\_\_has.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/has_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙助听接入服务（Hearing Access Service，HAS）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

蓝牙助听接入服务（Hearing Access Service，HAS）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.2\_宏定义（Macros）

<a id="r_gacbc29958c09b26a81e02893cd5914074"></a>

```c
#define BT_HAS_PRESET_NAME_MIN 1U
```

相关声明：[BT_HAS_PRESET_NAME_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gacbc29958c09b26a81e02893cd5914074)。

预设名称（Preset Name）的最小长度。

<a id="r_gae133807f12d0d7a1ecd1f8dda24c7f09"></a>

```c
#define BT_HAS_PRESET_NAME_MAX 40U
```

相关声明：[BT_HAS_PRESET_NAME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gae133807f12d0d7a1ecd1f8dda24c7f09)。

预设名称（Preset Name）的最大长度。

<a id="define-members-0"></a>

### 预设索引定义（Preset Index Definitions）

<a id="r_ga462679b8b5c91762c6d1daf03c5675d0"></a>

```c
#define BT_HAS_PRESET_INDEX_NONE 0x00U
```

相关声明：[BT_HAS_PRESET_INDEX_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga462679b8b5c91762c6d1daf03c5675d0)。

无索引（No Index）。

<a id="r_ga38df8301e78111dc1e6241594a9bf8c3"></a>

```c
#define BT_HAS_PRESET_INDEX_FIRST 0x01U
```

相关声明：[BT_HAS_PRESET_INDEX_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga38df8301e78111dc1e6241594a9bf8c3)。

首个预设索引（Preset Index）。

<a id="r_ga2e1b80739eeb56d8e0b7779c3d488faa"></a>

```c
#define BT_HAS_PRESET_INDEX_LAST 0xFFU
```

相关声明：[BT_HAS_PRESET_INDEX_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga2e1b80739eeb56d8e0b7779c3d488faa)。

最后一个预设索引（Preset Index）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 17.3\_类型定义（Typedefs）

<a id="r_gaf83c83d9f2c9575e48455b975c4266ce"></a>

```c
typedef bool(* bt_has_preset_func_t) (uint8_t index, enum bt_has_properties properties, const char *name, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_has_preset_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaf83c83d9f2c9575e48455b975c4266ce)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_has_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga7b8913a9f9bc4d5c066582780adcf274)。

预设迭代器回调（Preset Iterator Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.4\_枚举（Enumerations）

<a id="r_gaa9572a32f912c8fe529b510aa23f4540"></a>

```c
enum bt_has_hearing_aid_type { BT_HAS_HEARING_AID_TYPE_BINAURAL = 0x00 , BT_HAS_HEARING_AID_TYPE_MONAURAL = 0x01 , BT_HAS_HEARING_AID_TYPE_BANDED = 0x02 }
```

相关声明：[bt_has_hearing_aid_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaa9572a32f912c8fe529b510aa23f4540)、[BT_HAS_HEARING_AID_TYPE_BINAURAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c)、[BT_HAS_HEARING_AID_TYPE_MONAURAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ggaa9572a32f912c8fe529b510aa23f4540a4b711ff711e81a22b7e80f7dc8a4aae8)、[BT_HAS_HEARING_AID_TYPE_BANDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ggaa9572a32f912c8fe529b510aa23f4540af9e7c56173aeeb593f9e12a0e3366a0b)。

助听器设备类型（Hearing Aid Device Type）。

<a id="r_ga7b8913a9f9bc4d5c066582780adcf274"></a>

```c
enum bt_has_properties { BT_HAS_PROP_NONE = 0 , BT_HAS_PROP_WRITABLE = (1UL << (0U)) , BT_HAS_PROP_AVAILABLE = (1UL << (1U)) }
```

相关声明：[bt_has_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga7b8913a9f9bc4d5c066582780adcf274)、[BT_HAS_PROP_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga7b8913a9f9bc4d5c066582780adcf274a70645a9bfc628425b93b0aa6ce539173)、[BT_HAS_PROP_WRITABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga7b8913a9f9bc4d5c066582780adcf274ad479ec0e277e2e894d0056965b484e09)、[BT_HAS_PROP_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59)。

预设属性值（Preset Properties Values）。

<a id="r_ga50d470390967317cb84b17fd450546a4"></a>

```c
enum bt_has_capabilities { BT_HAS_PRESET_SUPPORT = (1UL << (0U)) }
```

相关声明：[bt_has_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga50d470390967317cb84b17fd450546a4)、[BT_HAS_PRESET_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga50d470390967317cb84b17fd450546a4a885520fe7fa533b6ea79db7ebeeed258)。

助听器设备能力（Hearing Aid Device Capabilities）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.5\_函数（Functions）

<a id="r_ga9bc61dfc710070fb136120944c0776b9"></a>

```c
int bt_has_client_cb_register (const struct bt_has_client_cb *cb)
```

相关声明：[bt_has_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga9bc61dfc710070fb136120944c0776b9)、[bt_has_client_cb](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md)。

注册听力接入服务（Hearing Access Service）客户端使用的回调。

<a id="r_gaf3765300072b0a6d1ee45699e710d4da"></a>

```c
int bt_has_client_discover (struct bt_conn *conn)
```

相关声明：[bt_has_client_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaf3765300072b0a6d1ee45699e710d4da)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现远端设备上的听力接入服务（Hearing Access Service）。

<a id="r_ga8303b5fb2558a35bb2cb06cd5788e636"></a>

```c
int bt_has_client_conn_get (const struct bt_has *has, struct bt_conn **conn)
```

相关声明：[bt_has_client_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga8303b5fb2558a35bb2cb06cd5788e636)、[bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取服务对象的蓝牙连接对象（Bluetooth Connection Object）。

<a id="r_ga54ef9918e4fb458b7416ffb94acca808"></a>

```c
int bt_has_client_presets_read (struct bt_has *has, uint8_t index, uint8_t max_count)
```

相关声明：[bt_has_client_presets_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga54ef9918e4fb458b7416ffb94acca808)、[bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取预设记录（Preset Records）。

<a id="r_ga4a228ee29a26346867a6427f81816336"></a>

```c
int bt_has_client_preset_set (struct bt_has *has, uint8_t index, bool sync)
```

相关声明：[bt_has_client_preset_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga4a228ee29a26346867a6427f81816336)、[bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置活动预设（Active Preset）。

<a id="r_ga66943cb5275ca660f2eab11e37708d81"></a>

```c
int bt_has_client_preset_next (struct bt_has *has, bool sync)
```

相关声明：[bt_has_client_preset_next](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga66943cb5275ca660f2eab11e37708d81)、[bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

激活下一个预设（Preset）。

<a id="r_ga3a564b18ce6cbc7a5af970474ddf25a2"></a>

```c
int bt_has_client_preset_prev (struct bt_has *has, bool sync)
```

相关声明：[bt_has_client_preset_prev](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga3a564b18ce6cbc7a5af970474ddf25a2)、[bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

激活上一个预设（Preset）。

<a id="r_gac39ca2d72273bd591618d186b48c20b0"></a>

```c
int bt_has_register (const struct bt_has_features_param *features)
```

相关声明：[bt_has_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gac39ca2d72273bd591618d186b48c20b0)、[bt_has_features_param](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md)。

注册听力接入服务（Hearing Access Service）实例。

<a id="r_gadf0a488721910633fa2b54b2c7645bd9"></a>

```c
int bt_has_preset_register (const struct bt_has_preset_register_param *param)
```

相关声明：[bt_has_preset_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gadf0a488721910633fa2b54b2c7645bd9)、[bt_has_preset_register_param](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md)。

注册预设（Preset）。

<a id="r_ga39f9ac2f94b1febe8e834ae54e110e90"></a>

```c
int bt_has_preset_unregister (uint8_t index)
```

相关声明：[bt_has_preset_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga39f9ac2f94b1febe8e834ae54e110e90)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

注销预设（Preset）。

<a id="r_gacaa997913949b6ea98c5c6233fefdc52"></a>

```c
int bt_has_preset_available (uint8_t index)
```

相关声明：[bt_has_preset_available](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gacaa997913949b6ea98c5c6233fefdc52)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将预设（Preset）设为可用。

<a id="r_gabe523e1aefc789ad0031e3c0efb27379"></a>

```c
int bt_has_preset_unavailable (uint8_t index)
```

相关声明：[bt_has_preset_unavailable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gabe523e1aefc789ad0031e3c0efb27379)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将预设（Preset）设为不可用。

<a id="r_ga0bf932a9a1977e4d1926c11242c7b70d"></a>

```c
int bt_has_preset_foreach (uint8_t index, bt_has_preset_func_t func, void *user_data)
```

相关声明：[bt_has_preset_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga0bf932a9a1977e4d1926c11242c7b70d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_has_preset_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaf83c83d9f2c9575e48455b975c4266ce)。

预设迭代器（Preset Iterator）。

<a id="r_ga2c0fe62baa63b72703d6f553f1de072b"></a>

```c
int bt_has_preset_active_set (uint8_t index)
```

相关声明：[bt_has_preset_active_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga2c0fe62baa63b72703d6f553f1de072b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置活动预设（Active Preset）。

<a id="r_gae1787671fac3b7873c5994adc7d19b20"></a>

```c
uint8_t bt_has_preset_active_get (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_has_preset_active_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gae1787671fac3b7873c5994adc7d19b20)。

获取活动预设（Active Preset）。

<a id="r_ga715cfe5bd08fbd4557ee6052b38f27de"></a>

```c
static int bt_has_preset_active_clear (void)
```

相关声明：[bt_has_preset_active_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga715cfe5bd08fbd4557ee6052b38f27de)。

清除活动预设（Active Preset）。

<a id="r_ga6f06adc529a500fcfcfea2ae89ea60d5"></a>

```c
int bt_has_preset_name_change (uint8_t index, const char *name)
```

相关声明：[bt_has_preset_name_change](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga6f06adc529a500fcfcfea2ae89ea60d5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更改预设名称（Preset Name）。

<a id="r_ga7e37a89b1bf0a732045276cf6b922956"></a>

```c
int bt_has_features_set (const struct bt_has_features_param *features)
```

相关声明：[bt_has_features_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga7e37a89b1bf0a732045276cf6b922956)、[bt_has_features_param](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md)。

更改助听器特性（Hearing Aid Features）。


## 17.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P306_has.h_源码浏览.md)
- [bt_has_features_param](../bluetooth_service_model_reference/P079_bt_has_features_param_结构体.md)
- [bt_has_preset_record](../bluetooth_service_model_reference/P081_bt_has_preset_record_结构体.md)
- [bt_has_client_cb](../bluetooth_service_model_reference/P078_bt_has_client_cb_结构体.md)
- [bt_has_preset_ops](../bluetooth_service_model_reference/P080_bt_has_preset_ops_结构体.md)
- [bt_has_preset_register_param](../bluetooth_service_model_reference/P082_bt_has_preset_register_param_结构体.md)
- [BT_HAS_PRESET_NAME_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gacbc29958c09b26a81e02893cd5914074)
- [BT_HAS_PRESET_NAME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gae133807f12d0d7a1ecd1f8dda24c7f09)
- [BT_HAS_PRESET_INDEX_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga462679b8b5c91762c6d1daf03c5675d0)
- [BT_HAS_PRESET_INDEX_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga38df8301e78111dc1e6241594a9bf8c3)
- [BT_HAS_PRESET_INDEX_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga2e1b80739eeb56d8e0b7779c3d488faa)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_has_preset_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaf83c83d9f2c9575e48455b975c4266ce)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_has_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga7b8913a9f9bc4d5c066582780adcf274)
- [bt_has_hearing_aid_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaa9572a32f912c8fe529b510aa23f4540)
- [BT_HAS_HEARING_AID_TYPE_BINAURAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c)
- [BT_HAS_HEARING_AID_TYPE_MONAURAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ggaa9572a32f912c8fe529b510aa23f4540a4b711ff711e81a22b7e80f7dc8a4aae8)
- [BT_HAS_HEARING_AID_TYPE_BANDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ggaa9572a32f912c8fe529b510aa23f4540af9e7c56173aeeb593f9e12a0e3366a0b)
- [BT_HAS_PROP_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga7b8913a9f9bc4d5c066582780adcf274a70645a9bfc628425b93b0aa6ce539173)
- [BT_HAS_PROP_WRITABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga7b8913a9f9bc4d5c066582780adcf274ad479ec0e277e2e894d0056965b484e09)
- [BT_HAS_PROP_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59)
- [bt_has_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga50d470390967317cb84b17fd450546a4)
- [BT_HAS_PRESET_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gga50d470390967317cb84b17fd450546a4a885520fe7fa533b6ea79db7ebeeed258)
- [bt_has_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga9bc61dfc710070fb136120944c0776b9)
- [bt_has_client_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaf3765300072b0a6d1ee45699e710d4da)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_has_client_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga8303b5fb2558a35bb2cb06cd5788e636)
- [bt_has](../bluetooth_service_model_reference/P077_bt_has_结构体.md)
- [bt_has_client_presets_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga54ef9918e4fb458b7416ffb94acca808)
- [bt_has_client_preset_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga4a228ee29a26346867a6427f81816336)
- [bt_has_client_preset_next](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga66943cb5275ca660f2eab11e37708d81)
- [bt_has_client_preset_prev](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga3a564b18ce6cbc7a5af970474ddf25a2)
- [bt_has_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gac39ca2d72273bd591618d186b48c20b0)
- [bt_has_preset_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gadf0a488721910633fa2b54b2c7645bd9)
- [bt_has_preset_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga39f9ac2f94b1febe8e834ae54e110e90)
- [bt_has_preset_available](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gacaa997913949b6ea98c5c6233fefdc52)
- [bt_has_preset_unavailable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gabe523e1aefc789ad0031e3c0efb27379)
- [bt_has_preset_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga0bf932a9a1977e4d1926c11242c7b70d)
- [bt_has_preset_active_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga2c0fe62baa63b72703d6f553f1de072b)
- [bt_has_preset_active_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gae1787671fac3b7873c5994adc7d19b20)
- [bt_has_preset_active_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga715cfe5bd08fbd4557ee6052b38f27de)
- [bt_has_preset_name_change](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga6f06adc529a500fcfcfea2ae89ea60d5)
- [bt_has_features_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga7e37a89b1bf0a732045276cf6b922956)

<a id="header-details"></a>

---

[上一章](P016_zephyr__dt-bindings__reset__gd32c2x1.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt.h_文件参考.md)
