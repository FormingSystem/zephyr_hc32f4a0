---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-12
title: sys_getopt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_sys\_getopt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html)。

## 12.1\_原始可见代码（Source Code）

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
<a id="foldopen00016"></a>
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
<a id="foldopen00041"></a>
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
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="akernel_8h_html"></a>
<a id="astructsys__getopt__option_html"></a>
<a id="astructsys__getopt__option_html_a38c70fec67104f8721366063600ae890"></a>
<a id="astructsys__getopt__option_html_a5001cbba7a4968a76a2015f3bc0c752a"></a>
<a id="astructsys__getopt__option_html_a921375712892da06f943f1418bfca4ce"></a>
<a id="astructsys__getopt__option_html_ab7b799a1971273a5464eb9eca849606b"></a>
<a id="astructsys__getopt__state_html"></a>
<a id="astructsys__getopt__state_html_a51925275080512a6dcac6b4e1a28d8cb"></a>
<a id="astructsys__getopt__state_html_a65eb337bc32085a402a9fb0c58a2bea8"></a>
<a id="astructsys__getopt__state_html_a887b21d513bca0eee2a300b7ccd39364"></a>
<a id="astructsys__getopt__state_html_a8b05064215051a7ee82038bfb56a1cd1"></a>
<a id="astructsys__getopt__state_html_a9de2baf0642b3e50a05116b10706bbe8"></a>
<a id="astructsys__getopt__state_html_ad41495ab8dd1cb55efc177fdb3e45316"></a>
<a id="asys__getopt_8h_html_a091f245c08065a360b765b06a4bb3ec8"></a>
<a id="asys__getopt_8h_html_a162f907a30748f8e5b7bfed601c5723b"></a>
<a id="asys__getopt_8h_html_a35ad483c9371f3e0fd71813c3f2f39d2"></a>
<a id="asys__getopt_8h_html_a46ac8783a520db9faf201bfee4179d58"></a>
<a id="asys__getopt_8h_html_a585cba391f737a7db7247a55f964ec38"></a>
<a id="asys__getopt_8h_html_a823ee9bebc991cbb0f58f805c2df768d"></a>
<a id="asys__getopt_8h_html_a8339f5cdb7f036bec15e4a4a3b2fff20"></a>
<a id="asys__getopt_8h_html_a84af076f38140c6f7bc6c4797c96c157"></a>
<a id="asys__getopt_8h_html_aa259f622c6daa9a421e2542bc63bc29d"></a>
<a id="asys__getopt_8h_html_ae363b8a3a593e215292522d3ffd9839d"></a>

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SYS_SYS_GETOPT_H_
#define ZEPHYR_INCLUDE_SYS_SYS_GETOPT_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/kernel.h>

struct sys_getopt_state {
        int opterr;   /* if error message should be printed */
        int optind;   /* index into parent argv vector */
        int optopt;   /* character checked for validity */
        int optreset; /* reset getopt */
        char *optarg; /* argument associated with option */

        char *place; /* option letter processing */

#if CONFIG_GETOPT_LONG
        int nonopt_start;
        int nonopt_end;
#endif
};

extern int sys_getopt_optreset; /* reset getopt */
extern char *sys_getopt_optarg;
extern int sys_getopt_opterr;
extern int sys_getopt_optind;
extern int sys_getopt_optopt;

#define sys_getopt_no_argument       0
#define sys_getopt_required_argument 1
#define sys_getopt_optional_argument 2

struct sys_getopt_option {
        /* name of long option */
        const char *name;
        /*
         * one of no_argument, required_argument, and optional_argument:
         * whether option takes an argument
         */
        int has_arg;
        /* if not NULL, set *flag to val when option found */
        int *flag;
        /* if flag not NULL, value to set *flag to; else return value */
        int val;
};

/* Function initializes getopt_state structure for current thread */
void sys_getopt_init(void);

/* Function returns getopt_state structure for the current thread. */
struct sys_getopt_state *sys_getopt_state_get(void);

int sys_getopt(int nargc, char *const nargv[], const char *ostr);

int sys_getopt_long(int nargc, char *const *nargv, const char *options,
                    const struct sys_getopt_option *long_options, int *idx);

