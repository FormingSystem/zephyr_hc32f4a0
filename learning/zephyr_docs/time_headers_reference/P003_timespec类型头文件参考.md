---
id: learning.zephyr-docs.time-headers-reference.page-3
title: timespec类型头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/__timespec_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_timespec类型头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/__timespec_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入最小C库时间类型、系统时钟兼容入口和网络长超时参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

```c
#include <sys/_types.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_timespec"></a>

```c
struct timespec
```

相关声明：[timespec](P005_timespec时间结构.md)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.2\_类型定义（Typedefs）

<a id="r_aa17c461cd5eca7fc12a66daa803c7fd7"></a>

```c
typedef _TIME_T_ time_t
```

相关声明：[time_t](#aa17c461cd5eca7fc12a66daa803c7fd7)。

<a id="r_ad7acf95ceafb15a1d8d86af0c4982995"></a>

```c
typedef _SUSECONDS_T_ suseconds_t
```

相关声明：[suseconds_t](#ad7acf95ceafb15a1d8d86af0c4982995)。

## 3.3\_详细说明（Detailed Documentation）

<a id="ad7acf95ceafb15a1d8d86af0c4982995"></a>

### `suseconds_t`

```c
typedef _SUSECONDS_T_ suseconds_t
```

<a id="aa17c461cd5eca7fc12a66daa803c7fd7"></a>

### `time_t`

```c
typedef _TIME_T_ time_t
```

## 3.4\_源码定位与版本边界

相对源码定位：[timespec类型头文件](../../../lib/libc/minimal/include/sys/_timespec.h)、[底层类型](../../../lib/libc/minimal/include/sys/_types.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中保存摘要的官方main文件。译文与仓库内已有源码采用相对链接，不依赖作者机器位置；不同C库和构建配置须分别核对。

> 译注——源码核对：本次最小C库的time_t来自_TIME_T_，后者在sys/_types.h中定义为int64_t；suseconds_t来自int32_t的_SUSECONDS_T_。这些是该C库的具体类型，不应推广到所有外部C库或任意ABI。tv_nsec声明为long，不能把time_t和纳秒字段当作必然同宽。

> 译注——源码核对：结构体声明本身不会校验或规范化数值。Zephyr时间工具以0 ≤ tv_nsec < 10^9作为规范化条件（Normalization）；tv_sec为秒，tv_nsec为该秒内纳秒部分。类型不携带时钟标识（Clock ID）或纪元（Epoch），绝对时间与相对时长要由使用它的API决定。

> 译注——源码核对：_timespec.h用__time_t_defined、__suseconds_t_defined和两种timespec保护宏避免重复定义。Doxygen把同名timespec的多个来源汇到一个结构页，不意味着应用应同时手工包含不同C库的实现头文件。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.5\_原页交叉引用（Cross References）

- [sys/_types.h](https://docs.zephyrproject.org/latest/doxygen/html/__types_8h_source.html)
- [查看此文件的源码](P004_timespec类型头文件源码.md)
- [timespec](P005_timespec时间结构.md)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P002_最小C库定时规格头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_timespec类型头文件源码.md)
