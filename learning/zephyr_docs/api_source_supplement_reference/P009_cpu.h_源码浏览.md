---
id: learning.zephyr-docs.api-source-supplement-reference.page-9
title: cpu.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arch_2cpu_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_cpu.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arch_2cpu_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arch_2cpu_8h.html)。

## 9.1\_原始可见代码（Source Code）

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
<a id="aarch_8h_html"></a>
<a id="aarch__interface_8h_html"></a>

```c
/* cpu.h - automatically selects the correct arch.h file to include */

/*
 * Copyright (c) 1997-2014 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ARCH_CPU_H_
#define ZEPHYR_INCLUDE_ARCH_CPU_H_

#include <zephyr/arch/arch_interface.h>

#if defined(CONFIG_X86)
#include <zephyr/arch/x86/arch.h>
#elif defined(CONFIG_ARM64)
#include <zephyr/arch/arm64/arch.h>
#elif defined(CONFIG_ARM)
#include <zephyr/arch/arm/arch.h>
#elif defined(CONFIG_ARC)
#include <zephyr/arch/arc/arch.h>
#elif defined(CONFIG_RISCV)
#include <zephyr/arch/riscv/arch.h>
#elif defined(CONFIG_XTENSA)
#include <zephyr/arch/xtensa/arch.h>
#elif defined(CONFIG_MIPS)
#include <zephyr/arch/mips/arch.h>
#elif defined(CONFIG_OPENRISC)
#include <zephyr/arch/openrisc/arch.h>
#elif defined(CONFIG_ARCH_POSIX)
#include <zephyr/arch/posix/arch.h>
#elif defined(CONFIG_SPARC)
#include <zephyr/arch/sparc/arch.h>
#elif defined(CONFIG_RX)
#include <zephyr/arch/rx/arch.h>
#elif defined(CONFIG_HEXAGON)
#include <zephyr/arch/hexagon/arch.h>
#elif defined(CONFIG_TRICORE)
#include <zephyr/arch/tricore/arch.h>
#elif defined(CONFIG_ARCH_IS_SET)
#error "The selected architecture is missing from this dispatch header"
#endif

#endif /* ZEPHYR_INCLUDE_ARCH_CPU_H_ */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`cpu.h`：自动选择要包含的正确 `arch.h` 文件。

### 注释 2：原第 3 行

版权（Copyright）：© 1997-2014 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 44 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_CPU_H_`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arch_2cpu_8h.html)
- [zephyr/arch/arch_interface.h](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)
- [zephyr/arch/tricore/arch.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_8h.html)
- [arch.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_8h.html)
- [arch_interface.h](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)

---

[上一章](P008_ans.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P010_irq.h_源码浏览.md)
