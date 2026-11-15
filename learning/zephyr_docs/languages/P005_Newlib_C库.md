---
id: learning.zephyr-docs.languages.libc-newlib
title: Newlib_C库
kind: reference
status: maintained
domains: [zephyr, languages]
source_url: https://docs.zephyrproject.org/latest/develop/languages/c/newlib.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第5章\_Newlib_C库

原文：[Newlib](https://docs.zephyrproject.org/latest/develop/languages/c/newlib.html)。读取日期：2026-10-12，`latest`。

**Newlib（面向嵌入式系统的C标准库项目）**提供较完整的 C 库实现。它是[独立开源项目](https://sourceware.org/newlib/)，Zephyr 不直接包含其库实现源码，而由 **Zephyr软件开发工具包（Software Development Kit，SDK）**为支持的架构提供预编译库 `libc.a` 和数学库 `libm.a`。

> 原文注意：GNU Arm Embedded 等第三方工具链也会随附预编译 Newlib。

Zephyr 提供 Newlib 标准函数会调用的 **API钩子（Application Programming Interface Hook）**，实现在 `lib/libc/newlib/libc-hooks.c`。这些钩子将库内部的系统调用转换为相应 Zephyr 接口调用。

## 5.1\_完整与精简两种版本

Zephyr SDK 中的 Newlib 有 **完整版（Full Newlib）**和 **精简版（Nano Newlib）**两种变体。

### 5.1.1\_完整版

完整版的库文件为 `libc.a` 和 `libm.a`，支持几乎全部标准 C 库功能。它优先优化性能而不是代码体积，资源占用明显大于精简版。

在应用配置中启用 Kconfig 选项 [CONFIG_NEWLIB_LIBC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEWLIB_LIBC)，同时不启用 [CONFIG_NEWLIB_LIBC_NANO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEWLIB_LIBC_NANO)，即可选择完整版。

### 5.1.2\_精简版

精简版文件为 `libc_nano.a` 和 `libm_nano.a`，以减小体积为目标。原文说明它支持完整版的功能，但不支持 C99 新增的部分格式说明，例如 `char` 对应的 `%hhX` 和 `long long` 对应的 `%llX`。

在应用配置中同时启用 `CONFIG_NEWLIB_LIBC` 与 `CONFIG_NEWLIB_LIBC_NANO` 可选择精简版。并非所有架构都有这一变体，是否可用由 Kconfig 选项 `CONFIG_HAS_NEWLIB_LIBC_NANO` 表达。

## 5.2\_格式化输入输出

Newlib 支持 `printf`、`fprintf`、`sprintf`、`sscanf` 等标准 **格式化输入输出（Formatted Input/Output）**函数。支持标准格式说明符时有以下例外：

1. `%f` 等浮点格式需要相应配置：输出启用 [CONFIG_NEWLIB_LIBC_FLOAT_PRINTF](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEWLIB_LIBC_FLOAT_PRINTF)，输入启用 [CONFIG_NEWLIB_LIBC_FLOAT_SCANF](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEWLIB_LIBC_FLOAT_SCANF)。
2. Nano 变体不支持下列 C99 格式说明：`char` 的 `%hhX`、`long long` 的 `%llX`、`intmax_t` 的 `%jX`、`size_t` 的 `%zX`、`ptrdiff_t` 的 `%tX`。

> 译注：这里讨论的是运行库格式处理能力，不是这些 C 类型能否出现在应用代码中。启用浮点输入和浮点输出也是两个独立选择，按实际调用函数配置。

## 5.3\_动态内存管理

Newlib 有自己的内部**堆分配器（Heap Allocator）**，管理 [malloc()](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#a9c36d0fe3ec4675cbffdc9b52f5fb399)、[free()](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#afbedc913aa4651b3c3b4b3aecd9b4711) 等标准动态内存接口使用的内存块。

不同变体的分配器可能不同。例如 Zephyr SDK 的完整版向操作系统请求较大的内存块，因此最低内存需求明显高于 Nano 版。

Newlib 分配器与 Zephyr 侧 C 库钩子之间的接口是 `sbrk()`，用于调整供内部堆分配器使用的内存池大小。`libc-hooks.c` 中的 `_sbrk()` 钩子处理这些请求；当系统内存不足时返回错误，避免内存池超过可用空间。

启用**用户空间（Userspace）**时，该内存池位于 `z_malloc_partition` 专用内存分区，供用户态线程访问。

可用堆空间大小取决于系统配置：

| 配置条件 | Newlib堆空间 |
| --- | --- |
| 启用**内存管理单元（Memory Management Unit，MMU）**，即 [CONFIG_MMU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MMU) | 取 [k_mem_free_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gabb315b4994193147e9f51b0c3268bfcd) 返回的空闲空间与 [CONFIG_NEWLIB_LIBC_MAX_MAPPED_REGION_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEWLIB_LIBC_MAX_MAPPED_REGION_SIZE) 中较小者。 |
| 启用**内存保护单元（Memory Protection Unit，MPU）**，且它要求分区大小为2的幂并按大小对齐，`CONFIG_NEWLIB_LIBC_ALIGNED_HEAP_SIZE` 非零 | 由 [CONFIG_NEWLIB_LIBC_ALIGNED_HEAP_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEWLIB_LIBC_ALIGNED_HEAP_SIZE) 指定。 |
| 其他情况 | 使用**静态随机存取存储器（Static Random-Access Memory，SRAM）**区域中尚未分配的空间。 |

Newlib 提供的标准动态内存函数具备**线程安全性（Thread Safety）**，可由多个线程同时调用。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：最小C库](P004_最小C库.md) · [本模块主线目录](../reading/languages.md) · [全部主线](../reading/README.md) · [下一篇：Picolibc_C库](P006_Picolibc_C库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：最小C库](P004_最小C库.md) · [下一章：Picolibc](P006_Picolibc_C库.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
