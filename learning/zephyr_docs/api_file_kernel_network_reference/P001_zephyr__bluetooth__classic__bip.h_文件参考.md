---
id: learning.zephyr-docs.api-file-kernel-network-reference.page-1
title: zephyr__bluetooth__classic__bip.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bip_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_classic\_\_bip.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

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

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

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

## 1.2\_宏定义（Macros）

<a id="r_ga09dfef702e656fcc8ee33a42ff567689"></a>

```c
#define BT_BIP_HDR_TYPE_GET_CAPS "x-bt/img-capabilities"
```

相关声明：[BT_BIP_HDR_TYPE_GET_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga09dfef702e656fcc8ee33a42ff567689)。

用于获取能力操作（Get Capabilities）的 OBEX 类型报头（Type Header）。

<a id="r_gae993464cf0ac6e7e58f42869effc84a2"></a>

```c
#define BT_BIP_HDR_TYPE_GET_IMAGE_LIST "x-bt/img-listing"
```

相关声明：[BT_BIP_HDR_TYPE_GET_IMAGE_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae993464cf0ac6e7e58f42869effc84a2)。

用于获取图像列表操作（Get Image List）的 OBEX 类型报头（Type Header）。

<a id="r_ga7eba82c88fc511a25210b65f0d7c4a4f"></a>

```c
#define BT_BIP_HDR_TYPE_GET_IMAGE_PROPERTIES "x-bt/img-properties"
```

相关声明：[BT_BIP_HDR_TYPE_GET_IMAGE_PROPERTIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga7eba82c88fc511a25210b65f0d7c4a4f)。

用于获取图像属性操作（Get Image Properties）的 OBEX 类型报头（Type Header）。

<a id="r_ga6bd29c7d876e3f617797fa91a0ea7ab6"></a>

```c
#define BT_BIP_HDR_TYPE_GET_IMAGE "x-bt/img-img"
```

相关声明：[BT_BIP_HDR_TYPE_GET_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga6bd29c7d876e3f617797fa91a0ea7ab6)。

用于获取图像操作（Get Image）的 OBEX 类型报头（Type Header）。

<a id="r_ga34b8c83f54c32026bd7fba15b3333489"></a>

```c
#define BT_BIP_HDR_TYPE_GET_LINKED_THUMBNAIL "x-bt/img-thm"
```

相关声明：[BT_BIP_HDR_TYPE_GET_LINKED_THUMBNAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga34b8c83f54c32026bd7fba15b3333489)。

用于获取关联缩略图操作（Get Linked Thumbnail）的 OBEX 类型报头（Type Header）。

<a id="r_gadcfcdfac4571707f8b8b15fba18c592a"></a>

```c
#define BT_BIP_HDR_TYPE_GET_LINKED_ATTACHMENT "x-bt/img-attachment"
```

相关声明：[BT_BIP_HDR_TYPE_GET_LINKED_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gadcfcdfac4571707f8b8b15fba18c592a)。

用于获取关联附件操作（Get Linked Attachment）的 OBEX 类型报头（Type Header）。

<a id="r_gab4136d9a07d10380590e791adf57069f"></a>

```c
#define BT_BIP_HDR_TYPE_GET_PARTIAL_IMAGE "x-bt/img-partial"
```

相关声明：[BT_BIP_HDR_TYPE_GET_PARTIAL_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gab4136d9a07d10380590e791adf57069f)。

用于获取部分图像操作（Get Partial Image）的 OBEX 类型报头（Type Header）。

<a id="r_gabb3046494704ab9e6959324e459cbc80"></a>

```c
#define BT_BIP_HDR_TYPE_GET_MONITORING_IMAGE "x-bt/img-monitoring"
```

相关声明：[BT_BIP_HDR_TYPE_GET_MONITORING_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gabb3046494704ab9e6959324e459cbc80)。

用于获取监控图像操作（Get Monitoring Image）的 OBEX 类型报头（Type Header）。

<a id="r_ga6c4c9d3b20c7ab5daf5b7cfbc9fcac2f"></a>

```c
#define BT_BIP_HDR_TYPE_GET_STATUS "x-bt/img-status"
```

相关声明：[BT_BIP_HDR_TYPE_GET_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga6c4c9d3b20c7ab5daf5b7cfbc9fcac2f)。

用于获取状态操作（Get Status）的 OBEX 类型报头（Type Header）。

<a id="r_ga667582c6e8641099a13671e406f5fd96"></a>

```c
#define BT_BIP_HDR_TYPE_PUT_IMAGE "x-bt/img-img"
```

相关声明：[BT_BIP_HDR_TYPE_PUT_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga667582c6e8641099a13671e406f5fd96)。

用于放入图像操作（Put Image）的 OBEX 类型报头（Type Header）。

<a id="r_gaf12eff4b680872a4690a0d9c6f873b26"></a>

```c
#define BT_BIP_HDR_TYPE_PUT_LINKED_THUMBNAIL "x-bt/img-thm"
```

相关声明：[BT_BIP_HDR_TYPE_PUT_LINKED_THUMBNAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf12eff4b680872a4690a0d9c6f873b26)。

用于放入关联缩略图操作（Put Linked Thumbnail）的 OBEX 类型报头（Type Header）。

<a id="r_gaf90f12fea45e37a1d59684a578a58bba"></a>

```c
#define BT_BIP_HDR_TYPE_PUT_LINKED_ATTACHMENT "x-bt/img-attachment"
```

相关声明：[BT_BIP_HDR_TYPE_PUT_LINKED_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf90f12fea45e37a1d59684a578a58bba)。

用于放入关联附件操作（Put Linked Attachment）的 OBEX 类型报头（Type Header）。

<a id="r_ga4391371df2040895f16e0eed56e75e57"></a>

```c
#define BT_BIP_HDR_TYPE_REMOTE_DISPLAY "x-bt/img-display"
```

相关声明：[BT_BIP_HDR_TYPE_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga4391371df2040895f16e0eed56e75e57)。

用于远程显示操作（Remote Display）的 OBEX 类型报头（Type Header）。

<a id="r_gae16d011e1a911d2f380bcbe0c648762a"></a>

```c
#define BT_BIP_HDR_TYPE_DELETE_IMAGE "x-bt/img-img"
```

相关声明：[BT_BIP_HDR_TYPE_DELETE_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae16d011e1a911d2f380bcbe0c648762a)。

用于删除图像操作（Delete Image）的 OBEX 类型报头（Type Header）。

<a id="r_gad57d3fcc35a89eeacb4d92e1362a7097"></a>

```c
#define BT_BIP_HDR_TYPE_START_PRINT "x-bt/img-print"
```

相关声明：[BT_BIP_HDR_TYPE_START_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad57d3fcc35a89eeacb4d92e1362a7097)。

用于开始打印操作（Start Print）的 OBEX 类型报头（Type Header）。

<a id="r_gaafe1edaef34603ceffdb08062e721ed8"></a>

```c
#define BT_BIP_HDR_TYPE_START_ARCHIVE "x-bt/img-archive"
```

相关声明：[BT_BIP_HDR_TYPE_START_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaafe1edaef34603ceffdb08062e721ed8)。

用于开始归档操作（Start Archive）的 OBEX 类型报头（Type Header）。

<a id="r_gaabe060f5798f742942d382ed4f06c83d"></a>

```c
#define BT_BIP_HEADER_ID_IMG_DESC 0x71
```

相关声明：[BT_BIP_HEADER_ID_IMG_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaabe060f5798f742942d382ed4f06c83d)。

图像描述符报头 ID（Img-Descriptor Header ID）。

<a id="r_gafb1b58780a45e82c7b1c90a738bddbb9"></a>

```c
#define BT_BIP_HEADER_ID_IMG_HANDLE 0x30
```

相关声明：[BT_BIP_HEADER_ID_IMG_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gafb1b58780a45e82c7b1c90a738bddbb9)。

图像句柄报头 ID（Img-Handle Header ID）。

<a id="r_ga3d5c7f3a6a0a2fe541022c22995d4274"></a>

```c
#define BT_BIP_PRIM_IMAGE_PUSH_CB(_connect, _disconnect, _get_caps, _put_image, _put_linked_thumbnail, _put_linked_attachment)
```

相关声明：[BT_BIP_PRIM_IMAGE_PUSH_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga3d5c7f3a6a0a2fe541022c22995d4274)。

主图像推送服务器回调初始化器（Primary Image Push Server Callback Initializer）。

<a id="r_gada2fa948ead9c05ec300dc3af8722e87"></a>

```c
#define BT_BIP_PRIM_IMAGE_PULL_CB(_connect, _disconnect, _get_caps, _get_image_list, _get_image_properties, _get_image, _get_linked_thumbnail, _get_linked_attachment, _delete_image)
```

相关声明：[BT_BIP_PRIM_IMAGE_PULL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gada2fa948ead9c05ec300dc3af8722e87)。

