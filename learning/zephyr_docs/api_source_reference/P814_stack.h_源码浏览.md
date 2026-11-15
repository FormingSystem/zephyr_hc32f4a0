---
id: learning.zephyr-docs.api-source-reference.page-814
title: stack.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stack_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第814章\_stack.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stack_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stack_8h.html)。

## 814.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="foldopen00020"></a>
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
<a id="agroup__log__api_html_ga8193b0e10e5ee64b86848bb52be31869"></a>
<a id="agroup__log__api_html_ga9c338f3170acf38a8532d1181d26704e"></a>
<a id="agroup__thread__apis_html_gadebf45da56dee393164569742459dc0a"></a>
<a id="agroup__toolchain_html_ga1f08471f8dba6ce2a3e0f38bea73d7b5"></a>
<a id="agroup__toolchain_html_ga5365fdbb6323f48ddca9ab4149e9a561"></a>
<a id="agroup__toolchain_html_gae917ae1adad468956fa5d28a50d10670"></a>
<a id="akernel_2thread_8h_html_a6379f5a1f19ffbc262a6877c4f6e3647"></a>
<a id="akernel_8h_html"></a>
<a id="alog_8h_html"></a>
<a id="astack_8h_html_afeac222d2c3b1887fcc97221c6a3054d"></a>
<a id="astdbool_8h_html"></a>
<a id="astructk__thread_html"></a>
<a id="astructk__thread_html_a8be452e7b016fc901adad8518d7fe518"></a>
<a id="atoolchain_8h_html"></a>

```c


/*
 * Copyright (c) 2015 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DEBUG_STACK_H_
#define ZEPHYR_INCLUDE_DEBUG_STACK_H_

#include <zephyr/logging/log.h>
#include <zephyr/kernel.h>
#include <zephyr/toolchain.h>
#include <stdbool.h>

static inline void log_stack_usage(const struct k_thread *thread)
{
#if defined(CONFIG_INIT_STACKS) && defined(CONFIG_THREAD_STACK_INFO)
        size_t unused, size = thread->stack_info.size;

        TOOLCHAIN_DISABLE_WARNING(TOOLCHAIN_WARNING_SHADOW);
        LOG_MODULE_DECLARE(os, CONFIG_KERNEL_LOG_LEVEL);
        TOOLCHAIN_ENABLE_WARNING(TOOLCHAIN_WARNING_SHADOW);

        if (k_thread_stack_space_get(thread, &unused) == 0) {
                unsigned int pcnt = ((size - unused) * 100U) / size;
                const char *tname;

                tname = k_thread_name_get((k_tid_t)thread);
                if (tname == NULL) {
                        tname = "unknown";
                }

                LOG_INF("%p (%s):\tunused %zu\tusage %zu / %zu (%u %%)",
                        thread, tname, unused, size - unused, size,
                        pcnt);
        }
#else
        ARG_UNUSED(thread);
#endif
}
#endif /* ZEPHYR_INCLUDE_DEBUG_STACK_H_ */
```

## 814.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2015 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 46 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DEBUG_STACK_H_`。

## 814.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stack_8h.html)
- [zephyr/logging/log.h](../log_core_reference/P003_日志公共头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [log_stack_usage](https://docs.zephyrproject.org/latest/doxygen/html/stack_8h.html#afeac222d2c3b1887fcc97221c6a3054d)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [stack_info](../thread_core_reference/P004_线程对象结构.md#a8be452e7b016fc901adad8518d7fe518)
- [TOOLCHAIN_DISABLE_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga1f08471f8dba6ce2a3e0f38bea73d7b5)
- [TOOLCHAIN_WARNING_SHADOW](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gae917ae1adad468956fa5d28a50d10670)
- [LOG_MODULE_DECLARE](../log_core_reference/P002_日志公共接口.md#ga8193b0e10e5ee64b86848bb52be31869)
- [TOOLCHAIN_ENABLE_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga5365fdbb6323f48ddca9ab4149e9a561)
- [k_thread_name_get](../thread_core_reference/P001_线程公共接口.md#gadebf45da56dee393164569742459dc0a)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)
- [LOG_INF](../log_core_reference/P002_日志公共接口.md#ga9c338f3170acf38a8532d1181d26704e)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [log.h](../log_core_reference/P003_日志公共头文件参考.md)
- [k_thread::stack_info](../thread_core_reference/P004_线程对象结构.md#a8be452e7b016fc901adad8518d7fe518)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P813_st87mxx_app_services.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P815_stat_mgmt.h_源码浏览.md)
