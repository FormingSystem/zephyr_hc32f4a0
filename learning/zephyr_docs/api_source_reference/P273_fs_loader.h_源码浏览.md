---
id: learning.zephyr-docs.api-source-reference.page-273
title: fs_loader.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fs__loader_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第273章\_fs\_loader.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fs__loader_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fs__loader_8h.html)。

## 273.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="foldopen00052"></a>
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
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="afs_8h_html"></a>
<a id="aloader_8h_html"></a>
<a id="astructfs__file__t_html"></a>
<a id="astructllext__fs__loader_html"></a>
<a id="astructllext__fs__loader_html_a33f0ba96f4437d74faff6cb78c2188cb"></a>
<a id="astructllext__loader_html"></a>

```c
/*
 * Copyright (c) 2024 BayLibre SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_LLEXT_FS_LOADER_H_
#define ZEPHYR_INCLUDE_LLEXT_FS_LOADER_H_

#include <zephyr/llext/loader.h>
#include <zephyr/fs/fs.h>

#ifdef __cplusplus
extern "C" {
#endif


struct llext_fs_loader {
        struct llext_loader loader;

        bool is_open;
        const char *name;
        struct fs_file_t file;
};

int llext_fs_prepare(struct llext_loader *ldr);
int llext_fs_read(struct llext_loader *ldr, void *buf, size_t len);
int llext_fs_seek(struct llext_loader *ldr, size_t pos);
void llext_fs_finalize(struct llext_loader *ldr);

#define LLEXT_FS_LOADER(_filename)                                                                 \
        {                                                                                          \
                .loader =                                                                          \
                        {                                                                          \
                                .prepare = llext_fs_prepare,                                       \
                                .read = llext_fs_read,                                             \
                                .seek = llext_fs_seek,                                             \
                                .peek = NULL,                                                      \
                                .finalize = llext_fs_finalize,                                     \
                                .storage = LLEXT_STORAGE_TEMPORARY,                                \
                        },                                                                         \
                .is_open = false,                                                                  \
                .name = (_filename),                                                               \
        }


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_LLEXT_FS_LOADER_H_ */
```

## 273.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 BayLibre SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 75 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_LLEXT_FS_LOADER_H_`。

## 273.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fs__loader_8h.html)
- [zephyr/llext/loader.h](https://docs.zephyrproject.org/latest/doxygen/html/loader_8h.html)
- [zephyr/fs/fs.h](../storage/P077_文件系统公共头文件.md)
- [llext_fs_loader](../llext/P023_文件系统加载器.md)
- [llext_loader](../llext/P025_扩展加载器上下文.md)
- [loader](../llext/P023_文件系统加载器.md#a33f0ba96f4437d74faff6cb78c2188cb)
- [fs_file_t](../storage/P038_文件系统文件对象.md)
- [fs.h](../storage/P077_文件系统公共头文件.md)
- [loader.h](https://docs.zephyrproject.org/latest/doxygen/html/loader_8h.html)
- [llext_fs_loader::loader](../llext/P023_文件系统加载器.md#a33f0ba96f4437d74faff6cb78c2188cb)

---

[上一章](P272_zms.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P274_fs_mgmt.h_源码浏览.md)
