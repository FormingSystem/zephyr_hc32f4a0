---
id: learning.zephyr-docs.api-file-input-wake-protocol-reference.page-5
title: zephyr__bluetooth__classic__sdp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_bluetooth\_\_classic\_\_sdp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务发现协议（Service Discovery Protocol）的处理。

<a id="details"></a>

```c
#include <sys/types.h>
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/bluetooth/conn.h>
```

查看此文件的源码。

服务发现协议处理（Service Discovery Protocol Handling）。服务发现协议（SDP）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

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

## 5.2\_宏定义（Macros）

<a id="r_ga610e7cab0a598f272eeb2838f4c4c996"></a>

```c
#define BT_SDP_SERVER_RECORD_HANDLE 0x0000
```

相关声明：[BT_SDP_SERVER_RECORD_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga610e7cab0a598f272eeb2838f4c4c996)。

<a id="r_gab502c9288e5f01dfdaaf8390bb3f6e49"></a>

```c
#define BT_SDP_PRIMARY_LANG_BASE 0x0100
```

相关声明：[BT_SDP_PRIMARY_LANG_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab502c9288e5f01dfdaaf8390bb3f6e49)。

<a id="r_ga76737502226c623bf508ae53a6015e08"></a>

```c
#define BT_SDP_ATTR_SVCNAME_PRIMARY (0x0000 + BT_SDP_PRIMARY_LANG_BASE)
```

相关声明：[BT_SDP_ATTR_SVCNAME_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga76737502226c623bf508ae53a6015e08)、[BT_SDP_PRIMARY_LANG_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab502c9288e5f01dfdaaf8390bb3f6e49)。

<a id="r_ga3e991ec1d5467c0b3ce5d9a7e750a300"></a>

```c
#define BT_SDP_ATTR_SVCDESC_PRIMARY (0x0001 + BT_SDP_PRIMARY_LANG_BASE)
```

相关声明：[BT_SDP_ATTR_SVCDESC_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3e991ec1d5467c0b3ce5d9a7e750a300)、[BT_SDP_PRIMARY_LANG_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab502c9288e5f01dfdaaf8390bb3f6e49)。

<a id="r_gab8b0110be857d6eca206e00c3b5e373a"></a>

```c
#define BT_SDP_ATTR_PROVNAME_PRIMARY (0x0002 + BT_SDP_PRIMARY_LANG_BASE)
```

相关声明：[BT_SDP_ATTR_PROVNAME_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab8b0110be857d6eca206e00c3b5e373a)、[BT_SDP_PRIMARY_LANG_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab502c9288e5f01dfdaaf8390bb3f6e49)。

<a id="r_ga3eb2a5501341f6c5186a27219cf27cdf"></a>

```c
#define BT_SDP_TYPE_DESC_MASK 0xf8
```

相关声明：[BT_SDP_TYPE_DESC_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3eb2a5501341f6c5186a27219cf27cdf)。

<a id="r_ga2d1040ccd11d1dd4c697525ebc323243"></a>

```c
#define BT_SDP_SIZE_DESC_MASK 0x07
```

相关声明：[BT_SDP_SIZE_DESC_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2d1040ccd11d1dd4c697525ebc323243)。

<a id="r_ga6e8f843aeb2d325058214d2a1454737a"></a>

```c
#define BT_SDP_SIZE_INDEX_OFFSET 5
```

相关声明：[BT_SDP_SIZE_INDEX_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga6e8f843aeb2d325058214d2a1454737a)。

<a id="r_gaef264fa3621c3df7a164128bb95b30fc"></a>

```c
#define BT_SDP_ARRAY_8(...)
```

相关声明：[BT_SDP_ARRAY_8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaef264fa3621c3df7a164128bb95b30fc)。

在属性（Attribute）中声明由 8 位元素组成的数组。

<a id="r_gaa4bb67164ae1f16b26081668d00f45c7"></a>

```c
#define BT_SDP_ARRAY_16(...)
```

相关声明：[BT_SDP_ARRAY_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa4bb67164ae1f16b26081668d00f45c7)。

在属性（Attribute）中声明由 16 位元素组成的数组。

<a id="r_ga7a17ee4872190a087cf2e5ea4db9e737"></a>

```c
#define BT_SDP_ARRAY_32(...)
```

相关声明：[BT_SDP_ARRAY_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga7a17ee4872190a087cf2e5ea4db9e737)。

在属性（Attribute）中声明由 32 位元素组成的数组。

<a id="r_gadbdfa913e11ed7b8e691a1fc1712e6eb"></a>

```c
#define BT_SDP_ARRAY_UUID_128(w32, w1, w2, w3, w48)
```

相关声明：[BT_SDP_ARRAY_UUID_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gadbdfa913e11ed7b8e691a1fc1712e6eb)。

在属性中声明采用小端字节序（Little-endian）的 128 位 UUID。

<a id="r_ga66778ac38fb5b82d3b514fe0da008393"></a>

```c
#define BT_SDP_TYPE_SIZE(_type)
```

相关声明：[BT_SDP_TYPE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga66778ac38fb5b82d3b514fe0da008393)。

声明固定大小的数据元素头（Fixed-size Data Element Header）。

<a id="r_gabbb2bd6a8321513082851fe73dfa44bc"></a>

```c
#define BT_SDP_TYPE_SIZE_VAR(_type, _size)
```

相关声明：[BT_SDP_TYPE_SIZE_VAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gabbb2bd6a8321513082851fe73dfa44bc)。

声明可变大小的数据元素头（Variable-size Data Element Header）。

<a id="r_gaa2954f3df4d0ee9684721cbc6182e37c"></a>

```c
#define BT_SDP_DATA_ELEM_LIST(...)
```

相关声明：[BT_SDP_DATA_ELEM_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa2954f3df4d0ee9684721cbc6182e37c)。

声明数据元素列表（Data Element List）。

<a id="r_gaee13722587e4eb8c4beaaa0abad88fe5"></a>

```c
#define BT_SDP_NEW_SERVICE
```

相关声明：[BT_SDP_NEW_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaee13722587e4eb8c4beaaa0abad88fe5)。

SDP 新服务记录声明宏（New Service Record Declaration Macro）。

<a id="r_ga25b31454ee5b5fe23b617b5256ba00c4"></a>

```c
#define BT_SDP_LIST(_att_id, _type_size, _data_elem_seq)
```

相关声明：[BT_SDP_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga25b31454ee5b5fe23b617b5256ba00c4)。

通用 SDP 列表属性声明宏（List Attribute Declaration Macro）。

<a id="r_gaa57f3c9a52ae29c02d7577be99f91e7c"></a>

```c
#define BT_SDP_SERVICE_ID(_uuid)
```

相关声明：[BT_SDP_SERVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa57f3c9a52ae29c02d7577be99f91e7c)。

SDP 服务 ID 属性声明宏（Service ID Attribute Declaration Macro）。

<a id="r_ga83de8e62415d3e31b3b5434b9db633d0"></a>

```c
#define BT_SDP_SERVICE_NAME(_name)
```

相关声明：[BT_SDP_SERVICE_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga83de8e62415d3e31b3b5434b9db633d0)。

SDP 名称属性声明宏（Name Attribute Declaration Macro）。

<a id="r_ga096c84414b429aa05bed45cf6175361e"></a>

```c
#define BT_SDP_SUPPORTED_FEATURES(_features)
```

相关声明：[BT_SDP_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga096c84414b429aa05bed45cf6175361e)。

SDP 支持特性属性声明宏（Supported Features Attribute Declaration Macro）。

<a id="r_ga3a1feb6311af64292c1f22ff54e01876"></a>

```c
#define BT_SDP_SUPPORTED_CAPABILITIES(_capabilities)
```

相关声明：[BT_SDP_SUPPORTED_CAPABILITIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3a1feb6311af64292c1f22ff54e01876)。

SDP 支持能力属性声明宏（Supported Capabilities Attribute Declaration Macro）。

<a id="r_ga48eadaa621be7eaecbf5d2f8cc1354ab"></a>

```c
#define BT_SDP_SUPPORTED_FUNCTIONS(_functions)
```

相关声明：[BT_SDP_SUPPORTED_FUNCTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga48eadaa621be7eaecbf5d2f8cc1354ab)。

SDP 支持功能属性声明宏（Supported Functions Attribute Declaration Macro）。

<a id="r_ga555f10b8f3ae3710c6dda9f37e78547b"></a>

```c
#define BT_SDP_RECORD(_attrs)
```

相关声明：[BT_SDP_RECORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga555f10b8f3ae3710c6dda9f37e78547b)。

SDP 服务声明宏（Service Declaration Macro）。

<a id="r_ga920e61b784c4ae47bc51ac5c46273220"></a>

```c
#define BT_SDP_ATTR_ID_RANGE(beginning, ending)
```

相关声明：[BT_SDP_ATTR_ID_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga920e61b784c4ae47bc51ac5c46273220)。

初始化 SDP 属性 ID 范围（Attribute ID Range）。

<a id="define-members-0"></a>

### 标准服务与服务组的服务类标识符（Service class identifiers of standard services and service groups）

<a id="r_gac2c2379f8e483939826297dc49657837"></a>

```c
#define BT_SDP_SDP_SERVER_SVCLASS 0x1000
```

相关声明：[BT_SDP_SDP_SERVER_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac2c2379f8e483939826297dc49657837)。

服务发现服务器（Service Discovery Server）。

<a id="r_gabe05780702a9be7da54a8c04f79ad752"></a>

```c
#define BT_SDP_BROWSE_GRP_DESC_SVCLASS 0x1001
```

相关声明：[BT_SDP_BROWSE_GRP_DESC_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gabe05780702a9be7da54a8c04f79ad752)。

浏览组描述符（Browse Group Descriptor）。

<a id="r_ga383233a0ff3159ed653786490a4c06ae"></a>

```c
#define BT_SDP_PUBLIC_BROWSE_GROUP 0x1002
```

相关声明：[BT_SDP_PUBLIC_BROWSE_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga383233a0ff3159ed653786490a4c06ae)。

公共浏览组（Public Browse Group）。

<a id="r_gab1234d808a7e347328bf95ad065fd9c4"></a>

```c
#define BT_SDP_SERIAL_PORT_SVCLASS 0x1101
```

相关声明：[BT_SDP_SERIAL_PORT_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab1234d808a7e347328bf95ad065fd9c4)。

串行端口（Serial Port）。

<a id="r_gaf0199837105ded0d65314e573da6a3ed"></a>

```c
#define BT_SDP_LAN_ACCESS_SVCLASS 0x1102
```

相关声明：[BT_SDP_LAN_ACCESS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf0199837105ded0d65314e573da6a3ed)。

使用 PPP 的局域网访问（LAN Access Using PPP）。

<a id="r_gaab655c1f93029ed64743156734e2519e"></a>

```c
#define BT_SDP_DIALUP_NET_SVCLASS 0x1103
```

相关声明：[BT_SDP_DIALUP_NET_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaab655c1f93029ed64743156734e2519e)。

拨号网络（Dialup Networking）。

<a id="r_ga28fc78fc21e4d88569e5ca5727ed6202"></a>

```c
#define BT_SDP_IRMC_SYNC_SVCLASS 0x1104
```

相关声明：[BT_SDP_IRMC_SYNC_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga28fc78fc21e4d88569e5ca5727ed6202)。

IrMC 同步（IrMC Sync）。

<a id="r_gaaf64788e0cc6d54a8511c07af22f6740"></a>

```c
#define BT_SDP_OBEX_OBJPUSH_SVCLASS 0x1105
```

相关声明：[BT_SDP_OBEX_OBJPUSH_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaaf64788e0cc6d54a8511c07af22f6740)。

OBEX 对象推送（OBEX Object Push）。

<a id="r_gacd25278a573edcb16aa4b60f8ffad20d"></a>

```c
#define BT_SDP_OBEX_FILETRANS_SVCLASS 0x1106
```

相关声明：[BT_SDP_OBEX_FILETRANS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gacd25278a573edcb16aa4b60f8ffad20d)。

OBEX 文件传输（OBEX File Transfer）。

<a id="r_ga39d4ce2465b10c10ee746c1491c49bea"></a>

```c
#define BT_SDP_IRMC_SYNC_CMD_SVCLASS 0x1107
```

相关声明：[BT_SDP_IRMC_SYNC_CMD_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga39d4ce2465b10c10ee746c1491c49bea)。

IrMC 同步命令（IrMC Sync Command）。

<a id="r_ga6eb16aacf468b460fa7675ffc4703e68"></a>

```c
#define BT_SDP_HEADSET_SVCLASS 0x1108
```

相关声明：[BT_SDP_HEADSET_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga6eb16aacf468b460fa7675ffc4703e68)。

带麦克风耳机（Headset）。

<a id="r_ga16e1bc10528ac82f6cec822912f97d8c"></a>

```c
#define BT_SDP_CORDLESS_TELEPHONY_SVCLASS 0x1109
```

相关声明：[BT_SDP_CORDLESS_TELEPHONY_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga16e1bc10528ac82f6cec822912f97d8c)。

无绳电话（Cordless Telephony）。

<a id="r_gafeb3a3184a0b83e0045187cbe3cf24dc"></a>

```c
#define BT_SDP_AUDIO_SOURCE_SVCLASS 0x110a
```

相关声明：[BT_SDP_AUDIO_SOURCE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gafeb3a3184a0b83e0045187cbe3cf24dc)。

音频源（Audio Source）。

<a id="r_gaa0e334873b5477523572caa2359a4098"></a>

```c
#define BT_SDP_AUDIO_SINK_SVCLASS 0x110b
```

相关声明：[BT_SDP_AUDIO_SINK_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa0e334873b5477523572caa2359a4098)。

音频接收端（Audio Sink）。

<a id="r_gafe96e9d32797a83c793f0ed278054b80"></a>

```c
#define BT_SDP_AV_REMOTE_TARGET_SVCLASS 0x110c
```

相关声明：[BT_SDP_AV_REMOTE_TARGET_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gafe96e9d32797a83c793f0ed278054b80)。

音视频远程控制目标端（A/V Remote Control Target）。

<a id="r_ga2fdc3eb32196b5135b7f595a36cacb4c"></a>

```c
#define BT_SDP_ADVANCED_AUDIO_SVCLASS 0x110d
```

相关声明：[BT_SDP_ADVANCED_AUDIO_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2fdc3eb32196b5135b7f595a36cacb4c)。

高级音频分发（Advanced Audio Distribution）。

<a id="r_gaea94250bed4c5e6ad47749a1237778f5"></a>

```c
#define BT_SDP_AV_REMOTE_SVCLASS 0x110e
```

相关声明：[BT_SDP_AV_REMOTE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaea94250bed4c5e6ad47749a1237778f5)。

音视频远程控制（A/V Remote Control）。

<a id="r_gaaae997769dfc8325c38830707f4d22e3"></a>

```c
#define BT_SDP_AV_REMOTE_CONTROLLER_SVCLASS 0x110f
```

相关声明：[BT_SDP_AV_REMOTE_CONTROLLER_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaaae997769dfc8325c38830707f4d22e3)。

音视频远程控制控制器（A/V Remote Control Controller）。

<a id="r_ga9681e34d78cea87e413fa4be40e4239a"></a>

```c
#define BT_SDP_INTERCOM_SVCLASS 0x1110
```

