---
id: learning.zephyr-docs.api-source-configuration-reference.page-128
title: ztest_error_hook.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ztest__error__hook_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第128章\_ztest\_error\_hook.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ztest__error__hook_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ztest__error__hook_8h.html)。

## 128.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
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
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="akernel_8h_html"></a>

```c
/*
 * Copyright (c) 2020 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ZTEST_FATAL_HOOK_H_
#define ZEPHYR_INCLUDE_ZTEST_FATAL_HOOK_H_

#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_ZTEST_FATAL_HOOK)
__syscall void ztest_set_fault_valid(bool valid);

/* @brief A hook after fatal error handler
 *
 * @details This is a test case hook that can run code from test case, in
 * order to deal with some special case when catching the expected fatal
 * error.
 *
 * Usage: Define your own hook function in your test case code, and do what
 * you want to do after fatal error handler.
 *
 * By default, it will do nothing before leaving error handler.
 */
void ztest_post_fatal_error_hook(unsigned int reason,
                const struct arch_esf *pEsf);

#endif


#if defined(CONFIG_ZTEST_ASSERT_HOOK)
__syscall void ztest_set_assert_valid(bool valid);

/* @brief A hook after assert fault handler
 *
 * @details This is a test case hook that can run code from test case, in
 * order to deal with some special case when catching the expected assert
 * failed.
 *
 * Usage: Define your own hook function in your test case code, and do what
 * you want to do after assert handler.
 *
 * By default, it will abort the thread which assert failed.
 */
void ztest_post_assert_fail_hook(void);

#endif

#ifdef __cplusplus
}
#endif

#if defined(CONFIG_ZTEST_FATAL_HOOK) || defined(CONFIG_ZTEST_ASSERT_HOOK)
#include <zephyr/syscalls/ztest_error_hook.h>
#endif

#endif /* ZEPHYR_INCLUDE_ZTEST_FATAL_HOOK_H_ */
```

## 128.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 29 行

功能（Brief）：致命错误处理程序之后的钩子（Hook）。

详细说明（Details）：这是一个测试用例钩子，可运行测试用例中的代码，以便在捕获预期的致命错误时处理某些特殊情况。

用法（Usage）：在测试用例代码中定义自己的钩子函数，执行希望在致命错误处理程序之后进行的操作。

默认情况下，在退出错误处理程序之前不执行任何操作。

### 注释 3：原第 59 行

功能（Brief）：断言故障处理程序之后的钩子（Hook）。

详细说明（Details）：这是一个测试用例钩子，可运行测试用例中的代码，以便在捕获预期的断言失败时处理某些特殊情况。

用法（Usage）：在测试用例代码中定义自己的钩子函数，执行希望在断言处理程序之后进行的操作。

默认情况下，它会中止发生断言失败的线程。

### 注释 4：原第 82 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ZTEST_FATAL_HOOK_H_`。

## 128.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ztest__error__hook_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P127_ztest.h_源码浏览.md) · [返回大纲](大纲.md)
