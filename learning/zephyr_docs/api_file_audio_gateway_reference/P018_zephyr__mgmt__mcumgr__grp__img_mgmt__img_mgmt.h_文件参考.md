---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-18
title: zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_img\_mgmt\_\_img\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr映像管理组（Image Management Group）API的头文件。

<a id="details"></a>

```c
#include <inttypes.h>
#include <bootutil/image.h>
#include <zcbor_common.h>
```

查看此文件的源码。

MCUmgr映像管理组（Image Management Group）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

<a id="r_img_5Fmgmt_5Fupload_5Freq"></a>

```c
struct img_mgmt_upload_req
```

相关声明：[img_mgmt_upload_req](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md)。

表示单个上传请求（Upload Request）。

<a id="r_img_5Fmgmt_5Fstate"></a>

```c
struct img_mgmt_state
```

相关声明：[img_mgmt_state](../system_service_model_reference/P047_img_mgmt_state_结构体.md)。

进行中的上传所用的全局状态（Global State）。

<a id="r_img_5Fmgmt_5Fupload_5Faction"></a>

```c
struct img_mgmt_upload_action
```

相关声明：[img_mgmt_upload_action](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md)。

描述处理上传请求（Upload Request）时要执行的操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.2\_宏定义（Macros）

<a id="r_ga70168b0d707c15658fd09b02c361a64c"></a>

```c
#define IMG_MGMT_DATA_SHA_LEN 32 /* SHA256 */
```

相关声明：[IMG_MGMT_DATA_SHA_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga70168b0d707c15658fd09b02c361a64c)。

<a id="r_ga57a5c429be5a3860981007e9728db181"></a>

```c
#define IMG_MGMT_VER_MAX_STR_LEN (sizeof("255.255.65535.4294967295"))
```

相关声明：[IMG_MGMT_VER_MAX_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga57a5c429be5a3860981007e9728db181)。

<a id="r_ga56e01e5bfa9fdd9bf6ebdc0dc3ac19ba"></a>

```c
#define IMG_MGMT_UPLOAD_ACTION_SET_RC_RSN(action, rsn)
```

相关声明：[IMG_MGMT_UPLOAD_ACTION_SET_RC_RSN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga56e01e5bfa9fdd9bf6ebdc0dc3ac19ba)。

<a id="r_gaee07bacea29269e24ca15a2e1716390d"></a>

```c
#define IMG_MGMT_UPLOAD_ACTION_RC_RSN(action)
```

相关声明：[IMG_MGMT_UPLOAD_ACTION_RC_RSN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gaee07bacea29269e24ca15a2e1716390d)。

<a id="define-members-0"></a>

### 镜像状态标志（Image State Flags）

<a id="r_ga459776db5ce7bbfebae5e74aef4067ef"></a>

```c
#define IMG_MGMT_STATE_F_PENDING 0x01
```

相关声明：[IMG_MGMT_STATE_F_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga459776db5ce7bbfebae5e74aef4067ef)。

已将此镜像设为下次交换（Swap）的对象。

<a id="r_ga581c2626a47ca249ecbcc42edb7a59c2"></a>

```c
#define IMG_MGMT_STATE_F_CONFIRMED 0x02
```

相关声明：[IMG_MGMT_STATE_F_CONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga581c2626a47ca249ecbcc42edb7a59c2)。

镜像已确认（Confirmed）。

<a id="r_ga2a11cfad9698b0460b846fa079234c03"></a>

```c
#define IMG_MGMT_STATE_F_ACTIVE 0x04
```

相关声明：[IMG_MGMT_STATE_F_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga2a11cfad9698b0460b846fa079234c03)。

镜像当前处于活动状态（Active）。

<a id="r_gae47e88131d96901e70b2b67ea43ceb4a"></a>

```c
#define IMG_MGMT_STATE_F_PERMANENT 0x08
```

相关声明：[IMG_MGMT_STATE_F_PERMANENT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gae47e88131d96901e70b2b67ea43ceb4a)。

镜像将在下次启动后保留在主槽位（Primary Slot）。

<a id="define-members-1"></a>

### 镜像管理状态机的交换类型（Swap Types for Image Management State Machine）

<a id="r_ga55e68ef4a5caa3c68987af438ebe8236"></a>

