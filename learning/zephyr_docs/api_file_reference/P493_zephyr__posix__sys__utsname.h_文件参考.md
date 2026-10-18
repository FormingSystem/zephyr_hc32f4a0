---
id: learning.zephyr-docs.api-file-reference.page-493
title: zephyr__posix__sys__utsname.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/utsname_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第493章\_zephyr\_\_posix\_\_sys\_\_utsname.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/utsname_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 493.1\_数据结构（Data Structures）

<a id="r_utsname"></a>

```c
struct utsname
```

相关声明：[utsname](../posix_system_model_reference/P028_utsname_结构体.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 493.2\_函数（Functions）

<a id="r_a1ad7a68f28b58669758da1b12061a81f"></a>

```c
int uname (struct utsname *name)
```

相关声明：[uname](#a1ad7a68f28b58669758da1b12061a81f)、[utsname](../posix_system_model_reference/P028_utsname_结构体.md)。

## 493.3\_详细说明（Detailed Documentation）

<a id="a1ad7a68f28b58669758da1b12061a81f"></a>

### `uname()`

```c
int uname ( struct utsname * name)
```


## 493.4\_原页交叉引用（Cross References）

- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P241_utsname.h_源码浏览.md)
- [utsname](../posix_system_model_reference/P028_utsname_结构体.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P492_zephyr__posix__unistd.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P494_zephyr__net__virtual_mgmt.h_文件参考.md)
