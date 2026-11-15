---
id: learning.zephyr-docs.api-file-reference.page-159
title: zephyr__posix__sys__time.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2posix_2sys_2time_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第159章\_zephyr\_\_posix\_\_sys\_\_time.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2posix_2sys_2time_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <sys/types.h>
#include <sys/_timeval.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 159.1\_函数（Functions）

<a id="r_a2f316a4ad94a242df56b01953677015d"></a>

```c
int gettimeofday (struct timeval *tv, void *tz)
```

相关声明：[gettimeofday](#a2f316a4ad94a242df56b01953677015d)、[timeval](../posix_system_model_reference/P024_timeval_结构体.md)。

## 159.2\_详细说明（Detailed Documentation）

<a id="a2f316a4ad94a242df56b01953677015d"></a>

### `gettimeofday()`

```c
int gettimeofday ( struct timeval * tv, void * tz )
```


## 159.3\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [sys/_timeval.h](../api_source_reference/P001__timeval.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P093_time.h_源码浏览.md)
- [timeval](../posix_system_model_reference/P024_timeval_结构体.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P158_zephyr__posix__netinet__in.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P160_zephyr__types.h_文件参考.md)