主图像拉取服务器回调初始化器（Primary Image Pull Server Callback Initializer）。

<a id="r_gaf51de11367b7eeaa0be094d5ad561636"></a>

```c
#define BT_BIP_PRIM_IMAGE_PRINT_CB(_connect, _disconnect, _get_caps, _get_status, _start_print)
```

相关声明：[BT_BIP_PRIM_IMAGE_PRINT_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf51de11367b7eeaa0be094d5ad561636)。

主图像打印服务器回调初始化器（Primary Image Print Server Callback Initializer）。

<a id="r_gae1fd7d679c6e197b2af5557ead4b4a13"></a>

```c
#define BT_BIP_2ND_IMAGE_PRINT_CB(_connect, _disconnect, _get_partial_image)
```

相关声明：[BT_BIP_2ND_IMAGE_PRINT_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae1fd7d679c6e197b2af5557ead4b4a13)。

次级图像打印服务器回调初始化器（Secondary Image Print Server Callback Initializer）。

<a id="r_ga445d8c170b5c805d86604f4d474ad0e8"></a>

```c
#define BT_BIP_PRIM_AUTO_ARCHIVE_CB(_connect, _disconnect, _get_status, _start_archive)
```

相关声明：[BT_BIP_PRIM_AUTO_ARCHIVE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga445d8c170b5c805d86604f4d474ad0e8)。

主自动归档服务器回调初始化器（Primary Auto Archive Server Callback Initializer）。

<a id="r_ga2a719b3a6266dd6ce5827be47467ff14"></a>

```c
#define BT_BIP_2ND_AUTO_ARCHIVE_CB(_connect, _disconnect, _get_caps, _get_image_list, _get_image_properties, _get_image, _get_linked_thumbnail, _get_linked_attachment, _delete_image)
```

相关声明：[BT_BIP_2ND_AUTO_ARCHIVE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga2a719b3a6266dd6ce5827be47467ff14)。

次级自动归档服务器回调初始化器（Secondary Auto Archive Server Callback Initializer）。

<a id="r_ga144e0d9835516f2e9390d1c966ede6bd"></a>

```c
#define BT_BIP_PRIM_REMOTE_CAMERA_CB(_connect, _disconnect, _get_image_properties, _get_image, _get_linked_thumbnail, _get_monitoring_image)
```

相关声明：[BT_BIP_PRIM_REMOTE_CAMERA_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga144e0d9835516f2e9390d1c966ede6bd)。

主远程相机服务器回调初始化器（Primary Remote Camera Server Callback Initializer）。

<a id="r_gabf52b29d7e2f727d9f14e8b53bcc3f4f"></a>

```c
#define BT_BIP_PRIM_REMOTE_DISPLAY_CB(_connect, _disconnect, _get_caps, _get_image_list, _put_image, _put_linked_thumbnail, _remote_display)
```

相关声明：[BT_BIP_PRIM_REMOTE_DISPLAY_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gabf52b29d7e2f727d9f14e8b53bcc3f4f)。

主远程显示服务器回调初始化器（Primary Remote Display Server Callback Initializer）。

<a id="r_gaca571268fd723b69d19ef7cd97db1da3"></a>

```c
#define BT_BIP_UUID_IMAGE_PUSH
```

相关声明：[BT_BIP_UUID_IMAGE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaca571268fd723b69d19ef7cd97db1da3)。

基本成像配置文件（BIP）的图像推送服务（Image Push Service）的 UUID。

<a id="r_ga42116d3c159adecc6d63c32f0a1c4672"></a>

```c
#define BT_BIP_UUID_IMAGE_PULL
```

相关声明：[BT_BIP_UUID_IMAGE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga42116d3c159adecc6d63c32f0a1c4672)。

基本成像配置文件（BIP）的图像拉取服务（Image Pull Service）的 UUID。

<a id="r_gaa4b44603eb57cbc223d94a8723abf06a"></a>

```c
#define BT_BIP_UUID_IMAGE_PRINT
```

相关声明：[BT_BIP_UUID_IMAGE_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaa4b44603eb57cbc223d94a8723abf06a)。

基本成像配置文件（BIP）的高级图像打印服务（Advanced Image Printing Service）的 UUID。

<a id="r_ga098a435c80d373158ade3dc15dd538e6"></a>

```c
#define BT_BIP_UUID_AUTO_ARCHIVE
```

相关声明：[BT_BIP_UUID_AUTO_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga098a435c80d373158ade3dc15dd538e6)。

基本成像配置文件（BIP）的自动归档服务（Auto Archive Service）的 UUID。

<a id="r_ga305af9409b4cfa25a16bed28cd305175"></a>

```c
#define BT_BIP_UUID_REMOTE_CAMERA
```

相关声明：[BT_BIP_UUID_REMOTE_CAMERA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga305af9409b4cfa25a16bed28cd305175)。

基本成像配置文件（BIP）的远程相机服务（Remote Camera Service）的 UUID。

<a id="r_gaa8b43801cd1bf8a4d2c51b0d25a408fc"></a>

```c
#define BT_BIP_UUID_REMOTE_DISPLAY
```

相关声明：[BT_BIP_UUID_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaa8b43801cd1bf8a4d2c51b0d25a408fc)。

基本成像配置文件（BIP）的远程显示服务（Remote Display Service）的 UUID。

<a id="r_ga8ef9620a71471340492feb1c8a820b5d"></a>

```c
#define BT_BIP_UUID_REFERENCED_OBJ
```

相关声明：[BT_BIP_UUID_REFERENCED_OBJ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga8ef9620a71471340492feb1c8a820b5d)。

基本成像配置文件（BIP）的引用对象服务（Referenced Objects Service）的 UUID。

<a id="r_gae305dd59c79605feebffc3c91e641e67"></a>

```c
#define BT_BIP_UUID_ARCHIVED_OBJ
```

相关声明：[BT_BIP_UUID_ARCHIVED_OBJ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae305dd59c79605feebffc3c91e641e67)。

基本成像配置文件（BIP）的已归档对象服务（Archived Objects Service）的 UUID。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.3\_枚举（Enumerations）

<a id="r_ga34de6d20263274292543a7a8afbd2c6b"></a>

```c
enum bt_bip_appl_param_tag_id { BT_BIP_APPL_PARAM_TAG_ID_RETURNED_HANDLES = 0x01 , BT_BIP_APPL_PARAM_TAG_ID_LIST_START_OFFSET = 0x02 , BT_BIP_APPL_PARAM_TAG_ID_LATEST_CAPTURED_IMAGES = 0x03 , BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_LEN = 0x04 , BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_START_OFFSET = 0x05 , BT_BIP_APPL_PARAM_TAG_ID_TOTAL_FILE_SIZE = 0x06 , BT_BIP_APPL_PARAM_TAG_ID_END_FLAG = 0x07 , BT_BIP_APPL_PARAM_TAG_ID_REMOTE_DISPLAY = 0x08 , BT_BIP_APPL_PARAM_TAG_ID_SERVICE_ID = 0x09 , BT_BIP_APPL_PARAM_TAG_ID_STORE_FLAG = 0x0a }
```

相关声明：[bt_bip_appl_param_tag_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga34de6d20263274292543a7a8afbd2c6b)、[BT_BIP_APPL_PARAM_TAG_ID_RETURNED_HANDLES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6bace4966644e9194273b635b916eac0871)、[BT_BIP_APPL_PARAM_TAG_ID_LIST_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba0f0d78c2da3d8f3d0caf015525b3e010)、[BT_BIP_APPL_PARAM_TAG_ID_LATEST_CAPTURED_IMAGES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba9dbbb8ed95c7ccd86a74263fef1a1e92)、[BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6bad6511bb04da2cf325a39bfee93f51e0c)、[BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba0ff60914fb36e587b42a473c25bd6a2d)、[BT_BIP_APPL_PARAM_TAG_ID_TOTAL_FILE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba2565f26c0322935acef85725ac8982e5)、[BT_BIP_APPL_PARAM_TAG_ID_END_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6baa7b18ee3ae56c0f0e84a103c1e59f05d)、[BT_BIP_APPL_PARAM_TAG_ID_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6bab0e2dfb17de25f4ec3b27b29c2659afa)、[BT_BIP_APPL_PARAM_TAG_ID_SERVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba683d101ea1babf1f147d1869ab7424f4)、[BT_BIP_APPL_PARAM_TAG_ID_STORE_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6baef58e631bfd6c511318c386308374274)。

基本成像配置文件（BIP）的应用参数标记 ID（Application Parameter Tag IDs）。

<a id="r_gaff38654d69104bebaaf5884283e197ef"></a>

