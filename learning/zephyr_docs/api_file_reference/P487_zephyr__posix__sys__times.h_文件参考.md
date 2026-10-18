---
id: learning.zephyr-docs.api-file-reference.page-487
title: zephyr__posix__sys__times.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/times_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第487章\_zephyr\_\_posix\_\_sys\_\_times.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/times_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <time.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 487.1\_数据结构（Data Structures）

<a id="r_tms"></a>

```c
struct tms
```

相关声明：[tms](../posix_system_model_reference/P026_tms_结构体.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 487.2\_函数（Functions）

<a id="r_a73fc89d71a97e11d44bdd0bbb851a9cb"></a>

```c
clock_t times (struct tms *buf)
```

相关声明：[clock_t](P312_zephyr__posix__posix_types.h_文件参考.md#a3b55f88f25d2c571de53a365ad658426)、[times](#a73fc89d71a97e11d44bdd0bbb851a9cb)、[tms](../posix_system_model_reference/P026_tms_结构体.md)。

## 487.3\_详细说明（Detailed Documentation）

<a id="a73fc89d71a97e11d44bdd0bbb851a9cb"></a>

### `times()`

```c
clock_t times ( struct tms * buf)
```


## 487.4\_原页交叉引用（Cross References）

- [time.h](../api_source_supplement_reference/P093_time.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P225_times.h_源码浏览.md)
- [tms](../posix_system_model_reference/P026_tms_结构体.md)
- [clock_t](P312_zephyr__posix__posix_types.h_文件参考.md#a3b55f88f25d2c571de53a365ad658426)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P486_zephyr__dt-bindings__pinctrl__ti-k3-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md)
