---
id: learning.zephyr-docs.api-source-supplement-reference.page-225
title: times.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/times_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第225章\_times.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/times_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/times_8h.html)。

## 225.1\_原始可见代码（Source Code）

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
<a id="foldopen00019"></a>
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
<a id="ainclude_2zephyr_2posix_2sys_2time_8h_html"></a>
<a id="aposix__types_8h_html_a3b55f88f25d2c571de53a365ad658426"></a>
<a id="astructtms_html"></a>
<a id="astructtms_html_a2522ba0b91f98baeb8f2b7249f367b7c"></a>
<a id="astructtms_html_a60d97d80205a34858387314fb00cc4c0"></a>
<a id="astructtms_html_ad21f41a18aff2813fe6154154f1f9522"></a>
<a id="astructtms_html_adc1a7576a7287de70b7611047829ab6f"></a>
<a id="atimes_8h_html_a73fc89d71a97e11d44bdd0bbb851a9cb"></a>

```c
/*
 * Copyright (c) 2025 Tenstorrent AI ULC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_SYS_TIMES_H_
#define ZEPHYR_INCLUDE_POSIX_SYS_TIMES_H_

#include <time.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(_POSIX_MULTI_PROCESS) || defined(__DOXYGEN__)

#if !defined(_TMS_DECLARED) && !defined(__tms_defined)
struct tms {
        clock_t tms_utime;
        clock_t tms_stime;
        clock_t tms_cutime;
        clock_t tms_cstime;
};
#define _TMS_DECLARED
#define __tms_defined
#endif

clock_t times(struct tms *buf);

#endif /* _POSIX_MULTI_PROCESS */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_SYS_TIMES_H_ */
```

## 225.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Tenstorrent AI ULC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 31 行

条件编译标记：`_POSIX_MULTI_PROCESS`。

### 注释 3：原第 37 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SYS_TIMES_H_`。

## 225.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/times_8h.html)
- [time.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2posix_2sys_2time_8h.html)
- [tms](../posix_system_model_reference/P026_tms_结构体.md)
- [clock_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3b55f88f25d2c571de53a365ad658426)
- [tms_utime](../posix_system_model_reference/P026_tms_结构体.md#a2522ba0b91f98baeb8f2b7249f367b7c)
- [tms_stime](../posix_system_model_reference/P026_tms_结构体.md#a60d97d80205a34858387314fb00cc4c0)
- [tms_cutime](../posix_system_model_reference/P026_tms_结构体.md#adc1a7576a7287de70b7611047829ab6f)
- [tms_cstime](../posix_system_model_reference/P026_tms_结构体.md#ad21f41a18aff2813fe6154154f1f9522)
- [times](https://docs.zephyrproject.org/latest/doxygen/html/times_8h.html#a73fc89d71a97e11d44bdd0bbb851a9cb)
- [tms::tms_utime](../posix_system_model_reference/P026_tms_结构体.md#a2522ba0b91f98baeb8f2b7249f367b7c)
- [tms::tms_stime](../posix_system_model_reference/P026_tms_结构体.md#a60d97d80205a34858387314fb00cc4c0)
- [tms::tms_cstime](../posix_system_model_reference/P026_tms_结构体.md#ad21f41a18aff2813fe6154154f1f9522)
- [tms::tms_cutime](../posix_system_model_reference/P026_tms_结构体.md#adc1a7576a7287de70b7611047829ab6f)

---

[上一章](P224_ti-k3-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P226_tiva-c-pinctrl.h_源码浏览.md)
