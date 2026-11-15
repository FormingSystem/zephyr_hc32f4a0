---
id: learning.zephyr-docs.api-source-reference.page-851
title: dirent.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sys_2dirent_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第851章\_dirent.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sys_2dirent_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sys_2dirent_8h.html)。

## 851.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00026"></a>
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
<a id="alimits_8h_html"></a>
<a id="astructdirent_html"></a>
<a id="astructdirent_html_a493ff210982a02728c1b177139bfdb47"></a>
<a id="astructdirent_html_ae4afde6b22d291bf27193ad4fe20b0bf"></a>
<a id="asys_2dirent_8h_html_a6808d95339147c6e29523463181854cc"></a>

```c
/*
 * Copyright (c) 2024 Tenstorrent AI ULC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_SYS_DIRENT_H_
#define ZEPHYR_INCLUDE_POSIX_SYS_DIRENT_H_

#include <limits.h>

#if !defined(NAME_MAX) && defined(_XOPEN_SOURCE)
#define NAME_MAX _XOPEN_NAME_MAX
#endif

#if !defined(NAME_MAX) && defined(_POSIX_C_SOURCE)
#define NAME_MAX _POSIX_NAME_MAX
#endif

#ifdef __cplusplus
extern "C" {
#endif

typedef void DIR;

struct dirent {
        unsigned int d_ino;
        char d_name[NAME_MAX + 1];
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_SYS_DIRENT_H_ */
```

## 851.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Tenstorrent AI ULC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 35 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SYS_DIRENT_H_`。

## 851.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sys_2dirent_8h.html)
- [limits.h](https://docs.zephyrproject.org/latest/doxygen/html/limits_8h.html)
- [DIR](https://docs.zephyrproject.org/latest/doxygen/html/sys_2dirent_8h.html#a6808d95339147c6e29523463181854cc)
- [dirent](../posix_system_model_reference/P001_dirent_结构体.md)
- [d_ino](../posix_system_model_reference/P001_dirent_结构体.md#ae4afde6b22d291bf27193ad4fe20b0bf)
- [d_name](../posix_system_model_reference/P001_dirent_结构体.md#a493ff210982a02728c1b177139bfdb47)
- [dirent::d_name](../posix_system_model_reference/P001_dirent_结构体.md#a493ff210982a02728c1b177139bfdb47)
- [dirent::d_ino](../posix_system_model_reference/P001_dirent_结构体.md#ae4afde6b22d291bf27193ad4fe20b0bf)

---

[上一章](P850_syna_sr100_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P852_sysctl.h_源码浏览.md)
