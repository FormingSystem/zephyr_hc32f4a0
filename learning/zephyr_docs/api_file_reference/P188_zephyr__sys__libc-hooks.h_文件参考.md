---
id: learning.zephyr-docs.api-file-reference.page-188
title: zephyr__sys__libc-hooks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/libc-hooks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第188章\_zephyr\_\_sys\_\_libc-hooks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/libc-hooks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/toolchain.h>
#include <zephyr/app_memory/app_memdomain.h>
#include <stdio.h>
#include <stddef.h>
#include <zephyr/syscalls/libc-hooks.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 188.1\_函数（Functions）

<a id="r_ac5b3b7e59825b80ba65bb6346ee88e3c"></a>

```c
int zephyr_fputc (int c, FILE *stream)
```

相关声明：[zephyr_fputc](#ac5b3b7e59825b80ba65bb6346ee88e3c)、[FILE](P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#ac15bbd02a147d1595cdfb8b2979693d7)。

## 188.2\_详细说明（Detailed Documentation）

<a id="ac5b3b7e59825b80ba65bb6346ee88e3c"></a>

### `zephyr_fputc()`

```c
int zephyr_fputc ( int c, FILE * stream )
```


## 188.3\_原页交叉引用（Cross References）

- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [zephyr/app_memory/app_memdomain.h](../memory_domain_reference/P010_应用内存域头文件源码.md)
- [stdio.h](https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/libc-hooks_8h_source.html)
- [FILE](P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#ac15bbd02a147d1595cdfb8b2979693d7)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P187_____w__zephyr__zephyr__lib__libc__minimal__include__time.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P189_____w__zephyr__zephyr__lib__libc__minimal__include__limits.h_文件参考.md)
