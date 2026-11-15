---
id: learning.zephyr-docs.api-file-media-sensor-reference.page-2
title: zephyr__bluetooth__classic__map.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_bluetooth\_\_classic\_\_map.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息访问配置文件（Message Access Profile）的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <errno.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/l2cap.h>
#include <zephyr/bluetooth/classic/goep.h>
```

查看此文件的源码。

消息访问配置文件（Message Access Profile）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fmap_5Fmce_5Fmas_5Fcb"></a>

```c
struct bt_map_mce_mas_cb
```

相关声明：[bt_map_mce_mas_cb](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md)。

消息访问配置文件（MAP）客户端的MAS回调。

<a id="r_bt_5Fmap_5Fmce_5Fmas"></a>

```c
struct bt_map_mce_mas
```

相关声明：[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)。

消息访问配置文件（MAP）客户端的消息访问服务器（MAS）实例结构。

<a id="r_bt_5Fmap_5Fmce_5Fmns_5Frfcomm_5Fserver"></a>

```c
struct bt_map_mce_mns_rfcomm_server
```

相关声明：[bt_map_mce_mns_rfcomm_server](../bluetooth_service_model_reference/P112_bt_map_mce_mns_rfcomm_server_结构体.md)。

消息访问配置文件（MAP）客户端的MNS RFCOMM服务器。

<a id="r_bt_5Fmap_5Fmce_5Fmns_5Fl2cap_5Fserver"></a>

```c
struct bt_map_mce_mns_l2cap_server
```

相关声明：[bt_map_mce_mns_l2cap_server](../bluetooth_service_model_reference/P111_bt_map_mce_mns_l2cap_server_结构体.md)。

消息访问配置文件（MAP）客户端的MNS L2CAP服务器。

<a id="r_bt_5Fmap_5Fmce_5Fmns_5Fcb"></a>

```c
struct bt_map_mce_mns_cb
```

相关声明：[bt_map_mce_mns_cb](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md)。

消息访问配置文件（MAP）客户端的MNS回调。

<a id="r_bt_5Fmap_5Fmce_5Fmns"></a>

```c
struct bt_map_mce_mns
```

相关声明：[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)。

消息访问配置文件（MAP）客户端的消息通知服务器（MNS）实例结构。

<a id="r_bt_5Fmap_5Fmse_5Fmas_5Frfcomm_5Fserver"></a>

```c
struct bt_map_mse_mas_rfcomm_server
```

相关声明：[bt_map_mse_mas_rfcomm_server](../bluetooth_service_model_reference/P116_bt_map_mse_mas_rfcomm_server_结构体.md)。

消息访问配置文件（MAP）服务器的MAS RFCOMM服务器。

<a id="r_bt_5Fmap_5Fmse_5Fmas_5Fl2cap_5Fserver"></a>

```c
struct bt_map_mse_mas_l2cap_server
```

相关声明：[bt_map_mse_mas_l2cap_server](../bluetooth_service_model_reference/P115_bt_map_mse_mas_l2cap_server_结构体.md)。

消息访问配置文件（MAP）服务器的MAS L2CAP服务器。

<a id="r_bt_5Fmap_5Fmse_5Fmas_5Fcb"></a>

```c
struct bt_map_mse_mas_cb
```

相关声明：[bt_map_mse_mas_cb](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md)。

消息访问配置文件（MAP）服务器的MAS回调。

<a id="r_bt_5Fmap_5Fmse_5Fmas"></a>

```c
struct bt_map_mse_mas
```

相关声明：[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)。

消息访问配置文件（MAP）服务器的消息访问服务器（MAS）实例结构。

<a id="r_bt_5Fmap_5Fmse_5Fmns_5Fcb"></a>

```c
struct bt_map_mse_mns_cb
```

相关声明：[bt_map_mse_mns_cb](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md)。

消息访问配置文件（MAP）服务器的MNS回调。

<a id="r_bt_5Fmap_5Fmse_5Fmns"></a>

```c
struct bt_map_mse_mns
```

相关声明：[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)。

消息访问配置文件（MAP）服务器的消息通知服务器（MNS）实例结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga109c4eba9cdfc3b938344e2348db940e"></a>

```c
#define BT_MAP_MANDATORY_SUPPORTED_FEATURES (0x0000001FU)
```

相关声明：[BT_MAP_MANDATORY_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga109c4eba9cdfc3b938344e2348db940e)。

消息访问配置文件必需支持功能的位掩码（MAP Mandatory Supported Features Bitmask）。

<a id="r_ga13bacf997de99061640a03a5a6393d55"></a>

```c
#define BT_MAP_UUID_MAS
```

相关声明：[BT_MAP_UUID_MAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga13bacf997de99061640a03a5a6393d55)。

MAP 消息访问服务器（Message Access Server，MAS）的 UUID。

<a id="r_gae8154c6af172a42e5cdbbcf2d1f42ade"></a>

```c
#define BT_MAP_UUID_MNS
```

相关声明：[BT_MAP_UUID_MNS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gae8154c6af172a42e5cdbbcf2d1f42ade)。

MAP 消息通知服务器（Message Notification Server，MNS）的 UUID。

<a id="r_ga166e2fb2e91f001dc8c612b4771855bd"></a>

```c
#define BT_MAP_FILLER_BYTE "0"
```

相关声明：[BT_MAP_FILLER_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga166e2fb2e91f001dc8c612b4771855bd)。

用于填充（Padding）的填充字节（Filler Byte）。

<a id="r_ga5066d3a3d110307380af2e660fa1db39"></a>

```c
#define BT_MAP_HDR_TYPE_SEND_EVENT "x-bt/MAP-event-report"
```

相关声明：[BT_MAP_HDR_TYPE_SEND_EVENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5066d3a3d110307380af2e660fa1db39)。

发送事件操作（Send Event Operation）的类型头部（Type Header）。

<a id="r_ga95985386e036f2c4914c1dc2060b2b2c"></a>

```c
#define BT_MAP_HDR_TYPE_SET_NTF_REG "x-bt/MAP-NotificationRegistration"
```

相关声明：[BT_MAP_HDR_TYPE_SET_NTF_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga95985386e036f2c4914c1dc2060b2b2c)。

设置通知注册操作（Set Notification Registration Operation）的类型头部（Type Header）。

<a id="r_gadd74dc8a80aa351a62d5d50a2f49e955"></a>

```c
#define BT_MAP_HDR_TYPE_GET_FOLDER_LISTING "x-obex/folder-listing"
```

相关声明：[BT_MAP_HDR_TYPE_GET_FOLDER_LISTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gadd74dc8a80aa351a62d5d50a2f49e955)。

获取文件夹列表操作（Get Folder Listing Operation）的类型头部（Type Header）。

<a id="r_gaaef898bb0e87c7ddbd95943dd7941ab8"></a>

```c
#define BT_MAP_HDR_TYPE_GET_MSG_LISTING "x-bt/MAP-msg-listing"
```

相关声明：[BT_MAP_HDR_TYPE_GET_MSG_LISTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gaaef898bb0e87c7ddbd95943dd7941ab8)。

获取消息列表操作（Get Message Listing Operation）的类型头部（Type Header）。

<a id="r_ga59cd61db282e7c78045b1c485e7af843"></a>

```c
#define BT_MAP_HDR_TYPE_GET_MSG "x-bt/message"
```

相关声明：[BT_MAP_HDR_TYPE_GET_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga59cd61db282e7c78045b1c485e7af843)。

获取消息操作（Get Message Operation）的类型头部（Type Header）。

<a id="r_ga7b11a9d0535fe964a8b9e523428fce82"></a>

```c
#define BT_MAP_HDR_TYPE_SET_MSG_STATUS "x-bt/messageStatus"
```

相关声明：[BT_MAP_HDR_TYPE_SET_MSG_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga7b11a9d0535fe964a8b9e523428fce82)。

设置消息状态操作（Set Message Status Operation）的类型头部（Type Header）。

<a id="r_ga3f11b300752a32f6cb8f915d5230c7ad"></a>

```c
#define BT_MAP_HDR_TYPE_PUSH_MSG "x-bt/message"
```

相关声明：[BT_MAP_HDR_TYPE_PUSH_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga3f11b300752a32f6cb8f915d5230c7ad)。

推送消息操作（Push Message Operation）的类型头部（Type Header）。

<a id="r_ga92aa24fa6950c5704ab8ad86d47e7077"></a>

```c
#define BT_MAP_HDR_TYPE_UPDATE_INBOX "x-bt/MAP-messageUpdate"
```

相关声明：[BT_MAP_HDR_TYPE_UPDATE_INBOX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga92aa24fa6950c5704ab8ad86d47e7077)。

更新收件箱操作（Update Inbox Operation）的类型头部（Type Header）。

<a id="r_ga9477fa19750161e79bae0bf7053ccb30"></a>

```c
#define BT_MAP_HDR_TYPE_GET_MAS_INST_INFO "x-bt/MASInstanceInformation"
```

相关声明：[BT_MAP_HDR_TYPE_GET_MAS_INST_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga9477fa19750161e79bae0bf7053ccb30)。

获取 MAS 实例信息操作（Get MAS Instance Info Operation）的类型头部（Type Header）。

<a id="r_gafb909e47193e0ef0549c4b0c1f98002e"></a>

```c
#define BT_MAP_HDR_TYPE_SET_OWNER_STATUS "x-bt/ownerStatus"
```

相关声明：[BT_MAP_HDR_TYPE_SET_OWNER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gafb909e47193e0ef0549c4b0c1f98002e)。

设置所有者状态操作（Set Owner Status Operation）的类型头部（Type Header）。

<a id="r_gae2ed8a5602fc3796d65f825af2f7192e"></a>

```c
#define BT_MAP_HDR_TYPE_GET_OWNER_STATUS "x-bt/ownerStatus"
```

相关声明：[BT_MAP_HDR_TYPE_GET_OWNER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gae2ed8a5602fc3796d65f825af2f7192e)。

获取所有者状态操作（Get Owner Status Operation）的类型头部（Type Header）。

<a id="r_gada79ac46d960d75c784617aeeba935d3"></a>

```c
#define BT_MAP_HDR_TYPE_GET_CONVO_LISTING "x-bt/MAP-convo-listing"
```

相关声明：[BT_MAP_HDR_TYPE_GET_CONVO_LISTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gada79ac46d960d75c784617aeeba935d3)。

获取会话列表操作（Get Conversation Listing Operation）的类型头部（Type Header）。

<a id="r_gaa1ba29f46678e49896ab0fc7a7b5c413"></a>

```c
#define BT_MAP_HDR_TYPE_SET_NTF_FILTER "x-bt/MAP-notification-filter"
```

相关声明：[BT_MAP_HDR_TYPE_SET_NTF_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gaa1ba29f46678e49896ab0fc7a7b5c413)。

设置通知过滤器操作（Set Notification Filter Operation）的类型头部（Type Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.3\_枚举（Enumerations）

<a id="r_ga6d4c3231e2e64190c6ccc30b4d5f822c"></a>

```c
enum bt_map_supported_features { BT_MAP_NTF_REG_FEATURE = (1UL << (0)) , BT_MAP_NTF_FEATURE = (1UL << (1)) , BT_MAP_BROWSING_FEATURE = (1UL << (2)) , BT_MAP_UPLOADING_FEATURE = (1UL << (3)) , BT_MAP_DELETE_FEATURE = (1UL << (4)) , BT_MAP_INST_INFO_FEATURE = (1UL << (5)) , BT_MAP_EXT_EVENT_REPORT_V11 = (1UL << (6)) , BT_MAP_EXT_EVENT_REPORT_V12 = (1UL << (7)) , BT_MAP_MSG_FORMAT_V11 = (1UL << (8)) , BT_MAP_MSG_LISTING_FORMAT_V11 = (1UL << (9)) , BT_MAP_PERSISTENT_MSG_HANDLE = (1UL << (10)) , BT_MAP_DB_ID = (1UL << (11)) , BT_MAP_FOLDER_VER_CNTR = (1UL << (12)) , BT_MAP_CONVO_VER_CNTR = (1UL << (13)) , BT_MAP_PARTICIPANT_PRESENCE_CHANGE_NTF = (1UL << (14)) , BT_MAP_PARTICIPANT_CHAT_STATE_CHANGE_NTF = (1UL << (15)) , BT_MAP_PBAP_CONTACT_XREF = (1UL << (16)) , BT_MAP_NTF_FILTERING = (1UL << (17)) , BT_MAP_UTC_OFFSET_TIMESTAMP_FORMAT = (1UL << (18)) , BT_MAP_SUPPORTED_FEATURES_CONN_REQ = (1UL << (19)) , BT_MAP_CONVO_LISTING = (1UL << (20)) , BT_MAP_OWNER_STATUS = (1UL << (21)) , BT_MAP_MSG_FORWARDING = (1UL << (22)) }
```

相关声明：[bt_map_supported_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga6d4c3231e2e64190c6ccc30b4d5f822c)、[BT_MAP_NTF_REG_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822cae5fa5f417d064a1b85e9db70a5ce94e5)、[BT_MAP_NTF_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822cac4a88df48198a497da4a94ec124bb735)、[BT_MAP_BROWSING_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caec96609ac47f6cf1e779d049687f2e63)、[BT_MAP_UPLOADING_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca572d7eb54deb371cee55c0149f21d6db)、[BT_MAP_DELETE_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caa7e8028e50f7903aefd379d76695408f)、[BT_MAP_INST_INFO_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca32cf970e22e8f082293225b5a614de8d)、[BT_MAP_EXT_EVENT_REPORT_V11](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca7467b703f0cf9d760d6d18e0dd6dfa7f)、[BT_MAP_EXT_EVENT_REPORT_V12](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca2cbc347cb637a951868052e58eb3dab9)、[BT_MAP_MSG_FORMAT_V11](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caa6de591a1e2d5936263741f273c9fb8a)、[BT_MAP_MSG_LISTING_FORMAT_V11](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822cae28c62057713e3a7318cf85eaa7c337e)、[BT_MAP_PERSISTENT_MSG_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca5e63f64fb534af8295995a0fbec364df)、[BT_MAP_DB_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca71243a44c4d5a105c02b49318302fb7a)、[BT_MAP_FOLDER_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca2c7cbab7fe254b975668563039c7ace8)、[BT_MAP_CONVO_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca8d214b20b66be2264fb8da2d9feb93d0)、[BT_MAP_PARTICIPANT_PRESENCE_CHANGE_NTF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca2843780dad72eaa1d84cec56077cff93)、[BT_MAP_PARTICIPANT_CHAT_STATE_CHANGE_NTF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca1bc10abe061f68c3de72c37b5307c484)、[BT_MAP_PBAP_CONTACT_XREF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca679c98163ee9b3114c7adf64b6976a9e)、[BT_MAP_NTF_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca3353469789a5a72f4fc97dabed1d4dcf)、[BT_MAP_UTC_OFFSET_TIMESTAMP_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca9aaa859278454e081c5fe5e83dfded5d)、[BT_MAP_SUPPORTED_FEATURES_CONN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caa76c12d6babf2df623f28f58ed1912d0)、[BT_MAP_CONVO_LISTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca35f15fe0fba34519ff0d1087c2e32c4c)、[BT_MAP_OWNER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca6aa30c2d7dccbe630756c1f1e4f7a141)、[BT_MAP_MSG_FORWARDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caccc791a50cc33ef4d62d6b126c1ba898)。

MAP 支持的功能（Supported Features）。

<a id="r_ga5bb2e0b7951bde5042fbb9c4e0c7cc26"></a>

```c
enum bt_map_supported_msg_type { BT_MAP_MSG_TYPE_EMAIL = (1UL << (0)) , BT_MAP_MSG_TYPE_SMS_GSM = (1UL << (1)) , BT_MAP_MSG_TYPE_SMS_CDMA = (1UL << (2)) , BT_MAP_MSG_TYPE_MMS = (1UL << (3)) , BT_MAP_MSG_TYPE_IM = (1UL << (4)) }
```

相关声明：[bt_map_supported_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5bb2e0b7951bde5042fbb9c4e0c7cc26)、[BT_MAP_MSG_TYPE_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26ae0396ce6457b9792d564195f906fafe3)、[BT_MAP_MSG_TYPE_SMS_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a0f4bd271fb4a331e66dafde2a04fd62a)、[BT_MAP_MSG_TYPE_SMS_CDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a803694148d134338a83f365390929505)、[BT_MAP_MSG_TYPE_MMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a9f65cf3b8d5a5855219599ed656ea56c)、[BT_MAP_MSG_TYPE_IM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a038430c6eea453638a2fc3351315b638)。

MAP 支持的消息类型（Supported Message Types）。

<a id="r_ga5678131af7da533ff8b751555542933e"></a>

```c
enum bt_map_set_folder_flags { BT_MAP_SET_FOLDER_FLAGS_ROOT = BT_OBEX_SETPATH_FLAG_NO_CREATE , BT_MAP_SET_FOLDER_FLAGS_DOWN = BT_OBEX_SETPATH_FLAG_NO_CREATE , BT_MAP_SET_FOLDER_FLAGS_UP = BT_OBEX_SETPATH_FLAG_BACKUP | BT_OBEX_SETPATH_FLAG_NO_CREATE }
```

相关声明：[bt_map_set_folder_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5678131af7da533ff8b751555542933e)、[BT_MAP_SET_FOLDER_FLAGS_ROOT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5678131af7da533ff8b751555542933eaa5d3b0ad2bf7f8600ad059132aaed665)、[BT_MAP_SET_FOLDER_FLAGS_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5678131af7da533ff8b751555542933ead7b0402847a837a69055dcf4b6fad674)、[BT_MAP_SET_FOLDER_FLAGS_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5678131af7da533ff8b751555542933ea8b13f5d7fc245c7b66a65e0845ed7edc)。

MAP 设置文件夹操作标志（Set Folder Operation Flags）。

<a id="r_ga7310a116a939b40d7ee346371b5ccd88"></a>

```c
enum bt_map_appl_param_tag_id { BT_MAP_APPL_PARAM_TAG_ID_MAX_LIST_CNT = 0x01 , BT_MAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET = 0x02 , BT_MAP_APPL_PARAM_TAG_ID_FILTER_MSG_TYPE = 0x03 , BT_MAP_APPL_PARAM_TAG_ID_FILTER_PERIOD_BEGIN = 0x04 , BT_MAP_APPL_PARAM_TAG_ID_FILTER_PERIOD_END = 0x05 , BT_MAP_APPL_PARAM_TAG_ID_FILTER_READ_STATUS = 0x06 , BT_MAP_APPL_PARAM_TAG_ID_FILTER_RECIPIENT = 0x07 , BT_MAP_APPL_PARAM_TAG_ID_FILTER_ORIGINATOR = 0x08 , BT_MAP_APPL_PARAM_TAG_ID_FILTER_PRIORITY = 0x09 , BT_MAP_APPL_PARAM_TAG_ID_ATTACHMENT = 0x0a , BT_MAP_APPL_PARAM_TAG_ID_TRANSPARENT = 0x0b , BT_MAP_APPL_PARAM_TAG_ID_RETRY = 0x0c , BT_MAP_APPL_PARAM_TAG_ID_NEW_MSG = 0x0d , BT_MAP_APPL_PARAM_TAG_ID_NTF_STATUS = 0x0e , BT_MAP_APPL_PARAM_TAG_ID_MAS_INST_ID = 0x0f , BT_MAP_APPL_PARAM_TAG_ID_PARAM_MASK = 0x10 , BT_MAP_APPL_PARAM_TAG_ID_FOLDER_LISTING_SIZE = 0x11 , BT_MAP_APPL_PARAM_TAG_ID_LISTING_SIZE = 0x12 , BT_MAP_APPL_PARAM_TAG_ID_SUBJECT_LEN = 0x13 , BT_MAP_APPL_PARAM_TAG_ID_CHARSET = 0x14 , BT_MAP_APPL_PARAM_TAG_ID_FRACTION_REQUEST = 0x15 , BT_MAP_APPL_PARAM_TAG_ID_FRACTION_DELIVER = 0x16 , BT_MAP_APPL_PARAM_TAG_ID_STATUS_IND = 0x17 , BT_MAP_APPL_PARAM_TAG_ID_STATUS_VAL = 0x18 , BT_MAP_APPL_PARAM_TAG_ID_MSE_TIME = 0x19 , BT_MAP_APPL_PARAM_TAG_ID_DB_ID = 0x1a , BT_MAP_APPL_PARAM_TAG_ID_CONVO_LISTING_VER_CNTR = 0x1b , BT_MAP_APPL_PARAM_TAG_ID_PRESENCE_AVAIL = 0x1c , BT_MAP_APPL_PARAM_TAG_ID_PRESENCE_TEXT = 0x1d , BT_MAP_APPL_PARAM_TAG_ID_LAST_ACTIVITY = 0x1e , BT_MAP_APPL_PARAM_TAG_ID_FILTER_LAST_ACTIVITY_BEGIN = 0x1f , BT_MAP_APPL_PARAM_TAG_ID_FILTER_LAST_ACTIVITY_END = 0x20 , BT_MAP_APPL_PARAM_TAG_ID_CHAT_STATE = 0x21 , BT_MAP_APPL_PARAM_TAG_ID_CONVO_ID = 0x22 , BT_MAP_APPL_PARAM_TAG_ID_FOLDER_VER_CNTR = 0x23 , BT_MAP_APPL_PARAM_TAG_ID_FILTER_MSG_HANDLE = 0x24 , BT_MAP_APPL_PARAM_TAG_ID_NTF_FILTER_MASK = 0x25 , BT_MAP_APPL_PARAM_TAG_ID_CONVO_PARAM_MASK = 0x26 , BT_MAP_APPL_PARAM_TAG_ID_OWNER_UCI = 0x27 , BT_MAP_APPL_PARAM_TAG_ID_EXT_DATA = 0x28 , BT_MAP_APPL_PARAM_TAG_ID_MAP_SUPPORTED_FEATURES = 0x29 , BT_MAP_APPL_PARAM_TAG_ID_MSG_HANDLE = 0x2a , BT_MAP_APPL_PARAM_TAG_ID_MODIFY_TEXT = 0x2b }
```

相关声明：[bt_map_appl_param_tag_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga7310a116a939b40d7ee346371b5ccd88)、[BT_MAP_APPL_PARAM_TAG_ID_MAX_LIST_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a2df85ffb7e034732fb608c6935af9297)、[BT_MAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7227e024472a421c86c3cb7a0db65e55)、[BT_MAP_APPL_PARAM_TAG_ID_FILTER_MSG_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88af39bad93c459fcb86b9583a1519c070b)、[BT_MAP_APPL_PARAM_TAG_ID_FILTER_PERIOD_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7627a7496631fbe6326e4c1c43e4877c)、[BT_MAP_APPL_PARAM_TAG_ID_FILTER_PERIOD_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a2071ba2e3ec0dc8b5adc8b97a37a010d)、[BT_MAP_APPL_PARAM_TAG_ID_FILTER_READ_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88aa1b59e01c63abc3ccc7ee54ca27e9296)、[BT_MAP_APPL_PARAM_TAG_ID_FILTER_RECIPIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ac6118aa692c3c382ce7630ac2d499aac)、[BT_MAP_APPL_PARAM_TAG_ID_FILTER_ORIGINATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88adb08ba0bbc13653357e835dcd6fa5770)、[BT_MAP_APPL_PARAM_TAG_ID_FILTER_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a637ac76aafe5a586819b9897acc7d1da)、[BT_MAP_APPL_PARAM_TAG_ID_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad53697174462dfe4d2d592bf71bf180c)、[BT_MAP_APPL_PARAM_TAG_ID_TRANSPARENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a595f6e5f7eac3c57dccf13e1e45dfd6b)、[BT_MAP_APPL_PARAM_TAG_ID_RETRY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a19b5e72c512c29b5cfbe58dbdaf63064)、[BT_MAP_APPL_PARAM_TAG_ID_NEW_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a4871d9d7da47983cd5fd7a7718ab2478)、[BT_MAP_APPL_PARAM_TAG_ID_NTF_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88aee3ebbef8eb74deefedb414daea2dc1e)、[BT_MAP_APPL_PARAM_TAG_ID_MAS_INST_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a170d3717ab48a7f6a63e8bd66d1cb228)、[BT_MAP_APPL_PARAM_TAG_ID_PARAM_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a563fbb6001387da1389713be552fec13)、[BT_MAP_APPL_PARAM_TAG_ID_FOLDER_LISTING_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a1aca8ccd385944cb73f03568123dc1e3)、[BT_MAP_APPL_PARAM_TAG_ID_LISTING_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88aa9241c4f620f61717160d5dbc9dc5389)、[BT_MAP_APPL_PARAM_TAG_ID_SUBJECT_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a15c0a2959d67e24ed18203cd8c9fe46a)、[BT_MAP_APPL_PARAM_TAG_ID_CHARSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad1d1edb33a8147e1d96400607e8f3f1e)、[BT_MAP_APPL_PARAM_TAG_ID_FRACTION_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88acfef6214cbd687aa5ad7ee4d8d3a4a2d)、[BT_MAP_APPL_PARAM_TAG_ID_FRACTION_DELIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a8651767d6b1c5dc6f0affac25014aeaa)、[BT_MAP_APPL_PARAM_TAG_ID_STATUS_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a5622480195120444b2f200e79db09499)、[BT_MAP_APPL_PARAM_TAG_ID_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a4ee0642cd16aa8e1ce5224118968f9ee)、[BT_MAP_APPL_PARAM_TAG_ID_MSE_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a0bb8acb58e8983793bb787ae8e6d4033)、[BT_MAP_APPL_PARAM_TAG_ID_DB_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7f9d301f9383d8179611344d18f03094)、[BT_MAP_APPL_PARAM_TAG_ID_CONVO_LISTING_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a8f4a492c9619ec1b78124f0509b93857)、[BT_MAP_APPL_PARAM_TAG_ID_PRESENCE_AVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7636683c2efff7c4c8d59a141c6e12b6)、[BT_MAP_APPL_PARAM_TAG_ID_PRESENCE_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a06ae16f7d6a3a247e5e1771254df0ea9)、[BT_MAP_APPL_PARAM_TAG_ID_LAST_ACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a6f5914896a591c0008fb744506ec98d4)、[BT_MAP_APPL_PARAM_TAG_ID_FILTER_LAST_ACTIVITY_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a5ec11c380b39a38cade5acd06545b1a1)、[BT_MAP_APPL_PARAM_TAG_ID_FILTER_LAST_ACTIVITY_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad49f0edd1a6e1c1da5a37abd552cc6b1)、[BT_MAP_APPL_PARAM_TAG_ID_CHAT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88adaad04f88448466dd606527157d74cc7)、[BT_MAP_APPL_PARAM_TAG_ID_CONVO_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a72083eddb755825e5899dfddbcc10085)、[BT_MAP_APPL_PARAM_TAG_ID_FOLDER_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a706346ca21cb1f76c22dc02af1076b04)、[BT_MAP_APPL_PARAM_TAG_ID_FILTER_MSG_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a600395d6f4620dffee2447ae8b9a4fbe)、[BT_MAP_APPL_PARAM_TAG_ID_NTF_FILTER_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a161b7d1952483a47eee81dfd98ce831c)、[BT_MAP_APPL_PARAM_TAG_ID_CONVO_PARAM_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a79da1ebc8b5e7e0d1098d4b022fa8da7)、[BT_MAP_APPL_PARAM_TAG_ID_OWNER_UCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad3058d06b585289586c5cccaab548bc2)、[BT_MAP_APPL_PARAM_TAG_ID_EXT_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a81297adf58afc780a00afe8ef4a70c95)、[BT_MAP_APPL_PARAM_TAG_ID_MAP_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a9f08b382471f807452d9cf7e1bff1b3b)、[BT_MAP_APPL_PARAM_TAG_ID_MSG_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a6b4d28c95336af96c06a71f6cb40060b)、[BT_MAP_APPL_PARAM_TAG_ID_MODIFY_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a208c8d9ea3195b7d70ab2e7ccae6671d)。

MAP 应用参数标签标识符（Application Parameter Tag Identifiers）。

<a id="r_ga7c4ba8b9727c454a54a2178d584dfcb7"></a>

```c
enum bt_map_filter_msg_type { BT_MAP_FILTER_MSG_TYPE_NO_FILTERING = 0x00 , BT_MAP_FILTER_MSG_TYPE_SMS_GSM = (1UL << (0)) , BT_MAP_FILTER_MSG_TYPE_SMS_CDMA = (1UL << (1)) , BT_MAP_FILTER_MSG_TYPE_EMAIL = (1UL << (2)) , BT_MAP_FILTER_MSG_TYPE_MMS = (1UL << (3)) , BT_MAP_FILTER_MSG_TYPE_IM = (1UL << (4)) }
```

相关声明：[bt_map_filter_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga7c4ba8b9727c454a54a2178d584dfcb7)、[BT_MAP_FILTER_MSG_TYPE_NO_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7adfc6a259bbc5d1b6a0b30d57d1a5b7a9)、[BT_MAP_FILTER_MSG_TYPE_SMS_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a2ab7b8a63e2dae0bf8d82e5c7aae3038)、[BT_MAP_FILTER_MSG_TYPE_SMS_CDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a9df74f88cb18833440816218a610527c)、[BT_MAP_FILTER_MSG_TYPE_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a37bca39682be9efa27f906754d972b7d)、[BT_MAP_FILTER_MSG_TYPE_MMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a1b10e235398a004168731de140b7e6d8)、[BT_MAP_FILTER_MSG_TYPE_IM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7ab80d08d33c7fc5adc1483b1be64390c0)。

MAP 消息类型过滤值（Filter Message Type Values）。

<a id="r_gabf5f60778a9adf113e86e559095dd66f"></a>

```c
enum bt_map_filter_read_status { BT_MAP_FILTER_READ_STATUS_NO_FILTERING = 0x00 , BT_MAP_FILTER_READ_STATUS_UNREAD = 0x01 , BT_MAP_FILTER_READ_STATUS_READ = 0x02 }
```

相关声明：[bt_map_filter_read_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gabf5f60778a9adf113e86e559095dd66f)、[BT_MAP_FILTER_READ_STATUS_NO_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabf5f60778a9adf113e86e559095dd66fa0c7b3c3b9c8f0d9c514a9730d57d7738)、[BT_MAP_FILTER_READ_STATUS_UNREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabf5f60778a9adf113e86e559095dd66fae90806b4b223afc531d74dd1819ff7b3)、[BT_MAP_FILTER_READ_STATUS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabf5f60778a9adf113e86e559095dd66faf9e8514d6411d25bc71a33e7f351f93f)。

MAP 已读状态过滤值（Filter Read Status Values）。

<a id="r_ga4f1f483d5edfaa151a11086caac24e5c"></a>

```c
enum bt_map_filter_priority { BT_MAP_FILTER_PRIORITY_NO_FILTERING = 0x00 , BT_MAP_FILTER_PRIORITY_HIGH = 0x01 , BT_MAP_FILTER_PRIORITY_NON_HIGH = 0x02 }
```

相关声明：[bt_map_filter_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga4f1f483d5edfaa151a11086caac24e5c)、[BT_MAP_FILTER_PRIORITY_NO_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4f1f483d5edfaa151a11086caac24e5ca0f8654affc09e99bad440d2b9faeb163)、[BT_MAP_FILTER_PRIORITY_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4f1f483d5edfaa151a11086caac24e5ca66220e415b9164fe41a19e423b4aad90)、[BT_MAP_FILTER_PRIORITY_NON_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4f1f483d5edfaa151a11086caac24e5ca12b73e28e320ba1bf3aa8edf44b053cd)。

MAP 优先级过滤值（Filter Priority Values）。

<a id="r_ga34cee2f295fee5b00bced31753f03b25"></a>

```c
enum bt_map_attachment { BT_MAP_ATTACHMENT_OFF = 0x00 , BT_MAP_ATTACHMENT_ON = 0x01 }
```

相关声明：[bt_map_attachment](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga34cee2f295fee5b00bced31753f03b25)、[BT_MAP_ATTACHMENT_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga34cee2f295fee5b00bced31753f03b25a74198afdf437d36971d5cf4fdcaab5b8)、[BT_MAP_ATTACHMENT_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga34cee2f295fee5b00bced31753f03b25a089baca6845a803dda4b7e506e452b5b)。

MAP 附件取值（Attachment Values）。

<a id="r_ga215e8bd71131e739b19f5f5ee57904e6"></a>

```c
enum bt_map_transparent { BT_MAP_TRANSPARENT_OFF = 0x00 , BT_MAP_TRANSPARENT_ON = 0x01 }
```

相关声明：[bt_map_transparent](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga215e8bd71131e739b19f5f5ee57904e6)、[BT_MAP_TRANSPARENT_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga215e8bd71131e739b19f5f5ee57904e6a5f1552a26d09f1c696f828967222707f)、[BT_MAP_TRANSPARENT_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga215e8bd71131e739b19f5f5ee57904e6addfabaeaa7d8903c81b41c9844514849)。

MAP 透明传输取值（Transparent Values）。

<a id="r_ga4a9fc0bfa14b5e91491aec130e396429"></a>

```c
enum bt_map_retry { BT_MAP_RETRY_OFF = 0x00 , BT_MAP_RETRY_ON = 0x01 }
```

相关声明：[bt_map_retry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga4a9fc0bfa14b5e91491aec130e396429)、[BT_MAP_RETRY_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4a9fc0bfa14b5e91491aec130e396429a4955b62b432b783eb774d704e2f2b4e2)、[BT_MAP_RETRY_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4a9fc0bfa14b5e91491aec130e396429a0215a73c93fe79bbd9fc28b34af31057)。

MAP 重试取值（Retry Values）。

<a id="r_ga8dcd4f8704a2b1cab77b2279d7f2024f"></a>

```c
enum bt_map_new_msg { BT_MAP_NEW_MSG_OFF = 0x00 , BT_MAP_NEW_MSG_ON = 0x01 }
```

相关声明：[bt_map_new_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga8dcd4f8704a2b1cab77b2279d7f2024f)、[BT_MAP_NEW_MSG_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8dcd4f8704a2b1cab77b2279d7f2024fabe2ef316affe063b7634ca5e5f2e0351)、[BT_MAP_NEW_MSG_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8dcd4f8704a2b1cab77b2279d7f2024fa735aac580ed7fae38d10bcc41f2b393a)。

MAP 新消息取值（New Message Values）。

<a id="r_ga8b805587e1abb311367e59d80d223516"></a>

```c
enum bt_map_ntf_status { BT_MAP_NTF_STATUS_OFF = 0x00 , BT_MAP_NTF_STATUS_ON = 0x01 }
```

相关声明：[bt_map_ntf_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga8b805587e1abb311367e59d80d223516)、[BT_MAP_NTF_STATUS_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8b805587e1abb311367e59d80d223516a8c7e4fd24ff699c52a7ecba484923cfb)、[BT_MAP_NTF_STATUS_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8b805587e1abb311367e59d80d223516a25fc04d24537a005dc4674d29ad48357)。

MAP 通知状态取值（Notification Status Values）。

<a id="r_gadec3f7d6faccc656739a7b7a88c10387"></a>

```c
enum bt_map_param_mask { BT_MAP_PARAM_MASK_SUBJECT = (1UL << (0)) , BT_MAP_PARAM_MASK_DATETIME = (1UL << (1)) , BT_MAP_PARAM_MASK_SENDER_NAME = (1UL << (2)) , BT_MAP_PARAM_MASK_SENDER_ADDRESSING = (1UL << (3)) , BT_MAP_PARAM_MASK_RECIPIENT_NAME = (1UL << (4)) , BT_MAP_PARAM_MASK_RECIPIENT_ADDRESSING = (1UL << (5)) , BT_MAP_PARAM_MASK_TYPE = (1UL << (6)) , BT_MAP_PARAM_MASK_SIZE = (1UL << (7)) , BT_MAP_PARAM_MASK_RECEPTION_STATUS = (1UL << (8)) , BT_MAP_PARAM_MASK_TEXT = (1UL << (9)) , BT_MAP_PARAM_MASK_ATTACHMENT_SIZE = (1UL << (10)) , BT_MAP_PARAM_MASK_PRIORITY = (1UL << (11)) , BT_MAP_PARAM_MASK_READ = (1UL << (12)) , BT_MAP_PARAM_MASK_SENT = (1UL << (13)) , BT_MAP_PARAM_MASK_PROTECTED = (1UL << (14)) , BT_MAP_PARAM_MASK_REPLYTO_ADDRESSING = (1UL << (15)) , BT_MAP_PARAM_MASK_DELIVERY_STATUS = (1UL << (16)) , BT_MAP_PARAM_MASK_CONVO_ID = (1UL << (17)) , BT_MAP_PARAM_MASK_CONVO_NAME = (1UL << (18)) , BT_MAP_PARAM_MASK_DIRECTION = (1UL << (19)) , BT_MAP_PARAM_MASK_ATTACHMENT_MIME = (1UL << (20)) }
```

相关声明：[bt_map_param_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gadec3f7d6faccc656739a7b7a88c10387)、[BT_MAP_PARAM_MASK_SUBJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387aac91fbe72b91381095f4f2f32e7be327)、[BT_MAP_PARAM_MASK_DATETIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a898d380bc11251e69d4525c2e3f5fcbe)、[BT_MAP_PARAM_MASK_SENDER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a1cad006d6e9d8740e929a801a3a3593f)、[BT_MAP_PARAM_MASK_SENDER_ADDRESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a0c4cac1477808905597af3d1373663d4)、[BT_MAP_PARAM_MASK_RECIPIENT_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a90f5931d1fe65f3f2b0718c357e45740)、[BT_MAP_PARAM_MASK_RECIPIENT_ADDRESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387aeaaa6e5cad8201d747248f40cef19038)、[BT_MAP_PARAM_MASK_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387ab62fbb3ed1d684c4e0e86e0d04ee6995)、[BT_MAP_PARAM_MASK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a8c7c06f8ebdd5e433e926345d62c092b)、[BT_MAP_PARAM_MASK_RECEPTION_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a1b55581c15bf6d915a748fff1655f2eb)、[BT_MAP_PARAM_MASK_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a5b0a0672211d6e9a0e377baaa16f449a)、[BT_MAP_PARAM_MASK_ATTACHMENT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a1c86d02bc4003273da0e84ebaeaa4ae8)、[BT_MAP_PARAM_MASK_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a07145a14474b470e1dc9143d115add4f)、[BT_MAP_PARAM_MASK_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387afb8f5b6bde20c9526dc520dea12f5fc6)、[BT_MAP_PARAM_MASK_SENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a47987b441c785b7657f9323ec7858d51)、[BT_MAP_PARAM_MASK_PROTECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a302b63d08cb7ff36204c2f390b746375)、[BT_MAP_PARAM_MASK_REPLYTO_ADDRESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a295391beee4e7f92c9e5745785da214d)、[BT_MAP_PARAM_MASK_DELIVERY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387acb4ed5200b771b50ec1481a779230850)、[BT_MAP_PARAM_MASK_CONVO_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387ac421a69062c73e6eeae9c1730072cfe8)、[BT_MAP_PARAM_MASK_CONVO_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a21a483901085035c22fc3baf02931df6)、[BT_MAP_PARAM_MASK_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a001c4dc6084e12938867c4a1eb7316ea)、[BT_MAP_PARAM_MASK_ATTACHMENT_MIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387aac5a5819c4a284c9067951724cd5e794)。

MAP 参数掩码位（Parameter Mask Bits）。

<a id="r_ga0fa30e8b33826204f0625a2223cfaf1c"></a>

```c
enum bt_map_charset { BT_MAP_CHARSET_NATIVE = 0x00 , BT_MAP_CHARSET_UTF8 = 0x01 }
```

相关声明：[bt_map_charset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga0fa30e8b33826204f0625a2223cfaf1c)、[BT_MAP_CHARSET_NATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga0fa30e8b33826204f0625a2223cfaf1ca104a2dd364f1e86b9b5f4cd8fea38011)、[BT_MAP_CHARSET_UTF8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga0fa30e8b33826204f0625a2223cfaf1ca45f4dd02d1e4c1ce1ceef8be95684a51)。

MAP 字符集取值（Charset Values）。

<a id="r_ga430b14f450167b13329f54377473b699"></a>

```c
enum bt_map_fraction_request { BT_MAP_FRACTION_REQUEST_FIRST = 0x00 , BT_MAP_FRACTION_REQUEST_NEXT = 0x01 }
```

相关声明：[bt_map_fraction_request](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga430b14f450167b13329f54377473b699)、[BT_MAP_FRACTION_REQUEST_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga430b14f450167b13329f54377473b699a1a041e3eed1744fe8d02908be402b0a4)、[BT_MAP_FRACTION_REQUEST_NEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga430b14f450167b13329f54377473b699a22d8803a6310974137af6d8bc0c9e6a8)。

MAP 分段请求取值（Fraction Request Values）。

<a id="r_ga3d3327344323fae6f7a2b1ebca459db0"></a>

```c
enum bt_map_fraction_deliver { BT_MAP_FRACTION_DELIVER_MORE = 0x00 , BT_MAP_FRACTION_DELIVER_LAST = 0x01 }
```

相关声明：[bt_map_fraction_deliver](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga3d3327344323fae6f7a2b1ebca459db0)、[BT_MAP_FRACTION_DELIVER_MORE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga3d3327344323fae6f7a2b1ebca459db0ab4134b8e2c9987789fa541627d9ab19f)、[BT_MAP_FRACTION_DELIVER_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga3d3327344323fae6f7a2b1ebca459db0aebc96aeb807ea78da5d8714b1213e6f7)。

MAP 分段交付取值（Fraction Deliver Values）。

<a id="r_gabd4c099cc62671f53edec84eb04c50ff"></a>

```c
enum bt_map_status_ind { BT_MAP_STATUS_IND_READ = 0x00 , BT_MAP_STATUS_IND_DELETED = 0x01 , BT_MAP_STATUS_IND_EXTENDED_DATA = 0x02 }
```

相关声明：[bt_map_status_ind](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gabd4c099cc62671f53edec84eb04c50ff)、[BT_MAP_STATUS_IND_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabd4c099cc62671f53edec84eb04c50ffa64afbc9334b9ee926b11dd473d70e0aa)、[BT_MAP_STATUS_IND_DELETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabd4c099cc62671f53edec84eb04c50ffad1adaa8853f8bca4f4d21b378caeaf19)、[BT_MAP_STATUS_IND_EXTENDED_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabd4c099cc62671f53edec84eb04c50ffaf9dd6096a95f6f75140d2d37d12e24b3)。

MAP 状态指示器取值（Status Indicator Values）。

<a id="r_ga7af9d1e4244a00f8d2ae607f590fea94"></a>

```c
enum bt_map_status_val { BT_MAP_STATUS_VAL_NO = 0x00 , BT_MAP_STATUS_VAL_YES = 0x01 }
```

相关声明：[bt_map_status_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga7af9d1e4244a00f8d2ae607f590fea94)、[BT_MAP_STATUS_VAL_NO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7af9d1e4244a00f8d2ae607f590fea94a28da6d9711231be9117aec9feb9104f4)、[BT_MAP_STATUS_VAL_YES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7af9d1e4244a00f8d2ae607f590fea94af5d7d30b5e5d6f0e8a4dd5ae42104bf8)。

MAP 状态值取值（Status Value Values）。

<a id="r_ga9523beb219a00ac4e6dba3e021b491d4"></a>

```c
enum bt_map_presence { BT_MAP_PRESENCE_UNKNOWN = 0x00 , BT_MAP_PRESENCE_OFFLINE = 0x01 , BT_MAP_PRESENCE_ONLINE = 0x02 , BT_MAP_PRESENCE_AWAY = 0x03 , BT_MAP_PRESENCE_DO_NOT_DISTURB = 0x04 , BT_MAP_PRESENCE_BUSY = 0x05 , BT_MAP_PRESENCE_IN_A_MEETING = 0x06 }
```

相关声明：[bt_map_presence](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga9523beb219a00ac4e6dba3e021b491d4)、[BT_MAP_PRESENCE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a9a458e69d88a1f2c3be14c4c69c99b39)、[BT_MAP_PRESENCE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a4affc47380cbcbbfcb819092d9c5cfd5)、[BT_MAP_PRESENCE_ONLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4ade1acc46b57740b9c113cdf4ea8a502f)、[BT_MAP_PRESENCE_AWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a98e509fe029643bb5f281b9274c70583)、[BT_MAP_PRESENCE_DO_NOT_DISTURB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a3c1a5486acfe0d06fa935f34c5bf0d1c)、[BT_MAP_PRESENCE_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4afc2b4a0338e768d25f200efe3c14081a)、[BT_MAP_PRESENCE_IN_A_MEETING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a4d4a9258001731ffb4ea74d807394050)。

MAP 在线可用性状态（Presence Availability States）。

<a id="r_gace38e2a78aaba1e2c48572e0d247e68c"></a>

```c
enum bt_map_chat_state { BT_MAP_CHAT_STATE_UNKNOWN = 0x00 , BT_MAP_CHAT_STATE_INACTIVE = 0x01 , BT_MAP_CHAT_STATE_ACTIVE = 0x02 , BT_MAP_CHAT_STATE_COMPOSING = 0x03 , BT_MAP_CHAT_STATE_PAUSED_COMPOSING = 0x04 , BT_MAP_CHAT_STATE_GONE = 0x05 }
```

相关声明：[bt_map_chat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gace38e2a78aaba1e2c48572e0d247e68c)、[BT_MAP_CHAT_STATE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68cad9c127c32a580302536aa13cddd52085)、[BT_MAP_CHAT_STATE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca179f10a2a6dd6184f4604794f2bb170f)、[BT_MAP_CHAT_STATE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca1bb84095702eb5c6263a6ee908a6d1c6)、[BT_MAP_CHAT_STATE_COMPOSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca95cb2a4eb0e6d8d2f2dd9f03a3c7c720)、[BT_MAP_CHAT_STATE_PAUSED_COMPOSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68cacfffcf3cef8adddd1e1768fda9cdcf6d)、[BT_MAP_CHAT_STATE_GONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca496b9d0393213a460a0b0bd2c8e4ba33)。

MAP 聊天状态（Chat States）。

<a id="r_ga5acd8d8cfc6358140438860067970e2b"></a>

```c
enum bt_map_ntf_filter_mask { BT_MAP_NTF_FILTER_MASK_NEW_MSG = (1UL << (0)) , BT_MAP_NTF_FILTER_MASK_MSG_DELETED = (1UL << (1)) , BT_MAP_NTF_FILTER_MASK_MSG_SHIFT = (1UL << (2)) , BT_MAP_NTF_FILTER_MASK_SENDING_SUCCESS = (1UL << (3)) , BT_MAP_NTF_FILTER_MASK_SENDING_FAILURE = (1UL << (4)) , BT_MAP_NTF_FILTER_MASK_DELIVERY_SUCCESS = (1UL << (5)) , BT_MAP_NTF_FILTER_MASK_DELIVERY_FAILURE = (1UL << (6)) , BT_MAP_NTF_FILTER_MASK_MEM_FULL = (1UL << (7)) , BT_MAP_NTF_FILTER_MASK_MEM_AVAIL = (1UL << (8)) , BT_MAP_NTF_FILTER_MASK_READ_STATUS_CHANGED = (1UL << (9)) , BT_MAP_NTF_FILTER_MASK_CONVO_CHANGED = (1UL << (10)) , BT_MAP_NTF_FILTER_MASK_PARTICIPANT_PRESENCE_CHANGED = (1UL << (11)) , BT_MAP_NTF_FILTER_MASK_PARTICIPANT_CHAT_STATE_CHANGED = (1UL << (12)) , BT_MAP_NTF_FILTER_MASK_MSG_EXT_DATA_CHANGED = (1UL << (13)) , BT_MAP_NTF_FILTER_MASK_MSG_REMOVED = (1UL << (14)) }
```

相关声明：[bt_map_ntf_filter_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5acd8d8cfc6358140438860067970e2b)、[BT_MAP_NTF_FILTER_MASK_NEW_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba77669e589a872268da67098ef008f3eb)、[BT_MAP_NTF_FILTER_MASK_MSG_DELETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba88aa3bd1aeac147410ae96e8c7de43f9)、[BT_MAP_NTF_FILTER_MASK_MSG_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2bad0ef68fc6a11e2429f67e1d6564597ef)、[BT_MAP_NTF_FILTER_MASK_SENDING_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba5e21b8db192673e5b6e3146ed5b04dba)、[BT_MAP_NTF_FILTER_MASK_SENDING_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba47d696ec191c6a0463ce70d5742616ad)、[BT_MAP_NTF_FILTER_MASK_DELIVERY_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2baf34804c0b883c1a172c92ba237e05817)、[BT_MAP_NTF_FILTER_MASK_DELIVERY_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2baa8e1626a89d2824b2fa3d6723a3a45cd)、[BT_MAP_NTF_FILTER_MASK_MEM_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba83158a4308e7e89422541f2120e9baeb)、[BT_MAP_NTF_FILTER_MASK_MEM_AVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2baa869867c70b17e91f726f27c6cbcacda)、[BT_MAP_NTF_FILTER_MASK_READ_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2bab1a7d0518b5555eb63fb7ecee7e43bc9)、[BT_MAP_NTF_FILTER_MASK_CONVO_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba8394516a5a3f2cc43b5facc1a39d29d4)、[BT_MAP_NTF_FILTER_MASK_PARTICIPANT_PRESENCE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba9775c436fbf2f2211daea1b08f2a03e1)、[BT_MAP_NTF_FILTER_MASK_PARTICIPANT_CHAT_STATE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba3802bd6debad36401e16092e5837f382)、[BT_MAP_NTF_FILTER_MASK_MSG_EXT_DATA_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2bae685c7a86ab34c48a1e36ef7c5a3c9de)、[BT_MAP_NTF_FILTER_MASK_MSG_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba169927e375629a179d5326d9db81c6f1)。

MAP 通知过滤器掩码位（Notification Filter Mask Bits）。

<a id="r_ga5f8e52ddea4d8e70373306c11e0bc7cf"></a>

```c
enum bt_map_convo_param_mask { BT_MAP_CONVO_PARAM_MASK_CONVO_NAME = (1UL << (0)) , BT_MAP_CONVO_PARAM_MASK_CONVO_LAST_ACTIVITY = (1UL << (1)) , BT_MAP_CONVO_PARAM_MASK_READ_STATUS = (1UL << (2)) , BT_MAP_CONVO_PARAM_MASK_VER_CNTR = (1UL << (3)) , BT_MAP_CONVO_PARAM_MASK_SUMMARY = (1UL << (4)) , BT_MAP_CONVO_PARAM_MASK_PARTICIPANTS = (1UL << (5)) , BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_UCI = (1UL << (6)) , BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_DISP_NAME = (1UL << (7)) , BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_CHAT_STATE = (1UL << (8)) , BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_LAST_ACTIVITY = (1UL << (9)) , BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_X_BT_UID = (1UL << (10)) , BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_NAME = (1UL << (11)) , BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRESENCE_AVAIL = (1UL << (12)) , BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRESENCE_TEXT = (1UL << (13)) , BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRIORITY = (1UL << (14)) }
```

相关声明：[bt_map_convo_param_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5f8e52ddea4d8e70373306c11e0bc7cf)、[BT_MAP_CONVO_PARAM_MASK_CONVO_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa8bdec6724248fb7c9c03dfc68a74685d)、[BT_MAP_CONVO_PARAM_MASK_CONVO_LAST_ACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfaa09c318962d5b45ec38803e76bdde12f)、[BT_MAP_CONVO_PARAM_MASK_READ_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa219e72e5bda08cfc385be812c758e643)、[BT_MAP_CONVO_PARAM_MASK_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa59c95bdc52ee0322073f77dd0e105793)、[BT_MAP_CONVO_PARAM_MASK_SUMMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfadb591e1a00ec2aa5769da57ad9fee449)、[BT_MAP_CONVO_PARAM_MASK_PARTICIPANTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa46cefe87f4e615449d6c455f7fb46ff6)、[BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_UCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfafa05e0c6bd1e94c084c38576351e7aa1)、[BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_DISP_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa4a6ee544171c8b462b67e06ac83f1f82)、[BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_CHAT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa86c6406f1611ab59bec605c453e4de83)、[BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_LAST_ACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa5dc039eda9209a6d0e2fde493be3e539)、[BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_X_BT_UID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa3c2987c761d5b59e8dc2e32f86f2385b)、[BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa2719dcdd029ab08b613199779d03ffb4)、[BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRESENCE_AVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfaf249580f9df1595dfafe8ac26544c1cf)、[BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRESENCE_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa99d249a960b62ff69f4f2a1a13709d3a)、[BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa5d27a1c447d9f5a1b6c52b86915355c8)。

MAP 会话参数掩码位（Conversation Parameter Mask Bits）。

<a id="r_ga2fdf1a6a310fec131555fbdc62c524a2"></a>

```c
enum bt_map_msg_ext_data { BT_MAP_MSG_EXT_DATA_FACEBOOK_LIKES = 0x00 , BT_MAP_MSG_EXT_DATA_TWITTER_FOLLOWERS = 0x01 , BT_MAP_MSG_EXT_DATA_TWITTER_RETWEETS = 0x02 , BT_MAP_MSG_EXT_DATA_GOOGLE_1S = 0x03 }
```

相关声明：[bt_map_msg_ext_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga2fdf1a6a310fec131555fbdc62c524a2)、[BT_MAP_MSG_EXT_DATA_FACEBOOK_LIKES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2abced9c6dcd9d3e6b11c2c73e7480a202)、[BT_MAP_MSG_EXT_DATA_TWITTER_FOLLOWERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2a5ad011cef696acfa77ff9d36c80c727a)、[BT_MAP_MSG_EXT_DATA_TWITTER_RETWEETS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2a0aecdd208590887c87b783b9b42730e7)、[BT_MAP_MSG_EXT_DATA_GOOGLE_1S](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2a1e746d528718d93d50dba7770e6d128c)。

MAP 消息扩展数据类型（Message Extended Data Types）。

<a id="r_gaef50be9a23daf42f669fde9e067b18f3"></a>

```c
enum bt_map_modify_text { BT_MAP_MODIFY_TEXT_REPLACE = 0x00 , BT_MAP_MODIFY_TEXT_PREPEND = 0x01 }
```

相关声明：[bt_map_modify_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gaef50be9a23daf42f669fde9e067b18f3)、[BT_MAP_MODIFY_TEXT_REPLACE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggaef50be9a23daf42f669fde9e067b18f3a8c6316a42d350cd845a68110708a146e)、[BT_MAP_MODIFY_TEXT_PREPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggaef50be9a23daf42f669fde9e067b18f3a219ffe5a4584dd6eb7fdc6150389cf4c)。

MAP 修改文本取值（Modify Text Values）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_ga04bf8d4d99165e7cf49613fe82432ca7"></a>

```c
int bt_map_mce_mas_rfcomm_connect (struct bt_conn *conn, struct bt_map_mce_mas *mce_mas, const struct bt_map_mce_mas_cb *cb, uint8_t channel)
```

相关声明：[bt_map_mce_mas_rfcomm_connect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga04bf8d4d99165e7cf49613fe82432ca7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bt_map_mce_mas_cb](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 RFCOMM 连接 MAP 客户端的消息访问服务（MAS）。

<a id="r_ga3202aee97828ecd8ed6f39f9eb6c98f2"></a>

```c
int bt_map_mce_mas_rfcomm_disconnect (struct bt_map_mce_mas *mce_mas)
```

相关声明：[bt_map_mce_mas_rfcomm_disconnect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga3202aee97828ecd8ed6f39f9eb6c98f2)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)。

通过 RFCOMM 断开 MAP 客户端的消息访问服务（MAS）连接。

<a id="r_ga539c08b47cc73a23d24bd54dcb5d6dc4"></a>

```c
int bt_map_mce_mas_l2cap_connect (struct bt_conn *conn, struct bt_map_mce_mas *mce_mas, const struct bt_map_mce_mas_cb *cb, uint16_t psm)
```

相关声明：[bt_map_mce_mas_l2cap_connect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga539c08b47cc73a23d24bd54dcb5d6dc4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bt_map_mce_mas_cb](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 L2CAP 连接 MAP 客户端的消息访问服务（MAS）。

<a id="r_ga1a00c2b646b9a10c3deb6f4953f04683"></a>

```c
int bt_map_mce_mas_l2cap_disconnect (struct bt_map_mce_mas *mce_mas)
```

相关声明：[bt_map_mce_mas_l2cap_disconnect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga1a00c2b646b9a10c3deb6f4953f04683)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)。

通过 L2CAP 断开 MAP 客户端的消息访问服务（MAS）连接。

<a id="r_ga666d58fd65852372fa22328b6cd9aa82"></a>

```c
struct net_buf * bt_map_mce_mas_create_pdu (struct bt_map_mce_mas *mce_mas, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_map_mce_mas_create_pdu](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga666d58fd65852372fa22328b6cd9aa82)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 MAP 客户端的消息访问服务（MAS）创建协议数据单元（PDU）。

