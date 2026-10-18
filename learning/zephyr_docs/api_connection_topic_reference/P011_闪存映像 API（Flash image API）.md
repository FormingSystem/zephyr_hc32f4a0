---
id: learning.zephyr-docs.api-connection-topic-reference.page-11
title: 闪存映像 API（Flash image API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_闪存映像 API（Flash image API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

将固件映像写入闪存的抽象层。

<a id="details"></a>

将固件映像写入闪存的抽象层。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

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

## 11.2\_函数（Functions）

<a id="r_ga1b194edcb7e4ae34717d011f08d93e0c"></a>

```c
int flash_img_init_id (struct flash_img_context *ctx, uint8_t area_id)
```

相关声明：[flash_img_init_id](#ga1b194edcb7e4ae34717d011f08d93e0c)、[flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化将映像写入闪存所需的上下文（context）。

<a id="r_gac6d1d7811516493242b318be2ecd82df"></a>

```c
int flash_img_init (struct flash_img_context *ctx)
```

相关声明：[flash_img_init](#gac6d1d7811516493242b318be2ecd82df)、[flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)。

初始化将映像写入闪存所需的上下文（context）。

<a id="r_gac1ef017d400bda921ca894d13126b390"></a>

```c
size_t flash_img_bytes_written (struct flash_img_context *ctx)
```

相关声明：[flash_img_bytes_written](#gac1ef017d400bda921ca894d13126b390)、[flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)。

读取已写入闪存的映像字节数。

<a id="r_gae3cb2d6be9f993bcf5a97931475d9a6d"></a>

```c
int flash_img_buffered_write (struct flash_img_context *ctx, const uint8_t *data, size_t len, bool flush)
```

相关声明：[flash_img_buffered_write](#gae3cb2d6be9f993bcf5a97931475d9a6d)、[flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

处理要写入映像槽位 1（image slot 1）的输入缓冲区。

<a id="r_ga5a025255d8bf4a94f9e8d315d5502e88"></a>

```c
int flash_img_check (struct flash_img_context *ctx, const struct flash_img_check *fic, uint8_t area_id)
```

相关声明：[flash_img_check](#ga5a025255d8bf4a94f9e8d315d5502e88)、[flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

验证闪存区域（flash area）中 `length` 字节的完整性（integrity）。

<a id="r_gaeb242ed3d7654bf94e0dce7d6c24c2a0"></a>

```c
uint8_t flash_img_get_upload_slot (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flash_img_get_upload_slot](#gaeb242ed3d7654bf94e0dce7d6c24c2a0)。

获取映像上传槽位（image upload slot）的闪存区域 ID。

## 11.3\_详细说明（Detailed Documentation）

<a id="gae3cb2d6be9f993bcf5a97931475d9a6d"></a>

### `flash_img_buffered_write()`

```c
int flash_img_buffered_write ( struct flash_img_context * ctx, const uint8_t * data, size_t len, bool flush )
```

```c
#include <zephyr/dfu/flash_img.h>
```

处理要写入映像槽位 1（image slot 1）的输入缓冲区。

按单个块写入闪存（flash memory），在多次调用之间保留尚未写满一块的剩余数据。

最后一次调用此函数时将 `flush` 设为 true，会将块缓冲区中剩余内容写入闪存。由于闪存按块写入，从最后一个已写字节之后直到下一个 `CONFIG_IMG_BLOCK_BUF_SIZE` 整数倍边界的区域，以 `0xff` 填充。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 上下文。 |
| `data` | 要写入的数据。 |
| `len` | 要写入的字节数。 |
| `flush` | 为true时，强制将所有已缓存的数据写入Flash。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="gac1ef017d400bda921ca894d13126b390"></a>

### `flash_img_bytes_written()`

```c
size_t flash_img_bytes_written ( struct flash_img_context * ctx)
```

```c
#include <zephyr/dfu/flash_img.h>
```

读取已写入闪存的映像字节数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 上下文。 |

**返回（Returns）**：返回值：已写入映像闪存的字节数。

<a id="ga5a025255d8bf4a94f9e8d315d5502e88"></a>

### `flash_img_check()`

```c
int flash_img_check ( struct flash_img_context * ctx, const struct flash_img_check * fic, uint8_t area_id )
```

```c
#include <zephyr/dfu/flash_img.h>
```

验证闪存区域（flash area）中 `length` 字节的完整性（integrity）。

起始位置由偏移值（offset）指定。

通过 Kconfig 选项 `CONFIG_IMG_ENABLE_IMAGE_CHECK` 启用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ctx` | 上下文。 |
| `[in] fic` | 闪存映像检查数据（flash image check data）。 |
| `[in] area_id` | 待验证映像所在分区的闪存区域 ID（flash area ID）。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="gaeb242ed3d7654bf94e0dce7d6c24c2a0"></a>

### `flash_img_get_upload_slot()`

```c
uint8_t flash_img_get_upload_slot ( void )
```

```c
#include <zephyr/dfu/flash_img.h>
```

获取映像上传槽位（image upload slot）的闪存区域 ID。

**返回（Returns）**：返回值：映像上传槽位的闪存区域 ID。

<a id="gac6d1d7811516493242b318be2ecd82df"></a>

### `flash_img_init()`

```c
int flash_img_init ( struct flash_img_context * ctx)
```

```c
#include <zephyr/dfu/flash_img.h>
```

初始化将映像写入闪存所需的上下文（context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 待初始化的上下文。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="ga1b194edcb7e4ae34717d011f08d93e0c"></a>

### `flash_img_init_id()`

```c
int flash_img_init_id ( struct flash_img_context * ctx, uint8_t area_id )
```

```c
#include <zephyr/dfu/flash_img.h>
```

初始化将映像写入闪存所需的上下文（context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 待初始化的上下文。 |
| `area_id` | 待写入映像所在分区的闪存区域 ID。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。


## 11.4\_原页交叉引用（Cross References）

- [flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)
- [flash_img_check](../system_service_model_reference/P028_flash_img_check_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/dfu/flash_img.h](../api_file_management_reference/P014_zephyr__dfu__flash_img.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_OpenISA RV32M1中断多路复用器（INTMUX）.md) · [返回大纲](大纲.md) · [下一章](P012_LPS22HH API主题.md)
