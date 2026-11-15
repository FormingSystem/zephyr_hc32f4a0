---
id: learning.zephyr-docs.api-file-system-power-reference.page-43
title: zephyr__mgmt__mcumgr__grp__transport_mgmt__transport_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/transport__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_transport\_mgmt\_\_transport\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/transport__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr传输管理组（Transport Management Group）API的头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/mgmt/mcumgr/transport/smp.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h>
```

查看此文件的源码。

MCUmgr传输管理组（Transport Management Group）API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 43.1\_宏定义（Macros）

<a id="r_ga9cdb0b588d6d3f12c8f845bc69ef9d13"></a>

```c
#define TRANSPORT_MGMT_DIRECTION_INCOMING false
```

相关声明：[TRANSPORT_MGMT_DIRECTION_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga9cdb0b588d6d3f12c8f845bc69ef9d13)、[false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)。

入向传输（Incoming Transport）：设备将指定传输上的读／写请求包（Read/Write Request Packets）转发到与其桥接（Bridged）的传输，并从该传输出站。

<a id="r_ga22375d795b497134e20678d16352135d"></a>

```c
#define TRANSPORT_MGMT_DIRECTION_OUTGOING true
```

相关声明：[TRANSPORT_MGMT_DIRECTION_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga22375d795b497134e20678d16352135d)、[true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)。

出向传输（Outgoing Transport）：设备将指定传输上的读／写响应包（Read/Write Response Packets）转发到与其桥接（Bridged）的传输，并从该传输出站。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 43.2\_枚举（Enumerations）

<a id="r_gafd6cc94b25d114564c6aa30bec41c14b"></a>

```c
enum transport_mgmt_ids { TRANSPORT_MGMT_ID_CONNECT , TRANSPORT_MGMT_ID_DISCONNECT , TRANSPORT_MGMT_ID_STATUS , TRANSPORT_MGMT_ID_RESERVED_1 , TRANSPORT_MGMT_ID_RESERVED_2 , TRANSPORT_MGMT_ID_RESERVED_3 , TRANSPORT_MGMT_ID_LIST , TRANSPORT_MGMT_ID_GET_MODES , TRANSPORT_MGMT_ID_GET_CONFIG_DETAILS }
```

相关声明：[transport_mgmt_ids](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gafd6cc94b25d114564c6aa30bec41c14b)、[TRANSPORT_MGMT_ID_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba87735cde975ff404e10ff29cfe76c24c)、[TRANSPORT_MGMT_ID_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba9c46215d029d1d0b030a69fcb1812ad1)、[TRANSPORT_MGMT_ID_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba6cd0a2a1b247e0e2f2683f4063adaee3)、[TRANSPORT_MGMT_ID_RESERVED_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba408f083dddd2d42987dd5ea47572f5e0)、[TRANSPORT_MGMT_ID_RESERVED_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba3a451c036732b87208c38d84df384c2c)、[TRANSPORT_MGMT_ID_RESERVED_3](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba50d0df5f92d46b697e7cc7c8d3a43e93)、[TRANSPORT_MGMT_ID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba67b28c281b5d0ba9a7a686cf76881a85)、[TRANSPORT_MGMT_ID_GET_MODES](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba04662ef967bc6ad42b7606a11aec773f)、[TRANSPORT_MGMT_ID_GET_CONFIG_DETAILS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba22083e434ea11e01916bb0d58f5a33a3)。

传输管理组（Transport Management Group）的命令 ID。

<a id="r_ga9dccb97ec585e3f6fbefb076c0702a0b"></a>

```c
enum transport_mgmt_ret_code_t { TRANSPORT_MGMT_ERR_OK = 0 , TRANSPORT_MGMT_ERR_UNKNOWN , TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_REQUIRED_FUNCTIONS , TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_INFO_FUNCTIONS , TRANSPORT_MGMT_ERR_INVALID_TRANSPORT , TRANSPORT_MGMT_ERR_INVALID_MODE , TRANSPORT_MGMT_ERR_ALL_CONTEXTS_USED , TRANSPORT_MGMT_ERR_BOTH_TRANSPORT_AND_ALL_PARAMETERS , TRANSPORT_MGMT_ERR_NOT_BRIDGED , TRANSPORT_MGMT_ERR_SAME_BRIDGE_DEVICE_DISALLOWED , TRANSPORT_MGMT_ERR_TRANSPORT_INGOING_NOT_SUPPORTED , TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_NOT_SUPPORTED , TRANSPORT_MGMT_ERR_TRANSPORT_INCOMING_TRANSPORT_ALREADY_BRIDGED , TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_TRANSPORT_ALREADY_BRIDGED , TRANSPORT_MGMT_ERR_CONNECT_MISSING_PARAMETER , TRANSPORT_MGMT_ERR_CONNECT_INVALID_PARAMETER , TRANSPORT_MGMT_ERR_CONNECT_UNSUPPORTED_PARAMETER , TRANSPORT_MGMT_ERR_CONNECT_FAILED }
```

相关声明：[transport_mgmt_ret_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga9dccb97ec585e3f6fbefb076c0702a0b)、[TRANSPORT_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba7833f384ca57c0118790fbf7af281a97)、[TRANSPORT_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba2563b4336e20d0b4573b08787682aa03)、[TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_REQUIRED_FUNCTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0baee652c087a1ab0f7188febb1e907db7d)、[TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_INFO_FUNCTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba5e289fe0655882faa108e7171c2d229f)、[TRANSPORT_MGMT_ERR_INVALID_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba6926fbd86577bd23b2caa51cd6715f56)、[TRANSPORT_MGMT_ERR_INVALID_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0babdb237a6ddbe8d2bfb5103fb2f0c5155)、[TRANSPORT_MGMT_ERR_ALL_CONTEXTS_USED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba1e1c7e63d17dca29404f64960a564eea)、[TRANSPORT_MGMT_ERR_BOTH_TRANSPORT_AND_ALL_PARAMETERS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba8ba2d5d9553578df5eea84eac24bb399)、[TRANSPORT_MGMT_ERR_NOT_BRIDGED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0babea503e9b932a05eecc1f179ed651bb2)、[TRANSPORT_MGMT_ERR_SAME_BRIDGE_DEVICE_DISALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0bae90d5593819ce610d78723d5f33e4f43)、[TRANSPORT_MGMT_ERR_TRANSPORT_INGOING_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0baf89cd9308236121019733517eeaea421)、[TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0baf746faaf0b368fd076190aebde47097a)、[TRANSPORT_MGMT_ERR_TRANSPORT_INCOMING_TRANSPORT_ALREADY_BRIDGED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0babcf4a53c480f3e80b5aab929d83d29e8)、[TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_TRANSPORT_ALREADY_BRIDGED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba0fde105d8cd7cbf0a8781faa9db8136d)、[TRANSPORT_MGMT_ERR_CONNECT_MISSING_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba684cfd90f80df815703e5db5f19cc32b)、[TRANSPORT_MGMT_ERR_CONNECT_INVALID_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba33a1996969a80f586aa07b5579825dee)、[TRANSPORT_MGMT_ERR_CONNECT_UNSUPPORTED_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba05be247bbd2ed96809ca856d71d0e88f)、[TRANSPORT_MGMT_ERR_CONNECT_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba8654385eede95aa8c1d42be55f442bec)。

传输管理组（Transport Management Group）的命令结果码（Command Result Codes）。

<a id="r_ga20cae62e5a2ff1edd8bd47c09bedb899"></a>

```c
enum transport_mgmt_config_type_t { TRANSPORT_MGMT_CONFIG_TYPE_UINT = 0 , TRANSPORT_MGMT_CONFIG_TYPE_INT , TRANSPORT_MGMT_CONFIG_TYPE_BOOL , TRANSPORT_MGMT_CONFIG_TYPE_STRING , TRANSPORT_MGMT_CONFIG_TYPE_BYTE_STRING }
```

相关声明：[transport_mgmt_config_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga20cae62e5a2ff1edd8bd47c09bedb899)、[TRANSPORT_MGMT_CONFIG_TYPE_UINT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899a4791f3585507952d1a86aa9eafb5f1af)、[TRANSPORT_MGMT_CONFIG_TYPE_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899abea44b2b3b70a48bce31d6ae07ff7977)、[TRANSPORT_MGMT_CONFIG_TYPE_BOOL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899a4541d5558c4049f81f1436c4fc7f53e3)、[TRANSPORT_MGMT_CONFIG_TYPE_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899ab3bedc6db7e1da2334c5c7af64fa68e5)、[TRANSPORT_MGMT_CONFIG_TYPE_BYTE_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899a71b75164c2408986e43093e817a15532)。

配置类型（Config Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 43.3\_函数（Functions）

<a id="r_gace3b51c7b0e6ca80b70a8602800f540f"></a>

```c
bool transport_mgmt_is_bridged (struct smp_transport *transport, bool direction)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[transport_mgmt_is_bridged](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gace3b51c7b0e6ca80b70a8602800f540f)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查给定传输（Transport）是否已桥接（Bridged）。