相关声明：[BT_SDP_INTERCOM_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9681e34d78cea87e413fa4be40e4239a)。

对讲（Intercom）。

<a id="r_ga31962fab5bed7c54311c4b291713a836"></a>

```c
#define BT_SDP_FAX_SVCLASS 0x1111
```

相关声明：[BT_SDP_FAX_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga31962fab5bed7c54311c4b291713a836)。

传真（Fax）。

<a id="r_ga4c9322cf28a8b1aa96828152e8ee7379"></a>

```c
#define BT_SDP_HEADSET_AGW_SVCLASS 0x1112
```

相关声明：[BT_SDP_HEADSET_AGW_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4c9322cf28a8b1aa96828152e8ee7379)。

耳机音频网关（Headset AG）。

<a id="r_ga2ab79d7ff4e88820773cf24f0b0b6e20"></a>

```c
#define BT_SDP_WAP_SVCLASS 0x1113
```

相关声明：[BT_SDP_WAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2ab79d7ff4e88820773cf24f0b0b6e20)。

无线应用协议（WAP）。

<a id="r_ga22624d29917aaeaa0c281d9517178821"></a>

```c
#define BT_SDP_WAP_CLIENT_SVCLASS 0x1114
```

相关声明：[BT_SDP_WAP_CLIENT_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga22624d29917aaeaa0c281d9517178821)。

无线应用协议客户端（WAP Client）。

<a id="r_gaa9abb444e3b43c1164d6b450b1c066e5"></a>

```c
#define BT_SDP_PANU_SVCLASS 0x1115
```

相关声明：[BT_SDP_PANU_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa9abb444e3b43c1164d6b450b1c066e5)。

个人区域网络用户（Personal Area Networking User）。

<a id="r_ga78a7be1db8be8d7eece0d17c629dd009"></a>

```c
#define BT_SDP_NAP_SVCLASS 0x1116
```

相关声明：[BT_SDP_NAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga78a7be1db8be8d7eece0d17c629dd009)。

网络接入点（Network Access Point）。

<a id="r_gaed2d6f72c344e2e9b9bdcefd23cb4086"></a>

```c
#define BT_SDP_GN_SVCLASS 0x1117
```

相关声明：[BT_SDP_GN_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaed2d6f72c344e2e9b9bdcefd23cb4086)。

组网络（Group Network）。

<a id="r_ga30f6edbd67d96f7752a223409c8e4431"></a>

```c
#define BT_SDP_DIRECT_PRINTING_SVCLASS 0x1118
```

相关声明：[BT_SDP_DIRECT_PRINTING_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga30f6edbd67d96f7752a223409c8e4431)。

直接打印（Direct Printing）。

<a id="r_ga6bc247854656613d2fa9b47d55bd69d6"></a>

```c
#define BT_SDP_REFERENCE_PRINTING_SVCLASS 0x1119
```

相关声明：[BT_SDP_REFERENCE_PRINTING_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga6bc247854656613d2fa9b47d55bd69d6)。

引用打印（Reference Printing）。

<a id="r_ga08730b1fd7088101fadb85e5dc13fd24"></a>

```c
#define BT_SDP_IMAGING_SVCLASS 0x111a
```

相关声明：[BT_SDP_IMAGING_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga08730b1fd7088101fadb85e5dc13fd24)。

基本图像配置文件（Basic Imaging Profile）。

<a id="r_gaf19cd136b780ef303c1290b26ab2ca17"></a>

```c
#define BT_SDP_IMAGING_RESPONDER_SVCLASS 0x111b
```

相关声明：[BT_SDP_IMAGING_RESPONDER_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf19cd136b780ef303c1290b26ab2ca17)。

图像响应端（Imaging Responder）。

<a id="r_ga3f04a28d9764a0c7755babe379c25393"></a>

```c
#define BT_SDP_IMAGING_ARCHIVE_SVCLASS 0x111c
```

相关声明：[BT_SDP_IMAGING_ARCHIVE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3f04a28d9764a0c7755babe379c25393)。

图像自动归档（Imaging Automatic Archive）。

<a id="r_ga51a4cfc28f86a650b03a7bbe6e5b883a"></a>

```c
#define BT_SDP_IMAGING_REFOBJS_SVCLASS 0x111d
```

相关声明：[BT_SDP_IMAGING_REFOBJS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga51a4cfc28f86a650b03a7bbe6e5b883a)。

图像引用对象（Imaging Referenced Objects）。

<a id="r_gab9f99989420545b3b0e71da6c5475f90"></a>

```c
#define BT_SDP_HANDSFREE_SVCLASS 0x111e
```

相关声明：[BT_SDP_HANDSFREE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab9f99989420545b3b0e71da6c5475f90)。

免提（Handsfree）。

<a id="r_ga1c44ae236a292c91dc81539c9c89947c"></a>

```c
#define BT_SDP_HANDSFREE_AGW_SVCLASS 0x111f
```

相关声明：[BT_SDP_HANDSFREE_AGW_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1c44ae236a292c91dc81539c9c89947c)。

免提音频网关（Handsfree Audio Gateway）。

<a id="r_ga79d34c3b7641cf523adf6515720ceceb"></a>

```c
#define BT_SDP_DIRECT_PRT_REFOBJS_SVCLASS 0x1120
```

相关声明：[BT_SDP_DIRECT_PRT_REFOBJS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga79d34c3b7641cf523adf6515720ceceb)。

直接打印引用对象服务（Direct Printing Reference Objects Service）。

<a id="r_ga78607a42f5228b37d348614b12e48a77"></a>

```c
#define BT_SDP_REFLECTED_UI_SVCLASS 0x1121
```

相关声明：[BT_SDP_REFLECTED_UI_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga78607a42f5228b37d348614b12e48a77)。

映射用户界面（Reflected UI）。

<a id="r_gac727f387a55a76c9a071cf62792f50e4"></a>

```c
#define BT_SDP_BASIC_PRINTING_SVCLASS 0x1122
```

相关声明：[BT_SDP_BASIC_PRINTING_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac727f387a55a76c9a071cf62792f50e4)。

基本打印（Basic Printing）。

<a id="r_ga9298ac73a26a1ab2e53733f404e5c6ea"></a>

```c
#define BT_SDP_PRINTING_STATUS_SVCLASS 0x1123
```

相关声明：[BT_SDP_PRINTING_STATUS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9298ac73a26a1ab2e53733f404e5c6ea)。

打印状态（Printing Status）。

<a id="r_gab63eab5791898a47bd540eed4d55cddc"></a>

```c
#define BT_SDP_HID_SVCLASS 0x1124
```

相关声明：[BT_SDP_HID_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab63eab5791898a47bd540eed4d55cddc)。

人机接口设备服务（Human Interface Device Service）。

<a id="r_ga873f8e03aeb696d3eb287a8d00796a4f"></a>

```c
#define BT_SDP_HCR_SVCLASS 0x1125
```

相关声明：[BT_SDP_HCR_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga873f8e03aeb696d3eb287a8d00796a4f)。

硬拷贝线缆替代（Hardcopy Cable Replacement）。

<a id="r_ga4ca1e6eb6fe385e526f8d84ed65ab285"></a>

```c
#define BT_SDP_HCR_PRINT_SVCLASS 0x1126
```

相关声明：[BT_SDP_HCR_PRINT_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4ca1e6eb6fe385e526f8d84ed65ab285)。

HCR 打印（HCR Print）。

<a id="r_ga621afe0f5a6d176c26e140c4162bee07"></a>

```c
#define BT_SDP_HCR_SCAN_SVCLASS 0x1127
```

相关声明：[BT_SDP_HCR_SCAN_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga621afe0f5a6d176c26e140c4162bee07)。

HCR 扫描（HCR Scan）。

<a id="r_ga9617c02c6999d9fe987e91c6c2dc5dca"></a>

```c
#define BT_SDP_CIP_SVCLASS 0x1128
```

相关声明：[BT_SDP_CIP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9617c02c6999d9fe987e91c6c2dc5dca)。

通用 ISDN 访问（Common ISDN Access）。

<a id="r_ga3e087c095a78f07efae660eceae9c11e"></a>

```c
#define BT_SDP_VIDEO_CONF_GW_SVCLASS 0x1129
```

相关声明：[BT_SDP_VIDEO_CONF_GW_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3e087c095a78f07efae660eceae9c11e)。

视频会议网关（Video Conferencing Gateway）。

<a id="r_ga629179357eff2cd60621f0e1e435df06"></a>

```c
#define BT_SDP_UDI_MT_SVCLASS 0x112a
```

相关声明：[BT_SDP_UDI_MT_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga629179357eff2cd60621f0e1e435df06)。

UDI MT 服务（UDI MT）。

<a id="r_ga846599abf75f1cbb27028aea8a619f31"></a>

```c
#define BT_SDP_UDI_TA_SVCLASS 0x112b
```

相关声明：[BT_SDP_UDI_TA_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga846599abf75f1cbb27028aea8a619f31)。

UDI TA 服务（UDI TA）。

<a id="r_gab7a8499dbb73a2700389d55d331bd23e"></a>

```c
#define BT_SDP_AV_SVCLASS 0x112c
```

相关声明：[BT_SDP_AV_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab7a8499dbb73a2700389d55d331bd23e)。

音频／视频（Audio/Video）。

<a id="r_gad2234f8e0bce0e6b55d18c7a7c950e1d"></a>

```c
#define BT_SDP_SAP_SVCLASS 0x112d
```

相关声明：[BT_SDP_SAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad2234f8e0bce0e6b55d18c7a7c950e1d)。

SIM 卡访问（SIM Access）。

<a id="r_gaec2475b7ba36b860c0f8a9cfc33df4a8"></a>

```c
#define BT_SDP_PBAP_PCE_SVCLASS 0x112e
```

相关声明：[BT_SDP_PBAP_PCE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaec2475b7ba36b860c0f8a9cfc33df4a8)。

电话簿访问客户端（Phonebook Access Client）。

<a id="r_ga612bb83e9f08edd163433a5fbe9528fc"></a>

```c
#define BT_SDP_PBAP_PSE_SVCLASS 0x112f
```

相关声明：[BT_SDP_PBAP_PSE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga612bb83e9f08edd163433a5fbe9528fc)。

电话簿访问服务器（Phonebook Access Server）。

<a id="r_ga60a9fad26300c15e988e101f90c06435"></a>

```c
#define BT_SDP_PBAP_SVCLASS 0x1130
```

相关声明：[BT_SDP_PBAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga60a9fad26300c15e988e101f90c06435)。

电话簿访问（Phonebook Access）。

<a id="r_ga58f5cc54014e3723720e7c3b7ba82fd8"></a>

```c
#define BT_SDP_MAP_MSE_SVCLASS 0x1132
```

相关声明：[BT_SDP_MAP_MSE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga58f5cc54014e3723720e7c3b7ba82fd8)。

消息访问服务器（Message Access Server）。

<a id="r_ga47849c599678f7ec48c237b8b36e9cb7"></a>

```c
#define BT_SDP_MAP_MCE_SVCLASS 0x1133
```

相关声明：[BT_SDP_MAP_MCE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga47849c599678f7ec48c237b8b36e9cb7)。

消息通知服务器（Message Notification Server）。

<a id="r_gaec665050af4cc3affcef3912bb212fc0"></a>

```c
#define BT_SDP_MAP_SVCLASS 0x1134
```

相关声明：[BT_SDP_MAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaec665050af4cc3affcef3912bb212fc0)。

消息访问配置文件（Message Access Profile）。

<a id="r_ga300585062ed9ae05daca226cb3c5440d"></a>

```c
#define BT_SDP_GNSS_SVCLASS 0x1135
```

相关声明：[BT_SDP_GNSS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga300585062ed9ae05daca226cb3c5440d)。

全球导航卫星系统（GNSS）

<a id="r_gacdfb8ca6a776f57a2df38b4a6eaa8403"></a>

```c
#define BT_SDP_GNSS_SERVER_SVCLASS 0x1136
```

相关声明：[BT_SDP_GNSS_SERVER_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gacdfb8ca6a776f57a2df38b4a6eaa8403)。

全球导航卫星系统服务器（GNSS Server）。

<a id="r_ga9cce7e3a576329661b363b102cefa494"></a>

```c
#define BT_SDP_MPS_SC_SVCLASS 0x113a
```

相关声明：[BT_SDP_MPS_SC_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9cce7e3a576329661b363b102cefa494)。

MPS SC 服务标识（MPS SC）。

<a id="r_gaf847b2675482d3bb9674f569c3604e40"></a>

```c
#define BT_SDP_MPS_SVCLASS 0x113b
```

相关声明：[BT_SDP_MPS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf847b2675482d3bb9674f569c3604e40)。

多配置文件规范（MPS）。

<a id="r_gaed5403661e0eb8f798a950bead59369a"></a>

```c
#define BT_SDP_PNP_INFO_SVCLASS 0x1200
```

相关声明：[BT_SDP_PNP_INFO_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaed5403661e0eb8f798a950bead59369a)。

即插即用信息（PnP Information）。

<a id="r_ga1b9a169ff4db4fda939cba3ce21f808b"></a>

```c
#define BT_SDP_GENERIC_NETWORKING_SVCLASS 0x1201
```

相关声明：[BT_SDP_GENERIC_NETWORKING_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1b9a169ff4db4fda939cba3ce21f808b)。

通用联网（Generic Networking）。

<a id="r_gaa8e5c423fca1fb0d06504cdc5be276d1"></a>

```c
#define BT_SDP_GENERIC_FILETRANS_SVCLASS 0x1202
```

相关声明：[BT_SDP_GENERIC_FILETRANS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa8e5c423fca1fb0d06504cdc5be276d1)。

通用文件传输（Generic File Transfer）。

<a id="r_gaec7548467ffb686b22a907d05e38f275"></a>

```c
#define BT_SDP_GENERIC_AUDIO_SVCLASS 0x1203
```

相关声明：[BT_SDP_GENERIC_AUDIO_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaec7548467ffb686b22a907d05e38f275)。

通用音频（Generic Audio）。

<a id="r_ga010b005cfdb69c67cfc7e3c5c8426778"></a>

```c
#define BT_SDP_GENERIC_TELEPHONY_SVCLASS 0x1204
```

相关声明：[BT_SDP_GENERIC_TELEPHONY_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga010b005cfdb69c67cfc7e3c5c8426778)。

通用电话（Generic Telephony）。

<a id="r_ga9e7fa3bcf139462a2c33f90b526e1ad1"></a>

```c
#define BT_SDP_UPNP_SVCLASS 0x1205
```

相关声明：[BT_SDP_UPNP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9e7fa3bcf139462a2c33f90b526e1ad1)。

通用即插即用服务（UPnP Service）。

<a id="r_ga102b24708429877c4f37a5008fb176b1"></a>

```c
#define BT_SDP_UPNP_IP_SVCLASS 0x1206
```

相关声明：[BT_SDP_UPNP_IP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga102b24708429877c4f37a5008fb176b1)。

UPnP IP 服务（UPnP IP Service）。

<a id="r_ga3f50947a742b24089f86193e773d623b"></a>

```c
#define BT_SDP_UPNP_PAN_SVCLASS 0x1300
```

相关声明：[BT_SDP_UPNP_PAN_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3f50947a742b24089f86193e773d623b)。

UPnP IP 个人区域网络（UPnP IP PAN）。

