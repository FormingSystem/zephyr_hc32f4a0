---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-6
title: libc-hooks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/libc-hooks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_libc-hooks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/libc-hooks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P188_zephyr__sys__libc-hooks.h_文件参考.md)。

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
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="aapp__memdomain_8h_html"></a>
<a id="alibc-hooks_8h_html_ac5b3b7e59825b80ba65bb6346ee88e3c"></a>
<a id="astdio_8h_html"></a>
<a id="astdio_8h_html_ac15bbd02a147d1595cdfb8b2979693d7"></a>
<a id="astructk__mem__partition_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2018, Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SYS_LIBC_HOOKS_H_
#define ZEPHYR_INCLUDE_SYS_LIBC_HOOKS_H_

#include <zephyr/toolchain.h>
#include <zephyr/app_memory/app_memdomain.h>
#include <stdio.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Private header for specifying accessory functions to the C library internals
 * that need to call into the kernel as system calls
 */

#if defined(CONFIG_NEWLIB_LIBC) || defined(CONFIG_ARCMWDT_LIBC)

/* syscall generation ignores preprocessor, ensure this is defined to ensure
 * we don't have compile errors
 */
__syscall int zephyr_read_stdin(char *buf, int nbytes);

__syscall int zephyr_write_stdout(const void *buf, int nbytes);

#else
/* Minimal libc and picolibc */

__syscall int zephyr_fputc(int c, FILE * stream);

#ifdef CONFIG_MINIMAL_LIBC
/* Minimal libc only */

__syscall size_t zephyr_fwrite(const void *ZRESTRICT ptr, size_t size,
                                size_t nitems, FILE *ZRESTRICT stream);
#endif

#endif /* CONFIG_NEWLIB_LIBC */

void __stdout_hook_install(int (*hook)(int c));

#ifdef CONFIG_USERSPACE
#ifdef CONFIG_COMMON_LIBC_MALLOC

/* When using the common malloc implementation with CONFIG_USERSPACE, the
 * heap will be in a separate partition when there's an MPU or MMU
 * available.
 */
#if CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE != 0 && \
(defined(CONFIG_MPU) || defined(CONFIG_MMU))
#define Z_MALLOC_PARTITION_EXISTS 1
#endif

#elif defined(CONFIG_NEWLIB_LIBC) && !defined(CONFIG_NEWLIB_LIBC_CUSTOM_SBRK)
/* If we are using newlib, the heap arena is in one of two areas:
 *  - If we have an MPU that requires power of two alignment, the heap bounds
 *    must be specified in Kconfig via CONFIG_NEWLIB_LIBC_ALIGNED_HEAP_SIZE.
 *  - Otherwise, the heap arena on most arches starts at a suitably
 *    aligned base address after the `_end` linker symbol, through to the end
 *    of system RAM.
 */
#if (!defined(CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT) || \
     (defined(CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT) && \
      CONFIG_NEWLIB_LIBC_ALIGNED_HEAP_SIZE))
#define Z_MALLOC_PARTITION_EXISTS 1
#endif

#endif /* CONFIG_NEWLIB_LIBC */

#ifdef Z_MALLOC_PARTITION_EXISTS
/* Memory partition containing the libc malloc arena. Configuration controls
 * whether this is available, and an arena size may need to be set.
 */
extern struct k_mem_partition z_malloc_partition;
#endif

#ifdef CONFIG_NEED_LIBC_MEM_PARTITION
/* - All newlib globals will be placed into z_libc_partition.
 * - Minimal C library globals, if any, will be placed into
 *   z_libc_partition.
 * - Stack canary globals will be placed into z_libc_partition since
 *   it is not worth placing in its own partition.
 * - Some architectures may place the global pointer to the thread local
 *   storage in z_libc_partition since it is not worth placing in its
 *   own partition.
 */
#define Z_LIBC_PARTITION_EXISTS 1

/* C library globals, except the malloc arena */
extern struct k_mem_partition z_libc_partition;
#endif
#endif /* CONFIG_USERSPACE */

#include <zephyr/syscalls/libc-hooks.h>

/* C library memory partitions */
#define Z_LIBC_DATA K_APP_DMEM(z_libc_partition)

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SYS_LIBC_HOOKS_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018, Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 19 行

私有头文件，用于声明 C 库内部需要通过系统调用（system calls）进入内核的辅助函数。

### 注释 3：原第 26 行

系统调用生成过程忽略预处理器，因此确保定义此项，以免出现编译错误。

### 注释 4：原第 34 行

最小 C 库（Minimal libc）和 picolibc。

### 注释 5：原第 39 行

仅最小 C 库（Minimal libc）。

### 注释 6：原第 45 行

条件编译配置（Configuration）标记：`CONFIG_NEWLIB_LIBC`。

### 注释 7：原第 52 行

在启用 `CONFIG_USERSPACE` 的情况下使用公共 `malloc` 实现时，如果提供了内存保护单元（MPU）或内存管理单元（MMU），堆将位于独立分区（partition）中。

### 注释 8：原第 62 行

使用 newlib 时，堆区（heap arena）位于以下两类区域之一：

- 如果 MPU 要求按 2 的幂对齐，则必须通过 Kconfig 选项 `CONFIG_NEWLIB_LIBC_ALIGNED_HEAP_SIZE` 指定堆边界。
- 否则，在多数架构上，堆区从链接器符号 `_end` 之后满足适当对齐要求的基地址开始，一直延伸到系统 RAM 末端。

### 注释 9：原第 75 行

条件编译配置（Configuration）标记：`CONFIG_NEWLIB_LIBC`。

### 注释 10：原第 78 行

包含 libc `malloc` 堆区（arena）的内存分区。该分区是否可用由配置决定，可能还需要设置堆区大小。

### 注释 11：原第 85 行

- 所有 newlib 全局变量均放入 `z_libc_partition`。
- 最小 C 库如有全局变量，也放入 `z_libc_partition`。
- 栈保护哨兵（stack canary）的全局变量放入 `z_libc_partition`，因为没有必要为它们单独建立分区。
- 部分架构可能将指向线程局部存储（thread-local storage）的全局指针放入 `z_libc_partition`，同样因为没有必要单独建立分区。

### 注释 12：原第 96 行

C 库全局变量，不包括 `malloc` 堆区（arena）。

### 注释 13：原第 99 行

条件编译配置（Configuration）标记：`CONFIG_USERSPACE`。

### 注释 14：原第 103 行

C 库内存分区（memory partitions）。

### 注释 15：原第 110 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SYS_LIBC_HOOKS_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P188_zephyr__sys__libc-hooks.h_文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/app_memory/app_memdomain.h](../memory_domain_reference/P009_应用内存域头文件参考.md)
- [stdio.h](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md)
- [zephyr_fputc](../api_file_reference/P188_zephyr__sys__libc-hooks.h_文件参考.md#ac5b3b7e59825b80ba65bb6346ee88e3c)
- [FILE](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#ac15bbd02a147d1595cdfb8b2979693d7)
- [k_mem_partition](../memory_domain_reference/P005_内存分区结构.md)
- [app_memdomain.h](../memory_domain_reference/P009_应用内存域头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P005_interrupt_util.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_max32664c.h_源码浏览.md)