```c
#define IMG_MGMT_SWAP_TYPE_NONE 0
```

相关声明：[IMG_MGMT_SWAP_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga55e68ef4a5caa3c68987af438ebe8236)。

不交换（No Swap）。

<a id="r_ga71a0715be72de416f3d4744f4763a241"></a>

```c
#define IMG_MGMT_SWAP_TYPE_TEST 1
```

相关声明：[IMG_MGMT_SWAP_TYPE_TEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga71a0715be72de416f3d4744f4763a241)。

测试交换（Test Swap）。

<a id="r_ga69c51ca39c8d33db392e2353873aac43"></a>

```c
#define IMG_MGMT_SWAP_TYPE_PERM 2
```

相关声明：[IMG_MGMT_SWAP_TYPE_PERM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga69c51ca39c8d33db392e2353873aac43)。

永久交换（Permanent Swap）。

<a id="r_ga43a9afd49822eda7b640d3adb9219f10"></a>

```c
#define IMG_MGMT_SWAP_TYPE_REVERT 3
```

相关声明：[IMG_MGMT_SWAP_TYPE_REVERT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga43a9afd49822eda7b640d3adb9219f10)。

回退交换（Revert Swap）。

<a id="r_ga35a8dd8ca661f2a602bc04d4ae6361a6"></a>

```c
#define IMG_MGMT_SWAP_TYPE_UNKNOWN 255
```

相关声明：[IMG_MGMT_SWAP_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga35a8dd8ca661f2a602bc04d4ae6361a6)。

未知交换（Unknown Swap）。

<a id="define-members-2"></a>

### 镜像管理组命令 ID（Command IDs for Image Management Group）

<a id="r_ga19396c2690a0d40f625792ab644e7d17"></a>

```c
#define IMG_MGMT_ID_STATE 0
```

相关声明：[IMG_MGMT_ID_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga19396c2690a0d40f625792ab644e7d17)。

镜像状态（State of Images）。

<a id="r_ga70541d06c76224a631f493023e05a73a"></a>

```c
#define IMG_MGMT_ID_UPLOAD 1
```

相关声明：[IMG_MGMT_ID_UPLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga70541d06c76224a631f493023e05a73a)。

镜像上传（Image Upload）。

<a id="r_ga90225baf3e08859f294d9aaaf2012e6b"></a>

```c
#define IMG_MGMT_ID_FILE 2
```

相关声明：[IMG_MGMT_ID_FILE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga90225baf3e08859f294d9aaaf2012e6b)。

文件（File）。

<a id="r_ga46e9a83aab777da2591d4c7cb701b5cd"></a>

```c
#define IMG_MGMT_ID_CORELIST 3
```

相关声明：[IMG_MGMT_ID_CORELIST](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga46e9a83aab777da2591d4c7cb701b5cd)。

核心转储列表（Corelist）。

<a id="r_ga22af869af6cbdde12f2cbc811fe7d443"></a>

```c
#define IMG_MGMT_ID_CORELOAD 4
```

相关声明：[IMG_MGMT_ID_CORELOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga22af869af6cbdde12f2cbc811fe7d443)。

核心转储加载（Coreload）。

<a id="r_gaf7de4c1d77bc29eea4b3d46382bd954f"></a>

```c
#define IMG_MGMT_ID_ERASE 5
```

相关声明：[IMG_MGMT_ID_ERASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gaf7de4c1d77bc29eea4b3d46382bd954f)。

镜像擦除（Image Erase）。

<a id="r_gacb33e3b0729f8621275c6b3dc9795d57"></a>

```c
#define IMG_MGMT_ID_SLOT_INFO 6
```

相关声明：[IMG_MGMT_ID_SLOT_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gacb33e3b0729f8621275c6b3dc9795d57)。

槽位信息（Slot Info）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 18.3\_枚举（Enumerations）

<a id="r_ga669286d96816e0e99792f407752c81a5"></a>

