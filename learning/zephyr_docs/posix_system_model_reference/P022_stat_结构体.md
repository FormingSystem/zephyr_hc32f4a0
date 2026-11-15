---
id: learning.zephyr-docs.posix-system-model-reference.page-22
title: stat_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structstat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_stat\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structstat.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/sys/stat.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_ac5b90090ae323741ae4c9e4f3683a29f"></a>

```c
dev_t st_dev
```

相关声明：[dev_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a0f89a9a6420c24efc5254e10170009e9)、[st_dev](#ac5b90090ae323741ae4c9e4f3683a29f)。

<a id="r_a9769ed8f0d4c5a9f329c32bc92479d56"></a>

```c
ino_t st_ino
```

相关声明：[ino_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a779f87527fcb00a46d12056b753cf22c)、[st_ino](#a9769ed8f0d4c5a9f329c32bc92479d56)。

<a id="r_a5cbdd829011af82ba61e83773bbcbc7d"></a>

```c
mode_t st_mode
```

相关声明：[mode_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#adb8322e115035a284aab704909e63d00)、[st_mode](#a5cbdd829011af82ba61e83773bbcbc7d)。

<a id="r_a0ed9092fa6c77a3251b9b9a4738ef84f"></a>

```c
nlink_t st_nlink
```

相关声明：[nlink_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a952c84a825bb4f319cf55c9afb99ee0e)、[st_nlink](#a0ed9092fa6c77a3251b9b9a4738ef84f)。

<a id="r_a4a8708a3d18be60ee7b2f06c4cab0c70"></a>

```c
uid_t st_uid
```

相关声明：[uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)、[st_uid](#a4a8708a3d18be60ee7b2f06c4cab0c70)。

<a id="r_ab864f16f436cec370f0ced585d897698"></a>

```c
gid_t st_gid
```

相关声明：[gid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3a7834be1a79bb0c5a65d3546c2e3bd8)、[st_gid](#ab864f16f436cec370f0ced585d897698)。

<a id="r_aa61e6c1a8a91c69f1d26f6700a0546cb"></a>

```c
dev_t st_rdev
```

相关声明：[dev_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a0f89a9a6420c24efc5254e10170009e9)、[st_rdev](#aa61e6c1a8a91c69f1d26f6700a0546cb)。

<a id="r_a040e19c8b9766f841fde8786ce9297bf"></a>

```c
off_t st_size
```

相关声明：[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[st_size](#a040e19c8b9766f841fde8786ce9297bf)。

<a id="r_a8447c545451bec2b95f9d67787404934"></a>

```c
struct timespec st_atim
```

相关声明：[timespec](../time_headers_reference/P005_timespec时间结构.md)、[st_atim](#a8447c545451bec2b95f9d67787404934)。

<a id="r_a78eca07da5a8a88b1c3dd8be5a32821e"></a>

```c
struct timespec st_mtim
```

相关声明：[timespec](../time_headers_reference/P005_timespec时间结构.md)、[st_mtim](#a78eca07da5a8a88b1c3dd8be5a32821e)。

<a id="r_a8fcf65727b775d92b773776ed1210c8b"></a>

```c
struct timespec st_ctim
```

相关声明：[timespec](../time_headers_reference/P005_timespec时间结构.md)、[st_ctim](#a8fcf65727b775d92b773776ed1210c8b)。

<a id="r_a38d474e1ae3cf6fbdde89ac3c3e308f1"></a>

```c
blksize_t st_blksize
```

相关声明：[blksize_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a50c0d048e63387089a42aaf054a6d05b)、[st_blksize](#a38d474e1ae3cf6fbdde89ac3c3e308f1)。

<a id="r_a42dd716b2f9234f961d949fc9500eefb"></a>

```c
blkcnt_t st_blocks
```

相关声明：[blkcnt_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#aa9a628992e7bcdc59d4fb606baada347)、[st_blocks](#a42dd716b2f9234f961d949fc9500eefb)。

<a id="r_a3715a60e75816e25a52d150e1893af76"></a>

```c
long st_spare4 [2]
```

相关声明：[st_spare4](#a3715a60e75816e25a52d150e1893af76)。

## 22.2\_详细说明（Detailed Documentation）

<a id="a8447c545451bec2b95f9d67787404934"></a>

### `st_atim`

```c
struct timespec stat::st_atim
```

<a id="a38d474e1ae3cf6fbdde89ac3c3e308f1"></a>

### `st_blksize`

```c
blksize_t stat::st_blksize
```

<a id="a42dd716b2f9234f961d949fc9500eefb"></a>

### `st_blocks`

```c
blkcnt_t stat::st_blocks
```

<a id="a8fcf65727b775d92b773776ed1210c8b"></a>

### `st_ctim`

```c
struct timespec stat::st_ctim
```

<a id="ac5b90090ae323741ae4c9e4f3683a29f"></a>

### `st_dev`

```c
dev_t stat::st_dev
```

<a id="ab864f16f436cec370f0ced585d897698"></a>

### `st_gid`

```c
gid_t stat::st_gid
```

<a id="a9769ed8f0d4c5a9f329c32bc92479d56"></a>

### `st_ino`

```c
ino_t stat::st_ino
```

<a id="a5cbdd829011af82ba61e83773bbcbc7d"></a>

### `st_mode`

```c
mode_t stat::st_mode
```

<a id="a78eca07da5a8a88b1c3dd8be5a32821e"></a>

### `st_mtim`

```c
struct timespec stat::st_mtim
```

<a id="a0ed9092fa6c77a3251b9b9a4738ef84f"></a>

### `st_nlink`

```c
nlink_t stat::st_nlink
```

<a id="aa61e6c1a8a91c69f1d26f6700a0546cb"></a>

### `st_rdev`

```c
dev_t stat::st_rdev
```

<a id="a040e19c8b9766f841fde8786ce9297bf"></a>

### `st_size`

```c
off_t stat::st_size
```

<a id="a3715a60e75816e25a52d150e1893af76"></a>

### `st_spare4`

```c
long stat::st_spare4[2]
```

<a id="a4a8708a3d18be60ee7b2f06c4cab0c70"></a>

### `st_uid`

```c
uid_t stat::st_uid
```

本数据类型文档由以下文件生成：

- `zephyr/posix/sys/stat.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/posix/sys/stat.h](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h_source.html)
- [dev_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a0f89a9a6420c24efc5254e10170009e9)
- [ino_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a779f87527fcb00a46d12056b753cf22c)
- [mode_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#adb8322e115035a284aab704909e63d00)
- [nlink_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a952c84a825bb4f319cf55c9afb99ee0e)
- [uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)
- [gid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3a7834be1a79bb0c5a65d3546c2e3bd8)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [blksize_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a50c0d048e63387089a42aaf054a6d05b)
- [blkcnt_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#aa9a628992e7bcdc59d4fb606baada347)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_stack_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_strbuf_结构体.md)
