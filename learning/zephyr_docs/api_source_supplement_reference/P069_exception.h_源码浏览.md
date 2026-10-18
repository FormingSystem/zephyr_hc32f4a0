---
id: learning.zephyr-docs.api-source-supplement-reference.page-69
title: exception.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/exception_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_exception.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/exception_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/exception_8h.html)。

## 69.1\_原始可见代码（Source Code）

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
<a id="foldopen00018"></a>
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
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
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
<a id="l00111"></a>
<a id="l00112"></a>
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
<a id="foldopen00134"></a>
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
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="aexception_8h_html_a9998b45688b94011e21d501addff40bc"></a>
<a id="aprintk_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="atricore_2exception_8h_html"></a>

```c
/* exception.h - automatically selects the correct exception.h file to include */

/*
 * Copyright (c) 2024 Meta Platforms
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ARCH_EXCEPTION_H_
#define ZEPHYR_INCLUDE_ARCH_EXCEPTION_H_

#ifndef _ASMLANGUAGE

#include <stdarg.h>
#include <zephyr/toolchain.h>
#include <zephyr/sys/printk.h>

static inline __printf_like(1, 2) void arch_exception_dump_arg_check(const char *fmt, ...)
{
        ARG_UNUSED(fmt);
}

#if defined(CONFIG_EXCEPTION_DUMP_HOOK)

#include <stdbool.h>
#include <stdarg.h>

typedef void (*arch_exception_dump_hook_t)(const char *format, va_list args);

typedef void (*arch_exception_drain_hook_t)(bool flush);

extern arch_exception_dump_hook_t arch_exception_dump_hook;
extern arch_exception_drain_hook_t arch_exception_drain_hook;

static inline void arch_exception_set_dump_hook(arch_exception_dump_hook_t dump,
                                                arch_exception_drain_hook_t drain)
{
        arch_exception_dump_hook = dump;
        arch_exception_drain_hook = drain;
}

static inline void arch_exception_call_drain_hook(bool flush)
{
        if (arch_exception_drain_hook) {
                arch_exception_drain_hook(flush);
        }
}

static inline void arch_exception_call_dump_hook(const char *format, ...)
{
        va_list args;

        if (arch_exception_dump_hook) {
                va_start(args, format);
                arch_exception_dump_hook(format, args);
                va_end(args);
        }
}

#if !defined(CONFIG_EXCEPTION_DUMP)
#define EXCEPTION_DUMP(format, ...)                                                                \
        do {                                                                                       \
                if (0) {                                                                           \
                        arch_exception_dump_arg_check(format, ##__VA_ARGS__);                      \
                }                                                                                  \
        } while (false)
#elif defined(CONFIG_EXCEPTION_DUMP_HOOK_ONLY)
#define EXCEPTION_DUMP(format, ...)                                                                \
        do {                                                                                       \
                printk_panic();                                                                    \
                arch_exception_call_dump_hook(format "\n", ##__VA_ARGS__);                         \
        } while (false)
#elif defined(CONFIG_LOG)
#define EXCEPTION_DUMP(format, ...)                                                                \
        do {                                                                                       \
                printk_panic();                                                                    \
                arch_exception_call_dump_hook(format "\n", ##__VA_ARGS__);                         \
                LOG_ERR(format, ##__VA_ARGS__);                                                    \
        } while (false)
#else
#define EXCEPTION_DUMP(format, ...)                                                                \
        do {                                                                                       \
                printk_panic();                                                                    \
                arch_exception_call_dump_hook(format "\n", ##__VA_ARGS__);                         \
                printk(format "\n", ##__VA_ARGS__);                                                \
        } while (false)
#endif

#else

#if !defined(CONFIG_EXCEPTION_DUMP)
#define EXCEPTION_DUMP(format, ...)                                                                \
        do {                                                                                       \
                if (0) {                                                                           \
                        arch_exception_dump_arg_check(format, ##__VA_ARGS__);                      \
                }                                                                                  \
        } while (false)
#elif defined(CONFIG_LOG)
#define EXCEPTION_DUMP(...)                                                                        \
        do {                                                                                       \
                printk_panic();                                                                    \
                LOG_ERR(__VA_ARGS__);                                                              \
        } while (false)
#else
#define EXCEPTION_DUMP(format, ...)                                                                \
        do {                                                                                       \
                printk_panic();                                                                    \
                printk(format "\n", ##__VA_ARGS__);                                                \
        } while (false)
#endif
#endif

#endif /* _ASMLANGUAGE */

#if defined(CONFIG_X86_64)
#include <zephyr/arch/x86/intel64/exception.h>
#elif defined(CONFIG_X86)
#include <zephyr/arch/x86/ia32/exception.h>
#elif defined(CONFIG_ARM64)
#include <zephyr/arch/arm64/exception.h>
#elif defined(CONFIG_ARM)
#include <zephyr/arch/arm/exception.h>
#elif defined(CONFIG_ARC)
#include <zephyr/arch/arc/v2/exception.h>
#elif defined(CONFIG_RISCV)
#include <zephyr/arch/riscv/exception.h>
#elif defined(CONFIG_XTENSA)
#include <zephyr/arch/xtensa/exception.h>
#elif defined(CONFIG_MIPS)
#include <zephyr/arch/mips/exception.h>
#elif defined(CONFIG_OPENRISC)
#include <zephyr/arch/openrisc/exception.h>
#elif defined(CONFIG_ARCH_POSIX)
#include <zephyr/arch/posix/exception.h>
#elif defined(CONFIG_SPARC)
#include <zephyr/arch/sparc/exception.h>
#elif defined(CONFIG_RX)
#include <zephyr/arch/rx/exception.h>
#elif defined(CONFIG_HEXAGON)
#include <zephyr/arch/hexagon/exception.h>
#elif defined(CONFIG_TRICORE)
#include <zephyr/arch/tricore/exception.h>
#elif defined(CONFIG_ARCH_IS_SET)
#error "The selected architecture is missing from this dispatch header"
#endif

#endif /* ZEPHYR_INCLUDE_ARCH_EXCEPTION_H_ */
```

## 69.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`exception.h`：自动选择要包含的正确 `exception.h` 文件。

### 注释 2：原第 3 行

版权（Copyright）：© 2024 Meta Platforms。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 155 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 4：原第 189 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_EXCEPTION_H_`。

## 69.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/exception_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/sys/printk.h](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)
- [arch_exception_dump_arg_check](https://docs.zephyrproject.org/latest/doxygen/html/exception_8h.html#a9998b45688b94011e21d501addff40bc)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/arch/tricore/exception.h](https://docs.zephyrproject.org/latest/doxygen/html/tricore_2exception_8h.html)
- [printk.h](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [exception.h](https://docs.zephyrproject.org/latest/doxygen/html/tricore_2exception_8h.html)

---

[上一章](P068_exc_handle.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P070_fdc2x1x.h_源码浏览.md)
