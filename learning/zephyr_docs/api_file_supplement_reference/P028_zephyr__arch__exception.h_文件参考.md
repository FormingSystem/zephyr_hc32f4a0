---
id: learning.zephyr-docs.api-file-supplement-reference.page-28
title: zephyr__arch__exception.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/exception_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_arch\_\_exception.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/exception_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdarg.h>
#include <zephyr/toolchain.h>
#include <zephyr/sys/printk.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 28.1\_宏定义（Macros）

<a id="r_a39da57c6e073d8a2ea07b49b0c51aa3e"></a>

```c
#define EXCEPTION_DUMP(format, ...)
```

相关声明：[EXCEPTION_DUMP](#a39da57c6e073d8a2ea07b49b0c51aa3e)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.2\_函数（Functions）

<a id="r_a9998b45688b94011e21d501addff40bc"></a>

```c
static void arch_exception_dump_arg_check (const char *fmt,...)
```

相关声明：[arch_exception_dump_arg_check](#a9998b45688b94011e21d501addff40bc)。

用于触发异常转储参数类型检查（Exception Dump Argument Type Checking）的虚拟函数（Dummy Function）。

## 28.3\_详细说明（Detailed Documentation）

<a id="a39da57c6e073d8a2ea07b49b0c51aa3e"></a>

### `EXCEPTION_DUMP`

```c
#define EXCEPTION_DUMP ( format, ... )
```

展开值（Value）：

```c
do {                                                                                       \
        if (0) {                                                                           \
                arch_exception_dump_arg_check(format, ##__VA_ARGS__);                      \
        }                                                                                  \
} while (false)
```

<a id="a9998b45688b94011e21d501addff40bc"></a>

### `arch_exception_dump_arg_check()`

```c
void arch_exception_dump_arg_check ( const char * fmt, ... )
```

声明属性：`inline`、`static`。

用于触发异常转储参数类型检查（Exception Dump Argument Type Checking）的虚拟函数（Dummy Function）。


## 28.4\_原页交叉引用（Cross References）

- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [zephyr/sys/printk.h](../api_source_runtime_reference/P051_printk.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P069_exception.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P027_zephyr__dt-bindings__interrupt-controller__esp-esp32p4-intmux.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__drivers__sensor__explorir_m.h_文件参考.md)
