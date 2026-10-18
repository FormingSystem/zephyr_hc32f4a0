---
id: learning.zephyr-docs.api-file-storage-event-reference.page-25
title: zephyr__sys__zassert.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zassert_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_sys\_\_zassert.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/zassert_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Zephyr断言框架（Assertion Framework）。

<a id="details"></a>

```c
#include <stdarg.h>
#include <stddef.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

Zephyr 断言框架（Assertion Framework）。此框架提供在运行时检查条件、以结构化方式报告失败的机制。它支持按模块设置断言级别（Assertion Levels），允许开发者逐模块控制断言输出详细程度和行为；也支持自定义断言失败处理，允许覆盖默认行为，实现自己的报告及恢复／崩溃机制（Recovery/Crash Mechanism）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 25.1\_宏定义（Macros）

<a id="r_gad1a1263184000f91a1f17655cd5074ee"></a>

```c
#define ZASSERT_LEVEL_OFF 0
```

相关声明：[ZASSERT_LEVEL_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gad1a1263184000f91a1f17655cd5074ee)。

禁用断言（Assertions），并在编译时移除。

<a id="r_ga9c86df1bad747a60474e5bb799218071"></a>

```c
#define ZASSERT_LEVEL_TERSE 1
```

相关声明：[ZASSERT_LEVEL_TERSE](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#ga9c86df1bad747a60474e5bb799218071)。

检查断言（Assertions），不报告附加信息。

<a id="r_gab91fabc5db83d859e36bd6b313ec427b"></a>

```c
#define ZASSERT_LEVEL_NORMAL 2
```

相关声明：[ZASSERT_LEVEL_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gab91fabc5db83d859e36bd6b313ec427b)。

检查断言（Assertions），仅报告失败位置（Failing Location）。

<a id="r_gaed3f8dc1cf2160c1f8a04f3e74f5a136"></a>

```c
#define ZASSERT_LEVEL_VERBOSE 3
```

相关声明：[ZASSERT_LEVEL_VERBOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gaed3f8dc1cf2160c1f8a04f3e74f5a136)。

检查断言（Assertions），报告条件、位置和消息（Condition、Location、Message）。

<a id="r_gacb3b895fe52481a4165e79a3c51438c0"></a>

```c
#define ZASSERT_TERSE(_test, ...)
```

相关声明：[ZASSERT_TERSE](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gacb3b895fe52481a4165e79a3c51438c0)。

仅报告固定提示文字（Fixed Banner）、不含位置或消息的断言（Assertion）。

<a id="r_gabb28809d1f97cc6d9d4434a2cd91b760"></a>

```c
#define ZASSERT_NORMAL(_test, ...)
```

相关声明：[ZASSERT_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gabb28809d1f97cc6d9d4434a2cd91b760)。

仅报告失败位置（Failing Location）的断言（Assertion）。

<a id="r_ga32f08bc980eb63596e963d66c246d0bd"></a>

```c
#define ZASSERT_VERBOSE(_test, ...)
```

相关声明：[ZASSERT_VERBOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#ga32f08bc980eb63596e963d66c246d0bd)。

报告条件、位置和可选消息（Optional Message）的断言（Assertion）。

<a id="r_gaf33d60719a2317efdd756a2df385343e"></a>

```c
#define ZASSERT_MODULE(...)
```

相关声明：[ZASSERT_MODULE](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gaf33d60719a2317efdd756a2df385343e)。

选择本文件中 `ZASSERT()` 所用的、由 Kconfig 定义的断言模块（Assertion Module）。

<a id="r_gacb48ee150ebe9d7b2a415ec8bee79cb7"></a>

```c
#define ZASSERT(_test, ...)
```

相关声明：[ZASSERT](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gacb48ee150ebe9d7b2a415ec8bee79cb7)。

感知模块的断言（Module-aware Assertion）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.2\_函数（Functions）

<a id="r_ga72d07b4b0fb4190dc675813c0d9215b1"></a>

```c
FUNC_NORETURN void zassert_fail (const char *cond, const char *file, unsigned int line, const char *fmt,...)
```

相关声明：[zassert_fail](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#ga72d07b4b0fb4190dc675813c0d9215b1)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

报告断言失败（Assertion Failure），并采取终止动作（Terminal Action）。

<a id="r_ga98d7d44bfde093e6abe6cf51566c77d5"></a>

```c
FUNC_NORETURN void zassert_post_action (const char *file, unsigned int line)
```

相关声明：[zassert_post_action](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#ga98d7d44bfde093e6abe6cf51566c77d5)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

断言失败时采取的终止动作（Terminal Action）。

<a id="r_gadf431a5e2a87111d50cd268d309f3eea"></a>

```c
void zassert_vprint (const char *fmt, va_list ap)
```

相关声明：[zassert_vprint](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gadf431a5e2a87111d50cd268d309f3eea)。

输出断言文本（Assertion Text），使用 `va_list` 形式。

<a id="r_gaf1c13156eb4331a95f2e396afb7736ba"></a>

```c
static void zassert_print (const char *fmt,...)
```

相关声明：[zassert_print](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gaf1c13156eb4331a95f2e396afb7736ba)。

以类似 `printf` 的形式输出断言文本（Assertion Text），经 `zassert_vprint()` 路由。


## 25.3\_原页交叉引用（Cross References）

- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_architecture_reference/P024_zassert.h_源码浏览.md)
- [ZASSERT_LEVEL_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gad1a1263184000f91a1f17655cd5074ee)
- [ZASSERT_LEVEL_TERSE](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#ga9c86df1bad747a60474e5bb799218071)
- [ZASSERT_LEVEL_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gab91fabc5db83d859e36bd6b313ec427b)
- [ZASSERT_LEVEL_VERBOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gaed3f8dc1cf2160c1f8a04f3e74f5a136)
- [ZASSERT_TERSE](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gacb3b895fe52481a4165e79a3c51438c0)
- [ZASSERT_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gabb28809d1f97cc6d9d4434a2cd91b760)
- [ZASSERT_VERBOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#ga32f08bc980eb63596e963d66c246d0bd)
- [ZASSERT_MODULE](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gaf33d60719a2317efdd756a2df385343e)
- [ZASSERT()](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gacb48ee150ebe9d7b2a415ec8bee79cb7)
- [zassert_fail](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#ga72d07b4b0fb4190dc675813c0d9215b1)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [zassert_post_action](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#ga98d7d44bfde093e6abe6cf51566c77d5)
- [zassert_vprint](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gadf431a5e2a87111d50cd268d309f3eea)
- [zassert_print](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html#gaf1c13156eb4331a95f2e396afb7736ba)

<a id="header-details"></a>

---

[上一章](P024_zephyr__net__websocket.h_文件参考.md) · [返回大纲](大纲.md)