```c
enum bt_bip_conn_type { BT_BIP_PRIM_CONN_TYPE_IMAGE_PUSH = 0 , BT_BIP_PRIM_CONN_TYPE_IMAGE_PULL = 1 , BT_BIP_PRIM_CONN_TYPE_ADVANCED_IMAGE_PRINTING = 2 , BT_BIP_PRIM_CONN_TYPE_AUTO_ARCHIVE = 3 , BT_BIP_PRIM_CONN_TYPE_REMOTE_CAMERA = 4 , BT_BIP_PRIM_CONN_TYPE_REMOTE_DISPLAY = 5 , BT_BIP_2ND_CONN_TYPE_REFERENCED_OBJECTS = 10 , BT_BIP_2ND_CONN_TYPE_ARCHIVED_OBJECTS = 11 }
```

相关声明：[bt_bip_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaff38654d69104bebaaf5884283e197ef)、[BT_BIP_PRIM_CONN_TYPE_IMAGE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa612cd818200f49e37235917fead216d2)、[BT_BIP_PRIM_CONN_TYPE_IMAGE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa05372dbd0a01855f0863ce355a503c61)、[BT_BIP_PRIM_CONN_TYPE_ADVANCED_IMAGE_PRINTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa05de3a972070aa4d1e29851479860d9f)、[BT_BIP_PRIM_CONN_TYPE_AUTO_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efaf762949693b7cf70739ed0a0eb6a9d58)、[BT_BIP_PRIM_CONN_TYPE_REMOTE_CAMERA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa8b576c667b9c6458e44ec67674bdffbd)、[BT_BIP_PRIM_CONN_TYPE_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa12873fc1888cd99703131ae71134f0c7)、[BT_BIP_2ND_CONN_TYPE_REFERENCED_OBJECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa4d5ab575c877aa2a43c29cbb52a361c7)、[BT_BIP_2ND_CONN_TYPE_ARCHIVED_OBJECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efabe15f984d6907bdb40c10e893e1c3bf6)。

BIP 的 OBEX 连接类型（Connection Types）。

<a id="r_ga30d9309cbbd88b54508551285b21e575"></a>

```c
enum bt_bip_role { BT_BIP_ROLE_UNKNOWN = 0 , BT_BIP_ROLE_INITIATOR = 1 , BT_BIP_ROLE_RESPONDER = 2 }
```

相关声明：[bt_bip_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga30d9309cbbd88b54508551285b21e575)、[BT_BIP_ROLE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga30d9309cbbd88b54508551285b21e575aaa7de8d668d248049c5d5c75ae35d74b)、[BT_BIP_ROLE_INITIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga30d9309cbbd88b54508551285b21e575aa5cdb11f2b0ac9c20c380dd48c9edaa5)、[BT_BIP_ROLE_RESPONDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga30d9309cbbd88b54508551285b21e575a87d1fe99824b216780435898c2dfa968)。

BIP 角色类型（Role Types）。

<a id="r_ga7b3c6cb1159e7b2ede57c66f20b23827"></a>

```c
enum bt_bip_transport_state { BT_BIP_TRANSPORT_STATE_DISCONNECTED = 0 , BT_BIP_TRANSPORT_STATE_CONNECTING = 1 , BT_BIP_TRANSPORT_STATE_CONNECTED = 2 , BT_BIP_TRANSPORT_STATE_DISCONNECTING = 3 }
```

相关声明：[bt_bip_transport_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga7b3c6cb1159e7b2ede57c66f20b23827)、[BT_BIP_TRANSPORT_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827ae78c865c0034d405391aaf9f72e4c9b2)、[BT_BIP_TRANSPORT_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827ad4444da19b4e0f499867ea967dfc578f)、[BT_BIP_TRANSPORT_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827a1af8a1481b10b53c58af8e36c7b91588)、[BT_BIP_TRANSPORT_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827a7340b2e209c71d9f944b303c22cb264d)。

BIP 传输状态（Transport State）。

<a id="r_gad062c0f3d2feeb92a866f0fe91a6f231"></a>

```c
enum bt_bip_supported_capabilities { BT_BIP_SUPP_CAP_GENERIC_IMAGE = 0 , BT_BIP_SUPP_CAP_CAPTURING = 1 , BT_BIP_SUPP_CAP_PRINTING = 2 , BT_BIP_SUPP_CAP_DISPLAYING = 3 }
```

相关声明：[bt_bip_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad062c0f3d2feeb92a866f0fe91a6f231)、[BT_BIP_SUPP_CAP_GENERIC_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231a786ef1ad1bde68f9b026c9d080cc41d4)、[BT_BIP_SUPP_CAP_CAPTURING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231ac9c5d73b0d2d5eb25a962fa72ede6d5a)、[BT_BIP_SUPP_CAP_PRINTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231a4a738d195dcf0908a64bdd246672d4bb)、[BT_BIP_SUPP_CAP_DISPLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231a324c0590cefb5d7a39f90d90e3466334)。

BIP 支持的能力（Supported Capabilities）。

<a id="r_gacfc8aaea3d27e3a42a14c49b880a5b90"></a>

```c
enum bt_bip_supported_features { BT_BIP_SUPP_FEAT_IMAGE_PUSH = 0 , BT_BIP_SUPP_FEAT_IMAGE_PUSH_STORE = 1 , BT_BIP_SUPP_FEAT_IMAGE_PUSH_PRINT = 2 , BT_BIP_SUPP_FEAT_IMAGE_PUSH_DISPLAY = 3 , BT_BIP_SUPP_FEAT_IMAGE_PULL = 4 , BT_BIP_SUPP_FEAT_ADVANCED_IMAGE_PRINT = 5 , BT_BIP_SUPP_FEAT_AUTO_ARCHIVE = 6 , BT_BIP_SUPP_FEAT_REMOTE_CAMERA = 7 , BT_BIP_SUPP_FEAT_REMOTE_DISPLAY = 8 }
```

相关声明：[bt_bip_supported_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gacfc8aaea3d27e3a42a14c49b880a5b90)、[BT_BIP_SUPP_FEAT_IMAGE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90ac14657fd4af96f4c837916b832c25a0f)、[BT_BIP_SUPP_FEAT_IMAGE_PUSH_STORE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a8904b7b8288e1b47d2242f5d686e32d9)、[BT_BIP_SUPP_FEAT_IMAGE_PUSH_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90add6c2e70541aae8124bad4b102d64b88)、[BT_BIP_SUPP_FEAT_IMAGE_PUSH_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a49668a596059e535bd59ac095dffa050)、[BT_BIP_SUPP_FEAT_IMAGE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90aba576edd916dbf49118e78572f70320b)、[BT_BIP_SUPP_FEAT_ADVANCED_IMAGE_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90ac64d953311bc9b76bfe75dd3133f5563)、[BT_BIP_SUPP_FEAT_AUTO_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90af72e05ca427f8c5091e50cddac522045)、[BT_BIP_SUPP_FEAT_REMOTE_CAMERA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a97141e2764fad3714c03b6be69ff2a9a)、[BT_BIP_SUPP_FEAT_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a132dd77e79fbfda8a78d5034d4c618c5)。

BIP 支持的特性（Supported Features）。

<a id="r_ga6768e59b79bb67b5d385fdaa3dfb8888"></a>

```c
enum bt_bip_supported_functions { BT_BIP_SUPP_FUNC_GET_CAPS = 0 , BT_BIP_SUPP_FUNC_PUT_IMAGE = 1 , BT_BIP_SUPP_FUNC_PUT_LINKED_ATTACHMENT = 2 , BT_BIP_SUPP_FUNC_PUT_LINKED_THUMBNAIL = 3 , BT_BIP_SUPP_FUNC_REMOTE_DISPLAY = 4 , BT_BIP_SUPP_FUNC_GET_IMAGE_LIST = 5 , BT_BIP_SUPP_FUNC_GET_IMAGE_PROPERTIES = 6 , BT_BIP_SUPP_FUNC_GET_IMAGE = 7 , BT_BIP_SUPP_FUNC_GET_LINKED_THUMBNAIL = 8 , BT_BIP_SUPP_FUNC_GET_LINKED_ATTACHMENT = 9 , BT_BIP_SUPP_FUNC_DELETE_IMAGE = 10 , BT_BIP_SUPP_FUNC_START_PRINT = 11 , BT_BIP_SUPP_FUNC_GET_PARTIAL_IMAGE = 12 , BT_BIP_SUPP_FUNC_START_ARCHIVE = 13 , BT_BIP_SUPP_FUNC_GET_MONITORING_IMAGE = 14 , BT_BIP_SUPP_FUNC_GET_STATUS = 16 }
```