<a id="r_gad418094573383e6252719abed97d24dd"></a>

```c
#define BT_SDP_UPNP_LAP_SVCLASS 0x1301
```

相关声明：[BT_SDP_UPNP_LAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad418094573383e6252719abed97d24dd)。

UPnP IP 局域网访问配置文件（UPnP IP LAP）。

<a id="r_gad4d97c0b664c48bdc0842f92240409c7"></a>

```c
#define BT_SDP_UPNP_L2CAP_SVCLASS 0x1302
```

相关声明：[BT_SDP_UPNP_L2CAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad4d97c0b664c48bdc0842f92240409c7)。

UPnP IP L2CAP（UPnP IP L2CAP）。

<a id="r_ga17d7fb3a77ef7266ea2d760fb3696a83"></a>

```c
#define BT_SDP_VIDEO_SOURCE_SVCLASS 0x1303
```

相关声明：[BT_SDP_VIDEO_SOURCE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga17d7fb3a77ef7266ea2d760fb3696a83)。

视频源（Video Source）。

<a id="r_ga1e3428b6d0197bd7c9d72154c025e9f5"></a>

```c
#define BT_SDP_VIDEO_SINK_SVCLASS 0x1304
```

相关声明：[BT_SDP_VIDEO_SINK_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1e3428b6d0197bd7c9d72154c025e9f5)。

视频接收端（Video Sink）。

<a id="r_ga4e2ef8310c9396f9fb7781ab4732f308"></a>

```c
#define BT_SDP_VIDEO_DISTRIBUTION_SVCLASS 0x1305
```

相关声明：[BT_SDP_VIDEO_DISTRIBUTION_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4e2ef8310c9396f9fb7781ab4732f308)。

视频分发（Video Distribution）。

<a id="r_gaf8fc80f3b2ff245b7d354aa0488bb42b"></a>

```c
#define BT_SDP_HDP_SVCLASS 0x1400
```

相关声明：[BT_SDP_HDP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf8fc80f3b2ff245b7d354aa0488bb42b)。

健康设备配置文件（HDP）。

<a id="r_ga87ba9fdf39fb99397a6dec4d92b6e3f1"></a>

```c
#define BT_SDP_HDP_SOURCE_SVCLASS 0x1401
```

相关声明：[BT_SDP_HDP_SOURCE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga87ba9fdf39fb99397a6dec4d92b6e3f1)。

健康设备配置文件源端（HDP Source）。

<a id="r_ga2125a92c6eb724a63d04188919a12bf1"></a>

```c
#define BT_SDP_HDP_SINK_SVCLASS 0x1402
```

相关声明：[BT_SDP_HDP_SINK_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2125a92c6eb724a63d04188919a12bf1)。

健康设备配置文件接收端（HDP Sink）。

<a id="r_gae8010af5b12cd1c1b1633a4d2c9f5ab0"></a>

```c
#define BT_SDP_GENERIC_ACCESS_SVCLASS 0x1800
```

相关声明：[BT_SDP_GENERIC_ACCESS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gae8010af5b12cd1c1b1633a4d2c9f5ab0)。

通用访问配置文件（Generic Access Profile）。

<a id="r_gad3f345431526bb713921f4b51c48b056"></a>

```c
#define BT_SDP_GENERIC_ATTRIB_SVCLASS 0x1801
```

相关声明：[BT_SDP_GENERIC_ATTRIB_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad3f345431526bb713921f4b51c48b056)。

通用属性配置文件（Generic Attribute Profile）。

<a id="r_ga694b04c2dae3b06b7fd66640468a5a38"></a>

```c
#define BT_SDP_APPLE_AGENT_SVCLASS 0x2112
```

相关声明：[BT_SDP_APPLE_AGENT_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga694b04c2dae3b06b7fd66640468a5a38)。

Apple 代理（Apple Agent）。

<a id="define-members-1"></a>

### 属性标识符编码（Attribute identifier codes）

`attribute-id` 的可能值列在下方。

详情参见 SDP 规范中的“服务属性定义（Service Attribute Definitions）”一节。

<a id="r_ga38f32cae462272b51eb4edca0c5c95a2"></a>

```c
#define BT_SDP_ATTR_RECORD_HANDLE 0x0000
```

相关声明：[BT_SDP_ATTR_RECORD_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga38f32cae462272b51eb4edca0c5c95a2)。

服务记录句柄（Service Record Handle）。

<a id="r_gab5c5be56c54d3f8bd4ac6defff0b1e7c"></a>

```c
#define BT_SDP_ATTR_SVCLASS_ID_LIST 0x0001
```

相关声明：[BT_SDP_ATTR_SVCLASS_ID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab5c5be56c54d3f8bd4ac6defff0b1e7c)。

服务类别 ID 列表（Service Class ID List）。

<a id="r_ga4d458591f8eba26feaab1220c49f6a29"></a>

```c
#define BT_SDP_ATTR_RECORD_STATE 0x0002
```

相关声明：[BT_SDP_ATTR_RECORD_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4d458591f8eba26feaab1220c49f6a29)。

服务记录状态（Service Record State）。

<a id="r_gad2149fd761f7ae2ea6ef761ab2545ab4"></a>

```c
#define BT_SDP_ATTR_SERVICE_ID 0x0003
```

相关声明：[BT_SDP_ATTR_SERVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad2149fd761f7ae2ea6ef761ab2545ab4)。

服务 ID（Service ID）。

<a id="r_ga3e7dad966deab42ff9fa0fd04d3d4514"></a>

```c
#define BT_SDP_ATTR_PROTO_DESC_LIST 0x0004
```

相关声明：[BT_SDP_ATTR_PROTO_DESC_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3e7dad966deab42ff9fa0fd04d3d4514)。

协议描述符列表（Protocol Descriptor List）。

<a id="r_ga2609212bf5400c31351bc3ec5f60a7e1"></a>

```c
#define BT_SDP_ATTR_BROWSE_GRP_LIST 0x0005
```

相关声明：[BT_SDP_ATTR_BROWSE_GRP_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2609212bf5400c31351bc3ec5f60a7e1)。

浏览组列表（Browse Group List）。

<a id="r_ga462ec997a81c6b439a24e2de085676ab"></a>

```c
#define BT_SDP_ATTR_LANG_BASE_ATTR_ID_LIST 0x0006
```

相关声明：[BT_SDP_ATTR_LANG_BASE_ATTR_ID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga462ec997a81c6b439a24e2de085676ab)。

语言基础属性 ID 列表（Language Base Attribute ID List）。

<a id="r_ga7ef037ed6628aa7354736295e0e4ec77"></a>

```c
#define BT_SDP_ATTR_SVCINFO_TTL 0x0007
```

相关声明：[BT_SDP_ATTR_SVCINFO_TTL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga7ef037ed6628aa7354736295e0e4ec77)。

服务信息生存时间（Service Info Time to Live）。

<a id="r_gaf55a72ce05def1da08d15a23cee4c5e3"></a>

```c
#define BT_SDP_ATTR_SERVICE_AVAILABILITY 0x0008
```

相关声明：[BT_SDP_ATTR_SERVICE_AVAILABILITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf55a72ce05def1da08d15a23cee4c5e3)。

服务可用性（Service Availability）。

<a id="r_ga0b5b19caa523e4cb9da8a2bfc6eab20a"></a>

```c
#define BT_SDP_ATTR_PROFILE_DESC_LIST 0x0009
```

相关声明：[BT_SDP_ATTR_PROFILE_DESC_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga0b5b19caa523e4cb9da8a2bfc6eab20a)。

蓝牙配置文件描述符列表（Bluetooth Profile Descriptor List）。

<a id="r_gad8302739bca706f6da851d912ada0f82"></a>

```c
#define BT_SDP_ATTR_DOC_URL 0x000a
```

相关声明：[BT_SDP_ATTR_DOC_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad8302739bca706f6da851d912ada0f82)。

文档 URL（Documentation URL）。

<a id="r_ga0bc613d68dace4cce7a4eec654f5a1e4"></a>

```c
#define BT_SDP_ATTR_CLNT_EXEC_URL 0x000b
```

相关声明：[BT_SDP_ATTR_CLNT_EXEC_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga0bc613d68dace4cce7a4eec654f5a1e4)。

客户端可执行文件 URL（Client Executable URL）。

<a id="r_ga365048bcb0ad2989aec9dd0d89abbfb9"></a>

```c
#define BT_SDP_ATTR_ICON_URL 0x000c
```

相关声明：[BT_SDP_ATTR_ICON_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga365048bcb0ad2989aec9dd0d89abbfb9)。

图标 URL（Icon URL）。

<a id="r_gaf7f0b2f30ede36cf280bf31c5e76a99c"></a>

```c
#define BT_SDP_ATTR_ADD_PROTO_DESC_LIST 0x000d
```

相关声明：[BT_SDP_ATTR_ADD_PROTO_DESC_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf7f0b2f30ede36cf280bf31c5e76a99c)。

附加协议描述符列表（Additional Protocol Descriptor List）。

<a id="r_ga15a104c78357f2353cd49eb858de057d"></a>

```c
#define BT_SDP_ATTR_GROUP_ID 0x0200
```

相关声明：[BT_SDP_ATTR_GROUP_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga15a104c78357f2353cd49eb858de057d)。

组 ID（Group ID）。

<a id="r_ga23a63b424ab381048cb898ebbdb64a02"></a>

```c
#define BT_SDP_ATTR_IP_SUBNET 0x0200
```

相关声明：[BT_SDP_ATTR_IP_SUBNET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga23a63b424ab381048cb898ebbdb64a02)。

IP 子网（IP Subnet）。

<a id="r_gab698c476197acca0d499e39f7f246c66"></a>

```c
#define BT_SDP_ATTR_VERSION_NUM_LIST 0x0200
```

相关声明：[BT_SDP_ATTR_VERSION_NUM_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab698c476197acca0d499e39f7f246c66)。

版本号列表（Version Number List）。

<a id="r_ga8a693e5265c7801e3c1125473c31445f"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_FEATURES_LIST 0x0200
```

相关声明：[BT_SDP_ATTR_SUPPORTED_FEATURES_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga8a693e5265c7801e3c1125473c31445f)。

支持的特性列表（Supported Features List）。

<a id="r_gac7583b3d2a0ebc82e5cf2e6705249201"></a>

```c
#define BT_SDP_ATTR_GOEP_L2CAP_PSM 0x0200
```

相关声明：[BT_SDP_ATTR_GOEP_L2CAP_PSM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac7583b3d2a0ebc82e5cf2e6705249201)。

通用对象交换配置文件的 L2CAP PSM（GOEP L2CAP PSM）。

<a id="r_gab8fe8881b4470ab3522e710e36470ddb"></a>

```c
#define BT_SDP_ATTR_SVCDB_STATE 0x0201
```

相关声明：[BT_SDP_ATTR_SVCDB_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab8fe8881b4470ab3522e710e36470ddb)。

服务数据库状态（Service Database State）。

<a id="r_ga39b3436f9da303bd2ce1ad38f072ed9f"></a>

```c
#define BT_SDP_ATTR_MPSD_SCENARIOS 0x0200
```

相关声明：[BT_SDP_ATTR_MPSD_SCENARIOS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga39b3436f9da303bd2ce1ad38f072ed9f)。

MPSD 场景（MPSD Scenarios）。

<a id="r_gaa3cc3d9a6ac7375e66b0892631698fd0"></a>

```c
#define BT_SDP_ATTR_MPMD_SCENARIOS 0x0201
```

相关声明：[BT_SDP_ATTR_MPMD_SCENARIOS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa3cc3d9a6ac7375e66b0892631698fd0)。

MPMD 场景（MPMD Scenarios）。

<a id="r_ga45795e50564492ac9bce8d6832883741"></a>

```c
#define BT_SDP_ATTR_MPS_DEPENDENCIES 0x0202
```

相关声明：[BT_SDP_ATTR_MPS_DEPENDENCIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga45795e50564492ac9bce8d6832883741)。

支持的配置文件与协议（Supported Profiles & Protocols）。

<a id="r_ga230f70b576c14ba1dbe0cf6eda6220e0"></a>

```c
#define BT_SDP_ATTR_SERVICE_VERSION 0x0300
```

相关声明：[BT_SDP_ATTR_SERVICE_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga230f70b576c14ba1dbe0cf6eda6220e0)。

服务版本（Service Version）。

<a id="r_ga617dc829eb1192cd283bef67a357d75f"></a>

```c
#define BT_SDP_ATTR_EXTERNAL_NETWORK 0x0301
```

相关声明：[BT_SDP_ATTR_EXTERNAL_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga617dc829eb1192cd283bef67a357d75f)。

外部网络（External Network）。

<a id="r_gae12e2daea8febbbd047c1c3843f56933"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_DATA_STORES_LIST 0x0301
```

相关声明：[BT_SDP_ATTR_SUPPORTED_DATA_STORES_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gae12e2daea8febbbd047c1c3843f56933)。

支持的数据存储列表（Supported Data Stores List）。

<a id="r_ga4732f83c88de43a90ca3d58a136907b6"></a>

```c
#define BT_SDP_ATTR_DATA_EXCHANGE_SPEC 0x0301
```

相关声明：[BT_SDP_ATTR_DATA_EXCHANGE_SPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4732f83c88de43a90ca3d58a136907b6)。

数据交换规范（Data Exchange Specification）。

<a id="r_ga9c78d47f54e82a51f7d04a6f6c97663c"></a>

```c
#define BT_SDP_ATTR_NETWORK 0x0301
```

相关声明：[BT_SDP_ATTR_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9c78d47f54e82a51f7d04a6f6c97663c)。

网络（Network）

<a id="r_gaeebfb4a085417db65241b21a27258d84"></a>

```c
#define BT_SDP_ATTR_FAX_CLASS1_SUPPORT 0x0302
```

相关声明：[BT_SDP_ATTR_FAX_CLASS1_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaeebfb4a085417db65241b21a27258d84)。

传真类别 1 支持（Fax Class 1 Support）。

<a id="r_gaa122bfee476a8e83346823e23978f7a0"></a>

```c
#define BT_SDP_ATTR_REMOTE_AUDIO_VOLUME_CONTROL 0x0302
```

相关声明：[BT_SDP_ATTR_REMOTE_AUDIO_VOLUME_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa122bfee476a8e83346823e23978f7a0)。

远程音频音量控制（Remote Audio Volume Control）。

<a id="r_ga54e285c7a12becef9742093e1777c06b"></a>

```c
#define BT_SDP_ATTR_MCAP_SUPPORTED_PROCEDURES 0x0302
```

相关声明：[BT_SDP_ATTR_MCAP_SUPPORTED_PROCEDURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga54e285c7a12becef9742093e1777c06b)。

多通道适配协议支持的过程（MCAP Supported Procedures）。

<a id="r_ga861470cd4b505d074abb727ba72c088a"></a>

```c
#define BT_SDP_ATTR_FAX_CLASS20_SUPPORT 0x0303
```

相关声明：[BT_SDP_ATTR_FAX_CLASS20_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga861470cd4b505d074abb727ba72c088a)。

传真类别 2.0 支持（Fax Class 2.0 Support）。

