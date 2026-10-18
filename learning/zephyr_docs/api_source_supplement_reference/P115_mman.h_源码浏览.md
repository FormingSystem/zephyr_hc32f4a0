---
id: learning.zephyr-docs.api-source-supplement-reference.page-115
title: mman.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mman_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第115章\_mman.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html)。

## 115.1\_原始可见代码（Source Code）

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
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_adb8322e115035a284aab704909e63d00"></a>
<a id="amman_8h_html_a01ff21bc70401bee9b80c350763087f7"></a>
<a id="amman_8h_html_a03b30383879c5b943ac4d4f9077aeb66"></a>
<a id="amman_8h_html_a14d35ac0e791a20d8773bfa13c456c2b"></a>
<a id="amman_8h_html_a4037e49e9537e24edd610bd1acf090da"></a>
<a id="amman_8h_html_a49da9349d68e3ced27b73c1b2e88ebf3"></a>
<a id="amman_8h_html_abef113c04cdf88b279b9d4204a63d448"></a>
<a id="amman_8h_html_ac2e7d057b16f0c959ffb39d8719eb1ed"></a>
<a id="amman_8h_html_ad3cfd73f8180a1a364cb57dc909bcb69"></a>
<a id="amman_8h_html_ad4697a198c5b65f462dc77e3699a4f03"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>

```c
/*
 * Copyright (c) 2024, Tenstorrent AI ULC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_SYS_MMAN_H_
#define ZEPHYR_INCLUDE_POSIX_SYS_MMAN_H_

#include <stddef.h>
#include <sys/types.h>

#define PROT_NONE  0x0
#define PROT_READ  0x1
#define PROT_WRITE 0x2
#define PROT_EXEC  0x4

#define MAP_SHARED  0x1
#define MAP_PRIVATE 0x2
#define MAP_FIXED   0x4

/* for Linux compatibility */
#define MAP_ANONYMOUS 0x20

#define MS_SYNC       0x0
#define MS_ASYNC      0x1
#define MS_INVALIDATE 0x2

#define MAP_FAILED ((void *)-1)

#define MCL_CURRENT 0
#define MCL_FUTURE  1

#ifdef __cplusplus
extern "C" {
#endif

int mlock(const void *addr, size_t len);
int mlockall(int flags);
void *mmap(void *addr, size_t len, int prot, int flags, int fildes, off_t off);
int msync(void *addr, size_t length, int flags);
int munlock(const void *addr, size_t len);
int munlockall(void);
int munmap(void *addr, size_t len);
int shm_open(const char *name, int oflag, mode_t mode);
int shm_unlink(const char *name);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_SYS_MMAN_H_ */
```

## 115.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024, Tenstorrent AI ULC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 22 行

用于 Linux 兼容。

### 注释 3：原第 52 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SYS_MMAN_H_`。

## 115.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [mlock](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html#a49da9349d68e3ced27b73c1b2e88ebf3)
- [mlockall](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html#ad4697a198c5b65f462dc77e3699a4f03)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [mmap](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html#ac2e7d057b16f0c959ffb39d8719eb1ed)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [msync](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html#abef113c04cdf88b279b9d4204a63d448)
- [munlock](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html#ad3cfd73f8180a1a364cb57dc909bcb69)
- [munlockall](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html#a03b30383879c5b943ac4d4f9077aeb66)
- [munmap](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html#a01ff21bc70401bee9b80c350763087f7)
- [shm_open](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html#a14d35ac0e791a20d8773bfa13c456c2b)
- [mode_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#adb8322e115035a284aab704909e63d00)
- [shm_unlink](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html#a4037e49e9537e24edd610bd1acf090da)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)

---

[上一章](P114_mic_privacy.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P116_uart.h_源码浏览.md)