<a id="r_ga01d1677204f204feb2474a61bfcc118a"></a>

```c
int bt_map_mce_mas_connect (struct bt_map_mce_mas *mce_mas, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_connect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga01d1677204f204feb2474a61bfcc118a)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送对象交换协议（OBEX）连接请求（Connect Request）。

<a id="r_ga0c58e5c7f70c15409ae9241d0b412400"></a>

```c
int bt_map_mce_mas_disconnect (struct bt_map_mce_mas *mce_mas, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_disconnect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga0c58e5c7f70c15409ae9241d0b412400)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 断开请求（Disconnect Request）。

<a id="r_gaf9836663a18ecc62b5330a1682f4b42e"></a>

```c
int bt_map_mce_mas_abort (struct bt_map_mce_mas *mce_mas, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_abort](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gaf9836663a18ecc62b5330a1682f4b42e)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 中止请求（Abort Request）。

<a id="r_ga9e6640177b225a5b7448cde8a17de4f0"></a>

```c
int bt_map_mce_mas_set_folder (struct bt_map_mce_mas *mce_mas, uint8_t flags, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_set_folder](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga9e6640177b225a5b7448cde8a17de4f0)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置文件夹请求（Set Folder Request）。

<a id="r_gad528c35977847525d781a39c50a3e793"></a>

