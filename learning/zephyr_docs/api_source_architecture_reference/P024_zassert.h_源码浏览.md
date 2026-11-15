---
id: learning.zephyr-docs.api-source-architecture-reference.page-24
title: zassert.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zassert_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zassert.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/zassert_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/zassert_8h.html)。

## 24.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
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
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00108"></a>
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
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="foldopen00196"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00217"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="agroup__zassert_html_ga72d07b4b0fb4190dc675813c0d9215b1"></a>
<a id="agroup__zassert_html_ga98d7d44bfde093e6abe6cf51566c77d5"></a>
<a id="agroup__zassert_html_gadf431a5e2a87111d50cd268d309f3eea"></a>
<a id="agroup__zassert_html_gaf1c13156eb4331a95f2e396afb7736ba"></a>
<a id="atoolchain_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Måns Ansgariusson <mansgariusson@gmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_SYS_ZASSERT_H_
#define ZEPHYR_INCLUDE_SYS_ZASSERT_H_

#include <stdarg.h>
#include <stddef.h>

#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>


/*
 * Granular, per-source-file assertions.
 *
 * ZASSERT_MODULE() opts a scope into the module-aware ZASSERT() macro. The
 * resulting assertion level is a compile-time constant, so disabled assertions
 * (and, below ZASSERT_LEVEL_VERBOSE, the message and its arguments) are folded away by
 * the optimizer. An individual file may set its level explicitly, overriding the
 * module default.
 *
 * For headers and inline functions, place ZASSERT_MODULE() inside the function
 * body so the selection does not leak into the includer, or use ZASSERT_TERSE(),
 * ZASSERT_NORMAL() or ZASSERT_VERBOSE() for an assertion with a fixed level.
 */

#define ZASSERT_LEVEL_OFF     0
#define ZASSERT_LEVEL_TERSE   1
#define ZASSERT_LEVEL_NORMAL  2
#define ZASSERT_LEVEL_VERBOSE 3

#ifdef __cplusplus
extern "C" {
#endif

#ifndef CONFIG_ASSERT_TEST
FUNC_NORETURN
#endif
__printf_like(4, 5)
void zassert_fail(const char *cond, const char *file, unsigned int line, const char *fmt, ...);

#ifndef CONFIG_ASSERT_TEST
FUNC_NORETURN
#endif
void zassert_post_action(const char *file, unsigned int line);

__printf_like(1, 0)
void zassert_vprint(const char *fmt, va_list ap);


static inline __printf_like(1, 2) void zassert_print(const char *fmt, ...)
{
        va_list ap;

        va_start(ap, fmt);
        zassert_vprint(fmt, ap);
        va_end(ap);
}

#ifdef __cplusplus
}
#endif

/* @cond INTERNAL_HIDDEN */
/* Level of a named Kconfig module: CONFIG_ASSERT_MODULE_<module>_LEVEL. */
#define ZASSERT_IMPL_MODULE_LEVEL(module) UTIL_CAT(UTIL_CAT(CONFIG_ASSERT_MODULE_, module), _LEVEL)

/*
 * ZASSERT_MODULE(module)        -> CONFIG_ASSERT_MODULE_<module>_LEVEL
 * ZASSERT_MODULE(module, level) -> explicit level
 */
#define ZASSERT_IMPL_LEVEL_RESOLVE(...) \
        GET_ARG_N(2, __VA_ARGS__, ZASSERT_IMPL_MODULE_LEVEL(GET_ARG_N(1, __VA_ARGS__)), _)

#ifndef CONFIG_ASSERT
#define ZASSERT_IMPL(_level, _test, ...)
#define ZASSERT_IMPL_MODULE(...)
#else
#define ZASSERT_IMPL(_level, _test, ...)                                                \
        do {                                                                            \
                if ((_level) != ZASSERT_LEVEL_OFF && unlikely(!(_test))) {              \
                        switch ((_level)) {                                             \
                        case ZASSERT_LEVEL_VERBOSE:                                     \
                                zassert_fail(Z_STRINGIFY(_test), __FILE__, __LINE__,    \
                                             COND_CODE_1(IS_EMPTY(__VA_ARGS__),         \
                                                         (NULL), (__VA_ARGS__)));       \
                                break;                                                  \
                        case ZASSERT_LEVEL_NORMAL:                                      \
                                zassert_fail(NULL, __FILE__, __LINE__, NULL);           \
                                break;                                                  \
                        case ZASSERT_LEVEL_TERSE:                                       \
                                zassert_fail(NULL, NULL, 0, NULL);                      \
                                break;                                                  \
                        default: /* ZASSERT_LEVEL_OFF */                                \
                                break;                                                  \
                        }                                                               \
                }                                                                       \
        } while (false)

