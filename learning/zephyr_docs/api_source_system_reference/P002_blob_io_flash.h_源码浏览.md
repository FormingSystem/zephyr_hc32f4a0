---
id: learning.zephyr-docs.api-source-system-reference.page-2
title: blob_io_flash.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/blob__io__flash_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_blob\_io\_flash.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/blob__io__flash_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_supplement_reference/P009_zephyr__bluetooth__mesh__blob_io_flash.h_文件参考.md)。

## 2.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00027"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="agroup__bt__mesh__blob__io__flash_html_ga8d99fd3dc35230447f7e7ef9f2c4bc81"></a>
<a id="agroup__bt__mesh__blob_html_ga2618fb7365f180a73a7eecd11cf2f962"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__mesh__blob__io__flash_html"></a>
<a id="astructbt__mesh__blob__io__flash_html_a24abc17719dd627e3e3d7c8e61d4c96f"></a>
<a id="astructbt__mesh__blob__io__flash_html_a3b506d86d9cc7fb7206f96cbdd2cd3fe"></a>
<a id="astructbt__mesh__blob__io__flash_html_a511648b9e653993aee99eda5efe3b1e9"></a>
<a id="astructbt__mesh__blob__io__flash_html_a99227cd93d2b6230be7bd5cef9fb8232"></a>
<a id="astructbt__mesh__blob__io__flash_html_ac4eb40a7e53adce60c2fcd11eb0b6b57"></a>
<a id="astructbt__mesh__blob__io_html"></a>
<a id="astructflash__area_html"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_IO_FLASH_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_IO_FLASH_H__

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif


struct bt_mesh_blob_io_flash {
        uint8_t area_id;
        enum bt_mesh_blob_io_mode mode;
        off_t offset;


        /* Internal flash area pointer. */
        const struct flash_area *area;
        /* BLOB stream. */
        struct bt_mesh_blob_io io;

#if defined(CONFIG_BT_MESH_BLOB_IO_FLASH_BLOCK_CACHE)
        /* Block cache used when CONFIG_BT_MESH_BLOB_IO_FLASH_BLOCK_CACHE is set.
         * Received chunks are accumulated here by block-relative offset, and the
         * whole block is programmed write-block-aligned, exactly once, by the
         * wr() call that completes the block. This prevents re-programming a
         * write block that is shared by two adjacent chunks, which would corrupt
         * the ECC syndrome on flash that allows only one program per erase.
         */
        /* Staging buffer for the current block. */
        uint8_t block_buf[CONFIG_BT_MESH_BLOB_BLOCK_SIZE_MAX];
        /* Number of valid bytes received into block_buf for the current block;
         * reaches the block size when the block is complete and gets flushed.
         */
        size_t received;
        /* Sticky error: set when a block flush fails, so that no later wr() can
         * re-program a write block. Cleared only in io_open (NOT block_start,
         * which does not always erase); a failed flush latches for the rest of
         * the stream and the whole transfer fails.
         */
        bool block_err;
#endif /* CONFIG_BT_MESH_BLOB_IO_FLASH_BLOCK_CACHE */
};

int bt_mesh_blob_io_flash_init(struct bt_mesh_blob_io_flash *flash,
                               uint8_t area_id, off_t offset);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_IO_FLASH_H__ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 38 行

内部闪存区域指针（Internal Flash Area Pointer）。

### 注释 3：原第 40 行

二进制大对象流（BLOB Stream）。

### 注释 4：原第 44 行

启用 `CONFIG_BT_MESH_BLOB_IO_FLASH_BLOCK_CACHE` 时使用的块缓存（Block Cache）。接收的数据分块（Chunks）按照块内相对偏移（Block-Relative Offset）积累于此；收到整个块后，由补全该块的那次 `wr()` 调用按写块边界对齐（Write-Block-Aligned），且仅编程一次。这样可以避免对相邻两个数据分块共用的写块重复编程；对于每次擦除后仅允许编程一次的闪存，重复编程会破坏纠错码校验信息（ECC Syndrome）。

### 注释 5：原第 51 行

当前块（Current Block）的暂存缓冲区（Staging Buffer）。

### 注释 6：原第 53 行

当前块接收到 `block_buf` 中的有效字节数（Valid Bytes）。块完整时达到块大小，随后被刷写（Flushed）。

### 注释 7：原第 57 行

粘滞错误（Sticky Error）：块刷写失败时置位，防止后续 `wr()` 再次对写块编程。仅在 `io_open` 中清除，不能在 `block_start` 中清除，因为后者并非总会擦除。刷写失败状态在该数据流剩余期间持续锁存（Latched），导致整个传输失败。

### 注释 8：原第 63 行

条件编译配置（Configuration）标记：`CONFIG_BT_MESH_BLOB_IO_FLASH_BLOCK_CACHE`。

### 注释 9：原第 83 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_IO_FLASH_H__`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_supplement_reference/P009_zephyr__bluetooth__mesh__blob_io_flash.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [bt_mesh_blob_io_flash](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [area_id](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md#a3b506d86d9cc7fb7206f96cbdd2cd3fe)
- [bt_mesh_blob_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga2618fb7365f180a73a7eecd11cf2f962)
- [mode](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md#a511648b9e653993aee99eda5efe3b1e9)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [offset](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md#ac4eb40a7e53adce60c2fcd11eb0b6b57)
- [flash_area](../system_service_model_reference/P027_flash_area_结构体.md)
- [area](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md#a99227cd93d2b6230be7bd5cef9fb8232)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [io](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md#a24abc17719dd627e3e3d7c8e61d4c96f)
- [bt_mesh_blob_io_flash_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__io__flash.html#ga8d99fd3dc35230447f7e7ef9f2c4bc81)
- [bt_mesh_blob_io_flash::io](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md#a24abc17719dd627e3e3d7c8e61d4c96f)
- [bt_mesh_blob_io_flash::area_id](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md#a3b506d86d9cc7fb7206f96cbdd2cd3fe)
- [bt_mesh_blob_io_flash::mode](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md#a511648b9e653993aee99eda5efe3b1e9)
- [bt_mesh_blob_io_flash::area](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md#a99227cd93d2b6230be7bd5cef9fb8232)
- [bt_mesh_blob_io_flash::offset](../bluetooth_mesh_model_reference/P008_bt_mesh_blob_io_flash_结构体.md#ac4eb40a7e53adce60c2fcd11eb0b6b57)

---

[上一章](P001_att.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_bluetooth.h_源码浏览.md)
