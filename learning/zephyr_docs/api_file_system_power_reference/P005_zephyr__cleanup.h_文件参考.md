---
id: learning.zephyr-docs.api-file-system-power-reference.page-5
title: zephyr__cleanup.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cleanup_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_cleanup.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cleanup_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors SPDX-License-Identifier: Apache-2.0.

<a id="details"></a>

```c
#include <zephyr/toolchain.h>
```

查看此文件的源码。

`SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors`；`SPDX-License-Identifier: Apache-2.0`。清理辅助 API 接口（Cleanup Helper API Interface）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_ga4faf2c585a3fa2ce28480a5e2805ca8b"></a>

```c
#define SCOPE_VAR_DEFINE(_name, _type, _exit_fn, _init_fn, ...)
```

相关声明：[SCOPE_VAR_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga4faf2c585a3fa2ce28480a5e2805ca8b)。

定义作用域变量类型（Scoped Variable Type）。

<a id="r_gab584b9adf45e13376c0f8e0b817a6213"></a>

```c
#define SCOPE_GUARD_DEFINE(_name, _type, _lock, _unlock)
```

相关声明：[SCOPE_GUARD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#gab584b9adf45e13376c0f8e0b817a6213)。

定义作用域守卫类型（Scoped Guard Type）。

<a id="r_ga88752a55762b11e721c3052c6adc401a"></a>

```c
#define SCOPE_COND_GUARD_DEFINE(_name, _type, _try_lock, _unlock)
```

相关声明：[SCOPE_COND_GUARD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga88752a55762b11e721c3052c6adc401a)。

定义条件式、可失败的作用域守卫类型（Conditional/Failable Scoped Guard Type）。

<a id="r_ga07847cc6bb3cd5f63b4d05e084eb9203"></a>

```c
#define SCOPE_DEFER_DEFINE(_func, ...)
```

相关声明：[SCOPE_DEFER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga07847cc6bb3cd5f63b4d05e084eb9203)。

定义作用域延后执行类型（Scoped Defer Type）。

<a id="r_ga62362f13860dbea4361e7cf149801d3f"></a>

```c
#define scope_var(_name, _var)
```

相关声明：[scope_var](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga62362f13860dbea4361e7cf149801d3f)。

声明具有自动清理（Automatic Cleanup）功能的变量。

<a id="r_ga096c421f2ba9d7acd68039d493a80b63"></a>

```c
#define scope_var_init(_name, _var, _init_expr)
```

相关声明：[scope_var_init](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga096c421f2ba9d7acd68039d493a80b63)。

通过直接初始化（Direct Initialization）声明具有自动清理（Automatic Cleanup）功能的变量。

<a id="r_ga3905160905199178d29b66084f237f4e"></a>

```c
#define scope_guard(_name)
```

相关声明：[scope_guard](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga3905160905199178d29b66084f237f4e)。

获取作用域守卫锁（Scoped Guard Lock）。

<a id="r_gad7807c92614173dacfe7af2ca6a572ab"></a>

```c
#define scoped_guard(_name, ...)
```

相关声明：[scoped_guard](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#gad7807c92614173dacfe7af2ca6a572ab)。

为随后代码块的生命周期（Lifetime）获取守卫（Guard）。

<a id="r_ga1f5c0f74610d1bbcc1fd3c7914ab9a7c"></a>

```c
#define scoped_cond_guard(_name, _fail, ...)
```

相关声明：[scoped_cond_guard](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga1f5c0f74610d1bbcc1fd3c7914ab9a7c)。

为随后代码块的生命周期（Lifetime）有条件地获取守卫（Guard）。

<a id="r_ga5ea0ef9eed956fa112b069d87f8b05e5"></a>

```c
#define scope_defer(_name)
```

相关声明：[scope_defer](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga5ea0ef9eed956fa112b069d87f8b05e5)。

注册作用域延后调用（Scoped Deferred Call）。


## 5.2\_原页交叉引用（Cross References）

- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P008_cleanup.h_源码浏览.md)
- [SCOPE_VAR_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga4faf2c585a3fa2ce28480a5e2805ca8b)
- [SCOPE_GUARD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#gab584b9adf45e13376c0f8e0b817a6213)
- [SCOPE_COND_GUARD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga88752a55762b11e721c3052c6adc401a)
- [SCOPE_DEFER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga07847cc6bb3cd5f63b4d05e084eb9203)
- [scope_var](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga62362f13860dbea4361e7cf149801d3f)
- [scope_var_init](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga096c421f2ba9d7acd68039d493a80b63)
- [scope_guard](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga3905160905199178d29b66084f237f4e)
- [scoped_guard](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#gad7807c92614173dacfe7af2ca6a572ab)
- [scoped_cond_guard](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga1f5c0f74610d1bbcc1fd3c7914ab9a7c)
- [scope_defer](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga5ea0ef9eed956fa112b069d87f8b05e5)

<a id="header-details"></a>

---

[上一章](P004_zephyr__drivers__charger.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__dma__dma_bee.h_文件参考.md)
