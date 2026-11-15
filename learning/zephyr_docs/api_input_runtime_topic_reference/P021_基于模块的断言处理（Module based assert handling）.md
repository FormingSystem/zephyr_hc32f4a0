---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-21
title: 基于模块的断言处理（Module based assert handling）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_基于模块的断言处理（Module based assert handling）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__zassert.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.1\_宏定义（Macros）

<a id="r_gad1a1263184000f91a1f17655cd5074ee"></a>

```c
#define ZASSERT_LEVEL_OFF 0
```

相关声明：[ZASSERT_LEVEL_OFF](#gad1a1263184000f91a1f17655cd5074ee)。

禁用断言（Assertions），并在编译时移除。

<a id="r_ga9c86df1bad747a60474e5bb799218071"></a>

```c
#define ZASSERT_LEVEL_TERSE 1
```

相关声明：[ZASSERT_LEVEL_TERSE](#ga9c86df1bad747a60474e5bb799218071)。

检查断言（Assertions），不报告附加信息。

<a id="r_gab91fabc5db83d859e36bd6b313ec427b"></a>

```c
#define ZASSERT_LEVEL_NORMAL 2
```

相关声明：[ZASSERT_LEVEL_NORMAL](#gab91fabc5db83d859e36bd6b313ec427b)。

检查断言（Assertions），仅报告失败位置（Failing Location）。

<a id="r_gaed3f8dc1cf2160c1f8a04f3e74f5a136"></a>

```c
#define ZASSERT_LEVEL_VERBOSE 3
```

相关声明：[ZASSERT_LEVEL_VERBOSE](#gaed3f8dc1cf2160c1f8a04f3e74f5a136)。

检查断言（Assertions），报告条件、位置和消息（Condition、Location、Message）。

<a id="r_gacb3b895fe52481a4165e79a3c51438c0"></a>

```c
#define ZASSERT_TERSE(_test, ...)
```

相关声明：[ZASSERT_TERSE](#gacb3b895fe52481a4165e79a3c51438c0)。

仅报告固定提示文字（Fixed Banner）、不含位置或消息的断言（Assertion）。

<a id="r_gabb28809d1f97cc6d9d4434a2cd91b760"></a>

```c
#define ZASSERT_NORMAL(_test, ...)
```

相关声明：[ZASSERT_NORMAL](#gabb28809d1f97cc6d9d4434a2cd91b760)。

仅报告失败位置（Failing Location）的断言（Assertion）。

<a id="r_ga32f08bc980eb63596e963d66c246d0bd"></a>

```c
#define ZASSERT_VERBOSE(_test, ...)
```

相关声明：[ZASSERT_VERBOSE](#ga32f08bc980eb63596e963d66c246d0bd)。

报告条件、位置和可选消息（Optional Message）的断言（Assertion）。

<a id="r_gaf33d60719a2317efdd756a2df385343e"></a>

```c
#define ZASSERT_MODULE(...)
```

相关声明：[ZASSERT_MODULE](#gaf33d60719a2317efdd756a2df385343e)。

选择本文件中 `ZASSERT()` 所用的、由 Kconfig 定义的断言模块（Assertion Module）。

<a id="r_gacb48ee150ebe9d7b2a415ec8bee79cb7"></a>

```c
#define ZASSERT(_test, ...)
```

相关声明：[ZASSERT](#gacb48ee150ebe9d7b2a415ec8bee79cb7)。

感知模块的断言（Module-aware Assertion）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.2\_函数（Functions）

<a id="r_ga72d07b4b0fb4190dc675813c0d9215b1"></a>

```c
FUNC_NORETURN void zassert_fail (const char *cond, const char *file, unsigned int line, const char *fmt,...)
```

相关声明：[zassert_fail](#ga72d07b4b0fb4190dc675813c0d9215b1)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

报告断言失败（Assertion Failure），并采取终止动作（Terminal Action）。

<a id="r_ga98d7d44bfde093e6abe6cf51566c77d5"></a>

```c
FUNC_NORETURN void zassert_post_action (const char *file, unsigned int line)
```

相关声明：[zassert_post_action](#ga98d7d44bfde093e6abe6cf51566c77d5)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

断言失败时采取的终止动作（Terminal Action）。

<a id="r_gadf431a5e2a87111d50cd268d309f3eea"></a>

```c
void zassert_vprint (const char *fmt, va_list ap)
```

相关声明：[zassert_vprint](#gadf431a5e2a87111d50cd268d309f3eea)。

输出断言文本（Assertion Text），使用 `va_list` 形式。

<a id="r_gaf1c13156eb4331a95f2e396afb7736ba"></a>

```c
static void zassert_print (const char *fmt,...)
```

相关声明：[zassert_print](#gaf1c13156eb4331a95f2e396afb7736ba)。

以类似 `printf` 的形式输出断言文本（Assertion Text），经 `zassert_vprint()` 路由。

## 21.3\_详细说明（Detailed Documentation）

<a id="gacb48ee150ebe9d7b2a415ec8bee79cb7"></a>

### `ZASSERT`

```c
#define ZASSERT ( _test, ... )
```

```c
#include <zephyr/sys/zassert.h>
```

展开值（Value）：

```c
ZASSERT_IMPL(zassert_impl_level, _test, ##__VA_ARGS__)
```

感知模块的断言（Module-aware Assertion）。

是否启用及输出多少内容，由本文件 `ZASSERT_MODULE()` 的级别控制。`ZASSERT_LEVEL_TERSE` 只报告固定的 `ASSERTION FAIL` 提示；`ZASSERT_LEVEL_NORMAL` 增加失败位置；`ZASSERT_LEVEL_VERBOSE` 还会将字符串化条件（Stringified Condition）、可选消息及其参数编译进程序并打印。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_test` | 要检查的条件（Condition）。若为假，触发致命错误（Fatal Error）。 |
| `...` | 可选消息格式字符串（Message Format String），后跟其参数。检查含义明确时可以省略。 |

<a id="gab91fabc5db83d859e36bd6b313ec427b"></a>

### `ZASSERT_LEVEL_NORMAL`

```c
#define ZASSERT_LEVEL_NORMAL 2
```

```c
#include <zephyr/sys/zassert.h>
```

检查断言（Assertions），仅报告失败位置（Failing Location）。

<a id="gad1a1263184000f91a1f17655cd5074ee"></a>

### `ZASSERT_LEVEL_OFF`

```c
#define ZASSERT_LEVEL_OFF 0
```

```c
#include <zephyr/sys/zassert.h>
```

禁用断言（Assertions），并在编译时移除。

<a id="ga9c86df1bad747a60474e5bb799218071"></a>

### `ZASSERT_LEVEL_TERSE`

```c
#define ZASSERT_LEVEL_TERSE 1
```

```c
#include <zephyr/sys/zassert.h>
```

检查断言（Assertions），不报告附加信息。

<a id="gaed3f8dc1cf2160c1f8a04f3e74f5a136"></a>

### `ZASSERT_LEVEL_VERBOSE`

```c
#define ZASSERT_LEVEL_VERBOSE 3
```

```c
#include <zephyr/sys/zassert.h>
```

检查断言（Assertions），报告条件、位置和消息（Condition、Location、Message）。

<a id="gaf33d60719a2317efdd756a2df385343e"></a>

### `ZASSERT_MODULE`

```c
#define ZASSERT_MODULE ( ...)
```

```c
#include <zephyr/sys/zassert.h>
```

展开值（Value）：

```c
ZASSERT_IMPL_MODULE(__VA_ARGS__)
```

选择本文件中 `ZASSERT()` 所用的、由 Kconfig 定义的断言模块（Assertion Module）。

必须放在文件作用域（File Scope），并位于该翻译单元（Translation Unit）中任何 `ZASSERT()` 用法之前。每个使用 `ZASSERT()` 的文件都必须选择模块。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `...` | 断言模块名称（Assertion Module Name），为大写标识符，后面可跟显式级别。模块默认级别来自 Kconfig 符号 `CONFIG_ASSERT_MODULE_<module>_LEVEL`，该符号必须存在；名称按原样拼接，因此必须匹配。可选第二个参数 `ZASSERT_LEVEL_OFF`、`ZASSERT_LEVEL_TERSE`、`ZASSERT_LEVEL_NORMAL` 或 `ZASSERT_LEVEL_VERBOSE` 可覆盖本文件中的模块默认值。 |

**说明（Note）**：**注意（Note）：**`CONFIG_ASSERT` 是总开关。禁用时，所有模块都强制为 `ZASSERT_LEVEL_OFF`，不受模块默认值或显式级别影响。

<a id="gabb28809d1f97cc6d9d4434a2cd91b760"></a>

### `ZASSERT_NORMAL`

```c
#define ZASSERT_NORMAL ( _test, ... )
```

```c
#include <zephyr/sys/zassert.h>
```

展开值（Value）：

```c
ZASSERT_IMPL_LEVEL(ZASSERT_LEVEL_NORMAL, (_test), ##__VA_ARGS__)
```

仅报告失败位置（Failing Location）的断言（Assertion）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_test` | 要检查的条件（Condition）。若为假，触发致命错误（Fatal Error）。 |
| `...` | 被忽略的可选消息格式字符串（Message Format String）及参数。 |

<a id="gacb3b895fe52481a4165e79a3c51438c0"></a>

### `ZASSERT_TERSE`

```c
#define ZASSERT_TERSE ( _test, ... )
```

```c
#include <zephyr/sys/zassert.h>
```

展开值（Value）：

```c
ZASSERT_IMPL_LEVEL(ZASSERT_LEVEL_TERSE, (_test), ##__VA_ARGS__)
```

仅报告固定提示文字（Fixed Banner）、不含位置或消息的断言（Assertion）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_test` | 要检查的条件（Condition）。若为假，触发致命错误（Fatal Error）。 |
| `...` | 被忽略的可选消息格式字符串（Message Format String）及参数。 |

<a id="ga32f08bc980eb63596e963d66c246d0bd"></a>

### `ZASSERT_VERBOSE`

```c
#define ZASSERT_VERBOSE ( _test, ... )
```

```c
#include <zephyr/sys/zassert.h>
```

展开值（Value）：

```c
ZASSERT_IMPL_LEVEL(ZASSERT_LEVEL_VERBOSE, (_test), ##__VA_ARGS__)
```

报告条件、位置和可选消息（Optional Message）的断言（Assertion）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_test` | 要检查的条件（Condition）。若为假，触发致命错误（Fatal Error）。 |
| `...` | 可选消息格式字符串（Message Format String），后跟其参数。 |

<a id="ga72d07b4b0fb4190dc675813c0d9215b1"></a>

### `zassert_fail()`

```c
FUNC_NORETURN void zassert_fail ( const char * cond, const char * file, unsigned int line, const char * fmt, ... )
```

```c
#include <zephyr/sys/zassert.h>
```

报告断言失败（Assertion Failure），并采取终止动作（Terminal Action）。

弱符号（Weak），可覆盖（Overridable）。

将完整断言冷路径（Assertion Cold Path）集中为一次非内联调用（Out-of-line Call）。默认实现打印位置；`fmt` 非 `NULL` 时还打印用户消息，然后调用 `zassert_post_action()`。覆盖此接口即可在单一入口捕获或重定向完整断言输出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cond` | 字符串化的失败条件（Stringified Failing Condition）。 |
| `file` | 断言失败所在的源文件（Source File）。 |
| `line` | 断言失败所在的源码行（Source Line）。 |
| `fmt` | 可选用户消息格式字符串（User Message Format String），没有消息时为 `NULL`。 |
| `...` | `fmt` 的参数（Arguments）。 |

<a id="ga98d7d44bfde093e6abe6cf51566c77d5"></a>

### `zassert_post_action()`

```c
FUNC_NORETURN void zassert_post_action ( const char * file, unsigned int line )
```

```c
#include <zephyr/sys/zassert.h>
```

断言失败时采取的终止动作（Terminal Action）。

弱符号（Weak），可覆盖（Overridable）。

<a id="gaf1c13156eb4331a95f2e396afb7736ba"></a>

### `zassert_print()`

```c
void zassert_print ( const char * fmt, ... )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/zassert.h>
```

以类似 `printf` 的形式输出断言文本（Assertion Text），经 `zassert_vprint()` 路由。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fmt` | 消息格式字符串（Message Format String）。 |
| `...` | `fmt` 的参数（Arguments）。 |

<a id="gadf431a5e2a87111d50cd268d309f3eea"></a>

### `zassert_vprint()`

```c
void zassert_vprint ( const char * fmt, va_list ap )
```

```c
#include <zephyr/sys/zassert.h>
```

输出断言文本（Assertion Text），使用 `va_list` 形式。

弱符号（Weak），可覆盖（Overridable）。

全部断言输出都经过的唯一原语（Primitive）：默认 `zassert_fail()` 和 `zassert_print()` 将文本路由到此处。覆盖它即可集中捕获或重定向每条断言消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fmt` | 消息格式字符串（Message Format String）。 |
| `ap` | `fmt` 的参数（Arguments）。 |


## 21.4\_原页交叉引用（Cross References）

- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [zephyr/sys/zassert.h](../api_file_storage_event_reference/P025_zephyr__sys__zassert.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__zassert_html_gab91fabc5db83d859e36bd6b313ec427b"></a>
<a id="agroup__zassert_html_ga9c86df1bad747a60474e5bb799218071"></a>
<a id="agroup__zassert_html_gaed3f8dc1cf2160c1f8a04f3e74f5a136"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P020_视频控制项（Video Controls）.md) · [返回大纲](大纲.md)
