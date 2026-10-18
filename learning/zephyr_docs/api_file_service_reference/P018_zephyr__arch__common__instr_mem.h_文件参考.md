---
id: learning.zephyr-docs.api-file-service-reference.page-18
title: zephyr__arch__common__instr_mem.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/instr__mem_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_arch\_\_common\_\_instr\_mem.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/instr__mem_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

指令内存（Instruction Memory）的公共API。

<a id="details"></a>

```c
#include <zephyr/sys/util.h>
```

查看此文件的源码。

指令内存（Instruction Memory）的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.1\_函数（Functions）

<a id="r_ga61c79df57849b7e914cd33e0de4316a3"></a>

```c
bool arch_is_instr_mem (const void *addr, size_t len)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[arch_is_instr_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#ga61c79df57849b7e914cd33e0de4316a3)。

检查区域（Region）是否位于指令内存（Instruction Memory）。

<a id="r_gae80e1083bf80acaf0466d0bc2fe96bb4"></a>

```c
void * arch_memset_instr (void *buf, int c, size_t n)
```

相关声明：[arch_memset_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#gae80e1083bf80acaf0466d0bc2fe96bb4)。

对指令内存（Instruction Memory）中的缓冲区执行内存填充（Memset）。

<a id="r_ga506986b790b95fca0423e4c47690b1fe"></a>

```c
void * arch_memcpy_to_instr (void *d, const void *s, size_t n)
```

相关声明：[arch_memcpy_to_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#ga506986b790b95fca0423e4c47690b1fe)。

将缓冲区从数据内存（Data Memory）复制（Memcpy）到指令内存（Instruction Memory）。

<a id="r_ga03af01659004f2d96438b948f8c065a9"></a>

```c
void * arch_memcpy_from_instr (void *d, const void *s, size_t n)
```

相关声明：[arch_memcpy_from_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#ga03af01659004f2d96438b948f8c065a9)。

将缓冲区从指令内存（Instruction Memory）复制（Memcpy）到数据内存（Data Memory）。


## 18.2\_原页交叉引用（Cross References）

- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P391_instr_mem.h_源码浏览.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [arch_is_instr_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#ga61c79df57849b7e914cd33e0de4316a3)
- [arch_memset_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#gae80e1083bf80acaf0466d0bc2fe96bb4)
- [arch_memcpy_to_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#ga506986b790b95fca0423e4c47690b1fe)
- [arch_memcpy_from_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#ga03af01659004f2d96438b948f8c065a9)

<a id="header-details"></a>

---

[上一章](P017_zephyr__llext__inspect.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__dt-bindings__gpio__ite-it8xxx2-gpio.h_文件参考.md)
