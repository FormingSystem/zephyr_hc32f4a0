---
id: learning.zephyr-docs.api-file-supplement-reference.page-46
title: zephyr__net__openthread.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2openthread_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_zephyr\_\_net\_\_openthread.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2openthread_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

OpenThread协议栈（Stack）的公共头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/net/net_if.h>
#include <zephyr/kernel/thread.h>
#include <openthread.h>
```

查看此文件的源码。

OpenThread协议栈（Stack）的公共头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 46.1\_函数（Functions）

<a id="r_gad975528c91de66cd1054f3584bfcc957"></a>

```c
struct openthread_context * openthread_get_default_context (void)
```

相关声明：[openthread_get_default_context](https://docs.zephyrproject.org/latest/doxygen/html/group__openthread.html#gad975528c91de66cd1054f3584bfcc957)。

获取指向默认 OpenThread 上下文（Context）的指针（Pointer）。


## 46.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [zephyr/kernel/thread.h](../thread_core_reference/P003_线程头文件源码.md)
- [openthread.h](../api_source_reference/P365_openthread.h_源码浏览.md)
- [openthread_get_default_context](https://docs.zephyrproject.org/latest/doxygen/html/group__openthread.html#gad975528c91de66cd1054f3584bfcc957)

<a id="header-details"></a>

---

[上一章](P045_zephyr__arch__tricore__error.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P047_zephyr__input__input_analog_axis_settings.h_文件参考.md)
