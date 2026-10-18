---
id: learning.zephyr-docs.api-imaging-input-lwm2m-reference.page-2
title: 基本成像配置文件（Basic Imaging Profile，BIP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_基本成像配置文件（Basic Imaging Profile，BIP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基本成像配置文件（Basic Imaging Profile，BIP）

<a id="details"></a>

基本成像配置文件（Basic Imaging Profile，BIP）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fbip_5Ftransport_5Fops"></a>

```c
struct bt_bip_transport_ops
```

相关声明：[bt_bip_transport_ops](../bluetooth_service_model_reference/P008_bt_bip_transport_ops_结构体.md)。

BIP 传输层操作（Transport Layer Operations）。

<a id="r_bt_5Fbip_5Frfcomm_5Fserver"></a>

```c
struct bt_bip_rfcomm_server
```

相关声明：[bt_bip_rfcomm_server](../bluetooth_service_model_reference/P005_bt_bip_rfcomm_server_结构体.md)。

BIP 的 RFCOMM 服务器结构体。

<a id="r_bt_5Fbip_5Fl2cap_5Fserver"></a>

```c
struct bt_bip_l2cap_server
```

相关声明：[bt_bip_l2cap_server](../bluetooth_service_model_reference/P004_bt_bip_l2cap_server_结构体.md)。

BIP 的 L2CAP 服务器结构体。

<a id="r_bt_5Fbip"></a>

```c
struct bt_bip
```

相关声明：[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)。

基本图像配置文件（BIP）实例结构体。

<a id="r_bt_5Fbip_5Fserver_5Fcb"></a>

```c
struct bt_bip_server_cb
```

