---
id: learning.zephyr-docs.api-source-reference.page-446
title: littlefs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/littlefs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第446章\_littlefs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/littlefs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../storage/P041_LittleFS挂载配置头文件.md)。

## 446.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00120"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="aflash__map_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructfs__littlefs_html"></a>
<a id="astructfs__littlefs_html_a0ebbf427f161722fc269573d86e562c5"></a>
<a id="astructfs__littlefs_html_a239d1ac90cc0de3a9cca766d41180def"></a>
<a id="astructfs__littlefs_html_a337c24352a8f39c1d1f55682126341b5"></a>
<a id="astructfs__littlefs_html_a3a1902a64f78b65743786d154b435439"></a>
<a id="astructfs__littlefs_html_a7cd0dcd14e83138ba2ed698f55377e49"></a>
<a id="astructfs__littlefs_html_ab9b4cd8ce0aedfd071ea184d92b1224a"></a>
<a id="astructfs__littlefs_html_ac1b102a94e6db2dfb4ca0d0bee5a561e"></a>
<a id="astructk__mutex_html"></a>

```c
/*
 * Copyright (c) 2019 Bolt Innovation Management, LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_FS_LITTLEFS_H_
#define ZEPHYR_INCLUDE_FS_LITTLEFS_H_

#include <zephyr/types.h>
#include <zephyr/kernel.h>
#include <zephyr/storage/flash_map.h>

#include <lfs.h>

#ifdef __cplusplus
extern "C" {
#endif

#define FS_LITTLEFS_DISK_VERSION_MAJOR_GET(disk_version) FIELD_GET(GENMASK(31, 16), disk_version)

#define FS_LITTLEFS_DISK_VERSION_MINOR_GET(disk_version) FIELD_GET(GENMASK(15, 0), disk_version)

struct fs_littlefs {
        struct lfs_config cfg;

        uint8_t *read_buffer;

        uint8_t *prog_buffer;

        uint32_t *lookahead_buffer[CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE / sizeof(uint32_t)];

        struct lfs lfs;
        void *backend;
        struct k_mutex mutex;
};

#define FS_LITTLEFS_DECLARE_CUSTOM_CONFIG(name, alignment, read_sz, prog_sz, cache_sz,    \
                                          lookahead_sz)                                   \
        static uint8_t __aligned(alignment) name ## _read_buffer[cache_sz];               \
        static uint8_t __aligned(alignment) name ## _prog_buffer[cache_sz];               \
        static uint32_t name ## _lookahead_buffer[(lookahead_sz) / sizeof(uint32_t)];     \
        static struct fs_littlefs name = {                                                \
                .cfg = {                                                                  \
                        .read_size = (read_sz),                                           \
                        .prog_size = (prog_sz),                                           \
                        .cache_size = (cache_sz),                                         \
                        .lookahead_size = (lookahead_sz),                                 \
                        .read_buffer = name ## _read_buffer,                              \
                        .prog_buffer = name ## _prog_buffer,                              \
                        .lookahead_buffer = name ## _lookahead_buffer,                    \
                },                                                                        \
        }

#define FS_LITTLEFS_DECLARE_DEFAULT_CONFIG(name)                         \
        FS_LITTLEFS_DECLARE_CUSTOM_CONFIG(name,                          \
                                          4,                             \
                                          CONFIG_FS_LITTLEFS_READ_SIZE,  \
                                          CONFIG_FS_LITTLEFS_PROG_SIZE,  \
                                          CONFIG_FS_LITTLEFS_CACHE_SIZE, \
                                          CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE)

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_FS_LITTLEFS_H_ */
```

## 446.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Bolt Innovation Management, LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 132 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_FS_LITTLEFS_H_`。

## 446.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../storage/P041_LittleFS挂载配置头文件.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/storage/flash_map.h](https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h.html)
- [fs_littlefs](../storage/P042_LittleFS挂载数据.md)
- [cfg](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#ab9b4cd8ce0aedfd071ea184d92b1224a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [read_buffer](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#ac1b102a94e6db2dfb4ca0d0bee5a561e)
- [prog_buffer](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a239d1ac90cc0de3a9cca766d41180def)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [lookahead_buffer](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a7cd0dcd14e83138ba2ed698f55377e49)
- [lfs](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a3a1902a64f78b65743786d154b435439)
- [backend](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a0ebbf427f161722fc269573d86e562c5)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [mutex](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a337c24352a8f39c1d1f55682126341b5)
- [flash_map.h](https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [fs_littlefs::backend](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a0ebbf427f161722fc269573d86e562c5)
- [fs_littlefs::prog_buffer](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a239d1ac90cc0de3a9cca766d41180def)
- [fs_littlefs::mutex](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a337c24352a8f39c1d1f55682126341b5)
- [fs_littlefs::lfs](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a3a1902a64f78b65743786d154b435439)
- [fs_littlefs::lookahead_buffer](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a7cd0dcd14e83138ba2ed698f55377e49)
- [fs_littlefs::cfg](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#ab9b4cd8ce0aedfd071ea184d92b1224a)
- [fs_littlefs::read_buffer](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#ac1b102a94e6db2dfb4ca0d0bee5a561e)

---

[上一章](P445_lis2dw12.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P447_llvm.h_源码浏览.md)
