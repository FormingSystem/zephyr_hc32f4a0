---
id: learning.zephyr-docs.api-source-system-reference.page-12
title: fs_interface.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fs__interface_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_fs\_interface.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fs__interface_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../storage/P078_文件系统接口头文件.md)。

## 12.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
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
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00089"></a>
<a id="foldopen00095"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="afs__interface_8h_html_a7090a1b41e73d393b8be3e18ab411027"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructfs__dir__t_html"></a>
<a id="astructfs__dir__t_html_a6d8e0c603a33ed4870fcd7b82e1bc0a4"></a>
<a id="astructfs__dir__t_html_afdd8e0b7b0c528a420c050718213d1ff"></a>
<a id="astructfs__file__t_html"></a>
<a id="astructfs__file__t_html_a9a4fbedc9df828f7ec8eb3b9734a054e"></a>
<a id="astructfs__file__t_html_aa63d13a3c2923f1adecb55ab7e6d1bfa"></a>
<a id="astructfs__file__t_html_af027d2f6b262d26d9d45551e4b9044e2"></a>
<a id="astructfs__mount__t_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_FS_FS_INTERFACE_H_
#define ZEPHYR_INCLUDE_FS_FS_INTERFACE_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_FILE_SYSTEM_MAX_FILE_NAME) && (CONFIG_FILE_SYSTEM_MAX_FILE_NAME - 0) > 0

/* No in-tree file system supports name longer than 255 characters */
#if (CONFIG_FILE_SYSTEM_LITTLEFS || CONFIG_FAT_FILESYSTEM_ELM ||        \
        CONFIG_FILE_SYSTEM_EXT2) && (CONFIG_FILE_SYSTEM_MAX_FILE_NAME > 255)
#error "Max allowed CONFIG_FILE_SYSTEM_MAX_FILE_NAME is 255 characters, when any in-tree FS enabled"
#endif

/* Enabled FAT driver, without LFN, restricts name length to 12 characters */
#if defined(CONFIG_FAT_FILESYSTEM_ELM) && !(CONFIG_FS_FATFS_LFN) && \
        (CONFIG_FILE_SYSTEM_MAX_FILE_NAME > 12)
#error "CONFIG_FILE_SYSTEM_MAX_FILE_NAME can not be > 12 if FAT is enabled without LFN"
#endif

#define MAX_FILE_NAME CONFIG_FILE_SYSTEM_MAX_FILE_NAME

#else
/* Select from enabled file systems */

#if defined(CONFIG_FAT_FILESYSTEM_ELM)

#if defined(CONFIG_FS_FATFS_LFN)
#define MAX_FILE_NAME CONFIG_FS_FATFS_MAX_LFN
#else /* CONFIG_FS_FATFS_LFN */
#define MAX_FILE_NAME 12 /* Uses 8.3 SFN */
#endif /* CONFIG_FS_FATFS_LFN */

#endif

#if !defined(MAX_FILE_NAME) && defined(CONFIG_FILE_SYSTEM_EXT2)
#define MAX_FILE_NAME 255
#endif

#if !defined(MAX_FILE_NAME) && defined(CONFIG_FILE_SYSTEM_LITTLEFS)
#define MAX_FILE_NAME 255
#endif

#if !defined(MAX_FILE_NAME) && defined(CONFIG_FILE_SYSTEM_VIRTIOFS)
#define MAX_FILE_NAME 255
#endif

#if !defined(MAX_FILE_NAME) && defined(CONFIG_FILE_SYSTEM_RPMSGFS)
#define MAX_FILE_NAME 255
#endif

#if !defined(MAX_FILE_NAME) /* filesystem selection */
#define MAX_FILE_NAME 12
#endif /* filesystem selection */

#endif /* CONFIG_FILE_SYSTEM_MAX_FILE_NAME */


typedef uint8_t fs_mode_t;

struct fs_mount_t;


struct fs_file_t {
        void *filep;
        const struct fs_mount_t *mp;
        fs_mode_t flags;
};

struct fs_dir_t {
        void *dirp;
        const struct fs_mount_t *mp;
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_FS_FS_INTERFACE_H_ */
```

## 12.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 24 行

源码树中的文件系统（In-Tree File Systems）均不支持超过 255 个字符的名称。

### 注释 3：原第 30 行

启用 FAT 驱动但不启用长文件名（LFN）时，名称长度限制为 12 个字符。

### 注释 4：原第 39 行

从已启用的文件系统（Enabled File Systems）中选择。

### 注释 5：原第 45 行

条件编译配置（Configuration）标记：`CONFIG_FS_FATFS_LFN`。

### 注释 6：原第 46 行

使用 8.3 格式短文件名（Short File Name，SFN）。

### 注释 7：原第 47 行

条件编译配置（Configuration）标记：`CONFIG_FS_FATFS_LFN`。

### 注释 8：原第 67 行

文件系统选择（Filesystem Selection）。

### 注释 9：原第 75 行

文件系统选择（Filesystem Selection）。

### 注释 10：原第 77 行

条件编译配置（Configuration）标记：`CONFIG_FILE_SYSTEM_MAX_FILE_NAME`。

### 注释 11：原第 124 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_FS_FS_INTERFACE_H_`。

## 12.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../storage/P078_文件系统接口头文件.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [fs_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/fs__interface_8h.html#a7090a1b41e73d393b8be3e18ab411027)
- [fs_mount_t](../storage/P035_文件系统挂载结构.md)
- [fs_file_t](../storage/P038_文件系统文件对象.md)
- [filep](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__t.html#aa63d13a3c2923f1adecb55ab7e6d1bfa)
- [mp](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__t.html#af027d2f6b262d26d9d45551e4b9044e2)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__t.html#a9a4fbedc9df828f7ec8eb3b9734a054e)
- [fs_dir_t](../storage/P039_文件系统目录对象.md)
- [dirp](https://docs.zephyrproject.org/latest/doxygen/html/structfs__dir__t.html#afdd8e0b7b0c528a420c050718213d1ff)
- [mp](https://docs.zephyrproject.org/latest/doxygen/html/structfs__dir__t.html#a6d8e0c603a33ed4870fcd7b82e1bc0a4)
- [fs_dir_t::mp](https://docs.zephyrproject.org/latest/doxygen/html/structfs__dir__t.html#a6d8e0c603a33ed4870fcd7b82e1bc0a4)
- [fs_dir_t::dirp](https://docs.zephyrproject.org/latest/doxygen/html/structfs__dir__t.html#afdd8e0b7b0c528a420c050718213d1ff)
- [fs_file_t::flags](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__t.html#a9a4fbedc9df828f7ec8eb3b9734a054e)
- [fs_file_t::filep](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__t.html#aa63d13a3c2923f1adecb55ab7e6d1bfa)
- [fs_file_t::mp](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__t.html#af027d2f6b262d26d9d45551e4b9044e2)

---

[上一章](P011_eth_nxp_enet.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P013_haptics.h_源码浏览.md)
