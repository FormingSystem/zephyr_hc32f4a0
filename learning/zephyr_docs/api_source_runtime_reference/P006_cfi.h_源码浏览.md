---
id: learning.zephyr-docs.api-source-runtime-reference.page-6
title: cfi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cfi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_cfi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cfi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cfi_8h.html)。

## 6.1\_原始可见代码（Source Code）

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
<a id="aarch__interface_8h_html"></a>

```c
/*
 * Copyright (c) 2025 NXP Semicondutors
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/*
 * DWARF Control Flow Integrity (CFI) support for architectures.
 */

#ifndef ZEPHYR_INCLUDE_ARCH_CFI_H_
#define ZEPHYR_INCLUDE_ARCH_CFI_H_

#include <zephyr/arch/arch_interface.h>

#if defined(__GNUC__) || defined(__clang__)
/* DWARF Control Flow Integrity (CFI) support for architectures is only
 * supported by LLVM and GCC toolchains.
 */
#if defined(CONFIG_X86_64)
#include <zephyr/arch/x86/intel64/cfi.h>
#elif defined(CONFIG_X86)
#include <zephyr/arch/x86/ia32/cfi.h>
#elif defined(CONFIG_ARM64)
#include <zephyr/arch/arm64/cfi.h>
#elif defined(CONFIG_ARM)
#include <zephyr/arch/arm/cfi.h>
#elif defined(CONFIG_RISCV)
#include <zephyr/arch/riscv/cfi.h>
#endif
#endif

/*
 * Inform the unwinder that the return address is undefined.
 * This prevents bogus unwinding and potential faults.
 */
#ifndef ARCH_CFI_UNDEFINED_RETURN_ADDRESS
#define ARCH_CFI_UNDEFINED_RETURN_ADDRESS()
#endif

#endif /* ZEPHYR_INCLUDE_ARCH_CFI_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 NXP Semicondutors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 7 行

面向架构的 DWARF CFI 支持；原注释将 CFI 展开为控制流完整性（Control Flow Integrity）。

### 注释 3：原第 17 行

面向架构的 DWARF CFI 支持仅适用于 LLVM 和 GCC 工具链；原注释的全称为 Control Flow Integrity。

### 注释 4：原第 33 行

通知栈展开器（Unwinder）返回地址未定义，以避免错误的栈展开及潜在故障。

### 注释 5：原第 41 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_CFI_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cfi_8h.html)
- [zephyr/arch/arch_interface.h](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)
- [arch_interface.h](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)

---

[上一章](P005_ccs811.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_charger.h_源码浏览.md)
