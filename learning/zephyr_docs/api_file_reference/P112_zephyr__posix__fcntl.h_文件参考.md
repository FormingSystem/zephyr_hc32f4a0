---
id: learning.zephyr-docs.api-file-reference.page-112
title: zephyr__posix__fcntl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fcntl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第112章\_zephyr\_\_posix\_\_fcntl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fcntl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/fdtable.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 112.1\_宏定义（Macros）

<a id="r_ae036f789407d21f07b211552d67b3214"></a>

```c
#define O_APPEND ZVFS_O_APPEND
```

相关声明：[O_APPEND](#ae036f789407d21f07b211552d67b3214)、[ZVFS_O_APPEND](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#afa29fb3c7ff76f1e6cf2d69947865163)。

<a id="r_a1cf6b1de1fffedaa1d26b189e9a8d2cc"></a>

```c
#define O_CREAT ZVFS_O_CREAT
```

相关声明：[O_CREAT](#a1cf6b1de1fffedaa1d26b189e9a8d2cc)、[ZVFS_O_CREAT](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aff3387bcd512c9bea99c94aa3c459214)。

<a id="r_a9f5acfe79fafe14b6694447bd0e9f10b"></a>

```c
#define O_EXCL ZVFS_O_EXCL
```

相关声明：[O_EXCL](#a9f5acfe79fafe14b6694447bd0e9f10b)、[ZVFS_O_EXCL](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a2cb7a8f1c86ab67839458f0bc4198515)。

<a id="r_a39d33ce33804efd4d52606d59071c6d8"></a>

```c
#define O_NONBLOCK ZVFS_O_NONBLOCK
```

相关声明：[O_NONBLOCK](#a39d33ce33804efd4d52606d59071c6d8)、[ZVFS_O_NONBLOCK](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a122add73257644aab0689853c57c53f3)。

<a id="r_ad1d67e453fb3031f40f8cd3403773813"></a>

```c
#define O_TRUNC ZVFS_O_TRUNC
```

相关声明：[O_TRUNC](#ad1d67e453fb3031f40f8cd3403773813)、[ZVFS_O_TRUNC](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aecd7cfa3a9afdf22aac7b90911f4f459)。

<a id="r_a4dc4d45e07d2abc899bcaf04b2846a87"></a>

```c
#define O_ACCMODE (ZVFS_O_RDONLY | ZVFS_O_RDWR | ZVFS_O_WRONLY)
```

相关声明：[O_ACCMODE](#a4dc4d45e07d2abc899bcaf04b2846a87)、[ZVFS_O_RDONLY](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a1aeb8126a4c817bdd2740a93f191de16)、[ZVFS_O_RDWR](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a82be0ad3089fdd844137845fa50d6e21)、[ZVFS_O_WRONLY](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#abf07c70a006713aaed00a82ed87fb2be)。

<a id="r_a7a68c9ffaac7dbcd652225dd7c06a54b"></a>

```c
#define O_RDONLY ZVFS_O_RDONLY
```

相关声明：[O_RDONLY](#a7a68c9ffaac7dbcd652225dd7c06a54b)、[ZVFS_O_RDONLY](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a1aeb8126a4c817bdd2740a93f191de16)。

<a id="r_abb0586253488ee61072b73557eeb873b"></a>

```c
#define O_RDWR ZVFS_O_RDWR
```

相关声明：[O_RDWR](#abb0586253488ee61072b73557eeb873b)、[ZVFS_O_RDWR](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a82be0ad3089fdd844137845fa50d6e21)。

<a id="r_a11b644a8526139c4cc1850dac1271ced"></a>

```c
#define O_WRONLY ZVFS_O_WRONLY
```

相关声明：[O_WRONLY](#a11b644a8526139c4cc1850dac1271ced)、[ZVFS_O_WRONLY](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#abf07c70a006713aaed00a82ed87fb2be)。

<a id="r_ab93a8621587aba90181efd7d3aeea67e"></a>

```c
#define F_DUPFD ZVFS_F_DUPFD
```

相关声明：[F_DUPFD](#ab93a8621587aba90181efd7d3aeea67e)、[ZVFS_F_DUPFD](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#ac72b82ab9384b25f52acb061f96779b2)。

<a id="r_a025fad21a889c79f02ec53abe3526c32"></a>

```c
#define F_GETFL ZVFS_F_GETFL
```

相关声明：[F_GETFL](#a025fad21a889c79f02ec53abe3526c32)、[ZVFS_F_GETFL](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a02737faaf00631600b940982d1c9d0e5)。

<a id="r_af2939853c650561d3495ed40f68f6249"></a>

```c
#define F_SETFL ZVFS_F_SETFL
```

相关声明：[F_SETFL](#af2939853c650561d3495ed40f68f6249)、[ZVFS_F_SETFL](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a9f090c1504183cc5a023908dea28940b)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 112.2\_函数（Functions）

<a id="r_ac843f2e35e60c3bbf1da47d84306f29b"></a>

```c
int open (const char *name, int flags,...)
```

相关声明：[open](#ac843f2e35e60c3bbf1da47d84306f29b)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_acfc4bf677fc9f8be66d9624175cb3775"></a>

```c
int fcntl (int fildes, int cmd,...)
```

相关声明：[fcntl](#acfc4bf677fc9f8be66d9624175cb3775)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

## 112.3\_详细说明（Detailed Documentation）

<a id="ab93a8621587aba90181efd7d3aeea67e"></a>

### `F_DUPFD`

```c
#define F_DUPFD ZVFS_F_DUPFD
```

<a id="a025fad21a889c79f02ec53abe3526c32"></a>

### `F_GETFL`

```c
#define F_GETFL ZVFS_F_GETFL
```

<a id="af2939853c650561d3495ed40f68f6249"></a>

### `F_SETFL`

```c
#define F_SETFL ZVFS_F_SETFL
```

<a id="a4dc4d45e07d2abc899bcaf04b2846a87"></a>

### `O_ACCMODE`

```c
#define O_ACCMODE (ZVFS_O_RDONLY | ZVFS_O_RDWR | ZVFS_O_WRONLY)
```

<a id="ae036f789407d21f07b211552d67b3214"></a>

### `O_APPEND`

```c
#define O_APPEND ZVFS_O_APPEND
```

<a id="a1cf6b1de1fffedaa1d26b189e9a8d2cc"></a>

### `O_CREAT`

```c
#define O_CREAT ZVFS_O_CREAT
```

<a id="a9f5acfe79fafe14b6694447bd0e9f10b"></a>

### `O_EXCL`

```c
#define O_EXCL ZVFS_O_EXCL
```

<a id="a39d33ce33804efd4d52606d59071c6d8"></a>

### `O_NONBLOCK`

```c
#define O_NONBLOCK ZVFS_O_NONBLOCK
```

<a id="a7a68c9ffaac7dbcd652225dd7c06a54b"></a>

### `O_RDONLY`

```c
#define O_RDONLY ZVFS_O_RDONLY
```

<a id="abb0586253488ee61072b73557eeb873b"></a>

### `O_RDWR`

```c
#define O_RDWR ZVFS_O_RDWR
```

<a id="ad1d67e453fb3031f40f8cd3403773813"></a>

### `O_TRUNC`

```c
#define O_TRUNC ZVFS_O_TRUNC
```

<a id="a11b644a8526139c4cc1850dac1271ced"></a>

### `O_WRONLY`

```c
#define O_WRONLY ZVFS_O_WRONLY
```

<a id="acfc4bf677fc9f8be66d9624175cb3775"></a>

### `fcntl()`

```c
int fcntl ( int fildes, int cmd, ... )
```

<a id="ac843f2e35e60c3bbf1da47d84306f29b"></a>

### `open()`

```c
int open ( const char * name, int flags, ... )
```


## 112.4\_原页交叉引用（Cross References）

- [zephyr/sys/fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P255_fcntl.h_源码浏览.md)
- [ZVFS_O_APPEND](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#afa29fb3c7ff76f1e6cf2d69947865163)
- [ZVFS_O_CREAT](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aff3387bcd512c9bea99c94aa3c459214)
- [ZVFS_O_EXCL](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a2cb7a8f1c86ab67839458f0bc4198515)
- [ZVFS_O_NONBLOCK](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a122add73257644aab0689853c57c53f3)
- [ZVFS_O_TRUNC](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aecd7cfa3a9afdf22aac7b90911f4f459)
- [ZVFS_O_RDONLY](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a1aeb8126a4c817bdd2740a93f191de16)
- [ZVFS_O_RDWR](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a82be0ad3089fdd844137845fa50d6e21)
- [ZVFS_O_WRONLY](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#abf07c70a006713aaed00a82ed87fb2be)
- [ZVFS_F_DUPFD](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#ac72b82ab9384b25f52acb061f96779b2)
- [ZVFS_F_GETFL](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a02737faaf00631600b940982d1c9d0e5)
- [ZVFS_F_SETFL](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a9f090c1504183cc5a023908dea28940b)
- [flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P111_zephyr__arch__common__exc_handle.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P113_zephyr__posix__fnmatch.h_文件参考.md)