int sys_getopt_long_only(int nargc, char *const *nargv, const char *options,
                         const struct sys_getopt_option *long_options, int *idx);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SYS_SYS_GETOPT_H_ */
```

## 12.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 17 行

是否应打印错误消息（error message）。

### 注释 3：原第 18 行

父 `argv` 向量中的索引（index）。

### 注释 4：原第 19 行

正在检查其有效性的字符。

### 注释 5：原第 20 行

重置 `getopt`。

### 注释 6：原第 21 行

与选项（option）关联的参数（argument）。

### 注释 7：原第 23 行

选项字母处理（option letter processing）。

### 注释 8：原第 31 行

重置 `getopt`。

### 注释 9：原第 42 行

长选项（long option）的名称。

### 注释 10：原第 44 行

取 `no_argument`、`required_argument` 或 `optional_argument` 之一，表示选项是否带参数。

### 注释 11：原第 49 行

如果不为 `NULL`，则在找到选项时将 `*flag` 设为 `val`。

### 注释 12：原第 51 行

如果 `flag` 不为 `NULL`，这是赋给 `*flag` 的值；否则是返回值。

### 注释 13：原第 55 行

此函数初始化当前线程的 `getopt_state` 结构体。

### 注释 14：原第 58 行

此函数返回当前线程的 `getopt_state` 结构体。

### 注释 15：原第 130 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SYS_SYS_GETOPT_H_`。

## 12.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [sys_getopt_state](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md)
- [opterr](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#a51925275080512a6dcac6b4e1a28d8cb)
- [optind](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#a9de2baf0642b3e50a05116b10706bbe8)
- [optopt](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#ad41495ab8dd1cb55efc177fdb3e45316)
- [optreset](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#a8b05064215051a7ee82038bfb56a1cd1)
- [optarg](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#a65eb337bc32085a402a9fb0c58a2bea8)
- [place](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#a887b21d513bca0eee2a300b7ccd39364)
- [sys_getopt_optreset](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html#a46ac8783a520db9faf201bfee4179d58)
- [sys_getopt_optarg](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html#a091f245c08065a360b765b06a4bb3ec8)
- [sys_getopt_opterr](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html#a162f907a30748f8e5b7bfed601c5723b)
- [sys_getopt_optind](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html#aa259f622c6daa9a421e2542bc63bc29d)
- [sys_getopt_optopt](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html#ae363b8a3a593e215292522d3ffd9839d)
- [sys_getopt_option](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md)
- [name](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md#a5001cbba7a4968a76a2015f3bc0c752a)
- [has_arg](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md#a38c70fec67104f8721366063600ae890)
- [flag](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md#a921375712892da06f943f1418bfca4ce)
- [val](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md#ab7b799a1971273a5464eb9eca849606b)
- [sys_getopt_init](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html#a8339f5cdb7f036bec15e4a4a3b2fff20)
- [sys_getopt_state_get](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html#a84af076f38140c6f7bc6c4797c96c157)
- [sys_getopt](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html#a35ad483c9371f3e0fd71813c3f2f39d2)
- [sys_getopt_long](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html#a585cba391f737a7db7247a55f964ec38)
- [sys_getopt_long_only](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html#a823ee9bebc991cbb0f58f805c2df768d)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [sys_getopt_option::has_arg](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md#a38c70fec67104f8721366063600ae890)
- [sys_getopt_option::name](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md#a5001cbba7a4968a76a2015f3bc0c752a)
- [sys_getopt_option::flag](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md#a921375712892da06f943f1418bfca4ce)
- [sys_getopt_option::val](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md#ab7b799a1971273a5464eb9eca849606b)
- [sys_getopt_state::opterr](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#a51925275080512a6dcac6b4e1a28d8cb)
- [sys_getopt_state::optarg](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#a65eb337bc32085a402a9fb0c58a2bea8)
- [sys_getopt_state::place](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#a887b21d513bca0eee2a300b7ccd39364)
- [sys_getopt_state::optreset](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#a8b05064215051a7ee82038bfb56a1cd1)
- [sys_getopt_state::optind](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#a9de2baf0642b3e50a05116b10706bbe8)
- [sys_getopt_state::optopt](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md#ad41495ab8dd1cb55efc177fdb3e45316)

---

[上一章](P011_sleep.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P013_ti_hdc302x.h_源码浏览.md)