相关声明：[bt_bip_supported_functions](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga6768e59b79bb67b5d385fdaa3dfb8888)、[BT_BIP_SUPP_FUNC_GET_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a2e1f3364145560587963402881bb2705)、[BT_BIP_SUPP_FUNC_PUT_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888afb1777cefdbd00e3432ddf5180804f48)、[BT_BIP_SUPP_FUNC_PUT_LINKED_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a8a417f3073f017af866877f88ee10228)、[BT_BIP_SUPP_FUNC_PUT_LINKED_THUMBNAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a0ee047481a35e26fa0d03bf7594d7752)、[BT_BIP_SUPP_FUNC_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888adb0e03118b1cd62fe7e97b53e9f52d41)、[BT_BIP_SUPP_FUNC_GET_IMAGE_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a7843f4dece6ff449b97ba0a2c7298b90)、[BT_BIP_SUPP_FUNC_GET_IMAGE_PROPERTIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888af29095b3b5964062e98b9e357de87f89)、[BT_BIP_SUPP_FUNC_GET_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a50271c1bac792020f0fb869bb523e506)、[BT_BIP_SUPP_FUNC_GET_LINKED_THUMBNAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a03c928dd502a98b72cb7d8eebad4b384)、[BT_BIP_SUPP_FUNC_GET_LINKED_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888ac3ec252a63d494ce3e4dd696d05d94bc)、[BT_BIP_SUPP_FUNC_DELETE_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a045dfb07426eacb16fd69247eecf70b1)、[BT_BIP_SUPP_FUNC_START_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888ae1312bb3417f901204ac592e4b9376df)、[BT_BIP_SUPP_FUNC_GET_PARTIAL_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888ae1e97efb19d10ac2b508a9e65b5c43ce)、[BT_BIP_SUPP_FUNC_START_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a3cae66cb380311938f83bb099a2d02da)、[BT_BIP_SUPP_FUNC_GET_MONITORING_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a0bde5efd58b339e53db3779a159239c1)、[BT_BIP_SUPP_FUNC_GET_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888abf825fb7d634906f0204780ef81ca5b3)。

BIP 支持的功能（Supported Functions）。

<a id="r_gae4d1ed3b7e27768c1dbb6ce448cb5cf9"></a>

```c
enum bt_bip_state { BT_BIP_STATE_DISCONNECTED = 0 , BT_BIP_STATE_CONNECTING = 1 , BT_BIP_STATE_CONNECTED = 2 , BT_BIP_STATE_DISCONNECTING = 3 }
```

相关声明：[bt_bip_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae4d1ed3b7e27768c1dbb6ce448cb5cf9)、[BT_BIP_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a984245e44981ad3d85518ab1c3f576e8)、[BT_BIP_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9acdc7fe9ee4c0d0ba447bc43817364478)、[BT_BIP_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9ae65c7b972effa225116ec8abfcf07bc3)、[BT_BIP_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a96f12788ce6f56012ac4b1c25f63f67e)。

BIP 连接状态（Connection State）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_ga644ca479c156b10d920d87d862401fc7"></a>

```c
int bt_bip_rfcomm_register (struct bt_bip_rfcomm_server *server)
```

相关声明：[bt_bip_rfcomm_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga644ca479c156b10d920d87d862401fc7)、[bt_bip_rfcomm_server](../bluetooth_service_model_reference/P005_bt_bip_rfcomm_server_结构体.md)。

注册 BIP RFCOMM 服务器（Server）。

<a id="r_ga5ed2a46482e4fe60ef23c540001b58a3"></a>

```c
int bt_bip_rfcomm_connect (struct bt_conn *conn, struct bt_bip *bip, uint8_t channel)
```

相关声明：[bt_bip_rfcomm_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5ed2a46482e4fe60ef23c540001b58a3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 RFCOMM 创建传输连接（Transport Connection）。

<a id="r_ga66a86a399f73dba932dc05d63b3749bd"></a>

```c
int bt_bip_rfcomm_disconnect (struct bt_bip *bip)
```

相关声明：[bt_bip_rfcomm_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga66a86a399f73dba932dc05d63b3749bd)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)。

断开 BIP RFCOMM 连接（Connection）。

<a id="r_gaffb77f6c80ba05046df03d62baad211b"></a>

```c
int bt_bip_l2cap_register (struct bt_bip_l2cap_server *server)
```

相关声明：[bt_bip_l2cap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaffb77f6c80ba05046df03d62baad211b)、[bt_bip_l2cap_server](../bluetooth_service_model_reference/P004_bt_bip_l2cap_server_结构体.md)。

注册 BIP L2CAP 服务器（Server）。

<a id="r_gaf54b07acf22c5231b2de0fdeca7807c2"></a>

```c
int bt_bip_l2cap_connect (struct bt_conn *conn, struct bt_bip *bip, uint16_t psm)
```

相关声明：[bt_bip_l2cap_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf54b07acf22c5231b2de0fdeca7807c2)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 L2CAP 创建传输连接（Transport Connection）。

<a id="r_ga1fda174189b57c54f365784d1909152e"></a>

```c
int bt_bip_l2cap_disconnect (struct bt_bip *bip)
```

相关声明：[bt_bip_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga1fda174189b57c54f365784d1909152e)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)。

断开 BIP L2CAP 连接（Connection）。

<a id="r_ga0180461f24c6f741e056d64f9758b89e"></a>

```c
int bt_bip_set_supported_capabilities (struct bt_bip *bip, uint8_t capabilities)
```

相关声明：[bt_bip_set_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga0180461f24c6f741e056d64f9758b89e)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 BIP 响应方（Responder）支持的能力（Capabilities）。

<a id="r_gab5a80d7a992d0afa0270eb09d6f3275c"></a>

```c
int bt_bip_set_supported_features (struct bt_bip *bip, uint16_t features)
```

相关声明：[bt_bip_set_supported_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gab5a80d7a992d0afa0270eb09d6f3275c)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 BIP 响应方（Responder）支持的特性（Features）。

<a id="r_gafe7df6ee236da3a11104f1aa6e948bfe"></a>

```c
int bt_bip_set_supported_functions (struct bt_bip *bip, uint32_t functions)
```

相关声明：[bt_bip_set_supported_functions](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gafe7df6ee236da3a11104f1aa6e948bfe)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置 BIP 响应方（Responder）支持的功能（Functions）。

<a id="r_ga45f1ca2d2874500d6f8df3a62b01260e"></a>

```c
int bt_bip_primary_server_register (struct bt_bip *bip, struct bt_bip_server *server, enum bt_bip_conn_type type, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga45f1ca2d2874500d6f8df3a62b01260e)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_bip_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaff38654d69104bebaaf5884283e197ef)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主 BIP OBEX 服务器（Primary Server）。

<a id="r_gab0a3b58b041ac4af2682fb96b8f00a7e"></a>

```c
int bt_bip_secondary_server_register (struct bt_bip *bip, struct bt_bip_server *server, enum bt_bip_conn_type type, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb, struct bt_bip_client *primary_client)
```

相关声明：[bt_bip_secondary_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gab0a3b58b041ac4af2682fb96b8f00a7e)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_bip_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaff38654d69104bebaaf5884283e197ef)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)。

注册次级 BIP OBEX 服务器（Secondary Server）。

<a id="r_gaefd318b5dc2e813eea2cd7608be1170c"></a>

```c
static int bt_bip_primary_image_push_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_image_push_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaefd318b5dc2e813eea2cd7608be1170c)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主图像推送 OBEX 服务器（Primary Image Push OBEX server）。

<a id="r_ga35c44217cbfcd8661c3f2e5725be9323"></a>

```c
static int bt_bip_primary_image_pull_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_image_pull_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga35c44217cbfcd8661c3f2e5725be9323)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主图像拉取 OBEX 服务器（Primary Image Pull OBEX server）。

<a id="r_gae8b37b224ea419ca1f1761d98a34cb2d"></a>

```c
static int bt_bip_primary_advanced_image_printing_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_advanced_image_printing_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae8b37b224ea419ca1f1761d98a34cb2d)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主高级图像打印 OBEX 服务器（Primary Advanced Image Printing OBEX server）。

<a id="r_ga3848d86378912fbd9c896b14aed74161"></a>

```c
static int bt_bip_primary_auto_archive_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_auto_archive_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga3848d86378912fbd9c896b14aed74161)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主自动归档 OBEX 服务器（Primary Auto Archive OBEX server）。

<a id="r_ga4b236a8a28c359e392633d472a508405"></a>

```c
static int bt_bip_primary_remote_camera_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_remote_camera_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga4b236a8a28c359e392633d472a508405)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主远程相机 OBEX 服务器（Primary Remote Camera OBEX server）。

<a id="r_ga5167b2dab89a983fae9fca356e6fbcf9"></a>

```c
static int bt_bip_primary_remote_display_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb)
```

相关声明：[bt_bip_primary_remote_display_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5167b2dab89a983fae9fca356e6fbcf9)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)。

注册主远程显示 OBEX 服务器（Primary Remote Display OBEX server）。

<a id="r_ga54c37cced33fa72a2c6cea10e2996e6d"></a>

```c
static int bt_bip_secondary_advanced_image_printing_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb, struct bt_bip_client *primary_client)
```

相关声明：[bt_bip_secondary_advanced_image_printing_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga54c37cced33fa72a2c6cea10e2996e6d)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)。

注册次级高级图像打印 OBEX 服务器（Secondary Advanced Image Printing OBEX server）。

<a id="r_gab24c4f7144f8c43dcf1b82a4c33e4ffd"></a>

