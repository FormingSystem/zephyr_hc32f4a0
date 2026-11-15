---
id: learning.zephyr-docs.api-file-system-device-reference.page-15
title: zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt_client.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_img\_mgmt\_\_img\_mgmt\_client.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr映像管理客户端（Image Management Client）API的头文件。

<a id="details"></a>

```c
#include <inttypes.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h>
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
```

查看此文件的源码。

MCUmgr映像管理客户端（Image Management Client）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_mcumgr_5Fimage_5Flist_5Fflags"></a>

```c
struct mcumgr_image_list_flags
```

相关声明：[mcumgr_image_list_flags](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md)。

映像列表标志（Image List Flags）。

<a id="r_mcumgr_5Fimage_5Fdata"></a>

```c
struct mcumgr_image_data
```

相关声明：[mcumgr_image_data](../system_service_model_reference/P061_mcumgr_image_data_结构体.md)。

映像列表数据（Image List Data）。

<a id="r_mcumgr_5Fimage_5Fstate"></a>

```c
struct mcumgr_image_state
```

相关声明：[mcumgr_image_state](../system_service_model_reference/P063_mcumgr_image_state_结构体.md)。

MCUmgr的映像列表响应（Image List Response）。

<a id="r_mcumgr_5Fimage_5Fupload"></a>

```c
struct mcumgr_image_upload
```

相关声明：[mcumgr_image_upload](../system_service_model_reference/P064_mcumgr_image_upload_结构体.md)。

MCUmgr的映像上传响应（Image Upload Response）。

<a id="r_img_5Fgr_5Fupload"></a>

```c
struct img_gr_upload
```

相关声明：[img_gr_upload](../system_service_model_reference/P042_img_gr_upload_结构体.md)。

映像管理（IMG Management）客户端的上传结构。

<a id="r_img_5Fmgmt_5Fclient"></a>

```c
struct img_mgmt_client
```

相关声明：[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)。

映像管理（IMG Management）客户端对象。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ga96a605c7a4f46851eced1d538f3134b6"></a>

```c
#define IMG_MGMT_CLIENT_HASH_MAX_LEN 64
```

相关声明：[IMG_MGMT_CLIENT_HASH_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga96a605c7a4f46851eced1d538f3134b6)。

支持的最大映像摘要长度（image digest length）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.3\_函数（Functions）

<a id="r_ga1c21618818b5b058e28bdd32360e3838"></a>

```c
void img_mgmt_client_init (struct img_mgmt_client *client, struct smp_client_object *smp_client, int image_list_size, struct mcumgr_image_data *image_list)
```

相关声明：[img_mgmt_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga1c21618818b5b058e28bdd32360e3838)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)、[mcumgr_image_data](../system_service_model_reference/P061_mcumgr_image_data_结构体.md)。

初始化映像管理组客户端（image group client）。

<a id="r_ga99dccccacad33c5e7f91043b483a3884"></a>

```c
int img_mgmt_client_upload_init (struct img_mgmt_client *client, size_t image_size, uint32_t image_num, const char *image_hash)
```

相关声明：[img_mgmt_client_upload_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga99dccccacad33c5e7f91043b483a3884)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化映像上传（image upload）。

<a id="r_ga55fddd1f53765ce25e4285e45714ebc1"></a>

```c
int img_mgmt_client_upload (struct img_mgmt_client *client, const uint8_t *data, size_t length, struct mcumgr_image_upload *res_buf)
```

相关声明：[img_mgmt_client_upload](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga55fddd1f53765ce25e4285e45714ebc1)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mcumgr_image_upload](../system_service_model_reference/P064_mcumgr_image_upload_结构体.md)。

上传映像的一部分。

<a id="r_gab98286b3baac7330c7f42539d38663cd"></a>

```c
int img_mgmt_client_state_write (struct img_mgmt_client *client, const char *hash, size_t hash_len, bool confirm, struct mcumgr_image_state *res_buf)
```

相关声明：[img_mgmt_client_state_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#gab98286b3baac7330c7f42539d38663cd)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mcumgr_image_state](../system_service_model_reference/P063_mcumgr_image_state_结构体.md)。

写入映像状态（image state）。

<a id="r_gad1937b33597ddd012fc7d1fd04cf17f8"></a>

```c
int img_mgmt_client_state_read (struct img_mgmt_client *client, struct mcumgr_image_state *res_buf)
```

相关声明：[img_mgmt_client_state_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#gad1937b33597ddd012fc7d1fd04cf17f8)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[mcumgr_image_state](../system_service_model_reference/P063_mcumgr_image_state_结构体.md)。

读取映像状态。

<a id="r_ga27ca742a8fc5fc3a96510d73fa85a7a3"></a>

```c
int img_mgmt_client_erase (struct img_mgmt_client *client, uint32_t slot)
```

相关声明：[img_mgmt_client_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga27ca742a8fc5fc3a96510d73fa85a7a3)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

擦除所选映像槽位（Image Slot）。


## 15.4\_原页交叉引用（Cross References）

- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h_source.html)
- [zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h](../api_source_reference/P522_mgmt_defines.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h](../api_source_network_reference/P011_img_mgmt.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/smp/smp_client.h](../api_source_reference/P795_smp_client.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P348_img_mgmt_client.h_源码浏览.md)
- [mcumgr_image_list_flags](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md)
- [mcumgr_image_data](../system_service_model_reference/P061_mcumgr_image_data_结构体.md)
- [mcumgr_image_state](../system_service_model_reference/P063_mcumgr_image_state_结构体.md)
- [mcumgr_image_upload](../system_service_model_reference/P064_mcumgr_image_upload_结构体.md)
- [img_gr_upload](../system_service_model_reference/P042_img_gr_upload_结构体.md)
- [img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)
- [IMG_MGMT_CLIENT_HASH_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga96a605c7a4f46851eced1d538f3134b6)
- [img_mgmt_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga1c21618818b5b058e28bdd32360e3838)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [img_mgmt_client_upload_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga99dccccacad33c5e7f91043b483a3884)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [img_mgmt_client_upload](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga55fddd1f53765ce25e4285e45714ebc1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [img_mgmt_client_state_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#gab98286b3baac7330c7f42539d38663cd)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [img_mgmt_client_state_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#gad1937b33597ddd012fc7d1fd04cf17f8)
- [img_mgmt_client_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga27ca742a8fc5fc3a96510d73fa85a7a3)

<a id="header-details"></a>

---

[上一章](P014_zephyr__dt-bindings__clock__ifx_clock_source_psc3xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__dt-bindings__clock__imx_ccm.h_文件参考.md)
