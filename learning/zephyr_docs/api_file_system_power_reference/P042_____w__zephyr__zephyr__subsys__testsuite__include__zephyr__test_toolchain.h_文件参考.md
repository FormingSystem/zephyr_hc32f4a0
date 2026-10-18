---
id: learning.zephyr-docs.api-file-system-power-reference.page-42
title: ____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_toolchain.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/test__toolchain_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_testsuite\_\_include\_\_zephyr\_\_test\_toolchain.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/test__toolchain_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/toolchain.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 42.1\_宏定义（Macros）

<a id="r_a46a35ee1419f878aff6c4502a82fdad4"></a>

```c
#define TOOLCHAIN_WARNING_ALLOC_SIZE_LARGER_THAN
```

相关声明：[TOOLCHAIN_WARNING_ALLOC_SIZE_LARGER_THAN](#a46a35ee1419f878aff6c4502a82fdad4)。

针对分配大小超过给定值的工具链专用警告（Toolchain-specific Warning for Oversized Allocations）。

<a id="r_a41da25e145e8172cebcbbf31e0b79e17"></a>

```c
#define TOOLCHAIN_WARNING_DANGLING_POINTER
```

相关声明：[TOOLCHAIN_WARNING_DANGLING_POINTER](#a41da25e145e8172cebcbbf31e0b79e17)。

针对悬空指针（Dangling Pointers）的工具链专用警告。

<a id="r_ad3a914654f83a6490de9a84d090af496"></a>

```c
#define TOOLCHAIN_WARNING_FORMAT_TRUNCATION
```

相关声明：[TOOLCHAIN_WARNING_FORMAT_TRUNCATION](#ad3a914654f83a6490de9a84d090af496)。

针对格式化截断（Format Truncation）的工具链专用警告。

<a id="r_a01fd2ae9418bafbedeaa4f3aeea9b3a3"></a>

```c
#define TOOLCHAIN_WARNING_INFINITE_RECURSION
```

相关声明：[TOOLCHAIN_WARNING_INFINITE_RECURSION](#a01fd2ae9418bafbedeaa4f3aeea9b3a3)。

针对无限递归（Infinite Recursion）的工具链专用警告。

<a id="r_af1ec5706645d6b33ee0781b5e1127796"></a>

```c
#define TOOLCHAIN_WARNING_INTEGER_OVERFLOW
```

相关声明：[TOOLCHAIN_WARNING_INTEGER_OVERFLOW](#af1ec5706645d6b33ee0781b5e1127796)。

针对整数溢出（Integer Overflow）的工具链专用警告。

<a id="r_a4c9cbe2de87a179f951f6d10d0d919fd"></a>

```c
#define TOOLCHAIN_WARNING_OVERFLOW
```

相关声明：[TOOLCHAIN_WARNING_OVERFLOW](#a4c9cbe2de87a179f951f6d10d0d919fd)。

针对整数溢出（Integer Overflow）的工具链专用警告。

<a id="r_a78adf404c8b66e41066126c0221bd334"></a>

```c
#define TOOLCHAIN_WARNING_PRAGMAS
```

相关声明：[TOOLCHAIN_WARNING_PRAGMAS](#a78adf404c8b66e41066126c0221bd334)。

针对未知编译指示（Unknown Pragmas）的工具链专用警告。

<a id="r_a056ed97bac0f04be423885dc21b9df00"></a>

```c
#define TOOLCHAIN_WARNING_SIZEOF_ARRAY_DECAY
```

相关声明：[TOOLCHAIN_WARNING_SIZEOF_ARRAY_DECAY](#a056ed97bac0f04be423885dc21b9df00)。

针对 `sizeof` 中数组退化（Array Decay）的工具链专用警告。

<a id="r_ac45e9e7740ee6c5e20e0ec813499dad5"></a>

```c
#define TOOLCHAIN_WARNING_STRINGOP_OVERFLOW
```

相关声明：[TOOLCHAIN_WARNING_STRINGOP_OVERFLOW](#ac45e9e7740ee6c5e20e0ec813499dad5)。

针对字符串操作溢出（Stringop Overflow）的工具链专用警告。

<a id="r_a83c3c63db289d6024c809840492bce08"></a>

```c
#define TOOLCHAIN_WARNING_STRINGOP_TRUNCATION
```

相关声明：[TOOLCHAIN_WARNING_STRINGOP_TRUNCATION](#a83c3c63db289d6024c809840492bce08)。

针对字符串操作截断（Stringop Truncation）的工具链专用警告。

<a id="r_af90e0047b2708d02d3f69cd019a584df"></a>

```c
#define TOOLCHAIN_WARNING_UNUSED_FUNCTION
```

相关声明：[TOOLCHAIN_WARNING_UNUSED_FUNCTION](#af90e0047b2708d02d3f69cd019a584df)。

针对未使用函数（Unused Function）的工具链专用警告。

## 42.2\_详细说明（Detailed Documentation）

<a id="a46a35ee1419f878aff6c4502a82fdad4"></a>

### `TOOLCHAIN_WARNING_ALLOC_SIZE_LARGER_THAN`

```c
#define TOOLCHAIN_WARNING_ALLOC_SIZE_LARGER_THAN
```

针对分配大小超过给定值的工具链专用警告（Toolchain-specific Warning for Oversized Allocations）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="a41da25e145e8172cebcbbf31e0b79e17"></a>

### `TOOLCHAIN_WARNING_DANGLING_POINTER`

```c
#define TOOLCHAIN_WARNING_DANGLING_POINTER
```

针对悬空指针（Dangling Pointers）的工具链专用警告。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="ad3a914654f83a6490de9a84d090af496"></a>

### `TOOLCHAIN_WARNING_FORMAT_TRUNCATION`

```c
#define TOOLCHAIN_WARNING_FORMAT_TRUNCATION
```

针对格式化截断（Format Truncation）的工具链专用警告。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="a01fd2ae9418bafbedeaa4f3aeea9b3a3"></a>

### `TOOLCHAIN_WARNING_INFINITE_RECURSION`

```c
#define TOOLCHAIN_WARNING_INFINITE_RECURSION
```

针对无限递归（Infinite Recursion）的工具链专用警告。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="af1ec5706645d6b33ee0781b5e1127796"></a>

### `TOOLCHAIN_WARNING_INTEGER_OVERFLOW`

```c
#define TOOLCHAIN_WARNING_INTEGER_OVERFLOW
```

针对整数溢出（Integer Overflow）的工具链专用警告。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="a4c9cbe2de87a179f951f6d10d0d919fd"></a>

### `TOOLCHAIN_WARNING_OVERFLOW`

```c
#define TOOLCHAIN_WARNING_OVERFLOW
```

针对整数溢出（Integer Overflow）的工具链专用警告。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="a78adf404c8b66e41066126c0221bd334"></a>

### `TOOLCHAIN_WARNING_PRAGMAS`

```c
#define TOOLCHAIN_WARNING_PRAGMAS
```

针对未知编译指示（Unknown Pragmas）的工具链专用警告。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="a056ed97bac0f04be423885dc21b9df00"></a>

### `TOOLCHAIN_WARNING_SIZEOF_ARRAY_DECAY`

```c
#define TOOLCHAIN_WARNING_SIZEOF_ARRAY_DECAY
```

针对 `sizeof` 中数组退化（Array Decay）的工具链专用警告。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="ac45e9e7740ee6c5e20e0ec813499dad5"></a>

### `TOOLCHAIN_WARNING_STRINGOP_OVERFLOW`

```c
#define TOOLCHAIN_WARNING_STRINGOP_OVERFLOW
```

针对字符串操作溢出（Stringop Overflow）的工具链专用警告。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="a83c3c63db289d6024c809840492bce08"></a>

### `TOOLCHAIN_WARNING_STRINGOP_TRUNCATION`

```c
#define TOOLCHAIN_WARNING_STRINGOP_TRUNCATION
```

针对字符串操作截断（Stringop Truncation）的工具链专用警告。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="af90e0047b2708d02d3f69cd019a584df"></a>

### `TOOLCHAIN_WARNING_UNUSED_FUNCTION`

```c
#define TOOLCHAIN_WARNING_UNUSED_FUNCTION
```

针对未使用函数（Unused Function）的工具链专用警告。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。


## 42.3\_原页交叉引用（Cross References）

- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P861_test_toolchain.h_源码浏览.md)
- [TOOLCHAIN_DISABLE_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga1f08471f8dba6ce2a3e0f38bea73d7b5)
- [TOOLCHAIN_ENABLE_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga5365fdbb6323f48ddca9ab4149e9a561)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P041_zephyr__drivers__sensor__tdk_apex.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P043_zephyr__mgmt__mcumgr__grp__transport_mgmt__transport_mgmt.h_文件参考.md)
