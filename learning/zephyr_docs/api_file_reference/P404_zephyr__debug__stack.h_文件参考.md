---
id: learning.zephyr-docs.api-file-reference.page-404
title: zephyr__debug__stack.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stack_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第404章\_zephyr\_\_debug\_\_stack.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stack_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

栈使用量分析（Stack Usage Analysis）的辅助接口。

<a id="details"></a>

```c
#include <zephyr/logging/log.h>
#include <zephyr/kernel.h>
#include <zephyr/toolchain.h>
#include <stdbool.h>
```

查看此文件的源码。

栈使用量分析（Stack Usage Analysis）的辅助接口。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 404.1\_函数（Functions）

<a id="r_afeac222d2c3b1887fcc97221c6a3054d"></a>

```c
static void log_stack_usage (const struct k_thread *thread)
```

相关声明：[log_stack_usage](#afeac222d2c3b1887fcc97221c6a3054d)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

## 404.2\_详细说明（Detailed Documentation）

<a id="afeac222d2c3b1887fcc97221c6a3054d"></a>

### `log_stack_usage()`

```c
void log_stack_usage ( const struct k_thread * thread)
```

声明属性：`inline`、`static`。


## 404.3\_原页交叉引用（Cross References）

- [zephyr/logging/log.h](../log_core_reference/P004_日志公共头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P814_stack.h_源码浏览.md)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P403_zephyr__debug__sparse.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P405_zephyr__posix__sys__stat.h_文件参考.md)
