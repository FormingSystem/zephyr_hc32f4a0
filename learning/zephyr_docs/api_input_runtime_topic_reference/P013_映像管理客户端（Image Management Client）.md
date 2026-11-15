---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-13
title: 映像管理客户端（Image Management Client）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_映像管理客户端（Image Management Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 映像管理客户端 API

<a id="details"></a>

MCUmgr 映像管理客户端 API

<a id="header-files"></a>
<a id="files"></a>

## 13.1\_文件（Files）

<a id="r_img_5Fmgmt_5Fclient_2Eh"></a>

```c
file img_mgmt_client.h
```

相关声明：[img_mgmt_client.h](../api_file_system_device_reference/P015_zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt_client.h_文件参考.md)。

MCUmgr映像管理客户端（Image Management Client）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.2\_数据结构（Data Structures）

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

## 13.3\_宏定义（Macros）

<a id="r_ga96a605c7a4f46851eced1d538f3134b6"></a>

```c
#define IMG_MGMT_CLIENT_HASH_MAX_LEN 64
```

相关声明：[IMG_MGMT_CLIENT_HASH_MAX_LEN](#ga96a605c7a4f46851eced1d538f3134b6)。

支持的最大映像摘要长度（image digest length）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.4\_函数（Functions）

<a id="r_ga1c21618818b5b058e28bdd32360e3838"></a>

```c
void img_mgmt_client_init (struct img_mgmt_client *client, struct smp_client_object *smp_client, int image_list_size, struct mcumgr_image_data *image_list)
```

相关声明：[img_mgmt_client_init](#ga1c21618818b5b058e28bdd32360e3838)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)、[mcumgr_image_data](../system_service_model_reference/P061_mcumgr_image_data_结构体.md)。

初始化映像管理组客户端（image group client）。

<a id="r_ga99dccccacad33c5e7f91043b483a3884"></a>

```c
int img_mgmt_client_upload_init (struct img_mgmt_client *client, size_t image_size, uint32_t image_num, const char *image_hash)
```

相关声明：[img_mgmt_client_upload_init](#ga99dccccacad33c5e7f91043b483a3884)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化映像上传（image upload）。

<a id="r_ga55fddd1f53765ce25e4285e45714ebc1"></a>

```c
int img_mgmt_client_upload (struct img_mgmt_client *client, const uint8_t *data, size_t length, struct mcumgr_image_upload *res_buf)
```

相关声明：[img_mgmt_client_upload](#ga55fddd1f53765ce25e4285e45714ebc1)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mcumgr_image_upload](../system_service_model_reference/P064_mcumgr_image_upload_结构体.md)。

上传映像的一部分。

<a id="r_gab98286b3baac7330c7f42539d38663cd"></a>

```c
int img_mgmt_client_state_write (struct img_mgmt_client *client, const char *hash, size_t hash_len, bool confirm, struct mcumgr_image_state *res_buf)
```

相关声明：[img_mgmt_client_state_write](#gab98286b3baac7330c7f42539d38663cd)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mcumgr_image_state](../system_service_model_reference/P063_mcumgr_image_state_结构体.md)。

写入映像状态（image state）。

<a id="r_gad1937b33597ddd012fc7d1fd04cf17f8"></a>

```c
int img_mgmt_client_state_read (struct img_mgmt_client *client, struct mcumgr_image_state *res_buf)
```

相关声明：[img_mgmt_client_state_read](#gad1937b33597ddd012fc7d1fd04cf17f8)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[mcumgr_image_state](../system_service_model_reference/P063_mcumgr_image_state_结构体.md)。

读取映像状态。

<a id="r_ga27ca742a8fc5fc3a96510d73fa85a7a3"></a>

```c
int img_mgmt_client_erase (struct img_mgmt_client *client, uint32_t slot)
```

相关声明：[img_mgmt_client_erase](#ga27ca742a8fc5fc3a96510d73fa85a7a3)、[img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

擦除所选映像槽位（Image Slot）。

## 13.5\_详细说明（Detailed Documentation）

<a id="ga96a605c7a4f46851eced1d538f3134b6"></a>

### `IMG_MGMT_CLIENT_HASH_MAX_LEN`

```c
#define IMG_MGMT_CLIENT_HASH_MAX_LEN 64
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

支持的最大映像摘要长度（image digest length）。

镜像列表响应（Image List Response）可包含 SHA-256（32 字节）或 SHA-512（64 字节）摘要（Digest），取决于目标的 MCUboot 配置。

**说明（Note）**：**注意（Note）：**与 `IMG_MGMT_DATA_SHA_LEN` 不同，此值不表示镜像上传固定使用的 SHA-256 摘要长度（Digest Length）。

<a id="ga27ca742a8fc5fc3a96510d73fa85a7a3"></a>

### `img_mgmt_client_erase()`

```c
int img_mgmt_client_erase ( struct img_mgmt_client * client, uint32_t slot )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

擦除所选映像槽位（Image Slot）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 映像管理（IMG Management）客户端对象。 |
| `slot` | 槽位编号（Slot number）。 |

返回（Returns）：成功时为 0；失败时为 `mcumgr_err_t` 错误码。

<a id="ga1c21618818b5b058e28bdd32360e3838"></a>

### `img_mgmt_client_init()`

```c
void img_mgmt_client_init ( struct img_mgmt_client * client, struct smp_client_object * smp_client, int image_list_size, struct mcumgr_image_data * image_list )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

初始化映像管理组客户端（image group client）。

使用给定镜像数据（Image Data），为指定 SMP 客户端初始化镜像组客户端（Image Group Client）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 映像管理（IMG Management）客户端对象。 |
| `smp_client` | 简单管理协议（SMP）的客户端对象。 |
| `image_list_size` | `image_list` 缓冲区长度（Buffer Length）。 |
| `image_list` | 镜像列表缓冲区指针（Image List Buffer Pointer）。 |

<a id="gad1937b33597ddd012fc7d1fd04cf17f8"></a>

### `img_mgmt_client_state_read()`

```c
int img_mgmt_client_state_read ( struct img_mgmt_client * client, struct mcumgr_image_state * res_buf )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

读取映像状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 映像管理（IMG Management）客户端对象。 |
| `res_buf` | 指向命令响应结构体（Command Response Structure）的指针。 |

返回（Returns）：成功时为 0；失败时为 `mcumgr_err_t` 错误码。

<a id="gab98286b3baac7330c7f42539d38663cd"></a>

### `img_mgmt_client_state_write()`

```c
int img_mgmt_client_state_write ( struct img_mgmt_client * client, const char * hash, size_t hash_len, bool confirm, struct mcumgr_image_state * res_buf )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

写入映像状态（image state）。

向目标发送镜像状态写入请求（Image State Write Request）。通过摘要（Digest）选择镜像，摘要必须与 `img_mgmt_client_state_read` 报告的散列值匹配。依据目标配置，可使用 SHA-256 或 SHA-512。

请求的操作取决于 `hash` 和 `confirm`：

- `hash` 非 `NULL` 且 `confirm` 为 `false` 时，将所选镜像标记为测试（Test）。依据 MCUboot 模式，镜像将在下次启动时交换进入或被选中；除非后续确认，否则仍可回退（Revert）。
- `hash` 非 `NULL` 且 `confirm` 为 `true` 时，请求确认所选镜像。目标可拒绝确认非活动镜像（Non-active Image）。
- `hash` 为 `NULL` 且 `confirm` 为 `true` 时，确认当前活动镜像（Active Image）。
- `hash` 为 `NULL` 且 `confirm` 为 `false` 时，请求无效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 映像管理（IMG Management）客户端对象。 |
| `hash` | 用于选择目标镜像的摘要（Image Digest）。设为 `NULL` 表示选择当前活动镜像，仅当 `confirm` 为 `true` 时有效。 |
| `hash_len` | `hash` 的字节长度：SHA-256 为 `32`，SHA-512 为 `64`。`hash` 为 `NULL` 时设为 `0`。 |
| `confirm` | `false` 表示测试镜像（Test Image），`true` 表示确认镜像（Confirm Image）。 |
| `res_buf` | 命令响应结构体（Command Response Structure）。请求成功时，将目标返回的镜像状态存储在此。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求已成功完成（Completed Successfully）。 |

**返回（Returns）**：**返回值（Returns）：**失败时返回 `mcumgr_err_t` 错误码。

<a id="ga55fddd1f53765ce25e4285e45714ebc1"></a>

### `img_mgmt_client_upload()`

```c
int img_mgmt_client_upload ( struct img_mgmt_client * client, const uint8_t * data, size_t length, struct mcumgr_image_upload * res_buf )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

上传映像的一部分。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 映像管理（IMG Management）客户端对象。 |
| `data` | 数据指针。 |
| `length` | 数据长度。 |
| `res_buf` | 指向命令响应结构体（Command Response Structure）的指针。 |

返回（Returns）：成功时为 0；失败时为 `mcumgr_err_t` 错误码。

<a id="ga99dccccacad33c5e7f91043b483a3884"></a>

### `img_mgmt_client_upload_init()`

```c
int img_mgmt_client_upload_init ( struct img_mgmt_client * client, size_t image_size, uint32_t image_num, const char * image_hash )
```

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

初始化映像上传（image upload）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 映像管理（IMG Management）客户端对象。 |
| `image_size` | 镜像大小（Image Size），单位为字节。 |
| `image_num` | 镜像槽编号（Image Slot Number）。 |
| `image_hash` | 指向镜像散列值（HASH）的指针；若提供，必须是整个上传内容的 SHA-256 散列值（32 字节）。无法获取镜像 HASH 时使用 `NULL`。 |

返回（Returns）：成功时为 0；失败时为 `mcumgr_err_t` 错误码。


## 13.6\_原页交叉引用（Cross References）

- [img_mgmt_client.h](../api_file_system_device_reference/P015_zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt_client.h_文件参考.md)
- [mcumgr_image_list_flags](../system_service_model_reference/P062_mcumgr_image_list_flags_结构体.md)
- [mcumgr_image_data](../system_service_model_reference/P061_mcumgr_image_data_结构体.md)
- [mcumgr_image_state](../system_service_model_reference/P063_mcumgr_image_state_结构体.md)
- [mcumgr_image_upload](../system_service_model_reference/P064_mcumgr_image_upload_结构体.md)
- [img_gr_upload](../system_service_model_reference/P042_img_gr_upload_结构体.md)
- [img_mgmt_client](../system_service_model_reference/P043_img_mgmt_client_结构体.md)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_BBC micro_bit显示（Display）的API。.md) · [返回大纲](大纲.md) · [下一章](P014_线程（Threads）.md)
