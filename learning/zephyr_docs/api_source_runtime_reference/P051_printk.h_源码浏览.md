---
id: learning.zephyr-docs.api-source-runtime-reference.page-51
title: printk.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/printk_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_printk.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)。

## 51.1\_原始可见代码（Source Code）

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
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
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
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="ainttypes_8h_html"></a>
<a id="alog__core_8h_html"></a>
<a id="aprintk_8h_html_a0b0af71688f7e9170103d771d4e1eab2"></a>
<a id="aprintk_8h_html_a1bce54a738ce2d9dd6d95ee842ec237c"></a>
<a id="aprintk_8h_html_a2cf2f614c79e9e798eaffad1b47fb365"></a>
<a id="aprintk_8h_html_a4cc4b043259c5bb605c17702c988a68c"></a>
<a id="aprintk_8h_html_a9b5fa01884b98d143218af0cd0ffe841"></a>
<a id="aprintk_8h_html_ae824cc3368607ee5d45f860a1389794a"></a>
<a id="aprintk_8h_html_ae8424da1d9d23bcfa739790545b058fc"></a>
<a id="astdio_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/* printk.h - low-level debug output */

/*
 * Copyright (c) 2010-2012, 2014 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_SYS_PRINTK_H_
#define ZEPHYR_INCLUDE_SYS_PRINTK_H_

#include <zephyr/toolchain.h>
#include <stddef.h>
#include <stdarg.h>
#include <inttypes.h>

#ifdef CONFIG_LOG_PRINTK_STATIC
#include <zephyr/logging/log_core.h>
#endif

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_PRINTK) || defined(__DOXYGEN__)

#ifdef CONFIG_LOG_PRINTK_STATIC
/* If printk is redirected to the logging use the macro which allow build time
 * logging message creation which is faster and allows format string stripping in
 * case of dictionary based logging.
 */
#define printk(...) Z_LOG_PRINTK(0, __VA_ARGS__)
#else
__printf_like(1, 2) void printk(const char *fmt, ...);
#endif /* CONFIG_LOG_PRINTK_STATIC */

__printf_like(1, 0) void vprintk(const char *fmt, va_list ap);

__printf_like(1, 2) void printk_unlocked(const char *fmt, ...);

__printf_like(1, 0) void vprintk_unlocked(const char *fmt, va_list ap);

void printk_panic(void);

#else
static inline __printf_like(1, 2) void printk(const char *fmt, ...)
{
        ARG_UNUSED(fmt);
}

static inline __printf_like(1, 0) void vprintk(const char *fmt, va_list ap)
{
        ARG_UNUSED(fmt);
        ARG_UNUSED(ap);
}

static inline __printf_like(1, 2) void printk_unlocked(const char *fmt, ...)
{
        ARG_UNUSED(fmt);
}

static inline __printf_like(1, 0) void vprintk_unlocked(const char *fmt, va_list ap)
{
        ARG_UNUSED(fmt);
        ARG_UNUSED(ap);
}

static inline void printk_panic(void)
{
}
#endif /* defined(CONFIG_PRINTK) || defined(__DOXYGEN__) */

#ifdef CONFIG_PICOLIBC

#include <stdio.h>

#define snprintk(...) snprintf(__VA_ARGS__)
#define vsnprintk(str, size, fmt, ap) vsnprintf(str, size, fmt, ap)

#else

__printf_like(3, 4) int snprintk(char *str, size_t size,
                                        const char *fmt, ...);

__printf_like(3, 0) int vsnprintk(char *str, size_t size,
                                          const char *fmt, va_list ap);

#endif

#ifdef __cplusplus
}
#endif

#endif
```

## 51.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`printk.h`：底层调试输出（Low-level debug output）。

### 注释 2：原第 3 行

版权（Copyright）：© 2010-2012, 2014 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 52 行

如果 `printk` 被重定向到日志系统，应使用允许在构建时创建日志消息的宏；这种方式更快，而且在基于字典的日志模式（Dictionary based logging）下允许剥离格式字符串。

### 注释 4：原第 59 行

条件编译配置（Configuration）标记：`CONFIG_LOG_PRINTK_STATIC`。

### 注释 5：原第 141 行

条件编译表达式：`defined(CONFIG_PRINTK) || defined(__DOXYGEN__)`。

## 51.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h.html)
- [zephyr/logging/log_core.h](../log_internal_reference/P001_日志核心头文件参考.md)
- [printk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a1bce54a738ce2d9dd6d95ee842ec237c)
- [vprintk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a9b5fa01884b98d143218af0cd0ffe841)
- [printk_unlocked](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a2cf2f614c79e9e798eaffad1b47fb365)
- [vprintk_unlocked](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#ae8424da1d9d23bcfa739790545b058fc)
- [printk_panic](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a4cc4b043259c5bb605c17702c988a68c)
- [stdio.h](https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h.html)
- [snprintk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a0b0af71688f7e9170103d771d4e1eab2)
- [vsnprintk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#ae824cc3368607ee5d45f860a1389794a)
- [log_core.h](../log_internal_reference/P001_日志核心头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P050_sched.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P052_renesas_ra_cgc.h_源码浏览.md)