<a id="r_gac12ed37044c3f12c2d41b1fd23eacada"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_FORMATS_LIST 0x0303
```

相关声明：[BT_SDP_ATTR_SUPPORTED_FORMATS_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac12ed37044c3f12c2d41b1fd23eacada)。

支持的格式列表（Supported Formats List）。

<a id="r_ga2475947ccdb9f30ece61a34959fd6ce2"></a>

```c
#define BT_SDP_ATTR_FAX_CLASS2_SUPPORT 0x0304
```

相关声明：[BT_SDP_ATTR_FAX_CLASS2_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2475947ccdb9f30ece61a34959fd6ce2)。

传真类别 2 支持，厂商专用（Fax Class 2 Support (vendor-specific)）。

<a id="r_gac4906f9fa368fbf604830cd5c5fdcb57"></a>

```c
#define BT_SDP_ATTR_AUDIO_FEEDBACK_SUPPORT 0x0305
```

相关声明：[BT_SDP_ATTR_AUDIO_FEEDBACK_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac4906f9fa368fbf604830cd5c5fdcb57)。

音频反馈支持（Audio Feedback Support）。

<a id="r_ga74dacfd7807d7f3ec7a7594a9329f0b2"></a>

```c
#define BT_SDP_ATTR_NETWORK_ADDRESS 0x0306
```

相关声明：[BT_SDP_ATTR_NETWORK_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga74dacfd7807d7f3ec7a7594a9329f0b2)。

网络地址（Network Address）。

<a id="r_ga1ef964c955473601910ee3997b9ce5cd"></a>

```c
#define BT_SDP_ATTR_WAP_GATEWAY 0x0307
```

相关声明：[BT_SDP_ATTR_WAP_GATEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1ef964c955473601910ee3997b9ce5cd)。

无线应用协议网关（WAP Gateway）。

<a id="r_gafeff5e5b60bd47c44f8edbe8ff7e78a0"></a>

```c
#define BT_SDP_ATTR_HOMEPAGE_URL 0x0308
```

相关声明：[BT_SDP_ATTR_HOMEPAGE_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gafeff5e5b60bd47c44f8edbe8ff7e78a0)。

主页 URL（Homepage URL）。

<a id="r_gae1a3ff84a5588e55258c35ee57d6a5b5"></a>

```c
#define BT_SDP_ATTR_WAP_STACK_TYPE 0x0309
```

相关声明：[BT_SDP_ATTR_WAP_STACK_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gae1a3ff84a5588e55258c35ee57d6a5b5)。

无线应用协议栈类型（WAP Stack Type）。

<a id="r_ga21214c2236a5dca24a45998640761e7b"></a>

```c
#define BT_SDP_ATTR_SECURITY_DESC 0x030a
```

相关声明：[BT_SDP_ATTR_SECURITY_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga21214c2236a5dca24a45998640761e7b)。

安全描述（Security Description）。

<a id="r_ga13851f9f9a5ba8514d20cffbe5eb9f14"></a>

```c
#define BT_SDP_ATTR_NET_ACCESS_TYPE 0x030b
```

相关声明：[BT_SDP_ATTR_NET_ACCESS_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga13851f9f9a5ba8514d20cffbe5eb9f14)。

网络接入类型（Net Access Type）。

<a id="r_ga7347caab1c7e8755250567d9d8cc7266"></a>

```c
#define BT_SDP_ATTR_MAX_NET_ACCESSRATE 0x030c
```

相关声明：[BT_SDP_ATTR_MAX_NET_ACCESSRATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga7347caab1c7e8755250567d9d8cc7266)。

最大网络接入速率（Max Net Access Rate）。

<a id="r_ga01c0cdb8975484242e6c4b052dabfd91"></a>

```c
#define BT_SDP_ATTR_IP4_SUBNET 0x030d
```

相关声明：[BT_SDP_ATTR_IP4_SUBNET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga01c0cdb8975484242e6c4b052dabfd91)。

IPv4 子网（IPv4 Subnet）。

<a id="r_ga10b3d4826904489d474af5e9c21c0831"></a>

```c
#define BT_SDP_ATTR_IP6_SUBNET 0x030e
```

相关声明：[BT_SDP_ATTR_IP6_SUBNET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga10b3d4826904489d474af5e9c21c0831)。

IPv6 子网（IPv6 Subnet）。

<a id="r_ga5347dbc038ac9c259d17c14ed9a812d3"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_CAPABILITIES 0x0310
```

相关声明：[BT_SDP_ATTR_SUPPORTED_CAPABILITIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5347dbc038ac9c259d17c14ed9a812d3)。

基本图像配置文件支持的能力（BIP Supported Capabilities）。

<a id="r_ga498d9beaa7877570fe834d854de36fcb"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_FEATURES 0x0311
```

相关声明：[BT_SDP_ATTR_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga498d9beaa7877570fe834d854de36fcb)。

基本图像配置文件支持的特性（BIP Supported Features）。

<a id="r_gabc7cdfd247da5e2ecfd441c0436471f3"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_FUNCTIONS 0x0312
```

相关声明：[BT_SDP_ATTR_SUPPORTED_FUNCTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gabc7cdfd247da5e2ecfd441c0436471f3)。

基本图像配置文件支持的功能（BIP Supported Functions）。

<a id="r_gadbce181b739c201070d6abcbdc4139f4"></a>

```c
#define BT_SDP_ATTR_TOTAL_IMAGING_DATA_CAPACITY 0x0313
```

相关声明：[BT_SDP_ATTR_TOTAL_IMAGING_DATA_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gadbce181b739c201070d6abcbdc4139f4)。

基本图像配置文件总图像数据容量（BIP Total Imaging Data Capacity）。

