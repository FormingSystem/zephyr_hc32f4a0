---
id: learning.zephyr-docs.api-source-supplement-reference.page-11
title: syscall.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2syscall_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_syscall.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2syscall_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2syscall_8h.html)。

## 11.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2025 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 * SPDX-FileCopyrightText: Copyright (c) 2026 Linumiz
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_ARCH_TRICORE_SYSCALL_H_
#define ZEPHYR_INCLUDE_ARCH_TRICORE_SYSCALL_H_


/* Syscall ids used */
#define TRICORE_SYSCALL_CALL        0
#define TRICORE_SYSCALL_SWITCH      1
#define TRICORE_SYSCALL_EXCEPT      2
#define TRICORE_SYSCALL_IRQ_OFFLOAD 3


#endif /* ZEPHYR_INCLUDE_ARCH_TRICORE_SYSCALL_H_ */
```

## 11.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2025 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Linumiz。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 22 行

所用的系统调用标识符（Syscall IDs）。

### 注释 3：原第 30 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_TRICORE_SYSCALL_H_`。

## 11.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arch_2tricore_2syscall_8h.html)

---

[上一章](P010_irq.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P012_thread.h_源码浏览.md)
