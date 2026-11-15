---
id: learning.zephyr-docs.api-file-reference.page-189
title: ____w__zephyr__zephyr__lib__libc__minimal__include__limits.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/limits_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第189章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_lib\_\_libc\_\_minimal\_\_include\_\_limits.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/limits_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_limits.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 189.1\_宏定义（Macros）

<a id="r_a8c13fdd8c2840edf0cb04a65297037bb"></a>

```c
#define SCHAR_MAX __SCHAR_MAX__
```

相关声明：[SCHAR_MAX](#a8c13fdd8c2840edf0cb04a65297037bb)。

<a id="r_aa05d197000ad5c143ada0fcd9379b236"></a>

```c
#define SCHAR_MIN (-SCHAR_MAX - 1)
```

相关声明：[SCHAR_MIN](#aa05d197000ad5c143ada0fcd9379b236)、[SCHAR_MAX](#a8c13fdd8c2840edf0cb04a65297037bb)。

<a id="r_a778eefd6535a9d4b752fca5dd0af58db"></a>

```c
#define CHAR_MAX SCHAR_MAX
```

相关声明：[CHAR_MAX](#a778eefd6535a9d4b752fca5dd0af58db)、[SCHAR_MAX](#a8c13fdd8c2840edf0cb04a65297037bb)。

<a id="r_a5d707bd32338557ced18c6ac76ca1b3a"></a>

```c
#define CHAR_MIN SCHAR_MIN
```

相关声明：[CHAR_MIN](#a5d707bd32338557ced18c6ac76ca1b3a)、[SCHAR_MIN](#aa05d197000ad5c143ada0fcd9379b236)。

<a id="r_a308d9dd2c0028ddb184b455bbd7865de"></a>

```c
#define CHAR_BIT __CHAR_BIT__
```

相关声明：[CHAR_BIT](#a308d9dd2c0028ddb184b455bbd7865de)。

<a id="r_a88c78a5170af546a3417d28875fd3710"></a>

```c
#define LONG_BIT (__SIZEOF_LONG__ * CHAR_BIT)
```

相关声明：[LONG_BIT](#a88c78a5170af546a3417d28875fd3710)、[CHAR_BIT](#a308d9dd2c0028ddb184b455bbd7865de)。

<a id="r_af95e2cdeed2bb68c59e2c3d07b6c3d04"></a>

```c
#define WORD_BIT (__SIZEOF_POINTER__ * CHAR_BIT)
```

相关声明：[WORD_BIT](#af95e2cdeed2bb68c59e2c3d07b6c3d04)、[CHAR_BIT](#a308d9dd2c0028ddb184b455bbd7865de)。

<a id="r_a9ec306f36d50c7375e74f0d1c55a3a67"></a>

```c
#define INT_MAX __INT_MAX__
```

相关声明：[INT_MAX](#a9ec306f36d50c7375e74f0d1c55a3a67)。

<a id="r_a1f758438cb1c7bcf55da2431f5e319e6"></a>

```c
#define SHRT_MAX __SHRT_MAX__
```

相关声明：[SHRT_MAX](#a1f758438cb1c7bcf55da2431f5e319e6)。

<a id="r_a50fece4db74f09568b2938db583c5655"></a>

```c
#define LONG_MAX __LONG_MAX__
```

相关声明：[LONG_MAX](#a50fece4db74f09568b2938db583c5655)。

<a id="r_a23ec2cf7fc07ea8f817bbac758402baf"></a>

```c
#define LLONG_MAX __LONG_LONG_MAX__
```

相关声明：[LLONG_MAX](#a23ec2cf7fc07ea8f817bbac758402baf)。

<a id="r_a21658776274b3d146c674318b635a334"></a>

```c
#define INT_MIN (-INT_MAX - 1)
```

相关声明：[INT_MIN](#a21658776274b3d146c674318b635a334)、[INT_MAX](#a9ec306f36d50c7375e74f0d1c55a3a67)。

<a id="r_ae59de266aceffa1c258ac13f45fe0d18"></a>

```c
#define SHRT_MIN (-SHRT_MAX - 1)
```

相关声明：[SHRT_MIN](#ae59de266aceffa1c258ac13f45fe0d18)、[SHRT_MAX](#a1f758438cb1c7bcf55da2431f5e319e6)。

<a id="r_ae8a44c5a7436466221e0f3859d02420f"></a>

```c
#define LONG_MIN (-LONG_MAX - 1L)
```

相关声明：[LONG_MIN](#ae8a44c5a7436466221e0f3859d02420f)、[LONG_MAX](#a50fece4db74f09568b2938db583c5655)。

<a id="r_af17a13b2ae0e9c24c020ac1f044f30c2"></a>

```c
#define LLONG_MIN (-LLONG_MAX - 1LL)
```

相关声明：[LLONG_MIN](#af17a13b2ae0e9c24c020ac1f044f30c2)、[LLONG_MAX](#a23ec2cf7fc07ea8f817bbac758402baf)。

<a id="r_a2d6569aa794c2f23e90691e60d2f3ad2"></a>

```c
#define SSIZE_MAX __INT32_MAX__
```

相关声明：[SSIZE_MAX](#a2d6569aa794c2f23e90691e60d2f3ad2)。

## 189.2\_详细说明（Detailed Documentation）

<a id="a308d9dd2c0028ddb184b455bbd7865de"></a>

### `CHAR_BIT`

```c
#define CHAR_BIT __CHAR_BIT__
```

<a id="a778eefd6535a9d4b752fca5dd0af58db"></a>

### `CHAR_MAX`

```c
#define CHAR_MAX SCHAR_MAX
```

<a id="a5d707bd32338557ced18c6ac76ca1b3a"></a>

### `CHAR_MIN`

```c
#define CHAR_MIN SCHAR_MIN
```

<a id="a9ec306f36d50c7375e74f0d1c55a3a67"></a>

### `INT_MAX`

```c
#define INT_MAX __INT_MAX__
```

<a id="a21658776274b3d146c674318b635a334"></a>

### `INT_MIN`

```c
#define INT_MIN (-INT_MAX - 1)
```

<a id="a23ec2cf7fc07ea8f817bbac758402baf"></a>

### `LLONG_MAX`

```c
#define LLONG_MAX __LONG_LONG_MAX__
```

<a id="af17a13b2ae0e9c24c020ac1f044f30c2"></a>

### `LLONG_MIN`

```c
#define LLONG_MIN (-LLONG_MAX - 1LL)
```

<a id="a88c78a5170af546a3417d28875fd3710"></a>

### `LONG_BIT`

```c
#define LONG_BIT (__SIZEOF_LONG__ * CHAR_BIT)
```

<a id="a50fece4db74f09568b2938db583c5655"></a>

### `LONG_MAX`

```c
#define LONG_MAX __LONG_MAX__
```

<a id="ae8a44c5a7436466221e0f3859d02420f"></a>

### `LONG_MIN`

```c
#define LONG_MIN (-LONG_MAX - 1L)
```

<a id="a8c13fdd8c2840edf0cb04a65297037bb"></a>

### `SCHAR_MAX`

```c
#define SCHAR_MAX __SCHAR_MAX__
```

<a id="aa05d197000ad5c143ada0fcd9379b236"></a>

### `SCHAR_MIN`

```c
#define SCHAR_MIN (-SCHAR_MAX - 1)
```

<a id="a1f758438cb1c7bcf55da2431f5e319e6"></a>

### `SHRT_MAX`

```c
#define SHRT_MAX __SHRT_MAX__
```

<a id="ae59de266aceffa1c258ac13f45fe0d18"></a>

### `SHRT_MIN`

```c
#define SHRT_MIN (-SHRT_MAX - 1)
```

<a id="a2d6569aa794c2f23e90691e60d2f3ad2"></a>

### `SSIZE_MAX`

```c
#define SSIZE_MAX __INT32_MAX__
```

<a id="af95e2cdeed2bb68c59e2c3d07b6c3d04"></a>

### `WORD_BIT`

```c
#define WORD_BIT (__SIZEOF_POINTER__ * CHAR_BIT)
```


## 189.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_limits.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__limits_8h_source.html)
- [查看此文件的源码。](../api_source_runtime_reference/P039_limits.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P188_zephyr__sys__libc-hooks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P190_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_toolchain__llvm.h_文件参考.md)