<a id="r_gada3d989d6c8c0664ba0bf998414a0328"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_REPOSITORIES 0x0314
```

相关声明：[BT_SDP_ATTR_SUPPORTED_REPOSITORIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gada3d989d6c8c0664ba0bf998414a0328)。

支持的存储库（Supported Repositories）。

<a id="r_ga03d653957d68b5d0eeda1fa7c9aa4587"></a>

```c
#define BT_SDP_ATTR_MAS_INSTANCE_ID 0x0315
```

相关声明：[BT_SDP_ATTR_MAS_INSTANCE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga03d653957d68b5d0eeda1fa7c9aa4587)。

消息访问服务器实例 ID（MAS Instance ID）。

<a id="r_ga41fc674e8571556397135734d28b829a"></a>

```c
#define BT_SDP_ATTR_SUPPORTED_MESSAGE_TYPES 0x0316
```

相关声明：[BT_SDP_ATTR_SUPPORTED_MESSAGE_TYPES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga41fc674e8571556397135734d28b829a)。

支持的消息类型（Supported Message Types）。

<a id="r_gaa681b17ebfe013c196cf372dcd030c6e"></a>

```c
#define BT_SDP_ATTR_PBAP_SUPPORTED_FEATURES 0x0317
```

相关声明：[BT_SDP_ATTR_PBAP_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa681b17ebfe013c196cf372dcd030c6e)。

电话簿访问配置文件支持的特性（PBAP Supported Features）。

<a id="r_gaa50f16945c15f7a954c10dbc8fc394bf"></a>

```c
#define BT_SDP_ATTR_MAP_SUPPORTED_FEATURES 0x0317
```

相关声明：[BT_SDP_ATTR_MAP_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa50f16945c15f7a954c10dbc8fc394bf)。

消息访问配置文件支持的特性（MAP Supported Features）。

<a id="r_ga4af959fbdfe7cee84008642091df948d"></a>

```c
#define BT_SDP_ATTR_SPECIFICATION_ID 0x0200
```

相关声明：[BT_SDP_ATTR_SPECIFICATION_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4af959fbdfe7cee84008642091df948d)。

规范 ID（Specification ID）。

<a id="r_gab5c2534491b43cfc9d2c7e8807b29ff2"></a>

```c
#define BT_SDP_ATTR_VENDOR_ID 0x0201
```

相关声明：[BT_SDP_ATTR_VENDOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab5c2534491b43cfc9d2c7e8807b29ff2)。

厂商标识符（Vendor ID）。

<a id="r_gaac9298efffbcf07303f972a12b50f4b6"></a>

```c
#define BT_SDP_ATTR_PRODUCT_ID 0x0202
```

相关声明：[BT_SDP_ATTR_PRODUCT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaac9298efffbcf07303f972a12b50f4b6)。

产品标识符（Product ID）。

<a id="r_gae0f4af728f964ee1c11d86b785575a87"></a>

```c
#define BT_SDP_ATTR_VERSION 0x0203
```

相关声明：[BT_SDP_ATTR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gae0f4af728f964ee1c11d86b785575a87)。

版本（Version）。

<a id="r_ga0868f7d90e3944f105028868511896cf"></a>

```c
#define BT_SDP_ATTR_PRIMARY_RECORD 0x0204
```

相关声明：[BT_SDP_ATTR_PRIMARY_RECORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga0868f7d90e3944f105028868511896cf)。

主记录（Primary Record）。

<a id="r_gad0ac4a65c51ccdf4cd128eb8697e56ca"></a>

```c
#define BT_SDP_ATTR_VENDOR_ID_SOURCE 0x0205
```

相关声明：[BT_SDP_ATTR_VENDOR_ID_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad0ac4a65c51ccdf4cd128eb8697e56ca)。

厂商 ID 来源（Vendor ID Source）。

<a id="r_gab33be247c7574e985dfb34e3c121dd23"></a>

```c
#define BT_SDP_ATTR_HID_DEVICE_RELEASE_NUMBER 0x0200
```

相关声明：[BT_SDP_ATTR_HID_DEVICE_RELEASE_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab33be247c7574e985dfb34e3c121dd23)。

人机接口设备发行版本号（HID Device Release Number）。

<a id="r_ga8bb0a4f69b029048958a1395cc98d285"></a>

```c
#define BT_SDP_ATTR_HID_PARSER_VERSION 0x0201
```

相关声明：[BT_SDP_ATTR_HID_PARSER_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga8bb0a4f69b029048958a1395cc98d285)。

人机接口设备解析器版本（HID Parser Version）。

<a id="r_ga43aa99ef47032c04be1bdee571dcfa5c"></a>

```c
#define BT_SDP_ATTR_HID_DEVICE_SUBCLASS 0x0202
```

相关声明：[BT_SDP_ATTR_HID_DEVICE_SUBCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga43aa99ef47032c04be1bdee571dcfa5c)。

人机接口设备子类（HID Device Subclass）。

<a id="r_ga5c06a7b07412b0a319656208700ac48e"></a>

```c
#define BT_SDP_ATTR_HID_COUNTRY_CODE 0x0203
```

相关声明：[BT_SDP_ATTR_HID_COUNTRY_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5c06a7b07412b0a319656208700ac48e)。

人机接口设备国家代码（HID Country Code）。

<a id="r_ga26ff5394958b41c5a595952992e0bbbe"></a>

```c
#define BT_SDP_ATTR_HID_VIRTUAL_CABLE 0x0204
```

相关声明：[BT_SDP_ATTR_HID_VIRTUAL_CABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga26ff5394958b41c5a595952992e0bbbe)。

人机接口设备虚拟线缆（HID Virtual Cable）。

<a id="r_ga30c601e79bd47f29bcc8325ac19a8391"></a>

```c
#define BT_SDP_ATTR_HID_RECONNECT_INITIATE 0x0205
```

相关声明：[BT_SDP_ATTR_HID_RECONNECT_INITIATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga30c601e79bd47f29bcc8325ac19a8391)。

人机接口设备主动重连（HID Reconnect Initiate）。

<a id="r_gaadf6a1c7740d5055e1877142b75d07c2"></a>

```c
#define BT_SDP_ATTR_HID_DESCRIPTOR_LIST 0x0206
```

相关声明：[BT_SDP_ATTR_HID_DESCRIPTOR_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaadf6a1c7740d5055e1877142b75d07c2)。

人机接口设备描述符列表（HID Descriptor List）。

<a id="r_ga732063505ff39f236b03646f8b7a78c6"></a>

```c
#define BT_SDP_ATTR_HID_LANG_ID_BASE_LIST 0x0207
```

相关声明：[BT_SDP_ATTR_HID_LANG_ID_BASE_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga732063505ff39f236b03646f8b7a78c6)。

人机接口设备语言 ID 基础列表（HID Language ID Base List）。

<a id="r_ga498779c65f410192862aa288cb1e277f"></a>

```c
#define BT_SDP_ATTR_HID_SDP_DISABLE 0x0208
```

相关声明：[BT_SDP_ATTR_HID_SDP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga498779c65f410192862aa288cb1e277f)。

人机接口设备 SDP 禁用（HID SDP Disable）。

<a id="r_gac92ef24a03422abdc6ca932e0675aa57"></a>

```c
#define BT_SDP_ATTR_HID_BATTERY_POWER 0x0209
```

相关声明：[BT_SDP_ATTR_HID_BATTERY_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac92ef24a03422abdc6ca932e0675aa57)。

人机接口设备电池供电（HID Battery Power）。

<a id="r_ga4bd0452184af1530887b0a785e30fca7"></a>

```c
#define BT_SDP_ATTR_HID_REMOTE_WAKEUP 0x020a
```

相关声明：[BT_SDP_ATTR_HID_REMOTE_WAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4bd0452184af1530887b0a785e30fca7)。

人机接口设备远程唤醒（HID Remote Wakeup）。

<a id="r_gaa792255345fe4f62062a848aebb220c7"></a>

```c
#define BT_SDP_ATTR_HID_PROFILE_VERSION 0x020b
```

相关声明：[BT_SDP_ATTR_HID_PROFILE_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa792255345fe4f62062a848aebb220c7)。

人机接口设备配置文件版本（HID Profile Version）。

<a id="r_ga1cd5f256115ef60736eb1089bf66988c"></a>

```c
#define BT_SDP_ATTR_HID_SUPERVISION_TIMEOUT 0x020c
```

相关声明：[BT_SDP_ATTR_HID_SUPERVISION_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1cd5f256115ef60736eb1089bf66988c)。

人机接口设备监视超时（HID Supervision Timeout）。

<a id="r_ga866194b8e0ec3eebe086998ae0c6e2ab"></a>

```c
#define BT_SDP_ATTR_HID_NORMALLY_CONNECTABLE 0x020d
```

相关声明：[BT_SDP_ATTR_HID_NORMALLY_CONNECTABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga866194b8e0ec3eebe086998ae0c6e2ab)。

人机接口设备正常可连接状态（HID Normally Connectable）。

<a id="r_ga511980e049b047618f97ac38a4ea3f4e"></a>

```c
#define BT_SDP_ATTR_HID_BOOT_DEVICE 0x020e
```

相关声明：[BT_SDP_ATTR_HID_BOOT_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga511980e049b047618f97ac38a4ea3f4e)。

人机接口设备引导设备（HID Boot Device）。

<a id="r_gaee523f64ffc9ecdd78bd0482df277e36"></a>

```c
#define BT_SDP_ATTR_HID_SSR_HOST_MAX_LATENCY 0x020f
```

相关声明：[BT_SDP_ATTR_HID_SSR_HOST_MAX_LATENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaee523f64ffc9ecdd78bd0482df277e36)。

人机接口设备 SSR 主机最大延迟（HID SSR Host Max Latency）。

<a id="r_ga94f31ceeb80af508a03380c2fe03ace7"></a>

```c
#define BT_SDP_ATTR_HID_SSR_HOST_MIN_TIMEOUT 0x0210
```

相关声明：[BT_SDP_ATTR_HID_SSR_HOST_MIN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga94f31ceeb80af508a03380c2fe03ace7)。

人机接口设备 SSR 主机最小超时（HID SSR Host Min Timeout）。

<a id="define-members-2"></a>

### 协议标识符编码（Protocol identifier codes）

蓝牙服务发现协议（SDP）使用的协议标识符（Protocol Identifiers）。

注意：基于蓝牙分配编号规范（Bluetooth Assigned Numbers Specification）。

`protocol-id` 的可能值列在下方。详情参见分配编号规范（Assigned Numbers Specification）中的“协议标识符（Protocol Identifiers）”一节。

<a id="r_gaa5ae0cf1cd2933005ae70709bea76407"></a>

```c
#define BT_SDP_PROTO_SDP 0x0001
```

相关声明：[BT_SDP_PROTO_SDP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa5ae0cf1cd2933005ae70709bea76407)。

服务发现协议（Service Discovery Protocol）。

<a id="r_gace719188083da9941dcfa76176cdc98c"></a>

```c
#define BT_SDP_PROTO_UDP 0x0002
```

相关声明：[BT_SDP_PROTO_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gace719188083da9941dcfa76176cdc98c)。

用户数据报协议（User Datagram Protocol）。

<a id="r_ga17056b75f2596fe115d18e42e7f3285e"></a>

```c
#define BT_SDP_PROTO_RFCOMM 0x0003
```

相关声明：[BT_SDP_PROTO_RFCOMM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga17056b75f2596fe115d18e42e7f3285e)。

射频通信（Radio Frequency Communication）。

<a id="r_ga7934d7ed5ec1d7a78f9ea17e2c354af9"></a>

```c
#define BT_SDP_PROTO_TCP 0x0004
```

相关声明：[BT_SDP_PROTO_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga7934d7ed5ec1d7a78f9ea17e2c354af9)。

传输控制协议（Transmission Control Protocol）。

<a id="r_ga75468f9c406f9940f4d2b0d2d56a9762"></a>

```c
#define BT_SDP_PROTO_TCS_BIN 0x0005
```

相关声明：[BT_SDP_PROTO_TCS_BIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga75468f9c406f9940f4d2b0d2d56a9762)。

电话控制规范二进制协议（Telephony Control Specification Binary）。

<a id="r_ga426cddacc8f6a9e8c502d001d48ecc2f"></a>

```c
#define BT_SDP_PROTO_TCS_AT 0x0006
```

相关声明：[BT_SDP_PROTO_TCS_AT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga426cddacc8f6a9e8c502d001d48ecc2f)。

电话控制规范 AT 协议（Telephony Control Specification AT）。

<a id="r_ga772d50f5ea6dbf93bb648e84b8b2ea25"></a>

```c
#define BT_SDP_PROTO_ATT 0x0007
```

相关声明：[BT_SDP_PROTO_ATT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga772d50f5ea6dbf93bb648e84b8b2ea25)。

属性协议（Attribute Protocol）。

<a id="r_gab16c910f700b7341742f4d7eedc9d32e"></a>

```c
#define BT_SDP_PROTO_OBEX 0x0008
```

相关声明：[BT_SDP_PROTO_OBEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab16c910f700b7341742f4d7eedc9d32e)。

对象交换协议（Object Exchange Protocol）。

<a id="r_gab6db981f154c92d17a51b7144f1afebe"></a>

```c
#define BT_SDP_PROTO_IP 0x0009
```

相关声明：[BT_SDP_PROTO_IP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab6db981f154c92d17a51b7144f1afebe)。

互联网协议（Internet Protocol）。

<a id="r_ga51c5e425f9fc9c785b75c03d2517a2c3"></a>

```c
#define BT_SDP_PROTO_FTP 0x000a
```

相关声明：[BT_SDP_PROTO_FTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga51c5e425f9fc9c785b75c03d2517a2c3)。

文件传输协议（File Transfer Protocol）。

<a id="r_ga103e4968d26d94d56a56a6e4d02b7a9a"></a>

```c
#define BT_SDP_PROTO_HTTP 0x000c
```

相关声明：[BT_SDP_PROTO_HTTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga103e4968d26d94d56a56a6e4d02b7a9a)。

超文本传输协议（HyperText Transfer Protocol）。

<a id="r_ga40525df1204b9e7a3106994eb8b7046e"></a>

```c
#define BT_SDP_PROTO_WSP 0x000e
```

相关声明：[BT_SDP_PROTO_WSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga40525df1204b9e7a3106994eb8b7046e)。

无线会话协议（Wireless Session Protocol）。

<a id="r_ga29032e4ab9a24056a6088ac377444285"></a>

```c
#define BT_SDP_PROTO_BNEP 0x000f
```

相关声明：[BT_SDP_PROTO_BNEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga29032e4ab9a24056a6088ac377444285)。

蓝牙网络封装协议（Bluetooth Network Encapsulation Protocol）。

<a id="r_ga368af07bb117929235af5c0e7b9729f0"></a>

```c
#define BT_SDP_PROTO_UPNP 0x0010
```

相关声明：[BT_SDP_PROTO_UPNP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga368af07bb117929235af5c0e7b9729f0)。

通用即插即用（Universal Plug and Play）。

<a id="r_gacb8a22ed2d0045e66d9208b408a6228b"></a>

```c
#define BT_SDP_PROTO_HID 0x0011
```

相关声明：[BT_SDP_PROTO_HID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gacb8a22ed2d0045e66d9208b408a6228b)。

人机接口设备协议（Human Interface Device Protocol）。

<a id="r_ga9f1bdf155d4f0be01172f971bac67154"></a>

```c
#define BT_SDP_PROTO_HARDCOPY_CTRL 0x0012
```

相关声明：[BT_SDP_PROTO_HARDCOPY_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9f1bdf155d4f0be01172f971bac67154)。

硬拷贝控制通道（Hardcopy Control Channel）。

<a id="r_ga5095801fa0d28056017725860dc75a93"></a>

```c
#define BT_SDP_PROTO_HARDCOPY_DATA 0x0014
```

相关声明：[BT_SDP_PROTO_HARDCOPY_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5095801fa0d28056017725860dc75a93)。

硬拷贝数据通道（Hardcopy Data Channel）。

<a id="r_gaf17681a3af315b0edaa9c82dd3a7fb89"></a>

```c
#define BT_SDP_PROTO_HARDCOPY_NTF 0x0016
```

相关声明：[BT_SDP_PROTO_HARDCOPY_NTF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf17681a3af315b0edaa9c82dd3a7fb89)。

硬拷贝通知通道（Hardcopy Notification Channel）。

<a id="r_ga4fabbc2e0b5d83cc84c7db7b1a3640b7"></a>

```c
#define BT_SDP_PROTO_AVCTP 0x0017
```

相关声明：[BT_SDP_PROTO_AVCTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4fabbc2e0b5d83cc84c7db7b1a3640b7)。

音视频控制传输协议（Audio/Video Control Transport Protocol）。

<a id="r_gaa308561679578a5e1d013301b7792eb6"></a>

```c
#define BT_SDP_PROTO_AVDTP 0x0019
```

相关声明：[BT_SDP_PROTO_AVDTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa308561679578a5e1d013301b7792eb6)。

音视频分发传输协议（Audio/Video Distribution Transport Protocol）。

<a id="r_ga127e2b367475cc074268ad88eb648c63"></a>

```c
#define BT_SDP_PROTO_CMTP 0x001b
```

相关声明：[BT_SDP_PROTO_CMTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga127e2b367475cc074268ad88eb648c63)。

通用 ISDN 访问协议（Common ISDN Access Protocol）。

<a id="r_ga6c6e5cbaea972e982ea608705d2a06cc"></a>

```c
#define BT_SDP_PROTO_MCAP_CTRL 0x001e
```

相关声明：[BT_SDP_PROTO_MCAP_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga6c6e5cbaea972e982ea608705d2a06cc)。

多通道适配协议控制通道（Multi-Channel Adaptation Protocol Control）。

<a id="r_ga19c4608fe6f63fb553706b176ee56a9b"></a>

```c
#define BT_SDP_PROTO_MCAP_DATA 0x001f
```

相关声明：[BT_SDP_PROTO_MCAP_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga19c4608fe6f63fb553706b176ee56a9b)。

多通道适配协议数据通道（Multi-Channel Adaptation Protocol Data）。

<a id="r_gac055f0beba2c311e9f098217fc721a75"></a>

```c
#define BT_SDP_PROTO_L2CAP 0x0100
```

相关声明：[BT_SDP_PROTO_L2CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac055f0beba2c311e9f098217fc721a75)。

逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol）。

<a id="define-members-3"></a>

### SDP 协议数据单元中的数据表示（蓝牙 SDP 规范第 339、340 页）（The Data representation in SDP PDUs (pps 339, 340 of BT SDP Spec)）

这些值就是写入协议数据单元（PDU）缓冲区的数据类型与大小描述符（Data Type + Size Descriptor）的精确编码值。

数据类型占前 5 位，大小描述符（Size Descriptor）占后 3 位，总计 8 位。大小描述符至关重要，它决定从 PDU 中为数据值提取多少字节。

对于大多数基本类型，数据类型与大小描述符（Data Type + Size Descriptor）的组合很直接；但对于构造类型（Constructed Types）和字符串，数据大小存放在该 8 位描述符之后的下 `n` 个字节中。`n` 的确切值由数据大小描述符的 3 位指定。

文本字符串（TextString）和 URL 字符串（URLString）的大小可为 `2^{8, 16, 32}` 字节；数据序列（DataSequence）和数据序列备选项（DataSequenceAlternates）的大小也可为 `2^{8, 16, 32}`。这些大小在 API 中事后计算，事先并不知道。译注：幂次表达式沿用官方原文；前文的 8／16／32 位指长度字段的宽度。

对于 `BT_SDP_UINT128`、`BT_SDP_INT128` 和 `BT_SDP_UUID128` 类型，数据字节序应为小端（Little-endian）。例如，串口配置文件（SPP）的 UUID128 `00001101-0000-1000-8000-00805F9B34FB` 表示为 `{0xFB, 0x34, 0x9B, 0x5F, 0x80, 0x00, 0x00, 0x80, 0x00, 0x10, 0x00, 0x00, 0x01, 0x11, 0x00, 0x00}`。128 位 UUID 的数组使用 `BT_SDP_ARRAY_UUID_128` 声明。

<a id="r_ga36f257de103356c3ebeb55e23186ed99"></a>

```c
#define BT_SDP_DATA_NIL 0x00
```

相关声明：[BT_SDP_DATA_NIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga36f257de103356c3ebeb55e23186ed99)。

Nil，空类型（Nil, the null type）。

<a id="r_ga546a46c2aa7eb3306eb46768fb8737a4"></a>

```c
#define BT_SDP_UINT8 0x08
```

相关声明：[BT_SDP_UINT8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga546a46c2aa7eb3306eb46768fb8737a4)。

无符号 8 位整数（Unsigned 8-bit integer）。

<a id="r_ga1129f3a1364f29c9ce36f6f74ca21327"></a>

```c
#define BT_SDP_UINT16 0x09
```

相关声明：[BT_SDP_UINT16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1129f3a1364f29c9ce36f6f74ca21327)。

无符号 16 位整数（Unsigned 16-bit integer）。

<a id="r_ga4f3bcb36dfce975c2d9ab68894a9e49c"></a>

```c
#define BT_SDP_UINT32 0x0a
```

相关声明：[BT_SDP_UINT32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4f3bcb36dfce975c2d9ab68894a9e49c)。

无符号 32 位整数（Unsigned 32-bit integer）。

<a id="r_ga11261bf1c63a6d463ed41225c1e1a0c7"></a>

```c
#define BT_SDP_UINT64 0x0b
```

相关声明：[BT_SDP_UINT64](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga11261bf1c63a6d463ed41225c1e1a0c7)。

无符号 64 位整数（Unsigned 64-bit integer）。

<a id="r_ga9a815c6efe976f29e9f6f35a566245fd"></a>

```c
#define BT_SDP_UINT128 0x0c
```

相关声明：[BT_SDP_UINT128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9a815c6efe976f29e9f6f35a566245fd)。

无符号 128 位整数（Unsigned 128-bit integer）。

<a id="r_gaeed1818ca1bf762b23ab2bfcd18b8a66"></a>

```c
#define BT_SDP_INT8 0x10
```

相关声明：[BT_SDP_INT8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaeed1818ca1bf762b23ab2bfcd18b8a66)。

有符号 8 位整数（Signed 8-bit integer）。

<a id="r_gaf6a3795d22cff4a522a2225339fb5a57"></a>

```c
#define BT_SDP_INT16 0x11
```

相关声明：[BT_SDP_INT16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf6a3795d22cff4a522a2225339fb5a57)。

有符号 16 位整数（Signed 16-bit integer）。

<a id="r_ga0ad987ebeac3dab3ef2196f4dfeca1ab"></a>

```c
#define BT_SDP_INT32 0x12
```

相关声明：[BT_SDP_INT32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga0ad987ebeac3dab3ef2196f4dfeca1ab)。

有符号 32 位整数（Signed 32-bit integer）。

<a id="r_gaae793fef5690c6013e6e0e34ededb75f"></a>

```c
#define BT_SDP_INT64 0x13
```

相关声明：[BT_SDP_INT64](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaae793fef5690c6013e6e0e34ededb75f)。

有符号 64 位整数（Signed 64-bit integer）。

<a id="r_gaf754bbfd9cdc0e6a2bf7d6c46fab3f29"></a>

```c
#define BT_SDP_INT128 0x14
```

相关声明：[BT_SDP_INT128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf754bbfd9cdc0e6a2bf7d6c46fab3f29)。

有符号 128 位整数（Signed 128-bit integer）。

<a id="r_ga4f829572cca9669a8a96a857874bb022"></a>

```c
#define BT_SDP_UUID_UNSPEC 0x18
```

相关声明：[BT_SDP_UUID_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4f829572cca9669a8a96a857874bb022)。

通用唯一标识符，未指定大小（UUID, unspecified size）。

<a id="r_ga45598f1c663acd3a3e5a409696cb3d2f"></a>

```c
#define BT_SDP_UUID16 0x19
```

相关声明：[BT_SDP_UUID16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga45598f1c663acd3a3e5a409696cb3d2f)。

通用唯一标识符，16 位（UUID, 16-bit）。

<a id="r_ga78245bb059feb3ec039e05aba24746e7"></a>

```c
#define BT_SDP_UUID32 0x1a
```

相关声明：[BT_SDP_UUID32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga78245bb059feb3ec039e05aba24746e7)。

通用唯一标识符，32 位（UUID, 32-bit）。

<a id="r_gaadf48ba3e96687fff99ff58789d79a50"></a>

```c
#define BT_SDP_UUID128 0x1c
```

相关声明：[BT_SDP_UUID128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaadf48ba3e96687fff99ff58789d79a50)。

通用唯一标识符，128 位（UUID, 128-bit）。

<a id="r_gaca9942a42701cda835a5bf7b7aaf1d75"></a>

```c
#define BT_SDP_TEXT_STR_UNSPEC 0x20
```

相关声明：[BT_SDP_TEXT_STR_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaca9942a42701cda835a5bf7b7aaf1d75)。

文本字符串，未指定大小（Text string, unspecified size）。

<a id="r_ga885ace6b1def91f3fa4dd16cb391d2b8"></a>

```c
#define BT_SDP_TEXT_STR8 0x25
```

相关声明：[BT_SDP_TEXT_STR8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga885ace6b1def91f3fa4dd16cb391d2b8)。

文本字符串，长度字段为 8 位（Text string, 8-bit length）。

<a id="r_gaa5301cdac5fc9299837f29b92aa3c10b"></a>

```c
#define BT_SDP_TEXT_STR16 0x26
```

相关声明：[BT_SDP_TEXT_STR16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa5301cdac5fc9299837f29b92aa3c10b)。

文本字符串，长度字段为 16 位（Text string, 16-bit length）。

<a id="r_ga29657a21117a3fbe05942778a8d7637e"></a>

```c
#define BT_SDP_TEXT_STR32 0x27
```

相关声明：[BT_SDP_TEXT_STR32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga29657a21117a3fbe05942778a8d7637e)。

文本字符串，长度字段为 32 位（Text string, 32-bit length）。

<a id="r_gac48f198f6609fac95db69c09ac69efab"></a>

```c
#define BT_SDP_BOOL 0x28
```

相关声明：[BT_SDP_BOOL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac48f198f6609fac95db69c09ac69efab)。

布尔值（Boolean）。

<a id="r_gaa884191d772bfa24484cb33c0f614334"></a>

```c
#define BT_SDP_SEQ_UNSPEC 0x30
```

相关声明：[BT_SDP_SEQ_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa884191d772bfa24484cb33c0f614334)。

数据元素序列，未指定大小（Data element sequence, unspecified size）。

<a id="r_ga5a64e3bec70b40114a3160dbfb1e484b"></a>

```c
#define BT_SDP_SEQ8 0x35
```

相关声明：[BT_SDP_SEQ8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5a64e3bec70b40114a3160dbfb1e484b)。

数据元素序列，长度字段为 8 位（Data element sequence, 8-bit length）。

<a id="r_gadf5b15a0296a872ffefc24bbc90dc45b"></a>

```c
#define BT_SDP_SEQ16 0x36
```

相关声明：[BT_SDP_SEQ16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gadf5b15a0296a872ffefc24bbc90dc45b)。

数据元素序列，长度字段为 16 位（Data element sequence, 16-bit length）。

<a id="r_ga639e86b5103168917cb7202100e3124d"></a>

```c
#define BT_SDP_SEQ32 0x37
```

相关声明：[BT_SDP_SEQ32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga639e86b5103168917cb7202100e3124d)。

数据元素序列，长度字段为 32 位（Data element sequence, 32-bit length）。

<a id="r_gaee1bd735929cb2c4bca48cc7663407fd"></a>

```c
#define BT_SDP_ALT_UNSPEC 0x38
```

相关声明：[BT_SDP_ALT_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaee1bd735929cb2c4bca48cc7663407fd)。

数据元素备选项，未指定大小（Data element alternative, unspecified size）。

<a id="r_gab7460f41f05a418d58f4b6807d84cb40"></a>

```c
#define BT_SDP_ALT8 0x3d
```

相关声明：[BT_SDP_ALT8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab7460f41f05a418d58f4b6807d84cb40)。

数据元素备选项，长度字段为 8 位（Data element alternative, 8-bit length）。

<a id="r_gab976bc87f0dcba0e4bc61575ea04ccc7"></a>

```c
#define BT_SDP_ALT16 0x3e
```

相关声明：[BT_SDP_ALT16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab976bc87f0dcba0e4bc61575ea04ccc7)。

数据元素备选项，长度字段为 16 位（Data element alternative, 16-bit length）。

<a id="r_ga420936f672ae31ca701ae277b69d592a"></a>

```c
#define BT_SDP_ALT32 0x3f
```

相关声明：[BT_SDP_ALT32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga420936f672ae31ca701ae277b69d592a)。

数据元素备选项，长度字段为 32 位（Data element alternative, 32-bit length）。

<a id="r_ga32a7a79422f52b75c2eb2d2eb467dc00"></a>

```c
#define BT_SDP_URL_STR_UNSPEC 0x40
```

相关声明：[BT_SDP_URL_STR_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga32a7a79422f52b75c2eb2d2eb467dc00)。

URL 字符串，未指定大小（URL string, unspecified size）。

<a id="r_gafb2a77d6097c8c4cf9f01b7e16df26f1"></a>

```c
#define BT_SDP_URL_STR8 0x45
```

相关声明：[BT_SDP_URL_STR8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gafb2a77d6097c8c4cf9f01b7e16df26f1)。

URL 字符串，长度字段为 8 位（URL string, 8-bit length）。

<a id="r_gac1acc712468e5af1f54022ac3551882a"></a>

```c
#define BT_SDP_URL_STR16 0x46
```

相关声明：[BT_SDP_URL_STR16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac1acc712468e5af1f54022ac3551882a)。

URL 字符串，长度字段为 16 位（URL string, 16-bit length）。

<a id="r_ga37476681e9d4eee53b710c44e2da9a2f"></a>

```c
#define BT_SDP_URL_STR32 0x47
```

相关声明：[BT_SDP_URL_STR32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga37476681e9d4eee53b710c44e2da9a2f)。

URL 字符串，长度字段为 32 位（URL string, 32-bit length）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_gad672a89277b276d1b702fe07302c468e"></a>

```c
typedef uint8_t(* bt_sdp_discover_func_t) (struct bt_conn *conn, struct bt_sdp_client_result *result, const struct bt_sdp_discover_params *params)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_sdp_discover_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad672a89277b276d1b702fe07302c468e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_sdp_client_result](../bluetooth_service_model_reference/P168_bt_sdp_client_result_结构体.md)、[bt_sdp_discover_params](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md)。