#define ZASSERT_IMPL_MODULE(...)                                                                \
        BUILD_ASSERT((ZASSERT_IMPL_LEVEL_RESOLVE(__VA_ARGS__)) >= ZASSERT_LEVEL_OFF &&          \
                             (ZASSERT_IMPL_LEVEL_RESOLVE(__VA_ARGS__)) <= ZASSERT_LEVEL_VERBOSE,\
                     "Invalid assert level");                                                   \
        static const int zassert_impl_level __unused =                                          \
                IS_ENABLED(CONFIG_ASSERT) ? (ZASSERT_IMPL_LEVEL_RESOLVE(__VA_ARGS__))           \
                                           : ZASSERT_LEVEL_OFF

#endif /* ifndef CONFIG_ASSERT */
#define ZASSERT_IMPL_LEVEL(_level, _test, ...)                                                  \
        do {                                                                                    \
                BUILD_ASSERT((_level) >= ZASSERT_LEVEL_OFF && (_level) <= ZASSERT_LEVEL_VERBOSE,\
                             "Invalid assert level");                                           \
                ZASSERT_IMPL(_level, _test, ##__VA_ARGS__);                                     \
        } while (false)
/* @endcond */

#define ZASSERT_TERSE(_test, ...) ZASSERT_IMPL_LEVEL(ZASSERT_LEVEL_TERSE, (_test), ##__VA_ARGS__)

#define ZASSERT_NORMAL(_test, ...) ZASSERT_IMPL_LEVEL(ZASSERT_LEVEL_NORMAL, (_test), ##__VA_ARGS__)

#define ZASSERT_VERBOSE(_test, ...) \
        ZASSERT_IMPL_LEVEL(ZASSERT_LEVEL_VERBOSE, (_test), ##__VA_ARGS__)

#define ZASSERT_MODULE(...) ZASSERT_IMPL_MODULE(__VA_ARGS__)
#define ZASSERT(_test, ...) ZASSERT_IMPL(zassert_impl_level, _test, ##__VA_ARGS__)


#endif /* ZEPHYR_INCLUDE_SYS_ZASSERT_H_ */
```

## 24.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Måns Ansgariusson <mansgariusson@gmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 32 行

按源文件细分的断言（Granular Per-Source-File Assertions）。

`ZASSERT_MODULE()` 使某个作用域（Scope）采用支持模块识别的 `ZASSERT()` 宏。生成的断言级别（Assertion Level）是编译时常量（Compile-Time Constant），因此优化器（Optimizer）会消除被禁用的断言；级别低于 `ZASSERT_LEVEL_VERBOSE` 时，还会消除消息及其参数。单个文件可以显式设置其级别，覆盖模块默认值（Module Default）。

对于头文件和内联函数（Inline Functions），应将 `ZASSERT_MODULE()` 放在函数体内，避免选择结果泄漏到包含者；也可以使用 `ZASSERT_TERSE()`、`ZASSERT_NORMAL()` 或 `ZASSERT_VERBOSE()`，创建固定级别的断言。

### 注释 3：原第 121 行

隐藏内部文档条件块（Hidden Internal Documentation Block）：`@cond INTERNAL_HIDDEN`。

### 注释 4：原第 122 行

具名 Kconfig 模块（Named Kconfig Module）的级别：`CONFIG_ASSERT_MODULE_<module>_LEVEL`。

### 注释 5：原第 125 行

`ZASSERT_MODULE(module)` → `CONFIG_ASSERT_MODULE_<module>_LEVEL`。
`ZASSERT_MODULE(module, level)` → 显式指定的级别（Explicit Level）。

### 注释 6：原第 151 行

断言关闭级别（Assertion Off Level）：`ZASSERT_LEVEL_OFF`。

### 注释 7：原第 165 行

条件编译（Conditional Compilation）：未定义 `CONFIG_ASSERT`（`ifndef CONFIG_ASSERT`）。

### 注释 8：原第 172 行

Doxygen 条件文档块结束标记：`@endcond`。

### 注释 9：原第 234 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SYS_ZASSERT_H_`。

## 24.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/zassert_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zassert_fail](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#ga72d07b4b0fb4190dc675813c0d9215b1)
- [zassert_post_action](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#ga98d7d44bfde093e6abe6cf51566c77d5)
- [zassert_vprint](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gadf431a5e2a87111d50cd268d309f3eea)
- [zassert_print](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gaf1c13156eb4331a95f2e396afb7736ba)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P023_usb_device.h_源码浏览.md) · [返回大纲](大纲.md)