```c
static int bt_bip_secondary_auto_archive_server_register (struct bt_bip *bip, struct bt_bip_server *server, const struct bt_uuid_128 *uuid, struct bt_bip_server_cb *cb, struct bt_bip_client *primary_client)
```

相关声明：[bt_bip_secondary_auto_archive_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gab24c4f7144f8c43dcf1b82a4c33e4ffd)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)。

注册次级自动归档 OBEX 服务器（Secondary Auto Archive OBEX server）。

<a id="r_ga4e06b2fb9a99f89d7e65e8a52690442d"></a>

```c
int bt_bip_server_unregister (struct bt_bip_server *server)
```

相关声明：[bt_bip_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga4e06b2fb9a99f89d7e65e8a52690442d)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)。

注销 BIP OBEX 服务器（Server）。

<a id="r_gad32c1b1118b606ab3ae0d9db889cbab9"></a>

```c
int bt_bip_primary_client_connect (struct bt_bip *bip, struct bt_bip_client *client, enum bt_bip_conn_type type, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad32c1b1118b606ab3ae0d9db889cbab9)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaff38654d69104bebaaf5884283e197ef)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主 BIP OBEX 客户端（Primary Client）。

<a id="r_gae557b198b9d5606ee05cd29ed16f9482"></a>

```c
int bt_bip_secondary_client_connect (struct bt_bip *bip, struct bt_bip_client *client, enum bt_bip_conn_type type, struct bt_bip_client_cb *cb, struct net_buf *buf, struct bt_bip_server *primary_server)
```

相关声明：[bt_bip_secondary_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae557b198b9d5606ee05cd29ed16f9482)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaff38654d69104bebaaf5884283e197ef)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)。

连接次级 BIP OBEX 客户端（Secondary Client）。

<a id="r_ga39ec2019f86d42b02992b0a9d3ba094c"></a>

```c
static int bt_bip_primary_image_push_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_image_push_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga39ec2019f86d42b02992b0a9d3ba094c)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主图像推送 OBEX 客户端（Primary Image Push OBEX client）。

<a id="r_ga2d4919c1eb568f33a89d8b176f103601"></a>

```c
static int bt_bip_primary_image_pull_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_image_pull_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga2d4919c1eb568f33a89d8b176f103601)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主图像拉取 OBEX 客户端（Primary Image Pull OBEX client）。

<a id="r_ga9352b8309334a3fe89d77f5714443376"></a>

```c
static int bt_bip_primary_advanced_image_printing_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_advanced_image_printing_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9352b8309334a3fe89d77f5714443376)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主高级图像打印 OBEX 客户端（Primary Advanced Image Printing OBEX client）。

<a id="r_ga98dca7b222c8a09b1c44861c9060193b"></a>

```c
static int bt_bip_primary_auto_archive_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_auto_archive_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga98dca7b222c8a09b1c44861c9060193b)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主自动归档 OBEX 客户端（Primary Auto Archive OBEX client）。

<a id="r_ga30e3a6ad8c00c230ac3591a934cfb81f"></a>

```c
static int bt_bip_primary_remote_camera_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_remote_camera_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga30e3a6ad8c00c230ac3591a934cfb81f)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主远程相机 OBEX 客户端（Primary Remote Camera OBEX client）。

<a id="r_gac4ba5cef40cd451bd4b505dbea0fa135"></a>

```c
static int bt_bip_primary_remote_display_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf)
```

相关声明：[bt_bip_primary_remote_display_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gac4ba5cef40cd451bd4b505dbea0fa135)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

连接主远程显示 OBEX 客户端（Primary Remote Display OBEX client）。

<a id="r_ga72ef6cd266b7e57e1c80b6d8eba799e2"></a>

```c
static int bt_bip_secondary_advanced_image_printing_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf, struct bt_bip_server *primary_server)
```

相关声明：[bt_bip_secondary_advanced_image_printing_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga72ef6cd266b7e57e1c80b6d8eba799e2)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)。

连接次级高级图像打印 OBEX 客户端（Secondary Advanced Image Printing OBEX client）。

<a id="r_ga1975916aa3da40576499f6d05aac1285"></a>

```c
static int bt_bip_secondary_auto_archive_client_connect (struct bt_bip *bip, struct bt_bip_client *client, struct bt_bip_client_cb *cb, struct net_buf *buf, struct bt_bip_server *primary_server)
```

相关声明：[bt_bip_secondary_auto_archive_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga1975916aa3da40576499f6d05aac1285)、[bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)。

连接次级自动归档 OBEX 客户端（Secondary Auto Archive OBEX client）。

<a id="r_ga0987a342b43bdd1926f3730f471ca05f"></a>

```c
int bt_bip_connect_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_connect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga0987a342b43bdd1926f3730f471ca05f)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送OBEX连接响应（OBEX Connect response）。

<a id="r_gaafcd6a3503795299b6fb777ba0aa0cff"></a>

```c
int bt_bip_disconnect (struct bt_bip_client *client, struct net_buf *buf)
```

相关声明：[bt_bip_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaafcd6a3503795299b6fb777ba0aa0cff)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送OBEX断开连接请求（OBEX Disconnect request）。

<a id="r_gaddfcee2eaea19b4819d83cf6ecb396da"></a>

```c
int bt_bip_disconnect_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_disconnect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaddfcee2eaea19b4819d83cf6ecb396da)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送OBEX断开连接响应（OBEX Disconnect response）。

<a id="r_gaa0f071c8c83a54b2d48f478594579719"></a>

```c
int bt_bip_abort (struct bt_bip_client *client, struct net_buf *buf)
```

相关声明：[bt_bip_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaa0f071c8c83a54b2d48f478594579719)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送OBEX中止请求（OBEX Abort request）。

<a id="r_ga1c341ad182ff418286b64b4eff491445"></a>

```c
int bt_bip_abort_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_abort_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga1c341ad182ff418286b64b4eff491445)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送OBEX中止响应（OBEX Abort response）。

<a id="r_gafcd2d4e6a8ad906c9692313421175431"></a>

```c
int bt_bip_get_capabilities (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gafcd2d4e6a8ad906c9692313421175431)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取能力请求（Get Capabilities request）。

<a id="r_gaea5d5f5b6c29a44ae89939ee3e2d6efb"></a>

```c
int bt_bip_get_capabilities_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_capabilities_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaea5d5f5b6c29a44ae89939ee3e2d6efb)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取能力响应（Get Capabilities response）。

<a id="r_ga9542e030ea863b4379d36fa21de262dc"></a>

```c
int bt_bip_get_image_list (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_image_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9542e030ea863b4379d36fa21de262dc)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像列表请求（Get Image List request）。

<a id="r_ga6e33bba952a9693d1fed7ee9bdf03df8"></a>

```c
int bt_bip_get_image_list_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_image_list_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga6e33bba952a9693d1fed7ee9bdf03df8)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像列表响应（Get Image List response）。

<a id="r_ga17ae73bd6088b44206378afe3b0b9eb0"></a>

```c
int bt_bip_get_image_properties (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_image_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga17ae73bd6088b44206378afe3b0b9eb0)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像属性请求（Get Image Properties request）。

<a id="r_ga9a91c35e91a0c30eab55da5b842427d9"></a>

```c
int bt_bip_get_image_properties_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_image_properties_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9a91c35e91a0c30eab55da5b842427d9)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像属性响应（Get Image Properties response）。

<a id="r_ga79831fc5fff332a891e6b9ff71f81d20"></a>

```c
int bt_bip_get_image (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga79831fc5fff332a891e6b9ff71f81d20)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像请求（Get Image request）。

<a id="r_ga53fb15ff7d0728b09f1c4e8d2ceb6dee"></a>

```c
int bt_bip_get_image_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga53fb15ff7d0728b09f1c4e8d2ceb6dee)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像响应（Get Image response）。

<a id="r_gad9c05d28e1e2124675b5906990c3408c"></a>

```c
int bt_bip_get_linked_thumbnail (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_linked_thumbnail](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad9c05d28e1e2124675b5906990c3408c)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取关联缩略图请求（Get Linked Thumbnail request）。

<a id="r_ga5c3cd3e39fc21a584d6955a160ca126a"></a>

```c
int bt_bip_get_linked_thumbnail_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_linked_thumbnail_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5c3cd3e39fc21a584d6955a160ca126a)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取关联缩略图响应（Get Linked Thumbnail response）。

<a id="r_gad95944f07cd9f7b6bb9c81f21fffd447"></a>

```c
int bt_bip_get_linked_attachment (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_linked_attachment](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad95944f07cd9f7b6bb9c81f21fffd447)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取关联附件请求（Get Linked Attachment request）。

<a id="r_ga70bf0d46bd16d0207e13eeb9a7844f1c"></a>