回调类型，用于通知用户：已在远端解析出给定 UUID 的结果，用户可使用结果记录缓冲区（Result Record Buffer）进一步检查。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.4\_枚举（Enumerations）

<a id="r_ga278df12ff5def68ca4663defd178582c"></a>

```c
enum { BT_SDP_DISCOVER_UUID_STOP = 0 , BT_SDP_DISCOVER_UUID_CONTINUE }
```

相关声明：[BT_SDP_DISCOVER_UUID_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga278df12ff5def68ca4663defd178582ca990fbea48866b2acb7ccd67391b19636)、[BT_SDP_DISCOVER_UUID_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga278df12ff5def68ca4663defd178582ca94e15ea86b69d65ca9c1947d1e2157ef)。

用作 `bt_sdp_discover_func_t` 返回值的辅助枚举（Helper Enum）。

<a id="r_ga88019838cb3e5317fce93f4933583d94"></a>

```c
enum { BT_SDP_DISCOVER_SERVICE_SEARCH , BT_SDP_DISCOVER_SERVICE_ATTR , BT_SDP_DISCOVER_SERVICE_SEARCH_ATTR }
```

相关声明：[BT_SDP_DISCOVER_SERVICE_SEARCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga88019838cb3e5317fce93f4933583d94a9ce8c93cf1754fc7047951e891f66ff2)、[BT_SDP_DISCOVER_SERVICE_ATTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga88019838cb3e5317fce93f4933583d94a5b8c3260e5aaaa08e86a099ccfeee41f)、[BT_SDP_DISCOVER_SERVICE_SEARCH_ATTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga88019838cb3e5317fce93f4933583d94a64fff103816cfc0215b9b3909786fa4e)。

SDP 发现类型（Discover Types）。

<a id="r_ga5e4a45b7b860d82a111480c9f25c2666"></a>

```c
enum bt_sdp_attr_value_type { BT_SDP_ATTR_VALUE_TYPE_NONE = 0 , BT_SDP_ATTR_VALUE_TYPE_UINT , BT_SDP_ATTR_VALUE_TYPE_SINT , BT_SDP_ATTR_VALUE_TYPE_BOOL , BT_SDP_ATTR_VALUE_TYPE_TEXT , BT_SDP_ATTR_VALUE_TYPE_URL }
```

相关声明：[bt_sdp_attr_value_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5e4a45b7b860d82a111480c9f25c2666)、[BT_SDP_ATTR_VALUE_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666acaf932b38a1e17ca9e85c055096fa1da)、[BT_SDP_ATTR_VALUE_TYPE_UINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a5af87613192cda6a05fa280d2df8574b)、[BT_SDP_ATTR_VALUE_TYPE_SINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a5917deef84a7af5d5f908d4058732b1e)、[BT_SDP_ATTR_VALUE_TYPE_BOOL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a154bbb29fb26d007838c87def4cd34f8)、[BT_SDP_ATTR_VALUE_TYPE_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a80b8652e39dae70c61443adf4f29fb4d)、[BT_SDP_ATTR_VALUE_TYPE_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a27eccef21d812956c6ae7ff9194e20e4)。

SDP 属性值类型枚举（Attribute Value Type Enumeration）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.5\_函数（Functions）

<a id="r_ga6006e3cd593ef793273fb291913790fa"></a>

```c
int bt_sdp_register_service (struct bt_sdp_record *service)
```

相关声明：[bt_sdp_register_service](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga6006e3cd593ef793273fb291913790fa)、[bt_sdp_record](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md)。

注册服务记录（Service Record）。

<a id="r_ga71e7d75850becf4ead62668c8e7bebbc"></a>

```c
int bt_sdp_unregister_service (struct bt_sdp_record *service)
```

相关声明：[bt_sdp_unregister_service](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga71e7d75850becf4ead62668c8e7bebbc)、[bt_sdp_record](../bluetooth_service_model_reference/P171_bt_sdp_record_结构体.md)。

注销服务记录（Service Record）。

<a id="r_ga44658df825a40f820a31e7adb4240d25"></a>

```c
int bt_sdp_discover (struct bt_conn *conn, struct bt_sdp_discover_params *params)
```

相关声明：[bt_sdp_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga44658df825a40f820a31e7adb4240d25)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_sdp_discover_params](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md)。

允许用户启动 SDP 发现会话（Discovery Session）。

<a id="r_ga2eb0646597a44e0e3cb0234d2c12a2d7"></a>

```c
int bt_sdp_discover_cancel (struct bt_conn *conn, struct bt_sdp_discover_params *params)
```

相关声明：[bt_sdp_discover_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2eb0646597a44e0e3cb0234d2c12a2d7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_sdp_discover_params](../bluetooth_service_model_reference/P170_bt_sdp_discover_params_结构体.md)。

释放等待中的 SDP 发现请求（Discovery Request）。

<a id="r_gaf69723cff6dce7e86f0f0240ec3e2041"></a>

```c
int bt_sdp_get_proto_param (const struct net_buf *buf, uint16_t proto, uint16_t *param)
```

相关声明：[bt_sdp_get_proto_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf69723cff6dce7e86f0f0240ec3e2041)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向用户提供与给定协议栈层协议 UUID（Stacked Protocol UUID）相关的参数值。

<a id="r_gaba31a2327e4bba56ef2ac831b166e66a"></a>

```c
int bt_sdp_get_addl_proto_param (const struct net_buf *buf, uint16_t proto, uint8_t index, uint16_t *param)
```

相关声明：[bt_sdp_get_addl_proto_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaba31a2327e4bba56ef2ac831b166e66a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取与给定协议栈层协议 UUID（Stacked Protocol UUID）相关的附加参数值。

<a id="r_ga9e7d4bd0a407fe8254410f907db90f00"></a>

```c
int bt_sdp_get_profile_version (const struct net_buf *buf, uint16_t profile, uint16_t *version)
```

相关声明：[bt_sdp_get_profile_version](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9e7d4bd0a407fe8254410f907db90f00)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取配置文件版本（Profile Version）。

<a id="r_gae1c3110dfe24a939cc02d998c4699ca7"></a>

```c
int bt_sdp_get_features (const struct net_buf *buf, uint16_t *features)
```

相关声明：[bt_sdp_get_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gae1c3110dfe24a939cc02d998c4699ca7)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取支持特性（SupportedFeatures）属性值。

<a id="r_gaed089d52f57cb25d2b02b2adbc60a36a"></a>

```c
int bt_sdp_get_vendor_id (const struct net_buf *buf, uint16_t *vendor_id)
```

相关声明：[bt_sdp_get_vendor_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaed089d52f57cb25d2b02b2adbc60a36a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取厂商 ID（Vendor ID）。

<a id="r_ga71809908bb73150258b2a5ab3c2f8517"></a>

```c
int bt_sdp_get_product_id (const struct net_buf *buf, uint16_t *product_id)
```

相关声明：[bt_sdp_get_product_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga71809908bb73150258b2a5ab3c2f8517)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取产品 ID（Product ID）。

<a id="r_ga0ce1314e052881eec5a43f571857960e"></a>

```c
int bt_sdp_record_parse (const struct net_buf *buf, bool(*func)(const struct bt_sdp_attribute *attr, void *user_data), void *user_data)
```

相关声明：[bt_sdp_record_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga0ce1314e052881eec5a43f571857960e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)。

遍历发现的 SDP 记录（Record）。

<a id="r_ga2cb42ca8e487071682c37124ab56f2ab"></a>

```c
bool bt_sdp_has_attr (const struct net_buf *buf, uint16_t attr_id)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_sdp_has_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2cb42ca8e487071682c37124ab56f2ab)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查是否找到指定属性标识符（Attribute Identifier）。

<a id="r_ga9df34b18af051782377229a18e6d3887"></a>

```c
int bt_sdp_get_attr (const struct net_buf *buf, uint16_t attr_id, struct bt_sdp_attribute *attr)
```

相关声明：[bt_sdp_get_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9df34b18af051782377229a18e6d3887)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)。

按 ID 从 SDP 记录获取指定属性（Attribute）。

<a id="r_gab7d3e8bc83efff28cf9118710b5486fc"></a>

```c
int bt_sdp_attr_value_parse (const struct bt_sdp_attribute *attr, bool(*func)(const struct bt_sdp_attr_value_pair *value, void *user_data), void *user_data)
```

相关声明：[bt_sdp_attr_value_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab7d3e8bc83efff28cf9118710b5486fc)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_sdp_attr_value_pair](../bluetooth_service_model_reference/P161_bt_sdp_attr_value_pair_结构体.md)。

解析 SDP 属性值（Attribute Values）。

<a id="r_ga07ca5d4f383d74004478cfd6ead2b80a"></a>

```c
bool bt_sdp_attr_has_uuid (const struct bt_sdp_attribute *attr, const struct bt_uuid *uuid)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_sdp_attr_has_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga07ca5d4f383d74004478cfd6ead2b80a)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)。

检查 SDP 属性是否包含指定 UUID。

<a id="r_ga3bad45ab578c0277a320ac241692f799"></a>

```c
int bt_sdp_attr_read (const struct bt_sdp_attribute *attr, const struct bt_uuid *uuid, struct bt_sdp_attr_value *value)
```

相关声明：[bt_sdp_attr_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3bad45ab578c0277a320ac241692f799)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_sdp_attr_value](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md)。

读取指定 UUID 对应的 SDP 属性值（Attribute Value）。

<a id="r_gac395eff18a4d2af3d955e276bf13963a"></a>

```c
int bt_sdp_attr_addl_proto_parse (const struct bt_sdp_attribute *attr, bool(*func)(const struct bt_sdp_attribute *attr, void *user_data), void *user_data)
```