```c
enum img_mgmt_err_code_t { IMG_MGMT_ERR_OK = 0 , IMG_MGMT_ERR_UNKNOWN , IMG_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL , IMG_MGMT_ERR_NO_IMAGE , IMG_MGMT_ERR_NO_TLVS , IMG_MGMT_ERR_INVALID_TLV , IMG_MGMT_ERR_TLV_MULTIPLE_HASHES_FOUND , IMG_MGMT_ERR_TLV_INVALID_SIZE , IMG_MGMT_ERR_HASH_NOT_FOUND , IMG_MGMT_ERR_NO_FREE_SLOT , IMG_MGMT_ERR_FLASH_OPEN_FAILED , IMG_MGMT_ERR_FLASH_READ_FAILED , IMG_MGMT_ERR_FLASH_WRITE_FAILED , IMG_MGMT_ERR_FLASH_ERASE_FAILED , IMG_MGMT_ERR_INVALID_SLOT , IMG_MGMT_ERR_NO_FREE_MEMORY , IMG_MGMT_ERR_FLASH_CONTEXT_ALREADY_SET , IMG_MGMT_ERR_FLASH_CONTEXT_NOT_SET , IMG_MGMT_ERR_FLASH_AREA_DEVICE_NULL , IMG_MGMT_ERR_INVALID_PAGE_OFFSET , IMG_MGMT_ERR_INVALID_OFFSET , IMG_MGMT_ERR_INVALID_LENGTH , IMG_MGMT_ERR_INVALID_IMAGE_HEADER , IMG_MGMT_ERR_INVALID_IMAGE_HEADER_MAGIC , IMG_MGMT_ERR_INVALID_HASH , IMG_MGMT_ERR_INVALID_FLASH_ADDRESS , IMG_MGMT_ERR_VERSION_GET_FAILED , IMG_MGMT_ERR_CURRENT_VERSION_IS_NEWER , IMG_MGMT_ERR_IMAGE_ALREADY_PENDING , IMG_MGMT_ERR_INVALID_IMAGE_VECTOR_TABLE , IMG_MGMT_ERR_INVALID_IMAGE_TOO_LARGE , IMG_MGMT_ERR_INVALID_IMAGE_DATA_OVERRUN , IMG_MGMT_ERR_IMAGE_CONFIRMATION_DENIED , IMG_MGMT_ERR_IMAGE_SETTING_TEST_TO_ACTIVE_DENIED , IMG_MGMT_ERR_ACTIVE_SLOT_NOT_KNOWN }
```

