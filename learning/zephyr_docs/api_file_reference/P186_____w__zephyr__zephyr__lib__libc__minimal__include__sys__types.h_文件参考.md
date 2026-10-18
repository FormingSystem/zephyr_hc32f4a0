---
id: learning.zephyr-docs.api-file-reference.page-186
title: ____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第186章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_lib\_\_libc\_\_minimal\_\_include\_\_sys\_\_types.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <sys/_types.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 186.1\_宏定义（Macros）

<a id="r_a4089fb16419d359081465355db05f846"></a>

```c
#define unsigned signed /* parasoft-suppress MISRAC2012-RULE_20_4-a MISRAC2012-RULE_20_4-b */
```

相关声明：[unsigned](#a4089fb16419d359081465355db05f846)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 186.2\_类型定义（Typedefs）

<a id="r_adb8322e115035a284aab704909e63d00"></a>

```c
typedef unsigned int mode_t
```

相关声明：[unsigned](#a4089fb16419d359081465355db05f846)、[mode_t](#adb8322e115035a284aab704909e63d00)。

<a id="r_a5c5d83d87790efd59ea916c2b99f9118"></a>

```c
typedef __SIZE_TYPE__ ssize_t
```

相关声明：[ssize_t](#a5c5d83d87790efd59ea916c2b99f9118)。

<a id="r_a98a5cc5f4a350bf5652565021a2f239f"></a>

```c
typedef __INTPTR_TYPE__ off_t
```

相关声明：[off_t](#a98a5cc5f4a350bf5652565021a2f239f)。

## 186.3\_详细说明（Detailed Documentation）

<a id="a4089fb16419d359081465355db05f846"></a>

### `unsigned`

```c
#define unsigned signed /* parasoft-suppress MISRAC2012-RULE_20_4-a MISRAC2012-RULE_20_4-b */
```

<a id="adb8322e115035a284aab704909e63d00"></a>

### `mode_t`

```c
typedef unsigned int mode_t
```

<a id="a98a5cc5f4a350bf5652565021a2f239f"></a>

### `off_t`

```c
typedef __INTPTR_TYPE__ off_t
```

<a id="a5c5d83d87790efd59ea916c2b99f9118"></a>

### `ssize_t`

```c
typedef __SIZE_TYPE__ ssize_t
```


## 186.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [sys/_types.h](../api_source_supplement_reference/P001__types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P038_types.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P185_zephyr__net__prometheus__label.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P187_____w__zephyr__zephyr__lib__libc__minimal__include__time.h_文件参考.md)
