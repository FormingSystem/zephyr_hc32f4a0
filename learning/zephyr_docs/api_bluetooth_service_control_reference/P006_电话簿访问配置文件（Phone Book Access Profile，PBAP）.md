---
id: learning.zephyr-docs.api-bluetooth-service-control-reference.page-6
title: 电话簿访问配置文件（Phone Book Access Profile，PBAP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_电话簿访问配置文件（Phone Book Access Profile，PBAP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电话簿访问配置文件（Phone Book Access Profile，PBAP）

<a id="details"></a>

电话簿访问配置文件（Phone Book Access Profile，PBAP）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_bt_5Fpbap_5Fpce_5Fcb"></a>

```c
struct bt_pbap_pce_cb
```

相关声明：[bt_pbap_pce_cb](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md)。

电话簿访问配置文件（PBAP）的电话簿客户端设备（PCE）回调操作结构。

<a id="r_bt_5Fpbap_5Fpce"></a>

```c
struct bt_pbap_pce
```

相关声明：[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)。

电话簿访问配置文件（PBAP）的电话簿客户端设备（PCE）结构。

<a id="r_bt_5Fpbap_5Fpse_5Fcb"></a>

```c
struct bt_pbap_pse_cb
```

相关声明：[bt_pbap_pse_cb](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md)。

电话簿访问配置文件（PBAP）的电话簿服务器设备（PSE）回调操作结构。

<a id="r_bt_5Fpbap_5Fpse_5Frfcomm"></a>

```c
struct bt_pbap_pse_rfcomm
```

相关声明：[bt_pbap_pse_rfcomm](../bluetooth_service_model_reference/P154_bt_pbap_pse_rfcomm_结构体.md)。

电话簿访问配置文件（PBAP）的PSE RFCOMM服务器结构。

<a id="r_bt_5Fpbap_5Fpse_5Fl2cap"></a>

```c
struct bt_pbap_pse_l2cap
```

相关声明：[bt_pbap_pse_l2cap](../bluetooth_service_model_reference/P153_bt_pbap_pse_l2cap_结构体.md)。

电话簿访问配置文件（PBAP）的PSE L2CAP服务器结构。

<a id="r_bt_5Fpbap_5Fpse"></a>

```c
struct bt_pbap_pse
```

相关声明：[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)。

电话簿访问配置文件（PBAP）的电话簿服务器设备（PSE）结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga73f1c2b754b4fc3afe2f8f2cb154469b"></a>

```c
#define BT_PBAP_UUID
```