相关声明：[img_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga669286d96816e0e99792f407752c81a5)、[IMG_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a7db18fe6cb5913fec882dc515d8bb7a0)、[IMG_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a8f1bd00b3e00f070b07269fdddd2c8fe)、[IMG_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a5b4301665ef0c9818fcd3174908e5063)、[IMG_MGMT_ERR_NO_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a360155fc7e541080a7b80bee6ec9dbb6)、[IMG_MGMT_ERR_NO_TLVS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a598c03b99a2be60cf4847fa2f32c5d10)、[IMG_MGMT_ERR_INVALID_TLV](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a4725027793b17187474089fde35730cb)、[IMG_MGMT_ERR_TLV_MULTIPLE_HASHES_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5aced7bb74d51b7dd7ff922cf555722276)、[IMG_MGMT_ERR_TLV_INVALID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a967c4f0b3d33d925e28f076c8cc3ed5c)、[IMG_MGMT_ERR_HASH_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a5d89dde479611276e6956706ee357c6e)、[IMG_MGMT_ERR_NO_FREE_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a0d16138a65766047e4917022068832fa)、[IMG_MGMT_ERR_FLASH_OPEN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a8253896c206d8f3ba486466555662071)、[IMG_MGMT_ERR_FLASH_READ_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a9a09d73602a77e112a95fa977e9b0355)、[IMG_MGMT_ERR_FLASH_WRITE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5adf54010236b4e6bb4669cdeeb4a6979f)、[IMG_MGMT_ERR_FLASH_ERASE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a869d0aa27c38187fdb73d36397dcef3c)、[IMG_MGMT_ERR_INVALID_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a7c0f0cda8165d0acf5fc2a072a5c5cc5)、[IMG_MGMT_ERR_NO_FREE_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ab75ac303b054a02e99a0ed9726c988de)、[IMG_MGMT_ERR_FLASH_CONTEXT_ALREADY_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5af1eac867913981a4d8f1f2d64108706e)、[IMG_MGMT_ERR_FLASH_CONTEXT_NOT_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a9e4c9f1a79f645130ef9a8aa09b8b544)、[IMG_MGMT_ERR_FLASH_AREA_DEVICE_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a6c1c103d76e1f16fda77525ba136e9b2)、[IMG_MGMT_ERR_INVALID_PAGE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a857b6ecc22e5f54834638aa604cce6bf)、[IMG_MGMT_ERR_INVALID_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a8a94dfe1aca340c4337fe92554ede4b0)、[IMG_MGMT_ERR_INVALID_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a227b2b3be93cf963ce034b9cb817d0ca)、[IMG_MGMT_ERR_INVALID_IMAGE_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5acfdb28d59643e70db86abfa72c2833b7)、[IMG_MGMT_ERR_INVALID_IMAGE_HEADER_MAGIC](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a5606b72a7bf61832b92c77e729e02093)、[IMG_MGMT_ERR_INVALID_HASH](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a4b2994e51eadae6cb43c3683d6e223b6)、[IMG_MGMT_ERR_INVALID_FLASH_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a27502b76efcc09ef01cfbe777a9e8086)、[IMG_MGMT_ERR_VERSION_GET_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ae710879342357f27c9705989f572b82f)、[IMG_MGMT_ERR_CURRENT_VERSION_IS_NEWER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a37ad5efbaacdcb708a65674a4dc83d85)、[IMG_MGMT_ERR_IMAGE_ALREADY_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5af55239776b4b5a5eead0440fb3b884b3)、[IMG_MGMT_ERR_INVALID_IMAGE_VECTOR_TABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a3a8d3005c72273ee065c34396d3fd2f7)、[IMG_MGMT_ERR_INVALID_IMAGE_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ab258cd53a5cc13e2376662690703f54b)、[IMG_MGMT_ERR_INVALID_IMAGE_DATA_OVERRUN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a92ab3773cdbd00b42fb59865e958069b)、[IMG_MGMT_ERR_IMAGE_CONFIRMATION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ae2413b0ade3185b91ae085af397adabf)、[IMG_MGMT_ERR_IMAGE_SETTING_TEST_TO_ACTIVE_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ab195578794ddc6cffa5e056ee34350a8)、[IMG_MGMT_ERR_ACTIVE_SLOT_NOT_KNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a3220405113525f3d5af068b8bf2a80f6)。

镜像管理组（Image Management Group）的命令结果码。

<a id="r_ga1d239fef127e65b11b71360eadfa1ede"></a>

```c
enum img_mgmt_id_upload_t { IMG_MGMT_ID_UPLOAD_STATUS_START = 0 , IMG_MGMT_ID_UPLOAD_STATUS_ONGOING , IMG_MGMT_ID_UPLOAD_STATUS_COMPLETE }
```

相关声明：[img_mgmt_id_upload_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga1d239fef127e65b11b71360eadfa1ede)、[IMG_MGMT_ID_UPLOAD_STATUS_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga1d239fef127e65b11b71360eadfa1edeaff49286e379bd39781a563c1e52c6c8c)、[IMG_MGMT_ID_UPLOAD_STATUS_ONGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga1d239fef127e65b11b71360eadfa1edea7cf567b16af18752316fde6444e23a21)、[IMG_MGMT_ID_UPLOAD_STATUS_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga1d239fef127e65b11b71360eadfa1edeab106874625a50d626e55130e91d37bf2)。

IMG_MGMT_ID_UPLOAD 状态（Statuses）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.4\_函数（Functions）

<a id="r_ga60ae88823a561160b1ddc406382e4ac3"></a>

```c
int img_mgmt_read_info (int image_slot, struct image_version *ver, uint8_t *hash, uint32_t *flags)
```

相关声明：[img_mgmt_read_info](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga60ae88823a561160b1ddc406382e4ac3)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_gae9cfa02e5f171d68287cdb0d7d4c0610"></a>

```c
int img_mgmt_my_version (struct image_version *ver)
```

相关声明：[img_mgmt_my_version](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gae9cfa02e5f171d68287cdb0d7d4c0610)。

获取当前运行应用的镜像版本（Image Version）。

<a id="r_ga5199849b6d8847c6a1260254940db95b"></a>

```c
int img_mgmt_ver_str (const struct image_version *ver, char *dst)
```