<a id="r_ga6a3fc6b16a8f0a8be70a9c395c240344"></a>

```c
struct smp_transport * transport_mgmt_get_other_transport (struct smp_transport *transport, bool direction)
```

相关声明：[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[transport_mgmt_get_other_transport](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga6a3fc6b16a8f0a8be70a9c395c240344)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

获取网桥（Bridge）的另一端传输（Transport）。

<a id="r_gac35a18a01b5cff74aa117d7a3739e7a1"></a>

```c
const struct smp_transport_bridge * transport_mgmt_get_bridge (struct smp_transport *transport, bool direction)
```

相关声明：[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)、[transport_mgmt_get_bridge](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gac35a18a01b5cff74aa117d7a3739e7a1)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

获取传输网桥上下文（Transport Bridge Context）。

<a id="r_gae10192f3da308db7777aa9e13ec0dd98"></a>

```c
int transport_mgmt_disconnect_bridge (struct smp_transport_bridge *bridge)
```

相关声明：[transport_mgmt_disconnect_bridge](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gae10192f3da308db7777aa9e13ec0dd98)、[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)。

断开活动网桥（Active Bridge）。

<a id="r_ga2e6e8baabe2f34597bdba27bd8be3f5d"></a>

```c
int transport_mgmt_disconnect_transport (struct smp_transport *transport, bool incoming, bool outgoing)
```

相关声明：[transport_mgmt_disconnect_transport](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga2e6e8baabe2f34597bdba27bd8be3f5d)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

断开活动网桥（Active Bridge）。

<a id="r_ga3d0f57cfc30eea8b88a91444abc84587"></a>

```c
int transport_mgmt_disconnect_all (void)
```

相关声明：[transport_mgmt_disconnect_all](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga3d0f57cfc30eea8b88a91444abc84587)。

断开所有活动网桥（Active Bridges）。

<a id="r_ga63d8fff2d408a31503fd7d9900d014f8"></a>

```c
const uint16_t transport_mgmt_group_id (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[transport_mgmt_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga63d8fff2d408a31503fd7d9900d014f8)。

获取传输管理组（Transport Management Group）的组 ID。


## 43.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/transport/smp.h](../api_source_system_reference/P018_smp.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h](../api_source_reference/P522_mgmt_defines.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P228_transport_mgmt.h_源码浏览.md)
- [TRANSPORT_MGMT_DIRECTION_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga9cdb0b588d6d3f12c8f845bc69ef9d13)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [TRANSPORT_MGMT_DIRECTION_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga22375d795b497134e20678d16352135d)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [transport_mgmt_ids](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gafd6cc94b25d114564c6aa30bec41c14b)
- [TRANSPORT_MGMT_ID_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba87735cde975ff404e10ff29cfe76c24c)
- [TRANSPORT_MGMT_ID_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba9c46215d029d1d0b030a69fcb1812ad1)
- [TRANSPORT_MGMT_ID_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba6cd0a2a1b247e0e2f2683f4063adaee3)
- [TRANSPORT_MGMT_ID_RESERVED_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba408f083dddd2d42987dd5ea47572f5e0)
- [TRANSPORT_MGMT_ID_RESERVED_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba3a451c036732b87208c38d84df384c2c)
- [TRANSPORT_MGMT_ID_RESERVED_3](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba50d0df5f92d46b697e7cc7c8d3a43e93)
- [TRANSPORT_MGMT_ID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba67b28c281b5d0ba9a7a686cf76881a85)
- [TRANSPORT_MGMT_ID_GET_MODES](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba04662ef967bc6ad42b7606a11aec773f)
- [TRANSPORT_MGMT_ID_GET_CONFIG_DETAILS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ggafd6cc94b25d114564c6aa30bec41c14ba22083e434ea11e01916bb0d58f5a33a3)
- [transport_mgmt_ret_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga9dccb97ec585e3f6fbefb076c0702a0b)
- [TRANSPORT_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba7833f384ca57c0118790fbf7af281a97)
- [TRANSPORT_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba2563b4336e20d0b4573b08787682aa03)
- [TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_REQUIRED_FUNCTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0baee652c087a1ab0f7188febb1e907db7d)
- [TRANSPORT_MGMT_ERR_TRANSPORT_MISSING_INFO_FUNCTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba5e289fe0655882faa108e7171c2d229f)
- [TRANSPORT_MGMT_ERR_INVALID_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba6926fbd86577bd23b2caa51cd6715f56)
- [TRANSPORT_MGMT_ERR_INVALID_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0babdb237a6ddbe8d2bfb5103fb2f0c5155)
- [TRANSPORT_MGMT_ERR_ALL_CONTEXTS_USED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba1e1c7e63d17dca29404f64960a564eea)
- [TRANSPORT_MGMT_ERR_BOTH_TRANSPORT_AND_ALL_PARAMETERS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba8ba2d5d9553578df5eea84eac24bb399)
- [TRANSPORT_MGMT_ERR_NOT_BRIDGED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0babea503e9b932a05eecc1f179ed651bb2)
- [TRANSPORT_MGMT_ERR_SAME_BRIDGE_DEVICE_DISALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0bae90d5593819ce610d78723d5f33e4f43)
- [TRANSPORT_MGMT_ERR_TRANSPORT_INGOING_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0baf89cd9308236121019733517eeaea421)
- [TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0baf746faaf0b368fd076190aebde47097a)
- [TRANSPORT_MGMT_ERR_TRANSPORT_INCOMING_TRANSPORT_ALREADY_BRIDGED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0babcf4a53c480f3e80b5aab929d83d29e8)
- [TRANSPORT_MGMT_ERR_TRANSPORT_OUTGOING_TRANSPORT_ALREADY_BRIDGED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba0fde105d8cd7cbf0a8781faa9db8136d)
- [TRANSPORT_MGMT_ERR_CONNECT_MISSING_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba684cfd90f80df815703e5db5f19cc32b)
- [TRANSPORT_MGMT_ERR_CONNECT_INVALID_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba33a1996969a80f586aa07b5579825dee)
- [TRANSPORT_MGMT_ERR_CONNECT_UNSUPPORTED_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba05be247bbd2ed96809ca856d71d0e88f)
- [TRANSPORT_MGMT_ERR_CONNECT_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga9dccb97ec585e3f6fbefb076c0702a0ba8654385eede95aa8c1d42be55f442bec)
- [transport_mgmt_config_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga20cae62e5a2ff1edd8bd47c09bedb899)
- [TRANSPORT_MGMT_CONFIG_TYPE_UINT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899a4791f3585507952d1a86aa9eafb5f1af)
- [TRANSPORT_MGMT_CONFIG_TYPE_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899abea44b2b3b70a48bce31d6ae07ff7977)
- [TRANSPORT_MGMT_CONFIG_TYPE_BOOL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899a4541d5558c4049f81f1436c4fc7f53e3)
- [TRANSPORT_MGMT_CONFIG_TYPE_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899ab3bedc6db7e1da2334c5c7af64fa68e5)
- [TRANSPORT_MGMT_CONFIG_TYPE_BYTE_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gga20cae62e5a2ff1edd8bd47c09bedb899a71b75164c2408986e43093e817a15532)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [transport_mgmt_is_bridged](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gace3b51c7b0e6ca80b70a8602800f540f)
- [smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)
- [transport_mgmt_get_other_transport](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga6a3fc6b16a8f0a8be70a9c395c240344)
- [smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)
- [transport_mgmt_get_bridge](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gac35a18a01b5cff74aa117d7a3739e7a1)
- [transport_mgmt_disconnect_bridge](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#gae10192f3da308db7777aa9e13ec0dd98)
- [transport_mgmt_disconnect_transport](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga2e6e8baabe2f34597bdba27bd8be3f5d)
- [transport_mgmt_disconnect_all](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga3d0f57cfc30eea8b88a91444abc84587)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [transport_mgmt_group_id](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__mgmt.html#ga63d8fff2d408a31503fd7d9900d014f8)

<a id="header-details"></a>

---

[上一章](P042_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_toolchain.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P044_zephyr__drivers__console__uart_mcumgr.h_文件参考.md)
