---
id: learning.zephyr-docs.api-file-reference.page-227
title: zephyr__posix__sys__mman.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第227章\_zephyr\_\_posix\_\_sys\_\_mman.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mman_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stddef.h>
#include <sys/types.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 227.1\_宏定义（Macros）

<a id="r_a6a982b48b8d3eb8eccd17e0d54ee5379"></a>

```c
#define PROT_NONE 0x0
```

相关声明：[PROT_NONE](#a6a982b48b8d3eb8eccd17e0d54ee5379)。

<a id="r_a15bf68ce8b590838b3a5c0b639d8d519"></a>

```c
#define PROT_READ 0x1
```

相关声明：[PROT_READ](#a15bf68ce8b590838b3a5c0b639d8d519)。

<a id="r_a2a79c8ceefb8fc25a940ae07a3d94429"></a>

```c
#define PROT_WRITE 0x2
```

相关声明：[PROT_WRITE](#a2a79c8ceefb8fc25a940ae07a3d94429)。

<a id="r_a77848f068638e916c72cd543f5ecb815"></a>

```c
#define PROT_EXEC 0x4
```

相关声明：[PROT_EXEC](#a77848f068638e916c72cd543f5ecb815)。

<a id="r_a57028962c2a7c0c802ca6613492f2ef3"></a>

```c
#define MAP_SHARED 0x1
```

相关声明：[MAP_SHARED](#a57028962c2a7c0c802ca6613492f2ef3)。

<a id="r_a398ef47a991a44389aa9818c98a28d24"></a>

```c
#define MAP_PRIVATE 0x2
```

相关声明：[MAP_PRIVATE](#a398ef47a991a44389aa9818c98a28d24)。

<a id="r_a387ec707b30c5e78cf20a14517a63b96"></a>

```c
#define MAP_FIXED 0x4
```

相关声明：[MAP_FIXED](#a387ec707b30c5e78cf20a14517a63b96)。

<a id="r_ae4f86bff73414c5fc08c058f957212f0"></a>

```c
#define MAP_ANONYMOUS 0x20
```

相关声明：[MAP_ANONYMOUS](#ae4f86bff73414c5fc08c058f957212f0)。

<a id="r_aee74e153705852ce48dca911f1b94d72"></a>

```c
#define MS_SYNC 0x0
```

相关声明：[MS_SYNC](#aee74e153705852ce48dca911f1b94d72)。

<a id="r_a98930d8c4137a6cf3f9e21b2b7c84c24"></a>

```c
#define MS_ASYNC 0x1
```

相关声明：[MS_ASYNC](#a98930d8c4137a6cf3f9e21b2b7c84c24)。

<a id="r_ad094236c94cb5fcfd6a663b646782bc8"></a>

```c
#define MS_INVALIDATE 0x2
```

相关声明：[MS_INVALIDATE](#ad094236c94cb5fcfd6a663b646782bc8)。

<a id="r_a8523dcf952f6ff059a3bed717e4f1296"></a>

```c
#define MAP_FAILED ((void *)-1)
```

相关声明：[MAP_FAILED](#a8523dcf952f6ff059a3bed717e4f1296)。

<a id="r_a22408a60244fd4662ed07d8afd74f8d0"></a>

```c
#define MCL_CURRENT 0
```

相关声明：[MCL_CURRENT](#a22408a60244fd4662ed07d8afd74f8d0)。

<a id="r_a403c070913f388ac8d97521f949533ae"></a>

```c
#define MCL_FUTURE 1
```

相关声明：[MCL_FUTURE](#a403c070913f388ac8d97521f949533ae)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 227.2\_函数（Functions）

<a id="r_a49da9349d68e3ced27b73c1b2e88ebf3"></a>

```c
int mlock (const void *addr, size_t len)
```

相关声明：[mlock](#a49da9349d68e3ced27b73c1b2e88ebf3)。

<a id="r_ad4697a198c5b65f462dc77e3699a4f03"></a>

```c
int mlockall (int flags)
```

相关声明：[mlockall](#ad4697a198c5b65f462dc77e3699a4f03)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_ac2e7d057b16f0c959ffb39d8719eb1ed"></a>

```c
void * mmap (void *addr, size_t len, int prot, int flags, int fildes, off_t off)
```

相关声明：[mmap](#ac2e7d057b16f0c959ffb39d8719eb1ed)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[off_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

<a id="r_abef113c04cdf88b279b9d4204a63d448"></a>

```c
int msync (void *addr, size_t length, int flags)
```

相关声明：[msync](#abef113c04cdf88b279b9d4204a63d448)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_ad3cfd73f8180a1a364cb57dc909bcb69"></a>

```c
int munlock (const void *addr, size_t len)
```

相关声明：[munlock](#ad3cfd73f8180a1a364cb57dc909bcb69)。

<a id="r_a03b30383879c5b943ac4d4f9077aeb66"></a>

```c
int munlockall (void)
```

相关声明：[munlockall](#a03b30383879c5b943ac4d4f9077aeb66)。

<a id="r_a01ff21bc70401bee9b80c350763087f7"></a>

```c
int munmap (void *addr, size_t len)
```

相关声明：[munmap](#a01ff21bc70401bee9b80c350763087f7)。

<a id="r_a14d35ac0e791a20d8773bfa13c456c2b"></a>

```c
int shm_open (const char *name, int oflag, mode_t mode)
```

相关声明：[shm_open](#a14d35ac0e791a20d8773bfa13c456c2b)、[mode_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#adb8322e115035a284aab704909e63d00)。

<a id="r_a4037e49e9537e24edd610bd1acf090da"></a>

```c
int shm_unlink (const char *name)
```

相关声明：[shm_unlink](#a4037e49e9537e24edd610bd1acf090da)。

## 227.3\_详细说明（Detailed Documentation）

<a id="ae4f86bff73414c5fc08c058f957212f0"></a>

### `MAP_ANONYMOUS`

```c
#define MAP_ANONYMOUS 0x20
```

<a id="a8523dcf952f6ff059a3bed717e4f1296"></a>

### `MAP_FAILED`

```c
#define MAP_FAILED ((void *)-1)
```

<a id="a387ec707b30c5e78cf20a14517a63b96"></a>

### `MAP_FIXED`

```c
#define MAP_FIXED 0x4
```

<a id="a398ef47a991a44389aa9818c98a28d24"></a>

### `MAP_PRIVATE`

```c
#define MAP_PRIVATE 0x2
```

<a id="a57028962c2a7c0c802ca6613492f2ef3"></a>

### `MAP_SHARED`

```c
#define MAP_SHARED 0x1
```

<a id="a22408a60244fd4662ed07d8afd74f8d0"></a>

### `MCL_CURRENT`

```c
#define MCL_CURRENT 0
```

<a id="a403c070913f388ac8d97521f949533ae"></a>

### `MCL_FUTURE`

```c
#define MCL_FUTURE 1
```

<a id="a98930d8c4137a6cf3f9e21b2b7c84c24"></a>

### `MS_ASYNC`

```c
#define MS_ASYNC 0x1
```

<a id="ad094236c94cb5fcfd6a663b646782bc8"></a>

### `MS_INVALIDATE`

```c
#define MS_INVALIDATE 0x2
```

<a id="aee74e153705852ce48dca911f1b94d72"></a>

### `MS_SYNC`

```c
#define MS_SYNC 0x0
```

<a id="a77848f068638e916c72cd543f5ecb815"></a>

### `PROT_EXEC`

```c
#define PROT_EXEC 0x4
```

<a id="a6a982b48b8d3eb8eccd17e0d54ee5379"></a>

### `PROT_NONE`

```c
#define PROT_NONE 0x0
```

<a id="a15bf68ce8b590838b3a5c0b639d8d519"></a>

### `PROT_READ`

```c
#define PROT_READ 0x1
```

<a id="a2a79c8ceefb8fc25a940ae07a3d94429"></a>

### `PROT_WRITE`

```c
#define PROT_WRITE 0x2
```

<a id="a49da9349d68e3ced27b73c1b2e88ebf3"></a>

### `mlock()`

```c
int mlock ( const void * addr, size_t len )
```

<a id="ad4697a198c5b65f462dc77e3699a4f03"></a>

### `mlockall()`

```c
int mlockall ( int flags)
```

<a id="ac2e7d057b16f0c959ffb39d8719eb1ed"></a>

### `mmap()`

```c
void * mmap ( void * addr, size_t len, int prot, int flags, int fildes, off_t off )
```

<a id="abef113c04cdf88b279b9d4204a63d448"></a>

### `msync()`

```c
int msync ( void * addr, size_t length, int flags )
```

<a id="ad3cfd73f8180a1a364cb57dc909bcb69"></a>

### `munlock()`

```c
int munlock ( const void * addr, size_t len )
```

<a id="a03b30383879c5b943ac4d4f9077aeb66"></a>

### `munlockall()`

```c
int munlockall ( void )
```

<a id="a01ff21bc70401bee9b80c350763087f7"></a>

### `munmap()`

```c
int munmap ( void * addr, size_t len )
```

<a id="a14d35ac0e791a20d8773bfa13c456c2b"></a>

### `shm_open()`

```c
int shm_open ( const char * name, int oflag, mode_t mode )
```

<a id="a4037e49e9537e24edd610bd1acf090da"></a>

### `shm_unlink()`

```c
int shm_unlink ( const char * name)
```


## 227.4\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P115_mman.h_源码浏览.md)
- [flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [off_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [mode_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#adb8322e115035a284aab704909e63d00)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P226_zephyr__drivers__mm__mm_drv_intel_adsp_mtl_tlb.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P228_zephyr__modem__backend__tty.h_文件参考.md)
