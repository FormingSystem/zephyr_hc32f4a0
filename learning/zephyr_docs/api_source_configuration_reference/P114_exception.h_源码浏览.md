---
id: learning.zephyr-docs.api-source-configuration-reference.page-114
title: exception.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tricore_2exception_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第114章\_exception.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tricore_2exception_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tricore_2exception_8h.html)。

## 114.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
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
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2025 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 * SPDX-FileCopyrightText: Copyright (c) 2026 Linumiz
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_ARCH_TRICORE_EXCEPTION_H_
#define ZEPHYR_INCLUDE_ARCH_TRICORE_EXCEPTION_H_

#ifndef _ASMLANGUAGE
#include <zephyr/types.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif


/* TriCore Exception Stack Frame is the lower context*/
struct arch_esf {
        uint32_t pcxi;
        uint32_t a11;
        uint32_t a2;
        uint32_t a3;
        uint32_t d0;
        uint32_t d1;
        uint32_t d2;
        uint32_t d3;
        uint32_t a4;
        uint32_t a5;
        uint32_t a6;
        uint32_t a7;
        uint32_t d4;
        uint32_t d5;
        uint32_t d6;
        uint32_t d7;
};

#define TRICORE_TRAP_MMU                          0
#define TRICORE_TRAP_INTERNAL_PROTECTION_TRAPS    1
#define TRICORE_TRAP_INSTRUCTION_ERRORS           2
#define TRICORE_TRAP_CONTEXT_MANAGEMENT           3
#define TRICORE_TRAP_SYSTEM_BUS_PERIPHERAL_ERRORS 4
#define TRICORE_TRAP_ASSERTION_TRAPS              5
#define TRICORE_TRAP_SYSTEM_CALL                  6
#define TRICORE_TRAP_NMI                          7

/* Trap identification numbers (TIN) */
#define TRICORE_TRAP0_VAF 0
#define TRICORE_TRAP0_VAP 1

#define TRICORE_TRAP1_PRIV 1
#define TRICORE_TRAP1_MPR  2
#define TRICORE_TRAP1_MPW  3
#define TRICORE_TRAP1_MPX  4
#define TRICORE_TRAP1_MPP  5
#define TRICORE_TRAP1_MPN  6
#define TRICORE_TRAP1_GRWP 7

#define TRICORE_TRAP2_IOPC 1
#define TRICORE_TRAP2_UOPC 2
#define TRICORE_TRAP2_OPD  3
#define TRICORE_TRAP2_ALN  4
#define TRICORE_TRAP2_MEM  5
#define TRICORE_TRAP2_CSE  6

#define TRICORE_TRAP3_FCD  1
#define TRICORE_TRAP3_CDO  2
#define TRICORE_TRAP3_CDU  3
#define TRICORE_TRAP3_FCU  4
#define TRICORE_TRAP3_CSU  5
#define TRICORE_TRAP3_CTYP 6
#define TRICORE_TRAP3_NEST 7

#define TRICORE_TRAP4_PSE 1
#define TRICORE_TRAP4_DSE 2
#define TRICORE_TRAP4_DAE 3
#define TRICORE_TRAP4_CAE 4
#define TRICORE_TRAP4_PIE 5
#define TRICORE_TRAP4_DIE 6
#define TRICORE_TRAP4_TAE 7

#define TRICORE_TRAP5_OVF  1
#define TRICORE_TRAP5_SOVF 2


#ifdef __cplusplus
}
#endif
#endif
#endif
```

## 114.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2025 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Linumiz。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 29 行

TriCore 异常栈帧（Exception Stack Frame）是下层上下文（Lower context）。

### 注释 3：原第 58 行

陷阱标识号（Trap identification numbers，TIN）。

## 114.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tricore_2exception_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P113_test_asm_inline_gcc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P115_uart_console.h_源码浏览.md)
