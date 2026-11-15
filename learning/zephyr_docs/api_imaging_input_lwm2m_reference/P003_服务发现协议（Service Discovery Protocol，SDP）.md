---
id: learning.zephyr-docs.api-imaging-input-lwm2m-reference.page-3
title: 服务发现协议（Service Discovery Protocol，SDP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_服务发现协议（Service Discovery Protocol，SDP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

引入版本（Since）：1.6。接口版本（Version）：0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Fsdp_5Fdata_5Felem"></a>

```c
struct bt_sdp_data_elem
```

相关声明：[bt_sdp_data_elem](../bluetooth_service_model_reference/P169_bt_sdp_data_elem_结构体.md)。

服务发现协议（SDP）的通用数据元素值（Generic Data Element Value）。

<a id="r_bt_5Fsdp_5Fattribute"></a>

```c
struct bt_sdp_attribute
```

相关声明：[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)。

服务发现协议（SDP）的属性值。

<a id="r_bt_5Fsdp_5Frecord"></a>

```c
struct bt_sdp_record
```

相关声明：[bt_sdp_record](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md)。

服务发现协议（SDP）的服务记录值（Service Record Value）。

<a id="r_bt_5Fsdp_5Fclient_5Fresult"></a>

```c
struct bt_sdp_client_result
```

相关声明：[bt_sdp_client_result](../bluetooth_service_model_reference/P168_bt_sdp_client_result_结构体.md)。

通用SDP客户端查询结果（Client Query Result）的数据容器。

<a id="r_bt_5Fsdp_5Fattribute_5Fid_5Frange"></a>

```c
struct bt_sdp_attribute_id_range
```

相关声明：[bt_sdp_attribute_id_range](../bluetooth_service_model_reference/P167_bt_sdp_attribute_id_range_结构体.md)。

服务发现协议（SDP）的属性ID范围。

<a id="r_bt_5Fsdp_5Fattribute_5Fid_5Flist"></a>

```c
struct bt_sdp_attribute_id_list
```

相关声明：[bt_sdp_attribute_id_list](../bluetooth_service_model_reference/P166_bt_sdp_attribute_id_list_结构体.md)。

服务属性及服务搜索属性事务（Service Attribute / Service Search Attribute）使用的SDP属性ID列表。

<a id="r_bt_5Fsdp_5Fdiscover_5Fparams"></a>

```c
struct bt_sdp_discover_params
```

相关声明：[bt_sdp_discover_params](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md)。

用于远端SDP发现（SDP Discovery）的主要用户结构。

<a id="r_bt_5Fsdp_5Fattr_5Fvalue_5Fuint"></a>

```c
struct bt_sdp_attr_value_uint
```

相关声明：[bt_sdp_attr_value_uint](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md)。

服务发现协议（SDP）无符号整数类型的属性值。

<a id="r_bt_5Fsdp_5Fattr_5Fvalue_5Fint"></a>

```c
struct bt_sdp_attr_value_int
```

相关声明：[bt_sdp_attr_value_int](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md)。

服务发现协议（SDP）有符号整数类型的属性值。

<a id="r_bt_5Fsdp_5Fattr_5Fvalue_5Ftext"></a>

```c
struct bt_sdp_attr_value_text
```

相关声明：[bt_sdp_attr_value_text](../bluetooth_service_model_reference/P162_bt_sdp_attr_value_text_结构体.md)。

服务发现协议（SDP）文本字符串类型的属性值。

<a id="r_bt_5Fsdp_5Fattr_5Fvalue_5Furl"></a>

```c
struct bt_sdp_attr_value_url
```

相关声明：[bt_sdp_attr_value_url](../bluetooth_service_model_reference/P164_bt_sdp_attr_value_url_结构体.md)。

服务发现协议（SDP）URL字符串类型的属性值。

<a id="r_bt_5Fsdp_5Fattr_5Fvalue"></a>

```c
struct bt_sdp_attr_value
```

相关声明：[bt_sdp_attr_value](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md)。

服务发现协议（SDP）属性值的容器结构。

<a id="r_bt_5Fsdp_5Fattr_5Fvalue_5Fpair"></a>

```c
struct bt_sdp_attr_value_pair
```

相关声明：[bt_sdp_attr_value_pair](../bluetooth_service_model_reference/P161_bt_sdp_attr_value_pair_结构体.md)。

服务发现协议（SDP）属性值对的结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga610e7cab0a598f272eeb2838f4c4c996"></a>

```c
#define BT_SDP_SERVER_RECORD_HANDLE 0x0000
```