相关声明：[img_mgmt_ver_str](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga5199849b6d8847c6a1260254940db95b)。

根据 struct image_version 格式化版本字符串（Version String）。

<a id="r_gab35c8adf2e5e2c941ecbaf3c03101e55"></a>

```c
int img_mgmt_active_slot (int image)
```

相关声明：[img_mgmt_active_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gab35c8adf2e5e2c941ecbaf3c03101e55)。

获取指定镜像当前活动且正在运行的应用槽位编号（Slot Number）。

<a id="r_gab6a92433b859fce18b58e6110fa5f489"></a>

```c
int img_mgmt_active_image (void)
```

相关声明：[img_mgmt_active_image](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gab6a92433b859fce18b58e6110fa5f489)。

获取活动镜像编号（Active Image Number）。

<a id="r_ga90de2da23bcd650ca59219fdfd4f55a1"></a>

```c
int img_mgmt_slot_in_use (int slot)
```

相关声明：[img_mgmt_slot_in_use](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga90de2da23bcd650ca59219fdfd4f55a1)。

检查镜像槽位（Image Slot）是否正在使用。

<a id="r_ga3e496199d0ea4aa1b3f51e59bb7473f0"></a>

```c
int img_mgmt_state_any_pending (void)
```

相关声明：[img_mgmt_state_any_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga3e496199d0ea4aa1b3f51e59bb7473f0)。

检查是否有槽位处于 MCUboot 待处理状态（Pending State）。

<a id="r_ga42475389b4e31d5f35ea58873527e948"></a>

