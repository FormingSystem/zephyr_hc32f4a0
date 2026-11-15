---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-10
title: 映像管理（Image Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_映像管理（Image Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 映像管理 API

<a id="details"></a>

MCUmgr 映像管理 API

<a id="header-groups"></a>
<a id="groups"></a>

## 10.1\_主题（Topics）

<a id="r_mcumgr_5Fcallback_5Fapi_5Fimg_5Fmgmt"></a>

相关声明：[映像管理回调（Image Management Callbacks）](../api_update_memory_topic_reference/P010_映像管理回调（Image Management Callbacks）.md)。

MCUmgr 映像管理回调 API

<a id="r_mcumgr_5Fimg_5Fmgmt_5Fclient"></a>

相关声明：[映像管理客户端（Image Management Client）](../api_input_runtime_topic_reference/P013_映像管理客户端（Image Management Client）.md)。

MCUmgr 映像管理客户端 API

<a id="header-files"></a>
<a id="files"></a>

## 10.2\_文件（Files）

<a id="r_img_5Fmgmt_2Eh"></a>

```c
file img_mgmt.h
```

相关声明：[img_mgmt.h](../api_file_audio_gateway_reference/P018_zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt.h_文件参考.md)。

MCUmgr映像管理组（Image Management Group）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.3\_数据结构（Data Structures）

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

## 10.4\_宏定义（Macros）

<a id="r_ga70168b0d707c15658fd09b02c361a64c"></a>

```c
#define IMG_MGMT_DATA_SHA_LEN 32 /* SHA256 */
```

