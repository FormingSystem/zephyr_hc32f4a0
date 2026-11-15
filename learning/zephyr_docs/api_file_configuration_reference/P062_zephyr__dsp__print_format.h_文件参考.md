---
id: learning.zephyr-docs.api-file-configuration-reference.page-62
title: zephyr__dsp__print_format.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_zephyr\_\_dsp\_\_print\_format.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <inttypes.h>
#include <stdlib.h>
#include <zephyr/dsp/types.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 62.1\_宏定义（Macros）

<a id="r_ga08618ad8449ee21f0a57c151541e8ef8"></a>

```c
#define PRIq(precision)
```

相关声明：[PRIq](https://docs.zephyrproject.org/latest/doxygen/html/group__math__printing.html#ga08618ad8449ee21f0a57c151541e8ef8)。

插入 Q 值格式字符串（Q Value Format String）。

<a id="r_gad0393d2bb183784a9c09f2c05d7987f9"></a>

```c
#define PRIq_arg(q, precision, shift)
```

相关声明：[PRIq_arg](https://docs.zephyrproject.org/latest/doxygen/html/group__math__printing.html#gad0393d2bb183784a9c09f2c05d7987f9)。

将 Q 值参数（Q Value Arguments）插入打印格式（Print Format）。


## 62.2\_原页交叉引用（Cross References）

- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h_source.html)
- [stdlib.h](../api_source_configuration_reference/P107_stdlib.h_源码浏览.md)
- [zephyr/dsp/types.h](../api_source_reference/P364_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P670_print_format.h_源码浏览.md)
- [PRIq](https://docs.zephyrproject.org/latest/doxygen/html/group__math__printing.html#ga08618ad8449ee21f0a57c151541e8ef8)
- [PRIq_arg](https://docs.zephyrproject.org/latest/doxygen/html/group__math__printing.html#gad0393d2bb183784a9c09f2c05d7987f9)

---

[上一章](P061_zephyr__posix__sched.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md)
