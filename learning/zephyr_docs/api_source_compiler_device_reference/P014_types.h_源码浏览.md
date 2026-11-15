---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-14
title: types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P160_zephyr__types.h_文件参考.md)。

## 14.1\_原始可见代码（Source Code）

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
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_aac7deaa1633720ec64bd432bbc31af40"></a>

```c
/*
 * Copyright (c) 2017 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_TYPES_H_
#define ZEPHYR_INCLUDE_TYPES_H_

#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
 * A type with strong alignment requirements, similar to C11 max_align_t. It can
 * be used to force alignment of data structures allocated on the stack or as
 * return * type for heap allocators.
 */
typedef union {
        long long       thelonglong;
        long double     thelongdouble;
        uintmax_t       theuintmax_t;
        size_t          thesize_t;
        uintptr_t       theuintptr_t;
        void            *thepvoid;
        void            (*thepfunc)(void);
} z_max_align_t;

/*
 * Thread local variables are declared with different keywords depending on
 * which C/C++ standard that is used. C++11 and C23 uses "thread_local" whilst
 * C11 uses "_Thread_local". Previously the GNU "__thread" keyword was used
 * which is the same in both gcc and g++.
 */
#ifndef Z_THREAD_LOCAL
#if defined(__cplusplus) && (__cplusplus) >= 201103L /* C++11 */
#define Z_THREAD_LOCAL thread_local
#elif defined(__STDC_VERSION__) && (__STDC_VERSION__) >= 202311L /* C23 */
#define Z_THREAD_LOCAL thread_local
#elif defined(__STDC_VERSION__) && (__STDC_VERSION__) >= 201112L /* C11 */
#define Z_THREAD_LOCAL _Thread_local
#else /* Default back to old behavior which used the GNU keyword. */
#define Z_THREAD_LOCAL __thread
#endif
#endif /* Z_THREAD_LOCAL */

#ifdef __cplusplus

#if (!__STDC_HOSTED__)
/*
 * Zephyr requires an int main(void) signature with C linkage for the
 * application main if present. gcc, and clang when building in 'hosted' mode
 * will correctly assume this. But, when building freestanding, clang does not
 * treat main() specially, and by default name mangles its symbol, which
 * results in the linker not linking from the kernel init code into this
 * name mangled app main().
 *
 * At the same time, according to the C++ standard Section 6.9.3.1 of
 * ISO/IEC 14882:2024, main cannot be explicitly declared to have "C" linkage.
 * This restriction is relaxed for freestanding code, as main is not treated
 * specially in these circumstances.
 * Therefore, let's include the prototype when we are not building the code as
 * freestanding/not-hosted.
 */
extern int main(void);
#endif

}
#endif

#endif /* ZEPHYR_INCLUDE_TYPES_H_ */
```

## 14.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 17 行

具有严格对齐要求（strong alignment requirements）的类型，类似于 C11 的 `max_align_t`。可用于强制对栈上分配的数据结构进行对齐，或作为堆分配器（heap allocators）返回指针所指向的类型。

### 注释 3：原第 32 行

线程局部变量（thread-local variables）的声明关键字随使用的 C/C++ 标准而不同。C++11 和 C23 使用 `thread_local`，C11 使用 `_Thread_local`。此前使用的是 GNU 的 `__thread` 关键字，它在 gcc 和 g++ 中相同。

### 注释 4：原第 39 行

C++11 标准分支。

### 注释 5：原第 41 行

C23 标准分支。

### 注释 6：原第 43 行

C11 标准分支。

### 注释 7：原第 45 行

默认回退到旧行为，使用 GNU 关键字。

### 注释 8：原第 48 行

`Z_THREAD_LOCAL` 宏标记。

### 注释 9：原第 53 行

如果应用程序提供主函数，Zephyr 要求其签名为 `int main(void)`，并使用 C 语言链接（C linkage）。gcc，以及在宿主模式（hosted mode）下构建时的 clang，会正确作出这一假定。但在独立式（freestanding）构建中，clang 不会特殊处理 `main()`，默认会对其符号进行名称修饰（name mangling），使链接器无法将内核初始化代码链接到经过名称修饰的应用程序 `main()`。

同时，根据 C++ 标准 ISO/IEC 14882:2024 第 6.9.3.1 节，不得显式声明 `main` 具有 C 语言链接。对于独立式代码，这项限制有所放宽，因为在这种情况下不会特殊处理 `main`。因此，原注释建议在“不是以独立式／非宿主方式构建”（not building ... as freestanding/not-hosted）时包含该原型。

译注：原注释最后一句的否定措辞按原文保留；具体包含条件请结合上方保留的预处理条件阅读。

### 注释 10：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_TYPES_H_`。

## 14.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [uintmax_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#aac7deaa1633720ec64bd432bbc31af40)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)

---

[上一章](P013_imx8qxp-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P015_intc_exti_stm32.h_源码浏览.md)
