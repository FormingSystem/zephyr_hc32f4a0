---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-10
title: 传输管理（Transport management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_传输管理（Transport management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 传输管理 API

<a id="details"></a>

MCUmgr 传输管理 API（Transport Management API）。自 4.5 起提供（Since 4.5），版本（Version）0.1.0。

<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_transport_5Fmgmt_2Eh"></a>

```c
file transport_mgmt.h
```

相关声明：[transport_mgmt.h](../api_file_system_power_reference/P043_zephyr__mgmt__mcumgr__grp__transport_mgmt__transport_mgmt.h_文件参考.md)。

MCUmgr传输管理组（Transport Management Group）API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.2\_宏定义（Macros）

<a id="r_ga9cdb0b588d6d3f12c8f845bc69ef9d13"></a>

```c
#define TRANSPORT_MGMT_DIRECTION_INCOMING false
```

相关声明：[TRANSPORT_MGMT_DIRECTION_INCOMING](#ga9cdb0b588d6d3f12c8f845bc69ef9d13)、[false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)。

入向传输（Incoming Transport）：设备将指定传输上的读／写请求包（Read/Write Request Packets）转发到与其桥接（Bridged）的传输，并从该传输出站。

<a id="r_ga22375d795b497134e20678d16352135d"></a>

```c
#define TRANSPORT_MGMT_DIRECTION_OUTGOING true
```

相关声明：[TRANSPORT_MGMT_DIRECTION_OUTGOING](#ga22375d795b497134e20678d16352135d)、[true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)。

出向传输（Outgoing Transport）：设备将指定传输上的读／写响应包（Read/Write Response Packets）转发到与其桥接（Bridged）的传输，并从该传输出站。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.3\_枚举（Enumerations）

<a id="r_gafd6cc94b25d114564c6aa30bec41c14b"></a>

```c
enum transport_mgmt_ids { TRANSPORT_MGMT_ID_CONNECT , TRANSPORT_MGMT_ID_DISCONNECT , TRANSPORT_MGMT_ID_STATUS , TRANSPORT_MGMT_ID_RESERVED_1 , TRANSPORT_MGMT_ID_RESERVED_2 , TRANSPORT_MGMT_ID_RESERVED_3 , TRANSPORT_MGMT_ID_LIST , TRANSPORT_MGMT_ID_GET_MODES , TRANSPORT_MGMT_ID_GET_CONFIG_DETAILS }
```

相关声明：[transport_mgmt_ids](#gafd6cc94b25d114564c6aa30bec41c14b)、[TRANSPORT_MGMT_ID_CONNECT](#ggafd6cc94b25d114564c6aa30bec41c14ba87735cde975ff404e10ff29cfe76c24c)、[TRANSPORT_MGMT_ID_DISCONNECT](#ggafd6cc94b25d114564c6aa30bec41c14ba9c46215d029d1d0b030a69fcb1812ad1)、[TRANSPORT_MGMT_ID_STATUS](#ggafd6cc94b25d114564c6aa30bec41c14ba6cd0a2a1b247e0e2f2683f4063adaee3)、[TRANSPORT_MGMT_ID_RESERVED_1](#ggafd6cc94b25d114564c6aa30bec41c14ba408f083dddd2d42987dd5ea47572f5e0)、[TRANSPORT_MGMT_ID_RESERVED_2](#ggafd6cc94b25d114564c6aa30bec41c14ba3a451c036732b87208c38d84df384c2c)、[TRANSPORT_MGMT_ID_RESERVED_3](#ggafd6cc94b25d114564c6aa30bec41c14ba50d0df5f92d46b697e7cc7c8d3a43e93)、[TRANSPORT_MGMT_ID_LIST](#ggafd6cc94b25d114564c6aa30bec41c14ba67b28c281b5d0ba9a7a686cf76881a85)、[TRANSPORT_MGMT_ID_GET_MODES](#ggafd6cc94b25d114564c6aa30bec41c14ba04662ef967bc6ad42b7606a11aec773f)、[TRANSPORT_MGMT_ID_GET_CONFIG_DETAILS](#ggafd6cc94b25d114564c6aa30bec41c14ba22083e434ea11e01916bb0d58f5a33a3)。

传输管理组（Transport Management Group）的命令 ID。

<a id="r_ga9dccb97ec585e3f6fbefb076c0702a0b"></a>

```c
enum transport_mgmt_ret_code_t { TRANSPORT_MGMT_ERR_OK = 0 , TRANSPORT_MGMT_ERR_UNKNOWN , TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_REQUIRED_FUNCTIONS , TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_INFO_FUNCTIONS , TRANSPORT_MGMT_ERR_INVALID_TRANSPORT , TRANSPORT_MGMT_ERR_INVALID_MODE , TRANSPORT_MGMT_ERR_ALL_CONTEXTS_USED , TRANSPORT_MGMT_ERR_BOTH_TRANSPORT_AND_ALL_PARAMETERS , TRANSPORT_MGMT_ERR_NOT_BRIDGED , TRANSPORT_MGMT_ERR_SAME_BRIDGE_DEVICE_DISALLOWED , TRANSPORT_MGMT_ERR_TRANSPORT_INGOING_NOT_SUPPORTED , TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_NOT_SUPPORTED , TRANSPORT_MGMT_ERR_TRANSPORT_INCOMING_TRANSPORT_ALREADY_BRIDGED , TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_TRANSPORT_ALREADY_BRIDGED , TRANSPORT_MGMT_ERR_CONNECT_MISSING_PARAMETER , TRANSPORT_MGMT_ERR_CONNECT_INVALID_PARAMETER , TRANSPORT_MGMT_ERR_CONNECT_UNSUPPORTED_PARAMETER , TRANSPORT_MGMT_ERR_CONNECT_FAILED }
```

相关声明：[transport_mgmt_ret_code_t](#ga9dccb97ec585e3f6fbefb076c0702a0b)、[TRANSPORT_MGMT_ERR_OK](#gga9dccb97ec585e3f6fbefb076c0702a0ba7833f384ca57c0118790fbf7af281a97)、[TRANSPORT_MGMT_ERR_UNKNOWN](#gga9dccb97ec585e3f6fbefb076c0702a0ba2563b4336e20d0b4573b08787682aa03)、[TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_REQUIRED_FUNCTIONS](#gga9dccb97ec585e3f6fbefb076c0702a0baee652c087a1ab0f7188febb1e907db7d)、[TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_INFO_FUNCTIONS](#gga9dccb97ec585e3f6fbefb076c0702a0ba5e289fe0655882faa108e7171c2d229f)、[TRANSPORT_MGMT_ERR_INVALID_TRANSPORT](#gga9dccb97ec585e3f6fbefb076c0702a0ba6926fbd86577bd23b2caa51cd6715f56)、[TRANSPORT_MGMT_ERR_INVALID_MODE](#gga9dccb97ec585e3f6fbefb076c0702a0babdb237a6ddbe8d2bfb5103fb2f0c5155)、[TRANSPORT_MGMT_ERR_ALL_CONTEXTS_USED](#gga9dccb97ec585e3f6fbefb076c0702a0ba1e1c7e63d17dca29404f64960a564eea)、[TRANSPORT_MGMT_ERR_BOTH_TRANSPORT_AND_ALL_PARAMETERS](#gga9dccb97ec585e3f6fbefb076c0702a0ba8ba2d5d9553578df5eea84eac24bb399)、[TRANSPORT_MGMT_ERR_NOT_BRIDGED](#gga9dccb97ec585e3f6fbefb076c0702a0babea503e9b932a05eecc1f179ed651bb2)、[TRANSPORT_MGMT_ERR_SAME_BRIDGE_DEVICE_DISALLOWED](#gga9dccb97ec585e3f6fbefb076c0702a0bae90d5593819ce610d78723d5f33e4f43)、[TRANSPORT_MGMT_ERR_TRANSPORT_INGOING_NOT_SUPPORTED](#gga9dccb97ec585e3f6fbefb076c0702a0baf89cd9308236121019733517eeaea421)、[TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_NOT_SUPPORTED](#gga9dccb97ec585e3f6fbefb076c0702a0baf746faaf0b368fd076190aebde47097a)、[TRANSPORT_MGMT_ERR_TRANSPORT_INCOMING_TRANSPORT_ALREADY_BRIDGED](#gga9dccb97ec585e3f6fbefb076c0702a0babcf4a53c480f3e80b5aab929d83d29e8)、[TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_TRANSPORT_ALREADY_BRIDGED](#gga9dccb97ec585e3f6fbefb076c0702a0ba0fde105d8cd7cbf0a8781faa9db8136d)、[TRANSPORT_MGMT_ERR_CONNECT_MISSING_PARAMETER](#gga9dccb97ec585e3f6fbefb076c0702a0ba684cfd90f80df815703e5db5f19cc32b)、[TRANSPORT_MGMT_ERR_CONNECT_INVALID_PARAMETER](#gga9dccb97ec585e3f6fbefb076c0702a0ba33a1996969a80f586aa07b5579825dee)、[TRANSPORT_MGMT_ERR_CONNECT_UNSUPPORTED_PARAMETER](#gga9dccb97ec585e3f6fbefb076c0702a0ba05be247bbd2ed96809ca856d71d0e88f)、[TRANSPORT_MGMT_ERR_CONNECT_FAILED](#gga9dccb97ec585e3f6fbefb076c0702a0ba8654385eede95aa8c1d42be55f442bec)。

传输管理组（Transport Management Group）的命令结果码（Command Result Codes）。

<a id="r_ga20cae62e5a2ff1edd8bd47c09bedb899"></a>

```c
enum transport_mgmt_config_type_t { TRANSPORT_MGMT_CONFIG_TYPE_UINT = 0 , TRANSPORT_MGMT_CONFIG_TYPE_INT , TRANSPORT_MGMT_CONFIG_TYPE_BOOL , TRANSPORT_MGMT_CONFIG_TYPE_STRING , TRANSPORT_MGMT_CONFIG_TYPE_BYTE_STRING }
```

相关声明：[transport_mgmt_config_type_t](#ga20cae62e5a2ff1edd8bd47c09bedb899)、[TRANSPORT_MGMT_CONFIG_TYPE_UINT](#gga20cae62e5a2ff1edd8bd47c09bedb899a4791f3585507952d1a86aa9eafb5f1af)、[TRANSPORT_MGMT_CONFIG_TYPE_INT](#gga20cae62e5a2ff1edd8bd47c09bedb899abea44b2b3b70a48bce31d6ae07ff7977)、[TRANSPORT_MGMT_CONFIG_TYPE_BOOL](#gga20cae62e5a2ff1edd8bd47c09bedb899a4541d5558c4049f81f1436c4fc7f53e3)、[TRANSPORT_MGMT_CONFIG_TYPE_STRING](#gga20cae62e5a2ff1edd8bd47c09bedb899ab3bedc6db7e1da2334c5c7af64fa68e5)、[TRANSPORT_MGMT_CONFIG_TYPE_BYTE_STRING](#gga20cae62e5a2ff1edd8bd47c09bedb899a71b75164c2408986e43093e817a15532)。

配置类型（Config Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.4\_函数（Functions）

<a id="r_gace3b51c7b0e6ca80b70a8602800f540f"></a>

```c
bool transport_mgmt_is_bridged (struct smp_transport *transport, bool direction)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[transport_mgmt_is_bridged](#gace3b51c7b0e6ca80b70a8602800f540f)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查给定传输（Transport）是否已桥接（Bridged）。

<a id="r_ga6a3fc6b16a8f0a8be70a9c395c240344"></a>

```c
struct smp_transport * transport_mgmt_get_other_transport (struct smp_transport *transport, bool direction)
```

相关声明：[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[transport_mgmt_get_other_transport](#ga6a3fc6b16a8f0a8be70a9c395c240344)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

获取网桥（Bridge）的另一端传输（Transport）。

<a id="r_gac35a18a01b5cff74aa117d7a3739e7a1"></a>

```c
const struct smp_transport_bridge * transport_mgmt_get_bridge (struct smp_transport *transport, bool direction)
```

相关声明：[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)、[transport_mgmt_get_bridge](#gac35a18a01b5cff74aa117d7a3739e7a1)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

获取传输网桥上下文（Transport Bridge Context）。

<a id="r_gae10192f3da308db7777aa9e13ec0dd98"></a>

```c
int transport_mgmt_disconnect_bridge (struct smp_transport_bridge *bridge)
```

相关声明：[transport_mgmt_disconnect_bridge](#gae10192f3da308db7777aa9e13ec0dd98)、[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)。

断开活动网桥（Active Bridge）。

<a id="r_ga2e6e8baabe2f34597bdba27bd8be3f5d"></a>

```c
int transport_mgmt_disconnect_transport (struct smp_transport *transport, bool incoming, bool outgoing)
```

相关声明：[transport_mgmt_disconnect_transport](#ga2e6e8baabe2f34597bdba27bd8be3f5d)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

断开活动网桥（Active Bridge）。

<a id="r_ga3d0f57cfc30eea8b88a91444abc84587"></a>

```c
int transport_mgmt_disconnect_all (void)
```

相关声明：[transport_mgmt_disconnect_all](#ga3d0f57cfc30eea8b88a91444abc84587)。

断开所有活动网桥（Active Bridges）。

<a id="r_ga63d8fff2d408a31503fd7d9900d014f8"></a>

```c
const uint16_t transport_mgmt_group_id (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[transport_mgmt_group_id](#ga63d8fff2d408a31503fd7d9900d014f8)。

获取传输管理组（Transport Management Group）的组 ID。

## 10.5\_详细说明（Detailed Documentation）

<a id="ga9cdb0b588d6d3f12c8f845bc69ef9d13"></a>

### `TRANSPORT_MGMT_DIRECTION_INCOMING`

```c
#define TRANSPORT_MGMT_DIRECTION_INCOMING false
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

入向传输（Incoming Transport）：设备将指定传输上的读／写请求包（Read/Write Request Packets）转发到与其桥接（Bridged）的传输，并从该传输出站。

<a id="ga22375d795b497134e20678d16352135d"></a>

### `TRANSPORT_MGMT_DIRECTION_OUTGOING`

```c
#define TRANSPORT_MGMT_DIRECTION_OUTGOING true
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

出向传输（Outgoing Transport）：设备将指定传输上的读／写响应包（Read/Write Response Packets）转发到与其桥接（Bridged）的传输，并从该传输出站。

<a id="ga20cae62e5a2ff1edd8bd47c09bedb899"></a>

### `transport_mgmt_config_type_t`

```c
enum transport_mgmt_config_type_t
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

配置类型（Config Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TRANSPORT_MGMT_CONFIG_TYPE_UINT` | 无符号整数（Unsigned Integer）。 |
| `TRANSPORT_MGMT_CONFIG_TYPE_INT` | 有符号整数（Signed Integer）。 |
| `TRANSPORT_MGMT_CONFIG_TYPE_BOOL` | 布尔值（Boolean）。 |
| `TRANSPORT_MGMT_CONFIG_TYPE_STRING` | 文本字符串。 |
| `TRANSPORT_MGMT_CONFIG_TYPE_BYTE_STRING` | 字节串（Byte String）。 |

<a id="gafd6cc94b25d114564c6aa30bec41c14b"></a>

### `transport_mgmt_ids`

```c
enum transport_mgmt_ids
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

传输管理组（Transport Management Group）的命令 ID。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TRANSPORT_MGMT_ID_CONNECT` | 用于连接（桥接，Bridge）到另一项传输（Transport）。 |
| `TRANSPORT_MGMT_ID_DISCONNECT` | 用于断开当前桥接（Bridge）或全部桥接。 |
| `TRANSPORT_MGMT_ID_STATUS` | 返回当前桥接状态（Bridge Status）。 |
| `TRANSPORT_MGMT_ID_RESERVED_1` | 保留供将来使用。 |
| `TRANSPORT_MGMT_ID_RESERVED_2` | 保留供将来使用。 |
| `TRANSPORT_MGMT_ID_RESERVED_3` | 保留供将来使用。 |
| `TRANSPORT_MGMT_ID_LIST` | 列出支持的传输（Transports）。 |
| `TRANSPORT_MGMT_ID_GET_MODES` | 获取传输（Transport）所支持的模式（Modes）。 |
| `TRANSPORT_MGMT_ID_GET_CONFIG_DETAILS` | 获取传输（Transport）的配置详情（Configuration Details）。 |

<a id="ga9dccb97ec585e3f6fbefb076c0702a0b"></a>

### `transport_mgmt_ret_code_t`

```c
enum transport_mgmt_ret_code_t
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

传输管理组（Transport Management Group）的命令结果码（Command Result Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TRANSPORT_MGMT_ERR_OK` | 没有错误；如果响应中没有ret值，就隐含表示此结果。 |
| `TRANSPORT_MGMT_ERR_UNKNOWN` | 发生未知错误（Unknown Error）。 |
| `TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_REQUIRED_FUNCTIONS` | 传输（Transport）缺少必需的桥接函数（Mandatory Bridging Functions）。 |
| `TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_INFO_FUNCTIONS` | 传输（Transport）缺少桥接信息函数（Information Bridging Functions）。 |
| `TRANSPORT_MGMT_ERR_INVALID_TRANSPORT` | 传输标识符（Transport ID）无效、不受支持或未提供。 |
| `TRANSPORT_MGMT_ERR_INVALID_MODE` | 模式（Mode）无效、不受支持或未提供。 |
| `TRANSPORT_MGMT_ERR_ALL_CONTEXTS_USED` | 所有传输桥接上下文（Transport Bridging Contexts）均在使用中。 |
| `TRANSPORT_MGMT_ERR_BOTH_TRANSPORT_AND_ALL_PARAMETERS` | 同时提供了 transport 和 all 参数，而应只提供其中一个。 |
| `TRANSPORT_MGMT_ERR_NOT_BRIDGED` | 传输（Transport）未被桥接（Not Bridged）。 |
| `TRANSPORT_MGMT_ERR_SAME_BRIDGE_DEVICE_DISALLOWED` | 此传输不支持同时作为输入和输出桥接设备（Input and Output Bridge Device），原因可能是传输本身的性质，也可能是具体构建配置。 |
| `TRANSPORT_MGMT_ERR_TRANSPORT_INGOING_NOT_SUPPORTED` | 此传输不支持作为桥接的输入部分（Ingoing Part）。 |
| `TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_NOT_SUPPORTED` | 此传输不支持作为桥接的输出部分（Outgoing Part）。 |
| `TRANSPORT_MGMT_ERR_TRANSPORT_INCOMING_TRANSPORT_ALREADY_BRIDGED` | 输入传输（Incoming Transport）已桥接到另一项传输。 |
| `TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_TRANSPORT_ALREADY_BRIDGED` | 输出传输（Outgoing Transport）已桥接到另一项传输。 |
| `TRANSPORT_MGMT_ERR_CONNECT_MISSING_PARAMETER` | 提供的连接数据（Connection Data）缺少一个参数。 |
| `TRANSPORT_MGMT_ERR_CONNECT_INVALID_PARAMETER` | 提供的连接数据（Connection Data）中有一项无效。 |
| `TRANSPORT_MGMT_ERR_CONNECT_UNSUPPORTED_PARAMETER` | 提供的连接数据（Connection Data）中有一项有效，但此设备不支持，或设备配置不支持。 |
| `TRANSPORT_MGMT_ERR_CONNECT_FAILED` | 桥接连接尝试（Bridge Connection Attempt）失败。 |

<a id="ga3d0f57cfc30eea8b88a91444abc84587"></a>

### `transport_mgmt_disconnect_all()`

```c
int transport_mgmt_disconnect_all ( void )
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

断开所有活动网桥（Active Bridges）。

返回（Returns）：返回码（Return Code）。

<a id="gae10192f3da308db7777aa9e13ec0dd98"></a>

### `transport_mgmt_disconnect_bridge()`

```c
int transport_mgmt_disconnect_bridge ( struct smp_transport_bridge * bridge)
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

断开活动网桥（Active Bridge）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bridge` | 桥接上下文（Bridge Context）。 |

返回（Returns）：返回码（Return Code）。

<a id="ga2e6e8baabe2f34597bdba27bd8be3f5d"></a>

### `transport_mgmt_disconnect_transport()`

```c
int transport_mgmt_disconnect_transport ( struct smp_transport * transport, bool incoming, bool outgoing )
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

断开活动网桥（Active Bridge）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 已桥接的传输（Bridged Transport）。 |
| `incoming` | 为 true 时，断开此传输在输入模式（Incoming Mode）下所桥接的桥接上下文。 |
| `outgoing` | 为 true 时，断开此传输在输出模式（Outgoing Mode）下所桥接的桥接上下文。 |

返回（Returns）：返回码（Return Code）。

<a id="gac35a18a01b5cff74aa117d7a3739e7a1"></a>

### `transport_mgmt_get_bridge()`

```c
const struct smp_transport_bridge * transport_mgmt_get_bridge ( struct smp_transport * transport, bool direction )
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

获取传输网桥上下文（Transport Bridge Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 已桥接的传输（Bridged Transport）。 |
| `direction` | 指定要获取的桥接传输方向（Transport Direction），为 TRANSPORT_MGMT_DIRECTION_INCOMING 或 TRANSPORT_MGMT_DIRECTION_OUTGOING。 |

返回（Returns）：提供了有效的已桥接传输时，返回传输桥接上下文（Transport Bridge Context）；否则返回 NULL。

<a id="ga6a3fc6b16a8f0a8be70a9c395c240344"></a>

### `transport_mgmt_get_other_transport()`

```c
struct smp_transport * transport_mgmt_get_other_transport ( struct smp_transport * transport, bool direction )
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

获取网桥（Bridge）的另一端传输（Transport）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 已桥接的传输（Bridged Transport）。 |
| `direction` | 指定要检查的桥接方向（Bridge Direction），以获取另一侧传输，为 TRANSPORT_MGMT_DIRECTION_INCOMING 或 TRANSPORT_MGMT_DIRECTION_OUTGOING。 |

返回（Returns）：提供了有效桥接时，返回另一侧的传输上下文（Transport Context）；否则返回 NULL。

<a id="ga63d8fff2d408a31503fd7d9900d014f8"></a>

### `transport_mgmt_group_id()`

```c
const uint16_t transport_mgmt_group_id ( void )
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

获取传输管理组（Transport Management Group）的组 ID。

启用 CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_FUNCTION 后，如果用户希望使用在运行时设置的动态组标识符（Dynamic Group ID），必须在自己的代码中实现此函数。

返回（Returns）：传输管理组标识符（Transport Management Group ID），必须位于 64–65535 范围内。

<a id="gace3b51c7b0e6ca80b70a8602800f540f"></a>

### `transport_mgmt_is_bridged()`

```c
bool transport_mgmt_is_bridged ( struct smp_transport * transport, bool direction )
```

```c
#include <zephyr/mgmt/mcumgr/grp/transport_mgmt/transport_mgmt.h>
```

检查给定传输（Transport）是否已桥接（Bridged）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 要检查状态的传输（Transport）。 |
| `direction` | 指定要检查的桥接方向（Bridge Direction），为 TRANSPORT_MGMT_DIRECTION_INCOMING 或 TRANSPORT_MGMT_DIRECTION_OUTGOING。 |

返回（Returns）：给定传输在给定模式下已桥接时为 true，否则为 false。


## 10.6\_原页交叉引用（Cross References）

- [transport_mgmt.h](../api_file_system_power_reference/P043_zephyr__mgmt__mcumgr__grp__transport_mgmt__transport_mgmt.h_文件参考.md)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)
- [smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga20cae62e5a2ff1edd8bd47c09bedb899a4791f3585507952d1a86aa9eafb5f1af"></a>
<a id="gga20cae62e5a2ff1edd8bd47c09bedb899abea44b2b3b70a48bce31d6ae07ff7977"></a>
<a id="gga20cae62e5a2ff1edd8bd47c09bedb899a4541d5558c4049f81f1436c4fc7f53e3"></a>
<a id="gga20cae62e5a2ff1edd8bd47c09bedb899ab3bedc6db7e1da2334c5c7af64fa68e5"></a>
<a id="gga20cae62e5a2ff1edd8bd47c09bedb899a71b75164c2408986e43093e817a15532"></a>
<a id="ggafd6cc94b25d114564c6aa30bec41c14ba87735cde975ff404e10ff29cfe76c24c"></a>
<a id="ggafd6cc94b25d114564c6aa30bec41c14ba9c46215d029d1d0b030a69fcb1812ad1"></a>
<a id="ggafd6cc94b25d114564c6aa30bec41c14ba6cd0a2a1b247e0e2f2683f4063adaee3"></a>
<a id="ggafd6cc94b25d114564c6aa30bec41c14ba408f083dddd2d42987dd5ea47572f5e0"></a>
<a id="ggafd6cc94b25d114564c6aa30bec41c14ba3a451c036732b87208c38d84df384c2c"></a>
<a id="ggafd6cc94b25d114564c6aa30bec41c14ba50d0df5f92d46b697e7cc7c8d3a43e93"></a>
<a id="ggafd6cc94b25d114564c6aa30bec41c14ba67b28c281b5d0ba9a7a686cf76881a85"></a>
<a id="ggafd6cc94b25d114564c6aa30bec41c14ba04662ef967bc6ad42b7606a11aec773f"></a>
<a id="ggafd6cc94b25d114564c6aa30bec41c14ba22083e434ea11e01916bb0d58f5a33a3"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0ba7833f384ca57c0118790fbf7af281a97"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0ba2563b4336e20d0b4573b08787682aa03"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0baee652c087a1ab0f7188febb1e907db7d"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0ba5e289fe0655882faa108e7171c2d229f"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0ba6926fbd86577bd23b2caa51cd6715f56"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0babdb237a6ddbe8d2bfb5103fb2f0c5155"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0ba1e1c7e63d17dca29404f64960a564eea"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0ba8ba2d5d9553578df5eea84eac24bb399"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0babea503e9b932a05eecc1f179ed651bb2"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0bae90d5593819ce610d78723d5f33e4f43"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0baf89cd9308236121019733517eeaea421"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0baf746faaf0b368fd076190aebde47097a"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0babcf4a53c480f3e80b5aab929d83d29e8"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0ba0fde105d8cd7cbf0a8781faa9db8136d"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0ba684cfd90f80df815703e5db5f19cc32b"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0ba33a1996969a80f586aa07b5579825dee"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0ba05be247bbd2ed96809ca856d71d0e88f"></a>
<a id="gga9dccb97ec585e3f6fbefb076c0702a0ba8654385eede95aa8c1d42be55f442bec"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_NXP i.MX952 时钟源（Clock Sources）.md) · [返回大纲](大纲.md) · [下一章](P011_值容器（Value Container）.md)