```c
int bt_bip_get_linked_attachment_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_linked_attachment_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga70bf0d46bd16d0207e13eeb9a7844f1c)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取关联附件响应（Get Linked Attachment response）。

<a id="r_ga2b6a2a51fb00e7060e196051f8aea4c4"></a>

```c
int bt_bip_get_partial_image (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_partial_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga2b6a2a51fb00e7060e196051f8aea4c4)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取部分图像请求（Get Partial Image request）。

<a id="r_gadf624e05a6d008bdcfd8a61ae6341f42"></a>

```c
int bt_bip_get_partial_image_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_partial_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gadf624e05a6d008bdcfd8a61ae6341f42)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取部分图像响应（Get Partial Image response）。

<a id="r_ga9f1593748ffcf29015533d52266a8e19"></a>

```c
int bt_bip_get_monitoring_image (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_monitoring_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9f1593748ffcf29015533d52266a8e19)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取监控图像请求（Get Monitoring Image request）。

<a id="r_ga301ff6e5a1e8775295659442b8c20e15"></a>

```c
int bt_bip_get_monitoring_image_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_monitoring_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga301ff6e5a1e8775295659442b8c20e15)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取监控图像响应（Get Monitoring Image response）。

<a id="r_ga578c2b59fbc8afee530168452eb221fb"></a>

```c
int bt_bip_get_status (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga578c2b59fbc8afee530168452eb221fb)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取状态请求（Get Status request）。

<a id="r_ga7abdde3a7e5dcda9c6187b5e45b75cc2"></a>

```c
int bt_bip_get_status_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_get_status_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga7abdde3a7e5dcda9c6187b5e45b75cc2)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取状态响应（Get Status response）。

<a id="r_gaf551904672eda53e9dfcbb5a6bf4c2c3"></a>

```c
int bt_bip_put_image (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_put_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf551904672eda53e9dfcbb5a6bf4c2c3)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入图像请求（Put Image request）。

<a id="r_ga002f7713a8269c0b00a415bbb8c53fce"></a>

```c
int bt_bip_put_image_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_put_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga002f7713a8269c0b00a415bbb8c53fce)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入图像响应（Put Image response）。

<a id="r_ga8b730495f4dd4e6f8db85c5b060a3cae"></a>

```c
int bt_bip_put_linked_thumbnail (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_put_linked_thumbnail](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga8b730495f4dd4e6f8db85c5b060a3cae)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入关联缩略图请求（Put Linked Thumbnail request）。

<a id="r_gac96e873a840b072f5213b7483d633aaa"></a>

```c
int bt_bip_put_linked_thumbnail_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_put_linked_thumbnail_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gac96e873a840b072f5213b7483d633aaa)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入关联缩略图响应（Put Linked Thumbnail response）。

<a id="r_ga86085e98964dcfd19725b5d96f38a99b"></a>

```c
int bt_bip_put_linked_attachment (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_put_linked_attachment](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga86085e98964dcfd19725b5d96f38a99b)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入关联附件请求（Put Linked Attachment request）。

<a id="r_gad6a7df2b0c49c0df616ef170c7b9e431"></a>

```c
int bt_bip_put_linked_attachment_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_put_linked_attachment_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad6a7df2b0c49c0df616ef170c7b9e431)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送放入关联附件响应（Put Linked Attachment response）。

<a id="r_ga021a5d82b292d04cd0e2d53b1b32344b"></a>

```c
int bt_bip_remote_display (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_remote_display](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga021a5d82b292d04cd0e2d53b1b32344b)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送远程显示请求（Remote Display request）。

<a id="r_ga0c54da02bc8dda26794f398e06e66cb3"></a>

```c
int bt_bip_remote_display_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_remote_display_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga0c54da02bc8dda26794f398e06e66cb3)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送远程显示响应（Remote Display response）。

<a id="r_ga5302af5beb7cd5c98a9cbdc288f09d3c"></a>

```c
int bt_bip_delete_image (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_delete_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5302af5beb7cd5c98a9cbdc288f09d3c)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送删除图像请求（Delete Image request）。

<a id="r_gad53a7666b90a97034276fe341c2bd7a2"></a>

```c
int bt_bip_delete_image_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_delete_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad53a7666b90a97034276fe341c2bd7a2)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送删除图像响应（Delete Image response）。

<a id="r_ga8a948dcee431ced321e7b5d51c8d5f9c"></a>

```c
int bt_bip_start_print (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_start_print](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga8a948dcee431ced321e7b5d51c8d5f9c)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送开始打印请求（Start Print request）。

<a id="r_gae9ea9f936aa75b287a2152a747fd687a"></a>

