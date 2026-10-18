---
id: learning.zephyr-docs.api-source-reference.page-276
title: fs_mgmt_hash_checksum.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第276章\_fs\_mgmt\_hash\_checksum.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html)。

## 276.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="afs_8h_html"></a>
<a id="afs__mgmt__hash__checksum_8h_html_a0f429c6e46361838794a2fe733f4e2cb"></a>
<a id="afs__mgmt__hash__checksum_8h_html_a1a3db209871cb21f90c7feb5fda4db62"></a>
<a id="afs__mgmt__hash__checksum_8h_html_a5066ea99fe3f80652c364f9f779630d7"></a>
<a id="afs__mgmt__hash__checksum_8h_html_a5b299016aa5dab661395dbfb655af16c"></a>
<a id="afs__mgmt__hash__checksum_8h_html_a5f97144885d0a72dcab02de690511452"></a>
<a id="afs__mgmt__hash__checksum_8h_html_a97669e080a8bdaee3bb8f2593ba99639"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructfs__file__t_html"></a>
<a id="astructfs__mgmt__hash__checksum__group_html"></a>
<a id="astructfs__mgmt__hash__checksum__group_html_a003712f5384e918e5d7d51d9b7acfcb4"></a>
<a id="astructfs__mgmt__hash__checksum__group_html_a5f55c7a9e8905b3ca497cc4711527a2a"></a>
<a id="astructfs__mgmt__hash__checksum__group_html_a620d92183c78b36ad83793b9ceb9d098"></a>
<a id="astructfs__mgmt__hash__checksum__group_html_a8f6ef7d183c6b41c067b2a8544e79e7e"></a>
<a id="astructfs__mgmt__hash__checksum__group_html_aa9bb8702720e6a8287ec6c88da46afff"></a>
<a id="astructgroup_html"></a>

```c
/*
 * Copyright (c) 2018-2022 mcumgr authors
 * Copyright (c) 2022 Laird Connectivity
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_HASH_CHECKSUM_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_HASH_CHECKSUM_H_

#include <zephyr/kernel.h>
#include <zephyr/fs/fs.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef int (*fs_mgmt_hash_checksum_handler_fn)(struct fs_file_t *file, uint8_t *output,
                                                size_t *out_len, size_t len);

struct fs_mgmt_hash_checksum_group {
        sys_snode_t node;

        const char *group_name;

        bool byte_string;

        uint8_t output_size;

        fs_mgmt_hash_checksum_handler_fn function;
};

typedef void (*fs_mgmt_hash_checksum_list_cb)(const struct fs_mgmt_hash_checksum_group *group,
                                              void *user_data);

void fs_mgmt_hash_checksum_register_group(struct fs_mgmt_hash_checksum_group *group);

void fs_mgmt_hash_checksum_unregister_group(struct fs_mgmt_hash_checksum_group *group);

const struct fs_mgmt_hash_checksum_group *fs_mgmt_hash_checksum_find_handler(const char *name);

void fs_mgmt_hash_checksum_find_handlers(fs_mgmt_hash_checksum_list_cb cb, void *user_data);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_HASH_CHECKSUM_H_ */
```

## 276.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018-2022 mcumgr authors。

版权（Copyright）：© 2022 Laird Connectivity。

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 97 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_HASH_CHECKSUM_H_`。

## 276.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/fs/fs.h](../storage/P077_文件系统公共头文件.md)
- [fs_mgmt_hash_checksum_handler_fn](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html#a1a3db209871cb21f90c7feb5fda4db62)
- [fs_file_t](../storage/P038_文件系统文件对象.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [fs_mgmt_hash_checksum_group](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md#a620d92183c78b36ad83793b9ceb9d098)
- [group_name](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md#a5f55c7a9e8905b3ca497cc4711527a2a)
- [byte_string](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md#aa9bb8702720e6a8287ec6c88da46afff)
- [output_size](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md#a8f6ef7d183c6b41c067b2a8544e79e7e)
- [function](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md#a003712f5384e918e5d7d51d9b7acfcb4)
- [fs_mgmt_hash_checksum_list_cb](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html#a97669e080a8bdaee3bb8f2593ba99639)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [fs_mgmt_hash_checksum_register_group](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html#a0f429c6e46361838794a2fe733f4e2cb)
- [fs_mgmt_hash_checksum_unregister_group](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html#a5f97144885d0a72dcab02de690511452)
- [fs_mgmt_hash_checksum_find_handler](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html#a5066ea99fe3f80652c364f9f779630d7)
- [fs_mgmt_hash_checksum_find_handlers](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html#a5b299016aa5dab661395dbfb655af16c)
- [fs.h](../storage/P077_文件系统公共头文件.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [fs_mgmt_hash_checksum_group::function](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md#a003712f5384e918e5d7d51d9b7acfcb4)
- [fs_mgmt_hash_checksum_group::group_name](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md#a5f55c7a9e8905b3ca497cc4711527a2a)
- [fs_mgmt_hash_checksum_group::node](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md#a620d92183c78b36ad83793b9ceb9d098)
- [fs_mgmt_hash_checksum_group::output_size](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md#a8f6ef7d183c6b41c067b2a8544e79e7e)
- [fs_mgmt_hash_checksum_group::byte_string](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md#aa9bb8702720e6a8287ec6c88da46afff)

---

[上一章](P275_fs_mgmt_callbacks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P277_fs_sys.h_源码浏览.md)