```c
uint8_t img_mgmt_state_flags (int query_slot)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[img_mgmt_state_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga42475389b4e31d5f35ea58873527e948)。

返回为槽位设置的状态标志（State Flags）。

<a id="r_ga7e529fa76ddb3d3bf4a527cb11fa9c89"></a>

```c
int img_mgmt_state_set_pending (int slot, int permanent)
```

相关声明：[img_mgmt_state_set_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga7e529fa76ddb3d3bf4a527cb11fa9c89)。

设置指定镜像槽位的待处理标志（Pending Flag）。

<a id="r_gaed0b945d2f83daf63d850b232a2cfea8"></a>

```c
int img_mgmt_state_confirm (void)
```

相关声明：[img_mgmt_state_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gaed0b945d2f83daf63d850b232a2cfea8)。

确认当前镜像状态（Image State）。

<a id="r_ga6c9124cc59c99769908cdf83f58e1bf1"></a>

```c
int img_mgmt_vercmp (const struct image_version *a, const struct image_version *b)
```

相关声明：[img_mgmt_vercmp](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga6c9124cc59c99769908cdf83f58e1bf1)。

以兼容语义化版本（Semantic Versioning，SemVer）的方式比较两个镜像版本号。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 18.5\_变量（Variables）

<a id="r_ga0d6bb8877516ca486c318fa12c129138"></a>

```c
int boot_current_slot
```

相关声明：[boot_current_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga0d6bb8877516ca486c318fa12c129138)。

<a id="r_gad3dce7b70ce3338588003a021eec1ab6"></a>

```c
struct img_mgmt_state g_img_mgmt_state
```

相关声明：[img_mgmt_state](../system_service_model_reference/P047_img_mgmt_state_结构体.md)、[g_img_mgmt_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gad3dce7b70ce3338588003a021eec1ab6)。


## 18.6\_原页交叉引用（Cross References）

- [inttypes.h](../api_source_http_wifi_reference/P005_inttypes.h_源码浏览.md)
- [查看此文件的源码。](../api_source_network_reference/P011_img_mgmt.h_源码浏览.md)
- [img_mgmt_upload_req](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md)
- [img_mgmt_state](../system_service_model_reference/P047_img_mgmt_state_结构体.md)
- [img_mgmt_upload_action](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md)
- [IMG_MGMT_DATA_SHA_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga70168b0d707c15658fd09b02c361a64c)
- [IMG_MGMT_VER_MAX_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga57a5c429be5a3860981007e9728db181)
- [IMG_MGMT_UPLOAD_ACTION_SET_RC_RSN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga56e01e5bfa9fdd9bf6ebdc0dc3ac19ba)
- [IMG_MGMT_UPLOAD_ACTION_RC_RSN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gaee07bacea29269e24ca15a2e1716390d)
- [IMG_MGMT_STATE_F_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga459776db5ce7bbfebae5e74aef4067ef)
- [IMG_MGMT_STATE_F_CONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga581c2626a47ca249ecbcc42edb7a59c2)
- [IMG_MGMT_STATE_F_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga2a11cfad9698b0460b846fa079234c03)
- [IMG_MGMT_STATE_F_PERMANENT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gae47e88131d96901e70b2b67ea43ceb4a)
- [IMG_MGMT_SWAP_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga55e68ef4a5caa3c68987af438ebe8236)
- [IMG_MGMT_SWAP_TYPE_TEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga71a0715be72de416f3d4744f4763a241)
- [IMG_MGMT_SWAP_TYPE_PERM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga69c51ca39c8d33db392e2353873aac43)
- [IMG_MGMT_SWAP_TYPE_REVERT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga43a9afd49822eda7b640d3adb9219f10)
- [IMG_MGMT_SWAP_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga35a8dd8ca661f2a602bc04d4ae6361a6)
- [IMG_MGMT_ID_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga19396c2690a0d40f625792ab644e7d17)
- [IMG_MGMT_ID_UPLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga70541d06c76224a631f493023e05a73a)
- [IMG_MGMT_ID_FILE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga90225baf3e08859f294d9aaaf2012e6b)
- [IMG_MGMT_ID_CORELIST](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga46e9a83aab777da2591d4c7cb701b5cd)
- [IMG_MGMT_ID_CORELOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga22af869af6cbdde12f2cbc811fe7d443)
- [IMG_MGMT_ID_ERASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gaf7de4c1d77bc29eea4b3d46382bd954f)
- [IMG_MGMT_ID_SLOT_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gacb33e3b0729f8621275c6b3dc9795d57)
- [img_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga669286d96816e0e99792f407752c81a5)
- [IMG_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a7db18fe6cb5913fec882dc515d8bb7a0)
- [IMG_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a8f1bd00b3e00f070b07269fdddd2c8fe)
- [IMG_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a5b4301665ef0c9818fcd3174908e5063)
- [IMG_MGMT_ERR_NO_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a360155fc7e541080a7b80bee6ec9dbb6)
- [IMG_MGMT_ERR_NO_TLVS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a598c03b99a2be60cf4847fa2f32c5d10)
- [IMG_MGMT_ERR_INVALID_TLV](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a4725027793b17187474089fde35730cb)
- [IMG_MGMT_ERR_TLV_MULTIPLE_HASHES_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5aced7bb74d51b7dd7ff922cf555722276)
- [IMG_MGMT_ERR_TLV_INVALID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a967c4f0b3d33d925e28f076c8cc3ed5c)
- [IMG_MGMT_ERR_HASH_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a5d89dde479611276e6956706ee357c6e)
- [IMG_MGMT_ERR_NO_FREE_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a0d16138a65766047e4917022068832fa)
- [IMG_MGMT_ERR_FLASH_OPEN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a8253896c206d8f3ba486466555662071)
- [IMG_MGMT_ERR_FLASH_READ_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a9a09d73602a77e112a95fa977e9b0355)
- [IMG_MGMT_ERR_FLASH_WRITE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5adf54010236b4e6bb4669cdeeb4a6979f)
- [IMG_MGMT_ERR_FLASH_ERASE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a869d0aa27c38187fdb73d36397dcef3c)
- [IMG_MGMT_ERR_INVALID_SLOT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a7c0f0cda8165d0acf5fc2a072a5c5cc5)
- [IMG_MGMT_ERR_NO_FREE_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ab75ac303b054a02e99a0ed9726c988de)
- [IMG_MGMT_ERR_FLASH_CONTEXT_ALREADY_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5af1eac867913981a4d8f1f2d64108706e)
- [IMG_MGMT_ERR_FLASH_CONTEXT_NOT_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a9e4c9f1a79f645130ef9a8aa09b8b544)
- [IMG_MGMT_ERR_FLASH_AREA_DEVICE_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a6c1c103d76e1f16fda77525ba136e9b2)
- [IMG_MGMT_ERR_INVALID_PAGE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a857b6ecc22e5f54834638aa604cce6bf)
- [IMG_MGMT_ERR_INVALID_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a8a94dfe1aca340c4337fe92554ede4b0)
- [IMG_MGMT_ERR_INVALID_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a227b2b3be93cf963ce034b9cb817d0ca)
- [IMG_MGMT_ERR_INVALID_IMAGE_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5acfdb28d59643e70db86abfa72c2833b7)
- [IMG_MGMT_ERR_INVALID_IMAGE_HEADER_MAGIC](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a5606b72a7bf61832b92c77e729e02093)
- [IMG_MGMT_ERR_INVALID_HASH](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a4b2994e51eadae6cb43c3683d6e223b6)
- [IMG_MGMT_ERR_INVALID_FLASH_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a27502b76efcc09ef01cfbe777a9e8086)
- [IMG_MGMT_ERR_VERSION_GET_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ae710879342357f27c9705989f572b82f)
- [IMG_MGMT_ERR_CURRENT_VERSION_IS_NEWER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a37ad5efbaacdcb708a65674a4dc83d85)
- [IMG_MGMT_ERR_IMAGE_ALREADY_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5af55239776b4b5a5eead0440fb3b884b3)
- [IMG_MGMT_ERR_INVALID_IMAGE_VECTOR_TABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a3a8d3005c72273ee065c34396d3fd2f7)
- [IMG_MGMT_ERR_INVALID_IMAGE_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ab258cd53a5cc13e2376662690703f54b)
- [IMG_MGMT_ERR_INVALID_IMAGE_DATA_OVERRUN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a92ab3773cdbd00b42fb59865e958069b)
- [IMG_MGMT_ERR_IMAGE_CONFIRMATION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ae2413b0ade3185b91ae085af397adabf)
- [IMG_MGMT_ERR_IMAGE_SETTING_TEST_TO_ACTIVE_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5ab195578794ddc6cffa5e056ee34350a8)
- [IMG_MGMT_ERR_ACTIVE_SLOT_NOT_KNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga669286d96816e0e99792f407752c81a5a3220405113525f3d5af068b8bf2a80f6)
- [img_mgmt_id_upload_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga1d239fef127e65b11b71360eadfa1ede)
- [IMG_MGMT_ID_UPLOAD_STATUS_START](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga1d239fef127e65b11b71360eadfa1edeaff49286e379bd39781a563c1e52c6c8c)
- [IMG_MGMT_ID_UPLOAD_STATUS_ONGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga1d239fef127e65b11b71360eadfa1edea7cf567b16af18752316fde6444e23a21)
- [IMG_MGMT_ID_UPLOAD_STATUS_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gga1d239fef127e65b11b71360eadfa1edeab106874625a50d626e55130e91d37bf2)
- [img_mgmt_read_info](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga60ae88823a561160b1ddc406382e4ac3)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [img_mgmt_my_version](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gae9cfa02e5f171d68287cdb0d7d4c0610)
- [img_mgmt_ver_str](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga5199849b6d8847c6a1260254940db95b)
- [img_mgmt_active_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gab35c8adf2e5e2c941ecbaf3c03101e55)
- [img_mgmt_active_image](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gab6a92433b859fce18b58e6110fa5f489)
- [img_mgmt_slot_in_use](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga90de2da23bcd650ca59219fdfd4f55a1)
- [img_mgmt_state_any_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga3e496199d0ea4aa1b3f51e59bb7473f0)
- [img_mgmt_state_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga42475389b4e31d5f35ea58873527e948)
- [img_mgmt_state_set_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga7e529fa76ddb3d3bf4a527cb11fa9c89)
- [img_mgmt_state_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gaed0b945d2f83daf63d850b232a2cfea8)
- [img_mgmt_vercmp](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga6c9124cc59c99769908cdf83f58e1bf1)
- [boot_current_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga0d6bb8877516ca486c318fa12c129138)
- [g_img_mgmt_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#gad3dce7b70ce3338588003a021eec1ab6)

<a id="header-details"></a>

---

[上一章](P017_zephyr__bluetooth__audio__has.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__interrupt_controller__intc_infineon_aurix.h_文件参考.md)
