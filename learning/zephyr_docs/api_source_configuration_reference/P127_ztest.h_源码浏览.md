---
id: learning.zephyr-docs.api-source-configuration-reference.page-127
title: ztest.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ztest_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第127章\_ztest.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ztest_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ztest_8h.html)。

## 127.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
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
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="abenchmark_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="aprintk_8h_html"></a>
<a id="atc__util_8h_html"></a>
<a id="aztest_8h_html_a8a4533f287d99bb2d7c24c0e29c9a449"></a>
<a id="aztest__assert_8h_html"></a>
<a id="aztest__mock_8h_html"></a>
<a id="aztest__test_8h_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_TESTSUITE_INCLUDE_ZTEST_H_
#define ZEPHYR_TESTSUITE_INCLUDE_ZTEST_H_


#if !defined(CONFIG_ZTEST) && !defined(ZTEST_UNITTEST)
#error "You need to add CONFIG_ZTEST to your config file."
#endif

#ifdef ZTEST_UNITTEST
#define ARCH_STACK_PTR_ALIGN 8
/* FIXME: Properly integrate with Zephyr's arch specific code */
#ifdef __cplusplus
extern "C" {
#endif
struct arch_esf;
#ifdef __cplusplus
}
#endif
#endif /* ZTEST_UNITTEST */

#include <zephyr/sys/printk.h>
#define PRINT printk

#include <zephyr/kernel.h>

#include <zephyr/ztest_assert.h>
#include <zephyr/ztest_mock.h>
#include <zephyr/ztest_test.h>
#include <zephyr/tc_util.h>

#include <zephyr/benchmark.h>

#ifdef __cplusplus
extern "C" {
#endif

void test_main(void);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_TESTSUITE_INCLUDE_ZTEST_H_ */
```

## 127.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

待修复（FIXME）：与 Zephyr 的架构专用代码正确集成。

### 注释 3：原第 35 行

条件编译标记：`ZTEST_UNITTEST`。

### 注释 4：原第 59 行

头文件保护宏（Header guard）标记：`ZEPHYR_TESTSUITE_INCLUDE_ZTEST_H_`。

## 127.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ztest_8h.html)
- [zephyr/sys/printk.h](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/ztest_assert.h](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h.html)
- [zephyr/ztest_mock.h](https://docs.zephyrproject.org/latest/doxygen/html/ztest__mock_8h.html)
- [zephyr/ztest_test.h](https://docs.zephyrproject.org/latest/doxygen/html/ztest__test_8h.html)
- [zephyr/tc_util.h](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html)
- [zephyr/benchmark.h](../timing_reference/P011_基准测试头文件参考.md)
- [test_main](https://docs.zephyrproject.org/latest/doxygen/html/ztest_8h.html#a8a4533f287d99bb2d7c24c0e29c9a449)
- [benchmark.h](../timing_reference/P011_基准测试头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [printk.h](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)
- [tc_util.h](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html)
- [ztest_assert.h](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h.html)
- [ztest_mock.h](https://docs.zephyrproject.org/latest/doxygen/html/ztest__mock_8h.html)
- [ztest_test.h](https://docs.zephyrproject.org/latest/doxygen/html/ztest__test_8h.html)

---

[上一章](P126_xmc4xxx-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P128_ztest_error_hook.h_源码浏览.md)