```c
int bt_map_mce_mas_set_ntf_reg (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_set_ntf_reg](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gad528c35977847525d781a39c50a3e793)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置通知注册请求（Set Notification Registration Request）。

<a id="r_ga54fa7e185e5d949bec434935f51ae9fb"></a>

```c
int bt_map_mce_mas_get_folder_listing (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_folder_listing](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga54fa7e185e5d949bec434935f51ae9fb)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取文件夹列表请求（Get Folder Listing Request）。

<a id="r_gaf146e16f1b7950db4b5418bd27269ebb"></a>

```c
int bt_map_mce_mas_get_msg_listing (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_msg_listing](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gaf146e16f1b7950db4b5418bd27269ebb)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取消息列表请求（Get Message Listing Request）。

<a id="r_ga39795b7002cf40984b130d38179a5472"></a>

```c
int bt_map_mce_mas_get_msg (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_msg](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga39795b7002cf40984b130d38179a5472)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取消息请求（Get Message Request）。

<a id="r_gaa03c3ea1d6ec10d02412b4525dd3ffe5"></a>

```c
int bt_map_mce_mas_set_msg_status (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_set_msg_status](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gaa03c3ea1d6ec10d02412b4525dd3ffe5)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置消息状态请求（Set Message Status Request）。

<a id="r_ga54a2552080933e12b6b871bc9f898fce"></a>

```c
int bt_map_mce_mas_push_msg (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_push_msg](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga54a2552080933e12b6b871bc9f898fce)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送推送消息请求（Push Message Request）。