相关声明：[bt_sdp_attr_addl_proto_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac395eff18a4d2af3d955e276bf13963a)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)。

解析附加协议描述符列表属性（Additional Protocol Descriptor List Attribute）。

<a id="r_gaa104046a9e6e15f05961bf8652ecec16"></a>

```c
ssize_t bt_sdp_attr_addl_proto_count (const struct bt_sdp_attribute *attr)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_sdp_attr_addl_proto_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa104046a9e6e15f05961bf8652ecec16)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)。

获取附加协议描述符列表（Additional Protocol Descriptor List）中的协议描述符数量。

<a id="r_gacf20a00d84e6eed2c128284fe9c52024"></a>

```c
int bt_sdp_attr_addl_proto_read (const struct bt_sdp_attribute *attr, uint16_t index, const struct bt_uuid *uuid, struct bt_sdp_attr_value *value)
```

相关声明：[bt_sdp_attr_addl_proto_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gacf20a00d84e6eed2c128284fe9c52024)、[bt_sdp_attribute](../bluetooth_service_model_reference/P165_bt_sdp_attribute_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_sdp_attr_value](../bluetooth_service_model_reference/P159_bt_sdp_attr_value_结构体.md)。

读取附加协议描述符列表（Additional Protocol Descriptor List）中指定索引和 UUID 对应的值。


## 5.6\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/bluetooth/uuid.h](../api_source_supplement_reference/P020_uuid.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [查看此文件的源码。](../api_source_architecture_reference/P019_sdp.h_源码浏览.md)
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
- [BT_SDP_SERVER_RECORD_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga610e7cab0a598f272eeb2838f4c4c996)
- [BT_SDP_PRIMARY_LANG_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab502c9288e5f01dfdaaf8390bb3f6e49)
- [BT_SDP_ATTR_SVCNAME_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga76737502226c623bf508ae53a6015e08)
- [BT_SDP_ATTR_SVCDESC_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3e991ec1d5467c0b3ce5d9a7e750a300)
- [BT_SDP_ATTR_PROVNAME_PRIMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab8b0110be857d6eca206e00c3b5e373a)
- [BT_SDP_TYPE_DESC_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3eb2a5501341f6c5186a27219cf27cdf)
- [BT_SDP_SIZE_DESC_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2d1040ccd11d1dd4c697525ebc323243)
- [BT_SDP_SIZE_INDEX_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga6e8f843aeb2d325058214d2a1454737a)
- [BT_SDP_ARRAY_8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaef264fa3621c3df7a164128bb95b30fc)
- [BT_SDP_ARRAY_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa4bb67164ae1f16b26081668d00f45c7)
- [BT_SDP_ARRAY_32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga7a17ee4872190a087cf2e5ea4db9e737)
- [BT_SDP_ARRAY_UUID_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gadbdfa913e11ed7b8e691a1fc1712e6eb)
- [BT_SDP_TYPE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga66778ac38fb5b82d3b514fe0da008393)
- [BT_SDP_TYPE_SIZE_VAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gabbb2bd6a8321513082851fe73dfa44bc)
- [BT_SDP_DATA_ELEM_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa2954f3df4d0ee9684721cbc6182e37c)
- [BT_SDP_NEW_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaee13722587e4eb8c4beaaa0abad88fe5)
- [BT_SDP_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga25b31454ee5b5fe23b617b5256ba00c4)
- [BT_SDP_SERVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa57f3c9a52ae29c02d7577be99f91e7c)
- [BT_SDP_SERVICE_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga83de8e62415d3e31b3b5434b9db633d0)
- [BT_SDP_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga096c84414b429aa05bed45cf6175361e)
- [BT_SDP_SUPPORTED_CAPABILITIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3a1feb6311af64292c1f22ff54e01876)
- [BT_SDP_SUPPORTED_FUNCTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga48eadaa621be7eaecbf5d2f8cc1354ab)
- [BT_SDP_RECORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga555f10b8f3ae3710c6dda9f37e78547b)
- [BT_SDP_ATTR_ID_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga920e61b784c4ae47bc51ac5c46273220)
- [BT_SDP_SDP_SERVER_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac2c2379f8e483939826297dc49657837)
- [BT_SDP_BROWSE_GRP_DESC_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gabe05780702a9be7da54a8c04f79ad752)
- [BT_SDP_PUBLIC_BROWSE_GROUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga383233a0ff3159ed653786490a4c06ae)
- [BT_SDP_SERIAL_PORT_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab1234d808a7e347328bf95ad065fd9c4)
- [BT_SDP_LAN_ACCESS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf0199837105ded0d65314e573da6a3ed)
- [BT_SDP_DIALUP_NET_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaab655c1f93029ed64743156734e2519e)
- [BT_SDP_IRMC_SYNC_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga28fc78fc21e4d88569e5ca5727ed6202)
- [BT_SDP_OBEX_OBJPUSH_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaaf64788e0cc6d54a8511c07af22f6740)
- [BT_SDP_OBEX_FILETRANS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gacd25278a573edcb16aa4b60f8ffad20d)
- [BT_SDP_IRMC_SYNC_CMD_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga39d4ce2465b10c10ee746c1491c49bea)
- [BT_SDP_HEADSET_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga6eb16aacf468b460fa7675ffc4703e68)
- [BT_SDP_CORDLESS_TELEPHONY_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga16e1bc10528ac82f6cec822912f97d8c)
- [BT_SDP_AUDIO_SOURCE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gafeb3a3184a0b83e0045187cbe3cf24dc)
- [BT_SDP_AUDIO_SINK_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa0e334873b5477523572caa2359a4098)
- [BT_SDP_AV_REMOTE_TARGET_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gafe96e9d32797a83c793f0ed278054b80)
- [BT_SDP_ADVANCED_AUDIO_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2fdc3eb32196b5135b7f595a36cacb4c)
- [BT_SDP_AV_REMOTE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaea94250bed4c5e6ad47749a1237778f5)
- [BT_SDP_AV_REMOTE_CONTROLLER_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaaae997769dfc8325c38830707f4d22e3)
- [BT_SDP_INTERCOM_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9681e34d78cea87e413fa4be40e4239a)
- [BT_SDP_FAX_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga31962fab5bed7c54311c4b291713a836)
- [BT_SDP_HEADSET_AGW_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4c9322cf28a8b1aa96828152e8ee7379)
- [BT_SDP_WAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2ab79d7ff4e88820773cf24f0b0b6e20)
- [BT_SDP_WAP_CLIENT_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga22624d29917aaeaa0c281d9517178821)
- [BT_SDP_PANU_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa9abb444e3b43c1164d6b450b1c066e5)
- [BT_SDP_NAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga78a7be1db8be8d7eece0d17c629dd009)
- [BT_SDP_GN_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaed2d6f72c344e2e9b9bdcefd23cb4086)
- [BT_SDP_DIRECT_PRINTING_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga30f6edbd67d96f7752a223409c8e4431)
- [BT_SDP_REFERENCE_PRINTING_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga6bc247854656613d2fa9b47d55bd69d6)
- [BT_SDP_IMAGING_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga08730b1fd7088101fadb85e5dc13fd24)
- [BT_SDP_IMAGING_RESPONDER_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf19cd136b780ef303c1290b26ab2ca17)
- [BT_SDP_IMAGING_ARCHIVE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3f04a28d9764a0c7755babe379c25393)
- [BT_SDP_IMAGING_REFOBJS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga51a4cfc28f86a650b03a7bbe6e5b883a)
- [BT_SDP_HANDSFREE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab9f99989420545b3b0e71da6c5475f90)
- [BT_SDP_HANDSFREE_AGW_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1c44ae236a292c91dc81539c9c89947c)
- [BT_SDP_DIRECT_PRT_REFOBJS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga79d34c3b7641cf523adf6515720ceceb)
- [BT_SDP_REFLECTED_UI_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga78607a42f5228b37d348614b12e48a77)
- [BT_SDP_BASIC_PRINTING_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac727f387a55a76c9a071cf62792f50e4)
- [BT_SDP_PRINTING_STATUS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9298ac73a26a1ab2e53733f404e5c6ea)
- [BT_SDP_HID_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab63eab5791898a47bd540eed4d55cddc)
- [BT_SDP_HCR_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga873f8e03aeb696d3eb287a8d00796a4f)
- [BT_SDP_HCR_PRINT_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4ca1e6eb6fe385e526f8d84ed65ab285)
- [BT_SDP_HCR_SCAN_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga621afe0f5a6d176c26e140c4162bee07)
- [BT_SDP_CIP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9617c02c6999d9fe987e91c6c2dc5dca)
- [BT_SDP_VIDEO_CONF_GW_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3e087c095a78f07efae660eceae9c11e)
- [BT_SDP_UDI_MT_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga629179357eff2cd60621f0e1e435df06)
- [BT_SDP_UDI_TA_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga846599abf75f1cbb27028aea8a619f31)
- [BT_SDP_AV_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab7a8499dbb73a2700389d55d331bd23e)
- [BT_SDP_SAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad2234f8e0bce0e6b55d18c7a7c950e1d)
- [BT_SDP_PBAP_PCE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaec2475b7ba36b860c0f8a9cfc33df4a8)
- [BT_SDP_PBAP_PSE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga612bb83e9f08edd163433a5fbe9528fc)
- [BT_SDP_PBAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga60a9fad26300c15e988e101f90c06435)
- [BT_SDP_MAP_MSE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga58f5cc54014e3723720e7c3b7ba82fd8)
- [BT_SDP_MAP_MCE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga47849c599678f7ec48c237b8b36e9cb7)
- [BT_SDP_MAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaec665050af4cc3affcef3912bb212fc0)
- [BT_SDP_GNSS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga300585062ed9ae05daca226cb3c5440d)
- [BT_SDP_GNSS_SERVER_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gacdfb8ca6a776f57a2df38b4a6eaa8403)
- [BT_SDP_MPS_SC_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9cce7e3a576329661b363b102cefa494)
- [BT_SDP_MPS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf847b2675482d3bb9674f569c3604e40)
- [BT_SDP_PNP_INFO_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaed5403661e0eb8f798a950bead59369a)
- [BT_SDP_GENERIC_NETWORKING_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1b9a169ff4db4fda939cba3ce21f808b)
- [BT_SDP_GENERIC_FILETRANS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa8e5c423fca1fb0d06504cdc5be276d1)
- [BT_SDP_GENERIC_AUDIO_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaec7548467ffb686b22a907d05e38f275)
- [BT_SDP_GENERIC_TELEPHONY_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga010b005cfdb69c67cfc7e3c5c8426778)
- [BT_SDP_UPNP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9e7fa3bcf139462a2c33f90b526e1ad1)
- [BT_SDP_UPNP_IP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga102b24708429877c4f37a5008fb176b1)
- [BT_SDP_UPNP_PAN_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3f50947a742b24089f86193e773d623b)
- [BT_SDP_UPNP_LAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad418094573383e6252719abed97d24dd)
- [BT_SDP_UPNP_L2CAP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad4d97c0b664c48bdc0842f92240409c7)
- [BT_SDP_VIDEO_SOURCE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga17d7fb3a77ef7266ea2d760fb3696a83)
- [BT_SDP_VIDEO_SINK_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1e3428b6d0197bd7c9d72154c025e9f5)
- [BT_SDP_VIDEO_DISTRIBUTION_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4e2ef8310c9396f9fb7781ab4732f308)
- [BT_SDP_HDP_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf8fc80f3b2ff245b7d354aa0488bb42b)
- [BT_SDP_HDP_SOURCE_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga87ba9fdf39fb99397a6dec4d92b6e3f1)
- [BT_SDP_HDP_SINK_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2125a92c6eb724a63d04188919a12bf1)
- [BT_SDP_GENERIC_ACCESS_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gae8010af5b12cd1c1b1633a4d2c9f5ab0)
- [BT_SDP_GENERIC_ATTRIB_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad3f345431526bb713921f4b51c48b056)
- [BT_SDP_APPLE_AGENT_SVCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga694b04c2dae3b06b7fd66640468a5a38)
- [BT_SDP_ATTR_RECORD_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga38f32cae462272b51eb4edca0c5c95a2)
- [BT_SDP_ATTR_SVCLASS_ID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab5c5be56c54d3f8bd4ac6defff0b1e7c)
- [BT_SDP_ATTR_RECORD_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4d458591f8eba26feaab1220c49f6a29)
- [BT_SDP_ATTR_SERVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad2149fd761f7ae2ea6ef761ab2545ab4)
- [BT_SDP_ATTR_PROTO_DESC_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3e7dad966deab42ff9fa0fd04d3d4514)
- [BT_SDP_ATTR_BROWSE_GRP_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2609212bf5400c31351bc3ec5f60a7e1)
- [BT_SDP_ATTR_LANG_BASE_ATTR_ID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga462ec997a81c6b439a24e2de085676ab)
- [BT_SDP_ATTR_SVCINFO_TTL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga7ef037ed6628aa7354736295e0e4ec77)
- [BT_SDP_ATTR_SERVICE_AVAILABILITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf55a72ce05def1da08d15a23cee4c5e3)
- [BT_SDP_ATTR_PROFILE_DESC_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga0b5b19caa523e4cb9da8a2bfc6eab20a)
- [BT_SDP_ATTR_DOC_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad8302739bca706f6da851d912ada0f82)
- [BT_SDP_ATTR_CLNT_EXEC_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga0bc613d68dace4cce7a4eec654f5a1e4)
- [BT_SDP_ATTR_ICON_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga365048bcb0ad2989aec9dd0d89abbfb9)
- [BT_SDP_ATTR_ADD_PROTO_DESC_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf7f0b2f30ede36cf280bf31c5e76a99c)
- [BT_SDP_ATTR_GROUP_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga15a104c78357f2353cd49eb858de057d)
- [BT_SDP_ATTR_IP_SUBNET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga23a63b424ab381048cb898ebbdb64a02)
- [BT_SDP_ATTR_VERSION_NUM_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab698c476197acca0d499e39f7f246c66)
- [BT_SDP_ATTR_SUPPORTED_FEATURES_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga8a693e5265c7801e3c1125473c31445f)
- [BT_SDP_ATTR_GOEP_L2CAP_PSM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac7583b3d2a0ebc82e5cf2e6705249201)
- [BT_SDP_ATTR_SVCDB_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab8fe8881b4470ab3522e710e36470ddb)
- [BT_SDP_ATTR_MPSD_SCENARIOS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga39b3436f9da303bd2ce1ad38f072ed9f)
- [BT_SDP_ATTR_MPMD_SCENARIOS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa3cc3d9a6ac7375e66b0892631698fd0)
- [BT_SDP_ATTR_MPS_DEPENDENCIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga45795e50564492ac9bce8d6832883741)
- [BT_SDP_ATTR_SERVICE_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga230f70b576c14ba1dbe0cf6eda6220e0)
- [BT_SDP_ATTR_EXTERNAL_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga617dc829eb1192cd283bef67a357d75f)
- [BT_SDP_ATTR_SUPPORTED_DATA_STORES_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gae12e2daea8febbbd047c1c3843f56933)
- [BT_SDP_ATTR_DATA_EXCHANGE_SPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4732f83c88de43a90ca3d58a136907b6)
- [BT_SDP_ATTR_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9c78d47f54e82a51f7d04a6f6c97663c)
- [BT_SDP_ATTR_FAX_CLASS1_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaeebfb4a085417db65241b21a27258d84)
- [BT_SDP_ATTR_REMOTE_AUDIO_VOLUME_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa122bfee476a8e83346823e23978f7a0)
- [BT_SDP_ATTR_MCAP_SUPPORTED_PROCEDURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga54e285c7a12becef9742093e1777c06b)
- [BT_SDP_ATTR_FAX_CLASS20_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga861470cd4b505d074abb727ba72c088a)
- [BT_SDP_ATTR_SUPPORTED_FORMATS_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac12ed37044c3f12c2d41b1fd23eacada)
- [BT_SDP_ATTR_FAX_CLASS2_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2475947ccdb9f30ece61a34959fd6ce2)
- [BT_SDP_ATTR_AUDIO_FEEDBACK_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac4906f9fa368fbf604830cd5c5fdcb57)
- [BT_SDP_ATTR_NETWORK_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga74dacfd7807d7f3ec7a7594a9329f0b2)
- [BT_SDP_ATTR_WAP_GATEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1ef964c955473601910ee3997b9ce5cd)
- [BT_SDP_ATTR_HOMEPAGE_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gafeff5e5b60bd47c44f8edbe8ff7e78a0)
- [BT_SDP_ATTR_WAP_STACK_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gae1a3ff84a5588e55258c35ee57d6a5b5)
- [BT_SDP_ATTR_SECURITY_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga21214c2236a5dca24a45998640761e7b)
- [BT_SDP_ATTR_NET_ACCESS_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga13851f9f9a5ba8514d20cffbe5eb9f14)
- [BT_SDP_ATTR_MAX_NET_ACCESSRATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga7347caab1c7e8755250567d9d8cc7266)
- [BT_SDP_ATTR_IP4_SUBNET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga01c0cdb8975484242e6c4b052dabfd91)
- [BT_SDP_ATTR_IP6_SUBNET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga10b3d4826904489d474af5e9c21c0831)
- [BT_SDP_ATTR_SUPPORTED_CAPABILITIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5347dbc038ac9c259d17c14ed9a812d3)
- [BT_SDP_ATTR_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga498d9beaa7877570fe834d854de36fcb)
- [BT_SDP_ATTR_SUPPORTED_FUNCTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gabc7cdfd247da5e2ecfd441c0436471f3)
- [BT_SDP_ATTR_TOTAL_IMAGING_DATA_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gadbce181b739c201070d6abcbdc4139f4)
- [BT_SDP_ATTR_SUPPORTED_REPOSITORIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gada3d989d6c8c0664ba0bf998414a0328)
- [BT_SDP_ATTR_MAS_INSTANCE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga03d653957d68b5d0eeda1fa7c9aa4587)
- [BT_SDP_ATTR_SUPPORTED_MESSAGE_TYPES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga41fc674e8571556397135734d28b829a)
- [BT_SDP_ATTR_PBAP_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa681b17ebfe013c196cf372dcd030c6e)
- [BT_SDP_ATTR_MAP_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa50f16945c15f7a954c10dbc8fc394bf)
- [BT_SDP_ATTR_SPECIFICATION_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4af959fbdfe7cee84008642091df948d)
- [BT_SDP_ATTR_VENDOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab5c2534491b43cfc9d2c7e8807b29ff2)
- [BT_SDP_ATTR_PRODUCT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaac9298efffbcf07303f972a12b50f4b6)
- [BT_SDP_ATTR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gae0f4af728f964ee1c11d86b785575a87)
- [BT_SDP_ATTR_PRIMARY_RECORD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga0868f7d90e3944f105028868511896cf)
- [BT_SDP_ATTR_VENDOR_ID_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad0ac4a65c51ccdf4cd128eb8697e56ca)
- [BT_SDP_ATTR_HID_DEVICE_RELEASE_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab33be247c7574e985dfb34e3c121dd23)
- [BT_SDP_ATTR_HID_PARSER_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga8bb0a4f69b029048958a1395cc98d285)
- [BT_SDP_ATTR_HID_DEVICE_SUBCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga43aa99ef47032c04be1bdee571dcfa5c)
- [BT_SDP_ATTR_HID_COUNTRY_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5c06a7b07412b0a319656208700ac48e)
- [BT_SDP_ATTR_HID_VIRTUAL_CABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga26ff5394958b41c5a595952992e0bbbe)
- [BT_SDP_ATTR_HID_RECONNECT_INITIATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga30c601e79bd47f29bcc8325ac19a8391)
- [BT_SDP_ATTR_HID_DESCRIPTOR_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaadf6a1c7740d5055e1877142b75d07c2)
- [BT_SDP_ATTR_HID_LANG_ID_BASE_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga732063505ff39f236b03646f8b7a78c6)
- [BT_SDP_ATTR_HID_SDP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga498779c65f410192862aa288cb1e277f)
- [BT_SDP_ATTR_HID_BATTERY_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac92ef24a03422abdc6ca932e0675aa57)
- [BT_SDP_ATTR_HID_REMOTE_WAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4bd0452184af1530887b0a785e30fca7)
- [BT_SDP_ATTR_HID_PROFILE_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa792255345fe4f62062a848aebb220c7)
- [BT_SDP_ATTR_HID_SUPERVISION_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1cd5f256115ef60736eb1089bf66988c)
- [BT_SDP_ATTR_HID_NORMALLY_CONNECTABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga866194b8e0ec3eebe086998ae0c6e2ab)
- [BT_SDP_ATTR_HID_BOOT_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga511980e049b047618f97ac38a4ea3f4e)
- [BT_SDP_ATTR_HID_SSR_HOST_MAX_LATENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaee523f64ffc9ecdd78bd0482df277e36)
- [BT_SDP_ATTR_HID_SSR_HOST_MIN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga94f31ceeb80af508a03380c2fe03ace7)
- [BT_SDP_PROTO_SDP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa5ae0cf1cd2933005ae70709bea76407)
- [BT_SDP_PROTO_UDP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gace719188083da9941dcfa76176cdc98c)
- [BT_SDP_PROTO_RFCOMM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga17056b75f2596fe115d18e42e7f3285e)
- [BT_SDP_PROTO_TCP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga7934d7ed5ec1d7a78f9ea17e2c354af9)
- [BT_SDP_PROTO_TCS_BIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga75468f9c406f9940f4d2b0d2d56a9762)
- [BT_SDP_PROTO_TCS_AT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga426cddacc8f6a9e8c502d001d48ecc2f)
- [BT_SDP_PROTO_ATT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga772d50f5ea6dbf93bb648e84b8b2ea25)
- [BT_SDP_PROTO_OBEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab16c910f700b7341742f4d7eedc9d32e)
- [BT_SDP_PROTO_IP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab6db981f154c92d17a51b7144f1afebe)
- [BT_SDP_PROTO_FTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga51c5e425f9fc9c785b75c03d2517a2c3)
- [BT_SDP_PROTO_HTTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga103e4968d26d94d56a56a6e4d02b7a9a)
- [BT_SDP_PROTO_WSP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga40525df1204b9e7a3106994eb8b7046e)
- [BT_SDP_PROTO_BNEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga29032e4ab9a24056a6088ac377444285)
- [BT_SDP_PROTO_UPNP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga368af07bb117929235af5c0e7b9729f0)
- [BT_SDP_PROTO_HID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gacb8a22ed2d0045e66d9208b408a6228b)
- [BT_SDP_PROTO_HARDCOPY_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9f1bdf155d4f0be01172f971bac67154)
- [BT_SDP_PROTO_HARDCOPY_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5095801fa0d28056017725860dc75a93)
- [BT_SDP_PROTO_HARDCOPY_NTF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf17681a3af315b0edaa9c82dd3a7fb89)
- [BT_SDP_PROTO_AVCTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4fabbc2e0b5d83cc84c7db7b1a3640b7)
- [BT_SDP_PROTO_AVDTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa308561679578a5e1d013301b7792eb6)
- [BT_SDP_PROTO_CMTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga127e2b367475cc074268ad88eb648c63)
- [BT_SDP_PROTO_MCAP_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga6c6e5cbaea972e982ea608705d2a06cc)
- [BT_SDP_PROTO_MCAP_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga19c4608fe6f63fb553706b176ee56a9b)
- [BT_SDP_PROTO_L2CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac055f0beba2c311e9f098217fc721a75)
- [BT_SDP_DATA_NIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga36f257de103356c3ebeb55e23186ed99)
- [BT_SDP_UINT8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga546a46c2aa7eb3306eb46768fb8737a4)
- [BT_SDP_UINT16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga1129f3a1364f29c9ce36f6f74ca21327)
- [BT_SDP_UINT32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4f3bcb36dfce975c2d9ab68894a9e49c)
- [BT_SDP_UINT64](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga11261bf1c63a6d463ed41225c1e1a0c7)
- [BT_SDP_UINT128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9a815c6efe976f29e9f6f35a566245fd)
- [BT_SDP_INT8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaeed1818ca1bf762b23ab2bfcd18b8a66)
- [BT_SDP_INT16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf6a3795d22cff4a522a2225339fb5a57)
- [BT_SDP_INT32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga0ad987ebeac3dab3ef2196f4dfeca1ab)
- [BT_SDP_INT64](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaae793fef5690c6013e6e0e34ededb75f)
- [BT_SDP_INT128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf754bbfd9cdc0e6a2bf7d6c46fab3f29)
- [BT_SDP_UUID_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga4f829572cca9669a8a96a857874bb022)
- [BT_SDP_UUID16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga45598f1c663acd3a3e5a409696cb3d2f)
- [BT_SDP_UUID32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga78245bb059feb3ec039e05aba24746e7)
- [BT_SDP_UUID128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaadf48ba3e96687fff99ff58789d79a50)
- [BT_SDP_TEXT_STR_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaca9942a42701cda835a5bf7b7aaf1d75)
- [BT_SDP_TEXT_STR8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga885ace6b1def91f3fa4dd16cb391d2b8)
- [BT_SDP_TEXT_STR16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa5301cdac5fc9299837f29b92aa3c10b)
- [BT_SDP_TEXT_STR32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga29657a21117a3fbe05942778a8d7637e)
- [BT_SDP_BOOL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac48f198f6609fac95db69c09ac69efab)
- [BT_SDP_SEQ_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa884191d772bfa24484cb33c0f614334)
- [BT_SDP_SEQ8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5a64e3bec70b40114a3160dbfb1e484b)
- [BT_SDP_SEQ16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gadf5b15a0296a872ffefc24bbc90dc45b)
- [BT_SDP_SEQ32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga639e86b5103168917cb7202100e3124d)
- [BT_SDP_ALT_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaee1bd735929cb2c4bca48cc7663407fd)
- [BT_SDP_ALT8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab7460f41f05a418d58f4b6807d84cb40)
- [BT_SDP_ALT16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab976bc87f0dcba0e4bc61575ea04ccc7)
- [BT_SDP_ALT32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga420936f672ae31ca701ae277b69d592a)
- [BT_SDP_URL_STR_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga32a7a79422f52b75c2eb2d2eb467dc00)
- [BT_SDP_URL_STR8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gafb2a77d6097c8c4cf9f01b7e16df26f1)
- [BT_SDP_URL_STR16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac1acc712468e5af1f54022ac3551882a)
- [BT_SDP_URL_STR32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga37476681e9d4eee53b710c44e2da9a2f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_sdp_discover_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad672a89277b276d1b702fe07302c468e)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [BT_SDP_DISCOVER_UUID_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga278df12ff5def68ca4663defd178582ca990fbea48866b2acb7ccd67391b19636)
- [BT_SDP_DISCOVER_UUID_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga278df12ff5def68ca4663defd178582ca94e15ea86b69d65ca9c1947d1e2157ef)
- [BT_SDP_DISCOVER_SERVICE_SEARCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga88019838cb3e5317fce93f4933583d94a9ce8c93cf1754fc7047951e891f66ff2)
- [BT_SDP_DISCOVER_SERVICE_ATTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga88019838cb3e5317fce93f4933583d94a5b8c3260e5aaaa08e86a099ccfeee41f)
- [BT_SDP_DISCOVER_SERVICE_SEARCH_ATTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga88019838cb3e5317fce93f4933583d94a64fff103816cfc0215b9b3909786fa4e)
- [bt_sdp_attr_value_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5e4a45b7b860d82a111480c9f25c2666)
- [BT_SDP_ATTR_VALUE_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666acaf932b38a1e17ca9e85c055096fa1da)
- [BT_SDP_ATTR_VALUE_TYPE_UINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a5af87613192cda6a05fa280d2df8574b)
- [BT_SDP_ATTR_VALUE_TYPE_SINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a5917deef84a7af5d5f908d4058732b1e)
- [BT_SDP_ATTR_VALUE_TYPE_BOOL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a154bbb29fb26d007838c87def4cd34f8)
- [BT_SDP_ATTR_VALUE_TYPE_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a80b8652e39dae70c61443adf4f29fb4d)
- [BT_SDP_ATTR_VALUE_TYPE_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gga5e4a45b7b860d82a111480c9f25c2666a27eccef21d812956c6ae7ff9194e20e4)
- [bt_sdp_register_service](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga6006e3cd593ef793273fb291913790fa)
- [bt_sdp_unregister_service](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga71e7d75850becf4ead62668c8e7bebbc)
- [bt_sdp_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga44658df825a40f820a31e7adb4240d25)
- [bt_sdp_discover_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2eb0646597a44e0e3cb0234d2c12a2d7)
- [bt_sdp_get_proto_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaf69723cff6dce7e86f0f0240ec3e2041)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_sdp_get_addl_proto_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaba31a2327e4bba56ef2ac831b166e66a)
- [bt_sdp_get_profile_version](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9e7d4bd0a407fe8254410f907db90f00)
- [bt_sdp_get_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gae1c3110dfe24a939cc02d998c4699ca7)
- [bt_sdp_get_vendor_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaed089d52f57cb25d2b02b2adbc60a36a)
- [bt_sdp_get_product_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga71809908bb73150258b2a5ab3c2f8517)
- [bt_sdp_record_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga0ce1314e052881eec5a43f571857960e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_sdp_has_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga2cb42ca8e487071682c37124ab56f2ab)
- [bt_sdp_get_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga9df34b18af051782377229a18e6d3887)
- [bt_sdp_attr_value_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gab7d3e8bc83efff28cf9118710b5486fc)
- [bt_sdp_attr_has_uuid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga07ca5d4f383d74004478cfd6ead2b80a)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_sdp_attr_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga3bad45ab578c0277a320ac241692f799)
- [bt_sdp_attr_addl_proto_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gac395eff18a4d2af3d955e276bf13963a)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [bt_sdp_attr_addl_proto_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gaa104046a9e6e15f05961bf8652ecec16)
- [bt_sdp_attr_addl_proto_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gacf20a00d84e6eed2c128284fe9c52024)

<a id="header-details"></a>

---

[上一章](P004_zephyr__dt-bindings__pinctrl__lpc84x-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__usb_c__tcpci.h_文件参考.md)
