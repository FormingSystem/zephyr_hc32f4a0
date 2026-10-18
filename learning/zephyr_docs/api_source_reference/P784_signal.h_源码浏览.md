---
id: learning.zephyr-docs.api-source-reference.page-784
title: signal.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/signal_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第784章\_signal.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html)。

## 784.1\_原始可见代码（Source Code）

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
<a id="aposix__signal_8h_html"></a>
<a id="aposix__signal_8h_html_a87cd503247b3afbb79788256ac093ad5"></a>
<a id="asignal_8h_html_a08ba0dd26a850108a1746412faba2b21"></a>
<a id="asignal_8h_html_a5d326f119f87d0facaa662520f8c322a"></a>
<a id="asignal_8h_html_af93df1c6eefeb62980b2a73387e24156"></a>

```c
/*
 * Copyright (c) 2024 Synopsys
 * Copyright (c) 2025 Tenstorrent AI ULC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SIGNAL_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SIGNAL_H_

#ifdef __cplusplus
extern "C" {
#endif

#define SIGABRT 6
#define SIGFPE  8
#define SIGILL  4
#define SIGINT  2
#define SIGSEGV 11
#define SIGTERM 15

#define SIG_DFL ((sighandler_t)0)
#define SIG_IGN ((sighandler_t)1)
#define SIG_ERR ((sighandler_t)(-1))

typedef long sig_atomic_t;

#if !defined(_SIGHANDLER_T_DECLARED) && !defined(__sighandler_t_defined)
typedef void (*sighandler_t)(int sig);
#define _SIGHANDLER_T_DECLARED
#define __sighandler_t_defined
#endif

sighandler_t signal(int sig, sighandler_t handler);
int raise(int sig);

#ifdef __cplusplus
}
#endif

#include <zephyr/posix/posix_signal.h>

#endif /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SIGNAL_H_ */
```

## 784.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Synopsys。

版权（Copyright）：© 2025 Tenstorrent AI ULC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 43 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SIGNAL_H_`。

## 784.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html)
- [sig_atomic_t](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html#af93df1c6eefeb62980b2a73387e24156)
- [sighandler_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a87cd503247b3afbb79788256ac093ad5)
- [signal](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html#a5d326f119f87d0facaa662520f8c322a)
- [raise](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html#a08ba0dd26a850108a1746412faba2b21)
- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html)
- [posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html)

---

[上一章](P783_sifive-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P785_silabs_dcdc.h_源码浏览.md)
