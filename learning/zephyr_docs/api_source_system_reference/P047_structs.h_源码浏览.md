---
id: learning.zephyr-docs.api-source-system-reference.page-47
title: structs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_structs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/structs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P475_zephyr__arch__structs.h_文件参考.md)。

## 47.1\_原始可见代码（Source Code）

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
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="atricore_2structs_8h_html"></a>

```c
/*
 * Copyright (c) BayLibre SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/*
 * The purpose of this file is to provide essential/minimal architecture-
 * specific structure definitions to be included in generic kernel
 * structures.
 *
 * The following rules must be observed:
 *  1. arch/structs.h shall not depend on kernel.h both directly and
 *     indirectly (i.e. it shall not include any header files that include
 *     kernel.h in their dependency chain).
 *  2. kernel.h shall imply arch/structs.h via kernel_structs.h , such that
 *     it shall not be necessary to include arch/structs.h explicitly when
 *     kernel.h is included.
 */

#ifndef ZEPHYR_INCLUDE_ARCH_STRUCTS_H_
#define ZEPHYR_INCLUDE_ARCH_STRUCTS_H_

#if !defined(_ASMLANGUAGE)

#if defined(CONFIG_ARM64)
#include <zephyr/arch/arm64/structs.h>
#elif defined(CONFIG_RISCV)
#include <zephyr/arch/riscv/structs.h>
#elif defined(CONFIG_ARM)
#include <zephyr/arch/arm/structs.h>
#elif defined(CONFIG_X86) && !defined(CONFIG_X86_64)
#include <zephyr/arch/x86/ia32/structs.h>
#elif defined(CONFIG_XTENSA)
#include <zephyr/arch/xtensa/structs.h>
#elif defined(CONFIG_TRICORE)
#include <zephyr/arch/tricore/structs.h>
#else

/* Default definitions when no architecture specific definitions exist. */

/* Per CPU architecture specifics (empty) */
struct _cpu_arch {
#ifdef __cplusplus
        /* An empty struct is not valid C, and compilers that accept it give
         * it size 0 while C++ gives 1. Keep a byte so both languages agree.
         */
        uint8_t dummy;
#endif
};

#endif

/* typedefs to be used with GEN_OFFSET_SYM(), etc. */
typedef struct _cpu_arch _cpu_arch_t;

#endif /* _ASMLANGUAGE */

#endif /* ZEPHYR_INCLUDE_ARCH_STRUCTS_H_ */
```

## 47.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© BayLibre SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 7 行

本文件提供供通用内核结构体（Generic Kernel Structures）包含的必要且最小的架构专用结构体定义（Architecture-Specific Structure Definitions）。

必须遵守以下规则：

1. `arch/structs.h` 不得直接或间接依赖 `kernel.h`，即不得包含依赖链（Dependency Chain）中包含 `kernel.h` 的任何头文件。
2. `kernel.h` 应通过 `kernel_structs.h` 隐式包含 `arch/structs.h`，从而在包含 `kernel.h` 后，无需再显式包含 `arch/structs.h`。

### 注释 3：原第 40 行

不存在架构专用定义（Architecture-Specific Definitions）时使用的默认定义（Default Definitions）。

### 注释 4：原第 42 行

每个 CPU 的架构专用部分（Per-CPU Architecture Specifics），此处为空。

### 注释 5：原第 45 行

空结构体（Empty Struct）不符合 C 语言要求；接受空结构体的编译器会将其大小设为 0，而 C++ 将其大小设为 1。保留一个字节，使两种语言的结果一致。

### 注释 6：原第 54 行

供 `GEN_OFFSET_SYM()` 等使用的类型定义（Typedefs）。

### 注释 7：原第 57 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 8：原第 59 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_STRUCTS_H_`。

## 47.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P475_zephyr__arch__structs.h_文件参考.md)
- [zephyr/arch/tricore/structs.h](../api_file_reference/P490_zephyr__arch__tricore__structs.h_文件参考.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [structs.h](../api_file_reference/P490_zephyr__arch__tricore__structs.h_文件参考.md)

---

[上一章](P046_stm32n6_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P048_tsl2540.h_源码浏览.md)