相关声明：[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

BIP 服务器回调结构体。

<a id="r_bt_5Fbip_5Fclient_5Fcb"></a>

```c
struct bt_bip_client_cb
```

相关声明：[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)。

BIP 客户端回调结构体。

<a id="r_bt_5Fbip_5Fserver"></a>

```c
struct bt_bip_server
```

相关声明：[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)。

BIP 服务器实例结构体。

<a id="r_bt_5Fbip_5Fclient"></a>

```c
struct bt_bip_client
```

相关声明：[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)。

BIP 客户端实例结构体。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga09dfef702e656fcc8ee33a42ff567689"></a>

```c
#define BT_BIP_HDR_TYPE_GET_CAPS "x-bt/img-capabilities"
```

相关声明：[BT_BIP_HDR_TYPE_GET_CAPS](#ga09dfef702e656fcc8ee33a42ff567689)。

用于获取能力操作（Get Capabilities）的 OBEX 类型报头（Type Header）。

<a id="r_gae993464cf0ac6e7e58f42869effc84a2"></a>

```c
#define BT_BIP_HDR_TYPE_GET_IMAGE_LIST "x-bt/img-listing"
```

相关声明：[BT_BIP_HDR_TYPE_GET_IMAGE_LIST](#gae993464cf0ac6e7e58f42869effc84a2)。

用于获取图像列表操作（Get Image List）的 OBEX 类型报头（Type Header）。

<a id="r_ga7eba82c88fc511a25210b65f0d7c4a4f"></a>

```c
#define BT_BIP_HDR_TYPE_GET_IMAGE_PROPERTIES "x-bt/img-properties"
```

相关声明：[BT_BIP_HDR_TYPE_GET_IMAGE_PROPERTIES](#ga7eba82c88fc511a25210b65f0d7c4a4f)。

用于获取图像属性操作（Get Image Properties）的 OBEX 类型报头（Type Header）。

<a id="r_ga6bd29c7d876e3f617797fa91a0ea7ab6"></a>

```c
#define BT_BIP_HDR_TYPE_GET_IMAGE "x-bt/img-img"
```

相关声明：[BT_BIP_HDR_TYPE_GET_IMAGE](#ga6bd29c7d876e3f617797fa91a0ea7ab6)。

用于获取图像操作（Get Image）的 OBEX 类型报头（Type Header）。

<a id="r_ga34b8c83f54c32026bd7fba15b3333489"></a>

```c
#define BT_BIP_HDR_TYPE_GET_LINKED_THUMBNAIL "x-bt/img-thm"
```

相关声明：[BT_BIP_HDR_TYPE_GET_LINKED_THUMBNAIL](#ga34b8c83f54c32026bd7fba15b3333489)。

用于获取关联缩略图操作（Get Linked Thumbnail）的 OBEX 类型报头（Type Header）。

<a id="r_gadcfcdfac4571707f8b8b15fba18c592a"></a>

```c
#define BT_BIP_HDR_TYPE_GET_LINKED_ATTACHMENT "x-bt/img-attachment"
```

相关声明：[BT_BIP_HDR_TYPE_GET_LINKED_ATTACHMENT](#gadcfcdfac4571707f8b8b15fba18c592a)。

用于获取关联附件操作（Get Linked Attachment）的 OBEX 类型报头（Type Header）。

<a id="r_gab4136d9a07d10380590e791adf57069f"></a>

```c
#define BT_BIP_HDR_TYPE_GET_PARTIAL_IMAGE "x-bt/img-partial"
```

相关声明：[BT_BIP_HDR_TYPE_GET_PARTIAL_IMAGE](#gab4136d9a07d10380590e791adf57069f)。

用于获取部分图像操作（Get Partial Image）的 OBEX 类型报头（Type Header）。

<a id="r_gabb3046494704ab9e6959324e459cbc80"></a>

```c
#define BT_BIP_HDR_TYPE_GET_MONITORING_IMAGE "x-bt/img-monitoring"
```

相关声明：[BT_BIP_HDR_TYPE_GET_MONITORING_IMAGE](#gabb3046494704ab9e6959324e459cbc80)。

用于获取监控图像操作（Get Monitoring Image）的 OBEX 类型报头（Type Header）。

<a id="r_ga6c4c9d3b20c7ab5daf5b7cfbc9fcac2f"></a>

```c
#define BT_BIP_HDR_TYPE_GET_STATUS "x-bt/img-status"
```

相关声明：[BT_BIP_HDR_TYPE_GET_STATUS](#ga6c4c9d3b20c7ab5daf5b7cfbc9fcac2f)。

用于获取状态操作（Get Status）的 OBEX 类型报头（Type Header）。

<a id="r_ga667582c6e8641099a13671e406f5fd96"></a>

```c
#define BT_BIP_HDR_TYPE_PUT_IMAGE "x-bt/img-img"
```

相关声明：[BT_BIP_HDR_TYPE_PUT_IMAGE](#ga667582c6e8641099a13671e406f5fd96)。

用于放入图像操作（Put Image）的 OBEX 类型报头（Type Header）。

<a id="r_gaf12eff4b680872a4690a0d9c6f873b26"></a>

```c
#define BT_BIP_HDR_TYPE_PUT_LINKED_THUMBNAIL "x-bt/img-thm"
```

相关声明：[BT_BIP_HDR_TYPE_PUT_LINKED_THUMBNAIL](#gaf12eff4b680872a4690a0d9c6f873b26)。

用于放入关联缩略图操作（Put Linked Thumbnail）的 OBEX 类型报头（Type Header）。

<a id="r_gaf90f12fea45e37a1d59684a578a58bba"></a>

```c
#define BT_BIP_HDR_TYPE_PUT_LINKED_ATTACHMENT "x-bt/img-attachment"
```

相关声明：[BT_BIP_HDR_TYPE_PUT_LINKED_ATTACHMENT](#gaf90f12fea45e37a1d59684a578a58bba)。

用于放入关联附件操作（Put Linked Attachment）的 OBEX 类型报头（Type Header）。

<a id="r_ga4391371df2040895f16e0eed56e75e57"></a>

```c
#define BT_BIP_HDR_TYPE_REMOTE_DISPLAY "x-bt/img-display"
```

相关声明：[BT_BIP_HDR_TYPE_REMOTE_DISPLAY](#ga4391371df2040895f16e0eed56e75e57)。

用于远程显示操作（Remote Display）的 OBEX 类型报头（Type Header）。

<a id="r_gae16d011e1a911d2f380bcbe0c648762a"></a>

```c
#define BT_BIP_HDR_TYPE_DELETE_IMAGE "x-bt/img-img"
```

相关声明：[BT_BIP_HDR_TYPE_DELETE_IMAGE](#gae16d011e1a911d2f380bcbe0c648762a)。

用于删除图像操作（Delete Image）的 OBEX 类型报头（Type Header）。

<a id="r_gad57d3fcc35a89eeacb4d92e1362a7097"></a>

```c
#define BT_BIP_HDR_TYPE_START_PRINT "x-bt/img-print"
```

相关声明：[BT_BIP_HDR_TYPE_START_PRINT](#gad57d3fcc35a89eeacb4d92e1362a7097)。

用于开始打印操作（Start Print）的 OBEX 类型报头（Type Header）。

<a id="r_gaafe1edaef34603ceffdb08062e721ed8"></a>

```c
#define BT_BIP_HDR_TYPE_START_ARCHIVE "x-bt/img-archive"
```

相关声明：[BT_BIP_HDR_TYPE_START_ARCHIVE](#gaafe1edaef34603ceffdb08062e721ed8)。

用于开始归档操作（Start Archive）的 OBEX 类型报头（Type Header）。

<a id="r_gaabe060f5798f742942d382ed4f06c83d"></a>

```c
#define BT_BIP_HEADER_ID_IMG_DESC 0x71
```

相关声明：[BT_BIP_HEADER_ID_IMG_DESC](#gaabe060f5798f742942d382ed4f06c83d)。

图像描述符报头 ID（Img-Descriptor Header ID）。

<a id="r_gafb1b58780a45e82c7b1c90a738bddbb9"></a>

```c
#define BT_BIP_HEADER_ID_IMG_HANDLE 0x30
```

相关声明：[BT_BIP_HEADER_ID_IMG_HANDLE](#gafb1b58780a45e82c7b1c90a738bddbb9)。

图像句柄报头 ID（Img-Handle Header ID）。

<a id="r_ga3d5c7f3a6a0a2fe541022c22995d4274"></a>

```c
#define BT_BIP_PRIM_IMAGE_PUSH_CB(_connect, _disconnect, _get_caps, _put_image, _put_linked_thumbnail, _put_linked_attachment)
```

相关声明：[BT_BIP_PRIM_IMAGE_PUSH_CB](#ga3d5c7f3a6a0a2fe541022c22995d4274)。

主图像推送服务器回调初始化器（Primary Image Push Server Callback Initializer）。

<a id="r_gada2fa948ead9c05ec300dc3af8722e87"></a>

```c
#define BT_BIP_PRIM_IMAGE_PULL_CB(_connect, _disconnect, _get_caps, _get_image_list, _get_image_properties, _get_image, _get_linked_thumbnail, _get_linked_attachment, _delete_image)
```

相关声明：[BT_BIP_PRIM_IMAGE_PULL_CB](#gada2fa948ead9c05ec300dc3af8722e87)。

主图像拉取服务器回调初始化器（Primary Image Pull Server Callback Initializer）。

<a id="r_gaf51de11367b7eeaa0be094d5ad561636"></a>

```c
#define BT_BIP_PRIM_IMAGE_PRINT_CB(_connect, _disconnect, _get_caps, _get_status, _start_print)
```

相关声明：[BT_BIP_PRIM_IMAGE_PRINT_CB](#gaf51de11367b7eeaa0be094d5ad561636)。

主图像打印服务器回调初始化器（Primary Image Print Server Callback Initializer）。

<a id="r_gae1fd7d679c6e197b2af5557ead4b4a13"></a>

```c
#define BT_BIP_2ND_IMAGE_PRINT_CB(_connect, _disconnect, _get_partial_image)
```

相关声明：[BT_BIP_2ND_IMAGE_PRINT_CB](#gae1fd7d679c6e197b2af5557ead4b4a13)。

次级图像打印服务器回调初始化器（Secondary Image Print Server Callback Initializer）。

<a id="r_ga445d8c170b5c805d86604f4d474ad0e8"></a>

```c
#define BT_BIP_PRIM_AUTO_ARCHIVE_CB(_connect, _disconnect, _get_status, _start_archive)
```

相关声明：[BT_BIP_PRIM_AUTO_ARCHIVE_CB](#ga445d8c170b5c805d86604f4d474ad0e8)。

主自动归档服务器回调初始化器（Primary Auto Archive Server Callback Initializer）。

<a id="r_ga2a719b3a6266dd6ce5827be47467ff14"></a>

```c
#define BT_BIP_2ND_AUTO_ARCHIVE_CB(_connect, _disconnect, _get_caps, _get_image_list, _get_image_properties, _get_image, _get_linked_thumbnail, _get_linked_attachment, _delete_image)
```

相关声明：[BT_BIP_2ND_AUTO_ARCHIVE_CB](#ga2a719b3a6266dd6ce5827be47467ff14)。

次级自动归档服务器回调初始化器（Secondary Auto Archive Server Callback Initializer）。

<a id="r_ga144e0d9835516f2e9390d1c966ede6bd"></a>

```c
#define BT_BIP_PRIM_REMOTE_CAMERA_CB(_connect, _disconnect, _get_image_properties, _get_image, _get_linked_thumbnail, _get_monitoring_image)
```

相关声明：[BT_BIP_PRIM_REMOTE_CAMERA_CB](#ga144e0d9835516f2e9390d1c966ede6bd)。

主远程相机服务器回调初始化器（Primary Remote Camera Server Callback Initializer）。

<a id="r_gabf52b29d7e2f727d9f14e8b53bcc3f4f"></a>

```c
#define BT_BIP_PRIM_REMOTE_DISPLAY_CB(_connect, _disconnect, _get_caps, _get_image_list, _put_image, _put_linked_thumbnail, _remote_display)
```

相关声明：[BT_BIP_PRIM_REMOTE_DISPLAY_CB](#gabf52b29d7e2f727d9f14e8b53bcc3f4f)。

主远程显示服务器回调初始化器（Primary Remote Display Server Callback Initializer）。

<a id="r_gaca571268fd723b69d19ef7cd97db1da3"></a>

```c
#define BT_BIP_UUID_IMAGE_PUSH
```

相关声明：[BT_BIP_UUID_IMAGE_PUSH](#gaca571268fd723b69d19ef7cd97db1da3)。

基本成像配置文件（BIP）的图像推送服务（Image Push Service）的 UUID。

<a id="r_ga42116d3c159adecc6d63c32f0a1c4672"></a>

```c
#define BT_BIP_UUID_IMAGE_PULL
```

相关声明：[BT_BIP_UUID_IMAGE_PULL](#ga42116d3c159adecc6d63c32f0a1c4672)。

基本成像配置文件（BIP）的图像拉取服务（Image Pull Service）的 UUID。

<a id="r_gaa4b44603eb57cbc223d94a8723abf06a"></a>

```c
#define BT_BIP_UUID_IMAGE_PRINT
```

相关声明：[BT_BIP_UUID_IMAGE_PRINT](#gaa4b44603eb57cbc223d94a8723abf06a)。

基本成像配置文件（BIP）的高级图像打印服务（Advanced Image Printing Service）的 UUID。

<a id="r_ga098a435c80d373158ade3dc15dd538e6"></a>

```c
#define BT_BIP_UUID_AUTO_ARCHIVE
```

相关声明：[BT_BIP_UUID_AUTO_ARCHIVE](#ga098a435c80d373158ade3dc15dd538e6)。

基本成像配置文件（BIP）的自动归档服务（Auto Archive Service）的 UUID。

<a id="r_ga305af9409b4cfa25a16bed28cd305175"></a>

```c
#define BT_BIP_UUID_REMOTE_CAMERA
```

相关声明：[BT_BIP_UUID_REMOTE_CAMERA](#ga305af9409b4cfa25a16bed28cd305175)。

基本成像配置文件（BIP）的远程相机服务（Remote Camera Service）的 UUID。

<a id="r_gaa8b43801cd1bf8a4d2c51b0d25a408fc"></a>

```c
#define BT_BIP_UUID_REMOTE_DISPLAY
```

相关声明：[BT_BIP_UUID_REMOTE_DISPLAY](#gaa8b43801cd1bf8a4d2c51b0d25a408fc)。

基本成像配置文件（BIP）的远程显示服务（Remote Display Service）的 UUID。

<a id="r_ga8ef9620a71471340492feb1c8a820b5d"></a>

```c
#define BT_BIP_UUID_REFERENCED_OBJ
```

相关声明：[BT_BIP_UUID_REFERENCED_OBJ](#ga8ef9620a71471340492feb1c8a820b5d)。

基本成像配置文件（BIP）的引用对象服务（Referenced Objects Service）的 UUID。

<a id="r_gae305dd59c79605feebffc3c91e641e67"></a>

```c
#define BT_BIP_UUID_ARCHIVED_OBJ
```

相关声明：[BT_BIP_UUID_ARCHIVED_OBJ](#gae305dd59c79605feebffc3c91e641e67)。

基本成像配置文件（BIP）的已归档对象服务（Archived Objects Service）的 UUID。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.3\_枚举（Enumerations）

<a id="r_ga34de6d20263274292543a7a8afbd2c6b"></a>

```c
enum bt_bip_appl_param_tag_id { BT_BIP_APPL_PARAM_TAG_ID_RETURNED_HANDLES = 0x01 , BT_BIP_APPL_PARAM_TAG_ID_LIST_START_OFFSET = 0x02 , BT_BIP_APPL_PARAM_TAG_ID_LATEST_CAPTURED_IMAGES = 0x03 , BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_LEN = 0x04 , BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_START_OFFSET = 0x05 , BT_BIP_APPL_PARAM_TAG_ID_TOTAL_FILE_SIZE = 0x06 , BT_BIP_APPL_PARAM_TAG_ID_END_FLAG = 0x07 , BT_BIP_APPL_PARAM_TAG_ID_REMOTE_DISPLAY = 0x08 , BT_BIP_APPL_PARAM_TAG_ID_SERVICE_ID = 0x09 , BT_BIP_APPL_PARAM_TAG_ID_STORE_FLAG = 0x0a }
```

相关声明：[bt_bip_appl_param_tag_id](#ga34de6d20263274292543a7a8afbd2c6b)、[BT_BIP_APPL_PARAM_TAG_ID_RETURNED_HANDLES](#gga34de6d20263274292543a7a8afbd2c6bace4966644e9194273b635b916eac0871)、[BT_BIP_APPL_PARAM_TAG_ID_LIST_START_OFFSET](#gga34de6d20263274292543a7a8afbd2c6ba0f0d78c2da3d8f3d0caf015525b3e010)、[BT_BIP_APPL_PARAM_TAG_ID_LATEST_CAPTURED_IMAGES](#gga34de6d20263274292543a7a8afbd2c6ba9dbbb8ed95c7ccd86a74263fef1a1e92)、[BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_LEN](#gga34de6d20263274292543a7a8afbd2c6bad6511bb04da2cf325a39bfee93f51e0c)、[BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_START_OFFSET](#gga34de6d20263274292543a7a8afbd2c6ba0ff60914fb36e587b42a473c25bd6a2d)、[BT_BIP_APPL_PARAM_TAG_ID_TOTAL_FILE_SIZE](#gga34de6d20263274292543a7a8afbd2c6ba2565f26c0322935acef85725ac8982e5)、[BT_BIP_APPL_PARAM_TAG_ID_END_FLAG](#gga34de6d20263274292543a7a8afbd2c6baa7b18ee3ae56c0f0e84a103c1e59f05d)、[BT_BIP_APPL_PARAM_TAG_ID_REMOTE_DISPLAY](#gga34de6d20263274292543a7a8afbd2c6bab0e2dfb17de25f4ec3b27b29c2659afa)、[BT_BIP_APPL_PARAM_TAG_ID_SERVICE_ID](#gga34de6d20263274292543a7a8afbd2c6ba683d101ea1babf1f147d1869ab7424f4)、[BT_BIP_APPL_PARAM_TAG_ID_STORE_FLAG](#gga34de6d20263274292543a7a8afbd2c6baef58e631bfd6c511318c386308374274)。

基本成像配置文件（BIP）的应用参数标记 ID（Application Parameter Tag IDs）。

<a id="r_gaff38654d69104bebaaf5884283e197ef"></a>

```c
enum bt_bip_conn_type { BT_BIP_PRIM_CONN_TYPE_IMAGE_PUSH = 0 , BT_BIP_PRIM_CONN_TYPE_IMAGE_PULL = 1 , BT_BIP_PRIM_CONN_TYPE_ADVANCED_IMAGE_PRINTING = 2 , BT_BIP_PRIM_CONN_TYPE_AUTO_ARCHIVE = 3 , BT_BIP_PRIM_CONN_TYPE_REMOTE_CAMERA = 4 , BT_BIP_PRIM_CONN_TYPE_REMOTE_DISPLAY = 5 , BT_BIP_2ND_CONN_TYPE_REFERENCED_OBJECTS = 10 , BT_BIP_2ND_CONN_TYPE_ARCHIVED_OBJECTS = 11 }
```

相关声明：[bt_bip_conn_type](#gaff38654d69104bebaaf5884283e197ef)、[BT_BIP_PRIM_CONN_TYPE_IMAGE_PUSH](#ggaff38654d69104bebaaf5884283e197efa612cd818200f49e37235917fead216d2)、[BT_BIP_PRIM_CONN_TYPE_IMAGE_PULL](#ggaff38654d69104bebaaf5884283e197efa05372dbd0a01855f0863ce355a503c61)、[BT_BIP_PRIM_CONN_TYPE_ADVANCED_IMAGE_PRINTING](#ggaff38654d69104bebaaf5884283e197efa05de3a972070aa4d1e29851479860d9f)、[BT_BIP_PRIM_CONN_TYPE_AUTO_ARCHIVE](#ggaff38654d69104bebaaf5884283e197efaf762949693b7cf70739ed0a0eb6a9d58)、[BT_BIP_PRIM_CONN_TYPE_REMOTE_CAMERA](#ggaff38654d69104bebaaf5884283e197efa8b576c667b9c6458e44ec67674bdffbd)、[BT_BIP_PRIM_CONN_TYPE_REMOTE_DISPLAY](#ggaff38654d69104bebaaf5884283e197efa12873fc1888cd99703131ae71134f0c7)、[BT_BIP_2ND_CONN_TYPE_REFERENCED_OBJECTS](#ggaff38654d69104bebaaf5884283e197efa4d5ab575c877aa2a43c29cbb52a361c7)、[BT_BIP_2ND_CONN_TYPE_ARCHIVED_OBJECTS](#ggaff38654d69104bebaaf5884283e197efabe15f984d6907bdb40c10e893e1c3bf6)。

BIP 的 OBEX 连接类型（Connection Types）。

<a id="r_ga30d9309cbbd88b54508551285b21e575"></a>

```c
enum bt_bip_role { BT_BIP_ROLE_UNKNOWN = 0 , BT_BIP_ROLE_INITIATOR = 1 , BT_BIP_ROLE_RESPONDER = 2 }
```

相关声明：[bt_bip_role](#ga30d9309cbbd88b54508551285b21e575)、[BT_BIP_ROLE_UNKNOWN](#gga30d9309cbbd88b54508551285b21e575aaa7de8d668d248049c5d5c75ae35d74b)、[BT_BIP_ROLE_INITIATOR](#gga30d9309cbbd88b54508551285b21e575aa5cdb11f2b0ac9c20c380dd48c9edaa5)、[BT_BIP_ROLE_RESPONDER](#gga30d9309cbbd88b54508551285b21e575a87d1fe99824b216780435898c2dfa968)。

BIP 角色类型（Role Types）。

<a id="r_ga7b3c6cb1159e7b2ede57c66f20b23827"></a>

```c
enum bt_bip_transport_state { BT_BIP_TRANSPORT_STATE_DISCONNECTED = 0 , BT_BIP_TRANSPORT_STATE_CONNECTING = 1 , BT_BIP_TRANSPORT_STATE_CONNECTED = 2 , BT_BIP_TRANSPORT_STATE_DISCONNECTING = 3 }
```

相关声明：[bt_bip_transport_state](#ga7b3c6cb1159e7b2ede57c66f20b23827)、[BT_BIP_TRANSPORT_STATE_DISCONNECTED](#gga7b3c6cb1159e7b2ede57c66f20b23827ae78c865c0034d405391aaf9f72e4c9b2)、[BT_BIP_TRANSPORT_STATE_CONNECTING](#gga7b3c6cb1159e7b2ede57c66f20b23827ad4444da19b4e0f499867ea967dfc578f)、[BT_BIP_TRANSPORT_STATE_CONNECTED](#gga7b3c6cb1159e7b2ede57c66f20b23827a1af8a1481b10b53c58af8e36c7b91588)、[BT_BIP_TRANSPORT_STATE_DISCONNECTING](#gga7b3c6cb1159e7b2ede57c66f20b23827a7340b2e209c71d9f944b303c22cb264d)。

BIP 传输状态（Transport State）。

<a id="r_gad062c0f3d2feeb92a866f0fe91a6f231"></a>

```c
enum bt_bip_supported_capabilities { BT_BIP_SUPP_CAP_GENERIC_IMAGE = 0 , BT_BIP_SUPP_CAP_CAPTURING = 1 , BT_BIP_SUPP_CAP_PRINTING = 2 , BT_BIP_SUPP_CAP_DISPLAYING = 3 }
```

相关声明：[bt_bip_supported_capabilities](#gad062c0f3d2feeb92a866f0fe91a6f231)、[BT_BIP_SUPP_CAP_GENERIC_IMAGE](#ggad062c0f3d2feeb92a866f0fe91a6f231a786ef1ad1bde68f9b026c9d080cc41d4)、[BT_BIP_SUPP_CAP_CAPTURING](#ggad062c0f3d2feeb92a866f0fe91a6f231ac9c5d73b0d2d5eb25a962fa72ede6d5a)、[BT_BIP_SUPP_CAP_PRINTING](#ggad062c0f3d2feeb92a866f0fe91a6f231a4a738d195dcf0908a64bdd246672d4bb)、[BT_BIP_SUPP_CAP_DISPLAYING](#ggad062c0f3d2feeb92a866f0fe91a6f231a324c0590cefb5d7a39f90d90e3466334)。

BIP 支持的能力（Supported Capabilities）。

<a id="r_gacfc8aaea3d27e3a42a14c49b880a5b90"></a>

```c
enum bt_bip_supported_features { BT_BIP_SUPP_FEAT_IMAGE_PUSH = 0 , BT_BIP_SUPP_FEAT_IMAGE_PUSH_STORE = 1 , BT_BIP_SUPP_FEAT_IMAGE_PUSH_PRINT = 2 , BT_BIP_SUPP_FEAT_IMAGE_PUSH_DISPLAY = 3 , BT_BIP_SUPP_FEAT_IMAGE_PULL = 4 , BT_BIP_SUPP_FEAT_ADVANCED_IMAGE_PRINT = 5 , BT_BIP_SUPP_FEAT_AUTO_ARCHIVE = 6 , BT_BIP_SUPP_FEAT_REMOTE_CAMERA = 7 , BT_BIP_SUPP_FEAT_REMOTE_DISPLAY = 8 }
```

相关声明：[bt_bip_supported_features](#gacfc8aaea3d27e3a42a14c49b880a5b90)、[BT_BIP_SUPP_FEAT_IMAGE_PUSH](#ggacfc8aaea3d27e3a42a14c49b880a5b90ac14657fd4af96f4c837916b832c25a0f)、[BT_BIP_SUPP_FEAT_IMAGE_PUSH_STORE](#ggacfc8aaea3d27e3a42a14c49b880a5b90a8904b7b8288e1b47d2242f5d686e32d9)、[BT_BIP_SUPP_FEAT_IMAGE_PUSH_PRINT](#ggacfc8aaea3d27e3a42a14c49b880a5b90add6c2e70541aae8124bad4b102d64b88)、[BT_BIP_SUPP_FEAT_IMAGE_PUSH_DISPLAY](#ggacfc8aaea3d27e3a42a14c49b880a5b90a49668a596059e535bd59ac095dffa050)、[BT_BIP_SUPP_FEAT_IMAGE_PULL](#ggacfc8aaea3d27e3a42a14c49b880a5b90aba576edd916dbf49118e78572f70320b)、[BT_BIP_SUPP_FEAT_ADVANCED_IMAGE_PRINT](#ggacfc8aaea3d27e3a42a14c49b880a5b90ac64d953311bc9b76bfe75dd3133f5563)、[BT_BIP_SUPP_FEAT_AUTO_ARCHIVE](#ggacfc8aaea3d27e3a42a14c49b880a5b90af72e05ca427f8c5091e50cddac522045)、[BT_BIP_SUPP_FEAT_REMOTE_CAMERA](#ggacfc8aaea3d27e3a42a14c49b880a5b90a97141e2764fad3714c03b6be69ff2a9a)、[BT_BIP_SUPP_FEAT_REMOTE_DISPLAY](#ggacfc8aaea3d27e3a42a14c49b880a5b90a132dd77e79fbfda8a78d5034d4c618c5)。

BIP 支持的特性（Supported Features）。

<a id="r_ga6768e59b79bb67b5d385fdaa3dfb8888"></a>

```c
enum bt_bip_supported_functions { BT_BIP_SUPP_FUNC_GET_CAPS = 0 , BT_BIP_SUPP_FUNC_PUT_IMAGE = 1 , BT_BIP_SUPP_FUNC_PUT_LINKED_ATTACHMENT = 2 , BT_BIP_SUPP_FUNC_PUT_LINKED_THUMBNAIL = 3 , BT_BIP_SUPP_FUNC_REMOTE_DISPLAY = 4 , BT_BIP_SUPP_FUNC_GET_IMAGE_LIST = 5 , BT_BIP_SUPP_FUNC_GET_IMAGE_PROPERTIES = 6 , BT_BIP_SUPP_FUNC_GET_IMAGE = 7 , BT_BIP_SUPP_FUNC_GET_LINKED_THUMBNAIL = 8 , BT_BIP_SUPP_FUNC_GET_LINKED_ATTACHMENT = 9 , BT_BIP_SUPP_FUNC_DELETE_IMAGE = 10 , BT_BIP_SUPP_FUNC_START_PRINT = 11 , BT_BIP_SUPP_FUNC_GET_PARTIAL_IMAGE = 12 , BT_BIP_SUPP_FUNC_START_ARCHIVE = 13 , BT_BIP_SUPP_FUNC_GET_MONITORING_IMAGE = 14 , BT_BIP_SUPP_FUNC_GET_STATUS = 16 }
```

相关声明：[bt_bip_supported_functions](#ga6768e59b79bb67b5d385fdaa3dfb8888)、[BT_BIP_SUPP_FUNC_GET_CAPS](#gga6768e59b79bb67b5d385fdaa3dfb8888a2e1f3364145560587963402881bb2705)、[BT_BIP_SUPP_FUNC_PUT_IMAGE](#gga6768e59b79bb67b5d385fdaa3dfb8888afb1777cefdbd00e3432ddf5180804f48)、[BT_BIP_SUPP_FUNC_PUT_LINKED_ATTACHMENT](#gga6768e59b79bb67b5d385fdaa3dfb8888a8a417f3073f017af866877f88ee10228)、[BT_BIP_SUPP_FUNC_PUT_LINKED_THUMBNAIL](#gga6768e59b79bb67b5d385fdaa3dfb8888a0ee047481a35e26fa0d03bf7594d7752)、[BT_BIP_SUPP_FUNC_REMOTE_DISPLAY](#gga6768e59b79bb67b5d385fdaa3dfb8888adb0e03118b1cd62fe7e97b53e9f52d41)、[BT_BIP_SUPP_FUNC_GET_IMAGE_LIST](#gga6768e59b79bb67b5d385fdaa3dfb8888a7843f4dece6ff449b97ba0a2c7298b90)、[BT_BIP_SUPP_FUNC_GET_IMAGE_PROPERTIES](#gga6768e59b79bb67b5d385fdaa3dfb8888af29095b3b5964062e98b9e357de87f89)、[BT_BIP_SUPP_FUNC_GET_IMAGE](#gga6768e59b79bb67b5d385fdaa3dfb8888a50271c1bac792020f0fb869bb523e506)、[BT_BIP_SUPP_FUNC_GET_LINKED_THUMBNAIL](#gga6768e59b79bb67b5d385fdaa3dfb8888a03c928dd502a98b72cb7d8eebad4b384)、[BT_BIP_SUPP_FUNC_GET_LINKED_ATTACHMENT](#gga6768e59b79bb67b5d385fdaa3dfb8888ac3ec252a63d494ce3e4dd696d05d94bc)、[BT_BIP_SUPP_FUNC_DELETE_IMAGE](#gga6768e59b79bb67b5d385fdaa3dfb8888a045dfb07426eacb16fd69247eecf70b1)、[BT_BIP_SUPP_FUNC_START_PRINT](#gga6768e59b79bb67b5d385fdaa3dfb8888ae1312bb3417f901204ac592e4b9376df)、[BT_BIP_SUPP_FUNC_GET_PARTIAL_IMAGE](#gga6768e59b79bb67b5d385fdaa3dfb8888ae1e97efb19d10ac2b508a9e65b5c43ce)、[BT_BIP_SUPP_FUNC_START_ARCHIVE](#gga6768e59b79bb67b5d385fdaa3dfb8888a3cae66cb380311938f83bb099a2d02da)、[BT_BIP_SUPP_FUNC_GET_MONITORING_IMAGE](#gga6768e59b79bb67b5d385fdaa3dfb8888a0bde5efd58b339e53db3779a159239c1)、[BT_BIP_SUPP_FUNC_GET_STATUS](#gga6768e59b79bb67b5d385fdaa3dfb8888abf825fb7d634906f0204780ef81ca5b3)。

BIP 支持的功能（Supported Functions）。

<a id="r_gae4d1ed3b7e27768c1dbb6ce448cb5cf9"></a>

```c
enum bt_bip_state { BT_BIP_STATE_DISCONNECTED = 0 , BT_BIP_STATE_CONNECTING = 1 , BT_BIP_STATE_CONNECTED = 2 , BT_BIP_STATE_DISCONNECTING = 3 }
```

相关声明：[bt_bip_state](#gae4d1ed3b7e27768c1dbb6ce448cb5cf9)、[BT_BIP_STATE_DISCONNECTED](#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a984245e44981ad3d85518ab1c3f576e8)、[BT_BIP_STATE_CONNECTING](#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9acdc7fe9ee4c0d0ba447bc43817364478)、[BT_BIP_STATE_CONNECTED](#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9ae65c7b972effa225116ec8abfcf07bc3)、[BT_BIP_STATE_DISCONNECTING](#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a96f12788ce6f56012ac4b1c25f63f67e)。

BIP 连接状态（Connection State）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_ga644ca479c156b10d920d87d862401fc7"></a>

```c
int bt_bip_rfcomm_register (struct bt_bip_rfcomm_server *server)
```

相关声明：[bt_bip_rfcomm_register](#ga644ca479c156b10d920d87d862401fc7)、[bt_bip_rfcomm_server](../bluetooth_service_model_reference/P005_bt_bip_rfcomm_server_结构体.md)。

注册 BIP RFCOMM 服务器（Server）。

<a id="r_ga5ed2a46482e4fe60ef23c540001b58a3"></a>

```c
int bt_bip_rfcomm_connect (struct bt_conn *conn, struct bt_bip *bip, uint8_t channel)
```

相关声明：[bt_bip_rfcomm_connect](#ga5ed2a46482e4fe60ef23c540001b58a3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 RFCOMM 创建传输连接（Transport Connection）。

<a id="r_ga66a86a399f73dba932dc05d63b3749bd"></a>

```c
int bt_bip_rfcomm_disconnect (struct bt_bip *bip)
```

相关声明：[bt_bip_rfcomm_disconnect](#ga66a86a399f73dba932dc05d63b3749bd)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)。

断开 BIP RFCOMM 连接（Connection）。

<a id="r_gaffb77f6c80ba05046df03d62baad211b"></a>

```c
int bt_bip_l2cap_register (struct bt_bip_l2cap_server *server)
```

相关声明：[bt_bip_l2cap_register](#gaffb77f6c80ba05046df03d62baad211b)、[bt_bip_l2cap_server](../bluetooth_service_model_reference/P004_bt_bip_l2cap_server_结构体.md)。

注册 BIP L2CAP 服务器（Server）。

<a id="r_gaf54b07acf22c5231b2de0fdeca7807c2"></a>

```c
int bt_bip_l2cap_connect (struct bt_conn *conn, struct bt_bip *bip, uint16_t psm)
```

相关声明：[bt_bip_l2cap_connect](#gaf54b07acf22c5231b2de0fdeca7807c2)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 L2CAP 创建传输连接（Transport Connection）。

<a id="r_ga1fda174189b57c54f365784d1909152e"></a>

```c
int bt_bip_l2cap_disconnect (struct bt_bip *bip)
```

相关声明：[bt_bip_l2cap_disconnect](#ga1fda174189b57c54f365784d1909152e)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)。

断开 BIP L2CAP 连接（Connection）。

<a id="r_ga0180461f24c6f741e056d64f9758b89e"></a>

```c
int bt_bip_set_supported_capabilities (struct bt_bip *bip, uint8_t capabilities)
```

相关声明：[bt_bip_set_supported_capabilities](#ga0180461f24c6f741e056d64f9758b89e)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 BIP 响应方（Responder）支持的能力（Capabilities）。

<a id="r_gab5a80d7a992d0afa0270eb09d6f3275c"></a>

```c
int bt_bip_set_supported_features (struct bt_bip *bip, uint16_t features)
```

相关声明：[bt_bip_set_supported_features](#gab5a80d7a992d0afa0270eb09d6f3275c)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 BIP 响应方（Responder）支持的特性（Features）。

<a id="r_gafe7df6ee236da3a11104f1aa6e948bfe"></a>

```c
int bt_bip_set_supported_functions (struct bt_bip *bip, uint32_t functions)
```

相关声明：[bt_bip_set_supported_functions](#gafe7df6ee236da3a11104f1aa6e948bfe)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置 BIP 响应方（Responder）支持的功能（Functions）。

<a id="r_ga45f1ca2d2874500d6f8df3a62b01260e"></a>

```c
int bt_bip_primary_server_register (struct bt_bip *bip, struct bt_bip_server *server, enum bt_bip_conn_type type, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_server_register](#ga45f1ca2d2874500d6f8df3a62b01260e)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_bip_conn_type](#gaff38654d69104bebaaf5884283e197ef)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主 BIP OBEX 服务器（Primary Server）。

<a id="r_gab0a3b58b041ac4af2682fb96b8f00a7e"></a>

```c
int bt_bip_secondary_server_register (struct bt_bip *bip, struct bt_bip_server *server, enum bt_bip_conn_type type, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb, struct bt_bip_client *primary_client)
```

相关声明：[bt_bip_secondary_server_register](#gab0a3b58b041ac4af2682fb96b8f00a7e)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_bip_conn_type](#gaff38654d69104bebaaf5884283e197ef)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)。

注册次级 BIP OBEX 服务器（Secondary Server）。

<a id="r_gaefd318b5dc2e813eea2cd7608be1170c"></a>

```c
static int bt_bip_primary_image_push_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_image_push_server_register](#gaefd318b5dc2e813eea2cd7608be1170c)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主图像推送 OBEX 服务器（Primary Image Push OBEX server）。

<a id="r_ga35c44217cbfcd8661c3f2e5725be9323"></a>

```c
static int bt_bip_primary_image_pull_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_image_pull_server_register](#ga35c44217cbfcd8661c3f2e5725be9323)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主图像拉取 OBEX 服务器（Primary Image Pull OBEX server）。

<a id="r_gae8b37b224ea419ca1f1761d98a34cb2d"></a>

```c
static int bt_bip_primary_advanced_image_printing_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_advanced_image_printing_server_register](#gae8b37b224ea419ca1f1761d98a34cb2d)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主高级图像打印 OBEX 服务器（Primary Advanced Image Printing OBEX server）。

<a id="r_ga3848d86378912fbd9c896b14aed74161"></a>

```c
static int bt_bip_primary_auto_archive_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_auto_archive_server_register](#ga3848d86378912fbd9c896b14aed74161)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主自动归档 OBEX 服务器（Primary Auto Archive OBEX server）。

<a id="r_ga4b236a8a28c359e392633d472a508405"></a>

```c
static int bt_bip_primary_remote_camera_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_remote_camera_server_register](#ga4b236a8a28c359e392633d472a508405)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主远程相机 OBEX 服务器（Primary Remote Camera OBEX server）。

<a id="r_ga5167b2dab89a983fae9fca356e6fbcf9"></a>

```c
static int bt_bip_primary_remote_display_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_remote_display_server_register](#ga5167b2dab89a983fae9fca356e6fbcf9)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主远程显示 OBEX 服务器（Primary Remote Display OBEX server）。

<a id="r_ga54c37cced33fa72a2c6cea10e2996e6d"></a>

```c
static int bt_bip_secondary_advanced_image_printing_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb, struct bt_bip_client *primary_client)
```

相关声明：[bt_bip_secondary_advanced_image_printing_server_register](#ga54c37cced33fa72a2c6cea10e2996e6d)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)。

注册次级高级图像打印 OBEX 服务器（Secondary Advanced Image Printing OBEX server）。

<a id="r_gab24c4f7144f8c43dcf1b82a4c33e4ffd"></a>

```c
static int bt_bip_secondary_auto_archive_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb, struct bt_bip_client *primary_client)
```

相关声明：[bt_bip_secondary_auto_archive_server_register](#gab24c4f7144f8c43dcf1b82a4c33e4ffd)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)。

注册次级自动归档 OBEX 服务器（Secondary Auto Archive OBEX server）。

<a id="r_ga4e06b2fb9a99f89d7e65e8a52690442d"></a>

```c
int bt_bip_server_unregister (struct bt_bip_server *server)
```

相关声明：[bt_bip_server_unregister](#ga4e06b2fb9a99f89d7e65e8a52690442d)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)。

注销 BIP OBEX 服务器（Server）。

<a id="r_gad32c1b1118b606ab3ae0d9db889cbab9"></a>

```c
int bt_bip_primary_client_connect (struct bt_bip *bip, struct bt_bip_client *client, enum bt_bip_conn_type type, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_client_connect](#gad32c1b1118b606ab3ae0d9db889cbab9)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_conn_type](#gaff38654d69104bebaaf5884283e197ef)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主 BIP OBEX 客户端（Primary Client）。

<a id="r_gae557b198b9d5606ee05cd29ed16f9482"></a>

```c
int bt_bip_secondary_client_connect (struct bt_bip *bip, struct bt_bip_client *client, enum bt_bip_conn_type type, struct bt_bip_client_cb *cb, struct net_buf *buf, struct bt_bip_server *primary_server)
```

相关声明：[bt_bip_secondary_client_connect](#gae557b198b9d5606ee05cd29ed16f9482)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_conn_type](#gaff38654d69104bebaaf5884283e197ef)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)。

连接次级 BIP OBEX 客户端（Secondary Client）。

<a id="r_ga39ec2019f86d42b02992b0a9d3ba094c"></a>

```c
static int bt_bip_primary_image_push_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_image_push_client_connect](#ga39ec2019f86d42b02992b0a9d3ba094c)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主图像推送 OBEX 客户端（Primary Image Push OBEX client）。

<a id="r_ga2d4919c1eb568f33a89d8b176f103601"></a>

```c
static int bt_bip_primary_image_pull_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_image_pull_client_connect](#ga2d4919c1eb568f33a89d8b176f103601)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主图像拉取 OBEX 客户端（Primary Image Pull OBEX client）。

<a id="r_ga9352b8309334a3fe89d77f5714443376"></a>

```c
static int bt_bip_primary_advanced_image_printing_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_advanced_image_printing_client_connect](#ga9352b8309334a3fe89d77f5714443376)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主高级图像打印 OBEX 客户端（Primary Advanced Image Printing OBEX client）。

<a id="r_ga98dca7b222c8a09b1c44861c9060193b"></a>

```c
static int bt_bip_primary_auto_archive_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_auto_archive_client_connect](#ga98dca7b222c8a09b1c44861c9060193b)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主自动归档 OBEX 客户端（Primary Auto Archive OBEX client）。

<a id="r_ga30e3a6ad8c00c230ac3591a934cfb81f"></a>

```c
static int bt_bip_primary_remote_camera_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_remote_camera_client_connect](#ga30e3a6ad8c00c230ac3591a934cfb81f)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主远程相机 OBEX 客户端（Primary Remote Camera OBEX client）。

<a id="r_gac4ba5cef40cd451bd4b505dbea0fa135"></a>

```c
static int bt_bip_primary_remote_display_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_remote_display_client_connect](#gac4ba5cef40cd451bd4b505dbea0fa135)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主远程显示 OBEX 客户端（Primary Remote Display OBEX client）。

<a id="r_ga72ef6cd266b7e57e1c80b6d8eba799e2"></a>

```c
static int bt_bip_secondary_advanced_image_printing_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf, struct bt_bip_server *primary_server)
```

相关声明：[bt_bip_secondary_advanced_image_printing_client_connect](#ga72ef6cd266b7e57e1c80b6d8eba799e2)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)。

连接次级高级图像打印 OBEX 客户端（Secondary Advanced Image Printing OBEX client）。

<a id="r_ga1975916aa3da40576499f6d05aac1285"></a>

```c
static int bt_bip_secondary_auto_archive_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf, struct bt_bip_server *primary_server)
```

相关声明：[bt_bip_secondary_auto_archive_client_connect](#ga1975916aa3da40576499f6d05aac1285)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)。

连接次级自动归档 OBEX 客户端（Secondary Auto Archive OBEX client）。

<a id="r_ga0987a342b43bdd1926f3730f471ca05f"></a>

```c
int bt_bip_connect_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_connect_rsp](#ga0987a342b43bdd1926f3730f471ca05f)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送OBEX连接响应（OBEX Connect response）。

<a id="r_gaafcd6a3503795299b6fb777ba0aa0cff"></a>

```c
int bt_bip_disconnect (struct bt_bip_client *client, struct net_buf *buf)
```

相关声明：[bt_bip_disconnect](#gaafcd6a3503795299b6fb777ba0aa0cff)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送OBEX断开连接请求（OBEX Disconnect request）。

<a id="r_gaddfcee2eaea19b4819d83cf6ecb396da"></a>

```c
int bt_bip_disconnect_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_disconnect_rsp](#gaddfcee2eaea19b4819d83cf6ecb396da)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送OBEX断开连接响应（OBEX Disconnect response）。

<a id="r_gaa0f071c8c83a54b2d48f478594579719"></a>

```c
int bt_bip_abort (struct bt_bip_client *client, struct net_buf *buf)
```

相关声明：[bt_bip_abort](#gaa0f071c8c83a54b2d48f478594579719)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送OBEX中止请求（OBEX Abort request）。

<a id="r_ga1c341ad182ff418286b64b4eff491445"></a>

```c
int bt_bip_abort_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_abort_rsp](#ga1c341ad182ff418286b64b4eff491445)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送OBEX中止响应（OBEX Abort response）。

<a id="r_gafcd2d4e6a8ad906c9692313421175431"></a>

```c
int bt_bip_get_capabilities (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_capabilities](#gafcd2d4e6a8ad906c9692313421175431)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取能力请求（Get Capabilities request）。

<a id="r_gaea5d5f5b6c29a44ae89939ee3e2d6efb"></a>

```c
int bt_bip_get_capabilities_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_capabilities_rsp](#gaea5d5f5b6c29a44ae89939ee3e2d6efb)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取能力响应（Get Capabilities response）。

<a id="r_ga9542e030ea863b4379d36fa21de262dc"></a>

```c
int bt_bip_get_image_list (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_image_list](#ga9542e030ea863b4379d36fa21de262dc)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像列表请求（Get Image List request）。

<a id="r_ga6e33bba952a9693d1fed7ee9bdf03df8"></a>

```c
int bt_bip_get_image_list_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_image_list_rsp](#ga6e33bba952a9693d1fed7ee9bdf03df8)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像列表响应（Get Image List response）。

<a id="r_ga17ae73bd6088b44206378afe3b0b9eb0"></a>

```c
int bt_bip_get_image_properties (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_image_properties](#ga17ae73bd6088b44206378afe3b0b9eb0)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像属性请求（Get Image Properties request）。

<a id="r_ga9a91c35e91a0c30eab55da5b842427d9"></a>

```c
int bt_bip_get_image_properties_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_image_properties_rsp](#ga9a91c35e91a0c30eab55da5b842427d9)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像属性响应（Get Image Properties response）。

<a id="r_ga79831fc5fff332a891e6b9ff71f81d20"></a>

```c
int bt_bip_get_image (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_image](#ga79831fc5fff332a891e6b9ff71f81d20)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像请求（Get Image request）。

<a id="r_ga53fb15ff7d0728b09f1c4e8d2ceb6dee"></a>

```c
int bt_bip_get_image_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_image_rsp](#ga53fb15ff7d0728b09f1c4e8d2ceb6dee)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像响应（Get Image response）。

<a id="r_gad9c05d28e1e2124675b5906990c3408c"></a>

```c
int bt_bip_get_linked_thumbnail (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_linked_thumbnail](#gad9c05d28e1e2124675b5906990c3408c)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取关联缩略图请求（Get Linked Thumbnail request）。

<a id="r_ga5c3cd3e39fc21a584d6955a160ca126a"></a>

```c
int bt_bip_get_linked_thumbnail_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_linked_thumbnail_rsp](#ga5c3cd3e39fc21a584d6955a160ca126a)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取关联缩略图响应（Get Linked Thumbnail response）。

<a id="r_gad95944f07cd9f7b6bb9c81f21fffd447"></a>

```c
int bt_bip_get_linked_attachment (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_linked_attachment](#gad95944f07cd9f7b6bb9c81f21fffd447)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取关联附件请求（Get Linked Attachment request）。

<a id="r_ga70bf0d46bd16d0207e13eeb9a7844f1c"></a>

```c
int bt_bip_get_linked_attachment_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_linked_attachment_rsp](#ga70bf0d46bd16d0207e13eeb9a7844f1c)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取关联附件响应（Get Linked Attachment response）。

<a id="r_ga2b6a2a51fb00e7060e196051f8aea4c4"></a>

```c
int bt_bip_get_partial_image (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_partial_image](#ga2b6a2a51fb00e7060e196051f8aea4c4)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取部分图像请求（Get Partial Image request）。

<a id="r_gadf624e05a6d008bdcfd8a61ae6341f42"></a>

```c
int bt_bip_get_partial_image_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_partial_image_rsp](#gadf624e05a6d008bdcfd8a61ae6341f42)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取部分图像响应（Get Partial Image response）。

<a id="r_ga9f1593748ffcf29015533d52266a8e19"></a>

```c
int bt_bip_get_monitoring_image (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_monitoring_image](#ga9f1593748ffcf29015533d52266a8e19)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取监控图像请求（Get Monitoring Image request）。

<a id="r_ga301ff6e5a1e8775295659442b8c20e15"></a>

```c
int bt_bip_get_monitoring_image_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_monitoring_image_rsp](#ga301ff6e5a1e8775295659442b8c20e15)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取监控图像响应（Get Monitoring Image response）。

<a id="r_ga578c2b59fbc8afee530168452eb221fb"></a>

```c
int bt_bip_get_status (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_status](#ga578c2b59fbc8afee530168452eb221fb)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取状态请求（Get Status request）。

<a id="r_ga7abdde3a7e5dcda9c6187b5e45b75cc2"></a>

```c
int bt_bip_get_status_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_status_rsp](#ga7abdde3a7e5dcda9c6187b5e45b75cc2)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取状态响应（Get Status response）。

<a id="r_gaf551904672eda53e9dfcbb5a6bf4c2c3"></a>

```c
int bt_bip_put_image (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_put_image](#gaf551904672eda53e9dfcbb5a6bf4c2c3)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入图像请求（Put Image request）。

<a id="r_ga002f7713a8269c0b00a415bbb8c53fce"></a>

```c
int bt_bip_put_image_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_put_image_rsp](#ga002f7713a8269c0b00a415bbb8c53fce)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入图像响应（Put Image response）。

<a id="r_ga8b730495f4dd4e6f8db85c5b060a3cae"></a>

```c
int bt_bip_put_linked_thumbnail (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_put_linked_thumbnail](#ga8b730495f4dd4e6f8db85c5b060a3cae)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入关联缩略图请求（Put Linked Thumbnail request）。

<a id="r_gac96e873a840b072f5213b7483d633aaa"></a>

```c
int bt_bip_put_linked_thumbnail_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_put_linked_thumbnail_rsp](#gac96e873a840b072f5213b7483d633aaa)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入关联缩略图响应（Put Linked Thumbnail response）。

<a id="r_ga86085e98964dcfd19725b5d96f38a99b"></a>

```c
int bt_bip_put_linked_attachment (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_put_linked_attachment](#ga86085e98964dcfd19725b5d96f38a99b)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入关联附件请求（Put Linked Attachment request）。

<a id="r_gad6a7df2b0c49c0df616ef170c7b9e431"></a>

```c
int bt_bip_put_linked_attachment_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_put_linked_attachment_rsp](#gad6a7df2b0c49c0df616ef170c7b9e431)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入关联附件响应（Put Linked Attachment response）。

<a id="r_ga021a5d82b292d04cd0e2d53b1b32344b"></a>

```c
int bt_bip_remote_display (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_remote_display](#ga021a5d82b292d04cd0e2d53b1b32344b)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送远程显示请求（Remote Display request）。

<a id="r_ga0c54da02bc8dda26794f398e06e66cb3"></a>

```c
int bt_bip_remote_display_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_remote_display_rsp](#ga0c54da02bc8dda26794f398e06e66cb3)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送远程显示响应（Remote Display response）。

<a id="r_ga5302af5beb7cd5c98a9cbdc288f09d3c"></a>

```c
int bt_bip_delete_image (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_delete_image](#ga5302af5beb7cd5c98a9cbdc288f09d3c)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送删除图像请求（Delete Image request）。

<a id="r_gad53a7666b90a97034276fe341c2bd7a2"></a>

```c
int bt_bip_delete_image_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_delete_image_rsp](#gad53a7666b90a97034276fe341c2bd7a2)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送删除图像响应（Delete Image response）。

<a id="r_ga8a948dcee431ced321e7b5d51c8d5f9c"></a>

```c
int bt_bip_start_print (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_start_print](#ga8a948dcee431ced321e7b5d51c8d5f9c)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送开始打印请求（Start Print request）。

<a id="r_gae9ea9f936aa75b287a2152a747fd687a"></a>

```c
int bt_bip_start_print_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_start_print_rsp](#gae9ea9f936aa75b287a2152a747fd687a)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送开始打印响应（Start Print response）。

<a id="r_ga9674dc3dc2137a663a971f8521a41845"></a>

```c
int bt_bip_start_archive (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_start_archive](#ga9674dc3dc2137a663a971f8521a41845)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送开始归档请求（Start Archive request）。

<a id="r_gad16038fa018919a10d9be7fa6deeb659"></a>

```c
int bt_bip_start_archive_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_start_archive_rsp](#gad16038fa018919a10d9be7fa6deeb659)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送开始归档响应（Start Archive response）。

<a id="r_gaf48266502eacfc19938e1dfb29a3619b"></a>

```c
int bt_bip_add_header_image_desc (struct net_buf *buf, uint16_t len, const uint8_t *desc)
```

相关声明：[bt_bip_add_header_image_desc](#gaf48266502eacfc19938e1dfb29a3619b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向缓冲区添加图像描述符报头（Image Descriptor Header）。

<a id="r_ga4ca80902f04ea770c59c5e498fef615a"></a>

```c
int bt_bip_add_header_image_handle (struct net_buf *buf, uint16_t len, const uint8_t *handle)
```

相关声明：[bt_bip_add_header_image_handle](#ga4ca80902f04ea770c59c5e498fef615a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向缓冲区添加图像句柄报头（Image Handle Header）。

## 2.5\_详细说明（Detailed Documentation）

<a id="ga2a719b3a6266dd6ce5827be47467ff14"></a>

### `BT_BIP_2ND_AUTO_ARCHIVE_CB`

```c
#define BT_BIP_2ND_AUTO_ARCHIVE_CB ( _connect, _disconnect, _get_caps, _get_image_list, _get_image_properties, _get_image, _get_linked_thumbnail, _get_linked_attachment, _delete_image )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
{                                                                                          \
        .connect = _connect, .disconnect = _disconnect, .get_caps = _get_caps,             \
        .get_image_list = _get_image_list, .get_image_properties = _get_image_properties,  \
        .get_image = _get_image, .get_linked_thumbnail = _get_linked_thumbnail,            \
        .get_linked_attachment = _get_linked_attachment, .delete_image = _delete_image,    \
}
```

次级自动归档服务器回调初始化器（Secondary Auto Archive Server Callback Initializer）。

用于初始化次级自动归档服务器（Secondary Auto Archive Server）回调的辅助宏。

<a id="gae1fd7d679c6e197b2af5557ead4b4a13"></a>

### `BT_BIP_2ND_IMAGE_PRINT_CB`

```c
#define BT_BIP_2ND_IMAGE_PRINT_CB ( _connect, _disconnect, _get_partial_image )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
{                                                                                          \
        .connect = _connect, .disconnect = _disconnect,                                    \
        .get_partial_image = _get_partial_image,                                           \
}
```

次级图像打印服务器回调初始化器（Secondary Image Print Server Callback Initializer）。

用于初始化次级图像打印服务器（Secondary Image Print Server）回调的辅助宏。

<a id="gae16d011e1a911d2f380bcbe0c648762a"></a>

### `BT_BIP_HDR_TYPE_DELETE_IMAGE`

```c
#define BT_BIP_HDR_TYPE_DELETE_IMAGE "x-bt/img-img"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于删除图像操作（Delete Image）的 OBEX 类型报头（Type Header）。

<a id="ga09dfef702e656fcc8ee33a42ff567689"></a>

### `BT_BIP_HDR_TYPE_GET_CAPS`

```c
#define BT_BIP_HDR_TYPE_GET_CAPS "x-bt/img-capabilities"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于获取能力操作（Get Capabilities）的 OBEX 类型报头（Type Header）。

<a id="ga6bd29c7d876e3f617797fa91a0ea7ab6"></a>

### `BT_BIP_HDR_TYPE_GET_IMAGE`

```c
#define BT_BIP_HDR_TYPE_GET_IMAGE "x-bt/img-img"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于获取图像操作（Get Image）的 OBEX 类型报头（Type Header）。

<a id="gae993464cf0ac6e7e58f42869effc84a2"></a>

### `BT_BIP_HDR_TYPE_GET_IMAGE_LIST`

```c
#define BT_BIP_HDR_TYPE_GET_IMAGE_LIST "x-bt/img-listing"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于获取图像列表操作（Get Image List）的 OBEX 类型报头（Type Header）。

<a id="ga7eba82c88fc511a25210b65f0d7c4a4f"></a>

### `BT_BIP_HDR_TYPE_GET_IMAGE_PROPERTIES`

```c
#define BT_BIP_HDR_TYPE_GET_IMAGE_PROPERTIES "x-bt/img-properties"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于获取图像属性操作（Get Image Properties）的 OBEX 类型报头（Type Header）。

<a id="gadcfcdfac4571707f8b8b15fba18c592a"></a>

### `BT_BIP_HDR_TYPE_GET_LINKED_ATTACHMENT`

```c
#define BT_BIP_HDR_TYPE_GET_LINKED_ATTACHMENT "x-bt/img-attachment"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于获取关联附件操作（Get Linked Attachment）的 OBEX 类型报头（Type Header）。

<a id="ga34b8c83f54c32026bd7fba15b3333489"></a>

### `BT_BIP_HDR_TYPE_GET_LINKED_THUMBNAIL`

```c
#define BT_BIP_HDR_TYPE_GET_LINKED_THUMBNAIL "x-bt/img-thm"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于获取关联缩略图操作（Get Linked Thumbnail）的 OBEX 类型报头（Type Header）。

<a id="gabb3046494704ab9e6959324e459cbc80"></a>

### `BT_BIP_HDR_TYPE_GET_MONITORING_IMAGE`

```c
#define BT_BIP_HDR_TYPE_GET_MONITORING_IMAGE "x-bt/img-monitoring"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于获取监控图像操作（Get Monitoring Image）的 OBEX 类型报头（Type Header）。

<a id="gab4136d9a07d10380590e791adf57069f"></a>

### `BT_BIP_HDR_TYPE_GET_PARTIAL_IMAGE`

```c
#define BT_BIP_HDR_TYPE_GET_PARTIAL_IMAGE "x-bt/img-partial"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于获取部分图像操作（Get Partial Image）的 OBEX 类型报头（Type Header）。

<a id="ga6c4c9d3b20c7ab5daf5b7cfbc9fcac2f"></a>

### `BT_BIP_HDR_TYPE_GET_STATUS`

```c
#define BT_BIP_HDR_TYPE_GET_STATUS "x-bt/img-status"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于获取状态操作（Get Status）的 OBEX 类型报头（Type Header）。

<a id="ga667582c6e8641099a13671e406f5fd96"></a>

### `BT_BIP_HDR_TYPE_PUT_IMAGE`

```c
#define BT_BIP_HDR_TYPE_PUT_IMAGE "x-bt/img-img"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于放入图像操作（Put Image）的 OBEX 类型报头（Type Header）。

<a id="gaf90f12fea45e37a1d59684a578a58bba"></a>

### `BT_BIP_HDR_TYPE_PUT_LINKED_ATTACHMENT`

```c
#define BT_BIP_HDR_TYPE_PUT_LINKED_ATTACHMENT "x-bt/img-attachment"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于放入关联附件操作（Put Linked Attachment）的 OBEX 类型报头（Type Header）。

<a id="gaf12eff4b680872a4690a0d9c6f873b26"></a>

### `BT_BIP_HDR_TYPE_PUT_LINKED_THUMBNAIL`

```c
#define BT_BIP_HDR_TYPE_PUT_LINKED_THUMBNAIL "x-bt/img-thm"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于放入关联缩略图操作（Put Linked Thumbnail）的 OBEX 类型报头（Type Header）。

<a id="ga4391371df2040895f16e0eed56e75e57"></a>

### `BT_BIP_HDR_TYPE_REMOTE_DISPLAY`

```c
#define BT_BIP_HDR_TYPE_REMOTE_DISPLAY "x-bt/img-display"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于远程显示操作（Remote Display）的 OBEX 类型报头（Type Header）。

<a id="gaafe1edaef34603ceffdb08062e721ed8"></a>

### `BT_BIP_HDR_TYPE_START_ARCHIVE`

```c
#define BT_BIP_HDR_TYPE_START_ARCHIVE "x-bt/img-archive"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于开始归档操作（Start Archive）的 OBEX 类型报头（Type Header）。

<a id="gad57d3fcc35a89eeacb4d92e1362a7097"></a>

### `BT_BIP_HDR_TYPE_START_PRINT`

```c
#define BT_BIP_HDR_TYPE_START_PRINT "x-bt/img-print"
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

用于开始打印操作（Start Print）的 OBEX 类型报头（Type Header）。

<a id="gaabe060f5798f742942d382ed4f06c83d"></a>

### `BT_BIP_HEADER_ID_IMG_DESC`

```c
#define BT_BIP_HEADER_ID_IMG_DESC 0x71
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

图像描述符报头 ID（Img-Descriptor Header ID）。

字节序列（Byte Sequence），前面使用两字节无符号整数表示长度。

<a id="gafb1b58780a45e82c7b1c90a738bddbb9"></a>

### `BT_BIP_HEADER_ID_IMG_HANDLE`

```c
#define BT_BIP_HEADER_ID_IMG_HANDLE 0x30
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

图像句柄报头 ID（Img-Handle Header ID）。

以空字符结尾、采用 UTF-16 编码的 Unicode 文本，前面使用两字节无符号整数表示长度。

<a id="ga445d8c170b5c805d86604f4d474ad0e8"></a>

### `BT_BIP_PRIM_AUTO_ARCHIVE_CB`

```c
#define BT_BIP_PRIM_AUTO_ARCHIVE_CB ( _connect, _disconnect, _get_status, _start_archive )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
{                                                                                          \
        .connect = _connect, .disconnect = _disconnect, .get_status = _get_status,         \
        .start_archive = _start_archive,                                                   \
}
```

主自动归档服务器回调初始化器（Primary Auto Archive Server Callback Initializer）。

用于初始化主级自动归档服务器（Primary Auto Archive Server）回调的辅助宏。

<a id="gaf51de11367b7eeaa0be094d5ad561636"></a>

### `BT_BIP_PRIM_IMAGE_PRINT_CB`

```c
#define BT_BIP_PRIM_IMAGE_PRINT_CB ( _connect, _disconnect, _get_caps, _get_status, _start_print )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
{                                                                                          \
        .connect = _connect, .disconnect = _disconnect, .get_caps = _get_caps,             \
        .get_status = _get_status, .start_print = _start_print,                            \
}
```

主图像打印服务器回调初始化器（Primary Image Print Server Callback Initializer）。

用于初始化主级图像打印服务器（Primary Image Print Server）回调的辅助宏。

<a id="gada2fa948ead9c05ec300dc3af8722e87"></a>

### `BT_BIP_PRIM_IMAGE_PULL_CB`

```c
#define BT_BIP_PRIM_IMAGE_PULL_CB ( _connect, _disconnect, _get_caps, _get_image_list, _get_image_properties, _get_image, _get_linked_thumbnail, _get_linked_attachment, _delete_image )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
{                                                                                          \
        .connect = _connect, .disconnect = _disconnect, .get_caps = _get_caps,             \
        .get_image_list = _get_image_list, .get_image_properties = _get_image_properties,  \
        .get_image = _get_image, .get_linked_thumbnail = _get_linked_thumbnail,            \
        .get_linked_attachment = _get_linked_attachment, .delete_image = _delete_image,    \
}
```

主图像拉取服务器回调初始化器（Primary Image Pull Server Callback Initializer）。

用于初始化主级图像拉取服务器（Primary Image Pull Server）回调的辅助宏。

<a id="ga3d5c7f3a6a0a2fe541022c22995d4274"></a>

### `BT_BIP_PRIM_IMAGE_PUSH_CB`

```c
#define BT_BIP_PRIM_IMAGE_PUSH_CB ( _connect, _disconnect, _get_caps, _put_image, _put_linked_thumbnail, _put_linked_attachment )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
{                                                                                          \
        .connect = _connect, .disconnect = _disconnect, .get_caps = _get_caps,             \
        .put_image = _put_image, .put_linked_thumbnail = _put_linked_thumbnail,            \
        .put_linked_attachment = _put_linked_attachment,                                   \
}
```

主图像推送服务器回调初始化器（Primary Image Push Server Callback Initializer）。

用于初始化主级图像推送服务器（Primary Image Push Server）回调的辅助宏。

<a id="ga144e0d9835516f2e9390d1c966ede6bd"></a>

### `BT_BIP_PRIM_REMOTE_CAMERA_CB`

```c
#define BT_BIP_PRIM_REMOTE_CAMERA_CB ( _connect, _disconnect, _get_image_properties, _get_image, _get_linked_thumbnail, _get_monitoring_image )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
{                                                                                          \
        .connect = _connect, .disconnect = _disconnect,                                    \
        .get_image_properties = _get_image_properties, .get_image = _get_image,            \
        .get_linked_thumbnail = _get_linked_thumbnail,                                     \
        .get_monitoring_image = _get_monitoring_image,                                     \
}
```

主远程相机服务器回调初始化器（Primary Remote Camera Server Callback Initializer）。

用于初始化主级远程相机服务器（Primary Remote Camera Server）回调的辅助宏。

<a id="gabf52b29d7e2f727d9f14e8b53bcc3f4f"></a>

### `BT_BIP_PRIM_REMOTE_DISPLAY_CB`

```c
#define BT_BIP_PRIM_REMOTE_DISPLAY_CB ( _connect, _disconnect, _get_caps, _get_image_list, _put_image, _put_linked_thumbnail, _remote_display )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
{                                                                                          \
        .connect = _connect, .disconnect = _disconnect, .get_caps = _get_caps,             \
        .get_image_list = _get_image_list, .put_image = _put_image,                        \
        .put_linked_thumbnail = _put_linked_thumbnail, .remote_display = _remote_display,  \
}
```

主远程显示服务器回调初始化器（Primary Remote Display Server Callback Initializer）。

用于初始化主级远程显示服务器（Primary Remote Display Server）回调的辅助宏。

<a id="gae305dd59c79605feebffc3c91e641e67"></a>

### `BT_BIP_UUID_ARCHIVED_OBJ`

```c
#define BT_BIP_UUID_ARCHIVED_OBJ
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
(const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
        BT_UUID_128_ENCODE(0x8E61F95E, 0x1A79, 0x11D4, 0x8EA4, 0x00805F9B9834))
```

基本成像配置文件（BIP）的已归档对象服务（Archived Objects Service）的 UUID。

<a id="ga098a435c80d373158ade3dc15dd538e6"></a>

### `BT_BIP_UUID_AUTO_ARCHIVE`

```c
#define BT_BIP_UUID_AUTO_ARCHIVE
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
(const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
        BT_UUID_128_ENCODE(0x940126C0, 0x4608, 0x11D5, 0x841A, 0x0002A5325B4E))
```

基本成像配置文件（BIP）的自动归档服务（Auto Archive Service）的 UUID。

<a id="gaa4b44603eb57cbc223d94a8723abf06a"></a>

### `BT_BIP_UUID_IMAGE_PRINT`

```c
#define BT_BIP_UUID_IMAGE_PRINT
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
(const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
        BT_UUID_128_ENCODE(0x92353350, 0x4608, 0x11D5, 0x841A, 0x0002A5325B4E))
```

基本成像配置文件（BIP）的高级图像打印服务（Advanced Image Printing Service）的 UUID。

<a id="ga42116d3c159adecc6d63c32f0a1c4672"></a>

### `BT_BIP_UUID_IMAGE_PULL`

```c
#define BT_BIP_UUID_IMAGE_PULL
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
(const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
        BT_UUID_128_ENCODE(0x8EE9B3D0, 0x4608, 0x11D5, 0x841A, 0x0002A5325B4E))
```

基本成像配置文件（BIP）的图像拉取服务（Image Pull Service）的 UUID。

<a id="gaca571268fd723b69d19ef7cd97db1da3"></a>

### `BT_BIP_UUID_IMAGE_PUSH`

```c
#define BT_BIP_UUID_IMAGE_PUSH
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
(const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
        BT_UUID_128_ENCODE(0xE33D9545, 0x8374, 0x4AD7, 0x9EC5, 0xC16BE31EDE8E))
```

基本成像配置文件（BIP）的图像推送服务（Image Push Service）的 UUID。

<a id="ga8ef9620a71471340492feb1c8a820b5d"></a>

### `BT_BIP_UUID_REFERENCED_OBJ`

```c
#define BT_BIP_UUID_REFERENCED_OBJ
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
(const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
        BT_UUID_128_ENCODE(0x8E61F95D, 0x1A79, 0x11D4, 0x8EA4, 0x00805F9B9834))
```

基本成像配置文件（BIP）的引用对象服务（Referenced Objects Service）的 UUID。

<a id="ga305af9409b4cfa25a16bed28cd305175"></a>

### `BT_BIP_UUID_REMOTE_CAMERA`

```c
#define BT_BIP_UUID_REMOTE_CAMERA
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
(const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
        BT_UUID_128_ENCODE(0x947E7420, 0x4608, 0x11D5, 0x841A, 0x0002A5325B4E))
```

基本成像配置文件（BIP）的远程相机服务（Remote Camera Service）的 UUID。

<a id="gaa8b43801cd1bf8a4d2c51b0d25a408fc"></a>

### `BT_BIP_UUID_REMOTE_DISPLAY`

```c
#define BT_BIP_UUID_REMOTE_DISPLAY
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

展开值（Value）：

```c
(const struct bt_uuid_128 *)BT_UUID_DECLARE_128(                                           \
        BT_UUID_128_ENCODE(0x94C7CD20, 0x4608, 0x11D5, 0x841A, 0x0002A5325B4E))
```

基本成像配置文件（BIP）的远程显示服务（Remote Display Service）的 UUID。

<a id="ga34de6d20263274292543a7a8afbd2c6b"></a>

### `bt_bip_appl_param_tag_id`

```c
enum bt_bip_appl_param_tag_id
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

基本成像配置文件（BIP）的应用参数标记 ID（Application Parameter Tag IDs）。

这些标签标识符（Tag ID）用于各种基本成像配置文件（BIP）操作的 OBEX 应用参数头（Application Parameter Header）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BIP_APPL_PARAM_TAG_ID_RETURNED_HANDLES` | 返回句柄数量参数（Number of Returned Handles）。 |
| `BT_BIP_APPL_PARAM_TAG_ID_LIST_START_OFFSET` | 列表起始偏移参数（List Start Offset）。 |
| `BT_BIP_APPL_PARAM_TAG_ID_LATEST_CAPTURED_IMAGES` | 最新拍摄图像参数（Latest Captured Images）。 |
| `BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_LEN` | 部分文件长度参数（Partial File Length）。 |
| `BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_START_OFFSET` | 部分文件起始偏移参数（Partial File Start Offset）。 |
| `BT_BIP_APPL_PARAM_TAG_ID_TOTAL_FILE_SIZE` | 文件总大小参数（Total File Size）。 |
| `BT_BIP_APPL_PARAM_TAG_ID_END_FLAG` | 结束标志参数（End Flag）。 |
| `BT_BIP_APPL_PARAM_TAG_ID_REMOTE_DISPLAY` | 远程显示参数（Remote Display）。 |
| `BT_BIP_APPL_PARAM_TAG_ID_SERVICE_ID` | 服务标识符参数（Service ID）。 |
| `BT_BIP_APPL_PARAM_TAG_ID_STORE_FLAG` | 存储标志参数（Store Flag）。 |

<a id="gaff38654d69104bebaaf5884283e197ef"></a>

### `bt_bip_conn_type`

```c
enum bt_bip_conn_type
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

BIP 的 OBEX 连接类型（Connection Types）。

按照基本成像配置文件规范（BIP Specification）定义不同的 BIP 连接类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BIP_PRIM_CONN_TYPE_IMAGE_PUSH` | 主级图像推送连接（Primary Image Push Connection）。 |
| `BT_BIP_PRIM_CONN_TYPE_IMAGE_PULL` | 主级图像拉取连接（Primary Image Pull Connection）。 |
| `BT_BIP_PRIM_CONN_TYPE_ADVANCED_IMAGE_PRINTING` | 主级高级图像打印连接（Primary Advanced Image Printing Connection）。 |
| `BT_BIP_PRIM_CONN_TYPE_AUTO_ARCHIVE` | 主级自动归档连接（Primary Auto Archive Connection）。 |
| `BT_BIP_PRIM_CONN_TYPE_REMOTE_CAMERA` | 主级远程相机连接（Primary Remote Camera Connection）。 |
| `BT_BIP_PRIM_CONN_TYPE_REMOTE_DISPLAY` | 主级远程显示连接（Primary Remote Display Connection）。 |
| `BT_BIP_2ND_CONN_TYPE_REFERENCED_OBJECTS` | 次级引用对象连接（Secondary Referenced Objects Connection）。 |
| `BT_BIP_2ND_CONN_TYPE_ARCHIVED_OBJECTS` | 次级归档对象连接（Secondary Archived Objects Connection）。 |

<a id="ga30d9309cbbd88b54508551285b21e575"></a>

### `bt_bip_role`

```c
enum bt_bip_role
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

BIP 角色类型（Role Types）。

定义设备在 BIP 连接中的角色（Role）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BIP_ROLE_UNKNOWN` | 未知角色（Unknown Role）。 |
| `BT_BIP_ROLE_INITIATOR` | 连接发起方（Connection Initiator）。 |
| `BT_BIP_ROLE_RESPONDER` | 连接响应方（Connection Responder）。 |

<a id="gae4d1ed3b7e27768c1dbb6ce448cb5cf9"></a>

### `bt_bip_state`

```c
enum bt_bip_state
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

BIP 连接状态（Connection State）。

定义 BIP OBEX 连接的状态（Connection State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BIP_STATE_DISCONNECTED` | 连接已断开（Disconnected）。 |
| `BT_BIP_STATE_CONNECTING` | 连接正在建立（Being Established）。 |
| `BT_BIP_STATE_CONNECTED` | 连接已建立（Established）。 |
| `BT_BIP_STATE_DISCONNECTING` | 连接正在终止（Being Terminated）。 |

<a id="gad062c0f3d2feeb92a866f0fe91a6f231"></a>

### `bt_bip_supported_capabilities`

```c
enum bt_bip_supported_capabilities
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

BIP 支持的能力（Supported Capabilities）。

定义 BIP 设备（响应方，Responder）支持的能力（Capabilities）。这些能力表示设备支持的主级 BIP 服务。可以通过按位或运算（Bitwise OR）组合多项能力。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BIP_SUPP_CAP_GENERIC_IMAGE` | 通用成像（Generic Imaging）。 |
| `BT_BIP_SUPP_CAP_CAPTURING` | 拍摄（Capturing）。 |
| `BT_BIP_SUPP_CAP_PRINTING` | 打印（Printing）。 |
| `BT_BIP_SUPP_CAP_DISPLAYING` | 显示（Displaying）。 |

<a id="gacfc8aaea3d27e3a42a14c49b880a5b90"></a>

### `bt_bip_supported_features`

```c
enum bt_bip_supported_features
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

BIP 支持的特性（Supported Features）。

定义 BIP 设备（响应方，Responder）支持的特性（Features）。这些特性表示设备支持的主级 BIP 服务。可以通过按位或运算（Bitwise OR）组合多项特性。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BIP_SUPP_FEAT_IMAGE_PUSH` | 图像推送特性（Image Push）：允许向对端设备推送图像。 |
| `BT_BIP_SUPP_FEAT_IMAGE_PUSH_STORE` | 图像推送存储特性（Image Push Store）：支持永久存储推送的图像。 |
| `BT_BIP_SUPP_FEAT_IMAGE_PUSH_PRINT` | 图像推送打印特性（Image Push Print）：支持直接打印推送的图像。 |
| `BT_BIP_SUPP_FEAT_IMAGE_PUSH_DISPLAY` | 图像推送显示特性（Image Push Display）：支持显示推送的图像。 |
| `BT_BIP_SUPP_FEAT_IMAGE_PULL` | 图像拉取特性（Image Pull）：允许从对端拉取／获取图像。 |
| `BT_BIP_SUPP_FEAT_ADVANCED_IMAGE_PRINT` | 高级图像打印特性（Advanced Image Printing）：支持高级打印操作。 |
| `BT_BIP_SUPP_FEAT_AUTO_ARCHIVE` | 自动归档特性（Auto Archive）：支持自动归档图像。 |
| `BT_BIP_SUPP_FEAT_REMOTE_CAMERA` | 远程相机特性（Remote Camera）：支持远程相机控制和图像拍摄。 |
| `BT_BIP_SUPP_FEAT_REMOTE_DISPLAY` | 远程显示特性（Remote Display）：支持远程显示控制。 |

<a id="ga6768e59b79bb67b5d385fdaa3dfb8888"></a>

### `bt_bip_supported_functions`

```c
enum bt_bip_supported_functions
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

BIP 支持的功能（Supported Functions）。

定义 BIP 设备（响应方，Responder）支持的功能（Functions）。这些功能表示设备能够执行的具体 BIP 操作。可以通过按位或运算（Bitwise OR）组合多项功能。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BIP_SUPP_FUNC_GET_CAPS` | 获取能力功能（Get Capabilities）：支持获取设备能力。 |
| `BT_BIP_SUPP_FUNC_PUT_IMAGE` | 放置图像功能（Put Image）：支持接收／存储图像。 |
| `BT_BIP_SUPP_FUNC_PUT_LINKED_ATTACHMENT` | 放置关联附件功能（Put Linked Attachment）：支持接收图像附件。 |
| `BT_BIP_SUPP_FUNC_PUT_LINKED_THUMBNAIL` | 放置关联缩略图功能（Put Linked Thumbnail）：支持接收图像缩略图。 |
| `BT_BIP_SUPP_FUNC_REMOTE_DISPLAY` | 远程显示功能（Remote Display）：支持远程显示操作。 |
| `BT_BIP_SUPP_FUNC_GET_IMAGE_LIST` | 获取图像列表功能（Get Images List）：支持获取可用图像的列表。 |
| `BT_BIP_SUPP_FUNC_GET_IMAGE_PROPERTIES` | 获取图像属性功能（Get Image Properties）：支持获取图像元数据（Metadata）。 |
| `BT_BIP_SUPP_FUNC_GET_IMAGE` | 获取图像功能（Get Image）：支持获取／发送图像。 |
| `BT_BIP_SUPP_FUNC_GET_LINKED_THUMBNAIL` | 获取关联缩略图功能（Get Linked Thumbnail）：支持获取图像缩略图。 |
| `BT_BIP_SUPP_FUNC_GET_LINKED_ATTACHMENT` | 获取关联附件功能（Get Linked Attachment）：支持获取图像附件。 |
| `BT_BIP_SUPP_FUNC_DELETE_IMAGE` | 删除图像功能（Delete Image）：支持删除对端设备上的图像。 |
| `BT_BIP_SUPP_FUNC_START_PRINT` | 开始打印功能（Start Print）：支持启动打印操作。 |
| `BT_BIP_SUPP_FUNC_GET_PARTIAL_IMAGE` | 获取部分图像功能（Get Partial Image）：支持获取图像的部分数据。 |
| `BT_BIP_SUPP_FUNC_START_ARCHIVE` | 开始归档功能（Start Archive）：支持启动归档操作。 |
| `BT_BIP_SUPP_FUNC_GET_MONITORING_IMAGE` | 获取监视图像功能（Get Monitoring Image）：支持从远程相机获取监视图像。 |
| `BT_BIP_SUPP_FUNC_GET_STATUS` | 获取状态功能（Get Status）：支持获取设备／操作状态。 |

**说明（Note）**：注意（Note）：这些值对应 BIP 规范中的功能定义，用于确定能够在对端设备上执行哪些操作。

<a id="ga7b3c6cb1159e7b2ede57c66f20b23827"></a>

### `bt_bip_transport_state`

```c
enum bt_bip_transport_state
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

BIP 传输状态（Transport State）。

定义底层传输连接（Transport Connection）的状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BIP_TRANSPORT_STATE_DISCONNECTED` | 传输连接已断开（Disconnected）。 |
| `BT_BIP_TRANSPORT_STATE_CONNECTING` | 传输连接正在连接（Connecting）。 |
| `BT_BIP_TRANSPORT_STATE_CONNECTED` | 传输连接已连接（Connected）。 |
| `BT_BIP_TRANSPORT_STATE_DISCONNECTING` | 传输连接正在断开（Disconnecting）。 |

<a id="gaa0f071c8c83a54b2d48f478594579719"></a>

### `bt_bip_abort()`

```c
int bt_bip_abort ( struct bt_bip_client * client, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送OBEX中止请求（OBEX Abort request）。

从客户端发起 OBEX 中止（Abort），取消正在进行的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `buf` | 请求数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga1c341ad182ff418286b64b4eff491445"></a>

### `bt_bip_abort_rsp()`

```c
int bt_bip_abort_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送OBEX中止响应（OBEX Abort response）。

对服务器收到的 OBEX 中止请求（Abort Request）发送响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaf48266502eacfc19938e1dfb29a3619b"></a>

### `bt_bip_add_header_image_desc()`

```c
int bt_bip_add_header_image_desc ( struct net_buf * buf, uint16_t len, const uint8_t * desc )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

向缓冲区添加图像描述符报头（Image Descriptor Header）。

向 OBEX 数据包缓冲区添加图像描述符头（Image Descriptor Header）。描述符包含图像的格式和编码信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要向其中添加头部的缓冲区（Buffer）。 |
| `len` | 描述符数据（Descriptor Data）的长度。 |
| `desc` | 指向描述符数据（Descriptor Data）的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga4ca80902f04ea770c59c5e498fef615a"></a>

### `bt_bip_add_header_image_handle()`

```c
int bt_bip_add_header_image_handle ( struct net_buf * buf, uint16_t len, const uint8_t * handle )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

向缓冲区添加图像句柄报头（Image Handle Header）。

向 OBEX 数据包缓冲区添加图像句柄头（Image Handle Header）。句柄是采用 UTF-16 编码、唯一标识一幅图像的字符串。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要向其中添加头部的缓冲区（Buffer）。 |
| `len` | 句柄数据（Handle Data）的长度，单位为字节。 |
| `handle` | 指向 UTF-16 编码句柄数据（Handle Data）的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga0987a342b43bdd1926f3730f471ca05f"></a>

### `bt_bip_connect_rsp()`

```c
int bt_bip_connect_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送OBEX连接响应（OBEX Connect response）。

对服务器收到的 OBEX 连接请求（Connect Request）发送响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga5302af5beb7cd5c98a9cbdc288f09d3c"></a>

### `bt_bip_delete_image()`

```c
int bt_bip_delete_image ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送删除图像请求（Delete Image request）。

请求删除服务器上的指定图像。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE` 和 `BT_BIP_HEADER_ID_IMG_HANDLE`。类型头（Type Header）的值为 `BT_BIP_HDR_TYPE_DELETE_IMAGE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），应包含图像句柄（Image Handle）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gad53a7666b90a97034276fe341c2bd7a2"></a>

### `bt_bip_delete_image_rsp()`

```c
int bt_bip_delete_image_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送删除图像响应（Delete Image response）。

响应删除图像请求（Delete Image Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaafcd6a3503795299b6fb777ba0aa0cff"></a>

### `bt_bip_disconnect()`

```c
int bt_bip_disconnect ( struct bt_bip_client * client, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送OBEX断开连接请求（OBEX Disconnect request）。

从客户端发起 OBEX 断开连接（Disconnect）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `buf` | 请求数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaddfcee2eaea19b4819d83cf6ecb396da"></a>

### `bt_bip_disconnect_rsp()`

```c
int bt_bip_disconnect_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送OBEX断开连接响应（OBEX Disconnect response）。

对服务器收到的 OBEX 断开连接请求（Disconnect Request）发送响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gafcd2d4e6a8ad906c9692313421175431"></a>

### `bt_bip_get_capabilities()`

```c
int bt_bip_get_capabilities ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取能力请求（Get Capabilities request）。

向服务器请求成像能力（Imaging Capabilities）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID` 和 `BT_OBEX_HEADER_ID_TYPE`。类型头的值为 `BT_BIP_HDR_TYPE_GET_CAPS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaea5d5f5b6c29a44ae89939ee3e2d6efb"></a>

### `bt_bip_get_capabilities_rsp()`

```c
int bt_bip_get_capabilities_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取能力响应（Get Capabilities response）。

使用服务器的能力响应获取能力请求（Get Capabilities Request）。首次响应应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_BODY` 或 `BT_OBEX_HEADER_ID_END_BODY`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），包含能力文档（Capabilities Document）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga79831fc5fff332a891e6b9ff71f81d20"></a>

### `bt_bip_get_image()`

```c
int bt_bip_get_image ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取图像请求（Get Image request）。

向服务器请求图像。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE`、`BT_BIP_HEADER_ID_IMG_HANDLE` 和 `BT_BIP_HEADER_ID_IMG_DESC`。类型头的值为 `BT_BIP_HDR_TYPE_GET_IMAGE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），应包含图像句柄（Image Handle）和描述符（Descriptor）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga9542e030ea863b4379d36fa21de262dc"></a>

### `bt_bip_get_image_list()`

```c
int bt_bip_get_image_list ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取图像列表请求（Get Image List request）。

向服务器请求可用图像的列表。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE`、`BT_OBEX_HEADER_ID_APP_PARAM` 和 `BT_BIP_HEADER_ID_IMG_DESC`。类型头的值为 `BT_BIP_HDR_TYPE_GET_IMAGE_LIST`。应用参数（Application Parameter）应包含标识符 `BT_BIP_APPL_PARAM_TAG_ID_RETURNED_HANDLES`、`BT_BIP_APPL_PARAM_TAG_ID_LIST_START_OFFSET` 和 `BT_BIP_APPL_PARAM_TAG_ID_LATEST_CAPTURED_IMAGES`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga6e33bba952a9693d1fed7ee9bdf03df8"></a>

### `bt_bip_get_image_list_rsp()`

```c
int bt_bip_get_image_list_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取图像列表响应（Get Image List response）。

使用可用图像列表响应获取图像列表请求（Get Image List Request）。首次响应应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_APP_PARAM` 和 `BT_BIP_HEADER_ID_IMG_DESC`。应用参数应包含标识符 `BT_BIP_APPL_PARAM_TAG_ID_RETURNED_HANDLES`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），包含图像列表文档（Image List Document）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga17ae73bd6088b44206378afe3b0b9eb0"></a>

### `bt_bip_get_image_properties()`

```c
int bt_bip_get_image_properties ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取图像属性请求（Get Image Properties request）。

向服务器请求指定图像的属性（Properties）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE` 和 `BT_BIP_HEADER_ID_IMG_HANDLE`。类型头的值为 `BT_BIP_HDR_TYPE_GET_IMAGE_PROPERTIES`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），应包含图像句柄（Image Handle）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga9a91c35e91a0c30eab55da5b842427d9"></a>

### `bt_bip_get_image_properties_rsp()`

```c
int bt_bip_get_image_properties_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取图像属性响应（Get Image Properties response）。

使用图像属性响应获取图像属性请求（Get Image Properties Request）。首次响应应包含应用参数头 `BT_OBEX_HEADER_ID_APP_PARAM`，以及 `BT_OBEX_HEADER_ID_BODY` 或 `BT_OBEX_HEADER_ID_END_BODY`。应用参数应包含标识符 `BT_BIP_APPL_PARAM_TAG_ID_RETURNED_HANDLES`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），包含图像属性文档（Image Properties Document）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga53fb15ff7d0728b09f1c4e8d2ceb6dee"></a>

### `bt_bip_get_image_rsp()`

```c
int bt_bip_get_image_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取图像响应（Get Image response）。

使用所请求的图像数据响应获取图像请求（Get Image Request）。首次响应应包含长度头 `BT_OBEX_HEADER_ID_LEN`，以及 `BT_OBEX_HEADER_ID_BODY` 或 `BT_OBEX_HEADER_ID_END_BODY`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），包含图像数据（Image Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gad95944f07cd9f7b6bb9c81f21fffd447"></a>

### `bt_bip_get_linked_attachment()`

```c
int bt_bip_get_linked_attachment ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取关联附件请求（Get Linked Attachment request）。

请求与指定图像关联的附件（Linked Attachment）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE`、`BT_BIP_HEADER_ID_IMG_HANDLE` 和 `BT_OBEX_HEADER_ID_NAME`。类型头的值为 `BT_BIP_HDR_TYPE_GET_LINKED_ATTACHMENT`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），应包含图像句柄（Image Handle）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga70bf0d46bd16d0207e13eeb9a7844f1c"></a>

### `bt_bip_get_linked_attachment_rsp()`

```c
int bt_bip_get_linked_attachment_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取关联附件响应（Get Linked Attachment response）。

使用附件数据响应获取关联附件请求（Get Linked Attachment Request）。首次响应应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_BODY` 或 `BT_OBEX_HEADER_ID_END_BODY`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），包含附件数据（Attachment Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gad9c05d28e1e2124675b5906990c3408c"></a>

### `bt_bip_get_linked_thumbnail()`

```c
int bt_bip_get_linked_thumbnail ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取关联缩略图请求（Get Linked Thumbnail request）。

请求与指定图像关联的缩略图（Linked Thumbnail）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE` 和 `BT_BIP_HEADER_ID_IMG_HANDLE`。类型头的值为 `BT_BIP_HDR_TYPE_GET_LINKED_THUMBNAIL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），应包含图像句柄（Image Handle）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga5c3cd3e39fc21a584d6955a160ca126a"></a>

### `bt_bip_get_linked_thumbnail_rsp()`

```c
int bt_bip_get_linked_thumbnail_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取关联缩略图响应（Get Linked Thumbnail response）。

使用缩略图数据响应获取关联缩略图请求（Get Linked Thumbnail Request）。首次响应应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_BODY` 或 `BT_OBEX_HEADER_ID_END_BODY`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），包含缩略图数据（Thumbnail Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga9f1593748ffcf29015533d52266a8e19"></a>

### `bt_bip_get_monitoring_image()`

```c
int bt_bip_get_monitoring_image ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取监控图像请求（Get Monitoring Image request）。

向远程相机请求监视图像（Monitoring Image）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE` 和 `BT_OBEX_HEADER_ID_APP_PARAM`。类型头的值为 `BT_BIP_HDR_TYPE_GET_MONITORING_IMAGE`。应用参数应包含标识符 `BT_BIP_APPL_PARAM_TAG_ID_STORE_FLAG`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga301ff6e5a1e8775295659442b8c20e15"></a>

### `bt_bip_get_monitoring_image_rsp()`

```c
int bt_bip_get_monitoring_image_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取监控图像响应（Get Monitoring Image response）。

使用监视图像响应获取监视图像请求（Get Monitoring Image Request）。首次响应应包含图像句柄头 `BT_BIP_HEADER_ID_IMG_HANDLE`，以及 `BT_OBEX_HEADER_ID_BODY` 或 `BT_OBEX_HEADER_ID_END_BODY`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），包含监视图像数据（Monitoring Image Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga2b6a2a51fb00e7060e196051f8aea4c4"></a>

### `bt_bip_get_partial_image()`

```c
int bt_bip_get_partial_image ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取部分图像请求（Get Partial Image request）。

向服务器请求部分图像（Partial Image，即图像的一部分）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE`、`BT_OBEX_HEADER_ID_NAME` 和 `BT_OBEX_HEADER_ID_APP_PARAM`。类型头的值为 `BT_BIP_HDR_TYPE_GET_PARTIAL_IMAGE`。应用参数应包含标识符 `BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_LEN` 和 `BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_START_OFFSET`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），应包含图像句柄（Image Handle）和范围信息（Range Info）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gadf624e05a6d008bdcfd8a61ae6341f42"></a>

### `bt_bip_get_partial_image_rsp()`

```c
int bt_bip_get_partial_image_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取部分图像响应（Get Partial Image response）。

使用所请求的图像部分响应获取部分图像请求（Get Partial Image Request）。首次响应应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_BODY` 或 `BT_OBEX_HEADER_ID_END_BODY`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），包含部分图像数据（Partial Image Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga578c2b59fbc8afee530168452eb221fb"></a>

### `bt_bip_get_status()`

```c
int bt_bip_get_status ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取状态请求（Get Status request）。

向服务器请求状态信息（Status Information）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID` 和 `BT_OBEX_HEADER_ID_TYPE`。类型头的值为 `BT_BIP_HDR_TYPE_GET_STATUS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga7abdde3a7e5dcda9c6187b5e45b75cc2"></a>

### `bt_bip_get_status_rsp()`

```c
int bt_bip_get_status_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送获取状态响应（Get Status response）。

使用状态信息响应获取状态请求（Get Status Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），包含状态文档（Status Document）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaf54b07acf22c5231b2de0fdeca7807c2"></a>

### `bt_bip_l2cap_connect()`

```c
int bt_bip_l2cap_connect ( struct bt_conn * conn, struct bt_bip * bip, uint16_t psm )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

通过 L2CAP 创建传输连接（Transport Connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | ACL 连接对象（Connection Object）。 |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `psm` | L2CAP 协议／服务复用器（PSM，Protocol Service Multiplexer）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga1fda174189b57c54f365784d1909152e"></a>

### `bt_bip_l2cap_disconnect()`

```c
int bt_bip_l2cap_disconnect ( struct bt_bip * bip)
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

断开 BIP L2CAP 连接（Connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaffb77f6c80ba05046df03d62baad211b"></a>

### `bt_bip_l2cap_register()`

```c
int bt_bip_l2cap_register ( struct bt_bip_l2cap_server * server)
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册 BIP L2CAP 服务器（Server）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 要注册的 L2CAP 服务器（Server）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga9352b8309334a3fe89d77f5714443376"></a>

### `bt_bip_primary_advanced_image_printing_client_connect()`

```c
int bt_bip_primary_advanced_image_printing_client_connect ( struct bt_bip * bip, struct bt_bip_client * client, struct bt_bip_client_cb * cb, struct net_buf * buf )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

连接主高级图像打印 OBEX 客户端（Primary Advanced Image Printing OBEX client）。

连接主级高级图像打印客户端（Primary Advanced Image Printing Client）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `client` | BIP 客户端结构（Client Structure）。 |
| `cb` | 客户端回调函数（Client Callback Functions）。 |
| `buf` | 连接请求数据（Connection Request Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gae8b37b224ea419ca1f1761d98a34cb2d"></a>

### `bt_bip_primary_advanced_image_printing_server_register()`

```c
int bt_bip_primary_advanced_image_printing_server_register ( struct bt_bip * bip, struct bt_bip_server * server, const struct bt_uuid_128 * uuid, struct bt_bip_server_cb * cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册主高级图像打印 OBEX 服务器（Primary Advanced Image Printing OBEX server）。

注册主级高级图像打印服务器（Primary Advanced Image Printing Server）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `server` | BIP 服务器结构（Server Structure）。 |
| `uuid` | 服务 UUID（Service UUID），通常为 `BT_BIP_UUID_IMAGE_PRINT`。 |
| `cb` | 服务器回调函数（Server Callback Functions）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga98dca7b222c8a09b1c44861c9060193b"></a>

### `bt_bip_primary_auto_archive_client_connect()`

```c
int bt_bip_primary_auto_archive_client_connect ( struct bt_bip * bip, struct bt_bip_client * client, struct bt_bip_client_cb * cb, struct net_buf * buf )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

连接主自动归档 OBEX 客户端（Primary Auto Archive OBEX client）。

连接主级自动归档客户端（Primary Auto Archive Client）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `client` | BIP 客户端结构（Client Structure）。 |
| `cb` | 客户端回调函数（Client Callback Functions）。 |
| `buf` | 连接请求数据（Connection Request Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga3848d86378912fbd9c896b14aed74161"></a>

### `bt_bip_primary_auto_archive_server_register()`

```c
int bt_bip_primary_auto_archive_server_register ( struct bt_bip * bip, struct bt_bip_server * server, const struct bt_uuid_128 * uuid, struct bt_bip_server_cb * cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册主自动归档 OBEX 服务器（Primary Auto Archive OBEX server）。

注册主级自动归档服务器（Primary Auto Archive Server）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `server` | BIP 服务器结构（Server Structure）。 |
| `uuid` | 服务 UUID（Service UUID），通常为 `BT_BIP_UUID_AUTO_ARCHIVE`。 |
| `cb` | 服务器回调函数（Server Callback Functions）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gad32c1b1118b606ab3ae0d9db889cbab9"></a>

### `bt_bip_primary_client_connect()`

```c
int bt_bip_primary_client_connect ( struct bt_bip * bip, struct bt_bip_client * client, enum bt_bip_conn_type type, struct bt_bip_client_cb * cb, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

连接主 BIP OBEX 客户端（Primary Client）。

针对指定的服务类型，发起主级 BIP 客户端连接（Primary BIP Client Connection）。服务类型使用 `bt_bip_conn_type` 中的 `BT_BIP_PRIM_CONN_TYPE_*` 值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `client` | BIP 客户端结构（Client Structure）。 |
| `type` | 主级连接类型（Primary Connection Type）。 |
| `cb` | 客户端回调函数（Client Callback Functions）。 |
| `buf` | 连接请求数据（Connection Request Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga2d4919c1eb568f33a89d8b176f103601"></a>

### `bt_bip_primary_image_pull_client_connect()`

```c
int bt_bip_primary_image_pull_client_connect ( struct bt_bip * bip, struct bt_bip_client * client, struct bt_bip_client_cb * cb, struct net_buf * buf )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

连接主图像拉取 OBEX 客户端（Primary Image Pull OBEX client）。

连接主级图像拉取客户端（Primary Image Pull Client）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `client` | BIP 客户端结构（Client Structure）。 |
| `cb` | 客户端回调函数（Client Callback Functions）。 |
| `buf` | 连接请求数据（Connection Request Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga35c44217cbfcd8661c3f2e5725be9323"></a>

### `bt_bip_primary_image_pull_server_register()`

```c
int bt_bip_primary_image_pull_server_register ( struct bt_bip * bip, struct bt_bip_server * server, const struct bt_uuid_128 * uuid, struct bt_bip_server_cb * cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册主图像拉取 OBEX 服务器（Primary Image Pull OBEX server）。

注册主级图像拉取服务器（Primary Image Pull Server）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `server` | BIP 服务器结构（Server Structure）。 |
| `uuid` | 服务 UUID（Service UUID），通常为 `BT_BIP_UUID_IMAGE_PULL`。 |
| `cb` | 服务器回调函数（Server Callback Functions）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga39ec2019f86d42b02992b0a9d3ba094c"></a>

### `bt_bip_primary_image_push_client_connect()`

```c
int bt_bip_primary_image_push_client_connect ( struct bt_bip * bip, struct bt_bip_client * client, struct bt_bip_client_cb * cb, struct net_buf * buf )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

连接主图像推送 OBEX 客户端（Primary Image Push OBEX client）。

连接主级图像推送客户端（Primary Image Push Client）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `client` | BIP 客户端结构（Client Structure）。 |
| `cb` | 客户端回调函数（Client Callback Functions）。 |
| `buf` | 连接请求数据（Connection Request Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaefd318b5dc2e813eea2cd7608be1170c"></a>

### `bt_bip_primary_image_push_server_register()`

```c
int bt_bip_primary_image_push_server_register ( struct bt_bip * bip, struct bt_bip_server * server, const struct bt_uuid_128 * uuid, struct bt_bip_server_cb * cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册主图像推送 OBEX 服务器（Primary Image Push OBEX server）。

注册主级图像推送服务器（Primary Image Push Server）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `server` | BIP 服务器结构（Server Structure）。 |
| `uuid` | 服务 UUID（Service UUID），通常为 `BT_BIP_UUID_IMAGE_PUSH`。 |
| `cb` | 服务器回调函数（Server Callback Functions）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga30e3a6ad8c00c230ac3591a934cfb81f"></a>

### `bt_bip_primary_remote_camera_client_connect()`

```c
int bt_bip_primary_remote_camera_client_connect ( struct bt_bip * bip, struct bt_bip_client * client, struct bt_bip_client_cb * cb, struct net_buf * buf )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

连接主远程相机 OBEX 客户端（Primary Remote Camera OBEX client）。

连接主级远程相机客户端（Primary Remote Camera Client）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `client` | BIP 客户端结构（Client Structure）。 |
| `cb` | 客户端回调函数（Client Callback Functions）。 |
| `buf` | 连接请求数据（Connection Request Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga4b236a8a28c359e392633d472a508405"></a>

### `bt_bip_primary_remote_camera_server_register()`

```c
int bt_bip_primary_remote_camera_server_register ( struct bt_bip * bip, struct bt_bip_server * server, const struct bt_uuid_128 * uuid, struct bt_bip_server_cb * cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册主远程相机 OBEX 服务器（Primary Remote Camera OBEX server）。

注册主级远程相机服务器（Primary Remote Camera Server）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `server` | BIP 服务器结构（Server Structure）。 |
| `uuid` | 服务 UUID（Service UUID），通常为 `BT_BIP_UUID_REMOTE_CAMERA`。 |
| `cb` | 服务器回调函数（Server Callback Functions）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gac4ba5cef40cd451bd4b505dbea0fa135"></a>

### `bt_bip_primary_remote_display_client_connect()`

```c
int bt_bip_primary_remote_display_client_connect ( struct bt_bip * bip, struct bt_bip_client * client, struct bt_bip_client_cb * cb, struct net_buf * buf )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

连接主远程显示 OBEX 客户端（Primary Remote Display OBEX client）。

连接主级远程显示客户端（Primary Remote Display Client）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `client` | BIP 客户端结构（Client Structure）。 |
| `cb` | 客户端回调函数（Client Callback Functions）。 |
| `buf` | 连接请求数据（Connection Request Data）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga5167b2dab89a983fae9fca356e6fbcf9"></a>

### `bt_bip_primary_remote_display_server_register()`

```c
int bt_bip_primary_remote_display_server_register ( struct bt_bip * bip, struct bt_bip_server * server, const struct bt_uuid_128 * uuid, struct bt_bip_server_cb * cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册主远程显示 OBEX 服务器（Primary Remote Display OBEX server）。

注册主级远程显示服务器（Primary Remote Display Server）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `server` | BIP 服务器结构（Server Structure）。 |
| `uuid` | 服务 UUID（Service UUID），通常为 `BT_BIP_UUID_REMOTE_DISPLAY`。 |
| `cb` | 服务器回调函数（Server Callback Functions）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga45f1ca2d2874500d6f8df3a62b01260e"></a>

### `bt_bip_primary_server_register()`

```c
int bt_bip_primary_server_register ( struct bt_bip * bip, struct bt_bip_server * server, enum bt_bip_conn_type type, const struct bt_uuid_128 * uuid, struct bt_bip_server_cb * cb )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册主 BIP OBEX 服务器（Primary Server）。

针对指定的连接类型（Connection Type）和服务 UUID，注册主级 BIP 服务器（Primary BIP Server）。主级服务器处理各自服务类型的主要 BIP 操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `server` | 要注册的 BIP 服务器结构（Server Structure）。 |
| `type` | 主级连接类型（Primary Connection Type），例如 `IMAGE_PUSH`、`IMAGE_PULL` 等。 |
| `uuid` | 服务器的服务 UUID（Service UUID）。 |
| `cb` | 处理服务器操作的回调函数（Callback Functions）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaf551904672eda53e9dfcbb5a6bf4c2c3"></a>

### `bt_bip_put_image()`

```c
int bt_bip_put_image ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送放入图像请求（Put Image request）。

向服务器发送图像。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE`、`BT_OBEX_HEADER_ID_NAME` 和 `BT_BIP_HEADER_ID_IMG_DESC`。类型头的值为 `BT_BIP_HDR_TYPE_PUT_IMAGE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），包含图像数据和元数据（Metadata）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga002f7713a8269c0b00a415bbb8c53fce"></a>

### `bt_bip_put_image_rsp()`

```c
int bt_bip_put_image_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送放入图像响应（Put Image response）。

响应放置图像请求（Put Image Request）。首次响应应包含以下 OBEX 头：`BT_BIP_HEADER_ID_IMG_HANDLE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），可能包含图像句柄（Image Handle）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga86085e98964dcfd19725b5d96f38a99b"></a>

### `bt_bip_put_linked_attachment()`

```c
int bt_bip_put_linked_attachment ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送放入关联附件请求（Put Linked Attachment request）。

发送与指定图像关联的附件（Linked Attachment）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE`、`BT_BIP_HEADER_ID_IMG_HANDLE` 和 `BT_BIP_HEADER_ID_IMG_DESC`。类型头的值为 `BT_BIP_HDR_TYPE_PUT_LINKED_ATTACHMENT`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），包含附件数据和图像句柄（Image Handle）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gad6a7df2b0c49c0df616ef170c7b9e431"></a>

### `bt_bip_put_linked_attachment_rsp()`

```c
int bt_bip_put_linked_attachment_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送放入关联附件响应（Put Linked Attachment response）。

响应放置关联附件请求（Put Linked Attachment Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga8b730495f4dd4e6f8db85c5b060a3cae"></a>

### `bt_bip_put_linked_thumbnail()`

```c
int bt_bip_put_linked_thumbnail ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送放入关联缩略图请求（Put Linked Thumbnail request）。

发送与指定图像关联的缩略图（Linked Thumbnail）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE` 和 `BT_BIP_HEADER_ID_IMG_HANDLE`。类型头的值为 `BT_BIP_HDR_TYPE_PUT_LINKED_THUMBNAIL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），包含缩略图数据和图像句柄（Image Handle）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gac96e873a840b072f5213b7483d633aaa"></a>

### `bt_bip_put_linked_thumbnail_rsp()`

```c
int bt_bip_put_linked_thumbnail_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送放入关联缩略图响应（Put Linked Thumbnail response）。

响应放置关联缩略图请求（Put Linked Thumbnail Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga021a5d82b292d04cd0e2d53b1b32344b"></a>

### `bt_bip_remote_display()`

```c
int bt_bip_remote_display ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送远程显示请求（Remote Display request）。

向服务器发送远程显示命令（Remote Display Command）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE`、`BT_BIP_HEADER_ID_IMG_HANDLE` 和 `BT_OBEX_HEADER_ID_APP_PARAM`。类型头的值为 `BT_BIP_HDR_TYPE_REMOTE_DISPLAY`。应用参数应包含标识符 `BT_BIP_APPL_PARAM_TAG_ID_REMOTE_DISPLAY`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），包含显示命令（Display Command）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga0c54da02bc8dda26794f398e06e66cb3"></a>

### `bt_bip_remote_display_rsp()`

```c
int bt_bip_remote_display_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送远程显示响应（Remote Display response）。

响应远程显示请求（Remote Display Request）。首次响应应包含以下 OBEX 头：`BT_BIP_HEADER_ID_IMG_HANDLE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga5ed2a46482e4fe60ef23c540001b58a3"></a>

### `bt_bip_rfcomm_connect()`

```c
int bt_bip_rfcomm_connect ( struct bt_conn * conn, struct bt_bip * bip, uint8_t channel )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

通过 RFCOMM 创建传输连接（Transport Connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | ACL 连接对象（Connection Object）。 |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `channel` | RFCOMM 通道编号（Channel Number）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga66a86a399f73dba932dc05d63b3749bd"></a>

### `bt_bip_rfcomm_disconnect()`

```c
int bt_bip_rfcomm_disconnect ( struct bt_bip * bip)
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

断开 BIP RFCOMM 连接（Connection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga644ca479c156b10d920d87d862401fc7"></a>

### `bt_bip_rfcomm_register()`

```c
int bt_bip_rfcomm_register ( struct bt_bip_rfcomm_server * server)
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册 BIP RFCOMM 服务器（Server）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 要注册的 RFCOMM 服务器（Server）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga72ef6cd266b7e57e1c80b6d8eba799e2"></a>

### `bt_bip_secondary_advanced_image_printing_client_connect()`

```c
int bt_bip_secondary_advanced_image_printing_client_connect ( struct bt_bip * bip, struct bt_bip_client * client, struct bt_bip_client_cb * cb, struct net_buf * buf, struct bt_bip_server * primary_server )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

连接次级高级图像打印 OBEX 客户端（Secondary Advanced Image Printing OBEX client）。

连接次级高级图像打印客户端（Secondary Advanced Image Printing Client）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `client` | BIP 客户端结构（Client Structure）。 |
| `cb` | 客户端回调函数（Client Callback Functions）。 |
| `buf` | 连接请求数据（Connection Request Data）。 |
| `primary_server` | 关联的主级服务器（Associated Primary Server）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga54c37cced33fa72a2c6cea10e2996e6d"></a>

### `bt_bip_secondary_advanced_image_printing_server_register()`

```c
int bt_bip_secondary_advanced_image_printing_server_register ( struct bt_bip * bip, struct bt_bip_server * server, const struct bt_uuid_128 * uuid, struct bt_bip_server_cb * cb, struct bt_bip_client * primary_client )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册次级高级图像打印 OBEX 服务器（Secondary Advanced Image Printing OBEX server）。

注册次级高级图像打印服务器（Secondary Advanced Image Printing Server）的便捷函数。此服务器处理打印服务的引用对象（Referenced Objects）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `server` | BIP 服务器结构（Server Structure）。 |
| `uuid` | 服务 UUID（Service UUID），通常为 `BT_BIP_UUID_REFERENCED_OBJ`。 |
| `cb` | 服务器回调函数（Server Callback Functions）。 |
| `primary_client` | 关联的主级客户端（Associated Primary Client）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga1975916aa3da40576499f6d05aac1285"></a>

### `bt_bip_secondary_auto_archive_client_connect()`

```c
int bt_bip_secondary_auto_archive_client_connect ( struct bt_bip * bip, struct bt_bip_client * client, struct bt_bip_client_cb * cb, struct net_buf * buf, struct bt_bip_server * primary_server )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

连接次级自动归档 OBEX 客户端（Secondary Auto Archive OBEX client）。

连接次级自动归档客户端（Secondary Auto Archive Client）的便捷函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `client` | BIP 客户端结构（Client Structure）。 |
| `cb` | 客户端回调函数（Client Callback Functions）。 |
| `buf` | 连接请求数据（Connection Request Data）。 |
| `primary_server` | 关联的主级服务器（Associated Primary Server）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gab24c4f7144f8c43dcf1b82a4c33e4ffd"></a>

### `bt_bip_secondary_auto_archive_server_register()`

```c
int bt_bip_secondary_auto_archive_server_register ( struct bt_bip * bip, struct bt_bip_server * server, const struct bt_uuid_128 * uuid, struct bt_bip_server_cb * cb, struct bt_bip_client * primary_client )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册次级自动归档 OBEX 服务器（Secondary Auto Archive OBEX server）。

注册次级自动归档服务器（Secondary Auto Archive Server）的便捷函数。此服务器处理自动归档服务的归档对象（Archived Objects）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `server` | BIP 服务器结构（Server Structure）。 |
| `uuid` | 服务 UUID（Service UUID），通常为 `BT_BIP_UUID_ARCHIVED_OBJ`。 |
| `cb` | 服务器回调函数（Server Callback Functions）。 |
| `primary_client` | 关联的主级客户端（Associated Primary Client）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gae557b198b9d5606ee05cd29ed16f9482"></a>

### `bt_bip_secondary_client_connect()`

```c
int bt_bip_secondary_client_connect ( struct bt_bip * bip, struct bt_bip_client * client, enum bt_bip_conn_type type, struct bt_bip_client_cb * cb, struct net_buf * buf, struct bt_bip_server * primary_server )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

连接次级 BIP OBEX 客户端（Secondary Client）。

使用 `bt_bip_conn_type` 中指定的 `BT_BIP_2ND_CONN_TYPE_` 类型，向 BIP 发起方（Initiator）的次级服务器发起次级 BIP 客户端连接。该 BIP 发起方作为主级 OBEX 客户端（Primary OBEX Client）工作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `client` | BIP 客户端结构（Client Structure）。 |
| `type` | 次级连接类型（Secondary Connection Type）。 |
| `cb` | 客户端回调函数（Client Callback Functions）。 |
| `buf` | 连接请求数据（Connection Request Data）。 |
| `primary_server` | 关联的主级服务器（Associated Primary Server）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gab0a3b58b041ac4af2682fb96b8f00a7e"></a>

### `bt_bip_secondary_server_register()`

```c
int bt_bip_secondary_server_register ( struct bt_bip * bip, struct bt_bip_server * server, enum bt_bip_conn_type type, const struct bt_uuid_128 * uuid, struct bt_bip_server_cb * cb, struct bt_bip_client * primary_client )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注册次级 BIP OBEX 服务器（Secondary Server）。

注册与主级客户端协同工作的次级 BIP 服务器（Secondary BIP Server）。次级服务器处理引用对象（Referenced Objects）或归档对象（Archived Objects）等操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | 基本成像规范实例（BIP instance）。 |
| `server` | 要注册的 BIP 服务器结构（Server Structure）。 |
| `type` | 次级连接类型（Secondary Connection Type），为 `REFERENCED_OBJECTS` 或 `ARCHIVED_OBJECTS`。 |
| `uuid` | 服务器的服务 UUID（Service UUID）。 |
| `cb` | 处理服务器操作的回调函数（Callback Functions）。 |
| `primary_client` | 关联的主级客户端（Associated Primary Client）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga4e06b2fb9a99f89d7e65e8a52690442d"></a>

### `bt_bip_server_unregister()`

```c
int bt_bip_server_unregister ( struct bt_bip_server * server)
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

注销 BIP OBEX 服务器（Server）。

注销此前已注册的 BIP 服务器（Server）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 要注销的 BIP 服务器（Server）。 |

**说明（Note）**：注意（Note）：指定服务器只有在连接已断开后才能注销。

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga0180461f24c6f741e056d64f9758b89e"></a>

### `bt_bip_set_supported_capabilities()`

```c
int bt_bip_set_supported_capabilities ( struct bt_bip * bip, uint8_t capabilities )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

设置 BIP 响应方（Responder）支持的能力（Capabilities）。

为本地 BIP 发起方（Initiator）设置对端 BIP 响应方（Responder）支持的能力位掩码（Capabilities Bitmask）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | BIP 发起方实例（Initiator Instance）。 |
| `capabilities` | 支持的能力位掩码（Capabilities Bitmask）。通过 SDP 发现过程（SDP Discovery）从 BIP 响应方获取。 |

返回（Returns）：成功时为0，失败时为负错误码。

**说明（Note）**：注意（Note）：应在建立任何 BIP OBEX 连接之前调用此函数。能力值（Capabilities Value）通常通过 SDP 发现过程获取。

<a id="gab5a80d7a992d0afa0270eb09d6f3275c"></a>

### `bt_bip_set_supported_features()`

```c
int bt_bip_set_supported_features ( struct bt_bip * bip, uint16_t features )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

设置 BIP 响应方（Responder）支持的特性（Features）。

为本地 BIP 发起方（Initiator）设置对端 BIP 响应方（Responder）支持的特性位掩码（Features Bitmask）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | BIP 发起方实例（Initiator Instance）。 |
| `features` | 支持的特性位掩码（Features Bitmask）。通过 SDP 发现过程（SDP Discovery）从 BIP 响应方获取。 |

返回（Returns）：成功时为0，失败时为负错误码。

**说明（Note）**：注意（Note）：应在建立任何 BIP OBEX 连接之前调用此函数。特性值（Features Value）通常通过 SDP 发现过程获取。

<a id="gafe7df6ee236da3a11104f1aa6e948bfe"></a>

### `bt_bip_set_supported_functions()`

```c
int bt_bip_set_supported_functions ( struct bt_bip * bip, uint32_t functions )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

设置 BIP 响应方（Responder）支持的功能（Functions）。

为本地 BIP 发起方（Initiator）设置对端 BIP 响应方（Responder）支持的功能位掩码（Functions Bitmask）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bip` | BIP 发起方实例（Initiator Instance）。 |
| `functions` | 支持的功能位掩码（Functions Bitmask）。通过 SDP 发现过程（SDP Discovery）从 BIP 响应方获取。 |

返回（Returns）：成功时为0，失败时为负错误码。

**说明（Note）**：注意（Note）：应在建立任何 BIP OBEX 连接之前调用此函数。功能值（Functions Value）通常通过 SDP 发现过程获取。

<a id="ga9674dc3dc2137a663a971f8521a41845"></a>

### `bt_bip_start_archive()`

```c
int bt_bip_start_archive ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送开始归档请求（Start Archive request）。

在服务器上启动归档操作（Archive Operation）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE` 和 `BT_OBEX_HEADER_ID_APP_PARAM`。类型头的值为 `BT_BIP_HDR_TYPE_START_ARCHIVE`。应用参数应包含标识符 `BT_BIP_APPL_PARAM_TAG_ID_STORE_FLAG`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），包含归档控制对象（Archive Control Object）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gad16038fa018919a10d9be7fa6deeb659"></a>

### `bt_bip_start_archive_rsp()`

```c
int bt_bip_start_archive_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送开始归档响应（Start Archive response）。

响应开始归档请求（Start Archive Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），可能包含作业标识符（Job ID）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga8a948dcee431ced321e7b5d51c8d5f9c"></a>

### `bt_bip_start_print()`

```c
int bt_bip_start_print ( struct bt_bip_client * client, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送开始打印请求（Start Print request）。

在服务器上启动打印作业（Print Job）。首次请求应包含以下 OBEX 头：`BT_OBEX_HEADER_ID_CONN_ID`、`BT_OBEX_HEADER_ID_TYPE` 和 `BT_OBEX_HEADER_ID_APP_PARAM`。类型头的值为 `BT_BIP_HDR_TYPE_START_PRINT`。应用参数应包含标识符 `BT_BIP_APPL_PARAM_TAG_ID_STORE_FLAG`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区（Request Data Buffer），包含打印控制对象（Print Control Object）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gae9ea9f936aa75b287a2152a747fd687a"></a>

### `bt_bip_start_print_rsp()`

```c
int bt_bip_start_print_rsp ( struct bt_bip_server * server, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/bip.h>
```

发送开始打印响应（Start Print response）。

响应开始打印请求（Start Print Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区（Response Data Buffer），可能包含作业标识符（Job ID）。 |

返回（Returns）：成功时为0，失败时为负错误码。


## 2.6\_原页交叉引用（Cross References）

- [bt_bip_transport_ops](../bluetooth_service_model_reference/P008_bt_bip_transport_ops_结构体.md)
- [bt_bip_rfcomm_server](../bluetooth_service_model_reference/P005_bt_bip_rfcomm_server_结构体.md)
- [bt_bip_l2cap_server](../bluetooth_service_model_reference/P004_bt_bip_l2cap_server_结构体.md)
- [bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)
- [bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)
- [bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)
- [bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)
- [bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/bluetooth/classic/bip.h](../api_file_kernel_network_reference/P001_zephyr__bluetooth__classic__bip.h_文件参考.md)
- [BT_UUID_DECLARE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gadece715e13e2a529aa55c298ff760bf0)
- [BT_UUID_128_ENCODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#gac3973b66e992cbc0940752b77b378f43)
- [BT_OBEX_HEADER_ID_CONN_ID](../api_bluetooth_service_control_reference/P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#gga3c893652eb9a5f0bf699d357caf40948a3417001aed5d114492dcbe2c29496a1b)
- [BT_OBEX_HEADER_ID_TYPE](../api_bluetooth_service_control_reference/P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#gga3c893652eb9a5f0bf699d357caf40948a8bfeff22eabea432eb5863a974adb745)
- [BT_OBEX_HEADER_ID_BODY](../api_bluetooth_service_control_reference/P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#gga3c893652eb9a5f0bf699d357caf40948a3264aa53da0fd7ec6611b8a20a8745f4)
- [BT_OBEX_HEADER_ID_END_BODY](../api_bluetooth_service_control_reference/P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#gga3c893652eb9a5f0bf699d357caf40948aaa78dab2eda48ebd5d594024b53bec6b)
- [BT_OBEX_HEADER_ID_APP_PARAM](../api_bluetooth_service_control_reference/P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#gga3c893652eb9a5f0bf699d357caf40948a6dac6844a5db11dbc0e43613a32c13a9)
- [BT_OBEX_HEADER_ID_LEN](../api_bluetooth_service_control_reference/P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#gga3c893652eb9a5f0bf699d357caf40948ae075bf9dd7e57c66613ffb3de84f09bb)
- [BT_OBEX_HEADER_ID_NAME](../api_bluetooth_service_control_reference/P005_IrDA 对象交换协议（Object Exchange Protocol，OBEX）.md#gga3c893652eb9a5f0bf699d357caf40948adf199ff987c26bd8d6301c409fb5f6a4)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__uuid_html_gac3973b66e992cbc0940752b77b378f43"></a>
<a id="agroup__bt__uuid_html_gadece715e13e2a529aa55c298ff760bf0"></a>
<a id="astructbt__uuid__128_html"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga34de6d20263274292543a7a8afbd2c6bace4966644e9194273b635b916eac0871"></a>
<a id="gga34de6d20263274292543a7a8afbd2c6ba0f0d78c2da3d8f3d0caf015525b3e010"></a>
<a id="gga34de6d20263274292543a7a8afbd2c6ba9dbbb8ed95c7ccd86a74263fef1a1e92"></a>
<a id="gga34de6d20263274292543a7a8afbd2c6bad6511bb04da2cf325a39bfee93f51e0c"></a>
<a id="gga34de6d20263274292543a7a8afbd2c6ba0ff60914fb36e587b42a473c25bd6a2d"></a>
<a id="gga34de6d20263274292543a7a8afbd2c6ba2565f26c0322935acef85725ac8982e5"></a>
<a id="gga34de6d20263274292543a7a8afbd2c6baa7b18ee3ae56c0f0e84a103c1e59f05d"></a>
<a id="gga34de6d20263274292543a7a8afbd2c6bab0e2dfb17de25f4ec3b27b29c2659afa"></a>
<a id="gga34de6d20263274292543a7a8afbd2c6ba683d101ea1babf1f147d1869ab7424f4"></a>
<a id="gga34de6d20263274292543a7a8afbd2c6baef58e631bfd6c511318c386308374274"></a>
<a id="ggaff38654d69104bebaaf5884283e197efa612cd818200f49e37235917fead216d2"></a>
<a id="ggaff38654d69104bebaaf5884283e197efa05372dbd0a01855f0863ce355a503c61"></a>
<a id="ggaff38654d69104bebaaf5884283e197efa05de3a972070aa4d1e29851479860d9f"></a>
<a id="ggaff38654d69104bebaaf5884283e197efaf762949693b7cf70739ed0a0eb6a9d58"></a>
<a id="ggaff38654d69104bebaaf5884283e197efa8b576c667b9c6458e44ec67674bdffbd"></a>
<a id="ggaff38654d69104bebaaf5884283e197efa12873fc1888cd99703131ae71134f0c7"></a>
<a id="ggaff38654d69104bebaaf5884283e197efa4d5ab575c877aa2a43c29cbb52a361c7"></a>
<a id="ggaff38654d69104bebaaf5884283e197efabe15f984d6907bdb40c10e893e1c3bf6"></a>
<a id="gga30d9309cbbd88b54508551285b21e575aaa7de8d668d248049c5d5c75ae35d74b"></a>
<a id="gga30d9309cbbd88b54508551285b21e575aa5cdb11f2b0ac9c20c380dd48c9edaa5"></a>
<a id="gga30d9309cbbd88b54508551285b21e575a87d1fe99824b216780435898c2dfa968"></a>
<a id="ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a984245e44981ad3d85518ab1c3f576e8"></a>
<a id="ggae4d1ed3b7e27768c1dbb6ce448cb5cf9acdc7fe9ee4c0d0ba447bc43817364478"></a>
<a id="ggae4d1ed3b7e27768c1dbb6ce448cb5cf9ae65c7b972effa225116ec8abfcf07bc3"></a>
<a id="ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a96f12788ce6f56012ac4b1c25f63f67e"></a>
<a id="ggad062c0f3d2feeb92a866f0fe91a6f231a786ef1ad1bde68f9b026c9d080cc41d4"></a>
<a id="ggad062c0f3d2feeb92a866f0fe91a6f231ac9c5d73b0d2d5eb25a962fa72ede6d5a"></a>
<a id="ggad062c0f3d2feeb92a866f0fe91a6f231a4a738d195dcf0908a64bdd246672d4bb"></a>
<a id="ggad062c0f3d2feeb92a866f0fe91a6f231a324c0590cefb5d7a39f90d90e3466334"></a>
<a id="ggacfc8aaea3d27e3a42a14c49b880a5b90ac14657fd4af96f4c837916b832c25a0f"></a>
<a id="ggacfc8aaea3d27e3a42a14c49b880a5b90a8904b7b8288e1b47d2242f5d686e32d9"></a>
<a id="ggacfc8aaea3d27e3a42a14c49b880a5b90add6c2e70541aae8124bad4b102d64b88"></a>
<a id="ggacfc8aaea3d27e3a42a14c49b880a5b90a49668a596059e535bd59ac095dffa050"></a>
<a id="ggacfc8aaea3d27e3a42a14c49b880a5b90aba576edd916dbf49118e78572f70320b"></a>
<a id="ggacfc8aaea3d27e3a42a14c49b880a5b90ac64d953311bc9b76bfe75dd3133f5563"></a>
<a id="ggacfc8aaea3d27e3a42a14c49b880a5b90af72e05ca427f8c5091e50cddac522045"></a>
<a id="ggacfc8aaea3d27e3a42a14c49b880a5b90a97141e2764fad3714c03b6be69ff2a9a"></a>
<a id="ggacfc8aaea3d27e3a42a14c49b880a5b90a132dd77e79fbfda8a78d5034d4c618c5"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888a2e1f3364145560587963402881bb2705"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888afb1777cefdbd00e3432ddf5180804f48"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888a8a417f3073f017af866877f88ee10228"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888a0ee047481a35e26fa0d03bf7594d7752"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888adb0e03118b1cd62fe7e97b53e9f52d41"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888a7843f4dece6ff449b97ba0a2c7298b90"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888af29095b3b5964062e98b9e357de87f89"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888a50271c1bac792020f0fb869bb523e506"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888a03c928dd502a98b72cb7d8eebad4b384"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888ac3ec252a63d494ce3e4dd696d05d94bc"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888a045dfb07426eacb16fd69247eecf70b1"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888ae1312bb3417f901204ac592e4b9376df"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888ae1e97efb19d10ac2b508a9e65b5c43ce"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888a3cae66cb380311938f83bb099a2d02da"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888a0bde5efd58b339e53db3779a159239c1"></a>
<a id="gga6768e59b79bb67b5d385fdaa3dfb8888abf825fb7d634906f0204780ef81ca5b3"></a>
<a id="gga7b3c6cb1159e7b2ede57c66f20b23827ae78c865c0034d405391aaf9f72e4c9b2"></a>
<a id="gga7b3c6cb1159e7b2ede57c66f20b23827ad4444da19b4e0f499867ea967dfc578f"></a>
<a id="gga7b3c6cb1159e7b2ede57c66f20b23827a1af8a1481b10b53c58af8e36c7b91588"></a>
<a id="gga7b3c6cb1159e7b2ede57c66f20b23827a7340b2e209c71d9f944b303c22cb264d"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_核心规范分配编号（Core Specification Assigned Numbers）.md) · [返回大纲](大纲.md) · [下一章](P003_服务发现协议（Service Discovery Protocol，SDP）.md)
