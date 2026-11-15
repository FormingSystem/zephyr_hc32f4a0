---
id: learning.zephyr-docs.api-connection-topic-reference.page-22
title: 按字粒度访问内存 API（Word Granular Access Memory APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_按字粒度访问内存 API（Word Granular Access Memory APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.1\_函数（Functions）

<a id="r_gad4ed45c6f5a03556730b10945625879b"></a>

```c
void * sys_memset_word_granular_access (void *buf, int c, size_t n)
```

相关声明：[sys_memset_word_granular_access](#gad4ed45c6f5a03556730b10945625879b)。

在以字为访问粒度的内存（Word Granular Access Memory）中，对缓冲区执行内存填充（Memset）。

<a id="r_ga9834656071d5aa892b4de9b3d47183c8"></a>

```c
void * sys_memcpy_to_word_granular_access (void *d, const void *s, size_t n)
```

相关声明：[sys_memcpy_to_word_granular_access](#ga9834656071d5aa892b4de9b3d47183c8)。

将缓冲区内容复制（Memcpy）到以字为访问粒度的内存（Word Granular Access Memory）。

<a id="r_ga65d008216186bbcfa2bc39493bf42325"></a>

```c
void * sys_memcpy_from_word_granular_access (void *d, const void *s, size_t n)
```

相关声明：[sys_memcpy_from_word_granular_access](#ga65d008216186bbcfa2bc39493bf42325)。

从以字为访问粒度的内存（Word Granular Access Memory）复制（Memcpy）缓冲区内容。

## 22.2\_详细说明（Detailed Documentation）

<a id="ga65d008216186bbcfa2bc39493bf42325"></a>

### `sys_memcpy_from_word_granular_access()`

```c
void * sys_memcpy_from_word_granular_access ( void * d, const void * s, size_t n )
```

```c
#include <zephyr/sys/word_granular_access.h>
```

从以字为访问粒度的内存（Word Granular Access Memory）复制（Memcpy）缓冲区内容。

用于从按字粒度访问的内存（word-granular-access memory）复制缓冲区的 `memcpy`。

注意：如果正在写入或读取的缓冲区起始位置未按字对齐（word-aligned），或长度不是字大小的整数倍，可能需要读取或写入请求范围之外的字节。这些字节中的数据保持不变。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `d` | 目标缓冲区。 |
| `s` | 源缓冲区。 |
| `n` | 要复制的字节数。 |

**返回（Returns）**：返回值：所提供的目标缓冲区指针；出错时返回 `NULL`。

<a id="ga9834656071d5aa892b4de9b3d47183c8"></a>

### `sys_memcpy_to_word_granular_access()`

```c
void * sys_memcpy_to_word_granular_access ( void * d, const void * s, size_t n )
```

```c
#include <zephyr/sys/word_granular_access.h>
```

将缓冲区内容复制（Memcpy）到以字为访问粒度的内存（Word Granular Access Memory）。

用于将缓冲区复制到按字粒度访问的内存（word-granular-access memory）的 `memcpy`。

注意：如果正在写入或读取的缓冲区起始位置未按字对齐（word-aligned），或长度不是字大小的整数倍，可能需要读取或写入请求范围之外的字节。这些字节中的数据保持不变。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `d` | 目标缓冲区。 |
| `s` | 源缓冲区。 |
| `n` | 要复制的字节数。 |

**返回（Returns）**：返回值：所提供的目标缓冲区指针；出错时返回 `NULL`。

<a id="gad4ed45c6f5a03556730b10945625879b"></a>

### `sys_memset_word_granular_access()`

```c
void * sys_memset_word_granular_access ( void * buf, int c, size_t n )
```

```c
#include <zephyr/sys/word_granular_access.h>
```

在以字为访问粒度的内存（Word Granular Access Memory）中，对缓冲区执行内存填充（Memset）。

在以字为访问粒度的内存（Word Granular Access Memory）中，对缓冲区执行内存填充（Memset）。

注意：如果正在写入的缓冲区起始位置未按字对齐（word-aligned），或长度不是字大小的整数倍，可能需要写入请求范围之外的字节。这些字节中的数据保持不变。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要执行 `memset` 的缓冲区。 |
| `c` | 要设置的值。 |
| `n` | 要设置的字节数。 |

**返回（Returns）**：返回值：所提供的缓冲区指针；出错时返回 `NULL`。


## 22.3\_原页交叉引用（Cross References）

- [zephyr/sys/word_granular_access.h](../api_file_runtime_reference/P075_zephyr__sys__word_granular_access.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P021_TMP114 API主题.md) · [返回大纲](大纲.md) · [下一章](P023_WUC 驱动后端 API.md)
