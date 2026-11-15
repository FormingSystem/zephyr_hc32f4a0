---
id: learning.zephyr-docs.api-source-supplement-reference.page-68
title: exc_handle.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/exc__handle_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_exc\_handle.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/exc__handle_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/exc__handle_8h.html)。

## 68.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2018 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ARCH_COMMON_EXC_HANDLE_H_
#define ZEPHYR_INCLUDE_ARCH_COMMON_EXC_HANDLE_H_

/*
 * This is used by some architectures to define code ranges which may
 * perform operations that could generate a CPU exception that should not
 * be fatal. Instead, the exception should return but set the program
 * counter to a 'fixup' memory address which will gracefully error out.
 *
 * For example, in the case where user mode passes in a C string via
 * system call, the length of that string needs to be measured. A specially
 * written assembly language version of strlen (arch_user_string_len)
 * defines start and end symbols where the memory in the string is examined;
 * if this generates a fault, jumping to the fixup symbol within the same
 * function will return an error result to the caller.
 *
 * To ensure precise control of the state of registers and the stack pointer,
 * these functions need to be written in assembly.
 *
 * The arch-specific fault handling code will define an array of these
 * z_exc_handle structures and return from the exception with the PC updated
 * to the fixup address if a match is found.
 */

struct z_exc_handle {
        void *start;
        void *end;
        void *fixup;
};

#define Z_EXC_HANDLE(name) \
        { name ## _fault_start, name ## _fault_end, name ## _fixup }

#define Z_EXC_DECLARE(name)          \
        void name ## _fault_start(void); \
        void name ## _fault_end(void);   \
        void name ## _fixup(void)

#endif /* ZEPHYR_INCLUDE_ARCH_COMMON_EXC_HANDLE_H_ */
```

## 68.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

某些架构使用此机制定义代码范围；这些范围内执行的操作可能引发 CPU 异常，但该异常不应成为致命错误。相反，应从异常返回，同时将程序计数器（Program counter）设为一个修复地址（Fixup address），由该处代码以受控方式返回错误。

例如，用户模式通过系统调用传入 C 字符串时，需要测量字符串长度。专门编写的汇编版 `strlen`（`arch_user_string_len`）定义起始和结束符号，标明检查字符串内存的代码范围。如果这一步触发故障，就跳转到同一函数内的修复符号，并向调用者返回错误结果。

为了精确控制寄存器和栈指针的状态，这些函数需要用汇编编写。

架构专用的故障处理代码会定义一个由 `z_exc_handle` 结构体组成的数组。如果找到匹配项，就将程序计数器（PC）更新为修复地址后从异常返回。

### 注释 3：原第 45 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_COMMON_EXC_HANDLE_H_`。

## 68.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/exc__handle_8h.html)

---

[上一章](P067_events.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P069_exception.h_源码浏览.md)