相关声明：[BT_SDP_SERVER_RECORD_HANDLE](#ga610e7cab0a598f272eeb2838f4c4c996)。

<a id="r_gab502c9288e5f01dfdaaf8390bb3f6e49"></a>

```c
#define BT_SDP_PRIMARY_LANG_BASE 0x0100
```

相关声明：[BT_SDP_PRIMARY_LANG_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)。

<a id="r_ga76737502226c623bf508ae53a6015e08"></a>

```c
#define BT_SDP_ATTR_SVCNAME_PRIMARY (0x0000 + BT_SDP_PRIMARY_LANG_BASE)
```

相关声明：[BT_SDP_ATTR_SVCNAME_PRIMARY](#ga76737502226c623bf508ae53a6015e08)、[BT_SDP_PRIMARY_LANG_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)。

<a id="r_ga3e991ec1d5467c0b3ce5d9a7e750a300"></a>

```c
#define BT_SDP_ATTR_SVCDESC_PRIMARY (0x0001 + BT_SDP_PRIMARY_LANG_BASE)
```

相关声明：[BT_SDP_ATTR_SVCDESC_PRIMARY](#ga3e991ec1d5467c0b3ce5d9a7e750a300)、[BT_SDP_PRIMARY_LANG_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)。

<a id="r_gab8b0110be857d6eca206e00c3b5e373a"></a>

```c
#define BT_SDP_ATTR_PROVNAME_PRIMARY (0x0002 + BT_SDP_PRIMARY_LANG_BASE)
```

相关声明：[BT_SDP_ATTR_PROVNAME_PRIMARY](#gab8b0110be857d6eca206e00c3b5e373a)、[BT_SDP_PRIMARY_LANG_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)。

<a id="r_ga3eb2a5501341f6c5186a27219cf27cdf"></a>

```c
#define BT_SDP_TYPE_DESC_MASK 0xf8
```

相关声明：[BT_SDP_TYPE_DESC_MASK](#ga3eb2a5501341f6c5186a27219cf27cdf)。

<a id="r_ga2d1040ccd11d1dd4c697525ebc323243"></a>

```c
#define BT_SDP_SIZE_DESC_MASK 0x07
```

相关声明：[BT_SDP_SIZE_DESC_MASK](#ga2d1040ccd11d1dd4c697525ebc323243)。

<a id="r_ga6e8f843aeb2d325058214d2a1454737a"></a>

```c
#define BT_SDP_SIZE_INDEX_OFFSET 5
```

相关声明：[BT_SDP_SIZE_INDEX_OFFSET](#ga6e8f843aeb2d325058214d2a1454737a)。

<a id="r_gaef264fa3621c3df7a164128bb95b30fc"></a>

```c
#define BT_SDP_ARRAY_8(...)
```

相关声明：[BT_SDP_ARRAY_8](#gaef264fa3621c3df7a164128bb95b30fc)。

在属性（Attribute）中声明由 8 位元素组成的数组。

<a id="r_gaa4bb67164ae1f16b26081668d00f45c7"></a>

```c
#define BT_SDP_ARRAY_16(...)
```

相关声明：[BT_SDP_ARRAY_16](#gaa4bb67164ae1f16b26081668d00f45c7)。

在属性（Attribute）中声明由 16 位元素组成的数组。

<a id="r_ga7a17ee4872190a087cf2e5ea4db9e737"></a>

```c
#define BT_SDP_ARRAY_32(...)
```

相关声明：[BT_SDP_ARRAY_32](#ga7a17ee4872190a087cf2e5ea4db9e737)。

在属性（Attribute）中声明由 32 位元素组成的数组。

<a id="r_gadbdfa913e11ed7b8e691a1fc1712e6eb"></a>

```c
#define BT_SDP_ARRAY_UUID_128(w32, w1, w2, w3, w48)
```

相关声明：[BT_SDP_ARRAY_UUID_128](#gadbdfa913e11ed7b8e691a1fc1712e6eb)。

在属性中声明采用小端字节序（Little-endian）的 128 位 UUID。

<a id="r_ga66778ac38fb5b82d3b514fe0da008393"></a>

```c
#define BT_SDP_TYPE_SIZE(_type)
```

相关声明：[BT_SDP_TYPE_SIZE](#ga66778ac38fb5b82d3b514fe0da008393)。

声明固定大小的数据元素头（Fixed-size Data Element Header）。

<a id="r_gabbb2bd6a8321513082851fe73dfa44bc"></a>

```c
#define BT_SDP_TYPE_SIZE_VAR(_type, _size)
```

相关声明：[BT_SDP_TYPE_SIZE_VAR](#gabbb2bd6a8321513082851fe73dfa44bc)。

声明可变大小的数据元素头（Variable-size Data Element Header）。

<a id="r_gaa2954f3df4d0ee9684721cbc6182e37c"></a>

```c
#define BT_SDP_DATA_ELEM_LIST(...)
```

相关声明：[BT_SDP_DATA_ELEM_LIST](#gaa2954f3df4d0ee9684721cbc6182e37c)。

声明数据元素列表（Data Element List）。

<a id="r_gaee13722587e4eb8c4beaaa0abad88fe5"></a>

```c
#define BT_SDP_NEW_SERVICE
```

相关声明：[BT_SDP_NEW_SERVICE](#gaee13722587e4eb8c4beaaa0abad88fe5)。

SDP 新服务记录声明宏（New Service Record Declaration Macro）。

<a id="r_ga25b31454ee5b5fe23b617b5256ba00c4"></a>

```c
#define BT_SDP_LIST(_att_id, _type_size, _data_elem_seq)
```

相关声明：[BT_SDP_LIST](#ga25b31454ee5b5fe23b617b5256ba00c4)。

通用 SDP 列表属性声明宏（List Attribute Declaration Macro）。

<a id="r_gaa57f3c9a52ae29c02d7577be99f91e7c"></a>

```c
#define BT_SDP_SERVICE_ID(_uuid)
```

相关声明：[BT_SDP_SERVICE_ID](#gaa57f3c9a52ae29c02d7577be99f91e7c)。

SDP 服务 ID 属性声明宏（Service ID Attribute Declaration Macro）。

<a id="r_ga83de8e62415d3e31b3b5434b9db633d0"></a>

```c
#define BT_SDP_SERVICE_NAME(_name)
```

相关声明：[BT_SDP_SERVICE_NAME](#ga83de8e62415d3e31b3b5434b9db633d0)。

SDP 名称属性声明宏（Name Attribute Declaration Macro）。

<a id="r_ga096c84414b429aa05bed45cf6175361e"></a>

```c
#define BT_SDP_SUPPORTED_FEATURES(_features)
```

相关声明：[BT_SDP_SUPPORTED_FEATURES](#ga096c84414b429aa05bed45cf6175361e)。

SDP 支持特性属性声明宏（Supported Features Attribute Declaration Macro）。

<a id="r_ga3a1feb6311af64292c1f22ff54e01876"></a>

```c
#define BT_SDP_SUPPORTED_CAPABILITIES(_capabilities)
```

相关声明：[BT_SDP_SUPPORTED_CAPABILITIES](#ga3a1feb6311af64292c1f22ff54e01876)。

SDP 支持能力属性声明宏（Supported Capabilities Attribute Declaration Macro）。

<a id="r_ga48eadaa621be7eaecbf5d2f8cc1354ab"></a>

```c
#define BT_SDP_SUPPORTED_FUNCTIONS(_functions)
```

相关声明：[BT_SDP_SUPPORTED_FUNCTIONS](#ga48eadaa621be7eaecbf5d2f8cc1354ab)。

SDP 支持功能属性声明宏（Supported Functions Attribute Declaration Macro）。

<a id="r_ga555f10b8f3ae3710c6dda9f37e78547b"></a>

```c
#define BT_SDP_RECORD(_attrs)
```

相关声明：[BT_SDP_RECORD](#ga555f10b8f3ae3710c6dda9f37e78547b)。

SDP 服务声明宏（Service Declaration Macro）。

<a id="r_ga920e61b784c4ae47bc51ac5c46273220"></a>

```c
#define BT_SDP_ATTR_ID_RANGE(beginning, ending)
```

相关声明：[BT_SDP_ATTR_ID_RANGE](#ga920e61b784c4ae47bc51ac5c46273220)。

初始化 SDP 属性 ID 范围（Attribute ID Range）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_gad672a89277b276d1b702fe07302c468e"></a>

```c
typedef uint8_t(* bt_sdp_discover_func_t) (struct bt_conn *conn, struct bt_sdp_client_result *result, const struct bt_sdp_discover_params *params)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_sdp_discover_func_t](#gad672a89277b276d1b702fe07302c468e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_sdp_client_result](../bluetooth_service_model_reference/P168_bt_sdp_client_result_结构体.md)、[bt_sdp_discover_params](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md)。

回调类型，用于通知用户：已在远端解析出给定 UUID 的结果，用户可使用结果记录缓冲区（Result Record Buffer）进一步检查。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.4\_枚举（Enumerations）

<a id="r_ga278df12ff5def68ca4663defd178582c"></a>

```c
enum { BT_SDP_DISCOVER_UUID_STOP = 0 , BT_SDP_DISCOVER_UUID_CONTINUE }
```

相关声明：[BT_SDP_DISCOVER_UUID_STOP](#gga278df12ff5def68ca4663defd178582ca990fbea48866b2acb7ccd67391b19636)、[BT_SDP_DISCOVER_UUID_CONTINUE](#gga278df12ff5def68ca4663defd178582ca94e15ea86b69d65ca9c1947d1e2157ef)。

用作 `bt_sdp_discover_func_t` 返回值的辅助枚举（Helper Enum）。

<a id="r_ga88019838cb3e5317fce93f4933583d94"></a>

```c
enum { BT_SDP_DISCOVER_SERVICE_SEARCH , BT_SDP_DISCOVER_SERVICE_ATTR , BT_SDP_DISCOVER_SERVICE_SEARCH_ATTR }
```

相关声明：[BT_SDP_DISCOVER_SERVICE_SEARCH](#gga88019838cb3e5317fce93f4933583d94a9ce8c93cf1754fc7047951e891f66ff2)、[BT_SDP_DISCOVER_SERVICE_ATTR](#gga88019838cb3e5317fce93f4933583d94a5b8c3260e5aaaa08e86a099ccfeee41f)、[BT_SDP_DISCOVER_SERVICE_SEARCH_ATTR](#gga88019838cb3e5317fce93f4933583d94a64fff103816cfc0215b9b3909786fa4e)。

SDP 发现类型（Discover Types）。

<a id="r_ga5e4a45b7b860d82a111480c9f25c2666"></a>

```c
enum bt_sdp_attr_value_type { BT_SDP_ATTR_VALUE_TYPE_NONE = 0 , BT_SDP_ATTR_VALUE_TYPE_UINT , BT_SDP_ATTR_VALUE_TYPE_SINT , BT_SDP_ATTR_VALUE_TYPE_BOOL , BT_SDP_ATTR_VALUE_TYPE_TEXT , BT_SDP_ATTR_VALUE_TYPE_URL }
```

相关声明：[bt_sdp_attr_value_type](#ga5e4a45b7b860d82a111480c9f25c2666)、[BT_SDP_ATTR_VALUE_TYPE_NONE](#gga5e4a45b7b860d82a111480c9f25c2666acaf932b38a1e17ca9e85c055096fa1da)、[BT_SDP_ATTR_VALUE_TYPE_UINT](#gga5e4a45b7b860d82a111480c9f25c2666a5af87613192cda6a05fa280d2df8574b)、[BT_SDP_ATTR_VALUE_TYPE_SINT](#gga5e4a45b7b860d82a111480c9f25c2666a5917deef84a7af5d5f908d4058732b1e)、[BT_SDP_ATTR_VALUE_TYPE_BOOL](#gga5e4a45b7b860d82a111480c9f25c2666a154bbb29fb26d007838c87def4cd34f8)、[BT_SDP_ATTR_VALUE_TYPE_TEXT](#gga5e4a45b7b860d82a111480c9f25c2666a80b8652e39dae70c61443adf4f29fb4d)、[BT_SDP_ATTR_VALUE_TYPE_URL](#gga5e4a45b7b860d82a111480c9f25c2666a27eccef21d812956c6ae7ff9194e20e4)。

SDP 属性值类型枚举（Attribute Value Type Enumeration）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.5\_函数（Functions）

<a id="r_ga6006e3cd593ef793273fb291913790fa"></a>

```c
int bt_sdp_register_service (struct bt_sdp_record *service)
```

相关声明：[bt_sdp_register_service](#ga6006e3cd593ef793273fb291913790fa)、[bt_sdp_record](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md)。

注册服务记录（Service Record）。

<a id="r_ga71e7d75850becf4ead62668c8e7bebbc"></a>

```c
int bt_sdp_unregister_service (struct bt_sdp_record *service)
```

相关声明：[bt_sdp_unregister_service](#ga71e7d75850becf4ead62668c8e7bebbc)、[bt_sdp_record](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md)。

注销服务记录（Service Record）。

<a id="r_ga44658df825a40f820a31e7adb4240d25"></a>

```c
int bt_sdp_discover (struct bt_conn *conn, struct bt_sdp_discover_params *params)
```

相关声明：[bt_sdp_discover](#ga44658df825a40f820a31e7adb4240d25)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_sdp_discover_params](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md)。

允许用户启动 SDP 发现会话（Discovery Session）。

<a id="r_ga2eb0646597a44e0e3cb0234d2c12a2d7"></a>

```c
int bt_sdp_discover_cancel (struct bt_conn *conn, struct bt_sdp_discover_params *params)
```

相关声明：[bt_sdp_discover_cancel](#ga2eb0646597a44e0e3cb0234d2c12a2d7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_sdp_discover_params](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md)。

释放等待中的 SDP 发现请求（Discovery Request）。

<a id="r_gaf69723cff6dce7e86f0f0240ec3e2041"></a>

```c
int bt_sdp_get_proto_param (const struct net_buf *buf, uint16_t proto, uint16_t *param)
```

相关声明：[bt_sdp_get_proto_param](#gaf69723cff6dce7e86f0f0240ec3e2041)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向用户提供与给定协议栈层协议 UUID（Stacked Protocol UUID）相关的参数值。

<a id="r_gaba31a2327e4bba56ef2ac831b166e66a"></a>

```c
int bt_sdp_get_addl_proto_param (const struct net_buf *buf, uint16_t proto, uint8_t index, uint16_t *param)
```

相关声明：[bt_sdp_get_addl_proto_param](#gaba31a2327e4bba56ef2ac831b166e66a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取与给定协议栈层协议 UUID（Stacked Protocol UUID）相关的附加参数值。

<a id="r_ga9e7d4bd0a407fe8254410f907db90f00"></a>

```c
int bt_sdp_get_profile_version (const struct net_buf *buf, uint16_t profile, uint16_t *version)
```

相关声明：[bt_sdp_get_profile_version](#ga9e7d4bd0a407fe8254410f907db90f00)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取配置文件版本（Profile Version）。

<a id="r_gae1c3110dfe24a939cc02d998c4699ca7"></a>

```c
int bt_sdp_get_features (const struct net_buf *buf, uint16_t *features)
```

相关声明：[bt_sdp_get_features](#gae1c3110dfe24a939cc02d998c4699ca7)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取支持特性（SupportedFeatures）属性值。

<a id="r_gaed089d52f57cb25d2b02b2adbc60a36a"></a>

```c
int bt_sdp_get_vendor_id (const struct net_buf *buf, uint16_t *vendor_id)
```

相关声明：[bt_sdp_get_vendor_id](#gaed089d52f57cb25d2b02b2adbc60a36a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取厂商 ID（Vendor ID）。

<a id="r_ga71809908bb73150258b2a5ab3c2f8517"></a>

```c
int bt_sdp_get_product_id (const struct net_buf *buf, uint16_t *product_id)
```

相关声明：[bt_sdp_get_product_id](#ga71809908bb73150258b2a5ab3c2f8517)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取产品 ID（Product ID）。

<a id="r_ga0ce1314e052881eec5a43f571857960e"></a>

```c
int bt_sdp_record_parse (const struct net_buf *buf, bool(*func)(const struct bt_sdp_attribute *attr, void *user_data), void *user_data)
```

相关声明：[bt_sdp_record_parse](#ga0ce1314e052881eec5a43f571857960e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)。

遍历发现的 SDP 记录（Record）。

<a id="r_ga2cb42ca8e487071682c37124ab56f2ab"></a>

```c
bool bt_sdp_has_attr (const struct net_buf *buf, uint16_t attr_id)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_sdp_has_attr](#ga2cb42ca8e487071682c37124ab56f2ab)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查是否找到指定属性标识符（Attribute Identifier）。

<a id="r_ga9df34b18af051782377229a18e6d3887"></a>

```c
int bt_sdp_get_attr (const struct net_buf *buf, uint16_t attr_id, struct bt_sdp_attribute *attr)
```

相关声明：[bt_sdp_get_attr](#ga9df34b18af051782377229a18e6d3887)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)。

按 ID 从 SDP 记录获取指定属性（Attribute）。

<a id="r_gab7d3e8bc83efff28cf9118710b5486fc"></a>

```c
int bt_sdp_attr_value_parse (const struct bt_sdp_attribute *attr, bool(*func)(const struct bt_sdp_attr_value_pair *value, void *user_data), void *user_data)
```

相关声明：[bt_sdp_attr_value_parse](#gab7d3e8bc83efff28cf9118710b5486fc)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_sdp_attr_value_pair](../bluetooth_service_model_reference/P161_bt_sdp_attr_value_pair_结构体.md)。

解析 SDP 属性值（Attribute Values）。

<a id="r_ga07ca5d4f383d74004478cfd6ead2b80a"></a>

```c
bool bt_sdp_attr_has_uuid (const struct bt_sdp_attribute *attr, const struct bt_uuid *uuid)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_sdp_attr_has_uuid](#ga07ca5d4f383d74004478cfd6ead2b80a)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

检查 SDP 属性是否包含指定 UUID。

<a id="r_ga3bad45ab578c0277a320ac241692f799"></a>

```c
int bt_sdp_attr_read (const struct bt_sdp_attribute *attr, const struct bt_uuid *uuid, struct bt_sdp_attr_value *value)
```

相关声明：[bt_sdp_attr_read](#ga3bad45ab578c0277a320ac241692f799)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_sdp_attr_value](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md)。

读取指定 UUID 对应的 SDP 属性值（Attribute Value）。

<a id="r_gac395eff18a4d2af3d955e276bf13963a"></a>

```c
int bt_sdp_attr_addl_proto_parse (const struct bt_sdp_attribute *attr, bool(*func)(const struct bt_sdp_attribute *attr, void *user_data), void *user_data)
```

相关声明：[bt_sdp_attr_addl_proto_parse](#gac395eff18a4d2af3d955e276bf13963a)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)。

解析附加协议描述符列表属性（Additional Protocol Descriptor List Attribute）。

<a id="r_gaa104046a9e6e15f05961bf8652ecec16"></a>

```c
ssize_t bt_sdp_attr_addl_proto_count (const struct bt_sdp_attribute *attr)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_sdp_attr_addl_proto_count](#gaa104046a9e6e15f05961bf8652ecec16)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)。

获取附加协议描述符列表（Additional Protocol Descriptor List）中的协议描述符数量。

<a id="r_gacf20a00d84e6eed2c128284fe9c52024"></a>

```c
int bt_sdp_attr_addl_proto_read (const struct bt_sdp_attribute *attr, uint16_t index, const struct bt_uuid *uuid, struct bt_sdp_attr_value *value)
```

相关声明：[bt_sdp_attr_addl_proto_read](#gacf20a00d84e6eed2c128284fe9c52024)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_sdp_attr_value](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md)。

读取附加协议描述符列表（Additional Protocol Descriptor List）中指定索引和 UUID 对应的值。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 3.6\_标准服务与服务组的服务类标识符（Service class identifiers of standard services and service groups）

<a id="r_gac2c2379f8e483939826297dc49657837"></a>

```c
#define BT_SDP_SDP_SERVER_SVCLASS 0x1000
```

相关声明：[BT_SDP_SDP_SERVER_SVCLASS](#gac2c2379f8e483939826297dc49657837)。

服务发现服务器（Service Discovery Server）。

<a id="r_gabe05780702a9be7da54a8c04f79ad752"></a>

```c
#define BT_SDP_BROWSE_GRP_DESC_SVCLASS 0x1001
```

相关声明：[BT_SDP_BROWSE_GRP_DESC_SVCLASS](#gabe05780702a9be7da54a8c04f79ad752)。

浏览组描述符（Browse Group Descriptor）。

<a id="r_ga383233a0ff3159ed653786490a4c06ae"></a>

```c
#define BT_SDP_PUBLIC_BROWSE_GROUP 0x1002
```

相关声明：[BT_SDP_PUBLIC_BROWSE_GROUP](#ga383233a0ff3159ed653786490a4c06ae)。

公共浏览组（Public Browse Group）。

<a id="r_gab1234d808a7e347328bf95ad065fd9c4"></a>

```c
#define BT_SDP_SERIAL_PORT_SVCLASS 0x1101
```

相关声明：[BT_SDP_SERIAL_PORT_SVCLASS](#gab1234d808a7e347328bf95ad065fd9c4)。

串行端口（Serial Port）。

<a id="r_gaf0199837105ded0d65314e573da6a3ed"></a>

```c
#define BT_SDP_LAN_ACCESS_SVCLASS 0x1102
```

相关声明：[BT_SDP_LAN_ACCESS_SVCLASS](#gaf0199837105ded0d65314e573da6a3ed)。

使用 PPP 的局域网访问（LAN Access Using PPP）。

<a id="r_gaab655c1f93029ed64743156734e2519e"></a>

```c
#define BT_SDP_DIALUP_NET_SVCLASS 0x1103
```

相关声明：[BT_SDP_DIALUP_NET_SVCLASS](#gaab655c1f93029ed64743156734e2519e)。

拨号网络（Dialup Networking）。

<a id="r_ga28fc78fc21e4d88569e5ca5727ed6202"></a>

```c
#define BT_SDP_IRMC_SYNC_SVCLASS 0x1104
```

相关声明：[BT_SDP_IRMC_SYNC_SVCLASS](#ga28fc78fc21e4d88569e5ca5727ed6202)。

IrMC 同步（IrMC Sync）。

<a id="r_gaaf64788e0cc6d54a8511c07af22f6740"></a>

```c
#define BT_SDP_OBEX_OBJPUSH_SVCLASS 0x1105
```

相关声明：[BT_SDP_OBEX_OBJPUSH_SVCLASS](#gaaf64788e0cc6d54a8511c07af22f6740)。

OBEX 对象推送（OBEX Object Push）。

<a id="r_gacd25278a573edcb16aa4b60f8ffad20d"></a>

```c
#define BT_SDP_OBEX_FILETRANS_SVCLASS 0x1106
```

相关声明：[BT_SDP_OBEX_FILETRANS_SVCLASS](#gacd25278a573edcb16aa4b60f8ffad20d)。

OBEX 文件传输（OBEX File Transfer）。

<a id="r_ga39d4ce2465b10c10ee746c1491c49bea"></a>

```c
#define BT_SDP_IRMC_SYNC_CMD_SVCLASS 0x1107
```

相关声明：[BT_SDP_IRMC_SYNC_CMD_SVCLASS](#ga39d4ce2465b10c10ee746c1491c49bea)。

IrMC 同步命令（IrMC Sync Command）。

<a id="r_ga6eb16aacf468b460fa7675ffc4703e68"></a>

```c
#define BT_SDP_HEADSET_SVCLASS 0x1108
```

相关声明：[BT_SDP_HEADSET_SVCLASS](#ga6eb16aacf468b460fa7675ffc4703e68)。

带麦克风耳机（Headset）。

<a id="r_ga16e1bc10528ac82f6cec822912f97d8c"></a>

```c
#define BT_SDP_CORDLESS_TELEPHONY_SVCLASS 0x1109
```

相关声明：[BT_SDP_CORDLESS_TELEPHONY_SVCLASS](#ga16e1bc10528ac82f6cec822912f97d8c)。

无绳电话（Cordless Telephony）。

<a id="r_gafeb3a3184a0b83e0045187cbe3cf24dc"></a>

```c
#define BT_SDP_AUDIO_SOURCE_SVCLASS 0x110a
```

相关声明：[BT_SDP_AUDIO_SOURCE_SVCLASS](#gafeb3a3184a0b83e0045187cbe3cf24dc)。

音频源（Audio Source）。

<a id="r_gaa0e334873b5477523572caa2359a4098"></a>

```c
#define BT_SDP_AUDIO_SINK_SVCLASS 0x110b
```

相关声明：[BT_SDP_AUDIO_SINK_SVCLASS](#gaa0e334873b5477523572caa2359a4098)。

音频接收端（Audio Sink）。

<a id="r_gafe96e9d32797a83c793f0ed278054b80"></a>

```c
#define BT_SDP_AV_REMOTE_TARGET_SVCLASS 0x110c
```

相关声明：[BT_SDP_AV_REMOTE_TARGET_SVCLASS](#gafe96e9d32797a83c793f0ed278054b80)。

音视频远程控制目标端（A/V Remote Control Target）。

<a id="r_ga2fdc3eb32196b5135b7f595a36cacb4c"></a>

```c
#define BT_SDP_ADVANCED_AUDIO_SVCLASS 0x110d
```

相关声明：[BT_SDP_ADVANCED_AUDIO_SVCLASS](#ga2fdc3eb32196b5135b7f595a36cacb4c)。

高级音频分发（Advanced Audio Distribution）。

<a id="r_gaea94250bed4c5e6ad47749a1237778f5"></a>

```c
#define BT_SDP_AV_REMOTE_SVCLASS 0x110e
```

相关声明：[BT_SDP_AV_REMOTE_SVCLASS](#gaea94250bed4c5e6ad47749a1237778f5)。

音视频远程控制（A/V Remote Control）。

<a id="r_gaaae997769dfc8325c38830707f4d22e3"></a>

```c
#define BT_SDP_AV_REMOTE_CONTROLLER_SVCLASS 0x110f
```

相关声明：[BT_SDP_AV_REMOTE_CONTROLLER_SVCLASS](#gaaae997769dfc8325c38830707f4d22e3)。

音视频远程控制控制器（A/V Remote Control Controller）。

<a id="r_ga9681e34d78cea87e413fa4be40e4239a"></a>

```c
#define BT_SDP_INTERCOM_SVCLASS 0x1110
```

相关声明：[BT_SDP_INTERCOM_SVCLASS](#ga9681e34d78cea87e413fa4be40e4239a)。

对讲（Intercom）。

<a id="r_ga31962fab5bed7c54311c4b291713a836"></a>

```c
#define BT_SDP_FAX_SVCLASS 0x1111
```

相关声明：[BT_SDP_FAX_SVCLASS](#ga31962fab5bed7c54311c4b291713a836)。

传真（Fax）。

<a id="r_ga4c9322cf28a8b1aa96828152e8ee7379"></a>

```c
#define BT_SDP_HEADSET_AGW_SVCLASS 0x1112
```

相关声明：[BT_SDP_HEADSET_AGW_SVCLASS](#ga4c9322cf28a8b1aa96828152e8ee7379)。

耳机音频网关（Headset AG）。

<a id="r_ga2ab79d7ff4e88820773cf24f0b0b6e20"></a>

```c
#define BT_SDP_WAP_SVCLASS 0x1113
```

相关声明：[BT_SDP_WAP_SVCLASS](#ga2ab79d7ff4e88820773cf24f0b0b6e20)。

无线应用协议（WAP）。

<a id="r_ga22624d29917aaeaa0c281d9517178821"></a>

```c
#define BT_SDP_WAP_CLIENT_SVCLASS 0x1114
```

相关声明：[BT_SDP_WAP_CLIENT_SVCLASS](#ga22624d29917aaeaa0c281d9517178821)。

无线应用协议客户端（WAP Client）。

<a id="r_gaa9abb444e3b43c1164d6b450b1c066e5"></a>

```c
#define BT_SDP_PANU_SVCLASS 0x1115
```

相关声明：[BT_SDP_PANU_SVCLASS](#gaa9abb444e3b43c1164d6b450b1c066e5)。

个人区域网络用户（Personal Area Networking User）。

<a id="r_ga78a7be1db8be8d7eece0d17c629dd009"></a>

```c
#define BT_SDP_NAP_SVCLASS 0x1116
```

相关声明：[BT_SDP_NAP_SVCLASS](#ga78a7be1db8be8d7eece0d17c629dd009)。

网络接入点（Network Access Point）。

<a id="r_gaed2d6f72c344e2e9b9bdcefd23cb4086"></a>

```c
#define BT_SDP_GN_SVCLASS 0x1117
```

相关声明：[BT_SDP_GN_SVCLASS](#gaed2d6f72c344e2e9b9bdcefd23cb4086)。

组网络（Group Network）。

<a id="r_ga30f6edbd67d96f7752a223409c8e4431"></a>

```c
#define BT_SDP_DIRECT_PRINTING_SVCLASS 0x1118
```

相关声明：[BT_SDP_DIRECT_PRINTING_SVCLASS](#ga30f6edbd67d96f7752a223409c8e4431)。

直接打印（Direct Printing）。

<a id="r_ga6bc247854656613d2fa9b47d55bd69d6"></a>

```c
#define BT_SDP_REFERENCE_PRINTING_SVCLASS 0x1119
```

相关声明：[BT_SDP_REFERENCE_PRINTING_SVCLASS](#ga6bc247854656613d2fa9b47d55bd69d6)。

引用打印（Reference Printing）。

<a id="r_ga08730b1fd7088101fadb85e5dc13fd24"></a>

```c
#define BT_SDP_IMAGING_SVCLASS 0x111a
```

相关声明：[BT_SDP_IMAGING_SVCLASS](#ga08730b1fd7088101fadb85e5dc13fd24)。

基本图像配置文件（Basic Imaging Profile）。

<a id="r_gaf19cd136b780ef303c1290b26ab2ca17"></a>

```c
#define BT_SDP_IMAGING_RESPONDER_SVCLASS 0x111b
```

相关声明：[BT_SDP_IMAGING_RESPONDER_SVCLASS](#gaf19cd136b780ef303c1290b26ab2ca17)。

图像响应端（Imaging Responder）。

<a id="r_ga3f04a28d9764a0c7755babe379c25393"></a>

```c
#define BT_SDP_IMAGING_ARCHIVE_SVCLASS 0x111c
```

相关声明：[BT_SDP_IMAGING_ARCHIVE_SVCLASS](#ga3f04a28d9764a0c7755babe379c25393)。

图像自动归档（Imaging Automatic Archive）。

<a id="r_ga51a4cfc28f86a650b03a7bbe6e5b883a"></a>

```c
#define BT_SDP_IMAGING_REFOBJS_SVCLASS 0x111d
```

相关声明：[BT_SDP_IMAGING_REFOBJS_SVCLASS](#ga51a4cfc28f86a650b03a7bbe6e5b883a)。

图像引用对象（Imaging Referenced Objects）。

<a id="r_gab9f99989420545b3b0e71da6c5475f90"></a>

```c
#define BT_SDP_HANDSFREE_SVCLASS 0x111e
```

相关声明：[BT_SDP_HANDSFREE_SVCLASS](#gab9f99989420545b3b0e71da6c5475f90)。

免提（Handsfree）。

<a id="r_ga1c44ae236a292c91dc81539c9c89947c"></a>

```c
#define BT_SDP_HANDSFREE_AGW_SVCLASS 0x111f
```

相关声明：[BT_SDP_HANDSFREE_AGW_SVCLASS](#ga1c44ae236a292c91dc81539c9c89947c)。

免提音频网关（Handsfree Audio Gateway）。

<a id="r_ga79d34c3b7641cf523adf6515720ceceb"></a>

```c
#define BT_SDP_DIRECT_PRT_REFOBJS_SVCLASS 0x1120
```

相关声明：[BT_SDP_DIRECT_PRT_REFOBJS_SVCLASS](#ga79d34c3b7641cf523adf6515720ceceb)。

直接打印引用对象服务（Direct Printing Reference Objects Service）。

<a id="r_ga78607a42f5228b37d348614b12e48a77"></a>

```c
#define BT_SDP_REFLECTED_UI_SVCLASS 0x1121
```

相关声明：[BT_SDP_REFLECTED_UI_SVCLASS](#ga78607a42f5228b37d348614b12e48a77)。

映射用户界面（Reflected UI）。

<a id="r_gac727f387a55a76c9a071cf62792f50e4"></a>

```c
#define BT_SDP_BASIC_PRINTING_SVCLASS 0x1122
```

相关声明：[BT_SDP_BASIC_PRINTING_SVCLASS](#gac727f387a55a76c9a071cf62792f50e4)。

基本打印（Basic Printing）。

<a id="r_ga9298ac73a26a1ab2e53733f404e5c6ea"></a>

```c
#define BT_SDP_PRINTING_STATUS_SVCLASS 0x1123
```

相关声明：[BT_SDP_PRINTING_STATUS_SVCLASS](#ga9298ac73a26a1ab2e53733f404e5c6ea)。

打印状态（Printing Status）。

<a id="r_gab63eab5791898a47bd540eed4d55cddc"></a>

```c
#define BT_SDP_HID_SVCLASS 0x1124
```

相关声明：[BT_SDP_HID_SVCLASS](#gab63eab5791898a47bd540eed4d55cddc)。

人机接口设备服务（Human Interface Device Service）。

<a id="r_ga873f8e03aeb696d3eb287a8d00796a4f"></a>

```c
#define BT_SDP_HCR_SVCLASS 0x1125
```

相关声明：[BT_SDP_HCR_SVCLASS](#ga873f8e03aeb696d3eb287a8d00796a4f)。

硬拷贝线缆替代（Hardcopy Cable Replacement）。

<a id="r_ga4ca1e6eb6fe385e526f8d84ed65ab285"></a>

```c
#define BT_SDP_HCR_PRINT_SVCLASS 0x1126
```

相关声明：[BT_SDP_HCR_PRINT_SVCLASS](#ga4ca1e6eb6fe385e526f8d84ed65ab285)。

HCR 打印（HCR Print）。

<a id="r_ga621afe0f5a6d176c26e140c4162bee07"></a>

```c
#define BT_SDP_HCR_SCAN_SVCLASS 0x1127
```

相关声明：[BT_SDP_HCR_SCAN_SVCLASS](#ga621afe0f5a6d176c26e140c4162bee07)。

HCR 扫描（HCR Scan）。

<a id="r_ga9617c02c6999d9fe987e91c6c2dc5dca"></a>

```c
#define BT_SDP_CIP_SVCLASS 0x1128
```

相关声明：[BT_SDP_CIP_SVCLASS](#ga9617c02c6999d9fe987e91c6c2dc5dca)。

通用 ISDN 访问（Common ISDN Access）。

<a id="r_ga3e087c095a78f07efae660eceae9c11e"></a>

```c
#define BT_SDP_VIDEO_CONF_GW_SVCLASS 0x1129
```

相关声明：[BT_SDP_VIDEO_CONF_GW_SVCLASS](#ga3e087c095a78f07efae660eceae9c11e)。

视频会议网关（Video Conferencing Gateway）。

<a id="r_ga629179357eff2cd60621f0e1e435df06"></a>

```c
#define BT_SDP_UDI_MT_SVCLASS 0x112a
```

相关声明：[BT_SDP_UDI_MT_SVCLASS](#ga629179357eff2cd60621f0e1e435df06)。

UDI MT 服务（UDI MT）。

<a id="r_ga846599abf75f1cbb27028aea8a619f31"></a>

```c
#define BT_SDP_UDI_TA_SVCLASS 0x112b
```

相关声明：[BT_SDP_UDI_TA_SVCLASS](#ga846599abf75f1cbb27028aea8a619f31)。

UDI TA 服务（UDI TA）。

<a id="r_gab7a8499dbb73a2700389d55d331bd23e"></a>

```c
#define BT_SDP_AV_SVCLASS 0x112c
```

相关声明：[BT_SDP_AV_SVCLASS](#gab7a8499dbb73a2700389d55d331bd23e)。

音频／视频（Audio/Video）。

<a id="r_gad2234f8e0bce0e6b55d18c7a7c950e1d"></a>

```c
#define BT_SDP_SAP_SVCLASS 0x112d
```

相关声明：[BT_SDP_SAP_SVCLASS](#gad2234f8e0bce0e6b55d18c7a7c950e1d)。

SIM 卡访问（SIM Access）。

<a id="r_gaec2475b7ba36b860c0f8a9cfc33df4a8"></a>

```c
#define BT_SDP_PBAP_PCE_SVCLASS 0x112e
```

相关声明：[BT_SDP_PBAP_PCE_SVCLASS](#gaec2475b7ba36b860c0f8a9cfc33df4a8)。

电话簿访问客户端（Phonebook Access Client）。

<a id="r_ga612bb83e9f08edd163433a5fbe9528fc"></a>

```c
#define BT_SDP_PBAP_PSE_SVCLASS 0x112f
```

相关声明：[BT_SDP_PBAP_PSE_SVCLASS](#ga612bb83e9f08edd163433a5fbe9528fc)。

电话簿访问服务器（Phonebook Access Server）。

<a id="r_ga60a9fad26300c15e988e101f90c06435"></a>

```c
#define BT_SDP_PBAP_SVCLASS 0x1130
```

相关声明：[BT_SDP_PBAP_SVCLASS](#ga60a9fad26300c15e988e101f90c06435)。

电话簿访问（Phonebook Access）。

<a id="r_ga58f5cc54014e3723720e7c3b7ba82fd8"></a>

```c
#define BT_SDP_MAP_MSE_SVCLASS 0x1132
```

相关声明：[BT_SDP_MAP_MSE_SVCLASS](#ga58f5cc54014e3723720e7c3b7ba82fd8)。

消息访问服务器（Message Access Server）。

<a id="r_ga47849c599678f7ec48c237b8b36e9cb7"></a>

```c
#define BT_SDP_MAP_MCE_SVCLASS 0x1133
```

相关声明：[BT_SDP_MAP_MCE_SVCLASS](#ga47849c599678f7ec48c237b8b36e9cb7)。

消息通知服务器（Message Notification Server）。

<a id="r_gaec665050af4cc3affcef3912bb212fc0"></a>

```c
#define BT_SDP_MAP_SVCLASS 0x1134
```

相关声明：[BT_SDP_MAP_SVCLASS](#gaec665050af4cc3affcef3912bb212fc0)。

消息访问配置文件（Message Access Profile）。

<a id="r_ga300585062ed9ae05daca226cb3c5440d"></a>

```c
#define BT_SDP_GNSS_SVCLASS 0x1135
```

相关声明：[BT_SDP_GNSS_SVCLASS](#ga300585062ed9ae05daca226cb3c5440d)。

全球导航卫星系统（GNSS）

<a id="r_gacdfb8ca6a776f57a2df38b4a6eaa8403"></a>

```c
#define BT_SDP_GNSS_SERVER_SVCLASS 0x1136
```

相关声明：[BT_SDP_GNSS_SERVER_SVCLASS](#gacdfb8ca6a776f57a2df38b4a6eaa8403)。

全球导航卫星系统服务器（GNSS Server）。

<a id="r_ga9cce7e3a576329661b363b102cefa494"></a>

```c
#define BT_SDP_MPS_SC_SVCLASS 0x113a
```

相关声明：[BT_SDP_MPS_SC_SVCLASS](#ga9cce7e3a576329661b363b102cefa494)。

MPS SC 服务标识（MPS SC）。

<a id="r_gaf847b2675482d3bb9674f569c3604e40"></a>

```c
#define BT_SDP_MPS_SVCLASS 0x113b
```

相关声明：[BT_SDP_MPS_SVCLASS](#gaf847b2675482d3bb9674f569c3604e40)。

多配置文件规范（MPS）。

<a id="r_gaed5403661e0eb8f798a950bead59369a"></a>

```c
#define BT_SDP_PNP_INFO_SVCLASS 0x1200
```

相关声明：[BT_SDP_PNP_INFO_SVCLASS](#gaed5403661e0eb8f798a950bead59369a)。

即插即用信息（PnP Information）。

<a id="r_ga1b9a169ff4db4fda939cba3ce21f808b"></a>

```c
#define BT_SDP_GENERIC_NETWORKING_SVCLASS 0x1201
```

相关声明：[BT_SDP_GENERIC_NETWORKING_SVCLASS](#ga1b9a169ff4db4fda939cba3ce21f808b)。

通用联网（Generic Networking）。

<a id="r_gaa8e5c423fca1fb0d06504cdc5be276d1"></a>

```c
#define BT_SDP_GENERIC_FILETRANS_SVCLASS 0x1202
```

相关声明：[BT_SDP_GENERIC_FILETRANS_SVCLASS](#gaa8e5c423fca1fb0d06504cdc5be276d1)。

通用文件传输（Generic File Transfer）。

<a id="r_gaec7548467ffb686b22a907d05e38f275"></a>

```c
#define BT_SDP_GENERIC_AUDIO_SVCLASS 0x1203
```

相关声明：[BT_SDP_GENERIC_AUDIO_SVCLASS](#gaec7548467ffb686b22a907d05e38f275)。

通用音频（Generic Audio）。

<a id="r_ga010b005cfdb69c67cfc7e3c5c8426778"></a>

```c
#define BT_SDP_GENERIC_TELEPHONY_SVCLASS 0x1204
```

相关声明：[BT_SDP_GENERIC_TELEPHONY_SVCLASS](#ga010b005cfdb69c67cfc7e3c5c8426778)。

通用电话（Generic Telephony）。

<a id="r_ga9e7fa3bcf139462a2c33f90b526e1ad1"></a>

```c
#define BT_SDP_UPNP_SVCLASS 0x1205
```

相关声明：[BT_SDP_UPNP_SVCLASS](#ga9e7fa3bcf139462a2c33f90b526e1ad1)。

通用即插即用服务（UPnP Service）。

<a id="r_ga102b24708429877c4f37a5008fb176b1"></a>

```c
#define BT_SDP_UPNP_IP_SVCLASS 0x1206
```

相关声明：[BT_SDP_UPNP_IP_SVCLASS](#ga102b24708429877c4f37a5008fb176b1)。

UPnP IP 服务（UPnP IP Service）。

<a id="r_ga3f50947a742b24089f86193e773d623b"></a>

```c
#define BT_SDP_UPNP_PAN_SVCLASS 0x1300
```

相关声明：[BT_SDP_UPNP_PAN_SVCLASS](#ga3f50947a742b24089f86193e773d623b)。

UPnP IP 个人区域网络（UPnP IP PAN）。

<a id="r_gad418094573383e6252719abed97d24dd"></a>

```c
#define BT_SDP_UPNP_LAP_SVCLASS 0x1301
```

相关声明：[BT_SDP_UPNP_LAP_SVCLASS](#gad418094573383e6252719abed97d24dd)。

UPnP IP 局域网访问配置文件（UPnP IP LAP）。

<a id="r_gad4d97c0b664c48bdc0842f92240409c7"></a>

```c
#define BT_SDP_UPNP_L2CAP_SVCLASS 0x1302
```

相关声明：[BT_SDP_UPNP_L2CAP_SVCLASS](#gad4d97c0b664c48bdc0842f92240409c7)。

UPnP IP L2CAP（UPnP IP L2CAP）。

<a id="r_ga17d7fb3a77ef7266ea2d760fb3696a83"></a>

```c
#define BT_SDP_VIDEO_SOURCE_SVCLASS 0x1303
```

相关声明：[BT_SDP_VIDEO_SOURCE_SVCLASS](#ga17d7fb3a77ef7266ea2d760fb3696a83)。

视频源（Video Source）。

<a id="r_ga1e3428b6d0197bd7c9d72154c025e9f5"></a>

```c
#define BT_SDP_VIDEO_SINK_SVCLASS 0x1304
```

相关声明：[BT_SDP_VIDEO_SINK_SVCLASS](#ga1e3428b6d0197bd7c9d72154c025e9f5)。

视频接收端（Video Sink）。

<a id="r_ga4e2ef8310c9396f9fb7781ab4732f308"></a>

```c
#define BT_SDP_VIDEO_DISTRIBUTION_SVCLASS 0x1305
```

相关声明：[BT_SDP_VIDEO_DISTRIBUTION_SVCLASS](#ga4e2ef8310c9396f9fb7781ab4732f308)。

视频分发（Video Distribution）。

<a id="r_gaf8fc80f3b2ff245b7d354aa0488bb42b"></a>

```c
#define BT_SDP_HDP_SVCLASS 0x1400
```

相关声明：[BT_SDP_HDP_SVCLASS](#gaf8fc80f3b2ff245b7d354aa0488bb42b)。

健康设备配置文件（HDP）。

<a id="r_ga87ba9fdf39fb99397a6dec4d92b6e3f1"></a>

```c
#define BT_SDP_HDP_SOURCE_SVCLASS 0x1401
```

相关声明：[BT_SDP_HDP_SOURCE_SVCLASS](#ga87ba9fdf39fb99397a6dec4d92b6e3f1)。

健康设备配置文件源端（HDP Source）。

<a id="r_ga2125a92c6eb724a63d04188919a12bf1"></a>

```c
#define BT_SDP_HDP_SINK_SVCLASS 0x1402
```

相关声明：[BT_SDP_HDP_SINK_SVCLASS](#ga2125a92c6eb724a63d04188919a12bf1)。

健康设备配置文件接收端（HDP Sink）。

<a id="r_gae8010af5b12cd1c1b1633a4d2c9f5ab0"></a>

```c
#define BT_SDP_GENERIC_ACCESS_SVCLASS 0x1800
```

相关声明：[BT_SDP_GENERIC_ACCESS_SVCLASS](#gae8010af5b12cd1c1b1633a4d2c9f5ab0)。

通用访问配置文件（Generic Access Profile）。

<a id="r_gad3f345431526bb713921f4b51c48b056"></a>

```c
#define BT_SDP_GENERIC_ATTRIB_SVCLASS 0x1801
```

相关声明：[BT_SDP_GENERIC_ATTRIB_SVCLASS](#gad3f345431526bb713921f4b51c48b056)。

通用属性配置文件（Generic Attribute Profile）。

<a id="r_ga694b04c2dae3b06b7fd66640468a5a38"></a>

```c
#define BT_SDP_APPLE_AGENT_SVCLASS 0x2112
```

相关声明：[BT_SDP_APPLE_AGENT_SVCLASS](#ga694b04c2dae3b06b7fd66640468a5a38)。

Apple 代理（Apple Agent）。

## 3.7\_属性标识符编码（Attribute identifier codes）

`attribute-id` 的可能值列在下方。

详情参见 SDP 规范中的“服务属性定义（Service Attribute Definitions）”一节。

<a id="r_ga38f32cae462272b51eb4edca0c5c95a2"></a>

```c
#define BT_SDP_ATTR_RECORD_HANDLE 0x0000
```

相关声明：[BT_SDP_ATTR_RECORD_HANDLE](#ga38f32cae462272b51eb4edca0c5c95a2)。

服务记录句柄（Service Record Handle）。

<a id="r_gab5c5be56c54d3f8bd4ac6defff0b1e7c"></a>

```c
#define BT_SDP_ATTR_SVCLASS_ID_LIST 0x0001
```

相关声明：[BT_SDP_ATTR_SVCLASS_ID_LIST](#gab5c5be56c54d3f8bd4ac6defff0b1e7c)。

服务类别 ID 列表（Service Class ID List）。

<a id="r_ga4d458591f8eba26feaab1220c49f6a29"></a>

```c
#define BT_SDP_ATTR_RECORD_STATE 0x0002
```

相关声明：[BT_SDP_ATTR_RECORD_STATE](#ga4d458591f8eba26feaab1220c49f6a29)。

服务记录状态（Service Record State）。

<a id="r_gad2149fd761f7ae2ea6ef761ab2545ab4"></a>

```c
#define BT_SDP_ATTR_SERVICE_ID 0x0003
```

相关声明：[BT_SDP_ATTR_SERVICE_ID](#gad2149fd761f7ae2ea6ef761ab2545ab4)。

服务 ID（Service ID）。

<a id="r_ga3e7dad966deab42ff9fa0fd04d3d4514"></a>

```c
#define BT_SDP_ATTR_PROTO_DESC_LIST 0x0004
```

相关声明：[BT_SDP_ATTR_PROTO_DESC_LIST](#ga3e7dad966deab42ff9fa0fd04d3d4514)。

协议描述符列表（Protocol Descriptor List）。

<a id="r_ga2609212bf5400c31351bc3ec5f60a7e1"></a>

```c
#define BT_SDP_ATTR_BROWSE_GRP_LIST 0x0005
```

相关声明：[BT_SDP_ATTR_BROWSE_GRP_LIST](#ga2609212bf5400c31351bc3ec5f60a7e1)。

浏览组列表（Browse Group List）。

<a id="r_ga462ec997a81c6b439a24e2de085676ab"></a>

```c
#define BT_SDP_ATTR_LANG_BASE_ATTR_ID_LIST 0x0006
```

相关声明：[BT_SDP_ATTR_LANG_BASE_ATTR_ID_LIST](#ga462ec997a81c6b439a24e2de085676ab)。

语言基础属性 ID 列表（Language Base Attribute ID List）。

<a id="r_ga7ef037ed6628aa7354736295e0e4ec77"></a>

```c
#define BT_SDP_ATTR_SVCINFO_TTL 0x0007
```

相关声明：[BT_SDP_ATTR_SVCINFO_TTL](#ga7ef037ed6628aa7354736295e0e4ec77)。

服务信息生存时间（Service Info Time to Live）。

<a id="r_gaf55a72ce05def1da08d15a23cee4c5e3"></a>

```c
#define BT_SDP_ATTR_SERVICE_AVAILABILITY 0x0008
```

相关声明：[BT_SDP_ATTR_SERVICE_AVAILABILITY](#gaf55a72ce05def1da08d15a23cee4c5e3)。

服务可用性（Service Availability）。

<a id="r_ga0b5b19caa523e4cb9da8a2bfc6eab20a"></a>

```c
#define BT_SDP_ATTR_PROFILE_DESC_LIST 0x0009
```

相关声明：[BT_SDP_ATTR_PROFILE_DESC_LIST](#ga0b5b19caa523e4cb9da8a2bfc6eab20a)。

蓝牙配置文件描述符列表（Bluetooth Profile Descriptor List）。

<a id="r_gad8302739bca706f6da851d912ada0f82"></a>

```c
#define BT_SDP_ATTR_DOC_URL 0x000a
```

相关声明：[BT_SDP_ATTR_DOC_URL](#gad8302739bca706f6da851d912ada0f82)。

文档 URL（Documentation URL）。

<a id="r_ga0bc613d68dace4cce7a4eec654f5a1e4"></a>

```c
#define BT_SDP_ATTR_CLNT_EXEC_URL 0x000b
```

相关声明：[BT_SDP_ATTR_CLNT_EXEC_URL](#ga0bc613d68dace4cce7a4eec654f5a1e4)。

客户端可执行文件 URL（Client Executable URL）。

<a id="r_ga365048bcb0ad2989aec9dd0d89abbfb9"></a>

```c
#define BT_SDP_ATTR_ICON_URL 0x000c
```

相关声明：[BT_SDP_ATTR_ICON_URL](#ga365048bcb0ad2989aec9dd0d89abbfb9)。

图标 URL（Icon URL）。

<a id="r_gaf7f0b2f30ede36cf280bf31c5e76a99c"></a>

```c
#define BT_SDP_ATTR_ADD_PROTO_DESC_LIST 0x000d
```

相关声明：[BT_SDP_ATTR_ADD_PROTO_DESC_LIST](#gaf7f0b2f30ede36cf280bf31c5e76a99c)。

附加协议描述符列表（Additional Protocol Descriptor List）。

<a id="r_ga15a104c78357f2353cd49eb858de057d"></a>

```c
#define BT_SDP_ATTR_GROUP_ID 0x0200
```

相关声明：[BT_SDP_ATTR_GROUP_ID](#ga15a104c78357f2353cd49eb858de057d)。

组 ID（Group ID）。

<a id="r_ga23a63b424ab381048cb898ebbdb64a02"></a>

```c
#define BT_SDP_ATTR_IP_SUBNET 0x0200
```

相关声明：[BT_SDP_ATTR_IP_SUBNET](#ga23a63b424ab381048cb898ebbdb64a02)。

IP 子网（IP Subnet）。

<a id="r_gab698c476197acca0d499e39f7f246c66"></a>

```c
#define BT_SDP_ATTR_VERSION_NUM_LIST 0x0200
```

相关声明：[BT_SDP_ATTR_VERSION_NUM_LIST](#gab698c476197acca0d499e39f7f246c66)。

版本号列表（Version Number List）。

<a id="r_ga8a693e5265c7801e3c1125473c31445f"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_FEATURES_LIST 0x0200
```

相关声明：[BT_SDP_ATTR_SUPPORTED_FEATURES_LIST](#ga8a693e5265c7801e3c1125473c31445f)。

支持的特性列表（Supported Features List）。

<a id="r_gac7583b3d2a0ebc82e5cf2e6705249201"></a>

```c
#define BT_SDP_ATTR_GOEP_L2CAP_PSM 0x0200
```

相关声明：[BT_SDP_ATTR_GOEP_L2CAP_PSM](#gac7583b3d2a0ebc82e5cf2e6705249201)。

通用对象交换配置文件的 L2CAP PSM（GOEP L2CAP PSM）。

<a id="r_gab8fe8881b4470ab3522e710e36470ddb"></a>

```c
#define BT_SDP_ATTR_SVCDB_STATE 0x0201
```

相关声明：[BT_SDP_ATTR_SVCDB_STATE](#gab8fe8881b4470ab3522e710e36470ddb)。

服务数据库状态（Service Database State）。

<a id="r_ga39b3436f9da303bd2ce1ad38f072ed9f"></a>

```c
#define BT_SDP_ATTR_MPSD_SCENARIOS 0x0200
```

相关声明：[BT_SDP_ATTR_MPSD_SCENARIOS](#ga39b3436f9da303bd2ce1ad38f072ed9f)。

MPSD 场景（MPSD Scenarios）。

<a id="r_gaa3cc3d9a6ac7375e66b0892631698fd0"></a>

```c
#define BT_SDP_ATTR_MPMD_SCENARIOS 0x0201
```

相关声明：[BT_SDP_ATTR_MPMD_SCENARIOS](#gaa3cc3d9a6ac7375e66b0892631698fd0)。

MPMD 场景（MPMD Scenarios）。

<a id="r_ga45795e50564492ac9bce8d6832883741"></a>

```c
#define BT_SDP_ATTR_MPS_DEPENDENCIES 0x0202
```

相关声明：[BT_SDP_ATTR_MPS_DEPENDENCIES](#ga45795e50564492ac9bce8d6832883741)。

支持的配置文件与协议（Supported Profiles & Protocols）。

<a id="r_ga230f70b576c14ba1dbe0cf6eda6220e0"></a>

```c
#define BT_SDP_ATTR_SERVICE_VERSION 0x0300
```

相关声明：[BT_SDP_ATTR_SERVICE_VERSION](#ga230f70b576c14ba1dbe0cf6eda6220e0)。

服务版本（Service Version）。

<a id="r_ga617dc829eb1192cd283bef67a357d75f"></a>

```c
#define BT_SDP_ATTR_EXTERNAL_NETWORK 0x0301
```

相关声明：[BT_SDP_ATTR_EXTERNAL_NETWORK](#ga617dc829eb1192cd283bef67a357d75f)。

外部网络（External Network）。

<a id="r_gae12e2daea8febbbd047c1c3843f56933"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_DATA_STORES_LIST 0x0301
```

相关声明：[BT_SDP_ATTR_SUPPORTED_DATA_STORES_LIST](#gae12e2daea8febbbd047c1c3843f56933)。

支持的数据存储列表（Supported Data Stores List）。

<a id="r_ga4732f83c88de43a90ca3d58a136907b6"></a>

```c
#define BT_SDP_ATTR_DATA_EXCHANGE_SPEC 0x0301
```

相关声明：[BT_SDP_ATTR_DATA_EXCHANGE_SPEC](#ga4732f83c88de43a90ca3d58a136907b6)。

数据交换规范（Data Exchange Specification）。

<a id="r_ga9c78d47f54e82a51f7d04a6f6c97663c"></a>

```c
#define BT_SDP_ATTR_NETWORK 0x0301
```

相关声明：[BT_SDP_ATTR_NETWORK](#ga9c78d47f54e82a51f7d04a6f6c97663c)。

网络（Network）

<a id="r_gaeebfb4a085417db65241b21a27258d84"></a>

```c
#define BT_SDP_ATTR_FAX_CLASS1_SUPPORT 0x0302
```

相关声明：[BT_SDP_ATTR_FAX_CLASS1_SUPPORT](#gaeebfb4a085417db65241b21a27258d84)。

传真类别 1 支持（Fax Class 1 Support）。

<a id="r_gaa122bfee476a8e83346823e23978f7a0"></a>

```c
#define BT_SDP_ATTR_REMOTE_AUDIO_VOLUME_CONTROL 0x0302
```

相关声明：[BT_SDP_ATTR_REMOTE_AUDIO_VOLUME_CONTROL](#gaa122bfee476a8e83346823e23978f7a0)。

远程音频音量控制（Remote Audio Volume Control）。

<a id="r_ga54e285c7a12becef9742093e1777c06b"></a>

```c
#define BT_SDP_ATTR_MCAP_SUPPORTED_PROCEDURES 0x0302
```

相关声明：[BT_SDP_ATTR_MCAP_SUPPORTED_PROCEDURES](#ga54e285c7a12becef9742093e1777c06b)。

多通道适配协议支持的过程（MCAP Supported Procedures）。

<a id="r_ga861470cd4b505d074abb727ba72c088a"></a>

```c
#define BT_SDP_ATTR_FAX_CLASS20_SUPPORT 0x0303
```

相关声明：[BT_SDP_ATTR_FAX_CLASS20_SUPPORT](#ga861470cd4b505d074abb727ba72c088a)。

传真类别 2.0 支持（Fax Class 2.0 Support）。

<a id="r_gac12ed37044c3f12c2d41b1fd23eacada"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_FORMATS_LIST 0x0303
```

相关声明：[BT_SDP_ATTR_SUPPORTED_FORMATS_LIST](#gac12ed37044c3f12c2d41b1fd23eacada)。

支持的格式列表（Supported Formats List）。

<a id="r_ga2475947ccdb9f30ece61a34959fd6ce2"></a>

```c
#define BT_SDP_ATTR_FAX_CLASS2_SUPPORT 0x0304
```

相关声明：[BT_SDP_ATTR_FAX_CLASS2_SUPPORT](#ga2475947ccdb9f30ece61a34959fd6ce2)。

传真类别 2 支持，厂商专用（Fax Class 2 Support (vendor-specific)）。

<a id="r_gac4906f9fa368fbf604830cd5c5fdcb57"></a>

```c
#define BT_SDP_ATTR_AUDIO_FEEDBACK_SUPPORT 0x0305
```

相关声明：[BT_SDP_ATTR_AUDIO_FEEDBACK_SUPPORT](#gac4906f9fa368fbf604830cd5c5fdcb57)。

音频反馈支持（Audio Feedback Support）。

<a id="r_ga74dacfd7807d7f3ec7a7594a9329f0b2"></a>

```c
#define BT_SDP_ATTR_NETWORK_ADDRESS 0x0306
```

相关声明：[BT_SDP_ATTR_NETWORK_ADDRESS](#ga74dacfd7807d7f3ec7a7594a9329f0b2)。

网络地址（Network Address）。

<a id="r_ga1ef964c955473601910ee3997b9ce5cd"></a>

```c
#define BT_SDP_ATTR_WAP_GATEWAY 0x0307
```

相关声明：[BT_SDP_ATTR_WAP_GATEWAY](#ga1ef964c955473601910ee3997b9ce5cd)。

无线应用协议网关（WAP Gateway）。

<a id="r_gafeff5e5b60bd47c44f8edbe8ff7e78a0"></a>

```c
#define BT_SDP_ATTR_HOMEPAGE_URL 0x0308
```

相关声明：[BT_SDP_ATTR_HOMEPAGE_URL](#gafeff5e5b60bd47c44f8edbe8ff7e78a0)。

主页 URL（Homepage URL）。

<a id="r_gae1a3ff84a5588e55258c35ee57d6a5b5"></a>

```c
#define BT_SDP_ATTR_WAP_STACK_TYPE 0x0309
```

相关声明：[BT_SDP_ATTR_WAP_STACK_TYPE](#gae1a3ff84a5588e55258c35ee57d6a5b5)。

无线应用协议栈类型（WAP Stack Type）。

<a id="r_ga21214c2236a5dca24a45998640761e7b"></a>

```c
#define BT_SDP_ATTR_SECURITY_DESC 0x030a
```

相关声明：[BT_SDP_ATTR_SECURITY_DESC](#ga21214c2236a5dca24a45998640761e7b)。

安全描述（Security Description）。

<a id="r_ga13851f9f9a5ba8514d20cffbe5eb9f14"></a>

```c
#define BT_SDP_ATTR_NET_ACCESS_TYPE 0x030b
```

相关声明：[BT_SDP_ATTR_NET_ACCESS_TYPE](#ga13851f9f9a5ba8514d20cffbe5eb9f14)。

网络接入类型（Net Access Type）。

<a id="r_ga7347caab1c7e8755250567d9d8cc7266"></a>

```c
#define BT_SDP_ATTR_MAX_NET_ACCESSRATE 0x030c
```

相关声明：[BT_SDP_ATTR_MAX_NET_ACCESSRATE](#ga7347caab1c7e8755250567d9d8cc7266)。

最大网络接入速率（Max Net Access Rate）。

<a id="r_ga01c0cdb8975484242e6c4b052dabfd91"></a>

```c
#define BT_SDP_ATTR_IP4_SUBNET 0x030d
```

相关声明：[BT_SDP_ATTR_IP4_SUBNET](#ga01c0cdb8975484242e6c4b052dabfd91)。

IPv4 子网（IPv4 Subnet）。

<a id="r_ga10b3d4826904489d474af5e9c21c0831"></a>

```c
#define BT_SDP_ATTR_IP6_SUBNET 0x030e
```

相关声明：[BT_SDP_ATTR_IP6_SUBNET](#ga10b3d4826904489d474af5e9c21c0831)。

IPv6 子网（IPv6 Subnet）。

<a id="r_ga5347dbc038ac9c259d17c14ed9a812d3"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_CAPABILITIES 0x0310
```

相关声明：[BT_SDP_ATTR_SUPPORTED_CAPABILITIES](#ga5347dbc038ac9c259d17c14ed9a812d3)。

基本图像配置文件支持的能力（BIP Supported Capabilities）。

<a id="r_ga498d9beaa7877570fe834d854de36fcb"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_FEATURES 0x0311
```

相关声明：[BT_SDP_ATTR_SUPPORTED_FEATURES](#ga498d9beaa7877570fe834d854de36fcb)。

基本图像配置文件支持的特性（BIP Supported Features）。

<a id="r_gabc7cdfd247da5e2ecfd441c0436471f3"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_FUNCTIONS 0x0312
```

相关声明：[BT_SDP_ATTR_SUPPORTED_FUNCTIONS](#gabc7cdfd247da5e2ecfd441c0436471f3)。

基本图像配置文件支持的功能（BIP Supported Functions）。

<a id="r_gadbce181b739c201070d6abcbdc4139f4"></a>

```c
#define BT_SDP_ATTR_TOTAL_IMAGING_DATA_CAPACITY 0x0313
```

相关声明：[BT_SDP_ATTR_TOTAL_IMAGING_DATA_CAPACITY](#gadbce181b739c201070d6abcbdc4139f4)。

基本图像配置文件总图像数据容量（BIP Total Imaging Data Capacity）。

<a id="r_gada3d989d6c8c0664ba0bf998414a0328"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_REPOSITORIES 0x0314
```

相关声明：[BT_SDP_ATTR_SUPPORTED_REPOSITORIES](#gada3d989d6c8c0664ba0bf998414a0328)。

支持的存储库（Supported Repositories）。

<a id="r_ga03d653957d68b5d0eeda1fa7c9aa4587"></a>

```c
#define BT_SDP_ATTR_MAS_INSTANCE_ID 0x0315
```

相关声明：[BT_SDP_ATTR_MAS_INSTANCE_ID](#ga03d653957d68b5d0eeda1fa7c9aa4587)。

消息访问服务器实例 ID（MAS Instance ID）。

<a id="r_ga41fc674e8571556397135734d28b829a"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_MESSAGE_TYPES 0x0316
```

相关声明：[BT_SDP_ATTR_SUPPORTED_MESSAGE_TYPES](#ga41fc674e8571556397135734d28b829a)。

支持的消息类型（Supported Message Types）。

<a id="r_gaa681b17ebfe013c196cf372dcd030c6e"></a>

```c
#define BT_SDP_ATTR_PBAP_SUPPORTED_FEATURES 0x0317
```

相关声明：[BT_SDP_ATTR_PBAP_SUPPORTED_FEATURES](#gaa681b17ebfe013c196cf372dcd030c6e)。

电话簿访问配置文件支持的特性（PBAP Supported Features）。

<a id="r_gaa50f16945c15f7a954c10dbc8fc394bf"></a>

```c
#define BT_SDP_ATTR_MAP_SUPPORTED_FEATURES 0x0317
```

相关声明：[BT_SDP_ATTR_MAP_SUPPORTED_FEATURES](#gaa50f16945c15f7a954c10dbc8fc394bf)。

消息访问配置文件支持的特性（MAP Supported Features）。

<a id="r_ga4af959fbdfe7cee84008642091df948d"></a>

```c
#define BT_SDP_ATTR_SPECIFICATION_ID 0x0200
```

相关声明：[BT_SDP_ATTR_SPECIFICATION_ID](#ga4af959fbdfe7cee84008642091df948d)。

规范 ID（Specification ID）。

<a id="r_gab5c2534491b43cfc9d2c7e8807b29ff2"></a>

```c
#define BT_SDP_ATTR_VENDOR_ID 0x0201
```

相关声明：[BT_SDP_ATTR_VENDOR_ID](#gab5c2534491b43cfc9d2c7e8807b29ff2)。

厂商标识符（Vendor ID）。

<a id="r_gaac9298efffbcf07303f972a12b50f4b6"></a>

```c
#define BT_SDP_ATTR_PRODUCT_ID 0x0202
```

相关声明：[BT_SDP_ATTR_PRODUCT_ID](#gaac9298efffbcf07303f972a12b50f4b6)。

产品标识符（Product ID）。

<a id="r_gae0f4af728f964ee1c11d86b785575a87"></a>

```c
#define BT_SDP_ATTR_VERSION 0x0203
```

相关声明：[BT_SDP_ATTR_VERSION](#gae0f4af728f964ee1c11d86b785575a87)。

版本（Version）。

<a id="r_ga0868f7d90e3944f105028868511896cf"></a>

```c
#define BT_SDP_ATTR_PRIMARY_RECORD 0x0204
```

相关声明：[BT_SDP_ATTR_PRIMARY_RECORD](#ga0868f7d90e3944f105028868511896cf)。

主记录（Primary Record）。

<a id="r_gad0ac4a65c51ccdf4cd128eb8697e56ca"></a>

```c
#define BT_SDP_ATTR_VENDOR_ID_SOURCE 0x0205
```

相关声明：[BT_SDP_ATTR_VENDOR_ID_SOURCE](#gad0ac4a65c51ccdf4cd128eb8697e56ca)。

厂商 ID 来源（Vendor ID Source）。

<a id="r_gab33be247c7574e985dfb34e3c121dd23"></a>

```c
#define BT_SDP_ATTR_HID_DEVICE_RELEASE_NUMBER 0x0200
```

相关声明：[BT_SDP_ATTR_HID_DEVICE_RELEASE_NUMBER](#gab33be247c7574e985dfb34e3c121dd23)。

人机接口设备发行版本号（HID Device Release Number）。

<a id="r_ga8bb0a4f69b029048958a1395cc98d285"></a>

```c
#define BT_SDP_ATTR_HID_PARSER_VERSION 0x0201
```

相关声明：[BT_SDP_ATTR_HID_PARSER_VERSION](#ga8bb0a4f69b029048958a1395cc98d285)。

人机接口设备解析器版本（HID Parser Version）。

<a id="r_ga43aa99ef47032c04be1bdee571dcfa5c"></a>

```c
#define BT_SDP_ATTR_HID_DEVICE_SUBCLASS 0x0202
```

相关声明：[BT_SDP_ATTR_HID_DEVICE_SUBCLASS](#ga43aa99ef47032c04be1bdee571dcfa5c)。

人机接口设备子类（HID Device Subclass）。

<a id="r_ga5c06a7b07412b0a319656208700ac48e"></a>

```c
#define BT_SDP_ATTR_HID_COUNTRY_CODE 0x0203
```

相关声明：[BT_SDP_ATTR_HID_COUNTRY_CODE](#ga5c06a7b07412b0a319656208700ac48e)。

人机接口设备国家代码（HID Country Code）。

<a id="r_ga26ff5394958b41c5a595952992e0bbbe"></a>

```c
#define BT_SDP_ATTR_HID_VIRTUAL_CABLE 0x0204
```

相关声明：[BT_SDP_ATTR_HID_VIRTUAL_CABLE](#ga26ff5394958b41c5a595952992e0bbbe)。

人机接口设备虚拟线缆（HID Virtual Cable）。

<a id="r_ga30c601e79bd47f29bcc8325ac19a8391"></a>

```c
#define BT_SDP_ATTR_HID_RECONNECT_INITIATE 0x0205
```

相关声明：[BT_SDP_ATTR_HID_RECONNECT_INITIATE](#ga30c601e79bd47f29bcc8325ac19a8391)。

人机接口设备主动重连（HID Reconnect Initiate）。

<a id="r_gaadf6a1c7740d5055e1877142b75d07c2"></a>

```c
#define BT_SDP_ATTR_HID_DESCRIPTOR_LIST 0x0206
```

相关声明：[BT_SDP_ATTR_HID_DESCRIPTOR_LIST](#gaadf6a1c7740d5055e1877142b75d07c2)。

人机接口设备描述符列表（HID Descriptor List）。

<a id="r_ga732063505ff39f236b03646f8b7a78c6"></a>

```c
#define BT_SDP_ATTR_HID_LANG_ID_BASE_LIST 0x0207
```

相关声明：[BT_SDP_ATTR_HID_LANG_ID_BASE_LIST](#ga732063505ff39f236b03646f8b7a78c6)。

人机接口设备语言 ID 基础列表（HID Language ID Base List）。

<a id="r_ga498779c65f410192862aa288cb1e277f"></a>

```c
#define BT_SDP_ATTR_HID_SDP_DISABLE 0x0208
```

相关声明：[BT_SDP_ATTR_HID_SDP_DISABLE](#ga498779c65f410192862aa288cb1e277f)。

人机接口设备 SDP 禁用（HID SDP Disable）。

<a id="r_gac92ef24a03422abdc6ca932e0675aa57"></a>

```c
#define BT_SDP_ATTR_HID_BATTERY_POWER 0x0209
```

相关声明：[BT_SDP_ATTR_HID_BATTERY_POWER](#gac92ef24a03422abdc6ca932e0675aa57)。

人机接口设备电池供电（HID Battery Power）。

<a id="r_ga4bd0452184af1530887b0a785e30fca7"></a>

```c
#define BT_SDP_ATTR_HID_REMOTE_WAKEUP 0x020a
```

相关声明：[BT_SDP_ATTR_HID_REMOTE_WAKEUP](#ga4bd0452184af1530887b0a785e30fca7)。

人机接口设备远程唤醒（HID Remote Wakeup）。

<a id="r_gaa792255345fe4f62062a848aebb220c7"></a>

```c
#define BT_SDP_ATTR_HID_PROFILE_VERSION 0x020b
```

相关声明：[BT_SDP_ATTR_HID_PROFILE_VERSION](#gaa792255345fe4f62062a848aebb220c7)。

人机接口设备配置文件版本（HID Profile Version）。

<a id="r_ga1cd5f256115ef60736eb1089bf66988c"></a>

```c
#define BT_SDP_ATTR_HID_SUPERVISION_TIMEOUT 0x020c
```

相关声明：[BT_SDP_ATTR_HID_SUPERVISION_TIMEOUT](#ga1cd5f256115ef60736eb1089bf66988c)。

人机接口设备监视超时（HID Supervision Timeout）。

<a id="r_ga866194b8e0ec3eebe086998ae0c6e2ab"></a>

```c
#define BT_SDP_ATTR_HID_NORMALLY_CONNECTABLE 0x020d
```

相关声明：[BT_SDP_ATTR_HID_NORMALLY_CONNECTABLE](#ga866194b8e0ec3eebe086998ae0c6e2ab)。

人机接口设备正常可连接状态（HID Normally Connectable）。

<a id="r_ga511980e049b047618f97ac38a4ea3f4e"></a>

```c
#define BT_SDP_ATTR_HID_BOOT_DEVICE 0x020e
```

相关声明：[BT_SDP_ATTR_HID_BOOT_DEVICE](#ga511980e049b047618f97ac38a4ea3f4e)。

人机接口设备引导设备（HID Boot Device）。

<a id="r_gaee523f64ffc9ecdd78bd0482df277e36"></a>

```c
#define BT_SDP_ATTR_HID_SSR_HOST_MAX_LATENCY 0x020f
```

相关声明：[BT_SDP_ATTR_HID_SSR_HOST_MAX_LATENCY](#gaee523f64ffc9ecdd78bd0482df277e36)。

人机接口设备 SSR 主机最大延迟（HID SSR Host Max Latency）。

<a id="r_ga94f31ceeb80af508a03380c2fe03ace7"></a>

```c
#define BT_SDP_ATTR_HID_SSR_HOST_MIN_TIMEOUT 0x0210
```

相关声明：[BT_SDP_ATTR_HID_SSR_HOST_MIN_TIMEOUT](#ga94f31ceeb80af508a03380c2fe03ace7)。

人机接口设备 SSR 主机最小超时（HID SSR Host Min Timeout）。

## 3.8\_协议标识符编码（Protocol identifier codes）

蓝牙服务发现协议（SDP）使用的协议标识符（Protocol Identifiers）。

注意：基于蓝牙分配编号规范（Bluetooth Assigned Numbers Specification）。

`protocol-id` 的可能值列在下方。详情参见分配编号规范（Assigned Numbers Specification）中的“协议标识符（Protocol Identifiers）”一节。

<a id="r_gaa5ae0cf1cd2933005ae70709bea76407"></a>

```c
#define BT_SDP_PROTO_SDP 0x0001
```

相关声明：[BT_SDP_PROTO_SDP](#gaa5ae0cf1cd2933005ae70709bea76407)。

服务发现协议（Service Discovery Protocol）。

<a id="r_gace719188083da9941dcfa76176cdc98c"></a>

```c
#define BT_SDP_PROTO_UDP 0x0002
```

相关声明：[BT_SDP_PROTO_UDP](#gace719188083da9941dcfa76176cdc98c)。

用户数据报协议（User Datagram Protocol）。

<a id="r_ga17056b75f2596fe115d18e42e7f3285e"></a>

```c
#define BT_SDP_PROTO_RFCOMM 0x0003
```

相关声明：[BT_SDP_PROTO_RFCOMM](#ga17056b75f2596fe115d18e42e7f3285e)。

射频通信（Radio Frequency Communication）。

<a id="r_ga7934d7ed5ec1d7a78f9ea17e2c354af9"></a>

```c
#define BT_SDP_PROTO_TCP 0x0004
```

相关声明：[BT_SDP_PROTO_TCP](#ga7934d7ed5ec1d7a78f9ea17e2c354af9)。

传输控制协议（Transmission Control Protocol）。

<a id="r_ga75468f9c406f9940f4d2b0d2d56a9762"></a>

```c
#define BT_SDP_PROTO_TCS_BIN 0x0005
```

相关声明：[BT_SDP_PROTO_TCS_BIN](#ga75468f9c406f9940f4d2b0d2d56a9762)。

电话控制规范二进制协议（Telephony Control Specification Binary）。

<a id="r_ga426cddacc8f6a9e8c502d001d48ecc2f"></a>

```c
#define BT_SDP_PROTO_TCS_AT 0x0006
```

相关声明：[BT_SDP_PROTO_TCS_AT](#ga426cddacc8f6a9e8c502d001d48ecc2f)。

电话控制规范 AT 协议（Telephony Control Specification AT）。

<a id="r_ga772d50f5ea6dbf93bb648e84b8b2ea25"></a>

```c
#define BT_SDP_PROTO_ATT 0x0007
```

相关声明：[BT_SDP_PROTO_ATT](#ga772d50f5ea6dbf93bb648e84b8b2ea25)。

属性协议（Attribute Protocol）。

<a id="r_gab16c910f700b7341742f4d7eedc9d32e"></a>

```c
#define BT_SDP_PROTO_OBEX 0x0008
```

相关声明：[BT_SDP_PROTO_OBEX](#gab16c910f700b7341742f4d7eedc9d32e)。

对象交换协议（Object Exchange Protocol）。

<a id="r_gab6db981f154c92d17a51b7144f1afebe"></a>

```c
#define BT_SDP_PROTO_IP 0x0009
```

相关声明：[BT_SDP_PROTO_IP](#gab6db981f154c92d17a51b7144f1afebe)。

互联网协议（Internet Protocol）。

<a id="r_ga51c5e425f9fc9c785b75c03d2517a2c3"></a>

```c
#define BT_SDP_PROTO_FTP 0x000a
```

相关声明：[BT_SDP_PROTO_FTP](#ga51c5e425f9fc9c785b75c03d2517a2c3)。

文件传输协议（File Transfer Protocol）。

<a id="r_ga103e4968d26d94d56a56a6e4d02b7a9a"></a>

```c
#define BT_SDP_PROTO_HTTP 0x000c
```

相关声明：[BT_SDP_PROTO_HTTP](#ga103e4968d26d94d56a56a6e4d02b7a9a)。

超文本传输协议（HyperText Transfer Protocol）。

<a id="r_ga40525df1204b9e7a3106994eb8b7046e"></a>

```c
#define BT_SDP_PROTO_WSP 0x000e
```

相关声明：[BT_SDP_PROTO_WSP](#ga40525df1204b9e7a3106994eb8b7046e)。

无线会话协议（Wireless Session Protocol）。

<a id="r_ga29032e4ab9a24056a6088ac377444285"></a>

```c
#define BT_SDP_PROTO_BNEP 0x000f
```

相关声明：[BT_SDP_PROTO_BNEP](#ga29032e4ab9a24056a6088ac377444285)。

蓝牙网络封装协议（Bluetooth Network Encapsulation Protocol）。

<a id="r_ga368af07bb117929235af5c0e7b9729f0"></a>

```c
#define BT_SDP_PROTO_UPNP 0x0010
```

相关声明：[BT_SDP_PROTO_UPNP](#ga368af07bb117929235af5c0e7b9729f0)。

通用即插即用（Universal Plug and Play）。

<a id="r_gacb8a22ed2d0045e66d9208b408a6228b"></a>

```c
#define BT_SDP_PROTO_HID 0x0011
```

相关声明：[BT_SDP_PROTO_HID](#gacb8a22ed2d0045e66d9208b408a6228b)。

人机接口设备协议（Human Interface Device Protocol）。

<a id="r_ga9f1bdf155d4f0be01172f971bac67154"></a>

```c
#define BT_SDP_PROTO_HARDCOPY_CTRL 0x0012
```

相关声明：[BT_SDP_PROTO_HARDCOPY_CTRL](#ga9f1bdf155d4f0be01172f971bac67154)。

硬拷贝控制通道（Hardcopy Control Channel）。

<a id="r_ga5095801fa0d28056017725860dc75a93"></a>

```c
#define BT_SDP_PROTO_HARDCOPY_DATA 0x0014
```

相关声明：[BT_SDP_PROTO_HARDCOPY_DATA](#ga5095801fa0d28056017725860dc75a93)。

硬拷贝数据通道（Hardcopy Data Channel）。

<a id="r_gaf17681a3af315b0edaa9c82dd3a7fb89"></a>

```c
#define BT_SDP_PROTO_HARDCOPY_NTF 0x0016
```

相关声明：[BT_SDP_PROTO_HARDCOPY_NTF](#gaf17681a3af315b0edaa9c82dd3a7fb89)。

硬拷贝通知通道（Hardcopy Notification Channel）。

<a id="r_ga4fabbc2e0b5d83cc84c7db7b1a3640b7"></a>

```c
#define BT_SDP_PROTO_AVCTP 0x0017
```

相关声明：[BT_SDP_PROTO_AVCTP](#ga4fabbc2e0b5d83cc84c7db7b1a3640b7)。

音视频控制传输协议（Audio/Video Control Transport Protocol）。

<a id="r_gaa308561679578a5e1d013301b7792eb6"></a>

```c
#define BT_SDP_PROTO_AVDTP 0x0019
```

相关声明：[BT_SDP_PROTO_AVDTP](#gaa308561679578a5e1d013301b7792eb6)。

音视频分发传输协议（Audio/Video Distribution Transport Protocol）。

<a id="r_ga127e2b367475cc074268ad88eb648c63"></a>

```c
#define BT_SDP_PROTO_CMTP 0x001b
```

相关声明：[BT_SDP_PROTO_CMTP](#ga127e2b367475cc074268ad88eb648c63)。

通用 ISDN 访问协议（Common ISDN Access Protocol）。

<a id="r_ga6c6e5cbaea972e982ea608705d2a06cc"></a>

```c
#define BT_SDP_PROTO_MCAP_CTRL 0x001e
```

相关声明：[BT_SDP_PROTO_MCAP_CTRL](#ga6c6e5cbaea972e982ea608705d2a06cc)。

多通道适配协议控制通道（Multi-Channel Adaptation Protocol Control）。

<a id="r_ga19c4608fe6f63fb553706b176ee56a9b"></a>

```c
#define BT_SDP_PROTO_MCAP_DATA 0x001f
```

相关声明：[BT_SDP_PROTO_MCAP_DATA](#ga19c4608fe6f63fb553706b176ee56a9b)。

多通道适配协议数据通道（Multi-Channel Adaptation Protocol Data）。

<a id="r_gac055f0beba2c311e9f098217fc721a75"></a>

```c
#define BT_SDP_PROTO_L2CAP 0x0100
```

相关声明：[BT_SDP_PROTO_L2CAP](#gac055f0beba2c311e9f098217fc721a75)。

逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol）。

## 3.9\_SDP 协议数据单元中的数据表示（蓝牙 SDP 规范第 339、340 页）（The Data representation in SDP PDUs (pps 339, 340 of BT SDP Spec)）

这些值就是写入协议数据单元（PDU）缓冲区的数据类型与大小描述符（Data Type + Size Descriptor）的精确编码值。

数据类型占前 5 位，大小描述符（Size Descriptor）占后 3 位，总计 8 位。大小描述符至关重要，它决定从 PDU 中为数据值提取多少字节。

对于大多数基本类型，数据类型与大小描述符（Data Type + Size Descriptor）的组合很直接；但对于构造类型（Constructed Types）和字符串，数据大小存放在该 8 位描述符之后的下 `n` 个字节中。`n` 的确切值由数据大小描述符的 3 位指定。

文本字符串（TextString）和 URL 字符串（URLString）的大小可为 `2^{8, 16, 32}` 字节；数据序列（DataSequence）和数据序列备选项（DataSequenceAlternates）的大小也可为 `2^{8, 16, 32}`。这些大小在 API 中事后计算，事先并不知道。译注：幂次表达式沿用官方原文；前文的 8／16／32 位指长度字段的宽度。

对于 `BT_SDP_UINT128`、`BT_SDP_INT128` 和 `BT_SDP_UUID128` 类型，数据字节序应为小端（Little-endian）。例如，串口配置文件（SPP）的 UUID128 `00001101-0000-1000-8000-00805F9B34FB` 表示为 `{0xFB, 0x34, 0x9B, 0x5F, 0x80, 0x00, 0x00, 0x80, 0x00, 0x10, 0x00, 0x00, 0x01, 0x11, 0x00, 0x00}`。128 位 UUID 的数组使用 `BT_SDP_ARRAY_UUID_128` 声明。

<a id="r_ga36f257de103356c3ebeb55e23186ed99"></a>

```c
#define BT_SDP_DATA_NIL 0x00
```

相关声明：[BT_SDP_DATA_NIL](#ga36f257de103356c3ebeb55e23186ed99)。

Nil，空类型（Nil, the null type）。

<a id="r_ga546a46c2aa7eb3306eb46768fb8737a4"></a>

```c
#define BT_SDP_UINT8 0x08
```

相关声明：[BT_SDP_UINT8](#ga546a46c2aa7eb3306eb46768fb8737a4)。

无符号 8 位整数（Unsigned 8-bit integer）。

<a id="r_ga1129f3a1364f29c9ce36f6f74ca21327"></a>

```c
#define BT_SDP_UINT16 0x09
```

相关声明：[BT_SDP_UINT16](#ga1129f3a1364f29c9ce36f6f74ca21327)。

无符号 16 位整数（Unsigned 16-bit integer）。

<a id="r_ga4f3bcb36dfce975c2d9ab68894a9e49c"></a>

```c
#define BT_SDP_UINT32 0x0a
```

相关声明：[BT_SDP_UINT32](#ga4f3bcb36dfce975c2d9ab68894a9e49c)。

无符号 32 位整数（Unsigned 32-bit integer）。

<a id="r_ga11261bf1c63a6d463ed41225c1e1a0c7"></a>

```c
#define BT_SDP_UINT64 0x0b
```

相关声明：[BT_SDP_UINT64](#ga11261bf1c63a6d463ed41225c1e1a0c7)。

无符号 64 位整数（Unsigned 64-bit integer）。

<a id="r_ga9a815c6efe976f29e9f6f35a566245fd"></a>

```c
#define BT_SDP_UINT128 0x0c
```

相关声明：[BT_SDP_UINT128](#ga9a815c6efe976f29e9f6f35a566245fd)。

无符号 128 位整数（Unsigned 128-bit integer）。

<a id="r_gaeed1818ca1bf762b23ab2bfcd18b8a66"></a>

```c
#define BT_SDP_INT8 0x10
```

相关声明：[BT_SDP_INT8](#gaeed1818ca1bf762b23ab2bfcd18b8a66)。

有符号 8 位整数（Signed 8-bit integer）。

<a id="r_gaf6a3795d22cff4a522a2225339fb5a57"></a>

```c
#define BT_SDP_INT16 0x11
```

相关声明：[BT_SDP_INT16](#gaf6a3795d22cff4a522a2225339fb5a57)。

有符号 16 位整数（Signed 16-bit integer）。

<a id="r_ga0ad987ebeac3dab3ef2196f4dfeca1ab"></a>

```c
#define BT_SDP_INT32 0x12
```

相关声明：[BT_SDP_INT32](#ga0ad987ebeac3dab3ef2196f4dfeca1ab)。

有符号 32 位整数（Signed 32-bit integer）。

<a id="r_gaae793fef5690c6013e6e0e34ededb75f"></a>

```c
#define BT_SDP_INT64 0x13
```

相关声明：[BT_SDP_INT64](#gaae793fef5690c6013e6e0e34ededb75f)。

有符号 64 位整数（Signed 64-bit integer）。

<a id="r_gaf754bbfd9cdc0e6a2bf7d6c46fab3f29"></a>

```c
#define BT_SDP_INT128 0x14
```

相关声明：[BT_SDP_INT128](#gaf754bbfd9cdc0e6a2bf7d6c46fab3f29)。

有符号 128 位整数（Signed 128-bit integer）。

<a id="r_ga4f829572cca9669a8a96a857874bb022"></a>

```c
#define BT_SDP_UUID_UNSPEC 0x18
```

相关声明：[BT_SDP_UUID_UNSPEC](#ga4f829572cca9669a8a96a857874bb022)。

通用唯一标识符，未指定大小（UUID, unspecified size）。

<a id="r_ga45598f1c663acd3a3e5a409696cb3d2f"></a>

```c
#define BT_SDP_UUID16 0x19
```

相关声明：[BT_SDP_UUID16](#ga45598f1c663acd3a3e5a409696cb3d2f)。

通用唯一标识符，16 位（UUID, 16-bit）。

<a id="r_ga78245bb059feb3ec039e05aba24746e7"></a>

```c
#define BT_SDP_UUID32 0x1a
```

相关声明：[BT_SDP_UUID32](#ga78245bb059feb3ec039e05aba24746e7)。

通用唯一标识符，32 位（UUID, 32-bit）。

<a id="r_gaadf48ba3e96687fff99ff58789d79a50"></a>

```c
#define BT_SDP_UUID128 0x1c
```

相关声明：[BT_SDP_UUID128](#gaadf48ba3e96687fff99ff58789d79a50)。

通用唯一标识符，128 位（UUID, 128-bit）。

<a id="r_gaca9942a42701cda835a5bf7b7aaf1d75"></a>

```c
#define BT_SDP_TEXT_STR_UNSPEC 0x20
```

相关声明：[BT_SDP_TEXT_STR_UNSPEC](#gaca9942a42701cda835a5bf7b7aaf1d75)。

文本字符串，未指定大小（Text string, unspecified size）。

<a id="r_ga885ace6b1def91f3fa4dd16cb391d2b8"></a>

```c
#define BT_SDP_TEXT_STR8 0x25
```

相关声明：[BT_SDP_TEXT_STR8](#ga885ace6b1def91f3fa4dd16cb391d2b8)。

文本字符串，长度字段为 8 位（Text string, 8-bit length）。

<a id="r_gaa5301cdac5fc9299837f29b92aa3c10b"></a>

```c
#define BT_SDP_TEXT_STR16 0x26
```

相关声明：[BT_SDP_TEXT_STR16](#gaa5301cdac5fc9299837f29b92aa3c10b)。

文本字符串，长度字段为 16 位（Text string, 16-bit length）。

<a id="r_ga29657a21117a3fbe05942778a8d7637e"></a>

```c
#define BT_SDP_TEXT_STR32 0x27
```

相关声明：[BT_SDP_TEXT_STR32](#ga29657a21117a3fbe05942778a8d7637e)。

文本字符串，长度字段为 32 位（Text string, 32-bit length）。

<a id="r_gac48f198f6609fac95db69c09ac69efab"></a>

```c
#define BT_SDP_BOOL 0x28
```

相关声明：[BT_SDP_BOOL](#gac48f198f6609fac95db69c09ac69efab)。

布尔值（Boolean）。

<a id="r_gaa884191d772bfa24484cb33c0f614334"></a>

```c
#define BT_SDP_SEQ_UNSPEC 0x30
```

相关声明：[BT_SDP_SEQ_UNSPEC](#gaa884191d772bfa24484cb33c0f614334)。

数据元素序列，未指定大小（Data element sequence, unspecified size）。

<a id="r_ga5a64e3bec70b40114a3160dbfb1e484b"></a>

```c
#define BT_SDP_SEQ8 0x35
```

相关声明：[BT_SDP_SEQ8](#ga5a64e3bec70b40114a3160dbfb1e484b)。

数据元素序列，长度字段为 8 位（Data element sequence, 8-bit length）。

<a id="r_gadf5b15a0296a872ffefc24bbc90dc45b"></a>

```c
#define BT_SDP_SEQ16 0x36
```

相关声明：[BT_SDP_SEQ16](#gadf5b15a0296a872ffefc24bbc90dc45b)。

数据元素序列，长度字段为 16 位（Data element sequence, 16-bit length）。

<a id="r_ga639e86b5103168917cb7202100e3124d"></a>

```c
#define BT_SDP_SEQ32 0x37
```

相关声明：[BT_SDP_SEQ32](#ga639e86b5103168917cb7202100e3124d)。

数据元素序列，长度字段为 32 位（Data element sequence, 32-bit length）。

<a id="r_gaee1bd735929cb2c4bca48cc7663407fd"></a>

```c
#define BT_SDP_ALT_UNSPEC 0x38
```

相关声明：[BT_SDP_ALT_UNSPEC](#gaee1bd735929cb2c4bca48cc7663407fd)。

数据元素备选项，未指定大小（Data element alternative, unspecified size）。

<a id="r_gab7460f41f05a418d58f4b6807d84cb40"></a>

```c
#define BT_SDP_ALT8 0x3d
```

相关声明：[BT_SDP_ALT8](#gab7460f41f05a418d58f4b6807d84cb40)。

数据元素备选项，长度字段为 8 位（Data element alternative, 8-bit length）。

<a id="r_gab976bc87f0dcba0e4bc61575ea04ccc7"></a>

```c
#define BT_SDP_ALT16 0x3e
```

相关声明：[BT_SDP_ALT16](#gab976bc87f0dcba0e4bc61575ea04ccc7)。

数据元素备选项，长度字段为 16 位（Data element alternative, 16-bit length）。

<a id="r_ga420936f672ae31ca701ae277b69d592a"></a>

```c
#define BT_SDP_ALT32 0x3f
```

相关声明：[BT_SDP_ALT32](#ga420936f672ae31ca701ae277b69d592a)。

数据元素备选项，长度字段为 32 位（Data element alternative, 32-bit length）。

<a id="r_ga32a7a79422f52b75c2eb2d2eb467dc00"></a>

```c
#define BT_SDP_URL_STR_UNSPEC 0x40
```

相关声明：[BT_SDP_URL_STR_UNSPEC](#ga32a7a79422f52b75c2eb2d2eb467dc00)。

URL 字符串，未指定大小（URL string, unspecified size）。

<a id="r_gafb2a77d6097c8c4cf9f01b7e16df26f1"></a>

```c
#define BT_SDP_URL_STR8 0x45
```

相关声明：[BT_SDP_URL_STR8](#gafb2a77d6097c8c4cf9f01b7e16df26f1)。

URL 字符串，长度字段为 8 位（URL string, 8-bit length）。

<a id="r_gac1acc712468e5af1f54022ac3551882a"></a>

```c
#define BT_SDP_URL_STR16 0x46
```

相关声明：[BT_SDP_URL_STR16](#gac1acc712468e5af1f54022ac3551882a)。

URL 字符串，长度字段为 16 位（URL string, 16-bit length）。

<a id="r_ga37476681e9d4eee53b710c44e2da9a2f"></a>

```c
#define BT_SDP_URL_STR32 0x47
```

相关声明：[BT_SDP_URL_STR32](#ga37476681e9d4eee53b710c44e2da9a2f)。

URL 字符串，长度字段为 32 位（URL string, 32-bit length）。

## 3.10\_详细说明（Detailed Documentation）

<a id="ga2fdc3eb32196b5135b7f595a36cacb4c"></a>

### `BT_SDP_ADVANCED_AUDIO_SVCLASS`

```c
#define BT_SDP_ADVANCED_AUDIO_SVCLASS 0x110d
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

高级音频分发（Advanced Audio Distribution）。

<a id="gab976bc87f0dcba0e4bc61575ea04ccc7"></a>

### `BT_SDP_ALT16`

```c
#define BT_SDP_ALT16 0x3e
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

数据元素备选项，长度字段为 16 位（Data element alternative, 16-bit length）。

<a id="ga420936f672ae31ca701ae277b69d592a"></a>

### `BT_SDP_ALT32`

```c
#define BT_SDP_ALT32 0x3f
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

数据元素备选项，长度字段为 32 位（Data element alternative, 32-bit length）。

<a id="gab7460f41f05a418d58f4b6807d84cb40"></a>

### `BT_SDP_ALT8`

```c
#define BT_SDP_ALT8 0x3d
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

数据元素备选项，长度字段为 8 位（Data element alternative, 8-bit length）。

<a id="gaee1bd735929cb2c4bca48cc7663407fd"></a>

### `BT_SDP_ALT_UNSPEC`

```c
#define BT_SDP_ALT_UNSPEC 0x38
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

数据元素备选项，未指定大小（Data element alternative, unspecified size）。

<a id="ga694b04c2dae3b06b7fd66640468a5a38"></a>

### `BT_SDP_APPLE_AGENT_SVCLASS`

```c
#define BT_SDP_APPLE_AGENT_SVCLASS 0x2112
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

Apple 代理（Apple Agent）。

<a id="gaa4bb67164ae1f16b26081668d00f45c7"></a>

### `BT_SDP_ARRAY_16`

```c
#define BT_SDP_ARRAY_16 ( ...)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
((uint16_t[]) {__VA_ARGS__})
```

在属性（Attribute）中声明由 16 位元素组成的数组。

<a id="ga7a17ee4872190a087cf2e5ea4db9e737"></a>

### `BT_SDP_ARRAY_32`

```c
#define BT_SDP_ARRAY_32 ( ...)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
((uint32_t[]) {__VA_ARGS__})
```

在属性（Attribute）中声明由 32 位元素组成的数组。

<a id="gaef264fa3621c3df7a164128bb95b30fc"></a>

### `BT_SDP_ARRAY_8`

```c
#define BT_SDP_ARRAY_8 ( ...)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
((uint8_t[]) {__VA_ARGS__})
```

在属性（Attribute）中声明由 8 位元素组成的数组。

<a id="gadbdfa913e11ed7b8e691a1fc1712e6eb"></a>

### `BT_SDP_ARRAY_UUID_128`

```c
#define BT_SDP_ARRAY_UUID_128 ( w32, w1, w2, w3, w48 )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
BT_SDP_ARRAY_8(BT_UUID_128_ENCODE(w32, w1, w2, w3, w48))
```

在属性中声明采用小端字节序（Little-endian）的 128 位 UUID。

用于根据可读 UUID 表示形式初始化 128 位 UUID 数组值的辅助宏（Helper Macro）。

以下示例演示如何声明 UUID `6E400001-B5A3-F393-E0A9-E50E24DCCA9E`。

原始示例（Example）：

```c
BT_SDP_ARRAY_UUID_128(0x6E400001, 0xB5A3, 0xF393, 0xE0A9, 0xE50E24DCCA9E)
```

只需将连字符替换为逗号，并加上 `0x` 前缀（Prefix）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `w32` | UUID 的第一部分（First Part），32 位。 |
| `w1` | UUID 的第二部分（Second Part），16 位。 |
| `w2` | UUID 的第三部分（Third Part），16 位。 |
| `w3` | UUID 的第四部分（Fourth Part），16 位。 |
| `w48` | UUID 的第五部分（Fifth Part），48 位。 |

**返回（Returns）**：返回值（Returns）：128 位 UUID 的逗号分隔值。

<a id="gaf7f0b2f30ede36cf280bf31c5e76a99c"></a>

### `BT_SDP_ATTR_ADD_PROTO_DESC_LIST`

```c
#define BT_SDP_ATTR_ADD_PROTO_DESC_LIST 0x000d
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

附加协议描述符列表（Additional Protocol Descriptor List）。

<a id="gac4906f9fa368fbf604830cd5c5fdcb57"></a>

### `BT_SDP_ATTR_AUDIO_FEEDBACK_SUPPORT`

```c
#define BT_SDP_ATTR_AUDIO_FEEDBACK_SUPPORT 0x0305
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

音频反馈支持（Audio Feedback Support）。

<a id="ga2609212bf5400c31351bc3ec5f60a7e1"></a>

### `BT_SDP_ATTR_BROWSE_GRP_LIST`

```c
#define BT_SDP_ATTR_BROWSE_GRP_LIST 0x0005
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

浏览组列表（Browse Group List）。

<a id="ga0bc613d68dace4cce7a4eec654f5a1e4"></a>

### `BT_SDP_ATTR_CLNT_EXEC_URL`

```c
#define BT_SDP_ATTR_CLNT_EXEC_URL 0x000b
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

客户端可执行文件 URL（Client Executable URL）。

<a id="ga4732f83c88de43a90ca3d58a136907b6"></a>

### `BT_SDP_ATTR_DATA_EXCHANGE_SPEC`

```c
#define BT_SDP_ATTR_DATA_EXCHANGE_SPEC 0x0301
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

数据交换规范（Data Exchange Specification）。

<a id="gad8302739bca706f6da851d912ada0f82"></a>

### `BT_SDP_ATTR_DOC_URL`

```c
#define BT_SDP_ATTR_DOC_URL 0x000a
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

文档 URL（Documentation URL）。

<a id="ga617dc829eb1192cd283bef67a357d75f"></a>

### `BT_SDP_ATTR_EXTERNAL_NETWORK`

```c
#define BT_SDP_ATTR_EXTERNAL_NETWORK 0x0301
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

外部网络（External Network）。

<a id="gaeebfb4a085417db65241b21a27258d84"></a>

### `BT_SDP_ATTR_FAX_CLASS1_SUPPORT`

```c
#define BT_SDP_ATTR_FAX_CLASS1_SUPPORT 0x0302
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

传真类别 1 支持（Fax Class 1 Support）。

<a id="ga861470cd4b505d074abb727ba72c088a"></a>

### `BT_SDP_ATTR_FAX_CLASS20_SUPPORT`

```c
#define BT_SDP_ATTR_FAX_CLASS20_SUPPORT 0x0303
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

传真类别 2.0 支持（Fax Class 2.0 Support）。

<a id="ga2475947ccdb9f30ece61a34959fd6ce2"></a>

### `BT_SDP_ATTR_FAX_CLASS2_SUPPORT`

```c
#define BT_SDP_ATTR_FAX_CLASS2_SUPPORT 0x0304
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

传真类别 2 支持，厂商专用（Fax Class 2 Support (vendor-specific)）。

<a id="gac7583b3d2a0ebc82e5cf2e6705249201"></a>

### `BT_SDP_ATTR_GOEP_L2CAP_PSM`

```c
#define BT_SDP_ATTR_GOEP_L2CAP_PSM 0x0200
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用对象交换配置文件的 L2CAP PSM（GOEP L2CAP PSM）。

<a id="ga15a104c78357f2353cd49eb858de057d"></a>

### `BT_SDP_ATTR_GROUP_ID`

```c
#define BT_SDP_ATTR_GROUP_ID 0x0200
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

组 ID（Group ID）。

<a id="gac92ef24a03422abdc6ca932e0675aa57"></a>

### `BT_SDP_ATTR_HID_BATTERY_POWER`

```c
#define BT_SDP_ATTR_HID_BATTERY_POWER 0x0209
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备电池供电（HID Battery Power）。

<a id="ga511980e049b047618f97ac38a4ea3f4e"></a>

### `BT_SDP_ATTR_HID_BOOT_DEVICE`

```c
#define BT_SDP_ATTR_HID_BOOT_DEVICE 0x020e
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备引导设备（HID Boot Device）。

<a id="ga5c06a7b07412b0a319656208700ac48e"></a>

### `BT_SDP_ATTR_HID_COUNTRY_CODE`

```c
#define BT_SDP_ATTR_HID_COUNTRY_CODE 0x0203
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备国家代码（HID Country Code）。

<a id="gaadf6a1c7740d5055e1877142b75d07c2"></a>

### `BT_SDP_ATTR_HID_DESCRIPTOR_LIST`

```c
#define BT_SDP_ATTR_HID_DESCRIPTOR_LIST 0x0206
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备描述符列表（HID Descriptor List）。

<a id="gab33be247c7574e985dfb34e3c121dd23"></a>

### `BT_SDP_ATTR_HID_DEVICE_RELEASE_NUMBER`

```c
#define BT_SDP_ATTR_HID_DEVICE_RELEASE_NUMBER 0x0200
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备发行版本号（HID Device Release Number）。

<a id="ga43aa99ef47032c04be1bdee571dcfa5c"></a>

### `BT_SDP_ATTR_HID_DEVICE_SUBCLASS`

```c
#define BT_SDP_ATTR_HID_DEVICE_SUBCLASS 0x0202
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备子类（HID Device Subclass）。

<a id="ga732063505ff39f236b03646f8b7a78c6"></a>

### `BT_SDP_ATTR_HID_LANG_ID_BASE_LIST`

```c
#define BT_SDP_ATTR_HID_LANG_ID_BASE_LIST 0x0207
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备语言 ID 基础列表（HID Language ID Base List）。

<a id="ga866194b8e0ec3eebe086998ae0c6e2ab"></a>

### `BT_SDP_ATTR_HID_NORMALLY_CONNECTABLE`

```c
#define BT_SDP_ATTR_HID_NORMALLY_CONNECTABLE 0x020d
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备正常可连接状态（HID Normally Connectable）。

<a id="ga8bb0a4f69b029048958a1395cc98d285"></a>

### `BT_SDP_ATTR_HID_PARSER_VERSION`

```c
#define BT_SDP_ATTR_HID_PARSER_VERSION 0x0201
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备解析器版本（HID Parser Version）。

<a id="gaa792255345fe4f62062a848aebb220c7"></a>

### `BT_SDP_ATTR_HID_PROFILE_VERSION`

```c
#define BT_SDP_ATTR_HID_PROFILE_VERSION 0x020b
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备配置文件版本（HID Profile Version）。

<a id="ga30c601e79bd47f29bcc8325ac19a8391"></a>

### `BT_SDP_ATTR_HID_RECONNECT_INITIATE`

```c
#define BT_SDP_ATTR_HID_RECONNECT_INITIATE 0x0205
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备主动重连（HID Reconnect Initiate）。

<a id="ga4bd0452184af1530887b0a785e30fca7"></a>

### `BT_SDP_ATTR_HID_REMOTE_WAKEUP`

```c
#define BT_SDP_ATTR_HID_REMOTE_WAKEUP 0x020a
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备远程唤醒（HID Remote Wakeup）。

<a id="ga498779c65f410192862aa288cb1e277f"></a>

### `BT_SDP_ATTR_HID_SDP_DISABLE`

```c
#define BT_SDP_ATTR_HID_SDP_DISABLE 0x0208
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备 SDP 禁用（HID SDP Disable）。

<a id="gaee523f64ffc9ecdd78bd0482df277e36"></a>

### `BT_SDP_ATTR_HID_SSR_HOST_MAX_LATENCY`

```c
#define BT_SDP_ATTR_HID_SSR_HOST_MAX_LATENCY 0x020f
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备 SSR 主机最大延迟（HID SSR Host Max Latency）。

<a id="ga94f31ceeb80af508a03380c2fe03ace7"></a>

### `BT_SDP_ATTR_HID_SSR_HOST_MIN_TIMEOUT`

```c
#define BT_SDP_ATTR_HID_SSR_HOST_MIN_TIMEOUT 0x0210
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备 SSR 主机最小超时（HID SSR Host Min Timeout）。

<a id="ga1cd5f256115ef60736eb1089bf66988c"></a>

### `BT_SDP_ATTR_HID_SUPERVISION_TIMEOUT`

```c
#define BT_SDP_ATTR_HID_SUPERVISION_TIMEOUT 0x020c
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备监视超时（HID Supervision Timeout）。

<a id="ga26ff5394958b41c5a595952992e0bbbe"></a>

### `BT_SDP_ATTR_HID_VIRTUAL_CABLE`

```c
#define BT_SDP_ATTR_HID_VIRTUAL_CABLE 0x0204
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备虚拟线缆（HID Virtual Cable）。

<a id="gafeff5e5b60bd47c44f8edbe8ff7e78a0"></a>

### `BT_SDP_ATTR_HOMEPAGE_URL`

```c
#define BT_SDP_ATTR_HOMEPAGE_URL 0x0308
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

主页 URL（Homepage URL）。

<a id="ga365048bcb0ad2989aec9dd0d89abbfb9"></a>

### `BT_SDP_ATTR_ICON_URL`

```c
#define BT_SDP_ATTR_ICON_URL 0x000c
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

图标 URL（Icon URL）。

<a id="ga920e61b784c4ae47bc51ac5c46273220"></a>

### `BT_SDP_ATTR_ID_RANGE`

```c
#define BT_SDP_ATTR_ID_RANGE ( beginning, ending )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
{(beginning), (ending)}
```

初始化 SDP 属性 ID 范围（Attribute ID Range）。

<a id="ga01c0cdb8975484242e6c4b052dabfd91"></a>

### `BT_SDP_ATTR_IP4_SUBNET`

```c
#define BT_SDP_ATTR_IP4_SUBNET 0x030d
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

IPv4 子网（IPv4 Subnet）。

<a id="ga10b3d4826904489d474af5e9c21c0831"></a>

### `BT_SDP_ATTR_IP6_SUBNET`

```c
#define BT_SDP_ATTR_IP6_SUBNET 0x030e
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

IPv6 子网（IPv6 Subnet）。

<a id="ga23a63b424ab381048cb898ebbdb64a02"></a>

### `BT_SDP_ATTR_IP_SUBNET`

```c
#define BT_SDP_ATTR_IP_SUBNET 0x0200
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

IP 子网（IP Subnet）。

<a id="ga462ec997a81c6b439a24e2de085676ab"></a>

### `BT_SDP_ATTR_LANG_BASE_ATTR_ID_LIST`

```c
#define BT_SDP_ATTR_LANG_BASE_ATTR_ID_LIST 0x0006
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

语言基础属性 ID 列表（Language Base Attribute ID List）。

<a id="gaa50f16945c15f7a954c10dbc8fc394bf"></a>

### `BT_SDP_ATTR_MAP_SUPPORTED_FEATURES`

```c
#define BT_SDP_ATTR_MAP_SUPPORTED_FEATURES 0x0317
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

消息访问配置文件支持的特性（MAP Supported Features）。

<a id="ga03d653957d68b5d0eeda1fa7c9aa4587"></a>

### `BT_SDP_ATTR_MAS_INSTANCE_ID`

```c
#define BT_SDP_ATTR_MAS_INSTANCE_ID 0x0315
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

消息访问服务器实例 ID（MAS Instance ID）。

<a id="ga7347caab1c7e8755250567d9d8cc7266"></a>

### `BT_SDP_ATTR_MAX_NET_ACCESSRATE`

```c
#define BT_SDP_ATTR_MAX_NET_ACCESSRATE 0x030c
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

最大网络接入速率（Max Net Access Rate）。

<a id="ga54e285c7a12becef9742093e1777c06b"></a>

### `BT_SDP_ATTR_MCAP_SUPPORTED_PROCEDURES`

```c
#define BT_SDP_ATTR_MCAP_SUPPORTED_PROCEDURES 0x0302
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

多通道适配协议支持的过程（MCAP Supported Procedures）。

<a id="gaa3cc3d9a6ac7375e66b0892631698fd0"></a>

### `BT_SDP_ATTR_MPMD_SCENARIOS`

```c
#define BT_SDP_ATTR_MPMD_SCENARIOS 0x0201
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

MPMD 场景（MPMD Scenarios）。

<a id="ga45795e50564492ac9bce8d6832883741"></a>

### `BT_SDP_ATTR_MPS_DEPENDENCIES`

```c
#define BT_SDP_ATTR_MPS_DEPENDENCIES 0x0202
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

支持的配置文件与协议（Supported Profiles & Protocols）。

<a id="ga39b3436f9da303bd2ce1ad38f072ed9f"></a>

### `BT_SDP_ATTR_MPSD_SCENARIOS`

```c
#define BT_SDP_ATTR_MPSD_SCENARIOS 0x0200
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

MPSD 场景（MPSD Scenarios）。

<a id="ga13851f9f9a5ba8514d20cffbe5eb9f14"></a>

### `BT_SDP_ATTR_NET_ACCESS_TYPE`

```c
#define BT_SDP_ATTR_NET_ACCESS_TYPE 0x030b
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

网络接入类型（Net Access Type）。

<a id="ga9c78d47f54e82a51f7d04a6f6c97663c"></a>

### `BT_SDP_ATTR_NETWORK`

```c
#define BT_SDP_ATTR_NETWORK 0x0301
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

网络（Network）

<a id="ga74dacfd7807d7f3ec7a7594a9329f0b2"></a>

### `BT_SDP_ATTR_NETWORK_ADDRESS`

```c
#define BT_SDP_ATTR_NETWORK_ADDRESS 0x0306
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

网络地址（Network Address）。

<a id="gaa681b17ebfe013c196cf372dcd030c6e"></a>

### `BT_SDP_ATTR_PBAP_SUPPORTED_FEATURES`

```c
#define BT_SDP_ATTR_PBAP_SUPPORTED_FEATURES 0x0317
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

电话簿访问配置文件支持的特性（PBAP Supported Features）。

<a id="ga0868f7d90e3944f105028868511896cf"></a>

### `BT_SDP_ATTR_PRIMARY_RECORD`

```c
#define BT_SDP_ATTR_PRIMARY_RECORD 0x0204
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

主记录（Primary Record）。

<a id="gaac9298efffbcf07303f972a12b50f4b6"></a>

### `BT_SDP_ATTR_PRODUCT_ID`

```c
#define BT_SDP_ATTR_PRODUCT_ID 0x0202
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

产品标识符（Product ID）。

<a id="ga0b5b19caa523e4cb9da8a2bfc6eab20a"></a>

### `BT_SDP_ATTR_PROFILE_DESC_LIST`

```c
#define BT_SDP_ATTR_PROFILE_DESC_LIST 0x0009
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

蓝牙配置文件描述符列表（Bluetooth Profile Descriptor List）。

<a id="ga3e7dad966deab42ff9fa0fd04d3d4514"></a>

### `BT_SDP_ATTR_PROTO_DESC_LIST`

```c
#define BT_SDP_ATTR_PROTO_DESC_LIST 0x0004
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

协议描述符列表（Protocol Descriptor List）。

<a id="gab8b0110be857d6eca206e00c3b5e373a"></a>

### `BT_SDP_ATTR_PROVNAME_PRIMARY`

```c
#define BT_SDP_ATTR_PROVNAME_PRIMARY (0x0002 + BT_SDP_PRIMARY_LANG_BASE)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="ga38f32cae462272b51eb4edca0c5c95a2"></a>

### `BT_SDP_ATTR_RECORD_HANDLE`

```c
#define BT_SDP_ATTR_RECORD_HANDLE 0x0000
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

服务记录句柄（Service Record Handle）。

<a id="ga4d458591f8eba26feaab1220c49f6a29"></a>

### `BT_SDP_ATTR_RECORD_STATE`

```c
#define BT_SDP_ATTR_RECORD_STATE 0x0002
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

服务记录状态（Service Record State）。

<a id="gaa122bfee476a8e83346823e23978f7a0"></a>

### `BT_SDP_ATTR_REMOTE_AUDIO_VOLUME_CONTROL`

```c
#define BT_SDP_ATTR_REMOTE_AUDIO_VOLUME_CONTROL 0x0302
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

远程音频音量控制（Remote Audio Volume Control）。

<a id="ga21214c2236a5dca24a45998640761e7b"></a>

### `BT_SDP_ATTR_SECURITY_DESC`

```c
#define BT_SDP_ATTR_SECURITY_DESC 0x030a
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

安全描述（Security Description）。

<a id="gaf55a72ce05def1da08d15a23cee4c5e3"></a>

### `BT_SDP_ATTR_SERVICE_AVAILABILITY`

```c
#define BT_SDP_ATTR_SERVICE_AVAILABILITY 0x0008
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

服务可用性（Service Availability）。

<a id="gad2149fd761f7ae2ea6ef761ab2545ab4"></a>

### `BT_SDP_ATTR_SERVICE_ID`

```c
#define BT_SDP_ATTR_SERVICE_ID 0x0003
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

服务 ID（Service ID）。

<a id="ga230f70b576c14ba1dbe0cf6eda6220e0"></a>

### `BT_SDP_ATTR_SERVICE_VERSION`

```c
#define BT_SDP_ATTR_SERVICE_VERSION 0x0300
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

服务版本（Service Version）。

<a id="ga4af959fbdfe7cee84008642091df948d"></a>

### `BT_SDP_ATTR_SPECIFICATION_ID`

```c
#define BT_SDP_ATTR_SPECIFICATION_ID 0x0200
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

规范 ID（Specification ID）。

<a id="ga5347dbc038ac9c259d17c14ed9a812d3"></a>

### `BT_SDP_ATTR_SUPPORTED_CAPABILITIES`

```c
#define BT_SDP_ATTR_SUPPORTED_CAPABILITIES 0x0310
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

基本图像配置文件支持的能力（BIP Supported Capabilities）。

<a id="gae12e2daea8febbbd047c1c3843f56933"></a>

### `BT_SDP_ATTR_SUPPORTED_DATA_STORES_LIST`

```c
#define BT_SDP_ATTR_SUPPORTED_DATA_STORES_LIST 0x0301
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

支持的数据存储列表（Supported Data Stores List）。

<a id="ga498d9beaa7877570fe834d854de36fcb"></a>

### `BT_SDP_ATTR_SUPPORTED_FEATURES`

```c
#define BT_SDP_ATTR_SUPPORTED_FEATURES 0x0311
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

基本图像配置文件支持的特性（BIP Supported Features）。

<a id="ga8a693e5265c7801e3c1125473c31445f"></a>

### `BT_SDP_ATTR_SUPPORTED_FEATURES_LIST`

```c
#define BT_SDP_ATTR_SUPPORTED_FEATURES_LIST 0x0200
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

支持的特性列表（Supported Features List）。

<a id="gac12ed37044c3f12c2d41b1fd23eacada"></a>

### `BT_SDP_ATTR_SUPPORTED_FORMATS_LIST`

```c
#define BT_SDP_ATTR_SUPPORTED_FORMATS_LIST 0x0303
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

支持的格式列表（Supported Formats List）。

<a id="gabc7cdfd247da5e2ecfd441c0436471f3"></a>

### `BT_SDP_ATTR_SUPPORTED_FUNCTIONS`

```c
#define BT_SDP_ATTR_SUPPORTED_FUNCTIONS 0x0312
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

基本图像配置文件支持的功能（BIP Supported Functions）。

<a id="ga41fc674e8571556397135734d28b829a"></a>

### `BT_SDP_ATTR_SUPPORTED_MESSAGE_TYPES`

```c
#define BT_SDP_ATTR_SUPPORTED_MESSAGE_TYPES 0x0316
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

支持的消息类型（Supported Message Types）。

<a id="gada3d989d6c8c0664ba0bf998414a0328"></a>

### `BT_SDP_ATTR_SUPPORTED_REPOSITORIES`

```c
#define BT_SDP_ATTR_SUPPORTED_REPOSITORIES 0x0314
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

支持的存储库（Supported Repositories）。

<a id="gab8fe8881b4470ab3522e710e36470ddb"></a>

### `BT_SDP_ATTR_SVCDB_STATE`

```c
#define BT_SDP_ATTR_SVCDB_STATE 0x0201
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

服务数据库状态（Service Database State）。

<a id="ga3e991ec1d5467c0b3ce5d9a7e750a300"></a>

### `BT_SDP_ATTR_SVCDESC_PRIMARY`

```c
#define BT_SDP_ATTR_SVCDESC_PRIMARY (0x0001 + BT_SDP_PRIMARY_LANG_BASE)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="ga7ef037ed6628aa7354736295e0e4ec77"></a>

### `BT_SDP_ATTR_SVCINFO_TTL`

```c
#define BT_SDP_ATTR_SVCINFO_TTL 0x0007
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

服务信息生存时间（Service Info Time to Live）。

<a id="gab5c5be56c54d3f8bd4ac6defff0b1e7c"></a>

### `BT_SDP_ATTR_SVCLASS_ID_LIST`

```c
#define BT_SDP_ATTR_SVCLASS_ID_LIST 0x0001
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

服务类别 ID 列表（Service Class ID List）。

<a id="ga76737502226c623bf508ae53a6015e08"></a>

### `BT_SDP_ATTR_SVCNAME_PRIMARY`

```c
#define BT_SDP_ATTR_SVCNAME_PRIMARY (0x0000 + BT_SDP_PRIMARY_LANG_BASE)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="gadbce181b739c201070d6abcbdc4139f4"></a>

### `BT_SDP_ATTR_TOTAL_IMAGING_DATA_CAPACITY`

```c
#define BT_SDP_ATTR_TOTAL_IMAGING_DATA_CAPACITY 0x0313
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

基本图像配置文件总图像数据容量（BIP Total Imaging Data Capacity）。

<a id="gab5c2534491b43cfc9d2c7e8807b29ff2"></a>

### `BT_SDP_ATTR_VENDOR_ID`

```c
#define BT_SDP_ATTR_VENDOR_ID 0x0201
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

厂商标识符（Vendor ID）。

<a id="gad0ac4a65c51ccdf4cd128eb8697e56ca"></a>

### `BT_SDP_ATTR_VENDOR_ID_SOURCE`

```c
#define BT_SDP_ATTR_VENDOR_ID_SOURCE 0x0205
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

厂商 ID 来源（Vendor ID Source）。

<a id="gae0f4af728f964ee1c11d86b785575a87"></a>

### `BT_SDP_ATTR_VERSION`

```c
#define BT_SDP_ATTR_VERSION 0x0203
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

版本（Version）。

<a id="gab698c476197acca0d499e39f7f246c66"></a>

### `BT_SDP_ATTR_VERSION_NUM_LIST`

```c
#define BT_SDP_ATTR_VERSION_NUM_LIST 0x0200
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

版本号列表（Version Number List）。

<a id="ga1ef964c955473601910ee3997b9ce5cd"></a>

### `BT_SDP_ATTR_WAP_GATEWAY`

```c
#define BT_SDP_ATTR_WAP_GATEWAY 0x0307
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

无线应用协议网关（WAP Gateway）。

<a id="gae1a3ff84a5588e55258c35ee57d6a5b5"></a>

### `BT_SDP_ATTR_WAP_STACK_TYPE`

```c
#define BT_SDP_ATTR_WAP_STACK_TYPE 0x0309
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

无线应用协议栈类型（WAP Stack Type）。

<a id="gaa0e334873b5477523572caa2359a4098"></a>

### `BT_SDP_AUDIO_SINK_SVCLASS`

```c
#define BT_SDP_AUDIO_SINK_SVCLASS 0x110b
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

音频接收端（Audio Sink）。

<a id="gafeb3a3184a0b83e0045187cbe3cf24dc"></a>

### `BT_SDP_AUDIO_SOURCE_SVCLASS`

```c
#define BT_SDP_AUDIO_SOURCE_SVCLASS 0x110a
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

音频源（Audio Source）。

<a id="gaaae997769dfc8325c38830707f4d22e3"></a>

### `BT_SDP_AV_REMOTE_CONTROLLER_SVCLASS`

```c
#define BT_SDP_AV_REMOTE_CONTROLLER_SVCLASS 0x110f
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

音视频远程控制控制器（A/V Remote Control Controller）。

<a id="gaea94250bed4c5e6ad47749a1237778f5"></a>

### `BT_SDP_AV_REMOTE_SVCLASS`

```c
#define BT_SDP_AV_REMOTE_SVCLASS 0x110e
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

音视频远程控制（A/V Remote Control）。

<a id="gafe96e9d32797a83c793f0ed278054b80"></a>

### `BT_SDP_AV_REMOTE_TARGET_SVCLASS`

```c
#define BT_SDP_AV_REMOTE_TARGET_SVCLASS 0x110c
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

音视频远程控制目标端（A/V Remote Control Target）。

<a id="gab7a8499dbb73a2700389d55d331bd23e"></a>

### `BT_SDP_AV_SVCLASS`

```c
#define BT_SDP_AV_SVCLASS 0x112c
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

音频／视频（Audio/Video）。

<a id="gac727f387a55a76c9a071cf62792f50e4"></a>

### `BT_SDP_BASIC_PRINTING_SVCLASS`

```c
#define BT_SDP_BASIC_PRINTING_SVCLASS 0x1122
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

基本打印（Basic Printing）。

<a id="gac48f198f6609fac95db69c09ac69efab"></a>

### `BT_SDP_BOOL`

```c
#define BT_SDP_BOOL 0x28
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

布尔值（Boolean）。

<a id="gabe05780702a9be7da54a8c04f79ad752"></a>

### `BT_SDP_BROWSE_GRP_DESC_SVCLASS`

```c
#define BT_SDP_BROWSE_GRP_DESC_SVCLASS 0x1001
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

浏览组描述符（Browse Group Descriptor）。

<a id="ga9617c02c6999d9fe987e91c6c2dc5dca"></a>

### `BT_SDP_CIP_SVCLASS`

```c
#define BT_SDP_CIP_SVCLASS 0x1128
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用 ISDN 访问（Common ISDN Access）。

<a id="ga16e1bc10528ac82f6cec822912f97d8c"></a>

### `BT_SDP_CORDLESS_TELEPHONY_SVCLASS`

```c
#define BT_SDP_CORDLESS_TELEPHONY_SVCLASS 0x1109
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

无绳电话（Cordless Telephony）。

<a id="gaa2954f3df4d0ee9684721cbc6182e37c"></a>

### `BT_SDP_DATA_ELEM_LIST`

```c
#define BT_SDP_DATA_ELEM_LIST ( ...)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
((struct bt_sdp_data_elem[]) {__VA_ARGS__})
```

声明数据元素列表（Data Element List）。

<a id="ga36f257de103356c3ebeb55e23186ed99"></a>

### `BT_SDP_DATA_NIL`

```c
#define BT_SDP_DATA_NIL 0x00
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

Nil，空类型（Nil, the null type）。

<a id="gaab655c1f93029ed64743156734e2519e"></a>

### `BT_SDP_DIALUP_NET_SVCLASS`

```c
#define BT_SDP_DIALUP_NET_SVCLASS 0x1103
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

拨号网络（Dialup Networking）。

<a id="ga30f6edbd67d96f7752a223409c8e4431"></a>

### `BT_SDP_DIRECT_PRINTING_SVCLASS`

```c
#define BT_SDP_DIRECT_PRINTING_SVCLASS 0x1118
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

直接打印（Direct Printing）。

<a id="ga79d34c3b7641cf523adf6515720ceceb"></a>

### `BT_SDP_DIRECT_PRT_REFOBJS_SVCLASS`

```c
#define BT_SDP_DIRECT_PRT_REFOBJS_SVCLASS 0x1120
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

直接打印引用对象服务（Direct Printing Reference Objects Service）。

<a id="ga31962fab5bed7c54311c4b291713a836"></a>

### `BT_SDP_FAX_SVCLASS`

```c
#define BT_SDP_FAX_SVCLASS 0x1111
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

传真（Fax）。

<a id="gae8010af5b12cd1c1b1633a4d2c9f5ab0"></a>

### `BT_SDP_GENERIC_ACCESS_SVCLASS`

```c
#define BT_SDP_GENERIC_ACCESS_SVCLASS 0x1800
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用访问配置文件（Generic Access Profile）。

<a id="gad3f345431526bb713921f4b51c48b056"></a>

### `BT_SDP_GENERIC_ATTRIB_SVCLASS`

```c
#define BT_SDP_GENERIC_ATTRIB_SVCLASS 0x1801
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用属性配置文件（Generic Attribute Profile）。

<a id="gaec7548467ffb686b22a907d05e38f275"></a>

### `BT_SDP_GENERIC_AUDIO_SVCLASS`

```c
#define BT_SDP_GENERIC_AUDIO_SVCLASS 0x1203
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用音频（Generic Audio）。

<a id="gaa8e5c423fca1fb0d06504cdc5be276d1"></a>

### `BT_SDP_GENERIC_FILETRANS_SVCLASS`

```c
#define BT_SDP_GENERIC_FILETRANS_SVCLASS 0x1202
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用文件传输（Generic File Transfer）。

<a id="ga1b9a169ff4db4fda939cba3ce21f808b"></a>

### `BT_SDP_GENERIC_NETWORKING_SVCLASS`

```c
#define BT_SDP_GENERIC_NETWORKING_SVCLASS 0x1201
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用联网（Generic Networking）。

<a id="ga010b005cfdb69c67cfc7e3c5c8426778"></a>

### `BT_SDP_GENERIC_TELEPHONY_SVCLASS`

```c
#define BT_SDP_GENERIC_TELEPHONY_SVCLASS 0x1204
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用电话（Generic Telephony）。

<a id="gaed2d6f72c344e2e9b9bdcefd23cb4086"></a>

### `BT_SDP_GN_SVCLASS`

```c
#define BT_SDP_GN_SVCLASS 0x1117
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

组网络（Group Network）。

<a id="gacdfb8ca6a776f57a2df38b4a6eaa8403"></a>

### `BT_SDP_GNSS_SERVER_SVCLASS`

```c
#define BT_SDP_GNSS_SERVER_SVCLASS 0x1136
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

全球导航卫星系统服务器（GNSS Server）。

<a id="ga300585062ed9ae05daca226cb3c5440d"></a>

### `BT_SDP_GNSS_SVCLASS`

```c
#define BT_SDP_GNSS_SVCLASS 0x1135
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

全球导航卫星系统（GNSS）

<a id="ga1c44ae236a292c91dc81539c9c89947c"></a>

### `BT_SDP_HANDSFREE_AGW_SVCLASS`

```c
#define BT_SDP_HANDSFREE_AGW_SVCLASS 0x111f
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

免提音频网关（Handsfree Audio Gateway）。

<a id="gab9f99989420545b3b0e71da6c5475f90"></a>

### `BT_SDP_HANDSFREE_SVCLASS`

```c
#define BT_SDP_HANDSFREE_SVCLASS 0x111e
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

免提（Handsfree）。

<a id="ga4ca1e6eb6fe385e526f8d84ed65ab285"></a>

### `BT_SDP_HCR_PRINT_SVCLASS`

```c
#define BT_SDP_HCR_PRINT_SVCLASS 0x1126
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

HCR 打印（HCR Print）。

<a id="ga621afe0f5a6d176c26e140c4162bee07"></a>

### `BT_SDP_HCR_SCAN_SVCLASS`

```c
#define BT_SDP_HCR_SCAN_SVCLASS 0x1127
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

HCR 扫描（HCR Scan）。

<a id="ga873f8e03aeb696d3eb287a8d00796a4f"></a>

### `BT_SDP_HCR_SVCLASS`

```c
#define BT_SDP_HCR_SVCLASS 0x1125
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

硬拷贝线缆替代（Hardcopy Cable Replacement）。

<a id="ga2125a92c6eb724a63d04188919a12bf1"></a>

### `BT_SDP_HDP_SINK_SVCLASS`

```c
#define BT_SDP_HDP_SINK_SVCLASS 0x1402
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

健康设备配置文件接收端（HDP Sink）。

<a id="ga87ba9fdf39fb99397a6dec4d92b6e3f1"></a>

### `BT_SDP_HDP_SOURCE_SVCLASS`

```c
#define BT_SDP_HDP_SOURCE_SVCLASS 0x1401
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

健康设备配置文件源端（HDP Source）。

<a id="gaf8fc80f3b2ff245b7d354aa0488bb42b"></a>

### `BT_SDP_HDP_SVCLASS`

```c
#define BT_SDP_HDP_SVCLASS 0x1400
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

健康设备配置文件（HDP）。

<a id="ga4c9322cf28a8b1aa96828152e8ee7379"></a>

### `BT_SDP_HEADSET_AGW_SVCLASS`

```c
#define BT_SDP_HEADSET_AGW_SVCLASS 0x1112
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

耳机音频网关（Headset AG）。

<a id="ga6eb16aacf468b460fa7675ffc4703e68"></a>

### `BT_SDP_HEADSET_SVCLASS`

```c
#define BT_SDP_HEADSET_SVCLASS 0x1108
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

带麦克风耳机（Headset）。

<a id="gab63eab5791898a47bd540eed4d55cddc"></a>

### `BT_SDP_HID_SVCLASS`

```c
#define BT_SDP_HID_SVCLASS 0x1124
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备服务（Human Interface Device Service）。

<a id="ga3f04a28d9764a0c7755babe379c25393"></a>

### `BT_SDP_IMAGING_ARCHIVE_SVCLASS`

```c
#define BT_SDP_IMAGING_ARCHIVE_SVCLASS 0x111c
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

图像自动归档（Imaging Automatic Archive）。

<a id="ga51a4cfc28f86a650b03a7bbe6e5b883a"></a>

### `BT_SDP_IMAGING_REFOBJS_SVCLASS`

```c
#define BT_SDP_IMAGING_REFOBJS_SVCLASS 0x111d
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

图像引用对象（Imaging Referenced Objects）。

<a id="gaf19cd136b780ef303c1290b26ab2ca17"></a>

### `BT_SDP_IMAGING_RESPONDER_SVCLASS`

```c
#define BT_SDP_IMAGING_RESPONDER_SVCLASS 0x111b
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

图像响应端（Imaging Responder）。

<a id="ga08730b1fd7088101fadb85e5dc13fd24"></a>

### `BT_SDP_IMAGING_SVCLASS`

```c
#define BT_SDP_IMAGING_SVCLASS 0x111a
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

基本图像配置文件（Basic Imaging Profile）。

<a id="gaf754bbfd9cdc0e6a2bf7d6c46fab3f29"></a>

### `BT_SDP_INT128`

```c
#define BT_SDP_INT128 0x14
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

有符号 128 位整数（Signed 128-bit integer）。

<a id="gaf6a3795d22cff4a522a2225339fb5a57"></a>

### `BT_SDP_INT16`

```c
#define BT_SDP_INT16 0x11
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

有符号 16 位整数（Signed 16-bit integer）。

<a id="ga0ad987ebeac3dab3ef2196f4dfeca1ab"></a>

### `BT_SDP_INT32`

```c
#define BT_SDP_INT32 0x12
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

有符号 32 位整数（Signed 32-bit integer）。

<a id="gaae793fef5690c6013e6e0e34ededb75f"></a>

### `BT_SDP_INT64`

```c
#define BT_SDP_INT64 0x13
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

有符号 64 位整数（Signed 64-bit integer）。

<a id="gaeed1818ca1bf762b23ab2bfcd18b8a66"></a>

### `BT_SDP_INT8`

```c
#define BT_SDP_INT8 0x10
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

有符号 8 位整数（Signed 8-bit integer）。

<a id="ga9681e34d78cea87e413fa4be40e4239a"></a>

### `BT_SDP_INTERCOM_SVCLASS`

```c
#define BT_SDP_INTERCOM_SVCLASS 0x1110
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

对讲（Intercom）。

<a id="ga39d4ce2465b10c10ee746c1491c49bea"></a>

### `BT_SDP_IRMC_SYNC_CMD_SVCLASS`

```c
#define BT_SDP_IRMC_SYNC_CMD_SVCLASS 0x1107
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

IrMC 同步命令（IrMC Sync Command）。

<a id="ga28fc78fc21e4d88569e5ca5727ed6202"></a>

### `BT_SDP_IRMC_SYNC_SVCLASS`

```c
#define BT_SDP_IRMC_SYNC_SVCLASS 0x1104
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

IrMC 同步（IrMC Sync）。

<a id="gaf0199837105ded0d65314e573da6a3ed"></a>

### `BT_SDP_LAN_ACCESS_SVCLASS`

```c
#define BT_SDP_LAN_ACCESS_SVCLASS 0x1102
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

使用 PPP 的局域网访问（LAN Access Using PPP）。

<a id="ga25b31454ee5b5fe23b617b5256ba00c4"></a>

### `BT_SDP_LIST`

```c
#define BT_SDP_LIST ( _att_id, _type_size, _data_elem_seq )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
{ \
        _att_id, { _type_size, _data_elem_seq } \
}
```

通用 SDP 列表属性声明宏（List Attribute Declaration Macro）。

用于声明列表属性（List Attribute）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_att_id` | 列表属性标识符（List Attribute ID）。 |
| `_data_elem_seq` | 列表的数据元素序列（Data Element Sequence）。 |
| `_type_size` | SDP 类型和大小描述符（Type and Size Descriptor）。 |

<a id="ga47849c599678f7ec48c237b8b36e9cb7"></a>

### `BT_SDP_MAP_MCE_SVCLASS`

```c
#define BT_SDP_MAP_MCE_SVCLASS 0x1133
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

消息通知服务器（Message Notification Server）。

<a id="ga58f5cc54014e3723720e7c3b7ba82fd8"></a>

### `BT_SDP_MAP_MSE_SVCLASS`

```c
#define BT_SDP_MAP_MSE_SVCLASS 0x1132
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

消息访问服务器（Message Access Server）。

<a id="gaec665050af4cc3affcef3912bb212fc0"></a>

### `BT_SDP_MAP_SVCLASS`

```c
#define BT_SDP_MAP_SVCLASS 0x1134
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

消息访问配置文件（Message Access Profile）。

<a id="ga9cce7e3a576329661b363b102cefa494"></a>

### `BT_SDP_MPS_SC_SVCLASS`

```c
#define BT_SDP_MPS_SC_SVCLASS 0x113a
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

MPS SC 服务标识（MPS SC）。

<a id="gaf847b2675482d3bb9674f569c3604e40"></a>

### `BT_SDP_MPS_SVCLASS`

```c
#define BT_SDP_MPS_SVCLASS 0x113b
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

多配置文件规范（MPS）。

<a id="ga78a7be1db8be8d7eece0d17c629dd009"></a>

### `BT_SDP_NAP_SVCLASS`

```c
#define BT_SDP_NAP_SVCLASS 0x1116
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

网络接入点（Network Access Point）。

<a id="gaee13722587e4eb8c4beaaa0abad88fe5"></a>

### `BT_SDP_NEW_SERVICE`

```c
#define BT_SDP_NEW_SERVICE
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
{ \
        BT_SDP_ATTR_RECORD_HANDLE, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UINT32), BT_SDP_ARRAY_32(0) } \
}, \
{ \
        BT_SDP_ATTR_RECORD_STATE, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UINT32), BT_SDP_ARRAY_32(0) } \
}, \
{ \
        BT_SDP_ATTR_LANG_BASE_ATTR_ID_LIST, \
        { BT_SDP_TYPE_SIZE_VAR(BT_SDP_SEQ8, 9), \
          BT_SDP_DATA_ELEM_LIST( \
                { BT_SDP_TYPE_SIZE(BT_SDP_UINT16), BT_SDP_ARRAY_8('n', 'e') }, \
                { BT_SDP_TYPE_SIZE(BT_SDP_UINT16), BT_SDP_ARRAY_16(106) }, \
                { BT_SDP_TYPE_SIZE(BT_SDP_UINT16), \
                        BT_SDP_ARRAY_16(BT_SDP_PRIMARY_LANG_BASE) } \
          ), \
        } \
}, \
{ \
        BT_SDP_ATTR_BROWSE_GRP_LIST, \
        { BT_SDP_TYPE_SIZE_VAR(BT_SDP_SEQ8, 3), \
          BT_SDP_DATA_ELEM_LIST( \
                { BT_SDP_TYPE_SIZE(BT_SDP_UUID16), \
                        BT_SDP_ARRAY_16(BT_SDP_PUBLIC_BROWSE_GROUP) }, \
          ), \
        } \
}
```

SDP 新服务记录声明宏（New Service Record Declaration Macro）。

用于声明新服务记录（Service Record）的辅助宏。默认属性包括记录句柄（Record Handle）、记录状态（Record State）、语言基址（Language Base）和根浏览组（Root Browse Group）。

<a id="gacd25278a573edcb16aa4b60f8ffad20d"></a>

### `BT_SDP_OBEX_FILETRANS_SVCLASS`

```c
#define BT_SDP_OBEX_FILETRANS_SVCLASS 0x1106
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

OBEX 文件传输（OBEX File Transfer）。

<a id="gaaf64788e0cc6d54a8511c07af22f6740"></a>

### `BT_SDP_OBEX_OBJPUSH_SVCLASS`

```c
#define BT_SDP_OBEX_OBJPUSH_SVCLASS 0x1105
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

OBEX 对象推送（OBEX Object Push）。

<a id="gaa9abb444e3b43c1164d6b450b1c066e5"></a>

### `BT_SDP_PANU_SVCLASS`

```c
#define BT_SDP_PANU_SVCLASS 0x1115
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

个人区域网络用户（Personal Area Networking User）。

<a id="gaec2475b7ba36b860c0f8a9cfc33df4a8"></a>

### `BT_SDP_PBAP_PCE_SVCLASS`

```c
#define BT_SDP_PBAP_PCE_SVCLASS 0x112e
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

电话簿访问客户端（Phonebook Access Client）。

<a id="ga612bb83e9f08edd163433a5fbe9528fc"></a>

### `BT_SDP_PBAP_PSE_SVCLASS`

```c
#define BT_SDP_PBAP_PSE_SVCLASS 0x112f
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

电话簿访问服务器（Phonebook Access Server）。

<a id="ga60a9fad26300c15e988e101f90c06435"></a>

### `BT_SDP_PBAP_SVCLASS`

```c
#define BT_SDP_PBAP_SVCLASS 0x1130
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

电话簿访问（Phonebook Access）。

<a id="gaed5403661e0eb8f798a950bead59369a"></a>

### `BT_SDP_PNP_INFO_SVCLASS`

```c
#define BT_SDP_PNP_INFO_SVCLASS 0x1200
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

即插即用信息（PnP Information）。

<a id="gab502c9288e5f01dfdaaf8390bb3f6e49"></a>

### `BT_SDP_PRIMARY_LANG_BASE`

```c
#define BT_SDP_PRIMARY_LANG_BASE 0x0100
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="ga9298ac73a26a1ab2e53733f404e5c6ea"></a>

### `BT_SDP_PRINTING_STATUS_SVCLASS`

```c
#define BT_SDP_PRINTING_STATUS_SVCLASS 0x1123
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

打印状态（Printing Status）。

<a id="ga772d50f5ea6dbf93bb648e84b8b2ea25"></a>

### `BT_SDP_PROTO_ATT`

```c
#define BT_SDP_PROTO_ATT 0x0007
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

属性协议（Attribute Protocol）。

<a id="ga4fabbc2e0b5d83cc84c7db7b1a3640b7"></a>

### `BT_SDP_PROTO_AVCTP`

```c
#define BT_SDP_PROTO_AVCTP 0x0017
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

音视频控制传输协议（Audio/Video Control Transport Protocol）。

<a id="gaa308561679578a5e1d013301b7792eb6"></a>

### `BT_SDP_PROTO_AVDTP`

```c
#define BT_SDP_PROTO_AVDTP 0x0019
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

音视频分发传输协议（Audio/Video Distribution Transport Protocol）。

<a id="ga29032e4ab9a24056a6088ac377444285"></a>

### `BT_SDP_PROTO_BNEP`

```c
#define BT_SDP_PROTO_BNEP 0x000f
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

蓝牙网络封装协议（Bluetooth Network Encapsulation Protocol）。

<a id="ga127e2b367475cc074268ad88eb648c63"></a>

### `BT_SDP_PROTO_CMTP`

```c
#define BT_SDP_PROTO_CMTP 0x001b
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用 ISDN 访问协议（Common ISDN Access Protocol）。

<a id="ga51c5e425f9fc9c785b75c03d2517a2c3"></a>

### `BT_SDP_PROTO_FTP`

```c
#define BT_SDP_PROTO_FTP 0x000a
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

文件传输协议（File Transfer Protocol）。

<a id="ga9f1bdf155d4f0be01172f971bac67154"></a>

### `BT_SDP_PROTO_HARDCOPY_CTRL`

```c
#define BT_SDP_PROTO_HARDCOPY_CTRL 0x0012
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

硬拷贝控制通道（Hardcopy Control Channel）。

<a id="ga5095801fa0d28056017725860dc75a93"></a>

### `BT_SDP_PROTO_HARDCOPY_DATA`

```c
#define BT_SDP_PROTO_HARDCOPY_DATA 0x0014
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

硬拷贝数据通道（Hardcopy Data Channel）。

<a id="gaf17681a3af315b0edaa9c82dd3a7fb89"></a>

### `BT_SDP_PROTO_HARDCOPY_NTF`

```c
#define BT_SDP_PROTO_HARDCOPY_NTF 0x0016
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

硬拷贝通知通道（Hardcopy Notification Channel）。

<a id="gacb8a22ed2d0045e66d9208b408a6228b"></a>

### `BT_SDP_PROTO_HID`

```c
#define BT_SDP_PROTO_HID 0x0011
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

人机接口设备协议（Human Interface Device Protocol）。

<a id="ga103e4968d26d94d56a56a6e4d02b7a9a"></a>

### `BT_SDP_PROTO_HTTP`

```c
#define BT_SDP_PROTO_HTTP 0x000c
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

超文本传输协议（HyperText Transfer Protocol）。

<a id="gab6db981f154c92d17a51b7144f1afebe"></a>

### `BT_SDP_PROTO_IP`

```c
#define BT_SDP_PROTO_IP 0x0009
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

互联网协议（Internet Protocol）。

<a id="gac055f0beba2c311e9f098217fc721a75"></a>

### `BT_SDP_PROTO_L2CAP`

```c
#define BT_SDP_PROTO_L2CAP 0x0100
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol）。

<a id="ga6c6e5cbaea972e982ea608705d2a06cc"></a>

### `BT_SDP_PROTO_MCAP_CTRL`

```c
#define BT_SDP_PROTO_MCAP_CTRL 0x001e
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

多通道适配协议控制通道（Multi-Channel Adaptation Protocol Control）。

<a id="ga19c4608fe6f63fb553706b176ee56a9b"></a>

### `BT_SDP_PROTO_MCAP_DATA`

```c
#define BT_SDP_PROTO_MCAP_DATA 0x001f
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

多通道适配协议数据通道（Multi-Channel Adaptation Protocol Data）。

<a id="gab16c910f700b7341742f4d7eedc9d32e"></a>

### `BT_SDP_PROTO_OBEX`

```c
#define BT_SDP_PROTO_OBEX 0x0008
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

对象交换协议（Object Exchange Protocol）。

<a id="ga17056b75f2596fe115d18e42e7f3285e"></a>

### `BT_SDP_PROTO_RFCOMM`

```c
#define BT_SDP_PROTO_RFCOMM 0x0003
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

射频通信（Radio Frequency Communication）。

<a id="gaa5ae0cf1cd2933005ae70709bea76407"></a>

### `BT_SDP_PROTO_SDP`

```c
#define BT_SDP_PROTO_SDP 0x0001
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

服务发现协议（Service Discovery Protocol）。

<a id="ga7934d7ed5ec1d7a78f9ea17e2c354af9"></a>

### `BT_SDP_PROTO_TCP`

```c
#define BT_SDP_PROTO_TCP 0x0004
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

传输控制协议（Transmission Control Protocol）。

<a id="ga426cddacc8f6a9e8c502d001d48ecc2f"></a>

### `BT_SDP_PROTO_TCS_AT`

```c
#define BT_SDP_PROTO_TCS_AT 0x0006
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

电话控制规范 AT 协议（Telephony Control Specification AT）。

<a id="ga75468f9c406f9940f4d2b0d2d56a9762"></a>

### `BT_SDP_PROTO_TCS_BIN`

```c
#define BT_SDP_PROTO_TCS_BIN 0x0005
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

电话控制规范二进制协议（Telephony Control Specification Binary）。

<a id="gace719188083da9941dcfa76176cdc98c"></a>

### `BT_SDP_PROTO_UDP`

```c
#define BT_SDP_PROTO_UDP 0x0002
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

用户数据报协议（User Datagram Protocol）。

<a id="ga368af07bb117929235af5c0e7b9729f0"></a>

### `BT_SDP_PROTO_UPNP`

```c
#define BT_SDP_PROTO_UPNP 0x0010
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用即插即用（Universal Plug and Play）。

<a id="ga40525df1204b9e7a3106994eb8b7046e"></a>

### `BT_SDP_PROTO_WSP`

```c
#define BT_SDP_PROTO_WSP 0x000e
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

无线会话协议（Wireless Session Protocol）。

<a id="ga383233a0ff3159ed653786490a4c06ae"></a>

### `BT_SDP_PUBLIC_BROWSE_GROUP`

```c
#define BT_SDP_PUBLIC_BROWSE_GROUP 0x1002
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

公共浏览组（Public Browse Group）。

<a id="ga555f10b8f3ae3710c6dda9f37e78547b"></a>

### `BT_SDP_RECORD`

```c
#define BT_SDP_RECORD ( _attrs)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
{ \
        .attrs = _attrs, \
        .attr_count = ARRAY_SIZE((_attrs)), \
}
```

SDP 服务声明宏（Service Declaration Macro）。

用于声明服务（Service）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_attrs` | 服务记录的属性列表（List of Attributes）。 |

<a id="ga6bc247854656613d2fa9b47d55bd69d6"></a>

### `BT_SDP_REFERENCE_PRINTING_SVCLASS`

```c
#define BT_SDP_REFERENCE_PRINTING_SVCLASS 0x1119
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

引用打印（Reference Printing）。

<a id="ga78607a42f5228b37d348614b12e48a77"></a>

### `BT_SDP_REFLECTED_UI_SVCLASS`

```c
#define BT_SDP_REFLECTED_UI_SVCLASS 0x1121
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

映射用户界面（Reflected UI）。

<a id="gad2234f8e0bce0e6b55d18c7a7c950e1d"></a>

### `BT_SDP_SAP_SVCLASS`

```c
#define BT_SDP_SAP_SVCLASS 0x112d
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

SIM 卡访问（SIM Access）。

<a id="gac2c2379f8e483939826297dc49657837"></a>

### `BT_SDP_SDP_SERVER_SVCLASS`

```c
#define BT_SDP_SDP_SERVER_SVCLASS 0x1000
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

服务发现服务器（Service Discovery Server）。

<a id="gadf5b15a0296a872ffefc24bbc90dc45b"></a>

### `BT_SDP_SEQ16`

```c
#define BT_SDP_SEQ16 0x36
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

数据元素序列，长度字段为 16 位（Data element sequence, 16-bit length）。

<a id="ga639e86b5103168917cb7202100e3124d"></a>

### `BT_SDP_SEQ32`

```c
#define BT_SDP_SEQ32 0x37
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

数据元素序列，长度字段为 32 位（Data element sequence, 32-bit length）。

<a id="ga5a64e3bec70b40114a3160dbfb1e484b"></a>

### `BT_SDP_SEQ8`

```c
#define BT_SDP_SEQ8 0x35
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

数据元素序列，长度字段为 8 位（Data element sequence, 8-bit length）。

<a id="gaa884191d772bfa24484cb33c0f614334"></a>

### `BT_SDP_SEQ_UNSPEC`

```c
#define BT_SDP_SEQ_UNSPEC 0x30
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

数据元素序列，未指定大小（Data element sequence, unspecified size）。

<a id="gab1234d808a7e347328bf95ad065fd9c4"></a>

### `BT_SDP_SERIAL_PORT_SVCLASS`

```c
#define BT_SDP_SERIAL_PORT_SVCLASS 0x1101
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

串行端口（Serial Port）。

<a id="ga610e7cab0a598f272eeb2838f4c4c996"></a>

### `BT_SDP_SERVER_RECORD_HANDLE`

```c
#define BT_SDP_SERVER_RECORD_HANDLE 0x0000
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="gaa57f3c9a52ae29c02d7577be99f91e7c"></a>

### `BT_SDP_SERVICE_ID`

```c
#define BT_SDP_SERVICE_ID ( _uuid)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
{ \
        BT_SDP_ATTR_SERVICE_ID, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UUID16), &((struct bt_uuid_16) _uuid) } \
}
```

SDP 服务 ID 属性声明宏（Service ID Attribute Declaration Macro）。

用于声明服务标识符属性（Service ID Attribute）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_uuid` | 服务标识符（Service ID），采用 16 位 UUID。 |

<a id="ga83de8e62415d3e31b3b5434b9db633d0"></a>

### `BT_SDP_SERVICE_NAME`

```c
#define BT_SDP_SERVICE_NAME ( _name)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
{ \
        BT_SDP_ATTR_SVCNAME_PRIMARY, \
        { BT_SDP_TYPE_SIZE_VAR(BT_SDP_TEXT_STR8, (sizeof(_name)-1)), _name } \
}
```

SDP 名称属性声明宏（Name Attribute Declaration Macro）。

用于声明服务名称属性（Service Name Attribute）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 以字符串表示的服务名称（Service Name），最多 256 个字符。 |

<a id="ga2d1040ccd11d1dd4c697525ebc323243"></a>

### `BT_SDP_SIZE_DESC_MASK`

```c
#define BT_SDP_SIZE_DESC_MASK 0x07
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="ga6e8f843aeb2d325058214d2a1454737a"></a>

### `BT_SDP_SIZE_INDEX_OFFSET`

```c
#define BT_SDP_SIZE_INDEX_OFFSET 5
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="ga3a1feb6311af64292c1f22ff54e01876"></a>

### `BT_SDP_SUPPORTED_CAPABILITIES`

```c
#define BT_SDP_SUPPORTED_CAPABILITIES ( _capabilities)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
{ \
        BT_SDP_ATTR_SUPPORTED_CAPABILITIES, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UINT8), BT_SDP_ARRAY_8(_capabilities) } \
}
```

SDP 支持能力属性声明宏（Supported Capabilities Attribute Declaration Macro）。

用于声明配置文件／协议所支持能力（Supported Capabilities）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_capabilities` | 能力掩码（Capability Mask），采用 8 位无符号整数。 |

<a id="ga096c84414b429aa05bed45cf6175361e"></a>

### `BT_SDP_SUPPORTED_FEATURES`

```c
#define BT_SDP_SUPPORTED_FEATURES ( _features)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
{ \
        BT_SDP_ATTR_SUPPORTED_FEATURES, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UINT16), BT_SDP_ARRAY_16(_features) } \
}
```

SDP 支持特性属性声明宏（Supported Features Attribute Declaration Macro）。

用于声明配置文件／协议所支持特性（Supported Features）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_features` | 特性掩码（Feature Mask），采用 16 位无符号整数。 |

<a id="ga48eadaa621be7eaecbf5d2f8cc1354ab"></a>

### `BT_SDP_SUPPORTED_FUNCTIONS`

```c
#define BT_SDP_SUPPORTED_FUNCTIONS ( _functions)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
{ \
        BT_SDP_ATTR_SUPPORTED_FUNCTIONS, \
        { BT_SDP_TYPE_SIZE(BT_SDP_UINT32), BT_SDP_ARRAY_32(_functions) } \
}
```

SDP 支持功能属性声明宏（Supported Functions Attribute Declaration Macro）。

用于声明配置文件／协议所支持功能（Supported Functions）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_functions` | 功能掩码（Function Mask），采用 32 位无符号整数。 |

<a id="gaa5301cdac5fc9299837f29b92aa3c10b"></a>

### `BT_SDP_TEXT_STR16`

```c
#define BT_SDP_TEXT_STR16 0x26
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

文本字符串，长度字段为 16 位（Text string, 16-bit length）。

<a id="ga29657a21117a3fbe05942778a8d7637e"></a>

### `BT_SDP_TEXT_STR32`

```c
#define BT_SDP_TEXT_STR32 0x27
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

文本字符串，长度字段为 32 位（Text string, 32-bit length）。

<a id="ga885ace6b1def91f3fa4dd16cb391d2b8"></a>

### `BT_SDP_TEXT_STR8`

```c
#define BT_SDP_TEXT_STR8 0x25
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

文本字符串，长度字段为 8 位（Text string, 8-bit length）。

<a id="gaca9942a42701cda835a5bf7b7aaf1d75"></a>

### `BT_SDP_TEXT_STR_UNSPEC`

```c
#define BT_SDP_TEXT_STR_UNSPEC 0x20
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

文本字符串，未指定大小（Text string, unspecified size）。

<a id="ga3eb2a5501341f6c5186a27219cf27cdf"></a>

### `BT_SDP_TYPE_DESC_MASK`

```c
#define BT_SDP_TYPE_DESC_MASK 0xf8
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="ga66778ac38fb5b82d3b514fe0da008393"></a>

### `BT_SDP_TYPE_SIZE`

```c
#define BT_SDP_TYPE_SIZE ( _type)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
.type = _type, \
.data_size = BIT(_type & BT_SDP_SIZE_DESC_MASK), \
.total_size = BIT(_type & BT_SDP_SIZE_DESC_MASK) + 1
```

声明固定大小的数据元素头（Fixed-size Data Element Header）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_type` | 数据元素头（Data Element Header），包含类型和大小描述符。 |

<a id="gabbb2bd6a8321513082851fe73dfa44bc"></a>

### `BT_SDP_TYPE_SIZE_VAR`

```c
#define BT_SDP_TYPE_SIZE_VAR ( _type, _size )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

展开值（Value）：

```c
.type = _type, \
.data_size = _size, \
.total_size = BIT((_type & BT_SDP_SIZE_DESC_MASK) - \
                  BT_SDP_SIZE_INDEX_OFFSET) + _size + 1
```

声明可变大小的数据元素头（Variable-size Data Element Header）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_type` | 数据元素头（Data Element Header），包含类型和大小描述符。 |
| `_size` | 数据的实际大小（Actual Size）。 |

<a id="ga629179357eff2cd60621f0e1e435df06"></a>

### `BT_SDP_UDI_MT_SVCLASS`

```c
#define BT_SDP_UDI_MT_SVCLASS 0x112a
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

UDI MT 服务（UDI MT）。

<a id="ga846599abf75f1cbb27028aea8a619f31"></a>

### `BT_SDP_UDI_TA_SVCLASS`

```c
#define BT_SDP_UDI_TA_SVCLASS 0x112b
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

UDI TA 服务（UDI TA）。

<a id="ga9a815c6efe976f29e9f6f35a566245fd"></a>

### `BT_SDP_UINT128`

```c
#define BT_SDP_UINT128 0x0c
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

无符号 128 位整数（Unsigned 128-bit integer）。

<a id="ga1129f3a1364f29c9ce36f6f74ca21327"></a>

### `BT_SDP_UINT16`

```c
#define BT_SDP_UINT16 0x09
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

无符号 16 位整数（Unsigned 16-bit integer）。

<a id="ga4f3bcb36dfce975c2d9ab68894a9e49c"></a>

### `BT_SDP_UINT32`

```c
#define BT_SDP_UINT32 0x0a
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

无符号 32 位整数（Unsigned 32-bit integer）。

<a id="ga11261bf1c63a6d463ed41225c1e1a0c7"></a>

### `BT_SDP_UINT64`

```c
#define BT_SDP_UINT64 0x0b
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

无符号 64 位整数（Unsigned 64-bit integer）。

<a id="ga546a46c2aa7eb3306eb46768fb8737a4"></a>

### `BT_SDP_UINT8`

```c
#define BT_SDP_UINT8 0x08
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

无符号 8 位整数（Unsigned 8-bit integer）。

<a id="ga102b24708429877c4f37a5008fb176b1"></a>

### `BT_SDP_UPNP_IP_SVCLASS`

```c
#define BT_SDP_UPNP_IP_SVCLASS 0x1206
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

UPnP IP 服务（UPnP IP Service）。

<a id="gad4d97c0b664c48bdc0842f92240409c7"></a>

### `BT_SDP_UPNP_L2CAP_SVCLASS`

```c
#define BT_SDP_UPNP_L2CAP_SVCLASS 0x1302
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

UPnP IP L2CAP（UPnP IP L2CAP）。

<a id="gad418094573383e6252719abed97d24dd"></a>

### `BT_SDP_UPNP_LAP_SVCLASS`

```c
#define BT_SDP_UPNP_LAP_SVCLASS 0x1301
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

UPnP IP 局域网访问配置文件（UPnP IP LAP）。

<a id="ga3f50947a742b24089f86193e773d623b"></a>

### `BT_SDP_UPNP_PAN_SVCLASS`

```c
#define BT_SDP_UPNP_PAN_SVCLASS 0x1300
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

UPnP IP 个人区域网络（UPnP IP PAN）。

<a id="ga9e7fa3bcf139462a2c33f90b526e1ad1"></a>

### `BT_SDP_UPNP_SVCLASS`

```c
#define BT_SDP_UPNP_SVCLASS 0x1205
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用即插即用服务（UPnP Service）。

<a id="gac1acc712468e5af1f54022ac3551882a"></a>

### `BT_SDP_URL_STR16`

```c
#define BT_SDP_URL_STR16 0x46
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

URL 字符串，长度字段为 16 位（URL string, 16-bit length）。

<a id="ga37476681e9d4eee53b710c44e2da9a2f"></a>

### `BT_SDP_URL_STR32`

```c
#define BT_SDP_URL_STR32 0x47
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

URL 字符串，长度字段为 32 位（URL string, 32-bit length）。

<a id="gafb2a77d6097c8c4cf9f01b7e16df26f1"></a>

### `BT_SDP_URL_STR8`

```c
#define BT_SDP_URL_STR8 0x45
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

URL 字符串，长度字段为 8 位（URL string, 8-bit length）。

<a id="ga32a7a79422f52b75c2eb2d2eb467dc00"></a>

### `BT_SDP_URL_STR_UNSPEC`

```c
#define BT_SDP_URL_STR_UNSPEC 0x40
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

URL 字符串，未指定大小（URL string, unspecified size）。

<a id="gaadf48ba3e96687fff99ff58789d79a50"></a>

### `BT_SDP_UUID128`

```c
#define BT_SDP_UUID128 0x1c
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用唯一标识符，128 位（UUID, 128-bit）。

<a id="ga45598f1c663acd3a3e5a409696cb3d2f"></a>

### `BT_SDP_UUID16`

```c
#define BT_SDP_UUID16 0x19
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用唯一标识符，16 位（UUID, 16-bit）。

<a id="ga78245bb059feb3ec039e05aba24746e7"></a>

### `BT_SDP_UUID32`

```c
#define BT_SDP_UUID32 0x1a
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用唯一标识符，32 位（UUID, 32-bit）。

<a id="ga4f829572cca9669a8a96a857874bb022"></a>

### `BT_SDP_UUID_UNSPEC`

```c
#define BT_SDP_UUID_UNSPEC 0x18
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

通用唯一标识符，未指定大小（UUID, unspecified size）。

<a id="ga3e087c095a78f07efae660eceae9c11e"></a>

### `BT_SDP_VIDEO_CONF_GW_SVCLASS`

```c
#define BT_SDP_VIDEO_CONF_GW_SVCLASS 0x1129
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

视频会议网关（Video Conferencing Gateway）。

<a id="ga4e2ef8310c9396f9fb7781ab4732f308"></a>

### `BT_SDP_VIDEO_DISTRIBUTION_SVCLASS`

```c
#define BT_SDP_VIDEO_DISTRIBUTION_SVCLASS 0x1305
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

视频分发（Video Distribution）。

<a id="ga1e3428b6d0197bd7c9d72154c025e9f5"></a>

### `BT_SDP_VIDEO_SINK_SVCLASS`

```c
#define BT_SDP_VIDEO_SINK_SVCLASS 0x1304
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

视频接收端（Video Sink）。

<a id="ga17d7fb3a77ef7266ea2d760fb3696a83"></a>

### `BT_SDP_VIDEO_SOURCE_SVCLASS`

```c
#define BT_SDP_VIDEO_SOURCE_SVCLASS 0x1303
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

视频源（Video Source）。

<a id="ga22624d29917aaeaa0c281d9517178821"></a>

### `BT_SDP_WAP_CLIENT_SVCLASS`

```c
#define BT_SDP_WAP_CLIENT_SVCLASS 0x1114
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

无线应用协议客户端（WAP Client）。

<a id="ga2ab79d7ff4e88820773cf24f0b0b6e20"></a>

### `BT_SDP_WAP_SVCLASS`

```c
#define BT_SDP_WAP_SVCLASS 0x1113
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

无线应用协议（WAP）。

<a id="gad672a89277b276d1b702fe07302c468e"></a>

### `bt_sdp_discover_func_t`

```c
typedef uint8_t(* bt_sdp_discover_func_t) (struct bt_conn *conn, struct bt_sdp_client_result *result, const struct bt_sdp_discover_params *params)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

回调类型，用于通知用户：已在远端解析出给定 UUID 的结果，用户可使用结果记录缓冲区（Result Record Buffer）进一步检查。

用户向 `bt_sdp_discover_params` 对象提供此类型的函数。每次完成给定 UUID 的有效记录发现（Record Discovery）时，都会调用它。如果 UUID 解析未返回任何记录，则向用户传入 `NULL`。否则，用户可以获取有效记录；内部的“下一条记录”（Next Record）提示设为 `false` 时，表示 UUID 解析已完成；调用方也可以将此提示设为 `true`，表示该 UUID 还有下一条记录。函数返回值允许用户控制是否继续获取已解析的后续记录。如果当前记录已经满足需求，用户不想继续读取该 UUID 的更多已解析记录，应返回 `BT_SDP_DISCOVER_UUID_STOP`。否则，返回值表示允许继续迭代子调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object），标识与被查询远端的连接。 |
| `result` | 指向逻辑上未解析的 SDP 记录的对象；该记录依据给定发现参数（Discovery Parameters）驱动的响应收集而成。 |
| `params` | 发现参数（Discover Parameters）。 |

**返回（Returns）**：返回值（Returns）：若无需继续读取下一条记录并继续该 UUID 的发现过程，则返回 `BT_SDP_DISCOVER_UUID_STOP`；返回 `BT_SDP_DISCOVER_UUID_CONTINUE` 则允许继续发现。

<a id="ga278df12ff5def68ca4663defd178582c"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

用作 `bt_sdp_discover_func_t` 返回值的辅助枚举（Helper Enum）。

此值通知调用者继续执行后续待处理操作（Pending Actions），或者停止这些操作。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_SDP_DISCOVER_UUID_STOP` |  |
| `BT_SDP_DISCOVER_UUID_CONTINUE` |  |

<a id="ga88019838cb3e5317fce93f4933583d94"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

SDP 发现类型（Discover Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_SDP_DISCOVER_SERVICE_SEARCH` | 发现类型：服务搜索（Service Search）。 |
| `BT_SDP_DISCOVER_SERVICE_ATTR` | 发现类型：服务属性（Service Attribute）。 |
| `BT_SDP_DISCOVER_SERVICE_SEARCH_ATTR` | 发现类型：服务搜索属性（Service Search Attribute）。 |

<a id="ga5e4a45b7b860d82a111480c9f25c2666"></a>

### `bt_sdp_attr_value_type`

```c
enum bt_sdp_attr_value_type
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

SDP 属性值类型枚举（Attribute Value Type Enumeration）。

定义可从 SDP 属性中解析的不同属性值类型（Attribute Value Types）的枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_SDP_ATTR_VALUE_TYPE_NONE` | 无值（No Value）。 |
| `BT_SDP_ATTR_VALUE_TYPE_UINT` | 无符号整数（Unsigned Integer）。 |
| `BT_SDP_ATTR_VALUE_TYPE_SINT` | 有符号整数（Signed Integer）。 |
| `BT_SDP_ATTR_VALUE_TYPE_BOOL` | 布尔值（Boolean）。 |
| `BT_SDP_ATTR_VALUE_TYPE_TEXT` | 文本字符串。 |
| `BT_SDP_ATTR_VALUE_TYPE_URL` | URL 字符串（URL String）。 |

<a id="gaa104046a9e6e15f05961bf8652ecec16"></a>

### `bt_sdp_attr_addl_proto_count()`

```c
ssize_t bt_sdp_attr_addl_proto_count ( const struct bt_sdp_attribute * attr)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

获取附加协议描述符列表（Additional Protocol Descriptor List）中的协议描述符数量。

此函数返回附加协议描述符列表属性（Additional Protocol Descriptor List Attribute）中包含的协议描述符数量。可据此确定服务有多少个可用的备选协议栈（Alternative Protocol Stacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `attr` | 指向包含附加协议描述符列表（Additional Protocol Descriptor List）的 SDP 属性的指针。 |

**返回（Returns）**：返回值（Returns）：成功时返回找到的协议描述符数量；解析出错时返回负值。

<a id="gac395eff18a4d2af3d955e276bf13963a"></a>

### `bt_sdp_attr_addl_proto_parse()`

```c
int bt_sdp_attr_addl_proto_parse ( const struct bt_sdp_attribute * attr, bool(* func )(const struct bt_sdp_attribute *attr, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

解析附加协议描述符列表属性（Additional Protocol Descriptor List Attribute）。

此函数解析附加协议描述符列表属性（Additional Protocol Descriptor List Attribute），并对属性中找到的每个协议描述符调用所提供的回调函数。该列表包含可用于访问服务的备选协议栈（Alternative Protocol Stacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `attr` | 指向包含附加协议描述符列表（Additional Protocol Descriptor List）的 SDP 属性的指针。 |
| `func` | 对每个协议描述符调用的回调函数（Callback Function）。回调接收协议描述符属性的指针和用户提供的数据。返回 `true` 继续解析，返回 `false` 停止。 |
| `user_data` | 可选的用户上下文数据（Context Data），传递给回调函数。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；解析出错时为负值。

<a id="gacf20a00d84e6eed2c128284fe9c52024"></a>

### `bt_sdp_attr_addl_proto_read()`

```c
int bt_sdp_attr_addl_proto_read ( const struct bt_sdp_attribute * attr, uint16_t index, const struct bt_uuid * uuid, struct bt_sdp_attr_value * value )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

读取附加协议描述符列表（Additional Protocol Descriptor List）中指定索引和 UUID 对应的值。

此函数在附加协议描述符列表属性（Additional Protocol Descriptor List Attribute）中给定索引的协议描述符内搜索指定协议 UUID，并提取其关联参数值。索引参数指定要搜索哪个协议描述符，即哪个备选协议栈（Alternative Protocol Stack）；UUID 则标识该描述符内的具体协议。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` attr` | 指向包含附加协议描述符列表（Additional Protocol Descriptor List）的 SDP 属性的指针。 |
| ` index` | 协议描述符（备选协议栈）的从零开始索引（Zero-based Index）。第一个描述符使用 `0`，第二个使用 `1`，依此类推。 |
| ` uuid` | 指向协议 UUID 标识符的指针，用于在指定协议描述符内搜索该协议。 |
| `[out] value` | 指向 `bt_sdp_attr_value` 结构的指针，用于保存提取出的参数值（Parameter Value）。 |

**返回（Returns）**：返回值（Returns）：成功找到协议及其参数并提取后为 `0`；若协议描述符索引无效、指定描述符中未找到 UUID，或解析出错，则为负值。

<a id="ga07ca5d4f383d74004478cfd6ead2b80a"></a>

### `bt_sdp_attr_has_uuid()`

```c
bool bt_sdp_attr_has_uuid ( const struct bt_sdp_attribute * attr, const struct bt_uuid * uuid )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

检查 SDP 属性是否包含指定 UUID。

此函数检查指定 SDP 属性是否包含给定 UUID。可据此确认属性是否引用了某个特定服务或协议 UUID。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `attr` | 指向待检查的 SDP 属性（Attribute）的指针。 |
| `uuid` | 指向要在该属性中搜索的 UUID 的指针。 |

**返回（Returns）**：返回值（Returns）：属性包含指定 UUID 时为 `true`，否则为 `false`。

<a id="ga3bad45ab578c0277a320ac241692f799"></a>

### `bt_sdp_attr_read()`

```c
int bt_sdp_attr_read ( const struct bt_sdp_attribute * attr, const struct bt_uuid * uuid, struct bt_sdp_attr_value * value )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

读取指定 UUID 对应的 SDP 属性值（Attribute Value）。

此函数从给定 SDP 属性中读取并提取与指定 UUID 关联的属性值（Attribute Value）。解析后的值保存在所提供的 `bt_sdp_attr_value` 结构中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` attr` | 指向要读取的 SDP 属性（Attribute）的指针。 |
| ` uuid` | 指向待读取值对应的 UUID 标识符的指针。 |
| `[out] value` | 指向 `bt_sdp_attr_value` 结构的指针，用于保存提取出的属性值（Attribute Value）。 |

**返回（Returns）**：返回值（Returns）：成功找到并提取值时为 `0`；未找到 UUID 或发生错误时为负值。

<a id="gab7d3e8bc83efff28cf9118710b5486fc"></a>

### `bt_sdp_attr_value_parse()`

```c
int bt_sdp_attr_value_parse ( const struct bt_sdp_attribute * attr, bool(* func )(const struct bt_sdp_attr_value_pair *value, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

解析 SDP 属性值（Attribute Values）。

解析 SDP 属性，对其中找到的每个已解析值调用所提供的回调函数（Callback Function）。此函数可处理包含多个值的复杂属性结构。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `attr` | 指向待解析的 SDP 属性（Attribute）的指针。 |
| `func` | 对每个已解析值调用的回调函数（Callback Function）。回调接收包含已解析值的 `bt_sdp_attr_value_pair` 结构及用户数据。返回 `true` 继续解析，返回 `false` 停止。 |
| `user_data` | 可选的用户上下文数据（Context Data），传递给回调。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；解析出错时为负值。

<a id="ga44658df825a40f820a31e7adb4240d25"></a>

### `bt_sdp_discover()`

```c
int bt_sdp_discover ( struct bt_conn * conn, struct bt_sdp_discover_params * params )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

允许用户启动 SDP 发现会话（Discovery Session）。

此函数按照用户提供的发现参数，在远端服务器上执行 SDP 服务发现（Service Discovery）。如果对端之间没有正在进行的 SDP 事务（Transaction），立即启动发现会话；如果存在事务，则将本次请求排队，等前一次发现完成后处理。服务发现完成时会调用回调函数，将发现结果反馈给用户。

对于服务搜索（Service Search）和服务搜索属性（Service Search Attribute）这两种发现类型，如果使用 128 位 UUID，UUID 数据应表示为小端字节序序列（Little-endian Byte Order Sequence）。

服务搜索（Service Search）：SDP 客户端生成 `SDP_SERVICE_SEARCH_REQ`，定位与服务搜索模式 `params->uuid` 匹配的服务记录；该模式作为 PDU 的第一个参数。服务属性（Service Attribute）：SDP 客户端生成 `SDP_SERVICE_ATTR_REQ`，从指定服务记录 `params->handle` 中获取指定属性值；属性标识符列表（AttributeIDList）由 `params->ids` 指定。服务搜索属性（Service Search Attribute）：SDP 客户端生成 `SDP_SERVICE_SEARCH_ATTR_REQ`，获取与服务搜索模式 `params->uuid` 匹配的指定属性值；该模式作为 PDU 的第一个参数，属性标识符列表由 `params->ids` 指定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 标识与远端连接的对象（Connection Object）。 |
| `params` | SDP 发现参数（Discovery Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求 `params` 已进入待处理请求队列（Request Pending Queue）。SDP 发现结果将通过 `params->func`（`bt_sdp_discover_params::func`）通知。如果参数 `result->resp_buf`（`bt_sdp_client_result::resp_buf`）为 `NULL`，则发现失败或未发现任何 SDP 记录。 |
| `-ENOTCONN` | 连接 `conn` 无效或尚未建立（Not Established）。 |
| `-EINVAL` | 请求 `params` 无效，或属性标识符列表（Attribute ID List）无法装入一个请求 PDU。 |

<a id="ga2eb0646597a44e0e3cb0234d2c12a2d7"></a>

### `bt_sdp_discover_cancel()`

```c
int bt_sdp_discover_cancel ( struct bt_conn * conn, struct bt_sdp_discover_params * params )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

释放等待中的 SDP 发现请求（Discovery Request）。

取消由 SDP 发现参数对象标识的等待中 SDP 客户端请求，即已经通过 `bt_sdp_discover()` 排队、但尚未开始解析的请求。成功后，不会再为该请求调用发现回调（Discovery Callback），并且可以立即复用参数对象。

正在解析的请求无法取消；此时返回 `-EINPROGRESS`，回调（Callback）仍然会被调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 标识与远端连接的对象（Connection Object）。 |
| `params` | SDP 发现参数（Discovery Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求已取消（Canceled）。 |
| `-EINVAL` | `conn` 或 `params` 为 `NULL`。 |
| `-EINPROGRESS` | 请求已经处于解析过程中（Being Resolved）。 |
| `-ESRCH` | 没有此类等待中的请求（Waiting Request）。 |

<a id="gaba31a2327e4bba56ef2ac831b166e66a"></a>

### `bt_sdp_get_addl_proto_param()`

```c
int bt_sdp_get_addl_proto_param ( const struct net_buf * buf, uint16_t proto, uint8_t index, uint16_t * param )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

获取与给定协议栈层协议 UUID（Stacked Protocol UUID）相关的附加参数值。

此 API 从附加协议描述符列表属性（Additional Protocol Descriptor List Attribute）中提取与给定协议 UUID 关联的指定参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` buf` | 缓冲区中的原始记录数据（Raw Record Data）。 |
| ` proto` | 要检查的已知协议（Protocol），例如 RFCOMM 或 L2CAP。 |
| ` index` | 协议描述符（备选协议栈）的从零开始索引（Zero-based Index）。第一个描述符使用 `0`，第二个使用 `1`，依此类推。 |
| `[out] param` | 成功时填入找到的参数值（Parameter Value）。 |

**返回（Returns）**：返回值（Returns）：成功找到与给定协议值关联的指定参数时为 `0`；处理出错时为负值。

<a id="ga9df34b18af051782377229a18e6d3887"></a>

### `bt_sdp_get_attr()`

```c
int bt_sdp_get_attr ( const struct net_buf * buf, uint16_t attr_id, struct bt_sdp_attribute * attr )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

按 ID 从 SDP 记录获取指定属性（Attribute）。

此函数通过搜索给定属性标识符（Attribute Identifier），从 SDP 记录数据中获取指定属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` buf` | 包含已发现的 SDP 记录数据的缓冲区（Buffer），这些数据将被解析。 |
| ` attr_id` | 要搜索的指定属性标识符（Attribute Identifier）。 |
| `[out] attr` | 指向 `bt_sdp_attribute` 结构的指针，用于保存找到的属性（Attribute）。 |

**返回（Returns）**：返回值（Returns）：成功找到并填入属性时为 `0`；未找到属性或出错时为负值。

<a id="gae1c3110dfe24a939cc02d998c4699ca7"></a>

### `bt_sdp_get_features()`

```c
int bt_sdp_get_features ( const struct net_buf * buf, uint16_t * features )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

获取支持特性（SupportedFeatures）属性值。

如果远端公开了支持特性属性（SupportedFeature），允许获取该属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 保存来自远端的原始记录数据（Raw Record Data）的缓冲区。 |
| `features` | 成功时填入支持特性掩码（SupportedFeature Mask）的对象。 |

**返回（Returns）**：返回值（Returns）：找到有效特性时成功返回 `0`；出现任何错误时返回负值。

<a id="ga71809908bb73150258b2a5ab3c2f8517"></a>

### `bt_sdp_get_product_id()`

```c
int bt_sdp_get_product_id ( const struct net_buf * buf, uint16_t * product_id )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

获取产品 ID（Product ID）。

用于提取远端产品标识符（Product ID）的辅助 API。为获取该值，需要选择恰当的通用配置文件参数（Generic Profile Parameter）；通常在对应配置文件规范的 SDP 互操作要求（SDP Interoperability Requirements）一节中列出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 保存来自远端的原始记录数据（Raw Record Data）的缓冲区。 |
| `product_id` | 成功时填入找到的产品标识符（Product ID）掩码。译注：原文写作“Product ID. mask.”，此处保留其用词。 |

**返回（Returns）**：返回值（Returns）：找到有效 `product_id` 时成功返回 `0`；出现任何错误时返回负值。

<a id="ga9e7d4bd0a407fe8254410f907db90f00"></a>

### `bt_sdp_get_profile_version()`

```c
int bt_sdp_get_profile_version ( const struct net_buf * buf, uint16_t profile, uint16_t * version )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

获取配置文件版本（Profile Version）。

用于提取远端配置文件版本号（Profile Version Number）的辅助 API。为获取该值，需要选择恰当的通用配置文件参数（Generic Profile Parameter）；通常在对应配置文件规范的 SDP 互操作要求（SDP Interoperability Requirements）一节中列出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 缓冲区中的原始记录数据（Raw Record Data）。 |
| `profile` | 该配置文件所属的配置文件族标识符（Profile Family Identifier）。 |
| `version` | 成功时填入找到的版本号（Version Number）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；处理出错时为负值。

<a id="gaf69723cff6dce7e86f0f0240ec3e2041"></a>

### `bt_sdp_get_proto_param()`

```c
int bt_sdp_get_proto_param ( const struct net_buf * buf, uint16_t proto, uint16_t * param )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

向用户提供与给定协议栈层协议 UUID（Stacked Protocol UUID）相关的参数值。

此 API 从协议描述符列表属性（Protocol Descriptor List Attribute）中提取与给定协议 UUID 关联的指定参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 缓冲区中的原始记录数据（Raw Record Data）。 |
| `proto` | 要检查的已知协议（Protocol），例如 RFCOMM 或 L2CAP。 |
| `param` | 成功时填入找到的参数值（Parameter Value）。 |

**返回（Returns）**：返回值（Returns）：成功找到与给定协议值关联的指定参数时为 `0`；处理出错时为负值。

<a id="gaed089d52f57cb25d2b02b2adbc60a36a"></a>

### `bt_sdp_get_vendor_id()`

```c
int bt_sdp_get_vendor_id ( const struct net_buf * buf, uint16_t * vendor_id )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

获取厂商 ID（Vendor ID）。

用于提取远端厂商标识符（Vendor ID）的辅助 API。为获取该值，需要选择恰当的通用配置文件参数（Generic Profile Parameter）；通常在对应配置文件规范的 SDP 互操作要求（SDP Interoperability Requirements）一节中列出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 保存来自远端的原始记录数据（Raw Record Data）的缓冲区。 |
| `vendor_id` | 成功时填入找到的厂商标识符（Vendor ID）。 |

**返回（Returns）**：返回值（Returns）：找到有效 `vendor_id` 时成功返回 `0`；出现任何错误时返回负值。

<a id="ga2cb42ca8e487071682c37124ab56f2ab"></a>

### `bt_sdp_has_attr()`

```c
bool bt_sdp_has_attr ( const struct net_buf * buf, uint16_t attr_id )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

检查是否找到指定属性标识符（Attribute Identifier）。

此 API 检查是否找到了指定属性标识符（Attribute Identifier）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 包含已发现的 SDP 记录数据的缓冲区（Buffer），这些数据将被解析。 |
| `attr_id` | 指定属性标识符（Attribute Identifier）。 |

**返回（Returns）**：返回值（Returns）：找到属性标识符时为 `true`，否则为 `false`。

<a id="ga0ce1314e052881eec5a43f571857960e"></a>

### `bt_sdp_record_parse()`

```c
int bt_sdp_record_parse ( const struct net_buf * buf, bool(* func )(const struct bt_sdp_attribute *attr, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

遍历发现的 SDP 记录（Record）。

用于遍历已发现 SDP 记录的辅助 API。它解析所提供缓冲区内指定的 SDP 原始记录数据（Raw Record Data），对找到的每个属性调用指定回调函数。遍历持续到全部属性处理完毕，或回调返回 `false` 以停止遍历。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 保存从远端发现的原始 SDP 记录数据（Raw SDP Record Data）的缓冲区。 |
| `func` | 对每个属性调用的回调函数（Callback Function）。回调接收当前属性的指针和用户提供的数据。返回 `true` 继续遍历，返回 `false` 停止。 |
| `user_data` | 可选的用户上下文数据（Context Data），传递给回调函数。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；解析或遍历期间出错时为负值。

<a id="ga6006e3cd593ef793273fb291913790fa"></a>

### `bt_sdp_register_service()`

```c
int bt_sdp_register_service ( struct bt_sdp_record * service)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

注册服务记录（Service Record）。

注册服务记录（Service Record）。应用可以使用 `BT_SDP_DECLARE_SERVICE`、`BT_SDP_LIST`、`BT_SDP_SERVICE_ID`、`BT_SDP_SERVICE_NAME` 等宏。服务声明必须以 `BT_SDP_NEW_SERVICE` 开始。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `service` | 使用 `BT_SDP_DECLARE_SERVICE` 声明的服务记录（Service Record）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga71e7d75850becf4ead62668c8e7bebbc"></a>

### `bt_sdp_unregister_service()`

```c
int bt_sdp_unregister_service ( struct bt_sdp_record * service)
```

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

注销服务记录（Service Record）。

从 SDP 数据库移除此前已注册的服务记录（Service Record）。此函数检查活动的 SDP L2CAP 通道；只要存在此类通道，就返回 `-EBUSY`。检查与实际移除之间仍存在竞态窗口（Race Window）；调用方负责确保本次调用期间不会建立新的 SDP 连接，例如提前断开 BR/EDR 链路，或禁用可连接模式（Connectable Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `service` | 要注销的服务记录（Service Record）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `service` 为 `NULL`。 |
| `-EBUSY` | 当前存在活动的 SDP L2CAP 通道（Active Channel）。 |
| `-ENOENT` | `service` 当前未注册（Not Registered）。 |


## 3.11\_原页交叉引用（Cross References）

- [bt_sdp_data_elem](../bluetooth_service_model_reference/P169_bt_sdp_data_elem_结构体.md)
- [bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)
- [bt_sdp_record](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md)
- [bt_sdp_client_result](../bluetooth_service_model_reference/P168_bt_sdp_client_result_结构体.md)
- [bt_sdp_attribute_id_range](../bluetooth_service_model_reference/P167_bt_sdp_attribute_id_range_结构体.md)
- [bt_sdp_attribute_id_list](../bluetooth_service_model_reference/P166_bt_sdp_attribute_id_list_结构体.md)
- [bt_sdp_discover_params](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md)
- [bt_sdp_attr_value_uint](../bluetooth_service_model_reference/P163_bt_sdp_attr_value_uint_结构体.md)
- [bt_sdp_attr_value_int](../bluetooth_service_model_reference/P160_bt_sdp_attr_value_int_结构体.md)
- [bt_sdp_attr_value_text](../bluetooth_service_model_reference/P162_bt_sdp_attr_value_text_结构体.md)
- [bt_sdp_attr_value_url](../bluetooth_service_model_reference/P164_bt_sdp_attr_value_url_结构体.md)
- [bt_sdp_attr_value](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md)
- [bt_sdp_attr_value_pair](../bluetooth_service_model_reference/P161_bt_sdp_attr_value_pair_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [zephyr/bluetooth/classic/sdp.h](../api_file_input_wake_protocol_reference/P005_zephyr__bluetooth__classic__sdp.h_文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [bt_uuid_16](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [bt_sdp_discover_params::func](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md#a650143f0733958cf1186543c3469facc)
- [bt_sdp_client_result::resp_buf](../bluetooth_service_model_reference/P168_bt_sdp_client_result_结构体.md#aa223dc666cbeaaebea462362188c531d)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="agroup__bt__sdp_html_gaef264fa3621c3df7a164128bb95b30fc"></a>
<a id="agroup__bt__uuid_html_gac3973b66e992cbc0940752b77b378f43"></a>
<a id="agroup__bt__sdp_html_gadbdfa913e11ed7b8e691a1fc1712e6eb"></a>
<a id="astructbt__sdp__data__elem_html"></a>
<a id="agroup__bt__sdp_html_ga1129f3a1364f29c9ce36f6f74ca21327"></a>
<a id="agroup__bt__sdp_html_ga2609212bf5400c31351bc3ec5f60a7e1"></a>
<a id="agroup__bt__sdp_html_ga383233a0ff3159ed653786490a4c06ae"></a>
<a id="agroup__bt__sdp_html_ga38f32cae462272b51eb4edca0c5c95a2"></a>
<a id="agroup__bt__sdp_html_ga45598f1c663acd3a3e5a409696cb3d2f"></a>
<a id="agroup__bt__sdp_html_ga462ec997a81c6b439a24e2de085676ab"></a>
<a id="agroup__bt__sdp_html_ga4d458591f8eba26feaab1220c49f6a29"></a>
<a id="agroup__bt__sdp_html_ga4f3bcb36dfce975c2d9ab68894a9e49c"></a>
<a id="agroup__bt__sdp_html_ga5a64e3bec70b40114a3160dbfb1e484b"></a>
<a id="agroup__bt__sdp_html_ga66778ac38fb5b82d3b514fe0da008393"></a>
<a id="agroup__bt__sdp_html_ga7a17ee4872190a087cf2e5ea4db9e737"></a>
<a id="agroup__bt__sdp_html_gaa4bb67164ae1f16b26081668d00f45c7"></a>
<a id="agroup__bt__sdp_html_gab502c9288e5f01dfdaaf8390bb3f6e49"></a>
<a id="agroup__bt__sdp_html_gabbb2bd6a8321513082851fe73dfa44bc"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="agroup__bt__sdp_html_gad2149fd761f7ae2ea6ef761ab2545ab4"></a>
<a id="astructbt__uuid__16_html"></a>
<a id="agroup__bt__sdp_html_ga76737502226c623bf508ae53a6015e08"></a>
<a id="agroup__bt__sdp_html_ga885ace6b1def91f3fa4dd16cb391d2b8"></a>
<a id="agroup__bt__sdp_html_ga5347dbc038ac9c259d17c14ed9a812d3"></a>
<a id="agroup__bt__sdp_html_ga546a46c2aa7eb3306eb46768fb8737a4"></a>
<a id="agroup__bt__sdp_html_ga498d9beaa7877570fe834d854de36fcb"></a>
<a id="agroup__bt__sdp_html_gabc7cdfd247da5e2ecfd441c0436471f3"></a>
<a id="agroup__bt__sdp_html_ga2d1040ccd11d1dd4c697525ebc323243"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__bt__sdp_html_ga6e8f843aeb2d325058214d2a1454737a"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga278df12ff5def68ca4663defd178582ca990fbea48866b2acb7ccd67391b19636"></a>
<a id="gga278df12ff5def68ca4663defd178582ca94e15ea86b69d65ca9c1947d1e2157ef"></a>
<a id="gga88019838cb3e5317fce93f4933583d94a9ce8c93cf1754fc7047951e891f66ff2"></a>
<a id="gga88019838cb3e5317fce93f4933583d94a5b8c3260e5aaaa08e86a099ccfeee41f"></a>
<a id="gga88019838cb3e5317fce93f4933583d94a64fff103816cfc0215b9b3909786fa4e"></a>
<a id="gga5e4a45b7b860d82a111480c9f25c2666acaf932b38a1e17ca9e85c055096fa1da"></a>
<a id="gga5e4a45b7b860d82a111480c9f25c2666a5af87613192cda6a05fa280d2df8574b"></a>
<a id="gga5e4a45b7b860d82a111480c9f25c2666a5917deef84a7af5d5f908d4058732b1e"></a>
<a id="gga5e4a45b7b860d82a111480c9f25c2666a154bbb29fb26d007838c87def4cd34f8"></a>
<a id="gga5e4a45b7b860d82a111480c9f25c2666a80b8652e39dae70c61443adf4f29fb4d"></a>
<a id="gga5e4a45b7b860d82a111480c9f25c2666a27eccef21d812956c6ae7ff9194e20e4"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_基本成像配置文件（Basic Imaging Profile，BIP）.md) · [返回大纲](大纲.md) · [下一章](P004_输入事件定义（Input Event Definitions）.md)