```c
int bt_bip_start_print_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_start_print_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae9ea9f936aa75b287a2152a747fd687a)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送开始打印响应（Start Print response）。

<a id="r_ga9674dc3dc2137a663a971f8521a41845"></a>

```c
int bt_bip_start_archive (struct bt_bip_client *client, bool final, struct net_buf *buf)
```

相关声明：[bt_bip_start_archive](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9674dc3dc2137a663a971f8521a41845)、[bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送开始归档请求（Start Archive request）。

<a id="r_gad16038fa018919a10d9be7fa6deeb659"></a>

```c
int bt_bip_start_archive_rsp (struct bt_bip_server *server, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_bip_start_archive_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad16038fa018919a10d9be7fa6deeb659)、[bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送开始归档响应（Start Archive response）。

<a id="r_gaf48266502eacfc19938e1dfb29a3619b"></a>

```c
int bt_bip_add_header_image_desc (struct net_buf *buf, uint16_t len, const uint8_t *desc)
```

相关声明：[bt_bip_add_header_image_desc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf48266502eacfc19938e1dfb29a3619b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向缓冲区添加图像描述符报头（Image Descriptor Header）。

<a id="r_ga4ca80902f04ea770c59c5e498fef615a"></a>

```c
int bt_bip_add_header_image_handle (struct net_buf *buf, uint16_t len, const uint8_t *handle)
```

相关声明：[bt_bip_add_header_image_handle](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga4ca80902f04ea770c59c5e498fef615a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向缓冲区添加图像句柄报头（Image Handle Header）。


## 1.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/bluetooth/uuid.h](../api_source_supplement_reference/P020_uuid.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/l2cap.h](../api_source_system_reference/P016_l2cap.h_源码浏览.md)
- [zephyr/bluetooth/classic/goep.h](../api_source_supplement_reference/P081_goep.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P019_bip.h_源码浏览.md)
- [bt_bip_transport_ops](../bluetooth_service_model_reference/P008_bt_bip_transport_ops_结构体.md)
- [bt_bip_rfcomm_server](../bluetooth_service_model_reference/P005_bt_bip_rfcomm_server_结构体.md)
- [bt_bip_l2cap_server](../bluetooth_service_model_reference/P004_bt_bip_l2cap_server_结构体.md)
- [bt_bip](../bluetooth_service_model_reference/P001_bt_bip_结构体.md)
- [bt_bip_server_cb](../bluetooth_service_model_reference/P007_bt_bip_server_cb_结构体.md)
- [bt_bip_client_cb](../bluetooth_service_model_reference/P003_bt_bip_client_cb_结构体.md)
- [bt_bip_server](../bluetooth_service_model_reference/P006_bt_bip_server_结构体.md)
- [bt_bip_client](../bluetooth_service_model_reference/P002_bt_bip_client_结构体.md)
- [BT_BIP_HDR_TYPE_GET_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga09dfef702e656fcc8ee33a42ff567689)
- [BT_BIP_HDR_TYPE_GET_IMAGE_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae993464cf0ac6e7e58f42869effc84a2)
- [BT_BIP_HDR_TYPE_GET_IMAGE_PROPERTIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga7eba82c88fc511a25210b65f0d7c4a4f)
- [BT_BIP_HDR_TYPE_GET_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga6bd29c7d876e3f617797fa91a0ea7ab6)
- [BT_BIP_HDR_TYPE_GET_LINKED_THUMBNAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga34b8c83f54c32026bd7fba15b3333489)
- [BT_BIP_HDR_TYPE_GET_LINKED_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gadcfcdfac4571707f8b8b15fba18c592a)
- [BT_BIP_HDR_TYPE_GET_PARTIAL_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gab4136d9a07d10380590e791adf57069f)
- [BT_BIP_HDR_TYPE_GET_MONITORING_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gabb3046494704ab9e6959324e459cbc80)
- [BT_BIP_HDR_TYPE_GET_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga6c4c9d3b20c7ab5daf5b7cfbc9fcac2f)
- [BT_BIP_HDR_TYPE_PUT_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga667582c6e8641099a13671e406f5fd96)
- [BT_BIP_HDR_TYPE_PUT_LINKED_THUMBNAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf12eff4b680872a4690a0d9c6f873b26)
- [BT_BIP_HDR_TYPE_PUT_LINKED_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf90f12fea45e37a1d59684a578a58bba)
- [BT_BIP_HDR_TYPE_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga4391371df2040895f16e0eed56e75e57)
- [BT_BIP_HDR_TYPE_DELETE_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae16d011e1a911d2f380bcbe0c648762a)
- [BT_BIP_HDR_TYPE_START_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad57d3fcc35a89eeacb4d92e1362a7097)
- [BT_BIP_HDR_TYPE_START_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaafe1edaef34603ceffdb08062e721ed8)
- [BT_BIP_HEADER_ID_IMG_DESC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaabe060f5798f742942d382ed4f06c83d)
- [BT_BIP_HEADER_ID_IMG_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gafb1b58780a45e82c7b1c90a738bddbb9)
- [BT_BIP_PRIM_IMAGE_PUSH_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga3d5c7f3a6a0a2fe541022c22995d4274)
- [BT_BIP_PRIM_IMAGE_PULL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gada2fa948ead9c05ec300dc3af8722e87)
- [BT_BIP_PRIM_IMAGE_PRINT_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf51de11367b7eeaa0be094d5ad561636)
- [BT_BIP_2ND_IMAGE_PRINT_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae1fd7d679c6e197b2af5557ead4b4a13)
- [BT_BIP_PRIM_AUTO_ARCHIVE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga445d8c170b5c805d86604f4d474ad0e8)
- [BT_BIP_2ND_AUTO_ARCHIVE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga2a719b3a6266dd6ce5827be47467ff14)
- [BT_BIP_PRIM_REMOTE_CAMERA_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga144e0d9835516f2e9390d1c966ede6bd)
- [BT_BIP_PRIM_REMOTE_DISPLAY_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gabf52b29d7e2f727d9f14e8b53bcc3f4f)
- [BT_BIP_UUID_IMAGE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaca571268fd723b69d19ef7cd97db1da3)
- [BT_BIP_UUID_IMAGE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga42116d3c159adecc6d63c32f0a1c4672)
- [BT_BIP_UUID_IMAGE_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaa4b44603eb57cbc223d94a8723abf06a)
- [BT_BIP_UUID_AUTO_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga098a435c80d373158ade3dc15dd538e6)
- [BT_BIP_UUID_REMOTE_CAMERA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga305af9409b4cfa25a16bed28cd305175)
- [BT_BIP_UUID_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaa8b43801cd1bf8a4d2c51b0d25a408fc)
- [BT_BIP_UUID_REFERENCED_OBJ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga8ef9620a71471340492feb1c8a820b5d)
- [BT_BIP_UUID_ARCHIVED_OBJ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae305dd59c79605feebffc3c91e641e67)
- [bt_bip_appl_param_tag_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga34de6d20263274292543a7a8afbd2c6b)
- [BT_BIP_APPL_PARAM_TAG_ID_RETURNED_HANDLES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6bace4966644e9194273b635b916eac0871)
- [BT_BIP_APPL_PARAM_TAG_ID_LIST_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba0f0d78c2da3d8f3d0caf015525b3e010)
- [BT_BIP_APPL_PARAM_TAG_ID_LATEST_CAPTURED_IMAGES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba9dbbb8ed95c7ccd86a74263fef1a1e92)
- [BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6bad6511bb04da2cf325a39bfee93f51e0c)
- [BT_BIP_APPL_PARAM_TAG_ID_PARTIAL_FILE_START_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba0ff60914fb36e587b42a473c25bd6a2d)
- [BT_BIP_APPL_PARAM_TAG_ID_TOTAL_FILE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba2565f26c0322935acef85725ac8982e5)
- [BT_BIP_APPL_PARAM_TAG_ID_END_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6baa7b18ee3ae56c0f0e84a103c1e59f05d)
- [BT_BIP_APPL_PARAM_TAG_ID_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6bab0e2dfb17de25f4ec3b27b29c2659afa)
- [BT_BIP_APPL_PARAM_TAG_ID_SERVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6ba683d101ea1babf1f147d1869ab7424f4)
- [BT_BIP_APPL_PARAM_TAG_ID_STORE_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga34de6d20263274292543a7a8afbd2c6baef58e631bfd6c511318c386308374274)
- [bt_bip_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaff38654d69104bebaaf5884283e197ef)
- [BT_BIP_PRIM_CONN_TYPE_IMAGE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa612cd818200f49e37235917fead216d2)
- [BT_BIP_PRIM_CONN_TYPE_IMAGE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa05372dbd0a01855f0863ce355a503c61)
- [BT_BIP_PRIM_CONN_TYPE_ADVANCED_IMAGE_PRINTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa05de3a972070aa4d1e29851479860d9f)
- [BT_BIP_PRIM_CONN_TYPE_AUTO_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efaf762949693b7cf70739ed0a0eb6a9d58)
- [BT_BIP_PRIM_CONN_TYPE_REMOTE_CAMERA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa8b576c667b9c6458e44ec67674bdffbd)
- [BT_BIP_PRIM_CONN_TYPE_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa12873fc1888cd99703131ae71134f0c7)
- [BT_BIP_2ND_CONN_TYPE_REFERENCED_OBJECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efa4d5ab575c877aa2a43c29cbb52a361c7)
- [BT_BIP_2ND_CONN_TYPE_ARCHIVED_OBJECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggaff38654d69104bebaaf5884283e197efabe15f984d6907bdb40c10e893e1c3bf6)
- [bt_bip_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga30d9309cbbd88b54508551285b21e575)
- [BT_BIP_ROLE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga30d9309cbbd88b54508551285b21e575aaa7de8d668d248049c5d5c75ae35d74b)
- [BT_BIP_ROLE_INITIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga30d9309cbbd88b54508551285b21e575aa5cdb11f2b0ac9c20c380dd48c9edaa5)
- [BT_BIP_ROLE_RESPONDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga30d9309cbbd88b54508551285b21e575a87d1fe99824b216780435898c2dfa968)
- [bt_bip_transport_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga7b3c6cb1159e7b2ede57c66f20b23827)
- [BT_BIP_TRANSPORT_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827ae78c865c0034d405391aaf9f72e4c9b2)
- [BT_BIP_TRANSPORT_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827ad4444da19b4e0f499867ea967dfc578f)
- [BT_BIP_TRANSPORT_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827a1af8a1481b10b53c58af8e36c7b91588)
- [BT_BIP_TRANSPORT_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga7b3c6cb1159e7b2ede57c66f20b23827a7340b2e209c71d9f944b303c22cb264d)
- [bt_bip_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad062c0f3d2feeb92a866f0fe91a6f231)
- [BT_BIP_SUPP_CAP_GENERIC_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231a786ef1ad1bde68f9b026c9d080cc41d4)
- [BT_BIP_SUPP_CAP_CAPTURING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231ac9c5d73b0d2d5eb25a962fa72ede6d5a)
- [BT_BIP_SUPP_CAP_PRINTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231a4a738d195dcf0908a64bdd246672d4bb)
- [BT_BIP_SUPP_CAP_DISPLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggad062c0f3d2feeb92a866f0fe91a6f231a324c0590cefb5d7a39f90d90e3466334)
- [bt_bip_supported_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gacfc8aaea3d27e3a42a14c49b880a5b90)
- [BT_BIP_SUPP_FEAT_IMAGE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90ac14657fd4af96f4c837916b832c25a0f)
- [BT_BIP_SUPP_FEAT_IMAGE_PUSH_STORE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a8904b7b8288e1b47d2242f5d686e32d9)
- [BT_BIP_SUPP_FEAT_IMAGE_PUSH_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90add6c2e70541aae8124bad4b102d64b88)
- [BT_BIP_SUPP_FEAT_IMAGE_PUSH_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a49668a596059e535bd59ac095dffa050)
- [BT_BIP_SUPP_FEAT_IMAGE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90aba576edd916dbf49118e78572f70320b)
- [BT_BIP_SUPP_FEAT_ADVANCED_IMAGE_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90ac64d953311bc9b76bfe75dd3133f5563)
- [BT_BIP_SUPP_FEAT_AUTO_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90af72e05ca427f8c5091e50cddac522045)
- [BT_BIP_SUPP_FEAT_REMOTE_CAMERA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a97141e2764fad3714c03b6be69ff2a9a)
- [BT_BIP_SUPP_FEAT_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggacfc8aaea3d27e3a42a14c49b880a5b90a132dd77e79fbfda8a78d5034d4c618c5)
- [bt_bip_supported_functions](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga6768e59b79bb67b5d385fdaa3dfb8888)
- [BT_BIP_SUPP_FUNC_GET_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a2e1f3364145560587963402881bb2705)
- [BT_BIP_SUPP_FUNC_PUT_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888afb1777cefdbd00e3432ddf5180804f48)
- [BT_BIP_SUPP_FUNC_PUT_LINKED_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a8a417f3073f017af866877f88ee10228)
- [BT_BIP_SUPP_FUNC_PUT_LINKED_THUMBNAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a0ee047481a35e26fa0d03bf7594d7752)
- [BT_BIP_SUPP_FUNC_REMOTE_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888adb0e03118b1cd62fe7e97b53e9f52d41)
- [BT_BIP_SUPP_FUNC_GET_IMAGE_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a7843f4dece6ff449b97ba0a2c7298b90)
- [BT_BIP_SUPP_FUNC_GET_IMAGE_PROPERTIES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888af29095b3b5964062e98b9e357de87f89)
- [BT_BIP_SUPP_FUNC_GET_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a50271c1bac792020f0fb869bb523e506)
- [BT_BIP_SUPP_FUNC_GET_LINKED_THUMBNAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a03c928dd502a98b72cb7d8eebad4b384)
- [BT_BIP_SUPP_FUNC_GET_LINKED_ATTACHMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888ac3ec252a63d494ce3e4dd696d05d94bc)
- [BT_BIP_SUPP_FUNC_DELETE_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a045dfb07426eacb16fd69247eecf70b1)
- [BT_BIP_SUPP_FUNC_START_PRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888ae1312bb3417f901204ac592e4b9376df)
- [BT_BIP_SUPP_FUNC_GET_PARTIAL_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888ae1e97efb19d10ac2b508a9e65b5c43ce)
- [BT_BIP_SUPP_FUNC_START_ARCHIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a3cae66cb380311938f83bb099a2d02da)
- [BT_BIP_SUPP_FUNC_GET_MONITORING_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888a0bde5efd58b339e53db3779a159239c1)
- [BT_BIP_SUPP_FUNC_GET_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gga6768e59b79bb67b5d385fdaa3dfb8888abf825fb7d634906f0204780ef81ca5b3)
- [bt_bip_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae4d1ed3b7e27768c1dbb6ce448cb5cf9)
- [BT_BIP_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a984245e44981ad3d85518ab1c3f576e8)
- [BT_BIP_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9acdc7fe9ee4c0d0ba447bc43817364478)
- [BT_BIP_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9ae65c7b972effa225116ec8abfcf07bc3)
- [BT_BIP_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ggae4d1ed3b7e27768c1dbb6ce448cb5cf9a96f12788ce6f56012ac4b1c25f63f67e)
- [bt_bip_rfcomm_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga644ca479c156b10d920d87d862401fc7)
- [bt_bip_rfcomm_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5ed2a46482e4fe60ef23c540001b58a3)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_bip_rfcomm_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga66a86a399f73dba932dc05d63b3749bd)
- [bt_bip_l2cap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaffb77f6c80ba05046df03d62baad211b)
- [bt_bip_l2cap_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf54b07acf22c5231b2de0fdeca7807c2)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_bip_l2cap_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga1fda174189b57c54f365784d1909152e)
- [bt_bip_set_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga0180461f24c6f741e056d64f9758b89e)
- [bt_bip_set_supported_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gab5a80d7a992d0afa0270eb09d6f3275c)
- [bt_bip_set_supported_functions](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gafe7df6ee236da3a11104f1aa6e948bfe)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_bip_primary_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga45f1ca2d2874500d6f8df3a62b01260e)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_bip_secondary_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gab0a3b58b041ac4af2682fb96b8f00a7e)
- [bt_bip_primary_image_push_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaefd318b5dc2e813eea2cd7608be1170c)
- [bt_bip_primary_image_pull_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga35c44217cbfcd8661c3f2e5725be9323)
- [bt_bip_primary_advanced_image_printing_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae8b37b224ea419ca1f1761d98a34cb2d)
- [bt_bip_primary_auto_archive_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga3848d86378912fbd9c896b14aed74161)
- [bt_bip_primary_remote_camera_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga4b236a8a28c359e392633d472a508405)
- [bt_bip_primary_remote_display_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5167b2dab89a983fae9fca356e6fbcf9)
- [bt_bip_secondary_advanced_image_printing_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga54c37cced33fa72a2c6cea10e2996e6d)
- [bt_bip_secondary_auto_archive_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gab24c4f7144f8c43dcf1b82a4c33e4ffd)
- [bt_bip_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga4e06b2fb9a99f89d7e65e8a52690442d)
- [bt_bip_primary_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad32c1b1118b606ab3ae0d9db889cbab9)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_bip_secondary_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae557b198b9d5606ee05cd29ed16f9482)
- [bt_bip_primary_image_push_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga39ec2019f86d42b02992b0a9d3ba094c)
- [bt_bip_primary_image_pull_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga2d4919c1eb568f33a89d8b176f103601)
- [bt_bip_primary_advanced_image_printing_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9352b8309334a3fe89d77f5714443376)
- [bt_bip_primary_auto_archive_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga98dca7b222c8a09b1c44861c9060193b)
- [bt_bip_primary_remote_camera_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga30e3a6ad8c00c230ac3591a934cfb81f)
- [bt_bip_primary_remote_display_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gac4ba5cef40cd451bd4b505dbea0fa135)
- [bt_bip_secondary_advanced_image_printing_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga72ef6cd266b7e57e1c80b6d8eba799e2)
- [bt_bip_secondary_auto_archive_client_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga1975916aa3da40576499f6d05aac1285)
- [bt_bip_connect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga0987a342b43bdd1926f3730f471ca05f)
- [bt_bip_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaafcd6a3503795299b6fb777ba0aa0cff)
- [bt_bip_disconnect_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaddfcee2eaea19b4819d83cf6ecb396da)
- [bt_bip_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaa0f071c8c83a54b2d48f478594579719)
- [bt_bip_abort_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga1c341ad182ff418286b64b4eff491445)
- [bt_bip_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gafcd2d4e6a8ad906c9692313421175431)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_bip_get_capabilities_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaea5d5f5b6c29a44ae89939ee3e2d6efb)
- [bt_bip_get_image_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9542e030ea863b4379d36fa21de262dc)
- [bt_bip_get_image_list_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga6e33bba952a9693d1fed7ee9bdf03df8)
- [bt_bip_get_image_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga17ae73bd6088b44206378afe3b0b9eb0)
- [bt_bip_get_image_properties_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9a91c35e91a0c30eab55da5b842427d9)
- [bt_bip_get_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga79831fc5fff332a891e6b9ff71f81d20)
- [bt_bip_get_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga53fb15ff7d0728b09f1c4e8d2ceb6dee)
- [bt_bip_get_linked_thumbnail](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad9c05d28e1e2124675b5906990c3408c)
- [bt_bip_get_linked_thumbnail_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5c3cd3e39fc21a584d6955a160ca126a)
- [bt_bip_get_linked_attachment](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad95944f07cd9f7b6bb9c81f21fffd447)
- [bt_bip_get_linked_attachment_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga70bf0d46bd16d0207e13eeb9a7844f1c)
- [bt_bip_get_partial_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga2b6a2a51fb00e7060e196051f8aea4c4)
- [bt_bip_get_partial_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gadf624e05a6d008bdcfd8a61ae6341f42)
- [bt_bip_get_monitoring_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9f1593748ffcf29015533d52266a8e19)
- [bt_bip_get_monitoring_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga301ff6e5a1e8775295659442b8c20e15)
- [bt_bip_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga578c2b59fbc8afee530168452eb221fb)
- [bt_bip_get_status_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga7abdde3a7e5dcda9c6187b5e45b75cc2)
- [bt_bip_put_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf551904672eda53e9dfcbb5a6bf4c2c3)
- [bt_bip_put_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga002f7713a8269c0b00a415bbb8c53fce)
- [bt_bip_put_linked_thumbnail](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga8b730495f4dd4e6f8db85c5b060a3cae)
- [bt_bip_put_linked_thumbnail_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gac96e873a840b072f5213b7483d633aaa)
- [bt_bip_put_linked_attachment](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga86085e98964dcfd19725b5d96f38a99b)
- [bt_bip_put_linked_attachment_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad6a7df2b0c49c0df616ef170c7b9e431)
- [bt_bip_remote_display](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga021a5d82b292d04cd0e2d53b1b32344b)
- [bt_bip_remote_display_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga0c54da02bc8dda26794f398e06e66cb3)
- [bt_bip_delete_image](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga5302af5beb7cd5c98a9cbdc288f09d3c)
- [bt_bip_delete_image_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad53a7666b90a97034276fe341c2bd7a2)
- [bt_bip_start_print](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga8a948dcee431ced321e7b5d51c8d5f9c)
- [bt_bip_start_print_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gae9ea9f936aa75b287a2152a747fd687a)
- [bt_bip_start_archive](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga9674dc3dc2137a663a971f8521a41845)
- [bt_bip_start_archive_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gad16038fa018919a10d9be7fa6deeb659)
- [bt_bip_add_header_image_desc](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#gaf48266502eacfc19938e1dfb29a3619b)
- [bt_bip_add_header_image_handle](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html#ga4ca80902f04ea770c59c5e498fef615a)

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__pinctrl__ch32v20x_30x-pinctrl.h_文件参考.md)
