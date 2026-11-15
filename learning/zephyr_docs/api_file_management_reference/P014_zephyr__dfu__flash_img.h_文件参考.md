---
id: learning.zephyr-docs.api-file-management-reference.page-14
title: zephyr__dfu__flash_img.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/flash__img_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_dfu\_\_flash\_img.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/flash__img_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

闪存映像（Flash Image）的头文件。

<a id="details"></a>

```c
#include <zephyr/storage/stream_flash.h>
```

查看此文件的源码。

闪存映像头文件（Flash image header file）。声明设备固件升级（DFU）所用闪存映像 API 的函数原型。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_flash_5Fimg_5Fcontext"></a>

```c
struct flash_img_context
```

相关声明：[flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)。

<a id="r_flash_5Fimg_5Fcheck"></a>

```c
struct flash_img_check
```

相关声明：[flash_img_check](../system_service_model_reference/P028_flash_img_check_结构体.md)。

用于验证闪存区域完整性（Flash Region Integrity）的结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.2\_函数（Functions）

<a id="r_ga1b194edcb7e4ae34717d011f08d93e0c"></a>

```c
int flash_img_init_id (struct flash_img_context *ctx, uint8_t area_id)
```

相关声明：[flash_img_init_id](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#ga1b194edcb7e4ae34717d011f08d93e0c)、[flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化将映像写入闪存所需的上下文（context）。

<a id="r_gac6d1d7811516493242b318be2ecd82df"></a>

```c
int flash_img_init (struct flash_img_context *ctx)
```

相关声明：[flash_img_init](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gac6d1d7811516493242b318be2ecd82df)、[flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)。

初始化将映像写入闪存所需的上下文（context）。

<a id="r_gac1ef017d400bda921ca894d13126b390"></a>

```c
size_t flash_img_bytes_written (struct flash_img_context *ctx)
```

相关声明：[flash_img_bytes_written](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gac1ef017d400bda921ca894d13126b390)、[flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)。

读取已写入闪存的映像字节数。

<a id="r_gae3cb2d6be9f993bcf5a97931475d9a6d"></a>

```c
int flash_img_buffered_write (struct flash_img_context *ctx, const uint8_t *data, size_t len, bool flush)
```

相关声明：[flash_img_buffered_write](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gae3cb2d6be9f993bcf5a97931475d9a6d)、[flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

处理要写入映像槽位 1（image slot 1）的输入缓冲区。

<a id="r_ga5a025255d8bf4a94f9e8d315d5502e88"></a>

```c
int flash_img_check (struct flash_img_context *ctx, const struct flash_img_check *fic, uint8_t area_id)
```

相关声明：[flash_img_check](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#ga5a025255d8bf4a94f9e8d315d5502e88)、[flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

验证闪存区域（flash area）中 `length` 字节的完整性（integrity）。

<a id="r_gaeb242ed3d7654bf94e0dce7d6c24c2a0"></a>

```c
uint8_t flash_img_get_upload_slot (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flash_img_get_upload_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gaeb242ed3d7654bf94e0dce7d6c24c2a0)。

获取映像上传槽位（image upload slot）的闪存区域 ID。


## 14.3\_原页交叉引用（Cross References）

- [zephyr/storage/stream_flash.h](../stream_flash_reference/P002_流式Flash头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P264_flash_img.h_源码浏览.md)
- [flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)
- [flash_img_check](../system_service_model_reference/P028_flash_img_check_结构体.md)
- [flash_img_init_id](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#ga1b194edcb7e4ae34717d011f08d93e0c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flash_img_init](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gac6d1d7811516493242b318be2ecd82df)
- [flash_img_bytes_written](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gac1ef017d400bda921ca894d13126b390)
- [flash_img_buffered_write](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gae3cb2d6be9f993bcf5a97931475d9a6d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [flash_img_check](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#ga5a025255d8bf4a94f9e8d315d5502e88)
- [flash_img_get_upload_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gaeb242ed3d7654bf94e0dce7d6c24c2a0)

<a id="header-details"></a>

---

[上一章](P013_zephyr__dt-bindings__sent__sent.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt.h_文件参考.md)