相关声明：[IMG_MGMT_DATA_SHA_LEN](#ga70168b0d707c15658fd09b02c361a64c)。

<a id="r_ga57a5c429be5a3860981007e9728db181"></a>

```c
#define IMG_MGMT_VER_MAX_STR_LEN (sizeof("255.255.65535.4294967295"))
```

相关声明：[IMG_MGMT_VER_MAX_STR_LEN](#ga57a5c429be5a3860981007e9728db181)。

<a id="r_ga56e01e5bfa9fdd9bf6ebdc0dc3ac19ba"></a>

```c
#define IMG_MGMT_UPLOAD_ACTION_SET_RC_RSN(action, rsn)
```

相关声明：[IMG_MGMT_UPLOAD_ACTION_SET_RC_RSN](#ga56e01e5bfa9fdd9bf6ebdc0dc3ac19ba)。

<a id="r_gaee07bacea29269e24ca15a2e1716390d"></a>

```c
#define IMG_MGMT_UPLOAD_ACTION_RC_RSN(action)
```

相关声明：[IMG_MGMT_UPLOAD_ACTION_RC_RSN](#gaee07bacea29269e24ca15a2e1716390d)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.5\_枚举（Enumerations）

<a id="r_ga669286d96816e0e99792f407752c81a5"></a>

```c
enum img_mgmt_err_code_t { IMG_MGMT_ERR_OK = 0 , IMG_MGMT_ERR_UNKNOWN , IMG_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL , IMG_MGMT_ERR_NO_IMAGE , IMG_MGMT_ERR_NO_TLVS , IMG_MGMT_ERR_INVALID_TLV , IMG_MGMT_ERR_TLV_MULTIPLE_HASHES_FOUND , IMG_MGMT_ERR_TLV_INVALID_SIZE , IMG_MGMT_ERR_HASH_NOT_FOUND , IMG_MGMT_ERR_NO_FREE_SLOT , IMG_MGMT_ERR_FLASH_OPEN_FAILED , IMG_MGMT_ERR_FLASH_READ_FAILED , IMG_MGMT_ERR_FLASH_WRITE_FAILED , IMG_MGMT_ERR_FLASH_ERASE_FAILED , IMG_MGMT_ERR_INVALID_SLOT , IMG_MGMT_ERR_NO_FREE_MEMORY , IMG_MGMT_ERR_FLASH_CONTEXT_ALREADY_SET , IMG_MGMT_ERR_FLASH_CONTEXT_NOT_SET , IMG_MGMT_ERR_FLASH_AREA_DEVICE_NULL , IMG_MGMT_ERR_INVALID_PAGE_OFFSET , IMG_MGMT_ERR_INVALID_OFFSET , IMG_MGMT_ERR_INVALID_LENGTH , IMG_MGMT_ERR_INVALID_IMAGE_HEADER , IMG_MGMT_ERR_INVALID_IMAGE_HEADER_MAGIC , IMG_MGMT_ERR_INVALID_HASH , IMG_MGMT_ERR_INVALID_FLASH_ADDRESS , IMG_MGMT_ERR_VERSION_GET_FAILED , IMG_MGMT_ERR_CURRENT_VERSION_IS_NEWER , IMG_MGMT_ERR_IMAGE_ALREADY_PENDING , IMG_MGMT_ERR_INVALID_IMAGE_VECTOR_TABLE , IMG_MGMT_ERR_INVALID_IMAGE_TOO_LARGE , IMG_MGMT_ERR_INVALID_IMAGE_DATA_OVERRUN , IMG_MGMT_ERR_IMAGE_CONFIRMATION_DENIED , IMG_MGMT_ERR_IMAGE_SETTING_TEST_TO_ACTIVE_DENIED , IMG_MGMT_ERR_ACTIVE_SLOT_NOT_KNOWN }
```

相关声明：[img_mgmt_err_code_t](#ga669286d96816e0e99792f407752c81a5)、[IMG_MGMT_ERR_OK](#gga669286d96816e0e99792f407752c81a5a7db18fe6cb5913fec882dc515d8bb7a0)、[IMG_MGMT_ERR_UNKNOWN](#gga669286d96816e0e99792f407752c81a5a8f1bd00b3e00f070b07269fdddd2c8fe)、[IMG_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL](#gga669286d96816e0e99792f407752c81a5a5b4301665ef0c9818fcd3174908e5063)、[IMG_MGMT_ERR_NO_IMAGE](#gga669286d96816e0e99792f407752c81a5a360155fc7e541080a7b80bee6ec9dbb6)、[IMG_MGMT_ERR_NO_TLVS](#gga669286d96816e0e99792f407752c81a5a598c03b99a2be60cf4847fa2f32c5d10)、[IMG_MGMT_ERR_INVALID_TLV](#gga669286d96816e0e99792f407752c81a5a4725027793b17187474089fde35730cb)、[IMG_MGMT_ERR_TLV_MULTIPLE_HASHES_FOUND](#gga669286d96816e0e99792f407752c81a5aced7bb74d51b7dd7ff922cf555722276)、[IMG_MGMT_ERR_TLV_INVALID_SIZE](#gga669286d96816e0e99792f407752c81a5a967c4f0b3d33d925e28f076c8cc3ed5c)、[IMG_MGMT_ERR_HASH_NOT_FOUND](#gga669286d96816e0e99792f407752c81a5a5d89dde479611276e6956706ee357c6e)、[IMG_MGMT_ERR_NO_FREE_SLOT](#gga669286d96816e0e99792f407752c81a5a0d16138a65766047e4917022068832fa)、[IMG_MGMT_ERR_FLASH_OPEN_FAILED](#gga669286d96816e0e99792f407752c81a5a8253896c206d8f3ba486466555662071)、[IMG_MGMT_ERR_FLASH_READ_FAILED](#gga669286d96816e0e99792f407752c81a5a9a09d73602a77e112a95fa977e9b0355)、[IMG_MGMT_ERR_FLASH_WRITE_FAILED](#gga669286d96816e0e99792f407752c81a5adf54010236b4e6bb4669cdeeb4a6979f)、[IMG_MGMT_ERR_FLASH_ERASE_FAILED](#gga669286d96816e0e99792f407752c81a5a869d0aa27c38187fdb73d36397dcef3c)、[IMG_MGMT_ERR_INVALID_SLOT](#gga669286d96816e0e99792f407752c81a5a7c0f0cda8165d0acf5fc2a072a5c5cc5)、[IMG_MGMT_ERR_NO_FREE_MEMORY](#gga669286d96816e0e99792f407752c81a5ab75ac303b054a02e99a0ed9726c988de)、[IMG_MGMT_ERR_FLASH_CONTEXT_ALREADY_SET](#gga669286d96816e0e99792f407752c81a5af1eac867913981a4d8f1f2d64108706e)、[IMG_MGMT_ERR_FLASH_CONTEXT_NOT_SET](#gga669286d96816e0e99792f407752c81a5a9e4c9f1a79f645130ef9a8aa09b8b544)、[IMG_MGMT_ERR_FLASH_AREA_DEVICE_NULL](#gga669286d96816e0e99792f407752c81a5a6c1c103d76e1f16fda77525ba136e9b2)、[IMG_MGMT_ERR_INVALID_PAGE_OFFSET](#gga669286d96816e0e99792f407752c81a5a857b6ecc22e5f54834638aa604cce6bf)、[IMG_MGMT_ERR_INVALID_OFFSET](#gga669286d96816e0e99792f407752c81a5a8a94dfe1aca340c4337fe92554ede4b0)、[IMG_MGMT_ERR_INVALID_LENGTH](#gga669286d96816e0e99792f407752c81a5a227b2b3be93cf963ce034b9cb817d0ca)、[IMG_MGMT_ERR_INVALID_IMAGE_HEADER](#gga669286d96816e0e99792f407752c81a5acfdb28d59643e70db86abfa72c2833b7)、[IMG_MGMT_ERR_INVALID_IMAGE_HEADER_MAGIC](#gga669286d96816e0e99792f407752c81a5a5606b72a7bf61832b92c77e729e02093)、[IMG_MGMT_ERR_INVALID_HASH](#gga669286d96816e0e99792f407752c81a5a4b2994e51eadae6cb43c3683d6e223b6)、[IMG_MGMT_ERR_INVALID_FLASH_ADDRESS](#gga669286d96816e0e99792f407752c81a5a27502b76efcc09ef01cfbe777a9e8086)、[IMG_MGMT_ERR_VERSION_GET_FAILED](#gga669286d96816e0e99792f407752c81a5ae710879342357f27c9705989f572b82f)、[IMG_MGMT_ERR_CURRENT_VERSION_IS_NEWER](#gga669286d96816e0e99792f407752c81a5a37ad5efbaacdcb708a65674a4dc83d85)、[IMG_MGMT_ERR_IMAGE_ALREADY_PENDING](#gga669286d96816e0e99792f407752c81a5af55239776b4b5a5eead0440fb3b884b3)、[IMG_MGMT_ERR_INVALID_IMAGE_VECTOR_TABLE](#gga669286d96816e0e99792f407752c81a5a3a8d3005c72273ee065c34396d3fd2f7)、[IMG_MGMT_ERR_INVALID_IMAGE_TOO_LARGE](#gga669286d96816e0e99792f407752c81a5ab258cd53a5cc13e2376662690703f54b)、[IMG_MGMT_ERR_INVALID_IMAGE_DATA_OVERRUN](#gga669286d96816e0e99792f407752c81a5a92ab3773cdbd00b42fb59865e958069b)、[IMG_MGMT_ERR_IMAGE_CONFIRMATION_DENIED](#gga669286d96816e0e99792f407752c81a5ae2413b0ade3185b91ae085af397adabf)、[IMG_MGMT_ERR_IMAGE_SETTING_TEST_TO_ACTIVE_DENIED](#gga669286d96816e0e99792f407752c81a5ab195578794ddc6cffa5e056ee34350a8)、[IMG_MGMT_ERR_ACTIVE_SLOT_NOT_KNOWN](#gga669286d96816e0e99792f407752c81a5a3220405113525f3d5af068b8bf2a80f6)。

镜像管理组（Image Management Group）的命令结果码。

<a id="r_ga1d239fef127e65b11b71360eadfa1ede"></a>

```c
enum img_mgmt_id_upload_t { IMG_MGMT_ID_UPLOAD_STATUS_START = 0 , IMG_MGMT_ID_UPLOAD_STATUS_ONGOING , IMG_MGMT_ID_UPLOAD_STATUS_COMPLETE }
```

相关声明：[img_mgmt_id_upload_t](#ga1d239fef127e65b11b71360eadfa1ede)、[IMG_MGMT_ID_UPLOAD_STATUS_START](#gga1d239fef127e65b11b71360eadfa1edeaff49286e379bd39781a563c1e52c6c8c)、[IMG_MGMT_ID_UPLOAD_STATUS_ONGOING](#gga1d239fef127e65b11b71360eadfa1edea7cf567b16af18752316fde6444e23a21)、[IMG_MGMT_ID_UPLOAD_STATUS_COMPLETE](#gga1d239fef127e65b11b71360eadfa1edeab106874625a50d626e55130e91d37bf2)。

IMG_MGMT_ID_UPLOAD 状态（Statuses）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.6\_函数（Functions）

<a id="r_ga60ae88823a561160b1ddc406382e4ac3"></a>

```c
int img_mgmt_read_info (int image_slot, struct image_version *ver, uint8_t *hash, uint32_t *flags)
```

相关声明：[img_mgmt_read_info](#ga60ae88823a561160b1ddc406382e4ac3)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_gae9cfa02e5f171d68287cdb0d7d4c0610"></a>

```c
int img_mgmt_my_version (struct image_version *ver)
```

相关声明：[img_mgmt_my_version](#gae9cfa02e5f171d68287cdb0d7d4c0610)。

获取当前运行应用的镜像版本（Image Version）。

<a id="r_ga5199849b6d8847c6a1260254940db95b"></a>

```c
int img_mgmt_ver_str (const struct image_version *ver, char *dst)
```

相关声明：[img_mgmt_ver_str](#ga5199849b6d8847c6a1260254940db95b)。

根据 struct image_version 格式化版本字符串（Version String）。

<a id="r_gab35c8adf2e5e2c941ecbaf3c03101e55"></a>

```c
int img_mgmt_active_slot (int image)
```

相关声明：[img_mgmt_active_slot](#gab35c8adf2e5e2c941ecbaf3c03101e55)。

获取指定镜像当前活动且正在运行的应用槽位编号（Slot Number）。

<a id="r_gab6a92433b859fce18b58e6110fa5f489"></a>

```c
int img_mgmt_active_image (void)
```

相关声明：[img_mgmt_active_image](#gab6a92433b859fce18b58e6110fa5f489)。

获取活动镜像编号（Active Image Number）。

<a id="r_ga90de2da23bcd650ca59219fdfd4f55a1"></a>

```c
int img_mgmt_slot_in_use (int slot)
```

相关声明：[img_mgmt_slot_in_use](#ga90de2da23bcd650ca59219fdfd4f55a1)。

检查镜像槽位（Image Slot）是否正在使用。

<a id="r_ga3e496199d0ea4aa1b3f51e59bb7473f0"></a>

```c
int img_mgmt_state_any_pending (void)
```

相关声明：[img_mgmt_state_any_pending](#ga3e496199d0ea4aa1b3f51e59bb7473f0)。

检查是否有槽位处于 MCUboot 待处理状态（Pending State）。

<a id="r_ga42475389b4e31d5f35ea58873527e948"></a>

```c
uint8_t img_mgmt_state_flags (int query_slot)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[img_mgmt_state_flags](#ga42475389b4e31d5f35ea58873527e948)。

返回为槽位设置的状态标志（State Flags）。

<a id="r_ga7e529fa76ddb3d3bf4a527cb11fa9c89"></a>

```c
int img_mgmt_state_set_pending (int slot, int permanent)
```

相关声明：[img_mgmt_state_set_pending](#ga7e529fa76ddb3d3bf4a527cb11fa9c89)。

设置指定镜像槽位的待处理标志（Pending Flag）。

<a id="r_gaed0b945d2f83daf63d850b232a2cfea8"></a>

```c
int img_mgmt_state_confirm (void)
```

相关声明：[img_mgmt_state_confirm](#gaed0b945d2f83daf63d850b232a2cfea8)。

确认当前镜像状态（Image State）。

<a id="r_ga6c9124cc59c99769908cdf83f58e1bf1"></a>

```c
int img_mgmt_vercmp (const struct image_version *a, const struct image_version *b)
```

相关声明：[img_mgmt_vercmp](#ga6c9124cc59c99769908cdf83f58e1bf1)。

以兼容语义化版本（Semantic Versioning，SemVer）的方式比较两个镜像版本号。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 10.7\_变量（Variables）

<a id="r_ga0d6bb8877516ca486c318fa12c129138"></a>

```c
int boot_current_slot
```

相关声明：[boot_current_slot](#ga0d6bb8877516ca486c318fa12c129138)。

<a id="r_gad3dce7b70ce3338588003a021eec1ab6"></a>

```c
struct img_mgmt_state g_img_mgmt_state
```

相关声明：[img_mgmt_state](../system_service_model_reference/P047_img_mgmt_state_结构体.md)、[g_img_mgmt_state](#gad3dce7b70ce3338588003a021eec1ab6)。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 10.8\_镜像状态标志（Image State Flags）

<a id="r_ga459776db5ce7bbfebae5e74aef4067ef"></a>

```c
#define IMG_MGMT_STATE_F_PENDING 0x01
```

相关声明：[IMG_MGMT_STATE_F_PENDING](#ga459776db5ce7bbfebae5e74aef4067ef)。

已将此镜像设为下次交换（Swap）的对象。

<a id="r_ga581c2626a47ca249ecbcc42edb7a59c2"></a>

```c
#define IMG_MGMT_STATE_F_CONFIRMED 0x02
```

相关声明：[IMG_MGMT_STATE_F_CONFIRMED](#ga581c2626a47ca249ecbcc42edb7a59c2)。

镜像已确认（Confirmed）。

<a id="r_ga2a11cfad9698b0460b846fa079234c03"></a>

```c
#define IMG_MGMT_STATE_F_ACTIVE 0x04
```

相关声明：[IMG_MGMT_STATE_F_ACTIVE](#ga2a11cfad9698b0460b846fa079234c03)。

镜像当前处于活动状态（Active）。

<a id="r_gae47e88131d96901e70b2b67ea43ceb4a"></a>

```c
#define IMG_MGMT_STATE_F_PERMANENT 0x08
```

相关声明：[IMG_MGMT_STATE_F_PERMANENT](#gae47e88131d96901e70b2b67ea43ceb4a)。

镜像将在下次启动后保留在主槽位（Primary Slot）。

## 10.9\_镜像管理状态机的交换类型（Swap Types for Image Management State Machine）

<a id="r_ga55e68ef4a5caa3c68987af438ebe8236"></a>

```c
#define IMG_MGMT_SWAP_TYPE_NONE 0
```

相关声明：[IMG_MGMT_SWAP_TYPE_NONE](#ga55e68ef4a5caa3c68987af438ebe8236)。

不交换（No Swap）。

<a id="r_ga71a0715be72de416f3d4744f4763a241"></a>

```c
#define IMG_MGMT_SWAP_TYPE_TEST 1
```

相关声明：[IMG_MGMT_SWAP_TYPE_TEST](#ga71a0715be72de416f3d4744f4763a241)。

测试交换（Test Swap）。

<a id="r_ga69c51ca39c8d33db392e2353873aac43"></a>

```c
#define IMG_MGMT_SWAP_TYPE_PERM 2
```

相关声明：[IMG_MGMT_SWAP_TYPE_PERM](#ga69c51ca39c8d33db392e2353873aac43)。

永久交换（Permanent Swap）。

<a id="r_ga43a9afd49822eda7b640d3adb9219f10"></a>

```c
#define IMG_MGMT_SWAP_TYPE_REVERT 3
```

相关声明：[IMG_MGMT_SWAP_TYPE_REVERT](#ga43a9afd49822eda7b640d3adb9219f10)。

回退交换（Revert Swap）。

<a id="r_ga35a8dd8ca661f2a602bc04d4ae6361a6"></a>

```c
#define IMG_MGMT_SWAP_TYPE_UNKNOWN 255
```

相关声明：[IMG_MGMT_SWAP_TYPE_UNKNOWN](#ga35a8dd8ca661f2a602bc04d4ae6361a6)。

未知交换（Unknown Swap）。

## 10.10\_镜像管理组命令 ID（Command IDs for Image Management Group）

<a id="r_ga19396c2690a0d40f625792ab644e7d17"></a>

```c
#define IMG_MGMT_ID_STATE 0
```

相关声明：[IMG_MGMT_ID_STATE](#ga19396c2690a0d40f625792ab644e7d17)。

镜像状态（State of Images）。

<a id="r_ga70541d06c76224a631f493023e05a73a"></a>

```c
#define IMG_MGMT_ID_UPLOAD 1
```

相关声明：[IMG_MGMT_ID_UPLOAD](#ga70541d06c76224a631f493023e05a73a)。

镜像上传（Image Upload）。

<a id="r_ga90225baf3e08859f294d9aaaf2012e6b"></a>

```c
#define IMG_MGMT_ID_FILE 2
```

相关声明：[IMG_MGMT_ID_FILE](#ga90225baf3e08859f294d9aaaf2012e6b)。

文件（File）。

<a id="r_ga46e9a83aab777da2591d4c7cb701b5cd"></a>

```c
#define IMG_MGMT_ID_CORELIST 3
```

相关声明：[IMG_MGMT_ID_CORELIST](#ga46e9a83aab777da2591d4c7cb701b5cd)。

核心转储列表（Corelist）。

<a id="r_ga22af869af6cbdde12f2cbc811fe7d443"></a>

```c
#define IMG_MGMT_ID_CORELOAD 4
```

相关声明：[IMG_MGMT_ID_CORELOAD](#ga22af869af6cbdde12f2cbc811fe7d443)。

核心转储加载（Coreload）。

<a id="r_gaf7de4c1d77bc29eea4b3d46382bd954f"></a>

```c
#define IMG_MGMT_ID_ERASE 5
```

相关声明：[IMG_MGMT_ID_ERASE](#gaf7de4c1d77bc29eea4b3d46382bd954f)。

镜像擦除（Image Erase）。

<a id="r_gacb33e3b0729f8621275c6b3dc9795d57"></a>

```c
#define IMG_MGMT_ID_SLOT_INFO 6
```

相关声明：[IMG_MGMT_ID_SLOT_INFO](#gacb33e3b0729f8621275c6b3dc9795d57)。

槽位信息（Slot Info）。

## 10.11\_详细说明（Detailed Documentation）

<a id="ga70168b0d707c15658fd09b02c361a64c"></a>

### `IMG_MGMT_DATA_SHA_LEN`

```c
#define IMG_MGMT_DATA_SHA_LEN 32 /* SHA256 */
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

<a id="ga46e9a83aab777da2591d4c7cb701b5cd"></a>

### `IMG_MGMT_ID_CORELIST`

```c
#define IMG_MGMT_ID_CORELIST 3
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

核心转储列表（Corelist）。

<a id="ga22af869af6cbdde12f2cbc811fe7d443"></a>

### `IMG_MGMT_ID_CORELOAD`

```c
#define IMG_MGMT_ID_CORELOAD 4
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

核心转储加载（Coreload）。

<a id="gaf7de4c1d77bc29eea4b3d46382bd954f"></a>

### `IMG_MGMT_ID_ERASE`

```c
#define IMG_MGMT_ID_ERASE 5
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

镜像擦除（Image Erase）。

<a id="ga90225baf3e08859f294d9aaaf2012e6b"></a>

### `IMG_MGMT_ID_FILE`

```c
#define IMG_MGMT_ID_FILE 2
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

文件（File）。

<a id="gacb33e3b0729f8621275c6b3dc9795d57"></a>

### `IMG_MGMT_ID_SLOT_INFO`

```c
#define IMG_MGMT_ID_SLOT_INFO 6
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

槽位信息（Slot Info）。

<a id="ga19396c2690a0d40f625792ab644e7d17"></a>

### `IMG_MGMT_ID_STATE`

```c
#define IMG_MGMT_ID_STATE 0
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

镜像状态（State of Images）。

<a id="ga70541d06c76224a631f493023e05a73a"></a>

### `IMG_MGMT_ID_UPLOAD`

```c
#define IMG_MGMT_ID_UPLOAD 1
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

镜像上传（Image Upload）。

<a id="ga2a11cfad9698b0460b846fa079234c03"></a>

### `IMG_MGMT_STATE_F_ACTIVE`

```c
#define IMG_MGMT_STATE_F_ACTIVE 0x04
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

镜像当前处于活动状态（Active）。

<a id="ga581c2626a47ca249ecbcc42edb7a59c2"></a>

### `IMG_MGMT_STATE_F_CONFIRMED`

```c
#define IMG_MGMT_STATE_F_CONFIRMED 0x02
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

镜像已确认（Confirmed）。

<a id="ga459776db5ce7bbfebae5e74aef4067ef"></a>

### `IMG_MGMT_STATE_F_PENDING`

```c
#define IMG_MGMT_STATE_F_PENDING 0x01
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

已将此镜像设为下次交换（Swap）的对象。

<a id="gae47e88131d96901e70b2b67ea43ceb4a"></a>

### `IMG_MGMT_STATE_F_PERMANENT`

```c
#define IMG_MGMT_STATE_F_PERMANENT 0x08
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

镜像将在下次启动后保留在主槽位（Primary Slot）。

<a id="ga55e68ef4a5caa3c68987af438ebe8236"></a>

### `IMG_MGMT_SWAP_TYPE_NONE`

```c
#define IMG_MGMT_SWAP_TYPE_NONE 0
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

不交换（No Swap）。

<a id="ga69c51ca39c8d33db392e2353873aac43"></a>

### `IMG_MGMT_SWAP_TYPE_PERM`

```c
#define IMG_MGMT_SWAP_TYPE_PERM 2
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

永久交换（Permanent Swap）。

<a id="ga43a9afd49822eda7b640d3adb9219f10"></a>

### `IMG_MGMT_SWAP_TYPE_REVERT`

```c
#define IMG_MGMT_SWAP_TYPE_REVERT 3
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

回退交换（Revert Swap）。

<a id="ga71a0715be72de416f3d4744f4763a241"></a>

### `IMG_MGMT_SWAP_TYPE_TEST`

```c
#define IMG_MGMT_SWAP_TYPE_TEST 1
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

测试交换（Test Swap）。

<a id="ga35a8dd8ca661f2a602bc04d4ae6361a6"></a>

### `IMG_MGMT_SWAP_TYPE_UNKNOWN`

```c
#define IMG_MGMT_SWAP_TYPE_UNKNOWN 255
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

未知交换（Unknown Swap）。

<a id="gaee07bacea29269e24ca15a2e1716390d"></a>

### `IMG_MGMT_UPLOAD_ACTION_RC_RSN`

```c
#define IMG_MGMT_UPLOAD_ACTION_RC_RSN ( action)
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

展开值（Value）：

```c
NULL
```

<a id="ga56e01e5bfa9fdd9bf6ebdc0dc3ac19ba"></a>

### `IMG_MGMT_UPLOAD_ACTION_SET_RC_RSN`

```c
#define IMG_MGMT_UPLOAD_ACTION_SET_RC_RSN ( action, rsn )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

<a id="ga57a5c429be5a3860981007e9728db181"></a>

### `IMG_MGMT_VER_MAX_STR_LEN`

```c
#define IMG_MGMT_VER_MAX_STR_LEN (sizeof("255.255.65535.4294967295"))
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

<a id="ga669286d96816e0e99792f407752c81a5"></a>

### `img_mgmt_err_code_t`

```c
enum img_mgmt_err_code_t
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

镜像管理组（Image Management Group）的命令结果码。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IMG_MGMT_ERR_OK` | 没有错误；如果响应中没有ret值，就隐含表示此结果。 |
| `IMG_MGMT_ERR_UNKNOWN` | 发生未知错误（Unknown Error）。 |
| `IMG_MGMT_ERR_FLASH_CONFIG_QUERY_FAIL` | 查询闪存区域配置（Flash Area Configuration）失败。 |
| `IMG_MGMT_ERR_NO_IMAGE` | 槽位（Slot）中没有镜像（Image）。 |
| `IMG_MGMT_ERR_NO_TLVS` | 槽位中的镜像没有标签—长度—值条目（TLV，Tag/Length/Value）。 |
| `IMG_MGMT_ERR_INVALID_TLV` | 槽位中的镜像具有无效的 TLV 类型和／或长度。 |
| `IMG_MGMT_ERR_TLV_MULTIPLE_HASHES_FOUND` | 槽位中的镜像包含多个哈希 TLV（Hash TLV），这是无效的。 |
| `IMG_MGMT_ERR_TLV_INVALID_SIZE` | 槽位中的镜像具有无效的 TLV 大小。 |
| `IMG_MGMT_ERR_HASH_NOT_FOUND` | 槽位中的镜像缺少必需的哈希 TLV（Hash TLV）。 |
| `IMG_MGMT_ERR_NO_FREE_SLOT` | 没有可放置镜像（Image）的空闲槽位（Free Slot）。 |
| `IMG_MGMT_ERR_FLASH_OPEN_FAILED` | 打开闪存区域（Flash Area）失败。 |
| `IMG_MGMT_ERR_FLASH_READ_FAILED` | 读取闪存区域（Flash Area）失败。 |
| `IMG_MGMT_ERR_FLASH_WRITE_FAILED` | 写入闪存区域（Flash Area）失败。 |
| `IMG_MGMT_ERR_FLASH_ERASE_FAILED` | 擦除闪存区域（Flash Area）失败。 |
| `IMG_MGMT_ERR_INVALID_SLOT` | 提供的槽位（Slot）无效。 |
| `IMG_MGMT_ERR_NO_FREE_MEMORY` | 堆内存（Heap Memory）不足，`malloc` 失败。 |
| `IMG_MGMT_ERR_FLASH_CONTEXT_ALREADY_SET` | 闪存上下文（Flash Context）已设置。 |
| `IMG_MGMT_ERR_FLASH_CONTEXT_NOT_SET` | 闪存上下文（Flash Context）未设置。 |
| `IMG_MGMT_ERR_FLASH_AREA_DEVICE_NULL` | 闪存区域（Flash Area）对应的设备为 `NULL`。 |
| `IMG_MGMT_ERR_INVALID_PAGE_OFFSET` | 页号（Page Number）对应的偏移量（Offset）无效。 |
| `IMG_MGMT_ERR_INVALID_OFFSET` | 未提供必需的偏移量参数（Offset Parameter）。 |
| `IMG_MGMT_ERR_INVALID_LENGTH` | 未提供必需的长度参数（Length Parameter）。 |
| `IMG_MGMT_ERR_INVALID_IMAGE_HEADER` | 镜像长度（Image Length）小于镜像头（Image Header）的大小。 |
| `IMG_MGMT_ERR_INVALID_IMAGE_HEADER_MAGIC` | 镜像头魔数（Image Header Magic Value）与预期值不匹配。 |
| `IMG_MGMT_ERR_INVALID_HASH` | 提供的哈希参数（Hash Parameter）无效。 |
| `IMG_MGMT_ERR_INVALID_FLASH_ADDRESS` | 镜像加载地址（Image Load Address）与闪存区域（Flash Area）的地址不匹配。 |
| `IMG_MGMT_ERR_VERSION_GET_FAILED` | 获取当前运行应用的版本（Version）失败。 |
| `IMG_MGMT_ERR_CURRENT_VERSION_IS_NEWER` | 当前运行应用的版本比正在上传的版本更新。 |
| `IMG_MGMT_ERR_IMAGE_ALREADY_PENDING` | 已有镜像操作（Image Operation）待处理。 |
| `IMG_MGMT_ERR_INVALID_IMAGE_VECTOR_TABLE` | 镜像向量表（Image Vector Table）无效。 |
| `IMG_MGMT_ERR_INVALID_IMAGE_TOO_LARGE` | 镜像（Image）过大，无法容纳。 |
| `IMG_MGMT_ERR_INVALID_IMAGE_DATA_OVERRUN` | 发送的数据量大于提供的镜像大小（Image Size）。 |
| `IMG_MGMT_ERR_IMAGE_CONFIRMATION_DENIED` | 镜像确认（Image Confirmation）被拒绝。 |
| `IMG_MGMT_ERR_IMAGE_SETTING_TEST_TO_ACTIVE_DENIED` | 不允许将活动槽位（Active Slot）设置为测试（Test）。 |
| `IMG_MGMT_ERR_ACTIVE_SLOT_NOT_KNOWN` | 无法确定镜像当前的活动槽位（Active Slot）。 |

<a id="ga1d239fef127e65b11b71360eadfa1ede"></a>

### `img_mgmt_id_upload_t`

```c
enum img_mgmt_id_upload_t
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

IMG_MGMT_ID_UPLOAD 状态（Statuses）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `IMG_MGMT_ID_UPLOAD_STATUS_START` |  |
| `IMG_MGMT_ID_UPLOAD_STATUS_ONGOING` |  |
| `IMG_MGMT_ID_UPLOAD_STATUS_COMPLETE` |  |

<a id="gab6a92433b859fce18b58e6110fa5f489"></a>

### `img_mgmt_active_image()`

```c
int img_mgmt_active_image ( void )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

获取活动镜像编号（Active Image Number）。

获取正在运行的应用的编号（Number），从 0 开始计数。

**返回（Returns）**：返回值（Returns）：非负的镜像编号（Image Number）。

<a id="gab35c8adf2e5e2c941ecbaf3c03101e55"></a>

### `img_mgmt_active_slot()`

```c
int img_mgmt_active_slot ( int image)
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

获取指定镜像当前活动且正在运行的应用槽位编号（Slot Number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `image` | 要获取其活动槽位（Active Slot）的镜像编号（Image Number）。 |

**返回（Returns）**：返回值（Returns）：非负的槽位编号（Slot Number）。

<a id="gae9cfa02e5f171d68287cdb0d7d4c0610"></a>

### `img_mgmt_my_version()`

```c
int img_mgmt_my_version ( struct image_version * ver)
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

获取当前运行应用的镜像版本（Image Version）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ver` | 用于存储镜像版本信息对象（Image Version Information Object）的输出缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，失败时为非零值。

<a id="ga60ae88823a561160b1ddc406382e4ac3"></a>

### `img_mgmt_read_info()`

```c
int img_mgmt_read_info ( int image_slot, struct image_version * ver, uint8_t * hash, uint32_t * flags )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

<a id="ga90de2da23bcd650ca59219fdfd4f55a1"></a>

### `img_mgmt_slot_in_use()`

```c
int img_mgmt_slot_in_use ( int slot)
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

检查镜像槽位（Image Slot）是否正在使用。

检查依据是 MCUboot 标志（Flags），不是镜像内容。因此，即使槽位内存在镜像，只要未设置可引导标志（Bootable Flags），也会被视为空槽位。活动槽位（Active Slot）始终视为正在使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `slot` | 槽位编号（Slot number）。 |

**返回（Returns）**：返回值（Returns）：槽位（Slot）未使用时为 0，否则为非零值。

<a id="ga3e496199d0ea4aa1b3f51e59bb7473f0"></a>

### `img_mgmt_state_any_pending()`

```c
int img_mgmt_state_any_pending ( void )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

检查是否有槽位处于 MCUboot 待处理状态（Pending State）。

如果槽位 0 或槽位 1 处于 MCUboot 待处理状态（Pending State），函数返回 1；该状态表示镜像已标记为测试（Test）或已确认（Confirmed）。

**返回（Returns）**：返回值（Returns）：存在待处理的设备固件更新（DFU）时为 1，否则为 0。

<a id="gaed0b945d2f83daf63d850b232a2cfea8"></a>

### `img_mgmt_state_confirm()`

```c
int img_mgmt_state_confirm ( void )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

确认当前镜像状态（Image State）。

如果当前正在测试活动镜像（Active Image），则防止下次重新启动时发生回退（Fallback）。

**返回（Returns）**：返回值（Returns）：成功时为 0，失败时为非零值。

<a id="ga42475389b4e31d5f35ea58873527e948"></a>

### `img_mgmt_state_flags()`

```c
uint8_t img_mgmt_state_flags ( int query_slot)
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

返回为槽位设置的状态标志（State Flags）。

这些标志由 MCUboot 镜像状态标志（Image State Flags）转换而来。没有设置标志时返回 0，否则返回以下标志的组合：`IMG_MGMT_STATE_F_PENDING`、`IMG_MGMT_STATE_F_CONFIRMED`、`IMG_MGMT_STATE_F_ACTIVE`、`IMG_MGMT_STATE_F_PERMANENT`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `query_slot` | 槽位编号（Slot number）。 |

**返回（Returns）**：返回值（Returns）：状态标志（State Flags）。

<a id="ga7e529fa76ddb3d3bf4a527cb11fa9c89"></a>

### `img_mgmt_state_set_pending()`

```c
int img_mgmt_state_set_pending ( int slot, int permanent )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

设置指定镜像槽位的待处理标志（Pending Flag）。

将指定镜像槽位（Image Slot）设置为下次引导时使用的活动槽位（Active Slot），可用于测试或永久使用。非永久镜像必须在下次引导期间自行确认（Confirm），否则会被回退（Revert）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `slot` | 槽位编号（Slot number）。 |
| `permanent` | 永久使用（Permanent）或仅用于测试（Test Only）。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，失败时为非零值。

<a id="ga5199849b6d8847c6a1260254940db95b"></a>

### `img_mgmt_ver_str()`

```c
int img_mgmt_ver_str ( const struct image_version * ver, char * dst )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

根据 struct image_version 格式化版本字符串（Version String）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ver` | 指向 `image_version` 对象的指针。 |
| `dst` | 用于存储镜像版本字符串（Image Version String）的输出缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为非负值，出错时为负值。

<a id="ga6c9124cc59c99769908cdf83f58e1bf1"></a>

### `img_mgmt_vercmp()`

```c
int img_mgmt_vercmp ( const struct image_version * a, const struct image_version * b )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

以兼容语义化版本（Semantic Versioning，SemVer）的方式比较两个镜像版本号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 参与比较的第一个版本（Version）。 |
| `b` | 参与比较的第二个版本（Version）。 |

**返回（Returns）**：返回值（Returns）：`a < b` 时为 -1，`a = b` 时为 0，`a > b` 时为 1。

<a id="ga0d6bb8877516ca486c318fa12c129138"></a>

### `boot_current_slot`

```c
int boot_current_slot
```

声明属性：`extern`。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

<a id="gad3dce7b70ce3338588003a021eec1ab6"></a>

### `g_img_mgmt_state`

```c
struct img_mgmt_state g_img_mgmt_state
```

声明属性：`extern`。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```


## 10.12\_原页交叉引用（Cross References）

- [映像管理回调（Image Management Callbacks）](../api_update_memory_topic_reference/P010_映像管理回调（Image Management Callbacks）.md)
- [映像管理客户端（Image Management Client）](../api_input_runtime_topic_reference/P013_映像管理客户端（Image Management Client）.md)
- [img_mgmt.h](../api_file_audio_gateway_reference/P018_zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt.h_文件参考.md)
- [img_mgmt_upload_req](../system_service_model_reference/P051_img_mgmt_upload_req_结构体.md)
- [img_mgmt_state](../system_service_model_reference/P047_img_mgmt_state_结构体.md)
- [img_mgmt_upload_action](../system_service_model_reference/P049_img_mgmt_upload_action_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga669286d96816e0e99792f407752c81a5a7db18fe6cb5913fec882dc515d8bb7a0"></a>
<a id="gga669286d96816e0e99792f407752c81a5a8f1bd00b3e00f070b07269fdddd2c8fe"></a>
<a id="gga669286d96816e0e99792f407752c81a5a5b4301665ef0c9818fcd3174908e5063"></a>
<a id="gga669286d96816e0e99792f407752c81a5a360155fc7e541080a7b80bee6ec9dbb6"></a>
<a id="gga669286d96816e0e99792f407752c81a5a598c03b99a2be60cf4847fa2f32c5d10"></a>
<a id="gga669286d96816e0e99792f407752c81a5a4725027793b17187474089fde35730cb"></a>
<a id="gga669286d96816e0e99792f407752c81a5aced7bb74d51b7dd7ff922cf555722276"></a>
<a id="gga669286d96816e0e99792f407752c81a5a967c4f0b3d33d925e28f076c8cc3ed5c"></a>
<a id="gga669286d96816e0e99792f407752c81a5a5d89dde479611276e6956706ee357c6e"></a>
<a id="gga669286d96816e0e99792f407752c81a5a0d16138a65766047e4917022068832fa"></a>
<a id="gga669286d96816e0e99792f407752c81a5a8253896c206d8f3ba486466555662071"></a>
<a id="gga669286d96816e0e99792f407752c81a5a9a09d73602a77e112a95fa977e9b0355"></a>
<a id="gga669286d96816e0e99792f407752c81a5adf54010236b4e6bb4669cdeeb4a6979f"></a>
<a id="gga669286d96816e0e99792f407752c81a5a869d0aa27c38187fdb73d36397dcef3c"></a>
<a id="gga669286d96816e0e99792f407752c81a5a7c0f0cda8165d0acf5fc2a072a5c5cc5"></a>
<a id="gga669286d96816e0e99792f407752c81a5ab75ac303b054a02e99a0ed9726c988de"></a>
<a id="gga669286d96816e0e99792f407752c81a5af1eac867913981a4d8f1f2d64108706e"></a>
<a id="gga669286d96816e0e99792f407752c81a5a9e4c9f1a79f645130ef9a8aa09b8b544"></a>
<a id="gga669286d96816e0e99792f407752c81a5a6c1c103d76e1f16fda77525ba136e9b2"></a>
<a id="gga669286d96816e0e99792f407752c81a5a857b6ecc22e5f54834638aa604cce6bf"></a>
<a id="gga669286d96816e0e99792f407752c81a5a8a94dfe1aca340c4337fe92554ede4b0"></a>
<a id="gga669286d96816e0e99792f407752c81a5a227b2b3be93cf963ce034b9cb817d0ca"></a>
<a id="gga669286d96816e0e99792f407752c81a5acfdb28d59643e70db86abfa72c2833b7"></a>
<a id="gga669286d96816e0e99792f407752c81a5a5606b72a7bf61832b92c77e729e02093"></a>
<a id="gga669286d96816e0e99792f407752c81a5a4b2994e51eadae6cb43c3683d6e223b6"></a>
<a id="gga669286d96816e0e99792f407752c81a5a27502b76efcc09ef01cfbe777a9e8086"></a>
<a id="gga669286d96816e0e99792f407752c81a5ae710879342357f27c9705989f572b82f"></a>
<a id="gga669286d96816e0e99792f407752c81a5a37ad5efbaacdcb708a65674a4dc83d85"></a>
<a id="gga669286d96816e0e99792f407752c81a5af55239776b4b5a5eead0440fb3b884b3"></a>
<a id="gga669286d96816e0e99792f407752c81a5a3a8d3005c72273ee065c34396d3fd2f7"></a>
<a id="gga669286d96816e0e99792f407752c81a5ab258cd53a5cc13e2376662690703f54b"></a>
<a id="gga669286d96816e0e99792f407752c81a5a92ab3773cdbd00b42fb59865e958069b"></a>
<a id="gga669286d96816e0e99792f407752c81a5ae2413b0ade3185b91ae085af397adabf"></a>
<a id="gga669286d96816e0e99792f407752c81a5ab195578794ddc6cffa5e056ee34350a8"></a>
<a id="gga669286d96816e0e99792f407752c81a5a3220405113525f3d5af068b8bf2a80f6"></a>
<a id="gga1d239fef127e65b11b71360eadfa1edeaff49286e379bd39781a563c1e52c6c8c"></a>
<a id="gga1d239fef127e65b11b71360eadfa1edea7cf567b16af18752316fde6444e23a21"></a>
<a id="gga1d239fef127e65b11b71360eadfa1edeab106874625a50d626e55130e91d37bf2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P009_全球导航卫星系统（GNSS）.md) · [返回大纲](大纲.md) · [下一章](P011_管理（Management）.md)