<a id="r_gae91fb531b7164b389994b9391fa8e51e"></a>

```c
int bt_map_mce_mas_update_inbox (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_update_inbox](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gae91fb531b7164b389994b9391fa8e51e)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送更新收件箱请求（Update Inbox Request）。

<a id="r_gabbe39f067872a6c008269d483a97d234"></a>

```c
int bt_map_mce_mas_get_mas_inst_info (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_mas_inst_info](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gabbe39f067872a6c008269d483a97d234)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取 MAS 实例信息请求（Get MAS Instance Info Request）。

<a id="r_ga3b1dc36240679618c98df515a351a5e7"></a>

```c
int bt_map_mce_mas_set_owner_status (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_set_owner_status](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga3b1dc36240679618c98df515a351a5e7)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置所有者状态请求（Set Owner Status Request）。

<a id="r_ga2206f238364c04e180153c5cff10de94"></a>

```c
int bt_map_mce_mas_get_owner_status (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_owner_status](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga2206f238364c04e180153c5cff10de94)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取所有者状态请求（Get Owner Status Request）。

<a id="r_gabdd72751375fa9a0aa1f99e75137cb9e"></a>

```c
int bt_map_mce_mas_get_convo_listing (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_get_convo_listing](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gabdd72751375fa9a0aa1f99e75137cb9e)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取会话列表请求（Get Conversation Listing Request）。

<a id="r_ga28b33d6c38af9479e56e9c2c2c0f795a"></a>

```c
int bt_map_mce_mas_set_ntf_filter (struct bt_map_mce_mas *mce_mas, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mce_mas_set_ntf_filter](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga28b33d6c38af9479e56e9c2c2c0f795a)、[bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置通知过滤器请求（Set Notification Filter Request）。

<a id="r_gabae24c99ada5dae44ca657ae96008a69"></a>

```c
int bt_map_mce_mns_register (struct bt_map_mce_mns *mce_mns, const struct bt_map_mce_mns_cb *cb)
```

相关声明：[bt_map_mce_mns_register](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#gabae24c99ada5dae44ca657ae96008a69)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[bt_map_mce_mns_cb](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md)。

注册 MAP 客户端的消息通知服务（MNS）服务器。

<a id="r_ga574790bc59c82d89010e61f535849a35"></a>

```c
int bt_map_mce_mns_rfcomm_register (struct bt_map_mce_mns_rfcomm_server *server)
```

相关声明：[bt_map_mce_mns_rfcomm_register](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga574790bc59c82d89010e61f535849a35)、[bt_map_mce_mns_rfcomm_server](../bluetooth_service_model_reference/P112_bt_map_mce_mns_rfcomm_server_结构体.md)。

注册 MAP 客户端的 MNS RFCOMM 服务器。

<a id="r_gac6fa0bcfbea7b9a2a258678f5a2b8503"></a>

```c
int bt_map_mce_mns_rfcomm_disconnect (struct bt_map_mce_mns *mce_mns)
```

相关声明：[bt_map_mce_mns_rfcomm_disconnect](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#gac6fa0bcfbea7b9a2a258678f5a2b8503)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)。

通过 RFCOMM 断开 MAP 客户端 MNS 连接。

<a id="r_ga904970bac58822ec5336ce2bab226300"></a>

```c
int bt_map_mce_mns_l2cap_register (struct bt_map_mce_mns_l2cap_server *server)
```

相关声明：[bt_map_mce_mns_l2cap_register](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga904970bac58822ec5336ce2bab226300)、[bt_map_mce_mns_l2cap_server](../bluetooth_service_model_reference/P111_bt_map_mce_mns_l2cap_server_结构体.md)。

注册 MAP 客户端的 MNS L2CAP 服务器。

<a id="r_gad4207d61fbe40c34e753132fc742aba3"></a>

```c
int bt_map_mce_mns_l2cap_disconnect (struct bt_map_mce_mns *mce_mns)
```

相关声明：[bt_map_mce_mns_l2cap_disconnect](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#gad4207d61fbe40c34e753132fc742aba3)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)。

通过 L2CAP 断开 MAP 客户端 MNS 连接。

<a id="r_ga029cb5034f7cbf059653c763e4c767c2"></a>

```c
struct net_buf * bt_map_mce_mns_create_pdu (struct bt_map_mce_mns *mce_mns, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_map_mce_mns_create_pdu](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga029cb5034f7cbf059653c763e4c767c2)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 MAP 客户端 MNS 创建协议数据单元（PDU）。

<a id="r_gaab9161c0524c74cb4b03938c26642f4a"></a>

```c
int bt_map_mce_mns_connect (struct bt_map_mce_mns *mce_mns, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mce_mns_connect](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#gaab9161c0524c74cb4b03938c26642f4a)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 连接响应（Connect Response）。

<a id="r_ga14411f8c0e8ce90824d366d28d4a2d2e"></a>

```c
int bt_map_mce_mns_disconnect (struct bt_map_mce_mns *mce_mns, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mce_mns_disconnect](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga14411f8c0e8ce90824d366d28d4a2d2e)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 断开响应（Disconnect Response）。

<a id="r_ga7309e25833e6594dc0018afe8b0a403c"></a>

```c
int bt_map_mce_mns_abort (struct bt_map_mce_mns *mce_mns, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mce_mns_abort](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga7309e25833e6594dc0018afe8b0a403c)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 中止响应（Abort Response）。

<a id="r_ga3e181d1bd37877dd8abf47a541c4b98e"></a>

```c
int bt_map_mce_mns_send_event (struct bt_map_mce_mns *mce_mns, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mce_mns_send_event](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga3e181d1bd37877dd8abf47a541c4b98e)、[bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送事件响应（Event Response）。

<a id="r_ga14815828dbf7163ab8fb0b3a8c0165b4"></a>

```c
int bt_map_mse_mas_register (struct bt_map_mse_mas *mse_mas, const struct bt_map_mse_mas_cb *cb)
```

相关声明：[bt_map_mse_mas_register](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga14815828dbf7163ab8fb0b3a8c0165b4)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[bt_map_mse_mas_cb](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md)。

注册消息访问配置文件服务器（MAP Server）的消息访问服务器（MAS）。

<a id="r_ga670bebf0edd1e8d5f7a2de5403e042d0"></a>

```c
int bt_map_mse_mas_rfcomm_register (struct bt_map_mse_mas_rfcomm_server *server)
```

相关声明：[bt_map_mse_mas_rfcomm_register](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga670bebf0edd1e8d5f7a2de5403e042d0)、[bt_map_mse_mas_rfcomm_server](../bluetooth_service_model_reference/P116_bt_map_mse_mas_rfcomm_server_结构体.md)。

注册 MAP 服务器的 MAS RFCOMM 服务器（Server）。

<a id="r_ga7db0773e3e0425f77e965fece30c3697"></a>

```c
int bt_map_mse_mas_rfcomm_disconnect (struct bt_map_mse_mas *mse_mas)
```

相关声明：[bt_map_mse_mas_rfcomm_disconnect](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga7db0773e3e0425f77e965fece30c3697)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)。

通过 RFCOMM 断开 MAP 服务器 MAS 的连接。

<a id="r_ga031515fbb0ca110532f5a1e971a01739"></a>

```c
int bt_map_mse_mas_l2cap_register (struct bt_map_mse_mas_l2cap_server *server)
```

相关声明：[bt_map_mse_mas_l2cap_register](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga031515fbb0ca110532f5a1e971a01739)、[bt_map_mse_mas_l2cap_server](../bluetooth_service_model_reference/P115_bt_map_mse_mas_l2cap_server_结构体.md)。

注册 MAP 服务器的 MAS L2CAP 服务器（Server）。

<a id="r_ga6df473fe69d8b3d183ee8385613f786f"></a>

```c
int bt_map_mse_mas_l2cap_disconnect (struct bt_map_mse_mas *mse_mas)
```

相关声明：[bt_map_mse_mas_l2cap_disconnect](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga6df473fe69d8b3d183ee8385613f786f)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)。

通过 L2CAP 断开 MAP 服务器 MAS 的连接。

<a id="r_gab1c7678b39dad5309efde0b5950a997f"></a>

```c
struct net_buf * bt_map_mse_mas_create_pdu (struct bt_map_mse_mas *mse_mas, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_map_mse_mas_create_pdu](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gab1c7678b39dad5309efde0b5950a997f)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 MAP 服务器 MAS 创建协议数据单元（PDU）。

<a id="r_gadd1da4acdd8043aa542c0fe36259898f"></a>

```c
int bt_map_mse_mas_connect (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_connect](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gadd1da4acdd8043aa542c0fe36259898f)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 连接响应（Connect Response）。

<a id="r_gabc3a8d9eb9dbc3fd028d39e4a262388b"></a>

```c
int bt_map_mse_mas_disconnect (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_disconnect](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gabc3a8d9eb9dbc3fd028d39e4a262388b)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 断开响应（Disconnect Response）。

<a id="r_ga3eee467070483854e1a84a940ee031e2"></a>

```c
int bt_map_mse_mas_abort (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_abort](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga3eee467070483854e1a84a940ee031e2)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 中止响应（Abort Response）。

<a id="r_gac972589b96cd3931044f994d4c94cf20"></a>

```c
int bt_map_mse_mas_set_folder (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_set_folder](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gac972589b96cd3931044f994d4c94cf20)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置文件夹响应（Set Folder Response）。

<a id="r_ga55641e8681932d0e31021d3803625874"></a>

```c
int bt_map_mse_mas_set_ntf_reg (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_set_ntf_reg](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga55641e8681932d0e31021d3803625874)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置通知注册响应（Set Notification Registration Response）。

<a id="r_ga8263ea5145edcfd277f73980a3fcea57"></a>

```c
int bt_map_mse_mas_get_folder_listing (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_folder_listing](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga8263ea5145edcfd277f73980a3fcea57)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取文件夹列表响应（Get Folder Listing Response）。

<a id="r_ga2833ef99d384109acf304532d1820a36"></a>

```c
int bt_map_mse_mas_get_msg_listing (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_msg_listing](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga2833ef99d384109acf304532d1820a36)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取消息列表响应（Get Message Listing Response）。

<a id="r_ga852ae34e4f8b44fea3308a42baa15ec2"></a>

```c
int bt_map_mse_mas_get_msg (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_msg](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga852ae34e4f8b44fea3308a42baa15ec2)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取消息响应（Get Message Response）。

<a id="r_ga3cfbf0a8f1f1b6a730c401dac21e9f51"></a>

```c
int bt_map_mse_mas_set_msg_status (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_set_msg_status](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga3cfbf0a8f1f1b6a730c401dac21e9f51)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置消息状态响应（Set Message Status Response）。

<a id="r_gabcd127dc45e03820079be0dc92066b89"></a>

```c
int bt_map_mse_mas_push_msg (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_push_msg](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gabcd127dc45e03820079be0dc92066b89)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送推送消息响应（Push Message Response）。

<a id="r_ga2c0ed0fdc8fee3f98e671c5ec187c8ed"></a>

```c
int bt_map_mse_mas_update_inbox (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_update_inbox](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga2c0ed0fdc8fee3f98e671c5ec187c8ed)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送更新收件箱响应（Update Inbox Response）。

<a id="r_gab50e3d126e2d35e9b6724cf3112d0892"></a>

```c
int bt_map_mse_mas_get_mas_inst_info (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_mas_inst_info](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gab50e3d126e2d35e9b6724cf3112d0892)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取 MAS 实例信息响应（Get MAS Instance Info Response）。

<a id="r_ga275eff320f980230d8d80873ad0ef3ce"></a>

```c
int bt_map_mse_mas_set_owner_status (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_set_owner_status](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga275eff320f980230d8d80873ad0ef3ce)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置所有者状态响应（Set Owner Status Response）。

<a id="r_ga37c155889cd0e2bb902da2bd25415509"></a>

```c
int bt_map_mse_mas_get_owner_status (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_owner_status](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga37c155889cd0e2bb902da2bd25415509)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取所有者状态响应（Get Owner Status Response）。

<a id="r_gadeb8072cdca241b3ad15c2116733d155"></a>

```c
int bt_map_mse_mas_get_convo_listing (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_get_convo_listing](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gadeb8072cdca241b3ad15c2116733d155)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取会话列表响应（Get Conversation Listing Response）。

<a id="r_ga3aacf3e78b40f06bbf17baada2c59e04"></a>

```c
int bt_map_mse_mas_set_ntf_filter (struct bt_map_mse_mas *mse_mas, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_map_mse_mas_set_ntf_filter](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga3aacf3e78b40f06bbf17baada2c59e04)、[bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送设置通知过滤器响应（Set Notification Filter Response）。

<a id="r_gadf2f434d2565703781a46851d4444a80"></a>

```c
int bt_map_mse_mns_rfcomm_connect (struct bt_conn *conn, struct bt_map_mse_mns *mse_mns, const struct bt_map_mse_mns_cb *cb, uint8_t channel)
```

相关声明：[bt_map_mse_mns_rfcomm_connect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#gadf2f434d2565703781a46851d4444a80)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[bt_map_mse_mns_cb](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 RFCOMM 连接 MAP 服务器 MNS。

<a id="r_ga0513491439278cadc6897f9cb932cd67"></a>

```c
int bt_map_mse_mns_rfcomm_disconnect (struct bt_map_mse_mns *mse_mns)
```

相关声明：[bt_map_mse_mns_rfcomm_disconnect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#ga0513491439278cadc6897f9cb932cd67)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)。

通过 RFCOMM 断开 MAP 服务器 MNS 连接。

<a id="r_ga46fc48dafd5c173199274be1a616a109"></a>

```c
int bt_map_mse_mns_l2cap_connect (struct bt_conn *conn, struct bt_map_mse_mns *mse_mns, const struct bt_map_mse_mns_cb *cb, uint16_t psm)
```

相关声明：[bt_map_mse_mns_l2cap_connect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#ga46fc48dafd5c173199274be1a616a109)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[bt_map_mse_mns_cb](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 L2CAP 连接 MAP 服务器 MNS。

<a id="r_ga305dd055de4831ef68cff7b5346a4b5d"></a>

```c
int bt_map_mse_mns_l2cap_disconnect (struct bt_map_mse_mns *mse_mns)
```

相关声明：[bt_map_mse_mns_l2cap_disconnect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#ga305dd055de4831ef68cff7b5346a4b5d)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)。

通过 L2CAP 断开 MAP 服务器 MNS 连接。

<a id="r_gaa0298eb521d012a910eba4a552d55fa7"></a>

```c
struct net_buf * bt_map_mse_mns_create_pdu (struct bt_map_mse_mns *mse_mns, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_map_mse_mns_create_pdu](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#gaa0298eb521d012a910eba4a552d55fa7)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 MAP 服务器 MNS 创建协议数据单元（PDU）。

<a id="r_ga7bedc538a126b8c4d4c6fb393fc06218"></a>

```c
int bt_map_mse_mns_connect (struct bt_map_mse_mns *mse_mns, struct net_buf *buf)
```

相关声明：[bt_map_mse_mns_connect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#ga7bedc538a126b8c4d4c6fb393fc06218)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送对象交换协议（OBEX）连接请求（Connect Request）。

<a id="r_ga08513e5aa2b54e4474ee647232c0af91"></a>

```c
int bt_map_mse_mns_disconnect (struct bt_map_mse_mns *mse_mns, struct net_buf *buf)
```

相关声明：[bt_map_mse_mns_disconnect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#ga08513e5aa2b54e4474ee647232c0af91)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 断开请求（Disconnect Request）。

<a id="r_gafc1be36425faa6242ed8eb4f21d76b5f"></a>

```c
int bt_map_mse_mns_abort (struct bt_map_mse_mns *mse_mns, struct net_buf *buf)
```

相关声明：[bt_map_mse_mns_abort](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#gafc1be36425faa6242ed8eb4f21d76b5f)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 中止请求（Abort Request）。

<a id="r_gac8776edbbf4e2f891246cba86a1df589"></a>

```c
int bt_map_mse_mns_send_event (struct bt_map_mse_mns *mse_mns, bool final, struct net_buf *buf)
```

相关声明：[bt_map_mse_mns_send_event](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#gac8776edbbf4e2f891246cba86a1df589)、[bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送事件通知请求（Event Notification Request）。


## 2.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/bluetooth/uuid.h](../api_source_supplement_reference/P020_uuid.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/l2cap.h](../api_source_system_reference/P016_l2cap.h_源码浏览.md)
- [zephyr/bluetooth/classic/goep.h](../api_source_supplement_reference/P081_goep.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P002_map.h_源码浏览.md)
- [bt_map_mce_mas_cb](../bluetooth_service_model_reference/P108_bt_map_mce_mas_cb_结构体.md)
- [bt_map_mce_mas](../bluetooth_service_model_reference/P107_bt_map_mce_mas_结构体.md)
- [bt_map_mce_mns_rfcomm_server](../bluetooth_service_model_reference/P112_bt_map_mce_mns_rfcomm_server_结构体.md)
- [bt_map_mce_mns_l2cap_server](../bluetooth_service_model_reference/P111_bt_map_mce_mns_l2cap_server_结构体.md)
- [bt_map_mce_mns_cb](../bluetooth_service_model_reference/P110_bt_map_mce_mns_cb_结构体.md)
- [bt_map_mce_mns](../bluetooth_service_model_reference/P109_bt_map_mce_mns_结构体.md)
- [bt_map_mse_mas_rfcomm_server](../bluetooth_service_model_reference/P116_bt_map_mse_mas_rfcomm_server_结构体.md)
- [bt_map_mse_mas_l2cap_server](../bluetooth_service_model_reference/P115_bt_map_mse_mas_l2cap_server_结构体.md)
- [bt_map_mse_mas_cb](../bluetooth_service_model_reference/P114_bt_map_mse_mas_cb_结构体.md)
- [bt_map_mse_mas](../bluetooth_service_model_reference/P113_bt_map_mse_mas_结构体.md)
- [bt_map_mse_mns_cb](../bluetooth_service_model_reference/P118_bt_map_mse_mns_cb_结构体.md)
- [bt_map_mse_mns](../bluetooth_service_model_reference/P117_bt_map_mse_mns_结构体.md)
- [BT_MAP_MANDATORY_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga109c4eba9cdfc3b938344e2348db940e)
- [BT_MAP_UUID_MAS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga13bacf997de99061640a03a5a6393d55)
- [BT_MAP_UUID_MNS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gae8154c6af172a42e5cdbbcf2d1f42ade)
- [BT_MAP_FILLER_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga166e2fb2e91f001dc8c612b4771855bd)
- [BT_MAP_HDR_TYPE_SEND_EVENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5066d3a3d110307380af2e660fa1db39)
- [BT_MAP_HDR_TYPE_SET_NTF_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga95985386e036f2c4914c1dc2060b2b2c)
- [BT_MAP_HDR_TYPE_GET_FOLDER_LISTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gadd74dc8a80aa351a62d5d50a2f49e955)
- [BT_MAP_HDR_TYPE_GET_MSG_LISTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gaaef898bb0e87c7ddbd95943dd7941ab8)
- [BT_MAP_HDR_TYPE_GET_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga59cd61db282e7c78045b1c485e7af843)
- [BT_MAP_HDR_TYPE_SET_MSG_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga7b11a9d0535fe964a8b9e523428fce82)
- [BT_MAP_HDR_TYPE_PUSH_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga3f11b300752a32f6cb8f915d5230c7ad)
- [BT_MAP_HDR_TYPE_UPDATE_INBOX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga92aa24fa6950c5704ab8ad86d47e7077)
- [BT_MAP_HDR_TYPE_GET_MAS_INST_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga9477fa19750161e79bae0bf7053ccb30)
- [BT_MAP_HDR_TYPE_SET_OWNER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gafb909e47193e0ef0549c4b0c1f98002e)
- [BT_MAP_HDR_TYPE_GET_OWNER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gae2ed8a5602fc3796d65f825af2f7192e)
- [BT_MAP_HDR_TYPE_GET_CONVO_LISTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gada79ac46d960d75c784617aeeba935d3)
- [BT_MAP_HDR_TYPE_SET_NTF_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gaa1ba29f46678e49896ab0fc7a7b5c413)
- [bt_map_supported_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga6d4c3231e2e64190c6ccc30b4d5f822c)
- [BT_MAP_NTF_REG_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822cae5fa5f417d064a1b85e9db70a5ce94e5)
- [BT_MAP_NTF_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822cac4a88df48198a497da4a94ec124bb735)
- [BT_MAP_BROWSING_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caec96609ac47f6cf1e779d049687f2e63)
- [BT_MAP_UPLOADING_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca572d7eb54deb371cee55c0149f21d6db)
- [BT_MAP_DELETE_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caa7e8028e50f7903aefd379d76695408f)
- [BT_MAP_INST_INFO_FEATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca32cf970e22e8f082293225b5a614de8d)
- [BT_MAP_EXT_EVENT_REPORT_V11](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca7467b703f0cf9d760d6d18e0dd6dfa7f)
- [BT_MAP_EXT_EVENT_REPORT_V12](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca2cbc347cb637a951868052e58eb3dab9)
- [BT_MAP_MSG_FORMAT_V11](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caa6de591a1e2d5936263741f273c9fb8a)
- [BT_MAP_MSG_LISTING_FORMAT_V11](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822cae28c62057713e3a7318cf85eaa7c337e)
- [BT_MAP_PERSISTENT_MSG_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca5e63f64fb534af8295995a0fbec364df)
- [BT_MAP_DB_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca71243a44c4d5a105c02b49318302fb7a)
- [BT_MAP_FOLDER_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca2c7cbab7fe254b975668563039c7ace8)
- [BT_MAP_CONVO_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca8d214b20b66be2264fb8da2d9feb93d0)
- [BT_MAP_PARTICIPANT_PRESENCE_CHANGE_NTF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca2843780dad72eaa1d84cec56077cff93)
- [BT_MAP_PARTICIPANT_CHAT_STATE_CHANGE_NTF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca1bc10abe061f68c3de72c37b5307c484)
- [BT_MAP_PBAP_CONTACT_XREF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca679c98163ee9b3114c7adf64b6976a9e)
- [BT_MAP_NTF_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca3353469789a5a72f4fc97dabed1d4dcf)
- [BT_MAP_UTC_OFFSET_TIMESTAMP_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca9aaa859278454e081c5fe5e83dfded5d)
- [BT_MAP_SUPPORTED_FEATURES_CONN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caa76c12d6babf2df623f28f58ed1912d0)
- [BT_MAP_CONVO_LISTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca35f15fe0fba34519ff0d1087c2e32c4c)
- [BT_MAP_OWNER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822ca6aa30c2d7dccbe630756c1f1e4f7a141)
- [BT_MAP_MSG_FORWARDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga6d4c3231e2e64190c6ccc30b4d5f822caccc791a50cc33ef4d62d6b126c1ba898)
- [bt_map_supported_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5bb2e0b7951bde5042fbb9c4e0c7cc26)
- [BT_MAP_MSG_TYPE_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26ae0396ce6457b9792d564195f906fafe3)
- [BT_MAP_MSG_TYPE_SMS_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a0f4bd271fb4a331e66dafde2a04fd62a)
- [BT_MAP_MSG_TYPE_SMS_CDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a803694148d134338a83f365390929505)
- [BT_MAP_MSG_TYPE_MMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a9f65cf3b8d5a5855219599ed656ea56c)
- [BT_MAP_MSG_TYPE_IM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5bb2e0b7951bde5042fbb9c4e0c7cc26a038430c6eea453638a2fc3351315b638)
- [bt_map_set_folder_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5678131af7da533ff8b751555542933e)
- [BT_MAP_SET_FOLDER_FLAGS_ROOT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5678131af7da533ff8b751555542933eaa5d3b0ad2bf7f8600ad059132aaed665)
- [BT_MAP_SET_FOLDER_FLAGS_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5678131af7da533ff8b751555542933ead7b0402847a837a69055dcf4b6fad674)
- [BT_MAP_SET_FOLDER_FLAGS_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5678131af7da533ff8b751555542933ea8b13f5d7fc245c7b66a65e0845ed7edc)
- [bt_map_appl_param_tag_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga7310a116a939b40d7ee346371b5ccd88)
- [BT_MAP_APPL_PARAM_TAG_ID_MAX_LIST_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a2df85ffb7e034732fb608c6935af9297)
- [BT_MAP_APPL_PARAM_TAG_ID_LIST_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7227e024472a421c86c3cb7a0db65e55)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_MSG_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88af39bad93c459fcb86b9583a1519c070b)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_PERIOD_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7627a7496631fbe6326e4c1c43e4877c)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_PERIOD_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a2071ba2e3ec0dc8b5adc8b97a37a010d)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_READ_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88aa1b59e01c63abc3ccc7ee54ca27e9296)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_RECIPIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ac6118aa692c3c382ce7630ac2d499aac)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_ORIGINATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88adb08ba0bbc13653357e835dcd6fa5770)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a637ac76aafe5a586819b9897acc7d1da)
- [BT_MAP_APPL_PARAM_TAG_ID_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad53697174462dfe4d2d592bf71bf180c)
- [BT_MAP_APPL_PARAM_TAG_ID_TRANSPARENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a595f6e5f7eac3c57dccf13e1e45dfd6b)
- [BT_MAP_APPL_PARAM_TAG_ID_RETRY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a19b5e72c512c29b5cfbe58dbdaf63064)
- [BT_MAP_APPL_PARAM_TAG_ID_NEW_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a4871d9d7da47983cd5fd7a7718ab2478)
- [BT_MAP_APPL_PARAM_TAG_ID_NTF_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88aee3ebbef8eb74deefedb414daea2dc1e)
- [BT_MAP_APPL_PARAM_TAG_ID_MAS_INST_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a170d3717ab48a7f6a63e8bd66d1cb228)
- [BT_MAP_APPL_PARAM_TAG_ID_PARAM_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a563fbb6001387da1389713be552fec13)
- [BT_MAP_APPL_PARAM_TAG_ID_FOLDER_LISTING_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a1aca8ccd385944cb73f03568123dc1e3)
- [BT_MAP_APPL_PARAM_TAG_ID_LISTING_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88aa9241c4f620f61717160d5dbc9dc5389)
- [BT_MAP_APPL_PARAM_TAG_ID_SUBJECT_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a15c0a2959d67e24ed18203cd8c9fe46a)
- [BT_MAP_APPL_PARAM_TAG_ID_CHARSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad1d1edb33a8147e1d96400607e8f3f1e)
- [BT_MAP_APPL_PARAM_TAG_ID_FRACTION_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88acfef6214cbd687aa5ad7ee4d8d3a4a2d)
- [BT_MAP_APPL_PARAM_TAG_ID_FRACTION_DELIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a8651767d6b1c5dc6f0affac25014aeaa)
- [BT_MAP_APPL_PARAM_TAG_ID_STATUS_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a5622480195120444b2f200e79db09499)
- [BT_MAP_APPL_PARAM_TAG_ID_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a4ee0642cd16aa8e1ce5224118968f9ee)
- [BT_MAP_APPL_PARAM_TAG_ID_MSE_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a0bb8acb58e8983793bb787ae8e6d4033)
- [BT_MAP_APPL_PARAM_TAG_ID_DB_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7f9d301f9383d8179611344d18f03094)
- [BT_MAP_APPL_PARAM_TAG_ID_CONVO_LISTING_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a8f4a492c9619ec1b78124f0509b93857)
- [BT_MAP_APPL_PARAM_TAG_ID_PRESENCE_AVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a7636683c2efff7c4c8d59a141c6e12b6)
- [BT_MAP_APPL_PARAM_TAG_ID_PRESENCE_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a06ae16f7d6a3a247e5e1771254df0ea9)
- [BT_MAP_APPL_PARAM_TAG_ID_LAST_ACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a6f5914896a591c0008fb744506ec98d4)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_LAST_ACTIVITY_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a5ec11c380b39a38cade5acd06545b1a1)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_LAST_ACTIVITY_END](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad49f0edd1a6e1c1da5a37abd552cc6b1)
- [BT_MAP_APPL_PARAM_TAG_ID_CHAT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88adaad04f88448466dd606527157d74cc7)
- [BT_MAP_APPL_PARAM_TAG_ID_CONVO_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a72083eddb755825e5899dfddbcc10085)
- [BT_MAP_APPL_PARAM_TAG_ID_FOLDER_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a706346ca21cb1f76c22dc02af1076b04)
- [BT_MAP_APPL_PARAM_TAG_ID_FILTER_MSG_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a600395d6f4620dffee2447ae8b9a4fbe)
- [BT_MAP_APPL_PARAM_TAG_ID_NTF_FILTER_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a161b7d1952483a47eee81dfd98ce831c)
- [BT_MAP_APPL_PARAM_TAG_ID_CONVO_PARAM_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a79da1ebc8b5e7e0d1098d4b022fa8da7)
- [BT_MAP_APPL_PARAM_TAG_ID_OWNER_UCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88ad3058d06b585289586c5cccaab548bc2)
- [BT_MAP_APPL_PARAM_TAG_ID_EXT_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a81297adf58afc780a00afe8ef4a70c95)
- [BT_MAP_APPL_PARAM_TAG_ID_MAP_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a9f08b382471f807452d9cf7e1bff1b3b)
- [BT_MAP_APPL_PARAM_TAG_ID_MSG_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a6b4d28c95336af96c06a71f6cb40060b)
- [BT_MAP_APPL_PARAM_TAG_ID_MODIFY_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7310a116a939b40d7ee346371b5ccd88a208c8d9ea3195b7d70ab2e7ccae6671d)
- [bt_map_filter_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga7c4ba8b9727c454a54a2178d584dfcb7)
- [BT_MAP_FILTER_MSG_TYPE_NO_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7adfc6a259bbc5d1b6a0b30d57d1a5b7a9)
- [BT_MAP_FILTER_MSG_TYPE_SMS_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a2ab7b8a63e2dae0bf8d82e5c7aae3038)
- [BT_MAP_FILTER_MSG_TYPE_SMS_CDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a9df74f88cb18833440816218a610527c)
- [BT_MAP_FILTER_MSG_TYPE_EMAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a37bca39682be9efa27f906754d972b7d)
- [BT_MAP_FILTER_MSG_TYPE_MMS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7a1b10e235398a004168731de140b7e6d8)
- [BT_MAP_FILTER_MSG_TYPE_IM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7c4ba8b9727c454a54a2178d584dfcb7ab80d08d33c7fc5adc1483b1be64390c0)
- [bt_map_filter_read_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gabf5f60778a9adf113e86e559095dd66f)
- [BT_MAP_FILTER_READ_STATUS_NO_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabf5f60778a9adf113e86e559095dd66fa0c7b3c3b9c8f0d9c514a9730d57d7738)
- [BT_MAP_FILTER_READ_STATUS_UNREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabf5f60778a9adf113e86e559095dd66fae90806b4b223afc531d74dd1819ff7b3)
- [BT_MAP_FILTER_READ_STATUS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabf5f60778a9adf113e86e559095dd66faf9e8514d6411d25bc71a33e7f351f93f)
- [bt_map_filter_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga4f1f483d5edfaa151a11086caac24e5c)
- [BT_MAP_FILTER_PRIORITY_NO_FILTERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4f1f483d5edfaa151a11086caac24e5ca0f8654affc09e99bad440d2b9faeb163)
- [BT_MAP_FILTER_PRIORITY_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4f1f483d5edfaa151a11086caac24e5ca66220e415b9164fe41a19e423b4aad90)
- [BT_MAP_FILTER_PRIORITY_NON_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4f1f483d5edfaa151a11086caac24e5ca12b73e28e320ba1bf3aa8edf44b053cd)
- [bt_map_attachment](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga34cee2f295fee5b00bced31753f03b25)
- [BT_MAP_ATTACHMENT_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga34cee2f295fee5b00bced31753f03b25a74198afdf437d36971d5cf4fdcaab5b8)
- [BT_MAP_ATTACHMENT_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga34cee2f295fee5b00bced31753f03b25a089baca6845a803dda4b7e506e452b5b)
- [bt_map_transparent](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga215e8bd71131e739b19f5f5ee57904e6)
- [BT_MAP_TRANSPARENT_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga215e8bd71131e739b19f5f5ee57904e6a5f1552a26d09f1c696f828967222707f)
- [BT_MAP_TRANSPARENT_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga215e8bd71131e739b19f5f5ee57904e6addfabaeaa7d8903c81b41c9844514849)
- [bt_map_retry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga4a9fc0bfa14b5e91491aec130e396429)
- [BT_MAP_RETRY_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4a9fc0bfa14b5e91491aec130e396429a4955b62b432b783eb774d704e2f2b4e2)
- [BT_MAP_RETRY_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga4a9fc0bfa14b5e91491aec130e396429a0215a73c93fe79bbd9fc28b34af31057)
- [bt_map_new_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga8dcd4f8704a2b1cab77b2279d7f2024f)
- [BT_MAP_NEW_MSG_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8dcd4f8704a2b1cab77b2279d7f2024fabe2ef316affe063b7634ca5e5f2e0351)
- [BT_MAP_NEW_MSG_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8dcd4f8704a2b1cab77b2279d7f2024fa735aac580ed7fae38d10bcc41f2b393a)
- [bt_map_ntf_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga8b805587e1abb311367e59d80d223516)
- [BT_MAP_NTF_STATUS_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8b805587e1abb311367e59d80d223516a8c7e4fd24ff699c52a7ecba484923cfb)
- [BT_MAP_NTF_STATUS_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga8b805587e1abb311367e59d80d223516a25fc04d24537a005dc4674d29ad48357)
- [bt_map_param_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gadec3f7d6faccc656739a7b7a88c10387)
- [BT_MAP_PARAM_MASK_SUBJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387aac91fbe72b91381095f4f2f32e7be327)
- [BT_MAP_PARAM_MASK_DATETIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a898d380bc11251e69d4525c2e3f5fcbe)
- [BT_MAP_PARAM_MASK_SENDER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a1cad006d6e9d8740e929a801a3a3593f)
- [BT_MAP_PARAM_MASK_SENDER_ADDRESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a0c4cac1477808905597af3d1373663d4)
- [BT_MAP_PARAM_MASK_RECIPIENT_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a90f5931d1fe65f3f2b0718c357e45740)
- [BT_MAP_PARAM_MASK_RECIPIENT_ADDRESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387aeaaa6e5cad8201d747248f40cef19038)
- [BT_MAP_PARAM_MASK_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387ab62fbb3ed1d684c4e0e86e0d04ee6995)
- [BT_MAP_PARAM_MASK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a8c7c06f8ebdd5e433e926345d62c092b)
- [BT_MAP_PARAM_MASK_RECEPTION_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a1b55581c15bf6d915a748fff1655f2eb)
- [BT_MAP_PARAM_MASK_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a5b0a0672211d6e9a0e377baaa16f449a)
- [BT_MAP_PARAM_MASK_ATTACHMENT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a1c86d02bc4003273da0e84ebaeaa4ae8)
- [BT_MAP_PARAM_MASK_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a07145a14474b470e1dc9143d115add4f)
- [BT_MAP_PARAM_MASK_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387afb8f5b6bde20c9526dc520dea12f5fc6)
- [BT_MAP_PARAM_MASK_SENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a47987b441c785b7657f9323ec7858d51)
- [BT_MAP_PARAM_MASK_PROTECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a302b63d08cb7ff36204c2f390b746375)
- [BT_MAP_PARAM_MASK_REPLYTO_ADDRESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a295391beee4e7f92c9e5745785da214d)
- [BT_MAP_PARAM_MASK_DELIVERY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387acb4ed5200b771b50ec1481a779230850)
- [BT_MAP_PARAM_MASK_CONVO_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387ac421a69062c73e6eeae9c1730072cfe8)
- [BT_MAP_PARAM_MASK_CONVO_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a21a483901085035c22fc3baf02931df6)
- [BT_MAP_PARAM_MASK_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387a001c4dc6084e12938867c4a1eb7316ea)
- [BT_MAP_PARAM_MASK_ATTACHMENT_MIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggadec3f7d6faccc656739a7b7a88c10387aac5a5819c4a284c9067951724cd5e794)
- [bt_map_charset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga0fa30e8b33826204f0625a2223cfaf1c)
- [BT_MAP_CHARSET_NATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga0fa30e8b33826204f0625a2223cfaf1ca104a2dd364f1e86b9b5f4cd8fea38011)
- [BT_MAP_CHARSET_UTF8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga0fa30e8b33826204f0625a2223cfaf1ca45f4dd02d1e4c1ce1ceef8be95684a51)
- [bt_map_fraction_request](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga430b14f450167b13329f54377473b699)
- [BT_MAP_FRACTION_REQUEST_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga430b14f450167b13329f54377473b699a1a041e3eed1744fe8d02908be402b0a4)
- [BT_MAP_FRACTION_REQUEST_NEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga430b14f450167b13329f54377473b699a22d8803a6310974137af6d8bc0c9e6a8)
- [bt_map_fraction_deliver](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga3d3327344323fae6f7a2b1ebca459db0)
- [BT_MAP_FRACTION_DELIVER_MORE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga3d3327344323fae6f7a2b1ebca459db0ab4134b8e2c9987789fa541627d9ab19f)
- [BT_MAP_FRACTION_DELIVER_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga3d3327344323fae6f7a2b1ebca459db0aebc96aeb807ea78da5d8714b1213e6f7)
- [bt_map_status_ind](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gabd4c099cc62671f53edec84eb04c50ff)
- [BT_MAP_STATUS_IND_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabd4c099cc62671f53edec84eb04c50ffa64afbc9334b9ee926b11dd473d70e0aa)
- [BT_MAP_STATUS_IND_DELETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabd4c099cc62671f53edec84eb04c50ffad1adaa8853f8bca4f4d21b378caeaf19)
- [BT_MAP_STATUS_IND_EXTENDED_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggabd4c099cc62671f53edec84eb04c50ffaf9dd6096a95f6f75140d2d37d12e24b3)
- [bt_map_status_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga7af9d1e4244a00f8d2ae607f590fea94)
- [BT_MAP_STATUS_VAL_NO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7af9d1e4244a00f8d2ae607f590fea94a28da6d9711231be9117aec9feb9104f4)
- [BT_MAP_STATUS_VAL_YES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga7af9d1e4244a00f8d2ae607f590fea94af5d7d30b5e5d6f0e8a4dd5ae42104bf8)
- [bt_map_presence](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga9523beb219a00ac4e6dba3e021b491d4)
- [BT_MAP_PRESENCE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a9a458e69d88a1f2c3be14c4c69c99b39)
- [BT_MAP_PRESENCE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a4affc47380cbcbbfcb819092d9c5cfd5)
- [BT_MAP_PRESENCE_ONLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4ade1acc46b57740b9c113cdf4ea8a502f)
- [BT_MAP_PRESENCE_AWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a98e509fe029643bb5f281b9274c70583)
- [BT_MAP_PRESENCE_DO_NOT_DISTURB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a3c1a5486acfe0d06fa935f34c5bf0d1c)
- [BT_MAP_PRESENCE_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4afc2b4a0338e768d25f200efe3c14081a)
- [BT_MAP_PRESENCE_IN_A_MEETING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga9523beb219a00ac4e6dba3e021b491d4a4d4a9258001731ffb4ea74d807394050)
- [bt_map_chat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gace38e2a78aaba1e2c48572e0d247e68c)
- [BT_MAP_CHAT_STATE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68cad9c127c32a580302536aa13cddd52085)
- [BT_MAP_CHAT_STATE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca179f10a2a6dd6184f4604794f2bb170f)
- [BT_MAP_CHAT_STATE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca1bb84095702eb5c6263a6ee908a6d1c6)
- [BT_MAP_CHAT_STATE_COMPOSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca95cb2a4eb0e6d8d2f2dd9f03a3c7c720)
- [BT_MAP_CHAT_STATE_PAUSED_COMPOSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68cacfffcf3cef8adddd1e1768fda9cdcf6d)
- [BT_MAP_CHAT_STATE_GONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggace38e2a78aaba1e2c48572e0d247e68ca496b9d0393213a460a0b0bd2c8e4ba33)
- [bt_map_ntf_filter_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5acd8d8cfc6358140438860067970e2b)
- [BT_MAP_NTF_FILTER_MASK_NEW_MSG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba77669e589a872268da67098ef008f3eb)
- [BT_MAP_NTF_FILTER_MASK_MSG_DELETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba88aa3bd1aeac147410ae96e8c7de43f9)
- [BT_MAP_NTF_FILTER_MASK_MSG_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2bad0ef68fc6a11e2429f67e1d6564597ef)
- [BT_MAP_NTF_FILTER_MASK_SENDING_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba5e21b8db192673e5b6e3146ed5b04dba)
- [BT_MAP_NTF_FILTER_MASK_SENDING_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba47d696ec191c6a0463ce70d5742616ad)
- [BT_MAP_NTF_FILTER_MASK_DELIVERY_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2baf34804c0b883c1a172c92ba237e05817)
- [BT_MAP_NTF_FILTER_MASK_DELIVERY_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2baa8e1626a89d2824b2fa3d6723a3a45cd)
- [BT_MAP_NTF_FILTER_MASK_MEM_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba83158a4308e7e89422541f2120e9baeb)
- [BT_MAP_NTF_FILTER_MASK_MEM_AVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2baa869867c70b17e91f726f27c6cbcacda)
- [BT_MAP_NTF_FILTER_MASK_READ_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2bab1a7d0518b5555eb63fb7ecee7e43bc9)
- [BT_MAP_NTF_FILTER_MASK_CONVO_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba8394516a5a3f2cc43b5facc1a39d29d4)
- [BT_MAP_NTF_FILTER_MASK_PARTICIPANT_PRESENCE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba9775c436fbf2f2211daea1b08f2a03e1)
- [BT_MAP_NTF_FILTER_MASK_PARTICIPANT_CHAT_STATE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba3802bd6debad36401e16092e5837f382)
- [BT_MAP_NTF_FILTER_MASK_MSG_EXT_DATA_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2bae685c7a86ab34c48a1e36ef7c5a3c9de)
- [BT_MAP_NTF_FILTER_MASK_MSG_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5acd8d8cfc6358140438860067970e2ba169927e375629a179d5326d9db81c6f1)
- [bt_map_convo_param_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga5f8e52ddea4d8e70373306c11e0bc7cf)
- [BT_MAP_CONVO_PARAM_MASK_CONVO_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa8bdec6724248fb7c9c03dfc68a74685d)
- [BT_MAP_CONVO_PARAM_MASK_CONVO_LAST_ACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfaa09c318962d5b45ec38803e76bdde12f)
- [BT_MAP_CONVO_PARAM_MASK_READ_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa219e72e5bda08cfc385be812c758e643)
- [BT_MAP_CONVO_PARAM_MASK_VER_CNTR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa59c95bdc52ee0322073f77dd0e105793)
- [BT_MAP_CONVO_PARAM_MASK_SUMMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfadb591e1a00ec2aa5769da57ad9fee449)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa46cefe87f4e615449d6c455f7fb46ff6)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_UCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfafa05e0c6bd1e94c084c38576351e7aa1)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_DISP_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa4a6ee544171c8b462b67e06ac83f1f82)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_CHAT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa86c6406f1611ab59bec605c453e4de83)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_LAST_ACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa5dc039eda9209a6d0e2fde493be3e539)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_X_BT_UID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa3c2987c761d5b59e8dc2e32f86f2385b)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa2719dcdd029ab08b613199779d03ffb4)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRESENCE_AVAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfaf249580f9df1595dfafe8ac26544c1cf)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRESENCE_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa99d249a960b62ff69f4f2a1a13709d3a)
- [BT_MAP_CONVO_PARAM_MASK_PARTICIPANT_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga5f8e52ddea4d8e70373306c11e0bc7cfa5d27a1c447d9f5a1b6c52b86915355c8)
- [bt_map_msg_ext_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ga2fdf1a6a310fec131555fbdc62c524a2)
- [BT_MAP_MSG_EXT_DATA_FACEBOOK_LIKES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2abced9c6dcd9d3e6b11c2c73e7480a202)
- [BT_MAP_MSG_EXT_DATA_TWITTER_FOLLOWERS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2a5ad011cef696acfa77ff9d36c80c727a)
- [BT_MAP_MSG_EXT_DATA_TWITTER_RETWEETS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2a0aecdd208590887c87b783b9b42730e7)
- [BT_MAP_MSG_EXT_DATA_GOOGLE_1S](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gga2fdf1a6a310fec131555fbdc62c524a2a1e746d528718d93d50dba7770e6d128c)
- [bt_map_modify_text](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#gaef50be9a23daf42f669fde9e067b18f3)
- [BT_MAP_MODIFY_TEXT_REPLACE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggaef50be9a23daf42f669fde9e067b18f3a8c6316a42d350cd845a68110708a146e)
- [BT_MAP_MODIFY_TEXT_PREPEND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html#ggaef50be9a23daf42f669fde9e067b18f3a219ffe5a4584dd6eb7fdc6150389cf4c)
- [bt_map_mce_mas_rfcomm_connect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga04bf8d4d99165e7cf49613fe82432ca7)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_map_mce_mas_rfcomm_disconnect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga3202aee97828ecd8ed6f39f9eb6c98f2)
- [bt_map_mce_mas_l2cap_connect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga539c08b47cc73a23d24bd54dcb5d6dc4)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_map_mce_mas_l2cap_disconnect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga1a00c2b646b9a10c3deb6f4953f04683)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_map_mce_mas_create_pdu](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga666d58fd65852372fa22328b6cd9aa82)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bt_map_mce_mas_connect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga01d1677204f204feb2474a61bfcc118a)
- [bt_map_mce_mas_disconnect](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga0c58e5c7f70c15409ae9241d0b412400)
- [bt_map_mce_mas_abort](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gaf9836663a18ecc62b5330a1682f4b42e)
- [bt_map_mce_mas_set_folder](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga9e6640177b225a5b7448cde8a17de4f0)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_map_mce_mas_set_ntf_reg](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gad528c35977847525d781a39c50a3e793)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_map_mce_mas_get_folder_listing](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga54fa7e185e5d949bec434935f51ae9fb)
- [bt_map_mce_mas_get_msg_listing](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gaf146e16f1b7950db4b5418bd27269ebb)
- [bt_map_mce_mas_get_msg](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga39795b7002cf40984b130d38179a5472)
- [bt_map_mce_mas_set_msg_status](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gaa03c3ea1d6ec10d02412b4525dd3ffe5)
- [bt_map_mce_mas_push_msg](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga54a2552080933e12b6b871bc9f898fce)
- [bt_map_mce_mas_update_inbox](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gae91fb531b7164b389994b9391fa8e51e)
- [bt_map_mce_mas_get_mas_inst_info](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gabbe39f067872a6c008269d483a97d234)
- [bt_map_mce_mas_set_owner_status](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga3b1dc36240679618c98df515a351a5e7)
- [bt_map_mce_mas_get_owner_status](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga2206f238364c04e180153c5cff10de94)
- [bt_map_mce_mas_get_convo_listing](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#gabdd72751375fa9a0aa1f99e75137cb9e)
- [bt_map_mce_mas_set_ntf_filter](../api_usb_gnss_topic_reference/P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md#ga28b33d6c38af9479e56e9c2c2c0f795a)
- [bt_map_mce_mns_register](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#gabae24c99ada5dae44ca657ae96008a69)
- [bt_map_mce_mns_rfcomm_register](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga574790bc59c82d89010e61f535849a35)
- [bt_map_mce_mns_rfcomm_disconnect](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#gac6fa0bcfbea7b9a2a258678f5a2b8503)
- [bt_map_mce_mns_l2cap_register](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga904970bac58822ec5336ce2bab226300)
- [bt_map_mce_mns_l2cap_disconnect](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#gad4207d61fbe40c34e753132fc742aba3)
- [bt_map_mce_mns_create_pdu](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga029cb5034f7cbf059653c763e4c767c2)
- [bt_map_mce_mns_connect](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#gaab9161c0524c74cb4b03938c26642f4a)
- [bt_map_mce_mns_disconnect](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga14411f8c0e8ce90824d366d28d4a2d2e)
- [bt_map_mce_mns_abort](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga7309e25833e6594dc0018afe8b0a403c)
- [bt_map_mce_mns_send_event](../api_packet_provision_topic_reference/P002_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 服务器.md#ga3e181d1bd37877dd8abf47a541c4b98e)
- [bt_map_mse_mas_register](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga14815828dbf7163ab8fb0b3a8c0165b4)
- [bt_map_mse_mas_rfcomm_register](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga670bebf0edd1e8d5f7a2de5403e042d0)
- [bt_map_mse_mas_rfcomm_disconnect](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga7db0773e3e0425f77e965fece30c3697)
- [bt_map_mse_mas_l2cap_register](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga031515fbb0ca110532f5a1e971a01739)
- [bt_map_mse_mas_l2cap_disconnect](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga6df473fe69d8b3d183ee8385613f786f)
- [bt_map_mse_mas_create_pdu](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gab1c7678b39dad5309efde0b5950a997f)
- [bt_map_mse_mas_connect](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gadd1da4acdd8043aa542c0fe36259898f)
- [bt_map_mse_mas_disconnect](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gabc3a8d9eb9dbc3fd028d39e4a262388b)
- [bt_map_mse_mas_abort](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga3eee467070483854e1a84a940ee031e2)
- [bt_map_mse_mas_set_folder](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gac972589b96cd3931044f994d4c94cf20)
- [bt_map_mse_mas_set_ntf_reg](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga55641e8681932d0e31021d3803625874)
- [bt_map_mse_mas_get_folder_listing](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga8263ea5145edcfd277f73980a3fcea57)
- [bt_map_mse_mas_get_msg_listing](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga2833ef99d384109acf304532d1820a36)
- [bt_map_mse_mas_get_msg](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga852ae34e4f8b44fea3308a42baa15ec2)
- [bt_map_mse_mas_set_msg_status](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga3cfbf0a8f1f1b6a730c401dac21e9f51)
- [bt_map_mse_mas_push_msg](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gabcd127dc45e03820079be0dc92066b89)
- [bt_map_mse_mas_update_inbox](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga2c0ed0fdc8fee3f98e671c5ec187c8ed)
- [bt_map_mse_mas_get_mas_inst_info](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gab50e3d126e2d35e9b6724cf3112d0892)
- [bt_map_mse_mas_set_owner_status](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga275eff320f980230d8d80873ad0ef3ce)
- [bt_map_mse_mas_get_owner_status](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga37c155889cd0e2bb902da2bd25415509)
- [bt_map_mse_mas_get_convo_listing](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#gadeb8072cdca241b3ad15c2116733d155)
- [bt_map_mse_mas_set_ntf_filter](../api_memory_timer_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md#ga3aacf3e78b40f06bbf17baada2c59e04)
- [bt_map_mse_mns_rfcomm_connect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#gadf2f434d2565703781a46851d4444a80)
- [bt_map_mse_mns_rfcomm_disconnect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#ga0513491439278cadc6897f9cb932cd67)
- [bt_map_mse_mns_l2cap_connect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#ga46fc48dafd5c173199274be1a616a109)
- [bt_map_mse_mns_l2cap_disconnect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#ga305dd055de4831ef68cff7b5346a4b5d)
- [bt_map_mse_mns_create_pdu](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#gaa0298eb521d012a910eba4a552d55fa7)
- [bt_map_mse_mns_connect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#ga7bedc538a126b8c4d4c6fb393fc06218)
- [bt_map_mse_mns_disconnect](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#ga08513e5aa2b54e4474ee647232c0af91)
- [bt_map_mse_mns_abort](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#gafc1be36425faa6242ed8eb4f21d76b5f)
- [bt_map_mse_mns_send_event](../api_packet_provision_topic_reference/P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md#gac8776edbbf4e2f891246cba86a1df589)

<a id="header-details"></a>

---

[上一章](P001_zephyr__bluetooth__audio__bap.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__sys__fdtable.h_文件参考.md)
