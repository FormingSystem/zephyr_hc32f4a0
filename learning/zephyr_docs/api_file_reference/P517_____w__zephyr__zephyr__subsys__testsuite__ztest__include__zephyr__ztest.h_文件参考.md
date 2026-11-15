---
id: learning.zephyr-docs.api-file-reference.page-517
title: ____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztest.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ztest_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第517章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_testsuite\_\_ztest\_\_include\_\_zephyr\_\_ztest.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ztest_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Zephyr测试套件（Testsuite）。

<a id="details"></a>

```c
#include <zephyr/sys/printk.h>
#include <zephyr/kernel.h>
#include <zephyr/ztest_assert.h>
#include <zephyr/ztest_mock.h>
#include <zephyr/ztest_test.h>
#include <zephyr/tc_util.h>
#include <zephyr/benchmark.h>
```

查看此文件的源码。

Zephyr测试套件（Testsuite）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 517.1\_宏定义（Macros）

<a id="r_a8b43bafee90b30676faae508c21cb8d7"></a>

```c
#define PRINT printk
```

相关声明：[PRINT](#a8b43bafee90b30676faae508c21cb8d7)、[printk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a1bce54a738ce2d9dd6d95ee842ec237c)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 517.2\_函数（Functions）

<a id="r_a8a4533f287d99bb2d7c24c0e29c9a449"></a>

```c
void test_main (void)
```

相关声明：[test_main](#a8a4533f287d99bb2d7c24c0e29c9a449)。

## 517.3\_详细说明（Detailed Documentation）

<a id="a8b43bafee90b30676faae508c21cb8d7"></a>

### `PRINT`

```c
#define PRINT printk
```

<a id="a8a4533f287d99bb2d7c24c0e29c9a449"></a>

### `test_main()`

```c
void test_main ( void )
```


## 517.4\_原页交叉引用（Cross References）

- [zephyr/sys/printk.h](../api_source_runtime_reference/P051_printk.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/ztest_assert.h](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h_source.html)
- [zephyr/ztest_mock.h](../api_source_supplement_reference/P255_ztest_mock.h_源码浏览.md)
- [zephyr/ztest_test.h](https://docs.zephyrproject.org/latest/doxygen/html/ztest__test_8h_source.html)
- [zephyr/tc_util.h](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h_source.html)
- [zephyr/benchmark.h](../timing_reference/P012_基准测试头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P127_ztest.h_源码浏览.md)
- [printk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a1bce54a738ce2d9dd6d95ee842ec237c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P516_zephyr__dt-bindings__pinctrl__xmc4xxx-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P518_____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztest_error_hook.h_文件参考.md)