相关声明：[BT_PBAP_UUID](#ga73f1c2b754b4fc3afe2f8f2cb154469b)。

用于服务标识（Service Identification）的 PBAP 目标 UUID（Target UUID）。

<a id="r_gad8dc6e92eba851f2a8c6111d8d22edcc"></a>

```c
#define BT_PBAP_PULL_PHONE_BOOK_TYPE "x-bt/phonebook"
```

相关声明：[BT_PBAP_PULL_PHONE_BOOK_TYPE](#gad8dc6e92eba851f2a8c6111d8d22edcc)。

拉取电话簿操作（Pull Phone Book Operation）的 OBEX 类型头（Type Header）。

<a id="r_ga957dd1b14b50864ac9c4a057b3702dec"></a>

```c
#define BT_PBAP_PULL_VCARD_LISTING_TYPE "x-bt/vcard-listing"
```

相关声明：[BT_PBAP_PULL_VCARD_LISTING_TYPE](#ga957dd1b14b50864ac9c4a057b3702dec)。

拉取 vCard 列表操作（Pull vCard Listing Operation）的 OBEX 类型头（Type Header）。

<a id="r_gaac21da1879eed8074e5d01e315ea213a"></a>

```c
#define BT_PBAP_PULL_VCARD_ENTRY_TYPE "x-bt/vcard"
```

相关声明：[BT_PBAP_PULL_VCARD_ENTRY_TYPE](#gaac21da1879eed8074e5d01e315ea213a)。

拉取 vCard 条目操作（Pull vCard Entry Operation）的 OBEX 类型头（Type Header）。

<a id="r_ga9602f26d0e3524e0a5f40a9854432e44"></a>

```c
#define BT_PBAP_SET_PHONE_BOOK_FLAGS_UP (BT_OBEX_SETPATH_FLAG_BACKUP | BT_OBEX_SETPATH_FLAG_NO_CREATE)
```

相关声明：[BT_PBAP_SET_PHONE_BOOK_FLAGS_UP](#ga9602f26d0e3524e0a5f40a9854432e44)、[BT_OBEX_SETPATH_FLAG_BACKUP](P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75)、[BT_OBEX_SETPATH_FLAG_NO_CREATE](P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553)。

设置电话簿标志（Set Phone Book Flags）：向上导航到父目录（Parent Directory）。

<a id="r_ga66c979baa8aefbfab188d4c9017fac8b"></a>

```c
#define BT_PBAP_SET_PHONE_BOOK_FLAGS_DOWN_OR_ROOT BT_OBEX_SETPATH_FLAG_NO_CREATE
```

相关声明：[BT_PBAP_SET_PHONE_BOOK_FLAGS_DOWN_OR_ROOT](#ga66c979baa8aefbfab188d4c9017fac8b)、[BT_OBEX_SETPATH_FLAG_NO_CREATE](P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553)。

设置电话簿标志（Set Phone Book Flags）：向下导航到子目录（Child Directory），或导航到根目录（Root）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.3\_枚举（Enumerations）

<a id="r_ga9d9697d62b6bdbbc4feb0cf4b9776b58"></a>

```c
enum bt_pbap_rsp_code { BT_PBAP_RSP_CODE_CONTINUE = BT_OBEX_RSP_CODE_CONTINUE , BT_PBAP_RSP_CODE_OK = BT_OBEX_RSP_CODE_OK , BT_PBAP_RSP_CODE_SUCCESS = BT_OBEX_RSP_CODE_SUCCESS , BT_PBAP_RSP_CODE_BAD_REQ = BT_OBEX_RSP_CODE_BAD_REQ , BT_PBAP_RSP_CODE_UNAUTH = BT_OBEX_RSP_CODE_UNAUTH , BT_PBAP_RSP_CODE_FORBIDDEN = BT_OBEX_RSP_CODE_FORBIDDEN , BT_PBAP_RSP_CODE_NOT_FOUND = BT_OBEX_RSP_CODE_NOT_FOUND , BT_PBAP_RSP_CODE_NOT_ACCEPT = BT_OBEX_RSP_CODE_NOT_ACCEPT , BT_PBAP_RSP_CODE_PRECON_FAIL = BT_OBEX_RSP_CODE_PRECON_FAIL , BT_PBAP_RSP_CODE_NOT_IMPL = BT_OBEX_RSP_CODE_NOT_IMPL , BT_PBAP_RSP_CODE_UNAVAIL = BT_OBEX_RSP_CODE_UNAVAIL }
```

相关声明：[bt_pbap_rsp_code](#ga9d9697d62b6bdbbc4feb0cf4b9776b58)、[BT_PBAP_RSP_CODE_CONTINUE](#gga9d9697d62b6bdbbc4feb0cf4b9776b58a661acfbba2e792ee4444453650db00eb)、[BT_PBAP_RSP_CODE_OK](#gga9d9697d62b6bdbbc4feb0cf4b9776b58a904e13430e8318623f1a785b94caee93)、[BT_PBAP_RSP_CODE_SUCCESS](#gga9d9697d62b6bdbbc4feb0cf4b9776b58a26f8b1cb1f6bc983b1508b5a2e298a3e)、[BT_PBAP_RSP_CODE_BAD_REQ](#gga9d9697d62b6bdbbc4feb0cf4b9776b58a3130502de3a9c28985692f8d93b6ad08)、[BT_PBAP_RSP_CODE_UNAUTH](#gga9d9697d62b6bdbbc4feb0cf4b9776b58a9f3978e6433273f9a1af3e0c91ae33cd)、[BT_PBAP_RSP_CODE_FORBIDDEN](#gga9d9697d62b6bdbbc4feb0cf4b9776b58a7cab8c591dca0bc0279c6463ece416d6)、[BT_PBAP_RSP_CODE_NOT_FOUND](#gga9d9697d62b6bdbbc4feb0cf4b9776b58a2f4a1259666bfbf84c8c8ac02faa8683)、[BT_PBAP_RSP_CODE_NOT_ACCEPT](#gga9d9697d62b6bdbbc4feb0cf4b9776b58a806a9638aa9ca07d52f2dbb6946b6594)、[BT_PBAP_RSP_CODE_PRECON_FAIL](#gga9d9697d62b6bdbbc4feb0cf4b9776b58ab34bbcad2a7fe5c2b9f2efa511b69ccf)、[BT_PBAP_RSP_CODE_NOT_IMPL](#gga9d9697d62b6bdbbc4feb0cf4b9776b58aa0c1cbc8611c6a5f39d1d61858ea85cb)、[BT_PBAP_RSP_CODE_UNAVAIL](#gga9d9697d62b6bdbbc4feb0cf4b9776b58a722cfbba810a0646a340d8bba82282fa)。

PBAP 响应码（Response Codes）。

<a id="r_gac6c48c5b202c19567a4ddb008626f174"></a>

```c
enum bt_pbap_appl_param_order { BT_PBAP_APPL_PARAM_ORDER_INDEXED = 0x00 , BT_PBAP_APPL_PARAM_ORDER_ALPHABETICAL = 0x01 , BT_PBAP_APPL_PARAM_ORDER_PHONETIC = 0x02 }
```

相关声明：[bt_pbap_appl_param_order](#gac6c48c5b202c19567a4ddb008626f174)、[BT_PBAP_APPL_PARAM_ORDER_INDEXED](#ggac6c48c5b202c19567a4ddb008626f174ab03a1c4e18ea46da6c28fe83a850b510)、[BT_PBAP_APPL_PARAM_ORDER_ALPHABETICAL](#ggac6c48c5b202c19567a4ddb008626f174a59e2999c6d5af45b12c88d8bf78c7252)、[BT_PBAP_APPL_PARAM_ORDER_PHONETIC](#ggac6c48c5b202c19567a4ddb008626f174accbdbbf7c94a707b77c6b249760f37a1)。

PBAP 应用参数中 Order 参数的值（Parameter Values）。

<a id="r_gafc697dd2db191451f1d2334f5758be69"></a>

```c
enum bt_pbap_appl_param_search_property { BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NAME = 0x00 , BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NUMBER = 0x01 , BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_SOUND = 0x02 }
```

相关声明：[bt_pbap_appl_param_search_property](#gafc697dd2db191451f1d2334f5758be69)、[BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NAME](#ggafc697dd2db191451f1d2334f5758be69afb959ef0be8bd3e0e06eb26d8a186772)、[BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NUMBER](#ggafc697dd2db191451f1d2334f5758be69a7c22ec68b0d24778b1a0677b31f335a3)、[BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_SOUND](#ggafc697dd2db191451f1d2334f5758be69a7216e629be9047a08a48be8210c272bc)。

PBAP 应用参数中 Search Property 参数的值（Parameter Values）。

<a id="r_ga5cf30994d6344a67b22eb01baf863b1b"></a>

```c
enum bt_pbap_appl_param_format { BT_PBAP_APPL_PARAM_FORMAT_2_1 = 0x00 , BT_PBAP_APPL_PARAM_FORMAT_3_0 = 0x01 }
```

相关声明：[bt_pbap_appl_param_format](#ga5cf30994d6344a67b22eb01baf863b1b)、[BT_PBAP_APPL_PARAM_FORMAT_2_1](#gga5cf30994d6344a67b22eb01baf863b1baf5f30663b6083d8c09950e71dc6e1e0b)、[BT_PBAP_APPL_PARAM_FORMAT_3_0](#gga5cf30994d6344a67b22eb01baf863b1ba0fa84dbd58771867b547805099689a3a)。

PBAP 应用参数中 Format 参数的值（Parameter Values）。

<a id="r_ga76ceaa735d7bc5ee97d665d497b896cd"></a>

```c
enum bt_pbap_appl_param_vcard_selector_operator { BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_OR = 0x00 , BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_AND = 0x01 }
```

相关声明：[bt_pbap_appl_param_vcard_selector_operator](#ga76ceaa735d7bc5ee97d665d497b896cd)、[BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_OR](#gga76ceaa735d7bc5ee97d665d497b896cda338230ca0c8d07ca4a5cced68cf9faf4)、[BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_AND](#gga76ceaa735d7bc5ee97d665d497b896cda4f1435ad0230025a1bf612fd38df67a9)。

PBAP 应用参数中 vCard Selector Operator 参数的值（Parameter Values）。

<a id="r_gadc3ace27caf970d0f2f8c8278e50c7fc"></a>

```c
enum bt_pbap_appl_param_reset_new_missed_calls { BT_PBAP_APPL_PARAM_RESET_NEW_MISSED_CALLS = 0x01 }
```

相关声明：[bt_pbap_appl_param_reset_new_missed_calls](#gadc3ace27caf970d0f2f8c8278e50c7fc)、[BT_PBAP_APPL_PARAM_RESET_NEW_MISSED_CALLS](#ggadc3ace27caf970d0f2f8c8278e50c7fca99adb79a6d49413c2c3dc83ff4686e5d)。

PBAP 应用参数中重置新增未接来电（Reset New Missed Calls）参数的值。

<a id="r_ga81e3d8885dddfae8f8e2714ef9173949"></a>

```c
enum bt_pbap_appl_param_property_mask { BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_VERSION = (1ULL << (0)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_FN = (1ULL << (1)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_N = (1ULL << (2)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PHOTO = (1ULL << (3)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_BDAY = (1ULL << (4)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ADR = (1ULL << (5)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LABEL = (1ULL << (6)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TEL = (1ULL << (7)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_EMAIL = (1ULL << (8)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_MAILER = (1ULL << (9)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TZ = (1ULL << (10)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_GEO = (1ULL << (11)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TITLE = (1ULL << (12)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ROLE = (1ULL << (13)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LOGO = (1ULL << (14)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_AGENT = (1ULL << (15)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ORG = (1ULL << (16)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NOTE = (1ULL << (17)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_REV = (1ULL << (18)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SOUND = (1ULL << (19)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_URL = (1ULL << (20)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_UID = (1ULL << (21)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_KEY = (1ULL << (22)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NICKNAME = (1ULL << (23)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CATEGORIES = (1ULL << (24)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PRODID = (1ULL << (25)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CLASS = (1ULL << (26)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SORT_STRING = (1ULL << (27)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_IRMC_CALL_DATETIME = (1ULL << (28)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_SPEEDDIALKEY = (1ULL << (29)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UCI = (1ULL << (30)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UID = (1ULL << (31)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PROPRIETARY_FILTER = (1ULL << (39)) }
```

相关声明：[bt_pbap_appl_param_property_mask](#ga81e3d8885dddfae8f8e2714ef9173949)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_VERSION](#gga81e3d8885dddfae8f8e2714ef9173949a9dc945e68284feb0c84c3f266b504e9a)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_FN](#gga81e3d8885dddfae8f8e2714ef9173949a4eccbde165789980859146504dc6ad79)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_N](#gga81e3d8885dddfae8f8e2714ef9173949a095c248ed7a21c3024843b06c8757c65)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PHOTO](#gga81e3d8885dddfae8f8e2714ef9173949abbf728e6870fb11e11095741261dce74)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_BDAY](#gga81e3d8885dddfae8f8e2714ef9173949ab1029f770ff972cd56ca27149697b3c1)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ADR](#gga81e3d8885dddfae8f8e2714ef9173949a392c7a7f408f80443e330e7e8317790f)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LABEL](#gga81e3d8885dddfae8f8e2714ef9173949a534c44365efffc777b134db0d7158d01)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TEL](#gga81e3d8885dddfae8f8e2714ef9173949aba04655292e204ffea1ea8e6f868990a)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_EMAIL](#gga81e3d8885dddfae8f8e2714ef9173949ae97d497323807766a249a354d9c73440)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_MAILER](#gga81e3d8885dddfae8f8e2714ef9173949aaedbb7e84f50781fa88eaff8859bf0c0)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TZ](#gga81e3d8885dddfae8f8e2714ef9173949a8eeef93a6fb6d1f90688444d4c025d75)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_GEO](#gga81e3d8885dddfae8f8e2714ef9173949a2bd2e420601d0d8dfd6d308b48ab3cf5)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TITLE](#gga81e3d8885dddfae8f8e2714ef9173949a5cb26f5f8d5baff7b2d28e030db326f1)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ROLE](#gga81e3d8885dddfae8f8e2714ef9173949a2f7b5161e2440abaa4dbcaf4351f9dc8)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LOGO](#gga81e3d8885dddfae8f8e2714ef9173949af45314b48bb91277d8ad84d29e44ce54)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_AGENT](#gga81e3d8885dddfae8f8e2714ef9173949a8030f80cf155692c1728775885c0786b)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ORG](#gga81e3d8885dddfae8f8e2714ef9173949ac94b5f034af49ba23222988ac05dca41)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NOTE](#gga81e3d8885dddfae8f8e2714ef9173949a9e6232e6968a9604421a81a4d364e868)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_REV](#gga81e3d8885dddfae8f8e2714ef9173949aa5acc89efeae0ef6fabbcdbc5c461cf0)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SOUND](#gga81e3d8885dddfae8f8e2714ef9173949a07399ae04375a6c435f34815b734aabb)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_URL](#gga81e3d8885dddfae8f8e2714ef9173949a31e2f9be865df16c883964b8abaea828)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_UID](#gga81e3d8885dddfae8f8e2714ef9173949a0d8adde858f93c7d5b765fb0488f22ce)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_KEY](#gga81e3d8885dddfae8f8e2714ef9173949a1c16e137b53c6c88152ed49d693dd32b)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NICKNAME](#gga81e3d8885dddfae8f8e2714ef9173949a1622cc47e9c5d359d327b9175829b005)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CATEGORIES](#gga81e3d8885dddfae8f8e2714ef9173949a9b2cb462f56b4abbda146fc3b6e0250b)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PRODID](#gga81e3d8885dddfae8f8e2714ef9173949a12d9060eef27b4c048064df7b00faf7f)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CLASS](#gga81e3d8885dddfae8f8e2714ef9173949a728ddfce7f0f93564e6e657d3fd9f9ca)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SORT_STRING](#gga81e3d8885dddfae8f8e2714ef9173949a7cfcd8e622d1adb99c5ad598b2642720)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_IRMC_CALL_DATETIME](#gga81e3d8885dddfae8f8e2714ef9173949a6af54c454719c9a5baa75db6feb3c6e6)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_SPEEDDIALKEY](#gga81e3d8885dddfae8f8e2714ef9173949ad1b5c9ec39747786c90c89b190235b5e)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UCI](#gga81e3d8885dddfae8f8e2714ef9173949a1fe34f3b6c0a3c9ca0966106052faa61)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UID](#gga81e3d8885dddfae8f8e2714ef9173949a587cb6926e50eca38c633019312208d5)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PROPRIETARY_FILTER](#gga81e3d8885dddfae8f8e2714ef9173949ab98d31a99ac92b189b8963f275d6846b)。

PBAP 属性位掩码（Property Bitmask）。

<a id="r_gadbc19ba92332972e5d22e213c7618fa0"></a>

```c
enum bt_pbap_appl_param_tag_id { BT_PBAP_APPL_PARAM_TAG_ID_ORDER = 0x01 , BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_VALUE = 0x02 , BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_PROPERTY = 0x03 , BT_PBAP_APPL_PARAM_TAG_ID_MAX_LIST_COUNT = 0x04 , BT_PBAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET = 0x05 , BT_PBAP_APPL_PARAM_TAG_ID_PROPERTY_SELECTOR = 0x06 , BT_PBAP_APPL_PARAM_TAG_ID_FORMAT = 0x07 , BT_PBAP_APPL_PARAM_TAG_ID_PHONEBOOK_SIZE = 0x08 , BT_PBAP_APPL_PARAM_TAG_ID_NEW_MISSED_CALLS = 0x09 , BT_PBAP_APPL_PARAM_TAG_ID_PRIMARY_FOLDER_VERSION = 0x0a , BT_PBAP_APPL_PARAM_TAG_ID_SECONDARY_FOLDER_VERSION = 0x0b , BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR = 0x0c , BT_PBAP_APPL_PARAM_TAG_ID_DATABASE_IDENTIFIER = 0x0d , BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR_OPERATOR = 0x0e , BT_PBAP_APPL_PARAM_TAG_ID_RESET_NEW_MISSED_CALLS = 0x0f , BT_PBAP_APPL_PARAM_TAG_ID_SUPPORTED_FEATURES = 0x10 }
```

相关声明：[bt_pbap_appl_param_tag_id](#gadbc19ba92332972e5d22e213c7618fa0)、[BT_PBAP_APPL_PARAM_TAG_ID_ORDER](#ggadbc19ba92332972e5d22e213c7618fa0a32182e2f399ec292ea652dd7f04bbdee)、[BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_VALUE](#ggadbc19ba92332972e5d22e213c7618fa0a4a1bbc25a06c89dd948542ec700a7323)、[BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_PROPERTY](#ggadbc19ba92332972e5d22e213c7618fa0af4a5a102fc189ad256b75091522d1b66)、[BT_PBAP_APPL_PARAM_TAG_ID_MAX_LIST_COUNT](#ggadbc19ba92332972e5d22e213c7618fa0aa17305107ed8979b917dab98f04442bf)、[BT_PBAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET](#ggadbc19ba92332972e5d22e213c7618fa0a2cf69d5233c590f708571c2447539025)、[BT_PBAP_APPL_PARAM_TAG_ID_PROPERTY_SELECTOR](#ggadbc19ba92332972e5d22e213c7618fa0a7894ebcf543e20b5c3369ec6632fb9c9)、[BT_PBAP_APPL_PARAM_TAG_ID_FORMAT](#ggadbc19ba92332972e5d22e213c7618fa0ac9aade48ff6a95d27443f817daf6ba75)、[BT_PBAP_APPL_PARAM_TAG_ID_PHONEBOOK_SIZE](#ggadbc19ba92332972e5d22e213c7618fa0a0bc424753f8b1da0b3209c38925c6162)、[BT_PBAP_APPL_PARAM_TAG_ID_NEW_MISSED_CALLS](#ggadbc19ba92332972e5d22e213c7618fa0acc1b3f202aa38ff027a63aecb9108641)、[BT_PBAP_APPL_PARAM_TAG_ID_PRIMARY_FOLDER_VERSION](#ggadbc19ba92332972e5d22e213c7618fa0abea06880695df75ef9ca68e94e4596b4)、[BT_PBAP_APPL_PARAM_TAG_ID_SECONDARY_FOLDER_VERSION](#ggadbc19ba92332972e5d22e213c7618fa0a793e24d13b717616ee8eb09792d19310)、[BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR](#ggadbc19ba92332972e5d22e213c7618fa0aeac485e4bb2ca3d4fcdaf0e76fd55a08)、[BT_PBAP_APPL_PARAM_TAG_ID_DATABASE_IDENTIFIER](#ggadbc19ba92332972e5d22e213c7618fa0a60027135eafa915cac55a1cc59d68b4f)、[BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR_OPERATOR](#ggadbc19ba92332972e5d22e213c7618fa0acfbe210e7ef87a3a07b00f05b62f7616)、[BT_PBAP_APPL_PARAM_TAG_ID_RESET_NEW_MISSED_CALLS](#ggadbc19ba92332972e5d22e213c7618fa0a4eb10ced494b26ad1380f6808574716c)、[BT_PBAP_APPL_PARAM_TAG_ID_SUPPORTED_FEATURES](#ggadbc19ba92332972e5d22e213c7618fa0a66bf205d11a351aa10fba0c6648600db)。

PBAP 应用参数标签标识符（Application Parameter Tag IDs）。

<a id="r_gae51b98f9472a284aba377a0343a6335f"></a>

```c
enum bt_pbap_supported_feature { BT_PBAP_SUPPORTED_FEATURE_DOWNLOAD = (1UL << (0)) , BT_PBAP_SUPPORTED_FEATURE_BROWSING = (1UL << (1)) , BT_PBAP_SUPPORTED_FEATURE_DATABASE_IDENTIFIER = (1UL << (2)) , BT_PBAP_SUPPORTED_FEATURE_FOLDER_VERSION_COUNTERS = (1UL << (3)) , BT_PBAP_SUPPORTED_FEATURE_VCARD_SELECTOR = (1UL << (4)) , BT_PBAP_SUPPORTED_FEATURE_ENHANCED_MISSED_CALLS = (1UL << (5)) , BT_PBAP_SUPPORTED_FEATURE_UCI_VCARD_PROPERTY = (1UL << (6)) , BT_PBAP_SUPPORTED_FEATURE_UID_VCARD_PROPERTY = (1UL << (7)) , BT_PBAP_SUPPORTED_FEATURE_CONTACT_REFERENCING = (1UL << (8)) , BT_PBAP_SUPPORTED_FEATURE_DEFAULT_CONTACT_IMAGE = (1UL << (9)) }
```

相关声明：[bt_pbap_supported_feature](#gae51b98f9472a284aba377a0343a6335f)、[BT_PBAP_SUPPORTED_FEATURE_DOWNLOAD](#ggae51b98f9472a284aba377a0343a6335fadd13a4cd31cacd5a1ee3738f6514d7bf)、[BT_PBAP_SUPPORTED_FEATURE_BROWSING](#ggae51b98f9472a284aba377a0343a6335faeba96c52f51b6bcf64cdab4826104603)、[BT_PBAP_SUPPORTED_FEATURE_DATABASE_IDENTIFIER](#ggae51b98f9472a284aba377a0343a6335faa77889b21608736c840c5870236b8b7f)、[BT_PBAP_SUPPORTED_FEATURE_FOLDER_VERSION_COUNTERS](#ggae51b98f9472a284aba377a0343a6335fafcac813cc74198792f97e1eba6594a93)、[BT_PBAP_SUPPORTED_FEATURE_VCARD_SELECTOR](#ggae51b98f9472a284aba377a0343a6335fa04a72163c9a4aa1ca94e096fc61c0110)、[BT_PBAP_SUPPORTED_FEATURE_ENHANCED_MISSED_CALLS](#ggae51b98f9472a284aba377a0343a6335fa09b908bca7982fc1818791c6ff2a9d54)、[BT_PBAP_SUPPORTED_FEATURE_UCI_VCARD_PROPERTY](#ggae51b98f9472a284aba377a0343a6335fa208cd02d7acabf2f6444292d2f0290ec)、[BT_PBAP_SUPPORTED_FEATURE_UID_VCARD_PROPERTY](#ggae51b98f9472a284aba377a0343a6335faa9087f0238d221a036a599b2bcceee5e)、[BT_PBAP_SUPPORTED_FEATURE_CONTACT_REFERENCING](#ggae51b98f9472a284aba377a0343a6335faa7ab39682e0f35c54ff5e67c76b3741c)、[BT_PBAP_SUPPORTED_FEATURE_DEFAULT_CONTACT_IMAGE](#ggae51b98f9472a284aba377a0343a6335fa8f549e342b61b7bb4533eac1c4019a8f)。

PBAP 支持的特性位掩码（Supported Features Bitmask）。

<a id="r_gadd0760a5999620762367a5dda62018b7"></a>

```c
enum bt_pbap_supported_repositories { BT_PBAP_SUPPORTED_REPOSITORIES_LOCAL_PHONE_BOOK = (1UL << (0)) , BT_PBAP_SUPPORTED_REPOSITORIES_SIM = (1UL << (1)) , BT_PBAP_SUPPORTED_REPOSITORIES_SPEED_DIAL = (1UL << (2)) , BT_PBAP_SUPPORTED_REPOSITORIES_FAVORITES = (1UL << (3)) }
```

相关声明：[bt_pbap_supported_repositories](#gadd0760a5999620762367a5dda62018b7)、[BT_PBAP_SUPPORTED_REPOSITORIES_LOCAL_PHONE_BOOK](#ggadd0760a5999620762367a5dda62018b7a58a43511704fe46d8f8cdbb8d0e6f9fe)、[BT_PBAP_SUPPORTED_REPOSITORIES_SIM](#ggadd0760a5999620762367a5dda62018b7aaf5d738a116dd37e2bc18bec07858415)、[BT_PBAP_SUPPORTED_REPOSITORIES_SPEED_DIAL](#ggadd0760a5999620762367a5dda62018b7aa3f4d6139aad54ee40d60c9ab474dc48)、[BT_PBAP_SUPPORTED_REPOSITORIES_FAVORITES](#ggadd0760a5999620762367a5dda62018b7adf8db04f430e9b19d75fd6396f6bf0f2)。

PBAP 支持的资料库位掩码（Supported Repositories Bitmask）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.4\_函数（Functions）

<a id="r_ga9fcd75bb18c48756dfa4695890662ab0"></a>

```c
int bt_pbap_pce_rfcomm_connect (struct bt_conn *conn, struct bt_pbap_pce *pbap_pce, struct bt_pbap_pce_cb *cb, uint8_t channel)
```

相关声明：[bt_pbap_pce_rfcomm_connect](#ga9fcd75bb18c48756dfa4695890662ab0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[bt_pbap_pce_cb](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

电话簿客户端设备（PCE）通过 RFCOMM 传输连接电话簿服务器设备（PSE）。

<a id="r_gaae2eac838c1b825f5d31d7073608e56d"></a>

```c
int bt_pbap_pce_rfcomm_disconnect (struct bt_pbap_pce *pbap_pce)
```

相关声明：[bt_pbap_pce_rfcomm_disconnect](#gaae2eac838c1b825f5d31d7073608e56d)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)。

断开 PBAP PCE 的 RFCOMM 传输（Transport）。

<a id="r_gae9506155e96d3f641ee928754439f579"></a>

```c
int bt_pbap_pce_l2cap_connect (struct bt_conn *conn, struct bt_pbap_pce *pbap_pce, struct bt_pbap_pce_cb *cb, uint16_t psm)
```

相关声明：[bt_pbap_pce_l2cap_connect](#gae9506155e96d3f641ee928754439f579)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[bt_pbap_pce_cb](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 L2CAP 传输（Transport）连接 PBAP PCE 客户端。

<a id="r_gad407918b6c075045339aecd55b70db21"></a>

```c
int bt_pbap_pce_l2cap_disconnect (struct bt_pbap_pce *pbap_pce)
```

相关声明：[bt_pbap_pce_l2cap_disconnect](#gad407918b6c075045339aecd55b70db21)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)。

断开 PBAP PCE 的 L2CAP 传输（Transport）。

<a id="r_gab326aadad5f12827f08f6525b7dc5458"></a>

```c
struct net_buf * bt_pbap_pce_create_pdu (struct bt_pbap_pce *pbap_pce, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_pbap_pce_create_pdu](#gab326aadad5f12827f08f6525b7dc5458)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

从缓冲池（Pool）分配缓冲区，并为 PBAP PCE 预留头部空间（Headroom）。

<a id="r_ga29d4e867858a96606a623313acc808d9"></a>

```c
int bt_pbap_pce_connect (struct bt_pbap_pce *pbap_pce, uint16_t mopl, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_connect](#ga29d4e867858a96606a623313acc808d9)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

建立从 PCE 客户端到 PSE 服务器的 PBAP 协议连接（Protocol Connection）。

<a id="r_ga5af0c3016e948bc27df328432ffa9455"></a>

```c
int bt_pbap_pce_disconnect (struct bt_pbap_pce *pbap_pce, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_disconnect](#ga5af0c3016e948bc27df328432ffa9455)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP 客户端 PCE 断开 PBAP 连接（Connection）。

<a id="r_ga07f8db1528fc15bed243fc5da787354f"></a>

```c
int bt_pbap_pce_pull_phone_book (struct bt_pbap_pce *pbap_pce, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_pull_phone_book](#ga07f8db1528fc15bed243fc5da787354f)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP 服务器 PSE 拉取电话簿（Pull Phone Book）。

<a id="r_ga71ba43da527c77f3eaf7d43ae5c22cae"></a>

```c
int bt_pbap_pce_pull_vcard_listing (struct bt_pbap_pce *pbap_pce, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_pull_vcard_listing](#ga71ba43da527c77f3eaf7d43ae5c22cae)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP 服务器 PSE 拉取 vCard 列表（Pull vCard Listing）。

<a id="r_gac1f07e0eb9b256010fdbcf29b71701c6"></a>

```c
int bt_pbap_pce_pull_vcard_entry (struct bt_pbap_pce *pbap_pce, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_pull_vcard_entry](#gac1f07e0eb9b256010fdbcf29b71701c6)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP 服务器 PSE 拉取指定 vCard 条目（Pull vCard Entry）。

<a id="r_ga15403745f42ba10ba1dd9552895e111d"></a>

```c
int bt_pbap_pce_set_phone_book (struct bt_pbap_pce *pbap_pce, uint8_t flags, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_set_phone_book](#ga15403745f42ba10ba1dd9552895e111d)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置 PBAP 服务器 PSE 上的当前电话簿（Current Phone Book）。

<a id="r_gab24a2cb71edfa1d5e59c33fabc01c7d9"></a>

```c
int bt_pbap_pce_abort (struct bt_pbap_pce *pbap_pce, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_abort](#gab24a2cb71edfa1d5e59c33fabc01c7d9)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

中止 PBAP 服务器 PSE 上的当前操作（Abort Current Operation）。

<a id="r_gae26500d48fae5f26946ab7a4e261993c"></a>

```c
struct net_buf * bt_pbap_pse_create_pdu (struct bt_pbap_pse *pbap_pse, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_pbap_pse_create_pdu](#gae26500d48fae5f26946ab7a4e261993c)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

从缓冲池（Pool）分配缓冲区，并为 PBAP PSE 预留头部空间（Headroom）。

<a id="r_ga72b9420a34975c9691690977169bcec6"></a>

```c
int bt_pbap_pse_rfcomm_register (struct bt_pbap_pse_rfcomm *server)
```

相关声明：[bt_pbap_pse_rfcomm_register](#ga72b9420a34975c9691690977169bcec6)、[bt_pbap_pse_rfcomm](../bluetooth_service_model_reference/P154_bt_pbap_pse_rfcomm_结构体.md)。

注册 PBAP PSE RFCOMM 服务器（Server）。

<a id="r_gab37e9ea163060e8b770da56e5a6415cb"></a>

```c
int bt_pbap_pse_l2cap_register (struct bt_pbap_pse_l2cap *server)
```

相关声明：[bt_pbap_pse_l2cap_register](#gab37e9ea163060e8b770da56e5a6415cb)、[bt_pbap_pse_l2cap](../bluetooth_service_model_reference/P153_bt_pbap_pse_l2cap_结构体.md)。

注册 PBAP PSE L2CAP 服务器（Server）。

<a id="r_ga15c39f4afb996a37b43acd51cc82ed53"></a>

```c
int bt_pbap_pse_register (struct bt_pbap_pse *pbap_pse, struct bt_pbap_pse_cb *cb)
```

相关声明：[bt_pbap_pse_register](#ga15c39f4afb996a37b43acd51cc82ed53)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[bt_pbap_pse_cb](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md)。

注册 PBAP PSE 实例（Instance）。

<a id="r_gac76cb47df9f747f222d7cdbe627d3ead"></a>

```c
int bt_pbap_pse_connect_rsp (struct bt_pbap_pse *pbap_pse, uint16_t mopl, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_connect_rsp](#gac76cb47df9f747f222d7cdbe627d3ead)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送连接响应（Connect Response）。

<a id="r_gafa7ebec6db37286b0ca54ed1d9f4ca02"></a>

```c
int bt_pbap_pse_disconnect_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_disconnect_rsp](#gafa7ebec6db37286b0ca54ed1d9f4ca02)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送断开连接响应（Disconnect Response）。

<a id="r_gac8ef77affecb5316991afca6c1005f62"></a>

```c
int bt_pbap_pse_pull_phone_book_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_pull_phone_book_rsp](#gac8ef77affecb5316991afca6c1005f62)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送拉取电话簿响应（Pull Phone Book Response）。

<a id="r_gac511c99ae0c2d0f391f5dbf150599390"></a>

```c
int bt_pbap_pse_pull_vcard_listing_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_pull_vcard_listing_rsp](#gac511c99ae0c2d0f391f5dbf150599390)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送拉取 vCard 列表响应（Pull vCard Listing Response）。

<a id="r_gacdcbb62a6999c833e4e6d0846aad28d6"></a>

```c
int bt_pbap_pse_pull_vcard_entry_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_pull_vcard_entry_rsp](#gacdcbb62a6999c833e4e6d0846aad28d6)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送拉取 vCard 条目响应（Pull vCard Entry Response）。

<a id="r_ga09e255e0c5328a1f1e7286b7100eeb61"></a>

```c
int bt_pbap_pse_set_phone_book_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_set_phone_book_rsp](#ga09e255e0c5328a1f1e7286b7100eeb61)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送设置电话簿响应（Set Phone Book Response）。

<a id="r_ga9766bda140034251ba3287bfa116f359"></a>

```c
int bt_pbap_pse_abort_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_abort_rsp](#ga9766bda140034251ba3287bfa116f359)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送中止响应（Abort Response）。

## 6.5\_详细说明（Detailed Documentation）

<a id="gad8dc6e92eba851f2a8c6111d8d22edcc"></a>

### `BT_PBAP_PULL_PHONE_BOOK_TYPE`

```c
#define BT_PBAP_PULL_PHONE_BOOK_TYPE "x-bt/phonebook"
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

拉取电话簿操作（Pull Phone Book Operation）的 OBEX 类型头（Type Header）。

<a id="gaac21da1879eed8074e5d01e315ea213a"></a>

### `BT_PBAP_PULL_VCARD_ENTRY_TYPE`

```c
#define BT_PBAP_PULL_VCARD_ENTRY_TYPE "x-bt/vcard"
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

拉取 vCard 条目操作（Pull vCard Entry Operation）的 OBEX 类型头（Type Header）。

<a id="ga957dd1b14b50864ac9c4a057b3702dec"></a>

### `BT_PBAP_PULL_VCARD_LISTING_TYPE`

```c
#define BT_PBAP_PULL_VCARD_LISTING_TYPE "x-bt/vcard-listing"
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

拉取 vCard 列表操作（Pull vCard Listing Operation）的 OBEX 类型头（Type Header）。

<a id="ga66c979baa8aefbfab188d4c9017fac8b"></a>

### `BT_PBAP_SET_PHONE_BOOK_FLAGS_DOWN_OR_ROOT`

```c
#define BT_PBAP_SET_PHONE_BOOK_FLAGS_DOWN_OR_ROOT BT_OBEX_SETPATH_FLAG_NO_CREATE
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

设置电话簿标志（Set Phone Book Flags）：向下导航到子目录（Child Directory），或导航到根目录（Root）。

OBEX Setpath 标志（Flag），用于在电话簿层次结构中向下进入子目录或进入根目录。

<a id="ga9602f26d0e3524e0a5f40a9854432e44"></a>

### `BT_PBAP_SET_PHONE_BOOK_FLAGS_UP`

```c
#define BT_PBAP_SET_PHONE_BOOK_FLAGS_UP (BT_OBEX_SETPATH_FLAG_BACKUP | BT_OBEX_SETPATH_FLAG_NO_CREATE)
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

设置电话簿标志（Set Phone Book Flags）：向上导航到父目录（Parent Directory）。

OBEX Setpath 标志组合（Flag Combination），用于在电话簿层次结构中进入父目录。

<a id="ga73f1c2b754b4fc3afe2f8f2cb154469b"></a>

### `BT_PBAP_UUID`

```c
#define BT_PBAP_UUID
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

展开值（Value）：

```c
(const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
        BT_UUID_128_ENCODE(0x796135f0, 0xf0c5, 0x11d8, 0x0966, 0x0800200c9a66))
```

用于服务标识（Service Identification）的 PBAP 目标 UUID（Target UUID）。

128 位 UUID（`796135f0-f0c5-11d8-0966-0800200c9a66`），用于在 OBEX 连接建立过程中标识电话簿访问配置文件（Phone Book Access Profile，PBAP）服务。

<a id="ga5cf30994d6344a67b22eb01baf863b1b"></a>

### `bt_pbap_appl_param_format`

```c
enum bt_pbap_appl_param_format
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

PBAP 应用参数中 Format 参数的值（Parameter Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_PBAP_APPL_PARAM_FORMAT_2_1` | 电子名片（vCard）版本 2.1。 |
| `BT_PBAP_APPL_PARAM_FORMAT_3_0` | 电子名片（vCard）版本 3.0。 |

<a id="gac6c48c5b202c19567a4ddb008626f174"></a>

### `bt_pbap_appl_param_order`

```c
enum bt_pbap_appl_param_order
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

PBAP 应用参数中 Order 参数的值（Parameter Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_PBAP_APPL_PARAM_ORDER_INDEXED` | 按索引排序（Indexed Order）。 |
| `BT_PBAP_APPL_PARAM_ORDER_ALPHABETICAL` | 按字母排序（Alphabetical Order）。 |
| `BT_PBAP_APPL_PARAM_ORDER_PHONETIC` | 按发音排序（Phonetic Order）。 |

<a id="ga81e3d8885dddfae8f8e2714ef9173949"></a>

### `bt_pbap_appl_param_property_mask`

```c
enum bt_pbap_appl_param_property_mask
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

PBAP 属性位掩码（Property Bitmask）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_VERSION` | 电子名片（vCard）版本。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_FN` | 格式化姓名（Formatted Name）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_N` | 姓名的结构化表示（Structured Presentation of Name）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PHOTO` | 关联图像或照片（Image or Photo）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_BDAY` | 生日（Birthday）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ADR` | 投递地址（Delivery Address）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LABEL` | 投递地址标签（Delivery Address Label）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TEL` | 电话号码（Telephone Number）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_EMAIL` | 电子邮件地址（Electronic Mail Address）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_MAILER` | 电子邮件程序名称（Email Program Name）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TZ` | 时区（Time Zone）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_GEO` | 地理位置（Geographic Position）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TITLE` | 职务（Job Title）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ROLE` | 角色或职业（Role or Occupation）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LOGO` | 组织标志（Organization Logo）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_AGENT` | 代理人（Agent）的电子名片（vCard）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ORG` | 组织名称（Organization Name）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NOTE` | 备注（Comments）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_REV` | 修订信息（Revision）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SOUND` | 姓名发音（Pronunciation of Name）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_URL` | 统一资源定位符（Uniform Resource Locator，URL）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_UID` | 唯一 ID（Unique ID）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_KEY` | 公钥（Public Key）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NICKNAME` | 昵称（Nickname）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CATEGORIES` | 类别（Categories）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PRODID` | 产品标识符（Product ID）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CLASS` | 类信息（Class Information）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SORT_STRING` | 用于排序操作（Sorting Operations）的字符串。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_IRMC_CALL_DATETIME` | 未接来电的时间戳（Time Stamp）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_SPEEDDIALKEY` | 快速拨号快捷方式（Speed-dial Shortcut）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UCI` | 蓝牙唯一联系人标识符（Unique Contact Identifier，UCI）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UID` | 蓝牙唯一标识符（UID）。 |
| `BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PROPRIETARY_FILTER` | 专有筛选（Proprietary Filtering）。 |

<a id="gadc3ace27caf970d0f2f8c8278e50c7fc"></a>

### `bt_pbap_appl_param_reset_new_missed_calls`

```c
enum bt_pbap_appl_param_reset_new_missed_calls
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

PBAP 应用参数中重置新增未接来电（Reset New Missed Calls）参数的值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_PBAP_APPL_PARAM_RESET_NEW_MISSED_CALLS` | 复位（Reset）。 |

<a id="gafc697dd2db191451f1d2334f5758be69"></a>

### `bt_pbap_appl_param_search_property`

```c
enum bt_pbap_appl_param_search_property
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

PBAP 应用参数中 Search Property 参数的值（Parameter Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NAME` | 姓名（Name）。 |
| `BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NUMBER` | 数字（Number）。 |
| `BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_SOUND` | 发音（Sound）。 |

<a id="gadbc19ba92332972e5d22e213c7618fa0"></a>

### `bt_pbap_appl_param_tag_id`

```c
enum bt_pbap_appl_param_tag_id
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

PBAP 应用参数标签标识符（Application Parameter Tag IDs）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_PBAP_APPL_PARAM_TAG_ID_ORDER` | 排序方式（Order），参见 `bt_pbap_appl_param_order`。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_VALUE` | 搜索值（Search Value）。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_PROPERTY` | 搜索属性（Search Property），参见 `bt_pbap_appl_param_search_property`。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_MAX_LIST_COUNT` | 最大列表数量（Max List Count）。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET` | 列表起始偏移量（List Start Offset）。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_PROPERTY_SELECTOR` | 属性选择器（Property Selector），参见 `bt_pbap_appl_param_property_mask`。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_FORMAT` | 格式（Format），参见 `bt_pbap_appl_param_format`。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_PHONEBOOK_SIZE` | 电话簿大小（Phonebook Size）。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_NEW_MISSED_CALLS` | 新增未接来电（New Missed Calls）。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_PRIMARY_FOLDER_VERSION` | 主文件夹版本（Primary Folder Version）。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_SECONDARY_FOLDER_VERSION` | 次文件夹版本（Secondary Folder Version）。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR` | 电子名片选择器（vCard Selector），参见 `bt_pbap_appl_param_property_mask`。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_DATABASE_IDENTIFIER` | 数据库标识符（Database Identifier）。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR_OPERATOR` | 电子名片选择器运算符（vCard Selector Operator），参见 `bt_pbap_appl_param_property_mask`。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_RESET_NEW_MISSED_CALLS` | 重置新增未接来电（Reset New Missed Calls），参见 `bt_pbap_appl_param_reset_new_missed_calls`。 |
| `BT_PBAP_APPL_PARAM_TAG_ID_SUPPORTED_FEATURES` | PBAP 支持的特性（Supported Features），参见 `bt_pbap_supported_feature`。 |

<a id="ga76ceaa735d7bc5ee97d665d497b896cd"></a>

### `bt_pbap_appl_param_vcard_selector_operator`

```c
enum bt_pbap_appl_param_vcard_selector_operator
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

PBAP 应用参数中 vCard Selector Operator 参数的值（Parameter Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_OR` | 或运算符（OR Operator）。 |
| `BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_AND` | 与运算符（AND Operator）。 |

<a id="ga9d9697d62b6bdbbc4feb0cf4b9776b58"></a>

### `bt_pbap_rsp_code`

```c
enum bt_pbap_rsp_code
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

PBAP 响应码（Response Codes）。

PBAP 操作使用的响应码（Response Codes），由 OBEX 响应码映射而来，用于表示 PBAP 请求和操作的状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_PBAP_RSP_CODE_CONTINUE` | 继续（Continue）。 |
| `BT_PBAP_RSP_CODE_OK` | 成功（OK）。 |
| `BT_PBAP_RSP_CODE_SUCCESS` | 成功。 |
| `BT_PBAP_RSP_CODE_BAD_REQ` | 错误请求（Bad Request）：服务器无法理解请求。 |
| `BT_PBAP_RSP_CODE_UNAUTH` | 未经授权（Unauthorized）。 |
| `BT_PBAP_RSP_CODE_FORBIDDEN` | 禁止（Forbidden）：理解该操作，但拒绝执行。 |
| `BT_PBAP_RSP_CODE_NOT_FOUND` | 未找到（Not Found）。 |
| `BT_PBAP_RSP_CODE_NOT_ACCEPT` | 不可接受（Not Acceptable）。 |
| `BT_PBAP_RSP_CODE_PRECON_FAIL` | 前置条件失败（Precondition Failed）。 |
| `BT_PBAP_RSP_CODE_NOT_IMPL` | 未实现（Not Implemented）。 |
| `BT_PBAP_RSP_CODE_UNAVAIL` | 服务不可用（Service Unavailable）。 |

<a id="gae51b98f9472a284aba377a0343a6335f"></a>

### `bt_pbap_supported_feature`

```c
enum bt_pbap_supported_feature
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

PBAP 支持的特性位掩码（Supported Features Bitmask）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_PBAP_SUPPORTED_FEATURE_DOWNLOAD` | 下载特性（Download）：支持下载电话簿。 |
| `BT_PBAP_SUPPORTED_FEATURE_BROWSING` | 浏览特性（Browsing）：支持浏览电话簿。 |
| `BT_PBAP_SUPPORTED_FEATURE_DATABASE_IDENTIFIER` | 数据库标识符特性（Database Identifier）：支持跟踪数据库变化。 |
| `BT_PBAP_SUPPORTED_FEATURE_FOLDER_VERSION_COUNTERS` | 文件夹版本计数器特性（Folder Version Counters）：支持跟踪文件夹版本。 |
| `BT_PBAP_SUPPORTED_FEATURE_VCARD_SELECTOR` | 电子名片选择器特性（vCard Selector）：支持按 vCard 属性筛选。 |
| `BT_PBAP_SUPPORTED_FEATURE_ENHANCED_MISSED_CALLS` | 增强未接来电特性（Enhanced Missed Calls）：支持增强的未接来电处理。 |
| `BT_PBAP_SUPPORTED_FEATURE_UCI_VCARD_PROPERTY` | UCI 电子名片属性特性（UCI vCard Property）：支持唯一联系人标识符（Unique Contact Identifier）。 |
| `BT_PBAP_SUPPORTED_FEATURE_UID_VCARD_PROPERTY` | UID 电子名片属性特性（UID vCard Property）：支持 vCard 的 UID 属性。 |
| `BT_PBAP_SUPPORTED_FEATURE_CONTACT_REFERENCING` | 联系人引用特性（Contact Referencing）：支持处理联系人引用。 |
| `BT_PBAP_SUPPORTED_FEATURE_DEFAULT_CONTACT_IMAGE` | 默认联系人图像特性（Default Contact Image）：支持默认联系人图像。 |

<a id="gadd0760a5999620762367a5dda62018b7"></a>

### `bt_pbap_supported_repositories`

```c
enum bt_pbap_supported_repositories
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

PBAP 支持的资料库位掩码（Supported Repositories Bitmask）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_PBAP_SUPPORTED_REPOSITORIES_LOCAL_PHONE_BOOK` | 本地电话簿存储库（Local Phone Book Repository）。 |
| `BT_PBAP_SUPPORTED_REPOSITORIES_SIM` | SIM 卡存储库（SIM Card Repository）。 |
| `BT_PBAP_SUPPORTED_REPOSITORIES_SPEED_DIAL` | 快速拨号存储库（Speed Dial Repository）。 |
| `BT_PBAP_SUPPORTED_REPOSITORIES_FAVORITES` | 收藏夹存储库（Favorites Repository）。 |

<a id="gab24a2cb71edfa1d5e59c33fabc01c7d9"></a>

### `bt_pbap_pce_abort()`

```c
int bt_pbap_pce_abort ( struct bt_pbap_pce * pbap_pce, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

中止 PBAP 服务器 PSE 上的当前操作（Abort Current Operation）。

发送中止请求（Abort Request），取消当前正在进行的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `buf` | 包含可选中止头（Abort Headers）的缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga29d4e867858a96606a623313acc808d9"></a>

### `bt_pbap_pce_connect()`

```c
int bt_pbap_pce_connect ( struct bt_pbap_pce * pbap_pce, uint16_t mopl, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

建立从 PCE 客户端到 PSE 服务器的 PBAP 协议连接（Protocol Connection）。

在已建立的传输连接（Transport Connection）上发起 PBAP 协议连接。必须先使用 `bt_pbap_pce_rfcomm_connect` 或 `bt_pbap_pce_l2cap_connect` 连接传输层（RFCOMM 或 L2CAP）。

收到连接响应后，将调用 `bt_pbap_pce_cb` 中的 `connect` 回调。如果连接被拒绝，则调用该回调并传入错误响应码（Error Response Code）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP 电话簿客户端设备（Phone Book Client Equipment，PCE）对象，类型为 `bt_pbap_pce`；必须先连接传输层。 |
| `mopl` | 此连接的最大 OBEX 数据包长度（Maximum OBEX Packet Length）。 |
| `buf` | 包含连接请求头（Connection Request Headers）的缓冲区，应包含目标 UUID（Target UUID），还可包含认证质询（Authentication Challenge）、支持的特性（Supported Features）等。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gab326aadad5f12827f08f6525b7dc5458"></a>

### `bt_pbap_pce_create_pdu()`

```c
struct net_buf * bt_pbap_pce_create_pdu ( struct bt_pbap_pce * pbap_pce, struct net_buf_pool * pool )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从缓冲池（Pool）分配缓冲区，并为 PBAP PCE 预留头部空间（Headroom）。

为 PBAP 预留头部空间（Headroom）后，从给定缓冲池分配网络缓冲区。PBAP 通过 RFCOMM 连接时，预留空间包括 OBEX、RFCOMM、L2CAP 和 ACL 头；通过 L2CAP 连接时，包括 OBEX、L2CAP 和 ACL 头。这样可确保数据包符合底层传输的格式要求。如果 `pool` 为 `NULL`，则从默认缓冲池分配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | 将使用此缓冲区的 PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `pool` | 用于分配缓冲区的网络缓冲池（Network Buffer Pool）；为 `NULL` 时使用默认缓冲池。 |

**返回（Returns）**：返回值：指向新分配且已预留头部空间（Headroom）的缓冲区的指针；失败时为 `NULL`。

<a id="ga5af0c3016e948bc27df328432ffa9455"></a>

### `bt_pbap_pce_disconnect()`

```c
int bt_pbap_pce_disconnect ( struct bt_pbap_pce * pbap_pce, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从 PBAP 客户端 PCE 断开 PBAP 连接（Connection）。

通过发送 OBEX `DISCONNECT` 请求断开 PBAP 连接。收到响应时，会调用 `bt_pbap_pce_cb` 中的 `disconnect` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `buf` | 包含可选断开连接头（Disconnect Headers）的缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gae9506155e96d3f641ee928754439f579"></a>

### `bt_pbap_pce_l2cap_connect()`

```c
int bt_pbap_pce_l2cap_connect ( struct bt_conn * conn, struct bt_pbap_pce * pbap_pce, struct bt_pbap_pce_cb * cb, uint16_t psm )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

通过 L2CAP 传输（Transport）连接 PBAP PCE 客户端。

为 PBAP PCE 建立底层 L2CAP 传输连接（Transport Connection）。连接成功后调用 `l2cap_connected` 回调。传输连接建立后，调用 `bt_pbap_pce_connect` 建立 PBAP 协议连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接。 |
| `pbap_pce` | 要连接的 PBAP PCE 实例，类型为 `bt_pbap_pce`。 |
| `cb` | 用于处理 PBAP 事件的回调操作结构（Callback Operations Structure），类型为 `bt_pbap_pce_cb`。 |
| `psm` | 要连接的 L2CAP 协议／服务复用器（Protocol Service Multiplexer，PSM）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gad407918b6c075045339aecd55b70db21"></a>

### `bt_pbap_pce_l2cap_disconnect()`

```c
int bt_pbap_pce_l2cap_disconnect ( struct bt_pbap_pce * pbap_pce)
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

断开 PBAP PCE 的 L2CAP 传输（Transport）。

关闭底层 L2CAP 传输连接（Transport Connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | 要断开的 PBAP PCE 实例，类型为 `bt_pbap_pce`。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga07f8db1528fc15bed243fc5da787354f"></a>

### `bt_pbap_pce_pull_phone_book()`

```c
int bt_pbap_pce_pull_phone_book ( struct bt_pbap_pce * pbap_pce, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从 PBAP 服务器 PSE 拉取电话簿（Pull Phone Book）。

发送拉取电话簿（Pull Phone Book）命令，从电话簿服务器设备（Phone Book Server Equipment，PSE）获取完整的电话簿对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `buf` | 要发送的缓冲区。应包含：携带电话簿路径的名称头（Name），例如 `telecom/pb.vcf`；值为 `BT_PBAP_PULL_PHONE_BOOK_TYPE` 的类型头（Type）；可选的应用参数（Application Parameters），例如格式等。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gac1f07e0eb9b256010fdbcf29b71701c6"></a>

### `bt_pbap_pce_pull_vcard_entry()`

```c
int bt_pbap_pce_pull_vcard_entry ( struct bt_pbap_pce * pbap_pce, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从 PBAP 服务器 PSE 拉取指定 vCard 条目（Pull vCard Entry）。

发送请求，获取指定的电子名片条目（vCard Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `buf` | 缓冲区应包含：携带 vCard 条目名称的名称头（Name），例如 `0.vcf`；值为 `BT_PBAP_PULL_VCARD_ENTRY_TYPE` 的类型头（Type）；可选的应用参数（Application Parameters），例如属性选择器、格式等。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga71ba43da527c77f3eaf7d43ae5c22cae"></a>

### `bt_pbap_pce_pull_vcard_listing()`

```c
int bt_pbap_pce_pull_vcard_listing ( struct bt_pbap_pce * pbap_pce, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从 PBAP 服务器 PSE 拉取 vCard 列表（Pull vCard Listing）。

发送请求，从指定文件夹获取电子名片条目列表（vCard Listing）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `buf` | 缓冲区应包含：携带文件夹路径的名称头（Name）；值为 `BT_PBAP_PULL_VCARD_LISTING_TYPE` 的类型头（Type）；可选的应用参数（Application Parameters），例如搜索条件等。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga9fcd75bb18c48756dfa4695890662ab0"></a>

### `bt_pbap_pce_rfcomm_connect()`

```c
int bt_pbap_pce_rfcomm_connect ( struct bt_conn * conn, struct bt_pbap_pce * pbap_pce, struct bt_pbap_pce_cb * cb, uint8_t channel )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

电话簿客户端设备（PCE）通过 RFCOMM 传输连接电话簿服务器设备（PSE）。

为 PBAP PCE 建立底层 RFCOMM 传输连接（Transport Connection）。连接成功后调用 `rfcomm_connected` 回调。传输连接建立后，调用 `bt_pbap_pce_connect` 建立 PBAP 协议连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接。 |
| `pbap_pce` | 要连接的 PBAP PCE 实例，类型为 `bt_pbap_pce`。 |
| `cb` | 用于处理 PBAP 事件的回调操作结构（Callback Operations Structure），类型为 `bt_pbap_pce_cb`。 |
| `channel` | 要连接的 RFCOMM 服务器通道号（Server Channel Number）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaae2eac838c1b825f5d31d7073608e56d"></a>

### `bt_pbap_pce_rfcomm_disconnect()`

```c
int bt_pbap_pce_rfcomm_disconnect ( struct bt_pbap_pce * pbap_pce)
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

断开 PBAP PCE 的 RFCOMM 传输（Transport）。

关闭底层 RFCOMM 传输连接（Transport Connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | 要断开的 PBAP PCE 实例，类型为 `bt_pbap_pce`。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga15403745f42ba10ba1dd9552895e111d"></a>

### `bt_pbap_pce_set_phone_book()`

```c
int bt_pbap_pce_set_phone_book ( struct bt_pbap_pce * pbap_pce, uint8_t flags, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

设置 PBAP 服务器 PSE 上的当前电话簿（Current Phone Book）。

设置 PSE 上的当前电话簿（Current Phone Book）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `flags` | 导航标志（Navigation Flags）：`BT_PBAP_SET_PHONE_BOOK_FLAGS_UP` 表示进入父目录；`BT_PBAP_SET_PHONE_BOOK_FLAGS_DOWN_OR_ROOT` 表示进入子目录或根目录。 |
| `buf` | 包含可选名称头（Name Header）的缓冲区，该头携带文件夹名称。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga9766bda140034251ba3287bfa116f359"></a>

### `bt_pbap_pse_abort_rsp()`

```c
int bt_pbap_pse_abort_rsp ( struct bt_pbap_pse * pbap_pse, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从 PBAP PSE 发送中止响应（Abort Response）。

向 PCE 客户端的中止请求（Abort Request）发送响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `rsp_code` | 响应码（Response Code），类型为 `bt_pbap_rsp_code`，通常为 `BT_PBAP_RSP_CODE_SUCCESS`。 |
| `buf` | 包含可选响应头（Response Headers）的缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gac76cb47df9f747f222d7cdbe627d3ead"></a>

### `bt_pbap_pse_connect_rsp()`

```c
int bt_pbap_pse_connect_rsp ( struct bt_pbap_pse * pbap_pse, uint16_t mopl, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从 PBAP PSE 发送连接响应（Connect Response）。

向 PCE 客户端的连接请求（Connect Request）发送响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `mopl` | OBEX 数据包的最大长度。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 包含响应头（Response Headers）的缓冲区，应包含 `Who` 头、连接 ID 等。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gae26500d48fae5f26946ab7a4e261993c"></a>

### `bt_pbap_pse_create_pdu()`

```c
struct net_buf * bt_pbap_pse_create_pdu ( struct bt_pbap_pse * pbap_pse, struct net_buf_pool * pool )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从缓冲池（Pool）分配缓冲区，并为 PBAP PSE 预留头部空间（Headroom）。

为 PBAP 预留头部空间（Headroom）后，从给定缓冲池分配网络缓冲区。PBAP 通过 RFCOMM 连接时，预留空间包括 OBEX、RFCOMM、L2CAP 和 ACL 头；通过 L2CAP 连接时，包括 OBEX、L2CAP 和 ACL 头。这样可确保数据包符合底层传输的格式要求。如果 `pool` 为 `NULL`，则从默认缓冲池分配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | 将使用此缓冲区的 PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `pool` | 用于分配缓冲区的网络缓冲池（Network Buffer Pool）；为 `NULL` 时使用默认缓冲池。 |

**返回（Returns）**：返回值：指向新分配且已预留头部空间（Headroom）的缓冲区的指针；失败时为 `NULL`。

<a id="gafa7ebec6db37286b0ca54ed1d9f4ca02"></a>

### `bt_pbap_pse_disconnect_rsp()`

```c
int bt_pbap_pse_disconnect_rsp ( struct bt_pbap_pse * pbap_pse, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从 PBAP PSE 发送断开连接响应（Disconnect Response）。

向 PCE 客户端的断开连接请求（Disconnect Request）发送响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 包含可选响应头（Response Headers）的缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gab37e9ea163060e8b770da56e5a6415cb"></a>

### `bt_pbap_pse_l2cap_register()`

```c
int bt_pbap_pse_l2cap_register ( struct bt_pbap_pse_l2cap * server)
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

注册 PBAP PSE L2CAP 服务器（Server）。

注册监听传入 L2CAP 连接的 PBAP 服务器。系统会为该服务器分配一个 L2CAP PSM，该值应通过服务发现协议（SDP）发布。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | PBAP PSE 的 L2CAP 服务器结构，类型为 `bt_pbap_pse_l2cap`。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gac8ef77affecb5316991afca6c1005f62"></a>

### `bt_pbap_pse_pull_phone_book_rsp()`

```c
int bt_pbap_pse_pull_phone_book_rsp ( struct bt_pbap_pse * pbap_pse, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从 PBAP PSE 发送拉取电话簿响应（Pull Phone Book Response）。

向 PCE 客户端的拉取电话簿（Pull Phone Book）请求发送响应。对于较大的电话簿，可以先发送多个 `BT_PBAP_RSP_CODE_CONTINUE` 响应，再发送一个最终的 `BT_PBAP_RSP_CODE_SUCCESS` 响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gacdcbb62a6999c833e4e6d0846aad28d6"></a>

### `bt_pbap_pse_pull_vcard_entry_rsp()`

```c
int bt_pbap_pse_pull_vcard_entry_rsp ( struct bt_pbap_pse * pbap_pse, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从 PBAP PSE 发送拉取 vCard 条目响应（Pull vCard Entry Response）。

向 PCE 客户端的拉取电子名片条目（Pull vCard Entry）请求发送响应。对于较大的 vCard 条目，可以先发送多个 `BT_PBAP_RSP_CODE_CONTINUE` 响应，再发送一个最终的 `BT_PBAP_RSP_CODE_SUCCESS` 响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gac511c99ae0c2d0f391f5dbf150599390"></a>

### `bt_pbap_pse_pull_vcard_listing_rsp()`

```c
int bt_pbap_pse_pull_vcard_listing_rsp ( struct bt_pbap_pse * pbap_pse, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从 PBAP PSE 发送拉取 vCard 列表响应（Pull vCard Listing Response）。

向 PCE 客户端的拉取电子名片列表（Pull vCard Listing）请求发送响应。对于较大的列表，可以先发送多个 `BT_PBAP_RSP_CODE_CONTINUE` 响应，再发送一个最终的 `BT_PBAP_RSP_CODE_SUCCESS` 响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 包含响应头的缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga15c39f4afb996a37b43acd51cc82ed53"></a>

### `bt_pbap_pse_register()`

```c
int bt_pbap_pse_register ( struct bt_pbap_pse * pbap_pse, struct bt_pbap_pse_cb * cb )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

注册 PBAP PSE 实例（Instance）。

向 PBAP 子系统注册一个 PBAP PSE 实例。此操作初始化 PSE 对象，并将其与提供的回调结构关联，以处理 PBAP 服务器操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | 要注册的 PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `cb` | 用于处理 PSE 事件的回调操作结构（Callback Operations Structure），类型为 `bt_pbap_pse_cb`。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga72b9420a34975c9691690977169bcec6"></a>

### `bt_pbap_pse_rfcomm_register()`

```c
int bt_pbap_pse_rfcomm_register ( struct bt_pbap_pse_rfcomm * server)
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

注册 PBAP PSE RFCOMM 服务器（Server）。

注册监听传入 RFCOMM 连接的 PBAP 服务器。系统会为该服务器分配一个 RFCOMM 通道（Channel），该通道应通过服务发现协议（SDP）发布。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | PBAP PSE 的 RFCOMM 服务器结构，类型为 `bt_pbap_pse_rfcomm`。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga09e255e0c5328a1f1e7286b7100eeb61"></a>

### `bt_pbap_pse_set_phone_book_rsp()`

```c
int bt_pbap_pse_set_phone_book_rsp ( struct bt_pbap_pse * pbap_pse, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

从 PBAP PSE 发送设置电话簿响应（Set Phone Book Response）。

向 PCE 客户端的设置电话簿（Set Phone Book）请求发送响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pse` | PBAP PSE 对象，类型为 `bt_pbap_pse`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 包含可选响应头（Response Headers）的缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。


## 6.6\_原页交叉引用（Cross References）

- [bt_pbap_pce_cb](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md)
- [bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)
- [bt_pbap_pse_cb](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md)
- [bt_pbap_pse_rfcomm](../bluetooth_service_model_reference/P154_bt_pbap_pse_rfcomm_结构体.md)
- [bt_pbap_pse_l2cap](../bluetooth_service_model_reference/P153_bt_pbap_pse_l2cap_结构体.md)
- [bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)
- [BT_OBEX_SETPATH_FLAG_BACKUP](P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75)
- [BT_OBEX_SETPATH_FLAG_NO_CREATE](P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zephyr/bluetooth/classic/pbap.h](../api_file_flash_test_reference/P011_zephyr__bluetooth__classic__pbap.h_文件参考.md)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)
- [BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__uuid_html_gac3973b66e992cbc0940752b77b378f43"></a>
<a id="agroup__bt__uuid_html_gadece715e13e2a529aa55c298ff760bf0"></a>
<a id="astructbt__uuid__128_html"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga5cf30994d6344a67b22eb01baf863b1baf5f30663b6083d8c09950e71dc6e1e0b"></a>
<a id="gga5cf30994d6344a67b22eb01baf863b1ba0fa84dbd58771867b547805099689a3a"></a>
<a id="ggac6c48c5b202c19567a4ddb008626f174ab03a1c4e18ea46da6c28fe83a850b510"></a>
<a id="ggac6c48c5b202c19567a4ddb008626f174a59e2999c6d5af45b12c88d8bf78c7252"></a>
<a id="ggac6c48c5b202c19567a4ddb008626f174accbdbbf7c94a707b77c6b249760f37a1"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a9dc945e68284feb0c84c3f266b504e9a"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a4eccbde165789980859146504dc6ad79"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a095c248ed7a21c3024843b06c8757c65"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949abbf728e6870fb11e11095741261dce74"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949ab1029f770ff972cd56ca27149697b3c1"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a392c7a7f408f80443e330e7e8317790f"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a534c44365efffc777b134db0d7158d01"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949aba04655292e204ffea1ea8e6f868990a"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949ae97d497323807766a249a354d9c73440"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949aaedbb7e84f50781fa88eaff8859bf0c0"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a8eeef93a6fb6d1f90688444d4c025d75"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a2bd2e420601d0d8dfd6d308b48ab3cf5"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a5cb26f5f8d5baff7b2d28e030db326f1"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a2f7b5161e2440abaa4dbcaf4351f9dc8"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949af45314b48bb91277d8ad84d29e44ce54"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a8030f80cf155692c1728775885c0786b"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949ac94b5f034af49ba23222988ac05dca41"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a9e6232e6968a9604421a81a4d364e868"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949aa5acc89efeae0ef6fabbcdbc5c461cf0"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a07399ae04375a6c435f34815b734aabb"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a31e2f9be865df16c883964b8abaea828"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a0d8adde858f93c7d5b765fb0488f22ce"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a1c16e137b53c6c88152ed49d693dd32b"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a1622cc47e9c5d359d327b9175829b005"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a9b2cb462f56b4abbda146fc3b6e0250b"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a12d9060eef27b4c048064df7b00faf7f"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a728ddfce7f0f93564e6e657d3fd9f9ca"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a7cfcd8e622d1adb99c5ad598b2642720"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a6af54c454719c9a5baa75db6feb3c6e6"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949ad1b5c9ec39747786c90c89b190235b5e"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a1fe34f3b6c0a3c9ca0966106052faa61"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949a587cb6926e50eca38c633019312208d5"></a>
<a id="gga81e3d8885dddfae8f8e2714ef9173949ab98d31a99ac92b189b8963f275d6846b"></a>
<a id="ggadc3ace27caf970d0f2f8c8278e50c7fca99adb79a6d49413c2c3dc83ff4686e5d"></a>
<a id="ggafc697dd2db191451f1d2334f5758be69afb959ef0be8bd3e0e06eb26d8a186772"></a>
<a id="ggafc697dd2db191451f1d2334f5758be69a7c22ec68b0d24778b1a0677b31f335a3"></a>
<a id="ggafc697dd2db191451f1d2334f5758be69a7216e629be9047a08a48be8210c272bc"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0a32182e2f399ec292ea652dd7f04bbdee"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0a4a1bbc25a06c89dd948542ec700a7323"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0af4a5a102fc189ad256b75091522d1b66"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0aa17305107ed8979b917dab98f04442bf"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0a2cf69d5233c590f708571c2447539025"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0a7894ebcf543e20b5c3369ec6632fb9c9"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0ac9aade48ff6a95d27443f817daf6ba75"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0a0bc424753f8b1da0b3209c38925c6162"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0acc1b3f202aa38ff027a63aecb9108641"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0abea06880695df75ef9ca68e94e4596b4"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0a793e24d13b717616ee8eb09792d19310"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0aeac485e4bb2ca3d4fcdaf0e76fd55a08"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0a60027135eafa915cac55a1cc59d68b4f"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0acfbe210e7ef87a3a07b00f05b62f7616"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0a4eb10ced494b26ad1380f6808574716c"></a>
<a id="ggadbc19ba92332972e5d22e213c7618fa0a66bf205d11a351aa10fba0c6648600db"></a>
<a id="gga76ceaa735d7bc5ee97d665d497b896cda338230ca0c8d07ca4a5cced68cf9faf4"></a>
<a id="gga76ceaa735d7bc5ee97d665d497b896cda4f1435ad0230025a1bf612fd38df67a9"></a>
<a id="gga9d9697d62b6bdbbc4feb0cf4b9776b58a661acfbba2e792ee4444453650db00eb"></a>
<a id="gga9d9697d62b6bdbbc4feb0cf4b9776b58a904e13430e8318623f1a785b94caee93"></a>
<a id="gga9d9697d62b6bdbbc4feb0cf4b9776b58a26f8b1cb1f6bc983b1508b5a2e298a3e"></a>
<a id="gga9d9697d62b6bdbbc4feb0cf4b9776b58a3130502de3a9c28985692f8d93b6ad08"></a>
<a id="gga9d9697d62b6bdbbc4feb0cf4b9776b58a9f3978e6433273f9a1af3e0c91ae33cd"></a>
<a id="gga9d9697d62b6bdbbc4feb0cf4b9776b58a7cab8c591dca0bc0279c6463ece416d6"></a>
<a id="gga9d9697d62b6bdbbc4feb0cf4b9776b58a2f4a1259666bfbf84c8c8ac02faa8683"></a>
<a id="gga9d9697d62b6bdbbc4feb0cf4b9776b58a806a9638aa9ca07d52f2dbb6946b6594"></a>
<a id="gga9d9697d62b6bdbbc4feb0cf4b9776b58ab34bbcad2a7fe5c2b9f2efa511b69ccf"></a>
<a id="gga9d9697d62b6bdbbc4feb0cf4b9776b58aa0c1cbc8611c6a5f39d1d61858ea85cb"></a>
<a id="gga9d9697d62b6bdbbc4feb0cf4b9776b58a722cfbba810a0646a340d8bba82282fa"></a>
<a id="ggae51b98f9472a284aba377a0343a6335fadd13a4cd31cacd5a1ee3738f6514d7bf"></a>
<a id="ggae51b98f9472a284aba377a0343a6335faeba96c52f51b6bcf64cdab4826104603"></a>
<a id="ggae51b98f9472a284aba377a0343a6335faa77889b21608736c840c5870236b8b7f"></a>
<a id="ggae51b98f9472a284aba377a0343a6335fafcac813cc74198792f97e1eba6594a93"></a>
<a id="ggae51b98f9472a284aba377a0343a6335fa04a72163c9a4aa1ca94e096fc61c0110"></a>
<a id="ggae51b98f9472a284aba377a0343a6335fa09b908bca7982fc1818791c6ff2a9d54"></a>
<a id="ggae51b98f9472a284aba377a0343a6335fa208cd02d7acabf2f6444292d2f0290ec"></a>
<a id="ggae51b98f9472a284aba377a0343a6335faa9087f0238d221a036a599b2bcceee5e"></a>
<a id="ggae51b98f9472a284aba377a0343a6335faa7ab39682e0f35c54ff5e67c76b3741c"></a>
<a id="ggae51b98f9472a284aba377a0343a6335fa8f549e342b61b7bb4533eac1c4019a8f"></a>
<a id="ggadd0760a5999620762367a5dda62018b7a58a43511704fe46d8f8cdbb8d0e6f9fe"></a>
<a id="ggadd0760a5999620762367a5dda62018b7aaf5d738a116dd37e2bc18bec07858415"></a>
<a id="ggadd0760a5999620762367a5dda62018b7aa3f4d6139aad54ee40d60c9ab474dc48"></a>
<a id="ggadd0760a5999620762367a5dda62018b7adf8db04f430e9b19d75fd6396f6bf0f2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md) · [返回大纲](大纲.md) · [下一章](P007_增强串行外设接口（ESPI）.md)
