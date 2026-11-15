---
id: learning.zephyr-docs.api-file-flash-test-reference.page-11
title: zephyr__bluetooth__classic__pbap.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pbap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_bluetooth\_\_classic\_\_pbap.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pbap_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电话簿访问配置文件（Phone Book Access Profile）的处理。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <string.h>
#include <errno.h>
#include <stdbool.h>
#include <zephyr/bluetooth/classic/goep.h>
```

查看此文件的源码。

电话簿访问配置文件（Phone Book Access Profile）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

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

## 11.2\_宏定义（Macros）

<a id="r_ga73f1c2b754b4fc3afe2f8f2cb154469b"></a>

```c
#define BT_PBAP_UUID
```

相关声明：[BT_PBAP_UUID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga73f1c2b754b4fc3afe2f8f2cb154469b)。

用于服务标识（Service Identification）的 PBAP 目标 UUID（Target UUID）。

<a id="r_gad8dc6e92eba851f2a8c6111d8d22edcc"></a>

```c
#define BT_PBAP_PULL_PHONE_BOOK_TYPE "x-bt/phonebook"
```

相关声明：[BT_PBAP_PULL_PHONE_BOOK_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gad8dc6e92eba851f2a8c6111d8d22edcc)。

拉取电话簿操作（Pull Phone Book Operation）的 OBEX 类型头（Type Header）。

<a id="r_ga957dd1b14b50864ac9c4a057b3702dec"></a>

```c
#define BT_PBAP_PULL_VCARD_LISTING_TYPE "x-bt/vcard-listing"
```

相关声明：[BT_PBAP_PULL_VCARD_LISTING_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga957dd1b14b50864ac9c4a057b3702dec)。

拉取 vCard 列表操作（Pull vCard Listing Operation）的 OBEX 类型头（Type Header）。

<a id="r_gaac21da1879eed8074e5d01e315ea213a"></a>

```c
#define BT_PBAP_PULL_VCARD_ENTRY_TYPE "x-bt/vcard"
```

相关声明：[BT_PBAP_PULL_VCARD_ENTRY_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gaac21da1879eed8074e5d01e315ea213a)。

拉取 vCard 条目操作（Pull vCard Entry Operation）的 OBEX 类型头（Type Header）。

<a id="r_ga9602f26d0e3524e0a5f40a9854432e44"></a>

```c
#define BT_PBAP_SET_PHONE_BOOK_FLAGS_UP (BT_OBEX_SETPATH_FLAG_BACKUP | BT_OBEX_SETPATH_FLAG_NO_CREATE)
```

相关声明：[BT_PBAP_SET_PHONE_BOOK_FLAGS_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9602f26d0e3524e0a5f40a9854432e44)、[BT_OBEX_SETPATH_FLAG_BACKUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75)、[BT_OBEX_SETPATH_FLAG_NO_CREATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553)。

设置电话簿标志（Set Phone Book Flags）：向上导航到父目录（Parent Directory）。

<a id="r_ga66c979baa8aefbfab188d4c9017fac8b"></a>

```c
#define BT_PBAP_SET_PHONE_BOOK_FLAGS_DOWN_OR_ROOT BT_OBEX_SETPATH_FLAG_NO_CREATE
```

相关声明：[BT_PBAP_SET_PHONE_BOOK_FLAGS_DOWN_OR_ROOT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga66c979baa8aefbfab188d4c9017fac8b)、[BT_OBEX_SETPATH_FLAG_NO_CREATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553)。

设置电话簿标志（Set Phone Book Flags）：向下导航到子目录（Child Directory），或导航到根目录（Root）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.3\_枚举（Enumerations）

<a id="r_ga9d9697d62b6bdbbc4feb0cf4b9776b58"></a>

```c
enum bt_pbap_rsp_code { BT_PBAP_RSP_CODE_CONTINUE = BT_OBEX_RSP_CODE_CONTINUE , BT_PBAP_RSP_CODE_OK = BT_OBEX_RSP_CODE_OK , BT_PBAP_RSP_CODE_SUCCESS = BT_OBEX_RSP_CODE_SUCCESS , BT_PBAP_RSP_CODE_BAD_REQ = BT_OBEX_RSP_CODE_BAD_REQ , BT_PBAP_RSP_CODE_UNAUTH = BT_OBEX_RSP_CODE_UNAUTH , BT_PBAP_RSP_CODE_FORBIDDEN = BT_OBEX_RSP_CODE_FORBIDDEN , BT_PBAP_RSP_CODE_NOT_FOUND = BT_OBEX_RSP_CODE_NOT_FOUND , BT_PBAP_RSP_CODE_NOT_ACCEPT = BT_OBEX_RSP_CODE_NOT_ACCEPT , BT_PBAP_RSP_CODE_PRECON_FAIL = BT_OBEX_RSP_CODE_PRECON_FAIL , BT_PBAP_RSP_CODE_NOT_IMPL = BT_OBEX_RSP_CODE_NOT_IMPL , BT_PBAP_RSP_CODE_UNAVAIL = BT_OBEX_RSP_CODE_UNAVAIL }
```

相关声明：[bt_pbap_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9d9697d62b6bdbbc4feb0cf4b9776b58)、[BT_PBAP_RSP_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a661acfbba2e792ee4444453650db00eb)、[BT_PBAP_RSP_CODE_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a904e13430e8318623f1a785b94caee93)、[BT_PBAP_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a26f8b1cb1f6bc983b1508b5a2e298a3e)、[BT_PBAP_RSP_CODE_BAD_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a3130502de3a9c28985692f8d93b6ad08)、[BT_PBAP_RSP_CODE_UNAUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a9f3978e6433273f9a1af3e0c91ae33cd)、[BT_PBAP_RSP_CODE_FORBIDDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a7cab8c591dca0bc0279c6463ece416d6)、[BT_PBAP_RSP_CODE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a2f4a1259666bfbf84c8c8ac02faa8683)、[BT_PBAP_RSP_CODE_NOT_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a806a9638aa9ca07d52f2dbb6946b6594)、[BT_PBAP_RSP_CODE_PRECON_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58ab34bbcad2a7fe5c2b9f2efa511b69ccf)、[BT_PBAP_RSP_CODE_NOT_IMPL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58aa0c1cbc8611c6a5f39d1d61858ea85cb)、[BT_PBAP_RSP_CODE_UNAVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a722cfbba810a0646a340d8bba82282fa)。

PBAP 响应码（Response Codes）。

<a id="r_gac6c48c5b202c19567a4ddb008626f174"></a>

```c
enum bt_pbap_appl_param_order { BT_PBAP_APPL_PARAM_ORDER_INDEXED = 0x00 , BT_PBAP_APPL_PARAM_ORDER_ALPHABETICAL = 0x01 , BT_PBAP_APPL_PARAM_ORDER_PHONETIC = 0x02 }
```

相关声明：[bt_pbap_appl_param_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac6c48c5b202c19567a4ddb008626f174)、[BT_PBAP_APPL_PARAM_ORDER_INDEXED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggac6c48c5b202c19567a4ddb008626f174ab03a1c4e18ea46da6c28fe83a850b510)、[BT_PBAP_APPL_PARAM_ORDER_ALPHABETICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggac6c48c5b202c19567a4ddb008626f174a59e2999c6d5af45b12c88d8bf78c7252)、[BT_PBAP_APPL_PARAM_ORDER_PHONETIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggac6c48c5b202c19567a4ddb008626f174accbdbbf7c94a707b77c6b249760f37a1)。

PBAP 应用参数中 Order 参数的值（Parameter Values）。

<a id="r_gafc697dd2db191451f1d2334f5758be69"></a>

```c
enum bt_pbap_appl_param_search_property { BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NAME = 0x00 , BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NUMBER = 0x01 , BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_SOUND = 0x02 }
```

相关声明：[bt_pbap_appl_param_search_property](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gafc697dd2db191451f1d2334f5758be69)、[BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggafc697dd2db191451f1d2334f5758be69afb959ef0be8bd3e0e06eb26d8a186772)、[BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggafc697dd2db191451f1d2334f5758be69a7c22ec68b0d24778b1a0677b31f335a3)、[BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggafc697dd2db191451f1d2334f5758be69a7216e629be9047a08a48be8210c272bc)。

PBAP 应用参数中 Search Property 参数的值（Parameter Values）。

<a id="r_ga5cf30994d6344a67b22eb01baf863b1b"></a>

```c
enum bt_pbap_appl_param_format { BT_PBAP_APPL_PARAM_FORMAT_2_1 = 0x00 , BT_PBAP_APPL_PARAM_FORMAT_3_0 = 0x01 }
```

相关声明：[bt_pbap_appl_param_format](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga5cf30994d6344a67b22eb01baf863b1b)、[BT_PBAP_APPL_PARAM_FORMAT_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga5cf30994d6344a67b22eb01baf863b1baf5f30663b6083d8c09950e71dc6e1e0b)、[BT_PBAP_APPL_PARAM_FORMAT_3_0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga5cf30994d6344a67b22eb01baf863b1ba0fa84dbd58771867b547805099689a3a)。

PBAP 应用参数中 Format 参数的值（Parameter Values）。

<a id="r_ga76ceaa735d7bc5ee97d665d497b896cd"></a>

```c
enum bt_pbap_appl_param_vcard_selector_operator { BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_OR = 0x00 , BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_AND = 0x01 }
```

相关声明：[bt_pbap_appl_param_vcard_selector_operator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga76ceaa735d7bc5ee97d665d497b896cd)、[BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga76ceaa735d7bc5ee97d665d497b896cda338230ca0c8d07ca4a5cced68cf9faf4)、[BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_AND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga76ceaa735d7bc5ee97d665d497b896cda4f1435ad0230025a1bf612fd38df67a9)。

PBAP 应用参数中 vCard Selector Operator 参数的值（Parameter Values）。

<a id="r_gadc3ace27caf970d0f2f8c8278e50c7fc"></a>

```c
enum bt_pbap_appl_param_reset_new_missed_calls { BT_PBAP_APPL_PARAM_RESET_NEW_MISSED_CALLS = 0x01 }
```

相关声明：[bt_pbap_appl_param_reset_new_missed_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gadc3ace27caf970d0f2f8c8278e50c7fc)、[BT_PBAP_APPL_PARAM_RESET_NEW_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadc3ace27caf970d0f2f8c8278e50c7fca99adb79a6d49413c2c3dc83ff4686e5d)。

PBAP 应用参数中重置新增未接来电（Reset New Missed Calls）参数的值。

<a id="r_ga81e3d8885dddfae8f8e2714ef9173949"></a>

```c
enum bt_pbap_appl_param_property_mask { BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_VERSION = (1ULL << (0)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_FN = (1ULL << (1)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_N = (1ULL << (2)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PHOTO = (1ULL << (3)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_BDAY = (1ULL << (4)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ADR = (1ULL << (5)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LABEL = (1ULL << (6)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TEL = (1ULL << (7)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_EMAIL = (1ULL << (8)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_MAILER = (1ULL << (9)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TZ = (1ULL << (10)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_GEO = (1ULL << (11)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TITLE = (1ULL << (12)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ROLE = (1ULL << (13)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LOGO = (1ULL << (14)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_AGENT = (1ULL << (15)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ORG = (1ULL << (16)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NOTE = (1ULL << (17)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_REV = (1ULL << (18)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SOUND = (1ULL << (19)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_URL = (1ULL << (20)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_UID = (1ULL << (21)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_KEY = (1ULL << (22)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NICKNAME = (1ULL << (23)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CATEGORIES = (1ULL << (24)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PRODID = (1ULL << (25)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CLASS = (1ULL << (26)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SORT_STRING = (1ULL << (27)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_IRMC_CALL_DATETIME = (1ULL << (28)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_SPEEDDIALKEY = (1ULL << (29)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UCI = (1ULL << (30)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UID = (1ULL << (31)) , BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PROPRIETARY_FILTER = (1ULL << (39)) }
```

相关声明：[bt_pbap_appl_param_property_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga81e3d8885dddfae8f8e2714ef9173949)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a9dc945e68284feb0c84c3f266b504e9a)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_FN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a4eccbde165789980859146504dc6ad79)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_N](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a095c248ed7a21c3024843b06c8757c65)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PHOTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949abbf728e6870fb11e11095741261dce74)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_BDAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ab1029f770ff972cd56ca27149697b3c1)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ADR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a392c7a7f408f80443e330e7e8317790f)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LABEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a534c44365efffc777b134db0d7158d01)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949aba04655292e204ffea1ea8e6f868990a)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ae97d497323807766a249a354d9c73440)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_MAILER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949aaedbb7e84f50781fa88eaff8859bf0c0)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a8eeef93a6fb6d1f90688444d4c025d75)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_GEO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a2bd2e420601d0d8dfd6d308b48ab3cf5)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TITLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a5cb26f5f8d5baff7b2d28e030db326f1)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ROLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a2f7b5161e2440abaa4dbcaf4351f9dc8)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LOGO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949af45314b48bb91277d8ad84d29e44ce54)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_AGENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a8030f80cf155692c1728775885c0786b)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ORG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ac94b5f034af49ba23222988ac05dca41)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a9e6232e6968a9604421a81a4d364e868)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_REV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949aa5acc89efeae0ef6fabbcdbc5c461cf0)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a07399ae04375a6c435f34815b734aabb)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a31e2f9be865df16c883964b8abaea828)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_UID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a0d8adde858f93c7d5b765fb0488f22ce)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a1c16e137b53c6c88152ed49d693dd32b)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NICKNAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a1622cc47e9c5d359d327b9175829b005)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CATEGORIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a9b2cb462f56b4abbda146fc3b6e0250b)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PRODID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a12d9060eef27b4c048064df7b00faf7f)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a728ddfce7f0f93564e6e657d3fd9f9ca)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SORT_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a7cfcd8e622d1adb99c5ad598b2642720)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_IRMC_CALL_DATETIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a6af54c454719c9a5baa75db6feb3c6e6)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_SPEEDDIALKEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ad1b5c9ec39747786c90c89b190235b5e)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a1fe34f3b6c0a3c9ca0966106052faa61)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a587cb6926e50eca38c633019312208d5)、[BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PROPRIETARY_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ab98d31a99ac92b189b8963f275d6846b)。

PBAP 属性位掩码（Property Bitmask）。

<a id="r_gadbc19ba92332972e5d22e213c7618fa0"></a>

```c
enum bt_pbap_appl_param_tag_id { BT_PBAP_APPL_PARAM_TAG_ID_ORDER = 0x01 , BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_VALUE = 0x02 , BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_PROPERTY = 0x03 , BT_PBAP_APPL_PARAM_TAG_ID_MAX_LIST_COUNT = 0x04 , BT_PBAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET = 0x05 , BT_PBAP_APPL_PARAM_TAG_ID_PROPERTY_SELECTOR = 0x06 , BT_PBAP_APPL_PARAM_TAG_ID_FORMAT = 0x07 , BT_PBAP_APPL_PARAM_TAG_ID_PHONEBOOK_SIZE = 0x08 , BT_PBAP_APPL_PARAM_TAG_ID_NEW_MISSED_CALLS = 0x09 , BT_PBAP_APPL_PARAM_TAG_ID_PRIMARY_FOLDER_VERSION = 0x0a , BT_PBAP_APPL_PARAM_TAG_ID_SECONDARY_FOLDER_VERSION = 0x0b , BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR = 0x0c , BT_PBAP_APPL_PARAM_TAG_ID_DATABASE_IDENTIFIER = 0x0d , BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR_OPERATOR = 0x0e , BT_PBAP_APPL_PARAM_TAG_ID_RESET_NEW_MISSED_CALLS = 0x0f , BT_PBAP_APPL_PARAM_TAG_ID_SUPPORTED_FEATURES = 0x10 }
```

相关声明：[bt_pbap_appl_param_tag_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gadbc19ba92332972e5d22e213c7618fa0)、[BT_PBAP_APPL_PARAM_TAG_ID_ORDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a32182e2f399ec292ea652dd7f04bbdee)、[BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a4a1bbc25a06c89dd948542ec700a7323)、[BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_PROPERTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0af4a5a102fc189ad256b75091522d1b66)、[BT_PBAP_APPL_PARAM_TAG_ID_MAX_LIST_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0aa17305107ed8979b917dab98f04442bf)、[BT_PBAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a2cf69d5233c590f708571c2447539025)、[BT_PBAP_APPL_PARAM_TAG_ID_PROPERTY_SELECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a7894ebcf543e20b5c3369ec6632fb9c9)、[BT_PBAP_APPL_PARAM_TAG_ID_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0ac9aade48ff6a95d27443f817daf6ba75)、[BT_PBAP_APPL_PARAM_TAG_ID_PHONEBOOK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a0bc424753f8b1da0b3209c38925c6162)、[BT_PBAP_APPL_PARAM_TAG_ID_NEW_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0acc1b3f202aa38ff027a63aecb9108641)、[BT_PBAP_APPL_PARAM_TAG_ID_PRIMARY_FOLDER_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0abea06880695df75ef9ca68e94e4596b4)、[BT_PBAP_APPL_PARAM_TAG_ID_SECONDARY_FOLDER_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a793e24d13b717616ee8eb09792d19310)、[BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0aeac485e4bb2ca3d4fcdaf0e76fd55a08)、[BT_PBAP_APPL_PARAM_TAG_ID_DATABASE_IDENTIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a60027135eafa915cac55a1cc59d68b4f)、[BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR_OPERATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0acfbe210e7ef87a3a07b00f05b62f7616)、[BT_PBAP_APPL_PARAM_TAG_ID_RESET_NEW_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a4eb10ced494b26ad1380f6808574716c)、[BT_PBAP_APPL_PARAM_TAG_ID_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a66bf205d11a351aa10fba0c6648600db)。

PBAP 应用参数标签标识符（Application Parameter Tag IDs）。

<a id="r_gae51b98f9472a284aba377a0343a6335f"></a>

```c
enum bt_pbap_supported_feature { BT_PBAP_SUPPORTED_FEATURE_DOWNLOAD = (1UL << (0)) , BT_PBAP_SUPPORTED_FEATURE_BROWSING = (1UL << (1)) , BT_PBAP_SUPPORTED_FEATURE_DATABASE_IDENTIFIER = (1UL << (2)) , BT_PBAP_SUPPORTED_FEATURE_FOLDER_VERSION_COUNTERS = (1UL << (3)) , BT_PBAP_SUPPORTED_FEATURE_VCARD_SELECTOR = (1UL << (4)) , BT_PBAP_SUPPORTED_FEATURE_ENHANCED_MISSED_CALLS = (1UL << (5)) , BT_PBAP_SUPPORTED_FEATURE_UCI_VCARD_PROPERTY = (1UL << (6)) , BT_PBAP_SUPPORTED_FEATURE_UID_VCARD_PROPERTY = (1UL << (7)) , BT_PBAP_SUPPORTED_FEATURE_CONTACT_REFERENCING = (1UL << (8)) , BT_PBAP_SUPPORTED_FEATURE_DEFAULT_CONTACT_IMAGE = (1UL << (9)) }
```

相关声明：[bt_pbap_supported_feature](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gae51b98f9472a284aba377a0343a6335f)、[BT_PBAP_SUPPORTED_FEATURE_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fadd13a4cd31cacd5a1ee3738f6514d7bf)、[BT_PBAP_SUPPORTED_FEATURE_BROWSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faeba96c52f51b6bcf64cdab4826104603)、[BT_PBAP_SUPPORTED_FEATURE_DATABASE_IDENTIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faa77889b21608736c840c5870236b8b7f)、[BT_PBAP_SUPPORTED_FEATURE_FOLDER_VERSION_COUNTERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fafcac813cc74198792f97e1eba6594a93)、[BT_PBAP_SUPPORTED_FEATURE_VCARD_SELECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa04a72163c9a4aa1ca94e096fc61c0110)、[BT_PBAP_SUPPORTED_FEATURE_ENHANCED_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa09b908bca7982fc1818791c6ff2a9d54)、[BT_PBAP_SUPPORTED_FEATURE_UCI_VCARD_PROPERTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa208cd02d7acabf2f6444292d2f0290ec)、[BT_PBAP_SUPPORTED_FEATURE_UID_VCARD_PROPERTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faa9087f0238d221a036a599b2bcceee5e)、[BT_PBAP_SUPPORTED_FEATURE_CONTACT_REFERENCING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faa7ab39682e0f35c54ff5e67c76b3741c)、[BT_PBAP_SUPPORTED_FEATURE_DEFAULT_CONTACT_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa8f549e342b61b7bb4533eac1c4019a8f)。

PBAP 支持的特性位掩码（Supported Features Bitmask）。

<a id="r_gadd0760a5999620762367a5dda62018b7"></a>

```c
enum bt_pbap_supported_repositories { BT_PBAP_SUPPORTED_REPOSITORIES_LOCAL_PHONE_BOOK = (1UL << (0)) , BT_PBAP_SUPPORTED_REPOSITORIES_SIM = (1UL << (1)) , BT_PBAP_SUPPORTED_REPOSITORIES_SPEED_DIAL = (1UL << (2)) , BT_PBAP_SUPPORTED_REPOSITORIES_FAVORITES = (1UL << (3)) }
```

相关声明：[bt_pbap_supported_repositories](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gadd0760a5999620762367a5dda62018b7)、[BT_PBAP_SUPPORTED_REPOSITORIES_LOCAL_PHONE_BOOK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7a58a43511704fe46d8f8cdbb8d0e6f9fe)、[BT_PBAP_SUPPORTED_REPOSITORIES_SIM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7aaf5d738a116dd37e2bc18bec07858415)、[BT_PBAP_SUPPORTED_REPOSITORIES_SPEED_DIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7aa3f4d6139aad54ee40d60c9ab474dc48)、[BT_PBAP_SUPPORTED_REPOSITORIES_FAVORITES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7adf8db04f430e9b19d75fd6396f6bf0f2)。

PBAP 支持的资料库位掩码（Supported Repositories Bitmask）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.4\_函数（Functions）

<a id="r_ga9fcd75bb18c48756dfa4695890662ab0"></a>

```c
int bt_pbap_pce_rfcomm_connect (struct bt_conn *conn, struct bt_pbap_pce *pbap_pce, struct bt_pbap_pce_cb *cb, uint8_t channel)
```

相关声明：[bt_pbap_pce_rfcomm_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9fcd75bb18c48756dfa4695890662ab0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[bt_pbap_pce_cb](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

电话簿客户端设备（PCE）通过 RFCOMM 传输连接电话簿服务器设备（PSE）。

<a id="r_gaae2eac838c1b825f5d31d7073608e56d"></a>

```c
int bt_pbap_pce_rfcomm_disconnect (struct bt_pbap_pce *pbap_pce)
```

相关声明：[bt_pbap_pce_rfcomm_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gaae2eac838c1b825f5d31d7073608e56d)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)。

断开 PBAP PCE 的 RFCOMM 传输（Transport）。

<a id="r_gae9506155e96d3f641ee928754439f579"></a>

```c
int bt_pbap_pce_l2cap_connect (struct bt_conn *conn, struct bt_pbap_pce *pbap_pce, struct bt_pbap_pce_cb *cb, uint16_t psm)
```

相关声明：[bt_pbap_pce_l2cap_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gae9506155e96d3f641ee928754439f579)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[bt_pbap_pce_cb](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 L2CAP 传输（Transport）连接 PBAP PCE 客户端。

<a id="r_gad407918b6c075045339aecd55b70db21"></a>

```c
int bt_pbap_pce_l2cap_disconnect (struct bt_pbap_pce *pbap_pce)
```

相关声明：[bt_pbap_pce_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gad407918b6c075045339aecd55b70db21)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)。

断开 PBAP PCE 的 L2CAP 传输（Transport）。

<a id="r_gab326aadad5f12827f08f6525b7dc5458"></a>

```c
struct net_buf * bt_pbap_pce_create_pdu (struct bt_pbap_pce *pbap_pce, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_pbap_pce_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gab326aadad5f12827f08f6525b7dc5458)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

从缓冲池（Pool）分配缓冲区，并为 PBAP PCE 预留头部空间（Headroom）。

<a id="r_ga29d4e867858a96606a623313acc808d9"></a>

```c
int bt_pbap_pce_connect (struct bt_pbap_pce *pbap_pce, uint16_t mopl, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga29d4e867858a96606a623313acc808d9)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

建立从 PCE 客户端到 PSE 服务器的 PBAP 协议连接（Protocol Connection）。

<a id="r_ga5af0c3016e948bc27df328432ffa9455"></a>

```c
int bt_pbap_pce_disconnect (struct bt_pbap_pce *pbap_pce, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga5af0c3016e948bc27df328432ffa9455)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP 客户端 PCE 断开 PBAP 连接（Connection）。

<a id="r_ga07f8db1528fc15bed243fc5da787354f"></a>

```c
int bt_pbap_pce_pull_phone_book (struct bt_pbap_pce *pbap_pce, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_pull_phone_book](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga07f8db1528fc15bed243fc5da787354f)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP 服务器 PSE 拉取电话簿（Pull Phone Book）。

<a id="r_ga71ba43da527c77f3eaf7d43ae5c22cae"></a>

```c
int bt_pbap_pce_pull_vcard_listing (struct bt_pbap_pce *pbap_pce, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_pull_vcard_listing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga71ba43da527c77f3eaf7d43ae5c22cae)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP 服务器 PSE 拉取 vCard 列表（Pull vCard Listing）。

<a id="r_gac1f07e0eb9b256010fdbcf29b71701c6"></a>

```c
int bt_pbap_pce_pull_vcard_entry (struct bt_pbap_pce *pbap_pce, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_pull_vcard_entry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac1f07e0eb9b256010fdbcf29b71701c6)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP 服务器 PSE 拉取指定 vCard 条目（Pull vCard Entry）。

<a id="r_ga15403745f42ba10ba1dd9552895e111d"></a>

```c
int bt_pbap_pce_set_phone_book (struct bt_pbap_pce *pbap_pce, uint8_t flags, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_set_phone_book](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga15403745f42ba10ba1dd9552895e111d)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

设置 PBAP 服务器 PSE 上的当前电话簿（Current Phone Book）。

<a id="r_gab24a2cb71edfa1d5e59c33fabc01c7d9"></a>

```c
int bt_pbap_pce_abort (struct bt_pbap_pce *pbap_pce, struct net_buf *buf)
```

相关声明：[bt_pbap_pce_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gab24a2cb71edfa1d5e59c33fabc01c7d9)、[bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

中止 PBAP 服务器 PSE 上的当前操作（Abort Current Operation）。

<a id="r_gae26500d48fae5f26946ab7a4e261993c"></a>

```c
struct net_buf * bt_pbap_pse_create_pdu (struct bt_pbap_pse *pbap_pse, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_pbap_pse_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gae26500d48fae5f26946ab7a4e261993c)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

从缓冲池（Pool）分配缓冲区，并为 PBAP PSE 预留头部空间（Headroom）。

<a id="r_ga72b9420a34975c9691690977169bcec6"></a>

```c
int bt_pbap_pse_rfcomm_register (struct bt_pbap_pse_rfcomm *server)
```

相关声明：[bt_pbap_pse_rfcomm_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga72b9420a34975c9691690977169bcec6)、[bt_pbap_pse_rfcomm](../bluetooth_service_model_reference/P154_bt_pbap_pse_rfcomm_结构体.md)。

注册 PBAP PSE RFCOMM 服务器（Server）。

<a id="r_gab37e9ea163060e8b770da56e5a6415cb"></a>

```c
int bt_pbap_pse_l2cap_register (struct bt_pbap_pse_l2cap *server)
```

相关声明：[bt_pbap_pse_l2cap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gab37e9ea163060e8b770da56e5a6415cb)、[bt_pbap_pse_l2cap](../bluetooth_service_model_reference/P153_bt_pbap_pse_l2cap_结构体.md)。

注册 PBAP PSE L2CAP 服务器（Server）。

<a id="r_ga15c39f4afb996a37b43acd51cc82ed53"></a>

```c
int bt_pbap_pse_register (struct bt_pbap_pse *pbap_pse, struct bt_pbap_pse_cb *cb)
```

相关声明：[bt_pbap_pse_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga15c39f4afb996a37b43acd51cc82ed53)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[bt_pbap_pse_cb](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md)。

注册 PBAP PSE 实例（Instance）。

<a id="r_gac76cb47df9f747f222d7cdbe627d3ead"></a>

```c
int bt_pbap_pse_connect_rsp (struct bt_pbap_pse *pbap_pse, uint16_t mopl, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_connect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac76cb47df9f747f222d7cdbe627d3ead)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送连接响应（Connect Response）。

<a id="r_gafa7ebec6db37286b0ca54ed1d9f4ca02"></a>

```c
int bt_pbap_pse_disconnect_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_disconnect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gafa7ebec6db37286b0ca54ed1d9f4ca02)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送断开连接响应（Disconnect Response）。

<a id="r_gac8ef77affecb5316991afca6c1005f62"></a>

```c
int bt_pbap_pse_pull_phone_book_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_pull_phone_book_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac8ef77affecb5316991afca6c1005f62)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送拉取电话簿响应（Pull Phone Book Response）。

<a id="r_gac511c99ae0c2d0f391f5dbf150599390"></a>

```c
int bt_pbap_pse_pull_vcard_listing_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_pull_vcard_listing_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac511c99ae0c2d0f391f5dbf150599390)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送拉取 vCard 列表响应（Pull vCard Listing Response）。

<a id="r_gacdcbb62a6999c833e4e6d0846aad28d6"></a>

```c
int bt_pbap_pse_pull_vcard_entry_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_pull_vcard_entry_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gacdcbb62a6999c833e4e6d0846aad28d6)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送拉取 vCard 条目响应（Pull vCard Entry Response）。

<a id="r_ga09e255e0c5328a1f1e7286b7100eeb61"></a>

```c
int bt_pbap_pse_set_phone_book_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_set_phone_book_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga09e255e0c5328a1f1e7286b7100eeb61)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送设置电话簿响应（Set Phone Book Response）。

<a id="r_ga9766bda140034251ba3287bfa116f359"></a>

```c
int bt_pbap_pse_abort_rsp (struct bt_pbap_pse *pbap_pse, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_pbap_pse_abort_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9766bda140034251ba3287bfa116f359)、[bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 PBAP PSE 发送中止响应（Abort Response）。


## 11.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/bluetooth/classic/goep.h](../api_source_supplement_reference/P081_goep.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P644_pbap.h_源码浏览.md)
- [bt_pbap_pce_cb](../bluetooth_service_model_reference/P150_bt_pbap_pce_cb_结构体.md)
- [bt_pbap_pce](../bluetooth_service_model_reference/P149_bt_pbap_pce_结构体.md)
- [bt_pbap_pse_cb](../bluetooth_service_model_reference/P152_bt_pbap_pse_cb_结构体.md)
- [bt_pbap_pse_rfcomm](../bluetooth_service_model_reference/P154_bt_pbap_pse_rfcomm_结构体.md)
- [bt_pbap_pse_l2cap](../bluetooth_service_model_reference/P153_bt_pbap_pse_l2cap_结构体.md)
- [bt_pbap_pse](../bluetooth_service_model_reference/P151_bt_pbap_pse_结构体.md)
- [BT_PBAP_UUID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga73f1c2b754b4fc3afe2f8f2cb154469b)
- [BT_PBAP_PULL_PHONE_BOOK_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gad8dc6e92eba851f2a8c6111d8d22edcc)
- [BT_PBAP_PULL_VCARD_LISTING_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga957dd1b14b50864ac9c4a057b3702dec)
- [BT_PBAP_PULL_VCARD_ENTRY_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gaac21da1879eed8074e5d01e315ea213a)
- [BT_PBAP_SET_PHONE_BOOK_FLAGS_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9602f26d0e3524e0a5f40a9854432e44)
- [BT_OBEX_SETPATH_FLAG_BACKUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483a9f89d8219783650a02e8ceb3faf6bd75)
- [BT_OBEX_SETPATH_FLAG_NO_CREATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ggab5f7e6a6c7503f97a851f48c70162483ae47e6f7c5a8da44615e7245c5e1cd553)
- [BT_PBAP_SET_PHONE_BOOK_FLAGS_DOWN_OR_ROOT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga66c979baa8aefbfab188d4c9017fac8b)
- [bt_pbap_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9d9697d62b6bdbbc4feb0cf4b9776b58)
- [BT_PBAP_RSP_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a661acfbba2e792ee4444453650db00eb)
- [BT_PBAP_RSP_CODE_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a904e13430e8318623f1a785b94caee93)
- [BT_PBAP_RSP_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a26f8b1cb1f6bc983b1508b5a2e298a3e)
- [BT_PBAP_RSP_CODE_BAD_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a3130502de3a9c28985692f8d93b6ad08)
- [BT_PBAP_RSP_CODE_UNAUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a9f3978e6433273f9a1af3e0c91ae33cd)
- [BT_PBAP_RSP_CODE_FORBIDDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a7cab8c591dca0bc0279c6463ece416d6)
- [BT_PBAP_RSP_CODE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a2f4a1259666bfbf84c8c8ac02faa8683)
- [BT_PBAP_RSP_CODE_NOT_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a806a9638aa9ca07d52f2dbb6946b6594)
- [BT_PBAP_RSP_CODE_PRECON_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58ab34bbcad2a7fe5c2b9f2efa511b69ccf)
- [BT_PBAP_RSP_CODE_NOT_IMPL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58aa0c1cbc8611c6a5f39d1d61858ea85cb)
- [BT_PBAP_RSP_CODE_UNAVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga9d9697d62b6bdbbc4feb0cf4b9776b58a722cfbba810a0646a340d8bba82282fa)
- [bt_pbap_appl_param_order](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac6c48c5b202c19567a4ddb008626f174)
- [BT_PBAP_APPL_PARAM_ORDER_INDEXED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggac6c48c5b202c19567a4ddb008626f174ab03a1c4e18ea46da6c28fe83a850b510)
- [BT_PBAP_APPL_PARAM_ORDER_ALPHABETICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggac6c48c5b202c19567a4ddb008626f174a59e2999c6d5af45b12c88d8bf78c7252)
- [BT_PBAP_APPL_PARAM_ORDER_PHONETIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggac6c48c5b202c19567a4ddb008626f174accbdbbf7c94a707b77c6b249760f37a1)
- [bt_pbap_appl_param_search_property](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gafc697dd2db191451f1d2334f5758be69)
- [BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggafc697dd2db191451f1d2334f5758be69afb959ef0be8bd3e0e06eb26d8a186772)
- [BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggafc697dd2db191451f1d2334f5758be69a7c22ec68b0d24778b1a0677b31f335a3)
- [BT_PBAP_APPL_PARAM_SEARCH_PROPERTY_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggafc697dd2db191451f1d2334f5758be69a7216e629be9047a08a48be8210c272bc)
- [bt_pbap_appl_param_format](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga5cf30994d6344a67b22eb01baf863b1b)
- [BT_PBAP_APPL_PARAM_FORMAT_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga5cf30994d6344a67b22eb01baf863b1baf5f30663b6083d8c09950e71dc6e1e0b)
- [BT_PBAP_APPL_PARAM_FORMAT_3_0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga5cf30994d6344a67b22eb01baf863b1ba0fa84dbd58771867b547805099689a3a)
- [bt_pbap_appl_param_vcard_selector_operator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga76ceaa735d7bc5ee97d665d497b896cd)
- [BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga76ceaa735d7bc5ee97d665d497b896cda338230ca0c8d07ca4a5cced68cf9faf4)
- [BT_PBAP_APPL_PARAM_VCARD_SELECTOR_OPERATOR_AND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga76ceaa735d7bc5ee97d665d497b896cda4f1435ad0230025a1bf612fd38df67a9)
- [bt_pbap_appl_param_reset_new_missed_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gadc3ace27caf970d0f2f8c8278e50c7fc)
- [BT_PBAP_APPL_PARAM_RESET_NEW_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadc3ace27caf970d0f2f8c8278e50c7fca99adb79a6d49413c2c3dc83ff4686e5d)
- [bt_pbap_appl_param_property_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga81e3d8885dddfae8f8e2714ef9173949)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a9dc945e68284feb0c84c3f266b504e9a)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_FN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a4eccbde165789980859146504dc6ad79)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_N](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a095c248ed7a21c3024843b06c8757c65)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PHOTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949abbf728e6870fb11e11095741261dce74)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_BDAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ab1029f770ff972cd56ca27149697b3c1)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ADR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a392c7a7f408f80443e330e7e8317790f)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LABEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a534c44365efffc777b134db0d7158d01)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949aba04655292e204ffea1ea8e6f868990a)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ae97d497323807766a249a354d9c73440)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_MAILER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949aaedbb7e84f50781fa88eaff8859bf0c0)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a8eeef93a6fb6d1f90688444d4c025d75)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_GEO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a2bd2e420601d0d8dfd6d308b48ab3cf5)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_TITLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a5cb26f5f8d5baff7b2d28e030db326f1)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ROLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a2f7b5161e2440abaa4dbcaf4351f9dc8)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_LOGO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949af45314b48bb91277d8ad84d29e44ce54)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_AGENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a8030f80cf155692c1728775885c0786b)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_ORG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ac94b5f034af49ba23222988ac05dca41)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a9e6232e6968a9604421a81a4d364e868)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_REV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949aa5acc89efeae0ef6fabbcdbc5c461cf0)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a07399ae04375a6c435f34815b734aabb)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_URL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a31e2f9be865df16c883964b8abaea828)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_UID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a0d8adde858f93c7d5b765fb0488f22ce)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a1c16e137b53c6c88152ed49d693dd32b)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_NICKNAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a1622cc47e9c5d359d327b9175829b005)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CATEGORIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a9b2cb462f56b4abbda146fc3b6e0250b)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PRODID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a12d9060eef27b4c048064df7b00faf7f)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a728ddfce7f0f93564e6e657d3fd9f9ca)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_SORT_STRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a7cfcd8e622d1adb99c5ad598b2642720)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_IRMC_CALL_DATETIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a6af54c454719c9a5baa75db6feb3c6e6)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_SPEEDDIALKEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ad1b5c9ec39747786c90c89b190235b5e)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a1fe34f3b6c0a3c9ca0966106052faa61)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_X_BT_UID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949a587cb6926e50eca38c633019312208d5)
- [BT_PBAP_APPL_PARAM_PROPERTY_SELECTOR_PROPRIETARY_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gga81e3d8885dddfae8f8e2714ef9173949ab98d31a99ac92b189b8963f275d6846b)
- [bt_pbap_appl_param_tag_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gadbc19ba92332972e5d22e213c7618fa0)
- [BT_PBAP_APPL_PARAM_TAG_ID_ORDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a32182e2f399ec292ea652dd7f04bbdee)
- [BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a4a1bbc25a06c89dd948542ec700a7323)
- [BT_PBAP_APPL_PARAM_TAG_ID_SEARCH_PROPERTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0af4a5a102fc189ad256b75091522d1b66)
- [BT_PBAP_APPL_PARAM_TAG_ID_MAX_LIST_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0aa17305107ed8979b917dab98f04442bf)
- [BT_PBAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a2cf69d5233c590f708571c2447539025)
- [BT_PBAP_APPL_PARAM_TAG_ID_PROPERTY_SELECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a7894ebcf543e20b5c3369ec6632fb9c9)
- [BT_PBAP_APPL_PARAM_TAG_ID_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0ac9aade48ff6a95d27443f817daf6ba75)
- [BT_PBAP_APPL_PARAM_TAG_ID_PHONEBOOK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a0bc424753f8b1da0b3209c38925c6162)
- [BT_PBAP_APPL_PARAM_TAG_ID_NEW_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0acc1b3f202aa38ff027a63aecb9108641)
- [BT_PBAP_APPL_PARAM_TAG_ID_PRIMARY_FOLDER_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0abea06880695df75ef9ca68e94e4596b4)
- [BT_PBAP_APPL_PARAM_TAG_ID_SECONDARY_FOLDER_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a793e24d13b717616ee8eb09792d19310)
- [BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0aeac485e4bb2ca3d4fcdaf0e76fd55a08)
- [BT_PBAP_APPL_PARAM_TAG_ID_DATABASE_IDENTIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a60027135eafa915cac55a1cc59d68b4f)
- [BT_PBAP_APPL_PARAM_TAG_ID_VCARD_SELECTOR_OPERATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0acfbe210e7ef87a3a07b00f05b62f7616)
- [BT_PBAP_APPL_PARAM_TAG_ID_RESET_NEW_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a4eb10ced494b26ad1380f6808574716c)
- [BT_PBAP_APPL_PARAM_TAG_ID_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadbc19ba92332972e5d22e213c7618fa0a66bf205d11a351aa10fba0c6648600db)
- [bt_pbap_supported_feature](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gae51b98f9472a284aba377a0343a6335f)
- [BT_PBAP_SUPPORTED_FEATURE_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fadd13a4cd31cacd5a1ee3738f6514d7bf)
- [BT_PBAP_SUPPORTED_FEATURE_BROWSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faeba96c52f51b6bcf64cdab4826104603)
- [BT_PBAP_SUPPORTED_FEATURE_DATABASE_IDENTIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faa77889b21608736c840c5870236b8b7f)
- [BT_PBAP_SUPPORTED_FEATURE_FOLDER_VERSION_COUNTERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fafcac813cc74198792f97e1eba6594a93)
- [BT_PBAP_SUPPORTED_FEATURE_VCARD_SELECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa04a72163c9a4aa1ca94e096fc61c0110)
- [BT_PBAP_SUPPORTED_FEATURE_ENHANCED_MISSED_CALLS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa09b908bca7982fc1818791c6ff2a9d54)
- [BT_PBAP_SUPPORTED_FEATURE_UCI_VCARD_PROPERTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa208cd02d7acabf2f6444292d2f0290ec)
- [BT_PBAP_SUPPORTED_FEATURE_UID_VCARD_PROPERTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faa9087f0238d221a036a599b2bcceee5e)
- [BT_PBAP_SUPPORTED_FEATURE_CONTACT_REFERENCING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335faa7ab39682e0f35c54ff5e67c76b3741c)
- [BT_PBAP_SUPPORTED_FEATURE_DEFAULT_CONTACT_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggae51b98f9472a284aba377a0343a6335fa8f549e342b61b7bb4533eac1c4019a8f)
- [bt_pbap_supported_repositories](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gadd0760a5999620762367a5dda62018b7)
- [BT_PBAP_SUPPORTED_REPOSITORIES_LOCAL_PHONE_BOOK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7a58a43511704fe46d8f8cdbb8d0e6f9fe)
- [BT_PBAP_SUPPORTED_REPOSITORIES_SIM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7aaf5d738a116dd37e2bc18bec07858415)
- [BT_PBAP_SUPPORTED_REPOSITORIES_SPEED_DIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7aa3f4d6139aad54ee40d60c9ab474dc48)
- [BT_PBAP_SUPPORTED_REPOSITORIES_FAVORITES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ggadd0760a5999620762367a5dda62018b7adf8db04f430e9b19d75fd6396f6bf0f2)
- [bt_pbap_pce_rfcomm_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9fcd75bb18c48756dfa4695890662ab0)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_pbap_pce_rfcomm_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gaae2eac838c1b825f5d31d7073608e56d)
- [bt_pbap_pce_l2cap_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gae9506155e96d3f641ee928754439f579)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_pbap_pce_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gad407918b6c075045339aecd55b70db21)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_pbap_pce_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gab326aadad5f12827f08f6525b7dc5458)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bt_pbap_pce_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga29d4e867858a96606a623313acc808d9)
- [bt_pbap_pce_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga5af0c3016e948bc27df328432ffa9455)
- [bt_pbap_pce_pull_phone_book](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga07f8db1528fc15bed243fc5da787354f)
- [bt_pbap_pce_pull_vcard_listing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga71ba43da527c77f3eaf7d43ae5c22cae)
- [bt_pbap_pce_pull_vcard_entry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac1f07e0eb9b256010fdbcf29b71701c6)
- [bt_pbap_pce_set_phone_book](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga15403745f42ba10ba1dd9552895e111d)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_pbap_pce_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gab24a2cb71edfa1d5e59c33fabc01c7d9)
- [bt_pbap_pse_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gae26500d48fae5f26946ab7a4e261993c)
- [bt_pbap_pse_rfcomm_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga72b9420a34975c9691690977169bcec6)
- [bt_pbap_pse_l2cap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gab37e9ea163060e8b770da56e5a6415cb)
- [bt_pbap_pse_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga15c39f4afb996a37b43acd51cc82ed53)
- [bt_pbap_pse_connect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac76cb47df9f747f222d7cdbe627d3ead)
- [bt_pbap_pse_disconnect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gafa7ebec6db37286b0ca54ed1d9f4ca02)
- [bt_pbap_pse_pull_phone_book_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac8ef77affecb5316991afca6c1005f62)
- [bt_pbap_pse_pull_vcard_listing_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gac511c99ae0c2d0f391f5dbf150599390)
- [bt_pbap_pse_pull_vcard_entry_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#gacdcbb62a6999c833e4e6d0846aad28d6)
- [bt_pbap_pse_set_phone_book_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga09e255e0c5328a1f1e7286b7100eeb61)
- [bt_pbap_pse_abort_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9766bda140034251ba3287bfa116f359)

<a id="header-details"></a>

---

[上一章](P010_zephyr__bluetooth__mesh__main.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__net__rtp.h_文件参考.md)
